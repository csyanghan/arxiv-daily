# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-02 01:16:23

## 📅 2026-03-02 (今日最新)

**相关论文数：39**

### 1. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个用于3D分子和材料的统一生成与预测基础模型（Zatom-1），这直接属于“化学大模型”的核心主题。

**📖 中文摘要**

本文介绍了Zatom-1，一个用于3D分子和材料的统一基础模型。该模型是一个Transformer，通过多模态流匹配目标进行训练，联合建模离散原子类型和连续3D几何结构。这种方法支持可扩展的预训练，并能够实现快速稳定的采样。Zatom-1将联合生成式预训练作为下游多任务预测（如性质、能量和力）的通用初始化。该模型在生成和预测基准测试中匹配或超越了专门的基线模型，同时将生成推理时间减少了一个数量级以上。实验表明，联合生成式预训练在化学领域之间产生了正向的预测迁移：在预训练中建模材料提高了分子性质预测的准确性。这篇论文的核心是开发一个用于3D化学建模的通用AI模型，直接属于“化学大模型”的研究范畴。

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

满足标准3：论文提出了一个关于因果模型抽象和嵌入的理论框架，虽然不直接针对化学或质谱，但其关于整合多源、多分辨率模型的核心讨论，对于构建和理解复杂的“化学大模型”以及整合不同质谱数据源进行“结构推理”具有重要的方法论启示和前瞻性讨论价值。

**📖 中文摘要**

本文提出了一个用于因果嵌入的多分辨率框架，作为抽象化的泛化。作者将因果嵌入定义为抽象化的推广，并提出了一种广义的一致性概念。通过定义一个多分辨率边际问题，展示了因果嵌入对于统计边际问题和因果边际问题的相关性。该框架允许将多个详细模型映射到一个更粗糙因果模型的子系统中。这项工作为在具有不同表示的模型之间合并数据集提供了理论基础。虽然论文本身是理论性的，但它为理解和整合来自不同来源（例如，可能来自不同质谱实验或化学信息学模型）的因果或统计模型提供了一个通用框架，这对于构建更健壮、可解释的化学大模型或质谱结构推理系统具有潜在价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Abstractions of causal models allow for the coarsening of models such that relations of cause and effect are preserved. Whereas abstractions focus on the relation between two models, in this paper we study a framework for causal embeddings which enable multiple detailed models to be mapped into sub-systems of a coarser causal model. We define causal embeddings as a generalization of abstraction, and present a generalized notion of consistency. By defining a multi-resolution marginal problem, we showcase the relevance of causal embeddings for both the statistical marginal problem and the causal marginal problem; furthermore, we illustrate its practical use in merging datasets coming from models with different representations.

</details>

---

### 3. [A Reduced Order Model approach for First-Principles Molecular Dynamics Computations](https://arxiv.org/abs/2602.22390)

**基本信息**

- 🔗 arXiv: [`2602.22390`](https://arxiv.org/abs/2602.22390)
- 👥 作者: Siu Wun Cheung, Youngsoo Choi, Jean-Luc Fattebert 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22390.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一种数据驱动的降阶模型方法，用于加速第一性原理分子动力学中的Kohn-Sham DFT计算。这直接属于计算化学和“化学信息学”中构建高效、可扩展计算模型的核心主题，是构建复杂化学模拟“大模型”的基础技术之一。

**📖 中文摘要**

为了利用第一性原理分子动力学每一步计算出的电子结构之间的冗余性，本文提出了一种用于Kohn-Sham密度泛函理论的数据驱动建模框架，绕过了对电子波函数的显式优化。该方法先验地采样具有代表性的原子构型，并构建一个低维基，以高效近似电子结构子空间。随后，在电子单粒子密度矩阵的直接求解器中使用这个约化基，从而无需迭代波函数优化即可有效确定基态。作者在一个水分子的玻恩-奥本海默分子动力学中证明了该方法的有效性，表明由此产生的模拟能准确复现从完整第一性原理分子动力学获得的关键结构性质（如键长和键角）。这项工作突出了数据驱动方法为第一性原理模拟开发高效电子结构求解器的潜力。这篇论文的核心是应用降阶模型和数据驱动方法加速量子化学计算，这是“化学信息学”和计算化学中构建高效、可扩展模型（可视为特定领域的“化学大模型”基础）的关键技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To leverage the redundancy between the electronic structure computed at each step of first-principles molecular dynamics, we present a data-driven modeling framework for Kohn-Sham Density Functional Theory that bypasses the explicit optimization of electronic wavefunctions. We sample a priori representative atomic configurations and construct a low-dimensional basis that efficiently approximates the electronic structure subspace. Subsequently, we employ this reduced basis in a direct solver for the electronic single particle density matrix, thereby enabling the efficient determination of ground state without iterative wavefunction optimization. We demonstrate the efficacy of our approach in a Born-Oppenheimer molecular dynamics of a water molecule, showing that the resulting simulations accurately reproduce key structural properties, such as bond lengths and bond angle, obtained from full first-principles molecular dynamics. This work highlights the potential of data-driven approaches to develop efficient electronic structure solvers for first-principles simulations.

</details>

---

### 4. [MolFM-Lite: Multi-Modal Molecular Property Prediction with Conformer Ensemble Attention and Cross-Modal Fusion](https://arxiv.org/abs/2602.22405)

**基本信息**

- 🔗 arXiv: [`2602.22405`](https://arxiv.org/abs/2602.22405)
- 👥 作者: Syed Omer Shah, Mohammed Maqsood Ahmed, Danish Mohiuddin Mohammed 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22405.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（多模态分子表示学习与融合）是构建化学大模型的关键组成部分。其方法直接涉及如何整合和处理化学数据的多种表示形式，这对于开发能够理解分子结构、性质和功能的化学大模型至关重要。

**📖 中文摘要**

本文提出了MolFM-Lite，一个用于分子性质预测的多模态模型。它联合编码SELFIES序列（1D）、分子图（2D）和构象体集合（3D），并通过交叉注意力进行融合。该模型的核心贡献包括构象体集合注意力机制和跨模态融合层。虽然其主要应用是分子性质预测，但其核心方法——整合多种分子表示（序列、图、3D结构）并进行跨模态融合——是构建化学大模型（特别是多模态化学模型）的关键技术路径。论文还提到在ZINC250K数据集上进行预训练，并发布了代码、模型和数据，这些资源可用于相关研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Most machine learning models for molecular property prediction rely on a single molecular representation (either a sequence, a graph, or a 3D structure) and treat molecular geometry as static. We present MolFM-Lite, a multi-modal model that jointly encodes SELFIES sequences (1D), molecular graphs (2D), and conformer ensembles (3D) through cross-attention fusion, while conditioning predictions on experimental context via Feature-wise Linear Modulation (FiLM). Our main methodological contributions are: (1) a conformer ensemble attention mechanism that combines learnable attention with Boltzmann-weighted priors over multiple RDKit-generated conformers, capturing the thermodynamic distribution of molecular shapes; and (2) a cross-modal fusion layer where each modality can attend to others, enabling complementary information sharing. We evaluate on four MoleculeNet scaffold-split benchmarks using our model's own splits, and report all baselines re-evaluated under the same protocol. Comprehensive ablation studies across all four datasets confirm that each architectural component contributes independently, with tri-modal fusion providing 7-11% AUC improvement over single-modality baselines and conformer ensembles adding approximately 2% over single-conformer variants. Pre-training on ZINC250K (~250K molecules) using cross-modal contrastive and masked-atom objectives enables effective weight initialization at modest compute cost. We release all code, trained models, and data splits to support reproducibility.

</details>

---

### 5. [Revisiting Chebyshev Polynomial and Anisotropic RBF Models for Tabular Regression](https://arxiv.org/abs/2602.22422)

**基本信息**

- 🔗 arXiv: [`2602.22422`](https://arxiv.org/abs/2602.22422)
- 👥 作者: Luciano Gerber, Huw Lloyd
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22422.pdf)

**💡 相关性分析**

满足标准2：论文开发并发布了用于回归的平滑基模型（如各向异性RBF网络、切比雪夫回归器）的scikit-learn兼容包。这些模型和工具可以应用于化学信息学领域的QSAR建模、分子性质预测等任务，为相关研究提供了可用的模型资源和实现。

**📖 中文摘要**

本文重新审视了切比雪夫多项式回归和各向异性径向基函数（RBF）网络在表格回归任务中的应用。作者开发了各向异性RBF网络、岭正则化切比雪夫多项式回归器以及平滑树混合模型，并将其作为scikit-learn兼容包发布。研究在55个回归数据集上对这些平滑基模型与树集成、预训练Transformer等基线进行了基准测试。虽然论文主要关注通用表格回归，但其探索的平滑基模型（如RBF网络）在化学信息学中常用于构建定量构效关系（QSAR）模型，是化学大模型或分子性质预测模型的一种潜在基础架构。发布的模型包也可作为相关研究的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Smooth-basis models such as Chebyshev polynomial regressors and radial basis function (RBF) networks are well established in numerical analysis. Their continuously differentiable prediction surfaces suit surrogate optimisation, sensitivity analysis, and other settings where the response varies gradually with inputs. Despite these properties, smooth models seldom appear in tabular regression, where tree ensembles dominate. We ask whether they can compete, benchmarking models across 55 regression datasets organised by application domain. We develop an anisotropic RBF network with data-driven centre placement and gradient-based width optimisation, a ridge-regularised Chebyshev polynomial regressor, and a smooth-tree hybrid (Chebyshev model tree); all three are released as scikit-learn-compatible packages. We benchmark these against tree ensembles, a pre-trained transformer, and standard baselines, evaluating accuracy alongside generalisation behaviour. The transformer ranks first on accuracy across a majority of datasets, but its GPU dependence, inference latency, and dataset-size limits constrain deployment in the CPU-based settings common across applied science and industry. Among CPU-viable models, smooth models and tree ensembles are statistically tied on accuracy, but the former tend to exhibit tighter generalisation gaps. We recommend routinely including smooth-basis models in the candidate pool, particularly when downstream use benefits from tighter generalisation and gradually varying predictions.

</details>

---

### 6. [Predicting Known Vulnerabilities from Attack Descriptions Using Sentence Transformers](https://arxiv.org/abs/2602.22433)

**基本信息**

- 🔗 arXiv: [`2602.22433`](https://arxiv.org/abs/2602.22433)
- 👥 作者: Refat Othman
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22433.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法（使用句子Transformer编码文本描述并进行相似性匹配以推断结构化实体）与质谱结构推理的核心任务（从光谱特征或描述推断分子结构）在问题范式上高度相关。它为如何利用深度学习模型处理“描述-结构”映射问题提供了可借鉴的技术路线。

**📖 中文摘要**

本文提出了一种基于Transformer句子嵌入的方法，用于从网络攻击的自然语言描述中预测已知漏洞（CVE）。作者评估了14种最先进的Transformer模型在四种攻击描述类型上的性能，发现MITRE ATT&CK中的技术描述提供了最强的预测信号。最佳模型multi-qa-mpnet-base-dot-v1因其混合预训练和针对语义相似性的优化而表现最佳。该方法在VULDAT工具中实现，可自动将攻击与漏洞关联起来。虽然主题是网络安全，但其核心技术——使用句子Transformer将文本描述编码为语义向量以进行相似性匹配和推荐——与质谱结构推理中“从文本描述（或光谱特征描述）推断分子结构”的任务在方法论上高度相似。两者都涉及从非结构化的自然语言或特征描述到结构化实体（漏洞ID或分子结构）的映射。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern infrastructures rely on software systems that remain vulnerable to cyberattacks. These attacks frequently exploit vulnerabilities documented in repositories such as MITRE's Common Vulnerabilities and Exposures (CVE). However, Cyber Threat Intelligence resources, including MITRE ATT&CK and CVE, provide only partial coverage of attack-vulnerability relationships. Attack information often appears before vulnerabilities are formally linked, creating the need for automated methods that infer likely vulnerabilities directly from attack descriptions. This thesis addresses the problem of predicting known vulnerabilities from natural-language descriptions of cyberattacks. We develop transformer-based sentence embedding methods that encode attack and vulnerability descriptions into semantic vector representations, enabling similarity-based ranking and recommendation. Fourteen state-of-the-art transformer models were evaluated across four attack description types (Tactic, Technique, Procedure, and Attack Pattern). Results show that Technique descriptions in MITRE ATT&CK provide the strongest predictive signal. The multi-qa-mpnet-base-dot-v1 (MMPNet) model achieved the best performance due to its hybrid pre-training and optimization for semantic similarity. The approach was implemented in the VULDAT tool, which automatically links attacks to vulnerabilities. Manual validation revealed previously undocumented relationships in MITRE repositories. Evaluation on unseen cyberattack reports demonstrates that the models generalize beyond curated datasets and support proactive vulnerability awareness.

</details>

---

### 7. [Fault-tolerant Reduce and Allreduce operations based on correction](https://arxiv.org/abs/2602.22445)

**基本信息**

- 🔗 arXiv: [`2602.22445`](https://arxiv.org/abs/2602.22445)
- 👥 作者: Martin Kuettler, Hermann Haertig
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22445.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于PID的多模态信息解耦与表示学习方法，为化学信息学中整合多种分子表示（如质谱、核磁、分子指纹）进行联合推理提供了新颖且相关的技术思路。理解不同数据源在最终预测中的独特、冗余和互补作用，对于构建鲁棒、可解释的质谱结构推理模型至关重要。

**📖 中文摘要**

本文提出了DisQ-HNet，一个用于从配对的T1加权和FLAIR MRI合成tau-PET图像的框架，同时揭示了每种模态对预测的贡献。该方法结合了（1）基于部分信息分解（PID）引导的矢量量化编码器，将潜在信息划分为冗余、独特和互补成分；（2）Half-UNet解码器，使用基于结构边缘线索的伪跳跃连接来保留解剖细节。虽然应用领域是医学影像，但其核心创新点——使用PID引导的量化编码器来解耦和解释多模态信息（冗余、独特、互补）——对于化学信息学和质谱分析中处理多源、多模态数据（如多种光谱数据、分子描述符）具有重要的方法论启示。这种解耦分析有助于理解不同数据源在分子结构推理中的各自贡献。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Implementations of Broadcast based on some information dissemination algorithm -- e.g., gossip or tree-based communication -- followed by a correction algorithm has been proposed previously. This work describes an approach to apply a similar idea to Reduce. In it, a correction-like communication phase precedes a tree-based phase. This provides a Reduce algorithm which is tolerant to a number of failed processes. Semantics of the resulting algorithm are provided and proven. Based on these results, Broadcast and Reduce are combined to provide Allreduce.

</details>

---

### 8. [Mapping the Landscape of Artificial Intelligence in Life Cycle Assessment Using Large Language Models](https://arxiv.org/abs/2602.22500)

**基本信息**

- 🔗 arXiv: [`2602.22500`](https://arxiv.org/abs/2602.22500)
- 👥 作者: Anastasija Mensikova, Donna M. Rizzo, Kathryn Hinkelman
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22500.pdf)

**💡 相关性分析**

满足标准3：论文是一篇利用大语言模型进行的领域综述，其主题是“人工智能在生命周期评估中的应用”。虽然LCA与化学信息学/质谱分析不是同一领域，但论文所采用的研究方法——即使用LLMs进行大规模文献分析、趋势识别和主题挖掘——本身是构建和评估“化学大模型”或分析“质谱结构推理”领域发展态势的重要工具和方法论。它为相关领域的学者如何系统性地梳理自身领域提供了可借鉴的框架。

**📖 中文摘要**

本文对人工智能（AI）在生命周期评估（LCA）中的应用进行了详细综述。作者利用大语言模型（LLMs）进行文本挖掘，结合传统文献综述方法，综合分析了AI-LCA交叉领域的研究现状、趋势和未来方向。研究发现，随着LCA研究的扩展，AI技术的采用急剧增长，并明显转向LLM驱动的方法，同时机器学习应用持续增加。AI方法与相应LCA阶段之间存在统计学上显著的相关性。这项工作展示了LLM辅助方法在支持大规模、可重复的跨领域文献综述方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integration of artificial intelligence (AI) into life cycle assessment (LCA) has accelerated in recent years, with numerous studies successfully adapting machine learning algorithms to support various stages of LCA. Despite this rapid development, comprehensive and broad synthesis of AI-LCA research remains limited. To address this gap, this study presents a detailed review of published work at the intersection of AI and LCA, leveraging large language models (LLMs) to identify current trends, emerging themes, and future directions. Our analyses reveal that as LCA research continues to expand, the adoption of AI technologies has grown dramatically, with a noticeable shift toward LLM-driven approaches, continued increases in ML applications, and statistically significant correlations between AI approaches and corresponding LCA stages. By integrating LLM-based text-mining methods with traditional literature review techniques, this study introduces a dynamic and effective framework capable of capturing both high-level research trends and nuanced conceptual patterns (themes) across the field. Collectively, these findings demonstrate the potential of LLM-assisted methodologies to support large-scale, reproducible reviews across broad research domains, while also evaluating pathways for computationally-efficient LCA in the context of rapidly developing AI technologies. In doing so, this work helps LCA practitioners incorporate state-of-the-art tools and timely insights into environmental assessments that can enhance the rigor and quality of sustainability-driven decisions and decision-making processes.

</details>

---

### 9. [LUMOS: Democratizing SciML Workflows with L0-Regularized Learning for Unified Feature and Parameter Adaptation](https://arxiv.org/abs/2602.22537)

**基本信息**

- 🔗 arXiv: [`2602.22537`](https://arxiv.org/abs/2602.22537)
- 👥 作者: Shouwei Gao, Xu Zheng, Dongsheng Luo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22537.pdf)

**💡 相关性分析**

满足标准2：论文提出的LUMOS框架是一个用于SciML模型设计的通用工具，它通过L0正则化自动进行特征选择和模型剪枝。该框架及其实现可以应用于化学信息学和质谱分析中的模型构建，例如，在构建基于机器学习的质谱解析或分子性质预测模型时，自动选择最相关的分子特征或光谱峰，并优化模型复杂度。这为相关领域提供了实用的模型优化工具和方法。

**📖 中文摘要**

本文介绍了LUMOS，一个基于L0正则化学习的端到端框架，旨在通过统一特征选择和模型剪枝来民主化科学机器学习（SciML）模型设计。LUMOS采用半随机门控和重参数化技术，在训练过程中动态选择信息特征并剪枝冗余参数，减少对手动调优的依赖，同时保持预测准确性。作者在包括宇宙学和分子科学在内的13个不同的SciML工作负载上评估了LUMOS，证明了其有效性和泛化能力。实验表明，LUMOS平均实现了71.45%的参数减少和6.4倍的推理加速。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of scientific machine learning (SciML) has accelerated discovery across diverse domains, yet designing effective SciML models remains a challenging task. In practice, building such models often requires substantial prior knowledge and manual expertise, particularly in determining which input features to use and how large the model should be. We introduce LUMOS, an end-to-end framework based on L0-regularized learning that unifies feature selection and model pruning to democratize SciML model design. By employing semi-stochastic gating and reparameterization techniques, LUMOS dynamically selects informative features and prunes redundant parameters during training, reducing the reliance on manual tuning while maintaining predictive accuracy. We evaluate LUMOS across 13 diverse SciML workloads, including cosmology and molecular sciences, and demonstrate its effectiveness and generalizability. Experiments on 13 SciML models show that LUMOS achieves 71.45% parameter reduction and a 6.4x inference speedup on average. Furthermore, Distributed Data Parallel (DDP) training on up to eight GPUs confirms the scalability of

</details>

---

### 10. [Relatron: Automating Relational Machine Learning over Relational Databases](https://arxiv.org/abs/2602.22552)

**基本信息**

- 🔗 arXiv: [`2602.22552`](https://arxiv.org/abs/2602.22552)
- 👥 作者: Zhikai Chen, Han Xie, Jian Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22552.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容——关系数据库上的机器学习自动化（Relational Machine Learning）——与化学信息学中处理分子数据库（如将分子表示为图数据库或关系表）进行性质预测或结构推理的任务高度相关。其提出的统一设计空间分析、架构搜索以及任务感知的模型选择框架（Relatron），为化学信息学中如何自动化地构建和选择最适合特定分子预测任务的模型架构提供了直接相关的技术蓝图和方法论指导。

**📖 中文摘要**

本文对关系数据库（RDB）上的预测建模进行了全面研究，将关系深度学习（RDL）和经典方法（如深度特征合成DFS）统一在一个共享的设计空间中，并在多样化的RDB任务上进行了以架构为中心的搜索。分析得出三个关键发现，并基于此提出了Relatron，一个基于任务嵌入的元选择器，用于在RDL和DFS之间进行选择并修剪族内搜索。该研究揭示了不同架构在不同任务上的表现差异，并提供了基于任务信号进行模型选择的原理性方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling over relational databases (RDBs) powers applications, yet remains challenging due to capturing both cross-table dependencies and complex feature interactions. Relational Deep Learning (RDL) methods automate feature engineering via message passing, while classical approaches like Deep Feature Synthesis (DFS) rely on predefined non-parametric aggregators. Despite performance gains, the comparative advantages of RDL over DFS and the design principles for selecting effective architectures remain poorly understood. We present a comprehensive study that unifies RDL and DFS in a shared design space and conducts architecture-centric searches across diverse RDB tasks. Our analysis yields three key findings: (1) RDL does not consistently outperform DFS, with performance being highly task-dependent; (2) no single architecture dominates across tasks, underscoring the need for task-aware model selection; and (3) validation accuracy is an unreliable guide for architecture choice. This search yields a model performance bank that links architecture configurations to their performance; leveraging this bank, we analyze the drivers of the RDL-DFS performance gap and introduce two task signals -- RDB task homophily and an affinity embedding that captures size, path, feature, and temporal structure -- whose correlation with the gap enables principled routing. Guided by these signals, we propose Relatron, a task embedding-based meta-selector that chooses between RDL and DFS and prunes the within-family search. Lightweight loss-landscape metrics further guard against brittle checkpoints by preferring flatter optima. In experiments, Relatron resolves the "more tuning, worse performance" effect and, in joint hyperparameter-architecture optimization, achieves up to 18.5% improvement over strong baselines with 10x lower cost than Fisher information-based alternatives.

</details>

---

### 11. [Autoregressive Visual Decoding from EEG Signals](https://arxiv.org/abs/2602.22555)

**基本信息**

- 🔗 arXiv: [`2602.22555`](https://arxiv.org/abs/2602.22555)
- 👥 作者: Sicheng Dai, Hongwang Xiao, Shan Yu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22555.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法——使用自回归Transformer模型，从连续、高维的时序信号（EEG）解码生成结构化的视觉信息（图像）——与质谱结构推理的核心任务（从连续的质谱信号解码生成分子结构）在问题定义和技术路线上高度相似。两者都涉及将复杂的、非结构化的仪器测量数据转换为离散的、结构化的表示（图像令牌或分子子结构令牌）。AVDE所采用的多尺度自回归生成范式为质谱结构推理提供了极具参考价值的技术路径。

**📖 中文摘要**

本文提出了AVDE，一个从脑电图（EEG）信号进行视觉解码的轻量高效框架。首先，利用预训练的EEG模型LaBraM，并通过对比学习进行微调，以对齐EEG和图像表示。其次，采用基于“下一尺度预测”策略的自回归生成框架：使用预训练的VQ-VAE将图像编码为多尺度令牌映射，训练一个Transformer以EEG嵌入作为最粗表示，自回归地预测更细尺度的令牌。实验表明，AVDE在图像检索和重建任务上优于先前的方法，同时仅使用10%的参数。该框架展示了自回归模型作为高效、可解释的脑机接口工具的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalogram (EEG) signals have become a popular medium for decoding visual information due to their cost-effectiveness and high temporal resolution. However, current approaches face significant challenges in bridging the modality gap between EEG and image data. These methods typically rely on complex adaptation processes involving multiple stages, making it hard to maintain consistency and manage compounding errors. Furthermore, the computational overhead imposed by large-scale diffusion models limit their practicality in real-world brain-computer interface (BCI) applications. In this work, we present AVDE, a lightweight and efficient framework for visual decoding from EEG signals. First, we leverage LaBraM, a pre-trained EEG model, and fine-tune it via contrastive learning to align EEG and image representations. Second, we adopt an autoregressive generative framework based on a "next-scale prediction" strategy: images are encoded into multi-scale token maps using a pre-trained VQ-VAE, and a transformer is trained to autoregressively predict finer-scale tokens starting from EEG embeddings as the coarsest representation. This design enables coherent generation while preserving a direct connection between the input EEG signals and the reconstructed images. Experiments on two datasets show that AVDE outperforms previous state-of-the-art methods in both image retrieval and reconstruction tasks, while using only 10% of the parameters. In addition, visualization of intermediate outputs shows that the generative process of AVDE reflects the hierarchical nature of human visual perception. These results highlight the potential of autoregressive models as efficient and interpretable tools for practical BCI applications.

</details>

---

### 12. [Molecule Mixture Detection and Design for MC Systems with Non-linear, Cross-reactive Receiver Arrays](https://arxiv.org/abs/2602.22799)

**基本信息**

- 🔗 arXiv: [`2602.22799`](https://arxiv.org/abs/2602.22799)
- 👥 作者: Bastian Heinlein, Kaikai Zhu, Sümeyye Carkit-Yilmaz 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22799.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分子通信系统中的分子混合物检测和通信设计，这直接涉及化学信息学中的传感器数据处理和信号推理，与‘质谱结构推理’主题在方法论（从复杂、非线性的传感器信号中推断化学信息）上高度相关。

**📖 中文摘要**

本文研究了空气分子通信（MC）系统，该系统利用商用传感器进行分子混合物的检测和通信设计。这些传感器通常表现出非线性和交叉反应特性，这与MC文献中常见的理想化线性、分子类型特异性传感假设不符。论文提出了几种检测器和传输方案，用于处理接收器（RX）使用非线性、交叉反应传感器的情况。所有方案都基于通过无迹变换（Unscented Transform）馈入非线性RX的符号似然的一阶和二阶矩。具体来说，论文为无符号间干扰（ISI）的传输场景提出了一种近似最大似然（AML）符号检测器，以及一种考虑接收器特性的互补混合字母表设计算法。当在高数据速率下存在显著ISI时，AML检测器可以进行调整以利用统计ISI知识。此外，还提出了一种结合多个符号间隔信息的序列检测器。这项工作通过考虑发射机噪声、ISI和通用的非线性交叉反应RX阵列，为一大类MC系统实现可靠通信提供了方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Air-based molecular communication (MC) has the potential to be one of the first MC systems to be deployed in real-world applications, enabled by commercially available sensors. However, these sensors usually exhibit non-linear and cross-reactive behavior, contrary to the idealizing assumption of linear and perfectly molecule type-specific sensing often made in the MC literature. To address this mismatch, we propose several detectors and transmission schemes for a molecule mixture communication system where the receiver (RX) employs non-linear, cross-reactive sensors. All proposed schemes are based on the first- and second-order moments of the symbol likelihoods that are fed through the non-linear RX using the Unscented Transform. In particular, we propose an approximate maximum likelihood (AML) symbol-by-symbol detector for inter-symbol-interference (ISI)-free transmission scenarios and a complementary mixture alphabet design algorithm which accounts for the RX characteristics. When significant ISI is present at high data rates, the AML detector can be adapted to exploit statistical ISI knowledge. Additionally, we propose a sequence detector which combines information from multiple symbol intervals. For settings where sequence detection is not possible due to extremely limited computational power at the RX, we propose an adaptive transmission scheme which can be combined with symbol-by-symbol detection. Using computer simulations, we validate all proposed detectors and algorithms based on the responses of commercially available sensors as well as artificially generated sensor data incorporating the characteristics of metal-oxide semiconductor sensors. By employing a general system model that accounts for transmitter noise, ISI, and general non-linear, cross-reactive RX arrays, this work enables reliable communication for a large class of MC systems.

</details>

---

### 13. [FlexMS is a flexible framework for benchmarking deep learning-based mass spectrum prediction tools in metabolomics](https://arxiv.org/abs/2602.22822)

**基本信息**

- 🔗 arXiv: [`2602.22822`](https://arxiv.org/abs/2602.22822)
- 👥 作者: Yunhua Zhong, Yixuan Tang, Yifan Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22822.pdf)

**💡 相关性分析**

满足标准2和标准1：论文的核心是提供了一个用于评估质谱预测模型的基准框架（FlexMS），这直接贡献了可用于‘质谱结构推理’主题的数据集、资源和工具（标准2）。同时，其研究内容直接围绕使用深度学习模型从质谱数据中预测分子结构，与‘质谱结构推理’核心主题高度相关（标准1）。

**📖 中文摘要**

本文介绍了FlexMS，一个用于在代谢组学中基准测试基于深度学习的质谱预测工具的灵活框架。化学分子的鉴定和性质预测在药物发现和材料科学中至关重要，其中串联质谱技术以质荷比峰的形式提供了有价值的碎片化线索。然而，实验谱图的缺乏阻碍了每个分子鉴定的进行，因此迫切需要建立用于计算模型的预测方法。深度学习模型在预测分子结构谱图方面显示出前景，但由于方法的异质性和缺乏明确定义的基准，整体评估仍然具有挑战性。为了解决这个问题，我们创建了基准框架FlexMS，用于构建和评估质谱预测中的多样化模型架构。FlexMS支持动态构建众多不同的模型架构组合，同时使用不同的指标在预处理的公共数据集上评估其性能。本文提供了对影响性能因素的见解，包括数据集的结构多样性、学习率和数据稀疏性等超参数、预训练效果、元数据消融设置以及跨领域迁移学习分析。这为选择合适的模型提供了实用指导。此外，检索基准模拟了实际的鉴定场景，并根据预测的谱图对潜在匹配进行评分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The identification and property prediction of chemical molecules is of central importance in the advancement of drug discovery and material science, where the tandem mass spectrometry technology gives valuable fragmentation cues in the form of mass-to-charge ratio peaks. However, the lack of experimental spectra hinders the attachment of each molecular identification, and thus urges the establishment of prediction approaches for computational models. Deep learning models appear promising for predicting molecular structure spectra, but overall assessment remains challenging as a result of the heterogeneity in methods and the lack of well-defined benchmarks. To address this, our contribution is the creation of benchmark framework FlexMS for constructing and evaluating diverse model architectures in mass spectrum prediction. With its easy-to-use flexibility, FlexMS supports the dynamic construction of numerous distinct combinations of model architectures, while assessing their performance on preprocessed public datasets using different metrics. In this paper, we provide insights into factors influencing performance, including the structural diversity of datasets, hyperparameters like learning rate and data sparsity, pretraining effects, metadata ablation settings and cross-domain transfer learning analysis. This provides practical guidance in choosing suitable models. Moreover, retrieval benchmarks simulate practical identification scenarios and score potential matches based on predicted spectra.

</details>

---

### 14. [MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis](https://arxiv.org/abs/2602.22955)

**基本信息**

- 🔗 arXiv: [`2602.22955`](https://arxiv.org/abs/2602.22955)
- 👥 作者: Feng Guo, Jiaxiang Liu, Yang Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22955.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模、多模态的医学影像诊断数据集（MM-NeuroOnco）和评估基准（MM-NeuroOnco-Bench）。虽然其领域是医学影像（MRI），但其构建大规模、语义丰富的多模态数据集的方法论，以及使用自动化流程生成高质量注释的思路，对于构建和评估‘化学大模型’（尤其是在需要多模态数据，如化学结构、质谱、文本描述的场景）具有重要的参考价值和资源启示。

**📖 中文摘要**

本文介绍了MM-NeuroOnco，一个用于基于MRI的脑肿瘤诊断的大规模多模态基准和指令调优数据集。准确的脑肿瘤诊断要求模型不仅能检测病变，还能生成基于影像学表现的、临床可解释的推理。然而，现有的公共数据集在注释丰富性和诊断语义方面仍然有限。为了弥补这一差距，MM-NeuroOnco包含来自20个数据源的24,726个MRI切片，并配对了约200,000个涵盖不同肿瘤亚型和成像模式的语义丰富的多模态指令。为了缓解诊断语义注释的稀缺性和高成本，我们开发了一个多模型协作流程，用于自动完成医学信息并进行质量控制，从而生成超越仅掩码注释的诊断相关语义。基于此数据集，我们进一步构建了MM-NeuroOnco-Bench，这是一个手动注释的评估基准，采用拒绝感知设置以减少封闭式问题格式固有的偏见。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate brain tumor diagnosis requires models to not only detect lesions but also generate clinically interpretable reasoning grounded in imaging manifestations, yet existing public datasets remain limited in annotation richness and diagnostic semantics. To bridge this gap, we introduce MM-NeuroOnco, a large-scale multimodal benchmark and instruction-tuning dataset for brain tumor MRI understanding, consisting of 24,726 MRI slices from 20 data sources paired with approximately 200,000 semantically enriched multimodal instructions spanning diverse tumor subtypes and imaging modalities. To mitigate the scarcity and high cost of diagnostic semantic annotations, we develop a multi-model collaborative pipeline for automated medical information completion and quality control, enabling the generation of diagnosis-related semantics beyond mask-only annotations. Building upon this dataset, we further construct MM-NeuroOnco-Bench, a manually annotated evaluation benchmark with a rejection-aware setting to reduce biases inherent in closed-ended question formats. Evaluation across ten representative models shows that even the strongest baseline, Gemini 3 Flash, achieves only 41.88% accuracy on diagnosis-related questions, highlighting the substantial challenges of multimodal brain tumor diagnostic understanding. Leveraging MM-NeuroOnco, we further propose NeuroOnco-GPT, which achieves a 27% absolute accuracy improvement on diagnostic questions following fine-tuning. This result demonstrates the effectiveness of our dataset and benchmark in advancing clinically grounded multimodal diagnostic reasoning. Code and dataset are publicly available at: this https URL

</details>

---

### 15. [SPM-Bench: Benchmarking Large Language Models for Scanning Probe Microscopy](https://arxiv.org/abs/2602.22971)

**基本信息**

- 🔗 arXiv: [`2602.22971`](https://arxiv.org/abs/2602.22971)
- 👥 作者: Peiyao Xiao, Xiaogang Li, Chengliang Xu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22971.pdf)

**💡 相关性分析**

满足标准2：论文提出的自动化数据合成流水线和方法（如AGS技术、混合架构）是构建高质量科学数据集（包括化学信息学领域）的通用化范例，为训练和评估化学大模型提供了重要的数据资源构建工具和方法。

**📖 中文摘要**

论文提出了SPM-Bench，一个用于扫描探针显微镜（SPM）领域的多模态基准测试。其核心贡献在于一个全自动的数据合成流水线，用于从arXiv和期刊论文中高效提取高质量的图像-文本对，以构建专门的科学数据集。虽然其直接应用领域是SPM，但论文提出的自动化科学数据合成范式（包括使用Anchor-Gated Sieve技术和混合云-本地架构高效处理科学文献）具有通用性。该方法展示了如何从海量科学文献中构建高质量、领域特定的数据集，这为训练和评估其他科学领域的“化学大模型”提供了重要的数据资源构建思路和方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As LLMs achieved breakthroughs in general reasoning, their proficiency in specialized scientific domains reveals pronounced gaps in existing benchmarks due to data contamination, insufficient complexity, and prohibitive human labor costs. Here we present SPM-Bench, an original, PhD-level multimodal benchmark specifically designed for scanning probe microscopy (SPM). We propose a fully automated data synthesis pipeline that ensures both high authority and low-cost. By employing Anchor-Gated Sieve (AGS) technology, we efficiently extract high-value image-text pairs from arXiv and journal papers published between 2023 and 2025. Through a hybrid cloud-local architecture where VLMs return only spatial coordinates "llbox" for local high-fidelity cropping, our pipeline achieves extreme token savings while maintaining high dataset purity. To accurately and objectively evaluate the performance of the LLMs, we introduce the Strict Imperfection Penalty F1 (SIP-F1) score. This metric not only establishes a rigorous capability hierarchy but also, for the first time, quantifies model "personalities" (Conservative, Aggressive, Gambler, or Wise). By correlating these results with model-reported confidence and perceived difficulty, we expose the true reasoning boundaries of current AI in complex physical scenarios. These insights establish SPM-Bench as a generalizable paradigm for automated scientific data synthesis.

</details>

---

### 16. [RhythmBERT: A Self-Supervised Language Model Based on Latent Representations of ECG Waveforms for Heart Disease Detection](https://arxiv.org/abs/2602.23060)

**基本信息**

- 🔗 arXiv: [`2602.23060`](https://arxiv.org/abs/2602.23060)
- 👥 作者: Xin Wang, Burcu Ozek, Aruna Mohan 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23060.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将生物医学时间序列（ECG）结构化为一种语言并进行自监督建模（RhythmBERT）。这种“将复杂数据视为语言进行建模”的范式与化学信息学中构建“化学大模型”（将分子、光谱等视为序列或语言）的核心思想直接相关，为后者提供了方法论上的借鉴。

**📖 中文摘要**

论文提出了RhythmBERT，一种基于心电图（ECG）波形潜在表示的自监督语言模型，用于心脏病检测。其关键创新在于将ECG视为一种语言范式：通过基于自动编码器的潜在表示将P、QRS和T波片段编码为符号标记（Token），从而捕获节律语义；同时使用连续的嵌入来保留细粒度的形态学特征。该模型在大约80万份未标记的ECG记录上通过掩码预测目标进行预训练。这项工作展示了将复杂的时间序列数据（如ECG）结构化为一种“语言”并进行自监督学习的方法。这种将序列数据（波形）离散化为符号序列并构建语言模型的思想，与“化学大模型”中将分子结构（如SMILES字符串、质谱图）视为序列或语言进行处理的核心范式高度相似，为处理化学序列数据（如质谱）提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electrocardiogram (ECG) analysis is crucial for diagnosing heart disease, but most self-supervised learning methods treat ECG as a generic time series, overlooking physiologic semantics and rhythm-level structure. Existing contrastive methods utilize augmentations that distort morphology, whereas generative approaches employ fixed-window segmentation, which misaligns cardiac cycles. To address these limitations, we propose RhythmBERT, a generative ECG language model that considers ECG as a language paradigm by encoding P, QRS, and T segments into symbolic tokens via autoencoder-based latent representations. These discrete tokens capture rhythm semantics, while complementary continuous embeddings retain fine-grained morphology, enabling a unified view of waveform structure and rhythm. RhythmBERT is pretrained on approximately 800,000 unlabeled ECG recordings with a masked prediction objective, allowing it to learn contextual representations in a label-efficient manner. Evaluations show that despite using only a single lead, RhythmBERT achieves comparable or superior performance to strong 12-lead baselines. This generalization extends from prevalent conditions such as atrial fibrillation to clinically challenging cases such as subtle ST-T abnormalities and myocardial infarction. Our results suggest that considering ECG as structured language offers a scalable and physiologically aligned pathway for advancing cardiac analysis.

</details>

---

### 17. [CiteLLM: An Agentic Platform for Trustworthy Scientific Reference Discovery](https://arxiv.org/abs/2602.23075)

**基本信息**

- 🔗 arXiv: [`2602.23075`](https://arxiv.org/abs/2602.23075)
- 👥 作者: Mengze Hong, Di Jiang, Chen Jason Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23075.pdf)

**💡 相关性分析**

满足标准2：论文提出的CiteLLM平台是一个基于LLM的、与领域学术知识库集成的智能体系统架构。这种构建专业领域LLM工具（如用于化学文献检索、质谱数据解释的助手）的平台设计和实现思路，为化学信息学和质谱分析领域提供了有价值的工具开发范例。

**📖 中文摘要**

论文介绍了CiteLLM，一个专为可信科学参考文献发现而设计的智能体平台。该系统将大语言模型（LLM）功能直接嵌入LaTeX编辑器环境中，通过动态的学科感知路由从可信的学术知识库中检索候选文献，并利用LLM生成上下文感知的搜索查询、按相关性排序候选文献、并通过段落级语义匹配和集成聊天机器人进行验证和解释支持。该系统旨在为大语言模型在学术写作中的辅助应用提供一种可靠、可追溯且保护隐私的解决方案。虽然其应用场景是学术写作，但其核心是构建一个基于LLM的、与领域知识库（化学、生物等科学文献库）紧密集成的智能信息检索和验证系统。这种架构和思路对于开发面向化学信息学或质谱分析领域的专业LLM助手或工具具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have created new opportunities to enhance the efficiency of scholarly activities; however, challenges persist in the ethical deployment of AI assistance, including (1) the trustworthiness of AI-generated content, (2) preservation of academic integrity and intellectual property, and (3) protection of information privacy. In this work, we present CiteLLM, a specialized agentic platform designed to enable trustworthy reference discovery for grounding author-drafted claims and statements. The system introduces a novel interaction paradigm by embedding LLM utilities directly within the LaTeX editor environment, ensuring a seamless user experience and no data transmission outside the local system. To guarantee hallucination-free references, we employ dynamic discipline-aware routing to retrieve candidates exclusively from trusted web-based academic repositories, while leveraging LLMs solely for generating context-aware search queries, ranking candidates by relevance, and validating and explaining support through paragraph-level semantic matching and an integrated chatbot. Evaluation results demonstrate the superior performance of the proposed system in returning valid and highly usable references.

</details>

---

### 18. [Assessing Deanonymization Risks with Stylometry-Assisted LLM Agent](https://arxiv.org/abs/2602.23079)

**基本信息**

- 🔗 arXiv: [`2602.23079`](https://arxiv.org/abs/2602.23079)
- 👥 作者: Boyang Zhang, Yang Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23079.pdf)

**💡 相关性分析**

满足标准1：论文提出的SALA方法，即结合定量特征（文体计量特征）与LLM进行联合推理以解决归属/推断问题，其技术范式与“质谱结构推理”任务中结合光谱特征与序列模型进行分子结构推断的核心方法思路相关。

**📖 中文摘要**

论文提出了一个用于评估和缓解文本数据（如新闻文章）去匿名化风险的大语言模型（LLM）智能体框架。其核心是SALA（Stylometry-Assisted LLM Analysis）方法，该方法将定量的文体计量学特征与LLM推理相结合，实现鲁棒且可解释的作者身份归属。论文还提出了一种引导重写策略，利用智能体的推理轨迹生成改写提示，以在保持文本含义的同时降低作者可识别性。这项工作聚焦于LLM在文本分析中的应用及其隐私影响。虽然主题是作者身份分析，但其核心方法论——结合定量特征（类似于从质谱或分子描述符中提取的特征）与LLM进行联合推理——与“质谱结构推理”任务中结合光谱特征与序列模型进行分子结构推断的思路在技术层面上有相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid advancement of large language models (LLMs) has enabled powerful authorship inference capabilities, raising growing concerns about unintended deanonymization risks in textual data such as news articles. In this work, we introduce an LLM agent designed to evaluate and mitigate such risks through a structured, interpretable pipeline. Central to our framework is the proposed $\textit{SALA}$ (Stylometry-Assisted LLM Analysis) method, which integrates quantitative stylometric features with LLM reasoning for robust and transparent authorship attribution. Experiments on large-scale news datasets demonstrate that $\textit{SALA}$, particularly when augmented with a database module, achieves high inference accuracy in various scenarios. Finally, we propose a guided recomposition strategy that leverages the agent's reasoning trace to generate rewriting prompts, effectively reducing authorship identifiability while preserving textual meaning. Our findings highlight both the deanonymization potential of LLM agents and the importance of interpretable, proactive defenses for safeguarding author privacy.

</details>

---

### 19. [Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models](https://arxiv.org/abs/2602.23179)

**基本信息**

- 🔗 arXiv: [`2602.23179`](https://arxiv.org/abs/2602.23179)
- 👥 作者: Gal Kesten-Pomeranz, Yaniv Nikankin, Anja Reusch 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23179.pdf)

**💡 相关性分析**

满足标准1：论文对蛋白质语言模型（一种生物化学领域的“大模型”）内部工作机制进行机理可解释性研究，揭示了其如何整合领域知识进行模式识别和推理。这项研究为理解和设计“化学大模型”以及模型如何学习“质谱结构推理”等复杂任务提供了重要的研究范式和洞察。

**📖 中文摘要**

论文深入研究了蛋白质语言模型（PLM）内部检测蛋白质序列中重复片段（包括精确重复和近似重复）的机制。研究发现，PLM通过结合通用的模式匹配组件（如注意力头）和专门的生物学知识组件（如编码氨基酸相似性的神经元）来构建特征表示，然后通过归纳头（induction heads）跨重复片段关注对齐的标记，从而正确预测。这项工作揭示了PLM如何通过结合基于语言的模式匹配和专门的领域知识来解决生物学任务。这种对领域特定语言模型（蛋白质语言模型）内部工作机制的机理可解释性研究，为理解和设计其他领域的“大模型”（如化学大模型）提供了重要的研究范式和见解。特别是，它展示了模型如何整合领域先验知识（如化学规则、质谱碎裂规律）来增强推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequences are abundant in repeating segments, both as exact copies and as approximate segments with mutations. These repeats are important for protein structure and function, motivating decades of algorithmic work on repeat identification. Recent work has shown that protein language models (PLMs) identify repeats, by examining their behavior in masked-token prediction. To elucidate their internal mechanisms, we investigate how PLMs detect both exact and approximate repeats. We find that the mechanism for approximate repeats functionally subsumes that of exact repeats. We then characterize this mechanism, revealing two main stages: PLMs first build feature representations using both general positional attention heads and biologically specialized components, such as neurons that encode amino-acid similarity. Then, induction heads attend to aligned tokens across repeated segments, promoting the correct answer. Our results reveal how PLMs solve this biological task by combining language-based pattern matching with specialized biological knowledge, thereby establishing a basis for studying more complex evolutionary processes in PLMs.

</details>

---

### 20. [ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203)

**基本信息**

- 🔗 arXiv: [`2602.23203`](https://arxiv.org/abs/2602.23203)
- 👥 作者: Junhu Fu, Shuyu Liang, Wutong Li 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23203.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一个结合因果推理的机器学习理论框架，并应用于化学生物学领域。

**📖 中文摘要**

这篇论文题为《Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications》。它明确提出了一个新颖的理论框架，旨在将化学理论、生物理论、概率论和因果推理结合起来，以纠正当前机器学习在化学和生物学等自然科学领域应用中的因果缺陷。论文的核心是探索化学大模型（Machine Learning in Chemical Biology）的因果结构，并引入了“焦点（focus）”这一新概念，定义为机器学习算法在大型数据集中缩小到隐藏的底层机制的能力。论文还提供了对Akt抑制剂家族的初步原理验证。这直接针对“化学大模型”这一主题，旨在为化学生物学建立一种无需还原论工具的新型数学建模框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Colonoscopy video generation delivers dynamic, information-rich data critical for diagnosing intestinal diseases, particularly in data-scarce scenarios. High-quality video generation demands temporal consistency and precise control over clinical attributes, but faces challenges from irregular intestinal structures, diverse disease representations, and various imaging modalities. To this end, we propose ColoDiff, a diffusion-based framework that generates dynamic-consistent and content-aware colonoscopy videos, aiming to alleviate data shortage and assist clinical analysis. At the inter-frame level, our TimeStream module decouples temporal dependency from video sequences through a cross-frame tokenization mechanism, enabling intricate dynamic modeling despite irregular intestinal structures. At the intra-frame level, our Content-Aware module incorporates noise-injected embeddings and learnable prototypes to realize precise control over clinical attributes, breaking through the coarse guidance of diffusion models. Additionally, ColoDiff employs a non-Markovian sampling strategy that cuts steps by over 90% for real-time generation. ColoDiff is evaluated across three public datasets and one hospital database, based on both generation metrics and downstream tasks including disease diagnosis, modality discrimination, bowel preparation scoring, and lesion segmentation. Extensive experiments show ColoDiff generates videos with smooth transitions and rich dynamics. ColoDiff presents an effort in controllable colonoscopy video generation, revealing the potential of synthetic videos in complementing authentic representation and mitigating data scarcity in clinical settings.

</details>

---

### 21. [Survey on Neural Routing Solvers](https://arxiv.org/abs/2602.21761)

**基本信息**

- 🔗 arXiv: [`2602.21761`](https://arxiv.org/abs/2602.21761)
- 👥 作者: Yunpeng Ba, Xi Lin, Changliang Zhou 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21761.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于神经路由求解器的综述，系统地回顾了基于深度学习的优化求解器。其方法论和见解对于化学信息学中利用“化学大模型”解决分子设计、反应预测等优化问题具有重要的相关性和参考价值，属于相关领域的综述。

**📖 中文摘要**

这篇论文题为《Survey on Neural Routing Solvers》。论文对神经路由求解器（NRSs）进行了综述。NRSs利用深度学习来解决车辆路径问题，通过从数据中学习隐式启发式规则，取代了经典启发式框架中手工设计的部分。综述从启发式的角度回顾了现有的NRSs，并引入了基于启发式原则的分层分类法。此外，还提出了一个专注于泛化能力的评估流程。虽然主题是运筹学，但论文的核心是综述“神经”求解器（即基于神经网络的模型）如何学习解决组合优化问题。这种“学习优化”的范式与化学信息学中利用机器学习解决分子优化、逆合成规划等问题在方法论上高度相关，可被视为“化学大模型”在优化任务上的一个类比和参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural routing solvers (NRSs) that leverage deep learning to tackle vehicle routing problems have demonstrated notable potential for practical applications. By learning implicit heuristic rules from data, NRSs replace the handcrafted counterparts in classic heuristic frameworks, thereby reducing reliance on costly manual design and trial-and-error adjustments. This survey makes two main contributions: (1) The heuristic nature of NRSs is highlighted, and existing NRSs are reviewed from the perspective of heuristics. A hierarchical taxonomy based on heuristic principles is further introduced. (2) A generalization-focused evaluation pipeline is proposed to address limitations of the conventional pipeline. Comparative benchmarking of representative NRSs across both pipelines uncovers a series of previously unreported gaps in current research.

</details>

---

### 22. [CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction](https://arxiv.org/abs/2602.22236)

**基本信息**

- 🔗 arXiv: [`2602.22236`](https://arxiv.org/abs/2602.22236)
- 👥 作者: Rabeya Tus Sadia, Qiang Ye, Qiang Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22236.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是利用生物大语言模型（BioLLMs）进行RNA相互作用预测，这直接关联“化学大模型”在化学信息学领域的应用。

**📖 中文摘要**

这篇论文题为《CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction》。论文提出了一种名为CrossLLM-Mamba的新框架，用于预测RNA相关的相互作用（如RNA-蛋白质、RNA-小分子、RNA-RNA）。该框架利用生物大语言模型（BioLLMs，如ESM-2和RiNALMo）提供强大的序列表示，并通过双向Mamba编码器实现跨模态的深度“串扰”。其核心是将相互作用预测重新表述为一个状态空间对齐问题，通过隐藏状态传播对交互进行动态建模。这项工作展示了大型语言模型（作为“化学大模型”的一种形式）在生物分子相互作用预测这一化学信息学核心问题上的创新应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of RNA-associated interactions is essential for understanding cellular regulation and advancing drug discovery. While Biological Large Language Models (BioLLMs) such as ESM-2 and RiNALMo provide powerful sequence representations, existing methods rely on static fusion strategies that fail to capture the dynamic, context-dependent nature of molecular binding. We introduce CrossLLM-Mamba, a novel framework that reformulates interaction prediction as a state-space alignment problem. By leveraging bidirectional Mamba encoders, our approach enables deep ``crosstalk'' between modality-specific embeddings through hidden state propagation, modeling interactions as dynamic sequence transitions rather than static feature overlaps. The framework maintains linear computational complexity, making it scalable to high-dimensional BioLLM embeddings. We further incorporate Gaussian noise injection and Focal Loss to enhance robustness against hard-negative samples. Comprehensive experiments across three interaction categories, RNA-protein, RNA-small molecule, and RNA-RNA demonstrate that CrossLLM-Mamba achieves state-of-the-art performance. On the RPI1460 benchmark, our model attains an MCC of 0.892, surpassing the previous best by 5.2\%. For binding affinity prediction, we achieve Pearson correlations exceeding 0.95 on riboswitch and repeat RNA subtypes. These results establish state-space modeling as a powerful paradigm for multi-modal biological interaction prediction.

</details>

---

### 23. [VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction](https://arxiv.org/abs/2602.22239)

**基本信息**

- 🔗 arXiv: [`2602.22239`](https://arxiv.org/abs/2602.22239)
- 👥 作者: Ida Egendal, Rasmus Froberg Brøndum, Dan J Woodcock 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22239.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一种用于突变特征提取的深度学习模型（VAE），这是化学信息学和生物信息学中数据分析的一个具体应用，属于“化学大模型”在特定任务上的实例。

**📖 中文摘要**

这篇论文题为《VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction》。论文提出了一种用于突变特征提取的新型变分自编码器（VAE-MS）。突变特征分析是癌症基因组学中的关键方法，用于识别导致癌症发展的潜在生物学过程。VAE-MS结合了非对称架构和概率方法，旨在从癌症突变数据中更可靠地提取特征。该模型与包括SigProfilerExtractor（NMF方法）、MUSE-XAE（自编码器）和SigneR（贝叶斯NMF）在内的最先进模型进行了比较。这项工作展示了深度学习模型（特别是变分自编码器）在化学/生物信息学数据分析任务中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mutational signature analysis has emerged as a powerful method for uncovering the underlying biological processes driving cancer development. However, the signature extraction process, typically performed using non-negative matrix factorization (NMF), often lacks reliability and clinical applicability. To address these limitations, several solutions have been introduced, including the use of neural networks to achieve more accurate estimates and probabilistic methods to better capture natural variation in the data. In this work, we introduce a Variational Autoencoder for Mutational Signatures (VAE-MS), a novel model that leverages both an asymmetric architecture and probabilistic methods for the extraction of mutational signatures. VAE-MS is compared to with three state-of-the-art models for mutational signature extraction: SigProfilerExtractor, the NMF-based gold standard; MUSE-XAE, an autoencoder that employs an asymmetric design without probabilistic components; and SigneR, a Bayesian NMF model, to illustrate the strength in combining a nonlinear extraction with a probabilistic model. In the ability to reconstruct input data and generalize to unseen data, models with probabilistic components (VAE-MS, SigneR) dramatically outperformed models without (SigProfilerExtractor, MUSE-XAE). The NMF-baed models (SigneR, SigProfilerExtractor) had the most accurate reconstructions in simulated data, while VAE-MS reconstructed more accurately on real cancer data. Upon evaluating the ability to extract signatures consistently, no model exhibited a clear advantage over the others. Software for VAE-MS is available at this https URL .

</details>

---

### 24. [Stochastic Neural Networks for Quantum Devices](https://arxiv.org/abs/2602.22241)

**基本信息**

- 🔗 arXiv: [`2602.22241`](https://arxiv.org/abs/2602.22241)
- 👥 作者: Bodo Rosenhahn, Tobias J. Osborne, Christoph Hirche
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22241.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是在量子设备上实现随机神经网络，这属于量子机器学习领域，与未来可能用于化学模拟和物质科学计算的“化学大模型”的新型硬件实现相关。

**📖 中文摘要**

这篇论文题为《Stochastic Neural Networks for Quantum Devices》。论文提出了一种在基于门的量子计算中，将随机神经网络表达和优化为量子电路的表述方法。受经典感知器启发，引入了随机神经元并将其组合成量子神经网络。训练使用Kiefer-Wolfowitz算法结合模拟退火。论文展示了多种拓扑和模型，包括浅层全连接网络、Hopfield网络、受限玻尔兹曼机、自编码器和卷积神经网络，并演示了将优化后的神经网络作为Grover算法的预言机以实现量子生成AI模型。这项工作探索了在量子设备上实现神经网络，属于量子机器学习与化学信息学/计算化学的交叉前沿。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work presents a formulation to express and optimize stochastic neural networks as quantum circuits in gate-based quantum computing. Motivated by a classical perceptron, stochastic neurons are introduced and combined into a quantum neural network. The Kiefer-Wolfowitz algorithm in combination with simulated annealing is used for training the network weights. Several topologies and models are presented, including shallow fully connected networks, Hopfield Networks, Restricted Boltzmann Machines, Autoencoders and convolutional neural networks. We also demonstrate the combination of our optimized neural networks as an oracle for the Grover algorithm to realize a quantum generative AI model.

</details>

---

### 25. [Multi-Dimensional Spectral Geometry of Biological Knowledge in Single-Cell Transformer Representations](https://arxiv.org/abs/2602.22247)

**基本信息**

- 🔗 arXiv: [`2602.22247`](https://arxiv.org/abs/2602.22247)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22247.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析单细胞Transformer模型（scGPT）的内部表征，探索大模型如何编码生物学知识，直接关联“化学大模型”在生物信息学中的可解释性研究。

**📖 中文摘要**

这篇论文题为《Multi-Dimensional Spectral Geometry of Biological Knowledge in Single-Cell Transformer Representations》。论文系统地解码了单细胞基础模型scGPT（一种基于Transformer架构的模型）内部表征的几何结构。通过自动化假设筛选，研究发现scGPT将基因组织成一个结构化的生物坐标系，其中主导的光谱轴根据亚细胞定位分离基因，中间层编码线粒体和内质网等细胞器，正交轴编码蛋白质-蛋白质相互作用网络。这项工作深入分析了Transformer模型（一种大模型架构）在单细胞生物学数据中学到的生物学知识表示，揭示了其内部模型的生物学可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell foundation models such as scGPT learn high-dimensional gene representations, but what biological knowledge these representations encode remains unclear. We systematically decode the geometric structure of scGPT internal representations through 63 iterations of automated hypothesis screening (183 hypotheses tested), revealing that the model organizes genes into a structured biological coordinate system rather than an opaque feature space. The dominant spectral axis separates genes by subcellular localization, with secreted proteins at one pole and cytosolic proteins at the other. Intermediate transformer layers transiently encode mitochondrial and ER compartments in a sequence that mirrors the cellular secretory pathway. Orthogonal axes encode protein-protein interaction networks with graded fidelity to experimentally measured interaction strength (Spearman rho = 1.000 across n = 5 STRING confidence quintiles, p = 0.017). In a compact six-dimensional spectral subspace, the model distinguishes transcription factors from their target genes (AUROC = 0.744, all 12 layers significant). Early layers preserve which specific genes regulate which targets, while deeper layers compress this into a coarser regulator versus regulated distinction. Repression edges are geometrically more prominent than activation edges, and B-cell master regulators BATF and BACH2 show convergence toward the B-cell identity anchor PAX5 across transformer depth. Cell-type marker genes cluster with high fidelity (AUROC = 0.851). Residual-stream geometry encodes biological structure complementary to attention patterns. These results indicate that biological transformers learn an interpretable internal model of cellular organization, with implications for regulatory network inference, drug target prioritization, and model auditing.

</details>

---

### 26. [Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)](https://arxiv.org/abs/2602.22248)

**基本信息**

- 🔗 arXiv: [`2602.22248`](https://arxiv.org/abs/2602.22248)
- 👥 作者: Julia Gonski, Jenni Ott, Shiva Abbaszadeh 等100人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22248.pdf)

**💡 相关性分析**

满足标准3：论文是一份展望性白皮书，广泛讨论了机器学习在异构、边缘和量子硬件上的应用，其中涉及的实时推理、边缘AI和数据缩减等主题，对于实现高效的“质谱结构推理”系统具有重要的相关性和前瞻性讨论价值。

**📖 中文摘要**

这篇论文题为《Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)》。这是一份社区驱动的白皮书，旨在确定和优先考虑基于硬件的机器学习系统及其在物理学（特别是粒子物理学）应用中的研发机会。白皮书讨论了人工智能/机器学习、硅微电子学以及量子算法和处理等新兴技术的交叉领域，包括边缘计算、异构加速器系统、可重构硬件、协同设计策略以及模拟计算等。虽然主要面向粒子物理，但其关于在极端环境下（如高辐射）实现高效、低延迟ML推理的讨论，对于未来在实验室仪器（如质谱仪）端进行实时“质谱结构推理”具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The next generation of particle physics experiments will face a new era of challenges in data acquisition, due to unprecedented data rates and volumes along with extreme environments and operational constraints. Harnessing this data for scientific discovery demands real-time inference and decision-making, intelligent data reduction, and efficient processing architectures beyond current capabilities. Crucial to the success of this experimental paradigm are several emerging technologies, such as artificial intelligence and machine learning (AI/ML) and silicon microelectronics, and the advent of quantum algorithms and processing. Their intersection includes areas of research such as low-power and low-latency devices for edge computing, heterogeneous accelerator systems, reconfigurable hardware, novel codesign and synthesis strategies, readout for cryogenic or high-radiation environments, and analog computing. This white paper presents a community-driven vision to identify and prioritize research and development opportunities in hardware-based ML systems and corresponding physics applications, contributing towards a successful transition to the new data frontier of fundamental science.

</details>

---

### 27. [Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486)

**基本信息**

- 🔗 arXiv: [`2602.22486`](https://arxiv.org/abs/2602.22486)
- 👥 作者: Shivam Kumar, Yixin Wang, Lizhen Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22486.pdf)

**💡 相关性分析**

满足标准1：论文的核心理论分析直接围绕生成模型（流匹配）在低维流形数据（如分子结构）上的有效性展开，这与化学大模型中的生成建模主题高度相关。

**📖 中文摘要**

本文从理论角度分析了流匹配（Flow Matching）方法在目标分布位于低维流形上的情况。流匹配是一种免模拟的生成建模方法，通过学习源分布（如标准正态分布）与目标数据分布之间的插值路径上的速度场来生成样本。论文证明了当目标分布支撑在光滑流形上时，流匹配能够自适应于数据的内在几何结构，其学习到的速度场具有非渐近收敛保证，并且由此产生的隐式密度估计器具有统计一致性。收敛速率接近极小极大最优，且仅依赖于流形的内在维数。这项工作为流匹配在分子结构生成等数据集中于低维流形的场景中的有效性提供了理论解释，与【化学大模型】中生成模型的研究主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow matching has emerged as a simulation-free alternative to diffusion-based generative modeling, producing samples by solving an ODE whose time-dependent velocity field is learned along an interpolation between a simple source distribution (e.g., a standard normal) and a target data distribution. Flow-based methods often exhibit greater training stability and have achieved strong empirical performance in high-dimensional settings where data concentrate near a low-dimensional manifold, such as text-to-image synthesis, video generation, and molecular structure generation. Despite this success, existing theoretical analyses of flow matching assume target distributions with smooth, full-dimensional densities, leaving its effectiveness in manifold-supported settings largely unexplained. To this end, we theoretically analyze flow matching with linear interpolation when the target distribution is supported on a smooth manifold. We establish a non-asymptotic convergence guarantee for the learned velocity field, and then propagate this estimation error through the ODE to obtain statistical consistency of the implicit density estimator induced by the flow-matching objective. The resulting convergence rate is near minimax-optimal, depends only on the intrinsic dimension, and reflects the smoothness of both the manifold and the target distribution. Together, these results provide a principled explanation for how flow matching adapts to intrinsic data geometry and circumvents the curse of dimensionality.

</details>

---

### 28. [Discovery of Interpretable Physical Laws in Materials via Language-Model-Guided Symbolic Regression](https://arxiv.org/abs/2602.22967)

**基本信息**

- 🔗 arXiv: [`2602.22967`](https://arxiv.org/abs/2602.22967)
- 👥 作者: Yifeng Guan, Chuyi Liu, Dongzhan Zhou 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22967.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（作为化学大模型的一种基础）来引导符号回归，以发现材料科学中的物理定律，直接围绕化学大模型的应用主题。

**📖 中文摘要**

本文提出了一种利用大型语言模型（LLM）引导符号回归（Symbolic Regression）来从高维数据中发现可解释物理定律的框架。该方法旨在克服传统符号回归在搜索巨大可能形式空间时产生复杂、非物理解析式的缺点。通过利用LLM中嵌入的科学知识来引导搜索过程，该方法能够高效地从数据中识别物理定律。作者以钙钛矿材料的关键性质建模为例验证了该方法。该方法将传统符号回归中常见的组合爆炸问题减轻了约10^5倍，并识别出了一组关于体模量、带隙和析氧反应活性的新公式，这些公式不仅提供了有意义的物理见解，而且在准确性和简洁性上超越了先前的公式。这项工作直接应用了【化学大模型】中的基础模型（LLM）来指导科学发现，属于核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering interpretable physical laws from high-dimensional data is a fundamental challenge in scientific research. Traditional methods, such as symbolic regression, often produce complex, unphysical formulas when searching a vast space of possible forms. We introduce a framework that guides the search process by leveraging the embedded scientific knowledge of large language models, enabling efficient identification of physical laws in the data. We validate our approach by modeling key properties of perovskite materials. Our method mitigates the combinatorial explosion commonly encountered in traditional symbolic regression, reducing the effective search space by a factor of approximately $10^5$. A set of novel formulas for bulk modulus, band gap, and oxygen evolution reaction activity are identified, which not only provide meaningful physical insights but also outperform previous formulas in accuracy and simplicity.

</details>

---

### 29. [Efficient Graph Coloring with Neural Networks: A Physics-Inspired Approach for Large Graphs](https://arxiv.org/abs/2408.01503)

**基本信息**

- 🔗 arXiv: [`2408.01503`](https://arxiv.org/abs/2408.01503)
- 👥 作者: Lorenzo Colantonio, Andrea Cacioppo, Federico Scarpati 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2408.01503.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合图神经网络和统计力学原理的神经求解器框架，用于解决图着色等组合优化问题。这类基于深度学习的求解器与化学大模型中用于分子优化、性质预测的模型在方法论上高度相关。

**📖 中文摘要**

本文介绍了一个受物理学启发的神经框架，用于通过学习解决大规模图着色问题。该框架结合了图神经网络（GNN）和统计力学原理，集成了基于种植的监督信号、对称性破缺正则化和迭代噪声退火神经动力学，以在聚集的解空间中导航。当迭代次数与图规模呈二次方关系时，学习到的求解器在随机图中能达到接近理论动态相变的算法阈值，并在种植推断机制中实现接近最优的检测性能。该模型能够从小的训练图推广到规模大几个数量级的实例，证明了神经架构可以学习到在组合优化和推断的硬连通区域中仍然有效的可扩展算法策略。这项工作展示了【化学大模型】相关技术（如图神经网络、生成模型/求解器）在复杂优化问题中的应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Combinatorial optimization problems near algorithmic phase transitions represent a fundamental challenge for both classical algorithms and machine learning approaches. Among them, graph coloring stands as a prototypical constraint satisfaction problem exhibiting sharp dynamical and satisfiability thresholds. Here we introduce a physics-inspired neural framework that learns to solve large-scale graph coloring instances by combining graph neural networks with statistical-mechanics principles. Our approach integrates a planting-based supervised signal, symmetry-breaking regularization, and iterative noise-annealed neural dynamics to navigate clustered solution landscapes. When the number of iterations scales quadratically with graph size, the learned solver reaches algorithmic thresholds close to the theoretical dynamical transition in random graphs and achieves near-optimal detection performance in the planted inference regime. The model generalizes from small training graphs to instances orders of magnitude larger, demonstrating that neural architectures can learn scalable algorithmic strategies that remain effective in hard connectivity regions. These results establish a general paradigm for learning neural solvers that operate near fundamental phase boundaries in combinatorial optimization and inference.

</details>

---

### 30. [Neuro-Symbolic AI for Analytical Solutions of Differential Equations](https://arxiv.org/abs/2502.01476)

**基本信息**

- 🔗 arXiv: [`2502.01476`](https://arxiv.org/abs/2502.01476)
- 👥 作者: Orestis Oikonomou, Levi Lingsch, Dana Grund 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.01476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个神经符号AI框架（SIGS），用于自动发现微分方程的解析解。神经符号AI是化学大模型的一个重要研究方向，用于实现可解释和可靠的分子设计与性质预测。

**📖 中文摘要**

本文介绍了SIGS，一个用于自动求解微分方程解析解的神经符号框架。SIGS使用形式语法生成语法上有效的构建块，将这些表达式嵌入连续空间，然后在该空间中搜索，通过最小化基于物理的残差来组装、评分和细化候选的闭式解。这种设计将符号推理与数值优化统一起来。SIGS是第一个能够（i）解析求解非线性偏微分方程耦合系统，（ii）在语法未完全指定的情况下发现解，以及（iii）为缺乏已知闭式解的偏微分方程产生精确符号近似的神经符号方法。这项工作展示了【化学大模型】中神经符号AI和生成模型在解决科学计算问题（如计算化学中的微分方程）方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Analytical solutions to differential equations offer exact, interpretable insight but are rarely available because discovering them requires expert intuition or exhaustive search in combinatorial spaces. We introduce SIGS, a neuro-symbolic framework that automates this process. SIGS uses a formal grammar to generate only syntactically valid building blocks, embeds these expressions into a continuous space, and then searches this space to assemble, score, and refine candidate closed-form solutions by minimizing a physics-based residual. This design unifies symbolic reasoning with numerical optimization; the grammar constrains candidate solution blocks to be proper by construction, while the latent search makes exploration tractable and data-free. SIGS is the first neuro-symbolic method to (i) analytically solve coupled systems of nonlinear PDEs, (ii) discover solutions under grammar misspecification, and (iii) produce accurate symbolic approximations for PDEs lacking known closed-form solutions. Overall, SIGS achieves orders-of-magnitude improvements in accuracy and efficiency over existing symbolic methods on standard benchmarks.

</details>

---

### 31. [CLIP-Free, Label Free, Unsupervised Concept Bottleneck Models](https://arxiv.org/abs/2503.10981)

**基本信息**

- 🔗 arXiv: [`2503.10981`](https://arxiv.org/abs/2503.10981)
- 👥 作者: Fawaz Sammani, Jonas Fischer, Nikos Deligiannis
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.10981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的、无需外部标注或CLIP模型的概念瓶颈模型（CBM）。CBM是实现可解释AI的关键架构，其改进与化学大模型中追求可解释性和可靠性的目标直接相关。

**📖 中文摘要**

本文提出了一种无需CLIP模型、无需图像-概念标注、且以无监督方式推导线性分类器的概念瓶颈模型（CBM）构建方法。该方法通过将任何冻结的视觉分类器的分布（在离散类别索引上）与其从文本类别名称导出的对应视觉-语言分布对齐，同时保持分类器的性能，从而将分类器转换为CBM。该方法不需要真实图像-类别标注，具有很高的数据效率，并保留了分类器的推理过程。在超过40个视觉分类器上的应用和测试表明，所得到的无监督、无标签且无CLIP的CBM（U-F^2-CBM）达到了新的最先进水平，甚至超过了有监督的基于CLIP的CBM。这项工作挑战了现有CBM对CLIP或人工标注的依赖，为构建更通用的【化学大模型】（例如用于分子性质预测的可解释模型）提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) map dense feature representations into human-interpretable concepts which are then combined linearly to make a prediction. However, modern CBMs rely on the CLIP model to obtain image-concept annotations, and it remains unclear how to design CBMs without the CLIP bottleneck. Methods that do not use CLIP instead require manual, labor intensive annotation to associate feature representations with concepts. Furthermore, all CBMs necessitate training a linear classifier to map the extracted concepts to class labels. In this work, we lift all three limitations simultaneously by proposing a method that converts any frozen visual classifier into a CBM without requiring image-concept labels (label-free), without relying on the CLIP model (CLIP-free), and by deriving the linear classifier in an unsupervised manner. Our method is formulated by aligning the original classifier's distribution (over discrete class indices) with its corresponding vision-language counterpart distribution derived from textual class names, while preserving the classifier's performance. The approach requires no ground-truth image-class annotations, and is highly data-efficient and preserves the classifier's reasoning process. Applied and tested on over 40 visual classifiers, our resulting unsupervised, label-free and CLIP-free CBM (U-F$^2$-CBM) sets a new state of the art, surpassing even supervised CLIP-based CBMs. We also show that our method can be used for zero-shot image captioning, outperforming existing methods based on CLIP, and achieving state-of-art.

</details>

---

### 32. [The Spacetime of Diffusion Models: An Information Geometry Perspective](https://arxiv.org/abs/2505.17517)

**基本信息**

- 🔗 arXiv: [`2505.17517`](https://arxiv.org/abs/2505.17517)
- 👥 作者: Rafał Karczewski, Markus Heinonen, Alison Pouplin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.17517.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散模型的几何结构和潜在表示展开。扩散模型是当前化学信息学和分子生成领域（作为化学大模型的一种重要形式）的核心生成模型之一。论文提出的扩散编辑距离和过渡路径采样方法，直接关联于分子结构生成、编辑和构象采样等化学信息学任务，属于化学大模型研究范畴。

**📖 中文摘要**

本文从信息几何的角度为扩散模型的潜在空间提供了一个新颖的几何视角。作者指出，标准的基于确定性概率流ODE解码器的回拉方法存在根本性缺陷，因为它迫使测地线在数据空间中解码为直线段，从而忽略了数据的内在几何结构。作为补充，扩散模型也允许通过反向SDE进行随机解码，这为使用Fisher-Rao度量的信息几何处理提供了可能。为了解决因使用x_T作为潜在表示而导致度量坍缩的问题，作者引入了一个潜在时空z=(x_t, t)，该时空索引了所有噪声尺度下的去噪分布族p(x_0 | x_t)，从而产生了一个非平凡的几何结构。作者证明了这些分布形成了一个指数族，并推导了曲线长度的无模拟估计器，实现了高效的测地线计算。由此产生的结构引入了一种原则性的扩散编辑距离，其中测地线追踪数据之间噪声和去噪编辑的最小序列。作者还展示了该方法在分子系统（包括低方差过渡和区域规避等约束变体）中过渡路径采样的优势。这项工作为理解和操作扩散模型的潜在几何结构提供了理论基础，与化学信息学中利用生成模型（如扩散模型）进行分子结构生成和推理的研究主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a novel geometric perspective on the latent space of diffusion models. We first show that the standard pullback approach, utilizing the deterministic probability flow ODE decoder, is fundamentally flawed. It provably forces geodesics to decode as straight segments in data space, effectively ignoring any intrinsic data geometry beyond the ambient Euclidean space. Complementing this view, diffusion also admits a stochastic decoder via the reverse SDE, which enables an information geometric treatment with the Fisher-Rao metric. However, a choice of $x_T$ as the latent representation collapses this metric due to memorylessness. We address this by introducing a latent spacetime $z=(x_t,t)$ that indexes the family of denoising distributions $p(x_0 | x_t)$ across all noise scales, yielding a nontrivial geometric structure. We prove these distributions form an exponential family and derive simulation-free estimators for curve lengths, enabling efficient geodesic computation. The resulting structure induces a principled Diffusion Edit Distance, where geodesics trace minimal sequences of noise and denoise edits between data. We also demonstrate benefits for transition path sampling in molecular systems, including constrained variants such as low-variance transitions and region avoidance. Code is available at: this https URL .

</details>

---

### 33. [Random Matrix Theory-guided sparse PCA for single-cell RNA-seq data](https://arxiv.org/abs/2509.15429)

**基本信息**

- 🔗 arXiv: [`2509.15429`](https://arxiv.org/abs/2509.15429)
- 👥 作者: Victor Chardès
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.15429.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的数据处理和分析方法（RMT引导的稀疏PCA），并应用于单细胞RNA-seq数据。虽然论文本身不直接涉及质谱，但其核心是开发用于高维、噪声生物数据的降维和特征提取算法。这类算法（如PCA的变体、稀疏表示）是化学信息学和质谱数据分析（例如，用于质谱峰降维、特征选择或结构推理的预处理步骤）中的基础工具。因此，它提供了可用于相关主题的数据分析工具。

**📖 中文摘要**

本文提出了一种基于随机矩阵理论（RMT）的稀疏主成分分析（PCA）方法，用于处理单细胞RNA测序数据。单细胞RNA-seq数据噪声高、维度高，传统的PCA方法在高维情况下存在偏差。作者的方法首先引入了一种新颖的双白化算法，该算法能够自洽地估计每个基因在每个细胞中的转录组噪声大小，而无需假设特定的噪声分布。这使得能够使用基于RMT的标准自动选择稀疏度水平，从而使稀疏PCA几乎无需参数调整。这种基于数学原理的方法保留了PCA的可解释性，同时能够稳健、自动地推断稀疏主成分。作者在七种单细胞RNA-seq技术和四种稀疏PCA算法上进行了测试，结果表明该方法系统地改善了主成分子空间的重建，并在细胞类型分类任务中持续优于基于PCA、自编码器和扩散的方法。该方法为高维生物数据的降维和特征提取提供了新的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell RNA-seq provides detailed molecular snapshots of individual cells but is notoriously noisy. Variability stems from biological differences and technical factors, such as amplification bias and limited RNA capture efficiency, making it challenging to adapt computational pipelines to heterogeneous datasets or evolving technologies. As a result, most studies still rely on principal component analysis (PCA) for dimensionality reduction, valued for its interpretability and robustness, in spite of its known bias in high dimensions. Here, we improve upon PCA with a Random Matrix Theory (RMT)-based approach that guides the inference of sparse principal components using existing sparse PCA algorithms. We first introduce a novel biwhitening algorithm which self-consistently estimates the magnitude of transcriptomic noise affecting each gene in individual cells, without assuming a specific noise distribution. This enables the use of an RMT-based criterion to automatically select the sparsity level, rendering sparse PCA nearly parameter-free. Our mathematically grounded approach retains the interpretability of PCA while enabling robust, hands-off inference of sparse principal components. Across seven single-cell RNA-seq technologies and four sparse PCA algorithms, we show that this method systematically improves the reconstruction of the principal subspace and consistently outperforms PCA-, autoencoder-, and diffusion-based methods in cell-type classification tasks.

</details>

---

### 34. [Inducing Dyslexia in Vision Language Models](https://arxiv.org/abs/2509.24597)

**基本信息**

- 🔗 arXiv: [`2509.24597`](https://arxiv.org/abs/2509.24597)
- 👥 作者: Melika Honarmand, Ayati Sharma, Badr AlKhamissi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大规模视觉语言模型（VLMs）来模拟和理解阅读障碍的认知机制。虽然应用领域是神经科学，但其方法论核心是探究和操纵AI模型（VLMs）的内部表示与特定功能（如词汇处理）之间的因果关系。这种“模型作为认知模拟器”的研究范式，与化学信息学中利用“化学大模型”（如分子语言模型或扩散模型）来理解和预测分子性质、反应或结构的内部机制的研究思路高度相似。两者都涉及对复杂AI模型进行机理解释和功能操控，以解决特定领域的科学问题。

**📖 中文摘要**

本文利用大规模视觉语言模型（VLMs）来模拟阅读障碍（一种以持续阅读困难为特征的神经发育障碍）。阅读障碍通常与腹侧枕颞皮层视觉词形区（VWFA）活动减少有关。传统研究阅读障碍的方法（如行为和神经影像学）在测试阅读障碍潜在机制的因果假设方面能力有限。在本研究中，作者通过功能性地识别和扰动人工词汇处理的类似物来模拟阅读障碍。利用认知神经科学的刺激，作者在VLM中识别了视觉词形选择性单元，并证明它们可以预测人类VWFA的神经反应。消融模型的VWF单元会导致阅读任务的选择性损伤，而一般的视觉和语言理解能力保持完整。具体来说，由此产生的模型在没有显著改变正字法处理的情况下，匹配了阅读障碍患者的语音缺陷，并在字体敏感性方面反映了阅读障碍行为。总之，作者的建模结果复制了阅读障碍的关键特征，并为研究脑部疾病建立了一个计算框架。这项工作展示了使用AI模型模拟和理解复杂认知过程的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dyslexia, a neurodevelopmental disorder characterized by persistent reading difficulties, is often linked to reduced activity of the visual word form area (VWFA) in the ventral occipito-temporal cortex. Traditional approaches to studying dyslexia, such as behavioral and neuroimaging methods, have provided valuable insights but remain limited in their ability to test causal hypotheses about the underlying mechanisms of reading impairments. In this study, we use large-scale vision-language models (VLMs) to simulate dyslexia by functionally identifying and perturbing artificial analogues of word processing. Using stimuli from cognitive neuroscience, we identify visual-word-form-selective units within VLMs and demonstrate that they predict human VWFA neural responses. Ablating model VWF units leads to selective impairments in reading tasks while general visual and language comprehension abilities remain intact. In particular, the resulting model matches dyslexic humans' phonological deficits without a significant change in orthographic processing, and mirrors dyslexic behavior in font sensitivity. Taken together, our modeling results replicate key characteristics of dyslexia and establish a computational framework for investigating brain disorders.

</details>

---

### 35. [Mapping Semantic & Syntactic Relationships with Geometric Rotation](https://arxiv.org/abs/2510.09790)

**基本信息**

- 🔗 arXiv: [`2510.09790`](https://arxiv.org/abs/2510.09790)
- 👥 作者: Michael Freenor, Lauren Alvarez
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.09790.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和形式化AI模型（特别是语言嵌入模型）内部表示中语义和句法关系的几何结构。它提出了RISE方法来识别和操作这些关系。这与“化学大模型”的研究密切相关，因为在化学信息学中，一个核心挑战是理解分子表示（如SMILES字符串、图神经网络嵌入或扩散模型潜在向量）如何编码化学结构和性质之间的关系。论文中探索“关系几何”的方法论（如将转换建模为旋转）可以为化学大模型中分子相似性、性质预测和结构转换（例如，反应预测、分子优化）的表示学习提供新的视角和工具。

**📖 中文摘要**

本文旨在理解语言和嵌入模型如何编码语义关系，这是模型可解释性的基础。早期词嵌入展示了直观的向量算术（如“国王”-“男人”+“女人”=“女王”），但现代高维文本表示缺乏直接可解释的几何特性。作者引入了转子不变位移估计（RISE），一种几何方法，将语义-句法转换表示为嵌入空间中一致的旋转操作，利用了现代语言表示的流形结构。RISE操作能够跨语言和跨模型工作而不降低性能，这表明存在跨语言的类似几何结构。作者使用两种基线方法、三种嵌入模型、三个数据集以及五个主要语系中的七种形态多样的语言来比较和评估RISE。结果表明，RISE能够一致地映射具有不同语法特征（如否定和条件性）的话语级语义-句法转换。这项工作首次证明，话语级语义-句法转换对应于多语言嵌入空间中一致的几何操作，在句子层面为线性表示假说提供了实证支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding how language and embedding models encode semantic relationships is fundamental to model interpretability. While early word embeddings exhibited intuitive vector arithmetic (''king'' - ''man'' + ''woman'' = ''queen''), modern high-dimensional text representations lack straightforward interpretable geometric properties. We introduce Rotor-Invariant Shift Estimation (RISE), a geometric approach that represents semantic-syntactic transformations as consistent rotational operations in embedding space, leveraging the manifold structure of modern language representations. RISE operations have the ability to operate across both languages and models without reducing performance, suggesting the existence of analogous cross-lingual geometric structure. We compare and evaluate RISE using two baseline methods, three embedding models, three datasets, and seven morphologically diverse languages in five major language groups. Our results demonstrate that RISE consistently maps discourse-level semantic-syntactic transformations with distinct grammatical features (e.g., negation and conditionality) across languages and models. This work provides the first demonstration that discourse-level semantic-syntactic transformations correspond to consistent geometric operations in multilingual embedding spaces, empirically supporting the linear representation hypothesis at the sentence level.

</details>

---

### 36. [AngelSlim: A more accessible, comprehensive, and efficient toolkit for large model compression](https://arxiv.org/abs/2602.21233)

**基本信息**

- 🔗 arXiv: [`2602.21233`](https://arxiv.org/abs/2602.21233)
- 👥 作者: Rui Cen, QiangQiang Hu, Hong Huang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21233.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为AngelSlim的综合工具包，专门用于大模型（包括可能的化学大模型）的压缩和加速。它提供了量化、推测解码、令牌剪枝等多种算法和工具，是开发和部署高效化学大模型的重要资源。

**📖 中文摘要**

本技术报告介绍了AngelSlim，一个由腾讯混元团队开发的用于大模型压缩的全面且多功能的工具包。它整合了包括量化、推测解码、令牌剪枝和蒸馏在内的前沿算法，提供了一个统一的流水线，简化了从模型压缩到工业规模部署的过渡。为了促进高效加速，我们集成了最先进的FP8和INT8训练后量化算法，以及在超低位领域的前沿研究，其中HY-1.8B-int2是首个工业上可行的2位大模型。除了量化，我们还提出了一个与多模态架构和现代推理引擎兼容的训练对齐推测解码框架，在不影响输出正确性的情况下实现了1.8倍到2.倍的吞吐量提升。此外，我们开发了一个无需训练的稀疏注意力框架，通过结合静态模式和动态令牌选择将稀疏内核与模型架构解耦，从而减少长上下文场景中的首令牌时间。对于多模态模型，AngelSlim整合了专门的剪枝策略。通过从底层实现整合这些压缩策略，AngelSlim支持以算法为中心的研究和工具辅助的部署。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This technical report introduces AngelSlim, a comprehensive and versatile toolkit for large model compression developed by the Tencent Hunyuan team. By consolidating cutting-edge algorithms, including quantization, speculative decoding, token pruning, and distillation. AngelSlim provides a unified pipeline that streamlines the transition from model compression to industrial-scale deployment. To facilitate efficient acceleration, we integrate state-of-the-art FP8 and INT8 Post-Training Quantization (PTQ) algorithms alongside pioneering research in ultra-low-bit regimes, featuring HY-1.8B-int2 as the first industrially viable 2-bit large model. Beyond quantization, we propose a training-aligned speculative decoding framework compatible with multimodal architectures and modern inference engines, achieving 1.8x to 2.0x throughput gains without compromising output correctness. Furthermore, we develop a training-free sparse attention framework that reduces Time-to-First-Token (TTFT) in long-context scenarios by decoupling sparse kernels from model architectures through a hybrid of static patterns and dynamic token selection. For multimodal models, AngelSlim incorporates specialized pruning strategies, namely IDPruner for optimizing vision tokens via Maximal Marginal Relevance and Samp for adaptive audio token merging and pruning. By integrating these compression strategies from low-level implementations, AngelSlim enables algorithm-focused research and tool-assisted deployment.

</details>

---

### 37. [Understanding protein function with a multimodal retrieval-augmented foundation model](https://arxiv.org/abs/2508.04724)

**基本信息**

- 🔗 arXiv: [`2508.04724`](https://arxiv.org/abs/2508.04724)
- 👥 作者: Timothy Fei Truong Jr, Tristan Bepler
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.04724.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质序列和功能理解的化学大模型（PoET-2）。它直接围绕‘化学大模型’这一主题，旨在通过多模态和检索增强技术提升对蛋白质功能的理解和预测能力。

**📖 中文摘要**

这篇论文介绍了PoET-2，一个多模态、检索增强的蛋白质基础模型。该模型通过结合家族特异性进化约束的上下文学习和可选的结构条件，来学习蛋白质序列的生成分布。PoET-2采用分层Transformer编码器和具有因果与掩码语言建模目标的双解码器架构，使其能够在完全生成和双向表示学习两种模式下工作。论文指出，PoET-2在零样本变异效应预测上达到了最先进的性能，特别擅长对包含多个突变和具有挑战性的插入缺失突变进行评分。在监督设置下，PoET-2的嵌入在序列-功能关系学习方面优于先前的方法，尤其是在小数据集上。这项工作强调了将检索增强与多模态、以家族为中心的建模相结合，对于推进蛋白质基础模型的益处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (PLMs) learn probability distributions over natural protein sequences. By learning from hundreds of millions of natural protein sequences, protein understanding and design capabilities emerge. Recent works have shown that scaling these models improves structure prediction, but does not seem to improve mutation understanding and representation quality for protein function prediction. We introduce PoET-2, a multimodal, retrieval-augmented protein foundation model that incorporates in-context learning of family-specific evolutionary constraints with optional structure conditioning to learn generative distributions over protein sequences. PoET-2 uses a hierarchical transformer encoder that is equivariant to sequence context ordering and a dual decoder architecture with both causal and masked language modeling objectives, allowing PoET-2 to operate in both fully generative and bidirectional representation learning modes. PoET-2 achieves state-of-the-art performance on zero-shot variant effect prediction, excelling at scoring variants with multiple mutations and challenging indel mutations. In supervised settings, PoET-2 embeddings outperform previous methods for learning sequence-function relationships, especially with small datasets. This work highlights the benefits of combining retrieval augmentation with multimodal, family-centric modeling for advancing protein foundation models.

</details>

---

### 38. [TokEye: Fast Signal Extraction for Fluctuating Time Series via Offline Self-Supervised Learning From Fusion Diagnostics to Bioacoustics](https://arxiv.org/abs/2602.20317)

**基本信息**

- 🔗 arXiv: [`2602.20317`](https://arxiv.org/abs/2602.20317)
- 👥 作者: Nathaniel Chen, Kouroche Bouchiat, Peter Steiner 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20317.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种通用工具（TokEye）和框架，用于从复杂的多诊断信号（如聚变诊断中的质谱类数据）中自动提取模式。这为‘质谱结构推理’（此处扩展理解为复杂光谱/信号的结构推理）提供了可用的数据处理工具和资源。

**📖 中文摘要**

本文提出了一个“信号优先”的自监督框架，用于从各种传感器的高噪声时频数据中自动提取相干和瞬态模式。该方法开发了一种通用工具，通过在多通道信号处理中采用非线性最优技术，并利用快速神经网络代理，从DIII-D托卡马克的快速磁学、电子回旋辐射、CO2干涉仪和束发射光谱测量中提取相干、准相干和瞬态模式。该框架在DIII-D、TJ-II和非聚变谱图数据上进行了测试。推理延迟为0.5秒，使其能够实现实时模式识别和大规模自动化数据库生成，用于先进的等离子体控制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Next-generation fusion facilities like ITER face a "data deluge," generating petabytes of multi-diagnostic signals daily that challenge manual analysis. We present a "signals-first" self-supervised framework for the automated extraction of coherent and transient modes from high-noise time-frequency data across a variety of sensors. We also develop a general-purpose method and tool for extracting coherent, quasi-coherent, and transient modes for fluctuation measurements in tokamaks by employing non-linear optimal techniques in multichannel signal processing with a fast neural network surrogate on fast magnetics, electron cyclotron emission, CO2 interferometers, and beam emission spectroscopy measurements from DIII-D. Results are tested on data from DIII-D, TJ-II, and non-fusion spectrograms. With an inference latency of 0.5 seconds, this framework enables real-time mode identification and large-scale automated database generation for advanced plasma control. Repository is in this https URL .

</details>

---

### 39. [Not Just How Much, But Where: Decomposing Epistemic Uncertainty into Per-Class Contributions](https://arxiv.org/abs/2602.21160)

**基本信息**

- 🔗 arXiv: [`2602.21160`](https://arxiv.org/abs/2602.21160)
- 👥 作者: Mame Diarra Toure, David A. Stephens
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21160.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进深度学习模型（可视为一种特定类型的“模型”）的不确定性量化方法，特别是通过分解认知不确定性来提供更精细的洞察。这直接与‘化学大模型’主题中模型的可解释性、可靠性评估相关，是构建更可靠化学AI模型的关键技术。

**📖 中文摘要**

在安全关键分类中，失败的代价通常是不对称的，然而贝叶斯深度学习用单一标量互信息（MI）来总结认知不确定性，无法区分模型的未知性涉及的是良性类别还是安全关键类别。本文提出将MI分解为每个类别的向量贡献C_k(x)。该分解源于熵的二阶泰勒展开；1/μ_k权重校正了边界抑制，并使C_k在稀有和常见类别之间具有可比性。通过构造，∑_k C_k ≈ MI。作者在三个任务上验证了C_k：糖尿病视网膜病变的选择性预测、临床和图像基准上的分布外检测，以及受控的标签噪声研究。结果表明，分解后的不确定性度量在选择性风险降低和暴露分布不对称偏移方面优于传统的MI。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In safety-critical classification, the cost of failure is often asymmetric, yet Bayesian deep learning summarises epistemic uncertainty with a single scalar, mutual information (MI), that cannot distinguish whether a model's ignorance involves a benign or safety-critical class. We decompose MI into a per-class vector $C_k(x)=\sigma_k^{2}/(2\mu_k)$, with $\mu_k{=}\mathbb{E}[p_k]$ and $\sigma_k^2{=}\mathrm{Var}[p_k]$ across posterior samples. The decomposition follows from a second-order Taylor expansion of the entropy; the $1/\mu_k$ weighting corrects boundary suppression and makes $C_k$ comparable across rare and common classes. By construction $\sum_k C_k \approx \mathrm{MI}$, and a companion skewness diagnostic flags inputs where the approximation degrades. After characterising the axiomatic properties of $C_k$, we validate it on three tasks: (i) selective prediction for diabetic retinopathy, where critical-class $C_k$ reduces selective risk by 34.7\% over MI and 56.2\% over variance baselines; (ii) out-of-distribution detection on clinical and image benchmarks, where $\sum_k C_k$ achieves the highest AUROC and the per-class view exposes asymmetric shifts invisible to MI; and (iii) a controlled label-noise study in which $\sum_k C_k$ shows less sensitivity to injected aleatoric noise than MI under end-to-end Bayesian training, while both metrics degrade under transfer learning. Across all tasks, the quality of the posterior approximation shapes uncertainty at least as strongly as the choice of metric, suggesting that how uncertainty is propagated through the network matters as much as how it is measured.

</details>

---

## 📊 数据统计
- 累计运行天数：4
- 累计论文数量：173

## 📝 历史记录

> 暂无历史数据

