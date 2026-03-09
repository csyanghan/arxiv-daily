# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-09 01:31:17

## 📅 2026-03-09 (今日最新)

**相关论文数：75**

### 1. [A unified foundational framework for knowledge injection and evaluation of Large Language Models in Combustion Science](https://arxiv.org/abs/2603.04452)

**基本信息**

- 🔗 arXiv: [`2603.04452`](https://arxiv.org/abs/2603.04452)
- 👥 作者: Zonglin Yang, Runze Mao, Tianhao Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04452.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个面向【化学信息学】子领域（燃烧科学）的领域专业化大语言模型（化学大模型）开发框架，包括知识库构建、评估基准和知识注入方法。

**📖 中文摘要**

本文提出了一个用于燃烧科学领域大语言模型（LLM）开发的端到端框架。该框架的核心是构建了一个包含35亿token的多模态知识库，数据源包括20多万篇同行评审文章、8000篇学位论文以及约40万行燃烧计算流体动力学（CFD）代码。此外，还创建了一个包含8个子领域、436个问题的自动化评估基准（CombustionQA）。研究探讨了从轻量级检索增强生成（RAG）到知识图谱增强检索和持续预训练的三阶段知识注入路径。研究发现，标准RAG在燃烧科学问答任务中的准确率存在上限（60%），远低于理论上限（87%），并受限于上下文污染问题，从而论证了构建领域基础模型需要结构化知识图谱和持续预训练的必要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To advance foundation Large Language Models (LLMs) for combustion science, this study presents the first end-to-end framework for developing domain-specialized models for the combustion community. The framework comprises an AI-ready multimodal knowledge base at the 3.5 billion-token scale, extracted from over 200,000 peer-reviewed articles, 8,000 theses and dissertations, and approximately 400,000 lines of combustion CFD code; a rigorous and largely automated evaluation benchmark (CombustionQA, 436 questions across eight subfields); and a three-stage knowledge-injection pathway that progresses from lightweight retrieval-augmented generation (RAG) to knowledge-graph-enhanced retrieval and continued pretraining. We first quantitatively validate Stage 1 (naive RAG) and find a hard ceiling: standard RAG accuracy peaks at 60%, far surpassing zero-shot performance (23%) yet well below the theoretical upper bound (87%). We further demonstrate that this stage's performance is severely constrained by context contamination. Consequently, building a domain foundation model requires structured knowledge graphs and continued pretraining (Stages 2 and 3).

</details>

---

### 2. [iScript: A Domain-Adapted Large Language Model and Benchmark for Physical Design Tcl Script Generation](https://arxiv.org/abs/2603.04476)

**基本信息**

- 🔗 arXiv: [`2603.04476`](https://arxiv.org/abs/2603.04476)
- 👥 作者: Ning Xu, Zhaoyang Zhang, Senlin Shu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个面向电子设计自动化（EDA）特定领域（物理设计Tcl脚本生成）的领域适应大语言模型（化学大模型在相关工程领域的应用）。

**📖 中文摘要**

本文介绍了iScript，一个针对物理设计工具Innovus的Tcl脚本生成任务进行领域适应训练的大语言模型（基于Qwen3-8B）。同时，提出了iScript-Bench基准测试，涵盖5个任务类别和3个难度级别。为了解决EDA领域训练数据稀缺的问题，论文提出了一种多阶段数据合成流程，通过命令提取、静态检查、需求反推和思维链生成，生成了一个包含1万组（需求、思维链、脚本）的数据集。iScript通过领域自适应预训练和监督微调的两阶段策略进行训练。论文还提出了一个包含静态语法验证和基于LLM的功能评估的两步验证框架来高效评估脚本正确性。实验表明，iScript在基准测试上的表现优于当前最先进的大语言模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern EDA flows rely heavily on Tcl scripting, yet general LLMs perform poorly in this domain due to extreme data scarcity, domain-specific semantics, and the high reliability required in physical design. We present iScript, a domain-adapted Qwen3-8B model for Innovus Tcl script generation, and iScript-Bench, a comprehensive benchmark covering five task categories and three difficulty levels. To overcome the lack of training data, we introduce a multi-stage data synthesis pipeline that integrates command extraction, static linting, requirement back-inference, and Chain-of-Thought generation, producing a 10K-tuple (requirement, CoT, script) dataset. iScript is trained through a two-stage strategy combining domain-adaptive pretraining and supervised fine-tuning. To evaluate script correctness efficiently, we further propose a two-step verification framework consisting of static syntax verification and LLM-based functional evaluation. On our benchmark, iScript shows higher pass@k scores than currently state-of-the-art LLMs on average. These results demonstrate the effectiveness of domain adaptation and data synthesis for EDA scripting tasks.

</details>

---

### 3. [Augmenting representations with scientific papers](https://arxiv.org/abs/2603.04516)

**基本信息**

- 🔗 arXiv: [`2603.04516`](https://arxiv.org/abs/2603.04516)
- 👥 作者: Nicolò Oreste Pinciroli Vago, Rocco Di Tella, Carolina Cuesta-Lázaro 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04516.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个多模态对比学习框架，用于对齐科学数据（X射线光谱）与文本知识（科学文献），这本质上是构建一个能够理解和关联【化学信息学】及质谱相关领域（天体物理光谱学）数据与文本的【化学大模型】或科学基础模型。

**📖 中文摘要**

本文提出了一个对比学习框架，旨在将X射线光谱与从科学文献中提取的领域知识对齐，从而促进共享多模态表示的发展。建立这种联系非常复杂，因为科学文本包含的物理背景比光谱更广泛、更多样。作者提出的对比学习流程在根据光谱检索相关文本的任务中实现了20%的Recall@1，证明这两种模态之间有意义的对齐不仅是可能的，而且能够加速对稀有或理解不足的天体源的解释。此外，得到的共享潜在空间有效地编码了具有物理意义的信息。通过融合光谱和文本数据，在20个物理变量的估计上，比单模态光谱基线提高了16-18%。结果表明，利用专家混合（MoE）策略，同时利用单模态和共享表示，可以获得更优的性能。

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

满足标准1：论文的核心研究内容是开发一个能够自主进行数学概念发现（如同调）的多智能体系统，这属于探索人工智能（大模型/多智能体系统）在科学发现（包括化学信息学中的结构推理）中的应用，与【化学大模型】和自主科学推理的主题相关。

**📖 中文摘要**

本文提出了一种新的多智能体计算数学发现模型。该系统能够自主提出猜想并尝试证明，根据反馈和不断演化的数据分布做出决策。受欧拉多面体猜想历史和文献中开放挑战的启发，论文以从多面体数据中自主恢复同调概念为基准任务，并在线性代数知识的基础上进行测试。该系统成功完成了这一学习问题。最重要的是，实验进行了消融研究，统计测试了完整动态过程的价值，并控制了实验设置。结果支持了主要主张：优化正确的局部过程组合可以导致与数学趣味性惊人一致的概念。

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

满足标准1：论文的核心研究内容涉及利用真实世界数据（可视为一种特殊的数据资源）来蒸馏和提升模型在机器人操作中的感知与策略，这属于【化学大模型】在机器人学与具身智能中的交叉应用，其“数据蒸馏”思想与构建领域模型相关。

**📖 中文摘要**

本文提出了PTLD（sim-to-real Privileged Tactile Latent Distillation），一种无需触觉模拟即可学习触觉操作技能的新方法。其核心思想是利用现实世界中的特权传感器收集真实世界的触觉策略数据，然后利用这些数据蒸馏出一个基于触觉输入的鲁棒状态估计器。实验表明，PTLD可用于显著改进在模拟中训练的本体感知操作策略，通过融入触觉感知。在基准手内旋转任务上，PTLD比纯本体感知策略提高了182%。PTLD还能学习具有挑战性的触觉手内重定向任务，在此任务上比单独使用本体感知达到的目标数量提高了57%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tactile dexterous manipulation is essential to automating complex household tasks, yet learning effective control policies remains a challenge. While recent work has relied on imitation learning, obtaining high quality demonstrations for multi-fingered hands via robot teleoperation or kinesthetic teaching is prohibitive. Alternatively, with reinforcement we can learn skills in simulation, but fast and realistic simulation of tactile observations is challenging. To bridge this gap, we introduce PTLD: sim-to-real Privileged Tactile Latent Distillation, a novel approach to learning tactile manipulation skills without requiring tactile simulation. Instead of simulating tactile sensors or relying purely on proprioceptive policies to transfer zero-shot sim-to-real, our key idea is to leverage privileged sensors in the real world to collect real-world tactile policy data. This data is then used to distill a robust state estimator that operates on tactile input. We demonstrate from our experiments that PTLD can be used to improve proprioceptive manipulation policies trained in simulation significantly by incorporating tactile sensing. On the benchmark in-hand rotation task, PTLD achieves a 182% improvement over a proprioception only policy. We also show that PTLD enables learning the challenging task of tactile in-hand reorientation where we see a 57% improvement in the number of goals reached over using proprioception alone. Website: this https URL .

</details>

---

### 6. [Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling](https://arxiv.org/abs/2603.04553)

**基本信息**

- 🔗 arXiv: [`2603.04553`](https://arxiv.org/abs/2603.04553)
- 👥 作者: Tal Daniel, Carl Qi, Dan Haramati 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04553.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个能够从视频中无监督发现物体表示（关键点、边界框、掩码）的模型框架。这种学习物体中心表示和动力学的能力，为【质谱结构推理】等任务提供了潜在的通用表示学习方法和数据生成/模拟思路，属于可用于相关主题的工具或方法资源。

**📖 中文摘要**

本文介绍了潜在粒子世界模型（LPWM），一个可扩展到真实世界多物体数据集并适用于决策的自监督物体中心世界模型。LPWM直接从视频数据中自主发现关键点、边界框和物体掩码，使其能够在没有监督的情况下学习丰富的场景分解。该架构完全从视频端到端训练，支持灵活地以动作、语言和图像目标为条件。LPWM通过新颖的潜在动作模块对随机粒子动力学进行建模，并在多样化的真实世界和合成数据集上取得了最先进的结果。除了随机视频建模，LPWM readily适用于决策任务，包括目标条件模仿学习。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Latent Particle World Model (LPWM), a self-supervised object-centric world model scaled to real-world multi-object datasets and applicable in decision-making. LPWM autonomously discovers keypoints, bounding boxes, and object masks directly from video data, enabling it to learn rich scene decompositions without supervision. Our architecture is trained end-to-end purely from videos and supports flexible conditioning on actions, language, and image goals. LPWM models stochastic particle dynamics via a novel latent action module and achieves state-of-the-art results on diverse real-world and synthetic datasets. Beyond stochastic video modeling, LPWM is readily applicable to decision-making, including goal-conditioned imitation learning, as we demonstrate in the paper. Code, data, pre-trained models and video rollouts are available: this https URL

</details>

---

### 7. [Structure-Guided Histopathology Synthesis via Dual-LoRA Diffusion](https://arxiv.org/abs/2603.04565)

**基本信息**

- 🔗 arXiv: [`2603.04565`](https://arxiv.org/abs/2603.04565)
- 👥 作者: Xuan Xu, Prateek Prasanna
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04565.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于扩散模型和细胞核中心点先验的图像合成与修复方法。这种生成高质量、结构可控的生物医学图像（组织病理学）的技术，可以作为生成用于【化学大模型】或【质谱结构推理】训练的合成数据或增强数据的工具，属于数据生成资源。

**📖 中文摘要**

本文提出了一种双LoRA可控扩散框架，用于组织病理学图像合成。该框架统一支持局部结构补全和全局结构合成。多类细胞核中心点作为轻量级且注释高效的空间先验，在图像部分或完全缺失的情况下提供具有生物学意义的指导。两个任务特定的LoRA适配器使共享主干网络专用于局部和全局目标，而无需重新训练单独的扩散模型。大量实验表明，在修复和合成任务上，该方法 consistently 优于最先进的GAN和扩散基线。对于局部补全，掩码区域内的LPIPS从0.1797（HARP）提高到0.1524；对于全局合成，FID从225.15（CoSys）提高到76.04，表明结构保真度和真实感得到改善。该方法在掩码区域实现了更忠实的结构恢复，在全合成中显著提高了真实感和形态一致性，支持可扩展的泛癌组织病理学建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathology image synthesis plays an important role in tissue restoration, data augmentation, and modeling of tumor microenvironments. However, existing generative methods typically address restoration and generation as separate tasks, although both share the same objective of structure-consistent tissue synthesis under varying degrees of missingness, and often rely on weak or inconsistent structural priors that limit realistic cellular organization. We propose Dual-LoRA Controllable Diffusion, a unified centroid-guided diffusion framework that jointly supports Local Structure Completion and Global Structure Synthesis within a single model. Multi-class nuclei centroids serve as lightweight and annotation-efficient spatial priors, providing biologically meaningful guidance under both partial and complete image absence. Two task-specific LoRA adapters specialize the shared backbone for local and global objectives without retraining separate diffusion models. Extensive experiments demonstrate consistent improvements over state-of-the-art GAN and diffusion baselines across restoration and synthesis tasks. For local completion, LPIPS computed within the masked region improves from 0.1797 (HARP) to 0.1524, and for global synthesis, FID improves from 225.15 (CoSys) to 76.04, indicating improved structural fidelity and realism. Our approach achieves more faithful structural recovery in masked regions and substantially improved realism and morphology consistency in full synthesis, supporting scalable pan-cancer histopathology modeling.

</details>

---

### 8. [PDE foundation model-accelerated inverse estimation of system parameters in inertial confinement fusion](https://arxiv.org/abs/2603.04606)

**基本信息**

- 🔗 arXiv: [`2603.04606`](https://arxiv.org/abs/2603.04606)
- 👥 作者: Mahindra Rautela, Alexander Scheinker, Bradley Love 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04606.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用预训练的PDE基础模型（一种特定领域的大模型）解决从观测数据反推系统参数的逆问题。这与“化学大模型”和“质谱结构推理”（从质谱数据推理分子结构）的核心研究范式高度一致，都是利用大模型/基础模型处理复杂的、数据驱动的科学推理任务。

**📖 中文摘要**

本文研究了偏微分方程（PDE）基础模型在惯性约束聚变（ICF）逆问题中的应用，即从多模态观测数据中估计系统参数。研究利用JAG基准数据集，通过微调PDE基础模型并训练一个轻量级的任务特定头，联合重建高光谱图像并回归系统参数。该工作展示了基础模型在数据受限的逆问题中的样本效率优势。虽然应用领域是物理模拟，但其核心方法——使用预训练的基础模型（可视为一种“化学大模型”的物理模拟类比）解决复杂的、数据驱动的逆问题——与“化学大模型”用于从观测数据（如质谱）推理结构（系统参数）的研究范式高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PDE foundation models are typically pretrained on large, diverse corpora of PDE datasets and can be adapted to new settings with limited task-specific data. However, most downstream evaluations focus on forward problems, such as autoregressive rollout prediction. In this work, we study an inverse problem in inertial confinement fusion (ICF): estimating system parameters (inputs) from multi-modal, snapshot-style observations (outputs). Using the open JAG benchmark, which provides hyperspectral X-ray images and scalar observables per simulation, we finetune the PDE foundation model and train a lightweight task-specific head to jointly reconstruct hyperspectral images and regress system parameters. The fine-tuned model achieves accurate hyperspectral reconstruction (test MSE 1.2e-3) and strong parameter-estimation performance (up to R^2=0.995). Data-scaling experiments (5%-100% of the training set) show consistent improvements in both reconstruction and regression losses as the amount of training data increases, with the largest marginal gains in the low-data regime. Finally, finetuning from pretrained MORPH weights outperforms training the same architecture from scratch, demonstrating that foundation-model initialization improves sample efficiency for data-limited inverse problems in ICF.

</details>

---

### 9. [When Agents Persuade: Propaganda Generation and Mitigation in LLMs](https://arxiv.org/abs/2603.04636)

**基本信息**

- 🔗 arXiv: [`2603.04636`](https://arxiv.org/abs/2603.04636)
- 👥 作者: Julia Jose, Ritik Roongta, Rachel Greenstadt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04636.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从扩散MRI测量数据中，通过可微分物理模拟和优化，逆向推理出组织的微结构（包括边界和渗透性）。这本质上是一个从复杂观测数据（dMRI信号）推理底层物理/化学结构（组织微结构）的逆问题，与“质谱结构推理”（从质谱信号推理分子结构）在问题定义和解决范式上高度相似，都属于科学数据分析中的结构推理问题。

**📖 中文摘要**

本文提出了Spinverse，一种用于从扩散MRI（dMRI）测量中感知渗透性的微结构重建方法。该方法通过一个完全可微分的Bloch-Torrey模拟器来反演dMRI测量值。Spinverse在固定的四面体网格上表示组织，并将每个内部面的渗透率作为可学习参数；低渗透率的面充当扩散屏障，从而在不改变网格连接的情况下浮现出微结构边界。给定目标信号，通过反向传播信号匹配损失来优化面渗透率，并通过阈值化学习到的渗透率场来恢复界面。该工作解决了从dMRI数据中显式恢复可渗透界面的逆问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their wide-ranging benefits, LLM-based agents deployed in open environments can be exploited to produce manipulative material. In this study, we task LLMs with propaganda objectives and analyze their outputs using two domain-specific models: one that classifies text as propaganda or non-propaganda, and another that detects rhetorical techniques of propaganda (e.g., loaded language, appeals to fear, flag-waving, name-calling). Our findings show that, when prompted, LLMs exhibit propagandistic behaviors and use a variety of rhetorical techniques in doing so. We also explore mitigation via Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and ORPO (Odds Ratio Preference Optimization). We find that fine-tuning significantly reduces their tendency to generate such content, with ORPO proving most effective.

</details>

---

### 10. [Gamified Informed Decision-Making for Performance-Aware Design by Non-Experts: An Exoskeleton Design Case Study](https://arxiv.org/abs/2603.04643)

**基本信息**

- 🔗 arXiv: [`2603.04643`](https://arxiv.org/abs/2603.04643)
- 👥 作者: Arman Khalilbeigi Khameneh, Armin Mostafavi, Alicia Nahmad Vazquez
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04643.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门为R统计生态系统（广泛用于化学计量学、生物信息学数据分析）设计的检索增强生成（RAG）框架和嵌入模型（DARE）。它提供了一个用于检索R包和函数的知识库（RPKB）和工具（RCodingAgent），这些资源可直接用于化学信息学领域的数据分析任务，辅助质谱数据分析或化学大模型的应用开发。

**📖 中文摘要**

本文提出了DARE（Distribution-Aware Retrieval Embedding），一个轻量级、即插即用的检索模型，它将数据分布信息整合到函数表示中，用于R软件包的检索。主要贡献包括：（i）RPKB，一个从8,191个高质量CRAN包中提取的R包知识库；（ii）DARE，一个融合分布特征与函数元数据的嵌入模型；（iii）RCodingAgent，一个面向R的LLM智能体，用于可靠的R代码生成。DARE显著提升了R包检索的相关性，并将其集成到RCodingAgent中，在下游分析任务上带来了显著增益。这项工作旨在缩小LLM自动化与成熟的R统计生态系统之间的差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Decision Support Systems (DSS) play a crucial role in enabling non-expert designers to explore complex, performance-driven design spaces. This paper presents a gamified decision-making framework that integrates game engines with real-time performance feedback. Performance criteria include structural behavior, environmental parameters, fabrication, material, and cost considerations. The developed design framework was tested with architecture students and non-expert designers on the design of an exoskeleton facade to retrofit an existing building. Participants (N=24) were able to iteratively modify façade geometries while receiving real-time feedback across the three key criteria: 1) structural behavior, including deflection, mass, and stress/strength ratio; 2) environmental parameters, such as solar gain and heating/cooling energy demands; and 3) fabrication considerations, including fabrication and material costs, robotic machining, and material setup. The evaluation of participant interactions reveals that gamified feedback mechanisms significantly enhance user comprehension and informed decision-making across the criteria. Further, participants' understanding of structural, material, and fabrication performance in relation to the iterative design task suggests that curated design spaces and structured guidance improve efficiency compared to open-ended generative tools. This research contributes to pre-occupancy evaluations, demonstrating how gamified environments enable stakeholder participation in the design process through informed decisionmaking and customized negotiation of performance criteria. .

</details>

---

### 11. [Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings](https://arxiv.org/abs/2603.04692)

**基本信息**

- 🔗 arXiv: [`2603.04692`](https://arxiv.org/abs/2603.04692)
- 👥 作者: Lyle Regenwetter, Rosen Yu, Cyril Picard 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04692.pdf)

**💡 相关性分析**

满足标准1和2：1）论文核心研究表格基础模型（TabPFN）在科学和工业领域（包括化学、材料等）回归任务中的领域适应和性能提升，属于“化学信息学”中模型应用的前沿问题。2）论文提出了TREDBench基准数据集和一种新的合成数据筛选方法，为在数据稀缺的科学领域（如化学）训练和评估基础模型提供了数据集和方法论资源。

**📖 中文摘要**

本文研究了表格数据基础模型在工程回归任务中的领域适应问题。作者发现，工程数据集与非工程数据集在表示空间中部分可区分，而程序生成的数据集与工程数据集之间存在显著的合成-真实领域差距。为了在不使用真实工程样本的情况下弥合这一差距，作者提出了一种嵌入引导的合成数据筛选方法：生成并识别“类工程”的合成数据集，并仅使用选定的合成任务对TabPFN 2.5进行持续预训练。在35个工程回归数据集上的评估表明，这种仅使用合成数据的适应方法提高了预测准确性和数据效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression datasets with expert engineering/non-engineering labels, and use TabPFN 2.5's dataset-level embedding to study domain structure in a common representation space. We find that engineering datasets are partially distinguishable from non-engineering datasets, while standard procedurally generated datasets are highly distinguishable from engineering datasets, revealing a substantial synthetic-real domain gap. To bridge this gap without training on real engineering samples, we propose an embedding-guided synthetic data curation method: we generate and identify "engineering-like" synthetic datasets, and perform continued pre-training of TabPFN 2.5 using only the selected synthetic tasks. Across 35 engineering regression datasets, this synthetic-only adaptation improves predictive accuracy and data efficiency, outperforming TabPFN 2.5 on 29/35 datasets and AutoGluon on 27/35, with mean multiplicative data-efficiency gains of 1.75x and 4.44x, respectively. More broadly, our results indicate that principled synthetic data curation can convert procedural generators into domain-relevant "data engines," enabling foundation models to improve in data-sparse scientific and industrial domains where real data collection is the primary bottleneck.

</details>

---

### 12. [Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery](https://arxiv.org/abs/2603.04735)

**基本信息**

- 🔗 arXiv: [`2603.04735`](https://arxiv.org/abs/2603.04735)
- 👥 作者: Michael P. Brenner, Vincent Cohen-Addad, David Woodruff
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04735.pdf)

**💡 相关性分析**

满足标准1：论文的核心是使用AI（大语言模型）辅助解决理论物理中的复杂数学问题（推导积分解析解）。这展示了“大模型”在科学发现和复杂符号推理方面的能力。虽然领域是物理，但其“使用大模型进行科学计算和公式推导”的核心主题与“化学大模型”用于辅助化学研究（如反应预测、性质计算）在方法论和精神上高度一致。

**📖 中文摘要**

本文展示了一个结合Gemini Deep Think大语言模型、系统化树搜索框架和自动化数值反馈的神经符号系统，成功推导出了宇宙弦引力辐射功率谱的新颖精确解析解。具体来说，智能体评估了任意环几何的核心积分I(N, α)，直接改进了近期仅产生部分渐近解的AI辅助尝试。作者详细介绍了引导模型的系统提示、搜索约束和间歇性反馈循环。智能体识别了6种不同的分析方法，其中最优雅的方法是用Gegenbauer多项式C_l^{(3/2)}展开核函数，以自然吸收被积函数的奇点。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper demonstrates that artificial intelligence can accelerate mathematical discovery by autonomously solving an open problem in theoretical physics. We present a neuro-symbolic system, combining the Gemini Deep Think large language model with a systematic Tree Search (TS) framework and automated numerical feedback, that successfully derived novel, exact analytical solutions for the power spectrum of gravitational radiation emitted by cosmic strings. Specifically, the agent evaluated the core integral $I(N,\alpha)$ for arbitrary loop geometries, directly improving upon recent AI-assisted attempts \cite{BCE+25} that only yielded partial asymptotic solutions. To substantiate our methodological claims regarding AI-accelerated discovery and to ensure transparency, we detail system prompts, search constraints, and intermittent feedback loops that guided the model. The agent identified a suite of 6 different analytical methods, the most elegant of which expands the kernel in Gegenbauer polynomials $C_l^{(3/2)}$ to naturally absorb the integrand's singularities. The methods lead to an asymptotic result for $I(N,\alpha)$ at large $N$ that both agrees with numerical results and also connects to the continuous Feynman parameterization of Quantum Field Theory. We detail both the algorithmic methodology that enabled this discovery and the resulting mathematical derivations.

</details>

---

### 13. [Distribution-Conditioned Transport](https://arxiv.org/abs/2603.04736)

**基本信息**

- 🔗 arXiv: [`2603.04736`](https://arxiv.org/abs/2603.04736)
- 👥 作者: Nic Fishman, Gokul Gowri, Paolo L. B. Fischer 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04736.pdf)

**💡 相关性分析**

满足标准1和2：1）论文的核心是开发一种通用的、可泛化的分布间映射（传输）模型，这对于化学信息学中的多个任务至关重要，例如将一种实验条件下的质谱数据映射到另一种条件，或跨不同仪器/协议的数据对齐。2）论文提出的DCT框架本身是一个新的工具，可用于处理化学和生物数据中的分布偏移和匹配问题，为质谱数据标准化、跨数据集分析等提供了方法论资源。

**📖 中文摘要**

本文提出了分布条件传输（DCT），一个将传输图条件化于源和目标分布的学习嵌入框架，从而能够泛化到未见过的分布对。DCT还支持分布预测问题的半监督学习。DCT与底层传输机制无关，支持从流匹配到基于分布散度的模型（如Wasserstein, MMD）。作者在合成基准和四个生物学应用中展示了DCT的实际性能优势：单细胞基因组学中的批次效应转移、从质谱流式数据预测扰动、学习造血中的克隆转录动力学以及建模T细胞受体序列进化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning a transport model that maps a source distribution to a target distribution is a canonical problem in machine learning, but scientific applications increasingly require models that can generalize to source and target distributions unseen during training. We introduce distribution-conditioned transport (DCT), a framework that conditions transport maps on learned embeddings of source and target distributions, enabling generalization to unseen distribution pairs. DCT also allows semi-supervised learning for distributional forecasting problems: because it learns from arbitrary distribution pairs, it can leverage distributions observed at only one condition to improve transport prediction. DCT is agnostic to the underlying transport mechanism, supporting models ranging from flow matching to distributional divergence-based models (e.g. Wasserstein, MMD). We demonstrate the practical performance benefits of DCT on synthetic benchmarks and four applications in biology: batch effect transfer in single-cell genomics, perturbation prediction from mass cytometry data, learning clonal transcriptional dynamics in hematopoiesis, and modeling T-cell receptor sequence evolution.

</details>

---

### 14. [CONE: Embeddings for Complex Numerical Data Preserving Unit and Variable Semantics](https://arxiv.org/abs/2603.04741)

**基本信息**

- 🔗 arXiv: [`2603.04741`](https://arxiv.org/abs/2603.04741)
- 👥 作者: Gyanendra Shrestha, Anna Pyayt, Michael Gubanov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04741.pdf)

**💡 相关性分析**

满足标准2：论文提出了CONE模型，专门用于编码数字、范围和带有单位的数值数据，并保持其语义和距离关系。这种能力对于化学信息学和质谱分析至关重要，因为该领域大量处理带有单位和物理意义的数值数据（如质荷比、强度、浓度、化学位移等）。CONE为处理和嵌入此类结构化化学数据提供了专门的工具资源。

**📖 中文摘要**

本文提出了CONE，一个混合Transformer编码器预训练模型，用于将数字、范围和正态分布编码到保持距离的嵌入向量空间中。作者引入了一种新颖的复合嵌入构建算法，该算法将数值、范围或正态分布与其关联的单位和属性名称集成在一起，以精确捕捉其复杂的语义。在涵盖不同领域（网络、医疗、金融和政府）的大规模数据集上进行的大量实验评估证明了CONE强大的数值推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large pre-trained models (LMs) and Large Language Models (LLMs) are typically effective at capturing language semantics and contextual relationships. However, these models encounter challenges in maintaining optimal performance on tasks involving numbers. Blindly treating numerical or structured data as terms is inadequate -- their semantics must be well understood and encoded by the models. In this paper, we propose CONE, a hybrid transformer encoder pre-trained model that encodes numbers, ranges, and gaussians into an embedding vector space preserving distance. We introduce a novel composite embedding construction algorithm that integrates numerical values, ranges or gaussians together with their associated units and attribute names to precisely capture their intricate semantics. We conduct extensive experimental evaluation on large-scale datasets across diverse domains (web, medical, finance, and government) that justifies CONE's strong numerical reasoning capabilities, achieving an F1 score of 87.28% on DROP, a remarkable improvement of up to 9.37% in F1 over state-of-the-art (SOTA) baselines, and outperforming major SOTA models with a significant Recall@10 gain of up to 25%.

</details>

---

### 15. [Evaluating GPT-5 as a Multimodal Clinical Reasoner: A Landscape Commentary](https://arxiv.org/abs/2603.04763)

**基本信息**

- 🔗 arXiv: [`2603.04763`](https://arxiv.org/abs/2603.04763)
- 👥 作者: Alexandru Florea, Shansong Wang, Mingzhe Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04763.pdf)

**💡 相关性分析**

满足标准1：论文的核心是评估最新的大语言模型（GPT-5）在多模态科学数据（医学影像和文本）上的复杂推理能力。虽然领域是医学，但其评估的“大模型处理多模态科学数据并进行综合推理”的能力，与“化学大模型”处理质谱、分子结构、文献等多模态信息以进行结构推理或性质预测的主题直接相关。这属于大模型在科学领域应用的前沿研究。

**📖 中文摘要**

本文对GPT-5系列模型在临床医学推理任务上进行了首次受控的横断面评估，任务范围包括医学教育考试、基于文本的推理基准，以及神经放射学、数字病理学和乳腺X线摄影的视觉问答。GPT-5在专家级文本推理上表现出显著进步，在MedXpertQA上绝对改进超过25个百分点。在多模态合成任务中，GPT-5有效地利用这种增强的推理能力，将不确定的临床叙述建立在具体的影像证据上，在大多数VQA基准上达到了最先进或具有竞争力的性能。研究结果表明，GPT-5在整合多模态临床推理方面取得了有意义的进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The transition from task-specific artificial intelligence toward general-purpose foundation models raises fundamental questions about their capacity to support the integrated reasoning required in clinical medicine, where diagnosis demands synthesis of ambiguous patient narratives, laboratory data, and multimodal imaging. This landscape commentary provides the first controlled, cross-sectional evaluation of the GPT-5 family (GPT-5, GPT-5 Mini, GPT-5 Nano) against its predecessor GPT-4o across a diverse spectrum of clinically grounded tasks, including medical education examinations, text-based reasoning benchmarks, and visual question-answering in neuroradiology, digital pathology, and mammography using a standardized zero-shot chain-of-thought protocol. GPT-5 demonstrated substantial gains in expert-level textual reasoning, with absolute improvements exceeding 25 percentage-points on MedXpertQA. When tasked with multimodal synthesis, GPT-5 effectively leveraged this enhanced reasoning capacity to ground uncertain clinical narratives in concrete imaging evidence, achieving state-of-the-art or competitive performance across most VQA benchmarks and outperforming GPT-4o by margins of 10-40% in mammography tasks requiring fine-grained lesion characterization. However, performance remained moderate in neuroradiology (44% macro-average accuracy) and lagged behind domain-specific models in mammography, where specialized systems exceed 80% accuracy compared to GPT-5's 52-64%. These findings indicate that while GPT-5 represents a meaningful advance toward integrated multimodal clinical reasoning, mirroring the clinician's cognitive process of biasing uncertain information with objective findings, generalist models are not yet substitutes for purpose-built systems in highly specialized, perception-critical tasks.

</details>

---

### 16. [Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator](https://arxiv.org/abs/2603.04797)

**基本信息**

- 🔗 arXiv: [`2603.04797`](https://arxiv.org/abs/2603.04797)
- 👥 作者: Cong Li, Yihan Yin, Chenhao Xue 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04797.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕优化大语言模型（LLM）的推理服务，而“化学大模型”是LLM在化学领域的特定应用。论文提出的分布式注意力执行和KV缓存管理技术是支撑大模型（包括化学领域大模型）高效运行的基础设施，因此与“化学大模型”这一主题直接相关。

**📖 中文摘要**

本文提出Helios，一种基于混合键合的LLM服务加速器硬件-软件协同设计。虽然论文主要关注大语言模型（LLM）服务的基础设施优化，但其核心是解决LLM推理中的动态KV缓存管理和注意力计算问题。论文提出的“空间感知KV缓存分配机制”和分布式分块注意力执行流程，是优化大模型（包括潜在的化学大模型）推理效率和内存管理的关键技术。这些底层优化方法对于需要处理复杂图结构或序列数据的“化学大模型”和“质谱结构推理”任务具有重要的借鉴意义，可以提升此类模型的服务效率和可扩展性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been widely deployed for online generative services, where numerous LLM instances jointly handle workloads with fluctuating request arrival rates and variable request lengths. To efficiently execute coexisting compute-intensive and memory-intensive operators, near-memory processing (NMP) based computing paradigm has been extensively proposed. However, existing NMP designs adopt coarse-grained KV cache management and inflexible attention execution flow. Such limitations hinder these proposals from efficiently handling \textit{highly dynamic} LLM serving workloads, limiting their ability to accelerate LLM serving. To tackle these problems, we propose Helios, a Hybrid-bonding-based \uline{L}LM \uline{S}erving accelerator. Helios aims to bridge the fundamental gap between the dynamic nature of KV cache management in LLM serving and the distributed, non-uniform memory abstraction among NMP processing engines (PEs). To this end, we design both the intra-PE execution flow and the inter-PE communication primitives for distributed tiled attention execution. We further propose \textit{spatially-aware} KV cache allocation mechanism to balance the attention workload distribution while minimizing the inter-PE data transfer overhead. Compared with existing GPU/NMP designs, Helios achieves 3.25 times (geomean) speedup and 3.36 times (geomean) better energy efficiency, along with up to 72%/76% P50/P99 time-between-tokens degradation.

</details>

---

### 17. [Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm](https://arxiv.org/abs/2603.04799)

**基本信息**

- 🔗 arXiv: [`2603.04799`](https://arxiv.org/abs/2603.04799)
- 👥 作者: Nan Hou, Kangfei Zhao, Jiadong Xie 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04799.pdf)

**💡 相关性分析**

满足标准1：论文提出的“亚线性语义过滤框架”是一种面向大模型的高效推理方法。这种方法论可以迁移应用于“质谱结构推理”任务，用于从庞大的化学结构数据库中高效筛选候选结构，因此与核心主题相关。

**📖 中文摘要**

本文针对大语言模型（LLM）在语义查询处理中的线性调用瓶颈，提出了一个名为CSV（聚类-采样-投票）的新框架。该框架通过将元组嵌入到语义簇中、采样少量子集进行LLM评估，并通过投票策略推断簇级标签，从而将LLM调用复杂度降低到亚线性。虽然论文的应用场景是通用表格数据的语义过滤，但其核心方法论——利用嵌入进行语义聚类、采样以减少对大模型的调用——对于处理海量化合物质谱数据具有直接的启发性。在“质谱结构推理”任务中，经常需要从大量候选结构中筛选出与质谱匹配的目标，CSV框架提供了一种高效减少推理计算成本的可能路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are increasingly used for semantic query processing over large corpora. A set of semantic operators derived from relational algebra has been proposed to provide a unified interface for expressing such queries, among which the semantic filter operator serves as a cornerstone. Given a table T with a natural language predicate e, for each tuple in the relation, the execution of a semantic filter proceeds by constructing an input prompt that combines the predicate e with its content, querying the LLM, and obtaining the binary decision. However, this tuple-by-tuple evaluation necessitates a complete linear scan of the table, incurring prohibitive latency and token costs. Although recent work has attempted to optimize semantic filtering, it still does not break the linear LLM invocation barriers. To address this, we propose Clustering-Sampling-Voting (CSV), a new framework that reduces LLM invocations to sublinear complexity while providing error guarantees. CSV embeds tuples into semantic clusters, samples a small subset for LLM evaluation, and infers cluster-level labels via two proposed voting strategies: UniVote, which aggregates labels uniformly, and SimVote, which weights votes by semantic similarity. Moreover, CSV triggers re-clustering on ambiguous clusters to ensure robustness across diverse datasets. The results conducted on real-world datasets demonstrate that CSV reduces the number of LLM calls by 1.28-355x compared to the state-of-the-art approaches, while maintaining comparable effectiveness in terms of Accuracy and F1 score.

</details>

---

### 18. [MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models](https://arxiv.org/abs/2603.04800)

**基本信息**

- 🔗 arXiv: [`2603.04800`](https://arxiv.org/abs/2603.04800)
- 👥 作者: Lulu Hu, Wenhu Xiao, Xin Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04800.pdf)

**💡 相关性分析**

满足标准1：论文专注于多模态大语言模型（MLLM）的量化技术。考虑到“化学大模型”和“质谱结构推理”可能涉及分子结构、光谱数据、文本知识等多模态信息的融合与处理，该论文提出的量化框架与未来化学领域多模态大模型的优化与部署这一核心主题直接相关。

**📖 中文摘要**

本文提出了MASQuant，一种用于多模态大语言模型（MLLM）的后训练量化框架。论文指出，将现有的LLM量化技术（如SmoothQuant）直接应用于MLLM会遇到“平滑错位”和“跨模态计算不变性”两大挑战。为此，MASQuant引入了模态感知平滑和跨模态补偿机制，以实现对双模态和三模态MLLM的稳定量化。虽然论文聚焦于视觉-语言模型，但其解决多模态数据量化问题的核心思想——为不同模态学习独立的平滑因子并使用SVD白化来统一量化——对于未来可能出现的、整合了质谱、分子图、文本描述等多模态信息的“化学大模型”具有前瞻性的参考价值。量化技术是部署大型模型的关键，此工作为化学领域多模态大模型的轻量化部署提供了技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Post-training quantization (PTQ) with computational invariance for Large Language Models~(LLMs) have demonstrated remarkable advances, however, their application to Multimodal Large Language Models~(MLLMs) presents substantial challenges. In this paper, we analyze SmoothQuant as a case study and identify two critical issues: Smoothing Misalignment and Cross-Modal Computational Invariance. To address these issues, we propose Modality-Aware Smoothing Quantization (MASQuant), a novel framework that introduces (1) Modality-Aware Smoothing (MAS), which learns separate, modality-specific smoothing factors to prevent Smoothing Misalignment, and (2) Cross-Modal Compensation (CMC), which addresses Cross-modal Computational Invariance by using SVD whitening to transform multi-modal activation differences into low-rank forms, enabling unified quantization across modalities. MASQuant demonstrates stable quantization performance across both dual-modal and tri-modal MLLMs. Experimental results show that MASQuant is competitive among the state-of-the-art PTQ algorithms. Source code: this https URL .

</details>

---

### 19. [Attention's Gravitational Field:A Power-Law Interpretation of Positional Correlation](https://arxiv.org/abs/2603.04805)

**基本信息**

- 🔗 arXiv: [`2603.04805`](https://arxiv.org/abs/2603.04805)
- 👥 作者: Edward Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）的基础机制（注意力、位置编码）的理论探索与优化。这些基础性改进是构建更高效、更精准的领域大模型（包括化学大模型）的基石，因此与“化学大模型”主题相关。

**📖 中文摘要**

本文探索了大语言模型（LLM）中位置关系与编码的底层原理，并引入了“注意力引力场”的概念。通过将位置编码与语义嵌入解耦来优化模型架构，取得了优于主流编码方法的准确率。论文对AGF进行了深入分析，展示了其与学习/稳定性曲线的内在一致性，以及与牛顿万有引力定律的经验对齐。这项工作为理解注意力机制和模型优化提供了新的理论视角。虽然论文是基础性研究，但其对LLM内部机制（如注意力、位置编码）的深入理解和优化，为构建更强大、更可解释的“化学大模型”（例如，用于理解分子序列或光谱序列中的长程依赖关系）提供了理论基础和方法启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper explores the underlying principles of positional relationships and encodings within Large Language Models (LLMs) and introduces the concept of the Attention Gravitational Field (AGF). By decoupling positional encodings from semantic embeddings, we optimize the model architecture and achieve superior accuracy compared to prevailing encoding methods. Furthermore, we provide an in-depth analysis of AGF, demonstrating its intrinsic consistency with learning and stability curves, as well as its empirical alignment with Newton's Law of Universal Gravitation. By offering a rigorous theoretical exploration of these phenomena, this work represents a significant step toward interpreting the Attention mechanism and unlocks new possibilities for future research in model optimization and interpretability.

</details>

---

### 20. [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827)

**基本信息**

- 🔗 arXiv: [`2603.04827`](https://arxiv.org/abs/2603.04827)
- 👥 作者: Ben S. Southworth, Jonas A. Actor, Graham Harper 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04827.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种针对柯尔莫哥洛夫-阿诺德网络（KAN）的高效多级训练算法。KAN作为一种具有强可解释性和潜在高精度的新型网络架构，非常适合用于科学计算和推理任务，包括“化学大模型”和“质谱结构推理”。因此，该训练方法与核心主题直接相关。

**📖 中文摘要**

本文针对柯尔莫哥洛夫-阿诺德网络（KAN）提出了一种多级训练算法，以利用其基于基函数展开的结构化特性来加速训练。论文首先建立了使用样条基函数的KAN与使用幂ReLU激活函数的多通道MLP之间的等价关系，并分析了基变换对优化几何的影响。基于此，提出了通过样条节点的均匀细化自然定义一系列KAN，并使用解析几何插值算子在模型间传递知识的训练方法。实验表明，该方法在训练可比KAN或MLP时，能获得数量级上的精度提升。KAN作为一种新兴的、可解释性更强的神经网络架构，其在物理信息神经网络（PINN）中的成功应用，暗示了它在解决化学、物理等科学计算问题上的潜力。本文的高效训练方法为将KAN应用于“化学大模型”或“质谱结构推理”这类需要高精度和可解释性的任务提供了有力的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

</details>

---

### 21. [From Unfamiliar to Familiar: Detecting Pre-training Data via Gradient Deviations in Large Language Models](https://arxiv.org/abs/2603.04828)

**基本信息**

- 🔗 arXiv: [`2603.04828`](https://arxiv.org/abs/2603.04828)
- 👥 作者: Ruiqi Zhang, Lingxiang Wang, Hainan Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04828.pdf)

**💡 相关性分析**

满足标准1：论文研究LLM预训练数据检测，这是构建、审计和管理大模型（包括化学领域大模型）的关键技术。确保化学大模型训练数据的纯净性、避免基准污染，对于其科学可靠性至关重要，因此该研究与核心主题相关。

**📖 中文摘要**

本文从优化视角出发，研究了大语言模型（LLM）的预训练数据检测问题。论文观察到，在训练过程中，样本从“不熟悉”到“熟悉”的转变会体现在梯度行为的系统性差异上。基于此洞察，提出了GDS方法，通过探测目标样本的梯度偏差分数来识别预训练数据。具体而言，GDS利用梯度剖面（捕捉FFN和注意力模块中参数更新的幅度、位置和集中度）来表征每个样本，并输入轻量级分类器进行成员推断。实验表明GDS在跨数据集可转移性上显著优于强基线。这项工作对于管理“化学大模型”的训练数据版权、评估模型在特定化学数据集上的污染情况、以及确保模型推理的可靠性具有重要价值，是构建负责任化学AI的基础技术之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pre-training data detection for LLMs is essential for addressing copyright concerns and mitigating benchmark contamination. Existing methods mainly focus on the likelihood-based statistical features or heuristic signals before and after fine-tuning, but the former are susceptible to word frequency bias in corpora, and the latter strongly depend on the similarity of fine-tuning data. From an optimization perspective, we observe that during training, samples transition from unfamiliar to familiar in a manner reflected by systematic differences in gradient behavior. Familiar samples exhibit smaller update magnitudes, distinct update locations in model components, and more sharply activated neurons. Based on this insight, we propose GDS, a method that identifies pre-training data by probing Gradient Deviation Scores of target samples. Specifically, we first represent each sample using gradient profiles that capture the magnitude, location, and concentration of parameter updates across FFN and Attention modules, revealing consistent distinctions between member and non-member data. These features are then fed into a lightweight classifier to perform binary membership inference. Experiments on five public datasets show that GDS achieves state-of-the-art performance with significantly improved cross-dataset transferability over strong baselines. Further interpretability analyse show gradient feature distribution differences, enabling practical and scalable pre-training data detection.

</details>

---

### 22. [Why Is RLHF Alignment Shallow? A Gradient Analysis](https://arxiv.org/abs/2603.04851)

**基本信息**

- 🔗 arXiv: [`2603.04851`](https://arxiv.org/abs/2603.04851)
- 👥 作者: Robin Young
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04851.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）安全对齐机制的深度理论分析。如何对齐“化学大模型”，使其输出符合化学规则、安全规范和科学伦理，是该领域面临的关键挑战。因此，这项关于对齐深度与改进方法的基础研究与核心主题高度相关。

**📖 中文摘要**

本文通过梯度分析，从理论上解释了为什么基于人类反馈的强化学习（RLHF）对大语言模型的安全对齐是“浅层”的。论文证明，基于梯度的对齐本质上集中在决定危害的位置，并在此之后消失。作者引入了“危害信息”的概念来量化每个位置对危害的影响，并证明均衡的KL散度跟踪这个量。最后，论文推导了一个基于恢复惩罚的目标，该目标在所有位置创建梯度信号。这项研究深入揭示了当前大模型对齐方法的局限性，并提出了改进方向。对于旨在构建安全、可靠、符合科学伦理的“化学大模型”（例如，避免生成有害化合物或错误的结构预测）而言，理解对齐机制的深度和局限性，并探索更有效的对齐方法，具有根本性的重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Why is safety alignment in LLMs shallow? We prove that gradient-based alignment inherently concentrates on positions where harm is decided and vanishes beyond. Using a martingale decomposition of sequence-level harm, we derive an exact characterization of alignment gradients. The gradient at position $t$ equals the covariance between the conditional expected harm and the score function. This implies that positions beyond the harm horizon where the output's harmfulness is already determined receive zero gradient signal during training. This explains empirical observations that KL divergence between aligned and base models concentrates on early tokens. Consequently, standard alignment objectives cannot produce deep alignment, regardless of optimization quality. We introduce the concept of harm information $I_t$, which quantifies each position's influence on harm, and prove that equilibrium KL divergence tracks this quantity. Finally, we derive an objective based on recovery penalties that creates gradient signal at all positions, providing theoretical grounding for empirically successful data augmentation techniques.

</details>

---

### 23. [On Multi-Step Theorem Prediction via Non-Parametric Structural Priors](https://arxiv.org/abs/2603.04852)

**基本信息**

- 🔗 arXiv: [`2603.04852`](https://arxiv.org/abs/2603.04852)
- 👥 作者: Junbo Zhao, Ting Zhang, Can Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04852.pdf)

**💡 相关性分析**

满足标准1：论文研究如何通过引入显式结构先验来增强大语言模型（LLM）的多步符号推理能力。“质谱结构推理”本质上是一个需要多步逻辑推导的复杂符号推理问题，该论文的方法论为改进化学领域的结构推理模型提供了直接的技术参考。

**📖 中文摘要**

本文探索了通过上下文学习（ICL）进行免训练的多步定理预测。论文指出了“结构漂移”这一关键的可扩展性瓶颈，即随着推理深度增加，普通ICL的性能会急剧下降。为解决此问题，提出了“定理先序图”，将历史解轨迹中的时间依赖编码为有向图，并在推理过程中施加明确的结构约束以剪枝搜索空间。结合检索增强的图构建和逐步符号执行器，该方法使LLM能够作为结构化规划器而无需任何基于梯度的优化。在FormalGeo7k基准测试中达到了最先进的精度。这项研究展示了如何为LLM注入显式的结构先验来增强其符号推理能力。这对于“质谱结构推理”这类需要严格、多步逻辑推导（从质谱峰推导出化学键和官能团）的任务具有重要的方法论启示，为构建更可靠、可解释的化学推理模型提供了思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-step theorem prediction is a central challenge in automated reasoning. Existing neural-symbolic approaches rely heavily on supervised parametric models, which exhibit limited generalization to evolving theorem libraries. In this work, we explore training-free theorem prediction through the lens of in-context learning (ICL). We identify a critical scalability bottleneck, termed Structural Drift: as reasoning depth increases, the performance of vanilla ICL degrades sharply, often collapsing to near zero. We attribute this failure to the LLM's inability to recover latent topological dependencies, leading to unstructured exploration. To address this issue, we propose Theorem Precedence Graphs, which encode temporal dependencies from historical solution traces as directed graphs, and impose explicit topological constraints that effectively prune the search space during inference. Coupled with retrieval-augmented graph construction and a stepwise symbolic executor, our approach enables LLMs to act as structured planners without any gradient-based optimization. Experiments on the FormalGeo7k benchmark show that our method achieves 89.29% accuracy, substantially outperforming ICL baselines and matching state-of-the-art supervised models. These results indicate that explicit structural priors offer a promising direction for scaling LLM-based symbolic reasoning.

</details>

---

### 24. [Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models](https://arxiv.org/abs/2603.04893)

**基本信息**

- 🔗 arXiv: [`2603.04893`](https://arxiv.org/abs/2603.04893)
- 👥 作者: Sean Lamont, Christian Walder, Paul Montague 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04893.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种提升扩散语言模型生成多样性的高效方法。生成多样性是“化学大模型”在分子设计、逆合成规划和“质谱结构推理”中生成多个合理候选结构的关键需求，因此该技术与核心主题直接相关。

**📖 中文摘要**

本文针对扩散语言模型，提出了一种无需训练、低成本的干预措施来增强生成多样性。该方法在批次中顺序修改中间样本，使每个样本在特征空间中被先前样本“排斥”，从而主动惩罚冗余。与需要重新训练或波束搜索的先前方法不同，该策略计算开销可忽略，同时确保每个样本为批次提供独特的视角。在HumanEval和GSM8K基准测试上的评估表明，该方法显著提高了多样性和Pass@k性能。对于“化学大模型”和“质谱结构推理”任务，生成多样性至关重要。例如，在基于质谱推理化学结构时，需要模型能够生成多种合理的候选结构以供进一步验证。该论文提供了一种简单有效的方法来提升扩散模型在开放域生成任务中的多样性，可直接应用于化学结构生成或候选结构扩增等场景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diverse outputs in text generation are necessary for effective exploration in complex reasoning tasks, such as code generation and mathematical problem solving. Such Pass@$k$ problems benefit from distinct candidates covering the solution space. However, traditional sampling approaches often waste computational resources on repetitive failure modes. While Diffusion Language Models have emerged as a competitive alternative to the prevailing Autoregressive paradigm, they remain susceptible to this redundancy, with independent samples frequently collapsing into similar modes. To address this, we propose a training free, low cost intervention to enhance generative diversity in Diffusion Language Models. Our approach modifies intermediate samples in a batch sequentially, where each sample is repelled from the feature space of previous samples, actively penalising redundancy. Unlike prior methods that require retraining or beam search, our strategy incurs negligible computational overhead, while ensuring that each sample contributes a unique perspective to the batch. We evaluate our method on the HumanEval and GSM8K benchmarks using the LLaDA-8B-Instruct model. Our results demonstrate significantly improved diversity and Pass@$k$ performance across various temperature settings. As a simple modification to the sampling process, our method offers an immediate, low-cost improvement for current and future Diffusion Language Models in tasks that benefit from diverse solution search. We make our code available at this https URL .

</details>

---

### 25. [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900)

**基本信息**

- 🔗 arXiv: [`2603.04900`](https://arxiv.org/abs/2603.04900)
- 👥 作者: Shuo Yang, Soyeon Caren Han, Xueqi Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04900.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个用于优化大语言模型智能体工具使用策略的自进化框架。构建能够有效利用化学信息学工具和数据库的AI智能体，是推进“化学大模型”和自动化“质谱结构推理”的重要方向，因此该框架与核心主题相关。

**📖 中文摘要**

本文提出了EvoTool，一个通过无梯度进化范式优化模块化工具使用策略的自进化框架。EvoTool将智能体的工具使用策略分解为四个模块，并通过三个新机制在自改进循环中迭代优化它们。在四个基准测试中，EvoTool在GPT-4.1和Qwen3-8B上都显著优于强基线。这项工作展示了如何通过模块化设计和进化优化来提升LLM智能体使用工具（包括可能用于化学信息学或质谱分析的专用工具）的能力。对于构建能够自主调用化学数据库、计算软件或光谱解析工具来完成“质谱结构推理”等复杂任务的化学AI智能体，EvoTool提供了一个强大的策略优化框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

</details>

---

### 26. [$\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](https://arxiv.org/abs/2603.04948)

**基本信息**

- 🔗 arXiv: [`2603.04948`](https://arxiv.org/abs/2603.04948)
- 👥 作者: Peihao Wang, Ruisi Cai, Zhen Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04948.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种在推理时利用梯度下降优化LLM生成策略的新框架。这种将优化深度集成到推理过程中的方法，为提升“化学大模型”在复杂任务（如质谱结构推理）中的精度和效率提供了新颖且强大的技术路径。

**📖 中文摘要**

本文提出了$\nabla$-Reasoner，一种将可微分优化集成到解码循环中的迭代生成框架，以在推理时动态优化策略。其核心组件“可微分文本优化”（DTO）利用来自LLM似然和奖励模型的梯度信号来优化文本表示。理论上，论文证明了在样本空间中进行推理时梯度下降以最大化奖励，与通过KL正则化强化学习对齐LLM策略是对偶的。实证上，$\nabla$-Reasoner在具有挑战性的数学推理基准上实现了超过20%的准确率提升。这项工作引入了从零阶搜索到一阶优化的范式转变，为增强LLM推理提供了一条经济有效的路径。这种在推理时利用梯度信息进行精细优化的思想，可以应用于“化学大模型”的推理过程，例如，在质谱解析中迭代优化对分子结构的假设，从而提升推理的准确性和效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

</details>

---

### 27. [Programmable superconducting neuron with intrinsic in-memory computation and dual-timescale plasticity for ultra-efficient neuromorphic computing](https://arxiv.org/abs/2603.04966)

**基本信息**

- 🔗 arXiv: [`2603.04966`](https://arxiv.org/abs/2603.04966)
- 👥 作者: Muen Wang, Shucheng Yang, Yuxiang Lin 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04966.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新型的可编程超导神经元硬件单元，该单元具有事件驱动、内存内计算和双时间尺度可塑性等特性。这种底层计算架构和硬件资源，为构建高效的、处理复杂时序数据（如质谱信号）的专用计算系统或加速相关模型推理提供了潜在的硬件工具和实现路径。

**📖 中文摘要**

本文提出了一种可编程的超导神经元，用于构建超高效、超高速的神经形态计算架构。该神经元集成了固有的静态内存和精确的可编程性，并支持双时间尺度的可塑性。虽然论文的核心是硬件和计算架构，但其提出的“事件驱动、内存内神经形态架构”以及用于构建SNN的单元，为构建高效的、事件驱动的计算系统提供了基础。这种底层计算架构和单元设计，可以被视为一种潜在的“工具”或“资源”，用于支持需要高效处理时序和事件数据的高级模型，例如处理质谱数据流或构建化学信息学中的专用计算模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The escalating energy demands of artificial intelligence pose a critical challenge to conventional computing. Leveraging the efficiency of event-driven, in-memory neuromorphic architectures into the superconducting circuits with ultra-high speed and low power dissipation advantages offers a promising solution to energy-efficient computing. However, the potential of such a solution has yet to be realized, owning to the absence of a fundamental superconducting unit that unifies programmability, local memory, and multi-timescale plasticity. Here, we introduce a programmable Josephson-junction-based leaky integrate-and-fire (LIF) neuron that features intrinsic static memory and precise programmability by encoding somatic and synaptic parameters directly in the bias current. This neuron is also capable of dual-timescale plasticity: picosecond-scale short-term modulation of spike transmission and long-term weight retention exceeding 10,000 seconds, facilitating both rapid temporal adaptation and robust weight storage. It can operate up to 45 GHz with femtojoule-level energy dissipation per spike, and supports 10 somatic threshold levels and 20 synaptic states. Furthermore, we demonstrate a crossbar-based spiking neural network (SNN) utilizing this neuron, which achieves outstanding performance across multiple tasks. By fusing computation, memory and plasticity into a single superconducting unit, our work paves the way for the next generation of ultrafast, energy-efficient neuromorphic computing.

</details>

---

### 28. [Functionality-Oriented LLM Merging on the Fisher--Rao Manifold](https://arxiv.org/abs/2603.04972)

**基本信息**

- 🔗 arXiv: [`2603.04972`](https://arxiv.org/abs/2603.04972)
- 👥 作者: Jiayu Wang, Zuojun Ye, Wenpeng Yin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04972.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型（LLM）的权重空间合并技术。该技术是构建和优化“化学大模型”的关键环节之一，旨在将多个针对不同化学子任务微调的专家模型高效、稳定地合并为一个统一的、多功能的化学大模型，直接服务于化学信息学中模型集成与部署的需求。

**📖 中文摘要**

本文提出了一种在Fisher-Rao流形上进行模型权重合并的新方法，旨在将多个经过微调的大语言模型（LLM）的功能合并到一个单一模型中。该方法将模型合并问题形式化为计算加权Karcher均值，以最小化预测分布之间的KL散度距离。论文的核心是解决大模型（尤其是LLM）的权重空间合并问题，以提高合并后模型的稳定性和性能。这直接关系到“化学大模型”领域的一个关键实践问题：如何高效地整合针对不同化学任务（如分子性质预测、反应预测、质谱解析）微调的多个专家模型，形成一个统一且功能强大的化学大模型，而无需重新训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective. We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

</details>

---

### 29. [Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination](https://arxiv.org/abs/2603.05040)

**基本信息**

- 🔗 arXiv: [`2603.05040`](https://arxiv.org/abs/2603.05040)
- 👥 作者: Hyuntae Park, Yeachan Kim, SangKeun Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05040.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过整合机器生成的视觉信号来增强语言模型的零样本推理能力。这种方法论与“化学大模型”和“质谱结构推理”的研究高度相关。在化学信息学中，增强模型对分子结构（视觉/图信息）与质谱/文本描述之间的跨模态理解和推理能力，是提升结构解析准确性的关键途径之一。

**📖 中文摘要**

本文提出了一个名为Imagine的零样本常识推理框架，旨在通过整合机器生成的视觉知识来增强预训练语言模型（PLM）的推理能力。该框架的核心创新在于将图像生成器嵌入推理流程，为文本输入补充机器想象的视觉信号，以缓解文本知识中的人类报告偏差。论文通过构建合成数据集来模拟视觉问答场景，并在多个常识推理基准上验证了其有效性。虽然论文的评估领域是通用常识推理，但其核心方法论——利用多模态（文本+生成图像）信息来增强模型对复杂概念（对应化学结构、质谱图）的理解和推理——与“化学大模型”和“质谱结构推理”的研究思路高度契合。例如，在质谱结构推理中，结合分子结构图（或生成的候选结构图像）与质谱文本描述进行联合推理，是一个重要的研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

</details>

---

### 30. [Why Do You Contribute to Stack Overflow? Understanding Cross-Cultural Motivations and Usage Patterns before the Age of LLMs](https://arxiv.org/abs/2603.05043)

**基本信息**

- 🔗 arXiv: [`2603.05043`](https://arxiv.org/abs/2603.05043)
- 👥 作者: Sherlock A. Licorish, Elijah Zolduoarrati, Tony Savarimuthu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05043.pdf)

**💡 相关性分析**

满足标准2和3：论文提供了关于如何理解和激励社区贡献以构建高质量数据资源的深入分析（标准2）。同时，其关于跨文化知识共享行为的研究，对于思考如何在全球范围内组织和维护化学、质谱领域的专业数据集和知识库（这些是训练相关大模型的基础资源）具有重要的综述和展望价值（标准3）。

**📖 中文摘要**

本文研究了Stack Overflow贡献者在不同国家文化背景下的参与动机和平台活动模式。通过结合定性内容分析和定量语言分析，论文识别了17种动机类别，并分析了美国、中国和俄罗斯贡献者在自我推广、学习导向等行为上的差异。虽然论文主题是软件工程社区，但其研究方法和发现——关于知识贡献动机、数据质量、以及跨文化差异——对于构建和维护化学与质谱领域的专业数据集和知识库具有重要的启示意义。例如，在构建用于训练“化学大模型”或“质谱结构推理”模型的高质量数据集时，理解领域专家（如化学家、质谱分析师）的贡献动机、设计激励和协作机制，是确保数据资源可持续性和质量的关键。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding motivations of contributors for participating in community question and answer platforms is crucial for sustaining knowledge-sharing ecosystem, which is necessary to advance the discipline while also ensuring its longevity. This is particularly necessary in the age of LLMs, where data from such portals are used to train these models. Limited insights exist regarding how motivations of contributors vary across different national cultures. This research investigates Stack Overflow contributor motivations, analysing regional differences and relations to platform activity. We combined qualitative content analysis of Stack Overflow profiles with quantitative linguistic analysis of data from the United States, China, and Russia. Using deductive content analysis, we identified 17 motivational categories. We applied correlation analysis to identify associations between stated motivations and platform activities. Contributors are primarily motivated by advertising opportunities and altruistic problem solving desires. American contributors demonstrated stronger self promotional behaviours while Chinese contributors exhibited greater learning oriented engagement. Our correlation analysis showed that those with more detailed profiles tend to engage in advertising and social activities, while learning oriented users maintain minimal self presentation. Understanding these variations can inform strategies for enhancing cross cultural participation in software engineering.

</details>

---

### 31. [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)

**基本信息**

- 🔗 arXiv: [`2603.05044`](https://arxiv.org/abs/2603.05044)
- 👥 作者: Sicheng Fan, Qingyun Shi, Shengze Xu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05044.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种创新的、数据高效的智能体训练框架，该框架利用LLM知识和自动化的环境合成来生成训练数据。这种方法为解决化学信息学和质谱分析中高质量标注数据稀缺的挑战提供了潜在的工具和思路，可用于生成仿真的质谱数据或分子结构-性质关系数据，以辅助模型训练。

**📖 中文摘要**

本文提出了WebFactory，一个用于训练GUI智能体的全自动闭环强化学习框架。该框架通过可扩展的环境合成、知识感知的任务生成、LLM驱动的轨迹收集、分解奖励的RL训练和系统化的智能体评估，旨在将大语言模型中编码的互联网知识高效“压缩”为可操作的、基于环境的智能体行为。论文的核心是解决智能体训练中的数据效率和泛化能力问题。虽然应用场景是网页交互，但其方法论——特别是利用LLM的先验知识来生成合成训练数据、设计训练流程以高效地将潜在知识转化为具体技能——对于在数据稀缺的化学信息学领域（如需要大量标注的质谱-结构对）训练专用模型或智能体（例如，用于自动解析质谱的智能体）具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

</details>

---

### 32. [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046)

**基本信息**

- 🔗 arXiv: [`2603.05046`](https://arxiv.org/abs/2603.05046)
- 👥 作者: Rongzhi Li, Hitomi Yanaka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05046.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大语言模型的、基于神经元分析的混合专家（MoE）架构设计方法。这种方法论可以直接应用于“化学大模型”的架构设计中，用于高效地整合和处理化学领域内不同子领域（可类比为不同“语言”）的知识和任务，是构建专业化、高效能化学大模型的关键技术之一。

**📖 中文摘要**

本文提出了NeuronMoE，一种用于高效扩展大语言模型（LLM）到低资源语言的方法。该方法通过分析跨所有Transformer组件的语言特定神经元，来指导基于经验测量的跨语言神经元多样性为每一层分配专家（MoE）。论文在将Llama-3.2-3B扩展到希腊语、土耳其语和匈牙利语等低资源语言的实验中验证了其有效性。这项研究虽然针对多语言扩展，但其核心技术创新——基于神经元级分析来精细化设计混合专家（MoE）架构——对于构建“化学大模型”具有直接相关性。化学领域包含众多子领域（如有机化学、药物化学、分析化学），每个子领域可能对应不同的“语言”或表示模式。NeuronMoE提供了一种方法论，可以指导如何为化学大模型的不同模块或处理不同化学子任务的专家进行更精细、更高效的参数分配和架构设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We propose $\textbf{NeuronMoE}$, a method that analyzes language-specific neurons across all transformer components to guide expert allocation per layer based on empirically measured cross-lingual neuron diversity. Applied to Llama-3.2-3B for low-resource languages (Greek, Turkish, and Hungarian), this approach achieves approximately 40% average parameter reduction while matching the performance of the LayerMoE baseline. We find that low-resource language experts independently develop neuron specialization patterns mirroring the high-resource language, which are concentrated in early and late layers. This reveals potential universal architectural principles in how multilingual models organize linguistic knowledge.

</details>

---

### 33. [Cyber Threat Intelligence for Artificial Intelligence Systems](https://arxiv.org/abs/2603.05068)

**基本信息**

- 🔗 arXiv: [`2603.05068`](https://arxiv.org/abs/2603.05068)
- 👥 作者: Natalia Krawczyk, Mateusz Szczepkowski, Adrian Brodzik 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05068.pdf)

**💡 相关性分析**

满足标准2和3：论文系统地回顾和组织了针对AI系统的安全威胁知识，并提出了构建相应威胁情报知识库的框架（标准2）。这为部署“化学大模型”和“质谱结构推理”等AI系统时，确保其安全性和可靠性提供了重要的知识资源和安全指南，具有综述和前瞻性价值（标准3）。

**📖 中文摘要**

本文探讨了网络威胁情报（CTI）如何演进以应对针对人工智能（AI）系统的安全威胁。论文分析了传统CTI的假设和工作流程与AI防御需求之间的差距，回顾并组织了当前AI安全知识体系，并概述了面向AI的威胁情报知识库应包含的内容，包括针对AI供应链不同阶段和产物的具体入侵指标（IoC）。随着“化学大模型”和基于AI的“质谱结构推理”系统在科研和工业中的部署日益增多，其安全性（如模型窃取、数据投毒、对抗性攻击）至关重要。本文系统地梳理了AI系统特有的安全威胁和防御知识，为相关领域的研究者和开发者提供了重要的安全框架和资源参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) becomes deeply embedded in critical services and everyday products, it is increasingly exposed to security threats which traditional cyber defenses were not designed to handle. In this paper, we investigate how cyber threat intelligence (CTI) may evolve to address attacks that target AI systems. We first analyze the assumptions and workflows of conventional threat intelligence with the needs of AI-focused defense, highlighting AI-specific assets and vulnerabilities. We then review and organize the current landscape of AI security knowledge. Based on this, we outline what an AI-oriented threat intelligence knowledge base should contain, describing concrete indicators of compromise (IoC) for different AI supply-chain phases and artifacts, and showing how such a knowledge base could support security tools. Finally, we discuss techniques for measuring similarity between collected indicators and newly observed AI artifacts. The review reveals gaps and quality issues in existing resources and identifies potential future research directions toward a practical threat intelligence framework tailored to AI.

</details>

---

### 34. [TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling](https://arxiv.org/abs/2603.05094)

**基本信息**

- 🔗 arXiv: [`2603.05094`](https://arxiv.org/abs/2603.05094)
- 👥 作者: Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05094.pdf)

**💡 相关性分析**

满足标准2：论文提出并详细描述了一个针对特定领域（方言音频）的高质量多模态数据集的构建方法论和验证流程。这套数据收集、清洗、验证和扩充的协议与工具，可以直接借鉴用于构建化学信息学和质谱分析领域所需的专业数据集，例如大规模的质谱图-分子结构配对数据集，这是训练相关模型的关键资源。

**📖 中文摘要**

本文介绍了TW-Sound580K，一个通过验证-生成-批判（VGC）协议开发的台湾地区音频-文本指令数据集。该数据集旨在解决大音频语言模型（LALM）在处理地方方言韵律时因专业语料库稀缺而面临的困难。论文详细描述了利用双重ASR验证过滤原始音频、并使用教师模型扩展为高质量指令对的数据构建流程。此外，论文还展示了基于该数据集训练的Tai-LALM模型在当地方言语音理解任务上的性能提升。这项工作直接相关于构建高质量、特定领域的多模态数据集。对于“化学大模型”和“质谱结构推理”而言，高质量、大规模、标注良好的数据集（如质谱-分子结构对、化学反应文本-条件对）是模型训练和评估的基础。本论文提供了一套严谨的数据集构建、验证和扩充的方法论，可作为化学信息学领域构建专业数据资源的参考范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio-Language Models (LALMs) typically struggle with localized dialectal prosody due to the scarcity of specialized corpora. We present TW-Sound580K, a Taiwanese audio-text instruction dataset developed through a Verify-Generate-Critique (VGC) protocol. This pipeline leverages Dual-ASR validation to filter 522K raw clips, subsequently expanding them into 580,000 high-fidelity instruction pairs using a teacher model. The dataset's utility is demonstrated through Tai-LALM, which fine-tunes a DeSTA 2.5-Audio-initialized backbone and incorporates a dynamic Dual-ASR Arbitration strategy to optimize transcription selection during inference. On the TAU Benchmark, Tai-LALM reaches 49.1% accuracy, marking a 6.5% absolute improvement over the zero-shot baseline (42.6% with ASR text conditioning). This confirms that integrating regional corpora with rigorous curation and dynamic arbitration significantly enhances LALM performance on localized speech.

</details>

---

### 35. [Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning](https://arxiv.org/abs/2603.05120)

**基本信息**

- 🔗 arXiv: [`2603.05120`](https://arxiv.org/abs/2603.05120)
- 👥 作者: Boren Hu, Xiao Liu, Boci Peng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05120.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种创新的课程学习框架，能够动态生成适配模型当前能力的训练数据，以极高效的方式利用有限的数据资源提升模型性能。这种方法为解决化学信息学和质谱分析中高质量标注数据稀缺的普遍挑战，提供了一种强大的数据生成和课程设计工具与思路。

**📖 中文摘要**

本文提出了一个名为“双向课程生成”的多智能体框架，用于提升大语言模型在数学推理任务上的数据效率。该框架模拟自适应教学法，通过一个封闭的反馈循环动态生成训练数据：当模型表现良好时，智能体生成更复杂的问题进行挑战；当模型出现特定推理失败时，智能体则生成简化版问题以修复知识漏洞。这种方法旨在最大化每个训练样本的教学价值，优化学习轨迹。这项研究针对的是数学推理，但其核心思想——通过智能课程生成来高效利用有限数据、针对性强化模型薄弱环节——完全适用于数据获取成本高、标注困难的“化学大模型”和“质谱结构推理”领域。例如，可以设计智能体来为质谱解析模型动态生成从简单到复杂、或针对特定难点化合物类别的训练样本序列。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enhancing mathematical reasoning in Large Language Models typically demands massive datasets, yet data efficiency remains a critical bottleneck. While Curriculum Learning attempts to structure this process, standard unidirectional approaches (simple-to-complex) suffer from inefficient sample utilization: they blindly escalate complexity even when foundational gaps persist, leading to wasted computation on unsolvable problems. To maximize the instructional value of every training sample, we introduce a novel Bidirectional Curriculum Generation framework. Unlike rigid trajectories, our multi-agent ecosystem mimics adaptive pedagogy to establish a closed feedback loop. It dynamically generates data by either complicating problems to challenge the model or, crucially, simplying them to repair specific reasoning failures. This mechanism ensures that the model consumes only the most effective data at any given stage. Grounded in the Optimal Pacing Theorem, our approach optimizes the learning trajectory, significantly outperforming baselines while achieving superior reasoning performance with substantially fewer instruction samples.

</details>

---

### 36. [Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs](https://arxiv.org/abs/2603.05343)

**基本信息**

- 🔗 arXiv: [`2603.05343`](https://arxiv.org/abs/2603.05343)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进用于分子模拟的等变图神经网络（一种化学大模型），通过量化方法解决其计算瓶颈，同时保持其几何对称性。这与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一种用于保持SO(3)等变图神经网络（GNNs）连续对称性的几何感知量化（GAQ）框架。该研究针对分子模拟中的高计算成本和内存瓶颈问题，通过将不变长度与等变方向解耦的量化方案，在离散空间中严格保持连续对称性。实验在rMD17基准上进行，证明了该方法在保持几何保真度的同时，能显著加速推理并减少内存占用。这项工作直接改进了用于分子模拟的等变GNNs，这是化学信息学和质谱分析中用于分子结构表示和推理的核心模型类型，因此与“化学大模型”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

</details>

---

### 37. [On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395)

**基本信息**

- 🔗 arXiv: [`2603.05395`](https://arxiv.org/abs/2603.05395)
- 👥 作者: Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05395.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是层神经网络（Sheaf Neural Networks），这是图神经网络的一种变体。图神经网络是构建“化学大模型”（用于分子表示学习）的基础架构之一。因此，对这类网络基础性质（如过平滑、归纳偏置）的研究与化学大模型的主题相关。

**📖 中文摘要**

本文研究了层神经网络（SNNs）在异配图上的表现，并引入了一个身份层网络基线（所有限制映射固定为恒等映射）。研究通过消融实验，探讨了学习限制映射对于缓解过平滑问题是否必要。论文在五个流行的异配图基准上进行了评估，发现身份基线取得了与多种SNN变体相当的性能。这项工作对层神经网络（一种用于处理图结构数据的神经网络架构）的设计进行了基础性探讨和评估。虽然SNNs本身是图神经网络的一种，但论文的焦点在于其架构的归纳偏置和过平滑问题，而非专门针对化学或质谱数据。然而，考虑到图神经网络是构建化学大模型（用于分子图表示）的常用基础架构之一，对其基础性能和行为的研究具有间接的相关性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

</details>

---

### 38. [CogGen: Cognitive-Load-Informed Fully Unsupervised Deep Generative Modeling for Compressively Sampled MRI Reconstruction](https://arxiv.org/abs/2603.04438)

**基本信息**

- 🔗 arXiv: [`2603.04438`](https://arxiv.org/abs/2603.04438)
- 👥 作者: Qingyong Zhu, Yumin Tan, Xiang Gu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04438.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种新颖的全无监督深度生成建模（FU-DGM）框架。生成模型是“化学大模型”的一个重要组成部分（例如用于分子生成或质谱预测）。论文提出的认知负荷调度策略是一种通用的模型训练改进方法，与构建和优化大模型的主题相关。

**📖 中文摘要**

本文提出了CogGen，一种认知负荷感知的全无监督深度生成模型，用于压缩采样磁共振成像重建。该方法将CS-MRI视为分阶段反演，并通过渐进式调度内在难度和外部干扰来调节任务侧的“认知负荷”。CogGen用从易到难的k空间加权/选择策略取代了统一的数据拟合。虽然该论文的应用领域是医学成像，但其核心贡献是一种新的、用于解决病态逆问题的无监督深度生成建模框架。生成模型（如文中的DIP和INR）是构建“大模型”的重要类别。论文提出的“认知负荷”调度策略是一种新颖的训练范式，可能对训练其他领域的生成模型（包括潜在的化学或质谱生成模型）有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fully unsupervised deep generative modeling (FU-DGM) is promising for compressively sampled MRI (CS-MRI) when training data or compute are limited. Classical FU-DGMs such as DIP and INR rely on architectural priors, but the ill-conditioned inverse problem often demands many iterations and easily overfits measurement noise. We propose CogGen, a cognitive-load-informed FU-DGM that casts CS-MRI as staged inversion and regulates task-side "cognitive load" by progressively scheduling intrinsic difficulty and extraneous interference. CogGen replaces uniform data fitting with an easy-to-hard k-space weighting/selection strategy: early iterations emphasize low-frequency, high-SNR, structure-dominant samples, while higher-frequency or noise-dominated measurements are introduced later. We realize this schedule via self-paced curriculum learning with complementary student-mode (what the model can currently learn) and teacher-mode (what it should follow) criteria, supporting both soft weighting and hard selection. Experiments and analysis show that CogGen-DIP and CogGen-INR improve fidelity and convergence over strong unsupervised baselines and competitive supervised pipelines.

</details>

---

### 39. [A systematic approach to answering the easy problems of consciousness based on an executable cognitive system](https://arxiv.org/abs/2603.04440)

**基本信息**

- 🔗 arXiv: [`2603.04440`](https://arxiv.org/abs/2603.04440)
- 👥 作者: Qi Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04440.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个可执行的认知系统来模拟高级认知功能。虽然应用领域不同，但这项工作涉及构建复杂的、基于知识的AI系统，这与构建和理解“化学大模型”（作为复杂的、需要领域知识的AI系统）在系统架构和机制解释层面存在方法论上的相关性。

**📖 中文摘要**

本文基于一个可执行的认知系统及其实现的计算机制，首次尝试系统地解决Chalmers提出的意识的“简单问题”。该系统建立在康德提出的概念知识理解之上。研究认为，辨别、分类、反应、报告和整合信息的能力都可以从系统的学习机制中推导出来。虽然论文主要关注认知科学和人工智能中的意识建模，但其核心是描述一个基于特定知识表示和推理机制的可执行认知系统架构。这种对复杂系统内部机制进行建模和解释的尝试，与构建和理解“化学大模型”（作为复杂的AI系统）的内在工作机制这一更广泛的挑战在方法论上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Consciousness is the window of the brain and reflects many fundamental cognitive properties involving both computational and cognitive mechanisms. A collection of these properties was described as the "easy problems" by Chalmers, including the ability to discriminate, categorize, and react to stimuli; information integration; reportability; information access; attention; deliberate control; and the difference between wakefulness and sleep. These "easy problems" have not been systematically addressed. This study presents a first attempt to address them systematically based on an executable cognitive system and its implemented computational mechanisms, built upon an understanding of conceptual knowledge proposed by Kant. The study suggests that the abilities to discriminate, categorize, react, report, and integrate information can all be derived from the system's learning mechanism; attention and deliberate control are goal-oriented and can be attributed to emotional states and its information-manipulation mechanism; and the difference between wakefulness and dream sleep lies mainly in the source of stimuli. The connections between the implemented mechanisms in the executive system and conclusions drawn from empirical findings are also discussed, and many of these discussions and conclusions are supported by demonstrations of the executive system.

</details>

---

### 40. [AbAffinity: A Large Language Model for Predicting Antibody Binding Affinity against SARS-CoV-2](https://arxiv.org/abs/2603.04480)

**基本信息**

- 🔗 arXiv: [`2603.04480`](https://arxiv.org/abs/2603.04480)
- 👥 作者: Faisal Bin Ashraf, Animesh Ray, Stefano Lonardi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04480.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个名为AbAffinity的大型语言模型（LLM），用于预测抗体-抗原结合亲和力。这直接属于“化学大模型”在生物分子性质预测和药物发现领域的应用。

**📖 中文摘要**

本研究介绍了AbAffinity，一种新的大型语言模型，用于准确预测抗体与目标肽（例如SARS-CoV-2刺突蛋白）的结合亲和力。抗体结合亲和力是设计中和抗体的最关键特性之一。该模型利用人工智能领域的显著进步和实验抗体数据（特别是与COVID-19相关的数据）的指数级增长，展示了机器学习在抗体设计中的应用。这项工作是将大型语言模型应用于生物分子（抗体）性质预测的具体案例，是“化学大模型”在生物化学和药物发现领域的一个直接应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning-based antibody design is emerging as one of the most promising approaches to combat infectious diseases, due to significant advancements in the field of artificial intelligence and an exponential surge in experimental antibody data (in particular related to COVID-19). The ability of an antibody to bind to an antigens (called binding affinity) is one of the the most critical properties in designing neutralizing antibodies. In this study we introduce Ab-Affinity, a new large language model that can accurately predict the binding affinity of antibodies against a target peptide, e.g., the SARS-CoV-2 spike protein. Code and model are available at this https URL .

</details>

---

### 41. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2603.04523)

**基本信息**

- 🔗 arXiv: [`2603.04523`](https://arxiv.org/abs/2603.04523)
- 👥 作者: Austin Rodriguez, Justin S. Smith, Sakib Matin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04523.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对机器学习原子间势（MLIPs）的新型训练框架。MLIPs是计算化学中用于模拟分子势能面的关键“化学大模型”。本文提出的PHL方法旨在更高效、更准确地训练这类模型，与主题直接相关。

**📖 中文摘要**

本文介绍了投影Hessian学习（PHL），一个用于机器学习原子间势（MLIPs）的可扩展二阶训练框架。该方法通过仅使用Hessian-向量积（HVPs）来注入曲率信息，避免了构建和存储完整Hessian矩阵的二次方内存增长。PHL使用基于随机迹的无偏损失，实现了具有有利系统尺寸缩放的曲率感知训练。研究在ωB97XD/6-31G(d)水平计算的化学反应物、产物、过渡态、内禀反应坐标和简正模采样几何的化学多样化数据集上进行了基准测试。结果表明，PHL在保持大部分二阶精度增益的同时，可以扩展到更大、更复杂的分子系统。机器学习原子间势是“化学大模型”在计算化学和分子模拟中的核心应用之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hessian matrix (second derivatives) encodes far richer local curvature of the potential energy surface than energies and forces alone. However, training machine-learning interatomic potentials (MLIPs) with full Hessians is often impractical because explicitly forming and storing Hessian matrices scales quadratically in cost and memory. We introduce Projected Hessian Learning (PHL), a scalable second-order training framework that injects curvature information using only Hessian-vector products (HVPs). Rather than constructing the Hessian, PHL projects curvature along stochastic probe directions and uses an unbiased stochastic trace-based loss with favorable system-size scaling, enabling curvature-informed training without quadratic memory growth. We benchmark PHL on a chemically diverse dataset of reactants, products, transition states, intrinsic reaction coordinates, and normal-mode sampled geometries computed at omegaB97XD/6-31G(d). We compare energy-force training (E-F), two HVP-based schemes (E-F-HVP with one-hot or randomized probes), and full energy-force-Hessian training (E-F-H). With randomized probes per minibatch, both HVP schemes match full-Hessian training in energy, force, and Hessian accuracy while delivering >24x epoch speedups for the small molecular systems studied. In a fixed-probe regime with one HVP per molecule, randomized projections consistently outperform one-column probing, especially for far-from-equilibrium geometries. Overall, PHL replaces explicit Hessian supervision with force-complexity curvature training, retaining most second-order accuracy gains while scaling to larger, more complex molecular systems.

</details>

---

### 42. [The Volterra signature](https://arxiv.org/abs/2603.04525)

**基本信息**

- 🔗 arXiv: [`2603.04525`](https://arxiv.org/abs/2603.04525)
- 👥 作者: Paul P. Hager, Fabian N. Harang, Luca Pelizzari 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04525.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是提出Volterra签名作为一种用于非马尔可夫时间序列的通用特征表示框架。质谱数据可以视为一种特殊的时间序列或信号。因此，该框架在方法论上为“质谱结构推理”中可能用到的序列特征提取提供了新的工具和理论见解（标准1）。同时，作为一项基础性研究，它对时间序列表示学习领域有贡献，可能包含对相关主题的讨论（标准3）。

**📖 中文摘要**

本文提出了Volterra签名作为一种原则性的、显式的特征表示方法，用于处理具有历史依赖性的系统（非马尔可夫时间序列）。通过将由时间核加权的输入路径展开到张量代数中，并利用相关的Volterra-Chen恒等式，作者推导出了严格的学习理论保证。这包括一个单射性陈述（在增广下的可识别性）和无限维路径空间上的通用逼近定理。对于一大类指数型核，Volterra签名在张量代数中求解线性状态空间ODE。结合固有的时间重参数化不变性，这些结果将Volterra签名定位为数据科学中一个鲁棒、计算易处理的特征映射。作者在真实和合成数据的动态学习任务中展示了其有效性。虽然论文是通用方法，但处理序列数据（如时间序列）的特征提取是分析质谱数据（可视为一维信号或时间序列）和构建相关模型的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern approaches for learning from non-Markovian time series, such as recurrent neural networks, neural controlled differential equations or transformers, typically rely on implicit memory mechanisms that can be difficult to interpret or to train over long horizons. We propose the Volterra signature $\mathrm{VSig}(x;K)$ as a principled, explicit feature representation for history-dependent systems. By developing the input path $x$ weighted by a temporal kernel $K$ into the tensor algebra, we leverage the associated Volterra--Chen identity to derive rigorous learning-theoretic guarantees. Specifically, we prove an injectivity statement (identifiability under augmentation) that leads to a universal approximation theorem on the infinite dimensional path space, which in certain cases is achieved by linear functionals of $\mathrm{VSig}(x;K)$. Moreover, we demonstrate applicability of the kernel trick by showing that the inner product associated with Volterra signatures admits a closed characterization via a two-parameter integral equation, enabling numerical methods from PDEs for computation. For a large class of exponential-type kernels, $\mathrm{VSig}(x;K)$ solves a linear state-space ODE in the tensor algebra. Combined with inherent invariance to time reparameterization, these results position the Volterra signature as a robust, computationally tractable feature map for data science. We demonstrate its efficacy in dynamic learning tasks on real and synthetic data, where it consistently improves classical path signature baselines.

</details>

---

### 43. [Estimation of Persistence Diagrams via the Three Gap Theorem](https://arxiv.org/abs/2603.04570)

**基本信息**

- 🔗 arXiv: [`2603.04570`](https://arxiv.org/abs/2603.04570)
- 👥 作者: Luis Suarez Salas, Jose A. Perea
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04570.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用拓扑数据分析（TDA）中的持久图和数论工具，从准周期信号的频谱中近似其滑动窗口嵌入的拓扑特征（持久图）。虽然应用场景是动力系统，但该方法论（从信号频谱到结构描述符）与“质谱结构推理”中从质谱信号（可视为一种频谱）推断分子结构信息在问题形式上高度相似，因此具有核心主题相关性。

**📖 中文摘要**

本文提出了利用数论中的三间隔定理和拓扑数据分析中的持久Künneth公式，来近似准周期函数滑动窗口嵌入的持久图的理论和计算方案。持久图是拓扑数据分析中用于度量形状的描述符，已应用于包括周期性和准周期性量化在内的应用中。输入是信号的频谱，作者提供了数值和理论证据证明其捕获环形吸引子形状的效用。虽然应用背景是动力系统，但持久图（一种拓扑描述符）和从信号（频谱）中提取形状信息的方法，与“质谱结构推理”中从质谱信号（其频谱或轮廓包含分子结构信息）推断分子形状或结构存在概念上的相似性。该研究为从一维信号进行形状分析提供了数学工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The time delay (or Sliding Window) embedding is a technique from dynamical systems to reconstruct attractors from time series data. Recently, descriptors from Topological Data Analysis (TDA) -- specifically, persistence diagrams -- have been used to measure the shape of said reconstructed attractors in applications including periodicity and quasiperiodicity quantification. Despite their utility, the fast computation of persistence diagrams of sliding window embeddings is still poorly understood. In this work, we present theoretical and computational schemes to approximate the persistence diagrams of sliding window embeddings from quasiperiodic functions. We do so by combining the Three Gap Theorem from number theory with the Persistent Künneth formula from TDA, and derive fast and provably correct persistent homology approximations. The input to our procedure is the spectrum of the signal, and we provide numerical as well as theoretical evidence of its utility to capture the shape of toroidal attractors.

</details>

---

### 44. [Temporal Pooling Strategies for Training-Free Anomalous Sound Detection with Self-Supervised Audio Embeddings](https://arxiv.org/abs/2603.04605)

**基本信息**

- 🔗 arXiv: [`2603.04605`](https://arxiv.org/abs/2603.04605)
- 👥 作者: Kevin Wilkinghoff, Sarthak Yadav, Zheng-Hua Tan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04605.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对预训练模型产生的序列嵌入，系统评估和提出新的时序池化策略。由于质谱数据在分析前也常被编码为序列嵌入，因此如何有效地聚合这些嵌入以进行“质谱结构推理”是一个关键步骤。该研究为此提供了直接相关的技术方案和评估。

**📖 中文摘要**

本文系统评估了在基于预训练音频嵌入模型的免训练异常声音检测中，时序池化策略的作用。作者提出了相对偏差池化（RDP），一种强调信息性时序偏差的自适应池化方法，并引入了一种将RDP与广义均值池化相结合的混合池化策略。在五个基准数据集上的实验表明，所提方法 consistently 优于均值池化，并在免训练ASD中实现了最先进的性能。虽然应用领域是音频异常检测，但论文的核心贡献是针对序列嵌入（来自预训练模型）的池化策略研究。在“质谱结构推理”中，质谱数据也常被转化为嵌入表示，然后进行聚合或池化以进行分类或回归任务。因此，对序列嵌入池化策略的深入研究对该主题有直接的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training-free anomalous sound detection (ASD) based on pre-trained audio embedding models has recently garnered significant attention, as it enables the detection of anomalous sounds using only normal reference data while offering improved robustness under domain shifts. However, existing embedding-based approaches almost exclusively rely on temporal mean pooling, while alternative pooling strategies have so far only been explored for spectrogram-based representations. Consequently, the role of temporal pooling in training-free ASD with pre-trained embeddings remains insufficiently understood. In this paper, we present a systematic evaluation of temporal pooling strategies across multiple state-of-the-art audio embedding models. We propose relative deviation pooling (RDP), an adaptive pooling method that emphasizes informative temporal deviations, and introduce a hybrid pooling strategy that combines RDP with generalized mean pooling. Experiments on five benchmark datasets demonstrate that the proposed methods consistently outperform mean pooling and achieve state-of-the-art performance for training-free ASD, including results that surpass all previously reported trained systems and ensembles on the DCASE2025 ASD dataset.

</details>

---

### 45. [Why the Brain Consolidates: Predictive Forgetting for Optimal Generalisation](https://arxiv.org/abs/2603.04688)

**基本信息**

- 🔗 arXiv: [`2603.04688`](https://arxiv.org/abs/2603.04688)
- 👥 作者: Zafeirios Fountas, Adnan Oomerjee, Haitham Bou-Ammar 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04688.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从计算角度解释大脑记忆巩固，并提出了“预测性遗忘”作为优化存储表征泛化能力的机制。研究在Transformer语言模型上进行了验证。这为改进“化学大模型”（尤其是基于Transformer架构的）的训练策略、防止过拟合和提升泛化能力提供了新颖的理论视角和潜在方法。

**📖 中文摘要**

本文提出了“预测性遗忘”的理论，认为高容量皮层网络通过减少复杂性来优化存储的表征以进行泛化，即选择性地保留那些能预测未来结果或经验的已体验信息。研究证明，预测性遗忘在形式上改善了存储表征的信息论泛化界限。作者在基于自动编码器的皮层模型、生物合理的预测编码电路和基于Transformer的语言模型中演示了这种容量依赖性。这些结果确定了离线巩固在稳定之外的计算作用，表明以结果为条件的压缩优化了保留与泛化之间的权衡。虽然论文聚焦于神经科学和记忆巩固，但其核心思想——通过选择性压缩/遗忘存储的信息来优化AI模型的泛化能力——直接关系到“化学大模型”的训练和优化。特别是论文在Transformer语言模型上进行了模拟，这与大语言模型（作为大模型的一种）的改进相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Standard accounts of memory consolidation emphasise the stabilisation of stored representations, but struggle to explain representational drift, semanticisation, or the necessity of offline replay. Here we propose that high-capacity neocortical networks optimise stored representations for generalisation by reducing complexity via predictive forgetting, i.e. the selective retention of experienced information that predicts future outcomes or experience. We show that predictive forgetting formally improves information-theoretic generalisation bounds on stored representations. Under high-fidelity encoding constraints, such compression is generally unattainable in a single pass; high-capacity networks therefore benefit from temporally separated, iterative refinement of stored traces without re-accessing sensory input. We demonstrate this capacity dependence with simulations in autoencoder-based neocortical models, biologically plausible predictive coding circuits, and Transformer-based language models, and derive quantitative predictions for consolidation-dependent changes in neural representational geometry. These results identify a computational role for off-line consolidation beyond stabilisation, showing that outcome-conditioned compression optimises the retention-generalisation trade-off.

</details>

---

### 46. [Particle-Guided Diffusion for Gas-Phase Reaction Kinetics](https://arxiv.org/abs/2603.05139)

**基本信息**

- 🔗 arXiv: [`2603.05139`](https://arxiv.org/abs/2603.05139)
- 👥 作者: Andrew Millard, Henrik Pedersen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将扩散模型（一种生成式大模型）应用于化学动力学系统，属于化学大模型在物理化学系统建模中的具体应用。

**📖 中文摘要**

本文提出了一种基于扩散模型的粒子引导采样方法，用于解决气相化学反应动力学中的偏微分方程（PDE）控制问题。该方法在变化的参数条件下，对平流-反应-扩散（ARD）方程的解进行训练，以生成物理上一致的浓度场并准确预测出口浓度。这项工作展示了扩散模型在反应输运系统中进行推理的潜力，与化学信息学中利用生成模型（如化学大模型）进行物理引导的分子或反应路径生成与预测的研究主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

</details>

---

### 47. [Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks](https://arxiv.org/abs/2603.05188)

**基本信息**

- 🔗 arXiv: [`2603.05188`](https://arxiv.org/abs/2603.05188)
- 👥 作者: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05188.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发和应用大型语言模型（LLM）智能体进行化学材料的逆向设计，直接属于化学大模型的研究范畴。

**📖 中文摘要**

本文介绍了一个名为Ara的大型语言模型（LLM）智能体，用于共价有机框架（COFs）光催化剂的逆向设计。该智能体利用预训练的化学知识、给体-受体理论、共轭效应和连接键稳定性层次结构，指导搜索同时满足带隙、带边和水解稳定性标准的COFs。研究在一个由不同节点、连接体、连接键和R基团组成的候选空间中，将Ara与随机搜索和贝叶斯优化（BO）进行比较，结果表明Ara的命中率显著更高。这项工作展示了LLM化学先验知识如何加速多标准材料发现，是化学大模型在材料信息学领域的一个典型应用案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

</details>

---

### 48. [Path Planning for Masked Diffusion Model Sampling](https://arxiv.org/abs/2502.03540)

**基本信息**

- 🔗 arXiv: [`2502.03540`](https://arxiv.org/abs/2502.03540)
- 👥 作者: Fred Zhangzhi Peng, Zachary Bezemek, Sawan Patel 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03540.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进掩码扩散模型（一种生成式大模型）的推理算法，该模型在化学信息学中常用于分子序列、蛋白质结构等数据的生成与推理，与化学大模型主题直接相关。

**📖 中文摘要**

本文提出了一种名为路径规划（P2）的新型推理采样策略，用于提升掩码扩散模型（MDMs）在离散数据（如序列）生成中的性能。P2将每个生成步骤分解为规划和去噪两个子阶段，允许迭代地细化和更新已生成的标记。作者在蛋白质序列、RNA序列、数学推理、故事生成和代码生成等多个领域验证了P2的有效性，显著提升了生成质量。掩码扩散模型是生成式模型的一种，广泛应用于分子序列、蛋白质结构等化学信息学领域的数据生成与推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Any order generation of discrete data using masked diffusion models (MDMs) offers a compelling alternative to traditional autoregressive models, especially in domains that lack a natural causal ordering of data. However, current popular MDMs depart from their successful continuous diffusion model counterparts with simplified masked inference wherein unmasked tokens cannot be iteratively refined -- even if there is a mistake. In this paper, we extract the full power of MDMs by introducing a novel inference sampling strategy termed Path Planning (P2) that decomposes each generation step into two sub-stages: planning and denoising. Under P2, the planner at every step selects appropriate tokens that are marked to be updated, which can then be sampled using the denoiser. We demonstrate that P2 generalizes all existing sampling strategies for MDMs and critically enhances generative quality through the new capability of refining and updating existing unmasked tokens. We theoretically prove that P2 establishes a (new) expanded evidence lower bound (ELBO) on the log marginal likelihood of data. We instantiate P2 with a family of planners including: 1.) Self-Planning, 2.) BERT-Planning, and 3.) Trained-Planning with a learned planner leading to SOTA generative performance for MDMs on a suite of domains. Specifically, solely using P2 inference, we observe relative improvements of 22% in protein sequence foldability, 8% in RNA sequence pLDDT, 4% in math reasoning, 68% in story generation (ROUGE score), and 33% in code generation for the challenging pass@1 metric.

</details>

---

### 49. [PhysLLM: Harnessing Large Language Models for Cross-Modal Remote Physiological Sensing](https://arxiv.org/abs/2505.03621)

**基本信息**

- 🔗 arXiv: [`2505.03621`](https://arxiv.org/abs/2505.03621)
- 👥 作者: Yiping Xie, Bo Zhao, Mingtong Dai 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03621.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个利用大型语言模型（LLM）处理和理解连续生理信号的框架。LLM作为大模型的一种，其与连续信号（类比于化学中的质谱、光谱信号）的跨模态对齐和推理方法，与化学大模型及质谱结构推理的研究思路高度相关。

**📖 中文摘要**

本文提出PhysLLM，一个利用大型语言模型（LLM）进行跨模态远程生理感知（如远程光电容积描记术，rPPG）的协作优化框架。该框架通过文本原型引导策略建立血流动力学特征与LLM可解释语义空间之间的跨模态对齐，并引入双域平稳算法解决信号不稳定性问题。研究在多个基准数据集上验证了PhysLLM的准确性和鲁棒性。虽然应用领域是生理信号，但该工作核心是探索LLM（一种大模型）处理连续、噪声敏感信号并建立跨模态语义理解的方法论，其模型架构和训练策略对化学信息学中处理光谱、质谱等连续信号具有借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Remote photoplethysmography (rPPG) enables non-contact physiological measurement but remains highly susceptible to illumination changes, motion artifacts, and limited temporal modeling. Large Language Models (LLMs) excel at capturing long-range dependencies, offering a potential solution but struggle with the continuous, noise-sensitive nature of rPPG signals due to their text-centric design. To bridge this gap, we introduce the PhysLLM, a collaborative optimization framework that synergizes LLMs with domain-specific rPPG components. Specifically, the Text Prototype Guidance (TPG) strategy is proposed to establish cross-modal alignment by projecting hemodynamic features into LLM-interpretable semantic space, effectively bridging the representational gap between physiological signals and linguistic tokens. Besides, a novel Dual-Domain Stationary (DDS) Algorithm is proposed for resolving signal instability through adaptive time-frequency domain feature re-weighting. Finally, rPPG task-specific cues systematically inject physiological priors through physiological statistics, environmental contextual answering, and task description, leveraging cross-modal learning to integrate both visual and textual information, enabling dynamic adaptation to challenging scenarios like variable illumination and subject movements. Evaluation on four benchmark datasets, PhysLLM achieves state-of-the-art accuracy and robustness, demonstrating superior generalization across lighting variations and motion scenarios. The source code is available at this https URL .

</details>

---

### 50. [OSPO: Object-Centric Self-Improving Preference Optimization for Text-to-Image Generation](https://arxiv.org/abs/2506.02015)

**基本信息**

- 🔗 arXiv: [`2506.02015`](https://arxiv.org/abs/2506.02015)
- 👥 作者: Yoonjin Oh, Yongjin Kim, Hyomin Kim 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.02015.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对多模态大语言模型（MLLM）进行对象级细粒度对齐的优化，属于大模型能力优化与对齐的研究范畴。其方法对化学大模型处理分子结构等精细化学实体具有借鉴意义。

**📖 中文摘要**

本文提出了对象中心自改进偏好优化（OSPO），一个用于增强多模态大语言模型（MLLM）在文本到图像生成中细粒度、对象级图文对齐的自改进框架。OSPO自主构建对象中心的偏好数据，无需外部数据或模型，并引入基于注意力的对象掩码和对象加权的SimPO损失来增强对象保真度。实验表明OSPO显著改善了细粒度对齐并减少了对象幻觉。虽然应用在图像生成，但该工作针对大模型（MLLM）在细粒度属性（如颜色、形状、空间关系）对齐上的优化方法，对于化学大模型在精确描述分子结构、官能团空间排列等任务上具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in Multimodal Large Language Models (MLLMs) have enabled unified multimodal understanding and generation. However, they still struggle with fine-grained text-image alignment, often failing to faithfully depict objects with correct attributes such as color, shape, and spatial relations. To mitigate this issue, previous studies have explored preference optimization methods such as DPO and GRPO, but these approaches incur substantial computational cost, both in constructing preference data and in performing optimization. This has motivated self-improving preference optimization approaches, in which the MLLM autonomously generates its own training data, self-estimates preference feedback, and self-optimizes using the resulting self-constructed preference pairs. However, existing self-improving methods still overlook fine-grained, object-level semantics, allowing object hallucination to persist. To tackle this problem, we propose Object-centric Self-improving Preference Optimization (OSPO), a self-improving framework designed to enhance object-level text-image alignment. OSPO explicitly constructs object-centric preference data without relying on any external data and external models. We also introduce a new approach that leverages attention-based object masks together with an object-weighted SimPO loss to enhance object-specific fidelity. Extensive experiments on three compositional image generation benchmarks demonstrate that OSPO significantly improves fine-grained alignment and reduces object hallucination, outperforming prior self-improving methods and even specialized diffusion-based text-to-image models.

</details>

---

### 51. [HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals](https://arxiv.org/abs/2506.08618)

**基本信息**

- 🔗 arXiv: [`2506.08618`](https://arxiv.org/abs/2506.08618)
- 👥 作者: Xianquan Yan, Hakan Akgün, Kenji Kawaguchi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08618.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模图结构数据集HSG-12M和自动化生成工具Poly2Graph。这些资源可用于训练和评估图神经网络模型，而图神经网络是化学大模型和质谱结构推理中的关键技术。

**📖 中文摘要**

本文介绍了HSG-12M，一个包含1160万个静态和510万个动态哈密顿谱图的大规模数据集。该数据集源自非厄米量子物理领域，其中晶体的能谱在复平面上形成复杂的几何结构（哈密顿谱图）。论文的核心贡献是提出了Poly2Graph，一个将一维晶体哈密顿量自动映射为谱图的高性能开源流程。HSG-12M是第一个大规模的空间多重图数据集，其中节点嵌入在度量空间中，并且保留了节点之间多条几何上不同的轨迹作为独立的边。这项工作为数据驱动的科学发现（如凝聚态物理）奠定了基础，并为几何感知的图学习提供了新的机会。虽然论文主要关注物理系统，但其核心贡献——大规模、高质量的图结构数据集（HSG-12M）和自动化生成工具（Poly2Graph）——为化学信息学领域（特别是化学大模型和质谱结构推理中所需的图神经网络训练和基准测试）提供了宝贵的数据资源和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming scientific research by revealing new ways to understand complex physical systems, but its impact remains constrained by the lack of large, high-quality domain-specific datasets. A rich, largely untapped resource lies in non-Hermitian quantum physics, where the energy spectra of crystals form intricate geometries on the complex plane -- termed as Hamiltonian spectral graphs. Despite their significance as fingerprints for electronic behavior, their systematic study has been intractable due to the reliance on manual extraction. To unlock this potential, we introduce Poly2Graph: a high-performance, open-source pipeline that automates the mapping of 1-D crystal Hamiltonians to spectral graphs. Using this tool, we present HSG-12M: a dataset containing 11.6 million static and 5.1 million dynamic Hamiltonian spectral graphs across 1401 characteristic-polynomial classes, distilled from 177 TB of spectral potential data. Crucially, HSG-12M is the first large-scale dataset of spatial multigraphs -- graphs embedded in a metric space where multiple geometrically distinct trajectories between two nodes are retained as separate edges. This simultaneously addresses a critical gap, as existing graph benchmarks overwhelmingly assume simple, non-spatial edges, discarding vital geometric information. Benchmarks with popular GNNs expose new challenges in learning spatial multi-edges at scale. Beyond its practical utility, we show that spectral graphs serve as universal topological fingerprints of polynomials, vectors, and matrices, forging a new algebra-to-graph link. HSG-12M lays the groundwork for data-driven scientific discovery in condensed matter physics, new opportunities in geometry-aware graph learning and beyond.

</details>

---

### 52. [Bures-Wasserstein Flow Matching for Graph Generation](https://arxiv.org/abs/2506.14020)

**基本信息**

- 🔗 arXiv: [`2506.14020`](https://arxiv.org/abs/2506.14020)
- 👥 作者: Keyue Jiang, Jiahao Cui, Xiaowen Dong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图生成，并专门在分子生成任务上进行了实验验证。分子生成是化学大模型（如用于分子设计的生成模型）的核心应用之一。

**📖 中文摘要**

本文提出了一种名为BWFlow的基于流匹配的图生成框架。该框架针对现有扩散和流模型在生成图时，将节点和边的演化独立建模并使用线性插值，导致构建的概率路径不规则、不光滑的问题，提出了一种理论框架。该框架将图表示为马尔可夫随机场参数化的连接系统，并利用MRF对象之间的最优传输位移来设计一个平滑的概率路径，确保图组件的协同演化。实验在普通图生成和分子生成任务上验证了BWFlow的有效性，展示了其具有竞争力的性能、更好的训练收敛性和高效的采样。分子生成是化学信息学和药物发现的核心任务，因此，这篇论文提出的图生成方法直接与化学大模型（用于分子设计）相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation has emerged as a critical task in fields ranging from drug discovery to circuit design. Contemporary approaches, notably diffusion and flow-based models, have achieved solid graph generative performance through constructing a probability path that interpolates between reference and data distributions. However, these methods typically model the evolution of individual nodes and edges independently and use linear interpolations in the disjoint space of nodes/edges to build the path. This disentangled interpolation breaks the interconnected patterns of graphs, making the constructed probability path irregular and non-smooth, which causes poor training dynamics and faulty sampling convergence. To address the limitation, this paper first presents a theoretically grounded framework for probability path construction in graph generative models. Specifically, we model the joint evolution of the nodes and edges by representing graphs as connected systems parameterized by Markov random fields (MRF). We then leverage the optimal transport displacement between MRF objects to design a smooth probability path that ensures the co-evolution of graph components. Based on this, we introduce BWFlow, a flow-matching framework for graph generation that utilizes the derived optimal probability path to benefit the training and sampling algorithm design. Experimental evaluations in plain graph generation and molecule generation validate the effectiveness of BWFlow with competitive performance, better training convergence, and efficient sampling.

</details>

---

### 53. [Elucidating the Design Space of Arbitrary-Noise-Based Diffusion Models](https://arxiv.org/abs/2507.18534)

**基本信息**

- 🔗 arXiv: [`2507.18534`](https://arxiv.org/abs/2507.18534)
- 👥 作者: Xingyu Qiu, Mengying Yang, Xinghua Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.18534.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是阐明和统一扩散模型的设计空间。扩散模型是构建化学大模型（特别是生成式模型，如分子生成模型）的关键底层技术之一，其理论进展对化学信息学领域有直接影响。

**📖 中文摘要**

本文提出了EDA（Elucidating the Design space of Arbitrary-noise diffusion models），旨在为处理不同噪声模式的扩散模型提供一个统一的理论框架。EDA扩展了噪声模式的灵活性，同时保持了EDM的模块化特性，并严格证明了增加噪声复杂性不会在恢复过程中引入额外的计算开销。论文在三个具有代表性的医学图像去噪和自然图像恢复任务上验证了EDA：MRI偏置场校正（全局平滑噪声）、CT金属伪影去除（全局锐利噪声）和自然图像阴影去除（局部边界感知噪声）。结果表明，EDA在图像恢复方面具有很强的泛化能力。扩散模型是当前生成式AI的核心技术之一，其设计空间的阐明和统一框架的构建，对于理解和开发更强大的化学大模型（例如用于分子生成或光谱预测）具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although EDM aims to unify the design space of diffusion models, its reliance on fixed Gaussian noise prevents it from explaining emerging flow-based methods that diffuse arbitrary noise. Moreover, our study reveals that EDM's forcible injection of Gaussian noise has adverse effects on image restoration task, as it corrupts the degraded images, overextends the restoration distance, and increases the task's complexity. To interpret diverse methods for handling distinct noise patterns within a unified theoretical framework and to minimize the restoration distance, we propose EDA, which Elucidates the Design space of Arbitrary-noise diffusion models. Theoretically, EDA expands noise pattern flexibility while preserving EDM's modularity, with rigorous proof that increased noise complexity introduces no additional computational overhead during restoration. EDA is validated on three representative medical image denoising and natural image restoration tasks: MRI bias field correction (global smooth noise), CT metal artifact removal (global sharp noise) and natural image shadow removal (local boundary-aware noise). With only 5 sampling steps, competitive results against specialized methods across medical and natural tasks demonstrate EDA's strong generalization capability for image restoration. Code is available at: this https URL .

</details>

---

### 54. [Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks](https://arxiv.org/abs/2509.19696)

**基本信息**

- 🔗 arXiv: [`2509.19696`](https://arxiv.org/abs/2509.19696)
- 👥 作者: Noah Geiger, Tamim Asfour, Neville Hogan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.19696.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散模型进行生成和推理（生成物理一致的轨迹）。这种方法论与质谱结构推理中“从光谱数据生成/推断分子结构”这一逆问题在技术路径上高度相关，都是利用生成模型解决从观测数据到复杂结构的映射问题。

**📖 中文摘要**

本文提出了基于扩散的阻抗学习框架，用于接触丰富的机器人操作任务。该框架结合了生成建模与能量一致的阻抗控制。一个基于Transformer的扩散模型，通过交叉注意力在测量的外部力矩上进行条件化，重建模拟的零力轨迹（sZFT），该轨迹代表了接触一致的平衡行为。重建的sZFT被一个基于能量的估计器用于通过方向刚度和阻尼调制在线调整阻抗。该模型在通过Apple Vision Pro遥操作收集的跑酷和机器人辅助治疗演示上进行训练。虽然应用场景是机器人操作，但其核心技术创新——使用扩散模型生成物理一致的轨迹或状态——与质谱结构推理中“从数据生成或推断分子结构”这一核心问题在方法论上高度相似。生成模型（如扩散模型）是解决此类逆问题的有力工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning-based methods excel at robot motion generation but remain limited in contact-rich physical interaction. Impedance control provides stable and safe contact behavior but requires task-specific tuning of stiffness and damping parameters. We present Diffusion-Based Impedance Learning, a framework that bridges these paradigms by combining generative modeling with energy-consistent impedance control. A Transformer-based Diffusion Model, conditioned via cross-attention on measured external wrenches, reconstructs simulated Zero-Force Trajectories (sZFTs) that represent contact-consistent equilibrium behavior. A SLERP-based quaternion noise scheduler preserves geometric consistency for rotations on the unit sphere. The reconstructed sZFT is used by an energy-based estimator to adapt impedance online through directional stiffness and damping modulation. Trained on parkour and robot-assisted therapy demonstrations collected via Apple Vision Pro teleoperation, the model achieves sub-millimeter positional and sub-degree rotational accuracy using only tens of thousands of samples. Deployed in realtime torque control on a KUKA LBR iiwa, the approach enables smooth obstacle traversal and generalizes to unseen tasks, achieving 100% success in multi-geometry peg-in-hole insertion.

</details>

---

### 55. [Noise-to-Notes: Diffusion-based Generation and Refinement for Automatic Drum Transcription](https://arxiv.org/abs/2509.21739)

**基本信息**

- 🔗 arXiv: [`2509.21739`](https://arxiv.org/abs/2509.21739)
- 👥 作者: Michael Yeung, Keisuke Toyama, Toya Teramoto 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.21739.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散模型从音频信号生成结构化的符号序列（鼓点事件）。这与质谱结构推理中“从质谱信号生成分子结构”的任务在问题形式（从信号到结构）和技术路径（使用生成模型）上高度相似，具有直接的相关性。

**📖 中文摘要**

本文重新定义了自动鼓点转录（ADT）任务，将其视为条件生成任务，并引入了Noise-to-Notes（N2N）框架。该框架利用扩散建模，将音频条件化的高斯噪声转换为带有相关速度的鼓点事件。这种生成式扩散方法具有灵活的速度-精度权衡和强大的修复能力。为了增强低层级频谱图特征，论文提出整合从音乐基础模型（MFM）中提取的特征，这些特征捕获了高级语义信息并增强了对域外鼓音频的鲁棒性。实验结果表明，包含MFM特征显著提高了鲁棒性，并且N2N在多个ADT基准测试中建立了新的最先进性能。这篇论文展示了扩散模型在从音频信号（时序数据）生成结构化符号序列（鼓点事件）方面的成功应用。质谱数据也是一种时序/频谱信号，从中推断分子结构是一个类似的“从信号到结构”的生成任务。因此，该论文的方法为质谱结构推理提供了可借鉴的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automatic drum transcription (ADT) is traditionally formulated as a discriminative task to predict drum events from audio spectrograms. In this work, we redefine ADT as a conditional generative task and introduce Noise-to-Notes (N2N), a framework leveraging diffusion modeling to transform audio-conditioned Gaussian noise into drum events with associated velocities. This generative diffusion approach offers distinct advantages, including a flexible speed-accuracy trade-off and strong inpainting capabilities. However, the generation of binary onset and continuous velocity values presents a challenge for diffusion models, and to overcome this, we introduce an Annealed Pseudo-Huber loss to facilitate effective joint optimization. Finally, to augment low-level spectrogram features, we propose incorporating features extracted from music foundation models (MFMs), which capture high-level semantic information and enhance robustness to out-of-domain drum audio. Experimental results demonstrate that including MFM features significantly improves robustness and N2N establishes a new state-of-the-art performance across multiple ADT benchmarks.

</details>

---

### 56. [EchoMind: An Interrelated Multi-level Benchmark for Evaluating Empathetic Speech Language Models](https://arxiv.org/abs/2510.22758)

**基本信息**

- 🔗 arXiv: [`2510.22758`](https://arxiv.org/abs/2510.22758)
- 👥 作者: Li Zhou, Lutong Yu, You Lyu 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22758.pdf)

**💡 相关性分析**

满足标准3：论文是一个专门针对多模态模型（语音语言模型）评估的综述性/基准性工作。它提出了一个系统的、多层次的评估框架和方法论。这种构建综合性评估基准的思路，对于评估化学大模型或质谱分析模型的多模态理解和推理能力具有重要的借鉴和参考意义。

**📖 中文摘要**

本文提出了EchoMind，第一个相互关联的多层级基准测试，用于评估语音语言模型（SLMs）的共情对话能力。它通过顺序的、上下文关联的任务（口语内容理解、声音线索感知、综合推理和响应生成）来模拟共情对话的认知过程。所有任务共享相同且语义中立的脚本，并通过受控的声音风格变化来测试独立于文本内容的传递效果。EchoMind基于一个涵盖3个粗粒度和12个细粒度维度、包含39个声音属性的共情导向框架。虽然论文主要关注语音和对话，但其核心贡献——构建一个用于评估模型多模态（语音+文本）理解和推理能力的基准测试——其方法论（设计多模态、多任务评估框架）对于评估化学大模型或质谱分析模型的多模态能力（例如，结合分子结构图、光谱和文本描述）具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech Language Models (SLMs) have made significant progress in spoken language understanding. Yet it remains unclear whether they can fully perceive non lexical vocal cues alongside spoken words, and respond with empathy that aligns with both emotional and contextual factors. Existing benchmarks typically evaluate linguistic, acoustic, reasoning, or dialogue abilities in isolation, overlooking the integration of these skills that is crucial for human-like, emotionally intelligent conversation. We present EchoMind, the first interrelated, multi-level benchmark that simulates the cognitive process of empathetic dialogue through sequential, context-linked tasks: spoken-content understanding, vocal-cue perception, integrated reasoning, and response generation. All tasks share identical and semantically neutral scripts that are free of explicit emotional or contextual cues, and controlled variations in vocal style are used to test the effect of delivery independent of the transcript. EchoMind is grounded in an empathy-oriented framework spanning 3 coarse and 12 fine-grained dimensions, encompassing 39 vocal attributes, and evaluated using both objective and subjective metrics. Testing 12 advanced SLMs reveals that even state-of-the-art models struggle with high-expressive vocal cues, limiting empathetic response quality. Analyses of prompt strength, speech source, and ideal vocal cue recognition reveal persistent weaknesses in instruction-following, resilience to natural speech variability, and effective use of vocal cues for empathy. These results underscore the need for SLMs that integrate linguistic content with diverse vocal cues to achieve truly empathetic conversational ability.

</details>

---

### 57. [Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling](https://arxiv.org/abs/2510.26139)

**基本信息**

- 🔗 arXiv: [`2510.26139`](https://arxiv.org/abs/2510.26139)
- 👥 作者: Minseo Kwon, Young J. Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.26139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用视觉语言模型（VLM）引导复杂系统的规划与推理，并与专业验证工具结合。这种“大模型引导+专业验证”的范式，与化学大模型中利用LLM进行分子生成或合成路线规划，再通过计算化学工具验证其可行性的工作流程直接相关。

**📖 中文摘要**

本文提出了一种基于混合状态树的运动动力学任务与运动规划器，该规划器在规划过程中统一表示符号状态和数值状态，使得任务和运动决策能够共同决定。运动动力学约束由现成的运动规划器和物理模拟器验证，而视觉语言模型（VLM）则通过状态的可视化渲染来引导探索TAMP解决方案并基于此回溯搜索。实验表明，该方法相比传统和基于LLM的TAMP规划器，在复杂问题上提高了平均成功率并减少了规划时间。论文的核心是将高级符号推理（VLM）与低级几何/物理验证相结合来解决复杂规划问题。这种“大模型提供先验/引导，专用模块保证可行性”的范式，与化学信息学中利用大模型进行分子设计或反应预测，再通过计算化学方法（如DFT）验证的思路高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Task and Motion Planning (TAMP) integrates high-level task planning with low-level motion feasibility, but existing methods are costly in long-horizon problems due to excessive motion sampling. While LLMs provide commonsense priors, they lack 3D spatial reasoning and cannot ensure geometric or dynamic feasibility. We propose a kinodynamic TAMP planner based on a hybrid state tree that uniformly represents symbolic and numeric states during planning, enabling task and motion decisions to be jointly decided. Kinodynamic constraints embedded in the TAMP problem are verified by an off-the-shelf motion planner and physics simulator, and a VLM guides exploring a TAMP solution and backtracks the search based on visual rendering of the states. Experiments on the simulated domains and in the real world show 32.14% - 1166.67% increased average success rates compared to traditional and LLM-based TAMP planners and reduced planning time on complex problems, with ablations further highlighting the benefits of VLM backtracking. More details are available at this https URL .

</details>

---

### 58. [SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation](https://arxiv.org/abs/2510.27048)

**基本信息**

- 🔗 arXiv: [`2510.27048`](https://arxiv.org/abs/2510.27048)
- 👥 作者: Eric T. Chang, Peter Ballentine, Zhanpeng He 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27048.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及开发新型传感器（多模态触觉）并利用其数据通过机器学习（特别是强化学习）优化系统行为。这种方法论与质谱分析领域开发新型离子源、检测器，并利用机器学习优化仪器参数或解析复杂谱图的研究路径在概念上相关。

**📖 中文摘要**

本文介绍了SpikeATac，一种结合了静态（电容）和动态（PVDF）传感模式的多模态触觉手指。其16个触元的PVDF薄膜以4kHz采样，提供快速、灵敏的动态信号。论文展示了SpikeATac在抓取脆弱、可变形物体时能够快速、轻柔地停止。此外，论文还展示了一个结合人类反馈强化学习和基于触觉奖励的学习框架，用于微调策略以调制力。硬件平台和学习管道共同实现了一项此前未实现的困难灵巧接触任务：脆弱物体的手内操作。虽然应用领域是机器人，但其核心贡献——开发新型多模态传感器（触觉）并利用其信号通过强化学习优化接触行为——与质谱分析中开发新型仪器、获取高质量数据，并利用机器学习模型（如强化学习）优化分析流程或解释数据在方法论层面有相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we introduce SpikeATac, a multimodal tactile finger combining a taxelized and highly sensitive dynamic response (PVDF) with a static transduction method (capacitive) for multimodal touch sensing. Named for its `spiky' response, SpikeATac's 16-taxel PVDF film sampled at 4 kHz provides fast, sensitive dynamic signals to the very onset and breaking of contact. We characterize the sensitivity of the different modalities, and show that SpikeATac provides the ability to stop quickly and delicately when grasping fragile, deformable objects. Beyond parallel grasping, we show that SpikeATac can be used in a learning-based framework to achieve new capabilities on a dexterous multifingered robot hand. We use a learning recipe that combines reinforcement learning from human feedback with tactile-based rewards to fine-tune the behavior of a policy to modulate force. Our hardware platform and learning pipeline together enable a difficult dexterous and contact-rich task that has not previously been achieved: in-hand manipulation of fragile objects. Videos are available at this https URL .

</details>

---

### 59. [FMint-SDE: A Multimodal Foundation Model for Accelerating Numerical Simulation of SDEs via Error Correction](https://arxiv.org/abs/2510.27173)

**基本信息**

- 🔗 arXiv: [`2510.27173`](https://arxiv.org/abs/2510.27173)
- 👥 作者: Jiaxin Yuan, Haizhao Yang, Maria Cameron
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27173.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于加速科学计算（SDE模拟）的基础模型。分子动力学模拟是化学和生物化学研究的核心计算工具，其本质也是求解微分方程。因此，该论文提出的加速模拟的基础模型框架，与化学大模型中用于加速分子模拟或性质预测的模型在目标和技术上高度相关。

**📖 中文摘要**

本文介绍了FMint-SDE，一个基于解码器Transformer和上下文学习的多模态基础模型，用于加速随机微分方程（SDEs）的数值模拟。该模型学习一种通用的误差校正方案，通过使用传统求解器生成的粗略解序列进行提示训练，从而能够广泛泛化到不同的系统。论文在涵盖分子动力学、机械系统、金融和生物学应用的SDE基准测试套件上评估了模型。实验结果表明，与经典求解器相比，该方法实现了更优的精度-效率权衡。FMint-SDE作为一个用于动力系统模拟的通用工具，其核心思想——训练一个基础模型来校正传统数值方法的误差——对于化学模拟领域（如分子动力学模拟）具有直接的潜在应用价值，可以加速计算成本高昂的模拟过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fast and accurate simulation of dynamical systems is a fundamental challenge across scientific and engineering domains. Traditional numerical integrators often face a trade-off between accuracy and computational efficiency, while existing neural network-based approaches typically require training a separate model for each case. To overcome these limitations, we introduce a novel multi-modal foundation model for large-scale simulations of differential equations: FMint-SDE (Foundation Model based on Initialization for stochastic differential equations). Based on a decoder-only transformer with in-context learning, FMint-SDE leverages numerical and textual modalities to learn a universal error-correction scheme. It is trained using prompted sequences of coarse solutions generated by conventional solvers, enabling broad generalization across diverse systems. We evaluate our models on a suite of challenging SDE benchmarks spanning applications in molecular dynamics, mechanical systems, finance, and biology. Experimental results show that our approach achieves a superior accuracy-efficiency tradeoff compared to classical solvers, underscoring the potential of FMint-SDE as a general-purpose simulation tool for dynamical systems.

</details>

---

### 60. [FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding](https://arxiv.org/abs/2511.00141)

**基本信息**

- 🔗 arXiv: [`2511.00141`](https://arxiv.org/abs/2511.00141)
- 👥 作者: Janghoon Cho, Jungsoo Lee, Munawar Hayat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.00141.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为长序列多模态数据（视频）设计高效的信息压缩和选择方法。化学信息学和质谱分析中经常需要处理长序列或高维数据（如分子描述符向量、质谱峰列表、色谱时间序列），高效的数据压缩和特征选择是构建可扩展模型的关键。该论文的方法提供了解决这一共性问题的技术思路。

**📖 中文摘要**

本文提出了FLoC，一种基于设施选址函数的高效视觉令牌压缩框架，用于长视频理解。该方法基于一个原则性方法，在预定义的视觉令牌数量预算内，快速选择一个紧凑但具有高度代表性和多样性的视觉令牌子集。通过集成惰性贪婪算法，该方法通过快速选择紧凑的令牌子集，显著减少了视觉令牌的数量，同时保证了接近最优的性能。该方法无需训练、与模型无关且与查询无关，提供了一个可无缝集成到各种视频-LLM和现有工作流程中的通用解决方案。在Video-MME、MLVU、LongVideoBench和EgoSchema等大规模基准测试上的广泛评估表明，该框架 consistently超越了最近的压缩技术。虽然应用于视频，但其核心技术创新——为处理长序列多模态数据（视频帧）设计高效的令牌压缩/选择策略——对于处理化学中的长序列数据（如长时间分子动力学轨迹、高通量筛选数据）或复杂的质谱/光谱数据序列具有重要的方法论参考价值。高效的序列信息压缩是处理大规模科学数据的关键。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent studies in long video understanding have harnessed the advanced visual-language reasoning capabilities of Large Multimodal Models (LMMs), driving the evolution of video-LMMs specialized for processing extended video sequences. However, the scalability of these models is severely limited by the overwhelming volume of visual tokens generated from extended video sequences. To address this challenge, we propose FLoC, an efficient visual token compression framework based on the facility location function, a principled approach that swiftly selects a compact yet highly representative and diverse subset of visual tokens within a predefined budget on the number of visual tokens. By integrating the lazy greedy algorithm, our method achieves remarkable efficiency gains by swiftly selecting a compact subset of tokens, drastically reducing the number of visual tokens while guaranteeing near-optimal performance. Notably, our approach is training-free, model-agnostic, and query-agnostic, providing a versatile solution that seamlessly integrates with diverse video-LLMs and existing workflows. Extensive evaluations on large-scale benchmarks, such as Video-MME, MLVU, LongVideoBench, and EgoSchema, show that our framework consistently surpasses recent compression techniques, highlighting its effectiveness and robustness in addressing the challenges of long video understanding as well as its processing efficiency.

</details>

---

### 61. [Interleaved Tool-Call Reasoning for Protein Function Understanding](https://arxiv.org/abs/2601.03604)

**基本信息**

- 🔗 arXiv: [`2601.03604`](https://arxiv.org/abs/2601.03604)
- 👥 作者: Chuanliu Fan, Zicheng Ma, Huanran Meng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.03604.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质功能理解的工具增强推理代理（PFUA），这直接属于‘化学大模型’在生物化学领域的应用，即利用大语言模型结合领域工具进行科学推理和知识发现。

**📖 中文摘要**

本文提出PFUA，一个用于蛋白质功能理解的工具增强推理代理。论文指出，直接将基于文本的思维链推理范式（如数学和编程领域）迁移到蛋白质功能理解是无效的，因为强化学习主要放大了表面的关键词模式，而未能引入新的生物学知识。作者认为，蛋白质功能预测是一个知识密集型的科学任务，根本上依赖于外部的生物学先验和计算工具，而非纯粹的内部推理。PFUA框架统一了问题分解、工具调用和基于证据的答案生成，通过整合领域特定工具来产生可验证的中间证据，从而增强推理的可靠性和泛化能力。实验表明，PFUA在四个基准测试上持续优于纯文本推理模型，平均性能提升103%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

</details>

---

### 62. [Controlled LLM Training on Spectral Sphere](https://arxiv.org/abs/2601.08393)

**基本信息**

- 🔗 arXiv: [`2601.08393`](https://arxiv.org/abs/2601.08393)
- 👥 作者: Tian Xie, Haoming Luo, Haoyu Tang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.08393.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大规模语言模型（LLM）训练的新型优化器（SSO）。‘化学大模型’作为大模型的一个特定应用领域，其训练同样面临稳定性、效率和扩展性的挑战。该论文提出的优化方法具有普适性，可直接应用于训练化学领域的大模型，因此与核心主题相关。

**📖 中文摘要**

本文介绍了谱球优化器（SSO），这是一种用于大规模模型训练的新型优化器。SSO通过对权重及其更新施加严格的模块化谱约束，实现了与最大更新参数化理论完全对齐的优化过程。论文在包括Dense 1.7B、MoE 8B-A1B和200层DeepNet模型在内的多种架构上进行了广泛的预训练实验，证明SSO consistently outperforms AdamW和Muon等现有优化器。研究还观察到显著的实践稳定性收益，包括改进的MoE路由器负载平衡、抑制异常值和严格有界的激活值。这项工作为大模型（包括化学领域可能用到的模型）的高效、稳定训练提供了新的优化策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only ``half-aligned'' with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the \textbf{Spectral Sphere Optimizer (SSO)}, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To enable large-scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

</details>

---

### 63. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)

**基本信息**

- 🔗 arXiv: [`2601.18734`](https://arxiv.org/abs/2601.18734)
- 👥 作者: Siyan Zhao, Zhihui Xie, Mengchen Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18734.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）推理能力的自我改进框架（OPSD）。‘化学大模型’作为专注于化学领域的大模型，其核心能力之一正是复杂的科学推理（如质谱结构推理）。该论文提出的提升模型推理效率和性能的方法，对于构建和优化化学大模型具有直接的相关性和借鉴意义。

**📖 中文摘要**

本文提出了策略内自蒸馏（OPSD）框架，用于提升大语言模型的推理能力。与需要独立教师模型的传统知识蒸馏不同，OPSD让单个模型通过在不同上下文条件下同时扮演教师和学生的角色。教师策略以特权信息（如已验证的推理轨迹）为条件，而学生策略只看到问题；训练过程最小化学生自身 rollout 过程中两个分布在每个 token 上的差异。该方法在多个数学推理基准测试中证明了其有效性，实现了比强化学习方法（如GRPO）高8-12倍的token效率，并且性能优于策略外蒸馏方法。这项工作为大模型（包括可能用于化学推理的模型）的高效自我改进提供了新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self (i.e., the version without access to privileged information), we introduce On-Policy Self-Distillation (OPSD), a framework where a single model acts as both teacher and student by conditioning on different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving 8-12x token efficiency compared to reinforcement learning methods such as GRPO and superior performance over off-policy distillation methods.

</details>

---

### 64. [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2602.01601)

**基本信息**

- 🔗 arXiv: [`2602.01601`](https://arxiv.org/abs/2602.01601)
- 👥 作者: Hieu Trung Nguyen, Bao Nguyen, Wenao Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01601.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型在强化学习训练中的采样效率（VIP策略）。训练‘化学大模型’进行任务（如分子优化、反应预测）时，经常需要结合强化学习并使用模拟或计算化学工具提供可验证的奖励。该论文提出的高效采样方法 directly addresses a key challenge in scaling up the training of such chemistry-specific AI agents。

**📖 中文摘要**

本文针对具有可验证奖励的强化学习中的采样效率瓶颈，提出了VIP（方差感知预测分配）策略。现有基于组的策略优化方法（如GRPO）为所有训练提示分配固定数量的rollout，这隐含地假设所有提示信息量相同，可能导致计算预算使用效率低下。VIP使用一个轻量级高斯过程模型，根据最近的rollout来预测每个提示的成功概率，进而转化为方差估计。然后，在一个硬计算预算约束下，通过凸优化问题确定最优的rollout分配，以最小化策略更新的期望梯度方差。实验结果表明，VIP consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks。该方法对于高效训练需要大量模拟或实验验证的模型（如用于分子设计或光谱分析的化学大模型）具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce VIP, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, VIP uses a lightweight Gaussian process model to predict per-prompt success probabilities based on recent rollouts. These probability predictions are translated into variance estimates, which are then fed into a convex optimization problem to determine the optimal rollout allocations under a hard compute budget constraint. Empirical results show that VIP consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks.

</details>

---

### 65. [SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework](https://arxiv.org/abs/2602.17330)

**基本信息**

- 🔗 arXiv: [`2602.17330`](https://arxiv.org/abs/2602.17330)
- 👥 作者: Rong Fu, Zijian Zhang, Kun Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.17330.pdf)

**💡 相关性分析**

满足标准2：论文提出的SubQuad框架，通过近次二次方检索、GPU加速亲和力计算和多模态融合等技术，为解决质谱结构推理中的大规模谱图相似性比较和检索这一核心瓶颈问题提供了高效的计算方法和工具资源。

**📖 中文摘要**

这篇论文提出了SubQuad，一个用于自适应免疫受体库比较分析的计算框架。虽然其应用背景是免疫学，但其核心方法旨在解决大规模成对亲和力评估的近二次方计算成本瓶颈。论文中提出的“抗原感知、近次二次方检索”方法、GPU加速的亲和力核函数、学习的多模态融合以及公平性约束聚类，为解决“质谱结构推理”中常见的海量谱图-结构对相似性计算和检索问题提供了通用的算法思路和工具。该框架通过紧凑的MinHash预过滤、可微分门控模块和自动校准例程，显著提升了大规模数据集上的处理效率和结果公平性，其设计理念可直接迁移至化学信息学中处理质谱数据库搜索和结构推断任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Comparative analysis of adaptive immune repertoires at population scale is hampered by two practical bottlenecks: the near-quadratic cost of pairwise affinity evaluations and dataset imbalances that obscure clinically important minority clonotypes. We introduce SubQuad, an end-to-end pipeline that addresses these challenges by combining antigen-aware, near-subquadratic retrieval with GPU-accelerated affinity kernels, learned multimodal fusion, and fairness-constrained clustering. The system employs compact MinHash prefiltering to sharply reduce candidate comparisons, a differentiable gating module that adaptively weights complementary alignment and embedding channels on a per-pair basis, and an automated calibration routine that enforces proportional representation of rare antigen-specific subgroups. On large viral and tumor repertoires SubQuad achieves measured gains in throughput and peak memory usage while preserving or improving recall@k, cluster purity, and subgroup equity. By co-designing indexing, similarity fusion, and equity-aware objectives, SubQuad offers a scalable, bias-aware platform for repertoire mining and downstream translational tasks such as vaccine target prioritization and biomarker discovery.

</details>

---

### 66. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型（Zatom-1），这直接围绕“化学大模型”这一主题。

**📖 中文摘要**

本文介绍了Zatom-1，一个用于3D分子和材料的统一多模态流匹配基础模型。该模型是一个Transformer，通过联合建模离散原子类型和连续3D几何的流匹配目标进行训练。Zatom-1统一了生成（如分子生成）和预测（如性质预测）任务，支持对分子和材料进行可扩展的预训练和快速采样。论文明确指出，该模型在生成和预测基准测试上都达到或超过了专业基线模型的性能，同时将生成推理时间减少了一个数量级以上。这项工作直接面向“化学大模型”的核心主题，即开发能够统一处理多种化学任务（生成与预测）且可扩展的基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first end-to-end, fully open-source foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 67. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个高效、准确的机器学习原子间势（MLIP）基础模型（MatRIS），这直接属于“化学大模型”在计算材料科学方向的研究范畴。

**📖 中文摘要**

本文提出了MatRIS，一个用于材料科学的机器学习原子间势（MLIP）基础模型。针对当前等变MLIP计算成本高的问题，MatRIS引入了一种基于注意力机制的三体相互作用建模方法，并采用具有线性复杂度的可分离注意力机制，实现了可扩展性和表达能力的平衡。论文在包括Matbench-Discovery、MatPES在内的多个流行基准测试上验证了MatRIS的准确性，其性能与领先的等变模型相当，但训练成本更低。这项工作致力于开发准确且高效的MLIP，是构建面向材料科学的“化学大模型”的重要尝试，其模型架构和训练方法对该领域具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 68. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准1：论文的核心理论分析旨在为现代机器学习系统中的顺序推理提供原理性解释，这直接关联到“化学大模型”等复杂模型内部可能涉及的推理与检索机制。

**📖 中文摘要**

本文为输入驱动的Hopfield网络中的顺序检索开发了一套动力学理论。论文分析了耦合快速关联检索与慢速推理动力学的双时间尺度架构，推导了自维持记忆转换的明确条件。作者指出，理解关联记忆模型中的检索和顺序性，为了解机器学习中的推理（如语言理解和多模态生成）提供了强大的桥梁。虽然论文更偏向理论计算机科学和动力学系统，但其明确将现代推理架构（如基于字典或原型模式操作的ML系统）与经典的Hopfield动力学联系起来，为理解“化学大模型”或“质谱结构推理”模型中可能涉及的顺序推理和记忆检索机制提供了理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 69. [Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning](https://arxiv.org/abs/2603.03229)

**基本信息**

- 🔗 arXiv: [`2603.03229`](https://arxiv.org/abs/2603.03229)
- 👥 作者: Adam Watts, Andrew Jeon, Destry Newton 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03229.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于CVAE的深度生成建模方法，为解决“从谱图逆向重建原始信号/结构”这一类逆问题（与质谱结构推理问题同构）提供了通用的算法框架和工具思路。

**📖 中文摘要**

本文提出使用条件变分自编码器（CVAE）从冲击响应谱（SRS）曲线逆向重建加速度时间序列。该方法学习了一个从SRS到时间序列的数据驱动逆映射，无需迭代优化即可生成符合目标谱的信号。虽然应用场景是工程动力学，但论文解决的核心问题是“从谱图逆向重建原始信号”，这与“质谱结构推理”中“从质谱图推断分子结构”这一逆问题在数学形式和挑战上高度相似（都是非线性、多对一的逆映射问题）。论文提出的深度生成建模方法为处理此类逆问题提供了一个可扩展且高效的范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions. We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

</details>

---

### 70. [LoRA-MME: Multi-Model Ensemble of LoRA-Tuned Encoders for Code Comment Classification](https://arxiv.org/abs/2603.03959)

**基本信息**

- 🔗 arXiv: [`2603.03959`](https://arxiv.org/abs/2603.03959)
- 👥 作者: Md Akib Haider, Ahsan Bulbul, Nafis Fuad Shahid 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03959.pdf)

**💡 相关性分析**

满足标准2：论文详细展示了使用低秩适应（LoRA）对多个Transformer模型进行参数高效微调并集成的完整技术流程，这为构建和优化领域特定的“化学大模型”提供了可直接借鉴的方法和工具实践。

**📖 中文摘要**

本文介绍了LoRA-MME，一个用于代码注释分类的多模型集成架构，采用了参数高效微调（PEFT）技术。虽然应用领域是软件工程，但论文的核心方法——使用低秩适应（LoRA）独立微调多个Transformer编码器（如UniXcoder, CodeBERT），并通过学习的加权集成策略聚合预测——是当前构建和优化“化学大模型”时广泛采用的关键技术之一。LoRA作为一种高效的微调方法，对于在特定化学数据集上适配大型预训练模型（如用于分子性质预测或反应预测）至关重要。该论文为如何有效集成多个经LoRA微调的专家模型提供了具体案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Code comment classification is a critical task for automated software documentation and analysis. In the context of the NLBSE'26 Tool Competition, we present LoRA-MME, a Multi-Model Ensemble architecture utilizing Parameter-Efficient Fine-Tuning (PEFT). Our approach addresses the multi-label classification challenge across Java, Python, and Pharo by combining the strengths of four distinct transformer encoders: UniXcoder, CodeBERT, GraphCodeBERT, and CodeBERTa. By independently fine-tuning these models using Low-Rank Adaptation(LoRA) and aggregating their predictions via a learned weighted ensemble strategy, we maximize classification performance without the memory overhead of full model fine-tuning. Our tool achieved an F1 Weighted score of 0.7906 and a Macro F1 of 0.6867 on the test set. However, the computational cost of the ensemble resulted in a final submission score of 41.20%, highlighting the trade-off between semantic accuracy and inference efficiency.

</details>

---

### 71. [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)

**基本信息**

- 🔗 arXiv: [`2603.04384`](https://arxiv.org/abs/2603.04384)
- 👥 作者: Zijian Chen, Xueguang Ma, Shengyao Zhuang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04384.pdf)

**💡 相关性分析**

满足标准2：论文提出的“推理感知检索”范式和配套的数据合成方法，为开发需要复杂知识检索能力的“化学大模型”或研究辅助系统提供了新颖的检索架构和工具思路。

**📖 中文摘要**

本文提出了AgentIR，一个用于深度研究智能体的推理感知检索框架。针对现有检索器忽略智能体推理过程所包含的丰富意图和上下文信息的问题，该工作引入了“推理感知检索”范式，将智能体的推理轨迹与其查询共同嵌入。同时，提出了DR-Synth数据合成方法，从标准QA数据集生成训练数据。最终训练的嵌入模型AgentIR-4B在检索基准上表现优异。这项工作虽然面向通用AI智能体，但其核心思想——利用模型内部推理过程（而不仅仅是最终查询）来增强检索——对于构建需要从海量文献或数据库中检索相关化学知识、反应路径或谱图信息的“化学大模型”或“质谱结构推理”系统具有重要的方法论启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep Research agents are rapidly emerging as primary consumers of modern retrieval systems. Unlike human users who issue and refine queries without documenting their intermediate thought processes, Deep Research agents generate explicit natural language reasoning before each search call, revealing rich intent and contextual information that existing retrievers entirely ignore. To exploit this overlooked signal, we introduce: (1) Reasoning-Aware Retrieval, a retrieval paradigm that jointly embeds the agent's reasoning trace alongside its query; and (2) DR-Synth, a data synthesis method that generates Deep Research retriever training data from standard QA datasets. We demonstrate that both components are independently effective, and their combination yields a trained embedding model, AgentIR-4B, with substantial gains. On the challenging BrowseComp-Plus benchmark, AgentIR-4B achieves 68\% accuracy with the open-weight agent Tongyi-DeepResearch, compared to 50\% with conventional embedding models twice its size, and 37\% with BM25. Code and data are available at: this https URL .

</details>

---

### 72. [CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery](https://arxiv.org/abs/2511.19500)

**基本信息**

- 🔗 arXiv: [`2511.19500`](https://arxiv.org/abs/2511.19500)
- 👥 作者: Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.19500.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学大模型（用于分子生成和性质预测的机器学习模型）展开，并应用于化学材料发现。

**📖 中文摘要**

本文提出了一个用于有机光伏（OPV）材料发现的机器学习框架CycleChemist。该框架结合了预测建模和生成式分子设计，并引入了OPV2D数据集，这是目前最大的、包含2000个实验表征的供体-受体对的精选数据集。框架包含用于预测材料是否具有OPV行为的分类器（OPVC）、用于预测HOMO和LUMO能级的分子轨道能量估计器（MOE2）、用于估计功率转换效率（PCE）的光伏性能预测器（P3），以及用于生成可合成有机半导体的生成式模型（MatGPT）。该工作通过将分子表示学习与性能预测相结合，推动了高性能OPV材料的数据驱动发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials.

</details>

---

### 73. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学大模型（化学大语言模型）的推理机制进行创新，提出了新的潜在推理范式。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）依赖显式自然语言思维链（CoT）进行推理的局限性。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中进行多步推理，仅对最终输出生成语言。研究表明，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐步放弃冗长的文本推导，转而采用隐式的潜在计算。在多个化学推理基准测试中，LatentChem相比基于CoT的基线模型取得了显著优势，并实现了平均10.84倍的推理加速。这为化学推理更自然地实现为连续潜在动态过程而非离散语言轨迹提供了实证证据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 74. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及为分子（作为图结构）的预测提供不确定性量化框架，这与化学信息学中的分子性质预测和质谱结构推理（将质谱数据映射到分子结构图）高度相关。

**📖 中文摘要**

本文提出了一种用于图结构输出的保形预测框架，旨在为结构化输出空间（如图）提供分布无关的覆盖保证。该方法通过Z-Gromov-Wasserstein距离（实践中实例化为Fused Gromov-Wasserstein距离）来定义非保形性度量，从而实现对预测图和候选图之间置换不变的比较。为了获得自适应的预测集，作者将保形化分位数回归（CQR）扩展到复杂输出空间，提出了分数保形化分位数回归（SCQR）。论文在一个合成任务和一个真实的分子识别问题上评估了所提出的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 75. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用多智能体框架（一种高级的AI/大模型应用形式）来自动化化学计算（DFT）的核心工作流，直接服务于化学信息学领域。

**📖 中文摘要**

本文介绍了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学的基石，但其实际执行涉及协调复杂、多步骤的工作流。TritonDFT通过专家策划、可扩展的工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效、准确的DFT执行。该框架旨在解决现有工具和基于LLM的解决方案在支持完整工作流自动化、多样化任务适应以及DFT配置中精度-成本权衡优化方面的不足。此外，作者还引入了DFTBench基准，用于评估智能体在科学专业知识、权衡优化、高性能计算知识和成本效率等多维度的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：18
- 累计论文数量：1268

## 📝 历史记录

> 暂无历史数据

