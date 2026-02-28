# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-02-28 18:16:08

## 📅 2026-02-28 (今日最新)

**相关论文数：37**

### 1. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型，这直接属于‘化学大模型’的研究范畴。

**📖 中文摘要**

本文介绍了Zatom-1，这是首个统一3D分子和材料生成与预测学习的基础模型。它是一个基于Transformer的模型，通过多模态流匹配目标联合建模离散原子类型和连续3D几何结构。该模型支持可扩展的预训练，并能够进行快速稳定的采样。通过联合生成式预训练作为下游多任务（如性质、能量和力预测）的通用初始化，Zatom-1在生成和预测基准测试中匹配或超越了专门的基线模型，同时将生成推理时间减少了一个数量级以上。实验表明，联合生成式预训练在化学领域之间产生了正向的预测迁移：在预训练中建模材料可以提高分子性质预测的准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 2. [Energy Efficient Federated Learning with Hyperdimensional Computing (HDC)](https://arxiv.org/abs/2602.22290)

**基本信息**

- 🔗 arXiv: [`2602.22290`](https://arxiv.org/abs/2602.22290)
- 👥 作者: Yahao Ding, Yinchao Yang, Jiaxiang Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22290.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个结合超维计算（HDC）的联邦学习框架，HDC是一种用于高效处理化学信息（如分子指纹）的潜在方法，因此该框架可被视为一种可用于化学信息学领域（如分子表示学习）的工具或方法。

**📖 中文摘要**

本文研究了无线边缘网络中安全联邦学习（FL）的总能耗最小化问题。为了应对传统神经网络处理大规模分布式数据时的高计算成本和隐私挑战，作者提出了一个结合超维计算（HDC）和差分隐私（DP）的联邦学习框架（FL-HDC-DP）。每个边缘设备使用HDC进行轻量级本地训练，并应用DP噪声来保护传输的模型更新。通过联合优化HDC维度、发射功率和CPU频率来最小化总能耗。研究开发了一种高效的混合算法，结合了用于HDC维度的外部枚举搜索和用于资源分配的内部一维搜索。仿真结果表明，与基线方案相比，所提出的框架能耗降低了高达83.3%，同时保持了高精度和更快的收敛速度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper investigates the problem of minimizing total energy consumption for secure federated learning (FL) in wireless edge networks, a key paradigm for decentralized big data analytics. To tackle the high computational cost and privacy challenges of processing large-scale distributed data with conventional neural networks, we propose an FL with hyperdimensional computing and differential privacy (FL-HDC-DP) framework. Each edge device employs hyperdimensional computing (HDC) for lightweight local training and applies differential privacy (DP) noise to protect transmitted model updates. The total energy consumption is minimized through a joint optimization of the HDC dimension, transmit power, and CPU frequency. An efficient hybrid algorithm is developed, combining an outer enumeration search for HDC dimensions with an inner one-dimensional search for resource allocation. Simulation results show that the proposed framework achieves up to 83.3% energy reduction compared with baseline schemes, while maintaining high accuracy and faster convergence.

</details>

---

### 3. [Learning Rewards, Not Labels: Adversarial Inverse Reinforcement Learning for Machinery Fault Detection](https://arxiv.org/abs/2602.22297)

**基本信息**

- 🔗 arXiv: [`2602.22297`](https://arxiv.org/abs/2602.22297)
- 👥 作者: Dhiraj Neupane, Richard Dazeley, Mohamed Reda Bouadjenek 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22297.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于逆强化学习的异常检测框架，其核心思想是从正常数据序列中学习动态模式并检测偏差。这种时序模式学习和异常检测的方法论，可以迁移应用于质谱分析领域，例如从正常的质谱数据中学习模式，并用于检测异常或推断未知化合物的结构，因此与‘质谱结构推理’主题在方法论上相关。

**📖 中文摘要**

本文提出将机械故障检测（MFD）表述为一个离线逆强化学习问题，其中智能体直接从健康操作序列中学习奖励动态，从而绕过了手动奖励工程和故障标签的需求。该框架采用对抗性逆强化学习来训练一个判别器，以区分正常（专家）和策略生成的转换。判别器学习到的奖励作为异常分数，指示与正常操作行为的偏差。通过在三个运行至故障基准数据集（HUMS2023， IMS， 和 XJTU-SY）上的评估，该模型始终为正常样本分配低异常分数，为故障样本分配高分数，从而实现早期且稳健的故障检测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement learning (RL) offers significant promise for machinery fault detection (MFD). However, most existing RL-based MFD approaches do not fully exploit RL's sequential decision-making strengths, often treating MFD as a simple guessing game (Contextual Bandits). To bridge this gap, we formulate MFD as an offline inverse reinforcement learning problem, where the agent learns the reward dynamics directly from healthy operational sequences, thereby bypassing the need for manual reward engineering and fault labels. Our framework employs Adversarial Inverse Reinforcement Learning to train a discriminator that distinguishes between normal (expert) and policy-generated transitions. The discriminator's learned reward serves as an anomaly score, indicating deviations from normal operating behaviour. When evaluated on three run-to-failure benchmark datasets (HUMS2023, IMS, and XJTU-SY), the model consistently assigns low anomaly scores to normal samples and high scores to faulty ones, enabling early and robust fault detection. By aligning RL's sequential reasoning with MFD's temporal structure, this work opens a path toward RL-based diagnostics in data-driven industrial settings.

</details>

---

### 4. [Disentangling Shared and Target-Enriched Topics via Background-Contrastive Non-negative Matrix Factorization](https://arxiv.org/abs/2602.22387)

**基本信息**

- 🔗 arXiv: [`2602.22387`](https://arxiv.org/abs/2602.22387)
- 👥 作者: Yixuan Li, Archer Y. Yang, Yue Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22387.pdf)

**💡 相关性分析**

满足标准2：论文提出的背景对比非负矩阵分解（BC-NMF）是一种新颖的降维和特征提取方法，专门设计用于从高维数据（如组学数据）中分离目标特异性信号。这种数据分析和模式识别方法可以直接应用于化学信息学和质谱分析领域，用于从复杂的质谱或光谱数据中提取与特定化合物或结构相关的特征，因此提供了可用于这些主题的数据分析工具。

**📖 中文摘要**

本文介绍了背景对比非负矩阵分解（BC-NMF），该方法通过联合分解目标数据集和匹配的背景数据集，使用共享的非负基，在对比性目标下抑制背景表达的结构，从而提取目标富集的潜在主题。这种方法产生可直接在特征层面解释的非负成分，并明确隔离目标特异性变异。BC-NMF通过高效的乘法更新算法学习，该算法通过矩阵乘法实现，使其在GPU硬件上高度高效，并且通过类似于深度学习的小批量训练可扩展到大数据。在模拟和多样化的生物数据集上的实验表明，BC-NMF揭示了传统方法所掩盖的信号。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biological signals of interest in high-dimensional data are often masked by dominant variation shared across conditions. This variation, arising from baseline biological structure or technical effects, can prevent standard dimensionality reduction methods from resolving condition-specific structure. The challenge is that these confounding topics are often unknown and mixed with biological signals. Existing background correction methods are either unscalable to high dimensions or not interpretable. We introduce background contrastive Non-negative Matrix Factorization (\model), which extracts target-enriched latent topics by jointly factorizing a target dataset and a matched background using shared non-negative bases under a contrastive objective that suppresses background-expressed structure. This approach yields non-negative components that are directly interpretable at the feature level, and explicitly isolates target-specific variation. \model is learned by an efficient multiplicative update algorithm via matrix multiplication such that it is highly efficient on GPU hardware and scalable to big data via minibatch training akin to deep learning approach. Across simulations and diverse biological datasets, \model reveals signals obscured by conventional methods, including disease-associated programs in postmortem depressive brain single-cell RNA-seq, genotype-linked protein expression patterns in mice, treatment-specific transcriptional changes in leukemia, and TP53-dependent drug responses in cancer cell lines.

</details>

---

### 5. [MolFM-Lite: Multi-Modal Molecular Property Prediction with Conformer Ensemble Attention and Cross-Modal Fusion](https://arxiv.org/abs/2602.22405)

**基本信息**

- 🔗 arXiv: [`2602.22405`](https://arxiv.org/abs/2602.22405)
- 👥 作者: Syed Omer Shah, Mohammed Maqsood Ahmed, Danish Mohiuddin Mohammed 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22405.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕多模态分子表示学习，这是构建化学大模型（用于性质预测、结构推理等）的关键基础技术。

**📖 中文摘要**

本文提出了MolFM-Lite，一个用于分子性质预测的多模态模型。它联合编码SELFIES序列（1D）、分子图（2D）和构象体集合（3D），并通过跨模态注意力融合进行信息共享。模型的核心贡献包括构象体集合注意力机制和跨模态融合层。该研究在化学信息学领域直接涉及分子表示学习，这是构建化学大模型（如用于性质预测或结构推理的模型）的基础。论文还提到在ZINC250K数据集上进行预训练，并发布了所有代码、训练模型和数据分割以支持可重复性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Most machine learning models for molecular property prediction rely on a single molecular representation (either a sequence, a graph, or a 3D structure) and treat molecular geometry as static. We present MolFM-Lite, a multi-modal model that jointly encodes SELFIES sequences (1D), molecular graphs (2D), and conformer ensembles (3D) through cross-attention fusion, while conditioning predictions on experimental context via Feature-wise Linear Modulation (FiLM). Our main methodological contributions are: (1) a conformer ensemble attention mechanism that combines learnable attention with Boltzmann-weighted priors over multiple RDKit-generated conformers, capturing the thermodynamic distribution of molecular shapes; and (2) a cross-modal fusion layer where each modality can attend to others, enabling complementary information sharing. We evaluate on four MoleculeNet scaffold-split benchmarks using our model's own splits, and report all baselines re-evaluated under the same protocol. Comprehensive ablation studies across all four datasets confirm that each architectural component contributes independently, with tri-modal fusion providing 7-11% AUC improvement over single-modality baselines and conformer ensembles adding approximately 2% over single-conformer variants. Pre-training on ZINC250K (~250K molecules) using cross-modal contrastive and masked-atom objectives enables effective weight initialization at modest compute cost. We release all code, trained models, and data splits to support reproducibility.

</details>

---

### 6. [Mapping the Landscape of Artificial Intelligence in Life Cycle Assessment Using Large Language Models](https://arxiv.org/abs/2602.22500)

**基本信息**

- 🔗 arXiv: [`2602.22500`](https://arxiv.org/abs/2602.22500)
- 👥 作者: Anastasija Mensikova, Donna M. Rizzo, Kathryn Hinkelman
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22500.pdf)

**💡 相关性分析**

满足标准3：论文是关于AI（特别是大语言模型）在科学领域（生命周期评估）应用的综述，并包含对相关技术趋势的重要讨论。虽然不直接针对化学大模型或质谱，但其对AI在科学计算中应用的宏观综述与构建科学领域大模型（包括化学信息学）的背景高度相关。

**📖 中文摘要**

本文综述了人工智能（AI）在生命周期评估（LCA）中的整合应用。研究利用大语言模型（LLMs）对AI-LCA交叉领域的已发表工作进行详细回顾，以识别当前趋势、新兴主题和未来方向。分析表明，随着LCA研究的扩展，AI技术的采用急剧增长，并明显转向LLM驱动的方法。该研究通过将基于LLM的文本挖掘方法与传统的文献综述技术相结合，引入了一个动态有效的框架，能够捕捉该领域的高层研究趋势和细粒度的概念模式。这项工作展示了LLM辅助方法在支持大规模、可重复的跨领域文献综述方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integration of artificial intelligence (AI) into life cycle assessment (LCA) has accelerated in recent years, with numerous studies successfully adapting machine learning algorithms to support various stages of LCA. Despite this rapid development, comprehensive and broad synthesis of AI-LCA research remains limited. To address this gap, this study presents a detailed review of published work at the intersection of AI and LCA, leveraging large language models (LLMs) to identify current trends, emerging themes, and future directions. Our analyses reveal that as LCA research continues to expand, the adoption of AI technologies has grown dramatically, with a noticeable shift toward LLM-driven approaches, continued increases in ML applications, and statistically significant correlations between AI approaches and corresponding LCA stages. By integrating LLM-based text-mining methods with traditional literature review techniques, this study introduces a dynamic and effective framework capable of capturing both high-level research trends and nuanced conceptual patterns (themes) across the field. Collectively, these findings demonstrate the potential of LLM-assisted methodologies to support large-scale, reproducible reviews across broad research domains, while also evaluating pathways for computationally-efficient LCA in the context of rapidly developing AI technologies. In doing so, this work helps LCA practitioners incorporate state-of-the-art tools and timely insights into environmental assessments that can enhance the rigor and quality of sustainability-driven decisions and decision-making processes.

</details>

---

### 7. [LUMOS: Democratizing SciML Workflows with L0-Regularized Learning for Unified Feature and Parameter Adaptation](https://arxiv.org/abs/2602.22537)

**基本信息**

- 🔗 arXiv: [`2602.22537`](https://arxiv.org/abs/2602.22537)
- 👥 作者: Shouwei Gao, Xu Zheng, Dongsheng Luo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22537.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是科学机器学习（SciML）模型的自动化设计框架，并明确在分子科学等领域进行评估。这直接关系到如何高效构建和优化用于化学信息学任务的机器学习模型（可视为化学大模型的基础设施或方法论）。

**📖 中文摘要**

本文介绍了LUMOS，一个基于L0正则化学习的端到端框架，旨在民主化科学机器学习（SciML）模型的设计。它通过半随机门控和重参数化技术，统一了特征选择和模型剪枝，在训练过程中动态选择信息特征并剪枝冗余参数，减少了对人工调优的依赖。研究在包括分子科学在内的13个不同的SciML工作负载上评估了LUMOS，证明了其有效性和通用性。该框架直接应用于分子科学等领域的SciML模型构建，与开发用于化学信息学任务的专用、高效模型（可视为化学大模型的一种形式）高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of scientific machine learning (SciML) has accelerated discovery across diverse domains, yet designing effective SciML models remains a challenging task. In practice, building such models often requires substantial prior knowledge and manual expertise, particularly in determining which input features to use and how large the model should be. We introduce LUMOS, an end-to-end framework based on L0-regularized learning that unifies feature selection and model pruning to democratize SciML model design. By employing semi-stochastic gating and reparameterization techniques, LUMOS dynamically selects informative features and prunes redundant parameters during training, reducing the reliance on manual tuning while maintaining predictive accuracy. We evaluate LUMOS across 13 diverse SciML workloads, including cosmology and molecular sciences, and demonstrate its effectiveness and generalizability. Experiments on 13 SciML models show that LUMOS achieves 71.45% parameter reduction and a 6.4x inference speedup on average. Furthermore, Distributed Data Parallel (DDP) training on up to eight GPUs confirms the scalability of

</details>

---

### 8. [DisQ-HNet: A Disentangled Quantized Half-UNet for Interpretable Multimodal Image Synthesis Applications to Tau-PET Synthesis from T1 and FLAIR MRI](https://arxiv.org/abs/2602.22545)

**基本信息**

- 🔗 arXiv: [`2602.22545`](https://arxiv.org/abs/2602.22545)
- 👥 作者: Agamdeep S. Chopra, Caitlin Neher, Tianyi Ren 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22545.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是多模态数据融合与可解释的生成模型，用于从一种数据模态（MRI）推理/合成另一种复杂数据模态（PET图像）。这种“从数据A推理结构/属性B”的范式与“质谱结构推理”（从质谱数据推理分子结构）在方法论上高度相关，都属于科学发现中的逆向推理问题。

**📖 中文摘要**

本文提出了DisQ-HNet（DQH），一个用于从配对T1加权和FLAIR MRI合成tau-PET图像的框架，并揭示了每种模态对预测的贡献。该方法结合了（i）基于部分信息分解（PID）引导的、矢量量化的编码器，将潜在信息划分为冗余、独特和互补部分；（ii）Half-UNet解码器。该研究在包括阿尔茨海默病分类在内的下游任务中评估了模型。虽然应用领域是医学影像，但其核心方法论——使用多模态数据和可解释的深度学习模型进行复杂信号（此处为生物标记物）的预测与合成——在方法论上与“质谱结构推理”有相似之处，后者也涉及从复杂、多源数据（质谱峰）推理出结构信息。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tau positron emission tomography (tau-PET) provides an in vivo marker of Alzheimer's disease pathology, but cost and limited availability motivate MRI-based alternatives. We introduce DisQ-HNet (DQH), a framework that synthesizes tau-PET from paired T1-weighted and FLAIR MRI while exposing how each modality contributes to the prediction. The method combines (i) a Partial Information Decomposition (PID)-guided, vector-quantized encoder that partitions latent information into redundant, unique, and complementary components, and (ii) a Half-UNet decoder that preserves anatomical detail using pseudo-skip connections conditioned on structural edge cues rather than direct encoder feature reuse. Across multiple baselines (VAE, VQ-VAE, and UNet), DisQ-HNet maintains reconstruction fidelity and better preserves disease-relevant signal for downstream AD tasks, including Braak staging, tau localization, and classification. PID-based Shapley analysis provides modality-specific attribution of synthesized uptake patterns.

</details>

---

### 9. [Autoregressive Visual Decoding from EEG Signals](https://arxiv.org/abs/2602.22555)

**基本信息**

- 🔗 arXiv: [`2602.22555`](https://arxiv.org/abs/2602.22555)
- 👥 作者: Sicheng Dai, Hongwang Xiao, Shan Yu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22555.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从复杂的、高维的时序信号（EEG）中解码/重建视觉信息。这种“从复杂测量数据逆向推理出原始结构或内容”的研究范式，与“质谱结构推理”（从质谱峰逆向推理分子结构）在问题定义和技术挑战上高度相似，都属于信号解译和逆向推理问题。

**📖 中文摘要**

本文提出了AVDE，一个从脑电图（EEG）信号进行视觉解码的轻量高效框架。首先，利用预训练的EEG模型LaBraM，并通过对比学习进行微调，以对齐EEG和图像表示。其次，采用基于“下一尺度预测”策略的自回归生成框架：使用预训练的VQ-VAE将图像编码为多尺度令牌映射，并训练一个Transformer以EEG嵌入作为最粗糙表示，自回归地预测更细尺度的令牌。实验表明，AVDE在图像检索和重建任务上优于先前的方法。该研究展示了如何从复杂的、非结构化的生物信号（EEG）中解码出视觉信息，这种“从复杂信号推理结构/内容”的范式与“质谱结构推理”具有概念上的相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalogram (EEG) signals have become a popular medium for decoding visual information due to their cost-effectiveness and high temporal resolution. However, current approaches face significant challenges in bridging the modality gap between EEG and image data. These methods typically rely on complex adaptation processes involving multiple stages, making it hard to maintain consistency and manage compounding errors. Furthermore, the computational overhead imposed by large-scale diffusion models limit their practicality in real-world brain-computer interface (BCI) applications. In this work, we present AVDE, a lightweight and efficient framework for visual decoding from EEG signals. First, we leverage LaBraM, a pre-trained EEG model, and fine-tune it via contrastive learning to align EEG and image representations. Second, we adopt an autoregressive generative framework based on a "next-scale prediction" strategy: images are encoded into multi-scale token maps using a pre-trained VQ-VAE, and a transformer is trained to autoregressively predict finer-scale tokens starting from EEG embeddings as the coarsest representation. This design enables coherent generation while preserving a direct connection between the input EEG signals and the reconstructed images. Experiments on two datasets show that AVDE outperforms previous state-of-the-art methods in both image retrieval and reconstruction tasks, while using only 10% of the parameters. In addition, visualization of intermediate outputs shows that the generative process of AVDE reflects the hierarchical nature of human visual perception. These results highlight the potential of autoregressive models as efficient and interpretable tools for practical BCI applications.

</details>

---

### 10. [Molecule Mixture Detection and Design for MC Systems with Non-linear, Cross-reactive Receiver Arrays](https://arxiv.org/abs/2602.22799)

**基本信息**

- 🔗 arXiv: [`2602.22799`](https://arxiv.org/abs/2602.22799)
- 👥 作者: Bastian Heinlein, Kaikai Zhu, Sümeyye Carkit-Yilmaz 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22799.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分子通信系统中的分子混合物检测和设计，这与【化学信息学】领域直接相关，特别是涉及化学传感器（质谱分析中常用传感器类型）的信号处理和分析。

**📖 中文摘要**

本文研究了空气分子通信（MC）系统，该系统使用商业传感器进行分子混合物检测和设计。这些传感器通常表现出非线性和交叉反应行为。论文提出了几种检测器和传输方案，用于处理接收器（RX）使用非线性、交叉反应传感器的情况。所有方案都基于通过无迹变换（Unscented Transform）馈入非线性RX的符号似然的一阶和二阶矩。具体来说，论文为无符号间干扰（ISI）的传输场景提出了一个近似最大似然（AML）符号检测器，以及一个考虑接收器特性的互补混合物字母表设计算法。当在高数据速率下存在显著ISI时，AML检测器可以进行调整以利用统计ISI知识。此外，还提出了一个结合多个符号间隔信息的序列检测器。这项工作通过考虑发射机噪声、ISI和一般的非线性、交叉反应RX阵列，为一大类MC系统实现了可靠通信。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Air-based molecular communication (MC) has the potential to be one of the first MC systems to be deployed in real-world applications, enabled by commercially available sensors. However, these sensors usually exhibit non-linear and cross-reactive behavior, contrary to the idealizing assumption of linear and perfectly molecule type-specific sensing often made in the MC literature. To address this mismatch, we propose several detectors and transmission schemes for a molecule mixture communication system where the receiver (RX) employs non-linear, cross-reactive sensors. All proposed schemes are based on the first- and second-order moments of the symbol likelihoods that are fed through the non-linear RX using the Unscented Transform. In particular, we propose an approximate maximum likelihood (AML) symbol-by-symbol detector for inter-symbol-interference (ISI)-free transmission scenarios and a complementary mixture alphabet design algorithm which accounts for the RX characteristics. When significant ISI is present at high data rates, the AML detector can be adapted to exploit statistical ISI knowledge. Additionally, we propose a sequence detector which combines information from multiple symbol intervals. For settings where sequence detection is not possible due to extremely limited computational power at the RX, we propose an adaptive transmission scheme which can be combined with symbol-by-symbol detection. Using computer simulations, we validate all proposed detectors and algorithms based on the responses of commercially available sensors as well as artificially generated sensor data incorporating the characteristics of metal-oxide semiconductor sensors. By employing a general system model that accounts for transmitter noise, ISI, and general non-linear, cross-reactive RX arrays, this work enables reliable communication for a large class of MC systems.

</details>

---

### 11. [FlexMS is a flexible framework for benchmarking deep learning-based mass spectrum prediction tools in metabolomics](https://arxiv.org/abs/2602.22822)

**基本信息**

- 🔗 arXiv: [`2602.22822`](https://arxiv.org/abs/2602.22822)
- 👥 作者: Yunhua Zhong, Yixuan Tang, Yifan Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22822.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心主题是开发一个用于评估深度学习质谱预测模型的基准框架（FlexMS），这直接围绕【质谱分析】和【化学信息学】中的【质谱结构推理】主题。同时，该框架本身是一个用于模型评估和比较的工具/资源，符合标准2。

**📖 中文摘要**

本文介绍了FlexMS，一个用于在代谢组学中基准测试基于深度学习的质谱预测工具的灵活框架。质谱技术以质荷比峰的形式提供有价值的碎片化线索，对于化学分子的鉴定和性质预测至关重要。然而，实验谱图的缺乏阻碍了分子鉴定，因此迫切需要建立计算模型进行预测。深度学习模型在预测分子结构谱图方面前景广阔，但由于方法的异质性和缺乏明确定义的基准，整体评估仍然具有挑战性。为了解决这个问题，我们创建了基准框架FlexMS，用于构建和评估质谱预测中的多种模型架构。FlexMS支持动态构建众多不同的模型架构组合，同时使用不同的指标在预处理的公共数据集上评估其性能。本文提供了对影响性能因素的见解，包括数据集的结构多样性、学习率和数据稀疏性等超参数、预训练效果、元数据消融设置以及跨领域迁移学习分析。这为选择合适的模型提供了实用指导。此外，检索基准模拟了实际的鉴定场景，并根据预测的谱图对潜在匹配进行评分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The identification and property prediction of chemical molecules is of central importance in the advancement of drug discovery and material science, where the tandem mass spectrometry technology gives valuable fragmentation cues in the form of mass-to-charge ratio peaks. However, the lack of experimental spectra hinders the attachment of each molecular identification, and thus urges the establishment of prediction approaches for computational models. Deep learning models appear promising for predicting molecular structure spectra, but overall assessment remains challenging as a result of the heterogeneity in methods and the lack of well-defined benchmarks. To address this, our contribution is the creation of benchmark framework FlexMS for constructing and evaluating diverse model architectures in mass spectrum prediction. With its easy-to-use flexibility, FlexMS supports the dynamic construction of numerous distinct combinations of model architectures, while assessing their performance on preprocessed public datasets using different metrics. In this paper, we provide insights into factors influencing performance, including the structural diversity of datasets, hyperparameters like learning rate and data sparsity, pretraining effects, metadata ablation settings and cross-domain transfer learning analysis. This provides practical guidance in choosing suitable models. Moreover, retrieval benchmarks simulate practical identification scenarios and score potential matches based on predicted spectra.

</details>

---

### 12. [MEDNA-DFM: A Dual-View FiLM-MoE Model for Explainable DNA Methylation Prediction](https://arxiv.org/abs/2602.22850)

**基本信息**

- 🔗 arXiv: [`2602.22850`](https://arxiv.org/abs/2602.22850)
- 👥 作者: Yi He, Yina Cao, Jixiu Zhai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22850.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发用于DNA序列（一种化学/生物分子）甲基化模式预测和解释的深度学习模型。这属于【化学信息学】的范畴，涉及分子序列数据的建模和推理。

**📖 中文摘要**

本文提出了MEDNA-DFM，一个用于DNA甲基化预测的高性能、可解释的双视图FiLM-MoE模型。准确的DNA甲基化计算鉴定对于理解表观遗传调控至关重要。虽然深度学习在这一二元分类任务中表现出色，但其“黑箱”性质阻碍了生物学洞察。我们通过引入高性能模型MEDNA-DFM以及机制启发的信号纯化算法来解决这个问题。我们的研究表明，MEDNA-DFM能有效捕捉保守的甲基化模式，在不同物种间实现稳健区分。在外部独立数据集上的验证证实，模型的泛化能力是由保守的内在基序（如GC含量）驱动的，而非系统发育上的接近性。此外，应用我们开发的算法提取的基序比先前的研究具有显著更高的可靠性。最后，来自果蝇6mA案例研究的实证证据促使我们提出了一个“序列-结构协同”假说，表明GAGG核心基序和上游的A-tract元件协同作用。我们通过计算机诱变进一步验证了这一假说，确认消除任一或两个元件都会显著降低模型的识别能力。这项工作为甲基化预测提供了一个强大的工具，并展示了可解释的深度学习如何推动方法学创新和生物学假说的产生。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate computational identification of DNA methylation is essential for understanding epigenetic regulation. Although deep learning excels in this binary classification task, its "black-box" nature impedes biological insight. We address this by introducing a high-performance model MEDNA-DFM, alongside mechanism-inspired signal purification algorithms. Our investigation demonstrates that MEDNA-DFM effectively captures conserved methylation patterns, achieving robust distinction across diverse species. Validation on external independent datasets confirms that the model's generalization is driven by conserved intrinsic motifs (e.g., GC content) rather than phylogenetic proximity. Furthermore, applying our developed algorithms extracted motifs with significantly higher reliability than prior studies. Finally, empirical evidence from a Drosophila 6mA case study prompted us to propose a "sequence-structure synergy" hypothesis, suggesting that the GAGG core motif and an upstream A-tract element function cooperatively. We further validated this hypothesis via in silico mutagenesis, confirming that the ablation of either or both elements significantly degrades the model's recognition capabilities. This work provides a powerful tool for methylation prediction and demonstrates how explainable deep learning can drive both methodological innovation and the generation of biological hypotheses.

</details>

---

### 13. [MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis](https://arxiv.org/abs/2602.22955)

**基本信息**

- 🔗 arXiv: [`2602.22955`](https://arxiv.org/abs/2602.22955)
- 👥 作者: Feng Guo, Jiaxiang Liu, Yang Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22955.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模的多模态医学影像数据集（MM-NeuroOnco）和评估基准（MM-NeuroOnco-Bench）。虽然其直接应用领域是医学影像，但该工作核心是构建和利用高质量、语义丰富的多模态数据集来训练和评估AI模型。这种构建数据集和基准的方法论与【化学信息学】和【质谱分析】中构建用于模型训练和评估的化学/质谱数据集（如质谱库、分子属性数据集）在理念和技术路径上高度相关，属于重要的数据资源。

**📖 中文摘要**

本文介绍了MM-NeuroOnco，一个用于基于MRI的脑肿瘤诊断的大规模多模态基准和指令调优数据集。准确的脑肿瘤诊断要求模型不仅能检测病变，还能生成基于影像学表现的临床可解释推理。然而，现有的公共数据集在注释丰富性和诊断语义方面仍然有限。为了弥补这一差距，我们引入了MM-NeuroOnco，它包含来自20个数据源的24,726个MRI切片，配对了大约200,000个涵盖不同肿瘤亚型和成像模式的语义丰富的多模态指令。为了缓解诊断语义注释的稀缺性和高成本，我们开发了一个用于自动化医学信息补全和质量控制的多模型协作流程，从而能够生成超越仅掩码注释的诊断相关语义。基于此数据集，我们进一步构建了MM-NeuroOnco-Bench，这是一个带有拒绝感知设置的人工标注评估基准，以减少封闭式问题格式固有的偏见。对十个代表性模型的评估表明，即使是最强的基线模型Gemini 3 Flash，在诊断相关问题上也仅达到41.88%的准确率，突显了多模态脑肿瘤诊断理解的巨大挑战。利用MM-NeuroOnco，我们进一步提出了NeuroOnco-GPT，经过微调后，其在诊断问题上的准确率绝对提升了27%。这一结果证明了我们的数据集和基准在推进基于临床的多模态诊断推理方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate brain tumor diagnosis requires models to not only detect lesions but also generate clinically interpretable reasoning grounded in imaging manifestations, yet existing public datasets remain limited in annotation richness and diagnostic semantics. To bridge this gap, we introduce MM-NeuroOnco, a large-scale multimodal benchmark and instruction-tuning dataset for brain tumor MRI understanding, consisting of 24,726 MRI slices from 20 data sources paired with approximately 200,000 semantically enriched multimodal instructions spanning diverse tumor subtypes and imaging modalities. To mitigate the scarcity and high cost of diagnostic semantic annotations, we develop a multi-model collaborative pipeline for automated medical information completion and quality control, enabling the generation of diagnosis-related semantics beyond mask-only annotations. Building upon this dataset, we further construct MM-NeuroOnco-Bench, a manually annotated evaluation benchmark with a rejection-aware setting to reduce biases inherent in closed-ended question formats. Evaluation across ten representative models shows that even the strongest baseline, Gemini 3 Flash, achieves only 41.88% accuracy on diagnosis-related questions, highlighting the substantial challenges of multimodal brain tumor diagnostic understanding. Leveraging MM-NeuroOnco, we further propose NeuroOnco-GPT, which achieves a 27% absolute accuracy improvement on diagnostic questions following fine-tuning. This result demonstrates the effectiveness of our dataset and benchmark in advancing clinically grounded multimodal diagnostic reasoning. Code and dataset are publicly available at: this https URL

</details>

---

### 14. [SPM-Bench: Benchmarking Large Language Models for Scanning Probe Microscopy](https://arxiv.org/abs/2602.22971)

**基本信息**

- 🔗 arXiv: [`2602.22971`](https://arxiv.org/abs/2602.22971)
- 👥 作者: Peiyao Xiao, Xiaogang Li, Chengliang Xu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22971.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个自动化数据合成管道和基准测试SPM-Bench，其方法论（从科学文献中提取多模态数据、构建领域专用数据集）为构建用于“化学大模型”训练和评估的化学领域数据集提供了直接相关的技术思路和可借鉴的范式。

**📖 中文摘要**

论文提出了SPM-Bench，一个用于扫描探针显微镜（SPM）领域的多模态基准测试。其核心贡献在于一个全自动的数据合成管道，该管道利用Anchor-Gated Sieve（AGS）技术从arXiv和期刊论文（2023-2025年）中高效提取高质量的图像-文本对。这项工作虽然聚焦于SPM领域，但其提出的自动化科学数据合成范式、从海量科学文献（包括arXiv）中提取结构化多模态数据的方法，以及构建领域专用基准测试的框架，与化学信息学中构建用于训练和评估“化学大模型”的数据集和资源的需求高度相关。它为如何从科学文献中自动构建高质量、领域特定的训练和评估数据提供了一个可推广的范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As LLMs achieved breakthroughs in general reasoning, their proficiency in specialized scientific domains reveals pronounced gaps in existing benchmarks due to data contamination, insufficient complexity, and prohibitive human labor costs. Here we present SPM-Bench, an original, PhD-level multimodal benchmark specifically designed for scanning probe microscopy (SPM). We propose a fully automated data synthesis pipeline that ensures both high authority and low-cost. By employing Anchor-Gated Sieve (AGS) technology, we efficiently extract high-value image-text pairs from arXiv and journal papers published between 2023 and 2025. Through a hybrid cloud-local architecture where VLMs return only spatial coordinates "llbox" for local high-fidelity cropping, our pipeline achieves extreme token savings while maintaining high dataset purity. To accurately and objectively evaluate the performance of the LLMs, we introduce the Strict Imperfection Penalty F1 (SIP-F1) score. This metric not only establishes a rigorous capability hierarchy but also, for the first time, quantifies model "personalities" (Conservative, Aggressive, Gambler, or Wise). By correlating these results with model-reported confidence and perceived difficulty, we expose the true reasoning boundaries of current AI in complex physical scenarios. These insights establish SPM-Bench as a generalizable paradigm for automated scientific data synthesis.

</details>

---

### 15. [Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models](https://arxiv.org/abs/2602.23179)

**基本信息**

- 🔗 arXiv: [`2602.23179`](https://arxiv.org/abs/2602.23179)
- 👥 作者: Gal Kesten-Pomeranz, Yaniv Nikankin, Anja Reusch 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23179.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探究蛋白质语言模型（一种用于生物分子的“化学大模型”）内部检测序列重复模式的机制，这直接关联到“化学大模型”的可解释性和其如何编码化学/结构知识，对于构建和理解用于结构推理的模型至关重要。

**📖 中文摘要**

论文研究了蛋白质语言模型（PLMs）内部检测蛋白质序列中重复片段（包括精确重复和近似重复）的机制。作者发现PLMs通过结合基于语言的模式匹配（如归纳头）和专门的生物学知识（如编码氨基酸相似性的神经元）来解决这一生物学任务。这项工作属于对“化学大模型”（此处特指面向生物大分子的语言模型）内部工作机制的可解释性研究。它揭示了PLMs如何学习和利用化学/生物学先验知识（如氨基酸相似性）来完成特定的结构推理任务，这对于理解和改进用于“质谱结构推理”或更广泛的分子结构预测的模型具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequences are abundant in repeating segments, both as exact copies and as approximate segments with mutations. These repeats are important for protein structure and function, motivating decades of algorithmic work on repeat identification. Recent work has shown that protein language models (PLMs) identify repeats, by examining their behavior in masked-token prediction. To elucidate their internal mechanisms, we investigate how PLMs detect both exact and approximate repeats. We find that the mechanism for approximate repeats functionally subsumes that of exact repeats. We then characterize this mechanism, revealing two main stages: PLMs first build feature representations using both general positional attention heads and biologically specialized components, such as neurons that encode amino-acid similarity. Then, induction heads attend to aligned tokens across repeated segments, promoting the correct answer. Our results reveal how PLMs solve this biological task by combining language-based pattern matching with specialized biological knowledge, thereby establishing a basis for studying more complex evolutionary processes in PLMs.

</details>

---

### 16. [Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications](https://arxiv.org/abs/2602.23303)

**基本信息**

- 🔗 arXiv: [`2602.23303`](https://arxiv.org/abs/2602.23303)
- 👥 作者: Ilya Balabin, Thomas M. Kaiser
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23303.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学生物学中机器学习模型的因果推理基础理论。它旨在为构建能够理解机制而不仅仅是关联的、更强大的“化学大模型”提供数学和理论框架，这与关注主题中“化学大模型”的可靠性和可解释性发展高度相关。

**📖 中文摘要**

这篇论文是系列文章的第一部分，旨在为化学生物学中的机器学习建立一个统一的因果力学理论框架。它批判了当前将机器学习模型视为黑箱的做法，并强调需要理解数据背后的因果结构。论文提出了“焦点”这一新概念，即机器学习算法从大数据集中聚焦于隐藏底层机制的能力。作者以Akt抑制剂家族为例提供了初步证明。该工作直接针对化学和生物学领域机器学习模型的基础理论，旨在纠正当前方法在因果关系上的缺陷，这对于构建能够进行可靠推理而不仅仅是模式匹配的“化学大模型”至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning techniques are now routinely encountered in research laboratories across the globe. Impressive progress has been made through ML and AI techniques with regards to large data set processing. This progress has increased the ability of the experimenter to digest data and make novel predictions regarding phenomena of interest. However, machine learning predictors generated from data sets taken from the natural sciences are often treated as black boxes which are used broadly and generally without detailed consideration of the causal structure of the data set of interest. Work has been attempted to bring causality into discussions of machine learning models of natural phenomena; however, a firm and unified theoretical treatment is lacking. This series of three papers explores the union of chemical theory, biological theory, probability theory and causality that will correct current causal flaws of machine learning in the natural sciences. This paper, Part 1 of the series, provides the formal framework of the foundational causal structure of phenomena in chemical biology and is extended to machine learning through the novel concept of focus, defined here as the ability of a machine learning algorithm to narrow down to a hidden underpinning mechanism in large data sets. Initial proof of these principles on a family of Akt inhibitors is also provided. The second paper containing Part 2 will provide a formal exploration of chemical similarity, and Part 3 will present extensive experimental evidence of how hidden causal structures weaken all machine learning in chemical biology. This series serves to establish for chemical biology a new kind of mathematical framework for modeling mechanisms in Nature without the need for the tools of reductionism: inferential mechanics.

</details>

---

### 17. [CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction](https://arxiv.org/abs/2602.22236)

**基本信息**

- 🔗 arXiv: [`2602.22236`](https://arxiv.org/abs/2602.22236)
- 👥 作者: Rabeya Tus Sadia, Qiang Ye, Qiang Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22236.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（BioLLMs）的表示进行多模态生物分子相互作用的预测与推理。其方法论（基于LLM的表示学习与状态空间模型进行动态推理）直接围绕“化学大模型”（扩展至生物大分子）和“结构推理”（预测分子间相互作用结构）的主题。

**📖 中文摘要**

这篇论文提出了一种名为CrossLLM-Mamba的新型框架，用于预测RNA相关的相互作用（如RNA-蛋白质、RNA-小分子）。其核心创新在于利用双向Mamba编码器，实现不同模态大型语言模型（如ESM-2, RiNALMo）嵌入之间的深度“对话”，通过隐藏状态传播将相互作用建模为动态序列转换。该框架旨在从生物序列的表示中学习并预测复杂的分子间相互作用。虽然其直接应用是生物分子相互作用，但其核心方法论——利用大型语言模型的表示能力，并通过先进的序列模型（Mamba）进行多模态融合与动态推理——与“化学大模型”和从复杂数据（类比于质谱数据）中进行“结构推理”的研究主题在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of RNA-associated interactions is essential for understanding cellular regulation and advancing drug discovery. While Biological Large Language Models (BioLLMs) such as ESM-2 and RiNALMo provide powerful sequence representations, existing methods rely on static fusion strategies that fail to capture the dynamic, context-dependent nature of molecular binding. We introduce CrossLLM-Mamba, a novel framework that reformulates interaction prediction as a state-space alignment problem. By leveraging bidirectional Mamba encoders, our approach enables deep ``crosstalk'' between modality-specific embeddings through hidden state propagation, modeling interactions as dynamic sequence transitions rather than static feature overlaps. The framework maintains linear computational complexity, making it scalable to high-dimensional BioLLM embeddings. We further incorporate Gaussian noise injection and Focal Loss to enhance robustness against hard-negative samples. Comprehensive experiments across three interaction categories, RNA-protein, RNA-small molecule, and RNA-RNA demonstrate that CrossLLM-Mamba achieves state-of-the-art performance. On the RPI1460 benchmark, our model attains an MCC of 0.892, surpassing the previous best by 5.2\%. For binding affinity prediction, we achieve Pearson correlations exceeding 0.95 on riboswitch and repeat RNA subtypes. These results establish state-space modeling as a powerful paradigm for multi-modal biological interaction prediction.

</details>

---

### 18. [VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction](https://arxiv.org/abs/2602.22239)

**基本信息**

- 🔗 arXiv: [`2602.22239`](https://arxiv.org/abs/2602.22239)
- 👥 作者: Ida Egendal, Rasmus Froberg Brøndum, Dan J Woodcock 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22239.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种深度生成模型（变分自编码器），用于从高维、复杂的生物医学数据（突变谱）中提取可解释的潜在特征。这种“从数据中学习表示并进行推理”的方法论，与“质谱结构推理”中从质谱数据推断分子结构或特征的核心任务在技术路线上高度相关。

**📖 中文摘要**

这篇论文提出了VAE-MS，一种用于从癌症基因组数据中提取突变特征的非对称变分自编码器模型。突变特征分析旨在识别导致DNA突变的潜在生物学过程。该研究将神经网络（特别是概率生成模型VAE）应用于从高维、稀疏的突变计数数据中学习可解释的潜在模式（即“特征”）。这项工作展示了深度学习模型在从复杂的生物医学数据中提取有意义的、可解释的表示方面的能力。其方法论——使用深度生成模型对高维科学数据进行降维和特征发现——与化学信息学中利用模型从质谱等复杂数据中推断分子特征或结构的研究范式具有相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mutational signature analysis has emerged as a powerful method for uncovering the underlying biological processes driving cancer development. However, the signature extraction process, typically performed using non-negative matrix factorization (NMF), often lacks reliability and clinical applicability. To address these limitations, several solutions have been introduced, including the use of neural networks to achieve more accurate estimates and probabilistic methods to better capture natural variation in the data. In this work, we introduce a Variational Autoencoder for Mutational Signatures (VAE-MS), a novel model that leverages both an asymmetric architecture and probabilistic methods for the extraction of mutational signatures. VAE-MS is compared to with three state-of-the-art models for mutational signature extraction: SigProfilerExtractor, the NMF-based gold standard; MUSE-XAE, an autoencoder that employs an asymmetric design without probabilistic components; and SigneR, a Bayesian NMF model, to illustrate the strength in combining a nonlinear extraction with a probabilistic model. In the ability to reconstruct input data and generalize to unseen data, models with probabilistic components (VAE-MS, SigneR) dramatically outperformed models without (SigProfilerExtractor, MUSE-XAE). The NMF-baed models (SigneR, SigProfilerExtractor) had the most accurate reconstructions in simulated data, while VAE-MS reconstructed more accurately on real cancer data. Upon evaluating the ability to extract signatures consistently, no model exhibited a clear advantage over the others. Software for VAE-MS is available at this https URL .

</details>

---

### 19. [Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)](https://arxiv.org/abs/2602.22248)

**基本信息**

- 🔗 arXiv: [`2602.22248`](https://arxiv.org/abs/2602.22248)
- 👥 作者: Julia Gonski, Jenni Ott, Shiva Abbaszadeh 等100人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22248.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及在科学计算中（特别是粒子物理）部署和优化机器学习模型所需的硬件和系统架构。虽然应用领域不同，但其对大规模、低延迟科学ML模型在专用硬件上实现的技术讨论，与构建和部署需要处理海量数据、进行复杂推理的“化学大模型”系统所面临的核心工程挑战直接相关。

**📖 中文摘要**

这篇论文探讨了在粒子物理实验中应用机器学习所面临的硬件挑战和机遇，特别关注异构计算、边缘计算和量子硬件。虽然领域不同，但论文中深入讨论了为应对极端数据速率和实时推理需求，在专用硬件（如低功耗边缘设备、可重构硬件、模拟计算）上部署和优化机器学习模型（包括可能的未来大模型）的策略。这些关于在资源受限环境下高效部署和运行复杂模型的技术讨论，对于旨在处理海量化合物质谱数据、需要进行实时或近实时结构推理的“化学大模型”系统具有重要的参考价值，涉及模型压缩、硬件协同设计等共性挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The next generation of particle physics experiments will face a new era of challenges in data acquisition, due to unprecedented data rates and volumes along with extreme environments and operational constraints. Harnessing this data for scientific discovery demands real-time inference and decision-making, intelligent data reduction, and efficient processing architectures beyond current capabilities. Crucial to the success of this experimental paradigm are several emerging technologies, such as artificial intelligence and machine learning (AI/ML) and silicon microelectronics, and the advent of quantum algorithms and processing. Their intersection includes areas of research such as low-power and low-latency devices for edge computing, heterogeneous accelerator systems, reconfigurable hardware, novel codesign and synthesis strategies, readout for cryogenic or high-radiation environments, and analog computing. This white paper presents a community-driven vision to identify and prioritize research and development opportunities in hardware-based ML systems and corresponding physics applications, contributing towards a successful transition to the new data frontier of fundamental science.

</details>

---

### 20. [Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486)

**基本信息**

- 🔗 arXiv: [`2602.22486`](https://arxiv.org/abs/2602.22486)
- 👥 作者: Shivam Kumar, Yixin Wang, Lizhen Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22486.pdf)

**💡 相关性分析**

满足标准1：论文的核心理论分析直接围绕生成建模方法（流匹配）展开，该方法在分子结构生成等场景中表现出色，而分子结构生成是'质谱结构推理'和'化学大模型'（特别是生成模型）的核心应用之一。论文为这类模型在流形数据上的有效性提供了理论解释。

**📖 中文摘要**

这篇论文从理论上分析了流匹配（Flow Matching）方法，这是一种用于生成建模的无模拟替代方案，特别适用于数据集中在低维流形上的高维场景。论文的核心贡献在于，当目标分布支撑在光滑流形上时，为流匹配方法建立了非渐近收敛保证和统计一致性。研究结果表明，流匹配能够自适应于数据的内在几何结构，规避维度灾难，其收敛速率仅依赖于内在维度。这一理论分析为流匹配在分子结构生成等领域的成功提供了原理性解释。由于分子结构生成是化学信息学和质谱分析中结构推理的核心问题，该论文提出的理论框架和分析方法为开发用于质谱结构推理的生成式化学大模型（特别是基于流的模型）提供了重要的理论基础和理论保证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow matching has emerged as a simulation-free alternative to diffusion-based generative modeling, producing samples by solving an ODE whose time-dependent velocity field is learned along an interpolation between a simple source distribution (e.g., a standard normal) and a target data distribution. Flow-based methods often exhibit greater training stability and have achieved strong empirical performance in high-dimensional settings where data concentrate near a low-dimensional manifold, such as text-to-image synthesis, video generation, and molecular structure generation. Despite this success, existing theoretical analyses of flow matching assume target distributions with smooth, full-dimensional densities, leaving its effectiveness in manifold-supported settings largely unexplained. To this end, we theoretically analyze flow matching with linear interpolation when the target distribution is supported on a smooth manifold. We establish a non-asymptotic convergence guarantee for the learned velocity field, and then propagate this estimation error through the ODE to obtain statistical consistency of the implicit density estimator induced by the flow-matching objective. The resulting convergence rate is near minimax-optimal, depends only on the intrinsic dimension, and reflects the smoothness of both the manifold and the target distribution. Together, these results provide a principled explanation for how flow matching adapts to intrinsic data geometry and circumvents the curse of dimensionality.

</details>

---

### 21. [Discovery of Interpretable Physical Laws in Materials via Language-Model-Guided Symbolic Regression](https://arxiv.org/abs/2602.22967)

**基本信息**

- 🔗 arXiv: [`2602.22967`](https://arxiv.org/abs/2602.22967)
- 👥 作者: Yifeng Guan, Chuyi Liu, Dongzhan Zhou 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22967.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个由大语言模型（LLM）引导的、用于发现材料科学中物理定律的框架。这直接属于'化学大模型'的研究范畴，即利用先进的人工智能模型（特别是LLM）来解决化学和材料科学中的复杂问题，如从数据中推导 interpretable 的物理规律。

**📖 中文摘要**

本文提出了一种利用大型语言模型（LLM）引导符号回归（Symbolic Regression）来从高维数据中发现可解释物理定律的框架。该方法旨在缓解传统符号回归在搜索巨大可能形式空间时产生的组合爆炸问题。研究者通过利用LLM中嵌入的科学知识来引导搜索过程，从而高效地识别数据中的物理定律。该方法在钙钛矿材料的关键属性建模上进行了验证，成功地将有效搜索空间减少了约10^5倍，并识别出了用于体模量、带隙和析氧反应活性的新公式。这些公式不仅提供了有意义的物理见解，而且在准确性和简洁性上超越了以往的公式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering interpretable physical laws from high-dimensional data is a fundamental challenge in scientific research. Traditional methods, such as symbolic regression, often produce complex, unphysical formulas when searching a vast space of possible forms. We introduce a framework that guides the search process by leveraging the embedded scientific knowledge of large language models, enabling efficient identification of physical laws in the data. We validate our approach by modeling key properties of perovskite materials. Our method mitigates the combinatorial explosion commonly encountered in traditional symbolic regression, reducing the effective search space by a factor of approximately $10^5$. A set of novel formulas for bulk modulus, band gap, and oxygen evolution reaction activity are identified, which not only provide meaningful physical insights but also outperform previous formulas in accuracy and simplicity.

</details>

---

### 22. [Efficient Graph Coloring with Neural Networks: A Physics-Inspired Approach for Large Graphs](https://arxiv.org/abs/2408.01503)

**基本信息**

- 🔗 arXiv: [`2408.01503`](https://arxiv.org/abs/2408.01503)
- 👥 作者: Lorenzo Colantonio, Andrea Cacioppo, Federico Scarpati 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2408.01503.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于解决组合优化问题（图着色）的神经求解器框架。虽然应用领域是图论，但该方法论（结合GNN与物理原理的神经框架）对于构建用于分子性质预测、分子图生成或化学反应推理的'化学大模型'具有重要的借鉴意义。这类模型的核心挑战之一就是处理分子图表示和相关的组合优化问题。

**📖 中文摘要**

本文介绍了一种受物理学启发的神经框架，用于解决大规模图着色问题，这是一种典型的组合优化问题。该框架结合了图神经网络（GNN）和统计力学原理，通过集成基于种植的监督信号、对称性破缺正则化和迭代噪声退火神经动力学，来导航聚集的解空间。研究表明，当迭代次数与图规模呈二次方关系时，学习到的求解器在随机图中能达到接近理论动态相变的算法阈值。该模型能够从小的训练图泛化到规模大几个数量级的实例，证明了神经架构可以学习到在组合优化的硬连通区域仍然有效的可扩展算法策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Combinatorial optimization problems near algorithmic phase transitions represent a fundamental challenge for both classical algorithms and machine learning approaches. Among them, graph coloring stands as a prototypical constraint satisfaction problem exhibiting sharp dynamical and satisfiability thresholds. Here we introduce a physics-inspired neural framework that learns to solve large-scale graph coloring instances by combining graph neural networks with statistical-mechanics principles. Our approach integrates a planting-based supervised signal, symmetry-breaking regularization, and iterative noise-annealed neural dynamics to navigate clustered solution landscapes. When the number of iterations scales quadratically with graph size, the learned solver reaches algorithmic thresholds close to the theoretical dynamical transition in random graphs and achieves near-optimal detection performance in the planted inference regime. The model generalizes from small training graphs to instances orders of magnitude larger, demonstrating that neural architectures can learn scalable algorithmic strategies that remain effective in hard connectivity regions. These results establish a general paradigm for learning neural solvers that operate near fundamental phase boundaries in combinatorial optimization and inference.

</details>

---

### 23. [CLIP-Free, Label Free, Unsupervised Concept Bottleneck Models](https://arxiv.org/abs/2503.10981)

**基本信息**

- 🔗 arXiv: [`2503.10981`](https://arxiv.org/abs/2503.10981)
- 👥 作者: Fawaz Sammani, Jonas Fischer, Nikos Deligiannis
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.10981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的、无需外部标注或CLIP模型的概念瓶颈模型（CBM）。CBM是一种旨在提高AI模型可解释性的架构，通过将特征映射到人类可解释的概念。这项工作在机器学习可解释性方面属于前沿探索，其方法论对于构建可解释的'化学大模型'（例如，将分子特征映射到化学官能团或反应类型等概念）具有直接的启发和参考价值。

**📖 中文摘要**

本文提出了一种无需CLIP模型、无需图像-概念标注、且能以无监督方式推导线性分类器的概念瓶颈模型（CBM）构建方法。该方法通过将任何冻结的视觉分类器的分布（在离散类别索引上）与其对应的、从文本类别名称衍生的视觉-语言对应分布对齐，同时保持分类器的性能，从而将分类器转换为CBM。该方法不需要真实图像-类别标注，具有很高的数据效率，并保留了分类器的推理过程。在超过40个视觉分类器上的应用和测试表明，所得到的无监督、无标签、无CLIP的CBM（U-F^2-CBM）设立了新的性能标杆，甚至超过了有监督的基于CLIP的CBM。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) map dense feature representations into human-interpretable concepts which are then combined linearly to make a prediction. However, modern CBMs rely on the CLIP model to obtain image-concept annotations, and it remains unclear how to design CBMs without the CLIP bottleneck. Methods that do not use CLIP instead require manual, labor intensive annotation to associate feature representations with concepts. Furthermore, all CBMs necessitate training a linear classifier to map the extracted concepts to class labels. In this work, we lift all three limitations simultaneously by proposing a method that converts any frozen visual classifier into a CBM without requiring image-concept labels (label-free), without relying on the CLIP model (CLIP-free), and by deriving the linear classifier in an unsupervised manner. Our method is formulated by aligning the original classifier's distribution (over discrete class indices) with its corresponding vision-language counterpart distribution derived from textual class names, while preserving the classifier's performance. The approach requires no ground-truth image-class annotations, and is highly data-efficient and preserves the classifier's reasoning process. Applied and tested on over 40 visual classifiers, our resulting unsupervised, label-free and CLIP-free CBM (U-F$^2$-CBM) sets a new state of the art, surpassing even supervised CLIP-based CBMs. We also show that our method can be used for zero-shot image captioning, outperforming existing methods based on CLIP, and achieving state-of-art.

</details>

---

### 24. [The Spacetime of Diffusion Models: An Information Geometry Perspective](https://arxiv.org/abs/2505.17517)

**基本信息**

- 🔗 arXiv: [`2505.17517`](https://arxiv.org/abs/2505.17517)
- 👥 作者: Rafał Karczewski, Markus Heinonen, Alison Pouplin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.17517.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散模型的几何结构和潜在表示，这与“化学大模型”主题中用于分子生成和设计的生成模型（如扩散模型）直接相关。论文提出的几何视角和编辑距离为理解和操作这类大模型提供了新的理论基础。

**📖 中文摘要**

本文从信息几何的角度提出了对扩散模型潜在空间的新颖几何视角。作者指出，传统的基于确定性概率流ODE解码器的回拉方法存在根本性缺陷，因为它强制要求测地线在数据空间中解码为直线段，从而忽略了数据的内在几何结构。作为补充，扩散模型也允许通过反向SDE进行随机解码，这使得可以使用Fisher-Rao度量进行信息几何处理。然而，选择x_T作为潜在表示会由于无记忆性而导致该度量坍缩。为了解决这个问题，作者引入了一个潜在时空z=(x_t, t)，该时空索引了所有噪声尺度下的去噪分布族p(x_0 | x_t)，从而产生了一个非平凡的几何结构。他们证明了这些分布形成了一个指数族，并推导了曲线长度的无模拟估计器，从而实现了高效的测地线计算。由此产生的结构引入了一种原则性的扩散编辑距离，其中测地线追踪数据之间噪声和去噪编辑的最小序列。作者还展示了该方法在分子系统（包括约束变体，如低方差跃迁和区域规避）中过渡路径采样的好处。这项工作为理解和操作扩散模型的潜在几何结构提供了一个理论框架，与“化学大模型”的主题相关，因为它为生成模型（如用于分子设计的扩散模型）提供了理论基础和几何解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a novel geometric perspective on the latent space of diffusion models. We first show that the standard pullback approach, utilizing the deterministic probability flow ODE decoder, is fundamentally flawed. It provably forces geodesics to decode as straight segments in data space, effectively ignoring any intrinsic data geometry beyond the ambient Euclidean space. Complementing this view, diffusion also admits a stochastic decoder via the reverse SDE, which enables an information geometric treatment with the Fisher-Rao metric. However, a choice of $x_T$ as the latent representation collapses this metric due to memorylessness. We address this by introducing a latent spacetime $z=(x_t,t)$ that indexes the family of denoising distributions $p(x_0 | x_t)$ across all noise scales, yielding a nontrivial geometric structure. We prove these distributions form an exponential family and derive simulation-free estimators for curve lengths, enabling efficient geodesic computation. The resulting structure induces a principled Diffusion Edit Distance, where geodesics trace minimal sequences of noise and denoise edits between data. We also demonstrate benefits for transition path sampling in molecular systems, including constrained variants such as low-variance transitions and region avoidance. Code is available at: this https URL .

</details>

---

### 25. [Random Matrix Theory-guided sparse PCA for single-cell RNA-seq data](https://arxiv.org/abs/2509.15429)

**基本信息**

- 🔗 arXiv: [`2509.15429`](https://arxiv.org/abs/2509.15429)
- 👥 作者: Victor Chardès
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.15429.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于分析高通量生物分子数据（单细胞RNA-seq）的机器学习方法。虽然标题未直接提及“化学信息学”，但单细胞RNA-seq数据分析是化学生物学和计算生物学交叉领域的核心任务，属于广义的化学信息学范畴。论文提出的RMT引导的稀疏PCA方法是一种新颖的数据分析和特征提取技术，可用于从复杂的化学/生物测量数据中推断有意义的模式。

**📖 中文摘要**

本文提出了一种基于随机矩阵理论（RMT）的稀疏主成分分析（PCA）方法，用于处理单细胞RNA测序数据。单细胞RNA-seq数据噪声大，变异性来源于生物学差异和技术因素，使得计算流程难以适应异构数据集或不断发展的技术。尽管PCA在高维数据中存在已知偏差，但由于其可解释性和鲁棒性，大多数研究仍依赖其进行降维。本文改进了PCA，提出了一种RMT引导的方法，利用现有的稀疏PCA算法来推断稀疏主成分。作者首先引入了一种新颖的双白化算法，该算法自洽地估计了每个基因在单个细胞中受转录组噪声影响的大小，而无需假设特定的噪声分布。这使得能够使用基于RMT的标准自动选择稀疏度水平，从而使稀疏PCA几乎无需参数调整。这种基于数学的方法保留了PCA的可解释性，同时实现了对稀疏主成分的稳健、无需手动干预的推断。在七种单细胞RNA-seq技术和四种稀疏PCA算法上的实验表明，该方法系统地改善了主子空间的重建，并在细胞类型分类任务中持续优于基于PCA、自编码器和扩散的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell RNA-seq provides detailed molecular snapshots of individual cells but is notoriously noisy. Variability stems from biological differences and technical factors, such as amplification bias and limited RNA capture efficiency, making it challenging to adapt computational pipelines to heterogeneous datasets or evolving technologies. As a result, most studies still rely on principal component analysis (PCA) for dimensionality reduction, valued for its interpretability and robustness, in spite of its known bias in high dimensions. Here, we improve upon PCA with a Random Matrix Theory (RMT)-based approach that guides the inference of sparse principal components using existing sparse PCA algorithms. We first introduce a novel biwhitening algorithm which self-consistently estimates the magnitude of transcriptomic noise affecting each gene in individual cells, without assuming a specific noise distribution. This enables the use of an RMT-based criterion to automatically select the sparsity level, rendering sparse PCA nearly parameter-free. Our mathematically grounded approach retains the interpretability of PCA while enabling robust, hands-off inference of sparse principal components. Across seven single-cell RNA-seq technologies and four sparse PCA algorithms, we show that this method systematically improves the reconstruction of the principal subspace and consistently outperforms PCA-, autoencoder-, and diffusion-based methods in cell-type classification tasks.

</details>

---

### 26. [Object-Centric Representation Learning for Enhanced 3D Semantic Scene Graph Prediction](https://arxiv.org/abs/2510.04714)

**基本信息**

- 🔗 arXiv: [`2510.04714`](https://arxiv.org/abs/2510.04714)
- 👥 作者: KunHo Heo, GiHyun Kim, SuYeon Kim 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04714.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于3D场景理解的机器学习模型，特别是对象检测和关系预测。虽然应用领域是机器人视觉，但其核心方法论——设计判别性特征编码器、使用对比学习进行预训练、整合多模态（几何和语义）特征——是机器学习在结构化数据推理中的高级应用。这些方法与“化学大模型”和“质谱结构推理”中所需的、从复杂数据（如分子图或质谱图）中学习表示和关系有概念上的相似性。论文提出的技术（如对比预训练、特征解耦）可以启发化学信息学中类似问题的解决方案。

**📖 中文摘要**

本文研究了3D语义场景图预测任务，该任务旨在检测3D场景中的对象及其语义关系，是机器人和AR/VR应用的关键技术。先前的研究虽然解决了数据集限制并探索了包括开放词汇设置在内的各种方法，但经常未能优化对象和关系特征的表示能力，表现出对图神经网络的过度依赖，尽管其判别能力不足。在这项工作中，作者通过广泛分析证明，对象特征的质量在决定整体场景图准确性方面起着关键作用。为了解决这一挑战，他们设计了一个高度判别性的对象特征编码器，并采用了一种对比预训练策略，将对象表示学习与场景图预测解耦。这种设计不仅提高了对象分类的准确性，还直接改善了关系预测。值得注意的是，当将预训练的编码器插入现有框架时，在所有评估指标上都观察到了显著的性能提升。此外，虽然现有方法尚未充分利用关系信息的整合，但作者有效地结合了几何和语义特征，实现了更优的关系预测。在3DSSG数据集上的综合实验表明，该方法显著优于先前的最先进方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

3D Semantic Scene Graph Prediction aims to detect objects and their semantic relationships in 3D scenes, and has emerged as a crucial technology for robotics and AR/VR applications. While previous research has addressed dataset limitations and explored various approaches including Open-Vocabulary settings, they frequently fail to optimize the representational capacity of object and relationship features, showing excessive reliance on Graph Neural Networks despite insufficient discriminative capability. In this work, we demonstrate through extensive analysis that the quality of object features plays a critical role in determining overall scene graph accuracy. To address this challenge, we design a highly discriminative object feature encoder and employ a contrastive pretraining strategy that decouples object representation learning from the scene graph prediction. This design not only enhances object classification accuracy but also yields direct improvements in relationship prediction. Notably, when plugging in our pretrained encoder into existing frameworks, we observe substantial performance improvements across all evaluation metrics. Additionally, whereas existing approaches have not fully exploited the integration of relationship information, we effectively combine both geometric and semantic features to achieve superior relationship prediction. Comprehensive experiments on the 3DSSG dataset demonstrate that our approach significantly outperforms previous state-of-the-art methods. Our code is publicly available at this https URL .

</details>

---

### 27. [Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics](https://arxiv.org/abs/2601.22123)

**基本信息**

- 🔗 arXiv: [`2601.22123`](https://arxiv.org/abs/2601.22123)
- 👥 作者: Winfried Ripken, Michael Plainer, Gregor Lied 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22123.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个机器学习框架来学习哈密顿系统的演化映射，这直接属于利用大模型/机器学习方法理解和模拟复杂化学/物理系统（如分子动力学）的范畴，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一种学习哈密顿流映射的框架，用于模拟哈密顿系统的长时间演化。该方法通过预测选定时间跨度内的平均相空间演化，实现了远超经典积分器稳定性限制的大时间步长更新。核心是施加了一个关于时间平均哈密顿动力学的“平均流一致性”条件。与先前方法不同，该方法允许在无需访问未来状态的情况下，在独立的相空间样本上进行训练，避免了昂贵的轨迹生成。该方法在包括使用机器学习力场（MLFF）的分子动力学模拟在内的多种哈密顿系统中得到验证。该框架旨在克服小时间步长的限制，通过机器学习模型直接学习从相空间状态到未来状态演化的映射，这与“化学大模型”中利用机器学习模型学习复杂物理/化学系统演化规律的核心主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn Hamiltonian Flow Maps by predicting the mean phase-space evolution over a chosen time span, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a Mean Flow consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available trajectory-free MLFF datasets.

</details>

---

### 28. [A Minimum Variance Path Principle for Accurate and Stable Score-Based Density Ratio Estimation](https://arxiv.org/abs/2602.00834)

**基本信息**

- 🔗 arXiv: [`2602.00834`](https://arxiv.org/abs/2602.00834)
- 👥 作者: Wei Chen, Jiacheng Li, Shigui Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00834.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进基于分数的机器学习方法，用于密度比估计等任务。虽然未明确提及化学或质谱，但其核心方法论——开发更优的生成模型或概率模型训练框架——是构建“化学大模型”（如用于分子生成、性质预测的生成模型）和进行“质谱结构推理”（如从质谱数据推断分子结构的概率建模）所依赖的基础技术之一。

**📖 中文摘要**

本文研究了基于分数的密度比估计方法。作者发现，尽管基于分数的方法在理论上是路径无关的，但在实际训练中却表现出路径依赖性。他们通过证明实际训练目标与理想目标之间相差一个关键的被忽视项——分数函数的路径方差——来解决这一悖论。为此，他们提出了“最小方差路径”（MVP）原则来最小化该路径方差。主要贡献是推导出了方差的闭式表达式，使优化变得可行。通过使用灵活的Kumaraswamy混合模型对路径进行参数化，该方法可以学习数据自适应的低方差路径，而无需启发式手动选择。这种对完整目标的优化产生了更准确和稳定的估计器。这项工作为优化基于分数的插值提供了一个通用框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Score-based methods are powerful across machine learning, but they face a paradox: theoretically path-independent, yet practically path-dependent. We resolve this by proving that practical training objectives differ from the ideal, ground-truth objective by a crucial, overlooked term: the path variance of the score function. We propose the MVP (**M**imum **V**ariance **P**ath) Principle to minimize this path variance. Our key contribution is deriving a closed-form expression for the variance, making optimization tractable. By parameterizing the path with a flexible Kumaraswamy Mixture Model, our method learns data-adaptive, low-variance paths without heuristic manual selection. This principled optimization of the complete objective yields more accurate and stable estimators, establishing new state-of-the-art results on challenging benchmarks and providing a general framework for optimizing score-based interpolation.

</details>

---

### 29. [Phase Transitions for Feature Learning in Neural Networks](https://arxiv.org/abs/2602.01434)

**基本信息**

- 🔗 arXiv: [`2602.01434`](https://arxiv.org/abs/2602.01434)
- 👥 作者: Andrea Montanari, Zihao Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01434.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是神经网络（作为大模型的基础组件）在高维数据下的特征学习机制和相变行为。理解神经网络如何从数据中学习有效的低维表示，对于构建和理解“化学大模型”（例如，从分子结构数据学习分子表示）以及改进“质谱结构推理”中的特征提取至关重要。这属于机器学习基础理论与应用主题的交叉。

**📖 中文摘要**

本文研究了神经网络在学习多索引模型时的特征学习动态。在此设置下，响应变量仅通过一个k维投影依赖于高维协变量。特征学习即学习这个潜在空间。作者在比例渐近（n, d→∞， n/d→δ）的框架下，研究了两层神经网络的梯度下降动力学，其中潜在空间维度k和隐藏神经元数量m固定。先前工作表明，当δ超过一个依赖于数据分布的阈值δ_alg时，通过多项式时间算法进行特征学习是可能的。本文推导出了两层网络的类似阈值δ_NN。该阈值由以下场景决定：训练首先访问经验风险梯度较大的点，学习这些梯度所跨越的方向；然后梯度变小，动力学由Hessian矩阵的负方向主导。阈值δ_NN对应于第二阶段Hessian谱的相变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

According to a popular viewpoint, neural networks learn from data by first identifying low-dimensional representations, and subsequently fitting the best model in this space. Recent works provide a formalization of this phenomenon when learning multi-index models. In this setting, we are given $n$ i.i.d. pairs $({\boldsymbol x}_i,y_i)$, where the covariate vectors ${\boldsymbol x}_i\in\mathbb{R}^d$ are isotropic, and responses $y_i$ only depend on ${\boldsymbol x}_i$ through a $k$-dimensional projection ${\boldsymbol \Theta}_*^{\sf T}{\boldsymbol x}_i$. Feature learning amounts to learning the latent space spanned by ${\boldsymbol \Theta}_*$. In this context, we study the gradient descent dynamics of two-layer neural networks under the proportional asymptotics $n,d\to\infty$, $n/d\to\delta$, while the dimension of the latent space $k$ and the number of hidden neurons $m$ are kept fixed. Earlier work establishes that feature learning via polynomial-time algorithms is possible if $\delta> \delta_{\text{alg}}$, for $\delta_{\text{alg}}$ a threshold depending on the data distribution, and is impossible (within a certain class of algorithms) below $\delta_{\text{alg}}$. Here we derive an analogous threshold $\delta_{\text{NN}}$ for two-layer networks. Our characterization of $\delta_{\text{NN}}$ opens the way to study the dependence of learning dynamics on the network architecture and training algorithm. The threshold $\delta_{\text{NN}}$ is determined by the following scenario. Training first visits points for which the gradient of the empirical risk is large and learns the directions spanned by these gradients. Then the gradient becomes smaller and the dynamics becomes dominated by negative directions of the Hessian. The threshold $\delta_{\text{NN}}$ corresponds to a phase transition in the spectrum of the Hessian in this second phase.

</details>

---

### 30. [Controlling Exploration-Exploitation in GFlowNets via Markov Chain Perspectives](https://arxiv.org/abs/2602.01749)

**基本信息**

- 🔗 arXiv: [`2602.01749`](https://arxiv.org/abs/2602.01749)
- 👥 作者: Lin Chen, Samuel Drapeau, Fanghao Shao 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.01749.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进生成流网络（GFlowNet），这是一种用于结构化对象（如分子、图）生成的生成模型。GFlowNet是构建“化学大模型”（用于分子生成、优化）的重要工具之一。本文提出的方法旨在更好地控制生成过程中的探索与利用，这对于在化学空间中进行高效搜索和发现新分子结构具有直接意义。

**📖 中文摘要**

本文研究了生成流网络（GFlowNet）中的探索-利用权衡问题。作者通过进一步探索GFlowNet与马尔可夫链之间的联系，建立了GFlowNet目标与马尔可夫链可逆性之间的等价关系，从而揭示了训练中隐含约束的根源，并提供了一个将马尔可夫链性质适配到GFlowNet的框架。基于这些理论发现，作者提出了α-GFN，通过一个可调参数α来泛化前向与后向策略的混合。这种泛化使得能够直接控制探索-利用动态以增强模式发现能力，同时确保收敛到唯一的流。在多个基准测试上的实验表明，α-GFN目标 consistently 优于先前的GFlowNet目标。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative Flow Network (GFlowNet) objectives implicitly fix an equal mixing of forward and backward policies, potentially constraining the exploration-exploitation trade-off during training. By further exploring the link between GFlowNets and Markov chains, we establish an equivalence between GFlowNet objectives and Markov chain reversibility, thereby revealing the origin of such constraints, and provide a framework for adapting Markov chain properties to GFlowNets. Building on these theoretical findings, we propose $\alpha$-GFNs, which generalize the mixing via a tunable parameter $\alpha$. This generalization enables direct control over exploration-exploitation dynamics to enhance mode discovery capabilities, while ensuring convergence to unique flows. Across various benchmarks, including Set, Bit Sequence, and Molecule Generation, $\alpha$-GFN objectives consistently outperform previous GFlowNet objectives, achieving up to a $10 \times$ increase in the number of discovered modes.

</details>

---

### 31. [VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations](https://arxiv.org/abs/2602.02334)

**基本信息**

- 🔗 arXiv: [`2602.02334`](https://arxiv.org/abs/2602.02334)
- 👥 作者: Fatemeh Zargarbashi, Dhruv Agrawal, Jakob Buhmann 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.02334.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于（残差）向量量化自编码器的生成模型，用于解耦数据中的风格与内容。虽然应用领域是人体运动，但其核心方法论——使用量化自编码器学习解耦的、层次化的表示——与“化学大模型”中用于分子表示学习（例如，解耦分子的功能团和骨架）或“质谱结构推理”中解耦质谱信号的不同来源（如碎片化模式与分子子结构）的技术路线高度相似。

**📖 中文摘要**

本文提出了一种新颖的方法，用于有效解耦人体运动数据中的风格和内容，以促进风格迁移。该方法基于内容对应粗略运动属性而风格捕捉更精细、富有表现力的细节这一洞见。为了建模这种层次结构，作者采用残差向量量化变分自编码器（RVQ-VAEs）来学习从粗到细的运动表示。通过将码本学习与对比学习以及一种新颖的信息泄漏损失相结合，以在不同码本中组织内容和风格，从而进一步增强解耦。作者利用这种解耦表示，通过一种简单有效的推理时技术“量化码交换”，实现了无需对未见风格进行任何微调的运动风格迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Human motion data is inherently rich and complex, containing both semantic content and subtle stylistic features that are challenging to model. We propose a novel method for effective disentanglement of the style and content in human motion data to facilitate style transfer. Our approach is guided by the insight that content corresponds to coarse motion attributes while style captures the finer, expressive details. To model this hierarchy, we employ Residual Vector Quantized Variational Autoencoders (RVQ-VAEs) to learn a coarse-to-fine representation of motion. We further enhance the disentanglement by integrating codebook learning with contrastive learning and a novel information leakage loss to organize the content and the style across different codebooks. We harness this disentangled representation using our simple and effective inference-time technique Quantized Code Swapping, which enables motion style transfer without requiring any fine-tuning for unseen styles. Our framework demonstrates strong versatility across multiple inference applications, including style transfer, style removal, and motion blending.

</details>

---

### 32. [Document Reconstruction Unlocks Scalable Long-Context RLVR](https://arxiv.org/abs/2602.08237)

**基本信息**

- 🔗 arXiv: [`2602.08237`](https://arxiv.org/abs/2602.08237)
- 👥 作者: Yao Xiao, Lei Wang, Yue Deng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.08237.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于强化学习的训练框架，用于提升大语言模型处理长上下文的能力。虽然应用场景是通用文档重建，但其核心方法——使用强化学习优化模型在特定任务（此处为文档补全）上的表现——是训练和优化“化学大模型”或用于“质谱结构推理”的专业化语言/多模态模型时可能采用的关键技术之一，特别是当需要模型根据不完整的化学信息（如部分质谱峰或分子描述）进行推理和补全时。

**📖 中文摘要**

本文研究了一种无监督方法来增强大语言模型（LLMs）的长上下文能力，无需昂贵的人工标注或教师模型的监督。具体方法是：首先在长文档中用特殊占位符替换几个段落，然后通过强化学习训练LLMs，通过从一组候选选项中正确识别和排序缺失的段落来重建文档。这种训练范式使模型能够捕捉全局叙事连贯性，从而显著提升长上下文性能。作者在两个广泛使用的基准测试上验证了该方法的有效性。此外，还进行了广泛的消融研究，分析了奖励设计、数据策划策略、训练方案和数据缩放效应对模型性能的影响。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards~(RLVR) has become a prominent paradigm to enhance the capabilities (i.e.\ long-context) of Large Language Models~(LLMs). However, it often relies on gold-standard answers or explicit evaluation rubrics provided by powerful teacher models or human experts, which are costly and time-consuming. In this work, we investigate unsupervised approaches to enhance the long-context capabilities of LLMs, eliminating the need for heavy human annotations or teacher models' supervision. Specifically, we first replace a few paragraphs with special placeholders in a long document. LLMs are trained through reinforcement learning to reconstruct the document by correctly identifying and sequencing missing paragraphs from a set of candidate options. This training paradigm enables the model to capture global narrative coherence, significantly boosting long-context performance. We validate the effectiveness of our method on two widely used benchmarks, RULER and LongBench~v2. While acquiring noticeable gains on RULER, it can also achieve a reasonable improvement on LongBench~v2 without any manually curated long-context QA data. Furthermore, we conduct extensive ablation studies to analyze the impact of reward design, data curation strategies, training schemes, and data scaling effects on model performance. We publicly release our code, data, and models.

</details>

---

### 33. [Learning beyond Teacher: Generalized On-Policy Distillation with Reward Extrapolation](https://arxiv.org/abs/2602.12125)

**基本信息**

- 🔗 arXiv: [`2602.12125`](https://arxiv.org/abs/2602.12125)
- 👥 作者: Wenkai Yang, Weijie Liu, Ruobing Xie 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.12125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大语言模型的蒸馏方法，特别是策略蒸馏。模型蒸馏是构建高效“化学大模型”（例如，将大型化学预训练模型的知识压缩到更小、更易部署的模型中）和专业化“质谱结构推理”模型的关键技术。本文提出的广义策略蒸馏框架为优化这一过程提供了新的理论视角和实用方法。

**📖 中文摘要**

本文首先从理论上证明了策略蒸馏（OPD）是密集KL约束强化学习的一个特例，其中奖励函数和KL正则化总是等权重，且参考模型可以是任何模型。然后，作者提出了广义策略蒸馏（G-OPD）框架，通过引入灵活的参考模型和控制奖励项相对于KL正则化相对权重的奖励缩放因子，扩展了标准OPD目标。通过在数学推理和代码生成任务上的综合实验，作者得出了两个新颖的见解：（1）将奖励缩放因子设置为大于1（即奖励外推），在广泛的师生规模配对中 consistently 优于标准OPD。（2）在强到弱的蒸馏设置中，通过选择教师RL之前的基模型作为参考模型来进行奖励校正，可以获得更准确的奖励信号并进一步提高蒸馏性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

On-policy distillation (OPD), which aligns the student with the teacher's logit distribution on student-generated trajectories, has demonstrated strong empirical gains in improving student performance and often outperforms off-policy distillation and reinforcement learning (RL) paradigms. In this work, we first theoretically show that OPD is a special case of dense KL-constrained RL where the reward function and the KL regularization are always weighted equally and the reference model can by any model. Then, we propose the Generalized On-Policy Distillation (G-OPD) framework, which extends the standard OPD objective by introducing a flexible reference model and a reward scaling factor that controls the relative weight of the reward term against the KL regularization. Through comprehensive experiments on math reasoning and code generation tasks, we derive two novel insights: (1) Setting the reward scaling factor to be greater than 1 (i.e., reward extrapolation), which we term ExOPD, consistently improves over standard OPD across a range of teacher-student size pairings. In particular, in the setting where we merge the knowledge from different domain experts, obtained by applying domain-specific RL to the same student model, back into the original student, ExOPD enables the student to even surpass the teacher's performance boundary and outperform the domain teachers. (2) Building on ExOPD, we further find that in the strong-to-weak distillation setting (i.e., distilling a smaller student from a larger teacher), performing reward correction by choosing the reference model as the teacher's base model before RL yields a more accurate reward signal and further improves distillation performance. However, this choice assumes access to the teacher's pre-RL variant and incurs more computational overhead. We hope our work offers new insights for future research on OPD.

</details>

---

### 34. [Symmetry in language statistics shapes the geometry of model representations](https://arxiv.org/abs/2602.15029)

**基本信息**

- 🔗 arXiv: [`2602.15029`](https://arxiv.org/abs/2602.15029)
- 👥 作者: Dhruva Karkada, Daniel J. Korchinski, Andres Nava 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.15029.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和解释大语言模型内部表示的几何结构及其与数据统计对称性的关系。虽然研究对象是通用语言模型，但其揭示的表示学习原理（对称性诱导几何结构）对于理解和设计“化学大模型”的分子表示（例如，周期表元素的几何排列、官能团的对称性）以及“质谱结构推理”中质谱特征与分子子结构之间的映射关系具有重要的启发意义。这属于机器学习基础理论与化学信息学应用的交叉。

**📖 中文摘要**

本文旨在解释语言模型内部表示中观察到的几何结构（如月份组织成圆形，年份形成一维流形）。作者首先展示了语言统计中存在平移对称性（例如，任意两个月在文本中共现的频率仅取决于它们之间的时间间隔）。他们证明了这种对称性支配着高维词嵌入模型中的几何结构，并解析地推导了词表示的流形几何。这些预测与大型文本嵌入模型和大型语言模型的实证结果相匹配。此外，即使相关统计受到扰动，在中等嵌入维度下，表示几何仍然保持稳健。作者证明，当共现统计由潜在变量控制时，这种稳健性会自然出现。这些结果表明，表示流形具有普遍的起源：自然数据统计中的对称性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The internal representations learned by language models consistently exhibit striking geometric structure: calendar months organize into a circle, historical years form a smooth one-dimensional manifold, and cities' latitudes and longitudes can be decoded using a linear probe. To explain this neural code, we first show that language statistics exhibit translation symmetry (for example, the frequency with which any two months co-occur in text depends only on the time interval between them). We prove that this symmetry governs these geometric structures in high-dimensional word embedding models, and we analytically derive the manifold geometry of word representations. These predictions empirically match large text embedding models and large language models. Moreover, the representational geometry persists at moderate embedding dimension even when the relevant statistics are perturbed (e.g., by removing all sentences in which two months co-occur). We prove that this robustness emerges naturally when the co-occurrence statistics are controlled by an underlying latent variable. These results suggest that representational manifolds have a universal origin: symmetry in the statistics of natural data.

</details>

---

### 35. [Understanding protein function with a multimodal retrieval-augmented foundation model](https://arxiv.org/abs/2508.04724)

**基本信息**

- 🔗 arXiv: [`2508.04724`](https://arxiv.org/abs/2508.04724)
- 👥 作者: Timothy Fei Truong Jr, Tristan Bepler
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.04724.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质序列理解和设计的化学大模型（PoET-2），这是一个典型的化学信息学领域的大模型应用。

**📖 中文摘要**

这篇论文介绍了PoET-2，一个多模态、检索增强的蛋白质基础模型。它通过结合家族特异性进化约束的上下文学习和可选的结构条件，来学习蛋白质序列的生成分布。该模型采用分层Transformer编码器和具有因果与掩码语言建模目标的双解码器架构，使其能够在完全生成和双向表示学习两种模式下工作。PoET-2在零样本变体效应预测上达到了最先进的性能，特别是在处理多重突变和具有挑战性的插入缺失突变方面。在监督设置下，PoET-2的嵌入在学习和预测序列-功能关系方面优于先前的方法，尤其是在小数据集上。这项工作强调了将检索增强与多模态、以家族为中心的建模相结合，对于推进蛋白质基础模型的益处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (PLMs) learn probability distributions over natural protein sequences. By learning from hundreds of millions of natural protein sequences, protein understanding and design capabilities emerge. Recent works have shown that scaling these models improves structure prediction, but does not seem to improve mutation understanding and representation quality for protein function prediction. We introduce PoET-2, a multimodal, retrieval-augmented protein foundation model that incorporates in-context learning of family-specific evolutionary constraints with optional structure conditioning to learn generative distributions over protein sequences. PoET-2 uses a hierarchical transformer encoder that is equivariant to sequence context ordering and a dual decoder architecture with both causal and masked language modeling objectives, allowing PoET-2 to operate in both fully generative and bidirectional representation learning modes. PoET-2 achieves state-of-the-art performance on zero-shot variant effect prediction, excelling at scoring variants with multiple mutations and challenging indel mutations. In supervised settings, PoET-2 embeddings outperform previous methods for learning sequence-function relationships, especially with small datasets. This work highlights the benefits of combining retrieval augmentation with multimodal, family-centric modeling for advancing protein foundation models.

</details>

---

### 36. [TokEye: Fast Signal Extraction for Fluctuating Time Series via Offline Self-Supervised Learning From Fusion Diagnostics to Bioacoustics](https://arxiv.org/abs/2602.20317)

**基本信息**

- 🔗 arXiv: [`2602.20317`](https://arxiv.org/abs/2602.20317)
- 👥 作者: Nathaniel Chen, Kouroche Bouchiat, Peter Steiner 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20317.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个从多诊断信号（包括质谱相关的诊断，如束发射光谱）中自动提取模式的框架。这直接涉及质谱分析领域（作为聚变等离子体诊断的一部分）和用于信号处理的机器学习模型，与“质谱结构推理”主题相关。

**📖 中文摘要**

本文提出了一个“信号优先”的自监督框架，用于从各种传感器的高噪声时频数据中自动提取相干和瞬态模式。该方法开发了一种通用工具，通过在多通道信号处理中采用非线性最优技术，并利用快速神经网络代理，从DIII-D托卡马克的快磁、电子回旋辐射、CO2干涉仪和束发射光谱测量中提取相干、准相干和瞬态模式。该框架在DIII-D、TJ-II和非聚变谱图数据上进行了测试。推理延迟为0.5秒，使得该框架能够实现实时模式识别和大规模自动化数据库生成，用于先进的等离子体控制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Next-generation fusion facilities like ITER face a "data deluge," generating petabytes of multi-diagnostic signals daily that challenge manual analysis. We present a "signals-first" self-supervised framework for the automated extraction of coherent and transient modes from high-noise time-frequency data across a variety of sensors. We also develop a general-purpose method and tool for extracting coherent, quasi-coherent, and transient modes for fluctuation measurements in tokamaks by employing non-linear optimal techniques in multichannel signal processing with a fast neural network surrogate on fast magnetics, electron cyclotron emission, CO2 interferometers, and beam emission spectroscopy measurements from DIII-D. Results are tested on data from DIII-D, TJ-II, and non-fusion spectrograms. With an inference latency of 0.5 seconds, this framework enables real-time mode identification and large-scale automated database generation for advanced plasma control. Repository is in this https URL .

</details>

---

### 37. [Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions](https://arxiv.org/abs/2602.21160)

**基本信息**

- 🔗 arXiv: [`2602.21160`](https://arxiv.org/abs/2602.21160)
- 👥 作者: Mame Diarra Toure, David A. Stephens
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21160.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进贝叶斯深度学习模型的不确定性量化方法。虽然应用领域是医学图像，但其提出的分解认知不确定性的方法具有普适性，可以应用于化学信息学或质谱分析中的分类或回归问题，以更好地理解和利用大模型（如用于光谱解释的模型）的预测不确定性。

**📖 中文摘要**

在安全关键分类中，失败的代价通常是不对称的，然而贝叶斯深度学习用单一标量互信息（MI）来总结认知不确定性，无法区分模型的未知性涉及的是良性类别还是安全关键类别。本文提出将MI分解为每个类别的向量C_k(x)。该分解源于熵的二阶泰勒展开；1/μ_k权重校正了边界抑制，并使C_k在稀有和常见类别之间具有可比性。通过构造，∑_k C_k ≈ MI，并且伴随的偏度诊断标记了近似退化的输入。在描述了C_k的公理性质后，我们在三个任务上验证了它：（i）糖尿病视网膜病变的选择性预测，其中关键类别的C_k将选择性风险比MI降低了34.7%，比方差基线降低了56.2%；（ii）临床和图像基准上的分布外检测，其中∑_k C_k达到了最高的AUROC，并且每个类别的视图暴露了MI不可见的不对称偏移；（iii）受控的标签噪声研究，其中在端到端贝叶斯训练下，∑_k C_k对注入的偶然噪声的敏感性低于MI，而两种度量在迁移学习下都会退化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In safety-critical classification, the cost of failure is often asymmetric, yet Bayesian deep learning summarises epistemic uncertainty with a single scalar, mutual information (MI), that cannot distinguish whether a model's ignorance involves a benign or safety-critical class. We decompose MI into a per-class vector $C_k(x)=\sigma_k^{2}/(2\mu_k)$, with $\mu_k{=}\mathbb{E}[p_k]$ and $\sigma_k^2{=}\mathrm{Var}[p_k]$ across posterior samples. The decomposition follows from a second-order Taylor expansion of the entropy; the $1/\mu_k$ weighting corrects boundary suppression and makes $C_k$ comparable across rare and common classes. By construction $\sum_k C_k \approx \mathrm{MI}$, and a companion skewness diagnostic flags inputs where the approximation degrades. After characterising the axiomatic properties of $C_k$, we validate it on three tasks: (i) selective prediction for diabetic retinopathy, where critical-class $C_k$ reduces selective risk by 34.7\% over MI and 56.2\% over variance baselines; (ii) out-of-distribution detection on clinical and image benchmarks, where $\sum_k C_k$ achieves the highest AUROC and the per-class view exposes asymmetric shifts invisible to MI; and (iii) a controlled label-noise study in which $\sum_k C_k$ shows less sensitivity to injected aleatoric noise than MI under end-to-end Bayesian training, while both metrics degrade under transfer learning. Across all tasks, the quality of the posterior approximation shapes uncertainty at least as strongly as the choice of metric, suggesting that how uncertainty is propagated through the network matters as much as how it is measured.

</details>

---

## 📊 数据统计
- 累计运行天数：1
- 累计论文数量：37

## 📝 历史记录

> 暂无历史数据

