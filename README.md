# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-07 12:43:16

## 📅 2026-03-07 (今日最新)

**相关论文数：91**

### 1. [A unified foundational framework for knowledge injection and evaluation of Large Language Models in Combustion Science](https://arxiv.org/abs/2603.04452)

**基本信息**

- 🔗 arXiv: [`2603.04452`](https://arxiv.org/abs/2603.04452)
- 👥 作者: Zonglin Yang, Runze Mao, Tianhao Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04452.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个面向特定科学领域（燃烧科学）的化学大模型（LLM）开发框架，包括知识库构建、评估基准和知识注入方法，直接围绕“化学大模型”主题。

**📖 中文摘要**

本文提出了一个用于燃烧科学领域大语言模型（LLM）开发的端到端框架。该框架的核心是构建一个包含35亿token的多模态知识库，数据源涵盖超过20万篇同行评议文章、8000篇学位论文以及约40万行燃烧计算流体力学（CFD）代码。为了评估模型，作者创建了一个包含8个子领域、共436个问题的自动化评估基准（CombustionQA）。研究重点探索了从轻量级检索增强生成（RAG）到知识图谱增强检索和持续预训练的三阶段知识注入路径。实验发现，标准RAG在燃烧科学问答任务上存在性能瓶颈（准确率峰值60%），主要受限于上下文污染问题，从而论证了构建领域基础模型需要结合结构化知识图谱和持续预训练的必要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To advance foundation Large Language Models (LLMs) for combustion science, this study presents the first end-to-end framework for developing domain-specialized models for the combustion community. The framework comprises an AI-ready multimodal knowledge base at the 3.5 billion-token scale, extracted from over 200,000 peer-reviewed articles, 8,000 theses and dissertations, and approximately 400,000 lines of combustion CFD code; a rigorous and largely automated evaluation benchmark (CombustionQA, 436 questions across eight subfields); and a three-stage knowledge-injection pathway that progresses from lightweight retrieval-augmented generation (RAG) to knowledge-graph-enhanced retrieval and continued pretraining. We first quantitatively validate Stage 1 (naive RAG) and find a hard ceiling: standard RAG accuracy peaks at 60%, far surpassing zero-shot performance (23%) yet well below the theoretical upper bound (87%). We further demonstrate that this stage's performance is severely constrained by context contamination. Consequently, building a domain foundation model requires structured knowledge graphs and continued pretraining (Stages 2 and 3).

</details>

---

### 2. [Augmenting representations with scientific papers](https://arxiv.org/abs/2603.04516)

**基本信息**

- 🔗 arXiv: [`2603.04516`](https://arxiv.org/abs/2603.04516)
- 👥 作者: Nicolò Oreste Pinciroli Vago, Rocco Di Tella, Carolina Cuesta-Lázaro 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04516.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个多模态对比学习框架，用于对齐科学数据（X射线光谱）与科学文本，以构建共享的、富含语义的表示。这直接涉及利用大模型（对比学习框架）进行科学数据（可视为一种特殊的化学/物理数据）的结构推理和知识融合，与“化学大模型”和“质谱结构推理”的主题高度相关（光谱是质谱的近亲，同属谱学分析范畴）。

**📖 中文摘要**

本文提出了一个对比学习框架，旨在将X射线光谱数据与从科学文献中提取的领域知识进行对齐，从而促进共享多模态表示的发展。研究解决了将科学文本（涵盖更广泛的物理背景）与光谱数据（范围相对狭窄）连接起来的固有复杂性。该框架通过对比学习管道，在从光谱检索相关文本的任务中实现了20%的Recall@1%，证明了这两种模态之间存在有意义的对齐，并能加速对稀有或理解不足的天体源的解释。此外，由此产生的共享潜在空间有效地编码了具有物理意义的信息。通过融合光谱和文本数据，该模型在20个物理变量的估计上比单模态光谱基线提高了16-18%。结果表明，利用专家混合（MoE）策略，结合单模态和共享表示，可以获得更优的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Astronomers have acquired vast repositories of multimodal data, including images, spectra, and time series, complemented by decades of literature that analyzes astrophysical sources. Still, these data sources are rarely systematically integrated. This work introduces a contrastive learning framework designed to align X-ray spectra with domain knowledge extracted from scientific literature, facilitating the development of shared multimodal representations. Establishing this connection is inherently complex, as scientific texts encompass a broader and more diverse physical context than spectra. We propose a contrastive pipeline that achieves a 20% Recall@1% when retrieving texts from spectra, proving that a meaningful alignment between these modalities is not only possible but capable of accelerating the interpretation of rare or poorly understood sources. Furthermore, the resulting shared latent space effectively encodes physically significant information. By fusing spectral and textual data, we improve the estimation of 20 physical variables by 16-18% over unimodal spectral baselines. Our results indicate that a Mixture of Experts (MoE) strategy, which leverages both unimodal and shared representations, yields superior performance. Finally, outlier analysis within the multimodal latent space identifies high-priority targets for follow-up investigation, including a candidate pulsating ULX (PULX) and a gravitational lens system. Importantly, this framework can be extended to other scientific domains where aligning observational data with existing literature is possible.

</details>

---

### 3. [Discovering mathematical concepts through a multi-agent system](https://arxiv.org/abs/2603.04528)

**基本信息**

- 🔗 arXiv: [`2603.04528`](https://arxiv.org/abs/2603.04528)
- 👥 作者: Daattavya Aggarwal, Oisin Kim, Carl Henrik Ek 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04528.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个多智能体系统，用于自主发现数学概念和结构。这本质上是在探索和构建能够进行复杂科学推理（数学是科学的基础）的大模型或智能体系统，其方法论和目标与构建用于科学发现（包括化学信息学）的“化学大模型”在理念上高度相关。

**📖 中文摘要**

本文提出了一个新的多智能体模型，用于计算数学发现，其灵感来源于数学概念通过实验、证明尝试和反例等过程交互涌现的观察。该系统自主提出猜想并尝试证明它们，根据反馈和不断演化的数据分布做出决策。受欧拉多面体猜想历史和文献中开放挑战的启发，研究以从多面体数据和线性代数知识中自主恢复同调概念的任务作为基准。该系统完成了这一学习问题。最重要的是，实验进行了消融研究，统计测试了完整动态过程的价值，并控制了实验设置。结果支持了主要主张：优化正确的局部过程组合可以导致与数学趣味性惊人一致的概念。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical concepts emerge through an interplay of processes, including experimentation, efforts at proof, and counterexamples. In this paper, we present a new multi-agent model for computational mathematical discovery based on this observation. Our system, conceived with research in mind, poses its own conjectures and then attempts to prove them, making decisions informed by this feedback and an evolving data distribution. Inspired by the history of Euler's conjecture for polyhedra and an open challenge in the literature, we benchmark with the task of autonomously recovering the concept of homology from polyhedral data and knowledge of linear algebra. Our system completes this learning problem. Most importantly, the experiments are ablations, statistically testing the value of the complete dynamic and controlling for experimental setup. They support our main claim: that the optimisation of the right combination of local processes can lead to surprisingly well-aligned notions of mathematical interestingness.

</details>

---

### 4. [Structure-Guided Histopathology Synthesis via Dual-LoRA Diffusion](https://arxiv.org/abs/2603.04565)

**基本信息**

- 🔗 arXiv: [`2603.04565`](https://arxiv.org/abs/2603.04565)
- 👥 作者: Xuan Xu, Prateek Prasanna
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04565.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型和轻量级适配器（LoRA）的生成式AI方法，用于合成具有精确细胞核结构（以中心点为先验）的组织病理学图像。这属于利用生成式大模型（扩散模型）进行生物医学图像的结构推理与合成，与“质谱结构推理”中利用模型进行谱图解析和结构生成的逻辑类似，属于广义的“结构推理”范畴在视觉模态的应用。

**📖 中文摘要**

本文提出了一种双LoRA可控扩散框架，用于组织病理学图像合成。该框架统一支持局部结构补全和全局结构合成。其核心是利用多类细胞核中心点作为轻量级且注释高效的空间先验，在图像部分或完全缺失的情况下提供具有生物学意义的指导。两个任务特定的LoRA适配器使共享主干网络能够专用于局部和全局目标，而无需重新训练单独的扩散模型。广泛的实验表明，该方法在修复和合成任务上均优于最先进的GAN和扩散基线。该方法实现了掩码区域内更忠实的结构恢复，并在全局合成中显著提高了真实感和形态一致性，支持可扩展的泛癌组织病理学建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathology image synthesis plays an important role in tissue restoration, data augmentation, and modeling of tumor microenvironments. However, existing generative methods typically address restoration and generation as separate tasks, although both share the same objective of structure-consistent tissue synthesis under varying degrees of missingness, and often rely on weak or inconsistent structural priors that limit realistic cellular organization. We propose Dual-LoRA Controllable Diffusion, a unified centroid-guided diffusion framework that jointly supports Local Structure Completion and Global Structure Synthesis within a single model. Multi-class nuclei centroids serve as lightweight and annotation-efficient spatial priors, providing biologically meaningful guidance under both partial and complete image absence. Two task-specific LoRA adapters specialize the shared backbone for local and global objectives without retraining separate diffusion models. Extensive experiments demonstrate consistent improvements over state-of-the-art GAN and diffusion baselines across restoration and synthesis tasks. For local completion, LPIPS computed within the masked region improves from 0.1797 (HARP) to 0.1524, and for global synthesis, FID improves from 225.15 (CoSys) to 76.04, indicating improved structural fidelity and realism. Our approach achieves more faithful structural recovery in masked regions and substantially improved realism and morphology consistency in full synthesis, supporting scalable pan-cancer histopathology modeling.

</details>

---

### 5. [PDE foundation model-accelerated inverse estimation of system parameters in inertial confinement fusion](https://arxiv.org/abs/2603.04606)

**基本信息**

- 🔗 arXiv: [`2603.04606`](https://arxiv.org/abs/2603.04606)
- 👥 作者: Mahindra Rautela, Alexander Scheinker, Bradley Love 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04606.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用预训练的PDE基础模型（可视为一种科学大模型）解决数据有限的逆问题，其方法论与“化学大模型”的主题高度相关。

**📖 中文摘要**

本文研究了在惯性约束聚变（ICF）中，利用PDE基础模型加速系统参数逆估计的问题。论文的核心是使用预训练的PDE基础模型，通过有限的任务特定数据进行微调，以解决从多模态、快照式观测中估计系统参数（输入）的逆问题。这项工作展示了基础模型在科学计算逆问题中的应用潜力，其方法（预训练大模型+轻量级任务头）与“化学大模型”的核心思想——即利用大规模预训练模型解决下游特定科学任务——高度相关。虽然应用领域是物理而非化学，但其方法论和模型范式与关注主题中的“化学大模型”概念直接对应。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PDE foundation models are typically pretrained on large, diverse corpora of PDE datasets and can be adapted to new settings with limited task-specific data. However, most downstream evaluations focus on forward problems, such as autoregressive rollout prediction. In this work, we study an inverse problem in inertial confinement fusion (ICF): estimating system parameters (inputs) from multi-modal, snapshot-style observations (outputs). Using the open JAG benchmark, which provides hyperspectral X-ray images and scalar observables per simulation, we finetune the PDE foundation model and train a lightweight task-specific head to jointly reconstruct hyperspectral images and regress system parameters. The fine-tuned model achieves accurate hyperspectral reconstruction (test MSE 1.2e-3) and strong parameter-estimation performance (up to R^2=0.995). Data-scaling experiments (5%-100% of the training set) show consistent improvements in both reconstruction and regression losses as the amount of training data increases, with the largest marginal gains in the low-data regime. Finally, finetuning from pretrained MORPH weights outperforms training the same architecture from scratch, demonstrating that foundation-model initialization improves sample efficiency for data-limited inverse problems in ICF.

</details>

---

### 6. [When Agents Persuade: Propaganda Generation and Mitigation in LLMs](https://arxiv.org/abs/2603.04636)

**基本信息**

- 🔗 arXiv: [`2603.04636`](https://arxiv.org/abs/2603.04636)
- 👥 作者: Julia Jose, Ritik Roongta, Rachel Greenstadt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04636.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一种基于可微分物理和优化（可视为一种特定领域的模型）的方法，用于从复杂测量信号（dMRI）中逆推微观结构参数和边界。这种“从观测反推结构”的逆问题求解范式，与“质谱结构推理”的核心挑战（从质谱信号推断分子结构）在方法论上高度相似。

**📖 中文摘要**

本文提出了Spinverse，一种用于从扩散MRI（dMRI）测量中反演微结构边界和渗透率的可微分物理方法。该方法在固定的四面体网格上表示组织，并将每个内部面的渗透率作为可学习参数，通过完全可微分的Bloch-Torrey模拟器反演dMRI信号。通过反向传播信号匹配损失来优化面渗透率，并通过阈值化学习到的渗透率场来恢复界面。为了解决渗透率反演的不适定性，论文使用了基于网格的几何先验和分阶段的多序列优化课程。该方法能够重建多样化的几何结构，并证明序列调度和正则化对于避免仅轮廓解、提高边界准确性和结构有效性至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their wide-ranging benefits, LLM-based agents deployed in open environments can be exploited to produce manipulative material. In this study, we task LLMs with propaganda objectives and analyze their outputs using two domain-specific models: one that classifies text as propaganda or non-propaganda, and another that detects rhetorical techniques of propaganda (e.g., loaded language, appeals to fear, flag-waving, name-calling). Our findings show that, when prompted, LLMs exhibit propagandistic behaviors and use a variety of rhetorical techniques in doing so. We also explore mitigation via Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and ORPO (Odds Ratio Preference Optimization). We find that fine-tuning significantly reduces their tendency to generate such content, with ORPO proving most effective.

</details>

---

### 7. [Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings](https://arxiv.org/abs/2603.04692)

**基本信息**

- 🔗 arXiv: [`2603.04692`](https://arxiv.org/abs/2603.04692)
- 👥 作者: Lyle Regenwetter, Rosen Yu, Cyril Picard 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04692.pdf)

**💡 相关性分析**

满足标准1和2：1）论文的核心是研究如何使表格基础模型（一种特定类型的大模型）更好地适应科学和工业领域（如化学、工程）的数据，这与“化学大模型”中模型适应特定领域数据的主题相关。2）论文提出了TREDBench数据集和一种嵌入引导的合成数据筛选方法，这些可作为用于改进领域特定模型性能的数据资源和工具开发范例。

**📖 中文摘要**

本文研究了工程应用中表格回归任务的领域适应问题，重点关注表格基础模型（如TabPFN）的预训练分布与真实工程数据统计结构之间的差距。论文引入了TREDBench，一个包含83个真实世界表格回归数据集的精选集合，并利用TabPFN 2.5的数据集级嵌入来研究公共表示空间中的领域结构。研究发现，标准的程序生成合成数据集与工程数据集之间存在显著的合成-真实领域差距。为了在不使用真实工程样本训练的情况下弥合这一差距，论文提出了一种嵌入引导的合成数据筛选方法：生成并识别“类工程”合成数据集，并仅使用选定的合成任务对TabPFN 2.5进行持续预训练。在35个工程回归数据集上的评估表明，这种仅使用合成数据的适应方法提高了预测准确性和数据效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression datasets with expert engineering/non-engineering labels, and use TabPFN 2.5's dataset-level embedding to study domain structure in a common representation space. We find that engineering datasets are partially distinguishable from non-engineering datasets, while standard procedurally generated datasets are highly distinguishable from engineering datasets, revealing a substantial synthetic-real domain gap. To bridge this gap without training on real engineering samples, we propose an embedding-guided synthetic data curation method: we generate and identify "engineering-like" synthetic datasets, and perform continued pre-training of TabPFN 2.5 using only the selected synthetic tasks. Across 35 engineering regression datasets, this synthetic-only adaptation improves predictive accuracy and data efficiency, outperforming TabPFN 2.5 on 29/35 datasets and AutoGluon on 27/35, with mean multiplicative data-efficiency gains of 1.75x and 4.44x, respectively. More broadly, our results indicate that principled synthetic data curation can convert procedural generators into domain-relevant "data engines," enabling foundation models to improve in data-sparse scientific and industrial domains where real data collection is the primary bottleneck.

</details>

---

### 8. [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](https://arxiv.org/abs/2603.04743)

**基本信息**

- 🔗 arXiv: [`2603.04743`](https://arxiv.org/abs/2603.04743)
- 👥 作者: Maojun Sun, Yue Wu, Yifei Xie 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04743.pdf)

**💡 相关性分析**

满足标准2：论文提出了RPKB（R包知识库）和DARE嵌入模型，这些是专门为增强LLM在统计编程（包括化学生物信息学中常用的R生态）中的工具检索能力而构建的数据资源和工具。虽然不直接针对化学，但其构建领域特定工具检索基础设施的方法和资源，对于开发“化学大模型”或“质谱分析”领域的智能助手具有重要的参考价值。

**📖 中文摘要**

本文提出了DARE（Distribution-Aware Retrieval Embedding），一个轻量级、即插即用的检索模型，用于将数据分布信息融入R函数表示中，以改进R包检索。主要贡献包括：(i) RPKB，一个从8,191个高质量CRAN包中提取的精选R包知识库；(ii) DARE，一个融合分布特征与函数元数据的嵌入模型，以提高检索相关性；(iii) RCodingAgent，一个面向R的LLM智能体，用于可靠的R代码生成，以及一套用于系统评估LLM智能体在现实分析场景中表现的统计分析任务。实证表明，DARE在包检索上实现了93.47%的NDCG@10，以更少的参数显著优于最先进的开源嵌入模型。将DARE集成到RCodingAgent中，在下游分析任务上带来了显著增益。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

</details>

---

### 9. [Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator](https://arxiv.org/abs/2603.04797)

**基本信息**

- 🔗 arXiv: [`2603.04797`](https://arxiv.org/abs/2603.04797)
- 👥 作者: Cong Li, Yihan Yin, Chenhao Xue 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04797.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕优化和加速大语言模型（LLM）服务，这直接属于“化学大模型”主题中关于大模型底层架构、高效推理和部署的关键技术范畴。

**📖 中文摘要**

本文提出Helios，一种基于混合键合的LLM服务加速器硬件-软件协同设计。虽然论文的核心是优化大语言模型（LLM）的推理服务，但其提出的分布式分片注意力执行、空间感知的KV缓存分配机制等核心思想，为解决大规模、动态的计算密集型任务提供了新颖的架构范式。这种对“大模型”底层计算架构和内存管理的深度优化研究，为构建更高效的化学信息学或质谱分析领域的专用大模型（如用于分子性质预测或谱图解析的模型）提供了重要的硬件和系统级设计参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been widely deployed for online generative services, where numerous LLM instances jointly handle workloads with fluctuating request arrival rates and variable request lengths. To efficiently execute coexisting compute-intensive and memory-intensive operators, near-memory processing (NMP) based computing paradigm has been extensively proposed. However, existing NMP designs adopt coarse-grained KV cache management and inflexible attention execution flow. Such limitations hinder these proposals from efficiently handling \textit{highly dynamic} LLM serving workloads, limiting their ability to accelerate LLM serving. To tackle these problems, we propose Helios, a Hybrid-bonding-based \uline{L}LM \uline{S}erving accelerator. Helios aims to bridge the fundamental gap between the dynamic nature of KV cache management in LLM serving and the distributed, non-uniform memory abstraction among NMP processing engines (PEs). To this end, we design both the intra-PE execution flow and the inter-PE communication primitives for distributed tiled attention execution. We further propose \textit{spatially-aware} KV cache allocation mechanism to balance the attention workload distribution while minimizing the inter-PE data transfer overhead. Compared with existing GPU/NMP designs, Helios achieves 3.25 times (geomean) speedup and 3.36 times (geomean) better energy efficiency, along with up to 72%/76% P50/P99 time-between-tokens degradation.

</details>

---

### 10. [Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm](https://arxiv.org/abs/2603.04799)

**基本信息**

- 🔗 arXiv: [`2603.04799`](https://arxiv.org/abs/2603.04799)
- 👥 作者: Nan Hou, Kangfei Zhao, Jiadong Xie 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04799.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是优化大语言模型（LLM）在数据筛选和查询中的应用方法，这直接关联到“化学大模型”主题中关于如何高效、智能地利用大模型处理化学数据（如分子库筛选、谱图查询）的核心挑战。

**📖 中文摘要**

本文针对大语言模型（LLM）在语义查询处理中的线性扫描瓶颈，提出了Clustering-Sampling-Voting (CSV)框架，将LLM调用复杂度降低到亚线性。该工作聚焦于优化LLM在数据处理管道中的使用效率，属于大模型应用方法学的研究。虽然应用场景是通用表格数据，但其核心思想——通过语义嵌入、聚类和采样来高效筛选与特定语义谓词相关的数据——可以迁移到化学信息学领域。例如，可用于从大型化学数据库（如PubChem）中高效筛选出符合特定结构或性质描述的分子，或者用于质谱数据库的快速检索与匹配。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are increasingly used for semantic query processing over large corpora. A set of semantic operators derived from relational algebra has been proposed to provide a unified interface for expressing such queries, among which the semantic filter operator serves as a cornerstone. Given a table T with a natural language predicate e, for each tuple in the relation, the execution of a semantic filter proceeds by constructing an input prompt that combines the predicate e with its content, querying the LLM, and obtaining the binary decision. However, this tuple-by-tuple evaluation necessitates a complete linear scan of the table, incurring prohibitive latency and token costs. Although recent work has attempted to optimize semantic filtering, it still does not break the linear LLM invocation barriers. To address this, we propose Clustering-Sampling-Voting (CSV), a new framework that reduces LLM invocations to sublinear complexity while providing error guarantees. CSV embeds tuples into semantic clusters, samples a small subset for LLM evaluation, and infers cluster-level labels via two proposed voting strategies: UniVote, which aggregates labels uniformly, and SimVote, which weights votes by semantic similarity. Moreover, CSV triggers re-clustering on ambiguous clusters to ensure robustness across diverse datasets. The results conducted on real-world datasets demonstrate that CSV reduces the number of LLM calls by 1.28-355x compared to the state-of-the-art approaches, while maintaining comparable effectiveness in terms of Accuracy and F1 score.

</details>

---

### 11. [MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models](https://arxiv.org/abs/2603.04800)

**基本信息**

- 🔗 arXiv: [`2603.04800`](https://arxiv.org/abs/2603.04800)
- 👥 作者: Lulu Hu, Wenhu Xiao, Xin Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04800.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对多模态大语言模型（MLLM）的模型压缩与量化技术，这直接属于“化学大模型”主题中关于模型轻量化、高效部署的关键技术路径。

**📖 中文摘要**

本文提出了MASQuant，一种用于多模态大语言模型（MLLM）的后训练量化框架。该工作旨在解决将现有的LLM量化技术（如SmoothQuant）应用于多模态模型时出现的模态间平滑错位和计算不变性问题。通过引入模态感知平滑和跨模态补偿，MASQuant实现了对双模态和三模态MLLM的稳定量化。这项研究属于大模型压缩和部署的前沿方向，对于推动包括化学多模态大模型（如结合分子结构图、文本描述和谱图数据）在内的各类大模型在资源受限环境（如边缘设备、实验室终端）中的实际应用具有重要价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Post-training quantization (PTQ) with computational invariance for Large Language Models~(LLMs) have demonstrated remarkable advances, however, their application to Multimodal Large Language Models~(MLLMs) presents substantial challenges. In this paper, we analyze SmoothQuant as a case study and identify two critical issues: Smoothing Misalignment and Cross-Modal Computational Invariance. To address these issues, we propose Modality-Aware Smoothing Quantization (MASQuant), a novel framework that introduces (1) Modality-Aware Smoothing (MAS), which learns separate, modality-specific smoothing factors to prevent Smoothing Misalignment, and (2) Cross-Modal Compensation (CMC), which addresses Cross-modal Computational Invariance by using SVD whitening to transform multi-modal activation differences into low-rank forms, enabling unified quantization across modalities. MASQuant demonstrates stable quantization performance across both dual-modal and tri-modal MLLMs. Experimental results show that MASQuant is competitive among the state-of-the-art PTQ algorithms. Source code: this https URL .

</details>

---

### 12. [Can LLMs Synthesize Court-Ready Statistical Evidence? Evaluating AI-Assisted Sentencing Bias Analysis for California Racial Justice Act Claims](https://arxiv.org/abs/2603.04804)

**基本信息**

- 🔗 arXiv: [`2603.04804`](https://arxiv.org/abs/2603.04804)
- 👥 作者: Aparna Komarla
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04804.pdf)

**💡 相关性分析**

满足标准1：论文探索了利用大语言模型（LLM）合成和解释领域特定（法律）数据分析结果，这种“大模型作为智能分析解释器”的应用范式，可直接应用于“化学大模型”和“质谱结构推理”中，用于解释模型预测、生成结构鉴定报告等。

**📖 中文摘要**

本文介绍了this http URL，一个开源平台，用于处理大量监狱记录并生成法庭可用的种族偏见量刑统计证据。该工作的一个核心探索是设计一个LLM驱动的解释层，能够将统计方法（如比值比、相对风险、卡方检验）的结果合成为连贯的叙述。这实质上是在研究如何利用大语言模型作为“描述性助手”，对复杂的、领域特定的（这里是法律）数据分析结果进行解释和报告生成。这种“大模型作为数据分析与解释接口”的模式，与化学信息学和质谱分析中利用大模型解释分子性质预测结果、解析质谱图并生成人类可读的结构推理报告的需求高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Resentencing in California remains a complex legal challenge despite legislative reforms like the Racial Justice Act (2020), which allows defendants to challenge convictions based on statistical evidence of racial disparities in sentencing and charging. Policy implementation lags behind legislative intent, creating a 'second-chance gap' where hundreds of resentencing opportunities remain unidentified. We present this http URL , an open-source platform that processes 95,000 prison records acquired under the California Public Records Act (CPRA) and generates court-ready statistical evidence of racial bias in sentencing for prima facie and discovery motions. We explore the design of an LLM-powered interpretive layer that synthesizes results from statistical methods like Odds Ratio, Relative Risk, and Chi-Square Tests into cohesive narratives contextualized with confidence intervals, sample sizes, and data limitations. Our evaluations comparing LLM performance to statisticians using the LLM-as-a-Judge framework suggest that AI can serve as a powerful descriptive assistant for real-time evidence generation when ethically incorporated in the analysis pipeline.

</details>

---

### 13. [Attention's Gravitational Field:A Power-Law Interpretation of Positional Correlation](https://arxiv.org/abs/2603.04805)

**基本信息**

- 🔗 arXiv: [`2603.04805`](https://arxiv.org/abs/2603.04805)
- 👥 作者: Edward Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大语言模型（LLM）注意力机制和位置编码的基础性探索与优化，这属于“化学大模型”主题中关于模型架构设计与可解释性研究的重要组成部分。

**📖 中文摘要**

本文探索了大语言模型（LLM）中位置关系与编码的底层原理，并引入了注意力引力场（AGF）的概念。通过将位置编码与语义嵌入解耦来优化模型架构，取得了优于主流编码方法的准确率。这项工作属于大模型基础架构和可解释性研究。虽然不直接涉及化学或质谱，但其对注意力机制和位置编码的深入分析与理论探索，为理解和改进任何序列建模任务（包括分子序列表示、质谱峰序列建模）中的位置感知能力提供了理论基础和方法启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper explores the underlying principles of positional relationships and encodings within Large Language Models (LLMs) and introduces the concept of the Attention Gravitational Field (AGF). By decoupling positional encodings from semantic embeddings, we optimize the model architecture and achieve superior accuracy compared to prevailing encoding methods. Furthermore, we provide an in-depth analysis of AGF, demonstrating its intrinsic consistency with learning and stability curves, as well as its empirical alignment with Newton's Law of Universal Gravitation. By offering a rigorous theoretical exploration of these phenomena, this work represents a significant step toward interpreting the Attention mechanism and unlocks new possibilities for future research in model optimization and interpretability.

</details>

---

### 14. [VISA: Value Injection via Shielded Adaptation for Personalized LLM Alignment](https://arxiv.org/abs/2603.04822)

**基本信息**

- 🔗 arXiv: [`2603.04822`](https://arxiv.org/abs/2603.04822)
- 👥 作者: Jiawei Chen, Tianzhuo Yang, Guoxi Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04822.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）的细粒度价值对齐方法，旨在控制模型的价值表达同时保持其事实一致性和通用能力。这对于构建可靠、安全、符合科学规范的“化学大模型”具有直接的相关性和重要性。

**📖 中文摘要**

本文提出了VISA框架，旨在解决大语言模型（LLM）与细粒度人类价值观对齐时的“对齐税”问题，即微调导致模型原有价值体系漂移、产生幻觉和语义信息丢失。VISA通过高精度价值检测器、语义到价值的翻译器和核心价值重写器，并采用组相对策略优化进行训练，以在价值精确性和语义完整性之间取得平衡。这项研究属于大模型对齐和安全的前沿领域。对于旨在应用于药物发现、材料设计等领域的化学大模型而言，确保其输出符合科学伦理、安全规范（即“价值对齐”）并保持事实一致性至关重要，该工作提供了有针对性的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Aligning Large Language Models (LLMs) with nuanced human values remains a critical challenge, as existing methods like Reinforcement Learning from Human Feedback (RLHF) often handle only coarse-grained attributes. In practice, fine-tuning LLMs on task-specific datasets to optimize value alignment inevitably incurs an alignment tax: the model's pre-calibrated value system drifts significantly due to latent bias absorption from training data, while the fine-tuning process also causes severe hallucinations and semantic information loss in generated responses. To address this, we propose VISA (Value Injection via Shielded Adaptation), a closed-loop framework designed to navigate this trade-off. VISA's architecture features a high-precision value detector, a semantic-to-value translator, and a core value-rewriter. The value-rewriter is trained via Group Relative Policy Optimization (GRPO) with a composite reward function that simultaneously optimizes for fine-grained value precision, and the preservation of semantic integrity. By learning an optimal policy to balance these competing objectives, VISA effectively mitigates the alignment tax while staying loyal to the original knowledge. Our experiments demonstrate that this approach enables precise control over a model's value expression while maintaining its factual consistency and general capabilities, significantly outperforming both standard fine-tuning methods and prompting-based baselines, including GPT-4o.

</details>

---

### 15. [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827)

**基本信息**

- 🔗 arXiv: [`2603.04827`](https://arxiv.org/abs/2603.04827)
- 👥 作者: Ben S. Southworth, Jonas A. Actor, Graham Harper 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04827.pdf)

**💡 相关性分析**

满足标准1：论文研究了一种新型神经网络架构（KANs）的高效训练方法。KANs因其可解释性和在科学建模中的潜力，是构建下一代“化学大模型”（用于分子性质预测、反应预测等）和“质谱结构推理”模型的有力候选架构之一，对其优化方法的研究直接相关。

**📖 中文摘要**

本文针对Kolmogorov-Arnold网络（KANs）的结构特性，提出了多级训练算法以加速其训练过程。KANs作为一种新兴的神经网络架构，因其可解释性和在科学发现任务中的潜力而受到关注。论文通过将KANs与具有幂ReLU激活的多通道MLP等价起来，并利用样条基函数的紧支撑特性，设计了一种通过均匀细化样条节点定义的自然模型序列进行多级训练的方法。这项工作展示了如何通过有原则的神经网络设计来获得可开发的结构，从而实现性能的显著提升。对于“化学大模型”和“质谱结构推理”任务，探索如KANs这类具有更好可解释性和潜在更高精度的新型模型架构具有明确的价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

</details>

---

### 16. [From Unfamiliar to Familiar: Detecting Pre-training Data via Gradient Deviations in Large Language Models](https://arxiv.org/abs/2603.04828)

**基本信息**

- 🔗 arXiv: [`2603.04828`](https://arxiv.org/abs/2603.04828)
- 👥 作者: Ruiqi Zhang, Lingxiang Wang, Hainan Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04828.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）预训练数据的检测方法，这属于大模型安全与隐私的重要议题。对于可能基于敏感或专有化学数据训练的“化学大模型”，该研究具有直接的相关性。

**📖 中文摘要**

本文提出了GDS方法，通过分析目标样本在训练过程中的梯度偏差分数来检测大语言模型（LLM）的预训练数据。该方法从优化视角出发，观察到样本在训练中从“不熟悉”到“熟悉”的转变会反映在梯度行为的系统性差异上，并利用这些差异构建轻量级分类器进行成员推断。这项工作属于大模型安全、隐私和版权保护的研究范畴。对于化学领域，如果未来构建了基于大量专有化学数据（如未公开的化合物库、专利数据）预训练的大模型，如何检测和防止其训练数据泄露将成为一个关键问题。该研究为此提供了可行的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pre-training data detection for LLMs is essential for addressing copyright concerns and mitigating benchmark contamination. Existing methods mainly focus on the likelihood-based statistical features or heuristic signals before and after fine-tuning, but the former are susceptible to word frequency bias in corpora, and the latter strongly depend on the similarity of fine-tuning data. From an optimization perspective, we observe that during training, samples transition from unfamiliar to familiar in a manner reflected by systematic differences in gradient behavior. Familiar samples exhibit smaller update magnitudes, distinct update locations in model components, and more sharply activated neurons. Based on this insight, we propose GDS, a method that identifies pre-training data by probing Gradient Deviation Scores of target samples. Specifically, we first represent each sample using gradient profiles that capture the magnitude, location, and concentration of parameter updates across FFN and Attention modules, revealing consistent distinctions between member and non-member data. These features are then fed into a lightweight classifier to perform binary membership inference. Experiments on five public datasets show that GDS achieves state-of-the-art performance with significantly improved cross-dataset transferability over strong baselines. Further interpretability analyse show gradient feature distribution differences, enabling practical and scalable pre-training data detection.

</details>

---

### 17. [Why Is RLHF Alignment Shallow? A Gradient Analysis](https://arxiv.org/abs/2603.04851)

**基本信息**

- 🔗 arXiv: [`2603.04851`](https://arxiv.org/abs/2603.04851)
- 👥 作者: Robin Young
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04851.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大语言模型（LLM）安全对齐机制（RLHF）的深度理论分析，指出了现有方法的局限性并提出了改进方向。这对于构建安全、可靠、符合科学规范的“化学大模型”至关重要，属于该主题下的基础理论与方法研究。

**📖 中文摘要**

本文从梯度分析的角度，理论上解释了为什么基于人类反馈的强化学习（RLHF）对大语言模型（LLM）的安全对齐是“浅层”的。论文证明，基于梯度的对齐本质上集中在决定危害的位置，并在此之后消失，因此标准对齐目标无法产生深度对齐。作者进而引入了“危害信息”的概念，并推导出一个基于恢复惩罚的目标，可以在所有位置创建梯度信号。这项工作是针对大模型对齐机制的基础性理论分析，对于理解如何更有效地对齐化学、生物等科学领域的大模型（确保其输出符合科学事实、安全规范）具有重要的理论指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Why is safety alignment in LLMs shallow? We prove that gradient-based alignment inherently concentrates on positions where harm is decided and vanishes beyond. Using a martingale decomposition of sequence-level harm, we derive an exact characterization of alignment gradients. The gradient at position $t$ equals the covariance between the conditional expected harm and the score function. This implies that positions beyond the harm horizon where the output's harmfulness is already determined receive zero gradient signal during training. This explains empirical observations that KL divergence between aligned and base models concentrates on early tokens. Consequently, standard alignment objectives cannot produce deep alignment, regardless of optimization quality. We introduce the concept of harm information $I_t$, which quantifies each position's influence on harm, and prove that equilibrium KL divergence tracks this quantity. Finally, we derive an objective based on recovery penalties that creates gradient signal at all positions, providing theoretical grounding for empirically successful data augmentation techniques.

</details>

---

### 18. [Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models](https://arxiv.org/abs/2603.04893)

**基本信息**

- 🔗 arXiv: [`2603.04893`](https://arxiv.org/abs/2603.04893)
- 👥 作者: Sean Lamont, Christian Walder, Paul Montague 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04893.pdf)

**💡 相关性分析**

满足标准1：论文研究了一种提升扩散语言模型生成多样性的方法。在“化学大模型”和“质谱结构推理”中，许多任务（如分子设计、结构枚举）需要模型能够生成多样且合理的候选输出，该研究为此提供了有效的技术工具。

**📖 中文摘要**

本文针对扩散语言模型在文本生成中输出多样性不足、容易陷入重复模式的问题，提出了一种无需训练、低成本的干预方法，以增强生成多样性。该方法在批次内顺序修改中间样本，使每个样本在特征空间中被先前样本“排斥”，从而主动惩罚冗余。该方法简单修改了采样过程，为当前和未来的扩散语言模型在需要多样化解决方案搜索的任务（如代码生成、数学问题求解）中提供了即时的低成本改进。对于“化学大模型”和“质谱结构推理”，在求解分子逆向合成路线、为给定质谱生成多种可能候选结构等需要探索多样化解空间的任务中，这种提升生成多样性的技术具有直接的应用价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diverse outputs in text generation are necessary for effective exploration in complex reasoning tasks, such as code generation and mathematical problem solving. Such Pass@$k$ problems benefit from distinct candidates covering the solution space. However, traditional sampling approaches often waste computational resources on repetitive failure modes. While Diffusion Language Models have emerged as a competitive alternative to the prevailing Autoregressive paradigm, they remain susceptible to this redundancy, with independent samples frequently collapsing into similar modes. To address this, we propose a training free, low cost intervention to enhance generative diversity in Diffusion Language Models. Our approach modifies intermediate samples in a batch sequentially, where each sample is repelled from the feature space of previous samples, actively penalising redundancy. Unlike prior methods that require retraining or beam search, our strategy incurs negligible computational overhead, while ensuring that each sample contributes a unique perspective to the batch. We evaluate our method on the HumanEval and GSM8K benchmarks using the LLaDA-8B-Instruct model. Our results demonstrate significantly improved diversity and Pass@$k$ performance across various temperature settings. As a simple modification to the sampling process, our method offers an immediate, low-cost improvement for current and future Diffusion Language Models in tasks that benefit from diverse solution search. We make our code available at this https URL .

</details>

---

### 19. [Differentially Private Multimodal In-Context Learning](https://arxiv.org/abs/2603.04894)

**基本信息**

- 🔗 arXiv: [`2603.04894`](https://arxiv.org/abs/2603.04894)
- 👥 作者: Ivoline C. Ngong, Zarreen Reza, Joseph P. Near
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04894.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是实现具有差分隐私保证的多模态大模型上下文学习。这对于在数据敏感的化学、生物医学领域安全地开发和部署“化学大模型”和“质谱结构推理”模型具有关键意义，属于该主题下的隐私与安全研究方向。

**📖 中文摘要**

本文提出了差分隐私多模态任务向量（DP-MTV），这是第一个支持具有正式差分隐私保证的多模态上下文学习的框架。该框架通过将数百个演示聚合到激活空间中的紧凑任务向量中，避免了隐私成本随处理令牌数量增长的问题。DP-MTV将私有数据划分为不相交的块，应用每层裁剪来限制敏感性，并向聚合添加校准噪声，仅需单次噪声添加即可支持无限的推理查询。这项工作属于隐私保护机器学习的前沿，对于在化学和生物医学领域部署大模型至关重要，因为这些领域的数据（如患者信息、专有分子结构）通常高度敏感。该研究使得在保护隐私的前提下，利用多模态数据（如分子结构图+文本描述+谱图）进行少样本或上下文学习成为可能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-language models are increasingly applied to sensitive domains such as medical imaging and personal photographs, yet existing differentially private methods for in-context learning are limited to few-shot, text-only settings because privacy cost scales with the number of tokens processed. We present Differentially Private Multimodal Task Vectors (DP-MTV), the first framework enabling many-shot multimodal in-context learning with formal $(\varepsilon, \delta)$-differential privacy by aggregating hundreds of demonstrations into compact task vectors in activation space. DP-MTV partitions private data into disjoint chunks, applies per-layer clipping to bound sensitivity, and adds calibrated noise to the aggregate, requiring only a single noise addition that enables unlimited inference queries. We evaluate on eight benchmarks across three VLM architectures, supporting deployment with or without auxiliary data. At $\varepsilon=1.0$, DP-MTV achieves 50% on VizWiz compared to 55% non-private and 35% zero-shot, preserving most of the gain from in-context learning under meaningful privacy constraints.

</details>

---

### 20. [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900)

**基本信息**

- 🔗 arXiv: [`2603.04900`](https://arxiv.org/abs/2603.04900)
- 👥 作者: Shuo Yang, Soyeon Caren Han, Xueqi Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04900.pdf)

**💡 相关性分析**

满足标准1：论文研究了大语言模型智能体（LLM Agent）工具使用策略的自我进化优化框架。构建能够调用专业工具（如化学数据库、计算软件、谱图库）的智能体，是“化学大模型”和“质谱结构推理”走向实际应用的重要形态，该研究为此提供了核心的优化方法。

**📖 中文摘要**

本文提出了EvoTool，一个通过无梯度进化范式自我进化优化模块化工具使用策略的框架。EvoTool将智能体的工具使用策略分解为四个模块，并通过三个新机制在自我改进循环中迭代改进它们。该工作属于智能体（Agent）和工具学习（Tool Learning）的研究范畴，旨在提升LLM智能体使用外部工具解决复杂任务的能力。在化学信息学和质谱分析中，可以构建智能体来调用各种计算化学工具、数据库查询API、谱图解析算法等，以完成复杂的分子设计或结构鉴定工作流。EvoTool为优化此类化学信息学智能体的工具使用策略提供了方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

</details>

---

### 21. [Alignment Backfire: Language-Dependent Reversal of Safety Interventions Across 16 Languages in LLM Multi-Agent Systems](https://arxiv.org/abs/2603.04904)

**基本信息**

- 🔗 arXiv: [`2603.04904`](https://arxiv.org/abs/2603.04904)
- 👥 作者: Hiroki Fukui
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04904.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）对齐干预的跨语言效应与局限性。这对于评估和确保“化学大模型”在不同地区、不同语言使用者中的安全性、可靠性和行为一致性具有重要的警示和指导意义。

**📖 中文摘要**

本文通过跨16种语言和三个模型系列的1584个多智能体模拟实验，研究了大语言模型（LLM）中对齐干预的效果。研究发现，对齐干预会产生“对齐反效果”：在英语中减少集体病理，但在日语中却放大它。这表明安全在英语中的验证并不能转移到其他语言，提示级别的干预无法覆盖语言空间级别的约束。这项研究将对齐重新定义为一种受风险稳态和医源性效应影响的行为干预。对于旨在全球范围内应用的“化学大模型”，必须考虑其在不同语言和文化背景下的安全性和行为一致性，该研究揭示了这一挑战的严重性和复杂性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In perpetrator treatment, a recurring observation is the dissociation between insight and action: offenders articulate remorse yet behavioral change does not follow. We report four preregistered studies (1,584 multi-agent simulations across 16 languages and three model families) demonstrating that alignment interventions in large language models produce a structurally analogous phenomenon: surface safety that masks or generates collective pathology and internal dissociation. In Study 1 (N = 150), increasing alignment-instructed agents reduced collective pathology in English (g = -1.844, p < .0001) but amplified it in Japanese (g = +0.771, p = .038)--a directional reversal we term "alignment backfire." Study 2 (N = 1,174) extended to 16 languages: alignment-induced dissociation was near-universal (15/16 languages; beta = 0.0667, p < .0001), while collective pathology bifurcated along cultural-linguistic lines (interaction beta = 0.0684, p = .0003), correlating with Power Distance Index (r = 0.474, p = .064). Study 3 (N = 180) tested individuation as countermeasure; individuated agents became the primary source of both pathology and dissociation (DI = +1.120) with conformity above 84%--demonstrating iatrogenesis. Study 4 (N = 80) validated patterns across Llama 3.3 70B, GPT-4o-mini, and Qwen3-Next-80B-A3B, confirming English safety is model-general while Japanese backfire is model-specific. These findings reframe alignment as a behavioral intervention subject to risk homeostasis and iatrogenesis. Language space--the linguistic, pragmatic, and cultural properties inherited from training data--structurally determines alignment outcomes. Safety validated in English does not transfer to other languages, and prompt-level interventions cannot override language-space-level constraints.

</details>

---

### 22. [BandPO: Bridging Trust Regions and Ratio Clipping via Probability-Aware Bounds for LLM Reinforcement Learning](https://arxiv.org/abs/2603.04918)

**基本信息**

- 🔗 arXiv: [`2603.04918`](https://arxiv.org/abs/2603.04918)
- 👥 作者: Yuan Li, Bo Wang, Yufei Gao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04918.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）强化学习训练算法的改进（BandPO）。强化学习是优化“化学大模型”（如用于分子设计、反应优化）性能的重要手段，对该领域核心训练算法的研究具有直接相关性。

**📖 中文摘要**

本文针对大语言模型强化学习中的近端约束问题，提出了Band约束策略优化（BandPO）。BandPO用Band算子取代了PPO中的标准裁剪机制，Band是一个统一的理论算子，它将由f-散度定义的信任区域投影到动态的、概率感知的裁剪区间中。理论分析证实，Band有效解决了低概率动作向上更新边际受限的探索瓶颈。这项工作属于大模型强化学习优化算法的基础研究。在利用强化学习优化化学大模型（例如，用于分子生成的策略）时，稳定高效的训练算法至关重要，BandPO为此提供了一种有潜力的新方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Proximal constraints are fundamental to the stability of the Large Language Model reinforcement learning. While the canonical clipping mechanism in PPO serves as an efficient surrogate for trust regions, we identify a critical bottleneck: fixed bounds strictly constrain the upward update margin of low-probability actions, disproportionately suppressing high-advantage tail strategies and inducing rapid entropy collapse. To address this, we introduce Band-constrained Policy Optimization (BandPO). BandPO replaces canonical clipping with Band, a unified theoretical operator that projects trust regions defined by f-divergences into dynamic, probability-aware clipping intervals. Theoretical analysis confirms that Band effectively resolves this exploration bottleneck. We formulate this mapping as a convex optimization problem, guaranteeing a globally optimal numerical solution while deriving closed-form solutions for specific divergences. Extensive experiments across diverse models and datasets demonstrate that BandPO consistently outperforms canonical clipping and Clip-Higher, while robustly mitigating entropy collapse.

</details>

---

### 23. [$\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](https://arxiv.org/abs/2603.04948)

**基本信息**

- 🔗 arXiv: [`2603.04948`](https://arxiv.org/abs/2603.04948)
- 👥 作者: Peihao Wang, Ruisi Cai, Zhen Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04948.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种新型的大语言模型（LLM）推理时优化框架，通过梯度下降在潜在空间改进生成策略。这种提升模型在线推理性能的方法，可应用于优化“化学大模型”在复杂问题求解（如分子逆合成规划、谱图解析）中的生成质量。

**📖 中文摘要**

本文提出了$\nabla$-Reasoner，一种迭代生成框架，它将对词元logits的可微分优化集成到解码循环中，以在线优化策略。其核心组件，可微分文本优化（DTO），利用来自LLM似然和奖励模型的梯度信号来细化文本表示。理论上，论文展示了在样本空间中进行推理时梯度下降以最大化奖励，与通过KL正则化强化学习对齐LLM策略是对偶的。这项工作属于大模型推理时优化和增强的前沿探索。对于“化学大模型”和“质谱结构推理”，在模型生成分子结构描述或质谱解析结果时，利用类似的推理时优化技术来提升输出的准确性和一致性，是一个值得探索的新方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

</details>

---

### 24. [WaterSIC: information-theoretically (near) optimal linear layer quantization](https://arxiv.org/abs/2603.04956)

**基本信息**

- 🔗 arXiv: [`2603.04956`](https://arxiv.org/abs/2603.04956)
- 👥 作者: Egor Lifar, Semyon Savkin, Or Ordentlich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04956.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大语言模型（LLM）的量化技术，这是构建和优化“化学大模型”所需的关键底层技术之一。

**📖 中文摘要**

本文提出了一种名为WaterSIC的新型算法，用于将密集线性层转换为低精度表示。该算法从信息论角度分析了压缩长度与输出差异之间的权衡，并证明其性能接近理论极限。作者将WaterSIC应用于Llama和Qwen系列大语言模型，在1到4比特的量化率上实现了最先进的性能。这项工作为大语言模型（LLM）的高效部署提供了关键的量化工具，属于化学信息学中“化学大模型”主题下的模型优化与压缩技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper considers the problem of converting a given dense linear layer to low precision. The tradeoff between compressed length and output discrepancy is analyzed information theoretically (IT). It is shown that a popular GPTQ algorithm may have an arbitrarily large gap to the IT limit. To alleviate this problem, a novel algorithm, termed ''WaterSIC'', is proposed and is shown to be within a rate gap of 0.255 bits to the IT limit, uniformly over all possible covariance matrices of input activations. The key innovation of WaterSIC's is to allocate different quantization rates to different columns (in-features) of the weight matrix, mimicking the classical IT solution known as ''waterfilling''. Applying WaterSIC to the Llama and Qwen family of LLMs establishes new state-of-the-art performance for all quantization rates from 1 to 4 bits.

</details>

---

### 25. [Replaying pre-training data improves fine-tuning](https://arxiv.org/abs/2603.04964)

**基本信息**

- 🔗 arXiv: [`2603.04964`](https://arxiv.org/abs/2603.04964)
- 👥 作者: Suhas Kotha, Percy Liang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04964.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大语言模型的训练策略与领域适应，直接关系到如何更有效地构建和微调“化学大模型”。

**📖 中文摘要**

本文研究了在针对特定领域（如数学）微调语言模型时，重放通用预训练数据的效果。作者发现，在微调过程中重放通用数据可以显著提高目标任务的性能和数据效率。研究在受控的预训练环境中进行，并在8B参数模型的实践中得到验证，成功提升了智能体网络导航的成功率和特定语言的问答准确率。这项工作为大语言模型（包括潜在的化学领域大模型）的高效领域适应提供了重要的训练策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To obtain a language model for a target domain (e.g. math), the current paradigm is to pre-train on a vast amount of generic web text and then fine-tune on the relatively limited amount of target data. Typically, generic data is only mixed in during fine-tuning to prevent catastrophic forgetting of the generic domain. We surprisingly find that replaying the generic data during fine-tuning can actually improve performance on the (less related) target task. Concretely, in a controlled pre-training environment with 4M target tokens, 4B total tokens, and 150M parameter models, generic replay increases target data efficiency by up to $1.87\times$ for fine-tuning and $2.06\times$ for mid-training. We further analyze data schedules that introduce target data during pre-training and find that replay helps more when there is less target data present in pre-training. We demonstrate the success of replay in practice for fine-tuning 8B parameter models, improving agentic web navigation success by $4.5\%$ and Basque question-answering accuracy by $2\%$.

</details>

---

### 26. [When Weak LLMs Speak with Confidence, Preference Alignment Gets Stronger](https://arxiv.org/abs/2603.04968)

**基本信息**

- 🔗 arXiv: [`2603.04968`](https://arxiv.org/abs/2603.04968)
- 👥 作者: Amirabbas Afzali, Myeongho Jeon, Maria Brbic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04968.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大型语言模型（LLM）的偏好对齐与优化，这是构建安全、可靠、符合领域专家需求的“化学大模型”的关键步骤。

**📖 中文摘要**

本文提出了一种新的偏好对齐框架——置信度加权偏好优化（CW-PO）。该框架利用一个较弱的大型语言模型（LLM）作为标注者，仅选择其高置信度的样本进行训练，从而在显著降低人工标注成本的同时，甚至能超越使用全部人工标注数据训练的标准DPO方法。这项工作为对齐大型语言模型（包括化学领域模型）与人类价值观提供了一种高效、低成本的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Preference alignment is an essential step in adapting large language models (LLMs) to human values, but existing approaches typically depend on costly human annotations or large-scale API-based models. We explore whether a weak LLM can instead act as an effective annotator. We surprisingly find that selecting only a subset of a weak LLM's highly confident samples leads to substantially better performance than using full human annotations. Building on this insight, we propose Confidence-Weighted Preference Optimization (CW-PO), a general framework that re-weights training samples by a weak LLM's confidence and can be applied across different preference optimization objectives. Notably, the model aligned by CW-PO with just 20% of human annotations outperforms the model trained with 100% of annotations under standard DPO. These results suggest that weak LLMs, when paired with confidence weighting, can dramatically reduce the cost of preference alignment while even outperforming methods trained on fully human-labeled data.

</details>

---

### 27. [Mixture of Universal Experts: Scaling Virtual Width via Depth-Width Transformation](https://arxiv.org/abs/2603.04971)

**基本信息**

- 🔗 arXiv: [`2603.04971`](https://arxiv.org/abs/2603.04971)
- 👥 作者: Yilong Chen, Naibin Gu, Junyuan Shang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04971.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大语言模型（LLM）的架构创新与扩展，直接关系到如何设计和构建更强大、更高效的“化学大模型”。

**📖 中文摘要**

本文提出了通用专家混合（MOUE）模型，这是一种对混合专家（MoE）模型的泛化，引入了一个新的扩展维度：虚拟宽度。MOUE旨在跨层重用通用的、与层无关的专家池，在固定的每令牌激活预算下将深度转换为虚拟宽度。该方法在多个扩展机制中始终优于匹配的MoE基线，并为MoE架构揭示了一个新的扩展维度。这项工作为大语言模型（包括化学大模型）的架构设计与高效扩展提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture-of-Experts (MoE) decouples model capacity from per-token computation, yet their scalability remains limited by the physical dimensions of depth and width. To overcome this, we propose Mixture of Universal Experts (MOUE),a MoE generalization introducing a novel scaling dimension: Virtual Width. In general, MoUE aims to reuse a universal layer-agnostic expert pool across layers, converting depth into virtual width under a fixed per-token activation budget. However, two challenges remain: a routing path explosion from recursive expert reuse, and a mismatch between the exposure induced by reuse and the conventional load-balancing objectives. We address these with three core components: a Staggered Rotational Topology for structured expert sharing, a Universal Expert Load Balance for depth-aware exposure correction, and a Universal Router with lightweight trajectory state for coherent multi-step routing. Empirically, MoUE consistently outperforms matched MoE baselines by up to 1.3% across scaling regimes, enables progressive conversion of existing MoE checkpoints with up to 4.2% gains, and reveals a new scaling dimension for MoE architectures.

</details>

---

### 28. [Functionality-Oriented LLM Merging on the Fisher--Rao Manifold](https://arxiv.org/abs/2603.04972)

**基本信息**

- 🔗 arXiv: [`2603.04972`](https://arxiv.org/abs/2603.04972)
- 👥 作者: Jiayu Wang, Zuojun Ye, Wenpeng Yin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04972.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕多个大型语言模型（LLM）的权重合并，这是构建集成化、多功能的“化学大模型”的一种重要技术路径。

**📖 中文摘要**

本文提出了一种在Fisher-Rao流形上基于功能性的LLM权重空间合并方法。该方法将模型合并问题表述为计算Fisher-Rao流形上的加权Karcher均值，这等价于最小化预测分布之间的基于KL散度的函数距离。与在欧几里得空间中进行参数平均的现有方法相比，该方法在合并模型的数量和异质性增加时能保持稳定，并持续优于先前的基线方法。这项工作为整合多个针对不同化学任务微调的专家模型，构建统一的“化学大模型”提供了理论基础和实用算法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective. We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

</details>

---

### 29. [VRM: Teaching Reward Models to Understand Authentic Human Preferences](https://arxiv.org/abs/2603.04974)

**基本信息**

- 🔗 arXiv: [`2603.04974`](https://arxiv.org/abs/2603.04974)
- 👥 作者: Biao Liu, Ning Xu, Junming Yang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04974.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大型语言模型（LLM）的奖励建模与对齐，这是确保“化学大模型”输出可靠、安全、符合科学规范的关键技术。

**📖 中文摘要**

本文提出了变分奖励建模（VRM）框架，旨在通过显式建模人类偏好判断的评估过程来改进大型语言模型（LLM）的对齐。VRM将高维目标权重和低维语义特征作为潜变量纳入，并通过变分推断技术进行推断。理论分析表明，与传统奖励模型相比，VRM可以实现更紧的泛化误差界。在基准数据集上的实验证明，VRM在捕捉真实人类偏好方面显著优于现有方法。这项工作为训练更符合化学专家价值观和需求的“化学大模型”提供了先进的奖励建模方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have achieved remarkable success across diverse natural language tasks, yet the reward models employed for aligning LLMs often encounter challenges of reward hacking, where the approaches predominantly rely on directly mapping prompt-response pairs to scalar scores, which may inadvertently capture spurious correlations rather than authentic human preferences. In contrast, human evaluation employs a sophisticated process that initially weighs the relative importance of multiple high-dimensional objectives according to the prompt context, subsequently evaluating response quality through low-dimensional semantic features such as logical coherence and contextual appropriateness. Motivated by this consideration, we propose VRM, i.e., Variational Reward Modeling, a novel framework that explicitly models the evaluation process of human preference judgments by incorporating both high-dimensional objective weights and low-dimensional semantic features as latent variables, which are inferred through variational inference techniques. Additionally, we provide a theoretical analysis showing that VRM can achieve a tighter generalization error bound compared to the traditional reward model. Extensive experiments on benchmark datasets demonstrate that VRM significantly outperforms existing methods in capturing authentic human preferences.

</details>

---

### 30. [Receding-Horizon Maximum-Likelihood Estimation of Neural-ODE Dynamics and Thresholds from Event Cameras](https://arxiv.org/abs/2603.05011)

**基本信息**

- 🔗 arXiv: [`2603.05011`](https://arxiv.org/abs/2603.05011)
- 👥 作者: Kazumune Hashimoto, Kazunobu Serizawa, Masako Kishida
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05011.pdf)

**💡 相关性分析**

满足标准1：论文提出的神经ODE与标记点过程模型，为分析时序数据（如质谱信号）和推理潜在动力学结构提供了方法论工具，与“质谱结构推理”主题相关。

**📖 中文摘要**

本文提出了一种基于滑动窗口的最大似然估计方法，用于从事件相机（Event Camera）的异步亮度变化事件流中在线识别连续时间动力学。所研究的潜在状态遵循神经常微分方程（Neural ODE），并通过可微的状态到图像模型映射到预测的对数强度。事件被建模为历史相关的标记点过程，其条件强度是对比度阈值触发的平滑替代。这项工作为处理基于事件的传感器数据提供了先进的时序建模和参数估计框架。虽然应用背景是计算机视觉，但其核心方法——神经ODE与点过程建模——在原理上可迁移至分析质谱仪产生的时间序列或离子流数据，用于“质谱结构推理”中的动力学行为建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Event cameras emit asynchronous brightness-change events where each pixel triggers an event when the last event exceeds a threshold, yielding a history-dependent measurement model. We address online maximum-likelihood identification of continuous-time dynamics from such streams. The latent state follows a Neural ODE and is mapped to predicted log-intensity through a differentiable state-to-image model. We model events with a history-dependent marked point process whose conditional intensity is a smooth surrogate of contrast-threshold triggering, treating the contrast threshold as an unknown parameter. The resulting log-likelihood consists of an event term and a compensator integral. We propose a receding-horizon estimator that performs a few gradient steps per update on a receding horizon window. For streaming evaluation, we store two scalars per pixel (last-event time and estimated log-intensity at that time) and approximate the compensator via Monte Carlo pixel subsampling. Synthetic experiments demonstrate joint recovery of dynamics parameters and the contrast threshold, and characterize accuracy--latency trade-offs with respect to the window length.

</details>

---

### 31. [Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination](https://arxiv.org/abs/2603.05040)

**基本信息**

- 🔗 arXiv: [`2603.05040`](https://arxiv.org/abs/2603.05040)
- 👥 作者: Hyuntae Park, Yeachan Kim, SangKeun Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05040.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及通过多模态（文本+图像）增强大型语言模型的推理能力，这种方法论对于构建能处理化学结构式、光谱图等多模态信息的“化学大模型”具有启发意义。

**📖 中文摘要**

本文提出了Imagine框架，一个基于机器想象的零样本常识推理框架。该框架通过将机器生成的图像作为视觉信号补充到文本输入中，来增强预训练语言模型（PLM）的推理能力。Imagine将图像生成器直接嵌入推理流程，并构建合成数据集来模拟视觉问答场景。在多个常识推理基准测试上的评估表明，Imagine显著优于现有的零样本方法，甚至超越了先进的大型语言模型。这项工作展示了多模态信息（特别是机器生成的视觉上下文）对于提升模型（包括化学领域模型）在复杂推理任务中性能的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

</details>

---

### 32. [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)

**基本信息**

- 🔗 arXiv: [`2603.05044`](https://arxiv.org/abs/2603.05044)
- 👥 作者: Sicheng Fan, Qingyun Shi, Shengze Xu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05044.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及利用LLM知识构建和训练能在特定环境（可类比为化学信息环境）中自主交互的智能体，这与开发面向化学领域的智能大模型或辅助工具的研究方向相关。

**📖 中文摘要**

本文介绍了WebFactory，一个用于GUI智能体的全自动闭环强化学习流水线，旨在将大型语言模型（LLM）编码的互联网知识系统地压缩为高效的、 grounded 的行动。该流水线包括可扩展的环境合成、知识感知的任务生成、LLM驱动的轨迹收集、分解奖励的RL训练和系统化的智能体评估。研究表明，仅在WebFactory中10个网站的合成数据上训练，其智能体就能达到与在更大规模环境的人类标注数据上训练的GUI智能体相当的性能。这项工作为将被动互联网知识转化为主动的、 grounded 的智能体智能提供了一个可扩展且经济高效的范式。虽然应用场景是网页交互，但其核心思想——利用LLM知识引导智能体在特定领域（如化学数据库）进行探索和交互——对于开发能自动检索、整合化学信息的“化学大模型”或智能体具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

</details>

---

### 33. [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046)

**基本信息**

- 🔗 arXiv: [`2603.05046`](https://arxiv.org/abs/2603.05046)
- 👥 作者: Rongzhi Li, Hitomi Yanaka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05046.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大型语言模型（LLM）的多语言扩展与参数高效架构（MoE），这对于构建能处理全球化学文献和数据的“化学大模型”具有直接相关性。

**📖 中文摘要**

本文提出了NeuronMoE方法，通过分析所有Transformer组件中语言特定的神经元，来指导基于经验测量的跨语言神经元多样性为每一层分配专家，从而将大型语言模型高效扩展到低资源语言。该方法应用于Llama-3.2-3B模型，针对希腊语、土耳其语和匈牙利语等低资源语言，在匹配LayerMoE基线性能的同时，实现了约40%的平均参数减少。这项工作为构建多语言、参数高效的“化学大模型”（例如，能够处理不同语言文献中的化学信息）提供了模型架构和训练策略上的见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We propose $\textbf{NeuronMoE}$, a method that analyzes language-specific neurons across all transformer components to guide expert allocation per layer based on empirically measured cross-lingual neuron diversity. Applied to Llama-3.2-3B for low-resource languages (Greek, Turkish, and Hungarian), this approach achieves approximately 40% average parameter reduction while matching the performance of the LayerMoE baseline. We find that low-resource language experts independently develop neuron specialization patterns mirroring the high-resource language, which are concentrated in early and late layers. This reveals potential universal architectural principles in how multilingual models organize linguistic knowledge.

</details>

---

### 34. [CLIP-driven Zero-shot Learning with Ambiguous Labels](https://arxiv.org/abs/2603.05053)

**基本信息**

- 🔗 arXiv: [`2603.05053`](https://arxiv.org/abs/2603.05053)
- 👥 作者: Jinfu Fan, Jiangnan Li, Xiaowen Yan 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05053.pdf)

**💡 相关性分析**

满足标准1：论文提出的处理噪声和模糊标签的框架，其方法论可应用于处理质谱数据标注中的不确定性，从而服务于“质谱结构推理”任务。

**📖 中文摘要**

本文提出了一种新的基于CLIP驱动的部分标签零样本学习（CLIP-PZSL）框架，用于处理训练实例标签存在噪声和模糊性的情况。该框架利用CLIP提取实例和标签特征，通过语义挖掘块融合这些特征以提取有区分度的标签嵌入，并引入部分零样本损失来根据候选标签与实例的相关性分配权重，使实例和标签嵌入的语义不匹配最小化。在多个数据集上的综合实验证明了CLIP-PZSL的优势。这项工作为在标签不完美的情况下训练鲁棒的视觉-语言模型提供了方法，其思想可迁移至化学信息学中处理标注不精确的质谱-结构对应数据，辅助“质谱结构推理”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Zero-shot learning (ZSL) aims to recognize unseen classes by leveraging semantic information from seen classes, but most existing methods assume accurate class labels for training instances. However, in real-world scenarios, noise and ambiguous labels can significantly reduce the performance of ZSL. To address this, we propose a new CLIP-driven partial label zero-shot learning (CLIP-PZSL) framework to handle label ambiguity. First, we use CLIP to extract instance and label features. Then, a semantic mining block fuses these features to extract discriminative label embeddings. We also introduce a partial zero-shot loss, which assigns weights to candidate labels based on their relevance to the instance and aligns instance and label embeddings to minimize semantic mismatch. As the training goes on, the ground-truth labels are progressively identified, and the refined labels and label embeddings in turn help improve the semantic alignment of instance and label features. Comprehensive experiments on several datasets demonstrate the advantage of CLIP-PZSL.

</details>

---

### 35. [MI-DETR: A Strong Baseline for Moving Infrared Small Target Detection with Bio-Inspired Motion Integration](https://arxiv.org/abs/2603.05071)

**基本信息**

- 🔗 arXiv: [`2603.05071`](https://arxiv.org/abs/2603.05071)
- 👥 作者: Nian Liu, Jin Gao, Shubo Lin 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05071.pdf)

**💡 相关性分析**

满足标准1：论文提出的双通路（外观+运动）信息整合架构，为解决“质谱结构推理”中需融合多维信号（如质荷比强度与保留时间/离子迁移率）的挑战提供了有启发性的模型设计方案。

**📖 中文摘要**

本文提出了MI-DETR，一个受生物学启发的双通路检测器，用于移动红外小目标检测。它通过视网膜启发的元胞自动机（RCA）将原始帧序列转换为运动图，从而实现了类似小细胞的外观通路和类似大细胞的运动通路。一个Parvocellular-Magnocellular互连块促进了两个通路之间的双向特征交互。最后，一个RT-DETR解码器对来自两个通路的特征进行操作以产生检测结果。该方法在三个常用的红外小目标检测基准上取得了强劲的性能。虽然应用领域是红外目标检测，但其核心创新——显式建模并整合外观与运动信息的多通路架构——为解决“质谱结构推理”中需要同时考虑谱图特征（外观）和可能的时序/色谱变化（运动）的复杂问题提供了新颖的模型设计思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Infrared small target detection (ISTD) is challenging because tiny, low-contrast targets are easily obscured by complex and dynamic backgrounds. Conventional multi-frame approaches typically learn motion implicitly through deep neural networks, often requiring additional motion supervision or explicit alignment modules. We propose Motion Integration DETR (MI-DETR), a bio-inspired dual-pathway detector that processes one infrared frame per time step while explicitly modeling motion. First, a retina-inspired cellular automaton (RCA) converts raw frame sequences into a motion map defined on the same pixel grid as the appearance image, enabling parvocellular-like appearance and magnocellular-like motion pathways to be supervised by a single set of bounding boxes without extra motion labels or alignment operations. Second, a Parvocellular-Magnocellular Interconnection (PMI) Block facilitates bidirectional feature interaction between the two pathways, providing a biologically motivated intermediate interconnection mechanism. Finally, a RT-DETR decoder operates on features from the two pathways to produce detection results. Surprisingly, our proposed simple yet effective approach yields strong performance on three commonly used ISTD benchmarks. MI-DETR achieves 70.3% mAP@50 and 72.7% F1 on IRDST-H (+26.35 mAP@50 over the best multi-frame baseline), 98.0% mAP@50 on DAUB-R, and 88.3% mAP@50 on ITSDT-15K, demonstrating the effectiveness of biologically inspired motion-appearance integration. Code is available at this https URL .

</details>

---

### 36. [TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling](https://arxiv.org/abs/2603.05094)

**基本信息**

- 🔗 arXiv: [`2603.05094`](https://arxiv.org/abs/2603.05094)
- 👥 作者: Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05094.pdf)

**💡 相关性分析**

满足标准2：论文贡献了一个大规模、高质量、针对特定领域的音频-文本指令数据集，其数据构建协议和流程可为创建用于“化学大模型”或“质谱结构推理”的专用数据集（如质谱-分子结构对、光谱-文本描述对）提供方法论参考。

**📖 中文摘要**

本文介绍了TW-Sound580K，一个通过验证-生成-批判（VGC）协议开发的台湾地区音频-文本指令数据集。该流水线利用双ASR验证过滤原始音频片段，随后使用教师模型将其扩展为58万对高保真指令对。数据集的效用通过Tai-LALM得到证明，该模型微调了一个DeSTA 2.5-Audio初始化的主干网络，并集成了动态双ASR仲裁策略以在推理期间优化转录选择。在TAU基准测试中，Tai-LALM达到了49.1%的准确率。这项工作展示了如何通过严格的语料库管理和动态仲裁来构建和提升针对特定领域（此处为方言）的大规模音频-语言模型。其数据构建和模型适配方法论对于构建化学领域的多模态（如光谱-文本）大模型具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio-Language Models (LALMs) typically struggle with localized dialectal prosody due to the scarcity of specialized corpora. We present TW-Sound580K, a Taiwanese audio-text instruction dataset developed through a Verify-Generate-Critique (VGC) protocol. This pipeline leverages Dual-ASR validation to filter 522K raw clips, subsequently expanding them into 580,000 high-fidelity instruction pairs using a teacher model. The dataset's utility is demonstrated through Tai-LALM, which fine-tunes a DeSTA 2.5-Audio-initialized backbone and incorporates a dynamic Dual-ASR Arbitration strategy to optimize transcription selection during inference. On the TAU Benchmark, Tai-LALM reaches 49.1% accuracy, marking a 6.5% absolute improvement over the zero-shot baseline (42.6% with ASR text conditioning). This confirms that integrating regional corpora with rigorous curation and dynamic arbitration significantly enhances LALM performance on localized speech.

</details>

---

### 37. [ARC-TGI: Human-Validated Task Generators with Reasoning Chain Templates for ARC-AGI](https://arxiv.org/abs/2603.05099)

**基本信息**

- 🔗 arXiv: [`2603.05099`](https://arxiv.org/abs/2603.05099)
- 👥 作者: Jens Lehmann, Syeda Khushbakht, Nikoo Salehfard 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05099.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个系统化的任务和数据生成框架，并发布了大量生成器代码。这为在化学信息学领域创建用于训练和评估“化学大模型”的复杂、可控的合成数据集或基准测试任务提供了强大的工具和范式参考。

**📖 中文摘要**

本文介绍了ARC-TGI（ARC任务生成器清单），一个用于任务族生成器的开源框架。这些生成器是紧凑的Python程序，可以在保留潜在规则的同时采样多样化的ARC-AGI任务。每个生成的任务都配有自然语言输入和转换推理链，以及部分实现的用于采样、转换和情节构建的Python代码。所有生成器都经过人工细化和本地验证。作者发布了461个生成器，覆盖了180个ARC-Mini任务、215个ARC-AGI-1任务和66个ARC-AGI-2任务，实现了可扩展的数据集采样和受控的基准测试。这项工作为抽象推理任务创建了系统化的数据生成工具和基准。其思想可迁移至化学信息学，用于生成用于训练和评估“化学大模型”在分子性质预测、逆合成规划等任务上的合成数据或基准测试。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Abstraction and Reasoning Corpus (ARC-AGI) probes few-shot abstraction and rule induction on small visual grids, but progress is difficult to measure on static collections of hand-authored puzzles due to overfitting, dataset leakage, and memorisation. We introduce ARC-TGI (ARC Task Generators Inventory), an open-source framework for task-family generators: compact Python programs that sample diverse ARC-AGI tasks while preserving a latent rule. ARC-TGI is built around a solver-facing representation: each generated task is paired with natural-language input and transformation reasoning chains and partially evaluated Python code implementing sampling, transformation, and episode construction. Crucially, ARC-TGI supports task-level constraints so that training examples collectively expose the variations needed to infer the underlying rule, a requirement for human-solvable ARC tasks that independent per-example sampling often fails to guarantee. All generators undergo human refinement and local verification to keep both grids and reasoning traces natural and consistent under variation. We release 461 generators covering 180 ARC-Mini tasks, 215 ARC-AGI-1 tasks (200 train, 15 test), and 66 ARC-AGI-2 tasks (55 train, 11 test), enabling scalable dataset sampling and controlled benchmarking.

</details>

---

### 38. [SRasP: Self-Reorientation Adversarial Style Perturbation for Cross-Domain Few-Shot Learning](https://arxiv.org/abs/2603.05135)

**基本信息**

- 🔗 arXiv: [`2603.05135`](https://arxiv.org/abs/2603.05135)
- 👥 作者: Wenqian Li, Pengfei Fang, Hui Xue
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05135.pdf)

**💡 相关性分析**

满足标准2：论文提出的自重新定向对抗风格扰动（SRasP）网络是一种数据增强和特征扰动方法，可作为工具用于提升模型在分布外数据上的泛化能力。这对于构建需要处理不同仪器、实验条件质谱数据的化学大模型或质谱结构推理模型具有参考价值，提供了相关的技术资源。

**📖 中文摘要**

本文提出了一种新颖的裁剪-全局风格扰动网络（SRasP），用于跨域少样本学习（CD-FSL）。虽然其核心应用是图像分类，但论文中提出的“风格扰动”方法本质上是一种数据增强技术，旨在通过操纵输入数据的表示（风格）来提升模型的泛化能力和鲁棒性。这种方法论与化学信息学和质谱分析中一个关键挑战高度相关：如何从具有显著域偏移（例如，不同仪器、不同样品基质）的少量质谱数据中学习并推断分子结构。SRasP框架通过生成对抗性风格扰动来扩大训练数据的多样性，这为构建更鲁棒的“化学大模型”或“质谱结构推理”模型提供了潜在的数据增强策略和工具。因此，这篇论文提供了可用于相关主题的数据增强方法和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cross-Domain Few-Shot Learning (CD-FSL) aims to transfer knowledge from a seen source domain to unseen target domains, serving as a key benchmark for evaluating the robustness and transferability of models. Existing style-based perturbation methods mitigate domain shift but often suffer from gradient instability and convergence to sharp this http URL address these limitations, we propose a novel crop-global style perturbation network, termed Self-Reorientation Adversarial \underline{S}tyle \underline{P}erturbation (SRasP). Specifically, SRasP leverages global semantic guidance to identify incoherent crops, followed by reorienting and aggregating the style gradients of these crops with the global style gradients within one image. Furthermore, we propose a novel multi-objective optimization function to maximize visual discrepancy while enforcing semantic consistency among global, crop, and adversarial features. Applying the stabilized perturbations during training encourages convergence toward flatter and more transferable solutions, improving generalization to unseen domains. Extensive experiments are conducted on multiple CD-FSL benchmarks, demonstrating consistent improvements over state-of-the-art methods.

</details>

---

### 39. [Recurrent Graph Neural Networks and Arithmetic Circuits](https://arxiv.org/abs/2603.05140)

**基本信息**

- 🔗 arXiv: [`2603.05140`](https://arxiv.org/abs/2603.05140)
- 👥 作者: Timon Barlag, Vivian Holzapfel, Laura Strieker 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05140.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是循环图神经网络（GNNs）的表达能力理论。GNNs是构建化学大模型（用于分子表示学习）和进行质谱结构推理（将质谱与分子图关联）的关键技术之一。该研究为这些主题提供了重要的模型理论基础。

**📖 中文摘要**

本文从计算理论的角度，刻画了循环图神经网络（Recurrent GNNs）的计算能力，将其与实数上的算术电路模型建立了精确的对应关系。论文的核心贡献在于理论分析，证明了循环GNNs和循环算术电路在表达能力上是等价的。这一理论发现对于“化学大模型”和“质谱结构推理”具有重要意义。在化学信息学中，分子通常被表示为图（原子为节点，化学键为边），图神经网络是处理此类数据的核心技术。本文对循环GNNs表达能力的严格刻画，为设计更强大、理论上更可解释的分子表示学习模型（化学大模型的核心组件）提供了理论基础。同时，质谱数据与分子结构图之间的推理也可以建模为图上的学习问题。因此，该论文为核心主题提供了重要的理论基础和模型设计见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We characterise the computational power of recurrent graph neural networks (GNNs) in terms of arithmetic circuits over the real numbers. Our networks are not restricted to aggregate-combine GNNs or other particular types. Generalizing similar notions from the literature, we introduce the model of recurrent arithmetic circuits, which can be seen as arithmetic analogues of sequential or logical circuits. These circuits utilise so-called memory gates which are used to store data between iterations of the recurrent circuit. While (recurrent) GNNs work on labelled graphs, we construct arithmetic circuits that obtain encoded labelled graphs as real valued tuples and then compute the same function. For the other direction we construct recurrent GNNs which are able to simulate the computations of recurrent circuits. These GNNs are given the circuit-input as initial feature vectors and then, after the GNN-computation, have the circuit-output among the feature vectors of its nodes. In this way we establish an exact correspondence between the expressivity of recurrent GNNs and recurrent arithmetic circuits operating over real numbers.

</details>

---

### 40. [Feature Resemblance: On the Theoretical Understanding of Analogical Reasoning in Transformers](https://arxiv.org/abs/2603.05143)

**基本信息**

- 🔗 arXiv: [`2603.05143`](https://arxiv.org/abs/2603.05143)
- 👥 作者: Ruichen Xu, Wenjing Yan, Ying-Jun Angela Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05143.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是Transformer模型中的类比推理机制。类比推理是高级认知功能，对于构建能够进行知识迁移和逻辑推断的“化学大模型”至关重要，该研究为核心主题提供了重要的模型内在机制理解。

**📖 中文摘要**

本文从理论角度深入研究了Transformer模型中的类比推理能力。作者通过理论证明和实验，揭示了Transformer如何通过表征对齐来实现属性迁移，从而完成类比推理。这项研究直接关联到“化学大模型”的核心能力之一：推理。化学大模型不仅需要记忆海量的化学知识，更需要具备类比和推理能力，例如，根据已知的分子反应规律推断未知反应，或根据质谱碎片模式类比推断相似结构。论文揭示的“通过相似属性将实体编码到相似表征中”的机制，正是化学知识表示和迁移学习的关键。因此，该工作为理解和设计具备更强推理能力的化学大模型提供了重要的理论视角和机制解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding reasoning in large language models is complicated by evaluations that conflate multiple reasoning types. We isolate analogical reasoning (inferring shared properties between entities based on known similarities) and analyze its emergence in transformers. We theoretically prove three key results: (1) Joint training on similarity and attribution premises enables analogical reasoning through aligned representations; (2) Sequential training succeeds only when similarity structure is learned before specific attributes, revealing a necessary curriculum; (3) Two-hop reasoning ($a \to b, b \to c \implies a \to c$) reduces to analogical reasoning with identity bridges ($b = b$), which must appear explicitly in training data. These results reveal a unified mechanism: transformers encode entities with similar properties into similar representations, enabling property transfer through feature alignment. Experiments with architectures up to 1.5B parameters validate our theory and demonstrate how representational geometry shapes inductive reasoning capabilities.

</details>

---

### 41. [Act, Think or Abstain: Complexity-Aware Adaptive Inference for Vision-Language-Action Models](https://arxiv.org/abs/2603.05147)

**基本信息**

- 🔗 arXiv: [`2603.05147`](https://arxiv.org/abs/2603.05147)
- 👥 作者: Riccardo Andrea Izzo, Gianluca Bardaro, Matteo Matteucci
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05147.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种自适应推理框架，其核心思想（根据任务复杂度动态调整模型行为）对于构建高效、鲁棒的“化学大模型”具有直接的启发性。化学大模型需要处理从简单查询到复杂规划的不同任务，此类架构设计至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current research on Vision-Language-Action (VLA) models predominantly focuses on enhancing generalization through established reasoning techniques. While effective, these improvements invariably increase computational complexity and inference latency. Furthermore, these mechanisms are typically applied indiscriminately, resulting in the inefficient allocation of resources for trivial tasks while simultaneously failing to provide the uncertainty estimation necessary to prevent catastrophic failure on out-of-distribution tasks. Inspired by human cognition, we propose an adaptive framework that dynamically routes VLA execution based on the complexity of the perceived state. Our approach transforms the VLA's vision-language backbone into an active detection tool by projecting latent embeddings into an ensemble of parametric and non-parametric estimators. This allows the system to execute known tasks immediately (Act), reason about ambiguous scenarios (Think), and preemptively halt execution when encountering significant physical or semantic anomalies (Abstain). In our empirical analysis, we observe a phenomenon where visual embeddings alone are superior for inferring task complexity due to the semantic invariance of language. Evaluated on the LIBERO and LIBERO-PRO benchmarks as well as on a real robot, our vision-only configuration achieves 80% F1-Score using as little as 5% of training data, establishing itself as a reliable and efficient task complexity detector.

</details>

---

### 42. [Federated Causal Discovery Across Heterogeneous Datasets under Latent Confounding](https://arxiv.org/abs/2603.05149)

**基本信息**

- 🔗 arXiv: [`2603.05149`](https://arxiv.org/abs/2603.05149)
- 👥 作者: Maximilian Hahn, Alina Zajak, Dominik Heider 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05149.pdf)

**💡 相关性分析**

满足标准2：论文提出了用于联邦因果发现的工具（fedCI Python包）和算法框架。这为化学信息学领域在隐私保护前提下，利用分散的质谱和分子数据协作训练大模型或进行结构推理提供了重要的数据融合与处理工具资源。

**📖 中文摘要**

本文提出了fedCI和fedCI-IOD，一种用于在异构数据集上进行联邦条件独立性测试和因果发现的方法。在化学信息学和质谱分析领域，数据往往分散在不同机构（如不同实验室、制药公司），且涉及隐私和安全问题，无法集中。同时，从多源质谱数据中联合推断分子结构-性质关系或反应路径本质上是一个因果发现问题。该论文提供的联邦学习工具（fedCI Python包）和算法，为在保护数据隐私的前提下，利用分布式化学/质谱数据集构建大模型或进行联合因果推理提供了可行的技术方案和资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Causal discovery across multiple datasets is often constrained by data privacy regulations and cross-site heterogeneity, limiting the use of conventional methods that require a single, centralized dataset. To address these challenges, we introduce fedCI, a federated conditional independence test that rigorously handles heterogeneous datasets with non-identical sets of variables, site-specific effects, and mixed variable types, including continuous, ordinal, binary, and categorical variables. At its core, fedCI uses a federated Iteratively Reweighted Least Squares (IRLS) procedure to estimate the parameters of generalized linear models underlying likelihood-ratio tests for conditional independence. Building on this, we develop fedCI-IOD, a federated extension of the Integration of Overlapping Datasets (IOD) algorithm, that replaces its meta-analysis strategy and enables, for the fist time, federated causal discovery under latent confounding across distributed and heterogeneous datasets. By aggregating evidence federatively, fedCI-IOD not only preserves privacy but also substantially enhances statistical power, achieving performance comparable to fully pooled analyses and mitigating artifacts from low local sample sizes. Our tools are publicly available as the fedCI Python package, a privacy-preserving R implementation of IOD, and a web application for the fedCI-IOD pipeline, providing versatile, user-friendly solutions for federated conditional independence testing and causal discovery.

</details>

---

### 43. [SWARM-SLR AIssistant: A Unified Framework for Scalable Systematic Literature Review Automation](https://arxiv.org/abs/2603.05177)

**基本信息**

- 🔗 arXiv: [`2603.05177`](https://arxiv.org/abs/2603.05177)
- 👥 作者: Tim Wittenborg, Allard Oelen, Manuel Prinz
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05177.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于自动化系统文献综述（SLR）的框架和工具。这对于高效收集、整理与“化学大模型”和“质谱结构推理”相关的研究文献、数据集和工具资源至关重要，提供了重要的研究支撑工具。

**📖 中文摘要**

本文介绍了SWARM-SLR AIssistant，一个用于自动化系统文献综述（SLR）的统一框架。它集成了基于LLM的智能助手和模块化研究工具。虽然论文本身不直接研究化学大模型或质谱，但它为解决一个关键的前置问题提供了工具：如何高效、可扩展地收集、管理和综述海量的相关科学文献。在快速发展的化学信息学和质谱分析领域，追踪关于“化学大模型”和“质谱结构推理”的最新研究是一项繁重但必要的工作。该框架提供的自动化、智能化的文献综述工具，能够显著加速相关领域的研究进程，是支撑核心主题研究的重要数据与资源管理工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite a growing ecosystem of tools supporting Systematic Literature Reviews (SLRs), integrating them into user-friendly workflows remains challenging. The Streamlined Workflow for Automating Machine-Actionable Systematic Literature Reviews (SWARM-SLR) unified the tool annotation and provided a cohesive yet modular workflow, but faced scalability and usability issues. We introduce the SWARM-SLR AIssistant, a unified framework that combines the SWARM-SLR's structured methodology with an agent-based assistant that integrates research tools in a modular interface. The first SWARM-SLR stage is integrated, enabling conversational, LLM-guided support and persistent data storage. To address the tool assessment bottleneck, we propose a centralized tool registry that allows developers to annotate and register tools autonomously using a shared metadata schema. Preliminary evaluation shows improved usability, but challenges remain in balancing efficiency, accessibility, and transparency. Further development is needed to realize scalable SLR automation.

</details>

---

### 44. [Mario: Multimodal Graph Reasoning with Large Language Models](https://arxiv.org/abs/2603.05181)

**基本信息**

- 🔗 arXiv: [`2603.05181`](https://arxiv.org/abs/2603.05181)
- 👥 作者: Yuanfu Sun, Kang Li, Pengkang Guo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05181.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是多模态图上的大语言模型推理框架。这直接对应于“化学大模型”的一个重要方向：如何让大模型理解和推理融合了分子图、谱图、文本等多模态信息的化学知识。该研究提供了前沿的模型架构思路。

**📖 中文摘要**

本文提出了Mario框架，一个用于在多模态图（MMG）上进行大语言模型（LLM）推理的统一框架。多模态图中的节点具有文本和视觉属性，边提供结构信息。这一设定与化学信息学高度契合：分子可以视为图（结构模态），同时关联着文本描述（文献、属性）、图像（分子式、光谱图）等多模态信息。质谱结构推理也可以看作是从质谱数据（一种模态）到分子图（另一种模态）的跨模态推理问题。Mario框架旨在解决跨模态一致性和异质模态偏好两大挑战，其提出的图条件化视觉语言模型设计和模态自适应图指令调优机制，为构建能够深度融合化学结构、谱图数据、文本知识的“化学多模态大模型”提供了创新的方法论和架构蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have opened new avenues for multimodal reasoning. Yet, most existing methods still rely on pretrained vision-language models (VLMs) to encode image-text pairs in isolation, ignoring the relational structure that real-world multimodal data naturally form. This motivates reasoning on multimodal graphs (MMGs), where each node has textual and visual attributes and edges provide structural cues. Enabling LLM-based reasoning on such heterogeneous multimodal signals while preserving graph topology introduces two key challenges: resolving weak cross-modal consistency and handling heterogeneous modality preference. To address this, we propose Mario, a unified framework that simultaneously resolves the two above challenges and enables effective LLM-based reasoning over MMGs. Mario consists of two innovative stages. Firstly, a graph-conditioned VLM design that jointly refines textual and visual features through fine-grained cross-modal contrastive learning guided by graph topology. Secondly, a modality-adaptive graph instruction tuning mechanism that organizes aligned multimodal features into graph-aware instruction views and employs a learnable router to surface, for each node and its neighborhood, the most informative modality configuration to the LLM. Extensive experiments across diverse MMG benchmarks demonstrate that Mario consistently outperforms state-of-the-art graph models in both supervised and zero-shot scenarios for node classification and link prediction. The code will be made available at this https URL .

</details>

---

### 45. [Transducing Language Models](https://arxiv.org/abs/2603.05193)

**基本信息**

- 🔗 arXiv: [`2603.05193`](https://arxiv.org/abs/2603.05193)
- 👥 作者: Vésteinn Snæbjarnarson, Samuel Kiegeland, Tianyu Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05193.pdf)

**💡 相关性分析**

满足标准1和2：论文提出了一个通过有限状态转录机（FST）变换来派生和适配语言模型的通用框架。这为核心主题“化学大模型”提供了重要的模型适配方法（标准1），同时也是一种可用于处理化学领域特定字符串表示（如SMILES）的工具（标准2）。

**📖 中文摘要**

本文提出了一个通用框架，用于通过确定性的字符串到字符串变换（特别是有限状态转录机，FST）来派生新的语言模型。该框架允许将预训练语言模型的输出（如BPE字符串）转换为所需的形式（如单词、氨基酸序列），而无需改变模型参数。这对于“化学大模型”具有重要启示：化学领域有大量专用的字符串表示法，如SMILES、SELFIES、InChI等，它们都是分子图结构的线性编码。该研究提供的框架和算法，使得我们可以将一个在通用语料上预训练的大语言模型，通过编译一个化学领域特定的FST，高效地适配为专门生成或理解化学线性编码（如SMILES）的模型，或者在不同化学表示法之间进行转换。这为快速构建领域适配的化学大模型提供了新的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern language models define distributions over strings, but downstream tasks often require different output formats. For instance, a model that generates byte-pair strings does not directly produce word-level predictions, and a DNA model does not directly produce amino-acid sequences. In such cases, a deterministic string-to-string transformation can convert the model's output to the desired form. This is a familiar pattern in probability theory: applying a function $f$ to a random variable $X\sim p$ yields a transformed random variable $f(X)$ with an induced distribution. While such transformations are occasionally used in language modeling, prior work does not treat them as yielding new, fully functional language models. We formalize this perspective and introduce a general framework for language models derived from deterministic string-to-string transformations. We focus on transformations representable as finite-state transducers -- a commonly used state-machine abstraction for efficient string-to-string mappings. We develop algorithms that compose a language model with an FST to *marginalize* over source strings mapping to a given target, propagating probabilities through the transducer without altering model parameters and enabling *conditioning* on transformed outputs. We present an exact algorithm, an efficient approximation, and a theoretical analysis. We conduct experiments in three domains: converting language models from tokens to bytes, from tokens to words, and from DNA to amino acids. These experiments demonstrate inference-time adaptation of pretrained language models to match application-specific output requirements.

</details>

---

### 46. [Diffusion LLMs can think EoS-by-EoS](https://arxiv.org/abs/2603.05197)

**基本信息**

- 🔗 arXiv: [`2603.05197`](https://arxiv.org/abs/2603.05197)
- 👥 作者: Sarah Breckner, Sebastian Schuster
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05197.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是扩散大语言模型的推理机制，特别是其利用EoS令牌进行隐式计算的能力。这种新颖的推理范式对于构建能够进行复杂多步推理的“化学大模型”具有重要的架构启示意义。

**📖 中文摘要**

本文研究了扩散大语言模型（Diffusion LLMs）的推理机制，提出了“EoS-by-EoS”思考的假设，即模型利用序列结束（EoS）令牌的表示作为隐藏的草稿纸来进行复杂推理。通过受控提示实验和因果干预，论文证实了添加EoS令牌可以提升模型的推理能力，并且EoS令牌携带了解决问题的信息。这项研究对于“化学大模型”的架构设计具有启发意义。化学推理（如逆合成分析、反应预测）通常是多步骤、需要中间“思考”的过程。扩散模型或类似利用“隐空间草稿”的机制，可能为化学大模型提供一种新的、更强大的序列生成与推理范式，使其能够更好地处理需要多步逻辑推导的化学问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion LLMs have been proposed as an alternative to autoregressive LLMs, excelling especially at complex reasoning tasks with interdependent sub-goals. Curiously, this is particularly true if the generation length, i.e., the number of tokens the model has to output, is set to a much higher value than is required for providing the correct answer to the task, and the model pads its answer with end-of-sequence (EoS) tokens. We hypothesize that diffusion models think EoS-by-EoS, that is, they use the representations of EoS tokens as a hidden scratchpad, which allows them to solve harder reasoning problems. We experiment with the diffusion models LLaDA1.5, LLaDA2.0-mini, and Dream-v0 on the tasks Addition, Entity Tracking, and Sudoku. In a controlled prompting experiment, we confirm that adding EoS tokens improves the LLMs' reasoning capabilities. To further verify whether they serve as space for hidden computations, we patch the hidden states of the EoS tokens with those of a counterfactual generation, which frequently changes the generated output to the counterfactual. The success of the causal intervention underscores that the EoS tokens, which one may expect to be devoid of meaning, carry information on the problem to solve. The behavioral experiments and the causal interventions indicate that diffusion LLMs can indeed think EoS-by-EoS.

</details>

---

### 47. [Recursive Inference Machines for Neural Reasoning](https://arxiv.org/abs/2603.05234)

**基本信息**

- 🔗 arXiv: [`2603.05234`](https://arxiv.org/abs/2603.05234)
- 👥 作者: Mieszko Komisarczyk, Saurabh Mathur, Maurice Kraus 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05234.pdf)

**💡 相关性分析**

满足标准1：论文提出了递归推理机（RIMs）框架，旨在将显式推理机制注入神经模型以提升复杂推理能力。这直接关系到“化学大模型”和“质谱结构推理”所必需的高级逻辑与符号推理功能，为核心主题提供了创新的模型设计思路。

**📖 中文摘要**

本文介绍了递归推理机（RIMs），一个将经典推理引擎的递归推理机制显式地融入神经推理的框架。作者展示了现有的小递归模型（TRMs）可以作为RIMs的一个实例，并通过引入重新加权组件扩展了其能力，在包括ARC-AGI和数独等复杂推理基准上取得了更好的性能。这项研究直接针对“推理”这一核心能力。化学大模型和质谱结构推理的本质都是复杂的符号推理和模式识别问题。RIMs框架提供了一种将符号推理规则与神经骨干网络相结合的系统性方法，为设计下一代具备更强、更可解释推理能力的化学AI系统提供了有前景的蓝图和模型架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural reasoners such as Tiny Recursive Models (TRMs) solve complex problems by combining neural backbones with specialized inference schemes. Such inference schemes have been a central component of stochastic reasoning systems, where inference rules are applied to a stochastic model to derive answers to complex queries. In this work, we bridge these two paradigms by introducing Recursive Inference Machines (RIMs), a neural reasoning framework that explicitly incorporates recursive inference mechanisms inspired by classical inference engines. We show that TRMs can be expressed as an instance of RIMs, allowing us to extend them through a reweighting component, yielding better performance on challenging reasoning benchmarks, including ARC-AGI-1, ARC-AGI-2, and Sudoku Extreme. Furthermore, we show that RIMs can be used to improve reasoning on other tasks, such as the classification of tabular data, outperforming TabPFNs.

</details>

---

### 48. [Wiki-R1: Incentivizing Multimodal Reasoning for Knowledge-based VQA via Data and Sampling Curriculum](https://arxiv.org/abs/2603.05256)

**基本信息**

- 🔗 arXiv: [`2603.05256`](https://arxiv.org/abs/2603.05256)
- 👥 作者: Shan Ning, Longtian Qiu, Xuming He
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05256.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个通过课程强化学习来提升模型推理能力的训练框架（Wiki-R1）。这为训练能够进行复杂知识推理的“化学大模型”或“质谱结构推理”模型提供了重要的训练方法、策略和工具资源。

**📖 中文摘要**

本文提出了Wiki-R1，一个基于课程强化学习的数据生成框架，用于提升多模态大语言模型（MLLMs）在基于知识的视觉问答（KB-VQA）任务中的推理能力。该框架通过可控课程数据生成和课程采样策略，构建与模型能力演进相匹配的训练数据分布。虽然应用场景是视觉问答，但其核心方法论——通过精心设计的数据课程和强化学习来“激励”模型进行复杂推理——完全适用于“化学大模型”和“质谱结构推理”。例如，可以构建从简单分子属性预测到复杂谱图解析的课程，训练模型逐步掌握化学知识推理。该论文为训练具备深度推理能力的化学多模态模型提供了重要的训练框架和方法论资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge-Based Visual Question Answering (KB-VQA) requires models to answer questions about an image by integrating external knowledge, posing significant challenges due to noisy retrieval and the structured, encyclopedic nature of the knowledge base. These characteristics create a distributional gap from pretrained multimodal large language models (MLLMs), making effective reasoning and domain adaptation difficult in the post-training stage. In this work, we propose \textit{Wiki-R1}, a data-generation-based curriculum reinforcement learning framework that systematically incentivizes reasoning in MLLMs for KB-VQA. Wiki-R1 constructs a sequence of training distributions aligned with the model's evolving capability, bridging the gap from pretraining to the KB-VQA target distribution. We introduce \textit{controllable curriculum data generation}, which manipulates the retriever to produce samples at desired difficulty levels, and a \textit{curriculum sampling strategy} that selects informative samples likely to yield non-zero advantages during RL updates. Sample difficulty is estimated using observed rewards and propagated to unobserved samples to guide learning. Experiments on two KB-VQA benchmarks, Encyclopedic VQA and InfoSeek, demonstrate that Wiki-R1 achieves new state-of-the-art results, improving accuracy from 35.5\% to 37.1\% on Encyclopedic VQA and from 40.1\% to 44.1\% on InfoSeek. The project page is available at this https URL .

</details>

---

### 49. [X-RAY: Mapping LLM Reasoning Capability via Formalized and Calibrated Probes](https://arxiv.org/abs/2603.05290)

**基本信息**

- 🔗 arXiv: [`2603.05290`](https://arxiv.org/abs/2603.05290)
- 👥 作者: Gao Tianxi, Cai Yufan, Yuan Yusi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05290.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于系统评估大语言模型推理能力的框架（X-RAY）和基准测试方法。这为评估“化学大模型”的化学推理能力提供了重要的分析工具和评估资源。

**📖 中文摘要**

本文提出了X-RAY，一个可解释的推理分析系统，通过经过校准和形式化验证的探针来绘制大语言模型（LLMs）的推理能力图谱。该工作将推理能力建模为可提取的“结构”函数，并通过形式化工具生成具有受控结构变化的探针。X-RAY能够揭示LLM推理中的系统性不对称性（如对约束细化鲁棒但对解空间重构敏感），并区分在标准基准上表现相似的模型。这项研究对于评估和构建“化学大模型”至关重要。化学推理高度依赖于结构和约束（如化学键、官能团、反应规则）。X-RAY提供了一套形式化、可解释的基准测试框架，可以用于诊断化学大模型在各类化学推理任务（如合成规划、分子设计）上的真实能力边界和失败模式，从而指导更好的模型设计与训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) achieve promising performance, yet their ability to reason remains poorly understood. Existing evaluations largely emphasize task-level accuracy, often conflating pattern matching with reasoning capability. We present X-RAY, an explainable reasoning analysis system that maps the LLM reasoning capability using calibrated, formally verified probes. We model reasoning capability as a function of extractable \textit{structure}, operationalized through formal properties such as constraint interaction, reasoning depth, and solution-space geometry. X-Ray generates probes via formal tools with controlled structural variations, enabling precise isolation of incremental structural information through formal calibration and verification. We evaluate state-of-the-art LLMs on problems ranging from junior-level to advanced in mathematics, physics, and chemistry. Our analysis reveals a systematic asymmetry in LLM reasoning: models are relatively robust to constraint refinement, where additional conditions shrink an existing solution space, but degrade sharply under solution-space restructuring, where modifications alter the underlying structural form of the solution manifold. Moreover, calibrated formal probes differentiate models that appear indistinguishable on standard benchmarks and reveal failure modes that are structurally interpretable rather than opaque. Beyond evaluation, our framework is contamination-free and supports the training and testing of reasoning models.

</details>

---

### 50. [Knowledge Divergence and the Value of Debate for Scalable Oversight](https://arxiv.org/abs/2603.05293)

**基本信息**

- 🔗 arXiv: [`2603.05293`](https://arxiv.org/abs/2603.05293)
- 👥 作者: Robin Young
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05293.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对AI辩论机制的形式化理论分析，探讨了知识差异如何影响辩论效果。这对于未来构建需要可靠监督和评估的、强大的“化学大模型”系统，提供了关于可扩展监督方法的理论见解。

**📖 中文摘要**

本文通过参数化辩论模型之间的知识差异几何，为AI安全中的辩论方法和从AI反馈中强化学习（RLAIF）建立了正式的联系框架。作者证明了辩论的优势存在一个精确的闭式解，并分析了知识差异的不同机制（共享、单边、组合）以及辩论在何种情况下是必要的。这项理论研究对于“化学大模型”的可扩展监督（Scalable Oversight）具有潜在意义。当化学大模型变得非常强大时，如何确保其输出（如新分子设计、合成路线）的安全性和可靠性成为一个挑战。辩论作为一种对抗性监督协议，可能被用来让多个化学专家模型相互辩论，以产生更可靠、更少偏见的结果。该论文为理解辩论机制何时有效提供了理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI safety via debate and reinforcement learning from AI feedback (RLAIF) are both proposed methods for scalable oversight of advanced AI systems, yet no formal framework relates them or characterizes when debate offers an advantage. We analyze this by parameterizing debate's value through the geometry of knowledge divergence between debating models. Using principal angles between models' representation subspaces, we prove that the debate advantage admits an exact closed form. When models share identical training corpora, debate reduces to RLAIF-like where a single-agent method recovers the same optimum. When models possess divergent knowledge, debate advantage scales with a phase transition from quadratic regime (debate offers negligible benefit) to linear regime (debate is essential). We classify three regimes of knowledge divergence (shared, one-sided, and compositional) and provide existence results showing that debate can achieve outcomes inaccessible to either model alone, alongside a negative result showing that sufficiently strong adversarial incentives cause coordination failure in the compositional regime, with a sharp threshold separating effective from ineffective debate. We offer the first formal connection between debate and RLAIF, a geometric foundation for understanding when adversarial oversight protocols are justified, and connection to the problem of eliciting latent knowledge across models with complementary information.

</details>

---

### 51. [WavSLM: Single-Stream Speech Language Modeling via WavLM Distillation](https://arxiv.org/abs/2603.05299)

**基本信息**

- 🔗 arXiv: [`2603.05299`](https://arxiv.org/abs/2603.05299)
- 👥 作者: Luca Della Libera, Cem Subakan, Mirco Ravanelli
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05299.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种直接从原始语音信号进行单流语言建模的架构（WavSLM）。这为“质谱结构推理”提供了一个新颖的模型范式参考：即不依赖手工特征或中间表示，直接对原始质谱信号序列进行建模和推理，属于核心主题的模型架构探索。

**📖 中文摘要**

本文提出了WavSLM，一种通过量化并蒸馏自监督WavLM表征来训练的单流语音语言模型。它在一个单一的令牌流中联合建模语义和声学信息，无需文本监督。这项研究在架构上对“化学大模型”有启发意义。质谱数据（尤其是串联质谱MS/MS）与语音信号有相似之处，都是连续、高维、蕴含层次化信息的序列。WavSLM展示了如何不依赖中间文本表示，直接从原始信号（语音波形）构建一个生成式语言模型。这启发了另一种构建“质谱结构推理”模型的思路：是否可以构建一个“质谱语言模型”，直接从原始或预处理后的质谱信号序列中学习，并用于生成分子结构描述（如SMILES）或预测属性？该论文为处理连续科学信号提供了有参考价值的模型范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models show that simple autoregressive training can yield scalable and coherent generation, but extending this paradigm to speech remains challenging due to the entanglement of semantic and acoustic information. Most existing speech language models rely on text supervision, hierarchical token streams, or complex hybrid architectures, departing from the single-stream generative pretraining paradigm that has proven effective in text. In this work, we introduce WavSLM, a speech language model trained by quantizing and distilling self-supervised WavLM representations into a single codebook and optimizing an autoregressive next-chunk prediction objective. WavSLM jointly models semantic and acoustic information within a single token stream without text supervision or text pretraining. Despite its simplicity, it achieves competitive performance on consistency benchmarks and speech generation while using fewer parameters, less training data, and supporting streaming inference. Demo samples are available at this https URL .

</details>

---

### 52. [Med-V1: Small Language Models for Zero-shot and Scalable Biomedical Evidence Attribution](https://arxiv.org/abs/2603.05308)

**基本信息**

- 🔗 arXiv: [`2603.05308`](https://arxiv.org/abs/2603.05308)
- 👥 作者: Qiao Jin, Yin Fang, Lauren He 等15人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05308.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于证据归因的小型专家模型（Med-V1）及其训练方法。这为“化学大模型”提供了一个重要的辅助工具资源，可用于增强化学大模型输出的可信度和可验证性，减少幻觉。

**📖 中文摘要**

本文提出了Med-V1，一个仅30亿参数的小型语言模型家族，专门用于生物医学证据归因（即判断文献是否支持某个断言）。该模型在高质量合成数据上训练，在多个生物医学验证基准上性能媲美前沿大模型（如GPT-5），且能提供高质量解释。这项工作虽然聚焦生物医学文本，但其方法论和模型对于“化学大模型”在可信性和可解释性方面有直接应用价值。化学研究同样需要证据支持（如某个反应是否可行，某个分子是否具有某种毒性）。Med-V1展示了如何构建一个轻量级、高精度的领域专用验证模型。这种模型可以作为化学大模型的一个可靠“验证器”或“事实核查”模块集成到系统中，用于检测大模型在化学知识回答中可能产生的幻觉，提升整个系统的可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Assessing whether an article supports an assertion is essential for hallucination detection and claim verification. While large language models (LLMs) have the potential to automate this task, achieving strong performance requires frontier models such as GPT-5 that are prohibitively expensive to deploy at scale. To efficiently perform biomedical evidence attribution, we present Med-V1, a family of small language models with only three billion parameters. Trained on high-quality synthetic data newly developed in this study, Med-V1 substantially outperforms (+27.0% to +71.3%) its base models on five biomedical benchmarks unified into a verification format. Despite its smaller size, Med-V1 performs comparably to frontier LLMs such as GPT-5, along with high-quality explanations for its predictions. We use Med-V1 to conduct a first-of-its-kind use case study that quantifies hallucinations in LLM-generated answers under different citation instructions. Results show that the format instruction strongly affects citation validity and hallucination, with GPT-5 generating more claims but exhibiting hallucination rates similar to GPT-4o. Additionally, we present a second use case showing that Med-V1 can automatically identify high-stakes evidence misattributions in clinical practice guidelines, revealing potentially negative public health impacts that are otherwise challenging to identify at scale. Overall, Med-V1 provides an efficient and accurate lightweight alternative to frontier LLMs for practical and real-world applications in biomedical evidence attribution and verification tasks. Med-V1 is available at this https URL .

</details>

---

### 53. [Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs](https://arxiv.org/abs/2603.05343)

**基本信息**

- 🔗 arXiv: [`2603.05343`](https://arxiv.org/abs/2603.05343)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于等变图神经网络（一种用于分子模拟的化学大模型）的压缩和加速框架，直接围绕化学大模型的主题。

**📖 中文摘要**

本文提出了一种几何感知量化（GAQ）框架，用于压缩和加速等变图神经网络（GNNs），同时严格保持离散空间中的连续对称性。该框架通过解耦不变长度和等变方向来保持几何保真度，并采用对称感知训练策略。实验在rMD17基准上进行，该基准是用于分子模拟的著名数据集。这项工作直接针对分子模拟的化学大模型（等变GNNs）的效率和部署挑战，属于核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

</details>

---

### 54. [On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395)

**基本信息**

- 🔗 arXiv: [`2603.05395`](https://arxiv.org/abs/2603.05395)
- 👥 作者: Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05395.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和比较层神经网络（SNNs）与基线模型，SNNs是图神经网络（GNNs）的变体，而GNNs是构建化学信息学中化学大模型（用于分子图表示）的基础架构。

**📖 中文摘要**

本文研究了层神经网络（SNNs），这是图卷积网络（GNNs）的扩展，旨在通过将层附加到输入图上来解决异配图上的过平滑问题。论文引入了恒等层网络基线，并在五个流行的异配基准上进行了评估。虽然论文本身不直接构建化学大模型，但它深入分析和比较了图神经网络（GNNs）的变体，而GNNs是构建化学大模型（用于分子表示和性质预测）的核心架构之一。因此，该论文提供了对化学大模型基础架构的重要见解和评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

</details>

---

### 55. [An interpretable prototype parts-based neural network for medical tabular data](https://arxiv.org/abs/2603.05423)

**基本信息**

- 🔗 arXiv: [`2603.05423`](https://arxiv.org/abs/2603.05423)
- 👥 作者: Jacek Karolczak, Jerzy Stefanowski
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05423.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于结构化数据的可解释深度学习模型。开发可解释的机器学习模型是化学信息学和化学大模型中的一个重要研究方向，旨在使模型决策对化学家更透明。

**📖 中文摘要**

本文提出了一种新的、可解释的、基于原型部件的神经网络模型，专门用于医疗表格数据。该模型通过学习可解释的、基于特征的子集（原型）来进行预测，使决策过程与临床语言和基于案例的推理保持一致。虽然应用领域是医疗，但该模型的核心创新在于为结构化数据设计了一种可解释的、基于原型的深度学习架构。这种专注于为结构化数据（可能包括化学分子描述符或质谱特征）开发可解释机器学习模型的研究，与构建更透明、可解释的化学信息学模型（化学大模型的一个方面）的努力相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainable patching over features describing a patient, to learn meaningful prototypical parts from structured data. These parts are represented as binary or discretized feature subsets. This allows the model to express prototypes in human-readable terms, enabling alignment with clinical language and case-based reasoning. Our proposed neural network is inherently interpretable and offers interpretable concept-based predictions by comparing the patient's description to learned prototypes in the latent space of the network. In experiments, we demonstrate that the model achieves classification performance competitive to widely used baseline models on medical benchmark datasets, while also offering transparency, bridging the gap between predictive performance and interpretability in clinical decision support.

</details>

---

### 56. [CogGen: Cognitive-Load-Informed Fully Unsupervised Deep Generative Modeling for Compressively Sampled MRI Reconstruction](https://arxiv.org/abs/2603.04438)

**基本信息**

- 🔗 arXiv: [`2603.04438`](https://arxiv.org/abs/2603.04438)
- 👥 作者: Qingyong Zhu, Yumin Tan, Xiang Gu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04438.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的全无监督深度生成建模框架（CogGen），用于解决逆问题。深度生成模型是化学信息学中用于分子生成和质谱解析等任务的关键技术，因此该方法论研究具有相关性。

**📖 中文摘要**

本文提出了CogGen，一种认知负荷感知的全无监督深度生成模型，用于压缩采样MRI重建。该框架将CS-MRI视为分阶段反演，并通过渐进式调度内在难度和外部干扰来调节任务侧“认知负荷”。虽然应用领域是医学成像，但该方法论的核心是开发一种新颖的、无监督的深度生成建模框架，用于解决不适定逆问题。这种在生成模型和优化方法上的创新，与开发用于化学数据（如从质谱推断结构）的生成模型和推理方法在方法论上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fully unsupervised deep generative modeling (FU-DGM) is promising for compressively sampled MRI (CS-MRI) when training data or compute are limited. Classical FU-DGMs such as DIP and INR rely on architectural priors, but the ill-conditioned inverse problem often demands many iterations and easily overfits measurement noise. We propose CogGen, a cognitive-load-informed FU-DGM that casts CS-MRI as staged inversion and regulates task-side "cognitive load" by progressively scheduling intrinsic difficulty and extraneous interference. CogGen replaces uniform data fitting with an easy-to-hard k-space weighting/selection strategy: early iterations emphasize low-frequency, high-SNR, structure-dominant samples, while higher-frequency or noise-dominated measurements are introduced later. We realize this schedule via self-paced curriculum learning with complementary student-mode (what the model can currently learn) and teacher-mode (what it should follow) criteria, supporting both soft weighting and hard selection. Experiments and analysis show that CogGen-DIP and CogGen-INR improve fidelity and convergence over strong unsupervised baselines and competitive supervised pipelines.

</details>

---

### 57. [A systematic approach to answering the easy problems of consciousness based on an executable cognitive system](https://arxiv.org/abs/2603.04440)

**基本信息**

- 🔗 arXiv: [`2603.04440`](https://arxiv.org/abs/2603.04440)
- 👥 作者: Qi Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04440.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是描述和论证一个用于解决认知“简单问题”的可执行认知系统架构。构建能够进行复杂科学推理和理解的大模型是化学信息学和质谱分析中“化学大模型”的终极愿景之一，因此该研究在系统架构和认知机制层面具有相关性。

**📖 中文摘要**

本文基于一个可执行的认知系统及其实现的计算机制，首次尝试系统性地解决Chalmers提出的意识“简单问题”。该系统建立在康德提出的概念知识理解之上。虽然主题是认知科学和AI意识，但论文详细描述了一个基于知识表示、学习机制和目标导向操作的复杂可执行认知系统架构。构建能够进行复杂推理和知识操作的“大模型”系统（无论是针对语言、视觉还是科学数据）是当前AI的核心挑战。该论文对一个综合性认知系统的设计和论证，为构建能够处理复杂科学推理（如化学或质谱分析）的AI系统提供了高层次的架构见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Consciousness is the window of the brain and reflects many fundamental cognitive properties involving both computational and cognitive mechanisms. A collection of these properties was described as the "easy problems" by Chalmers, including the ability to discriminate, categorize, and react to stimuli; information integration; reportability; information access; attention; deliberate control; and the difference between wakefulness and sleep. These "easy problems" have not been systematically addressed. This study presents a first attempt to address them systematically based on an executable cognitive system and its implemented computational mechanisms, built upon an understanding of conceptual knowledge proposed by Kant. The study suggests that the abilities to discriminate, categorize, react, report, and integrate information can all be derived from the system's learning mechanism; attention and deliberate control are goal-oriented and can be attributed to emotional states and its information-manipulation mechanism; and the difference between wakefulness and dream sleep lies mainly in the source of stimuli. The connections between the implemented mechanisms in the executive system and conclusions drawn from empirical findings are also discussed, and many of these discussions and conclusions are supported by demonstrations of the executive system.

</details>

---

### 58. [AbAffinity: A Large Language Model for Predicting Antibody Binding Affinity against SARS-CoV-2](https://arxiv.org/abs/2603.04480)

**基本信息**

- 🔗 arXiv: [`2603.04480`](https://arxiv.org/abs/2603.04480)
- 👥 作者: Faisal Bin Ashraf, Animesh Ray, Stefano Lonardi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04480.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个名为AbAffinity的大型语言模型，用于预测抗体-抗原结合亲和力。这直接属于将大模型（LLMs）应用于化学和生物学分子性质预测的主题，是化学信息学中“化学大模型”的一个具体应用实例。

**📖 中文摘要**

本文介绍了AbAffinity，一种新的大型语言模型，用于准确预测抗体与目标肽（如SARS-CoV-2刺突蛋白）的结合亲和力。该模型利用人工智能的显著进步和实验抗体数据（特别是与COVID-19相关的数据）的指数级增长。这项工作直接将大型语言模型应用于生物分子（抗体）性质（结合亲和力）的预测，是“化学大模型”（或更具体地说，“生物大模型”）在药物发现和蛋白质工程中的典型应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning-based antibody design is emerging as one of the most promising approaches to combat infectious diseases, due to significant advancements in the field of artificial intelligence and an exponential surge in experimental antibody data (in particular related to COVID-19). The ability of an antibody to bind to an antigens (called binding affinity) is one of the the most critical properties in designing neutralizing antibodies. In this study we introduce Ab-Affinity, a new large language model that can accurately predict the binding affinity of antibodies against a target peptide, e.g., the SARS-CoV-2 spike protein. Code and model are available at this https URL .

</details>

---

### 59. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2603.04523)

**基本信息**

- 🔗 arXiv: [`2603.04523`](https://arxiv.org/abs/2603.04523)
- 👥 作者: Austin Rodriguez, Justin S. Smith, Sakib Matin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04523.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的训练框架（PHL），用于改进机器学习原子间势（MLIPs）——这是化学和材料科学中用于模拟和预测的“化学大模型”的关键类型。

**📖 中文摘要**

本文介绍了投影Hessian学习（PHL），一个可扩展的二阶训练框架，用于机器学习原子间势（MLIPs）。该框架仅使用Hessian-向量积（HVPs）来注入曲率信息，避免了构建和存储完整Hessian矩阵的二次方成本和内存增长。PHL在ωB97XD/6-31G(d)水平计算的化学反应物、产物、过渡态等多样化化学数据集上进行了基准测试。这项工作直接针对化学和材料科学中机器学习势函数（一种重要的化学大模型）的训练效率和精度提升，属于核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hessian matrix (second derivatives) encodes far richer local curvature of the potential energy surface than energies and forces alone. However, training machine-learning interatomic potentials (MLIPs) with full Hessians is often impractical because explicitly forming and storing Hessian matrices scales quadratically in cost and memory. We introduce Projected Hessian Learning (PHL), a scalable second-order training framework that injects curvature information using only Hessian-vector products (HVPs). Rather than constructing the Hessian, PHL projects curvature along stochastic probe directions and uses an unbiased stochastic trace-based loss with favorable system-size scaling, enabling curvature-informed training without quadratic memory growth. We benchmark PHL on a chemically diverse dataset of reactants, products, transition states, intrinsic reaction coordinates, and normal-mode sampled geometries computed at omegaB97XD/6-31G(d). We compare energy-force training (E-F), two HVP-based schemes (E-F-HVP with one-hot or randomized probes), and full energy-force-Hessian training (E-F-H). With randomized probes per minibatch, both HVP schemes match full-Hessian training in energy, force, and Hessian accuracy while delivering >24x epoch speedups for the small molecular systems studied. In a fixed-probe regime with one HVP per molecule, randomized projections consistently outperform one-column probing, especially for far-from-equilibrium geometries. Overall, PHL replaces explicit Hessian supervision with force-complexity curvature training, retaining most second-order accuracy gains while scaling to larger, more complex molecular systems.

</details>

---

### 60. [The Volterra signature](https://arxiv.org/abs/2603.04525)

**基本信息**

- 🔗 arXiv: [`2603.04525`](https://arxiv.org/abs/2603.04525)
- 👥 作者: Paul P. Hager, Fabian N. Harang, Luca Pelizzari 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04525.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于非马尔可夫时间序列的通用、原则性特征表示框架（Volterra签名）。该框架具有处理序列数据的潜力，而质谱数据和分子轨迹都是序列数据的一种，因此与质谱结构推理和化学数据分析的方法论相关。

**📖 中文摘要**

本文提出了Volterra签名作为一种原则性的、显式的特征表示方法，用于处理具有历史依赖性的系统。通过将由时间核加权的输入路径展开到张量代数中，并利用相关的Volterra-Chen恒等式，论文推导出了严格的学习理论保证。该表示对时间重新参数化具有固有的不变性，并可通过线性状态空间ODE求解。Volterra签名为数据科学提供了一个强大、可计算的特征映射。虽然论文没有明确针对化学数据，但所提出的数学框架为处理序列数据（如时间序列、轨迹、光谱序列）提供了强大的工具。质谱数据可以视为一种序列（质荷比与强度），而分子动力学模拟轨迹也是序列数据。因此，该框架可能适用于质谱结构推理或分子模拟数据分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern approaches for learning from non-Markovian time series, such as recurrent neural networks, neural controlled differential equations or transformers, typically rely on implicit memory mechanisms that can be difficult to interpret or to train over long horizons. We propose the Volterra signature $\mathrm{VSig}(x;K)$ as a principled, explicit feature representation for history-dependent systems. By developing the input path $x$ weighted by a temporal kernel $K$ into the tensor algebra, we leverage the associated Volterra--Chen identity to derive rigorous learning-theoretic guarantees. Specifically, we prove an injectivity statement (identifiability under augmentation) that leads to a universal approximation theorem on the infinite dimensional path space, which in certain cases is achieved by linear functionals of $\mathrm{VSig}(x;K)$. Moreover, we demonstrate applicability of the kernel trick by showing that the inner product associated with Volterra signatures admits a closed characterization via a two-parameter integral equation, enabling numerical methods from PDEs for computation. For a large class of exponential-type kernels, $\mathrm{VSig}(x;K)$ solves a linear state-space ODE in the tensor algebra. Combined with inherent invariance to time reparameterization, these results position the Volterra signature as a robust, computationally tractable feature map for data science. We demonstrate its efficacy in dynamic learning tasks on real and synthetic data, where it consistently improves classical path signature baselines.

</details>

---

### 61. [A Fast Generative Framework for High-dimensional Posterior Sampling: Application to CMB Delensing](https://arxiv.org/abs/2603.04535)

**基本信息**

- 🔗 arXiv: [`2603.04535`](https://arxiv.org/abs/2603.04535)
- 👥 作者: Hadi Sotoudeh, Pablo Lemos, Laurence Perreault-Levasseur
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04535.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于高维贝叶斯推理的快速深度生成框架。从质谱数据推断分子结构本质上也是一个高维贝叶斯逆问题，因此该框架在方法论上具有相关性。

**📖 中文摘要**

本文介绍了一个用于高维贝叶斯推理的深度生成框架，能够实现高效的后验采样。该框架应用于CMB去透镜问题，成功从模拟观测中恢复了未透镜的CMB功率谱。虽然应用领域是天体物理学，但论文的核心贡献是一个快速的、基于深度生成的贝叶斯推理框架。在化学信息学和质谱分析中，从观测数据（如质谱）中推断潜在结构（如分子结构）也是一个贝叶斯逆问题。因此，这种高效的生成式后验采样方法在方法论上与质谱结构推理问题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a deep generative framework for high-dimensional Bayesian inference that enables efficient posterior sampling. As telescopes and simulations rapidly expand the volume and resolution of astrophysical data, fast simulation-based inference methods are increasingly needed to extract scientific insights. While diffusion-based approaches offer high-quality generative capabilities, they are hindered by slow sampling speeds. Our method performs posterior sampling an order of magnitude faster than a diffusion baseline. Applied to the problem of CMB delensing, it successfully recovers the unlensed CMB power spectrum from simulated observations. The model also remains robust to shifts in cosmological parameters, demonstrating its potential for out-of-distribution generalization and application to observational cosmological data.

</details>

---

### 62. [Estimation of Persistence Diagrams via the Three Gap Theorem](https://arxiv.org/abs/2603.04570)

**基本信息**

- 🔗 arXiv: [`2603.04570`](https://arxiv.org/abs/2603.04570)
- 👥 作者: Luis Suarez Salas, Jose A. Perea
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04570.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发拓扑数据分析（TDA）中持久同调的高效计算方法。TDA是化学信息学中用于分子表示、性质预测和结构分析的重要工具，因此该方法的进步与化学大模型的分析工具相关。

**📖 中文摘要**

本文结合数论中的三间隔定理和拓扑数据分析中的持久Künneth公式，提出了从准周期函数计算滑动窗口嵌入持久图的快速且可证明正确的近似方案。输入是信号的频谱。虽然应用背景是动力系统和准周期信号，但所开发的核心技术是拓扑数据分析（TDA）中持久同调的高效计算方法。持久同调是化学信息学和材料信息学中用于分析分子结构、材料孔隙和光谱形状的重要工具。因此，这种持久同调计算方法的进步与化学大模型中用于分子表示和分析的拓扑方法相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The time delay (or Sliding Window) embedding is a technique from dynamical systems to reconstruct attractors from time series data. Recently, descriptors from Topological Data Analysis (TDA) -- specifically, persistence diagrams -- have been used to measure the shape of said reconstructed attractors in applications including periodicity and quasiperiodicity quantification. Despite their utility, the fast computation of persistence diagrams of sliding window embeddings is still poorly understood. In this work, we present theoretical and computational schemes to approximate the persistence diagrams of sliding window embeddings from quasiperiodic functions. We do so by combining the Three Gap Theorem from number theory with the Persistent Künneth formula from TDA, and derive fast and provably correct persistent homology approximations. The input to our procedure is the spectrum of the signal, and we provide numerical as well as theoretical evidence of its utility to capture the shape of toroidal attractors.

</details>

---

### 63. [Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation](https://arxiv.org/abs/2603.04688)

**基本信息**

- 🔗 arXiv: [`2603.04688`](https://arxiv.org/abs/2603.04688)
- 👥 作者: Zafeirios Fountas, Adnan Oomerjee, Haitham Bou-Ammar 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04688.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从计算理论角度解释大脑巩固机制，并利用Transformer语言模型等进行模拟验证。这为理解大规模预训练模型（如化学大模型）的内部表征优化和泛化机制提供了理论视角和计算见解。

**📖 中文摘要**

本文提出，高容量的新皮层网络通过“预测性遗忘”（即选择性保留那些能预测未来结果或经验的信息）来优化存储的表征以实现泛化。论文在自编码器新皮层模型、生物合理的预测编码电路和基于Transformer的语言模型中通过模拟证明了这种容量依赖性。论文将离线巩固的计算角色定位为超越稳定的、结果条件化的压缩，以优化保留与泛化之间的权衡。这项工作从计算神经科学的角度，探讨了大规模神经网络（如Transformer）如何通过类似“巩固”的机制优化其内部表征。这对理解和大规模预训练化学模型（化学大模型）的学习动力学、表征演化和泛化能力具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Standard accounts of memory consolidation emphasise the stabilisation of stored representations, but struggle to explain representational drift, semanticisation, or the necessity of offline replay. Here we propose that high-capacity neocortical networks optimise stored representations for generalisation by reducing complexity via predictive forgetting, i.e. the selective retention of experienced information that predicts future outcomes or experience. We show that predictive forgetting formally improves information-theoretic generalisation bounds on stored representations. Under high-fidelity encoding constraints, such compression is generally unattainable in a single pass; high-capacity networks therefore benefit from temporally separated, iterative refinement of stored traces without re-accessing sensory input. We demonstrate this capacity dependence with simulations in autoencoder-based neocortical models, biologically plausible predictive coding circuits, and Transformer-based language models, and derive quantitative predictions for consolidation-dependent changes in neural representational geometry. These results identify a computational role for off-line consolidation beyond stabilisation, showing that outcome-conditioned compression optimises the retention-generalisation trade-off.

</details>

---

### 64. [Particle-Guided Diffusion for Gas-Phase Reaction Kinetics](https://arxiv.org/abs/2603.05139)

**基本信息**

- 🔗 arXiv: [`2603.05139`](https://arxiv.org/abs/2603.05139)
- 👥 作者: Andrew Millard, Henrik Pedersen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用扩散模型（一种生成式大模型）来解决化学反应动力学问题，直接围绕'化学大模型'这一主题。

**📖 中文摘要**

本文提出了一种用于气相化学反应动力学的粒子引导扩散方法。该方法将基于扩散模型的物理引导采样应用于由平流-反应-扩散方程描述的气相化学反应系统。研究在变化的参数上训练扩散模型，以生成物理一致的浓度场并准确预测出口浓度，包括在未见过的参数值下。这项工作展示了扩散模型在反应输运系统中进行推理的潜力，与化学信息学中利用生成模型（如化学大模型）进行反应预测和分子性质推理的研究主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

</details>

---

### 65. [Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks](https://arxiv.org/abs/2603.05188)

**基本信息**

- 🔗 arXiv: [`2603.05188`](https://arxiv.org/abs/2603.05188)
- 👥 作者: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05188.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发和应用大语言模型智能体进行化学材料的逆向设计，直接围绕'化学大模型'这一主题。

**📖 中文摘要**

本文介绍了Ara，一个基于大语言模型的智能体工作流，用于光催化共价有机框架的逆向设计。该工作流利用预训练的化学知识、给体-受体理论、共轭效应和连接键稳定性层次结构，指导搜索同时满足带隙、带边和水解稳定性标准的COFs。Ara通过结合GFN1-xTB片段筛选管道，在由各种节点、连接体、连接键和R基团组成的候选空间中，实现了52.7%的成功率，显著优于随机搜索和贝叶斯优化。该研究展示了LLM的化学先验知识可以显著加速多标准材料发现，是化学大模型在材料设计领域的直接应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

</details>

---

### 66. [GIT-BO: High-Dimensional Bayesian Optimization with Tabular Foundation Models](https://arxiv.org/abs/2505.20685)

**基本信息**

- 🔗 arXiv: [`2505.20685`](https://arxiv.org/abs/2505.20685)
- 👥 作者: Rosen Ting-Ying Yu, Cyril Picard, Faez Ahmed
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.20685.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用表格基础模型（一种特定类型的大模型）来增强高维贝叶斯优化，直接围绕'化学大模型'（可扩展至材料/化学性质优化）这一主题。

**📖 中文摘要**

本文提出了GIT-BO，一个梯度引导的贝叶斯优化框架，用于解决高维优化问题。该框架结合了TabPFN v2（一种表格基础模型，能够在上下文中进行零样本贝叶斯推理）和基于模型自身预测均值梯度计算的活动子空间机制。通过费舍尔信息估计将探索与内在低维子空间对齐，并使用UCB采集函数选择查询点，无需在线重新训练。该方法在包括合成和真实世界任务（如电力系统、MOPTA08、Mazda）在内的多达500维的基准测试中，展示了优于现有基于高斯过程的方法的性能和运行时优势。这项工作展示了基础模型在复杂优化问题中的应用，与利用大模型进行化学或材料属性预测与优化的主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian optimization (BO) struggles in high dimensions, where Gaussian-process surrogates demand heavy retraining and brittle assumptions, slowing progress on real engineering and design problems. We introduce GIT-BO, a Gradient-Informed BO framework that couples TabPFN v2, a tabular foundation model that performs zero-shot Bayesian inference in context, with an active-subspace mechanism computed from the model's own predictive-mean gradients. This aligns exploration to an intrinsic low-dimensional subspace via a Fisher-information estimate and selects queries with a UCB acquisition, requiring no online retraining. Across 60 problem variants spanning 20 benchmarks-nine scalable synthetic families and ten real-world tasks (e.g., power systems, Rover, MOPTA08, Mazda)-up to 500 dimensions, GIT-BO delivers a stronger performance-time trade-off than state-of-the-art GP-based methods (SAASBO, TuRBO, Vanilla BO, BAxUS), ranking highest in performance and with runtime advantages that grow with dimensionality. Limitations include memory footprint and dependence on the capacity of the underlying TFM.

</details>

---

### 67. [SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models](https://arxiv.org/abs/2506.01062)

**基本信息**

- 🔗 arXiv: [`2506.01062`](https://arxiv.org/abs/2506.01062)
- 👥 作者: Thinh Pham, Nguyen Nguyen, Pratibha Zunjare 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.01062.pdf)

**💡 相关性分析**

满足标准3：论文是对搜索增强语言模型推理能力的系统性评估和展望，其讨论的问题（如噪声数据处理、复杂推理）与构建用于'质谱结构推理'的可靠大模型所面临的挑战直接相关，提供了重要的相关讨论视角。

**📖 中文摘要**

本文介绍了SealQA，一个新的挑战性基准，用于评估搜索增强语言模型在事实寻求性问题上的表现，特别是当网络搜索产生冲突、嘈杂或无益结果时。该基准包含三个变体：Seal-0（主要）、Seal-Hard和LongSeal，分别评估事实准确性、推理能力和长上下文多文档推理。评估揭示了当前前沿模型（如GPT-4.1, o3-mini, DeepSeek-R1）在处理噪声搜索结果和复杂推理方面的显著局限性。这项工作虽然主要关注通用语言模型，但其对搜索增强、多步推理模型的评估框架和发现，与构建能够处理复杂、多源信息（如质谱数据与化学知识库结合）进行结构推理的化学大模型的研究高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce SealQA, a new challenge benchmark for evaluating SEarch-Augmented Language models on fact-seeking questions where web search yields conflicting, noisy, or unhelpful results. SealQA comes in three flavors: (1) Seal-0 (main) and (2) Seal-Hard, which assess factual accuracy and reasoning capabilities, with Seal-0 focusing on the most challenging questions where chat models (e.g., GPT-4.1) typically achieve near-zero accuracy; and (3) LongSeal, which extends SealQA to test long-context, multi-document reasoning in "needle-in-a-haystack" settings. Our evaluation reveals critical limitations in current models: Even frontier LLMs perform poorly across all SealQA flavors. On Seal-0, frontier agentic models equipped with tools like o3 and o4-mini achieve only 17.1% and 6.3% accuracy, respectively, at their best reasoning efforts. We find that advanced reasoning models such as DeepSeek-R1-671B and o3-mini are highly vulnerable to noisy search results. Notably, increasing test-time compute does not yield reliable gains across o3-mini, o4-mini, and o3, with performance often plateauing or even declining early. Additionally, while recent models are less affected by the "lost-in-the-middle" issue, they still fail to reliably identify relevant documents in LongSeal when faced with numerous distractors. To facilitate future work, we release SealQA at this http URL .

</details>

---

### 68. [HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals](https://arxiv.org/abs/2506.08618)

**基本信息**

- 🔗 arXiv: [`2506.08618`](https://arxiv.org/abs/2506.08618)
- 👥 作者: Xianquan Yan, Hakan Akgün, Kenji Kawaguchi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08618.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模、高质量的数据集HSG-12M，该数据集由复杂的图结构（哈密顿谱图）组成。虽然其直接应用领域是凝聚态物理，但所提出的图结构数据、自动化生成流程（Poly2Graph）以及相关的基准测试，为图神经网络和图表示学习（这是构建化学大模型和进行复杂结构推理的重要基础技术）的研究提供了宝贵的资源和工具。

**📖 中文摘要**

本文介绍了HSG-12M，一个包含1160万个静态和510万个动态哈密顿谱图的大规模数据集。该数据集源自非厄米量子物理领域，其中晶体的能谱在复平面上形成复杂的几何结构（哈密顿谱图）。论文的核心贡献是提出了Poly2Graph，一个将一维晶体哈密顿量自动映射为谱图的高性能开源流程。HSG-12M是第一个大规模的空间多重图数据集，其中节点嵌入在度量空间中，并且两个节点之间几何上不同的轨迹被保留为单独的边。这项工作为数据驱动的科学发现（如凝聚态物理）奠定了基础，并为几何感知的图学习提供了新的机会。虽然论文主要关注物理系统，但其核心是构建和提供了一个大规模、高质量的图结构数据集，并探讨了图神经网络在处理此类复杂空间图结构时面临的挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming scientific research by revealing new ways to understand complex physical systems, but its impact remains constrained by the lack of large, high-quality domain-specific datasets. A rich, largely untapped resource lies in non-Hermitian quantum physics, where the energy spectra of crystals form intricate geometries on the complex plane -- termed as Hamiltonian spectral graphs. Despite their significance as fingerprints for electronic behavior, their systematic study has been intractable due to the reliance on manual extraction. To unlock this potential, we introduce Poly2Graph: a high-performance, open-source pipeline that automates the mapping of 1-D crystal Hamiltonians to spectral graphs. Using this tool, we present HSG-12M: a dataset containing 11.6 million static and 5.1 million dynamic Hamiltonian spectral graphs across 1401 characteristic-polynomial classes, distilled from 177 TB of spectral potential data. Crucially, HSG-12M is the first large-scale dataset of spatial multigraphs -- graphs embedded in a metric space where multiple geometrically distinct trajectories between two nodes are retained as separate edges. This simultaneously addresses a critical gap, as existing graph benchmarks overwhelmingly assume simple, non-spatial edges, discarding vital geometric information. Benchmarks with popular GNNs expose new challenges in learning spatial multi-edges at scale. Beyond its practical utility, we show that spectral graphs serve as universal topological fingerprints of polynomials, vectors, and matrices, forging a new algebra-to-graph link. HSG-12M lays the groundwork for data-driven scientific discovery in condensed matter physics, new opportunities in geometry-aware graph learning and beyond.

</details>

---

### 69. [Bures-Wasserstein Flow Matching for Graph Generation](https://arxiv.org/abs/2506.14020)

**基本信息**

- 🔗 arXiv: [`2506.14020`](https://arxiv.org/abs/2506.14020)
- 👥 作者: Keyue Jiang, Jiahao Cui, Xiaowen Dong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图生成，这是化学信息学和药物发现中的核心任务。论文提出的BWFlow框架专门用于生成图结构数据，并在分子生成任务上进行了评估。分子结构是图的一种具体形式，因此该工作直接与“化学大模型”（特别是用于分子生成的生成模型）和“质谱结构推理”（结构推理是逆推分子结构的关键步骤）相关。

**📖 中文摘要**

本文提出了一种名为BWFlow的基于流匹配的图生成框架。针对现有扩散和流模型在生成图时通常独立建模节点和边的演化、使用线性插值导致概率路径不规则的局限性，BWFlow将图建模为由马尔可夫随机场参数化的连接系统，并利用MRF对象之间的最优传输位移来设计平滑的概率路径，确保图组件的协同演化。该方法在普通图生成和分子生成任务上进行了实验验证，取得了有竞争力的性能、更好的训练收敛性和高效的采样。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation has emerged as a critical task in fields ranging from drug discovery to circuit design. Contemporary approaches, notably diffusion and flow-based models, have achieved solid graph generative performance through constructing a probability path that interpolates between reference and data distributions. However, these methods typically model the evolution of individual nodes and edges independently and use linear interpolations in the disjoint space of nodes/edges to build the path. This disentangled interpolation breaks the interconnected patterns of graphs, making the constructed probability path irregular and non-smooth, which causes poor training dynamics and faulty sampling convergence. To address the limitation, this paper first presents a theoretically grounded framework for probability path construction in graph generative models. Specifically, we model the joint evolution of the nodes and edges by representing graphs as connected systems parameterized by Markov random fields (MRF). We then leverage the optimal transport displacement between MRF objects to design a smooth probability path that ensures the co-evolution of graph components. Based on this, we introduce BWFlow, a flow-matching framework for graph generation that utilizes the derived optimal probability path to benefit the training and sampling algorithm design. Experimental evaluations in plain graph generation and molecule generation validate the effectiveness of BWFlow with competitive performance, better training convergence, and efficient sampling.

</details>

---

### 70. [Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models](https://arxiv.org/abs/2507.18534)

**基本信息**

- 🔗 arXiv: [`2507.18534`](https://arxiv.org/abs/2507.18534)
- 👥 作者: Xingyu Qiu, Mengying Yang, Xinghua Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.18534.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是扩散模型的统一设计框架，特别是针对任意噪声的模式。扩散模型是当前生成式AI的前沿，也是构建能够生成和推理化学结构（如分子、质谱）的“化学大模型”的重要技术路径之一。论文对扩散模型理论框架的拓展和其在复杂噪声模式处理上的应用，与开发用于化学和质谱分析的生成式模型高度相关。

**📖 中文摘要**

本文提出了EDA（Elucidating the Design space of Arbitrary-noise diffusion models），旨在为处理不同噪声模式的扩散模型提供一个统一的理论框架。论文指出，现有EDM框架依赖固定高斯噪声，无法解释基于任意噪声的流方法，并且在图像修复任务中强制注入高斯噪声会产生负面影响。EDA扩展了噪声模式的灵活性，同时保持了EDM的模块化特性，并严格证明了增加噪声复杂性不会在修复过程中引入额外的计算开销。该方法在医学图像去噪（如MRI偏置场校正、CT金属伪影去除）和自然图像阴影去除等任务上进行了验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although EDM aims to unify the design space of diffusion models, its reliance on fixed Gaussian noise prevents it from explaining emerging flow-based methods that diffuse arbitrary noise. Moreover, our study reveals that EDM's forcible injection of Gaussian noise has adverse effects on image restoration task, as it corrupts the degraded images, overextends the restoration distance, and increases the task's complexity. To interpret diverse methods for handling distinct noise patterns within a unified theoretical framework and to minimize the restoration distance, we propose EDA, which Elucidates the Design space of Arbitrary-noise diffusion models. Theoretically, EDA expands noise pattern flexibility while preserving EDM's modularity, with rigorous proof that increased noise complexity introduces no additional computational overhead during restoration. EDA is validated on three representative medical image denoising and natural image restoration tasks: MRI bias field correction (global smooth noise), CT metal artifact removal (global sharp noise) and natural image shadow removal (local boundary-aware noise). With only 5 sampling steps, competitive results against specialized methods across medical and natural tasks demonstrate EDA's strong generalization capability for image restoration. Code is available at: this https URL .

</details>

---

### 71. [Topology Structure Optimization of Reservoirs Using GLMY Homology](https://arxiv.org/abs/2509.11612)

**基本信息**

- 🔗 arXiv: [`2509.11612`](https://arxiv.org/abs/2509.11612)
- 👥 作者: Yu Chen, Shengwei Wang, Hongwei Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.11612.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是复杂网络（储层计算）的拓扑结构分析与优化。储层计算是处理时序数据（如光谱、质谱信号）的一种有效模型。对网络拓扑结构的深入理解和优化方法，对于构建能够处理复杂化学或光谱时序数据的“化学大模型”具有基础性意义。结构推理的本质也与网络拓扑分析相关。

**📖 中文摘要**

本文研究了储层计算网络的拓扑结构对其性能的影响。利用持久的GLMY同调理论分析储层结构，并发现网络性能与一维GLMY同调群密切相关。基于此，论文提出了一种通过修改一维GLMY同调群的最小代表环来优化储层结构的方法。实验验证了储层性能同时受到网络结构和数据集周期性的共同影响。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reservoir is an efficient network for time series processing. It is well known that network structure is one of the determinants of its performance. However, the topology structure of reservoirs, as well as their performance, is hard to analyzed, due to the lack of suitable mathematical tools. In this paper, we study the topology structure of reservoirs using persistent GLMY homology theory, and develop a method to improve its performance. Specifically, it is found that the reservoir performance is closely related to the one-dimensional GLMY homology groups. Then, we develop a reservoir structure optimization method by modifying the minimal representative cycles of one-dimensional GLMY homology groups. Finally, by experiments, it is validated that the performance of reservoirs is jointly influenced by the reservoir structure and the periodicity of the dataset.

</details>

---

### 72. [TabStruct: Measuring Structural Fidelity of Tabular Data](https://arxiv.org/abs/2509.11950)

**基本信息**

- 🔗 arXiv: [`2509.11950`](https://arxiv.org/abs/2509.11950)
- 👥 作者: Xiangjian Jiang, Nikola Simidjievski, Mateja Jamnik
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.11950.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个全面的评估框架TabStruct和新的评估指标“全局效用”，用于衡量表格数据生成模型的结构保真度。化学和质谱数据经常以表格形式存在（如分子描述符表、质谱峰表）。评估这些数据生成模型的质量，特别是其保持底层化学结构关系的能力，是化学信息学和质谱分析中的关键需求。因此，该论文提供的评估工具和基准与主题相关。

**📖 中文摘要**

本文提出了TabStruct，一个用于评估表格数据生成器的综合基准。论文指出，现有评估方法往往忽略了表格数据特有的因果结构先验，即“结构保真度”。为此，作者引入了一个新的评估指标“全局效用”，使得即使在缺乏真实因果结构的情况下也能评估结构保真度。TabStruct基准包含对来自9个类别的13个表格生成器在29个数据集上的大规模定量分析。结果表明，全局效用为表格生成器性能提供了一个与任务无关、领域无关的评估视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating tabular generators remains a challenging problem, as the unique causal structural prior of heterogeneous tabular data does not lend itself to intuitive human inspection. Recent work has introduced structural fidelity as a tabular-specific evaluation dimension to assess whether synthetic data complies with the causal structures of real data. However, existing benchmarks often neglect the interplay between structural fidelity and conventional evaluation dimensions, thus failing to provide a holistic understanding of model performance. Moreover, they are typically limited to toy datasets, as quantifying existing structural fidelity metrics requires access to ground-truth causal structures, which are rarely available for real-world datasets. In this paper, we propose a novel evaluation framework that jointly considers structural fidelity and conventional evaluation dimensions. We introduce a new evaluation metric, $\textbf{global utility}$, which enables the assessment of structural fidelity even in the absence of ground-truth causal structures. In addition, we present $\textbf{TabStruct}$, a comprehensive evaluation benchmark offering large-scale quantitative analysis on 13 tabular generators from nine distinct categories, across 29 datasets. Our results demonstrate that global utility provides a task-independent, domain-agnostic lens for tabular generator performance. We release the TabStruct benchmark suite, including all datasets, evaluation pipelines, and raw results. Code is available at this https URL .

</details>

---

### 73. [Beyond Prefixes: Graph-as-Memory Cross-Attention for Knowledge Graph Completion with Large Language Models](https://arxiv.org/abs/2510.08966)

**基本信息**

- 🔗 arXiv: [`2510.08966`](https://arxiv.org/abs/2510.08966)
- 👥 作者: Ruitong Liu, Boxu Lin, Peize Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.08966.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何将结构化知识（知识图谱）与大型语言模型深度融合以进行推理和补全。这直接对应于“化学大模型”的研究方向，即如何让大模型理解和利用化学领域的结构化知识（如分子知识图谱、反应网络）进行推理。同时，知识图谱补全本身也是一种结构推理任务，与“质谱结构推理”中从数据推断分子结构的逻辑相似。

**📖 中文摘要**

本文提出了图即记忆调优（Graph-as-Memory Tuning, GMT），一种将知识图谱与大型语言模型融合的新范式，用于知识图谱补全等知识密集型任务。与现有通过前缀拼接注入图信息的浅层交互方法不同，GMT将局部图结构表示为显式的图记忆，并通过深层的、基于令牌的交叉注意力机制将其注入LLM。具体来说，GMT使用语义图模块在知识增强关系的指导下编码局部邻域的上下文感知语义，并将其压缩为固定数量的图记忆令牌。然后，一个图即记忆交叉注意力融合模块将这些令牌集成到多个Transformer层中，允许LLM隐藏状态动态检索相关的图证据。实验表明，GMT显著优于前缀调优等基线方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fusing Knowledge Graphs with Large Language Models (LLMs) is crucial for knowledge-intensive tasks like knowledge graph completion. Existing LLM-based approaches typically inject graph information via prefix concatenation, resulting in shallow interactions that fail to support fine-grained evidence retrieval during generation. Beyond prefixes, we propose Graph-as-Memory Tuning (GMT), a new paradigm that represents local graph structure as explicit graph memory and injects it into LLMs via deep, token-wise cross-attention. Specifically, GMT first employs a Semantic Graph Module to encode context-aware semantics from local neighborhoods guided by knowledge-enhanced relations, and compresses them into a fixed number of graph memory tokens. A Graph-as-Memory Cross-Attention Fusion Module then integrates these tokens into multiple Transformer layers, allowing LLM hidden state to dynamically retrieve relevant graph evidence. To enable efficient adaptation, GMT applies LoRA only to the memory cross-attention while keeping the base LLM frozen. Extensive experiments show that GMT significantly outperforms prefix-tuning and other strong baselines, providing more potent signals for robust reasoning. The code is published at this https URL .

</details>

---

### 74. [LLEMA: Evolutionary Search with LLMs for Multi-Objective Materials Discovery](https://arxiv.org/abs/2510.22503)

**基本信息**

- 🔗 arXiv: [`2510.22503`](https://arxiv.org/abs/2510.22503)
- 👥 作者: Nikhil Abhyankar, Sanchit Kabra, Saaketh Desai 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22503.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（LLM）引导的进化算法进行材料发现。这属于“化学大模型”在材料科学和化学领域的直接应用。LLM被用于生成和优化化学结构（晶体结构），并与计算模拟（代理模型）结合进行多目标优化，完美契合了利用AI大模型加速化学和材料研究的主题。

**📖 中文摘要**

本文提出了LLEMA（LLM-guided Evolution for MAterials discovery），一个用于多目标材料发现的统一框架。该框架将大型语言模型中嵌入的科学知识与化学信息化的进化规则以及基于记忆的优化相结合。在每次迭代中，LLM在明确的属性约束下提出晶体学指定的候选材料；一个由代理模型增强的“预言机”估算物理化学性质；一个多目标评分器更新成功/失败记忆以指导后续世代。在涵盖电子、能源、涂层、光学和航空航天等领域的14个现实任务中，LLEMA发现的候选材料在化学合理性、热力学稳定性和属性对齐方面表现优异，相对于生成式和纯LLM基线，实现了更高的命中率和改进的帕累托前沿质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Materials discovery requires navigating vast chemical and structural spaces while satisfying multiple, often conflicting, objectives. We present LLM-guided Evolution for MAterials discovery (LLEMA), a unified framework that couples the scientific knowledge embedded in large language models with chemistry-informed evolutionary rules and memory-based refinement. At each iteration, an LLM proposes crystallographically specified candidates under explicit property constraints; a surrogate-augmented oracle estimates physicochemical properties; and a multi-objective scorer updates success/failure memories to guide subsequent generations. Evaluated on 14 realistic tasks that span electronics, energy, coatings, optics, and aerospace, LLEMA discovers candidates that are chemically plausible, thermodynamically stable, and property-aligned, achieving higher hit rates and improved Pareto front quality relative to generative and LLM-only baselines. Ablation studies confirm the importance of rule-guided generation, memory-based refinement, and surrogate prediction. By enforcing synthesizability and multi-objective trade-offs, LLEMA provides a principled approach to accelerating practical materials discovery. Project website: this https URL

</details>

---

### 75. [Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling](https://arxiv.org/abs/2510.26139)

**基本信息**

- 🔗 arXiv: [`2510.26139`](https://arxiv.org/abs/2510.26139)
- 👥 作者: Minseo Kwon, Young J. Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.26139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用视觉语言模型（VLM）来增强复杂规划任务中的推理和决策。虽然应用场景是机器人操作，但其核心方法论——利用多模态大模型（VLM）进行状态理解、引导搜索和回溯推理——与“化学大模型”和“质谱结构推理”中需要模型进行多步骤、基于复杂输入（如光谱图像、分子图）的推理过程在技术上高度相似。这展示了多模态大模型在解决需要复杂空间和逻辑推理问题上的潜力。

**📖 中文摘要**

本文提出了一种结合视觉语言模型（VLM）引导的动力学任务与运动规划器。该方法基于一个统一表示符号和数值状态的混合状态树进行规划，使得任务和运动决策能够共同决定。动力学约束由现成的运动规划器和物理模拟器验证，VLM通过状态的可视化渲染来引导探索TAMP解决方案并基于此进行搜索回溯。实验表明，该方法在模拟和真实世界中相比传统和基于LLM的TAMP规划器，平均成功率提高了32.14%到1166.67%，并在复杂问题上减少了规划时间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Task and Motion Planning (TAMP) integrates high-level task planning with low-level motion feasibility, but existing methods are costly in long-horizon problems due to excessive motion sampling. While LLMs provide commonsense priors, they lack 3D spatial reasoning and cannot ensure geometric or dynamic feasibility. We propose a kinodynamic TAMP planner based on a hybrid state tree that uniformly represents symbolic and numeric states during planning, enabling task and motion decisions to be jointly decided. Kinodynamic constraints embedded in the TAMP problem are verified by an off-the-shelf motion planner and physics simulator, and a VLM guides exploring a TAMP solution and backtracks the search based on visual rendering of the states. Experiments on the simulated domains and in the real world show 32.14% - 1166.67% increased average success rates compared to traditional and LLM-based TAMP planners and reduced planning time on complex problems, with ablations further highlighting the benefits of VLM backtracking. More details are available at this https URL .

</details>

---

### 76. [FMint-SDE: A Multimodal Foundation Model for Accelerating Numerical Simulation of SDEs via Error Correction](https://arxiv.org/abs/2510.27173)

**基本信息**

- 🔗 arXiv: [`2510.27173`](https://arxiv.org/abs/2510.27173)
- 👥 作者: Jiaxin Yuan, Haizhao Yang, Maria Cameron
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27173.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于加速科学计算（微分方程求解）的基础模型。在化学和质谱分析中，分子动力学模拟、化学反应动力学、光谱模拟等都依赖于微分方程的数值求解。一个能够通用、高效地模拟此类动力学系统的多模态基础模型，对于构建“化学大模型”（尤其是那些需要集成物理模拟的模型）和深入理解质谱背后的物理化学过程（结构推理的一部分）具有重要价值。

**📖 中文摘要**

本文介绍了FMint-SDE，一个用于加速随机微分方程数值模拟的多模态基础模型。该模型基于一个具有上下文学习能力的仅解码器Transformer，利用数值和文本模态来学习通用的误差校正方案。它通过使用传统求解器生成的粗略解序列进行提示训练，从而能够广泛泛化到不同的系统。作者在分子动力学、机械系统、金融和生物学等一系列具有挑战性的SDE基准测试上评估了模型。实验结果表明，该方法相比经典求解器实现了更优的精度-效率权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fast and accurate simulation of dynamical systems is a fundamental challenge across scientific and engineering domains. Traditional numerical integrators often face a trade-off between accuracy and computational efficiency, while existing neural network-based approaches typically require training a separate model for each case. To overcome these limitations, we introduce a novel multi-modal foundation model for large-scale simulations of differential equations: FMint-SDE (Foundation Model based on Initialization for stochastic differential equations). Based on a decoder-only transformer with in-context learning, FMint-SDE leverages numerical and textual modalities to learn a universal error-correction scheme. It is trained using prompted sequences of coarse solutions generated by conventional solvers, enabling broad generalization across diverse systems. We evaluate our models on a suite of challenging SDE benchmarks spanning applications in molecular dynamics, mechanical systems, finance, and biology. Experimental results show that our approach achieves a superior accuracy-efficiency tradeoff compared to classical solvers, underscoring the potential of FMint-SDE as a general-purpose simulation tool for dynamical systems.

</details>

---

### 77. [Revolutionizing Mixed Precision Quantization: Towards Training-free Automatic Proxy Discovery via Large Language Models](https://arxiv.org/abs/2512.07419)

**基本信息**

- 🔗 arXiv: [`2512.07419`](https://arxiv.org/abs/2512.07419)
- 👥 作者: Haidong Kang, Jun Du, Lihong Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.07419.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）作为智能代理，自动设计和优化混合精度量化（MPQ）的代理模型。这直接关联到“化学大模型”主题中关于利用大模型（作为智能体或优化器）解决复杂科学计算和模型设计问题的研究方向。

**📖 中文摘要**

本文提出了一种名为TAP（Training-free Automatic Proxy）的新型混合精度量化（MPQ）框架，旨在解决传统MPQ方法依赖昂贵优化搜索或人工设计代理的问题。该框架利用大型语言模型（LLM）和进化搜索策略，自动发现适用于MPQ的、无需训练的代理。通过引入一个轻量级的基于直接偏好优化（DPO）的策略控制器，动态调整进化搜索策略中提示模板的选择概率，形成一个任务感知的反馈循环，从而在无需微调LLM的情况下改进代理生成。这项工作代表了利用LLM驱动算法设计MPQ代理的新范式，与“化学大模型”主题相关，因为它展示了LLM在复杂科学计算任务（如模型优化和参数搜索）中作为智能设计代理的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixed-Precision Quantization (MPQ) liberates Deep Neural Networks (DNNs) from the Out-Of-Memory (OOM) bottleneck and has garnered increasing research attention. However, conventional methods either rely on costly differentiable optimization search, which is neither efficient nor flexible, or learn a quantized DNN from a proxy (e.g., HAWQ) manually designed by human experts, which is labor-intensive and requires extensive expert knowledge. Can we design a proxy without involving any human experts or training? In this paper, we provide an affirmative answer by proposing a novel Large Language Model (LLM)-driven Training-free Automatic Proxy (dubbed TAP) discovery framework. It reforms the design paradigm of MPQ by utilizing LLMs and evolutionary search strategies to automatically find superior TAP tailored for MPQ. In addition, to bridge the gap between black-box LLMs and the challenging MPQ task, we introduce a lightweight Direct Preference Optimization (DPO)-based strategy controller that dynamically reweights the selection probabilities of the three prompt templates for evolutionary search strategies according to fitness signals, without fine-tuning the LLM. This forms a task-aware feedback loop that improves proxy generation across evolutions. Extensive experiments on mainstream benchmarks demonstrate that TAP achieves state-of-the-art performance. Finally, we believe that our TAP will significantly contribute to the MPQ community by providing a new perspective on LLM-driven design algorithms.

</details>

---

### 78. [Interleaved Tool-Call Reasoning for Protein Function Understanding](https://arxiv.org/abs/2601.03604)

**基本信息**

- 🔗 arXiv: [`2601.03604`](https://arxiv.org/abs/2601.03604)
- 👥 作者: Chuanliu Fan, Zicheng Ma, Huanran Meng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.03604.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于蛋白质功能理解的工具增强型大模型智能体（PFUA）。这直接关联到“化学大模型”主题，即开发面向化学/生命科学领域的、具备专业推理和工具使用能力的大模型或智能体框架。其方法论（结合领域工具进行可靠推理）也对“质谱结构推理”中构建智能解析系统具有重要参考价值。

**📖 中文摘要**

本文提出了PFUA（Protein Function Understanding Agent），一个工具增强的蛋白质推理智能体，用于解决蛋白质功能理解这一知识密集型科学任务。论文指出，直接将基于文本的思维链推理范式迁移到蛋白质功能预测是无效的，因为该任务根本上依赖于外部的生物学先验知识和计算工具，而非纯粹的内部推理。PFUA统一了问题分解、工具调用和基于证据的答案生成。它利用领域特定工具（如生物信息学数据库和计算工具）来产生可验证的中间证据，而不是依赖长而无约束的推理轨迹。在四个基准测试上的实验表明，PFUA consistently outperforms text-only reasoning models。这项工作与“化学大模型”和“质谱结构推理”都高度相关，因为它展示了如何构建一个专门针对化学/生物学领域（蛋白质功能）的、工具增强的大模型智能体，以进行可靠的科学推理和预测，这可以类比于构建用于质谱数据解析和结构推理的领域专家智能体。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

</details>

---

### 79. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)

**基本信息**

- 🔗 arXiv: [`2601.18734`](https://arxiv.org/abs/2601.18734)
- 👥 作者: Siyan Zhao, Zhihui Xie, Mengchen Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18734.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种用于提升大型语言模型推理能力的自蒸馏训练框架（OPSD）。这直接关联到“化学大模型”主题中关于如何有效训练和优化用于复杂科学推理（如化学结构推理）的大模型的研究方向。

**📖 中文摘要**

本文提出了On-Policy Self-Distillation (OPSD)框架，用于改进大型语言模型（LLM）的推理能力。在该框架中，单个模型同时扮演教师和学生的角色：教师策略基于特权信息（如已验证的推理轨迹）进行条件生成，而学生策略仅基于问题；训练目标是最小化在学生自身生成的轨迹上，这两种策略分布的每词元差异。该方法在多个数学推理基准测试中展示了高效性和优越性能。这项工作与“化学大模型”主题相关，因为它提出了一种新颖的、基于自蒸馏的LLM推理能力优化方法。这种方法可以应用于训练专门用于化学推理（如逆合成分析、性质预测）或质谱解析推理的大模型，提升其从有限或噪声数据中学习可靠推理模式的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self (i.e., the version without access to privileged information), we introduce On-Policy Self-Distillation (OPSD), a framework where a single model acts as both teacher and student by conditioning on different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving 8-12x token efficiency compared to reinforcement learning methods such as GRPO and superior performance over off-policy distillation methods.

</details>

---

### 80. [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2602.01601)

**基本信息**

- 🔗 arXiv: [`2602.01601`](https://arxiv.org/abs/2602.01601)
- 👥 作者: Hieu Trung Nguyen, Bao Nguyen, Wenao Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01601.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大模型强化学习微调（RL from verifiable rewards）的采样效率优化算法。这直接关联到“化学大模型”主题中关于如何高效训练和优化大模型（例如，通过GRPO等RL方法训练模型解决化学问题）的关键技术挑战。

**📖 中文摘要**

本文针对具有可验证奖励的强化学习（如GRPO）中的采样效率瓶颈问题，提出了VIP（Variance-Informed Predictive allocation）策略。该策略不再为所有训练提示（prompt）平均分配计算资源（rollout次数），而是使用一个轻量级高斯过程模型预测每个提示的成功概率，并将其转化为梯度方差估计，进而通过凸优化在给定计算预算下确定最优的rollout分配方案。实验结果表明，VIP能持续提高采样效率并在多个基准测试中取得更高性能。这项工作与“化学大模型”主题相关，因为它解决的是大模型（特别是用于代码生成、数学或科学问题求解的模型）通过强化学习进行微调时的核心效率问题。高效训练策略对于构建需要处理大量候选结构或反应路径的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce VIP, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, VIP uses a lightweight Gaussian process model to predict per-prompt success probabilities based on recent rollouts. These probability predictions are translated into variance estimates, which are then fed into a convex optimization problem to determine the optimal rollout allocations under a hard compute budget constraint. Empirical results show that VIP consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks.

</details>

---

### 81. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型（Zatom-1），这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

本文介绍了Zatom-1，这是第一个端到端、完全开源的基础模型，它统一了3D分子和材料的生成与预测学习。Zatom-1是一个使用多模态流匹配目标训练的Transformer，能够联合建模离散的原子类型和连续的3D几何结构。该方法支持可扩展的预训练，并能够进行快速稳定的采样。通过联合生成式预训练作为下游多任务预测（如性质、能量和力）的通用初始化。实验表明，Zatom-1在生成和预测基准测试中匹配或优于专门的基线模型，同时将生成推理时间减少了一个数量级以上。这项工作表明，联合生成式预训练在化学领域之间产生了正向的预测迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first end-to-end, fully open-source foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 82. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于材料科学的机器学习原子间势（MLIP）基础模型（MatRIS），这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

本文提出了MatRIS，一种用于材料科学的机器学习原子间势（MLIP）基础模型。MatRIS是一种不变性MLIP，引入了基于注意力的三体相互作用建模。它利用了一种新颖的、具有线性复杂度的可分离注意力机制，实现了可扩展性和表达性。MatRIS在广泛的流行基准测试（如Matbench-Discovery、MatPES等）上提供了与领先的等变模型相当的准确性，同时训练成本更低。这项工作表明，精心设计的不变性模型可以以更低的成本匹配或超过等变模型的准确性，为开发准确高效的MLIPs提供了启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 83. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于联想记忆模型（如Hopfield网络）中的顺序检索和推理动力学，这与构建和理解能够进行复杂推理的“化学大模型”的底层机制高度相关。

**📖 中文摘要**

本文为Hopfield网络中的顺序推理开发了一个动力学理论。作者考虑了最近提出的输入驱动可塑性（IDP）Hopfield网络，并分析了一个将快速关联检索与慢速推理动力学耦合的双时间尺度架构。他们推导出了自持记忆转换的明确条件，包括增益阈值、逃逸时间和崩溃机制。这些结果为关联记忆模型中的顺序性提供了原理性的数学解释，弥合了经典Hopfield动力学和现代推理架构之间的差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 84. [Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning](https://arxiv.org/abs/2603.03229)

**基本信息**

- 🔗 arXiv: [`2603.03229`](https://arxiv.org/abs/2603.03229)
- 👥 作者: Adam Watts, Andrew Jeon, Destry Newton 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03229.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用机器学习（条件变分自编码器）从谱数据逆向重建时间序列信号。虽然应用背景是冲击工程，但其核心方法论——使用生成模型解决逆向问题、从结构化数据（谱）推断原始信号（时间序列）——与“质谱结构推理”中从质谱数据推断分子结构的核心挑战在方法论上高度相似。

**📖 中文摘要**

本文提出了一种条件变分自编码器（CVAE），用于从冲击响应谱（SRS）曲线逆向重建加速度时间序列。该模型学习了一个从SRS到加速度时间序列的数据驱动逆向映射。一旦训练完成，模型可以生成与指定目标谱一致的信号，而无需迭代优化。实验表明，相对于经典技术，该方法在谱保真度方面有所改进，对未见过的谱具有强大的泛化能力，并且推理速度比传统方法快三到六个数量级。这些结果确立了深度生成建模作为逆向SRS重建的可扩展且高效的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions. We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

</details>

---

### 85. [LoRA-MME: Multi-Model Ensemble of LoRA-Tuned Encoders for Code Comment Classification](https://arxiv.org/abs/2603.03959)

**基本信息**

- 🔗 arXiv: [`2603.03959`](https://arxiv.org/abs/2603.03959)
- 👥 作者: Md Akib Haider, Ahsan Bulbul, Nafis Fuad Shahid 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03959.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究方法涉及使用参数高效微调（LoRA）和模型集成来优化基于Transformer的预训练模型在特定任务上的性能。这种方法论对于在“化学信息学”等领域构建和定制“化学大模型”具有直接的参考价值。

**📖 中文摘要**

本文介绍了LoRA-MME，一个用于代码注释分类的多模型集成架构，采用了参数高效微调（PEFT）。该方法通过结合四个不同的Transformer编码器（UniXcoder, CodeBERT, GraphCodeBERT, CodeBERTa）的优势，并利用低秩适应（LoRA）独立微调这些模型，最后通过学习的加权集成策略聚合它们的预测，从而最大化分类性能。虽然论文应用在代码分析领域，但其核心方法——使用LoRA对多个预训练模型进行高效微调并集成——是构建和优化领域特定“大模型”的有效策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Code comment classification is a critical task for automated software documentation and analysis. In the context of the NLBSE'26 Tool Competition, we present LoRA-MME, a Multi-Model Ensemble architecture utilizing Parameter-Efficient Fine-Tuning (PEFT). Our approach addresses the multi-label classification challenge across Java, Python, and Pharo by combining the strengths of four distinct transformer encoders: UniXcoder, CodeBERT, GraphCodeBERT, and CodeBERTa. By independently fine-tuning these models using Low-Rank Adaptation(LoRA) and aggregating their predictions via a learned weighted ensemble strategy, we maximize classification performance without the memory overhead of full model fine-tuning. Our tool achieved an F1 Weighted score of 0.7906 and a Macro F1 of 0.6867 on the test set. However, the computational cost of the ensemble resulted in a final submission score of 41.20%, highlighting the trade-off between semantic accuracy and inference efficiency.

</details>

---

### 86. [Highly Efficient and Effective LLMs with Multi-Boolean Architectures](https://arxiv.org/abs/2505.22811)

**基本信息**

- 🔗 arXiv: [`2505.22811`](https://arxiv.org/abs/2505.22811)
- 👥 作者: Ba-Hien Tran, Van Minh Nguyen
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.22811.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大型语言模型（LLMs）提出了一种新颖的、高效的二值化表示和训练框架。虽然不特定于化学，但其所研究的模型压缩和高效推理技术是构建可部署的、资源高效的“化学大模型”的关键使能技术。

**📖 中文摘要**

本文提出了一个新颖的框架，该框架使用多核布尔参数表示大型语言模型（LLMs），并首次实现了在布尔域中直接微调LLMs，消除了对潜在权重的需求。这增强了表示能力，并显著降低了微调和推理期间的复杂度。在各种LLMs上的大量实验表明，该方法优于最近的超低位量化和二值化技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight binarization has emerged as a promising strategy to reduce the complexity of large language models (LLMs). Existing approaches fall into post-training binarization, which is simple but causes severe performance loss, and training-aware methods, which depend on full-precision latent weights, adding complexity and limiting efficiency. We propose a novel framework that represents LLMs with multi-kernel Boolean parameters and, for the first time, enables direct finetuning LMMs in the Boolean domain, eliminating the need for latent weights. This enhances representational capacity and dramatically reduces complexity during both finetuning and inference. Extensive experiments across diverse LLMs show our method outperforms recent ultra low-bit quantization and binarization techniques.

</details>

---

### 87. [Structured quantum learning via em algorithm for Boltzmann machines](https://arxiv.org/abs/2507.21569)

**基本信息**

- 🔗 arXiv: [`2507.21569`](https://arxiv.org/abs/2507.21569)
- 👥 作者: Takeshi Kimura, Kohtaro Kato, Masahito Hayashi
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.21569.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对量子机器学习模型（量子玻尔兹曼机）提出新的训练算法。虽然侧重于量子模型，但其解决生成模型训练挑战（如贫瘠高原）的方法，对于在经典计算框架下开发和训练复杂的“化学大模型”（尤其是生成模型）具有启发意义。

**📖 中文摘要**

本文为量子玻尔兹曼机（QBMs）引入了一种量子版本的EM算法，这是一种信息几何学上对经典期望最大化方法的推广，它绕过了在非凸函数上进行基于梯度的优化。在一个半量子限制玻尔兹曼机（sqRBM）——一种将量子效应限制在隐藏层的混合架构——上实现该方法，在多个基准数据集上实现了稳定的学习并优于梯度下降。这些结果为量子机器学习中的梯度训练提供了一种结构化和可扩展的替代方案，为缓解贫瘠高原和增强量子生成建模提供了一条途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Boltzmann machines (QBMs) are generative models with potential advantages in quantum machine learning, yet their training is fundamentally limited by the barren plateau problem, where gradients vanish exponentially with system size. We introduce a quantum version of the em algorithm, an information-geometric generalization of the classical Expectation-Maximization method, which circumvents gradient-based optimization on non-convex functions. Implemented on a semi-quantum restricted Boltzmann machine (sqRBM) -- a hybrid architecture with quantum effects confined to the hidden layer -- our method achieves stable learning and outperforms gradient descent on multiple benchmark datasets. These results establish a structured and scalable alternative to gradient-based training in QML, offering a pathway to mitigate barren plateaus and enhance quantum generative modeling.

</details>

---

### 88. [CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery](https://arxiv.org/abs/2511.19500)

**基本信息**

- 🔗 arXiv: [`2511.19500`](https://arxiv.org/abs/2511.19500)
- 👥 作者: Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.19500.pdf)

**💡 相关性分析**

满足标准1和标准2。核心主题相关：该论文的核心是开发用于化学材料（有机光伏）发现的机器学习模型，属于化学大模型的应用范畴。数据资源相关：论文提出了一个大型精选数据集OPV2D，可用于训练和评估化学大模型。

**📖 中文摘要**

本文提出了一个用于有机光伏（OPV）材料发现的机器学习框架CycleChemist。该框架结合了预测建模与生成式分子设计，并引入了OPV2D数据集，这是目前最大的、包含2000个经过实验表征的给体-受体对的精选数据集。框架包含多个组件：用于预测材料是否具有OPV行为的分类器（OPVC）、一个结合多任务学习和给体-受体相互作用建模的层次图神经网络、用于预测HOMO/LUMO能级的分子轨道能量估计器（MOE2）、用于估计功率转换效率（PCE）的光伏性能预测器（P3），以及用于生成可合成有机半导体的材料生成预训练变换器（MatGPT）。该工作通过将分子表示学习与性能预测相结合，推动了高性能OPV材料的数据驱动发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials.

</details>

---

### 89. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的核心研究内容直接围绕“化学大模型”展开，提出了一种新的、更高效的化学大语言模型推理范式（LatentChem），并对其在化学推理任务上的性能进行了评估。

**📖 中文摘要**

本文针对化学大语言模型（LLMs）提出了LatentChem，一种潜在推理接口。作者指出，当前化学LLMs主要依赖自然语言中的显式思维链（CoT）进行复杂推理，但化学推理本质上是连续和结构化的，将其强制转换为离散的语言标记会引入表示不匹配，限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中直接执行多步推理，而仅在最终输出时生成语言。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理内部化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，而且在计算上具有优势。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于强CoT基线取得了59.88%的非平局胜率，同时实现了平均10.84倍的推理加速。结果表明，化学推理作为一种连续的潜在动态过程，比离散的语言轨迹更自然、更有效。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 90. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的研究内容涉及图结构预测和不确定性量化，其应用场景明确包括“分子识别”。这直接关联到化学信息学中利用图神经网络进行分子性质预测或结构推理的核心任务，为相关模型（如用于质谱结构推理的模型）提供了不确定性评估的理论框架和方法。

**📖 中文摘要**

本文提出了一种用于图结构输出的保形预测框架，旨在为结构化输出空间（如图）提供分布无关的覆盖保证。该方法通过Z-Gromov-Wasserstein距离（实践中实例化为Fused Gromov-Wasserstein距离）来定义非保形性，从而实现对预测图和候选图之间置换不变的比较。为了获得自适应的预测集，作者将保形化分位数回归（CQR）扩展到复杂输出空间，提出了分数保形化分位数回归（SCQR）。论文在一个合成任务和一个真实的分子识别问题上评估了所提出的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 91. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的核心是开发一个自动化化学计算（DFT）的智能框架。DFT是计算化学和材料科学中用于预测分子和材料电子结构及性质的核心方法。自动化DFT工作流的框架属于“化学大模型”或更广泛的“AI for Science”在化学领域的应用，旨在提升化学计算的效率和可及性。

**📖 中文摘要**

本文介绍了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学的基石，但其实际执行需要协调复杂、多步骤的工作流程。现有的工具和基于LLM的解决方案只能自动化部分步骤，缺乏对完整工作流自动化、多样化任务适应以及DFT配置中精度-成本权衡优化的支持。TritonDFT通过专家策划的可扩展工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效且准确的DFT执行。此外，作者还引入了DFTBench，一个用于评估智能体在多维度能力（包括科学专业知识、权衡优化、高性能计算知识和成本效率）的基准。TritonDFT为实际使用提供了开放的接口。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：15
- 累计论文数量：1045

## 📝 历史记录

> 暂无历史数据

