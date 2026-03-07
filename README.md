# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-07 01:21:59

## 📅 2026-03-07 (今日最新)

**相关论文数：62**

### 1. [A unified foundational framework for knowledge injection and evaluation of Large Language Models in Combustion Science](https://arxiv.org/abs/2603.04452)

**基本信息**

- 🔗 arXiv: [`2603.04452`](https://arxiv.org/abs/2603.04452)
- 👥 作者: Zonglin Yang, Runze Mao, Tianhao Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04452.pdf)

**💡 相关性分析**

满足标准1和标准2：论文核心研究内容围绕为特定化学领域（燃烧科学）构建和评估领域专业化的大语言模型（化学大模型），并提供了专门构建的数据集（知识库）和评估基准（CombustionQA）。

**📖 中文摘要**

本文提出了一个用于燃烧科学领域大语言模型（LLM）知识注入和评估的统一基础框架。该框架包含一个规模达35亿token的多模态知识库（从同行评审文章、论文和燃烧CFD代码中提取）、一个包含436个问题的严格评估基准（CombustionQA），以及一个三阶段知识注入路径（从检索增强生成到知识图谱增强检索和持续预训练）。该研究直接针对“化学大模型”主题，旨在为特定科学领域（燃烧学）构建和评估领域专业化的大模型。论文不仅提供了数据集和评估基准，还探讨了知识注入方法，完全符合核心主题相关和数据资源相关的标准。

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

满足标准1：论文的核心研究内容是利用对比学习对齐科学数据（X射线光谱）与科学文献文本，以构建共享的多模态表示。这直接关联到利用大模型处理和理解化学/科学领域多模态信息的主题，是构建领域大模型的关键技术路径之一。

**📖 中文摘要**

本文介绍了一个对比学习框架，旨在将X射线光谱与从科学文献中提取的领域知识对齐，以促进共享多模态表示的发展。该工作通过融合光谱和文本数据，改进了对20个物理变量的估计，性能比单模态光谱基线提高了16-18%。研究结果表明，融合观测数据和现有文献的框架可以扩展到其他科学领域。这项工作展示了如何利用大语言模型处理科学文本，并将其与科学数据（如光谱）进行对齐和融合，这为构建能够理解和推理科学文献与数据的“化学大模型”或“科学大模型”提供了方法论上的参考。

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

满足标准1：论文的核心研究内容是设计一个多智能体系统来自主发现数学概念和结构。其方法论（多智能体协作、假设生成与验证、从数据中学习结构）对于构建能够进行化学结构推理或发现化学规律的“化学大模型”具有直接的启发和参考价值。

**📖 中文摘要**

本文提出了一种新的多智能体模型，用于计算数学发现，其灵感来源于数学概念通过实验、证明尝试和反例的相互作用而出现的过程。该系统自主提出猜想并尝试证明它们，根据反馈和不断演化的数据分布做出决策。该模型以从多面体数据中自主恢复同调概念的任务为基准，并成功完成了这一学习问题。这项研究展示了多智能体系统如何通过优化局部过程的组合来发现数学中有趣的概念。虽然主题是数学发现，但其核心方法论——使用多智能体系统和学习框架来发现和推理复杂领域（如数学，可类比化学）中的潜在概念和结构——与构建能够进行科学发现和结构推理的“化学大模型”在理念和技术路径上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical concepts emerge through an interplay of processes, including experimentation, efforts at proof, and counterexamples. In this paper, we present a new multi-agent model for computational mathematical discovery based on this observation. Our system, conceived with research in mind, poses its own conjectures and then attempts to prove them, making decisions informed by this feedback and an evolving data distribution. Inspired by the history of Euler's conjecture for polyhedra and an open challenge in the literature, we benchmark with the task of autonomously recovering the concept of homology from polyhedral data and knowledge of linear algebra. Our system completes this learning problem. Most importantly, the experiments are ablations, statistically testing the value of the complete dynamic and controlling for experimental setup. They support our main claim: that the optimisation of the right combination of local processes can lead to surprisingly well-aligned notions of mathematical interestingness.

</details>

---

### 4. [PTLD: Sim-to-real Privileged Tactile Latent Distillation for Dexterous Manipulation](https://arxiv.org/abs/2603.04531)

**基本信息**

- 🔗 arXiv: [`2603.04531`](https://arxiv.org/abs/2603.04531)
- 👥 作者: Rosy Chen, Mustafa Mukadam, Michael Kaess 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04531.pdf)

**💡 相关性分析**

满足标准1：论文提出的“特权信息蒸馏”框架是一种新颖的模型训练与增强范式。虽然应用于机器人触觉，但其方法论对于解决“质谱结构推理”中数据稀缺、多模态信息融合等挑战具有潜在的借鉴意义，可被视为一种相关的方法论研究。

**📖 中文摘要**

本文提出了PTLD（特权触觉潜在蒸馏），一种无需触觉模拟即可学习触觉操作技能的新方法。其核心思想是利用真实世界中的特权传感器收集真实的触觉策略数据，然后用于蒸馏出一个基于触觉输入的鲁棒状态估计器。该方法通过将特权策略知识蒸馏到仅使用触觉的模型中，提升了在模拟中训练的操控策略。虽然应用场景是机器人操作，但其核心技术创新点——利用特权信息（可视为一种“教师”模型或更丰富的数据模态）来蒸馏和增强一个目标模态（触觉）的模型性能——与“质谱结构推理”中可能面临的挑战有相似之处。例如，在质谱解析中，可以设想利用更丰富但难以获取的标样数据或量子化学计算作为“特权信息”，来蒸馏一个仅从质谱数据推理结构的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tactile dexterous manipulation is essential to automating complex household tasks, yet learning effective control policies remains a challenge. While recent work has relied on imitation learning, obtaining high quality demonstrations for multi-fingered hands via robot teleoperation or kinesthetic teaching is prohibitive. Alternatively, with reinforcement we can learn skills in simulation, but fast and realistic simulation of tactile observations is challenging. To bridge this gap, we introduce PTLD: sim-to-real Privileged Tactile Latent Distillation, a novel approach to learning tactile manipulation skills without requiring tactile simulation. Instead of simulating tactile sensors or relying purely on proprioceptive policies to transfer zero-shot sim-to-real, our key idea is to leverage privileged sensors in the real world to collect real-world tactile policy data. This data is then used to distill a robust state estimator that operates on tactile input. We demonstrate from our experiments that PTLD can be used to improve proprioceptive manipulation policies trained in simulation significantly by incorporating tactile sensing. On the benchmark in-hand rotation task, PTLD achieves a 182% improvement over a proprioception only policy. We also show that PTLD enables learning the challenging task of tactile in-hand reorientation where we see a 57% improvement in the number of goals reached over using proprioception alone. Website: this https URL .

</details>

---

### 5. [Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling](https://arxiv.org/abs/2603.04553)

**基本信息**

- 🔗 arXiv: [`2603.04553`](https://arxiv.org/abs/2603.04553)
- 👥 作者: Tal Daniel, Carl Qi, Dan Haramati 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04553.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从高维、复杂的观测数据（视频）中无监督地学习以物体为中心的结构化表征和动力学模型。这本质上是一个“从数据推理结构”的问题，其技术思路（解耦表征、学习动力学）对于“质谱结构推理”（从质谱信号推理分子结构）这一具体领域的研究具有重要的方法论参考价值。

**📖 中文摘要**

本文介绍了潜在粒子世界模型（LPWM），一种可扩展到真实世界多物体数据集并适用于决策的、自监督的以物体为中心的世界模型。LPWM直接从视频数据中自主发现关键点、边界框和物体掩码，使其能够在没有监督的情况下学习丰富的场景分解。该架构通过新颖的潜在动作模块对随机粒子动力学进行建模。LPWM除了随机视频建模外，还 readily适用于决策任务，如目标条件模仿学习。这项研究展示了如何从高维观测数据（视频）中无监督地解耦出可解释的、以物体为中心的表征，并用于建模动态和决策。这种从复杂数据中推断结构化、可操作表示的能力，与“质谱结构推理”中从质谱数据推断分子结构这一核心任务在抽象层面上高度一致，都是“从信号到结构”的推理问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Latent Particle World Model (LPWM), a self-supervised object-centric world model scaled to real-world multi-object datasets and applicable in decision-making. LPWM autonomously discovers keypoints, bounding boxes, and object masks directly from video data, enabling it to learn rich scene decompositions without supervision. Our architecture is trained end-to-end purely from videos and supports flexible conditioning on actions, language, and image goals. LPWM models stochastic particle dynamics via a novel latent action module and achieves state-of-the-art results on diverse real-world and synthetic datasets. Beyond stochastic video modeling, LPWM is readily applicable to decision-making, including goal-conditioned imitation learning, as we demonstrate in the paper. Code, data, pre-trained models and video rollouts are available: this https URL

</details>

---

### 6. [Structure-Guided Histopathology Synthesis via Dual-LoRA Diffusion](https://arxiv.org/abs/2603.04565)

**基本信息**

- 🔗 arXiv: [`2603.04565`](https://arxiv.org/abs/2603.04565)
- 👥 作者: Xuan Xu, Prateek Prasanna
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04565.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种利用明确结构先验（细胞核中心点）来引导扩散模型进行图像合成与补全的方法。这种“结构先验引导的生成/推理”范式，对于“质谱结构推理”中如何融入化学规则或结构片段知识来约束分子结构生成，提供了有价值的技术思路。

**📖 中文摘要**

本文提出了双LoRA可控扩散模型，一个统一的以细胞核中心点为指导的扩散框架，联合支持局部结构补全和全局结构合成。多类细胞核中心点作为轻量级且注释高效的空间先验，在图像部分或完全缺失的情况下提供具有生物学意义的指导。两个任务特定的LoRA适配器使共享主干专门用于局部和全局目标，而无需重新训练单独的扩散模型。这项研究在组织病理学图像合成中，利用结构先验（细胞核位置）指导生成模型，实现了更逼真和结构一致的结果。虽然应用领域是生物医学图像，但其核心思想——利用明确的结构性先验（在本文中是细胞核中心点）来引导生成模型完成修复或合成任务——与“质谱结构推理”中可能利用的化学知识或结构片段作为先验来约束推理过程，在概念上是相通的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathology image synthesis plays an important role in tissue restoration, data augmentation, and modeling of tumor microenvironments. However, existing generative methods typically address restoration and generation as separate tasks, although both share the same objective of structure-consistent tissue synthesis under varying degrees of missingness, and often rely on weak or inconsistent structural priors that limit realistic cellular organization. We propose Dual-LoRA Controllable Diffusion, a unified centroid-guided diffusion framework that jointly supports Local Structure Completion and Global Structure Synthesis within a single model. Multi-class nuclei centroids serve as lightweight and annotation-efficient spatial priors, providing biologically meaningful guidance under both partial and complete image absence. Two task-specific LoRA adapters specialize the shared backbone for local and global objectives without retraining separate diffusion models. Extensive experiments demonstrate consistent improvements over state-of-the-art GAN and diffusion baselines across restoration and synthesis tasks. For local completion, LPIPS computed within the masked region improves from 0.1797 (HARP) to 0.1524, and for global synthesis, FID improves from 225.15 (CoSys) to 76.04, indicating improved structural fidelity and realism. Our approach achieves more faithful structural recovery in masked regions and substantially improved realism and morphology consistency in full synthesis, supporting scalable pan-cancer histopathology modeling.

</details>

---

### 7. [PDE foundation model-accelerated inverse estimation of system parameters in inertial confinement fusion](https://arxiv.org/abs/2603.04606)

**基本信息**

- 🔗 arXiv: [`2603.04606`](https://arxiv.org/abs/2603.04606)
- 👥 作者: Mahindra Rautela, Alexander Scheinker, Bradley Love 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04606.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用PDE基础模型（一种科学大模型）解决物理化学领域的逆问题，这与“化学大模型”主题直接相关。

**📖 中文摘要**

本文研究了一个惯性约束聚变（ICF）中的逆问题：从多模态、快照式观测中估计系统参数。该工作利用JAG基准数据集，对一个偏微分方程（PDE）基础模型进行微调，并训练一个轻量级的任务特定头，以联合重建高光谱图像和回归系统参数。这项工作与“化学大模型”主题相关，因为它探索了PDE基础模型（一种特定类型的科学大模型）在解决复杂科学逆问题中的应用。它展示了基础模型在数据有限的情况下，通过微调来提高样本效率的能力，这为化学信息学中类似的大模型应用（例如，从光谱数据逆向推断分子结构或性质）提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PDE foundation models are typically pretrained on large, diverse corpora of PDE datasets and can be adapted to new settings with limited task-specific data. However, most downstream evaluations focus on forward problems, such as autoregressive rollout prediction. In this work, we study an inverse problem in inertial confinement fusion (ICF): estimating system parameters (inputs) from multi-modal, snapshot-style observations (outputs). Using the open JAG benchmark, which provides hyperspectral X-ray images and scalar observables per simulation, we finetune the PDE foundation model and train a lightweight task-specific head to jointly reconstruct hyperspectral images and regress system parameters. The fine-tuned model achieves accurate hyperspectral reconstruction (test MSE 1.2e-3) and strong parameter-estimation performance (up to R^2=0.995). Data-scaling experiments (5%-100% of the training set) show consistent improvements in both reconstruction and regression losses as the amount of training data increases, with the largest marginal gains in the low-data regime. Finally, finetuning from pretrained MORPH weights outperforms training the same architecture from scratch, demonstrating that foundation-model initialization improves sample efficiency for data-limited inverse problems in ICF.

</details>

---

### 8. [When Agents Persuade: Propaganda Generation and Mitigation in LLMs](https://arxiv.org/abs/2603.04636)

**基本信息**

- 🔗 arXiv: [`2603.04636`](https://arxiv.org/abs/2603.04636)
- 👥 作者: Julia Jose, Ritik Roongta, Rachel Greenstadt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04636.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过可微分物理模拟解决从观测信号（dMRI）逆向推断微观结构（渗透性）的逆问题。这与“质谱结构推理”从质谱图逆向推断分子结构的核心主题在问题定义、方法论和技术路线上高度一致。

**📖 中文摘要**

本文提出了Spinverse，一种用于从扩散MRI (dMRI) 测量中感知渗透性的微结构重建方法。它通过一个完全可微分的Bloch-Torrey模拟器来反演dMRI测量。Spinverse将组织表示在固定的四面体网格上，并将每个内部面的渗透率作为可学习参数；低渗透率的面充当扩散屏障，因此微结构边界（其拓扑结构不是先验固定的）无需改变网格连接性或顶点位置即可出现。给定目标信号，通过反向传播信号匹配损失来优化面渗透率，并通过阈值化学习到的渗透率场来恢复界面。这项工作与“质谱结构推理”在方法论上高度相似。虽然领域不同（dMRI vs. 质谱），但核心都是解决一个逆问题：从宏观观测信号（dMRI信号/质谱图）中推断微观结构（组织渗透性/分子结构）。Spinverse使用的可微分物理模拟和基于梯度的优化，正是“质谱结构推理”中从谱图推断分子结构所需的核心技术路径（如可微分质谱模拟器）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their wide-ranging benefits, LLM-based agents deployed in open environments can be exploited to produce manipulative material. In this study, we task LLMs with propaganda objectives and analyze their outputs using two domain-specific models: one that classifies text as propaganda or non-propaganda, and another that detects rhetorical techniques of propaganda (e.g., loaded language, appeals to fear, flag-waving, name-calling). Our findings show that, when prompted, LLMs exhibit propagandistic behaviors and use a variety of rhetorical techniques in doing so. We also explore mitigation via Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and ORPO (Odds Ratio Preference Optimization). We find that fine-tuning significantly reduces their tendency to generate such content, with ORPO proving most effective.

</details>

---

### 9. [Spinverse: Differentiable Physics for Permeability-Aware Microstructure Reconstruction from Diffusion MRI](https://arxiv.org/abs/2603.04638)

**基本信息**

- 🔗 arXiv: [`2603.04638`](https://arxiv.org/abs/2603.04638)
- 👥 作者: Prathamesh Pradeep Khole, Mario M. Brenes, Zahra Kais Petiwala 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04638.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过可微分物理模拟解决从观测信号（dMRI）逆向推断微观结构（渗透性）的逆问题。这与“质谱结构推理”从质谱图逆向推断分子结构的核心主题在问题定义、方法论和技术路线上高度一致。

**📖 中文摘要**

本文提出了Spinverse，一种用于从扩散MRI (dMRI) 测量中感知渗透性的微结构重建方法。它通过一个完全可微分的Bloch-Torrey模拟器来反演dMRI测量。Spinverse将组织表示在固定的四面体网格上，并将每个内部面的渗透率作为可学习参数；低渗透率的面充当扩散屏障，因此微结构边界（其拓扑结构不是先验固定的）无需改变网格连接性或顶点位置即可出现。给定目标信号，通过反向传播信号匹配损失来优化面渗透率，并通过阈值化学习到的渗透率场来恢复界面。这项工作与“质谱结构推理”在方法论上高度相似。虽然领域不同（dMRI vs. 质谱），但核心都是解决一个逆问题：从宏观观测信号（dMRI信号/质谱图）中推断微观结构（组织渗透性/分子结构）。Spinverse使用的可微分物理模拟和基于梯度的优化，正是“质谱结构推理”中从谱图推断分子结构所需的核心技术路径（如可微分质谱模拟器）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion MRI (dMRI) is sensitive to microstructural barriers, yet most existing methods either assume impermeable boundaries or estimate voxel-level parameters without recovering explicit interfaces. We present Spinverse, a permeability-aware reconstruction method that inverts dMRI measurements through a fully differentiable Bloch-Torrey simulator. Spinverse represents tissue on a fixed tetrahedral grid and treats each interior face permeability as a learnable parameter; low-permeability faces act as diffusion barriers, so microstructural boundaries whose topology is not fixed a priori (up to the resolution of the ambient mesh) emerge without changing mesh connectivity or vertex positions. Given a target signal, we optimize face permeabilities by backpropagating a signal-matching loss through the PDE forward model, and recover an interface by thresholding the learned permeability field. To mitigate the ill-posedness of permeability inversion, we use mesh-based geometric priors; to avoid local minima, we use a staged multi-sequence optimization curriculum. Across a collection of synthetic voxel meshes, Spinverse reconstructs diverse geometries and demonstrates that sequence scheduling and regularization are critical to avoid outline-only solutions while improving both boundary accuracy and structural validity.

</details>

---

### 10. [Stan: An LLM-based thermodynamics course assistant](https://arxiv.org/abs/2603.04657)

**基本信息**

- 🔗 arXiv: [`2603.04657`](https://arxiv.org/abs/2603.04657)
- 👥 作者: Eric M. Furst, Vasudevan Venkateshwaran
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04657.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于化学工程热力学课程的LLM-based智能助手，这是一个在化学领域应用大模型（尽管规模可能不大）的具体案例，与“化学大模型”的应用主题直接相关。

**📖 中文摘要**

本文介绍了Stan，一套为本科化学工程热力学课程构建的工具套件，基于一个共享的讲座转录稿和结构化教科书索引的数据管道。在学生端，一个检索增强生成（RAG）管道通过提取技术术语、将其与教科书索引匹配，并合成带有具体章节和页面引用的有根据的回答，来回答自然语言查询。在教师端，相同的转录稿语料库通过结构化分析管道进行处理，生成每堂课的摘要、识别学生问题和困惑时刻，并分类用于激发难懂材料的轶事和类比。这项工作与“化学大模型”主题相关，因为它展示了一个在特定化学工程子领域（热力学）中构建和部署基于LLM的领域专用智能助手（可视为一种垂直领域的小型“大模型”应用）的完整案例。它涉及了RAG、本地化部署、结构化信息提取等与大模型应用相关的关键技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discussions of AI in education focus predominantly on student-facing tools -- chatbots, tutors, and problem generators -- while the potential for the same infrastructure to support instructors remains largely unexplored. We describe Stan, a suite of tools for an undergraduate chemical engineering thermodynamics course built on a data pipeline that we develop and deploy in dual roles: serving students and supporting instructors from a shared foundation of lecture transcripts and a structured textbook index. On the student side, a retrieval-augmented generation (RAG) pipeline answers natural-language queries by extracting technical terms, matching them against the textbook index, and synthesizing grounded responses with specific chapter and page references. On the instructor side, the same transcript corpus is processed through structured analysis pipelines that produce per-lecture summaries, identify student questions and moments of confusion, and catalog the anecdotes and analogies used to motivate difficult material -- providing a searchable, semester-scale record of teaching that supports course reflection, reminders, and improvement. All components, including speech-to-text transcription, structured content extraction, and interactive query answering, run entirely on locally controlled hardware using open-weight models (Whisper large-v3, Llama~3.1 8B) with no dependence on cloud APIs, ensuring predictable costs, full data privacy, and reproducibility independent of third-party services. We describe the design, implementation, and practical failure modes encountered when deploying 7--8 billion parameter models for structured extraction over long lecture transcripts, including context truncation, bimodal output distributions, and schema drift, along with the mitigations that resolved them.

</details>

---

### 11. [Neuro-Symbolic Financial Reasoning via Deterministic Fact Ledgers and Adversarial Low-Latency Hallucination Detector](https://arxiv.org/abs/2603.04663)

**基本信息**

- 🔗 arXiv: [`2603.04663`](https://arxiv.org/abs/2603.04663)
- 👥 作者: Pedram Agand
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04663.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决LLMs在需要精确、确定性推理的领域（如金融）中的根本缺陷，并提出了新的架构。这些挑战和解决方案与在“化学大模型”和“质谱结构推理”中确保模型输出的科学准确性和可靠性所面临的问题高度相关。

**📖 中文摘要**

本文针对高风险的金融领域，指出了标准检索增强生成（RAG）架构的两个根本性局限：大型语言模型（LLMs）固有的算术不称职性，以及密集向量检索的分布语义混淆。为了在确定性领域实现零幻觉的金融推理，作者引入了可验证数值推理代理（VeNRA）。VeNRA将RAG范式从检索概率性文本转变为通过严格类型的通用事实账本（UFL）检索确定性变量，并通过一种新颖的双锁接地算法进行数学约束。这项工作与“化学大模型”和“质谱结构推理”主题相关，因为它深入探讨了LLMs在需要精确数值和确定性推理的科学领域（如化学、质谱分析）中应用时可能遇到的类似根本问题（如算术错误、语义混淆）。论文提出的解决方案（如UFL、确定性检索）为解决科学大模型在化学和质谱推理中的可靠性和可验证性问题提供了重要的思路和参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Standard Retrieval-Augmented Generation (RAG) architectures fail in high-stakes financial domains due to two fundamental limitations: the inherent arithmetic incompetence of Large Language Models (LLMs) and the distributional semantic conflation of dense vector retrieval (e.g., mapping ``Net Income'' to ``Net Sales'' due to contextual proximity). In deterministic domains, a 99% accuracy rate yields 0% operational trust. To achieve zero-hallucination financial reasoning, we introduce the Verifiable Numerical Reasoning Agent (VeNRA). VeNRA shifts the RAG paradigm from retrieving probabilistic text to retrieving deterministic variables via a strictly typed Universal Fact Ledger (UFL), mathematically bounded by a novel Double-Lock Grounding algorithm. Recognizing that upstream parsing anomalies inevitably occur, we introduce the VeNRA Sentinel: a 3-billion parameter SLM trained to forensically audit Python execution traces with only one token test budget. To train this model, we avoid traditional generative hallucination datasets in favor of Adversarial Simulation, programmatically sabotaging golden financial records to simulate production-level ``Ecological Errors'' (e.g., Logic Code Lies and Numeric Neighbor Traps). Finally, to optimize the Sentinel under strict latency budgets, we utilize a single-pass classification paradigm with optional post thinking for debug. We identify the phenomenon of Loss Dilution in Reverse-Chain-of-Thought training and present a novel, OOM-safe Micro-Chunking loss algorithm to stabilize gradients under extreme differential penalization.

</details>

---

### 12. [Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings](https://arxiv.org/abs/2603.04692)

**基本信息**

- 🔗 arXiv: [`2603.04692`](https://arxiv.org/abs/2603.04692)
- 👥 作者: Lyle Regenwetter, Rosen Yu, Cyril Picard 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04692.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文研究如何通过合成数据筛选使表格基础模型更好地适应工程/科学领域（包括化学），这与“化学大模型”的领域适应主题相关。2) 数据资源相关：论文提出了TREDBench数据集和一种合成数据筛选方法，这些资源和方法可用于改进化学等领域的基础模型。

**📖 中文摘要**

本文针对工程应用中的预测建模，指出现有的表格基础模型的合成训练分布可能无法反映工程数据的统计结构，从而限制了向工程回归的迁移。作者引入了TREDBench，一个包含83个真实世界表格回归数据集的精选集合，并使用TabPFN 2.5的数据集级嵌入来研究公共表示空间中的领域结构。他们发现工程数据集与非工程数据集部分可区分，而标准程序生成的数据集与工程数据集高度可区分，揭示了显著的合成-真实领域差距。为了在不使用真实工程样本训练的情况下弥合这一差距，作者提出了一种嵌入引导的合成数据筛选方法：生成并识别“类工程”合成数据集，并仅使用选定的合成任务对TabPFN 2.5进行持续预训练。这项工作与“化学大模型”主题相关，因为它关注于基础模型（此处是表格基础模型）在科学和工业领域（如化学）的迁移和适应问题，其中真实数据收集是主要瓶颈。论文提出的合成数据筛选方法为在数据稀疏的化学领域改进基础模型性能提供了可行的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression datasets with expert engineering/non-engineering labels, and use TabPFN 2.5's dataset-level embedding to study domain structure in a common representation space. We find that engineering datasets are partially distinguishable from non-engineering datasets, while standard procedurally generated datasets are highly distinguishable from engineering datasets, revealing a substantial synthetic-real domain gap. To bridge this gap without training on real engineering samples, we propose an embedding-guided synthetic data curation method: we generate and identify "engineering-like" synthetic datasets, and perform continued pre-training of TabPFN 2.5 using only the selected synthetic tasks. Across 35 engineering regression datasets, this synthetic-only adaptation improves predictive accuracy and data efficiency, outperforming TabPFN 2.5 on 29/35 datasets and AutoGluon on 27/35, with mean multiplicative data-efficiency gains of 1.75x and 4.44x, respectively. More broadly, our results indicate that principled synthetic data curation can convert procedural generators into domain-relevant "data engines," enabling foundation models to improve in data-sparse scientific and industrial domains where real data collection is the primary bottleneck.

</details>

---

### 13. [Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery](https://arxiv.org/abs/2603.04735)

**基本信息**

- 🔗 arXiv: [`2603.04735`](https://arxiv.org/abs/2603.04735)
- 👥 作者: Michael P. Brenner, Vincent Cohen-Addad, David Woodruff
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04735.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用LLM-based的智能体系统解决理论物理中的开放问题，这代表了AI for Science的前沿。该方法论与构建用于化学发现和推理的“化学大模型”或智能体的目标高度一致，展示了相关技术的应用前景。

**📖 中文摘要**

本文展示了人工智能可以通过自主解决理论物理学中的一个开放问题来加速数学发现。作者提出了一个神经符号系统，该系统将Gemini Deep Think大型语言模型与系统化的树搜索（TS）框架和自动化的数值反馈相结合，成功推导出了宇宙弦发射的引力辐射功率谱的新颖、精确的解析解。具体来说，该智能体评估了任意环几何的核心积分 I(N, α)。这项工作与“化学大模型”主题相关，因为它是一个AI辅助科学发现的典型案例。论文中描述的将LLM与符号推理、搜索框架和数值验证相结合的方法论，完全可以迁移到化学信息学领域，用于解决复杂的化学问题，例如推导反应机理、发现新的解析关系或优化分子设计。它展示了“化学大模型”作为科学发现助手的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper demonstrates that artificial intelligence can accelerate mathematical discovery by autonomously solving an open problem in theoretical physics. We present a neuro-symbolic system, combining the Gemini Deep Think large language model with a systematic Tree Search (TS) framework and automated numerical feedback, that successfully derived novel, exact analytical solutions for the power spectrum of gravitational radiation emitted by cosmic strings. Specifically, the agent evaluated the core integral $I(N,\alpha)$ for arbitrary loop geometries, directly improving upon recent AI-assisted attempts \cite{BCE+25} that only yielded partial asymptotic solutions. To substantiate our methodological claims regarding AI-accelerated discovery and to ensure transparency, we detail system prompts, search constraints, and intermittent feedback loops that guided the model. The agent identified a suite of 6 different analytical methods, the most elegant of which expands the kernel in Gegenbauer polynomials $C_l^{(3/2)}$ to naturally absorb the integrand's singularities. The methods lead to an asymptotic result for $I(N,\alpha)$ at large $N$ that both agrees with numerical results and also connects to the continuous Feynman parameterization of Quantum Field Theory. We detail both the algorithmic methodology that enabled this discovery and the resulting mathematical derivations.

</details>

---

### 14. [Distribution-Conditioned Transport](https://arxiv.org/abs/2603.04736)

**基本信息**

- 🔗 arXiv: [`2603.04736`](https://arxiv.org/abs/2603.04736)
- 👥 作者: Nic Fishman, Gokul Gowri, Paolo L. B. Fischer 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04736.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文提出的DCT框架用于学习条件于分布嵌入的传输模型，这直接适用于质谱数据的跨条件映射和转换问题（质谱结构推理），也为构建适应性强的大模型提供了技术。2) 数据资源相关：DCT框架本身是一个可用于科学数据（包括化学和质谱数据）分析的工具。

**📖 中文摘要**

本文介绍了分布条件传输（DCT），一个将传输映射条件于源分布和目标分布的学得嵌入的框架，从而能够泛化到训练期间未见过的分布对。DCT还允许对分布预测问题进行半监督学习。DCT与底层传输机制无关，支持从流匹配到基于分布散度的模型（例如Wasserstein, MMD）等多种模型。作者在生物学中的四个应用上展示了DCT的实际性能优势：单细胞基因组学中的批次效应转移、从质谱流式数据中预测扰动、学习造血过程中的克隆转录动力学，以及建模T细胞受体序列进化。这项工作与“质谱结构推理”和“化学大模型”都相关。在质谱分析中，经常需要将一种实验条件下的谱图“转换”或“映射”到另一种条件下（如不同仪器、不同碎片能量），DCT框架为此类问题提供了通用的建模工具。同时，DCT作为一种能够处理分布级条件并实现跨分布泛化的生成模型框架，对于构建能够适应不同数据分布（如不同化合物库、不同实验协议）的“化学大模型”具有重要价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning a transport model that maps a source distribution to a target distribution is a canonical problem in machine learning, but scientific applications increasingly require models that can generalize to source and target distributions unseen during training. We introduce distribution-conditioned transport (DCT), a framework that conditions transport maps on learned embeddings of source and target distributions, enabling generalization to unseen distribution pairs. DCT also allows semi-supervised learning for distributional forecasting problems: because it learns from arbitrary distribution pairs, it can leverage distributions observed at only one condition to improve transport prediction. DCT is agnostic to the underlying transport mechanism, supporting models ranging from flow matching to distributional divergence-based models (e.g. Wasserstein, MMD). We demonstrate the practical performance benefits of DCT on synthetic benchmarks and four applications in biology: batch effect transfer in single-cell genomics, perturbation prediction from mass cytometry data, learning clonal transcriptional dynamics in hematopoiesis, and modeling T-cell receptor sequence evolution.

</details>

---

### 15. [DARE: Aligning LLM Agents with the R Statistical Ecosystem via Distribution-Aware Retrieval](https://arxiv.org/abs/2603.04743)

**基本信息**

- 🔗 arXiv: [`2603.04743`](https://arxiv.org/abs/2603.04743)
- 👥 作者: Maojun Sun, Yue Wu, Yifei Xie 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04743.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文研究如何为科学计算（R）构建LLM代理，这直接关联到为化学信息学构建领域专用大模型或智能体的努力。2) 数据资源相关：论文贡献了RPKB知识库和DARE检索模型，这些资源和方法可用于增强化学领域LLM的工具使用能力。

**📖 中文摘要**

本文提出DARE（分布感知检索嵌入），一个轻量级、即插即用的检索模型，它将数据分布信息整合到函数表示中，用于R包检索。主要贡献包括：(i) RPKB，一个从8,191个高质量CRAN包中提取的精选R包知识库；(ii) DARE，一个融合分布特征与函数元数据的嵌入模型，以提高检索相关性；(iii) RCodingAgent，一个面向R的LLM代理，用于可靠的R代码生成，以及一套用于系统评估LLM代理在现实分析场景中的统计分析任务。这项工作与“化学大模型”主题相关，因为它专注于为成熟的科学计算生态系统（R统计生态系统）构建LLM代理和检索增强工具。化学信息学和质谱分析严重依赖R/Bioconductor等生态系统进行数据分析。论文中解决的工具检索、代码生成和领域适应等挑战，正是构建能够熟练使用化学数据分析工具和库的“化学大模型”或智能体所必须克服的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Model (LLM) agents can automate data-science workflows, but many rigorous statistical methods implemented in R remain underused because LLMs struggle with statistical knowledge and tool retrieval. Existing retrieval-augmented approaches focus on function-level semantics and ignore data distribution, producing suboptimal matches. We propose DARE (Distribution-Aware Retrieval Embedding), a lightweight, plug-and-play retrieval model that incorporates data distribution information into function representations for R package retrieval. Our main contributions are: (i) RPKB, a curated R Package Knowledge Base derived from 8,191 high-quality CRAN packages; (ii) DARE, an embedding model that fuses distributional features with function metadata to improve retrieval relevance; and (iii) RCodingAgent, an R-oriented LLM agent for reliable R code generation and a suite of statistical analysis tasks for systematically evaluating LLM agents in realistic analytical scenarios. Empirically, DARE achieves an NDCG at 10 of 93.47%, outperforming state-of-the-art open-source embedding models by up to 17% on package retrieval while using substantially fewer parameters. Integrating DARE into RCodingAgent yields significant gains on downstream analysis tasks. This work helps narrow the gap between LLM automation and the mature R statistical ecosystem.

</details>

---

### 16. [MOOSEnger -- a Domain-Specific AI Agent for the MOOSE Ecosystem](https://arxiv.org/abs/2603.04756)

**基本信息**

- 🔗 arXiv: [`2603.04756`](https://arxiv.org/abs/2603.04756)
- 👥 作者: Mengnan Li, Jason Miller, Zachary Prince 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04756.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为一个科学计算框架（MOOSE）构建领域专用的AI代理，该框架常用于包含化学过程的模拟。这为“化学大模型”在自动化科学计算工作流（如计算化学设置）中的应用提供了一个具体的技术范例和设计模式。

**📖 中文摘要**

本文介绍了MOOSEnger，一个为多物理场面向对象模拟环境（MOOSE）定制的工具赋能AI代理。MOOSE案例在HIT ".i"输入文件中指定；庞大的对象目录和严格的语法使得初始设置和调试速度缓慢。MOOSEnger提供了一个对话式工作流，通过结合对精选文档/示例的检索增强生成与确定性的、MOOSE感知的解析、验证和执行工具，将自然语言意图转化为可运行的输入。这项工作与“化学大模型”主题相关，因为它展示了一个在特定科学计算领域（计算物理/化学）构建高度专业化AI代理的案例。MOOSE广泛应用于核工程、地球化学等多物理场模拟，其中许多涉及化学反应和输运。MOOSEnger将LLM与领域特定工具和验证相结合的模式，为在化学模拟领域（如量子化学计算、分子动力学模拟的输入生成）构建类似的“化学大模型”或智能体提供了宝贵的蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MOOSEnger is a tool-enabled AI agent tailored to the Multiphysics Object-Oriented Simulation Environment (MOOSE). MOOSE cases are specified in HIT ".i" input files; the large object catalog and strict syntax make initial setup and debugging slow. MOOSEnger offers a conversational workflow that turns natural-language intent into runnable inputs by combining retrieval-augmented generation over curated docs/examples with deterministic, MOOSE-aware parsing, validation, and execution tools. A core-plus-domain architecture separates reusable agent infrastructure (configuration, registries, tool dispatch, retrieval services, persistence, and evaluation) from a MOOSE plugin that adds HIT-based parsing, syntax-preserving ingestion of input files, and domain-specific utilities for input repair and checking. An input precheck pipeline removes hidden formatting artifacts, fixes malformed HIT structure with a bounded grammar-constrained loop, and resolves invalid object types via similarity search over an application syntax registry. Inputs are then validated and optionally smoke-tested with the MOOSE runtime in the loop via an MCP-backed execution backend (with local fallback), translating solver diagnostics into iterative verify-and-correct updates. Built-in evaluation reports RAG metrics (faithfulness, relevancy, context precision/recall) and end-to-end success by actual execution. On a 125-prompt benchmark spanning diffusion, transient heat conduction, solid mechanics, porous flow, and incompressible Navier--Stokes, MOOSEnger achieves a 0.93 execution pass rate versus 0.08 for an LLM-only baseline.

</details>

---

### 17. [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827)

**基本信息**

- 🔗 arXiv: [`2603.04827`](https://arxiv.org/abs/2603.04827)
- 👥 作者: Ben S. Southworth, Jonas A. Actor, Graham Harper 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕Kolmogorov-Arnold网络（KANs）展开，这是一种新型的神经网络架构，属于“化学大模型”主题下探索新型模型架构的研究范畴。

**📖 中文摘要**

本文研究了Kolmogorov-Arnold网络（KANs）的多级训练方法。KANs是一种具有明确结构（通过指定基函数展开学习到的激活函数）的神经网络架构，与传统的多层感知机（MLP）相比，其结构更利于算法加速。作者首先建立了使用样条基函数的KANs与具有幂ReLU激活函数的多通道MLPs之间的等价性。基于此，他们提出了一种多级训练策略：通过均匀细化样条节点定义一系列KANs，并利用解析几何插值算子在不同层级的模型之间进行转换。这种“正确嵌套的层次结构”确保了将粗粒度模型的进展保留到细粒度模型中，同时样条基函数的紧支撑特性保证了在后续层级上的互补优化。数值实验表明，该方法在训练可比较的KANs或MLPs时，相比传统方法可以获得数量级上的精度提升，特别是在物理信息神经网络（PINNs）中。这项工作展示了神经网络的有原则设计如何带来可利用的结构，从而实现能显著提升训练性能的多级算法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

</details>

---

### 18. [From Unfamiliar to Familiar: Detecting Pre-training Data via Gradient Deviations in Large Language Models](https://arxiv.org/abs/2603.04828)

**基本信息**

- 🔗 arXiv: [`2603.04828`](https://arxiv.org/abs/2603.04828)
- 👥 作者: Ruiqi Zhang, Lingxiang Wang, Hainan Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04828.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大型语言模型（LLMs）的预训练数据检测，LLMs是“化学大模型”主题下的核心模型类型之一，该研究直接关联到模型训练数据的溯源和管理。

**📖 中文摘要**

本文提出了一种名为GDS的新方法，用于检测大型语言模型（LLMs）的预训练数据，以解决版权问题和缓解基准污染。现有方法主要依赖于基于似然的统计特征或微调前后的启发式信号，但前者易受语料库词频偏差影响，后者则强烈依赖于微调数据的相似性。作者从优化角度观察到，在训练过程中，样本从“不熟悉”到“熟悉”的转变反映在梯度行为的系统性差异上。基于此洞察，GDS方法通过探测目标样本的梯度偏差分数来识别预训练数据。具体而言，该方法首先使用梯度剖面（捕捉FFN和Attention模块中参数更新的幅度、位置和集中度）来表示每个样本，揭示了成员数据与非成员数据之间的一致区别。然后将这些特征输入一个轻量级分类器进行二元成员推断。在五个公共数据集上的实验表明，GDS实现了最先进的性能，并且与强基线相比，跨数据集的可迁移性显著提高。可解释性分析进一步展示了梯度特征分布的差异，使得实用且可扩展的预训练数据检测成为可能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pre-training data detection for LLMs is essential for addressing copyright concerns and mitigating benchmark contamination. Existing methods mainly focus on the likelihood-based statistical features or heuristic signals before and after fine-tuning, but the former are susceptible to word frequency bias in corpora, and the latter strongly depend on the similarity of fine-tuning data. From an optimization perspective, we observe that during training, samples transition from unfamiliar to familiar in a manner reflected by systematic differences in gradient behavior. Familiar samples exhibit smaller update magnitudes, distinct update locations in model components, and more sharply activated neurons. Based on this insight, we propose GDS, a method that identifies pre-training data by probing Gradient Deviation Scores of target samples. Specifically, we first represent each sample using gradient profiles that capture the magnitude, location, and concentration of parameter updates across FFN and Attention modules, revealing consistent distinctions between member and non-member data. These features are then fed into a lightweight classifier to perform binary membership inference. Experiments on five public datasets show that GDS achieves state-of-the-art performance with significantly improved cross-dataset transferability over strong baselines. Further interpretability analyse show gradient feature distribution differences, enabling practical and scalable pre-training data detection.

</details>

---

### 19. [Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models](https://arxiv.org/abs/2603.04893)

**基本信息**

- 🔗 arXiv: [`2603.04893`](https://arxiv.org/abs/2603.04893)
- 👥 作者: Sean Lamont, Christian Walder, Paul Montague 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04893.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散语言模型（Diffusion Language Models）展开，这是一种生成式大语言模型，属于“化学大模型”主题下模型生成与优化技术的研究范畴。

**📖 中文摘要**

本文针对文本生成（如代码生成和数学问题求解）中的多样性输出需求，研究了扩散语言模型的采样策略。传统采样方法在计算资源上浪费于重复的失败模式，而扩散语言模型的独立样本也经常坍缩到相似的模式。为此，作者提出了一种无需训练、低成本的干预措施来增强扩散语言模型在生成时的多样性。该方法对批次中的中间样本进行顺序修改，使每个样本在特征空间中都远离先前样本的特征空间，从而主动惩罚冗余。与需要重新训练或波束搜索的先前方法不同，该策略产生的计算开销可以忽略不计，同时确保批次中的每个样本都贡献独特的视角。作者在HumanEval和GSM8K基准上使用LLaDA-8B-Instruct模型评估了该方法。结果表明，在各种温度设置下，该方法显著提高了多样性和Pass@k性能。作为一种对采样过程的简单修改，该方法为当前和未来的扩散语言模型在需要多样化解决方案搜索的任务中提供了一种即时、低成本的改进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diverse outputs in text generation are necessary for effective exploration in complex reasoning tasks, such as code generation and mathematical problem solving. Such Pass@$k$ problems benefit from distinct candidates covering the solution space. However, traditional sampling approaches often waste computational resources on repetitive failure modes. While Diffusion Language Models have emerged as a competitive alternative to the prevailing Autoregressive paradigm, they remain susceptible to this redundancy, with independent samples frequently collapsing into similar modes. To address this, we propose a training free, low cost intervention to enhance generative diversity in Diffusion Language Models. Our approach modifies intermediate samples in a batch sequentially, where each sample is repelled from the feature space of previous samples, actively penalising redundancy. Unlike prior methods that require retraining or beam search, our strategy incurs negligible computational overhead, while ensuring that each sample contributes a unique perspective to the batch. We evaluate our method on the HumanEval and GSM8K benchmarks using the LLaDA-8B-Instruct model. Our results demonstrate significantly improved diversity and Pass@$k$ performance across various temperature settings. As a simple modification to the sampling process, our method offers an immediate, low-cost improvement for current and future Diffusion Language Models in tasks that benefit from diverse solution search. We make our code available at this https URL .

</details>

---

### 20. [$\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](https://arxiv.org/abs/2603.04948)

**基本信息**

- 🔗 arXiv: [`2603.04948`](https://arxiv.org/abs/2603.04948)
- 👥 作者: Peihao Wang, Ruisi Cai, Zhen Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04948.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大型语言模型（LLMs）的推理能力优化，提出了一种新的推理时优化框架，直接关联“化学大模型”主题下的模型推理与优化技术。

**📖 中文摘要**

本文提出$\nabla$-Reasoner，一种迭代生成框架，将基于令牌逻辑的可微分优化集成到解码循环中，以在线优化策略。其核心组件“可微分文本优化”（DTO）利用来自LLM似然和奖励模型的梯度信号来优化文本表示。$\nabla$-Reasoner进一步结合了拒绝采样和加速设计，以使解码更鲁棒和快速。理论上，作者证明了在样本空间执行推理时梯度下降以最大化奖励，等同于通过KL正则化强化学习来对齐LLM策略。实证上，$\nabla$-Reasoner在一个具有挑战性的数学推理基准上实现了超过20%的准确率提升，同时与强基线相比，模型调用次数减少了约10-40%。总体而言，这项工作引入了从零阶搜索到一阶优化的范式转变，为增强LLM推理提供了一条经济有效的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

</details>

---

### 21. [Programmable superconducting neuron with intrinsic in-memory computation and dual-timescale plasticity for ultra-efficient neuromorphic computing](https://arxiv.org/abs/2603.04966)

**基本信息**

- 🔗 arXiv: [`2603.04966`](https://arxiv.org/abs/2603.04966)
- 👥 作者: Muen Wang, Shucheng Yang, Yuxiang Lin 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04966.pdf)

**💡 相关性分析**

满足标准1：论文提出的可编程超导神经元架构，集成本征内存和可塑性，其设计理念和高效处理时空信号的能力，与构建用于“质谱结构推理”等任务的专用、高效化学信息学模型的核心主题在方法论上相关。

**📖 中文摘要**

本文介绍了一种可编程的超导神经元，用于超高效神经形态计算。该神经元集成了本征内存计算和双时间尺度可塑性。虽然论文的核心是硬件设计和神经形态计算，但其提出的“本征内存计算”概念和用于处理时空信号的架构，与化学信息学中处理复杂序列数据（如质谱时间序列或分子结构序列）的模型有潜在关联。该工作展示了如何将计算、内存和可塑性融合到单个单元中，为设计用于处理化学和质谱数据的专用高效计算架构提供了灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The escalating energy demands of artificial intelligence pose a critical challenge to conventional computing. Leveraging the efficiency of event-driven, in-memory neuromorphic architectures into the superconducting circuits with ultra-high speed and low power dissipation advantages offers a promising solution to energy-efficient computing. However, the potential of such a solution has yet to be realized, owning to the absence of a fundamental superconducting unit that unifies programmability, local memory, and multi-timescale plasticity. Here, we introduce a programmable Josephson-junction-based leaky integrate-and-fire (LIF) neuron that features intrinsic static memory and precise programmability by encoding somatic and synaptic parameters directly in the bias current. This neuron is also capable of dual-timescale plasticity: picosecond-scale short-term modulation of spike transmission and long-term weight retention exceeding 10,000 seconds, facilitating both rapid temporal adaptation and robust weight storage. It can operate up to 45 GHz with femtojoule-level energy dissipation per spike, and supports 10 somatic threshold levels and 20 synaptic states. Furthermore, we demonstrate a crossbar-based spiking neural network (SNN) utilizing this neuron, which achieves outstanding performance across multiple tasks. By fusing computation, memory and plasticity into a single superconducting unit, our work paves the way for the next generation of ultrafast, energy-efficient neuromorphic computing.

</details>

---

### 22. [When Weak LLMs Speak with Confidence, Preference Alignment Gets Stronger](https://arxiv.org/abs/2603.04968)

**基本信息**

- 🔗 arXiv: [`2603.04968`](https://arxiv.org/abs/2603.04968)
- 👥 作者: Amirabbas Afzali, Myeongho Jeon, Maria Brbic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04968.pdf)

**💡 相关性分析**

满足标准1：论文研究的“利用弱模型置信度进行样本选择和模型优化”是机器学习，特别是大模型训练中的核心方法学。这种方法可以直接应用于“化学大模型”的训练、微调或“质谱结构推理”模型的优化中，属于核心方法论的相关扩展。

**📖 中文摘要**

本文探讨了在大型语言模型（LLM）与人类价值观对齐（偏好对齐）任务中，使用弱LLM作为标注者的有效性。作者发现，仅选择弱LLM高置信度的样本子集进行训练，其效果甚至优于使用全部人工标注数据。基于此，他们提出了置信度加权的偏好优化（CW-PO）通用框架。这项工作属于大模型对齐和优化领域。虽然不直接针对化学或质谱，但其核心思想——利用模型自身的不确定性或置信度来指导数据选择和模型优化——可以迁移到化学大模型和质谱分析任务中。例如，在质谱结构推理中，可以借鉴类似思想，利用模型对预测结构的置信度来筛选训练数据或改进推理过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Preference alignment is an essential step in adapting large language models (LLMs) to human values, but existing approaches typically depend on costly human annotations or large-scale API-based models. We explore whether a weak LLM can instead act as an effective annotator. We surprisingly find that selecting only a subset of a weak LLM's highly confident samples leads to substantially better performance than using full human annotations. Building on this insight, we propose Confidence-Weighted Preference Optimization (CW-PO), a general framework that re-weights training samples by a weak LLM's confidence and can be applied across different preference optimization objectives. Notably, the model aligned by CW-PO with just 20% of human annotations outperforms the model trained with 100% of annotations under standard DPO. These results suggest that weak LLMs, when paired with confidence weighting, can dramatically reduce the cost of preference alignment while even outperforming methods trained on fully human-labeled data.

</details>

---

### 23. [Functionality-Oriented LLM Merging on the Fisher--Rao Manifold](https://arxiv.org/abs/2603.04972)

**基本信息**

- 🔗 arXiv: [`2603.04972`](https://arxiv.org/abs/2603.04972)
- 👥 作者: Jiayu Wang, Zuojun Ye, Wenpeng Yin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04972.pdf)

**💡 相关性分析**

满足标准1：论文专注于大模型权重空间的合并与功能融合，这是构建多功能、通用型“化学大模型”的关键技术之一。其提出的稳定合并算法直接关系到如何整合不同化学子领域的专家模型，与核心主题高度相关。

**📖 中文摘要**

本文提出了一种在Fisher-Rao流形上合并多个微调后的大型语言模型（LLM）权重的算法，旨在融合不同任务的功能。该方法将模型合并表述为计算加权Karcher均值，以最小化预测分布之间的KL散度距离。论文解决了传统欧几里得空间合并方法在模型异构性高时导致的表示崩溃问题。这项工作属于大模型高效适配与融合的前沿领域。其提出的基于流形几何的模型功能融合框架，为构建能够同时处理多种化学信息学任务（如性质预测、反应预测、质谱解析）的“化学大模型”提供了重要的技术思路和理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective. We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

</details>

---

### 24. [VRM: Teaching Reward Models to Understand Authentic Human Preferences](https://arxiv.org/abs/2603.04974)

**基本信息**

- 🔗 arXiv: [`2603.04974`](https://arxiv.org/abs/2603.04974)
- 👥 作者: Biao Liu, Ning Xu, Junming Yang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04974.pdf)

**💡 相关性分析**

满足标准1：论文研究的“变分奖励建模”是优化和对齐大模型行为的关键技术。训练一个用于化学研究或质谱分析的可靠AI助手（化学大模型），必然涉及与专家知识对齐，因此该工作的方法与核心主题直接相关。

**📖 中文摘要**

本文针对大型语言模型对齐中奖励模型容易陷入奖励黑客（reward hacking）的问题，提出了变分奖励建模（VRM）框架。VRM通过变分推断技术，显式地对人类偏好判断过程中的高维目标权重和低维语义特征等潜变量进行建模，以更真实地捕捉人类偏好。论文提供了理论分析，表明VRM相比传统奖励模型能获得更紧的泛化误差界。这项工作属于大模型对齐与强化学习领域。其核心贡献——设计更鲁棒、更能理解真实人类意图的奖励模型——对于训练用于化学发现或质谱解析的AI助手（即特定领域的“化学大模型”）至关重要，因为这类模型也需要与化学家的专业判断和偏好进行对齐。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have achieved remarkable success across diverse natural language tasks, yet the reward models employed for aligning LLMs often encounter challenges of reward hacking, where the approaches predominantly rely on directly mapping prompt-response pairs to scalar scores, which may inadvertently capture spurious correlations rather than authentic human preferences. In contrast, human evaluation employs a sophisticated process that initially weighs the relative importance of multiple high-dimensional objectives according to the prompt context, subsequently evaluating response quality through low-dimensional semantic features such as logical coherence and contextual appropriateness. Motivated by this consideration, we propose VRM, i.e., Variational Reward Modeling, a novel framework that explicitly models the evaluation process of human preference judgments by incorporating both high-dimensional objective weights and low-dimensional semantic features as latent variables, which are inferred through variational inference techniques. Additionally, we provide a theoretical analysis showing that VRM can achieve a tighter generalization error bound compared to the traditional reward model. Extensive experiments on benchmark datasets demonstrate that VRM significantly outperforms existing methods in capturing authentic human preferences.

</details>

---

### 25. [Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination](https://arxiv.org/abs/2603.05040)

**基本信息**

- 🔗 arXiv: [`2603.05040`](https://arxiv.org/abs/2603.05040)
- 👥 作者: Hyuntae Park, Yeachan Kim, SangKeun Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05040.pdf)

**💡 相关性分析**

满足标准1：论文提出的利用多模态（视觉）信息增强语言模型推理能力的方法，为构建更强大的“化学大模型”提供了可行的技术路径。化学和质谱分析本质上是多模态的（结构式、光谱图、文本描述），因此该工作与核心主题在方法论上高度相关。

**📖 中文摘要**

本文针对预训练语言模型（PLM）在零样本常识推理中因文本知识存在的人类报告偏差而受限的问题，提出了Imagine框架。该框架通过集成机器生成的图像所提供的视觉信号，来补充文本输入，从而增强PLM的推理能力。具体而言，它在推理流程中直接嵌入了一个图像生成器，使模型具备“想象”能力，并构建了合成数据集来模拟视觉问答场景。实验表明，该方法显著提升了零样本常识推理的性能。这项工作属于多模态推理与常识理解领域。其核心思想——利用跨模态信息（视觉）来弥补单一模态（文本）的偏差和不足——对于“化学大模型”和“质谱结构推理”具有重要启示。例如，在解析质谱时，可以结合分子结构图像或化学空间的可视化信息来辅助推理；或者利用多模态信息来增强化学大模型对分子性质、反应等的理解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

</details>

---

### 26. [WebFactory: Automated Compression of Foundational Language Intelligence into Grounded Web Agents](https://arxiv.org/abs/2603.05044)

**基本信息**

- 🔗 arXiv: [`2603.05044`](https://arxiv.org/abs/2603.05044)
- 👥 作者: Sicheng Fan, Qingyun Shi, Shengze Xu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05044.pdf)

**💡 相关性分析**

满足标准1：论文提出的“将LLM知识压缩为可行动作”的智能体训练框架，为开发能够进行主动化学研究（如自动化实验、结构解析）的“化学大模型”或智能体提供了重要的架构参考和方法论启示，与核心主题直接相关。

**📖 中文摘要**

本文介绍了WebFactory，一个用于训练GUI智能体的全自动闭环强化学习管道。该管道系统地将在大型语言模型中编码的互联网知识压缩为高效、 grounded 的行动。其核心是通过可扩展的环境合成、知识感知的任务生成、LLM驱动的轨迹收集、分解奖励的RL训练和系统化的智能体评估，将被动互联网知识转化为主动的、 grounded 的智能体。论文强调了其方法在数据效率和泛化能力上的优势。这项工作属于具身AI和智能体研究领域。虽然主要针对网页交互，但其提出的“将LLM的潜在知识压缩为可行动作”的框架，与如何让“化学大模型”不仅理解化学知识，还能执行具体的实验设计、数据分析或仪器控制等任务（即成为化学研究智能体）的研究目标高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current paradigms for training GUI agents are fundamentally limited by a reliance on either unsafe, non-reproducible live web interactions or costly, scarce human-crafted data and environments. We argue this focus on data volume overlooks a more critical factor: the efficiency of compressing a large language model's (LLM) latent knowledge into actionable agent behavior. We introduce WebFactory, a novel, fully automated closed-loop reinforcement learning pipeline for GUI agents, systematically compressing LLM-encoded internet intelligence into efficient, grounded actions. Our pipeline features a process of scalable environment synthesis, knowledge-aware task generation, LLM-powered trajectory collection, decomposed reward RL training, and systematic agent evaluation. Remarkably, our agent demonstrates exceptional data efficiency and generalization. Trained on synthetic data from only 10 websites within WebFactory, it achieves performance comparable to GUI agents trained on the same amount of human-annotated data from a much larger set of environments. This superior performance is consistent across our internal offline and online transfer benchmarks, where our agent also significantly outperforms the base foundation model. We further provide critical insights into the "embodiment potential" of different LLM foundations, offering a new axis for model evaluation. This work presents a scalable and cost-effective paradigm for transforming passive internet knowledge into active, grounded intelligence, marking a critical step towards general-purpose interactive agents.

</details>

---

### 27. [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046)

**基本信息**

- 🔗 arXiv: [`2603.05046`](https://arxiv.org/abs/2603.05046)
- 👥 作者: Rongzhi Li, Hitomi Yanaka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05046.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于神经元分析的MoE专家分配方法，是一种先进的模型架构优化技术。构建能够处理化学多任务、多数据模态的“化学大模型”，MoE是关键技术之一，因此该工作与核心主题在模型架构层面相关。

**📖 中文摘要**

本文针对将大语言模型扩展到低资源语言时的高成本问题，提出了NeuronMoE方法。该方法通过分析所有Transformer组件中语言特定的神经元，根据经验测量的跨语言神经元多样性来指导每个层的专家分配，从而在混合专家架构中实现更高效的参数利用。应用于Llama-3.2-3B模型在希腊语、土耳其语和匈牙利语上的实验表明，该方法在匹配基线性能的同时，平均减少了约40%的参数。这项工作属于多语言大模型的高效扩展领域。其核心创新——基于神经元级分析来指导MoE架构的专家分配——是一种精细化的模型架构设计方法。这种方法论可以迁移到化学领域，例如，为处理不同分子表示（SMILES, SELFIES, 图）、不同光谱类型（质谱、核磁共振）或不同化学子任务（合成规划、性质预测）设计专用的、参数高效的“化学大模型”MoE架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We propose $\textbf{NeuronMoE}$, a method that analyzes language-specific neurons across all transformer components to guide expert allocation per layer based on empirically measured cross-lingual neuron diversity. Applied to Llama-3.2-3B for low-resource languages (Greek, Turkish, and Hungarian), this approach achieves approximately 40% average parameter reduction while matching the performance of the LayerMoE baseline. We find that low-resource language experts independently develop neuron specialization patterns mirroring the high-resource language, which are concentrated in early and late layers. This reveals potential universal architectural principles in how multilingual models organize linguistic knowledge.

</details>

---

### 28. [Cyber Threat Intelligence for Artificial Intelligence Systems](https://arxiv.org/abs/2603.05068)

**基本信息**

- 🔗 arXiv: [`2603.05068`](https://arxiv.org/abs/2603.05068)
- 👥 作者: Natalia Krawczyk, Mateusz Szczepkowski, Adrian Brodzik 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05068.pdf)

**💡 相关性分析**

满足标准1：论文系统性地研究了AI系统（包括大模型）的安全威胁与防御，这是任何领域（包括化学信息学）在部署关键AI应用时必须考虑的核心问题。确保“化学大模型”和“质谱结构推理”系统的安全性与鲁棒性，是该主题不可或缺的一部分。

**📖 中文摘要**

本文探讨了随着人工智能系统深度嵌入关键服务和日常产品，其面临传统网络防御无法处理的安全威胁。论文研究了网络威胁情报（CTI）应如何演进以应对针对AI系统的攻击。作者分析了传统威胁情报的假设和工作流程与AI防御需求之间的差距，回顾并组织了当前AI安全知识体系，并概述了面向AI的威胁情报知识库应包含的内容，描述了针对AI供应链不同阶段和产物的具体入侵指标。这项工作属于AI安全与治理领域。随着“化学大模型”和基于AI的“质谱结构推理”系统在药物研发、材料科学等关键领域部署，其安全性、对抗鲁棒性和可信赖性变得至关重要。该论文系统性地梳理了AI系统面临的威胁和防御思路，为保障化学AI模型的安全可靠运行提供了重要的背景知识和框架参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) becomes deeply embedded in critical services and everyday products, it is increasingly exposed to security threats which traditional cyber defenses were not designed to handle. In this paper, we investigate how cyber threat intelligence (CTI) may evolve to address attacks that target AI systems. We first analyze the assumptions and workflows of conventional threat intelligence with the needs of AI-focused defense, highlighting AI-specific assets and vulnerabilities. We then review and organize the current landscape of AI security knowledge. Based on this, we outline what an AI-oriented threat intelligence knowledge base should contain, describing concrete indicators of compromise (IoC) for different AI supply-chain phases and artifacts, and showing how such a knowledge base could support security tools. Finally, we discuss techniques for measuring similarity between collected indicators and newly observed AI artifacts. The review reveals gaps and quality issues in existing resources and identifies potential future research directions toward a practical threat intelligence framework tailored to AI.

</details>

---

### 29. [TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling](https://arxiv.org/abs/2603.05094)

**基本信息**

- 🔗 arXiv: [`2603.05094`](https://arxiv.org/abs/2603.05094)
- 👥 作者: Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05094.pdf)

**💡 相关性分析**

满足标准2：论文详细描述了一个针对特定领域（方言音频）的高质量指令数据集的构建流程、验证方法和应用效果。这为构建用于“化学大模型”和“质谱结构推理”的领域专用指令数据集提供了宝贵的实践指南和工具思路，符合“数据资源相关”标准。

**📖 中文摘要**

本文介绍了TW-Sound580K，一个通过验证-生成-评判协议构建的台湾地区音频-文本指令数据集，旨在解决大型音频-语言模型在处理地方方言韵律时数据稀缺的问题。该数据集通过双ASR验证过滤原始音频，并利用教师模型扩展为高质量的指令对。基于此数据集训练的Tai-LALM模型，结合动态双ASR仲裁策略，在当地方言语音理解基准上取得了显著提升。这项工作属于语音处理和领域自适应的大语言模型研究。其核心贡献——针对特定领域（方言）构建高质量、指令形式的数据集并用于微调大模型——为化学和质谱领域提供了直接范例。要构建专业的“化学大模型”或“质谱结构推理”模型，同样需要高质量、任务特定的指令微调数据集。该论文的数据集构建协议和模型适配方法具有很高的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio-Language Models (LALMs) typically struggle with localized dialectal prosody due to the scarcity of specialized corpora. We present TW-Sound580K, a Taiwanese audio-text instruction dataset developed through a Verify-Generate-Critique (VGC) protocol. This pipeline leverages Dual-ASR validation to filter 522K raw clips, subsequently expanding them into 580,000 high-fidelity instruction pairs using a teacher model. The dataset's utility is demonstrated through Tai-LALM, which fine-tunes a DeSTA 2.5-Audio-initialized backbone and incorporates a dynamic Dual-ASR Arbitration strategy to optimize transcription selection during inference. On the TAU Benchmark, Tai-LALM reaches 49.1% accuracy, marking a 6.5% absolute improvement over the zero-shot baseline (42.6% with ASR text conditioning). This confirms that integrating regional corpora with rigorous curation and dynamic arbitration significantly enhances LALM performance on localized speech.

</details>

---

### 30. [Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning](https://arxiv.org/abs/2603.05120)

**基本信息**

- 🔗 arXiv: [`2603.05120`](https://arxiv.org/abs/2603.05120)
- 👥 作者: Boren Hu, Xiao Liu, Boci Peng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05120.pdf)

**💡 相关性分析**

满足标准1：论文提出的“双向课程生成”是一种高效训练大模型（特别是数据稀缺领域）的核心方法学。该方法可以直接应用于优化“化学大模型”或“质谱结构推理”模型的训练过程，提高其数据利用效率和最终性能，与核心主题高度相关。

**📖 中文摘要**

本文针对大语言模型数学推理训练需要海量数据、数据效率低下的瓶颈，提出了一种新颖的双向课程生成框架。该框架采用多智能体生态系统，模拟自适应教学法，形成一个闭环反馈。它能动态生成数据，既可以增加问题复杂度来挑战模型，也可以在模型出现特定推理失败时简化问题以进行修复。这种方法确保了模型在任何阶段都只消费最有效的数据。实验表明，该方法在显著减少指令样本数量的同时，实现了更优的推理性能。这项工作属于大语言模型的高效训练与课程学习领域。其核心思想——通过动态、双向的数据生成和选择来最大化每个训练样本的教学价值——对于在数据可能相对稀缺的化学和质谱领域训练“化学大模型”具有非常重要的意义。可以借鉴此框架来生成或筛选用于训练质谱结构推理或化学性质预测模型的渐进式学习数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enhancing mathematical reasoning in Large Language Models typically demands massive datasets, yet data efficiency remains a critical bottleneck. While Curriculum Learning attempts to structure this process, standard unidirectional approaches (simple-to-complex) suffer from inefficient sample utilization: they blindly escalate complexity even when foundational gaps persist, leading to wasted computation on unsolvable problems. To maximize the instructional value of every training sample, we introduce a novel Bidirectional Curriculum Generation framework. Unlike rigid trajectories, our multi-agent ecosystem mimics adaptive pedagogy to establish a closed feedback loop. It dynamically generates data by either complicating problems to challenge the model or, crucially, simplying them to repair specific reasoning failures. This mechanism ensures that the model consumes only the most effective data at any given stage. Grounded in the Optimal Pacing Theorem, our approach optimizes the learning trajectory, significantly outperforming baselines while achieving superior reasoning performance with substantially fewer instruction samples.

</details>

---

### 31. [Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs](https://arxiv.org/abs/2603.05343)

**基本信息**

- 🔗 arXiv: [`2603.05343`](https://arxiv.org/abs/2603.05343)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化用于分子模拟的等变图神经网络（一种化学大模型），旨在解决其高计算成本和内存瓶颈问题。

**📖 中文摘要**

本文提出了一种用于SO(3)-等变图神经网络（GNNs）的几何感知量化（GAQ）框架，旨在压缩和加速等变模型，同时严格保持离散空间中的连续对称性。该研究针对分子模拟，通过解耦不变长度和等变方向，并采用对称感知的训练策略，在保持几何保真度的同时，显著降低了计算成本和内存占用。这项工作直接与“化学大模型”相关，因为它专注于用于分子模拟的等变GNNs的优化和加速，这是化学信息学中构建和部署大型、高效模型的核心挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

</details>

---

### 32. [AbAffinity: A Large Language Model for Predicting Antibody Binding Affinity against SARS-CoV-2](https://arxiv.org/abs/2603.04480)

**基本信息**

- 🔗 arXiv: [`2603.04480`](https://arxiv.org/abs/2603.04480)
- 👥 作者: Faisal Bin Ashraf, Animesh Ray, Stefano Lonardi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04480.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于预测抗体结合亲和力的大型语言模型（AbAffinity），这属于化学信息学中基于AI的分子性质预测和设计范畴。

**📖 中文摘要**

本研究介绍了AbAffinity，一个用于预测抗体与SARS-CoV-2刺突蛋白等靶肽结合亲和力的大型语言模型。随着人工智能的进步和实验抗体数据（特别是与COVID-19相关的数据）的激增，基于机器学习的抗体设计成为一种有前景的方法。抗体结合亲和力是设计中和抗体的最关键属性之一。该模型旨在准确预测这一关键性质，为抗感染药物设计提供工具。这项工作展示了大型语言模型在生物分子性质预测（特别是抗体-抗原相互作用）这一化学信息学子领域的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning-based antibody design is emerging as one of the most promising approaches to combat infectious diseases, due to significant advancements in the field of artificial intelligence and an exponential surge in experimental antibody data (in particular related to COVID-19). The ability of an antibody to bind to an antigens (called binding affinity) is one of the the most critical properties in designing neutralizing antibodies. In this study we introduce Ab-Affinity, a new large language model that can accurately predict the binding affinity of antibodies against a target peptide, e.g., the SARS-CoV-2 spike protein. Code and model are available at this https URL .

</details>

---

### 33. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2603.04523)

**基本信息**

- 🔗 arXiv: [`2603.04523`](https://arxiv.org/abs/2603.04523)
- 👥 作者: Austin Rodriguez, Justin S. Smith, Sakib Matin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04523.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进机器学习原子间势（MLIPs）的训练框架，这是一种在计算化学和材料科学中广泛使用的化学大模型。

**📖 中文摘要**

本文提出了投影Hessian学习（PHL），一个用于机器学习原子间势（MLIPs）的可扩展二阶训练框架。传统的基于能量和力的训练忽略了势能面上丰富的曲率信息（Hessian矩阵）。PHL通过使用Hessian-向量积（HVPs）注入曲率信息，避免了显式构建和存储Hessian矩阵带来的二次方内存增长。该方法在包含反应物、产物、过渡态等多样化化学结构的分子数据集上进行了基准测试，结果表明PHL在保持大部分二阶精度增益的同时，显著提升了训练效率。这项工作直接改进了化学大模型（MLIPs）的训练方法，使其能够更高效、更准确地学习分子系统的势能面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hessian matrix (second derivatives) encodes far richer local curvature of the potential energy surface than energies and forces alone. However, training machine-learning interatomic potentials (MLIPs) with full Hessians is often impractical because explicitly forming and storing Hessian matrices scales quadratically in cost and memory. We introduce Projected Hessian Learning (PHL), a scalable second-order training framework that injects curvature information using only Hessian-vector products (HVPs). Rather than constructing the Hessian, PHL projects curvature along stochastic probe directions and uses an unbiased stochastic trace-based loss with favorable system-size scaling, enabling curvature-informed training without quadratic memory growth. We benchmark PHL on a chemically diverse dataset of reactants, products, transition states, intrinsic reaction coordinates, and normal-mode sampled geometries computed at omegaB97XD/6-31G(d). We compare energy-force training (E-F), two HVP-based schemes (E-F-HVP with one-hot or randomized probes), and full energy-force-Hessian training (E-F-H). With randomized probes per minibatch, both HVP schemes match full-Hessian training in energy, force, and Hessian accuracy while delivering >24x epoch speedups for the small molecular systems studied. In a fixed-probe regime with one HVP per molecule, randomized projections consistently outperform one-column probing, especially for far-from-equilibrium geometries. Overall, PHL replaces explicit Hessian supervision with force-complexity curvature training, retaining most second-order accuracy gains while scaling to larger, more complex molecular systems.

</details>

---

### 34. [The Volterra signature](https://arxiv.org/abs/2603.04525)

**基本信息**

- 🔗 arXiv: [`2603.04525`](https://arxiv.org/abs/2603.04525)
- 👥 作者: Paul P. Hager, Fabian N. Harang, Luca Pelizzari 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04525.pdf)

**💡 相关性分析**

满足标准2：论文提出的Volterra签名框架为分析复杂时间序列数据（如分子动力学轨迹、光谱/质谱序列）提供了一种新的、具有理论保证的特征表示和通用逼近工具，可用于化学信息学和质谱分析中的模式识别与推理任务。

**📖 中文摘要**

本文提出了Volterra签名（Volterra signature）作为一种用于历史依赖系统的原则性、显式特征表示。该框架整合了算法信息论和香农信息论，通过将加权输入路径展开到张量代数中，为从时间序列数据中学习提供了严格的理论保证。作者证明了其通用逼近定理，并展示了该签名对于时间重新参数化的不变性。研究通过真实和合成数据上的动态学习任务验证了其有效性。虽然论文本身是通用方法，但其处理非马尔可夫时间序列和提供可解释特征表示的能力，与化学信息学中分析复杂分子动力学轨迹、光谱序列或质谱时间序列数据的需求高度相关，为这些领域提供了新的分析工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern approaches for learning from non-Markovian time series, such as recurrent neural networks, neural controlled differential equations or transformers, typically rely on implicit memory mechanisms that can be difficult to interpret or to train over long horizons. We propose the Volterra signature $\mathrm{VSig}(x;K)$ as a principled, explicit feature representation for history-dependent systems. By developing the input path $x$ weighted by a temporal kernel $K$ into the tensor algebra, we leverage the associated Volterra--Chen identity to derive rigorous learning-theoretic guarantees. Specifically, we prove an injectivity statement (identifiability under augmentation) that leads to a universal approximation theorem on the infinite dimensional path space, which in certain cases is achieved by linear functionals of $\mathrm{VSig}(x;K)$. Moreover, we demonstrate applicability of the kernel trick by showing that the inner product associated with Volterra signatures admits a closed characterization via a two-parameter integral equation, enabling numerical methods from PDEs for computation. For a large class of exponential-type kernels, $\mathrm{VSig}(x;K)$ solves a linear state-space ODE in the tensor algebra. Combined with inherent invariance to time reparameterization, these results position the Volterra signature as a robust, computationally tractable feature map for data science. We demonstrate its efficacy in dynamic learning tasks on real and synthetic data, where it consistently improves classical path signature baselines.

</details>

---

### 35. [Estimation of Persistence Diagrams via the Three Gap Theorem](https://arxiv.org/abs/2603.04570)

**基本信息**

- 🔗 arXiv: [`2603.04570`](https://arxiv.org/abs/2603.04570)
- 👥 作者: Luis Suarez Salas, Jose A. Perea
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04570.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于三间隔定理和持久Künneth公式的快速持久性图近似计算方法，为从准周期信号（可类比质谱峰序列）中提取拓扑特征提供了新工具，可用于质谱数据的结构表征和推理。

**📖 中文摘要**

本文结合数论中的三间隔定理和拓扑数据分析（TDA）中的持久Künneth公式，提出了从准周期函数的滑动窗口嵌入中近似计算持久性图的理论和计算方案。持久性图是TDA中用于量化形状的拓扑描述符，已应用于量化周期性等。该工作为快速、可证明正确的持久同调近似提供了方案，输入是信号的频谱。虽然论文背景是动力系统，但其核心贡献——高效计算时间序列嵌入的拓扑描述符（持久性图）——与“质谱结构推理”高度相关。在质谱分析中，质谱峰可以视为一种序列或时间序列，其拓扑特征可能蕴含分子结构信息。该方法为从质谱数据中提取稳健的拓扑特征以辅助结构推理提供了新的技术途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The time delay (or Sliding Window) embedding is a technique from dynamical systems to reconstruct attractors from time series data. Recently, descriptors from Topological Data Analysis (TDA) -- specifically, persistence diagrams -- have been used to measure the shape of said reconstructed attractors in applications including periodicity and quasiperiodicity quantification. Despite their utility, the fast computation of persistence diagrams of sliding window embeddings is still poorly understood. In this work, we present theoretical and computational schemes to approximate the persistence diagrams of sliding window embeddings from quasiperiodic functions. We do so by combining the Three Gap Theorem from number theory with the Persistent Künneth formula from TDA, and derive fast and provably correct persistent homology approximations. The input to our procedure is the spectrum of the signal, and we provide numerical as well as theoretical evidence of its utility to capture the shape of toroidal attractors.

</details>

---

### 36. [Particle-Guided Diffusion for Gas-Phase Reaction Kinetics](https://arxiv.org/abs/2603.05139)

**基本信息**

- 🔗 arXiv: [`2603.05139`](https://arxiv.org/abs/2603.05139)
- 👥 作者: Andrew Millard, Henrik Pedersen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05139.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容围绕利用扩散模型（一种生成式大模型）解决化学动力学问题，与'化学大模型'主题直接相关。

**📖 中文摘要**

本文提出了一种用于气相化学反应动力学的粒子引导扩散方法。该方法将基于扩散模型的物理引导采样应用于由平流-反应-扩散方程描述的气相化学反应系统。通过在不同参数下对ARD方程的解进行训练，该方法能够生成物理一致的浓度场，并准确预测出口浓度，包括在未见过的参数值下。这项工作展示了扩散模型在反应输运系统中进行推理的潜力，属于利用生成模型（扩散模型）解决化学动力学问题的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

</details>

---

### 37. [Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks](https://arxiv.org/abs/2603.05188)

**基本信息**

- 🔗 arXiv: [`2603.05188`](https://arxiv.org/abs/2603.05188)
- 👥 作者: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05188.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是利用大型语言模型（LLM）这一特定类型的化学大模型，进行共价有机框架材料的逆设计，直接围绕'化学大模型'主题。

**📖 中文摘要**

本文介绍了一个名为Ara的大型语言模型智能体，用于对光催化共价有机框架进行逆设计，以解决其水解稳定性与活性之间的权衡问题。该智能体利用预训练的化学知识、给体-受体理论、共轭效应和连接键稳定性层次结构，指导搜索同时满足带隙、带边和水解稳定性标准的COFs。在由各种节点、连接体、连接键和R基团组成的候选空间中，Ara的命中率达到52.7%，显著优于随机搜索和贝叶斯优化。该工作展示了LLM化学先验知识如何加速多标准材料发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

</details>

---

### 38. [PhysLLM: Harnessing Large Language Models for Cross-Modal Remote Physiological Sensing](https://arxiv.org/abs/2505.03621)

**基本信息**

- 🔗 arXiv: [`2505.03621`](https://arxiv.org/abs/2505.03621)
- 👥 作者: Yiping Xie, Bo Zhao, Mingtong Dai 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03621.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是设计一个利用大型语言模型（LLM）进行跨模态生理信号处理的框架，直接围绕'化学大模型'（广义上，LLM作为基础模型在科学计算中的应用）主题。

**📖 中文摘要**

本文提出了PhysLLM，一个利用大型语言模型进行跨模态远程生理感知的协作优化框架。该框架旨在解决远程光电容积描记术在光照变化和运动伪影下的挑战。其核心创新包括文本原型引导策略，将血流动力学特征投影到LLM可解释的语义空间，以建立跨模态对齐；以及双域平稳算法，通过自适应时频域特征重加权解决信号不稳定性。该工作展示了如何将LLM的长期依赖建模能力与领域特定的rPPG组件相结合，以提升生理信号测量的准确性和鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Remote photoplethysmography (rPPG) enables non-contact physiological measurement but remains highly susceptible to illumination changes, motion artifacts, and limited temporal modeling. Large Language Models (LLMs) excel at capturing long-range dependencies, offering a potential solution but struggle with the continuous, noise-sensitive nature of rPPG signals due to their text-centric design. To bridge this gap, we introduce the PhysLLM, a collaborative optimization framework that synergizes LLMs with domain-specific rPPG components. Specifically, the Text Prototype Guidance (TPG) strategy is proposed to establish cross-modal alignment by projecting hemodynamic features into LLM-interpretable semantic space, effectively bridging the representational gap between physiological signals and linguistic tokens. Besides, a novel Dual-Domain Stationary (DDS) Algorithm is proposed for resolving signal instability through adaptive time-frequency domain feature re-weighting. Finally, rPPG task-specific cues systematically inject physiological priors through physiological statistics, environmental contextual answering, and task description, leveraging cross-modal learning to integrate both visual and textual information, enabling dynamic adaptation to challenging scenarios like variable illumination and subject movements. Evaluation on four benchmark datasets, PhysLLM achieves state-of-the-art accuracy and robustness, demonstrating superior generalization across lighting variations and motion scenarios. The source code is available at this https URL .

</details>

---

### 39. [Foam-Agent: Towards Automated Intelligent CFD Workflows](https://arxiv.org/abs/2505.04997)

**基本信息**

- 🔗 arXiv: [`2505.04997`](https://arxiv.org/abs/2505.04997)
- 👥 作者: Ling Yue, Nithin Somasekharan, Tingwen Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.04997.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是构建一个由大型语言模型驱动的多智能体框架，用于自动化科学计算（CFD）工作流，与'化学大模型'（LLM在化学/化工相关科学计算中的应用）主题直接相关。

**📖 中文摘要**

本文提出了Foam-Agent，一个利用大型语言模型实现计算流体动力学端到端工作流自动化的多智能体框架。该框架能够从单一自然语言提示出发，自动执行从网格生成、高性能计算作业脚本编写到后处理可视化的完整CFD模拟工作流。它集成了检索增强生成和依赖感知调度，以合成高保真度的模拟配置。该工作展示了专门的多智能体系统如何有效降低专业知识壁垒并简化复杂的流体模拟，是LLM在科学计算（包括化学工程相关的CFD）中作为自动化智能体的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational fluid dynamics (CFD) has been the main workhorse of computational physics. Yet its steep learning curve and fragmented, multi-stage workflow create significant barriers. To address these challenges, we present Foam-Agent, a multi-agent framework leveraging large language models (LLMs) to automate the end-to-end CFD workflow from a single natural language prompt. Foam-Agent orchestrates the comprehensive simulation workflow from mesh generation and high-performance computing job scripting to post-processing visualization. The system integrates retrieval-augmented generation with dependency-aware scheduling to synthesize high-fidelity simulation configurations. Furthermore, Foam-Agent adopts the Model Context Protocol to expose its core functions as discrete, callable tools. This allows for flexible integration and use by any other agentic systems. Evaluated on 110 simulation tasks, Foam-Agent achieved a state-of-the-art execution success rate of 88.2% without expert intervention. These results demonstrate how specialized multi-agent systems can effectively reduce expertise barriers and streamline complex fluid simulations.

</details>

---

### 40. [HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals](https://arxiv.org/abs/2506.08618)

**基本信息**

- 🔗 arXiv: [`2506.08618`](https://arxiv.org/abs/2506.08618)
- 👥 作者: Xianquan Yan, Hakan Akgün, Kenji Kawaguchi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08618.pdf)

**💡 相关性分析**

满足标准2：论文提出了Poly2Graph工具并发布了HSG-12M大规模图数据集。该数据集包含复杂的空间多重图结构，可作为化学信息学中图神经网络（GNN）方法（例如用于分子图表示学习或结构推理）的重要基准或预训练资源。化学大模型（尤其是基于图结构的模型）和质谱结构推理（常涉及图表示）均可受益于此类高质量、结构丰富的图数据集。

**📖 中文摘要**

本文介绍了HSG-12M，一个包含1160万个静态和510万个动态哈密顿谱图的大规模数据集。该数据集源自非厄米量子物理中的晶体能量谱，这些谱图在复平面上形成复杂的几何结构。论文的核心贡献是提出了Poly2Graph，一个将一维晶体哈密顿量自动映射为谱图的高性能开源流程。HSG-12M是第一个大规模的空间多重图数据集，其中节点嵌入在度量空间中，并且两个节点之间几何上不同的轨迹被保留为单独的边。这项工作为数据驱动的科学发现（如凝聚态物理）奠定了基础，并为几何感知的图学习提供了新的机会。虽然论文主要关注物理系统，但其核心是构建和提供了一个大规模、高质量、结构复杂的图数据集（空间多重图）。

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

满足标准1：论文的核心研究内容是图生成模型，特别是用于分子生成。分子生成是化学信息学和药物发现的核心任务，属于化学大模型的应用范畴。BWFlow框架通过改进概率路径的构建来提升图（分子）生成的性能，直接与化学信息学中基于深度学习的分子设计与生成相关。

**📖 中文摘要**

本文提出了一种用于图生成的Bures-Wasserstein流匹配框架（BWFlow）。图生成是药物发现等领域的关键任务。现有方法（如扩散和流模型）通常独立地对节点和边的演化进行建模，并使用节点/边分离空间中的线性插值来构建概率路径，这破坏了图的互连模式，导致概率路径不规则。BWFlow通过将图表示为马尔可夫随机场（MRF）来建模节点和边的联合演化，并利用MRF对象之间的最优传输位移来设计平滑的概率路径，确保图组件的协同演化。实验在普通图生成和分子生成任务上验证了BWFlow的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation has emerged as a critical task in fields ranging from drug discovery to circuit design. Contemporary approaches, notably diffusion and flow-based models, have achieved solid graph generative performance through constructing a probability path that interpolates between reference and data distributions. However, these methods typically model the evolution of individual nodes and edges independently and use linear interpolations in the disjoint space of nodes/edges to build the path. This disentangled interpolation breaks the interconnected patterns of graphs, making the constructed probability path irregular and non-smooth, which causes poor training dynamics and faulty sampling convergence. To address the limitation, this paper first presents a theoretically grounded framework for probability path construction in graph generative models. Specifically, we model the joint evolution of the nodes and edges by representing graphs as connected systems parameterized by Markov random fields (MRF). We then leverage the optimal transport displacement between MRF objects to design a smooth probability path that ensures the co-evolution of graph components. Based on this, we introduce BWFlow, a flow-matching framework for graph generation that utilizes the derived optimal probability path to benefit the training and sampling algorithm design. Experimental evaluations in plain graph generation and molecule generation validate the effectiveness of BWFlow with competitive performance, better training convergence, and efficient sampling.

</details>

---

### 42. [Structured Kolmogorov-Arnold Neural ODEs for Interpretable Learning and Symbolic Discovery of Nonlinear Dynamics](https://arxiv.org/abs/2506.18339)

**基本信息**

- 🔗 arXiv: [`2506.18339`](https://arxiv.org/abs/2506.18339)
- 👥 作者: Wei Liu, Kiran Bacsa, Loon Ching Tang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.18339.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用Kolmogorov-Arnold网络（KANs）进行可解释的动力学建模和符号回归。KANs作为一种新兴的、具有潜在强大函数逼近和符号发现能力的神经网络架构，在科学机器学习（包括化学信息学）中受到广泛关注。该工作展示了KAN在从数据中发现物理定律（可视为一种“小模型”的符号推理）方面的应用，与构建可解释、可推理的“化学大模型”的研究方向在理念上相关。

**📖 中文摘要**

本文提出了结构化Kolmogorov-Arnold神经ODE（SKANODEs），一个用于非线性动力系统可解释学习和符号发现的框架。该框架将结构化状态空间建模与Kolmogorov-Arnold网络（KANs）相结合。在神经ODE架构中，SKANODE使用一个完全可训练的KAN作为通用函数逼近器来执行虚拟传感，恢复对应于可解释物理量（如位移和速度）的潜在状态。利用KAN的符号回归能力，SKANODE随后提取系统控制动力学的紧凑、可解释表达式。实验表明，SKANODE能够可靠地从加速度测量中恢复有物理意义的潜在轨迹，并识别正确的控制非线性（如Duffing振荡器中的立方刚度）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding and modeling nonlinear dynamical systems is a fundamental challenge across science and engineering. Deep learning has shown remarkable potential for capturing complex system behavior, yet achieving models that are both accurate and physically interpretable remains difficult. To address this, we propose Structured Kolmogorov-Arnold Neural ODEs (SKANODEs), a framework that integrates structured state-space modeling with Kolmogorov-Arnold Networks (KANs). Within a Neural ODE architecture, SKANODE employs a fully trainable KAN as a universal function approximator to perform virtual sensing, recovering latent states that correspond to interpretable physical quantities such as displacements and velocities. Leveraging KAN's symbolic regression capability, SKANODE then extracts compact, interpretable expressions for the system's governing dynamics. Experiments on two canonical nonlinear oscillators and a real-world F-16 ground vibration dataset demonstrate that SKANODE reliably recovers physically meaningful latent displacement and velocity trajectories from acceleration measurements, identifies the correct governing nonlinearities--including the cubic stiffness in the Duffing oscillator and the nonlinear damping structure in the Van der Pol oscillator--and reveals hysteretic signatures in the F-16 interface dynamics through structured latent phase portraits and an interpretable symbolic model. Across all three cases, SKANODE provides more accurate and robust predictions than black-box NODE baselines and classical ARX and NARX identification, while producing equation-level descriptions of the learned nonlinear dynamics.

</details>

---

### 43. [Topology Structure Optimization of Reservoirs Using GLMY Homology](https://arxiv.org/abs/2509.11612)

**基本信息**

- 🔗 arXiv: [`2509.11612`](https://arxiv.org/abs/2509.11612)
- 👥 作者: Yu Chen, Shengwei Wang, Hongwei Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.11612.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用拓扑数据分析（特别是GLMY同调）来分析和优化储层计算网络的拓扑结构。储层计算是处理时序数据（如光谱、质谱信号）的一种有效方法。优化其拓扑结构以提升性能，与化学信息学中处理复杂光谱数据、构建预测或分类模型的研究直接相关。这项工作为设计更高效的时序数据处理模型（可能用于质谱分析）提供了新思路。

**📖 中文摘要**

本文利用持久GLMY同调理论研究储层计算（Reservoir Computing）网络的拓扑结构，并开发了一种通过修改一维GLMY同调群的最小代表环来优化储层结构的方法。研究发现，储层性能与一维GLMY同调群密切相关。通过实验验证，储层性能共同受到储层结构和数据集周期性的影响。优化后的储层结构能提升时间序列处理任务的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reservoir is an efficient network for time series processing. It is well known that network structure is one of the determinants of its performance. However, the topology structure of reservoirs, as well as their performance, is hard to analyzed, due to the lack of suitable mathematical tools. In this paper, we study the topology structure of reservoirs using persistent GLMY homology theory, and develop a method to improve its performance. Specifically, it is found that the reservoir performance is closely related to the one-dimensional GLMY homology groups. Then, we develop a reservoir structure optimization method by modifying the minimal representative cycles of one-dimensional GLMY homology groups. Finally, by experiments, it is validated that the performance of reservoirs is jointly influenced by the reservoir structure and the periodicity of the dataset.

</details>

---

### 44. [TabStruct: Measuring Structural Fidelity of Tabular Data](https://arxiv.org/abs/2509.11950)

**基本信息**

- 🔗 arXiv: [`2509.11950`](https://arxiv.org/abs/2509.11950)
- 👥 作者: Xiangjian Jiang, Nikola Simidjievski, Mateja Jamnik
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.11950.pdf)

**💡 相关性分析**

满足标准2：论文提出了TabStruct基准和“全局效用”指标，用于系统评估表格数据生成器的结构保真度。化学信息学中大量使用表格数据（如分子描述符、物化性质、光谱特征等）。评估和生成高质量、结构合理的化学表格数据是构建可靠化学大模型的基础。该基准和评估框架为化学信息学领域评估数据生成方法（例如用于增强数据集或生成虚拟分子库）提供了重要的方法论参考和工具。

**📖 中文摘要**

本文提出了TabStruct，一个用于评估表格数据生成器结构保真度的新框架和基准。表格数据的独特因果结构先验使得评估合成数据是否遵守真实数据的因果结构具有挑战性。论文引入了一个新的评估指标“全局效用”，使得即使在缺乏真实因果结构的情况下也能评估结构保真度。TabStruct基准在29个数据集上对来自9个不同类别的13个表格生成器进行了大规模定量分析。结果表明，全局效用为表格生成器性能提供了一个与任务无关、领域无关的视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating tabular generators remains a challenging problem, as the unique causal structural prior of heterogeneous tabular data does not lend itself to intuitive human inspection. Recent work has introduced structural fidelity as a tabular-specific evaluation dimension to assess whether synthetic data complies with the causal structures of real data. However, existing benchmarks often neglect the interplay between structural fidelity and conventional evaluation dimensions, thus failing to provide a holistic understanding of model performance. Moreover, they are typically limited to toy datasets, as quantifying existing structural fidelity metrics requires access to ground-truth causal structures, which are rarely available for real-world datasets. In this paper, we propose a novel evaluation framework that jointly considers structural fidelity and conventional evaluation dimensions. We introduce a new evaluation metric, $\textbf{global utility}$, which enables the assessment of structural fidelity even in the absence of ground-truth causal structures. In addition, we present $\textbf{TabStruct}$, a comprehensive evaluation benchmark offering large-scale quantitative analysis on 13 tabular generators from nine distinct categories, across 29 datasets. Our results demonstrate that global utility provides a task-independent, domain-agnostic lens for tabular generator performance. We release the TabStruct benchmark suite, including all datasets, evaluation pipelines, and raw results. Code is available at this https URL .

</details>

---

### 45. [Beyond Prefixes: Graph-as-Memory Cross-Attention for Knowledge Graph Completion with Large Language Models](https://arxiv.org/abs/2510.08966)

**基本信息**

- 🔗 arXiv: [`2510.08966`](https://arxiv.org/abs/2510.08966)
- 👥 作者: Ruitong Liu, Boxu Lin, Peize Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.08966.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何将知识图谱（KG）的结构化知识有效地注入大型语言模型（LLM），以提升其在知识图谱补全等任务上的推理能力。这直接关联到“化学大模型”的研究，因为化学领域拥有丰富的知识图谱（如化合物-靶点关系、反应路径、物化性质等）。探索如何让LLM更好地理解和利用化学知识图谱进行推理（例如，质谱解析中的结构-谱图关系推理），是化学信息学大模型发展的关键方向之一。

**📖 中文摘要**

本文提出了Graph-as-Memory Tuning（GMT），一种将知识图谱与大型语言模型（LLMs）融合的新范式，用于知识图谱补全等知识密集型任务。与现有通过前缀拼接注入图谱信息的浅层交互方法不同，GMT将局部图结构表示为显式的图记忆，并通过深度、令牌级别的交叉注意力将其注入LLMs。具体来说，GMT首先使用语义图模块从局部邻域中编码上下文感知的语义，并将其压缩为固定数量的图记忆令牌。然后，一个图记忆交叉注意力融合模块将这些令牌集成到多个Transformer层中，允许LLM隐藏状态动态检索相关的图谱证据。实验表明，GMT显著优于前缀调优和其他强基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fusing Knowledge Graphs with Large Language Models (LLMs) is crucial for knowledge-intensive tasks like knowledge graph completion. Existing LLM-based approaches typically inject graph information via prefix concatenation, resulting in shallow interactions that fail to support fine-grained evidence retrieval during generation. Beyond prefixes, we propose Graph-as-Memory Tuning (GMT), a new paradigm that represents local graph structure as explicit graph memory and injects it into LLMs via deep, token-wise cross-attention. Specifically, GMT first employs a Semantic Graph Module to encode context-aware semantics from local neighborhoods guided by knowledge-enhanced relations, and compresses them into a fixed number of graph memory tokens. A Graph-as-Memory Cross-Attention Fusion Module then integrates these tokens into multiple Transformer layers, allowing LLM hidden state to dynamically retrieve relevant graph evidence. To enable efficient adaptation, GMT applies LoRA only to the memory cross-attention while keeping the base LLM frozen. Extensive experiments show that GMT significantly outperforms prefix-tuning and other strong baselines, providing more potent signals for robust reasoning. The code is published at this https URL .

</details>

---

### 46. [LLEMA: Evolutionary Search with LLMs for Multi-Objective Materials Discovery](https://arxiv.org/abs/2510.22503)

**基本信息**

- 🔗 arXiv: [`2510.22503`](https://arxiv.org/abs/2510.22503)
- 👥 作者: Nikhil Abhyankar, Sanchit Kabra, Saaketh Desai 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22503.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（LLM）引导的进化算法进行多目标材料发现。这直接属于“化学大模型”在材料科学和化学信息学中的应用。LLEMA框架展示了如何利用LLM的化学知识来提出、筛选和优化新材料，是化学领域AI for Science的典型范例。

**📖 中文摘要**

本文提出了LLEMA（LLM-guided Evolution for MAterials discovery），一个用于多目标材料发现的统一框架。该框架将大型语言模型（LLMs）中嵌入的科学知识与化学信息化的进化规则以及基于记忆的优化相结合。在每次迭代中，LLM在明确的属性约束下提出晶体学指定的候选材料；一个由代理模型增强的“预言机”估算物理化学性质；一个多目标评分器更新成功/失败记忆以指导后续世代。在涵盖电子、能源、涂层、光学和航空航天等14个现实任务上的评估表明，LLEMA发现的候选材料在化学合理性、热力学稳定性和属性对齐方面优于生成式和纯LLM基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Materials discovery requires navigating vast chemical and structural spaces while satisfying multiple, often conflicting, objectives. We present LLM-guided Evolution for MAterials discovery (LLEMA), a unified framework that couples the scientific knowledge embedded in large language models with chemistry-informed evolutionary rules and memory-based refinement. At each iteration, an LLM proposes crystallographically specified candidates under explicit property constraints; a surrogate-augmented oracle estimates physicochemical properties; and a multi-objective scorer updates success/failure memories to guide subsequent generations. Evaluated on 14 realistic tasks that span electronics, energy, coatings, optics, and aerospace, LLEMA discovers candidates that are chemically plausible, thermodynamically stable, and property-aligned, achieving higher hit rates and improved Pareto front quality relative to generative and LLM-only baselines. Ablation studies confirm the importance of rule-guided generation, memory-based refinement, and surrogate prediction. By enforcing synthesizability and multi-objective trade-offs, LLEMA provides a principled approach to accelerating practical materials discovery. Project website: this https URL

</details>

---

### 47. [FMint-SDE: A Multimodal Foundation Model for Accelerating Numerical Simulation of SDEs via Error Correction](https://arxiv.org/abs/2510.27173)

**基本信息**

- 🔗 arXiv: [`2510.27173`](https://arxiv.org/abs/2510.27173)
- 👥 作者: Jiaxin Yuan, Haizhao Yang, Maria Cameron
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27173.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于加速微分方程数值模拟的通用基础模型（FMint-SDE）。在化学和计算化学中，分子动力学模拟、化学反应动力学建模等都依赖于求解微分方程（包括SDEs）。一个能够加速此类模拟、同时保持高精度的通用模型，对化学信息学和计算化学领域具有重要价值，可视为服务于化学研究的“大模型”工具。

**📖 中文摘要**

本文介绍了FMint-SDE，一个基于初始化、用于加速随机微分方程（SDEs）数值模拟的多模态基础模型。FMint-SDE是一个基于仅解码器Transformer的模型，具有上下文学习能力，它利用数值和文本模态来学习通用的误差校正方案。该模型使用传统求解器生成的粗略解序列进行提示训练，从而能够广泛泛化到不同的系统。在涵盖分子动力学、机械系统、金融和生物学应用的SDE基准测试套件上的实验结果表明，该方法相比经典求解器实现了更优的精度-效率权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fast and accurate simulation of dynamical systems is a fundamental challenge across scientific and engineering domains. Traditional numerical integrators often face a trade-off between accuracy and computational efficiency, while existing neural network-based approaches typically require training a separate model for each case. To overcome these limitations, we introduce a novel multi-modal foundation model for large-scale simulations of differential equations: FMint-SDE (Foundation Model based on Initialization for stochastic differential equations). Based on a decoder-only transformer with in-context learning, FMint-SDE leverages numerical and textual modalities to learn a universal error-correction scheme. It is trained using prompted sequences of coarse solutions generated by conventional solvers, enabling broad generalization across diverse systems. We evaluate our models on a suite of challenging SDE benchmarks spanning applications in molecular dynamics, mechanical systems, finance, and biology. Experimental results show that our approach achieves a superior accuracy-efficiency tradeoff compared to classical solvers, underscoring the potential of FMint-SDE as a general-purpose simulation tool for dynamical systems.

</details>

---

### 48. [Interleaved Tool-Call Reasoning for Protein Function Understanding](https://arxiv.org/abs/2601.03604)

**基本信息**

- 🔗 arXiv: [`2601.03604`](https://arxiv.org/abs/2601.03604)
- 👥 作者: Chuanliu Fan, Zicheng Ma, Huanran Meng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.03604.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何为蛋白质功能理解这一化学/生物信息学领域构建专门的、工具增强的大语言模型（化学大模型）智能体，直接涉及“化学大模型”主题。

**📖 中文摘要**

这篇论文探讨了将大语言模型（LLMs）的推理能力应用于蛋白质功能理解这一特定领域。作者指出，直接将基于文本的推理范式（如思维链）迁移到蛋白质功能预测等知识密集型科学任务中是无效的，因为这些任务从根本上依赖于外部的生物学先验知识和计算工具，而非纯粹的内部推理。为此，他们提出了PFUA，一个工具增强的蛋白质推理智能体。PFUA将问题分解、工具调用和基于证据的答案生成统一起来，利用领域特定工具（如生物信息学数据库和计算工具）来产生可验证的中间证据，而不是依赖冗长且不受约束的推理轨迹。这项工作与“化学大模型”主题高度相关，因为它展示了如何为特定科学领域（此处为蛋白质科学，是化学信息学的核心领域）构建专门的、工具增强的LLM智能体框架，以解决复杂的科学推理问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

</details>

---

### 49. [Replacing Parameters with Preferences: Federated Alignment of Heterogeneous Vision-Language Models](https://arxiv.org/abs/2602.00485)

**基本信息**

- 🔗 arXiv: [`2602.00485`](https://arxiv.org/abs/2602.00485)
- 👥 作者: Shule Lu, Yujing Wang, Hainan Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00485.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于异构视觉语言模型的新型联邦对齐框架，其核心方法论（用偏好对齐替代参数共享）对于在受隐私和数据孤岛限制的领域（如化学信息学）构建和部署“化学大模型”具有直接的相关性和启发性。

**📖 中文摘要**

这篇论文提出了MoR，一个基于GRPO和混合奖励的联邦对齐框架，用于异构视觉语言模型（VLMs）。该框架旨在解决在隐私敏感领域（如医疗、金融）进行联邦学习时面临的客户端异构性挑战。MoR的核心思想是用“偏好”替代“参数”进行联邦对齐：每个客户端在本地从偏好标注中训练一个奖励模型，捕获特定的评估信号而不暴露原始数据；服务器则使用一种基于路由的融合机制自适应地聚合这些异构的客户端奖励信号，然后通过GRPO优化基础VLM。论文在三个公共VQA基准上进行了实验。这项工作与“化学大模型”主题相关，因为它提出了一种新颖的、可扩展的联邦学习框架，用于对齐异构的视觉语言模型。虽然论文以通用VLM为例，但其解决数据隐私、模型异构性和对齐问题的框架和方法，对于在化学信息学等受隐私和数据孤岛限制的领域中开发和部署专用大模型具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

VLMs have broad potential in privacy-sensitive domains such as healthcare and finance, yet strict data-sharing constraints render centralized training infeasible. FL mitigates this issue by enabling decentralized training, but practical deployments face challenges due to client heterogeneity in computational resources, application requirements, and model architectures. We argue that while replacing data with model parameters characterizes the present of FL, replacing parameters with preferences represents a more scalable and privacy-preserving future. Motivated by this perspective, we propose MoR, a federated alignment framework based on GRPO with Mixture-of-Rewards for heterogeneous VLMs. MoR initializes a visual foundation model as a KL-regularized reference, while each client locally trains a reward model from local preference annotations, capturing specific evaluation signals without exposing raw data. To reconcile heterogeneous rewards, we introduce a routing-based fusion mechanism that adaptively aggregates client reward signals. Finally, the server performs GRPO with this mixed reward to optimize the base VLM. Experiments on three public VQA benchmarks demonstrate that MoR consistently outperforms federated alignment baselines in generalization, robustness, and cross-client adaptability. Our approach provides a scalable solution for privacy-preserving alignment of heterogeneous VLMs under federated settings.

</details>

---

### 50. [SubQuad: Near-Quadratic-Free Structure Inference with Distribution-Balanced Objectives in Adaptive Receptor framework](https://arxiv.org/abs/2602.17330)

**基本信息**

- 🔗 arXiv: [`2602.17330`](https://arxiv.org/abs/2602.17330)
- 👥 作者: Rong Fu, Zijian Zhang, Kun Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.17330.pdf)

**💡 相关性分析**

满足标准2：提出的SubQuad系统是一个用于免疫受体库分析的计算工具和流程，其核心方法（如近次二次方检索、多模态融合、公平性约束聚类）在概念上与化学信息学中处理高维、复杂分子/生物分子数据（如质谱数据）和进行结构/功能推理的挑战高度相关。该系统可被视为一种用于复杂生物分子数据分析的‘工具’或‘资源’范例。

**📖 中文摘要**

本文提出SubQuad，一个用于自适应免疫受体库比较分析的计算框架。它解决了两个关键瓶颈：用于成对亲和力评估的近二次方计算成本，以及掩盖临床重要少数克隆型的数据集不平衡问题。该框架结合了抗原感知的近次二次方检索、GPU加速的亲和力核、学习的多模态融合和公平性约束的聚类。通过紧凑的MinHash预过滤、可微门控模块和自动校准例程，SubQuad在大型病毒和肿瘤受体库上实现了吞吐量和峰值内存使用的显著提升，同时保持或提高了召回率、聚类纯度和亚组公平性。该系统为可扩展、无偏见的受体库挖掘和下游转化任务（如疫苗靶点优先排序和生物标志物发现）提供了一个平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Comparative analysis of adaptive immune repertoires at population scale is hampered by two practical bottlenecks: the near-quadratic cost of pairwise affinity evaluations and dataset imbalances that obscure clinically important minority clonotypes. We introduce SubQuad, an end-to-end pipeline that addresses these challenges by combining antigen-aware, near-subquadratic retrieval with GPU-accelerated affinity kernels, learned multimodal fusion, and fairness-constrained clustering. The system employs compact MinHash prefiltering to sharply reduce candidate comparisons, a differentiable gating module that adaptively weights complementary alignment and embedding channels on a per-pair basis, and an automated calibration routine that enforces proportional representation of rare antigen-specific subgroups. On large viral and tumor repertoires SubQuad achieves measured gains in throughput and peak memory usage while preserving or improving recall@k, cluster purity, and subgroup equity. By co-designing indexing, similarity fusion, and equity-aware objectives, SubQuad offers a scalable, bias-aware platform for repertoire mining and downstream translational tasks such as vaccine target prioritization and biomarker discovery.

</details>

---

### 51. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕‘化学大模型’主题。Zatom-1是一个专门为3D分子和材料设计的、统一的生成与预测基础模型，是化学领域大模型的典型代表。其多模态流匹配方法和在分子/材料任务上的评估，完全契合化学信息学中对先进AI模型的研究。

**📖 中文摘要**

本文介绍了Zatom-1，一个用于3D分子和材料的统一多模态流匹配基础模型。该模型旨在统一生成和预测学习，克服现有AI方法通常针对单一领域（分子或材料）和单一任务（生成或预测）的局限性。Zatom-1是一个Transformer模型，通过多模态流匹配目标联合建模离散原子类型和连续3D几何结构。这种方法支持可扩展的预训练，并支持快速稳定的采样。作者使用联合生成预训练作为下游多任务预测（如性质、能量和力）的通用初始化。实验表明，Zatom-1在生成和预测基准测试中匹配或优于专门的基线模型，同时将生成推理时间减少了一个数量级以上。研究还证明了通过联合生成预训练在化学领域之间产生了正向的预测迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first end-to-end, fully open-source foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 52. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的、高效的机器学习原子间势（MLIP），这是化学和材料科学中‘化学大模型’的关键组成部分之一。MatRIS模型旨在解决现有大模型的计算瓶颈，并提升在材料预测任务上的性能，直接属于化学大模型的研究范畴。

**📖 中文摘要**

本文介绍了MatRIS，一个用于材料表示和交互模拟的不变机器学习原子间势（MLIP）模型。针对当前等变MLIPs因依赖张量积和高阶表示而导致计算成本高昂的问题，MatRIS提出了一种基于注意力的三体相互作用建模方法。它利用一种新颖的、具有线性复杂度的可分离注意力机制，实现了可扩展性和表达性。MatRIS在广泛的流行基准测试（如Matbench-Discovery, MatPES等）上提供了与领先的等变模型相媲美的精度，但训练成本更低。这项工作表明，精心设计的不变模型可以以较低的成本匹配甚至超过等变模型的精度，为开发准确高效的MLIPs提供了启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 53. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是发展关联记忆模型（如Hopfield网络）中顺序推理的理论，这直接关联到构建能够进行复杂、连贯推理的‘化学大模型’或‘科学推理模型’的基础机制。理解记忆检索和整合的动态过程对于设计能够处理多步质谱结构推理或化学知识发现的AI系统至关重要。

**📖 中文摘要**

本文为Hopfield网络中的顺序推理发展了一套动力学理论。作者考虑了最近提出的输入驱动可塑性（IDP）Hopfield网络，并分析了一个将快速关联检索与慢速推理动力学耦合的双时间尺度架构。他们推导出了自维持记忆转换的明确条件，包括增益阈值、逃逸时间和崩溃机制。这些结果为关联记忆模型中的顺序性提供了原则性的数学解释，桥接了经典的Hopfield动力学和现代推理架构。研究旨在理解检索和顺序性，为从语言理解到多模态生成的机器学习系统中的顺序推理提供见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 54. [Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning](https://arxiv.org/abs/2603.03229)

**基本信息**

- 🔗 arXiv: [`2603.03229`](https://arxiv.org/abs/2603.03229)
- 👥 作者: Adam Watts, Andrew Jeon, Destry Newton 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03229.pdf)

**💡 相关性分析**

满足标准2：论文提出的CVAE模型是一个用于解决逆问题的数据驱动生成工具。虽然应用领域是工程动力学，但其核心方法论——从谱数据（一种降维或特征化表示）逆向生成原始高维信号（时间序列）——与‘质谱结构推理’的核心挑战（从质谱数据逆向推导分子结构）在问题形式上高度相似。该论文展示了使用生成模型解决此类逆问题的有效框架。

**📖 中文摘要**

本文提出使用条件变分自编码器（CVAE）来学习从冲击响应谱（SRS）到加速度时间序列的数据驱动逆映射。该模型一旦训练完成，就可以根据指定的目标谱生成一致的时间信号，而无需迭代优化。实验表明，相对于经典技术，该方法在谱保真度方面有所改进，对未见过的谱具有强大的泛化能力，并且推理速度比传统方法快三到六个数量级。这些结果确立了深度生成模型作为逆SRS重建的可扩展且高效的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions. We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

</details>

---

### 55. [DMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement](https://arxiv.org/abs/2603.03769)

**基本信息**

- 🔗 arXiv: [`2603.03769`](https://arxiv.org/abs/2603.03769)
- 👥 作者: Youngmin Kim, Jaeyun Shin, Jeongchan Kim 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03769.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个结合了神经薛定谔桥和扩散模型引导的先进生成式AI框架，用于医学图像增强。虽然应用领域是医学影像，但其核心方法——利用生成模型进行跨域、无配对的数据转换和增强——为化学信息学中可能面临的数据稀缺、跨仪器/条件质谱数据标准化或增强问题提供了潜在的工具和方法论参考。

**📖 中文摘要**

本文提出了一种用于将超低场（64 mT）脑MRI增强到3 T质量的无配对图像翻译框架。该方法基于无配对神经薛定谔桥（UNSB）并进行多步细化。为了加强目标分布对齐，作者使用冻结的3T扩散教师模型，通过DMD2风格的扩散引导分布匹配来增强对抗目标。为了在图像块级对应之外明确约束全局结构，他们将PatchNCE与解剖结构保持（ASP）正则化器相结合，该正则化器强制执行软前景-背景一致性和边界感知约束。在两个独立队列上的评估表明，所提出的框架在未配对基准测试中提高了分布级真实感，同时在配对队列中与未配对基线相比增加了结构保真度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ultra Low Field (64 mT) brain MRI improves accessibility but suffers from reduced image quality compared to 3 T. As paired 64 mT - 3 T scans are scarce, we propose an unpaired 64 mT $\rightarrow$ 3 T translation framework that enhances realism while preserving anatomy. Our method builds upon the Unpaired Neural Schrödinge Bridge (UNSB) with multi-step refinement. To strengthen target distribution alignment, we augment the adversarial objective with DMD2-style diffusion-guided distribution matching using a frozen 3T diffusion teacher. To explicitly constrain global structure beyond patch-level correspondence, we combine PatchNCE with an Anatomical Structure Preservation (ASP) regularizer that enforces soft foreground background consistency and boundary aware constraints. Evaluated on two disjoint cohorts, the proposed framework achieves an improved realism structure trade-off, enhancing distribution level realism on unpaired benchmarks while increasing structural fidelity on the paired cohort compared to unpaired baselines.

</details>

---

### 56. [TumorFlow: Physics-Guided Longitudinal MRI Synthesis of Glioblastoma Growth](https://arxiv.org/abs/2603.04058)

**基本信息**

- 🔗 arXiv: [`2603.04058`](https://arxiv.org/abs/2603.04058)
- 👥 作者: Valentin Biller, Niklas Bubeck, Lucas Zimmer 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04058.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个结合了机理模型（生物物理生长模型）和生成式AI的框架，用于合成具有生物学合理性的医学影像数据。这种方法论对于化学信息学和质谱分析具有重要启示：可以类似地结合化学规则（如反应机理、质谱碎裂规则）与生成模型，来合成或增强质谱数据，或进行分子结构生成的逆向推理，是构建‘质谱结构推理’高级工具的一种可行路径。

**📖 中文摘要**

本文提出了一个生物物理条件生成框架，用于合成胶质母细胞瘤生长的纵向MRI。该方法结合了生成模型和可以通过生物物理生长模型在时间上传播的肿瘤浸润图，从而能够对肿瘤形状和生长进行细粒度控制，同时保留患者解剖结构。这使得能够直接在真实患者的空间中合成一致的肿瘤生长轨迹，提供可解释的、可控的肿瘤浸润和进展估计，超出了成像中明确观察到的范围。作者在纵向胶质母细胞瘤病例上评估了该框架，并证明其可以生成具有真实肿瘤外观和周围组织反应变化的时间相干序列。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Glioblastoma exhibits diverse, infiltrative, and patient-specific growth patterns that are only partially visible on routine MRI, making it difficult to reliably assess true tumor extent and personalize treatment planning and follow-up. We present a biophysically-conditioned generative framework that synthesizes biologically realistic 3D brain MRI volumes from estimated, spatially continuous tumor-concentration fields. Our approach combines a generative model with tumor-infiltration maps that can be propagated through time using a biophysical growth model, enabling fine-grained control over tumor shape and growth while preserving patient anatomy. This enables us to synthesize consistent tumor growth trajectories directly in the space of real patients, providing interpretable, controllable estimation of tumor infiltration and progression beyond what is explicitly observed in imaging. We evaluate the framework on longitudinal glioblastoma cases and demonstrate that it can generate temporally coherent sequences with realistic changes in tumor appearance and surrounding tissue response. These results suggest that integrating mechanistic tumor growth priors with modern generative modeling can provide a practical tool for patient-specific progression visualization and for generating controlled synthetic data to support downstream neuro-oncology workflows. In longitudinal extrapolation, we achieve a consistent 75% Dice overlap with the biophysical model while maintaining a constant PSNR of 25 in the surrounding tissue. Our code is available at: this https URL

</details>

---

### 57. [AgentIR: Reasoning-Aware Retrieval for Deep Research Agents](https://arxiv.org/abs/2603.04384)

**基本信息**

- 🔗 arXiv: [`2603.04384`](https://arxiv.org/abs/2603.04384)
- 👥 作者: Zijian Chen, Xueguang Ma, Shengyao Zhuang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04384.pdf)

**💡 相关性分析**

满足标准2：论文提出的‘推理感知检索’范式和DR-Synth数据合成方法，为构建更智能的检索系统提供了新的工具和资源思路。在化学信息学背景下，这种能够理解用户（或AI智能体）复杂推理意图的检索系统，对于辅助化学大模型进行文献调研、知识获取或质谱数据库检索以支持结构推理，具有重要的应用潜力。

**📖 中文摘要**

本文针对深度研究智能体这一新兴检索系统主要用户，提出了‘推理感知检索’新范式。该范式将智能体的自然语言推理轨迹与其查询共同嵌入，以利用其中被现有检索器忽略的丰富意图和上下文信息。作者还引入了DR-Synth数据合成方法，从标准QA数据集中生成深度研究检索器训练数据。结合两者训练出的嵌入模型AgentIR-4B在BrowseComp-Plus基准测试中取得了显著提升。这项工作展示了如何通过利用智能体推理过程来显著改进检索效果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep Research agents are rapidly emerging as primary consumers of modern retrieval systems. Unlike human users who issue and refine queries without documenting their intermediate thought processes, Deep Research agents generate explicit natural language reasoning before each search call, revealing rich intent and contextual information that existing retrievers entirely ignore. To exploit this overlooked signal, we introduce: (1) Reasoning-Aware Retrieval, a retrieval paradigm that jointly embeds the agent's reasoning trace alongside its query; and (2) DR-Synth, a data synthesis method that generates Deep Research retriever training data from standard QA datasets. We demonstrate that both components are independently effective, and their combination yields a trained embedding model, AgentIR-4B, with substantial gains. On the challenging BrowseComp-Plus benchmark, AgentIR-4B achieves 68\% accuracy with the open-weight agent Tongyi-DeepResearch, compared to 50\% with conventional embedding models twice its size, and 37\% with BM25. Code and data are available at: this https URL .

</details>

---

### 58. [Structured quantum learning via em algorithm for Boltzmann machines](https://arxiv.org/abs/2507.21569)

**基本信息**

- 🔗 arXiv: [`2507.21569`](https://arxiv.org/abs/2507.21569)
- 👥 作者: Takeshi Kimura, Kohtaro Kato, Masahito Hayashi
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.21569.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子机器学习模型（量子玻尔兹曼机）的新型训练算法。量子机器学习是推动下一代‘化学大模型’发展的前沿探索方向之一，特别是在模拟量子化学系统方面具有潜在优势。该研究提出的量子EM算法旨在解决QML中的关键训练难题，直接关联到未来可能用于化学模拟和发现的先进模型架构与训练方法。

**📖 中文摘要**

本文针对量子玻尔兹曼机（QBMs）训练中存在的梯度消失（贫瘠高原）问题，引入了一种量子版本的EM算法。该算法是经典期望最大化方法的信息几何推广，避免了在非凸函数上进行基于梯度的优化。作者在一个半量子限制玻尔兹曼机（sqRBM）——一种将量子效应限制在隐藏层的混合架构——上实现了该方法，并在多个基准数据集上实现了稳定的学习，且性能优于梯度下降。这些结果为量子机器学习中的梯度训练提供了一种结构化、可扩展的替代方案，为缓解贫瘠高原和增强量子生成建模提供了途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Boltzmann machines (QBMs) are generative models with potential advantages in quantum machine learning, yet their training is fundamentally limited by the barren plateau problem, where gradients vanish exponentially with system size. We introduce a quantum version of the em algorithm, an information-geometric generalization of the classical Expectation-Maximization method, which circumvents gradient-based optimization on non-convex functions. Implemented on a semi-quantum restricted Boltzmann machine (sqRBM) -- a hybrid architecture with quantum effects confined to the hidden layer -- our method achieves stable learning and outperforms gradient descent on multiple benchmark datasets. These results establish a structured and scalable alternative to gradient-based training in QML, offering a pathway to mitigate barren plateaus and enhance quantum generative modeling.

</details>

---

### 59. [CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery](https://arxiv.org/abs/2511.19500)

**基本信息**

- 🔗 arXiv: [`2511.19500`](https://arxiv.org/abs/2511.19500)
- 👥 作者: Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.19500.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学大模型（MatGPT，一种用于有机半导体生成的生成式模型）和化学信息学（利用图神经网络进行分子表示学习和性能预测）。同时满足标准2：论文提供了专门用于化学大模型和分子性质预测的大规模精选数据集OPV2D。

**📖 中文摘要**

本文提出了一个用于有机光伏（OPV）材料发现的机器学习框架CycleChemist。该框架结合了预测建模与生成式分子设计，并引入了有机光伏供体-受体数据集（OPV2D），这是目前同类中最大的、包含2000个实验表征的供体-受体对的精选数据集。框架包含多个组件：有机光伏分类器（OPVC）用于预测材料是否具有OPV特性；一个结合多任务学习和供体-受体相互作用建模的层次图神经网络；用于预测HOMO和LUMO能级的分子轨道能量估计器（MOE2）；以及用于估计功率转换效率（PCE）的光伏性能预测器（P3）。此外，还引入了材料生成预训练Transformer（MatGPT）来生成可合成的有机半导体。该工作通过将分子表示学习与性能预测相结合，推动了高性能OPV材料的数据驱动发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials.

</details>

---

### 60. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”（提出了一种新的化学大语言模型推理范式LatentChem）和“化学信息学”（专注于改进化学领域的复杂推理任务）。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。针对当前化学大语言模型（LLMs）主要依赖显式的自然语言思维链（CoT）进行复杂推理的局限性，LatentChem将化学计算与文本生成解耦，使模型能够在连续的潜在空间中直接执行多步推理，而仅在最终输出时生成语言。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，更具有计算优势。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于强大的CoT基线取得了59.88%的非平局胜率，同时实现了平均10.84倍的推理加速。结果表明，化学推理更自然、更有效地体现为连续的潜在动态过程，而非离散的语言轨迹。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 61. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准1：论文的研究内容与“化学信息学”和“质谱结构推理”高度相关，因为它提出的图结构预测和不确定性量化方法可直接应用于分子结构预测和推理问题，这是质谱结构推理的核心任务之一。

**📖 中文摘要**

本文提出了一种用于图结构输出的保形预测框架，旨在为结构化输出空间（如图）提供分布无关的覆盖保证。该方法通过Z-Gromov-Wasserstein距离（实践中通过融合Gromov-Wasserstein距离实例化）来定义非保形性度量，从而实现对预测图和候选图之间进行置换不变的比较。为了获得自适应的预测集，作者将保形化分位数回归（CQR）扩展到复杂输出空间，提出了分数保形化分位数回归（SCQR）。论文在一个合成任务和一个真实的分子识别问题上评估了所提出的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 62. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学中的核心计算工具——密度泛函理论（DFT）的自动化，并提出了一个多智能体框架（TritonDFT）来管理和优化这一复杂工作流，这属于化学大模型（自动化智能体系统）在计算化学中的应用。同时满足标准2：论文提供了用于评估此类自动化系统的基准测试DFTBench。

**📖 中文摘要**

本文介绍了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学的基石，但其实际执行需要协调复杂、多步骤的工作流程。TritonDFT通过专家策划、可扩展的工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效、准确的DFT执行。此外，论文还引入了DFTBench，一个用于评估智能体在多维度能力（包括科学专业知识、权衡优化、高性能计算知识和成本效率）的基准测试。TritonDFT为实际使用提供了开放的交互界面。该工作旨在自动化化学和材料科学中至关重要的计算工作流。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：14
- 累计论文数量：954

## 📝 历史记录

> 暂无历史数据

