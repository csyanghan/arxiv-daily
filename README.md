# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-14 01:17:20

## 📅 2026-03-14 (今日最新)

**相关论文数：53**

### 1. [Graph Tokenization for Bridging Graphs and Transformers](https://arxiv.org/abs/2603.11099)

**基本信息**

- 🔗 arXiv: [`2603.11099`](https://arxiv.org/abs/2603.11099)
- 👥 作者: Zeyuan Guo, Enmao Diao, Cheng Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11099.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（图标记化以连接图和Transformer）直接围绕“化学大模型”主题。化学大模型（如分子性质预测、反应预测模型）需要处理图结构数据，该论文提出的方法为将图数据适配到大模型生态系统中提供了通用且有效的解决方案。

**📖 中文摘要**

这篇论文提出了一种图标记化框架，旨在弥合图结构数据与Transformer序列模型之间的鸿沟。该框架通过结合可逆图序列化和字节对编码（BPE），将图转换为序列表示，使得像BERT这样的Transformer模型无需架构修改即可直接应用于图基准任务。论文在14个基准数据集上取得了最先进的结果，性能经常超越图神经网络和专门的图Transformer。这项工作与“化学大模型”主题高度相关，因为它提供了一种将复杂的、非欧几里得的分子图结构（化学信息学中的核心数据类型）转化为适合大型预训练Transformer模型处理的序列形式的方法。这为构建能够理解分子结构、性质和反应的化学领域大语言模型或图-语言混合模型奠定了关键的技术基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of large pretrained Transformers is closely tied to tokenizers, which convert raw input into discrete symbols. Extending these models to graph-structured data remains a significant challenge. In this work, we introduce a graph tokenization framework that generates sequential representations of graphs by combining reversible graph serialization, which preserves graph information, with Byte Pair Encoding (BPE), a widely adopted tokenizer in large language models (LLMs). To better capture structural information, the graph serialization process is guided by global statistics of graph substructures, ensuring that frequently occurring substructures appear more often in the sequence and can be merged by BPE into meaningful tokens. Empirical results demonstrate that the proposed tokenizer enables Transformers such as BERT to be directly applied to graph benchmarks without architectural modifications. The proposed approach achieves state-of-the-art results on 14 benchmark datasets and frequently outperforms both graph neural networks and specialized graph transformers. This work bridges the gap between graph-structured data and the ecosystem of sequence models. Our code is available at \href{ this https URL }{\color{blue}here}.

</details>

---

### 2. [Differentiable Thermodynamic Phase-Equilibria for Machine Learning](https://arxiv.org/abs/2603.11249)

**基本信息**

- 🔗 arXiv: [`2603.11249`](https://arxiv.org/abs/2603.11249)
- 👥 作者: Karim K. Ben Hicham, Moreno Ascani, Jan G. Rittig 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11249.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（将机器学习与热力学原理结合，构建可微分的相平衡模型）直接围绕“化学大模型”主题。它代表了在化学工程和物理化学领域开发具有物理可解释性的人工智能模型的前沿方向。

**📖 中文摘要**

本文提出了DISCOMAX，一种用于相平衡计算的可微分算法，该算法在训练和推理时都保证了热力学一致性。该方法植根于统计热力学，通过离散枚举和后续的掩码softmax聚合可行状态，并结合直通梯度估计器，实现了对神经超额吉布斯自由能模型的端到端物理一致性学习。论文在二元液-液平衡数据上评估了该方法，证明其性能优于现有的基于代理模型的方法。这项工作与“化学大模型”主题相关，因为它展示了如何将机器学习（特别是神经网络）与严格的热力学原理相结合，构建可解释、可微分且物理一致的模型。这类模型是下一代化学人工智能的核心，可用于预测复杂的相行为、溶解度、分配系数等，是化学信息学和过程工程中“大模型”的重要应用方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of phase equilibria remains a central challenge in chemical engineering. Physics-consistent machine learning methods that incorporate thermodynamic structure into neural networks have recently shown strong performance for activity-coefficient modeling. However, extending such approaches to equilibrium data arising from an extremum principle, such as liquid-liquid equilibria, remains difficult. Here we present DISCOMAX, a differentiable algorithm for phase-equilibrium calculation that guarantees thermodynamic consistency at both training and inference, only subject to a user-specified discretization. The method is rooted in statistical thermodynamics, and works via a discrete enumeration with subsequent masked softmax aggregation of feasible states, and together with a straight-through gradient estimator to enable physics-consistent end-to-end learning of neural $g^{E}$-models. We evaluate the approach on binary liquid-liquid equilibrium data and demonstrate that it outperforms existing surrogate-based methods, while offering a general framework for learning from different kinds of equilibrium data.

</details>

---

### 3. [A Machine Learning-Enhanced Hopf-Cole Formulation for Nonlinear Gas Flow in Porous Media](https://arxiv.org/abs/2603.11250)

**基本信息**

- 🔗 arXiv: [`2603.11250`](https://arxiv.org/abs/2603.11250)
- 👥 作者: V. S. Maduru, K. B. Nakshatrala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11250.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（将物理建模与深度学习结合，用于多孔介质中复杂气体输运的建模和反演）直接围绕“化学大模型”主题。它体现了在化学工程和地球科学领域开发高保真、可解释的AI代理模型的趋势。

**📖 中文摘要**

本文提出了一个用于多孔介质中气体输运的集成建模框架。该框架结合了Klinkenberg增强的本构关系、Hopf-Cole变换后的混合形式线性控制方程、共享主干神经网络架构和深度最小二乘求解器。Hopf-Cole变换将原始非线性流动方程重新表述为与达西模型密切相关的等效线性系统。该框架还自然地促进了从有限或间接观测中反演压力依赖性渗透率和滑移参数，实现了对难以通过实验测量的流动特性的高效估计。数值结果证明了该框架在宽压力范围内准确恢复流动动力学和参数的能力。这项工作与“化学大模型”主题相关，因为它展示了在复杂物理化学过程（多孔介质中的气体传输，涉及非线性、滑移效应）中应用先进的机器学习方法（深度学习与物理建模结合）的范例。这类“物理信息机器学习”模型是构建用于模拟、优化和发现化学与材料过程的“大模型”的关键组成部分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate modeling of gas flow through porous media is critical for many technological applications, including reservoir performance prediction, carbon capture and sequestration, and fuel cells and batteries. However, such modeling remains challenging due to strong nonlinear behavior and uncertainty in model parameters. In particular, gas slippage effects described by the Klinkenberg model introduce pressure-dependent permeability, which complicates numerical simulation and obscures deviations from classical Darcy flow behavior. To address these challenges, we present an integrated modeling framework for gas transport in porous media that combines a Klinkenberg-enhanced constitutive relation, Hopf-Cole-transformed mixed-form linear governing equations, a shared-trunk neural network architecture, and a Deep Least-Squares (DeepLS) solver. The Hopf-Cole transformation reformulates the original nonlinear flow equations into an equivalent linear system closely related to the Darcy model, while the mixed formulation, together with a shared-trunk neural architecture, enables simultaneous and accurate prediction of both pressure and velocity fields. A rigorous convergence analysis is performed both theoretically and numerically, establishing the stability and convergence properties of the proposed solver. Importantly, the proposed framework also naturally facilitates inverse modeling of pressure-dependent permeability and slippage parameters from limited or indirect observations, enabling efficient estimation of flow properties that are difficult to measure experimentally. Numerical results demonstrate accurate recovery of flow dynamics and parameters across a wide range of pressure regimes, highlighting the framework's robustness, accuracy, and computational efficiency for gas transport modeling and inversion in tight formations.

</details>

---

### 4. [Heavy-Tailed Principle Component Analysis](https://arxiv.org/abs/2603.11308)

**基本信息**

- 🔗 arXiv: [`2603.11308`](https://arxiv.org/abs/2603.11308)
- 👥 作者: Mario Sayde, Christopher Khater, Jihad Fahs 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11308.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种针对重尾数据的稳健主成分分析方法。虽然标题和摘要未直接提及“化学大模型”或“质谱结构推理”，但其研究的核心——高维数据降维、特征提取及对噪声和异常值的鲁棒性——是化学信息学和质谱数据分析（尤其是处理复杂、噪声质谱数据以进行化合物鉴定和结构推理）中的基础且关键的技术。因此，该论文与化学信息学领域的核心方法论高度相关。

**📖 中文摘要**

本文研究了重尾数据下的主成分分析（PCA）问题。经典PCA依赖于二阶矩，在存在重尾数据和脉冲噪声时非常脆弱。论文提出了一个统一的框架来处理无限方差模型，该框架基于超统计依赖模型，其中观测数据由正随机标量和高斯向量的乘积生成，这涵盖了多元t分布和亚高斯α稳定律等广泛的重尾分布。论文在即使矩不存在时也定义良好的对数损失下重新表述PCA，并证明了在该损失下，重尾观测的主成分与应用于底层高斯生成器协方差矩阵的标准PCA所得主成分一致。基于这一见解，论文提出了直接从重尾数据中稳健估计该协方差矩阵的方法，并与经验协方差和Tyler散度估计器进行了比较。实验表明，该方法在存在重尾和脉冲噪声时能可靠地恢复主方向，并显著优于经典PCA，同时在高斯噪声下保持竞争力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Principal Component Analysis (PCA) is a cornerstone of dimensionality reduction, yet its classical formulation relies critically on second-order moments and is therefore fragile in the presence of heavy-tailed data and impulsive noise. While numerous robust PCA variants have been proposed, most either assume finite variance, rely on sparsity-driven decompositions, or address robustness through surrogate loss functions without a unified treatment of infinite-variance models. In this paper, we study PCA for high-dimensional data generated according to a superstatistical dependent model of the form $\mathbf{X} = A^{1/2}\mathbf{G}$, where $A$ is a positive random scalar and $\mathbf{G}$ is a Gaussian vector. This framework captures a wide class of heavy-tailed distributions, including multivariate $t$ and sub-Gaussian $\alpha$-stable laws. We formulate PCA under a logarithmic loss, which remains well defined even when moments do not exist. Our main theoretical result shows that, under this loss, the principal components of the heavy-tailed observations coincide with those obtained by applying standard PCA to the covariance matrix of the underlying Gaussian generator. Building on this insight, we propose robust estimators for this covariance matrix directly from heavy-tailed data and compare them with the empirical covariance and Tyler's scatter estimator. Extensive experiments, including background denoising tasks, demonstrate that the proposed approach reliably recovers principal directions and significantly outperforms classical PCA in the presence of heavy-tailed and impulsive noise, while remaining competitive under Gaussian noise.

</details>

---

### 5. [Harnessing Data Asymmetry: Manifold Learning in the Finsler World](https://arxiv.org/abs/2603.11396)

**基本信息**

- 🔗 arXiv: [`2603.11396`](https://arxiv.org/abs/2603.11396)
- 👥 作者: Thomas Dagès, Simon Weber, Daniel Cremers 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11396.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是流形学习，这是一种用于高维数据降维和可视化的关键技术。在化学信息学和质谱分析中，流形学习常用于处理分子描述符空间、质谱特征空间或代谢组学数据，以发现潜在结构、进行化合物分类或可视化。论文重点研究的非对称相异性建模和芬斯勒几何，为处理化学数据中常见的复杂、非对称关系（例如，分子相似性度量、质谱峰强度与结构的关系可能不是对称的）提供了新的理论框架和工具，因此与化学信息学的核心方法论直接相关。

**📖 中文摘要**

流形学习是高维数据分析和可视化的核心任务，旨在通过保持低维嵌入中的成对相异性来捕捉复杂数据的底层简单结构。传统方法依赖于对称的黎曼几何，从而强制对称的相异性和嵌入空间（如欧几里得空间）。然而，这实际上丢弃了数据样本非均匀性所固有的有价值的非对称信息。本文提出通过转向芬斯勒几何（黎曼几何的非对称推广）来利用这种非对称性，并提出了一个芬斯勒流形学习流程，该流程构建非对称相异性并在芬斯勒空间中嵌入。这极大地扩展了现有非对称嵌入器的适用性，超越了传统的定向数据，适用于任何数据。论文还通过将当前参考方法（如芬斯勒t-SNE和芬斯勒Umap）推广到非对称情况来实现现代化。在受控合成和大型真实数据集上的实验表明，我们的非对称流程揭示了传统流程中丢失的宝贵信息（例如密度层次结构），并且始终提供比其欧几里得对应物更高质量的嵌入。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Manifold learning is a fundamental task at the core of data analysis and visualisation. It aims to capture the simple underlying structure of complex high-dimensional data by preserving pairwise dissimilarities in low-dimensional embeddings. Traditional methods rely on symmetric Riemannian geometry, thus forcing symmetric dissimilarities and embedding spaces, e.g. Euclidean. However, this discards in practice valuable asymmetric information inherent to the non-uniformity of data samples. We suggest to harness this asymmetry by switching to Finsler geometry, an asymmetric generalisation of Riemannian geometry, and propose a Finsler manifold learning pipeline that constructs asymmetric dissimilarities and embeds in a Finsler space. This greatly broadens the applicability of existing asymmetric embedders beyond traditionally directed data to any data. We also modernise asymmetric embedders by generalising current reference methods to asymmetry, like Finsler t-SNE and Finsler Umap. On controlled synthetic and large real datasets, we show that our asymmetric pipeline reveals valuable information lost in the traditional pipeline, e.g. density hierarchies, and consistently provides superior quality embeddings than their Euclidean counterparts.

</details>

---

### 6. [Reproducible Synthetic Clinical Letters for Seizure Frequency Information Extraction](https://arxiv.org/abs/2603.11407)

**基本信息**

- 🔗 arXiv: [`2603.11407`](https://arxiv.org/abs/2603.11407)
- 👥 作者: Yujian Gan, Stephen H. Barlow, Ben Holgate 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11407.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于生成合成临床文本数据（癫痫信件）的框架，并利用这些数据训练语言模型进行信息提取。虽然应用领域是医学，但其核心贡献——生成“任务忠实”的合成文本数据集以训练模型执行特定的信息提取任务——是一种重要的数据资源创建方法。这种方法论可以迁移到化学信息学领域，例如，生成合成的质谱报告、实验记录或化合物描述文本，用于训练模型进行质谱结构推理或化学实体关系提取。因此，该论文提供了可用于相关主题的数据集/资源创建工具和方法。

**📖 中文摘要**

癫痫发作频率信息对于癫痫研究和临床护理非常重要，但通常记录在多变且难以注释和共享的自由文本临床信件中。我们开发了一个可重复、保护隐私的框架，使用完全合成但忠实于任务的癫痫信件来提取发作频率。我们定义了一个结构化的标签方案，涵盖癫痫负担的常见描述，包括明确频率、范围、丛集、无发作间隔、未知频率和明确无发作陈述。一个教师语言模型生成具有标准化标签、基本原理和证据范围的NHS风格合成信件。我们在这些合成信件上微调了几个开放权重的语言模型（4B-14B参数），以从完整文档中提取发作频率，比较直接数值预测与结构化标签预测，并测试基于证据的输出。在临床医生检查的真实临床信件保留集上，仅使用合成数据训练的模型泛化良好，并且结构化标签始终优于直接数值回归。使用15,000封合成训练信件，模型在细粒度类别上达到高达0.788的微平均F1分数，在实用类别上达到0.847；一个医学导向的4B模型分别达到0.787和0.858。基于证据的输出也支持快速的临床验证和错误分析。这些结果表明，合成的、结构化的、基于证据的监督可以实现稳健的癫痫发作频率提取，而无需共享敏感的患者文本，并且可能推广到其他时间复杂的临床信息提取任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Seizure-frequency information is important for epilepsy research and clinical care, but it is usually recorded in variable free-text clinic letters that are hard to annotate and share. We developed a reproducible, privacy-preserving framework for extracting seizure frequency using fully synthetic yet task-faithful epilepsy letters. We defined a structured label scheme covering common descriptions of seizure burden, including explicit rates, ranges, clusters, seizure-free intervals, unknown frequency, and explicit no-seizure statements. A teacher language model generated NHS-style synthetic letters paired with normalized labels, rationales, and evidence spans. We fine-tuned several open-weight language models (4B-14B parameters) on these synthetic letters to extract seizure frequency from full documents, comparing direct numeric prediction with structured label prediction and testing evidence-grounded outputs. On a clinician-checked held-out set of real clinic letters, models trained only on synthetic data generalized well, and structured labels consistently outperformed direct numeric regression. With 15,000 synthetic training letters, models achieved micro-F1 scores up to 0.788 for fine-grained categories and 0.847 for pragmatic categories; a medically oriented 4B model achieved 0.787 and 0.858, respectively. Evidence-grounded outputs also supported rapid clinical verification and error analysis. These results show that synthetic, structured, evidence-grounded supervision can enable robust seizure-frequency extraction without sharing sensitive patient text and may generalize to other temporally complex clinical information extraction tasks.

</details>

---

### 7. [MaterialFigBENCH: benchmark dataset with figures for evaluating college-level materials science problem-solving abilities of multimodal large language models](https://arxiv.org/abs/2603.11414)

**基本信息**

- 🔗 arXiv: [`2603.11414`](https://arxiv.org/abs/2603.11414)
- 👥 作者: Michiko Yoshitake, Yuta Suzuki, Ryo Igarashi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11414.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于评估多模态大语言模型在材料科学领域图表理解能力的基准数据集“MaterialFigBench”。该数据集包含大量带有图表的问题和专家定义的答案。虽然主题是材料科学，但其核心——构建一个包含复杂科学图表（如相图、曲线图）和对应问题的高质量、领域特定的多模态评估基准——的方法论和资源，可以直接应用于化学信息学领域。例如，可以类似地构建用于评估模型理解质谱图、色谱图、分子结构图或化学相图能力的基准。因此，该论文提供了可用于相关主题（评估化学大模型的多模态能力）的数据集构建范例和潜在资源。

**📖 中文摘要**

我们提出了MaterialFigBench，一个旨在评估多模态大语言模型解决需要准确解读图表的大学生材料科学问题能力的基准数据集。与主要依赖文本表示的现有基准不同，MaterialFigBench专注于那些图表（如相图、应力-应变曲线、阿伦尼乌斯图、衍射图和微观结构示意图）对于得出正确答案不可或缺的问题。该数据集包含137个改编自标准材料科学教科书的自由回答问题，涵盖广泛的主题，包括晶体结构、机械性能、扩散、相图、相变和材料的电子性能。为了解决从图像中读取数值时不可避免的模糊性，在适当情况下提供了专家定义的答案范围。我们评估了几种最先进的多模态LLM，包括通过OpenAI API访问的ChatGPT和GPT模型，并分析了它们在不同问题类别和模型版本上的表现。结果表明，尽管整体准确性随着模型更新而提高，但当前的LLM仍然难以真正视觉理解和定量解读材料科学图表。在许多情况下，正确答案是通过依赖记忆的领域知识获得的，而不是通过阅读提供的图像。MaterialFigBench突出了在视觉推理、数值精度和有效数字处理方面的持续弱点，同时也确定了性能有所改进的问题类型。该基准为推进材料科学中的多模态推理能力以及指导未来具有更强基于图表理解能力的LLM开发提供了系统化和特定领域的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MaterialFigBench, a benchmark dataset designed to evaluate the ability of multimodal large language models (LLMs) to solve university-level materials science problems that require accurate interpretation of figures. Unlike existing benchmarks that primarily rely on textual representations, MaterialFigBench focuses on problems in which figures such as phase diagrams, stress-strain curves, Arrhenius plots, diffraction patterns, and microstructural schematics are indispensable for deriving correct answers. The dataset consists of 137 free-response problems adapted from standard materials science textbooks, covering a broad range of topics including crystal structures, mechanical properties, diffusion, phase diagrams, phase transformations, and electronic properties of materials. To address unavoidable ambiguity in reading numerical values from images, expert-defined answer ranges are provided where appropriate. We evaluate several state-of-the-art multimodal LLMs, including ChatGPT and GPT models accessed via OpenAI APIs, and analyze their performance across problem categories and model versions. The results reveal that, although overall accuracy improves with model updates, current LLMs still struggle with genuine visual understanding and quantitative interpretation of materials science figures. In many cases, correct answers are obtained by relying on memorized domain knowledge rather than by reading the provided images. MaterialFigBench highlights persistent weaknesses in visual reasoning, numerical precision, and significant-digit handling, while also identifying problem types where performance has improved. This benchmark provides a systematic and domain-specific foundation for advancing multimodal reasoning capabilities in materials science and for guiding the development of future LLMs with stronger figure-based understanding.

</details>

---

### 8. [ZTab: Domain-based Zero-shot Annotation for Table Columns](https://arxiv.org/abs/2603.11436)

**基本信息**

- 🔗 arXiv: [`2603.11436`](https://arxiv.org/abs/2603.11436)
- 👥 作者: Ehsan Hoseinzade, Ke Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11436.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为ZTab的框架，用于在给定领域配置（预定义语义类型和样本模式）的情况下，自动生成伪表数据并微调模型，以实现对关系表格列的零样本语义类型标注。这种方法的核心是创建合成数据（伪表）来训练模型。这种“基于领域配置生成训练数据”的范式，可以应用于化学信息学领域，例如，根据已知的化合物属性表模式生成合成表格数据，用于训练模型自动标注化学数据库中的列类型（如分子量、LogP、活性值等），或用于质谱数据表中峰的注释。因此，该论文提供了一种可用于相关主题的数据资源生成工具和方法论。

**📖 中文摘要**

本研究解决了在关系表中自动检测语义列类型的挑战，这是许多实际应用中的关键任务。零样本建模消除了对用户提供的标记训练数据的需求，使其成为数据收集成本高昂或由于隐私问题而受到限制的场景的理想选择。然而，当语义列类型的数量很大时，现有的零样本模型性能较差，对表格结构的理解有限，并且由于依赖高性能的闭源LLM而存在隐私风险。我们引入了ZTab，一个基于领域的零样本框架，旨在同时满足性能和零样本要求。给定一个由一组预定义语义类型和样本表模式组成的领域配置，ZTab为样本模式生成伪表，并在其上微调一个注释LLM。ZTab是基于领域的零样本，因为它不依赖于用户特定的标记训练数据；因此，对于来自类似领域的测试表，不需要重新训练。我们描述了基于领域的零样本的三种情况。ZTab的领域配置在零样本程度和注释性能之间提供了权衡：包含所有语义类型的“通用领域”接近“纯粹”零样本，而包含特定应用语义类型的“专业领域”则能在该领域内实现更好的零样本性能。源代码和数据集可在此https URL获取。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study addresses the challenge of automatically detecting semantic column types in relational tables, a key task in many real-world applications. Zero-shot modeling eliminates the need for user-provided labeled training data, making it ideal for scenarios where data collection is costly or restricted due to privacy concerns. However, existing zero-shot models suffer from poor performance when the number of semantic column types is large, limited understanding of tabular structure, and privacy risks arising from dependence on high-performance closed-source LLMs. We introduce ZTab, a domain-based zero-shot framework that addresses both performance and zero-shot requirements. Given a domain configuration consisting of a set of predefined semantic types and sample table schemas, ZTab generates pseudo-tables for the sample schemas and fine-tunes an annotation LLM on them. ZTab is domain-based zero-shot in that it does not depend on user-specific labeled training data; therefore, no retraining is needed for a test table from a similar domain. We describe three cases of domain-based zero-shot. The domain configuration of ZTab provides a trade-off between the extent of zero-shot and annotation performance: a "universal domain" that contains all semantic types approaches "pure" zero-shot, while a "specialized domain" that contains semantic types for a specific application enables better zero-shot performance within that domain. Source code and datasets are available at this https URL

</details>

---

### 9. [LLM-Assisted Causal Structure Disambiguation and Factor Extraction for Legal Judgment Prediction](https://arxiv.org/abs/2603.11446)

**基本信息**

- 🔗 arXiv: [`2603.11446`](https://arxiv.org/abs/2603.11446)
- 👥 作者: Yuzhi Liang, Lixiang Ma, Xinrong Zhu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11446.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将大语言模型与因果推理相结合，以解决领域特定（法律）的预测和推理任务。其关键技术包括利用LLM进行信息提取（法律要素）、提供先验知识以消歧因果结构，并构建因果感知的预测模型。这种方法论与“化学大模型”的研究高度相关。在化学信息学中，可以类似地利用LLM从科学文献中提取化学实体、反应条件和性质，结合因果推理来预测化合物性质、反应结果或进行逆合成分析。论文中提出的“LLM辅助因果结构消歧”和“因果感知建模”框架，为构建更可靠、可解释的化学领域大模型提供了直接的技术参考和思路。

**📖 中文摘要**

基于预训练语言模型的主流法律判决预测方法严重依赖案件事实与判决结果之间的统计相关性。这种范式缺乏对法律构成要素和底层因果逻辑的显式建模，使得模型容易学习虚假相关性并遭受鲁棒性差的问题。虽然引入因果推理可以缓解这个问题，但现有的因果LJP方法在真实法律文本中面临两个关键瓶颈：带有严重噪声的法律要素提取不准确，以及由于稀疏特征下的马尔可夫等价性导致因果结构发现存在显著不确定性。为了应对这些挑战，我们提出了一个增强的因果推理框架，该框架将大语言模型先验与统计因果发现相结合。首先，我们设计了一个结合统计采样和LLM语义推理的从粗到细的混合提取机制，以准确识别和纯化标准的法律构成要素。其次，为了解决结构不确定性，我们引入了一个LLM辅助的因果结构消歧机制。通过利用LLM作为约束先验知识库，我们对模糊的因果方向进行概率评估和剪枝，以生成符合法律规定的候选因果图。最后，通过生成的因果图显式约束文本注意力强度，构建了一个因果感知的判决预测模型。在多个基准数据集（包括LEVEN、QA和CAIL）上的大量实验表明，我们提出的方法在预测准确性和鲁棒性方面都显著优于最先进的基线，特别是在区分混淆指控方面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mainstream methods for Legal Judgment Prediction (LJP) based on Pre-trained Language Models (PLMs) heavily rely on the statistical correlation between case facts and judgment results. This paradigm lacks explicit modeling of legal constituent elements and underlying causal logic, making models prone to learning spurious correlations and suffering from poor robustness. While introducing causal inference can mitigate this issue, existing causal LJP methods face two critical bottlenecks in real-world legal texts: inaccurate legal factor extraction with severe noise, and significant uncertainty in causal structure discovery due to Markov equivalence under sparse features. To address these challenges, we propose an enhanced causal inference framework that integrates Large Language Model (LLM) priors with statistical causal discovery. First, we design a coarse-to-fine hybrid extraction mechanism combining statistical sampling and LLM semantic reasoning to accurately identify and purify standard legal constituent elements. Second, to resolve structural uncertainty, we introduce an LLM-assisted causal structure disambiguation mechanism. By utilizing the LLM as a constrained prior knowledge base, we conduct probabilistic evaluation and pruning on ambiguous causal directions to generate legally compliant candidate causal graphs. Finally, a causal-aware judgment prediction model is constructed by explicitly constraining text attention intensity via the generated causal graphs. Extensive experiments on multiple benchmark datasets, including LEVEN , QA, and CAIL, demonstrate that our proposed method significantly outperforms state-of-the-art baselines in both predictive accuracy and robustness, particularly in distinguishing confusing charges.

</details>

---

### 10. [Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes](https://arxiv.org/abs/2603.11462)

**基本信息**

- 🔗 arXiv: [`2603.11462`](https://arxiv.org/abs/2603.11462)
- 👥 作者: Yuxiang Liu, Qiao Liu, Tong Luo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11462.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是标记时间点过程的建模，这是一种用于分析异步、不规则间隔事件序列的强大统计框架。在化学信息学和质谱分析中，许多过程可以建模为事件序列，例如：质谱数据中的离子检测事件（带有m/z标记）、化学反应过程中的关键步骤事件、或高通量实验中的观测序列。论文提出的NEXTPP框架，通过结合离散事件标记和连续时间动力学，并利用神经ODE和注意力机制进行建模，为分析和预测此类化学相关的事件序列数据提供了先进的方法论工具。因此，该论文与质谱结构推理（将质谱峰序列映射到结构）和化学过程建模的核心技术直接相关。

**📖 中文摘要**

预测带有离散标记的不规则间隔事件序列具有重大挑战，因为连续时间数据中嵌入了复杂的异步依赖关系。顺序方法捕获事件标记之间的依赖关系，但忽略了事件之间的连续演化，而神经常微分方程方法建模平滑动力学，但未能考虑事件类型如何影响未来动态。为了克服这些限制，我们提出了NEXTPP，一个通过事件粒度神经进化与交叉交互实现离散和连续表示统一的双通道框架，用于标记时间点过程。具体来说，NEXTPP通过自注意力机制编码离散事件标记，同时使用神经ODE演化潜在连续时间状态。然后，这些并行流通过交叉注意力模块融合，以实现连续和离散表示之间显式的双向交互。融合后的表示驱动神经霍克斯过程的条件强度函数，同时采用迭代细化采样器来生成未来事件。在五个真实世界数据集上的广泛评估表明，NEXTPP始终优于最先进的模型。源代码可在此https URL找到。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting irregularly spaced event sequences with discrete marks poses significant challenges due to the complex, asynchronous dependencies embedded within continuous-time data this http URL sequential approaches capture dependencies among event tokens but ignore the continuous evolution between events, while Neural Ordinary Differential Equation (Neural ODE) methods model smooth dynamics yet fail to account for how event types influence future this http URL overcome these limitations, we propose NEXTPP, a dual-channel framework that unifies discrete and continuous representations via Event-granular Neural Evolution with Cross-Interaction for Marked Temporal Point Processes. Specifically, NEXTPP encodes discrete event marks via a self-attention mechanism, simultaneously evolving a latent continuous-time state using a Neural ODE. These parallel streams are then fused through a crossattention module to enable explicit bidirectional interaction between continuous and discrete representations. The fused representations drive the conditional intensity function of the neural Hawkes process, while an iterative thinning sampler is employed to generate future events. Extensive evaluations on five real-world datasets demonstrate that NEXTPP consistently outperforms state-of-the-art models. The source code can be found at this https URL .

</details>

---

### 11. [Leveraging Phytolith Research using Artificial Intelligence](https://arxiv.org/abs/2603.11476)

**基本信息**

- 🔗 arXiv: [`2603.11476`](https://arxiv.org/abs/2603.11476)
- 👥 作者: Andrés G. Mejía Ramón, Kate Dudgeon, Nina Witteveen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于微观粒子（植物硅酸体）的多模态AI分析流程，涉及2D图像和3D点云的结构推理。虽然研究对象是植物硅酸体而非化学分子，但其核心方法论——利用多模态数据（2D图像和3D点云）进行微观粒子的结构分类和解释——与“质谱结构推理”主题在方法论上高度相关，都是通过AI模型从复杂数据中推断微观结构信息。

**📖 中文摘要**

本文提出Sorometry，一个用于植物硅酸体高通量数字化、推理和解释的端到端人工智能流程。该工作流程处理Z-stack光学显微镜扫描，自动生成同步的2D正射影像和3D点云。作者开发了一个多模态融合模型，结合了用于2D图像分析的ConvNeXt和用于3D点云分析的PointNet++。该模型在24种诊断形态类型上实现了77.9%的全局分类准确率。该平台将植物硅酸体研究转变为一个“组学”规模的学科，显著扩展了分析能力，标准化了专家判断，并实现了可重复的、群体水平的考古和古生态组合表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phytolith analysis is a crucial tool for reconstructing past vegetation and human activities, but traditional methods are severely limited by labour-intensive, time-consuming manual microscopy. To address this bottleneck, we present Sorometry: a comprehensive end-to-end artificial intelligence pipeline for the high-throughput digitisation, inference, and interpretation of phytoliths. Our workflow processes z-stacked optical microscope scans to automatically generate synchronised 2D orthoimages and 3D point clouds of individual microscopic particles. We developed a multimodal fusion model that combines ConvNeXt for 2D image analysis and PointNet++ for 3D point cloud analysis, supported by a graphical user interface for expert annotation and review. Tested on reference collections and archaeological samples from the Bolivian Amazon, our fusion model achieved a global classification accuracy of 77.9\% across 24 diagnostic morphotypes and 84.5% for segmentation quality. Crucially, the integration of 3D data proved essential for distinguishing complex morphotypes (such as grass silica short cell phytoliths) whose diagnostic features are often obscured by their orientation in 2D projections. Beyond individual object classification, Sorometry incorporates Bayesian finite mixture modelling to predict overall plant source contributions at the assemblage level, successfully identifying specific plants like maize and palms in complex mixed samples. This integrated platform transforms phytolith research into an "omics"-scale discipline, dramatically expanding analytical capacity, standardising expert judgements, and enabling reproducible, population-level characterisations of archaeological and paleoecological assemblages.

</details>

---

### 12. [Leveraging Large Language Models and Survival Analysis for Early Prediction of Chemotherapy Outcomes](https://arxiv.org/abs/2603.11594)

**基本信息**

- 🔗 arXiv: [`2603.11594`](https://arxiv.org/abs/2603.11594)
- 👥 作者: Muhammad Faisal Shahid, Asad Afzal, Abdullah Faiz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11594.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大型语言模型（LLMs）从临床文本中提取结构化信息（表型、结果）以构建预测模型的框架。这直接涉及“化学大模型”主题的一个关键应用领域：利用大模型处理和分析复杂的化学/生物医学文本数据，以支持下游的预测和决策任务。

**📖 中文摘要**

本研究利用大型语言模型（LLMs）和基于本体的技术，从患者病历中提取表型和治疗结果标签（如癌症进展和毒性），用于早期预测化疗结果。研究聚焦于乳腺癌，提取了生命体征、人口统计学、分期、生物标志物、性能评分等特征，以及化疗方案。通过生存模型（随机生存森林）预测治疗失败时间，并作为分类器预测治疗结果。该方法显著减少了表型稀疏性并提高了预测准确性。研究还将该方法扩展到其他四种癌症类型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemotherapy for cancer treatment is costly and accompanied by severe side effects, highlighting the critical need for early prediction of treatment outcomes to improve patient management and informed decision-making. Predictive models for chemotherapy outcomes using real-world data face challenges, including the absence of explicit phenotypes and treatment outcome labels such as cancer progression and toxicity. This study addresses these challenges by employing Large Language Models (LLMs) and ontology-based techniques for phenotypes and outcome label extraction from patient notes. We focused on one of the most frequently occurring cancers, breast cancer, due to its high prevalence and significant variability in patient response to treatment, making it a critical area for improving predictive modeling. The dataset included features such as vitals, demographics, staging, biomarkers, and performance scales. Drug regimens and their combinations were extracted from the chemotherapy plans in the EMR data and shortlisted based on NCCN guidelines, verified with NIH standards, and analyzed through survival modeling. The proposed approach significantly reduced phenotypes sparsity and improved predictive accuracy. Random Survival Forest was used to predict time-to-failure, achieving a C-index of 73%, and utilized as a classifier at a specific time point to predict treatment outcomes, with accuracy and F1 scores above 70%. The outcome probabilities were validated for reliability by calibration curves. We extended our approach to four other cancer types. This research highlights the potential of early prediction of treatment outcomes using LLM-based clinical data extraction enabling personalized treatment plans with better patient outcomes.

</details>

---

### 13. [Performance Evaluation of Open-Source Large Language Models for Assisting Pathology Report Writing in Japanese](https://arxiv.org/abs/2603.11597)

**基本信息**

- 🔗 arXiv: [`2603.11597`](https://arxiv.org/abs/2603.11597)
- 👥 作者: Masataka Kawai, Singo Sakashita, Shumpei Ishikawa 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大型语言模型（LLMs）在专业医学文本（病理报告）生成、信息提取和纠错方面的能力。这直接属于“化学大模型”主题在生物医学领域的应用研究，探讨了大模型处理特定领域（病理学）结构化文本的潜力。

**📖 中文摘要**

本文评估了七种开源大型语言模型在支持日语病理报告撰写方面的性能，从三个角度进行评估：（A）按照预定义格式生成和提取病理诊断文本；（B）纠正日语病理报告中的拼写错误；（C）由病理学家和临床医生对模型生成的解释性文本进行主观评估。思维模型和医学专用模型在需要推理的结构化报告任务和拼写纠正方面表现出优势。结果表明，开源LLMs在有限但临床相关的场景中可用于辅助日语病理报告撰写。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The performance of large language models (LLMs) for supporting pathology report writing in Japanese remains unexplored. We evaluated seven open-source LLMs from three perspectives: (A) generation and information extraction of pathology diagnosis text following predefined formats, (B) correction of typographical errors in Japanese pathology reports, and (C) subjective evaluation of model-generated explanatory text by pathologists and clinicians. Thinking models and medical-specialized models showed advantages in structured reporting tasks that required reasoning and in typo correction. In contrast, preferences for explanatory outputs varied substantially across raters. Although the utility of LLMs differed by task, our findings suggest that open-source LLMs can be useful for assisting Japanese pathology report writing in limited but clinically relevant scenarios.

</details>

---

### 14. [Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)

**基本信息**

- 🔗 arXiv: [`2603.11627`](https://arxiv.org/abs/2603.11627)
- 👥 作者: Yichi Zhang, Le Xue, Wenbo Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11627.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于3D医学影像（PET）通用分割的基础模型。虽然应用领域是医学影像，但其核心是构建和利用大规模、多模态（3D影像与标注）数据集来训练通用AI模型。这从方法论上与“化学大模型”主题中利用大规模数据构建领域专用基础模型的研究思路高度一致。PET影像本身也反映了体内的生化过程（示踪剂分布），与化学生物信息学有交叉。

**📖 中文摘要**

本文开发了用于3D全身正电子发射断层扫描（PET）通用分割的基础模型。作者构建了迄今为止最大、最全面的PET数据集，包含11041个3D全身PET扫描和59831个分割掩码。基于此，提出了SegAnyPET，一个具有通用性的基础模型，适用于多种分割任务。该模型基于3D架构和提示工程策略，支持通用且可扩展的器官和病变分割，支持高效的人工校正，并实现了临床人机交互工作流程。在多中心、多示踪剂、多疾病数据集上的评估表明，SegAnyPET在广泛的分割任务中实现了强大的零样本性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a key nuclear medicine imaging modality that visualizes radiotracer distributions to quantify in vivo physiological and metabolic processes, playing an irreplaceable role in disease management. Despite its clinical importance, the development of deep learning models for quantitative PET image analysis remains severely limited, driven by both the inherent segmentation challenge from PET's paucity of anatomical contrast and the high costs of data acquisition and annotation. To bridge this gap, we develop generalist foundational models for universal segmentation from 3D whole-body PET imaging. We first build the largest and most comprehensive PET dataset to date, comprising 11041 3D whole-body PET scans with 59831 segmentation masks for model development. Based on this dataset, we present SegAnyPET, an innovative foundational model with general-purpose applicability to diverse segmentation tasks. Built on a 3D architecture with a prompt engineering strategy for mask generation, SegAnyPET enables universal and scalable organ and lesion segmentation, supports efficient human correction with minimal effort, and enables a clinical human-in-the-loop workflow. Extensive evaluations on multi-center, multi-tracer, multi-disease datasets demonstrate that SegAnyPET achieves strong zero-shot performance across a wide range of segmentation tasks, highlighting its potential to advance the clinical applications of molecular imaging.

</details>

---

### 15. [PolyCrysDiff: Controllable Generation of Three-Dimensional Computable Polycrystalline Material Structures](https://arxiv.org/abs/2603.11695)

**基本信息**

- 🔗 arXiv: [`2603.11695`](https://arxiv.org/abs/2603.11695)
- 👥 作者: Chi Chen, Tianle Jiang, Xiaodong Wei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成式AI模型（扩散模型）来生成和设计多晶材料的三维微观结构。这直接属于‘化学大模型’在材料科学和化学信息学中的应用范畴，即利用先进的人工智能模型来理解和生成化学/材料结构。

**📖 中文摘要**

本文提出了PolyCrysDiff，一个基于条件潜在扩散的框架，用于端到端生成可计算的3D多晶材料微观结构。该工作直接面向材料科学中的结构生成问题，属于化学信息学中利用生成模型（如扩散模型）进行材料结构设计的核心范畴。论文展示了该框架能够忠实再现目标晶粒的形态、取向分布和3D空间相关性，并通过晶体塑性有限元方法（CPFEM）模拟验证了生成微观结构的可计算性和物理有效性。利用PolyCrysDiff的可控生成能力，作者系统阐明了晶粒级微观结构特征如何影响多晶材料的力学性能。这项工作为数据驱动的多晶材料优化和设计铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The three-dimensional (3D) microstructures of polycrystalline materials exert a critical influence on their mechanical and physical properties. Realistic, controllable construction of these microstructures is a key step toward elucidating structure-property relationships, yet remains a formidable challenge. Herein, we propose PolyCrysDiff, a framework based on conditional latent diffusion that enables the end-to-end generation of computable 3D polycrystalline microstructures. Comprehensive qualitative and quantitative evaluations demonstrate that PolyCrysDiff faithfully reproduces target grain morphologies, orientation distributions, and 3D spatial correlations, while achieving an $R^2$ over 0.972 on grain attributes (e.g., size and sphericity) control, thereby outperforming mainstream approaches such as Markov random field (MRF)- and convolutional neural network (CNN)-based methods. The computability and physical validity of the generated microstructures are verified through a series of crystal plasticity finite element method (CPFEM) simulations. Leveraging PolyCrysDiff's controllable generative capability, we systematically elucidate how grain-level microstructural characteristics affect the mechanical properties of polycrystalline materials. This development is expected to pave a key step toward accelerated, data-driven optimization and design of polycrystalline materials.

</details>

---

### 16. [EvoFlows: Evolutionary Edit-Based Flow-Matching for Protein Engineering](https://arxiv.org/abs/2603.11703)

**基本信息**

- 🔗 arXiv: [`2603.11703`](https://arxiv.org/abs/2603.11703)
- 👥 作者: Nicolas Deutschmann, Constance Ferragu, Jonathan D. Ziegler 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11703.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于蛋白质工程的生成式AI模型（EvoFlows）。该模型学习蛋白质序列的分布和突变路径，属于‘化学大模型’在生物化学和蛋白质设计领域的直接应用。

**📖 中文摘要**

本文介绍了EvoFlows，一种适用于蛋白质工程的变长序列到序列蛋白质建模方法。与自回归和掩码语言模型不同，EvoFlows对模板蛋白质序列执行有限、可控数量的插入、删除和替换。该方法利用编辑流来学习进化相关蛋白质序列之间的突变轨迹，同时模拟相关天然蛋白质的分布以及连接它们的突变路径。通过在UNIREF和OAS的不同蛋白质群落上进行广泛的计算机评估，证明EvoFlows在捕获蛋白质序列分布方面与蛋白质工程中常用的领先掩码语言模型质量相当，同时在从给定模板蛋白质生成非平凡但类天然突变体方面表现出更强的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce EvoFlows, a variable-length sequence-to-sequence protein modeling approach uniquely suited to protein engineering. Unlike autoregressive and masked language models, EvoFlows perform a limited, controllable number of insertions, deletions, and substitutions on a template protein sequence. In other words, EvoFlows predict not only _which_ mutation to perform, but also _where_ it should occur. Our approach leverages edit flows to learn mutational trajectories between evolutionarily-related protein sequences, simultaneously modeling distributions of related natural proteins and the mutational paths connecting them. Through extensive _in silico_ evaluation on diverse protein communities from UNIREF and OAS, we demonstrate that EvoFlows capture protein sequence distributions with a quality comparable to leading masked language models commonly used in protein engineering, while showing improved ability to generate non-trivial yet natural-like mutants from a given template protein.

</details>

---

### 17. [PhiPlot: A Web-Based Interactive EDA Environment for Atmospherically Relevant Molecules](https://arxiv.org/abs/2603.11751)

**基本信息**

- 🔗 arXiv: [`2603.11751`](https://arxiv.org/abs/2603.11751)
- 👥 作者: Matias Loukojärvi, Ananth Mahadevan, Katsiaryna Haitsiukevich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11751.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于探索大气化学分子数据集的交互式网络工具PhiPlot。它提供了用于化学信息学分析的数据集、资源和工具，特别是针对大气气溶胶形成研究，这与化学信息学中的数据资源和分析工具主题直接相关。

**📖 中文摘要**

本文介绍了PhiPlot，一个用于大气相关分子交互式探索和基于知识的降维的Web环境。该应用连接到一个现有的、不断演化的分子数据库集合，为大气化学中的数据驱动研究提供了一个可访问的界面。其集成了可视化、聚类和领域知识引导的嵌入细化功能，能够发现数据中的模式并支持假设生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in computational chemistry have produced high-dimensional datasets on atmospherically relevant molecules. To aid exploration of such datasets, particularly for the study of atmospheric aerosol formation, we introduce PhiPlot: a web-based environment for interactive exploration and knowledge-based dimensionality reduction. The integration of visualisation, clustering, and domain knowledge-guided embedding refinement enables the discovery of patterns in the data and supports hypothesis generation. The application connects to an existing, evolving collection of molecular databases, offering an accessible interface for data-driven research in atmospheric chemistry.

</details>

---

### 18. [OMNIA: Closing the Loop by Leveraging LLMs for Knowledge Graph Completion](https://arxiv.org/abs/2603.11820)

**基本信息**

- 🔗 arXiv: [`2603.11820`](https://arxiv.org/abs/2603.11820)
- 👥 作者: Frédéric Ieng, Soror Sahri, Mourad Ouzzani 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11820.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进知识图谱的补全，这涉及从现有结构化数据中推理缺失的关系（一种结构推理）。虽然不直接针对质谱，但‘质谱结构推理’的本质是从数据中推断化学结构，这与从知识图谱中推断缺失链接（结构）在方法论上具有相似性，都属于结构推理问题。论文提出的方法（结合聚类、嵌入和LLM验证）对于化学信息学中的结构推理具有潜在的方法论参考价值。

**📖 中文摘要**

本文提出了OMNIA，一个用于知识图谱补全（KGC）的两阶段方法，旨在弥合结构推理和语义推理。它首先通过在知识图谱内对语义相关的实体和关系进行聚类来生成候选三元组，然后通过轻量级嵌入过滤和基于LLM的语义验证来验证它们。OMNIA在内部知识图谱上运行，无需外部源，并专门针对LLM生成的图谱中最常见的隐式语义。在多个数据集上的实验表明，OMNIA显著提高了F1分数。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge Graphs (KGs) are widely used to represent structured knowledge, yet their automatic construction, especially with Large Language Models (LLMs), often results in incomplete or noisy outputs. Knowledge Graph Completion (KGC) aims to infer and add missing triples, but most existing methods either rely on structural embeddings that overlook semantics or language models that ignore the graph's structure and depend on external sources. In this work, we present OMNIA, a two-stage approach that bridges structural and semantic reasoning for KGC. It first generates candidate triples by clustering semantically related entities and relations within the KG, then validates them through lightweight embedding filtering followed by LLM-based semantic validation. OMNIA performs on the internal KG, without external sources, and specifically targets implicit semantics that are most frequent in LLM-generated graphs. Extensive experiments on multiple datasets demonstrate that OMNIA significantly improves F1-score compared to traditional embedding-based models. These results highlight OMNIA's effectiveness and efficiency, as its clustering and filtering stages reduce both search space and validation cost while maintaining high-quality completion.

</details>

---

### 19. [A Decade of Generative Adversarial Networks for Porous Material Reconstruction](https://arxiv.org/abs/2603.11836)

**基本信息**

- 🔗 arXiv: [`2603.11836`](https://arxiv.org/abs/2603.11836)
- 👥 作者: Ali Sadeghkhani, Brandon Bennett, Masoud Babaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11836.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于使用生成对抗网络（GANs）进行多孔材料重建的综述。它系统地分析了该领域十年来的进展、不同GAN架构的类别以及面临的挑战。这属于对‘化学大模型’（特别是生成模型在材料科学中的应用）这一主题的专门综述，提供了重要的相关讨论和领域概览。

**📖 中文摘要**

本文系统回顾了2017年至2026年初发表的96篇同行评议文章，分析了基于生成对抗网络（GANs）的多孔材料图像重建方法的演变和应用。综述将GAN架构分为六类，并揭示了在孔隙度准确性、渗透率预测和可重建体积方面的实质性进展。尽管取得了这些进展，但在计算效率、大规模重建的内存限制以及2D到3D转换中保持结构连续性方面仍然存在持续挑战。这项系统分析为根据特定应用需求选择适当的GAN架构提供了一个全面的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital reconstruction of porous materials has become increasingly critical for applications ranging from geological reservoir characterization to tissue engineering and electrochemical device design. While traditional methods such as micro-computed tomography and statistical reconstruction approaches have established foundations in this field, the emergence of deep learning techniques, particularly Generative Adversarial Networks (GANs), has revolutionized porous media reconstruction capabilities. This review systematically analyzes 96 peer-reviewed articles published from 2017 to early 2026, examining the evolution and applications of GAN-based approaches for porous material image reconstruction. We categorize GAN architectures into six distinct classes, namely Vanilla GANs, Multi-Scale GANs, Conditional GANs, Attention-Enhanced GANs, Style-based GANs, and Hybrid Architecture GANs. Our analysis reveals substantial progress including improvements in porosity accuracy (within 1% of original samples), permeability prediction (up to 79% reduction in mean relative errors), and achievable reconstruction volumes (from initial $64^3$ to current $2{,}200^3$ voxels). Despite these advances, persistent challenges remain in computational efficiency, memory constraints for large-scale reconstruction, and maintaining structural continuity in 2D-to-3D transformations. This systematic analysis provides a comprehensive framework for selecting appropriate GAN architectures based on specific application requirements.

</details>

---

### 20. [Inverse Neural Operator for ODE Parameter Optimization](https://arxiv.org/abs/2603.11854)

**基本信息**

- 🔗 arXiv: [`2603.11854`](https://arxiv.org/abs/2603.11854)
- 👥 作者: Zhi-Song Liu, Wenqing Peng, Helmi Toropainen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11854.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的AI框架（逆向神经算子，INO），用于从观测数据中逆向推断微分方程模型的参数。这属于‘化学大模型’在计算化学和动力学建模中的一个高级应用，即利用神经网络解决复杂的化学系统逆向问题（一种特殊的结构/参数推理）。

**📖 中文摘要**

本文提出了逆向神经算子（INO），一个用于从稀疏、部分观测中恢复隐藏ODE参数的两阶段框架。第一阶段，一个带有交叉注意力的条件傅里叶神经算子（C-FNO）学习一个可微分的代理模型，从任意稀疏输入重建完整的ODE轨迹。第二阶段，一个摊销漂移模型（ADM）学习参数空间中的核加权速度场，将随机参数初始化传输到真实值，而无需通过代理模型反向传播。在真实世界的大气化学基准（POLLU，25个参数）和合成基因调控网络（GRN，40个参数）上的实验表明，INO在参数恢复准确性上优于基于梯度和摊销的基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Inverse Neural Operator (INO), a two-stage framework for recovering hidden ODE parameters from sparse, partial observations. In Stage 1, a Conditional Fourier Neural Operator (C-FNO) with cross-attention learns a differentiable surrogate that reconstructs full ODE trajectories from arbitrary sparse inputs, suppressing high-frequency artifacts via spectral regularization. In Stage 2, an Amortized Drifting Model (ADM) learns a kernel-weighted velocity field in parameter space, transporting random parameter initializations toward the ground truth without backpropagating through the surrogate, avoiding the Jacobian instabilities that afflict gradient-based inversion in stiff regimes. Experiments on a real-world stiff atmospheric chemistry benchmark (POLLU, 25 parameters) and a synthetic Gene Regulatory Network (GRN, 40 parameters) show that INO outperforms gradient-based and amortized baselines in parameter recovery accuracy while requiring only 0.23s inference time, a 487x speedup over iterative gradient descent.

</details>

---

### 21. [Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding](https://arxiv.org/abs/2603.11924)

**基本信息**

- 🔗 arXiv: [`2603.11924`](https://arxiv.org/abs/2603.11924)
- 👥 作者: Xinyu Li, Zhen Zhang, Qi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11924.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”主题，提出了一个名为Chem4DLLM的多模态大语言模型，用于理解和解释化学动态过程。

**📖 中文摘要**

本文针对现有化学理解任务主要依赖静态分子表示、无法建模化学键断裂或构象变化等动态过程的局限性，提出了化学动力学理解（ChemDU）这一新任务。该任务旨在将4D分子轨迹（包含随时间演化的三维几何结构）转化为可解释的自然语言描述。为了支持这一任务，作者构建了首个配对4D分子轨迹与专家撰写解释的数据集Chem4DBench，并提出了Chem4DLLM模型。该模型将等变图编码器与预训练大语言模型相结合，显式地捕捉分子的几何结构和旋转动力学。这项工作直接关联“化学大模型”主题，因为它提出了一个专门用于化学动态理解的多模态大语言模型框架，旨在推动动态化学理解和多模态科学推理的研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability, we construct Chem4DBench, the first dataset pairing 4D molecular trajectories with expert-authored explanations across these settings. We further propose Chem4DLLM, a unified model that integrates an equivariant graph encoder with a pretrained large language model to explicitly capture molecular geometry and rotational dynamics. We hope that ChemDU, together with Chem4DBench and Chem4DLLM, will stimulate further research in dynamic chemical understanding and multimodal scientific reasoning.

</details>

---

### 22. [Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era](https://arxiv.org/abs/2603.12016)

**基本信息**

- 🔗 arXiv: [`2603.12016`](https://arxiv.org/abs/2603.12016)
- 👥 作者: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12016.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个名为Nyxus的开源图像特征提取库和工具。虽然其应用领域是生物医学成像，但其核心功能——从图像中提取大量、可定制的特征——是构建化学信息学中“化学大模型”（例如，用于分子图像或光谱分析）所需数据预处理和特征工程环节的关键潜在工具或数据资源。

**📖 中文摘要**

本文介绍了Nyxus，一个为大数据和AI时代设计的下一代图像特征提取库。现代成像仪器产生的数据量巨大，而Nyxus旨在解决大规模图像数据集处理的计算瓶颈。它从底层设计为可扩展的核外特征提取，支持2D和3D图像数据，并针对CPU和GPU进行了优化。Nyxus的综合特征集覆盖了包括放射组学和细胞分析在内的多个生物医学领域。该库以多种形式提供，包括Python包、命令行工具、Napari插件以及符合OCI标准的容器，以适应不同用户的需求和云端/超算工作流。Nyxus还支持一种新的特征提取方法学，允许通过编程方式调整特征集，以优化计算效率或覆盖范围，用于新颖的机器学习和深度学习应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of extracted features. To address these needs, we developed a novel feature extraction library called Nyxus. Nyxus is designed from the ground up for scalable out-of-core feature extraction for 2D and 3D image data and rigorously tested against established standards. The comprehensive feature set of Nyxus covers multiple biomedical domains including radiomics and cellular analysis, and is designed for computational scalability across CPUs and GPUs. Nyxus has been packaged to be accessible to users of various skill sets and needs: as a Python package for code developers, a command line tool, as a Napari plugin for low to no-code users or users that want to visualize results, and as an Open Container Initiative (OCI) compliant container that can be used in cloud or super-computing workflows aimed at processing large data sets. Further, Nyxus enables a new methodological approach to feature extraction allowing for programmatic tuning of many features sets for optimal computational efficiency or coverage for use in novel machine learning and deep learning applications.

</details>

---

### 23. [Chemical Reaction Networks Learn Better than Spiking Neural Networks](https://arxiv.org/abs/2603.12060)

**基本信息**

- 🔗 arXiv: [`2603.12060`](https://arxiv.org/abs/2603.12060)
- 👥 作者: Sophie Jaffard, Ivo F. Sbalzarini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12060.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及一种新型的、基于化学反应网络的机器学习模型。虽然其应用示例是图像分类，但其提出的“化学反应网络”作为一种计算和学习框架，与“化学大模型”的主题在概念上高度相关，探索了利用化学系统进行高效计算和学习的可能性，为化学信息学中的模型构建提供了新的思路。

**📖 中文摘要**

本文从数学上证明，无隐藏层的化学反应网络（CRN）可以解决某些需要尖峰神经网络（SNN）具备隐藏层才能完成的任务。证明使用了确定性质量作用动力学公式化的化学反应网络。具体而言，作者证明了一个特定的无隐藏层反应网络可以学习一个先前被证明需要带隐藏层的SNN才能实现的分类任务。他们提供了网络全局行为的解析遗憾界，并分析了其渐近行为和VC维。在一个数值实验中，作者验证了所提出的化学反应网络对于像素图像手写数字分类的学习能力，并表明它比带隐藏层的SNN更准确、更高效地解决了该任务。这为化学计算机中的机器学习提供了动机，并为生物细胞如何在生化反应网络中表现出比神经元网络更高效的学习行为提供了数学解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We mathematically prove that chemical reaction networks without hidden layers can solve tasks for which spiking neural networks require hidden layers. Our proof uses the deterministic mass-action kinetics formulation of chemical reaction networks. Specifically, we prove that a certain reaction network without hidden layers can learn a classification task previously proved to be achievable by a spiking neural network with hidden layers. We provide analytical regret bounds for the global behavior of the network and analyze its asymptotic behavior and Vapnik-Chervonenkis dimension. In a numerical experiment, we confirm the learning capacity of the proposed chemical reaction network for classifying handwritten digits in pixel images, and we show that it solves the task more accurately and efficiently than a spiking neural network with hidden layers. This provides a motivation for machine learning in chemical computers and a mathematical explanation for how biological cells might exhibit more efficient learning behavior within biochemical reaction networks than neuronal networks.

</details>

---

### 24. [Paper Title: LoV3D: Grounding Cognitive Prognosis Reasoning in Longitudinal 3D Brain MRI via Regional Volume Assessments](https://arxiv.org/abs/2603.12071)

**基本信息**

- 🔗 arXiv: [`2603.12071`](https://arxiv.org/abs/2603.12071)
- 👥 作者: Zhaoyang Jiang, Zhizhong Fu, David McAllister 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12071.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于医学影像分析的3D视觉语言模型（LoV3D）。这直接属于“大模型”在科学（特别是生物医学）领域的应用，是“化学大模型”主题在相邻生命科学领域的平行体现。其提出的多模态、可解释、基于医学知识的模型框架，对于构建用于化学和质谱分析的类似科学大模型具有重要的参考价值。

**📖 中文摘要**

本文提出了LoV3D，一个用于训练3D视觉语言模型（VLM）的流程，用于读取纵向T1加权脑部MRI，生成区域级解剖学评估，与先前扫描进行纵向比较，并最终输出三类诊断（认知正常、轻度认知障碍或痴呆）以及合成的诊断摘要。该流程通过强制标签一致性、纵向连贯性和生物学合理性来夯实最终诊断，从而减少幻觉风险。训练过程引入了一个临床加权的验证器，根据从标准化体积指标得出的规范参考自动评分候选输出，驱动无需人工标注的直接偏好优化。在ADNI测试集上，LoV3D实现了93.7%的三类诊断准确率，并在区域级解剖分类和零样本泛化上表现出色。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Longitudinal brain MRI is essential for characterizing the progression of neurological diseases such as Alzheimer's disease assessment. However, current deep-learning tools fragment this process: classifiers reduce a scan to a label, volumetric pipelines produce uninterpreted measurements, and vision-language models (VLMs) may generate fluent but potentially hallucinated conclusions. We present LoV3D, a pipeline for training 3D vision-language models, which reads longitudinal T1-weighted brain MRI, produces a region-level anatomical assessment, conducts longitudinal comparison with the prior scan, and finally outputs a three-class diagnosis (Cognitively Normal, Mild Cognitive Impairment, or Dementia) along with a synthesized diagnostic summary. The stepped pipeline grounds the final diagnosis by enforcing label consistency, longitudinal coherence, and biological plausibility, thereby reducing the risks of hallucinations. The training process introduces a clinically-weighted Verifier that scores candidate outputs automatically against normative references derived from standardized volume metrics, driving Direct Preference Optimization without a single human annotation. On a subject-level held-out ADNI test set (479 scans, 258 subjects), LoV3D achieves 93.7% three-class diagnostic accuracy (+34.8% over the no-grounding baseline), 97.2% on two-class diagnosis accuracy (+4% over the SOTA) and 82.6% region-level anatomical classification accuracy (+33.1% over VLM baselines). Zero-shot transfer yields 95.4% on MIRIAD (100% Dementia recall) and 82.9% three-class accuracy on AIBL, confirming high generalizability across sites, scanners, and populations. Code is available at this https URL .

</details>

---

### 25. [A Multi-Label Temporal Convolutional Framework for Transcription Factor Binding Characterization](https://arxiv.org/abs/2603.12073)

**基本信息**

- 🔗 arXiv: [`2603.12073`](https://arxiv.org/abs/2603.12073)
- 👥 作者: Pietro Demurtas, Ferdinando Zanchetta, Giovanni Perini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用深度学习模型（时间卷积网络）解决生物信息学中的关键问题——转录因子结合位点预测。这属于“化学大模型”或更广义的“科学AI大模型”在分子生物学和基因组学中的应用范畴。模型旨在理解生物分子（蛋白质与DNA）相互作用的复杂模式，与化学信息学中理解分子结构与性质关系的目标在方法论上相通。

**📖 中文摘要**

本文研究了DNA转录因子（TF）结合位点识别作为一个多标签分类问题。转录因子通过复杂且协作的机制调控基因表达。大多数当前方法专注于单个TF和二元分类任务，没有全面分析各种TF之间可能的相互作用。本文基于时间卷积网络（TCNs）构建深度学习模型，能够预测DNA序列上的多个TF结合谱，捕捉TF之间的相关性及其协作调控机制。结果表明，多标签学习可以实现可靠的预测性能，揭示与已知TF相互作用一致的具有生物学意义的基序和共结合模式，同时也能提示TF之间新的关系和协作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transcription factors (TFs) regulate gene expression through complex and co-operative mechanisms. While many TFs act together, the logic underlying TFs binding and their interactions is not fully understood yet. Most current approaches for TF binding site prediction focus on individual TFs and binary classification tasks, without a full analysis of the possible interactions among various TFs. In this paper we investigate DNA TF binding site recognition as a multi-label classification problem, achieving reliable predictions for multiple TFs on DNA sequences retrieved in public repositories. Our deep learning models are based on Temporal Convolutional Networks (TCNs), which are able to predict multiple TF binding profiles, capturing correlations among TFs andtheir cooperative regulatory mechanisms. Our results suggest that multi-label learning leading to reliable predictive performances can reveal biologically meaningful motifs and co-binding patterns consistent with known TF interactions, while also suggesting novel relationships and cooperation among TFs.

</details>

---

### 26. [Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction](https://arxiv.org/abs/2603.11061)

**基本信息**

- 🔗 arXiv: [`2603.11061`](https://arxiv.org/abs/2603.11061)
- 👥 作者: Van Le, Tan Le
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11061.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于蛋白质残基pKa预测的混合量子-经典机器学习框架。这直接属于【化学信息学】领域，涉及分子性质预测的计算模型，是化学大模型在特定生化预测任务（pKa）中的应用。

**📖 中文摘要**

本文提出了一种用于准确预测残基水平pKa值的可重现混合量子-经典框架。该框架通过高斯核基的量子启发特征映射来丰富残基水平的表示，这些量子增强描述符与归一化的结构特征相结合，形成统一的混合编码，并由深度量子神经网络（DQNN）进行处理。该架构捕捉了残基微环境中经典模型无法访问的非线性关系。在多个精选描述符集上的基准测试表明，相对于经典基线，DQNN实现了改进的跨上下文泛化能力。在PKAD-R实验基准和Aβ40案例研究上的外部评估进一步凸显了量子启发表示的鲁棒性和可迁移性。通过将量子启发的特征变换与经典生化描述符相结合，这项工作为残基水平pKa预测和蛋白质静电学的更广泛应用建立了一种可扩展且具有实验可迁移性的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue microenvironments that are not accessible to classical models. Benchmarking across multiple curated descriptor sets demonstrates that the DQNN achieves improved cross-context generalization relative to classical baselines. External evaluation on the PKAD-R experimental benchmark and an A$\beta$40 case study further highlights the robustness and transferability of the quantum-inspired representation. By integrating quantum-inspired feature transformations with classical biochemical descriptors, this work establishes a scalable and experimentally transferable approach for residue-level pKa prediction and broader applications in protein electrostatics.

</details>

---

### 27. [From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery](https://arxiv.org/abs/2603.11068)

**基本信息**

- 🔗 arXiv: [`2603.11068`](https://arxiv.org/abs/2603.11068)
- 👥 作者: Iman Peivaste, Salim Belouettar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型（LLM）的智能体框架，用于高熵合金（HEA）的逆向设计和发现。这直接属于【化学信息学】领域，是化学大模型（LLM作为推理和决策核心）在材料发现和设计中的具体应用。

**📖 中文摘要**

本文提出了一种ReAct（推理+行动）大语言模型（LLM）智能体框架，用于高熵合金（HEA）的逆向设计。该智能体能够自主提出、验证并迭代优化HEA成分，以可靠地形成目标晶体相。它通过查询一个基于4,753个实验记录（涵盖FCC、BCC、BCC+FCC、BCC+IM四种相）训练并校准的XGBoost代理模型来实现，该模型准确率达到94.66%。与贝叶斯优化和随机搜索基线相比，该智能体在描述符空间中重新发现目标相的成功率显著更高，并且其提出的成分更接近实验相流形。消融实验表明，领域先验知识引导智能体从回忆文献中的已知合金转向探索成分多样化的空间。这项工作确立了LLM引导的智能体推理作为逆向合金设计的一种原则性、透明且对数据流形有感知的补充方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering high-entropy alloy (HEA) compositions that reliably form a target crystal phase is a high-dimensional inverse design problem that conventional trial-and-error experimentation and forward-only machine learning models cannot efficiently solve. Here we present a ReAct (Reasoning + Acting) LLM agent that autonomously proposes, validates, and iteratively refines HEA compositions by querying a calibrated XGBoost surrogate trained on 4,753 experimental records across four phases (FCC, BCC, BCC+FCC, BCC+IM), achieving 94.66\% accuracy (F1 macro = 0.896). Against Bayesian optimisation (BO) and random search baselines, the full-prompt agent achieves descriptor-space rediscovery rates of 38\%, 18\%, and 38\% for FCC, BCC, and BCC+FCC (Mann--Whitney $p \leq 0.039$), with proposals lying 2.4--22.8$\times$ closer to the experimental phase manifold than random search. An ablation reveals that domain priors shift the agent from landmark-alloy recall toward compositionally diverse exploration -- an uninformed agent scores higher rediscovery by concentrating on literature-dense families, while the full-prompt agent explores underrepresented space (unique ratio 1.0 vs.\ 0.39 for BCC+FCC). These regimes represent distinct criteria: proximity to known literature versus genuine discovery. Spearman analysis confirms agent reasoning is statistically aligned with empirical phase distributions ($\rho = 0.736$, $p = 0.004$ for BCC). This work establishes LLM-guided agentic reasoning as a principled, transparent, and manifold-aware complement to gradient-free optimisation for inverse alloy design.

</details>

---

### 28. [Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction](https://arxiv.org/abs/2603.11125)

**基本信息**

- 🔗 arXiv: [`2603.11125`](https://arxiv.org/abs/2603.11125)
- 👥 作者: Yining Qian, Pengjie Wang, Yixiao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的深度学习框架（Co-Diffusion）用于药物-靶点亲和力预测。这直接属于【化学信息学】领域，涉及用于分子性质预测和药物发现的生成式AI模型（扩散模型），是化学大模型的一种具体实现形式。

**📖 中文摘要**

本文提出了Co-Diffusion，一种新颖的亲和力感知框架，将药物-靶点亲和力（DTA）预测重新定义为约束性潜在去噪过程以增强泛化能力。Co-Diffusion采用两阶段范式：第一阶段通过在有明确监督目标下对齐药物和靶点嵌入，建立亲和力引导的潜在流形，确保潜在空间反映内在的结合景观。第二阶段引入模态特定的潜在扩散作为随机扰动-去噪正则化器，迫使模型从噪声结构表示中恢复一致的亲和力语义。该方法有效缓解了生成式DTA模型中常见的重建-回归冲突。理论分析表明，Co-Diffusion最大化了药物结构、蛋白质序列和结合强度的联合似然变分下界。在多个基准上的广泛实验表明，Co-Diffusion显著优于最先进的基线方法，特别是在未见过的分子支架和新蛋白质家族上表现出卓越的零样本泛化能力，为在未探索化学空间中进行计算机药物优先排序铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.

</details>

---

### 29. [A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation](https://arxiv.org/abs/2603.11242)

**基本信息**

- 🔗 arXiv: [`2603.11242`](https://arxiv.org/abs/2603.11242)
- 👥 作者: Xiaoan Lang, Fang Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11242.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于生成和评估解耦潜在表示的通用框架。这在化学信息学中直接相关于构建可解释、可控的化学大模型（例如，用于分子生成或性质预测的VAE变体），以及从复杂数据（如质谱）中学习有意义的、解耦的表示以进行结构推理。

**📖 中文摘要**

本文提出了一个统一的变分自编码器（VAE）框架bfVAE，用于生成有效的潜在空间解耦，特别适用于表格数据。该框架集成了多种最先进的解耦VAE方法，并提出了两种无需真实生成因子即可评估解耦有效性的新程序：通过潜在遍历的特征方差异质性（FVH-LT）和潜在空间中的脏块稀疏回归（DBSR-LS），以及一个总结解耦有效性的潜在空间解耦指数（LSDI）。该工作与化学信息学中构建可解释的化学表示（化学大模型的核心）高度相关，因为它提供了评估和解释潜在表示（如VAE）的通用框架和工具，这对于构建可解释、可控制的化学生成模型或从质谱数据中学习结构表示至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FVH-LT and DBSR-LS to summarize the overall effectiveness of a VAE disentanglement method without requiring access to or knowledge of the ground-truth generative factors. To the best of our knowledge, these are the first assessment tools to achieve this. FVH-LT and DBSR-LS also enhance latent space interpretability and provide guidance on more efficient content generation. To ensure robust and consistent disentanglement, we develop a greedy alignment strategy (GAS) that mitigates label switching and aligns latent dimensions across runs to obtain aggregated results. We assess the bfVAE framework and validate FVH-LT, DBSR-LS, and LSDI in extensive experiments on tabular and image data. The results suggest that bfVAE surpasses existing disentangled VAE frameworks in terms of disentanglement quality, robustness, achieving a near-zero false discovery rate for informative latent dimensions, that FVH-LT and DBSR-LS reliably uncover semantically meaningful and domain-relevant latent structures, and that LSDI makes an effective overall quantitative summary on disentanglement effectiveness.

</details>

---

### 30. [A Standardized Framework For Evaluating Gene Expression Generative Models](https://arxiv.org/abs/2603.11244)

**基本信息**

- 🔗 arXiv: [`2603.11244`](https://arxiv.org/abs/2603.11244)
- 👥 作者: Andrea Rubbi, Andrea Giuseppe Di Francesco, Mohammad Lotfollahi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11244.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个用于标准化评估生成模型的框架和工具（GGE）。虽然应用于生物信息学，但其核心贡献——一个用于公平比较生成方法、加速进展的标准化评估套件——是构建和验证化学大模型（如分子生成模型）以及可能用于质谱数据生成的模型所急需的数据资源和工具。

**📖 中文摘要**

本文提出了Generated Genetic Expression Evaluator (GGE)，一个用于标准化评估单细胞基因表达生成模型的开源Python框架。它解决了当前评估实践中指标实现不一致、超参数选择不可比以及缺乏生物学基础指标的问题。GGE提供了一套全面的分布度量，并包含基于差异表达基因（DEG）的分析和扰动效应相关性等生物学驱动的评估，以实现标准化报告和可复现的基准测试。该工作与构建和评估生成模型（化学大模型的一个子领域）高度相关，因为它为生成模型的标准化评估提供了一个急需的框架。虽然应用于基因表达数据，但其关于评估协议、指标标准化和生物学相关性的原则和方法可以直接迁移到化学信息学中，用于评估分子生成模型或从质谱数据生成结构的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid development of generative models for single-cell gene expression data has created an urgent need for standardised evaluation frameworks. Current evaluation practices suffer from inconsistent metric implementations, incomparable hyperparameter choices, and a lack of biologically-grounded metrics. We present Generated Genetic Expression Evaluator (GGE), an open-source Python framework that addresses these challenges by providing a comprehensive suite of distributional metrics with explicit computation space options and biologically-motivated evaluation through differentially expressed gene (DEG)-focused analysis and perturbation-effect correlation, enabling standardized reporting and reproducible benchmarking. Through extensive analysis of the single-cell generative modeling literature, we identify that no standardized evaluation protocol exists. Methods report incomparable metrics computed in different spaces with different hyperparameters. We demonstrate that metric values vary substantially depending on implementation choices, highlighting the critical need for standardization. GGE enables fair comparison across generative approaches and accelerates progress in perturbation response prediction, cellular identity modeling, and counterfactual inference.

</details>

---

### 31. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个整合领域特定嵌入模型与大型语言模型（LLM）进行交互式数据探索和发现的框架（ELISA）。这直接对应于“化学大模型”的研究主题，即如何将化学领域的预训练模型（如用于分子或光谱的模型）与LLM的能力相结合，以构建智能的、可交互的化学信息学助手或推理系统。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个将scGPT表达嵌入与基于BioBERT的语义检索和LLM介导的解释相统一的、可解释的框架，用于交互式单细胞发现。它通过自动查询分类器将输入路由到不同的分析管道（基因标记评分、语义匹配或混合），并集成了跨60多个基因集的通路活性评分、使用280多个配体-受体对预测相互作用、条件感知比较分析和细胞类型比例估计等模块，所有这些都直接在嵌入数据上操作，无需访问原始计数矩阵。该工作在单细胞RNA测序数据上进行了基准测试。ELISA框架的核心是整合预训练的领域特定嵌入模型（scGPT）与大型语言模型（LLM）进行交互式探索和假设生成。这种方法论与化学信息学中构建“化学大模型”高度相关，后者同样旨在整合化学领域的预训练模型（如分子表示模型）与LLM的推理和交互能力，以进行分子发现、性质预测或从光谱数据中推理结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 32. [drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network](https://arxiv.org/abs/2405.08979)

**基本信息**

- 🔗 arXiv: [`2405.08979`](https://arxiv.org/abs/2405.08979)
- 👥 作者: Yoshitaka Inoue, Hunmin Lee, Tianfan Fu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08979.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于图神经网络和注意力机制的模型，用于药物反应预测和可解释的生物标志物发现。这直接关联于化学信息学和化学大模型的应用领域，即利用机器学习（特别是图神经网络和注意力机制）从复杂的化学和生物数据中预测分子性质、相互作用并进行解释，这是构建智能化学辅助系统的关键组成部分。

**📖 中文摘要**

本文提出了drGT，一个基于图深度学习的模型，用于预测药物敏感性并利用注意力系数（ACs）辅助生物标志物识别。drGT利用一个由药物、基因和细胞系反应关系构成的异质图。该模型在主要基准数据集（Sanger GDSC, NCI60, Broad CTRP）上进行了训练和评估。drGT通过注意力系数提供可解释性，用于识别药物影响的基因和生物过程。该工作与化学信息学中构建用于药物发现的预测模型相关，这是化学大模型的一个重要应用领域。模型利用图神经网络处理药物-细胞-基因异质网络，并利用注意力机制提供解释，这些技术和方法可以启发用于分子性质预测或分子-靶点相互作用预测的化学大模型的设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A challenge in drug response prediction is result interpretation compared to established knowledge. drGT is a graph deep learning model that predicts sensitivity and aids in biomarker identification using attention coefficients (ACs). drGT leverages a heterogeneous graph composed of relationships drawn from drugs, genes, and cell line responses. The model is trained and evaluated using major benchmark datasets: Sanger GDSC, NCI60, and Broad CTRP, which cover a wide range of drugs and cancer cell lines. drGT demonstrates AUROC of up to 94.5% under random splitting, 84.4% for unseen drugs, and 70.6% for unseen cell lines, comparable to existing benchmark methods while also providing interpretability. Regarding interpretability, we review drug-gene co-occurrences by text-mining PubMed abstracts for high-coefficient genes mentioning particular drugs. Across 976 drugs from NCI60 with known drug-target interactions (DTIs), model predictions utilized both known DTIs (36.9%) as well as additional predictive associations, many supported by literature. In addition, we compare the drug-gene associations identified by drGT with those from an established DTI prediction model and find that 63.67% are supported by either PubMed literature or predictions from the DTI model. Further, we describe the utilization of ACs to identify affected biological processes by each drug via enrichment analyses, thereby enhancing biological interpretability. Code is available at this https URL .

</details>

---

### 33. [Geometry of Singular Foliations and Learning Manifolds in ReLU Networks via the Data Information Matrix](https://arxiv.org/abs/2409.07412)

**基本信息**

- 🔗 arXiv: [`2409.07412`](https://arxiv.org/abs/2409.07412)
- 👥 作者: Eliot Tron, Rita Fioresi
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.07412.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和表征由ReLU神经网络学习到的数据空间的几何结构（奇异叶状结构）。这对于理解“化学大模型”的内部表示、提高其可解释性、以及进行知识迁移至关重要。研究模型如何组织和结构化高维化学数据（如分子指纹、质谱特征）的表示空间，是化学信息学基础研究的一部分。

**📖 中文摘要**

本文通过数据信息矩阵（DIM），一种Fisher信息矩阵的变体，为ReLU神经网络分类器训练的数据空间提供了一种自然的几何结构。该模型能够辨别数据空间上的奇异叶状结构。论文展示了这种叶状结构的奇异点包含在一个测度为零的集合中，并且几乎处处存在局部正则叶状结构。实验表明数据与此类叶状的叶子相关。此外，通过分析DIM的谱来测量数据集之间的距离，展示了该方法在知识迁移方面的潜力。该工作与理解机器学习模型（如神经网络）内部表示和学习到的流形结构密切相关。这对于构建更强大、可解释的化学大模型（例如，理解分子表示空间的结构，或质谱数据形成的流形）具有基础性意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding how real data is distributed in high dimensional spaces is the key to many tasks in machine learning. We want to provide a natural geometric structure on the space of data employing a ReLU neural network trained as a classifier. Through the Data Information Matrix (DIM), a variation of the Fisher information matrix, the model will discern a singular foliation structure on the space of data. We show that the singular points of such foliation are contained in a measure zero set, and that a local regular foliation exists almost everywhere. Experiments show that the data is correlated with leaves of such foliation. Moreover we show the potential of our approach for knowledge transfer by analyzing the spectrum of the DIM to measure distances between datasets.

</details>

---

### 34. [Distributed Koopman Learning using Partial Trajectories for Control](https://arxiv.org/abs/2412.07212)

**基本信息**

- 🔗 arXiv: [`2412.07212`](https://arxiv.org/abs/2412.07212)
- 👥 作者: Wenjian Hao, Zehui Lu, Devesh Upadhyay 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.07212.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个分布式框架，用于从数据中学习动力学模型（基于Koopman算子）。虽然应用于控制领域，但其方法论（分布式学习、Koopman算子、深度神经网络）与化学信息学中从时间序列数据（如分子动力学轨迹、时间分辨质谱）学习化学系统动力学的挑战直接相关。这可以视为构建能够模拟和预测化学过程动态的“化学大模型”的基础技术。

**📖 中文摘要**

本文提出了一种用于动力学学习的分布式数据驱动框架，称为使用部分轨迹的分布式深度Koopman学习（DDKL-PT）。在该框架中，多智能体系统中的每个智能体被分配一个离线部分轨迹，并在Koopman算子框架内使用深度神经网络局部近似未知动力学。通过交换局部估计的动力学而非训练数据，智能体在不共享其私有训练轨迹的情况下就全局动力学模型达成共识。该工作与从时间序列数据中学习系统动力学相关，这在化学信息学中可用于从分子动力学模拟或时间分辨光谱/质谱数据中学习模型。虽然应用场景是水面舰艇，但其分布式学习Koopman算子的框架可以启发用于从分布式化学数据源学习共享的、可解释的动力学模型，这是构建能够推理化学过程的大模型的一个潜在方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper proposes a distributed data-driven framework for dynamics learning, termed distributed deep Koopman learning using partial trajectories (DDKL-PT). In this framework, each agent in a multi-agent system is assigned a partial trajectory offline and locally approximates the unknown dynamics using a deep neural network within the Koopman operator framework. By exchanging local estimated dynamics rather than training data, agents achieve consensus on a global dynamics model without sharing their private training trajectories. Simulation studies on a surface vehicle demonstrate that DDKL-PT achieves consensus on the learned dynamics, and each agent attains reasonably small approximation errors on the testing dataset. Furthermore, a model predictive control scheme is developed by integrating the learned Koopman dynamics with known kinematic relations. Results on a reference-tracking task indicate that the distributedly learned dynamics are sufficiently accurate for model-based optimal control.

</details>

---

### 35. [Using LLM-Generated Draft Replies to Support Human Experts in Responding to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of Industrial AI](https://arxiv.org/abs/2412.12732)

**基本信息**

- 🔗 arXiv: [`2412.12732`](https://arxiv.org/abs/2412.12732)
- 👥 作者: Tita Alissa Bach, Aleksandar Babic, Narae Park 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.12732.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大型语言模型（LLM）作为专业领域（海事）人类专家工作流程辅助工具的实际效用。这直接对应于“化学大模型”研究主题中一个关键的应用方向：如何将LLM或领域大模型有效地集成到化学家的工作中，辅助完成如质谱解析、文献调研、实验设计等任务，并理解其人机协作的可行模式和局限性。

**📖 中文摘要**

本文是一项关于在航运业中使用LLM生成草稿回复以支持人类专家处理利益相关者查询的案例研究。研究通过初步研究、调查和文本相似性分析，发现LLM草稿可以简化工作流程，但通常需要大量修改以满足海事通信的特定需求。研究结论是，LLM在无人监督的情况下尚不成熟，但可以作为有价值的增强工具，最终决策权必须保留在人类专家手中。该工作与大型语言模型（LLM）在专业领域（如化学）的应用和评估直接相关。虽然领域是海事，但其核心问题——LLM作为专业领域人类专家的辅助工具的有效性、局限性以及人机协作模式——与探索“化学大模型”如何作为化学家的智能助手（例如，协助解读质谱数据、撰写实验报告或推理反应路径）的研究主题高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

</details>

---

### 36. [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177)

**基本信息**

- 🔗 arXiv: [`2501.15177`](https://arxiv.org/abs/2501.15177)
- 👥 作者: Yi Su, Jisheng Bai, Qisheng Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.15177.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对音频-语言模型（ALMs）这一特定多模态大模型主题的系统性综述。它全面组织了该领域的发展，分析了模型基础、评估和未来方向。这为“化学大模型”和“质谱结构推理”（可视为化学领域的一种多模态任务）的研究者提供了重要的相关讨论、分类框架和研究视角，有助于理解多模态领域大模型的通用发展规律和挑战。

**📖 中文摘要**

本文对音频-语言模型（ALMs）进行了首次系统性综述。ALMs在配对音频-文本数据上训练，旨在处理、理解和推理以音频为中心的多模态内容。论文提出了一个统一的分类法，涵盖ALM的基础（模型架构和训练目标），并建立了一个捕捉不同研究方面相互促进和约束的研究图景，以总结评估、局限性、关注点和有前景的方向。该综述虽然聚焦音频领域，但其对多模态大模型（结合特定领域数据与语言模型）的发展、技术基础、评估和挑战的系统性梳理，为“化学大模型”（即结合化学数据与语言模型的多模态模型）的研究提供了极佳的参考框架和前瞻性洞察。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified taxonomy of ALM foundations, including model architectures and training objectives; (3) establishment of a research landscape capturing mutual promotion and constraints among different research aspects, aiding in summarizing evaluations, limitations, concerns and promising directions. Our review contributes to helping researchers understand the development of existing technologies and future trends, while also providing valuable references for implementation in practical applications.

</details>

---

### 37. [GTM: A General Time-series Model for Enhanced Representation Learning of Time-Series Data](https://arxiv.org/abs/2502.03264)

**基本信息**

- 🔗 arXiv: [`2502.03264`](https://arxiv.org/abs/2502.03264)
- 👥 作者: Cheng He, Xu Huang, Gangwei Jiang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03264.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个通用、任务无关的序列数据（时间序列）生成模型（GTM），并提出了创新的表示学习方法（频域注意力）和预训练策略。这直接关联于“化学大模型”中处理化学序列数据（如分子序列、光谱序列）的表示学习和生成模型构建。其方法论为设计适用于化学序列的通用预训练模型提供了新的思路和技术参考。

**📖 中文摘要**

本文提出了一个通用时间序列模型（GTM），它通过一种新颖的频域注意力机制来推进表示学习，该机制捕获时间粒度感知的特征。GTM采用了一种通过混合掩码机制统一重构和自回归目标的新预训练策略，并结合了2D位置编码和跨度洗牌，以增强表示的鲁棒性和泛化性。GTM被确立为第一个生成任务无关的时间序列分析模型，无需任何任务特定修改即可无缝适应各种生成任务。该工作与构建通用、强大的序列数据表示学习模型密切相关。虽然应用于时间序列，但其核心思想（频域注意力、统一的预训练策略、任务无关的生成能力）可以迁移到化学序列数据（如SMILES字符串、质谱序列）的建模中，对于构建能够处理多种化学任务的通用化学序列大模型具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite recent progress in time-series foundation models, challenges persist in improving representation learning and adapting to diverse downstream tasks. We introduce a General Time-series Model (GTM), which advances representation learning via a novel frequency-domain attention mechanism that captures time-granularity-aware features, an aspect underexplored in prior research. We further propose a novel pre-training strategy that unifies reconstruction and autoregressive objectives through a hybrid masking mechanism. Our pre-training strategy, combined with 2D positional encoding and span shuffling, enhances the robustness and generalization of representations. GTM is established as the first generative-task-agnostic model for time-series analysis, enabling seamless adaptation to various generative tasks without any task-specific modifications. Extensive experiments demonstrate that GTM consistently outperforms SOTA models on various generative tasks and achieves strong classification results with minimal adaptation. Furthermore, GTM exhibits clear scaling behavior, with accuracy improving as model size and pre-training data increase.

</details>

---

### 38. [Riemannian Variational Flow Matching for Material and Protein Design](https://arxiv.org/abs/2502.12981)

**基本信息**

- 🔗 arXiv: [`2502.12981`](https://arxiv.org/abs/2502.12981)
- 👥 作者: Olga Zaghen, Floor Eijkelboom, Alison Pouplin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.12981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于流形上生成建模的新方法（RG-VFM）。这在化学信息学和材料科学中直接相关，因为分子结构、材料晶体结构等通常存在于具有复杂约束和对称性的非欧几里得空间中。构建能够在这些流形上高效、准确生成结构的模型是“化学大模型”用于分子和材料设计的关键技术。

**📖 中文摘要**

本文提出了黎曼高斯变分流匹配（RG-VFM），这是变分流匹配（VFM）在流形上生成建模的几何扩展。该工作为具有闭式测地线的流形推导了一个基于黎曼高斯分布的变分流匹配目标。论文形式化分析了该模型与黎曼流匹配（RFM）的关系，并假设端点预测通过直接最小化测地线距离提供了更强的学习信号。实验在合成球面和双曲基准以及材料和蛋白质生成的真实任务上进行。该工作与在非欧几里得空间（如分子构象空间、对称性约束的空间）上进行生成建模密切相关，这是化学和材料科学中分子设计、蛋白质设计等“化学大模型”应用的核心挑战。论文提出的RG-VFM框架为在这些复杂流形上构建更有效的生成模型提供了新的理论基础和算法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Riemannian Gaussian Variational Flow Matching (RG-VFM), a geometric extension of Variational Flow Matching (VFM) for generative modeling on manifolds. Motivated by the benefits of VFM, we derive a variational flow matching objective for manifolds with closed-form geodesics based on Riemannian Gaussian distributions. Crucially, in Euclidean space, predicting endpoints (VFM), velocities (FM), or noise (diffusion) is largely equivalent due to affine interpolations. However, on curved manifolds this equivalence breaks down. We formally analyze the relationship between our model and Riemannian Flow Matching (RFM), revealing that the RFM objective lacks a curvature-dependent penalty -- encoded via Jacobi fields -- that is naturally present in RG-VFM. Based on this relationship, we hypothesize that endpoint prediction provides a stronger learning signal by directly minimizing geodesic distances. Experiments on synthetic spherical and hyperbolic benchmarks, as well as real-world tasks in material and protein generation, demonstrate that RG-VFM more effectively captures manifold structure and improves downstream performance over Euclidean and velocity-based baselines. Code available at this https URL .

</details>

---

### 39. [FedSKD: Aggregation-free Model-heterogeneous Federated Learning via Multi-dimensional Similarity Knowledge Distillation for Medical Image Classification](https://arxiv.org/abs/2503.18981)

**基本信息**

- 🔗 arXiv: [`2503.18981`](https://arxiv.org/abs/2503.18981)
- 👥 作者: Ziqiao Weng, Weidong Cai, Bo Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.18981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个支持完全模型异构性的联邦学习框架（FedSKD），通过创新的知识蒸馏机制实现有效的知识共享。这在化学信息学中直接相关于在保护数据隐私的前提下，跨多个机构或实验室协作训练“化学大模型”（例如，用于药物发现或光谱分析的模型）。解决模型异构性和知识蒸馏效率问题是实际部署此类系统的关键。

**📖 中文摘要**

本文提出了FedSKD，一个新颖的模型异构联邦学习（MHFL）框架，通过轮转模型循环促进直接知识交换，无需集中聚合，同时允许客户端间完全异构的模型架构。FedSKD的核心创新在于多维相似性知识蒸馏，使得异构模型在联邦学习中能够在批次、像素/体素和区域级别进行双向跨客户端知识转移。该框架在基于fMRI的自闭症谱系障碍诊断和皮肤病变分类上进行了广泛评估。该工作与在隐私敏感场景下（如跨机构协作）构建和训练化学大模型高度相关。联邦学习是训练涉及敏感化学或生物医学数据的大模型的重要范式。FedSKD解决了模型异构性、知识转移和个性化等关键挑战，其框架可以应用于分布式化学数据上的模型训练，例如联合学习从多个实验室的质谱数据中推理结构的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Federated learning (FL) enables privacy-preserving collaborative model training without direct data sharing. Model-heterogeneous FL (MHFL) extends this paradigm by allowing clients to train personalized models with heterogeneous architectures tailored to their computational resources and application-specific needs. However, existing MHFL methods predominantly rely on centralized aggregation, which introduces scalability and efficiency bottlenecks, or impose restrictions requiring partially identical model architectures across clients. While peer-to-peer (P2P) FL removes server dependence, it suffers from model drift and knowledge dilution, limiting its effectiveness in heterogeneous settings. To address these challenges, we propose FedSKD, a novel MHFL framework that facilitates direct knowledge exchange through round-robin model circulation, eliminating the need for centralized aggregation while allowing fully heterogeneous model architectures across clients. FedSKD's key innovation lies in multi-dimensional similarity knowledge distillation, which enables bidirectional cross-client knowledge transfer at batch, pixel/voxel, and region levels for heterogeneous models in FL. This approach mitigates catastrophic forgetting and model drift through progressive reinforcement and distribution alignment while preserving model heterogeneity. Extensive evaluations on fMRI-based autism spectrum disorder diagnosis and skin lesion classification demonstrate that FedSKD outperforms state-of-the-art heterogeneous and homogeneous FL baselines, achieving superior personalization (client-specific accuracy) and generalization (cross-institutional adaptability). These findings underscore FedSKD's potential as a scalable and robust solution for real-world medical federated learning applications.

</details>

---

### 40. [Tuning-Free LLM Can Build A Strong Recommender Under Sparse Connectivity And Knowledge Gap Via Extracting Intent](https://arxiv.org/abs/2505.10900)

**基本信息**

- 🔗 arXiv: [`2505.10900`](https://arxiv.org/abs/2505.10900)
- 👥 作者: Wenqing Zheng, Noah Fatsi, Daniel Barcklow 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用免调优LLM提取意图、构建意图知识图谱，并结合GNN进行下游任务的框架（IKGR）。这种方法论与化学信息学中利用LLM从文本中提取化学知识、构建或增强化学知识图谱，并用于辅助分子设计、性质预测或质谱结构推理（例如，将质谱特征与文本描述的化学意图相关联）的研究高度相关。

**📖 中文摘要**

本文提出了LLM-based Intent Knowledge Graph Recommender (IKGR)，一个新颖的框架，它构建了一个以意图为中心的知识图谱，其中用户和物品都通过一个免调优、RAG引导的LLM流程提取的意图节点显式连接。通过将意图锚定在外部知识源和用户画像中，IKGR规范地表示了用户寻求什么和物品满足什么作为一等实体。为了缓解稀疏性，引入了互意图连接致密化策略。最后，在意图增强的图谱上使用轻量级GNN层来生成推荐信号。该工作与利用大型语言模型（LLM）和图神经网络（GNN）构建智能推荐系统相关。虽然应用于推荐系统，但其核心方法论——使用免调优LLM从文本中提取结构化意图（概念），并构建意图图谱以增强下游任务（如推荐）——可以迁移到化学信息学中。例如，可以使用类似方法从化学文献或描述中提取化学实体、反应意图或性质需求，构建化学知识图谱，并辅助分子检索、反应预测或质谱解析，这属于“化学大模型”应用和“质谱结构推理”中利用外部知识的一种形式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in recommendation with large language models (LLMs) often rely on either commonsense augmentation at the item-category level or implicit intent modeling on existing knowledge graphs. However, such approaches struggle to capture grounded user intents and to handle sparsity and cold-start scenarios. In this work, we present LLM-based Intent Knowledge Graph Recommender (IKGR), a novel framework that constructs an intent-centric knowledge graph where both users and items are explicitly linked to intent nodes extracted by a tuning-free, RAG-guided LLM pipeline. By grounding intents in external knowledge sources and user profiles, IKGR canonically represents what a user seeks and what an item satisfies as first-class entities. To alleviate sparsity, we further introduce a mutual-intent connectivity densification strategy, which shortens semantic paths between users and long-tail items without requiring cross-graph fusion. Finally, a lightweight GNN layer is employed on top of the intent-enhanced graph to produce recommendation signals with low latency. Extensive experiments on public and enterprise datasets demonstrate that IKGR consistently outperforms strong baselines, particularly on cold-start and long-tail slices, while remaining efficient through a fully offline LLM pipeline.

</details>

---

### 41. [Can Theoretical Physics Research Benefit from Language Agents?](https://arxiv.org/abs/2506.06214)

**基本信息**

- 🔗 arXiv: [`2506.06214`](https://arxiv.org/abs/2506.06214)
- 👥 作者: Sirui Lu, Zhijing Jin, Terry Jingchen Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06214.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题的扩展——即领域专用大模型（如理论物理大模型）的必要性、能力差距和构建路径。论文讨论了为特定科学领域（如物理）开发专门训练的大模型和工具，这与构建“化学大模型”的理念和挑战完全平行。

**📖 中文摘要**

本文探讨了大型语言模型（LLMs）在理论物理研究中的应用潜力与当前局限。作者指出，尽管LLMs在数学推理和代码生成方面表现出色，但在物理直觉、约束满足和可靠推理方面存在关键差距。物理研究需要近似判断、对称性利用和物理基础，这要求AI智能体接受专门的物理推理模式训练，并配备物理感知的验证工具。文章呼吁物理和AI社区合作，开发专门的训练数据集、捕捉物理推理质量的奖励信号，以及编码基本原理的验证框架，以实现AI驱动的科学发现。这与“化学大模型”主题高度相关，因为它讨论了领域专用大模型的必要性、训练数据和验证框架的开发，这些都是构建化学或物理等科学领域大模型的核心议题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are rapidly advancing across diverse domains, yet their application in theoretical physics remains inadequate. While current models show competence in mathematical reasoning and code generation, we identify critical gaps in physical intuition, constraint satisfaction, and reliable reasoning that cannot be addressed through prompting alone. Physics demands approximation judgment, symmetry exploitation, and physical grounding that require AI agents specifically trained on physics reasoning patterns and equipped with physics-aware verification tools. We argue that LLM would require such domain-specialized training and tooling to be useful in real-world for physics research. We envision physics-specialized AI agents that seamlessly handle multimodal data, propose physically consistent hypotheses, and autonomously verify theoretical results. Realizing this vision requires developing physics-specific training datasets, reward signals that capture physical reasoning quality, and verification frameworks encoding fundamental principles. We call for collaborative efforts between physics and AI communities to build the specialized infrastructure necessary for AI-driven scientific discovery.

</details>

---

### 42. [Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism](https://arxiv.org/abs/2509.06322)

**基本信息**

- 🔗 arXiv: [`2509.06322`](https://arxiv.org/abs/2509.06322)
- 👥 作者: Jiajun Bao, Nicolas Boullé, Toni J.B. Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.06322.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容展示了大型语言模型（作为“化学大模型”的一种实例或基础技术）在科学计算和复杂系统建模（此处为PDE动力学推断）中的新兴能力和机制。这直接关联到“化学大模型”主题下，模型在科学推理、预测和仿真方面的应用潜力。

**📖 中文摘要**

本文展示了仅通过文本训练的基础大语言模型（LLMs）能够在不进行微调或自然语言提示的情况下，从离散化的偏微分方程（PDE）解中准确推断时空动力学。研究发现，预测准确性随着时间上下文长度的增加而提高，但在更精细的空间离散化下会下降。在多步推演中，误差随时间范围代数增长，类似于经典有限差分求解器中的全局误差累积。作者将此解释为上下文神经缩放定律。为了理解LLMs内部如何处理PDE解以进行准确推演，作者分析了令牌级输出分布，并揭示了一个一致的三阶段上下文学习进展：从语法模式模仿开始，经过探索性高熵阶段，最终形成自信的、基于数值的预测。这项研究展示了LLMs在科学计算和复杂系统建模中的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated emergent in-context learning (ICL) capabilities across a range of tasks, including zero-shot time-series forecasting. We show that text-trained foundation models can accurately extrapolate spatiotemporal dynamics from discretized partial differential equation (PDE) solutions without fine-tuning or natural language prompting. Predictive accuracy improves with longer temporal contexts but degrades at finer spatial discretizations. In multi-step rollouts, where the model recursively predicts future spatial states over multiple time steps, errors grow algebraically with the time horizon, reminiscent of global error accumulation in classical finite-difference solvers. We interpret these trends as in-context neural scaling laws, where prediction quality varies predictably with both context length and output length. To better understand how LLMs are able to internally process PDE solutions so as to accurately roll them out, we analyze token-level output distributions and uncover a consistent three-stage ICL progression: beginning with syntactic pattern imitation, transitioning through an exploratory high-entropy phase, and culminating in confident, numerically grounded predictions.

</details>

---

### 43. [Streamline pathology foundation model by cross-magnification distillation](https://arxiv.org/abs/2509.23097)

**基本信息**

- 🔗 arXiv: [`2509.23097`](https://arxiv.org/abs/2509.23097)
- 👥 作者: Ziyu Su, Abdul Rehman Akbar, Usama Sajjad 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23097.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是针对特定科学领域（计算病理学）开发轻量级基础模型（Foundation Model），这属于“化学大模型”在生命科学/化学交叉领域的直接应用和实例。2) 论文提出了构建和训练领域专用基础模型的方法论（跨放大倍数蒸馏），并使用了大规模领域数据集（349万张图像），这为相关主题提供了数据资源和模型构建思路。

**📖 中文摘要**

本文介绍了XMAG，一个通过跨放大倍数蒸馏开发的轻量级病理学基础模型。该方法将知识从最先进的20倍放大倍数教师模型转移到一个高效的5倍放大倍数学生架构中。XMAG采用紧凑的主干网络，完全在5倍放大倍数下运行，与现有方法相比，每张全切片图像所需的图块数量减少了11.3倍。新颖的蒸馏框架结合了双级知识转移，对齐全局图像表示和局部空间令牌映射。作者在从公开数据集中整理的349万张图像上训练了XMAG，并在跨越多种癌症类型的六项临床相关组织病理学分析任务上评估了性能。XMAG在达到显著更大基础模型诊断准确率的1%以内的同时，实现了30倍的处理加速。这项工作确立了跨放大倍数蒸馏作为在资源受限临床环境中部署基础模型能力的一种可行方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models (FM) have transformed computational pathology but remain computationally prohibitive for clinical deployment due to their massive parameter counts and high-magnification processing requirements. Here, we introduce XMAG, a lightweight FM developed through corss-magnification distillation that transfers knowledge from state-of-the-art 20x magnification teacher to an efficient 5x magnification student architecture. XMAG employs a compact backbone and operates entirely at 5x, requiring 11.3 times fewer patches per whole slide image (WSI) compared to existing approaches. Our Novel distillation framework incorporates dual-level knowledge transfer, aligning both global image representations and local spatial token mapping. We trained XMAG on 3.49 million images curated from publicly available datasets and evaluated performance across six clinically relevant histopathology analysis tasks spanning multiple cancer types. XMAG achieved diagnostic accuracy within 1% of substantially larger foundation models while delivering 30-fold processing acceleration, reaching 8.8 WSIs per minute processing speed. Our cross-institutional validation confirmed robust generalization. Further, we developed an end-to-end training strategy to further boost our model's performance to approach the larger FMs' performance. These results establish cross-magnification distillation as a viable approach for deploying FM capabilities in resource-constrained clinical environments, potentially enabling real-time pathology AI integration.

</details>

---

### 44. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建和评估一个自主的“AI科学家”系统，该系统能够进行完整的科学研究工作流程（分析、假设、实验、写作）。这是“化学大模型”或“科学AI”主题的前沿和高级形态，即大模型作为自主研究智能体的应用。论文直接探讨了如何利用AI（包括大语言模型和编码智能体）驱动科学发现，与主题高度相关。

**📖 中文摘要**

本文介绍了Jr. AI Scientist，一个最先进的自主AI科学家系统，它模拟了新手学生研究人员的核心研究工作流程：在给定人类导师的基线论文后，系统分析其局限性，提出改进的新假设，进行迭代实验直到取得改进，并撰写结果论文。与先前假设完全自动化或在小规模代码上运行的方法不同，Jr. AI Scientist遵循明确的研究工作流程，并利用现代编码智能体来处理复杂的多文件实现，从而产生有科学价值的贡献。通过实验，Jr. AI Scientist成功生成了基于真实NeurIPS、IJCV和ICLR工作的新研究论文。评估包括使用AI评审员进行自动评估、作者主导的评估以及向专注于AI驱动贡献的场所Agents4Science提交。研究结果展示了AI科学家系统的当前能力和局限性，并全面报告了开发过程中识别的各种风险。这项工作阐明了AI科学家系统在当前研究中的角色和局限。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems (autoresearch) is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, iteratively experiments until improvements are achieved, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel methods. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 45. [De novo molecular structure elucidation from mass spectra via flow matching](https://arxiv.org/abs/2602.19912)

**基本信息**

- 🔗 arXiv: [`2602.19912`](https://arxiv.org/abs/2602.19912)
- 👥 作者: Ghaith Mqawass, Tuan Le, Fabian Theis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.19912.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一种从质谱数据中推断分子结构的生成模型。

**📖 中文摘要**

这篇论文提出了一种名为MSFlow的新型两阶段流匹配生成模型，用于解决质谱分析中的一个核心挑战：从质谱数据中从头推断分子结构。该模型的第一阶段使用公式限制的Transformer编码器将质谱编码为连续且富含化学信息的嵌入向量；第二阶段训练一个解码器流匹配模型，从质谱的潜在嵌入中重建分子。作者通过消融研究证明了使用信息保留的分子描述符对编码质谱的重要性，并论证了其离散流基解码器的优势。严格的评估表明，MSFlow能够将高达45%的分子质谱准确翻译成相应的分子表示，比当前最先进方法的性能提升了高达14倍。这项工作直接针对“质谱结构推理”这一核心主题，为化学信息学领域提供了一个强大的新工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

</details>

---

### 46. [Towards Highly Transferable Vision-Language Attack via Semantic-Augmented Dynamic Contrastive Interaction](https://arxiv.org/abs/2603.04839)

**基本信息**

- 🔗 arXiv: [`2603.04839`](https://arxiv.org/abs/2603.04839)
- 👥 作者: Yuanbo Li, Tianyang Xu, Cong Hu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04839.pdf)

**💡 相关性分析**

满足标准1：论文的核心技术（动态对比学习、语义增强）直接关联到多模态大模型的表示学习和鲁棒性，这对于理解和构建可靠的“化学大模型”具有重要参考价值。

**📖 中文摘要**

本文提出了一种名为SADCA（语义增强动态对比攻击）的新方法，旨在通过渐进式和语义引导的扰动来增强对抗样本在视觉-语言预训练模型上的可迁移性。SADCA通过对抗图像和文本之间的动态交互，逐步破坏跨模态对齐。它建立了一个涉及对抗样本、正样本和负样本的对比学习机制，以增强所获扰动的语义不一致性。此外，作者还发现传统基于迁移的攻击中常用的输入变换也适用于VLP模型，这启发了一个语义增强模块，以增加对抗样本的多样性和泛化性。尽管论文主要关注对抗攻击，但其核心技术创新——利用动态对比学习和语义增强来操纵和优化跨模态表示——深刻触及了多模态大模型（作为“化学大模型”的一种重要形态）的内部工作机制和鲁棒性。这项研究为理解如何有效影响或引导此类模型的输出提供了重要见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rapid advancement and widespread application of vision-language pre-training (VLP) models, their vulnerability to adversarial attacks has become a critical concern. In general, the adversarial examples can typically be designed to exhibit transferable power, attacking not only different models but also across diverse tasks. However, existing attacks on language-vision models mainly rely on static cross-modal interactions and focus solely on disrupting positive image-text pairs, resulting in limited cross-modal disruption and poor transferability. To address this issue, we propose a Semantic-Augmented Dynamic Contrastive Attack (SADCA) that enhances adversarial transferability through progressive and semantically guided perturbation. SADCA progressively disrupts cross-modal alignment through dynamic interactions between adversarial images and texts. This is accomplished by SADCA establishing a contrastive learning mechanism involving adversarial, positive and negative samples, to reinforce the semantic inconsistency of the obtained perturbations. Moreover, we empirically find that input transformations commonly used in traditional transfer-based attacks also benefit VLPs, which motivates a semantic augmentation module that increases the diversity and generalization of adversarial examples. Extensive experiments on multiple datasets and models demonstrate that SADCA significantly improves adversarial transferability and consistently surpasses state-of-the-art methods. The code is released at this https URL .

</details>

---

### 47. [Multi-Paradigm Collaborative Adversarial Attack Against Multi-Modal Large Language Models](https://arxiv.org/abs/2603.04846)

**基本信息**

- 🔗 arXiv: [`2603.04846`](https://arxiv.org/abs/2603.04846)
- 👥 作者: Yuanbo Li, Tianyang Xu, Cong Hu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04846.pdf)

**💡 相关性分析**

满足标准1：论文提出的多范式协同优化框架，为如何有效整合与平衡来自不同模态或数据源的信息提供了方法论参考，这与构建能够处理多源化学数据的“化学大模型”的核心技术挑战直接相关。

**📖 中文摘要**

本文提出了一个新颖的多范式协同攻击框架MPCAttack，以提升针对多模态大语言模型的对抗样本的可迁移性。MPCAttack从视觉图像和语言文本中聚合语义表示，通过多范式协同优化策略在聚合特征上进行联合对抗优化。通过对多范式特征进行对比匹配，MPCO自适应地平衡不同范式表示的重要性，并指导全局扰动优化，有效缓解了表示偏差。这项工作虽然聚焦于对抗攻击，但其核心思想——通过协同优化来自不同范式（模态）的表示来生成更强大的扰动——与构建能够有效融合多源信息（如分子结构、质谱、文本描述）的“化学大模型”在技术上面临相似的挑战。如何整合与平衡不同来源、不同表示的化学信息，是化学大模型成功的关键，而本文的方法为此提供了有益的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid progress of Multi-Modal Large Language Models (MLLMs) has significantly advanced downstream applications. However, this progress also exposes serious transferable adversarial vulnerabilities. In general, existing adversarial attacks against MLLMs typically rely on surrogate models trained within a single learning paradigm and perform independent optimisation in their respective feature spaces. This straightforward setting naturally restricts the richness of feature representations, delivering limits on the search space and thus impeding the diversity of adversarial perturbations. To address this, we propose a novel Multi-Paradigm Collaborative Attack (MPCAttack) framework to boost the transferability of adversarial examples against MLLMs. In principle, MPCAttack aggregates semantic representations, from both visual images and language texts, to facilitate joint adversarial optimisation on the aggregated features through a Multi-Paradigm Collaborative Optimisation (MPCO) strategy. By performing contrastive matching on multi-paradigm features, MPCO adaptively balances the importance of different paradigm representations and guides the global perturbation optimisation, effectively alleviating the representation bias. Extensive experimental results on multiple benchmarks demonstrate the superiority of MPCAttack, indicating that our solution consistently outperforms state-of-the-art methods in both targeted and untargeted attacks on open-source and closed-source MLLMs. The code is released at this https URL .

</details>

---

### 48. [Hyperbolic Multiview Pretraining for Robotic Manipulation](https://arxiv.org/abs/2603.04848)

**基本信息**

- 🔗 arXiv: [`2603.04848`](https://arxiv.org/abs/2603.04848)
- 👥 作者: Jin Yang, Ping Wei, Yixin Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04848.pdf)

**💡 相关性分析**

满足标准1：论文的核心创新（使用双曲空间进行3D感知预训练以更好地建模结构关系）与化学信息学中为具有复杂结构的分子学习表示这一根本任务高度相关，为“化学大模型”的表示学习提供了新的几何视角和潜在技术路径。

**📖 中文摘要**

本文提出了HyperMVP，一个用于双曲多视图预训练的自监督框架。作者指出，现有的3D感知视觉预训练方法受限于欧几里得嵌入空间，其平坦的几何形状限制了它们对嵌入之间结构关系建模的能力。双曲空间提供了更适合捕捉结构关系的几何特性。在方法上，作者扩展了掩码自编码器范式，并设计了一个GeoLink编码器来学习多视图双曲表示。预训练的编码器随后在机器人操作任务上通过视觉运动策略进行微调。这项工作展示了在非欧几里得空间中进行3D感知预训练对于学习鲁棒和可泛化的表示的有效性。虽然应用场景是机器人操作，但其核心贡献——利用双曲空间更好地建模结构化关系（如分子图、官能团层次结构）——与化学信息学中表示学习的目标高度契合。为分子或材料等具有内在层次或树状结构的化学实体学习嵌入，是“化学大模型”的基础，而双曲空间为此提供了有潜力的数学工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

3D-aware visual pretraining has proven effective in improving the performance of downstream robotic manipulation tasks. However, existing methods are constrained to Euclidean embedding spaces, whose flat geometry limits their ability to model structural relations among embeddings. As a result, they struggle to learn structured embeddings that are essential for robust spatial perception in robotic applications. To this end, we propose HyperMVP, a self-supervised framework for \underline{Hyper}bolic \underline{M}ulti\underline{V}iew \underline{P}retraining. Hyperbolic space offers geometric properties well suited for capturing structural relations. Methodologically, we extend the masked autoencoder paradigm and design a GeoLink encoder to learn multiview hyperbolic representations. The pretrained encoder is then finetuned with visuomotor policies on manipulation tasks. In addition, we introduce 3D-MOV, a large-scale dataset comprising multiple types of 3D point clouds to support pretraining. We evaluate HyperMVP on COLOSSEUM, RLBench, and real-world scenarios, where it consistently outperforms strong baselines across diverse tasks and perturbation settings. Our results highlight the potential of 3D-aware pretraining in a non-Euclidean space for learning robust and generalizable robotic manipulation policies.

</details>

---

### 49. [On the Value of Tokeniser Pretraining in Physics Foundation Models](https://arxiv.org/abs/2603.05598)

**基本信息**

- 🔗 arXiv: [`2603.05598`](https://arxiv.org/abs/2603.05598)
- 👥 作者: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05598.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（基础模型的分词器预训练、表示学习优化）与构建和优化“化学大模型”的方法论高度相关，为处理复杂化学数据提供了可借鉴的技术思路。

**📖 中文摘要**

本文研究了分词器预训练对物理仿真基础模型精度和效率的影响。作者指出，现代高分辨率模拟产生了跨越不同物理体系和尺度的海量数据。训练基础模型来学习这些数据背后的动力学，能够对复杂多物理现象进行建模。然而，同时从头学习两个任务（提取高分辨率时空数据的紧凑表示和捕捉主导物理动力学）可能会相互影响。本文表明，在训练动力学模型之前，使用自编码目标对分词器进行预训练，可以显著提升物理仿真的计算效率。值得注意的是，这种收益的大小取决于领域对齐：在与仿真任务相同的物理系统上进行预训练能带来最大的改进。作者进一步引入了灵活的时空压缩操作，支持运行时可调的压缩比，以实现对不同下游任务的高效适应。这项工作虽然主要面向物理仿真，但其核心方法——通过预训练优化表示学习以提升下游任务（如动力学建模）的性能——与构建和优化“化学大模型”所面临的挑战（如高效处理高维化学数据、学习分子表示）在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an autoencoding objective prior to training the dynamics model enhances computational efficiency for physics emulation. Notably, the magnitude of this benefit depends on domain alignment: pretraining on the same physical system as the emulation task yields the largest improvements, while pretraining on other systems provides moderate gains. In-domain pretraining reduces VRMSE by 64% after 10,500 training steps compared to training from scratch. To our knowledge, this is the first systematic investigation of tokeniser pretraining for physics foundation models. We further introduce flexible spatiotemporal compression operations that extend causal convolutions to support runtime-adjustable compression ratios, enabling efficient adaptation to diverse downstream tasks. Our findings provide practical guidance for training efficient physics emulators and highlight the importance of strategic pretraining data selection.

</details>

---

### 50. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种新的潜在推理框架（LatentChem）来改进化学大语言模型的推理效率和性能。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）主要依赖显式自然语言思维链（CoT）进行复杂推理的局限性。作者认为，化学推理本质上是连续和结构化的，将其强制编码为离散的语言标记会导致表示不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续潜在空间中直接执行多步推理，而仅在最终输出时生成语言。实验表明，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐步放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变带来了计算优势，在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于基于CoT的基线取得了59.88%的非平局胜率，同时实现了平均10.84倍的推理加速。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 51. [Semantics-Aware Caching for Concept Learning](https://arxiv.org/abs/2603.06506)

**基本信息**

- 🔗 arXiv: [`2603.06506`](https://arxiv.org/abs/2603.06506)
- 👥 作者: Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06506.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于加速概念学习（一种知识库上的机器学习）的语义感知缓存工具/方法。概念学习是化学信息学中用于从结构化数据（如分子知识库）中学习规则或模式的重要技术，因此该工具与化学信息学领域的数据处理和资源优化相关。

**📖 中文摘要**

本文提出了一种语义感知缓存方法，用于加速概念学习。概念学习是一种在描述逻辑知识库上运行的监督机器学习形式。最先进的概念学习者通常需要在可数无限的概念空间中进行迭代搜索，每次迭代都需要检索候选概念的实例。复杂的学习问题可能需要数千次实例检索调用，导致运行时挑战。本文提出的缓存本质上是一个子包含感知映射，通过清晰的集合操作将概念与实例集联系起来。实验表明，该缓存可以将概念检索和概念学习的运行时间减少一个数量级，并且对符号推理器和神经符号推理器都有效。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

</details>

---

### 52. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于“机器学习原子间势”（MLIPs）的新型架构。MLIPs是计算化学和材料科学中用于模拟原子相互作用的核心工具，属于化学信息学和计算化学的交叉领域。论文直接围绕提升化学模拟模型的性能这一主题展开。

**📖 中文摘要**

本文系统地开发了用于机器学习原子间势（MLIPs）的混合专家（MoE）和混合线性专家（MoLE）架构，并分析了路由策略和专家设计的影响。MLIPs能够实现精确的大规模原子模拟。作者展示了稀疏激活与共享专家相结合能带来显著的性能提升，并且当存在共享专家时，非线性MoE公式优于MoLE，强调了非线性专家专业化的重要性。由此产生的元素级MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、具有化学可解释性的专家专业化，表明该模型有效地捕捉了元素特定的化学特征，用于精确的原子间建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 53. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准1和2：论文第一部分的核心内容是发展束-等离子体集体振荡的理论模型（标准1），这涉及带电粒子在介质中的相互作用，与质谱分析中离子运动的基本物理有概念上的关联。第二部分使用了无监督学习框架（Prometheus）来分析模拟数据，展示了机器学习在物理系统分析中的应用（标准2）。

**📖 中文摘要**

本文为中等能量（10-100 MeV）强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。第一部分从Vlasov-Poisson系统出发，推导了林哈德介电函数和随机相位近似极化张量，证明了在临界束密度以上存在无阻尼的朗缪尔波模式，并给出了显式的束-等离子体色散关系。空间电荷效应驱动了反常束展宽和弗里德尔振荡。束-等离子体转变通过重整化群分析属于3D Ising普适类。第二部分使用基于beta-VAE的Prometheus框架，对粒子模拟（PIC）得到的静态结构因子数据S(q)进行无监督分析，验证了理论预测，成功检测到集体等离子体振荡的开始，并解析了q=2k_F处的科恩异常。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

## 📊 数据统计
- 累计运行天数：28
- 累计论文数量：2030

## 📝 历史记录

> 暂无历史数据

