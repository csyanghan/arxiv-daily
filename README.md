# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-01 12:35:30

## 📅 2026-03-01 (今日最新)

**相关论文数：45**

### 1. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型（Zatom-1），这直接围绕“化学大模型”这一核心主题。

**📖 中文摘要**

本文介绍了Zatom-1，一个用于3D分子和材料的统一基础模型。该模型是一个Transformer，通过多模态流匹配目标进行训练，联合建模离散原子类型和连续3D几何结构。这种方法支持可扩展的预训练，并能够实现快速稳定的采样。Zatom-1将联合生成式预训练作为下游多任务预测（如性质、能量和力）的通用初始化。该模型在生成和预测基准测试中匹配或超越了专门的基线模型，同时将生成推理时间减少了一个数量级以上。实验表明，联合生成式预训练在化学领域之间产生了正向的预测迁移：在预训练中建模材料提高了分子性质预测的准确性。这篇论文的核心是开发一个用于3D化学建模的AI基础模型，直接属于“化学大模型”的研究范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 2. [Multi-Level Causal Embeddings](https://arxiv.org/abs/2602.22287)

**基本信息**

- 🔗 arXiv: [`2602.22287`](https://arxiv.org/abs/2602.22287)
- 👥 作者: Willem Schooltink, Fabio Massimo Zennaro
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22287.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是研究因果模型的抽象和嵌入框架。这一理论框架对于构建能够进行因果推理的“化学大模型”（例如，理解分子结构如何导致特定性质或活性）具有直接的相关性和指导意义。

**📖 中文摘要**

本文提出了一个用于因果嵌入的框架，作为抽象概念的泛化，并提出了一个广义的一致性概念。通过定义一个多分辨率边际问题，作者展示了因果嵌入对于统计边际问题和因果边际问题的相关性。虽然论文本身是理论性的，但其核心是研究因果模型的抽象和嵌入，旨在保留因果关系。在化学信息学领域，理解分子结构、性质与功能之间的因果关系至关重要。因此，这篇论文提出的因果嵌入框架，为构建能够理解和推理化学结构与性质之间因果关系的“化学大模型”提供了理论基础和方法论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Abstractions of causal models allow for the coarsening of models such that relations of cause and effect are preserved. Whereas abstractions focus on the relation between two models, in this paper we study a framework for causal embeddings which enable multiple detailed models to be mapped into sub-systems of a coarser causal model. We define causal embeddings as a generalization of abstraction, and present a generalized notion of consistency. By defining a multi-resolution marginal problem, we showcase the relevance of causal embeddings for both the statistical marginal problem and the causal marginal problem; furthermore, we illustrate its practical use in merging datasets coming from models with different representations.

</details>

---

### 3. [Quadratization of Autonomous Partial Differential Equations: Theory and Algorithms](https://arxiv.org/abs/2602.22371)

**基本信息**

- 🔗 arXiv: [`2602.22371`](https://arxiv.org/abs/2602.22371)
- 👥 作者: Albani Olivieri, Gleb Pogudin, Boris Kramer
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22371.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是偏微分方程（PDEs）的二次化，这是一种将复杂非线性系统转化为更易处理形式的数学方法。由于许多化学过程（如反应、扩散、传质）由PDE描述，该工作为简化和分析化学动力学模型提供了基础工具，与构建基于物理原理的“化学大模型”这一主题相关。

**📖 中文摘要**

本文研究了偏微分方程（PDEs）的二次化问题，这是一个通过引入辅助变量将非二次PDE转化为二次形式的符号变换过程。作者提出了PDE二次化的严格定义、关于一维空间PDE二次化问题的理论结果（包括存在性和复杂性），并介绍了QuPDE算法。该算法基于符号计算和离散优化，可以为任何一维空间多项式或有理PDE输出一个二次化形式。这是第一个为PDE寻找二次化的计算工具。在化学领域，许多物理化学过程（如反应扩散、流体动力学）都使用PDE建模。将复杂的非线性PDE二次化可以简化其分析和数值模拟。这项工作为处理化学系统中的复杂动力学模型提供了数学工具，间接支持了构建更高效、更可解释的“化学大模型”（特别是基于物理原理的模型）的努力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quadratization for partial differential equations (PDEs) is a process that transforms a nonquadratic PDE into a quadratic form by introducing auxiliary variables. This symbolic transformation has been used in diverse fields to simplify the analysis, simulation, and control of nonlinear and nonquadratic PDE models. This paper presents a rigorous definition of PDE quadratization, theoretical results for the PDE quadratization problem of spatially one-dimensional PDEs-including results on existence and complexity-and introduces QuPDE, an algorithm based on symbolic computation and discrete optimization that outputs a quadratization for any spatially one-dimensional polynomial or rational PDE. This algorithm is the first computational tool to find quadratizations for PDEs to date. We demonstrate QuPDE's performance by applying it to fourteen nonquadratic PDEs in diverse areas such as fluid mechanics, space physics, chemical engineering, and biological processes. QuPDE delivers a low-order quadratization in each case, uncovering quadratic transformations with fewer auxiliary variables than those previously discovered in the literature for some examples, and finding quadratizations for systems that had not been transformed to quadratic form before.

</details>

---

### 4. [A Reduced Order Model approach for First-Principles Molecular Dynamics Computations](https://arxiv.org/abs/2602.22390)

**基本信息**

- 🔗 arXiv: [`2602.22390`](https://arxiv.org/abs/2602.22390)
- 👥 作者: Siu Wun Cheung, Youngsoo Choi, Jean-Luc Fattebert 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22390.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种基于数据驱动和降阶模型的方法来加速第一性原理分子动力学中的电子结构计算。这直接关系到利用AI技术构建高效、准确的“化学大模型”用于分子模拟和性质预测。

**📖 中文摘要**

为了利用第一性原理分子动力学每一步计算出的电子结构之间的冗余性，本文提出了一种用于Kohn-Sham密度泛函理论的数据驱动建模框架，绕过了对电子波函数的显式优化。该方法通过先验采样代表性原子构型，构建一个能有效近似电子结构子空间的低维基。随后，在电子单粒子密度矩阵的直接求解器中使用这个约化基，从而无需迭代波函数优化即可高效确定基态。作者以水分子的玻恩-奥本海默分子动力学为例，展示了该方法的有效性，证明所得模拟能准确复现从完整第一性原理分子动力学获得的关键结构性质（如键长和键角）。这项工作突出了数据驱动方法在为第一性原理模拟开发高效电子结构求解器方面的潜力。该研究直接涉及使用AI/机器学习方法加速量子化学计算，这是构建高精度“化学大模型”（用于分子模拟和性质预测）的核心技术之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To leverage the redundancy between the electronic structure computed at each step of first-principles molecular dynamics, we present a data-driven modeling framework for Kohn-Sham Density Functional Theory that bypasses the explicit optimization of electronic wavefunctions. We sample a priori representative atomic configurations and construct a low-dimensional basis that efficiently approximates the electronic structure subspace. Subsequently, we employ this reduced basis in a direct solver for the electronic single particle density matrix, thereby enabling the efficient determination of ground state without iterative wavefunction optimization. We demonstrate the efficacy of our approach in a Born-Oppenheimer molecular dynamics of a water molecule, showing that the resulting simulations accurately reproduce key structural properties, such as bond lengths and bond angle, obtained from full first-principles molecular dynamics. This work highlights the potential of data-driven approaches to develop efficient electronic structure solvers for first-principles simulations.

</details>

---

### 5. [MolFM-Lite: Multi-Modal Molecular Property Prediction with Conformer Ensemble Attention and Cross-Modal Fusion](https://arxiv.org/abs/2602.22405)

**基本信息**

- 🔗 arXiv: [`2602.22405`](https://arxiv.org/abs/2602.22405)
- 👥 作者: Syed Omer Shah, Mohammed Maqsood Ahmed, Danish Mohiuddin Mohammed 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22405.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个整合1D、2D、3D分子表示的多模态模型，这直接属于“化学大模型”的主题。

**📖 中文摘要**

本文提出了MolFM-Lite，一个用于分子性质预测的多模态模型。它联合编码SELFIES序列（1D）、分子图（2D）和构象体集合（3D），并通过交叉注意力进行融合。该模型的核心贡献包括构象体集合注意力机制和跨模态融合层。虽然论文主要关注分子性质预测，但其核心方法——整合多种分子表示（序列、图、3D结构）并进行跨模态融合——直接属于“化学大模型”的研究范畴。模型在ZINC250K数据集上进行预训练，并发布了所有代码、训练模型和数据分割，为化学信息学领域提供了可复现的工具和资源。

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

满足标准3：论文是关于AI（包括大语言模型）在科学领域（生命周期评估）应用的综述，包含了对AI方法（包括LLMs）发展趋势的重要讨论，与“化学大模型”这一广泛主题相关。

**📖 中文摘要**

本文综述了人工智能（AI）在生命周期评估（LCA）中的整合应用。研究利用大型语言模型（LLMs）对AI-LCA交叉领域的已发表工作进行详细回顾，以识别当前趋势、新兴主题和未来方向。分析表明，随着LCA研究的扩展，AI技术的采用急剧增长，并明显转向LLM驱动的方法。通过将基于LLM的文本挖掘方法与传统的文献综述技术相结合，本研究引入了一个动态有效的框架，能够捕捉该领域的高层研究趋势和细微的概念模式。这项工作展示了LLM辅助方法在支持跨广泛研究领域的大规模、可重复综述方面的潜力，同时评估了在AI技术快速发展背景下实现计算高效LCA的途径。

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

满足标准1：论文的核心研究内容是开发一个用于科学机器学习（SciML）模型设计的自动化框架，并在分子科学等领域的任务上进行评估，这直接与利用AI/机器学习模型（可视为“化学大模型”的一种构建方法）解决化学科学问题的主题相关。

**📖 中文摘要**

本文介绍了LUMOS，一个基于L0正则化学习的端到端框架，旨在民主化科学机器学习（SciML）模型设计。它通过半随机门控和重参数化技术，在训练过程中动态选择信息特征并修剪冗余参数，减少了对人工调优的依赖。该框架在包括分子科学在内的13个不同的SciML工作负载上进行了评估，证明了其有效性和通用性。实验表明，LUMOS平均实现了71.45%的参数减少和6.4倍的推理加速。这项工作为科学领域（包括化学/分子科学）的机器学习模型设计提供了一种自动化的、数据驱动的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of scientific machine learning (SciML) has accelerated discovery across diverse domains, yet designing effective SciML models remains a challenging task. In practice, building such models often requires substantial prior knowledge and manual expertise, particularly in determining which input features to use and how large the model should be. We introduce LUMOS, an end-to-end framework based on L0-regularized learning that unifies feature selection and model pruning to democratize SciML model design. By employing semi-stochastic gating and reparameterization techniques, LUMOS dynamically selects informative features and prunes redundant parameters during training, reducing the reliance on manual tuning while maintaining predictive accuracy. We evaluate LUMOS across 13 diverse SciML workloads, including cosmology and molecular sciences, and demonstrate its effectiveness and generalizability. Experiments on 13 SciML models show that LUMOS achieves 71.45% parameter reduction and a 6.4x inference speedup on average. Furthermore, Distributed Data Parallel (DDP) training on up to eight GPUs confirms the scalability of

</details>

---

### 8. [dLLM: Simple Diffusion Language Modeling](https://arxiv.org/abs/2602.22661)

**基本信息**

- 🔗 arXiv: [`2602.22661`](https://arxiv.org/abs/2602.22661)
- 👥 作者: Zhanhui Zhou, Lingjie Chen, Hanghang Tong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22661.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学领域的重要主题——化学大模型（扩散语言模型是生成式模型的一种，属于化学大模型范畴）。

**📖 中文摘要**

本文介绍了dLLM，一个用于扩散语言建模的统一开源框架。该框架标准化了扩散语言模型（DLM）的核心组件，包括训练、推理和评估，使其易于定制新设计。dLLM允许用户通过标准化流程重现、微调、部署和评估开源的大型DLM（如LLaDA和Dream）。此外，该框架还提供了从零开始构建小型DLM的最小化、可复现方案，包括将任何BERT风格的编码器或自回归语言模型转换为DLM。这项工作通过提供统一的工具和预训练检查点，旨在使DLM更易于访问，并加速该领域的未来研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although diffusion language models (DLMs) are evolving quickly, many recent models converge on a set of shared components. These components, however, are distributed across ad-hoc research codebases or lack transparent implementations, making them difficult to reproduce or extend. As the field accelerates, there is a clear need for a unified framework that standardizes these common components while remaining flexible enough to support new methods and architectures. To address this gap, we introduce dLLM, an open-source framework that unifies the core components of diffusion language modeling -- training, inference, and evaluation -- and makes them easy to customize for new designs. With dLLM, users can reproduce, finetune, deploy, and evaluate open-source large DLMs such as LLaDA and Dream through a standardized pipeline. The framework also provides minimal, reproducible recipes for building small DLMs from scratch with accessible compute, including converting any BERT-style encoder or autoregressive LM into a DLM. We also release the checkpoints of these small DLMs to make DLMs more accessible and accelerate future research.

</details>

---

### 9. [Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs](https://arxiv.org/abs/2602.22698)

**基本信息**

- 🔗 arXiv: [`2602.22698`](https://arxiv.org/abs/2602.22698)
- 👥 作者: Siyue Su, Jian Yang, Bo Li 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22698.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学领域的关键主题——化学大模型（LLM）与知识图谱（KG）的集成与推理，这是构建化学领域知识增强大模型的重要方向。

**📖 中文摘要**

本文提出了KGT框架，旨在解决大型语言模型（LLM）用于知识图谱补全（KGC）时存在的粒度不匹配问题。LLM基于碎片化的token序列操作，而知识图谱中的实体是基本单元。KGT通过引入专用的实体token来实现高效的全空间预测。具体包括：1）专门的token化方法，在专用实体token级别构建特征表示；2）通过关系引导的门控机制，将预训练的结构和文本特征融合到统一的嵌入中；3）通过独立的预测头实现解耦预测，以分离和结合语义与结构推理。实验表明KGT在多个基准测试中优于现有方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Leveraging Large Language Models (LLMs) for Knowledge Graph Completion (KGC) is promising but hindered by a fundamental granularity mismatch. LLMs operate on fragmented token sequences, whereas entities are the fundamental units in knowledge graphs (KGs) scenarios. Existing approaches typically constrain predictions to limited candidate sets or align entities with the LLM's vocabulary by pooling multiple tokens or decomposing entities into fixed-length token sequences, which fail to capture both the semantic meaning of the text and the structural integrity of the graph. To address this, we propose KGT, a novel framework that uses dedicated entity tokens to enable efficient, full-space prediction. Specifically, we first introduce specialized tokenization to construct feature representations at the level of dedicated entity tokens. We then fuse pre-trained structural and textual features into these unified embeddings via a relation-guided gating mechanism, avoiding training from scratch. Finally, we implement decoupled prediction by leveraging independent heads to separate and combine semantic and structural reasoning. Experimental results show that KGT consistently outperforms state-of-the-art methods across multiple benchmarks.

</details>

---

### 10. [BRepMAE: Self-Supervised Masked BRep Autoencoders for Machining Feature Recognition](https://arxiv.org/abs/2602.22701)

**基本信息**

- 🔗 arXiv: [`2602.22701`](https://arxiv.org/abs/2602.22701)
- 👥 作者: Can Yao, Kang Wu, Zuheng Zheng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22701.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及化学信息学和材料科学中重要的分子/材料结构表示与学习（BRep表示和gAAG图），这是构建化学结构推理模型的基础。其自监督学习框架与化学大模型的预训练理念高度相关。

**📖 中文摘要**

本文提出了BRepMAE，一个用于计算机辅助设计（CAD）模型加工特征识别的掩码自监督学习框架。该框架在大型无标签CAD模型数据集上，使用源自边界表示（BRep）的几何属性邻接图（gAAG）进行表示学习。自监督网络是一个掩码图自编码器（MAE），专注于重建BRep面的几何和属性，而非图结构。预训练后，我们对一个包含编码器和任务特定分类网络的网络进行微调，用于加工特征识别（MFR）。实验表明，微调后的网络仅需少量数据（例如0.1%的训练数据）即可实现高识别率，显著提升了在现实（或私有）场景中数据有限时的实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a masked self-supervised learning framework, called BRepMAE, for automatically extracting a valuable representation of the input computer-aided design (CAD) model to recognize its machining features. Representation learning is conducted on a large-scale, unlabeled CAD model dataset using the geometric Attributed Adjacency Graph (gAAG) representation, derived from the boundary representation (BRep). The self-supervised network is a masked graph autoencoder (MAE) that focuses on reconstructing geometries and attributes of BRep facets, rather than graph structures. After pre-training, we fine-tune a network that contains both the encoder and a task-specific classification network for machining feature recognition (MFR). In the experiments, our fine-tuned network achieves high recognition rates with only a small amount of data (e.g., 0.1% of the training data), significantly enhancing its practicality in real-world (or private) scenarios where only limited data is available. Compared with other MFR methods, our fine-tuned network achieves a significant improvement in recognition rate with the same amount of training data, especially when the number of training samples is limited.

</details>

---

### 11. [IRSDE-Despeckle: A Physics-Grounded Diffusion Model for Generalizable Ultrasound Despeckling](https://arxiv.org/abs/2602.22717)

**基本信息**

- 🔗 arXiv: [`2602.22717`](https://arxiv.org/abs/2602.22717)
- 👥 作者: Shuoqi Chen, Yujia Wu, Geoffrey P. Luke
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22717.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕质谱分析领域的核心挑战——信号处理与去噪。虽然应用在医学超声成像，但其基于扩散模型的去噪框架、信号模拟、不确定性量化等方法论与质谱数据的预处理、谱图去卷积和噪声抑制高度相关，可视为质谱结构推理中信号增强的关键技术。

**📖 中文摘要**

本文提出了一种基于图像恢复随机微分方程（IR-SDE）框架的扩散模型超声去噪方法。为了进行监督训练，我们通过使用Matlab超声工具箱从无斑点的磁共振图像模拟超声图像，构建了大型配对数据集。所提出的模型在抑制斑点噪声的同时，保留了具有解剖学意义的边缘和对比度。在保留的模拟测试集上，我们的方法 consistently outperforms 经典滤波器和近期基于学习的去噪基线。我们通过跨模型方差量化预测不确定性，并表明更高的不确定性与更高的重建误差相关，为困难或易失败区域提供了实用的指示器。最后，我们评估了对模拟探头设置的敏感性，并观察到领域偏移，这促使了多样化的训练和适应以实现稳健的临床部署。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ultrasound imaging is widely used for real-time, noninvasive diagnosis, but speckle and related artifacts reduce image quality and can hinder interpretation. We present a diffusion-based ultrasound despeckling method built on the Image Restoration Stochastic Differential Equations framework. To enable supervised training, we curate large paired datasets by simulating ultrasound images from speckle-free magnetic resonance images using the Matlab UltraSound Toolbox. The proposed model reconstructs speckle-suppressed images while preserving anatomically meaningful edges and contrast. On a held-out simulated test set, our approach consistently outperforms classical filters and recent learning-based despeckling baselines. We quantify prediction uncertainty via cross-model variance and show that higher uncertainty correlates with higher reconstruction error, providing a practical indicator of difficult or failure-prone regions. Finally, we evaluate sensitivity to simulation probe settings and observe domain shift, motivating diversified training and adaptation for robust clinical deployment.

</details>

---

### 12. [Sapling-NeRF: Geo-Localised Sapling Reconstruction in Forests for Ecological Monitoring](https://arxiv.org/abs/2602.22731)

**基本信息**

- 🔗 arXiv: [`2602.22731`](https://arxiv.org/abs/2602.22731)
- 👥 作者: Miguel Ángel Muñoz-Bañón, Nived Chebrolu, Sruthi M. Krishna Moorthy 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22731.pdf)

**💡 相关性分析**

满足标准2：论文提出的多模态（NeRF， LiDAR， GNSS）融合三维重建与表征管道，为化学信息学中分子三维构象分析、材料微观结构表征以及质谱成像（MSI）数据的空间解析提供了强大的数据获取与处理工具和框架。

**📖 中文摘要**

本文提出了一种融合神经辐射场（NeRF）、激光雷达SLAM和GNSS的管道，以实现对森林中树苗的可重复、地理定位的生态监测。我们的系统提出了三级表示：1）使用GNSS进行粗略的地球坐标系定位；2）使用基于激光雷达的SLAM进行厘米级精度的定位和重建；3）使用NeRF衍生的以对象为中心的密集重建来重建单个树苗。该方法能够对树苗性状进行可重复的定量评估和长期监测。我们在英国牛津Wytham Woods和芬兰Evo的森林样地中的实验表明，与地面激光扫描（TLS）相比，该方法可以更准确地捕获茎干高度、分枝模式和叶木比。我们证明，可以原位测量高度在0.5米到2米之间的树苗的准确茎干骨架和叶片分布，为生态学家提供了更丰富的结构和定量数据来分析森林动态。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Saplings are key indicators of forest regeneration and overall forest health. However, their fine-scale architectural traits are difficult to capture with existing 3D sensing methods, which make quantitative evaluation difficult. Terrestrial Laser Scanners (TLS), Mobile Laser Scanners (MLS), or traditional photogrammetry approaches poorly reconstruct thin branches, dense foliage, and lack the scale consistency needed for long-term monitoring. Implicit 3D reconstruction methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) are promising alternatives, but cannot recover the true scale of a scene and lack any means to be accurately geo-localised. In this paper, we present a pipeline which fuses NeRF, LiDAR SLAM, and GNSS to enable repeatable, geo-localised ecological monitoring of saplings. Our system proposes a three-level representation: (i) coarse Earth-frame localisation using GNSS, (ii) LiDAR-based SLAM for centimetre-accurate localisation and reconstruction, and (iii) NeRF-derived object-centric dense reconstruction of individual saplings. This approach enables repeatable quantitative evaluation and long-term monitoring of sapling traits. Our experiments in forest plots in Wytham Woods (Oxford, UK) and Evo (Finland) show that stem height, branching patterns, and leaf-to-wood ratios can be captured with increased accuracy as compared to TLS. We demonstrate that accurate stem skeletons and leaf distributions can be measured for saplings with heights between 0.5m and 2m in situ, giving ecologists access to richer structural and quantitative data for analysing forest dynamics.

</details>

---

### 13. [Molecule Mixture Detection and Design for MC Systems with Non-linear, Cross-reactive Receiver Arrays](https://arxiv.org/abs/2602.22799)

**基本信息**

- 🔗 arXiv: [`2602.22799`](https://arxiv.org/abs/2602.22799)
- 👥 作者: Bastian Heinlein, Kaikai Zhu, Sümeyye Carkit-Yilmaz 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22799.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容围绕分子混合物的检测与推理，使用非线性和交叉反应传感器阵列，这与质谱分析中从复杂谱图进行结构推理的核心问题高度相关。

**📖 中文摘要**

本文研究空气分子通信（MC）系统，重点关注分子混合物检测与设计。系统使用非线性和交叉反应传感器作为接收器，这与质谱分析中传感器对复杂混合物（如代谢物或环境样本）的响应特性高度相关。论文提出了几种检测器和传输方案，包括近似最大似然（AML）符号检测器和互补混合物字母表设计算法，这些方案考虑了接收器的非线性特性。研究使用商业可用传感器（包括金属氧化物半导体传感器）的响应以及人工生成的传感器数据进行验证。这项工作为处理非理想、交叉反应传感器的分子通信系统提供了通用框架，其核心问题——从非线性传感器信号中推断混合物成分——与质谱分析中从复杂质谱图中解析化学结构的核心挑战直接对应。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Air-based molecular communication (MC) has the potential to be one of the first MC systems to be deployed in real-world applications, enabled by commercially available sensors. However, these sensors usually exhibit non-linear and cross-reactive behavior, contrary to the idealizing assumption of linear and perfectly molecule type-specific sensing often made in the MC literature. To address this mismatch, we propose several detectors and transmission schemes for a molecule mixture communication system where the receiver (RX) employs non-linear, cross-reactive sensors. All proposed schemes are based on the first- and second-order moments of the symbol likelihoods that are fed through the non-linear RX using the Unscented Transform. In particular, we propose an approximate maximum likelihood (AML) symbol-by-symbol detector for inter-symbol-interference (ISI)-free transmission scenarios and a complementary mixture alphabet design algorithm which accounts for the RX characteristics. When significant ISI is present at high data rates, the AML detector can be adapted to exploit statistical ISI knowledge. Additionally, we propose a sequence detector which combines information from multiple symbol intervals. For settings where sequence detection is not possible due to extremely limited computational power at the RX, we propose an adaptive transmission scheme which can be combined with symbol-by-symbol detection. Using computer simulations, we validate all proposed detectors and algorithms based on the responses of commercially available sensors as well as artificially generated sensor data incorporating the characteristics of metal-oxide semiconductor sensors. By employing a general system model that accounts for transmitter noise, ISI, and general non-linear, cross-reactive RX arrays, this work enables reliable communication for a large class of MC systems.

</details>

---

### 14. [FlexMS is a flexible framework for benchmarking deep learning-based mass spectrum prediction tools in metabolomics](https://arxiv.org/abs/2602.22822)

**基本信息**

- 🔗 arXiv: [`2602.22822`](https://arxiv.org/abs/2602.22822)
- 👥 作者: Yunhua Zhong, Yixuan Tang, Yifan Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22822.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为FlexMS的基准测试框架，专门用于构建和评估质谱预测模型，这为“质谱结构推理”主题提供了重要的工具和评估资源。同时，其核心研究内容也直接围绕质谱预测，满足标准1。

**📖 中文摘要**

本文介绍了FlexMS，一个用于在代谢组学中基准测试深度学习质谱预测工具的灵活框架。质谱技术通过质荷比峰为化学分子的鉴定和性质预测提供了关键信息。然而，实验谱图的缺乏阻碍了分子鉴定，因此迫切需要建立计算模型来预测分子结构谱图。深度学习模型在此任务上表现出潜力，但由于方法异质性和缺乏明确定义的基准，整体评估仍然具有挑战性。FlexMS旨在解决这一问题，支持动态构建多种不同的模型架构组合，并在预处理过的公共数据集上使用不同指标评估其性能。论文深入探讨了影响性能的因素，包括数据集的结构多样性、学习率等超参数、数据稀疏性、预训练效果、元数据消融设置以及跨领域迁移学习分析。此外，检索基准模拟了实际的鉴定场景，根据预测谱图对潜在匹配进行评分。该框架为开发和评估用于质谱预测的深度学习模型提供了标准化工具和深入见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The identification and property prediction of chemical molecules is of central importance in the advancement of drug discovery and material science, where the tandem mass spectrometry technology gives valuable fragmentation cues in the form of mass-to-charge ratio peaks. However, the lack of experimental spectra hinders the attachment of each molecular identification, and thus urges the establishment of prediction approaches for computational models. Deep learning models appear promising for predicting molecular structure spectra, but overall assessment remains challenging as a result of the heterogeneity in methods and the lack of well-defined benchmarks. To address this, our contribution is the creation of benchmark framework FlexMS for constructing and evaluating diverse model architectures in mass spectrum prediction. With its easy-to-use flexibility, FlexMS supports the dynamic construction of numerous distinct combinations of model architectures, while assessing their performance on preprocessed public datasets using different metrics. In this paper, we provide insights into factors influencing performance, including the structural diversity of datasets, hyperparameters like learning rate and data sparsity, pretraining effects, metadata ablation settings and cross-domain transfer learning analysis. This provides practical guidance in choosing suitable models. Moreover, retrieval benchmarks simulate practical identification scenarios and score potential matches based on predicted spectra.

</details>

---

### 15. [MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis](https://arxiv.org/abs/2602.22955)

**基本信息**

- 🔗 arXiv: [`2602.22955`](https://arxiv.org/abs/2602.22955)
- 👥 作者: Feng Guo, Jiaxiang Liu, Yang Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22955.pdf)

**💡 相关性分析**

满足标准2：论文详细描述了一个大规模、语义丰富的多模态数据集（MM-NeuroOnco）和评估基准（MM-NeuroOnco-Bench）的构建方法论。这种为复杂AI任务创建高质量数据资源的方法，可直接借鉴用于为“化学大模型”和“质谱结构推理”主题构建数据集。

**📖 中文摘要**

本文介绍了MM-NeuroOnco，一个用于基于MRI的脑肿瘤诊断的大规模多模态基准和指令调优数据集。尽管该论文主要关注医学影像（MRI），但其核心方法论——构建一个包含丰富诊断语义注释的大规模多模态数据集，并利用多模型协作管道自动完成医学信息——展示了如何为复杂推理任务（如诊断）创建高质量的数据资源。这种构建富含语义、可用于训练和评估AI模型的数据集的方法论，与化学信息学和质谱分析领域创建用于“化学大模型”或“质谱结构推理”的标注数据集的努力是平行的。论文中开发的数据集构建管道（自动化信息补全和质量控制）以及评估基准（MM-NeuroOnco-Bench）的设计思路，可为化学领域类似数据资源的创建提供参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate brain tumor diagnosis requires models to not only detect lesions but also generate clinically interpretable reasoning grounded in imaging manifestations, yet existing public datasets remain limited in annotation richness and diagnostic semantics. To bridge this gap, we introduce MM-NeuroOnco, a large-scale multimodal benchmark and instruction-tuning dataset for brain tumor MRI understanding, consisting of 24,726 MRI slices from 20 data sources paired with approximately 200,000 semantically enriched multimodal instructions spanning diverse tumor subtypes and imaging modalities. To mitigate the scarcity and high cost of diagnostic semantic annotations, we develop a multi-model collaborative pipeline for automated medical information completion and quality control, enabling the generation of diagnosis-related semantics beyond mask-only annotations. Building upon this dataset, we further construct MM-NeuroOnco-Bench, a manually annotated evaluation benchmark with a rejection-aware setting to reduce biases inherent in closed-ended question formats. Evaluation across ten representative models shows that even the strongest baseline, Gemini 3 Flash, achieves only 41.88% accuracy on diagnosis-related questions, highlighting the substantial challenges of multimodal brain tumor diagnostic understanding. Leveraging MM-NeuroOnco, we further propose NeuroOnco-GPT, which achieves a 27% absolute accuracy improvement on diagnostic questions following fine-tuning. This result demonstrates the effectiveness of our dataset and benchmark in advancing clinically grounded multimodal diagnostic reasoning. Code and dataset are publicly available at: this https URL

</details>

---

### 16. [SPM-Bench: Benchmarking Large Language Models for Scanning Probe Microscopy](https://arxiv.org/abs/2602.22971)

**基本信息**

- 🔗 arXiv: [`2602.22971`](https://arxiv.org/abs/2602.22971)
- 👥 作者: Peiyao Xiao, Xiaogang Li, Chengliang Xu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22971.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种自动化数据合成流水线和方法（AGS技术、混合架构），用于从科学文献中高效生成高质量、领域特定的多模态数据集。这种构建数据集和资源的方法论，可直接应用于为“化学大模型”创建训练和评估数据。

**📖 中文摘要**

本文介绍了SPM-Bench，一个专门为扫描探针显微镜（SPM）设计的、博士级别的多模态基准测试。论文的核心贡献在于提出了一种全自动的数据合成流水线，用于高效地从arXiv和期刊论文中提取高质量的图像-文本对。该流水线采用Anchor-Gated Sieve (AGS)技术和混合云-本地架构，在保持数据集高纯度的同时实现了极致的token节省。虽然论文主题是SPM，但其提出的自动化科学数据合成范式、从科学文献中高效提取结构化多模态数据的方法，以及构建领域特定基准测试的框架，与“化学大模型”主题高度相关。该方法展示了如何为特定科学领域（如化学）构建高质量、低成本的训练和评估数据资源，这对于训练领域专用的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As LLMs achieved breakthroughs in general reasoning, their proficiency in specialized scientific domains reveals pronounced gaps in existing benchmarks due to data contamination, insufficient complexity, and prohibitive human labor costs. Here we present SPM-Bench, an original, PhD-level multimodal benchmark specifically designed for scanning probe microscopy (SPM). We propose a fully automated data synthesis pipeline that ensures both high authority and low-cost. By employing Anchor-Gated Sieve (AGS) technology, we efficiently extract high-value image-text pairs from arXiv and journal papers published between 2023 and 2025. Through a hybrid cloud-local architecture where VLMs return only spatial coordinates "llbox" for local high-fidelity cropping, our pipeline achieves extreme token savings while maintaining high dataset purity. To accurately and objectively evaluate the performance of the LLMs, we introduce the Strict Imperfection Penalty F1 (SIP-F1) score. This metric not only establishes a rigorous capability hierarchy but also, for the first time, quantifies model "personalities" (Conservative, Aggressive, Gambler, or Wise). By correlating these results with model-reported confidence and perceived difficulty, we expose the true reasoning boundaries of current AI in complex physical scenarios. These insights establish SPM-Bench as a generalizable paradigm for automated scientific data synthesis.

</details>

---

### 17. [Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models](https://arxiv.org/abs/2602.23179)

**基本信息**

- 🔗 arXiv: [`2602.23179`](https://arxiv.org/abs/2602.23179)
- 👥 作者: Gal Kesten-Pomeranz, Yaniv Nikankin, Anja Reusch 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23179.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”的一个具体实例——蛋白质语言模型（PLMs）。它深入分析了这类大语言模型在生物化学序列（蛋白质）中识别复杂模式（重复片段）的内部机制，这与理解化学领域大模型的能力和原理高度相关。

**📖 中文摘要**

本文研究了蛋白质语言模型（PLMs）内部检测蛋白质序列中重复片段（包括精确重复和近似重复）的机制。这些重复对蛋白质结构和功能至关重要。论文发现PLMs能够识别这两种重复，并揭示了其内部工作机制包含两个主要阶段：首先，PLMs通过通用的位置注意力头和生物学特化的组件（如编码氨基酸相似性的神经元）构建特征表示；然后，归纳头（induction heads）关注重复片段间对齐的token，从而促进正确答案的预测。研究结果表明，PLMs通过结合基于语言的模式匹配和专门的生物学知识来解决这一生物信息学任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequences are abundant in repeating segments, both as exact copies and as approximate segments with mutations. These repeats are important for protein structure and function, motivating decades of algorithmic work on repeat identification. Recent work has shown that protein language models (PLMs) identify repeats, by examining their behavior in masked-token prediction. To elucidate their internal mechanisms, we investigate how PLMs detect both exact and approximate repeats. We find that the mechanism for approximate repeats functionally subsumes that of exact repeats. We then characterize this mechanism, revealing two main stages: PLMs first build feature representations using both general positional attention heads and biologically specialized components, such as neurons that encode amino-acid similarity. Then, induction heads attend to aligned tokens across repeated segments, promoting the correct answer. Our results reveal how PLMs solve this biological task by combining language-based pattern matching with specialized biological knowledge, thereby establishing a basis for studying more complex evolutionary processes in PLMs.

</details>

---

### 18. [Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications](https://arxiv.org/abs/2602.23303)

**基本信息**

- 🔗 arXiv: [`2602.23303`](https://arxiv.org/abs/2602.23303)
- 👥 作者: Ilya Balabin, Thomas M. Kaiser
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23303.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学领域的机器学习模型（化学大模型）的理论基础构建，旨在解决该领域模型存在的因果缺陷问题。

**📖 中文摘要**

这篇论文题为《Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications》。它直接针对化学信息学领域，提出了一个新颖的理论框架，旨在解决当前化学和生物学中机器学习模型（如用于药物发现的模型）普遍存在的因果结构缺陷问题。作者将化学理论、生物理论、概率论和因果推理相结合，为化学生物学中的机器学习建立了一个新的数学框架，称为“推理力学”。该框架的核心是引入了“焦点”这一新概念，即机器学习算法从大型数据集中聚焦于潜在机制的能力。论文还提供了在Akt抑制剂家族上的初步原理证明。这项工作直接围绕“化学大模型”的主题，因为它旨在为化学和生物学中的机器学习（可视为特定领域的“化学大模型”）提供一个更严谨、基于因果机制的理论基础，以纠正当前黑箱模型的缺陷。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning techniques are now routinely encountered in research laboratories across the globe. Impressive progress has been made through ML and AI techniques with regards to large data set processing. This progress has increased the ability of the experimenter to digest data and make novel predictions regarding phenomena of interest. However, machine learning predictors generated from data sets taken from the natural sciences are often treated as black boxes which are used broadly and generally without detailed consideration of the causal structure of the data set of interest. Work has been attempted to bring causality into discussions of machine learning models of natural phenomena; however, a firm and unified theoretical treatment is lacking. This series of three papers explores the union of chemical theory, biological theory, probability theory and causality that will correct current causal flaws of machine learning in the natural sciences. This paper, Part 1 of the series, provides the formal framework of the foundational causal structure of phenomena in chemical biology and is extended to machine learning through the novel concept of focus, defined here as the ability of a machine learning algorithm to narrow down to a hidden underpinning mechanism in large data sets. Initial proof of these principles on a family of Akt inhibitors is also provided. The second paper containing Part 2 will provide a formal exploration of chemical similarity, and Part 3 will present extensive experimental evidence of how hidden causal structures weaken all machine learning in chemical biology. This series serves to establish for chemical biology a new kind of mathematical framework for modeling mechanisms in Nature without the need for the tools of reductionism: inferential mechanics.

</details>

---

### 19. [CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction](https://arxiv.org/abs/2602.22236)

**基本信息**

- 🔗 arXiv: [`2602.22236`](https://arxiv.org/abs/2602.22236)
- 👥 作者: Rabeya Tus Sadia, Qiang Ye, Qiang Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22236.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是利用和融合生物大语言模型（BioLLMs）进行RNA相互作用预测，这直接属于“化学大模型”在化学生物学领域的应用和研究。

**📖 中文摘要**

这篇论文题为《CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction》。它提出了一种名为CrossLLM-Mamba的新型框架，用于预测RNA相关的相互作用（如RNA-蛋白质、RNA-小分子、RNA-RNA）。该框架的核心是利用生物大语言模型（BioLLMs，如ESM-2, RiNALMo）提供的强大序列表示，并通过双向Mamba编码器实现跨模态的深度状态空间对齐。这项工作将大型语言模型（LLMs）应用于生物分子（RNA）的表示学习和相互作用预测，属于“化学大模型”在生物化学和计算生物学领域的应用。论文展示了该框架在多个基准测试上达到了最先进的性能，证明了基于状态空间建模的LLM融合范式在生物多模态交互预测中的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of RNA-associated interactions is essential for understanding cellular regulation and advancing drug discovery. While Biological Large Language Models (BioLLMs) such as ESM-2 and RiNALMo provide powerful sequence representations, existing methods rely on static fusion strategies that fail to capture the dynamic, context-dependent nature of molecular binding. We introduce CrossLLM-Mamba, a novel framework that reformulates interaction prediction as a state-space alignment problem. By leveraging bidirectional Mamba encoders, our approach enables deep ``crosstalk'' between modality-specific embeddings through hidden state propagation, modeling interactions as dynamic sequence transitions rather than static feature overlaps. The framework maintains linear computational complexity, making it scalable to high-dimensional BioLLM embeddings. We further incorporate Gaussian noise injection and Focal Loss to enhance robustness against hard-negative samples. Comprehensive experiments across three interaction categories, RNA-protein, RNA-small molecule, and RNA-RNA demonstrate that CrossLLM-Mamba achieves state-of-the-art performance. On the RPI1460 benchmark, our model attains an MCC of 0.892, surpassing the previous best by 5.2\%. For binding affinity prediction, we achieve Pearson correlations exceeding 0.95 on riboswitch and repeat RNA subtypes. These results establish state-space modeling as a powerful paradigm for multi-modal biological interaction prediction.

</details>

---

### 20. [VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction](https://arxiv.org/abs/2602.22239)

**基本信息**

- 🔗 arXiv: [`2602.22239`](https://arxiv.org/abs/2602.22239)
- 👥 作者: Ida Egendal, Rasmus Froberg Brøndum, Dan J Woodcock 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22239.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一种基于变分自编码器的深度学习模型，用于分析癌症突变数据（一种化学生物学数据），属于化学信息学中机器学习模型的应用。

**📖 中文摘要**

这篇论文题为《VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction》。它提出了一种用于癌症突变特征提取的新型变分自编码器模型。突变特征分析是癌症基因组学和生物信息学中的关键方法。VAE-MS模型结合了非对称架构和概率方法，旨在从突变数据中更可靠地提取特征。论文将VAE-MS与现有的金标准方法（如SigProfilerExtractor）以及其他先进模型（如MUSE-XAE, SigneR）进行了比较。这项工作属于计算化学和生物信息学领域，利用深度学习模型（VAE）处理和分析化学生物学数据（癌症突变谱），是机器学习在化学和生物学数据建模中的一个具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mutational signature analysis has emerged as a powerful method for uncovering the underlying biological processes driving cancer development. However, the signature extraction process, typically performed using non-negative matrix factorization (NMF), often lacks reliability and clinical applicability. To address these limitations, several solutions have been introduced, including the use of neural networks to achieve more accurate estimates and probabilistic methods to better capture natural variation in the data. In this work, we introduce a Variational Autoencoder for Mutational Signatures (VAE-MS), a novel model that leverages both an asymmetric architecture and probabilistic methods for the extraction of mutational signatures. VAE-MS is compared to with three state-of-the-art models for mutational signature extraction: SigProfilerExtractor, the NMF-based gold standard; MUSE-XAE, an autoencoder that employs an asymmetric design without probabilistic components; and SigneR, a Bayesian NMF model, to illustrate the strength in combining a nonlinear extraction with a probabilistic model. In the ability to reconstruct input data and generalize to unseen data, models with probabilistic components (VAE-MS, SigneR) dramatically outperformed models without (SigProfilerExtractor, MUSE-XAE). The NMF-baed models (SigneR, SigProfilerExtractor) had the most accurate reconstructions in simulated data, while VAE-MS reconstructed more accurately on real cancer data. Upon evaluating the ability to extract signatures consistently, no model exhibited a clear advantage over the others. Software for VAE-MS is available at this https URL .

</details>

---

### 21. [Stochastic Neural Networks for Quantum Devices](https://arxiv.org/abs/2602.22241)

**基本信息**

- 🔗 arXiv: [`2602.22241`](https://arxiv.org/abs/2602.22241)
- 👥 作者: Bodo Rosenhahn, Tobias J. Osborne, Christoph Hirche
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22241.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是在量子设备上实现和优化随机神经网络，探索量子计算与机器学习的交叉，这与未来化学信息学中新型计算模型的发展方向相关。

**📖 中文摘要**

这篇论文题为《Stochastic Neural Networks for Quantum Devices》。它提出了一种在基于门的量子计算中，将随机神经网络表达和优化为量子电路的表述。论文受经典感知器启发，引入了随机神经元并将其组合成量子神经网络。模型使用Kiefer-Wolfowitz算法结合模拟退火进行训练。展示了多种拓扑和模型，包括浅层全连接网络、Hopfield网络、受限玻尔兹曼机、自编码器和卷积神经网络。此外，还演示了将优化后的神经网络作为Grover算法的预言机，以实现量子生成式AI模型。这项工作处于量子计算和机器学习的交叉领域，探索了在量子设备上实现神经网络的可能性，虽然不直接针对质谱，但其关于“模型”和“计算”的核心与广义的“化学信息学模型”有一定关联，且量子计算在未来的化学模拟和分子设计中具有潜在重要性。考虑到其与计算化学和新型计算模型的关联，以包容性原则纳入。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work presents a formulation to express and optimize stochastic neural networks as quantum circuits in gate-based quantum computing. Motivated by a classical perceptron, stochastic neurons are introduced and combined into a quantum neural network. The Kiefer-Wolfowitz algorithm in combination with simulated annealing is used for training the network weights. Several topologies and models are presented, including shallow fully connected networks, Hopfield Networks, Restricted Boltzmann Machines, Autoencoders and convolutional neural networks. We also demonstrate the combination of our optimized neural networks as an oracle for the Grover algorithm to realize a quantum generative AI model.

</details>

---

### 22. [Multi-Dimensional Spectral Geometry of Biological Knowledge in Single-Cell Transformer Representations](https://arxiv.org/abs/2602.22247)

**基本信息**

- 🔗 arXiv: [`2602.22247`](https://arxiv.org/abs/2602.22247)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22247.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深入分析和解释一个用于单细胞生物学的Transformer模型（可视为一种生物化学领域的大模型）的内部表示和知识编码机制。

**📖 中文摘要**

这篇论文题为《Multi-Dimensional Spectral Geometry of Biological Knowledge in Single-Cell Transformer Representations》。它系统地研究了单细胞基础模型scGPT（一种基于Transformer的模型）内部高维基因表示所编码的生物学知识。通过自动化的假设筛选，论文揭示了scGPT模型将基因组织成一个结构化的生物坐标系，其中主导的光谱轴根据亚细胞定位分离基因，正交轴编码蛋白质-蛋白质相互作用网络，并在一个紧凑的子空间中区分转录因子与其靶基因。这项工作深入分析了Transformer模型在单细胞生物学数据上学习到的可解释的内部表示，揭示了模型如何内化细胞组织的知识。这直接关联到“化学大模型”（此处为生物领域的Transformer模型）的可解释性和内部工作机制研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell foundation models such as scGPT learn high-dimensional gene representations, but what biological knowledge these representations encode remains unclear. We systematically decode the geometric structure of scGPT internal representations through 63 iterations of automated hypothesis screening (183 hypotheses tested), revealing that the model organizes genes into a structured biological coordinate system rather than an opaque feature space. The dominant spectral axis separates genes by subcellular localization, with secreted proteins at one pole and cytosolic proteins at the other. Intermediate transformer layers transiently encode mitochondrial and ER compartments in a sequence that mirrors the cellular secretory pathway. Orthogonal axes encode protein-protein interaction networks with graded fidelity to experimentally measured interaction strength (Spearman rho = 1.000 across n = 5 STRING confidence quintiles, p = 0.017). In a compact six-dimensional spectral subspace, the model distinguishes transcription factors from their target genes (AUROC = 0.744, all 12 layers significant). Early layers preserve which specific genes regulate which targets, while deeper layers compress this into a coarser regulator versus regulated distinction. Repression edges are geometrically more prominent than activation edges, and B-cell master regulators BATF and BACH2 show convergence toward the B-cell identity anchor PAX5 across transformer depth. Cell-type marker genes cluster with high fidelity (AUROC = 0.851). Residual-stream geometry encodes biological structure complementary to attention patterns. These results indicate that biological transformers learn an interpretable internal model of cellular organization, with implications for regulatory network inference, drug target prioritization, and model auditing.

</details>

---

### 23. [Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)](https://arxiv.org/abs/2602.22248)

**基本信息**

- 🔗 arXiv: [`2602.22248`](https://arxiv.org/abs/2602.22248)
- 👥 作者: Julia Gonski, Jenni Ott, Shiva Abbaszadeh 等100人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22248.pdf)

**💡 相关性分析**

满足标准3：论文是一份前瞻性的白皮书/综述，广泛讨论了机器学习在科学计算（包括可能涉及化学数据的领域）与新型硬件（边缘、量子）结合的应用、挑战和机遇，包含了与构建和处理大型科学模型及数据相关的重要讨论。

**📖 中文摘要**

这篇论文题为《Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)》。这是一份关于在高能物理实验中应用机器学习、边缘计算和量子硬件等新兴技术的白皮书。它概述了社区驱动的愿景，旨在识别和优先考虑基于硬件的ML系统及其物理应用的研究和开发机会。虽然主要针对粒子物理，但其中讨论的许多挑战和技术（如低功耗边缘AI、异构加速器、量子算法、模拟计算等）与处理大型科学数据（包括可能的化学或质谱数据）的通用高性能计算和智能信息学框架高度相关。论文强调了AI/ML与新型硬件协同设计对于应对未来科学实验数据挑战的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The next generation of particle physics experiments will face a new era of challenges in data acquisition, due to unprecedented data rates and volumes along with extreme environments and operational constraints. Harnessing this data for scientific discovery demands real-time inference and decision-making, intelligent data reduction, and efficient processing architectures beyond current capabilities. Crucial to the success of this experimental paradigm are several emerging technologies, such as artificial intelligence and machine learning (AI/ML) and silicon microelectronics, and the advent of quantum algorithms and processing. Their intersection includes areas of research such as low-power and low-latency devices for edge computing, heterogeneous accelerator systems, reconfigurable hardware, novel codesign and synthesis strategies, readout for cryogenic or high-radiation environments, and analog computing. This white paper presents a community-driven vision to identify and prioritize research and development opportunities in hardware-based ML systems and corresponding physics applications, contributing towards a successful transition to the new data frontier of fundamental science.

</details>

---

### 24. [Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486)

**基本信息**

- 🔗 arXiv: [`2602.22486`](https://arxiv.org/abs/2602.22486)
- 👥 作者: Shivam Kumar, Yixin Wang, Lizhen Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22486.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕生成模型（化学大模型的一个关键应用方向）的理论分析展开，特别是针对分子结构生成等场景，探讨了模型在低维流形数据上的适应性，与'化学大模型'主题直接相关。

**📖 中文摘要**

本文从理论角度分析了流匹配（Flow Matching）方法在目标分布支撑于低维流形时的性质。流匹配是一种免模拟的生成建模方法，通过学习源分布（如标准正态分布）与目标数据分布之间的插值路径上的速度场来生成样本。论文指出，尽管流匹配方法在文本到图像合成、视频生成和分子结构生成等高维数据集中表现出色，但现有理论分析通常假设目标分布具有平滑的全维密度，未能解释其在流形支撑数据上的有效性。为此，作者建立了当目标分布支撑于光滑流形时，流匹配方法中学习到的速度场的非渐近收敛保证，并将此估计误差通过常微分方程传播，得到了由流匹配目标诱导的隐式密度估计器的统计一致性。最终证明其收敛速率接近极小极大最优，且仅依赖于内在维度，反映了流形和目标分布的光滑性。这些结果为流匹配如何适应数据的内在几何结构并规避维度诅咒提供了原理性解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow matching has emerged as a simulation-free alternative to diffusion-based generative modeling, producing samples by solving an ODE whose time-dependent velocity field is learned along an interpolation between a simple source distribution (e.g., a standard normal) and a target data distribution. Flow-based methods often exhibit greater training stability and have achieved strong empirical performance in high-dimensional settings where data concentrate near a low-dimensional manifold, such as text-to-image synthesis, video generation, and molecular structure generation. Despite this success, existing theoretical analyses of flow matching assume target distributions with smooth, full-dimensional densities, leaving its effectiveness in manifold-supported settings largely unexplained. To this end, we theoretically analyze flow matching with linear interpolation when the target distribution is supported on a smooth manifold. We establish a non-asymptotic convergence guarantee for the learned velocity field, and then propagate this estimation error through the ODE to obtain statistical consistency of the implicit density estimator induced by the flow-matching objective. The resulting convergence rate is near minimax-optimal, depends only on the intrinsic dimension, and reflects the smoothness of both the manifold and the target distribution. Together, these results provide a principled explanation for how flow matching adapts to intrinsic data geometry and circumvents the curse of dimensionality.

</details>

---

### 25. [Discovery of Interpretable Physical Laws in Materials via Language-Model-Guided Symbolic Regression](https://arxiv.org/abs/2602.22967)

**基本信息**

- 🔗 arXiv: [`2602.22967`](https://arxiv.org/abs/2602.22967)
- 👥 作者: Yifeng Guan, Chuyi Liu, Dongzhan Zhou 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22967.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个由大语言模型引导的、用于从材料科学数据中发现物理定律的框架。这直接涉及利用'化学大模型'（此处指大型语言模型作为科学发现的工具）来解决化学信息学中的关键问题，即从数据中推导可解释的模型。

**📖 中文摘要**

本文提出了一种利用大型语言模型（LLM）引导符号回归，从高维数据中发现可解释物理定律的框架。传统符号回归方法在搜索巨大的可能形式空间时，常常产生复杂且不具物理意义的公式。该框架通过利用LLM中嵌入的科学知识来引导搜索过程，从而高效地从数据中识别物理定律。作者通过在钙钛矿材料的关键属性建模上验证了该方法。该方法缓解了传统符号回归中常见的组合爆炸问题，将有效搜索空间减少了约10^5倍。研究识别出了一组关于体模量、带隙和析氧反应活性的新公式，这些公式不仅提供了有意义的物理见解，而且在准确性和简洁性上超越了先前的公式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering interpretable physical laws from high-dimensional data is a fundamental challenge in scientific research. Traditional methods, such as symbolic regression, often produce complex, unphysical formulas when searching a vast space of possible forms. We introduce a framework that guides the search process by leveraging the embedded scientific knowledge of large language models, enabling efficient identification of physical laws in the data. We validate our approach by modeling key properties of perovskite materials. Our method mitigates the combinatorial explosion commonly encountered in traditional symbolic regression, reducing the effective search space by a factor of approximately $10^5$. A set of novel formulas for bulk modulus, band gap, and oxygen evolution reaction activity are identified, which not only provide meaningful physical insights but also outperform previous formulas in accuracy and simplicity.

</details>

---

### 26. [Efficient Graph Coloring with Neural Networks: A Physics-Inspired Approach for Large Graphs](https://arxiv.org/abs/2408.01503)

**基本信息**

- 🔗 arXiv: [`2408.01503`](https://arxiv.org/abs/2408.01503)
- 👥 作者: Lorenzo Colantonio, Andrea Cacioppo, Federico Scarpati 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2408.01503.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种结合图神经网络和物理原理的框架来解决图着色问题。虽然应用领域是组合优化，但其核心方法（图神经网络与生成式/推断框架的结合）与构建用于复杂化学系统（如分子图）推理和生成的'化学大模型'在方法论上高度相关。

**📖 中文摘要**

本文介绍了一个受物理学启发的神经框架，该框架结合图神经网络和统计力学原理，学习解决大规模图着色问题。图着色是约束满足问题的典型代表，表现出尖锐的动态和可满足性阈值。该框架整合了基于种植的监督信号、对称破缺正则化和迭代噪声退火神经动力学，以导航聚集的解空间。当迭代次数与图规模呈二次方增长时，学习到的求解器在随机图中能达到接近理论动态阈值的性能，并在种植推断机制中实现接近最优的检测性能。该模型能够从小型训练图泛化到规模大几个数量级的实例，证明了神经架构可以学习到在组合优化和推断的硬连通区域仍然有效的可扩展算法策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Combinatorial optimization problems near algorithmic phase transitions represent a fundamental challenge for both classical algorithms and machine learning approaches. Among them, graph coloring stands as a prototypical constraint satisfaction problem exhibiting sharp dynamical and satisfiability thresholds. Here we introduce a physics-inspired neural framework that learns to solve large-scale graph coloring instances by combining graph neural networks with statistical-mechanics principles. Our approach integrates a planting-based supervised signal, symmetry-breaking regularization, and iterative noise-annealed neural dynamics to navigate clustered solution landscapes. When the number of iterations scales quadratically with graph size, the learned solver reaches algorithmic thresholds close to the theoretical dynamical transition in random graphs and achieves near-optimal detection performance in the planted inference regime. The model generalizes from small training graphs to instances orders of magnitude larger, demonstrating that neural architectures can learn scalable algorithmic strategies that remain effective in hard connectivity regions. These results establish a general paradigm for learning neural solvers that operate near fundamental phase boundaries in combinatorial optimization and inference.

</details>

---

### 27. [Neuro-Symbolic AI for Analytical Solutions of Differential Equations](https://arxiv.org/abs/2502.01476)

**基本信息**

- 🔗 arXiv: [`2502.01476`](https://arxiv.org/abs/2502.01476)
- 👥 作者: Orestis Oikonomou, Levi Lingsch, Dana Grund 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.01476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个神经符号框架（SIGS），用于自动发现微分方程的解析解。该方法结合了形式语法（符号）和连续空间搜索（神经），是构建用于科学发现（包括化学动力学、分子模拟等领域）的'化学大模型'的一种前沿方法学探索。

**📖 中文摘要**

本文介绍了SIGS，一个用于自动求解微分方程解析解的神经符号框架。微分方程的解析解能提供精确、可解释的洞察，但很少可用，因为发现它们需要专家直觉或在组合空间中进行穷举搜索。SIGS使用形式语法仅生成语法有效的构建块，将这些表达式嵌入连续空间，然后通过最小化基于物理的残差，在该空间中搜索、评分和细化候选的闭式解。该设计将符号推理与数值优化相统一；语法确保候选解块在构造上是正确的，而潜在搜索使探索易于处理且无需数据。SIGS是第一个能够（i）解析求解非线性偏微分方程耦合系统，（ii）在语法未完全指定的情况下发现解，以及（iii）为缺乏已知闭式解的偏微分方程产生精确符号近似的神经符号方法。总体而言，SIGS在标准基准测试上，相比现有的符号方法，在准确性和效率上实现了数量级的提升。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Analytical solutions to differential equations offer exact, interpretable insight but are rarely available because discovering them requires expert intuition or exhaustive search in combinatorial spaces. We introduce SIGS, a neuro-symbolic framework that automates this process. SIGS uses a formal grammar to generate only syntactically valid building blocks, embeds these expressions into a continuous space, and then searches this space to assemble, score, and refine candidate closed-form solutions by minimizing a physics-based residual. This design unifies symbolic reasoning with numerical optimization; the grammar constrains candidate solution blocks to be proper by construction, while the latent search makes exploration tractable and data-free. SIGS is the first neuro-symbolic method to (i) analytically solve coupled systems of nonlinear PDEs, (ii) discover solutions under grammar misspecification, and (iii) produce accurate symbolic approximations for PDEs lacking known closed-form solutions. Overall, SIGS achieves orders-of-magnitude improvements in accuracy and efficiency over existing symbolic methods on standard benchmarks.

</details>

---

### 28. [CLIP-Free, Label Free, Unsupervised Concept Bottleneck Models](https://arxiv.org/abs/2503.10981)

**基本信息**

- 🔗 arXiv: [`2503.10981`](https://arxiv.org/abs/2503.10981)
- 👥 作者: Fawaz Sammani, Jonas Fischer, Nikos Deligiannis
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.10981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的、无需外部模型（CLIP）和标注的概念瓶颈模型。概念瓶颈模型旨在提高模型的可解释性，这是构建可靠、可解释的'化学大模型'（例如用于性质预测或反应推理）的一个重要研究方向。该方法在提升模型可解释性方面的创新与化学信息学中模型透明化的需求直接相关。

**📖 中文摘要**

本文提出了一种无需CLIP模型、无需图像-概念标注、且能以无监督方式推导线性分类器的概念瓶颈模型（CBM）构建方法。概念瓶颈模型将密集特征表示映射到人类可解释的概念，然后线性组合这些概念进行预测。现有CBM依赖CLIP模型获取图像-概念标注，或需要人工标注。本文方法通过将任何冻结的视觉分类器的分布（在离散类别索引上）与其对应的、从文本类别名称导出的视觉-语言对应分布对齐，同时保持分类器的性能，从而将其转换为CBM。该方法不需要真实图像-类别标注，数据效率高，并保留了分类器的推理过程。在超过40个视觉分类器上的应用和测试表明，所得到的无监督、无标签、无CLIP的CBM（U-F^2-CBM）达到了新的最先进水平，甚至超过了有监督的基于CLIP的CBM。作者还展示了该方法可用于零样本图像描述，性能优于基于CLIP的现有方法，达到最先进水平。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) map dense feature representations into human-interpretable concepts which are then combined linearly to make a prediction. However, modern CBMs rely on the CLIP model to obtain image-concept annotations, and it remains unclear how to design CBMs without the CLIP bottleneck. Methods that do not use CLIP instead require manual, labor intensive annotation to associate feature representations with concepts. Furthermore, all CBMs necessitate training a linear classifier to map the extracted concepts to class labels. In this work, we lift all three limitations simultaneously by proposing a method that converts any frozen visual classifier into a CBM without requiring image-concept labels (label-free), without relying on the CLIP model (CLIP-free), and by deriving the linear classifier in an unsupervised manner. Our method is formulated by aligning the original classifier's distribution (over discrete class indices) with its corresponding vision-language counterpart distribution derived from textual class names, while preserving the classifier's performance. The approach requires no ground-truth image-class annotations, and is highly data-efficient and preserves the classifier's reasoning process. Applied and tested on over 40 visual classifiers, our resulting unsupervised, label-free and CLIP-free CBM (U-F$^2$-CBM) sets a new state of the art, surpassing even supervised CLIP-based CBMs. We also show that our method can be used for zero-shot image captioning, outperforming existing methods based on CLIP, and achieving state-of-art.

</details>

---

### 29. [The Spacetime of Diffusion Models: An Information Geometry Perspective](https://arxiv.org/abs/2505.17517)

**基本信息**

- 🔗 arXiv: [`2505.17517`](https://arxiv.org/abs/2505.17517)
- 👥 作者: Rafał Karczewski, Markus Heinonen, Alison Pouplin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.17517.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散模型的几何结构展开，而扩散模型是构建化学大模型（用于分子生成、性质预测等）和进行质谱结构推理（如通过生成模型推断分子结构）的关键底层技术之一。论文对扩散模型潜在空间几何性质的深入分析，直接关联到如何更好地利用这类模型进行化学数据的表示与生成。

**📖 中文摘要**

本文从信息几何的角度为扩散模型的潜在空间提供了一个新颖的几何视角。作者指出，传统的基于确定性概率流ODE解码器的回拉方法存在根本性缺陷，因为它强制要求测地线在数据空间中解码为直线段，从而忽略了数据本身的内在几何结构。作为补充，扩散模型也允许通过反向SDE进行随机解码，这使得可以使用Fisher-Rao度量进行信息几何处理。然而，选择x_T作为潜在表示会导致该度量坍缩。为了解决这个问题，作者引入了一个潜在时空z=(x_t, t)，该时空索引了所有噪声尺度下的去噪分布族p(x_0 | x_t)，从而产生了一个非平凡的几何结构。作者证明了这些分布形成了一个指数族，并推导了曲线长度的无模拟估计器，从而实现了高效的测地线计算。由此产生的结构引入了一种原则性的扩散编辑距离，其中测地线追踪数据之间噪声和去噪编辑的最小序列。这项工作为理解扩散模型的几何结构提供了理论基础，这对于化学信息学领域（特别是质谱分析）中利用扩散模型进行分子生成、结构推理和路径采样等任务具有重要启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a novel geometric perspective on the latent space of diffusion models. We first show that the standard pullback approach, utilizing the deterministic probability flow ODE decoder, is fundamentally flawed. It provably forces geodesics to decode as straight segments in data space, effectively ignoring any intrinsic data geometry beyond the ambient Euclidean space. Complementing this view, diffusion also admits a stochastic decoder via the reverse SDE, which enables an information geometric treatment with the Fisher-Rao metric. However, a choice of $x_T$ as the latent representation collapses this metric due to memorylessness. We address this by introducing a latent spacetime $z=(x_t,t)$ that indexes the family of denoising distributions $p(x_0 | x_t)$ across all noise scales, yielding a nontrivial geometric structure. We prove these distributions form an exponential family and derive simulation-free estimators for curve lengths, enabling efficient geodesic computation. The resulting structure induces a principled Diffusion Edit Distance, where geodesics trace minimal sequences of noise and denoise edits between data. We also demonstrate benefits for transition path sampling in molecular systems, including constrained variants such as low-variance transitions and region avoidance. Code is available at: this https URL .

</details>

---

### 30. [Knowledge Fusion of Large Language Models Via Modular SkillPacks](https://arxiv.org/abs/2505.18502)

**基本信息**

- 🔗 arXiv: [`2505.18502`](https://arxiv.org/abs/2505.18502)
- 👥 作者: Guodong Du, Zhuo Li, Xuanning Zhou 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.18502.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型的跨能力迁移与知识融合方法。这直接关系到如何构建和优化面向特定领域（如化学信息学）的“化学大模型”，通过模块化地集成不同来源的知识和技能（例如，结构预测、谱图解析），提升模型的性能和适应性。

**📖 中文摘要**

本文提出了GraftLLM，一种新颖的方法，用于解决大型语言模型（LLM）中的跨能力迁移挑战，该挑战在多任务集成、模型压缩和持续学习等应用中至关重要。GraftLLM将源模型的能力以SkillPack格式存储在目标模型中。这种方法保留了模型的通用能力，减少了参数冲突，并支持无遗忘的持续学习和模型融合。作者采用了一种模块感知的自适应压缩策略来压缩参数更新，在确保高效存储的同时保持任务特定知识。生成的SkillPack作为一种紧凑且可迁移的知识载体，非常适合异构模型融合和持续学习。实验表明，GraftLLM在知识迁移、知识融合和无遗忘学习方面优于现有技术。这项工作为大模型的模块化、可组合能力构建和迁移提供了新思路，这对于构建面向化学或质谱领域的专用大模型（例如，将通用化学知识、谱图解析能力等模块化并迁移到新模型）具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cross-capability transfer is a key challenge in large language model (LLM) research, with applications in multi-task integration, model compression, and continual learning. Recent works like FuseLLM and FuseChat have demonstrated the potential of transferring multiple model capabilities to lightweight models, enhancing adaptability and efficiency, which motivates our investigation into more efficient cross-capability transfer methods. However, existing approaches primarily focus on small, homogeneous models, limiting their applicability. For large, heterogeneous models, knowledge distillation with full-parameter fine-tuning often overlooks the student model's intrinsic capacity and risks catastrophic forgetting, while PEFT methods struggle to effectively absorb knowledge from source LLMs. To address these issues, we introduce GraftLLM, a novel method that stores source model capabilities in a target model with SkillPack format. This approach preserves general capabilities, reduces parameter conflicts, and supports forget-free continual learning and model fusion. We employ a module-aware adaptive compression strategy to compress parameter updates, ensuring efficient storage while maintaining task-specific knowledge. The resulting SkillPack serves as a compact and transferable knowledge carrier, ideal for heterogeneous model fusion and continual learning. Experiments across various scenarios demonstrate that GraftLLM outperforms existing techniques in knowledge transfer, knowledge fusion, and forget-free learning, providing a scalable and efficient solution for cross-capability transfer. The code is publicly available at: this https URL .

</details>

---

### 31. [Random Matrix Theory-guided sparse PCA for single-cell RNA-seq data](https://arxiv.org/abs/2509.15429)

**基本信息**

- 🔗 arXiv: [`2509.15429`](https://arxiv.org/abs/2509.15429)
- 👥 作者: Victor Chardès
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.15429.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的数据处理和特征提取方法（基于RMT的稀疏PCA），并展示了其在生物医学高维数据（单细胞RNA-seq）上的有效性。这种方法作为一种通用的数据预处理和特征工程工具，可以应用于化学信息学和质谱分析领域，用于处理高维质谱数据或分子描述符数据，提取关键特征以用于后续的化学大模型训练或质谱结构推理。

**📖 中文摘要**

本文提出了一种基于随机矩阵理论（RMT）的稀疏主成分分析（PCA）方法，用于处理单细胞RNA-seq数据。单细胞RNA-seq数据噪声高、维度高，传统的PCA在高维情况下存在偏差。作者的方法首先引入了一种新颖的双白化算法，该算法能够自洽地估计每个基因在每个细胞中的转录组噪声大小，而无需假设特定的噪声分布。这使得能够使用基于RMT的标准自动选择稀疏度水平，从而使稀疏PCA几乎无需参数调整。这种基于数学的方法保留了PCA的可解释性，同时能够稳健、自动地推断稀疏主成分。在七种单细胞RNA-seq技术和四种稀疏PCA算法上的实验表明，该方法系统地改善了主成分子空间的重建，并在细胞类型分类任务中 consistently 优于基于PCA、自编码器和扩散的方法。该方法为高维、噪声数据的降维和特征提取提供了强大的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell RNA-seq provides detailed molecular snapshots of individual cells but is notoriously noisy. Variability stems from biological differences and technical factors, such as amplification bias and limited RNA capture efficiency, making it challenging to adapt computational pipelines to heterogeneous datasets or evolving technologies. As a result, most studies still rely on principal component analysis (PCA) for dimensionality reduction, valued for its interpretability and robustness, in spite of its known bias in high dimensions. Here, we improve upon PCA with a Random Matrix Theory (RMT)-based approach that guides the inference of sparse principal components using existing sparse PCA algorithms. We first introduce a novel biwhitening algorithm which self-consistently estimates the magnitude of transcriptomic noise affecting each gene in individual cells, without assuming a specific noise distribution. This enables the use of an RMT-based criterion to automatically select the sparsity level, rendering sparse PCA nearly parameter-free. Our mathematically grounded approach retains the interpretability of PCA while enabling robust, hands-off inference of sparse principal components. Across seven single-cell RNA-seq technologies and four sparse PCA algorithms, we show that this method systematically improves the reconstruction of the principal subspace and consistently outperforms PCA-, autoencoder-, and diffusion-based methods in cell-type classification tasks.

</details>

---

### 32. [G-reasoner: Foundation Models for Unified Reasoning over Graph-structured Knowledge](https://arxiv.org/abs/2509.24276)

**基本信息**

- 🔗 arXiv: [`2509.24276`](https://arxiv.org/abs/2509.24276)
- 👥 作者: Linhao Luo, Zicheng Zhao, Junnan Liu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24276.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建能够对图结构知识进行推理的基础模型框架。在化学信息学中，分子结构、反应网络、化合物-靶点相互作用等天然地以图的形式存在。G-reasoner这类框架为构建能够理解和推理化学图知识的“化学大模型”提供了重要的技术路径和架构参考，直接服务于基于图表示的分子性质预测、反应结果推理和质谱谱图与分子结构关联等任务。

**📖 中文摘要**

本文提出了G-reasoner，一个统一的框架，将图基础模型和语言基础模型集成起来，用于对多样化图结构知识进行可扩展的推理。大型语言模型在复杂推理方面表现出色，但受限于静态和不完整的参数化知识。检索增强生成通过整合外部知识来缓解这一问题，但现有的方法由于信息碎片化和知识结构建模薄弱，在处理知识密集型任务时仍存在困难。图提供了一种对知识内部关系进行建模的自然方式。G-reasoner的核心是QuadGraph，一个标准化的四层抽象，将异构知识源统一为通用的图表示。在此基础上，作者引入了一个3400万参数的图基础模型，该模型联合捕获图拓扑和文本语义，并与LLMs集成以增强下游应用中的推理能力。在六个基准测试上的大量实验表明，G-reasoner consistently 优于最先进的基线方法，显著增强了LLM的推理能力，并实现了强大的效率和跨图泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) excel at complex reasoning but remain limited by static and incomplete parametric knowledge. Retrieval-augmented generation (RAG) mitigates this by incorporating external knowledge, yet existing RAGs struggle with knowledge-intensive tasks due to fragmented information and weak modeling of knowledge structure. Graphs offer a natural way to model relationships within knowledge, but LLMs are inherently unstructured and cannot effectively reason over graph-structured data. Recent graph-enhanced RAG (GraphRAG) attempts to bridge this gap by constructing tailored graphs and enabling LLMs to reason on them. However, these methods often depend on ad-hoc graph designs, heuristic search, or costly agent pipelines, which hinder scalability and generalization. To address these challenges, we present G-reasoner, a unified framework that integrates graph and language foundation models for scalable reasoning over diverse graph-structured knowledge. Central to our approach is QuadGraph, a standardized four-layer abstraction that unifies heterogeneous knowledge sources into a common graph representation. Building on this, we introduce a 34M-parameter graph foundation model (GFM) that jointly captures graph topology and textual semantics, and is integrated with LLMs to enhance reasoning in downstream applications. To ensure scalability and efficiency, mixed-precision training and distributed message-passing are implemented to scale GFM with more GPUs. Extensive experiments on six benchmarks show that G-reasoner consistently outperforms state-of-the-art baselines, significantly enhances LLM reasoning, and achieves strong efficiency and cross-graph generalization.

</details>

---

### 33. [Object-Centric Representation Learning for Enhanced 3D Semantic Scene Graph Prediction](https://arxiv.org/abs/2510.04714)

**基本信息**

- 🔗 arXiv: [`2510.04714`](https://arxiv.org/abs/2510.04714)
- 👥 作者: KunHo Heo, GiHyun Kim, SuYeon Kim 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04714.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的对象特征编码器和对比预训练策略，用于提升3D场景理解任务的性能。这种专注于学习高质量、可区分对象表示的方法，可以迁移到化学信息学领域。例如，在质谱结构推理中，可以将质谱峰或碎片离子视为“对象”，学习其表示以推断它们之间的结构关系（如连接性），从而构建分子的“场景图”。论文提供的方法论对改进质谱数据的表示学习具有参考价值。

**📖 中文摘要**

本文专注于3D语义场景图预测任务，旨在检测3D场景中的对象及其语义关系。作者通过广泛分析发现，对象特征的质量在决定整体场景图准确性方面起着关键作用。为了解决这一挑战，作者设计了一个高度区分性的对象特征编码器，并采用了一种对比预训练策略，将对象表示学习与场景图预测解耦。这种设计不仅提高了对象分类的准确性，还直接改善了关系预测。当将预训练的编码器插入现有框架时，在所有评估指标上都观察到了显著的性能提升。此外，作者有效地结合了几何和语义特征来实现更优的关系预测。在3DSSG数据集上的综合实验表明，该方法显著优于先前最先进的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

3D Semantic Scene Graph Prediction aims to detect objects and their semantic relationships in 3D scenes, and has emerged as a crucial technology for robotics and AR/VR applications. While previous research has addressed dataset limitations and explored various approaches including Open-Vocabulary settings, they frequently fail to optimize the representational capacity of object and relationship features, showing excessive reliance on Graph Neural Networks despite insufficient discriminative capability. In this work, we demonstrate through extensive analysis that the quality of object features plays a critical role in determining overall scene graph accuracy. To address this challenge, we design a highly discriminative object feature encoder and employ a contrastive pretraining strategy that decouples object representation learning from the scene graph prediction. This design not only enhances object classification accuracy but also yields direct improvements in relationship prediction. Notably, when plugging in our pretrained encoder into existing frameworks, we observe substantial performance improvements across all evaluation metrics. Additionally, whereas existing approaches have not fully exploited the integration of relationship information, we effectively combine both geometric and semantic features to achieve superior relationship prediction. Comprehensive experiments on the 3DSSG dataset demonstrate that our approach significantly outperforms previous state-of-the-art methods. Our code is publicly available at this https URL .

</details>

---

### 34. [Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics](https://arxiv.org/abs/2601.22123)

**基本信息**

- 🔗 arXiv: [`2601.22123`](https://arxiv.org/abs/2601.22123)
- 👥 作者: Winfried Ripken, Michael Plainer, Gregor Lied 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22123.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发用于分子系统（化学信息学的核心领域）的新型机器学习框架，这与“化学大模型”主题直接相关，旨在实现高效、稳定的模拟。

**📖 中文摘要**

本文提出了一种学习哈密顿流映射的框架，用于分子动力学等哈密顿系统的长时间演化模拟。该方法通过预测选定时间跨度内的平均相空间演化，实现了远超经典积分器稳定性限制的大时间步长更新。其核心是施加了一个“平均流一致性”条件。与先前方法不同，该框架允许在独立相空间样本上进行训练，而无需访问未来状态，从而避免了昂贵的轨迹生成。该方法特别改进了使用机器学习力场的分子动力学模拟，在保持可比较的训练和推理成本的同时，支持显著更大的积分时间步长。这项工作与“化学大模型”主题相关，因为它提出了一种用于分子系统（化学信息学的核心）的新型机器学习框架，该框架能够实现高效、稳定的模拟，这是开发用于化学和材料科学的“大模型”的关键能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn Hamiltonian Flow Maps by predicting the mean phase-space evolution over a chosen time span, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a Mean Flow consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available trajectory-free MLFF datasets.

</details>

---

### 35. [A Minimum Variance Path Principle for Accurate and Stable Score-Based Density Ratio Estimation](https://arxiv.org/abs/2602.00834)

**基本信息**

- 🔗 arXiv: [`2602.00834`](https://arxiv.org/abs/2602.00834)
- 👥 作者: Wei Chen, Jiacheng Li, Shigui Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00834.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进基于分数的生成模型和密度估计方法，这是构建化学领域生成模型（化学大模型）和进行概率推理（如质谱结构推理）的基础技术。

**📖 中文摘要**

本文解决了基于分数的密度比估计方法中的一个核心悖论：理论上路径独立，但实践中路径依赖。作者通过证明实际训练目标与理想目标之间相差一个关键项——分数函数的路径方差，从而解决了这一问题。他们提出了“最小方差路径”原则来最小化此方差，并推导了方差的闭式表达式，使优化变得可行。通过使用灵活的Kumaraswamy混合模型对路径进行参数化，该方法可以学习数据自适应的低方差路径。这种对完整目标的优化产生了更准确和稳定的估计器。这项工作与“化学大模型”和“质谱结构推理”都相关，因为基于分数的生成模型和密度估计是构建化学领域生成模型（如分子生成）和进行概率推理（如从质谱数据推断结构）的核心技术。本文提出的改进方法可以提升这些化学信息学任务的模型性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Score-based methods are powerful across machine learning, but they face a paradox: theoretically path-independent, yet practically path-dependent. We resolve this by proving that practical training objectives differ from the ideal, ground-truth objective by a crucial, overlooked term: the path variance of the score function. We propose the MVP (**M**imum **V**ariance **P**ath) Principle to minimize this path variance. Our key contribution is deriving a closed-form expression for the variance, making optimization tractable. By parameterizing the path with a flexible Kumaraswamy Mixture Model, our method learns data-adaptive, low-variance paths without heuristic manual selection. This principled optimization of the complete objective yields more accurate and stable estimators, establishing new state-of-the-art results on challenging benchmarks and providing a general framework for optimizing score-based interpolation.

</details>

---

### 36. [VQ-Style: Disentangling Style and Content in Motion with Residual Quantized Representations](https://arxiv.org/abs/2602.02334)

**基本信息**

- 🔗 arXiv: [`2602.02334`](https://arxiv.org/abs/2602.02334)
- 👥 作者: Fatemeh Zargarbashi, Dhruv Agrawal, Jakob Buhmann 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.02334.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于RVQ-VAE的层次化解耦表示学习方法，其核心思想与化学信息学中解耦分子核心结构与功能基团的需求高度相关，是构建和理解“化学大模型”内部表示的重要技术路径。

**📖 中文摘要**

本文提出了一种新颖的方法，用于有效解耦人体运动数据中的风格和内容，以促进风格迁移。该方法利用残差向量量化变分自编码器学习从粗到细的运动表示，并通过结合码本学习、对比学习和新颖的信息泄漏损失来增强解耦。作者利用这种解耦表示，提出了一种简单有效的推理时技术“量化码交换”，无需对未见风格进行微调即可实现运动风格迁移。虽然论文应用在人体运动领域，但其核心方法论——使用RVQ-VAE进行层次化表示学习以解耦高级语义（内容）和低级细节（风格）——与化学信息学中分子表示学习的目标高度相似。在化学领域，类似技术可用于解耦分子的核心骨架（内容）和官能团/取代基（风格），这对于分子生成、优化和性质预测至关重要，是“化学大模型”研究的前沿方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Human motion data is inherently rich and complex, containing both semantic content and subtle stylistic features that are challenging to model. We propose a novel method for effective disentanglement of the style and content in human motion data to facilitate style transfer. Our approach is guided by the insight that content corresponds to coarse motion attributes while style captures the finer, expressive details. To model this hierarchy, we employ Residual Vector Quantized Variational Autoencoders (RVQ-VAEs) to learn a coarse-to-fine representation of motion. We further enhance the disentanglement by integrating codebook learning with contrastive learning and a novel information leakage loss to organize the content and the style across different codebooks. We harness this disentangled representation using our simple and effective inference-time technique Quantized Code Swapping, which enables motion style transfer without requiring any fine-tuning for unseen styles. Our framework demonstrates strong versatility across multiple inference applications, including style transfer, style removal, and motion blending.

</details>

---

### 37. [Enabling Large-Scale Channel Sounding for 6G: A Framework for Sparse Sampling and Multipath Component Extraction](https://arxiv.org/abs/2602.05405)

**基本信息**

- 🔗 arXiv: [`2602.05405`](https://arxiv.org/abs/2602.05405)
- 👥 作者: Yi Chen, Ming Li, Chong Han
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.05405.pdf)

**💡 相关性分析**

满足标准1：论文提出的用于从非均匀采样数据中提取多径分量的LR-SAGE算法，其核心方法论与“质谱结构推理”中从复杂质谱信号中解析碎片离子模式的任务直接相关，为解决质谱数据分析中的类似问题提供了新的技术思路。

**📖 中文摘要**

本文提出了一种用于6G大规模信道测量的新框架，涉及稀疏非均匀采样和一种用于多径分量提取的似然校正空间交替广义期望最大化算法。该框架能够在相同测量时间内获取大数十甚至数百倍的信道数据集，为利用AI缩放定律提供所需的海量数据。具体而言，作者提出了抛物线频率采样策略和非均匀采样下的LR-SAGE算法。这项工作与“质谱结构推理”在方法论上高度相关。质谱分析，尤其是串联质谱，其核心任务之一就是从复杂的谱图中提取和解析碎片离子信号（类似于通信中的多径分量），以推断分子结构。本文提出的针对非均匀采样数据的、高效的MPC提取算法（LR-SAGE），其思想可以迁移到质谱数据分析中，用于从高分辨率质谱数据中更鲁棒、更高效地解析出碎片离子峰及其关系，从而辅助“质谱结构推理”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Realizing the 6G vision of artificial intelligence (AI) and integrated sensing and communication (ISAC) critically requires large-scale real-world channel datasets for channel modeling and data-driven AI models. However, traditional frequency-domain channel sounding methods suffer from low efficiency due to a prohibitive number of frequency points to avoid delay ambiguity. This paper proposes a novel channel sounding framework involving sparse nonuniform sampling along with a likelihood-rectified space-alternating generalized expectation-maximization (LR-SAGE) algorithm for multipath component extraction. This framework enables the acquisition of channel datasets that are tens or even hundreds of times larger within the same channel measurement duration, thereby providing the massive data required to harness the full potential of AI scaling laws. Specifically, we propose a Parabolic Frequency Sampling (PFS) strategy that non-uniformly distributes frequency points, effectively eliminating delay ambiguity while reducing sampling overhead by orders of magnitude. To efficiently extract multipath components (MPCs) from the channel data measured by PFS, we develop a LR-SAGE algorithm, rectifying the likelihood distortion caused by nonuniform sampling and molecular absorption effect. Simulation results and experimental validation at 280--300~GHz confirm that the proposed PFS and LR-SAGE algorithm not only achieve 50$\times$ faster measurement, a 98\% reduction in data volume and a 99.96\% reduction in post-processing computational complexity, but also successfully captures MPCs and channel characteristics consistent with traditional exhaustive measurements, demonstrating its potential as a fundamental enabler for constructing the massive ISAC datasets required by AI-native 6G systems.

</details>

---

### 38. [Document Reconstruction Unlocks Scalable Long-Context RLVR](https://arxiv.org/abs/2602.08237)

**基本信息**

- 🔗 arXiv: [`2602.08237`](https://arxiv.org/abs/2602.08237)
- 👥 作者: Yao Xiao, Lei Wang, Yue Deng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.08237.pdf)

**💡 相关性分析**

满足标准1：论文提出的无监督长上下文训练方法（通过文档重建），为解决“化学大模型”中处理长序列化学数据（如蛋白质序列、文献）的核心挑战提供了创新的训练范式和技术思路。

**📖 中文摘要**

本文研究了一种无监督方法来增强大语言模型的长上下文能力，无需昂贵的人工标注或教师模型监督。具体方法是：在一篇长文档中，用特殊占位符替换少数段落，然后通过强化学习训练LLM，通过从一组候选选项中正确识别和排序缺失段落来重建文档。这种训练范式使模型能够捕捉全局叙事连贯性，从而显著提升长上下文性能。该方法在RULER和LongBench v2基准测试上验证了有效性。这项工作与“化学大模型”相关，因为处理长序列化学数据（如长蛋白质序列、高分子聚合物结构、复杂的反应路径描述）是化学领域大模型面临的关键挑战之一。本文提出的通过文档重建任务进行无监督长上下文训练的方法，为训练化学领域大模型处理长序列化学信息（如从长文献中提取反应规则或解析长生物分子序列）提供了新的、可扩展的训练范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards~(RLVR) has become a prominent paradigm to enhance the capabilities (i.e.\ long-context) of Large Language Models~(LLMs). However, it often relies on gold-standard answers or explicit evaluation rubrics provided by powerful teacher models or human experts, which are costly and time-consuming. In this work, we investigate unsupervised approaches to enhance the long-context capabilities of LLMs, eliminating the need for heavy human annotations or teacher models' supervision. Specifically, we first replace a few paragraphs with special placeholders in a long document. LLMs are trained through reinforcement learning to reconstruct the document by correctly identifying and sequencing missing paragraphs from a set of candidate options. This training paradigm enables the model to capture global narrative coherence, significantly boosting long-context performance. We validate the effectiveness of our method on two widely used benchmarks, RULER and LongBench~v2. While acquiring noticeable gains on RULER, it can also achieve a reasonable improvement on LongBench~v2 without any manually curated long-context QA data. Furthermore, we conduct extensive ablation studies to analyze the impact of reward design, data curation strategies, training schemes, and data scaling effects on model performance. We publicly release our code, data, and models.

</details>

---

### 39. [When Less is More: The LLM Scaling Paradox in Context Compression](https://arxiv.org/abs/2602.09789)

**基本信息**

- 🔗 arXiv: [`2602.09789`](https://arxiv.org/abs/2602.09789)
- 👥 作者: Ruishan Guo, Yibing Liu, Guoxin Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.09789.pdf)

**💡 相关性分析**

满足标准1：论文深入研究了大型语言模型在上下文压缩任务中的“尺寸-保真度悖论”，其发现和机理分析（知识覆盖、语义漂移）对于理解和评估“化学大模型”在压缩化学知识并保持推理忠实性方面的能力具有直接的相关性和重要的指导意义。

**📖 中文摘要**

本文研究了在压缩器-解码器设置下的有损上下文压缩中出现的“尺寸-保真度悖论”：增加压缩器的大小可能会降低重建上下文的忠实度，尽管训练损失在下降。通过对从0.6B到90B的模型进行广泛实验，作者将这一悖论归因于两个主要因素：1）知识覆盖：更大的模型越来越多地用其先验信念替换源事实；2）语义漂移：更大的模型倾向于意译或重组内容，而不是逐字复现。通过固定模型大小，作者反思了压缩上下文表示的涌现特性。这项工作与“化学大模型”高度相关。在化学领域，大模型经常被用于压缩和表示复杂的化学知识（如分子结构、反应规则），然后用于下游推理（如逆合成规划、性质预测）。本文揭示的“尺寸-保真度悖论”及其机理（知识覆盖、语义漂移），对于理解和评估化学大模型在知识压缩与忠实重建方面的能力具有重要启示，有助于设计更可靠、更忠实的化学知识表示与推理模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling up model parameters has long been a prevalent training paradigm driven by the assumption that larger models yield superior generation capabilities. However, under lossy context compression in a compressor-decoder setup, we observe a Size-Fidelity Paradox: increasing the compressor size can lessen the faithfulness of reconstructed contexts though training loss decreases. Through extensive experiments across models from 0.6B to 90B, we coin this paradox arising from two dominant factors: 1) knowledge overwriting: larger models increasingly replace source facts with their own prior beliefs, e.g., ``the white strawberry'' $\to$ ``the red strawberry''; and 2) semantic drift: larger models tend to paraphrase or restructure content instead of reproducing it verbatim, e.g., ``Alice hit Bob'' $\to$ ``Bob hit Alice''. By holding model size fixed, we reflect on the emergent properties of compressed context representations. We show that the culprit is not parameter count itself, but the excessive semantic capacity and amplified generative uncertainty that accompany scaling. Specifically, the increased rank of context embeddings facilitates prior knowledge intrusion, whereas higher entropy over token prediction distributions promotes rewriting. Our results complement existing evaluations over context compression paradigm, underpinning a breakdown in scaling laws for faithful preservation in open-ended generation.

</details>

---

### 40. [Versor: A Geometric Sequence Architecture](https://arxiv.org/abs/2602.10195)

**基本信息**

- 🔗 arXiv: [`2602.10195`](https://arxiv.org/abs/2602.10195)
- 👥 作者: Truong Minh Huy, Edward Hirst
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10195.pdf)

**💡 相关性分析**

满足标准1：论文提出的Versor架构原生支持SE(3)等变性，并提供了强大的几何关系建模工具，这与“化学大模型”（用于分子三维结构建模）和“质谱结构推理”（涉及三维空间中的化学键断裂）的核心需求直接相关，为这些领域提供了创新的模型架构选择。

**📖 中文摘要**

本文介绍了一种新颖的序列架构Versor，它使用共形几何代数代替传统的线性操作，以实现结构泛化并在多种任务上获得显著的性能提升。Versor将状态嵌入Cl_{4,1}流形并通过几何变换演化它们，原生表示SE(3)等变关系。该模型在混沌N体动力学、拓扑推理和多模态基准测试上进行了验证。这项工作与“化学大模型”和“质谱结构推理”都高度相关。首先，Versor原生支持SE(3)等变性，这是分子建模（如分子构象、蛋白质结构）和质谱推理（涉及三维空间中的碎片化过程）的关键属性。其次，其几何积注意力机制和递归转子累加器为建模分子内原子间的复杂空间关系和质谱碎片离子的生成路径提供了强大的新工具。Versor展示的卓越的OOD泛化能力和可解释性，使其成为开发下一代化学和质谱分析基础模型的极具潜力的架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A novel sequence architecture is introduced, Versor, which uses Conformal Geometric Algebra (CGA) in place of traditional linear operations to achieve structural generalization and significant performance improvements on a variety of tasks, while offering improved interpretability and efficiency. By embedding states in the $Cl_{4,1}$ manifold and evolving them via geometric transformations (rotors), Versor natively represents $SE(3)$-equivariant relationships without requiring explicit structural encoding. Versor is validated on chaotic N-body dynamics, topological reasoning, and standard multimodal benchmarks (CIFAR-10, WikiText-103), consistently outperforming Transformers, Graph Networks, and geometric baselines (GATr, EGNN). Key results include: orders-of-magnitude fewer parameters ($200\times$ vs. Transformers); interpretable attention decomposing into proximity and orientational components; zero-shot scale generalization (0.993 vs. 0.070 MCC for ViT); and featuring a Recursive Rotor Accumulator (RRA) for $O(L)$ linear temporal complexity in dynamical systems, and a Geometric Product Attention (GPA) mechanism for $O(L^{2})$ global relational modeling, allowing for task-specific architectural pruning or hybridization depending on the required scale. In out-of-distribution tests, Versor maintains stable predictions while Transformers fail catastrophically. Custom Clifford kernels achieve a cumulative over $100\times$ speedup via bit-masked contraction and specialized Matrix Isomorphism kernels, reducing per-step latency to 1.05 ms and outperforming highly-optimized Transformer baselines.

</details>

---

### 41. [Symmetry in language statistics shapes the geometry of model representations](https://arxiv.org/abs/2602.15029)

**基本信息**

- 🔗 arXiv: [`2602.15029`](https://arxiv.org/abs/2602.15029)
- 👥 作者: Dhruva Karkada, Daniel J. Korchinski, Andres Nava 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.15029.pdf)

**💡 相关性分析**

满足标准1：论文从数据统计对称性的角度，为语言模型内部表示的几何结构提供了理论解释。这一理论框架可直接应用于分析和设计“化学大模型”的内部表示，因为化学数据本身具有丰富的对称性和几何结构，对于提升模型的可解释性和泛化能力至关重要。

**📖 中文摘要**

本文解释了语言模型内部表示中出现的几何结构（如月份排列成圆、年份形成流形）的起源。作者首先证明语言统计具有平移对称性（例如，任意两个月在文本中共同出现的频率仅取决于它们之间的时间间隔）。他们证明了这种对称性支配着高维词嵌入模型中的这些几何结构，并解析地推导了词表示的流形几何。这些预测与大型文本嵌入模型和大型语言模型的实证结果相匹配。此外，即使相关统计受到扰动，表示几何在中等嵌入维度下仍然保持稳健。这项工作与“化学大模型”高度相关。化学领域的数据（如分子、反应）也蕴含着丰富的对称性和几何结构（如旋转、反射对称性，以及周期表中的周期性）。本文提供的理论框架——从数据统计的对称性推导出表示几何——为理解和设计化学领域大模型的内部表示提供了强大的理论工具。例如，可以研究分子描述符或反应条件在模型表示空间中是否也形成了有意义的几何流形，从而提升模型的可解释性和泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The internal representations learned by language models consistently exhibit striking geometric structure: calendar months organize into a circle, historical years form a smooth one-dimensional manifold, and cities' latitudes and longitudes can be decoded using a linear probe. To explain this neural code, we first show that language statistics exhibit translation symmetry (for example, the frequency with which any two months co-occur in text depends only on the time interval between them). We prove that this symmetry governs these geometric structures in high-dimensional word embedding models, and we analytically derive the manifold geometry of word representations. These predictions empirically match large text embedding models and large language models. Moreover, the representational geometry persists at moderate embedding dimension even when the relevant statistics are perturbed (e.g., by removing all sentences in which two months co-occur). We prove that this robustness emerges naturally when the co-occurrence statistics are controlled by an underlying latent variable. These results suggest that representational manifolds have a universal origin: symmetry in the statistics of natural data.

</details>

---

### 42. [Composable and adaptive design of machine learning interatomic potentials guided by Fisher-information analysis](https://arxiv.org/abs/2504.19372)

**基本信息**

- 🔗 arXiv: [`2504.19372`](https://arxiv.org/abs/2504.19372)
- 👥 作者: Weishi Wang, Mark K. Transtrum, Vincenzo Lordi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.19372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种自适应、可解释的机器学习原子间势（MLIP）设计框架。MLIP是化学信息学和计算化学中用于模拟分子和材料性质的核心“化学大模型”之一。本文提出的策略旨在通过迭代重构和费舍尔信息分析来改进MLIP的设计，直接围绕“化学大模型”的构建、优化和可解释性展开。

**📖 中文摘要**

本文提出了一种用于机器学习原子间势（MLIPs）的自适应、物理启发的模型设计策略。该策略依赖于从单术语模型迭代重构复合模型，并采用统一的训练程序。为了指导模型重构和超参数优化，作者提出了一种基于费舍尔信息矩阵（FIM）和多属性误差度量的模型评估方法。通过结合重构和评估子程序，该框架在灵活性和可扩展性之间取得了平衡。在一个针对结构多样的铌数据集的案例研究中，该框架生成的包含75个参数的最优模型配置，实现了0.172 eV/Å的力RMSE和0.013 eV/atom的能量RMSE。这项工作展示了通过迭代式、信息驱动的模型设计来改进化学信息学中关键工具（MLIPs）的方法，这与开发更智能、更可解释的“化学大模型”的目标高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An adaptive physics-inspired model design strategy for machine-learning interatomic potentials (MLIPs) is proposed. This strategy relies on iterative reconfigurations of composite models from single-term models, followed by a unified training procedure. A model evaluation method based on the Fisher information matrix (FIM) and multiple-property error metrics is also proposed to guide the model reconfiguration and hyperparameter optimization. By combining the reconfiguration and the evaluation subroutines, we provide an adaptive MLIP design strategy that balances flexibility and extensibility. In a case study of designing models against a structurally diverse niobium dataset, we managed to obtain an optimal model configuration with 75 parameters generated by our framework that achieved a force RMSE of 0.172 eV/Å and an energy RMSE of 0.013 eV/atom.

</details>

---

### 43. [Understanding protein function with a multimodal retrieval-augmented foundation model](https://arxiv.org/abs/2508.04724)

**基本信息**

- 🔗 arXiv: [`2508.04724`](https://arxiv.org/abs/2508.04724)
- 👥 作者: Timothy Fei Truong Jr, Tristan Bepler
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.04724.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个名为PoET-2的多模态、检索增强的蛋白质基础模型。蛋白质语言模型（PLMs）是“化学大模型”在生物分子领域的关键应用和前沿方向。本文直接围绕如何构建和提升这类化学大模型的性能（如零样本预测、表示学习）展开，并引入了新的架构和训练范式。

**📖 中文摘要**

本文介绍了PoET-2，一个多模态、检索增强的蛋白质基础模型。该模型结合了家族特异性进化约束的上下文学习以及可选的结构条件，以学习蛋白质序列的生成分布。PoET-2采用分层Transformer编码器（对序列上下文顺序具有等变性）和具有因果与掩码语言建模目标的双解码器架构，使其能够在完全生成和双向表示学习两种模式下运行。PoET-2在零样本变体效应预测上达到了最先进的性能，尤其在评分多重突变和具有挑战性的插入缺失突变方面表现出色。在监督设置下，PoET-2的嵌入在从序列学习功能关系方面优于先前的方法，特别是在小数据集上。这项工作强调了将检索增强与多模态、以家族为中心的建模相结合，对于推进蛋白质基础模型的益处。蛋白质语言模型是“化学大模型”在生物化学和药物发现领域的一个重要子类。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (PLMs) learn probability distributions over natural protein sequences. By learning from hundreds of millions of natural protein sequences, protein understanding and design capabilities emerge. Recent works have shown that scaling these models improves structure prediction, but does not seem to improve mutation understanding and representation quality for protein function prediction. We introduce PoET-2, a multimodal, retrieval-augmented protein foundation model that incorporates in-context learning of family-specific evolutionary constraints with optional structure conditioning to learn generative distributions over protein sequences. PoET-2 uses a hierarchical transformer encoder that is equivariant to sequence context ordering and a dual decoder architecture with both causal and masked language modeling objectives, allowing PoET-2 to operate in both fully generative and bidirectional representation learning modes. PoET-2 achieves state-of-the-art performance on zero-shot variant effect prediction, excelling at scoring variants with multiple mutations and challenging indel mutations. In supervised settings, PoET-2 embeddings outperform previous methods for learning sequence-function relationships, especially with small datasets. This work highlights the benefits of combining retrieval augmentation with multimodal, family-centric modeling for advancing protein foundation models.

</details>

---

### 44. [TokEye: Fast Signal Extraction for Fluctuating Time Series via Offline Self-Supervised Learning From Fusion Diagnostics to Bioacoustics](https://arxiv.org/abs/2602.20317)

**基本信息**

- 🔗 arXiv: [`2602.20317`](https://arxiv.org/abs/2602.20317)
- 👥 作者: Nathaniel Chen, Kouroche Bouchiat, Peter Steiner 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20317.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文提出了一种从高噪声时频数据（谱图）中自动提取相干和瞬态模式的通用框架。质谱数据本质上是质荷比与强度的谱图，其结构推理面临类似的噪声和特征提取挑战。该框架的方法论（自监督学习、信号处理、神经网络代理）可直接类比或应用于质谱解析问题。2) 数据资源/工具相关：论文开发了一个通用工具（TokEye），并提供了代码仓库，可用于处理类似谱图的信号提取任务，这为质谱数据分析提供了潜在的工具资源。

**📖 中文摘要**

本文提出了一个“信号优先”的自监督框架，用于从各种传感器的高噪声时频数据中自动提取相干和瞬态模式。作者开发了一种通用方法和工具，通过在多通道信号处理中采用非线性最优技术，并利用快速神经网络代理，从托卡马克装置（如DIII-D）的快磁、电子回旋辐射、CO2干涉仪和束发射光谱测量中提取相干、准相干和瞬态模式。该框架在DIII-D、TJ-II和非融合谱图数据上进行了测试。推理延迟为0.5秒，使得该框架能够实现实时模式识别和大规模自动化数据库生成，用于先进的等离子体控制。该方法虽然应用于聚变诊断，但其核心是从复杂、高噪声的谱图（一种与质谱图在数学和信号处理上类似的数据形式）中提取特征和模式。这为“质谱结构推理”中从原始谱数据解析出化学结构信息提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Next-generation fusion facilities like ITER face a "data deluge," generating petabytes of multi-diagnostic signals daily that challenge manual analysis. We present a "signals-first" self-supervised framework for the automated extraction of coherent and transient modes from high-noise time-frequency data across a variety of sensors. We also develop a general-purpose method and tool for extracting coherent, quasi-coherent, and transient modes for fluctuation measurements in tokamaks by employing non-linear optimal techniques in multichannel signal processing with a fast neural network surrogate on fast magnetics, electron cyclotron emission, CO2 interferometers, and beam emission spectroscopy measurements from DIII-D. Results are tested on data from DIII-D, TJ-II, and non-fusion spectrograms. With an inference latency of 0.5 seconds, this framework enables real-time mode identification and large-scale automated database generation for advanced plasma control. Repository is in this https URL .

</details>

---

### 45. [Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions](https://arxiv.org/abs/2602.21160)

**基本信息**

- 🔗 arXiv: [`2602.21160`](https://arxiv.org/abs/2602.21160)
- 👥 作者: Mame Diarra Toure, David A. Stephens
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21160.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进贝叶斯深度学习中的认知不确定性量化，提出了一种可解释的逐类不确定性分解方法。对于“化学大模型”和基于机器学习的“质谱结构推理”模型，理解模型在哪些特定化学类别或结构特征上不确定，对于提高预测的可靠性和可解释性至关重要。这项工作直接提供了提升此类模型安全性和可信度的技术路径。

**📖 中文摘要**

在安全关键分类中，失败的代价通常是不对称的，然而贝叶斯深度学习用单一标量——互信息（MI）来总结认知不确定性，这无法区分模型的未知性涉及的是良性类别还是安全关键类别。作者将MI分解为一个逐类向量，该分解源于熵的二阶泰勒展开。通过构造，各分量的和近似等于MI。作者在三个任务上验证了该分解：糖尿病视网膜病变的选择性预测、临床和图像基准上的分布外检测，以及受控的标签噪声研究。在糖尿病视网膜病变任务中，针对关键类别的分解分量将选择性风险相对于MI降低了34.7%，相对于方差基线降低了56.2%。这项工作虽然主要针对通用分类任务，但其核心是改进不确定性量化（UQ）的可解释性。在“化学大模型”和“质谱结构推理”中，模型预测的可信度评估和不确定性分解（例如，区分是对化合物类别还是特定官能团不确定）对于可靠部署至关重要。本文提出的方法为化学信息学中复杂模型的可靠性分析提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In safety-critical classification, the cost of failure is often asymmetric, yet Bayesian deep learning summarises epistemic uncertainty with a single scalar, mutual information (MI), that cannot distinguish whether a model's ignorance involves a benign or safety-critical class. We decompose MI into a per-class vector $C_k(x)=\sigma_k^{2}/(2\mu_k)$, with $\mu_k{=}\mathbb{E}[p_k]$ and $\sigma_k^2{=}\mathrm{Var}[p_k]$ across posterior samples. The decomposition follows from a second-order Taylor expansion of the entropy; the $1/\mu_k$ weighting corrects boundary suppression and makes $C_k$ comparable across rare and common classes. By construction $\sum_k C_k \approx \mathrm{MI}$, and a companion skewness diagnostic flags inputs where the approximation degrades. After characterising the axiomatic properties of $C_k$, we validate it on three tasks: (i) selective prediction for diabetic retinopathy, where critical-class $C_k$ reduces selective risk by 34.7\% over MI and 56.2\% over variance baselines; (ii) out-of-distribution detection on clinical and image benchmarks, where $\sum_k C_k$ achieves the highest AUROC and the per-class view exposes asymmetric shifts invisible to MI; and (iii) a controlled label-noise study in which $\sum_k C_k$ shows less sensitivity to injected aleatoric noise than MI under end-to-end Bayesian training, while both metrics degrade under transfer learning. Across all tasks, the quality of the posterior approximation shapes uncertainty at least as strongly as the choice of metric, suggesting that how uncertainty is propagated through the network matters as much as how it is measured.

</details>

---

## 📊 数据统计
- 累计运行天数：3
- 累计论文数量：134

## 📝 历史记录

> 暂无历史数据

