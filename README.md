# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-08 12:45:10

## 📅 2026-03-08 (今日最新)

**相关论文数：64**

### 1. [A unified foundational framework for knowledge injection and evaluation of Large Language Models in Combustion Science](https://arxiv.org/abs/2603.04452)

**基本信息**

- 🔗 arXiv: [`2603.04452`](https://arxiv.org/abs/2603.04452)
- 👥 作者: Zonglin Yang, Runze Mao, Tianhao Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04452.pdf)

**💡 相关性分析**

满足标准1和标准2：论文核心研究内容直接围绕为化学领域（燃烧科学）开发专业化的基础大语言模型（化学大模型）。同时，论文提供了专门构建的、可用于该主题的多模态知识库（数据集）和评估基准（工具/资源）。

**📖 中文摘要**

本文提出了一个用于燃烧科学领域大语言模型（LLM）开发的端到端框架，旨在推进该领域的化学信息学基础模型。该框架包含一个规模达35亿token的多模态知识库（从同行评审文章、论文和燃烧CFD代码中提取）、一个严格的自动化评估基准（CombustionQA），以及一个三阶段的知识注入路径（从轻量级检索增强生成到知识图谱增强检索和持续预训练）。研究定量验证了第一阶段（朴素RAG）的性能上限，并指出构建领域基础模型需要结构化知识图谱和持续预训练。这项工作直接围绕“化学大模型”主题，旨在为特定化学领域（燃烧科学）开发专业化的LLM，并提供了相关的数据集、资源和评估工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To advance foundation Large Language Models (LLMs) for combustion science, this study presents the first end-to-end framework for developing domain-specialized models for the combustion community. The framework comprises an AI-ready multimodal knowledge base at the 3.5 billion-token scale, extracted from over 200,000 peer-reviewed articles, 8,000 theses and dissertations, and approximately 400,000 lines of combustion CFD code; a rigorous and largely automated evaluation benchmark (CombustionQA, 436 questions across eight subfields); and a three-stage knowledge-injection pathway that progresses from lightweight retrieval-augmented generation (RAG) to knowledge-graph-enhanced retrieval and continued pretraining. We first quantitatively validate Stage 1 (naive RAG) and find a hard ceiling: standard RAG accuracy peaks at 60%, far surpassing zero-shot performance (23%) yet well below the theoretical upper bound (87%). We further demonstrate that this stage's performance is severely constrained by context contamination. Consequently, building a domain foundation model requires structured knowledge graphs and continued pretraining (Stages 2 and 3).

</details>

---

### 2. [Standing on the Shoulders of Giants: Rethinking EEG Foundation Model Pretraining via Multi-Teacher Distillation](https://arxiv.org/abs/2603.04478)

**基本信息**

- 🔗 arXiv: [`2603.04478`](https://arxiv.org/abs/2603.04478)
- 👥 作者: Chenqi Li, Yu Liu, Shuo Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04478.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过利用其他模态的大模型（基础模型/大模型）来改进和引导特定领域（EEG，可类比化学信息学）基础模型的训练。这直接涉及“化学大模型”主题中关于如何构建和优化领域专用大模型的方法论。

**📖 中文摘要**

本文提出了一种用于脑电图（EEG）基础模型预训练的新范式——多教师蒸馏预训练（MTDP）。与主流依赖于自监督掩码重建的方法不同，MTDP通过两阶段蒸馏，利用来自其他成熟模态（如视觉和时间序列）的预训练基础模型（如DINOv3, Chronos）的知识，来引导EEG基础模型的训练。该方法首先通过一个可学习的门控网络融合来自不同教师的表示，然后将其蒸馏到一个EEG基础模型中。在9个下游任务和12个数据集上的评估表明，MTDP模型优于自监督对比模型，且仅需25%的预训练数据。这项工作虽然聚焦于EEG，但其核心思想——利用跨模态的预训练大模型（视觉、时间序列基础模型）来引导和提升特定领域（可类比于化学）基础模型的性能——与“化学大模型”的主题高度相关，展示了构建领域专用大模型的一种有效方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pretraining for electroencephalogram (EEG) foundation models has predominantly relied on self-supervised masked reconstruction, a paradigm largely adapted from and inspired by the success of vision and language foundation models. However, unlike images and text, EEG datasets are notoriously expensive to collect and characterized by low signal-to-noise ratio. These challenges introduce difficulties in scaling the EEG foundation models and capturing the underlying neural semantics through reconstruction. In this work, we ask the question: can we stand on the shoulders of well-established foundation models from well-represented modalities to bootstrap the pretraining of EEG foundation models? We first demonstrate that mainstream foundation models, such as those from vision and time series, transfer surprisingly well to EEG domain. To this end, we propose the Multi-Teacher Distillation Pretraining (MTDP) framework for pretraining EEG foundation models via a two-stage multi-teacher distillation. In the first stage, we introduce a learnable gating network to fuse representations from diverse teachers (e.g., DINOv3 and Chronos) via a masked latent denoising objective. In the second stage, we distill the fused representation into an EEG foundation model. Extensive evaluations across 9 downstream tasks and 12 datasets demonstrate that our MTDP-based EEG foundation model outperforms its self-supervised counterparts while requiring only 25% of the pretraining data.

</details>

---

### 3. [Augmenting representations with scientific papers](https://arxiv.org/abs/2603.04516)

**基本信息**

- 🔗 arXiv: [`2603.04516`](https://arxiv.org/abs/2603.04516)
- 👥 作者: Nicolò Oreste Pinciroli Vago, Rocco Di Tella, Carolina Cuesta-Lázaro 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04516.pdf)

**💡 相关性分析**

满足标准1和标准3：论文核心研究内容是将科学数据（X射线光谱）与科学文献文本对齐以构建增强的多模态表示，这直接关联“化学大模型”（构建理解科学数据的模型）和“质谱结构推理”（光谱数据与结构/文本信息的关联）。同时，这项工作为如何整合科学文献知识到数据驱动模型中提供了重要的方法论讨论。

**📖 中文摘要**

本文介绍了一个对比学习框架，旨在将X射线光谱与从科学文献中提取的领域知识对齐，从而促进共享多模态表示的发展。该框架通过一个对比学习流程，实现了从光谱中检索相关文本（Recall@1%达到20%），证明了在这两种模态之间建立有意义的对齐是可能的。此外，得到的共享潜在空间有效地编码了具有物理意义的信息。通过融合光谱和文本数据，对20个物理变量的估计比单模态光谱基线提高了16-18%。这项工作展示了如何将观测数据（如光谱）与现有科学文献（文本）对齐，以创建更强大的多模态表示。虽然应用在天体物理学，但其核心方法——对齐科学数据（可视为一种“化学”或“物理”数据）与科学文本以增强模型理解和性能——与“化学大模型”和“质谱结构推理”的主题高度相关，为化学信息学中类似问题（如质谱与文献关联）提供了思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Astronomers have acquired vast repositories of multimodal data, including images, spectra, and time series, complemented by decades of literature that analyzes astrophysical sources. Still, these data sources are rarely systematically integrated. This work introduces a contrastive learning framework designed to align X-ray spectra with domain knowledge extracted from scientific literature, facilitating the development of shared multimodal representations. Establishing this connection is inherently complex, as scientific texts encompass a broader and more diverse physical context than spectra. We propose a contrastive pipeline that achieves a 20% Recall@1% when retrieving texts from spectra, proving that a meaningful alignment between these modalities is not only possible but capable of accelerating the interpretation of rare or poorly understood sources. Furthermore, the resulting shared latent space effectively encodes physically significant information. By fusing spectral and textual data, we improve the estimation of 20 physical variables by 16-18% over unimodal spectral baselines. Our results indicate that a Mixture of Experts (MoE) strategy, which leverages both unimodal and shared representations, yields superior performance. Finally, outlier analysis within the multimodal latent space identifies high-priority targets for follow-up investigation, including a candidate pulsating ULX (PULX) and a gravitational lens system. Importantly, this framework can be extended to other scientific domains where aligning observational data with existing literature is possible.

</details>

---

### 4. [Discovering mathematical concepts through a multi-agent system](https://arxiv.org/abs/2603.04528)

**基本信息**

- 🔗 arXiv: [`2603.04528`](https://arxiv.org/abs/2603.04528)
- 👥 作者: Daattavya Aggarwal, Oisin Kim, Carl Henrik Ek 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04528.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个能够自主进行科学概念发现和推理的多智能体AI系统。这直接关联“化学大模型”和“质谱结构推理”的终极目标之一，即构建能够像科学家一样进行假设驱动探索和结构推断的智能系统。

**📖 中文摘要**

本文提出了一种新的多智能体模型，用于计算数学发现，其灵感来源于数学概念通过实验、证明尝试和反例等过程交互涌现的观察。该系统自主提出猜想并尝试证明它们，根据反馈和不断演化的数据分布做出决策。受欧拉多面体猜想历史的启发，该研究以从多面体数据和线性代数知识中自主恢复同调概念为基准任务。该系统成功完成了这一学习问题。实验通过消融研究，统计测试了完整动态的价值。这项工作展示了通过优化局部过程的正确组合，可以导向与数学趣味性惊人一致的概念。虽然主题是数学发现，但其核心——设计能够自主进行科学推理（提出假设、验证、修正）的多智能体系统——与“化学大模型”和“质谱结构推理”中关于开发能够进行假设生成和结构推断的AI系统的愿景高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical concepts emerge through an interplay of processes, including experimentation, efforts at proof, and counterexamples. In this paper, we present a new multi-agent model for computational mathematical discovery based on this observation. Our system, conceived with research in mind, poses its own conjectures and then attempts to prove them, making decisions informed by this feedback and an evolving data distribution. Inspired by the history of Euler's conjecture for polyhedra and an open challenge in the literature, we benchmark with the task of autonomously recovering the concept of homology from polyhedral data and knowledge of linear algebra. Our system completes this learning problem. Most importantly, the experiments are ablations, statistically testing the value of the complete dynamic and controlling for experimental setup. They support our main claim: that the optimisation of the right combination of local processes can lead to surprisingly well-aligned notions of mathematical interestingness.

</details>

---

### 5. [PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation](https://arxiv.org/abs/2603.04531)

**基本信息**

- 🔗 arXiv: [`2603.04531`](https://arxiv.org/abs/2603.04531)
- 👥 作者: Rosy Chen, Mustafa Mukadam, Michael Kaess 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04531.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种利用特权数据（真实触觉）来蒸馏和增强感知模型的方法论。这与“质谱结构推理”中利用高置信度实验数据或专家知识来训练和提升结构推断模型的核心挑战和方法有很强的类比性和相关性。

**📖 中文摘要**

本文提出了PTLD（sim-to-real Privileged Tactile Latent Distillation），一种无需触觉模拟即可学习触觉操作技能的新方法。其核心思想是利用真实世界中的特权传感器收集真实的触觉策略数据，然后用于蒸馏出一个基于触觉输入的鲁棒状态估计器。实验表明，PTLD可以显著改进在模拟中训练的本体感知操作策略，通过融入触觉感知。在灵巧手旋转任务上，PTLD比纯本体感知策略有182%的提升。这项工作虽然聚焦于机器人触觉，但其方法论——利用真实世界的特权数据（可类比于高精度质谱或专家标注的结构数据）来蒸馏和增强一个更通用的感知模型（可类比于质谱结构推理模型）——与“质谱结构推理”中利用高质量数据提升模型推理能力的思路相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tactile dexterous manipulation is essential to automating complex household tasks, yet learning effective control policies remains a challenge. While recent work has relied on imitation learning, obtaining high quality demonstrations for multi-fingered hands via robot teleoperation or kinesthetic teaching is prohibitive. Alternatively, with reinforcement we can learn skills in simulation, but fast and realistic simulation of tactile observations is challenging. To bridge this gap, we introduce PTLD: sim-to-real Privileged Tactile Latent Distillation, a novel approach to learning tactile manipulation skills without requiring tactile simulation. Instead of simulating tactile sensors or relying purely on proprioceptive policies to transfer zero-shot sim-to-real, our key idea is to leverage privileged sensors in the real world to collect real-world tactile policy data. This data is then used to distill a robust state estimator that operates on tactile input. We demonstrate from our experiments that PTLD can be used to improve proprioceptive manipulation policies trained in simulation significantly by incorporating tactile sensing. On the benchmark in-hand rotation task, PTLD achieves a 182% improvement over a proprioception only policy. We also show that PTLD enables learning the challenging task of tactile in-hand reorientation where we see a 57% improvement in the number of goals reached over using proprioception alone. Website: this https URL .

</details>

---

### 6. [PDE foundation model-accelerated inverse estimation of system parameters in inertial confinement fusion](https://arxiv.org/abs/2603.04606)

**基本信息**

- 🔗 arXiv: [`2603.04606`](https://arxiv.org/abs/2603.04606)
- 👥 作者: Mahindra Rautela, Alexander Scheinker, Bradley Love 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04606.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容围绕利用预训练的PDE基础模型（可视为一种科学计算领域的大模型）解决从多模态观测数据（如高光谱图像）中估计系统参数的逆问题。这直接关联“化学大模型”（广义的科学计算模型）和“质谱结构推理”（从复杂光谱数据中推断参数/结构）的主题。

**📖 中文摘要**

本文研究了偏微分方程（PDE）基础模型在惯性约束聚变（ICF）逆问题中的应用，即从多模态观测数据中估计系统参数。研究使用JAG基准数据集，对预训练的PDE基础模型进行微调，并训练一个轻量级的任务特定头，以联合重建高光谱图像和回归系统参数。实验表明，微调后的模型在参数估计上表现出色（R^2高达0.995）。这项工作展示了基础模型（一种特定类型的“化学大模型”）在解决科学计算逆问题（包括从光谱数据中推断参数）方面的潜力，其方法论与“化学大模型”和从复杂观测数据（类似于质谱）中“推理结构/参数”的主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PDE foundation models are typically pretrained on large, diverse corpora of PDE datasets and can be adapted to new settings with limited task-specific data. However, most downstream evaluations focus on forward problems, such as autoregressive rollout prediction. In this work, we study an inverse problem in inertial confinement fusion (ICF): estimating system parameters (inputs) from multi-modal, snapshot-style observations (outputs). Using the open JAG benchmark, which provides hyperspectral X-ray images and scalar observables per simulation, we finetune the PDE foundation model and train a lightweight task-specific head to jointly reconstruct hyperspectral images and regress system parameters. The fine-tuned model achieves accurate hyperspectral reconstruction (test MSE 1.2e-3) and strong parameter-estimation performance (up to R^2=0.995). Data-scaling experiments (5%-100% of the training set) show consistent improvements in both reconstruction and regression losses as the amount of training data increases, with the largest marginal gains in the low-data regime. Finally, finetuning from pretrained MORPH weights outperforms training the same architecture from scratch, demonstrating that foundation-model initialization improves sample efficiency for data-limited inverse problems in ICF.

</details>

---

### 7. [When Agents Persuade: Propaganda Generation and Mitigation in LLMs](https://arxiv.org/abs/2603.04636)

**基本信息**

- 🔗 arXiv: [`2603.04636`](https://arxiv.org/abs/2603.04636)
- 👥 作者: Julia Jose, Ritik Roongta, Rachel Greenstadt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04636.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从扩散MRI测量数据中，通过可微分物理模拟和优化，推理并重建微观组织屏障（结构）。这本质上是一个从复杂谱信号（dMRI信号）中“推理结构”的逆问题，与“质谱结构推理”从质谱信号推断分子结构的核心主题直接相关。

**📖 中文摘要**

本文提出了Spinverse，一种用于扩散磁共振成像（dMRI）的、感知渗透率的微结构重建方法。该方法通过一个完全可微分的Bloch-Torrey模拟器来反演dMRI测量值。Spinverse将组织表示在固定的四面体网格上，并将每个内部面的渗透率作为可学习参数；低渗透率的面充当扩散屏障，从而在不改变网格连接的情况下浮现出微结构边界。给定目标信号，通过反向传播信号匹配损失来优化面渗透率，并通过阈值化学习到的渗透率场来恢复界面。该方法旨在从dMRI测量中明确重建微观屏障（结构），其“从测量数据中推理微观结构”的核心问题与“质谱结构推理”从谱数据中推断分子结构在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their wide-ranging benefits, LLM-based agents deployed in open environments can be exploited to produce manipulative material. In this study, we task LLMs with propaganda objectives and analyze their outputs using two domain-specific models: one that classifies text as propaganda or non-propaganda, and another that detects rhetorical techniques of propaganda (e.g., loaded language, appeals to fear, flag-waving, name-calling). Our findings show that, when prompted, LLMs exhibit propagandistic behaviors and use a variety of rhetorical techniques in doing so. We also explore mitigation via Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and ORPO (Odds Ratio Preference Optimization). We find that fine-tuning significantly reduces their tendency to generate such content, with ORPO proving most effective.

</details>

---

### 8. [Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings](https://arxiv.org/abs/2603.04692)

**基本信息**

- 🔗 arXiv: [`2603.04692`](https://arxiv.org/abs/2603.04692)
- 👥 作者: Lyle Regenwetter, Rosen Yu, Cyril Picard 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04692.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进表格基础模型（TabPFN 2.5）在数据稀缺的工程/科学领域（如化学信息学）的泛化能力。通过嵌入引导的合成数据筛选和持续预训练来优化基础模型，这直接围绕“化学大模型”（表格基础模型）的领域适应和性能提升展开。

**📖 中文摘要**

本文研究了表格回归任务中，基础模型（TabPFN 2.5）从合成数据到工程数据领域的迁移问题。作者发现工程数据集与非工程数据集在表示空间中可以部分区分，而标准程序生成的合成数据集与工程数据集之间存在显著的领域差距。为了在不使用真实工程样本的情况下弥合这一差距，论文提出了一种基于嵌入的合成数据筛选方法：生成并识别“类工程”的合成数据集，然后仅使用筛选出的合成任务对TabPFN 2.5进行持续预训练。在35个工程回归数据集上的实验表明，这种仅使用合成数据的适应方法提高了预测准确性和数据效率。这项工作涉及为科学和工业领域（可能包括化学信息学）开发和改进基础模型（大模型），并专注于处理数据稀缺的领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression datasets with expert engineering/non-engineering labels, and use TabPFN 2.5's dataset-level embedding to study domain structure in a common representation space. We find that engineering datasets are partially distinguishable from non-engineering datasets, while standard procedurally generated datasets are highly distinguishable from engineering datasets, revealing a substantial synthetic-real domain gap. To bridge this gap without training on real engineering samples, we propose an embedding-guided synthetic data curation method: we generate and identify "engineering-like" synthetic datasets, and perform continued pre-training of TabPFN 2.5 using only the selected synthetic tasks. Across 35 engineering regression datasets, this synthetic-only adaptation improves predictive accuracy and data efficiency, outperforming TabPFN 2.5 on 29/35 datasets and AutoGluon on 27/35, with mean multiplicative data-efficiency gains of 1.75x and 4.44x, respectively. More broadly, our results indicate that principled synthetic data curation can convert procedural generators into domain-relevant "data engines," enabling foundation models to improve in data-sparse scientific and industrial domains where real data collection is the primary bottleneck.

</details>

---

### 9. [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](https://arxiv.org/abs/2603.04743)

**基本信息**

- 🔗 arXiv: [`2603.04743`](https://arxiv.org/abs/2603.04743)
- 👥 作者: Maojun Sun, Yue Wu, Yifei Xie 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04743.pdf)

**💡 相关性分析**

满足标准2：论文提出了DARE模型和RCodingAgent智能体，这些是专门为增强LLM在R统计生态系统（化学信息学和生物信息学的核心工具集）中的能力而设计的工具和资源。这为“化学大模型”在专业科学计算环境中的应用提供了具体的工具和数据集（RPKB）。

**📖 中文摘要**

本文提出了DARE（Distribution-Aware Retrieval Embedding），一个轻量级、即插即用的检索模型，用于将数据分布信息融入R函数表示中，以改进R软件包的检索。主要贡献包括：（i）RPKB，一个从8,191个高质量CRAN包中提取的R包知识库；（ii）DARE嵌入模型；（iii）RCodingAgent，一个面向R的LLM智能体，用于可靠的R代码生成。论文系统评估了LLM智能体在现实分析场景中的表现。DARE在包检索任务上达到了93.47%的NDCG@10，优于现有开源嵌入模型。将DARE集成到RCodingAgent中，在下游分析任务上带来了显著增益。这项工作旨在缩小LLM自动化与成熟的R统计生态系统（广泛用于化学计量学和生物信息学）之间的差距，为化学信息学领域提供了潜在的、增强的AI辅助工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

</details>

---

### 10. [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827)

**基本信息**

- 🔗 arXiv: [`2603.04827`](https://arxiv.org/abs/2603.04827)
- 👥 作者: Ben S. Southworth, Jonas A. Actor, Graham Harper 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕Kolmogorov-Arnold网络（KANs）展开，这是一种具有特定数学结构的新型神经网络架构，属于‘化学大模型’研究范畴中探索新型模型架构的一部分。

**📖 中文摘要**

本文研究了Kolmogorov-Arnold网络（KANs）的多级训练方法。KANs是一种具有明确数学结构（如样条基函数）的神经网络，与传统的多层感知机（MLP）相比，其结构更利于算法加速。论文首先建立了使用样条基函数的KANs与具有幂ReLU激活函数的多通道MLPs之间的等价性。基于这种等价性，作者提出了一种多级训练策略：通过样条节点的均匀细化，定义一系列自然相关的KANs模型，并利用解析几何插值算子在不同层级的模型间传递知识。这种“适当嵌套的层次结构”确保了在精细模型上保留粗粒度模型的训练进展，同时样条基函数的紧支撑特性保证了后续层级的互补优化。数值实验表明，该方法在训练可比KANs或MLPs时，相比传统方法能实现数量级上的精度提升，特别是在物理信息神经网络（PINN）中效果显著。这项工作展示了神经网络的有原则设计如何产生可利用的结构，从而实现能极大提升训练性能的多级算法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

</details>

---

### 11. [SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms](https://arxiv.org/abs/2603.04873)

**基本信息**

- 🔗 arXiv: [`2603.04873`](https://arxiv.org/abs/2603.04873)
- 👥 作者: Longkun Xu, Xiaochun Zhang, Qiantu Tuo 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04873.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个能够自主生成和优化时间序列预测算法代码的智能体（SEA-TS）。这属于‘化学大模型’研究范畴中AI for Science（AI4S）和自动化机器学习（AutoML）的交叉领域，探讨了如何利用大模型或智能体框架来自动化科学计算和算法设计流程。

**📖 中文摘要**

本文提出了SEA-TS，一个用于时间序列预测算法代码自主生成、验证和优化的自进化智能体框架。该框架通过迭代的自进化循环，旨在解决传统机器学习开发中的数据稀缺、分布漂移适应性差以及手动迭代收益递减等问题。SEA-TS引入了三个关键创新：1) 度量优势蒙特卡洛树搜索，用归一化的优势分数替代固定奖励，以提供更具区分性的搜索指导；2) 带有运行提示精炼的代码审查，每个执行的解决方案都会经过自动化审查，随后更新提示以编码纠正模式，防止类似错误复发；3) 全局可引导推理，将每个节点与全局最优和最差解决方案进行比较，实现跨轨迹知识迁移。该框架采用MAP-Elites存档来维持架构多样性。在公开的Solar-Energy基准测试和专有数据集上的实验表明，SEA-TS生成的代码在预测精度上超越了现有最先进方法和人工设计的基线模型，并且能够发现新颖的架构模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate time series forecasting underpins decision-making across domains, yet conventional ML development suffers from data scarcity in new deployments, poor adaptability under distribution shift, and diminishing returns from manual iteration. We propose Self-Evolving Agent for Time Series Algorithms (SEA-TS), a framework that autonomously generates, validates, and optimizes forecasting code via an iterative self-evolution loop. Our framework introduces three key innovations: (1) Metric-Advantage Monte Carlo Tree Search (MA-MCTS), which replaces fixed rewards with a normalized advantage score for discriminative search guidance; (2) Code Review with running prompt refinement, where each executed solution undergoes automated review followed by prompt updates that encode corrective patterns, preventing recurrence of similar errors; and (3) Global Steerable Reasoning, which compares each node against global best and worst solutions, enabling cross-trajectory knowledge transfer. We adopt a MAP-Elites archive for architectural diversity. On the public Solar-Energy benchmark, SEA-TS generated code achieves a 40% MAE reduction relative to TimeMixer, surpassing state-of-the-art methods. On proprietary datasets, SEA-TS generated code reduces WAPE by 8.6% on solar PV forecasting and 7.7% on residential load forecasting compared to human-engineered baselines, and achieves 26.17% MAPE on load forecasting versus 29.34% by TimeMixer. Notably, the evolved models discover novel architectural patterns--including physics-informed monotonic decay heads encoding solar irradiance constraints, per-station learned diurnal cycle profiles, and learnable hourly bias correction--demonstrating that autonomous ML engineering can generate genuinely novel algorithmic ideas beyond manual design.

</details>

---

### 12. [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900)

**基本信息**

- 🔗 arXiv: [`2603.04900`](https://arxiv.org/abs/2603.04900)
- 👥 作者: Shuo Yang, Soyeon Caren Han, Xueqi Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大语言模型（LLM）智能体的工具使用策略。这直接属于‘化学大模型’研究范畴中智能体（Agent）和工具调用（Tool Use）的关键方向，旨在提升LLM在复杂任务中的规划和执行能力。

**📖 中文摘要**

本文提出了EvoTool，一个通过无梯度进化范式优化模块化工具使用策略的自进化框架。针对基于大语言模型（LLM）的智能体在解决复杂任务时对有效工具使用策略的依赖，以及现有优化方法面临的延迟监督和长轨迹信用分配困难等问题，EvoTool将智能体的工具使用策略分解为规划器、选择器、调用器和合成器四个模块，并通过一个自改进循环迭代优化它们。该框架包含三个新颖机制：基于轨迹的归因定位、反馈引导的定向突变和多样性感知的种群选择。通过在四个基准测试上的评估，EvoTool在GPT-4.1和Qwen3-8B等模型上均显著优于现有基线，同时实现了更高的效率和可迁移性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

</details>

---

### 13. [$\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](https://arxiv.org/abs/2603.04948)

**基本信息**

- 🔗 arXiv: [`2603.04948`](https://arxiv.org/abs/2603.04948)
- 👥 作者: Peihao Wang, Ruisi Cai, Zhen Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04948.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型（LLM）的推理能力，提出了一种新颖的、基于测试时梯度下降的推理框架（$\nabla$-Reasoner）。这直接属于‘化学大模型’研究范畴中模型推理、优化和算法创新的核心议题。

**📖 中文摘要**

本文提出了$\nabla$-Reasoner，一种在潜在空间通过测试时梯度下降进行大语言模型（LLM）推理的迭代生成框架。针对现有推理时扩展方法依赖低效离散搜索或试错提示的局限性，该框架将基于词元logits的可微分优化集成到解码循环中，以在线优化策略。其核心组件“可微分文本优化”（DTO）利用来自LLM似然和奖励模型的梯度信号来优化文本表示。$\nabla$-Reasoner进一步结合了拒绝采样和加速设计以增强鲁棒性和解码速度。理论分析表明，在样本空间执行推理时梯度下降以最大化奖励，与通过KL正则化强化学习对齐LLM策略是对偶的。在具有挑战性的数学推理基准测试中，$\nabla$-Reasoner实现了超过20%的准确率提升，同时相比强基线减少了约10-40%的模型调用次数。这项工作将测试时优化从零阶搜索转向一阶优化，为增强LLM推理能力提供了一条经济有效的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

</details>

---

### 14. [Programmable superconducting neuron with intrinsic in-memory computation and dual-timescale plasticity for ultra-efficient neuromorphic computing](https://arxiv.org/abs/2603.04966)

**基本信息**

- 🔗 arXiv: [`2603.04966`](https://arxiv.org/abs/2603.04966)
- 👥 作者: Muen Wang, Shucheng Yang, Yuxiang Lin 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04966.pdf)

**💡 相关性分析**

满足标准1：论文提出的将计算、内存和可塑性融合于一体的可编程超导神经元架构，其核心思想（事件驱动、内存计算、多时间尺度适应）与构建高效、专用的“化学大模型”用于质谱等数据的结构推理在技术范式上直接相关。

**📖 中文摘要**

本文提出了一种可编程的超导神经元，用于超高效神经形态计算。该神经元集成了本征内存计算和双时间尺度可塑性，将计算、内存和可塑性融合到单个超导单元中。虽然论文的核心是硬件和神经形态计算，但其提出的“本征内存计算”概念和用于模拟生物神经元可塑性的架构，与化学信息学中构建能够学习和推理分子结构（如质谱数据）的“化学大模型”在理念上高度相关。这种融合计算与内存的硬件设计思想，可以为未来专门用于化学结构推理和生成的大模型提供高效的底层计算架构启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The escalating energy demands of artificial intelligence pose a critical challenge to conventional computing. Leveraging the efficiency of event-driven, in-memory neuromorphic architectures into the superconducting circuits with ultra-high speed and low power dissipation advantages offers a promising solution to energy-efficient computing. However, the potential of such a solution has yet to be realized, owning to the absence of a fundamental superconducting unit that unifies programmability, local memory, and multi-timescale plasticity. Here, we introduce a programmable Josephson-junction-based leaky integrate-and-fire (LIF) neuron that features intrinsic static memory and precise programmability by encoding somatic and synaptic parameters directly in the bias current. This neuron is also capable of dual-timescale plasticity: picosecond-scale short-term modulation of spike transmission and long-term weight retention exceeding 10,000 seconds, facilitating both rapid temporal adaptation and robust weight storage. It can operate up to 45 GHz with femtojoule-level energy dissipation per spike, and supports 10 somatic threshold levels and 20 synaptic states. Furthermore, we demonstrate a crossbar-based spiking neural network (SNN) utilizing this neuron, which achieves outstanding performance across multiple tasks. By fusing computation, memory and plasticity into a single superconducting unit, our work paves the way for the next generation of ultrafast, energy-efficient neuromorphic computing.

</details>

---

### 15. [When Weak LLMs Speak with Confidence, Preference Alignment Gets Stronger](https://arxiv.org/abs/2603.04968)

**基本信息**

- 🔗 arXiv: [`2603.04968`](https://arxiv.org/abs/2603.04968)
- 👥 作者: Amirabbas Afzali, Myeongho Jeon, Maria Brbic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04968.pdf)

**💡 相关性分析**

满足标准1：论文研究的核心是利用弱模型进行高效模型对齐与优化的方法学，这直接关系到如何构建、训练和优化面向特定领域（如化学信息学）的“大模型”，是构建化学大模型的关键支撑技术之一。

**📖 中文摘要**

本文探讨了在大型语言模型（LLM）与人类价值观对齐（偏好对齐）任务中，使用弱LLM作为标注者的有效性。研究发现，仅选择弱LLM高置信度的样本子集进行训练，其效果甚至优于使用完整人工标注。基于此，作者提出了置信度加权的偏好优化（CW-PO）通用框架。这项研究属于大模型训练与对齐方法学范畴。虽然不直接针对化学或质谱，但其核心——如何利用（可能不完美的）模型或数据源来更高效地训练或优化另一个模型——是构建和优化“化学大模型”所需的关键技术之一。例如，在质谱结构推理中，可以利用多个不完美的预测模型或数据库来生成训练数据或进行模型微调。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Preference alignment is an essential step in adapting large language models (LLMs) to human values, but existing approaches typically depend on costly human annotations or large-scale API-based models. We explore whether a weak LLM can instead act as an effective annotator. We surprisingly find that selecting only a subset of a weak LLM's highly confident samples leads to substantially better performance than using full human annotations. Building on this insight, we propose Confidence-Weighted Preference Optimization (CW-PO), a general framework that re-weights training samples by a weak LLM's confidence and can be applied across different preference optimization objectives. Notably, the model aligned by CW-PO with just 20% of human annotations outperforms the model trained with 100% of annotations under standard DPO. These results suggest that weak LLMs, when paired with confidence weighting, can dramatically reduce the cost of preference alignment while even outperforming methods trained on fully human-labeled data.

</details>

---

### 16. [Functionality-Oriented LLM Merging on the Fisher--Rao Manifold](https://arxiv.org/abs/2603.04972)

**基本信息**

- 🔗 arXiv: [`2603.04972`](https://arxiv.org/abs/2603.04972)
- 👥 作者: Jiayu Wang, Zuojun Ye, Wenpeng Yin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04972.pdf)

**💡 相关性分析**

满足标准1：论文专注于大模型权重空间的合并技术，这对于整合针对化学信息学不同子任务（如质谱推理、分子生成）训练的多个专家模型，构建统一、强大的“化学大模型”具有直接的方法论参考价值。

**📖 中文摘要**

本文提出了一种在Fisher-Rao流形上合并多个微调后的大型语言模型（LLM）权重的算法。该方法旨在解决现有基于参数空间欧几里得平均的方法在合并功能异构的模型时容易导致表示崩溃和性能下降的问题。通过将模型合并表述为计算Fisher-Rao流形上的加权Karcher均值，该方法能更稳定地合并多个专家的功能。这项研究属于大模型的高效部署与集成领域。对于“化学大模型”而言，未来可能会针对不同的分子性质预测、反应预测或质谱解析任务训练出多个专家模型，如何将这些专家模型的能力安全、高效地合并到一个统一的模型中，是一个重要的实际问题。本文提供了一种具有理论保证的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective. We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

</details>

---

### 17. [VRM: Teaching Reward Models to Understand Authentic Human Preferences](https://arxiv.org/abs/2603.04974)

**基本信息**

- 🔗 arXiv: [`2603.04974`](https://arxiv.org/abs/2603.04974)
- 👥 作者: Biao Liu, Ning Xu, Junming Yang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04974.pdf)

**💡 相关性分析**

满足标准1：论文提出的变分奖励建模框架，其目标是为大模型训练设计更精准、抗干扰的评估机制。这一技术可直接应用于训练用于分子生成或质谱解析的化学大模型，为其提供高质量的训练信号（奖励）。

**📖 中文摘要**

本文提出了一种新颖的变分奖励建模（VRM）框架，旨在使奖励模型更好地理解真实的人类偏好，以解决大语言模型对齐中的奖励黑客问题。该框架通过变分推理技术，将人类评估过程建模为包含高维目标权重和低维语义特征的隐变量。这项工作属于大模型对齐与强化学习领域。虽然不直接涉及化学，但其核心思想——如何设计更鲁棒、更能捕捉复杂评估标准（在化学中可能是结构正确性、合成可行性、生物活性等）的奖励函数或评估模型——对于训练用于分子设计或质谱结构推理的生成式“化学大模型”至关重要。一个能够准确评估生成分子质量的奖励模型是此类大模型成功训练的关键组件。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have achieved remarkable success across diverse natural language tasks, yet the reward models employed for aligning LLMs often encounter challenges of reward hacking, where the approaches predominantly rely on directly mapping prompt-response pairs to scalar scores, which may inadvertently capture spurious correlations rather than authentic human preferences. In contrast, human evaluation employs a sophisticated process that initially weighs the relative importance of multiple high-dimensional objectives according to the prompt context, subsequently evaluating response quality through low-dimensional semantic features such as logical coherence and contextual appropriateness. Motivated by this consideration, we propose VRM, i.e., Variational Reward Modeling, a novel framework that explicitly models the evaluation process of human preference judgments by incorporating both high-dimensional objective weights and low-dimensional semantic features as latent variables, which are inferred through variational inference techniques. Additionally, we provide a theoretical analysis showing that VRM can achieve a tighter generalization error bound compared to the traditional reward model. Extensive experiments on benchmark datasets demonstrate that VRM significantly outperforms existing methods in capturing authentic human preferences.

</details>

---

### 18. [Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination](https://arxiv.org/abs/2603.05040)

**基本信息**

- 🔗 arXiv: [`2603.05040`](https://arxiv.org/abs/2603.05040)
- 👥 作者: Hyuntae Park, Yeachan Kim, SangKeun Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05040.pdf)

**💡 相关性分析**

满足标准1：论文核心是探索如何通过引入机器生成的视觉模态来增强大模型的推理能力，以克服单一文本模态的偏差。这种利用生成模型辅助多模态推理的思路，与化学信息学中结合分子图、谱图图像等多源信息进行结构推理的研究主题高度相关。

**📖 中文摘要**

本文针对预训练语言模型在零样本常识推理中因文本知识存在的人类报告偏差而受限的问题，提出了Imagine框架。该框架通过将机器生成的图像（视觉信号）作为额外模态，来增强模型的推理能力。具体而言，它在推理流程中嵌入了一个图像生成器，使模型具备“想象”能力，并利用合成的视觉问答数据来训练模型有效利用视觉上下文。这项工作属于多模态大模型与常识推理领域。对于“化学大模型”和“质谱结构推理”而言，引入多模态信息（如分子结构图、谱图可视化、3D分子构象）是提升模型推理能力的重要方向。本文提出的利用生成模型创造辅助视觉信息以弥补文本偏差的思路，可以启发化学信息学领域的研究，例如，如何利用生成模型为分子描述或谱图数据生成辅助的结构可视化，以增强模型对分子空间结构和谱图特征的理解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

</details>

---

### 19. [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)

**基本信息**

- 🔗 arXiv: [`2603.05044`](https://arxiv.org/abs/2603.05044)
- 👥 作者: Sicheng Fan, Qingyun Shi, Shengze Xu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05044.pdf)

**💡 相关性分析**

满足标准1：论文提出了一套系统性的框架，用于将大模型的潜在知识转化为可执行特定领域任务的智能体。这套方法论对于开发能够在化学信息学平台或质谱分析软件中自主工作的AI助手（即化学领域的行动型大模型应用）具有直接的指导意义。

**📖 中文摘要**

本文提出了WebFactory，一个用于图形用户界面（GUI）智能体的全自动闭环强化学习训练框架。该框架旨在将大型语言模型中编码的互联网知识“压缩”为高效、可落地的智能体行为，其核心是通过可扩展的环境合成、知识感知的任务生成、LLM驱动的轨迹收集、分解奖励的RL训练和系统化评估来实现数据高效和泛化性强的智能体训练。这项工作属于具身智能和智能体领域。虽然应用场景是GUI操作，但其方法论——如何系统地将大模型的潜在知识转化为在特定领域（如化学信息学平台、质谱数据分析软件）中执行复杂任务（如文献检索、数据提取、结构解析）的自主智能体——对于构建化学领域的AI助手或自动化研究工具具有重要的参考价值。这可以看作是构建面向化学领域的、具有行动能力的“化学大模型”智能体的前期探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

</details>

---

### 20. [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046)

**基本信息**

- 🔗 arXiv: [`2603.05046`](https://arxiv.org/abs/2603.05046)
- 👥 作者: Rongzhi Li, Hitomi Yanaka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05046.pdf)

**💡 相关性分析**

满足标准1：论文专注于利用混合专家（MoE）架构和神经元分析来高效扩展大模型能力。这种架构优化方法对于构建能够处理化学多模态数据（包括质谱）和多重任务的“化学大模型”具有核心的参考价值。

**📖 中文摘要**

本文提出了NeuronMoE方法，用于高效地将大语言模型扩展到低资源语言。该方法通过分析跨语言神经元特异性，来指导混合专家（MoE）模型中每层专家的分配，从而在减少约40%参数量的同时保持性能。这项工作属于大模型架构优化与多语言扩展领域。对于“化学大模型”而言，其面临的挑战之一是如何高效地整合来自不同子领域（如有机化学、药物化学、分析化学）或不同数据类型（如SMILES、分子图、质谱、核磁谱）的知识。MoE架构是解决这一挑战的潜在方案。本文提出的基于神经元分析进行专家分配的方法，为未来设计面向化学多任务、多数据类型的MoE大模型提供了重要的技术思路和优化路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We propose $\textbf{NeuronMoE}$, a method that analyzes language-specific neurons across all transformer components to guide expert allocation per layer based on empirically measured cross-lingual neuron diversity. Applied to Llama-3.2-3B for low-resource languages (Greek, Turkish, and Hungarian), this approach achieves approximately 40% average parameter reduction while matching the performance of the LayerMoE baseline. We find that low-resource language experts independently develop neuron specialization patterns mirroring the high-resource language, which are concentrated in early and late layers. This reveals potential universal architectural principles in how multilingual models organize linguistic knowledge.

</details>

---

### 21. [Cyber Threat Intelligence for Artificial Intelligence Systems](https://arxiv.org/abs/2603.05068)

**基本信息**

- 🔗 arXiv: [`2603.05068`](https://arxiv.org/abs/2603.05068)
- 👥 作者: Natalia Krawczyk, Mateusz Szczepkowski, Adrian Brodzik 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05068.pdf)

**💡 相关性分析**

满足标准1：论文系统性地研究了AI系统（包括大模型）面临的安全威胁及相应的威胁情报框架。确保“化学大模型”及其应用（如质谱推理系统）的安全、可靠、可信，是其在科研和工业界成功部署的前提，因此该研究主题与化学信息学AI系统的实际落地直接相关。

**📖 中文摘要**

本文探讨了随着人工智能系统在关键服务中的深度嵌入，其面临传统网络安全防御未涵盖的新型威胁。论文研究了网络威胁情报（CTI）应如何演进以应对针对AI系统的攻击。作者分析了AI特定资产和漏洞，回顾并组织了当前AI安全知识体系，并概述了AI威胁情报知识库应包含的内容，包括针对AI供应链不同阶段和产物的具体入侵指标（IoC）。这项工作属于AI安全与治理领域。对于“化学大模型”和基于AI的“质谱结构推理”系统而言，其安全性、可靠性和抗攻击能力至关重要，尤其是在涉及药物设计或安全评估等高风险场景。本文系统地梳理了AI系统面临的安全威胁和防御思路，为未来部署化学领域的大模型系统提供了必不可少的安全框架和风险考量视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) becomes deeply embedded in critical services and everyday products, it is increasingly exposed to security threats which traditional cyber defenses were not designed to handle. In this paper, we investigate how cyber threat intelligence (CTI) may evolve to address attacks that target AI systems. We first analyze the assumptions and workflows of conventional threat intelligence with the needs of AI-focused defense, highlighting AI-specific assets and vulnerabilities. We then review and organize the current landscape of AI security knowledge. Based on this, we outline what an AI-oriented threat intelligence knowledge base should contain, describing concrete indicators of compromise (IoC) for different AI supply-chain phases and artifacts, and showing how such a knowledge base could support security tools. Finally, we discuss techniques for measuring similarity between collected indicators and newly observed AI artifacts. The review reveals gaps and quality issues in existing resources and identifies potential future research directions toward a practical threat intelligence framework tailored to AI.

</details>

---

### 22. [TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling](https://arxiv.org/abs/2603.05094)

**基本信息**

- 🔗 arXiv: [`2603.05094`](https://arxiv.org/abs/2603.05094)
- 👥 作者: Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05094.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出了一个构建高质量、特定领域（方言音频）指令数据集的系统化流程和最终的数据集资源。这为化学信息学领域构建用于训练“化学大模型”和“质谱结构推理模型”的指令数据集提供了宝贵的方法论范例和可借鉴的实践框架。

**📖 中文摘要**

本文发布了TW-Sound580K，一个通过验证-生成-评判（VGC）协议构建的台湾地区音频-文本指令数据集，旨在解决大型音频-语言模型（LALM）在处理地方方言韵律时因缺乏专业语料而表现不佳的问题。该数据集包含58万条高质量指令对，并用于微调了一个名为Tai-LALM的模型，该模型采用了动态双ASR仲裁策略以优化推理时的转录选择。这项工作属于领域/区域特定大语言模型的数据集构建与模型优化范畴。虽然聚焦于方言音频，但其核心贡献——通过严谨的流程（双ASR验证、教师模型扩展）构建高质量、特定领域的指令数据集——对于化学信息学领域具有极强的借鉴意义。要训练一个优秀的“化学大模型”或“质谱结构推理模型”，同样需要大规模、高质量、针对化学任务（如“根据质谱图推断分子结构”、“解释这个反应机理”）的指令微调数据。本文的数据集构建方法论可直接迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio-Language Models (LALMs) typically struggle with localized dialectal prosody due to the scarcity of specialized corpora. We present TW-Sound580K, a Taiwanese audio-text instruction dataset developed through a Verify-Generate-Critique (VGC) protocol. This pipeline leverages Dual-ASR validation to filter 522K raw clips, subsequently expanding them into 580,000 high-fidelity instruction pairs using a teacher model. The dataset's utility is demonstrated through Tai-LALM, which fine-tunes a DeSTA 2.5-Audio-initialized backbone and incorporates a dynamic Dual-ASR Arbitration strategy to optimize transcription selection during inference. On the TAU Benchmark, Tai-LALM reaches 49.1% accuracy, marking a 6.5% absolute improvement over the zero-shot baseline (42.6% with ASR text conditioning). This confirms that integrating regional corpora with rigorous curation and dynamic arbitration significantly enhances LALM performance on localized speech.

</details>

---

### 23. [Diff-ES: Stage-wise Structural Diffusion Pruning via Evolutionary Search](https://arxiv.org/abs/2603.05105)

**基本信息**

- 🔗 arXiv: [`2603.05105`](https://arxiv.org/abs/2603.05105)
- 👥 作者: Zongfang Liu, Shengkun Tang, Zongliang Wu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05105.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通用的、基于进化搜索的扩散模型分阶段结构化剪枝框架。该模型压缩与加速技术可直接应用于未来可能基于扩散模型架构构建的“化学大模型”（如分子生成模型），以提升其部署效率。

**📖 中文摘要**

本文提出了Diff-ES，一种通过进化搜索进行分阶段结构化剪枝的扩散模型高效化框架。该框架旨在优化扩散模型中不同去噪阶段的结构化稀疏度规划，并通过内存高效的权重路由执行，而无需复制模型参数。Diff-ES解决了现有方法依赖启发式稀疏度规划、导致次优性能的问题。这项工作属于大模型（特别是扩散模型）的压缩与加速领域。虽然应用对象是图像生成扩散模型，但其核心方法——通过自动化搜索找到模型不同部分（对应于扩散过程的不同阶段）的最优剪枝策略——具有通用性。未来，如果“化学大模型”（特别是用于分子生成或谱图生成的扩散模型）需要部署在资源受限的环境或追求更高的推理效率，这种基于进化搜索的分阶段剪枝技术将是一种直接可用的模型压缩和加速解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have achieved remarkable success in high-fidelity image generation but remain computationally demanding due to their multi-step denoising process and large model sizes. Although prior work improves efficiency either by reducing sampling steps or by compressing model parameters, existing structured pruning approaches still struggle to balance real acceleration and image quality preservation. In particular, prior methods such as MosaicDiff rely on heuristic, manually tuned stage-wise sparsity schedules and stitch multiple independently pruned models during inference, which increases memory overhead. However, the importance of diffusion steps is highly non-uniform and model-dependent. As a result, schedules derived from simple heuristics or empirical observations often fail to generalize and may lead to suboptimal performance. To this end, we introduce \textbf{Diff-ES}, a stage-wise structural \textbf{Diff}usion pruning framework via \textbf{E}volutionary \textbf{S}earch, which optimizes the stage-wise sparsity schedule and executes it through memory-efficient weight routing without model duplication. Diff-ES divides the diffusion trajectory into multiple stages, automatically discovers an optimal stage-wise sparsity schedule via evolutionary search, and activates stage-conditioned weights dynamically without duplicating model parameters. Our framework naturally integrates with existing structured pruning methods for diffusion models including depth and width pruning. Extensive experiments on DiT and SDXL demonstrate that Diff-ES consistently achieves wall-clock speedups while incurring minimal degradation in generation quality, establishing state-of-the-art performance for structured diffusion model pruning.

</details>

---

### 24. [Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning](https://arxiv.org/abs/2603.05120)

**基本信息**

- 🔗 arXiv: [`2603.05120`](https://arxiv.org/abs/2603.05120)
- 👥 作者: Boren Hu, Xiao Liu, Boci Peng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05120.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通过双向课程生成来提升大模型训练数据效率的多智能体框架。这种动态、自适应的数据生成与课程学习策略，对于需要高效学习复杂化学知识与推理模式的“化学大模型”训练具有直接的方法论启示。

**📖 中文摘要**

本文针对大语言模型数学推理训练中的数据效率瓶颈，提出了双向课程生成框架。该框架采用多智能体模拟自适应教学，形成一个包含“复杂化”和“简化”问题的闭环反馈数据生成机制。当模型存在基础推理缺陷时，框架会生成简化问题来进行“修复”，从而最大化每个训练样本的教学价值。这项工作属于大模型高效训练与课程学习领域。其核心思想——动态生成适配模型当前能力的最有效训练数据——对于训练“化学大模型”进行复杂的化学推理（如逆合成分析、反应机理推导、质谱解析）具有极高的参考价值。化学推理任务同样具有层次性，且模型在不同阶段会犯不同类型的错误，本文的框架为如何自动化地生成针对性训练数据以高效提升模型化学推理能力提供了新颖的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enhancing mathematical reasoning in Large Language Models typically demands massive datasets, yet data efficiency remains a critical bottleneck. While Curriculum Learning attempts to structure this process, standard unidirectional approaches (simple-to-complex) suffer from inefficient sample utilization: they blindly escalate complexity even when foundational gaps persist, leading to wasted computation on unsolvable problems. To maximize the instructional value of every training sample, we introduce a novel Bidirectional Curriculum Generation framework. Unlike rigid trajectories, our multi-agent ecosystem mimics adaptive pedagogy to establish a closed feedback loop. It dynamically generates data by either complicating problems to challenge the model or, crucially, simplying them to repair specific reasoning failures. This mechanism ensures that the model consumes only the most effective data at any given stage. Grounded in the Optimal Pacing Theorem, our approach optimizes the learning trajectory, significantly outperforming baselines while achieving superior reasoning performance with substantially fewer instruction samples.

</details>

---

### 25. [Measuring the Redundancy of Decoder Layers in SpeechLLMs](https://arxiv.org/abs/2603.05121)

**基本信息**

- 🔗 arXiv: [`2603.05121`](https://arxiv.org/abs/2603.05121)
- 👥 作者: Adel Moumen, Guangzhi Sun, Philip C Woodland
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05121.pdf)

**💡 相关性分析**

满足标准1：论文通过实证研究揭示了语音大语言模型中LLM解码器部分的冗余特性及跨任务一致性。这一发现对于理解并优化类似架构的“化学大模型”（编码器-解码器）的效率具有直接参考价值，为模型剪枝和轻量化提供了重要见解。

**📖 中文摘要**

本文研究了语音大语言模型中解码器层的冗余性。研究发现，对于语音任务，解码器的冗余模式很大程度上继承了其预训练语言模型基座（文本输入与语音输入导致相似的冗余块）。通过剪枝解码器层和分析剪枝后的“愈合”效应，作者表明大规模模型（7-8B）在仅保留60%解码器层时仍能保持良好的自动语音识别性能，并且这种冗余模式在不同语音编码器、任务和语言间具有普遍性。这项工作属于大模型架构分析与高效化领域。对于“化学大模型”而言，其通常也采用“编码器（处理分子/谱图数据）+ 大语言模型解码器”的架构。本文的发现提示我们，化学大模型中的LLM解码器部分也可能存在类似的冗余性，对其进行剪枝或结构优化是降低模型部署成本、提升推理速度的可行途径。这为化学大模型的轻量化部署提供了实证依据和技术方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech Large Language Models route speech encoder representations into an LLM decoder that typically accounts for over 90% of total parameters. We study how much of this decoder capacity is actually needed for speech tasks. Across two LLM families and three scales (1-8B), we show that decoder redundancy is largely inherited from the pretrained LLM: text and speech inputs yield similar redundant blocks. We then measure excess capacity by pruning decoder layers and analysing post-pruning healing to increase robustness. Our findings show that 7-8B models retain good ASR performance with only 60% of decoder layers, and the same trend extends to smaller scales with reduced pruning tolerance. We then generalise to speech translation, and show that the same blocks of layers are redundant across speech encoders, tasks and languages, indicating that a more global redundancy structure exists, enabling a single pruned and multi-tasks SpeechLLM backbone to be deployed.

</details>

---

### 26. [Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs](https://arxiv.org/abs/2603.05343)

**基本信息**

- 🔗 arXiv: [`2603.05343`](https://arxiv.org/abs/2603.05343)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕用于分子模拟的等变图神经网络（一种化学模型）的压缩和加速，直接与“化学大模型”主题相关。

**📖 中文摘要**

本文提出了一种几何感知量化（GAQ）框架，用于压缩和加速等变图神经网络（GNNs），同时严格保持离散空间中的连续对称性。该研究针对分子模拟中的SO(3)-等变GNNs，解决了高计算成本和内存瓶颈问题。通过引入幅度-方向解耦量化（MDDQ）方案、对称感知训练策略和鲁棒的注意力归一化机制，该框架在保持几何保真度的同时，显著降低了模型的内存占用并提升了推理速度。实验在rMD17基准测试上进行，证明了该方法在分子动力学模拟中的有效性。这项工作直接与“化学大模型”主题相关，因为它专注于用于分子模拟的等变图神经网络（一种特定类型的化学模型）的高效实现和压缩。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

</details>

---

### 27. [On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395)

**基本信息**

- 🔗 arXiv: [`2603.05395`](https://arxiv.org/abs/2603.05395)
- 👥 作者: Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05395.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕层神经网络（SNNs），这是图神经网络的一种，在化学信息学中常用于分子图表示学习，因此与“化学大模型”主题间接但合理地相关。

**📖 中文摘要**

本文研究了层神经网络（SNNs）作为一种解决异配图上过度平滑问题的图卷积网络扩展。论文通过引入一个恒等层网络基线，对学习限制映射的必要性进行了实证分析。研究在五个流行的异配图基准上进行了测试，并引入了瑞利商作为衡量过度平滑的归一化指标。虽然论文主要关注图神经网络架构，但其核心研究对象（层神经网络）最初是为了处理图结构数据（包括分子图）而提出的，并在化学信息学等领域有潜在应用。论文对层学习架构的消融研究为图神经网络在复杂数据（如分子图）上的设计提供了见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

</details>

---

### 28. [CogGen: Cognitive-Load-Informed Fully Unsupervised Deep Generative Modeling for Compressively Sampled MRI Reconstruction](https://arxiv.org/abs/2603.04438)

**基本信息**

- 🔗 arXiv: [`2603.04438`](https://arxiv.org/abs/2603.04438)
- 👥 作者: Qingyong Zhu, Yumin Tan, Xiang Gu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04438.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种新的全无监督深度生成建模框架（CogGen），虽然应用于医学成像，但其方法论（处理逆问题、课程学习、生成模型）与构建和训练复杂数据驱动模型（“大模型”的一种形式）的核心挑战相关。

**📖 中文摘要**

本文提出了CogGen，一种认知负载感知的全无监督深度生成模型，用于压缩采样磁共振成像重建。当训练数据或计算资源有限时，这种完全无监督的深度生成建模方法具有前景。CogGen将CS-MRI重构视为分阶段反演，并通过逐步调度内在难度和外部干扰来调节任务侧的“认知负载”。该方法用从易到难的k空间加权/选择策略取代了统一的数据拟合。虽然应用领域是医学成像，但论文提出的“完全无监督深度生成建模”框架、课程学习策略以及处理逆问题的思路，在方法论层面上与构建和训练复杂模型（可被视为“大模型”在特定领域的应用）相关。其核心贡献是一种新的模型训练范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fully unsupervised deep generative modeling (FU-DGM) is promising for compressively sampled MRI (CS-MRI) when training data or compute are limited. Classical FU-DGMs such as DIP and INR rely on architectural priors, but the ill-conditioned inverse problem often demands many iterations and easily overfits measurement noise. We propose CogGen, a cognitive-load-informed FU-DGM that casts CS-MRI as staged inversion and regulates task-side "cognitive load" by progressively scheduling intrinsic difficulty and extraneous interference. CogGen replaces uniform data fitting with an easy-to-hard k-space weighting/selection strategy: early iterations emphasize low-frequency, high-SNR, structure-dominant samples, while higher-frequency or noise-dominated measurements are introduced later. We realize this schedule via self-paced curriculum learning with complementary student-mode (what the model can currently learn) and teacher-mode (what it should follow) criteria, supporting both soft weighting and hard selection. Experiments and analysis show that CogGen-DIP and CogGen-INR improve fidelity and convergence over strong unsupervised baselines and competitive supervised pipelines.

</details>

---

### 29. [AbAffinity: A Large Language Model for Predicting Antibody Binding Affinity against SARS-CoV-2](https://arxiv.org/abs/2603.04480)

**基本信息**

- 🔗 arXiv: [`2603.04480`](https://arxiv.org/abs/2603.04480)
- 👥 作者: Faisal Bin Ashraf, Animesh Ray, Stefano Lonardi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04480.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于预测抗体结合亲和力的大型语言模型（AbAffinity），这直接属于“化学大模型”在药物发现和生物分子信息学领域的应用。

**📖 中文摘要**

本研究介绍了AbAffinity，一种新的大型语言模型，用于准确预测抗体与目标肽（例如SARS-CoV-2刺突蛋白）的结合亲和力。基于人工智能的抗体设计因其在对抗传染病方面的潜力而成为一种新兴方法。该模型利用实验抗体数据（特别是与COVID-19相关的数据）的指数级增长进行训练。抗体结合亲和力是设计中和抗体的最关键特性之一。这项工作展示了将大型语言模型应用于生物分子特性预测，特别是抗体-抗原相互作用这一化学信息学和生物信息学的核心问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning-based antibody design is emerging as one of the most promising approaches to combat infectious diseases, due to significant advancements in the field of artificial intelligence and an exponential surge in experimental antibody data (in particular related to COVID-19). The ability of an antibody to bind to an antigens (called binding affinity) is one of the the most critical properties in designing neutralizing antibodies. In this study we introduce Ab-Affinity, a new large language model that can accurately predict the binding affinity of antibodies against a target peptide, e.g., the SARS-CoV-2 spike protein. Code and model are available at this https URL .

</details>

---

### 30. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2603.04523)

**基本信息**

- 🔗 arXiv: [`2603.04523`](https://arxiv.org/abs/2603.04523)
- 👥 作者: Austin Rodriguez, Justin S. Smith, Sakib Matin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04523.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进机器学习原子间势（MLIPs）的训练，这是计算化学和化学信息学中“化学大模型”的关键组成部分。提出的PHL框架旨在提升这类模型的训练效率和精度。

**📖 中文摘要**

本文介绍了投影Hessian学习（PHL），一个可扩展的二阶训练框架，用于机器学习原子间势。Hessian矩阵编码了势能面比能量和力更丰富的局部曲率信息，但使用完整Hessian矩阵训练MLIPs通常不切实际。PHL通过仅使用Hessian-向量积来注入曲率信息，避免了构建和存储Hessian矩阵的二次方开销。该方法在基于omegaB97XD/6-31G(d)计算的化学反应物、产物、过渡态等多样化化学数据集上进行了基准测试。PHL用力-复杂度曲率训练取代了显式的Hessian监督，在保持大部分二阶精度增益的同时，能够扩展到更大、更复杂的分子系统。这项工作直接针对化学模拟中机器学习势函数的训练改进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hessian matrix (second derivatives) encodes far richer local curvature of the potential energy surface than energies and forces alone. However, training machine-learning interatomic potentials (MLIPs) with full Hessians is often impractical because explicitly forming and storing Hessian matrices scales quadratically in cost and memory. We introduce Projected Hessian Learning (PHL), a scalable second-order training framework that injects curvature information using only Hessian-vector products (HVPs). Rather than constructing the Hessian, PHL projects curvature along stochastic probe directions and uses an unbiased stochastic trace-based loss with favorable system-size scaling, enabling curvature-informed training without quadratic memory growth. We benchmark PHL on a chemically diverse dataset of reactants, products, transition states, intrinsic reaction coordinates, and normal-mode sampled geometries computed at omegaB97XD/6-31G(d). We compare energy-force training (E-F), two HVP-based schemes (E-F-HVP with one-hot or randomized probes), and full energy-force-Hessian training (E-F-H). With randomized probes per minibatch, both HVP schemes match full-Hessian training in energy, force, and Hessian accuracy while delivering >24x epoch speedups for the small molecular systems studied. In a fixed-probe regime with one HVP per molecule, randomized projections consistently outperform one-column probing, especially for far-from-equilibrium geometries. Overall, PHL replaces explicit Hessian supervision with force-complexity curvature training, retaining most second-order accuracy gains while scaling to larger, more complex molecular systems.

</details>

---

### 31. [A Fast Generative Framework for High-dimensional Posterior Sampling: Application to CMB Delensing](https://arxiv.org/abs/2603.04535)

**基本信息**

- 🔗 arXiv: [`2603.04535`](https://arxiv.org/abs/2603.04535)
- 👥 作者: Hadi Sotoudeh, Pablo Lemos, Laurence Perreault-Levasseur
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04535.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个用于高维贝叶斯推断的深度生成框架，专注于高效后验采样。虽然应用在天体物理，但其核心是生成模型的方法论创新，与“大模型”中的生成模型主题相关。

**📖 中文摘要**

本文介绍了一个用于高维贝叶斯推断的深度生成框架，能够实现高效的后验采样。随着望远镜和模拟快速扩展天体物理数据的体积和分辨率，越来越需要快速的基于模拟的推断方法来提取科学见解。虽然基于扩散的方法提供了高质量的生成能力，但采样速度慢。该方法执行后验采样的速度比扩散基线快一个数量级。应用于CMB去透镜问题，它成功地从模拟观测中恢复了未透镜的CMB功率谱。该模型在宇宙学参数变化下也保持稳健。虽然应用领域是天体物理学，但论文的核心贡献是一个通用的、用于高维贝叶斯推断的深度生成框架，其方法论（生成模型、后验采样、加速推理）与构建和部署复杂生成模型（“大模型”的一种）密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a deep generative framework for high-dimensional Bayesian inference that enables efficient posterior sampling. As telescopes and simulations rapidly expand the volume and resolution of astrophysical data, fast simulation-based inference methods are increasingly needed to extract scientific insights. While diffusion-based approaches offer high-quality generative capabilities, they are hindered by slow sampling speeds. Our method performs posterior sampling an order of magnitude faster than a diffusion baseline. Applied to the problem of CMB delensing, it successfully recovers the unlensed CMB power spectrum from simulated observations. The model also remains robust to shifts in cosmological parameters, demonstrating its potential for out-of-distribution generalization and application to observational cosmological data.

</details>

---

### 32. [Transversal AND in Quantum Codes](https://arxiv.org/abs/2603.04548)

**基本信息**

- 🔗 arXiv: [`2603.04548`](https://arxiv.org/abs/2603.04548)
- 👥 作者: Christine Li, Lia Yeh
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04548.pdf)

**💡 相关性分析**

满足标准1：论文研究量子纠错码中逻辑门的 transversal 实现，这是构建大规模、容错量子计算机（可运行复杂量子算法或“量子模型”）的基础组件，与广义的“大模型”硬件基础相关。

**📖 中文摘要**

本文研究了量子码中的 transversal AND 门。AND 门在量子比特上是不可逆的，但在量子三态上是可逆的，使其成为用量子三态高效模拟量子比特计算的基础模块。论文的主要成果是构建了一个新颖的量子三态 [[6,2,2]] 量子纠错码，该码具有 transversal AND 门的实现。关键见解是将给定酉算子的对称 T-depth one 电路分解解释为 CSS 码。通过用额外的稳定子增广码电路可以增加码距，同时保留逻辑门。这项工作展示了如何为特定逻辑门（如AND）设计具有 transversal 实现的量子纠错码。虽然主要属于量子计算领域，但其关于在纠错码中实现特定逻辑操作的设计，与构建鲁棒的量子计算系统（可视为量子“大模型”或量子算法的硬件基础）相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The AND gate is not reversible$\unicode{x2014}$on qubits. However, it is reversible on qutrits, making it a building block for efficient simulation of qubit computation using qutrits. We first observe that there are multiple two-qutrit Clifford+T unitaries that realize the AND gate with T-count 3, and its generalizations to $n$ qubits with T-count $3n-3$. Our main result is the construction of a novel qutrit $\mathopen{[\![} 6,2,2 \mathclose{]\!]}$ quantum error-correcting code with a transversal implementation of the AND gate. The key insight in our approach is that a symmetric T-depth one circuit decomposition$\unicode{x2014}$composed of a CX circuit, T and T dagger gates, followed by the CX circuit in reverse$\unicode{x2014}$of a given unitary can be interpreted as a CSS code. We can increase the code distance by augmenting the code circuit with additional stabilizers while preserving the logical gate. This results in a code with a "built-in" transversal implementation of the original unitary, which can be further concatenated to attain a $\mathopen{[\![} 48,2,4 \mathclose{]\!]}$ code with the same transversal logical gate. Furthermore, we present several protocols for mixed qubit-qutrit codes which we call Qubit Subspace Codes, and for magic state distillation and injection.

</details>

---

### 33. [Estimation of Persistence Diagrams via the Three Gap Theorem](https://arxiv.org/abs/2603.04570)

**基本信息**

- 🔗 arXiv: [`2603.04570`](https://arxiv.org/abs/2603.04570)
- 👥 作者: Luis Suarez Salas, Jose A. Perea
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04570.pdf)

**💡 相关性分析**

满足标准1：论文提出了基于拓扑数据分析（TDA）和持久同调的新计算方法。TDA和持久同调是化学信息学中用于分析分子结构、构象空间和材料科学数据的重要工具，因此该方法论研究与化学信息学主题相关。

**📖 中文摘要**

本文提出了利用三间隙定理和持久同调来近似准周期函数滑动窗口嵌入的持久性图的理论和计算方案。时间延迟（或滑动窗口）嵌入是一种从时间序列数据重建吸引子的动力系统技术。最近，拓扑数据分析中的描述符——特别是持久性图——已被用于测量重建吸引子的形状。本文结合数论中的三间隙定理和TDA中的持久Künneth公式，推导出快速且可证明正确的持久同调近似。该过程的输入是信号的频谱，提供了捕获环形吸引子形状的理论和数值证据。虽然应用是通用的时间序列分析，但持久同调和拓扑数据分析是化学信息学中用于分析分子构象空间、材料结构等的强大工具。该方法为从复杂数据（如分子动力学轨迹）中提取拓扑特征提供了新的计算视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The time delay (or Sliding Window) embedding is a technique from dynamical systems to reconstruct attractors from time series data. Recently, descriptors from Topological Data Analysis (TDA) -- specifically, persistence diagrams -- have been used to measure the shape of said reconstructed attractors in applications including periodicity and quasiperiodicity quantification. Despite their utility, the fast computation of persistence diagrams of sliding window embeddings is still poorly understood. In this work, we present theoretical and computational schemes to approximate the persistence diagrams of sliding window embeddings from quasiperiodic functions. We do so by combining the Three Gap Theorem from number theory with the Persistent Künneth formula from TDA, and derive fast and provably correct persistent homology approximations. The input to our procedure is the spectrum of the signal, and we provide numerical as well as theoretical evidence of its utility to capture the shape of toroidal attractors.

</details>

---

### 34. [Particle-Guided Diffusion for Gas-Phase Reaction Kinetics](https://arxiv.org/abs/2603.05139)

**基本信息**

- 🔗 arXiv: [`2603.05139`](https://arxiv.org/abs/2603.05139)
- 👥 作者: Andrew Millard, Henrik Pedersen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用扩散模型（一种生成式大模型）来解决化学动力学问题，与'化学大模型'这一主题直接相关。

**📖 中文摘要**

该论文提出了一种基于扩散模型的粒子引导采样方法，用于解决气相化学反应动力学问题。该方法在变化的参数条件下，对平流-反应-扩散（ARD）方程的解进行训练，以生成物理一致的浓度场并准确预测出口浓度。这项工作展示了扩散模型在反应输运系统中进行推断的潜力，属于利用生成模型（扩散模型）解决化学物理问题的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

</details>

---

### 35. [Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks](https://arxiv.org/abs/2603.05188)

**基本信息**

- 🔗 arXiv: [`2603.05188`](https://arxiv.org/abs/2603.05188)
- 👥 作者: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05188.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发和应用大型语言模型（LLM）智能体来解决化学材料（共价有机框架）的逆向设计问题，直接围绕'化学大模型'这一主题。

**📖 中文摘要**

本文介绍了一个名为Ara的大型语言模型（LLM）智能体，用于通过逆向设计寻找同时满足带隙、带边和水解稳定性标准的耐用光催化共价有机框架（COFs）。该智能体利用预训练的化学知识、给体-受体理论、共轭效应和连接键稳定性层次结构来指导搜索。在由各种节点、连接体、连接键和R基团组成的候选空间中，Ara的命中率显著高于随机搜索和贝叶斯优化。这项工作展示了LLM化学先验知识在加速多标准材料发现方面的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

</details>

---

### 36. [Generative Models in Decision Making: A Survey](https://arxiv.org/abs/2502.17100)

**基本信息**

- 🔗 arXiv: [`2502.17100`](https://arxiv.org/abs/2502.17100)
- 👥 作者: Xinyu Shao, Jianping Zhang, Haozhi Wang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.17100.pdf)

**💡 相关性分析**

满足标准3：这是一篇专门针对生成模型（Generative Models）在决策制定中应用的综述论文，其中讨论的生成模型（如扩散模型）与'化学大模型'主题相关，提供了重要的相关讨论和展望。

**📖 中文摘要**

这篇综述论文系统性地探讨了生成模型在决策制定中的应用。它提出了一个基于“控制即推理”概率框架的原则性分类法，将生成式决策制定分解为控制器、建模器、优化器和评估器四个功能角色。文章批判性地分析了代表性的生成模型家族，并考察了它们在具体领域（如具身AI、自动驾驶、AI for Science）的部署。该综述为理解生成模型（包括扩散模型、世界模型等）如何重塑决策制定范式提供了全面的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching. This paradigm shift addresses intrinsic limitations in classical Reinforcement Learning (RL), particularly the limited expressivity of standard unimodal policy distributions in capturing complex, multi-modal behaviors embedded in diverse datasets. However, current literature often treats these models as isolated algorithmic improvements, rarely synthesizing them into a single comprehensive framework. This survey proposes a principled taxonomy grounding generative decision-making within the probabilistic framework of Control as Inference. By performing a variational factorization of the trajectory posterior, we conceptualize four distinct functional roles: Controllers for amortized policy inference, Modelers for dynamics priors, Optimizers for iterative trajectory refinement, and Evaluators for trajectory guidance and value assessment. Unlike existing architecture-centric reviews, this function-centric framework allows us to critically analyze representative generative families across distinct dimensions. Furthermore, we examine deployment in high-stakes domains, specifically Embodied AI, Autonomous Driving, and AI for Science, highlighting systemic risks such as dynamics hallucination in world models and proxy exploitation. Finally, we chart the path toward Generalist Physical Intelligence, identifying pivotal challenges in inference efficiency, trustworthiness, and the emergence of Physical Foundation Models.

</details>

---

### 37. [GIT-BO: High-Dimensional Bayesian Optimization with Tabular Foundation Models](https://arxiv.org/abs/2505.20685)

**基本信息**

- 🔗 arXiv: [`2505.20685`](https://arxiv.org/abs/2505.20685)
- 👥 作者: Rosen Ting-Ying Yu, Cyril Picard, Faez Ahmed
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.20685.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合了表格基础模型（TabPFN v2，一种特定类型的机器学习大模型）的新型贝叶斯优化框架。虽然应用领域不限于化学，但其核心方法（利用基础模型进行优化）与'化学大模型'主题中利用大模型解决科学计算问题的方向相关。

**📖 中文摘要**

本文提出了GIT-BO，一个梯度信息引导的贝叶斯优化框架，用于解决高维优化问题。它结合了TabPFN v2（一种表格基础模型，可在上下文中进行零样本贝叶斯推断）和基于模型预测均值梯度计算的活动子空间机制。该方法将探索与内在低维子空间对齐，并通过UCB采集函数选择查询点，无需在线重新训练。文章在包括合成和真实世界任务（如电力系统）在内的多个高维基准上进行了评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian optimization (BO) struggles in high dimensions, where Gaussian-process surrogates demand heavy retraining and brittle assumptions, slowing progress on real engineering and design problems. We introduce GIT-BO, a Gradient-Informed BO framework that couples TabPFN v2, a tabular foundation model that performs zero-shot Bayesian inference in context, with an active-subspace mechanism computed from the model's own predictive-mean gradients. This aligns exploration to an intrinsic low-dimensional subspace via a Fisher-information estimate and selects queries with a UCB acquisition, requiring no online retraining. Across 60 problem variants spanning 20 benchmarks-nine scalable synthetic families and ten real-world tasks (e.g., power systems, Rover, MOPTA08, Mazda)-up to 500 dimensions, GIT-BO delivers a stronger performance-time trade-off than state-of-the-art GP-based methods (SAASBO, TuRBO, Vanilla BO, BAxUS), ranking highest in performance and with runtime advantages that grow with dimensionality. Limitations include memory footprint and dependence on the capacity of the underlying TFM.

</details>

---

### 38. [SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models](https://arxiv.org/abs/2506.01062)

**基本信息**

- 🔗 arXiv: [`2506.01062`](https://arxiv.org/abs/2506.01062)
- 👥 作者: Thinh Pham, Nguyen Nguyen, Pratibha Zunjare 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.01062.pdf)

**💡 相关性分析**

满足标准3：论文虽然不是专门针对化学信息学或质谱的综述，但它对搜索增强语言模型（一种特定的大模型应用范式）在复杂推理任务上的能力进行了深入的评估和讨论，提供了关于大模型当前局限性的重要见解，这与'化学大模型'主题中模型能力评估的相关讨论相符。

**📖 中文摘要**

本文介绍了SealQA，一个新的挑战性基准，用于评估搜索增强语言模型在事实寻求性问题上的表现，特别是当网络搜索结果存在冲突、噪声或无用时。该基准包含三个变体：Seal-0（主要）、Seal-Hard和LongSeal，分别评估事实准确性、推理能力和长上下文多文档推理。文章评估揭示了当前前沿LLM（如GPT-4.1, o3, o4-mini, DeepSeek-R1）在处理此类复杂推理任务时的关键局限性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce SealQA, a new challenge benchmark for evaluating SEarch-Augmented Language models on fact-seeking questions where web search yields conflicting, noisy, or unhelpful results. SealQA comes in three flavors: (1) Seal-0 (main) and (2) Seal-Hard, which assess factual accuracy and reasoning capabilities, with Seal-0 focusing on the most challenging questions where chat models (e.g., GPT-4.1) typically achieve near-zero accuracy; and (3) LongSeal, which extends SealQA to test long-context, multi-document reasoning in "needle-in-a-haystack" settings. Our evaluation reveals critical limitations in current models: Even frontier LLMs perform poorly across all SealQA flavors. On Seal-0, frontier agentic models equipped with tools like o3 and o4-mini achieve only 17.1% and 6.3% accuracy, respectively, at their best reasoning efforts. We find that advanced reasoning models such as DeepSeek-R1-671B and o3-mini are highly vulnerable to noisy search results. Notably, increasing test-time compute does not yield reliable gains across o3-mini, o4-mini, and o3, with performance often plateauing or even declining early. Additionally, while recent models are less affected by the "lost-in-the-middle" issue, they still fail to reliably identify relevant documents in LongSeal when faced with numerous distractors. To facilitate future work, we release SealQA at this http URL .

</details>

---

### 39. [HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals](https://arxiv.org/abs/2506.08618)

**基本信息**

- 🔗 arXiv: [`2506.08618`](https://arxiv.org/abs/2506.08618)
- 👥 作者: Xianquan Yan, Hakan Akgün, Kenji Kawaguchi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08618.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模、高质量的图结构数据集（HSG-12M）和自动化生成工具（Poly2Graph）。图神经网络是化学信息学中用于分子表示和性质预测的核心工具之一，该数据集和工具为开发新的、能够处理复杂几何关系的图学习方法提供了宝贵的资源，这些方法可潜在应用于分子图表示学习或质谱解析中的结构推理任务。

**📖 中文摘要**

本文介绍了HSG-12M，一个包含1160万个静态和510万个动态哈密顿谱图的大规模数据集。该数据集源自非厄米量子物理领域，其中晶体的能谱在复平面上形成复杂的几何结构（哈密顿谱图）。论文的核心贡献是提出了Poly2Graph，一个将一维晶体哈密顿量自动映射为谱图的高性能开源流程。HSG-12M是首个大规模空间多重图数据集，图中的边保留了节点之间在度量空间中的几何轨迹信息。该数据集旨在为数据驱动的科学发现（如凝聚态物理）奠定基础，并为几何感知的图学习提供新的机会。虽然论文主要关注物理系统，但其核心是构建和提供了一个大规模、高质量的图结构数据集，并探讨了图神经网络在处理此类复杂几何图数据时面临的挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming scientific research by revealing new ways to understand complex physical systems, but its impact remains constrained by the lack of large, high-quality domain-specific datasets. A rich, largely untapped resource lies in non-Hermitian quantum physics, where the energy spectra of crystals form intricate geometries on the complex plane -- termed as Hamiltonian spectral graphs. Despite their significance as fingerprints for electronic behavior, their systematic study has been intractable due to the reliance on manual extraction. To unlock this potential, we introduce Poly2Graph: a high-performance, open-source pipeline that automates the mapping of 1-D crystal Hamiltonians to spectral graphs. Using this tool, we present HSG-12M: a dataset containing 11.6 million static and 5.1 million dynamic Hamiltonian spectral graphs across 1401 characteristic-polynomial classes, distilled from 177 TB of spectral potential data. Crucially, HSG-12M is the first large-scale dataset of spatial multigraphs -- graphs embedded in a metric space where multiple geometrically distinct trajectories between two nodes are retained as separate edges. This simultaneously addresses a critical gap, as existing graph benchmarks overwhelmingly assume simple, non-spatial edges, discarding vital geometric information. Benchmarks with popular GNNs expose new challenges in learning spatial multi-edges at scale. Beyond its practical utility, we show that spectral graphs serve as universal topological fingerprints of polynomials, vectors, and matrices, forging a new algebra-to-graph link. HSG-12M lays the groundwork for data-driven scientific discovery in condensed matter physics, new opportunities in geometry-aware graph learning and beyond.

</details>

---

### 40. [Bures-Wasserstein Flow Matching for Graph Generation](https://arxiv.org/abs/2506.14020)

**基本信息**

- 🔗 arXiv: [`2506.14020`](https://arxiv.org/abs/2506.14020)
- 👥 作者: Keyue Jiang, Jiahao Cui, Xiaowen Dong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图生成模型，这是化学信息学中分子生成和设计的核心课题。BWFlow框架直接针对分子图生成任务进行了评估，其改进的概率路径构建方法旨在更好地捕捉分子结构的内部关联，这对于生成合理的化学结构至关重要。

**📖 中文摘要**

本文提出了BWFlow，一种用于图生成的流匹配框架。针对现有扩散或流模型在构建概率路径时对节点和边进行独立线性插值，从而破坏图结构互联模式的问题，BWFlow将图建模为由马尔可夫随机场参数化的连接系统，并利用马尔可夫随机场对象之间的最优传输位移来设计平滑的概率路径，确保图组件的协同演化。该框架在普通图生成和分子生成任务上进行了实验验证，展示了其竞争性能、更好的训练收敛性和高效采样。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation has emerged as a critical task in fields ranging from drug discovery to circuit design. Contemporary approaches, notably diffusion and flow-based models, have achieved solid graph generative performance through constructing a probability path that interpolates between reference and data distributions. However, these methods typically model the evolution of individual nodes and edges independently and use linear interpolations in the disjoint space of nodes/edges to build the path. This disentangled interpolation breaks the interconnected patterns of graphs, making the constructed probability path irregular and non-smooth, which causes poor training dynamics and faulty sampling convergence. To address the limitation, this paper first presents a theoretically grounded framework for probability path construction in graph generative models. Specifically, we model the joint evolution of the nodes and edges by representing graphs as connected systems parameterized by Markov random fields (MRF). We then leverage the optimal transport displacement between MRF objects to design a smooth probability path that ensures the co-evolution of graph components. Based on this, we introduce BWFlow, a flow-matching framework for graph generation that utilizes the derived optimal probability path to benefit the training and sampling algorithm design. Experimental evaluations in plain graph generation and molecule generation validate the effectiveness of BWFlow with competitive performance, better training convergence, and efficient sampling.

</details>

---

### 41. [Structured Kolmogorov-Arnold Neural ODEs for Interpretable Learning and Symbolic Discovery of Nonlinear Dynamics](https://arxiv.org/abs/2506.18339)

**基本信息**

- 🔗 arXiv: [`2506.18339`](https://arxiv.org/abs/2506.18339)
- 👥 作者: Wei Liu, Kiran Bacsa, Loon Ching Tang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.18339.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及使用神经网络（特别是KAN）进行动力学系统的符号回归和可解释建模。在化学信息学中，从实验数据（如反应动力学数据、光谱时间序列）中发现可解释的物理定律或数学模型是一个重要方向。KAN作为一种新兴的、具有符号回归潜力的网络架构，为“化学大模型”中融入可解释的物理规则提供了有前景的技术路径。

**📖 中文摘要**

本文提出了结构化Kolmogorov-Arnold神经ODE（SKANODEs），一个用于非线性动力学系统可解释学习和符号发现的框架。该框架将结构化状态空间建模与Kolmogorov-Arnold网络（KANs）相结合。在神经ODE架构中，SKANODE使用一个完全可训练的KAN作为通用函数逼近器来执行虚拟传感，恢复对应于可解释物理量（如位移和速度）的潜在状态。利用KAN的符号回归能力，SKANODE随后提取系统控制动力学的紧凑、可解释表达式。实验表明，该方法能够从测量数据中恢复有物理意义的潜在轨迹，并识别出正确的控制非线性（如Duffing振荡器中的立方刚度），同时产生所学非线性动力学的方程级描述。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding and modeling nonlinear dynamical systems is a fundamental challenge across science and engineering. Deep learning has shown remarkable potential for capturing complex system behavior, yet achieving models that are both accurate and physically interpretable remains difficult. To address this, we propose Structured Kolmogorov-Arnold Neural ODEs (SKANODEs), a framework that integrates structured state-space modeling with Kolmogorov-Arnold Networks (KANs). Within a Neural ODE architecture, SKANODE employs a fully trainable KAN as a universal function approximator to perform virtual sensing, recovering latent states that correspond to interpretable physical quantities such as displacements and velocities. Leveraging KAN's symbolic regression capability, SKANODE then extracts compact, interpretable expressions for the system's governing dynamics. Experiments on two canonical nonlinear oscillators and a real-world F-16 ground vibration dataset demonstrate that SKANODE reliably recovers physically meaningful latent displacement and velocity trajectories from acceleration measurements, identifies the correct governing nonlinearities--including the cubic stiffness in the Duffing oscillator and the nonlinear damping structure in the Van der Pol oscillator--and reveals hysteretic signatures in the F-16 interface dynamics through structured latent phase portraits and an interpretable symbolic model. Across all three cases, SKANODE provides more accurate and robust predictions than black-box NODE baselines and classical ARX and NARX identification, while producing equation-level descriptions of the learned nonlinear dynamics.

</details>

---

### 42. [Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models](https://arxiv.org/abs/2507.18534)

**基本信息**

- 🔗 arXiv: [`2507.18534`](https://arxiv.org/abs/2507.18534)
- 👥 作者: Xingyu Qiu, Mengying Yang, Xinghua Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.18534.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是扩散模型的统一设计框架，特别是针对任意噪声模式。扩散模型是当前生成式AI的前沿，也是构建“化学大模型”（如用于分子生成、反应预测）的关键技术之一。理解并优化扩散模型在不同噪声模式下的行为，对于将其有效应用于化学领域（如处理带有特定噪声的谱图数据、生成具有特定性质的分子）具有重要意义。

**📖 中文摘要**

本文提出了EDA（Elucidates the Design space of Arbitrary-noise diffusion models），旨在为处理不同噪声模式的扩散模型建立一个统一的理论框架。论文指出，现有的EDM框架依赖于固定高斯噪声，无法解释基于任意噪声的流方法，并且强制注入高斯噪声会对图像修复任务产生不利影响。EDA扩展了噪声模式的灵活性，同时保持了EDM的模块化特性，并严格证明了增加的噪声复杂性在修复过程中不会引入额外的计算开销。EDA在医学图像去噪（如MRI偏置场校正、CT金属伪影去除）和自然图像阴影去除等任务上进行了验证，展示了其强大的图像修复泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although EDM aims to unify the design space of diffusion models, its reliance on fixed Gaussian noise prevents it from explaining emerging flow-based methods that diffuse arbitrary noise. Moreover, our study reveals that EDM's forcible injection of Gaussian noise has adverse effects on image restoration task, as it corrupts the degraded images, overextends the restoration distance, and increases the task's complexity. To interpret diverse methods for handling distinct noise patterns within a unified theoretical framework and to minimize the restoration distance, we propose EDA, which Elucidates the Design space of Arbitrary-noise diffusion models. Theoretically, EDA expands noise pattern flexibility while preserving EDM's modularity, with rigorous proof that increased noise complexity introduces no additional computational overhead during restoration. EDA is validated on three representative medical image denoising and natural image restoration tasks: MRI bias field correction (global smooth noise), CT metal artifact removal (global sharp noise) and natural image shadow removal (local boundary-aware noise). With only 5 sampling steps, competitive results against specialized methods across medical and natural tasks demonstrate EDA's strong generalization capability for image restoration. Code is available at: this https URL .

</details>

---

### 43. [Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks](https://arxiv.org/abs/2509.19696)

**基本信息**

- 🔗 arXiv: [`2509.19696`](https://arxiv.org/abs/2509.19696)
- 👥 作者: Noah Geiger, Tamim Asfour, Neville Hogan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.19696.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散模型（一种重要的生成模型）来学习机器人的接触动力学和控制策略。扩散模型作为“化学大模型”中用于分子构象生成、轨迹预测等任务的核心组件，其在不同领域（如机器人学）的应用和优化思路（如条件生成、与物理模型的结合）可以为化学领域的模型设计提供借鉴和启发。

**📖 中文摘要**

本文提出了基于扩散的阻抗学习框架，用于接触丰富的机器人操作任务。该框架结合了生成建模与能量一致的阻抗控制。一个基于Transformer的扩散模型，通过交叉注意力以测量的外部力矩为条件，重建模拟的零力轨迹（sZFT），该轨迹代表了接触一致的平衡行为。重建的sZFT被一个基于能量的估计器用于通过方向刚度和阻尼调制在线调整阻抗。该方法在通过Apple Vision Pro遥操作收集的跑酷和机器人辅助治疗演示数据上进行训练，并在KUKA LBR iiwa机器人上实现了实时的扭矩控制，能够平滑地穿越障碍物。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning-based methods excel at robot motion generation but remain limited in contact-rich physical interaction. Impedance control provides stable and safe contact behavior but requires task-specific tuning of stiffness and damping parameters. We present Diffusion-Based Impedance Learning, a framework that bridges these paradigms by combining generative modeling with energy-consistent impedance control. A Transformer-based Diffusion Model, conditioned via cross-attention on measured external wrenches, reconstructs simulated Zero-Force Trajectories (sZFTs) that represent contact-consistent equilibrium behavior. A SLERP-based quaternion noise scheduler preserves geometric consistency for rotations on the unit sphere. The reconstructed sZFT is used by an energy-based estimator to adapt impedance online through directional stiffness and damping modulation. Trained on parkour and robot-assisted therapy demonstrations collected via Apple Vision Pro teleoperation, the model achieves sub-millimeter positional and sub-degree rotational accuracy using only tens of thousands of samples. Deployed in realtime torque control on a KUKA LBR iiwa, the approach enables smooth obstacle traversal and generalizes to unseen tasks, achieving 100% success in multi-geometry peg-in-hole insertion.

</details>

---

### 44. [Noise-to-Notes: Diffusion-based Generation and Refinement for Automatic Drum Transcription](https://arxiv.org/abs/2509.21739)

**基本信息**

- 🔗 arXiv: [`2509.21739`](https://arxiv.org/abs/2509.21739)
- 👥 作者: Michael Yeung, Keisuke Toyama, Toya Teramoto 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.21739.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将一个传统的判别式任务（音频事件检测）重新定义为基于扩散模型的生成式任务。这种范式转换展示了扩散模型在序列数据生成和解析方面的强大能力。“质谱结构推理”本质上是从质谱信号（一维或二维序列）生成或推断出分子结构（图或序列），这与从音频序列生成音符事件在任务形式上具有相似性。N2N框架中处理序列生成、条件控制以及利用预训练基础模型增强特征的方法，对设计用于质谱解析的生成模型具有参考价值。

**📖 中文摘要**

本文重新将自动鼓转录（ADT）定义为条件生成任务，并引入了Noise-to-Notes（N2N）框架。该框架利用扩散建模将音频条件化的高斯噪声转换为带有相关速度的鼓事件。这种生成式扩散方法具有灵活的速度-精度权衡和强大的修复能力。为了处理二值起始点和连续速度值的联合生成挑战，论文引入了退火伪Huber损失。此外，为了增强低层级谱图特征，论文提出整合从音乐基础模型（MFMs）中提取的特征，这些特征捕获了高层级语义信息并增强了对域外鼓音频的鲁棒性。实验结果表明，N2N在多个ADT基准测试中建立了新的最先进性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automatic drum transcription (ADT) is traditionally formulated as a discriminative task to predict drum events from audio spectrograms. In this work, we redefine ADT as a conditional generative task and introduce Noise-to-Notes (N2N), a framework leveraging diffusion modeling to transform audio-conditioned Gaussian noise into drum events with associated velocities. This generative diffusion approach offers distinct advantages, including a flexible speed-accuracy trade-off and strong inpainting capabilities. However, the generation of binary onset and continuous velocity values presents a challenge for diffusion models, and to overcome this, we introduce an Annealed Pseudo-Huber loss to facilitate effective joint optimization. Finally, to augment low-level spectrogram features, we propose incorporating features extracted from music foundation models (MFMs), which capture high-level semantic information and enhance robustness to out-of-domain drum audio. Experimental results demonstrate that including MFM features significantly improves robustness and N2N establishes a new state-of-the-art performance across multiple ADT benchmarks.

</details>

---

### 45. [BeyondBench: Contamination-Resistant Evaluation of Reasoning in Language Models](https://arxiv.org/abs/2509.24210)

**基本信息**

- 🔗 arXiv: [`2509.24210`](https://arxiv.org/abs/2509.24210)
- 👥 作者: Gaurav Srivastava, Aafiya Hussain, Zhenyu Bi 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24210.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新颖的、抗污染的基准测试框架（BeyondBench）和相应的数据集。在“化学大模型”和“质谱结构推理”的研究中，评估模型的真实推理能力而非记忆能力至关重要。BeyondBench的设计理念（通过算法生成无限且可验证的问题）为解决化学领域基准测试的污染问题（例如，模型可能记忆了训练集中的已知分子-性质对或谱图-结构对，而非真正学会推理）提供了重要的方法论参考。其构建大规模、高质量、可验证评估集的方法，可以直接启发化学信息学领域评估资源的创建。

**📖 中文摘要**

本文介绍了BeyondBench，一个使用算法问题生成来动态创建数学基础问题的评估框架，以确保每个测试都不受训练数据污染。该框架涵盖44个算法任务，包含117种变体，分为三个难度级别：简单套件（29个任务）涉及算术和统计，中等套件（5个任务，49种变体）涉及序列模式和推理，困难套件（10个任务，68种变体）涉及NP完全和约束满足问题。每个任务从一个超过10^15个独特实例的空间中抽取，并具有确定性验证的解决方案。论文评估了101个语言模型，揭示了随着复杂性增加，性能急剧下降的推理缺陷。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating language models fairly is increasingly difficult as static benchmarks risk contamination by training data, obscuring whether models truly reason or recall. We introduce BeyondBench, an evaluation framework using algorithmic problem generation to create mathematically grounded problems on the fly, ensuring each test remains uncontaminated. Our framework covers 44 algorithmic tasks with 117 variations across three difficulty levels: the Easy Suite (29 tasks) for arithmetic and statistics, the Medium Suite (5 tasks, 49 variations) for sequence patterns and reasoning, and the Hard Suite (10 tasks, 68 variations) for NP-complete and constraint satisfaction problems. Each task draws from a space exceeding 10^15 unique instances, with deterministically verified solutions. We evaluated 101 language models (85 open-source, 16 closed-source), spanning 0.5B to 141B parameters and multiple quantization schemes, using three-fold evaluation for robustness. Results reveal consistent reasoning deficiencies, with performance degrading sharply as complexity increases. In Hard Suite evaluations, Gemini-2.5-pro, Llama-3.3-70B, and Qwen2.5-72B achieved accuracies of 56.21%, 27.16%, and 33.37% respectively. Performance drops significantly without tool usage, with GPT-5, GPT-5-mini, and GPT-5-nano showing declines of 16.81%, 15.86%, and 43.95% in overall accuracy. Contamination resistance rests on three guarantees: (i) the problem space vastly exceeds any static dataset, (ii) every instance has a deterministically verifiable solution, and (iii) isomorphic transformations yield semantically equivalent but syntactically novel problems. BeyondBench redefines reasoning evaluation via genuine algorithmic problem-solving. Our leaderboard is at this https URL , Python package at this https URL , and codebase at this https URL .

</details>

---

### 46. [Beyond Prefixes: Graph-as-Memory Cross-Attention for Knowledge Graph Completion with Large Language Models](https://arxiv.org/abs/2510.08966)

**基本信息**

- 🔗 arXiv: [`2510.08966`](https://arxiv.org/abs/2510.08966)
- 👥 作者: Ruitong Liu, Boxu Lin, Peize Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.08966.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何将结构化知识（知识图谱）深度集成到大型语言模型中，以增强其在知识推理任务（如知识图谱补全）上的性能。这与“化学大模型”的研究高度相关，因为化学领域拥有丰富的结构化知识（如分子图、化学反应网络、性质数据库）。GMT提出的深度集成方法（图记忆令牌+交叉注意力）为在化学大模型中有效嵌入化学领域的先验知识（如官能团规则、反应规律）提供了一种有前景的技术路径，可以提升模型在分子性质预测、逆合成分析、质谱解析等任务上的推理能力和可解释性。

**📖 中文摘要**

本文提出了Graph-as-Memory Tuning（GMT），一种将知识图谱与大型语言模型（LLMs）融合的新范式，用于知识图谱补全等知识密集型任务。与现有通过前缀拼接注入图谱信息的浅层交互方法不同，GMT将局部图结构表示为显式的图记忆，并通过深层的、令牌级别的交叉注意力将其注入LLMs。具体来说，GMT首先使用语义图模块在知识增强关系的指导下编码局部邻域的上下文感知语义，并将其压缩成固定数量的图记忆令牌。然后，一个图作为记忆的交叉注意力融合模块将这些令牌集成到多个Transformer层中，允许LLM隐藏状态动态检索相关的图谱证据。实验表明，GMT显著优于前缀调整和其他强基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fusing Knowledge Graphs with Large Language Models (LLMs) is crucial for knowledge-intensive tasks like knowledge graph completion. Existing LLM-based approaches typically inject graph information via prefix concatenation, resulting in shallow interactions that fail to support fine-grained evidence retrieval during generation. Beyond prefixes, we propose Graph-as-Memory Tuning (GMT), a new paradigm that represents local graph structure as explicit graph memory and injects it into LLMs via deep, token-wise cross-attention. Specifically, GMT first employs a Semantic Graph Module to encode context-aware semantics from local neighborhoods guided by knowledge-enhanced relations, and compresses them into a fixed number of graph memory tokens. A Graph-as-Memory Cross-Attention Fusion Module then integrates these tokens into multiple Transformer layers, allowing LLM hidden state to dynamically retrieve relevant graph evidence. To enable efficient adaptation, GMT applies LoRA only to the memory cross-attention while keeping the base LLM frozen. Extensive experiments show that GMT significantly outperforms prefix-tuning and other strong baselines, providing more potent signals for robust reasoning. The code is published at this https URL .

</details>

---

### 47. [Text-to-3D by Stitching a Multi-view Reconstruction Network to a Video Generator](https://arxiv.org/abs/2510.13454)

**基本信息**

- 🔗 arXiv: [`2510.13454`](https://arxiv.org/abs/2510.13454)
- 👥 作者: Hyojun Go, Dominik Narnhofer, Goutam Bhat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.13454.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用强大的生成模型（文本到视频）与专业的重建模型相结合，来完成复杂的生成任务（文本到3D）。这种“生成器-解码器”的协同框架和模型缝合技术，对于构建“化学大模型”具有启发意义。例如，可以设想使用一个强大的分子语言模型作为“生成器”来产生分子描述或潜在表示，然后与一个专门化的分子构象生成或性质预测模型（“解码器”）相结合，以完成从文本描述到3D分子结构或性质的端到端生成。论文中的技术思路为这类跨模型、跨任务的化学大模型架构设计提供了参考。

**📖 中文摘要**

本文介绍了VIST3A，一个将现代潜在文本到视频模型作为“生成器”与近期（前馈）3D重建系统作为“解码器”相结合，用于文本到3D生成的通用框架。该框架解决了两个主要挑战：首先，通过模型缝合技术，在3D解码器中识别与文本到视频生成器产生的潜在表示最匹配的层，并将两部分缝合在一起。其次，使用直接奖励微调来对齐文本到视频生成器与缝合后的3D解码器，以确保生成的潜在表示可解码为一致、感知上可信的3D场景几何。评估表明，VIST3A显著改进了先前输出高斯溅射的文本到3D模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid progress of large, pretrained models for both visual content generation and 3D reconstruction opens up new possibilities for text-to-3D generation. Intuitively, one could obtain a formidable 3D scene generator if one were able to combine the power of a modern latent text-to-video model as "generator" with the geometric abilities of a recent (feedforward) 3D reconstruction system as "decoder". We introduce VIST3A, a general framework that does just that, addressing two main challenges. First, the two components must be joined in a way that preserves the rich knowledge encoded in their weights. We revisit model stitching, i.e., we identify the layer in the 3D decoder that best matches the latent representation produced by the text-to-video generator and stitch the two parts together. That operation requires only a small dataset and no labels. Second, the text-to-video generator must be aligned with the stitched 3D decoder, to ensure that the generated latents are decodable into consistent, perceptually convincing 3D scene geometry. To that end, we adapt direct reward finetuning, a popular technique for human preference alignment. We evaluate the proposed VIST3A approach with different video generators and 3D reconstruction models. All tested pairings markedly improve over prior text-to-3D models that output Gaussian splats. Moreover, by choosing a suitable 3D base model, VIST3A also enables high-quality text-to-pointmap generation.

</details>

---

### 48. [EchoMind: An Interrelated Multi-level Benchmark for Evaluating Empathetic Speech Language Models](https://arxiv.org/abs/2510.22758)

**基本信息**

- 🔗 arXiv: [`2510.22758`](https://arxiv.org/abs/2510.22758)
- 👥 作者: Li Zhou, Lutong Yu, You Lyu 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22758.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新颖的、多模态的（语音+语言）基准测试框架和数据集（EchoMind），专门用于评估模型对非文本线索（声音特征）的感知和整合推理能力。在“质谱结构推理”中，模型需要从复杂的、多峰的质谱数据（如MS/MS谱图，可能包含强度、质量、同位素模式等多种“线索”）中推理出分子结构。EchoBench强调的“多线索感知”、“整合推理”和“上下文关联”的评估理念，与质谱解析任务对模型能力的要求高度吻合。该基准的设计思路和方法论可以为构建更全面、更贴近真实挑战的质谱结构推理评估基准提供重要参考。

**📖 中文摘要**

本文提出了EchoMind，首个相互关联的多层级基准测试，用于评估语音语言模型（SLMs）的共情对话能力。该基准通过顺序的、上下文关联的任务来模拟共情对话的认知过程：口语内容理解、声音线索感知、整合推理和响应生成。所有任务共享相同且语义中立的脚本，并通过受控的声音风格变化来测试独立于文本内容的表达效果。EchoMind基于一个涵盖3个粗粒度和12个细粒度维度、包含39种声音属性的共情导向框架，并使用主客观指标进行评估。对12个先进SLMs的测试表明，即使最先进的模型在处理高表现力声音线索时也存在困难，限制了共情回应的质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech Language Models (SLMs) have made significant progress in spoken language understanding. Yet it remains unclear whether they can fully perceive non lexical vocal cues alongside spoken words, and respond with empathy that aligns with both emotional and contextual factors. Existing benchmarks typically evaluate linguistic, acoustic, reasoning, or dialogue abilities in isolation, overlooking the integration of these skills that is crucial for human-like, emotionally intelligent conversation. We present EchoMind, the first interrelated, multi-level benchmark that simulates the cognitive process of empathetic dialogue through sequential, context-linked tasks: spoken-content understanding, vocal-cue perception, integrated reasoning, and response generation. All tasks share identical and semantically neutral scripts that are free of explicit emotional or contextual cues, and controlled variations in vocal style are used to test the effect of delivery independent of the transcript. EchoMind is grounded in an empathy-oriented framework spanning 3 coarse and 12 fine-grained dimensions, encompassing 39 vocal attributes, and evaluated using both objective and subjective metrics. Testing 12 advanced SLMs reveals that even state-of-the-art models struggle with high-expressive vocal cues, limiting empathetic response quality. Analyses of prompt strength, speech source, and ideal vocal cue recognition reveal persistent weaknesses in instruction-following, resilience to natural speech variability, and effective use of vocal cues for empathy. These results underscore the need for SLMs that integrate linguistic content with diverse vocal cues to achieve truly empathetic conversational ability.

</details>

---

### 49. [Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling](https://arxiv.org/abs/2510.26139)

**基本信息**

- 🔗 arXiv: [`2510.26139`](https://arxiv.org/abs/2510.26139)
- 👥 作者: Minseo Kwon, Young J. Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.26139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是结合大型视觉语言模型（VLM）来增强任务与运动规划（TAMP）中的推理和搜索过程。VLM作为“大模型”的一种，被用于提供常识先验和视觉引导。在“化学大模型”和“质谱结构推理”的语境下，类似的思想可以应用于结合化学领域的VLM或LLM来指导分子结构搜索、逆合成路线规划或质谱解析中的假设生成与验证。例如，一个化学VLM可以分析分子结构或谱图的视觉表示，提出可能的结构片段或反应步骤，从而引导更高效的计算搜索。论文展示了VLM与符号/数值规划系统集成的潜力。

**📖 中文摘要**

本文提出了一种基于混合状态树的运动动力学任务与运动规划（TAMP）规划器，该规划器在规划过程中统一表示符号和数值状态，使得任务和运动决策能够共同决定。TAMP问题中嵌入的运动动力学约束由现成的运动规划器和物理模拟器验证，而视觉语言模型（VLM）则通过状态的可视化渲染来引导探索TAMP解决方案并基于此回溯搜索。实验表明，该方法相比传统和基于LLM的TAMP规划器，在模拟领域和现实世界中平均成功率提高了32.14% - 1166.67%，并在复杂问题上减少了规划时间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Task and Motion Planning (TAMP) integrates high-level task planning with low-level motion feasibility, but existing methods are costly in long-horizon problems due to excessive motion sampling. While LLMs provide commonsense priors, they lack 3D spatial reasoning and cannot ensure geometric or dynamic feasibility. We propose a kinodynamic TAMP planner based on a hybrid state tree that uniformly represents symbolic and numeric states during planning, enabling task and motion decisions to be jointly decided. Kinodynamic constraints embedded in the TAMP problem are verified by an off-the-shelf motion planner and physics simulator, and a VLM guides exploring a TAMP solution and backtracks the search based on visual rendering of the states. Experiments on the simulated domains and in the real world show 32.14% - 1166.67% increased average success rates compared to traditional and LLM-based TAMP planners and reduced planning time on complex problems, with ablations further highlighting the benefits of VLM backtracking. More details are available at this https URL .

</details>

---

### 50. [FMint-SDE: A Multimodal Foundation Model for Accelerating Numerical Simulation of SDEs via Error Correction](https://arxiv.org/abs/2510.27173)

**基本信息**

- 🔗 arXiv: [`2510.27173`](https://arxiv.org/abs/2510.27173)
- 👥 作者: Jiaxin Yuan, Haizhao Yang, Maria Cameron
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27173.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于加速科学计算（SDE求解）的“基础模型”。该模型通过上下文学习来校正传统数值方法的误差，具有通用性和可转移性。这直接呼应了“化学大模型”的愿景：构建能够加速和革新化学计算（如分子动力学模拟、量子化学计算、谱图模拟）的基础模型。FMint-SDE展示了如何将大语言模型/Transformer的架构和训练范式（上下文学习、多模态提示）应用于解决传统的科学计算问题，为开发化学领域的“模拟基础模型”提供了重要的概念验证和技术参考。

**📖 中文摘要**

本文介绍了FMint-SDE，一个基于解码器Transformer和上下文学习的新型多模态基础模型，用于加速随机微分方程（SDEs）的大规模数值模拟。FMint-SDE利用数值和文本模态来学习通用的误差校正方案。它使用传统求解器生成的粗略解提示序列进行训练，从而能够广泛泛化到不同的系统。模型在涵盖分子动力学、机械系统、金融和生物学应用的具有挑战性的SDE基准测试套件上进行了评估。实验结果表明，与经典求解器相比，该方法实现了更优的精度-效率权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fast and accurate simulation of dynamical systems is a fundamental challenge across scientific and engineering domains. Traditional numerical integrators often face a trade-off between accuracy and computational efficiency, while existing neural network-based approaches typically require training a separate model for each case. To overcome these limitations, we introduce a novel multi-modal foundation model for large-scale simulations of differential equations: FMint-SDE (Foundation Model based on Initialization for stochastic differential equations). Based on a decoder-only transformer with in-context learning, FMint-SDE leverages numerical and textual modalities to learn a universal error-correction scheme. It is trained using prompted sequences of coarse solutions generated by conventional solvers, enabling broad generalization across diverse systems. We evaluate our models on a suite of challenging SDE benchmarks spanning applications in molecular dynamics, mechanical systems, finance, and biology. Experimental results show that our approach achieves a superior accuracy-efficiency tradeoff compared to classical solvers, underscoring the potential of FMint-SDE as a general-purpose simulation tool for dynamical systems.

</details>

---

### 51. [FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding](https://arxiv.org/abs/2511.00141)

**基本信息**

- 🔗 arXiv: [`2511.00141`](https://arxiv.org/abs/2511.00141)
- 👥 作者: Janghoon Cho, Jungsoo Lee, Munawar Hayat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.00141.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决多模态大模型（视频LLMs）处理长序列输入时的视觉令牌压缩问题。这是构建高效“化学大模型”必须面对的关键技术挑战之一。例如，在质谱结构推理中，高分辨率质谱数据可以非常长；在分子建模中，3D分子构象或分子动力学轨迹也包含大量信息。FLoC提出的基于设施选址的令牌选择方法，为在化学大模型中高效、有原则地压缩高维化学数据（如光谱、分子点云、轨迹）提供了一种有前景的、可证明性能的解决方案，有助于降低计算成本并可能提高模型对关键特征的关注。

**📖 中文摘要**

本文提出了FLoC，一种基于设施选址函数的高效视觉令牌压缩框架，用于长视频理解。该方法通过惰性贪婪算法，在预定义的视觉令牌数量预算内，快速选择出一个紧凑但高度代表性和多样性的视觉令牌子集，从而保证接近最优的性能。该方法无需训练、与模型无关且与查询无关，提供了一个可无缝集成到各种视频LLMs和现有工作流程中的通用解决方案。在Video-MME、MLVU、LongVideoBench和EgoSchema等大规模基准测试上的广泛评估表明，该框架持续优于近期的压缩技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent studies in long video understanding have harnessed the advanced visual-language reasoning capabilities of Large Multimodal Models (LMMs), driving the evolution of video-LMMs specialized for processing extended video sequences. However, the scalability of these models is severely limited by the overwhelming volume of visual tokens generated from extended video sequences. To address this challenge, we propose FLoC, an efficient visual token compression framework based on the facility location function, a principled approach that swiftly selects a compact yet highly representative and diverse subset of visual tokens within a predefined budget on the number of visual tokens. By integrating the lazy greedy algorithm, our method achieves remarkable efficiency gains by swiftly selecting a compact subset of tokens, drastically reducing the number of visual tokens while guaranteeing near-optimal performance. Notably, our approach is training-free, model-agnostic, and query-agnostic, providing a versatile solution that seamlessly integrates with diverse video-LLMs and existing workflows. Extensive evaluations on large-scale benchmarks, such as Video-MME, MLVU, LongVideoBench, and EgoSchema, show that our framework consistently surpasses recent compression techniques, highlighting its effectiveness and robustness in addressing the challenges of long video understanding as well as its processing efficiency.

</details>

---

### 52. [Interleaved Tool-Call Reasoning for Protein Function Understanding](https://arxiv.org/abs/2601.03604)

**基本信息**

- 🔗 arXiv: [`2601.03604`](https://arxiv.org/abs/2601.03604)
- 👥 作者: Chuanliu Fan, Zicheng Ma, Huanran Meng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.03604.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个工具增强的LLM智能体（PFUA）来理解和预测蛋白质功能。这直接关联到‘化学大模型’主题，因为它探讨了如何将大语言模型与领域特定工具（可视为化学/生物信息学工具）结合，以解决复杂的科学推理问题，是化学信息学中大模型应用的一个具体案例。

**📖 中文摘要**

这篇论文探讨了将大语言模型（LLM）的推理能力应用于蛋白质功能理解这一特定领域。作者指出，直接将基于文本的思维链（CoT）推理范式迁移到蛋白质功能预测等知识密集型科学任务中是无效的，因为这类任务从根本上依赖于外部的生物学先验知识和计算工具，而非纯粹的内部推理。为此，论文提出了PFUA（Protein Function Understanding Agent），一个工具增强的蛋白质推理智能体。PFUA统一了问题分解、工具调用和基于证据的答案生成过程，通过整合领域特定工具来产生可验证的中间证据，从而增强模型的推理能力和泛化性。实验在四个基准测试上表明，PFUA的性能平均比纯文本推理模型提升了103%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

</details>

---

### 53. [Simple generators of rational function fields](https://arxiv.org/abs/2602.10878)

**基本信息**

- 🔗 arXiv: [`2602.10878`](https://arxiv.org/abs/2602.10878)
- 👥 作者: Alexander Demin, Gleb Pogudin
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10878.pdf)

**💡 相关性分析**

满足标准2：论文提出的算法能够为有理函数域的子域生成简化的生成元集。在化学信息学中，尤其是在计算化学、反应网络分析和系统生物学中，经常需要处理由多项式或有理函数定义的复杂模型（例如，化学动力学模型、代谢通路）。该算法提供的工具和资源（简化生成元）可以用于分析和处理这些模型，有助于从复杂的数学描述中提取关键变量或关系，从而可能服务于化学大模型的数据预处理或特征工程环节。

**📖 中文摘要**

本文提出了一种算法，用于为多元有理函数域的子域寻找简单的生成元集。算法的主要创新点包括通过稀疏插值进行部分Gröbner基计算，以及高效搜索有理函数域子域中固定次数的多项式。论文提供了一个算法实现，并展示了其在效率和结果质量上优于现有技术。此外，作者通过来自不同应用领域的案例研究（例如结构参数可辨识性）证明了简化生成元的实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Consider a subfield of the field of rational functions in several indeterminates. We present an algorithm that, given a set of generators of such a subfield, finds a simple generating set. We provide an implementation of the algorithm and show that it improves upon the state of the art both in efficiency and the quality of the results. Furthermore, we demonstrate the utility of simplified generators through several case studies from different application domains, such as structural parameter identifiability. The main algorithmic novelties include performing only partial Gröbner basis computation via sparse interpolation and efficient search for polynomials of a fixed degree in a subfield of the rational function field.

</details>

---

### 54. [SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework](https://arxiv.org/abs/2602.17330)

**基本信息**

- 🔗 arXiv: [`2602.17330`](https://arxiv.org/abs/2602.17330)
- 👥 作者: Rong Fu, Zijian Zhang, Kun Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.17330.pdf)

**💡 相关性分析**

满足标准2：该论文提出的SubQuad是一个用于免疫受体库分析的端到端计算管道，其核心是解决大规模、高维生物分子数据的相似性比较和聚类问题。它结合了GPU加速的亲和力核、学习的多模态融合和公平性约束的聚类，这些方法和技术（如高效检索、多模态数据融合、聚类）与化学信息学中处理质谱或分子结构数据时面临的挑战（如高通量比较、异构数据整合、处理不平衡数据集）高度相关。该框架可以被视为一种可用于化学信息学领域（特别是处理复杂分子或质谱数据）的数据处理和分析工具或方法学资源。

**📖 中文摘要**

本文提出了SubQuad，一个用于自适应免疫受体库比较分析的计算框架。该框架旨在解决两个主要瓶颈：成对亲和力评估的近二次方计算成本，以及数据集不平衡对临床重要少数克隆型的掩盖。SubQuad结合了抗原感知的近次二次方检索、GPU加速的亲和力核、学习的多模态融合和公平性约束的聚类。该系统采用紧凑的MinHash预过滤来大幅减少候选比较，一个可微的门控模块自适应地加权互补的对齐和嵌入通道，以及一个自动校准例程来强制稀有抗原特异性亚群的比例表示。在大型病毒和肿瘤受体库上，SubQuad在保持或提高召回率、聚类纯度和亚群公平性的同时，实现了吞吐量和峰值内存使用量的显著提升。该工作通过共同设计索引、相似性融合和公平感知目标，为受体库挖掘和下游转化任务（如疫苗靶点优先级排序和生物标志物发现）提供了一个可扩展、偏差感知的平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Comparative analysis of adaptive immune repertoires at population scale is hampered by two practical bottlenecks: the near-quadratic cost of pairwise affinity evaluations and dataset imbalances that obscure clinically important minority clonotypes. We introduce SubQuad, an end-to-end pipeline that addresses these challenges by combining antigen-aware, near-subquadratic retrieval with GPU-accelerated affinity kernels, learned multimodal fusion, and fairness-constrained clustering. The system employs compact MinHash prefiltering to sharply reduce candidate comparisons, a differentiable gating module that adaptively weights complementary alignment and embedding channels on a per-pair basis, and an automated calibration routine that enforces proportional representation of rare antigen-specific subgroups. On large viral and tumor repertoires SubQuad achieves measured gains in throughput and peak memory usage while preserving or improving recall@k, cluster purity, and subgroup equity. By co-designing indexing, similarity fusion, and equity-aware objectives, SubQuad offers a scalable, bias-aware platform for repertoire mining and downstream translational tasks such as vaccine target prioritization and biomarker discovery.

</details>

---

### 55. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型（Zatom-1）。这直接属于“化学大模型”的范畴，因为它是一个旨在通用化学表示和任务（包括分子和材料）的AI模型。其多模态流匹配目标和对3D几何的建模也与“质谱结构推理”中涉及的分子结构生成和性质预测高度相关。

**📖 中文摘要**

本文介绍了Zatom-1，这是第一个端到端、完全开源的基础模型，它统一了3D分子和材料的生成与预测学习。Zatom-1是一个Transformer模型，通过多模态流匹配目标进行训练，该目标联合建模离散的原子类型和连续的3D几何结构。这种方法支持可扩展的预训练，并能够实现快速稳定的采样。作者使用联合生成预训练作为下游多任务预测（如性质、能量和力）的通用初始化。实验表明，Zatom-1在生成和预测基准测试中均匹配或优于专门的基线模型，同时将生成推理时间减少了一个数量级以上。研究还证明了通过联合生成预训练在化学领域之间（例如，在预训练中建模材料可以提高分子性质预测的准确性）存在正向的预测迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first end-to-end, fully open-source foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 56. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、高效的机器学习原子间势（MLIP）模型MatRIS，用于材料科学的模拟和预测。MLIP是化学信息学和计算化学中“化学大模型”的一个重要子领域，旨在用AI模型替代传统的量子力学计算，以加速分子和材料性质的预测。该工作直接贡献于化学大模型在材料发现和模拟方面的进展。

**📖 中文摘要**

本文提出了MatRIS，一种用于材料科学的不变机器学习原子间势（MLIP）。MatRIS引入了基于注意力的三体相互作用建模，并利用一种具有线性复杂度O(N)的新型可分离注意力机制，实现了可扩展性和表达性。MatRIS在广泛的流行基准测试（如Matbench-Discovery, MatPES, MDR phonon, Molecular dataset等）上提供了与领先的等变模型相媲美的准确性。例如，在Matbench-Discovery上，MatRIS的F1分数高达0.847，并且以更低的训练成本达到了相当的准确性。这项工作表明，经过精心设计的不变模型可以以较低的成本匹配或超过等变模型的准确性，为开发准确高效的MLIPs提供了启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 57. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是发展关联记忆模型（如Hopfield网络）中顺序推理的数学理论。虽然不直接处理化学或质谱数据，但其研究的“顺序推理”是“化学大模型”和“质谱结构推理”中核心的认知过程。例如，在质谱解析中，模型需要顺序地推断碎片化模式以构建分子结构；在化学大模型中，模型需要进行多步推理来预测反应或性质。因此，该论文对理解和支持这些主题背后的核心计算机制（推理）有重要贡献。

**📖 中文摘要**

本文为Hopfield网络中的顺序推理发展了一套动力学理论。作者考虑了最近提出的输入驱动可塑性（IDP）Hopfield网络，并分析了一个将快速关联检索与慢速推理动力学耦合的双时间尺度架构。他们推导出了自持记忆转换的明确条件，包括增益阈值、逃逸时间和崩溃机制。这些结果为关联记忆模型中的顺序性提供了原则性的数学解释，架起了经典Hopfield动力学与现代推理架构之间的桥梁。虽然论文主要关注抽象的关联记忆模型，但其理论旨在为理解机器学习系统（如大语言模型）中的顺序推理提供洞见。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 58. [Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning](https://arxiv.org/abs/2603.03229)

**基本信息**

- 🔗 arXiv: [`2603.03229`](https://arxiv.org/abs/2603.03229)
- 👥 作者: Adam Watts, Andrew Jeon, Destry Newton 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03229.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于深度生成模型（CVAE）的方法，用于解决从谱数据（冲击响应谱）逆推时间序列信号的问题。虽然应用领域是工程力学，但其核心方法论——使用生成模型从谱特征重建复杂信号——与“质谱结构推理”的核心问题高度相似。在质谱分析中，一个关键挑战是从质谱图（一种谱信号）逆推分子结构。该论文展示的“谱到信号/结构”的逆问题求解框架，为质谱结构推理提供了潜在的方法论参考和工具思路。

**📖 中文摘要**

本文提出了一种条件变分自编码器（CVAE），用于从冲击响应谱（SRS）曲线学习数据驱动的逆映射，以重建加速度时间序列。一旦训练完成，该模型可以根据规定的目标谱生成一致的信号，而无需迭代优化。实验证明，相对于经典技术，该方法在谱保真度方面有所改进，对未见过的谱具有强大的泛化能力，并且推理速度比传统方法快三到六个数量级。这些结果确立了深度生成建模作为一种可扩展且高效的逆SRS重建方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions. We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

</details>

---

### 59. [DMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement](https://arxiv.org/abs/2603.03769)

**基本信息**

- 🔗 arXiv: [`2603.03769`](https://arxiv.org/abs/2603.03769)
- 👥 作者: Youngmin Kim, Jaeyun Shin, Jeongchan Kim 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03769.pdf)

**💡 相关性分析**

满足标准2：论文的核心是开发一种用于医学图像翻译的生成模型框架，特别强调了在非配对数据设置下保持解剖结构。虽然应用领域是医学影像，但其采用的关键技术——非配对神经薛定谔桥（UNSB）、扩散模型引导和结构保持正则化——代表了生成模型和跨域翻译的前沿方法。这些方法可以迁移到化学信息学领域，例如，用于从低分辨率质谱数据生成高分辨率模拟谱图，或在不同仪器/条件下质谱数据的标准化和增强，从而为“质谱结构推理”提供数据预处理或增强工具。

**📖 中文摘要**

本文提出了一个用于超低场（64 mT）脑MRI到3 T MRI的非配对图像翻译框架，旨在提升图像真实感同时保持解剖结构。该方法建立在非配对神经薛定谔桥（UNSB）的基础上，并进行了多步细化。为了加强目标分布对齐，作者使用冻结的3T扩散教师模型，通过DMD2风格的扩散引导分布匹配来增强对抗目标。为了在图像块级对应之外明确约束全局结构，他们将PatchNCE与解剖结构保持（ASP）正则化器相结合，该正则化器强制执行软前景-背景一致性和边界感知约束。在两个独立队列上的评估表明，所提出的框架在非配对基准上改善了真实感与结构的权衡，同时在配对队列上与非配对基线相比提高了结构保真度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ultra Low Field (64 mT) brain MRI improves accessibility but suffers from reduced image quality compared to 3 T. As paired 64 mT - 3 T scans are scarce, we propose an unpaired 64 mT $\rightarrow$ 3 T translation framework that enhances realism while preserving anatomy. Our method builds upon the Unpaired Neural Schrödinge Bridge (UNSB) with multi-step refinement. To strengthen target distribution alignment, we augment the adversarial objective with DMD2-style diffusion-guided distribution matching using a frozen 3T diffusion teacher. To explicitly constrain global structure beyond patch-level correspondence, we combine PatchNCE with an Anatomical Structure Preservation (ASP) regularizer that enforces soft foreground background consistency and boundary aware constraints. Evaluated on two disjoint cohorts, the proposed framework achieves an improved realism structure trade-off, enhancing distribution level realism on unpaired benchmarks while increasing structural fidelity on the paired cohort compared to unpaired baselines.

</details>

---

### 60. [TumorFlow: Physics-Guided Longitudinal MRI Synthesis of Glioblastoma Growth](https://arxiv.org/abs/2603.04058)

**基本信息**

- 🔗 arXiv: [`2603.04058`](https://arxiv.org/abs/2603.04058)
- 👥 作者: Valentin Biller, Niklas Bubeck, Lucas Zimmer 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04058.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个结合了生物物理模型（机制性先验）和生成式AI的框架，用于合成具有生物学真实性的医学影像数据。这种方法论——将领域知识（物理/化学模型）与数据驱动的生成模型相结合——对于“化学大模型”和“质谱结构推理”具有重要的借鉴意义。例如，在质谱结构推理中，可以结合化学反应规则或碎片化规律作为先验知识，来引导生成更合理的分子结构假设。该论文展示的“模型+数据”混合框架为解决化学中的逆问题（如从谱推结构）提供了有价值的范式参考。

**📖 中文摘要**

本文提出了一个生物物理条件生成框架，用于从估计的、空间连续的肿瘤浓度场合成生物学上真实的3D脑MRI体积。该方法结合了一个生成模型和一个肿瘤浸润图，该图可以使用生物物理生长模型随时间传播，从而实现对肿瘤形状和生长的细粒度控制，同时保留患者解剖结构。这使得能够直接在真实患者的空间中合成一致的肿瘤生长轨迹，提供可解释的、可控的肿瘤浸润和进展估计，超出了成像中明确观察到的范围。在纵向胶质母细胞瘤病例上的评估表明，该框架可以生成具有真实肿瘤外观变化和周围组织反应的时间相干序列。这些结果表明，将机制性肿瘤生长先验与现代生成建模相结合，可以为患者特异性进展可视化和生成受控合成数据以支持下游神经肿瘤学工作流程提供一个实用工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Glioblastoma exhibits diverse, infiltrative, and patient-specific growth patterns that are only partially visible on routine MRI, making it difficult to reliably assess true tumor extent and personalize treatment planning and follow-up. We present a biophysically-conditioned generative framework that synthesizes biologically realistic 3D brain MRI volumes from estimated, spatially continuous tumor-concentration fields. Our approach combines a generative model with tumor-infiltration maps that can be propagated through time using a biophysical growth model, enabling fine-grained control over tumor shape and growth while preserving patient anatomy. This enables us to synthesize consistent tumor growth trajectories directly in the space of real patients, providing interpretable, controllable estimation of tumor infiltration and progression beyond what is explicitly observed in imaging. We evaluate the framework on longitudinal glioblastoma cases and demonstrate that it can generate temporally coherent sequences with realistic changes in tumor appearance and surrounding tissue response. These results suggest that integrating mechanistic tumor growth priors with modern generative modeling can provide a practical tool for patient-specific progression visualization and for generating controlled synthetic data to support downstream neuro-oncology workflows. In longitudinal extrapolation, we achieve a consistent 75% Dice overlap with the biophysical model while maintaining a constant PSNR of 25 in the surrounding tissue. Our code is available at: this https URL

</details>

---

### 61. [CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery](https://arxiv.org/abs/2511.19500)

**基本信息**

- 🔗 arXiv: [`2511.19500`](https://arxiv.org/abs/2511.19500)
- 👥 作者: Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.19500.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于化学材料（有机光伏）发现和设计的机器学习模型与框架，这直接属于“化学大模型”的研究范畴。同时，满足标准2：论文构建并提供了大型化学数据集OPV2D，可用于训练和评估化学大模型。

**📖 中文摘要**

本文提出了一个用于有机光伏（OPV）材料发现的机器学习框架CycleChemist。该框架结合了预测建模与生成式分子设计，并引入了OPV2D数据集，这是目前最大的、包含2000个实验表征的给体-受体对的数据集。框架包含多个组件：用于预测材料是否具有OPV行为的分类器（OPVC）、用于预测HOMO和LUMO能级的分子轨道能量估计器（MOE2）、用于预测功率转换效率（PCE）的光伏性能预测器（P3），以及用于生成可合成有机半导体的生成式预训练模型（MatGPT）。该工作通过将分子表示学习与性能预测相结合，推动了高性能OPV材料的数据驱动发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials.

</details>

---

### 62. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接针对“化学大模型”（具体是化学大语言模型）的推理范式进行创新，提出了从显式文本思维链转向隐式潜在推理的新方法，是化学大模型领域的前沿研究。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。针对当前化学大语言模型（LLMs）依赖显式自然语言思维链（CoT）进行推理的局限性，LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中进行多步推理，仅对最终输出生成语言。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变带来了显著的性能提升和效率优势。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于强大的CoT基线取得了59.88%的非平局胜率，同时实现了平均10.84倍的推理加速。结果表明，化学推理更自然、更有效地体现为连续的潜在动态过程，而非离散的语言轨迹。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 63. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准1：论文的研究内容涉及图结构预测和不确定性量化，其评估应用场景明确包含“分子识别”。这直接关联到化学信息学中利用图神经网络进行分子性质预测或结构推理的任务，与“质谱结构推理”中可能涉及的分子图生成或识别有潜在相关性。

**📖 中文摘要**

本文提出了一种用于图结构输出的保形预测框架，旨在为结构化输出（如图）提供分布无关的覆盖保证。该方法通过Z-Gromov-Wasserstein距离（实践中通过Fused Gromov-Wasserstein距离实例化）来定义非保形分数，从而实现对预测图与候选图之间的置换不变比较。为了获得自适应的预测集，作者将保形化分位数回归（CQR）扩展到复杂输出空间，提出了分数保形化分位数回归（SCQR）。论文在一个合成任务和一个真实的分子识别问题上评估了所提出的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 64. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个自动化执行计算化学核心方法（DFT）的智能框架。DFT是化学和材料科学中用于模拟分子和材料电子结构的基础理论工具，自动化DFT框架是支撑“化学大模型”数据生成和验证的关键基础设施，与化学信息学研究高度相关。

**📖 中文摘要**

本文介绍了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学和计算化学的基石，但其实际执行涉及协调复杂、多步骤的工作流。TritonDFT通过专家策划、可扩展的工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效、准确的DFT执行。此外，论文还引入了DFTBench，一个用于评估智能体在多维度能力（包括科学专业知识、权衡优化、高性能计算知识和成本效率）的基准测试。该框架为现实世界的DFT计算提供了开放的自动化用户界面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：17
- 累计论文数量：1193

## 📝 历史记录

> 暂无历史数据

