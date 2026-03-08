# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-08 01:28:18

## 📅 2026-03-08 (今日最新)

**相关论文数：84**

### 1. [Lost in Translation: How Language Re-Aligns Vision for Cross-Species Pathology](https://arxiv.org/abs/2603.04405)

**基本信息**

- 🔗 arXiv: [`2603.04405`](https://arxiv.org/abs/2603.04405)
- 👥 作者: Ekansh Arora
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04405.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用语言模型（作为大模型的一种）来引导和改善跨领域科学数据（病理图像）的推理与泛化，这与“化学大模型”主题中利用AI大模型处理和理解复杂科学数据的核心思想直接相关。

**📖 中文摘要**

本文研究了基础模型在计算病理学中的应用，特别是在跨癌症和跨物种迁移中的行为。研究重点在于通过语言对齐来引导视觉特征，以解决跨物种泛化中的语义崩溃问题。作者引入了“语义锚定”方法，利用语言为视觉特征提供一个稳定的坐标系。这项工作与“化学大模型”主题相关，因为它探索了多模态基础模型（结合视觉和语言）在科学领域（病理学）的应用，并深入研究了如何利用语言指导来改善模型在复杂、结构化数据（组织图像）上的推理和泛化能力。其核心机制——使用语言重新解释和稳定视觉语义——与构建能够理解和推理复杂科学数据（如化学结构或质谱）的大模型理念相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models are increasingly applied to computational pathology, yet their behavior under cross-cancer and cross-species transfer remains unspecified. This study investigated how fine-tuning CPath-CLIP affects cancer detection under same-cancer, cross-cancer, and cross-species conditions using whole-slide image patches from canine and human histopathology. Performance was measured using area under the receiver operating characteristic curve (AUC). Few-shot fine-tuning improved same-cancer (64.9% to 72.6% AUC) and cross-cancer performance (56.84% to 66.31% AUC). Cross-species evaluation revealed that while tissue matching enables meaningful transfer, performance remains below state-of-the-art benchmarks (H-optimus-0: 84.97% AUC), indicating that standard vision-language alignment is suboptimal for cross-species generalization. Embedding space analysis revealed extremely high cosine similarity (greater than 0.99) between tumor and normal prototypes. Grad-CAM shows prototype-based models remain domain-locked, while language-guided models attend to conserved tumor morphology. To address this, we introduce Semantic Anchoring, which uses language to provide a stable coordinate system for visual features. Ablation studies reveal that benefits stem from the text-alignment mechanism itself, regardless of text encoder complexity. Benchmarking against H-optimus-0 shows that CPath-CLIP's failure stems from intrinsic embedding collapse, which text alignment effectively circumvents. Additional gains were observed in same-cancer (8.52%) and cross-cancer classification (5.67%). We identified a previously uncharacterized failure mode: semantic collapse driven by species-dominated alignment rather than missing visual information. These results demonstrate that language acts as a control mechanism, enabling semantic re-interpretation without retraining.

</details>

---

### 2. [Additive Multi-Step Markov Chains and the Curse of Dimensionality in Large Language Models](https://arxiv.org/abs/2603.04412)

**基本信息**

- 🔗 arXiv: [`2603.04412`](https://arxiv.org/abs/2603.04412)
- 👥 作者: O.V. Usatenko, S.S. Melnyk, G.M. Pritula
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04412.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕大型语言模型（LLMs）的内部动力学建模，LLMs是“化学大模型”领域所依赖和借鉴的核心技术架构。论文的理论分析为理解大模型如何处理序列化、高维数据提供了基础视角，这与化学信息学中处理分子序列或光谱序列的挑战有共通之处。

**📖 中文摘要**

本文探讨了在大规模语言模型（LLMs）的极高维状态空间中，使用N阶加性马尔可夫链来近似其动态的理论可行性。该模型允许将下一个token的条件概率分解为多个历史深度的贡献叠加，从而减少了通常与高阶马尔可夫过程相关的组合爆炸。主要成果是建立了加性多步链与具有逐步记忆函数的链之间的对应关系，并引入了信息温度的概念。这项工作与“化学大模型”主题相关，因为它从理论计算模型的角度深入分析了大型语言模型（作为大模型的核心代表）的内部生成动力学和依赖关系。理解这种高维状态空间中的复杂依赖关系，对于构建和优化能够处理序列化科学数据（如分子SMILES字符串或质谱峰序列）的化学领域大模型具有基础理论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large-scale language models (LLMs) operate in extremely high-dimensional state spaces, where both token embeddings and their hidden representations create complex dependencies that are not easily reduced to classical Markov structures. In this paper, we explore a theoretically feasible approximation of LLM dynamics using N-order additive Markov chains. Such models allow the conditional probability of the next token to be decomposed into a superposition of contributions from multiple historical depths, reducing the combinatorial explosion typically associated with high-order Markov processes. The main result of the work is the establishment of a correspondence between an additive multi-step chain and a chain with a step-wise memory function. This equivalence allowed the introduction of the concept of information temperature not only for stepwise but also for additive N-order Markov chains.

</details>

---

### 3. [Machine Learning for Complex Systems Dynamics: Detecting Bifurcations in Dynamical Systems with Deep Neural Networks](https://arxiv.org/abs/2603.04420)

**基本信息**

- 🔗 arXiv: [`2603.04420`](https://arxiv.org/abs/2603.04420)
- 👥 作者: Swadesh Pal, Roderick Melnik
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04420.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于复杂动力系统分析的机器学习框架（EINNs），其核心是从数据中反向推断系统参数和状态。这种“逆向推理”能力与“质谱结构推理”（从光谱数据反推分子结构）以及构建能够进行化学系统推理的“大模型”在方法论上高度相关。

**📖 中文摘要**

本文提出了一种基于深度神经网络（DNNs）的新机器学习方法，称为平衡信息神经网络（EINNs），用于检测复杂动力系统中的临界转变（分岔点）。与传统方法固定参数寻找解不同，EINN方法反向操作，使用候选平衡状态作为输入，训练DNN来推断满足平衡条件的相应系统参数。通过分析学习到的参数景观并观察平衡映射的可行性或连续性中的突变，可以有效地检测临界阈值。这项工作与“化学大模型”和“质谱结构推理”主题均有潜在关联。在化学领域，理解分子动力学、反应网络或相变中的临界行为至关重要。论文提出的机器学习框架为从复杂、高维数据中推断底层物理/化学参数和状态提供了新思路，这种“从数据反推机制”的能力正是构建用于化学系统建模和推理的大模型所需要的。此外，该方法处理非线性系统和多稳态的能力，也与从质谱数据推理复杂分子结构所面临的挑战有相似之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Critical transitions are the abrupt shifts between qualitatively different states of a system, and they are crucial to understanding tipping points in complex dynamical systems across ecology, climate science, and biology. Detecting these shifts typically involves extensive forward simulations or bifurcation analyses, which are often computationally intensive and limited by parameter sampling. In this study, we propose a novel machine learning approach based on deep neural networks (DNNs) called equilibrium-informed neural networks (EINNs) to identify critical thresholds associated with catastrophic regime shifts. Rather than fixing parameters and searching for solutions, the EINN method reverses this process by using candidate equilibrium states as inputs and training a DNN to infer the corresponding system parameters that satisfy the equilibrium condition. By analyzing the learned parameter landscape and observing abrupt changes in the feasibility or continuity of equilibrium mappings, critical thresholds can be effectively detected. We demonstrate this capability on nonlinear systems exhibiting saddle-node bifurcations and multi-stability, showing that EINNs can recover the parameter regions associated with impending transitions. This method provides a flexible alternative to traditional techniques, offering new insights into the early detection and structure of critical shifts in high-dimensional and nonlinear systems.

</details>

---

### 4. [A unified foundational framework for knowledge injection and evaluation of Large Language Models in Combustion Science](https://arxiv.org/abs/2603.04452)

**基本信息**

- 🔗 arXiv: [`2603.04452`](https://arxiv.org/abs/2603.04452)
- 👥 作者: Zonglin Yang, Runze Mao, Tianhao Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04452.pdf)

**💡 相关性分析**

满足标准1、2、3：1) 核心主题直接围绕在化学子领域（燃烧科学）构建领域专业化大语言模型。2) 提供了可用于该主题的大规模、多模态领域数据集（知识库）和评估基准（CombustionQA）。3) 论文整体构成了一个针对化学领域大模型构建的框架性论述，包含重要的相关讨论和展望。

**📖 中文摘要**

本研究提出了首个用于燃烧科学领域专业化大语言模型（LLMs）开发的端到端框架。该框架包含一个规模达35亿token的多模态AI就绪知识库（从超过20万篇同行评议文章、8000篇学位论文和约40万行燃烧CFD代码中提取）、一个严格且大部分自动化的评估基准（CombustionQA，涵盖8个子领域的436个问题）、以及一个三阶段知识注入路径（从轻量级检索增强生成到知识图谱增强检索，再到持续预训练）。作者定量验证了第一阶段（朴素RAG），发现其性能存在硬性上限，并指出构建领域基础模型需要结构化的知识图谱和持续预训练。这项工作与“化学大模型”主题高度相关，因为它提供了一个在特定化学子领域（燃烧科学）构建领域专业化大语言模型的完整蓝图、数据集和评估方法。论文详细探讨了知识注入、评估基准构建以及RAG与持续预训练的结合，这些都是化学信息学领域开发专用大模型的关键技术环节。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To advance foundation Large Language Models (LLMs) for combustion science, this study presents the first end-to-end framework for developing domain-specialized models for the combustion community. The framework comprises an AI-ready multimodal knowledge base at the 3.5 billion-token scale, extracted from over 200,000 peer-reviewed articles, 8,000 theses and dissertations, and approximately 400,000 lines of combustion CFD code; a rigorous and largely automated evaluation benchmark (CombustionQA, 436 questions across eight subfields); and a three-stage knowledge-injection pathway that progresses from lightweight retrieval-augmented generation (RAG) to knowledge-graph-enhanced retrieval and continued pretraining. We first quantitatively validate Stage 1 (naive RAG) and find a hard ceiling: standard RAG accuracy peaks at 60%, far surpassing zero-shot performance (23%) yet well below the theoretical upper bound (87%). We further demonstrate that this stage's performance is severely constrained by context contamination. Consequently, building a domain foundation model requires structured knowledge graphs and continued pretraining (Stages 2 and 3).

</details>

---

### 5. [Standing on the Shoulders of Giants: Rethinking EEG Foundation Model Pretraining via Multi-Teacher Distillation](https://arxiv.org/abs/2603.04478)

**基本信息**

- 🔗 arXiv: [`2603.04478`](https://arxiv.org/abs/2603.04478)
- 👥 作者: Chenqi Li, Yu Liu, Shuo Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04478.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种新颖的基础模型构建范式——利用跨模态大模型（教师）通过蒸馏来引导特定科学领域（EEG）模型的训练。这种构建领域专用大模型的方法论与“化学大模型”主题中如何有效利用现有AI资源和有限领域数据构建化学AI模型的核心挑战直接相关。

**📖 中文摘要**

本文针对脑电图（EEG）基础模型的预训练提出了多教师蒸馏预训练（MTDP）框架。不同于主流依赖于掩码重建的自监督预训练范式，MTDP利用来自已建立的良好表征模态（如视觉和时间序列）的基础模型（教师模型），通过两阶段多教师蒸馏来引导EEG基础模型的预训练。第一阶段，通过可学习的门控网络和掩码潜在去噪目标，融合来自不同教师的表示。第二阶段，将融合后的表示蒸馏到EEG基础模型中。这项工作与“化学大模型”主题相关，因为它探索了一种新颖的、利用跨模态已有大模型知识来引导和加速特定科学领域（这里是神经科学，类比化学）基础模型构建的范式。这种“站在巨人肩膀上”的蒸馏思想，对于数据稀缺或信噪比低的科学领域（如某些化学或质谱数据集）构建大模型具有重要的方法论借鉴意义。它提供了一条可能绕过大规模领域数据预训练、利用现有通用模型能力的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pretraining for electroencephalogram (EEG) foundation models has predominantly relied on self-supervised masked reconstruction, a paradigm largely adapted from and inspired by the success of vision and language foundation models. However, unlike images and text, EEG datasets are notoriously expensive to collect and characterized by low signal-to-noise ratio. These challenges introduce difficulties in scaling the EEG foundation models and capturing the underlying neural semantics through reconstruction. In this work, we ask the question: can we stand on the shoulders of well-established foundation models from well-represented modalities to bootstrap the pretraining of EEG foundation models? We first demonstrate that mainstream foundation models, such as those from vision and time series, transfer surprisingly well to EEG domain. To this end, we propose the Multi-Teacher Distillation Pretraining (MTDP) framework for pretraining EEG foundation models via a two-stage multi-teacher distillation. In the first stage, we introduce a learnable gating network to fuse representations from diverse teachers (e.g., DINOv3 and Chronos) via a masked latent denoising objective. In the second stage, we distill the fused representation into an EEG foundation model. Extensive evaluations across 9 downstream tasks and 12 datasets demonstrate that our MTDP-based EEG foundation model outperforms its self-supervised counterparts while requiring only 25% of the pretraining data.

</details>

---

### 6. [Augmenting representations with scientific papers](https://arxiv.org/abs/2603.04516)

**基本信息**

- 🔗 arXiv: [`2603.04516`](https://arxiv.org/abs/2603.04516)
- 👥 作者: Nicolò Oreste Pinciroli Vago, Rocco Di Tella, Carolina Cuesta-Lázaro 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04516.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题直接围绕利用对比学习和大模型架构对齐科学文本与仪器光谱数据，构建共享的多模态表示，这本质上是构建用于科学数据推理的“化学大模型”的一个具体实例。2) 提出并验证了一种将领域知识（文献）与观测数据（光谱）融合的框架和方法，这本身就是一种可用于“质谱结构推理”等主题的数据资源整合与利用工具。

**📖 中文摘要**

本文引入了一个对比学习框架，旨在将X射线光谱与从科学文献中提取的领域知识对齐，以促进共享多模态表示的发展。研究表明，尽管科学文本比光谱包含更广泛、更多样的物理背景，但这种对齐是可能且有效的。该框架在从光谱检索文本时实现了20%的Recall@1%，并且所得的共享潜在空间有效地编码了具有物理意义的信息。通过融合光谱和文本数据，在20个物理变量的估计上比单模态光谱基线提高了16-18%。这项工作与“化学大模型”和“质谱结构推理”主题高度相关。它直接演示了如何将科学文献（文本知识）与仪器观测数据（光谱）通过大模型（对比学习框架）进行对齐和融合，从而提升对科学数据的理解和推理能力。这正是化学信息学和质谱分析中梦寐以求的能力：让模型能够同时“阅读”文献知识和“分析”实验数据，进行更准确的结构推断和性质预测。论文中处理X射线光谱与文本对齐的范式，可以类比为质谱与化学文献/数据库的对齐。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Astronomers have acquired vast repositories of multimodal data, including images, spectra, and time series, complemented by decades of literature that analyzes astrophysical sources. Still, these data sources are rarely systematically integrated. This work introduces a contrastive learning framework designed to align X-ray spectra with domain knowledge extracted from scientific literature, facilitating the development of shared multimodal representations. Establishing this connection is inherently complex, as scientific texts encompass a broader and more diverse physical context than spectra. We propose a contrastive pipeline that achieves a 20% Recall@1% when retrieving texts from spectra, proving that a meaningful alignment between these modalities is not only possible but capable of accelerating the interpretation of rare or poorly understood sources. Furthermore, the resulting shared latent space effectively encodes physically significant information. By fusing spectral and textual data, we improve the estimation of 20 physical variables by 16-18% over unimodal spectral baselines. Our results indicate that a Mixture of Experts (MoE) strategy, which leverages both unimodal and shared representations, yields superior performance. Finally, outlier analysis within the multimodal latent space identifies high-priority targets for follow-up investigation, including a candidate pulsating ULX (PULX) and a gravitational lens system. Importantly, this framework can be extended to other scientific domains where aligning observational data with existing literature is possible.

</details>

---

### 7. [Discovering mathematical concepts through a multi-agent system](https://arxiv.org/abs/2603.04528)

**基本信息**

- 🔗 arXiv: [`2603.04528`](https://arxiv.org/abs/2603.04528)
- 👥 作者: Daattavya Aggarwal, Oisin Kim, Carl Henrik Ek 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04528.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕多智能体AI系统进行自主数学概念发现，这代表了“大模型”或“AI系统”在科学推理和发现前沿的探索。其“提出猜想-尝试证明-利用反馈”的循环，与构建能够进行化学推理和发现的AI系统的目标在范式上直接相关。

**📖 中文摘要**

本文提出了一种新的基于多智能体的计算数学发现模型。该系统自主提出猜想并尝试证明它们，根据反馈和不断演变的数据分布做出决策。受欧拉多面体猜想历史和文献中开放挑战的启发，论文以从多面体数据和线性代数知识中自主恢复同调概念的任务作为基准。该系统完成了这一学习问题。实验通过消融研究，统计测试了完整动态的价值。这项工作与“化学大模型”主题在精神上高度相关。它探索了AI系统（多智能体）通过实验、证明尝试和反例的交互，自主发现复杂数学概念的能力。这种“自主科学发现”的范式是化学信息学和更广泛科学AI的终极目标之一。论文展示的从数据中自动发现抽象概念（如同调）的框架，为未来构建能够从化学数据（如分子图、反应网络、质谱）中自主发现新规律、新概念的“化学大模型”或“AI科学家”提供了概念验证和启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical concepts emerge through an interplay of processes, including experimentation, efforts at proof, and counterexamples. In this paper, we present a new multi-agent model for computational mathematical discovery based on this observation. Our system, conceived with research in mind, poses its own conjectures and then attempts to prove them, making decisions informed by this feedback and an evolving data distribution. Inspired by the history of Euler's conjecture for polyhedra and an open challenge in the literature, we benchmark with the task of autonomously recovering the concept of homology from polyhedral data and knowledge of linear algebra. Our system completes this learning problem. Most importantly, the experiments are ablations, statistically testing the value of the complete dynamic and controlling for experimental setup. They support our main claim: that the optimisation of the right combination of local processes can lead to surprisingly well-aligned notions of mathematical interestingness.

</details>

---

### 8. [Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling](https://arxiv.org/abs/2603.04553)

**基本信息**

- 🔗 arXiv: [`2603.04553`](https://arxiv.org/abs/2603.04553)
- 👥 作者: Tal Daniel, Carl Qi, Dan Haramati 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04553.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于从复杂数据中学习对象化、结构化世界模型的新框架（LPWM）。其核心思想——无监督地发现基本实体并建模其动力学——与“质谱结构推理”（从光谱中推断分子实体及其结构）以及构建能够理解化学系统动态的“大模型”在核心挑战（解耦与推理）上高度相关。

**📖 中文摘要**

本文介绍了潜在粒子世界模型（LPWM），一种可扩展到真实世界多对象数据集并适用于决策的自我监督对象中心世界模型。LPWM直接从视频数据中自主发现关键点、边界框和对象掩码，使其能够在没有监督的情况下学习丰富的场景分解。该架构完全从视频端到端训练，并支持对动作、语言和图像目标的灵活条件化。LPWM通过新颖的潜在动作模块对随机粒子动力学进行建模，并在多样化的真实世界和合成数据集上取得了最先进的结果。这项工作与“化学大模型”和“质谱结构推理”有潜在关联。LPWM的核心能力是从非结构化观测数据（视频）中无监督地解耦出可解释的、对象化的表示（粒子），并对它们的动力学进行建模。这种“从复杂信号中解耦出基本实体并推理其关系”的能力，正是从质谱等复杂仪器信号中推断分子结构（“粒子”及其“连接”），或对化学系统进行动态建模所需要的。论文展示的框架为处理化学中的多实体、结构化数据提供了一种有前景的机器学习范式参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Latent Particle World Model (LPWM), a self-supervised object-centric world model scaled to real-world multi-object datasets and applicable in decision-making. LPWM autonomously discovers keypoints, bounding boxes, and object masks directly from video data, enabling it to learn rich scene decompositions without supervision. Our architecture is trained end-to-end purely from videos and supports flexible conditioning on actions, language, and image goals. LPWM models stochastic particle dynamics via a novel latent action module and achieves state-of-the-art results on diverse real-world and synthetic datasets. Beyond stochastic video modeling, LPWM is readily applicable to decision-making, including goal-conditioned imitation learning, as we demonstrate in the paper. Code, data, pre-trained models and video rollouts are available: this https URL

</details>

---

### 9. [PDE foundation model-accelerated inverse estimation of system parameters in inertial confinement fusion](https://arxiv.org/abs/2603.04606)

**基本信息**

- 🔗 arXiv: [`2603.04606`](https://arxiv.org/abs/2603.04606)
- 👥 作者: Mahindra Rautela, Alexander Scheinker, Bradley Love 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04606.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用和微调PDE基础模型（一种科学计算领域的大模型）来解决逆问题，这直接围绕“化学大模型”这一主题。

**📖 中文摘要**

本文研究了在惯性约束聚变（ICF）中，利用PDE基础模型加速系统参数逆估计的问题。研究核心是使用预训练的PDE基础模型，通过有限的任务特定数据进行微调，以从多模态、快照式观测中联合重建高光谱图像并回归系统参数。这项工作与“化学大模型”主题相关，因为它探索了基础模型（一种特定领域的大模型）在科学计算和逆问题求解中的应用。模型在JAG基准测试中表现出色，证明了基础模型初始化对于数据有限的ICF逆问题能提高样本效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PDE foundation models are typically pretrained on large, diverse corpora of PDE datasets and can be adapted to new settings with limited task-specific data. However, most downstream evaluations focus on forward problems, such as autoregressive rollout prediction. In this work, we study an inverse problem in inertial confinement fusion (ICF): estimating system parameters (inputs) from multi-modal, snapshot-style observations (outputs). Using the open JAG benchmark, which provides hyperspectral X-ray images and scalar observables per simulation, we finetune the PDE foundation model and train a lightweight task-specific head to jointly reconstruct hyperspectral images and regress system parameters. The fine-tuned model achieves accurate hyperspectral reconstruction (test MSE 1.2e-3) and strong parameter-estimation performance (up to R^2=0.995). Data-scaling experiments (5%-100% of the training set) show consistent improvements in both reconstruction and regression losses as the amount of training data increases, with the largest marginal gains in the low-data regime. Finally, finetuning from pretrained MORPH weights outperforms training the same architecture from scratch, demonstrating that foundation-model initialization improves sample efficiency for data-limited inverse problems in ICF.

</details>

---

### 10. [When Agents Persuade: Propaganda Generation and Mitigation in LLMs](https://arxiv.org/abs/2603.04636)

**基本信息**

- 🔗 arXiv: [`2603.04636`](https://arxiv.org/abs/2603.04636)
- 👥 作者: Julia Jose, Ritik Roongta, Rachel Greenstadt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04636.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从质谱衍生数据（扩散MRI）进行结构推理（微结构重建）的方法。Spinverse方法通过可微物理模拟进行逆问题求解，直接围绕“质谱结构推理”这一主题。

**📖 中文摘要**

本文提出了Spinverse，一种用于从扩散MRI（dMRI）测量中感知渗透性的微结构重建方法。该方法通过一个完全可微的Bloch-Torrey模拟器来反演dMRI测量值。Spinverse将组织表示在固定的四面体网格上，并将每个内部面的渗透率作为可学习参数；低渗透率的面充当扩散屏障，从而在不改变网格连接或顶点位置的情况下，出现拓扑结构不固定的微结构边界。给定目标信号，通过反向传播信号匹配损失来优化面渗透率，并通过阈值化学习到的渗透率场来恢复界面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite their wide-ranging benefits, LLM-based agents deployed in open environments can be exploited to produce manipulative material. In this study, we task LLMs with propaganda objectives and analyze their outputs using two domain-specific models: one that classifies text as propaganda or non-propaganda, and another that detects rhetorical techniques of propaganda (e.g., loaded language, appeals to fear, flag-waving, name-calling). Our findings show that, when prompted, LLMs exhibit propagandistic behaviors and use a variety of rhetorical techniques in doing so. We also explore mitigation via Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and ORPO (Odds Ratio Preference Optimization). We find that fine-tuning significantly reduces their tendency to generate such content, with ORPO proving most effective.

</details>

---

### 11. [Spinverse: Differentiable Physics for Permeability-Aware Microstructure Reconstruction from Diffusion MRI](https://arxiv.org/abs/2603.04638)

**基本信息**

- 🔗 arXiv: [`2603.04638`](https://arxiv.org/abs/2603.04638)
- 👥 作者: Prathamesh Pradeep Khole, Mario M. Brenes, Zahra Kais Petiwala 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04638.pdf)

**💡 相关性分析**

满足标准2：论文提供了RCodingAgent这一工具，以及RPKB知识库和DARE检索模型，这些资源可用于构建面向化学、生物统计学等领域的专业数据分析工具，属于“数据资源相关”。

**📖 中文摘要**

本文提出了DARE（Distribution-Aware Retrieval Embedding），一个轻量级、即插即用的检索模型，用于将数据分布信息融入R包函数的表示中，以改进R语言生态系统中统计工具的检索。研究构建了RPKB（R包知识库），并开发了RCodingAgent，一个面向R的LLM智能体，用于可靠的R代码生成。DARE模型在包检索任务上显著优于现有开源嵌入模型。这项工作旨在缩小LLM自动化与成熟的R统计生态系统之间的差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion MRI (dMRI) is sensitive to microstructural barriers, yet most existing methods either assume impermeable boundaries or estimate voxel-level parameters without recovering explicit interfaces. We present Spinverse, a permeability-aware reconstruction method that inverts dMRI measurements through a fully differentiable Bloch-Torrey simulator. Spinverse represents tissue on a fixed tetrahedral grid and treats each interior face permeability as a learnable parameter; low-permeability faces act as diffusion barriers, so microstructural boundaries whose topology is not fixed a priori (up to the resolution of the ambient mesh) emerge without changing mesh connectivity or vertex positions. Given a target signal, we optimize face permeabilities by backpropagating a signal-matching loss through the PDE forward model, and recover an interface by thresholding the learned permeability field. To mitigate the ill-posedness of permeability inversion, we use mesh-based geometric priors; to avoid local minima, we use a staged multi-sequence optimization curriculum. Across a collection of synthetic voxel meshes, Spinverse reconstructs diverse geometries and demonstrates that sequence scheduling and regularization are critical to avoid outline-only solutions while improving both boundary accuracy and structural validity.

</details>

---

### 12. [Gamified Informed Decision-Making for Performance-Aware Design by Non-Experts: An Exoskeleton Design Case Study](https://arxiv.org/abs/2603.04643)

**基本信息**

- 🔗 arXiv: [`2603.04643`](https://arxiv.org/abs/2603.04643)
- 👥 作者: Arman Khalilbeigi Khameneh, Armin Mostafavi, Alicia Nahmad Vazquez
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04643.pdf)

**💡 相关性分析**

满足标准2：论文贡献了TREDBench基准数据集，这是一个专门用于评估表格回归模型（特别是工程领域）的精选数据集。该资源可用于开发和评估化学、材料等领域的预测模型，属于“数据资源相关”。

**📖 中文摘要**

本文提出了TREDBench，一个包含83个真实世界表格回归数据集的精选集合，并带有工程/非工程专家标签。研究使用TabPFN 2.5的数据集级嵌入来研究公共表示空间中的领域结构。研究发现工程数据集与非工程数据集部分可区分，而标准程序生成的数据集与工程数据集高度可区分，揭示了显著的合成-真实领域差距。为了在不使用真实工程样本的情况下弥合这一差距，论文提出了一种嵌入引导的合成数据筛选方法：生成并识别“类工程”合成数据集，并仅使用选定的合成任务对TabPFN 2.5进行持续预训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Decision Support Systems (DSS) play a crucial role in enabling non-expert designers to explore complex, performance-driven design spaces. This paper presents a gamified decision-making framework that integrates game engines with real-time performance feedback. Performance criteria include structural behavior, environmental parameters, fabrication, material, and cost considerations. The developed design framework was tested with architecture students and non-expert designers on the design of an exoskeleton facade to retrofit an existing building. Participants (N=24) were able to iteratively modify façade geometries while receiving real-time feedback across the three key criteria: 1) structural behavior, including deflection, mass, and stress/strength ratio; 2) environmental parameters, such as solar gain and heating/cooling energy demands; and 3) fabrication considerations, including fabrication and material costs, robotic machining, and material setup. The evaluation of participant interactions reveals that gamified feedback mechanisms significantly enhance user comprehension and informed decision-making across the criteria. Further, participants' understanding of structural, material, and fabrication performance in relation to the iterative design task suggests that curated design spaces and structured guidance improve efficiency compared to open-ended generative tools. This research contributes to pre-occupancy evaluations, demonstrating how gamified environments enable stakeholder participation in the design process through informed decisionmaking and customized negotiation of performance criteria. .

</details>

---

### 13. [Stan: An LLM-based thermodynamics course assistant](https://arxiv.org/abs/2603.04657)

**基本信息**

- 🔗 arXiv: [`2603.04657`](https://arxiv.org/abs/2603.04657)
- 👥 作者: Eric M. Furst, Vasudevan Venkateshwaran
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04657.pdf)

**💡 相关性分析**

满足标准2：论文提出了Stan，一个专门为化学工程课程设计的AI助手工具。它结合了RAG和结构化分析，为化学教育领域提供了具体的工具和数据处理流程，属于“数据资源相关”。

**📖 中文摘要**

本文介绍了Stan，一套为本科化学工程热力学课程构建的工具套件，基于一个共享的讲座转录稿和结构化教科书索引的数据管道。在学生端，一个检索增强生成（RAG）管道通过提取技术术语、与教科书索引匹配，并合成带有具体章节和页码引用的有根据的回答，来回答自然语言查询。在教师端，相同的转录稿语料库通过结构化分析管道进行处理，生成每堂课摘要、识别学生问题和困惑时刻，并分类用于激发难懂材料的轶事和类比。所有组件均在本地控制的硬件上运行，使用开源模型，不依赖云API。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discussions of AI in education focus predominantly on student-facing tools -- chatbots, tutors, and problem generators -- while the potential for the same infrastructure to support instructors remains largely unexplored. We describe Stan, a suite of tools for an undergraduate chemical engineering thermodynamics course built on a data pipeline that we develop and deploy in dual roles: serving students and supporting instructors from a shared foundation of lecture transcripts and a structured textbook index. On the student side, a retrieval-augmented generation (RAG) pipeline answers natural-language queries by extracting technical terms, matching them against the textbook index, and synthesizing grounded responses with specific chapter and page references. On the instructor side, the same transcript corpus is processed through structured analysis pipelines that produce per-lecture summaries, identify student questions and moments of confusion, and catalog the anecdotes and analogies used to motivate difficult material -- providing a searchable, semester-scale record of teaching that supports course reflection, reminders, and improvement. All components, including speech-to-text transcription, structured content extraction, and interactive query answering, run entirely on locally controlled hardware using open-weight models (Whisper large-v3, Llama~3.1 8B) with no dependence on cloud APIs, ensuring predictable costs, full data privacy, and reproducibility independent of third-party services. We describe the design, implementation, and practical failure modes encountered when deploying 7--8 billion parameter models for structured extraction over long lecture transcripts, including context truncation, bimodal output distributions, and schema drift, along with the mitigations that resolved them.

</details>

---

### 14. [Neuro-Symbolic Financial Reasoning via Deterministic Fact Ledgers and Adversarial Low-Latency Hallucination Detector](https://arxiv.org/abs/2603.04663)

**基本信息**

- 🔗 arXiv: [`2603.04663`](https://arxiv.org/abs/2603.04663)
- 👥 作者: Pedram Agand
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04663.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于高确定性领域（如金融）的神经符号推理系统。虽然领域是金融，但其核心方法——结合严格类型的事实账本、确定性变量检索和对抗训练来确保推理可靠性——与构建用于化学信息学中分子性质预测或谱图解析的可靠、可验证大模型所面临的挑战和方法论高度相关。

**📖 中文摘要**

本文介绍了可验证数值推理智能体（VeNRA），旨在实现金融领域零幻觉推理。VeNRA将RAG范式从检索概率文本转变为通过严格类型的通用事实账本（UFL）检索确定性变量，并通过一种新颖的双锁接地算法进行数学约束。论文还引入了VeNRA Sentinel：一个30亿参数的SLM，用于法证审计Python执行轨迹。为了训练该模型，研究避免了传统的生成幻觉数据集，转而采用对抗模拟，通过程序破坏黄金财务记录来模拟生产级“生态错误”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Standard Retrieval-Augmented Generation (RAG) architectures fail in high-stakes financial domains due to two fundamental limitations: the inherent arithmetic incompetence of Large Language Models (LLMs) and the distributional semantic conflation of dense vector retrieval (e.g., mapping ``Net Income'' to ``Net Sales'' due to contextual proximity). In deterministic domains, a 99% accuracy rate yields 0% operational trust. To achieve zero-hallucination financial reasoning, we introduce the Verifiable Numerical Reasoning Agent (VeNRA). VeNRA shifts the RAG paradigm from retrieving probabilistic text to retrieving deterministic variables via a strictly typed Universal Fact Ledger (UFL), mathematically bounded by a novel Double-Lock Grounding algorithm. Recognizing that upstream parsing anomalies inevitably occur, we introduce the VeNRA Sentinel: a 3-billion parameter SLM trained to forensically audit Python execution traces with only one token test budget. To train this model, we avoid traditional generative hallucination datasets in favor of Adversarial Simulation, programmatically sabotaging golden financial records to simulate production-level ``Ecological Errors'' (e.g., Logic Code Lies and Numeric Neighbor Traps). Finally, to optimize the Sentinel under strict latency budgets, we utilize a single-pass classification paradigm with optional post thinking for debug. We identify the phenomenon of Loss Dilution in Reverse-Chain-of-Thought training and present a novel, OOM-safe Micro-Chunking loss algorithm to stabilize gradients under extreme differential penalization.

</details>

---

### 15. [Engineering Regression Without Real-Data Training: Domain Adaptation for Tabular Foundation Models Using Multi-Dataset Embeddings](https://arxiv.org/abs/2603.04692)

**基本信息**

- 🔗 arXiv: [`2603.04692`](https://arxiv.org/abs/2603.04692)
- 👥 作者: Lyle Regenwetter, Rosen Yu, Cyril Picard 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04692.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和提升表格基础模型（TabPFN 2.5）在工程领域（可延伸至化学、材料科学）的回归任务上的表现。它直接涉及“化学大模型”中一个子类（表格/结构化数据基础模型）的领域适应和性能提升。

**📖 中文摘要**

本文研究了表格基础模型在工程回归任务中的领域适应问题。通过使用TabPFN 2.5的数据集级嵌入，研究发现工程数据集与非工程数据集部分可区分，而标准程序生成的数据集与工程数据集高度可区分，揭示了显著的合成-真实领域差距。为了在不使用真实工程样本的情况下弥合这一差距，论文提出了一种嵌入引导的合成数据筛选方法，仅使用选定的“类工程”合成任务对TabPFN 2.5进行持续预训练。在35个工程回归数据集上的评估表明，这种仅使用合成数据的适应提高了预测准确性和数据效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling in engineering applications has long been dominated by bespoke models and small, siloed tabular datasets, limiting the applicability of large-scale learning approaches. Despite recent progress in tabular foundation models, the resulting synthetic training distributions used for pre-training may not reflect the statistical structure of engineering data, limiting transfer to engineering regression. We introduce TREDBench, a curated collection of 83 real-world tabular regression datasets with expert engineering/non-engineering labels, and use TabPFN 2.5's dataset-level embedding to study domain structure in a common representation space. We find that engineering datasets are partially distinguishable from non-engineering datasets, while standard procedurally generated datasets are highly distinguishable from engineering datasets, revealing a substantial synthetic-real domain gap. To bridge this gap without training on real engineering samples, we propose an embedding-guided synthetic data curation method: we generate and identify "engineering-like" synthetic datasets, and perform continued pre-training of TabPFN 2.5 using only the selected synthetic tasks. Across 35 engineering regression datasets, this synthetic-only adaptation improves predictive accuracy and data efficiency, outperforming TabPFN 2.5 on 29/35 datasets and AutoGluon on 27/35, with mean multiplicative data-efficiency gains of 1.75x and 4.44x, respectively. More broadly, our results indicate that principled synthetic data curation can convert procedural generators into domain-relevant "data engines," enabling foundation models to improve in data-sparse scientific and industrial domains where real data collection is the primary bottleneck.

</details>

---

### 16. [Solving an Open Problem in Theoretical Physics using AI-Assisted Discovery](https://arxiv.org/abs/2603.04735)

**基本信息**

- 🔗 arXiv: [`2603.04735`](https://arxiv.org/abs/2603.04735)
- 👥 作者: Michael P. Brenner, Vincent Cohen-Addad, David Woodruff
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04735.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用AI辅助的神经符号系统（结合LLM和符号推理）来解决理论物理中的开放数学问题。这展示了“化学大模型”或更广义的“科学AI”在辅助复杂科学计算和符号推理方面的潜力，属于该主题的前沿探索。

**📖 中文摘要**

本文展示了一个结合Gemini Deep Think大语言模型与系统化树搜索框架和自动化数值反馈的神经符号系统，成功推导出了宇宙弦发射引力辐射功率谱的新颖、精确解析解。具体来说，该智能体评估了任意环几何的核心积分 I(N, α)。论文详细介绍了引导模型所需的系统提示、搜索约束和间歇性反馈循环。智能体识别了6种不同的分析方法，其中最优雅的方法是用Gegenbauer多项式 C_l^{(3/2)} 展开核函数，以自然吸收被积函数的奇点。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper demonstrates that artificial intelligence can accelerate mathematical discovery by autonomously solving an open problem in theoretical physics. We present a neuro-symbolic system, combining the Gemini Deep Think large language model with a systematic Tree Search (TS) framework and automated numerical feedback, that successfully derived novel, exact analytical solutions for the power spectrum of gravitational radiation emitted by cosmic strings. Specifically, the agent evaluated the core integral $I(N,\alpha)$ for arbitrary loop geometries, directly improving upon recent AI-assisted attempts \cite{BCE+25} that only yielded partial asymptotic solutions. To substantiate our methodological claims regarding AI-accelerated discovery and to ensure transparency, we detail system prompts, search constraints, and intermittent feedback loops that guided the model. The agent identified a suite of 6 different analytical methods, the most elegant of which expands the kernel in Gegenbauer polynomials $C_l^{(3/2)}$ to naturally absorb the integrand's singularities. The methods lead to an asymptotic result for $I(N,\alpha)$ at large $N$ that both agrees with numerical results and also connects to the continuous Feynman parameterization of Quantum Field Theory. We detail both the algorithmic methodology that enabled this discovery and the resulting mathematical derivations.

</details>

---

### 17. [Distribution-Conditioned Transport](https://arxiv.org/abs/2603.04736)

**基本信息**

- 🔗 arXiv: [`2603.04736`](https://arxiv.org/abs/2603.04736)
- 👥 作者: Nic Fishman, Gokul Gowri, Paolo L. B. Fischer 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04736.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个通用的生成模型框架（DCT），用于学习条件分布之间的映射，并特别应用于质谱流式细胞术（CyTOF）数据的扰动预测等生物学问题。这直接关联“化学大模型”中的生成模型分支，并涉及质谱衍生数据的建模，与“质谱结构推理”有间接关联。

**📖 中文摘要**

本文介绍了分布条件传输（DCT），一个将传输映射以源分布和目标分布的学得嵌入为条件的框架，从而能够泛化到未见过的分布对。DCT还支持分布预测问题的半监督学习：因为它从任意分布对中学习，所以可以利用仅在单一条件下观察到的分布来改进传输预测。DCT与底层传输机制无关，支持从流匹配到基于分布散度的模型（例如Wasserstein， MMD）等多种模型。论文在合成基准和四个生物学应用上展示了DCT的实际性能优势：单细胞基因组学中的批次效应转移、从质谱流式数据预测扰动、学习造血中的克隆转录动力学以及建模T细胞受体序列进化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning a transport model that maps a source distribution to a target distribution is a canonical problem in machine learning, but scientific applications increasingly require models that can generalize to source and target distributions unseen during training. We introduce distribution-conditioned transport (DCT), a framework that conditions transport maps on learned embeddings of source and target distributions, enabling generalization to unseen distribution pairs. DCT also allows semi-supervised learning for distributional forecasting problems: because it learns from arbitrary distribution pairs, it can leverage distributions observed at only one condition to improve transport prediction. DCT is agnostic to the underlying transport mechanism, supporting models ranging from flow matching to distributional divergence-based models (e.g. Wasserstein, MMD). We demonstrate the practical performance benefits of DCT on synthetic benchmarks and four applications in biology: batch effect transfer in single-cell genomics, perturbation prediction from mass cytometry data, learning clonal transcriptional dynamics in hematopoiesis, and modeling T-cell receptor sequence evolution.

</details>

---

### 18. [Hardware-Software Co-design for 3D-DRAM-based LLM Serving Accelerator](https://arxiv.org/abs/2603.04797)

**基本信息**

- 🔗 arXiv: [`2603.04797`](https://arxiv.org/abs/2603.04797)
- 👥 作者: Cong Li, Yihan Yin, Chenhao Xue 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04797.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕优化大语言模型（LLM）的服务架构，而“化学大模型”是LLM在化学领域的特定应用。论文提出的硬件-软件协同设计、分布式注意力执行和高效内存管理方案，为构建和部署需要处理复杂图结构数据（如分子）的大模型提供了底层计算范式和性能优化思路，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出Helios，一种基于混合键合的LLM服务加速器硬件-软件协同设计。虽然其核心是优化大语言模型（LLM）的推理服务，但其提出的分布式分片注意力执行、空间感知的KV缓存分配机制等核心思想，为解决大规模、动态负载下的计算与内存瓶颈提供了通用框架。该框架所处理的“动态KV缓存管理”和“分布式非均匀内存抽象”问题，与化学信息学中处理大规模、动态分子图数据或质谱数据库时面临的挑战在本质上相似。因此，论文提出的分布式计算和内存管理范式，可作为构建或优化“化学大模型”底层计算基础设施的重要参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been widely deployed for online generative services, where numerous LLM instances jointly handle workloads with fluctuating request arrival rates and variable request lengths. To efficiently execute coexisting compute-intensive and memory-intensive operators, near-memory processing (NMP) based computing paradigm has been extensively proposed. However, existing NMP designs adopt coarse-grained KV cache management and inflexible attention execution flow. Such limitations hinder these proposals from efficiently handling \textit{highly dynamic} LLM serving workloads, limiting their ability to accelerate LLM serving. To tackle these problems, we propose Helios, a Hybrid-bonding-based \uline{L}LM \uline{S}erving accelerator. Helios aims to bridge the fundamental gap between the dynamic nature of KV cache management in LLM serving and the distributed, non-uniform memory abstraction among NMP processing engines (PEs). To this end, we design both the intra-PE execution flow and the inter-PE communication primitives for distributed tiled attention execution. We further propose \textit{spatially-aware} KV cache allocation mechanism to balance the attention workload distribution while minimizing the inter-PE data transfer overhead. Compared with existing GPU/NMP designs, Helios achieves 3.25 times (geomean) speedup and 3.36 times (geomean) better energy efficiency, along with up to 72%/76% P50/P99 time-between-tokens degradation.

</details>

---

### 19. [Beyond Linear LLM Invocation: An Efficient and Effective Semantic Filter Paradigm](https://arxiv.org/abs/2603.04799)

**基本信息**

- 🔗 arXiv: [`2603.04799`](https://arxiv.org/abs/2603.04799)
- 👥 作者: Nan Hou, Kangfei Zhao, Jiadong Xie 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04799.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究优化LLM对数据的语义推理和过滤流程，这与利用“化学大模型”进行分子或谱图数据推理的核心任务高度相关。2) 论文提出的CSV框架本身是一种高效的语义数据处理工具/范式，可用于构建或优化化学信息学中处理大规模质谱或分子数据集的数据筛选流水线。

**📖 中文摘要**

本文针对大语言模型（LLM）在语义查询处理中的线性扫描瓶颈，提出了Clustering-Sampling-Voting (CSV)框架，将LLM调用复杂度降至亚线性。该框架通过将元组嵌入到语义簇中、采样评估、并通过投票策略推断簇级标签，实现了高效且带误差保证的语义过滤。这项工作的核心是优化LLM对结构化数据的推理和筛选流程。这种“语义过滤”和“亚线性推理”范式，可以迁移到化学信息学领域，例如：用于从大型质谱数据库或分子库中快速筛选出与目标结构或谱图特征相关的候选条目，从而为“质谱结构推理”或基于大模型的分子属性预测提供高效的数据预处理和检索工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are increasingly used for semantic query processing over large corpora. A set of semantic operators derived from relational algebra has been proposed to provide a unified interface for expressing such queries, among which the semantic filter operator serves as a cornerstone. Given a table T with a natural language predicate e, for each tuple in the relation, the execution of a semantic filter proceeds by constructing an input prompt that combines the predicate e with its content, querying the LLM, and obtaining the binary decision. However, this tuple-by-tuple evaluation necessitates a complete linear scan of the table, incurring prohibitive latency and token costs. Although recent work has attempted to optimize semantic filtering, it still does not break the linear LLM invocation barriers. To address this, we propose Clustering-Sampling-Voting (CSV), a new framework that reduces LLM invocations to sublinear complexity while providing error guarantees. CSV embeds tuples into semantic clusters, samples a small subset for LLM evaluation, and infers cluster-level labels via two proposed voting strategies: UniVote, which aggregates labels uniformly, and SimVote, which weights votes by semantic similarity. Moreover, CSV triggers re-clustering on ambiguous clusters to ensure robustness across diverse datasets. The results conducted on real-world datasets demonstrate that CSV reduces the number of LLM calls by 1.28-355x compared to the state-of-the-art approaches, while maintaining comparable effectiveness in terms of Accuracy and F1 score.

</details>

---

### 20. [MASQuant: Modality-Aware Smoothing Quantization for Multimodal Large Language Models](https://arxiv.org/abs/2603.04800)

**基本信息**

- 🔗 arXiv: [`2603.04800`](https://arxiv.org/abs/2603.04800)
- 👥 作者: Lulu Hu, Wenhu Xiao, Xin Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04800.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对多模态大语言模型（MLLMs）的模型压缩（量化）技术。“化学大模型”作为一类特定的、可能包含多模态输入（如结构、谱图、文本描述）的大模型，其优化和部署面临相同的挑战。论文提出的模态感知量化框架直接适用于优化化学大模型的推理效率。

**📖 中文摘要**

本文提出MASQuant，一种用于多模态大语言模型（MLLMs）的后训练量化框架。针对MLLMs量化中的平滑错位和跨模态计算不变性问题，MASQuant引入了模态感知平滑和跨模态补偿机制。虽然研究对象是通用的多模态大模型，但其解决的核心问题——如何在不同模态（如图像、文本）的数据分布和计算特性存在差异时，实现稳定且高效的模型压缩——同样存在于“化学大模型”中。化学大模型通常需要处理多种模态的输入，如分子图（结构）、SMILES（序列）、质谱（谱图数据）等。因此，该论文提出的量化技术和分析为化学领域多模态大模型的轻量化部署提供了重要的方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Post-training quantization (PTQ) with computational invariance for Large Language Models~(LLMs) have demonstrated remarkable advances, however, their application to Multimodal Large Language Models~(MLLMs) presents substantial challenges. In this paper, we analyze SmoothQuant as a case study and identify two critical issues: Smoothing Misalignment and Cross-Modal Computational Invariance. To address these issues, we propose Modality-Aware Smoothing Quantization (MASQuant), a novel framework that introduces (1) Modality-Aware Smoothing (MAS), which learns separate, modality-specific smoothing factors to prevent Smoothing Misalignment, and (2) Cross-Modal Compensation (CMC), which addresses Cross-modal Computational Invariance by using SVD whitening to transform multi-modal activation differences into low-rank forms, enabling unified quantization across modalities. MASQuant demonstrates stable quantization performance across both dual-modal and tri-modal MLLMs. Experimental results show that MASQuant is competitive among the state-of-the-art PTQ algorithms. Source code: this https URL .

</details>

---

### 21. [Attention's Gravitational Field:A Power-Law Interpretation of Positional Correlation](https://arxiv.org/abs/2603.04805)

**基本信息**

- 🔗 arXiv: [`2603.04805`](https://arxiv.org/abs/2603.04805)
- 👥 作者: Edward Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）的基础架构机制（位置编码、注意力）。这些机制是构建所有大模型（包括“化学大模型”）的通用组件。论文对位置编码的优化和理论解释，为设计更适合化学序列或图结构数据的模型架构提供了直接参考。

**📖 中文摘要**

本文探索了大语言模型（LLMs）中位置关系与编码的底层原理，提出了注意力引力场（AGF）的概念。通过将位置编码与语义嵌入解耦，并分析AGF与牛顿万有引力定律的经验一致性，该工作旨在提升模型性能并为注意力机制提供理论解释。这项研究属于大模型基础架构和可解释性方向。其对注意力机制和位置编码的深入分析与优化，为构建和理解任何领域的大模型（包括“化学大模型”）提供了通用的理论基础和架构改进思路。例如，在化学大模型中处理分子序列或图结构时，如何有效地编码原子或子结构的位置/拓扑关系是一个关键问题，本文的研究对此具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper explores the underlying principles of positional relationships and encodings within Large Language Models (LLMs) and introduces the concept of the Attention Gravitational Field (AGF). By decoupling positional encodings from semantic embeddings, we optimize the model architecture and achieve superior accuracy compared to prevailing encoding methods. Furthermore, we provide an in-depth analysis of AGF, demonstrating its intrinsic consistency with learning and stability curves, as well as its empirical alignment with Newton's Law of Universal Gravitation. By offering a rigorous theoretical exploration of these phenomena, this work represents a significant step toward interpreting the Attention mechanism and unlocks new possibilities for future research in model optimization and interpretability.

</details>

---

### 22. [LLM-Grounded Explainability for Port Congestion Prediction via Temporal Graph Attention Networks](https://arxiv.org/abs/2603.04818)

**基本信息**

- 🔗 arXiv: [`2603.04818`](https://arxiv.org/abs/2603.04818)
- 👥 作者: Zhiming Xue, Yujue Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04818.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将图神经网络（GNN）与大语言模型（LLM）结合，进行预测和可解释推理。这正是“化学大模型”和“质谱结构推理”中一种极具潜力的技术路线：用GNN处理分子图结构，用LLM进行高级推理和解释。论文为该技术路线的实现提供了具体案例和方法参考。

**📖 中文摘要**

本文提出AIS-TGNN框架，将时序图注意力网络（TGAT）与结构化大语言模型（LLM）推理模块相结合，用于港口拥堵预测和可解释性分析。其创新点在于利用LLM生成基于图模型内部证据（如特征z分数、注意力权重）的自然语言解释。这项工作展示了如何将图神经网络（GNN）的表示学习能力与LLM的推理和解释能力相结合，解决一个复杂的时空预测问题。这种“GNN + LLM”的混合架构范式，可以非常直接地迁移到“化学大模型”和“质谱结构推理”任务中。例如，可以将分子表示为图，用GNN编码，然后利用LLM根据学习到的分子表示和可能的谱图特征，进行性质预测、反应推理或生成质谱解析的自然语言解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Port congestion at major maritime hubs disrupts global supply chains, yet existing prediction systems typically prioritize forecasting accuracy without providing operationally interpretable explanations. This paper proposes AIS-TGNN, an evidence-grounded framework that jointly performs congestion-escalation prediction and faithful natural-language explanation by coupling a Temporal Graph Attention Network (TGAT) with a structured large language model (LLM) reasoning module. Daily spatial graphs are constructed from Automatic Identification System (AIS) broadcasts, where each grid cell represents localized vessel activity and inter-cell interactions are modeled through attention-based message passing. The TGAT predictor captures spatiotemporal congestion dynamics, while model-internal evidence, including feature z-scores and attention-derived neighbor influence, is transformed into structured prompts that constrain LLM reasoning to verifiable model outputs. To evaluate explanatory reliability, we introduce a directional-consistency validation protocol that quantitatively measures agreement between generated narratives and underlying statistical evidence. Experiments on six months of AIS data from the Port of Los Angeles and Long Beach demonstrate that the proposed framework outperforms both LR and GCN baselines, achieving a test AUC of 0.761, AP of 0.344, and recall of 0.504 under a strict chronological split while producing explanations with 99.6% directional consistency. Results show that grounding LLM generation in graph-model evidence enables interpretable and auditable risk reporting without sacrificing predictive performance. The framework provides a practical pathway toward operationally deployable explainable AI for maritime congestion monitoring and supply-chain risk management.

</details>

---

### 23. [Multilevel Training for Kolmogorov Arnold Networks](https://arxiv.org/abs/2603.04827)

**基本信息**

- 🔗 arXiv: [`2603.04827`](https://arxiv.org/abs/2603.04827)
- 👥 作者: Ben S. Southworth, Jonas A. Actor, Graham Harper 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化一种新型神经网络架构（KANs）的训练。KANs作为基础模型架构的一种探索，其高效训练方法对于构建任何领域的大模型（包括“化学大模型”）都具有通用价值。论文为在化学领域尝试和应用此类新架构提供了技术支撑。

**📖 中文摘要**

本文针对Kolmogorov-Arnold网络（KANs）提出了一种多级训练算法，利用其基于样条基函数的固有结构，通过均匀细化样条节点和几何插值算子，实现了训练速度的显著提升。KANs作为一种新兴的神经网络架构，因其可解释性和在某些任务上的优越性能而受到关注，被视为多层感知机（MLP）的潜在替代方案。论文对KANs的高效训练方法研究，为探索新型神经网络架构在科学计算（包括化学信息学）中的应用铺平了道路。化学大模型和质谱分析模型可以受益于像KANs这样具有更好数学解释性和潜在更高效率的模型架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

</details>

---

### 24. [From Unfamiliar to Familiar: Detecting Pre-training Data via Gradient Deviations in Large Language Models](https://arxiv.org/abs/2603.04828)

**基本信息**

- 🔗 arXiv: [`2603.04828`](https://arxiv.org/abs/2603.04828)
- 👥 作者: Ruiqi Zhang, Lingxiang Wang, Hainan Zhang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04828.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）的预训练数据检测，这属于大模型数据安全和评估范畴。该研究提出的基于梯度行为的分析方法，为理解和评估“化学大模型”与其训练数据（如分子、谱图数据库）之间的关系提供了新颖的技术视角。

**📖 中文摘要**

本文提出GDS方法，通过分析目标样本在训练过程中的梯度偏差分数，来检测大语言模型（LLMs）的预训练数据。该方法基于一个优化视角的观察：在训练过程中，样本从“不熟悉”到“熟悉”的转变会系统性地反映在梯度行为上。GDS利用梯度特征（更新幅度、位置、神经元激活集中度）来区分成员数据和非成员数据。这项研究涉及大模型的数据隐私和安全。虽然直接应用场景是版权和基准污染，但其核心——通过分析模型对数据的“反应”（梯度）来推断数据属性——与“质谱结构推理”有方法论上的相似性。在质谱解析中，也需要根据模型（或规则）对谱图数据的“反应”来推断其结构。此外，确保化学大模型训练数据的质量和溯源也同样重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pre-training data detection for LLMs is essential for addressing copyright concerns and mitigating benchmark contamination. Existing methods mainly focus on the likelihood-based statistical features or heuristic signals before and after fine-tuning, but the former are susceptible to word frequency bias in corpora, and the latter strongly depend on the similarity of fine-tuning data. From an optimization perspective, we observe that during training, samples transition from unfamiliar to familiar in a manner reflected by systematic differences in gradient behavior. Familiar samples exhibit smaller update magnitudes, distinct update locations in model components, and more sharply activated neurons. Based on this insight, we propose GDS, a method that identifies pre-training data by probing Gradient Deviation Scores of target samples. Specifically, we first represent each sample using gradient profiles that capture the magnitude, location, and concentration of parameter updates across FFN and Attention modules, revealing consistent distinctions between member and non-member data. These features are then fed into a lightweight classifier to perform binary membership inference. Experiments on five public datasets show that GDS achieves state-of-the-art performance with significantly improved cross-dataset transferability over strong baselines. Further interpretability analyse show gradient feature distribution differences, enabling practical and scalable pre-training data detection.

</details>

---

### 25. [Hyperbolic Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.04848)

**基本信息**

- 🔗 arXiv: [`2603.04848`](https://arxiv.org/abs/2603.04848)
- 👥 作者: Jin Yang, Ping Wei, Yixin Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04848.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用双曲空间进行3D感知的视觉预训练，以学习结构化的嵌入表示。分子结构和化学空间天然适合用双曲空间等非欧几何进行建模。因此，该研究为“化学大模型”探索更先进的几何感知表示学习方法提供了直接的技术借鉴和理论依据。

**📖 中文摘要**

本文提出HyperMVP，一个用于机器人操作的多视图双曲空间自监督预训练框架。该框架利用双曲空间的几何特性来更好地捕捉嵌入之间的结构关系，并设计了GeoLink编码器来学习多视图双曲表示。预训练后的编码器在多种操作任务上微调后表现出更强的鲁棒性和泛化能力。虽然应用场景是机器人视觉，但其核心贡献在于探索了非欧几里得空间（双曲空间）对于学习具有层次或树状结构数据的表征优势。分子结构和化学空间通常也具有类似的层次或树状关系（如官能团、子结构）。因此，这项研究为在“化学大模型”中采用双曲空间等非欧几何来更有效地表示和推理分子结构、化学知识图谱提供了重要的前瞻性探索和可行性证明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

3D-aware visual pretraining has proven effective in improving the performance of downstream robotic manipulation tasks. However, existing methods are constrained to Euclidean embedding spaces, whose flat geometry limits their ability to model structural relations among embeddings. As a result, they struggle to learn structured embeddings that are essential for robust spatial perception in robotic applications. To this end, we propose HyperMVP, a self-supervised framework for \underline{Hyper}bolic \underline{M}ulti\underline{V}iew \underline{P}retraining. Hyperbolic space offers geometric properties well suited for capturing structural relations. Methodologically, we extend the masked autoencoder paradigm and design a GeoLink encoder to learn multiview hyperbolic representations. The pretrained encoder is then finetuned with visuomotor policies on manipulation tasks. In addition, we introduce 3D-MOV, a large-scale dataset comprising multiple types of 3D point clouds to support pretraining. We evaluate HyperMVP on COLOSSEUM, RLBench, and real-world scenarios, where it consistently outperforms strong baselines across diverse tasks and perturbation settings. Our results highlight the potential of 3D-aware pretraining in a non-Euclidean space for learning robust and generalizable robotic manipulation policies.

</details>

---

### 26. [Why Is RLHF Alignment Shallow? A Gradient Analysis](https://arxiv.org/abs/2603.04851)

**基本信息**

- 🔗 arXiv: [`2603.04851`](https://arxiv.org/abs/2603.04851)
- 👥 作者: Robin Young
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04851.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型（LLM）对齐机制的理论分析。构建安全、可靠、符合科学规范的“化学大模型”同样面临对齐挑战。论文对RLHF局限性的理论揭示，为化学领域大模型的价值对齐和安全评估提供了重要的理论基础和方向指引。

**📖 中文摘要**

本文从梯度分析的角度，理论上证明了基于强化学习人类反馈（RLHF）的大语言模型对齐方法是“浅层”的。研究指出，基于梯度的对齐本质上集中在决定危害的位置，而在此范围之外的梯度信号会消失，导致无法产生深度对齐。论文引入了“危害信息”的概念，并推导了基于恢复惩罚的新目标。这项研究属于大模型对齐和安全性的理论基础。对于旨在用于药物发现、毒性预测等领域的“化学大模型”，确保其输出符合化学常识、安全性和伦理规范（即“对齐”）至关重要。本文对现有RLHF对齐机制局限性的理论剖析，为设计和评估化学大模型的安全对齐策略提供了关键的洞见和理论指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Why is safety alignment in LLMs shallow? We prove that gradient-based alignment inherently concentrates on positions where harm is decided and vanishes beyond. Using a martingale decomposition of sequence-level harm, we derive an exact characterization of alignment gradients. The gradient at position $t$ equals the covariance between the conditional expected harm and the score function. This implies that positions beyond the harm horizon where the output's harmfulness is already determined receive zero gradient signal during training. This explains empirical observations that KL divergence between aligned and base models concentrates on early tokens. Consequently, standard alignment objectives cannot produce deep alignment, regardless of optimization quality. We introduce the concept of harm information $I_t$, which quantifies each position's influence on harm, and prove that equilibrium KL divergence tracks this quantity. Finally, we derive an objective based on recovery penalties that creates gradient signal at all positions, providing theoretical grounding for empirically successful data augmentation techniques.

</details>

---

### 27. [Free Lunch for Pass@$k$? Low Cost Diverse Sampling for Diffusion Language Models](https://arxiv.org/abs/2603.04893)

**基本信息**

- 🔗 arXiv: [`2603.04893`](https://arxiv.org/abs/2603.04893)
- 👥 作者: Sean Lamont, Christian Walder, Paul Montague 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04893.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化扩散语言模型的采样策略以提高生成多样性，用于解决代码、数学等复杂推理任务。这与“化学大模型”在分子生成、反应预测等需要探索化学空间的任务高度相关。论文提出的方法为化学领域的扩散模型提供了即插即用的多样性提升工具。

**📖 中文摘要**

本文针对扩散语言模型（Diffusion Language Models）在文本生成中输出多样性不足的问题，提出了一种无需训练、低成本的干预方法，以增强生成多样性，从而提升在代码生成、数学解题等需要探索解空间的复杂推理任务中的Pass@k性能。该方法通过顺序修改批次中的中间样本，使每个样本在特征空间上排斥之前的样本，从而主动惩罚冗余。虽然论文主要评估领域是代码和数学，但其解决的核心问题——如何让生成模型产生多样且高质量的候选解——正是“化学大模型”在分子生成、逆合成规划等任务中面临的关键挑战。论文提出的简单而有效的采样策略，可以直接应用于化学领域的扩散模型，以提高分子设计的多样性和成功率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diverse outputs in text generation are necessary for effective exploration in complex reasoning tasks, such as code generation and mathematical problem solving. Such Pass@$k$ problems benefit from distinct candidates covering the solution space. However, traditional sampling approaches often waste computational resources on repetitive failure modes. While Diffusion Language Models have emerged as a competitive alternative to the prevailing Autoregressive paradigm, they remain susceptible to this redundancy, with independent samples frequently collapsing into similar modes. To address this, we propose a training free, low cost intervention to enhance generative diversity in Diffusion Language Models. Our approach modifies intermediate samples in a batch sequentially, where each sample is repelled from the feature space of previous samples, actively penalising redundancy. Unlike prior methods that require retraining or beam search, our strategy incurs negligible computational overhead, while ensuring that each sample contributes a unique perspective to the batch. We evaluate our method on the HumanEval and GSM8K benchmarks using the LLaDA-8B-Instruct model. Our results demonstrate significantly improved diversity and Pass@$k$ performance across various temperature settings. As a simple modification to the sampling process, our method offers an immediate, low-cost improvement for current and future Diffusion Language Models in tasks that benefit from diverse solution search. We make our code available at this https URL .

</details>

---

### 28. [EvoTool: Self-Evolving Tool-Use Policy Optimization in LLM Agents via Blame-Aware Mutation and Diversity-Aware Selection](https://arxiv.org/abs/2603.04900)

**基本信息**

- 🔗 arXiv: [`2603.04900`](https://arxiv.org/abs/2603.04900)
- 👥 作者: Shuo Yang, Soyeon Caren Han, Xueqi Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大语言模型（LLM）智能体使用工具的策略。构建能够调用专业计算工具和数据库的“化学大模型”智能体是化学信息学的重要方向。论文提出的自我进化框架为开发此类化学智能体提供了先进的架构和训练范式。

**📖 中文摘要**

本文提出EvoTool，一个通过无梯度进化范式自我进化优化LLM智能体工具使用策略的框架。它将智能体的工具使用策略分解为四个模块，并通过轨迹溯因归因、反馈引导的定向突变和多样性感知的种群选择三个新机制进行迭代改进。该研究专注于提升LLM智能体使用外部工具（如API）解决复杂任务的能力。在化学信息学中，“化学大模型”智能体同样需要调用各种计算工具（如量子化学计算、数据库查询、谱图模拟软件）来完成分子设计、性质预测、谱图解析等任务。因此，EvoTool框架为构建和优化能够熟练使用化学专业工具的智能体系统提供了一个强大的、可自动进化的方法论蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-based agents depend on effective tool-use policies to solve complex tasks, yet optimizing these policies remains challenging due to delayed supervision and the difficulty of credit assignment in long-horizon trajectories. Existing optimization approaches tend to be either monolithic, which are prone to entangling behaviors, or single-aspect, which ignore cross-module error propagation. To address these limitations, we propose EvoTool, a self-evolving framework that optimizes a modular tool-use policy via a gradient-free evolutionary paradigm. EvoTool decomposes agent's tool-use policy into four modules, including Planner, Selector, Caller, and Synthesizer, and iteratively improves them in a self-improving loop through three novel mechanisms. Trajectory-Grounded Blame Attribution uses diagnostic traces to localize failures to a specific module. Feedback-Guided Targeted Mutation then edits only that module via natural-language critique. Diversity-Aware Population Selection preserves complementary candidates to ensure solution diversity. Across four benchmarks, EvoTool outperforms strong baselines by over 5 points on both GPT-4.1 and Qwen3-8B, while achieving superior efficiency and transferability. The code will be released once paper is accepted.

</details>

---

### 29. [$\nabla$-Reasoner: LLM Reasoning via Test-Time Gradient Descent in Latent Space](https://arxiv.org/abs/2603.04948)

**基本信息**

- 🔗 arXiv: [`2603.04948`](https://arxiv.org/abs/2603.04948)
- 👥 作者: Peihao Wang, Ruisi Cai, Zhen Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04948.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过测试时梯度下降等高级优化技术来增强大语言模型（LLM）的推理能力。这种提升基础模型推理性能的通用方法，可直接应用于“化学大模型”，以解决化学领域需要多步、复杂逻辑推理的任务，是前沿的模型推理优化技术。

**📖 中文摘要**

本文提出$\nabla$-Reasoner，一种在潜在空间通过测试时梯度下降进行LLM推理的迭代生成框架。其核心组件“可微分文本优化”（DTO）利用来自LLM似然和奖励模型的梯度信号来优化文本表示。论文从理论上证明了在样本空间进行测试时梯度下降以最大化奖励，与通过KL正则化强化学习对齐LLM策略是对偶的。该方法在数学推理基准上取得了显著提升。这项研究代表了一种从零阶搜索到一阶优化的范式转变，旨在以更低的成本放大LLM的推理能力。这种在推理时主动优化生成过程的先进方法，为提升“化学大模型”在复杂问题（如逆合成分析、反应条件优化）上的推理精度和效率提供了全新的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling inference-time compute for Large Language Models (LLMs) has unlocked unprecedented reasoning capabilities. However, existing inference-time scaling methods typically rely on inefficient and suboptimal discrete search algorithms or trial-and-error prompting to improve the online policy. In this paper, we propose $\nabla$-Reasoner, an iterative generation framework that integrates differentiable optimization over token logits into the decoding loop to refine the policy on the fly. Our core component, Differentiable Textual Optimization (DTO), leverages gradient signals from both the LLM's likelihood and a reward model to refine textual representations. $\nabla$-Reasoner further incorporates rejection sampling and acceleration design to robustify and speed up decoding. Theoretically, we show that performing inference-time gradient descent in the sample space to maximize reward is dual to aligning an LLM policy via KL-regularized reinforcement learning. Empirically, $\nabla$-Reasoner achieves over 20% accuracy improvement on a challenging mathematical reasoning benchmark, while reducing number of model calls by approximately 10-40% compared to strong baselines. Overall, our work introduces a paradigm shift from zeroth-order search to first-order optimization at test time, offering a cost-effective path to amplify LLM reasoning.

</details>

---

### 30. [Programmable superconducting neuron with intrinsic in-memory computation and dual-timescale plasticity for ultra-efficient neuromorphic computing](https://arxiv.org/abs/2603.04966)

**基本信息**

- 🔗 arXiv: [`2603.04966`](https://arxiv.org/abs/2603.04966)
- 👥 作者: Muen Wang, Shucheng Yang, Yuxiang Lin 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04966.pdf)

**💡 相关性分析**

满足标准3：论文讨论了集成本地内存、可编程性和多时间尺度可塑性的新型计算单元架构。这些概念对于构建下一代高效的、专门用于处理时序数据（如质谱序列）和进行复杂结构推理的“化学大模型”或专用硬件加速器具有重要的启发和展望价值。

**📖 中文摘要**

本文介绍了一种可编程的超导神经元，用于超高效神经形态计算。该神经元集成了本征内存计算和双时间尺度可塑性。虽然论文的核心是硬件和神经形态计算架构，但其提出的“事件驱动、内存内神经形态架构”以及用于快速时间适应的“皮秒级短时调制”概念，与化学信息学中处理时序数据（如质谱扫描序列）和构建具有记忆与适应能力的推理模型在理念上存在潜在关联。该工作为构建高效、专用的计算单元提供了新思路，这类单元未来可能被应用于需要快速处理大量光谱数据并进行实时推理的化学信息学系统中。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The escalating energy demands of artificial intelligence pose a critical challenge to conventional computing. Leveraging the efficiency of event-driven, in-memory neuromorphic architectures into the superconducting circuits with ultra-high speed and low power dissipation advantages offers a promising solution to energy-efficient computing. However, the potential of such a solution has yet to be realized, owning to the absence of a fundamental superconducting unit that unifies programmability, local memory, and multi-timescale plasticity. Here, we introduce a programmable Josephson-junction-based leaky integrate-and-fire (LIF) neuron that features intrinsic static memory and precise programmability by encoding somatic and synaptic parameters directly in the bias current. This neuron is also capable of dual-timescale plasticity: picosecond-scale short-term modulation of spike transmission and long-term weight retention exceeding 10,000 seconds, facilitating both rapid temporal adaptation and robust weight storage. It can operate up to 45 GHz with femtojoule-level energy dissipation per spike, and supports 10 somatic threshold levels and 20 synaptic states. Furthermore, we demonstrate a crossbar-based spiking neural network (SNN) utilizing this neuron, which achieves outstanding performance across multiple tasks. By fusing computation, memory and plasticity into a single superconducting unit, our work paves the way for the next generation of ultrafast, energy-efficient neuromorphic computing.

</details>

---

### 31. [Functionality-Oriented LLM Merging on the Fisher--Rao Manifold](https://arxiv.org/abs/2603.04972)

**基本信息**

- 🔗 arXiv: [`2603.04972`](https://arxiv.org/abs/2603.04972)
- 👥 作者: Jiayu Wang, Zuojun Ye, Wenpeng Yin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04972.pdf)

**💡 相关性分析**

满足标准3：论文提出的基于流形几何的模型功能合并框架，为如何集成多个特定领域微调的专家模型（例如，分别擅长不同类别化合物质谱解析的模型）以构建统一、强大的“化学大模型”提供了重要的技术讨论和前瞻性思路。

**📖 中文摘要**

本文提出了一种在Fisher-Rao流形上进行LLM权重空间合并的新方法，旨在合并多个微调模型的功能。该方法将模型合并表述为计算加权Karcher均值，以最小化预测分布之间的KL散度。虽然论文主要关注通用LLM的合并，但其核心是解决模型功能（预测行为）的融合问题，并提供了稳定的多专家合并算法。这一框架对于构建和集成专注于不同化学领域（如质谱解析、分子性质预测）的专家模型，以形成更强大的“化学大模型”具有方法论上的参考意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight-space merging aims to combine multiple fine-tuned LLMs into a single model without retraining, yet most existing approaches remain fundamentally parameter-space heuristics. This creates three practical limitations. First, linear averaging, task vectors, and related rules operate on Euclidean coordinates, even though the desired goal is to merge functionality, i.e., predictive behaviors across tasks. Second, when the source checkpoints are farther apart or more heterogeneous, Euclidean blends often trigger representation collapse, manifested as activation variance shrinkage and effective-rank degradation, which sharply degrades accuracy. Third, many geometry-inspired methods are most natural for two-model interpolation and do not extend cleanly to merging N>2 experts with a principled objective. We address these issues by formulating model merging as computing a weighted Karcher mean on the Fisher--Rao manifold, which is locally equivalent to minimizing a KL-based function distance between predictive distributions. We derive a practical fixed-point algorithm using a lightweight spherical proxy that preserves norms and generalizes directly to multi-expert merging. Across various benchmarks and collapse diagnostics, our method remains stable as the number and heterogeneity of merged models increase, consistently outperforming prior baselines.

</details>

---

### 32. [VMXDOTP: A RISC-V Vector ISA Extension for Efficient Microscaling (MX) Format Acceleration](https://arxiv.org/abs/2603.04979)

**基本信息**

- 🔗 arXiv: [`2603.04979`](https://arxiv.org/abs/2603.04979)
- 👥 作者: Max Wipfli, Gamze İslamoğlu, Navaneeth Kunhi Purayil 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04979.pdf)

**💡 相关性分析**

满足标准3：论文专注于为低精度、高效率的数据格式设计硬件加速指令。这直接关系到未来“化学大模型”或计算密集型质谱分析模型在嵌入式或移动设备上的部署可行性、能效和速度，属于支撑性技术的展望和讨论。

**📖 中文摘要**

本文提出了VMXDOTP，一种RISC-V向量指令集架构扩展，用于高效加速微缩放（MX）数据格式（如MXFP8, MXFP4）的运算。MX格式基于块浮点表示，能减少数据量并保持精度。论文旨在解决MX语义与向量执行之间的不对齐问题，以实现高性能、高能效的矩阵乘法等计算。这项工作为在资源受限的边缘设备上部署需要大量矩阵运算的大模型（包括潜在的化学大模型）提供了硬件层面的高效计算支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Compared to the first generation of deep neural networks, dominated by regular, compute-intensive kernels such as matrix multiplications (MatMuls) and convolutions, modern decoder-based transformers interleave attention, normalization, and data-dependent control flow. This demands flexible accelerators, a requirement met by scalable, highly energy-efficient shared-L1-memory vector processing element (VPE) clusters. Meanwhile, the ever-growing size and bandwidth needs of state-of-the-art models make reduced-precision formats increasingly attractive. Microscaling (MX) data formats, based on block floating-point (BFP) representations, have emerged as a promising solution to reduce data volumes while preserving accuracy. However, MX semantics are poorly aligned with vector execution: block scaling and multi-step mixed-precision operations break the regularity of vector pipelines, leading to underutilized compute resources and performance degradation. To address these challenges, we propose VMXDOTP, a RISC-V Vector (RVV) 1.0 instruction set architecture (ISA) extension for efficient MX dot product execution, supporting MXFP8 and MXFP4 inputs, FP32 and BF16 accumulation, and software-defined block sizes. A VMXDOTP-enhanced VPE cluster achieves up to 97 % utilization on MX-MatMul. Implemented in 12 nm FinFET, it achieves up to 125 MXFP8-GFLOPS and 250 MXFP4-GFLOPS, with 843/1632 MXFP8/MXFP4-GFLOPS/W at 1 GHz, 0.8 V, and only 7.2 % area overhead. Our design yields up to 7.0x speedup and 4.9x energy efficiency with respect to software-emulated MXFP8-MatMul. Compared with prior MX engines, VMXDOTP supports variable block sizes, is up to 1.4x more area-efficient, and delivers up to 2.1x higher energy efficiency.

</details>

---

### 33. [Enhancing Zero-shot Commonsense Reasoning by Integrating Visual Knowledge via Machine Imagination](https://arxiv.org/abs/2603.05040)

**基本信息**

- 🔗 arXiv: [`2603.05040`](https://arxiv.org/abs/2603.05040)
- 👥 作者: Hyuntae Park, Yeachan Kim, SangKeun Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05040.pdf)

**💡 相关性分析**

满足标准3：论文提出的多模态增强推理框架，为如何克服单一数据模态（如文本或数值谱图）的局限性、通过引入互补信息（如分子可视化）来提升“化学大模型”或“质谱结构推理”模型的准确性和鲁棒性，提供了重要的方法论讨论和前瞻性视角。

**📖 中文摘要**

本文提出了Imagine框架，一个零样本常识推理框架，通过集成机器生成的视觉信号来增强预训练语言模型的推理能力。框架将图像生成器嵌入推理流程，利用合成的视觉问答数据来利用视觉上下文。该方法旨在缓解文本知识中的人类报告偏差，提升模型的泛化能力。虽然应用领域是通用常识推理，但其核心思想——通过引入多模态（视觉）信息来补充和纠正单模态（文本）模型的认知偏差——对于“化学大模型”和“质谱结构推理”具有启发意义。例如，在解析质谱时，可以结合分子结构图像或光谱图等视觉信息来辅助推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in zero-shot commonsense reasoning have empowered Pre-trained Language Models (PLMs) to acquire extensive commonsense knowledge without requiring task-specific fine-tuning. Despite this progress, these models frequently suffer from limitations caused by human reporting biases inherent in textual knowledge, leading to understanding discrepancies between machines and humans. To bridge this gap, we introduce an additional modality to enrich the reasoning capabilities of PLMs. We propose Imagine (Machine Imagination-based Reasoning), a novel zero-shot commonsense reasoning framework that supplements textual inputs with visual signals from machine-generated images. Specifically, we enhance PLMs with the ability to imagine by embedding an image generator directly into the reasoning pipeline. To facilitate effective utilization of this imagined visual context, we construct synthetic datasets designed to emulate visual question-answering scenarios. Through comprehensive evaluations on multiple commonsense reasoning benchmarks, we demonstrate that Imagine substantially outperforms existing zero-shot approaches and even surpasses advanced large language models. These results underscore the capability of machine imagination to mitigate reporting bias and significantly enhance the generalization ability of commonsense reasoning models

</details>

---

### 34. [NeuronMoE: Neuron-Guided Mixture-of-Experts for Efficient Multilingual LLM Extension](https://arxiv.org/abs/2603.05046)

**基本信息**

- 🔗 arXiv: [`2603.05046`](https://arxiv.org/abs/2603.05046)
- 👥 作者: Rongzhi Li, Hitomi Yanaka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05046.pdf)

**💡 相关性分析**

满足标准3：论文通过神经元分析来指导MoE架构中专家分配的方法，以及发现的语言知识组织模式，为如何设计高效、模块化的“化学大模型”架构（例如，针对不同分析技术或化合物类别的专家模块）提供了重要的技术见解和架构设计上的展望。

**📖 中文摘要**

本文提出了NeuronMoE方法，用于高效扩展大语言模型以支持低资源语言。该方法通过分析所有Transformer组件中语言特定神经元的跨语言多样性，来指导混合专家模型中每层的专家分配。研究发现了低资源语言专家会独立发展出与高资源语言相似的神经元专业化模式，且集中在早期和晚期层。这项工作揭示了多语言模型中语言知识组织的潜在通用架构原则。对于“化学大模型”，其启示在于：可以借鉴这种神经元级别的分析，来指导构建处理不同化学子领域（如有机化学、无机化学、质谱学）或不同数据类型（如光谱、分子图、文本）的专家混合模型，实现参数高效且性能强大的专用模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Extending large language models to low-resource languages is essential for global accessibility, but training separate models per language is prohibitively expensive. Mixture-of-Experts (MoE) architectures address this by adding sparse language-specific parameters, but determining how many experts each layer needs remains an open question. Current approaches allocate experts based on layer-level similarity, yet language processing exhibits fine-grained specialization at individual neurons. We propose $\textbf{NeuronMoE}$, a method that analyzes language-specific neurons across all transformer components to guide expert allocation per layer based on empirically measured cross-lingual neuron diversity. Applied to Llama-3.2-3B for low-resource languages (Greek, Turkish, and Hungarian), this approach achieves approximately 40% average parameter reduction while matching the performance of the LayerMoE baseline. We find that low-resource language experts independently develop neuron specialization patterns mirroring the high-resource language, which are concentrated in early and late layers. This reveals potential universal architectural principles in how multilingual models organize linguistic knowledge.

</details>

---

### 35. [MCEL: Margin-Based Cross-Entropy Loss for Error-Tolerant Quantized Neural Networks](https://arxiv.org/abs/2603.05048)

**基本信息**

- 🔗 arXiv: [`2603.05048`](https://arxiv.org/abs/2603.05048)
- 👥 作者: Mikail Yayla, Akash Kumar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05048.pdf)

**💡 相关性分析**

满足标准3：论文专注于提升神经网络在非理想硬件条件下的鲁棒性，这对于未来将大型、复杂的“化学大模型”部署到实际科研或工业环境中的计算平台（可能涉及近似计算或存算一体架构）具有重要的实用意义和前瞻性讨论价值。

**📖 中文摘要**

本文提出了边际交叉熵损失（MCEL），一种新的损失函数，旨在显式地促进输出层logit级别的边际分离，以提高量化神经网络的容错能力。论文建立了容错性与分类边际之间的直接联系，并通过大量实验证明MCEL能显著提升在各种量化方案下的比特错误容忍度。这项工作对于在近似计算或易出错内存平台上可靠地部署神经网络模型至关重要。考虑到未来“化学大模型”可能需要在边缘设备或特定计算硬件上运行以进行实时质谱分析，模型的鲁棒性和对计算误差的容忍度是一个重要的实际考量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Robustness to bit errors is a key requirement for the reliable use of neural networks (NNs) on emerging approximate computing platforms and error-prone memory technologies. A common approach to achieve bit error tolerance in NNs is injecting bit flips during training according to a predefined error model. While effective in certain scenarios, training-time bit flip injection introduces substantial computational overhead, often degrades inference accuracy at high error rates, and scales poorly for larger NN architectures. These limitations make error injection an increasingly impractical solution for ensuring robustness on future approximate computing platforms and error-prone memory technologies. In this work, we investigate the mechanisms that enable NNs to tolerate bit errors without relying on error-aware training. We establish a direct connection between bit error tolerance and classification margins at the output layer. Building on this insight, we propose a novel loss function, the Margin Cross-Entropy Loss (MCEL), which explicitly promotes logit-level margin separation while preserving the favorable optimization properties of the standard cross-entropy loss. Furthermore, MCEL introduces an interpretable margin parameter that allows robustness to be tuned in a principled manner. Extensive experimental evaluations across multiple datasets of varying complexity, diverse NN architectures, and a range of quantization schemes demonstrate that MCEL substantially improves bit error tolerance, up to 15 % in accuracy for an error rate of 1 %. Our proposed MCEL method is simple to implement, efficient, and can be integrated as a drop-in replacement for standard CEL. It provides a scalable and principled alternative to training-time bit flip injection, offering new insights into the origins of NN robustness and enabling more efficient deployment on approximate computing and memory systems.

</details>

---

### 36. [CLIP-driven Zero-shot Learning with Ambiguous Labels](https://arxiv.org/abs/2603.05053)

**基本信息**

- 🔗 arXiv: [`2603.05053`](https://arxiv.org/abs/2603.05053)
- 👥 作者: Jinfu Fan, Jiangnan Li, Xiaowen Yan 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05053.pdf)

**💡 相关性分析**

满足标准3：论文提出的利用预训练多模态模型处理模糊标签的零样本学习框架，为“质谱结构推理”中如何利用不完美、有噪声或带有多种可能性的标注数据来训练模型，以及如何提升模型在未见化合物类别上的泛化能力，提供了重要的技术思路和方法论讨论。

**📖 中文摘要**

本文提出了CLIP-PZSL框架，一种新的零样本学习框架，用于处理训练样本带有模糊标签（部分标签）的情况。该方法利用CLIP提取实例和标签特征，通过语义挖掘块融合特征以提取判别性标签嵌入，并引入部分零样本损失来对齐实例和标签嵌入。虽然应用场景是通用视觉零样本学习，但其核心技术创新——利用强大的预训练多模态模型（CLIP）来处理有噪声/不完整的监督信息并提升模型泛化能力——对于化学信息学具有借鉴意义。例如，在质谱结构推理中，训练数据可能包含不精确的化合物标注或多种可能的结构候选，该框架提供了处理此类模糊性的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Zero-shot learning (ZSL) aims to recognize unseen classes by leveraging semantic information from seen classes, but most existing methods assume accurate class labels for training instances. However, in real-world scenarios, noise and ambiguous labels can significantly reduce the performance of ZSL. To address this, we propose a new CLIP-driven partial label zero-shot learning (CLIP-PZSL) framework to handle label ambiguity. First, we use CLIP to extract instance and label features. Then, a semantic mining block fuses these features to extract discriminative label embeddings. We also introduce a partial zero-shot loss, which assigns weights to candidate labels based on their relevance to the instance and aligns instance and label embeddings to minimize semantic mismatch. As the training goes on, the ground-truth labels are progressively identified, and the refined labels and label embeddings in turn help improve the semantic alignment of instance and label features. Comprehensive experiments on several datasets demonstrate the advantage of CLIP-PZSL.

</details>

---

### 37. [Cyber Threat Intelligence for Artificial Intelligence Systems](https://arxiv.org/abs/2603.05068)

**基本信息**

- 🔗 arXiv: [`2603.05068`](https://arxiv.org/abs/2603.05068)
- 👥 作者: Natalia Krawczyk, Mateusz Szczepkowski, Adrian Brodzik 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05068.pdf)

**💡 相关性分析**

满足标准3：论文系统地讨论了AI系统特有的安全威胁和防御情报框架。这对于未来开发和部署“化学大模型”及“质谱结构推理”系统时，确保其安全性、可靠性，防止恶意数据污染、模型窃取或对抗性攻击具有重要的综述和前瞻指导意义。

**📖 中文摘要**

本文探讨了网络威胁情报（CTI）如何演进以应对针对人工智能系统的安全威胁。论文分析了传统威胁情报的假设和工作流程与AI防御需求之间的差距，回顾并组织了当前AI安全知识体系，并概述了AI导向的威胁情报知识库应包含的内容，描述了针对AI供应链不同阶段和产物的具体入侵指标。随着“化学大模型”和基于AI的“质谱结构推理”系统逐渐成为重要的科研和工业工具，其安全性、对抗攻击的鲁棒性以及训练数据的完整性变得至关重要。本文的工作为保护这类化学AI系统提供了安全框架层面的讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As artificial intelligence (AI) becomes deeply embedded in critical services and everyday products, it is increasingly exposed to security threats which traditional cyber defenses were not designed to handle. In this paper, we investigate how cyber threat intelligence (CTI) may evolve to address attacks that target AI systems. We first analyze the assumptions and workflows of conventional threat intelligence with the needs of AI-focused defense, highlighting AI-specific assets and vulnerabilities. We then review and organize the current landscape of AI security knowledge. Based on this, we outline what an AI-oriented threat intelligence knowledge base should contain, describing concrete indicators of compromise (IoC) for different AI supply-chain phases and artifacts, and showing how such a knowledge base could support security tools. Finally, we discuss techniques for measuring similarity between collected indicators and newly observed AI artifacts. The review reveals gaps and quality issues in existing resources and identifies potential future research directions toward a practical threat intelligence framework tailored to AI.

</details>

---

### 38. [UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark](https://arxiv.org/abs/2603.05075)

**基本信息**

- 🔗 arXiv: [`2603.05075`](https://arxiv.org/abs/2603.05075)
- 👥 作者: Yanlin Li, Minghui Guo, Kaiwen Zhang 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05075.pdf)

**💡 相关性分析**

满足标准2：论文提出了UniM基准，这是一个大规模、高质量、涵盖7种模态的交错多模态数据集。该数据集和评估套件可作为构建和评估能够处理复杂、异构化学信息（如结构图、谱图、文本）的“化学大模型”的重要数据资源和测试基准。

**📖 中文摘要**

本文介绍了UniM基准，这是第一个统一的任意到任意交错多模态数据集，包含文本、图像、音频、视频、文档、代码和3D共7种模态的3.1万个高质量实例。该基准旨在推动能够理解任意组合交错多模态输入并生成任意交错多媒体输出的统一模型的发展。对于“化学大模型”而言，化学研究本身天然是多模态的，涉及分子结构图（图像/3D）、光谱数据（图像/数值序列）、实验步骤文本、论文文档等。UniM基准为开发和评估能够统一处理这些异构化学信息的下一代大模型提供了一个极具参考价值的测试平台和设计范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In real-world multimodal applications, systems usually need to comprehend arbitrarily combined and interleaved multimodal inputs from users, while also generating outputs in any interleaved multimedia form. This capability defines the goal of any-to-any interleaved multimodal learning under a unified paradigm of understanding and generation, posing new challenges and opportunities for advancing Multimodal Large Language Models (MLLMs). To foster and benchmark this capability, this paper introduces the UniM benchmark, the first Unified Any-to-Any Interleaved Multimodal dataset. UniM contains 31K high-quality instances across 30 domains and 7 representative modalities: text, image, audio, video, document, code, and 3D, each requiring multiple intertwined reasoning and generation capabilities. We further introduce the UniM Evaluation Suite, which assesses models along three dimensions: Semantic Correctness & Generation Quality, Response Structure Integrity, and Interleaved Coherence. In addition, we propose UniMA, an agentic baseline model equipped with traceable reasoning for structured interleaved generation. Comprehensive experiments demonstrate the difficulty of UniM and highlight key challenges and directions for advancing unified any-to-any multimodal intelligence. The project page is this https URL .

</details>

---

### 39. [TW-Sound580K: A Regional Audio-Text Dataset with Verification-Guided Curation for Localized Audio-Language Modeling](https://arxiv.org/abs/2603.05094)

**基本信息**

- 🔗 arXiv: [`2603.05094`](https://arxiv.org/abs/2603.05094)
- 👥 作者: Hao-Hui Xie, Ho-Lam Chung, Yi-Cheng Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05094.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个针对特定领域（区域性音频）的大规模、高质量音频-文本指令数据集TW-Sound580K，并配套了详细的数据构建协议。这为化学信息学领域构建类似的专业数据集（例如，特定仪器、特定化合物类别的质谱-结构对应数据集）提供了宝贵的范例和方法论。同时，其模型适配策略也具有参考意义。

**📖 中文摘要**

本文发布了TW-Sound580K，一个通过验证-生成-批判协议构建的台湾地区音频-文本指令数据集，旨在解决大型音频-语言模型在当地方言语调上的不足。该工作包含数据清洗、扩展和模型微调（Tai-LALM）的全流程。虽然聚焦于方言音频，但其核心贡献在于提出了一套针对特定领域（区域性语言）数据稀缺问题的数据收集、验证和增强的方法论，以及一个动态双ASR仲裁策略以优化推理时的转录选择。这套数据工程和模型适配方案对于构建面向特定化学领域（如特定类别的质谱数据）或解决数据稀缺问题（如小众化合物谱图）的“化学大模型”或“质谱结构推理”模型具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Audio-Language Models (LALMs) typically struggle with localized dialectal prosody due to the scarcity of specialized corpora. We present TW-Sound580K, a Taiwanese audio-text instruction dataset developed through a Verify-Generate-Critique (VGC) protocol. This pipeline leverages Dual-ASR validation to filter 522K raw clips, subsequently expanding them into 580,000 high-fidelity instruction pairs using a teacher model. The dataset's utility is demonstrated through Tai-LALM, which fine-tunes a DeSTA 2.5-Audio-initialized backbone and incorporates a dynamic Dual-ASR Arbitration strategy to optimize transcription selection during inference. On the TAU Benchmark, Tai-LALM reaches 49.1% accuracy, marking a 6.5% absolute improvement over the zero-shot baseline (42.6% with ASR text conditioning). This confirms that integrating regional corpora with rigorous curation and dynamic arbitration significantly enhances LALM performance on localized speech.

</details>

---

### 40. [ARC-TGI: Human-Validated Task Generators with Reasoning Chain Templates for ARC-AGI](https://arxiv.org/abs/2603.05099)

**基本信息**

- 🔗 arXiv: [`2603.05099`](https://arxiv.org/abs/2603.05099)
- 👥 作者: Jens Lehmann, Syeda Khushbakht, Nikoo Salehfard 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05099.pdf)

**💡 相关性分析**

满足标准2：论文提出了ARC-TGI框架，这是一个用于生成具有复杂潜在规则的多样化任务的工具。该框架可用于为“化学大模型”或“质谱结构推理”模型生成合成训练或测试数据，例如模拟质谱碎裂规则或分子结构变换规律，从而提供可控、可扩展的数据资源来增强模型的抽象推理能力。

**📖 中文摘要**

本文介绍了ARC-TGI，一个用于抽象与推理语料库的任务生成器开源框架。它通过紧凑的Python程序来采样多样化的任务，同时保留潜在的规则。每个生成的任务都配有自然语言输入和转换推理链，以及部分实现的采样、转换和情节构建代码。该框架支持任务级约束，确保训练示例共同暴露推断底层规则所需的变化。这项工作旨在解决ARC-AGI评估中存在的过拟合和记忆化问题，通过可扩展的数据集采样实现受控的基准测试。对于“化学大模型”和“质谱结构推理”，其价值在于提供了一种生成具有复杂、抽象规则（类似于化学反应规则或质谱碎裂规律）的合成数据的方法论，可用于增强模型的推理和泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Abstraction and Reasoning Corpus (ARC-AGI) probes few-shot abstraction and rule induction on small visual grids, but progress is difficult to measure on static collections of hand-authored puzzles due to overfitting, dataset leakage, and memorisation. We introduce ARC-TGI (ARC Task Generators Inventory), an open-source framework for task-family generators: compact Python programs that sample diverse ARC-AGI tasks while preserving a latent rule. ARC-TGI is built around a solver-facing representation: each generated task is paired with natural-language input and transformation reasoning chains and partially evaluated Python code implementing sampling, transformation, and episode construction. Crucially, ARC-TGI supports task-level constraints so that training examples collectively expose the variations needed to infer the underlying rule, a requirement for human-solvable ARC tasks that independent per-example sampling often fails to guarantee. All generators undergo human refinement and local verification to keep both grids and reasoning traces natural and consistent under variation. We release 461 generators covering 180 ARC-Mini tasks, 215 ARC-AGI-1 tasks (200 train, 15 test), and 66 ARC-AGI-2 tasks (55 train, 11 test), enabling scalable dataset sampling and controlled benchmarking.

</details>

---

### 41. [Diff-ES: Stage-wise Structural Diffusion Pruning via Evolutionary Search](https://arxiv.org/abs/2603.05105)

**基本信息**

- 🔗 arXiv: [`2603.05105`](https://arxiv.org/abs/2603.05105)
- 👥 作者: Zongfang Liu, Shengkun Tang, Zongliang Wu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05105.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个针对扩散模型的高效结构化剪枝框架。这对于未来可能基于扩散模型架构构建的、参数庞大的“化学大模型”（用于分子设计、谱图预测等）的实际部署至关重要，为其模型压缩和加速提供了前沿的技术讨论和解决方案展望。

**📖 中文摘要**

本文提出了Diff-ES，一种通过进化搜索进行阶段式结构化扩散模型剪枝的框架。该方法将扩散轨迹划分为多个阶段，自动发现最优的阶段式稀疏度调度，并通过内存高效的权重路由动态激活阶段条件权重，而无需复制模型参数。Diff-ES旨在平衡扩散模型的加速与生成质量。考虑到扩散模型在分子生成、谱图生成等化学信息学任务中展现出潜力，未来可能出现基于扩散模型的“化学大模型”。Diff-ES为这类大模型的高效压缩和部署提供了先进的结构化剪枝方案，有助于降低其计算成本和推理延迟。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have achieved remarkable success in high-fidelity image generation but remain computationally demanding due to their multi-step denoising process and large model sizes. Although prior work improves efficiency either by reducing sampling steps or by compressing model parameters, existing structured pruning approaches still struggle to balance real acceleration and image quality preservation. In particular, prior methods such as MosaicDiff rely on heuristic, manually tuned stage-wise sparsity schedules and stitch multiple independently pruned models during inference, which increases memory overhead. However, the importance of diffusion steps is highly non-uniform and model-dependent. As a result, schedules derived from simple heuristics or empirical observations often fail to generalize and may lead to suboptimal performance. To this end, we introduce \textbf{Diff-ES}, a stage-wise structural \textbf{Diff}usion pruning framework via \textbf{E}volutionary \textbf{S}earch, which optimizes the stage-wise sparsity schedule and executes it through memory-efficient weight routing without model duplication. Diff-ES divides the diffusion trajectory into multiple stages, automatically discovers an optimal stage-wise sparsity schedule via evolutionary search, and activates stage-conditioned weights dynamically without duplicating model parameters. Our framework naturally integrates with existing structured pruning methods for diffusion models including depth and width pruning. Extensive experiments on DiT and SDXL demonstrate that Diff-ES consistently achieves wall-clock speedups while incurring minimal degradation in generation quality, establishing state-of-the-art performance for structured diffusion model pruning.

</details>

---

### 42. [Bidirectional Curriculum Generation: A Multi-Agent Framework for Data-Efficient Mathematical Reasoning](https://arxiv.org/abs/2603.05120)

**基本信息**

- 🔗 arXiv: [`2603.05120`](https://arxiv.org/abs/2603.05120)
- 👥 作者: Boren Hu, Xiao Liu, Boci Peng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05120.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个新颖的自适应、双向课程生成框架，用于提升数据效率。这对于训练数据获取成本高昂的“化学大模型”和“质谱结构推理”模型（需要专家标注的谱图-结构对）具有重要的方法论启示，为如何智能地组织训练过程以用更少数据达到更好性能提供了前瞻性思路。

**📖 中文摘要**

本文提出了双向课程生成框架，一个多智能体框架，用于数据高效的数学推理。与标准的单向（从易到难）课程学习不同，该框架建立了一个封闭的反馈循环，动态生成数据：要么复杂化问题以挑战模型，要么简化问题以修复特定的推理失败。这种方法确保了模型在任何阶段都只消耗最有效的数据，从而优化学习轨迹。该工作旨在最大化每个训练样本的教学价值。对于“化学大模型”和“质谱结构推理”模型的训练，特别是在高质量标注数据稀缺的情况下，这种自适应、双向的课程生成策略为如何更高效地利用现有数据、构建最优训练序列提供了创新的方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Enhancing mathematical reasoning in Large Language Models typically demands massive datasets, yet data efficiency remains a critical bottleneck. While Curriculum Learning attempts to structure this process, standard unidirectional approaches (simple-to-complex) suffer from inefficient sample utilization: they blindly escalate complexity even when foundational gaps persist, leading to wasted computation on unsolvable problems. To maximize the instructional value of every training sample, we introduce a novel Bidirectional Curriculum Generation framework. Unlike rigid trajectories, our multi-agent ecosystem mimics adaptive pedagogy to establish a closed feedback loop. It dynamically generates data by either complicating problems to challenge the model or, crucially, simplying them to repair specific reasoning failures. This mechanism ensures that the model consumes only the most effective data at any given stage. Grounded in the Optimal Pacing Theorem, our approach optimizes the learning trajectory, significantly outperforming baselines while achieving superior reasoning performance with substantially fewer instruction samples.

</details>

---

### 43. [Measuring the Redundancy of Decoder Layers in SpeechLLMs](https://arxiv.org/abs/2603.05121)

**基本信息**

- 🔗 arXiv: [`2603.05121`](https://arxiv.org/abs/2603.05121)
- 👥 作者: Adel Moumen, Guangzhi Sun, Philip C Woodland
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05121.pdf)

**💡 相关性分析**

满足标准3：论文通过实证研究发现并分析了SpeechLLM中解码器层的冗余性和全局结构。这一发现为未来设计“化学大模型”的架构（特别是基于适配LLM的架构）提供了重要参考，提示我们可以通过分析模型冗余来优化模型效率，实现更紧凑、部署成本更低的专业大模型。

**📖 中文摘要**

本文研究了语音大语言模型中解码器层的冗余性。研究表明，解码器冗余很大程度上是从预训练LLM继承而来的：文本和语音输入会产生类似的冗余块。通过剪枝解码器层和分析剪枝后的修复，论文发现大型模型（7-8B）在仅保留60%解码器层时仍能保持良好的ASR性能，并且相同的冗余层块模式在不同语音编码器、任务和语言中保持一致。这项工作表明SpeechLLM中存在全局冗余结构。这对于构建高效的“化学大模型”有借鉴意义：如果化学领域的大模型也基于类似的“编码器-大语言模型解码器”架构，那么可能也存在显著的解码器冗余，可以通过结构化剪枝来大幅减少参数量和计算开销，而不明显损失性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech Large Language Models route speech encoder representations into an LLM decoder that typically accounts for over 90% of total parameters. We study how much of this decoder capacity is actually needed for speech tasks. Across two LLM families and three scales (1-8B), we show that decoder redundancy is largely inherited from the pretrained LLM: text and speech inputs yield similar redundant blocks. We then measure excess capacity by pruning decoder layers and analysing post-pruning healing to increase robustness. Our findings show that 7-8B models retain good ASR performance with only 60% of decoder layers, and the same trend extends to smaller scales with reduced pruning tolerance. We then generalise to speech translation, and show that the same blocks of layers are redundant across speech encoders, tasks and languages, indicating that a more global redundancy structure exists, enabling a single pruned and multi-tasks SpeechLLM backbone to be deployed.

</details>

---

### 44. [Preserving Continuous Symmetry in Discrete Spaces: Geometric-Aware Quantization for SO(3)-Equivariant GNNs](https://arxiv.org/abs/2603.05343)

**基本信息**

- 🔗 arXiv: [`2603.05343`](https://arxiv.org/abs/2603.05343)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕等变图神经网络（GNNs）的压缩与加速，这是构建用于分子模拟的“化学大模型”的关键底层技术。论文明确在分子数据集（rMD17）上进行评估，并讨论其在分子动力学模拟中的应用。

**📖 中文摘要**

本文提出了一种几何感知量化（GAQ）框架，用于压缩和加速等变图神经网络（GNNs），同时严格保持离散空间中的连续对称性。该方法的核心贡献包括：1）将不变长度与等变方向解耦的幅度-方向解耦量化（MDDQ）方案，以保持几何保真度；2）对标量和向量特征采用不同量化策略的对称感知训练策略；3）用于稳定低比特状态下梯度的鲁棒注意力归一化机制。实验在rMD17基准上进行，证明了其有效性。该研究直接针对分子模拟中的等变GNNs，这是化学信息学中构建和处理分子表示（化学大模型）的核心技术之一。因此，该论文与“化学大模型”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant Graph Neural Networks (GNNs) are essential for physically consistent molecular simulations but suffer from high computational costs and memory bottlenecks, especially with high-order representations. While low-bit quantization offers a solution, applying it naively to rotation-sensitive features destroys the SO(3)-equivariant structure, leading to significant errors and violations of conservation laws. To address this issue, in this work, we propose a Geometric-Aware Quantization (GAQ) framework that compresses and accelerates equivariant models while rigorously preserving continuous symmetry in discrete spaces. Our approach introduces three key contributions: (1) a Magnitude-Direction Decoupled Quantization (MDDQ) scheme that separates invariant lengths from equivariant orientations to maintain geometric fidelity; (2) a symmetry-aware training strategy that treats scalar and vector features with distinct quantization schedules; and (3) a robust attention normalization mechanism to stabilize gradients in low-bit regimes. Experiments on the rMD17 benchmark demonstrate that our W4A8 models match the accuracy of FP32 baselines (9.31 meV vs. 23.20 meV) while reducing Local Equivariance Error (LEE) by over 30x compared to naive quantization. On consumer hardware, GAQ achieves 2.39x inference speedup and 4x memory reduction, enabling stable, energy-conserving molecular dynamics simulations for nanosecond timescales.

</details>

---

### 45. [On the Necessity of Learnable Sheaf Laplacians](https://arxiv.org/abs/2603.05395)

**基本信息**

- 🔗 arXiv: [`2603.05395`](https://arxiv.org/abs/2603.05395)
- 👥 作者: Ferran Hernandez Caralt, Mar Gonzàlez i Català, Adrián Bazaga 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05395.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是层神经网络（SNNs），这是图神经网络（GNNs）的一个重要变体。GNNs是构建“化学大模型”（用于分子表示学习、性质预测等）最主流和核心的架构之一。论文对SNN设计原则的探讨与优化化学领域GNN模型的研究直接相关。

**📖 中文摘要**

本文研究了层神经网络（SNNs）作为图卷积网络（GNNs）的扩展，旨在通过将层附加到输入图并用层拉普拉斯算子替换基于邻接的算子来解决异配图上的过平滑问题。作者引入了一个恒等层网络基线，其中所有限制映射都固定为恒等映射，并用于消融研究。论文在五个流行的异配图基准上进行了实验。虽然SNNs最初是为图数据设计的，但其核心思想——通过引入额外的几何或代数结构（层）来增强图神经网络的表现力和泛化能力——与构建更强大、更具解释性的“化学大模型”（用于分子图）的研究方向在方法论上紧密相关。该工作探讨了层学习是否必要，这直接关系到如何为分子等结构化数据设计更有效的神经网络架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sheaf Neural Networks (SNNs) were introduced as an extension of Graph Convolutional Networks to address oversmoothing on heterophilous graphs by attaching a sheaf to the input graph and replacing the adjacency-based operator with a sheaf Laplacian defined by (learnable) restriction maps. Prior work motivates this design through theoretical properties of sheaf diffusion and the kernel of the sheaf Laplacian, suggesting that suitable non-identity restriction maps can avoid representations converging to constants across connected components. Since oversmoothing can also be mitigated through residual connections and normalization, we revisit a trivial sheaf construction to ask whether the additional complexity of learning restriction maps is necessary. We introduce an Identity Sheaf Network baseline, where all restriction maps are fixed to the identity, and use it to ablate the empirical improvements reported by sheaf-learning architectures. Across five popular heterophilic benchmarks, the identity baseline achieves comparable performance to a range of SNN variants. Finally, we introduce the Rayleigh quotient as a normalized measure for comparing oversmoothing across models and show that, in trained networks, the behavior predicted by the diffusion-based analysis of SNNs is not reflected empirically. In particular, Identity Sheaf Networks do not appear to suffer more significant oversmoothing than their SNN counterparts.

</details>

---

### 46. [An interpretable prototype parts-based neural network for medical tabular data](https://arxiv.org/abs/2603.05423)

**基本信息**

- 🔗 arXiv: [`2603.05423`](https://arxiv.org/abs/2603.05423)
- 👥 作者: Jacek Karolczak, Jerzy Stefanowski
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05423.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于医疗表格数据的可解释原型学习模型。虽然应用领域是医疗，但其核心方法论——构建可解释的、基于原型的深度学习模型——与化学信息学中构建可解释的“化学大模型”（用于分子性质预测、反应分析等）的研究目标高度一致，属于同一类机器学习范式。

**📖 中文摘要**

本文提出了一种新的用于表格数据（特别是医疗记录）的可解释原型部件神经网络模型。该模型受到计算机视觉中原型部件深度神经网络发展的启发，通过对描述患者的特征进行可训练的“分块”处理，从结构化数据中学习有意义的原型部件。这些部件表示为二进制或离散化的特征子集，使得模型能够以人类可读的术语表达原型，从而实现与临床语言和基于案例的推理的对齐。该神经网络本质上是可解释的，并通过在网络的潜在空间中将患者描述与学习到的原型进行比较，提供基于概念的可解释预测。实验表明，该模型在医学基准数据集上的分类性能与广泛使用的基线模型具有竞争力，同时提供了透明度。该工作属于可解释AI在化学和生物医学信息学中的应用范畴，其“原型学习”和“概念可解释性”的思想对于构建可信的“化学大模型”（例如，用于药物发现或临床决策支持）具有重要参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The ability to interpret machine learning model decisions is critical in such domains as healthcare, where trust in model predictions is as important as their accuracy. Inspired by the development of prototype parts-based deep neural networks in computer vision, we propose a new model for tabular data, specifically tailored to medical records, that requires discretization of diagnostic result norms. Unlike the original vision models that rely on the spatial structure, our method employs trainable patching over features describing a patient, to learn meaningful prototypical parts from structured data. These parts are represented as binary or discretized feature subsets. This allows the model to express prototypes in human-readable terms, enabling alignment with clinical language and case-based reasoning. Our proposed neural network is inherently interpretable and offers interpretable concept-based predictions by comparing the patient's description to learned prototypes in the latent space of the network. In experiments, we demonstrate that the model achieves classification performance competitive to widely used baseline models on medical benchmark datasets, while also offering transparency, bridging the gap between predictive performance and interpretability in clinical decision support.

</details>

---

### 47. [AbAffinity: A Large Language Model for Predicting Antibody Binding Affinity against SARS-CoV-2](https://arxiv.org/abs/2603.04480)

**基本信息**

- 🔗 arXiv: [`2603.04480`](https://arxiv.org/abs/2603.04480)
- 👥 作者: Faisal Bin Ashraf, Animesh Ray, Stefano Lonardi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04480.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个名为AbAffinity的大型语言模型（LLM），用于预测抗体-抗原结合亲和力。这直接属于“化学大模型”或“生物大模型”在计算生物化学和药物发现中的应用。

**📖 中文摘要**

本研究介绍了AbAffinity，一种新的大型语言模型，用于准确预测抗体与目标肽（例如SARS-CoV-2刺突蛋白）的结合亲和力。作者指出，基于机器学习的抗体设计因人工智能领域的显著进步和实验抗体数据（特别是与COVID-19相关的数据）的指数级增长而成为最有前景的方法之一。抗体与抗原的结合能力（称为结合亲和力）是设计中和抗体的最关键特性之一。该工作直接应用大语言模型（LLM）技术来解决生物分子（抗体）的关键性质预测问题，是“化学大模型”或更广义的“科学大模型”在生物化学和药物发现领域的典型实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning-based antibody design is emerging as one of the most promising approaches to combat infectious diseases, due to significant advancements in the field of artificial intelligence and an exponential surge in experimental antibody data (in particular related to COVID-19). The ability of an antibody to bind to an antigens (called binding affinity) is one of the the most critical properties in designing neutralizing antibodies. In this study we introduce Ab-Affinity, a new large language model that can accurately predict the binding affinity of antibodies against a target peptide, e.g., the SARS-CoV-2 spike protein. Code and model are available at this https URL .

</details>

---

### 48. [Projected Hessian Learning: Fast Curvature Supervision for Accurate Machine-Learning Interatomic Potentials](https://arxiv.org/abs/2603.04523)

**基本信息**

- 🔗 arXiv: [`2603.04523`](https://arxiv.org/abs/2603.04523)
- 👥 作者: Austin Rodriguez, Justin S. Smith, Sakib Matin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04523.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习原子间势（MLIPs）的训练框架。MLIPs是计算化学和材料科学中用于模拟分子和材料体系的“化学大模型”的核心组成部分。论文提出的PHL方法旨在提高这类模型的训练效率和准确性。

**📖 中文摘要**

本文介绍了投影Hessian学习（PHL），一种用于机器学习原子间势（MLIPs）的可扩展二阶训练框架。Hessian矩阵（二阶导数）比能量和力编码了势能面更丰富的局部曲率信息。然而，使用完整的Hessian矩阵训练MLIPs通常不切实际，因为显式形成和存储Hessian矩阵在成本和内存上呈二次方增长。PHL通过仅使用Hessian-向量积（HVPs）来注入曲率信息，从而实现了基于曲率的训练，而没有二次内存增长。作者在化学多样化的数据集上对PHL进行了基准测试，该数据集包含在omegaB97XD/6-31G(d)水平上计算的反应物、产物、过渡态、内禀反应坐标和简正模采样几何结构。该研究专注于改进机器学习原子间势（MLIPs）的训练，而MLIPs是计算化学和材料科学中“化学大模型”的一种重要形式，用于准确、高效地模拟原子系统的势能面和动力学。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hessian matrix (second derivatives) encodes far richer local curvature of the potential energy surface than energies and forces alone. However, training machine-learning interatomic potentials (MLIPs) with full Hessians is often impractical because explicitly forming and storing Hessian matrices scales quadratically in cost and memory. We introduce Projected Hessian Learning (PHL), a scalable second-order training framework that injects curvature information using only Hessian-vector products (HVPs). Rather than constructing the Hessian, PHL projects curvature along stochastic probe directions and uses an unbiased stochastic trace-based loss with favorable system-size scaling, enabling curvature-informed training without quadratic memory growth. We benchmark PHL on a chemically diverse dataset of reactants, products, transition states, intrinsic reaction coordinates, and normal-mode sampled geometries computed at omegaB97XD/6-31G(d). We compare energy-force training (E-F), two HVP-based schemes (E-F-HVP with one-hot or randomized probes), and full energy-force-Hessian training (E-F-H). With randomized probes per minibatch, both HVP schemes match full-Hessian training in energy, force, and Hessian accuracy while delivering >24x epoch speedups for the small molecular systems studied. In a fixed-probe regime with one HVP per molecule, randomized projections consistently outperform one-column probing, especially for far-from-equilibrium geometries. Overall, PHL replaces explicit Hessian supervision with force-complexity curvature training, retaining most second-order accuracy gains while scaling to larger, more complex molecular systems.

</details>

---

### 49. [Estimation of Persistence Diagrams via the Three Gap Theorem](https://arxiv.org/abs/2603.04570)

**基本信息**

- 🔗 arXiv: [`2603.04570`](https://arxiv.org/abs/2603.04570)
- 👥 作者: Luis Suarez Salas, Jose A. Perea
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04570.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的、快速且可证明正确的持久同调（持久性图）近似计算方法。持久同调是拓扑数据分析（TDA）的核心工具，而TDA在化学信息学中被广泛用于分子表征、比较和性质预测。该方法为化学信息学中处理复杂分子结构数据提供了一种新的潜在计算工具。

**📖 中文摘要**

本文提出了利用数论中的三间隔定理和TDA中的持久Künneth公式，来近似准周期函数滑动窗口嵌入的持久性图的理论和计算方案。时间延迟（或滑动窗口）嵌入是一种从时间序列数据重建吸引子的动力系统技术。最近，拓扑数据分析（TDA）的描述符——特别是持久性图——已被用于测量所述重建吸引子的形状，应用于周期性、准周期性量化等领域。该工作虽然主要面向时间序列和动力系统，但其核心工具——持久同调（Persistent Homology）和持久性图——是拓扑数据分析（TDA）的关键组成部分。TDA在化学信息学中有着广泛应用，例如用于分析分子的拓扑特征（如持久同调用于分子表征）、比较分子形状、以及研究蛋白质结构等。因此，该论文提出的持久性图计算新方法，为相关领域提供了新的工具和思路，可被视为一种潜在的“数据资源相关”或“工具相关”的研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The time delay (or Sliding Window) embedding is a technique from dynamical systems to reconstruct attractors from time series data. Recently, descriptors from Topological Data Analysis (TDA) -- specifically, persistence diagrams -- have been used to measure the shape of said reconstructed attractors in applications including periodicity and quasiperiodicity quantification. Despite their utility, the fast computation of persistence diagrams of sliding window embeddings is still poorly understood. In this work, we present theoretical and computational schemes to approximate the persistence diagrams of sliding window embeddings from quasiperiodic functions. We do so by combining the Three Gap Theorem from number theory with the Persistent Künneth formula from TDA, and derive fast and provably correct persistent homology approximations. The input to our procedure is the spectrum of the signal, and we provide numerical as well as theoretical evidence of its utility to capture the shape of toroidal attractors.

</details>

---

### 50. [Particle-Guided Diffusion for Gas-Phase Reaction Kinetics](https://arxiv.org/abs/2603.05139)

**基本信息**

- 🔗 arXiv: [`2603.05139`](https://arxiv.org/abs/2603.05139)
- 👥 作者: Andrew Millard, Henrik Pedersen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用生成模型（扩散模型）解决化学动力学问题，与'化学大模型'主题直接相关。

**📖 中文摘要**

本文提出了一种基于扩散模型的粒子引导采样方法，用于解决气相化学反应动力学中的偏微分方程（PDE）控制问题。该方法在变化的参数条件下，对平流-反应-扩散（ARD）方程的解进行训练，以生成物理上一致的浓度场并准确预测出口浓度，包括在未见过的参数值下。这项工作展示了扩散模型在反应输运系统中进行推理的潜力，属于利用生成模型（扩散模型）解决化学动力学问题的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-guided sampling with diffusion model priors has shown promise for solving partial differential equation (PDE) governed problems, but applications to chemically meaningful reaction-transport systems remain limited. We apply diffusion-based guided sampling to gas-phase chemical reactions by training on solutions of the advection-reaction-diffusion (ARD) equation across varying parameters. The method generates physically consistent concentration fields and accurately predicts outlet concentrations, including at unseen parameter values, demonstrating the potential of diffusion models for inference in reactive transport.

</details>

---

### 51. [Escaping the Hydrolysis Trap: An Agentic Workflow for Inverse Design of Durable Photocatalytic Covalent Organic Frameworks](https://arxiv.org/abs/2603.05188)

**基本信息**

- 🔗 arXiv: [`2603.05188`](https://arxiv.org/abs/2603.05188)
- 👥 作者: Iman Peivaste, Nicolas D. Boscher, Ahmed Makradi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05188.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）作为智能体进行化学材料的逆向设计，直接围绕'化学大模型'主题。

**📖 中文摘要**

本文针对共价有机框架（COFs）光催化剂设计中存在的稳定性-活性权衡问题，引入了一个名为Ara的大型语言模型（LLM）智能体。该智能体利用预训练的化学知识、给体-受体理论、共轭效应和连接键稳定性层次结构，来指导搜索同时满足带隙、带边和水解稳定性标准的COFs。Ara通过结合化学先验知识，在由不同节点、连接体、连接键和R基团组成的候选空间中，实现了比随机搜索和贝叶斯优化更高的命中率。这项工作展示了LLM化学先验知识如何显著加速多标准材料发现，属于利用大语言模型（LLM）进行化学逆向设计的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Covalent organic frameworks (COFs) are promising photocatalysts for solar hydrogen production, yet the most electronically favorable linkages, imines, hydrolyze rapidly in water, creating a stability--activity trade-off that limits practical deployment. Navigating the combinatorial design space of nodes, linkers, linkages, and functional groups to identify candidates that are simultaneously active and durable remains a formidable challenge. Here we introduce Ara, a large-language-model (LLM) agent that leverages pretrained chemical knowledge, donor--acceptor theory, conjugation effects, and linkage stability hierarchies, to guide the search for photocatalytic COFs satisfying joint band-gap, band-edge, and hydrolytic-stability criteria. Evaluated against random search and Bayesian optimization (BO) over a space consisting of candidates with various nodes, linkers, linkages, and r-groups, screened with a GFN1-xTB fragment pipeline, Ara achieves a 52.7\% hit rate (11.5$\times$ random, p = 0.006), finds its first hit at iteration 12 versus 25 for random search, and significantly outperforms BO (p = 0.006). Inspection of the agent's reasoning traces reveals interpretable chemical logic: early convergence on vinylene and beta-ketoenamine linkages for stability, node selection informed by electron-withdrawing character, and systematic R-group optimization to center the band gap at 2.0 eV. Exhaustive evaluation of the full search space uncovers a complementary exploitation--exploration trade-off between the agent and BO, suggesting that hybrid strategies may combine the strengths of both approaches. These results demonstrate that LLM chemical priors can substantially accelerate multi-criteria materials discovery.

</details>

---

### 52. [Generative Models in Decision Making: A Survey](https://arxiv.org/abs/2502.17100)

**基本信息**

- 🔗 arXiv: [`2502.17100`](https://arxiv.org/abs/2502.17100)
- 👥 作者: Xinyu Shao, Jianping Zhang, Haozhi Wang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.17100.pdf)

**💡 相关性分析**

满足标准3：论文是一篇专门针对生成模型（作为一类大模型）在决策和推理中应用的综述，包含了对该主题的重要讨论。

**📖 中文摘要**

本文是一篇关于生成模型在决策制定中应用的综述。它探讨了生成模型如何通过将决策问题从纯粹的标量奖励最大化重新定义为高保真轨迹生成和分布匹配，从而重塑了决策制定的格局。该综述提出了一个基于“控制即推理”概率框架的原则性分类法，将生成决策制定概念化为四个不同的功能角色：控制器、建模器、优化器和评估器。文章分析了代表性生成模型家族，并考察了在具身AI、自动驾驶和AI for Science等高风险领域的部署。这篇综述全面涵盖了生成模型（作为一类重要的“大模型”）在决策和推理中的应用、挑战和未来方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have fundamentally reshaped the landscape of decision-making, reframing the problem from pure scalar reward maximization to high-fidelity trajectory generation and distribution matching. This paradigm shift addresses intrinsic limitations in classical Reinforcement Learning (RL), particularly the limited expressivity of standard unimodal policy distributions in capturing complex, multi-modal behaviors embedded in diverse datasets. However, current literature often treats these models as isolated algorithmic improvements, rarely synthesizing them into a single comprehensive framework. This survey proposes a principled taxonomy grounding generative decision-making within the probabilistic framework of Control as Inference. By performing a variational factorization of the trajectory posterior, we conceptualize four distinct functional roles: Controllers for amortized policy inference, Modelers for dynamics priors, Optimizers for iterative trajectory refinement, and Evaluators for trajectory guidance and value assessment. Unlike existing architecture-centric reviews, this function-centric framework allows us to critically analyze representative generative families across distinct dimensions. Furthermore, we examine deployment in high-stakes domains, specifically Embodied AI, Autonomous Driving, and AI for Science, highlighting systemic risks such as dynamics hallucination in world models and proxy exploitation. Finally, we chart the path toward Generalist Physical Intelligence, identifying pivotal challenges in inference efficiency, trustworthiness, and the emergence of Physical Foundation Models.

</details>

---

### 53. [GIT-BO: High-Dimensional Bayesian Optimization with Tabular Foundation Models](https://arxiv.org/abs/2505.20685)

**基本信息**

- 🔗 arXiv: [`2505.20685`](https://arxiv.org/abs/2505.20685)
- 👥 作者: Rosen Ting-Ying Yu, Cyril Picard, Faez Ahmed
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.20685.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用表格基础模型（TabPFN v2）来增强高维贝叶斯优化中的推理能力，与利用大模型进行复杂推理的主题相关。

**📖 中文摘要**

本文提出GIT-BO，一个梯度信息化的贝叶斯优化框架，用于解决高维优化问题。它结合了TabPFN v2（一种在上下文中执行零样本贝叶斯推理的表格基础模型）和一个基于模型自身预测均值梯度计算的活动子空间机制。该方法通过费舍尔信息估计将探索与内在低维子空间对齐，并使用UCB采集函数选择查询点，无需在线重新训练。论文在多达500维的基准问题上进行了评估。这项工作展示了如何利用表格基础模型（一种特定类型的机器学习模型）来增强高维优化中的推理能力，属于利用预训练模型进行复杂推理任务的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian optimization (BO) struggles in high dimensions, where Gaussian-process surrogates demand heavy retraining and brittle assumptions, slowing progress on real engineering and design problems. We introduce GIT-BO, a Gradient-Informed BO framework that couples TabPFN v2, a tabular foundation model that performs zero-shot Bayesian inference in context, with an active-subspace mechanism computed from the model's own predictive-mean gradients. This aligns exploration to an intrinsic low-dimensional subspace via a Fisher-information estimate and selects queries with a UCB acquisition, requiring no online retraining. Across 60 problem variants spanning 20 benchmarks-nine scalable synthetic families and ten real-world tasks (e.g., power systems, Rover, MOPTA08, Mazda)-up to 500 dimensions, GIT-BO delivers a stronger performance-time trade-off than state-of-the-art GP-based methods (SAASBO, TuRBO, Vanilla BO, BAxUS), ranking highest in performance and with runtime advantages that grow with dimensionality. Limitations include memory footprint and dependence on the capacity of the underlying TFM.

</details>

---

### 54. [SealQA: Raising the Bar for Reasoning in Search-Augmented Language Models](https://arxiv.org/abs/2506.01062)

**基本信息**

- 🔗 arXiv: [`2506.01062`](https://arxiv.org/abs/2506.01062)
- 👥 作者: Thinh Pham, Nguyen Nguyen, Pratibha Zunjare 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.01062.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统性地评估和揭示大型语言模型在复杂推理任务（如处理冲突/噪声信息）中的能力与局限性，直接围绕模型推理主题。

**📖 中文摘要**

本文引入了SealQA，一个新的挑战性基准，用于评估搜索增强语言模型在事实寻求性问题上的表现，特别是当网络搜索产生冲突、嘈杂或无益结果时。该基准包含三个变体：Seal-0（主要）、Seal-Hard和LongSeal，分别评估事实准确性、推理能力和长上下文多文档推理。评估揭示了当前前沿LLM（如GPT-4.1, o3-mini, DeepSeek-R1-671B等）在处理此类具有挑战性的推理任务时的显著局限性。这项工作系统地评估了大型语言模型在复杂、真实世界推理场景中的能力，直接关联到模型推理性能的评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce SealQA, a new challenge benchmark for evaluating SEarch-Augmented Language models on fact-seeking questions where web search yields conflicting, noisy, or unhelpful results. SealQA comes in three flavors: (1) Seal-0 (main) and (2) Seal-Hard, which assess factual accuracy and reasoning capabilities, with Seal-0 focusing on the most challenging questions where chat models (e.g., GPT-4.1) typically achieve near-zero accuracy; and (3) LongSeal, which extends SealQA to test long-context, multi-document reasoning in "needle-in-a-haystack" settings. Our evaluation reveals critical limitations in current models: Even frontier LLMs perform poorly across all SealQA flavors. On Seal-0, frontier agentic models equipped with tools like o3 and o4-mini achieve only 17.1% and 6.3% accuracy, respectively, at their best reasoning efforts. We find that advanced reasoning models such as DeepSeek-R1-671B and o3-mini are highly vulnerable to noisy search results. Notably, increasing test-time compute does not yield reliable gains across o3-mini, o4-mini, and o3, with performance often plateauing or even declining early. Additionally, while recent models are less affected by the "lost-in-the-middle" issue, they still fail to reliably identify relevant documents in LongSeal when faced with numerous distractors. To facilitate future work, we release SealQA at this http URL .

</details>

---

### 55. [OSPO: Object-Centric Self-Improving Preference Optimization for Text-to-Image Generation](https://arxiv.org/abs/2506.02015)

**基本信息**

- 🔗 arXiv: [`2506.02015`](https://arxiv.org/abs/2506.02015)
- 👥 作者: Yoonjin Oh, Yongjin Kim, Hyomin Kim 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.02015.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种自改进优化框架（OSPO），以增强多模态大语言模型（MLLMs）在图像生成任务中的对象级推理和对齐能力。

**📖 中文摘要**

本文针对多模态大语言模型（MLLMs）在细粒度文本-图像对齐（如物体属性、空间关系）方面的不足，提出了对象中心的自改进偏好优化（OSPO）框架。OSPO旨在增强对象级别的文本-图像对齐，减少物体幻觉。该框架使MLLM能够自主生成以对象为中心的偏好数据，进行自我偏好估计，并使用自构建的偏好对进行自我优化，而无需依赖外部数据或模型。实验表明，OSPO显著改善了细粒度对齐。这项工作直接涉及改进大语言模型（此处为MLLMs）的生成和推理能力，特别是针对图像生成中的对象级语义推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in Multimodal Large Language Models (MLLMs) have enabled unified multimodal understanding and generation. However, they still struggle with fine-grained text-image alignment, often failing to faithfully depict objects with correct attributes such as color, shape, and spatial relations. To mitigate this issue, previous studies have explored preference optimization methods such as DPO and GRPO, but these approaches incur substantial computational cost, both in constructing preference data and in performing optimization. This has motivated self-improving preference optimization approaches, in which the MLLM autonomously generates its own training data, self-estimates preference feedback, and self-optimizes using the resulting self-constructed preference pairs. However, existing self-improving methods still overlook fine-grained, object-level semantics, allowing object hallucination to persist. To tackle this problem, we propose Object-centric Self-improving Preference Optimization (OSPO), a self-improving framework designed to enhance object-level text-image alignment. OSPO explicitly constructs object-centric preference data without relying on any external data and external models. We also introduce a new approach that leverages attention-based object masks together with an object-weighted SimPO loss to enhance object-specific fidelity. Extensive experiments on three compositional image generation benchmarks demonstrate that OSPO significantly improves fine-grained alignment and reduces object hallucination, outperforming prior self-improving methods and even specialized diffusion-based text-to-image models.

</details>

---

### 56. [HSG-12M: A Large-Scale Benchmark of Spatial Multigraphs from the Energy Spectra of Non-Hermitian Crystals](https://arxiv.org/abs/2506.08618)

**基本信息**

- 🔗 arXiv: [`2506.08618`](https://arxiv.org/abs/2506.08618)
- 👥 作者: Xianquan Yan, Hakan Akgün, Kenji Kawaguchi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08618.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模、高质量的数据集HSG-12M，该数据集源自物理系统（晶体哈密顿量），但其核心贡献是生成和提供了一个图结构数据集。虽然其直接应用领域是物理和几何图学习，但‘图’是化学信息学中表示分子结构的核心工具（如分子图）。该论文提出的‘空间多重图’概念和生成大规模图数据集的方法论，为开发用于‘化学大模型’（特别是基于图的分子表示学习模型）或‘质谱结构推理’（将质谱数据映射为图结构）的通用图学习模型提供了潜在的高质量数据资源和工具。因此，它与化学信息学中基于图的模型开发高度相关。

**📖 中文摘要**

本文介绍了HSG-12M，一个包含1160万个静态和510万个动态哈密顿谱图的大规模数据集。该数据集源自非厄米量子物理领域，其中晶体的能谱在复平面上形成复杂的几何结构（哈密顿谱图）。论文的核心贡献是提出了Poly2Graph，一个将一维晶体哈密顿量自动映射为谱图的高性能开源流程。HSG-12M是第一个大规模的空间多重图数据集，图中的边保留了节点之间在度量空间中的几何轨迹信息。作者指出，谱图可以作为多项式、向量和矩阵的通用拓扑指纹，从而建立了一种新的代数到图的联系。该数据集为凝聚态物理中的数据驱动科学发现、几何感知图学习等领域奠定了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI is transforming scientific research by revealing new ways to understand complex physical systems, but its impact remains constrained by the lack of large, high-quality domain-specific datasets. A rich, largely untapped resource lies in non-Hermitian quantum physics, where the energy spectra of crystals form intricate geometries on the complex plane -- termed as Hamiltonian spectral graphs. Despite their significance as fingerprints for electronic behavior, their systematic study has been intractable due to the reliance on manual extraction. To unlock this potential, we introduce Poly2Graph: a high-performance, open-source pipeline that automates the mapping of 1-D crystal Hamiltonians to spectral graphs. Using this tool, we present HSG-12M: a dataset containing 11.6 million static and 5.1 million dynamic Hamiltonian spectral graphs across 1401 characteristic-polynomial classes, distilled from 177 TB of spectral potential data. Crucially, HSG-12M is the first large-scale dataset of spatial multigraphs -- graphs embedded in a metric space where multiple geometrically distinct trajectories between two nodes are retained as separate edges. This simultaneously addresses a critical gap, as existing graph benchmarks overwhelmingly assume simple, non-spatial edges, discarding vital geometric information. Benchmarks with popular GNNs expose new challenges in learning spatial multi-edges at scale. Beyond its practical utility, we show that spectral graphs serve as universal topological fingerprints of polynomials, vectors, and matrices, forging a new algebra-to-graph link. HSG-12M lays the groundwork for data-driven scientific discovery in condensed matter physics, new opportunities in geometry-aware graph learning and beyond.

</details>

---

### 57. [Bures-Wasserstein Flow Matching for Graph Generation](https://arxiv.org/abs/2506.14020)

**基本信息**

- 🔗 arXiv: [`2506.14020`](https://arxiv.org/abs/2506.14020)
- 👥 作者: Keyue Jiang, Jiahao Cui, Xiaowen Dong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图生成模型。在化学信息学领域，分子通常被表示为图（原子为节点，化学键为边）。因此，开发先进的图生成模型是‘化学大模型’（特别是分子生成模型）的核心研究方向之一。BWFlow提出的基于最优传输和流匹配的图生成框架，直接针对分子生成等任务，与化学信息学中利用生成模型进行分子设计这一主题高度相关。

**📖 中文摘要**

本文提出了BWFlow，一种用于图生成的流匹配框架。针对现有扩散和流模型在图生成中独立建模节点和边、使用线性插值导致概率路径不光滑的问题，BWFlow将图建模为由马尔可夫随机场参数化的连接系统，并利用MRF对象之间的最优传输位移来设计一个确保图组件协同演化的平滑概率路径。该框架在普通图生成和分子生成任务上进行了实验验证，取得了有竞争力的性能、更好的训练收敛性和高效的采样。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation has emerged as a critical task in fields ranging from drug discovery to circuit design. Contemporary approaches, notably diffusion and flow-based models, have achieved solid graph generative performance through constructing a probability path that interpolates between reference and data distributions. However, these methods typically model the evolution of individual nodes and edges independently and use linear interpolations in the disjoint space of nodes/edges to build the path. This disentangled interpolation breaks the interconnected patterns of graphs, making the constructed probability path irregular and non-smooth, which causes poor training dynamics and faulty sampling convergence. To address the limitation, this paper first presents a theoretically grounded framework for probability path construction in graph generative models. Specifically, we model the joint evolution of the nodes and edges by representing graphs as connected systems parameterized by Markov random fields (MRF). We then leverage the optimal transport displacement between MRF objects to design a smooth probability path that ensures the co-evolution of graph components. Based on this, we introduce BWFlow, a flow-matching framework for graph generation that utilizes the derived optimal probability path to benefit the training and sampling algorithm design. Experimental evaluations in plain graph generation and molecule generation validate the effectiveness of BWFlow with competitive performance, better training convergence, and efficient sampling.

</details>

---

### 58. [Diffusion-Based Impedance Learning for Contact-Rich Manipulation Tasks](https://arxiv.org/abs/2509.19696)

**基本信息**

- 🔗 arXiv: [`2509.19696`](https://arxiv.org/abs/2509.19696)
- 👥 作者: Noah Geiger, Tamim Asfour, Neville Hogan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.19696.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的生成框架（Transformer-based Diffusion Model）。虽然其应用场景是机器人操作，但该模型在方法论上属于‘化学大模型’所涵盖的生成式人工智能范畴。扩散模型是当前构建化学大模型（如分子生成、反应预测）的关键技术之一。论文中详细描述的扩散模型架构、条件生成（cross-attention on measured external wrenches）以及用于保持几何一致性的噪声调度器（SLERP-based quaternion noise scheduler），这些技术细节对于构建和理解复杂的生成模型具有参考价值，与化学信息学中利用扩散模型进行分子或反应路径生成的研究主题在方法论上直接相关。

**📖 中文摘要**

本文提出了基于扩散的阻抗学习框架，用于接触丰富的机器人操作任务。该框架结合了生成建模与能量一致的阻抗控制。一个基于Transformer的扩散模型，通过交叉注意力以测量的外部力矩为条件，重建模拟的零力轨迹（sZFT），该轨迹代表了接触一致的平衡行为。重建的sZFT随后被一个基于能量的估计器用于通过方向性刚度和阻尼调制在线调整阻抗。该方法在通过Apple Vision Pro遥操作收集的跑酷和机器人辅助治疗演示数据上进行训练，实现了亚毫米级的位置和亚度级的旋转精度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning-based methods excel at robot motion generation but remain limited in contact-rich physical interaction. Impedance control provides stable and safe contact behavior but requires task-specific tuning of stiffness and damping parameters. We present Diffusion-Based Impedance Learning, a framework that bridges these paradigms by combining generative modeling with energy-consistent impedance control. A Transformer-based Diffusion Model, conditioned via cross-attention on measured external wrenches, reconstructs simulated Zero-Force Trajectories (sZFTs) that represent contact-consistent equilibrium behavior. A SLERP-based quaternion noise scheduler preserves geometric consistency for rotations on the unit sphere. The reconstructed sZFT is used by an energy-based estimator to adapt impedance online through directional stiffness and damping modulation. Trained on parkour and robot-assisted therapy demonstrations collected via Apple Vision Pro teleoperation, the model achieves sub-millimeter positional and sub-degree rotational accuracy using only tens of thousands of samples. Deployed in realtime torque control on a KUKA LBR iiwa, the approach enables smooth obstacle traversal and generalizes to unseen tasks, achieving 100% success in multi-geometry peg-in-hole insertion.

</details>

---

### 59. [Noise-to-Notes: Diffusion-based Generation and Refinement for Automatic Drum Transcription](https://arxiv.org/abs/2509.21739)

**基本信息**

- 🔗 arXiv: [`2509.21739`](https://arxiv.org/abs/2509.21739)
- 👥 作者: Michael Yeung, Keisuke Toyama, Toya Teramoto 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.21739.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的生成框架（Noise-to-Notes）用于从音频信号生成结构化数据（鼓点事件）。虽然应用领域是音乐信息检索，但其核心技术——‘扩散模型用于从复杂信号（音频谱图）生成离散/连续的结构化输出’——与‘质谱结构推理’的核心挑战高度相似。在质谱分析中，目标是从质谱信号（一种复杂的一维或二维数据）推理出分子结构（离散的图或序列）。论文中解决联合优化二值事件和连续参数的方法、利用预训练基础模型增强特征表示以提升鲁棒性的策略，都为解决质谱到结构的生成式推理问题提供了直接的方法论参考和思路启发。

**📖 中文摘要**

本文重新定义了自动鼓点转录（ADT）任务，将其从一个判别式任务转变为条件生成任务，并引入了Noise-to-Notes（N2N）框架。N2N利用扩散建模，将音频条件化的高斯噪声转化为带有相关速度信息的鼓点事件。这种生成式扩散方法具有灵活的速度-精度权衡和强大的修复能力。为了有效联合优化二值起始点和连续速度值，论文引入了退火伪Huber损失。此外，为了增强低层级声谱图特征，论文提出整合从音乐基础模型中提取的特征，这些特征捕获了高层级语义信息，并增强了对域外鼓声音频的鲁棒性。实验结果表明，整合音乐基础模型特征显著提高了鲁棒性，并且N2N在多个ADT基准测试中取得了最先进的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automatic drum transcription (ADT) is traditionally formulated as a discriminative task to predict drum events from audio spectrograms. In this work, we redefine ADT as a conditional generative task and introduce Noise-to-Notes (N2N), a framework leveraging diffusion modeling to transform audio-conditioned Gaussian noise into drum events with associated velocities. This generative diffusion approach offers distinct advantages, including a flexible speed-accuracy trade-off and strong inpainting capabilities. However, the generation of binary onset and continuous velocity values presents a challenge for diffusion models, and to overcome this, we introduce an Annealed Pseudo-Huber loss to facilitate effective joint optimization. Finally, to augment low-level spectrogram features, we propose incorporating features extracted from music foundation models (MFMs), which capture high-level semantic information and enhance robustness to out-of-domain drum audio. Experimental results demonstrate that including MFM features significantly improves robustness and N2N establishes a new state-of-the-art performance across multiple ADT benchmarks.

</details>

---

### 60. [BeyondBench: Contamination-Resistant Evaluation of Reasoning in Language Models](https://arxiv.org/abs/2509.24210)

**基本信息**

- 🔗 arXiv: [`2509.24210`](https://arxiv.org/abs/2509.24210)
- 👥 作者: Gaurav Srivastava, Aafiya Hussain, Zhenyu Bi 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24210.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新颖的、抗污染的评估框架BeyondBench，用于评估语言模型的推理能力。该框架的核心是‘算法问题生成’，能够动态创建大量独特的、具有确定解的问题实例。虽然论文主要评估LLM，但这种生成可控、可验证的评估数据集的方法论，对于构建和评估‘化学大模型’或‘质谱结构推理’模型的性能至关重要。在化学信息学中，需要评估模型对分子性质预测、逆合成规划或从质谱推断结构的泛化能力和推理能力。BeyondBench提供的抗污染、可扩展的基准构建理念，可以直接借鉴用于创建化学或质谱领域的专用评估基准，以更可靠地衡量相关模型的真实能力。

**📖 中文摘要**

本文介绍了BeyondBench，一个使用算法问题生成来动态创建数学基础问题、从而确保测试不被训练数据污染的评估框架。该框架涵盖44个算法任务，包含117种变体，分为三个难度级别：简单套件（29个任务）涉及算术和统计；中等套件（5个任务，49种变体）涉及序列模式和推理；困难套件（10个任务，68种变体）涉及NP完全和约束满足问题。每个任务从一个超过10^15个独特实例的空间中抽取，并具有确定性验证的解决方案。论文评估了101个语言模型，揭示了随着复杂性增加，性能急剧下降的一致推理缺陷。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating language models fairly is increasingly difficult as static benchmarks risk contamination by training data, obscuring whether models truly reason or recall. We introduce BeyondBench, an evaluation framework using algorithmic problem generation to create mathematically grounded problems on the fly, ensuring each test remains uncontaminated. Our framework covers 44 algorithmic tasks with 117 variations across three difficulty levels: the Easy Suite (29 tasks) for arithmetic and statistics, the Medium Suite (5 tasks, 49 variations) for sequence patterns and reasoning, and the Hard Suite (10 tasks, 68 variations) for NP-complete and constraint satisfaction problems. Each task draws from a space exceeding 10^15 unique instances, with deterministically verified solutions. We evaluated 101 language models (85 open-source, 16 closed-source), spanning 0.5B to 141B parameters and multiple quantization schemes, using three-fold evaluation for robustness. Results reveal consistent reasoning deficiencies, with performance degrading sharply as complexity increases. In Hard Suite evaluations, Gemini-2.5-pro, Llama-3.3-70B, and Qwen2.5-72B achieved accuracies of 56.21%, 27.16%, and 33.37% respectively. Performance drops significantly without tool usage, with GPT-5, GPT-5-mini, and GPT-5-nano showing declines of 16.81%, 15.86%, and 43.95% in overall accuracy. Contamination resistance rests on three guarantees: (i) the problem space vastly exceeds any static dataset, (ii) every instance has a deterministically verifiable solution, and (iii) isomorphic transformations yield semantically equivalent but syntactically novel problems. BeyondBench redefines reasoning evaluation via genuine algorithmic problem-solving. Our leaderboard is at this https URL , Python package at this https URL , and codebase at this https URL .

</details>

---

### 61. [EchoMind: An Interrelated Multi-level Benchmark for Evaluating Empathetic Speech Language Models](https://arxiv.org/abs/2510.22758)

**基本信息**

- 🔗 arXiv: [`2510.22758`](https://arxiv.org/abs/2510.22758)
- 👥 作者: Li Zhou, Lutong Yu, You Lyu 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22758.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新颖的、多模态的基准测试框架EchoMind，专门用于评估模型对非文本线索（声音线索）的感知和整合推理能力。虽然其应用场景是共情对话，但其核心贡献在于构建了一个系统化的、多任务关联的评估体系。这种构建复杂、综合评估基准的方法论，对于‘化学大模型’和‘质谱结构推理’领域具有重要参考价值。例如，可以借鉴其思路，构建一个评估化学模型是否能够整合分子结构、光谱数据、文本描述和反应条件等多模态信息进行推理的基准。因此，该论文提供了与‘构建评估资源’相关的工具和方法论参考。

**📖 中文摘要**

本文提出了EchoMind，第一个相互关联的多层级基准测试，用于评估语音语言模型的共情对话能力。它通过顺序的、上下文关联的任务来模拟共情对话的认知过程：口语内容理解、声音线索感知、整合推理和回应生成。所有任务共享相同且语义中立的脚本，并通过受控的声音风格变化来测试独立于文本内容的表达效果。EchoMind基于一个涵盖3个粗粒度和12个细粒度维度、包含39个声音属性的共情导向框架，并使用主客观指标进行评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech Language Models (SLMs) have made significant progress in spoken language understanding. Yet it remains unclear whether they can fully perceive non lexical vocal cues alongside spoken words, and respond with empathy that aligns with both emotional and contextual factors. Existing benchmarks typically evaluate linguistic, acoustic, reasoning, or dialogue abilities in isolation, overlooking the integration of these skills that is crucial for human-like, emotionally intelligent conversation. We present EchoMind, the first interrelated, multi-level benchmark that simulates the cognitive process of empathetic dialogue through sequential, context-linked tasks: spoken-content understanding, vocal-cue perception, integrated reasoning, and response generation. All tasks share identical and semantically neutral scripts that are free of explicit emotional or contextual cues, and controlled variations in vocal style are used to test the effect of delivery independent of the transcript. EchoMind is grounded in an empathy-oriented framework spanning 3 coarse and 12 fine-grained dimensions, encompassing 39 vocal attributes, and evaluated using both objective and subjective metrics. Testing 12 advanced SLMs reveals that even state-of-the-art models struggle with high-expressive vocal cues, limiting empathetic response quality. Analyses of prompt strength, speech source, and ideal vocal cue recognition reveal persistent weaknesses in instruction-following, resilience to natural speech variability, and effective use of vocal cues for empathy. These results underscore the need for SLMs that integrate linguistic content with diverse vocal cues to achieve truly empathetic conversational ability.

</details>

---

### 62. [Kinodynamic Task and Motion Planning using VLM-guided and Interleaved Sampling](https://arxiv.org/abs/2510.26139)

**基本信息**

- 🔗 arXiv: [`2510.26139`](https://arxiv.org/abs/2510.26139)
- 👥 作者: Minseo Kwon, Young J. Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.26139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用视觉语言模型（VLM）来引导和优化任务与运动规划。虽然应用领域是机器人学，但其关键技术——‘使用VLM理解和推理空间场景（visual rendering of the states）以指导复杂决策过程’——与‘化学大模型’中利用多模态模型（结合分子结构图、文本描述等）进行分子设计或反应规划的思路高度相似。论文展示了如何将高级语义理解（通过VLM）与底层的几何/物理约束验证相结合，这种架构对于构建能够处理化学空间探索（任务规划）和分子构象/合成可行性（运动/物理约束）的化学智能体具有方法论上的启发性。

**📖 中文摘要**

本文提出了一种基于混合状态树的动力学任务与运动规划器，该规划器在规划过程中统一表示符号状态和数值状态，使得任务和运动决策能够共同决定。TAMP问题中嵌入的动力学约束由现成的运动规划器和物理模拟器验证，而视觉语言模型则通过状态的可视化渲染来引导探索TAMP解决方案并基于此回溯搜索。实验表明，与传统和基于LLM的TAMP规划器相比，该方法在复杂问题上提高了平均成功率并减少了规划时间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Task and Motion Planning (TAMP) integrates high-level task planning with low-level motion feasibility, but existing methods are costly in long-horizon problems due to excessive motion sampling. While LLMs provide commonsense priors, they lack 3D spatial reasoning and cannot ensure geometric or dynamic feasibility. We propose a kinodynamic TAMP planner based on a hybrid state tree that uniformly represents symbolic and numeric states during planning, enabling task and motion decisions to be jointly decided. Kinodynamic constraints embedded in the TAMP problem are verified by an off-the-shelf motion planner and physics simulator, and a VLM guides exploring a TAMP solution and backtracks the search based on visual rendering of the states. Experiments on the simulated domains and in the real world show 32.14% - 1166.67% increased average success rates compared to traditional and LLM-based TAMP planners and reduced planning time on complex problems, with ablations further highlighting the benefits of VLM backtracking. More details are available at this https URL .

</details>

---

### 63. [SpikeATac: A Multimodal Tactile Finger with Taxelized Dynamic Sensing for Dexterous Manipulation](https://arxiv.org/abs/2510.27048)

**基本信息**

- 🔗 arXiv: [`2510.27048`](https://arxiv.org/abs/2510.27048)
- 👥 作者: Eric T. Chang, Peter Ballentine, Zhanpeng He 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27048.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合了强化学习和多模态传感（触觉）的框架，用于实现复杂的机器人操作技能。虽然应用场景是机器人操控，但其核心技术——‘使用强化学习从人类反馈和特定模态（触觉）的奖励信号中微调策略’——是训练‘化学大模型’或智能体完成特定化学任务（如分子优化、实验操作）的常用范式之一。论文中描述的学习框架（RL from human feedback with tactile-based rewards）为如何在化学领域设计奖励函数、整合领域特定反馈（如光谱信号、合成成功率）来训练模型提供了实践参考。

**📖 中文摘要**

本文介绍了SpikeATac，一种多模态触觉手指，它将高度敏感的动态响应（PVDF）与静态传感方法（电容式）相结合，用于多模态触觉感知。SpikeATac的16个触元的PVDF薄膜以4 kHz采样，提供快速、灵敏的动态信号。论文展示了SpikeATac在抓取脆弱、可变形物体时快速、轻柔停止的能力。此外，论文还展示了一个结合人类反馈强化学习和基于触觉奖励的学习框架，用于在多指灵巧手机器人手上实现新功能，特别是实现了此前未完成的困难灵巧接触任务：脆弱物体的手内操控。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we introduce SpikeATac, a multimodal tactile finger combining a taxelized and highly sensitive dynamic response (PVDF) with a static transduction method (capacitive) for multimodal touch sensing. Named for its `spiky' response, SpikeATac's 16-taxel PVDF film sampled at 4 kHz provides fast, sensitive dynamic signals to the very onset and breaking of contact. We characterize the sensitivity of the different modalities, and show that SpikeATac provides the ability to stop quickly and delicately when grasping fragile, deformable objects. Beyond parallel grasping, we show that SpikeATac can be used in a learning-based framework to achieve new capabilities on a dexterous multifingered robot hand. We use a learning recipe that combines reinforcement learning from human feedback with tactile-based rewards to fine-tune the behavior of a policy to modulate force. Our hardware platform and learning pipeline together enable a difficult dexterous and contact-rich task that has not previously been achieved: in-hand manipulation of fragile objects. Videos are available at this https URL .

</details>

---

### 64. [FMint-SDE: A Multimodal Foundation Model for Accelerating Numerical Simulation of SDEs via Error Correction](https://arxiv.org/abs/2510.27173)

**基本信息**

- 🔗 arXiv: [`2510.27173`](https://arxiv.org/abs/2510.27173)
- 👥 作者: Jiaxin Yuan, Haizhao Yang, Maria Cameron
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.27173.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于加速科学计算（SDE求解）的‘基础模型’（FMint-SDE）。这直接对应于‘化学大模型’主题中的一个重要子方向：开发用于加速计算化学、分子动力学模拟的科学基础模型。FMint-SDE利用Transformer和上下文学习来校正传统数值方法的误差，这种‘AI加速科学计算’的范式正是化学信息学中构建下一代模拟工具的核心思路。因此，该论文在模型架构、训练方法（上下文学习、多模态提示）和应用目标上，都与化学大模型的研究高度相关。

**📖 中文摘要**

本文介绍了FMint-SDE，一个用于加速随机微分方程数值模拟的多模态基础模型。该模型基于一个具有上下文学习能力的仅解码器Transformer，利用数值和文本模态来学习通用的误差校正方案。它使用传统求解器生成的粗略解序列进行提示训练，从而能够泛化到不同的系统。论文在涵盖分子动力学、机械系统、金融和生物学应用的SDE基准测试套件上评估了模型，实验结果表明，与经典求解器相比，该方法在精度和效率之间取得了更优的权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fast and accurate simulation of dynamical systems is a fundamental challenge across scientific and engineering domains. Traditional numerical integrators often face a trade-off between accuracy and computational efficiency, while existing neural network-based approaches typically require training a separate model for each case. To overcome these limitations, we introduce a novel multi-modal foundation model for large-scale simulations of differential equations: FMint-SDE (Foundation Model based on Initialization for stochastic differential equations). Based on a decoder-only transformer with in-context learning, FMint-SDE leverages numerical and textual modalities to learn a universal error-correction scheme. It is trained using prompted sequences of coarse solutions generated by conventional solvers, enabling broad generalization across diverse systems. We evaluate our models on a suite of challenging SDE benchmarks spanning applications in molecular dynamics, mechanical systems, finance, and biology. Experimental results show that our approach achieves a superior accuracy-efficiency tradeoff compared to classical solvers, underscoring the potential of FMint-SDE as a general-purpose simulation tool for dynamical systems.

</details>

---

### 65. [FLoC: Facility Location-Based Efficient Visual Token Compression for Long Video Understanding](https://arxiv.org/abs/2511.00141)

**基本信息**

- 🔗 arXiv: [`2511.00141`](https://arxiv.org/abs/2511.00141)
- 👥 作者: Janghoon Cho, Jungsoo Lee, Munawar Hayat 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.00141.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效的、与模型无关的视觉令牌压缩框架FLoC。虽然其应用场景是长视频理解，但其核心技术创新——‘使用设施选址函数和贪婪算法从高维视觉序列中选择信息量最大、最具代表性的子集’——为解决化学信息学和质谱分析中的类似问题提供了强大的工具。例如，在分析高通量分子动力学模拟轨迹（可视为长序列）或高分辨率质谱数据时，都需要从海量数据点中提取关键特征或代表性片段。FLoC提供的这种可证明近似最优的稀疏化选择方法，可以直接应用于压缩分子构象序列或质谱峰数据，为后续的‘化学大模型’处理或‘质谱结构推理’降维提效。因此，它与主题在数据处理工具层面高度相关。

**📖 中文摘要**

本文提出了FLoC，一种基于设施选址函数的高效视觉令牌压缩框架，用于长视频理解。该方法是一种原则性的方法，能够在预定义的视觉令牌数量预算内，快速选择一个紧凑但具有高度代表性和多样性的视觉令牌子集。通过集成惰性贪婪算法，该方法实现了显著的效率提升，在保证接近最优性能的同时，大幅减少了视觉令牌的数量。该方法无需训练、与模型无关且与查询无关，提供了一个可无缝集成到各种视频LLM和现有工作流程中的通用解决方案。在Video-MME、MLVU、LongVideoBench和EgoSchema等大规模基准测试上的广泛评估表明，该框架 consistently 优于最近的压缩技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent studies in long video understanding have harnessed the advanced visual-language reasoning capabilities of Large Multimodal Models (LMMs), driving the evolution of video-LMMs specialized for processing extended video sequences. However, the scalability of these models is severely limited by the overwhelming volume of visual tokens generated from extended video sequences. To address this challenge, we propose FLoC, an efficient visual token compression framework based on the facility location function, a principled approach that swiftly selects a compact yet highly representative and diverse subset of visual tokens within a predefined budget on the number of visual tokens. By integrating the lazy greedy algorithm, our method achieves remarkable efficiency gains by swiftly selecting a compact subset of tokens, drastically reducing the number of visual tokens while guaranteeing near-optimal performance. Notably, our approach is training-free, model-agnostic, and query-agnostic, providing a versatile solution that seamlessly integrates with diverse video-LLMs and existing workflows. Extensive evaluations on large-scale benchmarks, such as Video-MME, MLVU, LongVideoBench, and EgoSchema, show that our framework consistently surpasses recent compression techniques, highlighting its effectiveness and robustness in addressing the challenges of long video understanding as well as its processing efficiency.

</details>

---

### 66. [Interleaved Tool-Call Reasoning for Protein Function Understanding](https://arxiv.org/abs/2601.03604)

**基本信息**

- 🔗 arXiv: [`2601.03604`](https://arxiv.org/abs/2601.03604)
- 👥 作者: Chuanliu Fan, Zicheng Ma, Huanran Meng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.03604.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于蛋白质功能理解的工具增强型推理代理（PFUA），这属于构建针对特定化学/生物学领域的、具备工具调用和推理能力的“化学大模型”或领域智能体。

**📖 中文摘要**

这篇论文提出了一种名为PFUA的工具增强蛋白质推理代理，用于蛋白质功能理解。它统一了问题分解、工具调用和基于证据的答案生成。作者指出，蛋白质功能预测是一项知识密集型的科学任务，本质上依赖于外部生物学先验和计算工具，而不是纯粹的内部推理。因此，该工作将化学/生物信息学领域的外部工具（如数据库查询、计算工具）与大型语言模型的推理能力相结合，以解决蛋白质功能预测问题。这直接关联到“化学大模型”主题，展示了如何构建一个专门针对化学/生物学领域的、能够调用领域工具进行推理的智能体或模型框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have highlighted the effectiveness of chain-of-thought reasoning in symbolic domains such as mathematics and programming. However, our study shows that directly transferring such text-based reasoning paradigms to protein function understanding is ineffective: reinforcement learning mainly amplifies superficial keyword patterns while failing to introduce new biological knowledge, resulting in limited generalization. We argue that protein function prediction is a knowledge-intensive scientific task that fundamentally relies on external biological priors and computational tools rather than purely internal reasoning. To address this gap, we propose PFUA, a tool-augmented protein reasoning agent that unifies problem decomposition, tool invocation, and grounded answer generation. Instead of relying on long unconstrained reasoning traces, PFUA integrates domain-specific tools to produce verifiable intermediate evidence. Experiments on four benchmarks demonstrate that PFUA consistently outperforms text-only reasoning models with an average performance improvement of 103%.

</details>

---

### 67. [Controlled LLM Training on Spectral Sphere](https://arxiv.org/abs/2601.08393)

**基本信息**

- 🔗 arXiv: [`2601.08393`](https://arxiv.org/abs/2601.08393)
- 👥 作者: Tian Xie, Haoming Luo, Haoyu Tang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.08393.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种新的、适用于大规模模型训练的优化器（SSO）。稳定高效的训练方法是构建任何领域“大模型”（包括化学大模型）的基础和关键组成部分，因此该工作与“化学大模型”主题在基础方法论层面直接相关。

**📖 中文摘要**

这篇论文提出了谱球优化器（SSO），一种用于大规模语言模型训练的新型优化器。SSO在谱球上强制执行严格的模块化谱约束，实现了与最大更新参数化（μP）完全对齐的优化过程。论文通过在包括密集模型、混合专家模型和深度网络在内的多种架构上进行广泛的预训练来验证SSO。这项工作属于大模型训练和优化的基础方法论研究。虽然不直接针对质谱，但其核心——优化大规模模型训练——是构建任何领域“大模型”（包括化学大模型）的关键使能技术。稳定的优化策略对于训练可靠的化学领域大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling large models requires optimization strategies that ensure rapid convergence grounded in stability. Maximal Update Parametrization ($\boldsymbol{\mu}$P) provides a theoretical safeguard for width-invariant $\Theta(1)$ activation control, whereas emerging optimizers like Muon are only ``half-aligned'' with these constraints: they control updates but allow weights to drift. To address this limitation, we introduce the \textbf{Spectral Sphere Optimizer (SSO)}, which enforces strict module-wise spectral constraints on both weights and their updates. By deriving the steepest descent direction on the spectral sphere, SSO realizes a fully $\boldsymbol{\mu}$P-aligned optimization process. To enable large-scale training, we implement SSO as an efficient parallel algorithm within Megatron. Through extensive pretraining on diverse architectures, including Dense 1.7B, MoE 8B-A1B, and 200-layer DeepNet models, SSO consistently outperforms AdamW and Muon. Furthermore, we observe significant practical stability benefits, including improved MoE router load balancing, suppressed outliers, and strictly bounded activations.

</details>

---

### 68. [Self-Distilled Reasoner: On-Policy Self-Distillation for Large Language Models](https://arxiv.org/abs/2601.18734)

**基本信息**

- 🔗 arXiv: [`2601.18734`](https://arxiv.org/abs/2601.18734)
- 👥 作者: Siyan Zhao, Zhihui Xie, Mengchen Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18734.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种新的、用于提升大型语言模型推理能力的自蒸馏框架（OPSD）。这种旨在增强模型复杂任务解决和泛化能力的方法论，是构建高性能“化学大模型”的关键技术，可应用于化学领域的推理任务，如质谱解析。

**📖 中文摘要**

这篇论文提出了策略内自蒸馏（OPSD），一个用于大型语言模型推理的蒸馏框架。在该框架中，单个模型通过在不同上下文条件下扮演教师和学生的角色。教师策略以特权信息（如已验证的推理轨迹）为条件，而学生策略只看到问题；训练过程最小化学生自身生成轨迹上两个分布之间的每词元差异。论文在多个数学推理基准上证明了该方法的有效性。这项工作属于提升大模型推理能力的方法学研究。虽然应用在数学领域，但其核心思想——通过自蒸馏提升模型的推理和泛化能力——可以直接迁移并应用于构建和优化“化学大模型”，特别是用于解决需要复杂推理的化学问题（如质谱结构推理）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge distillation improves large language model (LLM) reasoning by compressing the knowledge of a teacher LLM to train smaller LLMs. On-policy distillation advances this approach by having the student sample its own trajectories while a teacher LLM provides dense token-level supervision, addressing the distribution mismatch between training and inference in off-policy distillation methods. However, on-policy distillation typically requires a separate, often larger, teacher LLM and does not explicitly leverage ground-truth solutions available in reasoning datasets. Inspired by the intuition that a sufficiently capable LLM can rationalize external privileged reasoning traces and teach its weaker self (i.e., the version without access to privileged information), we introduce On-Policy Self-Distillation (OPSD), a framework where a single model acts as both teacher and student by conditioning on different contexts. The teacher policy conditions on privileged information (e.g., verified reasoning traces) while the student policy sees only the question; training minimizes the per-token divergence between these distributions over the student's own rollouts. We demonstrate the efficacy of our method on multiple mathematical reasoning benchmarks, achieving 8-12x token efficiency compared to reinforcement learning methods such as GRPO and superior performance over off-policy distillation methods.

</details>

---

### 69. [Replacing Parameters with Preferences: Federated Alignment of Heterogeneous Vision-Language Models](https://arxiv.org/abs/2602.00485)

**基本信息**

- 🔗 arXiv: [`2602.00485`](https://arxiv.org/abs/2602.00485)
- 👥 作者: Shule Lu, Yujing Wang, Hainan Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00485.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一个在联邦学习设置下对齐异构视觉语言模型的框架（MoR）。该工作直接关联“化学大模型”主题中关于模型训练、优化以及在隐私约束、数据分散场景下部署的挑战，提供了解决这些挑战的一种技术路径。

**📖 中文摘要**

这篇论文提出了MoR，一个基于GRPO和混合奖励的联邦对齐框架，用于异构视觉语言模型。该框架旨在隐私敏感的场景下（如医疗、金融），在客户端数据不共享的前提下，对齐和优化分布在多个客户端上的异构模型。每个客户端根据本地偏好标注训练一个奖励模型，服务器则使用混合奖励通过GRPO优化基础VLM。论文在三个公共VQA基准上进行了实验。这项工作涉及在联邦学习设置下对齐和优化大模型，特别是视觉语言模型。虽然主要针对VLM，但其解决的核心问题——在保护隐私和数据异构条件下有效优化和协调多个大模型——与构建安全、可协作的“化学大模型”生态系统所面临的挑战高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

VLMs have broad potential in privacy-sensitive domains such as healthcare and finance, yet strict data-sharing constraints render centralized training infeasible. FL mitigates this issue by enabling decentralized training, but practical deployments face challenges due to client heterogeneity in computational resources, application requirements, and model architectures. We argue that while replacing data with model parameters characterizes the present of FL, replacing parameters with preferences represents a more scalable and privacy-preserving future. Motivated by this perspective, we propose MoR, a federated alignment framework based on GRPO with Mixture-of-Rewards for heterogeneous VLMs. MoR initializes a visual foundation model as a KL-regularized reference, while each client locally trains a reward model from local preference annotations, capturing specific evaluation signals without exposing raw data. To reconcile heterogeneous rewards, we introduce a routing-based fusion mechanism that adaptively aggregates client reward signals. Finally, the server performs GRPO with this mixed reward to optimize the base VLM. Experiments on three public VQA benchmarks demonstrate that MoR consistently outperforms federated alignment baselines in generalization, robustness, and cross-client adaptability. Our approach provides a scalable solution for privacy-preserving alignment of heterogeneous VLMs under federated settings.

</details>

---

### 70. [Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards](https://arxiv.org/abs/2602.01601)

**基本信息**

- 🔗 arXiv: [`2602.01601`](https://arxiv.org/abs/2602.01601)
- 👥 作者: Hieu Trung Nguyen, Bao Nguyen, Wenao Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01601.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化用于训练大模型的强化学习算法（GRPO）的采样效率。这种提升训练效率的方法对于实际构建和迭代“化学大模型”至关重要，是相关技术栈的一部分。

**📖 中文摘要**

这篇论文提出了VIP，一种方差感知的预测性分配策略，用于优化具有可验证奖励的在线强化学习中的采样效率。VIP使用一个轻量级高斯过程模型来预测每个训练提示的成功概率，并将其转化为方差估计，然后通过凸优化在给定的计算预算约束下确定最优的模拟分配。论文在多个基准测试中展示了VIP能提高采样效率并获得更高性能。这项工作专注于改进用于训练大模型的强化学习算法（特别是GRPO及其变种）的效率。高效的RL训练方法是构建能够通过交互学习复杂技能的“化学大模型”（例如，学习设计分子或解析谱图）的重要工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce VIP, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, VIP uses a lightweight Gaussian process model to predict per-prompt success probabilities based on recent rollouts. These probability predictions are translated into variance estimates, which are then fed into a convex optimization problem to determine the optimal rollout allocations under a hard compute budget constraint. Empirical results show that VIP consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks.

</details>

---

### 71. [Position: Beyond Model-Centric Prediction -- Agentic Time Series Forecasting](https://arxiv.org/abs/2602.01776)

**基本信息**

- 🔗 arXiv: [`2602.01776`](https://arxiv.org/abs/2602.01776)
- 👥 作者: Mingyue Cheng, Xiaoyu Tao, Qi Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01776.pdf)

**💡 相关性分析**

满足标准1：论文的核心论点是倡导将预测任务重新构建为“智能体化”工作流。这一理念直接对应于“化学大模型”主题中关于构建能够自主规划、执行工具调用并迭代学习的化学领域智能体的前沿讨论和发展方向。

**📖 中文摘要**

这篇立场论文主张“智能体化时间序列预测”（ATSF），将预测重新定义为由感知、规划、行动、反思和记忆组成的智能体过程。论文认为，传统的模型中心预测范式在需要自适应、多轮交互的场景中不足，而ATSF强调将预测组织为能够与工具交互、结合结果反馈并通过经验积累进化的智能体工作流。论文概述了三种代表性的实现范式。虽然主题是时间序列预测，但其核心论点——将领域任务（如预测）重新构建为智能体工作流——与“化学大模型”的发展趋势高度一致。在化学信息学中，构建能够主动调用计算工具、设计实验、分析数据并迭代改进的“化学智能体”是“化学大模型”的一个重要演进方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Time series forecasting has traditionally been formulated as a model-centric, static, and single-pass prediction problem that maps historical observations to future values. While this paradigm has driven substantial progress, it proves insufficient in adaptive and multi-turn settings where forecasting requires informative feature extraction, reasoning-driven inference, iterative refinement, and continual adaptation over time. In this paper, we argue for agentic time series forecasting (ATSF), which reframes forecasting as an agentic process composed of perception, planning, action, reflection, and memory. Rather than focusing solely on predictive models, ATSF emphasizes organizing forecasting as an agentic workflow that can interact with tools, incorporate feedback from outcomes, and evolve through experience accumulation. We outline three representative implementation paradigms -- workflow-based design, agentic reinforcement learning, and a hybrid agentic workflow paradigm -- and discuss the opportunities and challenges that arise when shifting from model-centric prediction to agentic forecasting. Together, this position aims to establish agentic forecasting as a foundation for future research at the intersection of time series forecasting.

</details>

---

### 72. [Simple generators of rational function fields](https://arxiv.org/abs/2602.10878)

**基本信息**

- 🔗 arXiv: [`2602.10878`](https://arxiv.org/abs/2602.10878)
- 👥 作者: Alexander Demin, Gleb Pogudin
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10878.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种用于简化有理函数域子域表示的算法。这项基础性的符号计算工作与“化学大模型”和“质谱结构推理”主题存在潜在关联，因为化学系统的数学模型（如反应机理、定量结构-性质关系）经常使用有理函数进行描述，高效的符号处理工具可以支持更复杂的化学推理和模型构建。

**📖 中文摘要**

这篇论文提出了一种算法，用于为多元有理函数域的给定子域寻找简单的生成元集。算法的主要新颖之处包括通过稀疏插值进行部分Gröbner基计算，以及高效搜索有理函数域子域中固定次数的多项式。作者提供了算法的实现，并通过来自不同应用领域（如结构参数可辨识性）的案例研究展示了简化生成元的效用。这项工作属于计算代数和符号计算领域。虽然不直接处理质谱数据，但其核心算法——简化有理函数域的表示——在化学信息学中具有潜在应用，例如在表示化学反应网络、动力学模型或化学系统的输入输出关系时。这些模型经常涉及有理函数，简化其表示有助于分析和推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Consider a subfield of the field of rational functions in several indeterminates. We present an algorithm that, given a set of generators of such a subfield, finds a simple generating set. We provide an implementation of the algorithm and show that it improves upon the state of the art both in efficiency and the quality of the results. Furthermore, we demonstrate the utility of simplified generators through several case studies from different application domains, such as structural parameter identifiability. The main algorithmic novelties include performing only partial Gröbner basis computation via sparse interpolation and efficient search for polynomials of a fixed degree in a subfield of the rational function field.

</details>

---

### 73. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一基础模型（Zatom-1），这直接属于“化学大模型”的研究主题。

**📖 中文摘要**

本文介绍了Zatom-1，这是一个用于3D分子和材料的统一多模态流匹配基础模型。该模型是一个Transformer，通过多模态流匹配目标联合建模离散原子类型和连续3D几何结构。这种方法支持可扩展的预训练，并能够进行快速稳定的采样。作者使用联合生成预训练作为下游多任务预测（如性质、能量和力）的通用初始化。实验表明，Zatom-1在生成和预测基准测试中匹配或优于专门的基线模型，同时将生成推理时间减少了一个数量级以上。这项工作展示了化学大模型在统一生成和预测任务方面的进展，为3D化学建模提供了一个通用的基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first end-to-end, fully open-source foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 74. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个高效、准确的机器学习原子间势（MLIP）基础模型（MatRIS），这直接属于“化学大模型”在计算化学和材料科学中的应用主题。

**📖 中文摘要**

本文提出了MatRIS，一个用于材料表示和交互模拟的不变机器学习原子间势（MLIP）模型。MatRIS引入了一种基于注意力的三体相互作用建模方法，并利用具有线性复杂度的新型可分离注意力机制，实现了可扩展性和表达性。该模型在广泛的流行基准测试（如Matbench-Discovery、MatPES等）上达到了与领先的等变模型相当的精度，但训练成本更低。这项工作表明，经过精心设计的不变模型可以以较低的成本匹配或超过等变模型的精度，为开发准确高效的MLIPs提供了启示。MLIPs是化学信息学和计算材料科学中“化学大模型”的关键组成部分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 75. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准1：论文的核心理论分析（顺序检索和推理的动力学）为理解“化学大模型”中可能涉及的记忆、检索和顺序推理机制提供了基础理论框架和洞察。

**📖 中文摘要**

本文为Hopfield网络中的顺序推理开发了一个动力学理论。作者考虑了最近提出的输入驱动可塑性（IDP）Hopfield网络，并分析了一个将快速关联检索与慢速推理动力学耦合的双时间尺度架构。他们推导出了自持记忆转换的明确条件，包括增益阈值、逃逸时间和崩溃机制。这些结果为关联记忆模型中的顺序性提供了原理性的数学解释，架起了经典Hopfield动力学与现代推理架构之间的桥梁。虽然论文本身更偏向理论计算神经科学，但其核心——对顺序检索和推理的动力学建模——为理解更广泛的“化学大模型”（特别是那些涉及顺序推理和记忆检索的模型，如用于分子设计或性质预测的模型）的内部机制提供了理论基础和洞察。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 76. [Inverse Reconstruction of Shock Time Series from Shock Response Spectrum Curves using Machine Learning](https://arxiv.org/abs/2603.03229)

**基本信息**

- 🔗 arXiv: [`2603.03229`](https://arxiv.org/abs/2603.03229)
- 👥 作者: Adam Watts, Andrew Jeon, Destry Newton 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03229.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（使用深度学习模型从谱数据逆向生成源信号）与“质谱结构推理”主题在问题形式上高度相关，为解决从质谱推断分子结构这一逆问题提供了可借鉴的深度学习框架和思路。

**📖 中文摘要**

本文提出使用条件变分自编码器（CVAE）来学习从冲击响应谱（SRS）到加速度时间序列的数据驱动逆映射。一旦训练完成，该模型可以根据指定的目标谱生成信号，而无需迭代优化。实验表明，相对于经典技术，该方法在谱保真度方面有所改进，对未见过的谱具有强泛化能力，并且推理速度比传统方法快三到六个数量级。这些结果确立了深度生成模型作为逆SRS重建的可扩展且高效的方法。虽然应用领域是工程冲击分析，但论文的核心方法论——使用深度学习模型（CVAE）从谱数据中逆向生成时间序列信号——在概念上与“质谱结构推理”高度相关。质谱结构推理的核心挑战之一正是从质谱数据（一种谱图）逆向推断出产生该谱的分子结构（可以类比为“时间序列”或更一般的“信号源”）。本文展示的“谱到信号”的逆向生成框架，为质谱领域的类似问题（“谱到结构”）提供了方法论上的参考和验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The shock response spectrum (SRS) is widely used to characterize the response of single-degree-of-freedom (SDOF) systems to transient accelerations. Because the mapping from acceleration time history to SRS is nonlinear and many-to-one, reconstructing time-domain signals from a target spectrum is inherently ill-posed. Conventional approaches address this problem through iterative optimization, typically representing signals as sums of exponentially decayed sinusoids, but these methods are computationally expensive and constrained by predefined basis functions. We propose a conditional variational autoencoder (CVAE) that learns a data-driven inverse mapping from SRS to acceleration time series. Once trained, the model generates signals consistent with prescribed target spectra without requiring iterative optimization. Experiments demonstrate improved spectral fidelity relative to classical techniques, strong generalization to unseen spectra, and inference speeds three to six orders of magnitude faster. These results establish deep generative modeling as a scalable and efficient approach for inverse SRS reconstruction.

</details>

---

### 77. [DMD-augmented Unpaired Neural Schrödinger Bridge for Ultra-Low Field MRI Enhancement](https://arxiv.org/abs/2603.03769)

**基本信息**

- 🔗 arXiv: [`2603.03769`](https://arxiv.org/abs/2603.03769)
- 👥 作者: Youngmin Kim, Jaeyun Shin, Jeongchan Kim 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03769.pdf)

**💡 相关性分析**

满足标准1：论文的核心技术（基于扩散和桥接模型的未配对跨域信号翻译与增强）与“化学大模型”中可能涉及的光谱/质谱数据增强、跨仪器数据对齐、低质量数据修复等任务在方法论上高度相关。

**📖 中文摘要**

本文提出了一个用于64 mT超低场脑MRI到3 T MRI的未配对图像翻译框架。该方法基于未配对神经薛定谔桥（UNSB）并进行多步细化。为了加强目标分布对齐，作者使用冻结的3T扩散教师模型，通过DMD2风格的扩散引导分布匹配来增强对抗目标。为了在补丁级对应之外明确约束全局结构，他们将PatchNCE与解剖结构保持（ASP）正则化器相结合。该方法在未配对基准测试中提高了分布级真实感，同时在配对队列中与未配对基线相比增加了结构保真度。虽然应用领域是医学影像，但论文的核心技术——使用生成模型（特别是基于扩散和桥接的方法）进行跨域、跨模态的信号增强与翻译——与“化学大模型”中处理不同分辨率、不同仪器产生的光谱/质谱数据，或进行谱图增强、补全等任务在技术路径上具有相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ultra Low Field (64 mT) brain MRI improves accessibility but suffers from reduced image quality compared to 3 T. As paired 64 mT - 3 T scans are scarce, we propose an unpaired 64 mT $\rightarrow$ 3 T translation framework that enhances realism while preserving anatomy. Our method builds upon the Unpaired Neural Schrödinge Bridge (UNSB) with multi-step refinement. To strengthen target distribution alignment, we augment the adversarial objective with DMD2-style diffusion-guided distribution matching using a frozen 3T diffusion teacher. To explicitly constrain global structure beyond patch-level correspondence, we combine PatchNCE with an Anatomical Structure Preservation (ASP) regularizer that enforces soft foreground background consistency and boundary aware constraints. Evaluated on two disjoint cohorts, the proposed framework achieves an improved realism structure trade-off, enhancing distribution level realism on unpaired benchmarks while increasing structural fidelity on the paired cohort compared to unpaired baselines.

</details>

---

### 78. [Structured quantum learning via em algorithm for Boltzmann machines](https://arxiv.org/abs/2507.21569)

**基本信息**

- 🔗 arXiv: [`2507.21569`](https://arxiv.org/abs/2507.21569)
- 👥 作者: Takeshi Kimura, Kohtaro Kato, Masahito Hayashi
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.21569.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子机器学习模型（量子玻尔兹曼机）的新型训练算法，这直接关系到“化学大模型”在量子计算范式下的实现和优化，属于该主题的前沿交叉领域。

**📖 中文摘要**

本文为量子玻尔兹曼机（QBM）引入了一种量子版本的EM算法，这是一种信息几何上对经典期望最大化方法的推广，可以绕过在非凸函数上的基于梯度的优化。该方法在半量子受限玻尔兹曼机（sqRBM）上实现——这是一种将量子效应限制在隐藏层的混合架构。作者表明，该方法在多个基准数据集上实现了稳定学习，并且性能优于梯度下降。这些结果为量子机器学习中的梯度训练提供了一种结构化且可扩展的替代方案，为缓解贫瘠高原问题和增强量子生成建模提供了一条途径。量子机器学习模型，特别是用于化学和材料科学的量子生成模型，是“化学大模型”前沿探索的一个方向。本文提出的训练方法对于开发此类模型具有直接意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Boltzmann machines (QBMs) are generative models with potential advantages in quantum machine learning, yet their training is fundamentally limited by the barren plateau problem, where gradients vanish exponentially with system size. We introduce a quantum version of the em algorithm, an information-geometric generalization of the classical Expectation-Maximization method, which circumvents gradient-based optimization on non-convex functions. Implemented on a semi-quantum restricted Boltzmann machine (sqRBM) -- a hybrid architecture with quantum effects confined to the hidden layer -- our method achieves stable learning and outperforms gradient descent on multiple benchmark datasets. These results establish a structured and scalable alternative to gradient-based training in QML, offering a pathway to mitigate barren plateaus and enhance quantum generative modeling.

</details>

---

### 79. [CycleChemist: A Dual-Pronged Machine Learning Framework for Organic Photovoltaic Discovery](https://arxiv.org/abs/2511.19500)

**基本信息**

- 🔗 arXiv: [`2511.19500`](https://arxiv.org/abs/2511.19500)
- 👥 作者: Hou Hei Lam, Jiangjie Qiu, Xiuyuan Hu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.19500.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用机器学习（特别是图神经网络和生成模型）进行化学材料（有机光伏材料）的发现与设计，这直接属于“化学大模型”的应用范畴。

**📖 中文摘要**

本文提出了一个用于有机光伏（OPV）材料发现的机器学习框架CycleChemist。该框架结合了预测建模与生成式分子设计，并引入了有机光伏供体-受体数据集（OPV2D），这是同类中最大的、包含2000个实验表征的供体-受体对的精选数据集。框架包含多个组件：有机光伏分类器（OPVC）用于预测材料是否具有OPV行为；一个结合多任务学习和供体-受体相互作用建模的分层图神经网络；用于预测HOMO和LUMO能级的分子轨道能量估计器（MOE2）；以及用于估计功率转换效率（PCE）的光伏性能预测器（P3）。此外，还引入了材料生成预训练Transformer（MatGPT）来生成可合成的有机半导体。该工作通过将分子表示学习与性能预测联系起来，推进了高性能OPV材料的数据驱动发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Organic photovoltaic (OPV) materials offer a promising path toward sustainable energy generation, but their development is limited by the difficulty of identifying high performance donor and acceptor pairs with strong power conversion efficiencies (PCEs). Existing design strategies typically focus on either the donor or the acceptor alone, rather than using a unified approach capable of modeling both components. In this work, we introduce a dual machine learning framework for OPV discovery that combines predictive modeling with generative molecular design. We present the Organic Photovoltaic Donor Acceptor Dataset (OPV2D), the largest curated dataset of its kind, containing 2000 experimentally characterized donor acceptor pairs. Using this dataset, we develop the Organic Photovoltaic Classifier (OPVC) to predict whether a material exhibits OPV behavior, and a hierarchical graph neural network that incorporates multi task learning and donor acceptor interaction modeling. This framework includes the Molecular Orbital Energy Estimator (MOE2) for predicting HOMO and LUMO energy levels, and the Photovoltaic Performance Predictor (P3) for estimating PCE. In addition, we introduce the Material Generative Pretrained Transformer (MatGPT) to produce synthetically accessible organic semiconductors, guided by a reinforcement learning strategy with three objective policy optimization. By linking molecular representation learning with performance prediction, our framework advances data driven discovery of high performance OPV materials.

</details>

---

### 80. [Latent-IMH: Efficient Bayesian Inference for Inverse Problems with Approximate Operators](https://arxiv.org/abs/2601.20888)

**基本信息**

- 🔗 arXiv: [`2601.20888`](https://arxiv.org/abs/2601.20888)
- 👥 作者: Youguang Chen, George Biros
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.20888.pdf)

**💡 相关性分析**

满足标准1：论文提出的Latent-IMH方法，作为一种处理计算昂贵算子的高效贝叶斯推理框架，其核心思想可直接应用于“质谱结构推理”等化学逆问题中，用于加速从谱图数据推断分子结构的计算过程。

**📖 中文摘要**

本文提出了Latent-IMH，一种用于贝叶斯线性逆问题的采样方法，特别适用于参数到观测值的算子A计算成本高昂的场景。该方法的核心思想是利用算子A的近似版本Ā来高效生成中间潜变量，然后再使用精确的A进行精炼。虽然论文的通用背景是逆问题，但其核心方法——利用近似算子加速昂贵计算过程——与化学信息学和质谱分析中常见的、计算成本高昂的量子化学计算或谱图模拟问题高度相关。例如，在质谱结构推理中，从质谱数据反推分子结构是一个典型的逆问题，而精确的量子力学计算（如DFT）非常耗时。Latent-IMH提供了一种通过构建近似模型来加速此类贝叶斯推理过程的通用框架思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study sampling from posterior distributions in Bayesian linear inverse problems where $A$, the parameters to observables operator, is computationally expensive. In many applications, $A$ can be factored in a manner that facilitates the construction of a cost-effective approximation $\tilde{A}$. In this framework, we introduce Latent-IMH, a sampling method based on the Metropolis-Hastings independence (IMH) sampler. Latent-IMH first generates intermediate latent variables using the approximate $\tilde{A}$, and then refines them using the exact $A$. Its primary benefit is that it shifts the computational cost to an offline phase. We theoretically analyze the performance of Latent-IMH using KL divergence and mixing time bounds. Using numerical experiments on several model problems, we show that, under reasonable assumptions, it outperforms state-of-the-art methods such as the No-U-Turn sampler (NUTS) in computational efficiency. In some cases, Latent-IMH can be orders of magnitude faster than existing schemes.

</details>

---

### 81. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”的推理范式进行创新，提出了LatentChem这一旨在提升化学大语言模型推理效率和性能的潜在推理框架。

**📖 中文摘要**

本文针对化学大语言模型（LLMs）提出了LatentChem，一种潜在推理接口。作者指出，当前化学LLMs主要依赖自然语言中的显式思维链（CoT）进行复杂推理，但化学推理本质上是连续和结构化的，将其强制转化为离散的语言标记会造成表示上的不匹配，限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续的潜在空间中直接执行多步推理，而仅对最终输出生成语言。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变带来了计算优势。在多个化学推理基准测试中，LatentChem相比基于CoT的基线模型取得了显著优势（在ChemCoTBench上获得59.88%的非平局胜率），并实现了平均10.84倍的推理加速。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 82. [VoxKnesset: A Large-Scale Longitudinal Hebrew Speech Dataset for Aging Speaker Modeling](https://arxiv.org/abs/2603.01270)

**基本信息**

- 🔗 arXiv: [`2603.01270`](https://arxiv.org/abs/2603.01270)
- 👥 作者: Yanir Marmor, Arad Zulti, David Krongauz 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01270.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是构建并发布了一个大规模、高质量的纵向语音数据集VoxKnesset。虽然领域不同，但其在数据集的规模、质量、元数据完整性以及公开可用性方面的实践，为“化学大模型”和“质谱结构推理”领域所需的数据集构建提供了方法论上的参考和示范。

**📖 中文摘要**

本文介绍了VoxKnesset，一个用于研究语音随年龄变化的大规模纵向希伯来语语音数据集。该数据集包含约2300小时的议会演讲录音（2009-2025年），涉及393名发言人，录音时间跨度长达15年。每个片段都包含对齐的文本和经过验证的人口统计元数据。作者在年龄预测和说话人验证任务上对现代语音嵌入模型进行了基准测试。虽然论文本身聚焦于语音处理，但其核心贡献——构建并发布一个大规模、高质量、带有丰富元数据的纵向数据集——在方法论上与“数据资源相关”的标准高度契合。在化学信息学和质谱分析领域，类似的大规模、高质量、标注良好的数据集（如质谱-结构配对数据集）对于训练和评估化学大模型或质谱结构推理模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speech processing systems face a fundamental challenge: the human voice changes with age, yet few datasets support rigorous longitudinal evaluation. We introduce VoxKnesset, an open-access dataset of ~2,300 hours of Hebrew parliamentary speech spanning 2009-2025, comprising 393 speakers with recording spans of up to 15 years. Each segment includes aligned transcripts and verified demographic metadata from official parliamentary records. We benchmark modern speech embeddings (WavLM-Large, ECAPA-TDNN, Wav2Vec2-XLSR-1B) on age prediction and speaker verification under longitudinal conditions. Speaker verification EER rises from 2.15\% to 4.58\% over 15 years for the strongest model, and cross-sectionally trained age regressors fail to capture within-speaker aging, while longitudinally trained models recover a meaningful temporal signal. We publicly release the dataset and pipeline to support aging-robust speech systems and Hebrew speech processing.

</details>

---

### 83. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准1：论文将保形预测框架应用于图结构输出，并明确在一个真实的“分子识别”问题上进行了评估。分子可以自然地表示为图，因此该工作直接涉及利用图机器学习方法进行化学实体（分子）的预测与不确定性量化，与“化学大模型”和“质谱结构推理”（后者可视为从数据推断分子图）的研究主题相关。

**📖 中文摘要**

本文提出了一个用于图结构输出的保形预测框架，旨在为结构化输出空间（如图）提供分布自由的覆盖保证。该方法通过Z-Gromov-Wasserstein距离（实践中实例化为融合Gromov-Wasserstein距离，FGW）来定义非保形分数，从而实现预测图与候选图之间的排列不变比较。为了获得自适应的预测集，作者将保形化分位数回归（CQR）扩展到复杂输出空间，提出了分数保形化分位数回归（SCQR）。论文在一个合成任务和一个真实的分子识别问题上评估了所提出的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 84. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是开发一个自动化执行DFT计算的AI框架（TritonDFT），DFT是化学和材料科学中最核心的计算模拟方法之一，因此该工作直接属于“化学大模型”在计算化学自动化方面的前沿应用。2) 论文引入了DFTBench基准，这是一个用于评估AI智能体在DFT相关任务上能力的资源，符合“数据资源相关”标准中提供工具或基准的定义。

**📖 中文摘要**

本文介绍了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学的基石，但其实际执行涉及协调复杂、多步骤的工作流。TritonDFT通过专家策划、可扩展的工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效、准确的DFT执行。此外，论文还引入了DFTBench，一个用于评估智能体在多维度能力（包括科学专业知识、权衡优化、高性能计算知识和成本效率）的基准。TritonDFT提供了开放的用户界面供实际使用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：16
- 累计论文数量：1129

## 📝 历史记录

> 暂无历史数据

