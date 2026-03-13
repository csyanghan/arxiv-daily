# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-13 12:48:13

## 📅 2026-03-13 (今日最新)

**相关论文数：56**

### 1. [Graph Tokenization for Bridging Graphs and Transformers](https://arxiv.org/abs/2603.11099)

**基本信息**

- 🔗 arXiv: [`2603.11099`](https://arxiv.org/abs/2603.11099)
- 👥 作者: Zeyuan Guo, Enmao Diao, Cheng Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11099.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种连接图数据与Transformer的通用框架，这属于构建能够处理复杂结构化数据（如图）的‘化学大模型’的基础方法学研究。其提出的图标记化技术是构建和理解大模型如何处理非欧几里得数据的关键一步，与化学信息学中分子图表示学习高度相关。

**📖 中文摘要**

本文提出了一种图标记化框架，旨在弥合图结构化数据与Transformer序列模型之间的鸿沟。该框架结合了可逆的图序列化方法和在大型语言模型中广泛采用的字节对编码（BPE）标记器，将图转换为顺序表示。为了使序列化过程更好地捕捉结构信息，它利用图子结构的全局统计信息进行引导，确保频繁出现的子结构在序列中出现得更频繁，并能被BPE合并为有意义的标记。实验结果表明，该标记器使得BERT等Transformer模型无需架构修改即可直接应用于图基准测试，并在14个基准数据集上取得了最先进的结果，经常优于图神经网络和专门的图Transformer。这项工作为将图数据整合到序列模型生态系统中提供了桥梁。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of large pretrained Transformers is closely tied to tokenizers, which convert raw input into discrete symbols. Extending these models to graph-structured data remains a significant challenge. In this work, we introduce a graph tokenization framework that generates sequential representations of graphs by combining reversible graph serialization, which preserves graph information, with Byte Pair Encoding (BPE), a widely adopted tokenizer in large language models (LLMs). To better capture structural information, the graph serialization process is guided by global statistics of graph substructures, ensuring that frequently occurring substructures appear more often in the sequence and can be merged by BPE into meaningful tokens. Empirical results demonstrate that the proposed tokenizer enables Transformers such as BERT to be directly applied to graph benchmarks without architectural modifications. The proposed approach achieves state-of-the-art results on 14 benchmark datasets and frequently outperforms both graph neural networks and specialized graph transformers. This work bridges the gap between graph-structured data and the ecosystem of sequence models. Our code is available at \href{ this https URL }{\color{blue}here}.

</details>

---

### 2. [Learning Tree-Based Models with Gradient Descent](https://arxiv.org/abs/2603.11117)

**基本信息**

- 🔗 arXiv: [`2603.11117`](https://arxiv.org/abs/2603.11117)
- 👥 作者: Sascha Marton
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11117.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、可扩展的机器学习模型训练方法，该方法旨在提升模型的可解释性和性能。虽然未直接提及化学或质谱，但其核心——‘通过梯度下降学习决策树’——代表了一种构建更强大、更可解释的机器学习模型（可视为‘大模型’的一种形式或组件）的创新方法。这种基础模型学习方法与构建用于化学信息学的专用大模型高度相关。

**📖 中文摘要**

本文提出了一种通过梯度下降学习硬、轴对齐决策树的新方法。传统决策树学习算法（如CART）因其组合复杂性和离散、不可微的特性而面临挑战，通常依赖于贪婪搜索，导致次优结构且难以集成到现代机器学习流程中。本方法利用带有直通算子的反向传播，在密集的决策树表示上联合优化所有树参数。这解决了传统算法的两个主要限制：1）梯度训练不受局部最优分割顺序选择的约束，而是联合优化所有参数；2）通过利用梯度下降进行优化，该方法可以无缝集成到依赖梯度下降的现有ML方法中，例如多模态和强化学习任务。该方法在多个领域实现了最先进的结果，包括用于小型表格数据集的可解释决策树、用于复杂表格数据的高级模型、多模态学习和无信息损失的可解释强化学习。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tree-based models are widely recognized for their interpretability and have proven effective in various application domains, particularly in high-stakes domains. However, learning decision trees (DTs) poses a significant challenge due to their combinatorial complexity and discrete, non-differentiable nature. As a result, traditional methods such as CART, which rely on greedy search procedures, remain the most widely used approaches. These methods make locally optimal decisions at each node, constraining the search space and often leading to suboptimal tree structures. Additionally, their demand for custom training methods precludes a seamless integration into modern machine learning (ML) approaches. In this thesis, we propose a novel method for learning hard, axis-aligned DTs through gradient descent. Our approach utilizes backpropagation with a straight-through operator on a dense DT representation, enabling the joint optimization of all tree parameters, thereby addressing the two primary limitations of traditional DT algorithms. First, gradient-based training is not constrained by the sequential selection of locally optimal splits but, instead, jointly optimizes all tree parameters. Second, by leveraging gradient descent for optimization, our approach seamlessly integrates into existing ML approaches e.g., for multimodal and reinforcement learning tasks, which inherently rely on gradient descent. These advancements allow us to achieve state-of-the-art results across multiple domains, including interpretable DTs rees for small tabular datasets, advanced models for complex tabular data, multimodal learning, and interpretable reinforcement learning without information loss. By bridging the gap between DTs and gradient-based optimization, our method significantly enhances the performance and applicability of tree-based models across various ML domains.

</details>

---

### 3. [H2LooP Spark Preview: Continual Pretraining of Large Language Models for Low-Level Embedded Systems Code](https://arxiv.org/abs/2603.11139)

**基本信息**

- 🔗 arXiv: [`2603.11139`](https://arxiv.org/abs/2603.11139)
- 👥 作者: Amit Singh, Vedant Nipane, Pulkit Agrawal 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11139.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对特定领域（嵌入式系统）对大型语言模型进行持续预训练和适配。这直接属于‘化学大模型’研究范畴的平行案例，即如何使通用大模型获得特定领域的专业知识（在本文中是嵌入式代码，在化学信息学中则是化学知识）。其方法学（领域特定数据构建、持续预训练、LoRA适配）对构建化学领域大模型具有直接的参考价值。

**📖 中文摘要**

本文介绍了H2LooP Spark Preview，这是一个针对嵌入式系统代码领域的持续预训练（CPT）管道。大型语言模型在通用编程语言上表现出强大的代码生成能力，但在涉及硬件寄存器操作、供应商特定SDK、实时操作系统API和硬件抽象层等专业领域（如低级嵌入式系统编程）中仍然受限。该工作将完全开放的语言模型OLMo-3-7B适配到嵌入式系统领域，使用BF16 LoRA在8个NVIDIA H100 GPU上进行训练。训练语料库通过分层数据表到代码映射方法构建，涵盖117个制造商的100B原始嵌入式系统数据令牌。持续的预训练带来了显著提升，领域内困惑度降低了70.4%，在涵盖13个嵌入式领域的生成式代码补全基准测试中，该7B模型在8个类别上的令牌准确率超过了Claude Opus 4.6和Qwen3-Coder-30B。这表明有针对性的持续预训练能使较小的开放权重模型在专业任务上媲美前沿系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) demonstrate strong code generation abilities in general-purpose programming languages but remain limited in specialized domains such as low-level embedded systems programming. This domain involves hardware register manipulation, vendor-specific SDKs, real-time operating system APIs, and hardware abstraction layers that are underrepresented in standard pretraining corpora. We introduce H2LooP Spark Preview, a continual pretraining (CPT) pipeline that adapts the OLMo-3-7B-a fully open language model to the embedded systems domain using BF16 LoRA with rank-stabilized scaling on 8 NVIDIA H100 GPUs. Our training corpus is constructed from repository-datasheet pairs covering 100B tokens of raw embedded systems data across 117 manufacturers, processed using the hierarchical datasheet-to-code mapping approach proposed in SpecMap (Nipane et al., 2026). The resulting curated dataset split contains 23.5B tokens across 13 embedded domains. Continual pretraining with high-rank LoRA (r=512) yields substantial gains, reducing in-domain perplexity by 70.4% and held-out repository perplexity by 66.1%. On generative code completion benchmarks spanning 13 embedded domains, our 7B model outperforms Claude Opus 4.6 and Qwen3-Coder-30B on 8 categories in token accuracy, showing that targeted continual pretraining enables smaller open-weight models to rival frontier systems on specialized technical tasks. We release the production training checkpoint on Huggingface as an open-source artifact.

</details>

---

### 4. [Bridging Behavioral Biometrics and Source Code Stylometry: A Survey of Programmer Attribution](https://arxiv.org/abs/2603.11150)

**基本信息**

- 🔗 arXiv: [`2603.11150`](https://arxiv.org/abs/2603.11150)
- 👥 作者: Marek Horvath, Emilia Pietrikova, Diomidis Spinellis
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11150.pdf)

**💡 相关性分析**

满足标准3：这是一篇针对‘程序员归属’（可视为代码作者分析）领域的系统性综述论文。它全面回顾了该领域的研究现状、方法、特征和挑战。虽然主题是代码分析而非化学，但其作为‘综述展望相关’论文的性质符合标准3。它提供的系统化分析框架和方法论回顾，对于思考如何将类似的分析技术（如风格计量学、行为分析）应用于化学领域（例如，分析质谱数据或化学反应的‘风格’以进行来源推断或模式识别）具有启发意义。

**📖 中文摘要**

本文对源代码作者归属研究进行了系统的梳理和综述。程序员归属旨在利用风格、结构或行为特征来识别或验证源代码工件的作者。该问题在软件工程、安全和数字取证领域均有研究，产生了大量方法多样的出版物。本文通过结构化筛选过程，选取了2012年至2025年间发表的47项研究进行分析。分析维度包括作者归属任务、特征类别、学习与建模方法、数据集来源和评估实践。基于此分析，本文推导了一个将风格和行为特征类型与常用机器学习技术相关联的分类法，并提供了出版物趋势、基准和编程语言的描述性概述。内容级分析突出了该领域的主要主题集群。结果表明，当前研究强烈依赖于风格特征进行封闭世界的作者归属，并严重依赖少数基准数据集，而行为信号、作者验证和可重复性方面的探索较少。本研究将现有研究整合到一个统一的框架中，并指出了可指导未来工作的方法学差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Programmer attribution seeks to identify or verify the author of a source code artifact using stylistic, structural, or behavioural characteristics. This problem has been studied across software engineering, security, and digital forensics, resulting in a growing and methodologically diverse set of publications. This paper presents a systematic mapping study of programmer attribution research focused on source code analysis. From an initial set of 135 candidate publications, 47 studies published between 2012 and 2025 were selected through a structured screening process. The included works are analysed along several dimensions, including authorship tasks, feature categories, learning and modelling approaches, dataset sources, and evaluation practices. Based on this analysis, we derive a taxonomy that relates stylistic and behavioural feature types to commonly used machine learning techniques and provide a descriptive overview of publication trends, benchmarks, programming languages. A content-level analysis highlights the main thematic clusters in the field. The results indicate a strong focus on closed-world authorship attribution using stylometric features and a heavy reliance on a small number of benchmark datasets, while behavioural signals, authorship verification, and reproducibility remain less explored. The study consolidates existing research into a unified framework and outlines methodological gaps that can guide future work. This manuscript is currently under review. The present version is a preprint.

</details>

---

### 5. [Differentiable Thermodynamic Phase-Equilibria for Machine Learning](https://arxiv.org/abs/2603.11249)

**基本信息**

- 🔗 arXiv: [`2603.11249`](https://arxiv.org/abs/2603.11249)
- 👥 作者: Karim K. Ben Hicham, Moreno Ascani, Jan G. Rittig 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11249.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合机器学习和热力学原理的新方法，用于精确预测化学工程中的相平衡。这直接属于‘化学大模型’的应用范畴，即构建能够理解和模拟复杂化学物理过程的智能模型。其提出的‘可微分热力学相平衡’框架是化学信息学和过程工程中构建下一代预测模型的重要进展。

**📖 中文摘要**

本文提出了DISCOMAX，一种用于相平衡计算的可微分算法，该算法在训练和推理时都能保证热力学一致性。相平衡的准确预测是化学工程的核心挑战。最近，将热力学结构融入神经网络以实现物理一致性的机器学习方法在活度系数建模方面表现出强大性能。然而，将这些方法扩展到基于极值原理（如液-液平衡）的平衡数据仍然很困难。DISCOMAX方法植根于统计热力学，通过离散枚举随后对可行状态进行掩码softmax聚合来工作，并结合直通梯度估计器，实现对神经g^E模型端到端的物理一致性学习。该方法在二元液-液平衡数据上进行了评估，结果表明其性能优于现有的基于代理的方法，同时为从不同类型的平衡数据中学习提供了一个通用框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of phase equilibria remains a central challenge in chemical engineering. Physics-consistent machine learning methods that incorporate thermodynamic structure into neural networks have recently shown strong performance for activity-coefficient modeling. However, extending such approaches to equilibrium data arising from an extremum principle, such as liquid-liquid equilibria, remains difficult. Here we present DISCOMAX, a differentiable algorithm for phase-equilibrium calculation that guarantees thermodynamic consistency at both training and inference, only subject to a user-specified discretization. The method is rooted in statistical thermodynamics, and works via a discrete enumeration with subsequent masked softmax aggregation of feasible states, and together with a straight-through gradient estimator to enable physics-consistent end-to-end learning of neural $g^{E}$-models. We evaluate the approach on binary liquid-liquid equilibrium data and demonstrate that it outperforms existing surrogate-based methods, while offering a general framework for learning from different kinds of equilibrium data.

</details>

---

### 6. [A Machine Learning-Enhanced Hopf-Cole Formulation for Nonlinear Gas Flow in Porous Media](https://arxiv.org/abs/2603.11250)

**基本信息**

- 🔗 arXiv: [`2603.11250`](https://arxiv.org/abs/2603.11250)
- 👥 作者: V. S. Maduru, K. B. Nakshatrala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11250.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合物理模型（Klinkenberg效应、Hopf-Cole变换）和机器学习（共享主干神经网络、DeepLS求解器）的集成框架，用于模拟和反演多孔介质中的气体流动。这属于构建‘物理信息机器学习’或‘科学机器学习’模型，是‘化学大模型’在化工、能源等具体领域的高级应用，旨在解决具有强非线性和不确定性的复杂物理化学过程。

**📖 中文摘要**

本文提出了一个用于多孔介质中气体输运建模的集成框架，该框架结合了Klinkenberg增强的本构关系、Hopf-Cole变换的混合形式线性控制方程、共享主干神经网络架构和深度最小二乘（DeepLS）求解器。Hopf-Cole变换将原始非线性流动方程重新表述为与达西模型密切相关的等效线性系统，而混合公式与共享主干神经架构相结合，能够同时准确预测压力场和速度场。该框架还自然地促进了从有限或间接观测中反演压力依赖的渗透率和滑移参数，实现了对难以通过实验测量的流动特性的高效估计。数值结果表明，该框架在广泛的压力范围内能准确恢复流动动力学和参数，突出了其在致密地层中气体输运建模和反演方面的鲁棒性、准确性和计算效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate modeling of gas flow through porous media is critical for many technological applications, including reservoir performance prediction, carbon capture and sequestration, and fuel cells and batteries. However, such modeling remains challenging due to strong nonlinear behavior and uncertainty in model parameters. In particular, gas slippage effects described by the Klinkenberg model introduce pressure-dependent permeability, which complicates numerical simulation and obscures deviations from classical Darcy flow behavior. To address these challenges, we present an integrated modeling framework for gas transport in porous media that combines a Klinkenberg-enhanced constitutive relation, Hopf-Cole-transformed mixed-form linear governing equations, a shared-trunk neural network architecture, and a Deep Least-Squares (DeepLS) solver. The Hopf-Cole transformation reformulates the original nonlinear flow equations into an equivalent linear system closely related to the Darcy model, while the mixed formulation, together with a shared-trunk neural architecture, enables simultaneous and accurate prediction of both pressure and velocity fields. A rigorous convergence analysis is performed both theoretically and numerically, establishing the stability and convergence properties of the proposed solver. Importantly, the proposed framework also naturally facilitates inverse modeling of pressure-dependent permeability and slippage parameters from limited or indirect observations, enabling efficient estimation of flow properties that are difficult to measure experimentally. Numerical results demonstrate accurate recovery of flow dynamics and parameters across a wide range of pressure regimes, highlighting the framework's robustness, accuracy, and computational efficiency for gas transport modeling and inversion in tight formations.

</details>

---

### 7. [Heavy-Tailed Principle Component Analysis](https://arxiv.org/abs/2603.11308)

**基本信息**

- 🔗 arXiv: [`2603.11308`](https://arxiv.org/abs/2603.11308)
- 👥 作者: Mario Sayde, Christopher Khater, Jihad Fahs 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11308.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对重尾数据的主成分分析，提出了一种稳健的PCA框架。这与化学信息学中构建能够处理复杂、噪声数据（如质谱数据）的化学大模型的核心主题直接相关，因为稳健的特征提取和降维是构建此类模型的基础组件。

**📖 中文摘要**

本文研究了在重尾数据（如多元t分布和亚高斯α稳定律）下的主成分分析（PCA）问题。经典PCA依赖于二阶矩，在存在重尾噪声和脉冲噪声时表现脆弱。论文提出了一个基于对数损失的PCA框架，该框架即使在矩不存在时也定义良好。理论结果表明，在这种损失下，重尾观测的主成分与应用于底层高斯生成器协方差矩阵的标准PCA所获得的主成分一致。基于此，论文提出了直接从重尾数据中稳健估计该协方差矩阵的方法，并在包括背景去噪任务在内的实验中证明，该方法能可靠地恢复主方向，在重尾和脉冲噪声下显著优于经典PCA，在高斯噪声下也保持竞争力。这项工作为处理化学信息学（如质谱数据常具有复杂噪声分布）中的高维、噪声数据提供了稳健的降维和特征提取方法，其核心思想与构建能够处理复杂数据分布的化学大模型相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Principal Component Analysis (PCA) is a cornerstone of dimensionality reduction, yet its classical formulation relies critically on second-order moments and is therefore fragile in the presence of heavy-tailed data and impulsive noise. While numerous robust PCA variants have been proposed, most either assume finite variance, rely on sparsity-driven decompositions, or address robustness through surrogate loss functions without a unified treatment of infinite-variance models. In this paper, we study PCA for high-dimensional data generated according to a superstatistical dependent model of the form $\mathbf{X} = A^{1/2}\mathbf{G}$, where $A$ is a positive random scalar and $\mathbf{G}$ is a Gaussian vector. This framework captures a wide class of heavy-tailed distributions, including multivariate $t$ and sub-Gaussian $\alpha$-stable laws. We formulate PCA under a logarithmic loss, which remains well defined even when moments do not exist. Our main theoretical result shows that, under this loss, the principal components of the heavy-tailed observations coincide with those obtained by applying standard PCA to the covariance matrix of the underlying Gaussian generator. Building on this insight, we propose robust estimators for this covariance matrix directly from heavy-tailed data and compare them with the empirical covariance and Tyler's scatter estimator. Extensive experiments, including background denoising tasks, demonstrate that the proposed approach reliably recovers principal directions and significantly outperforms classical PCA in the presence of heavy-tailed and impulsive noise, while remaining competitive under Gaussian noise.

</details>

---

### 8. [Harnessing Data Asymmetry: Manifold Learning in the Finsler World](https://arxiv.org/abs/2603.11396)

**基本信息**

- 🔗 arXiv: [`2603.11396`](https://arxiv.org/abs/2603.11396)
- 👥 作者: Thomas Dagès, Simon Weber, Daniel Cremers 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11396.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的非对称流形学习框架。这直接关系到化学信息学和质谱分析中构建能够捕捉数据复杂内在结构（如分子空间、光谱空间）的表示学习模型（即化学大模型）这一主题。

**📖 中文摘要**

流形学习旨在通过保持低维嵌入中的成对相异性来捕获高维数据的底层结构。传统方法依赖于对称的黎曼几何，从而强制对称的相异性和嵌入空间（如欧几里得空间）。然而，这实际上丢弃了数据样本非均匀性所固有的有价值的非对称信息。本文提出通过转向芬斯勒几何（一种非对称的黎曼几何推广）来利用这种非对称性，并提出了一个芬斯勒流形学习流程，该流程构建非对称相异性并嵌入到芬斯勒空间中。这极大地扩展了现有非对称嵌入器的适用性，超越了传统的定向数据，适用于任何数据。论文还将当前参考方法（如芬斯勒 t-SNE 和芬斯勒 Umap）推广到非对称情况。在合成和真实数据集上的实验表明，该非对称流程揭示了传统流程中丢失的宝贵信息（如密度层次结构），并 consistently 提供比其欧几里得对应物更高质量的嵌入。这项工作为数据表示学习提供了新的几何视角，对于化学信息学中分子表示、质谱数据特征学习等任务具有潜在价值，是构建更强大化学大模型的基础工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Manifold learning is a fundamental task at the core of data analysis and visualisation. It aims to capture the simple underlying structure of complex high-dimensional data by preserving pairwise dissimilarities in low-dimensional embeddings. Traditional methods rely on symmetric Riemannian geometry, thus forcing symmetric dissimilarities and embedding spaces, e.g. Euclidean. However, this discards in practice valuable asymmetric information inherent to the non-uniformity of data samples. We suggest to harness this asymmetry by switching to Finsler geometry, an asymmetric generalisation of Riemannian geometry, and propose a Finsler manifold learning pipeline that constructs asymmetric dissimilarities and embeds in a Finsler space. This greatly broadens the applicability of existing asymmetric embedders beyond traditionally directed data to any data. We also modernise asymmetric embedders by generalising current reference methods to asymmetry, like Finsler t-SNE and Finsler Umap. On controlled synthetic and large real datasets, we show that our asymmetric pipeline reveals valuable information lost in the traditional pipeline, e.g. density hierarchies, and consistently provides superior quality embeddings than their Euclidean counterparts.

</details>

---

### 9. [MaterialFigBENCH: benchmark dataset with figures for evaluating college-level materials science problem-solving abilities of multimodal large language models](https://arxiv.org/abs/2603.11414)

**基本信息**

- 🔗 arXiv: [`2603.11414`](https://arxiv.org/abs/2603.11414)
- 👥 作者: Michiko Yoshitake, Yuta Suzuki, Ryo Igarashi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11414.pdf)

**💡 相关性分析**

满足标准2和3：论文提供了一个专门用于评估多模态大模型对科学图表理解和推理能力的基准数据集（MaterialFigBench）。这为化学信息学和质谱分析领域训练和评估能够处理光谱图、分子结构图等科学图表的化学大模型提供了重要的数据资源和评估框架（标准2）。同时，论文对当前模型能力的分析和讨论，也构成了对相关主题（多模态科学AI）的重要展望和评估（标准3）。

**📖 中文摘要**

本文提出了MaterialFigBench，一个用于评估多模态大语言模型解决大学级材料科学问题能力的基准数据集，这些问题需要准确解读图表（如相图、应力-应变曲线、阿伦尼乌斯图、衍射图案和微观结构示意图）。该数据集包含137个改编自标准材料科学教科书的自由回答问题，涵盖晶体结构、机械性能、扩散、相图、相变和材料电子性能等广泛主题。为了处理从图像中读取数值时不可避免的模糊性，在适当情况下提供了专家定义的答案范围。论文评估了包括通过OpenAI API访问的ChatGPT和GPT模型在内的几种最先进的多模态LLM，并分析了它们在不同问题类别和模型版本上的性能。结果表明，尽管整体准确性随着模型更新而提高，但当前的LLM在材料科学图表的真实视觉理解和定量解释方面仍然存在困难。在许多情况下，正确答案是通过依赖记忆的领域知识而非通过阅读提供的图像获得的。MaterialFigBench突出了在视觉推理、数值精度和有效数字处理方面的持续弱点，同时也识别了性能有所提高的问题类型。该基准为推进材料科学中的多模态推理能力以及指导未来具有更强基于图表理解能力的LLM开发提供了系统化和特定领域的基础。虽然主题是材料科学，但其核心——评估和提升多模态模型对科学图表（与化学中的光谱图、分子结构图高度相似）的理解和推理能力——与“化学大模型”和“质谱结构推理”（质谱图是一种关键的科学图表）高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MaterialFigBench, a benchmark dataset designed to evaluate the ability of multimodal large language models (LLMs) to solve university-level materials science problems that require accurate interpretation of figures. Unlike existing benchmarks that primarily rely on textual representations, MaterialFigBench focuses on problems in which figures such as phase diagrams, stress-strain curves, Arrhenius plots, diffraction patterns, and microstructural schematics are indispensable for deriving correct answers. The dataset consists of 137 free-response problems adapted from standard materials science textbooks, covering a broad range of topics including crystal structures, mechanical properties, diffusion, phase diagrams, phase transformations, and electronic properties of materials. To address unavoidable ambiguity in reading numerical values from images, expert-defined answer ranges are provided where appropriate. We evaluate several state-of-the-art multimodal LLMs, including ChatGPT and GPT models accessed via OpenAI APIs, and analyze their performance across problem categories and model versions. The results reveal that, although overall accuracy improves with model updates, current LLMs still struggle with genuine visual understanding and quantitative interpretation of materials science figures. In many cases, correct answers are obtained by relying on memorized domain knowledge rather than by reading the provided images. MaterialFigBench highlights persistent weaknesses in visual reasoning, numerical precision, and significant-digit handling, while also identifying problem types where performance has improved. This benchmark provides a systematic and domain-specific foundation for advancing multimodal reasoning capabilities in materials science and for guiding the development of future LLMs with stronger figure-based understanding.

</details>

---

### 10. [ZTab: Domain-based Zero-shot Annotation for Table Columns](https://arxiv.org/abs/2603.11436)

**基本信息**

- 🔗 arXiv: [`2603.11436`](https://arxiv.org/abs/2603.11436)
- 👥 作者: Ehsan Hoseinzade, Ke Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11436.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于关系表语义列类型标注的零样本框架（ZTab），并提供了源代码和数据集。这为化学信息学领域自动化处理和组织化学数据表格（如化合物数据库、质谱参数表）提供了潜在的工具和方法，这些结构化数据是训练化学大模型的重要资源。

**📖 中文摘要**

本研究解决了在关系表中自动检测语义列类型的挑战。零样本建模消除了对用户提供的标记训练数据的需求，使其成为数据收集成本高昂或由于隐私问题而受到限制的场景的理想选择。然而，现有的零样本模型在语义列类型数量很大时性能较差，对表格结构的理解有限，并且由于依赖高性能闭源LLM而带来隐私风险。本文介绍了ZTab，一个基于领域的零样本框架。给定一个由一组预定义语义类型和样本表模式组成的领域配置，ZTab为样本模式生成伪表，并在其上微调一个标注LLM。ZTab是基于领域的零样本，因为它不依赖于用户特定的标记训练数据；因此，对于来自类似领域的测试表，无需重新训练。ZTab的领域配置在零样本程度和标注性能之间提供了权衡：包含所有语义类型的“通用领域”接近“纯粹”零样本，而包含特定应用语义类型的“专用领域”则能在该领域内实现更好的零样本性能。这项工作为关系数据的语义类型标注提供了一种灵活、可配置的零样本解决方案。虽然不直接针对化学数据，但其框架和方法论可以迁移到化学信息学领域，用于自动化标注化学数据库中的表格列（如化合物属性、光谱参数等），为构建化学大模型提供高质量的结构化数据资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study addresses the challenge of automatically detecting semantic column types in relational tables, a key task in many real-world applications. Zero-shot modeling eliminates the need for user-provided labeled training data, making it ideal for scenarios where data collection is costly or restricted due to privacy concerns. However, existing zero-shot models suffer from poor performance when the number of semantic column types is large, limited understanding of tabular structure, and privacy risks arising from dependence on high-performance closed-source LLMs. We introduce ZTab, a domain-based zero-shot framework that addresses both performance and zero-shot requirements. Given a domain configuration consisting of a set of predefined semantic types and sample table schemas, ZTab generates pseudo-tables for the sample schemas and fine-tunes an annotation LLM on them. ZTab is domain-based zero-shot in that it does not depend on user-specific labeled training data; therefore, no retraining is needed for a test table from a similar domain. We describe three cases of domain-based zero-shot. The domain configuration of ZTab provides a trade-off between the extent of zero-shot and annotation performance: a "universal domain" that contains all semantic types approaches "pure" zero-shot, while a "specialized domain" that contains semantic types for a specific application enables better zero-shot performance within that domain. Source code and datasets are available at this https URL

</details>

---

### 11. [Bridging Discrete Marks and Continuous Dynamics: Dual-Path Cross-Interaction for Marked Temporal Point Processes](https://arxiv.org/abs/2603.11462)

**基本信息**

- 🔗 arXiv: [`2603.11462`](https://arxiv.org/abs/2603.11462)
- 👥 作者: Yuxiang Liu, Qiao Liu, Tong Luo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11462.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的标记时间点过程模型（NEXTPP），用于预测带有离散标记的连续时间事件序列。这直接与“质谱结构推理”主题相关，因为质谱数据本质上是一种连续（质荷比）和离散/连续（强度、碎片类型）混合的事件序列，该模型为从数据中推理结构提供了强大的序列建模工具。

**📖 中文摘要**

预测带有离散标记的不规则间隔事件序列具有重大挑战，因为连续时间数据中嵌入了复杂的异步依赖关系。顺序方法捕获事件标记之间的依赖关系但忽略了事件之间的连续演化，而神经常微分方程方法建模平滑动态却未能考虑事件类型如何影响未来动态。为了克服这些限制，本文提出了NEXTPP，一个通过事件粒度神经演化与交叉交互来统一离散和连续表示的双通道框架，用于标记时间点过程。具体来说，NEXTPP通过自注意力机制编码离散事件标记，同时使用神经ODE演化潜在连续时间状态。这些并行流然后通过一个交叉注意力模块融合，以实现连续和离散表示之间显式的双向交互。融合后的表示驱动神经霍克斯过程的条件强度函数，同时采用迭代细化采样器来生成未来事件。在五个真实世界数据集上的广泛评估表明，NEXTPP consistently 优于最先进的模型。该模型框架专门用于建模带有类型标记的连续时间事件序列。这与质谱分析中“质谱结构推理”的核心任务高度相关，因为质谱数据可以视为一系列带有质荷比（连续时间）和强度（可能作为离散标记或连续值）的“事件”。NEXTPP为从时间序列/点过程角度建模和推理质谱数据提供了先进的机器学习方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting irregularly spaced event sequences with discrete marks poses significant challenges due to the complex, asynchronous dependencies embedded within continuous-time data this http URL sequential approaches capture dependencies among event tokens but ignore the continuous evolution between events, while Neural Ordinary Differential Equation (Neural ODE) methods model smooth dynamics yet fail to account for how event types influence future this http URL overcome these limitations, we propose NEXTPP, a dual-channel framework that unifies discrete and continuous representations via Event-granular Neural Evolution with Cross-Interaction for Marked Temporal Point Processes. Specifically, NEXTPP encodes discrete event marks via a self-attention mechanism, simultaneously evolving a latent continuous-time state using a Neural ODE. These parallel streams are then fused through a crossattention module to enable explicit bidirectional interaction between continuous and discrete representations. The fused representations drive the conditional intensity function of the neural Hawkes process, while an iterative thinning sampler is employed to generate future events. Extensive evaluations on five real-world datasets demonstrate that NEXTPP consistently outperforms state-of-the-art models. The source code can be found at this https URL .

</details>

---

### 12. [Leveraging Phytolith Research using Artificial Intelligence](https://arxiv.org/abs/2603.11476)

**基本信息**

- 🔗 arXiv: [`2603.11476`](https://arxiv.org/abs/2603.11476)
- 👥 作者: Andrés G. Mejía Ramón, Kate Dudgeon, Nina Witteveen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11476.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于微观颗粒（植硅体）分析的多模态AI流程和工具，包括2D/3D数据生成、融合模型和贝叶斯建模工具。虽然其直接应用领域是考古学，但其核心方法——结合2D图像和3D点云进行结构推理和分类——与【质谱结构推理】中利用多维数据进行分子结构推断的核心理念高度相关。该工作提供了一个可用于类似结构推理问题的AI工具链范例。

**📖 中文摘要**

本文提出了一种名为Sorometry的端到端人工智能流程，用于高通量数字化、推断和解释植硅体。该工作流程处理Z-stacked光学显微镜扫描，自动生成单个微观颗粒的同步2D正射影像和3D点云。作者开发了一个多模态融合模型，结合了用于2D图像分析的ConvNeXt和用于3D点云分析的PointNet++。该模型在24种诊断形态类型上实现了77.9%的全局分类准确率。此外，该平台还整合了贝叶斯有限混合模型，用于在组合层面预测整体植物来源贡献。这项工作将植硅体研究转变为一个“组学”规模的学科，显著扩展了分析能力，并实现了考古和古生态组合的可重复、群体水平表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phytolith analysis is a crucial tool for reconstructing past vegetation and human activities, but traditional methods are severely limited by labour-intensive, time-consuming manual microscopy. To address this bottleneck, we present Sorometry: a comprehensive end-to-end artificial intelligence pipeline for the high-throughput digitisation, inference, and interpretation of phytoliths. Our workflow processes z-stacked optical microscope scans to automatically generate synchronised 2D orthoimages and 3D point clouds of individual microscopic particles. We developed a multimodal fusion model that combines ConvNeXt for 2D image analysis and PointNet++ for 3D point cloud analysis, supported by a graphical user interface for expert annotation and review. Tested on reference collections and archaeological samples from the Bolivian Amazon, our fusion model achieved a global classification accuracy of 77.9\% across 24 diagnostic morphotypes and 84.5% for segmentation quality. Crucially, the integration of 3D data proved essential for distinguishing complex morphotypes (such as grass silica short cell phytoliths) whose diagnostic features are often obscured by their orientation in 2D projections. Beyond individual object classification, Sorometry incorporates Bayesian finite mixture modelling to predict overall plant source contributions at the assemblage level, successfully identifying specific plants like maize and palms in complex mixed samples. This integrated platform transforms phytolith research into an "omics"-scale discipline, dramatically expanding analytical capacity, standardising expert judgements, and enabling reproducible, population-level characterisations of archaeological and paleoecological assemblages.

</details>

---

### 13. [Leveraging Large Language Models and Survival Analysis for Early Prediction of Chemotherapy Outcomes](https://arxiv.org/abs/2603.11594)

**基本信息**

- 🔗 arXiv: [`2603.11594`](https://arxiv.org/abs/2603.11594)
- 👥 作者: Muhammad Faisal Shahid, Asad Afzal, Abdullah Faiz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11594.pdf)

**💡 相关性分析**

满足标准2：论文展示了利用LLMs从非结构化文本（临床笔记）中提取结构化化学/治疗信息（化疗方案、结果）的方法。这为构建可用于【化学大模型】训练或评估的、高质量的领域特定（肿瘤学/药物）数据集提供了数据资源和技术路径。该方法本身是LLMs在化学医学信息学中的一个应用实例。

**📖 中文摘要**

本研究利用大型语言模型（LLMs）和基于本体的技术，从患者临床笔记中提取表型和治疗结果标签（如癌症进展和毒性），以解决真实世界数据中缺乏明确表型和标签的挑战。研究聚焦于乳腺癌，提取了生命体征、人口统计学、分期、生物标志物、化疗方案等特征。通过生存建模（随机生存森林）预测治疗失败时间，C-index达到73%，并在特定时间点作为分类器预测治疗结果，准确率和F1分数均超过70%。研究强调了基于LLM的临床数据提取在实现治疗结果早期预测方面的潜力，从而支持个性化治疗计划。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemotherapy for cancer treatment is costly and accompanied by severe side effects, highlighting the critical need for early prediction of treatment outcomes to improve patient management and informed decision-making. Predictive models for chemotherapy outcomes using real-world data face challenges, including the absence of explicit phenotypes and treatment outcome labels such as cancer progression and toxicity. This study addresses these challenges by employing Large Language Models (LLMs) and ontology-based techniques for phenotypes and outcome label extraction from patient notes. We focused on one of the most frequently occurring cancers, breast cancer, due to its high prevalence and significant variability in patient response to treatment, making it a critical area for improving predictive modeling. The dataset included features such as vitals, demographics, staging, biomarkers, and performance scales. Drug regimens and their combinations were extracted from the chemotherapy plans in the EMR data and shortlisted based on NCCN guidelines, verified with NIH standards, and analyzed through survival modeling. The proposed approach significantly reduced phenotypes sparsity and improved predictive accuracy. Random Survival Forest was used to predict time-to-failure, achieving a C-index of 73%, and utilized as a classifier at a specific time point to predict treatment outcomes, with accuracy and F1 scores above 70%. The outcome probabilities were validated for reliability by calibration curves. We extended our approach to four other cancer types. This research highlights the potential of early prediction of treatment outcomes using LLM-based clinical data extraction enabling personalized treatment plans with better patient outcomes.

</details>

---

### 14. [Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)

**基本信息**

- 🔗 arXiv: [`2603.11627`](https://arxiv.org/abs/2603.11627)
- 👥 作者: Yichi Zhang, Le Xue, Wenbo Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11627.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了一个大规模、高质量的3D医学影像（PET）数据集，并开发了一个通用的分割基础模型。虽然应用领域是医学影像，但其构建大规模、标注精细的3D体数据数据集的方法，以及开发通用基础模型的思路，对于【化学大模型】或【质谱结构推理】领域构建类似的3D分子结构或质谱成像数据集具有重要的参考价值。该工作提供了数据资源和模型工具。

**📖 中文摘要**

本文开发了用于3D全身正电子发射断层扫描（PET）通用分割的基础模型。作者构建了迄今为止最大、最全面的PET数据集，包含11041个3D全身PET扫描和59831个分割掩码。基于此，提出了SegAnyPET，一个具有通用适用性的创新基础模型，用于多样化的分割任务。该模型基于3D架构，采用提示工程策略进行掩码生成，支持通用且可扩展的器官和病灶分割，支持高效的人工校正，并实现了临床人机交互工作流程。在多中心、多示踪剂、多疾病数据集上的广泛评估表明，SegAnyPET在广泛的分割任务中实现了强大的零样本性能。

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

满足标准1：论文的核心研究内容是使用生成式AI模型（条件潜在扩散）来生成和设计多晶材料结构。这直接属于化学信息学中利用大模型（生成模型）进行材料设计和结构推理的范畴。

**📖 中文摘要**

本文提出PolyCrysDiff，一个基于条件潜在扩散的框架，用于端到端生成可计算的3D多晶材料微观结构。该工作直接面向材料科学中的结构生成问题，属于化学信息学中材料设计的核心范畴。论文的核心是开发一种可控的生成模型，能够根据目标属性（如晶粒尺寸、球形度）生成物理上有效的3D多晶结构，并通过晶体塑性有限元模拟验证其可计算性。这项工作为阐明多晶材料的结构-性能关系提供了关键工具，是数据驱动的材料优化和设计的重要一步。

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

满足标准1：论文的核心研究内容是开发一种新的生成模型（EvoFlows）用于蛋白质序列工程。这直接属于化学信息学/生物信息学中利用大模型（序列生成模型）进行分子（蛋白质）设计和结构推理的范畴。

**📖 中文摘要**

本文介绍了EvoFlows，一种用于蛋白质工程的变长序列到序列建模方法。与自回归或掩码语言模型不同，EvoFlows在模板蛋白质序列上执行有限、可控数量的插入、删除和替换。该方法利用编辑流来学习进化相关蛋白质序列之间的突变轨迹，同时模拟相关天然蛋白质的分布以及连接它们的突变路径。通过广泛的计算机评估，证明EvoFlows能够以与蛋白质工程中常用的领先掩码语言模型相当的质量捕获蛋白质序列分布，同时显示出从给定模板蛋白质生成非平凡但类天然突变体的改进能力。

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

满足标准2：论文提供了一个专门用于探索大气化学相关分子数据集的交互式工具和平台（PhiPlot）。这为化学信息学研究提供了可用于分析分子结构和性质的数据资源和可视化工具。

**📖 中文摘要**

本文介绍了PhiPlot，一个用于大气相关分子数据交互式探索和基于知识的降维的Web环境。该工具集成了可视化、聚类和领域知识引导的嵌入细化功能，旨在帮助发现数据中的模式并支持假设生成。该应用连接到一个不断发展的分子数据库集合，为大气化学中的数据驱动研究提供了一个可访问的界面。

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

满足标准1：论文的核心研究内容是改进知识图谱的补全，这涉及对实体和关系的结构化推理。虽然不直接针对化学分子，但知识图谱补全的方法论（结合嵌入和LLM进行语义验证）与化学信息学中分子知识图谱的构建和推理高度相关，可被视为一种通用的结构推理方法。

**📖 中文摘要**

本文提出了OMNIA，一个用于知识图谱补全的两阶段方法，它结合了结构推理和语义推理。该方法首先通过在知识图谱内部对语义相关的实体和关系进行聚类来生成候选三元组，然后通过轻量级嵌入过滤和基于LLM的语义验证来验证它们。OMNIA专门针对LLM生成的图谱中最常见的隐式语义，并在多个数据集上进行了评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge Graphs (KGs) are widely used to represent structured knowledge, yet their automatic construction, especially with Large Language Models (LLMs), often results in incomplete or noisy outputs. Knowledge Graph Completion (KGC) aims to infer and add missing triples, but most existing methods either rely on structural embeddings that overlook semantics or language models that ignore the graph's structure and depend on external sources. In this work, we present OMNIA, a two-stage approach that bridges structural and semantic reasoning for KGC. It first generates candidate triples by clustering semantically related entities and relations within the KG, then validates them through lightweight embedding filtering followed by LLM-based semantic validation. OMNIA performs on the internal KG, without external sources, and specifically targets implicit semantics that are most frequent in LLM-generated graphs. Extensive experiments on multiple datasets demonstrate that OMNIA significantly improves F1-score compared to traditional embedding-based models. These results highlight OMNIA's effectiveness and efficiency, as its clustering and filtering stages reduce both search space and validation cost while maintaining high-quality completion.

</details>

---

### 19. [Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding](https://arxiv.org/abs/2603.11831)

**基本信息**

- 🔗 arXiv: [`2603.11831`](https://arxiv.org/abs/2603.11831)
- 👥 作者: Jiahao Li, Qingwang Zhang, Qiuyu Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11831.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是使用大语言模型（LLM）驱动程序生成，以实现从文本到CAD模型的生成，这属于生成式大模型在结构设计中的应用。同时，论文构建了一个用于训练和评估的CAD模型数据集，这为相关研究提供了数据资源。

**📖 中文摘要**

本文提出了FutureCAD，一个新颖的文本到CAD框架，利用大语言模型和B-Rep grounding transformer进行高保真CAD生成。该方法生成可执行的CadQuery脚本，并引入一种基于文本的查询机制，使LLM能够通过自然语言指定几何选择，然后由BRepGround将其定位到目标几何图元。为了训练该框架，构建了一个包含真实世界CAD模型的新数据集。实验表明，FutureCAD实现了最先进的CAD生成性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) require explicit selection of B-Rep geometric primitives, and the B-Rep itself is derived from parametric operations. Consequently, this paradigm gap remains a critical factor limiting AI-driven CAD modeling for complex industrial product design. This paper present FutureCAD, a novel text-to-CAD framework that leverages large language models (LLMs) and a B-Rep grounding transformer (BRepGround) for high-fidelity CAD generation. Our method generates executable CadQuery scripts, and introduces a text-based query mechanism that enables the LLM to specify geometric selections via natural language, which BRepGround then grounds to the target primitives. To train our framework, we construct a new dataset comprising real-world CAD models. For the LLM, we apply supervised fine-tuning (SFT) to establish fundamental CAD generation capabilities, followed by reinforcement learning (RL) to improve generalization. Experiments show that FutureCAD achieves state-of-the-art CAD generation performance.

</details>

---

### 20. [A Decade of Generative Adversarial Networks for Porous Material Reconstruction](https://arxiv.org/abs/2603.11836)

**基本信息**

- 🔗 arXiv: [`2603.11836`](https://arxiv.org/abs/2603.11836)
- 👥 作者: Ali Sadeghkhani, Brandon Bennett, Masoud Babaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11836.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于使用生成对抗网络进行多孔材料重建的全面综述。它系统地分类和分析了该领域过去十年的进展、方法和挑战，为化学信息学和材料科学中利用生成模型进行材料结构重建的研究提供了重要的综述和展望。

**📖 中文摘要**

本文系统回顾了2017年至2026年初发表的96篇同行评议文章，分析了生成对抗网络在孔隙材料图像重建方面的演变和应用。综述将GAN架构分为六类，并揭示了在孔隙度精度、渗透率预测和可重建体积方面的显著进展。尽管取得了这些进展，但在计算效率、大规模重建的内存限制以及2D到3D转换中保持结构连续性方面仍然存在持续挑战。这项系统分析为根据特定应用需求选择适当的GAN架构提供了一个全面的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital reconstruction of porous materials has become increasingly critical for applications ranging from geological reservoir characterization to tissue engineering and electrochemical device design. While traditional methods such as micro-computed tomography and statistical reconstruction approaches have established foundations in this field, the emergence of deep learning techniques, particularly Generative Adversarial Networks (GANs), has revolutionized porous media reconstruction capabilities. This review systematically analyzes 96 peer-reviewed articles published from 2017 to early 2026, examining the evolution and applications of GAN-based approaches for porous material image reconstruction. We categorize GAN architectures into six distinct classes, namely Vanilla GANs, Multi-Scale GANs, Conditional GANs, Attention-Enhanced GANs, Style-based GANs, and Hybrid Architecture GANs. Our analysis reveals substantial progress including improvements in porosity accuracy (within 1% of original samples), permeability prediction (up to 79% reduction in mean relative errors), and achievable reconstruction volumes (from initial $64^3$ to current $2{,}200^3$ voxels). Despite these advances, persistent challenges remain in computational efficiency, memory constraints for large-scale reconstruction, and maintaining structural continuity in 2D-to-3D transformations. This systematic analysis provides a comprehensive framework for selecting appropriate GAN architectures based on specific application requirements.

</details>

---

### 21. [Inverse Neural Operator for ODE Parameter Optimization](https://arxiv.org/abs/2603.11854)

**基本信息**

- 🔗 arXiv: [`2603.11854`](https://arxiv.org/abs/2603.11854)
- 👥 作者: Zhi-Song Liu, Wenqing Peng, Helmi Toropainen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11854.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一种新的神经网络框架（INO）用于从观测数据中逆向推断动力学系统的参数。这属于化学信息学和计算化学中常见的逆问题，即从光谱或质谱等观测数据（类比于这里的稀疏轨迹）推理出底层分子结构或反应动力学参数，是一种高级的结构/参数推理方法。

**📖 中文摘要**

本文提出了逆向神经算子，一个用于从稀疏、部分观测中恢复隐藏ODE参数的两阶段框架。第一阶段，一个带有交叉注意力的条件傅里叶神经算子学习一个可微的代理模型，从任意稀疏输入重建完整的ODE轨迹。第二阶段，一个摊销漂移模型在参数空间中学习一个核加权的速度场，将随机参数初始化向真实值传输，而无需通过代理模型反向传播。实验在一个真实世界的刚性大气化学基准和合成基因调控网络上进行。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Inverse Neural Operator (INO), a two-stage framework for recovering hidden ODE parameters from sparse, partial observations. In Stage 1, a Conditional Fourier Neural Operator (C-FNO) with cross-attention learns a differentiable surrogate that reconstructs full ODE trajectories from arbitrary sparse inputs, suppressing high-frequency artifacts via spectral regularization. In Stage 2, an Amortized Drifting Model (ADM) learns a kernel-weighted velocity field in parameter space, transporting random parameter initializations toward the ground truth without backpropagating through the surrogate, avoiding the Jacobian instabilities that afflict gradient-based inversion in stiff regimes. Experiments on a real-world stiff atmospheric chemistry benchmark (POLLU, 25 parameters) and a synthetic Gene Regulatory Network (GRN, 40 parameters) show that INO outperforms gradient-based and amortized baselines in parameter recovery accuracy while requiring only 0.23s inference time, a 487x speedup over iterative gradient descent.

</details>

---

### 22. [AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization](https://arxiv.org/abs/2603.11873)

**基本信息**

- 🔗 arXiv: [`2603.11873`](https://arxiv.org/abs/2603.11873)
- 👥 作者: Qiyang Li, Rui Kong, Yuchen Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11873.pdf)

**💡 相关性分析**

满足标准2：论文提出的AdaFuse框架是一种用于优化动态、稀疏模型组件（如适配器）执行的系统工具和方法论。这种优化大型、动态模型推理效率的通用方法，可为构建和部署高效的“化学大模型”（例如，处理动态分子构象或质谱碎片的模型）提供重要的技术思路和工具参考。

**📖 中文摘要**

本文提出AdaFuse框架，旨在解决将动态稀疏结构（如MoE）与参数高效适配器（如LoRA）集成到大型语言模型（LLMs）时所导致的推理延迟激增问题。该框架通过算法与底层硬件系统的协同设计，实现高效的动态适配器执行。其核心创新包括令牌级预门控策略和定制的CUDA融合内核。虽然论文主要关注LLM的推理优化，但其核心方法——通过算法与系统协同设计来优化动态、稀疏组件的执行——与构建和部署高效“化学大模型”所面临的核心工程挑战（如处理动态、稀疏的分子结构或质谱数据）在方法论上高度相关。该框架可被视为一种用于构建和优化复杂、动态模型系统的通用工具或方法论资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of dynamic, sparse structures like Mixture-of-Experts (MoE) with parameter-efficient adapters (e.g., LoRA) is a powerful technique for enhancing Large Language Models (LLMs). However, this architectural enhancement comes at a steep cost: despite minimal increases in computational load, the inference latency often skyrockets, leading to decoding speeds slowing by over 2.5 times. Through a fine-grained performance analysis, we pinpoint the primary bottleneck not in the computation itself, but in the severe overhead from fragmented, sequential CUDA kernel launches required for conventional dynamic routing. To address this challenge, we introduce AdaFuse, a framework built on a tight co-design between the algorithm and the underlying hardware system to enable efficient dynamic adapter execution. Departing from conventional layer-wise or block-wise routing, AdaFuse employs a token-level pre-gating strategy, which makes a single, global routing decision for all adapter layers before a token is processed. This "decide-once, apply-everywhere" approach effectively staticizes the execution path for each token, creating an opportunity for holistic optimization. We capitalize on this by developing a custom CUDA kernel that performs a fused switching operation, merging the parameters of all selected LoRA adapters into the backbone model in a single, efficient pass. Experimental results on popular open-source LLMs show that AdaFuse achieves accuracy on par with state-of-the-art dynamic adapters while drastically cutting decoding latency by a factor of over 2.4x, thereby bridging the gap between model capability and inference efficiency.

</details>

---

### 23. [Bielik-Minitron-7B: Compressing Large Language Models via Structured Pruning and Knowledge Distillation for the Polish Language](https://arxiv.org/abs/2603.11881)

**基本信息**

- 🔗 arXiv: [`2603.11881`](https://arxiv.org/abs/2603.11881)
- 👥 作者: Remigiusz Kinas, Paweł Kiszczak, Sergio P. Perez 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11881.pdf)

**💡 相关性分析**

满足标准2：论文详细描述了一种用于创建高效、压缩版大型语言模型的方法论和工具链（结构化剪枝、知识蒸馏）。这种方法论对于构建和优化领域专用的“化学大模型”（需要在高计算成本下保持性能）具有直接的参考价值，提供了可用的技术资源和实践案例。

**📖 中文摘要**

本报告详细介绍了Bielik-Minitron-7B模型的创建过程，这是一个通过结构化混合剪枝和知识蒸馏压缩得到的7.35B参数模型，专门针对欧洲语言进行了优化。该工作展示了一种高效的两阶段压缩方法学，能够在减少模型参数和提升推理速度的同时，尽可能保留原始大语言模型的性能。虽然该模型针对自然语言任务，但其采用的“结构化剪枝+知识蒸馏”的模型压缩与优化流程，是构建领域专用大模型（如“化学大模型”）的关键技术路径之一。论文提供了具体的压缩方法、工具链（NVIDIA Model Optimizer, NeMo Framework）和评估结果，可作为构建轻量化、高效领域大模型的有价值参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This report details the creation of Bielik-Minitron-7B, a compressed 7.35B parameter version of the Bielik-11B-v3.0 model, specifically optimized for European languages. By leveraging a two-stage compression methodology inspired by the NVIDIA Minitron approach, we combined structured hybrid pruning and knowledge distillation to reduce the model's parameter count by 33.4%, from 11.04B to 7.35B. We utilized the NVIDIA Model Optimizer for structural pruning and the NVIDIA NeMo Framework for logit-based distillation for quality recovery. Following distillation, the model underwent a rigorous alignment pipeline consisting of Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO-P), and Reinforcement Learning (GRPO). Our final model successfully recovered approximately 90% of the baseline model's performance while providing up to 50% inference speedup. This approach demonstrates an efficient pathway to create language models for less-represented languages, preserving the original model quality while reducing inference deployment costs.

</details>

---

### 24. [Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding](https://arxiv.org/abs/2603.11924)

**基本信息**

- 🔗 arXiv: [`2603.11924`](https://arxiv.org/abs/2603.11924)
- 👥 作者: Xinyu Li, Zhen Zhang, Qi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11924.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容直接围绕“化学大模型”（Chem4DLLM）和“结构推理”（将4D分子轨迹推理为自然语言解释）展开。同时，它提供了专门用于此任务的数据集Chem4DBench和模型架构，是直接相关的数据资源和模型方法。

**📖 中文摘要**

本文针对现有化学理解任务主要依赖静态分子表示的局限性，引入了化学动力学理解（ChemDU）这一新任务，旨在将4D分子轨迹转化为可解释的自然语言描述。为此，作者构建了首个配对4D分子轨迹与专家解释的数据集Chem4DBench，并提出了统一模型Chem4DLLM。该模型将等变图编码器与预训练大语言模型相结合，显式捕获分子几何和旋转动力学。这项工作直接位于“化学大模型”与“（分子）结构推理”的交叉点：它旨在开发能够理解和推理动态分子结构（而不仅仅是静态结构）的多模态大语言模型。论文提出的任务、基准数据集和模型架构，为开发下一代能够处理时间序列结构数据的化学AI系统指明了方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability, we construct Chem4DBench, the first dataset pairing 4D molecular trajectories with expert-authored explanations across these settings. We further propose Chem4DLLM, a unified model that integrates an equivariant graph encoder with a pretrained large language model to explicitly capture molecular geometry and rotational dynamics. We hope that ChemDU, together with Chem4DBench and Chem4DLLM, will stimulate further research in dynamic chemical understanding and multimodal scientific reasoning.

</details>

---

### 25. [Learning Transferable Sensor Models via Language-Informed Pretraining](https://arxiv.org/abs/2603.11950)

**基本信息**

- 🔗 arXiv: [`2603.11950`](https://arxiv.org/abs/2603.11950)
- 👥 作者: Yuliang Chen, Arvind Pillai, Yu Yvonne Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11950.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于学习传感器数据语言对齐表征的通用框架SLIP。该框架的方法论（多模态预训练、语言对齐、序列建模）和开源实现，为构建能够理解和推理复杂科学仪器数据（如质谱）的“化学大模型”提供了重要的工具、架构思路和可复用的技术方案。

**📖 中文摘要**

本文介绍了SLIP（传感器语言信息预训练），一个用于学习跨不同传感器设置泛化的语言对齐表征的开源框架。SLIP整合了对比对齐与传感器条件描述生成，支持不同的时间分辨率和可变长度输入。论文在11个数据集上展示了SLIP在零样本迁移、信号描述和问答方面的优越性能。虽然主要面向通用传感器数据，但SLIP框架的核心思想——通过语言对齐的预训练让模型理解并推理复杂的、多模态的、序列化的数据——与“化学大模型”和“质谱结构推理”的目标高度契合。质谱数据本质上是复杂的、序列化的传感器信号，其结构推理需要模型具备强大的信号理解和语言推理能力。SLIP提供的方法论和框架可作为构建能够理解质谱信号的“化学大模型”的宝贵起点。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern sensing systems generate large volumes of unlabeled multivariate time-series data. This abundance of unlabeled data makes self-supervised learning (SSL) a natural approach for learning transferable representations. However, most existing approaches are optimized for reconstruction or forecasting objectives and often fail to capture the semantic structure required for downstream classification and reasoning tasks. While recent sensor-language alignment methods improve semantic generalization through captioning and zero-shot transfer, they are limited to fixed sensor configurations, such as predefined channel sets, signal lengths, or temporal resolutions, which hinders cross-domain applicability. To address these gaps, we introduce \textbf{SLIP} (\textbf{S}ensor \textbf{L}anguage-\textbf{I}nformed \textbf{P}retraining), an open-source framework for learning language-aligned representations that generalize across diverse sensor setups. SLIP integrates contrastive alignment with sensor-conditioned captioning, facilitating both discriminative understanding and generative reasoning. By repurposing a pretrained decoder-only language model via cross-attention and introducing an elegant, flexible patch-embedder, SLIP supports different temporal resolutions and variable-length input at inference time without additional retraining. Across 11 datasets, SLIP demonstrates superior performance in zero-shot transfer, signal captioning, and question answering. It achieves a 77.14% average linear-probing accuracy, a 5.93% relative improvement over strong baselines, and reaches 64.83% accuracy in sensor-based question answering.

</details>

---

### 26. [Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era](https://arxiv.org/abs/2603.12016)

**基本信息**

- 🔗 arXiv: [`2603.12016`](https://arxiv.org/abs/2603.12016)
- 👥 作者: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12016.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个高性能、可扩展的开源图像特征提取库Nyxus。该工具库能够处理2D/3D科学图像数据并提取大量定量特征，可直接应用于化学信息学领域，例如从质谱成像数据中提取特征用于后续的“质谱结构推理”或化学大模型训练，是一个有价值的数据处理工具和资源。

**📖 中文摘要**

本文介绍了Nyxus，一个为大数据和AI时代设计的下一代图像特征提取库。Nyxus针对2D和3D图像数据进行了可扩展的核外特征提取优化，并进行了严格的测试。其全面的特征集覆盖了包括放射组学和细胞分析在内的多个生物医学领域，并针对CPU和GPU进行了计算可扩展性设计。虽然Nyxus主要面向生物医学图像分析，但其核心功能——从复杂的科学图像数据中高效、可扩展地提取大量定量特征——与化学信息学中从分子图像、光谱图或微观结构图像中提取特征的任务高度相关。特别是，在质谱成像（MSI）或其它光谱成像技术中，需要从高维数据中提取特征以进行后续的结构或性质推理。Nyxus作为一个高性能、开源的特征提取工具库，可直接作为化学信息学和质谱分析领域的数据处理与特征工程资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of extracted features. To address these needs, we developed a novel feature extraction library called Nyxus. Nyxus is designed from the ground up for scalable out-of-core feature extraction for 2D and 3D image data and rigorously tested against established standards. The comprehensive feature set of Nyxus covers multiple biomedical domains including radiomics and cellular analysis, and is designed for computational scalability across CPUs and GPUs. Nyxus has been packaged to be accessible to users of various skill sets and needs: as a Python package for code developers, a command line tool, as a Napari plugin for low to no-code users or users that want to visualize results, and as an Open Container Initiative (OCI) compliant container that can be used in cloud or super-computing workflows aimed at processing large data sets. Further, Nyxus enables a new methodological approach to feature extraction allowing for programmatic tuning of many features sets for optimal computational efficiency or coverage for use in novel machine learning and deep learning applications.

</details>

---

### 27. [Chemical Reaction Networks Learn Better than Spiking Neural Networks](https://arxiv.org/abs/2603.12060)

**基本信息**

- 🔗 arXiv: [`2603.12060`](https://arxiv.org/abs/2603.12060)
- 👥 作者: Sophie Jaffard, Ivo F. Sbalzarini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12060.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种新型的、基于化学反应网络的机器学习模型展开。这直接关联到“化学大模型”的一个前沿探索方向：即利用化学系统本身作为计算介质来实现智能。论文从理论和实验上论证了这种化学模型的可行性和潜力，属于该主题的前沿性、基础性研究。

**📖 中文摘要**

本文从数学上证明了，在确定性质量作用动力学公式下，没有隐藏层的化学反应网络（CRNs）可以解决某些需要尖峰神经网络（SNNs）具备隐藏层才能完成的任务。作者提供了一个具体的CRN网络，并分析了其学习能力、渐近行为和VC维。数值实验进一步证实了该CRN在分类手写数字像素图像任务上的学习能力，并显示其比带隐藏层的SNN更准确、更高效。这项研究为“化学计算”中的机器学习提供了动机，并从数学上解释了生化反应网络如何可能表现出比神经元网络更高效的学习行为。这与“化学大模型”的愿景——探索超越传统硅基计算范式的、基于化学或分子系统的智能模型——在理念上高度相关，为构建新型计算范式下的智能系统提供了理论基础和实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We mathematically prove that chemical reaction networks without hidden layers can solve tasks for which spiking neural networks require hidden layers. Our proof uses the deterministic mass-action kinetics formulation of chemical reaction networks. Specifically, we prove that a certain reaction network without hidden layers can learn a classification task previously proved to be achievable by a spiking neural network with hidden layers. We provide analytical regret bounds for the global behavior of the network and analyze its asymptotic behavior and Vapnik-Chervonenkis dimension. In a numerical experiment, we confirm the learning capacity of the proposed chemical reaction network for classifying handwritten digits in pixel images, and we show that it solves the task more accurately and efficiently than a spiking neural network with hidden layers. This provides a motivation for machine learning in chemical computers and a mathematical explanation for how biological cells might exhibit more efficient learning behavior within biochemical reaction networks than neuronal networks.

</details>

---

### 28. [Paper Title: LoV3D: Grounding Cognitive Prognosis Reasoning in Longitudinal 3D Brain MRI via Regional Volume Assessments](https://arxiv.org/abs/2603.12071)

**基本信息**

- 🔗 arXiv: [`2603.12071`](https://arxiv.org/abs/2603.12071)
- 👥 作者: Zhaoyang Jiang, Zhizhong Fu, David McAllister 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12071.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于3D科学图像理解和诊断的、具有事实 grounding 机制的多模态大模型框架（LoV3D）。该框架的方法论（分步推理、基于领域知识的验证器、DPO训练策略）为构建用于“质谱结构推理”或其它化学数据解释的、可靠且可解释的“化学大模型”提供了重要的架构设计思路和技术方案参考。

**📖 中文摘要**

本文提出了LoV3D，一个用于训练3D视觉-语言模型的流程，用于处理纵向脑部MRI数据。该流程读取图像后，生成区域级解剖学评估，与先前扫描进行纵向比较，最终输出诊断类别和综合诊断摘要。其分步流程通过强制标签一致性、纵向连贯性和生物学合理性来支撑最终诊断，从而减少幻觉风险。训练过程引入了一个临床加权的验证器，基于标准化的体积指标来自动评分候选输出，驱动无需人工标注的直接偏好优化。虽然应用领域是神经医学，但LoV3D的核心贡献在于提出了一种用于3D科学图像（MRI）的、具有强推理链条和事实 grounding 机制的多模态大模型框架。这种方法论——将领域知识（体积指标）融入模型训练与验证，以产生可靠、可解释的推理——对于构建用于“质谱结构推理”或其它科学数据解释的“化学大模型”具有极高的参考价值。它展示了如何让大模型在复杂科学领域进行可靠、基于证据的推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Longitudinal brain MRI is essential for characterizing the progression of neurological diseases such as Alzheimer's disease assessment. However, current deep-learning tools fragment this process: classifiers reduce a scan to a label, volumetric pipelines produce uninterpreted measurements, and vision-language models (VLMs) may generate fluent but potentially hallucinated conclusions. We present LoV3D, a pipeline for training 3D vision-language models, which reads longitudinal T1-weighted brain MRI, produces a region-level anatomical assessment, conducts longitudinal comparison with the prior scan, and finally outputs a three-class diagnosis (Cognitively Normal, Mild Cognitive Impairment, or Dementia) along with a synthesized diagnostic summary. The stepped pipeline grounds the final diagnosis by enforcing label consistency, longitudinal coherence, and biological plausibility, thereby reducing the risks of hallucinations. The training process introduces a clinically-weighted Verifier that scores candidate outputs automatically against normative references derived from standardized volume metrics, driving Direct Preference Optimization without a single human annotation. On a subject-level held-out ADNI test set (479 scans, 258 subjects), LoV3D achieves 93.7% three-class diagnostic accuracy (+34.8% over the no-grounding baseline), 97.2% on two-class diagnosis accuracy (+4% over the SOTA) and 82.6% region-level anatomical classification accuracy (+33.1% over VLM baselines). Zero-shot transfer yields 95.4% on MIRIAD (100% Dementia recall) and 82.9% three-class accuracy on AIBL, confirming high generalizability across sites, scanners, and populations. Code is available at this https URL .

</details>

---

### 29. [A Multi-Label Temporal Convolutional Framework for Transcription Factor Binding Characterization](https://arxiv.org/abs/2603.12073)

**基本信息**

- 🔗 arXiv: [`2603.12073`](https://arxiv.org/abs/2603.12073)
- 👥 作者: Pietro Demurtas, Ferdinando Zanchetta, Giovanni Perini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12073.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于时序卷积网络（TCN）处理生物序列数据并进行多标签预测的深度学习方法。这种方法论可用于处理类似序列数据的质谱，进行多标签的结构片段或官能团推理，为“质谱结构推理”任务提供了可借鉴的模型架构和算法思路。

**📖 中文摘要**

本文研究了DNA转录因子结合位点识别这一多标签分类问题。作者提出了基于时序卷积网络（TCN）的深度学习模型，能够预测多个TF的结合谱，捕获TF之间的相关性及其协同调控机制。结果表明，多标签学习可以揭示具有生物学意义的 motif 和与已知TF相互作用一致的共结合模式。虽然研究领域是生物信息学，但其核心技术——使用深度学习模型（TCN）对生物分子序列数据进行多标签分类和模式挖掘，以推断复杂的结构-功能关系——与化学信息学中的许多任务在方法论上同源。例如，在“质谱结构推理”中，可能需要从质谱数据中同时推断出多种子结构或官能团的存在（多标签问题）。论文采用的TCN模型及其在多标签序列学习上的应用，可为处理质谱序列数据、进行多标签结构推理提供模型架构和算法思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transcription factors (TFs) regulate gene expression through complex and co-operative mechanisms. While many TFs act together, the logic underlying TFs binding and their interactions is not fully understood yet. Most current approaches for TF binding site prediction focus on individual TFs and binary classification tasks, without a full analysis of the possible interactions among various TFs. In this paper we investigate DNA TF binding site recognition as a multi-label classification problem, achieving reliable predictions for multiple TFs on DNA sequences retrieved in public repositories. Our deep learning models are based on Temporal Convolutional Networks (TCNs), which are able to predict multiple TF binding profiles, capturing correlations among TFs andtheir cooperative regulatory mechanisms. Our results suggest that multi-label learning leading to reliable predictive performances can reveal biologically meaningful motifs and co-binding patterns consistent with known TF interactions, while also suggesting novel relationships and cooperation among TFs.

</details>

---

### 30. [ChemSICal-Net: Timing-Controlled Chemical Reaction Network for Successive Interference Cancellation in Molecular Multiple Access](https://arxiv.org/abs/2603.12141)

**基本信息**

- 🔗 arXiv: [`2603.12141`](https://arxiv.org/abs/2603.12141)
- 👥 作者: Alexander Wietfeld, Oguz Turgut, Eneritz Somoza Rodríguez 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12141.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计和模拟一个名为ChemSICal-Net的“化学反应网络”（CRN），用于在分子通信中实现信号处理算法（连续干扰消除）。虽然应用背景是通信，但论文的核心是构建和优化一个复杂的、用于信息处理的化学系统模型。这直接属于“化学大模型”的广义范畴——即用于模拟和推理复杂化学系统（此处是反应网络）的计算模型。同时，论文中使用的贝叶斯优化（BO）和随机模拟也属于化学信息学中用于模型参数化和分析的高级计算方法。

**📖 中文摘要**

本文提出了ChemSICal-Net，一个用于分子通信（MC）网络中实现连续干扰消除（SIC）的化学接收器的综合化学反应网络（CRN）仿真模型。作者将SIC算法结构以基本化学构建块的形式呈现，并通过化学振荡器结合了时钟定时控制。论文提出了一种基于高斯过程代理的自适应贝叶斯优化（BO）方案，用于寻找合适的反应速率常数和初始浓度，并表明其在公平计算成本度量下优于相关工作中的基线方法。随后，在一系列时钟速度和不同配置下，对ChemSICal-Net框架的性能进行了随机评估，重点关注检测精度和决策时间等通信系统指标。结果表明，通过化学时钟进行定时可以将较短决策时间场景下的检测精度提高2倍，这突显了决策时间与检测概率之间的权衡如何影响CRN设计选择。BO方案被证明能够可靠地优化不同配置的参数，相比未优化情况提升约一个数量级。该系统揭示了结合外部BO和分子反应动力学随机模拟的多尺度方法对于以通信指标为中心的系统设计的必要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MC networks are envisioned to enable synthetic information exchange between nanoscale biological entities. For many algorithm proposals in the MC research field, the question of implementation at nanoscales and in biological environments remains open. Chemical reaction networks (CRNs) provide a natural framework to model computing processes in biological systems, while detailed simulations capture realistic stochastic effects. In this work, we present ChemSICal-Net, a comprehensive CRN simulation model of a chemical receiver implementing successive interference cancellation (SIC) to differentiate messages from multiple transmitters. We present the structure of the SIC algorithm in the form of basic chemical building blocks and incorporate clocked timing control by a chemical oscillator. We propose an adaptive Bayesian optimization (BO) scheme with a Gaussian process surrogate to find appropriate values for the reaction rate constants and the initial concentrations and show that it outperforms baseline methods from related work based on a fair computational cost metric. Then, the performance of the ChemSICal-Net framework is evaluated stochastically across a range of clock speeds and in different configurations focusing on communication system metrics such as detection accuracy and decision time. Our results highlight that the timing via a chemical clock can improve the detection accuracy by a factor of 2 in scenarios with shorter decision times, which underlines how the trade-off between decision time and detection probability can shape CRN design choices. The BO scheme is shown to reliably optimize parameters for different configurations by approximately one order of magnitude compared to the non-optimized case. Our system reveals the need for a multi-scale approach with external BO and stochastic simulation of molecular reaction dynamics for communication-metric-focused system design.

</details>

---

### 31. [Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction](https://arxiv.org/abs/2603.11061)

**基本信息**

- 🔗 arXiv: [`2603.11061`](https://arxiv.org/abs/2603.11061)
- 👥 作者: Van Le, Tan Le
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11061.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于蛋白质残基pKa预测的混合量子-经典机器学习模型。虽然pKa预测本身是生物物理化学问题，但论文的核心方法论是构建和评估一个“深度量子神经网络”（DQNN），并利用“量子启发特征映射”来增强分子表示。这直接属于“化学大模型”的范畴，即开发用于化学/生物分子性质预测的新型、复杂的机器学习模型。

**📖 中文摘要**

本文提出了一种用于准确预测残基水平pKa值的混合量子-经典框架。该框架通过高斯核基的量子启发特征映射来丰富残基水平的表示，这些量子增强的描述符与归一化的结构特征相结合，形成统一的混合编码，并由深度量子神经网络（DQNN）进行处理。该架构能够捕捉残基微环境中经典模型无法访问的非线性关系。在多个精选描述符集上的基准测试表明，相对于经典基线模型，DQNN在跨上下文泛化方面取得了改进。在PKAD-R实验基准和Aβ40案例研究上的外部评估进一步凸显了量子启发表示的鲁棒性和可迁移性。这项工作通过将量子启发特征变换与经典生化描述符相结合，为残基水平pKa预测及蛋白质静电学的更广泛应用建立了一种可扩展且具有实验可迁移性的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue microenvironments that are not accessible to classical models. Benchmarking across multiple curated descriptor sets demonstrates that the DQNN achieves improved cross-context generalization relative to classical baselines. External evaluation on the PKAD-R experimental benchmark and an A$\beta$40 case study further highlights the robustness and transferability of the quantum-inspired representation. By integrating quantum-inspired feature transformations with classical biochemical descriptors, this work establishes a scalable and experimentally transferable approach for residue-level pKa prediction and broader applications in protein electrostatics.

</details>

---

### 32. [Exploring Collatz Dynamics with Human-LLM Collaboration](https://arxiv.org/abs/2603.11066)

**基本信息**

- 🔗 arXiv: [`2603.11066`](https://arxiv.org/abs/2603.11066)
- 👥 作者: Edward Y. Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11066.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索Collatz猜想的动力学，并明确采用了“人类-LLM协作”作为研究方法论。虽然研究主题是数论，但论文的重点在于描述和论证如何利用LLM作为协作工具来辅助数学发现、提出猜想和进行证明。这直接涉及“化学大模型”的广义范畴——即大模型（此处为LLM）在科学研究（包括数学和理论化学信息学）中的创新应用模式。

**📖 中文摘要**

本文通过人类与大型语言模型（LLM）协作的方式，研究了Collatz迭代的结构特性。论文观察了大规模计算探索中出现的两种现象：剩余类的模运算扰乱以及轨迹的爆发-间隙分解。研究证明了若干结构结果，包括一个模扰乱引理（表明间隙返回映射在高位上充当精确双射）、一个持久退出引理（描述持久状态后的间隙结构）以及间隙返回动力学下已知二进制表示部分的衰减性质。此外，论文还在模模型中证明了间隙长度和2进赋值遵循几何分布，而持久运行长度是几何分布的，其预期爆发长度E[B]=2；这些共同预测了严格的轨道收缩。这些结果表明了一个条件框架，在该框架下，收敛性将取决于关于爆发和间隙长度的适当轨道假设，而这些假设又由一个轨道均匀分布猜想所暗示。论文还记录了通过这些观察发展起来的人与LLM协作过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate structural properties of the Collatz iteration through two phenomena observed in large computational exploration: modular scrambling of residue classes and a burst--gap decomposition of trajectories. We prove several structural results, including a modular scrambling lemma showing that the gap-return map acts as an exact bijection on high bits, a persistent exit lemma characterizing gap structure after persistent states, and a decay property for known portions of binary representations under gap-return dynamics. We further prove that, in the modular model, gap lengths and $2$-adic valuations follow geometric distributions, while persistent run lengths are geometric with expected burst length $E[B]=2$; together these predict strict orbit contraction. These results suggest a conditional framework in which convergence would follow from suitable orbitwise hypotheses on burst and gap lengths, which in turn are suggested by an orbit equidistribution conjecture. However, the key hypotheses remain open, and the framework is exploratory rather than a complete reduction. The paper also documents the human-LLM collaboration through which these observations were developed.

</details>

---

### 33. [From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery](https://arxiv.org/abs/2603.11068)

**基本信息**

- 🔗 arXiv: [`2603.11068`](https://arxiv.org/abs/2603.11068)
- 👥 作者: Iman Peivaste, Salim Belouettar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大型语言模型（LLM）的ReAct智能体，用于高通量熵合金（HEA）的成分逆向设计。这直接属于“化学大模型”的应用范畴，即利用先进的大模型（此处是具备推理和行动能力的LLM智能体）来驱动和加速材料发现这一化学信息学核心任务。

**📖 中文摘要**

本文提出了一种ReAct（推理+行动）大型语言模型（LLM）智能体框架，用于高通量熵合金（HEA）的逆向设计。该智能体能够自主提出、验证并迭代优化HEA成分，其方法是查询一个基于4,753个实验记录（涵盖FCC、BCC、BCC+FCC、BCC+IM四种相）训练并校准的XGBoost代理模型（准确率达94.66%）。与贝叶斯优化和随机搜索基线相比，配备完整提示的智能体在描述符空间中对于FCC、BCC和BCC+FCC相的重新发现率分别达到38%、18%和38%，且其提出的成分与实验相流形的距离比随机搜索近2.4至22.8倍。消融实验表明，领域先验知识使智能体从回忆文献中的标志性合金转向探索成分多样性的空间。这项工作确立了LLM引导的智能体推理作为逆向合金设计的一种原则性、透明且对流形感知的补充方法，是对无梯度优化的重要补充。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering high-entropy alloy (HEA) compositions that reliably form a target crystal phase is a high-dimensional inverse design problem that conventional trial-and-error experimentation and forward-only machine learning models cannot efficiently solve. Here we present a ReAct (Reasoning + Acting) LLM agent that autonomously proposes, validates, and iteratively refines HEA compositions by querying a calibrated XGBoost surrogate trained on 4,753 experimental records across four phases (FCC, BCC, BCC+FCC, BCC+IM), achieving 94.66\% accuracy (F1 macro = 0.896). Against Bayesian optimisation (BO) and random search baselines, the full-prompt agent achieves descriptor-space rediscovery rates of 38\%, 18\%, and 38\% for FCC, BCC, and BCC+FCC (Mann--Whitney $p \leq 0.039$), with proposals lying 2.4--22.8$\times$ closer to the experimental phase manifold than random search. An ablation reveals that domain priors shift the agent from landmark-alloy recall toward compositionally diverse exploration -- an uninformed agent scores higher rediscovery by concentrating on literature-dense families, while the full-prompt agent explores underrepresented space (unique ratio 1.0 vs.\ 0.39 for BCC+FCC). These regimes represent distinct criteria: proximity to known literature versus genuine discovery. Spearman analysis confirms agent reasoning is statistically aligned with empirical phase distributions ($\rho = 0.736$, $p = 0.004$ for BCC). This work establishes LLM-guided agentic reasoning as a principled, transparent, and manifold-aware complement to gradient-free optimisation for inverse alloy design.

</details>

---

### 34. [Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction](https://arxiv.org/abs/2603.11125)

**基本信息**

- 🔗 arXiv: [`2603.11125`](https://arxiv.org/abs/2603.11125)
- 👥 作者: Yining Qian, Pengjie Wang, Yixiao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种名为Co-Diffusion的新型深度学习框架，用于药物-靶标亲和力（DTA）预测。该框架基于扩散模型（一种生成式大模型）的思想，将其重新用于分子-蛋白质相互作用的判别性预测任务。这直接属于“化学大模型”的范畴，即开发用于化学信息学中关键预测任务（DTA）的先进生成式/扩散模型架构。

**📖 中文摘要**

本文提出了Co-Diffusion，一种新颖的亲和力感知框架，将药物-靶标亲和力（DTA）预测重新定义为约束潜在去噪过程以增强泛化能力。Co-Diffusion采用两阶段范式：第一阶段在显式监督目标下对齐药物和靶标嵌入，建立亲和力引导的潜在流形，确保潜在空间反映内在的结合景观。第二阶段引入模态特定的潜在扩散作为随机扰动-去噪正则化器，迫使模型从噪声结构表示中恢复一致的亲和力语义。该方法有效缓解了生成式DTA模型中常见的重建-回归冲突。理论分析表明，Co-Diffusion最大化了药物结构、蛋白质序列和结合强度的联合似然的变分下界。跨多个基准的大量实验证明，Co-Diffusion显著优于最先进的基线模型，特别是在未见过的分子支架和新蛋白质家族上表现出卓越的零样本泛化能力，为在未探索化学空间中进行计算机药物优先排序开辟了稳健的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.

</details>

---

### 35. [Learning to Unscramble: Simplifying Symbolic Expressions via Self-Supervised Oracle Trajectories](https://arxiv.org/abs/2603.11164)

**基本信息**

- 🔗 arXiv: [`2603.11164`](https://arxiv.org/abs/2603.11164)
- 👥 作者: David Shih
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11164.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用自监督学习和Transformer模型进行复杂符号表达式的简化与推理。虽然应用领域是高能物理，但其核心方法（符号推理、自监督学习、Transformer架构）与“化学大模型”中处理分子结构、反应路径和性质预测等复杂符号推理任务高度相关，可视为一种通用的符号推理模型。

**📖 中文摘要**

本文提出了一种新的自监督机器学习方法，用于简化复杂的数学表达式。该方法通过扰乱简单表达式并记录逆操作来生成训练数据，创建了提供目标状态和明确路径的“预言轨迹”。然后，一个基于Transformer的置换等变策略网络被训练来逐步预测给定输入表达式的预言动作。作者在两个高能物理问题（双对数归约和旋量-螺旋度散射振幅简化）上展示了该方法。在这两种情况下，训练后的策略网络在广泛的难度级别上实现了接近完美的求解率，显著优于基于强化学习和端到端回归的先前方法。该方法的核心——使用自监督学习简化复杂符号表达式——与“化学大模型”中处理复杂分子表示和推理的任务在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a new self-supervised machine learning approach for symbolic simplification of complex mathematical expressions. Training data is generated by scrambling simple expressions and recording the inverse operations, creating oracle trajectories that provide both goal states and explicit paths to reach them. A permutation-equivariant, transformer-based policy network is then trained on this data step-wise to predict the oracle action given the input expression. We demonstrate this approach on two problems in high-energy physics: dilogarithm reduction and spinor-helicity scattering amplitude simplification. In both cases, our trained policy network achieves near perfect solve rates across a wide range of difficulty levels, substantially outperforming prior approaches based on reinforcement learning and end-to-end regression. When combined with contrastive grouping and beam search, our model achieves a 100\% full simplification rate on a representative selection of 5-point gluon tree-level amplitudes in Yang-Mills theory, including expressions with over 200 initial terms.

</details>

---

### 36. [A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation](https://arxiv.org/abs/2603.11242)

**基本信息**

- 🔗 arXiv: [`2603.11242`](https://arxiv.org/abs/2603.11242)
- 👥 作者: Xiaoan Lang, Fang Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11242.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个通用的解纠缠VAE框架和一套评估工具。这些工具和方法（bfVAE, FVH-LT, DBSR-LS, LSDI）可以作为一种数据表示和特征学习资源，应用于“化学大模型”或“质谱结构推理”任务中，用于学习分子或质谱数据的低维、可解释的潜在表示，从而辅助下游的推理和预测任务。

**📖 中文摘要**

本文提出了一个通用的变分自编码器（VAE）解纠缠框架（bfVAE），并引入了两种无需真实生成因子知识的解纠缠效果评估程序（FVH-LT和DBSR-LS）以及一个总体解纠缠指数（LSDI）。该框架旨在为各种数据类型（尤其是表格数据）生成有效的潜在空间解纠缠表示。作者通过大量实验验证了bfVAE框架以及评估工具的有效性。bfVAE在解纠缠质量、鲁棒性和信息性潜在维度的低错误发现率方面超越了现有的解纠缠VAE框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FVH-LT and DBSR-LS to summarize the overall effectiveness of a VAE disentanglement method without requiring access to or knowledge of the ground-truth generative factors. To the best of our knowledge, these are the first assessment tools to achieve this. FVH-LT and DBSR-LS also enhance latent space interpretability and provide guidance on more efficient content generation. To ensure robust and consistent disentanglement, we develop a greedy alignment strategy (GAS) that mitigates label switching and aligns latent dimensions across runs to obtain aggregated results. We assess the bfVAE framework and validate FVH-LT, DBSR-LS, and LSDI in extensive experiments on tabular and image data. The results suggest that bfVAE surpasses existing disentangled VAE frameworks in terms of disentanglement quality, robustness, achieving a near-zero false discovery rate for informative latent dimensions, that FVH-LT and DBSR-LS reliably uncover semantically meaningful and domain-relevant latent structures, and that LSDI makes an effective overall quantitative summary on disentanglement effectiveness.

</details>

---

### 37. [A Standardized Framework For Evaluating Gene Expression Generative Models](https://arxiv.org/abs/2603.11244)

**基本信息**

- 🔗 arXiv: [`2603.11244`](https://arxiv.org/abs/2603.11244)
- 👥 作者: Andrea Rubbi, Andrea Giuseppe Di Francesco, Mohammad Lotfollahi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11244.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于评估生成模型的标准化框架（GGE）。虽然应用于基因表达数据，但其核心思想——为生成模型提供一套标准化、可复现的评估指标和流程——可以直接迁移或启发“化学大模型”领域（如分子生成模型）的评估工作。它为相关研究提供了重要的工具和评估方法资源。

**📖 中文摘要**

本文提出了Generated Genetic Expression Evaluator (GGE)，一个用于标准化评估单细胞基因表达数据生成模型的开源Python框架。GGE提供了一套全面的分布度量，并包含通过差异表达基因（DEG）分析和扰动效应相关性进行的生物学动机评估，以实现标准化报告和可复现的基准测试。作者通过分析单细胞生成建模文献，指出当前缺乏标准化的评估协议，不同方法报告的度量指标因实现选择和超参数不同而无法比较。GGE旨在解决这一挑战，促进生成方法之间的公平比较，并加速在扰动响应预测、细胞身份建模和反事实推理方面的进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid development of generative models for single-cell gene expression data has created an urgent need for standardised evaluation frameworks. Current evaluation practices suffer from inconsistent metric implementations, incomparable hyperparameter choices, and a lack of biologically-grounded metrics. We present Generated Genetic Expression Evaluator (GGE), an open-source Python framework that addresses these challenges by providing a comprehensive suite of distributional metrics with explicit computation space options and biologically-motivated evaluation through differentially expressed gene (DEG)-focused analysis and perturbation-effect correlation, enabling standardized reporting and reproducible benchmarking. Through extensive analysis of the single-cell generative modeling literature, we identify that no standardized evaluation protocol exists. Methods report incomparable metrics computed in different spaces with different hyperparameters. We demonstrate that metric values vary substantially depending on implementation choices, highlighting the critical need for standardization. GGE enables fair comparison across generative approaches and accelerates progress in perturbation response prediction, cellular identity modeling, and counterfactual inference.

</details>

---

### 38. [Ill-Conditioning in Dictionary-Based Dynamic-Equation Learning: A Systems Biology Case Study](https://arxiv.org/abs/2603.11330)

**基本信息**

- 🔗 arXiv: [`2603.11330`](https://arxiv.org/abs/2603.11330)
- 👥 作者: Yuxiang Feng, Niall M Mangan, Manu Jayadharan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11330.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是数据驱动的方程发现（稀疏回归），这是“化学大模型”和“质谱结构推理”中的一个关键子问题。例如，从质谱数据或分子动力学轨迹中发现支配结构-性质关系或反应动力学的方程。论文深入探讨了该过程中的核心挑战（病态条件、库选择），其分析和结论对相关领域的研究具有直接的指导意义。

**📖 中文摘要**

本文研究了从时间序列数据中数据驱动地发现支配方程时，候选函数库方法面临的数值病态问题。当候选函数因采样受限或特定选择而高度相关时，会产生严重的多重共线性和数值不稳定性，导致在测量噪声下恢复的模型差异巨大，阻碍准确的系统识别。作者使用系统生物学的基准模型，系统分析了病态条件如何影响稀疏识别。研究表明，仅涉及两到三项的组合就可能表现出强多重共线性和极大的条件数。此外，正交多项式基并不能一致地解决病态问题，当数据分布偏离与正交基相关的权函数时，其表现可能比单项式库更差。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Data-driven discovery of governing equations from time-series data provides a powerful framework for understanding complex biological systems. Library-based approaches that use sparse regression over candidate functions have shown considerable promise, but they face a critical challenge when candidate functions become strongly correlated: numerical ill-conditioning. Poor or restricted sampling, together with particular choices of candidate libraries, can produce strong multicollinearity and numerical instability. In such cases, measurement noise may lead to widely different recovered models, obscuring the true underlying dynamics and hindering accurate system identification. Although sparse regularization promotes parsimonious solutions and can partially mitigate conditioning issues, strong correlations may persist, regularization may bias the recovered models, and the regression problem may remain highly sensitive to small perturbations in the data. We present a systematic analysis of how ill-conditioning affects sparse identification of biological dynamics using benchmark models from systems biology. We show that combinations involving as few as two or three terms can already exhibit strong multicollinearity and extremely large condition numbers. We further show that orthogonal polynomial bases do not consistently resolve ill-conditioning and can perform worse than monomial libraries when the data distribution deviates from the weight function associated with the orthogonal basis. Finally, we demonstrate that when data are sampled from distributions aligned with the appropriate weight functions corresponding to the orthogonal basis, numerical conditioning improves, and orthogonal polynomial bases can yield improved model recovery accuracy across two baseline models.

</details>

---

### 39. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是构建一个结合了表达嵌入（scGPT）、语义检索（BioBERT）和大语言模型（LLM）的交互式生物发现框架。这直接体现了“化学大模型”中多模态、交互式智能体的思想。同时，ELISA框架本身及其集成的模块（如通路评分、相互作用预测）可以作为用于生物医学数据（可类比化学数据）探索和推理的工具资源。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个将scGPT表达嵌入与基于BioBERT的语义检索以及LLM介导的解释相结合的可解释框架，用于交互式单细胞发现。该框架包含一个自动查询分类器，根据查询是基因特征、自然语言概念还是两者的混合，将输入路由到不同的分析管道。集成的分析模块直接在嵌入数据上执行通路活性评分、配体-受体相互作用预测、条件感知比较分析和细胞类型比例估计，而无需访问原始计数矩阵。在涵盖炎症性肺病、儿科和成人癌症、类器官模型、健康组织和神经发育的六个不同scRNA-seq数据集上的基准测试表明，ELISA在细胞类型检索方面显著优于CellWhisperer。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 40. [Proof-Carrying Materials: Falsifiable Safety Certificates for Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2603.12183)

**基本信息**

- 🔗 arXiv: [`2603.12183`](https://arxiv.org/abs/2603.12183)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12183.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是提高机器学习原子间势（MLIPs）的可靠性和安全性，这直接属于“化学大模型”在材料科学中的应用。PCM框架提供了一套系统的方法（对抗性测试、置信区间、形式化验证）来评估和认证MLIPs，这为化学和材料领域的AI模型提供了重要的可靠性评估工具和资源。

**📖 中文摘要**

本文提出了Proof-Carrying Materials (PCM)，一个为机器学习原子间势（MLIPs）提供可证伪安全证书的框架。PCM通过三个阶段工作：跨组成空间的对抗性证伪、具有95%置信区间的引导包络细化，以及Lean 4形式化认证。作者审计了CHGNet、TensorNet和MACE等MLIP，揭示了架构特定的盲点。一个基于PCM发现特征训练的风险模型可以预测未见材料上的失败。在一个热电筛选案例研究中，经过PCM审计的协议发现了62个额外的稳定材料，这些材料被单MLIP筛选所遗漏——发现率提高了25%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learned interatomic potentials (MLIPs) are deployed for high-throughput materials screening without formal reliability guarantees. We show that a single MLIP used as a stability filter misses 93% of density functional theory (DFT)-stable materials (recall 0.07) on a 25,000-material benchmark. Proof-Carrying Materials (PCM) closes this gap through three stages: adversarial falsification across compositional space, bootstrap envelope refinement with 95% confidence intervals, and Lean 4 formal certification. Auditing CHGNet, TensorNet and MACE reveals architecture-specific blind spots with near-zero pairwise error correlations (r <= 0.13; n = 5,000), confirmed by independent Quantum ESPRESSO validation (20/20 converged; median DFT/CHGNet force ratio 12x). A risk model trained on PCM-discovered features predicts failures on unseen materials (AUC-ROC = 0.938 +/- 0.004) and transfers across architectures (cross-MLIP AUC-ROC ~ 0.70; feature importance r = 0.877). In a thermoelectric screening case study, PCM-audited protocols discover 62 additional stable materials missed by single-MLIP screening - a 25% improvement in discovery yield.

</details>

---

### 41. [drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network](https://arxiv.org/abs/2405.08979)

**基本信息**

- 🔗 arXiv: [`2405.08979`](https://arxiv.org/abs/2405.08979)
- 👥 作者: Yoshitaka Inoue, Hunmin Lee, Tianfan Fu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08979.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建一个用于药物反应预测的图神经网络模型（drGT）。这直接属于“化学大模型”在药物发现和化学生物学中的应用范畴。模型结合了药物、基因和细胞系的多模态信息进行预测和可解释性分析，是化学信息学中一个典型的研究案例。

**📖 中文摘要**

本文提出了drGT，一个利用注意力系数（ACs）预测药物敏感性并辅助生物标志物识别的图深度学习模型。drGT利用由药物、基因和细胞系响应关系构成的异构图。该模型在主要基准数据集（Sanger GDSC, NCI60, Broad CTRP）上进行了训练和评估。drGT在随机拆分下AUROC高达94.5%，对于未见药物为84.4%，对于未见细胞系为70.6%，与现有基准方法性能相当，同时提供了可解释性。在可解释性方面，作者通过文本挖掘PubMed摘要来审查高系数基因与特定药物的共现情况。此外，drGT利用ACs通过富集分析识别每种药物影响的生物过程，从而增强了生物学可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A challenge in drug response prediction is result interpretation compared to established knowledge. drGT is a graph deep learning model that predicts sensitivity and aids in biomarker identification using attention coefficients (ACs). drGT leverages a heterogeneous graph composed of relationships drawn from drugs, genes, and cell line responses. The model is trained and evaluated using major benchmark datasets: Sanger GDSC, NCI60, and Broad CTRP, which cover a wide range of drugs and cancer cell lines. drGT demonstrates AUROC of up to 94.5% under random splitting, 84.4% for unseen drugs, and 70.6% for unseen cell lines, comparable to existing benchmark methods while also providing interpretability. Regarding interpretability, we review drug-gene co-occurrences by text-mining PubMed abstracts for high-coefficient genes mentioning particular drugs. Across 976 drugs from NCI60 with known drug-target interactions (DTIs), model predictions utilized both known DTIs (36.9%) as well as additional predictive associations, many supported by literature. In addition, we compare the drug-gene associations identified by drGT with those from an established DTI prediction model and find that 63.67% are supported by either PubMed literature or predictions from the DTI model. Further, we describe the utilization of ACs to identify affected biological processes by each drug via enrichment analyses, thereby enhancing biological interpretability. Code is available at this https URL .

</details>

---

### 42. [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177)

**基本信息**

- 🔗 arXiv: [`2501.15177`](https://arxiv.org/abs/2501.15177)
- 👥 作者: Yi Su, Jisheng Bai, Qisheng Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.15177.pdf)

**💡 相关性分析**

满足标准3：论文是关于音频-语言模型（ALMs）的专门综述。虽然主题是音频，但其核心——多模态大模型（结合特定领域信号与语言）的架构、训练、评估和应用——与“化学大模型”（结合分子结构与语言/性质）的研究范式高度平行。这篇综述中讨论的模型设计原则、训练策略、评估挑战和未来方向，对“化学大模型”领域的研究人员具有重要的参考和借鉴价值，属于重要的相关讨论。

**📖 中文摘要**

本文对音频-语言模型（ALMs）进行了首次系统性综述。ALMs在配对音频-文本数据上训练，旨在处理、理解和推理以音频为中心的多模态内容。与使用预定义标签的传统监督方法不同，ALMs利用自然语言监督来更好地处理具有多个重叠事件的复杂真实世界音频场景。论文提出了三个主要贡献：（1）从通用音频角度全面覆盖了语音、音乐和声音领域的ALM工作；（2）建立了ALM基础的统一分类法，包括模型架构和训练目标；（3）建立了一个捕捉不同研究方面相互促进和制约的研究格局，有助于总结评估、局限性、关注点和有前景的方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified taxonomy of ALM foundations, including model architectures and training objectives; (3) establishment of a research landscape capturing mutual promotion and constraints among different research aspects, aiding in summarizing evaluations, limitations, concerns and promising directions. Our review contributes to helping researchers understand the development of existing technologies and future trends, while also providing valuable references for implementation in practical applications.

</details>

---

### 43. [GTM: A General Time-series Model for Enhanced Representation Learning of Time-Series Data](https://arxiv.org/abs/2502.03264)

**基本信息**

- 🔗 arXiv: [`2502.03264`](https://arxiv.org/abs/2502.03264)
- 👥 作者: Cheng He, Xu Huang, Gangwei Jiang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03264.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个通用的时间序列基础模型（GTM），其核心创新（频域注意力、混合预训练策略、任务无关设计）为序列数据建模提供了新的架构和方法。虽然应用于时间序列，但这些方法可以迁移或启发“化学大模型”中对分子序列（如SMILES）、光谱序列（如质谱）或时间演化过程（如反应动力学）的建模，提供了有价值的模型设计资源。

**📖 中文摘要**

本文提出了通用时间序列模型（GTM），通过一种新颖的频域注意力机制来推进表示学习，该机制捕获时间粒度感知特征。作者进一步提出了一种新颖的预训练策略，通过混合掩码机制统一了重构和自回归目标。结合2D位置编码和跨度洗牌，该预训练策略增强了表示的鲁棒性和泛化能力。GTM被确立为第一个用于时间序列分析的生成任务无关模型，无需任何任务特定修改即可无缝适应各种生成任务。大量实验表明，GTM在各种生成任务上始终优于SOTA模型，并且通过最小化适应实现了强大的分类结果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite recent progress in time-series foundation models, challenges persist in improving representation learning and adapting to diverse downstream tasks. We introduce a General Time-series Model (GTM), which advances representation learning via a novel frequency-domain attention mechanism that captures time-granularity-aware features, an aspect underexplored in prior research. We further propose a novel pre-training strategy that unifies reconstruction and autoregressive objectives through a hybrid masking mechanism. Our pre-training strategy, combined with 2D positional encoding and span shuffling, enhances the robustness and generalization of representations. GTM is established as the first generative-task-agnostic model for time-series analysis, enabling seamless adaptation to various generative tasks without any task-specific modifications. Extensive experiments demonstrate that GTM consistently outperforms SOTA models on various generative tasks and achieves strong classification results with minimal adaptation. Furthermore, GTM exhibits clear scaling behavior, with accuracy improving as model size and pre-training data increase.

</details>

---

### 44. [HOG-Diff: Higher-Order Guided Diffusion for Graph Generation](https://arxiv.org/abs/2502.04308)

**基本信息**

- 🔗 arXiv: [`2502.04308`](https://arxiv.org/abs/2502.04308)
- 👥 作者: Yiming Huang, Tolga Birdal
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.04308.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是用于图生成的扩散模型。分子是一种特殊的图，因此图生成是“化学大模型”中分子生成的核心技术。HOG-Diff创新性地引入了高阶拓扑引导，这对于生成具有正确化学键和环状结构的分子图至关重要。该模型为化学领域的分子生成任务提供了新的、有潜力的方法资源。

**📖 中文摘要**

本文提出了高阶引导扩散（HOG-Diff），一个逐步生成具有固有拓扑结构的合理图的原则性框架。HOG-Diff遵循由粗到细的生成课程，由高阶拓扑引导并通过扩散桥实现。作者进一步证明，该模型比经典扩散框架具有更强的理论保证。在八个图生成基准测试上的大量实验表明，该方法具有可扩展性，并且在成对和高阶拓扑度量上均表现出优越性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation is a critical yet challenging task, as empirical analyses require a deep understanding of complex, non-Euclidean structures. Diffusion models have recently made significant advances in graph generation, but these models are typically adapted from image generation frameworks and overlook inherent higher-order topology, limiting their ability to capture graph topology. In this work, we propose Higher-order Guided Diffusion (HOG-Diff), a principled framework that progressively generates plausible graphs with inherent topological structures. HOG-Diff follows a coarse-to-fine generation curriculum, guided by higher-order topology and implemented via diffusion bridges. We further prove that our model admits stronger theoretical guarantees than classical diffusion frameworks. Extensive experiments across eight graph generation benchmarks, spanning diverse domains and including large-scale settings, demonstrate the scalability of our method and its superior performance on both pairwise and higher-order topological metrics. Our project page is available \href{ this https URL }{here}.

</details>

---

### 45. [Riemannian Variational Flow Matching for Material and Protein Design](https://arxiv.org/abs/2502.12981)

**基本信息**

- 🔗 arXiv: [`2502.12981`](https://arxiv.org/abs/2502.12981)
- 👥 作者: Olga Zaghen, Floor Eijkelboom, Alison Pouplin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.12981.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是提出了一种在流形上进行生成建模的新方法（RG-VFM）。在化学和材料领域，分子和材料的结构空间通常被视为一个复杂的流形。RG-VFM为在这些流形上生成和优化分子/材料结构（例如，蛋白质设计、材料设计）提供了先进的生成建模框架。这直接与“化学大模型”中的生成任务相关，并提供了重要的方法学资源。

**📖 中文摘要**

本文提出了黎曼高斯变分流匹配（RG-VFM），这是变分流匹配（VFM）在流形上生成建模的几何扩展。受VFM优势的启发，作者基于黎曼高斯分布，为具有闭式测地线的流形推导了一个变分流匹配目标。关键的是，在欧几里得空间中，预测端点（VFM）、速度（FM）或噪声（扩散）在很大程度上是等价的。然而，在弯曲流形上，这种等价性被打破。作者正式分析了该模型与黎曼流匹配（RFM）之间的关系，揭示了RFM目标缺乏一个曲率相关的惩罚项——该惩罚项通过雅可比场自然编码在RG-VFM中。基于此关系，作者假设端点预测通过直接最小化测地线距离提供了更强的学习信号。在合成球面和双曲基准测试以及材料和蛋白质生成的真实世界任务上的实验表明，RG-VFM比欧几里得和基于速度的基线方法更有效地捕获流形结构并提高下游性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Riemannian Gaussian Variational Flow Matching (RG-VFM), a geometric extension of Variational Flow Matching (VFM) for generative modeling on manifolds. Motivated by the benefits of VFM, we derive a variational flow matching objective for manifolds with closed-form geodesics based on Riemannian Gaussian distributions. Crucially, in Euclidean space, predicting endpoints (VFM), velocities (FM), or noise (diffusion) is largely equivalent due to affine interpolations. However, on curved manifolds this equivalence breaks down. We formally analyze the relationship between our model and Riemannian Flow Matching (RFM), revealing that the RFM objective lacks a curvature-dependent penalty -- encoded via Jacobi fields -- that is naturally present in RG-VFM. Based on this relationship, we hypothesize that endpoint prediction provides a stronger learning signal by directly minimizing geodesic distances. Experiments on synthetic spherical and hyperbolic benchmarks, as well as real-world tasks in material and protein generation, demonstrate that RG-VFM more effectively captures manifold structure and improves downstream performance over Euclidean and velocity-based baselines. Code available at this https URL .

</details>

---

### 46. [Tuning-Free LLM Can Build A Strong Recommender Under Sparse Connectivity And Knowledge Gap Via Extracting Intent](https://arxiv.org/abs/2505.10900)

**基本信息**

- 🔗 arXiv: [`2505.10900`](https://arxiv.org/abs/2505.10900)
- 👥 作者: Wenqing Zheng, Noah Fatsi, Daniel Barcklow 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10900.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用大语言模型（LLM）提取用户和物品的“意图”，并构建意图知识图进行推荐。这种方法论与“化学大模型”中利用LLM理解分子“功能”或“性质”（可视为分子的“意图”），并基于此进行分子检索、推荐或设计的思想高度一致。它展示了LLM如何用于构建领域特定的语义表示以辅助决策，是相关研究的一个典型案例。

**📖 中文摘要**

本文提出了LLM-based Intent Knowledge Graph Recommender (IKGR)，一个新颖的框架，它构建了一个以意图为中心的知识图，其中用户和物品都通过一个免调优、RAG引导的LLM流程提取的意图节点显式连接。通过将意图锚定在外部知识源和用户画像中，IKGR规范地表示了用户寻求什么以及物品满足什么作为一等实体。为了缓解稀疏性，作者进一步引入了相互意图连接致密化策略，该策略缩短了用户和长尾物品之间的语义路径，而无需跨图融合。最后，在意图增强的图上采用轻量级GNN层，以低延迟产生推荐信号。在公共和企业数据集上的大量实验表明，IKGR始终优于强基线模型，特别是在冷启动和长尾数据切片上，同时通过完全离线的LLM流程保持高效。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in recommendation with large language models (LLMs) often rely on either commonsense augmentation at the item-category level or implicit intent modeling on existing knowledge graphs. However, such approaches struggle to capture grounded user intents and to handle sparsity and cold-start scenarios. In this work, we present LLM-based Intent Knowledge Graph Recommender (IKGR), a novel framework that constructs an intent-centric knowledge graph where both users and items are explicitly linked to intent nodes extracted by a tuning-free, RAG-guided LLM pipeline. By grounding intents in external knowledge sources and user profiles, IKGR canonically represents what a user seeks and what an item satisfies as first-class entities. To alleviate sparsity, we further introduce a mutual-intent connectivity densification strategy, which shortens semantic paths between users and long-tail items without requiring cross-graph fusion. Finally, a lightweight GNN layer is employed on top of the intent-enhanced graph to produce recommendation signals with low latency. Extensive experiments on public and enterprise datasets demonstrate that IKGR consistently outperforms strong baselines, particularly on cold-start and long-tail slices, while remaining efficient through a fully offline LLM pipeline.

</details>

---

### 47. [LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models](https://arxiv.org/abs/2505.19240)

**基本信息**

- 🔗 arXiv: [`2505.19240`](https://arxiv.org/abs/2505.19240)
- 👥 作者: Aida Kostikova, Zhipin Wang, Deidamea Bajri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19240.pdf)

**💡 相关性分析**

满足标准3：论文是针对大型语言模型（作为“化学大模型”的一种重要实现形式）局限性研究的系统性综述，包含了对模型能力、发展趋势和潜在风险的广泛讨论，为相关主题的研究提供了重要的背景和资源。

**📖 中文摘要**

本文对大型语言模型（LLM）的局限性研究进行了数据驱动的系统性综述。研究涵盖了2022年至2025年初的ACL和arXiv论文，通过关键词过滤、LLM分类和主题聚类等方法，从大量文献中识别出14,648篇相关论文。研究发现，关于LLM局限性的研究增长迅速，到2025年已占LLM相关论文的30%以上。研究主题包括推理、泛化、幻觉、偏见和安全性等。论文提供了带注释的摘要数据集和已验证的方法论。虽然论文主题是LLM的局限性，但其作为一篇针对“化学大模型”和“质谱结构推理”等AI模型在科学领域应用相关主题的综述，提供了关于模型能力边界、发展趋势和潜在风险的重要讨论和资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains the most studied limitation, followed by generalization, hallucination, bias, and security. The distribution of topics in the ACL dataset stays relatively stable over time, while arXiv shifts toward security risks, alignment, hallucinations, knowledge editing, and multimodality. We offer a quantitative view of trends in LLLMs research and release a dataset of annotated abstracts and a validated methodology, available at: this https URL .

</details>

---

### 48. [Can Theoretical Physics Research Benefit from Language Agents?](https://arxiv.org/abs/2506.06214)

**基本信息**

- 🔗 arXiv: [`2506.06214`](https://arxiv.org/abs/2506.06214)
- 👥 作者: Sirui Lu, Zhijing Jin, Terry Jingchen Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06214.pdf)

**💡 相关性分析**

满足标准3：论文的核心是讨论如何使大语言模型/智能体在特定科学领域（理论物理）中变得有用，这直接类比并关联到“化学大模型”和“质谱结构推理”等主题。论文包含了对领域专业化AI模型所需的训练数据、奖励信号和验证框架的重要讨论，为相关主题的研究提供了前瞻性视角和方法论参考。

**📖 中文摘要**

本文探讨了语言智能体（Language Agents）在理论物理学研究中的应用潜力与当前局限。作者指出，尽管当前大语言模型在数学推理和代码生成方面表现出色，但在物理直觉、约束满足和可靠推理方面存在关键缺陷。物理学研究需要近似判断、对称性利用和物理基础，这要求AI智能体经过专门的物理推理模式训练并配备物理感知的验证工具。论文呼吁在物理学和AI社区之间开展合作，开发特定领域的训练数据集、捕捉物理推理质量的奖励信号以及编码基本原理的验证框架。这篇论文的核心论点是：要使AI（包括大模型）在真实世界的科学研究（如理论物理）中发挥作用，需要领域专业化的训练和工具。这直接关联到“化学大模型”和“质谱结构推理”等主题，因为这些主题本质上也是AI/大模型在特定科学领域（化学、质谱学）的应用。论文提出的愿景和挑战，为在化学信息学和质谱分析领域开发专用AI模型和工具提供了重要的思路和框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are rapidly advancing across diverse domains, yet their application in theoretical physics remains inadequate. While current models show competence in mathematical reasoning and code generation, we identify critical gaps in physical intuition, constraint satisfaction, and reliable reasoning that cannot be addressed through prompting alone. Physics demands approximation judgment, symmetry exploitation, and physical grounding that require AI agents specifically trained on physics reasoning patterns and equipped with physics-aware verification tools. We argue that LLM would require such domain-specialized training and tooling to be useful in real-world for physics research. We envision physics-specialized AI agents that seamlessly handle multimodal data, propose physically consistent hypotheses, and autonomously verify theoretical results. Realizing this vision requires developing physics-specific training datasets, reward signals that capture physical reasoning quality, and verification frameworks encoding fundamental principles. We call for collaborative efforts between physics and AI communities to build the specialized infrastructure necessary for AI-driven scientific discovery.

</details>

---

### 49. [Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism](https://arxiv.org/abs/2509.06322)

**基本信息**

- 🔗 arXiv: [`2509.06322`](https://arxiv.org/abs/2509.06322)
- 👥 作者: Jiajun Bao, Nicolas Boullé, Toni J.B. Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.06322.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索大型语言模型（作为“大模型”的一种）处理科学数据（PDE解）并进行数值推理和外推的能力。这直接证明了基础模型在科学计算和数据分析方面的潜力，与“化学大模型”旨在处理化学和质谱数据并执行结构推理的目标高度相关。

**📖 中文摘要**

本文展示了仅通过文本训练的大型语言模型（LLMs）能够零样本外推偏微分方程（PDE）的时空动力学，而无需微调或自然语言提示。研究将离散化的PDE解作为输入，让LLMs预测未来的时空状态。预测准确性随着时间上下文长度的增加而提高，但在更精细的空间离散化下会下降。在多步滚动预测中，误差随预测时间范围代数增长，类似于经典有限差分求解器中的全局误差累积。作者将其解释为上下文神经缩放定律。为了理解LLMs如何处理PDE解以进行准确预测，作者分析了令牌级输出分布，并揭示了一个一致的三阶段上下文学习进展：从语法模式模仿开始，经过探索性高熵阶段，最终形成自信的、基于数值的预测。这项研究证明了文本训练的LLMs具有强大的数值推理和模式外推能力，这与构建用于科学计算（如化学或质谱数据分析）的“化学大模型”高度相关，展示了基础模型处理复杂科学数据和执行推理任务的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated emergent in-context learning (ICL) capabilities across a range of tasks, including zero-shot time-series forecasting. We show that text-trained foundation models can accurately extrapolate spatiotemporal dynamics from discretized partial differential equation (PDE) solutions without fine-tuning or natural language prompting. Predictive accuracy improves with longer temporal contexts but degrades at finer spatial discretizations. In multi-step rollouts, where the model recursively predicts future spatial states over multiple time steps, errors grow algebraically with the time horizon, reminiscent of global error accumulation in classical finite-difference solvers. We interpret these trends as in-context neural scaling laws, where prediction quality varies predictably with both context length and output length. To better understand how LLMs are able to internally process PDE solutions so as to accurately roll them out, we analyze token-level output distributions and uncover a consistent three-stage ICL progression: beginning with syntactic pattern imitation, transitioning through an exploratory high-entropy phase, and culminating in confident, numerically grounded predictions.

</details>

---

### 50. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是构建和评估一个自主的AI科学家系统，该系统能够进行从分析、假设到实验和撰文的完整科研流程。这直接关联到“化学大模型”和AI for Science的主题，展示了AI模型在自动化科学研究（包括化学和质谱领域）方面的潜力和具体实现框架。同时，论文也包含了对这类系统当前能力、局限性和风险的深入讨论，具有综述和展望的性质。

**📖 中文摘要**

本文介绍了Jr. AI Scientist，一个最先进的自主AI科学家系统，旨在模拟人类学生研究人员的核心研究工作流程。给定人类导师提供的基线论文后，系统会分析其局限性，提出改进的新假设，进行迭代实验直至取得改进，并撰写结果论文。与先前假设完全自动化或在小规模代码上运行的方法不同，Jr. AI Scientist遵循明确的研究工作流程，并利用现代编码智能体处理复杂的多文件实现，从而产生有科学价值的贡献。通过实验，Jr. AI Scientist成功地在真实的NeurIPS、IJCV和ICLR工作的基础上，通过提出和实现新方法，生成了新的研究论文。作者进行了自动化评估、作者主导的评估以及向专门从事AI驱动贡献的Agents4Science会议投稿。研究结果展示了AI科学家系统的当前能力和局限性。本文系统地探讨了AI驱动科学发现的框架、工作流程和风险评估，这与利用“化学大模型”或AI智能体自动化化学信息学或质谱分析中的研究流程（如假设生成、实验设计、数据分析）的主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems (autoresearch) is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, iteratively experiments until improvements are achieved, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel methods. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 51. [De novo molecular structure elucidation from mass spectra via flow matching](https://arxiv.org/abs/2602.19912)

**基本信息**

- 🔗 arXiv: [`2602.19912`](https://arxiv.org/abs/2602.19912)
- 👥 作者: Ghaith Mqawass, Tuan Le, Fabian Theis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.19912.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，开发了一个用于从质谱数据中从头解析分子结构的生成模型。

**📖 中文摘要**

本文提出了MSFlow，一个用于从质谱数据中从头解析分子结构的两阶段编码器-解码器流匹配生成模型。该研究直接针对“质谱结构推理”这一核心主题，旨在解决将质谱翻译为完整分子结构这一困难且定义不明确的逆问题。在第一阶段，模型使用公式限制的Transformer将质谱编码为连续且具有化学信息性的嵌入空间。在第二阶段，训练一个解码器流匹配模型，从质谱的潜在嵌入中重建分子。作者进行了严格的评估，证明MSFlow能够将高达45%的分子质谱准确翻译为其对应的分子表示，比当前最先进的方法提高了十四倍。这项工作代表了质谱结构解析领域的重大进展，并公开发布了训练好的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

</details>

---

### 52. [On the Value of Tokeniser Pretraining in Physics Foundation Models](https://arxiv.org/abs/2603.05598)

**基本信息**

- 🔗 arXiv: [`2603.05598`](https://arxiv.org/abs/2603.05598)
- 👥 作者: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05598.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（分词器预训练、两阶段训练、领域对齐）直接关联“化学大模型”的构建范式，为在化学信息学等领域训练高效、可迁移的基础模型提供了重要的技术见解和实证指导。

**📖 中文摘要**

本文研究了分词器预训练对物理仿真基础模型准确性和效率的影响。虽然论文主要关注物理仿真，但其核心方法论——使用自编码目标预训练分词器，然后训练动力学模型——与构建用于科学发现的“化学大模型”在架构和训练范式上高度相关。论文系统地探讨了将高分辨率时空数据压缩为紧凑表示（分词）与学习底层物理动力学这两个任务的解耦训练策略。研究发现，在训练动力学模型之前对分词器进行预训练，可以显著提高物理仿真的计算效率，并且收益大小取决于预训练数据与目标任务之间的领域对齐程度。这项工作为训练高效的物理仿真器（可视为科学领域的大模型）提供了实用的指导，并强调了策略性预训练数据选择的重要性，其方法论对构建化学领域的专用大模型具有直接的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an autoencoding objective prior to training the dynamics model enhances computational efficiency for physics emulation. Notably, the magnitude of this benefit depends on domain alignment: pretraining on the same physical system as the emulation task yields the largest improvements, while pretraining on other systems provides moderate gains. In-domain pretraining reduces VRMSE by 64% after 10,500 training steps compared to training from scratch. To our knowledge, this is the first systematic investigation of tokeniser pretraining for physics foundation models. We further introduce flexible spatiotemporal compression operations that extend causal convolutions to support runtime-adjustable compression ratios, enabling efficient adaptation to diverse downstream tasks. Our findings provide practical guidance for training efficient physics emulators and highlight the importance of strategic pretraining data selection.

</details>

---

### 53. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种名为LatentChem的新框架，旨在改进化学大语言模型的推理机制，使其从依赖显式文本思维链转向更高效的潜在空间推理。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）主要依赖显式自然语言思维链（CoT）进行复杂推理的局限性。作者认为，化学推理本质上是连续和结构化的，将其强制转换为离散的语言标记会导致表示不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续的潜在空间中直接执行多步推理，而仅在最终输出时生成语言。实验表明，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐步放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，而且在计算上具有优势。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于基于CoT的基线模型取得了59.88%的非平局胜率，同时实现了平均10.84倍的推理加速。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 54. [Semantics-Aware Caching for Concept Learning](https://arxiv.org/abs/2603.06506)

**基本信息**

- 🔗 arXiv: [`2603.06506`](https://arxiv.org/abs/2603.06506)
- 👥 作者: Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06506.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种通用的语义感知缓存框架和工具，可用于加速概念学习任务。虽然论文本身不专门针对化学，但其提出的方法（语义感知缓存）作为一种优化工具，可以应用于化学信息学领域的概念学习或知识发现任务，从而提供了潜在有用的资源。

**📖 中文摘要**

本文提出了一种语义感知缓存方法，用于加速概念学习。概念学习是一种在描述逻辑知识库上运行的监督机器学习形式。最先进的概念学习者通常依赖于在可数无限概念空间中的迭代搜索。在每次迭代中，它们检索候选解决方案的实例以选择下一个最佳概念。虽然简单的学习问题可能只需要几十次实例检索调用，但复杂的问题可能需要数千次调用。为了缓解由此产生的运行时挑战，作者提出了一种语义感知缓存方法。该缓存本质上是一个包含感知的映射，通过清晰的集合操作将概念与实例集链接起来。在5个数据集、4个符号推理器、1个神经符号推理器和5种流行分页策略上的实验表明，该缓存可以将概念检索和概念学习的运行时间减少一个数量级，并且对符号和神经符号推理器都有效。这项工作为知识库上的机器学习（包括化学信息学中可能涉及的概念学习任务）提供了性能优化工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

</details>

---

### 55. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于机器学习原子间势（MLIPs）的新型架构。MLIPs是化学信息学和计算化学中进行大规模原子模拟的关键工具，用于预测分子和材料的能量、力与性质。因此，该工作直接与“化学大模型”（此处指用于化学体系的机器学习模型）的主题相关。

**📖 中文摘要**

本文为机器学习原子间势（MLIPs）系统性地开发了混合专家（MoE）和混合线性专家（MoLE）架构，并分析了路由策略和专家设计的影响。作者表明，稀疏激活与共享专家相结合可带来显著的性能提升，并且当存在共享专家时，非线性MoE公式优于MoLE，这突显了非线性专家专业化的重要性。此外，基于元素的（element-wise）路由始终优于配置级（configuration-level）路由。由此产生的基于元素的MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、化学上可解释的专家专业化，表明该模型有效地捕获了元素特定的化学特性，用于精确的原子间建模。这项工作直接提升了用于分子和材料模拟的机器学习势函数的表达能力与效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 56. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准2：论文的第二部分使用了名为Prometheus的beta-VAE框架，这是一个基于变分自编码器（VAE）的机器学习工具，用于从模拟数据中无监督地检测物理相变和集体模式（如等离子体振荡）。虽然论文的物理背景是束物理，但其核心方法——无监督发现框架——作为一种通用工具，可以应用于其他领域的数据分析，包括潜在的化学或质谱数据分析，以发现数据中的隐藏模式或相变。

**📖 中文摘要**

本文为中等能量（10-100 MeV）强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。在第一部分，作者基于Vlasov-Poisson系统建立了动理学场论，推导了三种束分布函数的Lindhard介电函数和随机相位近似（RPA）极化张量。通过介电函数epsilon(omega,q)=0，证明了在临界束密度n_c以上存在无阻尼的朗缪尔波模式，获得了显式的束-等离子体色散关系，并证明了朗道阻尼在粒子-空穴连续谱之上消失。等离子体频率Omega_p^2由f求和定则固定，与分布形状无关；更高的色散系数依赖于速度矩。空间电荷效应驱动了具有sqrt(n-n_c)起始和q=2k_F处Friedel振荡的异常束展宽。通过重整化群分析，束-等离子体转变属于3D Ising普适类。在第二部分，作者使用在粒子模拟（PIC）束数据静态结构因子S(q)上训练的beta-VAE框架Prometheus验证了这些预测。Prometheus检测到了高斯和均匀分布中集体等离子体振荡的起始，确认了它们在简并费米气体（n_c -> 0）中的缺失，并解析了q=2k_F处的Kohn异常。对PIC模拟得到的S(q,omega)的色散分析验证了由f求和定则预测的与分布无关的Omega_p。这项工作展示了将第一性原理理论与基于机器学习的发现工具（如Prometheus）相结合，用于研究复杂物理系统（如束-等离子体相互作用）中的相变和集体模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

## 📊 数据统计
- 累计运行天数：27
- 累计论文数量：1977

## 📝 历史记录

> 暂无历史数据

