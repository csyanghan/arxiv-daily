# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-19 01:31:04

## 📅 2026-03-19 (今日最新)

**相关论文数：64**

### 1. [Finder: A Multimodal AI-Powered Search Framework for Pharmaceutical Data Retrieval](https://arxiv.org/abs/2603.15623)

**基本信息**

- 🔗 arXiv: [`2603.15623`](https://arxiv.org/abs/2603.15623)
- 👥 作者: Suyash Mishra, Srikanth Patil, Satyanarayan Pati 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15623.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于药物数据检索的多模态AI框架（Finder），该框架处理并提供了大规模、多模态的数据集和资源。这些数据资源（文档、视频、音频）是训练和验证化学大模型以及进行质谱结构推理研究的重要基础。

**📖 中文摘要**

本文介绍了Finder，一个用于药物数据检索的多模态AI搜索框架。该框架通过混合向量搜索（结合稀疏词法和密集语义模型）统一了对文本、图像、音频和视频的检索。其模块化管道可以处理多种格式，丰富元数据，并将内容存储在向量原生后端中。Finder支持基于推理的自然语言搜索，提高了精确度和上下文相关性。该系统已处理超过291,400份文档、31,070个视频和1,192个音频文件，涵盖98种语言。该工作与化学信息学领域相关，因为它提供了一个强大的、可扩展的AI驱动工具，用于检索和分析包含化学结构、质谱数据、研究论文和监管文件在内的多模态药物数据。这些数据资源对于构建和评估化学大模型（例如用于分子性质预测或逆合成规划）以及质谱结构推理任务至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming pharmaceutical search, where traditional systems struggle with multimodal content and manual curation. Finder is a scalable AI-powered framework that unifies retrieval across text, images, audio, and video using hybrid vector search, combining sparse lexical and dense semantic models. Its modular pipeline ingests diverse formats, enriches metadata, and stores content in a vector-native backend. Finder supports reasoning-aware natural language search, improving precision and contextual relevance. The system has processed over 291,400 documents, 31,070 videos, and 1,192 audio files in 98 languages. Techniques like hybrid fusion, chunking, and metadata-aware routing enable intelligent access across regulatory, research, and commercial domains.

</details>

---

### 2. [Neural-Symbolic Logic Query Answering in Non-Euclidean Space](https://arxiv.org/abs/2603.15633)

**基本信息**

- 🔗 arXiv: [`2603.15633`](https://arxiv.org/abs/2603.15633)
- 👥 作者: Lihui Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15633.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（神经符号模型、图神经网络、知识图谱推理）所采用的方法论与化学信息学和质谱分析中的关键任务直接相关，例如分子图表示学习、基于图模型的谱图解析和结构推理。

**📖 中文摘要**

本文提出了HYQNET，一个在双曲空间中用于知识图谱上复杂一阶逻辑查询推理的神经符号模型。它将FOL查询分解为关系投影和模糊集上的逻辑操作，并通过在双曲空间中基于双曲图神经网络的方法进行知识图谱补全，以有效嵌入递归查询树并保持结构依赖。该模型旨在整合符号方法的可解释性和神经方法的泛化能力。虽然论文核心是逻辑推理，但其方法论——特别是利用图神经网络（GNN）进行知识图谱补全和关系推理——与化学信息学中分子图表示学习、分子性质预测以及通过图模型进行谱图-结构关联推理（质谱结构推理的核心）高度相关。论文中提出的在非欧几里得空间（双曲空间）中捕获层次结构的方法，为处理具有固有层次或树状结构的化学数据（如分子片段树、代谢通路）提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Answering complex first-order logic (FOL) queries on knowledge graphs is essential for reasoning. Symbolic methods offer interpretability but struggle with incomplete graphs, while neural approaches generalize better but lack transparency. Neural-symbolic models aim to integrate both strengths but often fail to capture the hierarchical structure of logical queries, limiting their effectiveness. We propose HYQNET, a neural-symbolic model for logic query reasoning that fully leverages hyperbolic space. HYQNET decomposes FOL queries into relation projections and logical operations over fuzzy sets, enhancing interpretability. To address missing links, it employs a hyperbolic GNN-based approach for knowledge graph completion in hyperbolic space, effectively embedding the recursive query tree while preserving structural dependencies. By utilizing hyperbolic representations, HYQNET captures the hierarchical nature of logical projection reasoning more effectively than Euclidean-based approaches. Experiments on three benchmark datasets demonstrate that HYQNET achieves strong performance, highlighting the advantages of reasoning in hyperbolic space.

</details>

---

### 3. [Tokenization Tradeoffs in Structured EHR Foundation Models](https://arxiv.org/abs/2603.15644)

**基本信息**

- 🔗 arXiv: [`2603.15644`](https://arxiv.org/abs/2603.15644)
- 👥 作者: Lin Lawrence Guo, Santiago Eduardo Arciniegas, Joseph Jihyung Lee 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15644.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（结构化序列数据的标记化策略及其对模型性能与效率的影响）直接关系到如何为化学大模型（处理分子序列、反应SMILES等）和质谱结构推理模型（处理峰值序列）设计和优化输入表示，这是一个基础且关键的主题。

**📖 中文摘要**

本文研究了结构化电子健康记录基础模型中的标记化权衡。论文预训练了一个Transformer模型，通过因子设计改变事件编码、时间编码和工作流注释等标记化方式，并在74个临床预测任务上评估性能。研究发现，联合事件编码和位置时间编码优于其他方案，同时减少了预训练所需的浮点运算次数。针对性消融实验将联合编码的优势归因于局部绑定效率，即将代码-属性对组合成单个标记，而不是分割成需要模型在预训练中学习关联的多个标记。这项工作系统地探索了标记化设计选择对下游性能和计算效率的影响。虽然领域是医疗，但其核心主题——为结构化序列数据（类似于化学中的分子序列或谱图峰值序列）设计高效且信息保真的标记化方案——是构建化学领域大语言模型或质谱序列模型的基础性、核心问题。论文提供的分析框架和结论可直接迁移至化学信息学中分子SMILES/ SELFIES标记化或质谱峰列表编码的研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models for structured electronic health records (EHRs) are pretrained on longitudinal sequences of timestamped clinical events to learn adaptable patient representations. Tokenization -- how these timelines are converted into discrete model inputs -- determines what information is preserved, how efficiently it is encoded, and which relationships must be learned versus precomputed. Yet the impact of tokenization design choices on downstream performance and computational efficiency remains largely unexplored. Here, we pretrained a transformer on pediatric EHR data under a factorial design, varying tokenization along event encoding, time encoding, and workflow annotation. We evaluated area-under-the-receiver-operating-characteristic curve across 74 clinical prediction tasks. Joint event encoding and positional time encoding outperformed their alternatives (73/74 and 71/74 tasks) while requiring 39.5% and 9.6% fewer pretraining floating-point operations, respectively. Targeted ablations traced the joint encoding advantage to local binding efficiency, that is, code-attribute pairs are combined into single tokens, rather than split across tokens that the model must learn to associate during pretraining. External evaluation on an adult intensive care unit cohort demonstrated that this advantage generalizes despite substantial vocabulary mismatch, while temporal and workflow effects remain institution-specific. These results establish tokenization as a tractable lever for improving both the performance and efficiency of EHR foundation models.

</details>

---

### 4. [A Dynamic Survey of Fuzzy, Intuitionistic Fuzzy, Neutrosophic, Plithogenic, and Extensional Sets](https://arxiv.org/abs/2603.15667)

**基本信息**

- 🔗 arXiv: [`2603.15667`](https://arxiv.org/abs/2603.15667)
- 👥 作者: Takaaki Fujita, Florentin Smarandache
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15667.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于模糊集、直觉模糊集、中智集等不确定性建模理论的综合性综述。这些数学框架对于化学信息学（处理不精确的分子性质预测、模糊聚类）和质谱结构推理（处理不完整的谱图匹配、冲突的结构假设）具有重要的基础和指导意义，属于相关主题的重要方法论讨论。

**📖 中文摘要**

本文是一篇关于模糊集、直觉模糊集、中智集、Plithogenic集和可拓集等广义集合论框架的动态综述。它旨在对这些不确定性建模理论中的大量概念、构造和结构模式进行系统性的概述，并通过统一的阐述来激发新的见解、进一步的概念扩展和跨学科应用。虽然论文本身不专门针对化学或质谱，但它全面涵盖了处理不确定性、不精确性和部分真理的数学工具。这些工具在化学信息学和质谱分析中至关重要，例如：在化学大模型中处理预测的不确定性、在质谱结构推理中管理谱图匹配的模糊性、在QSAR模型中量化分子描述符的直觉模糊解释、或在中智逻辑框架下整合来自多个不完整或冲突证据（如不同数据库、不同解析算法）的结构假设。因此，这篇综述为相关领域的研究者提供了重要的方法论背景和潜在的建模框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real-world phenomena often exhibit vagueness, partial truth, and incomplete information. To model such uncertainty in a mathematically rigorous way, many generalized set-theoretic frameworks have been introduced, including Fuzzy Sets [1], Intuitionistic Fuzzy Sets [2], Neutrosophic Sets [3,4], Vague Sets [5], Hesitant Fuzzy Sets [6], Picture Fuzzy Sets [7], Quadripartitioned Neutrosophic Sets [8], Penta-Partitioned Neutrosophic Sets [9], Plithogenic Sets [10], HyperFuzzy Sets [11], and HyperNeutrosophic Sets [12]. Within these frameworks, a wide range of notions has been proposed and studied, particularly in the settings of fuzzy, intuitionistic fuzzy, neutrosophic, and plithogenic set theories. This extensive literature underscores both the significance of these theories and the breadth of their application areas. As a result, many ideas, constructions, and structural patterns recur across these four major families of uncertainty-oriented models. In this book, we provide a comprehensive, large-scale survey of Fuzzy, Intuitionistic Fuzzy, Neutrosophic, and Plithogenic Sets. Our goal is to give readers a systematic overview of existing developments and, through a unified exposition, to stimulate new insights, further conceptual extensions, and additional applications across a wide range of disciplines.

</details>

---

### 5. [I Know What I Don't Know: Latent Posterior Factor Models for Multi-Evidence Probabilistic Reasoning](https://arxiv.org/abs/2603.15670)

**基本信息**

- 🔗 arXiv: [`2603.15670`](https://arxiv.org/abs/2603.15670)
- 👥 作者: Aliyu Agboola Alege
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15670.pdf)

**💡 相关性分析**

满足标准1：论文提出的潜在后验因子框架专注于多证据概率推理，其核心方法论（整合多个不确定证据源进行结构化推理）直接适用于质谱结构推理中的关键问题，即如何融合来自不同数据库、算法或谱图特征的矛盾或不完整证据来推断最可能的结构。

**📖 中文摘要**

本文介绍了潜在后验因子模型，一个将变分自编码器的潜在后验转化为软似然因子以进行和积网络推理的框架，使得能够在非结构化证据上进行可处理的概率推理，同时保持校准的不确定性估计。论文实例化了LPF-SPN（基于结构的因子推理）和LPF-Learned（端到端学习聚合）两种架构，并在八个领域（七个合成数据集和FEVER基准）上进行了评估。该框架的核心贡献是桥接了潜在不确定性表示与结构化概率推理。在化学信息学和质谱分析中，经常需要整合来自多个嘈杂且可能矛盾的证据源（例如，多个质谱数据库的匹配结果、不同碎片化理论预测、互补的光谱技术）来推断分子结构或进行性质预测。LPF框架为解决这类“多证据概率推理”问题提供了一个原则性的、可解释的、且能量化不确定性的方法学工具，与质谱结构推理的核心挑战高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real-world decision-making, from tax compliance assessment to medical diagnosis, requires aggregating multiple noisy and potentially contradictory evidence sources. Existing approaches either lack explicit uncertainty quantification (neural aggregation methods) or rely on manually engineered discrete predicates (probabilistic logic frameworks), limiting scalability to unstructured data. We introduce Latent Posterior Factors (LPF), a framework that transforms Variational Autoencoder (VAE) latent posteriors into soft likelihood factors for Sum-Product Network (SPN) inference, enabling tractable probabilistic reasoning over unstructured evidence while preserving calibrated uncertainty estimates. We instantiate LPF as LPF-SPN (structured factor-based inference) and LPF-Learned (end-to-end learned aggregation), enabling a principled comparison between explicit probabilistic reasoning and learned aggregation under a shared uncertainty representation. Across eight domains (seven synthetic and the FEVER benchmark), LPF-SPN achieves high accuracy (up to 97.8%), low calibration error (ECE 1.4%), and strong probabilistic fit, substantially outperforming evidential deep learning, LLMs and graph-based baselines over 15 random seeds. Contributions: (1) A framework bridging latent uncertainty representations with structured probabilistic reasoning. (2) Dual architectures enabling controlled comparison of reasoning paradigms. (3) Reproducible training methodology with seed selection. (4) Evaluation against EDL, BERT, R-GCN, and large language model baselines. (5) Cross-domain validation. (6) Formal guarantees in a companion paper.

</details>

---

### 6. [Theoretical Foundations of Latent Posterior Factors: Formal Guarantees for Multi-Evidence Reasoning](https://arxiv.org/abs/2603.15674)

**基本信息**

- 🔗 arXiv: [`2603.15674`](https://arxiv.org/abs/2603.15674)
- 👥 作者: Aliyu Agboola Alege
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15674.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心内容是为一类多证据推理模型（LPF）建立严格的理论保证，这直接关系到如何构建可靠、可解释且具有不确定性量化能力的化学大模型和质谱结构推理系统。同时，它也可被视为对该方法论的重要理论性讨论和展望。

**📖 中文摘要**

本文提供了潜在后验因子理论基础的完整理论表征，证明了其在多证据聚合任务中的七个形式化保证，涵盖了校准保持、蒙特卡洛误差衰减、PAC-Bayes边界、信息论下界、在对抗性证据下的优雅性能衰减、校准衰减率以及精确的认知-偶然不确定性分解。所有定理都在包含多达4,200个训练示例的受控数据集上进行了实证验证。该理论框架将LPF确立为安全关键应用中可信多证据AI的基础。对于化学信息学和质谱分析，尤其是在高风险的药物发现或法医分析中，模型预测的可靠性、可解释性和不确定性量化至关重要。这篇论文为在多证据场景（如结合质谱、核磁、红外等多种光谱数据进行结构鉴定）中构建具有严格理论保证的、可信的AI系统提供了坚实的理论基础和验证工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a complete theoretical characterization of Latent Posterior Factors (LPF), a principled framework for aggregating multiple heterogeneous evidence items in probabilistic prediction tasks. Multi-evidence reasoning arises pervasively in high-stakes domains including healthcare diagnosis, financial risk assessment, legal case analysis, and regulatory compliance, yet existing approaches either lack formal guarantees or fail to handle multi-evidence scenarios architecturally. LPF encodes each evidence item into a Gaussian latent posterior via a variational autoencoder, converting posteriors to soft factors through Monte Carlo marginalization, and aggregating factors via exact Sum-Product Network inference (LPF-SPN) or a learned neural aggregator (LPF-Learned). We prove seven formal guarantees spanning the key desiderata for trustworthy AI: Calibration Preservation (ECE <= epsilon + C/sqrt(K_eff)); Monte Carlo Error decaying as O(1/sqrt(M)); a non-vacuous PAC-Bayes bound with train-test gap of 0.0085 at N=4200; operation within 1.12x of the information-theoretic lower bound; graceful degradation as O(epsilon*delta*sqrt(K)) under corruption, maintaining 88% performance with half of evidence adversarially replaced; O(1/sqrt(K)) calibration decay with R^2=0.849; and exact epistemic-aleatoric uncertainty decomposition with error below 0.002%. All theorems are empirically validated on controlled datasets spanning up to 4,200 training examples. Our theoretical framework establishes LPF as a foundation for trustworthy multi-evidence AI in safety-critical applications.

</details>

---

### 7. [PulmoVec: A Two-Stage Stacking Meta-Learning Architecture Built on the HeAR Foundation Model for Multi-Task Classification of Pediatric Respiratory Sounds](https://arxiv.org/abs/2603.15688)

**基本信息**

- 🔗 arXiv: [`2603.15688`](https://arxiv.org/abs/2603.15688)
- 👥 作者: Izzet Turkalp Akbasli, Oguzhan Serin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15688.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于领域基础模型（HeAR）的多任务学习框架，其方法论与在化学信息学中构建“质谱基础模型”或“分子基础模型”并用于多任务学习（如同时进行结构推理和性质预测）的研究主题直接相关，提供了可借鉴的技术路径。

**📖 中文摘要**

本文提出了PulmoVec，一个基于健康声学表示基础模型构建的多任务框架，用于儿科呼吸音分类。该框架包含三个特定任务的分类器（筛查、声音模式识别、疾病组预测），并通过一个LightGBM堆叠元模型结合其输出概率与人口统计学元数据。在SPRSound数据库的24,808个事件级标注片段上，该模型在事件级和患者级均表现出色。这项工作展示了基于基础模型的数字听诊在儿科呼吸医学中的潜力。虽然应用领域是医疗，但其方法论——利用预训练的基础模型（HeAR）提取通用声学表示，并针对下游任务进行多任务学习和元模型堆叠——与化学信息学和质谱分析中的范式高度相似。例如，在质谱分析中，可以预训练一个通用的“质谱基础模型”来学习谱图的通用表示，然后针对不同的下游任务（如化合物分类、结构推理、毒性预测）进行微调或构建多任务模型。PulmoVec为如何在特定科学领域（如质谱学）构建和利用领域基础模型提供了一个可参考的架构范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Background: Respiratory diseases are a leading cause of childhood morbidity and mortality, yet lung auscultation remains subjective and limited by inter-listener variability, particularly in pediatric populations. Existing AI approaches are further constrained by small datasets and single-task designs. We developed PulmoVec, a multi-task framework built on the Health Acoustic Representations (HeAR) foundation model for classification of pediatric respiratory sounds. Methods: In this retrospective analysis of the SPRSound database, 24,808 event-level annotated segments from 1,652 pediatric patients were analyzed. Three task-specific classifiers were trained for screening, sound-pattern recognition, and disease-group prediction. Their out-of-fold probability outputs were combined with demographic metadata in a LightGBM stacking meta-model, and event-level predictions were aggregated to the patient level using ensemble voting. Results: At the event level, the screening model achieved an ROC-AUC of 0.96 (95% CI, 0.95-0.97), the sound-pattern recognition model a macro ROC-AUC of 0.96 (95% CI, 0.96-0.97), and the disease-group prediction model a macro ROC-AUC of 0.94 (95% CI, 0.93-0.94). At the patient level, disease-group classification yielded an accuracy of 0.74 (95% CI, 0.71-0.77), a weighted F1-score of 0.73, and a macro ROC-AUC of 0.91 (95% CI, 0.90-0.93). Stacking improved performance across all tasks compared with base models alone. Conclusions: PulmoVec links event-level acoustic phenotyping with patient-level clinical classification, supporting the potential of foundation-model-based digital auscultation in pediatric respiratory medicine. Multi-center external validation across devices and real-world conditions remains essential.

</details>

---

### 8. [Knowledge Graph Extraction from Biomedical Literature for Alkaptonuria Rare Disease](https://arxiv.org/abs/2603.15711)

**基本信息**

- 🔗 arXiv: [`2603.15711`](https://arxiv.org/abs/2603.15711)
- 👥 作者: Giang Pham, Rebecca Finetti, Caterina Graziani 等15人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15711.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种从生物医学文献中提取关系以构建领域知识图谱的方法论和流程。所构建的知识图谱本身就是一种重要的数据资源，并且该方法可应用于化学和质谱领域，用于从科学文献中自动构建包含化合物、结构、谱图、性质等实体关系的化学知识图谱，为化学大模型提供训练和推理所需的结构化知识。

**📖 中文摘要**

本文提出了一种基于PubTator3文本挖掘的方法，用于从生物医学文献中大规模提取生物医学关系，以构建关于罕见病Alkaptonuria的知识图谱。由于该疾病在现有生物医学知识图谱中代表性不足或完全缺失，作者构建了两个不同规模的KG，利用现有生化知识进行验证，并用其提取可能与AKU相关的基因、疾病和疗法。该计算框架揭示了疾病的系统相互作用、其共病和潜在治疗靶点。这项工作与化学信息学高度相关，因为构建化学和药物相关的知识图谱（包含分子、靶点、通路、疾病、副作用等实体及其关系）是化学大模型训练和推理的重要数据基础。此外，从文献中自动提取化学结构-性质关系、反应条件或谱图-结构关联，正是丰富化学知识图谱、支持质谱结构推理系统的重要途径。论文展示的从文本到KG的流水线为化学领域类似工作提供了方法参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Alkaptonuria (AKU) is an ultra-rare autosomal recessive metabolic disorder caused by mutations in the HGD (Homogentisate 1,2-Dioxygenase) gene, leading to a pathological accumulation of homogentisic acid (HGA) in body fluids and tissues. This leads to systemic manifestations, including premature spondyloarthropathy, renal and prostatic stones, and cardiovascular complications. Being ultra-rare, the amount of data related to the disease is limited, both in terms of clinical data and literature. Knowledge graphs (KGs) can help connect the limited knowledge about the disease (basic mechanisms, manifestations and existing therapies) with other knowledge; however, AKU is frequently underrepresented or entirely absent in existing biomedical KGs. In this work, we apply a text-mining methodology based on PubTator3 for large-scale extraction of biomedical relations. We construct two KGs of different sizes, validate them using existing biochemical knowledge and use them to extract genes, diseases and therapies possibly related to AKU. This computational framework reveals the systemic interactions of the disease, its comorbidities, and potential therapeutic targets, demonstrating the efficacy of our approach in analyzing rare metabolic disorders.

</details>

---

### 9. [Embedding-Aware Feature Discovery: Bridging Latent Representations and Interpretable Features in Event Sequences](https://arxiv.org/abs/2603.15713)

**基本信息**

- 🔗 arXiv: [`2603.15713`](https://arxiv.org/abs/2603.15713)
- 👥 作者: Artem Sakhno, Ivan Sergeev, Alexey Shestov 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15713.pdf)

**💡 相关性分析**

满足标准1：论文提出的EAFD框架核心是桥接学习嵌入与可解释特征，并利用LLM进行特征发现。这一方法论直接适用于化学信息学和质谱分析，旨在提升分子或谱图表示的效能，并可能生成新的、可解释的化学描述符或谱图特征，从而增强相关模型的性能和可解释性。

**📖 中文摘要**

本文介绍了嵌入感知特征发现，一个统一框架，通过将预训练的事件序列嵌入与自反思的LLM驱动特征生成代理耦合，来弥合学习到的嵌入与基于特征的管道之间的差距。EAFD迭代地从原始事件序列中发现、评估和精炼特征，使用两个互补的标准：对齐（解释嵌入中已编码的信息）和互补性（识别嵌入中缺失的预测信号）。在工业和开源交易基准测试中，EAFD consistently outperforms embedding-only and feature-based baselines。在化学信息学和质谱分析中，同样存在“嵌入（如分子图神经网络嵌入、质谱潜在表示）与手工特征（如分子描述符、谱图指纹）”之间的鸿沟。EAFD框架为解决这一问题提供了新思路：利用LLM的推理能力，从原始数据（分子SMILES、质谱峰列表）中自动发现既与学习到的嵌入对齐、又能提供互补信息的新特征，从而可能提升下游任务（如性质预测、结构鉴定）的性能。这为增强化学大模型和质谱推理模型的表示能力和可解释性提供了创新方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Industrial financial systems operate on temporal event sequences such as transactions, user actions, and system logs. While recent research emphasizes representation learning and large language models, production systems continue to rely heavily on handcrafted statistical features due to their interpretability, robustness under limited supervision, and strict latency constraints. This creates a persistent disconnect between learned embeddings and feature-based pipelines. We introduce Embedding-Aware Feature Discovery (EAFD), a unified framework that bridges this gap by coupling pretrained event-sequence embeddings with a self-reflective LLM-driven feature generation agent. EAFD iteratively discovers, evaluates, and refines features directly from raw event sequences using two complementary criteria: \emph{alignment}, which explains information already encoded in embeddings, and \emph{complementarity}, which identifies predictive signals missing from them. Across both open-source and industrial transaction benchmarks, EAFD consistently outperforms embedding-only and feature-based baselines, achieving relative gains of up to $+5.8\%$ over state-of-the-art pretrained embeddings, resulting in new state-of-the-art performance across event-sequence datasets.

</details>

---

### 10. [A Framework and Prototype for a Navigable Map of Datasets in Engineering Design and Systems Engineering](https://arxiv.org/abs/2603.15722)

**基本信息**

- 🔗 arXiv: [`2603.15722`](https://arxiv.org/abs/2603.15722)
- 👥 作者: H. Sinan Bank, Daniel R. Herber
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15722.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了一个用于系统化组织、分类和发现领域数据集的框架和原型。这为化学信息学和质谱分析领域构建类似的数据集资源导航系统提供了重要的方法论指导和设计范例，属于数据资源相关的主题。同时，论文对数据格局的分析和挑战的讨论也具有综述和展望的性质。

**📖 中文摘要**

本文提出了一个用于工程设计与系统工程中数据集导航地图的系统框架和原型。该框架基于一个多维分类法构建，用于按领域、生命周期阶段、数据类型和格式对工程数据集进行分类，从而实现分面发现。该框架采用知识图谱数据模型来捕获数据集、工具和出版物之间丰富的语义关系。论文分析了当前数据格局，揭示了早期设计阶段的“数据荒漠”和预测性维护等领域的“数据绿洲”。这项工作虽然面向工程设计，但其核心问题——如何系统化地组织、分类、发现和访问特定科学领域的异构数据集——与化学信息学和质谱分析领域面临的数据挑战完全一致。构建一个“化学数据集导航地图”或“质谱数据集导航地图”，对于促进数据共享、加速模型开发（尤其是化学大模型的预训练）、以及支持可重复研究至关重要。论文提出的分类法、知识图谱架构和交互式发现工具原型，为在化学领域构建类似社区资源提供了直接的设计蓝图和参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The proliferation of data across the system lifecycle presents both a significant opportunity and a challenge for Engineering Design and Systems Engineering (EDSE). While this ``digital thread'' has the potential to drive innovation, the fragmented and inaccessible nature of existing datasets hinders method validation, limits reproducibility, and slows research progress. Unlike fields such as computer vision and natural language processing, which benefit from established benchmark ecosystems, engineering design research often relies on small, proprietary, or ad-hoc datasets. This paper addresses this challenge by proposing a systematic framework for a ``Map of Datasets in EDSE.'' The framework is built upon a multi-dimensional taxonomy designed to classify engineering datasets by domain, lifecycle stage, data type, and format, enabling faceted discovery. An architecture for an interactive discovery tool is detailed and demonstrated through a working prototype, employing a knowledge graph data model to capture rich semantic relationships between datasets, tools, and publications. An analysis of the current data landscape reveals underrepresented areas (``data deserts'') in early-stage design and system architecture, as well as relatively well-represented areas (``data oases'') in predictive maintenance and autonomous systems. The paper identifies key challenges in curation and sustainability and proposes mitigation strategies, laying the groundwork for a dynamic, community-driven resource to accelerate data-centric engineering research.

</details>

---

### 11. [Morphemes Without Borders: Evaluating Root-Pattern Morphology in Arabic Tokenizers and LLMs](https://arxiv.org/abs/2603.15773)

**基本信息**

- 🔗 arXiv: [`2603.15773`](https://arxiv.org/abs/2603.15773)
- 👥 作者: Yara Alakeel, Chatrine Qwaider, Hanan Aldarmaki 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15773.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（标记化方案对模型捕捉和生成底层结构能力的影响）与化学信息学中化学大模型的基础问题直接相关，即如何为分子序列（SMILES, SELFIES）设计最佳的标记化策略以优化模型对化学结构的理解和生成。

**📖 中文摘要**

本文研究了大型语言模型及其标记化方案如何有效表示和生成阿拉伯语词根-模式形态，探究它们是捕获了真正的形态结构还是依赖于表面记忆。研究首先评估了阿拉伯语和多语言标记器在黄金标准分割上的形态保真度，然后使用新开发的测试集分析了LLM在生成性词根-模式生成中的性能。研究发现在七个以阿拉伯语为中心和多语言的LLM及其各自的标记器中，标记器的形态对齐对于形态生成既非必要也非充分，这质疑了形态标记化在下游性能中的作用。这项研究虽然聚焦于语言学，但其核心科学问题——标记化方案如何影响模型对底层结构（如形态）的捕捉和生成能力——与化学信息学中一个根本性问题高度相关：对于化学大模型，不同的分子字符串标记化方案（如基于SMILES字符、基于SELFIES令牌、基于子词或基于化学子结构）如何影响模型对分子语法和语义（化学结构）的理解、生成和推理能力？论文提供的评估框架（分析标记化对齐、生成任务）可直接启发化学领域对分子表示标记化的系统性研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work investigates how effectively large language models (LLMs) and their tokenization schemes represent and generate Arabic root-pattern morphology, probing whether they capture genuine morphological structure or rely on surface memorization. Arabic morphological system provides a rich testbed for analyzing how LLMs handle complex, non-concatenative forms and how tokenization choices influence this process. Our study begins with an evaluation of morphological fidelity across Arabic and multilingual tokenizers against gold-standard segmentation, followed by an analysis of LLM performance in productive root-pattern generation using a newly developed test set. Our findings across seven Arabic-centric and multilingual LLMs and their respective tokenizers reveal that tokenizer morphological alignment is not necessary nor sufficient for morphological generation, which questions the role of morphological tokenization in downstream performance.

</details>

---

### 12. [Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs](https://arxiv.org/abs/2603.15803)

**基本信息**

- 🔗 arXiv: [`2603.15803`](https://arxiv.org/abs/2603.15803)
- 👥 作者: Linrui Ma, Yufei Cui, Kai Han 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15803.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种针对离散扩散模型训练的新型噪声调度策略，旨在优化模型对序列中信息密集区域的学习。这一方法论创新可直接应用于训练用于分子生成或质谱图生成的化学扩散模型，以提升其性能，因此与化学大模型（特别是生成模型）的研究主题直接相关。

**📖 中文摘要**

本文针对离散扩散语言模型，提出了一种信息密度驱动的智能噪声调度器。通过提取信息密集的枢纽并应用互补优先级掩码，该方法将单个训练实例解耦为相互增强的推理和语法样本，迫使模型掌握逻辑演绎和基础序列结构。实验表明，该方法在四个代码和数学推理基准测试中平均准确率提高了约4%，显著优于均匀基线。机理分析进一步表明，概率优先级掩码有效缓解了块扩散训练期间的上下文崩溃。总体而言，这种密度感知策略以最小的标注成本有效释放了扩散语言模型的推理潜力。虽然论文主要评估领域是代码和数学，但其提出的“针对序列非均匀信息密度优化扩散模型噪声调度”的核心思想，对于训练用于化学序列（如分子SMILES）或质谱序列（峰列表）生成的扩散模型具有重要的借鉴意义。化学序列同样具有高度非均匀的信息密度（例如，分子中的关键官能团区域、质谱中的特征碎片峰），论文的方法可能有助于提升化学扩散模型生成分子的有效性、多样性或质谱模拟的准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete diffusion models offer global context awareness and flexible parallel generation. However, uniform random noise schedulers in standard DLLM training overlook the highly non-uniform information density inherent in real-world sequences. This wastes optimization resources on low-density structural glues while leaving high-density logical pivot points severely under-optimized. To address this, we propose an Information Density Driven Smart Noise Scheduler. By extracting information-dense hubs and applying Complementary Priority Masking, our method decouples a single training instance into mutually reinforcing reasoning and syntax samples, forcing the model to master both logical deduction and foundational sequence structure. Experiments demonstrate that our approach improves average accuracy by ~4\% across four Code and Math reasoning benchmarks, significantly outperforming uniform baselines. Mechanistic analyses further reveal that probabilistic priority masking effectively mitigates contextual collapse during block diffusion training. Overall, this density-aware strategy efficiently unlocks the reasoning potential of diffusion language models at minimal annotation cost, emerging as a promising new masked data training paradigm for Diffusion LLMs. Our processed dataset can be found at this https URL .

</details>

---

### 13. [INSTRUMENTAL: Automatic Synthesizer Parameter Recovery from Audio via Evolutionary Optimization](https://arxiv.org/abs/2603.15905)

**基本信息**

- 🔗 arXiv: [`2603.15905`](https://arxiv.org/abs/2603.15905)
- 👥 作者: Philipp Bogdan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15905.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究问题是从观测信号（音频）中逆向推断产生该信号的设备参数（合成器设置）。这本质上是一个“结构推理”问题，与“质谱结构推理”从质谱数据推断分子结构的核心任务直接相关，属于同一类逆向问题求解范式。

**📖 中文摘要**

本文提出了Instrumental系统，通过将可微分的28参数减法合成器与无导数进化优化器（CMA-ES）耦合，从音频中恢复连续的合成器参数。该系统优化了一个结合梅尔尺度STFT、频谱质心和MFCC散度的复合感知损失函数。这项工作专注于从音频信号中逆向工程出生成该音频的仪器参数，这是一个典型的“逆向设计”或“结构推理”问题。虽然应用领域是音频合成，但其核心问题——从观测数据（音频）反推生成该数据的底层系统参数（合成器设置）——与“质谱结构推理”从质谱数据反推分子结构的逻辑完全一致。论文中使用的优化框架和评估方法（匹配损失）也为质谱领域的类似问题提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing audio-to-MIDI tools extract notes but discard the timbral characteristics that define an instrument's identity. We present Instrumental, a system that recovers continuous synthesizer parameters from audio by coupling a differentiable 28-parameter subtractive synthesizer with CMA-ES, a derivative-free evolutionary optimizer. We optimize a composite perceptual loss combining mel-scaled STFT, spectral centroid, and MFCC divergence, achieving a matching loss of 2.09 on real recorded audio. We systematically evaluate eight hypotheses for improving convergence and find that only parametric EQ boosting yields meaningful improvement. Our results show that CMA-ES outperforms gradient descent on this non-convex landscape, that more parameters do not monotonically improve matching, and that spectral analysis initialization accelerates convergence over random starts.

</details>

---

### 14. [Bayesian-guided inverse design of hyperelastic microstructures: Application to stochastic metamaterials](https://arxiv.org/abs/2603.15917)

**基本信息**

- 🔗 arXiv: [`2603.15917`](https://arxiv.org/abs/2603.15917)
- 👥 作者: Hooman Danesh, Henning Wessels
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15917.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是“逆向设计”框架，即从目标性能出发寻找最优微观结构设计。这本质上与“化学大模型”中的分子逆向设计（给定目标性质，生成或搜索分子结构）是同一类问题。论文中使用的贝叶斯优化、主动学习、代理模型等方法也是化学信息学中解决类似问题的常用技术。

**📖 中文摘要**

本文提出了一个贝叶斯引导的逆向设计框架，用于从大量候选结构中识别出能够实现目标宏观应力响应的超弹性微结构。该框架通过统计特征工程降低设计变体的维度，并使用多输出高斯过程代理模型将低维描述符映射到宏观超弹性响应的有效本构参数。代理模型在严格的预算约束下通过不确定性驱动的主动学习进行训练。在数值测试中，该方法仅需标注完整数据集的不到0.5%，就能在未见过的载荷条件下达到预设的误差阈值。这项工作展示了如何结合降维、代理模型和主动学习来解决高成本Oracle（如计算均质化或实验）评估下的逆向设计问题。虽然应用在力学超材料，但其“给定目标性能，寻找最优设计”的逆向设计范式，以及处理高维设计空间和昂贵评估的方法，与“化学大模型”和“质谱结构推理”中的分子逆向设计（给定性质，寻找分子）或分子生成问题在方法论上高度相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

From a given pool of all feasible design variants, our aim is to identify a structure that achieves a target macroscopic stress response. For each candidate design, the response is obtained from a high-fidelity oracle, in particular, time- and resource-intensive computational homogenization or experiments. We consider the case where (i) the geometry cannot be conveniently parameterized, rendering gradient-based optimization inapplicable, and (ii) brute-force evaluation of all candidates is infeasible due to the cost of oracle queries. To tackle this challenge, we propose a Bayesian-guided inverse design framework that proceeds as follows. First, the dimensionality of the design variants is reduced through statistical feature engineering, and the resulting low-dimensional descriptors are mapped to effective constitutive parameters describing the macroscopic hyperelastic response. This mapping is modeled using a multi-output Gaussian process surrogate that accounts for correlations between the parameters. The surrogate is trained using uncertainty-driven active learning under severe budget constraints, allowing only a very limited number of high-fidelity oracle evaluations. Based on surrogate predictions, a finite number of promising candidates are shortlisted. Since the surrogate accuracy is inherently limited, the final selection of the optimal design is performed through high-fidelity oracle evaluations within the shortlist. In numerical test cases, we consider a dataset of 50,000 candidate structures. Active learning requires labeling less than half a percent of the full dataset. Bayesian-guided inverse design under unseen loading conditions reaches a prescribed error threshold with only a handful of oracle evaluations in the majority of cases.

</details>

---

### 15. [Generative Inverse Design with Abstention via Diagonal Flow Matching](https://arxiv.org/abs/2603.15925)

**基本信息**

- 🔗 arXiv: [`2603.15925`](https://arxiv.org/abs/2603.15925)
- 👥 作者: Miguel de Campos, Werner Krebs, Hanno Gottschalk
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是“生成式逆向设计”，提出了改进的流匹配方法（Diag-CFM）来学习从性能到设计参数的映射。这直接对应“化学大模型”中的一个核心子领域：分子生成与逆向设计，即从所需的化学或物理性质出发，生成符合条件的分子结构。

**📖 中文摘要**

本文研究了逆向设计问题，即寻找能够实现目标性能的设计参数。生成式方法学习设计与标签之间的双向映射，从而实现多样化的解决方案采样。论文引入了Diagonal Flow Matching（Diag-CFM）方法，通过零锚定策略解决了标准条件流匹配在适应逆向问题时对参数排序和缩放敏感的问题。该方法在高达P=100的设计维度上，相比基线方法在往返精度上实现了数量级的提升。论文还开发了两种架构固有的不确定性度量，实现了三种实用能力：从多个生成结果中选择最佳候选、放弃不可靠的预测以及检测分布外目标。这项工作专注于生成式逆向设计方法，其核心目标（学习从性能空间到设计空间的映射）与“化学大模型”中的分子生成与优化任务完全一致。论文提出的改进流匹配的方法和不确定性处理技术，对化学领域类似的逆向设计问题（如基于性质的分子生成）具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse design aims to find design parameters $x$ achieving target performance $y^*$. Generative approaches learn bidirectional mappings between designs and labels, enabling diverse solution sampling. However, standard conditional flow matching (CFM), when adapted to inverse problems by pairing labels with design parameters, exhibits strong sensitivity to their arbitrary ordering and scaling, leading to unstable training. We introduce Diagonal Flow Matching (Diag-CFM), which resolves this through a zero-anchoring strategy that pairs design coordinates with noise and labels with zero, making the learning problem provably invariant to coordinate permutations. This yields order-of-magnitude improvements in round-trip accuracy over CFM and invertible neural network baselines across design dimensions up to $P{=}100$. We develop two architecture-intrinsic uncertainty metrics, Zero-Deviation and Self-Consistency, that enable three practical capabilities: selecting the best candidate among multiple generations, abstaining from unreliable predictions, and detecting out-of-distribution targets; consistently outperforming ensemble and general-purpose alternatives across all tasks. We validate on airfoil, gas turbine combustor, and an analytical benchmark with scalable design dimension.

</details>

---

### 16. [Discovery of interaction and diffusion kernels in particle-to-mean-field multi-agent systems](https://arxiv.org/abs/2603.15927)

**基本信息**

- 🔗 arXiv: [`2603.15927`](https://arxiv.org/abs/2603.15927)
- 👥 作者: Giacomo Albi, Alessandro Alla, Elisa Calzola
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15927.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从轨迹数据中学习多智能体系统的交互核（即动力学模型），这属于科学机器学习中“模型发现”的范畴。这与“化学大模型”主题中利用数据驱动方法发现或构建化学系统模型（如分子力场、反应动力学）的研究直接相关。

**📖 中文摘要**

本文提出了一个数据驱动框架，用于从随机多智能体系统的轨迹数据中学习交互核函数。该框架旨在直接从数据中识别非局部交互和扩散项的函数形式，而无需任何关于底层交互结构的先验知识。该问题被表述为一系列在由紧支撑基函数（如分段线性多项式）张成的结构化有限维空间中的稀疏回归任务。论文提出了两种互补的识别策略：基于随机批处理的采样和基于平均场近似的策略。该方法在包括有界置信度和吸引-排斥动力学在内的基准模型上得到了验证。这项工作属于“从数据中发现模型”的范畴，即利用机器学习方法从观测数据中推导出物理或化学系统的动力学方程。这与“化学大模型”中利用数据驱动方法构建或理解复杂化学系统模型的目标密切相关，也为从质谱时间序列或分子动力学模拟数据中学习相互作用规律提供了方法论启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a data-driven framework to learn interaction kernels in stochastic multi-agent systems. Our approach aims at identifying the functional form of nonlocal interaction and diffusion terms directly from trajectory data, without any a priori knowledge of the underlying interaction structure. Starting from a discrete stochastic binary-interaction model, we formulate the inverse problem as a sequence of sparse regression tasks in structured finite-dimensional spaces spanned by compactly supported basis functions, such as piecewise linear polynomials. In particular, we assume that pairwise interactions between agents are not directly observed and that only limited trajectory data are available. To address these challenges, we propose two complementary identification strategies. The first based on random-batch sampling, which compensates for latent interactions while preserving the statistical structure of the full dynamics in expectation. The second based on a mean-field approximation, where the empirical particle density reconstructed from the data defines a continuous nonlocal regression problem. Numerical experiments demonstrate the effectiveness and robustness of the proposed framework, showing accurate reconstruction of both interaction and diffusion kernels even from partially observed. The method is validated on benchmark models, including bounded-confidence and attraction-repulsion dynamics, where the two proposed strategies achieve comparable levels of accuracy.

</details>

---

### 17. [Nodule-Aligned Latent Space Learning with LLM-Driven Multimodal Diffusion for Lung Nodule Progression Prediction](https://arxiv.org/abs/2603.15932)

**基本信息**

- 🔗 arXiv: [`2603.15932`](https://arxiv.org/abs/2603.15932)
- 👥 作者: James Song, Yifan Wang, Chuan Zhou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15932.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（结合扩散模型和LLM进行多模态数据生成与推理，以预测生物实体进展）与“化学大模型”和“质谱结构推理”中利用复杂模型处理高维科学数据、进行结构或状态推理的核心主题高度相关。

**📖 中文摘要**

本文提出了NAMD框架，用于通过生成一年后的随访结节CT图像来预测肺结节进展。该框架引入了结节对齐的潜在空间，并利用LLM驱动的控制机制，将扩散主干网络以患者数据为条件。在NLST数据集上的实验表明，该方法合成的随访图像在肺癌恶性预测任务上取得了有竞争力的性能。这项工作展示了如何将大型生成模型（扩散模型）与语言模型（LLM）结合，用于处理复杂的化学信息学/医学影像分析任务，即从多模态数据（CT影像和电子健康记录）中推理生物实体的状态变化。虽然应用领域是医学，但其方法论（多模态生成模型、潜在空间对齐、LLM条件控制）与“化学大模型”和“质谱结构推理”中处理复杂、高维数据并推理其潜在结构的核心挑战有很强的概念相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early diagnosis of lung cancer is challenging due to biological uncertainty and the limited understanding of the biological mechanisms driving nodule progression. To address this, we propose Nodule-Aligned Multimodal (Latent) Diffusion (NAMD), a novel framework that predicts lung nodule progression by generating 1-year follow-up nodule computed tomography images with baseline scans and the patient's and nodule's Electronic Health Record (EHR). NAMD introduces a nodule-aligned latent space, where distances between latents directly correspond to changes in nodule attributes, and utilizes an LLM-driven control mechanism to condition the diffusion backbone on patient data. On the National Lung Screening Trial (NLST) dataset, our method synthesizes follow-up nodule images that achieve an AUROC of 0.805 and an AUPRC of 0.346 for lung nodule malignancy prediction, significantly outperforming both baseline scans and state-of-the-art synthesis methods, while closely approaching the performance of real follow-up scans (AUROC: 0.819, AUPRC: 0.393). These results demonstrate that NAMD captures clinically relevant features of lung nodule progression, facilitating earlier and more accurate diagnosis.

</details>

---

### 18. [Data-Local Autonomous LLM-Guided Neural Architecture Search for Multiclass Multimodal Time-Series Classification](https://arxiv.org/abs/2603.15939)

**基本信息**

- 🔗 arXiv: [`2603.15939`](https://arxiv.org/abs/2603.15939)
- 👥 作者: Emil Hardarson, Luka Biedebach, Ómar Bessi Ómarsson 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15939.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个在数据本地化约束下、由LLM引导的自动化机器学习管道搜索框架。这体现了“化学大模型”中“AI for Science”的一个关键方向：利用AI模型（如LLM）自动化科学发现流程，包括实验设计、模型选择和优化，尤其是在数据受限或隐私敏感的化学研究场景中。

**📖 中文摘要**

本文提出了一种新颖的、数据本地的、LLM引导的神经架构搜索（NAS）框架，用于多类别多模态时间序列分类。该框架在隐私受限的场景（如医院开发患者脑电图模型）下，远程处理候选管道，同时在固定协议下本地执行所有训练和评估。控制器仅观察试验级别的摘要（如管道描述符、指标、学习曲线统计数据和失败日志），而从不访问原始样本或中间特征表示。该框架通过针对每个类别和模态的“一对多”二元专家、一个轻量级融合MLP以及对专家架构和模态特定预处理的联合搜索，来定位多类别、多模态学习。这项工作展示了如何在严格的数据本地化约束下，利用LLM引导的自动化流程来优化机器学习管道（包括架构和预处理）。虽然应用在时间序列分类，但其“LLM引导的自动化实验设计”和“在隐私约束下进行模型搜索”的核心思想，与“化学大模型”中利用AI辅助进行实验设计、高通量筛选或模型优化的工作流高度相关，为解决化学信息学中类似的数据敏感和流程自动化问题提供了思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Applying machine learning to sensitive time-series data is often bottlenecked by the iteration loop: Performance depends strongly on preprocessing and architecture, yet training often has to run on-premise under strict data-local constraints. This is a common problem in healthcare and other privacy-constrained domains (e.g., a hospital developing deep learning models on patient EEG). This bottleneck is particularly challenging in multimodal fusion, where sensor modalities must be individually preprocessed and then combined. LLM-guided neural architecture search (NAS) can automate this exploration, but most existing workflows assume cloud execution or access to data-derived artifacts that cannot be exposed. We present a novel data-local, LLM-guided search framework that handles candidate pipelines remotely while executing all training and evaluation locally under a fixed protocol. The controller observes only trial-level summaries, such as pipeline descriptors, metrics, learning-curve statistics, and failure logs, without ever accessing raw samples or intermediate feature representations. Our framework targets multiclass, multimodal learning via one-vs-rest binary experts per class and modality, a lightweight fusion MLP, and joint search over expert architectures and modality-specific preprocessing. We evaluate our method on two regimes: UEA30 (public multivariate time-series classification dataset) and SleepEDFx sleep staging (heterogeneous clinical modalities such as EEG, EOG, and EMG). The results show that the modular baseline model is strong, and the LLM-guided NAS further improves it. Notably, our method finds models that perform within published ranges across most benchmark datasets. Across both settings, our method reduces manual intervention by enabling unattended architecture search while keeping sensitive data on-premise.

</details>

---

### 19. [Scientific Machine Learning-assisted Model Discovery from Telemetry Data](https://arxiv.org/abs/2603.15943)

**基本信息**

- 🔗 arXiv: [`2603.15943`](https://arxiv.org/abs/2603.15943)
- 👥 作者: Sebastian Micluta-Campeanu, Avinash Subramanian, Anas Abdelrehim 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15943.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（科学机器学习辅助的模型发现，从数据中学习符号表达式以增强物理模型）直接围绕“化学大模型”中利用数据和机器学习方法构建或增强模型的核心主题。

**📖 中文摘要**

本文提出了一种名为Dyad Model Discovery的半自动化方法，用于从数据中发现符号表达式，以增强物理模型的方程。该方法应用于运输制冷单元的数字孪生，利用遥测数据改进其预测性能。论文提出了一种工程师在环的工作流程，系统可以向用户提供建议，由用户决定接受或拒绝。这项工作被认为是首个AI辅助的工程设计工作流程，旨在解决当模型因简化假设过多而无法校准数据时的问题。该方法的核心是通过从数据中发现符号表达式来“增强”物理方程，这与“化学大模型”中利用数据驱动方法增强或构建模型的核心思想高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Calibration of dynamic models to data is an important step in building building digital twins of HVAC equipment, thermal loads and control systems. Sometimes, when a model fails to calibrate to data, a possible cause is that the model has made too many sim- plifying assumptions and is missing physics. In this paper we propose a semi-automated approach, called Dyad Model Discovery, that can augment the physical equations of the model with symbolic expressions discovered from the data. We demonstrate this method on a digital twin of a transportation refrigeration unit to improve its predictive performance, trained using telemetry data. An engineer-in-the-loop workflow is proposed, which provides suggestions to the user which can then be accepted or rejected. This is the first AI-assisted engineering design workflow to our knowledge.

</details>

---

### 20. [Protein Design with Agent Rosetta: A Case Study for Specialized Scientific Agents](https://arxiv.org/abs/2603.15952)

**基本信息**

- 🔗 arXiv: [`2603.15952`](https://arxiv.org/abs/2603.15952)
- 👥 作者: Jacopo Teneggi, S.M. Bargeen A. Turzo, Tanya Marwah 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15952.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于蛋白质设计的AI智能体（Agent Rosetta），它结合了LLM和专业的化学/生物分子设计软件。这直接围绕“化学大模型”的主题，即开发用于化学领域复杂任务（如分子设计）的AI模型或智能体。

**📖 中文摘要**

本文介绍了Agent Rosetta，这是一个将大语言模型（LLM）智能体与Rosetta（领先的基于物理的异质聚合物设计软件）结构化环境相结合的框架。该智能体能够迭代优化设计以实现用户定义的目标，将LLM的推理能力与Rosetta的通用性（如处理非经典氨基酸和几何结构的能力）结合起来。论文评估了Agent Rosetta在经典氨基酸设计（与专业模型和专家基线相当）和非经典残基设计（机器学习方法通常在此失效）上的性能。这项工作展示了如何通过精心设计的环境，使LLM智能体能够利用专业的科学软件（如Rosetta）执行复杂的科学任务（如蛋白质设计），这体现了构建领域专用“化学大模型”或科学智能体的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are capable of emulating reasoning and using tools, creating opportunities for autonomous agents that execute complex scientific tasks. Protein design provides a natural testbed: although machine learning (ML) methods achieve strong results, these are largely restricted to canonical amino acids and narrow objectives, leaving unfilled need for a generalist tool for broad design pipelines. We introduce Agent Rosetta, an LLM agent paired with a structured environment for operating Rosetta, the leading physics-based heteropolymer design software, capable of modeling non-canonical building blocks and geometries. Agent Rosetta iteratively refines designs to achieve user-defined objectives, combining LLM reasoning with Rosetta's generality. We evaluate Agent Rosetta on design with canonical amino acids, matching specialized models and expert baselines, and with non-canonical residues -- where ML approaches fail -- achieving comparable performance. Critically, prompt engineering alone often fails to generate Rosetta actions, demonstrating that environment design is essential for integrating LLM agents with specialized software. Our results show that properly designed environments enable LLM agents to make scientific software accessible while matching specialized tools and human experts.

</details>

---

### 21. [Sample-Efficient Adaptation of Drug-Response Models to Patient Tumors under Strong Biological Domain Shift](https://arxiv.org/abs/2603.16185)

**基本信息**

- 🔗 arXiv: [`2603.16185`](https://arxiv.org/abs/2603.16185)
- 👥 作者: Camille Jimenez Cortes, Philippe Lalanda, German Vega
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16185.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个机器学习框架，用于预测患者对药物的反应。这直接涉及化学信息学领域，即利用计算和数据分析方法解决化学和生物学问题（如药物发现和精准医疗）。

**📖 中文摘要**

本文提出了一种分阶段的迁移学习框架，用于解决药物反应预测中临床前细胞系数据与患者肿瘤数据之间的巨大生物学领域偏移问题。该框架首先利用大量未标记的药理基因组数据，通过基于自编码器的表示学习，独立学习细胞和药物的表示。然后，这些表示在细胞系数据上与药物反应标签进行对齐，最后使用少量样本监督将其适应到患者肿瘤数据上。研究表明，当源域和目标域（如细胞系与患者肿瘤）存在显著差异时，从无标签分子谱中学习结构化和可迁移的表示，可以大幅减少有效预测药物反应所需的临床监督数据量。这项工作为化学信息学中利用机器学习模型进行数据高效的临床前到临床转化提供了实用路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug response in patients from preclinical data remains a major challenge in precision oncology due to the substantial biological gap between in vitro cell lines and patient tumors. Rather than aiming to improve absolute in vitro prediction accuracy, this work examines whether explicitly separating representation learning from task supervision enables more sample-efficient adaptation of drug-response models to patient data under strong biological domain shift. We propose a staged transfer-learning framework in which cellular and drug representations are first learned independently from large collections of unlabeled pharmacogenomic data using autoencoder-based representation learning. These representations are then aligned with drug-response labels on cell-line data and subsequently adapted to patient tumors using few-shot supervision. Through a systematic evaluation spanning in-domain, cross-dataset, and patient-level settings, we show that unsupervised pretraining provides limited benefit when source and target domains overlap substantially, but yields clear gains when adapting to patient tumors with very limited labeled data. In particular, the proposed framework achieves faster performance improvements during few-shot patient-level adaptation while maintaining comparable accuracy to single-phase baselines on standard cell-line benchmarks. Overall, these results demonstrate that learning structured and transferable representations from unlabeled molecular profiles can substantially reduce the amount of clinical supervision required for effective drug-response prediction, offering a practical pathway toward data-efficient preclinical-to-clinical translation.

</details>

---

### 22. [Non-GRS type Euclidean and Hermitian LCD codes and Their Applications for EAQECCs](https://arxiv.org/abs/2603.16187)

**基本信息**

- 🔗 arXiv: [`2603.16187`](https://arxiv.org/abs/2603.16187)
- 👥 作者: Zhonghao Liang, Dongmei Huang, Qunying Liao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16187.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构造和分析具有特定代数结构（线性互补对偶）的纠错码。虽然主要属于编码理论，但其在量子通信和密码学中的应用与化学信息学中可能涉及的分子编码或安全数据传输等交叉领域有潜在关联。论文对非GRS型码的构造和分析也体现了对复杂结构推理的重视。

**📖 中文摘要**

本文研究了线性互补对偶码的构造及其在纠缠辅助量子纠错码中的应用。论文利用一类非GRS型线性码（广义Roth-Lempel码）构造了几类欧几里得LCD码、厄米特LCD码以及具有小维数壳的线性码。作为应用，本文获得了多个EAQECC族。论文还证明了对于k > ℓ的情况，GRL码是非GRS的。这项工作在编码理论领域，特别是在设计具有特定代数结构（如LCD属性）的纠错码方面做出了贡献，这些码在量子通信和密码学中具有应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, the construction of non-GRS type linear codes has attracted considerable attention due to that they can effectively resist both the Sidelnikov-Shestakov attack and the Wieschebrink attack. Constructing linear complementary dual (LCD) codes and determining the hull of linear codes have long been important topics in coding theory, as they play the crucial role in constructing entanglement-assisted quantum error-correcting codes (EAQECCs), certain communication systems and cryptography. In this paper, by utilizing a class of non-GRS type linear codes, namely, generalized Roth-Lempel (in short, GRL) codes, we firstly construct several classes of Euclidean LCD codes, Hermitian LCD codes, and linear codes with small-dimensional hulls, generalized the main results given by Wu et al. in 2021. We also present an upper bound for the number of a class of Euclidean GRL codes with 1-dimensional hull, and then for several classes of Hermitian GRL codes, we firstly derive an upper bound for the dimension of the hull, and prove that the bound is attainable. Secondly, as an application, we obtain several families of EAQECCs. Thirdly, we prove that the GRL code is non-GRS for $k >\ell$. Finally, some corresponding examples for LCD MDS codes and LCD NMDS codes are presented.

</details>

---

### 23. [Offline Exploration-Aware Fine-Tuning for Long-Chain Mathematical Reasoning](https://arxiv.org/abs/2603.16206)

**基本信息**

- 🔗 arXiv: [`2603.16206`](https://arxiv.org/abs/2603.16206)
- 👥 作者: Yongyu Mu, Jiali Zeng, Fandong Meng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16206.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大型语言模型在复杂数学推理任务上的训练方法。虽然主题是通用推理，但其重点关注的“长链推理”和“探索感知”微调策略，与“化学大模型”和“质谱结构推理”中所需的复杂、多步骤的分子结构解析和性质预测所面临的挑战高度相似。论文提出的方法对于训练用于科学推理（如化学信息学中的逆合成分析或质谱解析）的专用大模型具有直接的借鉴意义。

**📖 中文摘要**

本文提出了一种离线探索感知的监督微调方法，旨在提升大型语言模型在长链数学推理任务中的性能。该方法通过优化两个目标来调整SFT过程：一是促进低置信度但已验证正确的教师蒸馏数据，以吸收先前未捕获的推理模式；二是抑制高置信度但错误的自我蒸馏数据，将错误模式的概率质量重新分配给潜在正确的候选者。实验表明，该方法能有效提升初始策略的熵，并在后续的基于可验证奖励的强化学习训练中带来持续的性能增益。这项工作聚焦于改进模型在复杂推理任务（如数学推理）中的训练起点，强调了在微调阶段纳入探索性考量的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Through encouraging self-exploration, reinforcement learning from verifiable rewards (RLVR) has significantly advanced the mathematical reasoning capabilities of large language models. As the starting point for RLVR, the capacity of supervised fine-tuning (SFT) to memorize new chain-of-thought trajectories provides a crucial initialization that shapes the subsequent exploration landscape. However, existing research primarily focuses on facilitating exploration during RLVR training, leaving exploration-aware SFT under-explored. To bridge this gap, we propose Offline eXploration-Aware (OXA) fine-tuning. Specifically, OXA optimizes two objectives: promoting low-confidence verified teacher-distillation data to internalize previously uncaptured reasoning patterns, and suppressing high-confidence incorrect self-distillation data to redistribute probability mass of incorrect patterns toward potentially correct candidates. Experimental results across 6 benchmarks show that OXA consistently improves mathematical reasoning performance, especially achieving an average gain of $+6$ Pass@1 and $+5$ Pass@$k$ points compared to conventional SFT on the Qwen2.5-1.5B-Math. Crucially, OXA elevates initial policy entropy, and performance gains persist throughout extensive RLVR training, demonstrating the long-term value of OXA.

</details>

---

### 24. [Capability-Guided Compression: Toward Interpretability-Aware Budget Allocation for Large Language Models](https://arxiv.org/abs/2603.16440)

**基本信息**

- 🔗 arXiv: [`2603.16440`](https://arxiv.org/abs/2603.16440)
- 👥 作者: Rishaank Gupta
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16440.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大语言模型的压缩和组件功能分析，这属于“化学大模型”主题中模型架构、性能评估和优化的重要方面。

**📖 中文摘要**

本文提出了能力引导压缩（CGC）框架，旨在解决大语言模型压缩中存在的“能力盲压缩”问题。该框架利用稀疏自编码器（SAE）导出的能力密度图，为Transformer模型的不同组件分配差异化的压缩预算。能力密度是一个结合了特征广度、激活熵和跨输入一致性的标量度量。作者从理论上证明，具有更高能力密度的组件表现出更低的结构冗余，并在更低的压缩比下达到其个体相变点。实验在GPT-2 Medium上进行，表明能力密度与现有的Wanda重要性评分正交，是一个新颖的压缩信号。这项工作为大语言模型压缩提供了一个新的理论框架和评估视角，与“化学大模型”主题中模型架构优化和性能评估的核心问题直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model compression has made substantial progress through pruning, quantization, and low-rank decomposition, yet a fundamental limitation persists across all existing methods: compression budgets are allocated without any representation of what individual model components functionally encode. We term this the capability-blind compression problem and argue it is a root cause of two well-documented failures -- the insensitivity of perplexity-based evaluation to reasoning capability loss, and the abrupt phase transitions in model performance recently characterized by Ma et al. (2026). We propose Capability-Guided Compression (CGC), a framework that addresses this by using Sparse Autoencoder (SAE)-derived capability density maps to allocate differential compression budgets across transformer components. Capability density is a formally defined scalar measure combining the feature breadth, activation entropy, and cross-input consistency of a component's SAE feature activation distribution. We prove theoretically that components with higher capability density exhibit lower structural redundancy and reach their individual phase transition points at lower compression ratios, providing the first pre-compression mechanism for component-level phase transition prediction. Experiments on GPT-2 Medium confirm that capability density is statistically independent of Wanda importance scores (Spearman rho = -0.054, n = 384 heads), establishing it as a genuinely novel compression signal orthogonal to all existing importance metrics. We report a negative result on PPL-based compression comparison and provide a principled diagnosis identifying GPT-2 Medium as an insufficient test bed for the full CGC hypothesis. The theoretical framework, density formalism, and orthogonality finding constitute a foundation for capability-aware compression research.

</details>

---

### 25. [An approximate graph elicits detonation lattice](https://arxiv.org/abs/2603.16524)

**基本信息**

- 🔗 arXiv: [`2603.16524`](https://arxiv.org/abs/2603.16524)
- 👥 作者: Vansh Sharma, Venkat Raman
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16524.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用图论算法对爆轰实验/模拟产生的复杂3D数据进行分割和分析。这属于“化学信息学”中利用计算方法处理和分析化学/物理系统数据的范畴。

**📖 中文摘要**

本研究提出了一种基于图论的新算法，用于从3D压力痕迹（称为爆轰晶格）中对爆轰单元进行精确分割和测量。该算法旨在解决该领域中手动和原始2D边缘检测方法的局限性。通过使用分割模型，这种无需训练的方法能够准确提取细胞模式。研究首先在生成数据上展示了分割效果，预测误差为2%。然后使用3D模拟数据来验证基于图的工作流程的性能。统计和联合概率密度结果表明，细胞沿波传播轴方向呈椭圆形排列，偏差为17%。该框架具有鲁棒性，其基于图的公式适用于不同的细胞几何形状，使其成为爆轰分析的实用工具。这项工作展示了图论和算法在复杂物理现象（爆轰）数据分析中的应用，与“化学信息学”中利用计算和算法处理复杂化学/物理数据的主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study presents a novel algorithm based on graph theory for the precise segmentation and measurement of detonation cells from 3D pressure traces, termed detonation lattices, addressing the limitations of manual and primitive 2D edge detection methods prevalent in the field. Using a segmentation model, the proposed training-free algorithm is designed to accurately extract cellular patterns, a longstanding challenge in detonations research. First, the efficacy of segmentation on generated data is shown with a prediction error 2%. Next, 3D simulation data is used to establish performance of the graph-based workflow. The results of statistics and joint probability densities show oblong cells aligned with the wave propagation axis with 17% deviation, whereas larger dispersion in volume reflects cubic amplification of linear variability. Although the framework is robust, it remains challenging to reliably segment and quantify highly complex cellular patterns. However, the graph-based formulation generalizes across diverse cellular geometries, positioning it as a practical tool for detonation analysis and a strong foundation for future extensions in triple-point collision studies.

</details>

---

### 26. [Manifold-Matching Autoencoders](https://arxiv.org/abs/2603.16568)

**基本信息**

- 🔗 arXiv: [`2603.16568`](https://arxiv.org/abs/2603.16568)
- 👥 作者: Laurent Cheret, Vincent Létourneau, Isar Nejadgholi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16568.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是数据表示学习和流形对齐，这是“化学信息学”中分子表示、降维和特征学习的基础性方法。MMAE作为一种新颖的正则化方法，对于学习化学数据的低维表示具有直接相关性。

**📖 中文摘要**

本文研究了一种称为流形匹配（MMAE）的简单无监督自编码器正则化方案：通过最小化均方误差，将潜在空间中的成对距离与输入数据空间中的成对距离对齐。由于对齐发生在成对距离而非坐标上，该方法也可以扩展到数据的低维表示，增加了方法的灵活性。作者发现，这种正则化在基于最近邻距离保持和基于持续同源性度量的指标上优于类似方法。他们还观察到MMAE提供了多维缩放（MDS）的可扩展近似。该方法是一种通用的数据表示学习技术，对于“化学信息学”中分子表示学习、降维和特征提取具有潜在应用价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study a simple unsupervised regularization scheme for autoencoders called Manifold-Matching (MMAE): we align the pairwise distances in the latent space to those of the input data space by minimizing mean squared error. Because alignment occurs on pairwise distances rather than coordinates, it can also be extended to a lower-dimensional representation of the data, adding flexibility to the method. We find that this regularization outperforms similar methods on metrics based on preservation of nearest-neighbor distances and persistent homology-based measures. We also observe that MMAE provides a scalable approximation of Multi-Dimensional Scaling (MDS).

</details>

---

### 27. [Deep Tabular Representation Corrector](https://arxiv.org/abs/2603.16569)

**基本信息**

- 🔗 arXiv: [`2603.16569`](https://arxiv.org/abs/2603.16569)
- 👥 作者: Hangting Ye, Peng Wang, Wei Fan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16569.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是表格数据的深度表示学习和模型增强，这是“化学信息学”中处理分子描述符表格、进行定量构效关系（QSAR）建模等任务的核心技术。TRC方法对于提升化学表格数据模型的性能具有直接相关性。

**📖 中文摘要**

本文介绍了深度表格表示校正器（TRC），这是一种以模型无关的方式增强任何已训练的深度表格模型表示的方法，而无需更改其参数。具体来说，针对阻碍预测的表征偏移和表征冗余，作者提出了两个任务：（i）表格表示重估计，训练一个偏移估计器来计算表格表示的内在偏移并随后减轻它，从而重估计表示；（ii）表格空间映射，通过坐标估计器将上述重估计的表示转换到轻量嵌入向量空间，同时保留关键的预测信息以最小化冗余。这两个任务共同增强了深度表格模型的表示，且不触及原始模型，因此效率很高。最后，作者在各种表格基准上对最先进的深度表格机器学习模型与TRC结合进行了广泛实验，结果显示出持续的优势。这项工作为表格数据的深度表示学习提供了新工具，与“化学信息学”中处理分子属性表格数据、QSAR建模等任务直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tabular data have been playing a mostly important role in diverse real-world fields, such as healthcare, engineering, finance, etc. The recent success of deep learning has fostered many deep networks (e.g., Transformer, ResNet) based tabular learning methods. Generally, existing deep tabular machine learning methods are along with the two paradigms, i.e., in-learning and pre-learning. In-learning methods need to train networks from scratch or impose extra constraints to regulate the representations which nonetheless train multiple tasks simultaneously and make learning more difficult, while pre-learning methods design several pretext tasks for pre-training and then conduct task-specific fine-tuning, which however need much extra training effort with prior knowledge. In this paper, we introduce a novel deep Tabular Representation Corrector, TRC, to enhance any trained deep tabular model's representations without altering its parameters in a model-agnostic manner. Specifically, targeting the representation shift and representation redundancy that hinder prediction, we propose two tasks, i.e., (i) Tabular Representation Re-estimation, that involves training a shift estimator to calculate the inherent shift of tabular representations to subsequently mitigate it, thereby re-estimating the representations and (ii) Tabular Space Mapping, that transforms the above re-estimated representations into a light-embedding vector space via a coordinate estimator while preserves crucial predictive information to minimize redundancy. The two tasks jointly enhance the representations of deep tabular models without touching on the original models thus enjoying high efficiency. Finally, we conduct extensive experiments on state-of-the-art deep tabular machine learning models coupled with TRC on various tabular benchmarks which have shown consistent superiority.

</details>

---

### 28. [Reasoning About Variability Models Through Network Analysis](https://arxiv.org/abs/2603.16577)

**基本信息**

- 🔗 arXiv: [`2603.16577`](https://arxiv.org/abs/2603.16577)
- 👥 作者: Jose Manuel Sanchez, Miguel Angel Olivero, Ruben Heradio 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16577.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用图论和网络分析来研究复杂系统（软件特征模型）的结构。这种方法论与“化学信息学”中分析分子图、化学网络和系统结构（如分子相似性、反应路径分析）的核心技术直接相关，属于同一类计算方法。

**📖 中文摘要**

本文从网络分析的角度，对软件可变性模型中广泛使用的特征模型的结构特性进行了大规模系统性研究。作者分析了来自20个仓库的5,709个模型的数据集，这些模型跨越多个应用领域，规模各异。通过计算特征之间传递依赖和冲突的图，研究结果揭示了一致的结构特征（例如，依赖关系占主导地位、存在高度中心化的特征、或特征性的节点度分布）以及显著的领域特异性偏差。这些发现有助于识别与维护相关的特征、模块化分解的机会以及结构脆弱性的指标。该方法为可变性模型的实证分析提供了一个可扩展的、基于图的基础，并为其结构和演化的未来研究提供了定量证据。虽然主题是软件工程，但其核心方法论——使用图论和网络分析来理解和表征复杂系统的结构——与“化学信息学”中分析分子图、反应网络或化学系统的结构特性在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Feature models are widely used to capture the configuration space of software systems. Although automated reasoning has been studied for detecting problematic features and supporting configuration tasks, significantly less attention has been given to the systematic study of the structural properties of feature models at scale. The approach fills this gap by examining the models' structure through a network analysis perspective. We focus on three Research Questions concerning (i) the structural patterns exhibited by these graphs, (ii) the extent to which such patterns vary across domains and model sources, and (iii) the usefulness of network-based indicators for understanding, maintaining, and evolving variability models. To answer these questions, we analyze a dataset of 5,709 models from 20 repositories, spanning multiple application domains and varying sizes (ranging from 99 to 35,907 variables on their Boolean translation). To do so, graphs of transitive dependencies and conflicts between features are computed. Our results reveal consistent structural traits (e.g., the predominance of dependency relations, the presence of highly central features, or characteristic node degree distributions) as well as notable domain-specific deviations. These findings ease the identification of maintenance-relevant features, opportunities for modular decomposition, and indicators of structural fragility. This approach provides a scalable, graph-based foundation for the empirical analysis of variability models and contributes quantitative evidence to support future research on their structure and evolution.

</details>

---

### 29. [Trajectory-Optimized Time Reparameterization for Learning-Compatible Reduced-Order Modeling of Stiff Dynamical Systems](https://arxiv.org/abs/2603.16583)

**基本信息**

- 🔗 arXiv: [`2603.16583`](https://arxiv.org/abs/2603.16583)
- 👥 作者: Joe Standridge, Daniel Livescu, Paul Cizmas
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对刚性动力系统（包括化学动力学模型HIRES）的机器学习降阶建模。这直接属于“化学信息学”中计算化学和动力学模拟的范畴，并且其方法对于处理质谱数据中可能涉及的时间动力学过程也具有参考价值。

**📖 中文摘要**

本文研究了时间重参数化（TR）作为神经网络ODE降阶模型（ML-ROM）中刚度缓解机制的作用，并引入了一种轨迹优化的TR（TOTR）公式。该方法将时间重参数化转化为弧长坐标中的优化问题，其中选择遍历速度剖面以惩罚拉伸时间中的加速度。通过针对训练动力学的平滑性，该公式产生的重参数化轨迹比现有TR方法条件更好、更易于学习。TOTR在三个刚性问题上进行了评估：参数化刚性线性系统、van der Pol振荡器和HIRES化学动力学模型。在所有案例中，在相同的训练方案下，所提出的方法产生了更平滑的重参数化和改进的物理时间预测。定量结果表明，与基准算法相比，损失减少了一到两个数量级。这些结果突显了ML-ROM中有效的刚度缓解关键取决于时间映射本身的规律性和可学习性，并且基于优化的TR为多尺度动力系统的显式降阶建模提供了一个鲁棒的框架。这项工作直接处理化学动力学系统（HIRES模型）的建模，与“化学信息学”和“质谱分析”（涉及动力学过程）主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Stiff dynamical systems present a challenge for machine-learning reduced-order models (ML-ROMs), as explicit time integration becomes unstable in stiff regimes while implicit integration within learning loops is computationally expensive and often degrades training efficiency. Time reparameterization (TR) offers an alternative by transforming the independent variable so that rapid physical-time transients are spread over a stretched-time coordinate, enabling stable explicit integration on uniformly sampled grids. Although several TR strategies have been proposed, their effect on learnability in ML-ROMs remains incompletely understood. This work investigates time reparameterization as a stiffness-mitigation mechanism for neural ODE reduced-order modeling and introduces a trajectory-optimized TR (TOTR) formulation. The proposed approach casts time reparameterization as an optimization problem in arc-length coordinates, in which a traversal-speed profile is selected to penalize acceleration in stretched time. By targeting the smoothness of the training dynamics, this formulation produces reparameterized trajectories that are better conditioned and easier to learn than existing TR methods. TOTR is evaluated on three stiff problems: a parameterized stiff linear system, the van der Pol oscillator, and the HIRES chemical kinetics model. Across all cases, the proposed approach yields smoother reparameterizations and improved physical-time predictions under identical training regimens than other TR approaches. Quantitative results demonstrate loss reductions of one to two orders of magnitude compared to benchmark algorithms. These results highlight that effective stiffness mitigation in ML-ROMs depends critically on the regularity and learnability of the time map itself, and that optimization-based TR provides a robust framework for explicit reduced-order modeling of multiscale dynamical systems.

</details>

---

### 30. [On the Transfer of Collinearity to Computer Vision](https://arxiv.org/abs/2603.16592)

**基本信息**

- 🔗 arXiv: [`2603.16592`](https://arxiv.org/abs/2603.16592)
- 👥 作者: Frederik Beuth, Danny Kowerko
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16592.pdf)

**💡 相关性分析**

满足标准1：论文的核心是提出并验证一种新的图像处理原理（共线性），用于增强对具有线性结构特征的图像的识别和分析。这与“化学信息学”和“质谱分析”中处理光谱图像（具有峰和基线）、分子结构图或显微图像中线性特征的分析任务在方法论上相关。

**📖 中文摘要**

本文旨在将人类视觉中的共线性原理转移到计算机视觉中，并探索这一新原理在计算机视觉应用中的潜在用途。作者开发了一个原型模型来例证该原理，并系统性地测试了它，在四个用例的背景下进行了基准测试。用例选择涵盖了广泛的应用和场景：勾画共线性与深度学习的结合（用例I和II），将共线性与显著性模型结合使用（用例II），以及作为特征检测器（用例I）。在第一个用例中，作者发现共线性能够改善晶圆的故障检测，并通过共线性获得1.24倍的性能提升（错误率从6.5%降至5.26%）。在第二个用例中，测试了纳米技术材料中的缺陷识别，并通过共线性实现了3.2倍的性能提升（深度学习，错误率从21.65%降至6.64%）。作为第三个实验，涵盖了遮挡；作为第四个实验，测试了ImageNet并观察到它可能对ImageNet不是非常有益。因此，作者汇编了一个共线性有益的场景列表（晶圆、纳米技术、遮挡），以及无益的场景（ImageNet）。由此推断，共线性可能适用于工业应用，因为如果感兴趣的图像结构是人造的（通常由线条组成），它会有所帮助。这项工作为计算机视觉提供了另一个工具。虽然主要应用在工业视觉，但其核心是提出并验证一种新的、受生物视觉启发的图像处理原理，这对于“化学信息学”和“质谱分析”中处理具有特定结构（如光谱峰、分子结构图）的图像数据具有方法论上的启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Collinearity is a visual perception phenomenon in the human brain that amplifies spatially aligned edges arranged along a straight line. However, it is vague for which purpose humans might have this principle in the real-world, and its utilization in computer vision and engineering applications even is a largely unexplored field. In this work, our goal is to transfer the collinearity principle to computer vision, and we explore the potential usages of this novel principle for computer vision applications. We developed a prototype model to exemplify the principle, then tested it systematically, and benchmarked it in the context of four use cases. Our cases are selected to spawn a broad range of potential applications and scenarios: sketching the combination of collinearity with deep learning (case I and II), using collinearity with saliency models (case II), and as a feature detector (case I). In the first use case, we found that collinearity is able to improve the fault detection of wafers and obtain a performance increase by a factor 1.24 via collinearity (decrease of the error rate from 6.5% to 5.26%). In the second use case, we test the defect recognition in nanotechnology materials and achieve a performance increase by 3.2x via collinearity (deep learning, error from 21.65% to 6.64%), and also explore saliency models. As third experiment, we cover occlusions; while as fourth experiment, we test ImageNet and observe that it might not be very beneficial for ImageNet. Therefore, we can assemble a list of scenarios for which collinearity is beneficial (wafers, nanotechnology, occlusions), and for what is not beneficial (ImageNet). Hence, we infer collinearity might be suitable for industry applications as it helps if the image structures of interest are man-made because they often consist of lines. Our work provides another tool for CV, hope to capture the power of human processing.

</details>

---

### 31. [Machines acquire scientific taste from institutional traces](https://arxiv.org/abs/2603.16659)

**基本信息**

- 🔗 arXiv: [`2603.16659`](https://arxiv.org/abs/2603.16659)
- 👥 作者: Ziqin Gong, Ning Li, Huaikang Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16659.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容直接围绕“化学大模型”这一主题。它探讨了如何通过微调语言模型来获取科学评估（品味）能力，这是一种特定领域（科学）大模型的构建和应用，与“化学大模型”的主题高度相关，展示了如何利用领域数据（出版记录）来训练具有专业判断能力的模型。

**📖 中文摘要**

本文研究了人工智能在科学评估中的“品味”问题，即判断哪些未经测试的想法值得追求的能力。作者发现，在管理学研究领域，前沿大语言模型和人类专家小组对研究提案质量的判断准确率有限（分别为31%和42%）。然而，通过对期刊出版决策记录进行微调的语言模型，其评估判断能力显著超越了所有前沿模型和专家小组，最佳单一模型准确率达到59%。该模型表现出校准良好的置信度，并能将这种评估信号迁移到未经训练的成对比较和单句摘要任务中。这一机制具有普适性：在经济学出版记录上训练的模型也达到了70%的准确率。论文的核心观点是，科学品味并非AI无法触及，而是沉积在制度记录中等待被提取。这项工作为在质量难以形式化验证的学科中，规模化地筛选日益增长的科学产出提供了一种机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Artificial intelligence matches or exceeds human performance on tasks with verifiable answers, from protein folding to Olympiad mathematics. Yet the capacity that most governs scientific advance is not reasoning but taste: the ability to judge which untested ideas deserve pursuit, exercised daily by editors and funders but never successfully articulated, taught, or automated. Here we show that fine-tuning language models on journal publication decisions recovers evaluative judgment inaccessible to both frontier models and human expertise. Using a held-out benchmark of research pitches in management spanning four quality tiers, we find that eleven frontier models, spanning major proprietary and open architectures, barely exceed chance, averaging 31% accuracy. Panels of journal editors and editorial board members reach 42% by majority vote. Fine-tuned models trained on years of publication records each surpass every frontier model and expert panel, with the best single model achieving 59%. These models exhibit calibrated confidence, reaching 100% accuracy on their highest-confidence predictions, and transfer this evaluative signal to untrained pairwise comparisons and one-sentence summaries. The mechanism generalizes: models trained on economics publication records achieve 70% accuracy. Scientific taste was not missing from AI's reach; it was deposited in the institutional record, waiting to be extracted. These results provide a scalable mechanism to triage the expanding volume of scientific production across disciplines where quality resists formal verification.

</details>

---

### 32. [Evaluating Latent Space Structure in Timbre VAEs: A Comparative Study of Unsupervised, Descriptor-Conditioned, and Perceptual Feature-Conditioned Models](https://arxiv.org/abs/2603.16713)

**基本信息**

- 🔗 arXiv: [`2603.16713`](https://arxiv.org/abs/2603.16713)
- 👥 作者: Joseph Cameron, Alan Blackwell
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16713.pdf)

**💡 相关性分析**

满足标准2：论文提供了可用于“化学大模型”和“质谱结构推理”主题的数据集和资源。虽然论文核心是音频生成，但其核心贡献之一是一个精心策划的、带有语义描述符和强度级别的电吉他声音数据集。这种带有精细语义和强度标注的音频数据集，其构建理念和方法（如特征提取、标注体系、评估指标）可以为化学信息学中构建类似的、用于质谱-结构关联的标注数据集（例如，将质谱图与分子结构片段、官能团或物化性质进行关联标注）提供重要的参考和启发。

**📖 中文摘要**

本文对三种用于音乐音色生成的变分自编码器（VAE）的潜在空间结构进行了比较评估：无监督VAE、描述符条件VAE以及基于AudioCommons音色模型的连续感知特征条件VAE。研究使用了一个包含19个语义描述符、四个强度级别的电吉他声音标注数据集。通过一系列聚类和可解释性指标（如轮廓分数、音色描述符紧密度、音高条件分离度、轨迹线性度和跨音高一致性）评估了每个模型的潜在空间结构。研究结果表明，基于连续感知特征的条件VAE产生了更紧凑、更具判别性且对音高不变的潜在空间，其性能优于无监督和离散描述符条件模型。这项工作凸显了独热语义条件化的局限性，并为评估音色潜在空间提供了方法论工具，有助于开发更具可控性和可解释性的生成音频模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a comparative evaluation of latent space organization in three Variational Autoencoders (VAEs) for musical timbre generation: an unsupervised VAE, a descriptor-conditioned VAE, and a VAE conditioned on continuous perceptual features from the AudioCommons timbral models. Using a curated dataset of electric guitar sounds labeled with 19 semantic descriptors across four intensity levels, we assess each model's latent structure with a suite of clustering and interpretability metrics. These include silhouette scores, timbre descriptor compactness, pitch-conditional separation, trajectory linearity, and cross-pitch consistency. Our findings show that conditioning on perceptual features yields a more compact, discriminative, and pitch-invariant latent space, outperforming both the unsupervised and discrete descriptor-conditioned models. This work highlights the limitations of one-hot semantic conditioning and provides methodological tools for evaluating timbre latent spaces, contributing to the development of more controllable and interpretable generative audio models.

</details>

---

### 33. [Novelty-Driven Target-Space Discovery in Automated Electron and Scanning Probe Microscopy](https://arxiv.org/abs/2603.16715)

**基本信息**

- 🔗 arXiv: [`2603.16715`](https://arxiv.org/abs/2603.16715)
- 👥 作者: Utkarsh Pratiush, Kamyar Barakati, Boris N. Slautin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16715.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容是利用AI模型（深度核学习）主动探索科学数据（显微镜图像及光谱/功能响应）中的新规律，这本质上是构建和运用一种用于科学发现的“大模型”或智能代理。同时，论文提出的BEACON框架、基准测试方法以及公开的代码笔记本，为在化学、材料科学等领域开发类似的、用于探索结构-性质关系的AI驱动发现工具提供了重要的方法学资源和工具参考。

**📖 中文摘要**

本文针对自动化显微镜在科学发现中面临的挑战提出了一种解决方案。在许多系统中，最重要的科学信息并不存在于立即可见的图像特征中，而是存在于顺序获取的光谱或功能响应的目标空间中。因此，需要开发能够主动搜索新行为而非简单优化已知目标的策略。为此，作者开发了基于深度核学习的BEACON框架，该框架通过在实验中学习结构-性质关系，并利用这个不断演化的模型来寻找多样化的响应机制，从而引导目标空间的发现。该方法首先在预先获取的真实数据集上建立演示工作流程进行验证，使其能够直接与经典采集策略进行基准测试，并定义了一套监控函数，以透明和可重复的方式比较探索质量、目标空间覆盖率和代理模型行为。这个基准测试框架为评估发现驱动算法（而不仅仅是优化性能）提供了实践基础。随后，作者将工作流程操作化并部署到扫描透射电子显微镜（STEM）上，表明该方法可以从离线验证过渡到真实的实验实施。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern automated microscopy faces a fundamental discovery challenge: in many systems, the most important scientific information does not reside in the immediately visible image features, but in the target space of sequentially acquired spectra or functional responses, making it essential to develop strategies that can actively search for new behaviors rather than simply optimize known objectives. Here, we developed a deep-kernel-learning BEACON framework that is explicitly designed to guide discovery in the target space by learning structure-property relationships during the experiment and using that evolving model to seek diverse response regimes. We first established the method through demonstration workflows built on pre-acquired ground-truth datasets, which enabled direct benchmarking against classical acquisition strategies and allowed us to define a set of monitoring functions for comparing exploration quality, target-space coverage, and surrogate-model behavior in a transparent and reproducible manner. This benchmarking framework provides a practical basis for evaluating discovery-driven algorithms, not just optimization performance. We then operationalized and deployed the workflow on STEM, showing that the approach can transition from offline validation to real experimental implementation. To support adoption and extension by the broader community, the associated notebooks are available, allowing users to reproduce the workflows, test the benchmarks, and adapt the method to their own instruments and datasets.

</details>

---

### 34. [SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding](https://arxiv.org/abs/2603.16739)

**基本信息**

- 🔗 arXiv: [`2603.16739`](https://arxiv.org/abs/2603.16739)
- 👥 作者: D. Darankoum, C. Habermacher, J. Volle 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16739.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是构建一个用于跨领域（跨物种）解码任务的基础模型（SpecMoE）。虽然应用领域是神经科学（EEG），但其方法论核心——针对多模态（时频特征）数据设计掩码策略、构建分层U-Net架构、以及采用混合专家（MoE）框架来整合不同数据子集训练的专业模型——与构建“化学大模型”或用于“质谱结构推理”的通用基础模型在技术路线上高度相似。该论文为解决化学信息学中类似问题（如处理不同仪器、不同样本类型的质谱数据）提供了可借鉴的模型架构和训练范式。

**📖 中文摘要**

本文提出了SpecMoE，一个用于跨物种脑电图（EEG）解码的谱混合专家基础模型。解码脑电图信号中的神经活动编排是连接神经科学与人工智能的核心挑战。现有的脑电图基础模型框架主要依赖于在自监督预训练期间对原始信号进行单独的时域和频域掩码，这种策略往往使学习偏向高频振荡。为了克服这一局限，作者引入了一种新的高斯平滑掩码方案，应用于短时傅里叶变换（STFT）图谱，通过联合应用时间、频率和时频高斯掩码，使得重建任务更具挑战性，迫使模型学习跨高、低频域的复杂神经模式。为了有效恢复信号，作者设计了SpecHi-Net，一个具有多级编码和解码阶段的U形分层架构。为了加速大规模预训练，将数据分成三个子集，每个子集用于训练一个独立的专家模型，然后通过一个由学习的谱门控机制引导的混合专家（MoE）框架SpecMoE将这些模型结合起来。SpecMoE在一系列多样化的脑电图解码任务上实现了最先进的性能，并展示了强大的跨物种和跨被试泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Decoding the orchestration of neural activity in electroencephalography (EEG) signals is a central challenge in bridging neuroscience with artificial intelligence. Foundation models have made strides in generalized EEG decoding, yet many existing frameworks primarily relying on separate temporal and spectral masking of raw signals during self-supervised pretraining. Such strategies often tend to bias learning toward high-frequency oscillations, as low-frequency rhythmic patterns can be easily inferred from the unmasked signal. We introduce a foundation model that utilizes a novel Gaussian-smoothed masking scheme applied to short-time Fourier transform (STFT) maps. By jointly applying time, frequency, and time-frequency Gaussian masks, we make the reconstruction task much more challenging, forcing the model to learn intricate neural patterns across both high- and low-frequency domains. To effectively recover signals under this aggressive masking strategy, we design SpecHi-Net, a U-shaped hierarchical architecture with multiple encoding and decoding stages. To accelerate large-scale pretraining, we partition the data into three subsets, each used to train an independent expert model. We then combine these models through SpecMoE, a mixture of experts framework guided by a learned spectral gating mechanism. SpecMoE achieves state-of-the-art performance across a diverse set of EEG decoding tasks, including sleep staging, emotion recognition, motor imagery classification, abnormal signal detection, and drug effect prediction. Importantly, the model demonstrates strong cross-species and cross-subject generalization, maintaining high accuracy on both human and murine EEG datasets.

</details>

---

### 35. [pADAM: A Plug-and-Play All-in-One Diffusion Architecture for Multi-Physics Learning](https://arxiv.org/abs/2603.16757)

**基本信息**

- 🔗 arXiv: [`2603.16757`](https://arxiv.org/abs/2603.16757)
- 👥 作者: Amirhossein Mollaali, Bongseok Kim, Christian Moya 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16757.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是开发一个统一的生成式多物理建模框架（pADAM），该框架能够学习跨不同物理定律的共享先验，并执行前向预测、逆向推断和不确定性量化。这直接对应于“化学大模型”中一个关键愿景：构建能够统一处理多种化学现象（反应、扩散、光谱等）、进行逆向设计（如分子设计）和提供可靠不确定性评估的通用模型。pADAM的架构和思想为化学领域类似模型的构建提供了重要的概念和技术参考。

**📖 中文摘要**

本文介绍了pADAM，一个统一的生成式框架，用于在异构偏微分方程族中学习共享的概率先验。通过系统状态和（如适用）物理参数的联合分布，pADAM在单一架构内支持前向预测和逆向推断，而无需重新训练。在从标量扩散到非线性Navier-Stokes方程的基准测试中，pADAM即使在稀疏观测下也能实现准确的推断。结合保形预测，它还提供了具有覆盖保证的可靠不确定性量化。此外，pADAM仅从两个稀疏快照就能执行概率模型选择，通过其学习的生成表示识别控制定律。这些结果凸显了生成式多物理建模在实现统一且具有不确定性意识的科学推断方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generalizing across disparate physical laws remains a fundamental challenge for artificial intelligence in science. Existing deep-learning solvers are largely confined to single-equation settings, limiting transfer across physical regimes and inference tasks. Here we introduce pADAM, a unified generative framework that learns a shared probabilistic prior across heterogeneous partial differential equation families. Through a learned joint distribution of system states and, where applicable, physical parameters, pADAM supports forward prediction and inverse inference within a single architecture without retraining. Across benchmarks ranging from scalar diffusion to nonlinear Navier--Stokes equations, pADAM achieves accurate inference even under sparse observations. Combined with conformal prediction, it also provides reliable uncertainty quantification with coverage guarantees. In addition, pADAM performs probabilistic model selection from only two sparse snapshots, identifying governing laws through its learned generative representation. These results highlight the potential of generative multi-physics modeling for unified and uncertainty-aware scientific inference.

</details>

---

### 36. [Machine Learning Based Identification of Solvents from Post-Desiccation Patterns](https://arxiv.org/abs/2603.15660)

**基本信息**

- 🔗 arXiv: [`2603.15660`](https://arxiv.org/abs/2603.15660)
- 👥 作者: Jesús Israel Morán-Cortés, Felipe Pacheco-Vázquez
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15660.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用机器学习（人工神经网络）从干燥后形成的物理模式中识别化学溶剂。这直接关联到化学信息学中利用计算方法和数据分析解决化学识别问题的主题。

**📖 中文摘要**

本文提出了一种基于人工神经网络的优化协议，用于识别淀粉-液体浆料干燥开裂过程中涉及的溶剂，即使溶剂已完全蒸发。该协议利用图像分析技术，基于裂纹的九个形态特征（大小、形状、几何和取向排序）生成频率直方图，并将其作为神经网络的输入数据。该方法在识别单一溶剂（水、乙醇、丙酮）和双组分溶剂（不同浓度的水-乙醇混合物）时，平均准确率达到96%。该工作展示了机器学习方法在从干燥模式中识别化学成分（溶剂）的能力，这与化学信息学中利用模式识别进行物质分析的核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce an optimized protocol of fracture pattern classification using an artificial neural network to identify the solvent involved in the desiccation cracking process of starch-liquid slurries, even after it has been completely evaporated. For this purpose, image analysis techniques were used to characterize patterns obtained from drying suspensions using single solvents (water, ethanol, acetone) and two-component solvents (water-ethanol mixtures at different concentrations). Frequency histograms were generated based on nine morphological features, taking into account their size, shape, geometry and orientational ordering. Subsequently, we used these histograms as input data into artificial neural network variants to determine the set of features that lead to the higher accuracy in solvent identification. We obtained an average accuracy of $96(\pm 1)\%$ considering all solvents in the analysis. The highest accuracy was obtained with sets of features that include the crack area distribution. The proposed protocol can help to determine the combination of features that optimize pattern recognition in other fields of science and engineering.

</details>

---

### 37. [Life cycle assessment for all organic chemicals](https://arxiv.org/abs/2603.15686)

**基本信息**

- 🔗 arXiv: [`2603.15686`](https://arxiv.org/abs/2603.15686)
- 👥 作者: Shaohan Chen, Tim Langhorst, Julian Nöhl 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15686.pdf)

**💡 相关性分析**

满足标准2：论文提出了CRYSTAL框架，并创建了一个大规模、透明的有机化学品生命周期清单数据库。这为化学信息学领域（特别是可持续性和生命周期分析方向）提供了重要的数据集和计算工具资源。

**📖 中文摘要**

本文介绍了CRYSTAL框架，这是一个基于分子结构、利用逆合成和机器学习门到门清单，自动为有机化学品生成一致且透明的生命周期清单（LCI）数据的系统。该框架创建了一个包含超过70,000种有机化学品、涵盖110,000多个透明LCI数据集的数据库，量化了原料和能源需求、相关辅助材料、生物圈流动和废物流动。CRYSTAL旨在将化学品的生命周期评估从依赖“未知的未知”转变为协作可改进的“已知的未知”映射。这项工作为大规模、数据驱动的化学可持续性评估提供了系统化的工具和资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemicals are embedded in nearly every aspect of modern society, yet their production poses substantial sustainability concerns. Achieving a sustainable chemical industry requires detailed Life Cycle Assessment (LCA); however, current assessments face many unknowns due to limited, partly inconsistent, and untransparent data coverage since existing Life Cycle Inventory (LCI) databases account for only a tiny fraction of traded chemicals. Here, we introduce the Chemical RetrosYnthesiS for Transparent Assessment of Life-cycles (CRYSTAL) framework, which automatically generates consistent and transparent LCI data for organic chemicals based on their molecular structure using retrosynthesis and machine-learned gate-to-gate inventories. Using the predictive power of CRYSTAL, we create a consistent database for more than 70000 organic chemicals, comprising over 110000 transparent LCI datasets that quantify both feedstock and energy demands, together with associated auxiliary materials, biosphere flows, and waste flows. From this comprehensive database, we identify 50 key environmental hotspots driving high impacts of organic chemical production across multiple environmental categories and pivotal hub chemicals that are most critical for downstream chemical production. In providing this comprehensive data foundation, the CRYSTAL framework offers systematic guidance for targeted engineering and policy interventions. Its transparent, modular nature is designed to shift chemical LCA from a reliance on "unknown unknowns" to a collaboratively improvable mapping of "known unknowns".

</details>

---

### 38. [LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation](https://arxiv.org/abs/2603.15712)

**基本信息**

- 🔗 arXiv: [`2603.15712`](https://arxiv.org/abs/2603.15712)
- 👥 作者: AI Scientists, Xinyi Lin, Danqing Yin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15712.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容是使用检索增强生成的大型语言模型（LLM）进行催化剂发现和设计，这直接关联“化学大模型”主题。同时，该方法利用并构建了材料数据库作为检索基础，提供了用于材料发现的工具框架。

**📖 中文摘要**

本文展示了大型语言模型（LLMs）如何通过检索增强生成（RAG）框架协助催化剂发现过程。该框架使GPT-4能够访问包含50,000多种已知材料的数据集，从而在物理约束下导航化学空间，进行高通量材料设计。该方法生成了250多种催化剂候选物，其中82%具有热力学稳定性，68%实现了低成本、金属导电性和机械稳定性的多目标约束。最佳性能的催化剂在限制电位上比IrO2提高了25%。该工作表明，检索增强生成可以将AI的创造力锚定在物理约束中，而不牺牲探索性，为研究人员更高效地探索化学空间、解释结果和生成假设提供了一种方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

CO2 reduction requires efficient catalysts, yet materials discovery remains bottlenecked by 10-20 year development cycles requiring deep domain expertise. This paper demonstrates how large language models can assist the catalyst discovery process by helping researchers explore chemical spaces and interpret results when augmented with retrieval-based grounding. We introduce a retrieval-augmented generation framework that enables GPT-4 to navigate chemical space by accessing a database of 50,000+ known materials, adapting general-purpose language understanding for high-throughput materials design. Our approach generated over 250 catalyst candidates with an 82% thermodynamic stability rate while addressing multi-objective constraints: 68% achieved <$100/kg cost with metallic conductivity (band gap<0.1eV) and mechanical stability (B/G>1.75). The best-performing Fe0.2Co0.2Ni0.2Ir0.1Ru0.3 achieves 0.285V limiting potential (25% improvement over IrO2), while Cr0.2Fe0.2Co0.3Ni0.2Mo0.1 optimally balances performance-cost trade-offs at $18/kg. Volcano plot analysis confirms that 78% of LLM-generated catalysts cluster near the theoretical activity optimum, while our system achieves 200x computational efficiency compared to traditional high-throughput screening. By demonstrating that retrieval-augmented generation can ground AI creativity in physical constraints without sacrificing exploration, this work demonstrates an approach where natural language interfaces can streamline materials discovery workflows, enabling researchers to explore chemical spaces more efficiently while the LLM assists in result interpretation and hypothesis generation.

</details>

---

### 39. [Deep Adaptive Model-Based Design of Experiments](https://arxiv.org/abs/2603.16146)

**基本信息**

- 🔗 arXiv: [`2603.16146`](https://arxiv.org/abs/2603.16146)
- 👥 作者: Arno Strouwen, Sebastian Micluţa-Câmpeanu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16146.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于动力系统参数估计的深度自适应模型实验设计框架。这涉及到使用深度学习模型（Transformer）来优化实验过程，属于化学信息学/分析化学中利用AI模型优化实验设计和数据分析的范畴。

**📖 中文摘要**

本文提出了一种结合深度自适应设计（DAD）与可微分机理模型的深度学习方法，用于非线性动力系统的模型实验设计（MBDOE）。该方法将顺序实验设计摊销到一个离线训练的神经网络策略中，避免了传统自适应MBDOE在每一步之间进行昂贵后验推断和设计优化的需求。论文针对具有已知控制方程但参数不确定的动力系统，将顺序对比训练目标扩展到处理干扰参数，并提出了一个尊重动力系统时间结构的基于Transformer的策略架构。该方法在四个复杂性递增的系统上进行了演示，包括具有Monod动力学的补料分批生物反应器、具有不确定底物抑制的Haldane生物反应器、具有干扰清除参数的两室药代动力学模型以及用于实时部署的直流电机。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Model-based design of experiments (MBDOE) is essential for efficient parameter estimation in nonlinear dynamical systems. However, conventional adaptive MBDOE requires costly posterior inference and design optimization between each experimental step, precluding real-time applications. We address this by combining Deep Adaptive Design (DAD), which amortizes sequential design into a neural network policy trained offline, with differentiable mechanistic models. For dynamical systems with known governing equations but uncertain parameters, we extend sequential contrastive training objectives to handle nuisance parameters and propose a transformer-based policy architecture that respects the temporal structure of dynamical systems. We demonstrate the approach on four systems of increasing complexity: a fed-batch bioreactor with Monod kinetics, a Haldane bioreactor with uncertain substrate inhibition, a two-compartment pharmacokinetic model with nuisance clearance parameters, and a DC motor for real-time deployment.

</details>

---

### 40. [FAlCon: A unified framework for algorithmic control of quantum dot devices](https://arxiv.org/abs/2603.16650)

**基本信息**

- 🔗 arXiv: [`2603.16650`](https://arxiv.org/abs/2603.16650)
- 👥 作者: Tyler J. Kovach, Daniel Schug, Zach D. Merino 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16650.pdf)

**💡 相关性分析**

满足标准2：论文提出了FAlCon框架，这是一个用于量子点器件自动化表征和控制的软件生态系统，提供了领域特定语言、数据结构和协议库。这为化学信息学/材料科学中涉及自动化实验控制和数据分析的领域提供了重要的工具和资源。

**📖 中文摘要**

本文介绍了FAlCon，一个用于便携式、自动化量子点（QD）器件表征和调谐测量工作流程的开源软件生态系统。FAlCon提供了一种轻量级领域特定语言，用于以硬件无关的形式表达基于状态的调谐逻辑；专门的可传输量子点数据结构库（“调谐术语”）；以及可扩展的共享测量协议库，实现了实验室无关、可互操作的测量栈。通过将算法意图与仪器实现分离，同时保持可追溯性并支持类型化脚本，FAlCon使研究人员和工程师能够在异构的量子点设置中交换、适配和部署表征与自动调谐例程。该框架虽然目前针对量子点实验，但其模块化抽象也可通过提供新的调谐数据类型和仪器控制模板，复用于其他量子比特模态和科学实验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As spin-based quantum systems scale, their setup and control complexity increase sharply. In semiconductor quantum dot (QD) experiments, device-to-device variability, heterogeneous control-electronics stacks, and differing operational modalities make it difficult to reuse characterization, calibration, and control logic across laboratories. We present FAlCon, an open-source software ecosystem for portable, automated characterization and tuning measurement workflows. FAlCon provides (i) a lightweight domain-specific language for expressing state-based tuning logic in a hardware-agnostic form; (ii) specialized transmittable libraries of physics-informed QD data structures (``tuning vernacula''); and (iii) extensible libraries of shared measurement protocols enabling an interoperable lab-agnostic measurement stack. By separating algorithm intent from instrument realization, while preserving traceability and supporting typed scripting, FAlCon enables researchers and engineers to exchange, adapt, and deploy characterization and autotuning routines across heterogeneous QD setups. The framework supports all users, ranging from end users running prebuilt algorithms with custom initial conditions to developers extending instrumentation support and contributing new tuning strategies. Although the present release targets QD experiments, other qubit modalities and scientific experiments could reuse FAlCon's modular abstractions by providing new tuning data types and instrument control templates.

</details>

---

### 41. [Revisiting ASR Error Correction with Specialized Models](https://arxiv.org/abs/2405.15216)

**基本信息**

- 🔗 arXiv: [`2405.15216`](https://arxiv.org/abs/2405.15216)
- 👥 作者: Zijin Gu, Tatiana Likhomanenko, He Bai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.15216.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于药物反应预测的异质图神经网络模型drGT。虽然主要应用在生物医药领域，但其核心方法（图神经网络、注意力机制用于特征解释）是化学信息学和计算化学中用于分子性质预测、结构-活性关系研究的典型技术。模型旨在从基因表达等数据中推理药物反应，属于广义的化学信息学中的“化学大模型”（针对药物-基因系统的预测模型）范畴。

**📖 中文摘要**

本文提出drGT，一个基于药物-细胞-基因异质图网络的深度学习模型，用于药物反应预测和机制导向的可解释性。模型通过注意力系数（ACs）耦合预测与解释。drGT在多个数据集（GDSC, NCI60, CTRP）上评估了预测泛化能力（随机、未见药物、未见细胞、零样本划分）和生物学合理性。结果表明，drGT在回归任务上始终提供顶级的性能，同时在药物敏感性分类上保持竞争力。在可解释性方面，ACs衍生的药物-基因链接能够恢复已知的生物学知识，例如在已知药物-靶点相互作用（DTIs）的药物中，有相当比例的预测链接与已知DTIs匹配或得到文献支持。对ACs优先基因的富集分析揭示了药物扰动的生物过程，提供了通路层面的解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Language models play a central role in automatic speech recognition (ASR), yet most methods rely on text-only models unaware of ASR error patterns. Recently, large language models (LLMs) have been applied to ASR correction, but introduce latency and hallucination concerns. We revisit ASR error correction with compact seq2seq models, trained on ASR errors from real and synthetic audio. To scale training, we construct synthetic corpora via cascaded TTS and ASR, finding that matching the diversity of realistic error distributions is key. We propose correction-first decoding, where the correction model generates candidates rescored using ASR acoustic scores. With 15x fewer parameters than LLMs, our model achieves 1.5/3.3% WER on LibriSpeech test-clean/other, outperforms LLMs, generalizes across ASR architectures (CTC, Seq2seq, Transducer) and diverse domains, and provides precise corrections in the low-error regime where LLMs struggle.

</details>

---

### 42. [A Survey of Frontiers in LLM Reasoning: Inference Scaling, Learning to Reason, and Agentic Systems](https://arxiv.org/abs/2504.09037)

**基本信息**

- 🔗 arXiv: [`2504.09037`](https://arxiv.org/abs/2504.09037)
- 👥 作者: Zixuan Ke, Fangkai Jiao, Yifei Ming 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.09037.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于大型语言模型（LLMs）推理能力的综述。虽然标题未直接提及化学，但“化学大模型”本质上是领域特定或通用的LLMs在化学问题上的应用。该综述系统地总结了LLM推理的技术前沿（如思维链、智能体系统、训练方法），这些技术直接支撑和启发了化学领域大模型的开发与应用（例如，用于逆合成规划、文献信息提取的化学LLM智能体）。因此，它包含了与“化学大模型”主题相关的重要讨论和展望。

**📖 中文摘要**

本文对大型语言模型（LLMs）推理能力的前沿进展进行了综述。作者将现有方法沿着两个正交维度进行分类：（1）机制，定义推理实现的阶段（在推理时或通过专门训练）；（2）架构，确定推理过程中涉及的组件，区分独立的LLMs和包含外部工具、多智能体协作的智能体复合系统。在每个维度内，作者分析了两个关键视角：输入层面（专注于构建高质量提示的技术）和输出层面（精炼多个采样候选以提升推理质量的方法）。综述涵盖了从监督微调到强化学习（如PPO和GRPO）的广泛学习算法，以及推理器和验证器的训练。同时还考察了智能体工作流的关键设计，从生成器-评估器、LLM辩论等既定模式到最近的创新。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is a fundamental cognitive process that enables logical inference, problem-solving, and decision-making. With the rapid advancement of large language models (LLMs), reasoning has emerged as a key capability that distinguishes advanced AI systems from conventional models that empower chatbots. In this survey, we categorize existing methods along two orthogonal dimensions: (1) Regimes, which define the stage at which reasoning is achieved (either at inference time or through dedicated training); and (2) Architectures, which determine the components involved in the reasoning process, distinguishing between standalone LLMs and agentic compound systems that incorporate external tools, and multi-agent collaborations. Within each dimension, we analyze two key perspectives: (1) Input level, which focuses on techniques that construct high-quality prompts that the LLM condition on; and (2) Output level, which methods that refine multiple sampled candidates to enhance reasoning quality. This categorization provides a systematic understanding of the evolving landscape of LLM reasoning, highlighting emerging trends such as the shift from inference-scaling to learning-to-reason (e.g., DeepSeek-R1), and the transition to agentic workflows (e.g., OpenAI Deep Research, Manus Agent). Additionally, we cover a broad spectrum of learning algorithms, from supervised fine-tuning to reinforcement learning such as PPO and GRPO, and the training of reasoners and verifiers. We also examine key designs of agentic workflows, from established patterns like generator-evaluator and LLM debate to recent innovations. ...

</details>

---

### 43. [Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning](https://arxiv.org/abs/2507.00965)

**基本信息**

- 🔗 arXiv: [`2507.00965`](https://arxiv.org/abs/2507.00965)
- 👥 作者: Félix Lefebvre, Gaël Varoquaux
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.00965.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发用于大型知识图谱的嵌入学习算法SEPAL。知识图谱是化学信息学中存储化合物、反应、性质等结构化知识的核心数据资源。高效的图谱嵌入方法是构建化学领域大模型（如用于分子表示学习、反应预测的模型）的关键基础技术之一。因此，该工作与“化学大模型”主题在方法论和数据资源（知识图谱表示）上高度相关。

**📖 中文摘要**

本文提出SEPAL（可扩展嵌入传播算法），一种为大型知识图谱设计的大规模嵌入学习方法，旨在为下游任务生成高质量的嵌入。SEPAL的核心思想是通过仅在一小部分核心实体上优化嵌入来确保全局嵌入一致性，然后通过消息传递将其传播到图的其余部分。该方法解决了当前模型的两个局限性：它们主要针对链接预测进行优化，并且由于GPU内存限制，在最大规模图上的应用需要大量工程努力。作者在7个大规模知识图谱和46个下游机器学习任务上评估了SEPAL，结果表明其在下游任务上显著优于先前的方法，并且能够将基础嵌入模型扩展到在商用硬件上拟合巨大的知识图谱。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many machine learning tasks can benefit from external knowledge. Large knowledge graphs store such knowledge, and embedding methods can be used to distill it into ready-to-use vector representations for downstream applications. For this purpose, current models have however two limitations: they are primarily optimized for link prediction, via local contrastive learning, and their application to the largest graphs requires significant engineering effort due to GPU memory limits. To address these, we introduce SEPAL: a Scalable Embedding Propagation ALgorithm for large knowledge graphs designed to produce high-quality embeddings for downstream tasks at scale. The key idea of SEPAL is to ensure global embedding consistency by optimizing embeddings only on a small core of entities, and then propagating them to the rest of the graph with message passing. We evaluate SEPAL on 7 large-scale knowledge graphs and 46 downstream machine learning tasks. Our results show that SEPAL significantly outperforms previous methods on downstream tasks. In addition, SEPAL scales up its base embedding model, enabling fitting huge knowledge graphs on commodity hardware.

</details>

---

### 44. [Feature Attribution in 5G Intrusion Detection: A Statistical vs. Logic-Based Comparison](https://arxiv.org/abs/2509.10206)

**基本信息**

- 🔗 arXiv: [`2509.10206`](https://arxiv.org/abs/2509.10206)
- 👥 作者: Federica Uccello, Simin Nadjm-Tehrani
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.10206.pdf)

**💡 相关性分析**

满足标准2：论文深入分析和比较了用于模型解释的特征归因工具（SHAP和VoTE-XAI）。这些工具和方法本身是通用的，可被应用于化学信息学和质谱分析领域，用于解释化学大模型的预测或理解质谱特征与分子结构之间的关系，因此提供了潜在的方法论资源。

**📖 中文摘要**

本文题为《5G入侵检测中的特征归因：统计方法与逻辑方法的比较》。论文的核心是评估和比较两种可解释人工智能（XAI）方法——SHAP（统计方法）和VoTE-XAI（逻辑方法）——在5G入侵检测场景中的特征归因性能。研究使用XGBoost模型在三个5G相关数据集（5G-NIDD、MSA、PFCP）上生成安全警报，并分析这两种方法如何解释这些警报。论文评估了归因结果的稀疏性、稳定性和效率。这项工作直接提供了用于理解和解释机器学习模型（在安全领域）的工具和方法论比较，这些工具和方法（特别是逻辑方法）的原理和框架可以迁移到化学信息学领域，用于解释质谱数据分析或化学大模型的预测结果，例如理解哪些分子特征或质谱峰对结构推理至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rise of fifth-generation (5G) networks in critical applications, it is urgent to move from detection of malicious activity to systems capable of providing a reliable verdict suitable for mitigation. In this regard, understanding and interpreting machine learning (ML) models' security alerts is crucial for enabling actionable incident response orchestration. Explainable Artificial Intelligence (XAI) techniques are expected to enhance trust by providing insights into why alerts are raised. Under the umbrella of XAI, interpretability of outcomes is crucially dependent on understanding the influence of specific inputs, referred to as feature attribution. {A dominant approach to feature attribution statistically associates feature sets that can be correlated to a given alert. This paper investigates its merits against the backdrop of criticism from recent literature, in comparison with feature attribution based on logic. We extensively study two methods, SHAP and VoTE-XAI, as representatives of each feature attribution approach by analyzing their interpretations of alerts generated by an XGBoost model across three 5G-relevant datasets (5G-NIDD, MSA, and PFCP) covering multiple attack scenarios. We identify three metrics for assessing explanations: sparsity, how concise they are; stability, how consistent they are across samples from the same attack type; and efficiency, how fast an explanation is generated. Our results reveal that logic-based attributions are consistently more sparse and stable across alerts. More importantly, we found a significant divergence between features selected by SHAP and VoTE-XAI. However, none of the top-ranked features selected by SHAP were missed by VoTE-XAI. Finally, we analyze the efficiency of both methods, discussing their suitability for real-time security monitoring even in high-dimensional 5G environments (478 features).

</details>

---

### 45. [Controllable Graph Generation with Diffusion Models via Inference-Time Tree Search Guidance](https://arxiv.org/abs/2510.10402)

**基本信息**

- 🔗 arXiv: [`2510.10402`](https://arxiv.org/abs/2510.10402)
- 👥 作者: Jiachi Zhao, Zehong Wang, Yamei Liao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.10402.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图生成，并明确在分子生成（2D和3D分子）这一化学信息学核心任务上进行了验证和评估。这直接与“化学大模型”（特别是用于分子生成的模型）的研究主题相关。

**📖 中文摘要**

本文题为《通过推理时树搜索引导的可控图生成扩散模型》。论文提出了一种名为TreeDiff的新框架，用于可控的图生成。该框架将蒙特卡洛树搜索（MCTS）与双空间（潜在空间和图空间）扩散模型相结合，以在生成过程中精确控制图的性质。论文在2D和3D分子生成基准上进行了广泛的实验，证明了其在无条件和有条件设置下的最先进性能。分子图生成是化学信息学和药物发现中的核心任务。这项工作直接针对图结构数据的生成问题，并展示了在分子生成这一化学信息学关键应用上的有效性。其提出的可控生成框架对于构建用于分子设计的化学大模型或生成用于质谱结构推理的候选分子结构具有直接的相关性和应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation is a fundamental problem in graph learning with broad applications across Web-scale systems, knowledge graphs, and scientific domains such as drug and material discovery. Recent approaches leverage diffusion models for step-by-step generation, yet unconditional diffusion offers little control over desired properties, often leading to unstable quality and difficulty in incorporating new objectives. Inference-time guidance methods mitigate these issues by adjusting the sampling process without retraining, but they remain inherently local, heuristic, and limited in controllability. To overcome these limitations, we propose TreeDiff, a Monte Carlo Tree Search (MCTS) guided dual-space diffusion framework for controllable graph generation. TreeDiff is a plug-and-play inference-time method that expands the search space while keeping computation tractable. Specifically, TreeDiff introduces three key designs to make it practical and scalable: (1) a macro-step expansion strategy that groups multiple denoising updates into a single transition, reducing tree depth and enabling long-horizon exploration; (2) a dual-space denoising mechanism that couples efficient latent-space denoising with lightweight discrete correction in graph space, ensuring both scalability and structural fidelity; and (3) a dual-space verifier that predicts long-term rewards from partially denoised graphs, enabling early value estimation and removing the need for full rollouts. Extensive experiments on 2D and 3D molecular generation benchmarks, under both unconditional and conditional settings, demonstrate that TreeDiff achieves state-of-the-art performance. Notably, TreeDiff exhibits favorable inference-time scaling: it continues to improve with additional computation, while existing inference-time methods plateau early under limited resources.

</details>

---

### 46. [Connecting Jensen-Shannon and Kullback-Leibler Divergences: A New Bound for Representation Learning](https://arxiv.org/abs/2510.20644)

**基本信息**

- 🔗 arXiv: [`2510.20644`](https://arxiv.org/abs/2510.20644)
- 👥 作者: Reuben Dorent, Polina Golland, William Wells III
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.20644.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是表示学习中的基础理论问题，即互信息的估计与优化。这是构建和理解任何领域大模型（包括化学大模型）的关键理论基础。论文提出的新边界和理论分析可直接应用于改进化学分子表示学习模型。

**📖 中文摘要**

本文题为《连接Jensen-Shannon散度与Kullback-Leibler散度：表示学习的新边界》。论文从理论角度深入探讨了互信息（MI）的两种变分下界——基于Kullback-Leibler散度（KLD）和基于Jensen-Shannon散度（JSD）——之间的关系，并推导了一个新的、更紧致的下界。论文通过实验证明了该下界在MI估计中的有效性，并讨论了其在信息瓶颈等表示学习框架中的应用。表示学习是构建化学大模型（如用于分子性质预测或表征学习的模型）的基础。对互信息估计方法的改进和理论理解，直接影响着如何设计和训练更有效的化学表示模型。因此，这项工作为化学大模型的基础理论研究提供了重要的理论工具和见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mutual Information (MI) is a fundamental measure of statistical dependence widely used in representation learning. While direct optimization of MI via its definition as a Kullback-Leibler divergence (KLD) is often intractable, many recent methods have instead maximized alternative dependence measures, most notably, the Jensen-Shannon divergence (JSD) between joint and product of marginal distributions via discriminative losses. However, the connection between these surrogate objectives and MI remains poorly understood. In this work, we bridge this gap by deriving a new, tight, and tractable lower bound on KLD as a function of JSD in the general case. By specializing this bound to joint and marginal distributions, we demonstrate that maximizing the JSD-based information increases a guaranteed lower bound on mutual information. Furthermore, we revisit the practical implementation of JSD-based objectives and observe that minimizing the cross-entropy loss of a binary classifier trained to distinguish joint from marginal pairs recovers a known variational lower bound on the JSD. Extensive experiments demonstrate that our lower bound is tight when applied to MI estimation. We compared our lower bound to state-of-the-art neural estimators of variational lower bound across a range of established reference scenarios. Our lower bound estimator consistently provides a stable, low-variance estimate of a tight lower bound on MI. We also demonstrate its practical usefulness in the context of the Information Bottleneck framework. Taken together, our results provide new theoretical justifications and strong empirical evidence for using discriminative learning in MI-based representation learning.

</details>

---

### 47. [Testing Correlation in Graphs by Counting Bounded Degree Motifs](https://arxiv.org/abs/2510.25289)

**基本信息**

- 🔗 arXiv: [`2510.25289`](https://arxiv.org/abs/2510.25289)
- 👥 作者: Dong Huang, Pengkun Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.25289.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于图模体计数的统计测试方法。图是化学信息学中表示分子的基本数据结构。该方法为分析分子图集合的统计特性、评估生成模型或进行图数据集之间的比较提供了新的算法工具和思路。

**📖 中文摘要**

本文题为《通过计数有界度模体测试图的相关性》。论文研究的是两个Erdős-Rényi图之间相关性的检测问题，这是一个图论中的假设检验问题。作者提出了一种通过计数有界度模体（bounded degree motifs）来实现的多项式时间测试方法，并证明了其在特定参数条件下的有效性。虽然论文本身属于理论计算机科学/图论领域，但图模型和模体分析是化学信息学中分析分子图、反应网络和化学结构相似性的常用工具。论文提出的基于模体计数的相关性检测框架，可以启发或应用于化学信息学中，例如比较两个分子图数据集之间的分布差异，或作为评估分子生成模型的一种新方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the problem of detecting correlation between two Erdős-Rényi graphs $G(n,p)$, formulated as a hypothesis testing problem: under the null hypothesis, the two graphs are independent, while under the alternative hypothesis, they are correlated through a latent bijective mapping between their vertex sets. We develop a polynomial-time test by counting bounded degree motifs and prove its effectiveness for any constant correlation coefficient $\rho$ when the edge connecting probability satisfies $p\ge n^{-1+\delta}$ for some constant $\delta>0$. In particular, our guarantee improves the constrain of motif-counting methods from $\rho\ge \sqrt{\alpha}$ to any constant $\rho = \Omega(1)$, where $\alpha\approx 0.338$ is the Otter's constant.

</details>

---

### 48. [Efficient LLM Safety Evaluation through Multi-Agent Debate](https://arxiv.org/abs/2511.06396)

**基本信息**

- 🔗 arXiv: [`2511.06396`](https://arxiv.org/abs/2511.06396)
- 👥 作者: Dachuan Lin, Guobin Shen, Zihao Yang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.06396.pdf)

**💡 相关性分析**

满足标准2：论文构建了HAJailBench这一大规模、细粒度的人工标注基准数据集，并提出了一个多智能体评估框架。这为化学信息学领域如何系统性地构建和评估针对“化学大模型”或“质谱结构推理”模型的基准测试提供了方法论参考和范式。

**📖 中文摘要**

本文题为《通过多智能体辩论进行高效的大语言模型安全性评估》。论文提出了一个成本高效的多智能体评判框架，使用小型语言模型（SLM）通过结构化的辩论（批评者、辩护者、法官）来评估大语言模型（LLM）的安全性。为了严格评估，作者构建了一个大规模、人工标注的越狱基准测试HAJailBench。论文的核心是构建评估框架和基准数据集。虽然主题是LLM安全性，但其方法论——构建针对特定模型行为（如越狱）的、带有人工标注的基准数据集——对于化学信息学和质谱分析领域具有重要的借鉴意义。例如，可以类似地构建用于评估“化学大模型”在分子性质预测、逆合成规划或“质谱结构推理”模型在解析未知谱图方面的基准测试集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Safety evaluation of large language models (LLMs) increasingly relies on LLM-as-a-Judge frameworks, but the high cost of frontier models limits scalability. We propose a cost-efficient multi-agent judging framework that employs Small Language Models (SLMs) through structured debates among critic, defender, and judge agents. To rigorously assess safety judgments, we construct HAJailBench, a large-scale human-annotated jailbreak benchmark comprising 12,000 adversarial interactions across diverse attack methods and target models. The dataset provides fine-grained, expert-labeled ground truth for evaluating both safety robustness and judge reliability. Our SLM-based framework achieves agreement comparable to GPT-4o judges on HAJailBench while substantially reducing inference cost. Ablation results show that three rounds of debate yield the optimal balance between accuracy and efficiency. These findings demonstrate that structured, value-aligned debate enables SLMs to capture semantic nuances of jailbreak attacks and that HAJailBench offers a reliable foundation for scalable LLM safety evaluation.

</details>

---

### 49. [Flow Matching for Tabular Data Synthesis](https://arxiv.org/abs/2512.00698)

**基本信息**

- 🔗 arXiv: [`2512.00698`](https://arxiv.org/abs/2512.00698)
- 👥 作者: Bahrul Ilmi Nasution, Floor Eijkelboom, Mark Elliot 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00698.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是表格数据的生成模型，这是化学信息学中处理分子描述符、实验数据等表格数据的核心任务之一。同时，论文对多种生成方法进行了详尽的实证比较，为化学领域研究者选择合适的数据生成工具提供了重要的性能参考和资源（代码已开源）。

**📖 中文摘要**

本文题为《用于表格数据合成的流匹配》。论文专注于使用流匹配（Flow Matching）方法生成合成表格数据。作者对不同的流匹配实现（FM和变分FM）与最先进的扩散方法（TabDDPM）进行了全面的实证比较，评估了最优传输和方差保持概率路径，以及确定性和随机性采样器。合成数据生成在化学信息学中至关重要，例如用于扩充分子数据集以训练预测模型，或在保护隐私的前提下共享化学数据。论文系统性地比较了当前先进的生成模型在表格数据上的性能，其结论（如FM优于扩散模型、计算效率更高）对于选择或开发用于生成分子描述符、物化性质等表格化化学数据的模型具有直接的指导价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data generation is an important tool for privacy-preserving data sharing. Although diffusion models have set recent benchmarks, flow matching (FM) offers a promising alternative. This paper presents different ways to implement FM for tabular data synthesis. We provide a comprehensive empirical study that compares flow matching (FM and variational FM) with a state-of-the-art diffusion method (TabDDPM and TabSyn) in tabular data synthesis. We evaluate both the standard Optimal Transport (OT) and the Variance Preserving (VP) probability paths, and also compare deterministic and stochastic samplers -- something possible when learning to generate using \textit{variational} FM -- characterising the empirical relationship between data utility and privacy risk. Our key findings reveal that FM, particularly TabbyFlow, outperforms diffusion baselines. Flow matching methods also achieve better performance with remarkably low function evaluations ($\leq$ 100 steps), offering a substantial computational advantage. The choice of probability path is also crucial, as using the OT is a strong default and more robust to early stopping on average, while VP has potential to produce synthetic data with lower privacy risk. Lastly, our results show that making flows stochastic not only preserves marginal distributions but, in some instances, enables the generation of high utility synthetic data with reduced disclosure risk. The implementation code associated with this paper is publicly available at this https URL .

</details>

---

### 50. [SolarGPT-QA: A Domain-Adaptive Large Language Model for Educational Question Answering in Space Weather and Heliophysics](https://arxiv.org/abs/2601.12131)

**基本信息**

- 🔗 arXiv: [`2601.12131`](https://arxiv.org/abs/2601.12131)
- 👥 作者: Santosh Chapagain, MohammadReza EskandariNasab, Onur Vural 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.12131.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于特定科学领域（空间天气和太阳物理学）的领域自适应大语言模型（SolarGPT-QA）。这直接属于“化学大模型”主题的范畴，即针对特定科学或化学信息学领域构建和优化大型语言模型。

**📖 中文摘要**

本文介绍了SolarGPT-QA，一个基于领域自适应大语言模型（LLaMA-3）构建的问答系统，专门用于空间天气和太阳物理学的教育领域。该模型使用科学文献和由GPT-4生成、经Grok-3优化的问答数据进行训练，旨在提供科学准确且易于理解的教育解释。研究采用LLM-as-judge评估框架，根据科学准确性、清晰度、完整性和教学效果等结构化标准评估生成答案的质量。结果表明，SolarGPT-QA在零样本设置下相对于通用模型表现出色，在空间天气和太阳物理学的教育解释任务上，与经过指令微调的模型相比具有竞争力。消融研究表明，结合领域自适应预训练和微调对于平衡科学准确性和教学效果至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Solar activity, including solar flares, coronal mass ejections (CMEs), and geomagnetic storms can significantly impact satellites, aviation, power grids, data centers, and space missions. Extreme solar events can cause substantial economic damage with limited advance warning, underscoring the importance of early warning systems, accurate forecasting, and effective education in space science. Although large language models (LLMs) perform well on general tasks, they often lack domain specific knowledge and pedagogical capability to clearly explain complex space science concepts. We introduce SolarGPT-QA, a question answering system based on a domain adapted large language model built on the LLaMA-3 base model. The model is trained using scientific literature and large scale question and answer data generated with GPT-4 and refined using Grok-3 in a student friendly storytelling style. To evaluate response quality, we employ an LLM-as-judge evaluation framework, where a strong reference model assesses generated answers using structured criteria including scientific accuracy, clarity, completeness, and pedagogical effectiveness. Results show that SolarGPT-QA performs strongly relative to general purpose models in zero shot settings and achieves competitive performance compared to instruction tuned models for educational explanations in space weather and heliophysics. Ablation studies indicate that combining domain adaptive pretraining with fine tuning is important for balancing scientific accuracy and educational effectiveness.

</details>

---

### 51. [Aletheia: What Makes RLVR For Code Verifiers Tick?](https://arxiv.org/abs/2601.12186)

**基本信息**

- 🔗 arXiv: [`2601.12186`](https://arxiv.org/abs/2601.12186)
- 👥 作者: Vatsal Venkatkrishna, Indraneil Paul, Iryna Gurevych
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.12186.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析并优化用于代码验证的大语言模型（LLM）的训练方法（RLVR）。这直接涉及“化学大模型”主题中关于大模型训练、优化及其在特定任务（此处为代码验证，可类比复杂推理任务）中应用的研究。

**📖 中文摘要**

本文介绍了Aletheia，一个用于分析代码验证器（verifier）性能的受控测试平台。研究重点在于消融分析强化学习与可验证奖励（RLVR）训练方法中的三个关键驱动因素：中间思维轨迹、从负样本中学习以及在线策略训练。论文发现，对于代码验证器而言，最优的训练配方取决于模型规模：对于小型验证器，在线策略学习是主要性能驱动因素；而对于大型模型，思维轨迹则成为最关键的因素。此外，负样本能稳定大型模型的训练，并且推理时的计算扩展无法弥补任何核心RLVR组件的缺失。这些发现为从业者提供了基于计算效率最优化的路线图，以简化验证器训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-domain thinking verifiers trained via Reinforcement Learning with Verifiable Rewards (RLVR) are a cornerstone of modern post-training. However, their adoption in code generation has lagged behind execution feedback due to the prohibitive costs of the full RLVR pipeline. In this work, we ablate three primary drivers of RLVR performance and cost: intermediate thinking traces, learning from negative samples, and on-policy training. We introduce Aletheia, a controlled, execution-grounded testbed to facilitate a contamination-free analysis of code verifiers across disparate model sizes and covariate shifts. Our analysis reveals that the optimal training recipe is scale-dependent: on-policy learning is the primary performance driver for small verifiers, whereas thinking traces become the most vital factor for larger sizes. Furthermore, we show that negative samples stabilize training at large sizes, and scaling inference-time compute cannot compensate for any core RLVR component. These findings provide a compute-optimal roadmap for practitioners, offering concrete strategies to simplify verifier training based on model size. Consequently, our work establishes a foundation for scalable supervision, enabling efficiently trained code verifiers to reliably supervise much larger code generation policies.

</details>

---

### 52. [Semantic Identity Compression: Exact Zero-Error Laws, Rate-Distortion, and Neurosymbolic Necessity](https://arxiv.org/abs/2601.14252)

**基本信息**

- 🔗 arXiv: [`2601.14252`](https://arxiv.org/abs/2601.14252)
- 👥 作者: Tristan Simas
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.14252.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从信息论和表示学习的角度，深入分析神经符号系统中语义表示与精确身份之间的根本矛盾。这直接关联“化学大模型”主题中关于模型表示能力、语义理解以及神经符号集成等核心问题。

**📖 中文摘要**

本文研究了符号系统与神经嵌入在表示精确身份（identity）时的根本差异。符号系统操作于精确身份（如变量、指针、数据库键），而神经嵌入通过压缩语义细节进行泛化，但这会导致碰撞模糊性：多个不同实体可能共享相同的表示值。论文精确刻画了从这种表示中恢复精确身份所需额外信息量，该量由表示映射的碰撞纤维几何结构控制。研究证明了紧致的固定长度逆定理、精确的有限块缩放定律、点态自适应预算，以及当身份位被保留时的率失真权衡。研究结论指出，这种残余模糊性是结构性的而非表示特定的，因此符号身份机制（句柄、键、指针、名义标签）是任何非单射语义表示的必要系统级补充。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Symbolic systems operate over exact identities: variables denote specific objects, pointers target precise memory locations, and database keys refer to singular records. Neural embeddings generalize by compressing away semantic detail, but this compression creates collision ambiguity: multiple distinct entities can share the same representation value. We characterize exactly how much additional information must be supplied to recover precise identity from such representations. The answer is controlled by a single combinatorial object: the collision-fiber geometry of the representation map $\pi$. Let $A_{\pi}=\max_u |\pi^{-1}(u)|$ be the largest collision fiber. We prove a tight fixed-length converse $L \ge \log_2 A_{\pi}$, an exact finite-block scaling law, a pointwise adaptive budget $\lceil \log_2 |\pi^{-1}(u)|\rceil$, and the rate-distortion tradeoff with an explicit distortion floor when identity bits are withheld. The same fiber geometry determines query complexity and canonical structure for distinguishing families. Because this residual ambiguity is structural rather than representation-specific, symbolic identity mechanisms (handles, keys, pointers, nominal tags) are the necessary system-level complement to any non-injective semantic representation. All main results are machine-checked in Lean 4. Keywords: semantics-aware compression, zero-error coding, neurosymbolic systems, learned representations, side information

</details>

---

### 53. [VisTIRA: Closing the Image-Text Modality Gap in Visual Math Reasoning via Structured Tool Integration](https://arxiv.org/abs/2601.14440)

**基本信息**

- 🔗 arXiv: [`2601.14440`](https://arxiv.org/abs/2601.14440)
- 👥 作者: Saeed Khaki, Ashudeep Singh, Nima Safaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.14440.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升视觉语言模型（VLM）在视觉数学推理任务上的性能，通过引入工具集成推理框架（VisTIRA）和特定的训练数据生成方法。这属于“化学大模型”主题中关于多模态大模型（结合视觉和语言）在复杂科学推理任务上应用和优化的研究。

**📖 中文摘要**

本文指出，当数学问题以图像形式（如排版公式）而非文本形式呈现时，视觉语言模型（VLM）的数学推理能力会显著落后于纯文本语言模型。作者将这种现象定义为“模态鸿沟”。为了弥合这一鸿沟，论文引入了VisTIRA（视觉与工具集成推理智能体），一个集成了工具使用的推理框架。该框架通过迭代地将给定的数学问题图像分解为自然语言推理步骤和可执行的Python代码，以结构化方式解决问题。此外，论文还构建了一个评估和提升视觉数学推理的框架，包括一个将思维链数学语料库转换为具有挑战性的图像对应物的LaTeX流程，以及一个用于微调VLM的大规模合成工具使用轨迹数据集。实验表明，工具集成的监督能提升基于图像的推理能力，而OCR grounding（光学字符识别 grounding）能进一步缩小小型模型的模态鸿沟。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-language models (VLMs) lag behind text-only language models on mathematical reasoning when the same problems are presented as images rather than text. We empirically characterize this as a modality gap: the same question in text form yields markedly higher accuracy than its visually typeset counterpart, due to compounded failures in reading dense formulas, layout, and mixed symbolic-diagrammatic context. First, we introduce VisTIRA (Vision and Tool-Integrated Reasoning Agent), a tool-integrated reasoning framework that enables structured problem solving by iteratively decomposing a given math problem (as an image) into natural language rationales and executable Python steps to determine the final answer. Second, we build a framework to measure and improve visual math reasoning: a LaTeX-based pipeline that converts chain-of-thought math corpora (e.g., NuminaMath) into challenging image counterparts, and a large set of synthetic tool-use trajectories derived from a real-world, homework-style image dataset (called SnapAsk) for fine-tuning VLMs. Our experiments show that tool-integrated supervision improves image-based reasoning, and OCR grounding can further narrow the gap for smaller models, although its benefit diminishes at scale. These findings highlight that modality gap severity inversely correlates with model size, and that structured reasoning and OCR-based grounding are complementary strategies for advancing visual mathematical reasoning.

</details>

---

### 54. [CARE: A Molecular-Guided Foundation Model with Adaptive Region Modeling for Whole Slide Image Analysis](https://arxiv.org/abs/2602.21637)

**基本信息**

- 🔗 arXiv: [`2602.21637`](https://arxiv.org/abs/2602.21637)
- 👥 作者: Di Zhang, Zhangpeng Gong, Xiaobo Pang 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21637.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于计算病理学的多模态基础模型（CARE），该模型整合了组织形态学图像和分子（RNA、蛋白质）数据。这直接属于“化学大模型”主题的范畴，即开发用于化学、生物医学等多模态科学数据的大型AI模型。

**📖 中文摘要**

本文提出了CARE（跨模态自适应区域编码器），一种用于病理学全切片图像（WSI）分析的基础模型。CARE能够自动将WSI分割成多个形态学相关的区域。其预训练分为两个阶段：首先是无监督的单模态预训练，从大量未标注的WSI中学习形态学表示；其次是跨模态对齐阶段，利用RNA和蛋白质表达谱来细化和构建自适应区域。这种分子引导使CARE能够识别生物学相关模式，并生成不规则但连贯的组织区域，选择最具代表性的区域作为感兴趣区域（ROI）。CARE支持广泛的病理学相关任务，在仅使用主流基础模型十分之一的预训练数据的情况下，在33个下游基准测试（包括形态分类、分子预测和生存分析）中取得了优异的平均性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models have recently achieved impressive success in computational pathology, demonstrating strong generalization across diverse histopathology tasks. However, existing models overlook the heterogeneous and non-uniform organization of pathological regions of interest (ROIs) because they rely on natural image backbones not tailored for tissue morphology. Consequently, they often fail to capture the coherent tissue architecture beyond isolated patches, limiting interpretability and clinical relevance. To address these challenges, we present Cross-modal Adaptive Region Encoder (CARE), a foundation model for pathology that automatically partitions WSIs into several morphologically relevant regions. Specifically, CARE employs a two-stage pretraining strategy: (1) a self-supervised unimodal pretraining stage that learns morphological representations from 34,277 whole-slide images (WSIs) without segmentation annotations, and (2) a cross-modal alignment stage that leverages RNA and protein profiles to refine the construction and representation of adaptive regions. This molecular guidance enables CARE to identify biologically relevant patterns and generate irregular yet coherent tissue regions, selecting the most representative area as ROI. CARE supports a broad range of pathology-related tasks, using either the ROI feature or the slide-level feature obtained by aggregating adaptive regions. Based on only one-tenth of the pretraining data typically used by mainstream foundation models, CARE achieves superior average performance across 33 downstream benchmarks, including morphological classification, molecular prediction, and survival analysis, and outperforms other foundation model baselines overall.

</details>

---

### 55. [Model Medicine: A Clinical Framework for Understanding, Diagnosing, and Treating AI Models](https://arxiv.org/abs/2603.04722)

**基本信息**

- 🔗 arXiv: [`2603.04722`](https://arxiv.org/abs/2603.04722)
- 👥 作者: Jihoon Jeong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04722.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一个全新的、系统性的框架（“模型医学”）来诊断和理解大型AI模型（如大语言模型）的内部状态和行为。这直接关联“化学大模型”主题中关于大模型的可解释性、诊断、评估和治理等前沿问题。

**📖 中文摘要**

本文提出了“模型医学”作为一个研究计划，旨在系统性地理解、诊断、治疗和预防AI模型中的“疾病”。论文将AI模型类比为生物有机体，认为其具有内部结构、动态过程、可遗传特征、可观察症状、可分类状态和可治疗状态。作者贡献包括：一个包含15个子学科的学科分类法；一个基于行为遗传学的“四层外壳模型”框架；一个开源的诊断工具“神经MRI”（将医学神经影像模态映射到AI可解释性技术）；一个五层诊断框架；以及包括模型气质指数、模型症状学和标准化病例报告在内的临床模型科学。论文还提出了分层核心假设和一个连接诊断与治疗的治疗框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Model Medicine is the science of understanding, diagnosing, treating, and preventing disorders in AI models, grounded in the principle that AI models -- like biological organisms -- have internal structures, dynamic processes, heritable traits, observable symptoms, classifiable conditions, and treatable states. This paper introduces Model Medicine as a research program, bridging the gap between current AI interpretability research (anatomical observation) and the systematic clinical practice that complex AI systems increasingly require. We present five contributions: (1) a discipline taxonomy organizing 15 subdisciplines across four divisions -- Basic Model Sciences, Clinical Model Sciences, Model Public Health, and Model Architectural Medicine; (2) the Four Shell Model (v3.3), a behavioral genetics framework empirically grounded in 720 agents and 24,923 decisions from the Agora-12 program, explaining how model behavior emerges from Core--Shell interaction; (3) Neural MRI (Model Resonance Imaging), a working open-source diagnostic tool mapping five medical neuroimaging modalities to AI interpretability techniques, validated through four clinical cases demonstrating imaging, comparison, localization, and predictive capability; (4) a five-layer diagnostic framework for comprehensive model assessment; and (5) clinical model sciences including the Model Temperament Index for behavioral profiling, Model Semiology for symptom description, and M-CARE for standardized case reporting. We additionally propose the Layered Core Hypothesis -- a biologically-inspired three-layer parameter architecture -- and a therapeutic framework connecting diagnosis to treatment.

</details>

---

### 56. [Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing](https://arxiv.org/abs/2603.15011)

**基本信息**

- 🔗 arXiv: [`2603.15011`](https://arxiv.org/abs/2603.15011)
- 👥 作者: Jiahe Song, Chuang Wang, Yinfan Wang 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15011.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过增强视觉语言模型来解析化学反应图，这直接涉及化学结构的理解和推理，与“化学大模型”和“质谱结构推理”（作为化学结构解析和推理的一种形式）主题高度相关。

**📖 中文摘要**

本文提出了一种用于化学反应图解析（RxnDP）的新方法，旨在从文献中提取化学合成信息。该方法从提示表示和学习范式两个互补的角度增强了基于视觉语言模型（VLM）的RxnDP。首先，提出了“标识符作为视觉提示”（IdtVP），利用分子标识符（如粗体数字1a）来激活VLM预训练期间获得的化学知识，从而实现了强大的零样本和分布外泛化能力。其次，为了在微调范式中进一步优化性能，引入了Re3-DAPO，这是一种利用可验证奖励直接优化反应级指标的强化学习算法。此外，还发布了ScannedRxn基准数据集，包含带有真实世界伪影的扫描历史反应图，以严格评估模型的鲁棒性和分布外能力。这项工作直接针对化学信息学中的“化学大模型”（用于解析和理解化学结构）和“质谱结构推理”（作为理解化学结构的一种形式）主题，通过改进的VLM方法推进了化学结构解析的准确性和泛化性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reaction diagram parsing (RxnDP) is critical for extracting chemical synthesis information from literature. Although recent Vision-Language Models (VLMs) have emerged as a promising paradigm to automate this complex visual reasoning task, their application is fundamentally bottlenecked by the inability to align visual chemical entities with pre-trained knowledge, alongside the inherent discrepancy between token-level training and reaction-level evaluation. To address these dual challenges, this work enhances VLM-based RxnDP from two complementary perspectives: prompting representation and learning paradigms. First, we propose Identifier as Visual Prompting (IdtVP), which leverages naturally occurring molecule identifiers (e.g., bold numerals like 1a) to activate the chemical knowledge acquired during VLM pre-training. IdtVP enables powerful zero-shot and out-of-distribution capabilities, outperforming existing prompting strategies. Second, to further optimize performance within fine-tuning paradigms, we introduce Re3-DAPO, a reinforcement learning algorithm that leverages verifiable rewards to directly optimize reaction-level metrics, thereby achieving consistent gains over standard supervised fine-tuning. Additionally, we release the ScannedRxn benchmark, comprising scanned historical reaction diagrams with real-world artifacts, to rigorously assess model robustness and out-of-distribution ability. Our contributions advance the accuracy and generalization of VLM-based reaction diagram parsing. We will release data, models, and code on GitHub.

</details>

---

### 57. [General Mechanism of Evolution Shared by Proteins and Words](https://arxiv.org/abs/2012.14309)

**基本信息**

- 🔗 arXiv: [`2012.14309`](https://arxiv.org/abs/2012.14309)
- 👥 作者: Li-Min Wang, Hsing-Yi Lai, Sun-Ting Tsai 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2012.14309.pdf)

**💡 相关性分析**

满足标准1和3：论文核心主题是探索蛋白质和语言的进化机制，并明确提到了蛋白质语言建模（Protein language modeling），这直接与“化学大模型”（特别是用于蛋白质的AI模型）主题相关。同时，论文对蛋白质序列分析和语言模型之间的类比进行了广泛的讨论和展望，具有综述和展望的性质。

**📖 中文摘要**

本文探讨了蛋白质序列和人类语言文本等复杂系统共有的进化机制。通过类比生物学和语言学，论文提出了一个通用的进化数学公式，该公式通过最小努力原理（以熵的形式）量化自然选择，并解释了幂律行为的起源以及环境变化如何刺激新蛋白质和新词汇的出现。研究发现，生命和语言在多个层次上存在对应关系，并展示了复杂适应系统进化的新基本物理特性。这些统计测试可以作为定量标准，来检验序列进化理论是否与真实数据的规律性一致。这项工作为使用计算基础来表征和分析蛋白质序列、人类语料库及其进化提供了支持，与利用大模型（如蛋白质语言模型）进行化学信息学研究的主题密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Complex systems, such as life and languages, are governed by principles of evolution. The analogy and comparison between biology and linguistics\cite{alphafold2, RoseTTAFold, lang_virus, cell language, faculty1, language of gene, Protein linguistics, dictionary, Grammar of pro_dom, complexity, genomics_nlp, InterPro, language modeling, Protein language modeling} provide a computational foundation for characterizing and analyzing protein sequences, human corpora, and their evolution. However, no general mathematical formula has been proposed so far to illuminate the origin of quantitative hallmarks shared by life and language. Here we show several new statistical relationships shared by proteins and words, which inspire us to establish a general mechanism of evolution with explicit formulations that can incorporate both old and new characteristics. We found natural selection can be quantified via the entropic formulation by the principle of least effort to determine the sequence variation that survives in evolution. Besides, the origin of power law behavior and how changes in the environment stimulate the emergence of new proteins and words can also be explained via the introduction of function connection network. Our results demonstrate not only the correspondence between genetics and linguistics over their different hierarchies but also new fundamental physical properties for the evolution of complex adaptive systems. We anticipate our statistical tests can function as quantitative criteria to examine whether an evolution theory of sequence is consistent with the regularity of real data. In the meantime, their correspondence broadens the bridge to exchange existing knowledge, spurs new interpretations, and opens Pandora's box to release several potentially revolutionary challenges. For example, does linguistic arbitrariness conflict with the dogma that structure determines function?

</details>

---

### 58. [Predicting Biomedical Interactions with Probabilistic Model Selection for Graph Neural Networks](https://arxiv.org/abs/2211.13231)

**基本信息**

- 🔗 arXiv: [`2211.13231`](https://arxiv.org/abs/2211.13231)
- 👥 作者: Kishan KC, Rui Li, Paribesh Regmi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2211.13231.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发用于预测生物医学相互作用（如分子间相互作用）的图神经网络模型，这属于化学信息学中利用AI模型进行分子性质预测和关系推理的核心主题，与“化学大模型”广义相关。

**📖 中文摘要**

本文提出了一种贝叶斯模型选择框架，用于预测生物医学相互作用（如蛋白质-蛋白质相互作用）。该框架基于图神经网络（GNNs），能够联合推断数据支持的最合理的图卷积层数、应用dropout正则化并学习网络参数。该方法解决了为给定生物医学网络确定适当GNN深度的挑战，避免了启发式或大量实验带来的不可靠性或高计算开销。在四个生物医学相互作用数据集上的实验表明，该方法优于竞争方法，通过允许GNN调整其深度以适应各种生物医学网络中的相互作用信息，提供了经过良好校准的预测。这项工作属于利用图神经网络等AI模型进行生物分子相互作用预测的范畴，是化学信息学和生物信息学的交叉领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Heterogeneous molecular entities and their interactions, commonly depicted as a network, are crucial for advancing our systems-level understanding of biology. With recent advancements in high-throughput data generation and a significant improvement in computational power, graph neural networks (GNNs) have demonstrated their effectiveness in predicting biomedical interactions. Since GNNs follow a neighborhood aggregation scheme, the number of graph convolution (GC) layers (i.e., depth) determines the neighborhood orders from which they can aggregate information, thereby significantly impacting the model's performance. However, it often relies on heuristics or extensive experimentation to determine an appropriate GNN depth for a given biomedical network. These methods can be unreliable or result in expensive computational overhead. Moreover, GNNs with more GC layers tend to exhibit poor calibration, leading to high confidence in incorrect predictions. To address these challenges, we propose a Bayesian model selection framework to jointly infer the most plausible number of GC layers supported by the data, apply dropout regularization, and learn network parameters. Experiments on four biomedical interaction datasets demonstrate that our method achieves superior performance over competing methods, providing well-calibrated predictions by allowing GNNs to adapt their depths to accommodate interaction information from various biomedical networks. Source code and data is available at: this https URL

</details>

---

### 59. [From structure mining to unsupervised exploration of atomic octahedral networks](https://arxiv.org/abs/2306.12272)

**基本信息**

- 🔗 arXiv: [`2306.12272`](https://arxiv.org/abs/2306.12272)
- 👥 作者: R. Patrick Xian, Ryan J. Morelock, Ido Hadar 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2306.12272.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种无监督机器学习工作流，用于分析和分类材料化学中的原子级结构网络（八面体网络）。这属于化学信息学中利用AI和数据分析方法从材料结构数据中提取知识和规律的范畴，与“化学大模型”（用于材料发现和结构分析）主题相关。

**📖 中文摘要**

本文提出了一种自动化工作流，用于对原子中心配位八面体网络进行几何解析、量化和无监督机器学习分类。该工作流程将化学直觉操作化，以分析材料化学中八面体网络的大规模数据集。研究将其应用于两个数据集：计算生成的单一氧化物钙钛矿多晶型物和实验测量的杂化碘铂酸盐。对于钙钛矿，该方法揭示了轴依赖性倾斜趋势，有助于检测氧化态变化。对于碘铂酸盐，该方法对其八面体网络进行了分类，揭示了配位环境的类鲍林连接规则及其结构多样性背后的设计原理。这项工作展示了在材料化学中原子八面体网络广阔设计空间的一瞥，并为高通量、有针对性地筛选特定结构类型提供了信息。该方法的核心是利用无监督机器学习从结构数据中挖掘知识和模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the spatial arrangements of atom-centered coordination octahedra is crucial for relating structures to properties for many materials families. Traditional case-by-case inspection becomes a prohibitive task for discovering trends and similarities in large datasets. Here, we operationalize chemical intuition to automate the geometric parsing, quantification, and classification of coordination octahedral networks using unsupervised machine learning. We apply the workflow to analyze two datasets to demonstrate its effectiveness. For computationally generated single oxide perovskite (ABO$_{3}$) polymorphs, we uncover axis-dependent tilting trends which assist in detecting oxidation state changes. For hybrid iodoplumbates (A$_x$Pb$_y$I$_z$) from measured structures, we taxonomize their octahedral networks, revealing a Pauling-like connectivity rule for the coordination environment and the design principles underpinning their structural diversity. Our results offer a glimpse into the vast design space of atomic octahedral networks in materials chemistry and inform high-throughput, targeted screening of specific structure types.

</details>

---

### 60. [Making Multi-Axis Gaussian Graphical Models Scalable to Millions of Cells](https://arxiv.org/abs/2407.19892)

**基本信息**

- 🔗 arXiv: [`2407.19892`](https://arxiv.org/abs/2407.19892)
- 👥 作者: Bailey Andrew, Erica L. Harris, James A. Poulter 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.19892.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的、可扩展的多轴高斯图模型方法（GmGM），并提供了相应的Python工具包。这为化学信息学和生物信息学中分析高通量组学数据（如单细胞转录组学）提供了新的数据分析和建模工具/资源，与利用计算模型处理化学/生物数据的主题相关。

**📖 中文摘要**

本文开发了一种能够处理百万细胞数据集的多轴高斯图模型方法。传统方法在学习基因或细胞网络时通常做出错误的“独立性假设”，而现有的“多轴”方法无法扩展到几千个细胞或基因以上。本文提出的方法解决了这一可扩展性限制，能够在几分钟内处理百万细胞数据集，从而使其能够应用于现代单细胞RNA测序数据集以及更复杂的数据集。研究表明，该方法从真实单细胞数据中产生了新的生物学见解，并与现有的hdWGCNA方法进行了有利比较。特别是，它识别了在神经元发育中可能具有调节或功能作用的长链非编码RNA基因。该方法作为Python包GmGM提供。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: Networks underlie the generation and interpretation of many biological datasets: gene networks shed light on the regulatory structure of the genome, and cell networks can capture structure of the tumor micro-environment. However, most methods that learn such networks make the faulty 'independence assumption'; to learn the gene network, they assume that no cell network exists. 'Multi-axis' methods, which do not make this assumption, fail to scale beyond a few thousand cells or genes. This limits their applicability to only the smallest datasets. Results: We develop a multi-axis method capable of processing million-cell datasets within minutes. This was previously impossible, and unlocks the use of such methods on modern scRNA-seq datasets, as well as more complex datasets. We show that our method yields novel biological insights from real single-cell data, and compares favorably to the existing hdWGCNA methodology. In particular, it identifies long non-coding RNA genes that potentially have a regulatory or functional role in neuronal development. Availability and implementation: Our methodology is available as a Python package GmGM on PyPI ( this https URL ). The code for all experiments performed in this paper is available on GitHub ( this https URL ). Contact: sceba@leeds. this http URL Supplementary information: Our proofs, and some additional experiments, are available in the supplementary material. Keywords: gaussian graphical models, multi-axis models, transcriptomics, multi-omics, scalability

</details>

---

### 61. [Towards Robust Multimodal Physiological Foundation Models: Handling Arbitrary Missing Modalities](https://arxiv.org/abs/2504.19596)

**基本信息**

- 🔗 arXiv: [`2504.19596`](https://arxiv.org/abs/2504.19596)
- 👥 作者: Wei-Bang Jiang, Xi Fu, Yi Ding 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.19596.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是构建一个能够处理任意缺失模态的多模态基础模型框架。这种方法论与化学信息学中整合多种化学数据模态（如质谱、核磁、分子图）进行“质谱结构推理”或构建“化学大模型”所面临的挑战直接相关。论文提出的框架本身可被视为一种通用的多模态建模工具/方法资源。

**📖 中文摘要**

本文提出了PhysioOmni，一个用于多模态生理信号分析的基础模型。该模型通过解耦多模态标记器进行训练，支持通过模态不变和模态特定的目标进行掩码信号预训练。为确保对多样化和不完整模态组合的适应性，预训练的编码器在下游数据集上通过原型对齐进行鲁棒微调。在四个下游任务（情绪识别、睡眠阶段分类、运动预测和心理负荷检测）上的大量实验表明，PhysioOmni实现了最先进的性能，同时对缺失模态保持强大的鲁棒性。虽然主要应用于生理信号，但该框架提出的处理多模态、缺失模态以及学习通用表示的方法，对于化学信息学中处理多模态数据（如结合质谱、光谱、分子结构）具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal physiological signals, such as EEG, ECG, EOG, and EMG, are crucial for healthcare and brain-computer interfaces. While existing methods rely on specialized architectures and dataset-specific fusion strategies, they struggle to learn universal representations that generalize across datasets and handle missing modalities at inference time. To address these issues, we propose PhysioOmni, a foundation model for multimodal physiological signal analysis that models both homogeneous and heterogeneous features to decouple multimodal signals and extract generic representations while maintaining compatibility with arbitrary missing modalities. PhysioOmni trains a decoupled multimodal tokenizer, enabling masked signal pre-training via modality-invariant and modality-specific objectives. To ensure adaptability to diverse and incomplete modality combinations, the pre-trained encoders undergo resilient fine-tuning with prototype alignment on downstream datasets. Extensive experiments on four downstream tasks, emotion recognition, sleep stage classification, motor prediction, and mental workload detection, demonstrate that PhysioOmni achieves state-of-the-art performance while maintaining strong robustness to missing modalities. Our code and model weights will be released.

</details>

---

### 62. [Beyond Polarity: Multi-Dimensional LLM Sentiment Signals for WTI Crude Oil Futures Return Prediction](https://arxiv.org/abs/2603.11408)

**基本信息**

- 🔗 arXiv: [`2603.11408`](https://arxiv.org/abs/2603.11408)
- 👥 作者: Dehao Dai, Ding Ma, Dou Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11408.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）提取多维特征进行预测分析。LLM作为当前“化学大模型”在自然语言处理领域的典型代表，其应用方法和特征提取策略对化学信息学领域（如从科学文献中提取化学知识）具有直接的参考和借鉴意义。

**📖 中文摘要**

本文探讨了利用大型语言模型（LLM）提取的多维情感信号来预测WTI原油期货周度收益率。研究超越了传统基于极性的情感分析方法，构建了涵盖相关性、极性、强度、不确定性和前瞻性五个维度的情感指标。这些指标基于GPT-4o、Llama 3.2-3b等LLM以及FinBERT、AlphaVantage等基准模型，从2020年至2025年的能源领域新闻文章中提取。研究发现，结合GPT-4o和FinBERT的模型取得了最佳预测效果，表明LLM模型与传统金融情感模型提供互补的预测信息。SHAP分析进一步显示，强度和不确定性相关特征是最重要的预测因子。这项工作展示了LLM在金融时间序列预测中的应用潜力，特别是通过提取更丰富、更细粒度的文本特征来增强预测能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Forecasting crude oil prices remains challenging because market-relevant information is embedded in large volumes of unstructured news and is not fully captured by traditional polarity-based sentiment measures. This paper examines whether multi-dimensional sentiment signals extracted by large language models improve the prediction of weekly WTI crude oil futures returns. Using energy-sector news articles from 2020 to 2025, we construct five sentiment dimensions covering relevance, polarity, intensity, uncertainty, and forwardness based on GPT-4o, Llama 3.2-3b, and two benchmark models, FinBERT and AlphaVantage. We aggregate article-level signals to the weekly level and evaluate their predictive performance in a classification framework. The best results are achieved by combining GPT-4o and FinBERT, suggesting that LLM-based and conventional financial sentiment models provide complementary predictive information. SHAP analysis further shows that intensity- and uncertainty-related features are among the most important predictors, indicating that the predictive value of news sentiment extends beyond simple polarity. Overall, the results suggest that multi-dimensional LLM-based sentiment measures can improve commodity return forecasting and support energy-market risk monitoring.

</details>

---

### 63. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一个整合了预训练基础模型（scGPT，一种针对单细胞数据的“化学/生物大模型”）和大型语言模型（LLM）的AI框架展开。该框架旨在从复杂的生物分子数据（单细胞转录组）中提取和解释信息，这与“化学大模型”在分析和推理复杂化学/生物数据（如质谱数据）方面的目标高度一致。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个可解释的混合生成式AI代理框架，用于在单细胞基因组学中进行基于表达的发现。ELISA将scGPT（一种用于单细胞RNA测序数据的预训练基础模型）的表达嵌入与基于BioBERT的语义检索以及由LLM介导的解释相结合。框架包含自动查询分类器，根据输入是基因特征、自然语言概念还是两者的混合，将查询路由到不同的处理流程。集成的分析模块直接在嵌入数据上执行通路活性评分、配体-受体相互作用预测、条件感知比较分析和细胞类型比例估计等任务，而无需访问原始计数矩阵。该工作在六个不同的scRNA-seq数据集上进行了基准测试，结果表明ELISA在细胞类型检索等方面显著优于基线方法，并能通过基于LLM的推理生成候选生物学假设。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 64. [Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery](https://arxiv.org/abs/2603.12567)

**基本信息**

- 🔗 arXiv: [`2603.12567`](https://arxiv.org/abs/2603.12567)
- 👥 作者: Jeffrey Hu, Rongzhi Dong, Ying Feng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和利用预训练的基础模型（Foundation Model， 即“大模型”）来解决材料科学中的关键问题（主动学习）。TabPFN作为一个在大量合成任务上预训练的Transformer模型，是“化学大模型”在表格数据回归任务中的一个具体实例和成功应用，直接证明了基础模型在化学相关领域（材料发现）的价值。

**📖 中文摘要**

本文针对材料发现中主动学习（AL）面临的小数据挑战，提出了“上下文主动学习”（ICAL）框架。该框架用TabPFN替代了传统的高斯过程（GP）和随机森林（RF）代理模型。TabPFN是一种基于Transformer的基础模型（FM），在数百万个合成回归任务上进行了预训练，从而元学习到了一个对表格数据的通用先验。在此基础上，TabPFN无需针对特定数据集进行重新训练，即可通过单次前向传播执行原则性的贝叶斯推理，提供强大的小数据回归性能和良好校准的预测不确定性（这对有效的AL至关重要）。研究在10个材料数据集上对ICAL与GP和RF进行了基准测试，TabPFN在8个数据集上胜出，平均节省了52%（相对于GP）和29.77%（相对于RF）的额外评估次数。交叉验证分析证实，TabPFN的优势源于其卓越的不确定性校准能力。这项工作证明了预训练的基础模型可以作为主动学习的有效代理，在材料科学等小数据实验科学中实现数据高效发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward promising candidates, reducing the number of costly synthesis-and-characterization cycles needed to identify optimal materials. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates, which suffer from complementary limitations: GP underfits complex composition-property landscapes due to rigid kernel assumptions, while RF produces unreliable heuristic uncertainty estimates in small-data regimes. This small-data challenge is pervasive in materials science, making reliable surrogate modeling extremely difficult with models trained from scratch on each new dataset. Here we propose In-Context Active Learning (ICAL), which addresses this bottleneck by replacing conventional surrogates with TabPFN, a transformer-based foundation model (FM) pre-trained on millions of synthetic regression tasks to meta-learn a universal prior over tabular data, upon which TabPFN performs principled Bayesian inference in a single forward pass without dataset-specific retraining, delivering strong small-data regression performance and well-calibrated predictive uncertainty (required for effective AL). We benchmark ICAL against GP and RF across 10 materials datasets and TabPFN wins on 8 out of 10 datasets, achieving a mean saving of 52% in extra evaluations relative to GP and 29.77% relative to RF. Cross-validation analysis confirms that TabPFN's advantage stems from superior uncertainty calibration, achieving the lowest Negative Log-Likelihood and Area Under the Sparsification Error curve among all surrogates. These results demonstrate that pre-trained FMs can serve as effective surrogates for active learning, enabling data-efficient discovery across diverse materials systems and small-data experimental sciences.

</details>

---

## 📊 数据统计
- 累计运行天数：38
- 累计论文数量：2732

## 📝 历史记录

> 暂无历史数据

