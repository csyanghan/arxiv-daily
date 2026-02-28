import os
import re
import json
import time
import requests
import datetime
from bs4 import BeautifulSoup
from openai import OpenAI
import logging

# 配置 - 固定值
LIST_URL = "https://arxiv.org/list/cs/new"
TOPICS = ["化学大模型", "质谱结构推理"]
MODEL = "deepseek-chat"
HISTORY_PATH = "data/history.json"
OUTPUT_FILE = "README.md"

logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S',
                    level=logging.INFO)


def normalize_whitespace(text):
    """清理空白字符"""
    return re.sub(r"\s+", " ", text or "").strip()

def parse_submitted_date(raw_line):
    """解析提交日期"""
    if not raw_line:
        return None
    match = re.search(r"Submitted on\s+([0-9]{1,2}\s+\w+\s+[0-9]{4})", raw_line)
    if not match:
        return None
    raw_date = match.group(1).strip()
    for fmt in ("%d %b %Y", "%d %B %Y"):
        try:
            parsed = datetime.datetime.strptime(raw_date, fmt)
            return parsed.strftime("%Y-%m-%d")
        except ValueError:
            continue
    return raw_date

def fetch_papers():
    """抓取arxiv论文列表"""
    logging.info(f"正在抓取: {LIST_URL}")
    resp = requests.get(LIST_URL, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    
    papers = []
    for dt in soup.find_all("dt"):
        dd = dt.find_next_sibling("dd")
        if not dd:
            continue
            
        link = dt.find("a", title="Abstract")
        if not link:
            continue
            
        arxiv_id = link.text.replace("arXiv:", "").strip()
        
        # 标题
        title_node = dd.find("div", class_="list-title")
        title = normalize_whitespace(title_node.get_text(" ", strip=True).replace("Title:", "", 1)) if title_node else arxiv_id
        
        # 作者
        author_links = dd.select("div.list-authors a")
        authors = [normalize_whitespace(a.get_text()) for a in author_links]
        
        # 摘要
        abstract_node = dd.find("p", class_="mathjax")
        abstract = normalize_whitespace(abstract_node.get_text(" ", strip=True).replace("Abstract:", "", 1)) if abstract_node else ""
        
        # 提交日期
        submitted = None
        submitted_node = dd.find("div", class_="list-submitted")
        if submitted_node:
            submitted = parse_submitted_date(normalize_whitespace(submitted_node.get_text(" ", strip=True)))
        
        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "authors": authors,
            "abstract": abstract,
            "link": f"https://arxiv.org/abs/{arxiv_id}",
            "pdf_link": f"https://arxiv.org/pdf/{arxiv_id}.pdf",
            "submitted": submitted
        })
    
    logging.info(f"抓取到 {len(papers)} 篇论文")
    return papers

def analyze_papers(papers):
    """调用大模型分析论文"""
    if not papers:
        return []
    
    # 从环境变量获取API key
    api_key = os.environ.get("DEEPSEEK_API_KEY")
    if not api_key:
        raise Exception("请设置 DEEPSEEK_API_KEY 环境变量")
    
    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("DEEPSEEK_API_BASE", "https://api.deepseek.com")
    )
    
    # 分批处理，避免token超限
    chunk_size = 100
    all_results = []
    
    for i in range(0, len(papers), chunk_size):
        time.sleep(3)
        chunk = papers[i:i+chunk_size]
        
        # 准备数据
        topics_text = "\n".join(f"- {t}" for t in TOPICS)
        papers_data = [{"arxiv_id": p["arxiv_id"], "title": p["title"], "abstract": p["abstract"]} for p in chunk]
        
        prompt = f"""你是一位在【化学信息学】和【质谱分析】领域的科研专家。请筛选出与指定研究主题相关的论文。

【重点关注主题】
{topics_text}

【相关性判断标准】（满足任意一条即可视为相关）：
1. ✅ 核心主题相关：论文的主要研究内容直接围绕这些主题
2. ✅ 数据资源相关：论文提供了可用于这些主题的数据集、资源或工具
3. ✅ 综述展望相关：论文是专门针对这些主题的综述，或包含重要的相关讨论

【筛选原则】
- 只要满足上述任一标准，即可纳入
- 不需要论文同时满足多个标准
- 包容性筛选，但需要确实相关（不是完全无关）
- 综述类论文如果是专门针对这些主题，或包含重要章节讨论这些主题，也应纳入

请分析以下论文列表，筛选出【相关】的论文。对于每篇相关论文，需要说明它满足了哪条标准。

输出格式必须是严格的JSON：
{{
    "results": [
        {{
            "arxiv_id": "论文ID",
            "zh_summary": "500字以内的中文摘要总结，突出论文与关注主题相关的内容",
            "relevance_reason": "说明这篇论文的相关性，指出满足了哪条标准（例如：'满足标准2：提出的图神经网络方法可用于质谱结构推理'）"
        }}
    ]
}}

如果没有相关论文，请返回空的results列表：{{"results": []}}

论文列表：
{json.dumps(papers_data, ensure_ascii=False, indent=2)}"""

        # 调用API（带重试）
        for attempt in range(3):
            try:
                logging.info(f"正在分析第 {i//chunk_size + 1}/{(len(papers)-1)//chunk_size + 1} 批，共 {len(chunk)} 篇...")
                
                response = client.chat.completions.create(
                    model=MODEL,
                    temperature=0.6,
                    messages=[
                        {"role": "system", "content": """你是一个科研论文筛选助手。你的特点是：
1. 按照给定的相关性标准筛选论文
2. 只要满足任意一条标准即可纳入
3. 对每篇选中的论文都要明确指出满足了哪条标准
4. 筛选要合理，不要过度筛选，也不要漏掉明显相关的论文"""},
                        {"role": "user", "content": prompt}
                    ]
                )
                
                content = response.choices[0].message.content
                
                # 提取JSON
                json_match = re.search(r"\{[\s\S]*\}", content)
                if json_match:
                    result = json.loads(json_match.group())
                    results = result.get("results", [])
                    
                    # 简单检查：如果选中比例过低，提醒但继续
                    if len(results) == 0 and len(chunk) > 10:
                        logging.info(f"ℹ️ 提示：此批次未选中任何论文")
                    
                    all_results.extend(results)
                    logging.info(f"✅ 此批次筛选出 {len(results)} 篇相关论文")
                    break
                else:
                    logging.info("无法解析模型输出")
                    
            except Exception as e:
                logging.error(f"调用失败 (尝试 {attempt+1}/3): {e}")
                if attempt == 2:
                    logging.info(f"跳过此批次")
                else:
                    time.sleep(2 ** attempt)
    
    # 去重处理
    seen_ids = set()
    unique_results = []
    for r in all_results:
        if r["arxiv_id"] not in seen_ids:
            seen_ids.add(r["arxiv_id"])
            unique_results.append(r)
    
    logging.info(f"\n📊 筛选完成，总共找到 {len(unique_results)} 篇相关论文")
    return unique_results        

def load_history():
    """加载历史记录"""
    history = {}
    if os.path.exists(HISTORY_PATH):
        try:
            with open(HISTORY_PATH, "r", encoding="utf-8") as f:
                history = json.load(f)
            logging.info(f"加载历史记录，共 {len(history)} 天")
        except:
            logging.error("历史文件不存在或损坏，创建新的历史记录")
    return history

def save_history(history):
    """保存历史记录"""
    # 创建目录
    os.makedirs(os.path.dirname(HISTORY_PATH), exist_ok=True)
    
    # 保存
    with open(HISTORY_PATH, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    
    logging.info(f"历史记录已保存到 {HISTORY_PATH}")

def generate_readme(today_papers):
    """生成README，当天最新的内容插入到最前面"""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # 读取现有的 README 内容
    existing_content = ""
    if os.path.exists(OUTPUT_FILE):
        try:
            with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
                existing_content = f.read()
            logging.info("读取现有 README 文件")
        except Exception as e:
            logging.error(f"读取现有 README 失败: {e}")
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        # 写入标题和更新时间（始终保留在最上面）
        f.write("# 📚 ArXiv 论文日报\n\n")
        f.write(f"> 每天自动更新，关注 **{', '.join(TOPICS)}** 相关的最新论文\n\n")
        
        f.write("## 更新时间\n")
        f.write(f"⏰ {now}\n\n")
        
        # 写入当天的论文（最新的）
        f.write(f"## 📅 {today} (今日最新)\n\n")
        
        if not today_papers:
            f.write("> 今日没有找到相关论文\n\n")
        else:
            f.write(f"**相关论文数：{len(today_papers)}**\n\n")
            
            for i, paper in enumerate(today_papers, 1):
                f.write(f"### {i}. [{paper['title']}]({paper['link']})\n\n")
                
                # 基本信息
                f.write("**基本信息**\n\n")
                f.write(f"- 🔗 arXiv: [`{paper['arxiv_id']}`]({paper['link']})\n")
                if paper.get('submitted'):
                    f.write(f"- 📅 提交日期: {paper['submitted']}\n")
                if paper.get('authors'):
                    authors_display = ', '.join(paper['authors'][:3])
                    if len(paper['authors']) > 3:
                        authors_display += f" 等{len(paper['authors'])}人"
                    f.write(f"- 👥 作者: {authors_display}\n")
                f.write(f"- 📄 PDF: [下载]({paper['pdf_link']})\n\n")
                
                # 相关性分析
                if paper.get('relevance_reason'):
                    f.write("**💡 相关性分析**\n\n")
                    f.write(f"{paper['relevance_reason']}\n\n")
                
                # 中文摘要
                if paper.get('zh_summary'):
                    f.write("**📖 中文摘要**\n\n")
                    f.write(f"{paper['zh_summary']}\n\n")
                
                # 原文摘要（可折叠）
                f.write("<details>\n")
                f.write("<summary><b>🔍 查看原文摘要</b></summary>\n\n")
                f.write(f"{paper['abstract']}\n\n")
                f.write("</details>\n\n")
                
                f.write("---\n\n")
        
        # 写入历史统计（如果存在现有内容，提取并更新统计）
        f.write("## 📊 数据统计\n")
        
        # 从现有内容中提取历史数据
        total_days = 1  # 当前这一天
        total_papers = len(today_papers)
        
        if existing_content:
            # 尝试从现有内容中提取统计数据
            stats_pattern = r"- 累计运行天数：(\d+)\n- 累计论文数量：(\d+)"
            stats_match = re.search(stats_pattern, existing_content)
            if stats_match:
                total_days = int(stats_match.group(1)) + 1
                total_papers = int(stats_match.group(2)) + len(today_papers)
        
        f.write(f"- 累计运行天数：{total_days}\n")
        f.write(f"- 累计论文数量：{total_papers}\n\n")
        
        # 写入历史记录（如果存在现有内容，保留之前的内容）
        if existing_content:
            # 查找历史记录的起始位置
            history_start = existing_content.find("## 📊 数据统计")
            if history_start != -1:
                # 找到数据统计部分之后的内容
                after_stats = existing_content[history_start:]
                # 找到第一个历史日期标题
                date_start = after_stats.find("## 📅")
                if date_start != -1:
                    # 保留从历史日期开始的所有内容
                    historical_content = after_stats[date_start:]
                    f.write(historical_content)
                else:
                    # 如果没有找到历史日期，则写入新的历史记录部分
                    f.write("## 📝 历史记录\n\n")
                    f.write("> 暂无历史数据\n\n")
            else:
                # 如果没有找到数据统计部分，则写入新的历史记录部分
                f.write("## 📝 历史记录\n\n")
                f.write("> 暂无历史数据\n\n")
        else:
            # 如果没有现有内容，写入空的历史记录
            f.write("## 📝 历史记录\n\n")
            f.write("> 暂无历史数据\n\n")
    
    logging.info(f"README 已更新，今日添加 {len(today_papers)} 篇论文")

def main():
    """主函数"""
    try:
        logging.info("="*50)
        logging.info("开始抓取 arXiv 论文")
        logging.info("="*50)
        
        # 1. 加载历史记录
        history = load_history()
        
        # 2. 抓取论文
        papers = fetch_papers()

        # papers = papers[:100]  # 取前100篇，避免过多无关论文干扰分析

        logging.info(f"抓取到 {len(papers)} 篇论文，准备分析...")
        
        # 3. 大模型分析
        results = analyze_papers(papers)
        
        # 4. 合并数据
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        result_dict = {r["arxiv_id"]: r for r in results}
        today_papers = []
        
        for paper in papers:
            if paper["arxiv_id"] in result_dict:
                today_papers.append({
                    **paper,
                    "zh_summary": result_dict[paper["arxiv_id"]].get("zh_summary", ""),
                    "relevance_reason": result_dict[paper["arxiv_id"]].get("relevance_reason", "")
                })
        
        # 5. 更新历史记录
        history[today] = today_papers
        save_history(history)
        
        # 6. 生成README（最新的在上面）
        generate_readme(today_papers)
        
        logging.info("="*50)
        logging.info(f"✅ 运行完成！")
        logging.info(f"📊 今日抓取: {len(papers)} 篇")
        logging.info(f"🎯 今日相关: {len(today_papers)} 篇")
        logging.info(f"📚 累计天数: {len(history)} 天")
        logging.info(f"📝 README 已更新")
        logging.info("="*50)
        
    except Exception as e:
        logging.error(f"❌ 运行失败: {e}")
        raise

if __name__ == "__main__":
    main()
