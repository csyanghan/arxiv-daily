# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-17 01:17:11

## 📅 2026-03-17 (今日最新)

**相关论文数：55**

### 1. [Generalist Large Language Models for Molecular Property Prediction: Distilling Knowledge from Specialist Models](https://arxiv.org/abs/2603.12344)

**基本信息**

- 🔗 arXiv: [`2603.12344`](https://arxiv.org/abs/2603.12344)
- 👥 作者: Khiem Le, Sreejata Dey, Marcos Martínez Galindo 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12344.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型（LLMs）作为通用模型进行分子性质预测，并通过知识蒸馏方法提升其性能，这直接与‘化学大模型’这一重点关注主题相关。

**📖 中文摘要**

本文提出了一种名为TreeKD的新知识蒸馏方法，旨在提升大语言模型在分子性质预测任务中的性能。该方法的核心思想是将基于功能基团特征训练的专家决策树（如随机森林）所学习到的预测规则，转化为自然语言描述，从而为大语言模型提供规则增强的上下文学习能力。这使得大语言模型能够利用仅从SMILES字符串中难以提取的结构化洞察。论文在TDC基准的22个ADMET性质上进行了实验，结果表明TreeKD显著缩小了通用大语言模型与最先进的专家模型之间的性能差距，推动了面向药物发现的通用分子性质预测模型的发展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular Property Prediction (MPP) is a central task in drug discovery. While Large Language Models (LLMs) show promise as generalist models for MPP, their current performance remains below the threshold for practical adoption. We propose TreeKD, a novel knowledge distillation method that transfers complementary knowledge from tree-based specialist models into LLMs. Our approach trains specialist decision trees on functional group features, then verbalizes their learned predictive rules as natural language to enable rule-augmented context learning. This enables LLMs to leverage structural insights that are difficult to extract from SMILES strings alone. We further introduce rule-consistency, a test-time scaling technique inspired by bagging that ensembles predictions across diverse rules from a Random Forest. Experiments on 22 ADMET properties from the TDC benchmark demonstrate that TreeKD substantially improves LLM performance, narrowing the gap with SOTA specialist models and advancing toward practical generalist models for molecular property prediction.

</details>

---

### 2. [Budget-Sensitive Discovery Scoring: A Formally Verified Framework for Evaluating AI-Guided Scientific Selection](https://arxiv.org/abs/2603.12349)

**基本信息**

- 🔗 arXiv: [`2603.12349`](https://arxiv.org/abs/2603.12349)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12349.pdf)

**💡 相关性分析**

满足标准1：论文将大语言模型应用于药物发现中的候选分子筛选任务，并对其价值进行评估，这直接涉及‘化学大模型’在化学信息学领域的应用。

**📖 中文摘要**

本文提出了一个名为预算敏感发现分数的形式化验证框架，用于评估在预算约束下由AI引导的科学候选物选择策略。作为一个案例研究，该工作评估了多种提议者（包括多种大语言模型配置）在分子发现候选选择任务中的表现，具体使用了MoleculeNet HIV数据集中的SMILES分子表示。研究旨在回答“大语言模型能否为现有的分子发现机器学习流程增加边际价值”这一问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific discovery increasingly relies on AI systems to select candidates for expensive experimental validation, yet no principled, budget-aware evaluation framework exists for comparing selection strategies -- a gap intensified by large language models (LLMs), which generate plausible scientific proposals without reliable downstream evaluation. We introduce the Budget-Sensitive Discovery Score (BSDS), a formally verified metric -- 20 theorems machine-checked by the Lean 4 proof assistant -- that jointly penalizes false discoveries (lambda-weighted FDR) and excessive abstention (gamma-weighted coverage gap) at each budget level. Its budget-averaged form, the Discovery Quality Score (DQS), provides a single summary statistic that no proposer can inflate by performing well at a cherry-picked budget. As a case study, we apply BSDS/DQS to: do LLMs add marginal value to an existing ML pipeline for drug discovery candidate selection? We evaluate 39 proposers -- 11 mechanistic variants, 14 zero-shot LLM configurations, and 14 few-shot LLM configurations -- using SMILES representations on MoleculeNet HIV (41,127 compounds, 3.5% active, 1,000 bootstrap replicates) under both random and scaffold splits. Three findings emerge. First, the simple RF-based Greedy-ML proposer achieves the best DQS (-0.046), outperforming all MLP variants and LLM configurations. Second, no LLM surpasses the Greedy-ML baseline under zero-shot or few-shot evaluation on HIV or Tox21, establishing that LLMs provide no marginal value over an existing trained classifier. Third, the proposer hierarchy generalizes across five MoleculeNet benchmarks spanning 0.18%-46.2% prevalence, a non-drug AV safety domain, and a 9x7 grid of penalty parameters (tau >= 0.636, mean tau = 0.863). The framework applies to any setting where candidates are selected under budget constraints and asymmetric error costs.

</details>

---

### 3. [Shattering the Shortcut: A Topology-Regularized Benchmark for Multi-hop Medical Reasoning in LLMs](https://arxiv.org/abs/2603.12458)

**基本信息**

- 🔗 arXiv: [`2603.12458`](https://arxiv.org/abs/2603.12458)
- 👥 作者: Xing Zi, Xinying Zhou, Jinghao Xiao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12458.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建和评估大语言模型在复杂医学推理任务上的能力，这属于‘化学大模型’（广义上包括生物医学大模型）在专业领域应用的相关研究。

**📖 中文摘要**

本文介绍了ShatterMed-QA，一个用于评估大语言模型在医学领域进行多跳诊断推理能力的双语基准数据集。该数据集包含10,558个多跳临床问题，旨在通过拓扑正则化的医学知识图谱和k- Shattering算法来切断逻辑捷径，迫使模型进行真实的病理级联推理，从而诊断当前医学AI在根本推理能力上的缺陷。论文对21个大语言模型进行了全面评估，并验证了通过检索增强生成恢复被掩盖的证据可以触发性能的普遍恢复。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) achieve expert-level performance on standard medical benchmarks through single-hop factual recall, they severely struggle with the complex, multi-hop diagnostic reasoning required in real-world clinical settings. A primary obstacle is "shortcut learning", where models exploit highly connected, generic hub nodes (e.g., "inflammation") in knowledge graphs to bypass authentic micro-pathological cascades. To address this, we introduce ShatterMed-QA, a bilingual benchmark of 10,558 multi-hop clinical questions designed to rigorously evaluate deep diagnostic reasoning. Our framework constructs a topology-regularized medical Knowledge Graph using a novel $k$-Shattering algorithm, which physically prunes generic hubs to explicitly sever logical shortcuts. We synthesize the evaluation vignettes by applying implicit bridge entity masking and topology-driven hard negative sampling, forcing models to navigate biologically plausible distractors without relying on superficial elimination. Comprehensive evaluations of 21 LLMs reveal massive performance degradation on our multi-hop tasks, particularly among domain-specific models. Crucially, restoring the masked evidence via Retrieval-Augmented Generation (RAG) triggers near-universal performance recovery, validating ShatterMed-QA's structural fidelity and proving its efficacy in diagnosing the fundamental reasoning deficits of current medical AI. Explore the dataset, interactive examples, and full leaderboards at our project website: this https URL

</details>

---

### 4. [TRACE: Temporal Rule-Anchored Chain-of-Evidence on Knowledge Graphs for Interpretable Stock Movement Prediction](https://arxiv.org/abs/2603.12500)

**基本信息**

- 🔗 arXiv: [`2603.12500`](https://arxiv.org/abs/2603.12500)
- 👥 作者: Qianggang Ding, Haochen Shi, Luis Castejón Lozano 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12500.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法整合了大语言模型进行决策制定和解释生成，属于‘化学大模型’（广义AI大模型）在金融领域推理任务中的应用。

**📖 中文摘要**

本文提出了一种名为TRACE的时序规则锚定证据链方法，用于可解释的股票走势预测。该方法在知识图谱上统一了符号关系先验、动态图探索和LLM引导的决策制定。其核心流程包括在知识图谱上进行规则引导的多跳探索，将候选推理链锚定在 contemporaneous 新闻中，并将完全 grounded 的证据聚合成可审计的决策。该方法在标准普尔500指数基准测试中取得了优于基线模型的表现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a Temporal Rule-Anchored Chain-of-Evidence (TRACE) on knowledge graphs for interpretable stock movement prediction that unifies symbolic relational priors, dynamic graph exploration, and LLM-guided decision making in a single end-to-end pipeline. The approach performs rule-guided multi-hop exploration restricted to admissible relation sequences, grounds candidate reasoning chains in contemporaneous news, and aggregates fully grounded evidence into auditable \texttt{UP}/\texttt{DOWN} verdicts with human-readable paths connecting text and structure. On an S\&P~500 benchmark, the method achieves 55.1\% accuracy, 55.7\% precision, 71.5\% recall, and 60.8\% F1, surpassing strong baselines and improving recall and F1 over the best graph baseline under identical evaluation. The gains stem from (i) rule-guided exploration that focuses search on economically meaningful motifs rather than arbitrary walks, and (ii) text-grounded consolidation that selectively aggregates high-confidence, fully grounded hypotheses instead of uniformly pooling weak signals. Together, these choices yield higher sensitivity without sacrificing selectivity, delivering predictive lift with faithful, auditably interpretable explanations.

</details>

---

### 5. [A2Z-10M+: Geometric Deep Learning with A-to-Z BRep Annotations for AI-Assisted CAD Modeling and Reverse Engineering](https://arxiv.org/abs/2603.12605)

**基本信息**

- 🔗 arXiv: [`2603.12605`](https://arxiv.org/abs/2603.12605)
- 👥 作者: Pritham Kumar Jena, Bhavika Baburaj, Tushar Anand 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12605.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模的多模态CAD模型数据集（A2Z），该数据集包含几何、拓扑和文本信息，可作为化学信息学中分子结构表示、3D分子生成或材料设计等任务的宝贵数据资源或预训练基础。

**📖 中文摘要**

本研究提出了A2Z，据称是最大的多模态标注和元数据汇编，包含1000万个ABC CAD模型，旨在解锁前所未有的边界表示学习水平。A2Z包含高分辨率网格、3D手绘草图（配备有关BRep共边、角和面的几何与拓扑信息）以及描述机械世界产品的文本标题和标签。创建如此大规模、结构化的数据非常具有挑战性。作者还合并了额外的25,000个由熟练专业人员设计的电子外壳CAD模型。随后，作者在15万个CAD模型的子集上训练并基准测试了一个基础模型，以从3D扫描中检测BRep共边和角点顶点，这是CAD逆向工程中的关键下游任务。标注的数据集、指标和检查点将被公开发布以支持众多研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reverse engineering and rapid prototyping of computer-aided design (CAD) models from 3D scans, sketches, or simple text prompts are vital in industrial product design. However, recent advances in geometric deep learning techniques lack a multi-modal understanding of parametric CAD features stored in their boundary representation (BRep). This study presents the largest compilation of 10 million multi-modal annotations and metadata for 1 million ABC CAD models, namely A2Z, to unlock an unprecedented level of BRep learning. A2Z comprises (i) high-resolution meshes with salient 3D scanning features, (ii) 3D hand-drawn sketches equipped with (iii) geometric and topological information about BRep co-edges, corners, and surfaces, and (iv) textual captions and tags describing the product in the mechanical world. Creating such carefully structured, large-scale data, which requires nearly 5 terabytes of storage to leverage unparalleled CAD learning/retrieval tasks, is very challenging. The scale, quality, and diversity of our multi-modal annotations are assessed using novel metrics, GPT-5, Gemini, and extensive human feedback mechanisms. To this end, we also merge an additional 25,000 CAD models of electronic enclosures (e.g., tablets, ports) designed by skilled professionals with our A2Z dataset. Subsequently, we train and benchmark a foundation model on a subset of 150K CAD models to detect BRep co-edges and corner vertices from 3D scans, a key downstream task in CAD reverse engineering. The annotated dataset, metrics, and checkpoints will be publicly released to support numerous research directions.

</details>

---

### 6. [Human-AI Collaborative Autonomous Experimentation With Proxy Modeling for Comparative Observation](https://arxiv.org/abs/2603.12618)

**基本信息**

- 🔗 arXiv: [`2603.12618`](https://arxiv.org/abs/2603.12618)
- 👥 作者: Arpan Biswas, Hiroshi Funakubo, Yongtao Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12618.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容涉及化学信息学中的人机协作自主实验优化框架，这是化学大模型和智能实验系统的重要应用场景。

**📖 中文摘要**

本文提出了一种基于代理模型的贝叶斯优化（px-BO）框架，用于在材料科学等领域实现人机协作的自主实验。传统贝叶斯优化在高维、噪声大的实验物理描述符上定义标量目标函数可能出错，且纯数据驱动的探索可能忽略材料系统的细微变化和关键特征。px-BO框架通过人机智能体之间的即时协作，在贝叶斯优化循环中引入投票系统：人类专家对新实验与现有实验进行比较并选择偏好样本，这些人类引导的比较通过拟合Bradley-Terry模型转化为基于代理的目标函数。为了最小化人工交互，迭代训练的代理模型也可作为AI代理用于未来的模拟人类投票，并定期由人类专家验证和修正。论文在模拟数据和PTO样品的BEPS数据上验证了该框架的性能，表明该方法为领域专家提供了更好的控制，实现了比传统数据驱动探索更优的搜索，凸显了人机协作在加速且有意义的材料空间探索中的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Optimization for different tasks like material characterization, synthesis, and functional properties for desired applications over multi-dimensional control parameters need a rapid strategic search through active learning such as Bayesian optimization (BO). However, such high-dimensional experimental physical descriptors are complex and noisy, from which realization of a low-dimensional mathematical scalar metrics or objective functions can be erroneous. Moreover, in traditional purely data-driven autonomous exploration, such objective functions often ignore the subtle variation and key features of the physical descriptors, thereby can fail to discover unknown phenomenon of the material systems. To address this, here we present a proxy-modelled Bayesian optimization (px-BO) via on-the-fly teaming between human and AI agents. Over the loop of BO, instead of defining a mathematical objective function directly from the experimental data, we introduce a voting system on the fly where the new experimental outcome will be compared with existing experiments, and the human agents will choose the preferred samples. These human-guided comparisons are then transformed into a proxy-based objective function via fitting Bradley-Terry (BT) model. Then, to minimize human interaction, this iteratively trained proxy model also acts as an AI agent for future surrogate human votes. Finally, these surrogate votes are periodically validated by human agents, and the corrections are then learned by the proxy model on-the-fly. We demonstrated the performance of the proposed px-BO framework into simulated and BEPS data generated from PTO sample. We find that our approach provided better control of the domain experts for an improved search over traditional data-driven exploration, thus, signifies the importance of human-AI teaming in an accelerated and meaningful material space exploration.

</details>

---

### 7. [Using a Human-AI Teaming Approach to Create and Curate Scientific Datasets with the SCILIRE System](https://arxiv.org/abs/2603.12638)

**基本信息**

- 🔗 arXiv: [`2603.12638`](https://arxiv.org/abs/2603.12638)
- 👥 作者: Necva Bölücü, Jessica Irons, Changhyun Lee 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12638.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于从科学文献（包括化学领域）创建和整理数据集的系统（SCILIRE），这为化学大模型和质谱分析等领域提供了数据资源和工具支持。

**📖 中文摘要**

本文介绍了SCILIRE系统，一个基于人机协作原则从科学文献中创建数据集的系统。科学文献的快速增长使得手动提取结构化知识变得不切实际。SCILIRE围绕以工作流为中心的人机协作原则设计，用于验证和整理数据。它促进了一种迭代工作流，研究人员可以在其中审查和纠正AI输出。此外，这种交互被用作反馈信号来改进未来基于LLM的推理。作者通过内在基准测试结果和跨多个领域的真实案例研究来评估其设计。结果表明，SCILIRE提高了提取保真度，并促进了高效的数据集创建。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of scientific literature has made manual extraction of structured knowledge increasingly impractical. To address this challenge, we introduce SCILIRE, a system for creating datasets from scientific literature. SCILIRE has been designed around Human-AI teaming principles centred on workflows for verifying and curating data. It facilitates an iterative workflow in which researchers can review and correct AI outputs. Furthermore, this interaction is used as a feedback signal to improve future LLM-based inference. We evaluate our design using a combination of intrinsic benchmarking outcomes together with real-world case studies across multiple domains. The results demonstrate that SCILIRE improves extraction fidelity and facilitates efficient dataset creation.

</details>

---

### 8. [Continual Learning in Large Language Models: Methods, Challenges, and Opportunities](https://arxiv.org/abs/2603.12658)

**基本信息**

- 🔗 arXiv: [`2603.12658`](https://arxiv.org/abs/2603.12658)
- 👥 作者: Hongyang Chen, Zhongwu Sun, Hongfei Ye 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12658.pdf)

**💡 相关性分析**

满足标准3：论文是关于大语言模型（包括潜在的化学领域大模型）持续学习方法的综述，包含了对该主题的重要讨论和展望。

**📖 中文摘要**

本文是关于大语言模型持续学习的综述。持续学习已成为使大语言模型能够动态适应不断发展的知识和顺序任务，同时减轻灾难性遗忘的关键范式。本综述围绕三个核心训练阶段（持续预训练、持续微调和持续指令调优）构建，全面概述了为大语言模型量身定制的持续学习方法。在经典的基于排练、正则化和架构的方法分类基础上，进一步根据其独特的遗忘缓解机制对每个类别进行细分，并对传统持续学习方法在大语言模型上的适应性和关键改进进行了严格的比较分析。综述涵盖了基本评估指标（如遗忘率和知识迁移效率）以及用于评估持续学习性能的新兴基准。分析表明，虽然当前方法在特定领域显示出有希望的结果，但在实现跨不同任务和时间尺度的无缝知识整合方面仍存在根本性挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continual learning (CL) has emerged as a pivotal paradigm to enable large language models (LLMs) to dynamically adapt to evolving knowledge and sequential tasks while mitigating catastrophic forgetting-a critical limitation of the static pre-training paradigm inherent to modern LLMs. This survey presents a comprehensive overview of CL methodologies tailored for LLMs, structured around three core training stages: continual pre-training, continual fine-tuning, and continual this http URL the canonical taxonomy of rehearsal-, regularization-, and architecture-based methods, we further subdivide each category by its distinct forgetting mitigation mechanisms and conduct a rigorous comparative analysis of the adaptability and critical improvements of traditional CL methods for LLMs. In doing so, we explicitly highlight core distinctions between LLM CL and traditional machine learning, particularly with respect to scale, parameter efficiency, and emergent capabilities. Our analysis covers essential evaluation metrics, including forgetting rates and knowledge transfer efficiency, along with emerging benchmarks for assessing CL performance. This survey reveals that while current methods demonstrate promising results in specific domains, fundamental challenges persist in achieving seamless knowledge integration across diverse tasks and temporal scales. This systematic review contributes to the growing body of knowledge on LLM adaptation, providing researchers and practitioners with a structured framework for understanding current achievements and future opportunities in lifelong learning for language models.

</details>

---

### 9. [RetroReasoner: A Reasoning LLM for Strategic Retrosynthesis Prediction](https://arxiv.org/abs/2603.12666)

**基本信息**

- 🔗 arXiv: [`2603.12666`](https://arxiv.org/abs/2603.12666)
- 👥 作者: Hanbum Ko, Chanhui Lee, Ye Rin Kim 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12666.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容直接围绕化学大模型（RetroReasoner是一个用于逆合成预测的化学领域大语言模型）和质谱结构推理（逆合成预测是质谱结构解析和分子结构推理的核心上游任务，密切相关）。

**📖 中文摘要**

本文提出RetroReasoner，一个用于逆合成预测的推理型大语言模型。逆合成是有机合成的核心任务，旨在为给定产物分子预测反应物。传统方法依赖化学家选择合理的键断裂策略并推导相应反应物，耗时且需要大量专业知识。RetroReasoner借鉴化学家的策略性思维，通过监督微调和强化学习进行训练。监督微调阶段，作者引入了SyntheticRetro框架，生成结构化的断裂原理说明和反应物预测。强化学习阶段，则采用往返准确性作为奖励信号，即预测的反应物通过正向合成模型生成产物，若与原始输入产物匹配则给予奖励。实验表明，RetroReasoner不仅性能优于现有基线，还能生成更广泛的可行反应物方案，尤其在处理更具挑战性的反应实例时表现出色。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrosynthesis prediction is a core task in organic synthesis that aims to predict reactants for a given product molecule. Traditionally, chemists select a plausible bond disconnection and derive corresponding reactants, which is time-consuming and requires substantial expertise. While recent advancements in molecular large language models (LLMs) have made progress, many methods either predict reactants without strategic reasoning or conduct only a generic product analysis, rather than reason explicitly about bond-disconnection strategies that logically lead to the choice of specific reactants. To overcome these limitations, we propose RetroReasoner, a retrosynthetic reasoning model that leverages chemists' strategic thinking. RetroReasoner is trained using both supervised fine-tuning (SFT) and reinforcement learning (RL). For SFT, we introduce SyntheticRetro, a framework that generates structured disconnection rationales alongside reactant predictions. In the case of RL, we apply a round-trip accuracy as reward, where predicted reactants are passed through a forward synthesis model, and predictions are rewarded when the forward-predicted product matches the original input product. Experimental results show that RetroReasoner not only outperforms prior baselines but also generates a broader range of feasible reactant proposals, particularly in handling more challenging reaction instances.

</details>

---

### 10. [RXNRECer Enables Fine-grained Enzymatic Function Annotation through Active Learning and Protein Language Models](https://arxiv.org/abs/2603.12694)

**基本信息**

- 🔗 arXiv: [`2603.12694`](https://arxiv.org/abs/2603.12694)
- 👥 作者: Zhenkun Shi, Jun Zhu, Dehang Wang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12694.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用蛋白质语言模型（化学大模型的一种）进行酶催化反应的直接预测，属于化学信息学领域，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了RXNRECer，一个基于Transformer的集成框架，用于直接预测酶催化反应，而无需依赖EC编号。它整合了蛋白质语言建模和主动学习，以捕获高级序列语义和细粒度的转化模式。该工作直接涉及化学信息学中的大模型（蛋白质语言模型）应用，用于解决酶功能注释这一核心的生物化学信息学问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A key challenge in enzyme annotation is identifying the biochemical reactions catalyzed by proteins. Most existing methods rely on Enzyme Commission (EC) numbers as intermediaries: they first predict an EC number and then retrieve the associated reactions. This indirect strategy introduces ambiguity due to the complex many-to-many mappings among proteins, EC numbers, and reactions, and is further complicated by frequent updates to EC numbers and inconsistencies across databases. To address these challenges, we present RXNRECer, a transformer-based ensemble framework that directly predicts enzyme-catalyzed reactions without relying on EC numbers. It integrates protein language modeling and active learning to capture both high-level sequence semantics and fine-grained transformation patterns. Evaluations on curated cross-validation and temporal test sets demonstrate consistent improvements over six EC-based baselines, with gains of 16.54% in F1 score and 15.43% in accuracy. Beyond accuracy gains, the framework offers clear advantages for downstream applications, including scalable proteome-wide reaction annotation, enhanced specificity in refining generic reaction schemas, systematic annotation of previously uncurated proteins, and reliable identification of enzyme promiscuity. By incorporating large language models, it also provides interpretable rationales for predictions. These capabilities make RXNRECer a robust and versatile solution for EC-free, fine-grained enzyme function prediction, with potential applications across multiple areas of enzyme research and industrial applications.

</details>

---

### 11. [SciDesignBench: Benchmarking and Improving Language Models for Scientific Inverse Design](https://arxiv.org/abs/2603.12724)

**基本信息**

- 🔗 arXiv: [`2603.12724`](https://arxiv.org/abs/2603.12724)
- 👥 作者: David van Dijk, Ivan Vrkic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12724.pdf)

**💡 相关性分析**

满足标准1和标准3：论文的核心是构建基准和训练方法来提升语言模型（作为大模型的一种）在科学逆向设计（包括化学分子设计）中的能力，与“化学大模型”主题直接相关。同时，它作为一个基准和训练范式的提出，也包含了对该领域未来方向的重要讨论。

**📖 中文摘要**

本文介绍了SciDesignBench，一个包含14个科学领域、520个基于模拟器的任务的基准测试集，用于评估语言模型在科学逆向设计（如给定目标寻找满足条件的分子设计）中的能力。该基准测试了从单次设计到多轮模拟器反馈优化的多种设置。论文还提出了RLSF，一种利用模拟器反馈进行模型训练的方法。这项工作为评估和提升大语言模型在化学、材料等领域的逆向设计能力提供了基准和训练方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many of the most important problems in science and engineering are inverse problems: given a desired outcome, find a design that achieves it. Evaluating whether a candidate meets the spec is often routine; a binding energy can be computed, a reactor yield simulated, a pharmacokinetic profile predicted. But searching a combinatorial design space for inputs that satisfy those targets is fundamentally harder. We introduce SciDesignBench, a benchmark of 520 simulator-grounded tasks across 14 scientific domains and five settings spanning single-shot design, short-horizon feedback, long-horizon refinement, and seed-design optimization. On the 10-domain shared-core subset, the best zero-shot model reaches only 29.0% success despite substantially higher parse rates. Simulator feedback helps, but the leaderboard changes with horizon: Sonnet 4.5 is strongest in one-turn de novo design, whereas Opus 4.6 is strongest after 20 turns of simulator-grounded refinement. Providing a starting seed design reshuffles the leaderboard again, demonstrating that constrained modification requires a fundamentally different capability from unconstrained de novo generation. We then introduce RLSF, a simulator-feedback training recipe. An RLSF-tuned 8B model raises single-turn success rates by 8-17 percentage points across three domains. Together, these results position simulator-grounded inverse design as both a benchmark for scientific reasoning and a practical substrate for amortizing expensive test-time compute into model weights.

</details>

---

### 12. [A Multi-task Large Reasoning Model for Molecular Science](https://arxiv.org/abs/2603.12808)

**基本信息**

- 🔗 arXiv: [`2603.12808`](https://arxiv.org/abs/2603.12808)
- 👥 作者: Pengfei Liu, Shuang Ge, Jun Tao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12808.pdf)

**💡 相关性分析**

满足标准1：论文的核心是提出一个用于分子科学（化学信息学核心领域）的多任务大型推理模型，该模型整合了大语言模型和强化学习进行结构化推理，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文介绍了一个用于分子科学的多任务大型推理模型，旨在通过结构化推理和反思模拟分子科学家的认知。该模型整合了多专家模块和基于强化学习的思维链框架。在10个分子任务上的系统评估显示，该模型在数据量和计算资源更少的情况下，性能超越了包括超大规模基础模型在内的20多个先进基线。这验证了嵌入显式推理机制可实现高效学习。该框架通过中枢神经系统药物候选物设计的案例研究验证了其实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advancements in artificial intelligence for molecular science are necessitating a paradigm shift from purely data-driven predictions to knowledge-guided computational reasoning. Existing molecular models are predominantly proprietary, lacking general molecular intelligence and generalizability. This underscores the necessity for computational methods that can effectively integrate scientific logic with deep learning architectures. Here we introduce a multi-task large reasoning model designed to emulate the cognitive processes of molecular scientists through structured reasoning and reflection. Our approach incorporates multi-specialist modules to provide versatile molecular expertise and a chain-of-thought (CoT) framework enhanced by reinforcement learning infused with molecular knowledge, enabling structured and reflective reasoning. Systematic evaluations across 10 molecular tasks and 47 metrics demonstrate that our model achieves an average 50.3% improvement over the base architecture, outperforming over 20 state-of-the-art baselines, including ultra-large-parameter foundation models, despite using significantly fewer training data and computational resources. This validates that embedding explicit reasoning mechanisms enables high-efficiency learning, allowing smaller-scale models to surpass massive counterparts in both efficacy and interpretability. The practical utility of this computational framework was validated through a case study on the design of central nervous system (CNS) drug candidates, illustrating its capacity to bridge data-driven and knowledge-integrated approaches for intelligent molecular design.

</details>

---

### 13. [Enhanced Drug-drug Interaction Prediction Using Adaptive Knowledge Integration](https://arxiv.org/abs/2603.12885)

**基本信息**

- 🔗 arXiv: [`2603.12885`](https://arxiv.org/abs/2603.12885)
- 👥 作者: Pengfei Liu, Jun Tao, Zhixiang Ren
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12885.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究是利用强化学习优化大型语言模型（作为化学领域应用的大模型）在药物-药物相互作用预测这一化学信息学关键任务中的性能，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一种知识增强框架，用于药物-药物相互作用事件预测。该框架利用强化学习技术，自适应地将先验药物知识注入大型语言模型，以优化策略空间，从而提升LLM在DDIE预测中的准确性。通过小样本学习取得了显著改进。这项工作为DDIE预测中的科学知识学习建立了一个有效的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drug-drug interaction event (DDIE) prediction is crucial for preventing adverse reactions and ensuring optimal therapeutic outcomes. However, existing methods often face challenges with imbalanced datasets, complex interaction mechanisms, and poor generalization to unknown drug combinations. To address these challenges, we propose a knowledge augmentation framework that adaptively infuses prior drug knowledge into a large language model (LLM). This framework utilizes reinforcement learning techniques to facilitate adaptive knowledge extraction and synthesis, thereby efficiently optimizing the strategy space to enhance the accuracy of LLMs for DDIE predictions. As a result of few-shot learning, we achieved a notable improvement compared to the baseline. This approach establishes an effective framework for scientific knowledge learning for DDIE predictions.

</details>

---

### 14. [DS$^2$-Instruct: Domain-Specific Data Synthesis for Large Language Models Instruction Tuning](https://arxiv.org/abs/2603.12932)

**基本信息**

- 🔗 arXiv: [`2603.12932`](https://arxiv.org/abs/2603.12932)
- 👥 作者: Ruiyao Xu, Noelle I. Samia, Han Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12932.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何为特定领域（如数学、金融）生成高质量的指令调优数据，以提升大语言模型在该领域的性能。这直接关联“化学大模型”主题，因为该方法论可以迁移并应用于生成化学领域的指令数据，从而训练或优化化学领域的大模型。

**📖 中文摘要**

本文提出DS²-Instruct，一个用于大语言模型指令调优的零样本领域特定数据合成框架。该框架旨在解决现有数据合成方法在捕捉领域特定术语和推理模式方面的不足。它首先生成任务相关的关键词以确保全面的领域覆盖，然后结合布鲁姆分类法的不同认知层次创建多样化的指令，最后通过自一致性验证来保证数据质量。作者将该框架应用于数学、金融和逻辑推理等七个具有挑战性的领域生成数据集。综合评估表明，使用生成数据微调的模型相比现有数据生成方法有显著提升。这项工作直接关联“化学大模型”主题，因为它提供了一种为特定领域（如化学）生成高质量指令调优数据的方法论，这对于训练领域专用的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting Large Language Models (LLMs) to specialized domains requires high-quality instruction tuning datasets, which are expensive to create through human annotation. Existing data synthesis methods focus on general-purpose tasks and fail to capture domain-specific terminology and reasoning patterns. To address this, we introduce DS$^2$-Instruct, a zero-shot framework that generates domain-specific instruction datasets without human supervision. Our approach first generates task-informed keywords to ensure comprehensive domain coverage. It then creates diverse instructions by pairing these keywords with different cognitive levels from Bloom's Taxonomy. Finally, it uses self-consistency validation to ensure data quality. We apply this framework to generate datasets across seven challenging domains, such as mathematics, finance, and logical reasoning. Comprehensive evaluation demonstrates that models fine-tuned on our generated data achieve substantial improvements over existing data generation methods.

</details>

---

### 15. [Efficient and Interpretable Multi-Agent LLM Routing via Ant Colony Optimization](https://arxiv.org/abs/2603.12933)

**基本信息**

- 🔗 arXiv: [`2603.12933`](https://arxiv.org/abs/2603.12933)
- 👥 作者: Xudong Wang, Chaoning Zhang, Jiaquan Zhang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12933.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型在多智能体系统中的路由与协调优化。虽然应用场景是通用的，但其关于LLM驱动的多智能体系统架构、效率与可解释性的研究，为构建复杂的、由多个专业化模型（例如，分别负责反应预测、性质计算、文献检索的智能体）协同工作的“化学大模型”或智能体系统提供了技术参考和思路。

**📖 中文摘要**

本文提出AMRO-S，一个用于大语言模型驱动的多智能体系统的高效且可解释的路由框架。该框架将多智能体系统的路由建模为一个语义条件路径选择问题，通过三个关键机制提升路由性能：使用监督微调的小语言模型进行意图推断，为每个查询提供低开销的语义接口；将路由记忆分解为任务特定的信息素专家，减少跨任务干扰并在混合工作负载下优化路径选择；采用质量门控的异步更新机制，将推理与学习解耦，在不增加延迟的情况下优化路由。广泛的实验表明，AMRO-S在质量和成本权衡上优于强基线路由方法。这项工作与“化学大模型”主题相关，因为它研究了大语言模型在多智能体系统中的高效协调与路由问题，这种架构和优化思路可以应用于构建由多个化学信息处理智能体组成的复杂系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Model (LLM)-driven Multi-Agent Systems (MAS) have demonstrated strong capability in complex reasoning and tool use, and heterogeneous agent pools further broaden the quality--cost trade-off space. Despite these advances, real-world deployment is often constrained by high inference cost, latency, and limited transparency, which hinders scalable and efficient routing. Existing routing strategies typically rely on expensive LLM-based selectors or static policies, and offer limited controllability for semantic-aware routing under dynamic loads and mixed intents, often resulting in unstable performance and inefficient resource utilization. To address these limitations, we propose AMRO-S, an efficient and interpretable routing framework for Multi-Agent Systems (MAS). AMRO-S models MAS routing as a semantic-conditioned path selection problem, enhancing routing performance through three key mechanisms: First, it leverages a supervised fine-tuned (SFT) small language model for intent inference, providing a low-overhead semantic interface for each query; second, it decomposes routing memory into task-specific pheromone specialists, reducing cross-task interference and optimizing path selection under mixed workloads; finally, it employs a quality-gated asynchronous update mechanism to decouple inference from learning, optimizing routing without increasing latency. Extensive experiments on five public benchmarks and high-concurrency stress tests demonstrate that AMRO-S consistently improves the quality--cost trade-off over strong routing baselines, while providing traceable routing evidence through structured pheromone patterns.

</details>

---

### 16. [Can Fairness Be Prompted? Prompt-Based Debiasing Strategies in High-Stakes Recommendations](https://arxiv.org/abs/2603.12935)

**基本信息**

- 🔗 arXiv: [`2603.12935`](https://arxiv.org/abs/2603.12935)
- 👥 作者: Mihaela Rotar, Theresia Veronika Rampisela, Maria Maistro
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12935.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型的公平性去偏，特别是通过提示工程这一轻量级方法。虽然应用场景是推荐系统，但其方法论（提示策略）和关注点（模型偏见）对于任何领域的大模型（包括化学大模型）都具有普适的参考价值，有助于构建更负责任、更公平的化学AI系统。

**📖 中文摘要**

本文研究了大语言模型推荐系统中存在的隐性偏见，并探索了基于提示的轻量级去偏策略是否可行。大语言模型可以从姓名、代词等间接线索推断出性别、年龄等敏感属性，可能导致推荐结果产生偏见。作者贡献了三种针对LLM推荐器的偏见感知提示策略。据作者所知，这是首个专注于用户群体公平性的、在LLM推荐器中研究基于提示的去偏方法的工作。实验表明，所提出的去偏方法（即指示LLM保持公平）可以在保持可比有效性的同时，将公平性提升高达74%。这项工作与“化学大模型”主题相关，因为它探讨了大语言模型中的公平性与去偏技术。在构建用于药物发现、材料设计等领域的化学大模型时，确保模型决策的公平性和无偏见至关重要，该研究提供的提示工程方法为缓解化学大模型可能存在的偏见提供了一种轻量级解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) can infer sensitive attributes such as gender or age from indirect cues like names and pronouns, potentially biasing recommendations. While several debiasing methods exist, they require access to the LLMs' weights, are computationally costly, and cannot be used by lay users. To address this gap, we investigate implicit biases in LLM Recommenders (LLMRecs) and explore whether prompt-based strategies can serve as a lightweight and easy-to-use debiasing approach. We contribute three bias-aware prompting strategies for LLMRecs. To our knowledge, this is the first study on prompt-based debiasing approaches in LLMRecs that focuses on group fairness for users. Our experiments with 3 LLMs, 4 prompt templates, 9 sensitive attribute values, and 2 datasets show that our proposed debiasing approach, which instructs an LLM to be fair, can improve fairness by up to 74% while retaining comparable effectiveness, but might overpromote specific demographic groups in some cases.

</details>

---

### 17. [Delta1 with LLM: symbolic and neural integration for credible and explainable reasoning](https://arxiv.org/abs/2603.12953)

**基本信息**

- 🔗 arXiv: [`2603.12953`](https://arxiv.org/abs/2603.12953)
- 👥 作者: Yang Xu, Jun Liu, Shuwei Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12953.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是神经符号推理，旨在结合形式化逻辑的严谨性与大语言模型的可解释性。这种构建可解释、可靠AI系统的方法论，对于开发需要严格推理和可审计决策过程的“化学大模型”（例如，用于药物安全性评估或合成路线设计）具有重要的参考价值。

**📖 中文摘要**

本文介绍了一个端到端的可解释性构建流程，该流程将基于全三角标准矛盾的自动定理生成器Delta1与大语言模型集成。Delta1以构造性方式确定性地生成最小不可满足子句集和完备定理，确保了可靠性和最小性。LLM层将每个定理和证明轨迹用连贯的自然语言进行表述，生成可解释的说明和可操作的见解。在医疗保健、合规和监管等领域的实证研究表明，Delta1与LLM的结合能够实现可解释、可审计且与领域对齐的推理。这项工作推动了逻辑、语言和学习的融合，将构造性定理生成定位为神经符号可解释AI的原则性基础。该研究与“化学大模型”主题相关，因为它提供了一种将形式化逻辑推理与LLM的自然语言能力相结合以增强模型可解释性和可靠性的框架。在化学信息学中，对于分子性质预测、反应结果推理等任务，这种神经符号方法可以帮助构建更透明、更可信的化学大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neuro-symbolic reasoning increasingly demands frameworks that unite the formal rigor of logic with the interpretability of large language models (LLMs). We introduce an end to end explainability by construction pipeline integrating the Automated Theorem Generator Delta1 based on the full triangular standard contradiction (FTSC) with LLMs. Delta1 deterministically constructs minimal unsatisfiable clause sets and complete theorems in polynomial time, ensuring both soundness and minimality by construction. The LLM layer verbalizes each theorem and proof trace into coherent natural language explanations and actionable insights. Empirical studies across health care, compliance, and regulatory domains show that Delta1 and LLM enables interpretable, auditable, and domain aligned reasoning. This work advances the convergence of logic, language, and learning, positioning constructive theorem generation as a principled foundation for neuro-symbolic explainable AI.

</details>

---

### 18. [Long-form RewardBench: Evaluating Reward Models for Long-form Generation](https://arxiv.org/abs/2603.12963)

**基本信息**

- 🔗 arXiv: [`2603.12963`](https://arxiv.org/abs/2603.12963)
- 👥 作者: Hui Huang, Yancheng He, Wei Liu 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12963.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和改进用于长文本生成的奖励模型。奖励模型是使用RLHF等技术对齐和优化大语言模型（包括潜在的化学大模型）的核心部件。该工作建立的基准和发现，对于未来训练能生成高质量、可靠长格式化学文本的领域大模型具有直接指导意义。

**📖 中文摘要**

本文介绍了Long-form RewardBench，这是首个专门为长文本生成设计的奖励建模测试平台。随着基于强化学习的对齐方法广泛采用，奖励模型的重要性日益增长。该基准涵盖了问答、检索增强生成、聊天、写作和推理五个关键子任务。作者通过精心设计的多阶段数据收集过程收集了指令和偏好数据，并对20多个主流奖励模型（包括分类器和生成模型）进行了广泛实验。研究发现，当前模型仍然缺乏长文本奖励建模能力。此外，作者设计了一种新颖的“长文本大海捞针”测试，揭示了奖励建模性能与错误在响应中的位置以及整体响应长度之间的相关性，并且分类模型和生成模型表现出不同的特性。最后，实验证明分类器相比在相同数据上训练的生成模型具有更好的泛化能力。作为首个长文本奖励建模基准，这项工作旨在为该关键领域的进展评估提供一个稳健的平台。该研究与“化学大模型”主题相关，因为奖励模型是使用强化学习人类反馈对齐大语言模型（包括化学领域大模型）的关键组件。评估和提升奖励模型在生成长格式化学文本（如实验报告、文献综述、分子描述）方面的能力，对于优化化学大模型的输出质量和安全性至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The widespread adoption of reinforcement learning-based alignment highlights the growing importance of reward models. Various benchmarks have been built to evaluate reward models in various domains and scenarios. However, a significant gap remains in assessing reward models for long-form generation, despite its critical role in real-world applications. To bridge this, we introduce Long-form RewardBench, the first reward modeling testbed specifically designed for long-form generation. Our benchmark encompasses five key subtasks: QA, RAG, Chat, Writing, and Reasoning. We collected instruction and preference data through a meticulously designed multi-stage data collection process, and conducted extensive experiments on 20+ mainstream reward models, including both classifiers and generative models. Our findings reveal that current models still lack long-form reward modeling capabilities. Furthermore, we designed a novel Long-form Needle-in-a-Haystack Test, which revealed a correlation between reward modeling performance and the error's position within a response, as well as the overall response length, with distinct characteristics observed between classification and generative models. Finally, we demonstrate that classifiers exhibit better generalizability compared to generative models trained on the same data. As the first benchmark for long-form reward modeling, this work aims to offer a robust platform for visualizing progress in this crucial area.

</details>

---

### 19. [Is Human Annotation Necessary? Iterative MBR Distillation for Error Span Detection in Machine Translation](https://arxiv.org/abs/2603.12983)

**基本信息**

- 🔗 arXiv: [`2603.12983`](https://arxiv.org/abs/2603.12983)
- 👥 作者: Boxuan Lyu, Haiyue Song, Zhi Qu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12983.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种利用大语言模型自动生成伪标签以构建训练数据的方法。这种方法可以作为一种数据资源生成工具，应用于“质谱结构推理”领域，帮助从大量未标注的质谱数据中生成可用于模型训练的结构关联数据，从而解决该领域数据标注成本高的问题。

**📖 中文摘要**

本文提出了一种基于最小贝叶斯风险解码的新型自进化框架，名为“用于错误跨度检测的迭代MBR蒸馏”，旨在消除机器翻译评估中错误跨度检测任务对人工标注的依赖。该框架利用现成的大语言模型生成伪标签。在WMT指标共享任务数据集上的实验表明，仅在这些自生成的伪标签上训练的模型，在系统和跨度级别上均优于未适应的基础模型和使用人工标注训练的监督基线，同时在句子级别保持竞争力。该研究与“化学大模型”主题相关，因为它展示了一种利用大语言模型自动生成高质量训练数据（伪标签）以改进下游任务性能的方法。这种方法可以迁移到化学领域，例如，利用化学大模型为未标注的质谱-结构对生成伪标签，从而用于训练或改进“质谱结构推理”模型，缓解该领域标注数据稀缺的问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Error Span Detection (ESD) is a crucial subtask in Machine Translation (MT) evaluation, aiming to identify the location and severity of translation errors. While fine-tuning models on human-annotated data improves ESD performance, acquiring such data is expensive and prone to inconsistencies among annotators. To address this, we propose a novel self-evolution framework based on Minimum Bayes Risk (MBR) decoding, named Iterative MBR Distillation for ESD, which eliminates the reliance on human annotations by leveraging an off-the-shelf LLM to generate this http URL experiments on the WMT Metrics Shared Task datasets demonstrate that models trained solely on these self-generated pseudo-labels outperform both unadapted base model and supervised baselines trained on human annotations at the system and span levels, while maintaining competitive sentence-level performance.

</details>

---

### 20. [Deconstructing the Failure of Ideal Noise Correction: A Three-Pillar Diagnosis](https://arxiv.org/abs/2603.12997)

**基本信息**

- 🔗 arXiv: [`2603.12997`](https://arxiv.org/abs/2603.12997)
- 👥 作者: Chen Feng, Zhuo Zhi, Zhao Huang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12997.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习中“带噪声标签学习”这一基础问题的机理分析。虽然不直接针对质谱，但其揭示的理论和原理完全适用于“质谱结构推理”任务，因为该任务中用于训练的数据集很可能包含不准确或冲突的结构标注（即噪声标签）。该工作为构建对此类噪声具有鲁棒性的质谱结构推理模型提供了重要的理论基础和设计启示。

**📖 中文摘要**

本文对基于噪声转移矩阵的标签噪声学习方法的失败进行了深入诊断。即使在理想条件下（提供完美的、先知般的转移矩阵），这些理论上具有一致性的校正方法仍然会在训练过程中出现性能崩溃。这证明失败的根本原因并非转移矩阵估计问题，而是源于更深层次的缺陷。作者通过宏观收敛状态、微观优化动力学和信息论限制三个层面的统一分析来解释这一行为。这些结果为理想噪声校正为何失败提供了正式解释，并为设计更可靠的标签噪声学习方法提供了具体指导。该研究与“质谱结构推理”主题相关，因为在质谱解析中，数据库匹配或预测模型可能会产生带有噪声（错误）的结构标注。理解并解决在噪声标签下学习模型的根本挑战，对于开发能够从可能存在标注错误的质谱-结构数据中稳健学习的推理模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Statistically consistent methods based on the noise transition matrix ($T$) offer a theoretically grounded solution to Learning with Noisy Labels (LNL), with guarantees of convergence to the optimal clean-data classifier. In practice, however, these methods are often outperformed by empirical approaches such as sample selection, and this gap is usually attributed to the difficulty of accurately estimating $T$. The common assumption is that, given a perfect $T$, noise-correction methods would recover their theoretical advantage. In this work, we put this longstanding hypothesis to a decisive test. We conduct experiments under idealized conditions, providing correction methods with a perfect, oracle transition matrix. Even under these ideal conditions, we observe that these methods still suffer from performance collapse during training. This compellingly demonstrates that the failure is not fundamentally a $T$-estimation problem, but stems from a more deeply rooted flaw. To explain this behaviour, we provide a unified analysis that links three levels: macroscopic convergence states, microscopic optimisation dynamics, and information-theoretic limits on what can be learned from noisy labels. Together, these results give a formal account of why ideal noise correction fails and offer concrete guidance for designing more reliable methods for learning with noisy labels.

</details>

---

### 21. [Mending the Holes: Mitigating Reward Hacking in Reinforcement Learning for Multilingual Translation](https://arxiv.org/abs/2603.13045)

**基本信息**

- 🔗 arXiv: [`2603.13045`](https://arxiv.org/abs/2603.13045)
- 👥 作者: Yifeng Liu, Siqi Ouyang, Yatish Hosmane Revanasiddappa 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13045.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过改进强化学习奖励设计来提升大语言模型在多语言翻译中的性能。其关于奖励函数设计、避免奖励黑客和利用对齐技术的思想，可以迁移到使用强化学习优化“化学大模型”或“质谱结构推理”模型的任务中，例如设计奖励以鼓励模型生成化学上有效的分子描述或质谱解析结果。

**📖 中文摘要**

本文介绍了WALAR，一种仅使用单语文本的强化训练方法，旨在提升大语言模型在大量低资源语言上的翻译能力，同时保持其在高资源语言上的性能。该方法的关键洞见基于对现有基于源语的多语言质量评估模型失败模式（或“漏洞”）的观察。使用这些QE模型进行强化学习往往会放大此类漏洞，导致多语言LLM性能变差。作者开发了包括词对齐和语言对齐在内的技术，以减轻WALAR的强化学习奖励中的此类漏洞。作者使用WALAR持续训练了一个支持101种语言翻译的LLM。实验表明，新模型在Flores-101数据集的1400个语言方向上大幅优于最强的开源多语言LLM之一LLaMAX。该研究与“化学大模型”和“质谱结构推理”均相关。对于化学大模型，多语言能力有助于处理全球化的化学文献和专利。更重要的是，该方法中缓解奖励“漏洞”的技术（如对齐），可以启发我们设计更合理的奖励函数，用于通过强化学习对齐或优化化学领域大模型（例如，确保生成的分子结构不仅语法正确，而且化学合理）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated remarkable capability in machine translation on high-resource language pairs, yet their performance on low-resource translation still lags behind. Existing post-training methods rely heavily on high-quality parallel data, which are often scarce or unavailable for low-resource languages. In this paper, we introduce WALAR, a reinforcement training method using only monolingual text to elevate LLMs' translation capabilities on massive low-resource languages while retaining their performance on high-resource languages. Our key insight is based on the observation of failure modes (or "holes") in existing source-based multilingual quality estimation (QE) models. Reinforcement learning (RL) using these QE models tends to amplify such holes, resulting in poorer multilingual LLMs. We develop techniques including word alignment and language alignment to mitigate such holes in WALAR's reward for RL training. We continually trained an LLM supporting translation of 101 languages using WALAR. The experiments show that our new model outperforms LLaMAX, one of the strongest open-source multilingual LLMs by a large margin on 1400 language directions on Flores-101 dataset.

</details>

---

### 22. [Causal Cellular Context Transfer Learning (C3TL): An Efficient Architecture for Prediction of Unseen Perturbation Effects](https://arxiv.org/abs/2603.13051)

**基本信息**

- 🔗 arXiv: [`2603.13051`](https://arxiv.org/abs/2603.13051)
- 👥 作者: Michael Scholkemper, Sach Mukherjee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13051.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文直接研究化学扰动对生物系统影响的预测模型，这是化学信息学和药物发现的核心问题。2) 数据资源相关：论文提出了一种利用现有批量分子数据构建预测模型的框架，这种方法论本身可以视为一种构建用于化学扰动响应预测的数据集和模型资源的新策略。

**📖 中文摘要**

本文提出了一个轻量级框架，用于预测化学和遗传扰动对定量细胞状态的影响。该框架利用生物干预的结构化性质以及特定的归纳偏置/不变性，允许泛化到新的上下文环境，并且仅需要广泛可用的批量分子数据。通过将预测的上下文特异性扰动效应与真实的大规模干预实验进行比较，广泛的测试证明了在新上下文中的准确预测能力。所提出的方法与最先进的基础模型竞争，但需要更简单的数据、更小的模型规模和更少的时间。通过关注稳健的批量信号和高效的架构，研究表明，无需专有硬件或超大型模型，准确预测扰动效应是可能的，从而为在生物医学中广泛利用因果学习方法开辟了道路。该研究与“化学大模型”和“质谱结构推理”高度相关。它直接针对“化学扰动”（即化合物处理）对细胞系统的影响进行预测建模，这是药物发现和化学生物学的核心。其轻量级、高效率的架构设计思路，以及利用现有数据泛化到新场景的能力，对于构建用于预测分子生物活性的化学大模型具有重要参考价值。同时，细胞对化学扰动的响应数据常通过质谱等组学技术获取，因此该工作也与“质谱结构推理”的 downstream 应用相连。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting the effects of chemical and genetic perturbations on quantitative cell states is a central challenge in computational biology, molecular medicine and drug discovery. Recent work has leveraged large-scale single-cell data and massive foundation models to address this task. However, such computational resources and extensive datasets are not always accessible in academic or clinical settings, hence limiting utility. Here we propose a lightweight framework for perturbation effect prediction that exploits the structured nature of biological interventions and specific inductive biases/invariances. Our approach leverages available information concerning perturbation effects to allow generalization to novel contexts and requires only widely-available bulk molecular data. Extensive testing, comparing predictions of context-specific perturbation effects against real, large-scale interventional experiments, demonstrates accurate prediction in new contexts. The proposed approach is competitive with SOTA foundation models but requires simpler data, much smaller model sizes and less time. Focusing on robust bulk signals and efficient architectures, we show that accurate prediction of perturbation effects is possible without proprietary hardware or very large models, hence opening up ways to leverage causal learning approaches in biomedicine generally.

</details>

---

### 23. [GeoChemAD: Benchmarking Unsupervised Geochemical Anomaly Detection for Mineral Exploration](https://arxiv.org/abs/2603.13068)

**基本信息**

- 🔗 arXiv: [`2603.13068`](https://arxiv.org/abs/2603.13068)
- 👥 作者: Yihao Ding, Yiran Zhang, Chris Gonzalez 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13068.pdf)

**💡 相关性分析**

满足标准2和1：1) 数据资源相关：论文提供了一个大规模、多来源、公开的地球化学异常检测基准数据集，这是一种特定类型的化学数据集，可用于测试和开发化学信息学算法。2) 核心主题相关：论文提出的GeoChemFormer框架是针对化学数据（地球化学）进行表示学习和模式识别的深度学习方法，其技术思路可迁移至“质谱结构推理”中质谱数据的特征提取和建模。

**📖 中文摘要**

本文介绍了GeoChemAD，一个用于矿物勘探地球化学异常检测的开源基准数据集。该数据集从政府主导的地质调查中编译而成，涵盖多个区域、采样来源和目标元素，包含代表不同空间尺度和采样条件的八个子集。为了建立强基线，作者复现并基准测试了一系列无监督异常检测方法。此外，作者提出了GeoChemFormer，一个基于Transformer的框架，利用自监督预训练来学习目标元素感知的地球化学空间样本表示。大量实验表明，GeoChemFormer在所有八个子集上始终实现优异且稳健的性能，在异常检测准确性和泛化能力方面优于现有的无监督方法。所提出的数据集和框架为该方向的可重复研究和未来发展奠定了基础。该研究与“化学大模型”和“质谱结构推理”相关。首先，地球化学数据本质上是多维化学元素浓度数据，与质谱数据在数据结构上有相似性（都是高维向量）。其次，GeoChemFormer框架展示了一种针对化学数据（地球化学）进行表示学习和异常检测的有效方法，其架构和思路可以借鉴用于处理质谱数据，进行质谱异常检测或质谱特征学习。最后，该工作提供了一个公开的、多来源的化学数据集，可作为测试化学数据挖掘算法的基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Geochemical anomaly detection plays a critical role in mineral exploration as deviations from regional geochemical baselines may indicate mineralization. Existing studies suffer from two key limitations: (1) single region scenarios which limit model generalizability; (2) proprietary datasets, which makes result reproduction unattainable. In this work, we introduce \textbf{GeoChemAD}, an open-source benchmark dataset compiled from government-led geological surveys, covering multiple regions, sampling sources, and target elements. The dataset comprises eight subsets representing diverse spatial scales and sampling conditions. To establish strong baselines, we reproduce and benchmark a range of unsupervised anomaly detection methods, including statistical models, generative and transformer-based approaches. Furthermore, we propose \textbf{GeoChemFormer}, a transformer-based framework that leverages self-supervised pretraining to learn target-element-aware geochemical representations for spatial samples. Extensive experiments demonstrate that GeoChemFormer consistently achieves superior and robust performance across all eight subsets, outperforming existing unsupervised methods in both anomaly detection accuracy and generalization capability. The proposed dataset and framework provide a foundation for reproducible research and future development in this direction.

</details>

---

### 24. [SldprtNet: A Large-Scale Multimodal Dataset for CAD Generation in Language-Driven 3D Design](https://arxiv.org/abs/2603.13098)

**基本信息**

- 🔗 arXiv: [`2603.13098`](https://arxiv.org/abs/2603.13098)
- 👥 作者: Ruogu Li, Sikai Li, Yao Mu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13098.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是构建了一个大规模、多模态的3D CAD模型数据集，并提供了配套的数据处理工具和生成文本描述的方法论。这为构建化学领域的类似多模态数据集（如包含3D分子结构、质谱图像、文本描述的数据集）提供了宝贵的范例和技术参考，这类数据集是训练先进的“化学大模型”和“质谱结构推理”模型的关键资源。

**📖 中文摘要**

本文介绍了SldprtNet，一个包含超过24.2万个工业零件的大规模数据集，专为语义驱动的CAD建模、几何深度学习以及用于3D设计的 multimodal 模型训练和微调而设计。数据集提供.step和.sldprt两种格式的3D模型。为了实现参数化建模并促进数据集可扩展性，作者开发了支持工具（编码器和解码器），支持13种CAD命令，并实现3D模型与结构化文本表示之间的无损转换。此外，每个样本都配有一张由3D模型七个不同视角渲染图合并而成的复合图像。通过将此图像与编码器输出的参数化文本相结合，作者使用轻量级多模态语言模型Qwen2.5-VL-7B生成每个零件外观和功能的自然语言描述。这些描述与参数化建模脚本、渲染图像和3D模型文件完全对齐，共同构建了SldprtNet。为了评估其有效性，作者在数据集子集上对基线模型进行了微调，比较了图像加文本输入与纯文本输入的效果。结果证实了多模态数据集对于CAD生成的必要性和价值。该研究与“化学大模型”相关，因为它提供了一个大规模、多模态的3D几何数据集构建范例。在化学领域，分子和材料的3D结构至关重要。类似的数据集构建方法论（结合3D结构、图像和文本描述）可以应用于创建用于训练“化学大模型”的多模态分子数据集，例如包含3D分子结构、2D渲染图、SMILES字符串和文本描述的数据集，以增强模型对分子几何和性质的理解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce SldprtNet, a large-scale dataset comprising over 242,000 industrial parts, designed for semantic-driven CAD modeling, geometric deep learning, and the training and fine-tuning of multimodal models for 3D design. The dataset provides 3D models in both .step and .sldprt formats to support diverse training and testing. To enable parametric modeling and facilitate dataset scalability, we developed supporting tools, an encoder and a decoder, which support 13 types of CAD commands and enable lossless transformation between 3D models and a structured text representation. Additionally, each sample is paired with a composite image created by merging seven rendered views from different viewpoints of the 3D model, effectively reducing input token length and accelerating inference. By combining this image with the parameterized text output from the encoder, we employ the lightweight multimodal language model Qwen2.5-VL-7B to generate a natural language description of each part's appearance and functionality. To ensure accuracy, we manually verified and aligned the generated descriptions, rendered images, and 3D models. These descriptions, along with the parameterized modeling scripts, rendered images, and 3D model files, are fully aligned to construct SldprtNet. To assess its effectiveness, we fine-tuned baseline models on a dataset subset, comparing image-plus-text inputs with text-only inputs. Results confirm the necessity and value of multimodal datasets for CAD generation. It features carefully selected real-world industrial parts, supporting tools for scalable dataset expansion, diverse modalities, and ensured diversity in model complexity and geometric features, making it a comprehensive multimodal dataset built for semantic-driven CAD modeling and cross-modal learning.

</details>

---

### 25. [Neuron-Aware Data Selection In Instruction Tuning For Large Language Models](https://arxiv.org/abs/2603.13201)

**基本信息**

- 🔗 arXiv: [`2603.13201`](https://arxiv.org/abs/2603.13201)
- 👥 作者: Xin Chen, Junchao Wu, Shu Yang 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13201.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大型语言模型的指令微调提出一种数据选择方法，旨在高效开发模型在特定领域（可推广至化学）的能力。这直接关联到如何优化和训练面向专业领域的“化学大模型”。

**📖 中文摘要**

本文提出了NAIT，一种新颖高效的指令微调数据选择框架。NAIT通过分析指令微调数据与目标领域能力之间神经元激活模式的相似性，来评估数据对大型语言模型性能的影响。具体来说，NAIT从目标领域能力的域内数据集中捕获神经元激活模式，以构建可重用和可迁移的神经元激活特征，然后根据候选样本与目标能力预期激活特征之间的相似性来评估和选择最优样本。实验结果表明，使用NAIT从Alpaca-GPT4指令微调数据集中选择的10%子集进行训练，在各种任务上 consistently 优于依赖外部高级模型或基于不确定性特征的方法。研究还揭示了神经元激活特征在LLM不同能力间的可迁移性。这项工作为高效构建和优化用于特定领域（如化学）的大语言模型提供了数据选择策略，是“化学大模型”训练流程中的重要环节。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Instruction Tuning (IT) has been proven to be an effective approach to unlock the powerful capabilities of large language models (LLMs). Recent studies indicate that excessive IT data can degrade LLMs performance, while carefully selecting a small subset of high-quality IT data can significantly enhance their capabilities. Therefore, identifying the most efficient subset data from the IT dataset to effectively develop either specific or general abilities in LLMs has become a critical challenge. To address this, we propose a novel and efficient framework called NAIT. NAIT evaluates the impact of IT data on LLMs performance by analyzing the similarity of neuron activation patterns between the IT dataset and the target domain capability. Specifically, NAIT captures neuron activation patterns from in-domain datasets of target domain capabilities to construct reusable and transferable neuron activation features. It then evaluates and selects optimal samples based on the similarity between candidate samples and the expected activation features of the target capabilities. Experimental results show that training on the 10\% Alpaca-GPT4 IT data subset selected by NAIT consistently outperforms methods that rely on external advanced models or uncertainty-based features across various tasks. Our findings also reveal the transferability of neuron activation features across different capabilities of LLMs. In particular, IT data with more logical reasoning and programmatic features possesses strong general transferability, enabling models to develop stronger capabilities across multiple tasks, while a stable core subset of data is sufficient to consistently activate fundamental model capabilities and universally improve performance across diverse tasks.

</details>

---

### 26. [Generation of maximal snake polyominoes using a deep neural network](https://arxiv.org/abs/2603.12400)

**基本信息**

- 🔗 arXiv: [`2603.12400`](https://arxiv.org/abs/2603.12400)
- 👥 作者: Benjamin Gauthier, Alain Goupil, Fadel Toure
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12400.pdf)

**💡 相关性分析**

满足标准1：论文探索了使用深度生成模型（扩散模型）来生成复杂的组合结构（蛇形多联骨牌），这为使用生成式AI模型（如扩散模型）来生成分子或材料结构（化学大模型的核心任务之一）提供了方法论的启示和验证。

**📖 中文摘要**

本文研究了深度神经网络在生成最大蛇形多联骨牌（一种组合对象）中的应用。作者实验了一种去噪扩散模型（称为结构化像素空间扩散，SPS Diffusion），该模型从数据驱动的训练中学习生成最大蛇形多联骨牌，其中最大性和相邻约束没有被显式编码，而是被学习。研究发现，SPS Diffusion能够从小的网格泛化到更大的网格，生成在28x28方格内的有效蛇形，并在接近当前计算极限的方格上产生最大蛇形候选。尽管模型容易产生分支、循环或多个组件等错误，但结果表明扩散模型能够理解复杂的组合对象。这项研究展示了生成式AI（特别是扩散模型）在理解和生成复杂化学结构（此处以抽象的组合结构为例）方面的潜力，与探索新型“化学大模型”架构相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Maximal snake polyominoes are difficult to study numerically in large rectangles, as computing them requires the complete enumeration of all snakes for a specific grid size, which corresponds to a brute force algorithm. This technique is thus challenging to use in larger rectangles, which hinders the study of maximal snakes. Furthermore, most enumerable snakes lie in small rectangles, making it difficult to study large-scale patterns. In this paper, we investigate the contribution of a deep neural network to the generation of maximal snake polyominoes from a data-driven training, where the maximality and adjacency constraints are not encoded explicitly, but learned. To this extent, we experiment with a denoising diffusion model, which we call Structured Pixel Space Diffusion (SPS Diffusion). We find that SPS Diffusion generalizes from small grids to larger ones, generating valid snakes up to 28x28 squares and producing maximal snake candidates on squares close to the current computational limit. The model is, however, prone to errors such as branching, cycles, or multiple components. Overall, the diffusion model is promising and shows that complex combinatorial objects can be understood by deep neural networks, which is useful in their investigation.

</details>

---

### 27. [Accelerating materials discovery using foundation model based In-context active learning](https://arxiv.org/abs/2603.12567)

**基本信息**

- 🔗 arXiv: [`2603.12567`](https://arxiv.org/abs/2603.12567)
- 👥 作者: Jeffrey Hu, Rongzhi Dong, Ying Feng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用预训练的基础模型（TabPFN）作为代理来加速材料发现的主动学习过程，这直接应用了“化学大模型”的思想来解决化学信息学中的关键挑战。

**📖 中文摘要**

本文提出了一种基于基础模型的上下文主动学习（ICAL）方法，用于加速材料发现。该方法用TabPFN（一个在数百万合成任务上预训练的基于Transformer的基础模型）替代传统的高斯过程或随机森林代理模型。TabPFN通过单次前向传播执行原则性的贝叶斯推断，无需针对特定数据集重新训练，并能提供校准良好的预测不确定性。在涵盖铜合金硬度、导电性、块体金属玻璃形成能力、晶体晶格热导率等10个材料数据集的基准测试中，TabPFN在8个数据集上胜出，相对于高斯过程平均节省了52%的额外实验/评估，相对于随机森林节省了29.77%。交叉验证分析证实，TabPFN的优势源于其卓越的不确定性校准能力。这项工作展示了预训练的基础模型可以作为高效的代理模型，加速基于主动学习的材料发现，是“化学大模型”在材料科学领域的一个具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward the most promising candidates, reducing costly synthesis-and-characterization cycles. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates with complementary limitations: GP underfits complex composition--property landscapes due to rigid kernel assumptions, while RF produces unreliable uncertainty estimates in small-data regimes, precisely where most materials datasets reside (with < 500 samples). Here we propose foudaiton model based In-Context Active Learning (ICAL), replacing conventional surrogates with TabPFN, a transformer-based foundation model pre-trained on millions of synthetic tasks to meta-learn a universal prior over tabular data. TabPFN performs principled Bayesian inference in a single forward pass without dataset-specific retraining, delivering well-calibrated predictive uncertainty where GP and RF fail most severely. Benchmarked against GP and RF across 10 materials datasets spanning copper alloy hardness and electrical conductivity, bulk metallic glass-forming ability, and crystal lattice thermal conductivity, TabPFN wins on 8 out of 10 datasets, achieving a mean saving of 52\% in extra experiments/evaluations relative to GP and 29.77% relative to RF. Cross-validation analysis confirms that TabPFN's advantage stems from superior uncertainty calibration,achieving the lowest Negative Log-Likelihood and Area Under the Sparsification Error curve among all surrogates. Our work demonstrates that a pre-trained foundation model can serve as a highly effective surrogate for accelerating active learning-based materials discovery.

</details>

---

### 28. [VecMol: Vector-Field Representations for 3D Molecule Generation](https://arxiv.org/abs/2603.12734)

**基本信息**

- 🔗 arXiv: [`2603.12734`](https://arxiv.org/abs/2603.12734)
- 👥 作者: Yuchen Hua, Xingang Peng, Jianzhu Ma 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12734.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的生成式模型（VecMol）用于3D分子生成，这直接属于“化学大模型”的研究范畴，特别是专注于分子的几何结构生成。

**📖 中文摘要**

本文提出了VecMol，一个用于三维分子生成的范式转换框架。与现有方法（通常将分子表示为3D图并共同生成离散原子类型和连续原子坐标）不同，VecMol将3D分子重新构想为欧几里得空间上的连续向量场。在该表示中，向量指向附近的原子并隐式编码分子结构。向量场由神经场参数化，并使用潜在扩散模型生成，从而避免了显式的图生成，并将结构学习与离散原子实例化解耦。作者在QM9和GEOM-Drugs基准上验证了该方法的可行性。这项工作为3D分子生成提出了一种基于向量场表示的新方向，是“化学大模型”在分子生成任务上的一个创新性架构探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative modeling of three-dimensional (3D) molecules is a fundamental yet challenging problem in drug discovery and materials science. Existing approaches typically represent molecules as 3D graphs and co-generate discrete atom types with continuous atomic coordinates, leading to intrinsic learning difficulties such as heterogeneous modality entanglement and geometry-chemistry coherence constraints. We propose VecMol, a paradigm-shifting framework that reimagines molecular representation by modeling 3D molecules as continuous vector fields over Euclidean space, where vectors point toward nearby atoms and implicitly encode molecular structure. The vector field is parameterized by a neural field and generated using a latent diffusion model, avoiding explicit graph generation and decoupling structure learning from discrete atom instantiation. Experiments on the QM9 and GEOM-Drugs benchmarks validate the feasibility of this novel approach, suggesting vector-field-based representations as a promising new direction for 3D molecular generation.

</details>

---

### 29. [Clustering Astronomical Orbital Synthetic Data Using Advanced Feature Extraction and Dimensionality Reduction Techniques](https://arxiv.org/abs/2603.13177)

**基本信息**

- 🔗 arXiv: [`2603.13177`](https://arxiv.org/abs/2603.13177)
- 👥 作者: Eraldo Pereira Marinho, Nelson Callegari Junior, Fabricio Aparecido Breve 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13177.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种基于机器学习的时间序列特征提取和聚类分析流程，用于从复杂的物理系统模拟数据中推断结构（如稳定区域、共振）。这种方法论可以迁移到“质谱结构推理”中，用于从质谱时间序列数据中提取特征并推断分子结构或类别。

**📖 中文摘要**

本研究为分析土星卫星系统等大规模轨道数据集，引入了一个基于机器学习的流程，用于对约22,300个模拟卫星轨道进行聚类。该流程采用了先进的特征提取和降维技术。其关键在于使用MiniRocket，它能高效地将400个时间步转换为9,996维的特征空间，以捕捉复杂的时间模式。结合自动特征提取和降维技术，该流程能够揭示土星卫星系统中的稳定区域、共振结构和其他关键行为。这项研究通过将计算工具与传统天体力学技术相结合，为分析大规模轨道数据集提供了一种可扩展且可解释的方法论。虽然应用在天体力学，但其核心方法——使用现代机器学习（如MiniRocket）从时间序列数据中提取特征并进行聚类分析——完全适用于从质谱时间序列或分子动力学模拟轨迹中提取特征和模式，与“质谱结构推理”中从复杂数据推断结构信息的目标在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The dynamics of Saturn's satellite system offer a rich framework for studying orbital stability and resonance interactions. Traditional methods for analysing such systems, including Fourier analysis and stability metrics, struggle with the scale and complexity of modern datasets. This study introduces a machine learning-based pipeline for clustering approximately 22,300 simulated satellite orbits, addressing these challenges with advanced feature extraction and dimensionality reduction techniques. The key to this approach is using MiniRocket, which efficiently transforms 400 timesteps into a 9,996-dimensional feature space, capturing intricate temporal patterns. Additional automated feature extraction and dimensionality reduction techniques refine the data, enabling robust clustering analysis. This pipeline reveals stability regions, resonance structures, and other key behaviours in Saturn's satellite system, providing new insights into their long-term dynamical evolution. By integrating computational tools with traditional celestial mechanics techniques, this study offers a scalable and interpretable methodology for analysing large-scale orbital datasets and advancing the exploration of planetary dynamics.

</details>

---

### 30. [From Experiments to Expertise: Scientific Knowledge Consolidation for AI-Driven Computational Research](https://arxiv.org/abs/2603.13191)

**基本信息**

- 🔗 arXiv: [`2603.13191`](https://arxiv.org/abs/2603.13191)
- 👥 作者: Haonan Huang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13191.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何让AI代理在计算材料科学（可视为化学信息学的一个子领域）中积累和利用知识，这直接关联到构建能够进行复杂科学推理和学习的“化学大模型”这一主题。

**📖 中文摘要**

本文介绍了QMatSuite，一个用于AI驱动计算材料科学研究的开源平台。该平台的核心是解决当前AI驱动计算科学中一个关键缺陷：每次计算执行都是孤立的，宝贵的中间知识和见解（如哪些方法失败、跨系统的模式等）没有被积累和复用。QMatSuite通过让AI代理记录带有完整溯源的研究发现、在新计算前检索已有知识，并在专门的反思会话中纠正错误发现、将观察结果合成为跨化合物的模式，实现了知识的渐进式积累。在一个六步量子力学模拟工作流的基准测试中，积累的知识将推理开销降低了67%，并将准确性从与文献值47%的偏差提高到3%的偏差。当将学到的知识迁移到一个不熟悉的材料上时，实现了1%的偏差且零流程失败。这项工作展示了将AI执行与科学知识积累和整合相结合，对于推进计算研究至关重要，与构建能够学习和推理的“化学大模型”的研究方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While large language models (LLMs) have transformed AI agents into proficient executors of computational materials science, performing a hundred simulations does not make a researcher. What distinguishes research from routine execution is the progressive accumulation of knowledge -- learning which approaches fail, recognizing patterns across systems, and applying understanding to new problems. However, the prevailing paradigm in AI-driven computational science treats each execution in isolation, largely discarding hard-won insights between runs. Here we present QMatSuite, an open-source platform closing this gap. Agents record findings with full provenance, retrieve knowledge before new calculations, and in dedicated reflection sessions correct erroneous findings and synthesize observations into cross-compound patterns. In benchmarks on a six-step quantum-mechanical simulation workflow, accumulated knowledge reduces reasoning overhead by 67% and improves accuracy from 47% to 3% deviation from literature -- and when transferred to an unfamiliar material, achieves 1% deviation with zero pipeline failures.

</details>

---

### 31. [Denoising Diffusion Variational Inference: Diffusion Models as Expressive Variational Posteriors](https://arxiv.org/abs/2401.02739)

**基本信息**

- 🔗 arXiv: [`2401.02739`](https://arxiv.org/abs/2401.02739)
- 👥 作者: Wasu Top Piriyakulkij, Yingheng Wang, Volodymyr Kuleshov
- 📄 PDF: [下载](https://arxiv.org/pdf/2401.02739.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是推进扩散模型在概率推断中的应用，提出DDVI算法。扩散模型是构建“化学大模型”的关键技术之一，本文的工作为其提供了新的理论视角和应用范式（作为变分后验），有助于丰富化学领域生成和推断模型的方法工具箱。

**📖 中文摘要**

本文提出了去噪扩散变分推断（DDVI），一种用于潜变量模型的黑盒变分推断算法，该算法依赖扩散模型作为灵活的近似后验。具体来说，该方法引入了一类表达力强的、基于扩散的变分后验，这些后验在潜空间中进行迭代优化；并使用一种受醒眠算法启发的新型正则化证据下界来训练这些后验。该方法易于实现，与黑盒变分推断兼容，并且在深度潜变量模型的推断和学习上优于基于标准化流或对抗网络的替代后验类别。DDVI在常见基准测试以及一个生物学任务（从人类基因组推断潜在祖先）上改进了推断和学习性能。这项工作展示了扩散模型作为强大生成模型和推断工具的潜力。扩散模型是当前构建“化学大模型”（特别是生成模型）的主流架构之一，本文对其在变分推断中的应用进行了理论和方法上的推进，与利用扩散模型进行化学分子生成和性质预测的研究方向相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose denoising diffusion variational inference (DDVI), a black-box variational inference algorithm for latent variable models which relies on diffusion models as flexible approximate posteriors. Specifically, our method introduces an expressive class of diffusion-based variational posteriors that perform iterative refinement in latent space; we train these posteriors with a novel regularized evidence lower bound (ELBO) on the marginal likelihood inspired by the wake-sleep algorithm. Our method is easy to implement (it fits a regularized extension of the ELBO), is compatible with black-box variational inference, and outperforms alternative classes of approximate posteriors based on normalizing flows or adversarial networks. We find that DDVI improves inference and learning in deep latent variable models across common benchmarks as well as on a motivating task in biology -- inferring latent ancestry from human genomes -- where it outperforms strong baselines on the Thousand Genomes dataset.

</details>

---

### 32. [A DNN Biophysics Model with Topological and Electrostatic Features](https://arxiv.org/abs/2409.03658)

**基本信息**

- 🔗 arXiv: [`2409.03658`](https://arxiv.org/abs/2409.03658)
- 👥 作者: Elyssa Sliheet, Md Abu Talha, Weihua Geng
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.03658.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种结合拓扑和静电特征的深度神经网络模型，用于预测蛋白质的物理化学性质（如库仑能）。该方法利用持久同调等计算化学工具生成统一的多尺度特征，这些特征和模型框架本身可以作为化学信息学领域（特别是分子性质预测和结构-性质关系建模）的有价值的数据处理工具和资源，与‘化学大模型’主题中利用AI模型处理化学结构信息的研究方向相关。

**📖 中文摘要**

本文提出了一种基于深度神经网络（DNN）的生物物理模型，用于预测蛋白质性质（如库仑能或溶剂化能）。该模型利用多尺度和统一的拓扑与静电特征。拓扑特征通过对重原子或碳原子使用元素特异性持久同调（ESPH）生成。静电特征则使用一种新颖的笛卡尔树码生成，以添加底层静电相互作用来进一步改进模型预测。这些特征对于不同大小的蛋白质在数量上是统一的，因此可以利用广泛可用的蛋白质结构数据库来训练网络。这些特征也是多尺度的，允许用户在分辨率和计算成本之间进行权衡。该模型在超过17,000个蛋白质上训练以预测库仑能，取得了优异的预测性能。特征生成算法有潜力作为辅助基于机器学习的蛋白质性质和功能预测的通用工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this project, we present a deep neural network (DNN)-based biophysics model that uses multi-scale and uniform topological and electrostatic features to predict protein properties, such as Coulomb energies or solvation energies. The topological features are generated using element-specific persistent homology (ESPH) on a selection of heavy atoms or carbon atoms. The electrostatic features are generated using a novel Cartesian treecode, which adds underlying electrostatic interactions to further improve the model prediction. These features are uniform in number for proteins of varying sizes; therefore, the widely available protein structure databases can be used to train the network. These features are also multi-scale, allowing users to balance resolution and computational cost. The optimal model trained on more than 17,000 proteins for predicting Coulomb energy achieves MSE of approximately 0.024, MAPE of 0.073 and $R^2$ of 0.976. Meanwhile, the optimal model trained on more than 4,000 proteins for predicting solvation energy achieves MSE of approximately 0.064, MAPE of 0.081, and $R^2$ of 0.926, showing the efficiency and fidelity of these features in representing the protein structure and force field. The feature generation algorithms also have the potential to serve as general tools for assisting machine learning based prediction of protein properties and functions.

</details>

---

### 33. [3DGS-DET: Empower 3D Gaussian Splatting with Boundary Guidance and Box-Focused Sampling for Indoor 3D Object Detection](https://arxiv.org/abs/2410.01647)

**基本信息**

- 🔗 arXiv: [`2410.01647`](https://arxiv.org/abs/2410.01647)
- 👥 作者: Yang Cao, Yuanliang Ju, Dan Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.01647.pdf)

**💡 相关性分析**

满足标准2：论文的核心是开发一种新的3D表示（3D高斯泼溅）和相应的优化策略（边界引导、盒聚焦采样）用于3D场景理解和物体检测。虽然应用场景是计算机视觉，但其核心技术创新——一种新的、可微分的显式3D场景表示和重建方法——在原理上与化学信息学和质谱分析中处理3D分子结构、点云数据或光谱成像数据有潜在的相通之处。该方法作为一种新的‘数据表示与处理工具’，可能为相关领域（如分子3D构象生成、质谱成像的空间解析）提供思路或可借鉴的技术资源。

**📖 中文摘要**

本文提出了3DGS-DET，首次将3D高斯泼溅（3DGS）引入室内3D物体检测（3DOD）。3DGS是一种显式的3D表示方法，解决了神经辐射场（NeRF）等隐式表示的局限性。论文解决了两个主要挑战：（i）高斯斑点空间分布模糊，以及（ii）过多的背景斑点。为了解决（i），论文提出利用2D边界引导来显著增强高斯斑点的空间分布，从而更清晰地区分物体和背景。为了解决（ii），论文提出了一种使用2D边界框的盒聚焦采样策略，在3D空间中生成物体概率分布，从而在3D中进行有效的概率采样，保留更多物体斑点并减少噪声背景斑点。得益于这些创新，3DGS-DET在ScanNet和ARKITScenes等数据集上显著优于最先进的基于NeRF的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Radiance Fields (NeRF) have been adapted for indoor 3D Object Detection (3DOD), offering a promising approach to indoor 3DOD via view-synthesis representation. But its implicit nature limits representational capacity. Recently, 3D Gaussian Splatting (3DGS) has emerged as an explicit 3D representation that addresses the limitation. This work introduces 3DGS into indoor 3DOD for the first time, identifying two main challenges: (i) Ambiguous spatial distribution of Gaussian blobs -- 3DGS primarily relies on 2D pixel-level supervision, resulting in unclear 3D spatial distribution of Gaussian blobs and poor differentiation between objects and background, which hinders indoor 3DOD; (ii) Excessive background blobs -- 2D images typically include numerous background pixels, leading to densely reconstructed 3DGS with many noisy Gaussian blobs representing the background, negatively affecting detection. To tackle (i), we leverage the fact that 3DGS reconstruction is derived from 2D images, and propose an elegant solution by incorporating 2D Boundary Guidance to significantly enhance the spatial distribution of Gaussian blobs, resulting in clearer differentiation between objects and their background (please see fig:teaser). To address (ii), we propose a Box-Focused Sampling strategy using 2D boxes to generate object probability distribution in 3D space, allowing effective probabilistic sampling in 3D to retain more object blobs and reduce noisy background blobs. Benefiting from these innovations, 3DGS-DET significantly outperforms the state-of-the-art NeRF-based method, NeRF-Det++, achieving improvements of +6.0 on mAP@0.25 and +7.8 on mAP@0.5 for the ScanNet, and the +14.9 on mAP@0.25 for the ARKITScenes.

</details>

---

### 34. [RadField3D: A Data Generator and Data Format for Deep Learning in Radiation-Protection Dosimetry for Medical Applications](https://arxiv.org/abs/2412.13852)

**基本信息**

- 🔗 arXiv: [`2412.13852`](https://arxiv.org/abs/2412.13852)
- 👥 作者: Felix Lehner, Pasquale Lombardo, Susana Castillo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.13852.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是开发了一个用于生成三维辐射场数据集的模拟工具（RadField3D）以及配套的、便于机器学习研究的数据格式和API。这直接提供了可用于机器学习模型训练的数据集生成工具和资源。虽然应用领域是辐射防护剂量测定，但其‘为深度学习研究生成专用数据集并提供易用接口’的模式，与化学信息学和质谱分析中构建用于‘化学大模型’或‘质谱结构推理’的专用模拟或实验数据生成管道高度相关，可作为方法论参考。

**📖 中文摘要**

本研究介绍了RadField3D，一个基于Geant4的开源蒙特卡洛模拟应用程序，用于生成三维辐射场数据集以进行剂量测定。同时，论文引入了一种快速的、机器可解释的数据格式及其Python API，以便于集成到神经网络研究中。这两项开发旨在用于研究使用深度学习的替代辐射模拟方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this research work, we present our open-source Geant4-based Monte-Carlo simulation application, called RadField3D, for generating threedimensional radiation field datasets for dosimetry. Accompanying, we introduce a fast, machine-interpretable data format with a Python API for easy integration into neural network research, that we call RadFiled3D. Both developments are intended to be used to research alternative radiation simulation methods using deep learning.

</details>

---

### 35. [Unsupervised anomaly detection in MeV ultrafast electron diffraction](https://arxiv.org/abs/2505.13702)

**基本信息**

- 🔗 arXiv: [`2505.13702`](https://arxiv.org/abs/2505.13702)
- 👥 作者: Mariana A. Fazio, Manel Martinez-Ramon, Salvador Sosa Güitron 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13702.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于自编码器的无监督异常检测方法，专门用于处理质谱分析相关技术（超快电子衍射，MUED）产生的大型数据集中的噪声和异常数据。该方法的核心是提高衍射数据（一种结构分析数据）的质量和可靠性，这直接关系到后续结构推理的准确性。因此，该论文提供了一种可用于‘质谱结构推理’或类似光谱/衍射数据分析流程前期（数据清洗和质量控制）的具体工具和方法，属于数据预处理资源。

**📖 中文摘要**

本文针对MeV超快电子衍射（MUED）技术中，由于电子束不稳定性导致的异常衍射图案问题，开发了一种完全无监督的异常检测方法。该方法使用卷积自编码器计算衍射图案的重构均方误差，并基于该误差的统计分析，为用户提供图案正常的概率估计，从而允许对难以分类的图像进行后验视觉检查。该方法仅用100个衍射图案进行训练，在1521个测试图案上实现了低至0.2%-0.4%的误报率。所提出的方法也可应用于其他因仪器不稳定性而包含故障图像的大型数据集的衍射技术中。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MeV ultrafast electron diffraction (MUED) is a pump-probe technique used to study the dynamic structural evolution of materials. An ultrashort laser pulse triggers structural changes, which are then probed by an ultrashort relativistic electron beam. To overcome low signal-to-noise ratios, diffraction patterns are averaged over thousands of shots. However, shot-to-shot instabilities in the electron beam can distort individual patterns, introducing uncertainty. Improving MUED accuracy requires detecting and removing these anomalous patterns from large datasets. In this work, we developed a fully unsupervised methodology for the detection of anomalous diffraction patterns. Using a convolutional autoencoder, we calculate the reconstruction mean squared error of the diffraction patterns. Based on the statistical analysis of this error, we provide the user an estimation of the probability that the pattern is normal, which also allows a posterior visual inspection of the images that are difficult to classify. This method has been trained with only 100 diffraction patterns and tested on 1521 patterns, resulting in a false positive rate between 0.2\% and 0.4\%, with a training time of 10 seconds per image and a test time of about 1 second per image. The proposed methodology can also be applied to other diffraction techniques in which large datasets are collected that include faulty images due to instrumental instabilities.

</details>

---

### 36. [Extended Low-Rank Approximation Accelerates Learning of Elastic Response in Heterogeneous Materials](https://arxiv.org/abs/2509.20276)

**基本信息**

- 🔗 arXiv: [`2509.20276`](https://arxiv.org/abs/2509.20276)
- 👥 作者: Prabhat Karmakar, Sayan Gupta, Ilaksh Adlakha
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.20276.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为xLRA的框架，利用张量分解和低秩近似技术，高效建立从高维微观结构特征到材料性能（弹性响应）的映射。这种方法的核心是发展一种高效、数据需求量小的‘结构-性质’关系建模工具。这在化学信息学中与‘化学大模型’的目标高度一致，即学习分子结构（微观结构）与其性质/功能之间的复杂映射关系。xLRA所展示的数据效率、可迁移性和对高维特征的处理能力，为化学领域类似问题的建模提供了有价值的技术思路和潜在工具。

**📖 中文摘要**

本文提出了扩展低秩近似（xLRA）框架，该框架采用规范多元张量分解，通过自适应地纳入更高秩项，将高维微观结构信息高效地映射到局部弹性响应。xLRA能够准确预测多孔微结构中的局部弹性应变场，仅需最大秩为4。xLRA的紧凑公式使其在仅使用5%数据集训练时就能实现准确预测，展示了显著的数据效率。此外，xLRA证明了其可迁移性，能够在包括两相复合材料以及单相和双相多晶在内的代表性材料系统中提供结果。尽管结构紧凑，xLRA保留了必要的微观结构细节，从而能够对未见过的微观结构进行准确预测。基准测试表明，xLRA在预测准确性、泛化能力和计算效率方面优于当代方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting how the microstructure governs the mechanical response of heterogeneous materials is essential for optimizing design and performance. Yet this task remains difficult due to the complex, high dimensional nature of microstructural features. Relying on physics based simulations to probe the microstructural space is computationally prohibitive. This motivates the development of computational tools to efficiently learn structure property linkages governing mechanical behavior. While contemporary data driven approaches offer new possibilities, they often require large datasets. To address this challenge, this work presents the Extended Low Rank Approximation (xLRA), a framework that employs canonical polyadic tensor decomposition. It efficiently maps high dimensional microstructural information to the local elastic response by adaptively incorporating higher rank terms. xLRA accurately predicts the local elastic strain fields in porous microstructures, requiring a maximum rank of only 4. The compact formulation of xLRA achieves accurate predictions when trained on just 5% of the dataset, demonstrating significant data efficiency. Moreover, xLRA proves transferability by delivering results across representative material systems, including two phase composites and single and dual phase polycrystals. Despite being compact, xLRA retains essential microstructural details, enabling accurate predictions on unseen microstructures. Benchmarking shows that xLRA outperforms contemporary methods in predictive accuracy, generalizability, and computational efficiency, while requiring 6 orders of magnitude fewer floating point operations. In summary, xLRA provides an efficient framework for predicting the elastic response from microstructures, enabling scalable mapping of structure property linkages.

</details>

---

### 37. [LiLAW: Lightweight Learnable Adaptive Weighting to Meta-Learn Sample Difficulty, Improve Noisy Training, Increase Fairness, and Effectively Use Synthetic Data](https://arxiv.org/abs/2509.20786)

**基本信息**

- 🔗 arXiv: [`2509.20786`](https://arxiv.org/abs/2509.20786)
- 👥 作者: Abhishek Moturu, Muhammad Muzammil, Anna Goldenberg 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.20786.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种通用的训练策略（LiLAW），用于动态调整样本权重以处理噪声数据、提高数据利用效率和模型鲁棒性。该方法的普适性意味着它可以被应用于化学信息学和质谱分析领域，用于训练更稳健的‘化学大模型’或质谱分类/回归模型，特别是在处理带有噪声、不平衡或存在合成数据的化学数据集时。因此，它提供了一种可用于改进相关主题下模型训练过程的算法工具。

**📖 中文摘要**

本文介绍了轻量级可学习自适应加权（LiLAW）方法，该方法根据每个训练样本不断演变的难度（分为简单、中等、困难）动态调整其损失权重。LiLAW仅使用三个可学习参数，通过在每个训练小批量之后在验证小批量上执行单个梯度下降步骤来更新这些参数，从而在训练过程中自适应地优先处理信息丰富的样本。实验跨越多个通用和医学成像数据集、噪声水平/类型、损失函数和架构（带或不带预训练）表明，LiLAW即使在高噪声环境中也有效，且无需大量调参。LiLAW还被应用于两个最近引入的合成数据集：SynPAIN（用于自动疼痛检测的合成面部表情）和GAITGen（用于帕金森病严重程度估计的合成步态序列）。LiLAW在这些数据集上获得了最先进的结果。此外，LiLAW在Adult数据集上显示出改进的公平性。LiLAW提供了一种计算高效的解决方案，可在任何神经网络训练设置中提高泛化性和鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training deep neural networks with noise and data heterogeneity is a major challenge. We introduce Lightweight Learnable Adaptive Weighting (LiLAW), a method that dynamically adjusts the loss weight of each training sample based on its evolving difficulty, categorized as easy, moderate, or hard. Using only three learnable parameters, LiLAW adaptively prioritizes informative samples during training by updating these parameters using a single gradient descent step on a validation mini-batch after each training mini-batch. Experiments across multiple general and medical imaging datasets, noise levels/types, loss functions, and architectures with and without pretraining (with linear probing and full fine-tuning) demonstrate that LiLAW's effectiveness, even in high-noise environments, without excessive tuning. We also apply LiLAW to two recently introduced synthetic datasets: SynPAIN (synthetic facial expressions for automated pain detection) and GAITGen (synthetic gait sequences for Parkinson's disease severity estimation). We also validate on ECG5000, a time-series dataset for heartbeat classification, with simple augmentations. We obtain state-of-the-art results on these three datasets. We then use LiLAW on the Adult dataset to show improved fairness. LiLAW is effective without heavy reliance on advanced training techniques or data augmentations, highlighting its practicality, esp. in resource-constrained settings. It offers a computationally efficient solution to boost generalization and robustness in any neural network training setup.

</details>

---

### 38. [From Formal Language Theory to Statistical Learning: Finite Observability of Subregular Languages](https://arxiv.org/abs/2509.22598)

**基本信息**

- 🔗 arXiv: [`2509.22598`](https://arxiv.org/abs/2509.22598)
- 👥 作者: Katsuhiko Hayashi, Hidetaka Kamigaito
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.22598.pdf)

**💡 相关性分析**

满足标准2：论文从形式语言理论出发，研究了次正则语言类的线性可分性和可学习性，并通过英语形态学实验进行了验证。虽然主题是自然语言，但其核心贡献——为特定结构类别（次正则语言）建立可学习性理论并展示与语言学约束的对齐——为‘化学大模型’中处理具有特定语法或结构规则的化学语言（如SMILES字符串、分子图、质谱碎片模式）提供了理论框架和方法论启示。该研究展示了如何将形式语言理论应用于结构数据的机器学习，这与化学信息学中利用语言模型处理分子序列或利用图模型处理分子结构的思路相关。

**📖 中文摘要**

本文证明了所有标准的次正则语言类在由其判定谓词表示时都是线性可分的。这确立了有限可观察性，并保证了使用简单线性模型的可学习性。合成实验证实了在无噪声条件下的完美可分性，而对英语形态学的真实数据实验表明，学习到的特征与已知的语言学约束相一致。这些结果表明，次正则层级为建模自然语言结构提供了一个严谨且可解释的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We prove that all standard subregular language classes are linearly separable when represented by their deciding predicates. This establishes finite observability and guarantees learnability with simple linear models. Synthetic experiments confirm perfect separability under noise-free conditions, while real-data experiments on English morphology show that learned features align with well-known linguistic constraints. These results demonstrate that the subregular hierarchy provides a rigorous and interpretable foundation for modeling natural language structure. Our code used in real-data experiments is available at this https URL .

</details>

---

### 39. [ASTGI: Adaptive Spatio-Temporal Graph Interactions for Irregular Multivariate Time Series Forecasting](https://arxiv.org/abs/2509.23313)

**基本信息**

- 🔗 arXiv: [`2509.23313`](https://arxiv.org/abs/2509.23313)
- 👥 作者: Xvyuan Liu, Xiangfei Qiu, Hanyin Cheng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23313.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于处理不规则多元时间序列的新型图神经网络框架（ASTGI）。虽然应用场景是通用时间序列预测，但其核心技术——将不规则采样点嵌入到连续时空空间，并构建自适应图进行信息传播——与质谱分析中处理随时间或扫描索引变化的质谱信号（如LC-MS数据）、或化学信息学中处理分子动力学轨迹等不规则采样序列高度相关。该框架为这些领域处理类似结构的数据提供了新的建模工具和思路。

**📖 中文摘要**

本文针对不规则多元时间序列（IMTS）预测提出了自适应时空图交互（ASTGI）框架。该框架首先使用时空点表示模块将每个离散观测编码为可学习时空嵌入空间中的一个点。其次，邻域自适应图构建模块通过最近邻搜索为嵌入空间中的每个点自适应地构建因果图。随后，时空动态传播模块通过基于点之间相对时空位置生成消息和计算交互权重，在这些自适应因果图上迭代更新信息。最后，基于查询点的预测模块通过聚合新查询点的邻域信息并执行预测来生成最终预测。在多个基准数据集上的大量实验表明，ASTGI优于各种最先进的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Irregular multivariate time series (IMTS) are prevalent in critical domains like healthcare and finance, where accurate forecasting is vital for proactive decision-making. However, the asynchronous sampling and irregular intervals inherent to IMTS pose two core challenges for existing methods: (1) how to accurately represent the raw information of irregular time series without introducing data distortion, and (2) how to effectively capture the complex dynamic dependencies between observation points. To address these challenges, we propose the Adaptive Spatio-Temporal Graph Interaction (ASTGI) framework. Specifically, the framework first employs a Spatio-Temporal Point Representation module to encode each discrete observation as a point within a learnable spatio-temporal embedding space. Second, a Neighborhood-Adaptive Graph Construction module adaptively builds a causal graph for each point in the embedding space via nearest neighbor search. Subsequently, a Spatio-Temporal Dynamic Propagation module iteratively updates information on these adaptive causal graphs by generating messages and computing interaction weights based on the relative spatio-temporal positions between points. Finally, a Query Point-based Prediction module generates the final forecast by aggregating neighborhood information for a new query point and performing forecasting. Extensive experiments on multiple benchmark datasets demonstrate that ASTGI outperforms various state-of-the-art methods.

</details>

---

### 40. [Robust Fine-Tuning from Non-Robust Pretrained Models: Mitigating Suboptimal Transfer With Epsilon-Scheduling](https://arxiv.org/abs/2509.23325)

**基本信息**

- 🔗 arXiv: [`2509.23325`](https://arxiv.org/abs/2509.23325)
- 👥 作者: Jonas Ngnawé, Maxime Heuillet, Sabyasachi Sahoo 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23325.pdf)

**💡 相关性分析**

满足标准2：论文深入研究了鲁棒微调这一重要机器学习实践，并针对从非鲁棒预训练模型出发的挑战提出了有效的解决方案（Epsilon调度）和评估指标（期望鲁棒性）。‘化学大模型’和‘质谱结构推理’模型通常基于大规模预训练模型进行领域适配或微调。该论文提供的关于如何在进行对抗性训练或鲁棒性优化时避免损害模型原有知识迁移的见解和方法，对于开发更稳健、泛化能力更强的化学AI模型具有直接的参考价值，属于提升模型训练质量的工具性研究。

**📖 中文摘要**

本文系统地研究了从非鲁棒预训练模型进行鲁棒微调（RFT）。实验发现，使用鲁棒目标对非鲁棒模型进行微调，即使在小扰动下，也可能导致性能不佳，作者将这种现象称为次优迁移。在具有挑战性的场景中，最终性能可能低到可被视为迁移失败。作者发现，使用鲁棒目标进行微调会在训练开始时阻碍任务适应，并最终阻止最优迁移。为此，作者提出了一种新颖的启发式方法——Epsilon调度，即在训练期间对扰动强度进行调度，以促进最优迁移。此外，作者引入了期望鲁棒性这一指标，用于更全面地评估模型在测试时在不同扰动下的准确性与鲁棒性权衡。大量实验表明，Epsilon调度成功防止了次优迁移，并持续提高了期望鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fine-tuning pretrained models is a standard and effective workflow in modern machine learning. However, robust fine-tuning (RFT), which aims to simultaneously achieve adaptation to a downstream task and robustness to adversarial examples, remains challenging. Despite the abundance of non-robust pretrained models in open-source repositories, their potential for RFT is less understood. We address this knowledge gap by systematically examining RFT from such non-robust models. Our experiments reveal that fine-tuning non-robust models with a robust objective, even under small perturbations, can lead to poor performance, a phenomenon that we dub suboptimal transfer. In challenging scenarios (eg, difficult tasks, high perturbation), the resulting performance can be so low that it may be considered a transfer failure. We find that fine-tuning using a robust objective impedes task adaptation at the beginning of training and eventually prevents optimal transfer. However, we propose a novel heuristic, Epsilon-Scheduling, a schedule over perturbation strength used during training that promotes optimal transfer. Additionally, we introduce expected robustness, a metric that captures performance across a range of perturbations, providing a more comprehensive evaluation of the accuracy-robustness trade-off for diverse models at test time. Extensive experiments on a wide range of configurations (six pretrained models and five datasets) show that Epsilon-Scheduling successfully prevents suboptimal transfer and consistently improves expected robustness.

</details>

---

### 41. [SPELL: Self-Play Reinforcement Learning for Evolving Long-Context Language Models](https://arxiv.org/abs/2509.23863)

**基本信息**

- 🔗 arXiv: [`2509.23863`](https://arxiv.org/abs/2509.23863)
- 👥 作者: Ziyi Yang, Weizhou Shen, Chenliang Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23863.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为SPELL的创新框架，通过自博弈强化学习自动生成训练数据和奖励信号，以优化大语言模型的长上下文推理能力。这种方法减少了对人工标注数据的依赖，并实现了模型的自我迭代改进。该框架作为一种先进的‘模型训练与优化工具’，其核心思想（自动课程、自博弈、多角色交互）对于训练需要处理长序列、复杂推理的‘化学大模型’（如处理长文献、复杂反应路径或大型分子数据库）具有重要的方法论参考价值，提供了构建更智能、自适应化学AI系统的潜在技术路径。

**📖 中文摘要**

本文提出了SPELL，一个多角色自博弈强化学习框架，用于实现可扩展的、无标签的长上下文推理优化。SPELL在单个模型中整合了三个循环角色——提问者、回答者和验证者——以实现持续的自我改进。提问者从带有参考答案的原始文档中生成问题；回答者学习基于文档解决这些问题；验证者评估回答者输出与提问者参考答案之间的语义等价性，产生奖励信号以指导持续训练。为了稳定训练，作者引入了自动课程，逐渐增加文档长度，并采用了一种使问题难度适应模型演化能力的奖励函数。在六个长上下文基准测试上的大量实验表明，SPELL持续提升了不同LLMs的性能，并且优于在大型标注数据上微调的同规模模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Progress in long-context reasoning for large language models (LLMs) has lagged behind other recent advances. This gap arises not only from the intrinsic difficulty of processing long texts, but also from the scarcity of reliable human annotations and programmatically verifiable reward signals. In this paper, we propose SPELL, a multi-role self-play reinforcement learning framework that enables scalable, label-free optimization for long-context reasoning. SPELL integrates three cyclical roles-questioner, responder, and verifier-within a single model to enable continual self-improvement. The questioner generates questions from raw documents paired with reference answers; the responder learns to solve these questions based on the documents; and the verifier evaluates semantic equivalence between the responder's output and the questioner's reference answer, producing reward signals to guide continual training. To stabilize training, we introduce an automated curriculum that gradually increases document length and a reward function that adapts question difficulty to the model's evolving capabilities. Extensive experiments on six long-context benchmarks show that SPELL consistently improves performance across diverse LLMs and outperforms equally sized models fine-tuned on large-scale annotated data. Notably, SPELL achieves an average 7.6-point gain in pass@8 on the strong reasoning model Qwen3-30B-A3B-Thinking, raising its performance ceiling and showing promise for scaling to even more capable models. Our code is available at this https URL .

</details>

---

### 42. [Uni-Parser Technical Report](https://arxiv.org/abs/2512.15098)

**基本信息**

- 🔗 arXiv: [`2512.15098`](https://arxiv.org/abs/2512.15098)
- 👥 作者: Xi Fang, Haoyi Tao, Shuwen Yang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15098.pdf)

**💡 相关性分析**

满足标准2：论文提出的Uni-Parser工具能够从科学文献中高效提取化学结构、反应方案和生物活性数据，为化学大模型的训练提供了关键的数据集和资源。

**📖 中文摘要**

本文介绍了Uni-Parser，一个面向科学文献和专利的工业级文档解析引擎。其核心是一个模块化、松散耦合的多专家架构，能够跨文本、方程、表格、图形和化学结构等模态保持细粒度的跨模态对齐。该系统针对大规模云部署进行了优化，支持整体或特定模态的解析。对于化学信息学领域，该工具能够从科学文献中高效、准确地提取化学结构、反应方案和生物活性数据，这对于构建用于训练下一代化学大模型（如AI4Science模型）的大规模语料库至关重要。因此，它直接为化学大模型的研究提供了高质量的数据资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This technical report introduces Uni-Parser, an industrial-grade document parsing engine tailored for scientific literature and patents, delivering high throughput, robust accuracy, and cost efficiency. Unlike pipeline-based document parsing methods, Uni-Parser employs a modular, loosely coupled multi-expert architecture that preserves fine-grained cross-modal alignments across text, equations, tables, figures, and chemical structures, while remaining easily extensible to emerging modalities. The system incorporates adaptive GPU load balancing, distributed inference, dynamic module orchestration, and configurable modes that support either holistic or modality-specific parsing. Optimized for large-scale cloud deployment, Uni-Parser achieves a processing rate of up to 20 PDF pages per second on 8 x NVIDIA RTX 4090D GPUs, enabling cost-efficient inference across billions of pages. This level of scalability facilitates a broad spectrum of downstream applications, ranging from literature retrieval and summarization to the extraction of chemical structures, reaction schemes, and bioactivity data, as well as the curation of large-scale corpora for training next-generation large language models and AI4Science models.

</details>

---

### 43. [Development of Ontological Knowledge Bases by Leveraging Large Language Models](https://arxiv.org/abs/2601.10436)

**基本信息**

- 🔗 arXiv: [`2601.10436`](https://arxiv.org/abs/2601.10436)
- 👥 作者: Le Ngoc Luyen, Marie-Hélène Abel, Philippe Gouspillou
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.10436.pdf)

**💡 相关性分析**

满足标准2：论文提出的LLM驱动本体开发框架，为构建化学领域知识库（一种关键的数据/知识资源）提供了高效的方法论，这些资源是化学大模型进行知识推理和结构理解的基础。

**📖 中文摘要**

本文提出了一种利用大型语言模型（LLMs）开发和优化本体知识库（OKBs）的结构化、迭代方法。该方法通过LLMs自动化知识获取和本体构件生成，显著加速了本体构建过程，并提高了本体的一致性和可扩展性。论文通过一个车辆销售领域的用户上下文配置文件本体的案例研究进行了演示。在化学信息学背景下，本体是组织和表示化学知识（如化合物、反应、性质）的核心工具。本文提出的LLM驱动框架为高效构建和维护化学领域本体提供了方法论，这对于为化学大模型提供结构化、可推理的知识基础至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ontological Knowledge Bases (OKBs) play a vital role in structuring domain-specific knowledge and serve as a foundation for effective knowledge management systems. However, their traditional manual development poses significant challenges related to scalability, consistency, and adaptability. Recent advancements in Generative AI, particularly Large Language Models (LLMs), offer promising solutions for automating and enhancing OKB development. This paper introduces a structured, iterative methodology leveraging LLMs to optimize knowledge acquisition, automate ontology artifact generation, and enable continuous refinement cycles. We demonstrate this approach through a detailed case study focused on developing a user context profile ontology within the vehicle sales domain. Key contributions include significantly accelerated ontology construction processes, improved ontological consistency, effective bias mitigation, and enhanced transparency in the ontology engineering process. Our findings highlight the transformative potential of integrating LLMs into ontology development, notably improving scalability, integration capabilities, and overall efficiency in knowledge management systems.

</details>

---

### 44. [Expert Selections In MoE Models Reveal (Almost) As Much As Text](https://arxiv.org/abs/2602.04105)

**基本信息**

- 🔗 arXiv: [`2602.04105`](https://arxiv.org/abs/2602.04105)
- 👥 作者: Amir Nuriyev, Gabriel Kulp
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.04105.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕混合专家（MoE）模型展开，而MoE架构是构建和扩展化学大模型的关键技术之一。论文揭示了该架构的安全特性，与构建可靠化学大模型的研究直接相关。

**📖 中文摘要**

本文提出了一种针对混合专家（MoE）语言模型的文本重建攻击，仅通过分析模型为每个令牌选择的路由决策（即选择了哪些专家子网络）就能恢复原始文本。研究表明，MoE模型中的路由决策会泄露大量信息，使用基于Transformer的序列解码器可以在训练后以高准确率重建令牌序列。这项研究揭示了MoE模型在分布式推理等场景下的潜在安全风险。虽然论文主题是模型安全，但其核心研究对象——MoE架构——是构建大规模、高效化学大模型（例如，用于处理分子图、序列或光谱数据）的潜在关键技术路径之一。理解MoE模型的信息泄露机制对于设计安全可靠的化学领域大模型具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a text-reconstruction attack on mixture-of-experts (MoE) language models that recovers tokens from expert selections alone. In MoE models, each token is routed to a subset of expert subnetworks; we show these routing decisions leak substantially more information than previously understood. Prior work using logistic regression achieves limited reconstruction; we show that a 3-layer MLP improves this to 63.1% top-1 accuracy, and that a transformer-based sequence decoder recovers 91.2% of tokens top-1 (94.8% top-10) on 32-token sequences from OpenWebText after training on 100M tokens. These results connect MoE routing to the broader literature on embedding inversion. We outline practical leakage scenarios (e.g., distributed inference and side channels) and show that adding noise reduces but does not eliminate reconstruction. Our findings suggest that expert selections in MoE deployments should be treated as sensitive as the underlying text.

</details>

---

### 45. [On the Geometric Coherence of Global Aggregation in Federated Graph Neural Networks](https://arxiv.org/abs/2602.15510)

**基本信息**

- 🔗 arXiv: [`2602.15510`](https://arxiv.org/abs/2602.15510)
- 👥 作者: Chethana Prasad Kabgere, Shylaja SS
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.15510.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕图神经网络在异构数据上的稳健聚合与推理，这与构建需要处理分布式、多样化化学数据的化学大模型所面临的核心挑战直接相关。

**📖 中文摘要**

本文研究了联邦图神经网络（GNN）中全局聚合的几何一致性。作者指出，在跨域联邦GNN设置中，客户端图通常表现出异构的结构和传播特性。当标准的聚合机制应用于这些异构更新时，全局模型可能在数值上收敛，但其关系行为会退化。本文识别了全局聚合在跨域联邦GNN中的一种几何失效模式。GNN参数在数值上表示为向量，但它们编码了控制图邻域信息流方向、强度和敏感性的关系变换。聚合来自不兼容传播机制的更新可能会在变换空间中引入破坏性干扰，导致全局消息传递的一致性丧失。为了解决这个问题，作者提出了GGRS（全局几何参考结构），这是一个服务器端框架，基于几何可容许性标准在聚合前调节客户端更新。GGRS保持了关系变换的方向一致性，并维持了可容许传播子空间的多样性。

**与关注主题的相关性**：虽然论文主要关注联邦学习和图神经网络，但其核心是处理图结构数据上的关系推理和模型聚合。图神经网络是化学信息学中用于分子性质预测和结构表示的关键工具。本文提出的几何一致性问题和解决方案，对于构建在分布式、异构化学数据（如不同实验室的质谱或分子结构数据）上训练的稳健化学大模型具有重要启示。它满足了标准1（核心主题相关），因为其关于图神经网络在异构数据上稳健推理的讨论，直接关联到构建能够处理多样化、分布式化学数据的“化学大模型”所面临的挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Federated Learning (FL) enables distributed training across multiple clients without centralized data sharing, while Graph Neural Networks (GNNs) model relational data through message passing. In federated GNN settings, client graphs often exhibit heterogeneous structural and propagation characteristics. When standard aggregation mechanisms are applied to such heterogeneous updates, the global model may converge numerically while exhibiting degraded relational behavior. Our work identifies a geometric failure mode of global aggregation in Cross- Domain Federated GNNs. Although GNN parameters are numerically represented as vectors, they encode relational transformations that govern the direction, strength, and sensitivity of information flow across graph neighborhoods. Aggregating updates originating from incompatible propagation regimes can therefore introduce destructive interference in this transformation space. This leads to loss of coherence in global message passing. Importantly, this degradation is not necessarily reflected in conventional metrics such as loss or accuracy. To address this issue, we propose GGRS (Global Geometric Reference Structure), a server-side framework that regulates client updates prior to aggregation based on geometric admissibility criteria. GGRS preserves directional consistency of relational transformations as well as maintains diversity of admissible propagation subspaces. It also stabilizes sensitivity to neighborhood interactions, without accessing client data or graph topology. Experiments on heterogeneous GNN-native, Amazon Co-purchase datasets demonstrate that GGRS preserves global message-passing coherence across training rounds by highlighting the necessity of geometry-aware regulation in federated graph learning.

</details>

---

### 46. [Which Data Matter? Embedding-Based Data Selection for Speech Recognition](https://arxiv.org/abs/2603.05819)

**基本信息**

- 🔗 arXiv: [`2603.05819`](https://arxiv.org/abs/2603.05819)
- 👥 作者: Zakaria Aldeneh, Skyler Seto, Maureen de Seyssel 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05819.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于嵌入表示的目标数据选择框架，该方法论和工具思路可直接应用于为化学大模型或质谱结构推理模型从海量化学数据中筛选和构建高质量、领域特定的训练数据集。

**📖 中文摘要**

本文研究了针对特定领域的自动语音识别（ASR）系统的数据选择策略。现代ASR系统通常在包含多个领域的大规模伪标记、野外数据上进行训练。虽然这种异构数据有利于为广泛部署设计的通用模型，但对于针对特定领域的专家模型却带来了挑战：专家模型缺乏从所有可用数据中学习的能力，并且必须更仔细地解决训练和测试条件不匹配的问题。在这项工作中，作者研究了目标数据选择作为应对这些挑战的策略，从10万小时的野外训练数据中选择相关子集，以优化在目标领域上的性能。作者使用捕捉互补特征（说话者属性、语音内容、语义含义）的嵌入来表示语音样本，并分析了沿这些轴进行数据选择时的相关性和多样性如何影响下游ASR性能。

**与关注主题的相关性**：论文的核心贡献是提出了一种基于嵌入表示的数据选择方法，用于构建更高效的领域特定模型。在化学信息学和质谱分析中，高质量、特定领域的数据集对于训练可靠的化学大模型和质谱结构推理模型至关重要。本文提出的“目标数据选择”框架和利用嵌入（可视为一种表示学习）来评估数据相关性的方法论，为化学领域如何从海量、异构的化学数据（如PubChem、质谱数据库）中筛选和构建高质量训练集提供了直接的技术参考。这满足了标准2（数据资源相关），因为它提出了一种可用于为特定主题（如化学模型训练）筛选和构建数据资源的方法论和工具思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern ASR systems are typically trained on large-scale pseudo-labeled, in-the-wild data spanning multiple domains. While such heterogeneous data benefit generalist models designed for broad deployment, they pose challenges for specialist models targeting specific domains: specialist models lack the capacity to learn from all available data, and one must pay closer attention to addressing the mismatch between training and test conditions. In this work, we study targeted data selection as a strategy to address these challenges, selecting relevant subsets from 100k hours of in-the-wild training data to optimize performance on target domains. We represent speech samples using embeddings that capture complementary characteristic--speaker attributes, phonetic content, and semantic meaning--and analyze how relevance and diversity along these axes when performing data selection affect downstream ASR performance. Our experiments with CTC-based Conformer models show that training on a strategically selected 5% subset can exceed the performance of models trained on the full dataset by up to 36.8% relative WER reduction on target domains.

</details>

---

### 47. [Distributional Regression with Tabular Foundation Models: Evaluating Probabilistic Predictions via Proper Scoring Rules](https://arxiv.org/abs/2603.08206)

**基本信息**

- 🔗 arXiv: [`2603.08206`](https://arxiv.org/abs/2603.08206)
- 👥 作者: Jonas Landsgesell, Pascal Knoll
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08206.pdf)

**💡 相关性分析**

满足标准3：论文对预测模型（特别是表格基础模型）的评估指标进行了系统性讨论和比较，重点探讨了分布性评估和适当评分规则，这些讨论对于评估和构建能够进行不确定性量化的化学大模型具有重要的相关性和指导意义。

**📖 中文摘要**

本文指出，诸如TabPFN和TabICL等表格基础模型已经能够产生完整的预测分布，然而用于评估它们的基准（如TabArena, TALENT等）仍然几乎完全依赖点估计指标（如RMSE, R²）。这种不匹配隐含地奖励那些能产生良好条件均值的模型，而忽略了预测分布的质量。作者提出了两个贡献：首先，建议用适当的评分规则（如CRPS, CRLS, Interval Score）来补充标准的点估计指标，并在20个OpenML回归数据集上对TabPFN和TabICL进行了关于这些评分规则的直接比较。其次，作者从分析和实证上表明，不同的适当评分规则会导致不同的模型排名和训练期间不同的归纳偏差，即使每个规则本身都被真实分布最小化。

**与关注主题的相关性**：论文的核心是讨论如何更全面地评估和训练能够输出预测分布的表格基础模型。在化学信息学中，许多任务（如分子性质预测、反应产率估计、质谱解析中的候选结构排序）本质上是具有不确定性的回归或分类问题。构建化学大模型不仅需要准确的点预测，更需要可靠的不确定性量化。本文系统探讨的适当评分规则和分布性评估指标，为评估化学领域预测模型（尤其是那些旨在提供概率输出的化学大模型）的性能提供了重要的方法论指导。这满足了标准3（综述展望相关），因为它对预测模型（可视为基础模型的一种）的评估指标进行了系统的讨论和比较，包含了与构建可靠化学预测模型相关的重要评估维度讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tabular foundation models such as TabPFN and TabICL already produce full predictive distributions, yet the benchmarks used to evaluate them (TabArena, TALENT, and others) still rely almost exclusively on point-estimate metrics (RMSE, $R^2$). This mismatch implicitly rewards models that elicit a good conditional mean while ignoring the quality of the predicted distribution. We make two contributions. First, we propose supplementing standard point metrics with proper scoring rules (CRPS, CRLS, and the Interval Score) and provide a head-to-head comparison of realTabPFNv2.5 and TabICLv2 with regards to some proper scoring rules across 20 OpenML regression datasets. Second, we show analytically and empirically that different proper scoring rules induce different model rankings and different inductive biases during training, even though each rule is individually minimized by the true distribution. Fine-tuning realTabPFNv2.5 with scoring rules not seen during pretraining (CRLS, $\beta=1.8$ energy score) yields consistent improvements on the corresponding metrics, confirming that the training loss shapes the model beyond what propriety alone guarantees. Together, these findings argue for (i) reporting distributional metrics in tabular regression benchmarks and (ii) making the training objective of foundation models adaptable (via fine-tuning or task-token conditioning) to the scoring rule relevant to the downstream decision problem.

</details>

---

### 48. [Context Engineering: From Prompts to Corporate Multi-Agent Architecture](https://arxiv.org/abs/2603.09619)

**基本信息**

- 🔗 arXiv: [`2603.09619`](https://arxiv.org/abs/2603.09619)
- 👥 作者: Vera V. Vishnyakova
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09619.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于AI智能体系统架构和工程的前瞻性、综述性讨论，提出了“语境工程”等高层学科概念，对于设计和部署用于化学信息学与质谱分析自动化任务的化学大模型智能体具有重要的相关性和指导意义。

**📖 中文摘要**

本文提出了“语境工程”（Context Engineering, CE）作为一个独立的学科，关注于设计、构建和管理AI智能体进行决策的整个信息环境。随着AI系统从无状态的聊天机器人演变为自主的多步骤智能体，仅关注单个查询设计的“提示工程”（Prompt Engineering, PE）被证明是必要但不充分的。作者借鉴了供应商架构（Google ADK, Anthropic, LangChain）、当前学术工作（ACE框架，Google DeepMind的智能委托）、企业研究（德勤，2026；毕马威，2026）以及作者构建多智能体系统的经验，提出了五个语境质量标准：相关性、充分性、隔离性、经济性和可溯源性，并将语境框架为智能体的操作系统。

**与关注主题的相关性**：本文是一篇关于AI智能体系统设计与工程的前瞻性、综述性论文。它提出的“语境工程”概念，以及后续的“意图工程”和“规范工程”，构成了一个从提示到多智能体架构的成熟度模型。化学信息学和质谱分析领域正在积极探索AI智能体用于自动化实验设计、分子逆向合成、质谱数据解析等工作流。本文系统地梳理和展望了构建复杂、可扩展AI智能体系统所需的高层工程学科，为化学领域如何设计和部署用于自动化科学发现的化学大模型智能体提供了重要的架构指导和前瞻性思考。这满足了标准3（综述展望相关），因为它是一篇针对智能体系统架构和工程的前瞻性、综述性讨论，与如何构建和部署化学领域的AI智能体密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) systems evolve from stateless chatbots to autonomous multi-step agents, prompt engineering (PE), the discipline of crafting individual queries, proves necessary but insufficient. This paper introduces context engineering (CE) as a standalone discipline concerned with designing, structuring, and managing the entire informational environment in which an AI agent makes decisions. Drawing on vendor architectures (Google ADK, Anthropic, LangChain), current academic work (ACE framework, Google DeepMind's intelligent delegation), enterprise research (Deloitte, 2026; KPMG, 2026), and the author's experience building a multi-agent system, the paper proposes five context quality criteria: relevance, sufficiency, isolation, economy, and provenance, and frames context as the agent's operating system. Two higher-order disciplines follow. Intent engineering (IE) encodes organizational goals, values, and trade-off hierarchies into agent infrastructure. Specification engineering (SE) creates a machine-readable corpus of corporate policies and standards enabling autonomous operation of multi-agent systems at scale. Together these four disciplines form a cumulative pyramid maturity model of agent engineering, in which each level subsumes the previous one as a necessary foundation. Enterprise data reveals a gap: while 75% of enterprises plan agentic AI deployment within two years (Deloitte, 2026), deployment has surged and retreated as organizations confront scaling complexity (KPMG, 2026). The Klarna case illustrates a dual deficit, contextual and intentional. Whoever controls the agent's context controls its behavior; whoever controls its intent controls its strategy; whoever controls its specifications controls its scale.

</details>

---

### 49. [From Imitation to Intuition: Intrinsic Reasoning for Open-Instance Video Classification](https://arxiv.org/abs/2603.10300)

**基本信息**

- 🔗 arXiv: [`2603.10300`](https://arxiv.org/abs/2603.10300)
- 👥 作者: Ke Zhang, Xiangchen Zhao, Yunjie Tian 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10300.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于提升视觉语言模型（作为大模型的一种）的内在推理能力以应对开放实例挑战，其方法论（监督对齐、强化学习优化推理）直接关联到如何增强化学大模型和质谱结构推理模型处理新颖、复杂化学实体的核心能力。

**📖 中文摘要**

本文提出了一种名为DeepIntuit的框架，用于解决开放实例视频分类任务。传统视频分类模型在数据分布同质的场景下表现良好，但现实应用常呈现开放实例挑战，即类内变化巨大且复杂，超出了现有基准的范围。传统的视频编码器模型难以拟合这些多样化的分布，而视觉语言模型（VLMs）虽然具有优越的泛化能力，但尚未充分利用其推理能力（直觉）来完成此类任务。本文通过一个内在推理框架，将开放实例视频分类从模仿演进到直觉。DeepIntuit首先通过冷启动监督对齐来初始化推理能力，然后使用组相对策略优化（GRPO）通过强化学习来增强推理连贯性。关键的是，为了将这种推理转化为准确的分类，DeepIntuit随后引入了一个直觉校准阶段。在此阶段，一个分类器在由精炼后的VLM生成的内在推理轨迹上进行训练，确保在没有分布不匹配的情况下实现稳定的知识迁移。

**与关注主题的相关性**：论文的核心是探索如何让视觉语言模型（VLMs）超越简单的特征模仿，演进到利用其内在推理能力（“直觉”）来处理复杂、开放实例的任务。虽然应用领域是视频分类，但其方法论——即通过监督对齐和强化学习来激发和利用大模型（VLMs）的内在推理能力——具有普适性。在化学信息学中，化学大模型（如分子语言模型、质谱-结构联合模型）同样面临处理新颖、复杂化学实体（如新分子、未知质谱）的挑战。本文提出的“从模仿到直觉”的框架以及相关的训练技术（GRPO、直觉校准），为提升化学大模型在开放世界化学问题（如未知化合物的质谱解析）上的推理和泛化能力提供了有价值的方法论参考。这满足了标准1（核心主题相关），因为其关于提升大模型内在推理能力以应对开放实例挑战的研究，直接关联到化学大模型和质谱结构推理模型的核心能力建设。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Conventional video classification models, acting as effective imitators, excel in scenarios with homogeneous data distributions. However, real-world applications often present an open-instance challenge, where intra-class variations are vast and complex, beyond existing benchmarks. While traditional video encoder models struggle to fit these diverse distributions, vision-language models (VLMs) offer superior generalization but have not fully leveraged their reasoning capabilities (intuition) for such tasks. In this paper, we bridge this gap with an intrinsic reasoning framework that evolves open-instance video classification from imitation to intuition. Our approach, namely DeepIntuit, begins with a cold-start supervised alignment to initialize reasoning capability, followed by refinement using Group Relative Policy Optimization (GRPO) to enhance reasoning coherence through reinforcement learning. Crucially, to translate this reasoning into accurate classification, DeepIntuit then introduces an intuitive calibration stage. In this stage, a classifier is trained on this intrinsic reasoning traces generated by the refined VLM, ensuring stable knowledge transfer without distribution mismatch. Extensive experiments demonstrate that for open-instance video classification, DeepIntuit benefits significantly from transcending simple feature imitation and evolving toward intrinsic reasoning. Our project is available at this https URL .

</details>

---

### 50. [One Supervisor, Many Modalities: Adaptive Tool Orchestration for Autonomous Queries](https://arxiv.org/abs/2603.11545)

**基本信息**

- 🔗 arXiv: [`2603.11545`](https://arxiv.org/abs/2603.11545)
- 👥 作者: Mayank Saini, Arit Kumar Bishwas
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11545.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个用于自主多模态查询处理的智能AI框架，其核心的集中式工具编排和自适应路由架构，与构建需要集成多种化学信息工具和模型的化学大模型应用或质谱分析智能体的系统设计直接相关。

**📖 中文摘要**

本文提出了一个用于自主多模态查询处理的智能AI框架，该框架协调跨文本、图像、音频、视频和文档模态的专用工具。一个中央“监督器”动态分解用户查询，将子任务委托给适合模态的工具（例如，目标检测、OCR、语音转录），并通过自适应路由策略（而非预定的决策树）综合结果。对于纯文本查询，该框架使用通过RouteLLM学习的路由，而非文本路径则使用SLM辅助的模态分解。在涵盖15个任务类别的2847个查询上的评估表明，与匹配的层次结构基线相比，该框架在保持准确率持平的同时，实现了准确答案获取时间减少72%、对话返工减少85%、成本降低67%。

**与关注主题的相关性**：本文提出了一个多模态AI智能体框架，其核心是“中央监督器”对专用工具进行智能编排和路由。在化学信息学和质谱分析中，一个理想的“化学AI助手”或“质谱解析智能体”很可能需要集成多种工具和模型，例如：化学数据库查询、分子结构绘制、谱图模拟、物性计算、文献检索等。本文提出的集中式编排架构、动态查询分解、以及跨模态工具的自适应路由策略，为构建此类复杂的化学领域多模态AI智能体系统提供了可参考的架构蓝图和工程思路。这满足了标准1（核心主题相关），因为其关于构建能够协调多种工具和模态的自主AI智能体的研究，与构建功能强大的化学大模型应用或质谱分析智能体的系统架构直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present an agentic AI framework for autonomous multimodal query processing that coordinates specialized tools across text, image, audio, video, and document modalities. A central Supervisor dynamically decomposes user queries, delegates subtasks to modality-appropriate tools (e.g., object detection, OCR, speech transcription), and synthesizes results through adaptive routing strategies rather than predetermined decision trees. For text-only queries, the framework uses learned routing via RouteLLM, while non-text paths use SLM-assisted modality decomposition. Evaluated on 2,847 queries across 15 task categories, our framework achieves 72% reduction in time-to-accurate-answer, 85% reduction in conversational rework, and 67% cost reduction compared to the matched hierarchical baseline while maintaining accuracy parity. These results demonstrate that intelligent centralized orchestration fundamentally improves multimodal AI deployment economics.

</details>

---

### 51. [XSkill: Continual Learning from Experience and Skills in Multimodal Agents](https://arxiv.org/abs/2603.12056)

**基本信息**

- 🔗 arXiv: [`2603.12056`](https://arxiv.org/abs/2603.12056)
- 👥 作者: Guanyu Jiang, Zhaochen Su, Xiaoye Qu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12056.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个使多模态AI智能体能够从经验和技能中进行持续学习的框架，其方法论（视觉基础的双流知识积累与检索）与构建能够从历史化学数据和任务中学习并自我改进的化学大模型智能体直接相关。

**📖 中文摘要**

本文指出，多模态智能体现在能够利用多样化的工具处理复杂的推理任务，但在开放环境中仍然存在工具使用效率低下和编排不灵活的问题。一个核心挑战是使此类智能体能够在不更新参数的情况下，从过去的轨迹中持续学习以提高性能。作者识别了对这一目标至关重要的两种互补的可重用知识形式：经验（提供工具选择和决策制定的简洁行动级指导）和技能（提供规划和工具使用的结构化任务级指导）。为此，作者提出了XSkill，一个用于多模态智能体中从经验和技能进行持续学习的双流框架。XSkill将知识提取和检索都建立在视觉观察的基础上。在积累阶段，XSkill通过基于视觉的总结和跨轨迹批判，从多路径 rollout 中提炼和巩固经验和技能。在推理阶段，它根据当前的视觉上下文检索并调整这些知识，并将使用历史反馈回积累阶段，形成一个持续学习循环。

**与关注主题的相关性**：论文研究的是如何让多模态AI智能体通过持续学习（从经验与技能中）来提升其在复杂任务中的表现。在化学信息学领域，构建能够自动化实验、分析数据、提出假设的AI科研助手（化学大模型智能体）是一个前沿方向。这样的智能体需要能够从历史实验数据、成功/失败的分析案例中学习“经验”和“技能”。本文提出的XSkill框架，特别是其基于视觉（可类比为化学数据的多种可视化表示，如分子图、谱图）的知识积累与检索机制，以及双流（经验/技能）学习架构，为开发具有持续学习和自我改进能力的化学AI智能体提供了创新的方法论。这满足了标准1（核心主题相关），因为其关于赋予AI智能体持续学习能力的研究，直接关联到构建能够从历史化学数据中学习并不断优化的化学大模型智能体。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal agents can now tackle complex reasoning tasks with diverse tools, yet they still suffer from inefficient tool use and inflexible orchestration in open-ended settings. A central challenge is enabling such agents to continually improve without parameter updates by learning from past trajectories. We identify two complementary forms of reusable knowledge essential for this goal: experiences, providing concise action-level guidance for tool selection and decision making, and skills, providing structured task-level guidance for planning and tool use. To this end, we propose XSkill, a dual-stream framework for continual learning from experience and skills in multimodal agents. XSkill grounds both knowledge extraction and retrieval in visual observations. During accumulation, XSkill distills and consolidates experiences and skills from multi-path rollouts via visually grounded summarization and cross-rollout critique. During inference, it retrieves and adapts this knowledge to the current visual context and feeds usage history back into accumulation to form a continual learning loop. Evaluated on five benchmarks across diverse domains with four backbone models, XSkill consistently and substantially outperforms both tool-only and learning-based baselines. Further analysis reveals that the two knowledge streams play complementary roles in influencing the reasoning behaviors of agents and show superior zero-shot generalization.

</details>

---

### 52. [How to Build a Quantum Supercomputer: Scaling from Hundreds to Millions of Qubits](https://arxiv.org/abs/2411.10406)

**基本信息**

- 🔗 arXiv: [`2411.10406`](https://arxiv.org/abs/2411.10406)
- 👥 作者: Masoud Mohseni, Artur Scherer, K. Grace Johnson 等51人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.10406.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于量子超级计算机扩展及其在科学计算（特别是量子化学）中应用的综合性、前瞻性综述，其关于量子计算资源、架构和应用前景的讨论，对于展望未来量子计算如何赋能化学大模型和复杂化学系统模拟具有重要的相关性。

**📖 中文摘要**

本文全面回顾了从数百个量子比特扩展到数百万个量子比特的量子超级计算机所面临的挑战。作者展示了如何通过采用现有的半导体技术来构建质量更高的量子比特、采用系统工程方法以及执行分布式异构量子-经典计算来促进扩展。作者基于超导量子比特，根据当前、目标和期望的硬件规格，考虑误差的真实分布，为表面码纠错量子计算机上的量子应用提供了详细的资源和灵敏度分析。作者为几个实用规模的应用提供了全面的资源估算，包括量子化学计算、催化剂设计、NMR光谱和Fermi-Hubbard模拟。作者表明，通过硬件改进和紧密的量子-HPC集成相结合，可以获得数量级的性能提升。

**与关注主题的相关性**：虽然论文主要关注量子计算硬件和架构，但其核心目标之一是实现量子化学计算等科学应用的实用化。量子化学计算是化学信息学和计算化学的核心领域，用于精确模拟分子结构、反应和性质。本文对实现实用规模量子化学计算所需的硬件资源、误差容限和系统架构进行了深入分析和展望。这对于未来利用量子计算增强化学大模型（例如，提供高精度量子力学数据作为训练标签或验证手段）或解决经典计算难以处理的复杂化学系统（如催化剂设计）具有重要的指导意义。它满足了标准3（综述展望相关），因为它是一篇关于量子计算（特别是其在化学等科学计算中应用）扩展挑战和前景的综合性、前瞻性综述，包含了与未来化学计算范式相关的重要讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the span of four decades, quantum computation has evolved from an intellectual curiosity to a potentially realizable technology. Today, small-scale demonstrations have become possible for quantum algorithmic primitives on hundreds of physical qubits. Nevertheless, there are significant outstanding challenges in quantum hardware, fabrication, software architecture, and algorithms on the path towards a full-stack scalable quantum computing technology. Here, we provide a comprehensive review of these scaling challenges. We show how to facilitate scaling by adopting existing semiconductor technology to build much higher-quality qubits, employing systems engineering approaches, and performing distributed heterogeneous quantum-classical computing. We provide a detailed resource and sensitivity analysis for quantum applications on surface-code error-corrected quantum computers given current, target, and desired hardware specifications based on superconducting qubits, accounting for a realistic distribution of errors. We provide comprehensive resource estimates for several utility-scale applications including quantum chemistry calculations, catalyst design, NMR spectroscopy, and Fermi-Hubbard simulation. We show that orders of magnitude enhancement in performance could be obtained by a combination of hardware improvements and tight quantum-HPC integration. Furthermore, we introduce high-performance architectures for quantum-probabilistic computing with custom-designed accelerators to tackle today's industry-scale classical optimization, machine learning, and quantum simulation tasks in a cost-effective manner.

</details>

---

### 53. [Aligning Large Language Model Agents with Rational and Moral Preferences: A Supervised Fine-Tuning Approach](https://arxiv.org/abs/2507.20796)

**基本信息**

- 🔗 arXiv: [`2507.20796`](https://arxiv.org/abs/2507.20796)
- 👥 作者: Wei Lu, Amit Dhanda, Daniel L. Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.20796.pdf)

**💡 相关性分析**

满足标准1：论文研究了通过监督微调将LLM智能体行为与明确的经济/道德偏好对齐的方法，其技术框架和思想对于在化学信息学中训练目标导向、符合伦理或优化目标的化学大模型智能体具有直接的相关性。

**📖 中文摘要**

本文研究了在市场和组织中作为自主智能体运行的大型语言模型（LLMs）在战略环境中的行为。作者记录了现成的LLM智能体在经典经济博弈中表现出系统性地偏离对收益敏感的行为，包括过度合作和对激励的有限反应。作者引入了一种监督微调方法，使智能体行为与明确的经济偏好保持一致。具体来说，作者在两种程式化的效用规范下生成最优策略：最大化自身利益的“经济人”（homo economicus）和包含康德普遍性的“道德人”（homo moralis），并使用这些效用隐含的推理和策略来指导微调。在一个小的、理论驱动的合成数据集上进行微调，会在战略行为中引发持久且可解释的转变。在道德困境和重复双寡头定价的应用中，与不同偏好结构对齐的智能体产生了系统不同的均衡结果和定价动态。

**与关注主题的相关性**：本文研究的是如何通过微调使LLM智能体在战略互动中表现出符合特定理性或道德偏好的行为。在化学信息学领域，AI智能体可能被用于自动化实验决策（例如，选择下一个要合成的分子或要测试的反应条件），这本质上是一个在资源约束和不确定性下的序列决策问题。确保这些化学AI智能体的决策不仅有效，而且符合科学伦理（如绿色化学原则）、安全规范或资源优化目标，是一个重要课题。本文提出的基于经济/道德理论偏好对齐的微调方法，为在化学领域设计和训练具有特定目标函数（如最大化发现效率、最小化环境足迹）的“理性”或“负责任”的化学大模型智能体提供了方法论上的借鉴。这满足了标准1（核心主题相关），因为其关于对齐多智能体环境中AI行为与明确偏好的研究，与设计和训练目标导向、符合伦理的化学AI智能体直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As large language models (LLMs) increasingly act as autonomous agents in markets and organizations, their behavior in strategic environments becomes economically consequential. We document that off-the-shelf LLM agents exhibit systematic deviations from payoff-sensitive behavior in canonical economic games, including excessive cooperation and limited responsiveness to incentives. We introduce a supervised fine-tuning approach that aligns agent behavior with explicit economic preferences. Specifically, we generate optimal strategies under two stylized utility specifications, homo economicus, which maximizes self-interest, and homo moralis, which incorporates Kantian universalizability, and use these utility-implied reasoning and strategies to guide fine-tuning. Fine-tuning on a small, theory-driven synthetic dataset induces persistent and interpretable shifts in strategic behavior. In applications to moral dilemmas and repeated duopoly pricing, agents aligned to different preference structures produce systematically distinct equilibrium outcomes and pricing dynamics. These results frame AI alignment in multi-agent settings as an objective-design problem and illustrate how economic theory can guide the design of strategically coherent AI agents.

</details>

---

### 54. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等20人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了名为LatentChem的新方法，旨在改进化学大语言模型的推理机制。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学大语言模型（LLMs）的潜在推理接口。它旨在解决当前化学LLMs主要依赖显式自然语言思维链（CoT）进行复杂推理的局限性。作者认为化学推理本质上是连续和结构化的，将其强制转换为离散的语言标记会引入根本性的表示不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中直接执行多步推理，而仅输出最终的语言结果。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，更是计算优势上的。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于强大的CoT基线实现了59.88%的非平局胜率，同时平均减少了10.84倍的推理开销。这项工作直接针对“化学大模型”的核心主题，探索了超越传统文本CoT的更高效、更本质的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average reduction in reasoning overhead. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 55. [Proof-Carrying Materials: Falsifiable Safety Certificates for Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2603.12183)

**基本信息**

- 🔗 arXiv: [`2603.12183`](https://arxiv.org/abs/2603.12183)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12183.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（为机器学习原子间势提供可靠性保证）与构建可靠、可解释的“化学大模型”这一主题直接相关，提供了重要的方法论和工具。

**📖 中文摘要**

本文提出了“材料证明携带”（Proof-Carrying Materials, PCM）框架，旨在为机器学习原子间势（MLIPs）提供可证伪的安全证书。MLIPs被广泛用于高通量材料筛选，但缺乏形式化的可靠性保证。PCM通过三个阶段来缩小MLIP预测与高精度密度泛函理论（DFT）计算之间的差距：在成分空间中进行对抗性证伪、使用95%置信区间进行引导包络细化，以及使用Lean 4进行形式化验证。该研究对CHGNet、TensorNet和MACE等主流MLIP架构进行了审计，揭示了架构特定的盲点，并训练了一个风险模型来预测未见材料的失败情况。在一个热电材料筛选的案例研究中，经过PCM审计的协议发现了62种被单一MLIP筛选遗漏的稳定材料，将发现率提高了25%。虽然论文主要关注材料科学中的MLIP验证，但其核心方法——通过对抗性测试、统计置信区间和形式化验证来审计和保证机器学习模型（特别是用于物理科学领域的模型）的可靠性——与构建可靠、可解释的“化学大模型”这一更广泛的目标高度相关。它为如何评估和提升化学领域AI模型的可信度提供了方法论和工具层面的重要参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learned interatomic potentials (MLIPs) are deployed for high-throughput materials screening without formal reliability guarantees. We show that a single MLIP used as a stability filter misses 93% of density functional theory (DFT)-stable materials (recall 0.07) on a 25,000-material benchmark. Proof-Carrying Materials (PCM) closes this gap through three stages: adversarial falsification across compositional space, bootstrap envelope refinement with 95% confidence intervals, and Lean 4 formal certification. Auditing CHGNet, TensorNet and MACE reveals architecture-specific blind spots with near-zero pairwise error correlations (r <= 0.13; n = 5,000), confirmed by independent Quantum ESPRESSO validation (20/20 converged; median DFT/CHGNet force ratio 12x). A risk model trained on PCM-discovered features predicts failures on unseen materials (AUC-ROC = 0.938 +/- 0.004) and transfers across architectures (cross-MLIP AUC-ROC ~ 0.70; feature importance r = 0.877). In a thermoelectric screening case study, PCM-audited protocols discover 62 additional stable materials missed by single-MLIP screening - a 25% improvement in discovery yield.

</details>

---

## 📊 数据统计
- 累计运行天数：34
- 累计论文数量：2356

## 📝 历史记录

> 暂无历史数据

