# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-06 12:57:39

## 📅 2026-03-06 (今日最新)

**相关论文数：61**

### 1. [A unified foundational framework for knowledge injection and evaluation of Large Language Models in Combustion Science](https://arxiv.org/abs/2603.04452)

**基本信息**

- 🔗 arXiv: [`2603.04452`](https://arxiv.org/abs/2603.04452)
- 👥 作者: Zonglin Yang, Runze Mao, Tianhao Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04452.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕为特定化学领域（燃烧科学）构建和评估专业化的大语言模型（化学大模型）这一主题展开。

**📖 中文摘要**

本文提出了一个用于燃烧科学领域大语言模型（LLM）开发的端到端框架。该框架包含一个规模达35亿token的多模态知识库（从20万篇同行评议文章、8000篇学位论文和约40万行燃烧CFD代码中提取）、一个严格的自动化评估基准（CombustionQA，包含8个子领域的436个问题）以及一个三阶段知识注入路径。该路径从轻量级的检索增强生成（RAG）开始，逐步发展到知识图谱增强检索和持续预训练。作者验证了第一阶段（朴素RAG）存在性能上限（准确率峰值60%），并指出其性能受限于上下文污染，因此需要后续阶段的结构化知识图谱和持续预训练来构建领域基础模型。这项工作直接针对“化学大模型”主题，旨在为特定科学领域（燃烧学）构建和评估专业化的大语言模型。

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

满足标准1：论文的核心研究内容是利用来自其他模态的大模型（作为“教师”）来引导和优化特定科学数据模态（EEG）的基础模型，这直接涉及“化学大模型”中模型构建、知识迁移和优化的核心议题。

**📖 中文摘要**

本文提出了一种用于脑电图（EEG）基础模型预训练的新框架——多教师蒸馏预训练（MTDP）。与主流EEG基础模型依赖自监督掩码重建不同，MTDP通过两阶段多教师蒸馏，利用来自其他成熟模态（如视觉和时间序列）的基础模型（如DINOv3和Chronos）的知识来引导EEG模型的预训练。第一阶段，通过一个可学习的门控网络，将来自不同教师的表示与掩码潜在去噪目标融合。第二阶段，将融合后的表示蒸馏到一个EEG基础模型中。在9个下游任务和12个数据集上的广泛评估表明，MTDP模型优于自监督对比模型，且仅需25%的预训练数据。这项工作涉及利用大模型（视觉、时间序列基础模型）来提升特定科学数据模态（EEG）模型的性能，属于跨模态的模型构建与优化。

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

满足标准1：论文的核心研究内容是利用对比学习和大模型技术，对齐科学观测数据（X射线光谱）与科学文献文本，构建共享的多模态表示，这直接涉及科学领域（此处为天文学，但其方法论可推广至化学）中大模型的应用。

**📖 中文摘要**

本文引入了一个对比学习框架，旨在将X射线光谱与从科学文献中提取的领域知识对齐，以促进共享多模态表示的发展。建立这种联系非常复杂，因为科学文本比光谱包含更广泛、更多样化的物理背景。作者提出的对比学习流程在从光谱检索文本时实现了20%的Recall@1%，证明这两种模态之间有意义的对齐不仅是可能的，而且能够加速对稀有或理解不足的天体源的解释。此外，得到的共享潜在空间有效地编码了具有物理意义的信息。通过融合光谱和文本数据，与单模态光谱基线相比，对20个物理变量的估计提高了16-18%。这项工作展示了如何将观测数据（光谱）与科学文献（文本）通过大模型驱动的表示学习进行对齐和融合，以提升科学发现能力。

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

满足标准1：论文的核心研究内容是设计一个多智能体系统，通过与大模型类似的推理和学习过程，自主发现数学概念。虽然领域是数学，但其“从数据中自主发现结构/概念”的核心范式与“质谱结构推理”中从质谱数据推断分子结构在方法论上高度相关，都属于从复杂数据中推理出潜在结构的问题。

**📖 中文摘要**

本文提出了一种新的用于计算数学发现的多智能体模型。该系统自主提出猜想并尝试证明它们，根据反馈和不断演化的数据分布做出决策。受欧拉多面体猜想历史和文献中一个开放挑战的启发，作者使用从线性代数知识和多面体数据中自主恢复同调概念的任务进行基准测试。该系统完成了这个学习问题。最重要的是，实验是消融研究，统计测试了完整动态的价值并控制了实验设置。它们支持作者的主要主张：优化正确的局部过程组合可以导致与数学趣味性惊人一致的概念。这项工作展示了多智能体系统与大模型结合在自主科学概念发现（包括数学，可类比于化学中的结构发现）中的潜力。

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

满足标准1：论文的核心研究内容是利用从现实世界收集的数据来蒸馏和优化模型（状态估计器），以提升机器人的操作性能。这种方法论——使用真实数据改进和专业化模型——与“化学大模型”领域中利用领域数据微调或构建专业化模型的核心思路一致。

**📖 中文摘要**

本文提出了PTLD：从模拟到现实的特权触觉潜在蒸馏，一种无需触觉模拟即可学习触觉操作技能的新方法。其核心思想是利用现实世界中的特权传感器收集真实的触觉策略数据，然后用于蒸馏一个在触觉输入上操作的鲁棒状态估计器。作者证明，PTLD可用于通过结合触觉传感来显著改进在模拟中训练的本体感知操作策略。在基准手内旋转任务上，PTLD比纯本体感知策略提高了182%。这项工作涉及利用特权信息（在现实中收集的触觉数据）来蒸馏和提升模型（状态估计器）的性能，属于机器人学习中的模型优化和迁移范畴。

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

满足标准1：论文的核心研究内容是从复杂数据（视频）中无监督地学习物体中心的结构化表示，并用于建模动态和决策。这种“从数据中推断结构”的核心范式与“质谱结构推理”中从质谱数据推断分子结构在概念上高度相似，都属于从非结构化或高维数据中恢复潜在结构的问题。

**📖 中文摘要**

本文介绍了潜在粒子世界模型（LPWM），一个可扩展到真实世界多物体数据集并适用于决策的自监督物体中心世界模型。LPWM直接从视频数据中自主发现关键点、边界框和物体掩码，使其能够在没有监督的情况下学习丰富的场景分解。该架构完全从视频端到端训练，并支持对动作、语言和图像目标的灵活条件化。LPWM通过新颖的潜在动作模块对随机粒子动力学进行建模，并在多样化的真实世界和合成数据集上取得了最先进的结果。除了随机视频建模，LPWM很容易应用于决策，包括目标条件模仿学习。这项工作展示了从多模态数据（视频）中无监督地发现结构化表示（物体、关键点），并用于后续推理和决策。

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

满足标准1：论文的核心研究内容是使用先进的生成模型（扩散模型）和微调技术（LoRA），在生物医学图像模态上进行以结构（细胞核中心点）为指导的合成与修复。这直接涉及复杂科学数据（组织病理学图像）的生成与推理，其方法论可类比于化学信息学中分子结构的生成与预测。

**📖 中文摘要**

本文提出了双LoRA可控扩散，一个统一的以中心点为指导的扩散框架，在单个模型内联合支持局部结构完成和全局结构合成。多类细胞核中心点作为轻量级且注释高效的空间先验，在部分和完全图像缺失的情况下提供具有生物学意义的指导。两个任务特定的LoRA适配器使共享主干专门用于局部和全局目标，而无需重新训练单独的扩散模型。大量实验表明，在修复和合成任务上，该方法相对于最先进的GAN和扩散基线模型有一致的改进。该方法在掩码区域内实现了更忠实的结构恢复，在完整合成中实现了显著改善的真实感和形态一致性，支持可扩展的泛癌组织病理学建模。这项工作涉及使用扩散模型和适配器技术（LoRA）进行生物医学图像（组织病理学）的结构化合成与修复。

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

满足标准1：论文的核心研究内容是使用预训练的PDE基础模型解决科学逆问题（参数估计），这直接属于“化学大模型”在科学计算和推理应用范畴的延伸讨论。

**📖 中文摘要**

本文研究了偏微分方程（PDE）基础模型在惯性约束聚变（ICF）逆问题中的应用，即从多模态观测数据中估计系统参数。研究利用JAG基准数据集，通过微调PDE基础模型并训练一个轻量级的任务特定头，来联合重建高光谱图像和回归系统参数。该工作展示了基础模型在数据受限的逆问题中，通过预训练初始化提升样本效率的能力。虽然应用领域是物理模拟，但其核心方法——使用预训练的基础模型解决复杂的、数据驱动的科学逆问题——与“化学大模型”的主题高度相关，因为它展示了基础模型范式在科学计算和参数推理中的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PDE foundation models are typically pretrained on large, diverse corpora of PDE datasets and can be adapted to new settings with limited task-specific data. However, most downstream evaluations focus on forward problems, such as autoregressive rollout prediction. In this work, we study an inverse problem in inertial confinement fusion (ICF): estimating system parameters (inputs) from multi-modal, snapshot-style observations (outputs). Using the open JAG benchmark, which provides hyperspectral X-ray images and scalar observables per simulation, we finetune the PDE foundation model and train a lightweight task-specific head to jointly reconstruct hyperspectral images and regress system parameters. The fine-tuned model achieves accurate hyperspectral reconstruction (test MSE 1.2e-3) and strong parameter-estimation performance (up to R^2=0.995). Data-scaling experiments (5%-100% of the training set) show consistent improvements in both reconstruction and regression losses as the amount of training data increases, with the largest marginal gains in the low-data regime. Finally, finetuning from pretrained MORPH weights outperforms training the same architecture from scratch, demonstrating that foundation-model initialization improves sample efficiency for data-limited inverse problems in ICF.

</details>

---

### 9. [Spinverse: Differentiable Physics for Permeability-Aware Microstructure Reconstruction from Diffusion MRI](https://arxiv.org/abs/2603.04638)

**基本信息**

- 🔗 arXiv: [`2603.04638`](https://arxiv.org/abs/2603.04638)
- 👥 作者: Prathamesh Pradeep Khole, Mario M. Brenes, Zahra Kais Petiwala 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04638.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从测量信号（dMRI）中逆向估计物理参数和结构，这本质上是一个“结构推理”问题。其方法论——使用可微分物理模拟器和优化进行逆问题求解——与“质谱结构推理”中从质谱信号推断分子结构的计算范式高度相似，属于同一类科学计算逆问题。

**📖 中文摘要**

本文提出了Spinverse，一种用于从扩散MRI（dMRI）测量中重建具有渗透性感知的微观结构的方法。该方法通过一个完全可微分的Bloch-Torrey模拟器来反演dMRI信号。Spinverse在固定的四面体网格上表示组织，并将每个内部面的渗透性作为可学习参数；低渗透性面充当扩散屏障，从而在不改变网格连接或顶点位置的情况下，出现拓扑不固定的微观结构边界。给定目标信号，通过通过PDE前向模型反向传播信号匹配损失来优化面渗透性，并通过阈值化学习到的渗透性场来恢复界面。该工作解决了从测量数据中推断复杂微观结构（包括边界和渗透性）的逆问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion MRI (dMRI) is sensitive to microstructural barriers, yet most existing methods either assume impermeable boundaries or estimate voxel-level parameters without recovering explicit interfaces. We present Spinverse, a permeability-aware reconstruction method that inverts dMRI measurements through a fully differentiable Bloch-Torrey simulator. Spinverse represents tissue on a fixed tetrahedral grid and treats each interior face permeability as a learnable parameter; low-permeability faces act as diffusion barriers, so microstructural boundaries whose topology is not fixed a priori (up to the resolution of the ambient mesh) emerge without changing mesh connectivity or vertex positions. Given a target signal, we optimize face permeabilities by backpropagating a signal-matching loss through the PDE forward model, and recover an interface by thresholding the learned permeability field. To mitigate the ill-posedness of permeability inversion, we use mesh-based geometric priors; to avoid local minima, we use a staged multi-sequence optimization curriculum. Across a collection of synthetic voxel meshes, Spinverse reconstructs diverse geometries and demonstrates that sequence scheduling and regularization are critical to avoid outline-only solutions while improving both boundary accuracy and structural validity.

</details>

---

### 10. [Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings](https://arxiv.org/abs/2603.04692)

**基本信息**

- 🔗 arXiv: [`2603.04692`](https://arxiv.org/abs/2603.04692)
- 👥 作者: Lyle Regenwetter, Rosen Yu, Cyril Picard 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04692.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对特定领域（工程/科学）数据，对预训练的“表格基础模型”进行领域适应和性能提升。这直接围绕“化学大模型”主题下的一个关键子问题：如何让基础模型更好地适应化学、材料等科学领域的表格数据，并解决数据稀缺问题。

**📖 中文摘要**

本文研究了表格回归任务中，预训练的表格基础模型（如TabPFN）向工程领域迁移时存在的领域差距问题。作者引入了TREDBench，一个包含83个真实世界表格回归数据集的精选集合，并利用TabPFN 2.5的数据集级嵌入来研究公共表示空间中的领域结构。研究发现，工程数据集与非工程数据集部分可区分，而标准程序生成的数据集与工程数据集高度可区分，揭示了显著的合成-真实领域差距。为了在不使用真实工程样本训练的情况下弥合这一差距，作者提出了一种嵌入引导的合成数据筛选方法：生成并识别“类工程”合成数据集，并仅使用选定的合成任务对TabPFN 2.5进行持续预训练。在35个工程回归数据集上的评估表明，这种仅使用合成数据的适应方法提高了预测准确性和数据效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression datasets with expert engineering/non-engineering labels, and use TabPFN 2.5's dataset-level embedding to study domain structure in a common representation space. We find that engineering datasets are partially distinguishable from non-engineering datasets, while standard procedurally generated datasets are highly distinguishable from engineering datasets, revealing a substantial synthetic-real domain gap. To bridge this gap without training on real engineering samples, we propose an embedding-guided synthetic data curation method: we generate and identify "engineering-like" synthetic datasets, and perform continued pre-training of TabPFN 2.5 using only the selected synthetic tasks. Across 35 engineering regression datasets, this synthetic-only adaptation improves predictive accuracy and data efficiency, outperforming TabPFN 2.5 on 29/35 datasets and AutoGluon on 27/35, with mean multiplicative data-efficiency gains of 1.75x and 4.44x, respectively. More broadly, our results indicate that principled synthetic data curation can convert procedural generators into domain-relevant "data engines," enabling foundation models to improve in data-sparse scientific and industrial domains where real data collection is the primary bottleneck.

</details>

---

### 11. [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](https://arxiv.org/abs/2603.04743)

**基本信息**

- 🔗 arXiv: [`2603.04743`](https://arxiv.org/abs/2603.04743)
- 👥 作者: Maojun Sun, Yue Wu, Yifei Xie 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04743.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门为R统计生态系统（化学信息学和质谱分析中广泛使用的工具链）构建的检索增强工具（DARE模型、RPKB知识库）和智能体框架（RCodingAgent）。这些资源可直接用于辅助化学数据分析和建模任务，属于“数据资源相关”。

**📖 中文摘要**

本文提出了DARE（分布感知检索嵌入），一个轻量级、即插即用的检索模型，用于将数据分布信息融入R函数表示中，以改进R包检索。主要贡献包括：(i) RPKB，一个从8,191个高质量CRAN包中提取的精选R包知识库；(ii) DARE，一个融合分布特征与函数元数据的嵌入模型，以提高检索相关性；(iii) RCodingAgent，一个面向R的LLM智能体，用于可靠的R代码生成，以及一套用于系统评估LLM智能体在现实分析场景中表现的统计分析任务。实证表明，DARE在包检索上实现了93.47%的NDCG@10，优于最先进的开源嵌入模型。将DARE集成到RCodingAgent中，在下游分析任务上带来了显著增益。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

</details>

---

### 12. [MOOSEnger -- a Domain-Specific AI Agent for the MOOSE Ecosystem](https://arxiv.org/abs/2603.04756)

**基本信息**

- 🔗 arXiv: [`2603.04756`](https://arxiv.org/abs/2603.04756)
- 👥 作者: Mengnan Li, Jason Miller, Zachary Prince 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04756.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个针对科学计算框架（MOOSE）的专用AI智能体，它集成了检索、解析、验证和执行工具。虽然领域是物理模拟，但其构建“领域特定AI助手”的方法论和工具链，为在“化学信息学”中构建类似的、用于分子模拟或光谱分析流程的智能体提供了可借鉴的蓝图和潜在资源。

**📖 中文摘要**

本文介绍了MOOSEnger，一个专为多物理场面向对象模拟环境（MOOSE）定制的工具增强AI智能体。MOOSE案例在HIT ".i"输入文件中指定；庞大的对象目录和严格的语法使得初始设置和调试速度缓慢。MOOSEnger提供了一个对话式工作流，通过结合对精选文档/示例的检索增强生成（RAG）与确定性的、MOOSE感知的解析、验证和执行工具，将自然语言意图转化为可运行的输入。该智能体包含一个核心加领域架构，将可重用的智能体基础设施与MOOSE插件分离。论文在包含125个提示的基准测试上进行了评估，涵盖了扩散、瞬态热传导、固体力学、多孔流和不可压缩Navier-Stokes等领域，MOOSEnger实现了0.93的执行通过率，而纯LLM基线的通过率仅为0.08。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MOOSEnger is a tool-enabled AI agent tailored to the Multiphysics Object-Oriented Simulation Environment (MOOSE). MOOSE cases are specified in HIT ".i" input files; the large object catalog and strict syntax make initial setup and debugging slow. MOOSEnger offers a conversational workflow that turns natural-language intent into runnable inputs by combining retrieval-augmented generation over curated docs/examples with deterministic, MOOSE-aware parsing, validation, and execution tools. A core-plus-domain architecture separates reusable agent infrastructure (configuration, registries, tool dispatch, retrieval services, persistence, and evaluation) from a MOOSE plugin that adds HIT-based parsing, syntax-preserving ingestion of input files, and domain-specific utilities for input repair and checking. An input precheck pipeline removes hidden formatting artifacts, fixes malformed HIT structure with a bounded grammar-constrained loop, and resolves invalid object types via similarity search over an application syntax registry. Inputs are then validated and optionally smoke-tested with the MOOSE runtime in the loop via an MCP-backed execution backend (with local fallback), translating solver diagnostics into iterative verify-and-correct updates. Built-in evaluation reports RAG metrics (faithfulness, relevancy, context precision/recall) and end-to-end success by actual execution. On a 125-prompt benchmark spanning diffusion, transient heat conduction, solid mechanics, porous flow, and incompressible Navier--Stokes, MOOSEnger achieves a 0.93 execution pass rate versus 0.08 for an LLM-only baseline.

</details>

---

### 13. [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827)

**基本信息**

- 🔗 arXiv: [`2603.04827`](https://arxiv.org/abs/2603.04827)
- 👥 作者: Ben S. Southworth, Jonas A. Actor, Graham Harper 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种新型的神经网络架构（Kolmogorov-Arnold Networks）及其高效训练算法。KANs作为近期提出的、具有特定数学基础（Kolmogorov-Arnold表示定理）的模型，是‘化学大模型’在模型架构层面的一个具体而新颖的实例。论文重点探讨了如何利用其结构特性进行加速训练，这直接关系到构建和优化用于化学信息学等领域的大规模模型。

**📖 中文摘要**

本文研究了Kolmogorov-Arnold网络（KANs）的多级训练方法。KANs是一种具有明确结构（通过指定基函数展开学习到的激活函数）的神经网络，与多层感知机（MLP）相比，其结构更利于算法加速。作者首先建立了使用样条基函数的KANs与使用幂ReLU激活函数的多通道MLPs之间的等价关系。基于此，他们提出了一种多级训练策略：通过样条节点的均匀细化，自然地定义一系列KANs模型，并利用解析几何插值算子在不同层级的模型之间进行转换。这种插值方案确保了在精细模型上能保留在粗糙模型上取得的进展，而样条基函数的紧支撑特性则保证了在后续层级上的互补优化。数值实验表明，该方法在训练可比的KANs或MLPs时，相比传统方法能实现数量级上的精度提升，特别是在物理信息神经网络（PINN）中。这项工作展示了神经网络的有原则设计如何带来可利用的结构，从而实现能显著提升训练性能的多级算法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

</details>

---

### 14. [HACHIMI: Scalable and Controllable Student Persona Generation via Orchestrated Agents](https://arxiv.org/abs/2603.04855)

**基本信息**

- 🔗 arXiv: [`2603.04855`](https://arxiv.org/abs/2603.04855)
- 👥 作者: Yilin Jiang, Fei Tan, Xuanyu Yin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04855.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是生成了一个大规模、结构化、理论对齐的合成数据集（HACHIMI-1M语料库）。该数据集包含100万个详细的学生画像，并提供了生成框架和评估方法。这种高质量、大规模、可控的合成数据生成方法和资源，对于训练和评估需要理解复杂、结构化实体的‘化学大模型’（例如，用于预测分子性质或反应，需要理解反应物、条件、产物等实体及其关系）具有重要的参考价值和直接应用潜力，可作为构建或增强领域特定数据集的范例。

**📖 中文摘要**

本文提出了HACHIMI，一个用于生成理论对齐且分布可控的学生画像（Student Personas, SPs）的多智能体框架。作者将问题形式化为理论对齐和分布可控的画像生成（TAD-PG）。HACHIMI采用“提议-验证-修订”框架，将每个画像分解为一个理论锚定的教育模式，通过神经符号验证器强制执行发展和心理约束，并结合分层抽样与语义去重来减少模式崩溃。生成的HACHIMI-1M语料库包含100万个1至12年级的学生画像。内在评估显示其模式有效性近乎完美，配额准确且多样性丰富。外部评估则将画像实例化为回答CEPS和PISA 2022调查的学生智能体；在16个队列中，数学和好奇心/成长结构与人类数据高度一致，而课堂氛围和幸福感结构仅中度一致，揭示了一种保真度梯度。所有画像均使用Qwen2.5-72B生成。HACHIMI为群体层面的基准测试和社会科学模拟提供了一个标准化的合成学生群体。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Student Personas (SPs) are emerging as infrastructure for educational LLMs, yet prior work often relies on ad-hoc prompting or hand-crafted profiles with limited control over educational theory and population distributions. We formalize this as Theory-Aligned and Distribution-Controllable Persona Generation (TAD-PG) and introduce HACHIMI, a multi-agent Propose-Validate-Revise framework that generates theory-aligned, quota-controlled personas. HACHIMI factorizes each persona into a theory-anchored educational schema, enforces developmental and psychological constraints via a neuro-symbolic validator, and combines stratified sampling with semantic deduplication to reduce mode collapse. The resulting HACHIMI-1M corpus comprises 1 million personas for Grades 1-12. Intrinsic evaluation shows near-perfect schema validity, accurate quotas, and substantial diversity, while external evaluation instantiates personas as student agents answering CEPS and PISA 2022 surveys; across 16 cohorts, math and curiosity/growth constructs align strongly between humans and agents, whereas classroom-climate and well-being constructs are only moderately aligned, revealing a fidelity gradient. All personas are generated with Qwen2.5-72B, and HACHIMI provides a standardized synthetic student population for group-level benchmarking and social-science simulations. Resources available at this https URL

</details>

---

### 15. [SEA-TS: Self-Evolving Agent for Autonomous Code Generation of Time Series Forecasting Algorithms](https://arxiv.org/abs/2603.04873)

**基本信息**

- 🔗 arXiv: [`2603.04873`](https://arxiv.org/abs/2603.04873)
- 👥 作者: Longkun Xu, Xiaochun Zhang, Qiantu Tuo 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04873.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个能够自主生成和优化时间序列预测算法代码的智能体框架（SEA-TS）。这本质上是一个用于特定科学计算任务（时间序列预测）的‘化学大模型’或‘科学大模型’的构建与优化范式。其核心思想——利用大型语言模型（LLM）作为基础，结合搜索、评估和迭代优化来自主生成高性能代码——与构建用于化学信息学（如自主设计实验、优化分子生成模型参数）的智能体或大模型的研究主题高度相关，是‘化学大模型’在自动化科学发现和代码生成方向上的一个具体应用和探索。

**📖 中文摘要**

本文提出了SEA-TS，一个用于时间序列预测算法代码自主生成、验证和优化的自进化框架。该框架通过迭代的自进化循环工作，包含三个关键创新：(1) 度量优势蒙特卡洛树搜索（MA-MCTS），用归一化优势分数替代固定奖励，以提供有区分度的搜索指导；(2) 带有运行提示词精炼的代码审查，每个执行的解决方案都经过自动审查，随后更新提示词以编码纠正模式，防止类似错误复发；(3) 全局可引导推理，将每个节点与全局最佳和最差解决方案进行比较，实现跨轨迹知识转移。该框架采用MAP-Elites存档来维持架构多样性。在公开的Solar-Energy基准测试和专有数据集上的实验表明，SEA-TS生成的代码在预测精度上超越了最先进的方法和人工设计的基线，并且进化出的模型发现了新颖的架构模式。这证明了自主机器学习工程能够产生超越手动设计的真正新颖的算法思想。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate time series forecasting underpins decision-making across domains, yet conventional ML development suffers from data scarcity in new deployments, poor adaptability under distribution shift, and diminishing returns from manual iteration. We propose Self-Evolving Agent for Time Series Algorithms (SEA-TS), a framework that autonomously generates, validates, and optimizes forecasting code via an iterative self-evolution loop. Our framework introduces three key innovations: (1) Metric-Advantage Monte Carlo Tree Search (MA-MCTS), which replaces fixed rewards with a normalized advantage score for discriminative search guidance; (2) Code Review with running prompt refinement, where each executed solution undergoes automated review followed by prompt updates that encode corrective patterns, preventing recurrence of similar errors; and (3) Global Steerable Reasoning, which compares each node against global best and worst solutions, enabling cross-trajectory knowledge transfer. We adopt a MAP-Elites archive for architectural diversity. On the public Solar-Energy benchmark, SEA-TS generated code achieves a 40% MAE reduction relative to TimeMixer, surpassing state-of-the-art methods. On proprietary datasets, SEA-TS generated code reduces WAPE by 8.6% on solar PV forecasting and 7.7% on residential load forecasting compared to human-engineered baselines, and achieves 26.17% MAPE on load forecasting versus 29.34% by TimeMixer. Notably, the evolved models discover novel architectural patterns--including physics-informed monotonic decay heads encoding solar irradiance constraints, per-station learned diurnal cycle profiles, and learnable hourly bias correction--demonstrating that autonomous ML engineering can generate genuinely novel algorithmic ideas beyond manual design.

</details>

---

### 16. [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900)

**基本信息**

- 🔗 arXiv: [`2603.04900`](https://arxiv.org/abs/2603.04900)
- 👥 作者: Shuo Yang, Soyeon Caren Han, Xueqi Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大型语言模型（LLM）智能体的工具使用策略。虽然应用场景是通用任务，但其提出的‘自进化框架’、‘模块化策略分解’、‘基于轨迹的归因’和‘反馈引导的定向突变’等方法论，对于构建用于‘质谱结构推理’或化学问题求解的专用AI智能体具有直接的借鉴意义。例如，可以设想一个化学智能体，其工具使用模块专门用于调用质谱数据库、分子结构生成器或量子化学计算软件，EvoTool的优化框架可用于提升此类专业智能体在复杂推理链中的性能和可靠性。

**📖 中文摘要**

本文提出了EvoTool，一个通过无梯度进化范式优化模块化工具使用策略的自进化框架。EvoTool将智能体的工具使用策略分解为四个模块（规划器、选择器、调用器、合成器），并通过三种新颖机制在自改进循环中迭代优化它们：基于轨迹的归因定位使用诊断轨迹将失败定位到特定模块；反馈引导的定向突变则通过自然语言批评仅编辑该模块；多样性感知的群体选择保留互补的候选方案以确保解决方案的多样性。在四个基准测试上的实验表明，EvoTool在GPT-4.1和Qwen3-8B上均优于强基线5个点以上，同时实现了更高的效率和可迁移性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

</details>

---

### 17. [$\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](https://arxiv.org/abs/2603.04948)

**基本信息**

- 🔗 arXiv: [`2603.04948`](https://arxiv.org/abs/2603.04948)
- 👥 作者: Peihao Wang, Ruisi Cai, Zhen Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04948.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的、基于测试时梯度下降的大型语言模型（LLM）推理优化框架（$\nabla$-Reasoner）。该方法旨在提升LLM在复杂推理任务（如数学推理）中的性能。‘质谱结构推理’本质上也是一个需要复杂多步推理（从质谱峰推导出可能分子结构）的任务。因此，这篇论文提出的前沿推理优化技术，为开发更强大、更高效的‘质谱结构推理’专用大模型或增强现有模型的推理能力，提供了重要的方法论参考和技术路径。

**📖 中文摘要**

本文提出了$\nabla$-Reasoner，一种在潜在空间通过测试时梯度下降进行LLM推理的迭代生成框架。其核心组件是可微分文本优化（DTO），它利用来自LLM似然和奖励模型的梯度信号来优化文本表示。$\nabla$-Reasoner进一步结合了拒绝抽样和加速设计，以使解码过程更鲁棒和快速。理论上，作者证明了在样本空间中执行测试时梯度下降以最大化奖励，与通过KL正则化强化学习对齐LLM策略是对偶的。实证结果表明，$\nabla$-Reasoner在一个具有挑战性的数学推理基准上实现了超过20%的准确率提升，同时与强基线相比减少了大约10-40%的模型调用次数。这项工作引入了从零阶搜索到一阶优化的范式转变，为增强LLM推理提供了一条经济有效的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

</details>

---

### 18. [Programmable superconducting neuron with intrinsic in-memory computation and dual-timescale plasticity for ultra-efficient neuromorphic computing](https://arxiv.org/abs/2603.04966)

**基本信息**

- 🔗 arXiv: [`2603.04966`](https://arxiv.org/abs/2603.04966)
- 👥 作者: Muen Wang, Shucheng Yang, Yuxiang Lin 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04966.pdf)

**💡 相关性分析**

满足标准1：论文提出的可编程超导神经元架构，作为构建高效、专用计算硬件的基础单元，其设计理念（融合计算、内存、可塑性）与为“化学大模型”和“质谱结构推理”等复杂任务开发新型高效计算平台的核心主题间接相关。

**📖 中文摘要**

本文提出了一种可编程的超导神经元，用于超高效神经形态计算。该神经元集成了本征内存计算和双时间尺度可塑性，将计算、内存和可塑性融合到单个超导单元中。虽然论文的核心是硬件设计和神经形态计算，但其提出的可编程、具有内存和可塑性的基本计算单元，为构建新型计算架构提供了基础。这种底层硬件创新和架构设计理念，与构建能够处理复杂化学信息（如质谱数据）的专用“化学大模型”在思路上有潜在关联。例如，为质谱结构推理等任务设计高效、专用的计算硬件平台，可以从此类神经形态计算研究中获得灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The escalating energy demands of artificial intelligence pose a critical challenge to conventional computing. Leveraging the efficiency of event-driven, in-memory neuromorphic architectures into the superconducting circuits with ultra-high speed and low power dissipation advantages offers a promising solution to energy-efficient computing. However, the potential of such a solution has yet to be realized, owning to the absence of a fundamental superconducting unit that unifies programmability, local memory, and multi-timescale plasticity. Here, we introduce a programmable Josephson-junction-based leaky integrate-and-fire (LIF) neuron that features intrinsic static memory and precise programmability by encoding somatic and synaptic parameters directly in the bias current. This neuron is also capable of dual-timescale plasticity: picosecond-scale short-term modulation of spike transmission and long-term weight retention exceeding 10,000 seconds, facilitating both rapid temporal adaptation and robust weight storage. It can operate up to 45 GHz with femtojoule-level energy dissipation per spike, and supports 10 somatic threshold levels and 20 synaptic states. Furthermore, we demonstrate a crossbar-based spiking neural network (SNN) utilizing this neuron, which achieves outstanding performance across multiple tasks. By fusing computation, memory and plasticity into a single superconducting unit, our work paves the way for the next generation of ultrafast, energy-efficient neuromorphic computing.

</details>

---

### 19. [Functionality-Oriented LLM Merging on the Fisher--Rao Manifold](https://arxiv.org/abs/2603.04972)

**基本信息**

- 🔗 arXiv: [`2603.04972`](https://arxiv.org/abs/2603.04972)
- 👥 作者: Jiayu Wang, Zuojun Ye, Wenpeng Yin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04972.pdf)

**💡 相关性分析**

满足标准1：论文专注于大语言模型（LLM）的权重合并与功能融合方法。虽然未直接针对化学领域，但其解决“模型合并”这一核心问题的先进方法论，为未来构建、集成或优化面向化学信息学与质谱分析的专用“化学大模型”提供了重要的技术参考和理论基础。

**📖 中文摘要**

本文提出了一种在Fisher-Rao流形上进行LLM权重空间合并的新方法，旨在合并多个微调模型的功能，同时避免表示崩溃。该方法将模型合并表述为计算加权Karcher均值，以最小化预测分布之间的KL散度距离。论文的核心是解决大语言模型（LLM）参数高效合并的几何问题。虽然直接应用场景是通用LLM，但其解决“模型合并”这一核心问题的方法论（处理异构模型的功能融合与稳定性），对于未来构建和集成面向特定领域（如化学信息学）的专家模型或“化学大模型”具有重要的参考价值。如何将多个针对不同化学子任务（如质谱解析、分子性质预测）训练的专家模型有效合并为一个统一、稳健的大模型，是本工作可提供思路的相关研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective. We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

</details>

---

### 20. [VRM: Teaching Reward Models to Understand Authentic Human Preferences](https://arxiv.org/abs/2603.04974)

**基本信息**

- 🔗 arXiv: [`2603.04974`](https://arxiv.org/abs/2603.04974)
- 👥 作者: Biao Liu, Ning Xu, Junming Yang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04974.pdf)

**💡 相关性分析**

满足标准1：论文专注于改进大语言模型（LLM）对齐中的奖励建模（Reward Modeling）方法。虽然应用于通用场景，但其提出的变分奖励建模（VRM）框架所涉及的对齐技术、偏好学习机制，对于训练和优化面向化学信息学与质谱分析任务的“化学大模型”（例如，确保其推理结果符合化学规则或专家偏好）具有直接的方法论参考价值。

**📖 中文摘要**

本文提出了变分奖励建模（VRM）框架，旨在教导奖励模型理解真实的人类偏好，以更好地对齐大语言模型（LLM）。该框架通过变分推断技术，将人类评估过程建模为包含高维目标权重和低维语义特征的隐变量。论文的核心是改进LLM对齐中的奖励建模环节。虽然研究背景是通用LLM对齐，但其提出的更精细、更符合人类认知过程的奖励建模方法，对于训练面向科学领域（如化学）的领域大模型具有重要意义。例如，在构建用于质谱结构推理或分子设计的化学大模型时，如何设计有效的奖励函数或偏好学习机制来引导模型生成符合化学规则和专家偏好的输出，是本工作可以借鉴的相关技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have achieved remarkable success across diverse natural language tasks, yet the reward models employed for aligning LLMs often encounter challenges of reward hacking, where the approaches predominantly rely on directly mapping prompt-response pairs to scalar scores, which may inadvertently capture spurious correlations rather than authentic human preferences. In contrast, human evaluation employs a sophisticated process that initially weighs the relative importance of multiple high-dimensional objectives according to the prompt context, subsequently evaluating response quality through low-dimensional semantic features such as logical coherence and contextual appropriateness. Motivated by this consideration, we propose VRM, i.e., Variational Reward Modeling, a novel framework that explicitly models the evaluation process of human preference judgments by incorporating both high-dimensional objective weights and low-dimensional semantic features as latent variables, which are inferred through variational inference techniques. Additionally, we provide a theoretical analysis showing that VRM can achieve a tighter generalization error bound compared to the traditional reward model. Extensive experiments on benchmark datasets demonstrate that VRM significantly outperforms existing methods in capturing authentic human preferences.

</details>

---

### 21. [HiFlow: Hierarchical Feedback-Driven Optimization for Constrained Long-Form Text Generation](https://arxiv.org/abs/2603.04996)

**基本信息**

- 🔗 arXiv: [`2603.04996`](https://arxiv.org/abs/2603.04996)
- 👥 作者: Yifan Zhu, Guanting Chen, Bing Wei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04996.pdf)

**💡 相关性分析**

满足标准1：论文专注于解决大语言模型在“复杂约束下的长文本生成”这一核心问题。其提出的分层规划、约束感知优化和反馈机制，与“质谱结构推理”任务的内在需求高度契合（即根据质谱数据约束，推理出符合化学规则的结构）。该框架为解决化学信息学中的约束生成与推理问题提供了直接且先进的方法论参考。

**📖 中文摘要**

本文提出了HiFlow框架，用于解决受复杂约束的长文本生成问题。该框架将生成过程制定为一个包含规划层和生成层的两级优化过程，并通过约束感知的计划筛选和闭环反馈实现联合优化。论文的核心是提升LLM在复杂约束下的长文本生成能力。虽然应用场景是通用文本生成，但其解决“约束下生成”和“长序列规划”的核心技术，与化学信息学中一些挑战性问题高度相关。例如，在质谱结构推理中，模型需要根据质谱数据（约束）生成或推断出符合化学规则（复杂约束）的分子结构（可视为一种特殊“文本”或“序列”）。HiFlow中关于分层规划、约束建模和反馈优化的思想，可以为开发能够进行多步、受化学规则约束的分子结构推理模型提供技术灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models perform well in short text generation but still struggle with long text generation, particularly under complex constraints. Such tasks involve multiple tightly coupled objectives, including global structural consistency, local semantic coherence, and constraint feasibility, forming a challenging constrained optimization problem. Existing approaches mainly rely on static planning or offline supervision, limiting effective coordination between global and local objectives during generation. To address these challenges, we propose HiFlow, a hierarchical feedback-driven optimization framework for constrained long text generation. HiFlow formulates generation as a two-level optimization process, consisting of a planning layer for global structure and constraint modeling, and a generation layer for conditioned text generation. By incorporating constraint-aware plan screening and closed-loop feedback at both levels, HiFlow enables joint optimization of planning quality and generation behavior, progressively guiding the model toward high-quality, constraint-satisfying outputs. Experiments on multiple backbones confirm HiFlow's effectiveness over baseline methods.

</details>

---

### 22. [Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination](https://arxiv.org/abs/2603.05040)

**基本信息**

- 🔗 arXiv: [`2603.05040`](https://arxiv.org/abs/2603.05040)
- 👥 作者: Hyuntae Park, Yeachan Kim, SangKeun Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05040.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是探索多模态（文本+生成图像）信息融合以增强模型推理能力。这一方法论与“质谱结构推理”任务中融合质谱数据与分子结构信息（图像/图数据）以提升推理性能的研究方向高度相关，提供了跨模态增强推理的技术思路。

**📖 中文摘要**

本文提出了Imagine框架，一个基于机器想象的零样本常识推理框架。该框架通过将机器生成的图像作为视觉信号，来补充文本输入，以丰富预训练语言模型（PLM）的推理能力，从而缓解文本数据中的人类报告偏差。论文的核心是探索多模态（文本+图像）信息如何增强模型的常识推理。虽然其应用场景是通用常识推理，但其“利用机器生成图像作为辅助模态以弥补单一文本模态缺陷”的核心思想，对于化学信息学和质谱分析具有启发意义。例如，在质谱结构推理中，除了质谱数据（一种数值序列），分子结构图（2D/3D）是至关重要的信息。可以借鉴Imagine的思想，探索如何有效融合质谱数据与分子结构图（真实或生成）等多模态信息，来提升结构推理模型的性能和泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

</details>

---

### 23. [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)

**基本信息**

- 🔗 arXiv: [`2603.05044`](https://arxiv.org/abs/2603.05044)
- 👥 作者: Sicheng Fan, Qingyun Shi, Shengze Xu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05044.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个将大语言模型（LLM）知识压缩为可执行智能体行为的通用框架。这一“知识到行动”的转化范式，与构建能够利用化学知识进行推理、规划甚至操作的“化学大模型”或“化学AI智能体”的核心主题高度相关，提供了系统性的方法论参考。

**📖 中文摘要**

本文提出了WebFactory，一个用于训练GUI智能体的全自动闭环强化学习框架，旨在将大语言模型（LLM）中编码的互联网知识系统性地压缩为高效、可落地的智能体行为。论文的核心是研究如何将LLM的潜在知识转化为具体环境中的交互能力。虽然应用领域是网页交互，但其核心方法论——“系统性地压缩LLM的潜在知识为可行动的智能体”——与构建面向化学领域的AI智能体或专家系统在理念上相通。例如，可以设想一个“化学实验智能体”，它需要将化学文献知识（可能由LLM编码）转化为在虚拟或真实实验室环境中的操作步骤。WebFactory中关于环境合成、任务生成、轨迹收集和强化学习训练的自动化流水线，为开发此类领域专用智能体提供了可借鉴的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

</details>

---

### 24. [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046)

**基本信息**

- 🔗 arXiv: [`2603.05046`](https://arxiv.org/abs/2603.05046)
- 👥 作者: Rongzhi Li, Hitomi Yanaka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05046.pdf)

**💡 相关性分析**

满足标准1：论文专注于混合专家（MoE）模型架构中的专家分配策略优化，以实现模型容量的高效利用。这一核心主题与构建能够处理化学多个子领域（如质谱分析、分子设计）的模块化、高效“化学大模型”的架构设计挑战直接相关，提供了重要的技术思路。

**📖 中文摘要**

本文提出了NeuronMoE方法，用于高效地将大语言模型扩展到低资源语言。该方法通过分析跨语言神经元多样性，来指导混合专家（MoE）模型中每层的专家分配。论文的核心是解决MoE架构中专家分配的策略问题，以实现参数高效的多语言扩展。虽然应用场景是多语言NLP，但其解决的核心问题——如何根据任务特性（此处为语言特性）智能地分配模型容量（专家）——对于构建“化学大模型”具有重要参考价值。化学领域包含众多子方向（如有机合成、质谱解析、药物设计），一个统一的化学大模型可能需要像MoE一样动态调用不同“化学专家”子模块。NeuronMoE中基于神经元分析进行专家分配的方法，可以为设计面向化学不同子领域的模块化、高效大模型架构提供灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We propose $\textbf{NeuronMoE}$, a method that analyzes language-specific neurons across all transformer components to guide expert allocation per layer based on empirically measured cross-lingual neuron diversity. Applied to Llama-3.2-3B for low-resource languages (Greek, Turkish, and Hungarian), this approach achieves approximately 40% average parameter reduction while matching the performance of the LayerMoE baseline. We find that low-resource language experts independently develop neuron specialization patterns mirroring the high-resource language, which are concentrated in early and late layers. This reveals potential universal architectural principles in how multilingual models organize linguistic knowledge.

</details>

---

### 25. [Cyber Threat Intelligence for Artificial Intelligence Systems](https://arxiv.org/abs/2603.05068)

**基本信息**

- 🔗 arXiv: [`2603.05068`](https://arxiv.org/abs/2603.05068)
- 👥 作者: Natalia Krawczyk, Mateusz Szczepkowski, Adrian Brodzik 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05068.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是研究针对人工智能（AI）系统的威胁情报与安全框架。这直接关系到“化学大模型”和基于AI的“质谱结构推理”系统在实际部署中的安全性与可靠性，属于该主题下不可或缺的支撑性研究方向。

**📖 中文摘要**

本文探讨了如何发展网络威胁情报（CTI）以应对针对人工智能（AI）系统的安全威胁。论文分析了传统CTI的假设和工作流程与AI防御需求的差异，回顾并组织了当前AI安全知识体系，并概述了面向AI的威胁情报知识库应包含的内容，包括针对AI供应链不同阶段和产物的具体攻击指标（IoC）。论文的核心是提出一个面向AI系统的威胁情报框架。虽然主题是AI安全，但其系统性地梳理AI系统（包括模型、数据、管道）的资产、漏洞和威胁指标，对于保障“化学大模型”和“质谱结构推理”等AI系统的安全部署至关重要。例如，用于质谱分析的模型可能面临训练数据投毒、模型窃取或对抗性样本攻击。本工作提供的框架和思路，有助于化学信息学领域的研究者和实践者建立针对其AI系统的安全意识和防御基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) becomes deeply embedded in critical services and everyday products, it is increasingly exposed to security threats which traditional cyber defenses were not designed to handle. In this paper, we investigate how cyber threat intelligence (CTI) may evolve to address attacks that target AI systems. We first analyze the assumptions and workflows of conventional threat intelligence with the needs of AI-focused defense, highlighting AI-specific assets and vulnerabilities. We then review and organize the current landscape of AI security knowledge. Based on this, we outline what an AI-oriented threat intelligence knowledge base should contain, describing concrete indicators of compromise (IoC) for different AI supply-chain phases and artifacts, and showing how such a knowledge base could support security tools. Finally, we discuss techniques for measuring similarity between collected indicators and newly observed AI artifacts. The review reveals gaps and quality issues in existing resources and identifies potential future research directions toward a practical threat intelligence framework tailored to AI.

</details>

---

### 26. [TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling](https://arxiv.org/abs/2603.05094)

**基本信息**

- 🔗 arXiv: [`2603.05094`](https://arxiv.org/abs/2603.05094)
- 👥 作者: Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05094.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献之一是构建并发布了TW-Sound580K数据集，这是一个用于训练本地化音频-语言模型的高质量指令数据集。这为“化学大模型”和“质谱结构推理”领域提供了一个明确的示范，即构建领域特定、高质量的数据集是推动相关模型发展的关键资源，其数据构建和验证流程具有参考意义。

**📖 中文摘要**

本文发布了TW-Sound580K数据集，一个用于本地化音频-语言建模的台湾地区音频-文本指令数据集，并基于此训练了Tai-LALM模型。论文的核心是构建区域方言音频数据集并提升大型音频-语言模型（LALM）在当地方言上的性能。虽然领域是语音处理，但其工作完整展示了“构建领域/区域特定数据集 -> 训练/微调专用大模型”的全流程。这为化学信息学和质谱分析领域提供了一个清晰的范例：要构建高性能的“化学大模型”或“质谱推理模型”，高质量、大规模、任务特定的数据集（如标注好的质谱-结构对、化学反应数据等）是至关重要的基础资源。本工作在数据收集、验证、扩增和模型适配上的方法，对化学领域构建类似数据资源具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio-Language Models (LALMs) typically struggle with localized dialectal prosody due to the scarcity of specialized corpora. We present TW-Sound580K, a Taiwanese audio-text instruction dataset developed through a Verify-Generate-Critique (VGC) protocol. This pipeline leverages Dual-ASR validation to filter 522K raw clips, subsequently expanding them into 580,000 high-fidelity instruction pairs using a teacher model. The dataset's utility is demonstrated through Tai-LALM, which fine-tunes a DeSTA 2.5-Audio-initialized backbone and incorporates a dynamic Dual-ASR Arbitration strategy to optimize transcription selection during inference. On the TAU Benchmark, Tai-LALM reaches 49.1% accuracy, marking a 6.5% absolute improvement over the zero-shot baseline (42.6% with ASR text conditioning). This confirms that integrating regional corpora with rigorous curation and dynamic arbitration significantly enhances LALM performance on localized speech.

</details>

---

### 27. [ARC-TGI: Human-Validated Task Generators with Reasoning Chain Templates for ARC-AGI](https://arxiv.org/abs/2603.05099)

**基本信息**

- 🔗 arXiv: [`2603.05099`](https://arxiv.org/abs/2603.05099)
- 👥 作者: Jens Lehmann, Syeda Khushbakht, Nikoo Salehfard 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05099.pdf)

**💡 相关性分析**

满足标准2：论文提出了ARC-TGI框架，其核心是程序化生成具有明确规则和推理链的评估任务。这一方法论为“质谱结构推理”等领域构建系统化、可扩展、可解释的评估基准或训练数据生成工具提供了直接且强大的技术思路和工具参考，属于重要的数据/资源构建方法。

**📖 中文摘要**

本文介绍了ARC-TGI（ARC任务生成器清单），一个用于抽象与推理语料库（ARC-AGI）的开源任务生成框架。该框架围绕任务生成器构建，这些生成器是紧凑的Python程序，可以采样多样化的ARC-AGI任务，同时保留潜在的规则。每个生成的任务都配有自然语言输入和转换推理链。论文的核心是解决ARC-AGI基准测试中由于静态手工谜题集导致的过拟合和记忆问题，通过程序化生成大量可控的、具有明确推理链的任务。这项工作虽然针对通用抽象推理，但其“通过程序生成可控、可解释的评估任务”的方法论，对于化学信息学和质谱分析领域构建评估基准具有重要启示。例如，可以借鉴此思路，开发程序化生成质谱-分子结构对（包含不同复杂度、噪声、异构体）的框架，用于系统性地评估和比较不同“质谱结构推理”模型的泛化能力和鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Abstraction and Reasoning Corpus (ARC-AGI) probes few-shot abstraction and rule induction on small visual grids, but progress is difficult to measure on static collections of hand-authored puzzles due to overfitting, dataset leakage, and memorisation. We introduce ARC-TGI (ARC Task Generators Inventory), an open-source framework for task-family generators: compact Python programs that sample diverse ARC-AGI tasks while preserving a latent rule. ARC-TGI is built around a solver-facing representation: each generated task is paired with natural-language input and transformation reasoning chains and partially evaluated Python code implementing sampling, transformation, and episode construction. Crucially, ARC-TGI supports task-level constraints so that training examples collectively expose the variations needed to infer the underlying rule, a requirement for human-solvable ARC tasks that independent per-example sampling often fails to guarantee. All generators undergo human refinement and local verification to keep both grids and reasoning traces natural and consistent under variation. We release 461 generators covering 180 ARC-Mini tasks, 215 ARC-AGI-1 tasks (200 train, 15 test), and 66 ARC-AGI-2 tasks (55 train, 11 test), enabling scalable dataset sampling and controlled benchmarking.

</details>

---

### 28. [Diff-ES: Stage-wise Structural Diffusion Pruning via Evolutionary Search](https://arxiv.org/abs/2603.05105)

**基本信息**

- 🔗 arXiv: [`2603.05105`](https://arxiv.org/abs/2603.05105)
- 👥 作者: Zongfang Liu, Shengkun Tang, Zongliang Wu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05105.pdf)

**💡 相关性分析**

满足标准1：论文专注于扩散模型的高效结构化剪枝与加速。鉴于扩散模型在分子生成等化学任务中日益广泛的应用，以及“化学大模型”可能面临的巨大参数量问题，本工作提出的先进模型压缩与加速技术，与优化和部署此类大模型的核心主题直接相关。

**📖 中文摘要**

本文提出了Diff-ES，一个通过进化搜索进行阶段式结构化扩散模型剪枝的框架。该框架优化了扩散模型不同去噪阶段的稀疏度调度，并通过内存高效的权重路由执行，无需复制模型参数。论文的核心是提升扩散模型的结构化剪枝效率，在保证生成质量的同时实现实际加速。虽然应用对象是图像生成扩散模型，但其解决“大规模生成模型的高效压缩与加速”这一核心问题的方法，对于未来可能出现的、参数庞大的“化学大模型”（例如，用于分子生成或质谱预测的扩散模型）的部署和实用化至关重要。Diff-ES中基于进化搜索的自动稀疏调度和动态权重路由技术，为化学领域大模型的轻量化提供了前沿的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have achieved remarkable success in high-fidelity image generation but remain computationally demanding due to their multi-step denoising process and large model sizes. Although prior work improves efficiency either by reducing sampling steps or by compressing model parameters, existing structured pruning approaches still struggle to balance real acceleration and image quality preservation. In particular, prior methods such as MosaicDiff rely on heuristic, manually tuned stage-wise sparsity schedules and stitch multiple independently pruned models during inference, which increases memory overhead. However, the importance of diffusion steps is highly non-uniform and model-dependent. As a result, schedules derived from simple heuristics or empirical observations often fail to generalize and may lead to suboptimal performance. To this end, we introduce \textbf{Diff-ES}, a stage-wise structural \textbf{Diff}usion pruning framework via \textbf{E}volutionary \textbf{S}earch, which optimizes the stage-wise sparsity schedule and executes it through memory-efficient weight routing without model duplication. Diff-ES divides the diffusion trajectory into multiple stages, automatically discovers an optimal stage-wise sparsity schedule via evolutionary search, and activates stage-conditioned weights dynamically without duplicating model parameters. Our framework naturally integrates with existing structured pruning methods for diffusion models including depth and width pruning. Extensive experiments on DiT and SDXL demonstrate that Diff-ES consistently achieves wall-clock speedups while incurring minimal degradation in generation quality, establishing state-of-the-art performance for structured diffusion model pruning.

</details>

---

### 29. [SeedPolicy: Horizon Scaling via Self-Evolving Diffusion Policy for Robot Manipulation](https://arxiv.org/abs/2603.05117)

**基本信息**

- 🔗 arXiv: [`2603.05117`](https://arxiv.org/abs/2603.05117)
- 👥 作者: Youqiang Gui, Yuxuan Zhou, Shen Cheng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05117.pdf)

**💡 相关性分析**

满足标准1：论文专注于解决模仿学习中的长时域序列建模与决策问题，提出了创新的自演化注意力机制。这一核心主题与化学信息学中涉及长序列推理的任务（如多步合成规划、动态质谱数据分析）具有方法论上的相关性，为解决化学领域的复杂序列推理问题提供了技术参考。

**📖 中文摘要**

本文提出了SeedPolicy（自演化扩散策略），通过自演化门控注意力（SEGA）模块解决扩散策略（DP）在长时域机器人操作中因观察视野增加而性能下降的问题。SEGA模块通过门控注意力维护一个随时间演化的潜在状态，高效压缩长时域观测。论文的核心是提升模仿学习策略在长时域任务中的性能与可扩展性。虽然应用场景是机器人操作，但其解决“长序列建模与决策”的核心技术，与化学信息学中一些长序列推理问题有相似之处。例如，多步有机合成路线规划、从时间序列质谱数据中推断反应过程等，都可以被视为长时域序列决策或推理问题。SeedPolicy中处理长时域依赖和状态压缩的方法，可以为设计能够进行复杂、多步化学推理的模型提供算法层面的灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Imitation Learning (IL) enables robots to acquire manipulation skills from expert demonstrations. Diffusion Policy (DP) models multi-modal expert behaviors but suffers performance degradation as observation horizons increase, limiting long-horizon manipulation. We propose Self-Evolving Gated Attention (SEGA), a temporal module that maintains a time-evolving latent state via gated attention, enabling efficient recurrent updates that compress long-horizon observations into a fixed-size representation while filtering irrelevant temporal information. Integrating SEGA into DP yields Self-Evolving Diffusion Policy (SeedPolicy), which resolves the temporal modeling bottleneck and enables scalable horizon extension with moderate overhead. On the RoboTwin 2.0 benchmark with 50 manipulation tasks, SeedPolicy outperforms DP and other IL baselines. Averaged across both CNN and Transformer backbones, SeedPolicy achieves 36.8% relative improvement in clean settings and 169% relative improvement in randomized challenging settings over the DP. Compared to vision-language-action models such as RDT with 1.2B parameters, SeedPolicy achieves competitive performance with one to two orders of magnitude fewer parameters, demonstrating strong efficiency and scalability. These results establish SeedPolicy as a state-of-the-art imitation learning method for long-horizon robotic manipulation. Code is available at: this https URL .

</details>

---

### 30. [Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning](https://arxiv.org/abs/2603.05120)

**基本信息**

- 🔗 arXiv: [`2603.05120`](https://arxiv.org/abs/2603.05120)
- 👥 作者: Boren Hu, Xiao Liu, Boci Peng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05120.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是研究如何通过双向课程生成和多智能体协作来实现数据高效的学习，特别是在数学推理任务上。这一方法论对于数据标注成本高、获取困难的“质谱结构推理”和“化学大模型”训练具有直接且重要的参考价值，为解决该领域的数据瓶颈问题提供了先进思路。

**📖 中文摘要**

本文提出了双向课程生成框架，一个多智能体框架，用于数据高效的数学推理。该框架通过模拟自适应教学法，动态生成数据，既可以增加问题难度来挑战模型，也可以在模型出现特定推理失败时简化问题来进行修复，从而最大化每个训练样本的教学价值。论文的核心是提升大语言模型在数学推理任务上的数据效率。虽然领域是数学，但其解决“数据高效学习”和“自适应课程生成”的核心方法论，对于数据获取成本高昂或标注困难的化学信息学领域具有极高的应用价值。例如，在质谱结构推理中，高质量标注数据（质谱-精确结构对）稀缺。本框架提出的双向课程生成和基于反馈的数据构建机制，为在有限数据下高效训练鲁棒的“质谱结构推理模型”或“化学大模型”提供了创新的训练范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enhancing mathematical reasoning in Large Language Models typically demands massive datasets, yet data efficiency remains a critical bottleneck. While Curriculum Learning attempts to structure this process, standard unidirectional approaches (simple-to-complex) suffer from inefficient sample utilization: they blindly escalate complexity even when foundational gaps persist, leading to wasted computation on unsolvable problems. To maximize the instructional value of every training sample, we introduce a novel Bidirectional Curriculum Generation framework. Unlike rigid trajectories, our multi-agent ecosystem mimics adaptive pedagogy to establish a closed feedback loop. It dynamically generates data by either complicating problems to challenge the model or, crucially, simplying them to repair specific reasoning failures. This mechanism ensures that the model consumes only the most effective data at any given stage. Grounded in the Optimal Pacing Theorem, our approach optimizes the learning trajectory, significantly outperforming baselines while achieving superior reasoning performance with substantially fewer instruction samples.

</details>

---

### 31. [Measuring the Redundancy of Decoder Layers in SpeechLLMs](https://arxiv.org/abs/2603.05121)

**基本信息**

- 🔗 arXiv: [`2603.05121`](https://arxiv.org/abs/2603.05121)
- 👥 作者: Adel Moumen, Guangzhi Sun, Philip C Woodland
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05121.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是对大语言模型（此处为SpeechLLM）的架构进行冗余性分析和高效化探索。这一研究主题与方法论，对于未来设计和优化“化学大模型”的架构（如何平衡性能与效率、哪些组件可能冗余）具有直接且重要的指导意义，属于模型架构层面的核心相关研究。

**📖 中文摘要**

本文研究了语音大语言模型（SpeechLLM）中解码器层的冗余性。研究发现，解码器的冗余性很大程度上是从预训练LLM继承而来的，并且文本和语音输入会产生相似的冗余块。通过剪枝解码器层和分析剪枝后的修复，论文测量了模型的过剩容量，并展示了跨语音编码器、任务和语言的冗余结构存在一致性。论文的核心是对SpeechLLM模型架构进行可解释性分析和高效化探索。虽然对象是语音LLM，但其“分析大模型组件冗余性并探索高效架构”的研究范式，完全适用于“化学大模型”。在构建化学领域大模型时，如何设计既高效又高性能的架构是一个关键问题。本工作提供的冗余性分析方法和剪枝策略，为未来化学大模型的架构设计、压缩和加速提供了重要的实证研究方法和参考依据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech Large Language Models route speech encoder representations into an LLM decoder that typically accounts for over 90% of total parameters. We study how much of this decoder capacity is actually needed for speech tasks. Across two LLM families and three scales (1-8B), we show that decoder redundancy is largely inherited from the pretrained LLM: text and speech inputs yield similar redundant blocks. We then measure excess capacity by pruning decoder layers and analysing post-pruning healing to increase robustness. Our findings show that 7-8B models retain good ASR performance with only 60% of decoder layers, and the same trend extends to smaller scales with reduced pruning tolerance. We then generalise to speech translation, and show that the same blocks of layers are redundant across speech encoders, tasks and languages, indicating that a more global redundancy structure exists, enabling a single pruned and multi-tasks SpeechLLM backbone to be deployed.

</details>

---

### 32. [Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs](https://arxiv.org/abs/2603.05343)

**基本信息**

- 🔗 arXiv: [`2603.05343`](https://arxiv.org/abs/2603.05343)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕用于分子模拟的等变图神经网络（一种化学大模型）的压缩和加速，直接关联“化学大模型”主题。

**📖 中文摘要**

本文提出了一种几何感知量化（GAQ）框架，用于压缩和加速等变图神经网络（GNNs），同时严格保持离散空间中的连续对称性。该研究针对分子模拟中的SO(3)-等变GNNs，解决了高计算成本和内存瓶颈问题。通过引入幅度-方向解耦量化（MDDQ）方案、对称感知训练策略和鲁棒的注意力归一化机制，该框架在保持几何保真度的同时，显著降低了模型的内存占用并提升了推理速度。实验在rMD17基准测试上进行，证明了该方法在分子动力学模拟中的有效性。这项工作直接与“化学大模型”主题相关，因为它专注于用于分子模拟的等变GNNs的优化和加速，这是化学信息学中构建和部署大型、高效模型的核心问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

</details>

---

### 33. [On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395)

**基本信息**

- 🔗 arXiv: [`2603.05395`](https://arxiv.org/abs/2603.05395)
- 👥 作者: Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05395.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是层神经网络（SNNs），这是图神经网络（GNNs）的一种，而GNNs是构建“化学大模型”（用于分子表示和性质预测）的核心架构之一。论文探讨了其设计原理和有效性，属于该主题的研究范畴。

**📖 中文摘要**

本文研究了层神经网络（SNNs）作为图卷积网络在异配图上的扩展，旨在通过引入层和可学习的限制映射来解决过度平滑问题。作者引入了一个恒等层网络基线（所有限制映射固定为恒等映射），并在多个异配图基准上进行了消融实验，以探究学习限制映射的必要性。研究发现，恒等基线在性能上与多种SNN变体相当。此外，作者引入了瑞利商作为衡量过度平滑的归一化指标，并表明在训练网络中，基于扩散分析的SNN预测行为并未在经验上体现。这项工作深入探讨了图神经网络架构设计，与构建和改进用于化学或分子表示的图模型（化学大模型的一种形式）的研究方向密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

</details>

---

### 34. [An interpretable prototype parts-based neural network for medical tabular data](https://arxiv.org/abs/2603.05423)

**基本信息**

- 🔗 arXiv: [`2603.05423`](https://arxiv.org/abs/2603.05423)
- 👥 作者: Jacek Karolczak, Jerzy Stefanowski
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05423.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于医疗表格数据的可解释深度学习模型。虽然焦点是医疗记录，但其核心方法（原型学习、可解释AI）和领域（生物医学信息学）与“化学信息学”领域有很强的交叉和相关性，化学信息学同样关注于开发用于化学和生物数据的可解释机器学习模型。

**📖 中文摘要**

本文提出了一种新的用于医疗表格数据的可解释原型部件神经网络。该模型受计算机视觉中原型部件深度神经网络的启发，专门为需要将诊断结果规范离散化的医疗记录设计。与依赖空间结构的原始视觉模型不同，该方法通过对描述患者的特征进行可训练的“分块”处理，从结构化数据中学习有意义的原型部件。这些部件表示为二进制或离散化的特征子集，使得模型能够以人类可读的术语表达原型，从而与临床语言和基于案例的推理保持一致。该神经网络本质上是可解释的，并通过在网络的潜在空间中将患者描述与学习到的原型进行比较来提供基于概念的可解释预测。实验表明，该模型在医学基准数据集上的分类性能与广泛使用的基线模型具有竞争力，同时提供了透明度。这项工作展示了在临床决策支持中结合预测性能和可解释性的模型，属于机器学习在化学和生物医学信息学中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainable patching over features describing a patient, to learn meaningful prototypical parts from structured data. These parts are represented as binary or discretized feature subsets. This allows the model to express prototypes in human-readable terms, enabling alignment with clinical language and case-based reasoning. Our proposed neural network is inherently interpretable and offers interpretable concept-based predictions by comparing the patient's description to learned prototypes in the latent space of the network. In experiments, we demonstrate that the model achieves classification performance competitive to widely used baseline models on medical benchmark datasets, while also offering transparency, bridging the gap between predictive performance and interpretability in clinical decision support.

</details>

---

### 35. [AbAffinity: A Large Language Model for Predicting Antibody Binding Affinity against SARS-CoV-2](https://arxiv.org/abs/2603.04480)

**基本信息**

- 🔗 arXiv: [`2603.04480`](https://arxiv.org/abs/2603.04480)
- 👥 作者: Faisal Bin Ashraf, Animesh Ray, Stefano Lonardi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04480.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于预测抗体-抗原结合亲和力的大型语言模型（AbAffinity）。这直接属于“化学大模型”主题，即构建用于化学和生物分子性质预测的大型AI模型。

**📖 中文摘要**

本研究介绍了AbAffinity，一种新的大型语言模型，用于准确预测抗体与目标肽段（例如SARS-CoV-2刺突蛋白）的结合亲和力。随着人工智能领域的显著进步和实验抗体数据（特别是与COVID-19相关的数据）的指数级增长，基于机器学习的抗体设计正在成为对抗传染病最有前途的方法之一。抗体与抗原的结合能力（称为结合亲和力）是设计中和抗体最关键的属性之一。该工作利用大型语言模型处理蛋白质序列的能力，构建了一个专门针对抗体-抗原结合亲和力预测的模型。这直接位于“化学信息学”和“生物信息学”的交叉点，并且是构建用于生物分子相互作用的专用“化学大模型”的实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning-based antibody design is emerging as one of the most promising approaches to combat infectious diseases, due to significant advancements in the field of artificial intelligence and an exponential surge in experimental antibody data (in particular related to COVID-19). The ability of an antibody to bind to an antigens (called binding affinity) is one of the the most critical properties in designing neutralizing antibodies. In this study we introduce Ab-Affinity, a new large language model that can accurately predict the binding affinity of antibodies against a target peptide, e.g., the SARS-CoV-2 spike protein. Code and model are available at this https URL .

</details>

---

### 36. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2603.04523)

**基本信息**

- 🔗 arXiv: [`2603.04523`](https://arxiv.org/abs/2603.04523)
- 👥 作者: Austin Rodriguez, Justin S. Smith, Sakib Matin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04523.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习原子间势（MLIPs）的训练框架优化。MLIPs是计算化学和材料科学中至关重要的“化学大模型”，用于从第一性原理模拟中学习并预测原子系统的势能和力。

**📖 中文摘要**

本文介绍了投影Hessian学习（PHL），一个用于机器学习原子间势（MLIPs）的可扩展二阶训练框架。Hessian矩阵（二阶导数）编码了势能面比能量和力更丰富的局部曲率信息，但使用完整Hessian矩阵训练MLIPs通常不切实际，因为其计算和存储成本随系统大小呈二次方增长。PHL通过仅使用Hessian-向量积（HVPs）来注入曲率信息，从而避免了构建完整Hessian矩阵。该方法将曲率沿随机探测方向投影，并使用基于随机迹的无偏损失函数，实现了有利的系统大小缩放，使得在无需二次内存增长的情况下进行曲率感知训练成为可能。研究在ωB97XD/6-31G(d)水平计算的化学反应物、产物、过渡态、内禀反应坐标和简正模采样几何的化学多样化数据集上对PHL进行了基准测试。结果表明，PHL在能量、力和Hessian精度上匹配了完整Hessian训练，同时在小分子系统上实现了超过24倍的epoch加速。这项工作直接针对“化学大模型”中的一个关键子领域——机器学习原子间势的开发与优化，旨在提高其准确性和训练效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hessian matrix (second derivatives) encodes far richer local curvature of the potential energy surface than energies and forces alone. However, training machine-learning interatomic potentials (MLIPs) with full Hessians is often impractical because explicitly forming and storing Hessian matrices scales quadratically in cost and memory. We introduce Projected Hessian Learning (PHL), a scalable second-order training framework that injects curvature information using only Hessian-vector products (HVPs). Rather than constructing the Hessian, PHL projects curvature along stochastic probe directions and uses an unbiased stochastic trace-based loss with favorable system-size scaling, enabling curvature-informed training without quadratic memory growth. We benchmark PHL on a chemically diverse dataset of reactants, products, transition states, intrinsic reaction coordinates, and normal-mode sampled geometries computed at omegaB97XD/6-31G(d). We compare energy-force training (E-F), two HVP-based schemes (E-F-HVP with one-hot or randomized probes), and full energy-force-Hessian training (E-F-H). With randomized probes per minibatch, both HVP schemes match full-Hessian training in energy, force, and Hessian accuracy while delivering >24x epoch speedups for the small molecular systems studied. In a fixed-probe regime with one HVP per molecule, randomized projections consistently outperform one-column probing, especially for far-from-equilibrium geometries. Overall, PHL replaces explicit Hessian supervision with force-complexity curvature training, retaining most second-order accuracy gains while scaling to larger, more complex molecular systems.

</details>

---

### 37. [Particle-Guided Diffusion for Gas-Phase Reaction Kinetics](https://arxiv.org/abs/2603.05139)

**基本信息**

- 🔗 arXiv: [`2603.05139`](https://arxiv.org/abs/2603.05139)
- 👥 作者: Andrew Millard, Henrik Pedersen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用扩散模型（一种生成式大模型）来解决气相化学反应动力学问题，直接围绕'化学大模型'这一主题。

**📖 中文摘要**

该论文提出了一种基于扩散模型的粒子引导采样方法，用于解决气相化学反应动力学中的偏微分方程（PDE）控制问题。该方法在变化的参数条件下，对平流-反应-扩散（ARD）方程的解进行训练，以生成物理上一致的浓度场并准确预测出口浓度。这项工作展示了扩散模型在反应输运系统中进行推理的潜力，属于利用生成模型（扩散模型）解决化学动力学问题的研究范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

</details>

---

### 38. [Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks](https://arxiv.org/abs/2603.05188)

**基本信息**

- 🔗 arXiv: [`2603.05188`](https://arxiv.org/abs/2603.05188)
- 👥 作者: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05188.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发并应用大型语言模型（LLM）智能体来指导共价有机框架（COF）的逆向设计，直接围绕'化学大模型'这一主题。

**📖 中文摘要**

该论文针对共价有机框架（COF）光催化剂设计中稳定性与活性的权衡问题，引入了一个名为Ara的大型语言模型（LLM）智能体。该智能体利用预训练的化学知识、给体-受体理论、共轭效应和连接键稳定性层次结构，来指导搜索同时满足带隙、带边和水解稳定性标准的COF。研究评估了该智能体在由不同节点、连接体、连接键和R基团组成的候选空间中的性能，并与随机搜索和贝叶斯优化进行了比较。结果表明，LLM的化学先验知识可以显著加速多标准材料发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

</details>

---

### 39. [GIT-BO: High-Dimensional Bayesian Optimization with Tabular Foundation Models](https://arxiv.org/abs/2505.20685)

**基本信息**

- 🔗 arXiv: [`2505.20685`](https://arxiv.org/abs/2505.20685)
- 👥 作者: Rosen Ting-Ying Yu, Cyril Picard, Faez Ahmed
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.20685.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合表格基础模型（TabPFN v2）的贝叶斯优化框架，用于解决高维优化问题，这属于'化学大模型'在化学信息学和材料发现中应用的范畴。

**📖 中文摘要**

该论文提出了GIT-BO，一个梯度信息贝叶斯优化框架，用于解决高维优化问题。它结合了TabPFN v2（一种在上下文中执行零样本贝叶斯推理的表格基础模型）和基于模型自身预测均值梯度计算的活动子空间机制。该框架通过费舍尔信息估计将探索与内在低维子空间对齐，并使用UCB采集函数选择查询，无需在线重新训练。论文在多达500维的合成和真实世界任务（如电力系统、Rover、MOPTA08、Mazda）上进行了评估。这项工作展示了基础模型（TabPFN v2）在化学信息学相关的高维优化问题（如材料设计、分子优化）中的应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian optimization (BO) struggles in high dimensions, where Gaussian-process surrogates demand heavy retraining and brittle assumptions, slowing progress on real engineering and design problems. We introduce GIT-BO, a Gradient-Informed BO framework that couples TabPFN v2, a tabular foundation model that performs zero-shot Bayesian inference in context, with an active-subspace mechanism computed from the model's own predictive-mean gradients. This aligns exploration to an intrinsic low-dimensional subspace via a Fisher-information estimate and selects queries with a UCB acquisition, requiring no online retraining. Across 60 problem variants spanning 20 benchmarks-nine scalable synthetic families and ten real-world tasks (e.g., power systems, Rover, MOPTA08, Mazda)-up to 500 dimensions, GIT-BO delivers a stronger performance-time trade-off than state-of-the-art GP-based methods (SAASBO, TuRBO, Vanilla BO, BAxUS), ranking highest in performance and with runtime advantages that grow with dimensionality. Limitations include memory footprint and dependence on the capacity of the underlying TFM.

</details>

---

### 40. [HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals](https://arxiv.org/abs/2506.08618)

**基本信息**

- 🔗 arXiv: [`2506.08618`](https://arxiv.org/abs/2506.08618)
- 👥 作者: Xianquan Yan, Hakan Akgün, Kenji Kawaguchi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08618.pdf)

**💡 相关性分析**

满足标准2：论文提出了HSG-12M大规模图数据集和Poly2Graph生成工具，这为化学信息学中开发图神经网络等化学大模型提供了新颖且高质量的数据资源。

**📖 中文摘要**

本文介绍了HSG-12M，一个包含1160万个静态和510万个动态哈密顿谱图的大规模数据集。该数据集源自非厄米量子晶体的能谱，是首个大规模空间多重图数据集。论文的核心贡献是提出了一个从哈密顿量到谱图的自动化映射管道Poly2Graph，并创建了HSG-12M这一资源。该数据集旨在为数据驱动的科学发现（如凝聚态物理）和几何感知的图学习提供基础。虽然论文主要关注物理系统，但其核心是创建和提供了一个大规模、高质量的图结构数据集。这对于化学信息学领域，特别是用于开发或评估化学大模型（例如用于分子图生成或性质预测的图神经网络）具有直接价值，因为它提供了一个具有复杂几何和拓扑结构的新型图数据资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming scientific research by revealing new ways to understand complex physical systems, but its impact remains constrained by the lack of large, high-quality domain-specific datasets. A rich, largely untapped resource lies in non-Hermitian quantum physics, where the energy spectra of crystals form intricate geometries on the complex plane -- termed as Hamiltonian spectral graphs. Despite their significance as fingerprints for electronic behavior, their systematic study has been intractable due to the reliance on manual extraction. To unlock this potential, we introduce Poly2Graph: a high-performance, open-source pipeline that automates the mapping of 1-D crystal Hamiltonians to spectral graphs. Using this tool, we present HSG-12M: a dataset containing 11.6 million static and 5.1 million dynamic Hamiltonian spectral graphs across 1401 characteristic-polynomial classes, distilled from 177 TB of spectral potential data. Crucially, HSG-12M is the first large-scale dataset of spatial multigraphs -- graphs embedded in a metric space where multiple geometrically distinct trajectories between two nodes are retained as separate edges. This simultaneously addresses a critical gap, as existing graph benchmarks overwhelmingly assume simple, non-spatial edges, discarding vital geometric information. Benchmarks with popular GNNs expose new challenges in learning spatial multi-edges at scale. Beyond its practical utility, we show that spectral graphs serve as universal topological fingerprints of polynomials, vectors, and matrices, forging a new algebra-to-graph link. HSG-12M lays the groundwork for data-driven scientific discovery in condensed matter physics, new opportunities in geometry-aware graph learning and beyond.

</details>

---

### 41. [Bures-Wasserstein Flow Matching for Graph Generation](https://arxiv.org/abs/2506.14020)

**基本信息**

- 🔗 arXiv: [`2506.14020`](https://arxiv.org/abs/2506.14020)
- 👥 作者: Keyue Jiang, Jiahao Cui, Xiaowen Dong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进图生成模型，并专门在分子生成任务上进行了实验验证。这直接围绕“化学大模型”主题中分子生成与设计的子方向。

**📖 中文摘要**

本文提出了BWFlow，一种用于图生成的流匹配框架。该框架通过将图建模为马尔可夫随机场（MRF）参数化的连接系统，并利用MRF对象之间的最优传输位移来设计平滑的概率路径，从而确保图组件（节点和边）的协同演化。该方法旨在解决现有扩散或流模型因对节点和边进行独立建模和线性插值而导致的概率路径不规则、训练动态差和采样收敛问题。实验在普通图生成和分子生成任务上验证了BWFlow的有效性，展示了其具有竞争力的性能、更好的训练收敛性和高效的采样。论文的核心是改进图生成模型，而分子生成是化学信息学和药物发现中的核心任务。因此，该论文提出的图生成框架直接适用于分子结构（一种特殊的图）的生成，这与“化学大模型”中专注于分子设计与生成的研究主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation has emerged as a critical task in fields ranging from drug discovery to circuit design. Contemporary approaches, notably diffusion and flow-based models, have achieved solid graph generative performance through constructing a probability path that interpolates between reference and data distributions. However, these methods typically model the evolution of individual nodes and edges independently and use linear interpolations in the disjoint space of nodes/edges to build the path. This disentangled interpolation breaks the interconnected patterns of graphs, making the constructed probability path irregular and non-smooth, which causes poor training dynamics and faulty sampling convergence. To address the limitation, this paper first presents a theoretically grounded framework for probability path construction in graph generative models. Specifically, we model the joint evolution of the nodes and edges by representing graphs as connected systems parameterized by Markov random fields (MRF). We then leverage the optimal transport displacement between MRF objects to design a smooth probability path that ensures the co-evolution of graph components. Based on this, we introduce BWFlow, a flow-matching framework for graph generation that utilizes the derived optimal probability path to benefit the training and sampling algorithm design. Experimental evaluations in plain graph generation and molecule generation validate the effectiveness of BWFlow with competitive performance, better training convergence, and efficient sampling.

</details>

---

### 42. [From Bandit Regret to FDR Control: Online Selective Generation with Adversarial Feedback Unlocking](https://arxiv.org/abs/2506.14067)

**基本信息**

- 🔗 arXiv: [`2506.14067`](https://arxiv.org/abs/2506.14067)
- 👥 作者: Minjae Lee, Yoonjae Jung, Sangdon Park
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14067.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图生成模型的创新，并专门在分子生成任务上进行了实验和验证，这直接服务于“化学大模型”中分子生成与设计的核心主题。

**📖 中文摘要**

本文提出了Bures-Wasserstein Flow Matching for Graph Generation (BWFlow)，一个用于图生成的流匹配框架。该工作首先提出了一个图生成模型中概率路径构建的理论框架，将图建模为马尔可夫随机场（MRF）参数化的连接系统，并利用MRF对象间的最优传输位移来设计确保图组件协同演化的平滑概率路径。基于此，引入了BWFlow框架，利用推导出的最优概率路径来有益于训练和采样算法设计。实验评估在普通图生成和分子生成任务上进行，验证了BWFlow在具有竞争力的性能、更好的训练收敛性和高效采样方面的有效性。该研究专注于图生成模型的改进，并明确将分子生成作为关键应用和评估领域，这与化学信息学中利用生成模型进行分子设计的“化学大模型”主题直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As interactive generative systems are increasingly deployed in real-world applications, their tendency to generate unreliable or false responses raises serious concerns. Selective generation mitigates this risk by ensuring that the system answers only when confident. However, real-world deployments typically provide only partial user feedback on the selected response (e.g., thumbs up/down) and often operate in non-stationary or adversarial environments,for which effective learning methods are largely missing. To bridge this gap, we propose ExSUL, a novel online learning framework for selective generation with adversarial bandit feedback. Technically, we introduce (i) a novel conversion lemma that translates the regret of any bandit algorithm into an FDR bound, and (ii) feedback unlocking, a strategy that exploits the structure of selective generation to extract additional learning signals from partial feedback. We prove that ExSUL achieves a regret bound of $O(\sqrt{T \ln |H|})$, matching the efficiency and FDR controllability of full-information settings despite receiving only partial feedback. While applicable to general generative tasks, we demonstrate the efficacy of ExSUL for ensuring the reliability of Large Language Models (LLMs) through empirical validation on question-answering tasks across diverse non-stationary and adversarial settings. Our results demonstrate that ExSUL robustly controls the FDR while maintaining competitive answering coverage.

</details>

---

### 43. [Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks](https://arxiv.org/abs/2509.19696)

**基本信息**

- 🔗 arXiv: [`2509.19696`](https://arxiv.org/abs/2509.19696)
- 👥 作者: Noah Geiger, Tamim Asfour, Neville Hogan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.19696.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个基于扩散模型（一种生成式大模型）的框架，用于从观测数据中推理和生成物理交互轨迹。这种方法论与“质谱结构推理”中利用生成模型从质谱数据推理分子结构的核心思路相关。

**📖 中文摘要**

本文提出了Diffusion-Based Impedance Learning，一个结合生成建模与能量一致阻抗控制的框架，用于接触丰富的机器人操作任务。该框架使用一个基于Transformer的扩散模型，通过交叉注意力在测量的外部力矩上进行条件化，以重建模拟的零力轨迹（sZFTs），这些轨迹代表了接触一致的平衡行为。重建的sZFT随后被一个基于能量的估计器用于通过方向性刚度和阻尼调制在线调整阻抗。该方法在通过Apple Vision Pro遥操作收集的跑酷和机器人辅助治疗演示上进行训练。虽然论文主要关注机器人学，但其核心方法依赖于扩散模型（一种生成式大模型）来理解和生成复杂的物理交互轨迹。这种基于扩散模型的轨迹生成与推理框架，在方法论上与“质谱结构推理”中可能使用的、从复杂数据（质谱峰）生成或推理分子结构的生成式模型有潜在的类比和启发性。论文展示了生成模型在从高维、噪声观测中推理出潜在物理状态（sZFT）的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning-based methods excel at robot motion generation but remain limited in contact-rich physical interaction. Impedance control provides stable and safe contact behavior but requires task-specific tuning of stiffness and damping parameters. We present Diffusion-Based Impedance Learning, a framework that bridges these paradigms by combining generative modeling with energy-consistent impedance control. A Transformer-based Diffusion Model, conditioned via cross-attention on measured external wrenches, reconstructs simulated Zero-Force Trajectories (sZFTs) that represent contact-consistent equilibrium behavior. A SLERP-based quaternion noise scheduler preserves geometric consistency for rotations on the unit sphere. The reconstructed sZFT is used by an energy-based estimator to adapt impedance online through directional stiffness and damping modulation. Trained on parkour and robot-assisted therapy demonstrations collected via Apple Vision Pro teleoperation, the model achieves sub-millimeter positional and sub-degree rotational accuracy using only tens of thousands of samples. Deployed in realtime torque control on a KUKA LBR iiwa, the approach enables smooth obstacle traversal and generalizes to unseen tasks, achieving 100% success in multi-geometry peg-in-hole insertion.

</details>

---

### 44. [Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling](https://arxiv.org/abs/2510.26139)

**基本信息**

- 🔗 arXiv: [`2510.26139`](https://arxiv.org/abs/2510.26139)
- 👥 作者: Minseo Kwon, Young J. Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.26139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及将视觉语言模型（VLM）作为关键组件集成到任务与运动规划中，以提供推理和引导。这体现了大模型在复杂系统推理中的应用，与“化学大模型”主题中利用大模型进行化学问题求解的核心思路相关。

**📖 中文摘要**

本文提出了一个运动学任务与运动规划（TAMP）框架，该框架基于一个统一表示符号和数值状态的混合状态树进行规划，使任务和运动决策能够共同决定。运动学约束由现成的运动规划器和物理模拟器验证，而一个视觉语言模型（VLM）则通过状态的可视化渲染来引导探索TAMP解决方案并基于此进行搜索回溯。论文在模拟和真实世界领域进行了实验。虽然主要应用于机器人规划，但该工作的一个关键组成部分是使用VLM（一种多模态大模型）来提供常识先验并指导搜索过程。这体现了大模型（此处是VLM）在复杂规划与推理任务中的应用。尽管应用领域不同，但这种将大模型作为推理和引导组件集成到科学或工程问题求解流程中的范式，与“化学大模型”主题中利用大模型辅助化学研究（如逆合成规划、反应条件优化）的思路在概念上是相通的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Task and Motion Planning (TAMP) integrates high-level task planning with low-level motion feasibility, but existing methods are costly in long-horizon problems due to excessive motion sampling. While LLMs provide commonsense priors, they lack 3D spatial reasoning and cannot ensure geometric or dynamic feasibility. We propose a kinodynamic TAMP planner based on a hybrid state tree that uniformly represents symbolic and numeric states during planning, enabling task and motion decisions to be jointly decided. Kinodynamic constraints embedded in the TAMP problem are verified by an off-the-shelf motion planner and physics simulator, and a VLM guides exploring a TAMP solution and backtracks the search based on visual rendering of the states. Experiments on the simulated domains and in the real world show 32.14% - 1166.67% increased average success rates compared to traditional and LLM-based TAMP planners and reduced planning time on complex problems, with ablations further highlighting the benefits of VLM backtracking. More details are available at this https URL .

</details>

---

### 45. [SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation](https://arxiv.org/abs/2510.27048)

**基本信息**

- 🔗 arXiv: [`2510.27048`](https://arxiv.org/abs/2510.27048)
- 👥 作者: Eric T. Chang, Peter Ballentine, Zhanpeng He 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27048.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种结合强化学习和多模态触觉传感的学习框架，用于解决复杂的物理交互和推理问题。这种方法论与“质谱结构推理”中从复杂、高维数据中学习并推理出结构的核心挑战相关。

**📖 中文摘要**

本文介绍了SpikeATac，一种结合了静态（电容式）和动态（PVDF薄膜）传感模式的多模态触觉手指。该手指的16个触元PVDF薄膜以4kHz采样，提供快速、灵敏的动态信号。论文展示了SpikeATac在抓取易碎、可变形物体时快速、轻柔停止的能力。此外，论文还提出了一种结合人类反馈强化学习和基于触觉奖励的学习方法，用于在多指灵巧手机器人手上微调策略以调制力量。该硬件平台和学习管道共同实现了一项此前未实现的困难灵巧接触任务：易碎物体的手内操作。虽然主要贡献在机器人触觉和操作领域，但其学习框架整合了强化学习和触觉反馈，用于解决接触丰富的操作问题。这种方法论——即结合学习与多模态传感（此处是触觉）来理解和控制复杂物理交互——与“质谱结构推理”中可能采用的、从多模态或高维数据（质谱）中学习并推理出分子结构的方法在理念上有相似之处。两者都涉及从复杂、噪声的传感器数据中提取有意义信息以进行决策或推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we introduce SpikeATac, a multimodal tactile finger combining a taxelized and highly sensitive dynamic response (PVDF) with a static transduction method (capacitive) for multimodal touch sensing. Named for its `spiky' response, SpikeATac's 16-taxel PVDF film sampled at 4 kHz provides fast, sensitive dynamic signals to the very onset and breaking of contact. We characterize the sensitivity of the different modalities, and show that SpikeATac provides the ability to stop quickly and delicately when grasping fragile, deformable objects. Beyond parallel grasping, we show that SpikeATac can be used in a learning-based framework to achieve new capabilities on a dexterous multifingered robot hand. We use a learning recipe that combines reinforcement learning from human feedback with tactile-based rewards to fine-tune the behavior of a policy to modulate force. Our hardware platform and learning pipeline together enable a difficult dexterous and contact-rich task that has not previously been achieved: in-hand manipulation of fragile objects. Videos are available at this https URL .

</details>

---

### 46. [FMint-SDE: A Multimodal Foundation Model for Accelerating Numerical Simulation of SDEs via Error Correction](https://arxiv.org/abs/2510.27173)

**基本信息**

- 🔗 arXiv: [`2510.27173`](https://arxiv.org/abs/2510.27173)
- 👥 作者: Jiaxin Yuan, Haizhao Yang, Maria Cameron
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27173.pdf)

**💡 相关性分析**

满足标准1：论文提出了FMint-SDE，一个用于加速随机微分方程数值模拟的多模态基础模型，并明确在分子动力学等化学相关应用上进行了评估。这直接服务于“化学大模型”主题中开发用于化学计算和模拟的大模型。

**📖 中文摘要**

本文介绍了FMint-SDE，一个基于解码器Transformer并具有上下文学习能力的多模态基础模型，用于加速随机微分方程（SDE）的数值模拟。该模型利用数值和文本模态来学习通用的误差校正方案。它使用传统求解器生成的粗略解序列进行提示训练，从而能够广泛泛化到不同的系统。论文在涵盖分子动力学、机械系统、金融和生物学应用的SDE基准测试套件上评估了模型。实验结果表明，与经典求解器相比，该方法实现了更优的精度-效率权衡。该工作的核心是开发一个用于科学模拟（包括分子动力学）的通用基础模型。分子动力学模拟是计算化学和化学信息学的基石之一。因此，一个旨在加速和改善分子动力学等SDE模拟的基础模型，直接与“化学大模型”主题相关，因为它为化学领域的计算模拟提供了一种新的大模型驱动工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fast and accurate simulation of dynamical systems is a fundamental challenge across scientific and engineering domains. Traditional numerical integrators often face a trade-off between accuracy and computational efficiency, while existing neural network-based approaches typically require training a separate model for each case. To overcome these limitations, we introduce a novel multi-modal foundation model for large-scale simulations of differential equations: FMint-SDE (Foundation Model based on Initialization for stochastic differential equations). Based on a decoder-only transformer with in-context learning, FMint-SDE leverages numerical and textual modalities to learn a universal error-correction scheme. It is trained using prompted sequences of coarse solutions generated by conventional solvers, enabling broad generalization across diverse systems. We evaluate our models on a suite of challenging SDE benchmarks spanning applications in molecular dynamics, mechanical systems, finance, and biology. Experimental results show that our approach achieves a superior accuracy-efficiency tradeoff compared to classical solvers, underscoring the potential of FMint-SDE as a general-purpose simulation tool for dynamical systems.

</details>

---

### 47. [FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding](https://arxiv.org/abs/2511.00141)

**基本信息**

- 🔗 arXiv: [`2511.00141`](https://arxiv.org/abs/2511.00141)
- 👥 作者: Janghoon Cho, Jungsoo Lee, Munawar Hayat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.00141.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效、通用的序列数据（视觉令牌）压缩框架FLoC。这种方法论为处理高维序列数据（如质谱）提供了新的工具思路，可能应用于“质谱结构推理”中的数据降维或关键特征提取。

**📖 中文摘要**

本文提出了FLoC，一种基于设施选址函数的高效视觉令牌压缩框架，用于长视频理解。该方法通过惰性贪婪算法快速选择视觉令牌的一个紧凑、高代表性且多样化的子集，在保证接近最优性能的同时，大幅减少视觉令牌数量。该方法无需训练、与模型无关且与查询无关，可以无缝集成到各种视频大语言模型（Video-LLMs）和现有工作流中。在Video-MME、MLVU、LongVideoBench和EgoSchema等大规模基准测试上的广泛评估表明，该框架 consistently 优于最近的压缩技术。虽然论文聚焦于视频理解，但其核心贡献是一种通用的、基于优化理论的令牌选择/压缩方法。这种方法论对于处理其他高维序列数据（例如，质谱数据可以视为一维或二维序列）具有潜在的适用性。在“质谱结构推理”中，经常需要从冗长的质谱峰序列中提取关键特征或进行降维，FLoC所体现的“选择最具代表性和多样性的子集”的思想可以为此提供启发。因此，该论文提供了一种可能适用于质谱数据预处理或特征提取的工具思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent studies in long video understanding have harnessed the advanced visual-language reasoning capabilities of Large Multimodal Models (LMMs), driving the evolution of video-LMMs specialized for processing extended video sequences. However, the scalability of these models is severely limited by the overwhelming volume of visual tokens generated from extended video sequences. To address this challenge, we propose FLoC, an efficient visual token compression framework based on the facility location function, a principled approach that swiftly selects a compact yet highly representative and diverse subset of visual tokens within a predefined budget on the number of visual tokens. By integrating the lazy greedy algorithm, our method achieves remarkable efficiency gains by swiftly selecting a compact subset of tokens, drastically reducing the number of visual tokens while guaranteeing near-optimal performance. Notably, our approach is training-free, model-agnostic, and query-agnostic, providing a versatile solution that seamlessly integrates with diverse video-LLMs and existing workflows. Extensive evaluations on large-scale benchmarks, such as Video-MME, MLVU, LongVideoBench, and EgoSchema, show that our framework consistently surpasses recent compression techniques, highlighting its effectiveness and robustness in addressing the challenges of long video understanding as well as its processing efficiency.

</details>

---

### 48. [Interleaved Tool-Call Reasoning for Protein Function Understanding](https://arxiv.org/abs/2601.03604)

**基本信息**

- 🔗 arXiv: [`2601.03604`](https://arxiv.org/abs/2601.03604)
- 👥 作者: Chuanliu Fan, Zicheng Ma, Huanran Meng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.03604.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何将大语言模型（作为化学/生物信息领域的一种大模型）与领域工具结合，以解决蛋白质功能理解这一化学信息学中的关键问题。

**📖 中文摘要**

这篇论文探讨了将大语言模型（LLM）的推理能力应用于蛋白质功能理解这一特定领域。作者指出，直接将基于文本的推理范式（如思维链）迁移到蛋白质功能预测等知识密集型科学任务中是无效的，因为这些任务从根本上依赖于外部的生物学先验知识和计算工具，而非纯粹的内部推理。为此，论文提出了PFUA，一个工具增强的蛋白质推理智能体框架。该框架统一了问题分解、工具调用和基于证据的答案生成过程，通过整合领域特定的工具来产生可验证的中间证据，从而增强模型在蛋白质功能预测任务中的表现。实验表明，PFUA在多个基准测试中显著优于纯文本推理模型。这项工作与“化学大模型”主题相关，因为它探索了LLM在化学/生物学领域的专业化应用和工具增强推理，属于核心主题的延伸。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

</details>

---

### 49. [Controlled LLM Training on Spectral Sphere](https://arxiv.org/abs/2601.08393)

**基本信息**

- 🔗 arXiv: [`2601.08393`](https://arxiv.org/abs/2601.08393)
- 👥 作者: Tian Xie, Haoming Luo, Haoyu Tang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.08393.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大语言模型的优化训练方法，这是构建和优化“化学大模型”所依赖的基础技术和核心挑战之一。

**📖 中文摘要**

本文提出了一种名为“谱球优化器（SSO）”的新优化器，旨在通过强制对权重及其更新施加严格的模块化谱约束，实现与最大更新参数化理论完全对齐的优化过程。该优化器被设计用于大规模语言模型的训练，并在包括密集模型和混合专家模型在内的多种架构上进行了预训练验证。论文的核心贡献在于改进大模型训练的稳定性和收敛性。这项工作与“化学大模型”主题间接相关，因为它专注于提升大语言模型（作为构建化学大模型的基础架构）的训练效率和稳定性。虽然不直接涉及化学数据或任务，但其关于大模型训练方法的研究是构建和优化领域大模型（如化学大模型）的重要技术基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only ``half-aligned'' with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the \textbf{Spectral Sphere Optimizer (SSO)}, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To enable large-scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

</details>

---

### 50. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)

**基本信息**

- 🔗 arXiv: [`2601.18734`](https://arxiv.org/abs/2601.18734)
- 👥 作者: Siyan Zhao, Zhihui Xie, Mengchen Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18734.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕提升大语言模型的推理能力，这是构建能够进行复杂“质谱结构推理”或化学问题解决的“化学大模型”的关键技术组成部分。

**📖 中文摘要**

本文提出了一种名为“策略内自蒸馏（OPSD）”的新框架，用于提升大语言模型的推理能力。在该框架中，单个模型同时扮演教师和学生的角色：教师策略可以访问特权信息（如已验证的推理轨迹），而学生策略只能看到问题；训练目标是最小化在学生自身生成的推理轨迹上，两种策略分布之间的每词元差异。该方法在多个数学推理基准测试中证明了其有效性。这项工作与“化学大模型”主题相关，因为它专注于改进大语言模型的推理能力，而强大的推理能力是化学大模型（例如用于质谱结构推理或逆合成分析）所需的核心能力之一。论文提出的自蒸馏框架为训练更高效、更强大的领域专用模型提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self (i.e., the version without access to privileged information), we introduce On-Policy Self-Distillation (OPSD), a framework where a single model acts as both teacher and student by conditioning on different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving 8-12x token efficiency compared to reinforcement learning methods such as GRPO and superior performance over off-policy distillation methods.

</details>

---

### 51. [Replacing Parameters with Preferences: Federated Alignment of Heterogeneous Vision-Language Models](https://arxiv.org/abs/2602.00485)

**基本信息**

- 🔗 arXiv: [`2602.00485`](https://arxiv.org/abs/2602.00485)
- 👥 作者: Shule Lu, Yujing Wang, Hainan Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00485.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕异构环境下多模态大模型（VLMs）的联邦对齐，其方法和技术可直接应用于解决“化学大模型”在隐私敏感场景下的训练、对齐与部署挑战。

**📖 中文摘要**

本文针对视觉语言模型在隐私敏感领域（如医疗、金融）的应用挑战，提出了一个基于联邦学习的对齐框架MoR。该框架旨在异构的客户端环境中（不同计算资源、应用需求、模型架构），通过混合奖励的群体相对策略优化来对齐视觉语言模型。其核心思想是用“偏好”而非原始数据或完整模型参数来进行联邦协作。论文在多个视觉问答基准上验证了该方法的有效性。这项工作与“化学大模型”主题高度相关。首先，它处理的是“视觉语言模型”这一多模态大模型的对齐问题，方法论可迁移至化学多模态大模型。其次，联邦学习框架为解决化学领域（如药物发现）中数据隐私和孤岛问题下的模型训练与对齐提供了可行的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

VLMs have broad potential in privacy-sensitive domains such as healthcare and finance, yet strict data-sharing constraints render centralized training infeasible. FL mitigates this issue by enabling decentralized training, but practical deployments face challenges due to client heterogeneity in computational resources, application requirements, and model architectures. We argue that while replacing data with model parameters characterizes the present of FL, replacing parameters with preferences represents a more scalable and privacy-preserving future. Motivated by this perspective, we propose MoR, a federated alignment framework based on GRPO with Mixture-of-Rewards for heterogeneous VLMs. MoR initializes a visual foundation model as a KL-regularized reference, while each client locally trains a reward model from local preference annotations, capturing specific evaluation signals without exposing raw data. To reconcile heterogeneous rewards, we introduce a routing-based fusion mechanism that adaptively aggregates client reward signals. Finally, the server performs GRPO with this mixed reward to optimize the base VLM. Experiments on three public VQA benchmarks demonstrate that MoR consistently outperforms federated alignment baselines in generalization, robustness, and cross-client adaptability. Our approach provides a scalable solution for privacy-preserving alignment of heterogeneous VLMs under federated settings.

</details>

---

### 52. [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2602.01601)

**基本信息**

- 🔗 arXiv: [`2602.01601`](https://arxiv.org/abs/2602.01601)
- 👥 作者: Hieu Trung Nguyen, Bao Nguyen, Wenao Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01601.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕优化用于训练大模型推理能力的强化学习算法，这是训练能够进行复杂决策和优化的“化学大模型”或化学智能体的关键技术。

**📖 中文摘要**

本文针对具有可验证奖励的强化学习中的采样效率瓶颈问题，提出了一种名为VIP的自适应采样分配策略。与现有方法（如GRPO）为所有训练提示均匀分配采样次数不同，VIP使用轻量级高斯过程模型预测每个提示的成功概率，并将其转化为梯度方差估计，进而通过凸优化在给定计算预算下确定最优的采样分配方案。实验表明，VIP能持续提高采样效率并在多个基准测试中取得更高性能。这项工作与“化学大模型”主题相关，因为它优化了用于训练大语言模型推理能力的强化学习流程。在化学领域，例如训练模型进行分子性质预测或反应条件优化时，常使用基于验证的奖励（如实验成功率、性质指标），因此高效的强化学习采样策略对于训练面向化学任务的智能体或大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce VIP, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, VIP uses a lightweight Gaussian process model to predict per-prompt success probabilities based on recent rollouts. These probability predictions are translated into variance estimates, which are then fed into a convex optimization problem to determine the optimal rollout allocations under a hard compute budget constraint. Empirical results show that VIP consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks.

</details>

---

### 53. [SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework](https://arxiv.org/abs/2602.17330)

**基本信息**

- 🔗 arXiv: [`2602.17330`](https://arxiv.org/abs/2602.17330)
- 👥 作者: Rong Fu, Zijian Zhang, Kun Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.17330.pdf)

**💡 相关性分析**

满足标准2：论文提出的SubQuad框架，其核心算法（近次二次方检索、GPU加速核函数、多模态融合）为解决质谱结构推理中的关键计算瓶颈（成对谱图/结构比较的高昂成本）和数据集不平衡问题提供了潜在的工具和方法论资源。

**📖 中文摘要**

这篇论文提出了SubQuad，一个用于自适应免疫受体库比较分析的计算框架。其核心目标是解决两个瓶颈：近二次方的成对亲和力评估成本和数据集不平衡问题。虽然论文主要关注免疫学应用，但其提出的“近次二次方检索”方法、GPU加速的亲和力核函数以及学习型多模态融合技术，为解决“质谱结构推理”中常见的计算密集型成对比较（如质谱与候选结构之间的相似性计算）和数据集不平衡问题提供了通用的算法思路和工具。因此，它提供了可用于质谱结构推理任务的计算方法和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Comparative analysis of adaptive immune repertoires at population scale is hampered by two practical bottlenecks: the near-quadratic cost of pairwise affinity evaluations and dataset imbalances that obscure clinically important minority clonotypes. We introduce SubQuad, an end-to-end pipeline that addresses these challenges by combining antigen-aware, near-subquadratic retrieval with GPU-accelerated affinity kernels, learned multimodal fusion, and fairness-constrained clustering. The system employs compact MinHash prefiltering to sharply reduce candidate comparisons, a differentiable gating module that adaptively weights complementary alignment and embedding channels on a per-pair basis, and an automated calibration routine that enforces proportional representation of rare antigen-specific subgroups. On large viral and tumor repertoires SubQuad achieves measured gains in throughput and peak memory usage while preserving or improving recall@k, cluster purity, and subgroup equity. By co-designing indexing, similarity fusion, and equity-aware objectives, SubQuad offers a scalable, bias-aware platform for repertoire mining and downstream translational tasks such as vaccine target prioritization and biomarker discovery.

</details>

---

### 54. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型（Zatom-1），这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

这篇论文提出了Zatom-1，一个用于3D分子和材料统一建模的多模态流匹配基础模型。Zatom-1是一个Transformer模型，通过联合建模离散原子类型和连续3D几何结构，统一了生成（如分子生成）和预测（如性质预测）任务。它通过联合生成预训练作为下游多任务预测的通用初始化。该模型直接针对3D分子结构进行生成和预测，是“化学大模型”在三维分子表示与生成领域的典型代表。其多任务统一框架和流匹配生成方法，为化学领域的通用基础模型提供了新的范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first end-to-end, fully open-source foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 55. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发高效准确的机器学习原子间势能（MLIP）基础模型（MatRIS），这属于“化学大模型”在计算化学和材料科学中的应用。

**📖 中文摘要**

这篇论文提出了MatRIS，一个旨在构建可靠且高效的预训练机器学习原子间势能（MLIP）模型。MatRIS是一个不变性MLIP，引入了基于注意力的三体相互作用建模，并采用具有线性复杂度的可分离注意力机制以实现可扩展性。论文在包括Matbench-Discovery、MatPES在内的多个流行基准测试上评估了其性能。该工作致力于开发准确高效的MLIPs，这是“化学大模型”在计算材料科学和分子模拟领域的一个重要子方向，即用于替代传统量子化学计算的、基于机器学习的势能函数模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 56. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准3：论文对顺序推理在联想记忆模型中的动力学进行了理论分析，这为理解包括化学信息学或质谱分析中可能使用的推理模型在内的AI推理架构提供了重要的理论讨论和见解。

**📖 中文摘要**

这篇论文为输入驱动的Hopfield网络中的顺序检索开发了一个动力学理论。它分析了耦合快速关联检索与慢速推理动力学的双时间尺度架构，推导了自持记忆转换的明确条件。该工作将经典的Hopfield动力学与现代推理架构联系起来，旨在为顺序推理提供原理性的数学解释。虽然论文聚焦于联想记忆模型，但其对“顺序推理”动力学和架构的理论分析，为理解更广泛的AI推理系统（可能包括用于化学或质谱推理的模型）的内部机制提供了理论基础和见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 57. [Structured quantum learning via em algorithm for Boltzmann machines](https://arxiv.org/abs/2507.21569)

**基本信息**

- 🔗 arXiv: [`2507.21569`](https://arxiv.org/abs/2507.21569)
- 👥 作者: Takeshi Kimura, Kohtaro Kato, Masahito Hayashi
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.21569.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于训练量子生成模型（量子玻尔兹曼机）的新算法（量子EM算法），这为量子机器学习领域提供了新的工具和方法。这些工具有潜力未来被应用于化学或质谱数据的量子计算建模中。

**📖 中文摘要**

这篇论文为量子玻尔兹曼机（QBMs）引入了一种量子版本的EM算法，这是一种信息几何意义上对经典期望最大化方法的推广。该方法规避了在非凸函数上的基于梯度的优化，从而潜在地缓解了量子机器学习中因系统尺寸增大而梯度指数消失的“贫瘠高原”问题。该工作在半量子受限玻尔兹曼机（sqRBM）上实现了该方法。虽然主要应用于通用生成建模，但量子机器学习算法（如用于训练量子生成模型的算法）的进展，为未来可能应用于化学或质谱数据建模的量子计算范式提供了工具和方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Boltzmann machines (QBMs) are generative models with potential advantages in quantum machine learning, yet their training is fundamentally limited by the barren plateau problem, where gradients vanish exponentially with system size. We introduce a quantum version of the em algorithm, an information-geometric generalization of the classical Expectation-Maximization method, which circumvents gradient-based optimization on non-convex functions. Implemented on a semi-quantum restricted Boltzmann machine (sqRBM) -- a hybrid architecture with quantum effects confined to the hidden layer -- our method achieves stable learning and outperforms gradient descent on multiple benchmark datasets. These results establish a structured and scalable alternative to gradient-based training in QML, offering a pathway to mitigate barren plateaus and enhance quantum generative modeling.

</details>

---

### 58. [CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery](https://arxiv.org/abs/2511.19500)

**基本信息**

- 🔗 arXiv: [`2511.19500`](https://arxiv.org/abs/2511.19500)
- 👥 作者: Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.19500.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门用于化学材料发现的大规模精选数据集（OPV2D），并构建了包含预测和生成模型的机器学习框架，这些数据资源和工具可直接用于化学大模型（特别是针对分子性质预测和生成）的研究。

**📖 中文摘要**

本文介绍了一个用于有机光伏（OPV）材料发现的机器学习框架CycleChemist。该框架的核心贡献包括：1）构建了有机光伏供体-受体数据集（OPV2D），这是目前同类中最大的、包含2000个实验表征的供体-受体对的精选数据集。2）开发了一个结合了预测建模与生成分子设计的双机器学习框架，其中包含用于预测材料是否具有OPV行为的分类器（OPVC）、用于预测HOMO和LUMO能级的分子轨道能量估计器（MOE2）、用于估计功率转换效率（PCE）的光伏性能预测器（P3），以及用于生成可合成有机半导体的材料生成预训练变换器（MatGPT）。该工作通过将分子表示学习与性能预测相结合，推进了高性能OPV材料的数据驱动发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials.

</details>

---

### 59. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种新的潜在推理架构（LatentChem），旨在解决当前化学大语言模型在推理效率和表示匹配上的根本问题，并进行了系统的基准测试和性能评估。

**📖 中文摘要**

本文针对化学大语言模型（LLMs）提出了一种名为LatentChem的潜在推理接口。作者指出，当前化学LLMs主要依赖自然语言中的显式思维链（CoT）进行复杂推理，但化学推理本质上是连续和结构化的，将其强制转化为离散的语言标记会造成表示上的不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中直接执行多步推理，而仅对最终输出生成语言。研究发现，当仅针对任务成功率进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变带来了计算优势。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相比基于CoT的基线模型取得了59.88%的非平局胜率，同时实现了平均10.84倍的推理加速。结果表明，化学推理更自然、更有效地体现为连续的潜在动态过程，而非离散的语言轨迹。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 60. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准1和2：1）论文的核心方法（基于FGW距离的共形预测）直接适用于“质谱结构推理”中的一个关键挑战——即从质谱数据推断出的分子结构（图）的不确定性量化。2）论文提出的框架和度量方法（Z-Gromov-Wasserstein/FGW）为处理图结构数据（如分子）的预测和不确定性评估提供了新的工具和思路。

**📖 中文摘要**

本文提出了一种用于图结构输出（如图形）的共形预测框架，旨在为结构化输出空间提供分布自由的覆盖保证。该方法的核心是通过Z-Gromov-Wasserstein距离（实践中实例化为融合Gromov-Wasserstein距离，FGW）来定义非共形性度量，从而实现预测图与候选图之间排列不变的比较。为了获得自适应的预测集，作者将适用于复杂输出空间的Score Conformalized Quantile Regression (SCQR) 方法扩展到图值输出。论文在一个合成任务和一个真实的分子识别问题上评估了所提出的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 61. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个自动化DFT计算的多智能体框架（TritonDFT）和一个评估基准（DFTBench）。DFT是计算化学和材料科学中获取分子和材料性质（如能量、光谱）的核心工具，这些性质数据是构建和训练“化学大模型”以及辅助“质谱结构推理”的重要数据来源。该框架和工具集能够高效、自动化地生成高质量的计算化学数据，因此与主题高度相关。

**📖 中文摘要**

本文介绍了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学的基石，但其实际执行需要协调复杂、多步骤的工作流程。现有的工具和基于大语言模型（LLM）的解决方案只能自动化部分步骤，缺乏对完整工作流自动化、多样化任务适应以及DFT配置中精度-成本权衡优化的支持。TritonDFT通过专家策划的可扩展工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效、准确的DFT执行。此外，作者还引入了DFTBench，一个用于评估智能体在多维度能力（涵盖科学专业知识、权衡优化、高性能计算知识和成本效率）的基准测试。TritonDFT为实际使用提供了开放的交互界面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：13
- 累计论文数量：892

## 📝 历史记录

> 暂无历史数据

