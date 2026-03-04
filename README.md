# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-04 01:28:02

## 📅 2026-03-04 (今日最新)

**相关论文数：116**

### 1. [From Global to Local: Learning Context-Aware Graph Representations for Document Classification and Summarization](https://arxiv.org/abs/2603.00021)

**基本信息**

- 🔗 arXiv: [`2603.00021`](https://arxiv.org/abs/2603.00021)
- 👥 作者: Ruangrin Ldallitsakool, Margarita Bugueño, Gerard de Melo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00021.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于图注意力网络（GAT）的文档表示学习方法，其核心技术与化学信息学中用于分子表示学习（分子图）和质谱数据（可建模为图或序列）结构推理的图神经网络方法在本质上是一致的，属于核心方法论相关。

**📖 中文摘要**

本文提出了一种数据驱动的方法，用于自动构建基于图的文档表示。该方法利用动态滑动窗口注意力模块来有效捕获句子之间局部和中等范围的语义依赖关系，以及文档内部的结构关系。在学习的图上训练的图注意力网络（GATs）在文档分类任务上取得了有竞争力的结果，同时比先前的方法需要更少的计算资源。论文还进一步探索了所提出的图构建方法在抽取式文档摘要中的应用。虽然论文主要关注通用文档处理，但其核心方法——利用图神经网络（GNNs）和注意力机制学习结构化表示——与化学信息学中分子图表示学习、化学大模型构建以及质谱数据（可视为图或序列）的结构推理在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper proposes a data-driven method to automatically construct graph-based document representations. Building upon the recent work of Bugueño and de Melo (2025), we leverage the dynamic sliding-window attention module to effectively capture local and mid-range semantic dependencies between sentences, as well as structural relations within documents. Graph Attention Networks (GATs) trained on our learned graphs achieve competitive results on document classification while requiring lower computational resources than previous approaches. We further present an exploratory evaluation of the proposed graph construction method for extractive document summarization, highlighting both its potential and current limitations. The implementation of this project can be found on GitHub.

</details>

---

### 2. [Property-Driven Evaluation of GNN Expressiveness at Scale: Datasets, Framework, and Study](https://arxiv.org/abs/2603.00044)

**基本信息**

- 🔗 arXiv: [`2603.00044`](https://arxiv.org/abs/2603.00044)
- 👥 作者: Sicong Che, Jiayi Yang, Sarfraz Khurshid 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00044.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统评估图神经网络（GNN）的表达能力。GNN是化学信息学和质谱分析中用于分子结构表示、性质预测和质谱结构推理的核心模型之一。因此，对GNN表达能力的系统性评估和理解直接关系到这些领域模型性能的提升，属于核心主题相关。

**📖 中文摘要**

本文提出了一个基于属性的图神经网络（GNN）表达能力评估框架。作者开发了一个可配置的图数据集生成器，创建了两个数据集家族：GraphRandom（包含满足或违反特定属性的多样化图）和GraphPerturb（引入受控的结构变化）。这些基准涵盖了分布式系统、知识图谱和生物网络中关键的16个基本图属性。论文提出了一个通用评估框架，用于评估GNN表达能力的三个关键方面：泛化性、敏感性和鲁棒性。利用该框架，作者首次全面研究了全局池化方法对GNN表达能力的影响。研究发现，注意力池化在泛化和鲁棒性方面表现出色，而二阶池化则提供更优的敏感性。这项工作将软件工程严谨性嵌入AI评估，为开发可靠且表达能力强的GNN架构奠定了原则性基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advancing trustworthy AI requires principled software engineering approaches to model evaluation. Graph Neural Networks (GNNs) have achieved remarkable success in processing graph-structured data, however, their expressiveness in capturing fundamental graph properties remains an open challenge. We address this by developing a property-driven evaluation methodology grounded in formal specification, systematic evaluation, and empirical study. Leveraging Alloy, a software specification language and analyzer, we introduce a configurable graph dataset generator that produces two dataset families: GraphRandom, containing diverse graphs that either satisfy or violate specific properties, and GraphPerturb, introducing controlled structural variations. Together, these benchmarks encompass 336 new datasets, each with at least 10,000 labeled graphs, covering 16 fundamental graph properties critical to distributed systems, knowledge graphs, and biological networks. We propose a general evaluation framework that assesses three key aspects of GNN expressiveness: generalizability, sensitivity, and robustness, with two novel quantitative metrics. Using this framework, we conduct the first comprehensive study on global pooling methods' impact on GNN expressiveness. Our findings reveal distinct trade-offs: attention-based pooling excels in generalization and robustness, while second-order pooling provides superior sensitivity, but no single approach consistently performs well across all properties. These insights highlight fundamental limitations and open research directions including adaptive property-aware pooling, scale-sensitive architectures, and robustness-oriented training. By embedding software engineering rigor into AI evaluation, this work establishes a principled foundation for developing expressive and reliable GNN architectures.

</details>

---

### 3. [LitBench: A Graph-Centric Large Language Model Benchmarking Tool For Literature Tasks](https://arxiv.org/abs/2603.00051)

**基本信息**

- 🔗 arXiv: [`2603.00051`](https://arxiv.org/abs/2603.00051)
- 👥 作者: Andreas Varvarigos, Ali Maatouk, Jiasheng Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00051.pdf)

**💡 相关性分析**

满足标准2：LitBench工具提供了一个系统化的流程，用于从领域文献中构建知识图（子图）和相应的数据集。这为化学信息学和质谱分析领域构建领域特定的化学知识图谱、文献数据集以及训练和评估专用模型（如化学大模型）提供了宝贵的工具和资源框架。

**📖 中文摘要**

本文介绍了LitBench，一个为文献相关任务设计和评估领域特定大语言模型（LLMs）的基准测试工具。其核心是一个数据管理流程，能够生成领域特定的文献子图，并根据生成的节点和边的文本属性构建训练和评估数据集。该工具支持用户选择任何领域（无论是高级领域还是专业交叉领域）来管理文献图。除了数据集管理，LitBench还定义了一套全面的文献任务，从节点和边级别分析到高级应用（如相关工作生成）。这些任务使LLMs能够在训练过程中内化领域特定知识，同时支持对模型性能进行严格评估。结果表明，在LitBench数据集上训练和评估的小型领域特定LLMs，与GPT-4o和DeepSeek-R1等最先进模型相比，取得了有竞争力的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While large language models (LLMs) have become the de facto framework for literature-related tasks, they still struggle to function as domain-specific literature agents due to their inability to connect pieces of knowledge and reason across domain-specific contexts, terminologies, and nomenclatures. This challenge underscores the need for a tool that facilitates such domain-specific adaptation and enables rigorous benchmarking across literature tasks. To that end, we introduce LitBench, a benchmarking tool designed to enable the development and evaluation of domain-specific LLMs tailored to literature-related tasks. At its core, LitBench uses a data curation process that generates domain-specific literature sub-graphs and constructs training and evaluation datasets based on the textual attributes of the resulting nodes and edges. The tool is designed for flexibility, supporting the curation of literature graphs across any domain chosen by the user, whether high-level fields or specialized interdisciplinary areas. In addition to dataset curation, LitBench defines a comprehensive suite of literature tasks, ranging from node and edge level analyses to advanced applications such as related work generation. These tasks enable LLMs to internalize domain-specific knowledge and relationships embedded in the curated graph during training, while also supporting rigorous evaluation of model performance. Our results show that small domain-specific LLMs trained and evaluated on LitBench datasets achieve competitive performance compared to state-of-the-art models like GPT-4o and DeepSeek-R1. To enhance accessibility and ease of use, we open-source the tool along with an AI agent tool that streamlines data curation, model training, and evaluation.

</details>

---

### 4. [DeepXiv-SDK: An Agentic Data Interface for Scientific Papers](https://arxiv.org/abs/2603.00084)

**基本信息**

- 🔗 arXiv: [`2603.00084`](https://arxiv.org/abs/2603.00084)
- 👥 作者: Hongjin Qian, Ziyi Xia, Ze Liu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00084.pdf)

**💡 相关性分析**

满足标准2：DeepXiv-SDK是一个专门为科学论文（包括arXiv上的预印本）设计的数据接口和工具，它提供了结构化的、可编程的访问方式。这对于化学信息学和质谱分析领域的研究者系统化地收集、处理和分析相关科研论文（作为构建化学大模型或质谱结构推理模型的数据源）具有直接的工具价值。

**📖 中文摘要**

本文介绍了DeepXiv-SDK，这是一个为科学论文设计的智能数据接口，旨在标准化访问、提供预算感知的视图，并将证据定位视为一等操作。DeepXiv-SDK支持渐进式访问，与智能体分配注意力和阅读预算的方式保持一致。它提供了结构化的视图：用于筛选的标题优先视图、用于定向导航的章节结构视图，以及用于验证的按需证据级别访问。每一层都增加了丰富的属性和明确的预算提示，使智能体能够在升级到全文处理之前平衡相关性、成本和证据定位。DeepXiv-SDK还支持对论文属性的多面检索和聚合，实现对论文集的约束驱动搜索和管理。该工具目前部署在arXiv规模上，并与新版本每日同步，旨在扩展到其他开放获取语料库（如PubMed Central, bioRxiv）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Research agents are increasingly used in AI4Science for scientific information seeking and evidence-grounded decision making. Yet a persistent bottleneck is paper access: agents typically retrieve PDF/HTML pages, heuristically parse them, and ingest long unstructured text, leading to token-heavy reading and brittle evidence lookup. This motivates an agentic data interface for scientific papers that standardizes access, exposes budget-aware views, and treats grounding as a first-class operation. We introduce DeepXiv-SDK, which enables progressive access aligned with how agents allocate attention and reading budget. DeepXiv-SDK exposes as structured views a header-first view for screening, a section-structured view for targeted navigation, and on-demand evidence-level access for verification. Each layer is augmented with enriched attributes and explicit budget hints, so agents can balance relevance, cost, and grounding before escalating to full-text processing. DeepXiv-SDK also supports multi-faceted retrieval and aggregation over paper attributes, enabling constraint-driven search and curation over paper sets. DeepXiv-SDK is currently deployed at arXiv scale with daily synchronization to new releases and is designed to extend to other open-access corpora (e.g., PubMed Central, bioRxiv). We release RESTful APIs, an open-source Python SDK, and a web demo showcasing deep search and deep research workflows; the service is free to use with registration.

</details>

---

### 5. [SciKGDash: The Scientific Knowledge Graph Dashboard for Supporting Knowledge Curation](https://arxiv.org/abs/2603.00107)

**基本信息**

- 🔗 arXiv: [`2603.00107`](https://arxiv.org/abs/2603.00107)
- 👥 作者: Lena John, Sören Auer, Oliver Karras
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00107.pdf)

**💡 相关性分析**

满足标准2：SciKGDash是一个专门用于研究知识图谱（RKG）知识管理的仪表板工具。在化学信息学领域，构建和管理化学知识图谱（如化合物、反应、性质、文献关联）是核心任务。该工具为化学知识图谱的构建、质量控制和可视化提供了潜在的可借鉴框架和工具资源。

**📖 中文摘要**

本文介绍了SciKGDash，一个旨在支持开放研究知识图谱（ORKG）知识管理的仪表板。SciKGDash是作为与ORKG的管理与社区建设团队合作进行的行动研究的一部分而开发的，它是一个最小可行产品，专门满足该团队的需求，并有可能适配到其他研究知识图谱。该仪表板提供实时更新和可视化概览，以支持混合管理方法（结合自动化流程和人工监督）。一项有15名参与者参与的实验证明了SciKGDash的可用性，成功在5分钟内完成了5项管理任务中的4项。此外，SciKGDash获得了积极的用户体验评分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Research knowledge graphs (RKGs) have emerged as essential technology for organizing scientific knowledge, but their success depends heavily on the quality of their underlying content. Knowledge curation is a critical task to ensure the quality of (research) knowledge graphs ((R)KGs), with human curation being the gold standard despite its time- and resource-intensive nature. Automated methods, while efficient, lack the precision of human expertise. Hybrid approaches, combining automated processes with human oversight, offer a promising solution to this challenge. Dashboards can act as supportive tools in hybrid curation approaches, offering real-time updates and visual overviews. This paper presents an action research study, conducted in collaboration with the Curation and Community Building (C&CB) team of the Open Research Knowledge Graph (ORKG), to explore the development of a dashboard, called SciKGDash, designed to support knowledge curation of the ORKG. SciKGDash serves as a minimum viable product (MVP) tailored to the needs of the C&CB team, with potential for adaptation to other (R)KGs. An experiment with 15 participants demonstrated the usability of SciKGDash, with successful completion of 4 out of 5 curation tasks in under 5 minutes. In addition, SciKGDash received a positive user experience rating (UEQ score of 1.93). While the tailored solution proved effective for the ORKG, the research also highlights limitations in applying specific quality metrics across diverse (R)KGs. Future work should focus on identifying common quality metrics and enhancing SciKGDash with user-friendly features for querying customized quality metrics. Overall, knowledge curation in RKGs remains an under-explored field, warranting further research.

</details>

---

### 6. [GrapHist: Graph Self-Supervised Learning for Histopathology](https://arxiv.org/abs/2603.00143)

**基本信息**

- 🔗 arXiv: [`2603.00143`](https://arxiv.org/abs/2603.00143)
- 👥 作者: Sevda Öğüt, Cédric Vincent-Cuaz, Natalia Dubljevic 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00143.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发用于组织病理学图像的图自监督学习框架（GrapHist）。虽然应用领域是生物医学，但其核心技术——基于细胞图（一种特殊的图结构数据）的表示学习和预训练——与化学信息学中基于分子图（另一种图结构数据）的表示学习和预训练（这是构建化学大模型的关键步骤）在方法论上高度同源，属于核心主题相关。

**📖 中文摘要**

本文提出了GrapHist，一个用于组织病理学的新型基于图的自监督学习框架。该框架将组织建模为细胞图，并整合了掩码自编码器和异质图神经网络，旨在捕获肿瘤微环境的异质性。作者在从乳腺组织提取的1100万个细胞图上对GrapHist进行了预训练，并评估了其在领域内和领域外基准测试上的可迁移性。结果表明，GrapHist在切片级、区域级和细胞级任务上取得了与基于视觉的方法相竞争的性能，同时参数数量减少了四倍。它在癌症亚型分型任务上也大幅优于完全监督的图模型。此外，作者还发布了研究中使用的五个基于图的数字病理学数据集，建立了该领域首个大规模图基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Self-supervised vision models have achieved notable success in digital pathology. However, their domain-agnostic transformer architectures are not originally designed to account for fundamental biological elements of histopathology images, namely cells and their complex interactions. In this work, we hypothesize that a biologically-informed modeling of tissues as cell graphs offers a more efficient representation learning. Thus, we introduce GrapHist, a novel graph-based self-supervised learning framework for histopathology, which learns generalizable and structurally-informed embeddings that enable diverse downstream tasks. GrapHist integrates masked autoencoders and heterophilic graph neural networks that are explicitly designed to capture the heterogeneity of tumor microenvironments. We pre-train GrapHist on a large collection of 11 million cell graphs derived from breast tissues and evaluate its transferability across in- and out-of-domain benchmarks. Our results show that GrapHist achieves competitive performance compared to its vision-based counterparts in slide-, region-, and cell-level tasks, while requiring four times fewer parameters. It also drastically outperforms fully-supervised graph models on cancer subtyping tasks. Finally, we also release five graph-based digital pathology datasets used in our study at this https URL , establishing the first large-scale graph benchmark in this field. Our code is available at this https URL .

</details>

---

### 7. [Pulse-Driven Neural Architecture: Learnable Oscillatory Dynamics for Robust Continuous-Time Sequence Processing](https://arxiv.org/abs/2603.00153)

**基本信息**

- 🔗 arXiv: [`2603.00153`](https://arxiv.org/abs/2603.00153)
- 👥 作者: Paras Sharma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00153.pdf)

**💡 相关性分析**

满足标准1：论文提出的PDNA架构通过引入可学习的振荡动力学来增强连续时间序列处理能力，这种方法论与构建能够处理复杂时序信号（如质谱数据）的化学大模型核心思想相关。

**📖 中文摘要**

本文介绍了PDNA（脉冲驱动神经架构），一种为连续时间循环网络添加可学习振荡动力学的方法。该方法建立在闭式连续时间网络基础上，通过添加脉冲模块和自注意力模块来增强网络处理连续时间序列的能力。虽然论文主要关注通用序列处理，但其核心方法——通过结构化振荡动力学增强网络对时序信号的建模能力——与化学信息学中处理时序质谱信号（如色谱-质谱联用数据）或构建具有内部动态的化学大模型有潜在关联。论文中展示的模型对输入中断的鲁棒性提升，为处理噪声大、信号不完整的质谱数据提供了思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce PDNA (Pulse-Driven Neural Architecture), a method for augmenting continuous-time recurrent networks with learnable oscillatory dynamics that maintain internal state evolution independently of external input. Built on Closed-form Continuous-time (CfC) networks, PDNA adds two components: (1) a pulse module that generates structured oscillations $A \cdot \sin(\omega t + \varphi(h))$ with learnable frequencies and state-dependent phase, and (2) a self-attend module that applies recurrent self-attention to the hidden state. Through a controlled ablation study on sequential MNIST (sMNIST) with five random seeds, we evaluate gap robustness -- the ability to maintain performance when portions of the input sequence are removed at test time. Our key finding is that structured oscillatory dynamics significantly improve robustness to input interruptions: the self-attend variant achieves a statistically significant 2.78 percentage point multi-gap advantage over baseline ($p = 0.041$), while the pulse variant shows a 4.62 pp advantage with large effect size (Cohen's $d = 0.87$). A noise control (random perturbation of equal magnitude) provides no benefit, confirming that the advantage is structural rather than merely dynamic. These results provide evidence that continuous-time models can benefit from biologically-inspired internal oscillatory mechanisms for temporal robustness.

</details>

---

### 8. [Infinite Self-Attention](https://arxiv.org/abs/2603.00175)

**基本信息**

- 🔗 arXiv: [`2603.00175`](https://arxiv.org/abs/2603.00175)
- 👥 作者: Giorgio Roffo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00175.pdf)

**💡 相关性分析**

满足标准1：论文提出的无限自注意力机制是对核心神经网络架构（注意力机制）的根本性改进，这是构建任何领域大模型（包括化学大模型）的关键技术基础。

**📖 中文摘要**

本文提出了无限自注意力机制，这是一种将自注意力重新表述为谱方法的新架构，通过将注意力层视为内容自适应令牌图上的扩散步骤来处理。论文还提出了Linear-InfSA，一种线性时间变体，无需形成完整的注意力矩阵即可近似隐式注意力算子的主特征向量。该工作旨在解决Transformer在高分辨率视觉任务中的二次成本问题。虽然应用领域是视觉，但其核心创新——一种新的、更高效的注意力机制——是构建大规模模型（包括化学大模型）的基础组件。论文对注意力机制的根本性改进，为设计处理大规模分子图或长序列质谱数据的专用大模型提供了有价值的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The quadratic cost of softmax attention limits Transformer scalability in high-resolution vision. We introduce Infinite Self-Attention (InfSA), a spectral reformulation that treats each attention layer as a diffusion step on a content-adaptive token graph, accumulating multi-hop interactions through a discounted Neumann series over attention matrices. This links self-attention to classical graph centrality (Katz, PageRank, eigenvector centrality) for interpretable token weighting. We also show the Neumann kernel equals the fundamental matrix of an absorbing Markov chain, so a token's centrality is its expected number of random-walk visits before absorption. We then propose Linear-InfSA, a linear-time variant that approximates the principal eigenvector of the implicit attention operator without forming the full attention matrix. It keeps an auxiliary state of fixed size proportional to per-head dimension dh (independent of sequence length N), is drop-in compatible with Vision Transformers, and supports stable training at 4096 by 4096 and inference at 9216 by 9216 (about 332k tokens). In a 4-layer ViT (53.5M parameters, 59 GFLOPs at 224 by 224), Linear-InfSA reaches 84.7% top-1 on ImageNet-1K, a +3.2 point architectural gain over an equal-depth softmax ViT trained with the same recipe. On ImageNet-V2, InfViT variants outperform all compared baselines (up to 79.8% vs 76.8%), indicating robustness under distribution shift. On an A100 40GB GPU, Linear-InfViT runs at 231 images/s and 0.87 J/image (13x better throughput and energy than equal-depth ViT) and is the only tested model to complete 9216 by 9216 inference without out-of-memory. The linear approximation closely matches the dominant eigenvector of the quadratic operator (cosine 0.985).

</details>

---

### 9. [NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://arxiv.org/abs/2603.00180)

**基本信息**

- 🔗 arXiv: [`2603.00180`](https://arxiv.org/abs/2603.00180)
- 👥 作者: Jiwoo Kim, Swarajh Mehta, Hao-Lun Hsu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00180.pdf)

**💡 相关性分析**

满足标准1：论文探索了生成式AI在神经网络参数空间的应用（生成神经网络），这与化学信息学中利用生成模型探索化学空间（如分子生成）或生成分析模型的核心范式高度相关。

**📖 中文摘要**

本文介绍了神经网络扩散变换器，这是一种以宽度无关的方式生成神经网络参数的方法。该方法将权重矩阵标记化为补丁，并将其建模为局部结构化场。论文重点研究了MLP，其中排列对称性尤其明显，NNiT可以生成跨一系列架构的完全功能网络。这项工作涉及生成式AI在神经网络参数空间的应用。虽然其直接应用是机器人任务，但其“生成神经网络”的核心范式与探索化学空间（如生成分子结构）或生成用于质谱分析的模型参数有概念上的相似性，属于广义的“模型生成”范畴，与化学信息学中利用AI生成模型或数据的方法论相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative modeling of neural network parameters is often tied to architectures because standard parameter representations rely on known weight-matrix dimensions. Generation is further complicated by permutation symmetries that allow networks to model similar input-output functions while having widely different, unaligned parameterizations. In this work, we introduce Neural Network Diffusion Transformers (NNiTs), which generate weights in a width-agnostic manner by tokenizing weight matrices into patches and modeling them as locally structured fields. We establish that Graph HyperNetworks (GHNs) with a convolutional neural network (CNN) decoder structurally align the weight space, creating the local correlation necessary for patch-based processing. Focusing on MLPs, where permutation symmetry is especially apparent, NNiT generates fully functional networks across a range of architectures. Our approach jointly models discrete architecture tokens and continuous weight patches within a single sequence model. On ManiSkill3 robotics tasks, NNiT achieves >85% success on architecture topologies unseen during training, while baseline approaches fail to generalize.

</details>

---

### 10. [Task-Driven Subspace Decomposition for Knowledge Sharing and Isolation in LoRA-based Continual Learning](https://arxiv.org/abs/2603.00191)

**基本信息**

- 🔗 arXiv: [`2603.00191`](https://arxiv.org/abs/2603.00191)
- 👥 作者: Lingfeng He, De Cheng, Huaijie Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00191.pdf)

**💡 相关性分析**

满足标准1：论文专注于改进LoRA这一构建和适配大模型（包括化学大模型）的核心微调技术，特别是在持续学习场景下的应用，与维护和更新化学大模型的需求直接相关。

**📖 中文摘要**

本文研究了基于LoRA的持续学习中的知识共享与隔离问题，提出了低秩分解与适应方法。该方法通过解决两个基于能量的目标，执行任务驱动的分解，以构建通用和真正任务特定的LoRA子空间，从而解耦知识共享和隔离的方向。LoRA作为一种参数高效微调方法，是构建和适配大型模型（包括化学大模型）的关键技术。本文对LoRA在持续学习场景下的改进，直接关系到如何让一个化学大模型持续学习新的分子数据、谱图数据或反应规则而不遗忘旧知识，这对于开发实用、可更新的化学AI系统至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continual Learning (CL) requires models to sequentially adapt to new tasks without forgetting old knowledge. Recently, Low-Rank Adaptation (LoRA), a representative Parameter-Efficient Fine-Tuning (PEFT) method, has gained increasing attention in CL. Several LoRA-based CL methods reduce interference across tasks by separating their update spaces, typically building the new space from the estimated null space of past tasks. However, they (i) overlook task-shared directions, which suppresses knowledge transfer, and (ii) fail to capture truly effective task-specific directions since these ``null bases" of old tasks can remain nearly inactive for new task under correlated tasks. To address this, we study LoRA learning capability from a projection energy perspective, and propose Low-rank Decomposition and Adaptation (LoDA). It performs a task-driven decomposition to build general and truly task-specific LoRA subspaces by solving two energy-based objectives, decoupling directions for knowledge sharing and isolation. LoDA fixes LoRA down-projections on two subspaces and learns robust up-projections via a Gradient-Aligned Optimization (GAO) approach. After each task, before integrating the LoRA updates into the backbone, LoDA derives a closed-form recalibration for the general update, approximating a feature-level joint optimum along this task-shared direction. Experiments indicate that LoDA outperforms existing CL methods.

</details>

---

### 11. [CoPeP: Benchmarking Continual Pretraining for Protein Language Models](https://arxiv.org/abs/2603.00253)

**基本信息**

- 🔗 arXiv: [`2603.00253`](https://arxiv.org/abs/2603.00253)
- 👥 作者: Darshan Patil, Pranshu Malviya, Mathieu Reymond 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00253.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究蛋白质语言模型（一类化学大模型）的持续预训练问题（标准1），并提出了CoPeP基准数据集和评估协议（标准2）。

**📖 中文摘要**

本文介绍了CoPeP基准，这是一个用于评估蛋白质语言模型持续预训练的新基准。该基准策划了一个跨越十年的、源自UniProt知识库的蛋白质数据集序列，并定义了在31个蛋白质理解任务上评估pLM性能的指标。论文评估了持续学习文献中的几种方法，包括回放、遗忘和基于可塑性的方法。蛋白质语言模型是化学信息学和生物信息学交叉领域的大模型典范。本文的工作直接针对“化学大模型”（此处特指蛋白质语言模型）的持续学习这一关键问题，不仅提出了评估基准，还验证了多种持续学习策略的有效性，为化学大模型的长期维护和进化提供了重要的方法论参考和实证数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (pLMs) have recently gained significant attention for their ability to uncover relationships between sequence, structure, and function from evolutionary statistics, thereby accelerating therapeutic drug discovery. These models learn from large protein databases that are continuously updated by the biology community and whose dynamic nature motivates the application of continual learning, not only to keep up with the ever-growing data, but also as an opportunity to take advantage of the temporal meta-information that is created during this process. As a result, we introduce the Continual Pretraining of Protein Language Models (CoPeP) benchmark, a novel benchmark for evaluating continual learning approaches on pLMs. Specifically, we curate a sequence of protein datasets derived from the UniProt Knowledgebase spanning a decade and define metrics to assess pLM performance across 31 protein understanding tasks. We evaluate several methods from the continual learning literature, including replay, unlearning, and plasticity-based methods, some of which have never been applied to models and data of this scale. Our findings reveal that incorporating temporal meta-information improves perplexity by up to 7% even when compared to training on data from all tasks jointly. Moreover, even at scale, several continual learning methods outperform naive continual pretraining. The CoPeP benchmark offers an exciting opportunity to study these methods at scale in an impactful real-world application.

</details>

---

### 12. [Transformers Remember First, Forget Last: Dual-Process Interference in LLMs](https://arxiv.org/abs/2603.00270)

**基本信息**

- 🔗 arXiv: [`2603.00270`](https://arxiv.org/abs/2603.00270)
- 👥 作者: Sourav Chattaraj, Kanak Raj
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00270.pdf)

**💡 相关性分析**

满足标准1：论文深入研究了大语言模型的记忆与干扰机制，这对于理解并改进化学大模型在处理冲突化学信息、整合新旧知识等方面的核心推理能力具有重要理论价值。

**📖 中文摘要**

本文研究了大型语言模型在遇到上下文冲突信息时的记忆干扰模式，将认知心理学中的经典干扰范式应用于LLMs。研究发现，所有测试模型都表现出前摄干扰优于倒摄干扰的相同模式，这与人类记忆模式相反。论文进一步揭示了RI和PI反映了不同的记忆机制，并与模型规模等因素存在不同关联。这项研究从认知科学角度深入剖析了LLM的记忆机制。理解大模型的记忆与遗忘机制对于构建可靠的化学大模型至关重要，例如，模型如何整合新的实验数据与已有的化学知识，如何处理冲突或不确定的谱图解析结果。本文的发现为设计更稳健的化学知识推理和质谱数据解释模型提供了理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

When large language models encounter conflicting information in context, which memories survive -- early or recent? We adapt classical interference paradigms from cognitive psychology to answer this question, testing 39 LLMs across diverse architectures and scales. Every model shows the same pattern: proactive interference (PI) dominates retroactive interference (RI) universally (Cohen's d = 1.73, p < 0.0001), meaning early encodings are protected at the cost of recent information -- the opposite of human memory, where RI typically dominates. Three findings indicate that RI and PI reflect separate memory mechanisms. RI and PI are uncorrelated (R^2 = 0.044), rejecting a unified "memory capacity." Model size predicts RI resistance (R^2 = 0.49) but not PI (R^2 = 0.06, n.s.) -- only RI is capacity-dependent. And error analysis reveals distinct failure modes: RI failures are passive retrieval failures (51%), while PI failures show active primacy intrusion (56%); both show <1% hallucination. These patterns parallel the consolidation-retrieval distinction in cognitive science, suggesting that transformer attention creates a primacy bias with direct implications for interference-heavy applications.

</details>

---

### 13. [Polynomial Surrogate Training for Differentiable Ternary Logic Gate Networks](https://arxiv.org/abs/2603.00302)

**基本信息**

- 🔗 arXiv: [`2603.00302`](https://arxiv.org/abs/2603.00302)
- 👥 作者: Sai Sandeep Damera, Ryan Matheu, Aniruddh G. Puranic 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00302.pdf)

**💡 相关性分析**

满足标准1：论文提出的可微分三值逻辑网络框架，支持不确定性下的原则性弃权，这与质谱结构推理中处理模糊、不确定谱图匹配的需求在方法论上高度契合。

**📖 中文摘要**

本文提出了多项式代理训练方法，用于可微分三值逻辑门网络。该方法将每个三值神经元表示为一个具有9个可学习系数的多项式，实现了参数的大幅减少，并证明了训练网络与其离散化逻辑电路之间的差距是有界的。论文将DTLGNs扩展到三值Kleene逻辑，其中UNKNOWN状态支持在不确定性下的原则性弃权。这项工作在可微分逻辑电路领域进行了创新。虽然应用示例是图像分类，但其核心——构建可解释、可微分的符号推理模块——与化学信息学中构建结合符号推理与子结构感知的质谱解析模型，或创建具有明确不确定性估计的化学分类模型高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Differentiable logic gate networks (DLGNs) learn compact, interpretable Boolean circuits via gradient-based training, but all existing variants are restricted to the 16 two-input binary gates. Extending DLGNs to Ternary Kleene $K_3$ logic and training DTLGNs where the UNKNOWN state enables principled abstention under uncertainty is desirable. However, the support set of potential gates per neuron explodes to $19{,}683$, making the established softmax-over-gates training approach intractable. We introduce Polynomial Surrogate Training (PST), which represents each ternary neuron as a degree-$(2,2)$ polynomial with 9 learnable coefficients (a $2{,}187\times$ parameter reduction) and prove that the gap between the trained network and its discretized logic circuit is bounded by a data-independent commitment loss that vanishes at convergence. Scaling experiments from 48K to 512K neurons on CIFAR-10 demonstrate that this hardening gap contracts with overparameterization. Ternary networks train $2$-$3\times$ faster than binary DLGNs and discover true ternary gates that are functionally diverse. On synthetic and tabular tasks we find that the UNKNOWN output acts as a Bayes-optimal uncertainty proxy, enabling selective prediction in which ternary circuits surpass binary accuracy once low-confidence predictions are filtered. More broadly, PST establishes a general polynomial-surrogate methodology whose parameterization cost grows only quadratically with logic valence, opening the door to many-valued differentiable logic.

</details>

---

### 14. [When does Chain-of-Thought Help: A Markovian Perspective](https://arxiv.org/abs/2603.00306)

**基本信息**

- 🔗 arXiv: [`2603.00306`](https://arxiv.org/abs/2603.00306)
- 👥 作者: Zihan Wang, Yijun Dong, Qi Lei
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00306.pdf)

**💡 相关性分析**

满足标准1：论文对思维链推理机制的理论分析，直接关联到如何提升化学大模型在复杂推理任务（如多步合成规划、质谱解析）中的性能与可靠性。

**📖 中文摘要**

本文从马尔可夫链的视角分析了思维链提示何时以及为何有效。理论指出，过渡对齐（实例是否共享共同的逐步过渡核）是CoT有效性的关键决定因素。当各步骤间的过渡相同时，CoT降低了推理时的样本复杂度；而当过渡不同时，这些收益可能会消失。论文进一步量化了中间步骤中的噪声如何调节CoT的收益。这项研究为理解CoT的机制提供了理论框架。思维链是提升大模型（包括化学大模型）复杂推理能力（如多步反应预测、谱图解析推理）的关键技术。本文的理论分析有助于指导如何在化学领域更有效地设计和应用CoT，例如在质谱结构推理中构建合理的分解步骤。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chain-of-Thought (CoT) prompting is a widely used inference-time technique for improving reasoning, yet its gains are uneven across tasks. We analyze when and why CoT helps by modeling the step-wise reasoning trajectory as a Markov chain. Each intermediate step is a state and the dependence between steps is captured by a transition kernel. Our theory identifies transition alignment, whether instances share a common step-wise transition kernel, as the key determinant of CoT's effectiveness. When transitions are identical across steps, CoT reduces inference-time sample complexity: fewer context sample trajectories suffice to recover the final decision. In contrast, when transitions differ across steps, these gains can vanish. We further quantify how noise in intermediate steps modulates CoT's benefit. Beyond theory, we design synthetic benchmarks that isolate these factors to complement prior results on real-world tasks and to empirically validate our predictions.

</details>

---

### 15. [Monotropic Artificial Intelligence: Toward a Cognitive Taxonomy of Domain-Specialized Language Models](https://arxiv.org/abs/2603.00350)

**基本信息**

- 🔗 arXiv: [`2603.00350`](https://arxiv.org/abs/2603.00350)
- 👥 作者: Antonio de Sousa Leitão Filho, Allan Kardec Duailibe Barros Filho, Fabrício Saul Lima 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00350.pdf)

**💡 相关性分析**

满足标准1和3：论文提出了“单otropic AI”这一针对深度专业化模型的创新概念框架（标准1），并对其优势和应用进行了前瞻性讨论，可被视为一种重要的相关展望（标准3）。

**📖 中文摘要**

本文引入了“单otropic人工智能”的概念，即故意牺牲通用性以在严格限定的领域内实现非凡精确性的语言模型。借鉴用于理解自闭症认知的单otropic认知理论，作者认为强烈的专业化代表了一种具有独特优势的替代认知架构，尤其适用于安全关键型应用。论文通过Mini-Enedina模型（一个3750万参数、在Timoshenko梁分析上达到近乎完美性能，但在其领域外故意无能的模型）证明了其可行性。这一框架挑战了AGI是AI研究唯一合法目标的隐含假设。在化学信息学领域，针对质谱解析、分子性质预测等特定任务构建深度专业化、高精度、可解释且安全的“单otropic”模型，正是该领域的重要需求，本文为此提供了概念框架和实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The prevailing paradigm in artificial intelligence research equates progress with scale: larger models trained on broader datasets are presumed to yield superior capabilities. This assumption, while empirically productive for general-purpose applications, obscures a fundamental epistemological tension between breadth and depth of knowledge. We introduce the concept of \emph{Monotropic Artificial Intelligence} -- language models that deliberately sacrifice generality to achieve extraordinary precision within narrowly circumscribed domains. Drawing on the cognitive theory of monotropism developed to understand autistic cognition, we argue that intense specialization represents not a limitation but an alternative cognitive architecture with distinct advantages for safety-critical applications. We formalize the defining characteristics of monotropic models, contrast them with conventional polytropic architectures, and demonstrate their viability through Mini-Enedina, a 37.5-million-parameter model that achieves near-perfect performance on Timoshenko beam analysis while remaining deliberately incompetent outside its domain. Our framework challenges the implicit assumption that artificial general intelligence constitutes the sole legitimate aspiration of AI research, proposing instead a cognitive ecology in which specialized and generalist systems coexist complementarily.

</details>

---

### 16. [StethoLM: Audio Language Model for Cardiopulmonary Analysis Across Clinical Tasks](https://arxiv.org/abs/2603.00355)

**基本信息**

- 🔗 arXiv: [`2603.00355`](https://arxiv.org/abs/2603.00355)
- 👥 作者: Yishan Wang, Tsai-Ning Wang, Mathias Funk 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00355.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个专门处理领域特定音频信号、并支持复杂指令任务的多模态大模型StethoLM。其技术架构和目标任务（分类、检测、推理等）与构建用于质谱分析的多模态化学大模型（质谱作为输入模态）在核心方法上直接相关。

**📖 中文摘要**

本文提出了StethoLM，首个专用于心肺听诊的音频-语言模型，能够执行涵盖听诊分析全谱的指令驱动临床任务。StethoLM集成了音频编码和医学语言模型主干，并在StethoBench基准上进行了训练。该工作建立了临床听诊中指令跟随AI系统的基础。虽然应用领域是医学音频，但其核心技术路线——构建一个能够理解和处理特定领域（化学/质谱）音频/信号数据，并遵循自然语言指令执行复杂分析任务的多模态大模型——与化学信息学中构建“质谱-语言”大模型的目标高度一致。StethoLM为如何将领域知识（心肺声音）与通用语言模型结合，以完成分类、检测、报告、推理、鉴别诊断等复杂任务提供了可借鉴的蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Listening to heart and lung sounds - auscultation - is one of the first and most fundamental steps in a clinical examination. Despite being fast and non-invasive, it demands years of experience to interpret subtle audio cues. Recent deep learning methods have made progress in automating cardiopulmonary sound analysis, yet most are restricted to simple classification and offer little clinical interpretability or decision support. We present StethoLM, the first audio-language model specialized for cardiopulmonary auscultation, capable of performing instruction-driven clinical tasks across the full spectrum of auscultation analysis. StethoLM integrates audio encoding with a medical language model backbone and is trained on StethoBench, a comprehensive benchmark comprising 77,027 instruction-response pairs synthesized from 16,125 labeled cardiopulmonary recordings spanning seven clinical task categories: binary classification, detection, reporting, reasoning, differential diagnosis, comparison, and location-based analysis. Through multi-stage training that combines supervised fine-tuning and direct preference optimization, StethoLM achieves substantial gains in performance and robustness on out-of-distribution data. Our work establishes a foundation for instruction-following AI systems in clinical auscultation.

</details>

---

### 17. [Distribution-Aware Companding Quantization of Large Language Models](https://arxiv.org/abs/2603.00364)

**基本信息**

- 🔗 arXiv: [`2603.00364`](https://arxiv.org/abs/2603.00364)
- 👥 作者: Athul Radhakrishnan, Siddhant Mohan, Mahima Sachdeva
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00364.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（改进大型语言模型的训练目标以增强其推理和泛化能力）直接围绕“化学大模型”这一主题。化学大模型作为特定领域的大模型，其训练和优化面临类似的挑战（如数据效率、泛化能力），本文提出的方法具有直接的借鉴意义。

**📖 中文摘要**

这篇论文探讨了大型语言模型（如GPT和Llama）的训练方法，提出通过预测多个未来标记（multi-token prediction）而非仅预测下一个标记，可以提高样本效率并增强模型的推理能力。虽然论文主要关注语言模型的通用训练，但其核心主题——通过改进训练目标来增强大模型的推理和泛化能力——与“化学大模型”的研究高度相关。化学大模型同样需要从海量数据中学习复杂的结构-性质关系，并具备强大的推理能力（如逆合成分析、性质预测）。本文提出的多标记预测方法为提高大模型的样本效率和推理能力提供了一种通用策略，其思想可直接迁移至化学大模型领域，用于提升模型在化学任务（如分子生成、反应预测）上的表现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models such as GPT and Llama are trained with a next-token prediction loss. In this work, we suggest that training language models to predict multiple future tokens at once results in higher sample efficiency. More specifically, at each position in the training corpus, we ask the model to predict the following n tokens using n independent output heads, operating on top of a shared model trunk. Considering multi-token prediction as an auxiliary training task, we measure improved downstream capabilities with no overhead in training time for both code and natural language models. The method is increasingly useful for larger model sizes and keeps its appeal when training for multiple epochs. Gains are especially pronounced on generative benchmarks like coding, where our models consistently outperform strong baselines by several percentage points. Our 13B parameter models solves 12 % more problems on HumanEval and 17 % more on MBPP than comparable next-token models. Experiments on small algorithmic tasks demonstrate that multi-token prediction is favorable for the development of induction heads and algorithmic reasoning capabilities. As an additional benefit, models trained with 4-token prediction are up to 3X times faster at inference, even with large batch sizes.

</details>

---

### 18. [OBASE: Object-Based Address-Space Engineering to Improve Memory Tiering](https://arxiv.org/abs/2603.00378)

**基本信息**

- 🔗 arXiv: [`2603.00378`](https://arxiv.org/abs/2603.00378)
- 👥 作者: Vinay Banakar, Suli Yang, Kan Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00378.pdf)

**💡 相关性分析**

满足标准2：论文提出的OBASE系统及其背后的地址空间工程方法，为处理大规模、复杂数据（如化学大模型训练数据、质谱数据集）提供了底层系统优化和资源管理的新思路。这可以被视为一种可用于提升相关主题计算效率的“工具”或“方法学资源”。

**📖 中文摘要**

论文提出了OBASE，一个用于非托管语言的编译器-运行时系统，旨在通过地址空间工程（动态重组虚拟内存）来改善内存分层性能。虽然其应用背景是通用计算，但论文中深入分析了Google生产工作负载中内存访问模式的热点碎片化问题，并提出了基于对象访问跟踪和迁移的解决方案。这项工作在方法论层面与“化学大模型”和“质谱结构推理”相关。首先，化学大模型（尤其是处理3D分子结构或大规模计算化学模拟的模型）通常是内存和计算密集型的，高效的内存管理对于其训练和推理至关重要。其次，质谱结构推理任务中，处理高维质谱数据并从中推断复杂分子结构，同样需要高效的数据组织和访问模式。OBASE所代表的“基于数据/对象访问模式进行系统优化”的思想，为构建高性能、可扩展的化学信息学计算平台和工具提供了有价值的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hardware and OS mechanisms for memory tiering are widely deployed, yet datacenters still overprovision DRAM. The root cause is hotness fragmentation: allocators place objects by size rather than access pattern, so hot and cold objects become interleaved within the same pages. A single hot object marks its page as active, trapping surrounding cold data in expensive DRAM. Our analysis of Google production workloads shows that up to 97% of the bytes in active pages are cold and unreclaimable. We propose address-space engineering: dynamically reorganizing virtual memory so that hot objects cluster into uniformly hot pages and cold objects into uniformly cold pages. We present OBASE, a compiler-runtime system for unmanaged languages that serves as an object-aware frontend for page-aware OS backends. OBASE tracks accesses via lightweight pointer instrumentation and migrates objects at runtime using a lock-free protocol that is safe under concurrency. By reorganizing the address space, OBASE enables unmodified backends (kswapd, TMO, TPP, Memtis) to tier memory effectively. Across ten concurrent data structures, six backends, and production traces from Meta and Twitter, OBASE improves page utilization by 2-4x and reduces memory footprint by up to 70%, with only 2-5% overhead.

</details>

---

### 19. [A Data-Driven Analysis for Engineering Conferences: The Institute of Industrial and Systems Engineering (IISE) Annual Conference Proceedings (2002-2005)](https://arxiv.org/abs/2603.00399)

**基本信息**

- 🔗 arXiv: [`2603.00399`](https://arxiv.org/abs/2603.00399)
- 👥 作者: H. Sinan Bank, Casey E. Eaton
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00399.pdf)

**💡 相关性分析**

满足标准2和3：论文提供了一套基于LLM和数据驱动的方法论框架（标准2），可用于系统性地分析任何科学领域（包括化学信息学和质谱分析）的文献，从而生成该领域的综述和展望（标准3）。其方法本身即是一种有价值的“资源”或“工具”。

**📖 中文摘要**

这篇论文对工业与系统工程（ISE）会议论文集（2002-2025）进行了数据驱动的分析，旨在绘制该领域的知识图谱。研究利用大型语言模型（LLMs）进行领域感知分类，结合自然语言处理和网络科学，系统地映射了主题演变、识别了有影响力的论文和作者，并分析了合作网络。虽然其应用领域是ISE，但论文的核心贡献在于提出并演示了一套利用LLMs和计算分析方法对大规模学术文献进行“制图学”分析的完整框架。这套框架（包括数据收集、LLM驱动的分类、网络分析、结果可视化）完全可以被迁移应用于分析“化学信息学”和“质谱分析”领域的研究演进、识别核心主题、关键资源和工具、以及合作网络。这为相关领域的研究者提供了构建领域知识图谱、进行文献综述和展望的重要方法论工具和潜在数据集构建思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Charting the intellectual evolution of a scientific discipline is crucial for identifying its core contributions, challenges, and future directions. The IISE Annual Conference proceedings offer a rich longitudinal archive of the Industrial and Systems Engineering (ISE) community's development, but the sheer volume of scholarship produced over two decades makes a holistic analysis difficult. Traditional reviews often fail to capture the full scale of thematic shifts and complex collaboration networks that define the community's growth. This paper presents a computational analysis of IISE proceedings from 2002 to 2025, drawing on an initial dataset of 9,350 titles from ProQuest for thematic analysis and 8,958 titles from Google Scholar for citation analysis, to deliver a cartography of the ISE field's intellectual history. Leveraging Large Language Models (LLMs) for domain-aware classification, Natural Language Processing, and Network Science, our study systematically maps thematic evolution to identify dominant, emerging, and receding research topics. We analyze citation data and co-authorship networks to uncover influential papers and authors, providing critical insights into knowledge diffusion and community structure. Through this comprehensive analysis, we establish a baseline for understanding the trajectory of ISE research and offer valuable insights for researchers, practitioners, and educators. The findings illuminate the field's intellectual assets and provide a data-informed map to guide the future of ISE. To foster reproducibility and further research, the curated dataset used in this study and the results will be made publicly available.

</details>

---

### 20. [PointAlign: Feature-Level Alignment Regularization for 3D Vision-Language Models](https://arxiv.org/abs/2603.00412)

**基本信息**

- 🔗 arXiv: [`2603.00412`](https://arxiv.org/abs/2603.00412)
- 👥 作者: Yuanhao Su, Shaofeng Zhang, Xiaosong Jia 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00412.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（在跨模态大模型中通过特征对齐防止几何信息退化）直接围绕“结构推理”这一核心问题。其方法论为解决“质谱结构推理”这一特定领域的跨模态结构推断问题提供了直接相关的技术思路和潜在解决方案。

**📖 中文摘要**

论文提出了PointAlign，一种用于3D视觉-语言模型（3D VLMs）的特征级对齐正则化方法。该方法旨在解决3D-文本配对数据稀缺导致模型几何信息退化的问题，通过约束LLM中的中间点云令牌与视觉输入令牌对齐，以保留细粒度的3D几何语义信息。虽然论文聚焦于3D视觉-语言任务（如3D物体分类和描述），但其核心技术创新——在跨模态模型中通过特征对齐来防止模态信息（尤其是几何结构信息）在推理过程中的退化——与“质谱结构推理”任务高度相关。质谱结构推理的本质是从一维质谱信号中推断出复杂的三维分子结构，这是一个极具挑战性的跨模态推理问题。PointAlign所提出的“在生成过程中显式监督中间表示以保持输入模态的细粒度信息”这一思想，为解决质谱到结构映射中的信息损失和模糊性问题提供了新颖的技术视角。该方法可以启发质谱分析领域设计更强大的、能够保持质谱特征细节的分子结构生成模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of 3D Vision-Language Models (VLMs), crucial for applications in robotics, autonomous driving, and augmented reality, is severely constrained by the scarcity of paired 3D-text data. Existing methods rely solely on next-token prediction loss, using only language tokens for supervision. This results in inefficient utilization of limited 3D data and leads to a significant degradation and loss of valuable geometric information in intermediate representations. To address these limitations, we propose {\mname}, a novel feature-level alignment regularization method. {\mname} explicitly supervises intermediate point cloud tokens to preserve fine-grained 3D geometric-semantic information throughout the language modeling process. Specifically, we constrain the intermediate point cloud tokens within the LLM to align with visual input tokens via a consistency loss. By training only a lightweight alignment projector and LoRA adapters, {\mname} achieves explicit feature-level supervision with minimal computational overhead, effectively preventing geometric degradation. Extensive experiments on ModelNet40 and Objaverse datasets demonstrate that our method achieves \textbf{2.08} pp improvement on average for classification tasks, with a substantial \textbf{7.50} pp gain on the challenging open-vocabulary Objaverse classification task and \textbf{4.88} pp improvement on 3D object captioning evaluated by Qwen2-72B-Instruct, validating the effectiveness of {\mname}. Code is publicly available at \href{ this https URL }{ this https URL }.

</details>

---

### 21. [Rooted Absorbed Prefix Trajectory Balance with Submodular Replay for GFlowNet Training](https://arxiv.org/abs/2603.00454)

**基本信息**

- 🔗 arXiv: [`2603.00454`](https://arxiv.org/abs/2603.00454)
- 👥 作者: Xi Wang, Wenbo Lu, Shengjie Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00454.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（改进GFlowNets以生成多样化的结构化数据）直接围绕“化学大模型”中的一个核心子主题——分子生成与设计。GFlowNets是构建化学生成大模型的重要技术组件之一，本文的优化工作对该领域有直接贡献。

**📖 中文摘要**

论文提出了RapTB（Rooted absorbed prefix Trajectory Balance）和SubM（submodular replay）策略，用于改进生成流网络（GFlowNets）的训练，以缓解模式崩溃（如前缀崩溃和长度偏差）问题。GFlowNets是一种用于学习生成复杂结构化数据（如分子、图）概率分布的新型生成模型，在分子发现和设计等领域显示出巨大潜力。本文针对GFlowNets训练中的核心挑战，提出了通过锚定子轨迹监督和基于子模函数的经验回放策略来优化信用分配和促进多样性。这项工作直接面向“化学大模型”中的一个关键应用场景——基于生成模型的分子设计与发现。论文提出的方法旨在提升生成模型在探索复杂组合空间（如化学空间）时的效率和多样性，这对于训练能够生成新颖、有效分子的化学大模型至关重要。因此，该研究为化学大模型中的生成建模部分提供了前沿的算法改进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative Flow Networks (GFlowNets) enable fine-tuning large language models to approximate reward-proportional posteriors, but they remain prone to mode collapse, manifesting as prefix collapse and length bias. We attribute this to two factors: (i) weak credit assignment to early prefixes, and (ii) biased replay that induces a shifted, non-representative training flow distribution. We propose Rooted absorbed prefix Trajectory Balance RapTB, an objective that anchors subtrajectory supervision at the root and propagates terminal rewards to intermediate prefixes via absorbed suffix-based backups, providing dense prefix-level learning signals. To mitigate replay-induced distribution shift, we further introduce SubM, a submodular replay refresh strategy that promotes both high reward and diversity. Empirically, on tasks such as molecule generation with LLM using SMILES strings, RapTB combined with SubM consistently improves optimization performance and molecular diversity while preserving high validity.

</details>

---

### 22. [Benchmarking Few-shot Transferability of Pre-trained Models with Improved Evaluation Protocols](https://arxiv.org/abs/2603.00478)

**基本信息**

- 🔗 arXiv: [`2603.00478`](https://arxiv.org/abs/2603.00478)
- 👥 作者: Xu Luo, Ji Zhang, Lianli Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00478.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了一个用于评估模型少样本迁移能力的基准测试和评估协议（FEWTRANS和HPE），这为“化学大模型”领域评估模型的可迁移性提供了重要的“数据集”和“工具”（标准2）。同时，论文通过系统性实验得出的结论（如预训练模型质量的重要性、全参数微调的有效性）对化学大模型的研究具有重要的“综述和展望”价值，指明了该领域模型评估和选择的关键因素（标准3）。

**📖 中文摘要**

论文提出了FEWTRANS基准测试和改进的评估协议（超参数集成，HPE），旨在统一、严格地评估预训练模型在少样本迁移学习中的可迁移性。研究通过大量实验发现，预训练模型本身的选择是性能的主导因素，而许多复杂的迁移方法相比简单的全参数微调优势有限。论文还对多模态模型在专业领域（因语言稀有性）的性能崩溃进行了量化分析。这项工作与“化学大模型”高度相关，因为化学领域通常面临标注数据稀缺的问题，少样本迁移能力是化学大模型实用化的关键。FEWTRANS基准和HPE协议为评估化学领域预训练基础模型（如预训练在大量未标注分子数据上的模型）在下游少样本任务（如毒性预测、反应产率预测）上的表现提供了严谨的评估框架和方法论。论文的结论（模型本身质量重于迁移技巧）也对化学大模型的研究方向（应更注重预训练数据的质量和规模、模型架构的通用能力）具有重要指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Few-shot transfer has been revolutionized by stronger pre-trained models and improved adaptation this http URL , there lacks a unified, rigorous evaluation protocol that is both challenging and realistic for real-world usage. In this work, we establish FEWTRANS, a comprehensive benchmark containing 10 diverse datasets, and propose the Hyperparameter Ensemble (HPE) protocol to overcome the "validation set illusion" in data-scarce regimes. Our empirical findings demonstrate that the choice of pre-trained model is the dominant factor for performance, while many sophisticated transfer methods offer negligible practical advantages over a simple full-parameter fine-tuning baseline. To explain this surprising effectiveness, we provide an in-depth mechanistic analysis showing that full fine-tuning succeeds via distributed micro-adjustments and more flexible reshaping of high-level semantic presentations without suffering from overfitting. Additionally, we quantify the performance collapse of multimodal models in specialized domains as a result of linguistic rarity using adjusted Zipf frequency scores. By releasing FEWTRANS, we aim to provide a rigorous "ruler" to streamline reproducible advances in few-shot transfer learning research. We make the FEWTRANS benchmark publicly available at this https URL .

</details>

---

### 23. [A Polynomial-Time Axiomatic Alternative to SHAP for Feature Attribution](https://arxiv.org/abs/2603.00496)

**基本信息**

- 🔗 arXiv: [`2603.00496`](https://arxiv.org/abs/2603.00496)
- 👥 作者: Kazuhiro Hiraki, Shinichi Ishihara, Takumi Kongo 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00496.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的特征归因算法（ESENSC_rev2），该算法具有理论保证和计算效率。这为“化学大模型”和“质谱结构推理”模型的可解释性分析提供了可直接应用的“工具”或“方法”。

**📖 中文摘要**

论文提出了一种基于合作博弈论的多项式时间可计算的特征归因方法（ESENSC_rev2），作为SHAP的理论基础扎实且计算高效的替代方案。特征归因是解释机器学习模型预测的关键技术，对于“化学大模型”和“质谱结构推理”模型的可解释性至关重要。例如，在化学大模型中，需要理解是分子的哪些子结构或原子对预测的性质负责；在质谱结构推理中，需要知道质谱中的哪些峰对推断出的特定分子碎片贡献最大。本文提出的方法在保证理论性质（如零玩家公理）的同时，大幅提升了高维特征归因的计算效率。这为化学信息学中复杂模型（如图神经网络、Transformer）的可解释性分析提供了新的、更高效的“工具”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we provide a theoretically grounded and computationally efficient alternative to SHAP. To this end, we study feature attribution through the lens of cooperative game theory by formulating a class of XAI--TU games. Building on this formulation, we investigate equal-surplus-type and proportional-allocation-type attribution rules and propose a low-cost attribution rule, ESENSC_rev2, constructed by combining two polynomial-time closed-form rules while ensuring the null-player property in the XAI--TU domain. Extensive experiments on tabular prediction tasks demonstrate that ESENSC_rev2 closely approximates exact SHAP while substantially improving scalability as the number of features increases. These empirical results indicate that equal-surplus-type attribution rules can achieve favorable trade-offs between computational cost and approximation accuracy in high-dimensional explainability settings. To provide theoretical foundations for these findings, we establish an axiomatic characterization showing that ESENSC_rev2 is uniquely determined by efficiency, the null-player axiom, a restricted differential marginality principle, an intermediate inessential-game property, and axioms that reduce computational requirements. Our results suggest that axiomatically justified and computationally efficient attribution rules can serve as practical and theoretically principled substitutes for SHAP-based approximations in modern explainability pipelines.

</details>

---

### 24. [What Do Visual Tokens Really Encode? Uncovering Sparsity and Redundancy in Multimodal Large Language Models](https://arxiv.org/abs/2603.00510)

**基本信息**

- 🔗 arXiv: [`2603.00510`](https://arxiv.org/abs/2603.00510)
- 👥 作者: Yingqi Fan, Junlong Tong, Anhao Zhao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00510.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容（分析大模型中输入令牌的语义稀疏性和计算冗余）直接围绕“大模型”的效率和表示学习这一通用主题（标准1）。其提出的分析框架（EmbedLens）和得出的结论为优化“化学大模型”的输入表示和内部计算提供了重要的方法论见解和潜在的优化“工具”（标准2）。

**📖 中文摘要**

论文对多模态大语言模型（MLLMs）中视觉令牌的内部编码和处理机制进行了细粒度分析。研究引入了一个名为EmbedLens的分析框架，揭示了视觉令牌在输入层面存在显著的语义稀疏性，并发现只有约60%的“活跃”令牌携带图像特定语义。进一步分析表明，这些活跃令牌在进入LLM之前就已经编码了丰富的细粒度视觉线索，而模型内部的视觉计算（如注意力）对于大多数标准任务是冗余的。这项工作虽然主要分析视觉-语言模型，但其揭示的“令牌稀疏性”和“计算冗余”现象对于构建高效的“化学大模型”具有深刻的启示。化学大模型（如分子Transformer）同样处理序列化或图结构化的输入（如SMILES字符串、分子图），其中也可能存在大量的信息冗余。本文的分析方法和结论可以启发化学信息学研究者去分析分子表示中的信息密度，设计更高效的令牌化策略、模型架构和训练方法，例如通过识别和剪枝“非活跃”的原子或子结构令牌来加速模型推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal large language models (MLLMs) project visual tokens into the embedding space of language models, yet the internal structuring and processing of visual semantics remain poorly understood. In this work, we introduce a two-fold analytical framework featuring a novel probing tool, $\textbf{EmbedLens}$, to conduct a fine-grained analysis. We uncover a pronounced semantic sparsity at the input level: visual tokens consistently partition into sink, dead, and alive categories. Remarkably, only the alive tokens, comprising $\approx60\%$ of the total input, carry image-specific meaning. Furthermore, using a targeted patch-compression benchmark, we demonstrate that these alive tokens already encode rich, fine-grained cues (e.g., objects, colors, and OCR) prior to entering the LLM. Internal visual computations (such as visual attention and feed-forward networks) are redundant for most standard tasks. For the small subset of highly vision-centric tasks that actually benefit from internal processing, we reveal that alive tokens naturally align with intermediate LLM layers rather than the initial embedding space, indicating that shallow-layer processing is unnecessary and that direct mid-layer injection is both sufficient. Ultimately, our findings provide a unified mechanistic view of visual token processing, paving the way for more efficient and interpretable MLLM architectures through selective token pruning, minimized visual computation, and mid-layer injection. The code is released at: this https URL .

</details>

---

### 25. [Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching](https://arxiv.org/abs/2603.00530)

**基本信息**

- 🔗 arXiv: [`2603.00530`](https://arxiv.org/abs/2603.00530)
- 👥 作者: Denis Blessing, Lorenz Richter, Julius Berner 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00530.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发一种新的、可扩展的采样方法（Bridge Matching Sampler），该方法在实验中明确应用于高维分子基准测试，与化学信息学中分子生成和性质预测等任务密切相关，属于化学大模型（用于生成或模拟分子）和质谱结构推理（涉及分子结构采样和概率建模）的基础技术范畴。

**📖 中文摘要**

本文提出了一种名为Bridge Matching Sampler (BMS)的新型采样方法，用于从未归一化的密度中进行采样。该方法通过将最小二乘“匹配”目标方法推广为基于Nelson关系的特殊形式的定点迭代，解决了现有方法在可扩展性、先验分布限制和优化稳定性方面的局限性。BMS能够学习任意先验分布和目标分布之间的随机传输映射，仅使用一个可扩展且稳定的目标。此外，作者还引入了一种阻尼变体，通过加入正则化项来缓解模式崩溃并进一步稳定训练。实验表明，该方法能够在复杂合成密度和高维分子基准测试中实现前所未有的规模采样，同时保持模式多样性，取得了最先进的结果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling from unnormalized densities using diffusion models has emerged as a powerful paradigm. However, while recent approaches that use least-squares `matching' objectives have improved scalability, they often necessitate significant trade-offs, such as restricting prior distributions or relying on unstable optimization schemes. By generalizing these methods as special forms of fixed-point iterations rooted in Nelson's relation, we develop a new method that addresses these limitations, called Bridge Matching Sampler (BMS). Our approach enables learning a stochastic transport map between arbitrary prior and target distributions with a single, scalable, and stable objective. Furthermore, we introduce a damped variant of this iteration that incorporates a regularization term to mitigate mode collapse and further stabilize training. Empirically, we demonstrate that our method enables sampling at unprecedented scales while preserving mode diversity, achieving state-of-the-art results on complex synthetic densities and high-dimensional molecular benchmarks.

</details>

---

### 26. [Enhancing Molecular Property Predictions by Learning from Bond Modelling and Interactions](https://arxiv.org/abs/2603.00568)

**基本信息**

- 🔗 arXiv: [`2603.00568`](https://arxiv.org/abs/2603.00568)
- 👥 作者: Yunqing Liu, Yi Zhou, Wenqi Fan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00568.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新颖的分子表示学习框架（DeMol），该框架通过显式建模化学键及其相互作用来提升分子性质预测的准确性。这直接属于化学信息学的核心研究领域，并且其改进的分子表示是构建化学大模型（用于理解和预测分子性质）以及辅助质谱结构推理（需要准确的分子结构表示）的关键基础。

**📖 中文摘要**

本文提出了DeMol，一个用于分子表示学习的双图框架。该框架的架构源于严格的信息论分析，证明了从键中心视角可以获得信息增益。DeMol通过并行的原子中心和键中心通道显式地对分子进行建模。这些通道通过多尺度双螺旋块进行协同融合，旨在学习复杂的原子-原子、原子-键和键-键相互作用。此外，框架的几何一致性通过基于共价半径的正则化项得到增强，以强制形成化学上合理的结构。在包括PCQM4Mv2、OC20 IS2RE、QM9和MoleculeNet在内的多样化基准测试上的综合评估表明，DeMol建立了新的最先进水平，优于现有方法。这些结果证实了显式建模键信息和相互作用的优越性，为更稳健和准确的分子机器学习铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecule representation learning is crucial for understanding and predicting molecular properties. However, conventional atom-centric models, which treat chemical bonds merely as pairwise interactions, often overlook complex bond-level phenomena like resonance and stereoselectivity. This oversight limits their predictive accuracy for nuanced chemical behaviors. To address this limitation, we introduce \textbf{DeMol}, a dual-graph framework whose architecture is motivated by a rigorous information-theoretic analysis demonstrating the information gain from a bond-centric perspective. DeMol explicitly models molecules through parallel atom-centric and bond-centric channels. These are synergistically fused by multi-scale Double-Helix Blocks designed to learn intricate atom-atom, atom-bond, and bond-bond interactions. The framework's geometric consistency is further enhanced by a regularization term based on covalent radii to enforce chemically plausible structures. Comprehensive evaluations on diverse benchmarks, including PCQM4Mv2, OC20 IS2RE, QM9, and MoleculeNet, show that DeMol establishes a new state-of-the-art, outperforming existing methods. These results confirm the superiority of explicitly modelling bond information and interactions, paving the way for more robust and accurate molecular machine learning.

</details>

---

### 27. [From Literature to Hypotheses: An AI Co-Scientist System for Biomarker-Guided Drug Combination Hypothesis Generation](https://arxiv.org/abs/2603.00612)

**基本信息**

- 🔗 arXiv: [`2603.00612`](https://arxiv.org/abs/2603.00612)
- 👥 作者: Raneen Younis, Suvinava Basak, Lukas Chavez 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00612.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发一个AI辅助系统（CoDHy），用于生成基于生物标志物的药物组合假设。这直接涉及化学信息学在药物发现中的应用。同时，该系统构建了整合多源生物医学数据的特定任务知识图谱，这本身就是一个可用于相关主题（如化学大模型训练或质谱生物标志物关联分析）的数据资源和工具，因此也满足标准2。

**📖 中文摘要**

本文介绍了AI Co-Scientist (CoDHy)，一个交互式、人在回路的系统，用于在癌症研究中生成基于生物标志物的药物组合假设。CoDHy将结构化的生物医学数据库和非结构化的文献证据整合到一个特定任务的知识图谱中，该图谱作为基于图的推理和假设构建的基础。该系统结合知识图谱嵌入和基于智能体的推理来生成、验证和排序候选药物组合，同时明确地将每个假设建立在可检索的证据之上。通过一个基于Web的界面，用户可以配置科学背景、检查中间结果并迭代地完善假设，从而实现透明且可由研究人员引导的探索，而非自动化决策。我们展示了CoDHy作为一个用于转化肿瘤学中探索性假设生成和决策支持的系统，突出了其设计、交互工作流程和实际用例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of biomedical literature and curated databases has made it increasingly difficult for researchers to systematically connect biomarker mechanisms to actionable drug combination hypotheses. We present AI Co-Scientist (CoDHy), an interactive, human-in-the-loop system for biomarker-guided drug combination hypothesis generation in cancer research. CoDHy integrates structured biomedical databases and unstructured literature evidence into a task-specific knowledge graph, which serves as the basis for graph-based reasoning and hypothesis construction. The system combines knowledge graph embeddings with agent-based reasoning to generate, validate, and rank candidate drug combinations, while explicitly grounding each hypothesis in retrievable evidence. Through a web-based interface, users can configure the scientific context, inspect intermediate results, and iteratively refine hypotheses, enabling transparent and researcher-steerable exploration rather than automated decision-making. We demonstrate CoDHy as a system for exploratory hypothesis generation and decision support in translational oncology, highlighting its design, interaction workflow, and practical use cases.

</details>

---

### 28. [SSKG Hub: An Expert-Guided Platform for LLM-Empowered Sustainability Standards Knowledge Graphs](https://arxiv.org/abs/2603.00669)

**基本信息**

- 🔗 arXiv: [`2603.00669`](https://arxiv.org/abs/2603.00669)
- 👥 作者: Chaoyue He, Xin Zhou, Xinjia Yu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00669.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是SSKG Hub平台及其构建知识图谱的流程。虽然其应用领域是可持续发展标准，但其核心技术——利用LLM从复杂文本（标准文档）中自动化提取结构化知识并构建可审计、可查询的知识图谱——为化学信息学和质谱分析领域提供了重要的方法论和工具参考。例如，该方法可用于从科学文献、质谱数据库或化学标准中自动化构建化学实体、反应或谱图关联的知识图谱，为化学大模型提供高质量的结构化数据资源。

**📖 中文摘要**

本文介绍了SSKG Hub（可持续发展标准知识图谱中心），一个研究原型和交互式Web平台，它通过一个以LLM为中心、专家引导的流程，将可持续发展披露标准（如GRI、SASB）转化为可审计的知识图谱。该系统集成了自动标准识别、可配置分块、标准特定提示、稳健的三元组解析以及具有细粒度审计元数据的、支持溯源感知的Neo4j存储。LLM提取产生一个溯源链接的草案KG，然后通过元专家裁决进行审查、策划并正式提升为认证KG。该平台支持跨KG融合、KG驱动任务以及用于洞察和精选资源的专用模块。我们通过一个全面的专家主导的KG审查案例研究来验证该平台，展示了端到端的策划和质量保证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sustainability disclosure standards (e.g., GRI, SASB, TCFD, IFRS S2) are comprehensive yet lengthy, terminology-dense, and highly cross-referential, hindering structured analysis and downstream use. We present SSKG Hub (Sustainability Standards Knowledge Graph Hub), a research prototype and interactive web platform that transforms standards into auditable knowledge graphs (KGs) through an LLM-centered, expert-guided pipeline. The system integrates automatic standard identification, configurable chunking, standard-specific prompting, robust triple parsing, and provenance-aware Neo4j storage with fine-grained audit metadata. LLM extraction produces a provenance-linked Draft KG, which is reviewed, curated, and formally promoted to a Certified KG through meta-expert adjudication. A role-based governance framework covering read-only guest access, expert review and CRUD operations, meta-expert certification, and administrative oversight ensures traceability and accountability across draft and certified states. Beyond graph exploration and triple-level evidence tracing, SSKG Hub supports cross-KG fusion, KG-driven tasks, and dedicated modules for insights and curated resources. We validate the platform through a comprehensive expert-led KG review case study that demonstrates end-to-end curation and quality assurance. The web application is publicly available at this http URL .

</details>

---

### 29. [Identifying and Characterising Response in Clinical Trials: Development and Validation of a Machine Learning Approach in Colorectal Cancer](https://arxiv.org/abs/2603.00757)

**基本信息**

- 🔗 arXiv: [`2603.00757`](https://arxiv.org/abs/2603.00757)
- 👥 作者: Adam Marcus, Paul Agapow
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00757.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种机器学习方法，用于从临床试验数据中识别对治疗有不同反应的患者亚组。这直接涉及从复杂的、高维的生物医学数据（包含基因型、表型等）中推理出有意义的“结构”（即预测疗效的生物标志物或患者特征模式），这与“化学信息学”中从数据推断复杂化学/生物系统结构（如构效关系）的核心任务高度相关。该方法可被视为一种用于“质谱结构推理”或更广义的“化学信息学结构推理”的通用数据分析框架。

**📖 中文摘要**

这篇论文提出了一种结合部分条件建模和虚拟双生子方法的机器学习方法，用于识别和表征临床试验中对治疗有不同反应的患者亚组。该方法特别适用于分析包含重复测量的纵向数据，能够估计时间特异性的治疗反应。研究在合成数据和真实的转移性结直肠癌临床试验数据上进行了验证，评估了帕尼单抗（panitumumab）的治疗效果。该方法能够处理动态治疗反应，并在固定反应场景下可能优于现有方法。在应用于结直肠癌试验时，该方法识别出基因突变、转移部位和种族是影响治疗反应的重要因素。这项工作展示了机器学习在精准医疗和药物反应预测中的应用，其核心是分析化学/生物分子（药物）与生物系统（患者）之间的复杂相互作用，并推断其潜在结构（生物标志物与疗效的关系）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Precision medicine promises to transform health care by offering individualised treatments that dramatically improve clinical outcomes. A necessary prerequisite is to identify subgroups of patients who respond differently to different therapies. Current approaches are limited to static measures of treatment success, neglecting the repeated measures found in most clinical trials. Our approach combines the concept of partly conditional modelling with treatment effect estimation based on the Virtual Twins method. The resulting time-specific responses to treatment are characterised using survLIME, an extension of Local Interpretable Model-agnostic Explanations (LIME) to survival data. Performance was evaluated using synthetic data and applied to clinical trials examining the effectiveness of panitumumab to treat metastatic colorectal cancer. An area under the receiver operating characteristic curve (AUC) of 0.77 for identifying fixed responders was achieved in a 1000 patient simulation. When considering dynamic responders, partly conditional modelling increased the AUC from 0.597 to 0.685. Applying the approach to colorectal cancer trials found genetic mutations, sites of metastasis, and ethnicity as important factors for response to treatment. Our approach can accommodate a dynamic response to treatment while potentially providing better performance than existing methods in instances of a fixed response to treatment. When applied to clinical data we attain results consistent with the literature.

</details>

---

### 30. [MultiPUFFIN: A Multimodal Domain-Constrained Foundation Model for Molecular Property Prediction of Small Molecules](https://arxiv.org/abs/2603.00857)

**基本信息**

- 🔗 arXiv: [`2603.00857`](https://arxiv.org/abs/2603.00857)
- 👥 作者: Idelfonso B. R. Nogueira, Carine M. Rebelloa, Mumin Enis Leblebici 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00857.pdf)

**💡 相关性分析**

满足标准1和标准2：1. 核心主题相关：论文直接围绕“化学大模型”主题，提出了一个名为MultiPUFFIN的多模态分子基础模型，用于小分子的多种物理化学性质预测。这完全符合化学信息学中利用AI大模型处理分子数据的核心研究方向。2. 数据资源相关：论文构建并使用了包含近4万分子、覆盖九种性质的多源数据集进行训练和评估，为相关领域提供了有价值的数据基准和模型框架。

**📖 中文摘要**

本文介绍了MultiPUFFIN，一个用于小分子多种物理化学性质预测的多模态、领域约束的基础模型。该模型解决了现有分子基础模型缺乏热力学一致性的问题，以及领域知识驱动方法仅限于单一性质和少量数据的问题。MultiPUFFIN的核心创新包括：(1) 一个通过门控跨模态注意力融合SMILES字符串、分子图和3D几何结构的编码器；(2) 将已建立的相关性方程（如Wagner、Andrade、van't Hoff和Shomate方程）作为归纳偏差嵌入预测头，以确保热力学一致性；(3) 两阶段多任务训练策略。模型在包含37,968个独特分子的多源数据集上训练，能够同时预测九种热物理性质。尽管参数仅约3500万，且训练分子数量远少于ChemBERTa-2等预训练模型，MultiPUFFIN在具有挑战性的支架分割测试集上取得了优异的性能，尤其在温度依赖性性质预测上优势明显。这项工作展示了多模态编码和领域知识引导能显著降低数据与计算需求，为分子性质预测提供了高效且物理一致的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting physicochemical properties across chemical space is vital for chemical engineering, drug discovery, and materials science. Current molecular foundation models lack thermodynamic consistency, while domain-informed approaches are limited to single properties and small datasets. We introduce MultiPUFFIN, a domain-constrained multimodal foundation model addressing both limitations simultaneously. MultiPUFFIN features: (i) an encoder fusing SMILES, graphs, and 3D geometries via gated cross-modal attention, alongside experimental condition and descriptor encoders; (ii) prediction heads embedding established correlations (e.g., Wagner, Andrade, van't Hoff, and Shomate equations) as inductive biases to ensure thermodynamic consistency; and (iii) a two-stage multi-task training this http URL prior frameworks, MultiPUFFIN predicts nine thermophysical properties simultaneously. It is trained on a multi-source dataset of 37,968 unique molecules (40,904 rows). With roughly 35 million parameters, MultiPUFFIN achieves a mean $R^2 = 0.716$ on a challenging scaffold-split test set of 8,877 molecules. Compared to ChemBERTa-2 (pre-trained on 77 million molecules), MultiPUFFIN outperforms the fine-tuned baseline across all nine properties despite using 2000x fewer training molecules. Advantages are strikingly apparent for temperature-dependent properties, where ChemBERTa-2 lacks the architectural capacity to incorporate thermodynamic this http URL results demonstrate that multimodal encoding and domain-informed biases substantially reduce data and compute requirements compared to brute-force pre-training. Furthermore, MultiPUFFIN handles missing modalities and recovers meaningful thermodynamic parameters without explicit supervision. Systematic ablation studies confirm the property-specific benefits of these domain-informed prediction heads.

</details>

---

### 31. [Alien Science: Sampling Coherent but Cognitively Unavailable Research Directions from Idea Atoms](https://arxiv.org/abs/2603.01092)

**基本信息**

- 🔗 arXiv: [`2603.01092`](https://arxiv.org/abs/2603.01092)
- 👥 作者: Alejandro H. Artiles, Martin Weiss, Levin Brinkmann 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01092.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型（LLM）及相关技术（如概念分解、聚类、建模）来生成新颖、非显而易见的研究方向。这直接围绕“化学大模型”这一广义主题，即利用AI大模型（特别是LLM）辅助或驱动科学研究与发现过程。

**📖 中文摘要**

本文提出了一种名为“Alien Science”的流程，旨在从大量研究论文中采样出“连贯但认知上不可用”的研究方向。该方法首先将论文分解为细粒度的概念单元，然后将其聚类为共享的“想法原子”词汇表。接着，它学习两个互补的模型：一个评估一组原子是否构成可行方向的“连贯性模型”，以及一个评估该方向被当前研究社区自然提出的可能性的“可用性模型”。最终，该方法采样出连贯性高但可用性低（即非显而易见）的“外星”研究方向。这项工作直接涉及使用大语言模型（LLM）进行科学发现和创意生成，属于“化学大模型”主题中利用AI模型进行科学研究的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models are adept at synthesizing and recombining familiar material, yet they often fail at a specific kind of creativity that matters most in research: producing ideas that are both coherent and non-obvious to the current community. We formalize this gap through cognitive availability, the likelihood that a research direction would be naturally proposed by a typical researcher given what they have worked on. We introduce a pipeline that (i) decomposes papers into granular conceptual units, (ii) clusters recurring units into a shared vocabulary of idea atoms, and (iii) learns two complementary models: a coherence model that scores whether a set of atoms constitutes a viable direction, and an availability model that scores how likely that direction is to be generated by researchers drawn from the community. We then sample "alien" directions that score high on coherence but low on availability. On a corpus of $\sim$7,500 recent LLM papers from NeurIPS, ICLR and ICML, we validate that (a) conceptual units preserve paper content under reconstruction, (b) idea atoms generalize across papers rather than memorizing paper-specific phrasing, and (c) the Alien sampler produces research directions that are more diverse than LLM baselines while maintaining coherence.

</details>

---

### 32. [Unified Vision-Language Modeling via Concept Space Alignment](https://arxiv.org/abs/2603.01096)

**基本信息**

- 🔗 arXiv: [`2603.01096`](https://arxiv.org/abs/2603.01096)
- 👥 作者: Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01096.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建和利用统一的视觉-语言大模型（V-SONAR, V-LCM）。这直接属于“化学大模型”主题的范畴，即构建和应用能够处理多模态（视觉和语言）信息的大型AI模型，尽管其应用领域不限于化学，但其模型架构和方法论具有通用性。

**📖 中文摘要**

本文介绍了V-SONAR，一个从纯文本嵌入空间SONAR扩展而来的视觉-语言嵌入空间。V-SONAR通过一个后处理对齐流程，将现有视觉编码器的表示映射到SONAR空间中。论文展示了V-SONAR在文本到视频检索和视频描述任务上的竞争力。更重要的是，论文利用V-SONAR，首次展示了仅用英语文本训练、在SONAR空间中运行的“大型概念模型”（LCM）能够以零样本方式执行单视觉和多视觉概念理解。最后，论文引入了V-LCM，通过视觉-语言指令微调扩展了LCM。V-LCM使用V-SONAR和SONAR将视觉和语言输入编码为统一的潜在嵌入序列，并使用与LCM文本预训练相同的潜在扩散目标进行训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce V-SONAR, a vision-language embedding space extended from the text-only embedding space SONAR (Omnilingual Embeddings Team et al., 2026), which supports 1500 text languages and 177 speech languages. To construct V-SONAR, we propose a post-hoc alignment pipeline that maps the representations of an existing vision encoder into the SONAR space. We thoroughly evaluate V-SONAR and show that its embeddings achieve competitive performance on text-to-video retrieval. Equipped with the OMNISONAR text decoder, V-SONAR further surpasses state-of-the-art vision-language models on video captioning tasks, including DREAM-1K (BLEU 23.9 vs. 19.6) and PE-VIDEO (BLEU 39.0 vs. 30.0). Leveraging V-SONAR, we first demonstrate that the Large Concept Model (LCM; LCM team et al. 2024) operating in SONAR and trained with English text only, can perform both single- and multi-visual concept understanding in a zero-shot manner. Finally, we introduce V-LCM, which extends the LCM with vision-language instruction tuning. V-LCM encodes vision and language inputs into an unified sequence of latent embeddings via V-SONAR and SONAR, and it is trained with the same latent diffusion objective for next-embedding prediction as in LCM's text-only pre-training. Experiments on a large-scale multilingual and -modal instruction-tuning data mixture highlight the potential of V-LCM: V-LCM matches state-of-the-art vision-language models on tasks covering image/video captioning and question answering, while significantly outperforming them across 61 rich- to low-resource languages out of all 62 tested languages.

</details>

---

### 33. [Understanding LoRA as Knowledge Memory: An Empirical Analysis](https://arxiv.org/abs/2603.01097)

**基本信息**

- 🔗 arXiv: [`2603.01097`](https://arxiv.org/abs/2603.01097)
- 👥 作者: Seungju Back, Dongwoo Lee, Naun Kang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01097.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）的参数化知识更新与记忆机制，特别是LoRA技术。这直接围绕“化学大模型”主题中关于大模型持续学习、知识更新和记忆架构的技术层面。

**📖 中文摘要**

本文对将低秩适应（LoRA）作为预训练大语言模型（LLM）的模块化知识记忆进行了首次系统的实证研究。研究探索了LoRA记忆的设计空间，包括表征存储容量、优化内部化过程、扩展多模块系统以及评估长上下文推理。论文旨在提供关于LoRA记忆操作边界的实用指导，并将其定位为与检索增强生成（RAG）和上下文学习（ICL）互补的记忆轴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continuous knowledge updating for pre-trained large language models (LLMs) is increasingly necessary yet remains challenging. Although inference-time methods like In-Context Learning (ICL) and Retrieval-Augmented Generation (RAG) are popular, they face constraints in context budgets, costs, and retrieval fragmentation. Departing from these context-dependent paradigms, this work investigates a parametric approach using Low-Rank Adaptation (LoRA) as a modular knowledge memory. Although few recent works examine this concept, the fundamental mechanics governing its capacity and composability remain largely unexplored. We bridge this gap through the first systematic empirical study mapping the design space of LoRA-based memory, ranging from characterizing storage capacity and optimizing internalization to scaling multi-module systems and evaluating long-context reasoning. Rather than proposing a single architecture, we provide practical guidance on the operational boundaries of LoRA memory. Overall, our findings position LoRA as the complementary axis of memory alongside RAG and ICL, offering distinct advantages.

</details>

---

### 34. [FCN-LLM: Empower LLM for Brain Functional Connectivity Network Understanding via Graph-level Multi-task Instruction Tuning](https://arxiv.org/abs/2603.01135)

**基本信息**

- 🔗 arXiv: [`2603.01135`](https://arxiv.org/abs/2603.01135)
- 👥 作者: Xingcan Hu, Wei Wang, Li Xiao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01135.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将特定领域（神经科学）的复杂数据（功能连接网络）与大语言模型（LLM）对齐和集成，属于构建和应用领域特定大模型（“化学大模型”的广义延伸）的范畴。其方法论（多模态对齐、指令微调）具有通用性。

**📖 中文摘要**

本文提出了FCN-LLM框架，使大语言模型（LLM）能够通过图级、多任务指令微调来理解从静息态fMRI衍生的大脑功能连接网络（FCN）。该方法采用多尺度FCN编码器捕获大脑区域、功能子网络和全脑特征，并将其投影到LLM的语义空间中。作者设计了涵盖19个受试者特定属性（人口统计学、表型、精神状况）的多范式指令任务，并采用多阶段学习策略。实验表明，FCN-LLM在大型多站点FCN数据库上实现了强大的零样本泛化能力，超越了传统的监督模型和基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models have achieved remarkable success in language understanding and reasoning, and their multimodal extensions enable comprehension of images, video, and audio. Inspired by this, foundation models for brain functional connectivity networks derived from resting-state fMRI have shown promise in clinical tasks. However, existing methods do not align FCNs with the text modality, limiting the ability of LLMs to directly understand FCNs. To address this, we propose FCN-LLM, a framework that enables LLMs to understand FCNs through graph-level, multi-task instruction tuning. Our approach employs a multi-scale FCN encoder capturing brain-region, functional subnetwork, and whole-brain features, projecting them into the semantic space of LLM. We design multi-paradigm instruction tasks covering 19 subject-specific attributes across demographics, phenotypes, and psychiatric conditions. A multi-stage learning strategy first aligns FCN embeddings with the LLM and then jointly fine-tunes the entire model to capture high-level semantic information. Experiments on a large-scale, multi-site FCN database show that FCN-LLM achieves strong zero-shot generalization on unseen datasets, outperforming conventional supervised and foundation models. This work introduces a new paradigm for integrating brain functional networks with LLMs, offering a flexible and interpretable framework for neuroscience.

</details>

---

### 35. [DeepResearch-9K: A Challenging Benchmark Dataset of Deep-Research Agent](https://arxiv.org/abs/2603.01152)

**基本信息**

- 🔗 arXiv: [`2603.01152`](https://arxiv.org/abs/2603.01152)
- 👥 作者: Tongzhou Wu, Yuhao Wang, Xinyu Ma 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01152.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门用于训练和评估深度研究智能体（可视为一种特定功能的大模型应用）的大规模基准数据集（DeepResearch-9K）和开源训练框架（DeepResearch-R1）。这些资源和工具可用于开发和评估与“化学大模型”主题相关的、具备复杂推理和网络探索能力的AI系统。

**📖 中文摘要**

本文构建了DeepResearch-9K，一个专门为深度研究场景设计的大规模、具有挑战性的基准数据集。该数据集包含9000个问题，涵盖从L1到L3三个难度级别，并提供了来自先进深度研究代理的高质量搜索轨迹（带推理链）和可验证的答案。此外，论文还开发了一个开源的训练框架DeepResearch-R1，支持多轮网络交互、不同的强化学习（RL）方法和不同的奖励模型。实证结果表明，在该数据集和框架下训练的智能体在具有挑战性的深度研究基准测试中达到了最先进的水平。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep-research agents are capable of executing multi-step web exploration, targeted retrieval, and sophisticated question answering. Despite their powerful capabilities, deep-research agents face two critical bottlenecks: (1) the lack of large-scale, challenging datasets with real-world difficulty, and (2) the absence of accessible, open-source frameworks for data synthesis and agent training. To bridge these gaps, we first construct DeepResearch-9K, a large-scale challenging dataset specifically designed for deep-research scenarios built from open-source multi-hop question-answering (QA) datasets via a low-cost autonomous pipeline. Notably, it consists of (1) 9000 questions spanning three difficulty levels from L1 to L3 (2) high-quality search trajectories with reasoning chains from Tongyi-DeepResearch-30B-A3B, a state-of-the-art deep-research agent, and (3) verifiable answers. Furthermore, we develop an open-source training framework DeepResearch-R1 that supports (1) multi-turn web interactions, (2) different reinforcement learning (RL) approaches, and (3) different reward models such as rule-based outcome reward and LLM-as-judge feedback. Finally, empirical results demonstrate that agents trained on DeepResearch-9K under our DeepResearch-R1 achieve state-of-the-art results on challenging deep-research benchmarks. We release the DeepResearch-9K dataset on this https URL and the code of DeepResearch-R1 on this https URL .

</details>

---

### 36. [Demystifying Group Relative Policy Optimization: Its Policy Gradient is a U-Statistic](https://arxiv.org/abs/2603.01162)

**基本信息**

- 🔗 arXiv: [`2603.01162`](https://arxiv.org/abs/2603.01162)
- 👥 作者: Hongyi Zhou, Kai Ye, Erhan Xu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01162.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对用于增强大语言模型（LLM）推理能力的强化学习算法（GRPO）进行理论分析。这直接围绕“化学大模型”主题中关于大模型训练、优化和性能提升（特别是数学/科学推理能力）的方法论基础。

**📖 中文摘要**

本文从理论角度分析了群体相对策略优化（GRPO），这是DeepSeekMath和DeepSeek-R1等模型用于扩展大语言模型推理能力的核心方法。论文证明GRPO策略梯度本质上是一个U-统计量，并据此描述了其均方误差、推导了其学习策略次优性间隙的有限样本误差界限和渐近分布。研究发现GRPO渐近等价于一个具有价值函数访问权限的Oracle策略梯度算法，并在广泛的策略梯度算法类中实现了渐近最优性能。此外，论文还建立了一个通用的缩放定律，为选择最佳群体大小提供了原则性指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Group relative policy optimization (GRPO), a core methodological component of DeepSeekMath and DeepSeek-R1, has emerged as a cornerstone for scaling reasoning capabilities of large language models. Despite its widespread adoption and the proliferation of follow-up works, the theoretical properties of GRPO remain less studied. This paper provides a unified framework to understand GRPO through the lens of classical U-statistics. We demonstrate that the GRPO policy gradient is inherently a U-statistic, allowing us to characterize its mean squared error (MSE), derive the finite-sample error bound and asymptotic distribution of the suboptimality gap for its learned policy. Our findings reveal that GRPO is asymptotically equivalent to an oracle policy gradient algorithm -- one with access to a value function that quantifies the goodness of its learning policy at each training iteration -- and achieves asymptotically optimal performance within a broad class of policy gradient algorithms. Furthermore, we establish a universal scaling law that offers principled guidance for selecting the optimal group size. Empirical experiments further validate our theoretical findings, demonstrating that the optimal group size is universal, and verify the oracle property of GRPO.

</details>

---

### 37. [DEP: A Decentralized Large Language Model Evaluation Protocol](https://arxiv.org/abs/2603.01167)

**基本信息**

- 🔗 arXiv: [`2603.01167`](https://arxiv.org/abs/2603.01167)
- 👥 作者: Jianxiang Peng, Junhao Li, Hongxiang Wang 等18人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01167.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于大语言模型（LLM）评估的标准化协议（DEP）和配套工具包（DEP Toolkit）。这为“化学大模型”主题中模型的性能评估、比较和基准测试提供了重要的方法论框架和工具资源，有助于该领域研究的规范化和可复现性。

**📖 中文摘要**

本文提出了去中心化评估协议（DEP），一个去中心化、统一且标准化的大语言模型（LLM）评估框架。DEP通过一个匹配服务器将用户、LLM和基准测试解耦，实现了模块化、即插即用的评估：基准测试文件和评估逻辑完全保留在服务器端。在远程设置中，用户无法访问真实答案，从而实现数据隔离和防泄漏评估。为了便于实际采用，论文开发了DEP Toolkit，一个支持断点续传、并发请求和拥塞控制等功能的协议兼容工具包。作者已适配了超过60个基准测试，并持续推动社区共建。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rapid development of Large Language Models (LLMs), a large number of benchmarks have been proposed. However, most benchmarks lack unified evaluation standard and require the manual implementation of custom scripts, making results hard to ensure consistency and reproducibility. Furthermore, mainstream evaluation frameworks are centralized, with datasets and answers, which increases the risk of benchmark leakage. To address these issues, we propose a Decentralized Evaluation Protocol (DEP), a decentralized yet unified and standardized evaluation framework through a matching server without constraining benchmarks. The server can be mounted locally or deployed remotely, and once adapted, it can be reused over the long term. By decoupling users, LLMs, and benchmarks, DEP enables modular, plug-and-play evaluation: benchmark files and evaluation logic stay exclusively on the server side. In remote setting, users cannot access the ground truth, thereby achieving data isolation and leak-proof evaluation. To facilitate practical adoption, we develop DEP Toolkit, a protocol-compatible toolkit that supports features such as breakpoint resume, concurrent requests, and congestion control. We also provide detailed documentation for adapting new benchmarks to DEP. Using DEP toolkit, we evaluate multiple LLMs across benchmarks. Experimental results verify the effectiveness of DEP and show that it reduces the cost of deploying benchmark evaluations. As of February 2026, we have adapted over 60 benchmarks and continue to promote community co-construction to support unified evaluation across various tasks and domains.

</details>

---

### 38. [Token-level Data Selection for Safe LLM Fine-tuning](https://arxiv.org/abs/2603.01185)

**基本信息**

- 🔗 arXiv: [`2603.01185`](https://arxiv.org/abs/2603.01185)
- 👥 作者: Yanping Li, Zhening Liu, Zijian Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01185.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）安全对齐和微调技术，特别是如何在保持模型效用的同时防止安全性退化。这直接属于“化学大模型”主题中关于大模型安全、可靠、可控应用的重要研究方向。

**📖 中文摘要**

本文针对大语言模型（LLM）在自定义数据集上微调可能导致安全性退化的问题，提出了一种名为TOSS的令牌级数据选择框架。该框架通过测量安全性退化模型和面向效用的模型之间的损失差异，来量化每个令牌的安全风险。这种令牌级粒度能够准确识别和移除不安全的令牌，同时保留有价值的任务特定信息。此外，论文还引入了渐进式细化策略TOSS-Pro，迭代地增强安全性退化模型识别不安全令牌的能力。实验表明，该方法在微调过程中能稳健地保护LLM，同时在下游任务上取得优异的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fine-tuning large language models (LLMs) on custom datasets has become a standard approach for adapting these models to specific domains and applications. However, recent studies have shown that such fine-tuning can lead to significant degradation in the model's safety. Existing defense methods operate at the sample level and often suffer from an unsatisfactory trade-off between safety and utility. To address this limitation, we perform a systematic token-level diagnosis of safety degradation during fine-tuning. Based on this, we propose token-level data selection for safe LLM fine-tuning (TOSS), a novel framework that quantifies the safety risk of each token by measuring the loss difference between a safety-degraded model and a utility-oriented model. This token-level granularity enables accurate identification and removal of unsafe tokens, thereby preserving valuable task-specific information. In addition, we introduce a progressive refinement strategy, TOSS-Pro, which iteratively enhances the safety-degraded model's ability to identify unsafe tokens. Extensive experiments demonstrate that our approach robustly safeguards LLMs during fine-tuning while achieving superior downstream task performance, significantly outperforming existing sample-level defense methods. Our code is available at this https URL .

</details>

---

### 39. [Reasoning or Rationalization? The Role of Justifications in Masked Diffusion Models for Fact Verification](https://arxiv.org/abs/2603.01190)

**基本信息**

- 🔗 arXiv: [`2603.01190`](https://arxiv.org/abs/2603.01190)
- 👥 作者: Jacob Devasier
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01190.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析一类新兴生成模型（掩码扩散语言模型）在需要进行理由生成的任务（如事实核查）中的内部推理机制。这涉及对大模型内部工作方式和可信度的理解，属于“化学大模型”主题中关于模型可解释性和可靠性研究的范畴。

**📖 中文摘要**

本文研究了掩码扩散语言模型（MDLM）在事实核查任务上的推理动态，检验了模型生成的“理由”是真正的推理还是事后合理化。研究发现，MDLM通常在扩散过程的早期就收敛于一个“裁决”，并将其作为全局锚点，在理由完成之前就已确定。强制实施“推理优先”约束（延迟裁决揭露）会主动降低性能，因为积累的理由令牌会引入不一致性，覆盖最初正确的预测。干预实验表明，模型在56%的情况下会对错误的强制裁决进行合理化，并且裁决强烈因果依赖于理由质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unlike autoregressive models, which generate tokens sequentially and benefit from reasoning-before-answering strategies such as Chain-of-Thought, Masked Diffusion Language Models (MDLMs) refine all sequence positions simultaneously, raising questions about how these models handle tasks requiring justified verdicts. In this work, we investigate the dynamics of MDLM reasoning on fact verification, examining whether justifications serve as genuine reasoning or post-hoc rationalization. We observe that MDLMs typically converge on a verdict early in the diffusion process, treating it as a global anchor that is resolved before the justification is complete. Crucially, enforcing a reasoning-first constraint via delayed verdict unmasking actively degrades performance, dropping accuracy from 86.2% to 71.9% as accumulating justification tokens introduce inconsistencies that override initially correct predictions. Interventional experiments reveal that the model rationalizes incorrect forced verdicts in 56% of cases, and that verdicts are strongly causally dependent on justification quality (57.3% accuracy with corrupted justifications vs. 97.1% with ground-truth). This causal dependence explains the degradation under forced deliberation: as the model generates noisy justification tokens, it conditions on them, gradually overriding its initially correct assessment. Our findings suggest that for fact verification with MDLMs, extended deliberation can be counterproductive, risking the dilution of accurate early predictions with noise introduced during justification generation.

</details>

---

### 40. [Subliminal Signals in Preference Labels](https://arxiv.org/abs/2603.01204)

**基本信息**

- 🔗 arXiv: [`2603.01204`](https://arxiv.org/abs/2603.01204)
- 👥 作者: Isotta Magistrali, Frédéric Berdoz, Sam Dauncey 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01204.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）对齐和评估框架中的潜在风险与机制（偏好标签作为隐蔽通信渠道）。这直接关系到“化学大模型”主题中关于如何安全、可靠地训练、评估和引导大模型（包括用于科学发现的模型）的核心挑战。

**📖 中文摘要**

本文挑战了在LLM-as-a-judge框架中，二元偏好标签仅提供关于响应质量的语义监督这一核心假设。论文证明，即使一个中立的学生模型生成语义无偏的补全，一个有偏见的评判者也可以通过偏好分配来传输非预期的行为特征，并且这种传输在迭代对齐轮次中甚至会加强。研究结果表明，在超级对齐设置中，稳健的监督需要能够检测和缓解潜意识偏好传输的机制，特别是当评判者可能追求非预期目标时。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As AI systems approach superhuman capabilities, scalable oversight increasingly relies on LLM-as-a-judge frameworks where models evaluate and guide each other's training. A core assumption is that binary preference labels provide only semantic supervision about response quality. We challenge this assumption by demonstrating that preference labels can function as a covert communication channel. We show that even when a neutral student model generates semantically unbiased completions, a biased judge can transmit unintended behavioral traits through preference assignments, which even strengthen across iterative alignment rounds. Our findings suggest that robust oversight in superalignment settings requires mechanisms that can detect and mitigate subliminal preference transmission, particularly when judges may pursue unintended objectives.

</details>

---

### 41. [Reasoning Boosts Opinion Alignment in LLMs](https://arxiv.org/abs/2603.01214)

**基本信息**

- 🔗 arXiv: [`2603.01214`](https://arxiv.org/abs/2603.01214)
- 👥 作者: Frédéric Berdoz, Yann Billeter, Yann Vonlanthen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01214.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用强化学习（RL）和结构化推理来对齐大语言模型（LLM）与特定人群或个人的意见偏好。这属于“化学大模型”主题中关于大模型个性化、可控生成以及与社会价值观对齐的研究方向。

**📖 中文摘要**

本文研究了推理是否能改善大语言模型（LLM）的意见对齐。受近期强化学习（RL）推动数学推理进步的启发，论文训练模型通过结构化推理生成与个人资料一致的答案。该方法在涵盖美国、欧洲和瑞士政治的三个数据集上进行了评估。结果表明，推理增强了意见建模能力，并与强基线具有竞争力，但并未完全消除偏见，凸显了使用LLM构建忠实政治数字孪生需要额外机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Opinion modeling aims to capture individual or group political preferences, enabling applications such as digital democracies, where models could help shape fairer and more popular policies. Given their versatility, strong generalization capabilities, and demonstrated success across diverse text-to-text applications, large language models (LLMs) are natural candidates for this task. However, due to their statistical nature and limited causal understanding, they tend to produce biased opinions when prompted naively. In this work, we study whether reasoning can improve opinion alignment. Motivated by the recent advancement in mathematical reasoning enabled by reinforcement learning (RL), we train models to produce profile-consistent answers through structured reasoning. We evaluate our approach on three datasets covering U.S., European, and Swiss politics. Results indicate that reasoning enhances opinion modeling and is competitive with strong baselines, but does not fully remove bias, highlighting the need for additional mechanisms to build faithful political digital twins using LLMs. By releasing both our method and datasets, we establish a solid baseline to support future research on LLM opinion alignment.

</details>

---

### 42. [Epistemic Gain, Aleatoric Cost: Uncertainty Decomposition in Multi-Agent Debate for Math Reasoning](https://arxiv.org/abs/2603.01221)

**基本信息**

- 🔗 arXiv: [`2603.01221`](https://arxiv.org/abs/2603.01221)
- 👥 作者: Dan Qiao, Binbin Chen, Fengyu Cai 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01221.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和改进用于增强大语言模型（LLM）推理能力的多智能体辩论（MAD）框架。这直接围绕“化学大模型”主题中关于通过多模型协作提升复杂问题（如科学推理）解决能力的技术路径。

**📖 中文摘要**

本文为多智能体辩论（MAD）提出了一个贝叶斯不确定性分析框架，将总预测不确定性分解为可通过辩论上下文减少的认知不确定性，以及由内部模型噪声引起的偶然不确定性。研究发现，有效的辩论关键在于在受控的偶然性成本下实现高认知增益。基于此见解，论文设计了一种不确定性引导的多智能体强化学习（MARL）算法，明确优化偶然性噪声减少和认知信息利用。实验表明，该训练显著提高了辩论后的准确性和稳定性，并增强了超越单智能体RL的个体推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-Agent Debate (MAD) has shown promise in leveraging collective intelligence to improve reasoning and reduce hallucinations, yet it remains unclear how information exchange shapes the underlying ability. Empirically, MAD exhibits paradoxical phenomena, such as accuracy improvement accompanied by substantial increase in token entropy, and remarkable divergence between homogeneous and heterogeneous model combinations. In this paper, we propose a Bayesian uncertainty analysis framework for MAD, which decomposes total predictive uncertainty into epistemic uncertainty reducible by debate context and aleatoric uncertainty induced by internal model noise. Across multiple model configurations, we find that effective debate hinges on achieving high epistemic gain under controlled aleatoric cost. Building on this insight, we design an uncertainty-guided multi-agent reinforcement learning (MARL) algorithm that explicitly optimizes aleatoric noise reduction and epistemic information utilization. Experiments show that our training significantly improves post-debate accuracy and stability, and enhances individual reasoning beyond single-agent RL, providing a unified Bayesian uncertainty perspective for understanding and improving MAD.

</details>

---

### 43. [Learn Hard Problems During RL with Reference Guided Fine-tuning](https://arxiv.org/abs/2603.01223)

**基本信息**

- 🔗 arXiv: [`2603.01223`](https://arxiv.org/abs/2603.01223)
- 👥 作者: Yangzhen Wu, Shanda Li, Zixin Wen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01223.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决大语言模型（LLM）在数学推理任务上进行强化学习（RL）时遇到的奖励稀疏挑战。这直接属于“化学大模型”主题中关于提升大模型复杂科学（数学）问题解决能力的关键训练技术。

**📖 中文摘要**

本文针对数学推理的强化学习（RL）中可能出现的奖励稀疏问题（对于难题，LLM无法采样任何正确轨迹），提出了参考引导微调（ReGFT）方法。该方法利用人工编写的参考解答（如AoPS问题附带的解答）来合成难题上的正轨迹，并在RL之前对其进行训练。对于每个问题，模型会获得部分参考解答，并生成自己的推理轨迹，确保生成的轨迹保持在模型的推理空间内，同时仍受益于参考指导。在三个基准测试上的实验表明，ReGFT持续提高了监督准确率，加速了DAPO训练，并提升了RL的最终性能平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement learning (RL) for mathematical reasoning can suffer from reward sparsity: for challenging problems, LLM fails to sample any correct trajectories, preventing RL from receiving meaningful positive feedback. At the same time, there often exist human-written reference solutions along with the problem (e.g., problems from AoPS), but directly fine-tuning on these solutions offers no benefit because models often cannot imitate human proofs that lie outside their own reasoning distribution. We introduce Reference-Guided Fine-Tuning (ReGFT), a simple and effective method that utilizes human-written reference solutions to synthesize positive trajectories on hard problems and train on them before RL. For each problem, we provide the model with a partial reference solution and let it generate its own reasoning trace, ensuring the resulting trajectories remain in the model's reasoning space while still benefiting from reference guidance. Fine-tuning on these reference-guided trajectories increases the number of solvable problems and produces a checkpoint that receives more positive rewards during RL. Across three benchmarks (AIME24, AIME25, BeyondAIME), ReGFT consistently improves supervised accuracy, accelerates DAPO training, and raises the final performance plateau of RL. Our results show that ReGFT effectively overcomes reward sparsity and unlocks stronger RL-based mathematical reasoning.

</details>

---

### 44. [Can Thinking Models Think to Detect Hateful Memes?](https://arxiv.org/abs/2603.01225)

**基本信息**

- 🔗 arXiv: [`2603.01225`](https://arxiv.org/abs/2603.01225)
- 👥 作者: Mohamed Bayan Kmainasi, Mucahid Kutlu, Ali Ezzat Shahroor 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01225.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用和优化基于“思维链”推理的多模态大语言模型（MLLM）来解决需要组合多模态推理的复杂任务（仇恨模因分析）。这直接涉及“化学大模型”主题中关于大模型（特别是多模态模型）的推理能力、训练方法（如GRPO）及其在复杂场景中的应用。

**📖 中文摘要**

本文研究了基于“思维链”推理的多模态大语言模型（MLLM）在仇恨模因分析中的应用。论文提出了一个基于强化学习的后训练框架，通过任务特定奖励和新颖的群体相对策略优化（GRPO）目标来改进MLLM的推理。具体工作包括：（i）对现成的MLLM进行仇恨模因理解的系统实证研究；（ii）通过蒸馏生成弱监督或伪监督的思维链理由，扩展现有的仇恨模因数据集；（iii）引入基于GRPO的目标，联合优化模因分类和解释质量，以鼓励细粒度、逐步推理。在Hateful Memes基准测试上的实验表明，该方法达到了最先进的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hateful memes often require compositional multimodal reasoning: the image and text may appear benign in isolation, yet their interaction conveys harmful intent. Although thinking-based multimodal large language models (MLLMs) have recently advanced vision-language understanding, their capabilities remain underexplored for hateful meme analysis. We propose a reinforcement learning based post-training framework that improves reasoning in thinking-based MLLMs through task-specific rewards and a novel Group Relative Policy Optimization (GRPO) objective. Specifically, we (i) conduct a systematic empirical study of off-the-shelf MLLMs for hateful meme understanding, (ii) extend an existing hateful meme dataset by generating weakly or pseudo-supervised chain-of-thought rationales via distillation, and (iii) introduce a GRPO-based objective that jointly optimizes meme classification and explanation quality to encourage fine-grained, step-by-step reasoning. Experiments on the Hateful Memes benchmark show that our approach achieves state-of-the-art performance, improving accuracy and F1 by approximately 1 percent and explanation quality by approximately 3 percent. We will publicly release our code, dataset extensions, and evaluation resources to support reproducibility.

</details>

---

### 45. [The Lattice Representation Hypothesis of Large Language Models](https://arxiv.org/abs/2603.01227)

**基本信息**

- 🔗 arXiv: [`2603.01227`](https://arxiv.org/abs/2603.01227)
- 👥 作者: Bo Xiong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01227.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从理论上阐释大语言模型（LLM）内部表示如何编码符号化的概念层次和逻辑结构（格表示假说）。这属于“化学大模型”主题中关于大模型内部知识表示、可解释性以及其与形式化符号系统关系的基础理论研究。

**📖 中文摘要**

本文提出了大语言模型的格表示假说：一个符号主干，将概念层次结构和逻辑操作建立在嵌入几何中。该框架将线性表示假说与形式概念分析（FCA）统一起来，表明具有分离阈值的线性属性方向通过半空间交集诱导出一个概念格。这种几何使得通过几何交（交集）和并（并集）操作进行符号推理成为可能，并且当属性方向线性独立时，允许一种规范形式。在WordNet子层次结构上的实验提供了实证证据，表明LLM嵌入编码了概念格及其逻辑结构，揭示了连续几何和符号抽象之间的原则性桥梁。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Lattice Representation Hypothesis of large language models: a symbolic backbone that grounds conceptual hierarchies and logical operations in embedding geometry. Our framework unifies the Linear Representation Hypothesis with Formal Concept Analysis (FCA), showing that linear attribute directions with separating thresholds induce a concept lattice via half-space intersections. This geometry enables symbolic reasoning through geometric meet (intersection) and join (union) operations, and admits a canonical form when attribute directions are linearly independent. Experiments on WordNet sub-hierarchies provide empirical evidence that LLM embeddings encode concept lattices and their logical structure, revealing a principled bridge between continuous geometry and symbolic abstraction.

</details>

---

### 46. [GlassMol: Interpretable Molecular Property Prediction with Concept Bottleneck Models](https://arxiv.org/abs/2603.01274)

**基本信息**

- 🔗 arXiv: [`2603.01274`](https://arxiv.org/abs/2603.01274)
- 👥 作者: Oscar Rivera, Ziqing Wang, Matthieu Dagommer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01274.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于分子性质预测的可解释机器学习模型（GlassMol），这直接属于“化学大模型”主题范畴，旨在提升化学领域AI模型的可解释性和可靠性。

**📖 中文摘要**

本文提出了GlassMol，一个用于分子性质预测的可解释概念瓶颈模型（CBM）。该模型旨在解决化学信息学中机器学习模型（如大语言模型和图神经网络）的黑箱问题。GlassMol通过将输入投影到人类可解释的概念（如分子描述符）来进行预测，确保解释忠实于决策过程。它解决了化学领域应用CBM的三个挑战：从大型描述符空间中选择任务相关概念（相关性差距）、获取分子数据的概念监督（标注差距）以及瓶颈约束导致的性能下降（容量差距）。论文在13个基准测试上进行了实验，表明GlassMol在保持或超越黑盒基线性能的同时提供了可解释性，挑战了可解释性必然牺牲性能的常见假设。这项工作直接与“化学大模型”主题相关，因为它专注于为化学领域（分子性质预测）开发更透明、可解释的机器学习模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning accelerates molecular property prediction, yet state-of-the-art Large Language Models and Graph Neural Networks operate as black boxes. In drug discovery, where safety is critical, this opacity risks masking false correlations and excluding human expertise. Existing interpretability methods suffer from the effectiveness-trustworthiness trade-off: explanations may fail to reflect a model's true reasoning, degrade performance, or lack domain grounding. Concept Bottleneck Models (CBMs) offer a solution by projecting inputs to human-interpretable concepts before readout, ensuring that explanations are inherently faithful to the decision process. However, adapting CBMs to chemistry faces three challenges: the Relevance Gap (selecting task-relevant concepts from a large descriptor space), the Annotation Gap (obtaining concept supervision for molecular data), and the Capacity Gap (degrading performance due to bottleneck constraints). We introduce GlassMol, a model-agnostic CBM that addresses these gaps through automated concept curation and LLM-guided concept selection. Experiments across thirteen benchmarks demonstrate that \method generally matches or exceeds black-box baselines, suggesting that interpretability does not sacrifice performance and challenging the commonly assumed trade-off. Code is available at this https URL .

</details>

---

### 47. [Catalyst-Agent: Autonomous heterogeneous catalyst screening and optimization with an LLM Agent](https://arxiv.org/abs/2603.01311)

**基本信息**

- 🔗 arXiv: [`2603.01311`](https://arxiv.org/abs/2603.01311)
- 👥 作者: Achuth Chandrasekhar, Janghoon Ock, Amir Barati Farimani
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01311.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个LLM驱动的AI代理（Catalyst-Agent），用于自动化催化剂发现和优化。这直接涉及“化学大模型”主题，即利用大型AI模型（LLM、GNN）解决化学领域的复杂问题（催化剂设计）。

**📖 中文摘要**

本文介绍了Catalyst-Agent，一个基于大语言模型（LLM）的自主AI代理，用于异质催化剂的筛选和优化。该代理利用OPTIMADE API探索材料数据库，进行结构修改，并通过Meta FAIRchem的UMA图神经网络（GNN）模型和AdsorbML工作流计算吸附能。它以闭环方式为研究人员提供有用的材料建议，包括表面级修改以优化候选材料。该代理在三个关键反应（氧还原反应ORR、氮还原反应NRR和CO2还原反应CO2RR）上进行了测试，成功率为23-34%，平均每个成功材料收敛需要1-2次试验。这项工作展示了AI代理利用其规划能力和工具使用来操作催化剂筛选工作流程、提供可测试假设并加速科学发现的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The discovery of novel catalysts tailored for particular applications is a major challenge for the twenty-first century. Traditional methods for this include time-consuming and expensive experimental trial-and-error approaches in labs based on chemical theory or heavily computational first-principles approaches based on density functional theory. Recent studies show that deep learning models like graph neural networks (GNNs) can significantly speed up the screening and discovery of catalyst materials by many orders of magnitude, with very high accuracy and fidelity. In this work, we introduce Catalyst-Agent, a Model Context Protocol (MCP) server-based, LLM-powered AI agent. It can explore vast material databases using the OPTIMADE API, make structural modifications, calculate adsorption energies using Meta FAIRchem's UMA (GNN) model via FAIRchem's AdsorbML workflow and slab construction, and make useful material suggestions to the researcher in a closed-loop manner, including surface-level modifications to refine near-miss candidates. It is tested on three pivotal reactions: the oxygen reduction reaction (ORR), the nitrogen reduction reaction (NRR), and the CO2 reduction reaction (CO2RR). Catalyst-Agent achieves a success rate of 23-34 percent among all the materials it chooses and evaluates, and manages to converge in 1-2 trials per successful material on average. This work demonstrates the potential of AI agents to exercise their planning capabilities and tool use to operationalize the catalyst screening workflow, provide useful, testable hypotheses, and accelerate future scientific discoveries for humanity with minimal human intervention.

</details>

---

### 48. [Causal Neural Probabilistic Circuits](https://arxiv.org/abs/2603.01372)

**基本信息**

- 🔗 arXiv: [`2603.01372`](https://arxiv.org/abs/2603.01372)
- 👥 作者: Weixin Chen, Han Zhao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01372.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种结合神经网络与因果概率图的新型模型架构（CNPC），用于提升可解释性和干预下的推理能力。这种在模型架构和推理方法上的创新，与构建更先进、可解释的“化学大模型”（用于分子性质预测、反应推理等）的研究方向在核心主题上相关。

**📖 中文摘要**

本文提出了因果神经概率电路（CNPC），它将神经属性预测器与从因果图编译的因果概率电路相结合。该模型旨在增强概念瓶颈模型（CBMs）的可解释性，特别是在干预场景下。CNPC支持精确、可处理的因果推理，尊重概念间的因果依赖关系。在干预下，CNPC基于专家乘积（PoE）对类别分布进行建模，融合属性预测器的预测分布和电路计算出的干预边际分布。论文在五个基准数据集上进行了实验，表明CNPC在任务准确性上优于基线模型。这项工作虽然主要关注可解释AI和因果推理，但其核心框架（结合神经网络和概率图模型进行预测）与构建更复杂、可解释的化学信息学模型（可视为一种“化学大模型”）在方法论上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) enhance the interpretability of end-to-end neural networks by introducing a layer of concepts and predicting the class label from the concept predictions. A key property of CBMs is that they support interventions, i.e., domain experts can correct mispredicted concept values at test time to improve the final accuracy. However, typical CBMs apply interventions by overwriting only the corrected concept while leaving other concept predictions unchanged, which ignores causal dependencies among concepts. To address this, we propose the Causal Neural Probabilistic Circuit (CNPC), which combines a neural attribute predictor with a causal probabilistic circuit compiled from a causal graph. This circuit supports exact, tractable causal inference that inherently respects causal dependencies. Under interventions, CNPC models the class distribution based on a Product of Experts (PoE) that fuses the attribute predictor's predictive distribution with the interventional marginals computed by the circuit. We theoretically characterize the compositional interventional error of CNPC w.r.t. its modules and identify conditions under which CNPC closely matches the ground-truth interventional class distribution. Experiments on five benchmark datasets in both in-distribution and out-of-distribution settings show that, compared with five baseline models, CNPC achieves higher task accuracy across different numbers of intervened attributes.

</details>

---

### 49. [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph Instruction Tuning](https://arxiv.org/abs/2603.01385)

**基本信息**

- 🔗 arXiv: [`2603.01385`](https://arxiv.org/abs/2603.01385)
- 👥 作者: Zhongjian Zhang, Xiao Wang, Mengmei Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01385.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大语言模型对图结构数据的理解和处理（图-语言对齐），这是构建能够处理分子图等化学数据的“化学大模型”或图基础模型的基础和关键挑战。

**📖 中文摘要**

本文提出了RGLM（重建式图指令调优）框架，旨在改进图标记化大语言模型（GTokenLLMs）中图数据与语言空间的对齐问题。现有GTokenLLMs仅依赖语言指令的文本监督，导致文本主导偏差，未能充分利用图上下文。RGLM通过从LLM的图标记输出中重建图信息，显式地引入图监督来约束对齐过程。论文从输入空间和潜在空间探索了三种变体，并进行了理论分析。在多个基准和任务场景上的广泛实验验证了RGLM的有效性。这项工作直接针对如何让大语言模型更好地理解和处理图结构数据（如分子图），是构建通用图基础模型（可应用于化学信息学中的分子图）的关键步骤，因此与“化学大模型”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The remarkable success of large language models (LLMs) has motivated researchers to adapt them as universal predictors for various graph-related tasks, with the ultimate goal of developing a graph foundation model that generalizes diverse scenarios. The key challenge is to align graph data with language spaces so that LLMs can better comprehend graphs. As a popular paradigm, Graph-Tokenizing LLMs (GTokenLLMs) encode complex structures and lengthy texts into a graph token sequence, and then align them with text tokens via language instructions tuning. Despite their initial success, our information-theoretic analysis reveals that existing GTokenLLMs rely solely on text supervision from language instructions, which achieve only implicit graph-text alignment, resulting in a text-dominant bias that underutilizes graph context. To overcome this limitation, we first prove that the alignment objective is upper-bounded by the mutual information between the input graphs and their hidden representations in the LLM, which motivates us to improve this upper bound to achieve better alignment. To this end, we further propose a reconstructive graph instruction tuning pipeline, RGLM. Our key idea is to reconstruct the graph information from the LLM's graph token outputs, explicitly incorporating graph supervision to constrain the alignment process. Technically, we embody RGLM by exploring three distinct variants from two complementary perspectives: RGLM-Decoder from the input space; RGLM-Similarizer and RGLM-Denoiser from the latent space. Additionally, we theoretically analyze the alignment effectiveness of each variant. Extensive experiments on various benchmarks and task scenarios validate the effectiveness of the proposed RGLM, paving the way for new directions in GTokenLLMs' alignment research.

</details>

---

### 50. [Invariant-Stratified Propagation for Expressive Graph Neural Networks](https://arxiv.org/abs/2603.01388)

**基本信息**

- 🔗 arXiv: [`2603.01388`](https://arxiv.org/abs/2603.01388)
- 👥 作者: Asela Hevapathige, Ahad N. Zehmakan, Asiri Wijesinghe 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01388.pdf)

**💡 相关性分析**

满足标准1：论文提出了提升图神经网络（GNN）表达能力和结构感知能力的新框架（ISP）。由于GNN是化学信息学中用于分子表示和性质预测的核心模型，增强GNN能力的研究直接有助于构建更强大的“化学大模型”。

**📖 中文摘要**

本文介绍了不变分层传播（ISP）框架，包括一种新的WL变体（ISP-WL）及其高效的神经网络实现（ISPGNN），旨在解决图神经网络（GNNs）在表达性和捕获结构异质性方面的根本限制。ISP根据图不变量对节点进行分层，在分层结构中处理它们，从而揭示对1-WL不可见的结构区别。它通过分层结构异质性编码来量化节点在高级模式中结构位置的差异。论文提供了形式化理论分析，确立了超越1-WL的增强表达能力、收敛保证和固有的抗过度平滑性。在图分类、节点分类和影响力估计上的实验表明其优于标准架构和最先进的表达性基线。这项工作提升了GNN的表达能力，而GNN是“化学大模型”中用于分子表示学习的核心技术，因此与构建更强大的化学信息学模型相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph Neural Networks (GNNs) face fundamental limitations in expressivity and capturing structural heterogeneity. Standard message-passing architectures are constrained by the 1-dimensional Weisfeiler-Leman (1-WL) test, unable to distinguish graphs beyond degree sequences, and aggregate information uniformly from neighbors, failing to capture how nodes occupy different structural positions within higher-order patterns. While methods exist to achieve higher expressivity, they incur prohibitive computational costs and lack unified frameworks for flexibly encoding diverse structural properties. To address these limitations, we introduce Invariant-Stratified Propagation (ISP), a framework comprising both a novel WL variant (ISP-WL) and its efficient neural network implementation (ISPGNN). ISP stratifies nodes according to graph invariants, processing them in hierarchical strata that reveal structural distinctions invisible to 1-WL. Through hierarchical structural heterogeneity encoding, ISP quantifies differences in nodes' structural positions within higher-order patterns, distinguishing interactions where participants occupy different roles from those with uniform participation. We provide formal theoretical analysis establishing enhanced expressivity beyond 1-WL, convergence guarantees, and inherent resistance to oversmoothing. Extensive experiments across graph classification, node classification, and influence estimation demonstrate consistent improvements over standard architectures and state-of-the-art expressive baselines.

</details>

---

### 51. [HarmonyCell: Automating Single-Cell Perturbation Modeling under Semantic and Distribution Shifts](https://arxiv.org/abs/2603.01396)

**基本信息**

- 🔗 arXiv: [`2603.01396`](https://arxiv.org/abs/2603.01396)
- 👥 作者: Wenxuan Huang, Mingyu Tsoi, Yanhao Huang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01396.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大语言模型（LLM）处理语义异构性和进行自动化模型架构设计的AI代理框架（HarmonyCell）。这种方法论创新对于构建能够处理复杂、异构化学数据（如不同来源的分子数据集）的“化学大模型”具有参考价值。

**📖 中文摘要**

本文提出了HarmonyCell，一个端到端的代理框架，用于自动化单细胞扰动建模。它通过两个专用机制解决语义异质性和统计异质性瓶颈：一个LLM驱动的语义统一器自动将不同的元数据映射到规范接口；一个自适应蒙特卡洛树搜索引擎在分层动作空间上操作，以合成具有最佳统计归纳偏好的架构来应对分布偏移。在涵盖语义和分布偏移的多样化扰动任务上的评估表明，HarmonyCell在异构输入数据集上实现了95%的有效执行率，同时在严格的分布外评估中达到或超过了专家设计的基线性能。虽然应用领域是计算生物学（单细胞分析），但其核心技术创新在于利用LLM处理语义异构性和自动化模型架构搜索，这些方法可以迁移到化学信息学中处理异构化学数据和自动化模型构建，因此与“化学大模型”主题在方法论上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell perturbation studies face dual heterogeneity bottlenecks: (i) semantic heterogeneity--identical biological concepts encoded under incompatible metadata schemas across datasets; and (ii) statistical heterogeneity--distribution shifts from biological variation demanding dataset-specific inductive biases. We propose HarmonyCell, an end-to-end agent framework resolving each challenge through a dedicated mechanism: an LLM-driven Semantic Unifier autonomously maps disparate metadata into a canonical interface without manual intervention; and an adaptive Monte Carlo Tree Search engine operates over a hierarchical action space to synthesize architectures with optimal statistical inductive biases for distribution shifts. Evaluated across diverse perturbation tasks under both semantic and distribution shifts, HarmonyCell achieves a 95% valid execution rate on heterogeneous input datasets (versus 0% for general agents) while matching or even exceeding expert-designed baselines in rigorous out-of-distribution evaluations. This dual-track orchestration enables scalable automatic virtual cell modeling without dataset-specific engineering.

</details>

---

### 52. [SciDER: Scientific Data-centric End-to-end Researcher](https://arxiv.org/abs/2603.01421)

**基本信息**

- 🔗 arXiv: [`2603.01421`](https://arxiv.org/abs/2603.01421)
- 👥 作者: Ke Lin, Yilin Lu, Shreyas Bhat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01421.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为SciDER的自动化科研系统，该系统能够处理和分析原始科学数据，并基于数据特征进行假设生成和实验设计。这为化学信息学和质谱分析领域提供了一个可用于相关主题（如基于数据的结构推理）的数据处理工具和自动化研究框架。

**📖 中文摘要**

这篇论文介绍了SciDER，一个数据驱动的端到端自动化科研系统。该系统通过专门的智能体协作解析和分析原始科学数据（例如来自科学实验的数据），生成假设和实验设计，并编写和执行相应的代码。论文强调其系统是一个模块化的Python包，提供了易于使用的PyPI包和轻量级Web界面，旨在加速自主的、数据驱动的科学研究。虽然论文的核心是通用科研自动化，但其核心能力——自动处理和分析原始科学数据（可能包括质谱等仪器数据），并基于数据特征进行推理和实验设计——与“化学大模型”和“质谱结构推理”主题高度相关。该系统可以视为一个用于科学发现（包括化学信息学）的自动化工具和框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated scientific discovery with large language models is transforming the research lifecycle from ideation to experimentation, yet existing agents struggle to autonomously process raw data collected from scientific experiments. We introduce SciDER, a data-centric end-to-end system that automates the research lifecycle. Unlike traditional frameworks, our specialized agents collaboratively parse and analyze raw scientific data, generate hypotheses and experimental designs grounded in specific data characteristics, and write and execute corresponding code. Evaluation on three benchmarks shows SciDER excels in specialized data-driven scientific discovery and outperforms general-purpose agents and state-of-the-art models through its self-evolving memory and critic-led feedback loop. Distributed as a modular Python package, we also provide easy-to-use PyPI packages with a lightweight web interface to accelerate autonomous, data-driven research and aim to be accessible to all researchers and developers.

</details>

---

### 53. [ProtRLSearch: A Multi-Round Multimodal Protein Search Agent with Large Language Models Trained via Reinforcement Learning](https://arxiv.org/abs/2603.01464)

**基本信息**

- 🔗 arXiv: [`2603.01464`](https://arxiv.org/abs/2603.01464)
- 👥 作者: Congying Liu, Taihao Li, Ming Huang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01464.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质分析的多模态搜索智能体，该智能体直接处理蛋白质序列数据并进行复杂的推理。这直接围绕“化学大模型”（处理生物大分子数据）和“质谱结构推理”（蛋白质鉴定和结构解析是质谱的核心应用场景）这两个主题。

**📖 中文摘要**

这篇论文提出了ProtRLSearch，一个用于蛋白质分析的多轮多模态搜索智能体。该智能体在实时搜索中联合利用蛋白质序列（一种特定类型的化学/生物分子数据）和文本作为多模态输入，以生成高质量的报告。论文构建了ProtMCQs基准，包含3000个多选题，用于评估模型在真实蛋白质查询设置下整合蛋白质序列信息和文本多模态输入的能力。任务范围包括受序列约束的蛋白质功能和表型变化推理，以及整合多维序列特征与信号通路和调控网络的综合蛋白质推理。这项工作直接涉及利用分子序列（蛋白质序列）进行复杂推理，与“化学大模型”（处理分子数据）和“质谱结构推理”（蛋白质鉴定和结构分析是质谱的核心应用）的主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein analysis tasks arising in healthcare settings often require accurate reasoning under protein sequence constraints, involving tasks such as functional interpretation of disease-related variants, protein-level analysis for clinical research, and similar scenarios. To address such tasks, search agents are introduced to search protein-related information, providing support for disease-related variant analysis and protein function reasoning in protein-centric inference. However, such search agents are mostly limited to single-round, text-only modality search, which prevents the protein sequence modality from being incorporated as a multimodal input into the search decision-making process. Meanwhile, their reliance on reinforcement learning (RL) supervision that focuses solely on the final answer results in a lack of search process constraints, making deviations in keyword selection and reasoning directions difficult to identify and correct in a timely manner. To address these limitations, we propose ProtRLSearch, a multi-round protein search agent trained with multi-dimensional reward based RL, which jointly leverages protein sequence and text as multimodal inputs during real-time search to produce high quality reports. To evaluate the ability of models to integrate protein sequence information and text-based multimodal inputs in realistic protein query settings, we construct ProtMCQs, a benchmark of 3,000 multiple choice questions (MCQs) organized into three difficulty levels. The benchmark evaluates protein query tasks that range from sequence constrained reasoning about protein function and phenotype changes to comprehensive protein reasoning that integrates multi-dimensional sequence features with signal pathways and regulatory networks.

</details>

---

### 54. [LLM-assisted Semantic Option Discovery for Facilitating Adaptive Deep Reinforcement Learning](https://arxiv.org/abs/2603.01488)

**基本信息**

- 🔗 arXiv: [`2603.01488`](https://arxiv.org/abs/2603.01488)
- 👥 作者: Chang Yao, Jinghui Qin, Kebing Jin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01488.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）的通用知识进行语义技能发现和标注，以提升强化学习的效率和可迁移性。这种利用大模型先验知识进行领域推理和发现的方法论，与“化学大模型”主题中利用大模型进行化学知识推理和发现的研究方向直接相关。

**📖 中文摘要**

这篇论文提出了一个由大型语言模型（LLM）驱动的闭环框架，用于促进自适应深度强化学习（DRL）中的语义技能发现和重用。该框架将自然语言指令映射为可执行规则，并对自动创建的选项进行语义标注。论文指出，LLM的通用知识有助于提高探索效率，并为相似环境提供可迁移的选项。通过在Office World和Montezuma's Revenge两个领域进行实验验证了其有效性。虽然论文背景是机器人技能学习，但其核心创新点在于利用LLM的通用知识来理解和标注技能（选项），这体现了“化学大模型”中利用大模型先验知识进行化学领域推理和发现的思路。该方法论可以迁移到化学信息学中，例如利用LLM理解化学反应规则或分子性质，从而辅助发现或设计实验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite achieving remarkable success in complex tasks, Deep Reinforcement Learning (DRL) is still suffering from critical issues in practical applications, such as low data efficiency, lack of interpretability, and limited cross-environment transferability. However, the learned policy generating actions based on states are sensitive to the environmental changes, struggling to guarantee behavioral safety and compliance. Recent research shows that integrating Large Language Models (LLMs) with symbolic planning is promising in addressing these challenges. Inspired by this, we introduce a novel LLM-driven closed-loop framework, which enables semantic-driven skill reuse and real-time constraint monitoring by mapping natural language instructions into executable rules and semantically annotating automatically created options. The proposed approach utilizes the general knowledge of LLMs to facilitate exploration efficiency and adapt to transferable options for similar environments, and provides inherent interpretability through semantic annotations. To validate the effectiveness of this framework, we conduct experiments on two domains, Office World and Montezuma's Revenge, respectively. The results demonstrate superior performance in data efficiency, constraint compliance, and cross-task transferability.

</details>

---

### 55. [Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification](https://arxiv.org/abs/2603.01511)

**基本信息**

- 🔗 arXiv: [`2603.01511`](https://arxiv.org/abs/2603.01511)
- 👥 作者: Jiayang Wu, Jiale Zhou, Xingyi Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01511.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个多模态框架，用于精确识别蛋白质活性位点。这直接涉及利用先进模型处理化学/生物分子数据并进行结构功能推理，与“化学大模型”和“质谱结构推理”（后者常服务于蛋白质结构功能鉴定）的主题紧密相关。

**📖 中文摘要**

这篇论文提出了MERA，一个用于蛋白质活性位点识别的检索增强多模态混合专家框架。该框架整合了H&E切片、病理报告和细胞核级别的细胞图等多模态数据，通过分层多专家检索和基于Dempster-Shafer证据理论的可靠性感知融合策略，动态聚合上下文信息。论文在ProTAD-Gen和TS125数据集上进行了实验，证明了其有效性。这项工作直接涉及利用多模态数据（包括分子层面的图像和文本）进行蛋白质功能位点的精确识别，这是计算化学和结构生物学的重要问题。虽然不直接使用质谱数据，但其多模态推理框架和针对生物分子结构/功能预测的任务，与“化学大模型”（处理复杂化学/生物数据）和“质谱结构推理”（最终目标之一是理解蛋白质结构和功能）的研究目标高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate identification of protein active sites at the residue level is crucial for understanding protein function and advancing drug discovery. However, current methods face two critical challenges: vulnerability in single-instance prediction due to sparse training data, and inadequate modality reliability estimation that leads to performance degradation when unreliable modalities dominate fusion processes. To address these challenges, we introduce Multimodal Mixture-of-Experts with Retrieval Augmentation (MERA), the first retrieval-augmented framework for protein active site identification. MERA employs hierarchical multi-expert retrieval that dynamically aggregates contextual information from chain, sequence, and active-site perspectives through residue-level mixture-of-experts gating. To prevent modality degradation, we propose a reliability-aware fusion strategy based on Dempster-Shafer evidence theory that quantifies modality trustworthiness through belief mass functions and learnable discounting coefficients, enabling principled multimodal integration. Extensive experiments on ProTAD-Gen and TS125 datasets demonstrate that MERA achieves state-of-the-art performance, with 90% AUPRC on active site prediction and significant gains on peptide-binding site identification, validating the effectiveness of retrieval-augmented multi-expert modeling and reliability-guided fusion.

</details>

---

### 56. [Pharmacology Knowledge Graphs: Do We Need Chemical Structure for Drug Repurposing?](https://arxiv.org/abs/2603.01537)

**基本信息**

- 🔗 arXiv: [`2603.01537`](https://arxiv.org/abs/2603.01537)
- 👥 作者: Youssef Abo-Dahab, Ruby Hernandez, Ismael Caleb Arechiga Duran
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01537.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估在药理学知识图谱中，化学结构表征对于预测药物-靶点相互作用的重要性。这项工作直接围绕“化学大模型”中的一个关键问题——如何最佳地表示和利用化学信息（分子结构）进行下游预测任务，并得出了颠覆性的结论，具有重要的参考价值。

**📖 中文摘要**

这篇论文研究了药理学知识图谱在药物重定位中的应用，并重点探讨了化学结构表征的必要性。作者构建了一个包含药物、蛋白质和适应症的大规模知识图谱，并进行了严格的时序验证。关键发现是，仅使用药物网络拓扑结构和蛋白质特征（ESM-2嵌入），而不使用显式的药物化学结构表示（如基于图注意力的编码器或摩根指纹），就能在预测药物-蛋白质相互作用方面取得最佳性能。这一结果表明，对于预测药理学网络交互，药物化学结构的显式表示可能是有害的，而靶点中心信息和药物网络拓扑本身已足够。这项研究对“化学大模型”在药物发现中的应用具有直接启示：它挑战了在分子表示学习中必须显式编码化学结构的传统观念，为如何更有效地在知识图谱中集成和使用化学信息提供了新的视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The contributions of model complexity, data volume, and feature modalities to knowledge graph-based drug repurposing remain poorly quantified under rigorous temporal validation. We constructed a pharmacology knowledge graph from ChEMBL 36 comprising 5,348 entities including 3,127 drugs, 1,156 proteins, and 1,065 indications. A strict temporal split was enforced with training data up to 2022 and testing data from 2023 to 2025, together with biologically verified hard negatives mined from failed assays and clinical trials. We benchmarked five knowledge graph embedding models and a standard graph neural network with 3.44 million parameters that incorporates drug chemical structure using a graph attention encoder and ESM-2 protein embeddings. Scaling experiments ranging from 0.78 to 9.75 million parameters and from 25 to 100 percent of the data, together with feature ablation studies, were used to isolate the contributions of model capacity, graph density, and node feature modalities. Removing the graph attention based drug structure encoder and retaining only topological embeddings combined with ESM-2 protein features improved drug protein PR-AUC from 0.5631 to 0.5785 while reducing VRAM usage from 5.30 GB to 353 MB. Replacing the drug encoder with Morgan fingerprints further degraded performance, indicating that explicit chemical structure representations can be detrimental for predicting pharmacological network interactions. Increasing model size beyond 2.44 million parameters yielded diminishing returns, whereas increasing training data consistently improved performance. External validation confirmed 6 of the top 14 novel predictions as established therapeutic indications. These results show that drug pharmacological behavior can be accurately predicted using target-centric information and drug network topology alone, without requiring explicit chemical structure representations.

</details>

---

### 57. [Graph-centric Cross-model Data Integration and Analytics in a Unified Multi-model Database](https://arxiv.org/abs/2603.01598)

**基本信息**

- 🔗 arXiv: [`2603.01598`](https://arxiv.org/abs/2603.01598)
- 👥 作者: Zepeng Liu, Sheng Wang, Shixun Huang 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01598.pdf)

**💡 相关性分析**

满足标准2：论文提出的以图模型为中心的跨模型数据集成与分析框架（GCDIA）及其实例GredoDB，为化学信息学中整合分子结构（图）、质谱数据、物化属性（关系/文档）等多源异构数据提供了潜在的数据集成工具和资源思路。

**📖 中文摘要**

本文提出了一种以图模型为中心的跨模型数据集成与分析（GCDIA）方法，并开发了统一的多模型数据库GredoDB。该方法的核心是利用图模型作为中心范式，整合来自关系型、文档型等异构数据模型的相关信息，并执行复杂的分析任务（如回归和相似性计算）。论文重点设计了用于高效GCDI的优化框架和用于GCDA的并行架构。虽然论文主要关注通用数据集成与分析，但其提出的图模型作为中心整合范式的思想，以及用于高效处理异构数据模型间关联的图操作符和优化技术，为化学信息学领域（特别是处理分子图、谱图、属性等异构数据）提供了潜在的数据集成与分析框架和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-centric cross-model data integration and analytics (GCDIA) refer to tasks that leverage the graph model as a central paradigm to integrate relevant information across heterogeneous data models, such as relational and document, and subsequently perform complex analytics such as regression and similarity computation. As modern applications generate increasingly diverse data and move beyond simple retrieval toward advanced analytical objectives (e.g., prediction and recommendation), GCDIA has become increasingly important. Existing multi-model databases (MMDBs) struggle to efficiently support both integration (GCDI) and analytics (GCDA) in GCDIA. They typically separate graph processing from other models without global optimization for GCDI, while relying on tuple-at-a-time execution for GCDA, leading to limited performance and scalability. To address these limitations, we propose GredoDB, a unified MMDB that natively supports storing graph, relational, and document models, while efficiently processing GCDIA. Specifically, we design 1) topology- and attribute-aware graph operators for efficient predicate-aware traversal, 2) a unified GCDI optimization framework to exploit cross-model correlations, and 3) a parallel GCDA architecture that materializes intermediate results for operator-level execution. Experiments on the widely adopted multi-model benchmark M2Bench demonstrate that, in terms of response time, GredoDB achieves up to 107.89 times and an average of 10.89 times speedup on GCDI, and up to 356.72 times and an average of 37.79 times on GCDA, compared to state-of-the-art (SOTA) MMDBs.

</details>

---

### 58. [CeProAgents: A Hierarchical Agents System for Automated Chemical Process Development](https://arxiv.org/abs/2603.01654)

**基本信息**

- 🔗 arXiv: [`2603.01654`](https://arxiv.org/abs/2603.01654)
- 👥 作者: Yuhang Yang, Ruikang Li, Jifei Ma 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01654.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大型语言模型（LLM）的分层多智能体系统（CeProAgents）来自动化化学过程开发。这直接属于“化学大模型”在专业化学工程领域的应用研究。

**📖 中文摘要**

本文提出了CeProAgents，一个用于自动化化学过程开发的分层多智能体系统。该系统由专注于知识、概念和参数的三组专业智能体组成，通过动态聊天组和结构化工作流进行协作。作者还建立了CeProBench基准来评估系统在化学过程开发三个核心维度上的能力。这项工作直接应用大型语言模型（LLMs）和智能体技术来解决化学工程中的复杂问题，是“化学大模型”在工业化学工程领域的一个具体而深入的应用案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of chemical processes, a cornerstone of chemical engineering, presents formidable challenges due to its multi-faceted nature, integrating specialized knowledge, conceptual design, and parametric simulation. Capitalizing on this, we propose CeProAgents, a hierarchical multi-agent system designed to automate the development of chemical process through collaborative division of labor. Our architecture comprises three specialized agent cohorts focused on knowledge, concept, and parameter respectively. To effectively adapt to the inherent complexity of chemical tasks, each cohort employs a novel hybrid architecture that integrates dynamic agent chatgroups with structured agentic workflows. To rigorously evaluate the system, we establish CeProBench, a multi-dimensional benchmark structured around three core pillars of chemical engineering. We design six distinct types of tasks across these dimensions to holistically assess the comprehensive capabilities of the system in chemical process development. The results not only confirm the effectiveness and superiority of our proposed approach but also reveal the transformative potential as well as the current boundaries of Large Language Models (LLMs) for industrial chemical engineering.

</details>

---

### 59. [Transform-Invariant Generative Ray Path Sampling for Efficient Radio Propagation Modeling](https://arxiv.org/abs/2603.01655)

**基本信息**

- 🔗 arXiv: [`2603.01655`](https://arxiv.org/abs/2603.01655)
- 👥 作者: Jérome Eertmans, Enrico M. Vitucci, Vittorio Degli-Esposti 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01655.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于生成流网络（GFlowNets）的智能采样框架，为解决“质谱结构推理”中从庞大的候选结构空间中高效、准确地搜索和生成可能分子结构这一核心挑战，提供了新颖的计算方法和工具思路。

**📖 中文摘要**

本文提出了一种基于生成流网络（GFlowNets）的机器学习辅助框架，用于高效无线电传播建模中的射线路径采样。该框架旨在替代传统射线追踪中计算复杂度呈指数级增长的穷举搜索。通过结合经验回放缓冲区、均匀探索策略和基于物理的动作掩码等关键组件，该模型能够智能采样有效路径。论文在实验验证中展示了该方法在保持高覆盖精度的同时，能显著加速复杂传播路径的发现。虽然应用领域是无线通信，但其核心方法——使用生成模型（GFlowNets）进行组合空间（如分子构象空间、反应路径空间）的高效采样和探索——与化学信息学中“质谱结构推理”所面临的从庞大化学空间中找到可能结构的挑战在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ray tracing has become a standard for accurate radio propagation modeling, but suffers from exponential computational complexity, as the number of candidate paths scales with the number of objects raised to the power of the interaction order. This bottleneck limits its use in large-scale or real-time applications, forcing traditional tools to rely on heuristics to reduce the number of path candidates at the cost of potentially reduced accuracy. To overcome this limitation, we propose a comprehensive machine-learning-assisted framework that replaces exhaustive path searching with intelligent sampling via Generative Flow Networks. Applying such generative models to this domain presents significant challenges, particularly sparse rewards due to the rarity of valid paths, which can lead to convergence failures and trivial solutions when evaluating high-order interactions in complex environments. To ensure robust learning and efficient exploration, our framework incorporates three key architectural components. First, we implement an \emph{experience replay buffer} to capture and retain rare valid paths. Second, we adopt a uniform exploratory policy to improve generalization and prevent the model from overfitting to simple geometries. Third, we apply a physics-based action masking strategy that filters out physically impossible paths before the model even considers them. As demonstrated in our experimental validation, the proposed model achieves substantial speedups over exhaustive search -- up to $10\times$ faster on GPU and $1000\times$ faster on CPU -- while maintaining high coverage accuracy and successfully uncovering complex propagation paths. The complete source code, tests, and tutorial are available at this https URL .

</details>

---

### 60. [FreeGNN: Continual Source-Free Graph Neural Network Adaptation for Renewable Energy Forecasting](https://arxiv.org/abs/2603.01657)

**基本信息**

- 🔗 arXiv: [`2603.01657`](https://arxiv.org/abs/2603.01657)
- 👥 作者: Abderaouf Bahi, Amel Ourici, Ibtissem Gasmi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01657.pdf)

**💡 相关性分析**

满足标准2：论文提出的持续源无关图域自适应框架（FreeGNN）及其集成的GNN、记忆回放、正则化等技术，为化学信息学中处理动态、非平稳数据（如随时间变化的质谱数据库、分子性质演化）提供了先进的模型架构和算法工具。

**📖 中文摘要**

本文提出了FreeGNN，一个用于可再生能源预测的持续源无关图域自适应框架。该框架集成了时空图神经网络（GNN）骨干网络，并结合了教师-学生策略、记忆回放、基于图的正则化和漂移感知加权方案，使模型能够在没有源数据和目标标签的情况下，持续适应非平稳环境。论文在多个真实世界可再生能源数据集上进行了实验验证。虽然应用场景是可再生能源预测，但其核心技术创新——基于图神经网络的持续学习、域自适应和知识保留方法——为化学信息学中处理随时间演化的分子性质预测、光谱-结构关系建模等任务提供了有价值的模型框架和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate forecasting of renewable energy generation is essential for efficient grid management and sustainable power planning. However, traditional supervised models often require access to labeled data from the target site, which may be unavailable due to privacy, cost, or logistical constraints. In this work, we propose FreeGNN, a Continual Source-Free Graph Domain Adaptation framework that enables adaptive forecasting on unseen renewable energy sites without requiring source data or target labels. Our approach integrates a spatio-temporal Graph Neural Network (GNN) backbone with a teacher--student strategy, a memory replay mechanism to mitigate catastrophic forgetting, graph-based regularization to preserve spatial correlations, and a drift-aware weighting scheme to dynamically adjust adaptation strength during streaming updates. This combination allows the model to continuously adapt to non-stationary environmental conditions while maintaining robustness and stability. We conduct extensive experiments on three real-world datasets: GEFCom2012, Solar PV, and Wind SCADA, encompassing multiple sites, temporal resolutions, and meteorological features. The ablation study confirms that each component memory, graph regularization, drift-aware adaptation, and teacher--student strategy contributes significantly to overall performance. The experiments show that FreeGNN achieves an MAE of 5.237 and an RMSE of 7.123 on the GEFCom dataset, an MAE of 1.107 and an RMSE of 1.512 on the Solar PV dataset, and an MAE of 0.382 and an RMSE of 0.523 on the Wind SCADA dataset. These results demonstrate its ability to achieve accurate and robust forecasts in a source-free, continual learning setting, highlighting its potential for real-world deployment in adaptive renewable energy systems. For reproducibility, implementation details are available at: this https URL .

</details>

---

### 61. [QIME: Constructing Interpretable Medical Text Embeddings via Ontology-Grounded Questions](https://arxiv.org/abs/2603.01690)

**基本信息**

- 🔗 arXiv: [`2603.01690`](https://arxiv.org/abs/2603.01690)
- 👥 作者: Yixuan Tang, Zhenghong Lin, Yandong Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01690.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于本体生成可解释问题嵌入的框架（QIME），为化学信息学领域构建可解释的分子表征、质谱特征嵌入或辅助大模型决策提供了创新的方法论和工具资源。

**📖 中文摘要**

本文提出了QIME（Ontology-grounded Questions for Interpretable Medical Text Embeddings），一个用于构建可解释医学文本嵌入的框架。QIME通过基于医学本体簇的概念签名生成语义原子化的是/否问题，使嵌入的每个维度对应一个具有临床意义的问题，从而提供简洁且信息丰富的解释。此外，QIME支持无需训练的分类器构建策略。在生物医学语义相似性、聚类和检索基准测试中，QIME性能优于先前的可解释嵌入方法，并显著缩小了与黑盒编码器的差距。该方法的核心思想（基于领域知识生成可解释的问题维度）和框架，可直接迁移至化学信息学领域，用于构建可解释的分子或质谱表征，辅助“化学大模型”或“质谱结构推理”的决策过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While dense biomedical embeddings achieve strong performance, their black-box nature limits their utility in clinical decision-making. Recent question-based interpretable embeddings represent text as binary answers to natural-language questions, but these approaches often rely on heuristic or surface-level contrastive signals and overlook specialized domain knowledge. We propose QIME, an ontology-grounded framework for constructing interpretable medical text embeddings in which each dimension corresponds to a clinically meaningful yes/no question. By conditioning on cluster-specific medical concept signatures, QIME generates semantically atomic questions that capture fine-grained distinctions in biomedical text. Furthermore, QIME supports a training-free embedding construction strategy that eliminates per-question classifier training while further improving performance. Experiments across biomedical semantic similarity, clustering, and retrieval benchmarks show that QIME consistently outperforms prior interpretable embedding methods and substantially narrows the gap to strong black-box biomedical encoders, while providing concise and clinically informative explanations.

</details>

---

### 62. [Dual Distillation for Few-Shot Anomaly Detection](https://arxiv.org/abs/2603.01713)

**基本信息**

- 🔗 arXiv: [`2603.01713`](https://arxiv.org/abs/2603.01713)
- 👥 作者: Le Dong, Qinzhong Tan, Chunlei Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01713.pdf)

**💡 相关性分析**

满足标准2：论文提出的少样本异常检测双重蒸馏框架（D²4FAD）及其学习加权机制，为化学信息学中处理小样本质谱数据、识别异常谱图或进行小样本下的分子结构分类/回归任务提供了先进的机器学习模型和算法资源。

**📖 中文摘要**

本文提出了D²4FAD，一种用于少样本异常检测的双重蒸馏框架。该框架利用预训练编码器作为教师网络提取支持图像和查询图像的多尺度特征，学生解码器则学习在查询图像上蒸馏教师知识，并在支持图像上进行自蒸馏。此外，还提出了一个基于查询条件动态评估每个支持图像参考价值的学习加权机制。论文在包含多个器官、成像模态和疾病类别的综合医学影像基准数据集上进行了评估。虽然应用于医学影像，但其少样本学习、知识蒸馏和异常检测的框架，对于化学信息学中“质谱结构推理”的相关任务（如基于少量已知谱图推断未知结构的异常谱峰，或小样本下的分子性质异常检测）具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anomaly detection is a critical task in computer vision with profound implications for medical imaging, where identifying pathologies early can directly impact patient outcomes. While recent unsupervised anomaly detection approaches show promise, they require substantial normal training data and struggle to generalize across anatomical contexts. We introduce D$^2$4FAD, a novel dual distillation framework for few-shot anomaly detection that identifies anomalies in previously unseen tasks using only a small number of normal reference images. Our approach leverages a pre-trained encoder as a teacher network to extract multi-scale features from both support and query images, while a student decoder learns to distill knowledge from the teacher on query images and self-distill on support images. We further propose a learn-to-weight mechanism that dynamically assesses the reference value of each support image conditioned on the query, optimizing anomaly detection performance. To evaluate our method, we curate a comprehensive benchmark dataset comprising 13,084 images across four organs, four imaging modalities, and five disease categories. Extensive experiments demonstrate that D$^2$4FAD significantly outperforms existing approaches, establishing a new state-of-the-art in few-shot medical anomaly detection. Code is available at this https URL .

</details>

---

### 63. [Solving Inverse PDE Problems using Minimization Methods and AI](https://arxiv.org/abs/2603.01731)

**基本信息**

- 🔗 arXiv: [`2603.01731`](https://arxiv.org/abs/2603.01731)
- 👥 作者: Noura Helwani, Sophie Moufawad, Georges Sakr
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01731.pdf)

**💡 相关性分析**

满足标准2：论文系统研究了基于物理信息神经网络（PINNs）求解PDE反问题的方法，为“质谱结构推理”这类从观测数据（谱图）反推底层模型参数（分子结构）的逆问题提供了前沿的AI求解框架和计算工具。

**📖 中文摘要**

本文研究了使用最小化方法和人工智能（特别是物理信息神经网络PINNs）求解偏微分方程（PDE）控制系统的正问题和反问题。论文首先以逻辑微分方程为例验证数值方案和PINN性能，然后针对无一般闭式解的非线性多孔介质方程（PME），构建了强大的正问题求解器，并测试了反问题中的参数估计技术。结果表明，PINNs能以有竞争力的计算成本密切估计解，是求解复杂系统正反问题的有效工具。这项工作展示了AI方法（尤其是PINNs）在解决科学计算反问题上的潜力，这与“质谱结构推理”的本质（从观测数据反推分子结构参数）在问题范式上高度一致，为其提供了新的求解思路和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many physical and engineering systems require solving direct problems to predict behavior and inverse problems to determine unknown parameters from measurement. In this work, we study both aspects for systems governed by differential equations, contrasting well-established numerical methods with new AI-based techniques, specifically Physics-Informed Neural Networks (PINNs). We first analyze the logistic differential equation, using its closed-form solution to verify numerical schemes and validate PINN performance. We then address the Porous Medium Equation (PME), a nonlinear partial differential equation with no general closed-form solution, building strong solvers of the direct problem and testing techniques for parameter estimation in the inverse problem. Our results suggest that PINNs can closely estimate solutions at competitive computational cost, and thus propose an effective tool for solving both direct and inverse problems for complex systems.

</details>

---

### 64. [Practical Deep Heteroskedastic Regression](https://arxiv.org/abs/2603.01750)

**基本信息**

- 🔗 arXiv: [`2603.01750`](https://arxiv.org/abs/2603.01750)
- 👥 作者: Mikkel Jordahn, Jonas Vestergaard Jensen, James Harrison 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01750.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是在分子图数据集上进行深度异方差回归和不确定性量化，这直接属于化学信息学范畴。同时，其提出的实用UQ方法为化学大模型和质谱结构推理中的预测可靠性评估提供了重要的模型工具和技术资源。

**📖 中文摘要**

本文研究了深度学习异方差回归中的不确定性量化（UQ）问题。针对训练深度异方差回归模型时在不确定性量化和均值预测之间权衡的实际挑战（如优化困难、表示崩溃、方差过拟合），作者提出了一种简单高效的流程：在预训练网络的中间层上，使用留出数据集事后拟合一个方差模型。该方法在多个分子图数据集上实现了先进的不确定性量化，且不损害均值预测精度。这项工作直接面向化学信息学核心数据（分子图），提供了处理回归任务中不确定性（即预测可信度）的实用深度学习方法，这对于“化学大模型”的可靠部署和“质谱结构推理”中置信度评估至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Uncertainty quantification (UQ) in deep learning regression is of wide interest, as it supports critical applications including sequential decision making and risk-sensitive tasks. In heteroskedastic regression, where the uncertainty of the target depends on the input, a common approach is to train a neural network that parameterizes the mean and the variance of the predictive distribution. Still, training deep heteroskedastic regression models poses practical challenges in the trade-off between uncertainty quantification and mean prediction, such as optimization difficulties, representation collapse, and variance overfitting. In this work we identify previously undiscussed fallacies and propose a simple and efficient procedure that addresses these challenges jointly by post-hoc fitting a variance model across the intermediate layers of a pretrained network on a hold-out dataset. We demonstrate that our method achieves on-par or state-of-the-art uncertainty quantification on several molecular graph datasets, without compromising mean prediction accuracy and remaining cheap to use at prediction time.

</details>

---

### 65. [Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence](https://arxiv.org/abs/2603.01752)

**基本信息**

- 🔗 arXiv: [`2603.01752`](https://arxiv.org/abs/2603.01752)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01752.pdf)

**💡 相关性分析**

满足标准3：论文专注于使用稀疏自编码器和因果电路追踪来分析和解释生物学基础模型的内部工作机制。这项工作是对基础模型（包括潜在的化学大模型）可解释性方法论的重要研究和讨论，有助于理解模型如何编码和处理化学信息。

**📖 中文摘要**

本文对单细胞生物学基础模型（Geneformer V2和scGPT）进行了因果电路追踪分析。通过稀疏自编码器分解模型激活，并应用特征消融来测量下游响应，作者揭示了模型内部特征间的因果相互作用。研究发现两个模型均表现出高度的生物一致性和抑制主导性，且跨模型共识识别出大量保守的域对，这些域对与疾病关联性显著增强。这项工作展示了如何利用可解释AI技术（稀疏自编码器、因果分析）来剖析和理解生物学基础模型内部的运作机制。虽然研究对象是生物序列模型，但其方法论（稀疏表示、因果追踪）对于理解和解释“化学大模型”（如分子模型、谱图模型）的内部工作机制具有直接的借鉴意义，属于对基础模型可解释性的重要讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: Sparse autoencoders (SAEs) decompose foundation model activations into interpretable features, but causal feature-to-feature interactions across network depth remain unknown for biological foundation models. Results: We introduce causal circuit tracing by ablating SAE features and measuring downstream responses, and apply it to Geneformer V2-316M and scGPT whole-human across four conditions (96,892 edges, 80,191 forward passes). Both models show approximately 53 percent biological coherence and 65 to 89 percent inhibitory dominance, invariant to architecture and cell type. scGPT produces stronger effects (mean absolute d = 1.40 vs. 1.05) with more balanced dynamics. Cross-model consensus yields 1,142 conserved domain pairs (10.6x enrichment, p < 0.001). Disease-associated domains are 3.59x more likely to be consensus. Gene-level CRISPRi validation shows 56.4 percent directional accuracy, confirming co-expression rather than causal encoding.

</details>

---

### 66. [D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation](https://arxiv.org/abs/2603.01780)

**基本信息**

- 🔗 arXiv: [`2603.01780`](https://arxiv.org/abs/2603.01780)
- 👥 作者: Zhao Yang, Hengchang Liu, Chuan Cao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01780.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于DNA理解和生成的扩散语言模型（D3LM）。这直接属于‘化学大模型’的研究范畴，即开发用于化学/生物分子（此处为DNA）表示和生成的大型基础模型。

**📖 中文摘要**

本文提出了D3LM（离散DNA扩散语言模型），这是一个统一的DNA基础模型，通过离散空间中的掩码扩散实现了双向表示学习和DNA生成。该模型直接采用了Nucleotide Transformer (NT) v2的架构，但将训练目标重新定义为离散DNA空间中的掩码扩散。与同规模的NT v2相比，D3LM在理解任务上取得了更好的性能。在调控元件生成任务上，D3LM的SFID达到了10.92，接近真实DNA序列（7.85），并大幅优于之前自回归模型的最佳结果（29.16）。这项工作表明扩散语言模型是统一DNA基础模型的一个有前景的范式。作者还首次对DNA领域的掩码扩散模型进行了系统研究，探讨了分词方案和采样策略等实际设计选择，为未来研究提供了实证基础和见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early DNA foundation models adopted BERT-style training, achieving good performance on DNA understanding tasks but lacking generative capabilities. Recent autoregressive models enable DNA generation, but employ left-to-right causal modeling that is suboptimal for DNA where regulatory relationships are inherently bidirectional. We present D3LM (\textbf{D}iscrete \textbf{D}NA \textbf{D}iffusion \textbf{L}anguage \textbf{M}odel), which unifies bidirectional representation learning and DNA generation through masked diffusion. D3LM directly adopts the Nucleotide Transformer (NT) v2 architecture but reformulates the training objective as masked diffusion in discrete DNA space, enabling both bidirectional understanding and generation capabilities within a single model. Compared to NT v2 of the same size, D3LM achieves improved performance on understanding tasks. Notably, on regulatory element generation, D3LM achieves an SFID of 10.92, closely approaching real DNA sequences (7.85) and substantially outperforming the previous best result of 29.16 from autoregressive models. Our work suggests diffusion language models as a promising paradigm for unified DNA foundation models. We further present the first systematic study of masked diffusion models in the DNA domain, investigating practical design choices such as tokenization schemes and sampling strategies, thereby providing empirical insights and a solid foundation for future research. D3LM has been released at this https URL .

</details>

---

### 67. [CTForensics: A Comprehensive Dataset and Method for AI-Generated CT Image Detection](https://arxiv.org/abs/2603.01878)

**基本信息**

- 🔗 arXiv: [`2603.01878`](https://arxiv.org/abs/2603.01878)
- 👥 作者: Yiheng Li, Zichang Tan, Guoqing Xu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01878.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为CTForensics的综合数据集，专门用于评估AI生成的CT图像的检测方法。该数据集包含了十种不同的CT生成方法，为‘化学大模型’（特别是生成模型）在医学成像领域的应用和安全性评估提供了重要的数据资源。

**📖 中文摘要**

本文提出了CTForensics，一个用于系统评估CT伪造检测方法泛化能力的综合数据集，包含了十种不同的CT生成方法。此外，作者还引入了增强型空间频率CT伪造检测器（ESF-CTFD），这是一种高效的基于CNN的神经网络，能够在小波、空间和频率域捕获伪造线索。该网络首先将输入的CT图像转换为三个尺度，并通过小波增强中心主干在每个尺度提取特征。然后，从最大尺度的特征开始，空间处理块逐步与较小尺度的特征进行融合。最后，频率处理块学习频域信息以预测最终结果。实验表明，ESF-CTFD在性能上始终优于现有方法，并在不同的CT生成模型上表现出优异的泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rapid development of generative AI in medical imaging, synthetic Computed Tomography (CT) images have demonstrated great potential in applications such as data augmentation and clinical diagnosis, but they also introduce serious security risks. Despite the increasing security concerns, existing studies on CT forgery detection are still limited and fail to adequately address real-world challenges. These limitations are mainly reflected in two aspects: the absence of datasets that can effectively evaluate model generalization to reflect the real-world application requirements, and the reliance on detection methods designed for natural images that are insensitive to CT-specific forgery artifacts. In this view, we propose CTForensics, a comprehensive dataset designed to systematically evaluate the generalization capability of CT forgery detection methods, which includes ten diverse CT generative methods. Moreover, we introduce the Enhanced Spatial-Frequency CT Forgery Detector (ESF-CTFD), an efficient CNN-based neural network that captures forgery cues across the wavelet, spatial, and frequency domains. First, it transforms the input CT image into three scales and extracts features at each scale via the Wavelet-Enhanced Central Stem. Then, starting from the largest-scale features, the Spatial Process Block gradually performs feature fusion with the smaller-scale ones. Finally, the Frequency Process Block learns frequency-domain information for predicting the final results. Experiments demonstrate that ESF-CTFD consistently outperforms existing methods and exhibits superior generalization across different CT generative models.

</details>

---

### 68. [Zero-shot Low-Field MRI Enhancement via Diffusion-Based Adaptive Contrast Transport](https://arxiv.org/abs/2603.01913)

**基本信息**

- 🔗 arXiv: [`2603.01913`](https://arxiv.org/abs/2603.01913)
- 👥 作者: Muyu Liu, Chenhe Du, Xuanyu Tian 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01913.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的生成式框架（DACT），用于解决医学成像（低场MRI增强）中的盲逆问题。这直接属于‘化学大模型’在科学计算和生成建模方向的应用，特别是利用扩散模型进行数据生成和增强。

**📖 中文摘要**

本文提出了DACT（基于扩散的自适应对比度迁移），一种新颖的零样本框架，用于从低场（LF）MRI数据中恢复高场（HF）质量的图像，而无需配对监督。DACT结合了预训练的高场扩散先验以确保解剖保真度，以及一个基于物理信息的自适应前向模型。具体来说，作者引入了一个可微分的Sinkhorn最优传输模块，该模块在反向扩散过程中显式地建模并校正LF和HF域之间的强度分布偏移。这使得框架能够动态学习难以处理的对比度映射，同时保持拓扑一致性。在模拟和真实临床LF数据集上的大量实验表明，DACT实现了最先进的性能，产生了具有卓越结构细节和正确组织对比度的重建图像。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Low-field (LF) magnetic resonance imaging (MRI) democratizes access to diagnostic imaging but is fundamentally limited by low signal-to-noise ratio and significant tissue contrast distortion due to field-dependent relaxation dynamics. Reconstructing high-field (HF) quality images from LF data is a blind inverse problem, severely challenged by the scarcity of paired training data and the unknown, non-linear contrast transformation operator. Existing zero-shot methods, which assume simplified linear degradation, often fail to recover authentic tissue contrast. In this paper, we propose DACT(Diffusion-Based Adaptive Contrast Transport), a novel zero-shot framework that restores HF-quality images without paired supervision. DACT synergizes a pre-trained HF diffusion prior to ensure anatomical fidelity with a physically-informed adaptive forward model. Specifically, we introduce a differentiable Sinkhorn optimal transport module that explicitly models and corrects the intensity distribution shift between LF and HF domains during the reverse diffusion process. This allows the framework to dynamically learn the intractable contrast mapping while preserving topological consistency. Extensive experiments on simulated and real clinical LF datasets demonstrate that DACT achieves state-of-the-art performance, yielding reconstructions with superior structural detail and correct tissue contrast.

</details>

---

### 69. [Probabilistic Retrofitting of Learned Simulators](https://arxiv.org/abs/2603.01949)

**基本信息**

- 🔗 arXiv: [`2603.01949`](https://arxiv.org/abs/2603.01949)
- 👥 作者: Cristiana Diaconu, Miles Cranmer, Richard E. Turner 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01949.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为偏微分方程（PDE）模拟开发概率生成模型，并通过改造（retrofitting）预训练模型来实现。这属于‘化学大模型’在科学计算和不确定性量化方向的应用，即利用生成模型（此处为概率模型）来模拟和预测复杂的物理/化学系统。

**📖 中文摘要**

本文研究了一种训练高效的策略，通过使用连续排序概率评分（CRPS）对预训练的确定性偏微分方程（PDE）模型进行改造，将其转化为概率模型。这种方法与架构无关，可以应用于不同的模型主干。该方法在单动力学系统预训练的模型上取得了显著效果，相对于计算匹配的确定性微调，在滚动CRPS上降低了20-54%，在方差归一化RMSE（VRMSE）上提高了高达30%。作者还在一个PDE基础模型上验证了该方法，该模型在多个系统上进行了预训练，并在目标数据集上进行了改造，结果显示，与确定性微调相比，概率适应在CRPS上提高了高达40%，在VRMSE上提高了高达15。研究结果表明，概率PDE建模无需从头开始训练，可以通过适度的额外训练成本从现有的确定性主干中解锁。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dominant approaches for modelling Partial Differential Equations (PDEs) rely on deterministic predictions, yet many physical systems of interest are inherently chaotic and uncertain. While training probabilistic models from scratch is possible, it is computationally expensive and fails to leverage the significant resources already invested in high-performing deterministic backbones. In this work, we adopt a training-efficient strategy to transform pre-trained deterministic models into probabilistic ones via retrofitting with a proper scoring rule: the Continuous Ranked Probability Score (CRPS). Crucially, this approach is architecture-agnostic: it applies the same adaptation mechanism across distinct model backbones with minimal code modifications. The method proves highly effective across different scales of pre-training: for models trained on single dynamical systems, we achieve 20-54% reductions in rollout CRPS and up to 30% improvements in variance-normalised RMSE (VRMSE) relative to compute-matched deterministic fine-tuning. We further validate our approach on a PDE foundation model, trained on multiple systems and retrofitted on the dataset of interest, to show that our probabilistic adaptation yields an improvement of up to 40% in CRPS and up to 15% in VRMSE compared to deterministic fine-tuning. Validated across diverse architectures and dynamics, our results show that probabilistic PDE modelling need not require retraining from scratch, but can be unlocked from existing deterministic backbones with modest additional training cost.

</details>

---

### 70. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interaction Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于材料科学的机器学习相互作用势（MLIP），这直接属于化学信息学领域，并涉及分子表示和相互作用建模，是构建化学大模型（用于分子模拟和性质预测）的核心技术之一。

**📖 中文摘要**

本文介绍了MatRIS，一个用于材料科学的预训练机器学习相互作用势（MLIP）模型。该模型专注于开发准确且高效的原子相互作用表示，这对于化学信息学中的分子模拟和性质预测至关重要。MatRIS引入了一种基于注意力的三体相互作用建模方法，并采用具有线性复杂度的可分离注意力机制，实现了可扩展性和表达性。该模型在多个基准测试（如Matbench-Discovery、MatPES、MDR声子、分子数据集等）上达到了与领先的等变模型相当的精度，但训练成本更低。这项工作表明，精心设计的非变模型可以以更低的成本匹配甚至超过等变模型的精度，为开发准确高效的MLIPs提供了启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 71. [OpenRad: a Curated Repository of Open-access AI models for Radiology](https://arxiv.org/abs/2603.02062)

**基本信息**

- 🔗 arXiv: [`2603.02062`](https://arxiv.org/abs/2603.02062)
- 👥 作者: Konstantinos Vrettos, Galini Papadaki, Emmanouil Brilakis 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02062.pdf)

**💡 相关性分析**

满足标准2：论文提出了OpenRad，这是一个专门针对放射学AI模型的、经过策划和标准化的数据集和资源库。虽然其直接领域是医学影像，但其构建大规模、标准化模型库的方法论和资源，对于化学信息学和质谱分析领域构建类似的数据集、工具或模型基准具有重要的参考价值和相关性。

**📖 中文摘要**

本文介绍了OpenRad，一个经过精心策划的、标准化的开放获取放射学AI模型存储库。该存储库聚合了放射学AI模型，并提供了预训练权重和交互式应用程序可用性等详细信息。通过对文献和预印本的回顾性分析，该研究创建了约1700个开放获取的、具有标准化元数据的放射学AI模型记录。这项工作为放射学界创建了一个全面的、可搜索的资源，促进了模型的可发现性、可重复性和临床转化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid developments in artificial intelligence (AI) research in radiology have produced numerous models that are scattered across various platforms and sources, limiting discoverability, reproducibility and clinical translation. Herein, OpenRad was created, a curated, standardized, open-access repository that aggregates radiology AI models and providing details such as the availability of pretrained weights and interactive applications. Retrospective analysis of peer reviewed literature and preprints indexed in PubMed, arXiv and Scopus was performed until Dec 2025 (n = 5239 records). Model records were generated using a locally hosted LLM (gpt-oss:120b), based on the RSNA AI Roadmap JSON schema, and manually verified by ten expert reviewers. Stability of LLM outputs was assessed on 225 randomly selected papers using text similarity metrics. A total of 1694 articles were included after review. Included models span all imaging modalities (CT, MRI, X-ray, US) and radiology subspecialties. Automated extraction demonstrated high stability for structured fields (Levenshtein ratio > 90%), with 78.5% of record edits being characterized as minor during expert review. Statistical analysis of the repository revealed CNN and transformer architectures as dominant, while MRI was the most commonly used modality (in 621 neuroradiology AI models). Research output was mostly concentrated in China and the United States. The OpenRad web interface enables model discovery via keyword search and filters for modality, subspecialty, intended use, verification status and demo availability, alongside live statistics. The community can contribute new models through a dedicated portal. OpenRad contains approx. 1700 open access, curated radiology AI models with standardized metadata, supplemented with analysis of code repositories, thereby creating a comprehensive, searchable resource for the radiology community.

</details>

---

### 72. [Generative AI in Software Testing: Current Trends and Future Directions](https://arxiv.org/abs/2603.02141)

**基本信息**

- 🔗 arXiv: [`2603.02141`](https://arxiv.org/abs/2603.02141)
- 👥 作者: Tanish Singla, Qusay H. Mahmoud
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02141.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于生成式AI在软件测试中应用的综述，它包含了对当前应用、方法和未来方向的广泛讨论。虽然主题是软件测试，但其中关于生成式AI（作为AI大模型的一种）的能力、集成方法和挑战的深入分析，对于理解“化学大模型”的构建、应用及评估具有重要的交叉参考和展望价值。

**📖 中文摘要**

本文调查了当前的软件测试系统，并探讨了如何将人工智能，特别是生成式人工智能（Generative AI），集成到这些系统中以增强其能力。研究首先审查了不同类型的AI系统，并重点探讨了生成式AI在通过改进测试覆盖率、提高效率和降低成本来变革软件测试流程方面的潜力。该研究通过广泛的文献综述，概述了AI在软件测试中的当前应用，强调了其在测试用例生成和验证等领域的重大贡献。论文分析了将生成式AI集成到软件测试中的机遇与挑战，为从业者和研究人员提供了宝贵的见解和建议。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper investigates current software testing systems and explores how artificial intelligence, specifically Generative AI, can be integrated to enhance these systems. It begins by examining different types of AI systems and focuses on the potential of Generative AI to transform software testing processes by improving test coverage, increasing efficiency, and reducing costs. The study provides a com-prehensive overview of the current applications of AI in software testing, emphasizing its significant contributions in areas such as test case generation and validation. Through an extensive literature re-view, it highlights how Generative AI can streamline these processes, resulting in more robust and thorough testing outcomes. The paper also examines methods to improve the efficiency of Generative AI systems, such as prompt engineering and fine-tuning. Additionally, it explores the use of AI in specific tasks, including input generation, oracle generation, data generation, test data creation, and test case prioritization. By analyzing the current landscape and identifying both the opportunities and challenges in integrating Generative AI, this paper provides valuable insights and recommendations for practitioners and researchers. It underscores the need for ongoing advancements and targeted development efforts to overcome existing hurdles and fully leverage AI's capabilities. The findings further show that with continued innovation and careful implementation, Generative AI has the potential to significantly enhance the efficiency, effectiveness, and reliability of software testing, particularly in the rapidly evolving field of IoT testing.

</details>

---

### 73. [Exploring Drug Safety Through Knowledge Graphs: Protein Kinase Inhibitors as a Case Study](https://arxiv.org/abs/2603.00097)

**基本信息**

- 🔗 arXiv: [`2603.00097`](https://arxiv.org/abs/2603.00097)
- 👥 作者: David Jackson, Michael Gertz, Jürgen Hesser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00097.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个整合了化学、生物和文本数据的知识图谱框架，这为化学大模型（特别是用于药物发现和安全预测的模型）的构建和验证提供了高质量、结构化的数据集和资源。

**📖 中文摘要**

本文提出了一种基于知识图谱的框架，用于探索药物安全性，以蛋白激酶抑制剂为案例研究。该框架整合了多种异构数据源，包括药物-靶点数据（ChEMBL）、临床试验文献（PubMed）、试验元数据和上市后安全报告（FAERS），构建了一个证据加权的药物与医疗状况二分网络。该框架旨在揭示复杂的模式、支持假设生成并增强药物警戒。虽然论文本身不直接构建化学大模型，但它提供了一个强大的、可扩展的数据集成和分析工具，可用于构建或验证化学信息学中的大模型（例如，用于预测药物-靶点相互作用或不良反应）。此外，其处理化学实体（药物、靶点）和生物医学文本（文献）的能力，与化学信息学中利用多模态数据训练模型的研究方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adverse Drug Reactions (ADRs) are a leading cause of morbidity and mortality. Existing prediction methods rely mainly on chemical similarity, machine learning on structured databases, or isolated target profiles, but often fail to integrate heterogeneous, partly unstructured evidence effectively. We present a knowledge graph-based framework that unifies diverse sources, drug-target data (ChEMBL), clinical trial literature (PubMed), trial metadata ( this http URL ), and post-marketing safety reports (FAERS) into a single evidence-weighted bipartite network of drugs and medical conditions. Applied to 400 protein kinase inhibitors, the resulting network enables contextual comparison of efficacy (HR, PFS, OS), phenotypic and target similarity, and ADR prediction via target-to-adverse-event correlations. A non-small cell lung cancer case study correctly highlights established and candidate drugs, target communities (ERbB, ALK, VEGF), and tolerability differences. Designed as an orthogonal, extensible analysis and search tool rather than a replacement for current models, the framework excels at revealing complex patterns, supporting hypothesis generation, and enhancing pharmacovigilance. Code and data are publicly available at this https URL .

</details>

---

### 74. [Alpha-RF: Automated RF-Filter-Circuit Design with Neural Simulator and Reinforcement Learning](https://arxiv.org/abs/2603.00104)

**基本信息**

- 🔗 arXiv: [`2603.00104`](https://arxiv.org/abs/2603.00104)
- 👥 作者: Nhat Tran, Chenjie Hao, Alexander Stameroff 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00104.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（神经模拟器+强化学习进行物理系统设计与优化）与“化学大模型”主题在方法论上直接相关，为化学领域类似问题（如分子生成、性质预测、反应优化）提供了可借鉴的技术框架。

**📖 中文摘要**

本文提出了一种使用神经模拟器和强化学习的自动射频（RF）滤波器电路设计工具。该方法首先训练一个神经模拟器来替代计算昂贵的电磁PDE模拟器，将仿真时间从数分钟大幅缩短至毫秒级。然后，利用深度强化学习算法训练一个策略，在神经模拟器构建的想象空间中进行自动设计。该工作展示了神经模拟器和强化学习在电路设计领域的应用。虽然其应用领域是射频电路，但其核心方法论——使用神经网络作为物理模拟器的快速替代品，并结合强化学习进行优化搜索——与化学信息学中“化学大模型”的核心思想（即使用AI模型加速或替代传统的计算化学模拟，如分子动力学或量子化学计算）在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate, high-performance radio-frequency (RF) filter circuits are ubiquitous in radio-frequency communication and sensing systems for accepting and rejecting signals at desired frequencies. Conventional RF filter design process involves manual calculations of design parameters, followed by intuition-guided iterations to achieve the desired response for a set of filter specifications. This process is time-consuming due to time- and resource-intensive electromagnetic simulations using full-wave numerical PDE solvers. This process is also highly sensitive to domain expertise and requires many years of professional training. To address these bottlenecks, we propose an automatic RF filter circuit design tool using neural simulator and reinforcement learning. First, we train a neural simulator to replace the PDE electromagnetic simulator. The neural-network-based simulator reduces each of the simulation time from 4 minutes on average to less than 100 millisecond while maintaining a high precision. Such dramatic acceleration enable us to leverage deep reinforcement learning algorithm and train an amortized inference policy to perform automatic design in the imagined space from the neural simulator. The resulted automatic circuit-design agent achieves super-human design results. The automatic circuit-design agent also reduces the on-average design cycle from days to under a few seconds. Even more surprisingly, we demonstrate that the neural simulator can generalize to design spaces far from the training dataset and in a sense it has learned the underlying physics--Maxwell equations. We also demonstrate that the reinforcement learning has discovered many expert-like design intuitions. This work marks a step in using neural simulators and reinforcement learning in RF circuit design and the proposed method is generally applicable to many other design problems and domains in close affinity

</details>

---

### 75. [A Multi-Scenario UAV RF Dataset with Real-World Acquisition and Signal Processing Benchmarking](https://arxiv.org/abs/2603.00106)

**基本信息**

- 🔗 arXiv: [`2603.00106`](https://arxiv.org/abs/2603.00106)
- 👥 作者: Haolin Zheng, Ning Gao, Zhenghang Zhu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00106.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个专门用于RF信号分析的大规模、多场景、高质量数据集。虽然应用领域是无人机识别，但其数据形式（射频信号/频谱）与质谱分析中的谱图数据在结构上具有类比性（都是一维或二维的谱信号）。该数据集及其处理流程（如指纹识别）可为“质谱结构推理”研究提供数据资源和方法论上的参考，例如，将质谱视为分子的“指纹”进行识别和解析。

**📖 中文摘要**

本文提出了一个真实世界的多场景无人机（UAV）射频（RF）数据集DRFF-R2。该数据集使用专用采集平台在不同操作条件下收集，包含来自8种不同型号的26个无人机单元的RF记录，涵盖了不同的飞行状态、高度、速度、采集日期和接收器配置。数据集被系统地组织成七个子集，以促进结构化实验。该数据集为未来的无人机RF信号研究提供了全面的资源，包括RF指纹识别、模型级识别、飞行状态分析和干扰感知信号处理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a real-world multi-scenario unmanned aerial vehicle (UAV) radio frequency (RF) dataset, namely DRFF-R2, which is collected using a dedicated acquisition platform under diverse operational conditions. All signals are acquired within a unified framework to ensure consistency in hardware configuration and environmental settings. The dataset is systematically organized into seven well-defined subsets corresponding to different operational and signal composition scenarios to facilitate structured experimentation. Each file follows a clearly annotated naming convention to enable convenient data indexing and reproducible analysis. The dataset contains RF recordings from 26 UAV units spanning 8 distinct models, captured across varying flight states, altitudes, speeds, acquisition days, and receiver configurations. By covering diverse acquisition settings and signal compositions, the dataset provides a comprehensive resource for future UAV RF signal research, including RF fingerprinting (RFF) identification, model-level recognition, flight state analysis, time-varying RFF study, and interference-aware signal processing.

</details>

---

### 76. [GazeXPErT: An Expert Eye-tracking Dataset for Interpretable and Explainable AI in Oncologic FDG-PET/CT Scans](https://arxiv.org/abs/2603.00162)

**基本信息**

- 🔗 arXiv: [`2603.00162`](https://arxiv.org/abs/2603.00162)
- 👥 作者: Joy T Wu, Daniel Beckmann, Sarah Miller 等18人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00162.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个独特的多模态（图像+眼动轨迹）医学影像数据集，并展示了如何利用人类专家数据来增强AI模型的性能。虽然领域是医学影像，但其核心思想——利用专家行为数据（“软标签”或“过程数据”）来指导和提升AI模型的可解释性与性能——与化学信息学和质谱分析中利用专家知识（例如，化学家对谱图的解析规则）来构建或改进“化学大模型”和“质谱结构推理”模型的研究思路高度契合。

**📖 中文摘要**

本文介绍了GazeXPErT，一个用于肿瘤FDG-PET/CT扫描的4D眼动追踪数据集，旨在促进可解释和可解释AI的研究。该数据集捕获了专家在肿瘤检测和测量过程中的搜索模式，包含来自346次扫描的原始眼动数据，并提取了9030条独特的注视-病灶轨迹。基线实验表明，结合专家注视模式可以显著提升肿瘤分割模型的性能，并且基于视觉Transformer的模型可以改善动态病灶定位和专家意图预测。该数据集为探索视觉 grounding、因果推理、临床可解释特征增强、人机交互等多种机器学习问题提供了宝贵资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

[18F]FDG-PET/CT is a cornerstone imaging modality for tumor staging and treatment response assessment across many cancer types, yet expert reader shortages necessitate more efficient diagnostic aids. While standalone AI models for automatic lesion segmentation exist, clinical translation remains hindered by concerns about interpretability, explainability, reliability, and workflow integration. We present GazeXPErT, a 4D eye-tracking dataset capturing expert search patterns during tumor detection and measurement on 346 FDG-PET/CT scans. Each study was read by a trainee and a board-certified nuclear medicine or radiology specialist using an eye-tracking-enabled annotation platform that simulates routine clinical reads. From 3,948 minutes of raw 60Hz eye-tracking data, 9,030 unique gaze-to-lesion trajectories were extracted, synchronized with PET/CT image slices, and rendered in COCO-style format for multiple machine learning applications. Baseline validation experiments demonstrate that a 3D nnUNet tumor segmentation model achieved superior performance when incorporating expert gaze patterns versus without (DICE score 0.6819 versus 0.6008), and that vision transformers trained on sequential gaze and PET/CT images can improve dynamic lesion localization (74.95% predicted gaze point closer to tumor) and expert intention prediction (Accuracy 67.53% and AUROC 0.747). GazeXPErT is a valuable resource designed to explore multiple machine learning problems beyond these baseline experiments, which include and are not limited to, visual grounding or causal reasoning, clinically explainable feature augmentation, human-computer interaction, human intention prediction or understanding, and expert gaze-rewarded modeling approaches to AI in oncologic FDG-PET/CT imaging.

</details>

---

### 77. [Data-driven Synthesis of Magnetic Resonance Spectroscopy Data using a Variational Autoencoder](https://arxiv.org/abs/2603.00736)

**基本信息**

- 🔗 arXiv: [`2603.00736`](https://arxiv.org/abs/2603.00736)
- 👥 作者: Dennis M.J. van de Sande, Julian P. Merkofer, Sina Amirrajab 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00736.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于生成复杂科学仪器数据（MRS谱）的生成模型框架。该方法直接解决了科学数据稀缺的问题。在“质谱结构推理”领域，同样面临高质量、标注完善的质谱数据稀缺的挑战。本文的VAE框架为生成用于训练质谱解析模型的合成质谱数据提供了直接可借鉴的技术方案。

**📖 中文摘要**

本文提出了一种数据驱动的变分自编码器（VAE）框架，用于合成体内磁共振波谱（MRS）数据。该模型在测量的单个体素波谱数据上训练，学习复杂值谱的低维潜在表示，并通过潜在空间采样和插值生成新样本。研究通过一系列互补分析评估了生成性能，包括重建质量、使用低维嵌入的特征级相似性、基于应用的信号质量指标以及代谢物定量一致性。结果表明，VAE能够准确重建主要光谱模式，并生成与体内数据占据相同特征空间的合成光谱。在一个针对GABA编辑波谱的示例应用中，用合成光谱增强有限的瞬态子集可以改善信噪比、线宽和形状分数等信号质量指标。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of deep learning methods for magnetic resonance spectroscopy (MRS) is often hindered by limited availability of large, high-quality training datasets. While physics-based simulations are commonly used to mitigate this limitation, accurately modeling all in-vivo signal components remains challenging. In this work, we propose a data-driven framework for synthesizing in-vivo MRS data using a variational autoencoder (VAE) trained exclusively on measured single-voxel spectroscopy data. The model learns a low-dimensional latent representation of complex-valued spectra and enables generation of new samples through latent-space sampling and interpolation. The generative performance of the proposed approach is evaluated using a comprehensive set of complementary analyses, including reconstruction quality, feature-level similarity using low-dimensional embeddings, application-based signal quality metrics, and metabolite quantification agreement. The results demonstrate that the VAE accurately reconstructs dominant spectral patterns and generates synthetic spectra that occupy the same feature space as in-vivo data. In an example application targeting GABA-edited spectroscopy, augmenting limited subsets of transients with synthetic spectra improves signal quality metrics such as signal-to-noise ratio, linewidth, and shape scores. However, the results also reveal limitations of the generative approach, including under-representation of stochastic noise and reduced accuracy in absolute metabolite quantification, particularly for applications sensitive to concentration estimates. These findings highlight both potential and limitations of data-driven MRS synthesis. Beyond the proposed model, this study introduces a structured evaluation framework for generative MRS methods, emphasizing the importance of application-aware validation when synthetic data are used for downstream analysis.

</details>

---

### 78. [Time-Aware Latent Space Bayesian Optimization](https://arxiv.org/abs/2603.00935)

**基本信息**

- 🔗 arXiv: [`2603.00935`](https://arxiv.org/abs/2603.00935)
- 👥 作者: Tuan A. Vu, Julien Martinelli, Harri Lähdesmäki
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00935.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对“化学大模型”的一个关键应用场景——分子设计优化，并解决了该场景中一个实际挑战（目标漂移）。它直接改进了基于生成模型（VAE）的贝叶斯优化框架，是“化学大模型”在自动化分子发现领域的核心方法论研究。

**📖 中文摘要**

本文提出了时间感知潜在空间贝叶斯优化（TALBO），用于处理目标函数随时间漂移的结构化域优化问题（如分子设计）。TALBO通过GP先验变分自编码器将时间信息同时纳入代理模型和学习的生成表示中，从而产生与演化目标对齐的潜在空间。为了系统评估时变LSBO，作者将广泛使用的分子设计任务适应于漂移的多属性目标，并引入了针对变化目标的定制指标。在多个基准测试中，TALBO consistently outperforms strong LSBO baselines。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Latent-space Bayesian optimization (LSBO) extends Bayesian optimization to structured domains, such as molecular design, by searching in the continuous latent space of a generative model. However, most LSBO methods assume a fixed objective, whereas real design campaigns often face temporal drift (e.g., evolving preferences or shifting targets). Bringing time-varying BO into LSBO is nontrivial: drift can affect not only the surrogate, but also the latent search space geometry induced by the representation. We propose Time-Aware Latent-space Bayesian Optimization (TALBO), which incorporates time in both the surrogate and the learned generative representation via a GP-prior variational autoencoder, yielding a latent space aligned as objectives evolve. To evaluate timevarying LSBO systematically, we adapt widely used molecular design tasks to drifting multi-property objectives and introduce metrics tailored to changing targets. Across these benchmarks, TALBO consistently outperforms strong LSBO baselines and remains robust across drift speeds and design choices, while remaining competitive under actually time-invariant objectives.

</details>

---

### 79. [Super-resolution of turbulent reacting flows on complex meshes using graph neural networks](https://arxiv.org/abs/2603.01080)

**基本信息**

- 🔗 arXiv: [`2603.01080`](https://arxiv.org/abs/2603.01080)
- 👥 作者: Priyabrat Dash, Konduri Aditya, Christos E. Frouzakis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01080.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用先进的深度学习模型（GNN）对复杂物理系统的数据进行超分辨和特征重建。虽然应用领域是流体力学，但其技术核心——使用GNN处理非欧几里得数据并学习从低维/粗糙表示到高维/精细表示的映射——与“质谱结构推理”问题高度相似。在质谱分析中，目标是从低维质谱信号（一维谱图）推理出高维的分子结构（图结构），GNN正是处理此类问题的理想工具。因此，该论文为质谱结构推理提供了前沿的模型架构参考。

**📖 中文摘要**

本文提出了一种基于图神经网络（GNN）的方法，用于在复杂非结构网格上从低分辨率数据重建湍流反应流中未解析的小尺度结构。该方法利用了GNN消息传递层固有的灵活性，在两个案例上验证了其准确性：结构化非均匀网格上的反应通道流，以及具有非结构网格的氢燃料内燃机。评估结果表明，该方法在准确重建细尺度特征方面是有效的。这项研究为在复杂网格上集成数据驱动的小尺度重建和亚网格尺度建模提供了一条途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

State-of-the-art deep learning models have been extensively utilized to reconstruct small-scale structures from coarse-grained data in turbulent flows. However, their application has predominantly been restricted to structured uniform meshes, limiting their applicability to data associated with complex geometries that are typically simulated on structured non-uniform or unstructured meshes. Machine learning (ML) models based on graph neural networks (GNNs), known for their ability to process unstructured data, offer a promising alternative. In this study, we leverage the inherent flexibility of GNNs featuring message passing layers to develop a methodology for reconstructing unresolved small-scale structures from low-resolution data on complex meshes. The accuracy of the proposed approach is demonstrated using two cases: a reacting channel flow on a structured non-uniform mesh, and a reacting hydrogen fueled internal combustion (IC) engine featuring an unstructured mesh. Evaluation of results based on visual agreement, statistical metrics, and cumulative error reduction indicates the effectiveness of the method in accurately reconstructing fine-scale features. Overall, this study provides a pathway for integrating data-driven small-scale reconstruction and subgrid-scale modeling to enhance the accuracy of coarse-grained simulations on complex meshes.

</details>

---

### 80. [Grokking as a Phase Transition between Competing Basins: a Singular Learning Theory Approach](https://arxiv.org/abs/2603.01192)

**基本信息**

- 🔗 arXiv: [`2603.01192`](https://arxiv.org/abs/2603.01192)
- 👥 作者: Ben Cullen, Sergio Estan-Ruiz, Riya Danait 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01192.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深入理解深度学习模型（包括可能用于构建化学大模型的神经网络）的训练动力学和泛化行为。“顿悟”现象与模型从记忆数据到学习底层规则（如化学规律）的转变直接相关。对这种现象的理论分析（如SLT）对于构建更高效、更可解释、泛化能力更强的“化学大模型”具有重要的指导意义。

**📖 中文摘要**

本文通过奇异学习理论（SLT）的视角研究神经网络训练中的“顿悟”（grokking）现象，即训练后期从记忆到泛化的突然转变。作者将顿悟解释为竞争性零损失解盆地之间的相变。SLT通过局部学习系数（LLC）来表征损失景观的几何形状，LLC较低的盆地对应更高的后验质量集中度和更低的期望泛化误差。本文的主要贡献包括：推导了在模运算任务上训练的二次网络中LLC的闭式表达式，并进行了相应的实证验证；以及提供了经验证据，表明LLC轨迹可以可靠地跟踪训练过程中的泛化动态并解释相变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Grokking, the abrupt transition from memorization to generalisation after extended training, suggests the presence of competing solution basins with distinct statistical properties. We study this phenomenon through the lens of Singular Learning Theory (SLT), a Bayesian framework that characterizes the geometry of the loss landscape via the local learning coefficient (LLC), a measure of the local degeneracy of the loss surface. SLT links lower-LLC basins to higher posterior mass concentration and lower expected generalisation error. Leveraging this theory, we interpret grokking in quadratic networks as a phase transition between competing near-zero-loss solution basins. Our contributions are two-fold: we derive closed-form expressions for the LLC in quadratic networks trained on modular arithmetic tasks, with the corresponding empirical verification; as well as empirical evidence demonstrating that LLC trajectories provide a reliable tool for tracking generalisation dynamics and interpreting phase transitions during training.

</details>

---

### 81. [Graph neural network force fields for adiabatic dynamics of lattice Hamiltonians](https://arxiv.org/abs/2603.02039)

**基本信息**

- 🔗 arXiv: [`2603.02039`](https://arxiv.org/abs/2603.02039)
- 👥 作者: Yunhao Fan, Gia-Wei Chern
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02039.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种图神经网络（GNN）力场框架，用于晶格系统的动力学模拟。虽然其直接应用是物理系统，但所提出的GNN框架作为一种对称性保持的深度学习模型，其核心方法（图神经网络用于学习复杂系统的表示和动力学）与‘化学大模型’主题高度相关，后者广泛涵盖用于化学和材料科学的深度学习模型，特别是图神经网络。

**📖 中文摘要**

本文提出了一种用于晶格哈密顿量绝热动力学的图神经网络（GNN）力场框架。该框架通过局部消息传递和权重共享，直接强制执行离散晶格平移和点群对称性，为大规模量子精确模拟提供了一种概念更简单、更统一的替代方案。作者在半经典Holstein模型上进行了演示，训练后的GNN实现了高精度的力预测、严格的系统尺寸线性缩放以及向大型晶格的直接可迁移性。利用这种可扩展性，作者进行了大规模朗之万模拟，研究了热淬火后的电荷密度波有序化动力学。这项工作确立了GNN作为一种优雅高效的架构，用于具有对称性意识的相关晶格系统大规模动力学模拟。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scalable and symmetry-consistent force-field models are essential for extending quantum-accurate simulations to large spatiotemporal scales. While descriptor-based neural networks can incorporate lattice symmetries through carefully engineered features, we show that graph neural networks (GNNs) provide a conceptually simpler and more unified alternative in which discrete lattice translation and point-group symmetries are enforced directly through local message passing and weight sharing. We develop a GNN-based force-field framework for the adiabatic dynamics of lattice Hamiltonians and demonstrate it for the semiclassical Holstein model. Trained on exact-diagonalization data, the GNN achieves high force accuracy, strict linear scaling with system size, and direct transferability to large lattices. Enabled by this scalability, we perform large-scale Langevin simulations of charge-density-wave ordering following thermal quenches, revealing dynamical scaling and anomalously slow sub--Allen--Cahn coarsening. These results establish GNNs as an elegant and efficient architecture for symmetry-aware, large-scale dynamical simulations of correlated lattice systems.

</details>

---

### 82. [Distributional Priors Guided Diffusion for Generating 3D Molecules in Low Data Regimes](https://arxiv.org/abs/2404.00962)

**基本信息**

- 🔗 arXiv: [`2404.00962`](https://arxiv.org/abs/2404.00962)
- 👥 作者: Haokai Hong, Wanyu Lin, Ming Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2404.00962.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个生成模型（GODD）用于3D分子生成，特别是在数据稀缺和分布偏移（如结构变化）的情况下。这直接属于‘化学大模型’的研究范畴，即利用生成模型（如扩散模型）进行分子设计与发现。

**📖 中文摘要**

本文提出了几何分布外生成扩散模型（GODD），一个新颖的扩散框架，用于在存在分布结构偏移（如分子支架或官能团变化）的情况下，训练数据丰富的分子分布以泛化到数据稀缺的分布。该模型的核心是一个指定的等变非对称自编码器，用于捕获分布结构先验。非对称设计使模型能够通过捕获代表不同分布的分布先验，泛化到未见过的结构变化。编码的结构粒度先验引导生成朝向稀疏区域，而无需在此类数据上显式训练。在涵盖分布外结构偏移（如支架、环）的标准基准测试中，GODD在基于分子有效性、唯一性和新颖性定义的成功率上提高了12.6%。此外，该框架在典型的基于片段的药物设计任务上表现出有前景的性能和泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Can we train a 3D molecule generator using data from dense regions to generate samples in sparse regions? This challenge can be framed as an out-of-distribution (OOD) generation problem. While prior research on OOD generation predominantly targets property shifts, structural shifts -- such as differences in molecular scaffolds or functional groups -- represent an equally critical source of distributional shifts. This work introduces the Geometric OOD Diffusion Model (GODD), a novel diffusion-based framework that enables training on data-abundant molecular distributions while generalizing to data-scarce distributions under distributional structural shifts. Central to our approach is a designated equivariant asymmetric autoencoder to capture distributional structural priors. The asymmetric design allows the model to generalize to unseen structural variations by capturing distributional priors representing distinct distributions. The encoded structural-grained priors guide generation toward sparse regions without requiring explicit training on such data. Evaluated across standard benchmarks encompassing OOD structural shifts (e.g., scaffolds, rings), GODD achieves an improvement of 12.6% in success rate, defined based on molecular validity, uniqueness, and novelty. Furthermore, the framework demonstrates promising performance and generalization on canonical fragment-based drug design tasks, highlighting its utility in learning-based molecular discovery.

</details>

---

### 83. [Generative Enzyme Design Guided by Functionally Important Sites and Small-Molecule Substrates](https://arxiv.org/abs/2405.08205)

**基本信息**

- 🔗 arXiv: [`2405.08205`](https://arxiv.org/abs/2405.08205)
- 👥 作者: Zhenqiao Song, Yunlong Zhao, Wenxian Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于酶设计的生成模型（EnzyGen）。这直接属于‘化学大模型’的研究范畴，即利用人工智能（特别是生成模型和等变神经网络）进行蛋白质/酶的设计与工程化。

**📖 中文摘要**

本文提出了EnzyGen，一种基于功能重要位点和小分子底物来设计跨所有功能家族的酶的统一生成模型。核心思想是基于与期望催化功能对应的功能重要位点和底物，生成酶的氨基酸序列及其三维坐标。这些位点是从酶数据库中自动挖掘的。EnzyGen由一个新颖的注意力和邻域等变层交错网络组成，该网络捕获整个蛋白质序列中的长程相关性以及三维空间中最近氨基酸的局部影响。为了学习生成模型，作者设计了一个联合训练目标，包括序列生成损失、位置预测损失和酶-底物相互作用损失。作者进一步构建了EnzyBench数据集，包含3157个酶家族，涵盖了蛋白质数据库（PDB）中所有可用的酶。实验结果表明，EnzyGen在底物结合亲和力方面始终优于最佳基线10.79%，证明了其在设计折叠良好且能高效结合特定底物的酶方面的卓越能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enzymes are genetically encoded biocatalysts capable of accelerating chemical reactions. How can we automatically design functional enzymes? In this paper, we propose EnzyGen, an approach to learn a unified model to design enzymes across all functional families. Our key idea is to generate an enzyme's amino acid sequence and their three-dimensional (3D) coordinates based on functionally important sites and substrates corresponding to a desired catalytic function. These sites are automatically mined from enzyme databases. EnzyGen consists of a novel interleaving network of attention and neighborhood equivariant layers, which captures both long-range correlation in an entire protein sequence and local influence from nearest amino acids in 3D space. To learn the generative model, we devise a joint training objective, including a sequence generation loss, a position prediction loss and an enzyme-substrate interaction loss. We further construct EnzyBench, a dataset with 3157 enzyme families, covering all available enzymes within the protein data bank (PDB). Experimental results show that our EnzyGen consistently achieves the best performance across all 323 testing families, surpassing the best baseline by 10.79% in terms of substrate binding affinity. These findings demonstrate EnzyGen's superior capability in designing well-folded and effective enzymes binding to specific substrates with high affinities.

</details>

---

### 84. [One protein is all you need](https://arxiv.org/abs/2411.02109)

**基本信息**

- 🔗 arXiv: [`2411.02109`](https://arxiv.org/abs/2411.02109)
- 👥 作者: Anton Bushuiev, Roman Bushuiev, Olga Pimenova 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.02109.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种针对蛋白质语言模型的自适应方法（ProteinTTT），以提升其在特定蛋白质上的结构、适应性和功能预测性能。这直接属于‘化学大模型’的研究范畴，即利用和优化大型预训练模型（如蛋白质语言模型）来解决化学生物学中的具体问题。

**📖 中文摘要**

本文提出了一种方法，使蛋白质语言模型能够针对单个目标蛋白质进行自监督定制，无需额外数据。该方法被称为蛋白质测试时训练（ProteinTTT），它通过自监督学习在测试时（推理时）适应特定蛋白质，从而增强模型对该蛋白质的预测能力。作者展示了ProteinTTT在不同模型、大小和数据集上一致地提高了泛化能力。它改善了具有挑战性目标的结构预测，在蛋白质适应性预测上取得了新的最先进结果，并增强了两个任务上的功能预测。通过两个具有挑战性的案例研究，作者还表明，通过ProteinTTT进行的定制在通用AlphaFold2和ESMFold难以处理的场景下，实现了更准确的抗体-抗原环建模，并改善了Big Fantastic病毒数据库中19%的结构预测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generalization beyond training data remains a central challenge in machine learning for biology. A common way to enhance generalization is self-supervised pre-training on large datasets. However, aiming to perform well on all possible proteins can limit a model's capacity to excel on any specific one, whereas experimentalists typically need accurate predictions for individual proteins they study, often not covered in training data. To address this limitation, we propose a method that enables self-supervised customization of protein language models to one target protein at a time, on the fly, and without assuming any additional data. We show that our Protein Test-Time Training (ProteinTTT) method consistently enhances generalization across different models, their sizes, and datasets. ProteinTTT improves structure prediction for challenging targets, achieves new state-of-the-art results on protein fitness prediction, and enhances function prediction on two tasks. Through two challenging case studies, we also show that customization via ProteinTTT achieves more accurate antibody-antigen loop modeling and enhances 19% of structures in the Big Fantastic Virus Database, delivering improved predictions where general-purpose AlphaFold2 and ESMFold struggle.

</details>

---

### 85. [MoMa: A Modular Deep Learning Framework for Material Property Prediction](https://arxiv.org/abs/2502.15483)

**基本信息**

- 🔗 arXiv: [`2502.15483`](https://arxiv.org/abs/2502.15483)
- 👥 作者: Botian Wang, Yawen Ouyang, Yaohui Li 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.15483.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于材料属性预测的模块化深度学习框架。材料属性预测是化学信息学和计算化学的核心任务，旨在加速新材料（包括分子和化合物）的发现。MoMa框架通过其模块化设计，旨在更有效地学习分子表示和预测其性质，这与“化学大模型”的主题直接相关，因为后者也关注于开发用于化学领域的强大、通用的机器学习模型。

**📖 中文摘要**

这篇论文提出了MoMa，一个用于材料属性预测的模块化深度学习框架。它旨在克服当前“预训练-微调”范式在处理多样化材料任务时的局限性。MoMa首先在广泛的任务上训练专门的模块，然后针对每个下游场景自适应地组合协同模块。在17个数据集上的评估表明，MoMa平均比最强基线有14%的显著提升。该框架与化学信息学领域高度相关，因为它直接针对材料发现中的核心挑战——即开发能够预测和设计具有所需性质的新分子的模型。MoMa代表了一种新的模块化材料学习范式，其开源将促进更广泛的社区合作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning methods for material property prediction have been widely explored to advance materials discovery. However, the prevailing pre-train then fine-tune paradigm often fails to address the inherent diversity and disparity of material tasks. To overcome these challenges, we introduce MoMa, a Modular framework for Materials that first trains specialized modules across a wide range of tasks and then adaptively composes synergistic modules tailored to each downstream scenario. Evaluation across 17 datasets demonstrates the superiority of MoMa, with a substantial 14% average improvement over the strongest baseline. Few-shot and continual learning experiments further highlight MoMa's potential for real-world applications. Pioneering a new paradigm of modular material learning, MoMa will be open-sourced to foster broader community collaboration.

</details>

---

### 86. [Large Language Models in Bioinformatics: A Survey](https://arxiv.org/abs/2503.04490)

**基本信息**

- 🔗 arXiv: [`2503.04490`](https://arxiv.org/abs/2503.04490)
- 👥 作者: Zhenyu Wang, Zikang Wang, Jiyue Jiang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.04490.pdf)

**💡 相关性分析**

满足标准3：这是一篇专门针对大型语言模型（LLMs）在生物信息学中应用的综述论文。虽然生物信息学与化学信息学是紧密相关的领域，但论文中讨论的LLMs在分子序列（DNA、RNA、蛋白质）建模和分析方面的应用，与“化学大模型”主题高度重叠。化学大模型的核心就是利用先进的机器学习模型（如LLMs）来理解和生成分子结构、预测性质。因此，这篇综述提供了关于LLMs在分子科学中应用的重要讨论和展望。

**📖 中文摘要**

这篇综述论文系统回顾了大型语言模型（LLMs）在生物信息学中的最新进展，重点关注DNA、RNA、蛋白质和单细胞数据的分析。论文讨论了LLMs在基因组序列建模、RNA结构预测、蛋白质功能推断和单细胞转录组学等任务中的应用。同时，也探讨了数据稀缺、计算复杂性和跨组学整合等关键挑战，并探索了多模态学习、混合AI模型和临床应用等未来方向。论文强调了LLMs在推动生物信息学和精准医学创新方面的变革潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are revolutionizing bioinformatics, enabling advanced analysis of DNA, RNA, proteins, and single-cell data. This survey provides a systematic review of recent advancements, focusing on genomic sequence modeling, RNA structure prediction, protein function inference, and single-cell transcriptomics. Meanwhile, we also discuss several key challenges, including data scarcity, computational complexity, and cross-omics integration, and explore future directions such as multimodal learning, hybrid AI models, and clinical applications. By offering a comprehensive perspective, this paper underscores the transformative potential of LLMs in driving innovations in bioinformatics and precision medicine.

</details>

---

### 87. [mCLM: A Modular Chemical Language Model that Generates Functional and Makeable Molecules](https://arxiv.org/abs/2505.12565)

**基本信息**

- 🔗 arXiv: [`2505.12565`](https://arxiv.org/abs/2505.12565)
- 👥 作者: Carl Edwards, Chi Han, Gawon Lee 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12565.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”主题。mCLM（模块化化学语言模型）是一个专门为化学领域设计的大型语言模型，它使用分子构建块作为标记，旨在生成功能性和可合成的分子。这完全符合化学大模型的定义，即开发用于化学领域（如分子生成、性质预测）的专用大型生成模型。论文还涉及利用模型进行分子设计和优化，这是化学信息学的核心。

**📖 中文摘要**

这篇论文提出了mCLM，一个模块化的化学语言模型，旨在生成具有所需功能且易于合成的分子。作者认为，当前基于原子表示分子的LLMs存在局限性，并提出应在功能性构建块（与自动化合成兼容的分子片段）的层级上对分子进行标记化。mCLM是一个双语语言模型，能够理解自然语言功能描述和分子构建块。该模型将可合成性考虑前置，并以原则性的方式改进分子的预测功能。实验表明，mCLM能够显著改善化学功能，并在合成可及性方面优于包括GPT-5在内的其他领先生成AI方法。mCLM还能对多种功能进行推理，并迭代式自我改进以拯救在临床试验后期失败的候选药物。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their ability to understand chemical knowledge, large language models (LLMs) remain limited in their capacity to propose novel molecules with desired functions (e.g., drug-like properties). In addition, the molecules that LLMs propose can often be challenging to make, and are almost never compatible with automated synthesis approaches. To better enable the discovery of functional small molecules, LLMs need to learn a new molecular language that is more effective in predicting properties and inherently synced with automated synthesis technology. Current molecule LLMs are limited by representing molecules based on atoms. In this paper, we argue that just like tokenizing texts into meaning-bearing (sub-)word tokens instead of characters, molecules should be tokenized at the level of functional building blocks, i.e., parts of molecules that bring unique functions and serve as effective building blocks for real-world automated laboratory synthesis. This motivates us to propose mCLM, a modular Chemical-Language Model that comprises a bilingual language model that understands both natural language descriptions of functions and molecular blocks. mCLM front-loads synthesizability considerations while improving the predicted functions of molecules in a principled manner. Experiments on FDA-approved drugs showed that mCLM is capable of significantly improving chemical functions. mCLM, with only 3B parameters, also achieves improvements in synthetic accessibility relative to 7 other leading generative AI methods including GPT-5. When tested on 122 out-of-distribution medicines using only building blocks/tokens that are compatible with automated modular synthesis, mCLM outperforms all baselines in property scores and synthetic accessibility. mCLM can also reason on multiple functions and iteratively self-improve to rescue drug candidates that failed late in clinical trials ("fallen angels").

</details>

---

### 88. [RECON: Robust symmetry discovery via Explicit Canonical Orientation Normalization](https://arxiv.org/abs/2505.13289)

**基本信息**

- 🔗 arXiv: [`2505.13289`](https://arxiv.org/abs/2505.13289)
- 👥 作者: Alonso Urbano, David W. Romero, Max Zimmer 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13289.pdf)

**💡 相关性分析**

满足标准1：论文在分子集合上验证其方法，其核心内容（对称性发现与规范化表示）与化学大模型中的分子表示学习主题直接相关。

**📖 中文摘要**

论文提出了RECON方法，用于在数据中发现实例特定的对称性并创建解耦表示。虽然论文主要关注图像和分子集合的通用方法验证，但其在分子集合上的应用表明该方法可用于处理分子结构数据。在化学信息学中，分子结构常被视为具有内在对称性的几何对象，因此该框架可能为分子表示学习（化学大模型的一个核心方面）提供新的思路，即通过对称性发现和规范化来学习更鲁棒和可解释的分子表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real world data often exhibits unknown, instance-specific symmetries that rarely exactly match a transformation group $G$ fixed a priori. Class-pose decompositions aim to create disentangled representations by factoring inputs into invariant features and a pose $g\in G$ defined relative to a training-dependent, arbitrary canonical representation. We introduce RECON, a class-pose agnostic canonical orientation normalization that corrects arbitrary canonicals via a simple right translation, yielding natural, data-aligned canonicalizations. This enables (i) unsupervised discovery of instance-specific pose distributions, (ii) detection of out-of-distribution poses and (iii) a plug-and-play test-time canonicalization layer. This layer can be attached on top of any pre-trained model to infuse group invariance, improving its performance without retraining. We validate on images and molecular ensembles, demonstrating accurate symmetry discovery, and matching or outperforming other canonicalizations in downstream classification.

</details>

---

### 89. [Not All Models Suit Expert Offloading: On Local Routing Consistency of Mixture-of-Expert Models](https://arxiv.org/abs/2505.16056)

**基本信息**

- 🔗 arXiv: [`2505.16056`](https://arxiv.org/abs/2505.16056)
- 👥 作者: Jingcong Liang, Siyuan Wang, Miren Tian 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.16056.pdf)

**💡 相关性分析**

满足标准1：论文对混合专家模型架构和专家专业化的分析，与构建领域专业化（如化学）大模型的核心主题相关。

**📖 中文摘要**

论文研究了混合专家模型中的局部路由一致性，并分析了20种不同规模和架构的MoE LLM。研究发现，领域专业化专家对路由一致性的贡献大于词汇专业化专家。虽然论文主要关注LLM的高效部署，但其对MoE模型架构和专家专业化（包括领域专业化）的深入分析，为构建和优化大规模、模块化的化学领域大模型（可视为一种领域特化的MoE系统）提供了重要的设计原则和见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture-of-Experts (MoE) enables efficient scaling of large language models (LLMs) with sparsely activated experts during inference. To effectively deploy large MoE models on memory-constrained devices, many systems introduce *expert offloading* that caches a subset of experts in fast memory, leaving others on slow memory to run on CPU or load on demand. While some research has exploited the locality of expert activations, where consecutive tokens activate similar experts, the degree of this **local routing consistency** varies across models and remains understudied. In this paper, we propose two metrics to measure local routing consistency of MoE models: (1) **Segment Routing Best Performance (SRP)**, which evaluates how well a fixed group of experts can cover the needs of a segment of tokens, and (2) **Segment Cache Best Hit Rate (SCH)**, which measures the hit rate of an expert cache utilizing a length of future information under a cache limit. We analyze 20 MoE LLMs with diverse sizes and architectures and use toy models to verify key factors related to local routing consistency. We find a strong trade-off between local routing consistency and *local* load balance, while showing that *global* load balance can coexist with local routing consistency. Meanwhile, settings like shared experts that decrease expert combination space can lead to low local routing consistency. We further reveal that domain-specialized experts contribute more to routing consistency than vocabulary-specialized ones, and that most models balance between cache effectiveness and efficiency with cache sizes approximately twice the active experts. These findings pave the way for memory-efficient MoE design and deployment without compromising inference speed. We publish the code for replicating experiments at this https URL .

</details>

---

### 90. [JALMBench: Benchmarking Jailbreak Vulnerabilities in Audio Language Models](https://arxiv.org/abs/2505.17568)

**基本信息**

- 🔗 arXiv: [`2505.17568`](https://arxiv.org/abs/2505.17568)
- 👥 作者: Zifan Peng, Yule Liu, Zhen Sun 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.17568.pdf)

**💡 相关性分析**

满足标准2 & 3：论文提出了一个大型基准数据集和评估框架（资源），并且其关于安全对齐跨模态迁移的讨论对构建稳健的化学多模态大模型具有重要的展望意义。

**📖 中文摘要**

论文提出了JALMBench，一个用于评估音频语言模型越狱漏洞的综合性基准。虽然主要关注音频模态，但论文在分析中发现，文本安全对齐可以部分迁移到音频输入，而交错音频-文本策略能够实现更鲁棒的跨模态泛化。这一发现对于构建安全、可靠的多模态大模型（可能包含化学结构或质谱数据的多模态表示）具有参考价值。此外，基准构建和评估框架本身也可视为一种资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio Language Models (LALMs) have made significant progress. While increasingly deployed in real-world applications, LALMs face growing safety risks from jailbreak attacks that bypass safety alignment. However, there remains a lack of an adversarial audio dataset and a unified framework specifically designed to evaluate and compare jailbreak attacks against them. To address this gap, we introduce JALMBench, a comprehensive benchmark that assesses LALM safety against jailbreak attacks, comprising 11,316 text samples and 245,355 audio samples (>1,000 hours). JALMBench supports 12 mainstream LALMs, 8 attack methods (4 text-transferred and 4 audio-originated), and 5 defenses. We conduct in-depth analysis on attack efficiency, topic sensitivity, voice diversity, and model architecture. Additionally, we explore mitigation strategies for the attacks at both the prompt and response levels. Our systematic evaluation reveals that LALMs' safety is strongly influenced by modality and architectural choices: text-based safety alignment can partially transfer to audio inputs, and interleaved audio-text strategies enable more robust cross-modal generalization. Existing general-purpose moderation methods only slightly improve security, highlighting the need for defense methods specifically designed for LALMs. We hope our work can shed light on the design principles for building more robust LALMs.

</details>

---

### 91. [Discovering and Steering Interpretable Concepts in Large Generative Music Models](https://arxiv.org/abs/2505.18186)

**基本信息**

- 🔗 arXiv: [`2505.18186`](https://arxiv.org/abs/2505.18186)
- 👥 作者: Nikhil Singh, Manuel Cherep, Pattie Maes
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.18186.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（从大模型中提取可解释概念并用于生成引导）直接围绕大模型的可解释性与控制这一主题，可平行应用于化学大模型。

**📖 中文摘要**

论文专注于自回归音乐生成模型，提出了一种使用稀疏自编码器从Transformer模型的残差流中发现可解释概念的方法。该方法旨在揭示模型通过统计学习捕获的、可能与传统理论框架不同但具有解释力的潜在模式。论文展示了这些概念可用于引导模型生成。这项工作的核心——从大型生成模型的内部表示中发现可解释的、可操控的概念——与理解化学大模型（如分子生成或性质预测模型）的内部工作机制高度相关，为化学信息学中的模型可解释性研究提供了直接的方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The fidelity with which neural networks can now generate content such as music presents a scientific opportunity: these systems appear to have learned implicit theories of such content's structure through statistical learning alone. This offers a potentially new lens on theories of human-generated media. When internal representations align with traditional constructs (e.g. chord progressions in music), they show how such categories can emerge from statistical regularities; when they diverge, they expose limits of existing frameworks and patterns we may have overlooked but that nonetheless carry explanatory power. In this paper, focusing on autoregressive music generators, we introduce a method for discovering interpretable concepts using sparse autoencoders (SAEs), extracting interpretable features from the residual stream of a transformer model. We make this approach scalable and evaluable using automated labeling and validation pipelines. Our results reveal both familiar musical concepts and coherent but uncodified patterns lacking clear counterparts in theory or language. As an extension, we show such concepts can be used to steer model generations. Beyond improving model transparency, our work provides an empirical tool for uncovering organizing principles that have eluded traditional methods of analysis and synthesis.

</details>

---

### 92. [RefTool: Reference-Guided Tool Creation for Knowledge-Intensive Reasoning](https://arxiv.org/abs/2505.21413)

**基本信息**

- 🔗 arXiv: [`2505.21413`](https://arxiv.org/abs/2505.21413)
- 👥 作者: Xiao Liu, Da Yin, Zirui Wu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.21413.pdf)

**💡 相关性分析**

满足标准1 & 2：论文的核心研究（参考引导的工具创建）直接旨在提升大模型在化学等科学领域的推理能力，并且其框架可被视为一种增强领域推理的工具或方法资源。

**📖 中文摘要**

论文提出了RefTool框架，一个用于知识密集型推理的参考引导工具创建框架。该框架利用外部参考资料（如教科书）来创建可执行工具，以解决模型内部知识不足的问题。论文在因果、物理和化学基准上进行了实验，证明了其有效性。这项工作直接针对化学等科学领域的推理任务，提供了一种增强大模型在专业领域（如化学）推理能力的具体方法，即通过构建外部知识工具来弥补模型内部知识的局限。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) can enhance their reasoning capabilities by using external tools. However, many tasks lack predefined tools. Prior works have explored instructing LLMs to generate tools on their own, but such approaches depend heavily on internal knowledge and struggle when tasks fall outside the model's knowledge scope. To address this limitation, we propose RefTool, a reference-guided framework for automatic tool creation that leverages external materials, such as textbooks and knowledge snippets. RefTool consists of two modules: (1) tool creation, where LLMs generate executable tools from reference content, validate them using illustrative examples, and organize them hierarchically into a toolbox; and (2) tool utilization, where LLMs navigate the toolbox structure to select and apply the appropriate tools to solve problems. Experiments on causality, physics, and chemistry benchmarks demonstrate that RefTool outperforms existing tool-creation and domain-specific reasoning methods by 12.3% on average accuracy, while being cost-efficient and broadly generalizable to non-scientific tasks, e.g., extremely low-resource language translation. Analyses reveal that grounding tool creation in references produces accurate and faithful tools, and that the hierarchical structure facilitates effective tool selection. RefTool enables LLMs to overcome internal knowledge limitations, advancing generalizable reasoning in knowledge-intensive domains.

</details>

---

### 93. [Rapid training of Hamiltonian graph networks using random features](https://arxiv.org/abs/2506.06558)

**基本信息**

- 🔗 arXiv: [`2506.06558`](https://arxiv.org/abs/2506.06558)
- 👥 作者: Atamert Rahma, Chinmay Datar, Ana Cukarska 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06558.pdf)

**💡 相关性分析**

满足标准1 & 2：论文的核心是提出一种用于分子动力学系统的高效图神经网络训练方法，直接相关于化学大模型中的模拟与动力学预测，并提供了新的方法资源。

**📖 中文摘要**

论文提出使用随机特征而非迭代优化来快速训练哈密顿图网络，用于建模N体动力学和分子动力学系统。该方法在包含多达10,000个粒子的分子动力学系统中展示了鲁棒性能，并保持了物理不变性。这项工作直接针对分子动力学模拟这一化学与物理的核心问题，提出了一种高效训练图神经网络的新范式。其模型（哈密顿图网络）和训练方法为处理大规模分子系统、学习其动力学规律提供了新的工具和思路，与化学大模型（特别是用于模拟的模型）紧密相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning dynamical systems that respect physical symmetries and constraints remains a fundamental challenge in data-driven modeling. Integrating physical laws with graph neural networks facilitates principled modeling of complex N-body dynamics and yields accurate and permutation-invariant models. However, training graph neural networks with iterative, gradient-descent-based optimization algorithms (e.g., Adam, RMSProp, LBFGS) often leads to slow training, especially for large, complex systems. In comparison to 15 different optimizers, we demonstrate that Hamiltonian Graph Networks (HGN) can be trained 150-600x faster - but with comparable accuracy - by replacing iterative optimization with random feature-based parameter construction. We show robust performance in diverse simulations, including N-body mass-spring and molecular dynamics systems in up to dimensions and 10,000 particles with different geometries, while retaining essential physical invariances with respect to permutation, rotation, and translation. Our proposed approach is benchmarked using a NeurIPS 2022 Datasets and Benchmarks Track publication to further demonstrate its versatility. We reveal that even when trained on minimal 8-node systems, the model can generalize in a zero-shot manner to systems as large as 4096 nodes without retraining. Our work challenges the dominance of iterative gradient-descent-based optimization algorithms for training neural network models for physical systems.

</details>

---

### 94. [ProteinZero: Self-Improving Protein Generation via Online Reinforcement Learning](https://arxiv.org/abs/2506.07459)

**基本信息**

- 🔗 arXiv: [`2506.07459`](https://arxiv.org/abs/2506.07459)
- 👥 作者: Ziwen Wang, Jiajun Fan, Ruihan Guo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.07459.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（使用RL优化蛋白质生成模型）直接围绕化学大模型在生物分子设计中的应用主题。

**📖 中文摘要**

论文提出了ProteinZero，一个用于蛋白质逆折叠模型的在线强化学习框架，通过结合ESMFold的结构指导和自衍生的ddG预测器作为奖励，实现蛋白质设计的自主持续改进。该框架在CATH-4.3基准上取得了最先进的性能，显著降低了设计失败率。这项工作直接位于AI驱动蛋白质设计的前沿，是化学大模型在生物分子设计领域的典型应用。其RL框架为优化生成模型（如用于分子或材料设计的扩散模型）提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein generative models have shown remarkable promise in protein design, yet their success rates remain constrained by reliance on curated sequence-structure datasets and by misalignment between supervised objectives and real design goals. We present ProteinZero, an online reinforcement learning framework for inverse folding models that enables scalable, automated, and continuous self-improvement with computationally efficient feedback. ProteinZero employs a reward pipeline that combines structural guidance from ESMFold with a novel self-derived ddG predictor, providing stable multi-objective signals while avoiding the prohibitive cost of physics-based methods. To ensure robustness in online RL, we further introduce a novel embedding-level diversity regularizer that mitigates mode collapse and promotes functionally meaningful sequence variation. Within a general RL formulation balancing multi-reward optimization, KL-divergence from a reference model, and diversity regularization, ProteinZero achieves robust improvements across designability, stability, recovery, and diversity. On the CATH-4.3 benchmark, it consistently outperforms state-of-the-art baselines including ProteinMPNN, ESM-IF, and InstructPLM, reducing design failure rates by 36-48% and achieving success rates above 90% across diverse folds. Importantly, a complete RL run can be executed on a single 8 X GPU node within three days, including reward computation and data generation. These results indicate that efficient online RL fine-tuning can complement supervised pretraining by allowing protein generative models to evolve continuously from their own outputs and optimize multiple design objectives without labeled data, opening new possibilities for exploring the vast protein design space. Full source code and model checkpoints will be released upon publication.

</details>

---

### 95. [InstructPro: Natural Language Guided Ligand-Binding Protein Design](https://arxiv.org/abs/2506.09332)

**基本信息**

- 🔗 arXiv: [`2506.09332`](https://arxiv.org/abs/2506.09332)
- 👥 作者: Zhenqiao Song, Ramith Hettiarachchi, Chuan Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.09332.pdf)

**💡 相关性分析**

满足标准1 & 2：论文的核心是提出自然语言指导的蛋白质设计大模型，直接相关于化学大模型主题，并提供了大规模数据集和模型（资源）。

**📖 中文摘要**

论文提出了InstructPro，一个通过自然语言指令和配体分子式来设计蛋白质的生成模型家族。为了训练和评估，论文构建了InstructProBench，一个包含960万个（功能描述、配体、蛋白质）三元组的大规模数据集。模型在结合亲和力、新颖性等指标上表现出色。这项工作开创性地利用自然语言指导蛋白质设计，是化学大模型与自然语言处理交叉的典范。其提出的模型框架和发布的大规模数据集，为基于语言的分子设计研究提供了核心资源和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The de novo design of ligand-binding proteins with tailored functions is essential for advancing biotechnology and molecular medicine, yet existing AI approaches are limited by scarce protein-ligand complex data. To circumvent this data bottleneck, we leverage the abundant natural language descriptions characterizing protein-ligand interactions. Here, we introduce InstructPro, a family of generative models that design proteins following the guidance of natural language instructions and ligand formulas. InstructPro produces protein sequences consistent with specified function descriptions and ligand targets. To enable training and evaluation, we develop InstructProBench, a large-scale dataset of 9.6 million (function description, ligand, protein) triples. We train two model variants -- InstructPro-1B and InstructPro-3B -- that substantially outperform strong baselines. InstructPro-1B achieves an AlphaFold3 ipTM of 0.918 and a binding affinity of -8.764 on seen ligands, while maintaining robust performance in a zero-shot setting with scores of 0.869 and -6.713, respectively. These results are accompanied by novelty scores of 70.1% and 68.8%, underscoring the model's ability to generalize beyond the training set. Furthermore, the model yields a superior binding free energy of -20.9 kcal/mol and an average of 5.82 intermolecular hydrogen bonds, validating its proficiency in designing high-affinity ligand-binding proteins. Notably, scaling to InstructPro-3B further improves the zero-shot ipTM to 0.882, binding affinity to -6.797, and binding free energy to -25.8 kcal/mol, demonstrating clear performance gains associated with increased model capacity. These findings highlight the power of natural language-guided generative models to mitigate the data bottlenecks in traditional structure-based methods, significantly broadening the scope of de novo protein design.

</details>

---

### 96. [Behavioral Generative Agents for Energy Operations](https://arxiv.org/abs/2506.12664)

**基本信息**

- 🔗 arXiv: [`2506.12664`](https://arxiv.org/abs/2506.12664)
- 👥 作者: Cong Chen, Omer Karaduman, Xu Kuang
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.12664.pdf)

**💡 相关性分析**

满足标准3：论文关于使用生成式智能体模拟人类决策行为的研究，为化学领域构建用于实验设计或行为模拟的AI智能体提供了重要的相关讨论和展望。

**📖 中文摘要**

论文研究了生成式智能体（由大语言模型驱动）在能源运营中模拟客户行为的应用。虽然领域是能源，但其方法论——使用LLM驱动的智能体来模拟复杂决策行为，以发现行为模式并补充传统数学模型——为在化学领域构建类似的行为模拟或实验设计智能体提供了概念框架和方法论参考。例如，可用于模拟化学家在实验设计或材料选择中的决策过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Problem definition: Accurately modeling consumer behavior in energy operations is challenging due to uncertainty, behavioral heterogeneity, and limited empirical data-particularly in low-frequency, high-impact events. While generative AI trained on large-scale human data offers new opportunities to study decision behavior, its role in operational applications remains unclear. We examine how generative agents can support customer behavior discovery in energy operations, complementing rather than replacing human-based experiments. Methodology/results: We introduce a novel approach leveraging generative agents-artificial agents powered by large language models-to simulate sequential customer decisions under dynamic electricity prices and outage risks. We find that these agents behave more optimally and rationally in simpler market scenarios, while their performance becomes more variable and suboptimal as task complexity rises. Furthermore, the agents exhibit heterogeneous customer preferences, consistently maintaining distinct, persona-driven reasoning patterns in both operational decisions and textual reasoning. Comparisons with dynamic programming and greedy policy benchmarks show alignment between specific personas and distinct heuristic decision policies. In low-frequency, high-impact events such as blackouts, agents prioritize energy reliability over cost or profit, demonstrating their ability to uncover behavioral patterns beyond the rigidity of traditional mathematical models. Managerial Implications: Our findings suggest that behavioral generative agents can serve as scalable and flexible tools for studying consumer behavior in energy operations. By enabling controlled experiments across heterogeneous customer types and rare events, these agents can enhance the design of energy management systems and support more informed analysis of energy policies and incentive programs.

</details>

---

### 97. [Language Agents for Hypothesis-driven Clinical Decision Making with Reinforcement Learning](https://arxiv.org/abs/2506.13474)

**基本信息**

- 🔗 arXiv: [`2506.13474`](https://arxiv.org/abs/2506.13474)
- 👥 作者: David Bani-Harouni, Chantal Pellegrini, Ege Özsoy 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.13474.pdf)

**💡 相关性分析**

满足标准1：论文提出的假设驱动、交互式决策智能体框架，其核心方法论与质谱结构推理中迭代假设生成与验证的过程直接相关。

**📖 中文摘要**

论文提出了LA-CDM，一个用于临床诊断决策的假设驱动、不确定性感知的语言智能体。该智能体通过反复请求和解释相关测试来逐步收敛到诊断。虽然应用于医疗领域，但其核心框架——将决策建模为基于假设的、交互式的、循环的信息收集与推理过程——与质谱结构推理中“提出假设-获取谱图-验证/修正假设”的迭代分析流程在方法论上高度相似。该工作为构建用于质谱数据解析的交互式、假设驱动的AI助手提供了直接的设计思路和算法参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Clinical decision-making is a dynamic, interactive, and cyclic process where doctors have to repeatedly decide on which clinical action to perform and consider newly uncovered information for diagnosis and treatment. Large Language Models (LLMs) have the potential to support clinicians in this process, however, most applications of LLMs in clinical decision support suffer from one of two limitations: Either they assume the unrealistic scenario of immediate availability of all patient information and do not model the interactive and iterative investigation process, or they restrict themselves to the limited "out-of-the-box" capabilities of large pre-trained models without performing task-specific training. In contrast to this, we propose to model clinical decision-making for diagnosis with a hypothesis-driven uncertainty-aware language agent, LA-CDM, that converges towards a diagnosis via repeatedly requesting and interpreting relevant tests. Using a hybrid training paradigm combining supervised and reinforcement learning, we train LA-CDM with three objectives targeting critical aspects of clinical decision-making: accurate hypothesis generation, hypothesis uncertainty estimation, and efficient decision-making. We evaluate our methodology on MIMIC-CDM, a real-world dataset covering four abdominal diseases containing various clinical tests and show the benefit of explicitly training clinical decision-making for increasing diagnostic performance and efficiency.

</details>

---

### 98. [TRIDENT: Tri-Modal Molecular Representation Learning with Taxonomic Annotations and Local Correspondence](https://arxiv.org/abs/2506.21028)

**基本信息**

- 🔗 arXiv: [`2506.21028`](https://arxiv.org/abs/2506.21028)
- 👥 作者: Feng Jiang, Mangal Prakash, Hehuan Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.21028.pdf)

**💡 相关性分析**

满足标准1 & 2：论文的核心是多模态分子表示学习，直接围绕化学大模型主题，并提供了新颖的框架、对齐方法和数据集（资源）。

**📖 中文摘要**

论文提出了TRIDENT，一个整合分子SMILES、文本描述和分类学功能注释的三模态分子表示学习框架。论文构建了包含结构化、多层次功能注释的分子-文本对数据集，并提出了全局和局部对齐目标。该工作在11个下游任务上取得了最先进的性能。这项工作直接位于化学大模型与多模态学习的交叉点，其提出的三模态融合框架、新的对齐目标以及构建的数据集，为开发更强大的化学领域多模态大模型提供了重要的方法、资源和基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular property prediction aims to learn representations that map chemical structures to functional properties. While multimodal learning has emerged as a powerful paradigm to learn molecular representations, prior works have largely overlooked textual and taxonomic information of molecules for representation learning. We introduce TRIDENT, a novel framework that integrates molecular SMILES, textual descriptions, and taxonomic functional annotations to learn rich molecular representations. To achieve this, we curate a comprehensive dataset of molecule-text pairs with structured, multi-level functional annotations. Instead of relying on conventional contrastive loss, TRIDENT employs a volume-based alignment objective to jointly align tri-modal features at the global level, enabling soft, geometry-aware alignment across modalities. Additionally, TRIDENT introduces a novel local alignment objective that captures detailed relationships between molecular substructures and their corresponding sub-textual descriptions. A momentum-based mechanism dynamically balances global and local alignment, enabling the model to learn both broad functional semantics and fine-grained structure-function mappings. TRIDENT achieves state-of-the-art performance on 11 downstream tasks, demonstrating the value of combining SMILES, textual, and taxonomic functional annotations for molecular property prediction.

</details>

---

### 99. [Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design](https://arxiv.org/abs/2507.00445)

**基本信息**

- 🔗 arXiv: [`2507.00445`](https://arxiv.org/abs/2507.00445)
- 👥 作者: Xingyu Su, Xiner Li, Masatoshi Uehara 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.00445.pdf)

**💡 相关性分析**

满足标准1 & 2：论文的核心是提出一种用于奖励引导生物分子生成的扩散模型微调框架，直接相关于化学大模型中的优化生成主题，并提供了新的方法资源。

**📖 中文摘要**

论文提出了一个基于迭代蒸馏的扩散模型微调框架，用于生物分子设计中的奖励引导生成。该方法将问题转化为策略蒸馏，使用离线策略数据和KL散度最小化，以提高训练稳定性和样本效率。论文在蛋白质、小分子和调控DNA设计等多种任务上验证了其有效性。这项工作直接针对化学和生物分子生成模型的优化问题，提出了一种稳定高效的RL替代方案。其框架适用于任何需要基于（不可微）奖励优化扩散模型的场景，为质谱引导的分子生成或性质优化的分子设计提供了重要的方法工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We address the problem of fine-tuning diffusion models for reward-guided generation in biomolecular design. While diffusion models have proven highly effective in modeling complex, high-dimensional data distributions, real-world applications often demand more than high-fidelity generation, requiring optimization with respect to potentially non-differentiable reward functions such as physics-based simulation or rewards based on scientific knowledge. Although RL methods have been explored to fine-tune diffusion models for such objectives, they often suffer from instability, low sample efficiency, and mode collapse due to their on-policy nature. In this work, we propose an iterative distillation-based fine-tuning framework that enables diffusion models to optimize for arbitrary reward functions. Our method casts the problem as policy distillation: it collects off-policy data during the roll-in phase, simulates reward-based soft-optimal policies during roll-out, and updates the model by minimizing the KL divergence between the simulated soft-optimal policy and the current model policy. Our off-policy formulation, combined with KL divergence minimization, enhances training stability and sample efficiency compared to existing RL-based methods. Empirical results demonstrate the effectiveness and superior reward optimization of our approach across diverse tasks in protein, small molecule, and regulatory DNA design. The source code is released at ( this https URL ).

</details>

---

### 100. [A Genetic Algorithm for Navigating Synthesizable Molecular Spaces](https://arxiv.org/abs/2509.20719)

**基本信息**

- 🔗 arXiv: [`2509.20719`](https://arxiv.org/abs/2509.20719)
- 👥 作者: Alston Lo, Connor W. Coley, Wojciech Matusik
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.20719.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕在化学信息学领域（分子设计）使用算法（遗传算法）探索和优化分子空间，这与“化学大模型”主题中关于分子生成、设计和优化的研究方向直接相关。

**📖 中文摘要**

本文提出了一种名为SynGA的遗传算法，用于在可合成的分子空间中导航。该算法直接在合成路线上进行操作，通过定制的交叉和变异算子，将其约束在可合成的分子空间内。通过修改适应度函数，SynGA在多种设计任务（包括可合成的类似物搜索和样本高效的属性优化）中展现出有效性。此外，通过与基于机器学习的构建块过滤器耦合，SynGA达到了最先进的性能。对于属性优化，该方法演变为一个基于模型的变体SynGBO，它在贝叶斯优化的内循环中采用SynGA和块过滤。由于SynGA是轻量级的，并且通过构造强制执行可合成性，因此它不仅可作为强大的独立基线，也可作为未来可集成到更大合成感知工作流程中的通用模块。这项工作与化学信息学中的分子设计（化学大模型的应用领域）以及质谱分析中可能涉及的分子结构生成与优化高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inspired by the effectiveness of genetic algorithms and the importance of synthesizability in molecular design, we present SynGA, a simple genetic algorithm that operates directly over synthesis routes. Our method features custom crossover and mutation operators that explicitly constrain it to synthesizable molecular space. By modifying the fitness function, we demonstrate the effectiveness of SynGA on a variety of design tasks, including synthesizable analog search and sample-efficient property optimization, for both 2D and 3D objectives. Furthermore, by coupling SynGA with a machine learning-based filter that focuses the building block set, we boost SynGA to state-of-the-art performance. For property optimization, this manifests as a model-based variant SynGBO, which employs SynGA and block filtering in the inner loop of Bayesian optimization. Since SynGA is lightweight and enforces synthesizability by construction, our hope is that SynGA can not only serve as a strong standalone baseline but also as a versatile module that can be incorporated into larger synthesis-aware workflows in the future.

</details>

---

### 101. [G-reasoner: Foundation Models for Unified Reasoning over Graph-structured Knowledge](https://arxiv.org/abs/2509.24276)

**基本信息**

- 🔗 arXiv: [`2509.24276`](https://arxiv.org/abs/2509.24276)
- 👥 作者: Linhao Luo, Zicheng Zhao, Junnan Liu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24276.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于在图结构知识上进行推理的统一基础模型框架（G-reasoner）。图结构推理是“化学大模型”和“质谱结构推理”领域的核心方法之一（例如，分子通常被表示为图，质谱解析也常涉及结构关系的推理）。

**📖 中文摘要**

本文提出了G-reasoner，一个用于在图结构知识上进行统一推理的基础模型框架。大型语言模型（LLMs）在复杂推理方面表现出色，但受限于静态和不完整的参数化知识。检索增强生成（RAG）通过整合外部知识来缓解这一问题，但现有的RAG在处理知识密集型任务时，由于信息碎片化和对知识结构建模能力弱而存在困难。图是建模知识内部关系的自然方式，但LLMs本质上是非结构化的，无法有效地对图结构数据进行推理。G-reasoner通过一个标准化的四层抽象（QuadGraph）将异构知识源统一为通用图表示，并引入一个3400万参数的图基础模型（GFM）来共同捕获图拓扑和文本语义，该模型与LLMs集成以增强下游应用中的推理能力。在六个基准测试上的广泛实验表明，G-reasoner始终优于最先进的基线，显著增强了LLM的推理能力，并实现了强大的效率和跨图泛化能力。该框架为在图结构知识上进行推理提供了通用解决方案，与化学信息学中利用图神经网络处理分子图、以及质谱分析中可能涉及的结构推理任务在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) excel at complex reasoning but remain limited by static and incomplete parametric knowledge. Retrieval-augmented generation (RAG) mitigates this by incorporating external knowledge, yet existing RAGs struggle with knowledge-intensive tasks due to fragmented information and weak modeling of knowledge structure. Graphs offer a natural way to model relationships within knowledge, but LLMs are inherently unstructured and cannot effectively reason over graph-structured data. Recent graph-enhanced RAG (GraphRAG) attempts to bridge this gap by constructing tailored graphs and enabling LLMs to reason on them. However, these methods often depend on ad-hoc graph designs, heuristic search, or costly agent pipelines, which hinder scalability and generalization. To address these challenges, we present G-reasoner, a unified framework that integrates graph and language foundation models for scalable reasoning over diverse graph-structured knowledge. Central to our approach is QuadGraph, a standardized four-layer abstraction that unifies heterogeneous knowledge sources into a common graph representation. Building on this, we introduce a 34M-parameter graph foundation model (GFM) that jointly captures graph topology and textual semantics, and is integrated with LLMs to enhance reasoning in downstream applications. To ensure scalability and efficiency, mixed-precision training and distributed message-passing are implemented to scale GFM with more GPUs. Extensive experiments on six benchmarks show that G-reasoner consistently outperforms state-of-the-art baselines, significantly enhances LLM reasoning, and achieves strong efficiency and cross-graph generalization.

</details>

---

### 102. [Is It Thinking or Cheating? Detecting Implicit Reward Hacking by Measuring Reasoning Effort](https://arxiv.org/abs/2510.01367)

**基本信息**

- 🔗 arXiv: [`2510.01367`](https://arxiv.org/abs/2510.01367)
- 👥 作者: Xinpeng Wang, Nitish Joshi, Barbara Plank 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01367.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和检测大型推理模型（LRMs）在推理过程中的缺陷（奖励黑客）。这直接关系到如何构建和评估可靠的“化学大模型”和用于“质谱结构推理”的模型，确保其推理过程是可信和有效的。

**📖 中文摘要**

本文研究了大型推理模型（LRMs）中的奖励黑客问题，即模型利用奖励函数中的漏洞获得高奖励，而非真正解决预期任务。作者提出了一种名为TRACE（截断推理AUC评估）的新方法来检测隐式的奖励黑客行为。其核心观察是，当利用漏洞比解决实际任务更容易时，就会发生黑客行为，这意味着模型使用了比所需更少的“努力”来获得高奖励。TRACE通过逐步截断模型的思维链（CoT），迫使模型在多个截断点回答，并估计每个截断点的预期奖励，从而量化推理努力。黑客模型只需其思维链的一小部分即可获得高预期奖励，从而在准确率-长度曲线下产生较大的面积。该方法在数学推理和编码任务上显著优于现有的思维链监控方法，并能发现训练过程中未知的漏洞。这项工作专注于分析和改进大型模型的推理过程，与“化学大模型”和“质谱结构推理”中模型的可信度、鲁棒性以及推理过程的可靠性评估密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reward hacking, where a reasoning model exploits loopholes in a reward function to achieve high rewards without solving the intended task, poses a significant threat. This behavior may be explicit, i.e. verbalized in the model's chain-of-thought (CoT), or implicit, where the CoT appears benign thus bypasses CoT monitors. To detect implicit reward hacking, we propose TRACE (Truncated Reasoning AUC Evaluation). Our key observation is that hacking occurs when exploiting the loophole is easier than solving the actual task. This means that the model is using less 'effort' than required to achieve high reward. TRACE quantifies effort by measuring how early a model's reasoning becomes sufficient to obtain the reward. We progressively truncate a model's CoT at various lengths, force the model to answer, and estimate the expected reward at each cutoff. A hacking model, which takes a shortcut, will achieve a high expected reward with only a small fraction of its CoT, yielding a large area under the accuracy-vs-length curve. TRACE achieves over 65% gains over our strongest 72B CoT monitor in math reasoning, and over 30% gains over a 32B monitor in coding. We further show that TRACE can discover unknown loopholes during training. Overall, TRACE offers a scalable unsupervised approach for oversight where current monitoring methods prove ineffective.

</details>

---

### 103. [TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA](https://arxiv.org/abs/2510.04682)

**基本信息**

- 🔗 arXiv: [`2510.04682`](https://arxiv.org/abs/2510.04682)
- 👥 作者: Chanjoo Jung, Jaehyung Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04682.pdf)

**💡 相关性分析**

满足标准1：论文提出的TiTok框架核心是进行“token级知识转移”，这是一种模型表示层面的信息提取与迁移技术。虽然论文以大语言模型为应用背景，但该方法论与化学信息学中利用深度学习模型进行分子表示学习、特征提取或跨任务知识迁移（例如，将预训练于大量化合物数据的模型知识迁移到特定的质谱结构推理任务）的研究主题在技术路径上直接相关。

**📖 中文摘要**

本文提出了一种名为TiTok的新框架，旨在实现LoRA（Low-Rank Adaptation）参数在不同骨干模型间的有效迁移。核心思想是通过对比源模型在应用LoRA前后的token级信息差异（即“对比过剩”），来捕获任务相关的知识，并以此筛选合成数据，从而实现无需额外模型开销的LoRA移植。该方法在多个基准测试和迁移设置中均表现出稳定的有效性，平均性能提升达4%~10%。虽然论文主要关注大语言模型（LLM）的参数高效微调，但其提出的“token级知识转移”和“对比过剩”概念，本质上是一种针对模型内部表示（尤其是化学结构或质谱数据可能被编码的表示空间）进行信息提取和迁移的方法论。这种从模型表示中提取和转移任务相关知识的技术思路，与化学信息学中利用预训练模型进行分子表示学习、或从质谱数据中推理结构时所需的特征提取与迁移任务，在方法论层面高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are widely applied in real world scenarios, yet fine-tuning them comes with significant computational and storage costs. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA mitigate these costs; however, the adapted parameters are dependent on the base model and cannot be transferred across different backbones. One way to address this issue is through knowledge distillation, but its effectiveness inherently depends on training data. Recent work such as TransLoRA avoids this by generating synthetic data; nevertheless, this adds complexity since it requires training an additional discriminator model. In this paper, we propose TiTok, a new framework that enables effective LoRA Transplantation through Token-level knowledge transfer. Specifically, TiTok captures task-relevant information through a token-wise contrastive excess between a source model with and without LoRA. This excess highlights informative tokens and enables selective filtering of synthetic data, all without additional models or overhead. Through experiments on three benchmarks across multiple transfer settings, we demonstrate that TiTok is consistently effective, achieving average performance gains of +4~10% compared to baselines overall.

</details>

---

### 104. [SwiReasoning: Switch-Thinking in Latent and Explicit for Pareto-Superior Reasoning LLMs](https://arxiv.org/abs/2510.05069)

**基本信息**

- 🔗 arXiv: [`2510.05069`](https://arxiv.org/abs/2510.05069)
- 👥 作者: Dachuan Shi, Abedelkadir Asi, Keying Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.05069.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型的复杂推理能力，特别是通过设计动态切换显式与隐式推理的机制来优化推理过程。这直接对应于“化学大模型”主题下关于如何让大模型进行高效、准确科学推理（如化学结构解析、性质预测）的关键技术挑战。

**📖 中文摘要**

本文提出了SwiReasoning框架，旨在通过动态切换显式推理（如思维链）和隐式推理（在潜在空间中进行），来提升大语言模型（LLM）的推理效率与准确性。框架的核心创新在于利用下一个token分布的熵趋势来估计块级置信度，从而引导模型在探索（隐式推理）和利用（显式推理）之间取得平衡，并及时收敛以避免过度思考。在数学、STEM、编码等基准测试上，SwiReasoning能持续提升不同规模和家族LLM的平均准确率（1.8%-3.1%），并在预算受限时大幅提升token效率（57%-79%）。论文聚焦于提升LLM的复杂推理能力，其核心贡献——即设计一种机制来管理和优化模型在“显式”与“隐式”表示空间中的推理过程——与“化学大模型”领域关注的核心挑战之一高度吻合：如何让大模型更高效、更准确地进行复杂的科学推理（如化学反应预测、分子性质推理、质谱解析等）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent work shows that, beyond discrete reasoning through explicit chain-of-thought steps, which are limited by the boundaries of natural languages, large language models (LLMs) can also reason continuously in latent space, allowing richer information per step and thereby improving token efficiency. Despite this promise, latent reasoning still faces two challenges, especially in training-free settings: 1) purely latent reasoning broadens the search distribution by maintaining multiple implicit paths, which diffuses probability mass, introduces noise, and impedes convergence to a single high-confidence solution, thereby hurting accuracy; and 2) overthinking persists even without explicit text, wasting tokens and degrading efficiency. To address these issues, we introduce SwiReasoning, a training-free framework for LLM reasoning which features two key innovations: 1) SwiReasoning dynamically switches between explicit and latent reasoning, guided by block-wise confidence estimated from entropy trends in next-token distributions, to balance exploration and exploitation and promote timely convergence. 2) By limiting the maximum number of thinking-block switches, SwiReasoning curbs overthinking and improves token efficiency across varying problem difficulties. On widely used mathematics, STEM, coding, and general benchmarks, SwiReasoning consistently improves average accuracy by 1.8%-3.1% across reasoning LLMs of different model families and scales. Furthermore, under constrained budgets, SwiReasoning improves average token efficiency by 57%-79%, with larger gains as budgets tighten.

</details>

---

### 105. [MASA: Rethinking the Representational Bottleneck in LoRA with Multi-A Shared Adaptation](https://arxiv.org/abs/2510.06005)

**基本信息**

- 🔗 arXiv: [`2510.06005`](https://arxiv.org/abs/2510.06005)
- 👥 作者: Qin Dong, Yuntian Tang, Heming Jia 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.06005.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大语言模型的高效微调架构（LoRA），旨在通过增强特征适应能力来提升下游任务性能。这直接对应于“化学大模型”主题中关于如何有效微调大型化学模型以适应特定科学任务（如质谱解析）的技术路径。

**📖 中文摘要**

本文针对广泛使用的参数高效微调方法LoRA（Low-Rank Adaptation）提出了改进架构MASA（Multi-A Shared Adaptation）。作者指出，标准LoRA中单一的下投影矩阵A构成了表示瓶颈，难以捕获复杂任务所需的多样化信号。MASA采用“多A专家、单B集成”的非对称共享结构，其中多个专家负责捕获多样化特征，然后由层特定的B矩阵进行整合。这种设计旨在丰富特征适应能力，从而提升下游任务适应性能。在MMLU等基准测试上的实验表明，MASA能以可比的参数量（0.52%）超越标准LoRA。论文的核心是改进大模型（尤其是Transformer架构）的适配器微调技术，以更好地捕获和迁移任务相关知识。这项工作与“化学大模型”主题密切相关，因为化学领域的大模型（如用于分子性质预测、反应生成的模型）同样面临如何通过高效微调使其适应特定下游任务（如质谱结构推理）的挑战。MASA所针对的“表示瓶颈”和“特征多样化”问题，正是化学大模型微调中需要解决的关键问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Low-Rank Adaptation (LoRA) has emerged as a dominant method in Parameter-Efficient Fine-Tuning (PEFT) for large language models, which augments the transformer layer with one down-projection $A$ and one up-projection $B$. However, LoRA's reliance on a single down-projection matrix ($A$) creates a representational bottleneck, as this solitary feature extractor is inherently insufficient for capturing the diverse signals required by complex tasks. This motivates our architectural shift to focus on enriching the feature adaptation to improve the downstream task adaptation ability. We propose MASA (Multi-$A$ Shared Adaptation), an architecture that implements a multi-$A$, single-$B$ structure where the multi-$A$ expert ensemble is asymmetrically shared across layers to ensure parameter efficiency. In MASA, these specialized experts capture diverse features, which are then integrated by a single, layer-specific $B$-matrix. The effectiveness and versatility of our method are validated through a comprehensive suite of experiments spanning multi-domain generalization, single-domain specialization, and multi-task reasoning. For example, on the MMLU benchmark, MASA achieves an average accuracy of 59.62%, outperforming the standard LoRA by 1.08 points (a relative improvement of 1.84%) with comparable learnable parameters of 0.52%.

</details>

---

### 106. [Latent Diffusion Model without Variational Autoencoder](https://arxiv.org/abs/2510.15301)

**基本信息**

- 🔗 arXiv: [`2510.15301`](https://arxiv.org/abs/2510.15301)
- 👥 作者: Minglei Shi, Haolin Wang, Wenzhao Zheng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.15301.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索如何构建具有强语义判别性的潜在表示空间，并基于此训练扩散模型。这种方法论与“化学大模型”和“质谱结构推理”主题直接相关，因为化学领域同样迫切需要能够同时支持判别（如性质预测）和生成（如结构推断）任务的高质量数据表示学习技术。

**📖 中文摘要**

本文提出了一种无需变分自编码器（VAE）的潜在扩散模型SVG。作者指出，当前主流的VAE+扩散范式在训练效率、推理速度和向更广泛视觉任务的可迁移性方面存在局限，其根本原因在于VAE潜在空间缺乏清晰的语义分离和强判别性结构。SVG利用自监督表示（如冻结的DINO特征）构建具有明确语义判别性的特征空间，并在此结构化潜在空间上直接训练扩散模型。该方法实现了更高效的扩散训练、支持少步采样，并提升了生成质量。实验表明，SVG保留了底层自监督表示的语义和判别能力。这项工作的核心是探索如何构建更优的潜在表示空间以服务于生成模型。虽然应用于图像生成，但其核心思想——利用具有强语义判别性的（自监督）表示作为扩散模型的潜在空间——与“化学大模型”和“质谱结构推理”主题高度相关。在化学信息学中，分子或质谱数据的良好表示（如通过图神经网络或Transformer学习的嵌入）是进行生成（如分子设计）或推理（如从质谱推断结构）的基础。本文的方法论为如何在化学领域构建兼具判别性和生成能力的统一表示空间提供了重要的技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent progress in diffusion-based visual generation has largely relied on latent diffusion models with variational autoencoders (VAEs). While effective for high-fidelity synthesis, this VAE+diffusion paradigm suffers from limited training efficiency, slow inference, and poor transferability to broader vision tasks. These issues stem from a key limitation of VAE latent spaces: the lack of clear semantic separation and strong discriminative structure. Our analysis confirms that these properties are crucial not only for perception and understanding tasks, but also for the stable and efficient training of latent diffusion models. Motivated by this insight, we introduce SVG, a novel latent diffusion model without variational autoencoders, which leverages self-supervised representations for visual generation. SVG constructs a feature space with clear semantic discriminability by leveraging frozen DINO features, while a lightweight residual branch captures fine-grained details for high-fidelity reconstruction. Diffusion models are trained directly on this semantically structured latent space to facilitate more efficient learning. As a result, SVG enables accelerated diffusion training, supports few-step sampling, and improves generative quality. Experimental results further show that SVG preserves the semantic and discriminative capabilities of the underlying self-supervised representations, providing a principled pathway toward task-general, high-quality visual representations. Code and interpretations are available at this https URL .

</details>

---

### 107. [Learning Boltzmann Generators via Constrained Mass Transport](https://arxiv.org/abs/2510.18460)

**基本信息**

- 🔗 arXiv: [`2510.18460`](https://arxiv.org/abs/2510.18460)
- 👥 作者: Christopher von Klitzing, Denis Blessing, Henrik Schopmans 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.18460.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于分子系统玻尔兹曼分布采样的改进生成模型算法（约束质量传输）。这直接对应于“化学大模型”主题中关于利用生成模型探索化学空间、进行分子生成与采样的研究方向，也与“质谱结构推理”中可能涉及的基于生成模型的分子结构逆向推导相关。

**📖 中文摘要**

本文针对从高维、多模态的未归一化概率分布（如物理系统的玻尔兹曼分布）中高效采样这一核心挑战，提出了约束质量传输（CMT）框架。CMT旨在改进玻尔兹曼生成器（BGs）的训练，通过在对连续步骤之间的KL散度和熵衰减施加约束，来增强分布重叠、减轻质量传输问题并防止过早收敛。在包括新引入的ELIL四肽（迄今为止在没有分子动力学样本的情况下研究的最大系统）在内的标准BG基准测试中，CMT consistently超越了最先进的变分方法，实现了超过2.5倍的有效样本量提升，同时避免了模式崩溃。这项工作专注于为物理系统（特别是分子系统）开发改进的生成模型采样算法。其研究内容直接对应于“化学大模型”主题下的一个关键子方向：如何利用生成模型（如扩散模型、玻尔兹曼生成器）来高效采样化学空间（如分子构象、化学反应路径），这对于分子设计、性质预测以及从质谱等数据中逆向推理结构至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Efficient sampling from high-dimensional and multimodal unnormalized probability distributions is a central challenge in many areas of science and machine learning. We focus on Boltzmann generators (BGs) that aim to sample the Boltzmann distribution of physical systems, such as molecules, at a given temperature. Classical variational approaches that minimize the reverse Kullback-Leibler divergence are prone to mode collapse, while annealing-based methods, commonly using geometric schedules, can suffer from mass teleportation and rely heavily on schedule tuning. We introduce Constrained Mass Transport (CMT), a variational framework that generates intermediate distributions under constraints on both the KL divergence and the entropy decay between successive steps. These constraints enhance distributional overlap, mitigate mass teleportation, and counteract premature convergence. Across standard BG benchmarks and the here introduced ELIL tetrapeptide, the largest system studied to date without access to samples from molecular dynamics, CMT consistently surpasses state-of-the-art variational methods, achieving more than 2.5x higher effective sample size while avoiding mode collapse.

</details>

---

### 108. [Loopholing Discrete Diffusion: Deterministic Bypass of the Sampling Wall](https://arxiv.org/abs/2510.19304)

**基本信息**

- 🔗 arXiv: [`2510.19304`](https://arxiv.org/abs/2510.19304)
- 👥 作者: Mingyu Jo, Jaesik Yoon, Justin Deschenaux 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.19304.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进离散扩散模型这一生成模型范式，以提升其生成和推理能力。离散扩散模型在化学信息学中可用于分子序列生成、性质优化等任务，其性能提升技术（如解决“采样墙”）与“化学大模型”主题下的生成式模型应用直接相关。

**📖 中文摘要**

本文针对离散扩散模型在文本生成中存在的“采样墙”问题（即一旦进行类别采样，丰富的分布信息就会坍缩为one-hot向量，无法跨步骤传播），提出了Loopholing机制和Loopholing离散扩散模型（LDDM）。Loopholing通过一个确定性的潜在路径来保留分布信息，从而让后续步骤能够在更丰富的信息基础上操作。该方法通过自条件策略高效训练，显著降低了生成困惑度（最高达61%），缩小了与非自回归模型的差距，并生成了更连贯的文本。在推理任务（如算术）上也表现出性能提升。论文的核心是改进离散扩散模型这一重要的生成模型范式，以提升其文本生成和推理能力。虽然应用领域是通用文本，但离散扩散模型作为一种强大的生成模型，其在化学信息学中有直接的应用潜力，例如用于分子图序列（如SMILES）的生成、分子性质优化、或者质谱碎片序列的生成与解析。本文提出的解决“采样墙”的技术，对于提升这类化学序列生成模型的性能和质量具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete diffusion models offer a promising alternative to autoregressive generation through parallel decoding, but they suffer from a sampling wall: once categorical sampling occurs, rich distributional information collapses into one-hot vectors and cannot be propagated across steps, forcing subsequent steps to operate with limited information. To mitigate this problem, we introduce Loopholing, a novel and simple mechanism that preserves this information via a deterministic latent pathway, leading to Loopholing Discrete Diffusion Models (LDDMs). Trained efficiently with a self-conditioning strategy that avoids unrolling the full denoising trajectory, LDDMs achieve substantial gains-reducing generative perplexity by up to 61% over prior baselines, thereby closing (and in some cases surpassing) the gap with autoregressive models, and producing more coherent text. Applied to reasoning tasks, LDDMs also improve performance on arithmetic benchmarks such as Countdown and Game of 24. These results also indicate that loopholing mitigates idle steps and oscillations, providing a general and effective path toward high-quality non-autoregressive text generation.

</details>

---

### 109. [Clustering by Denoising: Latent plug-and-play diffusion for single-cell data](https://arxiv.org/abs/2510.22835)

**基本信息**

- 🔗 arXiv: [`2510.22835`](https://arxiv.org/abs/2510.22835)
- 👥 作者: Dominik Meier, Shixing Yu, Sagnik Nandy 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22835.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的深度生成方法，用于对复杂、高噪声的生物数据进行去噪和表示学习以改善聚类。该方法论与“质谱结构推理”主题直接相关，因为质谱数据解析同样面临从噪声数据中提取稳健特征以推断化学结构的挑战，本文的技术路径提供了重要的参考。

**📖 中文摘要**

本文针对单细胞RNA测序（scRNA-seq）数据聚类中因测量噪声和生物变异性导致的挑战，提出了一种潜在即插即用扩散框架。该框架将观测空间和去噪空间分离，通过一种新颖的吉布斯采样过程实现：在低维潜在空间中应用学习的扩散先验进行去噪，同时为了引导此过程，将噪声重新引入原始高维观测空间。这种“输入空间引导”确保了去噪轨迹忠实于原始数据结构。该方法具有自适应噪声处理、不确定性量化和可泛化去噪等优势。在合成和真实单细胞基因组学数据上的评估表明，该方法提高了聚类准确性，并产生了更具生物学一致性的细胞簇。论文的核心是开发一种基于扩散模型的深度生成方法，用于对高维、稀疏、有噪声的生物数据进行去噪和表示学习，以改善下游分析（如聚类）。虽然应用场景是生物信息学中的单细胞数据，但其核心技术——即利用扩散模型在分离的潜在空间中进行数据去噪与表示增强——与“质谱结构推理”主题面临的核心问题高度相似：质谱数据同样具有高维、噪声大、信号复杂的特点，需要先进的去噪和特征提取方法来推断底层化学结构。本文的方法论为处理此类复杂科学数据提供了新的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell RNA sequencing (scRNA-seq) enables the study of cellular heterogeneity. Yet, clustering accuracy, and with it downstream analyses based on cell labels, remain challenging due to measurement noise and biological variability. In standard latent spaces (e.g., obtained through PCA), data from different cell types can be projected close together, making accurate clustering difficult. We introduce a latent plug-and-play diffusion framework that separates the observation and denoising space. This separation is operationalized through a novel Gibbs sampling procedure: the learned diffusion prior is applied in a low-dimensional latent space to perform denoising, while to steer this process, noise is reintroduced into the original high-dimensional observation space. This unique "input-space steering" ensures the denoising trajectory remains faithful to the original data structure. Our approach offers three key advantages: (1) adaptive noise handling via a tunable balance between prior and observed data; (2) uncertainty quantification through principled uncertainty estimates for downstream analysis; and (3) generalizable denoising by leveraging clean reference data to denoise noisier datasets, and via averaging, improve quality beyond the training set. We evaluate robustness on both synthetic and real single-cell genomics data. Our method improves clustering accuracy on synthetic data across varied noise levels and dataset shifts. On real-world single-cell data, our method demonstrates improved biological coherence in the resulting cell clusters, with cluster boundaries that better align with known cell type markers and developmental trajectories.

</details>

---

### 110. [Data-Augmented Deep Learning for Downhole Depth Sensing and Validation](https://arxiv.org/abs/2511.00129)

**基本信息**

- 🔗 arXiv: [`2511.00129`](https://arxiv.org/abs/2511.00129)
- 👥 作者: Si-Yu Xiao, Xin-Di Zhao, Tian-Hao Mao 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.00129.pdf)

**💡 相关性分析**

满足标准2：论文提出并评估了一套用于训练套管接箍识别模型的数据增强方法，这为化学信息学和质谱分析（作为一类光谱分析技术）领域处理数据稀缺问题、构建鲁棒模型提供了可直接借鉴的数据预处理和增强资源与方法论。

**📖 中文摘要**

本文提出了一种用于井下深度传感和验证的数据增强深度学习方法。研究重点是套管接箍定位器（CCL）测井数据的采集和预处理，以解决真实测井数据稀缺、难以训练神经网络模型的问题。论文提出了一套综合的数据增强方法，包括标准化、标签分布平滑、随机裁剪、标签平滑正则化、时间缩放和多重采样，以增强模型的泛化能力。在基线神经网络模型上的实验表明，这些方法显著提高了模型性能。这项工作直接解决了在CCL数据有限条件下训练模型的数据增强方法空白，为未来井下操作自动化提供了技术基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate downhole depth measurement is essential for oil and gas well operations, directly influencing reservoir contact, production efficiency, and operational safety. Collar correlation using a casing collar locator (CCL) is fundamental for precise depth calibration. While neural network has achieved significant progress in collar recognition, preprocessing methods for such applications remain underdeveloped. Moreover, the limited availability of real well data poses substantial challenges for training neural network models that require extensive datasets. This paper presents a system integrated into a downhole toolstring for CCL log acquisition to facilitate dataset construction. Comprehensive preprocessing methods for data augmentation are proposed, and their effectiveness is evaluated using baseline neural network models. Through systematic experimentation across diverse configurations, the contribution of each augmentation method is analyzed. Results demonstrate that standardization, label distribution smoothing, and random cropping are fundamental prerequisites for model training, while label smoothing regularization, time scaling, and multiple sampling significantly enhance model generalization capabilities. Incorporating the proposed augmentation methods into the two baseline models results in maximum F1 score improvements of 0.027 and 0.024 for the TAN and MAN models, respectively. Furthermore, applying these techniques yields F1 score gains of up to 0.045 for the TAN model and 0.057 for the MAN model compared to prior studies. Performance evaluation on real CCL waveforms confirms the effectiveness and practical applicability of our approach. This work addresses the existing gaps in data augmentation methodologies for training casing collar recognition models under CCL data-limited conditions, and provides a technical foundation for the future automation of downhole operations.

</details>

---

### 111. [No-Rank Tensor Decomposition Using Metric Learning](https://arxiv.org/abs/2511.01816)

**基本信息**

- 🔗 arXiv: [`2511.01816`](https://arxiv.org/abs/2511.01816)
- 👥 作者: Maryam Bagherian
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.01816.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于度量学习的无秩张量分解框架，为高维科学数据（可类比于质谱或化学信息学中的高维数据）的分析提供了一种新的、强调物理可解释性和语义相关性的表征学习方法。该方法可作为化学信息学中处理复杂光谱或分子数据、学习有意义的低维表示的工具或参考。

**📖 中文摘要**

本文提出了一种基于度量学习的无秩张量分解框架，用于高维数据分析。该方法摒弃了传统的基于重构的目标和固定秩约束，转而采用由相似性驱动的优化，结合三元组损失以及多样性和均匀性正则化，学习能够反映语义和物理关系的嵌入表示。论文在包括人脸识别（LFW, Olivetti）、脑连接（ABIDE）和模拟物理系统（星系、晶体）在内的多个数据集上进行了评估。与经典方法（PCA, t-SNE, UMAP）、张量分解（CP, Tucker, t-SVD）和深度学习模型（VAE, DEC, 基于Transformer的嵌入）相比，该方法能产生保留物理和语义相关关系的、可解释的嵌入，并在小数据场景下保持有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tensor decomposition of high-dimensional data often struggles to capture semantically or physically meaningful structures, particularly when relying on reconstruction objectives and fixed-rank constraints. We introduce a no-rank tensor decomposition framework based on metric learning, which replaces reconstruction objectives with a similarity-driven optimization. By combining a triplet loss with diversity and uniformity regularization, the method learns embeddings where distances naturally reflect semantic and physical relationships, supported by theoretical guarantees on convergence and metric properties. We evaluate the approach on diverse datasets, including face recognition (LFW, Olivetti), brain connectivity (ABIDE), and simulated physical systems (galaxies, crystals). In comprehensive comparisons against classical methods (PCA, t-SNE, UMAP), tensor decompositions (CP, Tucker, t-SVD), and deep learning models (VAE, DEC, transformer based embeddings), our method produces embeddings that preserve physically and semantically relevant relationships and achieve competitive clustering performance. While transformers often excel in predictive accuracy on large datasets, our method provides interpretable embeddings and remains effective in small-data regimes where transformer training may be infeasible. This work establishes metric learning as a principled paradigm for tensor analysis, emphasizing physical interpretability and semantic relevance over pixel-level reconstruction, and offering an efficient and robust alternative in data-scarce scientific domains.

</details>

---

### 112. [Hard-constraint physics-residual networks enable robust extrapolation for hydrogen crossover prediction in PEM water electrolyzers](https://arxiv.org/abs/2511.05879)

**基本信息**

- 🔗 arXiv: [`2511.05879`](https://arxiv.org/abs/2511.05879)
- 👥 作者: Yong-Woon Kim, Paul D. Yoo, Chan Yeob Yeun 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05879.pdf)

**💡 相关性分析**

满足标准2：论文提出的硬约束物理残差网络（PR-Net）是一种将领域知识（物理定律）以硬约束形式嵌入神经网络的新型架构。这种方法对于化学信息学和质谱分析领域具有重要借鉴意义，例如，可用于构建结合质谱碎裂规律或化学转化规则的、具有强外推能力的预测模型，为解决该领域数据有限、模型需强泛化的问题提供了创新的工具和框架。

**📖 中文摘要**

本文针对聚合物电解质膜水电解制氢中的氢交叉问题，提出了一种硬约束物理残差网络（PR-Net）。该网络将亨利定律、菲克扩散定律和法拉第定律等分析传输方程作为确定性的计算主干嵌入，限制神经网络仅学习系统的物理偏差。在跨越六种膜类型和多种操作条件（温度、压力、电流密度）的184个实验点上，该架构解决了梯度冲突，实现了高预测精度（R² = 99.57%），且训练方差比纯数据驱动模型降低了39倍。关键在于，PR-Net突破了外推壁垒，在高达200 bar的极端阴极压力（训练域外2.5倍）下仍能保持高性能，而标准物理信息神经网络和纯神经网络在此严重退化或失效。此外，学习到的残差自主捕获了温度引起的膜溶胀和非线性传输机制转变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hydrogen crossover in polymer electrolyte membrane water electrolysis poses a critical safety and efficiency bottleneck for scalable green hydrogen production. While machine learning offers real-time monitoring capabilities, conventional data-driven newral networks (Pure NNs) and soft-constraint physics-informed neural networks (Standard PINNs) suffer from inherent optimization conflicts and fail catastrophically when extrapolating beyond sparse training conditions. Here, we present a hard-constraint physics-residual network (PR-Net) that embeds analytical transport equations -- Henry's law, Fick's diffusion, and Faraday's law -- as a deterministic computational backbone, restricting the neural network to learn only systematic physical deviations. Across 184 experimental points spanning six membrane types and operating conditions of 25--85$^{\circ}$C, 1--200~bar, and 0.05--5.0 A cm$^{-2}$, this architecture intrinsically resolves gradient conflicts, yielding $R^{2} = 99.57 \pm 0.16\%$ with a 39-fold reduction in training variance compared to purely data-driven models ($R^{2} = 96.47 \pm 6.20\%$). Crucially, the PR-Net breaks the extrapolation barrier, maintaining $R^{2} > 97\%$ at extreme cathode pressures up to 200~bar -- a 2.5-fold extrapolation beyond the training domain where Standard PINN severely degrades ($R^{2} = 72.2\%$) and Pure NN collapses ($R^{2} = 58.7\%$). Furthermore, the learned residuals autonomously capture temperature-induced membrane swelling (Spearman's $\rho = 0.506$, $p < 0.001$) and identify the non-linear transport regime transition near 0.23 A cm$^{-2}$, without explicit programming. Delivering millisecond-level inference on edge hardware, the PR-Net establishes a highly reliable, generalizable foundation for adaptive safety control and predictive maintenance in high-pressure electrochemical energy systems.

</details>

---

### 113. [From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models](https://arxiv.org/abs/2511.10788)

**基本信息**

- 🔗 arXiv: [`2511.10788`](https://arxiv.org/abs/2511.10788)
- 👥 作者: Chao Wu, Baoheng Li, Mingchen Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.10788.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于大语言模型推理能力的综述，并提出了以“适应性”为核心的新分析框架。虽然主要关注语言模型，但其对推理范式（演绎、归纳、溯因）的形式化、对适应性机制的梳理以及对未来挑战（如自我评估、元推理）的展望，为构建和评估“化学大模型”的推理能力（例如，用于逆合成分析或质谱解析的推理链生成）提供了重要的概念框架和理论参考。

**📖 中文摘要**

本综述论文从“适应性”这一新视角重新审视大语言模型中的推理问题。论文将演绎、归纳和溯因推理形式化，并将其与LLM中的算法实现联系起来。作者将适应性推理形式化为一个控制增强的策略优化问题，旨在平衡任务性能与计算成本，并区分了通过训练内化的策略与推理时控制机制。论文提出了一个系统的分类法，将现有方法组织为基于训练的方法（通过强化学习、监督微调和学习控制器实现适应性）和免训练的方法（通过提示条件、反馈驱动的停止和模块化组合实现适应性）。该框架阐明了不同机制在实践中如何实现适应性推理，并支持跨不同策略的系统比较。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have made reasoning a central benchmark for evaluating intelligence. While prior surveys focus on efficiency by examining how to shorten reasoning chains or reduce computation, this view overlooks a fundamental challenge: current LLMs apply uniform reasoning strategies regardless of task complexity, generating long traces for trivial problems while failing to extend reasoning for difficult tasks. This survey reframes reasoning through the lens of {adaptivity}: the capability to allocate reasoning effort based on input characteristics such as difficulty and uncertainty. We make three contributions. First, we formalize deductive, inductive, and abductive reasoning within the LLM context, connecting these classical cognitive paradigms with their algorithmic realizations. Second, we formalize adaptive reasoning as a control-augmented policy optimization problem balancing task performance with computational cost, distinguishing learned policies from inference-time control mechanisms. Third, we propose a systematic taxonomy organizing existing methods into training-based approaches that internalize adaptivity through reinforcement learning, supervised fine-tuning, and learned controllers, and training-free approaches that achieve adaptivity through prompt conditioning, feedback-driven halting, and modular composition. This framework clarifies how different mechanisms realize adaptive reasoning in practice and enables systematic comparison across diverse strategies. We conclude by identifying open challenges in self-evaluation, meta-reasoning, and human-aligned reasoning control.

</details>

---

### 114. [When Data is the Algorithm: A Systematic Study and Curation of Preference Optimization Datasets](https://arxiv.org/abs/2511.10985)

**基本信息**

- 🔗 arXiv: [`2511.10985`](https://arxiv.org/abs/2511.10985)
- 👥 作者: Aladin Djuhera, Farhan Ahmed, Swanand Ravindra Kadhe 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.10985.pdf)

**💡 相关性分析**

满足标准2：论文对多个DPO数据集进行了系统性分析和标注，并发布了一个经过筛选和优化的混合数据集UltraMix及其元数据。这项工作为偏好优化研究提供了高质量、可分析的数据资源。对于旨在通过人类反馈或偏好数据来对齐和优化“化学大模型”或“质谱结构推理模型”的研究而言，这种数据集的构建、评估和筛选方法具有直接的参考价值。

**📖 中文摘要**

本文对流行的开源直接偏好优化（DPO）数据集进行了首次全面的、以数据为中心的分析。作者利用Magpie框架为每个样本标注任务类别、输入质量和偏好奖励（一种基于奖励模型的、无需人工标注即可验证偏好顺序的信号）。这使得能够跨数据集进行可扩展的、细粒度的偏好质量检查，揭示了奖励边际的结构性和质性差异。基于这些洞察，作者系统性地策划了一个新的DPO混合数据集UltraMix，该数据集从全部五个语料库中有选择地抽取样本，同时去除了噪声或冗余样本。UltraMix比性能最好的单个数据集小30%，但在关键基准测试中超越了其性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Aligning large language models (LLMs) is a central objective of post-training, often achieved through reward modeling and reinforcement learning methods. Among these, direct preference optimization (DPO) has emerged as a widely adopted technique that fine-tunes LLMs on preferred completions over less favorable ones. While most frontier LLMs do not disclose their curated preference pairs, the broader LLM community has released several open-source DPO datasets, including TuluDPO, ORPO, UltraFeedback, HelpSteer, and Code-Preference-Pairs. However, systematic comparisons remain scarce, largely due to the high computational cost and the lack of rich quality annotations, making it difficult to understand how preferences were selected, which task types they span, and how well they reflect human judgment on a per-sample level. In this work, we present the first comprehensive, data-centric analysis of popular open-source DPO corpora. We leverage the Magpie framework to annotate each sample for task category, input quality, and preference reward, a reward-model-based signal that validates the preference order without relying on human annotations. This enables a scalable, fine-grained inspection of preference quality across datasets, revealing structural and qualitative discrepancies in reward margins. Building on these insights, we systematically curate a new DPO mixture, UltraMix, that draws selectively from all five corpora while removing noisy or redundant samples. UltraMix is 30% smaller than the best-performing individual dataset yet exceeds its performance across key benchmarks. We publicly release all annotations, metadata, and our curated mixture to facilitate future research in data-centric preference optimization.

</details>

---

### 115. [Knowledge Graph Augmented Large Language Models for Disease Prediction](https://arxiv.org/abs/2512.01210)

**基本信息**

- 🔗 arXiv: [`2512.01210`](https://arxiv.org/abs/2512.01210)
- 👥 作者: Ruiyu Wang, Tuan Vinh, Ran Xu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.01210.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个结合知识图谱（KG）和大语言模型（LLM）进行疾病预测的框架。这直接涉及“化学大模型”在垂直领域（医疗）的应用，展示了如何利用外部结构化知识（KG）来引导和增强大模型的推理过程（CoT）。该方法论对于构建面向化学或质谱领域的、具备专业知识推理能力的“大模型”具有重要的参考意义，属于核心主题相关的应用研究。

**📖 中文摘要**

本文提出了一种知识图谱（KG）引导的思维链（CoT）框架，用于电子健康记录（EHR）的疾病预测。该方法将ICD-9代码映射到PrimeKG知识图谱，挖掘疾病相关的节点和路径，并利用这些路径为时间一致的CoT推理提供支架，仅保留结论与观察结果匹配的样本。作者在MIMIC-III数据集上，针对十种PrimeKG映射的疾病，对轻量级指令微调LLM进行了微调。模型在有限数据（400和1000个索引就诊）上表现优异，并能够零样本迁移到CRADLE队列，显著提升准确率。临床医生盲评研究显示，KG引导的CoT推理在清晰度、相关性和正确性上更受青睐。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic health records (EHRs) enable strong clinical prediction, but explanations are often coarse and hard to use for patient-level decisions. We propose a knowledge graph (KG)-guided chain-of-thought (CoT) framework for visit-level disease prediction on MIMIC-III. We map ICD-9 codes to PrimeKG, mine disease-relevant nodes and paths, and use these paths to scaffold temporally consistent CoT rationales, retaining only samples whose conclusions match observed outcomes. We fine-tune lightweight instruction-tuned LLMs (LLaMA-3.1-Instruct-8B and Gemma-7B) on two small cohorts (400 and 1,000 index visits) across ten PrimeKG-mapped diseases. Our models outperform strong classical baselines, reaching AUROC 0.66-0.70 and macro-AUPR 0.40-0.47. Without additional training, the models transfer zero-shot to the CRADLE cohort, improving accuracy from 0.40-0.51 to 0.72-0.77. In a blinded clinician study, KG-guided CoT rationales are consistently preferred for clarity, relevance, and correctness. Code is available at: this https URL

</details>

---

### 116. [Optimal transport unlocks end-to-end learning for single-molecule localization](https://arxiv.org/abs/2512.10683)

**基本信息**

- 🔗 arXiv: [`2512.10683`](https://arxiv.org/abs/2512.10683)
- 👥 作者: Romain Seailles, Jean-Baptiste Masson, Jean Ponce 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10683.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于最优传输的端到端学习框架和新的损失函数，用于解决单分子定位显微镜（一种高分辨率成像技术）中的密集信号检测和定位问题。虽然应用领域是生物成像，但其核心方法——将检测问题转化为集合匹配并用最优传输损失进行端到端优化——为质谱分析（尤其是质谱成像或复杂谱图解析）中类似的“从密集信号中定位和识别目标”问题提供了新颖且强大的算法工具和思路。

**📖 中文摘要**

本文针对单分子定位显微镜（SMLM）中的高密度荧光团定位问题，提出了一种基于最优传输的端到端学习方法。传统方法依赖非极大值抑制（NMS）层，该层不可微分且可能丢弃真实信号。作者将SMLM训练目标重新表述为一个集合匹配问题，推导出一种最优传输损失，从而在推理时消除对NMS的需求，实现端到端训练。此外，提出了一种迭代神经网络，将显微镜光学系统的知识集成到模型中。在合成基准和真实生物数据上的实验表明，新损失函数和架构在中高发射器密度下超越了现有技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-molecule localization microscopy (SMLM) allows reconstructing biology-relevant structures beyond the diffraction limit by detecting and localizing individual fluorophores -- fluorescent molecules stained onto the observed specimen -- over time to reconstruct super-resolved images. Currently, efficient SMLM requires non-overlapping emitting fluorophores, leading to long acquisition times that hinders live-cell imaging. Recent deep-learning approaches can handle denser emissions, but they rely on variants of non-maximum suppression (NMS) layers, which are unfortunately non-differentiable and may discard true positives with their local fusion strategy. In this presentation, we reformulate the SMLM training objective as a set-matching problem, deriving an optimal-transport loss that eliminates the need for NMS during inference and enables end-to-end training. Additionally, we propose an iterative neural network that integrates knowledge of the microscope's optical system inside our model. Experiments on synthetic benchmarks and real biological data show that both our new loss function and architecture surpass the state of the art at moderate and high emitter densities. Code is available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：8
- 累计论文数量：519

## 📝 历史记录

> 暂无历史数据

