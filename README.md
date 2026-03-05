# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-05 01:26:00

## 📅 2026-03-05 (今日最新)

**相关论文数：83**

### 1. [RxnNano:Training Compact LLMs for Chemical Reaction and Retrosynthesis Prediction via Hierarchical Curriculum Learning](https://arxiv.org/abs/2603.02215)

**基本信息**

- 🔗 arXiv: [`2603.02215`](https://arxiv.org/abs/2603.02215)
- 👥 作者: Ran Li, Shimin Di, Haowei LI 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02215.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕“化学大模型”这一主题，提出了一个用于化学反应预测的紧凑型LLM训练框架RxnNano，并进行了性能验证。

**📖 中文摘要**

本文提出RxnNano，一个用于化学反应和逆合成预测的紧凑型大语言模型（LLM）训练框架。该研究直接针对化学信息学领域的核心挑战，即如何将深层化学直觉（如反应常识和拓扑原子映射逻辑）注入模型，而非仅仅依赖参数和数据规模的扩展。其核心创新包括：1）一个“潜在化学一致性”目标，将反应建模为连续化学流形上的运动，确保可逆且物理上合理的转化；2）一个“分层认知课程”，通过从语法掌握到语义推理的渐进阶段训练模型，构建稳健的化学直觉；3）“原子映射置换不变性”，迫使模型学习不变的关系拓扑并平衡多任务学习。该工作开发的0.5B参数模型RxnNano在严格基准测试中显著优于更大的微调LLM和所有领域基线，实现了23.5%的Top-1准确率提升。该论文的核心研究内容直接围绕“化学大模型”这一主题，属于化学信息学领域的前沿模型开发工作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical reaction prediction is pivotal for accelerating drug discovery and synthesis planning. Despite advances in data-driven models, current approaches are hindered by an overemphasis on parameter and dataset scaling. Some methods coupled with evaluation techniques that bypass fundamental challenges in reaction representation and fail to capture deep chemical intuition like reaction common sense and {topological atom mapping logic}. We argue that the core challenge lies in instilling these knowledge into the models. To this end, we propose a unified framework that prioritizes chemical understanding over scale through three key innovations: (1) a {Latent Chemical Consistency} objective that models reactions as movements on a continuous chemical manifold, ensuring reversible and physically plausible transformations; (2) a {Hierarchical Cognitive Curriculum} that trains the model through progressive stages, from syntax mastery to semantic reasoning, building robust chemical intuition; (3) {Atom-Map Permutation Invariance (AMPI)}, which force the model to learn invariant relational topology and balance multi-task learning. (4)and structured plan-based reasoning to improve the performance of the LLMs. Our compact {0.5B-parameter model}, \textbf{RxnNano} significantly outperforms fine-tuned LLMs ten times larger (>7B) and all the domain baselines, achieving a 23.5\% Top-1 accuracy improvement on rigorous benchmarks without test-time augmentation. this https URL .

</details>

---

### 2. [HELIOS: Harmonizing Early Fusion, Late Fusion, and LLM Reasoning for Multi-Granular Table-Text Retrieval](https://arxiv.org/abs/2603.02248)

**基本信息**

- 🔗 arXiv: [`2603.02248`](https://arxiv.org/abs/2603.02248)
- 👥 作者: Sungho Park, Joohyung Yun, Jongwuk Lee 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02248.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法（HELIOS）直接利用大语言模型（LLM）进行星图级别的逻辑推理精炼，以解决复杂的跨模态检索和推理问题，这属于“化学大模型”在广义信息处理（包括科学数据）中的应用和增强。

**📖 中文摘要**

本文提出HELIOS框架，旨在解决表格-文本检索任务中早期融合和晚期融合方法的局限性，并提升对高级推理任务（如列级聚合和多跳推理）的处理能力。该框架结合了两种方法的优势：首先通过基于边的二分子图检索识别细粒度的表格片段与文本段落之间的边，避免引入无关上下文；然后通过查询相关节点扩展，动态检索相关边以扩展二分子图，最小化遗漏重要上下文的风险；最后在星图级别而非二分子图级别进行基于LLM的逻辑推理精炼，以支持高级推理任务。实验结果表明，HELIOS在OTT-QA基准上显著优于现有最先进模型。该论文的核心创新在于利用大语言模型（LLM）进行推理精炼，以解决复杂的跨模态信息检索和推理问题，其方法直接依赖于并增强了LLM在结构化数据理解与推理方面的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Table-text retrieval aims to retrieve relevant tables and text to support open-domain question answering. Existing studies use either early or late fusion, but face limitations. Early fusion pre-aligns a table row with its associated passages, forming "stars," which often include irrelevant contexts and miss query-dependent relationships. Late fusion retrieves individual nodes, dynamically aligning them, but it risks missing relevant contexts. Both approaches also struggle with advanced reasoning tasks, such as column-wise aggregation and multi-hop reasoning. To address these issues, we propose HELIOS, which combines the strengths of both approaches. First, the edge-based bipartite subgraph retrieval identifies finer-grained edges between table segments and passages, effectively avoiding the inclusion of irrelevant contexts. Then, the query-relevant node expansion identifies the most promising nodes, dynamically retrieving relevant edges to grow the bipartite subgraph, minimizing the risk of missing important contexts. Lastly, the star-based LLM refinement performs logical inference at the star graph level rather than the bipartite subgraph, supporting advanced reasoning tasks. Experimental results show that HELIOS outperforms state-of-the-art models with a significant improvement up to 42.6\% and 39.9\% in recall and nDCG, respectively, on the OTT-QA benchmark.

</details>

---

### 3. [Graph Attention Based Prioritization of Disease Responsible Genes from Multimodal Alzheimer's Network](https://arxiv.org/abs/2603.02273)

**基本信息**

- 🔗 arXiv: [`2603.02273`](https://arxiv.org/abs/2603.02273)
- 👥 作者: Binon Teji, Subhajit Bandyopadhyay, Swarup Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02273.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法（NETRA）是一个基于图变换器的多模态深度学习框架，用于生物网络分析和疾病基因发现。这属于化学信息学和生物信息学中利用先进神经网络模型（可视为特定领域的“化学/生物大模型”）解决复杂生物医学问题的研究。

**📖 中文摘要**

本文提出NETRA，一个用于从多模态阿尔茨海默病网络中优先排序疾病相关基因的多模态图变换器框架。该研究旨在理解阿尔茨海默病等复杂疾病的分子机制。NETRA的创新在于用注意力驱动的相关性评分取代了传统的启发式中心性度量。它整合了来自微阵列、单细胞RNA-seq和单核RNA-seq数据构建的基因调控网络，以及蛋白质-蛋白质相互作用、基因本体语义相似性和基于扩散的基因相似性等辅助生物网络，形成一个统一的多模态图。一个图变换器被用来分配NETRA分数，以量化基因在疾病特定和上下文感知中的相关性。该框架被证明在阿尔茨海默病通路上显著优于经典的中心性度量和扩散模型。这项工作展示了图神经网络和变换器模型在整合多组学数据、进行生物网络分析和疾病基因发现方面的强大能力，属于计算生物学和化学信息学中复杂系统建模的前沿。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Prioritizing disease-associated genes is central to understanding the molecular mechanisms of complex disorders such as Alzheimer's disease (AD). Traditional network-based approaches rely on static centrality measures and often fail to capture cross-modal biological heterogeneity. We propose NETRA (Node Evaluation through Transformer-based Representation and Attention), a multimodal graph transformer framework that replaces heuristic centrality metrics with attention-driven relevance scoring. Using AD as a case study, gene regulatory networks are independently constructed from microarray, single-cell RNA-seq, and single-nucleus RNA-seq data. Random-walk sequences derived from these networks are used to train a BERT-based model for learning global gene embeddings, while modality-specific gene expression profiles are compressed using variational autoencoders. These representations are integrated with auxiliary biological networks, including protein-protein interactions, Gene Ontology semantic similarity, and diffusion-based gene similarity, into a unified multimodal graph. A graph transformer assigns NETRA scores that quantify gene relevance in a disease-specific and context-aware manner. Gene set enrichment analysis shows that NETRA achieves a normalized enrichment score of about 3.9 for the Alzheimer's disease pathway, substantially outperforming classical centrality measures and diffusion models. Top-ranked genes enrich multiple neurodegenerative pathways, recover a known late-onset AD susceptibility locus at chr12q13, and reveal conserved cross-disease gene modules. The framework preserves biologically realistic heavy-tailed network topology and is readily extensible to other complex disorders.

</details>

---

### 4. [Manifold Aware Denoising Score Matching (MAD)](https://arxiv.org/abs/2603.02452)

**基本信息**

- 🔗 arXiv: [`2603.02452`](https://arxiv.org/abs/2603.02452)
- 👥 作者: Alona Levy-Jurgenson, Alvaro Prat, James Cuin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02452.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进定义在流形（如旋转矩阵空间）上的分布学习算法。这种高效学习结构化数据分布的方法，是构建用于化学结构推理的生成模型（化学大模型的一种形式）的基础技术之一，因此与‘化学大模型’主题核心相关。

**📖 中文摘要**

本文提出了一种流形感知去噪分数匹配（MAD）方法，用于学习定义在流形上的分布。该方法通过将分数函数分解为已知分量和待学习的剩余分量，减轻了模型隐式学习数据流形结构的负担，同时保持了计算效率。作者推导了旋转矩阵分布和离散分布等几种重要情况下的已知分量解析形式。该方法的核心思想是通过修改环境空间中的去噪分数匹配来隐式地考虑流形结构，这对于学习复杂数据（如分子构象或质谱数据可能存在的潜在结构空间）的分布具有潜在价值。虽然论文未直接应用，但其提出的在结构化空间（可类比化学空间）中高效学习分布的方法论，与构建用于化学结构推理的生成模型（如化学大模型）的研究方向相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A major focus in designing methods for learning distributions defined on manifolds is to alleviate the need to implicitly learn the manifold so that learning can concentrate on the data distribution within the manifold. However, accomplishing this often leads to compute-intensive solutions. In this work, we propose a simple modification to denoising score-matching in the ambient space to implicitly account for the manifold, thereby reducing the burden of learning the manifold while maintaining computational efficiency. Specifically, we propose a simple decomposition of the score function into a known component $s^{base}$ and a remainder component $s-s^{base}$ (the learning target), with the former implicitly including information on where the data manifold resides. We derive known components $s^{base}$ in analytical form for several important cases, including distributions over rotation matrices and discrete distributions, and use them to demonstrate the utility of this approach in those cases.

</details>

---

### 5. [Diagnosing Retrieval vs. Utilization Bottlenecks in LLM Agent Memory](https://arxiv.org/abs/2603.02473)

**基本信息**

- 🔗 arXiv: [`2603.02473`](https://arxiv.org/abs/2603.02473)
- 👥 作者: Boqin Yuan, Yue Su, Kun Yao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02473.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析LLM智能体中记忆检索与利用的瓶颈。高效的检索和知识利用机制是构建能够处理复杂化学信息（如质谱-结构映射）的‘化学大模型’或‘质谱结构推理’系统的关键组成部分，因此与主题核心相关。

**📖 中文摘要**

本文研究了增强记忆的LLM智能体中，记忆写入策略与检索方法对性能影响的相对重要性。作者引入了一个诊断框架，分析了在不同写入策略（原始分块、事实提取、总结）和检索方法（余弦相似度、BM25、混合重排序）下性能差异的表现。研究发现，在当前实践中，检索方法是主导因素，而原始分块存储（无需LLM调用）的性能匹配或超过了昂贵的、有损的替代方案。这表明当前记忆管道可能丢弃了下游检索机制无法补偿的有用上下文。失败分析显示，性能崩溃最常发生在检索阶段而非利用阶段。这项工作强调了改进检索质量对于智能体性能的重要性。虽然论文聚焦于通用LLM智能体，但其对信息检索、表示和利用的深入分析，为构建需要从海量化学知识库（如质谱数据库）中高效检索和推理结构的化学大模型或质谱分析工具提供了重要的方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Memory-augmented LLM agents store and retrieve information from prior interactions, yet the relative importance of how memories are written versus how they are retrieved remains unclear. We introduce a diagnostic framework that analyzes how performance differences manifest across write strategies, retrieval methods, and memory utilization behavior, and apply it to a 3x3 study crossing three write strategies (raw chunks, Mem0-style fact extraction, MemGPT-style summarization) with three retrieval methods (cosine, BM25, hybrid reranking). On LoCoMo, retrieval method is the dominant factor: average accuracy spans 20 points across retrieval methods (57.1% to 77.2%) but only 3-8 points across write strategies. Raw chunked storage, which requires zero LLM calls, matches or outperforms expensive lossy alternatives, suggesting that current memory pipelines may discard useful context that downstream retrieval mechanisms fail to compensate for. Failure analysis shows that performance breakdowns most often manifest at the retrieval stage rather than at utilization. We argue that, under current retrieval practices, improving retrieval quality yields larger gains than increasing write-time sophistication. Code is publicly available at this https URL .

</details>

---

### 6. [NeuroProlog: Multi-Task Fine-Tuning for Neurosymbolic Mathematical Reasoning via the Cocktail Effect](https://arxiv.org/abs/2603.02504)

**基本信息**

- 🔗 arXiv: [`2603.02504`](https://arxiv.org/abs/2603.02504)
- 👥 作者: Pratibha Zunjare, Michael Hsiao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02504.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个结合神经网络与符号逻辑（Prolog）的框架，以解决LLM在严格推理任务中的不可靠性。这种神经符号方法对于开发能够进行可靠‘质谱结构推理’或复杂化学逻辑推理的‘化学大模型’具有直接的相关性和技术借鉴价值。

**📖 中文摘要**

本文提出了NeuroProlog，一个神经符号框架，旨在通过将数学应用题编译成可执行的Prolog程序并辅以形式化验证保证，来确保LLM数学推理的可验证性。作者提出了一种多任务鸡尾酒训练策略，在统一的符号表示空间中联合优化三个协同目标：数学公式到规则的翻译、自然语言到程序的合成、以及程序-答案对齐。这种联合监督实现了正向迁移，其中公式翻译中的符号基础直接提高了组合推理能力。在推理时，引入了一个带有细粒度错误分类的执行引导解码管道，支持迭代程序修复。该工作展示了如何将符号推理与神经网络结合，以解决当前LLM在数学等需要严格逻辑的领域中的不可靠性问题。这种方法论对于构建需要进行严格逻辑推理和结构解析的化学大模型（例如，从质谱数据推理分子式或结构）具有重要的启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) achieve strong performance on natural language tasks but remain unreliable in mathematical reasoning, frequently generating fluent yet logically inconsistent solutions. We present \textbf{NeuroProlog}, a neurosymbolic framework that ensures verifiable reasoning by compiling math word problems into executable Prolog programs with formal verification guarantees. We propose a multi-task Cocktail training strategy that jointly optimizes three synergistic objectives in a unified symbolic representation space: (i) mathematical formula-to-rule translation (KB), (ii) natural language-to-program synthesis (SOLVE), and (iii) program-answer alignment. This joint supervision enables positive transfer, where symbolic grounding in formula translation directly improves compositional reasoning capabilities. At inference, we introduce an execution-guided decoding pipeline with fine-grained error taxonomy that enables iterative program repair and quantifies model self-debugging capacity. Comprehensive evaluation on GSM8K across four model scales (3B--32B parameters) demonstrates consistent improvements: cocktail training achieves significant accuracy gains of +5.23\% (Qwen-32B, $p < 0.01$), +3.43\% (GPT-OSS-20B, $p < 0.01$), and +5.54\% (Llama-3B, $p < 0.05$) over single-task this http URL error analysis reveals scale-dependent learning dynamics: at 32B scale, cocktail training transforms unfixable type errors (12\% repair rate) into correctable domain errors (96\% repair rate), achieving 92.7\% overall correction; at 8B scale, the same training eliminates syntactic errors but introduces semantic failures, revealing a critical capacity threshold for type-safe symbolic reasoning.

</details>

---

### 7. [ParEVO: Synthesizing Code for Irregular Data: High-Performance Parallelism through Agentic Evolution](https://arxiv.org/abs/2603.02510)

**基本信息**

- 🔗 arXiv: [`2603.02510`](https://arxiv.org/abs/2603.02510)
- 👥 作者: Liu Yang, Zeyu Nie, Andrew Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02510.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用LLM和进化方法为不规则数据（如图）合成高性能并行算法。处理分子图、质谱峰列表等不规则数据结构是化学信息学和质谱分析中的核心挑战，因此该框架与方法与开发高效‘化学大模型’和‘质谱结构推理’系统的底层计算技术相关。

**📖 中文摘要**

本文提出了ParEVO框架，旨在为不规则数据结构合成高性能并行算法。该框架包含三个主要贡献：1) Parlay-Instruct语料库，一个通过“批评-精炼”管道合成的包含13,820个任务的数据集，明确筛选了能有效利用Work-Span并行原语的经验高性能算法；2) 针对ParlayLib库严格语义进行微调的专用模型；3) 进化编码代理（ECA），通过使用编译器、动态竞争检测器和性能分析器的反馈迭代修复代码，以提高“最后一英里”的正确性。该工作在ParEval基准测试中实现了平均106倍的加速。虽然论文聚焦于通用并行计算，但其核心是使用LLM和进化方法来自动生成和优化处理复杂、不规则数据（如图）的算法。这种方法论可以迁移到化学信息学领域，用于开发处理分子图、质谱数据流等不规则化学数据的专用算法或模型，从而服务于化学大模型的高效计算或质谱数据处理流水线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The transition from sequential to parallel computing is essential for modern high-performance applications but is hindered by the steep learning curve of concurrent programming. This challenge is magnified for irregular data structures (such as sparse graphs, unbalanced trees, and non-uniform meshes) where static scheduling fails and data dependencies are unpredictable. Current Large Language Models (LLMs) often fail catastrophically on these tasks, generating code plagued by subtle race conditions, deadlocks, and sub-optimal scaling. We bridge this gap with ParEVO, a framework designed to synthesize high-performance parallel algorithms for irregular data. Our contributions include: (1) The Parlay-Instruct Corpus, a curated dataset of 13,820 tasks synthesized via a "Critic-Refine" pipeline that explicitly filters for empirically performant algorithms that effectively utilize Work-Span parallel primitives; (2) specialized DeepSeek, Qwen, and Gemini models fine-tuned to align probabilistic generation with the rigorous semantics of the ParlayLib library; and (3) an Evolutionary Coding Agent (ECA) that improves the "last mile" of correctness by iteratively repairing code using feedback from compilers, dynamic race detectors, and performance profilers. On the ParEval benchmark, ParEVO achieves an average 106x speedup (with a maximum of 1103x) across the suite, and a robust 13.6x speedup specifically on complex irregular graph problems, outperforming state-of-the-art commercial models. Furthermore, our evolutionary approach matches state-of-the-art expert human baselines, achieving up to a 4.1x speedup on specific highly-irregular kernels. Source code and datasets are available at this https URL .

</details>

---

### 8. [Large Language Model-Enhanced Relational Operators: Taxonomy, Benchmark, and Analysis](https://arxiv.org/abs/2603.02537)

**基本信息**

- 🔗 arXiv: [`2603.02537`](https://arxiv.org/abs/2603.02537)
- 👥 作者: Yunxiang Su, Tianjing Zeng, Zhongjun Ding 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02537.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统化地研究LLM如何作为“操作符”增强关系型数据处理。这直接关系到如何将‘化学大模型’的能力集成到化学数据库查询、质谱库检索、跨模态数据关联等‘质谱结构推理’的关键环节中，因此与两个主题都高度相关。

**📖 中文摘要**

本文研究了将大语言模型（LLM）通过类似关系型操作符的组件集成到关系数据处理任务中的方法，例如带有语义谓词的过滤器、知识增强的表填充、推理驱动的实体匹配等。作者将这些保留关系型输入/输出接口并调用LLM的组件称为LLM增强关系操作符（LROs）。论文首先建立了一个统一的LRO分类法，将其归类为：选择、匹配、填充、聚类和排序，并讨论了它们的操作数和实现变体。其次，设计了LROBench，一个包含290个单LRO查询和60个多LRO查询的综合基准测试，涵盖超过10个领域的27个数据库。这项工作系统化地梳理和评估了LLM在结构化数据（如数据库）处理中的应用模式。对于化学信息学而言，分子数据库、质谱数据库是典型的结构化/半结构化数据源。该研究为如何利用LLM（作为化学大模型的核心或组件）来增强化学数据库的查询、信息提取、跨库关联（如质谱与结构数据库的匹配）等任务提供了重要的框架性参考和评估方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the development of large language models (LLMs), numerous studies integrate LLMs through operator-like components to enhance relational data processing tasks, e.g., filters with semantic predicates, knowledge-augmented table imputation, reasoning-driven entity matching and more challenging semantic query processing. These components invoke LLMs while preserving a relational input/output interface, which we refer to as LLM-Enhanced Relational Operators (LROs). From an operator perspective, unfortunately, these existing LROs suffer from fragmented definition, various implementation strategies and inadequate evaluation benchmarks. To this end, in this paper, we first establish a unified LRO taxonomy to align existing LROs, and categorize them into: Select, Match, Impute, Cluster and Order, along with their operands and implementation variants. Second, we design LROBench, a comprehensive benchmark featuring 290 single-LRO queries and 60 multi-LRO queries, spanning 27 databases across more than 10 domains. LROBench covers all operating logics and operand granularities in its single-LRO workload, and provides challenging multi-LRO queries stratified by query complexity. Based on these, we evaluate individual LROs under various implementations, deriving practical insights into LRO design choices and summarizing our empirical best practices. We further compare the end-to-end performance of existing multi-LRO systems against an LRO suite instantiated with these best practices, in order to investigate how to design an effective LRO set for multi-LRO systems targeting complex semantic queries. Last, to facilitate future work, we outline promising future directions and open-source all benchmark data and evaluation code, available at this https URL .

</details>

---

### 9. [A Neuropsychologically Grounded Evaluation of LLM Cognitive Abilities](https://arxiv.org/abs/2603.02540)

**基本信息**

- 🔗 arXiv: [`2603.02540`](https://arxiv.org/abs/2603.02540)
- 👥 作者: Faiz Ghifari Haznitrama, Faeyza Rishad Ardi, Alice Oh
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02540.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建和评估LLM的基础认知能力（如抽象推理、工作记忆）。这些高级认知能力是开发能够进行复杂‘质谱结构推理’和化学问题解决的‘化学大模型’所必需的核心能力之一，因此与主题相关。

**📖 中文摘要**

本文引入了NeuroCognition基准测试，该测试基于三种改编的神经心理学测试：瑞文渐进矩阵（抽象关系推理）、空间工作记忆（维持和系统搜索）以及威斯康星卡片分类测试（认知灵活性），旨在评估LLM的基础认知能力。研究发现，虽然模型在文本任务上表现强劲，但在图像任务上性能下降，且随着任务复杂性增加而退化。此外，复杂的推理并非普遍有益，而简单的人类式策略能带来部分收益。NeuroCognition与标准通用能力基准呈正相关，同时能测量超出这些基准的独特认知能力。该工作强调了对LLM进行更接近人类认知的、可验证的基础能力评估的重要性。对于‘化学大模型’和‘质谱结构推理’而言，模型不仅需要专业知识，还需要强大的抽象推理、模式识别和认知灵活性来处理复杂的化学结构和光谱数据。该基准测试及其反映的评估思想，为设计和评估具备高级推理能力的化学领域大模型提供了重要的评估维度和启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) exhibit a unified "general factor" of capability across 10 benchmarks, a finding confirmed by our factor analysis of 156 models, yet they still struggle with simple, trivial tasks for humans. This is because current benchmarks focus on task completion, failing to probe the foundational cognitive abilities that highlight these behaviors. We address this by introducing the NeuroCognition benchmark, grounded in three adapted neuropsychological tests: Raven's Progressive Matrices (abstract relational reasoning), Spatial Working Memory (maintenance and systematic search), and the Wisconsin Card Sorting Test (cognitive flexibility). Our evaluation reveals that while models perform strongly on text, their performance degrades for images and with increased complexity. Furthermore, we observe that complex reasoning is not universally beneficial, whereas simple, human-like strategies yield partial gains. We also find that NeuroCognition correlates positively with standard general-capability benchmarks, while still measuring distinct cognitive abilities beyond them. Overall, NeuroCognition emphasizes where current LLMs align with human-like intelligence and where they lack core adaptive cognition, showing the potential to serve as a verifiable, scalable source for improving LLMs.

</details>

---

### 10. [Relevance Matters: A Multi-Task and Multi-Stage Large Language Model Approach for E-commerce Query Rewriting](https://arxiv.org/abs/2603.02555)

**基本信息**

- 🔗 arXiv: [`2603.02555`](https://arxiv.org/abs/2603.02555)
- 👥 作者: Aijun Dai, Jixiang Zhang, Haiqing Hu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02555.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用LLM进行多任务学习（生成+相关性评估）并结合RL进行目标对齐的框架。这种方法论可以直接迁移到‘质谱结构推理’任务中，即构建一个同时生成候选结构并评估其与质谱匹配度的化学大模型，因此与主题核心相关。

**📖 中文摘要**

本文为电子商务搜索提出了一种基于大语言模型（LLM）的多任务多阶段查询重写框架。该框架的关键创新在于将相关性任务注入到查询重写过程中。具体而言，该方法首先利用在用户数据和产品信息上预训练的模型，进行包含重写查询生成任务以及查询与重写之间相关性标注任务的多任务监督微调（SFT）。随后，采用群组相对策略优化（GRPO）使模型的目标与提升相关性和刺激用户转化相一致。通过离线评估和在线A/B测试，该框架显著提升了电子商务查询重写的效果。虽然应用场景是电商，但其核心方法论——使用LLM进行多任务学习（同时优化生成和相关性判断）并结合强化学习进行目标对齐——对于化学信息学任务具有很高的借鉴价值。例如，可以构建一个化学大模型，其任务同时包括：根据质谱特征生成候选分子结构（生成任务），以及评估该结构与质谱数据的匹配程度（相关性/评分任务）。这种多任务框架正是该论文所探讨的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

For e-commerce search, user experience is measured by users' behavioral responses to returned products, like click-through rate and conversion rate, as well as the relevance between returned products and search queries. Consequently, relevance and user conversion constitute the two primary objectives in query rewriting, a strategy to bridge the lexical gap between user expressions and product descriptions. This research proposes a multi-task and multi-stage query rewriting framework grounded in large language models (LLMs). Critically, in contrast to previous works that primarily emphasized rewritten query generation, we inject the relevance task into query rewriting. Specifically, leveraging a pretrained model on user data and product information from this http URL , the approach initiates with multi-task supervised fine-tuning (SFT) comprising of the rewritten query generation task and the relevance tagging task between queries and rewrites. Subsequently, we employ Group Relative Policy Optimization (GRPO) for the model's objective alignment oriented toward enhancing the relevance and stimulating user conversions. Through offline evaluation and online A/B test, our framework illustrates substantial improvements in the effectiveness of e-commerce query rewriting, resulting in elevating the search results' relevance and boosting the number of purchases made per user (UCVR). Since August 2025, our approach has been implemented on this http URL , one of China's leading online shopping platforms.

</details>

---

### 11. [Through the Lens of Contrast: Self-Improving Visual Reasoning in VLMs](https://arxiv.org/abs/2603.02556)

**基本信息**

- 🔗 arXiv: [`2603.02556`](https://arxiv.org/abs/2603.02556)
- 👥 作者: Zhiyu Pan, Yizheng Wu, Jiashen Hua 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02556.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种利用对比学习来提升VLM推理可靠性和减少幻觉的自改进框架。这种方法对于构建需要处理高度相似或微妙差异数据（如质谱图）的‘质谱结构推理’模型至关重要，因此与主题核心相关。

**📖 中文摘要**

本文提出了视觉对比自教推理器（VC-STaR），一种利用视觉对比来减轻模型生成推理链中幻觉的新型自改进框架。其核心观察是：当呈现一个对比性的VQA对（即两个视觉相似、问题同义的图像）时，VLM能更精确地识别相关的视觉线索。基于此，VC-STaR利用视觉对比来引导模型生成更可靠的推理依据，从而构建了一个新的视觉推理数据集VisCoR-55K。实验表明，VC-STaR不仅优于现有的自改进方法，也超过了在现有视觉推理数据集上微调的模型。这项工作展示了如何利用模型自身的对比能力来提升其视觉推理能力。对于‘质谱结构推理’而言，处理对比性数据（如相似质谱对应不同结构，或不同质谱对应相似结构）是核心挑战之一。该论文提出的通过对比学习来提升模型推理可靠性和减少幻觉的方法，为开发更稳健的、能够处理微妙差异的质谱分析大模型提供了重要的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning has emerged as a key capability of large language models. In linguistic tasks, this capability can be enhanced by self-improving techniques that refine reasoning paths for subsequent finetuning. However, extending these language-based self-improving approaches to vision language models (VLMs) presents a unique challenge:~visual hallucinations in reasoning paths cannot be effectively verified or rectified. Our solution starts with a key observation about visual contrast: when presented with a contrastive VQA pair, i.e., two visually similar images with synonymous questions, VLMs identify relevant visual cues more precisely. Motivated by this observation, we propose Visual Contrastive Self-Taught Reasoner (VC-STaR), a novel self-improving framework that leverages visual contrast to mitigate hallucinations in model-generated rationales. We collect a diverse suite of VQA datasets, curate contrastive pairs according to multi-modal similarity, and generate rationales using VC-STaR. Consequently, we obtain a new visual reasoning dataset, VisCoR-55K, which is then used to boost the reasoning capability of various VLMs through supervised finetuning. Extensive experiments show that VC-STaR not only outperforms existing self-improving approaches but also surpasses models finetuned on the SoTA visual reasoning datasets, demonstrating that the inherent contrastive ability of VLMs can bootstrap their own visual reasoning. Project at: this https URL .

</details>

---

### 12. [CAPT: Confusion-Aware Prompt Tuning for Reducing Vision-Language Misalignment](https://arxiv.org/abs/2603.02557)

**基本信息**

- 🔗 arXiv: [`2603.02557`](https://arxiv.org/abs/2603.02557)
- 👥 作者: Maoyuan Shao, Yutong Gao, Xinyang Huang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02557.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一个混淆感知学习框架来提升模型对相似类别的区分能力。这种技术对于‘质谱结构推理’中区分结构相似分子产生的相似质谱图，以及化学大模型中精确的分子属性预测或分类任务至关重要，因此与主题高度相关。

**📖 中文摘要**

本文针对视觉-语言模型（如CLIP）在视觉和语义相似类别间存在系统性误分类的问题，提出了混淆感知提示调优框架（CAPT）。该框架使模型能够从自身的错配中学习。具体而言，构建了一个混淆库来显式建模类别间稳定的混淆关系。在此基础上，引入了语义混淆挖掘器（SEM）来捕获全局的类间混淆，以及样本混淆挖掘器（SAM）来从库中检索代表性的误分类实例并通过差异方式适配器捕获样本级线索。此外，还设计了一个多粒度差异专家（MGDE）模块来联合利用语义级和样本级专家进行更稳健的混淆感知推理。大量实验表明，该方法显著减少了混淆引起的错误。在化学信息学中，化合物分类、光谱解析经常面临结构相似或光谱相似但类别不同的混淆问题。该论文提出的混淆感知学习框架，为开发能够更好区分细微差别、减少错误预测的化学大模型（例如用于质谱谱图分类或分子属性预测）提供了直接且强大的技术工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-language models like CLIP have achieved remarkable progress in cross-modal representation learning, yet suffer from systematic misclassifications among visually and semantically similar categories. We observe that such confusion patterns are not random but persistently occur between specific category pairs, revealing the model's intrinsic bias and limited fine-grained discriminative ability. To address this, we propose CAPT, a Confusion-Aware Prompt Tuning framework that enables models to learn from their own misalignment. Specifically, we construct a Confusion Bank to explicitly model stable confusion relationships across categories and misclassified samples. On this basis, we introduce a Semantic Confusion Miner (SEM) to capture global inter-class confusion through semantic difference and commonality prompts, and a Sample Confusion Miner (SAM) to retrieve representative misclassified instances from the bank and capture sample-level cues through a Diff-Manner Adapter that integrates global and local contexts. To further unify confusion information across different granularities, a Multi-Granularity Difference Expert (MGDE) module is designed to jointly leverage semantic- and sample-level experts for more robust confusion-aware reasoning. Extensive experiments on 11 benchmark datasets demonstrate that our method significantly reduces confusion-induced errors while enhancing the discriminability and generalization of both base and novel classes, successfully resolving 50.72 percent of confusable sample pairs. Code will be released at this https URL .

</details>

---

### 13. [Molecular Dynamics Simulations Reveal PolyQ-Length-Dependent Conformational Changes in Huntingtin Exon-1: Implications for Environmental Co-Solvent Modulation of Aggregation-Prone States](https://arxiv.org/abs/2603.02572)

**基本信息**

- 🔗 arXiv: [`2603.02572`](https://arxiv.org/abs/2603.02572)
- 👥 作者: Jai Geddes-Nelson, Xiaochen Liu, Ken-Tye Yong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02572.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用分子动力学模拟研究分子（蛋白质片段）的构象变化及其对环境因素的响应。分子模拟和构象分析是计算化学的基础，为‘化学大模型’提供训练数据、验证方法或物理见解，也与理解分子结构（质谱推理的目标）相关，因此与主题相关。

**📖 中文摘要**

本文通过全原子分子动力学模拟，研究了亨廷顿蛋白外显子-1（包含N17结构域、不同长度的多聚谷氨酰胺链和聚脯氨酸区域）的构象动力学。模拟分析了多聚谷氨酰胺链长度（Q21, Q40, Q70）对蛋白质半径、溶剂可及表面积等构象参数的影响，并进一步测试了有机共溶剂（甲醇、己烷、三氯乙烯）对这些构象景观的调制作用。研究发现，多聚谷氨酰胺链的扩展驱动了构象的逐步扩展和溶剂暴露增加。三氯乙烯等疏水共溶剂能够诱导Q21和Q40构象的显著扩展。这项工作首次通过MD模拟系统地研究了共溶剂对亨廷顿蛋白外显子-1构象动力学的影响。虽然研究对象是生物蛋白，但其采用的计算方法——分子动力学模拟结合环境因素（共溶剂）研究来揭示分子构象变化和聚集倾向——是计算化学和化学信息学的核心手段。这种方法论可直接应用于小分子、药物或材料分子的构象分析、溶剂效应研究，是构建和理解‘化学大模型’所需的基础物理化学知识来源，也是模拟质谱解析中可能涉及的分子构象变化的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Huntington's disease (HD) is caused by CAG-repeat expansion in HTT, which lengthens the polyglutamine (polyQ) tract in huntingtin (HTT) and promotes misfolding and aggregation. While polyQ-length-dependent aggregation is well established, the atomistic conformational dynamics preceding aggregation remain less defined. Here we perform all-atom molecular dynamics simulations of HTT exon-1 constructs containing the N17 domain, polyQ tracts of clinically relevant lengths (Q21, wildtype; Q40, adult onset threshold; Q70, juvenile onset), and the polyproline (polyP) region. Multi-copy simulations (four chains) were run for 100 ns in explicit SPC/E water using the OPLS-AA force field. We quantified radius of gyration (Rg), solvent-accessible surface area (SASA), root-mean-square deviation (RMSD), and intra-protein hydrogen bonds as proxies for conformational expansion and aggregation propensity. PolyQ expansion drove progressive increases in Rg and SASA, consistent with more extended, solvent-exposed ensembles. We further tested organic co-solvents (methanol, hexane, trichloroethylene; 0.5 to 1.0 M), which modulated these landscapes in a solvent-dependent manner. Trichloroethylene induced marked expansion in Q21 and Q40, whereas methanol produced mild compaction in Q21. To our knowledge, this is the first MD study to systematically examine co-solvent effects on HTT exon-1 conformational dynamics. Although limited sampling precludes definitive mechanistic conclusions, the observed trends suggest that hydrophobic co-solvents can bias HTT exon-1 toward more expanded ensembles, motivating computational studies of gene-environment modulation in HD.

</details>

---

### 14. [Maximizing Generalization: The Effect of Different Augmentation Techniques on Lightweight Vision Transformer for Bengali Character Classification](https://arxiv.org/abs/2603.02591)

**基本信息**

- 🔗 arXiv: [`2603.02591`](https://arxiv.org/abs/2603.02591)
- 👥 作者: Rafi Hassan Chowdhury, Naimul Haque, Kaniz Fatiha
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02591.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是对多种图像数据增强技术进行系统性实证研究和基准测试。数据增强是构建鲁棒深度学习模型的关键技术，对于准备用于训练‘化学大模型’或‘质谱结构推理’模型的化学数据集（如分子结构图像、光谱图）具有重要的方法论指导意义，因此与主题相关。

**📖 中文摘要**

本文针对孟加拉语手写字符识别中的数据稀缺问题，系统评估了多种图像数据增强技术（CLAHE、随机旋转、随机仿射、颜色抖动及其组合）对轻量级Vision Transformer模型性能的影响。实验在Ekush和AIBangla数据集上进行，发现随机仿射和颜色抖动的组合取得了最佳准确率。该研究深入分析了不同增强技术在处理资源有限语言（孟加拉语）图像数据时的效果。虽然应用领域是字符识别，但其核心贡献在于对数据增强技术的系统性实证研究。数据增强是训练深度学习模型（包括化学大模型）以克服数据稀缺、提高泛化能力的关键技术。在化学信息学中，分子图像、光谱图（如质谱、红外光谱）的数据同样可能面临标注数据有限的问题。该论文提供的关于不同增强技术有效性的分析，对于设计和优化用于‘质谱结构推理’或分子属性预测的深度学习模型的数据预处理和增强管道具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning models have proven to be highly effective in computer vision, with deep convolutional neural networks achieving impressive results across various computer vision tasks. However, these models rely heavily on large datasets to avoid overfitting. When a model learns features with either low or high variance, it can lead to underfitting or overfitting on the training data. Unfortunately, large-scale datasets may not be available in many domains, particularly for resource-limited languages such as Bengali. In this experiment, a series of tests were conducted in the field of image data augmentation as an approach to addressing the limited data problem for Bengali handwritten characters. The study also provides an in-depth analysis of the performance of different augmentation techniques. Data augmentation refers to a set of techniques applied to data to increase its size and diversity, making it more suitable for training deep learning models. The image augmentation techniques evaluated in this study include CLAHE, Random Rotation, Random Affine, Color Jitter, and their combinations. The study further explores the use of augmentation methods with a lightweight model such as EfficientViT. Among the different augmentation strategies, the combination of Random Affine and Color Jitter produced the best accuracy on the Ekush [1] and AIBangla [2] datasets, achieving accuracies of 97.48% and 97.57%, respectively. This combination outperformed all other individual and combined augmentation techniques. Overall, this analysis presents a thorough examination of the impact of image data augmentation in resource-scarce languages, particularly in the context of Bengali handwritten character recognition using lightweight models.

</details>

---

### 15. [Synthetic-Child: An AIGC-Based Synthetic Data Pipeline for Privacy-Preserving Child Posture Estimation](https://arxiv.org/abs/2603.02598)

**基本信息**

- 🔗 arXiv: [`2603.02598`](https://arxiv.org/abs/2603.02598)
- 👥 作者: Taowen Zeng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02598.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出一个完整的、基于AIGC的合成数据生成流水线，用于创建高质量的标注训练数据。这种方法论可以迁移到化学领域，用于生成虚拟分子结构、模拟质谱/光谱数据，从而为‘化学大模型’和‘质谱结构推理’研究提供宝贵的数据资源，因此与主题相关。

**📖 中文摘要**

本文提出了Synthetic-Child，一个基于AIGC的合成数据流水线，用于生成具有真实感的儿童姿势训练图像和关键点标注，而无需任何真实的儿童照片。该流水线包含四个阶段：1) 使用可编程3D儿童身体模型生成多样化的姿势并自动导出标注；2) 使用双ControlNet（姿势+深度）和FLUX-1 Dev合成12,000张真实感图像；3) 基于ViTPose的置信度过滤和针对性增强；4) 在合成数据上微调RTMPose-M模型并进行量化部署。在真实儿童测试集上，该模型取得了显著优于基线模型的性能。这项工作展示了精心设计的AIGC流水线可以在保护隐私的前提下，生成高质量的训练数据以训练高性能模型。对于化学信息学和质谱分析，获取大量高质量、标注准确的分子结构-性质数据或质谱-结构对数据同样成本高昂且可能存在知识产权限制。该论文提出的合成数据生成框架（结合3D建模、可控生成和后期处理）为创建用于训练‘化学大模型’或‘质谱结构推理’模型的合成化学数据集（如虚拟分子库及其模拟光谱）提供了极具潜力的技术蓝图和方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate child posture estimation is critical for AI-powered study companion devices, yet collecting large-scale annotated datasets of children is both expensive and ethically prohibitive due to privacy concerns. We present Synthetic-Child, an AIGC-based synthetic data pipeline that produces photorealistic child posture training images with ground-truth-projected keypoint annotations, requiring zero real child photographs. The pipeline comprises four stages: (1) a programmable 3D child body model (SMPL-X) in Blender generates diverse desk-study poses with IK-constrained anatomical plausibility and automatic COCO-format ground-truth export; (2) a custom PoseInjectorNode feeds 3D-derived skeletons into a dual ControlNet (pose + depth) conditioned on FLUX-1 Dev, synthesizing 12,000 photorealistic images across 10 posture categories with low annotation drift; (3) ViTPose-based confidence filtering and targeted augmentation remove generation failures and improve robustness; (4) RTMPose-M (13.6M params) is fine-tuned on the synthetic data and paired with geometric feature engineering and a lightweight MLP for posture classification, then quantized to INT8 for real-time edge deployment. On a real-child test set (n~300), the FP16 model achieves 71.2 AP -- a +12.5 AP improvement over the COCO-pretrained adult-data baseline at identical model capacity. After INT8 quantization the model retains 70.4 AP while running at 22 FPS on a 0.8-TOPS Rockchip RK3568 NPU. In a single-subject controlled comparison with a commercial posture corrector, our system achieves substantially higher recognition rates across most tested categories and responds ~1.8x faster on average. These results demonstrate that carefully designed AIGC pipelines can substantially reduce dependence on real child imagery while achieving deployment-ready accuracy, with potential applications to other privacy-sensitive domains.

</details>

---

### 16. [AlphaFree: Recommendation Free from Users, IDs, and GNNs](https://arxiv.org/abs/2603.02653)

**基本信息**

- 🔗 arXiv: [`2603.02653`](https://arxiv.org/abs/2603.02653)
- 👥 作者: Minseo Jeon, Junwoo Jung, Daewon Gwak 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02653.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用预训练语言模型（LLMs）生成的语言表示来构建推荐系统。这种方法论（使用大规模预训练模型学习实体表示）与“化学大模型”主题中探索如何利用大模型学习分子、反应等化学实体表示的研究直接相关。

**📖 中文摘要**

本文提出了AlphaFree，一种新颖的推荐方法，旨在摆脱对用户嵌入、原始ID和图神经网络（GNN）的依赖。其核心思想是：1）无需用户嵌入，通过语言表示（LRs）从预训练语言模型中推断偏好；2）用语言表示替代原始ID；3）通过数据增强和对比学习捕捉协同信号，而无需GNN。该方法显著减少了GPU内存使用（在高维LR下最多减少69%），并在多个真实世界数据集上超越了现有方法。虽然论文主要关注推荐系统，但其核心创新——利用预训练语言模型生成的语言表示来替代传统的离散ID表示——为构建和理解复杂化学实体（如分子）的表示提供了新的视角。这种方法与“化学大模型”中探索如何利用大规模预训练模型学习分子表示的研究主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Can we design effective recommender systems free from users, IDs, and GNNs? Recommender systems are central to personalized content delivery across domains, with top-K item recommendation being a fundamental task to retrieve the most relevant items from historical interactions. Existing methods rely on entrenched design conventions, often adopted without reconsideration, such as storing per-user embeddings (user-dependent), initializing features from raw IDs (ID-dependent), and employing graph neural networks (GNN-dependent). These dependencies incur several limitations, including high memory costs, cold-start and over-smoothing issues, and poor generalization to unseen interactions. In this work, we propose AlphaFree, a novel recommendation method free from users, IDs, and GNNs. Our main ideas are to infer preferences on-the-fly without user embeddings (user-free), replace raw IDs with language representations (LRs) from pre-trained language models (ID-free), and capture collaborative signals through augmentation with similar items and contrastive learning, without GNNs (GNN-free). Extensive experiments on various real-world datasets show that AlphaFree consistently outperforms its competitors, achieving up to around 40% improvements over non-LR-based methods and up to 5.7% improvements over LR-based methods, while significantly reducing GPU memory usage by up to 69% under high-dimensional LRs.

</details>

---

### 17. [SorryDB: Can AI Provers Complete Real-World Lean Theorems?](https://arxiv.org/abs/2603.02668)

**基本信息**

- 🔗 arXiv: [`2603.02668`](https://arxiv.org/abs/2603.02668)
- 👥 作者: Austin Letson, Leopoldo Sarra, Auguste Poiroux 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02668.pdf)

**💡 相关性分析**

满足标准1：论文的核心是评估和提升大语言模型（LLMs）在专业领域（形式化数学）中的推理与代码生成能力。这种专注于将大模型应用于特定科学领域（此处为数学）并进行系统性评估的研究，与“化学大模型”主题中探索大模型在化学领域的应用、能力评估和提升的研究直接相关。

**📖 中文摘要**

本文介绍了SorryDB，一个动态更新的基准测试，用于评估AI证明器在真实世界Lean定理证明任务上的能力。该基准从GitHub上的78个实际形式化项目中收集开放任务，旨在评估工具对社区实际需求的理解、处理复杂依赖关系的能力，以及对新颖数学项目做出贡献的潜力。论文评估了包括通用大语言模型、智能体方法和专用符号证明器在内的多种方法。虽然论文聚焦于数学定理证明，但其核心是评估和提升AI模型（特别是大语言模型）在复杂、结构化领域（如形式化数学）中的推理和代码生成能力。这种对AI模型在专业领域进行基准测试和性能提升的研究范式，与探索“化学大模型”在化学信息学、分子设计等专业领域的应用和评估具有方法论上的相似性和相关性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present SorryDB, a dynamically-updating benchmark of open Lean tasks drawn from 78 real world formalization projects on GitHub. Unlike existing static benchmarks, often composed of competition problems, hillclimbing the SorryDB benchmark will yield tools that are aligned to the community needs, more usable by mathematicians, and more capable of understanding complex dependencies. Moreover, by providing a continuously updated stream of tasks, SorryDB mitigates test-set contamination and offers a robust metric for an agent's ability to contribute to novel formal mathematics projects. We evaluate a collection of approaches, including generalist large language models, agentic approaches, and specialized symbolic provers, over a selected snapshot of 1000 tasks from SorryDB. We show that current approaches are complementary: even though an agentic approach based on Gemini Flash is the most performant, it is not strictly better than other off-the-shelf large-language models, specialized provers, or even a curated list of Lean tactics.

</details>

---

### 18. [Optimum Battery Depth of Discharge of Stand-alone Hybrid System Using the MOPSO Method](https://arxiv.org/abs/2603.02687)

**基本信息**

- 🔗 arXiv: [`2603.02687`](https://arxiv.org/abs/2603.02687)
- 👥 作者: Mohamad Izdin Hlal, Hussien Elharati, Ahmed Altaher
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02687.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通过分析算法执行行为轨迹（PSTrajs）来评估算法相似性和多样性的新方法。这种方法论对于理解和评估“质谱结构推理”中各种解析算法的本质逻辑和性能差异具有直接的借鉴意义和相关性，可以视为该主题下算法评估与比较的一种创新思路。

**📖 中文摘要**

本文提出了BehaveSim，一种通过算法在解决问题过程中产生的中间解序列（即问题解决轨迹，PSTrajs）来衡量算法相似性的新方法。该方法使用动态时间规整（DTW）来量化PSTrajs之间的对齐程度，从而区分那些尽管在语法或输出层面相似，但底层逻辑不同的算法。论文展示了BehaveSim在两个关键应用中的效用：1）增强基于大语言模型的自动算法设计（LLM-AAD）：将其集成到现有框架（如FunSearch）中，可以促进行为多样性，从而显著提升在多个AAD任务上的性能。2）算法分析：通过行为对生成的算法进行聚类，实现对问题解决策略的系统分析。这项研究为评估AI生成算法的本质创新性提供了重要工具。虽然应用场景是通用算法设计，但其核心方法论——通过分析执行行为轨迹来理解和区分复杂系统的内在逻辑——对于“质谱结构推理”等领域具有启发意义，例如，可以类比为通过分析质谱解析过程中的中间推理步骤或子结构匹配轨迹来评估和比较不同的结构推理算法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents an optimized design of a Standalone Solar PV/Battery (SSPVB) system to address energy reliability and cost efficiency challenges in off-grid environments. The proposed system integrates a Multi-Objective Particle Swarm Optimization (MOPSO) approach and validates the results using the Non-Dominated Sorting Genetic Algorithm II (NSGA-II). The optimization process aims to minimize both the Cost of Energy (COE) and Loss of Load Probability (LLP), while examining the effects of Battery Depth of Discharge (DOD) on system reliability and lifecycle cost. Results indicate that an optimal DOD of approximately 70% yields a COE of 0.2059 USD/kWh with zero LLP, demonstrating strong reliability and cost-effectiveness. Comparative analysis shows that both MOPSO and NSGA-II methods achieve consistent outcomes, with MOPSO exhibiting faster convergence. The study provides valuable insights into optimal battery sizing for stand-alone systems, contributing to modern optimization practices in renewable energy applications.

</details>

---

### 19. [VA-DAR: A PQC-Ready, Vendor-Agnostic Deterministic Artifact Resolution for Serverless, Enumeration-Resistant Wallet Recovery](https://arxiv.org/abs/2603.02690)

**基本信息**

- 🔗 arXiv: [`2603.02690`](https://arxiv.org/abs/2603.02690)
- 👥 作者: Jian Sheng Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02690.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于安全、可验证的数据发现和恢复的协议框架（VA-DAR）。虽然应用于区块链钱包，但其设计思想（如基于口令的标识符生成、抗枚举的发现机制、完整性验证）为构建和管理化学信息学或质谱分析中可能需要的安全、可检索的数据集或工具资源提供了潜在的技术参考和思路。

**📖 中文摘要**

本文提出了VA-DAR，一种支持后量子密码（PQC）的、供应商无关的确定性工件解析协议，用于实现无需服务器、枚举抵抗的钱包恢复。该协议在ACE-GF钱包架构之上引入了一个去中心化的发现与恢复层。其核心设计包括：使用口令派生的密钥材料、领域分离的密钥、以及通过口令派生的发现标识符发布的注册记录。VA-DAR提供了实用的跨设备恢复、对公共目录枚举的计算抵抗、通过所有者授权的发现映射完整性，以及通过单调版本控制和工件承诺实现的回滚/篡改检测。论文形式化了安全目标并进行了证明。虽然该研究属于密码学和区块链领域，但其核心贡献——设计一种安全、可验证的协议来映射和处理结构化数据（此处是加密工件），并确保其完整性和抗枚举性——与“化学大模型”和“质谱结构推理”中可能涉及的安全、可验证的数据管理、标识符生成和资源检索等底层技术挑战存在概念上的关联。例如，在化学信息学中，安全地存储、检索和验证分子数据或质谱库条目可能面临类似挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Serverless wallet recovery must balance portability, usability, and privacy. Public registries enable decentralized lookup but naive identifier hashing leaks membership through enumeration. We present VA-DAR, a keyed-discovery protocol for ACE-GF-based wallets that use device-bound passkeys for day-to-day local unlock while supporting cross-device recovery using only a user-provided identifier (e.g., email) and a single recovery passphrase. As a discovery-and-recovery layer over ACE-GF, VA-DAR inherits ACE-GF's context-isolated, algorithm-agile derivation substrate, enabling non-disruptive migration to post-quantum algorithms at the identity layer. The design introduces a decentralized discovery-and-recovery layer that maps a privacy-preserving discovery identifier to an immutable content identifier of a backup sealed artifact stored on a decentralized storage network. Concretely, a user derives passphrase-rooted key material with a memory-hard KDF, domain-separates keys for artifact sealing and discovery indexing, and publishes a registry record keyed by a passphrase-derived discovery identifier. VA-DAR provides: (i) practical cross-device recovery using only identifier and passphrase, (ii) computational resistance to public-directory enumeration, (iii) integrity of discovery mappings via owner authorization, and (iv) rollback/tamper detection via monotonic versioning and artifact commitments. We define three sealed artifact roles, two update-authorization options, and three protocol flows (registration, recovery, update). We formalize security goals via cryptographic games and prove, under standard assumptions, that VA-DAR meets these goals while remaining vendor-agnostic and chain-agnostic. End-to-end post-quantum deployment additionally requires a PQ-secure instantiation of registry authorization.

</details>

---

### 20. [FinTexTS: Financial Text-Paired Time-Series Dataset via Semantic-Based and Multi-Level Pairing](https://arxiv.org/abs/2603.02702)

**基本信息**

- 🔗 arXiv: [`2603.02702`](https://arxiv.org/abs/2603.02702)
- 👥 作者: Jaehoon Lee, Suhwan Park, Tae Yoon Lim 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02702.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出了一种利用大语言模型（LLMs）进行语义理解和层次化分类，以构建高质量、对齐良好的文本-时间序列配对数据集（FinTexTS）的方法论。这种构建高质量、语义对齐的多模态数据集的方法，直接为“化学大模型”和“质谱结构推理”领域创建所需的数据集（如分子-性质-文本描述配对数据、质谱-结构配对数据）提供了宝贵的技术范例和可行性路径。

**📖 中文摘要**

本文构建了FinTexTS，一个新的用于股票价格预测的大规模文本配对时间序列数据集。为了解决金融市场中复杂的相互依赖关系（公司的股价不仅受公司特定事件影响，还受其他公司事件和宏观因素影响），论文提出了一个基于语义和多层次的配对框架。具体而言，该框架从SEC文件中提取目标公司的特定上下文，并应用基于嵌入的匹配机制来检索语义相关的新闻文章。此外，使用大语言模型（LLMs）将新闻文章分类为四个层次（宏观、行业、相关公司、目标公司级别），从而实现新闻文章与目标公司的多级配对。实验结果表明，这种基于语义和多层次的配对策略在股价预测中是有效的。这项工作的核心是构建高质量、语义对齐的多模态（文本-数值）数据集的方法论。这种方法——利用LLMs进行语义理解和层次化标注以构建精准配对的数据集——对于“化学大模型”和“质谱结构推理”领域至关重要，因为这些领域同样急需高质量、对齐良好的多模态数据集（例如，将分子结构图、SMILES字符串、质谱图、文本描述进行关联）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The financial domain involves a variety of important time-series problems. Recently, time-series analysis methods that jointly leverage textual and numerical information have gained increasing attention. Accordingly, numerous efforts have been made to construct text-paired time-series datasets in the financial domain. However, financial markets are characterized by complex interdependencies, in which a company's stock price is influenced not only by company-specific events but also by events in other companies and broader macroeconomic factors. Existing approaches that pair text with financial time-series data based on simple keyword matching often fail to capture such complex relationships. To address this limitation, we propose a semantic-based and multi-level pairing framework. Specifically, we extract company-specific context for the target company from SEC filings and apply an embedding-based matching mechanism to retrieve semantically relevant news articles based on this context. Furthermore, we classify news articles into four levels (macro-level, sector-level, related company-level, and target-company level) using large language models (LLMs), enabling multi-level pairing of news articles with the target company. Applying this framework to publicly-available news datasets, we construct \textbf{FinTexTS}, a new large-scale text-paired stock price dataset. Experimental results on \textbf{FinTexTS} demonstrate the effectiveness of our semantic-based and multi-level pairing strategy in stock price forecasting. In addition to publicly-available news underlying \textbf{FinTexTS}, we show that applying our method to proprietary yet carefully curated news sources leads to higher-quality paired data and improved stock price forecasting performance.

</details>

---

### 21. [Deep learning-guided evolutionary optimization for protein design](https://arxiv.org/abs/2603.02753)

**基本信息**

- 🔗 arXiv: [`2603.02753`](https://arxiv.org/abs/2603.02753)
- 👥 作者: Erik Hartman, Di Tang, Johan Malmström
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02753.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将机器学习优化框架（BoGA）应用于蛋白质/肽的分子设计。这属于“化学大模型”或“AI for Chemistry”范畴，即利用人工智能方法（此处是优化算法）来解决化学和生物学中的分子设计问题。

**📖 中文摘要**

本文提出了BoGA（贝叶斯优化遗传算法），一个将进化搜索与贝叶斯优化相结合的框架，用于高效探索蛋白质序列空间，以设计具有特定特性的新型蛋白质。BoGA将遗传算法作为随机提案生成器集成到代理模型循环中，根据先前的评估和代理模型预测对候选序列进行优先级排序，从而实现数据高效优化。作者在序列和结构设计任务上对BoGA进行了基准测试，并将其应用于设计针对肺炎链球菌关键毒力因子肺炎球菌溶血素的肽结合剂。BoGA加速了高置信度结合剂的发现。这项工作展示了将机器学习优化方法（结合贝叶斯优化和进化算法）应用于蛋白质设计这一特定化学/生物分子领域。这直接体现了“化学大模型”或更广义的“AI for Science”在分子设计中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Designing novel proteins with desired characteristics remains a significant challenge due to the large sequence space and the complexity of sequence-function relationships. Efficient exploration of this space to identify sequences that meet specific design criteria is crucial for advancing therapeutics and biotechnology. Here, we present BoGA (Bayesian Optimization Genetic Algorithm), a framework that combines evolutionary search with Bayesian optimization to efficiently navigate the sequence space. By integrating a genetic algorithm as a stochastic proposal generator within a surrogate modeling loop, BoGA prioritizes candidates based on prior evaluations and surrogate model predictions, enabling data-efficient optimization. We demonstrate the utility of BoGA through benchmarking on sequence and structure design tasks, followed by its application in designing peptide binders against pneumolysin, a key virulence factor of \textit{Streptococcus pneumoniae}. BoGA accelerates the discovery of high-confidence binders, demonstrating the potential for efficient protein design across diverse objectives. The algorithm is implemented within the BoPep suite and is available under an MIT license at \href{ this https URL }{GitHub}.

</details>

---

### 22. [Embedding interpretable $\ell_1$-regression into neural networks for uncovering temporal structure in cell imaging](https://arxiv.org/abs/2603.02899)

**基本信息**

- 🔗 arXiv: [`2603.02899`](https://arxiv.org/abs/2603.02899)
- 👥 作者: Fabian Kabus, Maren Hackenberg, Julia Hindel 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02899.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发一种结合神经网络和可解释统计模型（ℓ1正则化VAR）的新方法，用于从成像数据（如质谱成像或类似的高维化学数据）中提取稀疏的动态结构。这与化学信息学中从复杂数据中推理结构/关系的主题高度相关。

**📖 中文摘要**

本文提出了一种将可解释的ℓ1回归嵌入到神经网络中的方法，用于从细胞成像数据中提取稀疏的自回归动态结构。该方法的核心是将向量自回归（VAR）模型作为可解释的回归技术，嵌入到一个卷积自编码器中。自编码器提供降维，使时间建模变得可行，而一个跳跃连接则专门处理非稀疏的静态空间信息，将有选择地将稀疏结构引导至ℓ1正则化的VAR模型中。ℓ1回归参数的估计通过微分分段线性解路径实现。该方法旨在结合神经网络在无监督学习非稀疏结构方面的优势，以及经典统计回归（特别是通过ℓ1正则化强制稀疏性）在可解释性方面的优势，从而识别驱动观测动态的关键因素。这项工作展示了如何将统计模型嵌入神经网络框架，以解决化学和生物信息学中常见的从高维时间序列数据中推断稀疏因果或动态关系的问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While artificial neural networks excel in unsupervised learning of non-sparse structure, classical statistical regression techniques offer better interpretability, in particular when sparseness is enforced by $\ell_1$ regularization, enabling identification of which factors drive observed dynamics. We investigate how these two types of approaches can be optimally combined, exemplarily considering two-photon calcium imaging data where sparse autoregressive dynamics are to be extracted. We propose embedding a vector autoregressive (VAR) model as an interpretable regression technique into a convolutional autoencoder, which provides dimension reduction for tractable temporal modeling. A skip connection separately addresses non-sparse static spatial information, selectively channeling sparse structure into the $\ell_1$-regularized VAR. $\ell_1$-estimation of regression parameters is enabled by differentiating through the piecewise linear solution path. This is contrasted with approaches where the autoencoder does not adapt to the VAR model. Having an embedded statistical model also enables a testing approach for comparing temporal sequences from the same observational unit. Additionally, contribution maps visualize which spatial regions drive the learned dynamics.

</details>

---

### 23. [Speech recognition assisted by large language models to command software orally -- Application to an augmented and virtual reality web app for immersive molecular graphics](https://arxiv.org/abs/2603.02901)

**基本信息**

- 🔗 arXiv: [`2603.02901`](https://arxiv.org/abs/2603.02901)
- 👥 作者: Fabio Cortes Rodriguez, Luciano Abriata
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02901.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大语言模型（LLM）理解并执行化学/分子图形领域复杂指令的智能交互系统。这直接涉及“化学大模型”在特定化学应用场景（分子可视化与操控）中的实际部署和评估，是化学大模型应用的一个典型案例。

**📖 中文摘要**

本项目成功开发并集成了一套语音用户界面（VUI），用于控制一个沉浸式分子图形网络应用。该应用允许用户在增强现实（AR）和虚拟现实（VR）环境中用手操纵分子，这使得手无法用于传统的鼠标键盘GUI控制。所开发的基于语音的VUI系统解决了这个问题，使用户能够通过自然语音（或键入）命令轻松控制应用。为了实现这一VUI，作者评估了两种自动语音识别（ASR）系统，并最终选择了Chrome的原生Speech API。为了将转录的语音转化为软件命令，作者测试了两种由大语言模型（LLM）驱动的方法：生成可执行代码或调用预定义函数。最终采用了基于OpenAI GPT-4o-mini的函数调用方法，因其在安全性、效率和可靠性上优于代码生成方法。最终的VUI集成了Chrome的ASR和基于LLM的函数调用模块，使用户能够使用自然语言命令应用程序。这项工作展示了如何利用大语言模型（作为化学大模型的一种应用形式）来理解和执行复杂的、领域特定（化学/分子图形）的指令，实现了人机交互的智能化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This project successfully developed, evaluated and integrated a Voice User Interface (VUI) into a web application that we are developing for immersive molecular graphics. Said app provides augmented and virtual reality (AR and VR) environments where users manipulate molecules with their hands, but this means the hands can't be used to control the app through a regular mouse- and keyboard-based GUI. The speech-based VUI system developed here alleviates this problem, making it easy to control the app via natural spoken (or typed) commands. To achieve this VUI we evaluated two distinct Automated Speech Recognition (ASR) systems: Chrome's native Speech API and OpenAI's Whisper v3. While Whisper offered broader browser compatibility, its tendency to "hallucinate" with specialized scientific jargon proved very problematic. Consequently, we selected Chrome's ASR for its stability, speed, and reliability. For translating transcribed speech into software commands, we tested two Large Language Model (LLM)-driven approaches: either generating executable code, or calling predefined functions. The function call method, powered by OpenAI's GPT-4o-mini, was ultimately adopted due to its superior safety, efficiency, and reliability over the more complex and error-prone code-generation approach. The resulting VUI is then based on an integration of Chrome's ASR with our LLM-based function-calling module, enabling users to command the application using natural language as shown in a video linked inside this report. We provide links to live examples demonstrating all the intermediate components, and details on how we crafted the LLM's prompt in order to teach it the function calls as well as ways to clean up the transcribed speech and to explain itself while generating function calls. For best demonstration of the final system, we provide a video example.

</details>

---

### 24. [Distributed Dynamic Invariant Causal Prediction in Environmental Time Series](https://arxiv.org/abs/2603.02902)

**基本信息**

- 🔗 arXiv: [`2603.02902`](https://arxiv.org/abs/2603.02902)
- 👥 作者: Ziruo Hao, Tao Yang, Xiaofeng Wu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02902.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从环境时间序列数据中学习动态、不变因果关系的框架。虽然应用领域是环境科学，但其核心方法论——处理高维时序数据、进行鲁棒的因果/结构推理——与“质谱结构推理”中从复杂质谱数据序列中推断分子结构的本质问题高度相似，属于广义的“结构推理”范畴。

**📖 中文摘要**

本文提出了分布式动态不变因果预测框架，用于从具有环境属性的时间序列数据中提取不变的因果关系。该框架旨在在分布式时间序列设置中学习动态因果关系，同时减轻空间混杂变量的影响，且无需数据通信。作者从理论上证明了在标准采样假设下，该框架能在有限通信轮数内恢复稳定的因果预测因子。在合成基准测试和环境分段的真实世界数据集上的实证评估表明，该方法在预测稳定性和准确性方面优于基线方法。该方法在碳监测和天气预报等领域有应用前景。这项工作关注于从复杂时空数据中推理稳健的因果关系，其方法论（不变因果预测）与化学信息学和质谱分析中从高维、噪声数据中推断稳健分子结构或反应规律的核心挑战在理念上相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The extraction of invariant causal relationships from time series data with environmental attributes is critical for robust decision-making in domains such as climate science and environmental monitoring. However, existing methods either emphasize dynamic causal analysis without leveraging environmental contexts or focus on static invariant causal inference, leaving a gap in distributed temporal settings. In this paper, we propose Distributed Dynamic Invariant Causal Prediction in Time-series (DisDy-ICPT), a novel framework that learns dynamic causal relationships over time while mitigating spatial confounding variables without requiring data communication. We theoretically prove that DisDy-ICPT recovers stable causal predictors within a bounded number of communication rounds under standard sampling assumptions. Empirical evaluations on synthetic benchmarks and environment-segmented real-world datasets show that DisDy-ICPT achieves superior predictive stability and accuracy compared to baseline methods A and B. Our approach offers promising applications in carbon monitoring and weather forecasting. Future work will extend DisDy-ICPT to online learning scenarios.

</details>

---

### 25. [Towards Accurate and Interpretable Time-series Forecasting: A Polynomial Learning Approach](https://arxiv.org/abs/2603.02906)

**基本信息**

- 🔗 arXiv: [`2603.02906`](https://arxiv.org/abs/2603.02906)
- 👥 作者: Bo Liu, Shao-Bo Lin, Changmiao Wang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02906.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种兼具高精度和特征级可解释性的时间序列预测方法。其强调的“可解释性”和“结构推理”（通过多项式交互项显式建模关系）与化学信息学、质谱分析中追求模型可解释性、理解数据特征如何贡献于最终结构预测的目标直接相关。

**📖 中文摘要**

本文提出了可解释多项式学习方法，通过多项式表示显式建模原始特征及其任意阶交互，将可解释性融入模型结构。这种设计保留了时间依赖性，提供了特征级可解释性，并通过调整多项式阶数在预测准确性和可解释性之间实现灵活权衡。作者在模拟数据和比特币价格数据上评估了IPL，表明其在保持高预测精度的同时，相比广泛使用的可解释性方法具有更优的可解释性。在实地收集的天线数据上的实验进一步证明，IPL能产生更简单、更高效的早期预警机制。这项工作专注于开发兼具高精度和可解释性的时间序列预测模型。其强调的“特征级可解释性”和“结构推理”思想，对于化学信息学中理解模型如何从质谱等复杂数据中推理出分子结构至关重要，可被视为一种面向“结构推理”可解释性的方法学贡献。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Time series forecasting enables early warning and has driven asset performance management from traditional planned maintenance to predictive maintenance. However, the lack of interpretability in forecasting methods undermines users' trust and complicates debugging for developers. Consequently, interpretable time-series forecasting has attracted increasing research attention. Nevertheless, existing methods suffer from several limitations, including insufficient modeling of temporal dependencies, lack of feature-level interpretability to support early warning, and difficulty in simultaneously achieving the accuracy and interpretability. This paper proposes the interpretable polynomial learning (IPL) method, which integrates interpretability into the model structure by explicitly modeling original features and their interactions of arbitrary order through polynomial representations. This design preserves temporal dependencies, provides feature-level interpretability, and offers a flexible trade-off between prediction accuracy and interpretability by adjusting the polynomial degree. We evaluate IPL on simulated and Bitcoin price data, showing that it achieves high prediction accuracy with superior interpretability compared with widely used explainability methods. Experiments on field-collected antenna data further demonstrate that IPL yields simpler and more efficient early warning mechanisms.

</details>

---

### 26. [SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training](https://arxiv.org/abs/2603.02908)

**基本信息**

- 🔗 arXiv: [`2603.02908`](https://arxiv.org/abs/2603.02908)
- 👥 作者: Qi Zhang, Yifei Wang, Xiaohan Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02908.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于分析和预测大语言模型（LLMs）领域可迁移性的新方法。这直接涉及“化学大模型”在实际应用中面临的关键问题：如何评估和选择适合特定化学任务（如质谱解析）的预训练模型或微调策略，属于化学大模型方法论研究的一部分。

**📖 中文摘要**

本文提出了基于稀疏自编码器的可迁移性评分，一种利用稀疏自编码器来预测大语言模型后训练可迁移性的新指标。该指标识别SAE表示中发生偏移的维度，并计算它们与下游领域的相关性，从而能够在微调之前可靠地估计可迁移性。在多个模型和领域上的大量实验表明，STS能够准确预测监督微调的可迁移性，与实际性能变化之间的皮尔逊相关系数超过0.7。此外，作者初步尝试将STS扩展到强化学习。作者认为STS可以作为一个可解释的工具，用于指导LLMs的后训练策略。这项工作聚焦于分析和预测大语言模型（作为“大模型”的一种）在领域适应中的行为，其提出的分析工具（SAE）和评估指标（STS）对于理解和优化化学领域大模型的迁移和微调具有潜在价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, pre-trained large language models have achieved remarkable success across diverse tasks. Besides the pivotal role of self-supervised pre-training, their effectiveness in downstream applications also depends critically on the post-training process, which adapts models to task-specific data and objectives. However, this process inevitably introduces model shifts that can influence performance in different domains, and how such shifts transfer remains poorly understood. To open up the black box, we propose the SAE-based Transferability Score (STS), a new metric that leverages sparse autoencoders (SAEs) to forecast post-training transferability. Taking supervised fine-tuning as an example, STS identifies shifted dimensions in SAE representations and calculates their correlations with downstream domains, enabling reliable estimation of transferability \textit{before} fine-tuning. Extensive experiments across multiple models and domains show that STS accurately predicts the transferability of supervised fine-tuning, achieving Pearson correlation coefficients above 0.7 with actual performance changes. Beyond this, we take an initial step toward extending STS to reinforcement learning. We believe that STS can serve as an {\color{black} interpretable} tool for guiding post-training strategies in LLMs. Code is available at this https URL .

</details>

---

### 27. [Eliciting Numerical Predictive Distributions of LLMs Without Autoregression](https://arxiv.org/abs/2603.02913)

**基本信息**

- 🔗 arXiv: [`2603.02913`](https://arxiv.org/abs/2603.02913)
- 👥 作者: Julianna Piskorz, Katarzyna Kobalczyk, Mihaela van der Schaar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02913.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探究大语言模型在数值回归任务中的内部表示与不确定性编码。这与“化学大模型”应用于质谱分析（如预测质谱峰强度、化学位移等连续数值）时，对模型预测可靠性和不确定性量化的需求高度相关，属于化学大模型基础能力研究范畴。

**📖 中文摘要**

本文研究了是否可以在不进行显式自回归生成的情况下，从大语言模型的内部表示中恢复其数值预测的分布特性。为此，作者研究了一组回归探针，这些探针经过训练，可以直接从LLM的内部表示中预测其数值输出分布的统计函数（例如，均值、中位数、分位数）。研究结果表明，LLM嵌入携带了关于其预测分布摘要统计信息（包括数值不确定性）的信息信号。这项研究提出了关于LLM如何在数值任务内部编码不确定性，以及基于采样的不确定性感知数值预测方法的轻量级替代方案的可行性等新问题。这项工作探索了大语言模型在数值预测任务中的内部工作机制，特别是其表示中蕴含的不确定性信息。这对于将化学大模型应用于质谱数据解析、谱图预测等需要输出连续数值并评估其置信度的任务具有重要的方法论启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have recently been successfully applied to regression tasks -- such as time series forecasting and tabular prediction -- by leveraging their in-context learning abilities. However, their autoregressive decoding process may be ill-suited to continuous-valued outputs, where obtaining predictive distributions over numerical targets requires repeated sampling, leading to high computational cost and inference time. In this work, we investigate whether distributional properties of LLM predictions can be recovered without explicit autoregressive generation. To this end, we study a set of regression probes trained to predict statistical functionals (e.g., mean, median, quantiles) of the LLM's numerical output distribution directly from its internal representations. Our results suggest that LLM embeddings carry informative signals about summary statistics of their predictive distributions, including the numerical uncertainty. This investigation opens up new questions about how LLMs internally encode uncertainty in numerical tasks, and about the feasibility of lightweight alternatives to sampling-based approaches for uncertainty-aware numerical predictions.

</details>

---

### 28. [On the Structural Limitations of Weight-Based Neural Adaptation and the Role of Reversible Behavioral Learning](https://arxiv.org/abs/2603.02934)

**基本信息**

- 🔗 arXiv: [`2603.02934`](https://arxiv.org/abs/2603.02934)
- 👥 作者: Pardhu Sri Rushi Varma Konduru
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02934.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于大模型（LLMs）适应过程中的结构不可逆性与可逆行为学习。这直接关系到“化学大模型”如何被安全、可控地微调或强化学习以适应新的化学任务（如质谱结构推理），同时避免灾难性遗忘或行为漂移，是化学大模型部署与迭代的关键问题。

**📖 中文摘要**

本研究引入了“结构不可逆性”的概念，用以描述基于共享参数的模型适应（如微调、对齐训练、强化学习）的特征。这种不可逆性指的是任务特定目标与模型表示身份的纠缠。作者表明，当参数被直接修改时，所得模型的行为会与原始模型发生分歧，且这种分歧在没有显式参数快照的情况下无法确定性地逆转。作者引入了可逆行为学习，其中模型行为在结构上与身份参数分离，并可以通过显式的卸载过程确定性地卸载。作者还引入了可恢复性因子作为行为可恢复性的标准化度量，并提供基于模型分歧的额外诊断。实验表明，可逆模型适应能在数值精度内实现回滚，而共享参数突变则表现出持续的重置后分歧。这项工作从理论和方法上探讨了大模型适应过程中的行为持久性与可逆性问题，对于化学大模型在安全、可控地适应新任务（如学习新的质谱解析规则）同时保留核心能力具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural models are usually adapted through changes in parameters shared among model components via fine-tuning, alignment-based training, and reinforcement learning. These changes have been found effective in short-term optimization. However, they result in long-term alterations in the model's base behavior. In this study, we introduce the concept of structural irreversibility as a characteristic of shared-parameter model adaptation. This concept refers to the intertwining of task-specific objectives with the representational identity of the model. We show that when parameters are directly mutated, the resulting model behaves divergently from the original model. This divergence cannot be reversed deterministically without an explicit parameter snapshot. We introduce reversible behavioral learning, in which model behaviors are structurally dissociated from identity parameters and can be deterministically unloaded through an explicit unload process. We also introduce the Recoverability Factor as a normalized measure of behavioral recoverability and provide additional diagnostics based on model divergence. Experiments show that reversible model adaptation achieves rollback within numerical precision, whereas shared-parameter mutation exhibits persistent post-reset divergence.

</details>

---

### 29. [Beyond One-Size-Fits-All: Adaptive Subgraph Denoising for Zero-Shot Graph Learning with Large Language Models](https://arxiv.org/abs/2603.02938)

**基本信息**

- 🔗 arXiv: [`2603.02938`](https://arxiv.org/abs/2603.02938)
- 👥 作者: Fengzhi Li, Liang Zhang, Yuan Zuo 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02938.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型在零样本设置下对图结构数据的推理能力。由于分子通常以图结构表示，这项研究提出的方法（自适应子图提取、去噪、RL优化）可直接应用于或启发“化学大模型”处理分子图相关任务，包括“质谱结构推理”中将谱图信息与分子图关联的挑战。

**📖 中文摘要**

本文针对零样本图学习任务，提出了GraphSSR框架，该框架通过自适应子图提取和去噪来改进基于大语言模型的图推理。具体而言，作者提出了SSR流程，通过“采样-选择-推理”过程，根据特定上下文动态定制子图提取，使模型能够自主过滤掉与任务无关的邻居，克服一刀切的问题。为了内化这种能力，作者开发了SSR-SFT数据合成策略，生成高质量的SSR风格图推理轨迹，用于LLMs的监督微调。此外，作者还提出了SSR-RL，一个两阶段强化学习框架，在提出的SSR流程内显式调节采样和选择操作，以实现自适应子图去噪。这项工作专注于提升大语言模型在零样本图结构数据上的推理能力。图结构是分子表示的基石（如分子图），因此该研究提出的提升LLM处理图数据能力的方法，对于将化学大模型应用于分子性质预测、逆合成分析或质谱谱图到分子图的推理等任务具有直接的方法论价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-based tasks in the zero-shot setting remain a significant challenge due to data scarcity and the inability of traditional Graph Neural Networks (GNNs) to generalize to unseen domains or label spaces. While recent advancements have transitioned toward leveraging Large Language Models (LLMs) as predictors to enhance GNNs, these methods often suffer from cross-modal alignment issues. A recent paradigm (i.e., Graph-R1) overcomes the aforementioned architectural dependencies by adopting a purely text-based format and utilizing LLM-based graph reasoning, showing improved zero-shot generalization. However, it employs a task-agnostic, one-size-fits-all subgraph extraction strategy, which inevitably introduces significant structural noise--irrelevant neighbors and edges--that distorts the LLMs' receptive field and leads to suboptimal predictions. To address this limitation, we introduce GraphSSR, a novel framework designed for adaptive subgraph extraction and denoising in zero-shot LLM-based graph reasoning. Specifically, we propose the SSR pipeline, which dynamically tailors subgraph extraction to specific contexts through a "Sample-Select-Reason" process, enabling the model to autonomously filter out task-irrelevant neighbors and overcome the one-size-fits-all issue. To internalize this capability, we develop SSR-SFT, a data synthesis strategy that generates high-quality SSR-style graph reasoning traces for supervised fine-tuning of LLMs. Furthermore, we propose SSR-RL, a two-stage reinforcement learning framework that explicitly regulates sampling and selection operations within the proposed SSR pipeline designed for adaptive subgraph denoising. By incorporating Authenticity-Reinforced and Denoising-Reinforced RL, we guide the model to achieve accurate predictions using parsimonious, denoised subgraphs for reasoning.

</details>

---

### 30. [ShipTraj-R1: Reinforcing Ship Trajectory Prediction in Large Language Models via Group Relative Policy Optimization](https://arxiv.org/abs/2603.02939)

**基本信息**

- 🔗 arXiv: [`2603.02939`](https://arxiv.org/abs/2603.02939)
- 👥 作者: Yang Zhan, Yunhao Li, Zhang Chao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02939.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型和强化学习（GRPO）的框架，用于解决复杂的时空轨迹预测问题。虽然应用领域是船舶轨迹，但其技术路线（LLM + CoT + 领域特定RL）是构建面向复杂化学数据（如质谱时间序列、分子运动轨迹）的“化学大模型”或“质谱推理智能体”的可行且先进的范式，具有直接的方法论相关性。

**📖 中文摘要**

本文提出了ShipTraj-R1，一个新颖的基于大语言模型的框架，将船舶轨迹预测重新表述为文本到文本的生成问题。该框架包含三个关键部分：(1) 设计包含冲突船舶轨迹信息的动态提示，以引导模型实现自适应思维链推理。(2) 引入基于规则的综合性奖励机制，激励模型的推理格式和预测准确性。(3) 通过领域特定提示和奖励引导的组相对策略优化机制对ShipTraj-R1进行强化，并使用Qwen3作为模型主干。在两个复杂真实世界海事数据集上的大量实验结果表明，与最先进的深度学习和基于LLM的基线相比，所提出的ShipTraj-R1实现了最小的误差。这项工作展示了如何将大语言模型与强化学习（GRPO）结合，专门用于解决一个具有时空结构的复杂预测问题。其方法论（LLM+CoT+RL）对于开发用于化学时空数据（如反应过程模拟、分子动力学轨迹分析）或复杂谱图序列预测的化学大模型具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in reinforcement fine-tuning have significantly improved the reasoning ability of large language models (LLMs). In particular, methods such as group relative policy optimization (GRPO) have demonstrated strong capabilities across various fields. However, applying LLMs to ship trajectory prediction remains largely unexplored. In this paper, we propose ShipTraj-R1, a novel LLM-based framework that reformulates ship trajectory prediction as a text-to-text generation problem. (1) We design a dynamic prompt containing trajectory information about conflicting ships to guide the model to achieve adaptive chain-of-thought (CoT) reasoning. (2) We introduce a comprehensive rule-based reward mechanism to incentivize the reasoning format and prediction accuracy of the model. (3) Our ShipTraj-R1 is reinforced through the GRPO mechanism guided by domain-specific prompts and rewards, and utilizes the Qwen3 as the model backbone. Extensive experimental results on two complex and real-world maritime datasets show that the proposed ShipTraj-R1 achieves the least error compared with state-of-the-art deep learning and LLM-based baselines.

</details>

---

### 31. [Architecting Trust in Artificial Epistemic Agents](https://arxiv.org/abs/2603.02960)

**基本信息**

- 🔗 arXiv: [`2603.02960`](https://arxiv.org/abs/2603.02960)
- 👥 作者: Nahema Marchal, Stephanie Chan, Matija Franklin 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02960.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对大语言模型作为认知主体这一主题的综述和展望性文章，包含了重要的相关讨论。它从伦理、治理和系统设计的角度，深入探讨了包括“化学大模型”在内的AI主体应如何被构建、评估和整合到知识生态系统中，以确保其可靠、可信且有益。这属于对“化学大模型”长远发展和负责任创新的高层思考。

**📖 中文摘要**

本文认为，大语言模型日益扮演着认知主体的角色——能够自主追求认知目标并主动塑造我们共享知识环境的实体。它们策划我们接收的信息，并经常用于生成个人化和高度专业化的建议。因此，它们如何执行这些功能，包括是否可靠以及是否恰当地校准到个人和集体的认知规范，对我们所做的选择具有高度影响。作者主张，认知AI主体在知识创造、策划和综合实践中的潜在影响，特别是在复杂的多主体交互背景下，产生了新的信息相互依赖性，需要对AI的评估和治理进行根本性转变。为了确保有益的人-AI知识生态系统，作者提出了一个以建立和培养认知AI主体的可信度、将AI这些主体与人类认知目标对齐以及强化周围的社会认知基础设施为中心的框架。可信的AI主体必须表现出认知能力、强大的可证伪性和认知上 virtuous 的行为，并得到技术溯源系统和旨在保护人类复原力的“知识庇护所”的支持。这项规范性路线图为确保未来的AI系统在稳健和包容的知识生态系统中充当可靠伙伴提供了路径。这篇文章从哲学、伦理和治理的高层视角，系统论述了作为认知主体的大模型（包括潜在的化学领域大模型）所应具备的特质和所需的社会技术基础设施。对于负责任地开发和应用“化学大模型”具有重要的指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models increasingly function as epistemic agents -- entities that can 1) autonomously pursue epistemic goals and 2) actively shape our shared knowledge environment. They curate the information we receive, often supplanting traditional search-based methods, and are frequently used to generate both personal and deeply specialized advice. How they perform these functions, including whether they are reliable and properly calibrated to both individual and collective epistemic norms, is therefore highly consequential for the choices we make. We argue that the potential impact of epistemic AI agents on practices of knowledge creation, curation and synthesis, particularly in the context of complex multi-agent interactions, creates new informational interdependencies that necessitate a fundamental shift in evaluation and governance of AI. While a well-calibrated ecosystem could augment human judgment and collective decision-making, poorly aligned agents risk causing cognitive deskilling and epistemic drift, making the calibration of these models to human norms a high-stakes necessity. To ensure a beneficial human-AI knowledge ecosystem, we propose a framework centered on building and cultivating the trustworthiness of epistemic AI agents; aligning AI these agents with human epistemic goals; and reinforcing the surrounding socio-epistemic infrastructure. In this context, trustworthy AI agents must demonstrate epistemic competence, robust falsifiability, and epistemically virtuous behaviors, supported by technical provenance systems and "knowledge sanctuaries" designed to protect human resilience. This normative roadmap provides a path toward ensuring that future AI systems act as reliable partners in a robust and inclusive knowledge ecosystem.

</details>

---

### 32. [Delegation and Verification Under AI](https://arxiv.org/abs/2603.02961)

**基本信息**

- 🔗 arXiv: [`2603.02961`](https://arxiv.org/abs/2603.02961)
- 👥 作者: Lingxiao Huang, Wenyang Xiao, Nisheeth K. Vishnoi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02961.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过数学模型分析人类在任务中委托给AI（可视为大模型）并验证其输出的行为动态及其长期影响。这直接关系到“化学大模型”在化学研究、分析检测等实际工作场景中与化学家/分析师的协作模式，研究如何避免过度依赖导致的人类专家技能衰退，是化学大模型融入工作流程时必须考虑的核心问题。

**📖 中文摘要**

本文建模了在AI系统进入工作流程的背景下，工人决定是否将任务执行委托给AI以及投入多少精力验证AI输出的理性决策过程。模型将委托和验证定义为理性工人优化问题的解，并通过在所得最优行动处评估机构中心的效用来定义工人质量。作者正式描述了最优工人工作流程，并表明AI会引发相变，即验证能力上任意微小的差异会导致截然不同的行为。因此，AI可以放大具有强验证可靠性的工人，同时降低那些理性地过度委托并减少监督的工人的机构工人质量，即使基线任务成功率有所提高且不存在行为偏差。这些结果确定了AI重塑机构工人质量和放大具有不同验证可靠性的工人之间质量差异的结构性机制。这篇文章通过数学模型分析了人类与AI（可视为一种“大模型”提供的服务）协作中的委托与验证行为及其长期影响。其研究结论对于在化学研究或分析实验室中部署“化学大模型”（如用于辅助谱图解析）时，如何设计人机协作流程以避免人类技能退化、确保结果可靠性具有重要的启示作用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As AI systems enter institutional workflows, workers must decide whether to delegate task execution to AI and how much effort to invest in verifying AI outputs, while institutions evaluate workers using outcome-based standards that may misalign with workers' private costs. We model delegation and verification as the solution to a rational worker's optimization problem, and define worker quality by evaluating an institution-centered utility (distinct from the worker's objective) at the resulting optimal action. We formally characterize optimal worker workflows and show that AI induces *phase transitions*, where arbitrarily small differences in verification ability lead to sharply different behaviors. As a result, AI can amplify workers with strong verification reliability while degrading institutional worker quality for others who rationally over-delegate and reduce oversight, even when baseline task success improves and no behavioral biases are present. These results identify a structural mechanism by which AI reshapes institutional worker quality and amplifies quality disparities between workers with different verification reliability.

</details>

---

### 33. [OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents](https://arxiv.org/abs/2603.03005)

**基本信息**

- 🔗 arXiv: [`2603.03005`](https://arxiv.org/abs/2603.03005)
- 👥 作者: Yichao Feng, Haoran Luo, Zhenghong Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03005.pdf)

**💡 相关性分析**

满足标准1：论文提出的多智能体、多模型协作框架（OrchMAS）直接围绕如何构建更强大、更灵活的科学推理系统这一核心主题，这与构建用于复杂科学任务（如化学信息学和质谱分析）的“化学大模型”或智能推理系统的目标高度一致。

**📖 中文摘要**

本文提出OrchMAS，一个面向科学领域的交互式两层多模型编排框架，旨在解决复杂多步推理任务。该框架的核心是一个专用的编排模型，它分析任务、动态构建领域感知的推理管道，并实例化具有定制提示的专家代理。执行模型则在生成的指令下执行每个步骤。编排器根据中间反馈迭代更新管道，实现动态重新规划、角色重新分配和跨多轮交互的提示优化。该框架支持集成具有不同能力或成本的大语言模型，以实现性能与效率的权衡。虽然论文主要关注通用科学推理，但其核心思想——通过结构化、异构的模型协作来增强科学推理的鲁棒性和专业性——与构建用于化学信息学和质谱分析等领域的复杂、可解释的“化学大模型”或推理系统高度相关。它为解决“质谱结构推理”等需要多步骤、多专家知识整合的任务提供了一个有前景的架构范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-agent large language model frameworks are promising for complex multi step reasoning, yet existing systems remain weak for scientific and knowledge intensive domains due to static prompts and agent roles, rigid workflows, and homogeneous model reliance, leading to poor domain adaptation, limited reasoning flexibility, and high latency on heterogeneous or long-horizon scientific tasks. They also struggle to revise earlier decisions when intermediate reasoning diverges, reducing reliability in structured and calculation heavy settings. To address these limitations, we propose a scientific domain oriented interactive two tier multi model orchestration framework. A dedicated orchestration model analyzes each task, dynamically constructs a domain aware reasoning pipeline, and instantiates specialized expert agents with tailored prompts, while an execution model performs each step under generated role and instruction specifications. The orchestrator iteratively updates the pipeline based on intermediate feedback, enabling dynamic replanning, role reallocation, and prompt refinement across multi turn interactions, strengthening robustness and specialization for scientific reasoning through structured heterogeneous model collaboration. The framework is model agnostic and supports heterogeneous LLM integration with different capacities or costs, enabling flexible performance efficiency trade offs in practical scientific deployments. Experiments show consistent improvements over existing multi agent systems and strong baselines across diverse reasoning and scientific style benchmarks.

</details>

---

### 34. [Breaking the Prototype Bias Loop: Confidence-Aware Federated Contrastive Learning for Highly Imbalanced Clients](https://arxiv.org/abs/2603.03007)

**基本信息**

- 🔗 arXiv: [`2603.03007`](https://arxiv.org/abs/2603.03007)
- 👥 作者: Tian-Shuang Wu, Shen-Huan Lyu, Ning Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03007.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于对比学习和原型表示的联邦学习框架，其核心方法论（利用数据表征进行推理和分类）与“质谱结构推理”任务中通过质谱数据表征来推断分子结构的方法论有直接关联。

**📖 中文摘要**

本文提出置信感知联邦对比学习（CAFedCL），以解决联邦学习中因客户端数据类别高度不平衡而导致的“原型偏差循环”问题。该框架改进了原型聚合机制，并加强了基于原型的对比对齐。具体而言，CAFedCL采用置信感知聚合机制，利用预测不确定性对高方差的本地原型进行降权。此外，还集成了针对少数类别的生成增强和几何一致性正则化，以稳定类间结构。论文从理论角度提供了基于期望的分析，表明其聚合方法减少了估计方差，从而限制了全局原型漂移并确保收敛。尽管论文聚焦于联邦学习和计算机视觉任务，但其核心方法——利用对比学习和原型表示进行数据表征和推理——与“质谱结构推理”中通过对比学习或原型匹配来推断未知化合物结构的思路在方法论上相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Local class imbalance and data heterogeneity across clients often trap prototype-based federated contrastive learning in a prototype bias loop: biased local prototypes induced by imbalanced data are aggregated into biased global prototypes, which are repeatedly reused as contrastive anchors, accumulating errors across communication rounds. To break this loop, we propose Confidence-Aware Federated Contrastive Learning (CAFedCL), a novel framework that improves the prototype aggregation mechanism and strengthens the contrastive alignment guided by prototypes. CAFedCL employs a confidence-aware aggregation mechanism that leverages predictive uncertainty to downweight high-variance local prototypes. In addition, generative augmentation for minority classes and geometric consistency regularization are integrated to stabilize the structure between classes. From a theoretical perspective, we provide an expectation-based analysis showing that our aggregation reduces estimation variance, thereby bounding global prototype drift and ensuring convergence. Extensive experiments under varying levels of class imbalance and data heterogeneity demonstrate that CAFedCL consistently outperforms representative federated baselines in both accuracy and client fairness.

</details>

---

### 35. [SEHFS: Structural Entropy-Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection](https://arxiv.org/abs/2603.03022)

**基本信息**

- 🔗 arXiv: [`2603.03022`](https://arxiv.org/abs/2603.03022)
- 👥 作者: Cheng Peng, Yonghao Li, Wanfu Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03022.pdf)

**💡 相关性分析**

满足标准1：论文提出的结构熵引导的高阶相关性学习方法，为处理复杂、结构化数据（如分子图或质谱特征关系）提供了新的特征学习和表示框架，这与构建能够理解化学实体间复杂关系的“化学大模型”以及进行“质谱结构推理”的核心挑战直接相关。

**📖 中文摘要**

本文提出SEHFS，一种用于多视图多标签特征选择的新方法。该方法的核心思想是将特征图转换为结构熵最小化的编码树，以量化高阶依赖性的信息成本，从而学习超越成对相关性的高阶特征相关性。具体来说，具有强高阶冗余性的特征在编码树中被分组到单个簇中，同时最小化簇间特征相关性，从而消除簇内和簇间的冗余。此外，该方法采用了一个基于信息论和矩阵方法融合的新框架，学习共享语义矩阵和视图特定贡献矩阵以重建全局视图矩阵，从而增强信息论方法并平衡全局和局部优化。论文从理论上建立了结构熵学习高阶相关性的能力。虽然应用领域是多视图学习，但其核心贡献——一种能够捕获复杂、高阶依赖关系的特征选择和信息理论方法——对于构建能够理解化学结构复杂关系的“化学大模型”，或处理质谱数据中复杂特征关联的“质谱结构推理”模型，具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, multi-view multi-label learning (MVML) has attracted extensive attention due to its close alignment to real-world scenarios. Information-theoretic methods have gained prominence for learning nonlinear correlations. However, two key challenges persist: first, features in real-world data commonly exhibit high-order structural correlations, but existing information-theoretic methods struggle to learn such correlations; second, commonly relying on heuristic optimization, information-theoretic methods are prone to converging to local optima. To address these two challenges, we propose a novel method called Structural Entropy Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection (SEHFS). The core idea of SEHFS is to convert the feature graph into a structural-entropy-minimizing encoding tree, quantifying the information cost of high-order dependencies and thus learning high-order feature correlations beyond pairwise correlations. Specifically, features exhibiting strong high-order redundancy are grouped into a single cluster within the encoding tree, while inter-cluster feaeture correlations are minimized, thereby eliminating redundancy both within and across clusters. Furthermore, a new framework based on the fusion of information theory and matrix methods is adopted, which learns a shared semantic matrix and view-specific contribution matrices to reconstruct a global view matrix, thereby enhancing the information-theoretic method and balancing the global and local optimization. The ability of structural entropy to learn high-order correlations is theoretically established, and and both experiments on eight datasets from various domains and ablation studies demonstrate that SEHFS achieves superior performance in feature selection.

</details>

---

### 36. [Any Resolution Any Geometry: From Multi-View To Multi-Patch](https://arxiv.org/abs/2603.03026)

**基本信息**

- 🔗 arXiv: [`2603.03026`](https://arxiv.org/abs/2603.03026)
- 👥 作者: Wenqing Cui, Zhenyu Li, Mykola Lavreniuk 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03026.pdf)

**💡 相关性分析**

满足标准1：论文提出的多块变换器架构，专注于处理高分辨率、结构化数据并进行全局一致性推理，这种模型设计思路与构建用于处理复杂化学数据（如分子结构、质谱）并进行全局推理的“化学大模型”有概念上的相关性。

**📖 中文摘要**

本文提出超分辨率几何变换器（URGT），将视觉几何接地变换器（VGGT）适配为一个统一的、用于单目高分辨率深度-法线估计的多块变换器。该方法将高分辨率图像分割成多个块，并用预训练模型提供的粗略深度和法线先验进行增强，然后在单次前向传递中联合处理这些块以预测精细化的几何输出。通过跨块注意力强制全局一致性，实现长距离几何推理和共享主干内跨块的信息无缝传播。为了进一步增强空间鲁棒性，引入了GridMix块采样策略。该方法在几何估计任务上达到了最先进的性能。虽然论文聚焦于计算机视觉中的3D几何估计，但其核心架构——一个能够处理高分辨率输入、通过跨块注意力进行全局推理的“变换器”模型——与处理高维、复杂化学或质谱数据，并需要全局一致性推理的“化学大模型”在架构设计思路上有相似之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Joint estimation of surface normals and depth is essential for holistic 3D scene understanding, yet high-resolution prediction remains difficult due to the trade-off between preserving fine local detail and maintaining global consistency. To address this challenge, we propose the Ultra Resolution Geometry Transformer (URGT), which adapts the Visual Geometry Grounded Transformer (VGGT) into a unified multi-patch transformer for monocular high-resolution depth--normal estimation. A single high-resolution image is partitioned into patches that are augmented with coarse depth and normal priors from pre-trained models, and jointly processed in a single forward pass to predict refined geometric outputs. Global coherence is enforced through cross-patch attention, which enables long-range geometric reasoning and seamless propagation of information across patches within a shared backbone. To further enhance spatial robustness, we introduce a GridMix patch sampling strategy that probabilistically samples grid configurations during training, improving inter-patch consistency and generalization. Our method achieves state-of-the-art results on UnrealStereo4K, jointly improving depth and normal estimation, reducing AbsRel from 0.0582 to 0.0291, RMSE from 2.17 to 1.31, and lowering mean angular error from 23.36 degrees to 18.51 degrees, while producing sharper and more stable geometry. The proposed multi-patch framework also demonstrates strong zero-shot and cross-domain generalization and scales effectively to very high resolutions, offering an efficient and extensible solution for high-quality geometry refinement.

</details>

---

### 37. [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](https://arxiv.org/abs/2603.03031)

**基本信息**

- 🔗 arXiv: [`2603.03031`](https://arxiv.org/abs/2603.03031)
- 👥 作者: Xuan Yang, Jiayu Liu, Yuhang Lai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03031.pdf)

**💡 相关性分析**

满足标准1：论文提出的步骤级稀疏自编码器（SSAE）专注于分析和解构复杂推理过程，这对于构建和理解在“化学大模型”或“质谱结构推理”任务中可能涉及的、需要可解释性和可控性的多步骤化学推理模型，具有直接的方法论相关性。

**📖 中文摘要**

本文提出步骤级稀疏自编码器（SSAE），作为一种分析工具，将大语言模型的推理步骤的不同方面解耦为稀疏特征。具体而言，通过精确控制步骤特征在其上下文条件下的稀疏性，在步骤重建中形成信息瓶颈，从而将增量信息与背景信息分离，并将其解耦为几个稀疏激活的维度。实验表明，通过线性探测，可以轻松预测表面信息（如生成长度和首个词分布）以及更复杂的属性（如步骤的正确性和逻辑性）。这些观察表明，大语言模型在生成过程中至少部分地知道这些属性，这为LLMs的自我验证能力提供了基础。这项工作为大语言模型推理过程的可解释性提供了新工具。虽然不直接针对化学领域，但“步骤级推理分析”和“特征解耦”的方法对于理解和构建在“化学大模型”或“质谱结构推理”中可能需要的、可解释的、多步骤的化学推理过程具有重要的方法论启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have achieved strong complex reasoning capabilities through Chain-of-Thought (CoT) reasoning. However, their reasoning patterns remain too complicated to analyze. While Sparse Autoencoders (SAEs) have emerged as a powerful tool for interpretability, existing approaches predominantly operate at the token level, creating a granularity mismatch when capturing more critical step-level information, such as reasoning direction and semantic transitions. In this work, we propose step-level sparse autoencoder (SSAE), which serves as an analytical tool to disentangle different aspects of LLMs' reasoning steps into sparse features. Specifically, by precisely controlling the sparsity of a step feature conditioned on its context, we form an information bottleneck in step reconstruction, which splits incremental information from background information and disentangles it into several sparsely activated dimensions. Experiments on multiple base models and reasoning tasks show the effectiveness of the extracted features. By linear probing, we can easily predict surface-level information, such as generation length and first token distribution, as well as more complicated properties, such as the correctness and logicality of the step. These observations indicate that LLMs should already at least partly know about these properties during generation, which provides the foundation for the self-verification ability of LLMs. The code is available at this https URL

</details>

---

### 38. [Odin: Multi-Signal Graph Intelligence for Autonomous Discovery in Knowledge Graphs](https://arxiv.org/abs/2603.03097)

**基本信息**

- 🔗 arXiv: [`2603.03097`](https://arxiv.org/abs/2603.03097)
- 👥 作者: Muyukani Kizito, Elizabeth Nyambere
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03097.pdf)

**💡 相关性分析**

满足标准1：论文提出的Odin系统是一个用于知识图自主发现和推理的图智能引擎，其核心功能（多信号集成推理、模式发现）与构建能够在化学知识图谱或分子数据库中进行自主推理和结构发现的“化学大模型”或“质谱结构推理”系统直接相关。

**📖 中文摘要**

本文提出Odin，首个用于在知识图中自主发现有意义模式的生产级部署图智能引擎。与基于检索的系统不同，Odin通过COMPASS（复合导向多信号路径评估）分数引导探索，该分数结合了（1）通过个性化PageRank得到的结构重要性，（2）通过神经概率逻辑学习（NPLL）作为判别式过滤器得到的语义合理性，（3）具有可配置衰减的时间相关性，以及（4）通过GNN识别的桥接实体和社区间亲和力分数得到的社区感知引导。这种多信号集成解决了图探索陷入密集局部社区的“回声室”问题。Odin代表了首个在受监管生产环境（如医疗保健和保险）中部署的自主发现系统。虽然应用领域是通用知识图，但其核心能力——通过结合结构、语义、时间和社区信号在复杂图中进行自主模式发现和推理——与在化学知识图或分子数据库中自主发现化学模式、进行结构推理或假设生成的“化学大模型”或“质谱结构推理”系统的目标高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Odin, the first production-deployed graph intelligence engine for autonomous discovery of meaningful patterns in knowledge graphs without prior specification. Unlike retrieval-based systems that answer predefined queries, Odin guides exploration through the COMPASS (Composite Oriented Multi-signal Path Assessment) score, a novel metric that combines (1) structural importance via Personalized PageRank, (2) semantic plausibility through Neural Probabilistic Logic Learning (NPLL) used as a discriminative filter rather than generative model, (3) temporal relevance with configurable decay, and (4) community-aware guidance through GNN-identified bridge entities and inter-community affinity scores. This multi-signal integration, particularly the bridge scoring mechanism, addresses the "echo chamber" problem where graph exploration becomes trapped in dense local communities. We formalize the autonomous discovery problem, prove theoretical properties of our scoring function, and demonstrate that beam search with multi-signal guidance achieves $O(b \cdot h)$ complexity while maintaining high recall compared to exhaustive exploration. To our knowledge, Odin represents the first autonomous discovery system deployed in regulated production environments (healthcare and insurance), demonstrating significant improvements in pattern discovery quality and analyst efficiency. Our approach maintains complete provenance traceability -- a critical requirement for regulated industries where hallucination is unacceptable.

</details>

---

### 39. [MoECLIP: Patch-Specialized Experts for Zero-shot Anomaly Detection](https://arxiv.org/abs/2603.03101)

**基本信息**

- 🔗 arXiv: [`2603.03101`](https://arxiv.org/abs/2603.03101)
- 👥 作者: Jun Yeong Park, JunYoung Seo, Minji Kang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03101.pdf)

**💡 相关性分析**

满足标准1：论文提出的混合专家（MoE）架构，通过动态路由实现输入自适应和专业化处理，这种模型架构设计思想对于构建能够处理化学中多样化、专业化子任务（如不同类别的质谱结构推理）的“化学大模型”具有直接的启发性和相关性。

**📖 中文摘要**

本文提出MoECLIP，一种用于零样本异常检测（ZSAD）任务的混合专家（MoE）架构。该方法通过基于每个图像块的独特特征，将其动态路由到专门的低秩自适应（LoRA）专家，实现块级自适应。此外，为了防止LoRA专家之间的功能冗余，引入了（1）冻结正交特征分离（FOFS），正交分离输入特征空间以迫使专家关注不同的信息，以及（2）单纯形等角紧框架（ETF）损失来规范专家输出以形成最大等角表示。实验在涵盖工业和医疗领域的14个基准数据集上进行。虽然应用是异常检测，但其核心创新——使用混合专家（MoE）架构和自适应路由来实现对输入（如图像块）的细粒度、专业化处理——为构建能够处理化学中不同子领域或不同类型质谱数据的、模块化、专业化的“化学大模型”提供了有前景的架构思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The CLIP model's outstanding generalization has driven recent success in Zero-Shot Anomaly Detection (ZSAD) for detecting anomalies in unseen categories. The core challenge in ZSAD is to specialize the model for anomaly detection tasks while preserving CLIP's powerful generalization capability. Existing approaches attempting to solve this challenge share the fundamental limitation of a patch-agnostic design that processes all patches monolithically without regard for their unique characteristics. To address this limitation, we propose \textbf{MoECLIP}, a Mixture-of-Experts (MoE) architecture for the ZSAD task, which achieves patch-level adaptation by dynamically routing each image patch to a specialized Low-Rank Adaptation (LoRA) expert based on its unique characteristics. Furthermore, to prevent functional redundancy among the LoRA experts, we introduce (1) Frozen Orthogonal Feature Separation (FOFS), which orthogonally separates the input feature space to force experts to focus on distinct information, and (2) a simplex equiangular tight frame (ETF) loss to regulate the expert outputs to form maximally equiangular representations. Comprehensive experimental results across 14 benchmark datasets spanning industrial and medical domains demonstrate that MoECLIP outperforms existing state-of-the-art methods. The code is available at this https URL .

</details>

---

### 40. [The Science Data Lake: A Unified Open Infrastructure Integrating 293 Million Papers Across Eight Scholarly Sources with Embedding-Based Ontology Alignment](https://arxiv.org/abs/2603.03126)

**基本信息**

- 🔗 arXiv: [`2603.03126`](https://arxiv.org/abs/2603.03126)
- 👥 作者: Jonas Wilinski
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03126.pdf)

**💡 相关性分析**

满足标准2：论文提出的“科学数据湖”是一个大规模、多源集成的科学文献数据集和基础设施，为训练或评估“化学大模型”提供了宝贵的数据资源。其包含的化学相关论文和通过本体对齐提供的结构化语义信息，可直接用于化学信息学领域的模型开发和研究。

**📖 中文摘要**

本文介绍了科学数据湖（Science Data Lake），一个基于DuckDB和Parquet文件构建的、可本地部署的基础设施，它通过DOI规范化统一了八个开放学术数据源（包括Semantic Scholar, OpenAlex, SciSciNet, Papers with Code等），同时保留了源级模式。该资源包含约960GB的Parquet文件，涵盖约2.93亿篇唯一可识别的论文。此外，利用BGE-large句子嵌入进行基于嵌入的本体对齐，将4,516个OpenAlex主题映射到13个科学本体（约130万个术语），产生了16,150个映射。该资源是开源的，可通过HuggingFace远程查询，并包含适合基于大语言模型的研究代理的结构化文档。这项工作提供了一个大规模、多源集成的科学文献数据平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scholarly data are largely fragmented across siloed databases with divergent metadata and missing linkages among them. We present the Science Data Lake, a locally-deployable infrastructure built on DuckDB and simple Parquet files that unifies eight open sources - Semantic Scholar, OpenAlex, SciSciNet, Papers with Code, Retraction Watch, Reliance on Science, a preprint-to-published mapping, and Crossref - via DOI normalization while preserving source-level schemas. The resource comprises approximately 960GB of Parquet files spanning ~293 million uniquely identifiable papers across ~22 schemas and ~153 SQL views. An embedding-based ontology alignment using BGE-large sentence embeddings maps 4,516 OpenAlex topics to 13 scientific ontologies (~1.3 million terms), yielding 16,150 mappings covering 99.8% of topics ($\geq 0.65$ threshold) with $F1 = 0.77$ at the recommended $\geq 0.85$ operating point, outperforming TF-IDF, BM25, and Jaro-Winkler baselines on a 300-pair gold-standard evaluation. We validate through 10 automated checks, cross-source citation agreement analysis (pairwise Pearson $r = 0.76$ - $0.87$), and stratified manual annotation. Four vignettes demonstrate cross-source analyses infeasible with any single database. The resource is open source, deployable on a single drive or queryable remotely via HuggingFace, and includes structured documentation suitable for large language model (LLM) based research agents.

</details>

---

### 41. [FEAST: Retrieval-Augmented Multi-Hierarchical Food Classification for the FoodEx2 System](https://arxiv.org/abs/2603.03176)

**基本信息**

- 🔗 arXiv: [`2603.03176`](https://arxiv.org/abs/2603.03176)
- 👥 作者: Lorenzo Molfetta, Alessio Cocchieri, Stefano Fantazzini 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03176.pdf)

**💡 相关性分析**

满足标准1：论文提出的用于复杂层次分类任务的检索增强多阶段框架（FEAST），其方法论（处理层次标签、缓解数据稀疏、学习判别性嵌入）与化学信息学中处理化合物层次分类或质谱谱图分类等任务面临类似挑战，因此具有相关性。

**📖 中文摘要**

本文提出FEAST，一种新颖的检索增强框架，用于将FoodEx2食品分类任务分解为三个阶段：（1）基础术语识别，（2）多标签方面预测，和（3）方面描述符分配。通过利用系统的层次结构来指导训练并进行深度度量学习，FEAST学习具有区分性的嵌入，以缓解数据稀疏性并改善对稀有和细粒度标签的泛化。在多语言FoodEx2基准上的评估表明，FEAST在稀有类别上的F1分数比之前的基线提高了12-38%。虽然应用领域是食品分类，但其核心方法——针对复杂层次分类任务的、结合检索增强和度量学习的多阶段框架——对于处理化学中类似的层次分类问题（如化合物分类、质谱谱图分类）或构建具有细粒度识别能力的化学模型具有方法论上的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hierarchical text classification (HTC) and extreme multi-label classification (XML) tasks face compounded challenges from complex label interdependencies, data sparsity, and extreme output dimensions. These challenges are exemplified in the European Food Safety Authority's FoodEx2 system-a standardized food classification framework essential for food consumption monitoring and contaminant exposure assessment across Europe. FoodEx2 coding transforms natural language food descriptions into a set of codes from multiple standardized hierarchies, but faces implementation barriers due to its complex structure. Given a food description (e.g., "organic yogurt''), the system identifies its base term ("yogurt''), all the applicable facet categories (e.g., "production method''), and then, every relevant facet descriptors to each category (e.g., "organic production''). While existing models perform adequately on well-balanced and semantically dense hierarchies, no work has been applied on the practical constraints imposed by the FoodEx2 system. The limited literature addressing such real-world scenarios further compounds these challenges. We propose FEAST (Food Embedding And Semantic Taxonomy), a novel retrieval-augmented framework that decomposes FoodEx2 classification into a three-stage approach: (1) base term identification, (2) multi-label facet prediction, and (3) facet descriptor assignment. By leveraging the system's hierarchical structure to guide training and performing deep metric learning, FEASTlearns discriminative embeddings that mitigate data sparsity and improve generalization on rare and fine-grained labels. Evaluated on the multilingual FoodEx2 benchmark, FEAST outperforms the prior European's CNN baseline F1 scores by 12-38 % on rare classes.

</details>

---

### 42. [Neuro-Symbolic Artificial Intelligence: A Task-Directed Survey in the Black-Box Models Era](https://arxiv.org/abs/2603.03177)

**基本信息**

- 🔗 arXiv: [`2603.03177`](https://arxiv.org/abs/2603.03177)
- 👥 作者: Giovanni Pio Delvecchio, Lorenzo Molfetta, Gianluca Moro
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03177.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于神经符号人工智能（NeSy）的综述，专门讨论了如何整合符号计算与神经网络以增强推理和可解释性。这对于“化学大模型”和“质谱结构推理”的研究方向具有重要的前瞻性和指导意义，因为化学领域天然适合结合符号规则（化学知识）与数据驱动模型。

**📖 中文摘要**

本文对神经符号人工智能（NeSy）领域进行了以任务为导向的综述，探讨了将符号系统与神经网络结合如何增强可解释性和推理能力。综述审查了NeSy在特定任务上的进展，旨在作为研究人员探索用于现实任务和应用的、可解释的NeSy方法的资源。神经符号方法因其推断或利用行为模式的能力而被广泛认为是实现人类水平智能的可能途径之一。这篇综述系统地梳理了该领域的研究，对于正在寻求结合符号推理（如化学规则）与神经网络学习能力以构建更强大、可解释的“化学大模型”或“质谱结构推理”系统的研究者来说，是一份有价值的参考资料。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of symbolic computing with neural networks has intrigued researchers since the first theorizations of Artificial intelligence (AI). The ability of Neuro-Symbolic (NeSy) methods to infer or exploit behavioral schema has been widely considered as one of the possible proxies for human-level intelligence. However, the limited semantic generalizability and the challenges in declining complex domains with pre-defined patterns and rules hinder their practical implementation in real-world scenarios. The unprecedented results achieved by connectionist systems since the last AI breakthrough in 2017 have raised questions about the competitiveness of NeSy solutions, with particular emphasis on the Natural Language Processing and Computer Vision fields. This survey examines task-specific advancements in the NeSy domain to explore how incorporating symbolic systems can enhance explainability and reasoning capabilities. Our findings are meant to serve as a resource for researchers exploring explainable NeSy methodologies for real-life tasks and applications. Reproducibility details and in-depth comments on each surveyed research work are made available at this https URL .

</details>

---

### 43. [AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework](https://arxiv.org/abs/2603.03233)

**基本信息**

- 🔗 arXiv: [`2603.03233`](https://arxiv.org/abs/2603.03233)
- 👥 作者: Zihang Zeng, Jiaquan Zhang, Pengze Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03233.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用大语言模型（作为化学大模型的一种潜在形式）自动化科学工作流程，这与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一个用于科学人工智能（AI4S）任务的低代码平台，该平台集成了一个贝叶斯对抗多智能体框架。该框架协调三个基于大语言模型（LLM）的智能体（任务管理器、代码生成器和评估器），通过对抗循环和贝叶斯原则动态更新提示分布，以优化代码质量。虽然论文主要关注通用科学代码生成，但其核心是利用大语言模型（作为化学大模型的一种形式）自动化科学工作流程，并解决AI4S领域中的评估不确定性。该平台在跨学科任务（如地球科学）上进行了测试，展示了其可靠性和超越竞争模型的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) demonstrate potentials for automating scientific code generation but face challenges in reliability, error propagation in multi-agent workflows, and evaluation in domains with ill-defined success metrics. We present a Bayesian adversarial multi-agent framework specifically designed for AI for Science (AI4S) tasks in the form of a Low-code Platform (LCP). Three LLM-based agents are coordinated under the Bayesian framework: a Task Manager that structures user inputs into actionable plans and adaptive test cases, a Code Generator that produces candidate solutions, and an Evaluator providing comprehensive feedback. The framework employs an adversarial loop where the Task Manager iteratively refines test cases to challenge the Code Generator, while prompt distributions are dynamically updated using Bayesian principles by integrating code quality metrics: functional correctness, structural alignment, and static analysis. This co-optimization of tests and code reduces dependence on LLM reliability and addresses evaluation uncertainty inherent to scientific tasks. LCP also streamlines human-AI collaboration by translating non-expert prompts into domain-specific requirements, bypassing the need for manual prompt engineering by practitioners without coding backgrounds. Benchmark evaluations demonstrate LCP's effectiveness in generating robust code while minimizing error propagation. The proposed platform is also tested on an Earth Science cross-disciplinary task and demonstrates strong reliability, outperforming competing models.

</details>

---

### 44. [Valet: A Standardized Testbed of Traditional Imperfect-Information Card Games](https://arxiv.org/abs/2603.03252)

**基本信息**

- 🔗 arXiv: [`2603.03252`](https://arxiv.org/abs/2603.03252)
- 👥 作者: Mark Goadrich, Achille Morenville, Éric Piette
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03252.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个标准化的、多样化的游戏测试平台（Valet），该平台可用于评估和基准测试游戏AI算法。虽然不直接针对化学或质谱，但“数据资源相关”标准不限定领域，该论文提供了可用于算法评估的通用数据集/资源。

**📖 中文摘要**

本文介绍了Valet，一个包含21种传统不完美信息纸牌游戏的标准化测试平台。这些游戏涵盖了多种类型、文化、玩家数量、牌组结构、机制和隐藏/揭示信息的方法。为了在不同系统间标准化实现，作者使用RECYCLE卡牌游戏描述语言对每个游戏的规则进行了编码。该工作旨在为不完美信息游戏算法和游戏系统的比较研究提供便利，并提供了基线性能评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI algorithms for imperfect-information games are typically compared using performance metrics on individual games, making it difficult to assess robustness across game choices. Card games are a natural domain for imperfect information due to hidden hands and stochastic draws. To facilitate comparative research on imperfect-information game-playing algorithms and game systems, we introduce Valet, a diverse and comprehensive testbed of 21 traditional imperfect-information card games. These games span multiple genres, cultures, player counts, deck structures, mechanics, winning conditions, and methods of hiding and revealing information. To standardize implementations across systems, we encode the rules of each game in RECYCLE, a card game description language. We empirically characterize each game's branching factor and duration using random simulations, reporting baseline score distributions for a Monte Carlo Tree Search player against random opponents to demonstrate the suitability of Valet as a benchmarking suite.

</details>

---

### 45. [Contextual Invertible World Models: A Neuro-Symbolic Agentic Framework for Colorectal Cancer Drug Response](https://arxiv.org/abs/2603.02274)

**基本信息**

- 🔗 arXiv: [`2603.02274`](https://arxiv.org/abs/2603.02274)
- 👥 作者: Christopher Baker, Karen Rafferty, Hui Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02274.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型（LLM）作为智能体进行生物医学推理和预测，这属于“化学大模型”在药物发现和生物信息学领域的应用。

**📖 中文摘要**

本文提出了一个神经符号智能体框架，用于结直肠癌药物反应预测。该框架集成了一个定量的机器学习世界模型和一个基于大语言模型（LLM）的智能体推理层。系统利用Sanger GDSC数据集，通过显式建模临床背景（如微卫星不稳定性状态）实现了稳健的预测相关性。作者引入了“逆向推理”概念，智能体层通过模拟CRISPR扰动来预测特定基因组编辑如何改变药物敏感性。该框架为癌症研究中的可解释AI提供了一条透明、基于生物学的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Precision oncology is currently limited by the small-N, large-P paradox, where high-dimensional genomic data is abundant, but high-quality drug response samples are often sparse. While deep learning models achieve high predictive accuracy, they remain black boxes that fail to provide the causal mechanisms required for clinical decision-making. We present a Neuro-Symbolic Agentic Framework that bridges this gap by integrating a quantitative machine learning World Model with an LLM-based agentic reasoning layer. Our system utilises a forensic data pipeline built on the Sanger GDSC dataset (N=83), achieving a robust predictive correlation (r=0.504) and a significant performance gain through the explicit modelling of clinical context, specifically Microsatellite Instability (MSI) status. We introduce the concept of Inverse Reasoning, where the agentic layer performs in silico CRISPR perturbations to predict how specific genomic edits, such as APC or TP53 repair, alter drug sensitivity. By distinguishing between therapeutic opportunity and contextual resistance, and validating these findings against human clinical data (p=0.023), our framework provides a transparent, biologically grounded path towards explainable AI in cancer research.

</details>

---

### 46. [Hybrid Machine Learning for Enhanced Prediction of Diffusion Coefficients in Liquids](https://arxiv.org/abs/2603.02761)

**基本信息**

- 🔗 arXiv: [`2603.02761`](https://arxiv.org/abs/2603.02761)
- 👥 作者: Jens Wagner, Zeno Romero, Kerstin Münnemann 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02761.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是开发用于预测化学物质关键物理性质（扩散系数）的机器学习模型，这属于化学信息学中“化学大模型”的应用范畴。2) 论文提供了公开可用的预测模型（ESE）和交互式工具，这构成了一个可用于相关主题研究的“工具”资源。

**📖 中文摘要**

本文介绍了一种新的混合机器学习方法（ESE模型），用于预测分子组分在纯液体溶剂中无限稀释下的扩散系数。该方法将斯托克斯-爱因斯坦方程与机器学习相结合，仅需输入组分的SMILES字符串即可提供严格物理一致的预测。模型在广泛的二元液体体系无限稀释扩散系数文献数据上进行了训练和验证，其预测精度显著高于先前最先进的模型SEGWE。该模型及其源代码完全公开，可通过交互式网页界面访问。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion coefficients are key thermophysical properties for modeling mass transport in liquids, but experimental data are scarce, making reliable prediction methods indispensable. In the present work, we introduce a new method for predicting diffusion coefficients of molecular components at infinite dilution in pure liquid solvents by integrating the Stokes-Einstein (SE) equation with machine learning (ML). Unlike previous ML approaches, the resulting hybrid Enhanced Stokes-Einstein (ESE) model provides strictly physically consistent predictions for diffusion coefficients as a function of temperature across a broad range of binary mixtures. Trained and validated using an extensive compilation of literature data for infinite-dilution diffusion coefficients in binary liquid systems, ESE achieves significantly higher prediction accuracies than the previous state-of-the-art model, SEGWE, while requiring only the SMILES strings encoding of the molecular formulae of the components of interest as additional inputs, which are always available. This simplicity makes ESE broadly applicable, e.g., for process design and optimization. The ESE model and its source code are fully disclosed and are directly accessible via an interactive web interface at this https URL .

</details>

---

### 47. [ChemFlow:A Hierarchical Neural Network for Multiscale Representation Learning in Chemical Mixtures](https://arxiv.org/abs/2603.02810)

**基本信息**

- 🔗 arXiv: [`2603.02810`](https://arxiv.org/abs/2603.02810)
- 👥 作者: Jinming Fan, Chao Qian, Wilhelm T. S. Huck 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02810.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于化学混合物性质预测的图神经网络框架，这直接属于“化学大模型”和化学信息学的研究范畴。

**📖 中文摘要**

本文提出了ChemFlow，一种新颖的分层神经网络框架，用于化学混合物的多尺度表示学习。该框架集成了原子、官能团和分子级别的特征，通过跨层级的信息流来预测复杂化学混合物的物理化学性质。ChemFlow采用原子级特征融合模块生成受混合物状态影响的上下文感知原子表示，并利用双向的官能团-分子注意力机制来捕获混合物内和跨分子的官能团相互作用。通过根据浓度和组成动态调整表示，ChemFlow在预测浓度依赖性性质方面表现出色，并在浓度敏感和浓度无关的系统中显著优于最先进的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of the physicochemical properties of molecular mixtures using graph neural networks remains a significant challenge, as it requires simultaneous embedding of intramolecular interactions while accounting for mixture composition (i.e., concentrations and ratios). Existing approaches are ill-equipped to emulate realistic mixture environments, where densely coupled interactions propagate across hierarchical levels - from atoms and functional groups to entire molecules - and where cross-level information exchange is continuously modulated by composition. To bridge the gap between isolated molecules and realistic chemical environments, we present ChemFlow, a novel hierarchical framework that integrates atomic, functional group, and molecular-level features, facilitating information flow across these levels to predict the behavior of complex chemical mixtures. ChemFlow employs an atomic-level feature fusion module, Chem-embed, to generate context-aware atomic representations influenced by the mixture state and atomic characteristics. Next, bidirectional group-to-molecule and molecule-to-group attention mechanisms enable ChemFlow to capture functional group interactions both within and across molecules in the mixture. By dynamically adjusting representations based on concentration and composition, ChemFlow excels at predicting concentration-dependent properties and significantly outperforms state-of-the-art models in both concentration-sensitive and concentration-independent systems. Extensive experiments demonstrate ChemFlow's superior accuracy and efficiency in modeling complex chemical mixtures.

</details>

---

### 48. [Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT](https://arxiv.org/abs/2603.02952)

**基本信息**

- 🔗 arXiv: [`2603.02952`](https://arxiv.org/abs/2603.02952)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02952.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是对生物医学领域的基础模型（Geneformer和scGPT）进行可解释性分析，这属于“化学大模型”在生物信息学中的延伸应用。2) 论文发布了两个大型特征图谱作为交互式网络平台，这构成了可用于相关研究（如模型可解释性、特征发现）的“数据资源”。

**📖 中文摘要**

本文对单细胞基础模型（Geneformer和scGPT）进行了系统的稀疏自编码器分析，以探究这些模型内部编码的生物学知识。研究在模型的残差流激活上训练了TopK稀疏自编码器，生成了包含数万个可解释特征的图谱。分析表明，这些模型内部化了许多有组织的生物学知识，包括通路成员、蛋白质相互作用、功能模块和层次抽象。然而，当针对基因组规模的CRISPRi扰动数据进行测试时，只有极少数的转录因子显示出调控靶点特异性的特征响应，表明这些模型编码了最小的因果调控逻辑。作者发布了交互式网络平台，供探索两个领先单细胞基础模型中的超过10万个特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Background: Single-cell foundation models such as Geneformer and scGPT encode rich biological information, but whether this includes causal regulatory logic rather than statistical co-expression remains unclear. Sparse autoencoders (SAEs) can resolve superposition in neural networks by decomposing dense activations into interpretable features, yet they have not been systematically applied to biological foundation models. Results: We trained TopK SAEs on residual stream activations from all layers of Geneformer V2-316M (18 layers, d=1152) and scGPT whole-human (12 layers, d=512), producing atlases of 82525 and 24527 features, respectively. Both atlases confirm massive superposition, with 99.8 percent of features invisible to SVD. Systematic characterization reveals rich biological organization: 29 to 59 percent of features annotate to Gene Ontology, KEGG, Reactome, STRING, or TRRUST, with U-shaped layer profiles reflecting hierarchical abstraction. Features organize into co-activation modules (141 in Geneformer, 76 in scGPT), exhibit causal specificity (median 2.36x), and form cross-layer information highways (63 to 99.8 percent). When tested against genome-scale CRISPRi perturbation data, only 3 of 48 transcription factors (6.2 percent) show regulatory-target-specific feature responses. A multi-tissue control yields marginal improvement (10.4 percent, 5 of 48 TFs), establishing model representations as the bottleneck. Conclusions: These models have internalized organized biological knowledge, including pathway membership, protein interactions, functional modules, and hierarchical abstraction, yet they encode minimal causal regulatory logic. We release both feature atlases as interactive web platforms enabling exploration of more than 107000 features across 30 layers of two leading single-cell foundation models.

</details>

---

### 49. [Multiparty Quantum Key Agreement: Architectures, State-of-the-art, and Open Problems](https://arxiv.org/abs/2603.03225)

**基本信息**

- 🔗 arXiv: [`2603.03225`](https://arxiv.org/abs/2603.03225)
- 👥 作者: Malik Mouaji, Saif Al-Kuwari
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03225.pdf)

**💡 相关性分析**

满足标准3：论文是关于“多方量子密钥协商”的综述，虽然量子密钥分发与“质谱结构推理”无直接关联，但论文是专门针对一个特定主题（量子密码协议）的全面综述，符合“综述展望相关”标准。鉴于主题的明确性和综述的深度，应予以纳入。

**📖 中文摘要**

本文对多方量子密钥协商（MQKA）进行了全面综述，将其理解为一个沿三个正交轴组织的设计空间：网络架构、量子资源和安全模型。作者基于这一三维视角对MQKA协议进行了分类，分析了不同安全模型如何影响公平性和抗串谋性，并指出了在可组合安全框架、网络原生集成、设备无关实现等方面的开放挑战。最后，提出了面向后NISQ时代未来量子互联网部署的混合资源、玻色子码编码和公平感知的MQKA研究路线图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multiparty quantum key agreement (MQKA) enables $n \geq 3$ mutually distrustful users to establish a shared secret key through collaborative quantum protocols. In this paper, we provide a comprehensive review where we argue that MQKA is best understood as a design space organized along three orthogonal but tightly coupled axes: (1) network architecture, which determines how quantum states flow between participants; (2) quantum resources, which encode the physical degrees of freedom used for implementation; and (3) security model, which defines trust assumptions about devices and infrastructure. Rather than treating MQKA as a linear sequence of isolated protocols, we develop this three-axis perspective to reveal recurrent patterns, sharp trade-offs, and unexplored design spaces. We classify MQKA protocols into structural families, map them to underlying quantum resources, and analyze how different security models shape fairness and collusion resistance. We further identify open challenges in composable security frameworks, network native integration, device-independent implementations, and propose a research roadmap toward hybrid-resource, bosonic-code-encoded, and fairness-aware MQKA suitable for the future quantum internet deployments in the post-NISQ era.

</details>

---

### 50. [The elbow statistic: Multiscale clustering statistical significance](https://arxiv.org/abs/2603.03235)

**基本信息**

- 🔗 arXiv: [`2603.03235`](https://arxiv.org/abs/2603.03235)
- 👥 作者: Francisco J. Perez-Reche
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03235.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种通用的、算法无关的统计框架（ElbowSig）和相应的统计量，用于评估聚类结果的显著性。这提供了一个可用于数据分析（包括潜在的化学或质谱数据分析）的“工具”或“方法”，符合数据资源/工具相关的标准。

**📖 中文摘要**

本文提出了ElbowSig框架，将启发式的“肘部”方法形式化为一个严格的推断问题，用于评估聚类分析中多尺度结构的统计显著性。该框架的核心是一个从聚类异质性序列导出的归一化离散曲率统计量，该统计量针对非结构化数据的零分布进行评估。作者推导了该零统计量在大样本和高维情况下的渐近性质，并证明该方法是算法无关的，仅需异质性序列即可与多种聚类方法兼容。实验表明，该方法能控制I类错误，并具备解析通常被单分辨率选择标准所掩盖的多尺度组织结构的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Selecting the number of clusters remains a fundamental challenge in unsupervised learning. Existing criteria typically target a single ``optimal'' partition, often overlooking statistically meaningful structure present at multiple resolutions. We introduce ElbowSig, a framework that formalizes the heuristic ``elbow'' method as a rigorous inferential problem. Our approach centers on a normalized discrete curvature statistic derived from the cluster heterogeneity sequence, which is evaluated against a null distribution of unstructured data. We derive the asymptotic properties of this null statistic in both large-sample and high-dimensional regimes, characterizing its baseline behavior and stochastic variability. As an algorithm-agnostic procedure, ElbowSig requires only the heterogeneity sequence and is compatible with a wide range of clustering methods, including hard, fuzzy, and model-based clustering. Extensive experiments on synthetic and empirical datasets demonstrate that the method maintains appropriate Type-I error control while providing the power to resolve multiscale organizational structures that are typically obscured by single-resolution selection criteria.

</details>

---

### 51. [Learning Lagrangian Interaction Dynamics with Sampling-Based Model Order Reduction](https://arxiv.org/abs/2407.03925)

**基本信息**

- 🔗 arXiv: [`2407.03925`](https://arxiv.org/abs/2407.03925)
- 👥 作者: Hrishikesh Viswanath, Yue Chang, Aleksey Panas 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.03925.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于模拟拉格朗日物理系统的数据驱动降阶建模框架（GIOROM），并提供了代码和数据。该框架和资源可用于构建或增强化学信息学领域的物理引导大模型，或作为模拟复杂分子/反应系统（与质谱分析相关）的工具。

**📖 中文摘要**

本文提出了一种基于采样的模型降阶框架（GIOROM），用于高效模拟由拉格朗日动力学控制的物理系统，如流体流动、颗粒介质和弹塑性动力学。该框架通过数据驱动的神经PDE算子直接在物理空间中演化拉格朗日系统，并引入可学习的核参数化，利用时间演化的样本粒子局部空间信息来推断底层解流形。该方法在多种拉格朗日体系中实现了输入维度6.6倍至32倍的降低，同时保持高保真度评估。论文提供了所有代码和数据，可作为开发用于复杂物理系统（可能包括化学反应或分子动力学模拟）的化学大模型或质谱结构推理模型的数据资源或工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Simulating physical systems governed by Lagrangian dynamics often entails solving partial differential equations (PDEs) over high-resolution spatial domains, leading to significant computational expense. Reduced-order modeling (ROM) mitigates this cost by evolving low-dimensional latent representations of the underlying system. While neural ROMs enable querying solutions from latent states at arbitrary spatial points, their latent states typically represent the global domain and struggle to capture localized, highly dynamic behaviors such as fluids. We propose a sampling-based reduction framework that evolves Lagrangian systems directly in physical space over the particles themselves, reducing the number of active degrees of freedom via data-driven neural PDE operators. To enable querying at arbitrary spatial locations, we introduce a learnable kernel parameterization that uses local spatial information from time-evolved sample particles to infer the underlying solution manifold. Empirically, our approach achieves a 6.6x to 32x reduction in input dimensionality while maintaining high-fidelity evaluations across diverse Lagrangian regimes, including fluid flows, granular media, and elastoplastic dynamics. We refer to this framework as GIOROM (Geometry-Informed Reduced-Order Modeling). All code and data are available at: this https URL

</details>

---

### 52. [Unsupervised Representation Learning -- an Invariant Risk Minimization Perspective](https://arxiv.org/abs/2505.12506)

**基本信息**

- 🔗 arXiv: [`2505.12506`](https://arxiv.org/abs/2505.12506)
- 👥 作者: Yotam Norman, Ron Meir
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12506.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕无监督表征学习，旨在学习对分布变化鲁棒的表征。这与构建化学大模型（如用于分子性质预测或反应预测的模型）的核心挑战之一——学习可泛化的、鲁棒的分子表征——直接相关。

**📖 中文摘要**

本文提出了一种新颖的无监督不变风险最小化（IRM）框架，用于在没有标签的情况下学习对分布变化鲁棒的表征。该框架通过特征分布对齐来重新定义不变性，并引入了两种方法：主不变成分分析（PICA）和变分不变自编码器（VIAE）。PICA在假设高斯分布下提取不变方向，而VIAE是一种深度生成模型，用于分离环境不变和环境依赖的潜在因子。该方法基于一个新的“无监督”结构因果模型，支持环境条件样本生成和干预。在合成数据集、修改版MNIST和CelebA上的实验证明了该方法在捕获不变结构、保留相关信息以及跨环境泛化方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a novel unsupervised framework for \emph{Invariant Risk Minimization} (IRM), extending the concept of invariance to settings where labels are unavailable. Traditional IRM methods rely on labeled data to learn representations that are robust to distributional shifts across environments. In contrast, our approach redefines invariance through feature distribution alignment, enabling robust representation learning from unlabeled data. We introduce two methods within this framework: Principal Invariant Component Analysis (PICA), a linear method that extracts invariant directions under Gaussian assumptions, and Variational Invariant Autoencoder (VIAE), a deep generative model that separates environment-invariant and environment-dependent latent factors. Our approach is based on a novel ``unsupervised'' structural causal model and supports environment-conditioned sample-generation and intervention. Empirical evaluations on synthetic dataset, modified versions of MNIST, and CelebA demonstrate the effectiveness of our methods in capturing invariant structure, preserving relevant information, and generalizing across environments without access to labels.

</details>

---

### 53. [ViPlan: A Benchmark for Visual Planning with Symbolic Predicates and Vision-Language Models](https://arxiv.org/abs/2505.13180)

**基本信息**

- 🔗 arXiv: [`2505.13180`](https://arxiv.org/abs/2505.13180)
- 👥 作者: Matteo Merler, Nicola Dainese, Minttu Alakuijala 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13180.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于评估多模态大模型在规划任务中推理能力的基准（ViPlan），并提供了代码和数据集。这个基准可以作为评估化学信息学或质谱分析领域大模型（例如，用于逆合成规划或质谱解析推理的模型）的推理和规划能力的工具或参考框架。

**📖 中文摘要**

本文提出了ViPlan，这是第一个用于比较基于视觉语言模型（VLM）的符号规划方法（VLM作为接地器）与直接VLM规划方法（VLM作为规划器）的开源基准。ViPlan包含两个视觉领域（经典积木世界规划问题的视觉变体和模拟家庭机器人环境）中一系列难度递增的任务。研究发现，在图像接地至关重要且准确的积木世界任务中，VLM作为接地器的方法优于直接VLM规划；而在语言知识有帮助的家庭机器人任务中，直接VLM规划方法则大大优于VLM作为接地器的方法。该基准旨在系统评估VLM在战术、技术和程序维度上的推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating Large Language Models with symbolic planners is a promising direction for obtaining verifiable and grounded plans, with recent work extending this idea to visual domains using Vision-Language Models (VLMs). However, a rigorous comparison with methods that plan directly with VLMs is missing, due to a lack of visual benchmarks that support symbolic planning. We present ViPlan, the first open-source benchmark for comparing VLM-grounded symbolic approaches (VLM-as-grounder) with direct VLM planning methods (VLM-as-planner). ViPlan introduces a series of increasingly challenging tasks in two visual domains: a visual variant of the classic Blocksworld planning problem and a simulated household robotics environment. We find VLM-as-grounder methods to outperform direct VLM planning in Blocksworld (solving 46% of the tasks against 9%), where image grounding is both crucial and accurate. However, in the household robotics tasks, where linguistic knowledge helps, VLM-as-planner methods are greatly superior to VLM-as-grounder approaches (solving 34% of the tasks against 5%), which are hindered by partial observability. Thus, ViPlan domains capture fundamental shortcomings of both planning approaches, which we further diagnose with a qualitative failure analysis. Finally, across methods, we observe no consistent benefit from Chain-of-Thought prompting, suggesting persistent limitations in current VLMs' visual reasoning abilities.

</details>

---

### 54. [Deterministic Bounds and Random Estimates of Metric Tensors on Neuromanifolds](https://arxiv.org/abs/2505.13614)

**基本信息**

- 🔗 arXiv: [`2505.13614`](https://arxiv.org/abs/2505.13614)
- 👥 作者: Ke Sun
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13614.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深度神经网络的几何结构（神经流形）及其Fisher信息度量。理解模型参数空间的几何对于优化、理解和构建更强大的模型（包括化学领域的大模型）至关重要。这项工作提供了分析模型内部表示和优化动态的理论工具，与改进大模型训练和理解的底层研究直接相关。

**📖 中文摘要**

本文研究了深度神经网络参数空间（神经流形）上的Fisher信息度量张量。聚焦于神经分类器，作者返回到一个低维的概率分布空间（核心空间），并检查其Fisher信息矩阵的谱和包络。将这些发现扩展到神经流形上度量张量的确定性边界。此外，引入了一种基于Hutchinson迹方法的无偏随机估计器，并推导了相关边界。该估计器可以高效评估，每次反向传播的标准差以真实值为界（最多缩放）。这项工作为理论和实践提供了可靠且可扩展的度量张量计算方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The high-dimensional parameter space of deep neural networks -- the neuromanifold -- is endowed with a unique metric tensor defined by the Fisher information. Reliable and scalable computation of this metric tensor is valuable for theorists and practitioners. Focusing on neural classifiers, we return to a low-dimensional space of probability distributions, which we call the core space, and examine the spectrum and envelopes of its Fisher information matrix. We extend our discoveries there to deterministic bounds for the metric tensor on the neuromanifold. We introduce an unbiased random estimator based on Hutchinson's trace method and derive related bounds. It can be evaluated efficiently with a single backward pass per batch, with a standard deviation bounded by the true value up to scaling.

</details>

---

### 55. [Automatic and Structure-Aware Sparsification of Hybrid Neural ODEs](https://arxiv.org/abs/2505.18996)

**基本信息**

- 🔗 arXiv: [`2505.18996`](https://arxiv.org/abs/2505.18996)
- 👥 作者: Bob Junyi Zou, Lu Tian
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.18996.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于混合神经ODE（结合了机理模型和神经网络）的自动状态选择和结构优化方法。这种将领域知识（机理）与数据驱动学习相结合的框架，与构建用于化学动力学、反应预测或分子系统模拟的“化学大模型”的研究范式高度一致。

**📖 中文摘要**

本文提出了一种新的混合管道，用于在机理神经常微分方程（神经ODE）中自动选择状态和优化结构。混合神经ODE将机理模型与神经ODE相结合，在数据稀缺的医疗保健等场景中具有优势。然而，机理模型带来的过多潜在状态和相互作用可能导致训练效率低下和过拟合。所提出的方法结合了领域知识引导的图修改和数据驱动的正则化，以稀疏化模型，在保留机理合理性的同时提高预测性能和稳定性。在合成数据和真实世界数据上的实验显示了该方法在实现期望稀疏性的同时，提高了预测性能和鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hybrid neural ordinary differential equations (neural ODEs) integrate mechanistic models with neural ODEs, offering strong inductive bias and flexibility, and are particularly advantageous in data-scarce healthcare settings. However, excessive latent states and interactions from mechanistic models can lead to training inefficiency and over-fitting, limiting practical effectiveness of hybrid neural ODEs. In response, we propose a new hybrid pipeline for automatic state selection and structure optimization in mechanistic neural ODEs, combining domain-informed graph modifications with data-driven regularization to sparsify the model for improving predictive performance and stability while retaining mechanistic plausibility. Experiments on synthetic and real-world data show improved predictive performance and robustness with desired sparsity, establishing an effective solution for hybrid model reduction in healthcare applications.

</details>

---

### 56. [Learning of Population Dynamics: Inverse Optimization Meets JKO Scheme](https://arxiv.org/abs/2506.01502)

**基本信息**

- 🔗 arXiv: [`2506.01502`](https://arxiv.org/abs/2506.01502)
- 👥 作者: Mikhail Persiianov, Jiawei Chen, Petr Mokrov 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.01502.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是学习群体动力学，即从观测数据中推断控制粒子（或实体）演化的动态过程。这与质谱结构推理中的一个核心问题相关：从质谱数据的时间序列或不同条件下的测量中，推断出潜在的分子结构演化或反应路径。该论文提出的框架可能为动态化学系统的建模提供方法论参考。

**📖 中文摘要**

本文提出了iJKOnet，一种结合JKO框架和逆优化技术来学习群体动力学的方法。学习群体动力学涉及从离散时间点的样本演化快照中恢复控制粒子演化的底层过程。该方法将问题表述为概率空间中的能量最小化问题，并利用著名的JKO方案进行高效时间离散化。iJKOnet依赖于传统的端到端对抗训练过程，不需要限制性的架构选择（例如输入凸神经网络）。作者为该方法的理论保证提供了证明，并展示了其优于先前基于JKO的方法的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning population dynamics involves recovering the underlying process that governs particle evolution, given evolutionary snapshots of samples at discrete time points. Recent methods frame this as an energy minimization problem in probability space and leverage the celebrated JKO scheme for efficient time discretization. In this work, we introduce $\texttt{iJKOnet}$, an approach that combines the JKO framework with inverse optimization techniques to learn population dynamics. Our method relies on a conventional $\textit{end-to-end}$ adversarial training procedure and does not require restrictive architectural choices, e.g., input-convex neural networks. We establish theoretical guarantees for our methodology and demonstrate improved performance over prior JKO-based methods. The code of $\texttt{iJKOnet}$ is available at this https URL .

</details>

---

### 57. [RNE: plug-and-play diffusion inference-time control and energy-based training](https://arxiv.org/abs/2506.05668)

**基本信息**

- 🔗 arXiv: [`2506.05668`](https://arxiv.org/abs/2506.05668)
- 👥 作者: Jiajun He, José Miguel Hernández-Lobato, Yuanqi Du 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.05668.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是提出一个统一的框架（RNE），用于扩散模型的密度估计、推理时间控制和能量模型训练。这直接与生成模型（包括可能用于分子生成或质谱模拟的扩散模型）的底层方法论发展相关。同时，该框架作为一种新的工具，可用于改进或控制化学大模型（特别是基于扩散的模型）的生成过程。

**📖 中文摘要**

本文介绍了Radon-Nikodym估计器（RNE），基于路径分布之间的密度比概念，揭示了边缘密度和转移核之间的基本联系，提供了一个灵活的即插即用框架，将（1）扩散密度估计、（2）推理时间控制和（3）基于能量的扩散训练统一在一个视角下。实验表明，RNE在推理时间控制应用（如退火和模型组合）中提供了强大的结果，并具有有希望的推理时间缩放性能，同时为训练基于能量的扩散模型实现了一种简单而有效的正则化。此外，RNE是模态无关的，不仅适用于连续扩散模型，也适用于离散扩散模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models generate data by removing noise gradually, which corresponds to the time-reversal of a noising process. However, access to only the denoising kernels is often insufficient. In many applications, we need the knowledge of the marginal densities along the generation trajectory, which enables tasks such as inference-time control. To address this gap, in this paper, we introduce the Radon-Nikodym Estimator (RNE). Based on the concept of the \textit{density ratio} between path distributions, it reveals a fundamental connection between marginal densities and transition kernels, providing a flexible plug-and-play framework that unifies (1) diffusion density estimation, (2) inference-time control, and (3) energy-based diffusion training under a single perspective. Experiments demonstrate that RNE delivers strong results in inference-time control applications, such as annealing and model composition, with promising inference-time scaling performance, and achieves a simple yet efficient regularisation for training energy-based diffusion models. Additionally, our proposed RNE is modality-agnostic and applicable not only to continuous diffusion models but also to their discrete diffusion counterparts.

</details>

---

### 58. [Federated ADMM from Bayesian Duality](https://arxiv.org/abs/2506.13150)

**基本信息**

- 🔗 arXiv: [`2506.13150`](https://arxiv.org/abs/2506.13150)
- 👥 作者: Thomas Möllenhoff, Siddharth Swaroop, Finale Doshi-Velez 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.13150.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种基于贝叶斯对偶性的新框架，用于推广联邦优化算法（ADMM）。虽然应用场景是联邦学习，但其核心贡献在于优化算法和概率建模方法的创新。开发更高效、更强大的优化算法是训练大规模化学模型（化学大模型）的基础支撑技术之一，因此该研究与模型训练方法的进步相关。

**📖 中文摘要**

本文提出了一种新的贝叶斯方法来推广联邦交替方向乘子法（ADMM）。作者展示了变分贝叶斯（VB）目标的解与一种对偶结构相关联，这种结构不仅类似于ADMM不动点的结构，而且推广了它。例如，当在各项同性高斯族上优化VB目标时，可以恢复出类似ADMM的更新；而对于其他指数族分布，则可以得到新的非平凡扩展。这些扩展包括一个在二次目标上一步收敛的类牛顿变体，以及一个在深度异构情况下能带来高达7%准确率提升的类Adam变体。这项工作为推广ADMM和其他原始-对偶方法开辟了一条新的贝叶斯途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Bayesian approach to generalize the federated Alternating Direction Method of Multipliers (ADMM). We show that the solutions of variational-Bayesian (VB) objectives are associated with a duality structure that not only resembles the structure of ADMM's fixed-points but also generalizes it. For example, ADMM-like updates are recovered when the VB objective is optimized over the isotropic-Gaussian family, and new non-trivial extensions are obtained for other exponential-family distributions. These extensions include a Newton-like variant that converges in one step on quadratic objectives and an Adam-like variant that yields up to 7% accuracy boosts for deep heterogeneous cases. Our work opens a new Bayesian way to generalize ADMM and other primal-dual methods.

</details>

---

### 59. [Evolutionary Caching to Accelerate Your Off-the-Shelf Diffusion Model](https://arxiv.org/abs/2506.15682)

**基本信息**

- 🔗 arXiv: [`2506.15682`](https://arxiv.org/abs/2506.15682)
- 👥 作者: Anirud Aggarwal, Abhinav Shrivastava, Matthew Gwilliam
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.15682.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于加速扩散模型推理的通用工具（ECAD算法）。虽然主要应用于图像生成，但其核心方法——通过优化缓存策略来加速生成过程——可以迁移到其他领域的扩散模型，包括可能用于分子生成或质谱数据生成的化学扩散模型。这为相关领域的研究者提供了一个潜在的效率提升工具。

**📖 中文摘要**

本文提出了ECAD（进化缓存加速扩散模型），一种遗传算法，用于学习高效的、针对特定模型的缓存调度策略，形成一个帕累托前沿，仅使用少量校准提示。ECAD不需要修改网络参数或参考图像。它提供了显著的推理加速，实现了对质量-延迟权衡的细粒度控制，并能无缝适应不同的扩散模型。值得注意的是，ECAD学习到的调度策略可以有效地泛化到校准期间未见的分辨率和模型变体。作者在PixArt-alpha、PixArt-Sigma和FLUX.1-dev等模型上使用多个指标（FID、CLIP、Image Reward）和多样化基准（COCO、MJHQ-30k、PartiPrompts）进行了评估，证明了其相对于先前方法的持续改进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion-based image generation models excel at producing high-quality synthetic content, but suffer from slow and computationally expensive inference. Prior work has attempted to mitigate this by caching and reusing features within diffusion transformers across inference steps. These methods, however, often rely on rigid heuristics that result in limited acceleration or poor generalization across architectures. We propose Evolutionary Caching to Accelerate Diffusion models (ECAD), a genetic algorithm that learns efficient, per-model, caching schedules forming a Pareto frontier, using only a small set of calibration prompts. ECAD requires no modifications to network parameters or reference images. It offers significant inference speedups, enables fine-grained control over the quality-latency trade-off, and adapts seamlessly to different diffusion models. Notably, ECAD's learned schedules can generalize effectively to resolutions and model variants not seen during calibration. We evaluate ECAD on PixArt-alpha, PixArt-Sigma, and FLUX$.$1-dev using multiple metrics (FID, CLIP, Image Reward) across diverse benchmarks (COCO, MJHQ-30k, PartiPrompts), demonstrating consistent improvements over previous approaches. On PixArt-alpha, ECAD identifies a schedule that outperforms the previous state-of-the-art method by 4.47 COCO FID while increasing inference speedup from 2.35x to 2.58x. Our results establish ECAD as a scalable and generalizable approach for accelerating diffusion inference. Our project page and code are available here: this https URL

</details>

---

### 60. [LEDOM: Reverse Language Model](https://arxiv.org/abs/2507.01335)

**基本信息**

- 🔗 arXiv: [`2507.01335`](https://arxiv.org/abs/2507.01335)
- 👥 作者: Xunjian Yin, Sitao Cheng, Yuxi Xie 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.01335.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是训练和研究纯反向语言模型，并探索其独特的推理能力（如溯因推理）以及通过与正向模型结合来提升推理质量的方法。这种对模型推理机制、双向信息利用的深入研究，与提升化学大模型（例如用于逆合成分析或反应条件推理）的推理能力和可靠性的目标直接相关。

**📖 中文摘要**

本文探索了纯反向自回归语言模型的训练（LEDOM，2B/7B参数），并发现其发展出与正向模型不同的能力，包括溯因推理、问题合成以及自然解决逆转诅咒。然后，作者探索了反向模型的一个应用：通过噪声信道对偶性结合正向似然P(y|x)和反向后验P(x|y)。提出了反向奖励（Reverse Reward），它使用反向后验估计对正向输出进行重排序，并证明双向评分可以惩罚那些反向重建质量下降的幻觉推理链。反向奖励在AIME 2024和AMC 2023等多个强基线上实现了高达6.6%和15%的性能提升。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autoregressive language models are trained exclusively left-to-right. We explore the complementary factorization, training right-to-left at scale, and ask what reasoning patterns emerge when a model conditions on future context to predict the past. We train LEDOM, an open-source purely reverse autoregressive language model (2B/7B parameters, 435B tokens), and find it develops capabilities distinct from forward models, including abductive inference, question synthesis, and natural resolution of the reversal curse. We then explore one application of the reverse model: combining forward likelihood $P(y \mid x)$ with reverse posterior $P(x \mid y)$ through noisy channel duality. We propose Reverse Reward, which reranks forward outputs using reverse posterior estimates, and prove that bidirectional scoring penalizes hallucinated reasoning chains whose backward reconstruction degrades. Reverse Reward yields gains of up to 6.6\% on AIME 2024 and 15\% on AMC 2023 across multiple strong baselines. We release all models, code, and data here.

</details>

---

### 61. [Prior-based Noisy Text Data Filtering: Fast and Strong Alternative For Perplexity](https://arxiv.org/abs/2509.18577)

**基本信息**

- 🔗 arXiv: [`2509.18577`](https://arxiv.org/abs/2509.18577)
- 👥 作者: Yeongbin Seo, Gayoung Kim, Jaehyung Kim 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.18577.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效的数据过滤方法，该方法可用于构建高质量的数据集，这对于训练化学大模型或为质谱结构推理任务准备数据至关重要，属于数据资源相关的贡献。

**📖 中文摘要**

本文提出了一种基于先验的文本数据过滤方法，作为困惑度（PPL）过滤的快速且强大的替代方案。该方法利用语料库级别的词频统计来估计词元先验，并基于词元先验的均值和标准差来过滤文档。该方法无需模型推理，计算成本极低（比PPL过滤快1000倍以上），且在20个下游基准测试中取得了最高的平均性能。论文还展示了该方法对代码和数学等符号语言以及多语言语料库的适用性。虽然论文主要关注LLM预训练数据筛选，但其核心方法——利用统计先验进行数据质量评估和筛选——与化学信息学中构建高质量数据集（例如用于训练化学大模型或质谱结构推理模型的数据集）的理念高度相关，可被视为一种数据预处理和资源构建工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As large language models (LLMs) are pretrained on massive web corpora, careful selection of data becomes essential to ensure effective and efficient learning. While perplexity (PPL)-based filtering has shown strong performance, it suffers from drawbacks: substantial time costs and inherent unreliability of the model when handling noisy or out-of-distribution samples. In this work, we propose a simple yet powerful alternative: a prior-based data filtering method that estimates token priors using corpus-level term frequency statistics, inspired by linguistic insights on word roles and lexical density. Our approach filters documents based on the mean and standard deviation of token priors, serving as a fast proxy to PPL while requiring no model inference. Despite its simplicity, the prior-based filter achieves the highest average performance across 20 downstream benchmarks, while reducing time cost by over 1000x compared to PPL-based filtering. We further demonstrate its applicability to symbolic languages such as code and math, and its dynamic adaptability to multilingual corpora without supervision

</details>

---

### 62. [LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning](https://arxiv.org/abs/2510.04573)

**基本信息**

- 🔗 arXiv: [`2510.04573`](https://arxiv.org/abs/2510.04573)
- 👥 作者: Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04573.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的新型推理框架（LaDiR），用于增强模型的生成和推理能力。这种方法论与“化学大模型”中涉及分子生成、性质预测等生成式任务，以及“质谱结构推理”中从数据生成分子结构的核心主题直接相关，提供了可借鉴的技术路径。

**📖 中文摘要**

本文提出LaDiR（潜在扩散推理器），一种新颖的推理框架，它将连续潜在表示的表达能力与潜在扩散模型的迭代优化能力相结合，用于增强现有大语言模型（LLM）的推理。该框架首先使用变分自编码器（VAE）构建一个结构化的潜在推理空间，将文本推理步骤编码为“思想块”词元。然后，利用一个潜在扩散模型学习对潜在思想块进行去噪，该模型采用块状双向注意力掩码，支持长程规划和迭代优化。这种方法允许高效并行生成多样化的推理轨迹，使模型能够整体规划和修订推理过程。在数学推理和规划基准测试上的实验表明，LaDiR在准确性、多样性和可解释性上均优于现有的自回归、基于扩散和潜在推理方法。虽然论文主要针对通用文本推理，但其核心思想——使用扩散模型在潜在空间中进行结构化、可迭代的推理生成——与“化学大模型”中分子生成、逆合成规划或“质谱结构推理”中从谱图到分子结构的生成式推理在方法论上高度相似，为这些领域的模型设计提供了新的范式参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) demonstrate their reasoning ability through chain-of-thought (CoT) generation. However, LLM's autoregressive decoding may limit the ability to revisit and refine earlier tokens in a holistic manner, which can also lead to inefficient exploration for diverse solutions. In this paper, we propose LaDiR (Latent Diffusion Reasoner), a novel reasoning framework that unifies the expressiveness of continuous latent representation with the iterative refinement capabilities of latent diffusion models for an existing LLM. We first construct a structured latent reasoning space using a Variational Autoencoder (VAE) that encodes text reasoning steps into blocks of thought tokens, preserving semantic information and interpretability while offering compact but expressive representations. Subsequently, we utilize a latent diffusion model that learns to denoise a block of latent thought tokens with a blockwise bidirectional attention mask, enabling longer horizon and iterative refinement with adaptive test-time compute. This design allows efficient parallel generation of diverse reasoning trajectories, allowing the model to plan and revise the reasoning process holistically. We conduct evaluations on a suite of mathematical reasoning and planning benchmarks. Empirical results show that LaDiR consistently improves accuracy, diversity, and interpretability over existing autoregressive, diffusion-based, and latent reasoning methods, revealing a new paradigm for text reasoning with latent diffusion.

</details>

---

### 63. [A Set of Quebec-French Corpus of Regional Expressions and Terms](https://arxiv.org/abs/2510.05026)

**基本信息**

- 🔗 arXiv: [`2510.05026`](https://arxiv.org/abs/2510.05026)
- 👥 作者: David Beauchemin, Yan Tremblay, Mohamed Amine Youssef 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.05026.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是创建并发布了用于评估模型方言理解能力的专用基准数据集。这种构建和发布领域特定评估资源的行为，与为“化学大模型”和“质谱结构推理”任务创建标准化评估数据集和基准的努力高度相关，属于数据/资源贡献。

**📖 中文摘要**

本文提出了两个新的基准数据集：QFrCoRE（包含4,633个魁北克法语习语实例）和QFrCoRT（包含171个魁北克法语区域性习语词实例），以及一个用于法国本土法语表达的基准MFrCoE（包含4,938个短语）。这些数据集旨在结合方言理解和习语理解任务，用于评估大语言模型（LLM）的方言能力。论文详细说明了数据集的构建方法，并通过对111个LLM的实验，揭示了模型在方言能力上的关键差异：虽然模型在法国本土法语上表现良好，但65.8%的模型在魁北克习语上表现显著更差。这项工作为量化方言差距提供了可靠工具。虽然论文聚焦于自然语言处理中的方言评估，但其核心贡献——构建高质量、领域特定（此处是方言习语）的评估数据集和基准——与化学信息学和质谱分析领域构建评估“化学大模型”或“质谱结构推理”模型性能的专用基准数据集（例如，特定类型的分子性质预测、谱图-结构匹配任务）在理念和实践上完全一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The tasks of idiom understanding and dialect understanding are both well-established benchmarks in natural language processing. In this paper, we propose combining them, and using regional idioms as a test of dialect understanding. Towards this end, we propose two new benchmark datasets for the Quebec dialect of French: QFrCoRE, which contains 4,633 instances of idiomatic phrases, and QFrCoRT, which comprises 171 regional instances of idiomatic words, and a new benchmark for French Metropolitan expressions, MFrCoE, which comprises 4,938 phrases. We explain how to construct these corpora, so that our methodology can be replicated for other dialects. Our experiments with 111 LLMs reveal a critical disparity in dialectal competence: while models perform well on French Metropolitan , 65.8% of them perform significantly worse on Quebec idioms, with only 9.0% favoring the regional dialect. These results confirm that our benchmarks are a reliable tool for quantifying the dialect gap and that prestige-language proficiency does not guarantee regional dialect understanding.

</details>

---

### 64. [Auditing Information Disclosure During LLM-Scale Gradient Descent Using Gradient Uniqueness](https://arxiv.org/abs/2510.10902)

**基本信息**

- 🔗 arXiv: [`2510.10902`](https://arxiv.org/abs/2510.10902)
- 👥 作者: Sleem Abdelghafar, Maryam Aliakbarpour, Chris Jermaine
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.10902.pdf)

**💡 相关性分析**

满足标准1：论文提出的梯度唯一性（GNQ）度量及其计算框架，核心是分析和量化机器学习模型（特别是大模型）训练过程中的信息泄露。这种方法论可直接应用于审计“化学大模型”或“质谱结构推理”模型在训练时是否记忆了特定分子或谱图数据，与核心主题中模型的可解释性、安全性和可靠性评估直接相关。

**📖 中文摘要**

本文提出了梯度唯一性（GNQ），一种原则性的、与攻击无关的度量标准，用于审计在大语言模型（LLM）训练期间通过梯度下降嵌入到模型中的关于单个训练点的信息量。GNQ源自信息论上界，无需对每个数据点进行昂贵的矩阵求逆计算。作者进一步引入了批量空间幽灵GNQ（BS-Ghost GNQ）这一高效算法，在更小的批量空间中进行计算，并以最小的计算开销“在运行中”计算GNQ。实验验证表明，GNQ成功考虑了先验/常识知识，并能强烈预测目标攻击中的序列可提取性，揭示了在LLM训练过程中披露风险如何异质地集中在特定样本上。虽然论文主要关注LLM训练中的隐私审计，但其核心方法——量化模型参数更新（梯度）与单个训练数据点之间的关联强度——对于化学信息学领域具有重要启示。例如，在训练用于“质谱结构推理”或“化学大模型”时，可以使用类似的方法来审计模型是否过度记忆了训练集中某些特定（可能是敏感或受专利保护的）分子结构，从而评估模型的知识泄露风险和泛化可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Disclosing information via the publication of a machine learning model poses significant privacy risks. However, auditing this disclosure across every datapoint during the training of Large Language Models (LLMs) is computationally prohibitive. In this paper, we present Gradient Uniqueness (GNQ), a principled, attack-agnostic metric derived from an information-theoretic upper bound on the amount of information embedded in a model about individual training points via gradient descent. While naively computing GNQ requires forming and inverting an $P \times P$ matrix for every datapoint (for a model with $P$ parameters), we introduce Batch-Space Ghost GNQ (BS-Ghost GNQ). This efficient algorithm performs all computations in a much smaller batch-space and leverages ghost kernels to compute GNQ ``in-run'' with minimal computational overhead. We empirically validate that GNQ successfully accounts for prior/common knowledge. Our evaluation demonstrates that GNQ strongly predicts sequence extractability in targeted attacks and reveals how disclosure risk concentrates heterogeneously on specific examples over the course of LLM training.

</details>

---

### 65. [Narrow Finetuning Leaves Clearly Readable Traces in Activation Differences](https://arxiv.org/abs/2510.13900)

**基本信息**

- 🔗 arXiv: [`2510.13900`](https://arxiv.org/abs/2510.13900)
- 👥 作者: Julian Minder, Clément Dumas, Stewart Slocum 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.13900.pdf)

**💡 相关性分析**

满足标准1：论文核心研究了窄域微调对LLM内部表示的影响，并提出了分析这种影响（模型差分）的方法。这对于理解“化学大模型”在经过特定化学任务（如逆合成、毒性预测）微调后的行为变化、内部知识表征以及潜在的过拟合问题具有直接相关性，属于对模型行为机理的核心研究。

**📖 中文摘要**

本文研究表明，在狭窄领域（narrow domain）上对大型语言模型（LLM）进行微调会在模型激活中产生强烈的、可解释的偏差。通过分析微调前后模型的差异（模型差分），作者发现只需分析模型在随机文本前几个词元上的激活差异，并将这种差异添加到模型激活中进行引导，就能生成与微调数据格式和内容相似的文本。他们创建了一个基于LLM的可解释性代理来理解微调领域，在获得这种偏差信息后，该代理的性能显著优于仅使用简单提示的基线代理。分析涵盖了不同架构和规模的模型，涉及虚假事实微调、突发错位、潜意识学习等场景。论文指出，这种偏差可能反映了过拟合，并发现将预训练数据混合到微调语料中可以很大程度上消除它们。这项工作揭示了窄域微调模型在其激活中留有训练目标的显著痕迹，警告AI安全研究人员使用此类模型作为研究更广泛微调（如聊天微调）的代理可能不现实。虽然论文主要针对通用NLP中的模型可解释性和安全性，但其揭示的“窄域微调在模型内部留下可检测特征”的现象，对于“化学大模型”的领域适应（例如，在特定化学反应或分子性质预测任务上微调）具有重要参考价值。它提供了分析模型在化学领域微调后内部表示变化的方法，并警示了过拟合和领域偏移的风险。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Finetuning on narrow domains has become an essential tool to adapt Large Language Models (LLMs) to specific tasks and to create models with known unusual properties that are useful for research. We show that narrow finetuning creates strong biases in LLM activations that can be interpreted to understand the finetuning domain. These biases can be discovered using simple tools from model diffing - the study of differences between models before and after finetuning. In particular, analyzing activation differences on the first few tokens of random text and steering by adding this difference to the model activations produces text similar to the format and general content of the finetuning data. We demonstrate that these analyses contain crucial information by creating an LLM-based interpretability agent to understand the finetuning domain. With access to the bias, the agent performs significantly better compared to baseline agents using simple prompting. Our analysis spans synthetic document finetuning for false facts, emergent misalignment, subliminal learning, and taboo word guessing game models across different architectures (Gemma, LLaMA, Qwen) and scales (1B to 32B parameters). We suspect these biases reflect overfitting and find that mixing pretraining data into the finetuning corpus largely removes them, though residual risks may remain. Our work (1) demonstrates that narrowly finetuned models have salient traces of their training objective in their activations and suggests ways to improve how they are trained, (2) warns AI safety and interpretability researchers that the common practice of using such models as a proxy for studying broader finetuning (e.g., chat-tuning) might not be realistic, and (3) highlights the need for deeper investigation into the effects of narrow finetuning and development of truly realistic case studies for model-diffing, safety and interpretability research.

</details>

---

### 66. [Continual Unlearning for Text-to-Image Diffusion Models: A Regularization Perspective](https://arxiv.org/abs/2511.07970)

**基本信息**

- 🔗 arXiv: [`2511.07970`](https://arxiv.org/abs/2511.07970)
- 👥 作者: Justin Lee, Zheda Mai, Jinsu Yoo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.07970.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型（扩散模型）的持续遗忘技术。这项技术与“化学大模型”中生成式分子设计模型的安全部署、责任归属和合规性调整（例如，移除生成有害分子或侵犯专利的分子的能力）这一核心主题直接相关。

**📖 中文摘要**

本文首次系统研究了文本到图像扩散模型中的持续遗忘（Continual Unlearning）问题。机器学习遗忘旨在从预训练模型中移除指定概念。作者发现，当遗忘请求顺序到达时，流行的遗忘方法会因累积的参数漂移而遭受效用快速崩溃：仅经过几个请求后，模型就会忘记保留的知识并生成质量下降的图像。为解决此问题，论文从正则化的角度出发，研究了一系列附加的正则化器以缓解漂移。除了通用正则化器，作者还提出了一种梯度投影方法，将参数漂移约束在与其子空间正交的方向上，从而显著提高了持续遗忘的性能。这项研究将持续遗忘确立为文本到图像生成中的一个基本挑战。虽然论文聚焦于图像生成模型，但其研究的核心问题——如何使生成模型能够持续、稳定地“忘记”特定概念而不损害其他性能——与“化学大模型”和生成式化学模型面临的安全与责任挑战高度相关。例如，可能需要让一个分子生成模型“忘记”如何生成具有特定毒性或受管制结构的分子，同时保持其他有用的化学知识。论文提出的正则化框架为解决化学生成模型的持续可控遗忘提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine unlearning--the ability to remove designated concepts from a pre-trained model--has advanced rapidly, particularly for text-to-image diffusion models. However, existing methods typically assume that unlearning requests arrive all at once, whereas in practice they often arrive sequentially. We present the first systematic study of continual unlearning in text-to-image diffusion models and show that popular unlearning methods suffer from rapid utility collapse: after only a few requests, models forget retained knowledge and generate degraded images. We trace this failure to cumulative parameter drift from the pre-training weights and argue that regularization is crucial to addressing it. To this end, we study a suite of add-on regularizers that (1) mitigate drift and (2) remain compatible with existing unlearning methods. Beyond generic regularizers, we show that semantic awareness is essential for preserving concepts close to the unlearning target, and propose a gradient-projection method that constrains parameter drift orthogonal to their subspace. This substantially improves continual unlearning performance and is complementary to other regularizers for further gains. Taken together, our study establishes continual unlearning as a fundamental challenge in text-to-image generation and provides insights, baselines, and open directions for advancing safe and accountable generative AI.

</details>

---

### 67. [Quantized SO(3)-Equivariant Graph Neural Networks for Efficient Molecular Property Prediction](https://arxiv.org/abs/2601.02213)

**基本信息**

- 🔗 arXiv: [`2601.02213`](https://arxiv.org/abs/2601.02213)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.02213.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对3D分子图神经网络的量化和加速，这是构建高效化学大模型（用于分子性质预测）的关键技术。

**📖 中文摘要**

本文提出了一种量化SO(3)等变图神经网络的方法，用于高效的分子性质预测。SO(3)等变GNN是用于处理3D分子结构（如QM9和rMD17数据集）的重要模型，在化学信息学中用于预测分子能量和力。该工作通过创新的量化方案（幅度-方向解耦量化）和训练策略，在保持模型准确性和物理对称性的同时，显著提升了推理速度并减小了模型大小。这项工作直接为化学大模型（特别是用于分子表示的3D GNN）提供了高效的部署方案，属于核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deploying 3D graph neural networks (GNNs) that are equivariant to 3D rotations (the group SO(3)) on edge devices is challenging due to their high computational cost. This paper addresses the problem by compressing and accelerating an SO(3)-equivariant GNN using low-bit quantization techniques. Specifically, we introduce three innovations for quantized equivariant transformers: (1) a magnitude-direction decoupled quantization scheme that separately quantizes the norm and orientation of equivariant (vector) features, (2) a branch-separated quantization-aware training strategy that treats invariant and equivariant feature channels differently in an attention-based $SO(3)$-GNN, and (3) a robustness-enhancing attention normalization mechanism that stabilizes low-precision attention computations. Experiments on the QM9 and rMD17 molecular benchmarks demonstrate that our 8-bit models achieve accuracy on energy and force predictions comparable to full-precision baselines with markedly improved efficiency. We also conduct ablation studies to quantify the contribution of each component to maintain accuracy and equivariance under quantization, using the Local error of equivariance (LEE) metric. The proposed techniques enable the deployment of symmetry-aware GNNs in practical chemistry applications with 2.37--2.73x faster inference and 4x smaller model size, without sacrificing accuracy or physical symmetry.

</details>

---

### 68. [Entropy Sentinel: Continuous LLM Accuracy Monitoring from Decoding Entropy Traces in STEM](https://arxiv.org/abs/2601.09001)

**基本信息**

- 🔗 arXiv: [`2601.09001`](https://arxiv.org/abs/2601.09001)
- 👥 作者: Pedro Memoli Buffa, Luciano Del Corro
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.09001.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法是评估和监控大型语言模型在STEM（包括化学等科学领域）推理任务上的性能，这与评估和提升化学大模型的能力直接相关。

**📖 中文摘要**

本文提出了Entropy Sentinel方法，通过分析LLM解码过程中的熵迹来持续监控其在STEM领域的准确性。该方法计算最终层下一个token的概率（来自top-k logprobs）得到输出熵分布，并用统计量进行总结。一个轻量级分类器可以预测单个回答的正确性，进而聚合得到领域级别的准确率估计。该方法在超过20个STEM领域的基准上进行了评估。虽然论文主要关注LLM的监控，但其方法论（基于输出熵的分析）和评估领域（广泛的STEM推理）与构建和评估用于科学推理（包括化学信息学）的大模型高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deploying LLMs raises two coupled challenges: (1) monitoring--estimating where a model underperforms as traffic and domains drift--and (2) improvement--prioritizing data acquisition to close the largest performance gaps. We test whether an inference-time signal can estimate slice-level accuracy under domain shift. For each response, we compute an output-entropy profile from final-layer next-token probabilities (from top-$k$ logprobs) and summarize it with different statistics. A lightweight classifier predicts instance correctness, and averaging predicted probabilities yields a domain-level accuracy estimate. We evaluate on ten STEM reasoning benchmarks with exhaustive train/test compositions ($k\in\{1,2,3,4\}$; all $\binom{10}{k}$ combinations), on different classifier models and features across nine LLMs from six families (3B--20B). Estimates often track held-out benchmark accuracy, and several models show near-monotonic ordering of domains, providing evidence for output-entropy profiles being an accessible signal for scalable monitoring and for targeted data acquisition.

</details>

---

### 69. [WristMIR: Coarse-to-Fine Region-Aware Retrieval of Pediatric Wrist Radiographs with Radiology Report-Driven Learning](https://arxiv.org/abs/2602.07872)

**基本信息**

- 🔗 arXiv: [`2602.07872`](https://arxiv.org/abs/2602.07872)
- 👥 作者: Mert Sonmezer, Serge Vasylechko, Duygu Atasoy 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07872.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法涉及使用大型语言模型处理科学文本（放射学报告）以增强多模态（图像）数据的表示学习，这种方法论可以迁移到化学信息学中，例如用LLM处理化学文献来增强质谱或分子数据的表示。

**📖 中文摘要**

本文提出了WristMIR，一个用于儿科腕部X光片检索的区域感知框架。其核心创新在于利用放射学报告（通过MedGemma进行结构化挖掘）来生成全局和区域级别的描述，从而学习细粒度的、具有临床意义的图像表示，而无需任何手动图像级标注。该方法联合训练全局和局部对比编码器，并执行两阶段检索过程。虽然应用领域是医学影像，但其方法论——利用大型语言模型（MedGemma）从文本报告中提取结构化信息以增强多模态（图像-文本）表示学习——与化学信息学中利用文本描述（如论文、实验记录）来增强分子表示或质谱数据解释的思路高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieving wrist radiographs with analogous fracture patterns is challenging because clinically important cues are subtle, highly localized and often obscured by overlapping anatomy or variable imaging views. Progress is further limited by the scarcity of large, well-annotated datasets for case-based medical image retrieval. We introduce WristMIR, a region-aware pediatric wrist radiograph retrieval framework that leverages dense radiology reports and bone-specific localization to learn fine-grained, clinically meaningful image representations without any manual image-level annotations. Using MedGemma-based structured report mining to generate both global and region-level captions, together with pre-processed wrist images and bone-specific crops of the distal radius, distal ulna, and ulnar styloid, WristMIR jointly trains global and local contrastive encoders and performs a two-stage retrieval process: (1) coarse global matching to identify candidate exams, followed by (2) region-conditioned reranking aligned to a predefined anatomical bone region. WristMIR improves retrieval performance over strong vision-language baselines, raising image-to-text Recall@5 from 0.82% to 9.35%. Its embeddings also yield stronger fracture classification (AUROC 0.949, AUPRC 0.953). In region-aware evaluation, the two-stage design markedly improves retrieval-based fracture diagnosis, increasing mean $F_1$ from 0.568 to 0.753, and radiologists rate its retrieved cases as more clinically relevant, with mean scores rising from 3.36 to 4.35. These findings highlight the potential of anatomically guided retrieval to enhance diagnostic reasoning and support clinical decision-making in pediatric musculoskeletal imaging. The source code is publicly available at this https URL .

</details>

---

### 70. [The Garbage Dataset (GD): A Multi-Class Image Benchmark for Automated Waste Segregation](https://arxiv.org/abs/2602.10500)

**基本信息**

- 🔗 arXiv: [`2602.10500`](https://arxiv.org/abs/2602.10500)
- 👥 作者: Suman Kunwar
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10500.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个公开的、多类别的图像数据集（GD）以及详细的基准测试结果，这可以作为构建和评估特定领域（环境科学/材料分类）视觉模型的数据资源和基准。

**📖 中文摘要**

本研究介绍了垃圾数据集（GD），一个用于通过机器学习和计算机视觉进行自动废物分类的公开图像数据集。它涵盖了10类常见生活垃圾。论文对数据集进行了基准测试，使用了包括EfficientNetV2、MobileNet、ResNet在内的最先进的深度学习模型，并评估了性能指标和运行碳排放。虽然应用领域是废物分类，但该工作创建了一个标注好的、多类别的图像数据集，并提供了完整的基准测试流程和结果。从更广义的“数据资源”角度看，它为构建和评估视觉模型（可视为一种特定领域的“视觉大模型”）提供了标准化的数据集和评估基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study introduces the Garbage Dataset (GD), a publicly available image dataset designed to advance automated waste segregation through machine learning and computer vision. It is a diverse dataset that covers 10 categories of common household waste: metal, glass, biological, paper, battery, trash, cardboard, shoes, clothes, and plastic. The dataset comprises 12,259 labeled images collected through multiple methods, including the DWaste mobile app and curated web sources. The methods included rigorous validation through checksums and outlier detection, analysis of class imbalance and visual separability through PCA/t-SNE, and assessment of background complexity using entropy and saliency measures. The dataset was benchmarked using state-of-the-art deep learning models (EfficientNetV2M, EfficientNetV2S, MobileNet, ResNet50, ResNet101) evaluated on performance metrics and operational carbon emissions. The results of the experiment indicate that EfficientNetV2S achieved the highest performance with a accuracy of 95.13% and an F1-score of 0.95 with moderate carbon cost. Analysis revealed inherent dataset characteristics including class imbalance, a skew toward high-outlier classes (plastic, cardboard, paper), and brightness variations that require consideration. The main conclusion is that GD provides a valuable real-world benchmark for waste classification research while highlighting important challenges such as class imbalance, background complexity, and environmental trade-offs in model selection that must be addressed for practical deployment. The dataset is publicly released to support further research in environmental sustainability applications.

</details>

---

### 71. [MoToRec: Sparse-Regularized Multimodal Tokenization for Cold-Start Recommendation](https://arxiv.org/abs/2602.11062)

**基本信息**

- 🔗 arXiv: [`2602.11062`](https://arxiv.org/abs/2602.11062)
- 👥 作者: Jialin Liu, Zhaorui Zhang, Ray C.C. Cheung
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.11062.pdf)

**💡 相关性分析**

满足标准1：论文的核心技术（多模态数据的离散语义标记化）为解决化学信息学中的关键问题（如分子、谱图的符号化表示）提供了直接的方法论参考，是构建化学多模态大模型的基础。

**📖 中文摘要**

本文提出了MoToRec，一个通过离散语义标记化解决推荐系统中物品冷启动问题的框架。其核心是一个稀疏正则化的残差量化变分自编码器（RQ-VAE），用于生成由离散、可解释的标记组成的组合语义代码，从而促进解耦表示。该框架将多模态（如图像、文本）内容转化为离散标记。虽然应用于推荐系统，但其核心技术创新——**将多模态数据离散化为语义标记**——与化学信息学中一个核心挑战高度相关：如何将分子结构、质谱图等多模态化学数据有效地、可解释地表示为离散的、机器可处理的符号（标记），以便用于下游的大模型训练或推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph neural networks (GNNs) have revolutionized recommender systems by effectively modeling complex user-item interactions, yet data sparsity and the item cold-start problem significantly impair performance, particularly for new items with limited or no interaction history. While multimodal content offers a promising solution, existing methods result in suboptimal representations for new items due to noise and entanglement in sparse data. To address this, we transform multimodal recommendation into discrete semantic tokenization. We present Sparse-Regularized Multimodal Tokenization for Cold-Start Recommendation (MoToRec), a framework centered on a sparsely-regularized Residual Quantized Variational Autoencoder (RQ-VAE) that generates a compositional semantic code of discrete, interpretable tokens, promoting disentangled representations. MoToRec's architecture is enhanced by three synergistic components: (1) a sparsely-regularized RQ-VAE that promotes disentangled representations, (2) a novel adaptive rarity amplification that promotes prioritized learning for cold-start items, and (3) a hierarchical multi-source graph encoder for robust signal fusion with collaborative signals. Extensive experiments on three large-scale datasets demonstrate MoToRec's superiority over state-of-the-art methods in both overall and cold-start scenarios. Our work validates that discrete tokenization provides an effective and scalable alternative for mitigating the long-standing cold-start challenge.

</details>

---

### 72. [Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage](https://arxiv.org/abs/2602.12274)

**基本信息**

- 🔗 arXiv: [`2602.12274`](https://arxiv.org/abs/2602.12274)
- 👥 作者: Xin Ju, Jiachen Yao, Anima Anandkumar 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.12274.pdf)

**💡 相关性分析**

满足标准1：论文提出的结合扩散模型和物理引导神经算子的框架，为解决化学信息学中的核心逆问题（如从质谱数据推理分子结构）提供了强大的方法论范例。

**📖 中文摘要**

本文提出了Fun-DDPS，一个用于碳捕集与封存（CCS）中地下流正演和反演建模的生成框架。它结合了函数空间扩散模型和可微神经算子代理。该方法学习地质参数（地质模型）的先验分布，并利用局部神经算子（LNO）代理为动力学场提供物理一致的指导以进行跨场条件处理。这种解耦允许扩散先验在参数空间中稳健地恢复缺失信息，而代理则为数据同化提供高效的基于梯度的指导。论文在合成CCS建模数据集上进行了演示。该工作展示了**扩散模型与物理引导的神经算子相结合**解决复杂科学计算问题（反演、生成）的能力。这种方法论可以迁移到化学信息学中，例如，用于从稀疏的质谱数据反推分子结构（一个病态反问题），或者生成符合物理/化学规律的分子构型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate characterization of subsurface flow is critical for Carbon Capture and Storage (CCS) but remains challenged by the ill-posed nature of inverse problems with sparse observations. We present Function-space Decoupled Diffusion Posterior Sampling (Fun-DDPS), a generative framework that combines function-space diffusion models with differentiable neural operator surrogates for both forward and inverse modeling. Our approach learns a prior distribution over geological parameters (geomodel) using a single-channel diffusion model, then leverages a Local Neural Operator (LNO) surrogate to provide physics-consistent guidance for cross-field conditioning on the dynamics field. This decoupling allows the diffusion prior to robustly recover missing information in parameter space, while the surrogate provides efficient gradient-based guidance for data assimilation. We demonstrate Fun-DDPS on synthetic CCS modeling datasets, achieving two key results: (1) For forward modeling with only 25% observations, Fun-DDPS achieves 7.7% relative error compared to 86.9% for standard surrogates (an 11x improvement), proving its capability to handle extreme data sparsity where deterministic methods fail. (2) We provide the first rigorous validation of diffusion-based inverse solvers against asymptotically exact Rejection Sampling (RS) posteriors. Both Fun-DDPS and the joint-state baseline (Fun-DPS) achieve Jensen-Shannon divergence less than 0.06 against the ground truth. Crucially, Fun-DDPS produces physically consistent realizations free from the high-frequency artifacts observed in joint-state baselines, achieving this with 4x improved sample efficiency compared to rejection sampling.

</details>

---

### 73. [MedXIAOHE: A Comprehensive Recipe for Building Medical MLLMs](https://arxiv.org/abs/2602.12705)

**基本信息**

- 🔗 arXiv: [`2602.12705`](https://arxiv.org/abs/2602.12705)
- 👥 作者: Baorong Shi, Bo Cui, Boyuan Jiang 等20人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.12705.pdf)

**💡 相关性分析**

满足标准1和3：论文详细介绍了构建一个专业领域（医学）多模态大模型的完整方案，包括知识整合、推理能力提升和可靠性设计，这对构建“化学大模型”具有直接的综述和蓝图价值（标准3）。同时，其核心研究内容就是大模型构建（标准1）。

**📖 中文摘要**

本文介绍了MedXIAOHE，一个旨在推进现实世界临床应用中通用医学理解和推理的医学视觉语言基础模型。它通过实体感知的持续预训练框架来组织异构医学语料库，以拓宽知识覆盖范围并减少长尾差距（例如罕见疾病）。为了达到医学专家级的推理和交互，MedXIAOHE通过强化学习和工具增强的智能体训练融入了多样化的医学推理模式，实现了具有可验证决策轨迹的多步骤诊断推理。这是一个构建**领域大模型（医学MLLM）** 的全面实践报告。其设计选择、扩展见解和评估框架（特别是针对专业领域知识的整合、多步推理和可靠性提升）为在化学领域构建类似的“化学大模型”或“质谱分析专家模型”提供了宝贵的路线图参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MedXIAOHE, a medical vision-language foundation model designed to advance general-purpose medical understanding and reasoning in real-world clinical applications. MedXIAOHE achieves state-of-the-art performance across diverse medical benchmarks and surpasses leading closed-source multimodal systems on multiple capabilities. To achieve this, we propose an entity-aware continual pretraining framework that organizes heterogeneous medical corpora to broaden knowledge coverage and reduce long-tail gaps (e.g., rare diseases). For medical expert-level reasoning and interaction, MedXIAOHE incorporates diverse medical reasoning patterns via reinforcement learning and tool-augmented agentic training, enabling multi-step diagnostic reasoning with verifiable decision traces. To improve reliability in real-world use, MedXIAOHE integrates user-preference rubrics, evidence-grounded reasoning, and low-hallucination long-form report generation, with improved adherence to medical instructions. We release this report to document our practical design choices, scaling insights, and evaluation framework, hoping to inspire further research.

</details>

---

### 74. [Rethinking the Role of LLMs in Time Series Forecasting](https://arxiv.org/abs/2602.14744)

**基本信息**

- 🔗 arXiv: [`2602.14744`](https://arxiv.org/abs/2602.14744)
- 👥 作者: Xin Qiu, Junlong Tong, Yirong Sun 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.14744.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是评估LLM处理复杂序列数据的能力并得出积极结论，这直接支持了在化学信息学（分子序列、谱图序列）中应用LLM的可行性（标准1）。同时，它也是一篇对LLM在非传统领域应用的系统性评估和展望（标准3）。

**📖 中文摘要**

本文对基于大语言模型的时间序列预测（LLM4TSF）进行了大规模研究，涵盖了80亿个观测值、17个预测场景、多个时间跨度和对齐策略。研究结果表明，LLM4TS确实提高了预测性能，特别是在跨领域泛化方面有巨大收益。论文详细分析了LLM的预训练知识和模型架构的贡献，并推翻了先前关于LLM对时间序列预测无用的负面评估。这项研究系统地**重新评估并证实了LLM在复杂序列建模任务中的价值**。虽然应用领域是时间序列，但其核心结论——LLM的预训练知识和架构能够提升对复杂、非文本序列数据的建模和泛化能力——强烈支持在化学信息学中探索LLM用于分子序列（SMILES）、光谱序列（质谱峰）或时间序列数据的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been introduced to time series forecasting (TSF) to incorporate contextual knowledge beyond numerical signals. However, existing studies question whether LLMs provide genuine benefits, often reporting comparable performance without LLMs. We show that such conclusions stem from limited evaluation settings and do not hold at scale. We conduct a large-scale study of LLM-based TSF (LLM4TSF) across 8 billion observations, 17 forecasting scenarios, 4 horizons, multiple alignment strategies, and both in-domain and out-of-domain settings. Our results demonstrate that \emph{LLM4TS indeed improves forecasting performance}, with especially large gains in cross-domain generalization. Pre-alignment outperforming post-alignment in over 90\% of tasks. Both pretrained knowledge and model architecture of LLMs contribute and play complementary roles: pretraining is critical under distribution shifts, while architecture excels at modeling complex temporal dynamics. Moreover, under large-scale mixed distributions, a fully intact LLM becomes indispensable, as confirmed by token-level routing analysis and prompt-based improvements. Overall, Our findings overturn prior negative assessments, establish clear conditions under which LLMs are not only useful, and provide practical guidance for effective model design. We release our code at this https URL .

</details>

---

### 75. [UniTAF: A Modular Framework for Joint Text-to-Speech and Audio-to-Face Modeling](https://arxiv.org/abs/2602.15651)

**基本信息**

- 🔗 arXiv: [`2602.15651`](https://arxiv.org/abs/2602.15651)
- 👥 作者: Qiangong Zhou, Nagasaka Tomohiro
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.15651.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是多模态生成模型的联合设计与特征共享，这种方法论可以迁移到化学信息学中，用于构建统一处理化学文本、结构和谱图的多模态大模型。

**📖 中文摘要**

本文提出了UniTAF，一个用于联合文本到语音和音频到人脸建模的模块化框架。其核心考虑是将两个独立的模型（TTS和A2F）合并为一个统一模型，以实现内部特征转移，从而提高从文本生成的音频和人脸表情之间的一致性。论文从系统设计的角度验证了重用TTS中间表示进行语音和面部表情联合建模的可行性。这项工作展示了**多模态生成模型的联合设计与内部特征共享**的工程实践。这种统一多模态建模的思路可以启发化学信息学中类似的研究，例如构建一个统一模型，同时处理分子描述文本生成、分子结构生成和预测质谱图，并共享中间的化学表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work considers merging two independent models, TTS and A2F, into a unified model to enable internal feature transfer, thereby improving the consistency between audio and facial expressions generated from text. We also discuss the extension of the emotion control mechanism from TTS to the joint model. This work does not aim to showcase generation quality; instead, from a system design perspective, it validates the feasibility of reusing intermediate representations from TTS for joint modeling of speech and facial expressions, and provides engineering practice references for subsequent speech expression co-design. The project code has been open source at: this https URL

</details>

---

### 76. [Classroom Final Exam: An Instructor-Tested Reasoning Benchmark](https://arxiv.org/abs/2602.19517)

**基本信息**

- 🔗 arXiv: [`2602.19517`](https://arxiv.org/abs/2602.19517)
- 👥 作者: Chongyang Gao, Diji Yang, Shuyan Zhou 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.19517.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专注于STEM推理的多模态基准（CFE-Bench），并提供了详细的评估和诊断方法，这可以作为评估化学大模型复杂推理能力的数据资源和评估框架。

**📖 中文摘要**

本文介绍了CFE-Bench（课堂期末考试），一个用于评估大语言模型在超过20个STEM领域推理能力的多模态基准。该基准来源于大学真实使用的作业和考试题目，并配有课程教师提供的参考答案。论文对前沿模型进行了诊断分析，将教师参考答案分解为结构化的推理流程，发现模型在可靠地推导和维护多步解决方案中的中间状态方面存在困难。这是一个**专注于STEM领域复杂推理评估的基准**。其涵盖的领域可能包括化学，并且其构建高质量、具有结构化推理过程标注的基准的方法，对于评估化学大模型（特别是需要多步推理的化学问题解决能力）具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce CFE-Bench (Classroom Final Exam), a multimodal benchmark for evaluating the reasoning capabilities of large language models across more than 20 STEM domains. CFE-Bench is curated from repeatedly used, authentic university homework and exam problems, paired with reference solutions provided by course instructors. CFE-Bench remains challenging for frontier models: the newly released Gemini-3.1-pro-preview achieves 59.69% overall accuracy, while the second-best model, Gemini-3-flash-preview, reaches 55.46%, leaving substantial room for improvement. Beyond aggregate scores, we conduct a diagnostic analysis by decomposing instructor reference solutions into structured reasoning flows. We find that while frontier models often answer intermediate sub-questions correctly, they struggle to reliably derive and maintain correct intermediate states throughout multi-step solutions. We further observe that model-generated solutions typically contain more reasoning steps than instructor solutions, indicating lower step efficiency and a higher risk of error accumulation. Data and code are available at this https URL .

</details>

---

### 77. [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://arxiv.org/abs/2602.21628)

**基本信息**

- 🔗 arXiv: [`2602.21628`](https://arxiv.org/abs/2602.21628)
- 👥 作者: Yukun Chen, Jiaming Li, Longze Chen 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21628.pdf)

**💡 相关性分析**

满足标准1：论文提出的通过规则和课程学习提升MLLM推理能力的框架，其方法论可以迁移并应用于训练和提升化学领域大模型或质谱结构推理模型的逻辑和分步推理能力。

**📖 中文摘要**

本文提出了分层规则课程学习（RuCL），一个用于增强多模态大语言模型（MLLM）推理的新框架。它通过生成通用规则并根据模型能力对其进行分层，动态调整训练过程中的规则权重，从而引导模型从掌握基础感知到处理高级逻辑推理。该框架在多个视觉推理基准上进行了广泛实验。RuCL的核心是**通过课程学习和细粒度规则（rubric）来提升MLLM的推理能力**。这种方法论可以直接应用于提升化学大模型或质谱分析模型的推理能力，例如，设计化学领域特定的规则（如官能团识别、裂解规则、光谱解读步骤）来指导模型进行更可靠、更结构化的化学推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a prevailing paradigm for enhancing reasoning in Multimodal Large Language Models (MLLMs). However, relying solely on outcome supervision risks reward hacking, where models learn spurious reasoning patterns to satisfy final answer checks. While recent rubric-based approaches offer fine-grained supervision signals, they suffer from high computational costs of instance-level generation and inefficient training dynamics caused by treating all rubrics as equally learnable. In this paper, we propose Stratified Rubric-based Curriculum Learning (RuCL), a novel framework that reformulates curriculum learning by shifting the focus from data selection to reward design. RuCL generates generalized rubrics for broad applicability and stratifies them based on the model's competence. By dynamically adjusting rubric weights during training, RuCL guides the model from mastering foundational perception to tackling advanced logical reasoning. Extensive experiments on various visual reasoning benchmarks show that RuCL yields a remarkable +7.83% average improvement over the Qwen2.5-VL-7B model, achieving a state-of-the-art accuracy of 60.06%.

</details>

---

### 78. [Scalable Multilingual Multimodal Machine Translation with Speech-Text Fusion](https://arxiv.org/abs/2602.21646)

**基本信息**

- 🔗 arXiv: [`2602.21646`](https://arxiv.org/abs/2602.21646)
- 👥 作者: Yexing Du, Youcheng Pan, Zekun Wang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21646.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究是利用与文本对齐的连续模态（语音）增强MLLM，这为化学信息学中利用连续谱图模态（如质谱）增强分子文本或结构模型提供了直接的方法论类比和灵感。

**📖 中文摘要**

本文提出了一个语音引导的机器翻译（SMT）框架，将语音和文本作为融合输入集成到MLLM中以提高翻译质量。为了减少对低资源数据的依赖，引入了自进化机制，包括一个用于生成合成语音的文本到语音模型和一个能够对合成语音样本进行分类并利用正样本迭代优化自身的MLLM。该工作在Multi30K多模态机器翻译基准和通用机器翻译数据集FLORES-200上取得了最先进的结果。这项研究展示了**利用语音这种天然与文本对齐的模态来增强MLLM性能**的有效路径。虽然应用于翻译，但其核心思想——利用与文本对齐的、易于获取的连续信号模态（语音）来增强模型——可以类比到化学信息学中：利用与分子结构紧密相关的、连续的谱图数据（如质谱、红外光谱）作为多模态信号，来增强分子表示学习或分子属性预测模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal Large Language Models (MLLMs) have achieved notable success in enhancing translation performance by integrating multimodal information. However, existing research primarily focuses on image-guided methods, whose applicability is constrained by the scarcity of multilingual image-text pairs. The speech modality overcomes this limitation due to its natural alignment with text and the abundance of existing speech datasets, which enable scalable language coverage. In this paper, we propose a Speech-guided Machine Translation (SMT) framework that integrates speech and text as fused inputs into an MLLM to improve translation quality. To mitigate reliance on low-resource data, we introduce a Self-Evolution Mechanism. The core components of this framework include a text-to-speech model, responsible for generating synthetic speech, and an MLLM capable of classifying synthetic speech samples and iteratively optimizing itself using positive samples. Experimental results demonstrate that our framework surpasses all existing methods on the Multi30K multimodal machine translation benchmark, achieving new state-of-the-art results. Furthermore, on general machine translation datasets, particularly the FLORES-200, it achieves average state-of-the-art performance in 108 translation directions. Ablation studies on CoVoST-2 confirms that differences between synthetic and authentic speech have negligible impact on translation quality. The code and models are released at this https URL .

</details>

---

### 79. [DeepXiv-SDK: An Agentic Data Interface for Scientific Literature](https://arxiv.org/abs/2603.00084)

**基本信息**

- 🔗 arXiv: [`2603.00084`](https://arxiv.org/abs/2603.00084)
- 👥 作者: Hongjin Qian, Ziyi Xia, Ze Liu 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00084.pdf)

**💡 相关性分析**

满足标准2：提供了一个专门用于科学文献（包括化学领域预印本如chemRxiv）的结构化数据接口和工具集，可作为化学大模型和质谱结构推理研究的重要数据资源。

**📖 中文摘要**

本文介绍了DeepXiv-SDK，这是一个为科学文献设计的智能体数据接口。它旨在解决LLM智能体在科学研究中访问和处理非结构化文献数据（如PDF和HTML）时面临的效率低下和成本高昂的问题。该框架包含数据层、服务层和应用层，能够将非结构化数据转换为规范化的JSON格式，并提供工具支持CLI、MCP和Python SDK等多种使用方式。DeepXiv-SDK目前支持完整的ArXiv语料库，并计划扩展到PubMed Central、bioRxiv、medRxiv和chemRxiv等其他开放获取语料库。这项工作为构建高效的科研文献访问工具提供了框架，有助于加速化学信息学等领域的研究进程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-agents are increasingly used to accelerate the progress of scientific research. Yet a persistent bottleneck is data access: agents not only lack readily available tools for retrieval, but also have to work with unstrcutured, human-centric data on the Internet, such as HTML web-pages and PDF files, leading to excessive token consumption, limit working efficiency, and brittle evidence look-up. This gap motivates the development of \textit{an agentic data interface}, which is designed to enable agents to access and utilize scientific literature in a more effective, efficient, and cost-aware manner. In this paper, we introduce DeepXiv-SDK, which offers a three-layer agentic data interface for scientific literature. 1) Data Layer, which transforms unstructured, human-centric data into normalized and structured representations in JSON format, improving data usability and enabling progressive accessibility of the data. 2) Service Layer, which presents readily available tools for data access and ad-hoc retrieval. It also enables a rich form of agent usage, including CLI, MCP, and Python SDK. 3) Application Layer, which creates a built-in agent, packaging basic tools from the service layer to support complex data access demands. DeepXiv-SDK currently supports the complete ArXiv corpus, and is synchronized daily to incorporate new releases. It is designed to extend to all common open-access corpora, such as PubMed Central, bioRxiv, medRxiv, and chemRxiv. We release RESTful APIs, an open-source Python SDK, and a web demo showcasing deep search and deep research workflows. DeepXiv-SDK is free to use with registration.

</details>

---

### 80. [CoPeP: Benchmarking Continual Pretraining for Protein Language Models](https://arxiv.org/abs/2603.00253)

**基本信息**

- 🔗 arXiv: [`2603.00253`](https://arxiv.org/abs/2603.00253)
- 👥 作者: Darshan Patil, Pranshu Malviya, Mathieu Reymond 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00253.pdf)

**💡 相关性分析**

满足标准2：提出了一个针对蛋白质语言模型持续学习的基准和评估框架，其处理动态、大规模生物分子数据的方法论与化学信息学中处理不断增长的化学和质谱数据的需求高度相关，可作为相关工具和资源的参考。

**📖 中文摘要**

本文介绍了CoPeP基准，这是一个用于评估蛋白质语言模型持续预训练性能的新基准。随着生物学数据库（如UniProt）的不断更新，持续学习对于保持模型时效性和利用时间元信息至关重要。CoPeP基准基于跨越十年的蛋白质序列数据集构建，并定义了31个蛋白质理解任务的评估指标。作者评估了包括重放、遗忘和基于可塑性的方法在内的多种持续学习策略，发现结合时间元信息可以将困惑度提升高达7%。这项工作展示了在真实世界生物数据上大规模应用持续学习方法的潜力，为化学信息学中处理动态演化的化学和生物分子数据（如质谱数据库）提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (pLMs) have recently gained significant attention for their ability to uncover relationships between sequence, structure, and function from evolutionary statistics, thereby accelerating therapeutic drug discovery. These models learn from large protein databases that are continuously updated by the biology community and whose dynamic nature motivates the application of continual learning, not only to keep up with the ever-growing data, but also as an opportunity to take advantage of the temporal meta-information that is created during this process. As a result, we introduce the Continual Pretraining of Protein Language Models (CoPeP) benchmark, a novel benchmark for evaluating continual learning approaches on pLMs. Specifically, we curate a sequence of protein datasets derived from the UniProt Knowledgebase spanning a decade and define metrics to assess pLM performance across 31 protein understanding tasks. We evaluate several methods from the continual learning literature, including replay, unlearning, and plasticity-based methods, some of which have never been applied to models and data of this scale. Our findings reveal that incorporating temporal meta-information improves perplexity by up to 7% even when compared to training on data from all tasks jointly. Moreover, even at scale, several continual learning methods outperform naive continual pretraining. The CoPeP benchmark offers an exciting opportunity to study these methods at scale in an impactful real-world application.

</details>

---

### 81. [BioChemInsight: An Online Platform for Automated Extraction of Chemical Structures and Activity Data from Patents](https://arxiv.org/abs/2504.10525)

**基本信息**

- 🔗 arXiv: [`2504.10525`](https://arxiv.org/abs/2504.10525)
- 👥 作者: Zhe Wang, Fangtian Fu, Wei Zhang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.10525.pdf)

**💡 相关性分析**

满足标准2：提供了一个专门从专利中提取化学结构和生物活性数据的自动化工具和流程，为化学大模型和质谱结构推理研究创建了高质量、互补的数据集和资源。

**📖 中文摘要**

本文介绍了BioChemInsight，一个用于从专利中自动提取化学结构及其生物活性数据的开源平台。该平台集成了DECIMER Segmentation、MolNexTR（用于化学结构识别）、GLM-4.5V（用于化合物标识符关联）以及PaddleOCR与GLM-4（用于生物活性数据提取和单位标准化）。在涵盖15个治疗靶点的181项专利上进行评估，该系统在化学结构识别、生物活性数据提取和化合物标识符关联三个关键任务上的平均提取准确率超过90%。分析表明，专利覆盖的化学空间与公共数据库ChEMBL有很强的互补性。该工具能将数据预处理时间从数周缩短到数小时，为定量构效关系建模和靶向筛选提供了丰富的数据基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The automated extraction of chemical structures and their corresponding bioactivity data is essential for accelerating drug discovery and enabling data-driven research. Current optical chemical structure recognition tools lack the capability to autonomously link molecular structures with their bioactivity profiles, posing a significant bottleneck in structure-activity relationship analysis. To address this, we present BioChemInsight, an open-source pipeline that integrates DECIMER Segmentation with MolNexTR for chemical structure recognition, GLM-4.5V for compound identifier association, and PaddleOCR combined with GLM-4.6 for bioactivity extraction and unit normalization. We evaluated BioChemInsight on 181 patents covering 15 therapeutic targets. The system achieved an average extraction accuracy of above 90% across three key tasks: chemical structure recognition, bioactivity data extraction, and compound identifier association. Our analysis indicates that the chemical space covered by patents is largely complementary to that contained in established public database ChEMBL. Consequently, by enabling systematic patent mining, BioChemInsight provides access to chemical information underrepresented in ChEMBL. This capability expands the landscape of explorable compound-target interactions, enriches the data foundation for quantitative structure-activity relationship modeling and targeted screening, and reduces data preprocessing time from weeks to hours. BioChemInsight is available at this https URL .

</details>

---

### 82. [Sustainable Materials Discovery in the Era of Artificial Intelligence](https://arxiv.org/abs/2601.21527)

**基本信息**

- 🔗 arXiv: [`2601.21527`](https://arxiv.org/abs/2601.21527)
- 👥 作者: Sajid Mannan, Rupert J. Myers, Rohit Batra 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.21527.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个整合AI（机器学习）与可持续性评估的材料发现框架（ML-LCA），这直接涉及利用“化学大模型”进行材料设计与优化，是化学信息学的重要应用方向。

**📖 中文摘要**

本文探讨了在人工智能时代实现可持续材料发现的框架。作者指出，当前AI驱动的材料发现工作流通常优先优化性能，而将可持续性评估推迟到合成之后，这可能导致资源浪费。为了解决原子尺度设计与全生命周期评估之间的脱节，作者提出了ML-LCA框架，旨在将上游的机器学习辅助材料发现与下游的生命周期评估整合到一个统一的环境中。该框架包含五个组件：信息提取、关联属性与可持续性指标的数据库、连接原子性质与生命周期影响的多尺度模型、制造路径的集成预测与不确定性量化，以及支持性能与可持续性同步优化的不确定性感知优化。案例研究涵盖了玻璃、水泥、半导体光刻胶和聚合物，展示了该框架的必要性和可行性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Artificial intelligence (AI) has transformed materials discovery, enabling rapid exploration of chemical space through generative models and surrogate screening. Yet current AI workflows optimize performance first, deferring sustainability to post synthesis assessment. This creates inefficiency by the time environmental burdens are quantified, resources have been invested in potentially unsustainable solutions. The disconnect between atomic scale design and lifecycle assessment (LCA) reflects fundamental challenges, data scarcity across heterogeneous sources, scale gaps from atoms to industrial systems, uncertainty in synthesis pathways, and the absence of frameworks that co-optimize performance with environmental impact. We propose to integrate upstream machine learning (ML) assisted materials discovery with downstream lifecycle assessment into a uniform ML-LCA environment. The framework ML-LCA integrates five components, information extraction for building materials-environment knowledge bases, harmonized databases linking properties to sustainability metrics, multi-scale models bridging atomic properties to lifecycle impacts, ensemble prediction of manufacturing pathways with uncertainty quantification, and uncertainty-aware optimization enabling simultaneous performance-sustainability navigation. Case studies spanning glass, cement, semiconductor photoresists, and polymers demonstrate both necessity and feasibility while identifying material-specific integration challenges. Realizing ML-LCA demands coordinated advances in data infrastructure, ex-ante assessment methodologies, multi-objective optimization, and regulatory alignment enabling the discovery of materials that are sustainable by design rather than by chance.

</details>

---

### 83. [ReDON: Recurrent Diffractive Optical Neural Processor with Reconfigurable Self-Modulated Nonlinearity](https://arxiv.org/abs/2602.23616)

**基本信息**

- 🔗 arXiv: [`2602.23616`](https://arxiv.org/abs/2602.23616)
- 👥 作者: Ziang Yin, Qi Jing, Raktim Sarma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23616.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的、具有可重构非线性的光学神经网络处理器（ReDON）。虽然其直接应用是图像处理，但其“循环”和“自调制”的架构思想，以及旨在提升模型表达能力和适应性的目标，与构建更强大、更高效的“化学大模型”在底层计算架构和创新思路上有潜在的相关性。

**📖 中文摘要**

本文介绍了循环衍射光学神经处理器（ReDON），一种具有可重构自调制非线性的新型光学神经网络架构。衍射光学神经网络因其直接在光域处理信息而具有极高的能效和并行性，但其计算表达能力受限于静态的、被动的衍射相位掩模。ReDON通过原位电光自调制机制，实现了动态的、输入依赖的光学传输，从而提供了高效且可重构的光学非线性计算方法。其自调制机制受大语言模型中门控线性单元的启发，通过轻量级参数函数调制传播光场的相位或强度。在图像识别和分割基准测试中，ReDON在模型复杂度相当且额外功耗可忽略的情况下，比采用光学或数字非线性的先前DONN方法将测试准确率和平均交并比提升了高达20%。这项工作为可重构非线性光学计算建立了新范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffractive optical neural networks (DONNs) have demonstrated unparalleled energy efficiency and parallelism by processing information directly in the optical domain. However, their computational expressivity is constrained by static, passive diffractive phase masks that lack efficient nonlinear responses and reprogrammability. To address these limitations, we introduce the Recurrent Diffractive Optical Neural Processor (ReDON), a novel architecture featuring reconfigurable, recurrent self-modulated nonlinearity. This mechanism enables dynamic, input-dependent optical transmission through in-situ electro-optic self-modulation, providing a highly efficient and reprogrammable approach to optical computation. Inspired by the gated linear unit (GLU) used in large language models, ReDON senses a fraction of the propagating optical field and modulates its phase or intensity via a lightweight parametric function, enabling effective nonlinearity with minimal inference overhead. As a non-von Neumann architecture in which the primary weighting elements (metasurfaces) remain fixed, ReDON substantially extends the nonlinear representational capacity and task adaptability of conventional DONNs through recurrent optical hardware reuse and dynamically tunable nonlinearity. We systematically investigate various self-modulation configurations to characterize the trade-offs between hardware efficiency and computational expressivity. On image recognition and segmentation benchmarks, ReDON improves test accuracy and mean intersection-over-union (mIoU) by up to 20% compared with prior DONNs employing either optical or digital nonlinearities at comparable model complexity and negligible additional power consumption. This work establishes a new paradigm for reconfigurable nonlinear optical computing, uniting recurrence and self-modulation within non-von Neumann analog processors.

</details>

---

## 📊 数据统计
- 累计运行天数：10
- 累计论文数量：691

## 📝 历史记录

> 暂无历史数据

