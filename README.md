# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-01 01:25:28

## 📅 2026-03-01 (今日最新)

**相关论文数：52**

### 1. [Zatom-1: A Multimodal Flow Foundation Model for 3D Molecules and Materials](https://arxiv.org/abs/2602.22251)

**基本信息**

- 🔗 arXiv: [`2602.22251`](https://arxiv.org/abs/2602.22251)
- 👥 作者: Alex Morehead, Miruna Cretu, Antonia Panescu 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22251.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于3D分子和材料的统一基础模型（Zatom-1），这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

本文介绍了Zatom-1，一个用于3D分子和材料的统一基础模型。该模型是一个Transformer，通过多模态流匹配目标进行训练，联合建模离散原子类型和连续3D几何结构。这种方法支持可扩展的预训练，并能够实现快速稳定的采样。Zatom-1将联合生成式预训练作为下游多任务预测（如性质、能量和力）的通用初始化。该模型在生成和预测基准测试中匹配或超越了专门的基线模型，同时将生成推理时间减少了一个数量级以上。实验表明，联合生成式预训练在化学领域之间实现了正向的预测迁移：在预训练中建模材料可以提高分子性质预测的准确性。这篇论文的核心是开发一个通用的3D化学模型，直接与化学信息学中的“化学大模型”主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose 3D chemical modeling encompasses molecules and materials, requiring both generative and predictive capabilities. However, most existing AI approaches are optimized for a single domain (molecules or materials) and a single task (generation or prediction), which limits representation sharing and transfer. We introduce Zatom-1, the first foundation model that unifies generative and predictive learning of 3D molecules and materials. Zatom-1 is a Transformer trained with a multimodal flow matching objective that jointly models discrete atom types and continuous 3D geometries. This approach supports scalable pretraining with predictable gains as model capacity increases, while enabling fast and stable sampling. We use joint generative pretraining as a universal initialization for downstream multi-task prediction of properties, energies, and forces. Empirically, Zatom-1 matches or outperforms specialized baselines on both generative and predictive benchmarks, while reducing the generative inference time by more than an order of magnitude. Our experiments demonstrate positive predictive transfer between chemical domains from joint generative pretraining: modeling materials during pretraining improves molecular property prediction accuracy.

</details>

---

### 2. [AR&D: A Framework for Retrieving and Describing Concepts for Interpreting AudioLLMs](https://arxiv.org/abs/2602.22253)

**基本信息**

- 🔗 arXiv: [`2602.22253`](https://arxiv.org/abs/2602.22253)
- 👥 作者: Townim Faisal Chowdhury, Ta Duc Huy, Siqi Pan 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22253.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于理解大型模型（AudioLLMs）内部表示的可解释性框架。虽然应用领域是音频，但其方法论（稀疏自编码器、特征解耦）与化学信息学和质谱分析中理解和构建“化学大模型”、进行“质谱结构推理”所依赖的表示学习和可解释性技术直接相关。

**📖 中文摘要**

尽管大型音频-语言模型在音频感知任务中表现出色，但其内部机制仍然不透明。缺乏可解释性的一个主要因素是模型中的单个神经元经常对多个不相关的概念产生响应。本文引入了第一个用于AudioLLMs的机制可解释性框架，利用稀疏自编码器将多义激活分解为单义特征。该流程通过自动标注识别代表性音频片段、分配有意义的名称，并通过人工评估和引导来验证概念。实验表明，AudioLLMs编码了结构化和可解释的特征，从而增强了透明度和可控性。这项工作为高风险领域的可信部署奠定了基础，并支持未来扩展到更大的模型、多语言音频和更细粒度的副语言特征。虽然论文主要关注音频模型，但其核心方法论——使用稀疏自编码器进行特征解耦和可解释性分析——是机器学习模型可解释性的通用技术。这种对模型内部表示进行解耦和分析的思路，与化学信息学中理解“化学大模型”内部工作机制、进行“质谱结构推理”等任务背后的表示学习原理高度相关，提供了方法论上的借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite strong performance in audio perception tasks, large audio-language models (AudioLLMs) remain opaque to interpretation. A major factor behind this lack of interpretability is that individual neurons in these models frequently activate in response to several unrelated concepts. We introduce the first mechanistic interpretability framework for AudioLLMs, leveraging sparse autoencoders (SAEs) to disentangle polysemantic activations into monosemantic features. Our pipeline identifies representative audio clips, assigns meaningful names via automated captioning, and validates concepts through human evaluation and steering. Experiments show that AudioLLMs encode structured and interpretable features, enhancing transparency and control. This work provides a foundation for trustworthy deployment in high-stakes domains and enables future extensions to larger models, multilingual audio, and more fine-grained paralinguistic features. Project URL: this https URL

</details>

---

### 3. [Multi-Level Causal Embeddings](https://arxiv.org/abs/2602.22287)

**基本信息**

- 🔗 arXiv: [`2602.22287`](https://arxiv.org/abs/2602.22287)
- 👥 作者: Willem Schooltink, Fabio Massimo Zennaro
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22287.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是因果表示学习和模型抽象的理论框架。这对于构建能够进行可靠科学推理（如“质谱结构推理”）的“化学大模型”具有重要的方法论和理论基础，因为因果理解是科学模型的核心。

**📖 中文摘要**

因果模型的抽象化允许对模型进行粗化，同时保留因果效应关系。虽然抽象化关注两个模型之间的关系，但本文研究了一个因果嵌入框架，该框架允许多个详细模型被映射到一个更粗粒度因果模型的子系统中。我们将因果嵌入定义为抽象化的泛化，并提出了一种广义的一致性概念。通过定义一个多分辨率边际问题，我们展示了因果嵌入对于统计边际问题和因果边际问题的相关性；此外，我们说明了其在合并来自不同表示模型的数据集方面的实际用途。这篇论文的核心是研究因果表示和模型抽象/嵌入的理论框架。虽然不直接应用化学或质谱，但其关于从数据中学习结构化、可解释的因果表示的理论，是构建能够进行可靠推理（如质谱结构推理）的“化学大模型”的重要理论基础。理解数据背后的因果结构对于提高模型在科学发现任务中的泛化性和可解释性至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Abstractions of causal models allow for the coarsening of models such that relations of cause and effect are preserved. Whereas abstractions focus on the relation between two models, in this paper we study a framework for causal embeddings which enable multiple detailed models to be mapped into sub-systems of a coarser causal model. We define causal embeddings as a generalization of abstraction, and present a generalized notion of consistency. By defining a multi-resolution marginal problem, we showcase the relevance of causal embeddings for both the statistical marginal problem and the causal marginal problem; furthermore, we illustrate its practical use in merging datasets coming from models with different representations.

</details>

---

### 4. [Disentangling Shared and Target-Enriched Topics via Background-Contrastive Non-negative Matrix Factorization](https://arxiv.org/abs/2602.22387)

**基本信息**

- 🔗 arXiv: [`2602.22387`](https://arxiv.org/abs/2602.22387)
- 👥 作者: Yixuan Li, Archer Y. Yang, Yue Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22387.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的数据分析和特征提取方法（背景对比非负矩阵分解），用于从高维数据中分离目标信号。这种方法与化学信息学和质谱分析中处理复杂数据集（如质谱数据）以进行“质谱结构推理”的核心数据分析任务直接相关。

**📖 中文摘要**

高维数据中感兴趣的生物信号常常被跨条件共享的主导变异所掩盖。这种变异源于基线生物结构或技术效应，会阻碍标准降维方法解析条件特异性结构。挑战在于这些混杂主题通常是未知的，并与生物信号混合在一起。现有的背景校正方法要么无法扩展到高维度，要么不可解释。我们引入了背景对比非负矩阵分解（BCNMF），它通过使用共享的非负基联合分解目标数据集和匹配的背景，并在抑制背景表达结构的对比目标下，提取目标富集的潜在主题。这种方法产生在特征级别可直接解释的非负成分，并明确隔离目标特异性变异。BCNMF通过高效的乘法更新算法学习，该算法通过矩阵乘法实现，使其在GPU硬件上高度高效，并且通过类似于深度学习方法的小批量训练可扩展到大数据。在模拟和多样化的生物数据集上，BCNMF揭示了传统方法所掩盖的信号，包括死后抑郁大脑单细胞RNA-seq中与疾病相关的程序、小鼠中与基因型相关的蛋白质表达模式、白血病中治疗特异性的转录变化以及癌症细胞系中TP53依赖的药物反应。这篇论文的核心是开发一种新的降维和特征提取方法，用于从高维生物数据中分离特定信号。该方法（非负矩阵分解的变体）是化学信息学（如分析质谱数据、分子描述符）和质谱分析（如从复杂谱图中提取化合物特征）中常用的数据分析技术的核心。论文提出的“背景对比”思想对于处理质谱数据中的基线噪声和背景干扰具有直接借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biological signals of interest in high-dimensional data are often masked by dominant variation shared across conditions. This variation, arising from baseline biological structure or technical effects, can prevent standard dimensionality reduction methods from resolving condition-specific structure. The challenge is that these confounding topics are often unknown and mixed with biological signals. Existing background correction methods are either unscalable to high dimensions or not interpretable. We introduce background contrastive Non-negative Matrix Factorization (\model), which extracts target-enriched latent topics by jointly factorizing a target dataset and a matched background using shared non-negative bases under a contrastive objective that suppresses background-expressed structure. This approach yields non-negative components that are directly interpretable at the feature level, and explicitly isolates target-specific variation. \model is learned by an efficient multiplicative update algorithm via matrix multiplication such that it is highly efficient on GPU hardware and scalable to big data via minibatch training akin to deep learning approach. Across simulations and diverse biological datasets, \model reveals signals obscured by conventional methods, including disease-associated programs in postmortem depressive brain single-cell RNA-seq, genotype-linked protein expression patterns in mice, treatment-specific transcriptional changes in leukemia, and TP53-dependent drug responses in cancer cell lines.

</details>

---

### 5. [A Reduced Order Model approach for First-Principles Molecular Dynamics Computations](https://arxiv.org/abs/2602.22390)

**基本信息**

- 🔗 arXiv: [`2602.22390`](https://arxiv.org/abs/2602.22390)
- 👥 作者: Siu Wun Cheung, Youngsoo Choi, Jean-Luc Fattebert 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22390.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发数据驱动的降阶模型来加速第一性原理分子动力学计算。这属于计算化学和化学信息学中构建高效“化学大模型”（基于物理的模型）的核心方法学，与利用机器学习加速量子化学计算的研究主题直接相关。

**📖 中文摘要**

为了利用第一性原理分子动力学每一步计算出的电子结构之间的冗余性，我们提出了一个用于Kohn-Sham密度泛函理论的数据驱动建模框架，该框架绕过了电子波函数的显式优化。我们预先采样具有代表性的原子构型，并构建一个低维基，该基能有效近似电子结构子空间。随后，我们在电子单粒子密度矩阵的直接求解器中采用这个约化基，从而能够在无需迭代波函数优化的情况下高效确定基态。我们在水分子的Born-Oppenheimer分子动力学中证明了我们方法的有效性，表明所得模拟准确再现了从完整第一性原理分子动力学获得的关键结构特性，如键长和键角。这项工作突出了数据驱动方法为第一性原理模拟开发高效电子结构求解器的潜力。这篇论文的核心是使用降阶模型（ROM）和数据驱动方法加速第一性原理计算。这属于计算化学领域的前沿方法学，是构建更高效、更快速的“化学大模型”（特别是基于物理原理的模型）的关键技术。虽然不直接涉及质谱，但其加速量子化学计算的方法对化学信息学至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To leverage the redundancy between the electronic structure computed at each step of first-principles molecular dynamics, we present a data-driven modeling framework for Kohn-Sham Density Functional Theory that bypasses the explicit optimization of electronic wavefunctions. We sample a priori representative atomic configurations and construct a low-dimensional basis that efficiently approximates the electronic structure subspace. Subsequently, we employ this reduced basis in a direct solver for the electronic single particle density matrix, thereby enabling the efficient determination of ground state without iterative wavefunction optimization. We demonstrate the efficacy of our approach in a Born-Oppenheimer molecular dynamics of a water molecule, showing that the resulting simulations accurately reproduce key structural properties, such as bond lengths and bond angle, obtained from full first-principles molecular dynamics. This work highlights the potential of data-driven approaches to develop efficient electronic structure solvers for first-principles simulations.

</details>

---

### 6. [MolFM-Lite: Multi-Modal Molecular Property Prediction with Conformer Ensemble Attention and Cross-Modal Fusion](https://arxiv.org/abs/2602.22405)

**基本信息**

- 🔗 arXiv: [`2602.22405`](https://arxiv.org/abs/2602.22405)
- 👥 作者: Syed Omer Shah, Mohammed Maqsood Ahmed, Danish Mohiuddin Mohammed 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22405.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个整合1D、2D、3D分子表示的多模态机器学习模型（MolFM-Lite），这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

本文提出了MolFM-Lite，一个用于分子性质预测的多模态模型。它联合编码SELFIES序列（1D）、分子图（2D）和构象体集合（3D），并通过跨模态注意力进行融合。该模型的核心贡献包括构象体集合注意力机制和跨模态融合层。虽然论文主要关注分子性质预测，但其核心方法——整合多模态分子表示（包括3D结构）并进行跨模态信息共享——与“化学大模型”的主题高度相关。MolFM-Lite代表了一种构建能够处理复杂、多维度化学信息的机器学习模型（即化学大模型）的努力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Most machine learning models for molecular property prediction rely on a single molecular representation (either a sequence, a graph, or a 3D structure) and treat molecular geometry as static. We present MolFM-Lite, a multi-modal model that jointly encodes SELFIES sequences (1D), molecular graphs (2D), and conformer ensembles (3D) through cross-attention fusion, while conditioning predictions on experimental context via Feature-wise Linear Modulation (FiLM). Our main methodological contributions are: (1) a conformer ensemble attention mechanism that combines learnable attention with Boltzmann-weighted priors over multiple RDKit-generated conformers, capturing the thermodynamic distribution of molecular shapes; and (2) a cross-modal fusion layer where each modality can attend to others, enabling complementary information sharing. We evaluate on four MoleculeNet scaffold-split benchmarks using our model's own splits, and report all baselines re-evaluated under the same protocol. Comprehensive ablation studies across all four datasets confirm that each architectural component contributes independently, with tri-modal fusion providing 7-11% AUC improvement over single-modality baselines and conformer ensembles adding approximately 2% over single-conformer variants. Pre-training on ZINC250K (~250K molecules) using cross-modal contrastive and masked-atom objectives enables effective weight initialization at modest compute cost. We release all code, trained models, and data splits to support reproducibility.

</details>

---

### 7. [Revisiting Chebyshev Polynomial and Anisotropic RBF Models for Tabular Regression](https://arxiv.org/abs/2602.22422)

**基本信息**

- 🔗 arXiv: [`2602.22422`](https://arxiv.org/abs/2602.22422)
- 👥 作者: Luciano Gerber, Huw Lloyd
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22422.pdf)

**💡 相关性分析**

满足标准2：论文开发并发布了用于表格回归的scikit-learn兼容模型包（如各向异性RBF网络、切比雪夫回归器），这些工具和代码资源可用于化学信息学领域的分子性质预测等任务，属于“化学大模型”构建的数据处理或基础模型组件。

**📖 中文摘要**

本文重新审视了切比雪夫多项式回归和各向异性径向基函数（RBF）网络在表格回归任务中的应用。作者开发了各向异性RBF网络、岭正则化切比雪夫多项式回归器以及平滑树混合模型（Chebyshev model tree），并将它们作为scikit-learn兼容的包发布。论文对这些平滑基模型与树集成、预训练Transformer等基线模型在55个回归数据集上进行了基准测试。虽然论文主题是通用的表格回归，但其核心贡献是发布了一系列新的、可复用的回归模型（工具），这些模型在化学信息学等领域（作为表格数据的一种）的定量构效关系（QSAR）建模等任务中具有潜在应用价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Smooth-basis models such as Chebyshev polynomial regressors and radial basis function (RBF) networks are well established in numerical analysis. Their continuously differentiable prediction surfaces suit surrogate optimisation, sensitivity analysis, and other settings where the response varies gradually with inputs. Despite these properties, smooth models seldom appear in tabular regression, where tree ensembles dominate. We ask whether they can compete, benchmarking models across 55 regression datasets organised by application domain. We develop an anisotropic RBF network with data-driven centre placement and gradient-based width optimisation, a ridge-regularised Chebyshev polynomial regressor, and a smooth-tree hybrid (Chebyshev model tree); all three are released as scikit-learn-compatible packages. We benchmark these against tree ensembles, a pre-trained transformer, and standard baselines, evaluating accuracy alongside generalisation behaviour. The transformer ranks first on accuracy across a majority of datasets, but its GPU dependence, inference latency, and dataset-size limits constrain deployment in the CPU-based settings common across applied science and industry. Among CPU-viable models, smooth models and tree ensembles are statistically tied on accuracy, but the former tend to exhibit tighter generalisation gaps. We recommend routinely including smooth-basis models in the candidate pool, particularly when downstream use benefits from tighter generalisation and gradually varying predictions.

</details>

---

### 8. [Predicting Known Vulnerabilities from Attack Descriptions Using Sentence Transformers](https://arxiv.org/abs/2602.22433)

**基本信息**

- 🔗 arXiv: [`2602.22433`](https://arxiv.org/abs/2602.22433)
- 👥 作者: Refat Othman
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22433.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发基于句子Transformer的语义相似性方法，用于从文本描述推理出对应的结构化实体（漏洞）。这种方法论与“质谱结构推理”中从质谱数据或描述推理出分子结构的任务在核心逻辑上直接相关，都是跨模态或跨表示的推理问题。

**📖 中文摘要**

本文提出了一种基于Transformer句子嵌入的方法，用于从网络攻击的自然语言描述中预测已知漏洞（CVE）。作者评估了14种最先进的Transformer模型在四种攻击描述类型上的性能，并实现了VULDAT工具，用于自动将攻击链接到漏洞。该方法的核心是利用语义向量表示进行基于相似性的排序和推荐。虽然论文主题是网络安全，但其核心技术——使用句子Transformer将文本描述编码为语义向量并进行相似性匹配——与“质谱结构推理”中可能用到的、将质谱特征或描述与已知化合物结构数据库进行匹配的思路在方法论上高度相似。这种文本/描述到结构化标识（漏洞ID/化合物结构）的映射框架具有借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern infrastructures rely on software systems that remain vulnerable to cyberattacks. These attacks frequently exploit vulnerabilities documented in repositories such as MITRE's Common Vulnerabilities and Exposures (CVE). However, Cyber Threat Intelligence resources, including MITRE ATT&CK and CVE, provide only partial coverage of attack-vulnerability relationships. Attack information often appears before vulnerabilities are formally linked, creating the need for automated methods that infer likely vulnerabilities directly from attack descriptions. This thesis addresses the problem of predicting known vulnerabilities from natural-language descriptions of cyberattacks. We develop transformer-based sentence embedding methods that encode attack and vulnerability descriptions into semantic vector representations, enabling similarity-based ranking and recommendation. Fourteen state-of-the-art transformer models were evaluated across four attack description types (Tactic, Technique, Procedure, and Attack Pattern). Results show that Technique descriptions in MITRE ATT&CK provide the strongest predictive signal. The multi-qa-mpnet-base-dot-v1 (MMPNet) model achieved the best performance due to its hybrid pre-training and optimization for semantic similarity. The approach was implemented in the VULDAT tool, which automatically links attacks to vulnerabilities. Manual validation revealed previously undocumented relationships in MITRE repositories. Evaluation on unseen cyberattack reports demonstrates that the models generalize beyond curated datasets and support proactive vulnerability awareness.

</details>

---

### 9. [MammoWise: Multi-Model Local RAG Pipeline for Mammography Report Generation](https://arxiv.org/abs/2602.22462)

**基本信息**

- 🔗 arXiv: [`2602.22462`](https://arxiv.org/abs/2602.22462)
- 👥 作者: Raiyan Jahangir, Nafiz Imtiaz Khan, Amritanand Sudheerkumar 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22462.pdf)

**💡 相关性分析**

满足标准2和间接满足标准1：论文提出了一个集成了VLM、RAG和微调技术的本地多模型流程框架（MammoWise），并发布了相关实现。这为构建用于科学数据（如质谱图像）分析的多模态AI系统提供了可参考的工具链和架构范例。其核心任务（从图像生成解释性报告/分类）也与“质谱结构推理”的目标（从谱图生成结构信息）在形式上类似。

**📖 中文摘要**

本文提出了MammoWise，一个用于乳腺X光检查报告生成和多项分类的本地多模型流程。它支持任何通过Ollama托管的视觉语言模型（VLM），并支持零样本、少样本和思维链提示，还可选择使用向量数据库进行多模态检索增强生成（RAG）。论文在VinDr-Mammo和DMID数据集上评估了MedGemma、LLaVA-Med和Qwen2.5-VL等模型，涉及报告质量、BI-RADS分类、乳腺密度和关键发现等任务。MammoWise提供了一个实用且可扩展的框架，用于在统一且可复现的工作流程中部署本地VLMs。虽然应用于医学影像，但其核心框架——整合多模态VLM、RAG和参数高效微调（QLoRA）以完成从图像到结构化报告/分类的生成任务——展示了构建领域专用多模态AI系统（可视为一种特定领域的“化学大模型”雏形）的完整技术栈，对构建用于质谱图像分析或光谱解释的类似系统具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Screening mammography is high volume, time sensitive, and documentation heavy. Radiologists must translate subtle visual findings into consistent BI-RADS assessments, breast density categories, and structured narrative reports. While recent Vision Language Models (VLMs) enable image-to-text reporting, many rely on closed cloud systems or tightly coupled architectures that limit privacy, reproducibility, and adaptability. We present MammoWise, a local multi-model pipeline that transforms open source VLMs into mammogram report generators and multi-task classifiers. MammoWise supports any Ollama-hosted VLM and mammography dataset, and enables zero-shot, few-shot, and Chain-of-Thought prompting, with optional multimodal Retrieval Augmented Generation (RAG) using a vector database for case-specific context. We evaluate MedGemma, LLaVA-Med, and Qwen2.5-VL on VinDr-Mammo and DMID datasets, assessing report quality (BERTScore, ROUGE-L), BI-RADS classification, breast density, and key findings. Report generation is consistently strong and improves with few-shot prompting and RAG. Classification is feasible but sensitive to model and dataset choice. Parameter-efficient fine-tuning (QLoRA) of MedGemma improves reliability, achieving BI-RADS accuracy of 0.7545, density accuracy of 0.8840, and calcification accuracy of 0.9341 while preserving report quality. MammoWise provides a practical and extensible framework for deploying local VLMs for mammography reporting within a unified and reproducible workflow.

</details>

---

### 10. [Mapping the Landscape of Artificial Intelligence in Life Cycle Assessment Using Large Language Models](https://arxiv.org/abs/2602.22500)

**基本信息**

- 🔗 arXiv: [`2602.22500`](https://arxiv.org/abs/2602.22500)
- 👥 作者: Anastasija Mensikova, Donna M. Rizzo, Kathryn Hinkelman
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22500.pdf)

**💡 相关性分析**

满足标准3：论文是一篇利用大语言模型进行辅助的综述性文章，系统性地回顾和展望了人工智能（包括机器学习和大语言模型）在生命周期评估（LCA）领域的整合、趋势和未来方向。这属于对AI在科学领域应用的综述，与广义的“化学大模型”（作为科学AI的一部分）的讨论相关。

**📖 中文摘要**

本文对人工智能（AI）在生命周期评估（LCA）中的整合研究进行了详细综述。作者利用大语言模型（LLMs）辅助文本挖掘方法，结合传统文献综述技术，识别了AI-LCA交叉领域的当前趋势、新兴主题和未来方向。分析表明，随着LCA研究的扩展，AI技术的采用急剧增长，并明显转向LLM驱动的方法。论文引入了一个动态有效的框架，能够捕捉该领域的高层研究趋势和细微的概念模式。这项工作展示了LLM辅助方法在支持大规模、可复现的跨领域文献综述方面的潜力。虽然主题是LCA，但论文本身是一篇关于AI在特定科学领域（LCA）应用的综述，并且重点介绍了LLM在该综述过程中的作用。这符合“综述展望相关”的标准，因为它系统地回顾了AI（包括机器学习和大语言模型）在一个重要的环境科学和工程领域的应用现状与未来。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integration of artificial intelligence (AI) into life cycle assessment (LCA) has accelerated in recent years, with numerous studies successfully adapting machine learning algorithms to support various stages of LCA. Despite this rapid development, comprehensive and broad synthesis of AI-LCA research remains limited. To address this gap, this study presents a detailed review of published work at the intersection of AI and LCA, leveraging large language models (LLMs) to identify current trends, emerging themes, and future directions. Our analyses reveal that as LCA research continues to expand, the adoption of AI technologies has grown dramatically, with a noticeable shift toward LLM-driven approaches, continued increases in ML applications, and statistically significant correlations between AI approaches and corresponding LCA stages. By integrating LLM-based text-mining methods with traditional literature review techniques, this study introduces a dynamic and effective framework capable of capturing both high-level research trends and nuanced conceptual patterns (themes) across the field. Collectively, these findings demonstrate the potential of LLM-assisted methodologies to support large-scale, reproducible reviews across broad research domains, while also evaluating pathways for computationally-efficient LCA in the context of rapidly developing AI technologies. In doing so, this work helps LCA practitioners incorporate state-of-the-art tools and timely insights into environmental assessments that can enhance the rigor and quality of sustainability-driven decisions and decision-making processes.

</details>

---

### 11. [LUMOS: Democratizing SciML Workflows with L0-Regularized Learning for Unified Feature and Parameter Adaptation](https://arxiv.org/abs/2602.22537)

**基本信息**

- 🔗 arXiv: [`2602.22537`](https://arxiv.org/abs/2602.22537)
- 👥 作者: Shouwei Gao, Xu Zheng, Dongsheng Luo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22537.pdf)

**💡 相关性分析**

满足标准2：论文提出了LUMOS框架，并进行了广泛的评估。该框架提供了用于科学机器学习模型自动化设计（特别是特征选择和模型剪枝）的工具和方法，这些工具可直接应用于构建更高效、更精简的“化学大模型”，属于重要的方法学资源。

**📖 中文摘要**

本文介绍了LUMOS，一个基于L0正则化学习的端到端框架，旨在通过统一特征选择和模型剪枝来 democratize 科学机器学习（SciML）模型的设计。LUMOS采用半随机门控和重参数化技术，在训练过程中动态选择信息特征并剪枝冗余参数，减少对手动调优的依赖，同时保持预测准确性。论文在包括宇宙学和分子科学在内的13个不同的SciML工作负载上评估了LUMOS，证明了其有效性和泛化能力。实验表明，LUMOS平均实现了71.45%的参数减少和6.4倍的推理加速。该框架直接针对SciML模型设计中的自动化挑战，其方法（特征选择、模型压缩）对于构建高效、可解释的“化学大模型”具有直接的工具价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of scientific machine learning (SciML) has accelerated discovery across diverse domains, yet designing effective SciML models remains a challenging task. In practice, building such models often requires substantial prior knowledge and manual expertise, particularly in determining which input features to use and how large the model should be. We introduce LUMOS, an end-to-end framework based on L0-regularized learning that unifies feature selection and model pruning to democratize SciML model design. By employing semi-stochastic gating and reparameterization techniques, LUMOS dynamically selects informative features and prunes redundant parameters during training, reducing the reliance on manual tuning while maintaining predictive accuracy. We evaluate LUMOS across 13 diverse SciML workloads, including cosmology and molecular sciences, and demonstrate its effectiveness and generalizability. Experiments on 13 SciML models show that LUMOS achieves 71.45% parameter reduction and a 6.4x inference speedup on average. Furthermore, Distributed Data Parallel (DDP) training on up to eight GPUs confirms the scalability of

</details>

---

### 12. [DisQ-HNet: A Disentangled Quantized Half-UNet for Interpretable Multimodal Image Synthesis Applications to Tau-PET Synthesis from T1 and FLAIR MRI](https://arxiv.org/abs/2602.22545)

**基本信息**

- 🔗 arXiv: [`2602.22545`](https://arxiv.org/abs/2602.22545)
- 👥 作者: Agamdeep S. Chopra, Caitlin Neher, Tianyi Ren 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22545.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新颖的多模态图像合成框架（DisQ-HNet），其关键技术（PID引导的潜在解耦、量化表示、可解释性分析）直接涉及多模态数据的信息融合与归因。这与“质谱结构推理”中整合多种光谱数据以推理分子结构，并理解不同数据源贡献的核心挑战高度相关。

**📖 中文摘要**

本文提出了DisQ-HNet（DQH），一个用于从配对的T1加权和FLAIR MRI合成tau-PET图像的框架，并揭示了每种模态对预测的贡献。该方法结合了（i）基于部分信息分解（PID）指导的、矢量量化的编码器，将潜在信息划分为冗余、独特和互补成分；（ii）Half-UNet解码器，使用以结构边缘线索为条件的伪跳跃连接来保留解剖细节。该框架在多个基线模型上保持了重建保真度，并更好地保留了用于下游阿尔茨海默病任务的相关信号。虽然应用于医学影像，但其核心创新——使用PID指导的量化编码器来解耦多模态信息贡献，并实现可解释的合成——为多模态数据融合和解释提供了先进的方法论。这种方法对于“质谱结构推理”中可能涉及的多谱图（如MS/MS, IR）融合以推断结构，以及增强模型的可解释性，具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tau positron emission tomography (tau-PET) provides an in vivo marker of Alzheimer's disease pathology, but cost and limited availability motivate MRI-based alternatives. We introduce DisQ-HNet (DQH), a framework that synthesizes tau-PET from paired T1-weighted and FLAIR MRI while exposing how each modality contributes to the prediction. The method combines (i) a Partial Information Decomposition (PID)-guided, vector-quantized encoder that partitions latent information into redundant, unique, and complementary components, and (ii) a Half-UNet decoder that preserves anatomical detail using pseudo-skip connections conditioned on structural edge cues rather than direct encoder feature reuse. Across multiple baselines (VAE, VQ-VAE, and UNet), DisQ-HNet maintains reconstruction fidelity and better preserves disease-relevant signal for downstream AD tasks, including Braak staging, tau localization, and classification. PID-based Shapley analysis provides modality-specific attribution of synthesized uptake patterns.

</details>

---

### 13. [Relatron: Automating Relational Machine Learning over Relational Databases](https://arxiv.org/abs/2602.22552)

**基本信息**

- 🔗 arXiv: [`2602.22552`](https://arxiv.org/abs/2602.22552)
- 👥 作者: Zhikai Chen, Han Xie, Jian Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22552.pdf)

**💡 相关性分析**

满足标准2：论文提出了Relatron框架，这是一个用于关系数据库上预测建模的自动化机器学习（AutoML）元选择器。该工具和方法可用于优化化学信息学中基于关系型分子数据库的机器学习模型（即化学大模型）的架构选择，属于重要的模型构建与优化资源。

**📖 中文摘要**

本文对关系数据库（RDB）上的预测建模进行了全面研究，将关系深度学习（RDL）和经典方法（如深度特征合成DFS）统一在一个共享的设计空间中，并在多样化的RDB任务上进行了以架构为中心的搜索。分析得出了三个关键发现，并基于此提出了Relatron，一个基于任务嵌入的元选择器，用于在RDL和DFS之间进行选择，并对族内搜索进行剪枝。论文通过实验验证了Relatron的有效性。虽然主要面向通用的关系型数据预测，但关系数据库是化学信息学中存储分子、反应、性质数据的核心形式。因此，该研究提供的自动化机器学习框架和见解（Relatron）对于在化学信息学领域构建和优化基于关系数据的“化学大模型”具有直接的工具和方法论意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predictive modeling over relational databases (RDBs) powers applications, yet remains challenging due to capturing both cross-table dependencies and complex feature interactions. Relational Deep Learning (RDL) methods automate feature engineering via message passing, while classical approaches like Deep Feature Synthesis (DFS) rely on predefined non-parametric aggregators. Despite performance gains, the comparative advantages of RDL over DFS and the design principles for selecting effective architectures remain poorly understood. We present a comprehensive study that unifies RDL and DFS in a shared design space and conducts architecture-centric searches across diverse RDB tasks. Our analysis yields three key findings: (1) RDL does not consistently outperform DFS, with performance being highly task-dependent; (2) no single architecture dominates across tasks, underscoring the need for task-aware model selection; and (3) validation accuracy is an unreliable guide for architecture choice. This search yields a model performance bank that links architecture configurations to their performance; leveraging this bank, we analyze the drivers of the RDL-DFS performance gap and introduce two task signals -- RDB task homophily and an affinity embedding that captures size, path, feature, and temporal structure -- whose correlation with the gap enables principled routing. Guided by these signals, we propose Relatron, a task embedding-based meta-selector that chooses between RDL and DFS and prunes the within-family search. Lightweight loss-landscape metrics further guard against brittle checkpoints by preferring flatter optima. In experiments, Relatron resolves the "more tuning, worse performance" effect and, in joint hyperparameter-architecture optimization, achieves up to 18.5% improvement over strong baselines with 10x lower cost than Fisher information-based alternatives.

</details>

---

### 14. [Autoregressive Visual Decoding from EEG Signals](https://arxiv.org/abs/2602.22555)

**基本信息**

- 🔗 arXiv: [`2602.22555`](https://arxiv.org/abs/2602.22555)
- 👥 作者: Sicheng Dai, Hongwang Xiao, Shan Yu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22555.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新颖的跨模态自回归生成框架（AVDE），用于从EEG信号解码视觉图像。这种方法论（使用一种模态的嵌入作为条件，自回归生成另一种模态的层次化令牌序列）与“质谱结构推理”中从质谱数据生成分子结构序列（如SMILES）的任务在问题定义和解决思路上高度相似，具有直接的相关性。

**📖 中文摘要**

本文提出了AVDE，一个从脑电图（EEG）信号进行视觉解码的轻量高效框架。首先，利用预训练的EEG模型（LaBraM）并通过对比学习进行微调，以对齐EEG和图像表示。其次，采用基于“下一尺度预测”策略的自回归生成框架：使用预训练的VQ-VAE将图像编码为多尺度令牌映射，并训练一个Transformer以EEG嵌入作为最粗表示，自回归地预测更细尺度的令牌。该设计在保持输入EEG信号与重建图像之间直接联系的同时，实现了连贯的生成。实验表明AVDE在图像检索和重建任务上优于先前的方法。虽然应用于神经科学，但其核心框架——将一种模态（EEG）的嵌入作为种子，通过自回归方式生成另一种模态（图像）的层次化表示——为跨模态生成任务提供了新颖的架构。这种方法对于“质谱结构推理”中从质谱数据自回归地生成分子结构表示（如SMILES或图令牌）具有直接的启发性和参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalogram (EEG) signals have become a popular medium for decoding visual information due to their cost-effectiveness and high temporal resolution. However, current approaches face significant challenges in bridging the modality gap between EEG and image data. These methods typically rely on complex adaptation processes involving multiple stages, making it hard to maintain consistency and manage compounding errors. Furthermore, the computational overhead imposed by large-scale diffusion models limit their practicality in real-world brain-computer interface (BCI) applications. In this work, we present AVDE, a lightweight and efficient framework for visual decoding from EEG signals. First, we leverage LaBraM, a pre-trained EEG model, and fine-tune it via contrastive learning to align EEG and image representations. Second, we adopt an autoregressive generative framework based on a "next-scale prediction" strategy: images are encoded into multi-scale token maps using a pre-trained VQ-VAE, and a transformer is trained to autoregressively predict finer-scale tokens starting from EEG embeddings as the coarsest representation. This design enables coherent generation while preserving a direct connection between the input EEG signals and the reconstructed images. Experiments on two datasets show that AVDE outperforms previous state-of-the-art methods in both image retrieval and reconstruction tasks, while using only 10% of the parameters. In addition, visualization of intermediate outputs shows that the generative process of AVDE reflects the hierarchical nature of human visual perception. These results highlight the potential of autoregressive models as efficient and interpretable tools for practical BCI applications.

</details>

---

### 15. [dLLM: Simple Diffusion Language Modeling](https://arxiv.org/abs/2602.22661)

**基本信息**

- 🔗 arXiv: [`2602.22661`](https://arxiv.org/abs/2602.22661)
- 👥 作者: Zhanhui Zhou, Lingjie Chen, Hanghang Tong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22661.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个统一的扩散语言建模框架（dLLM），该框架作为工具和资源，可用于构建和评估化学领域（如分子结构生成、性质预测）的专用大模型，与“化学大模型”主题高度相关。

**📖 中文摘要**

这篇论文提出了dLLM，一个用于扩散语言建模（DLM）的统一开源框架。DLM是生成模型的一种，与化学信息学中用于分子生成和性质预测的“化学大模型”在方法论上高度相关。该框架标准化了DLM的核心组件（训练、推理、评估），并提供了将任何BERT风格编码器或自回归语言模型转换为DLM的配方。这对于构建和评估专门用于化学领域（如分子生成、质谱解析）的扩散模型或大语言模型具有重要的工具和资源价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although diffusion language models (DLMs) are evolving quickly, many recent models converge on a set of shared components. These components, however, are distributed across ad-hoc research codebases or lack transparent implementations, making them difficult to reproduce or extend. As the field accelerates, there is a clear need for a unified framework that standardizes these common components while remaining flexible enough to support new methods and architectures. To address this gap, we introduce dLLM, an open-source framework that unifies the core components of diffusion language modeling -- training, inference, and evaluation -- and makes them easy to customize for new designs. With dLLM, users can reproduce, finetune, deploy, and evaluate open-source large DLMs such as LLaDA and Dream through a standardized pipeline. The framework also provides minimal, reproducible recipes for building small DLMs from scratch with accessible compute, including converting any BERT-style encoder or autoregressive LM into a DLM. We also release the checkpoints of these small DLMs to make DLMs more accessible and accelerate future research.

</details>

---

### 16. [Tokenization, Fusion and Decoupling: Bridging the Granularity Mismatch Between Large Language Models and Knowledge Graphs](https://arxiv.org/abs/2602.22698)

**基本信息**

- 🔗 arXiv: [`2602.22698`](https://arxiv.org/abs/2602.22698)
- 👥 作者: Siyue Su, Jian Yang, Bo Li 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22698.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决LLM与知识图谱的融合问题，其提出的统一表示、特征融合和推理方法可直接应用于化学信息学领域，用于构建能够处理分子结构图与文本信息的化学大模型，并支持从多模态数据（如质谱）中进行结构推理。

**📖 中文摘要**

本文提出了KGT框架，旨在解决大型语言模型（LLM）与知识图谱（KG）在粒度上的不匹配问题，以改进知识图谱补全（KGC）。虽然论文主要关注通用知识图谱，但其核心方法——使用专用实体令牌进行高效的全空间预测、融合预训练的结构和文本特征、以及解耦的语义与结构推理——为解决化学信息学中的关键问题提供了直接思路。例如，将分子结构（图）与文本描述（文献、属性）对齐，或从质谱数据中推理分子结构（质谱结构推理），都可以被视为一种特殊的“知识图谱补全”任务。论文提出的统一嵌入和关系引导门控机制等方法，对于构建能够同时理解化学结构（图）和文本描述（如质谱解析报告）的多模态化学大模型具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Leveraging Large Language Models (LLMs) for Knowledge Graph Completion (KGC) is promising but hindered by a fundamental granularity mismatch. LLMs operate on fragmented token sequences, whereas entities are the fundamental units in knowledge graphs (KGs) scenarios. Existing approaches typically constrain predictions to limited candidate sets or align entities with the LLM's vocabulary by pooling multiple tokens or decomposing entities into fixed-length token sequences, which fail to capture both the semantic meaning of the text and the structural integrity of the graph. To address this, we propose KGT, a novel framework that uses dedicated entity tokens to enable efficient, full-space prediction. Specifically, we first introduce specialized tokenization to construct feature representations at the level of dedicated entity tokens. We then fuse pre-trained structural and textual features into these unified embeddings via a relation-guided gating mechanism, avoiding training from scratch. Finally, we implement decoupled prediction by leveraging independent heads to separate and combine semantic and structural reasoning. Experimental results show that KGT consistently outperforms state-of-the-art methods across multiple benchmarks.

</details>

---

### 17. [BRepMAE: Self-Supervised Masked BRep Autoencoders for Machining Feature Recognition](https://arxiv.org/abs/2602.22701)

**基本信息**

- 🔗 arXiv: [`2602.22701`](https://arxiv.org/abs/2602.22701)
- 👥 作者: Can Yao, Kang Wu, Zuheng Zheng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22701.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心方法（基于图的掩码自编码预训练）与化学信息学中用于分子表示学习的图神经网络方法高度一致，为构建化学大模型提供了直接的方法论参考（标准1）。同时，其提出的框架本身可被视为一种处理结构化数据的工具或范式，可迁移至化学领域（标准2）。

**📖 中文摘要**

本文提出了BRepMAE，一个用于计算机辅助设计（CAD）模型中加工特征识别的掩码自监督学习框架。其核心是使用边界表示（BRep）衍生的几何属性邻接图（gAAG）作为输入，通过掩码图自编码器（MAE）进行预训练，学习CAD模型的有价值表示。虽然应用领域是机械制造，但其方法论与化学信息学高度相似：1）将复杂结构（CAD模型/分子）表示为图（gAAG/分子图）；2）使用自监督学习（掩码自动编码）从无标签数据中学习通用表示；3）下游任务是对结构中的功能单元进行识别（加工特征/官能团、子结构）。这种基于图的掩码自编码预训练范式，正是构建能够理解分子几何和拓扑结构的“化学大模型”的一种主流且有效的技术路径。论文为在化学领域应用类似技术提供了可借鉴的框架和验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a masked self-supervised learning framework, called BRepMAE, for automatically extracting a valuable representation of the input computer-aided design (CAD) model to recognize its machining features. Representation learning is conducted on a large-scale, unlabeled CAD model dataset using the geometric Attributed Adjacency Graph (gAAG) representation, derived from the boundary representation (BRep). The self-supervised network is a masked graph autoencoder (MAE) that focuses on reconstructing geometries and attributes of BRep facets, rather than graph structures. After pre-training, we fine-tune a network that contains both the encoder and a task-specific classification network for machining feature recognition (MFR). In the experiments, our fine-tuned network achieves high recognition rates with only a small amount of data (e.g., 0.1% of the training data), significantly enhancing its practicality in real-world (or private) scenarios where only limited data is available. Compared with other MFR methods, our fine-tuned network achieves a significant improvement in recognition rate with the same amount of training data, especially when the number of training samples is limited.

</details>

---

### 18. [Molecule Mixture Detection and Design for MC Systems with Non-linear, Cross-reactive Receiver Arrays](https://arxiv.org/abs/2602.22799)

**基本信息**

- 🔗 arXiv: [`2602.22799`](https://arxiv.org/abs/2602.22799)
- 👥 作者: Bastian Heinlein, Kaikai Zhu, Sümeyye Carkit-Yilmaz 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22799.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分子通信系统中的分子混合物检测与设计，这直接涉及化学信息学中通过传感器信号进行化学物质识别和推理的问题，与‘质谱结构推理’的主题在方法论上高度相关（都是通过分析信号来推断化学组成/结构）。

**📖 中文摘要**

本文研究空气分子通信（MC）系统，重点关注分子混合物检测与设计。系统使用非线性和交叉反应传感器作为接收器（RX），这与MC文献中常见的理想线性、分子类型特异性传感假设不同。论文提出了几种检测器和传输方案，包括用于无码间干扰（ISI）场景的近似最大似然（AML）符号检测器，以及一种考虑接收器特性的互补混合物字母表设计算法。对于存在显著ISI的高数据速率场景，AML检测器可以进行调整以利用统计ISI知识。此外，还提出了一种结合多个符号间隔信息的序列检测器。这项工作通过一个考虑发射器噪声、ISI以及通用非线性、交叉反应RX阵列的系统模型，为一大类MC系统实现可靠通信提供了方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Air-based molecular communication (MC) has the potential to be one of the first MC systems to be deployed in real-world applications, enabled by commercially available sensors. However, these sensors usually exhibit non-linear and cross-reactive behavior, contrary to the idealizing assumption of linear and perfectly molecule type-specific sensing often made in the MC literature. To address this mismatch, we propose several detectors and transmission schemes for a molecule mixture communication system where the receiver (RX) employs non-linear, cross-reactive sensors. All proposed schemes are based on the first- and second-order moments of the symbol likelihoods that are fed through the non-linear RX using the Unscented Transform. In particular, we propose an approximate maximum likelihood (AML) symbol-by-symbol detector for inter-symbol-interference (ISI)-free transmission scenarios and a complementary mixture alphabet design algorithm which accounts for the RX characteristics. When significant ISI is present at high data rates, the AML detector can be adapted to exploit statistical ISI knowledge. Additionally, we propose a sequence detector which combines information from multiple symbol intervals. For settings where sequence detection is not possible due to extremely limited computational power at the RX, we propose an adaptive transmission scheme which can be combined with symbol-by-symbol detection. Using computer simulations, we validate all proposed detectors and algorithms based on the responses of commercially available sensors as well as artificially generated sensor data incorporating the characteristics of metal-oxide semiconductor sensors. By employing a general system model that accounts for transmitter noise, ISI, and general non-linear, cross-reactive RX arrays, this work enables reliable communication for a large class of MC systems.

</details>

---

### 19. [FlexMS is a flexible framework for benchmarking deep learning-based mass spectrum prediction tools in metabolomics](https://arxiv.org/abs/2602.22822)

**基本信息**

- 🔗 arXiv: [`2602.22822`](https://arxiv.org/abs/2602.22822)
- 👥 作者: Yunhua Zhong, Yixuan Tang, Yifan Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22822.pdf)

**💡 相关性分析**

满足标准2和标准1：论文的核心是提供了一个用于评估质谱预测模型的基准框架FlexMS（标准1：核心主题围绕质谱分析）。更重要的是，它明确旨在提供用于质谱结构推理（即从结构预测谱图）的数据集、工具和评估基准（标准2：数据资源相关）。

**📖 中文摘要**

本文介绍了FlexMS，一个用于在代谢组学中基准测试深度学习质谱预测工具的灵活框架。质谱技术以质荷比峰的形式提供有价值的碎片化线索，对于化学分子的鉴定和性质预测至关重要。然而，实验谱图的缺乏阻碍了分子鉴定，因此迫切需要建立计算模型进行预测。深度学习模型在预测分子结构谱图方面前景广阔，但由于方法异质性和缺乏明确定义的基准，整体评估仍然具有挑战性。为了解决这个问题，作者创建了基准框架FlexMS，用于构建和评估质谱预测中的多样化模型架构。FlexMS支持动态构建众多不同的模型架构组合，并使用不同的指标在预处理的公共数据集上评估其性能。论文还提供了对影响性能因素的见解，包括数据集的结构多样性、学习率等超参数、数据稀疏性、预训练效果、元数据消融设置以及跨领域迁移学习分析。此外，检索基准模拟了实际的鉴定场景，根据预测的谱图对潜在匹配进行评分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The identification and property prediction of chemical molecules is of central importance in the advancement of drug discovery and material science, where the tandem mass spectrometry technology gives valuable fragmentation cues in the form of mass-to-charge ratio peaks. However, the lack of experimental spectra hinders the attachment of each molecular identification, and thus urges the establishment of prediction approaches for computational models. Deep learning models appear promising for predicting molecular structure spectra, but overall assessment remains challenging as a result of the heterogeneity in methods and the lack of well-defined benchmarks. To address this, our contribution is the creation of benchmark framework FlexMS for constructing and evaluating diverse model architectures in mass spectrum prediction. With its easy-to-use flexibility, FlexMS supports the dynamic construction of numerous distinct combinations of model architectures, while assessing their performance on preprocessed public datasets using different metrics. In this paper, we provide insights into factors influencing performance, including the structural diversity of datasets, hyperparameters like learning rate and data sparsity, pretraining effects, metadata ablation settings and cross-domain transfer learning analysis. This provides practical guidance in choosing suitable models. Moreover, retrieval benchmarks simulate practical identification scenarios and score potential matches based on predicted spectra.

</details>

---

### 20. [MEDNA-DFM: A Dual-View FiLM-MoE Model for Explainable DNA Methylation Prediction](https://arxiv.org/abs/2602.22850)

**基本信息**

- 🔗 arXiv: [`2602.22850`](https://arxiv.org/abs/2602.22850)
- 👥 作者: Yi He, Yina Cao, Jixiu Zhai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22850.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于DNA序列化学修饰（甲基化）预测的深度学习模型。这属于化学信息学中利用计算模型（可视为一种特定领域的化学大模型）预测分子或生物大分子化学属性的范畴，与‘化学大模型’主题相关。

**📖 中文摘要**

本文提出MEDNA-DFM，一种用于DNA甲基化预测的双视图FiLM-MoE模型，并辅以机制启发的信号纯化算法以实现可解释性。准确的DNA甲基化计算识别对于理解表观遗传调控至关重要。虽然深度学习在此二元分类任务中表现出色，但其“黑盒”性质阻碍了生物学洞察。作者的研究表明，MEDNA-DFM能有效捕捉保守的甲基化模式，在不同物种间实现稳健区分。在外部独立数据集上的验证证实，模型的泛化能力是由保守的内在基序（如GC含量）驱动的，而非系统发育上的接近性。此外，应用作者开发的算法提取的基序比先前研究具有显著更高的可靠性。最后，来自果蝇6mA案例研究的实证证据促使作者提出了一个“序列-结构协同”假说。这项工作为甲基化预测提供了一个强大工具，并展示了可解释深度学习如何推动方法创新和生物学假说的生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate computational identification of DNA methylation is essential for understanding epigenetic regulation. Although deep learning excels in this binary classification task, its "black-box" nature impedes biological insight. We address this by introducing a high-performance model MEDNA-DFM, alongside mechanism-inspired signal purification algorithms. Our investigation demonstrates that MEDNA-DFM effectively captures conserved methylation patterns, achieving robust distinction across diverse species. Validation on external independent datasets confirms that the model's generalization is driven by conserved intrinsic motifs (e.g., GC content) rather than phylogenetic proximity. Furthermore, applying our developed algorithms extracted motifs with significantly higher reliability than prior studies. Finally, empirical evidence from a Drosophila 6mA case study prompted us to propose a "sequence-structure synergy" hypothesis, suggesting that the GAGG core motif and an upstream A-tract element function cooperatively. We further validated this hypothesis via in silico mutagenesis, confirming that the ablation of either or both elements significantly degrades the model's recognition capabilities. This work provides a powerful tool for methylation prediction and demonstrates how explainable deep learning can drive both methodological innovation and the generation of biological hypotheses.

</details>

---

### 21. [MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis](https://arxiv.org/abs/2602.22955)

**基本信息**

- 🔗 arXiv: [`2602.22955`](https://arxiv.org/abs/2602.22955)
- 👥 作者: Feng Guo, Jiaxiang Liu, Yang Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22955.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是创建并发布了一个大规模、多模态的医学影像诊断数据集和基准（MM-NeuroOnco和MM-NeuroOnco-Bench）。虽然其应用领域是医学影像，但其构建多模态指令数据、进行模型评估的框架和方法，对于构建和评估更通用的化学信息学或质谱分析领域的多模态大模型（例如，结合分子结构图、质谱图和文本描述）具有重要的参考价值和资源意义。

**📖 中文摘要**

本文介绍了MM-NeuroOnco，一个用于基于MRI的脑肿瘤诊断的大规模多模态基准和指令微调数据集。准确的脑肿瘤诊断要求模型不仅能检测病变，还能生成基于影像学表现的临床可解释推理。然而，现有的公共数据集在注释丰富度和诊断语义方面仍然有限。为了弥补这一差距，MM-NeuroOnco包含来自20个数据源的24,726个MRI切片，配对了约200,000个涵盖不同肿瘤亚型和成像模式的语义丰富的多模态指令。为了缓解诊断语义注释的稀缺性和高成本，作者开发了一个多模型协作流程，用于自动完成医学信息并进行质量控制，从而生成超越仅掩码注释的诊断相关语义。基于此数据集，作者进一步构建了MM-NeuroOnco-Bench，这是一个带有拒绝感知设置的手动注释评估基准，以减少封闭式问题格式固有的偏见。在十个代表性模型上的评估表明，即使是最强的基线模型Gemini 3 Flash，在诊断相关问题上的准确率也仅为41.88%，突显了多模态脑肿瘤诊断理解的巨大挑战。利用MM-NeuroOnco，作者进一步提出了NeuroOnco-GPT，该模型在微调后诊断问题的准确率绝对提升了27%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate brain tumor diagnosis requires models to not only detect lesions but also generate clinically interpretable reasoning grounded in imaging manifestations, yet existing public datasets remain limited in annotation richness and diagnostic semantics. To bridge this gap, we introduce MM-NeuroOnco, a large-scale multimodal benchmark and instruction-tuning dataset for brain tumor MRI understanding, consisting of 24,726 MRI slices from 20 data sources paired with approximately 200,000 semantically enriched multimodal instructions spanning diverse tumor subtypes and imaging modalities. To mitigate the scarcity and high cost of diagnostic semantic annotations, we develop a multi-model collaborative pipeline for automated medical information completion and quality control, enabling the generation of diagnosis-related semantics beyond mask-only annotations. Building upon this dataset, we further construct MM-NeuroOnco-Bench, a manually annotated evaluation benchmark with a rejection-aware setting to reduce biases inherent in closed-ended question formats. Evaluation across ten representative models shows that even the strongest baseline, Gemini 3 Flash, achieves only 41.88% accuracy on diagnosis-related questions, highlighting the substantial challenges of multimodal brain tumor diagnostic understanding. Leveraging MM-NeuroOnco, we further propose NeuroOnco-GPT, which achieves a 27% absolute accuracy improvement on diagnostic questions following fine-tuning. This result demonstrates the effectiveness of our dataset and benchmark in advancing clinically grounded multimodal diagnostic reasoning. Code and dataset are publicly available at: this https URL

</details>

---

### 22. [SPM-Bench: Benchmarking Large Language Models for Scanning Probe Microscopy](https://arxiv.org/abs/2602.22971)

**基本信息**

- 🔗 arXiv: [`2602.22971`](https://arxiv.org/abs/2602.22971)
- 👥 作者: Peiyao Xiao, Xiaogang Li, Chengliang Xu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22971.pdf)

**💡 相关性分析**

满足标准2：论文提出的自动化数据合成管道和基准构建方法，为构建科学领域（如化学）的大模型提供了可借鉴的数据集创建工具和资源范式。

**📖 中文摘要**

本文提出了SPM-Bench，一个专门为扫描探针显微镜（SPM）设计的博士级多模态基准测试。论文的核心贡献在于一个全自动的数据合成流程，该流程利用Anchor-Gated Sieve（AGS）技术从arXiv和期刊论文中高效提取高质量的图像-文本对。虽然SPM本身是物理表征技术，但该论文提出的自动化数据合成范式、从科学文献中提取结构化数据的方法，以及构建领域特定基准测试的框架，为构建和评估科学领域（包括化学信息学和质谱分析）的“化学大模型”提供了重要的方法论参考和工具思路。它展示了如何自动化地创建高质量、低成本的科学数据集，这对于训练需要大量领域数据的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As LLMs achieved breakthroughs in general reasoning, their proficiency in specialized scientific domains reveals pronounced gaps in existing benchmarks due to data contamination, insufficient complexity, and prohibitive human labor costs. Here we present SPM-Bench, an original, PhD-level multimodal benchmark specifically designed for scanning probe microscopy (SPM). We propose a fully automated data synthesis pipeline that ensures both high authority and low-cost. By employing Anchor-Gated Sieve (AGS) technology, we efficiently extract high-value image-text pairs from arXiv and journal papers published between 2023 and 2025. Through a hybrid cloud-local architecture where VLMs return only spatial coordinates "llbox" for local high-fidelity cropping, our pipeline achieves extreme token savings while maintaining high dataset purity. To accurately and objectively evaluate the performance of the LLMs, we introduce the Strict Imperfection Penalty F1 (SIP-F1) score. This metric not only establishes a rigorous capability hierarchy but also, for the first time, quantifies model "personalities" (Conservative, Aggressive, Gambler, or Wise). By correlating these results with model-reported confidence and perceived difficulty, we expose the true reasoning boundaries of current AI in complex physical scenarios. These insights establish SPM-Bench as a generalizable paradigm for automated scientific data synthesis.

</details>

---

### 23. [RhythmBERT: A Self-Supervised Language Model Based on Latent Representations of ECG Waveforms for Heart Disease Detection](https://arxiv.org/abs/2602.23060)

**基本信息**

- 🔗 arXiv: [`2602.23060`](https://arxiv.org/abs/2602.23060)
- 👥 作者: Xin Wang, Burcu Ozek, Aruna Mohan 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23060.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（将结构化序列数据视为语言进行自监督建模）为“化学大模型”和“质谱结构推理”提供了直接的方法论启示。将质谱图类比为语言，并采用类似的token化和预训练策略，是构建质谱专用大模型、进行结构推理的一条可行技术路径。

**📖 中文摘要**

本文提出了RhythmBERT，一种基于心电图（ECG）波形潜在表示的自监督语言模型，用于心脏疾病检测。该模型将ECG视为一种语言范式，通过自编码器将P、QRS、T波等片段编码为符号化token，同时保留连续的形态学嵌入。RhythmBERT在约80万份未标记的ECG记录上进行掩码预测目标的预训练，以学习上下文表征。尽管该工作针对生物医学信号，但其核心思想——将复杂的、结构化的序列数据（如ECG波形）分解为离散的、有语义的token和连续的嵌入，并利用自监督语言模型进行学习——与“化学大模型”和“质谱结构推理”的研究主题高度相关。质谱图同样是一种复杂的结构化序列/图谱数据，可以借鉴类似的“谱图作为语言”的范式，将质谱峰、碎片离子等信息token化，并利用大模型进行预训练和下游推理（如结构解析）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electrocardiogram (ECG) analysis is crucial for diagnosing heart disease, but most self-supervised learning methods treat ECG as a generic time series, overlooking physiologic semantics and rhythm-level structure. Existing contrastive methods utilize augmentations that distort morphology, whereas generative approaches employ fixed-window segmentation, which misaligns cardiac cycles. To address these limitations, we propose RhythmBERT, a generative ECG language model that considers ECG as a language paradigm by encoding P, QRS, and T segments into symbolic tokens via autoencoder-based latent representations. These discrete tokens capture rhythm semantics, while complementary continuous embeddings retain fine-grained morphology, enabling a unified view of waveform structure and rhythm. RhythmBERT is pretrained on approximately 800,000 unlabeled ECG recordings with a masked prediction objective, allowing it to learn contextual representations in a label-efficient manner. Evaluations show that despite using only a single lead, RhythmBERT achieves comparable or superior performance to strong 12-lead baselines. This generalization extends from prevalent conditions such as atrial fibrillation to clinically challenging cases such as subtle ST-T abnormalities and myocardial infarction. Our results suggest that considering ECG as structured language offers a scalable and physiologically aligned pathway for advancing cardiac analysis.

</details>

---

### 24. [Assessing Deanonymization Risks with Stylometry-Assisted LLM Agent](https://arxiv.org/abs/2602.23079)

**基本信息**

- 🔗 arXiv: [`2602.23079`](https://arxiv.org/abs/2602.23079)
- 👥 作者: Boyang Zhang, Yang Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23079.pdf)

**💡 相关性分析**

满足标准1：论文提出的LLM智能体分析框架（结合领域特征与LLM推理）为构建用于“质谱结构推理”的智能体系统提供了可参考的架构和实现思路。

**📖 中文摘要**

本文研究了大型语言模型在文本作者推断方面的能力及其带来的去匿名化风险，并提出了一个名为SALA（Stylometry-Assisted LLM Analysis）的LLM智能体框架。该框架将定量的文体计量学特征与LLM推理相结合，用于鲁棒且可解释的作者归属分析。论文还提出了一种引导重写策略，利用智能体的推理轨迹生成改写提示，以降低作者的可识别性。这项工作虽然聚焦于文本作者分析，但其核心——利用LLM智能体进行细粒度的、基于特征的分析和生成——与利用AI进行科学数据分析（如质谱解析）在范式上相通。构建一个类似的“质谱解析智能体”，结合化学规则（类似文体特征）和LLM的推理能力，进行质谱图的结构推理，是一个值得探索的方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid advancement of large language models (LLMs) has enabled powerful authorship inference capabilities, raising growing concerns about unintended deanonymization risks in textual data such as news articles. In this work, we introduce an LLM agent designed to evaluate and mitigate such risks through a structured, interpretable pipeline. Central to our framework is the proposed $\textit{SALA}$ (Stylometry-Assisted LLM Analysis) method, which integrates quantitative stylometric features with LLM reasoning for robust and transparent authorship attribution. Experiments on large-scale news datasets demonstrate that $\textit{SALA}$, particularly when augmented with a database module, achieves high inference accuracy in various scenarios. Finally, we propose a guided recomposition strategy that leverages the agent's reasoning trace to generate rewriting prompts, effectively reducing authorship identifiability while preserving textual meaning. Our findings highlight both the deanonymization potential of LLM agents and the importance of interpretable, proactive defenses for safeguarding author privacy.

</details>

---

### 25. [Induction Meets Biology: Mechanisms of Repeat Detection in Protein Language Models](https://arxiv.org/abs/2602.23179)

**基本信息**

- 🔗 arXiv: [`2602.23179`](https://arxiv.org/abs/2602.23179)
- 👥 作者: Gal Kesten-Pomeranz, Yaniv Nikankin, Anja Reusch 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23179.pdf)

**💡 相关性分析**

满足标准1：论文对蛋白质语言模型内部机制（结合通用模式匹配与领域知识）的深入研究，为理解和设计用于“质谱结构推理”的“化学大模型”的内部架构和学习机制提供了重要的理论基础和灵感。

**📖 中文摘要**

本文深入研究了蛋白质语言模型（PLM）内部检测蛋白质序列中重复片段（包括精确重复和近似重复）的机制。研究发现，PLM通过结合通用的基于位置的注意力头和生物学特化的组件（如编码氨基酸相似性的神经元）来构建特征表示，然后通过归纳头（induction heads）关注重复片段间对齐的token，从而完成检测任务。这项工作揭示了PLM如何将基于语言的模式匹配与专门的生物学知识相结合来解决生物任务。这一机制研究对于理解“化学大模型”在化学和质谱领域的潜在工作方式具有重要参考价值。例如，一个用于质谱结构推理的化学大模型，很可能也需要类似的机制：既需要通用的序列/图谱模式识别能力，也需要内化化学知识（如官能团特性、裂解规则）的特化组件，才能有效推理出分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequences are abundant in repeating segments, both as exact copies and as approximate segments with mutations. These repeats are important for protein structure and function, motivating decades of algorithmic work on repeat identification. Recent work has shown that protein language models (PLMs) identify repeats, by examining their behavior in masked-token prediction. To elucidate their internal mechanisms, we investigate how PLMs detect both exact and approximate repeats. We find that the mechanism for approximate repeats functionally subsumes that of exact repeats. We then characterize this mechanism, revealing two main stages: PLMs first build feature representations using both general positional attention heads and biologically specialized components, such as neurons that encode amino-acid similarity. Then, induction heads attend to aligned tokens across repeated segments, promoting the correct answer. Our results reveal how PLMs solve this biological task by combining language-based pattern matching with specialized biological knowledge, thereby establishing a basis for studying more complex evolutionary processes in PLMs.

</details>

---

### 26. [ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203)

**基本信息**

- 🔗 arXiv: [`2602.23203`](https://arxiv.org/abs/2602.23203)
- 👥 作者: Junhu Fu, Shuyu Liang, Wutong Li 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23203.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一个旨在理解和改进化学生物学中机器学习模型因果推理能力的统一理论框架。

**📖 中文摘要**

这篇论文题为《Inferential Mechanics Part 1: Causal Mechanistic Theories of Machine Learning in Chemical Biology with Implications》。它提出了一种新颖的理论框架，旨在将化学理论、生物学理论、概率论和因果推理结合起来，以纠正当前机器学习在自然科学（特别是化学生物学）中存在的因果缺陷。论文的核心是探索化学大模型（Machine Learning in Chemical Biology）的因果结构，并引入了“焦点”（focus）这一新概念，即机器学习算法在大型数据集中聚焦于隐藏底层机制的能力。论文提供了在Akt抑制剂家族上的初步原理证明。该工作为化学生物学建立了一种新的数学框架，用于在不使用还原论工具的情况下对自然机制进行建模，即“推理力学”（inferential mechanics）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Colonoscopy video generation delivers dynamic, information-rich data critical for diagnosing intestinal diseases, particularly in data-scarce scenarios. High-quality video generation demands temporal consistency and precise control over clinical attributes, but faces challenges from irregular intestinal structures, diverse disease representations, and various imaging modalities. To this end, we propose ColoDiff, a diffusion-based framework that generates dynamic-consistent and content-aware colonoscopy videos, aiming to alleviate data shortage and assist clinical analysis. At the inter-frame level, our TimeStream module decouples temporal dependency from video sequences through a cross-frame tokenization mechanism, enabling intricate dynamic modeling despite irregular intestinal structures. At the intra-frame level, our Content-Aware module incorporates noise-injected embeddings and learnable prototypes to realize precise control over clinical attributes, breaking through the coarse guidance of diffusion models. Additionally, ColoDiff employs a non-Markovian sampling strategy that cuts steps by over 90% for real-time generation. ColoDiff is evaluated across three public datasets and one hospital database, based on both generation metrics and downstream tasks including disease diagnosis, modality discrimination, bowel preparation scoring, and lesion segmentation. Extensive experiments show ColoDiff generates videos with smooth transitions and rich dynamics. ColoDiff presents an effort in controllable colonoscopy video generation, revealing the potential of synthetic videos in complementing authentic representation and mitigating data scarcity in clinical settings.

</details>

---

### 27. [Strengthening security and noise resistance in one-way quantum key distribution protocols through hypercube-based quantum walks](https://arxiv.org/abs/2602.23261)

**基本信息**

- 🔗 arXiv: [`2602.23261`](https://arxiv.org/abs/2602.23261)
- 👥 作者: David Polzoni, Tommaso Bianchi, Mauro Conti
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23261.pdf)

**💡 相关性分析**

满足标准2：论文提出并发布了一个用于基于量子行走的QKD协议的开源模拟框架。该工具/资源可用于相关领域（如量子信息处理）的研究和开发，虽然不直接针对质谱结构推理，但作为“数据资源相关”的工具被纳入。

**📖 中文摘要**

这篇论文题为《Strengthening security and noise resistance in one-way quantum key distribution protocols through hypercube-based quantum walks》。它研究了一种基于离散时间量子行走（QWs）的单向量子密钥分发协议。论文的核心是引入了一种基于超立方体拓扑的新型QKD协议，并证明在相同参数下，该协议比基于环形拓扑（当前最先进）的协议提供了显著增强的安全性和抗噪性。论文还介绍了一个高效的、可扩展的模拟框架，用于分析基于QWs的QKD协议。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Key Distribution (QKD) is a foundational cryptographic protocol that ensures information-theoretic security. However, classical protocols such as BB84, though favored for their simplicity, offer limited resistance to eavesdropping, and perform poorly under realistic noise conditions. Recent research has explored the use of discrete-time Quantum Walks (QWs) to enhance QKD schemes. In this work, we specifically focus on a one-way QKD protocol, where security depends exclusively on the underlying Quantum Walk (QW) topology, rather than the details of the protocol itself. Our paper introduces a novel protocol based on QWs over a hypercube topology and demonstrates that, under identical parameters, it provides significantly enhanced security and noise resistance compared to the circular topology (i.e., state-of-the-art), thereby strengthening protection against eavesdropping. Furthermore, we introduce an efficient and extensible simulation framework for one-way QKD protocols based on QWs, supporting both circular and hypercube topologies. Implemented with IBM's software development kit for quantum computing (i.e., Qiskit), our toolkit enables noise-aware analysis under realistic noise models. To support reproducibility and future developments, we release our entire simulation framework as open-source. This contribution establishes a foundation for the design of topology-aware QKD protocols that combine enhanced noise tolerance with topologically driven security.

</details>

---

### 28. [Quantum Key Distribution](https://arxiv.org/abs/2507.23192)

**基本信息**

- 🔗 arXiv: [`2507.23192`](https://arxiv.org/abs/2507.23192)
- 👥 作者: Sebastian Kish, Josef Pieprzyk, Seyit Camtepe
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.23192.pdf)

**💡 相关性分析**

满足标准3：论文是一篇专门针对量子密钥分发（QKD）技术的综述，提供了该领域的成熟度、趋势、挑战和前景的全面概述。

**📖 中文摘要**

这篇论文题为《Quantum Key Distribution》。它是一篇关于量子密钥分发技术的综述章节。文章概述了QKD技术的成熟度和趋势，强调了单光子源和探测技术方面的重大进展，这些进展使QKD更接近广泛采用。文章还讨论了成本、集成、标准化以及量子中继器需求等挑战，并强调了QKD在保护关键通信免受未来量子威胁方面日益增长的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Key Distribution (QKD) is a technology that ensures secure communication by leveraging the principles of quantum mechanics, such as the no-cloning theorem and quantum uncertainty. This chapter provides an overview of this quantum technology's maturity and trends. It highlights significant advancements in single-photon sources and detection technologies that have brought QKD closer to widespread adoption, including real-world deployments by industry leaders. While addressing challenges such as cost, integration, standardization, and the need for quantum repeaters, the chapter emphasizes the growing importance of QKD in securing mission-critical communications against future quantum threats. Through its unique ability to achieve information-theoretic security, QKD is poised to play a vital role in quantum-safe cryptographic algorithms and protocols.

</details>

---

### 29. [CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction](https://arxiv.org/abs/2602.22236)

**基本信息**

- 🔗 arXiv: [`2602.22236`](https://arxiv.org/abs/2602.22236)
- 👥 作者: Rabeya Tus Sadia, Qiang Ye, Qiang Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22236.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用生物大语言模型（BioLLMs）进行多模态生物分子相互作用预测，直接涉及“化学大模型”在化学生物学领域的应用。

**📖 中文摘要**

这篇论文题为《CrossLLM-Mamba: Multimodal State Space Fusion of LLMs for RNA Interaction Prediction》。它提出了一种名为CrossLLM-Mamba的新颖框架，用于预测RNA相关的相互作用（如RNA-蛋白质、RNA-小分子、RNA-RNA）。该框架利用生物大语言模型（BioLLMs，如ESM-2和RiNALMo）提供强大的序列表示，并通过双向Mamba编码器实现模态特定嵌入之间的深度“串扰”。其核心是将相互作用预测重新表述为一个状态空间对齐问题，通过隐藏状态传播对相互作用进行动态建模。论文在多个基准测试中展示了最先进的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of RNA-associated interactions is essential for understanding cellular regulation and advancing drug discovery. While Biological Large Language Models (BioLLMs) such as ESM-2 and RiNALMo provide powerful sequence representations, existing methods rely on static fusion strategies that fail to capture the dynamic, context-dependent nature of molecular binding. We introduce CrossLLM-Mamba, a novel framework that reformulates interaction prediction as a state-space alignment problem. By leveraging bidirectional Mamba encoders, our approach enables deep ``crosstalk'' between modality-specific embeddings through hidden state propagation, modeling interactions as dynamic sequence transitions rather than static feature overlaps. The framework maintains linear computational complexity, making it scalable to high-dimensional BioLLM embeddings. We further incorporate Gaussian noise injection and Focal Loss to enhance robustness against hard-negative samples. Comprehensive experiments across three interaction categories, RNA-protein, RNA-small molecule, and RNA-RNA demonstrate that CrossLLM-Mamba achieves state-of-the-art performance. On the RPI1460 benchmark, our model attains an MCC of 0.892, surpassing the previous best by 5.2\%. For binding affinity prediction, we achieve Pearson correlations exceeding 0.95 on riboswitch and repeat RNA subtypes. These results establish state-space modeling as a powerful paradigm for multi-modal biological interaction prediction.

</details>

---

### 30. [VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction](https://arxiv.org/abs/2602.22239)

**基本信息**

- 🔗 arXiv: [`2602.22239`](https://arxiv.org/abs/2602.22239)
- 👥 作者: Ida Egendal, Rasmus Froberg Brøndum, Dan J Woodcock 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22239.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于变分自编码器的深度学习模型，用于从癌症基因组数据中提取突变特征。这属于“化学大模型”在计算生物学和化学信息学中的一个具体应用。

**📖 中文摘要**

这篇论文题为《VAE-MS: An Asymmetric Variational Autoencoder for Mutational Signature Extraction》。它提出了一种用于癌症突变特征提取的新型变分自编码器模型（VAE-MS）。突变特征分析是揭示癌症发展背后生物学过程的重要方法。VAE-MS结合了非对称架构和概率方法，旨在提高特征提取的可靠性和临床适用性。论文将VAE-MS与现有的金标准方法（如SigProfilerExtractor）以及其他先进模型（如MUSE-XAE, SigneR）进行了比较，展示了其在结合非线性提取与概率建模方面的优势。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mutational signature analysis has emerged as a powerful method for uncovering the underlying biological processes driving cancer development. However, the signature extraction process, typically performed using non-negative matrix factorization (NMF), often lacks reliability and clinical applicability. To address these limitations, several solutions have been introduced, including the use of neural networks to achieve more accurate estimates and probabilistic methods to better capture natural variation in the data. In this work, we introduce a Variational Autoencoder for Mutational Signatures (VAE-MS), a novel model that leverages both an asymmetric architecture and probabilistic methods for the extraction of mutational signatures. VAE-MS is compared to with three state-of-the-art models for mutational signature extraction: SigProfilerExtractor, the NMF-based gold standard; MUSE-XAE, an autoencoder that employs an asymmetric design without probabilistic components; and SigneR, a Bayesian NMF model, to illustrate the strength in combining a nonlinear extraction with a probabilistic model. In the ability to reconstruct input data and generalize to unseen data, models with probabilistic components (VAE-MS, SigneR) dramatically outperformed models without (SigProfilerExtractor, MUSE-XAE). The NMF-baed models (SigneR, SigProfilerExtractor) had the most accurate reconstructions in simulated data, while VAE-MS reconstructed more accurately on real cancer data. Upon evaluating the ability to extract signatures consistently, no model exhibited a clear advantage over the others. Software for VAE-MS is available at this https URL .

</details>

---

### 31. [Stochastic Neural Networks for Quantum Devices](https://arxiv.org/abs/2602.22241)

**基本信息**

- 🔗 arXiv: [`2602.22241`](https://arxiv.org/abs/2602.22241)
- 👥 作者: Bodo Rosenhahn, Tobias J. Osborne, Christoph Hirche
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22241.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将（随机）神经网络实现为量子电路，并探索其在量子设备上的应用。这直接涉及“化学大模型”在量子计算这一新兴交叉领域的形式和实现，与利用先进计算模型解决化学/科学问题相关。

**📖 中文摘要**

这篇论文题为《Stochastic Neural Networks for Quantum Devices》。它提出了一种在基于门的量子计算中，将随机神经网络表达和优化为量子电路的方案。论文受经典感知器启发，引入了随机神经元并将其组合成量子神经网络。使用Kiefer-Wolfowitz算法结合模拟退火来训练网络权重。展示了多种拓扑和模型，包括浅层全连接网络、Hopfield网络、受限玻尔兹曼机、自编码器和卷积神经网络。此外，还演示了将优化后的神经网络作为Grover算法的预言机，以实现量子生成式AI模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work presents a formulation to express and optimize stochastic neural networks as quantum circuits in gate-based quantum computing. Motivated by a classical perceptron, stochastic neurons are introduced and combined into a quantum neural network. The Kiefer-Wolfowitz algorithm in combination with simulated annealing is used for training the network weights. Several topologies and models are presented, including shallow fully connected networks, Hopfield Networks, Restricted Boltzmann Machines, Autoencoders and convolutional neural networks. We also demonstrate the combination of our optimized neural networks as an oracle for the Grover algorithm to realize a quantum generative AI model.

</details>

---

### 32. [Multi-Dimensional Spectral Geometry of Biological Knowledge in Single-Cell Transformer Representations](https://arxiv.org/abs/2602.22247)

**基本信息**

- 🔗 arXiv: [`2602.22247`](https://arxiv.org/abs/2602.22247)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22247.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和解释单细胞Transformer模型（scGPT）的内部表示和知识编码，直接围绕“化学大模型”（在生物学/化学交叉领域的应用）这一主题。

**📖 中文摘要**

这篇论文题为《Multi-Dimensional Spectral Geometry of Biological Knowledge in Single-Cell Transformer Representations》。它系统地解码了单细胞基础模型scGPT内部表示（即其学习到的高维基因表征）的几何结构。通过自动化假设筛选，研究发现scGPT将基因组织成一个结构化的生物坐标系，其中主导的光谱轴根据亚细胞定位分离基因，中间层编码线粒体和内质网等细胞器，正交轴编码蛋白质-蛋白质相互作用网络。该工作揭示了生物Transformer（如scGPT）学习了一个可解释的细胞组织内部模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell foundation models such as scGPT learn high-dimensional gene representations, but what biological knowledge these representations encode remains unclear. We systematically decode the geometric structure of scGPT internal representations through 63 iterations of automated hypothesis screening (183 hypotheses tested), revealing that the model organizes genes into a structured biological coordinate system rather than an opaque feature space. The dominant spectral axis separates genes by subcellular localization, with secreted proteins at one pole and cytosolic proteins at the other. Intermediate transformer layers transiently encode mitochondrial and ER compartments in a sequence that mirrors the cellular secretory pathway. Orthogonal axes encode protein-protein interaction networks with graded fidelity to experimentally measured interaction strength (Spearman rho = 1.000 across n = 5 STRING confidence quintiles, p = 0.017). In a compact six-dimensional spectral subspace, the model distinguishes transcription factors from their target genes (AUROC = 0.744, all 12 layers significant). Early layers preserve which specific genes regulate which targets, while deeper layers compress this into a coarser regulator versus regulated distinction. Repression edges are geometrically more prominent than activation edges, and B-cell master regulators BATF and BACH2 show convergence toward the B-cell identity anchor PAX5 across transformer depth. Cell-type marker genes cluster with high fidelity (AUROC = 0.851). Residual-stream geometry encodes biological structure complementary to attention patterns. These results indicate that biological transformers learn an interpretable internal model of cellular organization, with implications for regulatory network inference, drug target prioritization, and model auditing.

</details>

---

### 33. [Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486)

**基本信息**

- 🔗 arXiv: [`2602.22486`](https://arxiv.org/abs/2602.22486)
- 👥 作者: Shivam Kumar, Yixin Wang, Lizhen Lin
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22486.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕生成模型（如流匹配）在分子结构生成等领域的应用进行理论分析，这与‘化学大模型’主题中关于生成模型的理论基础高度相关。

**📖 中文摘要**

本文从理论角度分析了流匹配（Flow Matching）方法在目标分布位于低维流形上的情况。流匹配是一种免模拟的生成建模方法，通过学习源分布（如标准正态分布）与目标数据分布之间插值的时变速度场来生成样本。论文指出，尽管流匹配方法在文本到图像合成、视频生成和分子结构生成等高维数据集中表现出色，但现有理论分析假设目标分布具有平滑的全维密度，未能解释其在流形支撑数据上的有效性。为此，作者建立了当目标分布支撑在光滑流形上时，流匹配方法中学习到的速度场的非渐近收敛保证，并将此估计误差通过常微分方程传播，得到了由流匹配目标诱导的隐式密度估计器的统计一致性。最终证明其收敛速率接近极小极大最优，且仅依赖于内在维度，反映了流形和目标分布的平滑性。这些结果为流匹配如何适应内在数据几何结构并规避维度诅咒提供了原理性解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow matching has emerged as a simulation-free alternative to diffusion-based generative modeling, producing samples by solving an ODE whose time-dependent velocity field is learned along an interpolation between a simple source distribution (e.g., a standard normal) and a target data distribution. Flow-based methods often exhibit greater training stability and have achieved strong empirical performance in high-dimensional settings where data concentrate near a low-dimensional manifold, such as text-to-image synthesis, video generation, and molecular structure generation. Despite this success, existing theoretical analyses of flow matching assume target distributions with smooth, full-dimensional densities, leaving its effectiveness in manifold-supported settings largely unexplained. To this end, we theoretically analyze flow matching with linear interpolation when the target distribution is supported on a smooth manifold. We establish a non-asymptotic convergence guarantee for the learned velocity field, and then propagate this estimation error through the ODE to obtain statistical consistency of the implicit density estimator induced by the flow-matching objective. The resulting convergence rate is near minimax-optimal, depends only on the intrinsic dimension, and reflects the smoothness of both the manifold and the target distribution. Together, these results provide a principled explanation for how flow matching adapts to intrinsic data geometry and circumvents the curse of dimensionality.

</details>

---

### 34. [Discovery of Interpretable Physical Laws in Materials via Language-Model-Guided Symbolic Regression](https://arxiv.org/abs/2602.22967)

**基本信息**

- 🔗 arXiv: [`2602.22967`](https://arxiv.org/abs/2602.22967)
- 👥 作者: Yifeng Guan, Chuyi Liu, Dongzhan Zhou 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22967.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大型语言模型（LLM）引导符号回归以发现材料科学中物理定律的框架。这直接涉及‘化学大模型’主题中利用AI/LLM进行科学发现和建模的研究方向。

**📖 中文摘要**

本文提出了一种利用大型语言模型（LLM）引导符号回归（Symbolic Regression）来从高维数据中发现可解释物理定律的框架。该方法旨在解决传统符号回归在搜索巨大可能形式空间时产生复杂、非物理解析式的难题。通过利用大型语言模型中嵌入的科学知识来引导搜索过程，该方法能够高效地从数据中识别物理定律。作者以钙钛矿材料的关键性质建模为例验证了该方法。该方法缓解了传统符号回归中常见的组合爆炸问题，将有效搜索空间减少了约10^5倍。研究识别出了一组关于体模量、带隙和析氧反应活性的新公式，这些公式不仅提供了有意义的物理见解，而且在准确性和简洁性上超越了先前的公式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering interpretable physical laws from high-dimensional data is a fundamental challenge in scientific research. Traditional methods, such as symbolic regression, often produce complex, unphysical formulas when searching a vast space of possible forms. We introduce a framework that guides the search process by leveraging the embedded scientific knowledge of large language models, enabling efficient identification of physical laws in the data. We validate our approach by modeling key properties of perovskite materials. Our method mitigates the combinatorial explosion commonly encountered in traditional symbolic regression, reducing the effective search space by a factor of approximately $10^5$. A set of novel formulas for bulk modulus, band gap, and oxygen evolution reaction activity are identified, which not only provide meaningful physical insights but also outperform previous formulas in accuracy and simplicity.

</details>

---

### 35. [Not All Attention is Needed: Parameter and Computation Efficient Transfer Learning for Multi-modal Large Language Models](https://arxiv.org/abs/2403.15226)

**基本信息**

- 🔗 arXiv: [`2403.15226`](https://arxiv.org/abs/2403.15226)
- 👥 作者: Qiong Wu, Weihao Ye, Yiyi Zhou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2403.15226.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕多模态大语言模型（MLLMs）的高效调优方法。虽然应用领域是视觉语言，但其核心技术创新（注意力机制优化、参数高效调优）是构建和优化‘化学大模型’这类复杂AI模型时可能借鉴的关键技术。

**📖 中文摘要**

本文提出了一种用于多模态大语言模型（MLLMs）的新型参数和计算高效调优方法，称为高效注意力跳过（Efficient Attention Skipping, EAS）。该方法首先揭示了多头注意力（MHA）——MLLMs的主要计算开销——对于下游任务通常是冗余的。基于这一观察，EAS评估注意力冗余性并跳过较不重要的MHA以加速推理。此外，论文还提出了一种新颖的信息传播适配器（propagation-of-information adapter, PIA）来服务于EAS的注意力跳过并保持参数效率，该适配器可以进一步重新参数化到前馈网络（FFN）中，实现零额外延迟。作者将EAS应用于最近提出的MLLM模型LaVIN和一个经典的视觉语言预训练模型METER，并在多个基准测试上进行了广泛实验。实验表明，EAS不仅保持了高性能和参数效率，而且大大加快了推理速度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we propose a novel parameter and computation efficient tuning method for Multi-modal Large Language Models (MLLMs), termed Efficient Attention Skipping (EAS). Concretely, we first reveal that multi-head attentions (MHAs), the main computational overhead of MLLMs, are often redundant to downstream tasks. Based on this observation, EAS evaluates the attention redundancy and skips the less important MHAs to speed up inference. Besides, we also propose a novel propagation-of-information adapter (PIA) to serve the attention skipping of EAS and keep parameter efficiency, which can be further re-parameterized into feed-forward networks (FFNs) for zero-extra latency. To validate EAS, we apply it to a recently proposed MLLM called LaVIN and a classic VL pre-trained model called METER, and conduct extensive experiments on a set of benchmarks. The experiments show that EAS not only retains high performance and parameter efficiency, but also greatly speeds up inference speed. For instance, LaVIN-EAS can obtain 89.98\% accuracy on ScineceQA while speeding up inference by 2.2 times to LaVIN

</details>

---

### 36. [StableMaterials: Enhancing Diversity in Material Generation via Semi-Supervised Learning](https://arxiv.org/abs/2406.09293)

**基本信息**

- 🔗 arXiv: [`2406.09293`](https://arxiv.org/abs/2406.09293)
- 👥 作者: Giuseppe Vecchio
- 📄 PDF: [下载](https://arxiv.org/pdf/2406.09293.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于生成物理渲染（PBR）材料的生成模型（StableMaterials），该方法基于隐扩散模型（LDMs）。生成模型是‘化学大模型’的一个重要组成部分，特别是在材料发现和分子生成领域。虽然本文聚焦于图形学材料，但其底层生成模型技术具有通用性。

**📖 中文摘要**

本文介绍了StableMaterials，一种通过将半监督学习与隐扩散模型（LDMs）相结合来生成逼真物理渲染（PBR）材料的新方法。该方法采用对抗训练从现有的大规模图像生成模型中提取知识，最小化对标注数据的依赖，并增强生成的多样性。这种蒸馏方法将生成材料的分布与SDXL模型的图像纹理分布对齐，从而能够生成初始训练数据集中不存在的新材料。此外，作者采用了一个基于扩散的细化模型来提高样本的视觉质量并实现高分辨率生成。最后，作者蒸馏了一个潜在一致性模型用于仅需四步的快速生成，并提出了一种新的可平铺技术，以减少通常与较少扩散步骤相关的视觉伪影。论文详细介绍了StableMaterials的架构和训练过程，现有LDM框架内半监督训练的集成，并展示了该方法的优势。与最先进方法的比较评估显示了StableMaterials的有效性，突出了其在计算机图形学及其他领域的潜在应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce StableMaterials, a novel approach for generating photorealistic physical-based rendering (PBR) materials that integrate semi-supervised learning with Latent Diffusion Models (LDMs). Our method employs adversarial training to distill knowledge from existing large-scale image generation models, minimizing the reliance on annotated data and enhancing the diversity in generation. This distillation approach aligns the distribution of the generated materials with that of image textures from an SDXL model, enabling the generation of novel materials that are not present in the initial training dataset. Furthermore, we employ a diffusion-based refiner model to improve the visual quality of the samples and achieve high-resolution generation. Finally, we distill a latent consistency model for fast generation in just four steps and propose a new tileability technique that removes visual artifacts typically associated with fewer diffusion steps. We detail the architecture and training process of StableMaterials, the integration of semi-supervised training within existing LDM frameworks and show the advantages of our approach. Comparative evaluations with state-of-the-art methods show the effectiveness of StableMaterials, highlighting its potential applications in computer graphics and beyond. StableMaterials is publicly available at this https URL .

</details>

---

### 37. [Efficient Graph Coloring with Neural Networks: A Physics-Inspired Approach for Large Graphs](https://arxiv.org/abs/2408.01503)

**基本信息**

- 🔗 arXiv: [`2408.01503`](https://arxiv.org/abs/2408.01503)
- 👥 作者: Lorenzo Colantonio, Andrea Cacioppo, Federico Scarpati 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2408.01503.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于解决组合优化问题（如图着色）的神经求解器框架，该框架结合了图神经网络和物理原理。图神经网络是构建‘化学大模型’（用于分子表示、性质预测、反应推理）的核心架构之一。本文对GNN在复杂优化问题中的应用进行了深入探索，相关方法和技术可能迁移至化学信息学任务。

**📖 中文摘要**

本文介绍了一个受物理学启发的神经框架，该框架通过结合图神经网络和统计力学原理，学习解决大规模图着色实例。该方法整合了基于种植的监督信号、对称性破缺正则化和迭代噪声退火神经动力学，以导航聚集的解空间。当迭代次数与图大小成二次方比例时，学习到的求解器在随机图中达到接近理论动态转变的算法阈值，并在种植推断机制中实现接近最优的检测性能。该模型能够从小型训练图推广到规模大几个数量级的实例，表明神经架构可以学习到在组合优化和推断的基本相边界附近仍然有效的可扩展算法策略。这些结果为学习在组合优化和推断的基本相边界附近操作的神经求解器建立了一个通用范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Combinatorial optimization problems near algorithmic phase transitions represent a fundamental challenge for both classical algorithms and machine learning approaches. Among them, graph coloring stands as a prototypical constraint satisfaction problem exhibiting sharp dynamical and satisfiability thresholds. Here we introduce a physics-inspired neural framework that learns to solve large-scale graph coloring instances by combining graph neural networks with statistical-mechanics principles. Our approach integrates a planting-based supervised signal, symmetry-breaking regularization, and iterative noise-annealed neural dynamics to navigate clustered solution landscapes. When the number of iterations scales quadratically with graph size, the learned solver reaches algorithmic thresholds close to the theoretical dynamical transition in random graphs and achieves near-optimal detection performance in the planted inference regime. The model generalizes from small training graphs to instances orders of magnitude larger, demonstrating that neural architectures can learn scalable algorithmic strategies that remain effective in hard connectivity regions. These results establish a general paradigm for learning neural solvers that operate near fundamental phase boundaries in combinatorial optimization and inference.

</details>

---

### 38. [Open-Set Deepfake Detection: A Parameter-Efficient Adaptation Method with Forgery Style Mixture](https://arxiv.org/abs/2408.12791)

**基本信息**

- 🔗 arXiv: [`2408.12791`](https://arxiv.org/abs/2408.12791)
- 👥 作者: Chenqi Kong, Anwei Luo, Peijun Bao 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2408.12791.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于开放集检测任务的参数高效视觉Transformer模型。虽然应用领域是Deepfake检测，但其核心技术创新（参数高效调优、模型泛化）是构建和优化‘化学大模型’（如用于光谱分析或分子属性预测的视觉-语言模型）时可能面临和需要解决的共性问题。

**📖 中文摘要**

本文针对开放集人脸伪造检测的挑战，提出了一种通用且参数高效的方法。该方法基于一个假设：不同的伪造源域表现出不同的风格统计特征。先前的方法通常需要对预训练网络进行完全微调，消耗大量时间和计算资源。为此，作者设计了一种伪造风格混合公式，以增强伪造源域的多样性，从而提高模型对未见域的泛化能力。借鉴视觉Transformer（ViT）在人脸伪造检测中的最新进展，作者开发了一个参数高效的基于ViT的检测模型，该模型包含轻量级的伪造特征提取模块，并使模型能够同时提取全局和局部伪造线索。在训练期间，仅优化插入的轻量级模块，保持原始ViT结构及其预训练的ImageNet权重不变。这种训练策略有效地保留了信息丰富的预训练知识，同时灵活地将模型适应于Deepfake检测任务。大量实验结果表明，所设计的模型以显著减少的可训练参数实现了最先进的泛化能力，代表了向开放集Deepfake检测迈出的重要一步。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Open-set face forgery detection poses significant security threats and presents substantial challenges for existing detection models. These detectors primarily have two limitations: they cannot generalize across unknown forgery domains and inefficiently adapt to new data. To address these issues, we introduce an approach that is both general and parameter-efficient for face forgery detection. It builds on the assumption that different forgery source domains exhibit distinct style statistics. Previous methods typically require fully fine-tuning pre-trained networks, consuming substantial time and computational resources. In turn, we design a forgery-style mixture formulation that augments the diversity of forgery source domains, enhancing the model's generalizability across unseen domains. Drawing on recent advancements in vision transformers (ViT) for face forgery detection, we develop a parameter-efficient ViT-based detection model that includes lightweight forgery feature extraction modules and enables the model to extract global and local forgery clues simultaneously. We only optimize the inserted lightweight modules during training, maintaining the original ViT structure with its pre-trained ImageNet weights. This training strategy effectively preserves the informative pre-trained knowledge while flexibly adapting the model to the task of Deepfake detection. Extensive experimental results demonstrate that the designed model achieves state-of-the-art generalizability with significantly reduced trainable parameters, representing an important step toward open-set Deepfake detection in the wild.

</details>

---

### 39. [Beyond Attribution: Unified Concept-Level Explanations](https://arxiv.org/abs/2410.12439)

**基本信息**

- 🔗 arXiv: [`2410.12439`](https://arxiv.org/abs/2410.12439)
- 👥 作者: Junhao Liu, Haonan Yu, Xin Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.12439.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个为AI模型（包括多模态模型）提供基于概念的解释的通用框架（UnCLE）。模型可解释性是‘化学大模型’和‘质谱结构推理’模型在实际科学应用中取得信任和验证其预测的关键需求。本文提出的方法为复杂模型的解释提供了新思路。

**📖 中文摘要**

本文提出了一个通用框架UnCLE，旨在将现有的局部模型无关解释技术提升到提供基于概念的解释。现有的基于概念的模型无关解释方法范围有限，主要关注归因解释，而忽略了充分条件和反事实等多种形式，从而缩小了其实用性。为了弥补这一差距，UnCLE通过利用大型预训练模型扰动，统一扩展了现有的局部模型无关方法，以提供统一的基于概念的解释。作者将UnCLE实例化，以三种形式提供基于概念的解释：归因、充分条件和反事实，并将其应用于流行的文本、图像和多模态模型。评估结果表明，UnCLE提供的解释比最先进的基于概念的解释方法更忠实，并且提供了满足各种用户需求的更丰富的解释形式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

There is an increasing need to integrate model-agnostic explanation techniques with concept-based approaches, as the former can explain models across different architectures while the latter makes explanations more faithful and understandable to end-users. However, existing concept-based model-agnostic explanation methods are limited in scope, mainly focusing on attribution-based explanations while neglecting diverse forms like sufficient conditions and counterfactuals, thus narrowing their utility. To bridge this gap, we propose a general framework UnCLE to elevate existing local model-agnostic techniques to provide concept-based explanations. Our key insight is that we can uniformly extend existing local model-agnostic methods to provide unified concept-based explanations with large pre-trained model perturbation. We have instantiated UnCLE to provide concept-based explanations in three forms: attributions, sufficient conditions, and counterfactuals, and applied it to popular text, image, and multimodal models. Our evaluation results demonstrate that UnCLE provides explanations more faithful than state-of-the-art concept-based explanation methods, and provides richer explanation forms that satisfy various user needs.

</details>

---

### 40. [LLM4AD: A Platform for Algorithm Design with Large Language Model](https://arxiv.org/abs/2412.17287)

**基本信息**

- 🔗 arXiv: [`2412.17287`](https://arxiv.org/abs/2412.17287)
- 👥 作者: Fei Liu, Rui Zhang, Zhuoliang Xie 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.17287.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个统一的平台（LLM4AD），专门用于LLM辅助的算法设计。该平台提供了工具、接口和评估环境，可作为‘化学大模型’和‘质谱结构推理’领域研究人员开发和测试新算法（如用于分子优化、光谱解析的新方法）的潜在资源或工具。

**📖 中文摘要**

本文介绍了LLM4AD，一个用于大型语言模型（LLMs）辅助算法设计的统一Python平台。LLM4AD是一个通用框架，具有模块化块，用于搜索方法、算法设计任务和LLM接口。该平台集成了许多关键方法，并支持跨多个领域（包括优化、机器学习和科学发现）的各种算法设计任务。作者还设计了一个统一的评估沙盒，以确保对算法进行安全稳健的评估。此外，作者编制了一套全面的支持资源，包括教程、示例、用户手册、在线资源和专用的图形用户界面（GUI），以增强LLM4AD的使用体验。作者相信该平台将成为促进LLM辅助算法设计这一新兴研究方向未来发展的宝贵工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce LLM4AD, a unified Python platform for algorithm design (AD) with large language models (LLMs). LLM4AD is a generic framework with modularized blocks for search methods, algorithm design tasks, and LLM interface. The platform integrates numerous key methods and supports a wide range of algorithm design tasks across various domains including optimization, machine learning, and scientific discovery. We have also designed a unified evaluation sandbox to ensure a secure and robust assessment of algorithms. Additionally, we have compiled a comprehensive suite of support resources, including tutorials, examples, a user manual, online resources, and a dedicated graphical user interface (GUI) to enhance the usage of LLM4AD. We believe this platform will serve as a valuable tool for fostering future development in the merging research direction of LLM-assisted algorithm design.

</details>

---

### 41. [Neuro-Symbolic AI for Analytical Solutions of Differential Equations](https://arxiv.org/abs/2502.01476)

**基本信息**

- 🔗 arXiv: [`2502.01476`](https://arxiv.org/abs/2502.01476)
- 👥 作者: Orestis Oikonomou, Levi Lingsch, Dana Grund 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.01476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个神经符号框架（SIGS），用于自动发现微分方程的解析解。虽然不直接针对化学，但该方法论（结合符号推理与神经搜索）是推进‘化学大模型’科学发现能力（如从数据中发现物理定律、推导反应动力学方程）的前沿方向，具有高度的相关性。

**📖 中文摘要**

本文介绍了SIGS，一个用于自动发现微分方程解析解的神经符号框架。SIGS使用形式语法仅生成语法有效的构建块，将这些表达式嵌入连续空间，然后搜索该空间以通过最小化基于物理的残差来组装、评分和细化候选闭式解。该设计将符号推理与数值优化相统一；语法约束候选解块在构造上是正确的，而潜在搜索使探索易于处理且无需数据。SIGS是第一个能够（i）解析求解非线性偏微分方程耦合系统，（ii）在语法未指定情况下发现解，以及（iii）为缺乏已知闭式解的偏微分方程产生精确符号近似的神经符号方法。总体而言，SIGS在标准基准测试上比现有符号方法在准确性和效率上实现了数量级的改进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Analytical solutions to differential equations offer exact, interpretable insight but are rarely available because discovering them requires expert intuition or exhaustive search in combinatorial spaces. We introduce SIGS, a neuro-symbolic framework that automates this process. SIGS uses a formal grammar to generate only syntactically valid building blocks, embeds these expressions into a continuous space, and then searches this space to assemble, score, and refine candidate closed-form solutions by minimizing a physics-based residual. This design unifies symbolic reasoning with numerical optimization; the grammar constrains candidate solution blocks to be proper by construction, while the latent search makes exploration tractable and data-free. SIGS is the first neuro-symbolic method to (i) analytically solve coupled systems of nonlinear PDEs, (ii) discover solutions under grammar misspecification, and (iii) produce accurate symbolic approximations for PDEs lacking known closed-form solutions. Overall, SIGS achieves orders-of-magnitude improvements in accuracy and efficiency over existing symbolic methods on standard benchmarks.

</details>

---

### 42. [CLIP-Free, Label Free, Unsupervised Concept Bottleneck Models](https://arxiv.org/abs/2503.10981)

**基本信息**

- 🔗 arXiv: [`2503.10981`](https://arxiv.org/abs/2503.10981)
- 👥 作者: Fawaz Sammani, Jonas Fischer, Nikos Deligiannis
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.10981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发无需CLIP和人工标注的概念瓶颈模型（CBM）构建方法。概念瓶颈模型是一种可解释的AI模型，其思想可以迁移到‘化学大模型’和‘质谱结构推理’中，用于构建具有人类可理解中间概念（如官能团、碎片离子）的预测模型，从而增强模型的可信度和可解释性。

**📖 中文摘要**

本文提出了一种方法，可以将任何冻结的视觉分类器转换为概念瓶颈模型（CBM），而无需图像-概念标签（无标签）、不依赖CLIP模型（无CLIP），并以无监督方式推导线性分类器。该方法通过将原始分类器的分布（在离散类别索引上）与其从文本类别名称派生的相应视觉-语言对应分布对齐，同时保留分类器的性能。该方法不需要真实图像-类别标注，具有高度数据效率，并保留了分类器的推理过程。在超过40个视觉分类器上应用和测试，所得出的无监督、无标签和无CLIP的CBM（U-F^2-CBM）设立了新的最先进水平，甚至超过了有监督的基于CLIP的CBM。作者还表明，该方法可用于零样本图像描述，优于基于CLIP的现有方法，并达到最先进水平。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) map dense feature representations into human-interpretable concepts which are then combined linearly to make a prediction. However, modern CBMs rely on the CLIP model to obtain image-concept annotations, and it remains unclear how to design CBMs without the CLIP bottleneck. Methods that do not use CLIP instead require manual, labor intensive annotation to associate feature representations with concepts. Furthermore, all CBMs necessitate training a linear classifier to map the extracted concepts to class labels. In this work, we lift all three limitations simultaneously by proposing a method that converts any frozen visual classifier into a CBM without requiring image-concept labels (label-free), without relying on the CLIP model (CLIP-free), and by deriving the linear classifier in an unsupervised manner. Our method is formulated by aligning the original classifier's distribution (over discrete class indices) with its corresponding vision-language counterpart distribution derived from textual class names, while preserving the classifier's performance. The approach requires no ground-truth image-class annotations, and is highly data-efficient and preserves the classifier's reasoning process. Applied and tested on over 40 visual classifiers, our resulting unsupervised, label-free and CLIP-free CBM (U-F$^2$-CBM) sets a new state of the art, surpassing even supervised CLIP-based CBMs. We also show that our method can be used for zero-shot image captioning, outperforming existing methods based on CLIP, and achieving state-of-art.

</details>

---

### 43. [Compositional-ARC: Assessing Systematic Generalization in Abstract Spatial Reasoning](https://arxiv.org/abs/2504.01445)

**基本信息**

- 🔗 arXiv: [`2504.01445`](https://arxiv.org/abs/2504.01445)
- 👥 作者: Philipp Mondorf, Shijia Zhou, Monica Riedler 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.01445.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升AI模型（特别是Transformer架构）的系统性组合泛化能力。这种能力对于‘化学大模型’至关重要，例如需要模型理解已知化学反应或分子片段的新组合，或从有限的质谱碎片模式推理出新的分子结构。本文的研究范式（元学习、组合性评估）对该主题有直接借鉴意义。

**📖 中文摘要**

本文引入了Compositional-ARC数据集，旨在评估模型从已知几何变换（如平移、旋转）系统泛化到这些变换的新组合（如平移+旋转）的能力。研究结果表明，一个基于Transformer的小型编码器-解码器模型，通过为组合性设计的元学习进行训练，可以系统性地泛化到先前未见过的变换组合。值得注意的是，尽管该模型只有570万个参数，但其性能显著优于最先进的大型语言模型（包括o3-mini、GPT-4o和Gemini 2.0 Flash，这些模型未能表现出类似的系统行为），并与ARC prize 2024的获胜模型（一个通过测试时训练的80亿参数LLM）表现相当。研究结果强调了元学习在促进语言任务之外的系统性方面的有效性，为开发更稳健和可泛化的模型指明了有希望的方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Systematic generalization refers to the capacity to understand and generate novel combinations from known components. Despite recent progress by large language models (LLMs) across various domains, these models often fail to extend their knowledge to novel compositional scenarios, revealing notable limitations in systematic generalization. There has been an ongoing debate about whether neural networks possess the capacity for systematic generalization, with recent studies suggesting that meta-learning approaches designed for compositionality can significantly enhance this ability. However, these insights have largely been confined to linguistic problems, leaving their applicability to other tasks an open question. In this study, we extend meta-learning for compositionality to the domain of abstract spatial reasoning. To this end, we introduce $\textit{Compositional-ARC}\unicode{x2014}$a dataset designed to evaluate the capacity of models to systematically generalize from known geometric transformations (e.g., translation, rotation) of abstract two-dimensional objects to novel combinations of these transformations (e.g., translation+rotation). Our results show that a small transformer-based encoder-decoder model, trained via meta-learning for compositionality, can systematically generalize to previously unseen transformation compositions. Notably, despite having only 5.7M parameters, this model significantly outperforms state-of-the-art LLMs$\unicode{x2014}$including o3-mini, GPT-4o, and Gemini 2.0 Flash, which fail to exhibit similar systematic behavior$\unicode{x2014}$and performs on par with the winning model of the ARC prize 2024, an 8B-parameter LLM trained via test-time training. Our findings highlight the effectiveness of meta-learning in promoting systematicity beyond linguistic tasks, suggesting a promising direction toward more robust and generalizable models.

</details>

---

### 44. [The Spacetime of Diffusion Models: An Information Geometry Perspective](https://arxiv.org/abs/2505.17517)

**基本信息**

- 🔗 arXiv: [`2505.17517`](https://arxiv.org/abs/2505.17517)
- 👥 作者: Rafał Karczewski, Markus Heinonen, Alison Pouplin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.17517.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学中的一个关键主题——分子系统的表示与生成模型（扩散模型）。论文提出的几何框架和编辑距离直接与分子结构的推理、编辑和采样相关，这是质谱结构推理和化学大模型（用于分子生成与表示）的核心问题。

**📖 中文摘要**

本文从信息几何的角度提出了扩散模型潜在空间的一种新颖几何视角。作者指出，标准的基于确定性概率流ODE解码器的回拉方法存在根本性缺陷，因为它迫使测地线在数据空间中解码为直线段，从而忽略了数据的内在几何结构。作为补充，扩散模型也允许通过反向SDE进行随机解码，这使得可以使用Fisher-Rao度量进行信息几何处理。然而，选择x_T作为潜在表示会由于无记忆性导致该度量坍缩。为了解决这个问题，作者引入了一个潜在时空z=(x_t, t)，该时空索引了所有噪声尺度下的去噪分布族p(x_0 | x_t)，从而产生了一个非平凡的几何结构。作者证明了这些分布形成了一个指数族，并推导了曲线长度的无模拟估计器，从而实现了高效的测地线计算。由此产生的结构引入了一种原则性的扩散编辑距离，其中测地线追踪数据之间噪声和去噪编辑的最小序列。这项工作还展示了该方法在分子系统（包括约束变体，如低方差跃迁和区域规避）中过渡路径采样的好处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a novel geometric perspective on the latent space of diffusion models. We first show that the standard pullback approach, utilizing the deterministic probability flow ODE decoder, is fundamentally flawed. It provably forces geodesics to decode as straight segments in data space, effectively ignoring any intrinsic data geometry beyond the ambient Euclidean space. Complementing this view, diffusion also admits a stochastic decoder via the reverse SDE, which enables an information geometric treatment with the Fisher-Rao metric. However, a choice of $x_T$ as the latent representation collapses this metric due to memorylessness. We address this by introducing a latent spacetime $z=(x_t,t)$ that indexes the family of denoising distributions $p(x_0 | x_t)$ across all noise scales, yielding a nontrivial geometric structure. We prove these distributions form an exponential family and derive simulation-free estimators for curve lengths, enabling efficient geodesic computation. The resulting structure induces a principled Diffusion Edit Distance, where geodesics trace minimal sequences of noise and denoise edits between data. We also demonstrate benefits for transition path sampling in molecular systems, including constrained variants such as low-variance transitions and region avoidance. Code is available at: this https URL .

</details>

---

### 45. [Random Matrix Theory-guided sparse PCA for single-cell RNA-seq data](https://arxiv.org/abs/2509.15429)

**基本信息**

- 🔗 arXiv: [`2509.15429`](https://arxiv.org/abs/2509.15429)
- 👥 作者: Victor Chardès
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.15429.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的数据处理和分析方法（基于RMT的稀疏PCA），并应用于单细胞RNA-seq数据。虽然主题更偏向生物信息学，但其核心是开发用于高维、噪声生物分子数据（转录组）的分析工具和算法。这种数据处理和特征提取方法在化学信息学中具有直接的类比和应用潜力，例如用于处理质谱数据或构建化学数据的表示，因此提供了可用于相关主题的数据分析资源和方法论。

**📖 中文摘要**

本文提出了一种基于随机矩阵理论（RMT）的稀疏主成分分析（PCA）方法，用于处理单细胞RNA测序（scRNA-seq）数据。单细胞RNA-seq数据噪声高，变异性来源于生物学差异和技术因素（如扩增偏差和有限的RNA捕获效率），这使得将计算流程适应异构数据集或不断发展的技术具有挑战性。大多数研究仍然依赖主成分分析（PCA）进行降维，尽管已知其在维数较高时存在偏差。本文改进了PCA，提出了一种基于随机矩阵理论（RMT）的方法，该方法利用现有的稀疏PCA算法来指导稀疏主成分的推断。作者首先引入了一种新颖的双白化算法，该算法能够自一致地估计每个基因在每个细胞中受转录组噪声影响的大小，而无需假设特定的噪声分布。这使得能够使用基于RMT的标准自动选择稀疏度水平，从而使稀疏PCA几乎无需参数。这种基于数学的方法保留了PCA的可解释性，同时能够稳健、无需人工干预地推断稀疏主成分。在七种单细胞RNA-seq技术和四种稀疏PCA算法上的实验表明，该方法系统地改善了主成分子空间的重建，并在细胞类型分类任务中持续优于基于PCA、自编码器和扩散的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Single-cell RNA-seq provides detailed molecular snapshots of individual cells but is notoriously noisy. Variability stems from biological differences and technical factors, such as amplification bias and limited RNA capture efficiency, making it challenging to adapt computational pipelines to heterogeneous datasets or evolving technologies. As a result, most studies still rely on principal component analysis (PCA) for dimensionality reduction, valued for its interpretability and robustness, in spite of its known bias in high dimensions. Here, we improve upon PCA with a Random Matrix Theory (RMT)-based approach that guides the inference of sparse principal components using existing sparse PCA algorithms. We first introduce a novel biwhitening algorithm which self-consistently estimates the magnitude of transcriptomic noise affecting each gene in individual cells, without assuming a specific noise distribution. This enables the use of an RMT-based criterion to automatically select the sparsity level, rendering sparse PCA nearly parameter-free. Our mathematically grounded approach retains the interpretability of PCA while enabling robust, hands-off inference of sparse principal components. Across seven single-cell RNA-seq technologies and four sparse PCA algorithms, we show that this method systematically improves the reconstruction of the principal subspace and consistently outperforms PCA-, autoencoder-, and diffusion-based methods in cell-type classification tasks.

</details>

---

### 46. [G-reasoner: Foundation Models for Unified Reasoning over Graph-structured Knowledge](https://arxiv.org/abs/2509.24276)

**基本信息**

- 🔗 arXiv: [`2509.24276`](https://arxiv.org/abs/2509.24276)
- 👥 作者: Linhao Luo, Zicheng Zhao, Junnan Liu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24276.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于在结构化知识（如图）上进行推理的统一基础模型框架。这直接与“化学大模型”主题相关，因为化学领域知识（如分子结构、反应路径、性质关系）天然适合用图来表示。G-reasoner框架为构建能够理解和推理化学图结构（如分子图）的大模型提供了方法论和架构上的参考，是化学信息学中构建具有深度推理能力的大模型的重要相关研究。

**📖 中文摘要**

本文提出了G-reasoner，一个将图与语言基础模型相集成的统一框架，用于对多样化图结构知识进行可扩展推理。大语言模型（LLMs）擅长复杂推理，但受限于静态和不完整的参数化知识。检索增强生成（RAG）通过整合外部知识来缓解这一问题，但现有的RAG由于信息碎片化和知识结构建模薄弱，在知识密集型任务中仍然存在困难。图提供了一种对知识内部关系进行建模的自然方式，但LLMs本质上是非结构化的，无法有效地对图结构数据进行推理。最近的图增强RAG（GraphRAG）试图通过构建定制化的图并让LLMs在其上进行推理来弥合这一差距。然而，这些方法通常依赖于临时性的图设计、启发式搜索或成本高昂的智能体流程，这阻碍了可扩展性和泛化能力。为了解决这些挑战，本文提出了G-reasoner。其核心是QuadGraph，一个标准化的四层抽象，将异构知识源统一为通用的图表示。在此基础上，作者引入了一个3400万参数的图基础模型（GFM），该模型联合捕获图拓扑和文本语义，并与LLMs集成以增强下游应用中的推理能力。在六个基准测试上的广泛实验表明，G-reasoner持续优于最先进的基线方法，显著增强了LLM的推理能力，并实现了强大的效率和跨图泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) excel at complex reasoning but remain limited by static and incomplete parametric knowledge. Retrieval-augmented generation (RAG) mitigates this by incorporating external knowledge, yet existing RAGs struggle with knowledge-intensive tasks due to fragmented information and weak modeling of knowledge structure. Graphs offer a natural way to model relationships within knowledge, but LLMs are inherently unstructured and cannot effectively reason over graph-structured data. Recent graph-enhanced RAG (GraphRAG) attempts to bridge this gap by constructing tailored graphs and enabling LLMs to reason on them. However, these methods often depend on ad-hoc graph designs, heuristic search, or costly agent pipelines, which hinder scalability and generalization. To address these challenges, we present G-reasoner, a unified framework that integrates graph and language foundation models for scalable reasoning over diverse graph-structured knowledge. Central to our approach is QuadGraph, a standardized four-layer abstraction that unifies heterogeneous knowledge sources into a common graph representation. Building on this, we introduce a 34M-parameter graph foundation model (GFM) that jointly captures graph topology and textual semantics, and is integrated with LLMs to enhance reasoning in downstream applications. To ensure scalability and efficiency, mixed-precision training and distributed message-passing are implemented to scale GFM with more GPUs. Extensive experiments on six benchmarks show that G-reasoner consistently outperforms state-of-the-art baselines, significantly enhances LLM reasoning, and achieves strong efficiency and cross-graph generalization.

</details>

---

### 47. [Object-Centric Representation Learning for Enhanced 3D Semantic Scene Graph Prediction](https://arxiv.org/abs/2510.04714)

**基本信息**

- 🔗 arXiv: [`2510.04714`](https://arxiv.org/abs/2510.04714)
- 👥 作者: KunHo Heo, GiHyun Kim, SuYeon Kim 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04714.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献之一是提出了一种用于学习对象中心表示的新颖对比预训练策略和特征编码器。虽然应用场景是3D场景理解，但其方法论——即通过解耦表示学习和下游任务来学习高度判别性的对象特征——在化学信息学和质谱分析中具有潜在的应用价值。例如，在质谱结构推理中，可以将质谱峰或分子片段视为“对象”，学习其判别性表示对于推断分子结构至关重要。因此，该论文提供了一种可用于相关主题的特征学习方法和工具。

**📖 中文摘要**

本文专注于3D语义场景图预测任务，旨在检测3D场景中的对象及其语义关系。作者指出，先前的研究虽然解决了数据集限制并探索了包括开放词汇设置在内的各种方法，但未能优化对象和关系特征的表示能力，表现出对图神经网络的过度依赖，尽管其判别能力不足。本文通过广泛分析证明，对象特征的质量在决定整体场景图准确性方面起着关键作用。为了解决这一挑战，作者设计了一个高度判别性的对象特征编码器，并采用了一种对比预训练策略，将对象表示学习与场景图预测解耦。这种设计不仅提高了对象分类的准确性，还直接改善了关系预测。当将预训练的编码器插入现有框架时，在所有评估指标上都观察到了显著的性能提升。此外，作者有效地结合了几何和语义特征来实现更优的关系预测。在3DSSG数据集上的综合实验表明，该方法显著优于先前最先进的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

3D Semantic Scene Graph Prediction aims to detect objects and their semantic relationships in 3D scenes, and has emerged as a crucial technology for robotics and AR/VR applications. While previous research has addressed dataset limitations and explored various approaches including Open-Vocabulary settings, they frequently fail to optimize the representational capacity of object and relationship features, showing excessive reliance on Graph Neural Networks despite insufficient discriminative capability. In this work, we demonstrate through extensive analysis that the quality of object features plays a critical role in determining overall scene graph accuracy. To address this challenge, we design a highly discriminative object feature encoder and employ a contrastive pretraining strategy that decouples object representation learning from the scene graph prediction. This design not only enhances object classification accuracy but also yields direct improvements in relationship prediction. Notably, when plugging in our pretrained encoder into existing frameworks, we observe substantial performance improvements across all evaluation metrics. Additionally, whereas existing approaches have not fully exploited the integration of relationship information, we effectively combine both geometric and semantic features to achieve superior relationship prediction. Comprehensive experiments on the 3DSSG dataset demonstrate that our approach significantly outperforms previous state-of-the-art methods. Our code is publicly available at this https URL .

</details>

---

### 48. [Learning Hamiltonian Flow Maps: Mean Flow Consistency for Large-Timestep Molecular Dynamics](https://arxiv.org/abs/2601.22123)

**基本信息**

- 🔗 arXiv: [`2601.22123`](https://arxiv.org/abs/2601.22123)
- 👥 作者: Winfried Ripken, Michael Plainer, Gregor Lied 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22123.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分子动力学模拟的机器学习框架，这直接属于化学信息学中利用大模型（如机器学习力场）进行分子系统模拟和性质预测的核心主题。

**📖 中文摘要**

本文提出了一种学习哈密顿流映射的框架，用于模拟哈密顿系统的长时间演化。该方法通过预测选定时间跨度内的平均相空间演化，实现了远超经典积分器稳定性限制的大时间步长更新。其核心是施加了一个关于时间平均哈密顿动力学的“平均流一致性”条件。与先前方法不同，该框架允许在无需访问未来状态的情况下，在独立的相空间样本上进行训练，避免了昂贵的轨迹生成。该方法在包括使用机器学习力场（MLFF）的分子动力学模拟在内的多种哈密顿系统中得到验证。该工作与“化学大模型”主题相关，因为它提出了一种用于分子动力学模拟的机器学习框架，这是化学信息学和计算化学中利用大模型进行分子模拟和性质预测的核心应用场景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Simulating the long-time evolution of Hamiltonian systems is limited by the small timesteps required for stable numerical integration. To overcome this constraint, we introduce a framework to learn Hamiltonian Flow Maps by predicting the mean phase-space evolution over a chosen time span, enabling stable large-timestep updates far beyond the stability limits of classical integrators. To this end, we impose a Mean Flow consistency condition for time-averaged Hamiltonian dynamics. Unlike prior approaches, this allows training on independent phase-space samples without access to future states, avoiding expensive trajectory generation. Validated across diverse Hamiltonian systems, our method in particular improves upon molecular dynamics simulations using machine-learned force fields (MLFF). Our models maintain comparable training and inference cost, but support significantly larger integration timesteps while trained directly on widely-available trajectory-free MLFF datasets.

</details>

---

### 49. [A Minimum Variance Path Principle for Accurate and Stable Score-Based Density Ratio Estimation](https://arxiv.org/abs/2602.00834)

**基本信息**

- 🔗 arXiv: [`2602.00834`](https://arxiv.org/abs/2602.00834)
- 👥 作者: Wei Chen, Jiacheng Li, Shigui Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00834.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于概率分布建模，特别是针对分类/离散数据在单纯形上的表示和学习。这种方法是化学信息学中分子表示学习（化学大模型）和质谱数据概率建模（质谱结构推理）的基础工具。

**📖 中文摘要**

本文提出了一种用于在单纯形上学习和采样概率分布的方法。该方法通过光滑双射将开放单纯形映射到欧几里得空间，利用Aitchison几何来定义映射，并通过狄利克雷插值将离散观测去量化成连续观测，从而支持对分类数据的建模。这使得能够通过双射在欧几里得空间中进行密度建模，同时仍能精确恢复原始离散分布。与先前在单纯形上使用黎曼几何或自定义噪声过程的方法相比，该方法在欧几里得空间中工作，同时尊重Aitchison几何，并在合成和真实世界数据集上实现了有竞争力的性能。该工作与“化学大模型”和“质谱结构推理”均相关，因为它提出了一种处理分类/离散数据（如分子指纹、质谱峰的存在/缺失或化合物类别）的概率建模方法，这是化学信息学中分子表示和质谱数据分析的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Score-based methods are powerful across machine learning, but they face a paradox: theoretically path-independent, yet practically path-dependent. We resolve this by proving that practical training objectives differ from the ideal, ground-truth objective by a crucial, overlooked term: the path variance of the score function. We propose the MVP (**M**imum **V**ariance **P**ath) Principle to minimize this path variance. Our key contribution is deriving a closed-form expression for the variance, making optimization tractable. By parameterizing the path with a flexible Kumaraswamy Mixture Model, our method learns data-adaptive, low-variance paths without heuristic manual selection. This principled optimization of the complete objective yields more accurate and stable estimators, establishing new state-of-the-art results on challenging benchmarks and providing a general framework for optimizing score-based interpolation.

</details>

---

### 50. [Composable and adaptive design of machine learning interatomic potentials guided by Fisher-information analysis](https://arxiv.org/abs/2504.19372)

**基本信息**

- 🔗 arXiv: [`2504.19372`](https://arxiv.org/abs/2504.19372)
- 👥 作者: Weishi Wang, Mark K. Transtrum, Vincenzo Lordi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.19372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于机器学习原子间势（MLIPs）的自适应设计策略和评估框架。MLIPs是化学信息学和计算化学中用于预测分子和材料性质的核心模型类型。这项工作通过迭代模型重构和基于费舍尔信息的评估，旨在创建更优、更可解释的化学模型，这直接围绕“化学大模型”的主题，即开发更先进、更智能的化学领域机器学习模型。

**📖 中文摘要**

本文提出了一种用于机器学习原子间势（MLIPs）的自适应、物理启发的模型设计策略。该策略依赖于从单术语模型迭代重构复合模型，并辅以统一的训练程序。为了指导模型重构和超参数优化，作者提出了一种基于费舍尔信息矩阵（FIM）和多属性误差度量的模型评估方法。通过结合重构和评估子程序，该框架在灵活性和可扩展性之间取得了平衡。在一个针对结构多样的铌数据集的案例研究中，该框架生成的包含75个参数的最优模型配置实现了0.172 eV/Å的力RMSE和0.013 eV/原子的能量RMSE。这项工作展示了如何通过系统性的、信息驱动的框架来设计和优化用于化学和材料科学的机器学习模型，与开发更智能、更可解释的“化学大模型”的研究方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An adaptive physics-inspired model design strategy for machine-learning interatomic potentials (MLIPs) is proposed. This strategy relies on iterative reconfigurations of composite models from single-term models, followed by a unified training procedure. A model evaluation method based on the Fisher information matrix (FIM) and multiple-property error metrics is also proposed to guide the model reconfiguration and hyperparameter optimization. By combining the reconfiguration and the evaluation subroutines, we provide an adaptive MLIP design strategy that balances flexibility and extensibility. In a case study of designing models against a structurally diverse niobium dataset, we managed to obtain an optimal model configuration with 75 parameters generated by our framework that achieved a force RMSE of 0.172 eV/Å and an energy RMSE of 0.013 eV/atom.

</details>

---

### 51. [Understanding protein function with a multimodal retrieval-augmented foundation model](https://arxiv.org/abs/2508.04724)

**基本信息**

- 🔗 arXiv: [`2508.04724`](https://arxiv.org/abs/2508.04724)
- 👥 作者: Timothy Fei Truong Jr, Tristan Bepler
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.04724.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个名为PoET-2的多模态、检索增强的蛋白质基础模型。蛋白质是复杂的生物大分子，其序列-结构-功能关系的建模是化学信息学和计算生物学的前沿。PoET-2作为一个先进的蛋白质语言模型，直接属于“化学大模型”的研究范畴，旨在提升对蛋白质功能的理解和预测能力。

**📖 中文摘要**

本文介绍了PoET-2，一个多模态、检索增强的蛋白质基础模型。该模型通过结合家族特异性进化约束的上下文学习以及可选的结构条件，来学习蛋白质序列的生成分布。PoET-2采用分层Transformer编码器和具有因果与掩码语言建模目标的双解码器架构，使其能够在完全生成和双向表示学习两种模式下运行。PoET-2在零样本变体效应预测上达到了最先进的性能，尤其在评分多重突变和具有挑战性的插入缺失突变方面表现出色。在监督设置下，PoET-2的嵌入在学习和预测蛋白质序列-功能关系方面优于先前的方法，特别是在小数据集上。这项工作强调了将检索增强与多模态、以家族为中心的建模相结合，对于推进蛋白质基础模型的益处。蛋白质序列和功能的建模是化学信息学和生物信息学的核心，属于广义的“化学大模型”范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (PLMs) learn probability distributions over natural protein sequences. By learning from hundreds of millions of natural protein sequences, protein understanding and design capabilities emerge. Recent works have shown that scaling these models improves structure prediction, but does not seem to improve mutation understanding and representation quality for protein function prediction. We introduce PoET-2, a multimodal, retrieval-augmented protein foundation model that incorporates in-context learning of family-specific evolutionary constraints with optional structure conditioning to learn generative distributions over protein sequences. PoET-2 uses a hierarchical transformer encoder that is equivariant to sequence context ordering and a dual decoder architecture with both causal and masked language modeling objectives, allowing PoET-2 to operate in both fully generative and bidirectional representation learning modes. PoET-2 achieves state-of-the-art performance on zero-shot variant effect prediction, excelling at scoring variants with multiple mutations and challenging indel mutations. In supervised settings, PoET-2 embeddings outperform previous methods for learning sequence-function relationships, especially with small datasets. This work highlights the benefits of combining retrieval augmentation with multimodal, family-centric modeling for advancing protein foundation models.

</details>

---

### 52. [TokEye: Fast Signal Extraction for Fluctuating Time Series via Offline Self-Supervised Learning From Fusion Diagnostics to Bioacoustics](https://arxiv.org/abs/2602.20317)

**基本信息**

- 🔗 arXiv: [`2602.20317`](https://arxiv.org/abs/2602.20317)
- 👥 作者: Nathaniel Chen, Kouroche Bouchiat, Peter Steiner 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20317.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个从高噪声、多通道时序信号中自动提取相干和瞬态模式的通用框架。尽管应用场景是聚变等离子体诊断，但其核心技术——针对波动测量进行信号处理、特征提取和模式识别——与“质谱结构推理”中处理复杂的质谱/色谱-质谱数据以识别分子特征和碎片的挑战在本质上是一致的。论文提出的自监督学习框架和快速神经网络代理方法，为解决质谱数据中类似的信息提取和推理问题提供了潜在的技术路径。

**📖 中文摘要**

本文提出了一个“信号优先”的自监督学习框架，用于从各种传感器的高噪声时频数据中自动提取相干和瞬态模式。作者开发了一种通用方法和工具，通过在多通道信号处理中应用非线性优化技术，并利用快速神经网络代理，从托卡马克装置（如DIII-D）的快速磁学、电子回旋辐射、CO2干涉仪和束发射光谱测量中提取相干、准相干和瞬态模式。该框架在DIII-D、TJ-II和非融合语谱图的数据上进行了测试。推理延迟为0.5秒，使得该框架能够实现实时模式识别和大规模自动化数据库生成，用于先进的等离子体控制。这项工作虽然主要应用于聚变诊断，但其核心是开发一种从复杂、高噪声的时序信号（类似于质谱中的色谱-质谱联用数据）中提取特征和模式的通用方法。这种信号处理和模式识别技术与“质谱结构推理”中从质谱数据中提取分子特征和推断结构所面临的挑战在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Next-generation fusion facilities like ITER face a "data deluge," generating petabytes of multi-diagnostic signals daily that challenge manual analysis. We present a "signals-first" self-supervised framework for the automated extraction of coherent and transient modes from high-noise time-frequency data across a variety of sensors. We also develop a general-purpose method and tool for extracting coherent, quasi-coherent, and transient modes for fluctuation measurements in tokamaks by employing non-linear optimal techniques in multichannel signal processing with a fast neural network surrogate on fast magnetics, electron cyclotron emission, CO2 interferometers, and beam emission spectroscopy measurements from DIII-D. Results are tested on data from DIII-D, TJ-II, and non-fusion spectrograms. With an inference latency of 0.5 seconds, this framework enables real-time mode identification and large-scale automated database generation for advanced plasma control. Repository is in this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：2
- 累计论文数量：89

## 📝 历史记录

> 暂无历史数据

