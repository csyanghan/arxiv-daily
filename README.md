# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-03 12:58:35

## 📅 2026-03-03 (今日最新)

**相关论文数：131**

### 1. [LitBench: A Graph-Centric Large Language Model Benchmarking Tool For Literature Tasks](https://arxiv.org/abs/2603.00051)

**基本信息**

- 🔗 arXiv: [`2603.00051`](https://arxiv.org/abs/2603.00051)
- 👥 作者: Andreas Varvarigos, Ali Maatouk, Jiasheng Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00051.pdf)

**💡 相关性分析**

满足标准2：LitBench是一个专门为文献相关任务（可视为化学信息学领域的一个子集）构建数据集和评估框架的工具。它通过生成领域特定的文献图并基于此创建训练/评估数据集，为开发化学信息学领域的专业LLM提供了数据资源和基准测试工具。

**📖 中文摘要**

本文介绍了LitBench，一个用于开发和评估针对文献相关任务的领域特定大语言模型（LLM）的基准测试工具。其核心是一个数据整理流程，能够生成领域特定的文献子图，并根据生成的节点和边的文本属性构建训练和评估数据集。该工具支持用户选择任何领域（无论是高层领域还是专业交叉领域）来整理文献图。除了数据集整理，LitBench还定义了一套全面的文献任务，从节点和边级别的分析到高级应用（如相关工作生成）。这些任务使LLM能够在训练过程中内化嵌入在整理图中的领域特定知识和关系，同时支持对模型性能进行严格评估。结果表明，在LitBench数据集上训练和评估的小型领域特定LLM，与GPT-4o和DeepSeek-R1等最先进模型相比，取得了有竞争力的性能。该工具已开源，以增强可访问性和易用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While large language models (LLMs) have become the de facto framework for literature-related tasks, they still struggle to function as domain-specific literature agents due to their inability to connect pieces of knowledge and reason across domain-specific contexts, terminologies, and nomenclatures. This challenge underscores the need for a tool that facilitates such domain-specific adaptation and enables rigorous benchmarking across literature tasks. To that end, we introduce LitBench, a benchmarking tool designed to enable the development and evaluation of domain-specific LLMs tailored to literature-related tasks. At its core, LitBench uses a data curation process that generates domain-specific literature sub-graphs and constructs training and evaluation datasets based on the textual attributes of the resulting nodes and edges. The tool is designed for flexibility, supporting the curation of literature graphs across any domain chosen by the user, whether high-level fields or specialized interdisciplinary areas. In addition to dataset curation, LitBench defines a comprehensive suite of literature tasks, ranging from node and edge level analyses to advanced applications such as related work generation. These tasks enable LLMs to internalize domain-specific knowledge and relationships embedded in the curated graph during training, while also supporting rigorous evaluation of model performance. Our results show that small domain-specific LLMs trained and evaluated on LitBench datasets achieve competitive performance compared to state-of-the-art models like GPT-4o and DeepSeek-R1. To enhance accessibility and ease of use, we open-source the tool along with an AI agent tool that streamlines data curation, model training, and evaluation.

</details>

---

### 2. [DeepXiv-SDK: An Agentic Data Interface for Scientific Papers](https://arxiv.org/abs/2603.00084)

**基本信息**

- 🔗 arXiv: [`2603.00084`](https://arxiv.org/abs/2603.00084)
- 👥 作者: Hongjin Qian, Ziyi Xia, Ze Liu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00084.pdf)

**💡 相关性分析**

满足标准2：DeepXiv-SDK是一个专门为科学论文（包括化学、质谱等领域）设计的智能数据接口和工具。它提供了结构化的论文访问、检索和整理功能，可作为化学信息学和质谱分析研究中的数据资源获取和预处理工具，支持高效的知识发现和证据定位。

**📖 中文摘要**

本文介绍了DeepXiv-SDK，这是一个面向科学论文的智能数据接口，旨在解决研究智能体在科学信息检索和基于证据的决策中面临的论文访问瓶颈。该SDK将论文访问标准化，提供预算感知的视图，并将证据定位视为首要操作。它支持渐进式访问，与智能体分配注意力和阅读预算的方式保持一致。DeepXiv-SDK以结构化视图的形式提供：用于筛选的标题优先视图、用于定向导航的章节结构化视图，以及用于验证的按需证据级别访问。每一层都通过丰富的属性和明确的预算提示进行增强，使智能体能够在升级到全文处理之前平衡相关性、成本和证据定位。DeepXiv-SDK还支持对论文属性的多面检索和聚合，实现对论文集的约束驱动搜索和整理。该工具目前已在arXiv规模上部署，并设计为可扩展到其他开放获取语料库（如PubMed Central, bioRxiv）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Research agents are increasingly used in AI4Science for scientific information seeking and evidence-grounded decision making. Yet a persistent bottleneck is paper access: agents typically retrieve PDF/HTML pages, heuristically parse them, and ingest long unstructured text, leading to token-heavy reading and brittle evidence lookup. This motivates an agentic data interface for scientific papers that standardizes access, exposes budget-aware views, and treats grounding as a first-class operation. We introduce DeepXiv-SDK, which enables progressive access aligned with how agents allocate attention and reading budget. DeepXiv-SDK exposes as structured views a header-first view for screening, a section-structured view for targeted navigation, and on-demand evidence-level access for verification. Each layer is augmented with enriched attributes and explicit budget hints, so agents can balance relevance, cost, and grounding before escalating to full-text processing. DeepXiv-SDK also supports multi-faceted retrieval and aggregation over paper attributes, enabling constraint-driven search and curation over paper sets. DeepXiv-SDK is currently deployed at arXiv scale with daily synchronization to new releases and is designed to extend to other open-access corpora (e.g., PubMed Central, bioRxiv). We release RESTful APIs, an open-source Python SDK, and a web demo showcasing deep search and deep research workflows; the service is free to use with registration.

</details>

---

### 3. [SciKGDash: The Scientific Knowledge Graph Dashboard for Supporting Knowledge Curation](https://arxiv.org/abs/2603.00107)

**基本信息**

- 🔗 arXiv: [`2603.00107`](https://arxiv.org/abs/2603.00107)
- 👥 作者: Lena John, Sören Auer, Oliver Karras
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00107.pdf)

**💡 相关性分析**

满足标准2：SciKGDash是一个专门为研究知识图谱（包括化学信息学领域可能构建的图谱）设计的知识整理和支持工具。它提供了用于评估和提升知识图谱质量的数据集（基准）和仪表板工具，可作为化学信息学领域知识库构建和管理的数据资源与工具。

**📖 中文摘要**

本文介绍了SciKGDash，一个旨在支持开放研究知识图谱（ORKG）知识整理的科学知识图谱仪表板。该研究采用行动研究方法，与ORKG的整理与社区建设团队合作，探索开发一个旨在支持知识整理的仪表板。SciKGDash作为一个最小可行产品，根据C&CB团队的需求定制，并有可能适配到其他研究知识图谱。一项有15名参与者参与的实验证明了SciKGDash的可用性，在5分钟内成功完成了5项整理任务中的4项。此外，SciKGDash获得了积极的用户体验评分。这项研究强调了在多样化研究知识图谱中应用特定质量指标的局限性。未来的工作应侧重于识别通用的质量指标，并增强SciKGDash以支持查询定制化质量指标的用户友好功能。总体而言，研究知识图谱中的知识整理仍是一个未被充分探索的领域，值得进一步研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Research knowledge graphs (RKGs) have emerged as essential technology for organizing scientific knowledge, but their success depends heavily on the quality of their underlying content. Knowledge curation is a critical task to ensure the quality of (research) knowledge graphs ((R)KGs), with human curation being the gold standard despite its time- and resource-intensive nature. Automated methods, while efficient, lack the precision of human expertise. Hybrid approaches, combining automated processes with human oversight, offer a promising solution to this challenge. Dashboards can act as supportive tools in hybrid curation approaches, offering real-time updates and visual overviews. This paper presents an action research study, conducted in collaboration with the Curation and Community Building (C&CB) team of the Open Research Knowledge Graph (ORKG), to explore the development of a dashboard, called SciKGDash, designed to support knowledge curation of the ORKG. SciKGDash serves as a minimum viable product (MVP) tailored to the needs of the C&CB team, with potential for adaptation to other (R)KGs. An experiment with 15 participants demonstrated the usability of SciKGDash, with successful completion of 4 out of 5 curation tasks in under 5 minutes. In addition, SciKGDash received a positive user experience rating (UEQ score of 1.93). While the tailored solution proved effective for the ORKG, the research also highlights limitations in applying specific quality metrics across diverse (R)KGs. Future work should focus on identifying common quality metrics and enhancing SciKGDash with user-friendly features for querying customized quality metrics. Overall, knowledge curation in RKGs remains an under-explored field, warranting further research.

</details>

---

### 4. [NovaLAD: A Fast, CPU-Optimized Document Extraction Pipeline for Generative AI and Data Intelligence](https://arxiv.org/abs/2603.00122)

**基本信息**

- 🔗 arXiv: [`2603.00122`](https://arxiv.org/abs/2603.00122)
- 👥 作者: Aman Ulla
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00122.pdf)

**💡 相关性分析**

满足标准2：NovaLAD是一个高效的文档解析工具，能够从PDF等非结构化文档（包括科学论文、实验报告）中提取结构化文本、布局信息和图像内容，并生成RAG就绪文本和知识图谱。这为化学信息学和质谱分析领域从文献中自动化提取数据、构建数据集或知识库提供了强大的数据预处理工具和资源。

**📖 中文摘要**

本文介绍了NovaLAD，一个全面的文档解析系统，集成了两个并发的YOLO目标检测模型（元素检测和布局检测）以及基于规则的分组和可选的视觉语言增强。当页面图像输入时，它同时通过两个模型处理。元素模型查找标题、页眉、文本、表格、图像等语义内容，布局模型查找布局框、列组、多列、行组等结构区域。一个关键设计是首先将图像或图形通过图像分类器（ViT）判断其是否相关。只有有用的图像才会提交给视觉大语言模型以获取标题、摘要和结构化信息，从而减少噪音和成本。NovaLAD为速度而构建：可在CPU上运行，对检测、分类、OCR和转换采用并行执行，并生成多种格式，包括结构化JSON、Markdown、RAG就绪文本和知识图谱。在DP-Bench基准测试中，NovaLAD获得了96.49%的TEDS和98.51%的NID，优于商业和开源解析器。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Document extraction is an important step before retrieval-augmented generation (RAG), knowledge bases, and downstream generative AI can work. It turns unstructured documents like PDFs and scans into structured text and layout-aware representations. We introduce NovaLAD, a comprehensive document parsing system that integrates two concurrent YOLO object detection models - element detection and layout detection - with rule-based grouping and optional vision-language enhancement. When a page image is sent in, the first thing that happens is that it goes through both models at the same time. The element model finds semantic content like the title, header, text, table, image, and so on, and the layout model finds structural regions like layout_box, column_group, multi_column, row_group, and so on. A key design decision is to first send an image or figure through an image classifier (ViT) that decides whether it is relevant or not. Only useful images are then submitted to the Vision LLM for title, summary, and structured information, which cuts down on noise and costs. NovaLAD is built for speed: it works on CPU, employs parallel execution for detection, classification, OCR, and conversion, and generates several forms, including structured JSON, Markdown, RAG-ready texts, and knowledge graphs. We test on the DP-Bench benchmark (upstage/dp-bench) and get 96.49% TEDS and 98.51% NID, which is better than both commercial and open-source parsers. This paper explains how to extract data, how the architecture works, how data flows, and how to make NovaLAD both accurate and usable without needing a GPU.

</details>

---

### 5. [Leveraging GenAI for Segmenting and Labeling Centuries-old Technical Documents](https://arxiv.org/abs/2603.00147)

**基本信息**

- 🔗 arXiv: [`2603.00147`](https://arxiv.org/abs/2603.00147)
- 👥 作者: Carlos Monroy, Benjamin Navarro
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00147.pdf)

**💡 相关性分析**

满足标准2：本文提出了一种利用生成式AI（SAM2, Florence2, ChatGPT）和领域特定本体（ontoShip, glosShip）来自动化分割和标记历史技术文档图像的方法。虽然案例是造船论文，但该方法论（结合领域知识进行文档图像信息提取）可迁移到化学信息学领域，例如从历史化学文献或图谱中提取化合物结构和反应信息，因此提供了相关的工具和方法思路。

**📖 中文摘要**

本文报告了在分割和标记十六、十七世纪造船论文图像方面的持续工作。为此，我们利用SAM2进行图像分割；利用Florence2和ChatGPT进行标记；并利用专门的船舶建筑本体ontoShip和术语表glosShip来增强标记过程。初步结果展示了结合这些技术来改善珍贵历史文献的整理和检索的潜力。我们还讨论了在这种方法中遇到的挑战和限制，以及未来如何克服这些问题的想法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Image segmentation and image recognition are well established computational techniques in the broader discipline of image processing. Segmentation allows to locate areas in an image, while recognition identifies specific objects within an image. These techniques have shown remarkable accuracy with modern images, mainly because the amount of training data is vast. Achieving similar accuracy in digitized images of centuries-old documents is more challenging. This difficulty is due to two main reasons: first, the lack of sufficient training data, and second, because the degree of specialization in a given domain. Despite these limitations, the ability to segment and recognize objects in these collections is important for automating the curation, cataloging, and dissemination of knowledge, making the contents of priceless collections accessible to scholars and the general public. In this paper, we report on our ongoing work in segmenting and labeling images pertaining to shipbuilding treatises from the XVI and XVII centuries, a historical period known as the Age of Exploration. To this end, we leverage SAM2 for image segmentation; Florence2 and ChatGPT for labeling; and a specialized ontology ontoShip and glossary glosShip of nautical architecture for enhancing the labeling process. Preliminary results demonstrate the potential of marrying these technologies for improving curation and retrieval of priceless historical documents. We also discuss the challenges and limitations encountered in this approach and ideas on how to overcome them in the future.

</details>

---

### 6. [Pulse-Driven Neural Architecture: Learnable Oscillatory Dynamics for Robust Continuous-Time Sequence Processing](https://arxiv.org/abs/2603.00153)

**基本信息**

- 🔗 arXiv: [`2603.00153`](https://arxiv.org/abs/2603.00153)
- 👥 作者: Paras Sharma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00153.pdf)

**💡 相关性分析**

满足标准1：论文提出的PDNA架构，其核心是可学习的振荡动力学，这为构建能够处理复杂时间序列和动态过程的化学大模型（如分子动力学模拟、光谱时间序列分析）提供了创新的模型设计思路和方法论参考。

**📖 中文摘要**

这篇论文提出了PDNA（脉冲驱动神经架构），一种为连续时间循环网络添加可学习振荡动力学的方法。虽然其核心应用是序列处理，但其引入的“可学习振荡动力学”概念与“化学大模型”中探索分子动态、时间序列或周期性行为的建模思路在方法论上存在潜在关联。例如，在化学信息学中，分子动力学模拟、光谱时间序列分析或反应过程建模都可能受益于这种能够维持内部状态独立演化的振荡机制。因此，该工作为构建能够处理复杂时间演化或周期性模式的化学领域大模型提供了新颖的架构设计思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce PDNA (Pulse-Driven Neural Architecture), a method for augmenting continuous-time recurrent networks with learnable oscillatory dynamics that maintain internal state evolution independently of external input. Built on Closed-form Continuous-time (CfC) networks, PDNA adds two components: (1) a pulse module that generates structured oscillations $A \cdot \sin(\omega t + \varphi(h))$ with learnable frequencies and state-dependent phase, and (2) a self-attend module that applies recurrent self-attention to the hidden state. Through a controlled ablation study on sequential MNIST (sMNIST) with five random seeds, we evaluate gap robustness -- the ability to maintain performance when portions of the input sequence are removed at test time. Our key finding is that structured oscillatory dynamics significantly improve robustness to input interruptions: the self-attend variant achieves a statistically significant 2.78 percentage point multi-gap advantage over baseline ($p = 0.041$), while the pulse variant shows a 4.62 pp advantage with large effect size (Cohen's $d = 0.87$). A noise control (random perturbation of equal magnitude) provides no benefit, confirming that the advantage is structural rather than merely dynamic. These results provide evidence that continuous-time models can benefit from biologically-inspired internal oscillatory mechanisms for temporal robustness.

</details>

---

### 7. [Summer-22B: A Systematic Approach to Dataset Engineering and Training at Scale for Video Foundation Model](https://arxiv.org/abs/2603.00173)

**基本信息**

- 🔗 arXiv: [`2603.00173`](https://arxiv.org/abs/2603.00173)
- 👥 作者: Simo Ryu, Chunghwan Han
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00173.pdf)

**💡 相关性分析**

满足标准2：论文系统性地总结了构建和训练大规模基础模型（Summer-22B）的数据集工程方法、训练框架和架构决策。这些经验、工具（如Lavender Data系统）和方法论（如μP参数化）可直接作为构建化学信息学或质谱分析领域大模型时可借鉴的数据资源和工程实践。

**📖 中文摘要**

这篇论文详细介绍了从头开始训练视频基础模型Summer-22B的系统性工程经验。报告重点阐述了从原始素材收集到模型训练全流程中的工程挑战、设计决策和经验教训，特别是数据集工程（包括基于元数据的筛选、多阶段过滤）、大规模训练（使用μP参数化和超球约束优化）以及架构选择。虽然主题是视频模型，但其在“大规模数据集工程”、“模型训练规模化”和“架构设计决策”方面的系统性方法和经验总结，对于在化学信息学或质谱分析领域构建和训练需要处理海量分子或光谱数据的“化学大模型”具有极高的参考价值。它为解决数据管理、质量控制和训练稳定性等共性问题提供了宝贵的实践指南。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We describe our experience training Summer-22B, a video foundation model developed from scratch. This report documents the engineering challenges, design decisions, and lessons learned while scaling from raw footage collection to a functional model trained on approximately 50 million clips. We outline our approach combining metadata-driven dataset curation, multi-stage filtering, $\mu$P parameterization, and hypersphere-constrained optimization. We developed the Lavender Data system for dataset management and adopted inference-aware architectural choices. We share observations on what worked in our setting: dataset engineering consumed the majority of effort, architectural variants showed smaller differences than we expected, and $\mu$P hyperparameter transfer appeared effective even under geometric constraints. We hope this account proves useful to others undertaking similar projects.

</details>

---

### 8. [NNiT: Width-Agnostic Neural Network Generation with Structurally Aligned Weight Spaces](https://arxiv.org/abs/2603.00180)

**基本信息**

- 🔗 arXiv: [`2603.00180`](https://arxiv.org/abs/2603.00180)
- 👥 作者: Jiwoo Kim, Swarajh Mehta, Hao-Lun Hsu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00180.pdf)

**💡 相关性分析**

满足标准1：论文提出的NNiT框架是一种生成神经网络参数的生成模型。这一核心方法与“化学大模型”中探索使用生成模型来设计分子、预测性质或自动化构建分析模型的研究方向直接相关，为后者提供了创新的技术思路。

**📖 中文摘要**

这篇论文提出了NNiT（神经网络的扩散变换器），一种以宽度无关的方式生成神经网络参数的方法。它通过将权重矩阵标记化为补丁，并将其建模为局部结构化场来实现。该方法解决了神经网络参数生成中的排列对称性问题，并能在未见过的架构拓扑上生成功能完整的网络。虽然其应用场景是机器人任务，但其核心贡献——一种能够“生成”或“设计”神经网络权重/架构的生成模型——与“化学大模型”的研究前沿高度相关。在化学领域，类似的思想可以应用于生成分子结构、预测分子性质模型的参数，或自动化设计用于质谱解析的专用神经网络架构。因此，该工作为化学大模型的研究，特别是在自动化模型设计和生成方面，提供了重要的方法论启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative modeling of neural network parameters is often tied to architectures because standard parameter representations rely on known weight-matrix dimensions. Generation is further complicated by permutation symmetries that allow networks to model similar input-output functions while having widely different, unaligned parameterizations. In this work, we introduce Neural Network Diffusion Transformers (NNiTs), which generate weights in a width-agnostic manner by tokenizing weight matrices into patches and modeling them as locally structured fields. We establish that Graph HyperNetworks (GHNs) with a convolutional neural network (CNN) decoder structurally align the weight space, creating the local correlation necessary for patch-based processing. Focusing on MLPs, where permutation symmetry is especially apparent, NNiT generates fully functional networks across a range of architectures. Our approach jointly models discrete architecture tokens and continuous weight patches within a single sequence model. On ManiSkill3 robotics tasks, NNiT achieves >85% success on architecture topologies unseen during training, while baseline approaches fail to generalize.

</details>

---

### 9. [Task-Driven Subspace Decomposition for Knowledge Sharing and Isolation in LoRA-based Continual Learning](https://arxiv.org/abs/2603.00191)

**基本信息**

- 🔗 arXiv: [`2603.00191`](https://arxiv.org/abs/2603.00191)
- 👥 作者: Lingfeng He, De Cheng, Huaijie Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00191.pdf)

**💡 相关性分析**

满足标准1：论文的核心是改进LoRA这一广泛用于大模型适配的技术，提出了任务驱动的子空间分解方法。这对于在化学信息学和质谱分析领域高效地定制和微调大模型（例如，针对不同的分子家族或质谱仪器进行适配）具有直接的方法论指导意义。

**📖 中文摘要**

这篇论文针对基于LoRA的持续学习，提出了LoDA方法，通过任务驱动的子空间分解来实现知识共享与隔离。它从投影能量的角度研究LoRA的学习能力，并构建通用和真正任务特定的LoRA子空间。这项工作虽然聚焦于持续学习场景，但其对LoRA这一参数高效微调技术的深入分析和改进，对于在化学信息学和质谱分析中应用和优化大模型具有重要价值。例如，在构建用于质谱结构推理或分子性质预测的大模型时，经常需要针对不同的子任务（如不同类别的分子、不同仪器类型的光谱）进行高效适配。LoDA提供了一种在微调过程中更好地平衡知识迁移（共享）和任务特异性（隔离）的理论框架和实用方法，有助于提升大模型在化学领域的泛化能力和应用效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continual Learning (CL) requires models to sequentially adapt to new tasks without forgetting old knowledge. Recently, Low-Rank Adaptation (LoRA), a representative Parameter-Efficient Fine-Tuning (PEFT) method, has gained increasing attention in CL. Several LoRA-based CL methods reduce interference across tasks by separating their update spaces, typically building the new space from the estimated null space of past tasks. However, they (i) overlook task-shared directions, which suppresses knowledge transfer, and (ii) fail to capture truly effective task-specific directions since these ``null bases" of old tasks can remain nearly inactive for new task under correlated tasks. To address this, we study LoRA learning capability from a projection energy perspective, and propose Low-rank Decomposition and Adaptation (LoDA). It performs a task-driven decomposition to build general and truly task-specific LoRA subspaces by solving two energy-based objectives, decoupling directions for knowledge sharing and isolation. LoDA fixes LoRA down-projections on two subspaces and learns robust up-projections via a Gradient-Aligned Optimization (GAO) approach. After each task, before integrating the LoRA updates into the backbone, LoDA derives a closed-form recalibration for the general update, approximating a feature-level joint optimum along this task-shared direction. Experiments indicate that LoDA outperforms existing CL methods.

</details>

---

### 10. [CoPeP: Benchmarking Continual Pretraining for Protein Language Models](https://arxiv.org/abs/2603.00253)

**基本信息**

- 🔗 arXiv: [`2603.00253`](https://arxiv.org/abs/2603.00253)
- 👥 作者: Darshan Patil, Pranshu Malviya, Mathieu Reymond 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00253.pdf)

**💡 相关性分析**

满足标准2和3：首先，论文提出了CoPeP基准，这是一个用于评估蛋白质语言模型持续预训练的数据集和评估框架（标准2）。其次，论文系统性地评估和比较了多种持续学习方法，并总结了关键发现，这为化学大模型如何适应不断增长的数据这一重要问题提供了综述性的讨论和前瞻性见解（标准3）。

**📖 中文摘要**

这篇论文引入了CoPeP基准，用于评估蛋白质语言模型的持续预训练。该基准包含一个跨越十年的蛋白质数据集序列，并定义了在31个蛋白质理解任务上的评估指标。论文评估了多种持续学习方法，并发现结合时间元信息可以显著提升模型性能。这项工作直接针对“大模型”（蛋白质语言模型）的“持续学习”这一重要主题。虽然领域是生物信息学，但其核心问题——如何让大模型持续学习不断增长和更新的科学数据（如新的分子结构、质谱图谱）——与化学信息学和质谱分析领域面临的挑战完全相同。CoPeP基准本身就是一个重要的“数据资源”和评估框架，其提出的方法、评估协议和结论，为化学领域构建能够与时俱进、吸收新知识的大模型提供了宝贵的参考和可直接借鉴的基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (pLMs) have recently gained significant attention for their ability to uncover relationships between sequence, structure, and function from evolutionary statistics, thereby accelerating therapeutic drug discovery. These models learn from large protein databases that are continuously updated by the biology community and whose dynamic nature motivates the application of continual learning, not only to keep up with the ever-growing data, but also as an opportunity to take advantage of the temporal meta-information that is created during this process. As a result, we introduce the Continual Pretraining of Protein Language Models (CoPeP) benchmark, a novel benchmark for evaluating continual learning approaches on pLMs. Specifically, we curate a sequence of protein datasets derived from the UniProt Knowledgebase spanning a decade and define metrics to assess pLM performance across 31 protein understanding tasks. We evaluate several methods from the continual learning literature, including replay, unlearning, and plasticity-based methods, some of which have never been applied to models and data of this scale. Our findings reveal that incorporating temporal meta-information improves perplexity by up to 7% even when compared to training on data from all tasks jointly. Moreover, even at scale, several continual learning methods outperform naive continual pretraining. The CoPeP benchmark offers an exciting opportunity to study these methods at scale in an impactful real-world application.

</details>

---

### 11. [Transformers Remember First, Forget Last: Dual-Process Interference in LLMs](https://arxiv.org/abs/2603.00270)

**基本信息**

- 🔗 arXiv: [`2603.00270`](https://arxiv.org/abs/2603.00270)
- 👥 作者: Sourav Chattaraj, Kanak Raj
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00270.pdf)

**💡 相关性分析**

满足标准1：论文的核心是研究大模型的记忆和推理机制，特别是信息冲突下的处理模式。这对于构建和理解需要进行复杂、多步推理的“化学大模型”和“质谱结构推理”模型的内在工作机制、潜在偏差及改进方向具有直接的理论相关性。

**📖 中文摘要**

这篇论文研究了大型语言模型在遇到上下文冲突信息时的记忆干扰模式，发现了与人类记忆相反的“首因效应”（早期编码被保护）。论文通过将认知心理学中的经典干扰范式适配到LLM评估中，对39种不同架构和规模的LLM进行了测试，并揭示了RI（倒摄干扰）和PI（前摄干扰）作为独立记忆机制的证据。这项工作的核心是理解和诊断大模型的内部记忆与推理机制。虽然不直接针对化学领域，但其研究范式、发现的问题（如首因偏差、不同干扰类型的独立性）以及提出的分析框架，对于理解和改进旨在进行复杂推理的“化学大模型”和“质谱结构推理”模型具有根本性的启示。例如，在质谱解析中，模型可能需要整合来自多个谱图或数据库的先验知识（早期信息）与当前观察到的碎片峰（近期信息），这项工作为分析此类模型可能存在的推理偏差和失败模式提供了理论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

When large language models encounter conflicting information in context, which memories survive -- early or recent? We adapt classical interference paradigms from cognitive psychology to answer this question, testing 39 LLMs across diverse architectures and scales. Every model shows the same pattern: proactive interference (PI) dominates retroactive interference (RI) universally (Cohen's d = 1.73, p < 0.0001), meaning early encodings are protected at the cost of recent information -- the opposite of human memory, where RI typically dominates. Three findings indicate that RI and PI reflect separate memory mechanisms. RI and PI are uncorrelated (R^2 = 0.044), rejecting a unified "memory capacity." Model size predicts RI resistance (R^2 = 0.49) but not PI (R^2 = 0.06, n.s.) -- only RI is capacity-dependent. And error analysis reveals distinct failure modes: RI failures are passive retrieval failures (51%), while PI failures show active primacy intrusion (56%); both show <1% hallucination. These patterns parallel the consolidation-retrieval distinction in cognitive science, suggesting that transformer attention creates a primacy bias with direct implications for interference-heavy applications.

</details>

---

### 12. [Polynomial Surrogate Training for Differentiable Ternary Logic Gate Networks](https://arxiv.org/abs/2603.00302)

**基本信息**

- 🔗 arXiv: [`2603.00302`](https://arxiv.org/abs/2603.00302)
- 👥 作者: Sai Sandeep Damera, Ryan Matheu, Aniruddh G. Puranic 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00302.pdf)

**💡 相关性分析**

满足标准1：论文提出了可处理三值逻辑（包含未知状态）的可微逻辑网络训练方法。这为在化学信息学和质谱分析中构建能够进行不确定性推理、提供置信度评估的“大模型”和“结构推理”模型提供了新颖且强大的建模框架和算法基础。

**📖 中文摘要**

这篇论文提出了多项式代理训练方法，用于可微的三值逻辑门网络。该方法将每个三值神经元表示为一个低阶多项式，大幅减少了参数，并证明了训练网络与其离散化逻辑电路之间的误差是有界的。这项工作将可微逻辑网络从二值扩展到了三值（包含UNKNOWN状态），使得网络能够进行原则性的不确定性弃权。这一进展与“化学大模型”和“质谱结构推理”高度相关。在化学信息学中，分子性质预测、反应结果判断常常存在不确定性；在质谱结构推理中，对碎片峰的归属或分子结构的推断也经常不是非黑即白的。能够表达“未知”或“不确定”状态的逻辑框架，为构建更加稳健、可解释且能表达置信度的化学推理模型提供了强大的底层计算范式。论文提出的PST方法为解决逻辑价态扩展带来的组合爆炸问题提供了通用方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Differentiable logic gate networks (DLGNs) learn compact, interpretable Boolean circuits via gradient-based training, but all existing variants are restricted to the 16 two-input binary gates. Extending DLGNs to Ternary Kleene $K_3$ logic and training DTLGNs where the UNKNOWN state enables principled abstention under uncertainty is desirable. However, the support set of potential gates per neuron explodes to $19{,}683$, making the established softmax-over-gates training approach intractable. We introduce Polynomial Surrogate Training (PST), which represents each ternary neuron as a degree-$(2,2)$ polynomial with 9 learnable coefficients (a $2{,}187\times$ parameter reduction) and prove that the gap between the trained network and its discretized logic circuit is bounded by a data-independent commitment loss that vanishes at convergence. Scaling experiments from 48K to 512K neurons on CIFAR-10 demonstrate that this hardening gap contracts with overparameterization. Ternary networks train $2$-$3\times$ faster than binary DLGNs and discover true ternary gates that are functionally diverse. On synthetic and tabular tasks we find that the UNKNOWN output acts as a Bayes-optimal uncertainty proxy, enabling selective prediction in which ternary circuits surpass binary accuracy once low-confidence predictions are filtered. More broadly, PST establishes a general polynomial-surrogate methodology whose parameterization cost grows only quadratically with logic valence, opening the door to many-valued differentiable logic.

</details>

---

### 13. [When does Chain-of-Thought Help: A Markovian Perspective](https://arxiv.org/abs/2603.00306)

**基本信息**

- 🔗 arXiv: [`2603.00306`](https://arxiv.org/abs/2603.00306)
- 👥 作者: Zihan Wang, Yijun Dong, Qi Lei
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00306.pdf)

**💡 相关性分析**

满足标准1：论文对思维链这一核心推理技术的有效性条件进行了理论建模和分析。这对于在化学大模型和质谱结构推理任务中有效利用和优化CoT提示，以提升模型的多步、复杂推理能力，具有根本性的理论指导价值。

**📖 中文摘要**

这篇论文从马尔可夫链的视角分析了思维链提示何时以及为何有效。理论分析指出，“转移对齐”（即不同实例是否共享共同的逐步转移核）是CoT有效性的关键决定因素。当步骤间的转移一致时，CoT能降低推理时的样本复杂度；反之则收益可能消失。论文还量化了中间步骤噪声对CoT收益的调节作用。这项研究是对大模型推理机制的基础性理论探索。虽然不特定于化学领域，但其结论对于在化学信息学和质谱分析中设计和应用CoT进行复杂问题求解（如多步分子合成规划、质谱谱图的逐步解析）具有至关重要的指导意义。它帮助研究者理解在什么条件下CoT可能有效，如何设计提示以促进“转移对齐”，以及如何评估和提升化学领域大模型的推理可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chain-of-Thought (CoT) prompting is a widely used inference-time technique for improving reasoning, yet its gains are uneven across tasks. We analyze when and why CoT helps by modeling the step-wise reasoning trajectory as a Markov chain. Each intermediate step is a state and the dependence between steps is captured by a transition kernel. Our theory identifies transition alignment, whether instances share a common step-wise transition kernel, as the key determinant of CoT's effectiveness. When transitions are identical across steps, CoT reduces inference-time sample complexity: fewer context sample trajectories suffice to recover the final decision. In contrast, when transitions differ across steps, these gains can vanish. We further quantify how noise in intermediate steps modulates CoT's benefit. Beyond theory, we design synthetic benchmarks that isolate these factors to complement prior results on real-world tasks and to empirically validate our predictions.

</details>

---

### 14. [Monotropic Artificial Intelligence: Toward a Cognitive Taxonomy of Domain-Specialized Language Models](https://arxiv.org/abs/2603.00350)

**基本信息**

- 🔗 arXiv: [`2603.00350`](https://arxiv.org/abs/2603.00350)
- 👥 作者: Antonio de Sousa Leitão Filho, Allan Kardec Duailibe Barros Filho, Fabrício Saul Lima 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00350.pdf)

**💡 相关性分析**

满足标准3：论文提出了“单otropic AI”这一概念框架，对AI研究中的通用性与专业性范式进行了深刻的综述和展望性讨论。这为化学信息学和质谱分析领域发展高度专业化、可靠的大模型或推理系统提供了重要的哲学依据和分类学参考，属于重要的相关讨论。

**📖 中文摘要**

这篇论文提出了“单otropic人工智能”的概念，即故意牺牲通用性以在狭窄限定领域内实现非凡精度的语言模型。论文借鉴了用于理解自闭症认知的单otropic理论，认为强烈的专业化代表了一种具有独特优势的替代认知架构，特别是在安全关键应用中。论文通过一个在Timoshenko梁分析上达到近乎完美性能、但在其领域外故意无能的模型进行了演示。这一框架直接挑战了“规模即一切”的AI研究范式，为“化学大模型”和“质谱结构推理”领域提供了一个重要的哲学和技术视角。它论证了发展高度专业化、深度领域知识模型的合法性和价值，这与构建用于分子设计、反应预测或高精度质谱解析的专家模型的目标高度一致。论文为化学领域发展“小而精”的专家模型提供了理论基础和概念框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The prevailing paradigm in artificial intelligence research equates progress with scale: larger models trained on broader datasets are presumed to yield superior capabilities. This assumption, while empirically productive for general-purpose applications, obscures a fundamental epistemological tension between breadth and depth of knowledge. We introduce the concept of \emph{Monotropic Artificial Intelligence} -- language models that deliberately sacrifice generality to achieve extraordinary precision within narrowly circumscribed domains. Drawing on the cognitive theory of monotropism developed to understand autistic cognition, we argue that intense specialization represents not a limitation but an alternative cognitive architecture with distinct advantages for safety-critical applications. We formalize the defining characteristics of monotropic models, contrast them with conventional polytropic architectures, and demonstrate their viability through Mini-Enedina, a 37.5-million-parameter model that achieves near-perfect performance on Timoshenko beam analysis while remaining deliberately incompetent outside its domain. Our framework challenges the implicit assumption that artificial general intelligence constitutes the sole legitimate aspiration of AI research, proposing instead a cognitive ecology in which specialized and generalist systems coexist complementarily.

</details>

---

### 15. [How Large Language Models Get Stuck: Early structure with persistent errors](https://arxiv.org/abs/2603.00359)

**基本信息**

- 🔗 arXiv: [`2603.00359`](https://arxiv.org/abs/2603.00359)
- 👥 作者: Alokesh Manna, William Snyder, Whitney Tabor
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00359.pdf)

**💡 相关性分析**

满足标准1：论文的核心是研究大模型在语言习得中形成并持续错误模式的内在机制。这一基础性研究对于理解和改进化学大模型、质谱结构推理模型的学习过程、避免早期偏见和错误固化具有直接的相关性和方法论价值。

**📖 中文摘要**

这篇论文通过训练OPT模型并评估其在BLiMP句法语义基准上的表现，研究了大型语言模型如何“卡住”——即在早期处理阶段就建立并持续保持错误的似然性分离。论文提出了“二元语法假说”，认为如果二元统计信息在训练早期使模型偏向错误的区分，学习过程就会表现出错误的固化。这项工作是理解和诊断大模型语言习得和泛化失败机制的基础研究。对于“化学大模型”和“质谱结构推理”模型而言，理解模型何时以及为何会学习到错误的模式或产生系统性偏差至关重要。例如，在质谱解析中，模型可能过早地依赖于某些常见的碎片模式而忽略更细微的证据。该研究提供的分析框架（结合语言理论和深度学习理论）和假设，可用于分析和改进化学领域模型的学习动态和鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Linguistic insights may help make Large Language Model (LLM) training more efficient. We trained Meta's OPT model on the 100M word BabyLM dataset, and evaluated it on the BLiMP benchmark, which consists of 67 classes, each defined by sentence pairs that differ in a targeted syntactic or semantic rule violation. We tested the model's preference for grammatical over ungrammatical sentences across training iterations and grammatical types. In nearly one-third of the BLiMP classes, OPT fails to consistently assign a higher likelihood to grammatical sentences, even after extensive training. When it fails, it often establishes a clear (erroneous) separation of the likelihoods at an early stage of processing and sustains this to the end of our training phase. We hypothesize that this mis-categorization is costly because it creates entrenched biases that must, eventually, be reversed in order for the model to perform well. We probe this phenomenon using a mixture of qualitative (based on linguistic theory and the theory of Deep Learning) and quantitative (based on numerical testing) assessments. Our qualitative assessments indicate that only some BLiMP tests are meaningful guides. We conclude by articulating a hypothesis, the Bigram Hypothesis, which claims that the learning process will exhibit erroneous entrenchment if bigram statistics bias the model toward wrong distinctions early in training, and we describe a method (in progress) of testing the hypothesis on appropriately selected BLiMP classes.

</details>

---

### 16. [Distribution-Aware Companding Quantization of Large Language Models](https://arxiv.org/abs/2603.00364)

**基本信息**

- 🔗 arXiv: [`2603.00364`](https://arxiv.org/abs/2603.00364)
- 👥 作者: Athul Radhakrishnan, Siddhant Mohan, Mahima Sachdeva
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00364.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进大型语言模型的训练方法，这直接关联到“化学大模型”主题中关于如何构建和优化用于化学领域的大规模基础模型或预训练模型。

**📖 中文摘要**

这篇论文提出了一种用于训练大型语言模型的多令牌预测方法，旨在提高样本效率和下游能力。虽然论文本身主要关注语言模型的通用训练方法，但其核心主题——通过改进训练目标来增强大型模型（如GPT和Llama）的能力——与“化学大模型”这一关注主题高度相关。论文探讨了如何通过修改训练损失函数来提升模型在代码生成和算法推理等任务上的性能，这为构建和优化面向化学领域的专用大模型（例如用于分子生成、性质预测或反应推理的模型）提供了重要的方法论参考。其提出的多令牌预测框架可以视为一种增强模型内部表示和推理能力的通用策略，可应用于化学信息学中的序列生成任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models such as GPT and Llama are trained with a next-token prediction loss. In this work, we suggest that training language models to predict multiple future tokens at once results in higher sample efficiency. More specifically, at each position in the training corpus, we ask the model to predict the following n tokens using n independent output heads, operating on top of a shared model trunk. Considering multi-token prediction as an auxiliary training task, we measure improved downstream capabilities with no overhead in training time for both code and natural language models. The method is increasingly useful for larger model sizes and keeps its appeal when training for multiple epochs. Gains are especially pronounced on generative benchmarks like coding, where our models consistently outperform strong baselines by several percentage points. Our 13B parameter models solves 12 % more problems on HumanEval and 17 % more on MBPP than comparable next-token models. Experiments on small algorithmic tasks demonstrate that multi-token prediction is favorable for the development of induction heads and algorithmic reasoning capabilities. As an additional benefit, models trained with 4-token prediction are up to 3X times faster at inference, even with large batch sizes.

</details>

---

### 17. [PointAlign: Feature-Level Alignment Regularization for 3D Vision-Language Models](https://arxiv.org/abs/2603.00412)

**基本信息**

- 🔗 arXiv: [`2603.00412`](https://arxiv.org/abs/2603.00412)
- 👥 作者: Yuanhao Su, Shaofeng Zhang, Xiaosong Jia 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00412.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于3D视觉语言模型的特征对齐方法，以增强模型对3D几何结构的理解。这直接关联到“化学大模型”主题中处理3D分子结构表示和推理的需求，也为“质谱结构推理”中可能涉及的三维结构推断提供了潜在的技术借鉴。

**📖 中文摘要**

这篇论文针对3D视觉语言模型（3D VLMs）开发中面临的3D-文本配对数据稀缺问题，提出了一种名为PointAlign的特征级对齐正则化方法。该方法通过约束大型语言模型（LLM）内部的中间点云令牌与视觉输入令牌保持一致，来保留细粒度的3D几何语义信息，防止几何信息在语言建模过程中退化。论文在ModelNet40和Objaverse等3D数据集上进行了广泛实验，证明了其在分类和描述生成任务上的有效性。这项工作为构建能够理解和推理3D结构（如分子三维构象）的多模态大模型提供了重要的技术思路和方法，与“化学大模型”中处理3D分子表示和“质谱结构推理”中可能需要结合3D结构信息的需求相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of 3D Vision-Language Models (VLMs), crucial for applications in robotics, autonomous driving, and augmented reality, is severely constrained by the scarcity of paired 3D-text data. Existing methods rely solely on next-token prediction loss, using only language tokens for supervision. This results in inefficient utilization of limited 3D data and leads to a significant degradation and loss of valuable geometric information in intermediate representations. To address these limitations, we propose {\mname}, a novel feature-level alignment regularization method. {\mname} explicitly supervises intermediate point cloud tokens to preserve fine-grained 3D geometric-semantic information throughout the language modeling process. Specifically, we constrain the intermediate point cloud tokens within the LLM to align with visual input tokens via a consistency loss. By training only a lightweight alignment projector and LoRA adapters, {\mname} achieves explicit feature-level supervision with minimal computational overhead, effectively preventing geometric degradation. Extensive experiments on ModelNet40 and Objaverse datasets demonstrate that our method achieves \textbf{2.08} pp improvement on average for classification tasks, with a substantial \textbf{7.50} pp gain on the challenging open-vocabulary Objaverse classification task and \textbf{4.88} pp improvement on 3D object captioning evaluated by Qwen2-72B-Instruct, validating the effectiveness of {\mname}. Code is publicly available at \href{ this https URL }{ this https URL }.

</details>

---

### 18. [Taxonomy-Aware Representation Alignment for Hierarchical Visual Recognition with Large Multimodal Models](https://arxiv.org/abs/2603.00431)

**基本信息**

- 🔗 arXiv: [`2603.00431`](https://arxiv.org/abs/2603.00431)
- 👥 作者: Hulingxiao He, Zhi Tan, Yuxin Peng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00431.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将层次化的分类学知识整合到大型多模态模型中，以增强其对已知和新类别物体的识别与推理能力。这直接关联到“化学大模型”主题中关于模型需要理解和推理化学物质层次化分类、官能团关系等复杂知识体系的需求。

**📖 中文摘要**

这篇论文提出了Taxonomy-Aware Representation Alignment (TARA)方法，旨在将分类学知识注入大型多模态模型（LMMs），以提升其在层次视觉识别（HVR）任务上的性能，特别是对于训练集中未见过的新类别。TARA利用生物学基础模型（BFMs）中编码的丰富层次关系，通过层次对比学习，将视觉特征表示与BFMs的表示对齐，从而鼓励模型提取在分类学树中结构良好的判别性视觉线索。该方法在复杂的生物分类学任务上展示了可靠识别已知和新颖类别的能力。这项工作为构建能够理解复杂科学分类体系（如化学物质分类、代谢通路）的大模型提供了关键技术，与“化学大模型”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A high-performing, general-purpose visual understanding model should map visual inputs to a taxonomic tree of labels, identify novel categories beyond the training set for which few or no publicly available images exist. Large Multimodal Models (LMMs) have achieved remarkable progress in fine-grained visual recognition (FGVR) for known categories. However, they remain limited in hierarchical visual recognition (HVR) that aims at predicting consistent label paths from coarse to fine categories, especially for novel categories. To tackle these challenges, we propose Taxonomy-Aware Representation Alignment (TARA), a simple yet effective strategy to inject taxonomic knowledge into LMMs. TARA leverages representations from biology foundation models (BFMs) that encode rich biological relationships through hierarchical contrastive learning. By aligning the intermediate representations of visual features with those of BFMs, LMMs are encouraged to extract discriminative visual cues well structured in the taxonomy tree. Additionally, we align the representations of the first answer token with the ground-truth label, flexibly bridging the gap between contextualized visual features and categories of varying granularity according to user intent. Experiments demonstrate that TARA consistently enhances LMMs' hierarchical consistency and leaf node accuracy, enabling reliable recognition of both known and novel categories within complex biological taxonomies. Code is available at this https URL .

</details>

---

### 19. [Mamba-CAD: State Space Model For 3D Computer-Aided Design Generative Modeling](https://arxiv.org/abs/2603.00439)

**基本信息**

- 🔗 arXiv: [`2603.00439`](https://arxiv.org/abs/2603.00439)
- 👥 作者: Xueyang Li, Yunzhong Lou, Yu Song 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00439.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用先进的序列模型（Mamba）进行复杂三维结构的生成建模。这直接关联到“化学大模型”和“质谱结构推理”主题中关于分子结构（可视为一种特殊的三维/二维图形序列）的生成、表示和推理任务。其方法对处理化学信息学中的序列数据（如SMILES）具有直接的借鉴意义。

**📖 中文摘要**

这篇论文提出了Mamba-CAD，一个基于状态空间模型（Mamba架构）的自监督生成模型，用于工业中复杂的三维计算机辅助设计（CAD）模型的生成建模。CAD生成建模在工业中有长期应用，而工业CAD模型通常由冗长的参数化CAD序列定义。Mamba-CAD采用编码器-解码器框架，并配合CAD重建任务进行预训练，以建模CAD模型的潜在表示，然后利用学习到的表示通过生成对抗网络生成假的CAD表示，最终通过解码器恢复为参数化CAD序列。为了训练模型，作者创建了一个包含77,078个具有长参数序列的CAD模型的新数据集。这项工作展示了先进序列模型（Mamba）在复杂结构化数据（如CAD序列）生成中的应用，为“化学大模型”中处理类似结构化序列数据（如SMILES字符串、反应SMILES、质谱碎片序列）的生成和表示学习提供了重要的方法论参考和架构灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computer-Aided Design (CAD) generative modeling has a strong and long-term application in the industry. Recently, the parametric CAD sequence as the design logic of an object has been widely mined by sequence models. However, the industrial CAD models, especially in component objects, are fine-grained and complex, requiring a longer parametric CAD sequence to define. To address the problem, we introduce Mamba-CAD, a self-supervised generative modeling for complex CAD models in the industry, which can model on a longer parametric CAD sequence. Specifically, we first design an encoder-decoder framework based on a Mamba architecture and pair it with a CAD reconstruction task for pre-training to model the latent representation of CAD models; and then we utilize the learned representation to guide a generative adversarial network to produce the fake representation of CAD models, which would be finally recovered into parametric CAD sequences via the decoder of MambaCAD. To train Mamba-CAD, we further create a new dataset consisting of 77,078 CAD models with longer parametric CAD sequences. Comprehensive experiments are conducted to demonstrate the effectiveness of our model under various evaluation metrics, especially in the generation length of valid parametric CAD sequences. The code and dataset can be achieved from this https URL .

</details>

---

### 20. [Rooted Absorbed Prefix Trajectory Balance with Submodular Replay for GFlowNet Training](https://arxiv.org/abs/2603.00454)

**基本信息**

- 🔗 arXiv: [`2603.00454`](https://arxiv.org/abs/2603.00454)
- 👥 作者: Xi Wang, Wenbo Lu, Shengjie Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00454.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进生成流网络（GFlowNets）在微调大型语言模型进行序列生成（特别是分子SMILES字符串生成）时的训练目标和方法，以解决模式崩溃问题。这直接且核心地围绕“化学大模型”主题中的分子生成与优化任务。

**📖 中文摘要**

这篇论文针对生成流网络（GFlowNets）在微调大型语言模型以近似奖励比例后验时容易出现的模式崩溃（如前缀崩溃和长度偏差）问题，提出了Rooted absorbed prefix Trajectory Balance (RapTB)目标函数和SubM回放策略。RapTB通过将子轨迹监督锚定在根节点，并利用吸收后缀的备份将终端奖励传播到中间前缀，提供了密集的前缀级学习信号。SubM则是一种子模回放刷新策略，旨在促进高奖励和多样性。论文在基于SMILES字符串的LLM分子生成任务上进行了实证评估。这项工作直接解决了使用生成流网络和大型语言模型进行分子生成时的优化挑战，与“化学大模型”主题中的分子生成和优化子领域高度相关，并为相关方法提供了改进思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative Flow Networks (GFlowNets) enable fine-tuning large language models to approximate reward-proportional posteriors, but they remain prone to mode collapse, manifesting as prefix collapse and length bias. We attribute this to two factors: (i) weak credit assignment to early prefixes, and (ii) biased replay that induces a shifted, non-representative training flow distribution. We propose Rooted absorbed prefix Trajectory Balance RapTB, an objective that anchors subtrajectory supervision at the root and propagates terminal rewards to intermediate prefixes via absorbed suffix-based backups, providing dense prefix-level learning signals. To mitigate replay-induced distribution shift, we further introduce SubM, a submodular replay refresh strategy that promotes both high reward and diversity. Empirically, on tasks such as molecule generation with LLM using SMILES strings, RapTB combined with SubM consistently improves optimization performance and molecular diversity while preserving high validity.

</details>

---

### 21. [MED-COPILOT: A Medical Assistant Powered by GraphRAG and Similar Patient Case Retrieval](https://arxiv.org/abs/2603.00460)

**基本信息**

- 🔗 arXiv: [`2603.00460`](https://arxiv.org/abs/2603.00460)
- 👥 作者: Shuheng Chen, Namratha Patil, Haonan Pan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00460.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是构建一个整合了结构化知识（知识图谱）和案例数据检索的临床决策支持系统，这为“化学大模型”和“质谱结构推理”领域提供了构建增强型AI助手的方法论框架（标准1）。同时，其工作中构建知识图谱和病例数据库的流程，也为相关领域创建高质量、结构化的数据集和资源提供了参考（标准2）。

**📖 中文摘要**

这篇论文提出了MED-COPILOT，一个用于临床决策支持的交互式系统，它结合了基于指南的GraphRAG检索和混合语义-关键词的相似患者病例检索，以支持透明和基于证据的临床推理。该系统从WHO和NICE指南构建结构化知识图谱，并对一个包含36,000个病例的相似患者数据库（源自MIMIC-IV笔记和Synthea生成记录）进行检索。论文在临床笔记完成和医学问答任务上评估了该框架，证明其性能优于参数化LLM基线和标准RAG。虽然该工作聚焦于医学领域，但其核心方法——整合结构化领域知识（知识图谱）和实例数据（相似病例）到大型语言模型的工作流程中，以增强推理的准确性和可解释性——为“化学大模型”和“质谱结构推理”领域提供了极具价值的范式参考。例如，可以类似地构建化学知识图谱（如反应规则、化合物性质）和质谱数据库检索系统，来增强化学大模型在化合物鉴定、反应预测等任务上的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Clinical decision-making requires synthesizing heterogeneous evidence, including patient histories, clinical guidelines, and trajectories of comparable cases. While large language models (LLMs) offer strong reasoning capabilities, they remain prone to hallucinations and struggle to integrate long, structured medical documents. We present MED-COPILOT, an interactive clinical decision-support system designed for clinicians and medical trainees, which combines guideline-grounded GraphRAG retrieval with hybrid semantic-keyword similar-patient retrieval to support transparent and evidence-aware clinical reasoning. The system builds a structured knowledge graph from WHO and NICE guidelines, applies community-level summarization for efficient retrieval, and maintains a 36,000-case similar-patient database derived from SOAP-normalized MIMIC-IV notes and Synthea-generated records. We evaluate our framework on clinical note completion and medical question answering, and demonstrate that it consistently outperforms parametric LLM baselines and standard RAG, improving both generation fidelity and clinical reasoning accuracy. The full system is available at this https URL , enabling users to inspect retrieved evidence, visualize token-level similarity contributions, and conduct guided follow-up analysis. Our results demonstrate a practical and interpretable approach to integrating structured guideline knowledge with patient-level analogical evidence for clinical LLMs.

</details>

---

### 22. [Benchmarking Few-shot Transferability of Pre-trained Models with Improved Evaluation Protocols](https://arxiv.org/abs/2603.00478)

**基本信息**

- 🔗 arXiv: [`2603.00478`](https://arxiv.org/abs/2603.00478)
- 👥 作者: Xu Luo, Ji Zhang, Lianli Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00478.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了一个用于评估少样本迁移学习的综合性基准FEWTRANS（标准2），并对预训练模型迁移的关键因素进行了深入分析，这些讨论和结论对于“化学大模型”领域如何选择和微调模型以应对数据稀缺问题具有重要的综述和展望价值（标准3）。

**📖 中文摘要**

这篇论文建立了FEWTRANS，一个包含10个多样化数据集的综合性少样本迁移学习基准，并提出了超参数集成（HPE）协议来克服数据稀缺机制中的“验证集幻觉”。论文通过实证研究发现，预训练模型的选择是性能的主导因素，而许多复杂的迁移方法相对于简单的全参数微调基线带来的实际优势微乎其微。论文还通过机制分析解释了全参数微调的成功之处。此外，论文量化了多模态模型在专业领域（由于语言稀有性）的性能崩溃。虽然论文主题是通用的少样本迁移学习，但其对预训练模型重要性、微调策略有效性的深入分析和建立的基准，对于“化学大模型”领域的研究具有重要的指导意义。化学领域常面临标注数据稀缺的问题，因此如何有效地将通用大模型或少样本学习技术迁移到化学特定任务（如质谱解析、分子性质预测）是核心挑战。FEWTRANS基准和其分析结论为评估和开发适用于化学领域的少样本迁移方法提供了重要的评估工具和设计原则。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Few-shot transfer has been revolutionized by stronger pre-trained models and improved adaptation this http URL , there lacks a unified, rigorous evaluation protocol that is both challenging and realistic for real-world usage. In this work, we establish FEWTRANS, a comprehensive benchmark containing 10 diverse datasets, and propose the Hyperparameter Ensemble (HPE) protocol to overcome the "validation set illusion" in data-scarce regimes. Our empirical findings demonstrate that the choice of pre-trained model is the dominant factor for performance, while many sophisticated transfer methods offer negligible practical advantages over a simple full-parameter fine-tuning baseline. To explain this surprising effectiveness, we provide an in-depth mechanistic analysis showing that full fine-tuning succeeds via distributed micro-adjustments and more flexible reshaping of high-level semantic presentations without suffering from overfitting. Additionally, we quantify the performance collapse of multimodal models in specialized domains as a result of linguistic rarity using adjusted Zipf frequency scores. By releasing FEWTRANS, we aim to provide a rigorous "ruler" to streamline reproducible advances in few-shot transfer learning research. We make the FEWTRANS benchmark publicly available at this https URL .

</details>

---

### 23. [Bridge Matching Sampler: Scalable Sampling via Generalized Fixed-Point Diffusion Matching](https://arxiv.org/abs/2603.00530)

**基本信息**

- 🔗 arXiv: [`2603.00530`](https://arxiv.org/abs/2603.00530)
- 👥 作者: Denis Blessing, Lorenz Richter, Julius Berner 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00530.pdf)

**💡 相关性分析**

满足标准2：提出的Bridge Matching Sampler (BMS)是一种用于从复杂分布（包括高维分子基准）中采样的可扩展方法。该方法为化学大模型（特别是生成模型）的构建和训练提供了关键的采样工具和算法资源。

**📖 中文摘要**

本文提出了一种名为Bridge Matching Sampler (BMS)的新型采样方法，用于从非归一化密度中进行采样。该方法通过广义的固定点扩散匹配，学习任意先验分布和目标分布之间的随机传输映射。论文在包括高维分子基准测试在内的复杂合成密度上进行了实证评估，证明了该方法能够在保持模式多样性的同时实现前所未有的规模采样，并取得了最先进的结果。该方法的核心——学习从先验到目标的映射并进行采样——与化学信息学中分子生成和性质预测等任务高度相关，可被视为构建或服务于化学大模型（如生成模型）的基础工具或方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling from unnormalized densities using diffusion models has emerged as a powerful paradigm. However, while recent approaches that use least-squares `matching' objectives have improved scalability, they often necessitate significant trade-offs, such as restricting prior distributions or relying on unstable optimization schemes. By generalizing these methods as special forms of fixed-point iterations rooted in Nelson's relation, we develop a new method that addresses these limitations, called Bridge Matching Sampler (BMS). Our approach enables learning a stochastic transport map between arbitrary prior and target distributions with a single, scalable, and stable objective. Furthermore, we introduce a damped variant of this iteration that incorporates a regularization term to mitigate mode collapse and further stabilize training. Empirically, we demonstrate that our method enables sampling at unprecedented scales while preserving mode diversity, achieving state-of-the-art results on complex synthetic densities and high-dimensional molecular benchmarks.

</details>

---

### 24. [Enhancing Molecular Property Predictions by Learning from Bond Modelling and Interactions](https://arxiv.org/abs/2603.00568)

**基本信息**

- 🔗 arXiv: [`2603.00568`](https://arxiv.org/abs/2603.00568)
- 👥 作者: Yunqing Liu, Yi Zhou, Wenqi Fan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00568.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分子表示学习，这是化学信息学和化学大模型（用于分子性质预测、生成等）的基础。其提出的DeMol框架通过显式建模化学键信息，旨在提高分子属性预测的准确性，直接服务于化学大模型的构建。

**📖 中文摘要**

本文提出了DeMol，一个用于分子表示学习的双图框架。该框架的动机源于信息论分析，证明了从键中心视角能获得信息增益。DeMol通过并行的原子中心和键中心通道显式建模分子，并通过多尺度双螺旋块学习复杂的原子-原子、原子-键和键-键相互作用。此外，框架还引入了基于共价半径的正则化项以增强几何一致性。在包括PCQM4Mv2、OC20 IS2RE、QM9和MoleculeNet在内的多个基准测试上的综合评估表明，DeMol的性能超越了现有方法，达到了新的最先进水平。这项工作明确强调了在分子机器学习中建模键信息和相互作用的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecule representation learning is crucial for understanding and predicting molecular properties. However, conventional atom-centric models, which treat chemical bonds merely as pairwise interactions, often overlook complex bond-level phenomena like resonance and stereoselectivity. This oversight limits their predictive accuracy for nuanced chemical behaviors. To address this limitation, we introduce \textbf{DeMol}, a dual-graph framework whose architecture is motivated by a rigorous information-theoretic analysis demonstrating the information gain from a bond-centric perspective. DeMol explicitly models molecules through parallel atom-centric and bond-centric channels. These are synergistically fused by multi-scale Double-Helix Blocks designed to learn intricate atom-atom, atom-bond, and bond-bond interactions. The framework's geometric consistency is further enhanced by a regularization term based on covalent radii to enforce chemically plausible structures. Comprehensive evaluations on diverse benchmarks, including PCQM4Mv2, OC20 IS2RE, QM9, and MoleculeNet, show that DeMol establishes a new state-of-the-art, outperforming existing methods. These results confirm the superiority of explicitly modelling bond information and interactions, paving the way for more robust and accurate molecular machine learning.

</details>

---

### 25. [From Literature to Hypotheses: An AI Co-Scientist System for Biomarker-Guided Drug Combination Hypothesis Generation](https://arxiv.org/abs/2603.00612)

**基本信息**

- 🔗 arXiv: [`2603.00612`](https://arxiv.org/abs/2603.00612)
- 👥 作者: Raneen Younis, Suvinava Basak, Lukas Chavez 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00612.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是构建一个AI辅助的科学发现系统，该系统整合多源数据（生物医学数据库和文献）构建知识图谱并进行推理，以生成药物组合假设。这直接涉及化学信息学中的核心任务（如药物发现），并提供了一个可用于相关主题（如化学大模型在药物设计中的应用）的数据整合与推理工具框架。

**📖 中文摘要**

本文介绍了AI Co-Scientist (CoDHy)，一个用于癌症研究中生物标志物引导的药物组合假设生成的交互式、人在回路系统。该系统将结构化的生物医学数据库和非结构化的文献证据整合到一个特定任务的知识图谱中，作为基于图的推理和假设构建的基础。它结合知识图谱嵌入和基于代理的推理来生成、验证和排序候选药物组合，同时将每个假设明确地建立在可检索的证据之上。通过基于Web的界面，用户可以配置科学背景、检查中间结果并迭代地完善假设，从而实现透明且由研究人员引导的探索，而非自动化决策。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of biomedical literature and curated databases has made it increasingly difficult for researchers to systematically connect biomarker mechanisms to actionable drug combination hypotheses. We present AI Co-Scientist (CoDHy), an interactive, human-in-the-loop system for biomarker-guided drug combination hypothesis generation in cancer research. CoDHy integrates structured biomedical databases and unstructured literature evidence into a task-specific knowledge graph, which serves as the basis for graph-based reasoning and hypothesis construction. The system combines knowledge graph embeddings with agent-based reasoning to generate, validate, and rank candidate drug combinations, while explicitly grounding each hypothesis in retrievable evidence. Through a web-based interface, users can configure the scientific context, inspect intermediate results, and iteratively refine hypotheses, enabling transparent and researcher-steerable exploration rather than automated decision-making. We demonstrate CoDHy as a system for exploratory hypothesis generation and decision support in translational oncology, highlighting its design, interaction workflow, and practical use cases.

</details>

---

### 26. [SSKG Hub: An Expert-Guided Platform for LLM-Empowered Sustainability Standards Knowledge Graphs](https://arxiv.org/abs/2603.00669)

**基本信息**

- 🔗 arXiv: [`2603.00669`](https://arxiv.org/abs/2603.00669)
- 👥 作者: Chaoyue He, Xin Zhou, Xinjia Yu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00669.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个利用大语言模型从复杂文本（可持续发展标准）中自动化构建知识图谱的完整框架和平台（SSKG Hub）。虽然领域特定，但其核心方法——LLM驱动的信息提取、三元组解析和知识图谱构建——为化学信息学领域（如从科学文献中自动提取化学实体、反应和关系以构建化学知识图谱）提供了通用的工具、资源和方法论参考。

**📖 中文摘要**

本文介绍了SSKG Hub（可持续发展标准知识图谱中心），一个研究原型和交互式Web平台，它通过一个以LLM为中心、专家引导的流程，将冗长、术语密集且高度交叉引用的可持续发展披露标准（如GRI、SASB）转化为可审计的知识图谱。该系统集成了自动标准识别、可配置分块、标准特定提示、稳健的三元组解析以及具有细粒度审计元数据的可追溯Neo4j存储。LLM提取产生一个可追溯的草案知识图谱，经过专家评审、整理后，通过元专家裁决正式提升为认证知识图谱。该平台支持知识图谱探索、三元组级证据追溯、跨知识图谱融合以及知识图谱驱动的任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sustainability disclosure standards (e.g., GRI, SASB, TCFD, IFRS S2) are comprehensive yet lengthy, terminology-dense, and highly cross-referential, hindering structured analysis and downstream use. We present SSKG Hub (Sustainability Standards Knowledge Graph Hub), a research prototype and interactive web platform that transforms standards into auditable knowledge graphs (KGs) through an LLM-centered, expert-guided pipeline. The system integrates automatic standard identification, configurable chunking, standard-specific prompting, robust triple parsing, and provenance-aware Neo4j storage with fine-grained audit metadata. LLM extraction produces a provenance-linked Draft KG, which is reviewed, curated, and formally promoted to a Certified KG through meta-expert adjudication. A role-based governance framework covering read-only guest access, expert review and CRUD operations, meta-expert certification, and administrative oversight ensures traceability and accountability across draft and certified states. Beyond graph exploration and triple-level evidence tracing, SSKG Hub supports cross-KG fusion, KG-driven tasks, and dedicated modules for insights and curated resources. We validate the platform through a comprehensive expert-led KG review case study that demonstrates end-to-end curation and quality assurance. The web application is publicly available at this http URL .

</details>

---

### 27. [Identifying and Characterising Response in Clinical Trials: Development and Validation of a Machine Learning Approach in Colorectal Cancer](https://arxiv.org/abs/2603.00757)

**基本信息**

- 🔗 arXiv: [`2603.00757`](https://arxiv.org/abs/2603.00757)
- 👥 作者: Adam Marcus, Paul Agapow
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00757.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种机器学习方法来分析临床试验数据，以识别对治疗有不同反应的患者亚组，这直接关联到化学信息学中利用数据驱动模型进行预测和推理的核心主题。

**📖 中文摘要**

本文提出了一种结合部分条件建模和基于虚拟双生子方法的机器学习方法，用于识别和表征临床试验中对治疗有不同反应的患者亚组。该方法能够处理临床试验中常见的重复测量数据，并估计时间特异性的治疗反应。作者在合成数据和转移性结直肠癌的临床试验数据上进行了评估，以评估帕尼单抗的治疗效果。该方法可以适应动态治疗反应，同时在固定反应场景下可能比现有方法表现更好。当应用于临床数据时，该方法识别出的重要因素（如基因突变、转移部位和种族）与文献报道一致。这项工作展示了机器学习在精准医疗和药物反应预测中的应用，与化学信息学中利用数据模型预测分子性质或生物活性的目标高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Precision medicine promises to transform health care by offering individualised treatments that dramatically improve clinical outcomes. A necessary prerequisite is to identify subgroups of patients who respond differently to different therapies. Current approaches are limited to static measures of treatment success, neglecting the repeated measures found in most clinical trials. Our approach combines the concept of partly conditional modelling with treatment effect estimation based on the Virtual Twins method. The resulting time-specific responses to treatment are characterised using survLIME, an extension of Local Interpretable Model-agnostic Explanations (LIME) to survival data. Performance was evaluated using synthetic data and applied to clinical trials examining the effectiveness of panitumumab to treat metastatic colorectal cancer. An area under the receiver operating characteristic curve (AUC) of 0.77 for identifying fixed responders was achieved in a 1000 patient simulation. When considering dynamic responders, partly conditional modelling increased the AUC from 0.597 to 0.685. Applying the approach to colorectal cancer trials found genetic mutations, sites of metastasis, and ethnicity as important factors for response to treatment. Our approach can accommodate a dynamic response to treatment while potentially providing better performance than existing methods in instances of a fixed response to treatment. When applied to clinical data we attain results consistent with the literature.

</details>

---

### 28. [MultiPUFFIN: A Multimodal Domain-Constrained Foundation Model for Molecular Property Prediction of Small Molecules](https://arxiv.org/abs/2603.00857)

**基本信息**

- 🔗 arXiv: [`2603.00857`](https://arxiv.org/abs/2603.00857)
- 👥 作者: Idelfonso B. R. Nogueira, Carine M. Rebelloa, Mumin Enis Leblebici 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00857.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是开发一个用于分子多任务性质预测的化学大模型（MultiPUFFIN），这直接围绕“化学大模型”主题。同时，论文提出的模型架构、训练方法和在特定数据集上的验证，为分子性质预测领域提供了新的工具和资源。

**📖 中文摘要**

本文提出了MultiPUFFIN，一个用于小分子多任务物化性质预测的多模态、领域约束的基础模型。该模型融合了SMILES字符串、分子图和3D几何结构等多种分子表示，并通过门控跨模态注意力进行编码。其创新之处在于预测头中嵌入了已知的热力学关联方程（如Wagner、Andrade等）作为归纳偏置，以确保预测的热力学一致性。模型在包含近4万行数据、涵盖9种热物理性质的数据集上进行训练。尽管参数量仅为3500万，且训练数据远少于传统预训练模型（如ChemBERTa-2），MultiPUFFIN在具有挑战性的支架分割测试集上取得了优异的预测性能（平均R²=0.716），显著优于微调后的基线模型。结果表明，多模态编码和领域知识引导能大幅降低对数据和算力的需求。该工作为分子性质预测提供了一个高效、一致且可解释的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting physicochemical properties across chemical space is vital for chemical engineering, drug discovery, and materials science. Current molecular foundation models lack thermodynamic consistency, while domain-informed approaches are limited to single properties and small datasets. We introduce MultiPUFFIN, a domain-constrained multimodal foundation model addressing both limitations simultaneously. MultiPUFFIN features: (i) an encoder fusing SMILES, graphs, and 3D geometries via gated cross-modal attention, alongside experimental condition and descriptor encoders; (ii) prediction heads embedding established correlations (e.g., Wagner, Andrade, van't Hoff, and Shomate equations) as inductive biases to ensure thermodynamic consistency; and (iii) a two-stage multi-task training this http URL prior frameworks, MultiPUFFIN predicts nine thermophysical properties simultaneously. It is trained on a multi-source dataset of 37,968 unique molecules (40,904 rows). With roughly 35 million parameters, MultiPUFFIN achieves a mean $R^2 = 0.716$ on a challenging scaffold-split test set of 8,877 molecules. Compared to ChemBERTa-2 (pre-trained on 77 million molecules), MultiPUFFIN outperforms the fine-tuned baseline across all nine properties despite using 2000x fewer training molecules. Advantages are strikingly apparent for temperature-dependent properties, where ChemBERTa-2 lacks the architectural capacity to incorporate thermodynamic this http URL results demonstrate that multimodal encoding and domain-informed biases substantially reduce data and compute requirements compared to brute-force pre-training. Furthermore, MultiPUFFIN handles missing modalities and recovers meaningful thermodynamic parameters without explicit supervision. Systematic ablation studies confirm the property-specific benefits of these domain-informed prediction heads.

</details>

---

### 29. [Active Flow Matching](https://arxiv.org/abs/2603.00877)

**基本信息**

- 🔗 arXiv: [`2603.00877`](https://arxiv.org/abs/2603.00877)
- 👥 作者: Yashvir S. Grewal, Daniel M. Steinberg, Thang D. Bui 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00877.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的生成模型框架（主动流匹配，AFM），用于在线黑盒优化任务，如蛋白质和小分子设计。这直接关联到化学信息学中利用生成模型进行分子设计与优化的核心主题，是化学大模型在生成任务上的一个重要应用和拓展。

**📖 中文摘要**

本文提出了主动流匹配（AFM），这是一种将变分目标重新表述为在流轨迹上的条件端点分布上操作的新方法。它使得能够基于梯度引导流模型向高适应度区域演化，同时保持变分搜索分布（VSD）和自适应采样条件（CbAS）等原则性在线黑盒优化框架的严谨性。作者推导了使用自归一化重要性采样的前向和反向KL散度变体。在一系列在线蛋白质和小分子设计任务中，前向KL AFM与最先进的基线方法相比始终具有竞争力，证明了其在严格实验预算下的有效探索-利用平衡。这项工作将离散扩散和流匹配生成模型与原则性的优化框架相结合，为分子设计等领域的定向生成提供了新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete diffusion and flow matching models capture complex, non-additive and non-autoregressive structure in high-dimensional objective landscapes through parallel, iterative refinement. However, their implicit generative nature precludes direct integration with principled variational frameworks for online black-box optimisation, such as variational search distributions (VSD) and conditioning by adaptive sampling (CbAS). We introduce Active Flow Matching (AFM), which reformulates variational objectives to operate on conditional endpoint distributions along the flow, enabling gradient-based steering of flow models toward high-fitness regions while preserving the rigour of VSD and CbAS. We derive forward and reverse Kullback-Leibler (KL) variants using self-normalised importance sampling. Across a suite of online protein and small molecule design tasks, forward-KL AFM consistently performs competitively compared to state-of-the-art baselines, demonstrating effective exploration-exploitation under tight experimental budgets.

</details>

---

### 30. [Forgetting is Competition: Rethinking Unlearning as Representation Interference in Diffusion Models](https://arxiv.org/abs/2603.00975)

**基本信息**

- 🔗 arXiv: [`2603.00975`](https://arxiv.org/abs/2603.00975)
- 👥 作者: Ashutosh Ranjan, Vivek Srivastava, Shirish Karande 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00975.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对生成模型（扩散模型）的精确概念移除（遗忘/擦除）技术。这与化学信息学中构建可控、安全的化学大模型（需要遗忘不良分子模式或受保护结构）的核心主题直接相关。

**📖 中文摘要**

本文提出了一种用于文本到图像扩散模型的“外科手术式”遗忘方法SurgUn，旨在精确移除特定的视觉概念（如受版权保护的内容、艺术家风格等）。该方法基于“追溯性干扰”理论，通过在权重空间进行针对性更新，诱导目标概念的表征路径发生干扰，从而实现对该概念的聚焦性破坏，同时保留不相关的能力。论文在多种模型架构（如Stable Diffusion v1.5, SDXL, SANA）上验证了其高精度遗忘能力。这项研究对于化学信息学领域具有重要意义，例如在构建用于分子生成的化学大模型时，可能需要安全地遗忘某些具有毒性或专利限制的分子子结构，同时保持模型整体的生成能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unlearning in text-to-image diffusion models often leads to uneven concept removal and unintended forgetting of unrelated capabilities. This complicates tasks such as copyright compliance, protected data mitigation, artist opt-outs, and policy-driven content updates. As models grow larger and adopt more diverse architectures, achieving precise and selective unlearning while preserving generative quality becomes increasingly challenging. We introduce SurgUn (pronounced as Surgeon), a surgical unlearning method that applies targeted weight-space updates to remove specific visual concepts in text-conditioned diffusion models. Our approach is motivated by retroactive interference theory, which holds that newly acquired memories can overwrite, suppress, or impede access to prior ones by competing for shared representational pathways. We adapt this principle to diffusion models by inducing retroactive concept interference, enabling focused destabilization of only the target concept while preserving unrelated capabilities through a novel training paradigm. SurgUn achieves high-precision unlearning across diverse settings. It performs strongly on compact U-Net based models such as Stable Diffusion v1.5, scales effectively to the larger U-Net architecture SDXL, and extends to SANA, representing an underexplored Diffusion Transformer based architecture for unlearning.

</details>

---

### 31. [EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization](https://arxiv.org/abs/2603.00978)

**基本信息**

- 🔗 arXiv: [`2603.00978`](https://arxiv.org/abs/2603.00978)
- 👥 作者: Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00978.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对下一代扩散模型（包括图像和视频）的概念擦除技术。这与确保化学大模型生成内容的安全性、合规性，以及从模型中移除特定化学实体知识的需求直接相关。

**📖 中文摘要**

本文提出了EraseAnything++，一个用于图像和视频扩散模型（特别是基于流匹配和Transformer架构的现代模型，如Stable Diffusion v3, Flux, OpenSora）的统一概念擦除框架。该框架将概念擦除形式化为一个约束多目标优化问题，明确平衡概念移除与生成效用保留。通过引入基于隐式梯度手术的高效效用保留遗忘策略，并结合LoRA参数调优与注意力级正则化，该方法能够在空间和时间维度上一致地锚定和传播擦除效果。实验表明，该方法在擦除有效性、生成保真度和时间一致性方面显著优于先前方法。该技术对于化学大模型的安全部署至关重要，例如需要从预训练模型中移除特定危险化合物或受管制物质的知识。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Removing undesired concepts from large-scale text-to-image (T2I) and text-to-video (T2V) diffusion models while preserving overall generative quality remains a major challenge, particularly as modern models such as Stable Diffusion v3, Flux, and OpenSora employ flow-matching and transformer-based architectures and extend to long-horizon video generation. Existing concept erasure methods, designed for earlier T2I/T2V models, often fail to generalize to these paradigms. To address this issue, we propose EraseAnything++, a unified framework for concept erasure in both image and video diffusion models with flow-matching objectives. Central to our approach is formulating concept erasure as a constrained multi-objective optimization problem that explicitly balances concept removal with preservation of generative utility. To solve the resulting conflicting objectives, we introduce an efficient utility-preserving unlearning strategy based on implicit gradient surgery. Furthermore, by integrating LoRA-based parameter tuning with attention-level regularization, our method anchors erasure on key visual representations and propagates it consistently across spatial and temporal dimensions. In the video setting, we further enhance consistency through an anchor-and-propagate mechanism that initializes erasure on reference frames and enforces it throughout subsequent transformer layers, thereby mitigating temporal drift. Extensive experiments on both image and video benchmarks demonstrate that EraseAnything++ substantially outperforms prior methods in erasure effectiveness, generative fidelity, and temporal consistency, establishing a new state of the art for concept erasure in next-generation diffusion models.

</details>

---

### 32. [Compensation-free Machine Unlearning in Text-to-Image Diffusion Models by Eliminating the Mutual Information](https://arxiv.org/abs/2603.00992)

**基本信息**

- 🔗 arXiv: [`2603.00992`](https://arxiv.org/abs/2603.00992)
- 👥 作者: Xinwen Cheng, Jingyuan Zhang, Zhehao Huang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00992.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕如何从生成模型中移除特定知识（概念擦除），这是构建可控、安全的化学大模型（如用于分子生成的扩散模型）的关键技术之一。

**📖 中文摘要**

本文针对扩散模型中的机器遗忘（概念擦除）问题，提出了一种无需补偿的精确概念擦除方法MiM-MU。该方法通过最小化模型与待擦除概念之间的互信息来实现精确的知识移除，旨在将对其他概念生成质量的影响降至最低。与依赖事后补偿（如重新吸收剩余数据或约束与预训练模型的差异）的现有方法不同，该方法首次实现了不依赖任何事后补偿的有效概念擦除。论文在多个基准上进行了广泛评估，证明了该方法在有效移除目标概念的同时，能保持其他概念的高质量生成。这项工作直接关联到化学信息学中利用生成模型（如化学大模型）进行分子设计时，对特定不良或敏感属性/结构进行可控移除的需求。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The powerful generative capabilities of diffusion models have raised growing privacy and safety concerns regarding generating sensitive or undesired content. In response, machine unlearning (MU) -- commonly referred to as concept erasure (CE) in diffusion models -- has been introduced to remove specific knowledge from model parameters meanwhile preserving innocent knowledge. Despite recent advancements, existing unlearning methods often suffer from excessive and indiscriminate removal, which leads to substantial degradation in the quality of innocent generations. To preserve model utility, prior works rely on compensation, i.e., re-assimilating a subset of the remaining data or explicitly constraining the divergence from the pre-trained model on remaining concepts. However, we reveal that generations beyond the compensation scope still suffer, suggesting such post-remedial compensations are inherently insufficient for preserving the general utility of large-scale generative models. Therefore, in this paper, we advocate for developing compensation-free concept erasure operations, which precisely identify and eliminate the undesired knowledge such that the impact on other generations is minimal. In technique, we propose to MiM-MU, which is to unlearn a concept by minimizing the mutual information with a delicate design for computational effectiveness and for maintaining sampling distribution for other concepts. Extensive evaluations demonstrate that our proposed method achieves effective concept removal meanwhile maintaining high-quality generations for other concepts, and remarkably, without relying on any post-remedial compensation for the first time.

</details>

---

### 33. [Thoth: Mid-Training Bridges LLMs to Time Series Understanding](https://arxiv.org/abs/2603.01042)

**基本信息**

- 🔗 arXiv: [`2603.01042`](https://arxiv.org/abs/2603.01042)
- 👥 作者: Jiafeng Lin, Yuxuan Wang, Jialong Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01042.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使大语言模型获得理解和推理时间序列数据的能力。质谱数据（如色谱-质谱联用数据）是典型的时间/序列数据，因此这项工作直接关系到构建能够处理质谱数据、进行质谱结构推理的化学大模型这一核心主题。

**📖 中文摘要**

本文提出了Thoth，这是第一个通过“中期训练”获得通用时间序列理解能力的大语言模型家族。为了在时间序列和自然语言之间实现任务和领域无关的对齐，作者构建了Book-of-Thoth，一个高质量、以时间序列为中心的中期训练语料库，支持时间序列到文本和文本到时间序列的生成。此外，作者还提出了KnoTS，一个用于评估时间序列与领域知识联合推理的新基准。实验表明，Thoth在时间序列问答基准上显著优于其基础模型和先进的大语言模型。这项研究为将大语言模型的能力扩展到结构化数据（如时间序列）理解提供了新范式。在化学信息学和质谱分析中，质谱数据本质上是时间或质荷比序列，该工作为构建能够理解和推理质谱数据的化学大模型提供了重要的方法论参考和技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated remarkable success in general-purpose reasoning. However, they still struggle to understand and reason about time series data, which limits their effectiveness in decision-making scenarios that depend on temporal dynamics. In this paper, we propose Thoth, the first family of mid-trained LLMs with general-purpose time series understanding capabilities. As a pivotal intermediate stage, mid-training achieves task- and domain-agnostic alignment between time series and natural language, for which we construct Book-of-Thoth, a high-quality, time-series-centric mid-training corpus. Book-of-Thoth enables both time-series-to-text and text-to-time-series generation, equipping LLMs with a foundational grasp of temporal patterns. To better evaluate advanced reasoning capabilities, we further present KnoTS, a novel benchmark of knowledge-intensive time series understanding, designed for joint reasoning over temporal patterns and domain knowledge. Extensive experiments demonstrate that mid-training with Book-of-Thoth enables Thoth to significantly outperform its base model and advanced LLMs across a range of time series question answering benchmarks. Moreover, Thoth exhibits superior capabilities when fine-tuned under data scarcity, underscoring the effectiveness of mid-training for time series understanding. Code is available at: this https URL .

</details>

---

### 34. [MMCOMET: A Large-Scale Multimodal Commonsense Knowledge Graph for Contextual Reasoning](https://arxiv.org/abs/2603.01055)

**基本信息**

- 🔗 arXiv: [`2603.01055`](https://arxiv.org/abs/2603.01055)
- 👥 作者: Eileen Wang, Hiba Arnaout, Dhita Pratama 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01055.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个大规模的多模态常识知识图谱（MMCOMET），它整合了视觉和文本知识。这种多模态知识资源可以作为化学大模型和质谱结构推理任务的重要外部知识库或预训练数据来源，帮助模型建立化学实体、结构、性质及其多模态表征（如分子图、光谱图）之间的关联。

**📖 中文摘要**

本文提出了MMCOMET，这是第一个整合了物理、社会和事件性知识的多模态常识知识图谱。它通过高效的图像检索过程，将ATOMIC2020知识图谱扩展至包含视觉维度，产生了超过90万个多模态三元组。这一资源解决了现有多模态知识图谱在支持复杂推理任务（如图像描述和故事生成）方面的主要限制。通过视觉叙事生成实验，作者展示了这种整体方法能够生成比仅使用文本知识更丰富、连贯且基于上下文的叙事。MMCOMET为多模态常识推理建立了新的基础。对于化学大模型和质谱结构推理，多模态知识图谱可以整合分子结构图像、光谱图、文本描述和化学常识，为模型提供更丰富的上下文信息，从而提升其对复杂化学现象的理解和推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MMCOMET, the first multimodal commonsense knowledge graph (MMKG) that integrates physical, social, and eventive knowledge. MMCOMET extends the ATOMIC2020 knowledge graph to include a visual dimension, through an efficient image retrieval process, resulting in over 900K multimodal triples. This new resource addresses a major limitation of existing MMKGs in supporting complex reasoning tasks like image captioning and storytelling. Through a standard visual storytelling experiment, we show that our holistic approach enables the generation of richer, coherent, and contextually grounded stories than those produced using text-only knowledge. This resource establishes a new foundation for multimodal commonsense reasoning and narrative generation.

</details>

---

### 35. [Alien Science: Sampling Coherent but Cognitively Unavailable Research Directions from Idea Atoms](https://arxiv.org/abs/2603.01092)

**基本信息**

- 🔗 arXiv: [`2603.01092`](https://arxiv.org/abs/2603.01092)
- 👥 作者: Alejandro H. Artiles, Martin Weiss, Levin Brinkmann 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01092.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕从海量文献中提取和建模概念单元（“想法原子”）以生成新的研究方向。这种方法论与构建“化学大模型”所需的知识表示、概念提取和知识发现过程直接相关，为化学领域的大模型构建提供了可借鉴的框架。

**📖 中文摘要**

本文提出了一种名为“Alien Science”的流程，旨在从大量研究论文中生成“连贯但认知上不可用”的研究方向。其核心是将论文分解为细粒度的概念单元，并将其聚类为共享的“想法原子”词汇表。然后，该流程学习两个互补模型：一个评估一组原子是否构成可行方向的“连贯性模型”，以及一个评估该方向被当前研究社区自然提出的可能性的“可用性模型”。最终，该流程采样那些连贯性高但可用性低（即非显而易见）的“外星”研究方向。该研究在约7500篇最近的LLM论文上进行了验证。虽然论文本身聚焦于LLM研究方向的生成，但其提出的“想法原子”分解、聚类和建模流程，为构建和理解“化学大模型”或“质谱结构推理”领域的概念空间和知识图谱提供了方法论基础。其核心思想——从海量文献中提取和重组概念单元以发现新方向——与化学信息学中从文献挖掘化学知识、构建预测模型的研究范式高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models are adept at synthesizing and recombining familiar material, yet they often fail at a specific kind of creativity that matters most in research: producing ideas that are both coherent and non-obvious to the current community. We formalize this gap through cognitive availability, the likelihood that a research direction would be naturally proposed by a typical researcher given what they have worked on. We introduce a pipeline that (i) decomposes papers into granular conceptual units, (ii) clusters recurring units into a shared vocabulary of idea atoms, and (iii) learns two complementary models: a coherence model that scores whether a set of atoms constitutes a viable direction, and an availability model that scores how likely that direction is to be generated by researchers drawn from the community. We then sample "alien" directions that score high on coherence but low on availability. On a corpus of $\sim$7,500 recent LLM papers from NeurIPS, ICLR and ICML, we validate that (a) conceptual units preserve paper content under reconstruction, (b) idea atoms generalize across papers rather than memorizing paper-specific phrasing, and (c) the Alien sampler produces research directions that are more diverse than LLM baselines while maintaining coherence.

</details>

---

### 36. [Unified Vision-Language Modeling via Concept Space Alignment](https://arxiv.org/abs/2603.01096)

**基本信息**

- 🔗 arXiv: [`2603.01096`](https://arxiv.org/abs/2603.01096)
- 👥 作者: Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01096.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容围绕构建统一的多模态、多语言大模型（V-LCM）和概念模型（LCM），这与“化学大模型”的研究主题直接相关。2) 论文提出的V-SONAR嵌入空间、V-LCM模型架构以及相关的训练方法（如后处理对齐、潜在扩散目标）为化学领域构建类似的多模态大模型提供了可借鉴的技术资源和工具思路。

**📖 中文摘要**

本文介绍了V-SONAR，一个从纯文本嵌入空间SONAR扩展而来的视觉-语言嵌入空间。V-SONAR通过一个后处理对齐流程，将现有视觉编码器的表示映射到SONAR空间中。论文展示了V-SONAR在文本到视频检索和视频描述任务上的竞争力。更重要的是，论文利用V-SONAR，首次展示了仅用英语文本训练的、在SONAR空间中运行的“大概念模型”（LCM）能够以零样本方式执行单视觉和多视觉概念理解。最后，论文引入了V-LCM，通过视觉-语言指令微调扩展了LCM。V-LCM通过V-SONAR和SONAR将视觉和语言输入编码为统一的潜在嵌入序列，并使用与LCM文本预训练相同的潜在扩散目标进行训练。实验表明，V-LCM在图像/视频描述和问答任务上匹配了最先进的视觉-语言模型，同时在62种测试语言中的61种上显著优于它们。这项工作构建了一个强大的多模态、多语言统一表示空间和模型（V-SONAR, V-LCM, LCM），为处理化学结构（图像/图）、质谱数据（序列/图）和文本描述的多模态“化学大模型”提供了重要的模型架构和表示学习思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce V-SONAR, a vision-language embedding space extended from the text-only embedding space SONAR (Omnilingual Embeddings Team et al., 2026), which supports 1500 text languages and 177 speech languages. To construct V-SONAR, we propose a post-hoc alignment pipeline that maps the representations of an existing vision encoder into the SONAR space. We thoroughly evaluate V-SONAR and show that its embeddings achieve competitive performance on text-to-video retrieval. Equipped with the OMNISONAR text decoder, V-SONAR further surpasses state-of-the-art vision-language models on video captioning tasks, including DREAM-1K (BLEU 23.9 vs. 19.6) and PE-VIDEO (BLEU 39.0 vs. 30.0). Leveraging V-SONAR, we first demonstrate that the Large Concept Model (LCM; LCM team et al. 2024) operating in SONAR and trained with English text only, can perform both single- and multi-visual concept understanding in a zero-shot manner. Finally, we introduce V-LCM, which extends the LCM with vision-language instruction tuning. V-LCM encodes vision and language inputs into an unified sequence of latent embeddings via V-SONAR and SONAR, and it is trained with the same latent diffusion objective for next-embedding prediction as in LCM's text-only pre-training. Experiments on a large-scale multilingual and -modal instruction-tuning data mixture highlight the potential of V-LCM: V-LCM matches state-of-the-art vision-language models on tasks covering image/video captioning and question answering, while significantly outperforming them across 61 rich- to low-resource languages out of all 62 tested languages.

</details>

---

### 37. [Understanding LoRA as Knowledge Memory: An Empirical Analysis](https://arxiv.org/abs/2603.01097)

**基本信息**

- 🔗 arXiv: [`2603.01097`](https://arxiv.org/abs/2603.01097)
- 👥 作者: Seungju Back, Dongwoo Lee, Naun Kang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01097.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用LoRA作为大模型的参数化知识记忆模块。这一研究方向与如何构建、更新和管理“化学大模型”中的领域专业知识直接相关，为化学领域大模型的高效知识注入和持续学习提供了重要的技术路径参考。

**📖 中文摘要**

本文对将LoRA（低秩适应）作为预训练大语言模型（LLMs）的模块化“知识记忆”进行了首次系统的实证研究。研究探索了LoRA记忆的设计空间，包括表征存储容量、优化内部化过程、扩展多模块系统以及评估长上下文推理。研究旨在提供关于LoRA记忆操作边界的实用指导，并将其定位为与RAG和ICL互补的记忆轴。虽然论文主要针对LLMs的持续知识更新，但其对参数化记忆模块（LoRA）的容量、可组合性和系统评估的深入分析，对于在“化学大模型”中管理领域特定知识（如化学反应规则、化合物性质、质谱解析规则）具有重要的参考价值。研究为如何以模块化、参数高效的方式为化学大模型注入和更新专业知识提供了实证依据和方法论启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continuous knowledge updating for pre-trained large language models (LLMs) is increasingly necessary yet remains challenging. Although inference-time methods like In-Context Learning (ICL) and Retrieval-Augmented Generation (RAG) are popular, they face constraints in context budgets, costs, and retrieval fragmentation. Departing from these context-dependent paradigms, this work investigates a parametric approach using Low-Rank Adaptation (LoRA) as a modular knowledge memory. Although few recent works examine this concept, the fundamental mechanics governing its capacity and composability remain largely unexplored. We bridge this gap through the first systematic empirical study mapping the design space of LoRA-based memory, ranging from characterizing storage capacity and optimizing internalization to scaling multi-module systems and evaluating long-context reasoning. Rather than proposing a single architecture, we provide practical guidance on the operational boundaries of LoRA memory. Overall, our findings position LoRA as the complementary axis of memory alongside RAG and ICL, offering distinct advantages.

</details>

---

### 38. [FCN-LLM: Empower LLM for Brain Functional Connectivity Network Understanding via Graph-level Multi-task Instruction Tuning](https://arxiv.org/abs/2603.01135)

**基本信息**

- 🔗 arXiv: [`2603.01135`](https://arxiv.org/abs/2603.01135)
- 👥 作者: Xingcan Hu, Wei Wang, Li Xiao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01135.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是将图结构数据（大脑功能连接网络）与大语言模型对齐和集成，使其能够进行理解和推理，这与让化学大模型理解分子图、质谱图进行“质谱结构推理”的研究主题高度一致。2) 论文提出的FCN-LLM框架（多尺度图编码器、图-语义空间对齐、多任务指令微调）为化学领域实现类似的图-语言大模型提供了具体的方法、架构和工具思路。

**📖 中文摘要**

本文提出了FCN-LLM，一个通过图级、多任务指令微调使大语言模型（LLMs）能够理解大脑功能连接网络（FCN）的框架。该框架采用多尺度FCN编码器捕获大脑区域、功能子网络和全脑特征，并将其投影到LLM的语义空间中。研究设计了涵盖人口统计学、表型和精神病学条件等19个受试者特定属性的多范式指令任务，并采用多阶段学习策略。实验表明，FCN-LLM在大型多站点FCN数据库上实现了强大的零样本泛化能力。这项工作为将大脑功能网络与LLMs集成引入了一种新范式。虽然应用领域是神经科学，但其核心方法论——将复杂的图结构数据（FCN）通过编码器与LLM的语义空间对齐，并通过多任务指令微调使LLM能够理解和推理图数据——与“化学大模型”和“质谱结构推理”高度相关。化学分子本质上是图结构，质谱数据也可以表示为图或序列。该框架为如何让LLM理解分子图、质谱图并进行推理（如结构解析）提供了直接的技术蓝图和可行性证明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models have achieved remarkable success in language understanding and reasoning, and their multimodal extensions enable comprehension of images, video, and audio. Inspired by this, foundation models for brain functional connectivity networks derived from resting-state fMRI have shown promise in clinical tasks. However, existing methods do not align FCNs with the text modality, limiting the ability of LLMs to directly understand FCNs. To address this, we propose FCN-LLM, a framework that enables LLMs to understand FCNs through graph-level, multi-task instruction tuning. Our approach employs a multi-scale FCN encoder capturing brain-region, functional subnetwork, and whole-brain features, projecting them into the semantic space of LLM. We design multi-paradigm instruction tasks covering 19 subject-specific attributes across demographics, phenotypes, and psychiatric conditions. A multi-stage learning strategy first aligns FCN embeddings with the LLM and then jointly fine-tunes the entire model to capture high-level semantic information. Experiments on a large-scale, multi-site FCN database show that FCN-LLM achieves strong zero-shot generalization on unseen datasets, outperforming conventional supervised and foundation models. This work introduces a new paradigm for integrating brain functional networks with LLMs, offering a flexible and interpretable framework for neuroscience.

</details>

---

### 39. [DeepResearch-9K: A Challenging Benchmark Dataset of Deep-Research Agent](https://arxiv.org/abs/2603.01152)

**基本信息**

- 🔗 arXiv: [`2603.01152`](https://arxiv.org/abs/2603.01152)
- 👥 作者: Tongzhou Wu, Yuhao Wang, Xinyu Ma 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01152.pdf)

**💡 相关性分析**

满足标准2：论文提供了用于训练和评估深度研究智能体的大规模基准数据集（DeepResearch-9K）和开源训练框架（DeepResearch-R1）。这些资源和工具可以经过适配，用于构建和训练专注于化学信息学与质谱分析领域文献挖掘、数据分析和结构推理的研究型AI智能体，为相关主题提供了重要的数据和方法资源。

**📖 中文摘要**

本文构建了DeepResearch-9K，一个专门为深度研究场景设计的大规模、具有挑战性的基准数据集。该数据集通过一个低成本的自主流程，从开源的多跳问答数据集中构建而成，包含9000个问题、来自先进深度研究代理的高质量搜索轨迹与推理链，以及可验证的答案。此外，本文还开发了一个开源训练框架DeepResearch-R1，支持多轮网络交互、不同的强化学习方法以及不同的奖励模型。实验结果表明，在该数据集和框架下训练的智能体在具有挑战性的深度研究基准测试中取得了最先进的结果。该工作虽然面向通用的深度研究智能体，但其构建高质量、复杂推理数据集的流程（从多跳QA数据转化），以及支持复杂交互和强化学习的训练框架，为开发和评估专注于“化学文献挖掘”、“质谱数据解析推理”的领域特定研究型AI智能体提供了宝贵的数据集构建方法论和训练工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep-research agents are capable of executing multi-step web exploration, targeted retrieval, and sophisticated question answering. Despite their powerful capabilities, deep-research agents face two critical bottlenecks: (1) the lack of large-scale, challenging datasets with real-world difficulty, and (2) the absence of accessible, open-source frameworks for data synthesis and agent training. To bridge these gaps, we first construct DeepResearch-9K, a large-scale challenging dataset specifically designed for deep-research scenarios built from open-source multi-hop question-answering (QA) datasets via a low-cost autonomous pipeline. Notably, it consists of (1) 9000 questions spanning three difficulty levels from L1 to L3 (2) high-quality search trajectories with reasoning chains from Tongyi-DeepResearch-30B-A3B, a state-of-the-art deep-research agent, and (3) verifiable answers. Furthermore, we develop an open-source training framework DeepResearch-R1 that supports (1) multi-turn web interactions, (2) different reinforcement learning (RL) approaches, and (3) different reward models such as rule-based outcome reward and LLM-as-judge feedback. Finally, empirical results demonstrate that agents trained on DeepResearch-9K under our DeepResearch-R1 achieve state-of-the-art results on challenging deep-research benchmarks. We release the DeepResearch-9K dataset on this https URL and the code of DeepResearch-R1 on this https URL .

</details>

---

### 40. [DEP: A Decentralized Large Language Model Evaluation Protocol](https://arxiv.org/abs/2603.01167)

**基本信息**

- 🔗 arXiv: [`2603.01167`](https://arxiv.org/abs/2603.01167)
- 👥 作者: Jianxiang Peng, Junhao Li, Hongxiang Wang 等18人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01167.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个去中心化、标准化的LLM评估协议（DEP）及配套工具包（DEP Toolkit）。这为“化学大模型”和“质谱结构推理”模型建立专业、公平、可重复的评估基准和测试平台提供了重要的框架性工具和资源，有助于相关领域的模型比较和性能评估。

**📖 中文摘要**

本文提出了一个去中心化评估协议（DEP），用于大语言模型（LLMs）的评估。它是一个去中心化、统一且标准化的评估框架，通过一个匹配服务器实现，不限制基准测试。服务器可以本地安装或远程部署，一旦适配，可以长期复用。通过将用户、LLMs和基准测试解耦，DEP实现了模块化、即插即用的评估：基准测试文件和评估逻辑完全保留在服务器端。在远程设置中，用户无法访问真实答案，从而实现数据隔离和防泄漏评估。为了便于实际采用，本文开发了DEP Toolkit，一个协议兼容的工具包。作者已经适配了超过60个基准测试。这项工作虽然主要针对通用LLM评估，但其提出的去中心化、防泄漏、标准化的评估协议和工具包，为“化学大模型”或“质谱结构推理”模型建立公平、可靠、可重复的评估基准和平台提供了重要的框架和工具资源。可以用于构建化学领域的专业模型评估生态。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rapid development of Large Language Models (LLMs), a large number of benchmarks have been proposed. However, most benchmarks lack unified evaluation standard and require the manual implementation of custom scripts, making results hard to ensure consistency and reproducibility. Furthermore, mainstream evaluation frameworks are centralized, with datasets and answers, which increases the risk of benchmark leakage. To address these issues, we propose a Decentralized Evaluation Protocol (DEP), a decentralized yet unified and standardized evaluation framework through a matching server without constraining benchmarks. The server can be mounted locally or deployed remotely, and once adapted, it can be reused over the long term. By decoupling users, LLMs, and benchmarks, DEP enables modular, plug-and-play evaluation: benchmark files and evaluation logic stay exclusively on the server side. In remote setting, users cannot access the ground truth, thereby achieving data isolation and leak-proof evaluation. To facilitate practical adoption, we develop DEP Toolkit, a protocol-compatible toolkit that supports features such as breakpoint resume, concurrent requests, and congestion control. We also provide detailed documentation for adapting new benchmarks to DEP. Using DEP toolkit, we evaluate multiple LLMs across benchmarks. Experimental results verify the effectiveness of DEP and show that it reduces the cost of deploying benchmark evaluations. As of February 2026, we have adapted over 60 benchmarks and continue to promote community co-construction to support unified evaluation across various tasks and domains.

</details>

---

### 41. [VisNec: Measuring and Leveraging Visual Necessity for Multimodal Instruction Tuning](https://arxiv.org/abs/2603.01195)

**基本信息**

- 🔗 arXiv: [`2603.01195`](https://arxiv.org/abs/2603.01195)
- 👥 作者: Mingkang Dong, Hongyi Cai, Jie Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01195.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是多模态指令微调中视觉必要性的度量和数据选择，这与构建需要处理分子图像、谱图等多模态数据的“化学大模型”的训练数据优化问题直接相关。2) 论文提出的VisNec框架和度量方法为化学领域构建高质量多模态训练数据集提供了具体的工具和筛选策略。

**📖 中文摘要**

本文提出了VisNec（视觉必要性分数），一个用于多模态指令微调的数据选择框架。它通过比较模型在有视觉输入和没有视觉输入情况下的预测损失，来衡量视觉输入对于完成指令的边际贡献，从而识别出训练样本是视觉关键、视觉冗余还是多模态未对齐的。为了保持任务多样性，VisNec与语义聚类结合，在每个聚类中选择高必要性样本。实验表明，使用VisNec从LLaVA-665K数据集中仅选择15%的数据进行训练，就能达到全数据性能的100.2%。在更小的Vision-Flan-186K数据集上，其选择不仅进一步减少了数据量，而且性能超过了全数据训练15.8%。这项工作直接针对多模态模型训练中数据质量的核心问题，其提出的视觉必要性度量方法和数据选择策略，对于构建高效的“化学大模型”至关重要。在化学领域，训练数据可能包含分子结构图、质谱图、文本描述等，VisNec的方法可以帮助筛选出那些真正需要多模态（如图+文）联合推理才能解决的样本，从而构建更高质量、更高效的训练数据集，避免在大量视觉冗余样本上浪费算力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The effectiveness of multimodal instruction tuning depends not only on dataset scale, but critically on whether training samples genuinely require visual reasoning. However, existing instruction datasets often contain a substantial portion of visually redundant samples (solvable from text alone), as well as multimodally misaligned supervision that can degrade learning. To address this, we propose VisNec (Visual Necessity Score), a principled data selection framework that measures the marginal contribution of visual input during instruction tuning. By comparing predictive loss with and without visual context, VisNec identifies whether a training instance is vision-critical, redundant, or misaligned. To preserve task diversity, we combine VisNec with semantic clustering and select high-necessity samples within each cluster. Across 10 downstream benchmarks, training on only 15% of the LLaVA-665K dataset selected by VisNec achieves 100.2% of full-data performance. On the smaller Vision-Flan-186K dataset, our selection not only further reduces data size but also surpasses full-data training by 15.8%. These results demonstrate that measuring and leveraging visual necessity provides an effective solution for both efficient and robust multimodal instruction tuning. Codes and selected subsets will be released upon acceptance.

</details>

---

### 42. [CoSMo3D: Open-World Promptable 3D Semantic Part Segmentation through LLM-Guided Canonical Spatial Modeling](https://arxiv.org/abs/2603.01205)

**基本信息**

- 🔗 arXiv: [`2603.01205`](https://arxiv.org/abs/2603.01205)
- 👥 作者: Li Jin, Weikai Chen, Yujie Wang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是学习3D对象的规范空间表示以实现稳定、可迁移的语义理解。这一思想与化学信息学中寻求对分子功能、性质进行与具体表示形式（如不同绘图方式、构象）无关的稳健表示的学习目标高度相关，为“化学大模型”中的分子表示学习提供了重要的方法论参考。

**📖 中文摘要**

本文提出了CoSMo3D，一个通过LLM引导的规范空间建模实现开放世界可提示3D语义部件分割的方法。为了解决开放世界3D语义分割在输入传感器坐标中推断语义的脆弱性问题，该方法通过从数据中直接学习一个潜在的规范参考框架，来获得规范空间感知。具体而言，该方法通过LLM引导的类别内和跨类别对齐，创建了一个统一的规范数据集，揭示了跨200个类别的规范空间规律性。通过一个具有规范图锚定和规范框校准的双分支架构，将姿态变化和对称性折叠到一个稳定的规范嵌入中。这种从输入姿态空间到规范嵌入的转变，产生了更稳定和可迁移的部件语义。这项工作在3D视觉领域，但其核心思想——学习一个与姿态无关的、基于功能的规范表示空间来稳定语义理解——与“化学大模型”和“质谱结构推理”中面临的问题有相似之处。例如，在化学中，分子功能（语义）应与其具体的二维绘制或三维构象（姿态）相对独立。该论文的方法论为化学领域表示学习（如学习分子功能的规范表示）提供了启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Open-world promptable 3D semantic segmentation remains brittle as semantics are inferred in the input sensor coordinates. Yet, humans, in contrast, interpret parts via functional roles in a canonical space -- wings extend laterally, handles protrude to the side, and legs support from below. Psychophysical evidence shows that we mentally rotate objects into canonical frames to reveal these roles. To fill this gap, we propose \methodName{}, which attains canonical space perception by inducing a latent canonical reference frame learned directly from data. By construction, we create a unified canonical dataset through LLM-guided intra- and cross-category alignment, exposing canonical spatial regularities across 200 categories. By induction, we realize canonicality inside the model through a dual-branch architecture with canonical map anchoring and canonical box calibration, collapsing pose variation and symmetry into a stable canonical embedding. This shift from input pose space to canonical embedding yields far more stable and transferable part semantics. Experimental results show that \methodName{} establishes new state of the art in open-world promptable 3D segmentation.

</details>

---

### 43. [The Lattice Representation Hypothesis of Large Language Models](https://arxiv.org/abs/2603.01227)

**基本信息**

- 🔗 arXiv: [`2603.01227`](https://arxiv.org/abs/2603.01227)
- 👥 作者: Bo Xiong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01227.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出并验证大语言模型内部可能存在“概念格”形式的符号化、结构化表示。这一理论发现对于理解和构建能够进行复杂逻辑和层次推理的“化学大模型”具有根本性的指导意义，直接关系到模型如何表示和组织化学领域的概念体系。

**📖 中文摘要**

本文提出了大语言模型的“格表示假说”：一个在嵌入几何中锚定概念层次和逻辑操作的符号主干。该框架将“线性表示假说”与“形式概念分析”统一起来，表明具有分离阈值的线性属性方向通过半空间交集诱导出一个概念格。这种几何结构使得通过几何交（交集）和并（并集）操作进行符号推理成为可能，并且当属性方向线性无关时，允许一种规范形式。在WordNet子层次结构上的实验提供了实证证据，表明LLM嵌入编码了概念格及其逻辑结构，揭示了连续几何和符号抽象之间有原则的桥梁。这项工作从理论层面揭示了LLM内部可能存在的符号化、结构化的知识表示形式（概念格）。这对于理解“化学大模型”如何组织和推理化学概念（如官能团、反应类型、性质趋势）具有根本性的启示。如果化学知识在模型中以类似概念格的形式存在，将极大地促进模型的可解释性和可控性，并为基于逻辑的化学推理提供基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Lattice Representation Hypothesis of large language models: a symbolic backbone that grounds conceptual hierarchies and logical operations in embedding geometry. Our framework unifies the Linear Representation Hypothesis with Formal Concept Analysis (FCA), showing that linear attribute directions with separating thresholds induce a concept lattice via half-space intersections. This geometry enables symbolic reasoning through geometric meet (intersection) and join (union) operations, and admits a canonical form when attribute directions are linearly independent. Experiments on WordNet sub-hierarchies provide empirical evidence that LLM embeddings encode concept lattices and their logical structure, revealing a principled bridge between continuous geometry and symbolic abstraction.

</details>

---

### 44. [GlassMol: Interpretable Molecular Property Prediction with Concept Bottleneck Models](https://arxiv.org/abs/2603.01274)

**基本信息**

- 🔗 arXiv: [`2603.01274`](https://arxiv.org/abs/2603.01274)
- 👥 作者: Oscar Rivera, Ziqing Wang, Matthieu Dagommer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01274.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学大模型的可解释性这一主题，提出了一个专门针对分子性质预测的概念瓶颈模型框架。

**📖 中文摘要**

本文提出了GlassMol，一种基于概念瓶颈模型（CBM）的可解释分子性质预测框架。该工作旨在解决化学信息学和药物发现中机器学习模型（如大语言模型和图神经网络）的黑箱性问题。GlassMol通过将输入投影到人类可解释的概念（如分子描述符）上，再进行最终预测，确保了决策过程的忠实可解释性。它解决了概念瓶颈模型在化学领域应用的三个关键挑战：从大型描述符空间中选择任务相关概念的“相关性鸿沟”、获取分子数据概念监督的“标注鸿沟”以及因瓶颈约束导致性能下降的“容量鸿沟”。论文在13个基准测试上进行了实验，表明GlassMol在保持或超越黑盒基线模型性能的同时，提供了固有的可解释性。这项工作直接关联到“化学大模型”主题，因为它专注于为化学领域的机器学习模型（可视为特定领域的化学大模型）提供可解释性框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning accelerates molecular property prediction, yet state-of-the-art Large Language Models and Graph Neural Networks operate as black boxes. In drug discovery, where safety is critical, this opacity risks masking false correlations and excluding human expertise. Existing interpretability methods suffer from the effectiveness-trustworthiness trade-off: explanations may fail to reflect a model's true reasoning, degrade performance, or lack domain grounding. Concept Bottleneck Models (CBMs) offer a solution by projecting inputs to human-interpretable concepts before readout, ensuring that explanations are inherently faithful to the decision process. However, adapting CBMs to chemistry faces three challenges: the Relevance Gap (selecting task-relevant concepts from a large descriptor space), the Annotation Gap (obtaining concept supervision for molecular data), and the Capacity Gap (degrading performance due to bottleneck constraints). We introduce GlassMol, a model-agnostic CBM that addresses these gaps through automated concept curation and LLM-guided concept selection. Experiments across thirteen benchmarks demonstrate that \method generally matches or exceeds black-box baselines, suggesting that interpretability does not sacrifice performance and challenging the commonly assumed trade-off. Code is available at this https URL .

</details>

---

### 45. [Attention Smoothing Is All You Need For Unlearning](https://arxiv.org/abs/2603.01285)

**基本信息**

- 🔗 arXiv: [`2603.01285`](https://arxiv.org/abs/2603.01285)
- 👥 作者: Saleh Zare Zade, Xiangyu Zhou, Sijia Liu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01285.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大语言模型的编辑与知识管理，这是构建和优化领域大模型（如化学大模型）的关键技术之一。

**📖 中文摘要**

本文提出了注意力平滑遗忘（ASU）框架，用于解决大语言模型（LLMs）中记忆敏感、受版权保护或有害内容的问题。ASU将遗忘过程视为基于模型自身注意力的自蒸馏过程，通过提高softmax温度来平滑注意力分布，从而直接抑制与记忆知识重建相关的词汇级和语义级关联。该方法旨在实现有界优化目标，在擦除事实信息的同时，保持对遗忘提示响应的连贯性，并最小化模型效用的损失。论文在TOFU、MUSE和WMDP等基准以及现实世界和持续遗忘场景中进行了评估。虽然论文主要关注通用大语言模型，但其提出的基于注意力机制的模型编辑和知识管理方法，对于构建更安全、可控的领域大模型（如化学大模型）具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models are prone to memorizing sensitive, copyrighted, or hazardous content, posing significant privacy and legal concerns. Retraining from scratch is computationally infeasible, whereas current unlearning methods exhibit unstable trade-offs between forgetting and utility, frequently producing incoherent outputs on forget prompts and failing to generalize due to the persistence of lexical-level and semantic-level associations in attention. We propose Attention Smoothing Unlearning (ASU), a principled framework that casts unlearning as self-distillation from a forget-teacher derived from the model's own attention. By increasing the softmax temperature, ASU flattens attention distributions and directly suppresses the lexical-level and semantic-level associations responsible for reconstructing memorized knowledge. This results in a bounded optimization objective that erases factual information yet maintains coherence in responses to forget prompts. Empirical evaluation on TOFU, MUSE, and WMDP, along with real-world and continual unlearning scenarios across question answering and text completion, demonstrates that ASU outperforms the baselines for most unlearning scenarios, delivering robust unlearning with minimal loss of model utility.

</details>

---

### 46. [Efficient Extractive Summarization with MAMBA-Transformer Hybrids for Low-Resource Scenarios](https://arxiv.org/abs/2603.01288)

**基本信息**

- 🔗 arXiv: [`2603.01288`](https://arxiv.org/abs/2603.01288)
- 👥 作者: Nisrine Ait Khayi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01288.pdf)

**💡 相关性分析**

满足标准1：论文探索了Transformer与状态空间模型（Mamba）的混合架构，这是大模型（包括潜在化学大模型）架构创新的重要方向，旨在提升长序列建模的效率。

**📖 中文摘要**

本文提出了一种用于抽取式文本摘要的Mamba-Transformer混合架构，旨在解决长文档处理中的二次复杂度瓶颈。该架构结合了预训练Transformer的语义能力和状态空间模型（Mamba）的线性时间处理能力，能够在低资源场景下实现高效的摘要生成。虽然论文聚焦于自然语言处理任务，但其核心创新——将Transformer与新型状态空间模型（SSM）结合以提升长序列建模效率——是当前大模型架构探索的前沿方向。这种高效的序列建模范式对于处理化学中的长序列数据（如分子SMILES字符串、光谱序列）具有潜在的借鉴意义，可能应用于构建更高效的化学序列模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extractive summarization of long documents is bottlenecked by quadratic complexity, often forcing truncation and limiting deployment in resource-constrained settings. We introduce the first Mamba-Transformer hybrid for extractive summarization, combining the semantic strength of pre-trained transformers with the linear-time processing of state space models. Leveraging Mamba's ability to process full documents without truncation, our approach preserves context while maintaining strong summarization quality. The architecture includes: (1) a transformer encoder for sentence-level semantics, (2) a Mamba state space model to capture inter-sentence dependencies efficiently, and (3) a linear classifier for sentence relevance prediction. Across news, argumentative, and scientific domains under low-resource conditions, our method achieves: (1) large gains over BERTSUM and MATCHSUM, including +0.23 ROUGE-1 on ArXiv and statistically significant improvements on all datasets (p < 0.001); (2) consistent advantages across domains, strongest on the longest documents; (3) robust performance with limited training data; and (4) 24-27% faster inference on news summarization (CNN/DailyMail). We introduce the first hybrid Transformer-state space architecture for summarization, showing significant ROUGE improvements in low-resource scenarios.

</details>

---

### 47. [Catalyst-Agent: Autonomous heterogeneous catalyst screening and optimization with an LLM Agent](https://arxiv.org/abs/2603.01311)

**基本信息**

- 🔗 arXiv: [`2603.01311`](https://arxiv.org/abs/2603.01311)
- 👥 作者: Achuth Chandrasekhar, Janghoon Ock, Amir Barati Farimani
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01311.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题直接围绕利用大语言模型（LLM）代理驱动化学研究（催化剂发现），是化学大模型的具体应用；2) 提出了一个集成了LLM、材料数据库接口和GNN计算工具的工作流程框架，可视为一种用于化学发现的工具或方法资源。

**📖 中文摘要**

本文介绍了Catalyst-Agent，一个基于大语言模型（LLM）的自主AI代理，用于异质催化剂的筛选和优化。该代理能够通过OPTIMADE API探索大型材料数据库，进行结构修改，并利用Meta FAIRchem的图神经网络（GNN）模型（通过AdsorbML工作流）计算吸附能。它以闭环方式为研究人员提供有用的材料建议，包括表面级修改以优化接近成功的候选材料。该工作在三个关键反应（氧还原反应ORR、氮还原反应NRR和CO2还原反应CO2RR）上进行了测试，成功率为23-34%，平均每个成功材料收敛需要1-2次试验。这项工作展示了AI代理利用其规划能力和工具使用来操作催化剂筛选工作流程的潜力，为加速科学发现提供了最小人工干预的范例。该研究是“化学大模型”与“AI for Science”结合的典型代表，利用LLM作为智能体核心，驱动基于GNN的计算工具，完成复杂的化学研究任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The discovery of novel catalysts tailored for particular applications is a major challenge for the twenty-first century. Traditional methods for this include time-consuming and expensive experimental trial-and-error approaches in labs based on chemical theory or heavily computational first-principles approaches based on density functional theory. Recent studies show that deep learning models like graph neural networks (GNNs) can significantly speed up the screening and discovery of catalyst materials by many orders of magnitude, with very high accuracy and fidelity. In this work, we introduce Catalyst-Agent, a Model Context Protocol (MCP) server-based, LLM-powered AI agent. It can explore vast material databases using the OPTIMADE API, make structural modifications, calculate adsorption energies using Meta FAIRchem's UMA (GNN) model via FAIRchem's AdsorbML workflow and slab construction, and make useful material suggestions to the researcher in a closed-loop manner, including surface-level modifications to refine near-miss candidates. It is tested on three pivotal reactions: the oxygen reduction reaction (ORR), the nitrogen reduction reaction (NRR), and the CO2 reduction reaction (CO2RR). Catalyst-Agent achieves a success rate of 23-34 percent among all the materials it chooses and evaluates, and manages to converge in 1-2 trials per successful material on average. This work demonstrates the potential of AI agents to exercise their planning capabilities and tool use to operationalize the catalyst screening workflow, provide useful, testable hypotheses, and accelerate future scientific discoveries for humanity with minimal human intervention.

</details>

---

### 48. [PymooLab: An Open-Source Visual Analytics Framework for Multi-Objective Optimization using LLM-Based Code Generation and MCDM](https://arxiv.org/abs/2603.01345)

**基本信息**

- 🔗 arXiv: [`2603.01345`](https://arxiv.org/abs/2603.01345)
- 👥 作者: Thiago Santos, Sebastiao Xavier, Luiz Gustavo de Oliveira Carneiro 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01345.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容涉及利用大语言模型（LLM）辅助生成代码以简化多目标优化流程，这是大模型在科学计算和工程优化中的具体应用，与“化学大模型”主题中利用大模型提升科研效率的方向相关。

**📖 中文摘要**

本文介绍了PymooLab，一个基于pymoo的开源可视化分析框架，用于多目标优化。该平台通过集成大语言模型（LLM）辅助的代码生成，简化了问题定义、算法配置和后验分析的过程，降低了使用门槛。虽然该框架是通用优化工具，但其核心特性——利用LLM辅助生成优化模型代码——体现了大语言模型作为编程和建模助手的应用，属于“大模型辅助科研”的范畴。对于化学信息学领域，这种工具可以加速化学过程优化、分子设计等涉及多目标优化问题的建模与求解流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-objective optimization is now a core paradigm in engineering design and scientific discovery. Yet mainstream evolutionary frameworks, including \textit{pymoo}, still depend on imperative coding for problem definition, algorithm configuration, and post-hoc analysis. That requirement creates a non-trivial barrier for practitioners without strong software-engineering training and often complicates reproducible experimentation. We address this gap through PymooLab, an open-source visual analytics environment built on top of \textit{pymoo}. The platform unifies configuration, execution monitoring, and formal decision support in a single reproducible workflow that automatically records hyperparameters, evaluation budgets, and random seeds. Its decoupled object-oriented architecture preserves compatibility with the base ecosystem while enabling LLM-assisted code generation for rapid model formulation. The interface also embeds interactive Multi-Criteria Decision Making (MCDM) tools, which reduces the cognitive burden of Pareto-front inspection. For computationally intensive studies, PymooLab relies on the native \textit{pymoo} acceleration pathway through JAX, improving scalability in high-dimensional evaluations. Overall, the framework combines visual experimentation, LLM-based modeling, and deterministic orchestration to narrow the gap between rigorous operations research and practical accessibility for domain experts. Source code is publicly available at this https URL .

</details>

---

### 49. [UTICA: Multi-Objective Self-Distllation Foundation Model Pretraining for Time Series Classification](https://arxiv.org/abs/2603.01348)

**基本信息**

- 🔗 arXiv: [`2603.01348`](https://arxiv.org/abs/2603.01348)
- 👥 作者: Yessin Moakher, Youssef Attia El Hili, Vasilii Feofanov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01348.pdf)

**💡 相关性分析**

满足标准1：论文专注于为时间序列数据构建基础模型，并探索了非对比预训练策略。这种“基础模型”的构建思路和预训练方法是“化学大模型”或“质谱基础模型”领域可以直接借鉴和参考的核心技术路径。

**📖 中文摘要**

本文提出了UTICA，一个基于自蒸馏（DINOv2风格）预训练的时间序列基础模型。该工作将非对比学习方法（自蒸馏）适配到时间序列数据上，使用Mantis分词器和Transformer编码器作为骨干网络，通过学生-教师框架学习同时捕捉时间不变性和局部细粒度结构的表示。论文在UCR和UEA基准上取得了最先进的分类性能。虽然研究领域是时间序列，但其核心贡献在于探索并验证了非对比学习（自蒸馏）作为时间序列基础模型预训练策略的有效性。这种基础模型预训练范式的探索，对于其他序列数据领域（如化学中的质谱序列、分子序列）构建领域基础模型具有重要的启发和参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Self-supervised foundation models have achieved remarkable success across domains, including time series. However, the potential of non-contrastive methods, a paradigm that has driven significant advances in computer vision, remains underexplored for time series. In this work, we adapt DINOv2-style self-distillation to pretrain a time series foundation model, building on the Mantis tokenizer and transformer encoder architecture as our backbone. Through a student-teacher framework, our method Utica learns representations that capture both temporal invariance via augmented crops and fine-grained local structure via patch masking. Our approach achieves state-of-the-art classification performance on both UCR and UEA benchmarks. These results suggest that non-contrastive methods are a promising and complementary pretraining strategy for time series foundation models.

</details>

---

### 50. [Constructing Synthetic Instruction Datasets for Improving Reasoning in Domain-Specific LLMs: A Case Study in the Japanese Financial Domain](https://arxiv.org/abs/2603.01353)

**基本信息**

- 🔗 arXiv: [`2603.01353`](https://arxiv.org/abs/2603.01353)
- 👥 作者: Yuma Okochi, Fabio Milentiansen Sim, Tomoyasu Okada
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01353.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题是提升领域大语言模型（LLM）的专业知识和推理能力，直接关联“化学大模型”的构建与优化；2) 提出了一种构建领域合成指令数据集的通用方法，这为化学领域构建类似训练资源提供了可借鉴的方案。

**📖 中文摘要**

本研究提出了一种为特定领域（以日本金融领域为例）构建高质量合成指令数据集的通用方法，旨在提升领域大语言模型（LLMs）的领域专业知识和推理能力。该方法从领域特定词汇出发，构建了包含约95亿token、带有思维链推理轨迹的大规模指令数据集。评估结果表明，基于该数据集训练的模型在金融基准测试上性能优于基线模型。论文还报告了推理轨迹长度对性能的影响及其局限性。这项工作为领域大模型的指令微调和数据构建提供了系统性的方法论，其思路可迁移至化学信息学领域，用于构建化学专业知识与推理能力并重的化学大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In adapting LLMs to specific domains, achieving both domain expertise and reasoning ability remains an urgent challenge. This study proposes a general method for constructing high-quality synthetic instruction data for any domain, starting from domain-specific vocabulary. As a demonstration, we applied this method to the financial domain and constructed a large-scale instruction dataset totaling approximately 9.5 billion tokens with Chain-of-Thought reasoning traces. Evaluation results confirmed performance improvements over baseline models on financial benchmarks, demonstrating the effectiveness of our approach. We also report findings on the impact of reasoning trace length on performance and its limitations. Lastly, we open-source our models and datasets on this https URL .

</details>

---

### 51. [Causal Neural Probabilistic Circuits](https://arxiv.org/abs/2603.01372)

**基本信息**

- 🔗 arXiv: [`2603.01372`](https://arxiv.org/abs/2603.01372)
- 👥 作者: Weixin Chen, Han Zhao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将因果推理与神经概率电路结合，构建可解释、可干预的预测模型。这一研究方向对于开发具有可解释性和可靠性的化学大模型（特别是性质预测模型）具有重要的参考价值。

**📖 中文摘要**

本文提出了因果神经概率电路（CNPC），它结合了神经属性预测器和从因果图编译而来的因果概率电路，以增强概念瓶颈模型（CBMs）的可解释性和干预支持。CNPC支持精确、易处理的因果推理，在干预下，它基于专家乘积（PoE）模型类别分布，融合属性预测器的预测分布和电路计算的干预边际。论文在五个基准数据集上进行了实验，表明CNPC在不同干预属性数量下实现了更高的任务准确性。这项工作属于可解释人工智能（XAI）在具有结构化知识（如因果图）的领域中的应用。对于化学信息学，分子性质通常与可解释的分子描述符或子结构（概念）相关，且这些概念间可能存在因果关系。因此，CNPC框架为构建可解释、可干预的化学性质预测模型提供了新的思路，是化学大模型可解释性方向的前沿探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) enhance the interpretability of end-to-end neural networks by introducing a layer of concepts and predicting the class label from the concept predictions. A key property of CBMs is that they support interventions, i.e., domain experts can correct mispredicted concept values at test time to improve the final accuracy. However, typical CBMs apply interventions by overwriting only the corrected concept while leaving other concept predictions unchanged, which ignores causal dependencies among concepts. To address this, we propose the Causal Neural Probabilistic Circuit (CNPC), which combines a neural attribute predictor with a causal probabilistic circuit compiled from a causal graph. This circuit supports exact, tractable causal inference that inherently respects causal dependencies. Under interventions, CNPC models the class distribution based on a Product of Experts (PoE) that fuses the attribute predictor's predictive distribution with the interventional marginals computed by the circuit. We theoretically characterize the compositional interventional error of CNPC w.r.t. its modules and identify conditions under which CNPC closely matches the ground-truth interventional class distribution. Experiments on five benchmark datasets in both in-distribution and out-of-distribution settings show that, compared with five baseline models, CNPC achieves higher task accuracy across different numbers of intervened attributes.

</details>

---

### 52. [Toward Graph-Tokenizing Large Language Models with Reconstructive Graph Instruction Tuning](https://arxiv.org/abs/2603.01385)

**基本信息**

- 🔗 arXiv: [`2603.01385`](https://arxiv.org/abs/2603.01385)
- 👥 作者: Zhongjian Zhang, Xiao Wang, Mengmei Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01385.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何让大语言模型（LLM）更好地理解和对齐图结构数据，这是构建能够处理分子图等复杂结构数据的“化学大模型”或“图基础模型”的关键技术挑战。

**📖 中文摘要**

本文旨在通过重构性图指令微调（RGLM）来改进图标记化大语言模型（GTokenLLMs）的图-文本对齐。论文指出，现有的GTokenLLMs仅依赖语言指令的文本监督，导致文本主导的偏见，未能充分利用图上下文。为了克服这一限制，作者从信息论角度证明对齐目标的上界是输入图与LLM中其隐藏表示之间的互信息，并提出通过重构图信息来显式引入图监督，以约束对齐过程。具体地，RGLM探索了从输入空间和潜在空间两个互补视角的三个变体。该工作为大语言模型理解图结构数据（如分子图、知识图谱）提供了新的对齐方法和理论分析，直接服务于开发通用的图基础模型这一目标，与化学信息学中利用大模型处理分子图数据的研究高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The remarkable success of large language models (LLMs) has motivated researchers to adapt them as universal predictors for various graph-related tasks, with the ultimate goal of developing a graph foundation model that generalizes diverse scenarios. The key challenge is to align graph data with language spaces so that LLMs can better comprehend graphs. As a popular paradigm, Graph-Tokenizing LLMs (GTokenLLMs) encode complex structures and lengthy texts into a graph token sequence, and then align them with text tokens via language instructions tuning. Despite their initial success, our information-theoretic analysis reveals that existing GTokenLLMs rely solely on text supervision from language instructions, which achieve only implicit graph-text alignment, resulting in a text-dominant bias that underutilizes graph context. To overcome this limitation, we first prove that the alignment objective is upper-bounded by the mutual information between the input graphs and their hidden representations in the LLM, which motivates us to improve this upper bound to achieve better alignment. To this end, we further propose a reconstructive graph instruction tuning pipeline, RGLM. Our key idea is to reconstruct the graph information from the LLM's graph token outputs, explicitly incorporating graph supervision to constrain the alignment process. Technically, we embody RGLM by exploring three distinct variants from two complementary perspectives: RGLM-Decoder from the input space; RGLM-Similarizer and RGLM-Denoiser from the latent space. Additionally, we theoretically analyze the alignment effectiveness of each variant. Extensive experiments on various benchmarks and task scenarios validate the effectiveness of the proposed RGLM, paving the way for new directions in GTokenLLMs' alignment research.

</details>

---

### 53. [Invariant-Stratified Propagation for Expressive Graph Neural Networks](https://arxiv.org/abs/2603.01388)

**基本信息**

- 🔗 arXiv: [`2603.01388`](https://arxiv.org/abs/2603.01388)
- 👥 作者: Asela Hevapathige, Ahad N. Zehmakan, Asiri Wijesinghe 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01388.pdf)

**💡 相关性分析**

满足标准1：论文专注于提升图神经网络的表达能力和结构感知能力，这是构建更强大、更能理解复杂分子结构的化学信息学模型（可视为化学大模型的组成部分）的核心基础研究。

**📖 中文摘要**

本文提出了不变分层传播（ISP）框架，包括一个新的WL变体（ISP-WL）及其高效的神经网络实现（ISPGNN），以解决图神经网络在表达能力和捕捉结构异质性方面的根本限制。ISP根据图不变量对节点进行分层，在分层中处理它们，揭示对1-WL不可见的结构区别。该框架通过分层结构异质性编码，量化节点在高级模式中结构位置的差异。论文提供了形式化理论分析，建立了超越1-WL的增强表达能力、收敛保证和固有的抗过度平滑性。虽然论文是通用的图学习研究，但其在提升图神经网络表达能力方面的创新，对于化学信息学中处理分子图至关重要。更强大的图神经网络是构建高性能化学性质预测模型、进行分子表示学习的核心组件，也是复杂“化学大模型”中处理结构信息的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph Neural Networks (GNNs) face fundamental limitations in expressivity and capturing structural heterogeneity. Standard message-passing architectures are constrained by the 1-dimensional Weisfeiler-Leman (1-WL) test, unable to distinguish graphs beyond degree sequences, and aggregate information uniformly from neighbors, failing to capture how nodes occupy different structural positions within higher-order patterns. While methods exist to achieve higher expressivity, they incur prohibitive computational costs and lack unified frameworks for flexibly encoding diverse structural properties. To address these limitations, we introduce Invariant-Stratified Propagation (ISP), a framework comprising both a novel WL variant (ISP-WL) and its efficient neural network implementation (ISPGNN). ISP stratifies nodes according to graph invariants, processing them in hierarchical strata that reveal structural distinctions invisible to 1-WL. Through hierarchical structural heterogeneity encoding, ISP quantifies differences in nodes' structural positions within higher-order patterns, distinguishing interactions where participants occupy different roles from those with uniform participation. We provide formal theoretical analysis establishing enhanced expressivity beyond 1-WL, convergence guarantees, and inherent resistance to oversmoothing. Extensive experiments across graph classification, node classification, and influence estimation demonstrate consistent improvements over standard architectures and state-of-the-art expressive baselines.

</details>

---

### 54. [HarmonyCell: Automating Single-Cell Perturbation Modeling under Semantic and Distribution Shifts](https://arxiv.org/abs/2603.01396)

**基本信息**

- 🔗 arXiv: [`2603.01396`](https://arxiv.org/abs/2603.01396)
- 👥 作者: Wenxuan Huang, Mingyu Tsoi, Yanhao Huang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01396.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用大语言模型（LLM）作为智能体来解决科学数据建模中的语义异构和模型设计自动化问题，这是“化学大模型”或“AI for Chemistry”中实现自动化、智能化科研的关键技术路径。

**📖 中文摘要**

本文提出了HarmonyCell，一个端到端的智能体框架，用于自动化单细胞扰动建模，以解决语义异质性和统计异质性两大瓶颈。其核心包括一个LLM驱动的语义统一器，用于自主将不同的元数据映射到规范接口；以及一个自适应蒙特卡洛树搜索引擎，用于合成具有最优统计归纳偏好的架构以应对分布偏移。该框架在包含语义和分布偏移的多种扰动任务上进行了评估。虽然应用领域是单细胞生物学，但其方法论的核心是使用大语言模型（LLM）作为智能体来处理科学数据中的语义异构问题，并自动进行模型架构搜索。这种“LLM智能体+自动化机器学习”的范式，对于化学信息学中处理来自不同数据库、具有不同标注规范的化学数据（如质谱数据库、分子数据库），以及自动化构建化学预测模型具有直接的启发和应用价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell perturbation studies face dual heterogeneity bottlenecks: (i) semantic heterogeneity--identical biological concepts encoded under incompatible metadata schemas across datasets; and (ii) statistical heterogeneity--distribution shifts from biological variation demanding dataset-specific inductive biases. We propose HarmonyCell, an end-to-end agent framework resolving each challenge through a dedicated mechanism: an LLM-driven Semantic Unifier autonomously maps disparate metadata into a canonical interface without manual intervention; and an adaptive Monte Carlo Tree Search engine operates over a hierarchical action space to synthesize architectures with optimal statistical inductive biases for distribution shifts. Evaluated across diverse perturbation tasks under both semantic and distribution shifts, HarmonyCell achieves a 95% valid execution rate on heterogeneous input datasets (versus 0% for general agents) while matching or even exceeding expert-designed baselines in rigorous out-of-distribution evaluations. This dual-track orchestration enables scalable automatic virtual cell modeling without dataset-specific engineering.

</details>

---

### 55. [SciDER: Scientific Data-centric End-to-end Researcher](https://arxiv.org/abs/2603.01421)

**基本信息**

- 🔗 arXiv: [`2603.01421`](https://arxiv.org/abs/2603.01421)
- 👥 作者: Ke Lin, Yilin Lu, Shreyas Bhat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01421.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于自动化科学发现的数据驱动端到端系统（SciDER），该系统能够处理和分析原始科学数据。这为化学信息学和质谱分析领域提供了潜在的数据处理工具和资源，可用于自动化质谱数据的解析和结构推理流程。

**📖 中文摘要**

本文介绍了SciDER，一个数据驱动的端到端自动化科研系统。该系统通过专门的智能体协作，能够解析和分析原始科学数据（例如来自科学实验的数据），并基于数据特征生成假设和实验设计，然后编写和执行相应的代码。论文强调其系统是一个模块化的Python包，旨在加速自主的、数据驱动的科学研究。虽然论文主要关注通用科学发现流程，但其核心是处理和分析原始科学数据（可能包括化学或质谱数据）以驱动假设生成和实验的自动化框架。这为化学信息学和质谱分析领域提供了潜在的工具和数据处理范式，可用于自动化质谱数据的解析和结构推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated scientific discovery with large language models is transforming the research lifecycle from ideation to experimentation, yet existing agents struggle to autonomously process raw data collected from scientific experiments. We introduce SciDER, a data-centric end-to-end system that automates the research lifecycle. Unlike traditional frameworks, our specialized agents collaboratively parse and analyze raw scientific data, generate hypotheses and experimental designs grounded in specific data characteristics, and write and execute corresponding code. Evaluation on three benchmarks shows SciDER excels in specialized data-driven scientific discovery and outperforms general-purpose agents and state-of-the-art models through its self-evolving memory and critic-led feedback loop. Distributed as a modular Python package, we also provide easy-to-use PyPI packages with a lightweight web interface to accelerate autonomous, data-driven research and aim to be accessible to all researchers and developers.

</details>

---

### 56. [Decoding Answers Before Chain-of-Thought: Evidence from Pre-CoT Probes and Activation Steering](https://arxiv.org/abs/2603.01437)

**基本信息**

- 🔗 arXiv: [`2603.01437`](https://arxiv.org/abs/2603.01437)
- 👥 作者: Kyle Cox, Darius Kianersi, Adrià Garriga-Alonso
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01437.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕药理学知识图谱的构建与应用，这是化学信息学的一个核心领域。它深入探讨了化学实体（药物）在知识图谱中的表示方法（包括是否需用化学结构），并用于预测药物-蛋白质相互作用，这与利用大模型进行化学性质预测和关系推理的主题高度相关。

**📖 中文摘要**

本文研究了药理学知识图谱在药物重定位中的应用。作者构建了一个包含药物、蛋白质和适应症等实体的药理学知识图谱，并严格评估了不同知识图谱嵌入模型和图神经网络在预测药物-蛋白质相互作用方面的性能。论文的核心是探索在药物重定位任务中，是否需要显式的药物化学结构信息。通过特征消融实验，作者发现仅使用药物网络拓扑结构和蛋白质特征（ESM-2嵌入），而不使用显式的化学结构表示，就能获得优异的预测性能。这项研究直接涉及化学信息学中的核心问题——如何有效表示和利用化学实体（药物）的信息进行下游预测任务（如药物-蛋白质相互作用、药物重定位）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As chain-of-thought (CoT) has become central to scaling reasoning capabilities in large language models (LLMs), it has also emerged as a promising tool for interpretability, suggesting the opportunity to understand model decisions through verbalized reasoning. However, the utility of CoT toward interpretability depends upon its faithfulness -- whether the model's stated reasoning reflects the underlying decision process. We provide mechanistic evidence that instruction-tuned models often determine their answer before generating CoT. Training linear probes on residual stream activations at the last token before CoT, we can predict the model's final answer with 0.9 AUC on most tasks. We find that these directions are not only predictive, but also causal: steering activations along the probe direction flips model answers in over 50% of cases, significantly exceeding orthogonal baselines. When steering induces incorrect answers, we observe two distinct failure modes: non-entailment (stating correct premises but drawing unsupported conclusions) and confabulation (fabricating false premises). While post-hoc reasoning may be instrumentally useful when the model has a correct pre-CoT belief, these failure modes suggest it can result in undesirable behaviors when reasoning from a false belief.

</details>

---

### 57. [ProtRLSearch: A Multi-Round Multimodal Protein Search Agent with Large Language Models Trained via Reinforcement Learning](https://arxiv.org/abs/2603.01464)

**基本信息**

- 🔗 arXiv: [`2603.01464`](https://arxiv.org/abs/2603.01464)
- 👥 作者: Congying Liu, Taihao Li, Ming Huang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01464.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个用于蛋白质分析的多模态搜索智能体，它直接处理蛋白质序列（一种重要的化学/生物分子表示）并与文本信息融合进行推理。这属于化学信息学中“大模型”应用于分子（此处为生物大分子）分析和推理的范畴。

**📖 中文摘要**

本文提出了ProtRLSearch，一个用于蛋白质分析的多轮、多模态搜索智能体。该智能体能够联合利用蛋白质序列和文本作为多模态输入，在实时搜索中做出决策，以生成高质量的蛋白质分析报告。为了解决蛋白质序列信息与文本信息的多模态融合问题，论文构建了ProtMCQs基准数据集，用于评估模型在蛋白质查询任务中的能力，这些任务包括基于序列约束的蛋白质功能推理、表型变化分析等。这项工作将大型语言模型与蛋白质序列信息相结合，用于蛋白质相关的推理和搜索，是化学信息学与生物信息学交叉领域的前沿探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein analysis tasks arising in healthcare settings often require accurate reasoning under protein sequence constraints, involving tasks such as functional interpretation of disease-related variants, protein-level analysis for clinical research, and similar scenarios. To address such tasks, search agents are introduced to search protein-related information, providing support for disease-related variant analysis and protein function reasoning in protein-centric inference. However, such search agents are mostly limited to single-round, text-only modality search, which prevents the protein sequence modality from being incorporated as a multimodal input into the search decision-making process. Meanwhile, their reliance on reinforcement learning (RL) supervision that focuses solely on the final answer results in a lack of search process constraints, making deviations in keyword selection and reasoning directions difficult to identify and correct in a timely manner. To address these limitations, we propose ProtRLSearch, a multi-round protein search agent trained with multi-dimensional reward based RL, which jointly leverages protein sequence and text as multimodal inputs during real-time search to produce high quality reports. To evaluate the ability of models to integrate protein sequence information and text-based multimodal inputs in realistic protein query settings, we construct ProtMCQs, a benchmark of 3,000 multiple choice questions (MCQs) organized into three difficulty levels. The benchmark evaluates protein query tasks that range from sequence constrained reasoning about protein function and phenotype changes to comprehensive protein reasoning that integrates multi-dimensional sequence features with signal pathways and regulatory networks.

</details>

---

### 58. [Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification](https://arxiv.org/abs/2603.01511)

**基本信息**

- 🔗 arXiv: [`2603.01511`](https://arxiv.org/abs/2603.01511)
- 👥 作者: Jiayang Wu, Jiale Zhou, Xingyi Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01511.pdf)

**💡 相关性分析**

满足标准1：论文专注于开发多模态大模型（混合专家）框架，用于蛋白质活性位点的识别。这直接涉及化学信息学中利用人工智能模型进行分子（蛋白质）功能与结构预测的核心主题。

**📖 中文摘要**

本文提出了MERA，一个用于蛋白质活性位点识别的、基于检索增强的多模态混合专家模型。该框架整合了组织病理学切片（WSI）、病理报告文本和细胞核图等多模态信息，通过分层多专家检索和基于证据理论的可靠性感知融合策略，来精确识别蛋白质（在组织中的）活性位点。论文在蛋白质活性位点预测和肽结合位点识别任务上进行了评估。这项工作属于计算生物学和化学信息学的交叉领域，它利用多模态大模型和检索增强技术来解决蛋白质功能位点预测这一关键问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate identification of protein active sites at the residue level is crucial for understanding protein function and advancing drug discovery. However, current methods face two critical challenges: vulnerability in single-instance prediction due to sparse training data, and inadequate modality reliability estimation that leads to performance degradation when unreliable modalities dominate fusion processes. To address these challenges, we introduce Multimodal Mixture-of-Experts with Retrieval Augmentation (MERA), the first retrieval-augmented framework for protein active site identification. MERA employs hierarchical multi-expert retrieval that dynamically aggregates contextual information from chain, sequence, and active-site perspectives through residue-level mixture-of-experts gating. To prevent modality degradation, we propose a reliability-aware fusion strategy based on Dempster-Shafer evidence theory that quantifies modality trustworthiness through belief mass functions and learnable discounting coefficients, enabling principled multimodal integration. Extensive experiments on ProTAD-Gen and TS125 datasets demonstrate that MERA achieves state-of-the-art performance, with 90% AUPRC on active site prediction and significant gains on peptide-binding site identification, validating the effectiveness of retrieval-augmented multi-expert modeling and reliability-guided fusion.

</details>

---

### 59. [Pharmacology Knowledge Graphs: Do We Need Chemical Structure for Drug Repurposing?](https://arxiv.org/abs/2603.01537)

**基本信息**

- 🔗 arXiv: [`2603.01537`](https://arxiv.org/abs/2603.01537)
- 👥 作者: Youssef Abo-Dahab, Ruby Hernandez, Ismael Caleb Arechiga Duran
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01537.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是药理学知识图谱与药物重定位，这是化学信息学的核心应用。它深入分析了化学结构表示在知识图谱预测任务中的作用，直接关联到“化学大模型”中如何有效嵌入和利用分子信息的问题。

**📖 中文摘要**

本文深入研究了药理学知识图谱在药物重定位中的应用，并重点探讨了化学结构信息在此任务中的必要性。作者构建了一个大规模的药理学知识图谱，并进行了严格的时序验证。通过系统的实验（包括模型缩放、特征消融），论文发现，仅使用药物在网络中的拓扑结构（关系）和蛋白质特征，而不使用显式的药物化学结构编码器，就能取得优异的预测性能，甚至优于包含化学结构的方法。这项研究对化学信息学中如何表示分子（药物）以用于知识图谱推理和预测任务提供了重要的实证见解，挑战了“必须使用化学结构”的传统观念。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The contributions of model complexity, data volume, and feature modalities to knowledge graph-based drug repurposing remain poorly quantified under rigorous temporal validation. We constructed a pharmacology knowledge graph from ChEMBL 36 comprising 5,348 entities including 3,127 drugs, 1,156 proteins, and 1,065 indications. A strict temporal split was enforced with training data up to 2022 and testing data from 2023 to 2025, together with biologically verified hard negatives mined from failed assays and clinical trials. We benchmarked five knowledge graph embedding models and a standard graph neural network with 3.44 million parameters that incorporates drug chemical structure using a graph attention encoder and ESM-2 protein embeddings. Scaling experiments ranging from 0.78 to 9.75 million parameters and from 25 to 100 percent of the data, together with feature ablation studies, were used to isolate the contributions of model capacity, graph density, and node feature modalities. Removing the graph attention based drug structure encoder and retaining only topological embeddings combined with ESM-2 protein features improved drug protein PR-AUC from 0.5631 to 0.5785 while reducing VRAM usage from 5.30 GB to 353 MB. Replacing the drug encoder with Morgan fingerprints further degraded performance, indicating that explicit chemical structure representations can be detrimental for predicting pharmacological network interactions. Increasing model size beyond 2.44 million parameters yielded diminishing returns, whereas increasing training data consistently improved performance. External validation confirmed 6 of the top 14 novel predictions as established therapeutic indications. These results show that drug pharmacological behavior can be accurately predicted using target-centric information and drug network topology alone, without requiring explicit chemical structure representations.

</details>

---

### 60. [Graph-centric Cross-model Data Integration and Analytics in a Unified Multi-model Database](https://arxiv.org/abs/2603.01598)

**基本信息**

- 🔗 arXiv: [`2603.01598`](https://arxiv.org/abs/2603.01598)
- 👥 作者: Zepeng Liu, Sheng Wang, Shixun Huang 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01598.pdf)

**💡 相关性分析**

满足标准1：论文提出的以图为中心的跨模型数据集成与分析框架，其核心思想（利用图结构进行信息关联与复杂分析）与化学信息学中利用图神经网络构建和处理化学大模型（分子图模型）的核心主题直接相关。

**📖 中文摘要**

本文提出了一种以图模型为中心的跨模型数据集成与分析（GCDIA）方法，并在统一的多模型数据库GredoDB中实现。该方法的核心是利用图模型作为中心范式，集成来自异构数据模型（如关系型和文档型）的相关信息，并执行复杂的分析任务，如回归和相似性计算。虽然论文主要关注通用数据库系统，但其提出的图中心集成与分析方法，特别是利用图结构进行信息关联和复杂推理的框架，与化学信息学中利用图神经网络（GNN）处理分子结构图、进行性质预测或结构推理的核心思路高度一致。因此，该论文提出的方法和技术路线为构建用于化学大模型（特别是基于图表示的模型）的数据集成与分析平台提供了重要的技术参考和架构思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-centric cross-model data integration and analytics (GCDIA) refer to tasks that leverage the graph model as a central paradigm to integrate relevant information across heterogeneous data models, such as relational and document, and subsequently perform complex analytics such as regression and similarity computation. As modern applications generate increasingly diverse data and move beyond simple retrieval toward advanced analytical objectives (e.g., prediction and recommendation), GCDIA has become increasingly important. Existing multi-model databases (MMDBs) struggle to efficiently support both integration (GCDI) and analytics (GCDA) in GCDIA. They typically separate graph processing from other models without global optimization for GCDI, while relying on tuple-at-a-time execution for GCDA, leading to limited performance and scalability. To address these limitations, we propose GredoDB, a unified MMDB that natively supports storing graph, relational, and document models, while efficiently processing GCDIA. Specifically, we design 1) topology- and attribute-aware graph operators for efficient predicate-aware traversal, 2) a unified GCDI optimization framework to exploit cross-model correlations, and 3) a parallel GCDA architecture that materializes intermediate results for operator-level execution. Experiments on the widely adopted multi-model benchmark M2Bench demonstrate that, in terms of response time, GredoDB achieves up to 107.89 times and an average of 10.89 times speedup on GCDI, and up to 356.72 times and an average of 37.79 times on GCDA, compared to state-of-the-art (SOTA) MMDBs.

</details>

---

### 61. [CeProAgents: A Hierarchical Agents System for Automated Chemical Process Development](https://arxiv.org/abs/2603.01654)

**基本信息**

- 🔗 arXiv: [`2603.01654`](https://arxiv.org/abs/2603.01654)
- 👥 作者: Yuhang Yang, Ruikang Li, Jifei Ma 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01654.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用大型语言模型（作为化学领域大模型的一种形式）和智能体技术来自动化化学过程开发，是“化学大模型”主题在工业化学工程中的具体应用和系统性探索。

**📖 中文摘要**

本文提出了CeProAgents，一个用于自动化化学过程开发的分层多智能体系统。该系统由专注于知识、概念和参数的三组专业智能体组成，通过协作分工来模拟化学工程师的开发流程。为了系统评估，作者建立了CeProBench基准，该基准围绕化学工程的三个核心维度构建了六种不同类型的任务，以全面评估系统在化学过程开发中的综合能力。这项工作直接应用大型语言模型（LLM）和智能体技术来解决化学工程中的核心问题，是“化学大模型”在特定工业领域（过程开发）的具象化实现和评估范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of chemical processes, a cornerstone of chemical engineering, presents formidable challenges due to its multi-faceted nature, integrating specialized knowledge, conceptual design, and parametric simulation. Capitalizing on this, we propose CeProAgents, a hierarchical multi-agent system designed to automate the development of chemical process through collaborative division of labor. Our architecture comprises three specialized agent cohorts focused on knowledge, concept, and parameter respectively. To effectively adapt to the inherent complexity of chemical tasks, each cohort employs a novel hybrid architecture that integrates dynamic agent chatgroups with structured agentic workflows. To rigorously evaluate the system, we establish CeProBench, a multi-dimensional benchmark structured around three core pillars of chemical engineering. We design six distinct types of tasks across these dimensions to holistically assess the comprehensive capabilities of the system in chemical process development. The results not only confirm the effectiveness and superiority of our proposed approach but also reveal the transformative potential as well as the current boundaries of Large Language Models (LLMs) for industrial chemical engineering.

</details>

---

### 62. [Transform-Invariant Generative Ray Path Sampling for Efficient Radio Propagation Modeling](https://arxiv.org/abs/2603.01655)

**基本信息**

- 🔗 arXiv: [`2603.01655`](https://arxiv.org/abs/2603.01655)
- 👥 作者: Jérome Eertmans, Enrico M. Vitucci, Vittorio Degli-Esposti 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01655.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于生成流网络（GFlowNets）的智能组合空间采样框架，其方法论与质谱结构推理中从高维、组合性的分子结构空间中进行高效搜索和推断的核心问题直接相关，为解决类似推理问题提供了新的技术思路。

**📖 中文摘要**

本文提出了一种基于生成流网络（GFlowNets）的机器学习辅助框架，用于高效无线电传播建模中的智能射线路径采样，以替代计算复杂度呈指数增长的传统穷举射线追踪。该框架通过引入经验回放缓冲区、均匀探索策略和基于物理的动作掩码等关键组件，解决了生成模型在此领域应用中的挑战（如稀疏奖励、收敛困难）。论文展示了该方法在保持高覆盖精度的同时，能显著加速复杂传播路径的发现。虽然应用领域是无线通信，但其核心方法——使用生成模型进行组合空间（路径搜索空间）的高效、结构化探索与采样——与质谱分析中“质谱结构推理”的核心挑战（从质谱数据中高效搜索和推断可能的分子结构空间）在方法论上高度同构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ray tracing has become a standard for accurate radio propagation modeling, but suffers from exponential computational complexity, as the number of candidate paths scales with the number of objects raised to the power of the interaction order. This bottleneck limits its use in large-scale or real-time applications, forcing traditional tools to rely on heuristics to reduce the number of path candidates at the cost of potentially reduced accuracy. To overcome this limitation, we propose a comprehensive machine-learning-assisted framework that replaces exhaustive path searching with intelligent sampling via Generative Flow Networks. Applying such generative models to this domain presents significant challenges, particularly sparse rewards due to the rarity of valid paths, which can lead to convergence failures and trivial solutions when evaluating high-order interactions in complex environments. To ensure robust learning and efficient exploration, our framework incorporates three key architectural components. First, we implement an \emph{experience replay buffer} to capture and retain rare valid paths. Second, we adopt a uniform exploratory policy to improve generalization and prevent the model from overfitting to simple geometries. Third, we apply a physics-based action masking strategy that filters out physically impossible paths before the model even considers them. As demonstrated in our experimental validation, the proposed model achieves substantial speedups over exhaustive search -- up to $10\times$ faster on GPU and $1000\times$ faster on CPU -- while maintaining high coverage accuracy and successfully uncovering complex propagation paths. The complete source code, tests, and tutorial are available at this https URL .

</details>

---

### 63. [A Diffusion-Driven Fine-Grained Nodule Synthesis Framework for Enhanced Lung Nodule Detection from Chest Radiographs](https://arxiv.org/abs/2603.01659)

**基本信息**

- 🔗 arXiv: [`2603.01659`](https://arxiv.org/abs/2603.01659)
- 👥 作者: Aryan Goyal, Shreshtha Singh, Ashish Mittal 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01659.pdf)

**💡 相关性分析**

满足标准2：论文提出的扩散模型与LoRA结合的可控合成数据生成框架，为生成用于训练领域大模型（如化学大模型）或解决特定推理任务（如质谱结构推理）所需的高质量、特征可控的合成数据集提供了重要的方法工具和资源思路。

**📖 中文摘要**

本文提出了一种基于扩散模型和低秩适配器（LoRA）的框架，用于在胸部X光片上实现特征可控的肺结节合成。该框架通过结节掩码条件训练控制大小和形状，并训练独立的LoRA模块来控制特定的放射学特征（如纹理、边界）。为了解决多特征协同控制的问题，论文引入了新颖的正交性损失项来改进LoRA的组合训练。生成的合成结节数据用于增强下游结节检测模型的性能。这项工作展示了扩散模型和参数高效微调技术在生成特定领域（医学影像）可控合成数据方面的应用，其“可控生成”和“数据增强”的思路对于构建和扩充用于训练“化学大模型”或“质谱结构推理”模型的专用数据集具有直接的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early detection of lung cancer in chest radiographs (CXRs) is crucial for improving patient outcomes, yet nodule detection remains challenging due to their subtle appearance and variability in radiological characteristics like size, texture, and boundary. For robust analysis, this diversity must be well represented in training datasets for deep learning based Computer-Assisted Diagnosis (CAD) systems. However, assembling such datasets is costly and often impractical, motivating the need for realistic synthetic data generation. Existing methods lack fine-grained control over synthetic nodule generation, limiting their utility in addressing data scarcity. This paper proposes a novel diffusion-based framework with low-rank adaptation (LoRA) adapters for characteristic controlled nodule synthesis on CXRs. We begin by addressing size and shape control through nodule mask conditioned training of the base diffusion model. To achieve individual characteristic control, we train separate LoRA modules, each dedicated to a specific radiological feature. However, since nodules rarely exhibit isolated characteristics, effective multi-characteristic control requires a balanced integration of features. We address this by leveraging the dynamic composability of LoRAs and revisiting existing merging strategies. Building on this, we identify two key issues, overlapping attention regions and non-orthogonal parameter spaces. To overcome these limitations, we introduce a novel orthogonality loss term during LoRA composition training. Extensive experiments on both in-house and public datasets demonstrate improved downstream nodule detection. Radiologist evaluations confirm the fine-grained controllability of our generated nodules, and across multiple quantitative metrics, our method surpasses existing nodule generation approaches for CXRs.

</details>

---

### 64. [QIME: Constructing Interpretable Medical Text Embeddings via Ontology-Grounded Questions](https://arxiv.org/abs/2603.01690)

**基本信息**

- 🔗 arXiv: [`2603.01690`](https://arxiv.org/abs/2603.01690)
- 👥 作者: Yixuan Tang, Zhenghong Lin, Yandong Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01690.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于本体和问题构建可解释嵌入的框架，其核心思想（将复杂数据表示为结构化、可解释的语义问题答案）与构建可解释的“化学大模型”或“质谱分析模型”的研究主题直接相关，提供了一种新颖的模型表示和解释思路。

**📖 中文摘要**

本文提出了QIME（Ontology-grounded Questions for Interpretable Medical Embeddings）框架，用于构建可解释的医学文本嵌入。该框架的每个维度对应一个具有临床意义的“是/否”问题。通过基于医学本体概念签名生成语义原子化的问题，QIME能够捕捉生物医学文本中的细粒度区别。此外，它支持一种无需训练的分类器构建策略来创建嵌入。在生物医学语义相似性、聚类和检索基准测试中，QIME的性能优于先前的可解释嵌入方法，并显著缩小了与强大黑盒生物医学编码器的差距。这种方法将文本表示为对一系列问题的答案，这种“问题-答案”式的结构化、可解释表示范式，对于构建化学或质谱领域的可解释大模型（例如，将分子或谱图表示为对一系列化学或光谱学问题的回答）具有重要的启发价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While dense biomedical embeddings achieve strong performance, their black-box nature limits their utility in clinical decision-making. Recent question-based interpretable embeddings represent text as binary answers to natural-language questions, but these approaches often rely on heuristic or surface-level contrastive signals and overlook specialized domain knowledge. We propose QIME, an ontology-grounded framework for constructing interpretable medical text embeddings in which each dimension corresponds to a clinically meaningful yes/no question. By conditioning on cluster-specific medical concept signatures, QIME generates semantically atomic questions that capture fine-grained distinctions in biomedical text. Furthermore, QIME supports a training-free embedding construction strategy that eliminates per-question classifier training while further improving performance. Experiments across biomedical semantic similarity, clustering, and retrieval benchmarks show that QIME consistently outperforms prior interpretable embedding methods and substantially narrows the gap to strong black-box biomedical encoders, while providing concise and clinically informative explanations.

</details>

---

### 65. [Solving Inverse PDE Problems using Minimization Methods and AI](https://arxiv.org/abs/2603.01731)

**基本信息**

- 🔗 arXiv: [`2603.01731`](https://arxiv.org/abs/2603.01731)
- 👥 作者: Noura Helwani, Sophie Moufawad, Georges Sakr
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01731.pdf)

**💡 相关性分析**

满足标准1：论文核心研究了使用PINNs等AI方法求解PDE反问题，这与“质谱结构推理”本质上同属于从观测数据推断底层系统参数/结构的反问题求解范畴，方法论上直接相关。

**📖 中文摘要**

本文研究了使用最小化方法和人工智能（特别是物理信息神经网络PINNs）求解偏微分方程（PDE）的正问题和反问题。论文首先在逻辑微分方程上验证数值方案和PINN性能，然后针对无一般闭式解的非线性多孔介质方程（PME），构建了强大的正问题求解器，并测试了反问题中的参数估计技术。结果表明，PINNs能够以有竞争力的计算成本密切估计解，从而为求解复杂系统的正反问题提供了有效工具。求解PDE反问题（即从观测数据推断系统参数）与“质谱结构推理”（从质谱数据推断分子结构参数）在数学形式上同属反问题范畴。因此，论文评估的PINNs等方法为质谱结构推理这类科学反问题提供了潜在且强大的求解工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many physical and engineering systems require solving direct problems to predict behavior and inverse problems to determine unknown parameters from measurement. In this work, we study both aspects for systems governed by differential equations, contrasting well-established numerical methods with new AI-based techniques, specifically Physics-Informed Neural Networks (PINNs). We first analyze the logistic differential equation, using its closed-form solution to verify numerical schemes and validate PINN performance. We then address the Porous Medium Equation (PME), a nonlinear partial differential equation with no general closed-form solution, building strong solvers of the direct problem and testing techniques for parameter estimation in the inverse problem. Our results suggest that PINNs can closely estimate solutions at competitive computational cost, and thus propose an effective tool for solving both direct and inverse problems for complex systems.

</details>

---

### 66. [Practical Deep Heteroskedastic Regression](https://arxiv.org/abs/2603.01750)

**基本信息**

- 🔗 arXiv: [`2603.01750`](https://arxiv.org/abs/2603.01750)
- 👥 作者: Mikkel Jordahn, Jonas Vestergaard Jensen, James Harrison 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01750.pdf)

**💡 相关性分析**

满足标准1：论文的研究直接应用于化学信息学中的分子图数据集，并提出了改进深度回归模型不确定性估计的实用方法，这对于构建和评估可靠的化学预测大模型（核心主题）具有直接价值。

**📖 中文摘要**

本文研究了深度学习回归中的异方差不确定性量化（UQ）问题。针对训练深度异方差回归模型时存在的优化困难、表示崩溃和方差过拟合等实际挑战，论文提出了一种简单高效的流程：在预训练网络的中间层上，使用留出数据集事后拟合一个方差模型。该方法在多个分子图数据集上实现了与现有方法相当或更优的不确定性量化，且不影响均值预测精度。这项工作直接应用于分子图数据集，是化学信息学领域的典型应用。其提出的改进深度模型不确定性估计的实用方法，对于构建可靠、可信任的“化学大模型”（尤其是用于回归预测任务的模型）至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Uncertainty quantification (UQ) in deep learning regression is of wide interest, as it supports critical applications including sequential decision making and risk-sensitive tasks. In heteroskedastic regression, where the uncertainty of the target depends on the input, a common approach is to train a neural network that parameterizes the mean and the variance of the predictive distribution. Still, training deep heteroskedastic regression models poses practical challenges in the trade-off between uncertainty quantification and mean prediction, such as optimization difficulties, representation collapse, and variance overfitting. In this work we identify previously undiscussed fallacies and propose a simple and efficient procedure that addresses these challenges jointly by post-hoc fitting a variance model across the intermediate layers of a pretrained network on a hold-out dataset. We demonstrate that our method achieves on-par or state-of-the-art uncertainty quantification on several molecular graph datasets, without compromising mean prediction accuracy and remaining cheap to use at prediction time.

</details>

---

### 67. [Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence](https://arxiv.org/abs/2603.01752)

**基本信息**

- 🔗 arXiv: [`2603.01752`](https://arxiv.org/abs/2603.01752)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01752.pdf)

**💡 相关性分析**

满足标准1：论文对生物学基础模型进行因果可解释性分析的方法论，与理解和解释“化学大模型”内部工作机制这一核心研究主题直接相关，提供了重要的分析技术参考。

**📖 中文摘要**

本文对单细胞生物学基础模型（Geneformer V2-316M和scGPT）进行了因果电路追踪分析。通过稀疏自编码器（SAE）分解模型激活并应用特征消融来测量下游响应，作者揭示了这些模型中特征间相互作用的因果结构。研究发现两个模型都表现出高度的生物一致性和抑制性主导，并且跨模型共识产生了大量保守的域对，其中疾病相关域更可能成为共识。这项工作首次在生物学基础模型中系统性地揭示了其内部计算的因果架构。虽然模型领域是生物学，但其方法论——对大规模预训练基础模型进行可解释性分析和因果发现——完全适用于“化学大模型”。该论文为理解和解释化学领域大模型（如分子预训练模型）的内部工作机制提供了前沿的分析框架和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: Sparse autoencoders (SAEs) decompose foundation model activations into interpretable features, but causal feature-to-feature interactions across network depth remain unknown for biological foundation models. Results: We introduce causal circuit tracing by ablating SAE features and measuring downstream responses, and apply it to Geneformer V2-316M and scGPT whole-human across four conditions (96,892 edges, 80,191 forward passes). Both models show approximately 53 percent biological coherence and 65 to 89 percent inhibitory dominance, invariant to architecture and cell type. scGPT produces stronger effects (mean absolute d = 1.40 vs. 1.05) with more balanced dynamics. Cross-model consensus yields 1,142 conserved domain pairs (10.6x enrichment, p < 0.001). Disease-associated domains are 3.59x more likely to be consensus. Gene-level CRISPRi validation shows 56.4 percent directional accuracy, confirming co-expression rather than causal encoding.

</details>

---

### 68. [D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation](https://arxiv.org/abs/2603.01780)

**基本信息**

- 🔗 arXiv: [`2603.01780`](https://arxiv.org/abs/2603.01780)
- 👥 作者: Zhao Yang, Hengchang Liu, Chuan Cao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01780.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于DNA序列理解和生成的化学大模型（D3LM），这直接属于‘化学大模型’主题。

**📖 中文摘要**

本文提出了D3LM，一个用于DNA序列理解和生成的离散DNA扩散语言模型。该模型采用掩码扩散训练目标，在统一的架构中实现了对DNA序列的双向理解（如调控元件识别）和生成能力。与早期基于BERT或自回归的DNA基础模型相比，D3LM在理解任务上表现更优，并在调控元件生成任务上取得了接近真实DNA序列的质量。这项工作将扩散语言模型确立为构建统一DNA基础模型的一个有前景的范式，并首次系统性地研究了DNA领域的掩码扩散模型设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early DNA foundation models adopted BERT-style training, achieving good performance on DNA understanding tasks but lacking generative capabilities. Recent autoregressive models enable DNA generation, but employ left-to-right causal modeling that is suboptimal for DNA where regulatory relationships are inherently bidirectional. We present D3LM (\textbf{D}iscrete \textbf{D}NA \textbf{D}iffusion \textbf{L}anguage \textbf{M}odel), which unifies bidirectional representation learning and DNA generation through masked diffusion. D3LM directly adopts the Nucleotide Transformer (NT) v2 architecture but reformulates the training objective as masked diffusion in discrete DNA space, enabling both bidirectional understanding and generation capabilities within a single model. Compared to NT v2 of the same size, D3LM achieves improved performance on understanding tasks. Notably, on regulatory element generation, D3LM achieves an SFID of 10.92, closely approaching real DNA sequences (7.85) and substantially outperforming the previous best result of 29.16 from autoregressive models. Our work suggests diffusion language models as a promising paradigm for unified DNA foundation models. We further present the first systematic study of masked diffusion models in the DNA domain, investigating practical design choices such as tokenization schemes and sampling strategies, thereby providing empirical insights and a solid foundation for future research. D3LM has been released at this https URL .

</details>

---

### 69. [CTForensics: A Comprehensive Dataset and Method for AI-Generated CT Image Detection](https://arxiv.org/abs/2603.01878)

**基本信息**

- 🔗 arXiv: [`2603.01878`](https://arxiv.org/abs/2603.01878)
- 👥 作者: Yiheng Li, Zichang Tan, Guoqing Xu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01878.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是检测AI生成的医学影像（CT），这涉及化学/医学成像领域的生成式模型（化学大模型）及其安全评估。同时，论文提出了一个综合性的数据集CTForensics，这提供了可用于相关主题研究的数据资源。

**📖 中文摘要**

本文提出了CTForensics，一个用于检测AI生成的CT图像的综合性数据集和方法。随着生成式AI在医学成像中的快速发展，合成CT图像在带来应用潜力的同时也引入了严重的安全风险。该研究构建了一个包含十种不同CT生成方法的数据集，以系统评估检测方法的泛化能力。同时，作者提出了ESF-CTFD，一种高效的CNN网络，通过在小波、空间和频率域捕捉伪造痕迹来检测CT图像的真伪。这项工作直接针对生成式AI在化学/医学成像领域的应用及其安全检测，属于化学信息学中数据处理和模型安全的重要议题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rapid development of generative AI in medical imaging, synthetic Computed Tomography (CT) images have demonstrated great potential in applications such as data augmentation and clinical diagnosis, but they also introduce serious security risks. Despite the increasing security concerns, existing studies on CT forgery detection are still limited and fail to adequately address real-world challenges. These limitations are mainly reflected in two aspects: the absence of datasets that can effectively evaluate model generalization to reflect the real-world application requirements, and the reliance on detection methods designed for natural images that are insensitive to CT-specific forgery artifacts. In this view, we propose CTForensics, a comprehensive dataset designed to systematically evaluate the generalization capability of CT forgery detection methods, which includes ten diverse CT generative methods. Moreover, we introduce the Enhanced Spatial-Frequency CT Forgery Detector (ESF-CTFD), an efficient CNN-based neural network that captures forgery cues across the wavelet, spatial, and frequency domains. First, it transforms the input CT image into three scales and extracts features at each scale via the Wavelet-Enhanced Central Stem. Then, starting from the largest-scale features, the Spatial Process Block gradually performs feature fusion with the smaller-scale ones. Finally, the Frequency Process Block learns frequency-domain information for predicting the final results. Experiments demonstrate that ESF-CTFD consistently outperforms existing methods and exhibits superior generalization across different CT generative models.

</details>

---

### 70. [MobileMold: A Smartphone-Based Microscopy Dataset for Food Mold Detection](https://arxiv.org/abs/2603.01944)

**基本信息**

- 🔗 arXiv: [`2603.01944`](https://arxiv.org/abs/2603.01944)
- 👥 作者: Dinh Nam Pham, Leonard Prokisch, Bennet Meyer 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01944.pdf)

**💡 相关性分析**

满足标准2：论文提供了MobileMold数据集，这是一个用于食品霉菌检测的智能手机显微镜图像数据集，可作为化学信息学或分析检测领域模型训练的数据资源。

**📖 中文摘要**

本文介绍了MobileMold，一个基于智能手机显微镜的开源数据集，用于食品霉菌检测和食品分类。该数据集包含4941张手持显微镜图像，涵盖11种食物类型，并使用多种智能手机和显微镜附件在真实条件下采集。研究为霉菌检测和食品分类任务建立了基线模型，并展示了利用智能手机和低成本附件进行化学/生物传感的潜力。这项工作为开发可访问的食品安全传感和移动成像应用提供了数据基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Smartphone clip-on microscopes turn everyday devices into low-cost, portable imaging systems that can even reveal fungal structures at the microscopic level, enabling mold inspection beyond unaided visual checks. In this paper, we introduce MobileMold, an open smartphone-based microscopy dataset for food mold detection and food classification. MobileMold contains 4,941 handheld microscopy images spanning 11 food types, 4 smartphones, 3 microscopes, and diverse real-world conditions. Beyond the dataset release, we establish baselines for (i) mold detection and (ii) food-type classification, including a multi-task setting that predicts both attributes. Across multiple pretrained deep learning architectures and augmentation strategies, we obtain near-ceiling performance (accuracy = 0.9954, F1 = 0.9954, MCC = 0.9907), validating the utility of our dataset for detecting food spoilage. To increase transparency, we complement our evaluation with saliency-based visual explanations highlighting mold regions associated with the model's predictions. MobileMold aims to contribute to research on accessible food-safety sensing, mobile imaging, and exploring the potential of smartphones enhanced with attachments.

</details>

---

### 71. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interaction Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于材料科学的机器学习相互作用势（MatRIS），这是一种特定领域的化学大模型，旨在准确高效地模拟原子间相互作用，属于化学信息学和计算化学的核心范畴。

**📖 中文摘要**

本文介绍了MatRIS，一种用于材料科学的机器学习相互作用势（MLIP）。MLIP是化学信息学和计算材料科学中的核心工具，用于预测原子间的相互作用能。MatRIS作为一种不变量MLIP，引入了基于注意力的三体相互作用建模，具有线性复杂度，在保持高精度的同时显著提升了计算效率。论文在多个标准基准（如Matbench-Discovery、MatPES等）上验证了其性能，表明其精度可与领先的等变模型相媲美，但训练成本更低。这项工作直接涉及化学大模型（用于材料科学的机器学习模型）的开发，旨在构建更准确、高效的原子尺度模拟工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 72. [OpenRad: a Curated Repository of Open-access AI models for Radiology](https://arxiv.org/abs/2603.02062)

**基本信息**

- 🔗 arXiv: [`2603.02062`](https://arxiv.org/abs/2603.02062)
- 👥 作者: Konstantinos Vrettos, Galini Papadaki, Emmanouil Brilakis 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02062.pdf)

**💡 相关性分析**

满足标准2：论文提出了OpenRad，这是一个经过精心策划、包含标准化元数据的大规模AI模型存储库。它提供了一种系统化的方法来聚合、描述和管理科学模型资源。这种为特定领域（此处为放射学）构建可搜索、可复现模型库的框架和方法，可以直接借鉴用于构建化学信息学或质谱分析领域的模型、工具或数据集资源库。

**📖 中文摘要**

本文介绍了OpenRad，一个经过人工审核、标准化的开放获取放射学AI模型存储库。该研究通过回顾性分析文献和预印本，使用本地部署的大语言模型（LLM）基于RSNA AI路线图JSON模式自动提取模型元数据，并由专家审核，最终收录了约1700个模型。OpenRad提供了基于模态、亚专业、预期用途等条件的搜索和筛选功能。这项工作创建了一个集中的、可搜索的资源，旨在提高放射学AI模型的可发现性、可重复性和临床转化潜力。虽然其直接应用在医学影像，但其构建大规模、标准化模型库的方法论，以及利用LLM进行自动化元数据提取和管理的流程，对于构建和管理其他科学领域（如化学信息学）的模型和数据资源具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid developments in artificial intelligence (AI) research in radiology have produced numerous models that are scattered across various platforms and sources, limiting discoverability, reproducibility and clinical translation. Herein, OpenRad was created, a curated, standardized, open-access repository that aggregates radiology AI models and providing details such as the availability of pretrained weights and interactive applications. Retrospective analysis of peer reviewed literature and preprints indexed in PubMed, arXiv and Scopus was performed until Dec 2025 (n = 5239 records). Model records were generated using a locally hosted LLM (gpt-oss:120b), based on the RSNA AI Roadmap JSON schema, and manually verified by ten expert reviewers. Stability of LLM outputs was assessed on 225 randomly selected papers using text similarity metrics. A total of 1694 articles were included after review. Included models span all imaging modalities (CT, MRI, X-ray, US) and radiology subspecialties. Automated extraction demonstrated high stability for structured fields (Levenshtein ratio > 90%), with 78.5% of record edits being characterized as minor during expert review. Statistical analysis of the repository revealed CNN and transformer architectures as dominant, while MRI was the most commonly used modality (in 621 neuroradiology AI models). Research output was mostly concentrated in China and the United States. The OpenRad web interface enables model discovery via keyword search and filters for modality, subspecialty, intended use, verification status and demo availability, alongside live statistics. The community can contribute new models through a dedicated portal. OpenRad contains approx. 1700 open access, curated radiology AI models with standardized metadata, supplemented with analysis of code repositories, thereby creating a comprehensive, searchable resource for the radiology community.

</details>

---

### 73. [Generative AI in Software Testing: Current Trends and Future Directions](https://arxiv.org/abs/2603.02141)

**基本信息**

- 🔗 arXiv: [`2603.02141`](https://arxiv.org/abs/2603.02141)
- 👥 作者: Tanish Singla, Qusay H. Mahmoud
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02141.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于生成式AI在软件测试中应用的综述。虽然主题并非直接针对化学信息学或质谱分析，但生成式AI（作为AI大模型的一个子类）的方法论、应用模式（如生成测试数据、用例）以及文中讨论的挑战和未来方向，对于思考如何将生成式AI或大模型技术应用于化学信息学（例如生成分子结构、模拟光谱）或质谱分析（例如生成解释性数据）等科学领域具有重要的前瞻性和参考价值，属于包含重要相关讨论的综述。

**📖 中文摘要**

本文是一篇综述性论文，探讨了生成式人工智能（Generative AI）在软件测试中的当前应用和未来方向。文章全面回顾了AI在软件测试中的现有应用，重点阐述了生成式AI在测试用例生成、验证等关键领域如何改进测试覆盖率、提高效率并降低成本。论文还讨论了提升生成式AI系统效率的方法（如提示工程和微调），并分析了AI在输入生成、预言生成、测试数据创建和测试用例优先级排序等具体任务中的应用。通过分析现状、识别机遇与挑战，本文为研究者和实践者提供了关于如何整合生成式AI以显著提升软件测试效率、效果和可靠性的见解与建议。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper investigates current software testing systems and explores how artificial intelligence, specifically Generative AI, can be integrated to enhance these systems. It begins by examining different types of AI systems and focuses on the potential of Generative AI to transform software testing processes by improving test coverage, increasing efficiency, and reducing costs. The study provides a com-prehensive overview of the current applications of AI in software testing, emphasizing its significant contributions in areas such as test case generation and validation. Through an extensive literature re-view, it highlights how Generative AI can streamline these processes, resulting in more robust and thorough testing outcomes. The paper also examines methods to improve the efficiency of Generative AI systems, such as prompt engineering and fine-tuning. Additionally, it explores the use of AI in specific tasks, including input generation, oracle generation, data generation, test data creation, and test case prioritization. By analyzing the current landscape and identifying both the opportunities and challenges in integrating Generative AI, this paper provides valuable insights and recommendations for practitioners and researchers. It underscores the need for ongoing advancements and targeted development efforts to overcome existing hurdles and fully leverage AI's capabilities. The findings further show that with continued innovation and careful implementation, Generative AI has the potential to significantly enhance the efficiency, effectiveness, and reliability of software testing, particularly in the rapidly evolving field of IoT testing.

</details>

---

### 74. [Exploring Drug Safety Through Knowledge Graphs: Protein Kinase Inhibitors as a Case Study](https://arxiv.org/abs/2603.00097)

**基本信息**

- 🔗 arXiv: [`2603.00097`](https://arxiv.org/abs/2603.00097)
- 👥 作者: David Jackson, Michael Gertz, Jürgen Hesser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00097.pdf)

**💡 相关性分析**

满足标准2：论文提出的知识图谱框架整合了化学、生物和临床数据，为构建或验证化学信息学大模型（如用于药物发现或安全性预测的模型）提供了重要的数据资源和工具基础。

**📖 中文摘要**

本文提出了一个基于知识图谱的框架，用于探索药物安全性，以蛋白激酶抑制剂为案例研究。该框架整合了异构数据源，包括药物-靶点数据（ChEMBL）、临床试验文献（PubMed）、试验元数据和上市后安全报告（FAERS），构建了一个证据加权的药物-医疗条件二分网络。该框架旨在揭示复杂模式、支持假设生成并增强药物警戒。虽然论文本身不直接研究化学大模型或质谱结构推理，但它提供了一个整合化学、生物和临床数据的知识图谱框架。这种框架和生成的数据资源（如网络和关联）可以被视为构建或验证化学信息学大模型（例如用于预测药物-靶点相互作用或不良反应）的重要数据基础设施和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adverse Drug Reactions (ADRs) are a leading cause of morbidity and mortality. Existing prediction methods rely mainly on chemical similarity, machine learning on structured databases, or isolated target profiles, but often fail to integrate heterogeneous, partly unstructured evidence effectively. We present a knowledge graph-based framework that unifies diverse sources, drug-target data (ChEMBL), clinical trial literature (PubMed), trial metadata ( this http URL ), and post-marketing safety reports (FAERS) into a single evidence-weighted bipartite network of drugs and medical conditions. Applied to 400 protein kinase inhibitors, the resulting network enables contextual comparison of efficacy (HR, PFS, OS), phenotypic and target similarity, and ADR prediction via target-to-adverse-event correlations. A non-small cell lung cancer case study correctly highlights established and candidate drugs, target communities (ERbB, ALK, VEGF), and tolerability differences. Designed as an orthogonal, extensible analysis and search tool rather than a replacement for current models, the framework excels at revealing complex patterns, supporting hypothesis generation, and enhancing pharmacovigilance. Code and data are publicly available at this https URL .

</details>

---

### 75. [Alpha-RF: Automated RF-Filter-Circuit Design with Neural Simulator and Reinforcement Learning](https://arxiv.org/abs/2603.00104)

**基本信息**

- 🔗 arXiv: [`2603.00104`](https://arxiv.org/abs/2603.00104)
- 👥 作者: Nhat Tran, Chenjie Hao, Alexander Stameroff 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00104.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用神经模拟器（一种特定的大模型）和强化学习进行自动化设计。这种方法论与“化学大模型”主题中利用AI模型加速科学计算和发现的过程直接相关。

**📖 中文摘要**

本文提出了一种使用神经模拟器和强化学习的自动射频（RF）滤波器电路设计工具。该方法首先训练一个神经模拟器来替代计算昂贵的电磁PDE模拟器，将仿真时间从数分钟大幅缩短至毫秒级。然后，利用深度强化学习算法训练一个策略，在神经模拟器构建的想象空间中进行自动设计。该工作展示了神经模拟器和强化学习在RF电路设计中的应用，并指出该方法可推广到其他设计领域。虽然应用领域是电路设计，但其核心方法——使用神经网络作为物理模拟器的快速替代品（即“神经模拟器”），并利用强化学习进行优化——与“化学大模型”中利用AI模型加速计算或指导设计的理念高度相关。例如，在化学信息学中，类似的方法可用于加速分子动力学模拟或指导分子设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate, high-performance radio-frequency (RF) filter circuits are ubiquitous in radio-frequency communication and sensing systems for accepting and rejecting signals at desired frequencies. Conventional RF filter design process involves manual calculations of design parameters, followed by intuition-guided iterations to achieve the desired response for a set of filter specifications. This process is time-consuming due to time- and resource-intensive electromagnetic simulations using full-wave numerical PDE solvers. This process is also highly sensitive to domain expertise and requires many years of professional training. To address these bottlenecks, we propose an automatic RF filter circuit design tool using neural simulator and reinforcement learning. First, we train a neural simulator to replace the PDE electromagnetic simulator. The neural-network-based simulator reduces each of the simulation time from 4 minutes on average to less than 100 millisecond while maintaining a high precision. Such dramatic acceleration enable us to leverage deep reinforcement learning algorithm and train an amortized inference policy to perform automatic design in the imagined space from the neural simulator. The resulted automatic circuit-design agent achieves super-human design results. The automatic circuit-design agent also reduces the on-average design cycle from days to under a few seconds. Even more surprisingly, we demonstrate that the neural simulator can generalize to design spaces far from the training dataset and in a sense it has learned the underlying physics--Maxwell equations. We also demonstrate that the reinforcement learning has discovered many expert-like design intuitions. This work marks a step in using neural simulators and reinforcement learning in RF circuit design and the proposed method is generally applicable to many other design problems and domains in close affinity

</details>

---

### 76. [A Multi-Scenario UAV RF Dataset with Real-World Acquisition and Signal Processing Benchmarking](https://arxiv.org/abs/2603.00106)

**基本信息**

- 🔗 arXiv: [`2603.00106`](https://arxiv.org/abs/2603.00106)
- 👥 作者: Haolin Zheng, Ning Gao, Zhenghang Zhu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00106.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个高质量、多场景的射频信号数据集。这种时序物理信号数据集及其相关的分析任务（如指纹识别），为开发和处理类似复杂信号（如质谱）的推理模型提供了有价值的数据资源和参考基准。

**📖 中文摘要**

本文介绍了一个真实世界的多场景无人机（UAV）射频（RF）数据集DRFF-R2。该数据集使用专用采集平台在多样化的操作条件下收集，包含来自8种不同型号的26个无人机单元的RF记录，涵盖了不同的飞行状态、高度、速度、采集日期和接收器配置。数据集被系统地组织成七个子集，以促进结构化实验。该数据集为未来的UAV RF信号研究提供了全面的资源，包括RF指纹识别、模型级识别、飞行状态分析和干扰感知信号处理。虽然应用领域是无人机通信，但论文提供的是一个高质量的、标注清晰的RF信号数据集。这种时序的、包含复杂物理过程（电磁波传播与散射）的信号数据集，其构建理念、处理方法和分析任务（如指纹识别）与“质谱结构推理”中处理复杂的质谱信号以推断分子结构具有方法论上的相似性。该数据集可作为测试和开发信号处理、模式识别及推理模型的基准资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a real-world multi-scenario unmanned aerial vehicle (UAV) radio frequency (RF) dataset, namely DRFF-R2, which is collected using a dedicated acquisition platform under diverse operational conditions. All signals are acquired within a unified framework to ensure consistency in hardware configuration and environmental settings. The dataset is systematically organized into seven well-defined subsets corresponding to different operational and signal composition scenarios to facilitate structured experimentation. Each file follows a clearly annotated naming convention to enable convenient data indexing and reproducible analysis. The dataset contains RF recordings from 26 UAV units spanning 8 distinct models, captured across varying flight states, altitudes, speeds, acquisition days, and receiver configurations. By covering diverse acquisition settings and signal compositions, the dataset provides a comprehensive resource for future UAV RF signal research, including RF fingerprinting (RFF) identification, model-level recognition, flight state analysis, time-varying RFF study, and interference-aware signal processing.

</details>

---

### 77. [GazeXPErT: An Expert Eye-tracking Dataset for Interpretable and Explainable AI in Oncologic FDG-PET/CT Scans](https://arxiv.org/abs/2603.00162)

**基本信息**

- 🔗 arXiv: [`2603.00162`](https://arxiv.org/abs/2603.00162)
- 👥 作者: Joy T Wu, Daniel Beckmann, Sarah Miller 等18人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00162.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个独特的多模态数据集（医学影像+专家眼动轨迹），旨在推动可解释AI的发展。这种融合领域专家行为数据以增强和解释模型的方法，为化学信息学和质谱分析中构建更可靠、可解释的推理模型提供了重要的方法论参考和数据资源范式。

**📖 中文摘要**

本文介绍了GazeXPErT，一个用于肿瘤FDG-PET/CT扫描的四维眼动追踪数据集，旨在推动可解释和可解释AI在医学影像中的应用。数据集捕获了专家在肿瘤检测和测量过程中的视觉搜索模式，包含来自346次扫描的原始眼动数据，并提取了9030条独特的注视-病灶轨迹。基线实验表明，融入专家注视模式可以提升肿瘤分割模型的性能，并且基于视觉Transformer的模型可以改善动态病灶定位和专家意图预测。该数据集被设计用于探索多种机器学习问题，包括视觉 grounding、因果推理、临床可解释特征增强、人机交互以及专家注视奖励建模等。虽然领域是医学影像，但其核心是提供“专家行为数据”（眼动轨迹）来增强和解释AI模型。这种利用专家先验知识（以行为数据形式）来指导、解释或提升模型性能的思路，与“化学大模型”和“质谱结构推理”中寻求融合领域知识、提高模型可解释性和可靠性的目标高度一致。该数据集本身也是一个重要的多模态（图像+行为）资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

[18F]FDG-PET/CT is a cornerstone imaging modality for tumor staging and treatment response assessment across many cancer types, yet expert reader shortages necessitate more efficient diagnostic aids. While standalone AI models for automatic lesion segmentation exist, clinical translation remains hindered by concerns about interpretability, explainability, reliability, and workflow integration. We present GazeXPErT, a 4D eye-tracking dataset capturing expert search patterns during tumor detection and measurement on 346 FDG-PET/CT scans. Each study was read by a trainee and a board-certified nuclear medicine or radiology specialist using an eye-tracking-enabled annotation platform that simulates routine clinical reads. From 3,948 minutes of raw 60Hz eye-tracking data, 9,030 unique gaze-to-lesion trajectories were extracted, synchronized with PET/CT image slices, and rendered in COCO-style format for multiple machine learning applications. Baseline validation experiments demonstrate that a 3D nnUNet tumor segmentation model achieved superior performance when incorporating expert gaze patterns versus without (DICE score 0.6819 versus 0.6008), and that vision transformers trained on sequential gaze and PET/CT images can improve dynamic lesion localization (74.95% predicted gaze point closer to tumor) and expert intention prediction (Accuracy 67.53% and AUROC 0.747). GazeXPErT is a valuable resource designed to explore multiple machine learning problems beyond these baseline experiments, which include and are not limited to, visual grounding or causal reasoning, clinically explainable feature augmentation, human-computer interaction, human intention prediction or understanding, and expert gaze-rewarded modeling approaches to AI in oncologic FDG-PET/CT imaging.

</details>

---

### 78. [Scaling Quantum Machine Learning without Tricks: High-Resolution and Diverse Image Generation](https://arxiv.org/abs/2603.00233)

**基本信息**

- 🔗 arXiv: [`2603.00233`](https://arxiv.org/abs/2603.00233)
- 👥 作者: Jonas Jäger, Florian J. Kiwit, Carlos A. Riofrío
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00233.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子生成模型（一种特定类型的大模型）在复杂数据集上的扩展和应用。这直接与“化学大模型”主题中探索前沿AI/机器学习模型（包括量子模型）以解决科学计算问题的方向相关。

**📖 中文摘要**

本文研究了量子生成建模，特别关注量子Wasserstein GAN在经典图像数据集（MNIST, Fashion-MNIST）上的训练。论文克服了当前量子机器学习通常局限于玩具数据集或需要降维技巧的限制，通过利用经典的图像加载到量子计算机的最新进展，实现了在完整数据集上训练量子生成器，并生成了全分辨率、跨所有类别的图像，在单端到端量子生成器上达到了新的最先进性能。论文还分析了变分电路架构的选择如何引入归纳偏置，从而解锁了这一性能。虽然应用领域是图像生成，但其核心是探索和推进“量子机器学习”模型的能力边界，特别是生成模型。量子机器学习是机器学习的一个前沿分支，可以视为“大模型”探索的一个新兴方向（即量子架构下的大模型）。论文在量子硬件上扩展模型规模和处理复杂数据集的努力，与“化学大模型”中探索新型计算架构（如量子计算）以解决化学问题的趋势相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum generative modeling is a rapidly evolving discipline at the intersection of quantum computing and machine learning. Contemporary quantum machine learning is generally limited to toy examples or heavily restricted datasets with few elements. This is not only due to the current limitations of available quantum hardware but also due to the absence of inductive biases arising from application-agnostic designs. Current quantum solutions must resort to tricks to scale down high-resolution images, such as relying heavily on dimensionality reduction or utilizing multiple quantum models for low-resolution image patches. Building on recent developments in classical image loading to quantum computers, we circumvent these limitations and train quantum Wasserstein GANs on the established classical MNIST and Fashion-MNIST datasets. Using the complete datasets, our system generates full-resolution images across all ten classes and establishes a new state-of-the-art performance with a single end-to-end quantum generator without tricks. As a proof-of-principle, we also demonstrate that our approach can be extended to color images, exemplified on the Street View House Numbers dataset. We analyze how the choice of variational circuit architecture introduces inductive biases, which crucially unlock this performance. Furthermore, enhanced noise input techniques enable highly diverse image generation while maintaining quality. Finally, we show promising results even under quantum shot noise conditions.

</details>

---

### 79. [Data-driven Synthesis of Magnetic Resonance Spectroscopy Data using a Variational Autoencoder](https://arxiv.org/abs/2603.00736)

**基本信息**

- 🔗 arXiv: [`2603.00736`](https://arxiv.org/abs/2603.00736)
- 👥 作者: Dennis M.J. van de Sande, Julian P. Merkofer, Sina Amirrajab 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00736.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心研究内容是利用生成模型（VAE）进行光谱数据合成，这与“质谱结构推理”中处理和分析复杂光谱信号的核心任务直接相关。2) 提出的框架和生成的数据集为解决质谱分析中类似的数据稀缺和增强问题提供了重要的方法工具和资源思路。

**📖 中文摘要**

本文提出了一种数据驱动的变分自编码器（VAE）框架，用于合成体内磁共振波谱（MRS）数据。该模型仅在测量的单个体素波谱数据上训练，学习复杂值波谱的低维潜在表示，并通过潜在空间采样和插值生成新样本。研究通过一系列互补分析评估了生成性能，包括重建质量、使用低维嵌入的特征级相似性、基于应用的信号质量指标以及代谢物量化一致性。结果表明，VAE能够准确重建主要光谱模式，并生成与体内数据占据相同特征空间的合成光谱。在一个针对GABA编辑波谱的示例应用中，用合成光谱增强有限的瞬态子集改善了信噪比、线宽和形状分数等信号质量指标。这项工作突出了数据驱动MRS合成的潜力和局限性。虽然领域是医学波谱，但MRS与质谱同属光谱分析技术，都涉及从复杂的光谱信号中解码化学/生物信息。论文提出的使用生成模型（VAE）合成光谱数据以解决数据稀缺问题、并用于下游任务增强的方法，与“质谱结构推理”中可能面临的数据不足和需要数据增强的挑战直接相关。其方法论对质谱数据的合成与增强具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of deep learning methods for magnetic resonance spectroscopy (MRS) is often hindered by limited availability of large, high-quality training datasets. While physics-based simulations are commonly used to mitigate this limitation, accurately modeling all in-vivo signal components remains challenging. In this work, we propose a data-driven framework for synthesizing in-vivo MRS data using a variational autoencoder (VAE) trained exclusively on measured single-voxel spectroscopy data. The model learns a low-dimensional latent representation of complex-valued spectra and enables generation of new samples through latent-space sampling and interpolation. The generative performance of the proposed approach is evaluated using a comprehensive set of complementary analyses, including reconstruction quality, feature-level similarity using low-dimensional embeddings, application-based signal quality metrics, and metabolite quantification agreement. The results demonstrate that the VAE accurately reconstructs dominant spectral patterns and generates synthetic spectra that occupy the same feature space as in-vivo data. In an example application targeting GABA-edited spectroscopy, augmenting limited subsets of transients with synthetic spectra improves signal quality metrics such as signal-to-noise ratio, linewidth, and shape scores. However, the results also reveal limitations of the generative approach, including under-representation of stochastic noise and reduced accuracy in absolute metabolite quantification, particularly for applications sensitive to concentration estimates. These findings highlight both potential and limitations of data-driven MRS synthesis. Beyond the proposed model, this study introduces a structured evaluation framework for generative MRS methods, emphasizing the importance of application-aware validation when synthetic data are used for downstream analysis.

</details>

---

### 80. [Time-Aware Latent Space Bayesian Optimization](https://arxiv.org/abs/2603.00935)

**基本信息**

- 🔗 arXiv: [`2603.00935`](https://arxiv.org/abs/2603.00935)
- 👥 作者: Tuan A. Vu, Julien Martinelli, Harri Lähdesmäki
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00935.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对分子设计任务，开发一种结合了生成模型（VAE）和贝叶斯优化的时间感知优化框架。这直接围绕“化学大模型”主题，具体应用于分子生成与优化。

**📖 中文摘要**

本文提出了时间感知潜在空间贝叶斯优化（TALBO），用于处理具有时间漂移目标的结构化域（如分子设计）优化问题。TALBO通过GP先验变分自编码器将时间信息整合到代理模型和学习的生成表示中，从而产生与演化目标对齐的潜在空间。为了系统评估时变LSBO，论文将广泛使用的分子设计任务适应于漂移的多属性目标，并引入了针对变化目标的定制指标。在多个基准测试中，TALBO consistently outperforms strong LSBO baselines。虽然论文主要关注贝叶斯优化，但其应用场景是“分子设计”，并且核心框架建立在潜在空间生成模型（VAE）之上。这直接属于“化学大模型”的应用范畴——使用生成模型和优化算法进行分子发现和设计。论文特别关注了目标随时间变化的现实场景，提升了该方法的实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Latent-space Bayesian optimization (LSBO) extends Bayesian optimization to structured domains, such as molecular design, by searching in the continuous latent space of a generative model. However, most LSBO methods assume a fixed objective, whereas real design campaigns often face temporal drift (e.g., evolving preferences or shifting targets). Bringing time-varying BO into LSBO is nontrivial: drift can affect not only the surrogate, but also the latent search space geometry induced by the representation. We propose Time-Aware Latent-space Bayesian Optimization (TALBO), which incorporates time in both the surrogate and the learned generative representation via a GP-prior variational autoencoder, yielding a latent space aligned as objectives evolve. To evaluate timevarying LSBO systematically, we adapt widely used molecular design tasks to drifting multi-property objectives and introduce metrics tailored to changing targets. Across these benchmarks, TALBO consistently outperforms strong LSBO baselines and remains robust across drift speeds and design choices, while remaining competitive under actually time-invariant objectives.

</details>

---

### 81. [Super-resolution of turbulent reacting flows on complex meshes using graph neural networks](https://arxiv.org/abs/2603.01080)

**基本信息**

- 🔗 arXiv: [`2603.01080`](https://arxiv.org/abs/2603.01080)
- 👥 作者: Priyabrat Dash, Konduri Aditya, Christos E. Frouzakis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01080.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用图神经网络（GNN）处理复杂网格数据并执行物理场超分辨率。GNN是构建化学、材料科学等领域大模型（用于分子、材料、反应预测）的核心架构。该工作展示了GNN在科学计算中的高级应用，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一种基于图神经网络（GNN）的方法，用于在复杂非结构网格上从低分辨率数据重建湍流反应流中的未解析小尺度结构。该方法利用GNN的消息传递层处理非结构化数据的能力，开发了一种从复杂网格上的低分辨率数据重建未解析小尺度结构的方法论。在两个案例上验证了准确性：结构化非均匀网格上的反应通道流，以及具有非结构化网格的反应氢燃料内燃机。评估结果表明，该方法在准确重建细尺度特征方面是有效的。这项工作为在复杂网格上集成数据驱动的小尺度重建和亚网格尺度建模提供了一条途径。虽然应用领域是计算流体力学，但其核心是使用GNN这种强大的深度学习模型来处理科学计算中的复杂网格数据并执行超分辨率任务。GNN是构建“科学大模型”的关键架构之一，用于学习物理系统的表示。论文展示的方法论——使用GNN在复杂几何上进行物理场重建——与“化学大模型”中利用GNN处理分子图、材料结构或反应网络等复杂非欧数据的精神完全一致，是跨领域的方法论借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

State-of-the-art deep learning models have been extensively utilized to reconstruct small-scale structures from coarse-grained data in turbulent flows. However, their application has predominantly been restricted to structured uniform meshes, limiting their applicability to data associated with complex geometries that are typically simulated on structured non-uniform or unstructured meshes. Machine learning (ML) models based on graph neural networks (GNNs), known for their ability to process unstructured data, offer a promising alternative. In this study, we leverage the inherent flexibility of GNNs featuring message passing layers to develop a methodology for reconstructing unresolved small-scale structures from low-resolution data on complex meshes. The accuracy of the proposed approach is demonstrated using two cases: a reacting channel flow on a structured non-uniform mesh, and a reacting hydrogen fueled internal combustion (IC) engine featuring an unstructured mesh. Evaluation of results based on visual agreement, statistical metrics, and cumulative error reduction indicates the effectiveness of the method in accurately reconstructing fine-scale features. Overall, this study provides a pathway for integrating data-driven small-scale reconstruction and subgrid-scale modeling to enhance the accuracy of coarse-grained simulations on complex meshes.

</details>

---

### 82. [Structure-preserving Randomized Neural Networks for Incompressible Magnetohydrodynamics Equations](https://arxiv.org/abs/2603.01102)

**基本信息**

- 🔗 arXiv: [`2603.01102`](https://arxiv.org/abs/2603.01102)
- 👥 作者: Yunlong Li, Fei Wang, Lingxiao Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01102.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结构保持的随机神经网络（SP-RaNN）来求解物理方程。这属于“科学机器学习”或“物理信息机器学习”的范畴，是构建用于科学计算的“大模型”的重要技术路径之一，与“化学大模型”主题中利用AI解决科学计算问题的方向高度相关。

**📖 中文摘要**

本文提出了一种用于求解不可压缩磁流体动力学（MHD）方程的结构保持随机神经网络（SP-RaNN）。该方法自动且精确地满足散度为零的条件。与依赖昂贵非线性非凸优化的深度神经网络不同，SP-RaNN将训练过程重新表述为线性最小二乘系统，从而消除了非凸优化。该方法通过Picard或Newton迭代线性化控制方程，在域内和边界上的配置点使用有限差分格式进行离散化，并通过线性最小二乘程序求解所得线性系统。SP-RaNN在统一的时空框架内保持了方程的固有数学结构。在Navier-Stokes、Maxwell和MHD方程上的数值实验表明，与传统数值方法和基于DNN的方法相比，SP-RaNN实现了更高的精度、更快的收敛速度以及散度自由约束的精确执行。虽然应用领域是物理方程求解，但其核心是提出了一种新型的“随机神经网络”框架，用于高效、准确地求解具有复杂约束的偏微分方程。这种将物理结构（如守恒律）硬编码到神经网络架构中的“物理信息神经网络”方法，是构建“科学大模型”的一个重要范式。该方法论对于化学、材料科学中需要求解具有特定约束（如对称性、守恒律）的方程问题具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The incompressible magnetohydrodynamic (MHD) equations are fundamental in many scientific and engineering applications. However, their strong nonlinearity and dual divergence-free constraints make them highly challenging for conventional numerical solvers. To overcome these difficulties, we propose a Structure-Preserving Randomized Neural Network (SP-RaNN) that automatically and exactly satisfies the divergence-free conditions. Unlike deep neural network (DNN) approaches that rely on expensive nonlinear and nonconvex optimization, SP-RaNN reformulates the training process into a linear least-squares system, thereby eliminating nonconvex optimization. The method linearizes the governing equations through Picard or Newton iterations, discretizes them at collocation points within the domain and on the boundaries using finite-difference schemes, and solves the resulting linear system via a linear least-squares procedure. By design, SP-RaNN preserves the intrinsic mathematical structure of the equations within a unified space-time framework, ensuring both stability and accuracy. Numerical experiments on the Navier-Stokes, Maxwell, and MHD equations demonstrate that SP-RaNN achieves higher accuracy, faster convergence, and exact enforcement of divergence-free constraints compared with both traditional numerical methods and DNN-based approaches. This structure-preserving framework provides an efficient and reliable tool for solving complex PDE systems while rigorously maintaining their underlying physical laws.

</details>

---

### 83. [Grokking as a Phase Transition between Competing Basins: a Singular Learning Theory Approach](https://arxiv.org/abs/2603.01192)

**基本信息**

- 🔗 arXiv: [`2603.01192`](https://arxiv.org/abs/2603.01192)
- 👥 作者: Ben Cullen, Sergio Estan-Ruiz, Riya Danait 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01192.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用奇异学习理论（SLT）分析和理解深度学习模型（作为大模型的基础）的泛化行为（顿悟）。这种对模型训练动力学和泛化原理的基础理论研究，对于构建和优化“化学大模型”具有重要的理论指导意义。

**📖 中文摘要**

本文通过奇异学习理论（SLT）的视角研究“顿悟”（grokking）现象，即训练后期从记忆到泛化的突然转变。SLT是一个贝叶斯框架，通过局部学习系数（LLC）来表征损失景观的几何形状，LLC衡量损失表面的局部退化程度。SLT将较低的LLC basin与较高的后验质量集中度和较低的预期泛化误差联系起来。利用这一理论，作者将二次网络中的顿悟解释为竞争性近零损失解basin之间的相变。贡献包括：推导了在模运算任务上训练的二次网络的LLC闭式表达式，并进行了相应的实证验证；以及实证证据表明LLC轨迹为跟踪训练期间的泛化动力学和解释相变提供了可靠的工具。虽然论文以简单的二次网络和模运算为例，但其研究的是深度学习模型（可视为一种基础“大模型”）泛化行为的基本理论。理解“顿悟”等泛化现象对于训练更高效、更可靠的化学或科学大模型至关重要。该工作提供的理论工具（SLT, LLC）和分析框架，对于分析和改进化学信息学中大模型的训练动态和泛化能力具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Grokking, the abrupt transition from memorization to generalisation after extended training, suggests the presence of competing solution basins with distinct statistical properties. We study this phenomenon through the lens of Singular Learning Theory (SLT), a Bayesian framework that characterizes the geometry of the loss landscape via the local learning coefficient (LLC), a measure of the local degeneracy of the loss surface. SLT links lower-LLC basins to higher posterior mass concentration and lower expected generalisation error. Leveraging this theory, we interpret grokking in quadratic networks as a phase transition between competing near-zero-loss solution basins. Our contributions are two-fold: we derive closed-form expressions for the LLC in quadratic networks trained on modular arithmetic tasks, with the corresponding empirical verification; as well as empirical evidence demonstrating that LLC trajectories provide a reliable tool for tracking generalisation dynamics and interpreting phase transitions during training.

</details>

---

### 84. [Probing Materials Knowledge in LLMs: From Latent Embeddings to Reliable Predictions](https://arxiv.org/abs/2603.01834)

**基本信息**

- 🔗 arXiv: [`2603.01834`](https://arxiv.org/abs/2603.01834)
- 👥 作者: Vineeth Venugopal, Soroush Mahjoubi, Elsa Olivetti
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01834.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大型语言模型在材料科学（化学相关领域）中的应用、知识编码和可靠性进行评估，与“化学大模型”主题直接相关。

**📖 中文摘要**

这篇论文评估了25个大型语言模型在材料科学四个任务上的表现，涉及超过200个基础模型和微调配置。研究发现，输出模态从根本上决定了模型行为：对于符号任务，微调能收敛到一致且可验证的答案；而对于数值任务，微调虽能提高预测准确性，但模型在不同推理运行中仍不一致，限制了其作为定量预测器的可靠性。论文还发现，对于数值回归任务，直接从中间Transformer层提取嵌入比从模型文本输出中提取能获得更好的性能，这揭示了一种“LLM头部瓶颈”现象。此外，论文对GPT模型在材料科学中的性能进行了纵向研究，观察到在18个月内性能有9-43%的波动，这对科学应用的可重复性提出了挑战。这项工作直接探讨了大型语言模型在材料科学领域的知识编码和可靠性，与“化学大模型”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models are increasingly applied to materials science, yet fundamental questions remain about their reliability and knowledge encoding. Evaluating 25 LLMs across four materials science tasks -- over 200 base and fine-tuned configurations -- we find that output modality fundamentally determines model behavior. For symbolic tasks, fine-tuning converges to consistent, verifiable answers with reduced response entropy, while for numerical tasks, fine-tuning improves prediction accuracy but models remain inconsistent across repeated inference runs, limiting their reliability as quantitative predictors. For numerical regression, we find that better performance can be obtained by extracting embeddings directly from intermediate transformer layers than from model text output, revealing an ``LLM head bottleneck,'' though this effect is property- and dataset-dependent. Finally, we present a longitudinal study of GPT model performance in materials science, tracking four models over 18 months and observing 9--43\% performance variation that poses reproducibility challenges for scientific applications.

</details>

---

### 85. [Distributional Priors Guided Diffusion for Generating 3D Molecules in Low Data Regimes](https://arxiv.org/abs/2404.00962)

**基本信息**

- 🔗 arXiv: [`2404.00962`](https://arxiv.org/abs/2404.00962)
- 👥 作者: Haokai Hong, Wanyu Lin, Ming Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2404.00962.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子生成的扩散模型框架（GODD），专门处理分布外生成和结构偏移问题，直接涉及分子（化学实体）的生成和设计，与“化学大模型”主题相关。

**📖 中文摘要**

本文提出了几何分布外扩散模型（GODD），一个新颖的扩散框架，用于在分布结构偏移下，利用数据丰富的分子分布进行训练，同时泛化到数据稀缺的分布。该模型的核心是一个指定的等变非对称自编码器，用于捕获分布结构先验。非对称设计使模型能够通过捕获代表不同分布的分布先验，泛化到未见过的结构变化。编码的结构粒度先验引导生成朝向稀疏区域，而无需在此类数据上显式训练。该框架在包含分布外结构偏移（如支架、环）的标准基准上进行了评估，GODD在基于分子有效性、独特性和新颖性定义的成功率上提高了12.6%。此外，该框架在规范的基于片段的药物设计任务上表现出有前景的性能和泛化能力，突出了其在基于学习的分子发现中的实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Can we train a 3D molecule generator using data from dense regions to generate samples in sparse regions? This challenge can be framed as an out-of-distribution (OOD) generation problem. While prior research on OOD generation predominantly targets property shifts, structural shifts -- such as differences in molecular scaffolds or functional groups -- represent an equally critical source of distributional shifts. This work introduces the Geometric OOD Diffusion Model (GODD), a novel diffusion-based framework that enables training on data-abundant molecular distributions while generalizing to data-scarce distributions under distributional structural shifts. Central to our approach is a designated equivariant asymmetric autoencoder to capture distributional structural priors. The asymmetric design allows the model to generalize to unseen structural variations by capturing distributional priors representing distinct distributions. The encoded structural-grained priors guide generation toward sparse regions without requiring explicit training on such data. Evaluated across standard benchmarks encompassing OOD structural shifts (e.g., scaffolds, rings), GODD achieves an improvement of 12.6% in success rate, defined based on molecular validity, uniqueness, and novelty. Furthermore, the framework demonstrates promising performance and generalization on canonical fragment-based drug design tasks, highlighting its utility in learning-based molecular discovery.

</details>

---

### 86. [Generative Enzyme Design Guided by Functionally Important Sites and Small-Molecule Substrates](https://arxiv.org/abs/2405.08205)

**基本信息**

- 🔗 arXiv: [`2405.08205`](https://arxiv.org/abs/2405.08205)
- 👥 作者: Zhenqiao Song, Yunlong Zhao, Wenxian Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个生成模型（EnzyGen）用于酶（一种生物大分子）的设计，涉及氨基酸序列和三维结构的生成，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了EnzyGen，一种学习统一模型以跨所有功能家族设计酶的方法。核心思想是基于与所需催化功能对应的功能重要位点和底物，生成酶的氨基酸序列及其三维坐标。这些位点是从酶数据库中自动挖掘的。EnzyGen由一个新颖的注意力和邻域等变层交错网络组成，该网络捕获整个蛋白质序列中的长程相关性以及三维空间中最近氨基酸的局部影响。为了学习生成模型，我们设计了一个联合训练目标，包括序列生成损失、位置预测损失和酶-底物相互作用损失。我们进一步构建了EnzyBench，一个包含3157个酶家族的数据集，涵盖了蛋白质数据库（PDB）中所有可用的酶。实验结果表明，我们的EnzyGen在所有323个测试家族中始终取得最佳性能，在底物结合亲和力方面超过最佳基线10.79%。这些发现证明了EnzyGen在设计折叠良好且能高效结合特定底物的酶方面的卓越能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enzymes are genetically encoded biocatalysts capable of accelerating chemical reactions. How can we automatically design functional enzymes? In this paper, we propose EnzyGen, an approach to learn a unified model to design enzymes across all functional families. Our key idea is to generate an enzyme's amino acid sequence and their three-dimensional (3D) coordinates based on functionally important sites and substrates corresponding to a desired catalytic function. These sites are automatically mined from enzyme databases. EnzyGen consists of a novel interleaving network of attention and neighborhood equivariant layers, which captures both long-range correlation in an entire protein sequence and local influence from nearest amino acids in 3D space. To learn the generative model, we devise a joint training objective, including a sequence generation loss, a position prediction loss and an enzyme-substrate interaction loss. We further construct EnzyBench, a dataset with 3157 enzyme families, covering all available enzymes within the protein data bank (PDB). Experimental results show that our EnzyGen consistently achieves the best performance across all 323 testing families, surpassing the best baseline by 10.79% in terms of substrate binding affinity. These findings demonstrate EnzyGen's superior capability in designing well-folded and effective enzymes binding to specific substrates with high affinities.

</details>

---

### 87. [One protein is all you need](https://arxiv.org/abs/2411.02109)

**基本信息**

- 🔗 arXiv: [`2411.02109`](https://arxiv.org/abs/2411.02109)
- 👥 作者: Anton Bushuiev, Roman Bushuiev, Olga Pimenova 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.02109.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对单个目标蛋白质定制蛋白质语言模型，以改善结构预测、适应性预测和功能预测，直接涉及蛋白质（化学/生物大分子）的建模，与“化学大模型”主题相关。

**📖 中文摘要**

本文提出了一种方法，使蛋白质语言模型能够针对单个目标蛋白质进行自监督定制，无需额外数据。该方法被称为蛋白质测试时训练（ProteinTTT），它持续增强了不同模型、大小和数据集上的泛化能力。ProteinTTT改善了具有挑战性目标的结构预测，在蛋白质适应性预测上取得了新的最先进结果，并增强了两个任务上的功能预测。通过两个具有挑战性的案例研究，我们还表明，通过ProteinTTT进行的定制实现了更准确的抗体-抗原环建模，并改善了大型神奇病毒数据库中19%的结构，在通用AlphaFold2和ESMFold难以处理的情况下提供了改进的预测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generalization beyond training data remains a central challenge in machine learning for biology. A common way to enhance generalization is self-supervised pre-training on large datasets. However, aiming to perform well on all possible proteins can limit a model's capacity to excel on any specific one, whereas experimentalists typically need accurate predictions for individual proteins they study, often not covered in training data. To address this limitation, we propose a method that enables self-supervised customization of protein language models to one target protein at a time, on the fly, and without assuming any additional data. We show that our Protein Test-Time Training (ProteinTTT) method consistently enhances generalization across different models, their sizes, and datasets. ProteinTTT improves structure prediction for challenging targets, achieves new state-of-the-art results on protein fitness prediction, and enhances function prediction on two tasks. Through two challenging case studies, we also show that customization via ProteinTTT achieves more accurate antibody-antigen loop modeling and enhances 19% of structures in the Big Fantastic Virus Database, delivering improved predictions where general-purpose AlphaFold2 and ESMFold struggle.

</details>

---

### 88. [MoMa: A Modular Deep Learning Framework for Material Property Prediction](https://arxiv.org/abs/2502.15483)

**基本信息**

- 🔗 arXiv: [`2502.15483`](https://arxiv.org/abs/2502.15483)
- 👥 作者: Botian Wang, Yawen Ouyang, Yaohui Li 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.15483.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕化学信息学领域的深度学习模型（化学大模型）进行，旨在通过模块化框架预测材料属性，推动材料发现。

**📖 中文摘要**

本文介绍了MoMa，一个用于材料属性预测的模块化深度学习框架。该框架旨在克服材料任务固有的多样性和差异性挑战。MoMa首先在广泛的任务上训练专门的模块，然后针对每个下游场景自适应地组合协同模块。在17个数据集上的评估表明，MoMa相对于最强基线平均提升了14%。少样本和持续学习实验进一步凸显了MoMa在实际应用中的潜力。MoMa开创了模块化材料学习的新范式，并将开源以促进更广泛的社区合作。这项工作直接涉及化学信息学领域，通过深度学习模型预测材料性质，是化学大模型在材料科学中的具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning methods for material property prediction have been widely explored to advance materials discovery. However, the prevailing pre-train then fine-tune paradigm often fails to address the inherent diversity and disparity of material tasks. To overcome these challenges, we introduce MoMa, a Modular framework for Materials that first trains specialized modules across a wide range of tasks and then adaptively composes synergistic modules tailored to each downstream scenario. Evaluation across 17 datasets demonstrates the superiority of MoMa, with a substantial 14% average improvement over the strongest baseline. Few-shot and continual learning experiments further highlight MoMa's potential for real-world applications. Pioneering a new paradigm of modular material learning, MoMa will be open-sourced to foster broader community collaboration.

</details>

---

### 89. [Large Language Models in Bioinformatics: A Survey](https://arxiv.org/abs/2503.04490)

**基本信息**

- 🔗 arXiv: [`2503.04490`](https://arxiv.org/abs/2503.04490)
- 👥 作者: Zhenyu Wang, Zikang Wang, Jiyue Jiang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.04490.pdf)

**💡 相关性分析**

满足标准3：论文是关于大型语言模型在科学领域（生物信息学）应用的综述，其中关于模型能力、数据处理和跨领域整合的讨论，对理解和构建化学大模型具有重要的相关性和前瞻性指导意义。

**📖 中文摘要**

本综述论文系统回顾了大型语言模型（LLMs）在生物信息学中的最新进展，重点关注基因组序列建模、RNA结构预测、蛋白质功能推断和单细胞转录组学。论文讨论了数据稀缺、计算复杂性和跨组学整合等关键挑战，并探讨了多模态学习、混合AI模型和临床应用等未来方向。通过提供全面的视角，本文强调了LLMs在推动生物信息学和精准医学创新方面的变革潜力。虽然主要关注生物信息学，但LLMs作为基础模型，其方法论、挑战和未来方向与构建和应用化学领域的大模型（化学大模型）高度相关，提供了跨领域的见解和参考框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are revolutionizing bioinformatics, enabling advanced analysis of DNA, RNA, proteins, and single-cell data. This survey provides a systematic review of recent advancements, focusing on genomic sequence modeling, RNA structure prediction, protein function inference, and single-cell transcriptomics. Meanwhile, we also discuss several key challenges, including data scarcity, computational complexity, and cross-omics integration, and explore future directions such as multimodal learning, hybrid AI models, and clinical applications. By offering a comprehensive perspective, this paper underscores the transformative potential of LLMs in driving innovations in bioinformatics and precision medicine.

</details>

---

### 90. [mCLM: A Modular Chemical Language Model that Generates Functional and Makeable Molecules](https://arxiv.org/abs/2505.12565)

**基本信息**

- 🔗 arXiv: [`2505.12565`](https://arxiv.org/abs/2505.12565)
- 👥 作者: Carl Edwards, Chi Han, Gawon Lee 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12565.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学大模型（mCLM）展开，专注于生成功能性和可合成的分子结构，这与“化学大模型”和“质谱结构推理”（涉及分子结构生成与推断）主题高度相关。

**📖 中文摘要**

本文提出了mCLM，一个模块化化学语言模型，旨在生成具有所需功能（如类药性）且可合成的分子。与基于原子表示分子的现有模型不同，mCLM在功能性构建块（即具有独特功能并可作为现实世界自动化实验室合成有效构建块的分子部分）的层面上对分子进行标记化。mCLM包含一个双语语言模型，能够理解功能的自然语言描述和分子模块。该模型前置了可合成性考虑，同时以原理性的方式改进分子的预测功能。在FDA批准药物上的实验表明，mCLM能够显著改善化学功能，并在合成可及性方面优于包括GPT-5在内的其他领先生成AI方法。mCLM还能够对多种功能进行推理，并迭代自我改进以拯救在临床试验后期失败的候选药物。这项工作直接针对化学大模型和分子结构生成（与质谱结构推理相关）的核心主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their ability to understand chemical knowledge, large language models (LLMs) remain limited in their capacity to propose novel molecules with desired functions (e.g., drug-like properties). In addition, the molecules that LLMs propose can often be challenging to make, and are almost never compatible with automated synthesis approaches. To better enable the discovery of functional small molecules, LLMs need to learn a new molecular language that is more effective in predicting properties and inherently synced with automated synthesis technology. Current molecule LLMs are limited by representing molecules based on atoms. In this paper, we argue that just like tokenizing texts into meaning-bearing (sub-)word tokens instead of characters, molecules should be tokenized at the level of functional building blocks, i.e., parts of molecules that bring unique functions and serve as effective building blocks for real-world automated laboratory synthesis. This motivates us to propose mCLM, a modular Chemical-Language Model that comprises a bilingual language model that understands both natural language descriptions of functions and molecular blocks. mCLM front-loads synthesizability considerations while improving the predicted functions of molecules in a principled manner. Experiments on FDA-approved drugs showed that mCLM is capable of significantly improving chemical functions. mCLM, with only 3B parameters, also achieves improvements in synthetic accessibility relative to 7 other leading generative AI methods including GPT-5. When tested on 122 out-of-distribution medicines using only building blocks/tokens that are compatible with automated modular synthesis, mCLM outperforms all baselines in property scores and synthetic accessibility. mCLM can also reason on multiple functions and iteratively self-improve to rescue drug candidates that failed late in clinical trials ("fallen angels").

</details>

---

### 91. [RECON: Robust symmetry discovery via Explicit Canonical Orientation Normalization](https://arxiv.org/abs/2505.13289)

**基本信息**

- 🔗 arXiv: [`2505.13289`](https://arxiv.org/abs/2505.13289)
- 👥 作者: Alonso Urbano, David W. Romero, Max Zimmer 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13289.pdf)

**💡 相关性分析**

满足标准2：论文提出的对称性发现和规范化方法在分子集合上进行了验证，其产生的数据对齐的规范表示可能作为化学大模型或质谱结构推理任务中处理分子几何和对称性的有用工具或数据预处理步骤。

**📖 中文摘要**

论文提出了RECON方法，用于在未知、实例特定对称性的数据中发现鲁棒的对称性。该方法通过显式规范方向归一化，将输入分解为不变特征和相对于训练依赖的任意规范表示的姿态。RECON通过简单的右平移校正任意规范，产生自然的、数据对齐的规范化。该方法在图像和分子集合上进行了验证，展示了准确的对称性发现。虽然论文主要关注对称性发现的通用方法，但其在分子集合上的验证表明，该方法可用于处理化学结构数据，其产生的规范化表示可能有助于化学大模型中对分子对称性和几何结构的建模，或为质谱结构推理中处理分子构象提供工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real world data often exhibits unknown, instance-specific symmetries that rarely exactly match a transformation group $G$ fixed a priori. Class-pose decompositions aim to create disentangled representations by factoring inputs into invariant features and a pose $g\in G$ defined relative to a training-dependent, arbitrary canonical representation. We introduce RECON, a class-pose agnostic canonical orientation normalization that corrects arbitrary canonicals via a simple right translation, yielding natural, data-aligned canonicalizations. This enables (i) unsupervised discovery of instance-specific pose distributions, (ii) detection of out-of-distribution poses and (iii) a plug-and-play test-time canonicalization layer. This layer can be attached on top of any pre-trained model to infuse group invariance, improving its performance without retraining. We validate on images and molecular ensembles, demonstrating accurate symmetry discovery, and matching or outperforming other canonicalizations in downstream classification.

</details>

---

### 92. [Rapid training of Hamiltonian graph networks using random features](https://arxiv.org/abs/2506.06558)

**基本信息**

- 🔗 arXiv: [`2506.06558`](https://arxiv.org/abs/2506.06558)
- 👥 作者: Atamert Rahma, Chinmay Datar, Ana Cukarska 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06558.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容围绕用于分子动力学等物理系统的图神经网络模型，这直接与化学信息学中分子模拟和建模相关。同时，其提出的快速训练框架和模型本身可作为处理分子结构动力学数据的工具或方法，服务于化学大模型或质谱结构推理所需的数据生成或特征学习。

**📖 中文摘要**

论文提出了一种使用随机特征快速训练哈密顿图网络（HGN）的方法，用于学习尊重物理对称性和约束的动力学系统。该方法将物理定律与图神经网络结合，以对复杂的N体动力学进行建模，并产生准确且置换不变的模型。与15种不同的优化器相比，该方法通过用基于随机特征的参数构建替换迭代优化，实现了150-600倍的训练加速，同时保持了相当的准确性。研究在包括N体质量弹簧和分子动力学系统在内的多种模拟中展示了鲁棒的性能，同时保留了关于置换、旋转和平移的基本物理不变性。该方法在NeurIPS 2022数据集和基准测试上进行了基准测试。即使是在最小的8节点系统上训练，模型也能以零样本方式泛化到多达4096节点的系统而无需重新训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning dynamical systems that respect physical symmetries and constraints remains a fundamental challenge in data-driven modeling. Integrating physical laws with graph neural networks facilitates principled modeling of complex N-body dynamics and yields accurate and permutation-invariant models. However, training graph neural networks with iterative, gradient-descent-based optimization algorithms (e.g., Adam, RMSProp, LBFGS) often leads to slow training, especially for large, complex systems. In comparison to 15 different optimizers, we demonstrate that Hamiltonian Graph Networks (HGN) can be trained 150-600x faster - but with comparable accuracy - by replacing iterative optimization with random feature-based parameter construction. We show robust performance in diverse simulations, including N-body mass-spring and molecular dynamics systems in up to dimensions and 10,000 particles with different geometries, while retaining essential physical invariances with respect to permutation, rotation, and translation. Our proposed approach is benchmarked using a NeurIPS 2022 Datasets and Benchmarks Track publication to further demonstrate its versatility. We reveal that even when trained on minimal 8-node systems, the model can generalize in a zero-shot manner to systems as large as 4096 nodes without retraining. Our work challenges the dominance of iterative gradient-descent-based optimization algorithms for training neural network models for physical systems.

</details>

---

### 93. [InstructPro: Natural Language Guided Ligand-Binding Protein Design](https://arxiv.org/abs/2506.09332)

**基本信息**

- 🔗 arXiv: [`2506.09332`](https://arxiv.org/abs/2506.09332)
- 👥 作者: Zhenqiao Song, Ramith Hettiarachchi, Chuan Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.09332.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容直接围绕使用自然语言指导的生成模型进行蛋白质设计，特别是配体结合蛋白质的设计，这属于化学信息学和计算化学的核心主题。同时，论文提出了InstructPro模型框架并发布了大规模数据集InstructProBench，这为化学大模型（特别是蛋白质生成模型）和基于结构的推理任务提供了重要的数据资源和工具。

**📖 中文摘要**

论文介绍了InstructPro，一个通过自然语言指令和配体公式指导设计蛋白质的生成模型家族。该模型旨在规避蛋白质-配体复合物数据稀缺的瓶颈，利用丰富的描述蛋白质-配体相互作用的自然语言。为了训练和评估，研究开发了InstructProBench，一个包含960万（功能描述，配体，蛋白质）三元组的大规模数据集。训练了两个模型变体——InstructPro-1B和InstructPro-3B，它们在多个指标上显著优于强基线。模型在已知配体上实现了高AlphaFold3 ipTM和结合亲和力，并在零样本设置中保持了稳健的性能。此外，模型产生了优异的结合自由能和分子间氢键数量，验证了其设计高亲和力配体结合蛋白质的能力。缩放至InstructPro-3B进一步改善了零样本性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The de novo design of ligand-binding proteins with tailored functions is essential for advancing biotechnology and molecular medicine, yet existing AI approaches are limited by scarce protein-ligand complex data. To circumvent this data bottleneck, we leverage the abundant natural language descriptions characterizing protein-ligand interactions. Here, we introduce InstructPro, a family of generative models that design proteins following the guidance of natural language instructions and ligand formulas. InstructPro produces protein sequences consistent with specified function descriptions and ligand targets. To enable training and evaluation, we develop InstructProBench, a large-scale dataset of 9.6 million (function description, ligand, protein) triples. We train two model variants -- InstructPro-1B and InstructPro-3B -- that substantially outperform strong baselines. InstructPro-1B achieves an AlphaFold3 ipTM of 0.918 and a binding affinity of -8.764 on seen ligands, while maintaining robust performance in a zero-shot setting with scores of 0.869 and -6.713, respectively. These results are accompanied by novelty scores of 70.1% and 68.8%, underscoring the model's ability to generalize beyond the training set. Furthermore, the model yields a superior binding free energy of -20.9 kcal/mol and an average of 5.82 intermolecular hydrogen bonds, validating its proficiency in designing high-affinity ligand-binding proteins. Notably, scaling to InstructPro-3B further improves the zero-shot ipTM to 0.882, binding affinity to -6.797, and binding free energy to -25.8 kcal/mol, demonstrating clear performance gains associated with increased model capacity. These findings highlight the power of natural language-guided generative models to mitigate the data bottlenecks in traditional structure-based methods, significantly broadening the scope of de novo protein design.

</details>

---

### 94. [A High-Quality Dataset and Reliable Evaluation for Interleaved Image-Text Generation](https://arxiv.org/abs/2506.09427)

**基本信息**

- 🔗 arXiv: [`2506.09427`](https://arxiv.org/abs/2506.09427)
- 👥 作者: Yukang Feng, Jianwen Sun, Chuanhao Li 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.09427.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模、高质量的交错图像-文本生成数据集InterSyn和相应的评估框架SynJudge。虽然主要针对视觉-语言模型，但其构建高质量、指令丰富多模态数据的方法论和资源，对于构建和评估化学领域（如分子结构图像与文本描述）的多模态大模型具有重要的参考价值和潜在适用性，可作为相关主题的数据资源。

**📖 中文摘要**

论文关注交错图像-文本生成任务，指出当前大型多模态模型（LMMs）在此任务上的不足主要源于训练数据在规模、质量和指令丰富性方面的限制。为此，论文引入了InterSyn数据集，该数据集具有大规模（180万多模态样本）、高质量（通过提出的SEIR方法进行自动化质量精炼）和丰富的指令多样性（基于人类偏好和涵盖3500个主题层次结构的多样化问题模板）的特点。这些特性使得InterSyn特别适合训练LMMs的交互式图像-文本生成能力。为了评估这些能力，论文提出了SynJudge，一个可靠的自评估器，输出四个可解释的分数。实验结果表明，即使在较小的数据子集（如25K-50K样本）上训练也能带来实质性改进，而扩展到100K/200K能带来进一步增益，突出了InterSyn的可扩展性和效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in Large Multimodal Models (LMMs) have significantly improved multimodal understanding and generation. However, these models still struggle to generate tightly interleaved image-text outputs, primarily due to the limited scale, quality, and instructional richness of current training datasets. To address this, we introduce InterSyn, a dataset that features: (1) large scale, comprising 1.8M multimodal samples; (2) high quality, supported by our proposed Self-Evaluation with Iterative Refinement (SEIR) method for rigorous automated quality refinement; (3) rich instructional diversity, ensured through diverse well-designed question templates, based on human preferences and covering a 3500-topic hierarchy. These characteristics make InterSyn particularly well-suited for training LMMs in interactive image-text generation capabilities. To evaluate the capabilities, we propose SynJudge, a reliable automatic evaluator that aligns closely with human judge and outputs four interpretable scores: Text Content Completeness (TCC), Image Content Completeness (ICC), Image Quality (IQ), and Image-Text Synergy (ITS). These scores are complementary, covering both content and quality as well as cross-modal interaction, thereby forming a comprehensive evaluation framework. Experimental results on InterSyn subsets of up to 200K samples show that 25K-50K already yield substantial improvements, while scaling to 100K/200K brings further gains in TCC, ICC, and especially ITS, highlighting InterSyn's: (1) scalability, as performance consistently improves with more data; (2) efficiency, as significant gains are achievable even with smaller subsets, making it accessible to researchers with varying computational resources.

</details>

---

### 95. [Safeguarding Multimodal Knowledge Copyright in the RAG-as-a-Service Environment](https://arxiv.org/abs/2506.10030)

**基本信息**

- 🔗 arXiv: [`2506.10030`](https://arxiv.org/abs/2506.10030)
- 👥 作者: Tianyu Chen, Jian Lou, Wenjie Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.10030.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于保护多模态RAG系统中图像知识版权的水印框架AQUA。虽然不直接针对化学领域，但其保护多模态数据（可能包括分子结构图像、光谱图等）版权的方法和技术，对于构建安全、可信的化学信息学数据共享平台或工具具有潜在的应用价值，属于数据资源保护相关的工具。

**📖 中文摘要**

论文关注在检索增强生成（RAG）演变为服务化平台（Rag-as-a-Service）并共享知识库的背景下，保护贡献数据的版权问题。现有RAG中的水印方法仅关注文本知识，而图像知识未受保护。为此，论文提出了AQUA，这是首个用于多模态RAG系统中图像知识保护的水印框架。AQUA使用两种互补的方法将语义信号嵌入合成图像中：基于首字母缩写的触发器和空间关系线索。这些技术确保水印信号在从图像检索器到文本生成器的间接水印传播中存活下来，具有高效、有效和不可感知的特点。在不同模型和数据集上的实验表明，AQUA能够实现鲁棒、隐蔽和可靠的版权追踪。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As Retrieval-Augmented Generation (RAG) evolves into service-oriented platforms (Rag-as-a-Service) with shared knowledge bases, protecting the copyright of contributed data becomes essential. Existing watermarking methods in RAG focus solely on textual knowledge, leaving image knowledge unprotected. In this work, we propose AQUA, the first watermark framework for image knowledge protection in Multimodal RAG systems. AQUA embeds semantic signals into synthetic images using two complementary methods: acronym-based triggers and spatial relationship cues. These techniques ensure watermark signals survive indirect watermark propagation from image retriever to textual generator, being efficient, effective and imperceptible. Experiments across diverse models and datasets show that AQUA enables robust, stealthy, and reliable copyright tracing, filling a key gap in multimodal RAG protection.

</details>

---

### 96. [Behavioral Generative Agents for Energy Operations](https://arxiv.org/abs/2506.12664)

**基本信息**

- 🔗 arXiv: [`2506.12664`](https://arxiv.org/abs/2506.12664)
- 👥 作者: Cong Chen, Omer Karaduman, Xu Kuang
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.12664.pdf)

**💡 相关性分析**

满足标准2：论文提出了利用大型语言模型驱动的生成式智能体来模拟和发现消费者行为的方法论和框架。虽然应用领域是能源运营，但其核心方法——使用LLM智能体进行行为建模和决策模拟——可以迁移到化学信息学领域，例如用于模拟化学实验决策、分子设计过程的探索，或为化学大模型提供交互式、基于反馈的训练环境，属于一种潜在的工具或方法资源。

**📖 中文摘要**

论文研究了生成式智能体（由大型语言模型驱动的人工智能体）在能源运营中模拟客户行为的应用。论文引入了一种新颖方法，利用生成式智能体来模拟动态电价和停电风险下客户的连续决策。研究发现，这些智能体在简单的市场场景中行为更接近最优和理性，而在任务复杂性增加时，其表现变得更多样化和次优。智能体表现出异质的客户偏好，在操作决策和文本推理中始终保持独特的、角色驱动的推理模式。在停电等低频高影响事件中，智能体优先考虑能源可靠性而非成本或利润。论文表明，行为生成式智能体可以作为研究能源运营中消费者行为的可扩展和灵活工具。

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

满足标准2：论文提出了一个用于临床决策制定的语言智能体框架LA-CDM，其核心是假设驱动、多步推理和基于反馈（测试结果）的迭代优化。这种框架与“质谱结构推理”中通过多轮质谱数据分析和假设验证来确定分子结构的逻辑高度相似。因此，该论文提出的智能体架构、训练方法（特别是混合强化学习）和推理范式，可以作为构建用于质谱数据解析和结构推断的AI代理的有价值参考模型或工具框架。

**📖 中文摘要**

论文提出LA-CDM，一个用于诊断的假设驱动、不确定性感知的语言智能体，通过反复请求和解释相关测试来收敛到诊断。该模型采用结合监督学习和强化学习的混合训练范式，针对临床决策制定的三个关键方面进行训练：准确的假设生成、假设不确定性估计和高效决策制定。研究方法在MIMIC-CDM真实世界数据集上进行了评估，该数据集涵盖四种腹部疾病，包含各种临床测试。结果表明，明确训练临床决策制定有助于提高诊断性能和效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Clinical decision-making is a dynamic, interactive, and cyclic process where doctors have to repeatedly decide on which clinical action to perform and consider newly uncovered information for diagnosis and treatment. Large Language Models (LLMs) have the potential to support clinicians in this process, however, most applications of LLMs in clinical decision support suffer from one of two limitations: Either they assume the unrealistic scenario of immediate availability of all patient information and do not model the interactive and iterative investigation process, or they restrict themselves to the limited "out-of-the-box" capabilities of large pre-trained models without performing task-specific training. In contrast to this, we propose to model clinical decision-making for diagnosis with a hypothesis-driven uncertainty-aware language agent, LA-CDM, that converges towards a diagnosis via repeatedly requesting and interpreting relevant tests. Using a hybrid training paradigm combining supervised and reinforcement learning, we train LA-CDM with three objectives targeting critical aspects of clinical decision-making: accurate hypothesis generation, hypothesis uncertainty estimation, and efficient decision-making. We evaluate our methodology on MIMIC-CDM, a real-world dataset covering four abdominal diseases containing various clinical tests and show the benefit of explicitly training clinical decision-making for increasing diagnostic performance and efficiency.

</details>

---

### 98. [SPARE: Single-Pass Annotation with Reference-Guided Evaluation for Automatic Process Supervision and Reward Modelling](https://arxiv.org/abs/2506.15498)

**基本信息**

- 🔗 arXiv: [`2506.15498`](https://arxiv.org/abs/2506.15498)
- 👥 作者: Md Imbesat Hassan Rizvi, Xiaodan Zhu, Iryna Gurevych
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.15498.pdf)

**💡 相关性分析**

满足标准2：论文提出了SPARE框架，用于自动化生成高质量的过程监督数据（即推理步骤的标注）。这种自动化标注工具对于训练和评估化学大模型（尤其是需要多步推理的分子性质预测、逆合成规划）和质谱结构推理模型（需要逐步解析碎片信息）至关重要。它提供了一种可扩展的方法来创建训练数据，直接服务于相关主题的研究。

**📖 中文摘要**

论文针对大型语言模型（LLMs）在复杂多步推理中的过程监督问题，提出了SPARE框架，用于高效、高质量的自动化过程标注。SPARE通过单次生成，将解决方案步骤与参考解决方案对齐，并确定其准确性。论文在数学推理（GSM8K, MATH）、多跳问答（MuSiQue-Ans）和空间推理（SpaRP）四个不同数据集上展示了SPARE的有效性，并在两个应用中显示出一致改进：1）训练过程奖励模型（PRMs）用于排序和聚合多个生成结果；2）通过离线强化学习微调模型以进行贪婪解码。在ProcessBench上，SPARE展示了数据高效的分布外泛化能力，仅使用约16%的训练样本即可达到与人工标注和其他合成训练基线相当的性能。此外，它在总令牌数方面实现了2.3倍的加速。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Process or step-wise supervision has played a crucial role in advancing complex multi-step reasoning capabilities of Large Language Models (LLMs). However, efficient, high-quality automated process annotation remains a significant challenge. To address this, we introduce Single-Pass Annotation with Reference-Guided Evaluation (SPARE), a novel structured framework that enables efficient per-step annotation by jointly aligning solution steps to reference solutions and determine its accuracy with explicit reasoning in single generation. We demonstrate SPARE's effectiveness across four diverse datasets spanning mathematical reasoning (GSM8K, MATH), multi-hop question answering (MuSiQue-Ans), and spatial reasoning (SpaRP), showing consistent improvements in two applications: (1) training Process Reward Models (PRMs) for ranking and aggregating multiple generations, and (2) fine-tuning models via offline reinforcement learning for greedy decoding. On ProcessBench, SPARE demonstrates data-efficient out-of-distribution generalization, using only $\sim$16% of training samples compared to human-labeled and other synthetically trained baselines. Additionally, it achieves competitive performance with MCTS-based methods while offering 2.3$\times$ speedup in terms of total token count. Manual analysis reveals complementary precision-recall characteristics with MCTS approaches, suggesting potential for ensemble methods. These results establish SPARE as a practical and scalable solution for automatic process supervision in LLM reasoning.

</details>

---

### 99. [TRIDENT: Tri-Modal Molecular Representation Learning with Taxonomic Annotations and Local Correspondence](https://arxiv.org/abs/2506.21028)

**基本信息**

- 🔗 arXiv: [`2506.21028`](https://arxiv.org/abs/2506.21028)
- 👥 作者: Feng Jiang, Mangal Prakash, Hehuan Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.21028.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容直接围绕多模态分子表示学习，整合了化学结构（SMILES）、文本描述和功能注释，这属于化学信息学和化学大模型的核心主题。同时，论文提出了TRIDENT框架、新的对齐目标，并策划了包含多模态信息的大规模数据集，为化学大模型的训练和评估提供了重要的方法、模型架构和数据资源。

**📖 中文摘要**

论文介绍了TRIDENT，一个新颖的分子表示学习框架，它整合了分子SMILES、文本描述和分类学功能注释来学习丰富的分子表示。为此，研究策划了一个包含结构化、多层次功能注释的分子-文本对综合数据集。TRIDENT采用基于体积的对齐目标，在全局层面联合对齐三模态特征，实现跨模态的软性、几何感知对齐。此外，TRIDENT引入了一种新颖的局部对齐目标，捕捉分子子结构与其对应子文本描述之间的详细关系。一个基于动量的机制动态平衡全局和局部对齐，使模型能够学习广泛的功能语义和细粒度的结构-功能映射。TRIDENT在11个下游任务上实现了最先进的性能，证明了结合SMILES、文本和分类学功能注释对于分子性质预测的价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular property prediction aims to learn representations that map chemical structures to functional properties. While multimodal learning has emerged as a powerful paradigm to learn molecular representations, prior works have largely overlooked textual and taxonomic information of molecules for representation learning. We introduce TRIDENT, a novel framework that integrates molecular SMILES, textual descriptions, and taxonomic functional annotations to learn rich molecular representations. To achieve this, we curate a comprehensive dataset of molecule-text pairs with structured, multi-level functional annotations. Instead of relying on conventional contrastive loss, TRIDENT employs a volume-based alignment objective to jointly align tri-modal features at the global level, enabling soft, geometry-aware alignment across modalities. Additionally, TRIDENT introduces a novel local alignment objective that captures detailed relationships between molecular substructures and their corresponding sub-textual descriptions. A momentum-based mechanism dynamically balances global and local alignment, enabling the model to learn both broad functional semantics and fine-grained structure-function mappings. TRIDENT achieves state-of-the-art performance on 11 downstream tasks, demonstrating the value of combining SMILES, textual, and taxonomic functional annotations for molecular property prediction.

</details>

---

### 100. [Iterative Distillation for Reward-Guided Fine-Tuning of Diffusion Models in Biomolecular Design](https://arxiv.org/abs/2507.00445)

**基本信息**

- 🔗 arXiv: [`2507.00445`](https://arxiv.org/abs/2507.00445)
- 👥 作者: Xingyu Su, Xiner Li, Masatoshi Uehara 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.00445.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容直接围绕用于生物分子（蛋白质、小分子）设计的扩散模型的奖励引导微调，这属于化学信息学和AI辅助分子设计的核心主题。同时，论文提出了一种新颖、稳定的迭代蒸馏框架，用于优化扩散模型以适应任意奖励函数，这为化学大模型（特别是生成模型）的性能优化和定向设计提供了重要的算法工具和方法论。

**📖 中文摘要**

论文解决了在生物分子设计中为奖励引导生成微调扩散模型的问题。现实世界的应用通常不仅需要高保真生成，还需要针对可能不可微的奖励函数（如基于物理的模拟或基于科学知识的奖励）进行优化。尽管已有RL方法被探索用于微调扩散模型以实现此类目标，但它们往往由于在线策略性质而存在不稳定、样本效率低和模式崩溃的问题。为此，论文提出了一种基于迭代蒸馏的微调框架，使扩散模型能够针对任意奖励函数进行优化。该方法将问题转化为策略蒸馏：在roll-in阶段收集离线策略数据，在roll-out阶段模拟基于奖励的软最优策略，并通过最小化模拟的软最优策略与当前模型策略之间的KL散度来更新模型。这种离线策略公式与KL散度最小化相结合，增强了与现有基于RL的方法相比的训练稳定性和样本效率。实证结果证明了该方法在蛋白质、小分子和调控DNA设计等多种任务中的有效性和优异的奖励优化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We address the problem of fine-tuning diffusion models for reward-guided generation in biomolecular design. While diffusion models have proven highly effective in modeling complex, high-dimensional data distributions, real-world applications often demand more than high-fidelity generation, requiring optimization with respect to potentially non-differentiable reward functions such as physics-based simulation or rewards based on scientific knowledge. Although RL methods have been explored to fine-tune diffusion models for such objectives, they often suffer from instability, low sample efficiency, and mode collapse due to their on-policy nature. In this work, we propose an iterative distillation-based fine-tuning framework that enables diffusion models to optimize for arbitrary reward functions. Our method casts the problem as policy distillation: it collects off-policy data during the roll-in phase, simulates reward-based soft-optimal policies during roll-out, and updates the model by minimizing the KL divergence between the simulated soft-optimal policy and the current model policy. Our off-policy formulation, combined with KL divergence minimization, enhances training stability and sample efficiency compared to existing RL-based methods. Empirical results demonstrate the effectiveness and superior reward optimization of our approach across diverse tasks in protein, small molecule, and regulatory DNA design. The source code is released at ( this https URL ).

</details>

---

### 101. [A Genetic Algorithm for Navigating Synthesizable Molecular Spaces](https://arxiv.org/abs/2509.20719)

**基本信息**

- 🔗 arXiv: [`2509.20719`](https://arxiv.org/abs/2509.20719)
- 👥 作者: Alston Lo, Connor W. Coley, Wojciech Matusik
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.20719.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学中的分子设计，特别是利用遗传算法在可合成的化学空间中进行导航和优化，这与“化学大模型”主题中利用算法模型探索化学空间的方向高度相关。

**📖 中文摘要**

本文提出SynGA，一种直接在合成路线上运行的遗传算法，用于在可合成的分子空间中进行导航。该方法具有定制的交叉和变异算子，将其明确约束在可合成的分子空间内。通过修改适应度函数，SynGA在多种设计任务中展现出有效性，包括可合成类似物搜索和样本高效的性质优化。此外，通过将SynGA与基于机器学习的过滤器耦合以聚焦构建块集，其性能提升至最先进水平。对于性质优化，这表现为一个基于模型的变体SynGBO，它在贝叶斯优化的内循环中采用SynGA和块过滤。由于SynGA是轻量级的且通过构造强制执行可合成性，它不仅可以作为一个强大的独立基线，也可以作为一个可集成到未来更大合成感知工作流程中的通用模块。该工作与化学信息学中的分子设计主题直接相关，特别是利用算法在化学空间中进行探索和优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inspired by the effectiveness of genetic algorithms and the importance of synthesizability in molecular design, we present SynGA, a simple genetic algorithm that operates directly over synthesis routes. Our method features custom crossover and mutation operators that explicitly constrain it to synthesizable molecular space. By modifying the fitness function, we demonstrate the effectiveness of SynGA on a variety of design tasks, including synthesizable analog search and sample-efficient property optimization, for both 2D and 3D objectives. Furthermore, by coupling SynGA with a machine learning-based filter that focuses the building block set, we boost SynGA to state-of-the-art performance. For property optimization, this manifests as a model-based variant SynGBO, which employs SynGA and block filtering in the inner loop of Bayesian optimization. Since SynGA is lightweight and enforces synthesizability by construction, our hope is that SynGA can not only serve as a strong standalone baseline but also as a versatile module that can be incorporated into larger synthesis-aware workflows in the future.

</details>

---

### 102. [G-reasoner: Foundation Models for Unified Reasoning over Graph-structured Knowledge](https://arxiv.org/abs/2509.24276)

**基本信息**

- 🔗 arXiv: [`2509.24276`](https://arxiv.org/abs/2509.24276)
- 👥 作者: Linhao Luo, Zicheng Zhao, Junnan Liu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24276.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个统一的图-语言基础模型框架（G-reasoner），用于在结构化知识上进行推理。这直接关联“化学大模型”和“质谱结构推理”主题中对复杂、结构化化学信息（如分子图、质谱解析）进行建模和推理的需求。

**📖 中文摘要**

本文提出G-reasoner，一个将图与语言基础模型相集成的统一框架，用于在多样化的图结构知识上进行可扩展的推理。核心是QuadGraph，一个将异构知识源统一为通用图表示的四层抽象。在此基础上，引入了一个3400万参数的图基础模型，该模型共同捕获图拓扑和文本语义，并与LLMs集成以增强下游应用中的推理。为确保可扩展性和效率，实现了混合精度训练和分布式消息传递。在六个基准测试上的广泛实验表明，G-reasoner始终优于最先进的基线，显著增强了LLM的推理能力，并实现了强大的效率和跨图泛化能力。该框架旨在解决知识密集型任务中现有检索增强生成方法的局限性，通过图结构对知识关系进行建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) excel at complex reasoning but remain limited by static and incomplete parametric knowledge. Retrieval-augmented generation (RAG) mitigates this by incorporating external knowledge, yet existing RAGs struggle with knowledge-intensive tasks due to fragmented information and weak modeling of knowledge structure. Graphs offer a natural way to model relationships within knowledge, but LLMs are inherently unstructured and cannot effectively reason over graph-structured data. Recent graph-enhanced RAG (GraphRAG) attempts to bridge this gap by constructing tailored graphs and enabling LLMs to reason on them. However, these methods often depend on ad-hoc graph designs, heuristic search, or costly agent pipelines, which hinder scalability and generalization. To address these challenges, we present G-reasoner, a unified framework that integrates graph and language foundation models for scalable reasoning over diverse graph-structured knowledge. Central to our approach is QuadGraph, a standardized four-layer abstraction that unifies heterogeneous knowledge sources into a common graph representation. Building on this, we introduce a 34M-parameter graph foundation model (GFM) that jointly captures graph topology and textual semantics, and is integrated with LLMs to enhance reasoning in downstream applications. To ensure scalability and efficiency, mixed-precision training and distributed message-passing are implemented to scale GFM with more GPUs. Extensive experiments on six benchmarks show that G-reasoner consistently outperforms state-of-the-art baselines, significantly enhances LLM reasoning, and achieves strong efficiency and cross-graph generalization.

</details>

---

### 103. [LEAP: Local ECT-Based Learnable Positional Encodings for Graphs](https://arxiv.org/abs/2510.00757)

**基本信息**

- 🔗 arXiv: [`2510.00757`](https://arxiv.org/abs/2510.00757)
- 👥 作者: Juan Amboage, Ernst Röell, Patrick Schnider 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.00757.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的图结构位置编码方法（LEAP），用于增强图神经网络的能力。这与“化学大模型”和“质谱结构推理”中处理分子图结构、从复杂数据中学习拓扑和几何特征的需求直接相关。

**📖 中文摘要**

本文提出LEAP，一种基于可微分欧拉特征变换及其局部变体的、端到端可训练的新型局部结构位置编码方法，用于图神经网络。欧拉特征变换是一种可高效计算的几何拓扑不变量，用于表征形状和图。LEAP结合了DECT及其局部变体，作为图表示学习流程中提取拓扑特征的强大组件。该方法在多个真实世界数据集以及一个旨在测试其提取拓扑特征能力的合成任务上进行了评估。结果凸显了基于LEAP的编码作为图表示学习流程强大组件的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph neural networks (GNNs) largely rely on the message-passing paradigm, where nodes iteratively aggregate information from their neighbors. Yet, standard message passing neural networks (MPNNs) face well-documented theoretical and practical limitations. Graph positional encoding (PE) has emerged as a promising direction to address these limitations. The Euler Characteristic Transform (ECT) is an efficiently computable geometric-topological invariant that characterizes shapes and graphs. In this work, we combine the differentiable approximation of the ECT (DECT) and its local variant ($\ell$-ECT) to propose LEAP, a new end-to-end trainable local structural PE for graphs. We evaluate our approach on multiple real-world datasets as well as on a synthetic task designed to test its ability to extract topological features. Our results underline the potential of LEAP-based encodings as a powerful component for graph representation learning pipelines.

</details>

---

### 104. [Energy-Regularized Sequential Model Editing on Hyperspheres](https://arxiv.org/abs/2510.01172)

**基本信息**

- 🔗 arXiv: [`2510.01172`](https://arxiv.org/abs/2510.01172)
- 👥 作者: Qingyuan Liu, Jia-Chen Gu, Yunzhi Yao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01172.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型的知识编辑，这是一种使大模型（包括潜在的化学大模型）能够高效更新和修正知识（如化学事实、谱图解析规则）的关键技术。

**📖 中文摘要**

本文研究大型语言模型的知识编辑问题，特别是顺序编辑导致的性能退化。作者假设超球面均匀性有助于模型保持稳定并容纳新知识。他们使用超球面能量来量化编辑过程中的神经元均匀性，并检验其与编辑性能的相关性。基于此，提出了SPHERE，一种超球面能量驱动的正则化策略，通过将新知识投影到与预训练权重矩阵主超球面方向互补的稀疏空间中来稳定神经元权重分布，从而在实现可靠顺序更新的同时保留先验知识。在LLaMA3和Qwen2.5上的大量实验表明，SPHERE在编辑能力上平均优于最佳基线16.41%，同时最忠实地保留了一般模型性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) require constant updates to remain aligned with evolving real-world knowledge. Model editing offers a lightweight alternative to retraining, but sequential editing often destabilizes representations and induces catastrophic forgetting. In this work, we seek to better understand and mitigate performance degradation caused by sequential editing. We hypothesize that hyperspherical uniformity, a property that maintains uniform distribution of neuron weights on a hypersphere, helps the model remain stable, retain prior knowledge, while still accommodate new updates. We use Hyperspherical Energy (HE) to quantify neuron uniformity during editing, and examine its correlation with editing performance. Empirical studies across widely used editing methods reveals a strong correlation between HE dynamics and editing performance, with editing failures consistently coinciding with high HE fluctuations. We further theoretically prove that HE dynamics impose a lower bound on the degradation of pretrained knowledge, highlighting why HE stability is crucial for knowledge retention. Motivated by these insights, we propose SPHERE (Sparse Projection for Hyperspherical Energy-Regularized Editing), an HE-driven regularization strategy that stabilizes neuron weight distributions, ultimately preserving prior knowledge while enabling reliable sequential updates. Specifically, SPHERE identifies a sparse space complementary to the principal hyperspherical directions of the pretrained weight matrices and projects new knowledge onto it, attenuating perturbations on the principal directions. Extensive experiments on LLaMA3 (8B) and Qwen2.5 (7B) show that SPHERE outperforms the best baseline in editing capability by an average of 16.41%, while most faithfully preserving general model performance, thereby offering a principled path toward reliable large-scale knowledge editing.

</details>

---

### 105. [RLP: Reinforcement as a Pretraining Objective](https://arxiv.org/abs/2510.01265)

**基本信息**

- 🔗 arXiv: [`2510.01265`](https://arxiv.org/abs/2510.01265)
- 👥 作者: Ali Hatamizadeh, Syeda Nahida Akter, Shrimai Prabhumoye 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01265.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种新的预训练目标（RLP），旨在让大语言模型在预训练阶段就涌现出有用的思维链推理能力。这直接关系到构建具有更强推理能力的“化学大模型”，以解决如质谱结构推理等复杂问题。

**📖 中文摘要**

本文提出RLP，一种信息驱动的强化预训练目标，将强化学习的核心精神——探索——引入预训练的最后阶段。关键思想是将思维链视为一种探索性动作，其奖励基于它为预测未来token所提供的信息增益来计算。这个训练目标本质上鼓励模型在预测接下来内容之前进行独立思考，从而在预训练的早期阶段教授独立的思考行为。具体而言，奖励信号衡量在同时以上下文和采样的推理链为条件时，下一个token的对数似然相比仅以上下文为条件时的增加。这种方法产生了一个无验证器的密集奖励信号，允许在预训练期间对整个文档流进行高效训练。在Qwen3-1.7B-Base上的预训练实验表明，RLP在八项数学和科学基准测试的整体平均分上提升了19%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The dominant paradigm for training large reasoning models starts with pre-training using next-token prediction loss on vast amounts of data. Reinforcement learning, while powerful in scaling reasoning, is introduced only as the very last phase of post-training, preceded by supervised fine-tuning. While dominant, is this an optimal way of training? In this paper, we present RLP, an information-driven reinforcement pretraining objective, that brings the core spirit of reinforcement learning -- exploration -- to the last phase of pretraining. The key idea is to treat chain-of-thought as an exploratory action, with rewards computed based on the information gain it provides for predicting future tokens. This training objective essentially encourages the model to think for itself before predicting what comes next, thus teaching an independent thinking behavior earlier in the pretraining. More concretely, the reward signal measures the increase in log-likelihood of the next token when conditioning on both context and a sampled reasoning chain, compared to conditioning on context alone. This approach yields a verifier-free dense reward signal, allowing for efficient training for the full document stream during pretraining. Specifically, RLP reframes reinforcement learning for reasoning as a pretraining objective on ordinary text, bridging the gap between next-token prediction and the emergence of useful chain-of-thought reasoning. Pretraining with RLP on Qwen3-1.7B-Base lifts the overall average across an eight-benchmark math-and-science suite by 19%. With identical post-training, the gains compound, with the largest improvements on reasoning-heavy tasks such as AIME25 and MMLU-Pro. Applying RLP to the Nemotron-Nano-12B-v2 increases the overall average from 42.81% to 61.32% and raises the average on scientific reasoning by 23%, demonstrating scalability across architectures and model sizes.

</details>

---

### 106. [TiTok: Transfer Token-level Knowledge via Contrastive Excess to Transplant LoRA](https://arxiv.org/abs/2510.04682)

**基本信息**

- 🔗 arXiv: [`2510.04682`](https://arxiv.org/abs/2510.04682)
- 👥 作者: Chanjoo Jung, Jaehyung Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04682.pdf)

**💡 相关性分析**

满足标准2：论文提出的TiTok框架是一种实现参数高效微调（PEFT）模块（LoRA）跨模型迁移的新工具和方法。虽然论文本身不直接针对化学或质谱，但其核心是解决大模型适配中的工具/方法问题，属于为‘化学大模型’的构建和优化提供了潜在的技术路径和工具资源。

**📖 中文摘要**

本文提出了一种名为TiTok的新框架，旨在实现LoRA（Low-Rank Adaptation）参数在不同骨干模型间的有效迁移。核心思想是通过对比源模型在应用LoRA前后产生的token级信息差异（即“对比超额”），来捕获任务相关信息，并以此筛选合成数据，从而实现无需额外模型开销的知识蒸馏。该方法在多个基准测试和迁移设置中均表现出稳定的有效性，平均性能提升达4%~10%。这项工作为参数高效微调（PEFT）领域提供了新的工具和思路，其提出的token级知识捕获和迁移机制，对于构建和优化面向特定任务（如化学信息学中的分子性质预测或质谱解析）的“化学大模型”具有潜在的应用价值，属于为特定主题提供方法工具的相关研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are widely applied in real world scenarios, yet fine-tuning them comes with significant computational and storage costs. Parameter-Efficient Fine-Tuning (PEFT) methods such as LoRA mitigate these costs; however, the adapted parameters are dependent on the base model and cannot be transferred across different backbones. One way to address this issue is through knowledge distillation, but its effectiveness inherently depends on training data. Recent work such as TransLoRA avoids this by generating synthetic data; nevertheless, this adds complexity since it requires training an additional discriminator model. In this paper, we propose TiTok, a new framework that enables effective LoRA Transplantation through Token-level knowledge transfer. Specifically, TiTok captures task-relevant information through a token-wise contrastive excess between a source model with and without LoRA. This excess highlights informative tokens and enables selective filtering of synthetic data, all without additional models or overhead. Through experiments on three benchmarks across multiple transfer settings, we demonstrate that TiTok is consistently effective, achieving average performance gains of +4~10% compared to baselines overall.

</details>

---

### 107. [SwiReasoning: Switch-Thinking in Latent and Explicit for Pareto-Superior Reasoning LLMs](https://arxiv.org/abs/2510.05069)

**基本信息**

- 🔗 arXiv: [`2510.05069`](https://arxiv.org/abs/2510.05069)
- 👥 作者: Dachuan Shi, Abedelkadir Asi, Keying Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.05069.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型（LLM）的推理能力，提出了一个在显式和隐式推理间动态切换的通用框架。这直接关系到如何构建和优化能够进行复杂科学推理（如化学结构推理）的‘化学大模型’，属于核心主题相关。

**📖 中文摘要**

本文提出了SwiReasoning框架，旨在解决大语言模型（LLM）在推理任务中面临的效率与准确性权衡问题。该框架的核心创新在于动态地在显式推理（如思维链）和隐式推理（在潜在空间中进行连续推理）之间进行切换。切换的指导信号来源于对下一个token分布熵趋势的块级置信度估计。通过限制最大切换次数，该框架还能抑制过度思考，提升token效率。在广泛的数学、STEM、编程和通用基准测试中，SwiReasoning能持续提升不同模型系列和规模的推理LLM的平均准确率1.8%-3.1%，并在预算受限时显著提升token效率。这项工作深入探讨了LLM的推理机制，并提出了一个通用的、无需训练的优化框架，对于理解和提升‘化学大模型’在复杂科学推理（如分子结构推导、反应预测）任务中的性能具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent work shows that, beyond discrete reasoning through explicit chain-of-thought steps, which are limited by the boundaries of natural languages, large language models (LLMs) can also reason continuously in latent space, allowing richer information per step and thereby improving token efficiency. Despite this promise, latent reasoning still faces two challenges, especially in training-free settings: 1) purely latent reasoning broadens the search distribution by maintaining multiple implicit paths, which diffuses probability mass, introduces noise, and impedes convergence to a single high-confidence solution, thereby hurting accuracy; and 2) overthinking persists even without explicit text, wasting tokens and degrading efficiency. To address these issues, we introduce SwiReasoning, a training-free framework for LLM reasoning which features two key innovations: 1) SwiReasoning dynamically switches between explicit and latent reasoning, guided by block-wise confidence estimated from entropy trends in next-token distributions, to balance exploration and exploitation and promote timely convergence. 2) By limiting the maximum number of thinking-block switches, SwiReasoning curbs overthinking and improves token efficiency across varying problem difficulties. On widely used mathematics, STEM, coding, and general benchmarks, SwiReasoning consistently improves average accuracy by 1.8%-3.1% across reasoning LLMs of different model families and scales. Furthermore, under constrained budgets, SwiReasoning improves average token efficiency by 57%-79%, with larger gains as budgets tighten.

</details>

---

### 108. [MASA: Rethinking the Representational Bottleneck in LoRA with Multi-A Shared Adaptation](https://arxiv.org/abs/2510.06005)

**基本信息**

- 🔗 arXiv: [`2510.06005`](https://arxiv.org/abs/2510.06005)
- 👥 作者: Qin Dong, Yuntian Tang, Heming Jia 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.06005.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种改进的参数高效微调（PEFT）架构MASA，旨在通过增强特征适应能力来提升大模型在下游任务上的表现。这为‘化学大模型’的领域适配和微调提供了新的、潜在更有效的工具和方法。

**📖 中文摘要**

本文针对参数高效微调（PEFT）的主流方法LoRA（低秩适应）提出了改进架构MASA（Multi-A Shared Adaptation）。作者指出，标准的LoRA依赖单一的下投影矩阵（A）会形成表征瓶颈，难以捕获复杂任务所需的多样化信号。MASA采用多专家A矩阵、单共享B矩阵的结构，其中多个专家A被非对称地跨层共享以保证参数效率。这些专家捕获多样化特征，然后由层特定的B矩阵进行整合。实验表明，在MMLU等基准测试上，MASA以可比的参数量（0.52%）超越了标准LoRA。这项工作是对大模型微调架构的重要改进，其目标是通过更丰富的特征适应来提升下游任务适应能力。这对于需要精细调整以适应特定科学领域（如化学信息学）的‘化学大模型’的构建和优化，提供了新的、更高效的PEFT架构选择，属于方法工具层面的贡献。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Low-Rank Adaptation (LoRA) has emerged as a dominant method in Parameter-Efficient Fine-Tuning (PEFT) for large language models, which augments the transformer layer with one down-projection $A$ and one up-projection $B$. However, LoRA's reliance on a single down-projection matrix ($A$) creates a representational bottleneck, as this solitary feature extractor is inherently insufficient for capturing the diverse signals required by complex tasks. This motivates our architectural shift to focus on enriching the feature adaptation to improve the downstream task adaptation ability. We propose MASA (Multi-$A$ Shared Adaptation), an architecture that implements a multi-$A$, single-$B$ structure where the multi-$A$ expert ensemble is asymmetrically shared across layers to ensure parameter efficiency. In MASA, these specialized experts capture diverse features, which are then integrated by a single, layer-specific $B$-matrix. The effectiveness and versatility of our method are validated through a comprehensive suite of experiments spanning multi-domain generalization, single-domain specialization, and multi-task reasoning. For example, on the MMLU benchmark, MASA achieves an average accuracy of 59.62%, outperforming the standard LoRA by 1.08 points (a relative improvement of 1.84%) with comparable learnable parameters of 0.52%.

</details>

---

### 109. [Relational Transformer: Toward Zero-Shot Foundation Models for Relational Data](https://arxiv.org/abs/2510.06377)

**基本信息**

- 🔗 arXiv: [`2510.06377`](https://arxiv.org/abs/2510.06377)
- 👥 作者: Rishabh Ranjan, Valter Hudovernik, Mark Znidar 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.06377.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是提出一种能直接处理异构关系数据并支持零样本迁移的基础模型架构（RT）。这直接关联到构建能够理解和推理化学数据库、谱图-结构关系等结构化科学数据的‘化学大模型’，属于核心主题相关。同时，它也为这些主题提供了一种潜在的新型模型架构工具。

**📖 中文摘要**

本文提出了关系型Transformer（RT）架构，旨在为零样本的关系型数据基础模型奠定基础。RT能够通过预训练适应多样的关系数据库，并直接应用于未见过的数据集和任务，无需任务特定微调或上下文示例检索。其核心创新包括通过任务表提示进行任务指定、结合表/列元数据的单元标记化、掩码标记预测预训练，以及一种新颖的跨列、行和主外键链接的关系注意力机制。在RelBench数据集上的预训练表明，RT在零样本设置下取得了强劲的性能。这项工作代表了构建通用关系数据基础模型的重要一步。虽然不直接针对化学或质谱，但其处理结构化、异构关系数据（类似于化学数据库、质谱-结构关联数据库）的能力，以及零样本迁移的愿景，与‘化学大模型’和‘质谱结构推理’中处理复杂、结构化科学数据的需求高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pretrained transformers readily adapt to new sequence modeling tasks via zero-shot prompting, but relational domains still lack architectures that transfer across datasets and tasks. The core challenge is the diversity of relational data, with varying heterogeneous schemas, graph structures and functional dependencies. In this paper, we present the Relational Transformer (RT) architecture, which can be pretrained on diverse relational databases and directly applied to unseen datasets and tasks without task- or dataset-specific fine-tuning, or retrieval of in-context examples. RT (i) incorporates task specification via task table prompting, (ii) tokenizes cells with table/column metadata, (iii) is pretrained via masked token prediction, and (iv) utilizes a novel Relational Attention mechanism over columns, rows, and primary-foreign key links. Pretrained on RelBench datasets spanning tasks such as churn and sales forecasting, RT attains strong zero-shot performance, averaging 93% of fully supervised AUROC on binary classification tasks with a single forward pass of a 22M parameter model, as opposed to 84% for a 27B LLM. Fine-tuning yields state-of-the-art results with high sample efficiency. Our experimental analyses show that RT's zero-shot transfer leverages task context, relational attention patterns and schema semantics. Overall, RT provides a practical path toward foundation models for relational data. Code, models, data: this https URL .

</details>

---

### 110. [On the Reasoning Abilities of Masked Diffusion Language Models](https://arxiv.org/abs/2510.13117)

**基本信息**

- 🔗 arXiv: [`2510.13117`](https://arxiv.org/abs/2510.13117)
- 👥 作者: Anej Svete, Ashish Sabharwal
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.13117.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是理论分析掩码扩散语言模型（MDMs）的推理能力及其与思维链等推理框架的关系。这直接关系到评估和选择适合构建下一代‘化学大模型’（可能采用扩散等非自回归架构）的模型范式，属于核心主题相关。

**📖 中文摘要**

本文从计算理论的角度，深入分析了掩码扩散语言模型（MDMs）的推理能力。作者将MDMs与思维链（CoT）增强的Transformer以及填充循环Transformer（PLTs）在有限精度对数宽度设置下联系起来，证明了MDMs能够解决CoT增强Transformer所能解决的所有问题，并且对于某些问题类别（如正则语言），MDMs凭借其并行生成能力，能实现比CoT Transformer更高效的推理。这项工作首次从理论层面刻画了MDMs这类并行生成模型在解决推理问题上的能力和效率边界。对于探索新型非自回归模型（如扩散模型）在构建‘化学大模型’、尤其是进行高效并行科学推理（如分子生成、性质预测）方面的潜力，提供了重要的理论依据和见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Masked diffusion models (MDMs) for text offer a compelling alternative to traditional autoregressive language models. Parallel generation makes them efficient, but their computational capabilities and the limitations inherent in their parallelism remain largely unexplored. To this end, we characterize what types of reasoning problems MDMs can provably solve and how efficiently. We do this by connecting MDMs to the well-understood reasoning frameworks of chain of thought (CoT) and padded looped transformers (PLTs) in the finite-precision log-width setting: We show that MDMs and polynomially-padded PLTs are, in fact, equivalent in this setting, and that MDMs can solve all problems that CoT-augmented transformers can. Moreover, we showcase classes of problems (including regular languages) for which MDMs are inherently more efficient than CoT transformers, where parallel generation allows for substantially faster reasoning.

</details>

---

### 111. [Reliable Fine-Grained Evaluation of Natural Language Math Proofs](https://arxiv.org/abs/2510.13888)

**基本信息**

- 🔗 arXiv: [`2510.13888`](https://arxiv.org/abs/2510.13888)
- 👥 作者: Wenjie Ma, Andrei Cojocaru, Neel Kolhe 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.13888.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出了一套构建可靠、细粒度证明评估器的方法论，并发布了首个专家标注的评估数据集ProofBench。这为评估‘化学大模型’或‘质谱结构推理’模型生成的复杂科学解释、推理链的可靠性和质量，提供了至关重要的评估工具和基准资源。

**📖 中文摘要**

本文针对大语言模型生成的数学自然语言证明的评估难题，提出了一套系统的方法论来开发和验证细粒度评估器。作者引入了ProofBench，这是第一个由专家标注的数学证明细粒度评分数据集，涵盖了来自六大数学竞赛的145个问题和435个LLM生成的解答。基于此，论文系统探索了评估器的设计空间，并最终提出了ProofGrader评估器。该评估器结合了强大的推理骨干模型、来自参考答案和评分方案的丰富上下文以及简单的集成方法，在专家评分上实现了较低的均方误差。实验证明，ProofGrader在最佳-n选择任务中能显著提升所选证明的质量。这项工作为解决复杂科学推理（包括化学推理、质谱解析逻辑）输出的可靠、细粒度评估提供了重要的方法论参考和工具原型，是推动相关领域模型发展不可或缺的一环。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) for mathematical reasoning have largely focused on tasks with easily verifiable final answers while generating and verifying natural language math proofs remains an open challenge. We identify the absence of a reliable, fine-grained evaluator for LLM-generated math proofs as a critical gap. To address this, we propose a systematic methodology for developing and validating evaluators that assign fine-grained scores on a 0-7 scale to model-generated math proofs. To enable this study, we introduce ProofBench, the first expert-annotated dataset of fine-grained proof ratings, spanning 145 problems from six major math competitions (USAMO, IMO, Putnam, etc) and 435 LLM-generated solutions from Gemini-2.5-Pro, o3, and DeepSeek-R1. Using ProofBench as a testbed, we systematically explore the evaluator design space across key axes: the backbone model, input context, instructions and evaluation workflow. Our analysis delivers ProofGrader, an evaluator that combines a strong reasoning backbone LM, rich context from reference solutions and marking schemes, and a simple ensembling method; it achieves a low Mean Absolute Error (MAE) of 0.926 against expert scores, significantly outperforming naive baselines. Finally, we demonstrate its practical utility in a best-of-$n$ selection task: at $n=16$, ProofGrader achieves an average score of 4.14/7, closing 78\% of the gap between a naive binary evaluator (2.48) and the human oracle (4.62), highlighting its potential to advance downstream proof generation.

</details>

---

### 112. [Soft-Masked Diffusion Language Models](https://arxiv.org/abs/2510.17206)

**基本信息**

- 🔗 arXiv: [`2510.17206`](https://arxiv.org/abs/2510.17206)
- 👥 作者: Michael Hersche, Samuel Moor-Smith, Thomas Hofmann 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.17206.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种改进扩散语言模型生成机制的软掩码（SM）技术，能提升模型在代码生成等任务上的性能。这为构建基于扩散模型的‘化学大模型’（例如用于分子SMILES生成或化学文本生成）提供了一种新的、潜在更优的模型底层技术工具。

**📖 中文摘要**

本文针对扩散语言模型中常用的二值掩码机制提出了改进，引入了软掩码（Soft-Masking, SM）方法。传统的二值掩码在解码时，对于保留的掩码位置直接丢弃了预测信息。SM则动态地将掩码标记的嵌入与上一步解码中top-k预测标记的嵌入进行混合，为模型提供了更丰富的信息先验，允许部分信息跨步传播。作者提出了相应的训练方法，并证明从头开始训练或对预训练模型进行持续预训练加入SM，都能提升模型性能（困惑度、MAUVE分数）。在代码生成基准测试中，对现有SOTA扩散模型进行SM微调后，性能得到一致提升。这项工作是对扩散模型文本生成机制的重要改进，提升了其推理和生成质量。对于探索使用扩散模型架构构建‘化学大模型’（如用于分子序列生成、描述生成）的研究者来说，SM提供了一种提升模型表现力的有效技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have demonstrated strong potential in language modeling, offering various advantages over traditional autoregressive approaches. Their ability to generate and revise entire responses in parallel enables faster generation and built-in self-correction mechanisms. Most modern diffusion-based language models employ masked diffusion, where decoding involves iteratively processing masked tokens based on a binary decision: either retaining the mask or replacing it with the predicted token. However, this binary choice discards valuable predictive information when the mask is retained. To address this limitation, we introduce soft-masking (SM), a novel method that dynamically blends the embedding of the mask token with the embeddings of the top-k predicted tokens from the previous decoding step, for each retained mask. This provides the model with a more informative prior, preserving context from earlier computations and allowing partial information about masked tokens to propagate beyond a single step. We propose a training methodology that efficiently adapts masked diffusion language models to incorporate SM. We demonstrate that training a 169M parameter model from scratch with SM yields superior perplexity and MAUVE scores compared to binary masking baselines. Similarly, a pretrained model can be enhanced with SM through continued pretraining. Finally, we finetune two state-of-the-art diffusion models, Dream-7B and Dream-Coder-7B, with SM. SM consistently improves performance across multiple coding benchmarks, particularly in high-throughput settings. The code is available at this https URL .

</details>

---

### 113. [Scaling Laws Meet Model Architecture: Toward Inference-Efficient LLMs](https://arxiv.org/abs/2510.18245)

**基本信息**

- 🔗 arXiv: [`2510.18245`](https://arxiv.org/abs/2510.18245)
- 👥 作者: Song Bian, Tao Yu, Shivaram Venkataraman 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.18245.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型的架构设计与缩放定律，旨在寻找推理效率与准确性之间的最优平衡。这直接关系到如何为计算化学、质谱分析等领域设计和部署高效、实用的‘化学大模型’，属于核心主题相关。

**📖 中文摘要**

本文研究了在大语言模型（LLM）扩展中，模型架构对推理效率和准确性的联合影响。作者引入了条件缩放定律，将Chinchilla框架与隐藏大小、MLP-注意力参数分配比、分组查询注意力（GQA）等关键架构因素相结合。基于此，提出了一个搜索框架，用于识别同时具备高推理效率和准确性的架构。为了验证，作者训练了超过200个从80M到3B参数、8B到100B训练token的模型，并拟合了所提出的条件缩放定律。结果表明，优化后的架构在相同训练预算下，比LLaMA-3.2等基线实现了更高的准确性和推理吞吐量。这项工作为在资源约束下设计和缩放高效能的‘化学大模型’提供了重要的指导原则和实证依据，直接关系到如何权衡模型能力与部署成本。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling the number of parameters and the size of training data has proven to be an effective strategy for improving large language model (LLM) performance. Yet, as these models grow increasingly powerful and widely deployed, the cost of inference has become a pressing concern. Despite its importance, the trade-off between model accuracy and inference efficiency remains underexplored. In this work, we examine how key architectural factors, hidden size, the allocation of parameters between MLP and attention (mlp-to-attention ratio), and grouped-query attention (GQA), influence both inference cost and accuracy. We introduce a conditional scaling law that augments the Chinchilla framework with architectural information, along with a search framework for identifying architectures that are simultaneously inference-efficient and accurate. To validate our approach, we train more than 200 models spanning 80M to 3B parameters and 8B to 100B training tokens, and fit the proposed conditional scaling law. Our results show that the conditional scaling law reliably predicts optimal architectural choices and that the resulting models outperform existing open-source baselines. Under the same training budget, optimized architectures achieve up to 2.1% higher accuracy and 42% greater inference throughput compared to LLaMA-3.2.

</details>

---

### 114. [Learning Boltzmann Generators via Constrained Mass Transport](https://arxiv.org/abs/2510.18460)

**基本信息**

- 🔗 arXiv: [`2510.18460`](https://arxiv.org/abs/2510.18460)
- 👥 作者: Christopher von Klitzing, Denis Blessing, Henrik Schopmans 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.18460.pdf)

**💡 相关性分析**

满足标准2：论文提出了CMT框架，显著改进了玻尔兹曼生成器（BGs）这一用于物理系统（如分子）采样的生成模型的训练效果。这为‘化学大模型’中涉及分子构象生成、化学空间探索等任务提供了更强大、更高效的底层生成工具和方法。

**📖 中文摘要**

本文针对从高维、多模态未归一化概率分布（如分子系统的玻尔兹曼分布）中高效采样的挑战，提出了约束质量传输（Constrained Mass Transport, CMT）框架，用于改进玻尔兹曼生成器（Boltzmann Generators, BGs）的训练。CMT在变分框架下生成中间分布，并对连续步骤间的KL散度和熵衰减施加约束，从而增强分布重叠、缓解质量传输问题并抵抗过早收敛。在标准BG基准和新引入的ELIL四肽系统上的实验表明，CMT consistently超越了SOTA变分方法，实现了2.5倍以上的有效样本量提升，同时避免了模式崩溃。这项工作显著提升了生成模型在物理系统（包括分子构象）采样上的效率和效果。虽然BG本身是生成模型，但其高效采样物理相关分布的能力，是构建能够探索化学空间、生成合理分子结构的‘化学大模型’的重要组成部分，属于底层生成技术的关键进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Efficient sampling from high-dimensional and multimodal unnormalized probability distributions is a central challenge in many areas of science and machine learning. We focus on Boltzmann generators (BGs) that aim to sample the Boltzmann distribution of physical systems, such as molecules, at a given temperature. Classical variational approaches that minimize the reverse Kullback-Leibler divergence are prone to mode collapse, while annealing-based methods, commonly using geometric schedules, can suffer from mass teleportation and rely heavily on schedule tuning. We introduce Constrained Mass Transport (CMT), a variational framework that generates intermediate distributions under constraints on both the KL divergence and the entropy decay between successive steps. These constraints enhance distributional overlap, mitigate mass teleportation, and counteract premature convergence. Across standard BG benchmarks and the here introduced ELIL tetrapeptide, the largest system studied to date without access to samples from molecular dynamics, CMT consistently surpasses state-of-the-art variational methods, achieving more than 2.5x higher effective sample size while avoiding mode collapse.

</details>

---

### 115. [Loopholing Discrete Diffusion: Deterministic Bypass of the Sampling Wall](https://arxiv.org/abs/2510.19304)

**基本信息**

- 🔗 arXiv: [`2510.19304`](https://arxiv.org/abs/2510.19304)
- 👥 作者: Mingyu Jo, Jaesik Yoon, Justin Deschenaux 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.19304.pdf)

**💡 相关性分析**

满足标准2：论文提出了Loopholing机制，显著提升了离散扩散语言模型的生成质量和连贯性。这为构建基于扩散模型的‘化学大模型’（用于文本或序列生成）提供了一种新的、性能更强的底层模型架构改进工具。

**📖 中文摘要**

本文提出了Loopholing机制，旨在解决离散扩散模型在采样过程中面临的信息坍缩问题（即“采样墙”）。一旦进行类别采样，丰富的分布信息就会坍缩为one-hot向量，无法跨步传播。Loopholing通过一个确定性的潜在路径来保留这部分信息，从而形成了Loopholing离散扩散模型（LDDMs）。LDDM使用自条件策略进行高效训练，避免了展开完整的去噪轨迹。实验表明，LDDM大幅降低了生成困惑度（相对提升达61%），缩小了与非自回归模型的差距，并能生成更连贯的文本。在推理任务（如算术）上也表现出性能提升。这项工作是对离散扩散文本生成模型的重要改进，使其更接近自回归模型的质量。对于探索使用扩散模型架构构建高质量‘化学大模型’（如用于分子序列生成、化学反应预测）的研究具有重要的参考价值，提供了一种缓解其固有缺陷的新技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete diffusion models offer a promising alternative to autoregressive generation through parallel decoding, but they suffer from a sampling wall: once categorical sampling occurs, rich distributional information collapses into one-hot vectors and cannot be propagated across steps, forcing subsequent steps to operate with limited information. To mitigate this problem, we introduce Loopholing, a novel and simple mechanism that preserves this information via a deterministic latent pathway, leading to Loopholing Discrete Diffusion Models (LDDMs). Trained efficiently with a self-conditioning strategy that avoids unrolling the full denoising trajectory, LDDMs achieve substantial gains-reducing generative perplexity by up to 61% over prior baselines, thereby closing (and in some cases surpassing) the gap with autoregressive models, and producing more coherent text. Applied to reasoning tasks, LDDMs also improve performance on arithmetic benchmarks such as Countdown and Game of 24. These results also indicate that loopholing mitigates idle steps and oscillations, providing a general and effective path toward high-quality non-autoregressive text generation.

</details>

---

### 116. [DAG-Math: Graph-of-Thought Guided Mathematical Reasoning in LLMs](https://arxiv.org/abs/2510.19842)

**基本信息**

- 🔗 arXiv: [`2510.19842`](https://arxiv.org/abs/2510.19842)
- 👥 作者: Yuanhe Zhang, Ilja Kuzborskij, Jason D. Lee 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.19842.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个基于有向无环图（DAG）的框架和相应的基准（DAG-MATH），用于细粒度评估大语言模型推理过程的规则一致性和逻辑保真度。这为评估‘化学大模型’在复杂科学推理任务中的可靠性和可解释性提供了重要的新型评估工具和基准资源。

**📖 中文摘要**

本文提出将大语言模型的思维链（CoT）建模为基于规则的有向无环图（DAG）上的随机过程，并在此基础上引入了DAG-MATH CoT格式和相应的基准测试。该框架旨在评估LLM的推理过程是否遵循一致的推导规则，而不仅仅是最终答案的正确性。作者提出了“逻辑紧密度”这一度量，用于量化模型的CoT轨迹与DAG结构的贴合程度。实验表明，即使在PASS@k指标相近的情况下，不同LLM家族在推理保真度上存在显著差异。这项工作在自由形式的CoT和形式化证明系统之间取得了平衡，为评估LLM（包括潜在的‘化学大模型’）在科学推理（如化学推导、谱图解析逻辑）中的规则一致性和可靠性提供了新的、更细致的评估框架和诊断工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) demonstrate strong performance on mathematical problems when prompted with Chain-of-Thought (CoT), yet it remains unclear whether this success stems from search, rote procedures, or rule-consistent reasoning. To address this, we propose modeling CoT as a certain rule-based stochastic process over directed acyclic graphs (DAGs), where nodes represent intermediate derivation states and edges encode rule applications. Within this framework, we introduce \textbf{logical closeness}, a metric that quantifies how well a model's CoT trajectory (i.e., the LLM's final output) adheres to the DAG structure, providing evaluation beyond classical PASS@$k$ metrics. Building on this, we introduce the \emph{DAG-MATH} CoT format and construct a benchmark that guides LLMs to generate CoT trajectories in this format, thereby enabling the evaluation of their reasoning ability under our framework. Across standard mathematical reasoning datasets, our analysis uncovers statistically significant differences in reasoning fidelity among representative LLM families-even when PASS@$k$ is comparable-highlighting gaps between final-answer accuracy and rule-consistent derivation. Our framework provides a balance between free-form CoT and formal proofs systems, offering actionable diagnostics for LLMs reasoning evaluation. Our benchmark and code are available at this https URL .

</details>

---

### 117. [BioCAP: Exploiting Synthetic Captions Beyond Labels in Biological Foundation Models](https://arxiv.org/abs/2510.20095)

**基本信息**

- 🔗 arXiv: [`2510.20095`](https://arxiv.org/abs/2510.20095)
- 👥 作者: Ziheng Zhang, Xinyue Ma, Arpita Chowdhury 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.20095.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种利用MLLM生成领域特定合成描述性标题，以增强多模态基础模型语义理解的方法论和流程。这为构建‘化学大模型’或‘质谱结构推理’模型时，如何利用文本描述增强模型对化学结构或谱图的理解，提供了重要的数据资源构建方法和工具思路。

**📖 中文摘要**

本文研究了在生物多模态基础模型中，利用描述性标题作为监督信号的潜力。针对生物领域缺乏大规模实例特异性标题标注的挑战，作者提出利用多模态大语言模型（MLLMs），在维基百科视觉信息和特定分类单元格式示例的引导下，生成合成标题。这些领域特定的上下文有助于减少幻觉，产生准确、基于实例的描述性标题。利用这些标题，作者训练了BioCAP模型，该模型捕获了丰富的语义，并在物种分类和图文检索任务上取得了强劲性能。这项工作展示了超越简单类别标签的描述性标题在桥接生物图像与多模态基础模型方面的价值。其方法论（利用MLLM生成领域特定合成数据以增强模型语义理解）对于构建‘化学大模型’或‘质谱结构推理’模型具有直接的启发性。例如，可以利用类似方法为分子结构图像或质谱图生成描述性文本，以训练更强大的化学多模态模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work investigates descriptive captions as an additional source of supervision for biological multimodal foundation models. Images and captions can be viewed as complementary samples from the latent morphospace of a species, each capturing certain biological traits. Incorporating captions during training encourages alignment with this shared latent structure, emphasizing potentially diagnostic characters while suppressing spurious correlations. The main challenge, however, lies in obtaining faithful, instance-specific captions at scale. This requirement has limited the utilization of natural language supervision in organismal biology compared with many other scientific domains. We complement this gap by generating synthetic captions with multimodal large language models (MLLMs), guided by Wikipedia-derived visual information and taxon-tailored format examples. These domain-specific contexts help reduce hallucination and yield accurate, instance-based descriptive captions. Using these captions, we train BioCAP (i.e., BioCLIP with Captions), a biological foundation model that captures rich semantics and achieves strong performance in species classification and text-image retrieval. These results demonstrate the value of descriptive captions beyond labels in bridging biological images with multimodal foundation models.

</details>

---

### 118. [Clustering by Denoising: Latent plug-and-play diffusion for single-cell data](https://arxiv.org/abs/2510.22835)

**基本信息**

- 🔗 arXiv: [`2510.22835`](https://arxiv.org/abs/2510.22835)
- 👥 作者: Dominik Meier, Shixing Yu, Sagnik Nandy 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22835.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于扩散模型的潜空间去噪聚类框架，专门用于处理高维、嘈杂的单细胞数据。其方法论核心（扩散模型、潜空间去噪、不确定性处理）与‘质谱结构推理’中处理高维、 noisy 谱图数据并推断低维结构信息的任务高度相关，为解决质谱数据分析中的类似问题提供了潜在的新工具和算法思路。

**📖 中文摘要**

本文提出了一种用于单细胞RNA测序（scRNA-seq）数据聚类的新型潜空间即插即用扩散框架。该框架将观测空间和去噪空间分离，通过一种新颖的吉布斯采样过程实现：在低维潜空间中应用学习的扩散先验进行去噪，同时为了引导此过程，将噪声重新引入原始高维观测空间。这种独特的“输入空间引导”确保了去噪轨迹忠实于原始数据结构。该方法具有自适应噪声处理、不确定性量化和可泛化去噪（利用干净参考数据去噪更嘈杂的数据集）三大优势。在合成和真实单细胞基因组学数据上的评估表明，该方法提高了聚类准确性并产生了更具生物学一致性的细胞簇。虽然应用于生物信息学，但其核心思想——利用扩散模型在潜空间进行去噪以提升聚类效果，并处理噪声和不确定性——与‘质谱结构推理’中从嘈杂、高维的质谱数据中推断出清晰、低维的分子结构或类别表示这一核心挑战在方法论上高度同构。该框架为质谱数据的降噪、特征提取和聚类分析提供了新的潜在工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell RNA sequencing (scRNA-seq) enables the study of cellular heterogeneity. Yet, clustering accuracy, and with it downstream analyses based on cell labels, remain challenging due to measurement noise and biological variability. In standard latent spaces (e.g., obtained through PCA), data from different cell types can be projected close together, making accurate clustering difficult. We introduce a latent plug-and-play diffusion framework that separates the observation and denoising space. This separation is operationalized through a novel Gibbs sampling procedure: the learned diffusion prior is applied in a low-dimensional latent space to perform denoising, while to steer this process, noise is reintroduced into the original high-dimensional observation space. This unique "input-space steering" ensures the denoising trajectory remains faithful to the original data structure. Our approach offers three key advantages: (1) adaptive noise handling via a tunable balance between prior and observed data; (2) uncertainty quantification through principled uncertainty estimates for downstream analysis; and (3) generalizable denoising by leveraging clean reference data to denoise noisier datasets, and via averaging, improve quality beyond the training set. We evaluate robustness on both synthetic and real single-cell genomics data. Our method improves clustering accuracy on synthetic data across varied noise levels and dataset shifts. On real-world single-cell data, our method demonstrates improved biological coherence in the resulting cell clusters, with cluster boundaries that better align with known cell type markers and developmental trajectories.

</details>

---

### 119. [Data-Augmented Deep Learning for Downhole Depth Sensing and Validation](https://arxiv.org/abs/2511.00129)

**基本信息**

- 🔗 arXiv: [`2511.00129`](https://arxiv.org/abs/2511.00129)
- 👥 作者: Si-Yu Xiao, Xin-Di Zhao, Tian-Hao Mao 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.00129.pdf)

**💡 相关性分析**

满足标准2：论文提出了一套针对时序信号（CCL波形）的数据增强方法，旨在解决训练数据稀缺的问题。这套系统化的数据预处理和增强流程（如时间缩放、多重采样）作为一种技术资源，对于在数据有限的条件下（例如某些小众化合物的质谱数据）训练用于结构推理或分类的化学信息学/质谱分析模型具有参考和借鉴价值。

**📖 中文摘要**

本文提出了一种用于井下深度传感和验证的数据增强深度学习方法。核心是针对套管接箍定位器（CCL）数据有限的问题，开发了一套综合的数据预处理和增强方法，包括标准化、标签分布平滑、随机裁剪、标签平滑正则化、时间缩放和多重采样。这些方法旨在提高用于识别套管接箍的神经网络的泛化能力。虽然论文主要关注石油天然气领域的特定传感器数据处理，但其核心贡献在于为数据稀缺条件下的神经网络训练提供了一套系统化的数据增强技术。这些技术（如时间缩放、多重采样）在概念上可以迁移到其他时序信号处理领域，例如质谱分析中处理低丰度或噪声信号、构建稳健的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate downhole depth measurement is essential for oil and gas well operations, directly influencing reservoir contact, production efficiency, and operational safety. Collar correlation using a casing collar locator (CCL) is fundamental for precise depth calibration. While neural network has achieved significant progress in collar recognition, preprocessing methods for such applications remain underdeveloped. Moreover, the limited availability of real well data poses substantial challenges for training neural network models that require extensive datasets. This paper presents a system integrated into a downhole toolstring for CCL log acquisition to facilitate dataset construction. Comprehensive preprocessing methods for data augmentation are proposed, and their effectiveness is evaluated using baseline neural network models. Through systematic experimentation across diverse configurations, the contribution of each augmentation method is analyzed. Results demonstrate that standardization, label distribution smoothing, and random cropping are fundamental prerequisites for model training, while label smoothing regularization, time scaling, and multiple sampling significantly enhance model generalization capabilities. Incorporating the proposed augmentation methods into the two baseline models results in maximum F1 score improvements of 0.027 and 0.024 for the TAN and MAN models, respectively. Furthermore, applying these techniques yields F1 score gains of up to 0.045 for the TAN model and 0.057 for the MAN model compared to prior studies. Performance evaluation on real CCL waveforms confirms the effectiveness and practical applicability of our approach. This work addresses the existing gaps in data augmentation methodologies for training casing collar recognition models under CCL data-limited conditions, and provides a technical foundation for the future automation of downhole operations.

</details>

---

### 120. [No-Rank Tensor Decomposition Using Metric Learning](https://arxiv.org/abs/2511.01816)

**基本信息**

- 🔗 arXiv: [`2511.01816`](https://arxiv.org/abs/2511.01816)
- 👥 作者: Maryam Bagherian
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.01816.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的张量分解和表示学习框架（基于度量学习的无秩分解）。该框架专注于从高维数据（如脑连接组、晶体模拟数据）中学习具有物理和语义意义的、可解释的嵌入表示。这种学习稳健、可解释表征的方法本身可以视为一种工具或方法论资源，对于化学信息学中处理高维分子描述符、质谱数据或学习分子表示具有潜在的适用性和启发性。

**📖 中文摘要**

本文提出了一种基于度量学习的无秩张量分解框架。该方法摒弃了传统的基于重建的目标和固定秩约束，转而使用由三元组损失与多样性和均匀性正则化驱动的相似性优化。其目标是学习嵌入表示，使得嵌入空间中的距离能够自然反映数据点之间的语义或物理关系。论文在多个数据集上进行了评估，包括人脸识别、脑连接组和模拟物理系统（星系、晶体）。作者指出，与依赖像素级重建的模型相比，该方法能产生保留物理和语义相关关系的、可解释的嵌入表示，并且在数据稀缺的科学领域中，它提供了一种高效且稳健的替代方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tensor decomposition of high-dimensional data often struggles to capture semantically or physically meaningful structures, particularly when relying on reconstruction objectives and fixed-rank constraints. We introduce a no-rank tensor decomposition framework based on metric learning, which replaces reconstruction objectives with a similarity-driven optimization. By combining a triplet loss with diversity and uniformity regularization, the method learns embeddings where distances naturally reflect semantic and physical relationships, supported by theoretical guarantees on convergence and metric properties. We evaluate the approach on diverse datasets, including face recognition (LFW, Olivetti), brain connectivity (ABIDE), and simulated physical systems (galaxies, crystals). In comprehensive comparisons against classical methods (PCA, t-SNE, UMAP), tensor decompositions (CP, Tucker, t-SVD), and deep learning models (VAE, DEC, transformer based embeddings), our method produces embeddings that preserve physically and semantically relevant relationships and achieve competitive clustering performance. While transformers often excel in predictive accuracy on large datasets, our method provides interpretable embeddings and remains effective in small-data regimes where transformer training may be infeasible. This work establishes metric learning as a principled paradigm for tensor analysis, emphasizing physical interpretability and semantic relevance over pixel-level reconstruction, and offering an efficient and robust alternative in data-scarce scientific domains.

</details>

---

### 121. [Leveraging Discrete Function Decomposability for Scientific Design](https://arxiv.org/abs/2511.03032)

**基本信息**

- 🔗 arXiv: [`2511.03032`](https://arxiv.org/abs/2511.03032)
- 👥 作者: James C. Bowden, Sergey Levine, Jennifer Listgarten
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.03032.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对科学设计（如蛋白质、材料设计）的优化算法。这直接属于“化学大模型”的应用范畴，即利用机器学习模型（特别是生成模型和优化算法）来设计具有目标性质的化学实体（分子、材料）。DADO算法旨在更高效地优化此类生成模型，是化学大模型在逆向设计方向上的相关研究。

**📖 中文摘要**

本文提出了一种名为“分解感知分布优化”（DADO）的新分布优化算法，用于科学设计问题（如设计具有特定性质的蛋白质、材料）。该算法的核心是能够利用设计变量上的可分解性结构（由连接树定义）来使优化更高效。许多科学应用中的性质预测模型具有可分解性，即可以按设计变量进行因子分解。DADO采用软因子化的“搜索分布”（一种学习到的生成模型）来高效导航搜索空间，并利用图消息传递来协调跨链接因子的优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the era of AI-driven science and engineering, we often want to design discrete objects in silico according to user-specified properties. For example, we may wish to design a protein to bind its target, arrange components within a circuit to minimize latency, or find materials with certain properties. Given a property predictive model, in silico design typically involves training a generative model over the design space (e.g., protein sequence space) to concentrate on designs with the desired properties. Distributional optimization$\unicode{x2013}$which can be formalized as an estimation of distribution algorithm or as reinforcement learning policy optimization$\unicode{x2013}$finds the generative model that maximizes an objective function in expectation. Optimizing a distribution over discrete-valued designs is in general challenging because of the combinatorial nature of the design space. However, many property predictors in scientific applications are decomposable in the sense that they can be factorized over design variables in a way that could in principle enable more effective optimization. For example, amino acids at a catalytic site of a protein may only loosely interact with amino acids of the rest of the protein to achieve maximal catalytic activity. Current distributional optimization algorithms are unable to make use of such decomposability structure. Herein, we propose and demonstrate use of a new distributional optimization algorithm, Decomposition-Aware Distributional Optimization (DADO), that can leverage any decomposability defined by a junction tree on the design variables, to make optimization more efficient. At its core, DADO employs a soft-factorized "search distribution"$\unicode{x2013}$a learned generative model$\unicode{x2013}$for efficient navigation of the search space, invoking graph message-passing to coordinate optimization across linked factors.

</details>

---

### 122. [Hard-constraint physics-residual networks enable robust extrapolation for hydrogen crossover prediction in PEM water electrolyzers](https://arxiv.org/abs/2511.05879)

**基本信息**

- 🔗 arXiv: [`2511.05879`](https://arxiv.org/abs/2511.05879)
- 👥 作者: Yong-Woon Kim, Paul D. Yoo, Chan Yeob Yeun 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05879.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的模型架构（硬约束物理残差网络，PR-Net），它将领域知识（物理方程）硬编码为模型主干，让神经网络学习系统偏差。这种融合物理先验与数据驱动学习的方法论，为构建更可靠、可外推的科学模型（包括化学和质谱分析模型）提供了一种强大的工具和框架。例如，在质谱结构推理中，可以嵌入质谱碎裂规则或化学计量约束。

**📖 中文摘要**

本文针对聚合物电解质膜水电解槽中的氢交叉问题，提出了一种硬约束物理残差网络（PR-Net）。该架构将分析传输方程（亨利定律、菲克扩散、法拉第定律）作为确定性的计算主干嵌入，限制神经网络仅学习系统的物理偏差。这种方法本质上解决了纯数据驱动模型和标准物理信息神经网络中的梯度冲突问题，并在训练数据域之外（例如极端压力条件下）实现了出色的外推性能。模型能够以毫秒级速度在边缘硬件上进行推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hydrogen crossover in polymer electrolyte membrane water electrolysis poses a critical safety and efficiency bottleneck for scalable green hydrogen production. While machine learning offers real-time monitoring capabilities, conventional data-driven newral networks (Pure NNs) and soft-constraint physics-informed neural networks (Standard PINNs) suffer from inherent optimization conflicts and fail catastrophically when extrapolating beyond sparse training conditions. Here, we present a hard-constraint physics-residual network (PR-Net) that embeds analytical transport equations -- Henry's law, Fick's diffusion, and Faraday's law -- as a deterministic computational backbone, restricting the neural network to learn only systematic physical deviations. Across 184 experimental points spanning six membrane types and operating conditions of 25--85$^{\circ}$C, 1--200~bar, and 0.05--5.0 A cm$^{-2}$, this architecture intrinsically resolves gradient conflicts, yielding $R^{2} = 99.57 \pm 0.16\%$ with a 39-fold reduction in training variance compared to purely data-driven models ($R^{2} = 96.47 \pm 6.20\%$). Crucially, the PR-Net breaks the extrapolation barrier, maintaining $R^{2} > 97\%$ at extreme cathode pressures up to 200~bar -- a 2.5-fold extrapolation beyond the training domain where Standard PINN severely degrades ($R^{2} = 72.2\%$) and Pure NN collapses ($R^{2} = 58.7\%$). Furthermore, the learned residuals autonomously capture temperature-induced membrane swelling (Spearman's $\rho = 0.506$, $p < 0.001$) and identify the non-linear transport regime transition near 0.23 A cm$^{-2}$, without explicit programming. Delivering millisecond-level inference on edge hardware, the PR-Net establishes a highly reliable, generalizable foundation for adaptive safety control and predictive maintenance in high-pressure electrochemical energy systems.

</details>

---

### 123. [From Efficiency to Adaptivity: A Deeper Look at Adaptive Reasoning in Large Language Models](https://arxiv.org/abs/2511.10788)

**基本信息**

- 🔗 arXiv: [`2511.10788`](https://arxiv.org/abs/2511.10788)
- 👥 作者: Chao Wu, Baoheng Li, Mingchen Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.10788.pdf)

**💡 相关性分析**

满足标准3：论文是一篇专门针对大语言模型（LLMs）推理能力，特别是“自适应推理”这一主题的综述。它系统性地形式化了不同类型的推理，并提出了一个分类法来组织现有的自适应推理方法。这对于理解和设计更高效的“化学大模型”（例如用于分子性质预测、反应条件优化或文献信息提取的LLMs）中的推理机制具有重要的参考和展望价值。

**📖 中文摘要**

本文是一篇关于大语言模型（LLMs）中自适应推理的综述。论文将推理重新置于“适应性”的视角下：即根据输入特征（如难度和不确定性）分配推理努力的能力。作者形式化了演绎、归纳和溯因推理，并将自适应推理形式化为一个控制增强的策略优化问题。论文提出了一个系统的分类法，将现有方法组织为基于训练的方法（通过强化学习、监督微调和学习控制器内化适应性）和免训练的方法（通过提示条件、反馈驱动的停止和模块化组合实现适应性）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have made reasoning a central benchmark for evaluating intelligence. While prior surveys focus on efficiency by examining how to shorten reasoning chains or reduce computation, this view overlooks a fundamental challenge: current LLMs apply uniform reasoning strategies regardless of task complexity, generating long traces for trivial problems while failing to extend reasoning for difficult tasks. This survey reframes reasoning through the lens of {adaptivity}: the capability to allocate reasoning effort based on input characteristics such as difficulty and uncertainty. We make three contributions. First, we formalize deductive, inductive, and abductive reasoning within the LLM context, connecting these classical cognitive paradigms with their algorithmic realizations. Second, we formalize adaptive reasoning as a control-augmented policy optimization problem balancing task performance with computational cost, distinguishing learned policies from inference-time control mechanisms. Third, we propose a systematic taxonomy organizing existing methods into training-based approaches that internalize adaptivity through reinforcement learning, supervised fine-tuning, and learned controllers, and training-free approaches that achieve adaptivity through prompt conditioning, feedback-driven halting, and modular composition. This framework clarifies how different mechanisms realize adaptive reasoning in practice and enables systematic comparison across diverse strategies. We conclude by identifying open challenges in self-evaluation, meta-reasoning, and human-aligned reasoning control.

</details>

---

### 124. [When Data is the Algorithm: A Systematic Study and Curation of Preference Optimization Datasets](https://arxiv.org/abs/2511.10985)

**基本信息**

- 🔗 arXiv: [`2511.10985`](https://arxiv.org/abs/2511.10985)
- 👥 作者: Aladin Djuhera, Farhan Ahmed, Swanand Ravindra Kadhe 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.10985.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是对多个DPO数据集进行系统性分析和比较，并策划发布了一个新的、高质量的偏好优化数据集（UltraMix）。数据是训练和评估大模型（包括化学领域大模型）的基石。这项工作提供了关于偏好数据质量的深入见解和一个经过策划的数据集资源，对于训练用于化学任务（如分子生成偏好、反应条件推荐）的、经过对齐的LLMs具有直接的工具和资源价值。

**📖 中文摘要**

本文对流行的开源直接偏好优化（DPO）数据集进行了首次全面的、以数据为中心的分析。作者利用Magpie框架为每个样本标注任务类别、输入质量和偏好奖励，从而能够跨数据集进行细粒度的偏好质量检查。基于这些分析，作者通过从五个语料库中有选择地抽取样本并去除噪声或冗余样本，系统地策划了一个新的DPO混合数据集UltraMix。实验表明，UltraMix比性能最好的单个数据集小30%，但在关键基准测试中性能更优。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Aligning large language models (LLMs) is a central objective of post-training, often achieved through reward modeling and reinforcement learning methods. Among these, direct preference optimization (DPO) has emerged as a widely adopted technique that fine-tunes LLMs on preferred completions over less favorable ones. While most frontier LLMs do not disclose their curated preference pairs, the broader LLM community has released several open-source DPO datasets, including TuluDPO, ORPO, UltraFeedback, HelpSteer, and Code-Preference-Pairs. However, systematic comparisons remain scarce, largely due to the high computational cost and the lack of rich quality annotations, making it difficult to understand how preferences were selected, which task types they span, and how well they reflect human judgment on a per-sample level. In this work, we present the first comprehensive, data-centric analysis of popular open-source DPO corpora. We leverage the Magpie framework to annotate each sample for task category, input quality, and preference reward, a reward-model-based signal that validates the preference order without relying on human annotations. This enables a scalable, fine-grained inspection of preference quality across datasets, revealing structural and qualitative discrepancies in reward margins. Building on these insights, we systematically curate a new DPO mixture, UltraMix, that draws selectively from all five corpora while removing noisy or redundant samples. UltraMix is 30% smaller than the best-performing individual dataset yet exceeds its performance across key benchmarks. We publicly release all annotations, metadata, and our curated mixture to facilitate future research in data-centric preference optimization.

</details>

---

### 125. [Knowledge Graph Augmented Large Language Models for Disease Prediction](https://arxiv.org/abs/2512.01210)

**基本信息**

- 🔗 arXiv: [`2512.01210`](https://arxiv.org/abs/2512.01210)
- 👥 作者: Ruiyu Wang, Tuan Vinh, Ran Xu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.01210.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用知识图谱增强大语言模型（LLMs）进行疾病预测。这属于“大模型”（具体是LLMs）在科学领域（医疗）的应用。虽然领域是医疗而非化学，但其方法论——将结构化领域知识（KG）与LLMs的推理能力（CoT）相结合——与化学信息学中利用化学知识图谱（如PubChem, ChEBI）来增强LLMs进行分子性质预测、反应推理或文献挖掘的思路高度相关，是化学大模型的一种重要技术路径。

**📖 中文摘要**

本文提出了一种知识图谱（KG）引导的思维链（CoT）框架，用于电子健康记录（EHR）的疾病预测。该方法将ICD-9代码映射到PrimeKG知识图谱，挖掘疾病相关的节点和路径，并利用这些路径来搭建时间上一致的CoT推理依据。然后，使用这些生成的推理链对轻量级指令微调LLMs（如LLaMA-3.1）进行微调，以进行疾病预测。结果表明，该框架在疾病预测任务上表现优异，并且其生成的推理依据在临床医生评估中因清晰度、相关性和正确性而受到青睐。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic health records (EHRs) enable strong clinical prediction, but explanations are often coarse and hard to use for patient-level decisions. We propose a knowledge graph (KG)-guided chain-of-thought (CoT) framework for visit-level disease prediction on MIMIC-III. We map ICD-9 codes to PrimeKG, mine disease-relevant nodes and paths, and use these paths to scaffold temporally consistent CoT rationales, retaining only samples whose conclusions match observed outcomes. We fine-tune lightweight instruction-tuned LLMs (LLaMA-3.1-Instruct-8B and Gemma-7B) on two small cohorts (400 and 1,000 index visits) across ten PrimeKG-mapped diseases. Our models outperform strong classical baselines, reaching AUROC 0.66-0.70 and macro-AUPR 0.40-0.47. Without additional training, the models transfer zero-shot to the CRADLE cohort, improving accuracy from 0.40-0.51 to 0.72-0.77. In a blinded clinician study, KG-guided CoT rationales are consistently preferred for clarity, relevance, and correctness. Code is available at: this https URL

</details>

---

### 126. [Cache What Lasts: Token Retention for Memory-Bounded KV Cache in LLMs](https://arxiv.org/abs/2512.03324)

**基本信息**

- 🔗 arXiv: [`2512.03324`](https://arxiv.org/abs/2512.03324)
- 👥 作者: Ngoc Bui, Shubham Sharma, Simran Lamba 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03324.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种优化大语言模型（LLMs）长上下文推理效率的新方法（TRIM-KV）。高效的长上下文处理是“化学大模型”实际部署的关键挑战之一，例如处理长分子序列（蛋白质、聚合物）、复杂的实验步骤描述或冗长的科学文献。TRIM-KV作为一种提升LLMs在内存受限条件下处理长序列能力的工具和技术，对于构建实用的化学领域大模型具有直接的技术资源价值。

**📖 中文摘要**

本文提出了TRIM-KV，一种用于大语言模型（LLMs）内存受限推理的新方法。该方法通过学习每个token在创建时的内在重要性（通过一个轻量级的保留门），来动态管理不断增长的键值（KV）缓存。当内存预算超出时，分数低的token会被驱逐。TRIM-KV通过从冻结的LLM中进行蒸馏并结合容量损失来高效训练，仅需微调门网络，且增加的开销可忽略不计。该方法在数学推理、长对话记忆和长上下文理解等多项任务中，在低内存状态下 consistently 优于现有的驱逐和可学习检索基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Memory and computation remain core bottlenecks in long-horizon LLM inference due to the quadratic cost of self-attention and the ever-growing key-value (KV) cache. Existing strategies for memory-bounded inference, such as quantization, offloading, or heuristic KV eviction, either incur high orchestration costs or rely on unreliable attention-based proxies of importance. We propose TRIM-KV, a novel approach that learns each token's intrinsic importance at creation time via a lightweight retention gate. Each gate predicts a scalar retention score that decays over time, reflecting the long-term utility of the token for a specific layer and head. Tokens with low scores are evicted when the memory budget is exceeded, ensuring that the cache always contains the most critical tokens. TRIM-KV is trained efficiently through distillation from a frozen LLM combined with a capacity loss, requiring only gate fine-tuning and adding negligible inference overhead. Across mathematical reasoning (GSM8K, MATH-500, AIME24), procedural generation (LongProc), conversational long-memory benchmarks (LongMemEval), and long-context understanding (LongBenchV2 and SCBench), TRIM-KV consistently outperforms strong eviction and learnable retrieval baselines, especially in low-memory regimes. Remarkably, it even surpasses full-cache models in some settings, showing that selective retention can serve as a form of regularization, suppressing noise from uninformative tokens. Qualitative analyses further reveal that learned retention scores align with human intuition, naturally recovering heuristics such as sink tokens, sliding windows, and gist compression without explicit design. Beyond efficiency, retention scores provide insights into layer- and head-specific roles, suggesting a new path toward LLM interpretability.

</details>

---

### 127. [Fourier-Attentive Representation Learning: A Fourier-Guided Framework for Few-Shot Generalization in Vision-Language Models](https://arxiv.org/abs/2512.04395)

**基本信息**

- 🔗 arXiv: [`2512.04395`](https://arxiv.org/abs/2512.04395)
- 👥 作者: Hieu Dinh Trung Pham, Huy Minh Nhat Nguyen, Cuong Tuan Nguyen
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.04395.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的视觉-语言模型（VLM）表征学习框架（FARL），它利用傅里叶分析来解耦图像的结构和风格信息。虽然论文针对通用视觉任务，但这种学习解耦、鲁棒表征的方法论对于化学和质谱分析具有启发性。例如，在质谱分析中，可以借鉴类似思想解耦化合物的核心结构信息（对应相位/结构）和仪器/实验条件带来的变异（对应幅度/风格），从而提升跨平台、跨实验室的质谱结构推理模型的泛化能力。

**📖 中文摘要**

本文提出了傅里叶注意力表征学习（FARL），一种用于视觉-语言模型（VLMs）少样本学习的新框架。该框架通过傅里叶分析显式解耦视觉表征：其核心是一个双重交叉注意力机制，其中可学习的表征token分别查询图像的结构特征（来自相位谱）和风格特征（来自幅度谱）。这个过程产生丰富的、解耦的token，然后被注入到VLM编码器中以指导适应。该方法在15个数据集上的实验证明了其有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large-scale pre-trained Vision-Language Models (VLMs) have demonstrated strong few-shot learning capabilities. However, these methods typically learn holistic representations where an image's domain-invariant structure is implicitly entangled with its domain-specific style. This presents an opportunity to further enhance generalization by disentangling these visual cues. In this paper, we propose Fourier-Attentive Representation Learning (FARL), a novel framework that addresses this by explicitly disentangling visual representations using Fourier analysis. The core of our method is a dual cross-attention mechanism, where learnable representation tokens separately query an image's structural features (from the phase spectrum) and stylistic features (from the amplitude spectrum). This process yields enriched, disentangled tokens that are then injected deep into the VLM encoders to guide adaptation. Our design, which includes an asymmetric injection strategy, forces the model to learn a more robust vision-language alignment. Extensive experiments on 15 datasets demonstrate the effectiveness of our approach.

</details>

---

### 128. [TRINITY: An Evolved LLM Coordinator](https://arxiv.org/abs/2512.04695)

**基本信息**

- 🔗 arXiv: [`2512.04695`](https://arxiv.org/abs/2512.04695)
- 👥 作者: Jinglue Xu, Qi Sun, Peter Schwendeman 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.04695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个用于协调多个大语言模型（LLMs）协作的智能体（Trinity）。这属于“大模型”生态中的高级应用和研究方向，即如何让多个大模型有效协同工作以解决复杂问题。这种多智能体协调框架对于构建复杂的化学研究助手（例如，一个模型负责文献检索，一个负责反应预测，一个负责安全性评估）具有直接的参考价值，是化学大模型系统实现形式的一种探索。

**📖 中文摘要**

本文提出了Trinity，一个轻量级的协调器模型，用于协调多个大语言模型（LLMs）之间的协作。该协调器包括一个紧凑的语言模型（约0.6B参数）和一个轻量级头部（约10K参数），通过进化策略进行优化，以实现高效和自适应的任务委派。Trinity在多轮中处理查询，每轮协调器为选定的LLM分配三个角色（思考者、工作者或验证者）之一，从而将复杂的技能获取卸载给底层的LLMs。实验表明，Trinity在编码、数学、推理和领域知识任务上 consistently 优于单个模型和现有方法，并能稳健地泛化到分布外任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Combining diverse foundation models is promising, but weight-merging is limited by mismatched architectures and closed APIs. Trinity addresses this with a lightweight coordinator that orchestrates collaboration among large language models (LLMs). The coordinator, comprising a compact language model (approximately $0.6$B parameters) and a lightweight head (approximately $10$K parameters), is optimized with an evolutionary strategy for efficient and adaptive delegation. Trinity processes queries over multiple turns, where at each turn the coordinator assigns one of three roles (Thinker, Worker, or Verifier) to a selected LLM, effectively offloading complex skill acquisition from the coordinator itself. Experiments show that Trinity consistently outperforms individual models and existing methods across coding, math, reasoning, and domain knowledge tasks, and generalizes robustly to out-of-distribution tasks. On standard benchmarks, Trinity achieves state-of-the-art results, including a score of 86.2% on LiveCodeBench. Theoretical and empirical analyses identify two main factors behind this performance: (1) the coordinator's hidden-state representations provide rich contextualization of inputs, and (2) under high dimensionality and strict budget constraints, the separable Covariance Matrix Adaptation Evolution Strategy offers advantages over reinforcement learning, imitation learning, and random search by exploiting potential block-epsilon-separability.

</details>

---

### 129. [Optimal transport unlocks end-to-end learning for single-molecule localization](https://arxiv.org/abs/2512.10683)

**基本信息**

- 🔗 arXiv: [`2512.10683`](https://arxiv.org/abs/2512.10683)
- 👥 作者: Romain Seailles, Jean-Baptiste Masson, Jean Ponce 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10683.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于最优传输的端到端深度学习框架，用于解决生物成像中高密度单分子定位的挑战。虽然应用领域是显微镜成像，但其核心技术创新——使用最优传输损失解决密集目标检测中的集合匹配问题，并整合领域知识（光学系统）——为处理其他科学中的密集、噪声信号和复杂空间分布问题提供了强大的方法论工具。在质谱分析中，类似的技术可以用于从复杂的质谱图中精确解析和定位多个共洗脱化合物的碎片离子峰，这对于质谱结构推理至关重要。

**📖 中文摘要**

本文针对单分子定位显微镜（SMLM）中的高密度荧光团定位问题，提出了一种基于最优传输（Optimal Transport）的端到端学习方法。该方法将训练目标重新表述为一个集合匹配问题，推导出一种最优传输损失，从而在推理时消除了对非极大值抑制（NMS）层的需求，并实现了端到端训练。此外，作者还提出了一种迭代神经网络，将显微镜光学系统的知识整合到模型中。在合成基准和真实生物数据上的实验表明，新损失函数和架构在中等和高发射器密度下超越了现有技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-molecule localization microscopy (SMLM) allows reconstructing biology-relevant structures beyond the diffraction limit by detecting and localizing individual fluorophores -- fluorescent molecules stained onto the observed specimen -- over time to reconstruct super-resolved images. Currently, efficient SMLM requires non-overlapping emitting fluorophores, leading to long acquisition times that hinders live-cell imaging. Recent deep-learning approaches can handle denser emissions, but they rely on variants of non-maximum suppression (NMS) layers, which are unfortunately non-differentiable and may discard true positives with their local fusion strategy. In this presentation, we reformulate the SMLM training objective as a set-matching problem, deriving an optimal-transport loss that eliminates the need for NMS during inference and enables end-to-end training. Additionally, we propose an iterative neural network that integrates knowledge of the microscope's optical system inside our model. Experiments on synthetic benchmarks and real biological data show that both our new loss function and architecture surpass the state of the art at moderate and high emitter densities. Code is available at this https URL .

</details>

---

### 130. [The Procedural Semantics Gap in Structured CTI: A Measurement-Driven STIX Analysis for APT Emulation](https://arxiv.org/abs/2512.12078)

**基本信息**

- 🔗 arXiv: [`2512.12078`](https://arxiv.org/abs/2512.12078)
- 👥 作者: Ágney Lopes Roth Ferraz, Sidnei Barbieri, Murray Evangelista de Souza 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.12078.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献在于对一种结构化知识表示（STIX/ATT&CK）进行系统性分析，并提出了一个将其转化为可执行工作流的方法论。这种将高层次、描述性的领域知识转化为机器可操作、可推理步骤的研究，与化学信息学的目标高度相似。例如，将文献中描述的实验步骤（文本）或反应规则（SMARTS）转化为可执行的合成规划或自动化实验指令。这项工作为化学领域如何构建和利用“可执行的知识库”来驱动大模型或自动化系统提供了重要的方法论参考和工具思路。

**📖 中文摘要**

本文对结构化网络威胁情报（CTI，特别是STIX格式和MITRE ATT&CK框架）进行了系统的测量分析，旨在评估其是否包含足够的行为细节以支持多阶段对手模拟。分析发现，当前的CTI标准存在“程序语义鸿沟”：它们描述了对手做什么，但没有详细说明这些行为是如何具体操作化的（例如，顺序、前提条件、环境假设）。为了弥合这一鸿沟，论文引入了一个三阶段方法论，将结构化CTI中的行为信息转化为可执行的步骤，并使必要的环境假设显式化。作者通过实例化MITRE Caldera框架中的操作，展示了该方法的可行性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cyber threat intelligence (CTI) encoded in STIX and structured according to the MITRE ATT&CK framework has become a global reference for describing adversary behavior. However, ATT&CK was designed as a descriptive knowledge base rather than a procedural model. We therefore ask whether its structured artifacts contain sufficient behavioral detail to support multi-stage adversary emulation. Through systematic measurements of the ATT&CK Enterprise bundle, we show that campaign objects encode just fragmented slices of behavior. Only 35.6% of techniques appear in at least one campaign, and neither clustering nor sequence analysis reveals any reusable behavioral structure under technique overlap or LCS-based analyses. Intrusion sets cover a broader portion of the technique space, yet omit the procedural semantics required to transform behavioral knowledge into executable chains, including ordering, preconditions, and environmental assumptions. These findings reveal a procedural semantic gap in current CTI standards: they describe what adversaries do, but not exactly how that behavior was operationalized. To assess how far this gap can be bridged in practice, we introduce a three-stage methodology that translates behavioral information from structured CTI into executable steps and makes the necessary environmental assumptions explicit. We demonstrate its viability by instantiating the resulting steps as operations in the MITRE Caldera framework. Case studies of ShadowRay and Soft Cell show that structured CTI can enable the emulation of multi-stage APT campaigns, but only when analyst-supplied parameters and assumptions are explicitly recorded. This, in turn, exposes the precise points at which current standards fail to support automation. Our results clarify the boundary between descriptive and machine-actionable CTI for adversary emulation.

</details>

---

### 131. [A Single Architecture for Representing Invariance Under Any Space Group](https://arxiv.org/abs/2512.13989)

**基本信息**

- 🔗 arXiv: [`2512.13989`](https://arxiv.org/abs/2512.13989)
- 👥 作者: Cindy Y. Zhang, Elif Ertekin, Peter Orbanz 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.13989.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种创新的、统一的神经网络架构，能够通过编码对称性约束（空间群）来学习对晶体材料的不变表示。对称性是化学和材料科学的核心。这种能够自动适应并强制执行复杂化学对称性（如点群、空间群）的通用架构，是构建下一代化学和材料科学大模型的关键技术工具。它为解决化学结构（分子、晶体）表示学习中的对称性难题提供了强大的框架资源。

**📖 中文摘要**

本文提出了一种新的机器学习架构，能够自动调整其权重以强制实现对任何输入空间群（共230个）的不变性。该方法基于通过对傅里叶系数施加群操作所蕴含的约束来构建对称适应的傅里叶基。将这些约束编码到神经网络层中，可以实现不同空间群之间的权重共享，使模型能够利用群之间的结构相似性，并在特定群的数据稀缺时克服数据稀疏性问题。作者在材料性能预测任务上展示了该方法的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Incorporating known symmetries in data into machine learning models has consistently improved predictive accuracy, robustness, and generalization. However, achieving exact invariance to specific symmetries typically requires designing bespoke architectures for each group, limiting scalability and preventing knowledge transfer across related symmetries. In the case of the space groups, symmetries critical to modeling crystalline solids in materials science and condensed matter physics, this challenge is particularly salient as there are 230 such groups in three dimensions. In this work we present a new approach to such crystallographic symmetries by developing a single machine learning architecture that is capable of adapting its weights automatically to enforce invariance to any input space group. Our approach is based on constructing symmetry-adapted Fourier bases through an explicit characterization of constraints that group operations impose on Fourier coefficients. Encoding these constraints into a neural network layer enables weight sharing across different space groups, allowing the model to leverage structural similarities between groups and overcome data sparsity when limited measurements are available for specific groups. We demonstrate the effectiveness of this approach in achieving competitive performance on material property prediction tasks and performing zero-shot learning to generalize to unseen groups.

</details>

---

## 📊 数据统计
- 累计运行天数：7
- 累计论文数量：403

## 📝 历史记录

> 暂无历史数据

