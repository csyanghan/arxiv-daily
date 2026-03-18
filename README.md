# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-18 13:16:35

## 📅 2026-03-18 (今日最新)

**相关论文数：78**

### 1. [Finder: A Multimodal AI-Powered Search Framework for Pharmaceutical Data Retrieval](https://arxiv.org/abs/2603.15623)

**基本信息**

- 🔗 arXiv: [`2603.15623`](https://arxiv.org/abs/2603.15623)
- 👥 作者: Suyash Mishra, Srikanth Patil, Satyanarayan Pati 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15623.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个可扩展的、AI驱动的多模态数据检索框架（Finder），该框架能够处理文本、图像、音频和视频。虽然其应用场景是制药数据，但其核心技术和架构（如混合向量搜索、多模态内容处理、推理感知搜索）为化学信息学和质谱分析领域构建或增强数据资源、工具和知识发现系统提供了直接相关的技术方案和思路。

**📖 中文摘要**

本文介绍了Finder，一个用于药物数据检索的多模态AI搜索框架。该系统旨在解决传统系统在处理多模态内容（文本、图像、音频、视频）和手动管理方面的困难。Finder采用混合向量搜索（结合稀疏词法和密集语义模型）来统一跨模态检索。其模块化流程可以处理多种格式的数据，丰富元数据，并将内容存储在向量原生后端中。该系统支持基于推理的自然语言搜索，以提高精度和上下文相关性。Finder已处理超过291,400份文档、31,070个视频和1,192个音频文件，涵盖98种语言。虽然论文主要聚焦于制药信息检索的通用框架，但其核心——多模态AI驱动的数据检索和知识发现——与化学信息学中利用AI处理和分析复杂化学数据（如文献、光谱、分子结构）的目标高度相关。该系统提供的工具和框架思路，可用于构建或增强化学领域（如质谱数据库、分子性质库）的专用检索和分析系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming pharmaceutical search, where traditional systems struggle with multimodal content and manual curation. Finder is a scalable AI-powered framework that unifies retrieval across text, images, audio, and video using hybrid vector search, combining sparse lexical and dense semantic models. Its modular pipeline ingests diverse formats, enriches metadata, and stores content in a vector-native backend. Finder supports reasoning-aware natural language search, improving precision and contextual relevance. The system has processed over 291,400 documents, 31,070 videos, and 1,192 audio files in 98 languages. Techniques like hybrid fusion, chunking, and metadata-aware routing enable intelligent access across regulatory, research, and commercial domains.

</details>

---

### 2. [Tokenization Tradeoffs in Structured EHR Foundation Models](https://arxiv.org/abs/2603.15644)

**基本信息**

- 🔗 arXiv: [`2603.15644`](https://arxiv.org/abs/2603.15644)
- 👥 作者: Lin Lawrence Guo, Santiago Eduardo Arciniegas, Joseph Jihyung Lee 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15644.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是基础模型的标记化策略，这是构建和处理大规模、结构化序列数据（如EHR时间线）的关键技术。虽然应用领域是医疗，但其中研究的“标记化”问题——如何将复杂的、带有时序和属性的结构化数据有效地编码为模型输入——与化学信息学和质谱分析中处理分子序列、质谱峰列表或色谱-质谱联用数据流等时序/结构化数据的核心挑战直接相关。论文为化学领域构建用于分子性质预测、反应预测或质谱解析的序列模型提供了重要的方法论参考。

**📖 中文摘要**

本文研究了结构化电子健康记录（EHR）基础模型中的标记化（Tokenization）权衡。标记化决定了时间戳临床事件序列如何被转换为离散的模型输入，从而影响信息的保留、编码效率以及模型需要学习的关系。论文通过因子设计预训练了一个基于儿科EHR数据的Transformer模型，评估了事件编码、时间编码和工作流注释等不同标记化策略对下游74项临床预测任务性能的影响。研究发现，联合事件编码和位置时间编码在大多数任务中表现最优，同时显著减少了预训练所需的浮点运算次数。外部评估表明，这种优势可以推广到成人ICU队列。论文的核心贡献在于系统性地评估了标记化设计选择对EHR基础模型性能和效率的影响，并确立了标记化作为改进模型的一个可操作性杠杆。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models for structured electronic health records (EHRs) are pretrained on longitudinal sequences of timestamped clinical events to learn adaptable patient representations. Tokenization -- how these timelines are converted into discrete model inputs -- determines what information is preserved, how efficiently it is encoded, and which relationships must be learned versus precomputed. Yet the impact of tokenization design choices on downstream performance and computational efficiency remains largely unexplored. Here, we pretrained a transformer on pediatric EHR data under a factorial design, varying tokenization along event encoding, time encoding, and workflow annotation. We evaluated area-under-the-receiver-operating-characteristic curve across 74 clinical prediction tasks. Joint event encoding and positional time encoding outperformed their alternatives (73/74 and 71/74 tasks) while requiring 39.5% and 9.6% fewer pretraining floating-point operations, respectively. Targeted ablations traced the joint encoding advantage to local binding efficiency, that is, code-attribute pairs are combined into single tokens, rather than split across tokens that the model must learn to associate during pretraining. External evaluation on an adult intensive care unit cohort demonstrated that this advantage generalizes despite substantial vocabulary mismatch, while temporal and workflow effects remain institution-specific. These results establish tokenization as a tractable lever for improving both the performance and efficiency of EHR foundation models.

</details>

---

### 3. [A Dynamic Survey of Fuzzy, Intuitionistic Fuzzy, Neutrosophic, Plithogenic, and Extensional Sets](https://arxiv.org/abs/2603.15667)

**基本信息**

- 🔗 arXiv: [`2603.15667`](https://arxiv.org/abs/2603.15667)
- 👥 作者: Takaaki Fujita, Florentin Smarandache
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15667.pdf)

**💡 相关性分析**

满足标准3：论文是一篇专门针对模糊集、直觉模糊集、中智集、泛生集等不确定性建模理论的综述。这些数学框架是处理化学信息学和质谱分析中常见不确定性的重要工具，例如在分子相似性计算、谱图匹配置信度评估、多源数据融合、以及基于不完整或噪声数据的结构推理中。这篇综述为相关领域的研究者提供了系统的理论概览和未来研究方向，属于重要的相关讨论和展望。

**📖 中文摘要**

本文是一篇关于模糊集、直觉模糊集、中智集、泛生集及其扩展集的动态综述。现实世界现象常常表现出模糊性、部分真实性和信息不完全性。为了以数学上严谨的方式对这种不确定性进行建模，引入了许多广义的集合论框架。本文对模糊集、直觉模糊集、中智集和泛生集这四大不确定性导向模型家族进行了全面、大规模的综述。目标是让读者系统地了解现有发展，并通过统一的阐述，激发跨学科的新见解、进一步的概念扩展和额外的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real-world phenomena often exhibit vagueness, partial truth, and incomplete information. To model such uncertainty in a mathematically rigorous way, many generalized set-theoretic frameworks have been introduced, including Fuzzy Sets [1], Intuitionistic Fuzzy Sets [2], Neutrosophic Sets [3,4], Vague Sets [5], Hesitant Fuzzy Sets [6], Picture Fuzzy Sets [7], Quadripartitioned Neutrosophic Sets [8], Penta-Partitioned Neutrosophic Sets [9], Plithogenic Sets [10], HyperFuzzy Sets [11], and HyperNeutrosophic Sets [12]. Within these frameworks, a wide range of notions has been proposed and studied, particularly in the settings of fuzzy, intuitionistic fuzzy, neutrosophic, and plithogenic set theories. This extensive literature underscores both the significance of these theories and the breadth of their application areas. As a result, many ideas, constructions, and structural patterns recur across these four major families of uncertainty-oriented models. In this book, we provide a comprehensive, large-scale survey of Fuzzy, Intuitionistic Fuzzy, Neutrosophic, and Plithogenic Sets. Our goal is to give readers a systematic overview of existing developments and, through a unified exposition, to stimulate new insights, further conceptual extensions, and additional applications across a wide range of disciplines.

</details>

---

### 4. [Survey of Various Fuzzy and Uncertain Decision-Making Methods](https://arxiv.org/abs/2603.15709)

**基本信息**

- 🔗 arXiv: [`2603.15709`](https://arxiv.org/abs/2603.15709)
- 👥 作者: Takaaki Fujita, Florentin Smarandache
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15709.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于模糊和不确定决策方法的综述。在化学信息学和质谱分析中，决策过程无处不在，例如基于多源信息的化合物鉴定、实验条件优化、候选分子筛选等，这些过程常常涉及不精确、不完整或冲突的数据。该综述系统梳理了相关的决策理论和方法，为化学领域处理类似问题提供了重要的方法论参考和理论框架，属于重要的相关讨论。

**📖 中文摘要**

本文综述了各种模糊和不确定决策方法。现实应用中的决策常常受到模糊性、信息不完全、异构数据和冲突专家意见的影响。本综述回顾了不确定性感知的多准则决策（MCDM），并将其组织成一个简洁的、面向任务的分类法。总结了问题层面的设置、权重分配、标准间结构和因果关系建模。对于求解过程，对比了补偿性评分方法、到参考点的距离和折衷方法，以及用于排序或分类的非补偿性优劣排序框架。还概述了产生可解释规则或策略的规则/证据基础和序列决策模型。综述强调了典型的输入、核心计算步骤和主要输出，并根据鲁棒性、可解释性和数据可用性提供了选择方法的指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Decision-making in real applications is often affected by vagueness, incomplete information, heterogeneous data, and conflicting expert opinions. This survey reviews uncertainty-aware multi-criteria decision-making (MCDM) and organizes the field into a concise, task-oriented taxonomy. We summarize problem-level settings (discrete, group/consensus, dynamic, multi-stage, multi-level, multiagent, and multi-scenario), weight elicitation (subjective and objective schemes under fuzzy/linguistic inputs), and inter-criteria structure and causality modelling. For solution procedures, we contrast compensatory scoring methods, distance-to-reference and compromise approaches, and non-compensatory outranking frameworks for ranking or sorting. We also outline rule/evidence-based and sequential decision models that produce interpretable rules or policies. The survey highlights typical inputs, core computational steps, and primary outputs, and provides guidance on choosing methods according to robustness, interpretability, and data availability. It concludes with open directions on explainable uncertainty integration, stability, and scalability in large-scale and dynamic decision environments.

</details>

---

### 5. [Knowledge Graph Extraction from Biomedical Literature for Alkaptonuria Rare Disease](https://arxiv.org/abs/2603.15711)

**基本信息**

- 🔗 arXiv: [`2603.15711`](https://arxiv.org/abs/2603.15711)
- 👥 作者: Giang Pham, Rebecca Finetti, Caterina Graziani 等15人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15711.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种从生物医学文献中大规模提取关系以构建知识图谱的方法论和流程。虽然应用案例是特定疾病，但其核心技术——基于文本挖掘的生物医学知识图谱自动构建——为化学信息学和质谱分析领域提供了直接可用的数据资源构建工具和范例。该方法可用于从化学文献中自动提取化合物-性质、反应-条件、谱图-结构等关系，构建领域专用的知识图谱，服务于化学大模型训练或质谱结构推理。

**📖 中文摘要**

本文提出了一种从生物医学文献中提取知识图谱（KG）的方法，并将其应用于罕见病尿黑酸尿症（AKU）。AKU是一种超罕见疾病，相关数据有限。知识图谱可以帮助连接关于该疾病的有限知识（基本机制、表现和现有疗法）与其他知识。本文应用了一种基于PubTator3的大规模生物医学关系文本挖掘方法。构建了两个不同大小的知识图谱，使用现有生化知识进行验证，并利用它们提取可能与AKU相关的基因、疾病和疗法。该计算框架揭示了疾病的系统相互作用、其共病和潜在治疗靶点，证明了该方法在分析罕见代谢疾病方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Alkaptonuria (AKU) is an ultra-rare autosomal recessive metabolic disorder caused by mutations in the HGD (Homogentisate 1,2-Dioxygenase) gene, leading to a pathological accumulation of homogentisic acid (HGA) in body fluids and tissues. This leads to systemic manifestations, including premature spondyloarthropathy, renal and prostatic stones, and cardiovascular complications. Being ultra-rare, the amount of data related to the disease is limited, both in terms of clinical data and literature. Knowledge graphs (KGs) can help connect the limited knowledge about the disease (basic mechanisms, manifestations and existing therapies) with other knowledge; however, AKU is frequently underrepresented or entirely absent in existing biomedical KGs. In this work, we apply a text-mining methodology based on PubTator3 for large-scale extraction of biomedical relations. We construct two KGs of different sizes, validate them using existing biochemical knowledge and use them to extract genes, diseases and therapies possibly related to AKU. This computational framework reveals the systemic interactions of the disease, its comorbidities, and potential therapeutic targets, demonstrating the efficacy of our approach in analyzing rare metabolic disorders.

</details>

---

### 6. [A Framework and Prototype for a Navigable Map of Datasets in Engineering Design and Systems Engineering](https://arxiv.org/abs/2603.15722)

**基本信息**

- 🔗 arXiv: [`2603.15722`](https://arxiv.org/abs/2603.15722)
- 👥 作者: H. Sinan Bank, Daniel R. Herber
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15722.pdf)

**💡 相关性分析**

满足标准2：论文的核心是提出一个用于组织、分类和发现工程数据集的系统框架和原型工具。虽然应用领域是工程设计，但其解决的核心问题——数据集的碎片化、难以发现和访问——在化学信息学和质谱分析领域同样突出且关键。该论文提出的框架（多维分类法、知识图谱模型、交互式发现工具）为化学领域构建一个类似的、统一的质谱数据集、分子数据集或计算化学数据集导航平台提供了直接相关的设计思路、架构参考和技术方案。

**📖 中文摘要**

本文提出了一个用于工程设计与系统工程（EDSE）中数据集导航地图的框架和原型。系统生命周期中数据的激增为EDSE带来了重大机遇和挑战。虽然“数字主线”有潜力推动创新，但现有数据集的碎片化和难以获取性阻碍了方法验证、限制了可重复性并减缓了研究进展。与计算机视觉和自然语言处理等领域不同，工程设计研究通常依赖于小型、专有或临时数据集。本文通过提出一个“EDSE数据集地图”的系统框架来解决这一挑战。该框架建立在一个多维分类法之上，旨在通过领域、生命周期阶段、数据类型和格式对工程数据集进行分类，实现分面发现。详细介绍了交互式发现工具的架构，并通过一个工作原型进行了演示，该原型采用知识图谱数据模型来捕获数据集、工具和出版物之间丰富的语义关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The proliferation of data across the system lifecycle presents both a significant opportunity and a challenge for Engineering Design and Systems Engineering (EDSE). While this ``digital thread'' has the potential to drive innovation, the fragmented and inaccessible nature of existing datasets hinders method validation, limits reproducibility, and slows research progress. Unlike fields such as computer vision and natural language processing, which benefit from established benchmark ecosystems, engineering design research often relies on small, proprietary, or ad-hoc datasets. This paper addresses this challenge by proposing a systematic framework for a ``Map of Datasets in EDSE.'' The framework is built upon a multi-dimensional taxonomy designed to classify engineering datasets by domain, lifecycle stage, data type, and format, enabling faceted discovery. An architecture for an interactive discovery tool is detailed and demonstrated through a working prototype, employing a knowledge graph data model to capture rich semantic relationships between datasets, tools, and publications. An analysis of the current data landscape reveals underrepresented areas (``data deserts'') in early-stage design and system architecture, as well as relatively well-represented areas (``data oases'') in predictive maintenance and autonomous systems. The paper identifies key challenges in curation and sustainability and proposes mitigation strategies, laying the groundwork for a dynamic, community-driven resource to accelerate data-centric engineering research.

</details>

---

### 7. [Informationally Compressive Anonymization: Non-Degrading Sensitive Input Protection for Privacy-Preserving Supervised Machine Learning](https://arxiv.org/abs/2603.15842)

**基本信息**

- 🔗 arXiv: [`2603.15842`](https://arxiv.org/abs/2603.15842)
- 👥 作者: Jeremy J Samuelson
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15842.pdf)

**💡 相关性分析**

满足标准1：论文提出的信息压缩匿名化（ICA）框架，其核心思想是通过编码器学习任务对齐的潜在表示，这与化学信息学中构建分子表示、质谱数据分析中提取特征表示的核心方法论直接相关，为相关主题提供了重要的技术思路。

**📖 中文摘要**

这篇论文提出了信息压缩匿名化（ICA）和VEIL架构，这是一种隐私保护机器学习框架。虽然其核心主题是隐私保护机器学习，而非直接的化学大模型或质谱结构推理，但它提出了一种通过监督、多目标编码器将原始输入转换为低维、任务对齐的潜在表示的方法。这种将复杂输入（如原始数据）编码为紧凑、信息丰富的潜在向量的思想，与化学信息学中构建分子表示或质谱数据降维与特征提取的核心任务在方法论上高度相关。论文中关于“任务对齐的潜在表示”和“结构不可逆性”的讨论，为如何从高维化学或质谱数据中学习稳健、可解释的表示提供了重要的技术思路和理论框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern machine learning systems increasingly rely on sensitive data, creating significant privacy, security, and regulatory risks that existing privacy-preserving machine learning (ppML) techniques, such as Differential Privacy (DP) and Homomorphic Encryption (HE), address only at the cost of degraded performance, increased complexity, or prohibitive computational overhead. This paper introduces Informationally Compressive Anonymization (ICA) and the VEIL architecture, a privacy-preserving ML framework that achieves strong privacy guarantees through architectural and mathematical design rather than noise injection or cryptography. ICA embeds a supervised, multi-objective encoder within a trusted Source Environment to transform raw inputs into low-dimensional, task-aligned latent representations, ensuring that only irreversibly anonymized vectors are exported to untrusted Training and Inference Environments. The paper rigorously proves that these encodings are structurally non-invertible using topological and information-theoretic arguments, showing that inversion is logically impossible, even under idealized attacker assumptions, and that, in realistic deployments, the attackers conditional entropy over the original data diverges, driving reconstruction probability to zero. Unlike prior autoencoder-based ppML approaches, ICA preserves predictive utility by aligning representation learning with downstream supervised objectives, enabling low-latency, high-performance ML without gradient clipping, noise budgets, or encryption at inference time. The VEIL architecture enforces strict trust boundaries, supports scalable multi-region deployment, and naturally aligns with privacy-by-design regulatory frameworks, establishing a new foundation for enterprise ML that is secure, performant, and safe by construction, even in the face of post-quantum threats.

</details>

---

### 8. [INSTRUMENTAL: Automatic Synthesizer Parameter Recovery from Audio via Evolutionary Optimization](https://arxiv.org/abs/2603.15905)

**基本信息**

- 🔗 arXiv: [`2603.15905`](https://arxiv.org/abs/2603.15905)
- 👥 作者: Philipp Bogdan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15905.pdf)

**💡 相关性分析**

满足标准1：论文的核心是从观测数据（音频）中逆向推断生成参数（合成器设置），这与“质谱结构推理”从质谱数据推断分子结构的逆向问题在方法论上完全同构，提供了直接相关的技术思路和算法框架。

**📖 中文摘要**

这篇论文提出了INSTRUMENTAL系统，旨在从音频中恢复合成器的连续参数。它通过将可微分的减法合成器与无导数进化优化器（CMA-ES）耦合来实现。虽然应用领域是音频合成，但其核心方法论——使用可微分模型结合优化算法从观测数据（音频）中反推生成该数据的底层参数（合成器参数）——与“质谱结构推理”问题在数学和计算范式上高度一致。质谱结构推理的目标是从观测到的质谱数据中推断出产生该谱图的分子结构及其参数，这同样是一个复杂的逆向问题。论文中评估的优化策略、损失函数设计以及对非凸景观的处理，为质谱数据的逆向解析提供了直接可借鉴的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing audio-to-MIDI tools extract notes but discard the timbral characteristics that define an instrument's identity. We present Instrumental, a system that recovers continuous synthesizer parameters from audio by coupling a differentiable 28-parameter subtractive synthesizer with CMA-ES, a derivative-free evolutionary optimizer. We optimize a composite perceptual loss combining mel-scaled STFT, spectral centroid, and MFCC divergence, achieving a matching loss of 2.09 on real recorded audio. We systematically evaluate eight hypotheses for improving convergence and find that only parametric EQ boosting yields meaningful improvement. Our results show that CMA-ES outperforms gradient descent on this non-convex landscape, that more parameters do not monotonically improve matching, and that spectral analysis initialization accelerates convergence over random starts.

</details>

---

### 9. [Bayesian-guided inverse design of hyperelastic microstructures: Application to stochastic metamaterials](https://arxiv.org/abs/2603.15917)

**基本信息**

- 🔗 arXiv: [`2603.15917`](https://arxiv.org/abs/2603.15917)
- 👥 作者: Hooman Danesh, Henning Wessels
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15917.pdf)

**💡 相关性分析**

满足标准1：论文提出的贝叶斯引导逆向设计框架，其核心方法（主动学习、代理模型、高维空间搜索）直接适用于“化学大模型”相关的逆向分子设计问题，以及“质谱结构推理”中的候选结构搜索与匹配问题。

**📖 中文摘要**

这篇论文提出了一个贝叶斯引导的逆向设计框架，用于从大量候选结构中识别出具有目标宏观应力响应的超弹性微结构。其核心是结合降维、主动学习和高斯过程代理模型，在有限的高保真度评估（计算或实验）预算下，高效地搜索设计空间。这种方法论与“化学大模型”和“质谱结构推理”中的关键挑战高度相关：1）在化学信息学中，逆向分子设计（给定目标性质寻找分子）面临类似的组合爆炸和昂贵评估问题；2）在质谱分析中，从谱图库中匹配或生成候选结构也是一个高维逆向搜索问题。论文提出的基于代理模型的主动学习框架和贝叶斯优化策略，为这些领域的数据高效逆向设计提供了强大的通用工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

From a given pool of all feasible design variants, our aim is to identify a structure that achieves a target macroscopic stress response. For each candidate design, the response is obtained from a high-fidelity oracle, in particular, time- and resource-intensive computational homogenization or experiments. We consider the case where (i) the geometry cannot be conveniently parameterized, rendering gradient-based optimization inapplicable, and (ii) brute-force evaluation of all candidates is infeasible due to the cost of oracle queries. To tackle this challenge, we propose a Bayesian-guided inverse design framework that proceeds as follows. First, the dimensionality of the design variants is reduced through statistical feature engineering, and the resulting low-dimensional descriptors are mapped to effective constitutive parameters describing the macroscopic hyperelastic response. This mapping is modeled using a multi-output Gaussian process surrogate that accounts for correlations between the parameters. The surrogate is trained using uncertainty-driven active learning under severe budget constraints, allowing only a very limited number of high-fidelity oracle evaluations. Based on surrogate predictions, a finite number of promising candidates are shortlisted. Since the surrogate accuracy is inherently limited, the final selection of the optimal design is performed through high-fidelity oracle evaluations within the shortlist. In numerical test cases, we consider a dataset of 50,000 candidate structures. Active learning requires labeling less than half a percent of the full dataset. Bayesian-guided inverse design under unseen loading conditions reaches a prescribed error threshold with only a handful of oracle evaluations in the majority of cases.

</details>

---

### 10. [Generative Inverse Design with Abstention via Diagonal Flow Matching](https://arxiv.org/abs/2603.15925)

**基本信息**

- 🔗 arXiv: [`2603.15925`](https://arxiv.org/abs/2603.15925)
- 👥 作者: Miguel de Campos, Werner Krebs, Hanno Gottschalk
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15925.pdf)

**💡 相关性分析**

满足标准1：论文专注于生成式逆向设计，提出了用于学习设计-性能双向映射的Diag-CFM方法，这与“化学大模型”中的生成式分子设计以及“质谱结构推理”中的谱图到结构的生成任务在核心目标和方法论上直接相关。

**📖 中文摘要**

这篇论文专注于逆向设计问题，旨在寻找实现目标性能的设计参数。它引入了对角流匹配（Diag-CFM）方法，这是一种生成式方法，用于学习设计与标签之间的双向映射，从而能够对多样化解决方案进行采样。论文解决了标准条件流匹配（CFM）在应用于逆向问题时的不稳定性，并提出了架构内在的不确定性度量。这项工作与“化学大模型”和“质谱结构推理”高度相关：1）在化学领域，生成式逆向分子设计是一个核心课题，需要模型能够从目标性质生成多样的分子结构；2）在质谱领域，从谱图生成或检索候选分子结构也是一个生成式逆向任务。论文提出的生成式逆向设计框架、稳定性改进方法以及不确定性量化技术，为这些化学信息学任务提供了先进的建模工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse design aims to find design parameters $x$ achieving target performance $y^*$. Generative approaches learn bidirectional mappings between designs and labels, enabling diverse solution sampling. However, standard conditional flow matching (CFM), when adapted to inverse problems by pairing labels with design parameters, exhibits strong sensitivity to their arbitrary ordering and scaling, leading to unstable training. We introduce Diagonal Flow Matching (Diag-CFM), which resolves this through a zero-anchoring strategy that pairs design coordinates with noise and labels with zero, making the learning problem provably invariant to coordinate permutations. This yields order-of-magnitude improvements in round-trip accuracy over CFM and invertible neural network baselines across design dimensions up to $P{=}100$. We develop two architecture-intrinsic uncertainty metrics, Zero-Deviation and Self-Consistency, that enable three practical capabilities: selecting the best candidate among multiple generations, abstaining from unreliable predictions, and detecting out-of-distribution targets; consistently outperforming ensemble and general-purpose alternatives across all tasks. We validate on airfoil, gas turbine combustor, and an analytical benchmark with scalable design dimension.

</details>

---

### 11. [Discovery of interaction and diffusion kernels in particle-to-mean-field multi-agent systems](https://arxiv.org/abs/2603.15927)

**基本信息**

- 🔗 arXiv: [`2603.15927`](https://arxiv.org/abs/2603.15927)
- 👥 作者: Giacomo Albi, Alessandro Alla, Elisa Calzola
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15927.pdf)

**💡 相关性分析**

满足标准1：论文提出了从系统轨迹数据中学习交互核的通用框架，这与化学中从分子动力学轨迹学习力场、或质谱中从碎裂数据推断反应规律等逆问题在方法论上高度相关，为核心主题提供了数据驱动的发现工具。

**📖 中文摘要**

这篇论文提出了一个数据驱动框架，用于从轨迹数据中学习随机多智能体系统中的交互核。其目标是在没有底层交互结构先验知识的情况下，直接从数据中识别非局部交互和扩散项的函数形式。该方法将逆问题表述为一系列稀疏回归任务。这项工作与“化学大模型”和“质谱结构推理”具有潜在相关性：1）在化学领域，分子动力学模拟产生粒子轨迹，从中学习粒子间相互作用势（力场）是一个核心的逆问题，与本论文的框架类似；2）在质谱解析中，理解分子碎裂动力学（一种“交互”过程）以从谱图反推结构，也涉及从数据中学习规律。论文提出的从轨迹数据中发现交互规律的方法论，为化学和质谱中类似的从观测数据推断底层物理/化学规律的问题提供了通用的计算框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a data-driven framework to learn interaction kernels in stochastic multi-agent systems. Our approach aims at identifying the functional form of nonlocal interaction and diffusion terms directly from trajectory data, without any a priori knowledge of the underlying interaction structure. Starting from a discrete stochastic binary-interaction model, we formulate the inverse problem as a sequence of sparse regression tasks in structured finite-dimensional spaces spanned by compactly supported basis functions, such as piecewise linear polynomials. In particular, we assume that pairwise interactions between agents are not directly observed and that only limited trajectory data are available. To address these challenges, we propose two complementary identification strategies. The first based on random-batch sampling, which compensates for latent interactions while preserving the statistical structure of the full dynamics in expectation. The second based on a mean-field approximation, where the empirical particle density reconstructed from the data defines a continuous nonlocal regression problem. Numerical experiments demonstrate the effectiveness and robustness of the proposed framework, showing accurate reconstruction of both interaction and diffusion kernels even from partially observed. The method is validated on benchmark models, including bounded-confidence and attraction-repulsion dynamics, where the two proposed strategies achieve comparable levels of accuracy.

</details>

---

### 12. [Nodule-Aligned Latent Space Learning with LLM-Driven Multimodal Diffusion for Lung Nodule Progression Prediction](https://arxiv.org/abs/2603.15932)

**基本信息**

- 🔗 arXiv: [`2603.15932`](https://arxiv.org/abs/2603.15932)
- 👥 作者: James Song, Yifan Wang, Chuan Zhou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15932.pdf)

**💡 相关性分析**

满足标准1：论文提出的“结节对齐潜在空间”和LLM驱动的多模态条件生成方法，与“化学大模型”中构建连续分子表示空间、进行条件分子生成的核心任务直接相关。其扩散模型框架也是化学生成模型的主流技术之一。

**📖 中文摘要**

这篇论文提出了NAMD框架，用于通过生成一年后的随访结节CT图像来预测肺结节进展。其核心创新是引入了结节对齐的潜在空间，并利用LLM驱动的控制机制来调节扩散模型。虽然应用领域是医学影像，但其方法论与“化学大模型”和“质谱结构推理”有深刻联系：1）“结节对齐的潜在空间”概念，即潜在空间中的距离直接对应属性变化，这与化学中构建分子连续表示空间（如化学空间）以进行属性预测和分子生成的目标一致；2）使用LLM整合多模态患者数据（EHR）来调节生成过程，这与用自然语言或结构化信息指导分子生成或质谱解析的思路类似；3）扩散模型本身是强大的生成模型，在分子和材料设计中有广泛应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early diagnosis of lung cancer is challenging due to biological uncertainty and the limited understanding of the biological mechanisms driving nodule progression. To address this, we propose Nodule-Aligned Multimodal (Latent) Diffusion (NAMD), a novel framework that predicts lung nodule progression by generating 1-year follow-up nodule computed tomography images with baseline scans and the patient's and nodule's Electronic Health Record (EHR). NAMD introduces a nodule-aligned latent space, where distances between latents directly correspond to changes in nodule attributes, and utilizes an LLM-driven control mechanism to condition the diffusion backbone on patient data. On the National Lung Screening Trial (NLST) dataset, our method synthesizes follow-up nodule images that achieve an AUROC of 0.805 and an AUPRC of 0.346 for lung nodule malignancy prediction, significantly outperforming both baseline scans and state-of-the-art synthesis methods, while closely approaching the performance of real follow-up scans (AUROC: 0.819, AUPRC: 0.393). These results demonstrate that NAMD captures clinically relevant features of lung nodule progression, facilitating earlier and more accurate diagnosis.

</details>

---

### 13. [Data-Local Autonomous LLM-Guided Neural Architecture Search for Multiclass Multimodal Time-Series Classification](https://arxiv.org/abs/2603.15939)

**基本信息**

- 🔗 arXiv: [`2603.15939`](https://arxiv.org/abs/2603.15939)
- 👥 作者: Emil Hardarson, Luka Biedebach, Ómar Bessi Ómarsson 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15939.pdf)

**💡 相关性分析**

满足标准1：论文提出的LLM引导的神经架构搜索（NAS）框架，其自动化机器学习（AutoML）方法论直接适用于“化学大模型”的构建过程，可以帮助自动化地设计和优化用于分子表示学习、性质预测或质谱分析的神经网络架构。

**📖 中文摘要**

这篇论文提出了一个数据本地的、LLM引导的神经架构搜索（NAS）框架，用于多类别多模态时间序列分类。该框架在数据隐私约束下（如医疗数据），远程处理候选管道描述，而所有训练和评估都在本地执行。虽然应用场景是时间序列分类，但其核心方法——LLM引导的自动化机器学习（AutoML）和神经架构搜索——与“化学大模型”的构建和优化高度相关。在化学信息学中，设计用于分子性质预测、反应结果预测或谱图分析的神经网络架构本身就是一个复杂任务。本论文提供的LLM引导的、考虑多模态融合和预处理步骤的自动化搜索框架，为化学领域定制和优化专用模型架构提供了一个强有力的、可迁移的自动化工具链范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Applying machine learning to sensitive time-series data is often bottlenecked by the iteration loop: Performance depends strongly on preprocessing and architecture, yet training often has to run on-premise under strict data-local constraints. This is a common problem in healthcare and other privacy-constrained domains (e.g., a hospital developing deep learning models on patient EEG). This bottleneck is particularly challenging in multimodal fusion, where sensor modalities must be individually preprocessed and then combined. LLM-guided neural architecture search (NAS) can automate this exploration, but most existing workflows assume cloud execution or access to data-derived artifacts that cannot be exposed. We present a novel data-local, LLM-guided search framework that handles candidate pipelines remotely while executing all training and evaluation locally under a fixed protocol. The controller observes only trial-level summaries, such as pipeline descriptors, metrics, learning-curve statistics, and failure logs, without ever accessing raw samples or intermediate feature representations. Our framework targets multiclass, multimodal learning via one-vs-rest binary experts per class and modality, a lightweight fusion MLP, and joint search over expert architectures and modality-specific preprocessing. We evaluate our method on two regimes: UEA30 (public multivariate time-series classification dataset) and SleepEDFx sleep staging (heterogeneous clinical modalities such as EEG, EOG, and EMG). The results show that the modular baseline model is strong, and the LLM-guided NAS further improves it. Notably, our method finds models that perform within published ranges across most benchmark datasets. Across both settings, our method reduces manual intervention by enabling unattended architecture search while keeping sensitive data on-premise.

</details>

---

### 14. [Scientific Machine Learning-assisted Model Discovery from Telemetry Data](https://arxiv.org/abs/2603.15943)

**基本信息**

- 🔗 arXiv: [`2603.15943`](https://arxiv.org/abs/2603.15943)
- 👥 作者: Sebastian Micluta-Campeanu, Avinash Subramanian, Anas Abdelrehim 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15943.pdf)

**💡 相关性分析**

满足标准1：论文提出的Dyad Model Discovery方法，其核心是从数据中发现符号表达式以增强模型，这与“化学大模型”中从数据学习可解释的化学规律、或“质谱结构推理”中学习谱图生成规则的任务在目标和方法上直接相关。

**📖 中文摘要**

这篇论文提出了一种半自动化方法，称为Dyad Model Discovery，用于从数据中发现符号表达式以增强物理方程的建模。当现有模型因简化假设过多而无法很好地校准时，该方法可以从数据中自动发现符号表达式来补充缺失的物理机制。该方法采用“人在回路”的工作流程。这项工作与“化学大模型”和“质谱结构推理”高度相关：1）在计算化学和化学动力学中，从实验或模拟数据中发现速率方程、反应机理或经验势函数是核心任务；2）在质谱解析中，从大量谱图数据中学习碎裂规则或分子描述符与谱图特征的映射关系，也可以视为一种模型发现。论文提出的结合符号回归与领域知识（人在回路）的框架，为从化学和质谱数据中自动发现可解释的物理或经验模型提供了直接可用的方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Calibration of dynamic models to data is an important step in building building digital twins of HVAC equipment, thermal loads and control systems. Sometimes, when a model fails to calibrate to data, a possible cause is that the model has made too many sim- plifying assumptions and is missing physics. In this paper we propose a semi-automated approach, called Dyad Model Discovery, that can augment the physical equations of the model with symbolic expressions discovered from the data. We demonstrate this method on a digital twin of a transportation refrigeration unit to improve its predictive performance, trained using telemetry data. An engineer-in-the-loop workflow is proposed, which provides suggestions to the user which can then be accepted or rejected. This is the first AI-assisted engineering design workflow to our knowledge.

</details>

---

### 15. [Protein Design with Agent Rosetta: A Case Study for Specialized Scientific Agents](https://arxiv.org/abs/2603.15952)

**基本信息**

- 🔗 arXiv: [`2603.15952`](https://arxiv.org/abs/2603.15952)
- 👥 作者: Jacopo Teneggi, S.M. Bargeen A. Turzo, Tanya Marwah 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15952.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建用于蛋白质设计（化学信息学子领域）的AI智能体（Agent Rosetta），这直接属于“化学大模型”在具体科学任务中的应用和实现，展示了LLM与专业科学软件结合完成复杂化学设计任务的范式。

**📖 中文摘要**

这篇论文介绍了Agent Rosetta，这是一个与结构化环境配对的LLM智能体，用于操作领先的基于物理的异质聚合物设计软件Rosetta。该智能体能够迭代优化设计以实现用户定义的目标，将LLM的推理能力与Rosetta的通用性相结合。论文评估了Agent Rosetta在规范氨基酸和非规范氨基酸设计上的性能。这项工作与“化学大模型”高度相关：1）蛋白质设计是化学和生物信息学的核心领域，是“化学大模型”的重要应用场景；2）论文展示了如何构建AI智能体来驱动专业的科学计算软件（Rosetta），完成复杂的分子设计任务，这为构建用于其他化学领域（如小分子设计、材料设计）的AI智能体提供了直接的范例和方法论。它体现了“化学大模型”从被动预测工具向主动设计智能体的演进方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are capable of emulating reasoning and using tools, creating opportunities for autonomous agents that execute complex scientific tasks. Protein design provides a natural testbed: although machine learning (ML) methods achieve strong results, these are largely restricted to canonical amino acids and narrow objectives, leaving unfilled need for a generalist tool for broad design pipelines. We introduce Agent Rosetta, an LLM agent paired with a structured environment for operating Rosetta, the leading physics-based heteropolymer design software, capable of modeling non-canonical building blocks and geometries. Agent Rosetta iteratively refines designs to achieve user-defined objectives, combining LLM reasoning with Rosetta's generality. We evaluate Agent Rosetta on design with canonical amino acids, matching specialized models and expert baselines, and with non-canonical residues -- where ML approaches fail -- achieving comparable performance. Critically, prompt engineering alone often fails to generate Rosetta actions, demonstrating that environment design is essential for integrating LLM agents with specialized software. Our results show that properly designed environments enable LLM agents to make scientific software accessible while matching specialized tools and human experts.

</details>

---

### 16. [A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Histopathology](https://arxiv.org/abs/2603.15967)

**基本信息**

- 🔗 arXiv: [`2603.15967`](https://arxiv.org/abs/2603.15967)
- 👥 作者: Harishwar Reddy Kasireddy, Patricio S. La Rosa, Akshita Gupta 等15人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15967.pdf)

**💡 相关性分析**

满足标准2：论文对基础模型进行的系统性评估框架、基准任务设计、统计分析方法以及发布的评估工具包，为“化学大模型”和“质谱分析基础模型”的评估提供了可直接借鉴或迁移的方法论、工具和最佳实践范例。

**📖 中文摘要**

这篇论文对11个公开可用的组织病理学基础模型（HFMs）在肾脏特异性下游任务上进行了系统评估。虽然领域是医学影像，但其工作流程和方法论与评估“化学大模型”或“质谱分析基础模型”高度相似。论文涵盖了多染色、多空间尺度、多任务类型的综合评估，并使用了严格的统计检验。这项工作为“化学大模型”和“质谱分析基础模型”的评估提供了宝贵的范例：1）如何系统性地评估一个预训练基础模型在特定化学领域（如分子性质预测、反应预测）或质谱任务（如谱图分类、结构检索）上的迁移能力和局限性；2）如何设计涵盖不同难度和侧重点的基准任务；3）如何分析模型失败的模式。论文中发布的评估工具包（kidney-hfm-eval）也体现了标准化的、可复现的评估框架的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathology foundation models (HFMs), pretrained on large-scale cancer datasets, have advanced computational pathology. However, their applicability to non-cancerous chronic kidney disease remains underexplored, despite coexistence of renal pathology with malignancies such as renal cell and urothelial carcinoma. We systematically evaluate 11 publicly available HFMs across 11 kidney-specific downstream tasks spanning multiple stains (PAS, H&E, PASM, and IHC), spatial scales (tile and slide-level), task types (classification, regression, and copy detection), and clinical objectives, including detection, diagnosis, and prognosis. Tile-level performance is assessed using repeated stratified group cross-validation, while slide-level tasks are evaluated using repeated nested stratified cross-validation. Statistical significance is examined using Friedman test followed by pairwise Wilcoxon signed-rank testing with Holm-Bonferroni correction and compact letter display visualization. To promote reproducibility, we release an open-source Python package, kidney-hfm-eval, available at this https URL , that reproduces the evaluation pipelines. Results show moderate to strong performance on tasks driven by coarse meso-scale renal morphology, including diagnostic classification and detection of prominent structural alterations. In contrast, performance consistently declines for tasks requiring fine-grained microstructural discrimination, complex biological phenotypes, or slide-level prognostic inference, largely independent of stain type. Overall, current HFMs appear to encode predominantly static meso-scale representations and may have limited capacity to capture subtle renal pathology or prognosis-related signals. Our results highlight the need for kidney-specific, multi-stain, and multimodal foundation models to support clinically reliable decision-making in nephrology.

</details>

---

### 17. [Visual Set Program Synthesizer](https://arxiv.org/abs/2603.15997)

**基本信息**

- 🔗 arXiv: [`2603.15997`](https://arxiv.org/abs/2603.15997)
- 👥 作者: Zehua Cheng, Wei Dai, Wenhu Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15997.pdf)

**💡 相关性分析**

满足标准1：论文提出的视觉程序合成框架，其将复杂推理任务分解为可执行符号程序的思路，与“化学大模型”中需要的可解释分子推理（如逆合成规划）和“质谱结构推理”中多步骤谱图解析的逻辑链条在方法论上直接相关，提供了一种构建可解释AI系统的途径。

**📖 中文摘要**

这篇论文提出了将视觉推理视为视觉程序合成的思路，即模型首先生成一个符号化程序，然后由一个基于视觉场景的独立引擎执行。论文还引入了Set-VQA这一新的基准，专门用于评估基于集合的视觉推理。虽然应用场景是视觉问答，但其核心方法论——将复杂推理任务分解为可执行的符号化程序——与“化学大模型”和“质谱结构推理”中面临的挑战高度相关。在化学信息学中，许多任务（如逆合成分析、分子性质的多步推理）可以形式化为程序合成问题。在质谱解析中，从谱图推导出分子结构也涉及一系列逻辑推理步骤（如识别官能团、拼接碎片）。论文提出的程序合成框架，为构建可解释、可组合的化学或质谱推理系统提供了有前景的架构方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A user pointing their phone at a supermarket shelf and asking "Which soda has the least sugar?" poses a difficult challenge for current visual Al assistants. Such queries require not only object recognition, but explicit set-based reasoning such as filtering, comparison, and aggregation. Standard endto-end MLLMs often fail at these tasks because they lack an explicit mechanism for compositional logic. We propose treating visual reasoning as Visual Program Synthesis, where the model first generates a symbolic program that is executed by a separate engine grounded in visual scenes. We also introduce Set-VQA, a new benchmark designed specifically for evaluating set-based visual reasoning. Experiments show that our approach significantly outperforms state-of-the-art baselines on complex reasoning tasks, producing more systematic and transparent behavior while substantially improving answer accuracy. These results demonstrate that program-driven reasoning provides a principled alternative to black-box visual-language inference.

</details>

---

### 18. [RadAnnotate: Large Language Models for Efficient and Reliable Radiology Report Annotation](https://arxiv.org/abs/2603.16002)

**基本信息**

- 🔗 arXiv: [`2603.16002`](https://arxiv.org/abs/2603.16002)
- 👥 作者: Saisha Pradeep Shetty, Roger Eric Goldman, Vladimir Filkov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16002.pdf)

**💡 相关性分析**

满足标准2：论文提出的LLM辅助数据标注和合成框架（RadAnnotate），其方法（RAG生成合成数据、置信度筛选）可直接用于生成或增强“化学大模型”和“质谱结构推理”所需的关键训练数据（如分子数据集、谱图-结构对数据集），提供了构建数据资源的新工具。

**📖 中文摘要**

这篇论文提出了RadAnnotate，一个基于LLM的框架，用于放射学报告的高效可靠标注。它研究了基于检索增强的合成报告和基于置信度的选择性自动化，以减少专家标注工作量。虽然领域是医学文本，但其核心方法——利用LLM和检索增强生成（RAG）进行数据标注和增强——与“化学大模型”和“质谱结构推理”中的数据资源构建高度相关。在化学和质谱领域，获取高质量、大规模标注数据（如分子-性质对、谱图-结构对）是训练强大模型的关键瓶颈。RadAnnotate框架展示了如何利用LLM和合成数据来辅助或自动化这一过程，包括生成合成数据、自动标注以及通过置信度筛选保证质量。这为化学和质谱领域构建和扩充关键数据集提供了直接可用的技术方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Radiology report annotation is essential for clinical NLP, yet manual labeling is slow and costly. We present RadAnnotate, an LLM-based framework that studies retrieval-augmented synthetic reports and confidence-based selective automation to reduce expert effort for labeling in RadGraph. We study RadGraph-style entity labeling (graph nodes) and leave relation extraction (edges) to future work. First, we train entity-specific classifiers on gold-standard reports and characterize their strengths and failure modes across anatomy and observation categories, with uncertain observations hardest to learn. Second, we generate RAG-guided synthetic reports and show that synthetic-only models remain within 1-2 F1 points of gold-trained models, and that synthetic augmentation is especially helpful for uncertain observations in a low-resource setting, improving F1 from 0.61 to 0.70. Finally, by learning entity-specific confidence thresholds, RadAnnotate can automatically annotate 55-90% of reports at 0.86-0.92 entity match score while routing low-confidence cases for expert review.

</details>

---

### 19. [Evaluating Agentic Optimization on Large Codebases](https://arxiv.org/abs/2603.16011)

**基本信息**

- 🔗 arXiv: [`2603.16011`](https://arxiv.org/abs/2603.16011)
- 👥 作者: Atharva Sehgal, James Hou, Akanksha Sarkar 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16011.pdf)

**💡 相关性分析**

满足标准2：论文提出的FormulaCode基准，其针对复杂、多目标、现实约束下的AI智能体评估框架，为未来设计和构建评估“化学大模型”或“化学AI智能体”在真实科研工作流中性能的基准提供了重要的方法论参考和设计范例。

**📖 中文摘要**

这篇论文介绍了FormulaCode，一个用于评估大型、真实世界代码库上智能体优化能力的基准。它包含从GitHub科学Python仓库中挖掘出的性能瓶颈，每个都配有专家编写的补丁和大量性能测试。虽然评估对象是代码优化智能体，但其基准设计理念——在现实约束下（正确性、性能）评估智能体对大型复杂工件的整体优化能力——与评估“化学大模型”或“化学AI智能体”的能力高度相关。例如，评估一个AI化学家智能体是否能够优化一个复杂的合成实验方案或分子设计流程，就需要类似的、多目标、细粒度的评估基准。FormulaCode为如何构建一个全面、严谨的基准来评估AI系统在复杂科学任务（如化学研究）中的表现提供了重要的设计范例和思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) coding agents increasingly operate at the repository level, motivating benchmarks that evaluate their ability to optimize entire codebases under realistic constraints. Existing code benchmarks largely rely on synthetic tasks, binary correctness signals, or single-objective evaluation, limiting their ability to assess holistic optimization behavior. We introduce FormulaCode, a benchmark for evaluating agentic optimization on large, real-world codebases with fine-grained, multi-objective performance metrics. FormulaCode comprises 957 performance bottlenecks mined from scientific Python repositories on GitHub, each paired with expert-authored patches and, on average, 264.6 community-maintained performance workloads per task, enabling the holistic ability of LLM agents to optimize codebases under realistic correctness and performance constraints. Our evaluations reveal that repository-scale, multi-objective optimization remains a major challenge for frontier LLM agents. Project website at: this https URL

</details>

---

### 20. [Interpretable Context Methodology: Folder Structure as Agentic Architecture](https://arxiv.org/abs/2603.16021)

**基本信息**

- 🔗 arXiv: [`2603.16021`](https://arxiv.org/abs/2603.16021)
- 👥 作者: Jake Van Clief, David McDermott
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16021.pdf)

**💡 相关性分析**

满足标准1：论文提出的MWP协议，为构建和编排由“化学大模型”驱动的、人类在回路的自动化化学研究或分析工作流，提供了一种简单、可解释、易于实现的架构方法论，直接关系到如何将大模型能力有效集成到化学研究实践中。

**📖 中文摘要**

这篇论文提出了模型工作空间协议（MWP），一种用文件系统结构替代复杂多智能体框架来编排AI工作流的方法。编号文件夹代表阶段，纯Markdown文件携带提示和上下文，指导单个AI智能体在每一步扮演什么角色。这种方法将Unix管道设计、模块化分解等思想应用于为AI智能体构建上下文。虽然不直接针对化学领域，但这种轻量级、可解释、易于人类审查和干预的智能体工作流编排方法，对于构建用于化学研究（如实验设计、数据分析、文献调研）的AI辅助系统具有很高的实用价值。它降低了构建领域专用AI工作流（如“化学大模型”驱动的自动化研究管道）的技术门槛和工程开销，提供了一种简洁有效的架构模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current approaches to AI agent orchestration typically involve building multi-agent frameworks that manage context passing, memory, error handling, and step coordination through code. These frameworks work well for complex, concurrent systems. But for sequential workflows where a human reviews output at each step, they introduce engineering overhead that the problem does not require. This paper presents Model Workspace Protocol (MWP), a method that replaces framework-level orchestration with filesystem structure. Numbered folders represent stages. Plain markdown files carry the prompts and context that tell a single AI agent what role to play at each step. Local scripts handle the mechanical work that does not need AI at all. The result is a system where one agent, reading the right files at the right moment, does the work that would otherwise require a multi-agent framework. This approach applies ideas from Unix pipeline design, modular decomposition, multi-pass compilation, and literate programming to the specific problem of structuring context for AI agents. The protocol is open source under the MIT license.

</details>

---

### 21. [MDM-Prime-v2: Binary Encoding and Index Shuffling Enable Compute-optimal Scaling of Diffusion Language Models](https://arxiv.org/abs/2603.16077)

**基本信息**

- 🔗 arXiv: [`2603.16077`](https://arxiv.org/abs/2603.16077)
- 👥 作者: Chen-Hao Chao, Wei-Fang Sun, Junwei Qua 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16077.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种高效的掩码扩散语言模型（MDM-Prime-v2），这属于“化学大模型”主题下的模型架构与效率优化研究。

**📖 中文摘要**

本文提出了MDM-Prime-v2，一种掩码扩散语言模型，通过引入二进制编码和索引洗牌技术，显著提升了计算效率。研究表明，该模型在计算最优比较中比自回归模型（ARM）效率高21.8倍，并在OpenWebText上实现了7.77的困惑度，优于ARM、MDM和MDM-Prime。该模型在扩展到11亿参数时，在多种常识推理任务上表现出优异的零样本准确性。这项工作直接围绕“化学大模型”主题，探索了扩散模型在语言建模中的高效架构，为构建化学领域的专用大语言模型提供了潜在的技术路径和效率基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Masked diffusion models (MDM) exhibit superior generalization when learned using a Partial masking scheme (Prime). This approach converts tokens into sub-tokens and models the diffusion process at the sub-token level. We identify two limitations of the MDM-Prime framework. First, we lack tools to guide the hyperparameter choice of the token granularity in the subtokenizer. Second, we find that the function form of the subtokenizer significantly degrades likelihood estimation when paired with commonly used Byte-Pair-Encoding (BPE) tokenizers. To address these limitations, we study the tightness of the variational bound in MDM-Prime and develop MDM-Prime-v2, a masked diffusion language model which incorporates Binary Encoding and Index Shuffling. Our scaling analysis reveals that MDM-Prime-v2 is 21.8$\times$ more compute-efficient than autoregressive models (ARM). In compute-optimal comparisons, MDM-Prime-v2 achieves 7.77 perplexity on OpenWebText, outperforming ARM (12.99), MDM (18.94), and MDM-Prime (13.41). When extending the model size to 1.1B parameters, our model further demonstrates superior zero-shot accuracy on various commonsense reasoning tasks.

</details>

---

### 22. [ASDA: Automated Skill Distillation and Adaptation for Financial Reasoning](https://arxiv.org/abs/2603.16112)

**基本信息**

- 🔗 arXiv: [`2603.16112`](https://arxiv.org/abs/2603.16112)
- 👥 作者: Tik Yu Yim, Wenting Tan, Sum Yee Chan 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16112.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于金融推理的自动化技能蒸馏与适应框架（ASDA），这属于“化学大模型”主题下，针对特定科学领域（此处为金融，但其方法论可迁移至化学）进行模型适应和性能提升的研究。

**📖 中文摘要**

本文提出了ASDA（自动化技能蒸馏与适应）框架，用于金融推理领域的领域适应。该框架通过迭代的错误纠正学习，自动生成结构化的技能工件（包含推理过程、代码模板和工作示例），并在推理过程中动态注入这些技能，从而在不修改模型权重的情况下提升模型在特定领域的性能。在金融推理基准FAMMA上的评估显示，ASDA在算术推理和非算术推理任务上分别取得了高达+17.33%和+5.95%的改进。该框架生成的技能工件是人类可读、版本可控的，并与Agent Skills开放标准兼容。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting large language models (LLMs) to specialized financial reasoning typically requires expensive fine-tuning that produces model-locked expertise. Training-free alternatives have emerged, yet our experiments show that leading methods (GEPA and ACE) achieve only marginal gains on the FAMMA financial reasoning benchmark, exposing the limits of unstructured text optimization for complex, multi-step domain reasoning. We introduce Automated Skill Distillation and Adaptation (ASDA), a framework that automatically generates structured skill artifacts through iterative error-corrective learning without modifying model weights. A teacher model analyzes a student model's failures on financial reasoning tasks, clusters errors by subfield and error type, and synthesizes skill files containing reasoning procedures, code templates, and worked examples, which are dynamically injected during inference. Evaluated on FAMMA, ASDA achieves up to +17.33% improvement on arithmetic reasoning and +5.95% on non-arithmetic reasoning, substantially outperforming all training-free baselines. The resulting skill artifacts are human-readable, version-controlled, and compatible with the Agent Skills open standard, offering any organization with a labeled domain dataset a practical and auditable path to domain adaptation without weight access or retraining.

</details>

---

### 23. [SIA: A Synthesize-Inject-Align Framework for Knowledge-Grounded and Secure E-commerce Search LLMs with Industrial Deployment](https://arxiv.org/abs/2603.16137)

**基本信息**

- 🔗 arXiv: [`2603.16137`](https://arxiv.org/abs/2603.16137)
- 👥 作者: Zhouwei Zhai, Mengxiang Chen, Anmeng Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16137.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于电子商务搜索的大语言模型框架（SIA），涉及知识注入、安全对齐和工业部署，这直接属于“化学大模型”主题下，构建领域专用、安全可靠的大型语言模型的研究范畴。

**📖 中文摘要**

本文提出了SIA（合成-注入-对齐）框架，用于构建知识丰富且安全的电子商务搜索大语言模型。该框架首先通过结合知识图谱和行为日志合成高质量的自然语言语料库；然后采用基于深度上采样的参数高效预训练策略，将领域知识注入模型；最后通过多任务指令微调和对抗训练进行双路径对齐，以增强任务性能和安全性。该框架已在京东（中国最大的自营电商平台）部署，A/B测试显示其在核心搜索场景的关键业务指标上取得了显著提升。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models offer transformative potential for e-commerce search by enabling intent-aware recommendations. However, their industrial deployment is hindered by two critical challenges: (1) knowledge hallucination due to insufficient encoding of dynamic, fine-grained product knowledge, and (2) security vulnerabilities under jailbreak attacks that threaten compliance. To address these issues, we propose SI--a Synthesize-Inject-Align framework for building knowledgeable and secure e-commerce search LLMs. Our approach first synthesizes high-quality natural language corpus by combining structured knowledge graphs with unstructured behavioral logs, augmented with reasoning chains and safety-aware this http URL then introduce a parameter-efficient pre-training strategy based on Depth Up-Scaling to inject domain knowledge while preserving general capabilities. Finally, a dual-path alignment method via multi-task instruction tuning and adversarial training strengthens both task performance and safety robustness. The framework has been deployed at this http URL , China's largest self-operated e-commerce platform, where A/B tests across five core search scenarios demonstrate significant improvements in key business metrics, validating its industrial effectiveness and scalability.

</details>

---

### 24. [The Finetuner's Fallacy: When to Pretrain with Your Finetuning Data](https://arxiv.org/abs/2603.16177)

**基本信息**

- 🔗 arXiv: [`2603.16177`](https://arxiv.org/abs/2603.16177)
- 👥 作者: Christina Baek, Ricardo Pio Monti, David Schwab 等34人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16177.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索大语言模型在狭窄专业领域（包括化学领域ChemPile）的高效适应策略（专业化预训练），这直接与“化学大模型”主题相关，为化学领域大模型的训练提供了数据效率和性能优化的方法论。

**📖 中文摘要**

本文研究了“专业化预训练”（SPT）策略，即在预训练阶段重复使用通常用于微调的小型领域数据集。研究表明，与标准预训练相比，SPT在微调后能提升模型在特定领域的性能，同时更好地保留通用能力。在化学（ChemPile）、音乐（MusicPile）和数学证明（ProofPile）三个专业领域上的实验表明，SPT能以更少的预训练token达到给定的领域性能，当目标领域在预训练语料库中代表性不足时，收益更为显著。论文还推导了过拟合缩放定律，以指导从业者为给定的计算预算选择最佳的领域数据重复策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real-world model deployments demand strong performance on narrow domains where data is often scarce. Typically, practitioners finetune models to specialize them, but this risks overfitting to the domain and forgetting general knowledge. We study a simple strategy, specialized pretraining (SPT), where a small domain dataset, typically reserved for finetuning, is repeated starting from pretraining as a fraction of the total tokens. Across three specialized domains (ChemPile, MusicPile, and ProofPile), SPT improves domain performance and preserves general capabilities after finetuning compared to standard pretraining. In our experiments, SPT reduces the pretraining tokens needed to reach a given domain performance by up to 1.75x. These gains grow when the target domain is underrepresented in the pretraining corpus: on domains far from web text, a 1B SPT model outperforms a 3B standard pretrained model. Beyond these empirical gains, we derive overfitting scaling laws to guide practitioners in selecting the optimal domain-data repetition for a given pretraining compute budget. Our observations reveal the finetuner's fallacy: while finetuning may appear to be the cheapest path to domain adaptation, introducing specialized domain data during pretraining stretches its utility. SPT yields better specialized domain performance (via reduced overfitting across repeated exposures) and better general domain performance (via reduced forgetting during finetuning), ultimately achieving stronger results with fewer parameters and less total compute when amortized over inference. To get the most out of domain data, incorporate it as early in training as possible.

</details>

---

### 25. [Sample-Efficient Adaptation of Drug-Response Models to Patient Tumors under Strong Biological Domain Shift](https://arxiv.org/abs/2603.16185)

**基本信息**

- 🔗 arXiv: [`2603.16185`](https://arxiv.org/abs/2603.16185)
- 👥 作者: Camille Jimenez Cortes, Philippe Lalanda, German Vega
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16185.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于药物反应预测的模型适应框架，该任务属于“化学信息学”和“质谱分析”领域常见的下游应用（尽管本文侧重于基因组数据，但其方法论与化学信息学中的QSAR/分子性质预测高度相关）。同时，其解决“领域偏移”和“少样本适应”的核心挑战，对于构建鲁棒的化学大模型具有重要参考价值。

**📖 中文摘要**

本文研究在强生物学领域偏移下，将临床前药物反应模型高效适应到患者肿瘤数据的问题。论文提出了一个分阶段的迁移学习框架，首先从大量未标记的药物基因组学数据中独立学习细胞和药物的表示，然后在细胞系数据上将表示与药物反应标签对齐，最后使用少量样本监督将模型适应到患者肿瘤数据。实验表明，当源域和目标域（如体外细胞系与体内患者肿瘤）存在显著差异时，无监督预训练学习到的结构化、可迁移表示可以大幅减少有效药物反应预测所需的临床监督数据量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug response in patients from preclinical data remains a major challenge in precision oncology due to the substantial biological gap between in vitro cell lines and patient tumors. Rather than aiming to improve absolute in vitro prediction accuracy, this work examines whether explicitly separating representation learning from task supervision enables more sample-efficient adaptation of drug-response models to patient data under strong biological domain shift. We propose a staged transfer-learning framework in which cellular and drug representations are first learned independently from large collections of unlabeled pharmacogenomic data using autoencoder-based representation learning. These representations are then aligned with drug-response labels on cell-line data and subsequently adapted to patient tumors using few-shot supervision. Through a systematic evaluation spanning in-domain, cross-dataset, and patient-level settings, we show that unsupervised pretraining provides limited benefit when source and target domains overlap substantially, but yields clear gains when adapting to patient tumors with very limited labeled data. In particular, the proposed framework achieves faster performance improvements during few-shot patient-level adaptation while maintaining comparable accuracy to single-phase baselines on standard cell-line benchmarks. Overall, these results demonstrate that learning structured and transferable representations from unlabeled molecular profiles can substantially reduce the amount of clinical supervision required for effective drug-response prediction, offering a practical pathway toward data-efficient preclinical-to-clinical translation.

</details>

---

### 26. [Offline Exploration-Aware Fine-Tuning for Long-Chain Mathematical Reasoning](https://arxiv.org/abs/2603.16206)

**基本信息**

- 🔗 arXiv: [`2603.16206`](https://arxiv.org/abs/2603.16206)
- 👥 作者: Yongyu Mu, Jiali Zeng, Fandong Meng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16206.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大语言模型的监督微调阶段，以更好地为后续的强化学习探索（如RLVR）做准备，从而提升复杂推理任务（如数学推理）的性能。这项工作属于“化学大模型”主题下，优化大模型训练流程以增强其科学推理能力的研究，其方法论可应用于化学推理任务。

**📖 中文摘要**

本文提出了离线探索感知微调（OXA）方法，用于提升大语言模型在长链数学推理任务中的性能。OXA通过优化两个目标来塑造初始策略：促进低置信度但已验证的教师蒸馏数据，以吸收先前未捕获的推理模式；抑制高置信度但错误的自我蒸馏数据，以将错误模式的概率质量重新分配给潜在正确的候选者。在6个基准测试上的实验结果表明，OXA能持续提升数学推理性能，并提高初始策略的熵，且这种性能增益在后续的强化学习验证奖励训练中得以保持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Through encouraging self-exploration, reinforcement learning from verifiable rewards (RLVR) has significantly advanced the mathematical reasoning capabilities of large language models. As the starting point for RLVR, the capacity of supervised fine-tuning (SFT) to memorize new chain-of-thought trajectories provides a crucial initialization that shapes the subsequent exploration landscape. However, existing research primarily focuses on facilitating exploration during RLVR training, leaving exploration-aware SFT under-explored. To bridge this gap, we propose Offline eXploration-Aware (OXA) fine-tuning. Specifically, OXA optimizes two objectives: promoting low-confidence verified teacher-distillation data to internalize previously uncaptured reasoning patterns, and suppressing high-confidence incorrect self-distillation data to redistribute probability mass of incorrect patterns toward potentially correct candidates. Experimental results across 6 benchmarks show that OXA consistently improves mathematical reasoning performance, especially achieving an average gain of $+6$ Pass@1 and $+5$ Pass@$k$ points compared to conventional SFT on the Qwen2.5-1.5B-Math. Crucially, OXA elevates initial policy entropy, and performance gains persist throughout extensive RLVR training, demonstrating the long-term value of OXA.

</details>

---

### 27. [MOSAIC: Composable Safety Alignment with Modular Control Tokens](https://arxiv.org/abs/2603.16210)

**基本信息**

- 🔗 arXiv: [`2603.16210`](https://arxiv.org/abs/2603.16210)
- 👥 作者: Jingyu Peng, Hongyu Chen, Jiancheng Dong 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16210.pdf)

**💡 相关性分析**

满足标准1：论文提出的模块化、可组合的条件控制框架，其核心思想（通过特定令牌控制模型输出）可直接应用于构建可控、可解释的化学大模型，属于核心主题相关。

**📖 中文摘要**

论文MOSAIC提出了一种用于大语言模型（LLMs）的模块化安全对齐框架。虽然其核心应用在自然语言处理领域，但论文提出的“可组合安全对齐”和“模块化控制令牌”的概念，与构建可控、可解释的“化学大模型”在方法论上高度相关。化学大模型（如用于分子生成或性质预测的模型）同样面临如何嵌入特定领域知识（如合成可行性、毒性）并实现灵活、可控生成的问题。MOSAIC框架展示了如何通过可学习的控制令牌来条件化模型行为，这一思路可直接迁移至化学信息学领域，用于指导大模型生成符合特定化学规则或安全约束的分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Safety alignment in large language models (LLMs) is commonly implemented as a single static policy embedded in model parameters. However, real-world deployments often require context-dependent safety rules that vary across users, regions, and applications. Existing approaches struggle to provide such conditional control: parameter-level alignment entangles safety behaviors with general capabilities, while prompt-based methods rely on natural language instructions that provide weak enforcement. We propose MOSAIC, a modular framework that enables compositional safety alignment through learnable control tokens optimized over a frozen backbone model. Each token represents a safety constraint and can be flexibly activated and composed at inference time. To train compositional tokens efficiently, we introduce order-based task sampling and a distribution-level alignment objective that mitigates over-refusal. Experiments show that MOSAIC achieves strong defense performance with substantially lower over-refusal while preserving model utility.

</details>

---

### 28. [Generative AI for Quantum Circuits and Quantum Code: A Technical Review and Taxonomy](https://arxiv.org/abs/2603.16216)

**基本信息**

- 🔗 arXiv: [`2603.16216`](https://arxiv.org/abs/2603.16216)
- 👥 作者: Juhani Merilehto
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16216.pdf)

**💡 相关性分析**

满足标准3：论文是对生成式AI在特定结构化领域（量子电路/代码）应用的系统性综述和分类，其方法论和评估框架的讨论对“化学大模型”（尤其是生成化学结构的模型）的研究具有重要的综述和展望参考价值。

**📖 中文摘要**

这篇论文对用于量子电路和量子代码生成的生成式人工智能系统进行了技术回顾和分类。虽然主题是量子计算，但论文系统地回顾了生成系统（包括基于监督微调、强化学习、扩散/图生成等方法）及其评估框架。这项工作为“生成式AI模型在结构化输出（如代码、电路图）生成中的应用”提供了一个清晰的综述和分类学范例。对于“化学大模型”领域，特别是专注于分子图、反应路径或光谱模拟等结构化数据生成的模型，这篇论文在模型架构、训练机制和评估方法上提供了有价值的跨领域参考和系统性思考框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We review thirteen generative systems and five supporting datasets for quantum circuit and quantum code generation, identified through a structured scoping review of Hugging Face, arXiv, and provenance tracing (January-February 2026). We organize the field along two axes: artifact type (Qiskit code, OpenQASM programs, circuit graphs); crossed with training regime (supervised fine-tuning, verifier-in-the-loop RL, diffusion/graph generation, agentic optimization); and systematically apply a three-layer evaluation framework covering syntactic validity, semantic correctness, and hardware executability. The central finding is that while all reviewed systems address syntax and most address semantics to some degree, none reports end-to-end evaluation on quantum hardware (Layer 3b), leaving a significant gap between generated circuits and practical deployment. Scope note: quantum code refers throughout to quantum program artifacts (QASM, Qiskit); we do not cover generation of quantum error-correcting codes (QEC).

</details>

---

### 29. [Visual Prompt Discovery via Semantic Exploration](https://arxiv.org/abs/2603.16250)

**基本信息**

- 🔗 arXiv: [`2603.16250`](https://arxiv.org/abs/2603.16250)
- 👥 作者: Jaechang Kim, Yotaro Shimose, Zhao Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16250.pdf)

**💡 相关性分析**

满足标准1：论文提出的自动化语义探索框架，其核心是通过实验发现增强模型对特定任务感知能力的最佳策略，这一“通过探索优化推理过程”的思路与“质谱结构推理”中寻求最优分析路径的核心主题高度相关。

**📖 中文摘要**

论文提出了一种通过语义探索自动发现视觉提示（Visual Prompts）的框架SEVEX，以解决大型视觉语言模型（LVLMs）在图像理解和视觉推理中的感知失败问题。虽然主要针对通用视觉任务，但其核心——通过自动化实验探索最优的“提示”（此处是图像操作代码）来增强模型对特定任务的感知能力——与“质谱结构推理”的研究思路有相通之处。在质谱分析中，从原始谱图到分子结构的推理也是一个复杂的感知和推理过程。SEVEX框架展示的“通过探索性实验优化任务特定提示/策略”的方法论，可以启发如何设计自动化流程来发现或优化从质谱数据中推理化学结构的最佳分析策略或特征提取方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LVLMs encounter significant challenges in image understanding and visual reasoning, leading to critical perception failures. Visual prompts, which incorporate image manipulation code, have shown promising potential in mitigating these issues. While emerged as a promising direction, previous methods for visual prompt generation have focused on tool selection rather than diagnosing and mitigating the root causes of LVLM perception failures. Because of the opacity and unpredictability of LVLMs, optimal visual prompts must be discovered through empirical experiments, which have relied on manual human trial-and-error. We propose an automated semantic exploration framework for discovering task-wise visual prompts. Our approach enables diverse yet efficient exploration through agent-driven experiments, minimizing human intervention and avoiding the inefficiency of per-sample generation. We introduce a semantic exploration algorithm named SEVEX, which addresses two major challenges of visual prompt exploration: (1) the distraction caused by lengthy, low-level code and (2) the vast, unstructured search space of visual prompts. Specifically, our method leverages an abstract idea space as a search space, a novelty-guided selection algorithm, and a semantic feedback-driven ideation process to efficiently explore diverse visual prompts based on empirical results. We evaluate SEVEX on the BlindTest and BLINK benchmarks, which are designed to assess LVLM perception. Experimental results demonstrate that SEVEX significantly outperforms baseline methods in task accuracy, inference efficiency, exploration efficiency, and exploration stability. Notably, our framework discovers sophisticated and counter-intuitive visual strategies that go beyond conventional tool usage, offering a new paradigm for enhancing LVLM perception through automated, task-wise visual prompts.

</details>

---

### 30. [Grounding the Score: Explicit Visual Premise Verification for Reliable Vision-Language Process Reward Models](https://arxiv.org/abs/2603.16253)

**基本信息**

- 🔗 arXiv: [`2603.16253`](https://arxiv.org/abs/2603.16253)
- 👥 作者: Junxin Wang, Dai Guan, Weijie Qiu 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16253.pdf)

**💡 相关性分析**

满足标准1：论文专注于提高多模态（视觉-语言）推理模型的可靠性和可解释性，其“显式验证推理前提”的核心方法与“质谱结构推理”中需要可靠、可验证地从数据推导结构这一核心主题直接相关。

**📖 中文摘要**

论文提出了显式视觉前提验证（EVPV）方法，用于提高视觉语言过程奖励模型（VL-PRMs）在评分多步推理过程中的可靠性。该方法通过让模型显式列出推理所依赖的视觉事实清单，并与从图像中独立提取的结构化视觉约束进行匹配，来校准奖励分数。这项工作直接关联到“多模态推理的可靠性与可解释性”。对于“质谱结构推理”而言，从质谱图（视觉/数据模态）到分子结构（符号模态）的推理也是一个多步、需要验证的过程。EVPV中“显式化前提并验证”的核心思想，为构建更可靠、可解释的质谱解析模型提供了重要的方法论参考，即要求模型在推理过程中明确其依据的谱图特征（如峰位、强度、同位素模式），并验证这些特征与数据的一致性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-language process reward models (VL-PRMs) are increasingly used to score intermediate reasoning steps and rerank candidates under test-time scaling. However, they often function as black-box judges: a low step score may reflect a genuine reasoning mistake or simply the verifier's misperception of the image. This entanglement between perception and reasoning leads to systematic false positives (rewarding hallucinated visual premises) and false negatives (penalizing correct grounded statements), undermining both reranking and error localization. We introduce Explicit Visual Premise Verification (EVPV), a lightweight verification interface that conditions step scoring on the reliability of the visual premises a step depends on. The policy is prompted to produce a step-wise visual checklist that makes required visual facts explicit, while a constraint extractor independently derives structured visual constraints from the input image. EVPV matches checklist claims against these constraints to compute a scalar visual reliability signal, and calibrates PRM step rewards via reliability gating: rewards for visually dependent steps are attenuated when reliability is low and preserved when reliability is high. This decouples perceptual uncertainty from logical evaluation without per-step tool calls. Experiments on VisualProcessBench and six multimodal reasoning benchmarks show that EVPV improves step-level verification and consistently boosts Best-of-N reranking accuracy over strong baselines. Furthermore, injecting controlled corruption into the extracted constraints produces monotonic performance degradation, providing causal evidence that the gains arise from constraint fidelity and explicit premise verification rather than incidental prompt effects. Code is available at: this https URL

</details>

---

### 31. [Hyperbolic Multimodal Generative Representation Learning for Generalized Zero-Shot Multimodal Information Extraction](https://arxiv.org/abs/2603.16259)

**基本信息**

- 🔗 arXiv: [`2603.16259`](https://arxiv.org/abs/2603.16259)
- 👥 作者: Baohang Zhou, Kehui Song, Rize Jin 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16259.pdf)

**💡 相关性分析**

满足标准1：论文研究从多模态数据中学习可泛化表示以进行结构化信息抽取，其双曲空间建模和生成式学习方法与“质谱结构推理”中需要关联谱图模态与结构模态、并处理未知分子的核心主题相关。

**📖 中文摘要**

论文提出了双曲多模态生成表示学习框架（HMGRL），用于解决广义零样本多模态信息抽取任务。该工作旨在从包含文本和图像的网页中提取结构化的实体和关系信息，并处理训练时未见过的类别。其核心创新在于利用双曲空间建模样本和类别原型之间的层次语义关联，并使用变分信息瓶颈和自编码器网络。虽然应用场景是网页信息抽取，但其处理的核心问题是“如何从多模态数据（文本+图像）中学习能够泛化到新类别的稳健表示”。这与“质谱结构推理”有潜在关联：质谱数据本身可以视为一种模态（数值/图像），而分子结构是另一种（图/文本）。学习能够关联质谱特征与分子结构片段、并能泛化到新结构类型的跨模态表示，是质谱解析的关键挑战之一。HMGRL框架为解决此类问题提供了新颖的几何（双曲空间）和生成式建模视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal information extraction (MIE) constitutes a set of essential tasks aimed at extracting structural information from Web texts with integrating images, to facilitate the structural construction of Web-based semantic knowledge. To address the expanding category set including newly emerging entity types or relations on websites, prior research proposed the zero-shot MIE (ZS-MIE) task which aims to extract unseen structural knowledge with textual and visual modalities. However, the ZS-MIE models are limited to recognizing the samples that fall within the unseen category set, and they struggle to deal with real-world scenarios that encompass both seen and unseen categories. The shortcomings of existing methods can be ascribed to two main aspects. On one hand, these methods construct representations of samples and categories within Euclidean space, failing to capture the hierarchical semantic relationships between the two modalities within a sample and their corresponding category prototypes. On the other hand, there is a notable gap in the distribution of semantic similarity between seen and unseen category sets, which impacts the generative capability of the ZS-MIE models. To overcome the disadvantages, we delve into the generalized zero-shot MIE (GZS-MIE) task and propose the hyperbolic multimodal generative representation learning framework (HMGRL). The variational information bottleneck and autoencoder networks are reconstructed with hyperbolic space for modeling the multi-level hierarchical semantic correlations among samples and prototypes. Furthermore, the proposed model is trained with the unseen samples generated by the decoder, and we introduce the semantic similarity distribution alignment loss to enhance the model's generalization performance. Experimental evaluations on two benchmark datasets underscore the superiority of HMGRL compared to existing baseline methods.

</details>

---

### 32. [Laya: A LeJEPA Approach to EEG via Latent Prediction over Reconstruction](https://arxiv.org/abs/2603.16281)

**基本信息**

- 🔗 arXiv: [`2603.16281`](https://arxiv.org/abs/2603.16281)
- 👥 作者: Saarang Panchavati, Uddhav Panchavati, Corey Arnold 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16281.pdf)

**💡 相关性分析**

满足标准1：论文探索了针对科学数据（EEG）的新型自监督学习架构（LeJEPA），其“预测潜在表示”的范式创新，对于为质谱等化学数据构建基础模型（化学大模型的一个子方向）具有直接的核心主题参考价值。

**📖 中文摘要**

论文提出了Laya，第一个基于LeJEPA（潜在联合嵌入预测架构）的脑电图（EEG）基础模型。该模型摒弃了以信号重建为自监督学习目标的做法，转而通过预测潜在表示来学习，旨在获得更可迁移、高层级的EEG表征。这项工作代表了自监督学习范式在特定科学数据模态（EEG）上的创新应用。对于“化学大模型”和“质谱分析”领域，尤其是当面临标记数据稀缺时，如何为质谱、核磁共振谱等光谱数据设计有效的自监督预训练方法是一个关键问题。Laya所探索的“基于潜在预测而非原始信号重建”的SSL范式，为化学光谱数据的基础模型预训练提供了新的、有潜力的技术路线参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalography (EEG) is a widely used tool for studying brain function, with applications in clinical neuroscience, diagnosis, and brain-computer interfaces (BCIs). Recent EEG foundation models trained on large unlabeled corpora aim to learn transferable representations, but their effectiveness remains unclear; reported improvements over smaller task-specific models are often modest, sensitive to downstream adaptation and fine-tuning strategies, and limited under linear probing. We hypothesize that one contributing factor is the reliance on signal reconstruction as the primary self-supervised learning (SSL) objective, which biases representations toward high-variance artifacts rather than task-relevant neural structure. To address this limitation, we explore an SSL paradigm based on Joint Embedding Predictive Architectures (JEPA), which learn by predicting latent representations instead of reconstructing raw signals. While earlier JEPA-style methods often rely on additional heuristics to ensure training stability, recent advances such as LeJEPA provide a more principled and stable formulation. We introduce Laya, the first EEG foundation model based on LeJEPA. Across a range of EEG benchmarks, Laya demonstrates improved performance under linear probing compared to reconstruction-based baselines, suggesting that latent predictive objectives offer a promising direction for learning transferable, high-level EEG representations.

</details>

---

### 33. [Learning to Predict, Discover, and Reason in High-Dimensional Discrete Event Sequences](https://arxiv.org/abs/2603.16313)

**基本信息**

- 🔗 arXiv: [`2603.16313`](https://arxiv.org/abs/2603.16313)
- 👥 作者: Hugo Math
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16313.pdf)

**💡 相关性分析**

满足标准1：论文的核心是使用Transformer、因果发现和LLM对高维事件序列进行建模、预测和规则提取，这一整套方法论与“质谱结构推理”（将质谱作为序列处理并提取结构规则）以及构建解释性强的“化学大模型”的核心主题高度相关。

**📖 中文摘要**

论文提出一个统一框架，将事件序列建模、因果发现和大语言模型（LLMs）结合起来，用于高维事件流（汽车诊断故障码序列）的自动化故障诊断。该工作将诊断序列视为一种“语言”进行建模、预测和解释，并引入了多种基于Transformer的架构进行预测性维护、可扩展的因果发现以及用于合成布尔规则的多智能体系统。这项研究的核心是将序列数据（诊断码）通过先进的机器学习（尤其是Transformer和LLM）进行建模、理解和规则提取。这与“化学大模型”和“质谱结构推理”高度相关：1）质谱数据可以视为一种时间或质荷比序列，类似事件序列；2）从质谱中推理结构或性质，本质上也是一个从复杂数据序列中提取符号化规则或知识的过程。论文中展示的序列建模、因果分析以及利用LLM进行规则合成的整套方法论，为构建智能化的质谱解析系统提供了极具价值的蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>

---

### 34. [An Interpretable Machine Learning Framework for Non-Small Cell Lung Cancer Drug Response Analysis](https://arxiv.org/abs/2603.16330)

**基本信息**

- 🔗 arXiv: [`2603.16330`](https://arxiv.org/abs/2603.16330)
- 👥 作者: Ann Rachel, Pranav M Pawar, Mithun Mukharjee 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16330.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个结合预测模型、可解释性分析和领域知识验证的框架，其致力于构建可信赖、可解释的生物医学AI模型的方法，与构建可靠、可解释的“化学大模型”（如用于性质预测或谱图解析）的核心主题直接相关。

**📖 中文摘要**

论文提出了一个可解释的机器学习框架，用于非小细胞肺癌的药物反应分析。该框架使用多组学数据（来自GDSC）和XGBoost回归器来预测药物敏感性（IC50），并利用SHAP进行特征重要性解释，同时使用大语言模型DeepSeek来验证特征的生物学合理性。这项工作展示了如何将机器学习预测模型与事后可解释性工具（SHAP）以及领域知识验证（通过LLM）相结合，以构建可信赖的生物医学分析模型。对于“化学大模型”和“质谱分析”领域，特别是在药物发现、代谢组学等领域，构建预测模型（如质谱预测性质或反应）时，模型的可解释性和与化学知识的对齐至关重要。该论文提供的“预测模型 + SHAP + LLM知识验证”框架，为开发更可靠、可解释的化学信息学模型提供了一个具体的技术范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Lung cancer is a condition where there is abnormal growth of malignant cells that spread in an uncontrollable fashion in the lungs. Some common treatment strategies are surgery, chemotherapy, and radiation which aren't the best options due to the heterogeneous nature of cancer. In personalized medicine, treatments are tailored according to the individual's genetic information along with lifestyle aspects. In addition, AI-based deep learning methods can analyze large sets of data to find early signs of cancer, types of tumor, and prospects of treatment. The paper focuses on the development of personalized treatment plans using specific patient data focusing primarily on the genetic profile. Multi-Omics data from Genomics of Drug Sensitivity in Cancer have been used to build a predictive model along with machine learning techniques. The value of the target variable, LN-IC50, determines how sensitive or resistive a drug is. An XGBoost regressor is utilized to predict the drug response focusing on molecular and cellular features extracted from cancer datasets. Cross-validation and Randomized Search are performed for hyperparameter tuning to further optimize the model's predictive performance. For explanation purposes, SHAP (SHapley Additive exPlanations) was used. SHAP values measure each feature's impact on an individual prediction. Furthermore, interpreting feature relationships was performed using DeepSeek, a large language model trained to verify the biological validity of the features. Contextual explanations regarding the most important genes or pathways were provided by DeepSeek alongside the top SHAP value constituents, supporting the predictability of the model.

</details>

---

### 35. [Decoding the Critique Mechanism in Large Reasoning Models](https://arxiv.org/abs/2603.16331)

**基本信息**

- 🔗 arXiv: [`2603.16331`](https://arxiv.org/abs/2603.16331)
- 👥 作者: Hoang Phan, Quang H. Nguyen, Hung T. Q. Le 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16331.pdf)

**💡 相关性分析**

满足标准1：论文专注于大型推理模型的自我批判和修正机制，这一核心研究主题对于构建能够进行多步、可靠推理的“化学大模型”（如进行合成规划或结构解析）具有根本性的重要参考价值。

**📖 中文摘要**

论文系统研究了大型推理模型（LRMs）中的“批判”机制，即模型检测并自我纠正中间推理错误的能力。通过向模型链式思考中插入错误，作者发现了模型隐藏的批判能力，并在特征空间中识别出了代表该行为的可解释“批判向量”。利用该向量在推理时引导潜在表示，可以提升模型的错误检测能力。这项研究深入探究了大模型内部的自验证和修正机制。对于“化学大模型”和“质谱结构推理”至关重要，因为化学推理（如逆合成分析、谱图解析）通常是多步骤的，且每一步都可能出错。理解并增强模型对自身推理步骤的批判和修正能力，是构建可靠化学AI助手的关键。该工作为在化学领域实现类似的“自我验证”推理模型提供了理论基础和技术启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Reasoning Models (LRMs) exhibit backtracking and self-verification mechanisms that enable them to revise intermediate steps and reach correct solutions, yielding strong performance on complex logical benchmarks. We hypothesize that such behaviors are beneficial only when the model has sufficiently strong "critique" ability to detect its own mistakes. This work systematically investigates how current LRMs recover from errors by inserting arithmetic mistakes in their intermediate reasoning steps. Notably, we discover a peculiar yet important phenomenon: despite the error propagating through the chain-of-thought (CoT), resulting in an incorrect intermediate conclusion, the model still reaches the correct final answer. This recovery implies that the model must possess an internal mechanism to detect errors and trigger self-correction, which we refer to as the hidden critique ability. Building on feature space analysis, we identify a highly interpretable critique vector representing this behavior. Extensive experiments across multiple model scales and families demonstrate that steering latent representations with this vector improves the model's error detection capability and enhances the performance of test-time scaling at no extra training cost. Our findings provide a valuable understanding of LRMs' critique behavior, suggesting a promising direction to control and improve their self-verification mechanism. Our code is available at this https URL .

</details>

---

### 36. [Automated identification of Ichneumonoidea wasps via YOLO-based deep learning: Integrating HiresCam for Explainable AI](https://arxiv.org/abs/2603.16351)

**基本信息**

- 🔗 arXiv: [`2603.16351`](https://arxiv.org/abs/2603.16351)
- 👥 作者: Joao Manoel Herrera Pinheiro, Gabriela Do Nascimento Herrera, Alvaro Doria Dos Santos 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16351.pdf)

**💡 相关性分析**

满足标准1：论文展示了深度学习与可解释AI（XAI）在科学图像分类中的结合应用，其“分类+特征可视化验证”的方法论与利用深度学习进行质谱图分类或识别（质谱分析的核心任务之一）的核心主题直接相关。

**📖 中文摘要**

论文提出了一种基于YOLO深度学习架构和HiResCAM可解释性技术的框架，用于自动识别姬蜂总科寄生蜂。该工作利用高分辨率图像，训练模型进行昆虫分类，并通过HiResCAM可视化模型关注的形态学特征区域，以验证其生物学合理性。这项研究是深度学习在分类学（Taxonomy）中的一个具体应用案例。对于“化学信息学”和“质谱分析”，特别是涉及光谱或谱图分类的任务（如根据质谱图对化合物进行分类、识别代谢物），该论文提供了一个完整的范例：即如何构建一个高效的图像（或谱图）分类模型，并集成可解释性技术来确保模型决策依赖于合理的特征（如特定的质谱峰），从而增加领域专家对模型的信任。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate taxonomic identification of parasitoid wasps within the superfamily Ichneumonoidea is essential for biodiversity assessment, ecological monitoring, and biological control programs. However, morphological similarity, small body size, and fine-grained interspecific variation make manual identification labor-intensive and expertise-dependent. This study proposes a deep learning-based framework for the automated identification of Ichneumonoidea wasps using a YOLO-based architecture integrated with High-Resolution Class Activation Mapping (HiResCAM) to enhance interpretability. The proposed system simultaneously identifies wasp families from high-resolution images. The dataset comprises 3556 high-resolution images of Hymenoptera specimens. The taxonomic distribution is primarily concentrated among the families Ichneumonidae (n = 786), Braconidae (n = 648), Apidae (n = 466), and Vespidae (n = 460). Extensive experiments were conducted using a curated dataset, with model performance evaluated through precision, recall, F1 score, and accuracy. The results demonstrate high accuracy of over 96 % and robust generalization across morphological variations. HiResCAM visualizations confirm that the model focuses on taxonomically relevant anatomical regions, such as wing venation, antennae segmentation, and metasomal structures, thereby validating the biological plausibility of the learned features. The integration of explainable AI techniques improves transparency and trustworthiness, making the system suitable for entomological research to accelerate biodiversity characterization in an under-described parasitoid superfamily.

</details>

---

### 37. [FactorEngine: A Program-level Knowledge-Infused Factor Mining Framework for Quantitative Investment](https://arxiv.org/abs/2603.16365)

**基本信息**

- 🔗 arXiv: [`2603.16365`](https://arxiv.org/abs/2603.16365)
- 👥 作者: Qinhong Lin, Ruitao Feng, Yinglun Feng 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16365.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个利用LLM和程序合成进行领域知识注入和可执行因子发现的框架，其“将知识转化为可执行代码”的核心思想与构建能够自动发现化学规则或描述符的“化学大模型”这一主题高度相关。

**📖 中文摘要**

论文提出了FactorEngine，一个程序级的知识注入因子挖掘框架，用于量化投资。该框架将阿尔法因子表示为图灵完备的代码，通过LLM引导的搜索、贝叶斯优化和知识注入（将金融报告转化为可执行因子程序）来发现可执行、可审计的预测信号。其核心是将因子发现过程形式化为程序合成问题，并融入领域知识。这一思路与“化学信息学”中“化学大模型”的一个潜在方向高度契合：即如何让AI自动发现或设计新的“化学描述符”或“反应规则”。将化学知识（如文献、专利）通过LLM转化为可执行的程序或函数，并用于指导分子设计或反应预测，是化学AI的前沿课题。FactorEngine在金融领域的成功实践，为化学领域类似的“可解释、可执行知识发现”提供了重要的架构参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study alpha factor mining, the automated discovery of predictive signals from noisy, non-stationary market data-under a practical requirement that mined factors be directly executable and auditable, and that the discovery process remain computationally tractable at scale. Existing symbolic approaches are limited by bounded expressiveness, while neural forecasters often trade interpretability for performance and remain vulnerable to regime shifts and overfitting. We introduce FactorEngine (FE), a program-level factor discovery framework that casts factors as Turing-complete code and improves both effectiveness and efficiency via three separations: (i) logic revision vs. parameter optimization, (ii) LLM-guided directional search vs. Bayesian hyperparameter search, and (iii) LLM usage vs. local computation. FE further incorporates a knowledge-infused bootstrapping module that transforms unstructured financial reports into executable factor programs through a closed-loop multi-agent extraction-verification-code-generation pipeline, and an experience knowledge base that supports trajectory-aware refinement (including learning from failures). Across extensive backtests on real-world OHLCV data, FE produces factors with substantially stronger predictive stability and portfolio impact-for example, higher IC/ICIR (and Rank IC/ICIR) and improved AR/Sharpe, than baseline methods, achieving state-of-the-art predictive and portfolio performance.

</details>

---

### 38. [DermaFlux: Synthetic Skin Lesion Generation with Rectified Flows for Enhanced Image Classification](https://arxiv.org/abs/2603.16392)

**基本信息**

- 🔗 arXiv: [`2603.16392`](https://arxiv.org/abs/2603.16392)
- 👥 作者: Stathis Galanakis, Alexandros Koliousis, Stefanos Zafeiriou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16392.pdf)

**💡 相关性分析**

满足标准1：论文专注于在特定科学领域（皮肤病学）构建高质量、可控的生成式AI模型以解决数据问题，其技术路线（修正流、LoRA微调、知识引导生成）和成功案例，与构建用于分子、反应或光谱生成的“化学大模型”核心主题高度相关。

**📖 中文摘要**

论文提出了DermaFlux，一个基于修正流（Rectified Flows）的文本到图像生成框架，专门用于合成具有临床基础的皮肤病变图像。该框架使用LoRA对Flux.1进行微调，并利用LLM根据皮肤病学标准生成描述性文本。生成的图像用于增强数据集，显著提升了皮肤病变分类器的性能。这项工作是在特定医学领域（皮肤病学）构建高质量、可控的生成式模型以解决数据稀缺和类别不平衡问题的典范。对于“化学大模型”，特别是在分子生成、反应预测或光谱生成等子领域，同样面临高质量数据稀缺的问题。DermaFlux展示的“利用领域知识（文本描述）指导扩散模型生成”以及“通过生成数据提升下游任务性能”的完整流程，为化学领域构建类似的生成模型（如根据文本描述生成分子结构或质谱图）提供了直接且先进的技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite recent advances in deep generative modeling, skin lesion classification systems remain constrained by the limited availability of large, diverse, and well-annotated clinical datasets, resulting in class imbalance between benign and malignant lesions and consequently reduced generalization performance. We introduce DermaFlux, a rectified flow-based text-to-image generative framework that synthesizes clinically grounded skin lesion images from natural language descriptions of dermatological attributes. Built upon Flux.1, DermaFlux is fine-tuned using parameter-efficient Low-Rank Adaptation (LoRA) on a large curated collection of publicly available clinical image datasets. We construct image-text pairs using synthetic textual captions generated by Llama 3.2, following established dermatological criteria including lesion asymmetry, border irregularity, and color variation. Extensive experiments demonstrate that DermaFlux generates diverse and clinically meaningful dermatology images that improve binary classification performance by up to 6% when augmenting small real-world datasets, and by up to 9% when classifiers are trained on DermaFlux-generated synthetic images rather than diffusion-based synthetic images. Our ImageNet-pretrained ViT fine-tuned with only 2,500 real images and 4,375 DermaFlux-generated samples achieves 78.04% binary classification accuracy and an AUC of 0.859, surpassing the next best dermatology model by 8%.

</details>

---

### 39. [3D Fourier-based Global Feature Extraction for Hyperspectral Image Classification](https://arxiv.org/abs/2603.16426)

**基本信息**

- 🔗 arXiv: [`2603.16426`](https://arxiv.org/abs/2603.16426)
- 👥 作者: Muhammad Ahmad
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16426.pdf)

**💡 相关性分析**

满足标准1：论文提出的多维频率变换和特征融合框架，其核心思想（处理高维、结构化数据以进行推理）与“质谱结构推理”任务中从多维质谱数据推断分子结构所面临的挑战和方法论高度相关。

**📖 中文摘要**

本文提出了一种用于高光谱图像分类（HSIC）的新型架构Hybrid GFNet (HGFNet)。该模型集成了局部3D卷积特征提取和基于频域的全局滤波。其核心创新在于引入了三种针对高光谱图像量身定制的频率变换：沿光谱轴的1D傅里叶变换（光谱傅里叶变换）、空间维度上的2D傅里叶变换（空间傅里叶变换）以及联合光谱和空间维度的3D傅里叶变换（空间-空间傅里叶变换）。这些变换实现了全面、高维的频率建模，以高效捕捉长程依赖并抑制噪声。虽然论文应用领域是图像分类，但其核心方法——利用多维度（光谱和空间）的变换和特征融合来推理复杂数据结构——与“质谱结构推理”有方法论上的高度相似性。质谱数据同样具有多维特性（如质荷比m/z轴与强度轴，可能还有保留时间轴），并且从这些数据中推断分子结构也需要捕捉局部模式和全局依赖关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hyperspectral image classification (HSIC) has been significantly advanced by deep learning methods that exploit rich spatial-spectral correlations. However, existing approaches still face fundamental limitations: transformer-based models suffer from poor scalability due to the quadratic complexity of self-attention, while recent Fourier transform-based methods typically rely on 2D spatial FFTs and largely ignore critical inter-band spectral dependencies inherent to hyperspectral data. To address these challenges, we propose Hybrid GFNet (HGFNet), a novel architecture that integrates localized 3D convolutional feature extraction with frequency-domain global filtering via GFNet-style blocks for efficient and robust spatial-spectral representation learning. HGFNet introduces three complementary frequency transforms tailored to hyperspectral imagery: Spectral Fourier Transform (a 1D FFT along the spectral axis), Spatial Fourier Transform (a 2D FFT over spatial dimensions), and Spatial-Spatial Fourier Transform (a 3D FFT jointly over spectral and spatial dimensions), enabling comprehensive and high-dimensional frequency modeling. The 3D convolutional layers capture fine-grained local spatial-spectral structures, while the Fourier-based global filtering modules efficiently model long-range dependencies and suppress noise. To further mitigate the severe class imbalance commonly observed in HSIC, HGFNet incorporates an Adaptive Focal Loss (AFL) that dynamically adjusts class-wise focusing and weighting, improving discrimination for underrepresented classes.

</details>

---

### 40. [Cross-modal learning for plankton recognition](https://arxiv.org/abs/2603.16427)

**基本信息**

- 🔗 arXiv: [`2603.16427`](https://arxiv.org/abs/2603.16427)
- 👥 作者: Joona Kareinen, Veikka Immonen, Tuomas Eerola 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16427.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文专注于从多模态数据（图像+光学剖面/光谱类数据）中进行识别和推理，这与“质谱结构推理”中从质谱数据（一种光谱数据）推断结构或身份的任务在问题定义和方法论上高度相似。2) 数据资源相关：论文提出了一种利用未标注多模态数据构建识别模型的方法框架，这为质谱领域构建数据高效的推理模型提供了可借鉴的技术路径。

**📖 中文摘要**

本文研究利用自监督跨模态协调策略进行浮游生物识别。现代浮游生物成像仪器在收集大规模图像数据的同时，通常还补充有光学测量数据（如散射和荧光剖面）。目前，自动识别方法主要依赖于需要大量标注的监督方法，而这些测量数据在识别中并未被充分利用。受对比语言-图像预训练（CLIP）概念的启发，本文训练了两种模态（图像和剖面）的编码器，仅使用二元监督信息（指示给定的图像和剖面是否来自同一颗粒）进行训练。对于识别任务，则结合一个已知浮游生物物种的小型标注库和k-NN分类器。该方法产生了一个本质上是多模态的识别模型，能够利用从图像和剖面数据中提取的信息。论文表明，该方法在仅需极少标注图像的情况下实现了高识别精度，并且优于仅使用图像的自监督基线。这项工作展示了如何利用多模态数据（图像+光谱/剖面数据）通过自监督学习提升识别性能，为“质谱结构推理”中如何整合质谱数据与其他模态数据（如分子描述符、图像）提供了思路和范式参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper considers self-supervised cross-modal coordination as a strategy enabling utilization of multiple modalities and large volumes of unlabeled plankton data to build models for plankton recognition. Automated imaging instruments facilitate the continuous collection of plankton image data on a large scale. Current methods for automatic plankton image recognition rely primarily on supervised approaches, which require labeled training sets that are labor-intensive to collect. On the other hand, some modern plankton imaging instruments complement image information with optical measurement data, such as scatter and fluorescence profiles, which currently are not widely utilized in plankton recognition. In this work, we explore the possibility of using such measurement data to guide the learning process without requiring manual labeling. Inspired by the concepts behind Contrastive Language-Image Pre-training, we train encoders for both modalities using only binary supervisory information indicating whether a given image and profile originate from the same particle or from different particles. For plankton recognition, we employ a small labeled gallery of known plankton species combined with a $k$-NN classifier. This approach yields a recognition model that is inherently multimodal, i.e., capable of utilizing information extracted from both image and profile data. We demonstrate that the proposed method achieves high recognition accuracy while requiring only a minimal number of labeled images. Furthermore, we show that the approach outperforms an image-only self-supervised baseline. Code available at this https URL .

</details>

---

### 41. [Capability-Guided Compression: Toward Interpretability-Aware Budget Allocation for Large Language Models](https://arxiv.org/abs/2603.16440)

**基本信息**

- 🔗 arXiv: [`2603.16440`](https://arxiv.org/abs/2603.16440)
- 👥 作者: Rishaank Gupta
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16440.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何理解和优化大型语言模型（作为“大模型”的一种）的内部能力表示进行压缩，这与“化学大模型”主题中关于模型架构、能力分析和优化的讨论直接相关。

**📖 中文摘要**

这篇论文提出了能力引导压缩（CGC）框架，旨在解决大型语言模型压缩中的“能力盲”问题。作者认为，现有的压缩方法（如剪枝、量化、低秩分解）在分配压缩预算时，没有考虑模型不同组件所编码的功能能力。CGC框架利用稀疏自编码器（SAE）导出的“能力密度图”来为Transformer的不同组件分配差异化的压缩预算。能力密度结合了特征广度、激活熵和跨输入一致性等指标。论文从理论上证明了能力密度更高的组件具有更低的结构冗余，并在更低的压缩比下达到其个体相变点。实验在GPT-2 Medium上进行，表明能力密度与现有的重要性度量（如Wanda分数）正交。这项工作为化学信息学中构建和优化用于分子性质预测或结构推理的“化学大模型”提供了重要的方法论参考，特别是关于如何有选择性地压缩模型以保留关键化学推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model compression has made substantial progress through pruning, quantization, and low-rank decomposition, yet a fundamental limitation persists across all existing methods: compression budgets are allocated without any representation of what individual model components functionally encode. We term this the capability-blind compression problem and argue it is a root cause of two well-documented failures -- the insensitivity of perplexity-based evaluation to reasoning capability loss, and the abrupt phase transitions in model performance recently characterized by Ma et al. (2026). We propose Capability-Guided Compression (CGC), a framework that addresses this by using Sparse Autoencoder (SAE)-derived capability density maps to allocate differential compression budgets across transformer components. Capability density is a formally defined scalar measure combining the feature breadth, activation entropy, and cross-input consistency of a component's SAE feature activation distribution. We prove theoretically that components with higher capability density exhibit lower structural redundancy and reach their individual phase transition points at lower compression ratios, providing the first pre-compression mechanism for component-level phase transition prediction. Experiments on GPT-2 Medium confirm that capability density is statistically independent of Wanda importance scores (Spearman rho = -0.054, n = 384 heads), establishing it as a genuinely novel compression signal orthogonal to all existing importance metrics. We report a negative result on PPL-based compression comparison and provide a principled diagnosis identifying GPT-2 Medium as an insufficient test bed for the full CGC hypothesis. The theoretical framework, density formalism, and orthogonality finding constitute a foundation for capability-aware compression research.

</details>

---

### 42. [Understanding Cell Fate Decisions with Temporal Attention](https://arxiv.org/abs/2603.16562)

**基本信息**

- 🔗 arXiv: [`2603.16562`](https://arxiv.org/abs/2603.16562)
- 👥 作者: Florian Bürger, Martim Dias Gomes, Adrián E. Granada 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16562.pdf)

**💡 相关性分析**

满足标准1：论文的核心是使用基于注意力机制的Transformer模型处理高维时序科学数据（细胞图像），进行结局预测和机制推理。这种处理复杂科学数据序列并进行推理的范式，与“化学大模型”处理化学序列数据（如分子序列、反应路径）和“质谱结构推理”中可能涉及的时序质谱数据分析在方法论上高度相关。

**📖 中文摘要**

本文提出了一种基于深度学习的方法，用于从癌细胞群体在化疗处理下的长期活细胞记录原始图像序列中预测细胞命运。研究使用Transformer模型直接从原始图像序列预测细胞命运，而不依赖于预定义的形态学或分子特征。除了分类，论文还引入了一个全面的可解释性框架，用于解释引导模型预测的时空线索。实验表明，仅基于视频即可预测细胞结局，模型平衡准确率达到0.94，F1分数0.93。注意力和掩码实验进一步表明，预测细胞命运的信号并非唯一位于细胞轨迹的最后几帧，在事件发生前10小时即可进行可靠预测。分析揭示了有丝分裂和凋亡序列中预测信息的不同时间分布，以及细胞形态和p53信号在决定细胞结局中的作用。这项工作展示了基于注意力的时序模型能够实现准确的细胞命运预测，同时为细胞决策的非遗传决定因素提供生物学上可解释的见解。虽然应用领域是生物医学，但其核心方法——使用Transformer处理时序图像数据以进行结局预测和机制解释——与“化学大模型”中处理时序数据（如反应监测、动力学分析）以及“质谱结构推理”中可能需要处理与时间或过程相关的谱图序列具有方法论上的关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding non-genetic determinants of cell fate is critical for developing and improving cancer therapies, as genetically identical cells can exhibit divergent outcomes under the same treatment conditions. In this work, we present a deep learning approach for cell fate prediction from raw long-term live-cell recordings of cancer cell populations under chemotherapeutic treatment. Our Transformer model is trained to predict cell fate directly from raw image sequences, without relying on predefined morphological or molecular features. Beyond classification, we introduce a comprehensive explainability framework for interpreting the temporal and morphological cues guiding the model's predictions. We demonstrate that prediction of cell outcomes is possible based on the video only, our model achieves balanced accuracy of 0.94 and an F1-score of 0.93. Attention and masking experiments further indicate that the signal predictive of the cell fate is not uniquely located in the final frames of a cell trajectory, as reliable predictions are possible up to 10 h before the event. Our analysis reveals distinct temporal distribution of predictive information in the mitotic and apoptotic sequences, as well as the role of cell morphology and p53 signaling in determining cell outcomes. Together, these findings demonstrate that attention-based temporal models enable accurate cell fate prediction while providing biologically interpretable insights into non-genetic determinants of cellular decision-making. The code is available at this https URL .

</details>

---

### 43. [Manifold-Matching Autoencoders](https://arxiv.org/abs/2603.16568)

**基本信息**

- 🔗 arXiv: [`2603.16568`](https://arxiv.org/abs/2603.16568)
- 👥 作者: Laurent Cheret, Vincent Létourneau, Isar Nejadgholi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16568.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通过匹配潜在空间与数据空间成对距离来正则化表示学习的方法（MMAE）。该方法的核心理念——保持数据点之间的几何关系，对于“化学大模型”中学习有意义的分子表示，以及“质谱结构推理”中建立谱图与结构之间的稳健映射，具有直接的方法论参考价值。

**📖 中文摘要**

本文研究了一种称为流形匹配（MMAE）的自编码器简单无监督正则化方案：通过最小化均方误差，将潜在空间中的成对距离与输入数据空间中的成对距离对齐。由于对齐发生在成对距离而非坐标上，该方法可以扩展到数据的低维表示，增加了方法的灵活性。研究发现，这种正则化在基于最近邻距离保持和基于持续同调度量的指标上优于类似方法。作者还观察到MMAE提供了多维缩放（MDS）的可扩展近似。MMAE的核心思想是通过保持数据流形的几何结构（成对距离）来正则化自编码器的学习。这对于“化学大模型”和“质谱结构推理”具有重要意义：在化学信息学中，分子通常被表示为高维描述符或指纹，其内在的相似性/距离关系对于性质预测和结构分析至关重要。MMAE提供了一种在学习分子表示时显式保持分子间相似性结构的方法，有助于学习到更稳健、更具化学意义的低维嵌入，可用于下游的分子性质预测、聚类或结构推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study a simple unsupervised regularization scheme for autoencoders called Manifold-Matching (MMAE): we align the pairwise distances in the latent space to those of the input data space by minimizing mean squared error. Because alignment occurs on pairwise distances rather than coordinates, it can also be extended to a lower-dimensional representation of the data, adding flexibility to the method. We find that this regularization outperforms similar methods on metrics based on preservation of nearest-neighbor distances and persistent homology-based measures. We also observe that MMAE provides a scalable approximation of Multi-Dimensional Scaling (MDS).

</details>

---

### 44. [Deep Tabular Representation Corrector](https://arxiv.org/abs/2603.16569)

**基本信息**

- 🔗 arXiv: [`2603.16569`](https://arxiv.org/abs/2603.16569)
- 👥 作者: Hangting Ye, Peng Wang, Wei Fan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16569.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文提出了一种通用的、模型无关的表示增强框架，专门针对深度表格模型。化学信息学中大量数据以表格形式存在（分子描述符、实验数据），该框架可直接应用于提升化学预测模型的性能。2) 数据资源相关：论文提出的TRC方法本身是一个工具/框架，可用于改善处理表格型化学数据的模型表示，属于可用于相关主题的工具资源。

**📖 中文摘要**

本文提出了一种新颖的深度表格表示校正器（TRC），用于以模型无关的方式增强任何已训练的深度表格模型的表示，而无需更改其参数。具体来说，针对阻碍预测的表征偏移和表征冗余，作者提出了两个任务：（i）表格表示重估计：训练一个偏移估计器来计算表格表示的内在偏移，随后减轻它，从而重估表示；（ii）表格空间映射：通过坐标估计器将上述重估的表示转换到轻量嵌入向量空间，同时保留关键的预测信息以最小化冗余。这两个任务共同增强了深度表格模型的表示，且不触及原始模型，因此效率很高。实验在各种表格基准上对最先进的深度表格机器学习模型与TRC结合进行了广泛测试，显示出一致的优越性。这项工作为处理表格数据（化学信息学中常见的数据形式，如分子描述符表、物化性质表）的模型性能提升提供了通用工具。TRC框架可以应用于化学信息学中的QSAR/QSPR模型，帮助校正和提升基于深度学习的分子性质预测模型的表示能力，从而间接服务于“化学大模型”的构建和优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tabular data have been playing a mostly important role in diverse real-world fields, such as healthcare, engineering, finance, etc. The recent success of deep learning has fostered many deep networks (e.g., Transformer, ResNet) based tabular learning methods. Generally, existing deep tabular machine learning methods are along with the two paradigms, i.e., in-learning and pre-learning. In-learning methods need to train networks from scratch or impose extra constraints to regulate the representations which nonetheless train multiple tasks simultaneously and make learning more difficult, while pre-learning methods design several pretext tasks for pre-training and then conduct task-specific fine-tuning, which however need much extra training effort with prior knowledge. In this paper, we introduce a novel deep Tabular Representation Corrector, TRC, to enhance any trained deep tabular model's representations without altering its parameters in a model-agnostic manner. Specifically, targeting the representation shift and representation redundancy that hinder prediction, we propose two tasks, i.e., (i) Tabular Representation Re-estimation, that involves training a shift estimator to calculate the inherent shift of tabular representations to subsequently mitigate it, thereby re-estimating the representations and (ii) Tabular Space Mapping, that transforms the above re-estimated representations into a light-embedding vector space via a coordinate estimator while preserves crucial predictive information to minimize redundancy. The two tasks jointly enhance the representations of deep tabular models without touching on the original models thus enjoying high efficiency. Finally, we conduct extensive experiments on state-of-the-art deep tabular machine learning models coupled with TRC on various tabular benchmarks which have shown consistent superiority.

</details>

---

### 45. [Trajectory-Optimized Time Reparameterization for Learning-Compatible Reduced-Order Modeling of Stiff Dynamical Systems](https://arxiv.org/abs/2603.16583)

**基本信息**

- 🔗 arXiv: [`2603.16583`](https://arxiv.org/abs/2603.16583)
- 👥 作者: Joe Standridge, Daniel Livescu, Paul Cizmas
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对刚性动力系统（包括化学动力学模型）提出一种改进的机器学习降阶建模方法。这直接与“化学大模型”中一个关键的子方向——构建能够准确、高效模拟化学动力学过程的可计算模型——高度相关。

**📖 中文摘要**

本文研究了时间重参数化（TR）作为缓解刚性动力系统机器学习降阶模型（ML-ROM）中刚度问题的机制，并提出了轨迹优化时间重参数化（TOTR）公式。刚性系统对ML-ROM构成挑战，因为显式时间积分在刚性区域变得不稳定，而在学习循环中进行隐式积分计算成本高且通常降低训练效率。TR通过变换自变量，使得快速的物理时间瞬态过程在拉伸的时间坐标上展开，从而使得在均匀采样网格上进行稳定的显式积分成为可能。本文提出的TOTR方法将时间重参数化表述为弧长坐标中的优化问题，其中选择遍历速度剖面以惩罚拉伸时间中的加速度。通过针对训练动态的平滑性，该公式产生的重参数化轨迹比现有TR方法条件更好、更易于学习。在参数化刚性线性系统、van der Pol振荡器和HIRES化学动力学模型三个刚性问题上进行了评估。结果表明，TOTR在所有情况下都能产生更平滑的重参数化和在相同训练方案下改进的物理时间预测。这项工作为处理多尺度动力系统的显式降阶建模提供了稳健框架。化学动力学系统（如反应网络）通常是刚性的，因此该研究为在“化学大模型”背景下构建能够模拟复杂化学反应动力学的可学习模型提供了重要的数值方法和理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Stiff dynamical systems present a challenge for machine-learning reduced-order models (ML-ROMs), as explicit time integration becomes unstable in stiff regimes while implicit integration within learning loops is computationally expensive and often degrades training efficiency. Time reparameterization (TR) offers an alternative by transforming the independent variable so that rapid physical-time transients are spread over a stretched-time coordinate, enabling stable explicit integration on uniformly sampled grids. Although several TR strategies have been proposed, their effect on learnability in ML-ROMs remains incompletely understood. This work investigates time reparameterization as a stiffness-mitigation mechanism for neural ODE reduced-order modeling and introduces a trajectory-optimized TR (TOTR) formulation. The proposed approach casts time reparameterization as an optimization problem in arc-length coordinates, in which a traversal-speed profile is selected to penalize acceleration in stretched time. By targeting the smoothness of the training dynamics, this formulation produces reparameterized trajectories that are better conditioned and easier to learn than existing TR methods. TOTR is evaluated on three stiff problems: a parameterized stiff linear system, the van der Pol oscillator, and the HIRES chemical kinetics model. Across all cases, the proposed approach yields smoother reparameterizations and improved physical-time predictions under identical training regimens than other TR approaches. Quantitative results demonstrate loss reductions of one to two orders of magnitude compared to benchmark algorithms. These results highlight that effective stiffness mitigation in ML-ROMs depends critically on the regularity and learnability of the time map itself, and that optimization-based TR provides a robust framework for explicit reduced-order modeling of multiscale dynamical systems.

</details>

---

### 46. [On the Transfer of Collinearity to Computer Vision](https://arxiv.org/abs/2603.16592)

**基本信息**

- 🔗 arXiv: [`2603.16592`](https://arxiv.org/abs/2603.16592)
- 👥 作者: Frederik Beuth, Danny Kowerko
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16592.pdf)

**💡 相关性分析**

满足标准1：论文的核心是研究一种特定的几何感知先验（共线性）及其在结构化模式识别中的应用。虽然应用领域是图像，但其方法论思想（利用对齐、规律性先验进行推理）与“质谱结构推理”中识别质谱峰模式、同位素簇等具有概念上的相关性，为后者提供了潜在的启发。

**📖 中文摘要**

本文探讨了将人类视觉中的“共线性”现象转移到计算机视觉中。共线性是一种视觉感知现象，能增强沿直线排列的空间对齐边缘。作者开发了一个原型模型来例证该原理，并系统测试了其在四个用例中的潜力。用例选择涵盖了广泛的应用场景：将共线性与深度学习结合（用例I和II）、将共线性与显著性模型结合（用例II）以及作为特征检测器（用例I）。在第一个用例中，发现共线性能够改进晶圆的缺陷检测，通过共线性使性能提高了1.24倍（错误率从6.5%降至5.26%）。在第二个用例中，测试了纳米技术材料中的缺陷识别，通过共线性实现了3.2倍的性能提升（深度学习，错误率从21.65%降至6.64%）。作为第三个实验，涵盖了遮挡情况；第四个实验测试了ImageNet。作者得出结论，共线性可能适用于工业应用，因为感兴趣的图像结构通常是人为的，通常由线条组成。虽然论文应用在图像处理，但其核心思想——利用特定的几何先验（共线性）来增强对结构化模式（如线条、边缘）的检测和推理——与“质谱结构推理”有潜在关联。质谱图中的峰位、同位素模式等也呈现出特定的“共线性”或对齐模式（如在m/z轴上的规律间隔），利用类似的几何先验可能有助于从噪声中识别特征峰或解析复杂谱图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Collinearity is a visual perception phenomenon in the human brain that amplifies spatially aligned edges arranged along a straight line. However, it is vague for which purpose humans might have this principle in the real-world, and its utilization in computer vision and engineering applications even is a largely unexplored field. In this work, our goal is to transfer the collinearity principle to computer vision, and we explore the potential usages of this novel principle for computer vision applications. We developed a prototype model to exemplify the principle, then tested it systematically, and benchmarked it in the context of four use cases. Our cases are selected to spawn a broad range of potential applications and scenarios: sketching the combination of collinearity with deep learning (case I and II), using collinearity with saliency models (case II), and as a feature detector (case I). In the first use case, we found that collinearity is able to improve the fault detection of wafers and obtain a performance increase by a factor 1.24 via collinearity (decrease of the error rate from 6.5% to 5.26%). In the second use case, we test the defect recognition in nanotechnology materials and achieve a performance increase by 3.2x via collinearity (deep learning, error from 21.65% to 6.64%), and also explore saliency models. As third experiment, we cover occlusions; while as fourth experiment, we test ImageNet and observe that it might not be very beneficial for ImageNet. Therefore, we can assemble a list of scenarios for which collinearity is beneficial (wafers, nanotechnology, occlusions), and for what is not beneficial (ImageNet). Hence, we infer collinearity might be suitable for industry applications as it helps if the image structures of interest are man-made because they often consist of lines. Our work provides another tool for CV, hope to capture the power of human processing.

</details>

---

### 47. [Machines acquire scientific taste from institutional traces](https://arxiv.org/abs/2603.16659)

**基本信息**

- 🔗 arXiv: [`2603.16659`](https://arxiv.org/abs/2603.16659)
- 👥 作者: Ziqin Gong, Ning Li, Huaikang Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16659.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容直接围绕如何利用大语言模型（化学大模型的一种）从科学文献数据中学习高级评估能力（科学品味），这属于化学信息学中利用AI模型处理和分析科学数据与知识的范畴。

**📖 中文摘要**

这篇论文探讨了人工智能如何从科学机构的出版记录中学习“科学品味”——即判断哪些未经验证的想法值得追求的评估能力。作者发现，在管理学和经济学领域，对期刊发表决策进行微调的语言模型，在评估研究提案质量方面，其表现超越了前沿大模型和人类专家小组。这项工作表明，科学品味并非AI无法触及，而是沉积在制度记录中等待提取。这为在质量难以形式化验证的学科中，大规模筛选不断增长的科学产出提供了一种可扩展的机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Artificial intelligence matches or exceeds human performance on tasks with verifiable answers, from protein folding to Olympiad mathematics. Yet the capacity that most governs scientific advance is not reasoning but taste: the ability to judge which untested ideas deserve pursuit, exercised daily by editors and funders but never successfully articulated, taught, or automated. Here we show that fine-tuning language models on journal publication decisions recovers evaluative judgment inaccessible to both frontier models and human expertise. Using a held-out benchmark of research pitches in management spanning four quality tiers, we find that eleven frontier models, spanning major proprietary and open architectures, barely exceed chance, averaging 31% accuracy. Panels of journal editors and editorial board members reach 42% by majority vote. Fine-tuned models trained on years of publication records each surpass every frontier model and expert panel, with the best single model achieving 59%. These models exhibit calibrated confidence, reaching 100% accuracy on their highest-confidence predictions, and transfer this evaluative signal to untrained pairwise comparisons and one-sentence summaries. The mechanism generalizes: models trained on economics publication records achieve 70% accuracy. Scientific taste was not missing from AI's reach; it was deposited in the institutional record, waiting to be extracted. These results provide a scalable mechanism to triage the expanding volume of scientific production across disciplines where quality resists formal verification.

</details>

---

### 48. [Evaluating Latent Space Structure in Timbre VAEs: A Comparative Study of Unsupervised, Descriptor-Conditioned, and Perceptual Feature-Conditioned Models](https://arxiv.org/abs/2603.16713)

**基本信息**

- 🔗 arXiv: [`2603.16713`](https://arxiv.org/abs/2603.16713)
- 👥 作者: Joseph Cameron, Alan Blackwell
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16713.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个带有语义描述符标注的、用于音色建模和生成的专用数据集（电吉他声音数据集）。该数据集作为一项数据资源，可用于训练和评估与“化学大模型”在概念上相似的、用于分子或材料性质（如光谱、气味）生成与分析的生成模型。

**📖 中文摘要**

本研究对三种用于音乐音色生成的变分自编码器（VAE）的潜在空间结构进行了比较评估：无监督VAE、描述符条件VAE以及基于AudioCommons音色模型的连续感知特征条件VAE。研究使用了一个包含19个语义描述符的标注电吉他声音数据集，并通过一系列聚类和可解释性指标（如轮廓分数、音色描述符紧密度、音高条件分离度等）评估了每个模型的潜在结构。结果表明，基于连续感知特征进行条件化的模型，其潜在空间更加紧凑、具有判别力且对音高变化不敏感，性能优于无监督和离散描述符条件模型。这项工作为评估音色潜在空间提供了方法论工具，有助于开发更可控、可解释的生成音频模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a comparative evaluation of latent space organization in three Variational Autoencoders (VAEs) for musical timbre generation: an unsupervised VAE, a descriptor-conditioned VAE, and a VAE conditioned on continuous perceptual features from the AudioCommons timbral models. Using a curated dataset of electric guitar sounds labeled with 19 semantic descriptors across four intensity levels, we assess each model's latent structure with a suite of clustering and interpretability metrics. These include silhouette scores, timbre descriptor compactness, pitch-conditional separation, trajectory linearity, and cross-pitch consistency. Our findings show that conditioning on perceptual features yields a more compact, discriminative, and pitch-invariant latent space, outperforming both the unsupervised and discrete descriptor-conditioned models. This work highlights the limitations of one-hot semantic conditioning and provides methodological tools for evaluating timbre latent spaces, contributing to the development of more controllable and interpretable generative audio models.

</details>

---

### 49. [Novelty-Driven Target-Space Discovery in Automated Electron and Scanning Probe Microscopy](https://arxiv.org/abs/2603.16715)

**基本信息**

- 🔗 arXiv: [`2603.16715`](https://arxiv.org/abs/2603.16715)
- 👥 作者: Utkarsh Pratiush, Kamyar Barakati, Boris N. Slautin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16715.pdf)

**💡 相关性分析**

满足标准2：论文提出并实现了一个用于自动化科学发现（在显微镜领域）的AI框架和算法。该框架的核心思想——学习结构-性质关系并主动探索——与“化学大模型”和“质谱结构推理”中利用AI模型从数据中学习并预测分子结构或性质的目标高度相关，可视为一种方法论工具。

**📖 中文摘要**

本研究开发了一个基于深度核学习的BEACON框架，旨在通过主动搜索新的行为模式来指导自动化显微镜实验中的目标空间发现。该方法在实验过程中学习结构-性质关系，并利用这个不断演化的模型来寻找多样化的响应机制。研究首先在预采集的真实数据集上建立了演示工作流程，从而能够与经典采集策略进行直接基准测试。随后，该方法在扫描透射电子显微镜（STEM）上进行了实际部署和操作。这项工作为评估发现驱动算法提供了一个实用基础，并支持社区采用和扩展该方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern automated microscopy faces a fundamental discovery challenge: in many systems, the most important scientific information does not reside in the immediately visible image features, but in the target space of sequentially acquired spectra or functional responses, making it essential to develop strategies that can actively search for new behaviors rather than simply optimize known objectives. Here, we developed a deep-kernel-learning BEACON framework that is explicitly designed to guide discovery in the target space by learning structure-property relationships during the experiment and using that evolving model to seek diverse response regimes. We first established the method through demonstration workflows built on pre-acquired ground-truth datasets, which enabled direct benchmarking against classical acquisition strategies and allowed us to define a set of monitoring functions for comparing exploration quality, target-space coverage, and surrogate-model behavior in a transparent and reproducible manner. This benchmarking framework provides a practical basis for evaluating discovery-driven algorithms, not just optimization performance. We then operationalized and deployed the workflow on STEM, showing that the approach can transition from offline validation to real experimental implementation. To support adoption and extension by the broader community, the associated notebooks are available, allowing users to reproduce the workflows, test the benchmarks, and adapt the method to their own instruments and datasets.

</details>

---

### 50. [MedCL-Bench: Benchmarking stability-efficiency trade-offs and scaling in biomedical continual learning](https://arxiv.org/abs/2603.16738)

**基本信息**

- 🔗 arXiv: [`2603.16738`](https://arxiv.org/abs/2603.16738)
- 👥 作者: Min Zeng, Shuang Zhou, Zaifu Zhan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16738.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于评估生物医学领域语言模型（可视为化学/生物医学大模型的一个子类）持续学习性能的基准（MedCL-Bench），包含多个数据集和评估协议，是一项重要的评估资源和工具。

**📖 中文摘要**

本研究引入了MedCL-Bench，这是一个用于评估生物医学自然语言处理（NLP）中持续学习性能的统一基准。它流式传输十个涵盖五个任务系列的生物医学NLP数据集，并在八个任务顺序下评估十一种持续学习策略，报告保留率、迁移性和GPU小时成本。该基准提供了在标准化协议下评估模型更新的可重复框架，对于审计部署前的模型更新至关重要。这项工作建立了一个用于生物医学语言模型（可视为特定领域的“化学大模型”）持续学习的评估框架和基准数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medical language models must be updated as evidence and terminology evolve, yet sequential updating can trigger catastrophic forgetting. Although biomedical NLP has many static benchmarks, no unified, task-diverse benchmark exists for evaluating continual learning under standardized protocols, robustness to task order and compute-aware reporting. We introduce MedCL-Bench, which streams ten biomedical NLP datasets spanning five task families and evaluates eleven continual learning strategies across eight task orders, reporting retention, transfer, and GPU-hour cost. Across backbones and task orders, direct sequential fine-tuning on incoming tasks induces catastrophic forgetting, causing update-induced performance regressions on prior tasks. Continual learning methods occupy distinct retention-compute frontiers: parameter-isolation provides the best retention per GPU-hour, replay offers strong protection at higher cost, and regularization yields limited benefit. Forgetting is task-dependent, with multi-label topic classification most vulnerable and constrained-output tasks more robust. MedCL-Bench provides a reproducible framework for auditing model updates before deployment.

</details>

---

### 51. [SpecMoE: Spectral Mixture-of-Experts Foundation Model for Cross-Species EEG Decoding](https://arxiv.org/abs/2603.16739)

**基本信息**

- 🔗 arXiv: [`2603.16739`](https://arxiv.org/abs/2603.16739)
- 👥 作者: D. Darankoum, C. Habermacher, J. Volle 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16739.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是开发一个用于光谱数据（脑电图STFT谱）解码和分析的基础模型（SpecMoE）。虽然应用领域是神经科学，但其处理光谱数据、学习谱模式、并进行跨领域泛化的方法论，与“质谱结构推理”中处理质谱数据、学习谱峰与结构关系、并进行化合物识别的核心任务在技术路径上高度相似，可视为同一类机器学习问题在不同光谱模态上的应用。

**📖 中文摘要**

本研究引入了SpecMoE，一个用于跨物种脑电图（EEG）解码的谱混合专家基础模型。该模型采用一种新颖的、应用于短时傅里叶变换（STFT）图谱的高斯平滑掩码方案，并结合时间、频率和时频联合掩码，迫使模型学习跨高、低频域的复杂神经模式。为了有效恢复信号，设计了SpecHi-Net架构。为了加速大规模预训练，将数据分成三个子集分别训练独立的专家模型，然后通过一个由学习的谱门控机制引导的混合专家框架（SpecMoE）进行组合。SpecMoE在一系列EEG解码任务上实现了最先进的性能，并展示了强大的跨物种和跨被试泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Decoding the orchestration of neural activity in electroencephalography (EEG) signals is a central challenge in bridging neuroscience with artificial intelligence. Foundation models have made strides in generalized EEG decoding, yet many existing frameworks primarily relying on separate temporal and spectral masking of raw signals during self-supervised pretraining. Such strategies often tend to bias learning toward high-frequency oscillations, as low-frequency rhythmic patterns can be easily inferred from the unmasked signal. We introduce a foundation model that utilizes a novel Gaussian-smoothed masking scheme applied to short-time Fourier transform (STFT) maps. By jointly applying time, frequency, and time-frequency Gaussian masks, we make the reconstruction task much more challenging, forcing the model to learn intricate neural patterns across both high- and low-frequency domains. To effectively recover signals under this aggressive masking strategy, we design SpecHi-Net, a U-shaped hierarchical architecture with multiple encoding and decoding stages. To accelerate large-scale pretraining, we partition the data into three subsets, each used to train an independent expert model. We then combine these models through SpecMoE, a mixture of experts framework guided by a learned spectral gating mechanism. SpecMoE achieves state-of-the-art performance across a diverse set of EEG decoding tasks, including sleep staging, emotion recognition, motor imagery classification, abnormal signal detection, and drug effect prediction. Importantly, the model demonstrates strong cross-species and cross-subject generalization, maintaining high accuracy on both human and murine EEG datasets.

</details>

---

### 52. [Bayesian Inference of Psychometric Variables From Brain and Behavior in Implicit Association Tests](https://arxiv.org/abs/2603.16741)

**基本信息**

- 🔗 arXiv: [`2603.16741`](https://arxiv.org/abs/2603.16741)
- 👥 作者: Christian A. Kothe, Sean Mullen, Michael V. Bronstein 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16741.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的、用于从多模态数据（包括可能的光谱/神经信号）中推断性质的贝叶斯建模框架。这种从复杂数据中推理潜在变量的方法论，与“质谱结构推理”中从质谱数据推断分子结构的统计建模思想相通，可视为一种相关的数据分析工具或方法。

**📖 中文摘要**

本研究建立了一种从内隐联想测试（IAT）产生的神经和行为数据中推断心理健康相关心理测量变量的原则性方法。我们提出了一个稀疏分层贝叶斯模型，该模型利用多模态数据来预测新参与者与精神疾病症状相关的体验。该模型是D-score（一种仅依赖反应时的金标准方法）的多元泛化，并具有可训练参数，针对IAT研究典型的小队列 regime 进行了参数效率优化。分析的数据来自两个IAT变体：与自杀风险相关的E-IAT和与精神病相关的PSY-IAT。结果表明，该框架在增强基于IAT的评估方面显示出潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Objective. We establish a principled method for inferring mental health related psychometric variables from neural and behavioral data using the Implicit Association Test (IAT) as the data generation engine, aiming to overcome the limited predictive performance (typically under 0.7 AUC) of the gold-standard D-score method, which relies solely on reaction times. Approach. We propose a sparse hierarchical Bayesian model that leverages multi-modal data to predict experiences related to mental illness symptoms in new participants. The model is a multivariate generalization of the D-score with trainable parameters, engineered for parameter efficiency in the small-cohort regime typical of IAT studies. Data from two IAT variants were analyzed: a suicidality-related E-IAT ($n=39$) and a psychosis-related PSY-IAT ($n=34$). Main Results. Our approach overcomes a high inter-individual variability and low within-session effect size in the dataset, reaching AUCs of 0.73 (E-IAT) and 0.76 (PSY-IAT) in the best modality configurations, though corrected 95% confidence intervals are wide ($\pm 0.18$) and results are marginally significant after FDR correction ($q=0.10$). Restricting the E-IAT to MDD participants improves AUC to 0.79 $[0.62, 0.97]$ (significant at $q=0.05$). Performance is on par with the best reference methods (shrinkage LDA and EEGNet) for each task, even when the latter were adapted to the task, while the proposed method was not. Accuracy was substantially above near-chance D-scores (0.50-0.53 AUC) in both tasks, with more consistent cross-task performance than any single reference method. Significance. Our framework shows promise for enhancing IAT-based assessment of experiences related to entrapment and psychosis, and potentially other mental health conditions, though further validation on larger and independent cohorts will be needed to establish clinical utility.

</details>

---

### 53. [pADAM: A Plug-and-Play All-in-One Diffusion Architecture for Multi-Physics Learning](https://arxiv.org/abs/2603.16757)

**基本信息**

- 🔗 arXiv: [`2603.16757`](https://arxiv.org/abs/2603.16757)
- 👥 作者: Amirhossein Mollaali, Bongseok Kim, Christian Moya 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16757.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是开发一个用于多物理场学习的统一生成式基础模型（pADAM）。该模型能够进行前向预测、逆向推断和不确定性量化，其“从数据中学习物理规律并用于推理”的核心范式，与“化学大模型”旨在从化学数据中学习并预测分子性质、反应或结构的愿景高度一致，是化学科学领域AI基础模型的一个紧密相关范例。

**📖 中文摘要**

本研究引入了pADAM，一个统一的生成式框架，用于跨异构偏微分方程族学习共享的概率先验。通过学习系统状态和（如适用）物理参数的联合分布，pADAM支持在单一架构内进行前向预测和逆向推断，而无需重新训练。在从标量扩散到非线性Navier-Stokes方程的基准测试中，pADAM即使在稀疏观测下也能实现准确的推断。结合保形预测，它还提供了具有覆盖保证的可靠不确定性量化。此外，pADAM仅从两个稀疏快照执行概率模型选择，通过其学习的生成表示识别控制定律。这些结果突显了生成式多物理建模在统一和不确定性感知的科学推断方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generalizing across disparate physical laws remains a fundamental challenge for artificial intelligence in science. Existing deep-learning solvers are largely confined to single-equation settings, limiting transfer across physical regimes and inference tasks. Here we introduce pADAM, a unified generative framework that learns a shared probabilistic prior across heterogeneous partial differential equation families. Through a learned joint distribution of system states and, where applicable, physical parameters, pADAM supports forward prediction and inverse inference within a single architecture without retraining. Across benchmarks ranging from scalar diffusion to nonlinear Navier--Stokes equations, pADAM achieves accurate inference even under sparse observations. Combined with conformal prediction, it also provides reliable uncertainty quantification with coverage guarantees. In addition, pADAM performs probabilistic model selection from only two sparse snapshots, identifying governing laws through its learned generative representation. These results highlight the potential of generative multi-physics modeling for unified and uncertainty-aware scientific inference.

</details>

---

### 54. [Machine Learning Based Identification of Solvents from Post-Desiccation Patterns](https://arxiv.org/abs/2603.15660)

**基本信息**

- 🔗 arXiv: [`2603.15660`](https://arxiv.org/abs/2603.15660)
- 👥 作者: Jesús Israel Morán-Cortés, Felipe Pacheco-Vázquez
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15660.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用机器学习（人工神经网络）从干燥裂纹图案中识别溶剂，这属于化学信息学中数据分析和模式识别的典型应用。

**📖 中文摘要**

本文提出了一种基于人工神经网络（ANN）的优化协议，用于从淀粉-液体浆料干燥后形成的裂纹图案中识别所涉及的溶剂。该研究属于化学信息学领域，因为它利用图像分析技术从干燥过程中产生的形态特征（如尺寸、形状、几何和取向）中提取数据，并训练神经网络模型进行模式识别和溶剂分类。该方法的核心是数据驱动的模式识别，旨在通过分析复杂的物理化学过程（干燥开裂）产生的数据来推断原始化学组成（溶剂类型）。实验对单一溶剂（水、乙醇、丙酮）和双组分溶剂（水-乙醇混合物）进行了测试，平均识别准确率达到96%。这项工作展示了机器学习在从复杂实验观测中提取化学信息方面的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce an optimized protocol of fracture pattern classification using an artificial neural network to identify the solvent involved in the desiccation cracking process of starch-liquid slurries, even after it has been completely evaporated. For this purpose, image analysis techniques were used to characterize patterns obtained from drying suspensions using single solvents (water, ethanol, acetone) and two-component solvents (water-ethanol mixtures at different concentrations). Frequency histograms were generated based on nine morphological features, taking into account their size, shape, geometry and orientational ordering. Subsequently, we used these histograms as input data into artificial neural network variants to determine the set of features that lead to the higher accuracy in solvent identification. We obtained an average accuracy of $96(\pm 1)\%$ considering all solvents in the analysis. The highest accuracy was obtained with sets of features that include the crack area distribution. The proposed protocol can help to determine the combination of features that optimize pattern recognition in other fields of science and engineering.

</details>

---

### 55. [Life cycle assessment for all organic chemicals](https://arxiv.org/abs/2603.15686)

**基本信息**

- 🔗 arXiv: [`2603.15686`](https://arxiv.org/abs/2603.15686)
- 👥 作者: Shaohan Chen, Tim Langhorst, Julian Nöhl 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15686.pdf)

**💡 相关性分析**

满足标准2：论文提出了CRYSTAL框架，并创建了一个大规模、透明的有机化学品生命周期清单数据库，这为化学信息学和大模型训练提供了重要的数据集和工具资源。

**📖 中文摘要**

本文提出了CRYSTAL（Chemical RetrosYnthesiS for Transparent Assessment of Life-cycles）框架，这是一个用于自动生成有机化学品透明生命周期清单（LCI）数据的系统。该框架结合了逆合成分析和机器学习预测的门到门清单，能够仅根据分子结构生成一致且透明的LCI数据。利用CRYSTAL，作者创建了一个包含超过70,000种有机化学品、涵盖110,000多个LCI数据集的数据库，量化了原料和能源需求、辅助材料、生物圈流动和废物流动。这项工作为化学信息学和大规模数据驱动分析提供了强大的工具和资源，旨在解决当前化学品生命周期评估中数据覆盖有限、不一致和不透明的问题。通过识别关键的环境热点和枢纽化学品，该框架为有针对性的工程和政策干预提供了系统指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemicals are embedded in nearly every aspect of modern society, yet their production poses substantial sustainability concerns. Achieving a sustainable chemical industry requires detailed Life Cycle Assessment (LCA); however, current assessments face many unknowns due to limited, partly inconsistent, and untransparent data coverage since existing Life Cycle Inventory (LCI) databases account for only a tiny fraction of traded chemicals. Here, we introduce the Chemical RetrosYnthesiS for Transparent Assessment of Life-cycles (CRYSTAL) framework, which automatically generates consistent and transparent LCI data for organic chemicals based on their molecular structure using retrosynthesis and machine-learned gate-to-gate inventories. Using the predictive power of CRYSTAL, we create a consistent database for more than 70000 organic chemicals, comprising over 110000 transparent LCI datasets that quantify both feedstock and energy demands, together with associated auxiliary materials, biosphere flows, and waste flows. From this comprehensive database, we identify 50 key environmental hotspots driving high impacts of organic chemical production across multiple environmental categories and pivotal hub chemicals that are most critical for downstream chemical production. In providing this comprehensive data foundation, the CRYSTAL framework offers systematic guidance for targeted engineering and policy interventions. Its transparent, modular nature is designed to shift chemical LCA from a reliance on "unknown unknowns" to a collaboratively improvable mapping of "known unknowns".

</details>

---

### 56. [LLM-Driven Discovery of High-Entropy Catalysts via Retrieval-Augmented Generation](https://arxiv.org/abs/2603.15712)

**基本信息**

- 🔗 arXiv: [`2603.15712`](https://arxiv.org/abs/2603.15712)
- 👥 作者: AI Scientists, Xinyi Lin, Danqing Yin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15712.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心内容是使用检索增强生成（RAG）的大型语言模型（化学大模型）来驱动催化剂发现，这直接围绕“化学大模型”主题。同时，它利用并整合了大规模材料数据库，提供了数据驱动的探索工具。

**📖 中文摘要**

本文介绍了一个基于检索增强生成（RAG）的大型语言模型（LLM）框架，用于加速二氧化碳还原催化剂的高通量发现。该框架使GPT-4能够访问包含50,000多种已知材料的数据集，从而在物理约束的指导下探索化学空间。该系统生成了250多种催化剂候选物，其中82%具有热力学稳定性，并且许多满足了成本、导电性和机械稳定性的多目标约束。最佳性能的催化剂在限制电位上比基准IrO2提高了25%。该工作展示了如何将自然语言界面与检索增强相结合，将AI的创造力扎根于物理约束中，从而显著提高材料发现的效率（相比传统高通量筛选提高了200倍计算效率）。这体现了化学大模型（LLM）在辅助科学发现和结果解释方面的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

CO2 reduction requires efficient catalysts, yet materials discovery remains bottlenecked by 10-20 year development cycles requiring deep domain expertise. This paper demonstrates how large language models can assist the catalyst discovery process by helping researchers explore chemical spaces and interpret results when augmented with retrieval-based grounding. We introduce a retrieval-augmented generation framework that enables GPT-4 to navigate chemical space by accessing a database of 50,000+ known materials, adapting general-purpose language understanding for high-throughput materials design. Our approach generated over 250 catalyst candidates with an 82% thermodynamic stability rate while addressing multi-objective constraints: 68% achieved <$100/kg cost with metallic conductivity (band gap<0.1eV) and mechanical stability (B/G>1.75). The best-performing Fe0.2Co0.2Ni0.2Ir0.1Ru0.3 achieves 0.285V limiting potential (25% improvement over IrO2), while Cr0.2Fe0.2Co0.3Ni0.2Mo0.1 optimally balances performance-cost trade-offs at $18/kg. Volcano plot analysis confirms that 78% of LLM-generated catalysts cluster near the theoretical activity optimum, while our system achieves 200x computational efficiency compared to traditional high-throughput screening. By demonstrating that retrieval-augmented generation can ground AI creativity in physical constraints without sacrificing exploration, this work demonstrates an approach where natural language interfaces can streamline materials discovery workflows, enabling researchers to explore chemical spaces more efficiently while the LLM assists in result interpretation and hypothesis generation.

</details>

---

### 57. [3D tomography of exchange phase in a Si/SiGe quantum dot device](https://arxiv.org/abs/2603.16025)

**基本信息**

- 🔗 arXiv: [`2603.16025`](https://arxiv.org/abs/2603.16025)
- 👥 作者: Dylan Albrecht, Sarah Thompson, N. Tobias Jacobson 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16025.pdf)

**💡 相关性分析**

满足标准1：论文的核心是从实验数据中逆向提取和解释物理参数（交换相位），其数据处理、信号分析和模型构建的方法论与质谱结构推理中从谱图推断分子结构有概念上的相似性，属于广义的“结构推理”范畴。

**📖 中文摘要**

本文提出了一种从实验数据中三维层析提取交换相互作用累积相位的方法，用于硅/硅锗量子点器件。研究涉及处理来自量子比特相干测量的调制余弦信号，以揭示底层物理参数。作者结合了来自多个领域的技术（如相位偏移数字全息术中的包裹相位测量、基于最大流/最小割的相位展开方法PUMA），在三维电压空间中稳健地提取和建模相位体积。该方法旨在为理解器件可变性、校准器件模型以及优化量子比特控制提供详细信息。虽然主要应用于量子计算，但其中从复杂、有噪声的实验数据中提取和解释物理参数（如相位）的数据处理和分析流程，与化学信息学和质谱分析中从复杂信号推断结构信息的精神相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The exchange interaction is a foundational building block for the operation of spin-based quantum processors. Extracting the exchange interaction coefficient $J(\mathbf{V})$, as a function of gate electrode voltages, is important for understanding disorder, faithfully simulating device performance, and operating spin qubits with high fidelity. Typical coherent measurements of exchange in spin qubit devices yield a modulated cosine of an accumulated phase, which in turn is the time integral of exchange. As such, extracting $J(\mathbf{V})$ from experimental data is difficult due to the ambiguity of inverting a cosine, the sensitivity to noise when unwrapping phase, as well as the problem of inverting the integral. As a step toward obtaining $J(\mathbf{V})$, we tackle the first two challenges to reveal the accumulated phase, $\phi(\mathbf{V})$. We incorporate techniques from a wide range of fields to robustly extract and model a 3D phase volume for spin qubit devices from a sequence of 2D measurements. In particular, we present a measurement technique to obtain the wrapped phase, as done in phase-shifting digital holography, and utilize the max-flow/min-cut phase unwrapping method (PUMA) to unwrap the phase in 3D voltage space. We show this method is robust to the minimal observed drift in the device, which we confirm by increasing scan resolution. Upon building a model of the extracted phase, we optimize over the model to locate a minimal-gradient $\pi$ exchange pulse point in voltage space. Our measurement protocol may provide detailed information useful for understanding the origins of device variability governing device yield, enable calibrating device models to specific devices during operation for more sophisticated error attribution, and enable a systematic optimization of qubit control. We anticipate that the methods presented here may be applicable to other qubit platforms.

</details>

---

### 58. [Deep Adaptive Model-Based Design of Experiments](https://arxiv.org/abs/2603.16146)

**基本信息**

- 🔗 arXiv: [`2603.16146`](https://arxiv.org/abs/2603.16146)
- 👥 作者: Arno Strouwen, Sebastian Micluţa-Câmpeanu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16146.pdf)

**💡 相关性分析**

满足标准1：论文将深度学习（Transformer）与机理模型结合，用于自动化实验设计和参数估计，这属于化学信息学中“化学大模型”在优化和控制复杂化学/生物过程方面的应用。

**📖 中文摘要**

本文提出了一种结合深度自适应设计（DAD）与可微分机理模型的深度自适应模型实验设计（MBDOE）方法，用于非线性动力系统的参数估计。该方法将序列实验设计摊销到一个离线训练的神经网络策略中，从而避免了传统自适应MBDOE在每一步实验后都需要进行昂贵的后验推断和设计优化的问题。作者针对具有已知控制方程但参数不确定的动力系统，扩展了序列对比训练目标以处理冗余参数，并提出了一个尊重动力系统时间结构的基于Transformer的策略架构。该方法在具有Monod动力学的补料分批生物反应器、具有不确定底物抑制的Haldane生物反应器等系统上进行了演示。这项工作展示了深度学习（特别是Transformer架构）与机理模型相结合，用于优化实验设计和参数估计，属于化学信息学中“化学大模型”与自动化实验、过程分析相结合的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Model-based design of experiments (MBDOE) is essential for efficient parameter estimation in nonlinear dynamical systems. However, conventional adaptive MBDOE requires costly posterior inference and design optimization between each experimental step, precluding real-time applications. We address this by combining Deep Adaptive Design (DAD), which amortizes sequential design into a neural network policy trained offline, with differentiable mechanistic models. For dynamical systems with known governing equations but uncertain parameters, we extend sequential contrastive training objectives to handle nuisance parameters and propose a transformer-based policy architecture that respects the temporal structure of dynamical systems. We demonstrate the approach on four systems of increasing complexity: a fed-batch bioreactor with Monod kinetics, a Haldane bioreactor with uncertain substrate inhibition, a two-compartment pharmacokinetic model with nuisance clearance parameters, and a DC motor for real-time deployment.

</details>

---

### 59. [FAlCon: A unified framework for algorithmic control of quantum dot devices](https://arxiv.org/abs/2603.16650)

**基本信息**

- 🔗 arXiv: [`2603.16650`](https://arxiv.org/abs/2603.16650)
- 👥 作者: Tyler J. Kovach, Daniel Schug, Zach D. Merino 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16650.pdf)

**💡 相关性分析**

满足标准2：论文提出了FAlCon框架，这是一个用于量子点设备自动化表征和控制的软件生态系统，提供了领域特定语言、数据结构和协议库，为化学与物理实验的自动化、数据驱动优化提供了重要的工具和资源。

**📖 中文摘要**

本文介绍了FAlCon，一个用于量子点（QD）设备便携式、自动化表征和调谐测量工作流程的开源软件生态系统。FAlCon提供了一个轻量级领域特定语言（DSL）用于表达硬件无关的状态调谐逻辑、专门的可传输量子点数据结构库（“调谐方言”）以及可扩展的共享测量协议库。通过将算法意图与仪器实现分离，FAlCon使研究人员和工程师能够在异构的量子点实验设置之间交换、调整和部署表征与自动调谐例程。该框架支持从使用预构建算法的最终用户到扩展仪器支持和贡献新调谐策略的开发者的所有用户。虽然当前版本针对量子点实验，但其他量子比特模态和科学实验可以通过提供新的调谐数据类型和仪器控制模板来重用FAlCon的模块化抽象。这项工作为实验自动化、数据采集和仪器控制提供了重要的软件工具和框架，是化学信息学和自动化实验基础设施的关键组成部分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As spin-based quantum systems scale, their setup and control complexity increase sharply. In semiconductor quantum dot (QD) experiments, device-to-device variability, heterogeneous control-electronics stacks, and differing operational modalities make it difficult to reuse characterization, calibration, and control logic across laboratories. We present FAlCon, an open-source software ecosystem for portable, automated characterization and tuning measurement workflows. FAlCon provides (i) a lightweight domain-specific language for expressing state-based tuning logic in a hardware-agnostic form; (ii) specialized transmittable libraries of physics-informed QD data structures (``tuning vernacula''); and (iii) extensible libraries of shared measurement protocols enabling an interoperable lab-agnostic measurement stack. By separating algorithm intent from instrument realization, while preserving traceability and supporting typed scripting, FAlCon enables researchers and engineers to exchange, adapt, and deploy characterization and autotuning routines across heterogeneous QD setups. The framework supports all users, ranging from end users running prebuilt algorithms with custom initial conditions to developers extending instrumentation support and contributing new tuning strategies. Although the present release targets QD experiments, other qubit modalities and scientific experiments could reuse FAlCon's modular abstractions by providing new tuning data types and instrument control templates.

</details>

---

### 60. [BiomedSQL: Text-to-SQL for Scientific Reasoning on Biomedical Knowledge Bases](https://arxiv.org/abs/2505.20321)

**基本信息**

- 🔗 arXiv: [`2505.20321`](https://arxiv.org/abs/2505.20321)
- 👥 作者: Mathew J. Koretsky, Maya Willey, Owen Bianchi 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.20321.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是开发一个用于生物医学知识库的文本到SQL基准（BiomedSQL），这涉及大型语言模型在科学领域（与化学/生物医学紧密相关）的复杂推理和查询任务，与'化学大模型'主题相关。2) 论文提供了BiomedSQL数据集和基准，这是一个可用于评估和开发面向科学领域的大语言模型推理能力的数据资源。

**📖 中文摘要**

本文介绍了BiomedSQL，这是第一个专门为在真实世界生物医学知识库上评估文本到SQL生成中的科学推理而设计的基准。BiomedSQL包含68,000个从模板生成的问题/SQL查询/答案三元组，并基于一个整合了基因-疾病关联、组学数据因果推断和药物批准记录的统一BigQuery知识库。每个问题都需要模型推断领域特定标准（例如全基因组显著性阈值、效应方向性或试验阶段过滤），而不是仅仅依赖句法翻译。该工作评估了一系列开源和闭源LLM，揭示了在结构化生物医学知识库上进行稳健推理支持科学发现的文本到SQL系统的性能差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biomedical researchers increasingly rely on large-scale structured databases for complex analytical tasks. However, current text-to-SQL systems often struggle to map qualitative scientific questions into executable SQL, particularly when implicit domain reasoning is required. We introduce BiomedSQL, the first benchmark explicitly designed to evaluate scientific reasoning in text-to-SQL generation over a real-world biomedical knowledge base. BiomedSQL comprises 68,000 question/SQL query/answer triples generated from templates and grounded in a harmonized BigQuery knowledge base that integrates gene-disease associations, causal inference from omics data, and drug approval records. Each question requires models to infer domain-specific criteria, such as genome-wide significance thresholds, effect directionality, or trial phase filtering, rather than rely on syntactic translation alone. We evaluate a range of open- and closed-source LLMs across prompting strategies and interaction paradigms. Our results reveal a substantial performance gap: Gemini-3-Pro achieves 58.1% execution accuracy, while our custom multi-step agent, BMSQL, reaches 62.6%, both well below the expert baseline of 90.0%. BiomedSQL provides a new foundation for advancing text-to-SQL systems capable of supporting scientific discovery through robust reasoning over structured biomedical knowledge bases. Our dataset is publicly available at this https URL , and our code is open-source at this https URL .

</details>

---

### 61. [Are LLMs Good Text Diacritizers? An Arabic and Yoruba Case Study](https://arxiv.org/abs/2506.11602)

**基本信息**

- 🔗 arXiv: [`2506.11602`](https://arxiv.org/abs/2506.11602)
- 👥 作者: Hawau Olamide Toyin, Samar Mohamed Magdy, Hanan Aldarmaki
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.11602.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新的多语言文本加符数据集MultiDiac，用于评估LLMs在特定语言处理任务上的性能。虽然论文主题是自然语言处理，但其核心贡献——数据集——作为一种数据资源，可用于训练和评估语言模型（包括可能应用于化学文本处理的模型），因此与提供数据资源的标准相关。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）在两种类型学不同的语言（阿拉伯语和约鲁巴语）中进行文本加符（diacritization）的有效性。为了进行严格评估，作者引入了新的多语言数据集MultiDiac，其中包含捕捉各种加符歧义的多样化样本。该工作评估了12个不同大小、可访问性和语言覆盖范围的LLM，并将它们与4个专门的加符模型进行了基准测试。此外，还使用LoRA为约鲁巴语微调了四个小型开源模型。结果表明，许多现成的LLM优于专门的加符模型，但较小的模型存在幻觉问题。研究发现，在小数据集上进行微调有助于提高约鲁巴语的加符性能并减少幻觉。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the effectiveness of large language models (LLMs) for text diacritization in two typologically distinct languages: Arabic and Yoruba. To enable a rigorous evaluation, we introduce a novel multilingual dataset MultiDiac, with diverse samples that capture a range of diacritic ambiguities. We evaluate 12 LLMs varying in size, accessibility, and language coverage, and benchmark them against $4$ specialized diacritization models. Additionally, we fine-tune four small open-source models using LoRA for Yoruba. Our results show that many off-the-shelf LLMs outperform specialized diacritization models, but smaller models suffer from hallucinations. We find that fine-tuning on a small dataset can help improve diacritization performance and reduce hallucinations for Yoruba.

</details>

---

### 62. [Scalable Feature Learning on Huge Knowledge Graphs for Downstream Machine Learning](https://arxiv.org/abs/2507.00965)

**基本信息**

- 🔗 arXiv: [`2507.00965`](https://arxiv.org/abs/2507.00965)
- 👥 作者: Félix Lefebvre, Gaël Varoquaux
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.00965.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是开发用于知识图谱的嵌入学习方法（SEPAL）。知识图谱和嵌入学习是化学信息学和生物信息学中表示分子、反应、蛋白质等实体及其关系的核心技术，与'化学大模型'的基础技术栈相关。2) 论文提出的SEPAL算法本身是一种可用于从知识图谱中提取特征表示的工具/方法，符合标准2中'提供了可用于这些主题的工具'。

**📖 中文摘要**

本文介绍了SEPAL：一种用于大型知识图谱的可扩展嵌入传播算法，旨在为下游任务大规模生产高质量的嵌入。SEPAL的核心思想是通过仅在一小部分核心实体上优化嵌入来确保全局嵌入一致性，然后通过消息传递将它们传播到图的其余部分。该工作在7个大规模知识图谱和46个下游机器学习任务上评估了SEPAL。结果表明，SEPAL在下游任务上显著优于先前的方法。此外，SEPAL可以扩展其基础嵌入模型，使得在商用硬件上拟合巨大的知识图谱成为可能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many machine learning tasks can benefit from external knowledge. Large knowledge graphs store such knowledge, and embedding methods can be used to distill it into ready-to-use vector representations for downstream applications. For this purpose, current models have however two limitations: they are primarily optimized for link prediction, via local contrastive learning, and their application to the largest graphs requires significant engineering effort due to GPU memory limits. To address these, we introduce SEPAL: a Scalable Embedding Propagation ALgorithm for large knowledge graphs designed to produce high-quality embeddings for downstream tasks at scale. The key idea of SEPAL is to ensure global embedding consistency by optimizing embeddings only on a small core of entities, and then propagating them to the rest of the graph with message passing. We evaluate SEPAL on 7 large-scale knowledge graphs and 46 downstream machine learning tasks. Our results show that SEPAL significantly outperforms previous methods on downstream tasks. In addition, SEPAL scales up its base embedding model, enabling fitting huge knowledge graphs on commodity hardware.

</details>

---

### 63. [Disentangling trust from cooperation: Evolution of trust as reduced monitoring in social dilemmas](https://arxiv.org/abs/2509.04143)

**基本信息**

- 🔗 arXiv: [`2509.04143`](https://arxiv.org/abs/2509.04143)
- 👥 作者: Cedric Perret, Anh Han, Elias Fernández Domingos 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.04143.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种利用多模态大语言模型（MLLM）进行推理以提升检测性能的方法。虽然主要应用场景是OOD检测，但其核心技术创新在于利用大模型（MLLM）进行理解和推理来构建语义空间，这与“化学大模型”主题中利用大模型进行化学信息处理和推理的核心思想高度相关。

**📖 中文摘要**

本文提出了一种名为ANTS（自适应负文本空间塑造）的方法，用于提升多模态大语言模型（MLLM）在分布外（OOD）检测中的性能。该方法的核心是利用MLLM的理解和推理能力来构建一个自适应的负文本空间。具体而言，系统会缓存历史测试中可能为OOD的图像样本，并提示MLLM描述这些图像，从而生成能够精确刻画OOD分布的、表达性强的负向句子，以增强远OOD检测。对于与分布内（ID）样本相似的近OOD场景，系统会缓存与历史测试图像在视觉上相似的ID类别子集，然后利用MLLM的推理能力，为该子集生成视觉上相似的负向标签，从而有效减少假阴性并改进近OOD检测。该方法无需训练且是零样本的，具有很高的可扩展性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

It is commonly assumed that trust increases cooperation. However, game-theoretic models often fail to distinguish between cooperative actions and trust, making it difficult to independently measure trust and determine how its effects vary in different social dilemmas. To address this, we build on influential theories that equate trust with reduced monitoring of an agent's actions. We implement this as a heuristic that cognitively bounded agents can use in repeated games to avoid spending time and effort always monitoring their partner. Agents using this heuristic reduce monitoring of a partner's actions once a threshold level of cooperativeness has been observed -- providing a measurable and architecture-agnostic definition of trust. Using evolutionary game theory, we systematically analyse the success of strategies that use this trust heuristic across the entire space of two-player symmetric social dilemma games. We demonstrate that trust-as-reduced-monitoring facilitates cooperation in two different ways. First, when monitoring is costly, trust heuristics allow for higher levels of cooperation in social dilemmas where the temptation to defect is high. Second, when agents can make action errors, trust heuristics promote cooperation even in coordination problems. Our results disentangle trust from cooperation, and provide a behavioural measure of trust that applies across interaction types.

</details>

---

### 64. [Connecting Jensen-Shannon and Kullback-Leibler Divergences: A New Bound for Representation Learning](https://arxiv.org/abs/2510.20644)

**基本信息**

- 🔗 arXiv: [`2510.20644`](https://arxiv.org/abs/2510.20644)
- 👥 作者: Reuben Dorent, Polina Golland, William Wells III
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.20644.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是建立和优化表示学习中的信息度量理论框架。虽然未直接提及化学或质谱，但其研究的核心——如何有效度量和优化数据表示中的信息——是构建和理解任何领域大模型（包括化学大模型）的基础理论问题。该工作为基于信息论的模型表示学习提供了理论工具，与“化学大模型”主题中模型表示和学习的理论基础相关。

**📖 中文摘要**

本文在表示学习领域建立了詹森-香农散度（JSD）和库尔巴克-莱布勒散度（KLD）之间的新联系。互信息（MI）是表示学习中衡量统计依赖性的基本指标，但直接优化基于KLD的MI通常难以处理。因此，许多近期方法转而通过判别性损失最大化联合分布与边缘分布乘积之间的JSD等替代依赖度量。然而，这些替代目标与MI之间的联系尚不明确。本研究通过推导出一个新的、紧致的、可处理的通用下界，弥合了这一差距。通过将该下界专门应用于联合分布和边缘分布，作者证明最大化基于JSD的信息量可以增加互信息的一个有保证的下界。这项工作为在基于MI的表示学习中使用判别性学习提供了新的理论依据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mutual Information (MI) is a fundamental measure of statistical dependence widely used in representation learning. While direct optimization of MI via its definition as a Kullback-Leibler divergence (KLD) is often intractable, many recent methods have instead maximized alternative dependence measures, most notably, the Jensen-Shannon divergence (JSD) between joint and product of marginal distributions via discriminative losses. However, the connection between these surrogate objectives and MI remains poorly understood. In this work, we bridge this gap by deriving a new, tight, and tractable lower bound on KLD as a function of JSD in the general case. By specializing this bound to joint and marginal distributions, we demonstrate that maximizing the JSD-based information increases a guaranteed lower bound on mutual information. Furthermore, we revisit the practical implementation of JSD-based objectives and observe that minimizing the cross-entropy loss of a binary classifier trained to distinguish joint from marginal pairs recovers a known variational lower bound on the JSD. Extensive experiments demonstrate that our lower bound is tight when applied to MI estimation. We compared our lower bound to state-of-the-art neural estimators of variational lower bound across a range of established reference scenarios. Our lower bound estimator consistently provides a stable, low-variance estimate of a tight lower bound on MI. We also demonstrate its practical usefulness in the context of the Information Bottleneck framework. Taken together, our results provide new theoretical justifications and strong empirical evidence for using discriminative learning in MI-based representation learning.

</details>

---

### 65. [Testing Correlation in Graphs by Counting Bounded Degree Motifs](https://arxiv.org/abs/2510.25289)

**基本信息**

- 🔗 arXiv: [`2510.25289`](https://arxiv.org/abs/2510.25289)
- 👥 作者: Dong Huang, Pengkun Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.25289.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于图结构模体计数的统计检验算法。图神经网络和图表征学习是“化学大模型”和“质谱结构推理”中处理分子图、谱图等结构化数据的核心技术之一。本文提出的图相关性检测方法，其底层思想（利用子图模式/模体进行图分析）与化学信息学中利用子结构（官能团、碎片）进行分子表征和推理的思路有相通之处，可视为图算法基础研究，对相关领域有潜在借鉴价值。

**📖 中文摘要**

本文研究了通过计算有界度模体（bounded degree motifs）来检测两个Erdős-Rényi图之间相关性的问题。该问题被表述为一个假设检验问题：在零假设下，两个图是独立的；在备择假设下，它们通过顶点集之间的潜在双射映射而相关。作者开发了一种通过计算有界度模体的多项式时间检验方法，并证明了当边连接概率满足一定条件时，该方法对于任何常数相关系数ρ都是有效的。这项工作在图结构数据分析中提供了一种新的、高效的统计检验方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the problem of detecting correlation between two Erdős-Rényi graphs $G(n,p)$, formulated as a hypothesis testing problem: under the null hypothesis, the two graphs are independent, while under the alternative hypothesis, they are correlated through a latent bijective mapping between their vertex sets. We develop a polynomial-time test by counting bounded degree motifs and prove its effectiveness for any constant correlation coefficient $\rho$ when the edge connecting probability satisfies $p\ge n^{-1+\delta}$ for some constant $\delta>0$. In particular, our guarantee improves the constrain of motif-counting methods from $\rho\ge \sqrt{\alpha}$ to any constant $\rho = \Omega(1)$, where $\alpha\approx 0.338$ is the Otter's constant.

</details>

---

### 66. [AGRAG: Advanced Graph-based Retrieval-Augmented Generation for LLMs](https://arxiv.org/abs/2511.05549)

**基本信息**

- 🔗 arXiv: [`2511.05549`](https://arxiv.org/abs/2511.05549)
- 👥 作者: Yubo Wang, Haoyang Li, Fei Teng 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05549.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型（LLM）与结构化知识（图）结合的能力。虽然应用场景是通用问答，但其核心技术——图结构的知识表示、检索和推理——与“化学大模型”主题高度相关。化学领域知识天然适合用图（分子图、反应网络）表示，如何让大模型有效理解和利用这类结构化知识是化学信息学的核心挑战之一。本文提出的图RAG框架为解决化学领域的知识增强和推理问题提供了直接相关的技术思路。

**📖 中文摘要**

本文提出了AGRAG，一种先进的基于图的检索增强生成框架，旨在增强大语言模型的结构化知识。针对现有图RAG方法的三个关键挑战（图构建不准确、推理能力差、回答不充分），AGRAG进行了改进：1）使用基于统计的方法替代广泛使用的LLM实体提取方法，以避免幻觉和错误传播；2）将图推理过程表述为最小成本最大影响子图生成问题，并设计贪心算法求解，生成的子图作为显式推理路径，告诉LLM为何检索某些文本块，从而提高推理能力；3）生成的MCMI子图允许更复杂的图结构（如环），提高了推理路径的全面性。实验表明AGRAG在多个任务上表现优异。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-based retrieval-augmented generation (Graph-based RAG) has demonstrated significant potential in enhancing Large Language Models (LLMs) with structured knowledge. However, existing methods face three critical challenges: Inaccurate Graph Construction, caused by LLM hallucination; Poor Reasoning Ability, caused by failing to generate explicit reasons telling LLM why certain chunks were selected; and Inadequate Answering, which only partially answers the query due to the inadequate LLM reasoning, making their performance lag behind NaiveRAG on certain tasks. To address these issues, we propose AGRAG, an advanced graph-based retrieval-augmented generation framework. When constructing the graph, AGRAG substitutes the widely used LLM entity extraction method with a statistics-based method, avoiding hallucination and error propagation. During retrieval, AGRAG formulates the graph reasoning procedure as the Minimum Cost Maximum Influence (MCMI) subgraph generation problem, where we try to include more nodes with high influence score, but with less involving edge cost, to make the generated reasoning paths more comprehensive. We prove this problem to be NP-hard, and propose a greedy algorithm to solve it. The MCMI subgraph generated can serve as explicit reasoning paths to tell LLM why certain chunks were retrieved, thereby making the LLM better focus on the query-related part contents of the chunks, reducing the impact of noise, and improving AGRAG's reasoning ability. Furthermore, compared with the simple tree-structured reasoning paths, our MCMI subgraph can allow more complex graph structures, such as cycles, and improve the comprehensiveness of the generated reasoning paths. The code and prompt of AGRAG are released at: this https URL .

</details>

---

### 67. [Flow Matching for Tabular Data Synthesis](https://arxiv.org/abs/2512.00698)

**基本信息**

- 🔗 arXiv: [`2512.00698`](https://arxiv.org/abs/2512.00698)
- 👥 作者: Bahrul Ilmi Nasution, Floor Eijkelboom, Mark Elliot 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00698.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是系统性地研究并提出了用于表格数据合成的流匹配方法，并进行了详尽的基准测试和比较。化学信息学和质谱分析领域经常需要处理表格格式的分子描述符、物化性质、谱图特征等数据集。本文提出的高效、高质量的表格数据生成框架（TabbyFlow）及相关代码，为化学领域生成用于模型训练的合成数据集、进行数据增强或隐私保护下的数据共享提供了直接可用的数据资源、工具和方法论参考。

**📖 中文摘要**

本文研究了流匹配（Flow Matching, FM）方法在表格数据合成中的应用。合成数据生成是隐私保护数据共享的重要工具。尽管扩散模型设定了近期基准，但流匹配提供了一个有前景的替代方案。论文提出了实现表格数据合成流匹配的不同方法，并对流匹配（FM和变分FM）与最先进的扩散方法进行了全面的实证比较。作者评估了标准最优传输和方差保持概率路径，并比较了确定性和随机性采样器。关键发现表明，FM（特别是TabbyFlow）优于扩散基线，且能以极少的函数评估步骤实现优异性能，提供了显著的计算优势。概率路径的选择至关重要，OT路径更鲁棒，而VP路径有潜力产生隐私风险更低的合成数据。此外，使流随机化不仅保留了边缘分布，在某些情况下还能生成高效用、低披露风险的合成数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data generation is an important tool for privacy-preserving data sharing. Although diffusion models have set recent benchmarks, flow matching (FM) offers a promising alternative. This paper presents different ways to implement FM for tabular data synthesis. We provide a comprehensive empirical study that compares flow matching (FM and variational FM) with a state-of-the-art diffusion method (TabDDPM and TabSyn) in tabular data synthesis. We evaluate both the standard Optimal Transport (OT) and the Variance Preserving (VP) probability paths, and also compare deterministic and stochastic samplers -- something possible when learning to generate using \textit{variational} FM -- characterising the empirical relationship between data utility and privacy risk. Our key findings reveal that FM, particularly TabbyFlow, outperforms diffusion baselines. Flow matching methods also achieve better performance with remarkably low function evaluations ($\leq$ 100 steps), offering a substantial computational advantage. The choice of probability path is also crucial, as using the OT is a strong default and more robust to early stopping on average, while VP has potential to produce synthetic data with lower privacy risk. Lastly, our results show that making flows stochastic not only preserves marginal distributions but, in some instances, enables the generation of high utility synthetic data with reduced disclosure risk. The implementation code associated with this paper is publicly available at this https URL .

</details>

---

### 68. [Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing](https://arxiv.org/abs/2603.15011)

**基本信息**

- 🔗 arXiv: [`2603.15011`](https://arxiv.org/abs/2603.15011)
- 👥 作者: Jiahe Song, Chuang Wang, Yinfan Wang 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15011.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于化学反应图解析的视觉语言模型方法，这直接属于化学信息学领域，并涉及利用和增强大模型（VLM）的能力来处理化学结构推理任务。

**📖 中文摘要**

本文提出了一种用于化学反应图解析（RxnDP）的新方法，旨在从文献中提取化学合成信息。该方法从提示表示和学习范式两个互补的角度增强基于视觉语言模型（VLM）的RxnDP。首先，提出了“标识符作为视觉提示”（IdtVP），利用自然存在的分子标识符（如粗体数字1a）来激活VLM预训练期间获得的化学知识，从而实现了强大的零样本和分布外能力。其次，为了在微调范式中进一步优化性能，引入了Re3-DAPO，这是一种利用可验证奖励直接优化反应级指标的强化学习算法。此外，还发布了ScannedRxn基准，包含带有真实世界伪影的扫描历史反应图，以严格评估模型的鲁棒性和分布外能力。这项工作直接针对“化学大模型”在化学信息学领域的应用，特别是利用VLM进行复杂的视觉推理任务（解析化学结构图），并提出了新的训练和评估方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reaction diagram parsing (RxnDP) is critical for extracting chemical synthesis information from literature. Although recent Vision-Language Models (VLMs) have emerged as a promising paradigm to automate this complex visual reasoning task, their application is fundamentally bottlenecked by the inability to align visual chemical entities with pre-trained knowledge, alongside the inherent discrepancy between token-level training and reaction-level evaluation. To address these dual challenges, this work enhances VLM-based RxnDP from two complementary perspectives: prompting representation and learning paradigms. First, we propose Identifier as Visual Prompting (IdtVP), which leverages naturally occurring molecule identifiers (e.g., bold numerals like 1a) to activate the chemical knowledge acquired during VLM pre-training. IdtVP enables powerful zero-shot and out-of-distribution capabilities, outperforming existing prompting strategies. Second, to further optimize performance within fine-tuning paradigms, we introduce Re3-DAPO, a reinforcement learning algorithm that leverages verifiable rewards to directly optimize reaction-level metrics, thereby achieving consistent gains over standard supervised fine-tuning. Additionally, we release the ScannedRxn benchmark, comprising scanned historical reaction diagrams with real-world artifacts, to rigorously assess model robustness and out-of-distribution ability. Our contributions advance the accuracy and generalization of VLM-based reaction diagram parsing. We will release data, models, and code on GitHub.

</details>

---

### 69. [To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation](https://arxiv.org/abs/2603.15159)

**基本信息**

- 🔗 arXiv: [`2603.15159`](https://arxiv.org/abs/2603.15159)
- 👥 作者: Yitong Zhang, Chengze Li, Ruize Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15159.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型（LLM）在特定领域（代码生成）的任务能力，特别是通过数据合成和自训练方法。虽然应用场景是代码生成，但其提升LLM领域适应性的方法论与构建专业领域“化学大模型”面临的技术挑战（如处理私有化学数据库、工具调用）高度相关。

**📖 中文摘要**

本文提出了PriCoder方法，旨在解决大语言模型（LLM）在面向私有库的代码生成中的局限性。现有方法主要依赖在推理时检索私有库API文档并将相关知识注入上下文，但这通常不足。PriCoder通过自动合成数据来教导LLM调用私有库API。具体而言，它将私有库数据合成建模为图的构建，并在两个图算子之间交替：（1）渐进式图演化，通过从基本样本逐步合成更多样化的训练样本来提高数据多样性；（2）多维图剪枝，通过严格的过滤流程提高数据质量。在三个主流LLM上的实验表明，PriCoder显著改善了面向私有库的代码生成，在许多设置中pass@1指标提升超过20%，同时对通用代码生成能力影响可忽略。这项工作专注于提升LLM在特定领域（代码生成）的能力，其方法论（数据合成、图表示）对于构建需要处理私有化学数据库或工具的“化学大模型”具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability. Our code and benchmarks are publicly available at this https URL .

</details>

---

### 70. [HindSight: Evaluating LLM-Generated Research Ideas via Future Impact](https://arxiv.org/abs/2603.15164)

**基本信息**

- 🔗 arXiv: [`2603.15164`](https://arxiv.org/abs/2603.15164)
- 👥 作者: Bo Jiang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15164.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大语言模型（LLM）生成研究想法的质量。虽然评估领域是AI/ML，但其提出的评估框架（HindSight）和方法论（基于真实未来影响的评估）可以直接应用于评估“化学大模型”在化学研究中的想法生成能力，属于该主题的评估方法研究。

**📖 中文摘要**

本文介绍了HindSight，一种时间分割评估框架，通过将生成的想法与真实的未来出版物进行匹配，并根据引用影响和会议接受度进行评分，来衡量AI生成研究想法的质量。使用时序截断T，将想法生成系统限制在T之前的文献，然后根据随后30个月内发表的论文评估其输出。在10个AI/ML研究主题上的实验揭示了一个显著的脱节：LLM-as-Judge发现检索增强和普通想法生成之间没有显著差异，而HindSight显示检索增强系统产生的想法得分高出2.5倍。此外，HindSight分数与LLM判断的新颖性呈负相关，表明LLM系统性地高估了那些从未在真实研究中实现的、听起来新颖的想法。这项工作提出了评估AI（特别是LLM）生成研究想法的新方法，对于评估“化学大模型”在化学研究中的创意生成潜力具有直接借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating AI-generated research ideas typically relies on LLM judges or human panels -- both subjective and disconnected from actual research impact. We introduce HindSight, a time-split evaluation framework that measures idea quality by matching generated ideas against real future publications and scoring them by citation impact and venue acceptance. Using a temporal cutoff~$T$, we restrict an idea generation system to pre-$T$ literature, then evaluate its outputs against papers published in the subsequent 30 months. Experiments across 10 AI/ML research topics reveal a striking disconnect: LLM-as-Judge finds no significant difference between retrieval-augmented and vanilla idea generation ($p{=}0.584$), while HindSight shows the retrieval-augmented system produces 2.5$\times$ higher-scoring ideas ($p{<}0.001$). Moreover, HindSight scores are \emph{negatively} correlated with LLM-judged novelty ($\rho{=}{-}0.29$, $p{<}0.01$), suggesting that LLMs systematically overvalue novel-sounding ideas that never materialize in real research.

</details>

---

### 71. [Why the Valuable Capabilities of LLMs Are Precisely the Unexplainable Ones](https://arxiv.org/abs/2603.15238)

**基本信息**

- 🔗 arXiv: [`2603.15238`](https://arxiv.org/abs/2603.15238)
- 👥 作者: Quan Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15238.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大语言模型（LLM）本质能力的理论分析，探讨其可解释性和能力边界。这直接与理解“化学大模型”的潜力和局限性相关，属于该主题的理论基础部分。

**📖 中文摘要**

本文提出了一个反直觉的论点：大语言模型（LLM）真正有价值的能力恰恰存在于无法完全被人可读的离散规则所捕获的部分。核心论证是通过专家系统等价性进行反证法：如果LLM的全部能力可以由一套完整的人可读规则描述，那么该规则集在功能上等同于一个专家系统；但专家系统在历史上和经验上都被证明严格弱于LLM；因此产生矛盾——LLM超越专家系统的能力正是那些无法被规则编码的能力。论文进一步用中国哲学概念“悟”（通过实践的顿悟）、专家系统的历史失败以及人类认知工具与复杂系统之间的结构不匹配来支持这一论点。本文讨论了对可解释性研究、AI安全和科学认识论的影响。这篇论文是对“大模型”（特别是LLM）本质能力的哲学和理论探讨，属于对“化学大模型”理论基础和局限性的高层思考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper proposes and argues for a counterintuitive thesis: the truly valuable capabilities of large language models (LLMs) reside precisely in the part that cannot be fully captured by human-readable discrete rules. The core argument is a proof by contradiction via expert system equivalence: if the full capabilities of an LLM could be described by a complete set of human-readable rules, then that rule set would be functionally equivalent to an expert system; but expert systems have been historically and empirically demonstrated to be strictly weaker than LLMs; therefore, a contradiction arises -- the capabilities of LLMs that exceed those of expert systems are exactly the capabilities that cannot be rule-encoded. This thesis is further supported by the Chinese philosophical concept of Wu (sudden insight through practice), the historical failure of expert systems, and a structural mismatch between human cognitive tools and complex systems. The paper discusses implications for interpretability research, AI safety, and scientific epistemology.

</details>

---

### 72. [SAGE: Multi-Agent Self-Evolution for LLM Reasoning](https://arxiv.org/abs/2603.15255)

**基本信息**

- 🔗 arXiv: [`2603.15255`](https://arxiv.org/abs/2603.15255)
- 👥 作者: Yulin Peng, Xinxin Zhu, Chenxing Wei 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15255.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个多代理自进化框架（SAGE）来提升大语言模型（LLM）的推理能力。虽然应用领域是广义的数学和代码生成，但其核心方法论（LLM推理、自训练、多代理系统）直接与构建和优化“化学大模型”所需的基础能力相关。

**📖 中文摘要**

本文提出了SAGE（用于广义推理进化的自进化代理），一个用于大语言模型（LLM）推理的闭环多代理自进化框架。该框架包含四个代理：挑战者、规划者、求解者和批评者，它们从一个共享的LLM主干共同进化，仅使用少量种子集。挑战者持续生成越来越难的任务；规划者将每个任务转换为结构化的多步骤计划；求解者遵循计划生成答案，其正确性由外部验证器确定。批评者对生成的问题和计划进行评分和过滤，以防止课程漂移并保持训练信号质量，从而实现稳定的自训练。在数学和代码生成基准测试中，SAGE在不同模型规模上带来了一致的性能提升。这项工作专注于通过多代理系统和自训练来提升LLM的推理能力，属于“化学大模型”范畴中更广义的“大模型”能力增强研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement learning with verifiable rewards improves reasoning in large language models (LLMs), but many methods still rely on large human-labeled datasets. While self-play reduces this dependency, it often lacks explicit planning and strong quality control, limiting stability in long-horizon multi-step reasoning. We present SAGE (Self-evolving Agents for Generalized reasoning Evolution), a closed-loop framework where four agents: Challenger, Planner, Solver, and Critic, co-evolve from a shared LLM backbone using only a small seed set. The Challenger continuously generates increasingly difficult tasks; the Planner converts each task into a structured multi-step plan; and the Solver follows the plan to produce an answer, whose correctness is determined by external verifiers. The Critic scores and filters both generated questions and plans to prevent curriculum drift and maintain training signal quality, enabling stable self-training. Across mathematics and code-generation benchmarks, SAGE delivers consistent gains across model scales, improving the Qwen-2.5-7B model by 8.9% on LiveCodeBench and 10.7% on OlympiadBench.

</details>

---

### 73. [General Mechanism of Evolution Shared by Proteins and Words](https://arxiv.org/abs/2012.14309)

**基本信息**

- 🔗 arXiv: [`2012.14309`](https://arxiv.org/abs/2012.14309)
- 👥 作者: Li-Min Wang, Hsing-Yi Lai, Sun-Ting Tsai 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2012.14309.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是建立蛋白质和语言序列进化的统一数学模型和统计规律。这直接属于化学信息学的基础理论研究，为理解蛋白质序列（质谱结构推理的目标实体）的生成和统计特性提供了理论基础，与“化学大模型”和“质谱结构推理”的底层数据（蛋白质序列）密切相关。

**📖 中文摘要**

本文揭示了蛋白质和单词共享的几种新的统计关系，并由此建立了一个具有明确公式的通用进化机制。研究发现自然选择可以通过最小努力原则的熵公式来量化，以确定在进化中存活的序列变异。此外，幂律行为的起源以及环境变化如何刺激新蛋白质和单词的出现，也可以通过引入功能连接网络来解释。结果表明，遗传学和语言学在其不同层次上不仅存在对应关系，而且复杂适应系统的进化具有新的基本物理特性。这项工作在序列层面建立了生物学（蛋白质）和语言学（单词）进化之间的深刻类比和统一数学模型。虽然不直接涉及“质谱结构推理”，但其对蛋白质序列统计规律和进化机制的建模是化学信息学和计算生物学的基础，为理解蛋白质序列（质谱推断的目标）提供了理论框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Complex systems, such as life and languages, are governed by principles of evolution. The analogy and comparison between biology and linguistics\cite{alphafold2, RoseTTAFold, lang_virus, cell language, faculty1, language of gene, Protein linguistics, dictionary, Grammar of pro_dom, complexity, genomics_nlp, InterPro, language modeling, Protein language modeling} provide a computational foundation for characterizing and analyzing protein sequences, human corpora, and their evolution. However, no general mathematical formula has been proposed so far to illuminate the origin of quantitative hallmarks shared by life and language. Here we show several new statistical relationships shared by proteins and words, which inspire us to establish a general mechanism of evolution with explicit formulations that can incorporate both old and new characteristics. We found natural selection can be quantified via the entropic formulation by the principle of least effort to determine the sequence variation that survives in evolution. Besides, the origin of power law behavior and how changes in the environment stimulate the emergence of new proteins and words can also be explained via the introduction of function connection network. Our results demonstrate not only the correspondence between genetics and linguistics over their different hierarchies but also new fundamental physical properties for the evolution of complex adaptive systems. We anticipate our statistical tests can function as quantitative criteria to examine whether an evolution theory of sequence is consistent with the regularity of real data. In the meantime, their correspondence broadens the bridge to exchange existing knowledge, spurs new interpretations, and opens Pandora's box to release several potentially revolutionary challenges. For example, does linguistic arbitrariness conflict with the dogma that structure determines function?

</details>

---

### 74. [Predicting Biomedical Interactions with Probabilistic Model Selection for Graph Neural Networks](https://arxiv.org/abs/2211.13231)

**基本信息**

- 🔗 arXiv: [`2211.13231`](https://arxiv.org/abs/2211.13231)
- 👥 作者: Kishan KC, Rui Li, Paribesh Regmi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2211.13231.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用图神经网络（GNN）和贝叶斯方法预测生物医学相互作用（如蛋白质相互作用）。这直接属于化学信息学和生物信息学的研究范畴，是“化学大模型”可能应用的子领域之一（分子相互作用预测）。

**📖 中文摘要**

本文提出了一个贝叶斯模型选择框架，用于联合推断数据支持的最可能的图卷积层数、应用dropout正则化并学习网络参数。该框架旨在解决图神经网络（GNN）在预测生物医学相互作用时，深度选择依赖启发式或大量实验，以及更深GNN往往校准不佳的问题。在四个生物医学相互作用数据集上的实验表明，该方法优于竞争方法，通过允许GNN调整其深度以适应各种生物医学网络中的相互作用信息，提供了良好校准的预测。这项工作专注于改进GNN在生物医学网络（如蛋白质相互作用）预测中的应用，属于化学信息学和生物信息学的交叉领域。虽然主要方法是GNN而非严格意义上的“大模型”，但其处理的生物分子相互作用网络是“化学大模型”可能处理的数据类型之一，且其模型选择框架对构建稳健的预测模型有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Heterogeneous molecular entities and their interactions, commonly depicted as a network, are crucial for advancing our systems-level understanding of biology. With recent advancements in high-throughput data generation and a significant improvement in computational power, graph neural networks (GNNs) have demonstrated their effectiveness in predicting biomedical interactions. Since GNNs follow a neighborhood aggregation scheme, the number of graph convolution (GC) layers (i.e., depth) determines the neighborhood orders from which they can aggregate information, thereby significantly impacting the model's performance. However, it often relies on heuristics or extensive experimentation to determine an appropriate GNN depth for a given biomedical network. These methods can be unreliable or result in expensive computational overhead. Moreover, GNNs with more GC layers tend to exhibit poor calibration, leading to high confidence in incorrect predictions. To address these challenges, we propose a Bayesian model selection framework to jointly infer the most plausible number of GC layers supported by the data, apply dropout regularization, and learn network parameters. Experiments on four biomedical interaction datasets demonstrate that our method achieves superior performance over competing methods, providing well-calibrated predictions by allowing GNNs to adapt their depths to accommodate interaction information from various biomedical networks. Source code and data is available at: this https URL

</details>

---

### 75. [From structure mining to unsupervised exploration of atomic octahedral networks](https://arxiv.org/abs/2306.12272)

**基本信息**

- 🔗 arXiv: [`2306.12272`](https://arxiv.org/abs/2306.12272)
- 👥 作者: R. Patrick Xian, Ryan J. Morelock, Ido Hadar 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2306.12272.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用无监督机器学习对化学材料中的原子配位网络进行解析和分类。这属于化学信息学中的结构分析领域，与“质谱结构推理”共享“结构推理”这一核心目标，尽管输入数据（晶体结构 vs 质谱数据）和具体任务不同。

**📖 中文摘要**

本文提出了一种工作流程，利用无监督机器学习对配位八面体网络进行几何解析、量化和分类。该工作流程将化学直觉操作化，应用于两个数据集的分析：计算生成的单一氧化物钙钛矿多晶型物和实验测量的杂化碘铅酸盐。对于钙钛矿，揭示了轴依赖性倾斜趋势，有助于检测氧化态变化。对于碘铅酸盐，对其八面体网络进行了分类，揭示了配位环境的鲍林式连接规则及其结构多样性背后的设计原则。这项工作展示了材料化学中原子八面体网络广阔设计空间的一瞥，并为高通量、有针对性的特定结构类型筛选提供了信息。本研究属于计算材料化学和化学信息学领域，利用机器学习分析材料结构。虽然不直接涉及“质谱”，但其对化学结构（配位网络）的解析和分类与“结构推理”这一核心主题在方法论上相通，都是对化学结构进行表征和理解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the spatial arrangements of atom-centered coordination octahedra is crucial for relating structures to properties for many materials families. Traditional case-by-case inspection becomes a prohibitive task for discovering trends and similarities in large datasets. Here, we operationalize chemical intuition to automate the geometric parsing, quantification, and classification of coordination octahedral networks using unsupervised machine learning. We apply the workflow to analyze two datasets to demonstrate its effectiveness. For computationally generated single oxide perovskite (ABO$_{3}$) polymorphs, we uncover axis-dependent tilting trends which assist in detecting oxidation state changes. For hybrid iodoplumbates (A$_x$Pb$_y$I$_z$) from measured structures, we taxonomize their octahedral networks, revealing a Pauling-like connectivity rule for the coordination environment and the design principles underpinning their structural diversity. Our results offer a glimpse into the vast design space of atomic octahedral networks in materials chemistry and inform high-throughput, targeted screening of specific structure types.

</details>

---

### 76. [Making Multi-Axis Gaussian Graphical Models Scalable to Millions of Cells](https://arxiv.org/abs/2407.19892)

**基本信息**

- 🔗 arXiv: [`2407.19892`](https://arxiv.org/abs/2407.19892)
- 👥 作者: Bailey Andrew, Erica L. Harris, James A. Poulter 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.19892.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发可扩展的多轴方法，用于从大规模单细胞数据中联合推断基因网络和细胞网络。这属于生物信息学中的网络推理问题，与“化学大模型”处理生物分子数据并进行结构/关系推理的目标相关。

**📖 中文摘要**

本文开发了一种能够处理百万细胞数据集的多轴方法，解决了现有多轴方法无法扩展到现代单细胞RNA测序数据集的问题。该方法可以学习基因网络和细胞网络，而不对它们做出错误的独立性假设。研究表明，该方法能够从真实单细胞数据中获得新的生物学见解，例如识别在神经元发育中可能具有调节或功能作用的长链非编码RNA基因。该方法作为一个Python包GmGM提供。这项工作属于生物信息学和计算生物学领域，专注于从单细胞数据中推断基因和细胞网络。虽然主要技术是多轴高斯图模型而非深度学习大模型，但其处理大规模生物分子数据（基因表达）并进行网络推理的目标，与“化学大模型”在生物医学数据分析和“结构推理”（此处是基因调控网络结构）方面的应用有概念上的关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: Networks underlie the generation and interpretation of many biological datasets: gene networks shed light on the regulatory structure of the genome, and cell networks can capture structure of the tumor micro-environment. However, most methods that learn such networks make the faulty 'independence assumption'; to learn the gene network, they assume that no cell network exists. 'Multi-axis' methods, which do not make this assumption, fail to scale beyond a few thousand cells or genes. This limits their applicability to only the smallest datasets. Results: We develop a multi-axis method capable of processing million-cell datasets within minutes. This was previously impossible, and unlocks the use of such methods on modern scRNA-seq datasets, as well as more complex datasets. We show that our method yields novel biological insights from real single-cell data, and compares favorably to the existing hdWGCNA methodology. In particular, it identifies long non-coding RNA genes that potentially have a regulatory or functional role in neuronal development. Availability and implementation: Our methodology is available as a Python package GmGM on PyPI ( this https URL ). The code for all experiments performed in this paper is available on GitHub ( this https URL ). Contact: sceba@leeds. this http URL Supplementary information: Our proofs, and some additional experiments, are available in the supplementary material. Keywords: gaussian graphical models, multi-axis models, transcriptomics, multi-omics, scalability

</details>

---

### 77. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕构建一个利用预训练基础模型（scGPT）和大型语言模型（LLM）进行科学发现的智能体框架，这直接属于“化学大模型”主题在生物医学数据上的一个具体应用和范例。

**📖 中文摘要**

本文介绍了ELISA，一个用于单细胞基因组学中基于表达进行发现的、可解释的混合生成式AI智能体框架。该框架的核心是将scGPT（一个用于单细胞RNA测序数据的预训练基础模型）的表达嵌入与基于BioBERT的语义检索以及由大型语言模型（LLM）介导的解释相统一。ELISA通过自动查询分类器，根据输入是基因特征、自然语言概念还是两者的混合，将查询路由到不同的分析管道。它集成了多种分析模块，如通路活性评分、配体-受体相互作用预测、条件感知比较分析和细胞类型比例估计，所有这些都直接在嵌入数据上操作，无需访问原始计数矩阵。这项工作与“化学大模型”主题高度相关，因为它展示了一个专门为生物医学数据（单细胞转录组学）设计和应用的领域基础模型（scGPT）如何与通用LLM结合，构建一个用于科学发现的交互式、可解释的AI系统。这为化学信息学领域（例如，为质谱或分子结构数据构建类似的“化学基础模型+LLM”智能体）提供了直接的范例和灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 78. [Foundation-Model Surrogates Enable Data-Efficient Active Learning for Materials Discovery](https://arxiv.org/abs/2603.12567)

**基本信息**

- 🔗 arXiv: [`2603.12567`](https://arxiv.org/abs/2603.12567)
- 👥 作者: Jeffrey Hu, Rongzhi Dong, Ying Feng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和验证预训练的基础模型（TabPFN）在材料科学主动学习中的应用，这直接属于“化学大模型”主题，展示了基础模型如何解决化学领域（材料发现）中的关键问题。

**📖 中文摘要**

本文提出了一种名为“上下文主动学习”（ICAL）的新方法，用于加速材料发现。该方法的核心创新在于使用TabPFN（一种基于Transformer的基础模型）替代传统的高斯过程或随机森林作为主动学习中的代理模型。TabPFN在数百万个合成回归任务上进行预训练，从而元学习到了一个对表格数据的通用先验。在面对新的小规模材料数据集时，TabPFN无需针对该数据集重新训练，仅通过一次前向传播即可进行原则性的贝叶斯推断，提供准确的回归预测和经过良好校准的不确定性估计，而这正是高效主动学习所必需的。作者在10个材料数据集上对ICAL进行了基准测试，结果表明TabPFN在8个数据集上优于传统代理模型，平均可节省52%的额外评估成本。这项工作与“化学大模型”主题高度相关，因为它展示了一个预训练的、通用的基础模型（TabPFN）如何作为强大的、数据高效的代理模型，直接应用于化学和材料科学中的核心挑战——小数据场景下的性质预测和主动学习。这为在化学信息学中开发和利用类似的基础模型提供了强有力的证据和方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Active learning (AL) has emerged as a powerful paradigm for accelerating materials discovery by iteratively steering experiments toward promising candidates, reducing the number of costly synthesis-and-characterization cycles needed to identify optimal materials. However, current AL relies predominantly on Gaussian Process (GP) and Random Forest (RF) surrogates, which suffer from complementary limitations: GP underfits complex composition-property landscapes due to rigid kernel assumptions, while RF produces unreliable heuristic uncertainty estimates in small-data regimes. This small-data challenge is pervasive in materials science, making reliable surrogate modeling extremely difficult with models trained from scratch on each new dataset. Here we propose In-Context Active Learning (ICAL), which addresses this bottleneck by replacing conventional surrogates with TabPFN, a transformer-based foundation model (FM) pre-trained on millions of synthetic regression tasks to meta-learn a universal prior over tabular data, upon which TabPFN performs principled Bayesian inference in a single forward pass without dataset-specific retraining, delivering strong small-data regression performance and well-calibrated predictive uncertainty (required for effective AL). We benchmark ICAL against GP and RF across 10 materials datasets and TabPFN wins on 8 out of 10 datasets, achieving a mean saving of 52% in extra evaluations relative to GP and 29.77% relative to RF. Cross-validation analysis confirms that TabPFN's advantage stems from superior uncertainty calibration, achieving the lowest Negative Log-Likelihood and Area Under the Sparsification Error curve among all surrogates. These results demonstrate that pre-trained FMs can serve as effective surrogates for active learning, enabling data-efficient discovery across diverse materials systems and small-data experimental sciences.

</details>

---

## 📊 数据统计
- 累计运行天数：37
- 累计论文数量：2668

## 📝 历史记录

> 暂无历史数据

