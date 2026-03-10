# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-10 12:57:44

## 📅 2026-03-10 (今日最新)

**相关论文数：131**

### 1. [Unmixing microinfrared spectroscopic images of cross-sections of historical oil paintings](https://arxiv.org/abs/2603.06673)

**基本信息**

- 🔗 arXiv: [`2603.06673`](https://arxiv.org/abs/2603.06673)
- 👥 作者: Shivam Pande, Nicolas Nadisic, Francisco Mederos-Henry 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06673.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于分析化学/材料（历史油画）高光谱图像的无监督CNN自编码器方法。该方法的核心是处理由ATR-μFTIR仪器产生的光谱数据，这是一种重要的化学分析技术。论文专注于从混合光谱中盲提取端元（化学组分）及其丰度，这本质上是化学信息学中的一种数据解析和特征提取任务，为相关领域提供了算法工具。

**📖 中文摘要**

本文提出了一种用于分析历史油画横截面的衰减全反射傅里叶变换红外显微光谱（ATR-μFTIR）高光谱图像（HSI）的无监督盲解混方法。该方法利用卷积神经网络（CNN）自编码器，通过基于图像块的建模来利用局部空间结构，从而估计端元光谱及其丰度图。为了解决超过1500个波段中由大气和采集伪影引起的敏感性，作者引入了一种加权光谱角距离（WSAD）损失函数，该函数利用空间平坦度、相邻像素一致性和光谱粗糙度的鲁棒度量来自动计算波段可靠性权重。与标准SAD训练相比，WSAD在易受污染的光谱区域提高了结果的可解释性。该方法在归因于范艾克兄弟的《根特祭坛画》的ATR-μFTIR横截面数据上进行了演示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Spectroscopic imaging (SI) has become central to heritage science because it enables non-invasive, spatially resolved characterisation of materials in artefacts. In particular, attenuated total reflection Fourier transform infrared microscopy (ATR-$\mu$FTIR) is widely used to analyse painting cross-sections, where a spectrum is recorded at each pixel to form a hyperspectral image (HSI). Interpreting these data is difficult: spectra are often mixtures of several species in heterogeneous, multi-layered and degraded samples, and current practice still relies heavily on manual comparison with reference libraries. This workflow is slow, subjective and hard to scale. We propose an unsupervised CNN autoencoder for blind unmixing of ATR-$\mu$FTIR HSIs, estimating endmember spectra and their abundance maps while exploiting local spatial structure through patch-based modelling. To reduce sensitivity to atmospheric and acquisition artefacts across $>1500$ bands, we introduce a weighted spectral angle distance (WSAD) loss with automatic band-reliability weights derived from robust measures of spatial flatness, neighbour agreement and spectral roughness. Compared with standard SAD training, WSAD improves interpretability in contamination-prone spectral regions. We demonstrate the method on an ATR-$\mu$FTIR cross-section from the Ghent Altarpiece attributed to the Van Eyck brothers.

</details>

---

### 2. [Spectral Gaps and Spatial Priors: Studying Hyperspectral Downstream Adaptation Using TerraMind](https://arxiv.org/abs/2603.06690)

**基本信息**

- 🔗 arXiv: [`2603.06690`](https://arxiv.org/abs/2603.06690)
- 👥 作者: Julia Anna Leonardi, Johannes Jakubik, Paolo Fraccaro 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06690.pdf)

**💡 相关性分析**

满足标准2：论文专注于高光谱成像（HSI）数据的下游任务适应。HSI是化学分析（如材料鉴定、环境监测）和质谱成像相关领域的重要数据模态。研究评估了基础模型处理这种复杂化学/光谱数据的能力，并提出了适应策略，为化学信息学中处理高维光谱数据提供了方法论参考和基准。

**📖 中文摘要**

本研究探讨了地理空间基础模型（GFM）TerraMind对高光谱成像（HSI）下游任务的适应性，而无需进行HSI特定的预训练。高光谱数据具有高维度和复杂性，通常缺乏原生支持。作者比较了两种通道适应策略：朴素波段选择和基于物理感知的光谱响应函数（SRF）分组。实验结果表明，具有HSI原生支持的深度学习模型总体表现更优，但TerraMind通过波段选择策略也能以适度的性能下降适应HSI下游任务。这项研究为HSI数据集成建立了关键基线，并激励未来多模态模型架构需要原生光谱标记化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Geospatial Foundation Models (GFMs) typically lack native support for Hyperspectral Imaging (HSI) due to the complexity and sheer size of high-dimensional spectral data. This study investigates the adaptability of TerraMind, a multimodal GFM, to address HSI downstream tasks \emph{without} HSI-specific pretraining. Therefore, we implement and compare two channel adaptation strategies: Naive Band Selection and physics-aware Spectral Response Function (SRF) grouping. Overall, our results indicate a general superiority of deep learning models with native support of HSI data. Our experiments also demonstrate the ability of TerraMind to adapt to HSI downstream tasks through band selection with moderate performance decline. Therefore, the findings of this research establish a critical baseline for HSI integration, motivating the need for native spectral tokenization in future multimodal model architectures.

</details>

---

### 3. [ProtAlign: Contrastive learning paradigm for Sequence and structure alignment](https://arxiv.org/abs/2603.06722)

**基本信息**

- 🔗 arXiv: [`2603.06722`](https://arxiv.org/abs/2603.06722)
- 👥 作者: Aditya Ranganath, Hasin Us Sami, Kowshik Thopalli 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06722.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个连接蛋白质序列和结构的对比学习框架。这直接属于‘化学大模型’的范畴，因为蛋白质语言模型是化学和生物信息学中大模型的重要应用。该工作旨在创建统一的表示，这对于基于大模型的分子/蛋白质性质预测和设计至关重要。

**📖 中文摘要**

本文提出了一种名为ProtAlign的序列结构对比对齐框架，旨在解决蛋白质语言模型通常只考虑蛋白质序列与其文本描述的对齐，而忽略结构信息的问题。该框架通过在大规模序列和实验解析或预测的结构对上训练，学习一个共享的嵌入空间，使得蛋白质在不同模态（序列和结构）下具有一致的表示。它最大化匹配的序列-结构对之间的一致性，同时推开不相关的对。这种对齐实现了跨模态检索（例如，给定序列找到结构邻居），并改善了功能注释和稳定性估计等下游预测任务，提供了序列变异和结构组织之间可解释的联系。这项工作展示了对比学习可以作为连接蛋白质序列和结构的强大桥梁，为理解和设计蛋白质提供了统一的表示方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models often take into consideration the alignment between a protein sequence and its textual description. However, they do not take structural information into consideration. Traditional methods treat sequence and structure separately, limiting the ability to exploit the alignment between the structure and protein sequence embeddings. In this paper, we introduce a sequence structure contrastive alignment framework, which learns a shared embedding space where proteins are represented consistently across modalities. By training on large-scale pairs of sequences and experimentally resolved or predicted structures, the model maximizes agreement between matched sequence structure pairs while pushing apart unrelated pairs. This alignment enables cross-modal retrieval (e.g., finding structural neighbors given a sequence), improves downstream prediction tasks such as function annotation and stability estimation, and provides interpretable links between sequence variation and structural organization. Our results demonstrate that contrastive learning can serve as a powerful bridge between protein sequences and structures, offering a unified representation for understanding and engineering proteins.

</details>

---

### 4. [Property-driven Protein Inverse Folding With Multi-Objective Preference Alignment](https://arxiv.org/abs/2603.06748)

**基本信息**

- 🔗 arXiv: [`2603.06748`](https://arxiv.org/abs/2603.06748)
- 👥 作者: Xiaoyang Hou, Junqi Liu, Chence Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06748.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质序列设计的AI框架（ProtAlign），它微调预训练的逆折叠模型（一种化学/生物大模型）以优化多个属性。这直接围绕‘化学大模型’主题，涉及使用和优化用于分子/蛋白质设计的机器学习模型。

**📖 中文摘要**

本文介绍了ProtAlign，一个多目标偏好对齐框架，用于微调预训练的蛋白质逆折叠模型（如ProteinMPNN），以在保持结构保真度的同时满足多种可开发性目标（如溶解度、热稳定性、表达水平）。蛋白质序列设计需要在可设计性（恢复目标骨架的能力）与多个通常相互竞争的可开发性属性之间取得平衡。现有方法通过事后突变、推理时偏置或在特定属性子集上重新训练来解决这些问题，但它们依赖于目标且需要大量领域专业知识或仔细的超参数调整。ProtAlign采用一种具有灵活偏好边界的半在线直接偏好优化策略，利用计算机属性预测器构建偏好对，以减轻竞争目标之间的冲突。应用表明，生成的模型MoMPNN在包括CATH 4.3晶体结构序列设计、从头生成的骨架以及真实世界结合剂设计场景等任务中，都能在不损害可设计性的情况下增强可开发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequence design must balance designability, defined as the ability to recover a target backbone, with multiple, often competing, developability properties such as solubility, thermostability, and expression. Existing approaches address these properties through post hoc mutation, inference-time biasing, or retraining on property-specific subsets, yet they are target dependent and demand substantial domain expertise or careful hyperparameter tuning. In this paper, we introduce ProtAlign, a multi-objective preference alignment framework that fine-tunes pretrained inverse folding models to satisfy diverse developability objectives while preserving structural fidelity. ProtAlign employs a semi-online Direct Preference Optimization strategy with a flexible preference margin to mitigate conflicts among competing objectives and constructs preference pairs using in silico property predictors. Applied to the widely used ProteinMPNN backbone, the resulting model MoMPNN enhances developability without compromising designability across tasks including sequence design for CATH 4.3 crystal structures, de novo generated backbones, and real-world binder design scenarios, making it an appealing framework for practical protein sequence design.

</details>

---

### 5. [Failure Detection in Chemical Processes using Symbolic Machine Learning: A Case Study on Ethylene Oxidation](https://arxiv.org/abs/2603.06767)

**基本信息**

- 🔗 arXiv: [`2603.06767`](https://arxiv.org/abs/2603.06767)
- 👥 作者: Julien Amblard, Niklas Groll, Matthew Tait 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06767.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用符号机器学习进行化学过程（乙烯氧化）的故障预测。这属于‘化学信息学’领域，涉及为化学过程开发基于AI的预测模型。虽然不直接涉及质谱，但其方法论（符号学习）和领域（化学过程）与化学信息学相关。

**📖 中文摘要**

本文研究了在化学过程中使用符号机器学习预测故障的方法，并以乙烯氧化过程为背景进行了可行性研究。在化学过程工业中，安全性至关重要，而大规模神经网络方法往往由于其脆弱性、缺乏可解释性和可解释性而不适用。此外，该领域包含历史故障的开源真实世界数据集稀缺。作者的方法建立在一种先进的符号机器学习系统之上，该系统能够从上下文相关的噪声示例中学习以概率规则形式表示的预测模型。该系统是一个通用符号学习器，因此该方法独立于任何特定的化学过程。为了解决缺乏真实故障数据的问题，本研究利用化学过程模拟器生成的数据进行可行性研究。实验结果表明，符号机器学习可以超越随机森林和多层感知机等基线方法，同时通过生成紧凑的、基于规则的预测模型来保持可解释性。最后，作者解释了如何将此类学习到的基于规则的模型集成到智能体中，以在潜在故障期间协助化工厂操作员进行决策。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Over the past decade, Artificial Intelligence has significantly advanced, mostly driven by large-scale neural approaches. However, in the chemical process industry, where safety is critical, these methods are often unsuitable due to their brittleness, and lack of explainability and interpretability. Furthermore, open-source real-world datasets containing historical failures are scarce in this domain. In this paper, we investigate an approach for predicting failures in chemical processes using symbolic machine learning and conduct a feasibility study in the context of an ethylene oxidation process. Our method builds on a state-of-the-art symbolic machine learning system capable of learning predictive models in the form of probabilistic rules from context-dependent noisy examples. This system is a general-purpose symbolic learner, which makes our approach independent of any specific chemical process. To address the lack of real-world failure data, we conduct our feasibility study leveraging data generated from a chemical process simulator. Experimental results show that symbolic machine learning can outperform baseline methods such as random forest and multilayer perceptron, while preserving interpretability through the generation of compact, rule-based predictive models. Finally, we explain how such learned rule-based models could be integrated into agents to assist chemical plant operators in decision-making during potential failures.

</details>

---

### 6. [Joint 3D Gravity and Magnetic Inversion via Rectified Flow and Ginzburg-Landau Guidance](https://arxiv.org/abs/2603.06829)

**基本信息**

- 🔗 arXiv: [`2603.06829`](https://arxiv.org/abs/2603.06829)
- 👥 作者: Dhruman Gupta, Yashas Shende, Aritra Das 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06829.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于3D重磁联合反演的生成式AI框架，并在Noddyverse数据集上进行了实现。Noddyverse被描述为‘最大的基于物理学的反演数据集’。虽然论文主题是地球物理反演而非化学质谱，但它明确提供了‘可用于这些主题的数据集、资源或工具’（即Noddyverse数据集和相关的生成模型/VAE）。这些资源和方法论（处理物理反问题的生成模型）可能对化学信息学中类似的反问题（如从光谱数据推断结构）具有启发性和潜在适用性。

**📖 中文摘要**

本文介绍了一个用于3D重力和磁力联合反演的新框架，该框架将反问题重新表述为在Noddyverse数据集（最大的基于物理学的反演数据集）上的整流流问题。地下矿石检测至关重要，而重磁联合反演是一种超越传统地质勘探方法局限性的有前景的新方法。给定表面上的磁力和重力数据，联合重建产生它们的底层密度场仍然是一个不适定的反问题。虽然多个属性的联合反演减轻了磁力和重力数据中的非唯一性问题，但确定性算法会收敛到单个正则化解，因此无法捕捉可能解的分布。同样，大多数基于机器学习的技术预测单个解而不对整个分布进行建模。作者引入了Ginzburg-Landau正则化器，这是Ising模型的广义版本，有助于矿石识别，实现了物理感知训练。还提出了一种基于GL理论的引导方法，可以作为即插即用模块与现有的无条件去噪器一起使用。此外，作者还训练并发布了一个用于3D密度场的VAE，以促进该领域的下游工作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Subsurface ore detection is of paramount importance given the gradual depletion of shallow mineral resources in recent years. It is crucial to explore approaches that go beyond the limitations of traditional geological exploration methods. One such promising new method is joint magnetic and gravitational inversion. Given magnetic and gravitational data on a surface, jointly reconstructing the underlying densities that generate them remains an ill-posed inverse problem. Although joint inversion of multiple properties mitigates the non-uniqueness problem in magnetic and gravitational data, deterministic algorithms converge to a single regularized solution and thus do not capture the distribution of possible solutions. Similarly, most machine learning based techniques predict a single solution without modelling the entire distribution. In this paper, we introduce a novel framework that reframes 3D gravity and magnetic joint inversion as a rectified flow on the Noddyverse dataset, the largest physics-based dataset for inversion. We introduce a Ginzburg-Landau (GL) regularizer, a generalized version of the Ising model that aids in ore identification, enabling physics-aware training. We also propose a guidance methodology based on GL theory that can be used as a plug-and-play module with existing unconditional denoisers. Lastly, we also train and release a VAE for the 3D densities, which facilitates downstream work in the field.

</details>

---

### 7. [Symmetry-Constrained Language-Guided Program Synthesis for Discovering Governing Equations from Noisy and Partial Observations](https://arxiv.org/abs/2603.06869)

**基本信息**

- 🔗 arXiv: [`2603.06869`](https://arxiv.org/abs/2603.06869)
- 👥 作者: Mirza Samad Ahmed Baig, Syeda Anshrah Gillani
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06869.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发一个用于从数据中发现符号方程的AI框架（SymLang），它结合了语言模型引导的程序合成和物理约束。这直接属于‘化学大模型’的范畴，因为发现控制方程是科学机器学习（AI4Science）和化学动力学建模的核心。此外，该框架本身是一个可用于这些主题的工具（数据驱动的方程发现）。

**📖 中文摘要**

本文介绍了SymLang（对称性约束的语言引导方程发现），一个统一的框架，用于从噪声和部分观测中发现紧凑的控制方程。该框架结合了三个先前独立的思想：(i) 类型化的对称性约束语法，将量纲分析、群论不变性和奇偶性约束编码为硬生产规则，平均在拟合之前消除了71.3%的候选表达式树；(ii) 语言模型引导的程序合成，其中微调过的70亿参数提议器，以可解释的数据描述符为条件，高效地导航受约束的搜索空间；(iii) MDL正则化的贝叶斯模型选择与块bootstrap稳定性分析相结合，量化结构不确定性而不是承诺单一的最佳方程。在涵盖经典力学、电动力学、热力学、种群动力学和非线性振荡器的133个动力系统中，SymLang在10%观测噪声下实现了83.7%的精确结构恢复率，比次优基线提高了22.4个百分点，同时将分布外外推误差减少了61%，并几乎消除了守恒律违反。该框架正确识别了结构简并性，明确报告了这一点，而不是返回一个 confidently wrong 的单一方程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering compact governing equations from experimental observations is one of the defining objectives of quantitative science, yet practical discovery pipelines routinely fail when measurements are noisy, relevant state variables are unobserved, or multiple symbolic structures explain the data equally well within statistical uncertainty. Here we introduce SymLang (Symmetry-constrained Language-guided equation discovery), a unified framework that brings together three previously separate ideas: (i) typed symmetry-constrained grammars that encode dimensional analysis, group-theoretic invariance, and parity constraints as hard production rules, eliminating on average 71.3% of candidate expression trees before any fitting; (ii) language-model-guided program synthesis in which a fine-tuned 7B-parameter proposer, conditioned on interpretable data descriptors, efficiently navigates the constrained search space; and (iii) MDL-regularized Bayesian model selection coupled with block-bootstrap stability analysis that quantifies structural uncertainty rather than committing to a single best equation. Across 133 dynamical systems spanning classical mechanics, electrodynamics, thermodynamics, population dynamics, and nonlinear oscillators, SymLang achieves an exact structural recovery rate of 83.7% under 10% observational noise - a 22.4 percentage-point improvement over the next-best baseline - while reducing out-of-distribution extrapolation error by 61% and near-eliminating conservation-law violations (3.1 x 10-3 vs. 187.3 x 10-3 physical drift for the closest competitor). In all tested regimes the framework correctly identifies structural degeneracy, reporting it explicitly rather than returning a confidently wrong single equation. The framework is fully open-source and reproducible, providing a principled pathway from raw data to interpretable, physically auditable symbolic laws.

</details>

---

### 8. [A Dynamic Self-Evolving Extraction System](https://arxiv.org/abs/2603.06915)

**基本信息**

- 🔗 arXiv: [`2603.06915`](https://arxiv.org/abs/2603.06915)
- 👥 作者: Moin Amin-Naseri, Hannah Kim, Estevam Hruschka
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06915.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个动态自进化的知识库系统，该系统利用LLM进行信息提取和知识积累，形成一个闭环学习框架。这与化学信息学中利用大模型（化学大模型）构建、管理和推理化学知识库（如分子结构、性质、反应等）的核心主题直接相关。

**📖 中文摘要**

本文提出DySECT，一个动态自进化的信息提取和知识库构建系统。该系统利用大型语言模型从原始文本中提取结构化信息（三元组），并持续填充一个自扩展的知识库。知识库通过整合概率知识和基于图的推理来丰富自身，逐渐积累领域概念和关系。随后，这个丰富的知识库通过提示调优、相关少样本示例采样或使用知识库衍生的合成数据进行微调，反馈给LLM提取器，形成一个提取与知识相互促进的共生闭环。该框架的核心是构建一个动态更新的、可推理的知识库，并利用LLM进行信息提取，这与化学信息学中构建和利用大型化学知识库、训练化学大模型进行信息提取和推理的任务高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The extraction of structured information from raw text is a fundamental component of many NLP applications, including document retrieval, ranking, and relevance estimation. High-quality extractions often require domain-specific accuracy, up-to-date understanding of specialized taxonomies, and the ability to incorporate emerging jargon and rare outliers. In many domains--such as medical, legal, and HR--the extraction model must also adapt to shifting terminology and benefit from explicit reasoning over structured knowledge. We propose DySECT, a Dynamic Self-Evolving Extraction and Curation Toolkit, which continually improves as it is used. The system incrementally populates a versatile, self-expanding knowledge base (KB) with triples extracted by the LLM. The KB further enriches itself through the integration of probabilistic knowledge and graph-based reasoning, gradually accumulating domain concepts and relationships. The enriched KB then feeds back into the LLM extractor via prompt tuning, sampling of relevant few-shot examples, or fine-tuning using KB-derived synthetic data. As a result, the system forms a symbiotic closed-loop cycle in which extraction continuously improves knowledge, and knowledge continuously improves extraction.

</details>

---

### 9. [NerVE: Nonlinear Eigenspectrum Dynamics in LLM Feed-Forward Networks](https://arxiv.org/abs/2603.06922)

**基本信息**

- 🔗 arXiv: [`2603.06922`](https://arxiv.org/abs/2603.06922)
- 👥 作者: Nandan Kumar Jha, Brandon Reagen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06922.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深入分析和理解大型语言模型（LLM）中前馈网络模块的内部工作机制和动力学。虽然研究对象是通用LLM，但其分析框架（NerVE）和关于模型容量分配、信息流调节的见解，对于理解和设计专门用于化学领域的“化学大模型”（如用于分子性质预测、反应生成的Transformer模型）具有重要的方法论参考价值，属于核心主题相关的底层机制研究。

**📖 中文摘要**

本文提出了NerVE框架，用于理解大型语言模型中前馈网络在高维潜在空间中组织和调节信息流的特征谱动力学。尽管FFN占据了大部分参数，但其高维动力学仍不明确。NerVE通过四个互补的指标（谱熵、参与比、特征值早期富集和Jensen-Shannon散度）来轻量级、高效地跟踪特征谱动态。核心见解是FFN的非线性会在特征模态间重新注入方差，从根本上控制潜在维度的利用，并且优化器的几何形状强烈调节这种方差重新注入的程度。该研究验证了NerVE在不同模型规模、架构和优化器配置下的有效性，揭示了FFN动力学的稳定特征谱特征，这些特征与模型的泛化能力相关。这项工作为理解大模型内部工作机制提供了新视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce NerVE, a unified eigenspectral framework for understanding how feed-forward networks (FFNs) in large language models (LLMs) organize and regulate information flow in high-dimensional latent space. Despite FFNs dominating the parameter budget, their high-dimensional dynamics remain poorly understood. NerVE addresses this gap through lightweight, memory-efficient tracking of eigenspectrum dynamics via four complementary metrics: Spectral Entropy (dispersion), Participation Ratio (effective dimensionality), Eigenvalue Early Enrichment (top-heaviness), and Jensen-Shannon divergence (distributional shifts). Our key insight is that FFN nonlinearities reinject variance across eigenmodes, fundamentally governing latent dimension utilization, and that optimizer geometry strongly modulates the extent of this variance reinjection. We validate NerVE across model scales, and diverse architectural and optimizer configurations, each uniquely shaping FFN dynamics: normalization schemes controlling variance flow; FFN weight geometries constraining latent space; positional encoding and activation functions regulating information flow; and optimizer choices redistributing effective capacity across depth. Across these settings, NerVE consistently recovers stable spectral signatures that correlate with model's generalization ability and respond predictably to design choices, generalizing beyond transformer to MLP-Mixer architectures, providing actionable insights for architectural and optimizer choices beyond trial-and-error.

</details>

---

### 10. [Extracting and analyzing 3D histomorphometric features related to perineural and lymphovascular invasion in prostate cancer](https://arxiv.org/abs/2603.06936)

**基本信息**

- 🔗 arXiv: [`2603.06936`](https://arxiv.org/abs/2603.06936)
- 👥 作者: Sarah S.L. Chow, Rui Wang, Robert B. Serafin 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06936.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个从3D医学影像数据中自动分割关键生物结构（神经、血管）并提取定量形态学特征的分析流程。虽然应用领域是病理学，但其核心贡献——一个基于深度学习的3D分割模型（nnU-Net）和一套特征提取方法——为化学信息学和质谱分析领域提供了潜在的数据处理工具和范式。例如，该流程可被借鉴用于从3D分子成像或复杂的质谱成像数据中分割特定区域、提取定量特征，从而构建用于“质谱结构推理”或化学大模型训练的数据集。

**📖 中文摘要**

本研究开发了一个分析流程，用于提取与前列腺癌预后不良相关的神经周围浸润和淋巴血管浸润的3D组织形态学特征。研究使用nnU-Net模型在3D前列腺切除标本数据集中分割神经和血管，这些数据集通过光学清除、荧光H&E类似物标记和开放式光片显微镜成像获得。基于3D神经/血管分割掩膜和癌症富集区域的3D掩膜，提取了描述癌-神经和癌-血管接近度的PNI和LVI相关特征。作为对这些特征预后价值的初步探索，研究训练了一个监督机器学习分类器来预测5年生化复发结果，发现3D PNI相关特征具有中等预后能力，且优于2D PNI相关特征。这项工作展示了利用3D成像和深度学习提取定量形态学特征以辅助癌症风险评估的流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diagnostic grading of prostate cancer (PCa) relies on the examination of 2D histology sections. However, the limited sampling of specimens afforded by 2D histopathology, and ambiguities when viewing 2D cross-sections, can lead to suboptimal treatment decisions. Recent studies have shown that 3D histomorphometric analysis of glands and nuclei can improve PCa risk assessment compared to analogous 2D features. Here, we expand on these efforts by developing an analytical pipeline to extract 3D features related to perineural invasion (PNI) and lymphovascular invasion (LVI), which correlate with poor prognosis for a variety of cancers. A 3D segmentation model (nnU-Net) was trained to segment nerves and vessels in 3D datasets of archived prostatectomy specimens that were optically cleared, labeled with a fluorescent analog of H&E, and imaged with open-top light-sheet (OTLS) microscopy. PNI- and LVI-related features, including metrics describing cancer-nerve and cancer-vessel proximity, were then extracted based on the 3D nerve/vessel segmentation masks in conjunction with 3D masks of cancer-enriched regions. As a preliminary exploration of the prognostic value of these features, we trained a supervised machine learning classifier to predict 5-year biochemical recurrence (BCR) outcomes, finding that 3D PNI-related features are moderately prognostic and outperform 2D PNI-related features (AUC = 0.71 vs. 0.52). Source code is available at this https URL .

</details>

---

### 11. [Conditional Unbalanced Optimal Transport Maps: An Outlier-Robust Framework for Conditional Generative Modeling](https://arxiv.org/abs/2603.06972)

**基本信息**

- 🔗 arXiv: [`2603.06972`](https://arxiv.org/abs/2603.06972)
- 👥 作者: Jiwoo Yoon, Kyumin Choi, Jaewoong Choi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06972.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进条件最优传输理论并应用于生成建模，提出了对异常值更鲁棒的条件生成模型。最优传输理论在机器学习中有着广泛应用，包括分子生成、化学空间探索等。这项工作为构建更稳健的“化学大模型”（特别是用于分子生成或条件分子设计的模型）提供了新的理论工具和算法思路，属于核心主题相关的底层方法学创新。

**📖 中文摘要**

本文针对条件最优传输在生成建模中对异常值敏感的问题，提出了条件非平衡最优传输框架。CUOT通过Csiszár散度惩罚放松了条件分布匹配约束，同时严格保留了条件边际。基于其对偶形式，提出了条件非平衡最优传输映射，这是一个基于三角c-变换参数化的、对异常值鲁棒的条件生成模型。理论证明了最优三角映射满足c-变换关系。在2D合成和图像尺度数据集上的实验表明，CUOTM在异常值鲁棒性和分布匹配性能上优于现有的基于COT的基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Conditional Optimal Transport (COT) problem aims to find a transport map between conditional source and target distributions while minimizing the transport cost. Recently, these transport maps have been utilized in conditional generative modeling tasks to establish efficient mappings between the distributions. However, classical COT inherits a fundamental limitation of optimal transport, i.e., sensitivity to outliers, which arises from the hard distribution matching constraints. This limitation becomes more pronounced in a conditional setting, where each conditional distribution is estimated from a limited subset of data. To address this, we introduce the Conditional Unbalanced Optimal Transport (CUOT) framework, which relaxes conditional distribution-matching constraints through Csiszár divergence penalties while strictly preserving the conditioning marginals. We establish a rigorous formulation of the CUOT problem and derive its dual and semi-dual formulations. Based on the semi-dual form, we propose Conditional Unbalanced Optimal Transport Maps (CUOTM), an outlier-robust conditional generative model built upon a triangular $c$-transform parameterization. We theoretically justify the validity of this parameterization by proving that the optimal triangular map satisfies the $c$-transform relationships. Our experiments on 2D synthetic and image-scale datasets demonstrate that CUOTM achieves superior outlier robustness and competitive distribution-matching performance compared to existing COT-based baselines, while maintaining high sampling efficiency.

</details>

---

### 12. [A Systematic Investigation of Document Chunking Strategies and Embedding Sensitivity](https://arxiv.org/abs/2603.06976)

**基本信息**

- 🔗 arXiv: [`2603.06976`](https://arxiv.org/abs/2603.06976)
- 👥 作者: Muhammad Arslan Shaukat, Muntasir Adnan, Carlos C. N. Kuhn
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06976.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是对文档分块策略进行了系统的实证研究和评估，并提供了性能最佳的策略（如段落分组分块）。在化学信息学中，处理科学文献、专利或分子数据库文本时，有效的文档分块是构建高质量检索系统或为大模型准备训练数据的关键预处理步骤。这项工作为相关领域的研究者和实践者提供了直接可用的数据预处理工具和策略选择指南，属于数据资源相关的工具和方法论。

**📖 中文摘要**

本文首次对稠密检索中的文档分块策略进行了大规模、跨领域的评估。研究比较了36种分割方法，包括固定大小、语义、结构感知、分层、自适应和LLM辅助等方法，在六个不同知识领域使用五种不同的嵌入模型进行了基准测试。结果表明，内容感知分块显著提高了检索效果。性能最佳的段落分组分块策略实现了最高的总体准确性。研究还观察到明显的领域特异性差异，并量化了高级分块策略在效率上的权衡。这些发现确立了分块作为提高检索性能和可靠性的关键杠杆。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present the first large-scale, cross-domain evaluation of document chunking strategies for dense retrieval, addressing a critical but underexplored aspect of retrieval-augmented systems. In our study, 36 segmentation methods spanning fixed-size, semantic, structure-aware, hierarchical, adaptive, and LLM-assisted approaches are benchmarked across six diverse knowledge domains using five different embedding models. Retrieval performance is assessed using graded relevance scores from a state-of-the-art LLM evaluator, with Normalised DCG@5 as the primary metric (complemented by Hit@5 and MRR). Our experiments show that content-aware chunking significantly improves retrieval effectiveness over naive fixed-length splitting. The top-performing strategy, Paragraph Group Chunking, achieved the highest overall accuracy (mean nDCG@5~0.459) and substantially better top-rank hit rates (Precision@1~24%, Hit@5~59%). In contrast, simple fixed-size character chunking as baselines performed poorly (nDCG@5 < 0.244, Precision@1~2-3%). We observe pronounced domain-specific differences: dynamic token sizing is strongest in biology, physics and health, while paragraph grouping is strongest in legal and maths. Larger embedding models yield higher absolute scores but remain sensitive to suboptimal segmentation, indicating that better chunking and large embeddings provide complementary benefits. In addition to accuracy gains, we quantify the efficiency trade-offs of advanced chunking. Producing more, smaller chunks can increase index size and latency. Consequently, we identify methods (like dynamic chunking) that approach an optimal balance of effectiveness and efficiency. These findings establish chunking as a vital lever for improving retrieval performance and reliability.

</details>

---

### 13. [Optimizing Multi-Modal Models for Image-Based Shape Retrieval: The Role of Pre-Alignment and Hard Contrastive Learning](https://arxiv.org/abs/2603.06982)

**基本信息**

- 🔗 arXiv: [`2603.06982`](https://arxiv.org/abs/2603.06982)
- 👥 作者: Paul Julius Kühn, Cedric Spengler, Michael Weinmann 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06982.pdf)

**💡 相关性分析**

满足标准2：论文提出并评估了基于预对齐多模态编码器的形状检索框架，并引入了改进的损失函数。虽然应用领域是3D形状检索，但其核心技术——预训练的多模态表示学习、共享嵌入空间构建、以及难样本对比学习——是构建化学多模态大模型（如关联分子结构图、质谱图、文本描述）的关键组成部分。该工作为化学信息学中开发类似的多模态检索或关联系统提供了可借鉴的架构和训练方法。

**📖 中文摘要**

本文研究了基于图像的形状检索任务，提出使用经过预对齐的图像-点云编码器（如ULIP、OpenShape）进行零样本和标准IBSR。该方法将图像和点云嵌入到一个共享的表示空间中，并通过紧凑的单嵌入形状描述符进行相似性搜索来实现检索。这种表述避免了视图合成，并自然支持零样本和跨域检索。此外，论文还引入了多模态难对比损失来进一步提高检索性能。评估表明，该方法在多个数据集上实现了最先进的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Image-based shape retrieval (IBSR) aims to retrieve 3D models from a database given a query image, hence addressing a classical task in computer vision, computer graphics, and robotics. Recent approaches typically rely on bridging the domain gap between 2D images and 3D shapes based on the use of multi-view renderings as well as task-specific metric learning to embed shapes and images into a common latent space. In contrast, we address IBSR through large-scale multi-modal pretraining and show that explicit view-based supervision is not required. Inspired by pre-aligned image--point-cloud encoders from ULIP and OpenShape that have been used for tasks such as 3D shape classification, we propose the use of pre-aligned image and shape encoders for zero-shot and standard IBSR by embedding images and point clouds into a shared representation space and performing retrieval via similarity search over compact single-embedding shape descriptors. This formulation allows skipping view synthesis and naturally enables zero-shot and cross-domain retrieval without retraining on the target database. We evaluate pre-aligned encoders in both zero-shot and supervised IBSR settings and additionally introduce a multi-modal hard contrastive loss (HCL) to further increase retrieval performance. Our evaluation demonstrates state-of-the-art performance, outperforming related methods on $Acc_{Top1}$ and $Acc_{Top10}$ for shape retrieval across multiple datasets, with best results observed for OpenShape combined with Point-BERT. Furthermore, training on our proposed multi-modal HCL yields dataset-dependent gains in standard instance retrieval tasks on shape-centric data, underscoring the value of pretraining and hard contrastive learning for 3D shape retrieval. The code will be made available via the project website.

</details>

---

### 14. [Adaptive Discovery of Interpretable Audio Attributes with Multimodal LLMs for Low-Resource Classification](https://arxiv.org/abs/2603.06991)

**基本信息**

- 🔗 arXiv: [`2603.06991`](https://arxiv.org/abs/2603.06991)
- 👥 作者: Kosuke Yoshimura, Hisashi Kashima
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06991.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用多模态大语言模型（MLLM）来自动发现数据中的可解释属性，并用于构建分类器。这直接关联到“化学大模型”的一个关键应用方向：让大模型自动从化学数据（如分子、光谱）中识别和定义有化学意义的、可解释的特征或描述符，从而辅助下游的分类、回归或推理任务。该工作为化学领域实现类似的功能提供了方法参考。

**📖 中文摘要**

本文提出了一种使用多模态大语言模型自适应发现可解释音频属性的方法，用于低资源音频分类。该方法用MLLM替代了AdaFlock框架中的人类，通过提示动态识别显著的声学特征，并构建基于属性的集成分类器。实验结果表明，该方法在多种音频任务上优于直接的MLLM预测，且整个训练在11分钟内完成，证明了其作为一种超越传统依赖人类方法的实用、自适应解决方案的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In predictive modeling for low-resource audio classification, extracting high-accuracy and interpretable attributes is critical. Particularly in high-reliability applications, interpretable audio attributes are indispensable. While human-driven attribute discovery is effective, its low throughput becomes a bottleneck. We propose a method for adaptively discovering interpretable audio attributes using Multimodal Large Language Models (MLLMs). By replacing humans in the AdaFlock framework with MLLMs, our method achieves significantly faster attribute discovery. Our method dynamically identifies salient acoustic characteristics via prompting and constructs an attribute-based ensemble classifier. Experimental results across various audio tasks demonstrate that our method outperforms direct MLLM prediction in the majority of evaluated cases. The entire training completes within 11 minutes, proving it a practical, adaptive solution that surpasses conventional human-reliant approaches.

</details>

---

### 15. [AdaGen: Learning Adaptive Policy for Image Synthesis](https://arxiv.org/abs/2603.06993)

**基本信息**

- 🔗 arXiv: [`2603.06993`](https://arxiv.org/abs/2603.06993)
- 👥 作者: Zanlin Ni, Yulin Wang, Yeguo Hua 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06993.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对迭代式生成模型，提出一个可学习的自适应调度框架，以优化生成过程的质量和效率。生成模型是“化学大模型”的重要分支，用于分子生成、反应预测等。AdaGen提出的动态调度思想可以迁移到化学生成模型中，用于优化分子构象搜索、反应路径探索等迭代过程，从而提升生成分子的质量或推理效率，属于核心主题相关的方法创新。

**📖 中文摘要**

本文提出了AdaGen，一个通用的、可学习的、样本自适应的框架，用于调度迭代图像生成过程（如MaskGIT、扩散模型）。该框架将调度问题表述为马尔可夫决策过程，由一个轻量级策略网络根据当前生成状态确定合适的参数，并通过强化学习进行训练。为了解决简单奖励设计可能被攻击的问题，提出了对抗性奖励设计来指导策略网络的训练。此外，还引入了推理时细化策略和可控的保真度-多样性权衡机制。在四种生成范式上的综合实验验证了AdaGen的优越性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in image synthesis have been propelled by powerful generative models, such as Masked Generative Transformers (MaskGIT), autoregressive models, diffusion models, and rectified flow models. A common principle behind their success is the decomposition of synthesis into multiple steps. However, this introduces a proliferation of step-specific parameters (e.g., noise level or temperature at each step). Existing approaches typically rely on manually-designed rules to manage this complexity, demanding expert knowledge and trial-and-error. Furthermore, these static schedules lack the flexibility to adapt to the unique characteristics of each sample, yielding sub-optimal performance. To address this issue, we present AdaGen, a general, learnable, and sample-adaptive framework for scheduling the iterative generation process. Specifically, we formulate the scheduling problem as a Markov Decision Process, where a lightweight policy network determines suitable parameters given the current generation state, and can be trained through reinforcement learning. Importantly, we demonstrate that simple reward designs, such as FID or pre-trained reward models, can be easily hacked and may not reliably guarantee the desired quality or diversity of generated samples. Therefore, we propose an adversarial reward design to guide the training of the policy networks. Finally, we introduce an inference-time refinement strategy and a controllable fidelity-diversity trade-off mechanism to further enhance the performance and flexibility of AdaGen. Comprehensive experiments on four generative paradigms validate the superiority of AdaGen. For example, AdaGen achieves better performance on DiT-XL with 3 times lower inference cost and improves the FID of VAR from 1.92 to 1.59 with negligible computational overhead.

</details>

---

### 16. [Large Language Model-Driven Full-Component Evolution of Adaptive Large Neighborhood Search](https://arxiv.org/abs/2603.06996)

**基本信息**

- 🔗 arXiv: [`2603.06996`](https://arxiv.org/abs/2603.06996)
- 👥 作者: Shaohua Yu, Tianyu Chen, Linyan Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06996.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型自动设计和优化元启发式算法（ALNS）的各个组件。这体现了“大模型”作为自动化算法设计工具的能力。在化学信息学中，存在大量需要优化的问题（如分子对接、合成路线规划），该工作展示的LLM驱动算法进化框架，为未来开发用于化学领域特定优化问题的“化学大模型”或自动化算法设计工具提供了前瞻性的思路和范例。

**📖 中文摘要**

本文提出了一个由大语言模型驱动的闭环进化框架，用于自动重建自适应大邻域搜索的所有组件。该框架将ALNS分解为七个关键模块（销毁、修复、算子选择等），并通过专用任务进化每个模块。结合MAP-Elites机制，框架维护一个多维精英档案，同时驱动解质量和策略多样性的进化。在TSPLIB基准测试中，进化出的算法在固定迭代和固定时间限制下均优于优化的经典ALNS基线。代码分析还揭示了进化过程中自然出现的几个反直觉但有意义的设计模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adaptive Large Neighborhood Search (ALNS) is a prominent metaheuristic and a widely adopted approach for production and logistics optimization. However, it has long relied on hand-crafted components built on expert experience, which makes development slow and costly to adapt to new problems. This paper proposes a closed-loop, large-language-model-driven evolutionary framework that decouples ALNS and automatically rebuilds all of its components. We break ALNS into seven key modules: destroy, repair, operator selection, weight update, initial solution construction, acceptance rule, and destroy-rate control, and evolve each module through a dedicated task. By incorporating the MAP-Elites mechanism, the framework maintains a multi-dimensional elite archive to simultaneously drive the evolution of solution quality and strategic diversity. On TSPLIB benchmarks, the evolved algorithms consistently outperform optimized classic ALNS baselines under both fixed-iteration and fixed-time limits. The gains are especially clear on large-scale instances, where the average optimality gap drops from 3.18% to 0.74%. Code analysis also uncovers several counterintuitive yet meaningful design patterns that emerged naturally during evolution, offering practical and theoretical insights for future ALNS design. Finally, comparisons across multiple language models highlight clear differences in their ability to support evolutionary algorithm design, helping guide model selection for real-world engineering use.

</details>

---

### 17. [AutoChecklist: Composable Pipelines for Checklist Generation and Scoring with LLM-as-a-Judge](https://arxiv.org/abs/2603.07019)

**基本信息**

- 🔗 arXiv: [`2603.07019`](https://arxiv.org/abs/2603.07019)
- 👥 作者: Karen Zhou, Chenhao Tan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07019.pdf)

**💡 相关性分析**

满足标准2：论文提出了AutoChecklist，一个用于自动化生成和评分检查表的工具库。在化学信息学和质谱分析领域，评估化学大模型或质谱解析算法的性能通常需要构建详细的评估标准（检查表）。该工具为系统化、自动化地生成和运用此类领域特定的评估标准提供了强大的框架和工具，属于数据资源/工具相关的贡献。

**📖 中文摘要**

本文介绍了AutoChecklist，一个用于基于检查表的评估和评分的开源库。它将检查表生成统一为可组合的流水线，核心是一个包含五种检查表生成抽象的分类法。一个模块化的生成器→精炼器→评分器流水线可以将任何生成器与统一的评分器连接起来。该库附带了十个实现已发表方法的内置流水线，并支持多个LLM提供商。除了Python API，该库还包括用于开箱即用评估的CLI和用于交互式探索的Web界面。验证实验证实，这些检查表方法与人类偏好和质量评级显著一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Checklists have emerged as a popular approach for interpretable and fine-grained evaluation, particularly with LLM-as-a-Judge. Beyond evaluation, these structured criteria can serve as signals for model alignment, reinforcement learning, and self-correction. To support these use cases, we present AutoChecklist, an open-source library that unifies checklist-based evaluation into composable pipelines. At its core is a taxonomy of five checklist generation abstractions, each encoding a distinct strategy for deriving evaluation criteria. A modular Generator $\rightarrow$ Refiner $\rightarrow$ Scorer pipeline connects any generator with a unified scorer, and new configurations can be registered via prompt templates alone. The library ships with ten built-in pipelines implementing published approaches and supports multiple LLM providers (OpenAI, OpenRouter, vLLM). Beyond the Python API, the library includes a CLI for off-the-shelf evaluation and a web interface for interactive exploration. Validation experiments confirm that these checklist methods significantly align with human preferences and quality ratings, and a case study on ICLR peer review rebuttals demonstrates flexible domain adaptation. AutoChecklist is publicly available at this https URL .

</details>

---

### 18. [Leveraging Large Language Models for Automated Scalable Development of Open Scientific Databases](https://arxiv.org/abs/2603.07050)

**基本信息**

- 🔗 arXiv: [`2603.07050`](https://arxiv.org/abs/2603.07050)
- 👥 作者: Nikita Gautam, Doina Caragea, Ignacio Ciampitti 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07050.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出了一个利用LLM自动化构建领域特定科学数据库的框架和工具。这直接对应于化学信息学和质谱分析中的一个核心需求：从海量科学文献和数据库中自动收集、筛选和整理化学分子、反应、谱图数据，以构建用于训练“化学大模型”或支持“质谱结构推理”的高质量数据集。该工作提供了切实可行的技术方案和工具原型。

**📖 中文摘要**

本文介绍了一个基于大语言模型的网络工具，用于自动化、可扩展地开发开放科学数据库。该工具基于一个自动化统一框架，结合了基于关键词的查询、API支持的数据检索和LLM驱动的文本分类，以构建领域特定的科学数据库。数据从多个可靠数据源和搜索引擎收集，然后使用针对每个关键词查询定制的提示查询LLM，以提取与科学查询相关的数据。该方法在农业和作物产量相关的多个领域特定任务上进行了测试，结果显示与小型专家策划数据库有90%的重叠，表明该工具可以显著减少人工工作量。该框架具有可扩展性和领域无关性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the exponential increase in online scientific literature, identifying reliable domain-specific data has become increasingly important but also very challenging. Manual data collection and filtering for domain-specific scientific literature is not only time-consuming but also labor-intensive and prone to errors and inconsistencies. To facilitate automated data collection, the paper introduces a web-based tool that leverages Large Language Models (LLMs) for automated and scalable development of open scientific databases. More specifically, the tool is based on an automated and unified framework that combines keyword-based querying, API-enabled data retrieval, and LLM-powered text classification to construct domain-specific scientific databases. Data is collected from multiple reliable data sources and search engines using a parallel querying technique to construct a combined unified dataset. The dataset is subsequently filtered using LLMs queried with prompts tailored for each keyword-based query to extract the relevant data to a scientific query of interest. The approach was tested across a set of variable keyword-based searches for different domain-specific tasks related to agriculture and crop yield. The results and analysis show 90\% overlap with small domain expert-curated databases, suggesting that the proposed tool can be used to significantly reduce manual workload. Furthermore, the proposed framework is both scalable and domain-agnostic and can be applied across diverse fields for building scalable open scientific databases.

</details>

---

### 19. [Bi-directional digital twin prototype anchoring with multi-periodicity learning for few-shot fault diagnosis](https://arxiv.org/abs/2603.07054)

**基本信息**

- 🔗 arXiv: [`2603.07054`](https://arxiv.org/abs/2603.07054)
- 👥 作者: Pengcheng Xia, Zhichao Dong, Yixiang Huang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07054.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是结合数字孪生（模拟数据生成）和元学习/少样本学习技术来解决数据稀缺下的故障诊断问题。虽然应用场景是电机故障诊断，但其方法论——利用模拟器（DT）生成数据、进行元训练、在真实数据上自适应——与化学信息学中利用计算化学模拟生成分子数据预训练大模型，再在少量实验数据上微调以进行性质预测或谱图推理的范式高度相似。该工作为化学领域类似问题的解决提供了可参考的技术路线。

**📖 中文摘要**

本文针对工业机械故障诊断中标记数据稀缺的问题，提出了一种基于数字孪生和双向原型锚定的少样本故障诊断方法。通过有限元方法构建异步电机的DT，在DT虚拟空间中进行元训练，在物理空间中进行测试时适应。提出了双向孪生域原型锚定策略和协方差引导的数据增强来提高原型估计的鲁棒性。此外，还设计了一个多周期性特征学习模块来捕获电流信号中的固有周期性特征。在多个少样本设置和三种工作条件下的实验证明了该方法在少样本故障诊断中的优越性和有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Intelligent fault diagnosis (IFD) has emerged as a powerful paradigm for ensuring the safety and reliability of industrial machinery. However, traditional IFD methods rely heavily on abundant labeled data for training, which is often difficult to obtain in practical industrial environments. Constructing a digital twin (DT) of the physical asset to obtain simulation data has therefore become a promising alternative. Nevertheless, existing DT-assisted diagnosis methods mainly transfer diagnostic knowledge through domain adaptation techniques, which still require a considerable amount of unlabeled data from the target asset. To address the challenges in few-shot scenarios where only extremely limited samples are available, a bi-directional DT prototype anchoring method with multi-periodicity learning is proposed. Specifically, a framework involving meta-training in the DT virtual space and test-time adaptation in the physical space is constructed for reliable few-shot model adaptation for the target asset. A bi-directional twin-domain prototype anchoring strategy with covariance-guided augmentation for adaptation is further developed to improve the robustness of prototype estimation. In addition, a multi-periodicity feature learning module is designed to capture the intrinsic periodic characteristics within current signals. A DT of an asynchronous motor is built based on finite element method, and experiments are conducted under multiple few-shot settings and three working conditions. Comparative and ablation studies demonstrate the superiority and effectiveness of the proposed method for few-shot fault diagnosis.

</details>

---

### 20. [Interpretable Maximum Margin Deep Anomaly Detection](https://arxiv.org/abs/2603.07073)

**基本信息**

- 🔗 arXiv: [`2603.07073`](https://arxiv.org/abs/2603.07073)
- 👥 作者: Zhiji Yang, Mei Huang, Xinyu Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07073.pdf)

**💡 相关性分析**

满足标准1：论文提出的可解释深度异常检测框架，其核心方法论（最大边际学习、端到端参数学习、内在可解释性）与构建和理解‘化学大模型’的底层技术（如模型可解释性、表示学习）直接相关。

**📖 中文摘要**

本文提出了一种可解释的最大边际深度异常检测方法（IMD-AD）。虽然论文主要关注通用异常检测，但其核心方法——利用最大边际目标来稳定训练并改进判别能力，以及证明超球面参数与网络最终层权重之间的等价性以实现端到端学习和内在可解释性——在方法论上与构建和解释化学大模型（特别是用于分类或异常检测的模型）有潜在关联。该方法提供的可解释性和可视化输出能力，对于理解化学大模型中学习到的表示或用于质谱数据的异常模式检测具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anomaly detection is a crucial machine-learning task with wide-ranging applications. Deep Support Vector Data Description (Deep SVDD) is a prominent deep one-class method, but it is vulnerable to hypersphere collapse, often relies on heuristic choices for hypersphere parameters, and provides limited interpretability. To address these issues, we propose Interpretable Maximum Margin Deep Anomaly Detection (IMD-AD), which leverages a small set of labeled anomalies and a maximum margin objective to stabilize training and improve discrimination. It is inherently resilient to hypersphere collapse. Furthermore, we prove an equivalence between hypersphere parameters and the network's final-layer weights, which allows the center and radius to be learned end-to-end as part of the model and yields intrinsic interpretability and visualizable outputs. We further develop an efficient training algorithm that jointly optimizes representation, margin, and final-layer parameters. Extensive experiments and ablation studies on image and tabular benchmarks demonstrate that IMD-AD empirically improves detection performance over several state-of-the-art baselines while providing interpretable decision diagnostics.

</details>

---

### 21. [Entropy-Aware On-Policy Distillation of Language Models](https://arxiv.org/abs/2603.07079)

**基本信息**

- 🔗 arXiv: [`2603.07079`](https://arxiv.org/abs/2603.07079)
- 👥 作者: Woogyeol Jin, Taywon Min, Yongjin Yang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07079.pdf)

**💡 相关性分析**

满足标准1：论文专注于改进大型语言模型之间的知识蒸馏技术，这是构建高效、专业化‘化学大模型’（例如，通过蒸馏获得）的关键技术路径之一。

**📖 中文摘要**

本文研究了语言模型在策略蒸馏中的知识迁移问题，重点关注教师模型分布熵值较高时反向KL散度的不稳定性，并提出了熵感知策略蒸馏方法。该方法通过平衡反向KL和正向KL目标，在保持生成多样性的同时改善对齐效果。虽然论文以通用语言模型和数学推理为背景，但其核心贡献——改进模型间知识蒸馏的稳定性和效果——对于训练专门领域的‘化学大模型’（例如，通过蒸馏大型通用科学模型来获得高效的专业模型）具有直接的方法论意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

On-policy distillation is a promising approach for transferring knowledge between language models, where a student learns from dense token-level signals along its own trajectories. This framework typically uses reverse KL divergence, encouraging the student to match the teacher's high-confidence predictions. However, we show that the mode-seeking property of reverse KL reduces generation diversity and yields unstable learning signals when the teacher distribution has high entropy. To address this, we introduce Entropy-Aware On-Policy Distillation. Our key idea is augmenting the standard reverse KL objective with forward KL when teacher entropy is high, capturing the full range of plausible outputs while retaining precise imitation elsewhere. It balances mode-seeking precision with mode-covering robustness without sacrificing on-policy training efficiency. Experiments show that our method maintains generation diversity (sustained token-level entropy) and improves student-teacher alignment (lower forward KL on high-entropy tokens). Across six math reasoning benchmarks, this yields Pass@8 accuracy gains of +1.37 for Qwen3-0.6B-Base, +2.39 for Qwen3-1.7B-Base, and +5.05 for Qwen3-4B-Base compared to baseline on-policy distillation methods. These results demonstrate that accounting for teacher uncertainty is essential for maintaining diversity and achieving effective knowledge transfer.

</details>

---

### 22. [Exploring the Reasoning Depth of Small Language Models in Software Architecture: A Multidimensional Evaluation Framework Towards Software Engineering 2.0](https://arxiv.org/abs/2603.07091)

**基本信息**

- 🔗 arXiv: [`2603.07091`](https://arxiv.org/abs/2603.07091)
- 👥 作者: Ha Vo, Nhut Tran, Khang Vo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07091.pdf)

**💡 相关性分析**

满足标准1：论文系统研究小型语言模型在复杂领域任务中的推理能力与优化方法，这直接关系到如何设计、评估和优化用于化学领域的专用‘化学大模型’，特别是考虑到计算成本和数据隐私时对较小模型的需求。

**📖 中文摘要**

本文在“软件工程2.0”背景下，评估了小型语言模型在软件架构任务中的推理深度。论文引入了评估技术合规性和语义多样性的多维框架，并对10个最先进的小型模型进行了基准测试。研究探索了参数规模、微调、少样本提示等对模型在架构决策记录生成任务上表现的影响。这项工作虽然针对软件工程，但其核心——系统性地评估和提升资源受限模型（SLMs）在复杂、结构化领域任务中的推理能力——为在化学信息学等领域开发和评估专用、高效的‘化学大模型’（尤其是参数规模较小的模型）提供了重要的评估方法论参考和实证见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the era of "Software Engineering 2.0" (SE 2.0), where intelligent agents collaborate with human engineers, Generative AI is advancing beyond code generation into Software Architecture (SA). While Large Language Models (LLMs) demonstrate superior capabilities, computational costs and data privacy concerns drive interest in Small Language Models (SLMs) with fewer than 7 billion parameters. However, the reasoning limits of these resource-constrained models remain unexplored. This study benchmarks 10 state-of-the-art SLMs on Architectural Decision Records generation, introducing a multi-dimensional framework evaluating Technical Compliance and Semantic Diversity. Our empirical results reveal a significant reasoning gap: models above the 3B-parameter threshold demonstrate robust zero-shot capabilities, while sub-2B models show the strongest BERTScore gains from Fine-Tuning, though compliance improvements are not guaranteed. Contrary to assumptions regarding context saturation, Few-Shot prompting serves as a highly effective calibration mechanism for select mid-sized models with short context windows. Furthermore, high semantic diversity in off-the-shelf small models often correlates with hallucination rather than productive exploration. These findings establish a rigorous baseline for deploying sustainable, locally hosted architectural assistants.

</details>

---

### 23. [Grounding Machine Creativity in Game Design Knowledge Representations: Empirical Probing of LLM-Based Executable Synthesis of Goal Playable Patterns under Structural Constraints](https://arxiv.org/abs/2603.07101)

**基本信息**

- 🔗 arXiv: [`2603.07101`](https://arxiv.org/abs/2603.07101)
- 👥 作者: Hugh Xuechen Liu, Kıvanç Tatar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07101.pdf)

**💡 相关性分析**

满足标准1：论文探索了大语言模型将结构化领域知识（设计模式）转化为受约束的可执行代码，这种“模式到代码”的生成范式与利用‘化学大模型’将化学规则或反应模板转化为可执行计算或结构推理任务的核心思想直接相关。

**📖 中文摘要**

本文研究了在游戏设计领域，如何利用大语言模型在满足引擎结构约束的条件下，根据目标可玩模式合成可执行的Unity代码（即游戏）。论文将可玩模式实现框架为受约束的可执行创意合成问题，并比较了不同生成管道（直接生成 vs. 基于中间表示的条件生成）的效果。这项工作展示了LLMs在将高级、结构化的领域知识（游戏设计模式）转化为具体、可执行代码方面的潜力。这种“受约束的生成”范式与‘化学大模型’的应用场景高度相关，例如，将化学反应规则或分子设计原则（作为“模式”）转化为可执行的模拟代码、合成路线或分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Creatively translating complex gameplay ideas into executable artifacts (e.g., games as Unity projects and code) remains a central challenge in computational game creativity. Gameplay design patterns provide a structured representation for describing gameplay phenomena, enabling designers to decompose high-level ideas into entities, constraints, and rule-driven dynamics. Among them, goal patterns formalize common player-objective relationships. Goal Playable Concepts (GPCs) operationalize these abstractions as playable Unity engine implementations, supporting experiential exploration and compositional gameplay design. We frame scalable playable pattern realization as a problem of constrained executable creative synthesis: generated artifacts must satisfy Unity's syntactic and architectural requirements while preserving the semantic gameplay meanings encoded in goal patterns. This dual constraint limits scalability. Therefore, we investigate whether contemporary large language models (LLMs) can perform such synthesis under engine-level structural constraints and generate Unity code (as games) structured and conditioned by goal playable patterns. Using 26 goal pattern instantiations, we compare a direct generation baseline (natural language -> C# -> Unity) with pipelines conditioned on a human-authored Unity-specific intermediate representation (IR), across three IR configurations and two open-source models (DeepSeek-Coder-V2-Lite-Instruct and Qwen2.5-Coder-7B-Instruct). Compilation success is evaluated via automated Unity replay. We propose grounding and hygiene failure modes, identifying structural and project-level grounding as primary bottlenecks.

</details>

---

### 24. [Toward Multimodal Industrial Fault Analysis: A Single-Speed Chain Conveyor Dataset with Audio and Vibration Signals](https://arxiv.org/abs/2603.07130)

**基本信息**

- 🔗 arXiv: [`2603.07130`](https://arxiv.org/abs/2603.07130)
- 👥 作者: Zhang Chen, Yucong Zhang, Xiaoxiao Miao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07130.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了一个结构化的多模态工业故障数据集，并提供了标准评估协议和基线。这为‘质谱结构推理’领域构建类似的多模态数据集（例如，结合光谱、结构、文本）提供了宝贵的范例和方法论参考。

**📖 中文摘要**

本文介绍了一个用于单速链式输送机系统的多模态工业故障分析数据集。该数据集包含音频和振动信号，覆盖正常操作和多种故障类型，并设计了用于无监督故障检测和有监督故障分类的标准评估协议。虽然应用场景是机械故障诊断，但该工作明确旨在支持通道级分析和多模态融合研究，并提供了统一的基线。对于‘质谱结构推理’研究而言，该论文提供了一个构建多模态（此处为音频和振动）工业数据集的范例，其数据收集、标注、基准测试和评估协议的设计思路，对于构建和评估用于质谱分析的多模态数据集（如结合质谱图、分子结构、文本描述）具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a multimodal industrial fault analysis dataset collected from a single-speed chain conveyor (SSCC) system, targeting system-level fault detection in production lines. The dataset consists of multimodal signals, including three audio and four vibration channels. It covers normal operation and four representative fault types under multiple speeds, loads, and both clean and realistic factory-noise conditions reproduced on-site. It is explicitly designed to support channel-wise analysis and multimodal fusion research. We establish standardized evaluation protocols for unsupervised fault detection with normal-only training and supervised fault classification with balanced dataset splits across different operating conditions and fault types. A unified channel-wise kNN baseline is provided to enable fair comparison of representation quality without task-specific training. The dataset offers a practical and extensible benchmark for robust multimodal industrial fault analysis.

</details>

---

### 25. [Improving reasoning at inference time via uncertainty minimisation](https://arxiv.org/abs/2603.07159)

**基本信息**

- 🔗 arXiv: [`2603.07159`](https://arxiv.org/abs/2603.07159)
- 👥 作者: Nicolas Legrand, Kenneth Enevoldsen, Márton Kardos 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07159.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种新的、高效的推理时优化方法，旨在提升大语言模型的推理性能和可靠性。该方法可直接应用于需要多步推理的‘化学大模型’和‘质谱结构推理’任务，以改善其输出质量。

**📖 中文摘要**

本文提出了一种基于不确定性最小化的推理时优化策略。该方法将推理过程视为不确定性最小化问题，在思维层面（而非词元层面）进行操作，通过选择使模型自确定性最大化的延续来改进推理。论文在数学推理基准上验证了该方法的有效性，并分析了自确定性动态以揭示早期决策对最终准确性的预测作用。这项工作为提升大语言模型的推理性能提供了一种高效、无需外部评估器的推理时缩放方法。这种优化推理过程的技术，对于需要复杂逻辑和步骤的‘化学大模型’（如逆合成分析、反应预测）和‘质谱结构推理’任务具有直接的应用潜力，可以帮助模型生成更可靠、更准确的推理链。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) now exhibit strong multi-step reasoning abilities, but existing inference-time scaling methods remain computationally expensive, often relying on extensive sampling or external evaluators. We propose a principled strategy that frames reasoning as uncertainty minimisation and operates at the level of individual thoughts rather than tokens. Our method selects, at each reasoning step, the continuation that maximizes the model's self-certainty, a metric computed from its internal predictive distribution. This approach achieves significant improvement with a small number of samples, relies exclusively on model-internal signals, and applies to open-ended questions as opposed to methods like majority voting. Experiments on MATH500 and GSM8K across multiple model sizes demonstrate that thought-level self-certainty maximization consistently outperforms greedy decoding and matches or exceeds self-consistency under comparable token budgets. Cross-linguistic evaluations further indicate that the method transfers robustly beyond high-resource languages. Furthermore, analysis of self-certainty dynamics reveals that correct reasoning trajectories converge early to stable paths, suggesting that early decisions, likely associated with the planning of the reasoning process, are predictive of final accuracy. Building on this result, we show that self-certainty maximisation applied to the early steps can explain most of the performance gain and provide a simple yet efficient inference-time scaling method.

</details>

---

### 26. [Retrieving Minimal and Sufficient Reasoning Subgraphs with Graph Foundation Models for Path-aware GraphRAG](https://arxiv.org/abs/2603.07179)

**基本信息**

- 🔗 arXiv: [`2603.07179`](https://arxiv.org/abs/2603.07179)
- 👥 作者: Haonan Yuan, Qingyun Sun, Junhua Shi 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07179.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个基于图基础模型的检索增强生成框架，专注于结构感知和路径感知的推理。这种方法与利用化学知识图来增强‘化学大模型’和‘质谱结构推理’任务的准确性与可解释性高度相关。

**📖 中文摘要**

本文提出了GFM-Retriever，一个用于图检索增强生成的新框架。该框架利用预训练的图基础模型作为跨领域检索器，直接响应用户查询返回一个子图，并通过信息瓶颈目标优化出一个信息充分且结构最小的“核心集”子图。最后，通过显式提取和组织关系路径作为上下文提示，支持可解释的推理。这项工作将检索视为结构性问题，并利用图基础模型进行多跳路径感知推理。对于‘化学大模型’和‘质谱结构推理’，该方法提供了利用大规模化学知识图（如反应网络、分子属性图）进行检索增强推理的新思路，能够帮助模型获取与查询相关的精确子结构信息，从而生成更准确、可解释的答案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-based retrieval-augmented generation (GraphRAG) exploits structured knowledge to support knowledge-intensive reasoning. However, most existing methods treat graphs as intermediate artifacts, and the few subgraph-based retrieval methods depend on heuristic rules coupled with domain-specific distributions. They fail in typical cold-start scenarios where data in target domains is scarce, thus yielding reasoning contexts that are either informationally incomplete or structurally redundant. In this work, we revisit retrieval from a structural perspective, and propose GFM-Retriever that directly responds to user queries with a subgraph, where a pre-trained Graph Foundation Model acts as a cross-domain Retriever for multi-hop path-aware reasoning. Building on this perspective, we repurpose a pre-trained GFM from an entity ranking function into a generalized retriever to support cross-domain retrieval. On top of the retrieved graph, we further derive a label-free subgraph selector optimized by a principled Information Bottleneck objective to identify the query-conditioned subgraph, which contains informationally sufficient and structurally minimal golden evidence in a self-contained "core set". To connect structure with generation, we explicitly extract and reorganize relational paths as in-context prompts, enabling interpretable reasoning. Extensive experiments on multi-hop question answering benchmarks demonstrate that GFM-Retriever achieves state-of-the-art performance in both retrieval quality and answer generation, while maintaining efficiency.

</details>

---

### 27. [$\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving](https://arxiv.org/abs/2603.07197)

**基本信息**

- 🔗 arXiv: [`2603.07197`](https://arxiv.org/abs/2603.07197)
- 👥 作者: Pinzheng Wang, Shuli Xu, Juntao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07197.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种新的强化学习框架，旨在教会大语言模型识别并放弃低效或错误的推理路径。这种提升模型推理稳健性和自我修正能力的方法，直接适用于对可靠性要求高的‘化学大模型’和‘质谱结构推理’任务。

**📖 中文摘要**

本文提出了Re²（带重解决的强化学习），一种用于提升大语言模型推理性能的强化学习框架。Re²让模型学会在初始思维链方向不佳或质量低下时，灵活放弃无效推理路径并重新开始求解过程，而不是始终承诺一个最终答案。该方法通过纯强化学习（无需监督微调）成功放大了模型中的“重做”行为，从而在相同训练计算预算下取得了比标准RLVR更好的性能。这种让模型具备“自我修正”和“战略放弃”能力的训练范式，对于需要高可靠性和复杂多步推理的‘化学大模型’（如合成路线设计）和‘质谱结构推理’（如从谱图推导可能结构）任务具有重要的启示意义，有助于模型避免陷入错误的推理轨迹。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement learning with verifiable rewards (RLVR) has shown promise in enhancing the reasoning performance of large language models (LLMs) by increasing test-time compute. However, even after extensive RLVR training, such models still tend to generate unnecessary and low-quality steps in their chain-of-thought (CoT), leading to inefficient overthinking and lower answer quality. We show that when the initial direction or quality of the CoT is suboptimal, the model often fails to reach the correct answer, even after generating several times more tokens than when the initial CoT is well-initialized. To this end, we introduce Reinforcement Learning with Re-solving (Re$^2$), in which LLMs learn to flexibly abandon unproductive reasoning paths and restart the solution process when necessary, rather than always committing to a final answer. Re$^2$ applies pure reinforcement learning without any preliminary supervised fine-tuning, successfully amplifying the rare redo behavior in vanilla models from only 0.5% to over 30%. This leads to substantial performance gains over standard RLVR under the same training compute budget, and also demonstrates notable improvements in test-time performance as the number of samples increases.

</details>

---

### 28. [Unlocking Data Value in Finance: A Study on Distillation and Difficulty-Aware Training](https://arxiv.org/abs/2603.07223)

**基本信息**

- 🔗 arXiv: [`2603.07223`](https://arxiv.org/abs/2603.07223)
- 👥 作者: Chuxue Cao, Honglin Lin, Zhanping Zhong 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07223.pdf)

**💡 相关性分析**

满足标准2：论文详细介绍了构建高质量、针对特定领域（金融）的微调数据集（包括思维链数据和难度感知数据）的方法论，并发布了这些数据集。这为‘化学大模型’和‘质谱结构推理’领域创建类似的高质量训练资源提供了直接的参考和可行的技术路径。

**📖 中文摘要**

本文通过一项实证研究，探讨了在金融垂直领域中，大语言模型性能与训练后数据的质量及难度/可验证性分布之间的关系。作者发布了ODA-Fin-SFT-318k和ODA-Fin-RL-12k两个高质量数据集，分别通过多阶段蒸馏验证构建了高质量的思维链监督数据，以及针对困难但可验证任务进行了采样优化。使用标准SFT和RL流程训练的模型在多个金融基准上取得了优异表现。这项工作虽然针对金融领域，但其核心贡献——通过数据工程（蒸馏、难度感知采样）来构建高质量、针对性的领域微调数据——为在‘化学信息学’和‘质谱分析’领域构建用于训练或微调专用‘化学大模型’的高质量数据集（例如，包含思维链的质谱解析数据、化学反应推理数据）提供了宝贵的方法论范例和实践经验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated strong general capabilities, yet their deployment in finance remains challenging due to dense domain-specific terminology, stringent numerical reasoning requirements, and low tolerance for factual errors. We conduct a controlled empirical study showing that in specialized vertical domains, performance is largely determined by the quality and difficulty/verifiability profile of post-training data. We introduce \textbf{ODA-Fin-SFT-318k}, constructed via multi-stage distillation and verification to produce high-quality Chain-of-Thought supervision, and \textbf{ODA-Fin-RL-12k}, curated for hard-but-verifiable tasks that balance reward precision and task diversity. Using standard SFT and RL pipelines, we show that high-quality CoT distillation establishes a robust foundation during SFT, while difficulty- and verifiability-aware sampling improves RL generalization. Evaluated on nine benchmarks spanning general financial tasks, sentiment analysis, and numerical reasoning, our ODA-Fin-RL-8B consistently surpasses open-source state-of-the-art (SOTA) financial LLMs of comparable size. We release our ODA-Fin-SFT-318k and ODA-Fin-RL-12k datasets, along with trained models to advance data-centric financial AI research.

</details>

---

### 29. [Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation](https://arxiv.org/abs/2603.07233)

**基本信息**

- 🔗 arXiv: [`2603.07233`](https://arxiv.org/abs/2603.07233)
- 👥 作者: Andrea Giuseppe Di Francesco, Andrea Rubbi, Pietro Liò
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07233.pdf)

**💡 相关性分析**

满足标准1：论文将检索增强生成框架创新性地应用于生物信息学中的基因扰动预测问题，其核心方法（领域特定嵌入、可微分检索、端到端优化）为在‘化学信息学’和‘质谱分析’中构建类似的RAG系统（例如，用于质谱图到分子结构的推理）提供了直接的技术蓝图和灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting how cells respond to genetic perturbations is fundamental to understanding gene function, disease mechanisms, and therapeutic development. While recent deep learning approaches have shown promise in modeling single-cell perturbation responses, they struggle to generalize across cell types and perturbation contexts due to limited contextual information during generation. We introduce PT-RAG (Perturbation-aware Two-stage Retrieval-Augmented Generation), a novel framework that extends Retrieval-Augmented Generation beyond traditional language-model applications to cellular biology. Unlike standard RAG systems designed for text retrieval with pre-trained LLMs, perturbation retrieval lacks established similarity metrics and requires learning what constitutes relevant context, making differentiable retrieval essential. PT-RAG addresses this through a two-stage pipeline: first, retrieving candidate perturbations $K$ using GenePT embeddings, then adaptively refining the selection through Gumbel-Softmax discrete sampling conditioned on both the cell state and the input perturbation. This cell-type-aware differentiable retrieval enables end-to-end optimization of the retrieval objective jointly with generation. On the Replogle-Nadig single-gene perturbation dataset, we demonstrate that PT-RAG outperforms both STATE and vanilla RAG under identical experimental conditions, with the strongest gains in distributional similarity metrics ($W_1$, $W_2$). Notably, vanilla RAG's dramatic failure is itself a key finding: it demonstrates that differentiable, cell-type-aware retrieval is essential in this domain, and that naive retrieval can actively harm performance. Our results establish retrieval-augmented generation as a promising paradigm for modelling cellular responses to gene perturbation. The code to reproduce our experiments is available at this https URL .

</details>

---

### 30. [Turning Time Series into Algebraic Equations: Symbolic Machine Learning for Interpretable Modeling of Chaotic Time Series](https://arxiv.org/abs/2603.07261)

**基本信息**

- 🔗 arXiv: [`2603.07261`](https://arxiv.org/abs/2603.07261)
- 👥 作者: Madhurima Panja, Grace Younes, Tanujit Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07261.pdf)

**💡 相关性分析**

满足标准1：论文致力于从复杂数据中学习可解释的符号方程，这种“白盒”建模范式与‘化学大模型’和‘质谱结构推理’中追求模型可解释性、发现潜在化学规律的目标直接相关。

**📖 中文摘要**

本文针对混沌时间序列预测的挑战，提出了两种可解释的符号预测器：符号神经预测器（SyNF）和符号树预测器（SyTF）。它们从混沌时间序列数据中学习显式的、可解释的代数方程。SyNF采用基于神经网络的方程学习架构，SyTF则基于进化符号回归直接搜索方程结构。这两种方法旨在提供透明、可解释的模型，以揭示潜在动力学。论文在多个混沌吸引子和真实世界时间序列上进行了评估。这项工作虽然聚焦时间序列，但其核心——从复杂数据中学习可解释的符号方程——与‘化学大模型’和‘质谱结构推理’的一个关键目标高度一致：即从海量化学或光谱数据中发现可解释的物理规律、经验公式或结构-性质关系。该研究为在化学领域开发可解释的符号机器学习模型提供了方法论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chaotic time series are notoriously difficult to forecast. Small uncertainties in initial conditions amplify rapidly, while strong nonlinearities and regime dependent variability constrain predictability. Although modern deep learning often delivers strong short horizon accuracy, its black box nature limits scientific insight and practical trust in settings where understanding the underlying dynamics matters. To address this gap, we propose two complementary symbolic forecasters that learn explicit, interpretable algebraic equations from chaotic time series data. Symbolic Neural Forecaster (SyNF) adapts a neural network based equation learning architecture to the forecasting setting, enabling fully differentiable discovery of compact and interpretable algebraic relations. The Symbolic Tree Forecaster (SyTF) builds on evolutionary symbolic regression to search directly over equation structures under a principled accuracy complexity trade off. We evaluate both approaches in a rolling window nowcasting setting with one step ahead forecasting using several accuracy metrics and compare against a broad suite of baselines spanning classical statistical models, tree ensembles, and modern deep learning architectures. Numerical experiments cover a benchmark of 132 low dimensional chaotic attractors and two real world chaotic time series, namely weekly dengue incidence in San Juan and the Nino 3.4 sea surface temperature index. Across datasets, symbolic forecasters achieve competitive one step ahead accuracy while providing transparent equations that reveal salient aspects of the underlying dynamics.

</details>

---

### 31. [Seeing the Context: Rich Visual Context-Aware Speech Recognition via Multimodal Reasoning](https://arxiv.org/abs/2603.07263)

**基本信息**

- 🔗 arXiv: [`2603.07263`](https://arxiv.org/abs/2603.07263)
- 👥 作者: Wenjie Tian, Mingchen Shao, Bingshen Mu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07263.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个利用思维链进行多模态（音频-视觉）推理的框架，并专注于解决模态对齐和偏差问题。这种方法论与‘质谱结构推理’这一多模态推理任务（光谱、结构、文本）的核心挑战高度相关，为解决类似问题提供了新思路。

**📖 中文摘要**

本文提出了VASR，一个用于“看到”并推理视觉上下文以改进语音识别的模型，旨在解决包含丰富视觉上下文（如说话场景、屏幕文本）的视听语音识别问题。作者构建了音频-视觉思维链（AV-CoT），通过显式的中间跨模态对齐来缓解“单模态主导”问题。此外，为了解决数据稀缺问题，论文还构建并发布了相应的数据管道和测试集。这项工作在方法论上强调了多模态推理和中间对齐的重要性。对于‘质谱结构推理’这类本质上属于多模态推理的任务（结合质谱图、分子结构、文本描述），该研究提供的多模态思维链框架和缓解模态偏差的技术，具有重要的借鉴意义，可以启发如何更好地整合光谱信号与化学先验知识进行联合推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-visual speech recognition (AVSR) is an extension of ASR that incorporates visual signals. Current AVSR approaches primarily focus on lip motion, largely overlooking rich context present in the video such as speaking scene and on-screen text. To tackle such CAVSR (AVSR including rich visual Context), we propose VASR designed to "see" and reason the visual context to improve speech recognition. Specifically, we construct an Audio-Visual Chain-of-Thought (AV-CoT) that explicitly enforces intermediate cross-modal grounding between acoustic signals and visual evidence. This evidence-driven reasoning mitigates the "single-modality dominance" problem, where models either over-rely on visual context or fail to utilize it. Besides, to address the data scarcity, we construct and release a corresponding data pipeline and test set. Experiments show that AV-CoT effectively mitigates the single-modality dominance, achieving state-of-the-art performance in CAVSR. The project is open-sourced.

</details>

---

### 32. [Towards Network-Aware Operation of Integrated Energy Systems: A Comprehensive Review](https://arxiv.org/abs/2603.07266)

**基本信息**

- 🔗 arXiv: [`2603.07266`](https://arxiv.org/abs/2603.07266)
- 👥 作者: Alessandra Parisio
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07266.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于复杂网络系统（综合能源系统）建模与优化的综述，其深入讨论的“网络感知”优化、约束处理和多尺度动力学等核心议题，为‘化学大模型’中处理类似网络结构问题（如分子图、反应网络）提供了重要的跨领域视角和方法论参考。

**📖 中文摘要**

本文对综合能源系统的网络感知运行建模、优化和控制方法进行了全面综述。IES涉及电、气、热、冷等多能源网络的互联与耦合。论文分析了现有方法在可处理性、可行性保证和可扩展性方面的局限性，并指出了包含理论保证的分布式优化和数据驱动的控制等研究方向。虽然主题是能源系统，但这项综述系统性地探讨了“网络感知”建模与优化这一核心问题。对于‘化学大模型’而言，尤其是那些涉及分子网络、反应网络或代谢网络建模的应用，理解如何对复杂网络结构进行感知、约束和优化至关重要。该综述提供的关于处理网络约束、非凸行为和保证可行性的方法论讨论，对构建能够处理化学结构网络或反应路径网络的“化学大模型”具有重要的跨领域参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrated Energy Systems (IES) are systems of interconnected electricity, gas, heating, and cooling networks, where the carriers interact and depend on one another. Beyond these core vectors, IES may also incorporate additional infrastructures, such as hydrogen, transportation and water networks, whenever sector coupling or cross-vector exchanges are relevant. Although modern cities already function as multi-energy systems, these networks are still planned and operated in isolation, which leads to inefficiencies and unused flexibility. As distributed energy resources (DERs) grow, local coupling among electricity, heating, and gas networks becomes stronger, so coordinated operation across carriers and infrastructures is essential. IES can improve efficiency, flexibility, and renewable integration, yet operation is challenging because of complex interdependencies, non-convex behaviors, and multi-scale dynamics of the energy networks. A key point that the literature often overlooks is the explicit role of network constraints and topology, which shape feasible operating regions, affect scalability, and determine how uncertainty and formal guarantees can be addressed. This review provides a first comprehensive analysis of network-aware modeling, optimization, and control methods for IES. We identify methodological limitations related to tractability, feasibility guarantees, and scalability. Building on these insights, we outline research directions that include distributed optimization with theoretical guarantees and control approaches informed by operational data. The review offers a foundation for scalable, network-aware operational frameworks for future low-carbon energy systems.

</details>

---

### 33. [AutoDataset: A Lightweight System for Continuous Dataset Discovery and Search](https://arxiv.org/abs/2603.07271)

**基本信息**

- 🔗 arXiv: [`2603.07271`](https://arxiv.org/abs/2603.07271)
- 👥 作者: Junzhe Yang, Xinghao Chen, Yunuo Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07271.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个自动化系统（AutoDataset），用于从研究论文中持续发现和索引数据集。这为化学信息学和质谱分析领域的研究人员提供了一个潜在的工具或资源，可以用于发现与“化学大模型”或“质谱结构推理”相关的新数据集。

**📖 中文摘要**

本文介绍了AutoDataset，一个用于实时数据集发现和检索的轻量级自动化系统。该系统采用“论文优先”的方法，通过持续监控arXiv来直接从新发表的研究中检测和索引数据集。其核心是一个低开销的多阶段流程：首先，一个轻量级分类器快速筛选标题和摘要，以识别发布数据集的论文；然后，解析PDF以提取数据集描述和URL；最后，使用密集语义检索器对结构化记录进行索引，以实现低延迟的自然语言搜索。该系统旨在显著减少研究人员定位新发布数据集所需的时间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The continuous expansion of task-specific datasets has become a major driver of progress in machine learning. However, discovering newly released datasets remains difficult, as existing platforms largely depend on manual curation or community submissions, leading to limited coverage and substantial delays. To address this challenge, we introduce AutoDataset, a lightweight, automated system for real-time dataset discovery and retrieval. AutoDataset adopts a paper-first approach by continuously monitoring arXiv to detect and index datasets directly from newly published research. The system operates through a low-overhead multi-stage pipeline. First, a lightweight classifier rapidly filters titles and abstracts to identify papers releasing datasets, achieving an F1 score of 0.94 with an inference latency of 11 ms. For identified papers, we parse PDFs with GROBID and apply a sentence-level extractor to extract dataset descriptions. Dataset URLs are extracted from the paper text with an automated fallback to LaTeX source analysis when needed. Finally, the structured records are indexed using a dense semantic retriever, enabling low-latency natural language search. We deploy AutoDataset as a live system that continuously ingests new papers and provides up-to-date dataset discovery. In practice, it has been shown to significantly reduce the time required for researchers to locate newly released datasets, improving dataset discovery efficiency by up to 80%.

</details>

---

### 34. [Variational Flow Maps: Make Some Noise for One-Step Conditional Generation](https://arxiv.org/abs/2603.07276)

**基本信息**

- 🔗 arXiv: [`2603.07276`](https://arxiv.org/abs/2603.07276)
- 👥 作者: Abbas Mammadov, So Takao, Bohan Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07276.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型（流映射）的条件生成框架。虽然未明确提及化学或质谱，但其核心主题“条件生成”和“学习初始噪声分布以匹配观测值”与“质谱结构推理”（即从质谱数据生成/推断分子结构）在方法论上高度相关，都属于条件生成或逆问题求解的范畴。

**📖 中文摘要**

本文提出了变分流映射（Variational Flow Maps, VFMs），这是一个用于条件采样的框架。该框架将条件生成的视角从“引导采样路径”转变为“学习合适的初始噪声”。具体来说，给定一个观测值，该框架学习一个噪声适配器模型，该模型输出一个噪声分布，使得通过流映射映射到数据空间后，生成的样本能够符合观测值和数据先验。该方法通过一个原则性的变分目标联合训练噪声适配器和流映射，改善了噪声与数据的对齐，从而实现了通过简单适配器对复杂数据后验进行采样。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow maps enable high-quality image generation in a single forward pass. However, unlike iterative diffusion models, their lack of an explicit sampling trajectory impedes incorporating external constraints for conditional generation and solving inverse problems. We put forth Variational Flow Maps, a framework for conditional sampling that shifts the perspective of conditioning from "guiding a sampling path", to that of "learning the proper initial noise". Specifically, given an observation, we seek to learn a noise adapter model that outputs a noise distribution, so that after mapping to the data space via flow map, the samples respect the observation and data prior. To this end, we develop a principled variational objective that jointly trains the noise adapter and the flow map, improving noise-data alignment, such that sampling from complex data posterior is achieved with a simple adapter. Experiments on various inverse problems show that VFMs produce well-calibrated conditional samples in a single (or few) steps. For ImageNet, VFM attains competitive fidelity while accelerating the sampling by orders of magnitude compared to alternative iterative diffusion/flow models. Code is available at this https URL

</details>

---

### 35. [LLM-FK: Multi-Agent LLM Reasoning for Foreign Key Detection in Large-Scale Complex Databases](https://arxiv.org/abs/2603.07278)

**基本信息**

- 🔗 arXiv: [`2603.07278`](https://arxiv.org/abs/2603.07278)
- 👥 作者: Zijian Tang, Ying Zhang, Sibo Cai 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07278.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用多智能体大型语言模型（LLM）进行复杂推理（外键检测）。虽然应用领域是数据库，但其核心主题“多智能体LLM推理”与“化学大模型”中可能涉及的复杂、多步骤的化学信息推理（如逆合成规划、性质预测）在方法论上具有相似性。

**📖 中文摘要**

本文提出了LLM-FK，这是第一个用于外键检测的完全自动化多智能体框架。该框架协调四个专门的智能体：分析器（Profiler）通过唯一键驱动的模式分解策略分解问题并修剪搜索空间；解释器（Interpreter）注入自增强的领域知识；精炼器（Refiner）构建紧凑的结构表示并进行多视角思维链推理；验证器（Verifier）通过整体冲突解决策略强制执行模式范围内的一致性。该框架旨在解决大规模复杂数据库中组合搜索空间爆炸、有限上下文下的模糊推理以及局部预测导致的全局不一致性等核心挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Detecting missing foreign keys (FKs) requires accurately modeling semantic dependencies across database schemas, which conventional heuristic-based methods are fundamentally limited in capturing. We propose LLM-FK, the first fully automated multi-agent framework for FK detection, designed to address three core challenges that hinder naive LLM-based solutions in large-scale complex databases: combinatorial search space explosion, ambiguous inference under limited context, and global inconsistency arising from isolated local predictions. LLM-FK coordinates four specialized agents: a Profiler that decomposes the FK detection problem into the task of validating FK candidate column pairs and prunes the search space via a unique-key-driven schema decomposition strategy; an Interpreter that injects self-augmented domain knowledge; a Refiner that constructs compact structural representations and performs multi-perspective chain-of-thought reasoning; and a Verifier that enforces schema-wide consistency through a holistic conflict resolution strategy. Experiments on five benchmark datasets demonstrate that LLM-FK consistently achieves F1-scores above 93%, surpassing existing baselines by 15% on the large-scale MusicBrainz database, while reducing the candidate search space by two to three orders of magnitude without losing true FKs and maintaining robustness under challenging conditions like missing data. These results demonstrate the effectiveness and scalability of LLM-FK in real-world databases.

</details>

---

### 36. [The Third Ambition: Artificial Intelligence and the Science of Human Behavior](https://arxiv.org/abs/2603.07329)

**基本信息**

- 🔗 arXiv: [`2603.07329`](https://arxiv.org/abs/2603.07329)
- 👥 作者: W. Russell Neuman, Chad Coleman
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07329.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于将大型语言模型（LLMs）作为科学研究工具的综述和展望性文章。它系统地讨论了LLMs作为“人类行为凝聚物”的潜力、方法论途径（如基于提示的实验、合成群体抽样）以及局限性。这为“化学大模型”的研究提供了重要的跨领域视角和讨论，涉及大模型在科学发现（包括化学）中的应用潜力、方法论和局限性。

**📖 中文摘要**

本文阐述并发展了一个新兴的研究目标：将大型语言模型（LLMs）作为研究人类行为、文化和道德推理的科学工具。论文认为，LLMs在大量人类产生的文本上训练，编码了人类如何跨社会领域进行论证、辩护、叙述和协商规范的大规模规律性。这些模型可以被理解为人类符号行为的“凝聚物”，是使集体话语模式可计算访问的压缩生成表示。论文将这一目标置于计算社会科学、内容分析、调查研究和比较历史探究的长期传统中，同时阐明了将模型输出视为证据的认识论限制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Contemporary artificial intelligence research has been organized around two dominant ambitions: productivity, which treats AI systems as tools for accelerating work and economic output, and alignment, which focuses on ensuring that increasingly capable systems behave safely and in accordance with human values. This paper articulates and develops a third, emerging ambition: the use of large language models (LLMs) as scientific instruments for studying human behavior, culture, and moral reasoning. Trained on unprecedented volumes of human-produced text, LLMs encode large-scale regularities in how people argue, justify, narrate, and negotiate norms across social domains. We argue that these models can be understood as condensates of human symbolic behavior, compressed, generative representations that render patterns of collective discourse computationally accessible. The paper situates this third ambition within long-standing traditions of computational social science, content analysis, survey research, and comparative-historical inquiry, while clarifying the epistemic limits of treating model output as evidence. We distinguish between base models and fine-tuned systems, showing how alignment interventions can systematically reshape or obscure the cultural regularities learned during pretraining, and we identify instruct-only and modular adaptation regimes as pragmatic compromises for behavioral research. We review emerging methodological approaches including prompt-based experiments, synthetic population sampling, comparative-historical modeling, and ablation studies and show how each maps onto familiar social-scientific designs while operating at unprecedented scale.

</details>

---

### 37. [Learning Concept Bottleneck Models from Mechanistic Explanations](https://arxiv.org/abs/2603.07343)

**基本信息**

- 🔗 arXiv: [`2603.07343`](https://arxiv.org/abs/2603.07343)
- 👥 作者: Antonio De Santis, Schrasing Tong, Marco Brambilla 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是概念瓶颈模型（CBMs），这是一种旨在实现事前可解释性的机器学习模型。虽然应用领域是通用图像分类，但其核心主题“可解释AI”和“从黑盒模型中提取可解释概念”与“化学大模型”的研究高度相关，因为化学领域对模型的可解释性和可靠性有极高要求（例如，理解模型做出特定分子性质预测的原因）。

**📖 中文摘要**

本文引入了机制概念瓶颈模型（Mechanistic CBM, M-CBM），这是一种新颖的CBM流程，它直接从黑盒模型自身学习的概念构建瓶颈层。这些概念通过稀疏自编码器（SAEs）提取，随后使用多模态LLM在选定的图像子集上进行命名和注释。为了进行公平比较和控制信息泄漏，论文还引入了贡献概念数（NCC），这是一个决策级稀疏性度量。在多样化数据集上的实验表明，M-CBMs在匹配的稀疏性下持续超越先前的CBMs，同时改善了概念预测并提供简洁的解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) aim for ante-hoc interpretability by learning a bottleneck layer that predicts interpretable concepts before the decision. State-of-the-art approaches typically select which concepts to learn via human specification, open knowledge graphs, prompting an LLM, or using general CLIP concepts. However, concepts defined a-priori may not have sufficient predictive power for the task or even be learnable from the available data. As a result, these CBMs often significantly trail their black-box counterpart when controlling for information leakage. To address this, we introduce a novel CBM pipeline named Mechanistic CBM (M-CBM), which builds the bottleneck directly from a black-box model's own learned concepts. These concepts are extracted via Sparse Autoencoders (SAEs) and subsequently named and annotated on a selected subset of images using a Multimodal LLM. For fair comparison and leakage control, we also introduce the Number of Contributing Concepts (NCC), a decision-level sparsity metric that extends the recently proposed NEC metric. Across diverse datasets, we show that M-CBMs consistently surpass prior CBMs at matched sparsity, while improving concept predictions and providing concise explanations. Our code is available at this https URL .

</details>

---

### 38. [Latent Generative Models with Tunable Complexity for Compressed Sensing and other Inverse Problems](https://arxiv.org/abs/2603.07357)

**基本信息**

- 🔗 arXiv: [`2603.07357`](https://arxiv.org/abs/2603.07357)
- 👥 作者: Sean Gunn, Jorio Cocola, Oliver De Candido 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07357.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是用于解决逆问题（如压缩感知、去噪）的可调复杂度生成模型。虽然未直接涉及化学或质谱，但其核心主题“生成模型作为逆问题的先验”与“质谱结构推理”（即从质谱数据这一观测值推断分子结构，这是一个典型的逆问题）在问题定义和解决方法论上高度相关。

**📖 中文摘要**

本文为扩散模型、归一化流和变分自编码器开发了可调复杂度的先验，利用嵌套丢弃（nested dropout）技术。论文表明，在包括压缩感知、修复、去噪和相位恢复等任务中，可调先验始终比固定复杂度的基线实现更低的重建误差。在线性去噪设置中，论文提供了理论分析，明确描述了最优调整参数如何依赖于噪声和模型结构。这项工作展示了可调复杂度生成先验的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have emerged as powerful priors for solving inverse problems. These models typically represent a class of natural signals using a single fixed complexity or dimensionality. This can be limiting: depending on the problem, a fixed complexity may result in high representation error if too small, or overfitting to noise if too large. We develop tunable-complexity priors for diffusion models, normalizing flows, and variational autoencoders, leveraging nested dropout. Across tasks including compressed sensing, inpainting, denoising, and phase retrieval, we show empirically that tunable priors consistently achieve lower reconstruction errors than fixed-complexity baselines. In the linear denoising setting, we provide a theoretical analysis that explicitly characterizes how the optimal tuning parameter depends on noise and model structure. This work demonstrates the potential of tunable-complexity generative priors and motivates both the development of supporting theory and their application across a wide range of inverse problems.

</details>

---

### 39. [ConfHit: Conformal Generative Design with Oracle Free Guarantees](https://arxiv.org/abs/2603.07371)

**基本信息**

- 🔗 arXiv: [`2603.07371`](https://arxiv.org/abs/2603.07371)
- 👥 作者: Siddhartha Laghuvarapu, Ying Jin, Jimeng Sun
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07371.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为生成模型（特别是在药物发现中）提供统计保证的框架。其核心主题“生成设计”和“提供统计有效性保证”与“化学大模型”在药物发现和分子生成中的应用场景直接相关，旨在解决该领域中对生成候选物可靠性的关键需求。

**📖 中文摘要**

本文介绍了ConfHit，一个用于生成设计的无分布框架，可在预算约束、缺乏实验验证（oracle）和分布偏移的条件下提供有效性保证。ConfHit形式化了两个核心问题：（i）认证：是否能在用户指定的置信水平下保证生成的一批候选物中包含至少一个“命中”（hit）；（ii）设计：生成过程是否能被精炼到一个紧凑的集合而不削弱这一保证。ConfHit利用历史样本和生成样本之间的加权可交换性来消除对实验验证的需求，构建多样本密度比加权保形p值来量化对命中的统计置信度，并提出一种嵌套测试程序来认证和精炼多个生成样本的候选集，同时保持统计保证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of deep generative models in scientific discovery requires not only the ability to generate novel candidates but also reliable guarantees that these candidates indeed satisfy desired properties. Recent conformal-prediction methods offer a path to such guarantees, but its application to generative modeling in drug discovery is limited by budget constraints, lack of oracle access, and distribution shift. To this end, we introduce ConfHit, a distribution-free framework that provides validity guarantees under these conditions. ConfHit formalizes two central questions: (i) Certification: whether a generated batch can be guaranteed to contain at least one hit with a user-specified confidence level, and (ii) Design: whether the generation can be refined to a compact set without weakening this guarantee. ConfHit leverages weighted exchangeability between historical and generated samples to eliminate the need for an experimental oracle, constructs multiple-sample density-ratio weighted conformal p-value to quantify statistical confidence in hits, and proposes a nested testing procedure to certify and refine candidate sets of multiple generated samples while maintaining statistical guarantees. Across representative generative molecule design tasks and a broad range of methods, ConfHit consistently delivers valid coverage guarantees at multiple confidence levels while maintaining compact certified sets, establishing a principled and reliable framework for generative modeling.

</details>

---

### 40. [SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions](https://arxiv.org/abs/2603.07379)

**基本信息**

- 🔗 arXiv: [`2603.07379`](https://arxiv.org/abs/2603.07379)
- 👥 作者: Saroj Mishra, Suman Niroula, Umesh Yadav 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07379.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于智能体化检索增强生成（Agentic RAG）的系统性综述（SoK）。它提供了对该领域的统一框架、分类、评估和风险的全面分析。这对于“化学大模型”的研究具有重要参考价值，因为RAG是增强大模型在专业领域（如化学）知识并减少幻觉的关键技术，而智能体化则可能用于构建复杂的化学信息推理管道。

**📖 中文摘要**

本文对智能体化检索增强生成（Agentic RAG）进行了系统化知识梳理（SoK）。论文将智能体化检索-生成循环形式化为有限范围部分可观测马尔可夫决策过程，明确建模其控制策略和状态转移。在此基础上，开发了一个全面的分类法和模块化架构分解，按规划机制、检索编排、记忆范式和工具调用行为对系统进行分类。论文进一步分析了传统静态评估实践的关键局限性，并识别了自主循环固有的严重系统性风险。最后，论文概述了关键的研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies. Despite rapid industrial adoption, current research lacks a systematic understanding of Agentic RAG as a sequential decision-making system, leading to highly fragmented architectures, inconsistent evaluation methodologies, and unresolved reliability risks. This Systematization of Knowledge (SoK) paper provides the first unified framework for understanding these autonomous systems. We formalize agentic retrieval-generation loops as finite-horizon partially observable Markov decision processes, explicitly modeling their control policies and state transitions. Building upon this formalization, we develop a comprehensive taxonomy and modular architectural decomposition that categorizes systems by their planning mechanisms, retrieval orchestration, memory paradigms, and tool-invocation behaviors. We further analyze the critical limitations of traditional static evaluation practices and identify severe systemic risks inherent to autonomous loops, including compounding hallucination propagation, memory poisoning, retrieval misalignment, and cascading tool-execution vulnerabilities. Finally, we outline key doctoral-scale research directions spanning stable adaptive retrieval, cost-aware orchestration, formal trajectory evaluation, and oversight mechanisms, providing a definitive roadmap for building reliable, controllable, and scalable agentic retrieval systems.

</details>

---

### 41. [Can Large Language Models Keep Up? Benchmarking Online Adaptation to Continual Knowledge Streams](https://arxiv.org/abs/2603.07392)

**基本信息**

- 🔗 arXiv: [`2603.07392`](https://arxiv.org/abs/2603.07392)
- 👥 作者: Jiyeon Kim, Hyunji Lee, Dylan Zhou 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07392.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于评估LLMs在线适应能力的基准（OAKS），其中包含动态变化知识的数据集。这为“化学大模型”的研究提供了一个潜在的数据资源或评估框架，用于测试模型在化学知识不断更新（如新反应、新分子发现）的环境下的适应和推理能力。

**📖 中文摘要**

本文引入了面向持续知识流的在线适应基准（OAKS），用于评估大型语言模型（LLMs）在流式、持续更新知识环境下的在线适应能力。该基准被构建为一系列细粒度的上下文块序列，其中事实随时间间隔动态变化。OAKS包含两个数据集：OAKS-BABI和OAKS-Novel，其中单个事实在多个上下文块中多次演变。这些数据集包含密集的注释，以衡量模型是否准确跟踪变化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLMs operating in dynamic real-world contexts often encounter knowledge that evolves continuously or emerges incrementally. To remain accurate and effective, models must adapt to newly arriving information on the fly. We introduce Online Adaptation to Continual Knowledge Streams(OAKS) to evaluate this capability, establishing a benchmark for online adaptation over streaming, continually updating knowledge. Specifically, the benchmark is structured as a sequence of fine-grained context chunks where facts change dynamically across time intervals. OAKS comprises two datasets: OAKS-BABI and OAKS-Novel, where individual facts evolve multiple times across context chunks. These datasets include dense annotations to measure whether models track changes accurately. Evaluating 14 models with varied inference approaches, we observe significant limitations in current methodologies. Both state-of-the-art models and agentic memory systems fail to adapt robustly on OAKS, demonstrating delays in state-tracking and susceptibility to distraction within streaming environments.

</details>

---

### 42. [VIVECaption: A Split Approach to Caption Quality Improvement](https://arxiv.org/abs/2603.07401)

**基本信息**

- 🔗 arXiv: [`2603.07401`](https://arxiv.org/abs/2603.07401)
- 👥 作者: Varun Ananth, Baqiao Liu, Haoran Cai
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07401.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种改进图像描述质量的方法论和流程，并可能涉及创建高质量的数据集。这对于“化学大模型”和“质谱结构推理”具有重要意义，因为高质量的、结构化的图像-描述对（例如，化学结构图与SMILES描述，或质谱图与分子描述）是训练多模态化学模型或进行质谱解释的关键数据资源。

**📖 中文摘要**

本文介绍了VIVECaption，一个系统性的双管齐下的图像描述质量改进方法。论文首先建立了一个全面的描述评估指标分类法，区分“通用”和“实例 grounded”指标。然后描述了双管齐下的方法：（1）使用分层抽样的金标准数据集创建方法；（2）包含上下文对齐和使用SFT进行参数级微调的模型对齐策略。论文展示了在开源模型上的方法论，专注于支持更好解析和下游利用的结构化描述格式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Caption quality has emerged as a critical bottleneck in training high-quality text-to-image (T2I) and text-to-video (T2V) generative models. While visual language models (VLMs) are commonly deployed to generate captions from visual data, they suffer from hallucinations, poor compositional reasoning, and limited fine-grained understanding, resulting in misaligned image-caption pairs that degrade downstream model performance. This technical report introduces VIVECaption, a systematic two-sided approach to caption quality improvement. We first establish a comprehensive taxonomy of caption evaluation metrics, distinguishing between "universal" and "instance-grounded" metrics, with the ultimate goal of showcasing the use-cases and tradeoffs between different caption quality metrics. We then use this language to describe our two-sided approach to caption quality improvement: (1) a gold-standard dataset creation methodology using stratified sampling and (2) a model alignment strategy encompassing context alignment and parameter-level finetuning using SFT. We demonstrate our methodology on open-source models, focusing on structured caption formats that enable better parsing and downstream utilization. We ultimately show that using a finetuned character detection model in an image captioning pipeline significantly improves holistic image-caption alignment quality. Our work addresses the growing need for high-quality "vegan" training data in enterprise AI development, providing practical solutions for teams seeking to improve caption-image alignment without relying on potentially copyright-protected web-scraped content.

</details>

---

### 43. [Prompt-Based Caption Generation for Single-Tooth Dental Images Using Vision-Language Models](https://arxiv.org/abs/2603.07403)

**基本信息**

- 🔗 arXiv: [`2603.07403`](https://arxiv.org/abs/2603.07403)
- 👥 作者: Anastasiia Sukhanova, Aiden Taylor, Julian Myers 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07403.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用视觉语言模型（VLMs）为专业领域（牙科）图像生成描述。虽然领域不同，但其核心主题“使用VLM为科学/医学图像生成结构化描述”与“质谱结构推理”（将质谱图转换为分子描述）和“化学大模型”（处理化学图像与文本）在任务形式上高度相似，都属于跨模态理解和生成。

**📖 中文摘要**

本文旨在通过评估使用视觉语言模型（VLMs）为牙科图像生成描述的可能性和范围，来填补单颗牙齿图像带牙科描述数据集的空白。研究结果表明，引导性提示有助于VLMs生成有意义的描述。论文展示，其框架生成的提示能更好地锚定在描述牙科图像的视觉方面。这项工作选择了RGB图像，因为它们在消费场景中具有更大的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital dentistry has made significant advances with the advent of deep learning. However, the majority of these deep learning-based dental image analysis models focus on very specific tasks such as tooth segmentation, tooth detection, cavity detection, and gingivitis classification. There is a lack of a specialized model that has holistic knowledge of teeth and can perform dental image analysis tasks based on that knowledge. Datasets of dental images with captions can help build such a model. To the best of our knowledge, existing dental image datasets with captions are few in number and limited in scope. In many of these datasets, the captions describe the entire mouth, while the images are limited to the anterior view. As a result, posterior teeth such as molars are not clearly visible, limiting the usefulness of the captions for training vision-language models. Additionally, the captions focus only on a specific disease (gingivitis) and do not provide a holistic assessment of each tooth. Moreover, tooth disease scores are typically assigned to individual teeth, and each tooth is treated as a separate entity in orthodontic procedures. Therefore, it is important to have captions for single-tooth images. As far as we know, no such dataset of single-tooth images with dental captions exists. In this work, we aim to bridge that gap by assessing the possibility of generating captions for dental images using Vision-Language Models (VLMs) and evaluating the extent and quality of those captions. Our findings suggest that guided prompts help VLMs generate meaningful captions. We show that the prompts generated by our framework are better anchored in describing the visual aspects of dental images. We selected RGB images as they have greater potential in consumer scenarios.

</details>

---

### 44. [Context Channel Capacity: An Information-Theoretic Framework for Understanding Catastrophic Forgetting](https://arxiv.org/abs/2603.07415)

**基本信息**

- 🔗 arXiv: [`2603.07415`](https://arxiv.org/abs/2603.07415)
- 👥 作者: Ran Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从信息论角度理解持续学习（Catastrophic Forgetting）的机制，并提出了一个理论框架。虽然不特定于化学，但其核心主题“持续学习”和“架构设计”对于“化学大模型”至关重要，因为化学大模型需要不断学习新反应、新分子或新性质而不遗忘旧知识，该研究为此提供了理论基础和设计原则。

**📖 中文摘要**

本文引入了上下文信道容量（C_ctx），即持续学习（CL）架构的上下文信号与其生成参数之间的互信息，并证明零遗忘要求 C_ctx ≥ H(T)，其中 H(T) 是任务身份熵。论文建立了一个“不可能三角”——零遗忘、在线学习和有限参数无法被基于顺序状态的学习者同时满足——并表明条件再生架构（超网络）通过将参数重新定义为函数值而非状态来绕过这个三角。该框架在 Split-MNIST 上通过 8 种 CL 方法（1,130+ 实验）得到验证，显示 C_ctx 完美预测遗忘行为。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Catastrophic forgetting remains a central challenge in continual learning (CL), yet lacks a unified information-theoretic explanation for why some architectures forget catastrophically while others do not. We introduce \emph{Context Channel Capacity} ($C_\mathrm{ctx}$), the mutual information between a CL architecture's context signal and its generated parameters, and prove that zero forgetting requires $C_\mathrm{ctx} \geq H(T)$, where $H(T)$ is the task identity entropy. We establish an \emph{Impossibility Triangle} -- zero forgetting, online learning, and finite parameters cannot be simultaneously satisfied by sequential state-based learners -- and show that conditional regeneration architectures (HyperNetworks) bypass this triangle by redefining parameters as function values rather than states. We validate this framework across 8 CL methods on Split-MNIST (1,130+ experiments over 86 days, 4 seeds each), showing that $C_\mathrm{ctx}$ perfectly predicts forgetting behavior: methods with $C_\mathrm{ctx} = 0$ (NaiveSGD, EWC, SI, LwF, CFlow) exhibit catastrophic forgetting (6--97\%), while methods with $C_\mathrm{ctx} \approx 1$ (HyperNetwork) achieve zero forgetting (98.8\% ACC). We further propose \emph{Wrong-Context Probing} (P5), a practical diagnostic protocol for measuring $C_\mathrm{ctx}$, and extend the framework to CIFAR-10 via a novel \emph{Gradient Context Encoder} that closes the oracle gap from 23.3pp to 0.7pp. A systematic taxonomy of 15+ closed research directions -- including the Hebbian null result (frozen random features outperform learned features), CFlow's $\theta_0$-memorizer phenomenon, and the $S_N$ symmetry barrier to column specialization -- provides the community with precisely diagnosed negative results. Our central design principle: \emph{architecture over algorithm} -- the context pathway must be structurally unbypassable.

</details>

---

### 45. [Disentangled Textual Priors for Diffusion-based Image Super-Resolution](https://arxiv.org/abs/2603.07430)

**基本信息**

- 🔗 arXiv: [`2603.07430`](https://arxiv.org/abs/2603.07430)
- 👥 作者: Lei Jiang, Xin Liu, Xinze Tong 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07430.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模数据集DisText-SR，其中包含具有解耦的全局、低频和高频描述的图像-文本对。虽然应用于超分辨率，但这种具有细粒度、结构化文本描述的多模态数据集构建方法，可以为“化学大模型”或“质谱结构推理”中创建类似的数据资源（例如，分子图/质谱图与分层描述的配对）提供参考和启发。

**📖 中文摘要**

本文提出了DTPSR，一种新颖的基于扩散的超分辨率框架，该框架引入了沿两个互补维度解耦的文本先验：空间层次（全局与局部）和频率语义（低频与高频）。通过显式分离这些先验，DTPSR使模型能够同时捕获场景级结构和对象特定细节，并具有频率感知的语义指导。为了支持这一范式，论文构建了DisText-SR，一个包含约95,000个图像-文本对的大规模数据集，其中包含精心解耦的全局、低频和高频描述。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Image Super-Resolution (SR) aims to reconstruct high-resolution images from degraded low-resolution inputs. While diffusion-based SR methods offer powerful generative capabilities, their performance heavily depends on how semantic priors are structured and integrated into the generation process. Existing approaches often rely on entangled or coarse-grained priors that mix global layout with local details, or conflate structural and textural cues, thereby limiting semantic controllability and interpretability. In this work, we propose DTPSR, a novel diffusion-based SR framework that introduces disentangled textual priors along two complementary dimensions: spatial hierarchy (global vs. local) and frequency semantics (low- vs. high-frequency). By explicitly separating these priors, DTPSR enables the model to simultaneously capture scene-level structure and object-specific details with frequency-aware semantic guidance. The corresponding embeddings are injected via specialized cross-attention modules, forming a progressive generation pipeline that reflects the semantic granularity of visual content, from global layout to fine-grained textures. To support this paradigm, we construct DisText-SR, a large-scale dataset containing approximately 95,000 image-text pairs with carefully disentangled global, low-frequency, and high-frequency descriptions. To further enhance controllability and consistency, we adopt a multi-branch classifier-free guidance strategy with frequency-aware negative prompts to suppress hallucinations and semantic drift. Extensive experiments on synthetic and real-world benchmarks show that DTPSR achieves high perceptual quality, competitive fidelity, and strong generalization across diverse degradation scenarios.

</details>

---

### 46. [OrthoFormer: Instrumental Variable Estimation in Transformer Hidden States via Neural Control Functions](https://arxiv.org/abs/2603.07431)

**基本信息**

- 🔗 arXiv: [`2603.07431`](https://arxiv.org/abs/2603.07431)
- 👥 作者: Charles Luo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07431.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建具有因果推理能力的Transformer架构（OrthoFormer）。其核心主题“因果序列建模”与“化学大模型”和“质谱结构推理”高度相关，因为化学研究（如反应预测、性质-结构关系）和质谱解析本质上是探索变量间的因果关系，而不仅仅是相关性。该研究为构建更可靠、可解释的化学AI模型提供了新的架构思路。

**📖 中文摘要**

本文提出了OrthoFormer，一种将工具变量估计通过神经控制函数直接嵌入Transformer块中的因果基础架构。该框架基于四个理论支柱：结构方向性、表示正交性、因果稀疏性和端到端一致性。论文证明，对于任何有效的工具变量滞后，OrthoFormer实现的偏差严格小于OLS，且残差偏差以O(ρ^k)几何衰减。OrthoFormer代表了从相关序列建模到因果序列建模的范式转变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transformer architectures excel at sequential modeling yet remain fundamentally limited by correlational learning - they capture spurious associations induced by latent confounders rather than invariant causal mechanisms. We identify this as an epistemological challenge: standard Transformers conflate static background factors (intrinsic identity, style, context) with dynamic causal flows (state evolution, mechanism), leading to catastrophic out-of-distribution failure. We propose OrthoFormer, a causally grounded architecture that embeds instrumental variable estimation directly into Transformer blocks via neural control functions. Our framework rests on four theoretical pillars: Structural Directionality (time-arrow enforcement), Representation Orthogonality (latent-noise separation), Causal Sparsity (Markov Blanket approximation), and End-to-End Consistency (gradient- detached stage separation). We prove that OrthoFormer achieves bias strictly less than OLS for any valid instrument lag, with residual bias decaying geometrically as O(\r{ho}k ). We characterize the bias-variance-exogeneity trilemma inherent in self-instrumenting and identify the neural forbidden regression - where removing gradient detachment improves prediction loss while destroying causal validity. Experiments confirm all theoretical predictions. OrthoFormer represents a paradigm shift from correlational to causal sequence modeling, with implications for robustness, interpretability, and reliable decision-making under distribution shift.

</details>

---

### 47. [Data Agent: Learning to Select Data via End-to-End Dynamic Optimization](https://arxiv.org/abs/2603.07433)

**基本信息**

- 🔗 arXiv: [`2603.07433`](https://arxiv.org/abs/2603.07433)
- 👥 作者: Suorong Yang, Fangjian Su, Hai Gan 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07433.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是用于加速训练的智能数据选择框架（Data Agent）。其核心主题“动态数据选择”和“顺序决策”与机器学习模型训练优化相关。虽然通用，但该方法可应用于“化学大模型”的训练过程，帮助从海量化学数据（如分子库、反应数据库）中高效选择信息量最大的样本进行训练，从而降低成本并可能提升性能。

**📖 中文摘要**

本文提出了Data Agent，一个端到端的动态数据选择框架，将数据选择表述为一个训练感知的顺序决策问题。智能体学习一个样本级的选择策略，该策略与模型优化共同进化，由一个复合奖励指导，该奖励整合了基于损失的难度和基于置信度的不确定性信号。奖励信号捕获了优化影响和信息增益的互补目标，并带有在整个训练过程中平衡这些信号的无调谐自适应加权机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dynamic Data selection aims to accelerate training by prioritizing informative samples during online training. However, existing methods typically rely on task-specific handcrafted metrics or static/snapshot-based criteria to estimate sample importance, limiting scalability across learning paradigms and making it difficult to capture the evolving utility of data throughout training. To address this challenge, we propose Data Agent, an end-to-end dynamic data selection framework that formulates data selection as a training-aware sequential decision-making problem. The agent learns a sample-wise selection policy that co-evolves with model optimization, guided by a composite reward that integrates loss-based difficulty and confidence-based uncertainty signals. The reward signals capture complementary objectives of optimization impact and information gain, together with a tuning-free adaptive weighting mechanism that balances these signals over training. Extensive experiments across a wide range of datasets and architectures demonstrate that Data Agent consistently accelerates training while preserving or improving performance, e.g., reducing costs by over 50\% on ImageNet-1k and MMLU with lossless performance. Moreover, its dataset-agnostic formulation and modular reward make it plug-and-play across tasks and scenarios, e.g., robustness to noisy datasets, highlighting its potential in real-world scenarios.

</details>

---

### 48. [Med-Evo: Test-time Self-evolution for Medical Multimodal Large Language Models](https://arxiv.org/abs/2603.07443)

**基本信息**

- 🔗 arXiv: [`2603.07443`](https://arxiv.org/abs/2603.07443)
- 👥 作者: Dunyuan Xu, Xikai Yang, Juzheng Miao 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07443.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是医学多模态大语言模型（MLLMs）的自进化（Self-evolution）框架。虽然领域是医学，但其核心主题“MLLMs的自进化”和“利用无标签数据进行模型增强”与“化学大模型”的研究高度相关。化学领域同样面临标注数据稀缺的问题，该框架为化学MLLMs利用大量未标注的化学文献、数据库或实验数据进行自我改进提供了可行的技术路径。

**📖 中文摘要**

本文提出了Med-Evo，这是第一个用于医学多模态大语言模型（MLLMs）的自进化框架，该框架利用无标签强化学习来提升模型性能，而无需额外的标注数据。该框架引入了两个关键创新：（1）特征驱动伪标签（FPL），从所有异构候选响应中识别语义质心，以在每个回合中选择伪标签；（2）硬-软奖励（HSR），将精确匹配与令牌级评估和语义相似性相结合，以提供分层奖励。在三个医学VQA基准和两个基础MLLM上的实验显示了该方法相对于SOTA方法的明显优势。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medical Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities across diverse healthcare tasks. However, current post-training strategies, such as supervised fine-tuning and reinforcement learning, heavily depend on substantial annotated data while overlooking the potential of unlabeled test data for model enhancement. This limitation becomes particularly pronounced in medical domains, where acquiring extensive labeled medical data is difficult due to the strict data sensitivity and annotation complexity. Moreover, leveraging test data poses challenges in generating reliable supervision signals from unlabeled samples and maintaining stable self-evolution. To address these limitations, we propose Med-Evo, the first self-evolution framework for medical MLLMs that utilizes label-free reinforcement learning to promote model performance without requiring additional labeled data. Our framework introduces two key innovations: $1)$ Feature-driven Pseudo Labeling (FPL) that identifies semantic centroids from all heterogeneous candidate responses to select pseudo labels in each rollout, and $2)$ Hard-Soft Reward (HSR) that combines exact match with token-level assessment and semantic similarity to provide hierarchical reward. Experiments on three medical VQA benchmarks and two base MLLMs show clear advantages of our approach over SOTA methods, with significant improvements of 10.43\% accuracy and 4.68\% recall on the SLAKE dataset using Qwen2.5-VL, showing the effectiveness of our method.

</details>

---

### 49. [Contact-Guided 3D Genome Structure Generation of E. coli via Diffusion Transformers](https://arxiv.org/abs/2603.07472)

**基本信息**

- 🔗 arXiv: [`2603.07472`](https://arxiv.org/abs/2603.07472)
- 👥 作者: Mingxin Zhang, Xiaofeng Dai, Yu Yao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07472.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用扩散Transformer模型进行3D基因组结构生成，这属于化学信息学中利用生成式AI模型（化学大模型）进行分子/生物大分子结构推理的范畴，与'化学大模型'和'质谱结构推理'（广义的结构推理）主题高度相关。

**📖 中文摘要**

本研究提出了一种条件扩散-Transformer框架，用于生成由Hi-C接触图引导的大肠杆菌三维基因组构象集合。该研究将基因组重建表述为一个条件生成建模问题，旨在采样异质性构象，使其集合平均接触与输入的Hi-C数据一致。研究构建了一个合成数据集，使用粗粒度分子动力学模拟在环状拓扑下生成染色质集合和相应的Hi-C图谱。模型在潜在扩散设置中运行，使用变分自编码器来保持每个bin的对齐并支持复制感知表示。Hi-C信息通过基于Transformer的编码器和交叉注意力注入，强制执行从Hi-C到结构的物理可解释的单向约束。模型使用流匹配目标进行稳定优化。在保留的集合上，生成的结构能够复现输入的Hi-C距离衰减和结构相关性指标，同时保持显著的构象多样性，证明了基于扩散的生成建模在集合水平3D基因组重建中的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this study, we present a conditional diffusion-transformer framework for generating ensembles of three-dimensional Escherichia coli genome conformations guided by Hi-C contact maps. Instead of producing a single deterministic structure, we formulate genome reconstruction as a conditional generative modeling problem that samples heterogeneous conformations whose ensemble-averaged contacts are consistent with the input Hi-C data. A synthetic dataset is constructed using coarse-grained molecular dynamics simulations to generate chromatin ensembles and corresponding Hi-C maps under circular topology. Our models operate in a latent diffusion setting with a variational autoencoder that preserves per-bin alignment and supports replication-aware representations. Hi-C information is injected through a transformer-based encoder and cross-attention, enforcing a physically interpretable one-way constraint from Hi-C to structure. The model is trained using a flow-matching objective for stable optimization. On held-out ensembles, generated structures reproduce the input Hi-C distance-decay and structural correlation metrics while maintaining substantial conformational diversity, demonstrating the effectiveness of diffusion-based generative modeling for ensemble-level 3D genome reconstruction.

</details>

---

### 50. [High-Fidelity Medical Shape Generation via Skeletal Latent Diffusion](https://arxiv.org/abs/2603.07504)

**基本信息**

- 🔗 arXiv: [`2603.07504`](https://arxiv.org/abs/2603.07504)
- 👥 作者: Guoqing Zhang, Jingyun Yang, Siqi Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07504.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的生成框架（骨骼潜在扩散框架）用于医学形状生成。这属于生成式AI模型（化学/生物大模型）在化学信息学和结构生物学领域的应用，与'化学大模型'主题相关。

**📖 中文摘要**

解剖形状建模是医学数据分析中的一个基本问题。然而，解剖结构的几何复杂性和拓扑可变性给精确的解剖形状生成带来了重大挑战。在这项工作中，我们提出了一个骨骼潜在扩散框架，该框架明确地结合了结构先验，以实现高效且高保真的医学形状生成。我们引入了一个形状自编码器，其中编码器通过可微分的骨架化模块捕获全局几何信息，并将局部表面特征聚合为形状潜在表示；解码器则在稀疏采样的坐标上预测相应的隐式场。新形状通过潜在空间扩散模型生成，随后进行神经隐式解码和网格提取。为了解决医学形状数据有限的问题，我们构建了一个大规模数据集《MedSDF》，包含多个解剖类别的表面点云和相应的有符号距离场。在MedSDF和血管数据集上的大量实验表明，与现有方法相比，所提出的方法在保持更高计算效率的同时，实现了卓越的重建和生成质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anatomy shape modeling is a fundamental problem in medical data analysis. However, the geometric complexity and topological variability of anatomical structures pose significant challenges to accurate anatomical shape generation. In this work, we propose a skeletal latent diffusion framework that explicitly incorporates structural priors for efficient and high-fidelity medical shape generation. We introduce a shape auto-encoder in which the encoder captures global geometric information through a differentiable skeletonization module and aggregates local surface features into shape latents, while the decoder predicts the corresponding implicit fields over sparsely sampled coordinates. New shapes are generated via a latent-space diffusion model, followed by neural implicit decoding and mesh extraction. To address the limited availability of medical shape data, we construct a large-scale dataset, \textit{MedSDF}, comprising surface point clouds and corresponding signed distance fields across multiple anatomical categories. Extensive experiments on MedSDF and vessel datasets demonstrate that the proposed method achieves superior reconstruction and generation quality while maintaining a higher computational efficiency compared with existing approaches. Code is available at: this https URL .

</details>

---

### 51. [Generative prediction of laser-induced rocket ignition with dynamic latent space representations](https://arxiv.org/abs/2603.07525)

**基本信息**

- 🔗 arXiv: [`2603.07525`](https://arxiv.org/abs/2603.07525)
- 👥 作者: Tony Zahtila, Ettore Saetta, Murray Cutforth 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07525.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合卷积自编码器和神经ODE的数据驱动代理模型，用于快速预测复杂的激光点火火箭发动机多物理场过程。这属于利用AI大模型（特别是时序和空间预测模型）解决复杂化学/物理系统模拟问题，与'化学大模型'在计算化学和过程模拟中的应用主题相关。

**📖 中文摘要**

激光点火火箭发动机的精确且可预测的尺度解析模拟非常耗时，因为该问题涉及湍流燃料-氧化剂混合动力学、激光诱导能量沉积和高速火焰生长。再加上主要由激光操作条件和目标位置构成的大设计空间，使得问题更加复杂。为了实现快速探索和不确定性量化，我们提出了一种数据驱动的代理建模方法，该方法将卷积自编码器（cAEs）与神经常微分方程（neural ODEs）相结合。将基于机器学习的代理模型应用于前沿的多物理场湍流模拟，是代理模型部署向增加现实世界复杂性范式转变的一部分。具体而言，cAE将高维流场空间压缩到低维潜在空间，然后通过神经ODE学习系统的时空动力学。一旦训练完成，该模型可以从初始条件和指定的操作输入快速生成时空预测。通过学习一个替代整个时间演化模拟的代理模型，预测一次点火试验的成本降低了几个数量级，从而允许高效地探索输入参数空间。此外，由于当前框架产生时空场预测，因此更容易评估模型输出的物理基础。这种方法标志着向激光点火火箭燃烧器的实时数字孪生迈出了重要一步，并代表了复杂系统背景下的代理建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate and predictive scale-resolving simulations of laser-ignited rocket engines are highly time-consuming because the problem includes turbulent fuel-oxidizer mixing dynamics, laser-induced energy deposition, and high-speed flame growth. This is conflated with the large design space primarily corresponding to the laser operating conditions and target location. To enable rapid exploration and uncertainty quantification, we propose a data-driven surrogate modeling approach that combines convolutional autoencoders (cAEs) with neural ordinary differential equations (neural ODEs). The present target application of an ML-based surrogate model to leading-edge multi-physics turbulence simulation is part of a paradigm shift in the deployment of surrogate models towards increasing real-world complexity. Sequentially, the cAE spatially compresses high-dimensional flow fields into a low-dimensional latent space, wherein the system's temporal dynamics are learned via neural ODEs. Once trained, the model generates fast spatiotemporal predictions from initial conditions and specified operating inputs. By learning a surrogate to replace the entirety of the time-evolving simulation, the cost of predicting an ignition trial is reduced by several orders of magnitude, allowing efficient exploration of the input parameter space. Further, as the current framework yields a spatiotemporal field prediction, appraisal of the model output's physical grounding is more tractable. This approach marks a significant step toward real-time digital twins for laser-ignited rocket combustors and represents surrogate modeling in a complex system context.

</details>

---

### 52. [Brain-WM: Brain Glioblastoma World Model](https://arxiv.org/abs/2603.07562)

**基本信息**

- 🔗 arXiv: [`2603.07562`](https://arxiv.org/abs/2603.07562)
- 👥 作者: Chenhui Wang, Boyun Zheng, Liuxin Bao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07562.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个生成式世界模型（Brain-WM），用于统一预测治疗和生成未来医学影像（MRI）。这属于生成式AI模型（化学/生物医学大模型）在药物发现和医疗化学领域的应用，与'化学大模型'主题相关。

**📖 中文摘要**

在变化治疗干预下对胶质母细胞瘤（GBM）进行精确的预后建模对于优化临床结果至关重要。虽然生成式AI在模拟GBM演变方面显示出潜力，但现有方法通常将干预视为静态条件输入而非动态决策变量。因此，它们未能捕捉肿瘤演变和治疗反应之间复杂的、相互的 interplay。为了弥补这一差距，我们提出了Brain-WM，一个开创性的脑GBM世界模型，它统一了下一步治疗预测和未来MRI生成，从而捕捉肿瘤和治疗之间的协同进化动力学。具体来说，Brain-WM将时空动力学编码到一个共享的潜在空间中，用于联合自回归治疗预测和基于流的未来MRI生成。然后，Brain-WM没有采用传统的单一框架，而是采用了一种新颖的Y形混合Transformer（MoT）架构。这种设计在结构上解耦了异构目标，成功利用了跨任务协同作用，同时防止了特征崩溃。最后，一个协同的多时间点掩码对齐目标明确地将潜在表示锚定到基于解剖学的肿瘤结构和进展感知语义上。在内部和外部多机构队列上的广泛验证证明了Brain-WM的优越性，在治疗计划中达到91.5%的准确率，在FLAIR、T1CE和T2W序列上分别达到0.8524、0.8581和0.8404的SSIM。最终，Brain-WM为优化患者医疗提供了一个强大的临床沙盒。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Precise prognostic modeling of glioblastoma (GBM) under varying treatment interventions is essential for optimizing clinical outcomes. While generative AI has shown promise in simulating GBM evolution, existing methods typically treat interventions as static conditional inputs rather than dynamic decision variables. Consequently, they fail to capture the complex, reciprocal interplay between tumor evolution and treatment response. To bridge this gap, we present Brain-WM, a pioneering brain GBM world model that unifies next-step treatment prediction and future MRI generation, thereby capturing the co-evolutionary dynamics between tumor and treatment. Specifically, Brain-WM encodes spatiotemporal dynamics into a shared latent space for joint autoregressive treatment prediction and flow-based future MRI generation. Then, instead of a conventional monolithic framework, Brain-WM adopts a novel Y-shaped Mixture-of-Transformers (MoT) architecture. This design structurally disentangles heterogeneous objectives, successfully leveraging cross-task synergies while preventing feature collapse. Finally, a synergistic multi-timepoint mask alignment objective explicitly anchors latent representations to anatomically grounded tumor structures and progression-aware semantics. Extensive validation on internal and external multi-institutional cohorts demonstrates the superiority of Brain-WM, achieving 91.5% accuracy in treatment planning and SSIMs of 0.8524, 0.8581, and 0.8404 for FLAIR, T1CE, and T2W sequences, respectively. Ultimately, Brain-WM offers a robust clinical sandbox for optimizing patient healthcare. The source code is made available at this https URL .

</details>

---

### 53. [Analysis-Driven Procedural Generation of an Engine Sound Dataset with Embedded Control Annotations](https://arxiv.org/abs/2603.07584)

**基本信息**

- 🔗 arXiv: [`2603.07584`](https://arxiv.org/abs/2603.07584)
- 👥 作者: Robin Doerfler, Lonce Wyse
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07584.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是构建并发布了一个大规模的、带有精确注释的程序化发动机声音数据集（Procedural Engine Sounds Dataset）。该数据集专为数据驱动的发动机声音分析和合成任务设计，可用于训练AI模型进行声音参数估计和生成，为相关领域的模型开发提供了重要的数据资源，与'化学大模型'（在音频化学信息学或材料声学属性建模的广义理解下）所需的数据资源主题相关。

**📖 中文摘要**

计算发动机声音建模是汽车音频行业的核心，特别是对于主动声音设计、虚拟原型制作以及新兴的数据驱动发动机声音合成方法。这些应用需要大量具有精确时间对齐的操作状态注释的标准化、干净音频录音：由于成本高、需要专门的测量设备以及不可避免的噪声污染，此类数据难以获得。我们提出了一个分析驱动的框架，用于生成具有样本精确控制注释的发动机音频。该方法通过音高自适应频谱分析从真实录音中提取谐波结构，然后驱动一个扩展的参数化谐波加噪声合成器。利用这个框架，我们生成了程序化发动机声音数据集（19小时，5,935个文件），这是一组具有样本精确RPM和扭矩注释的发动机音频信号，涵盖了广泛的操作条件、信号复杂性和谐波轮廓。与真实录音的比较验证了合成数据保留了特征谐波结构，基线实验证实了其适用于基于学习的参数估计和合成任务。该数据集公开发布，以支持发动机音色分析、控制参数估计、声学建模和神经生成网络的研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational engine sound modeling is central to the automotive audio industry, particularly for active sound design, virtual prototyping, and emerging data-driven engine sound synthesis methods. These applications require large volumes of standardized, clean audio recordings with precisely time-aligned operating-state annotations: data that is difficult to obtain due to high costs, specialized measurement equipment requirements, and inevitable noise contamination. We present an analysis-driven framework for generating engine audio with sample-accurate control annotations. The method extracts harmonic structures from real recordings through pitch-adaptive spectral analysis, which then drive an extended parametric harmonic-plus-noise synthesizer. With this framework, we generate the Procedural Engine Sounds Dataset (19 hours, 5,935 files), a set of engine audio signals with sample-accurate RPM and torque annotations, spanning a wide range of operating conditions, signal complexities, and harmonic profiles. Comparison against real recordings validates that the synthesized data preserves characteristic harmonic structures, and baseline experiments confirm its suitability for learning-based parameter estimation and synthesis tasks. The dataset is released publicly to support research on engine timbre analysis, control parameter estimation, acoustic modeling and neural generative networks.

</details>

---

### 54. [Partial Differential Equations in the Age of Machine Learning: A Critical Synthesis of Classical, Machine Learning, and Hybrid Methods](https://arxiv.org/abs/2603.07655)

**基本信息**

- 🔗 arXiv: [`2603.07655`](https://arxiv.org/abs/2603.07655)
- 👥 作者: Mohammad Nooraiepour, Jakub Wiktor Both, Teeratorn Kadeethum 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07655.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对PDE求解中机器学习方法（包括基础模型）的批判性综述，其中包含了对机器学习范式（作为大模型的一种体现）在科学计算中应用、优势、局限性与混合设计原则的重要讨论，与‘化学大模型’主题高度相关。

**📖 中文摘要**

这篇批判性综述系统性地评估了求解偏微分方程（PDE）的两种成熟范式：经典数值方法和机器学习方法。文章围绕六个基本计算挑战，构建了一个统一的评估框架。它评估了经典方法在结构保持特性、严格收敛理论和可扩展求解器设计方面的优势，并精确描述了其在处理高维和几何复杂场景时的局限性。同时，文章对机器学习方法进行了分类（根据物理知识融入的程度）并进行了同样严格的评估。文章指出，经典方法是演绎性的，而机器学习方法是归纳性的，这一认识论区别是负责任方法选择的主要标准。作者识别了两种范式之间的三种真正的互补性，并发展了混合设计的原则，包括解决经典保证何时通过混合耦合传播的“结构继承问题”框架，以及分离离散化、神经近似和耦合贡献的误差预算分解。文章还评估了包括基础模型、可微分编程、量子算法和百亿亿次协同设计在内的新兴前沿。这篇综述虽然主题广泛，但其对机器学习方法（包括基础模型）在科学计算中应用的深入、批判性讨论，为‘化学大模型’在计算化学、分子动力学模拟等领域的潜在应用和挑战提供了重要的背景和展望。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Partial differential equations (PDEs) govern physical phenomena across the full range of scientific scales, yet their computational solution remains one of the defining challenges of modern science. This critical review examines two mature but epistemologically distinct paradigms for PDE solution, classical numerical methods and machine learning approaches, through a unified evaluative framework organized around six fundamental computational challenges. Classical methods are assessed for their structure-preserving properties, rigorous convergence theory, and scalable solver design; their persistent limitations in high-dimensional and geometrically complex settings are characterized precisely. Machine learning approaches are introduced under a taxonomy organized by the degree to which physical knowledge is incorporated and subjected to the same critical evaluation applied to classical methods. Classical methods are deductive -- errors are bounded by quantities derivable from PDE structure and discretization parameters -- while machine learning methods are inductive -- accuracy depends on statistical proximity to the training distribution. This epistemological distinction is the primary criterion governing responsible method selection. We identify three genuine complementarities between the paradigms and develop principles for hybrid design, including a framework for the structure inheritance problem that addresses when classical guarantees propagate through hybrid couplings, and an error budget decomposition that separates discretization, neural approximation, and coupling contributions. We further assess emerging frontiers, including foundation models, differentiable programming, quantum algorithms, and exascale co-design, evaluating each against the structural constraints that determine whether current barriers are fundamental or contingent on engineering progress.

</details>

---

### 55. [Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)

**基本信息**

- 🔗 arXiv: [`2603.07670`](https://arxiv.org/abs/2603.07670)
- 👥 作者: Pengfei Du
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07670.pdf)

**💡 相关性分析**

满足标准3：论文是关于大语言模型智能体中记忆机制的综述，其中包含了对智能体在‘科学推理’等应用中记忆作用的讨论，这为构建用于化学问题求解（如文献分析、实验规划）的化学大模型或智能体提供了重要的技术背景和展望。

**📖 中文摘要**

本综述对现代基于大语言模型（LLM）的智能体中记忆机制的设计、实现和评估进行了结构化阐述。文章将智能体记忆形式化为一个与感知和动作紧密耦合的“写入-管理-读取”循环，并引入了一个跨越时间范围、表示基底和控制策略的三维分类法。文章深入研究了五种机制家族：上下文驻留压缩、检索增强存储、反思性自我改进、分层虚拟上下文以及策略学习的管理。在评估方面，文章追踪了从静态回忆基准测试到交织记忆与决策的多会话智能体测试的转变，分析了四个最近的基准测试，这些测试暴露了当前系统中的顽固差距。文章还调查了记忆作为差异化因素的应用领域，包括个人助手、编码智能体、开放世界游戏、科学推理和多智能体协作。这篇综述系统性地总结了智能体记忆（作为大模型能力扩展的关键组件）的前沿进展，其中对“科学推理”应用的讨论，与利用大模型进行化学问题求解（如逆合成分析、文献挖掘）的研究方向直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) agents increasingly operate in settings where a single context window is far too small to capture what has happened, what was learned, and what should not be repeated. Memory -- the ability to persist, organize, and selectively recall information across interactions -- is what turns a stateless text generator into a genuinely adaptive agent. This survey offers a structured account of how memory is designed, implemented, and evaluated in modern LLM-based agents, covering work from 2022 through early 2026. We formalize agent memory as a \emph{write--manage--read} loop tightly coupled with perception and action, then introduce a three-dimensional taxonomy spanning temporal scope, representational substrate, and control policy. Five mechanism families are examined in depth: context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, and policy-learned management. On the evaluation side, we trace the shift from static recall benchmarks to multi-session agentic tests that interleave memory with decision-making, analyzing four recent benchmarks that expose stubborn gaps in current systems. We also survey applications where memory is the differentiating factor -- personal assistants, coding agents, open-world games, scientific reasoning, and multi-agent teamwork -- and address the engineering realities of write-path filtering, contradiction handling, latency budgets, and privacy governance. The paper closes with open challenges: continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, and multimodal embodied memory.

</details>

---

### 56. [Learning Context-Adaptive Motion Priors for Masked Motion Diffusion Models with Efficient Kinematic Attention Aggregation](https://arxiv.org/abs/2603.07697)

**基本信息**

- 🔗 arXiv: [`2603.07697`](https://arxiv.org/abs/2603.07697)
- 👥 作者: Junkun Jiang, Jie Chen, Ho Yin Au 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07697.pdf)

**💡 相关性分析**

满足标准1：论文提出的掩码扩散模型框架及其‘学习上下文自适应先验’以处理不完整/噪声数据并进行重建的核心方法论，可直接应用于‘质谱结构推理’任务，即从有噪声或不完整的质谱数据中生成/推断完整的分子结构表示。

**📖 中文摘要**

该论文提出了掩码运动扩散模型（MMDM），一个基于扩散的生成式重建框架，用于在掩码自编码器架构内，利用部分可用的高质量重建数据来增强不完整或低置信度的运动数据。其设计核心是运动学注意力聚合（KAA）机制，该机制能够高效、深度、迭代地编码关节级和姿态级特征，捕获任务特定重建所需的结构和时间运动模式。论文专注于学习上下文自适应的运动先验，即由同一可重用架构提取的、专门的结构和时间特征，其中每个学习到的先验强调运动动态的不同方面，并对其对应任务特别高效。这使得架构能够在不改变其结构的情况下自适应地专业化。这种多功能性使MMDM能够高效地学习针对特定场景（如运动细化、补全和中间帧生成）的运动先验。虽然论文应用于人体运动捕捉，但其提出的“学习上下文自适应先验”的扩散模型框架，以及利用不完整/有噪声数据（类比于质谱中的噪声或不完整谱图）进行重建和补全的核心思想，为‘质谱结构推理’任务（即从有噪声、不完整的质谱数据中推断分子结构）提供了新颖且有潜力的方法论借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-based motion capture solutions often struggle with occlusions, which result in the loss of critical joint information and hinder accurate 3D motion reconstruction. Other wearable alternatives also suffer from noisy or unstable data, often requiring extensive manual cleaning and correction to achieve reliable results. To address these challenges, we introduce the Masked Motion Diffusion Model (MMDM), a diffusion-based generative reconstruction framework that enhances incomplete or low-confidence motion data using partially available high-quality reconstructions within a Masked Autoencoder architecture. Central to our design is the Kinematic Attention Aggregation (KAA) mechanism, which enables efficient, deep, and iterative encoding of both joint-level and pose-level features, capturing structural and temporal motion patterns essential for task-specific reconstruction. We focus on learning context-adaptive motion priors, specialized structural and temporal features extracted by the same reusable architecture, where each learned prior emphasizes different aspects of motion dynamics and is specifically efficient for its corresponding task. This enables the architecture to adaptively specialize without altering its structure. Such versatility allows MMDM to efficiently learn motion priors tailored to scenarios such as motion refinement, completion, and in-betweening. Extensive evaluations on public benchmarks demonstrate that MMDM achieves strong performance across diverse masking strategies and task settings. The source code is available at this https URL .

</details>

---

### 57. [Reverse Distillation: Consistently Scaling Protein Language Model Representations](https://arxiv.org/abs/2603.07710)

**基本信息**

- 🔗 arXiv: [`2603.07710`](https://arxiv.org/abs/2603.07710)
- 👥 作者: Darius Catrina, Christian Bepler, Samuel Sledzieski 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07710.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容直接围绕蛋白质语言模型（PLMs，化学大模型在生物化学领域的重要子类）的缩放难题，并提出了一种新的训练框架（反向蒸馏）来确保模型规模扩大时性能持续提升，与‘化学大模型’主题高度相关。

**📖 中文摘要**

该论文针对蛋白质语言模型（PLMs）缩放性能不佳的问题，提出了“反向蒸馏”框架。与自然语言处理中可预测的缩放定律不同，PLMs在同一家族内，模型性能会达到平台期甚至下降，中型模型的表现常常超过最大的模型。反向蒸馏将大型PLM的表示分解为由同一家族中较小模型引导的正交子空间。由此产生的嵌入具有嵌套的、俄罗斯套娃式的结构：较大模型嵌入的前k个维度恰好是较小模型的表示。这确保了较大的反向蒸馏模型始终优于较小的模型。其动机直觉是，受容量限制的较小模型优先编码广泛共享的蛋白质特征。反向蒸馏隔离了这些共享特征，并从较大模型中正交地提取额外贡献，防止两者之间的干扰。在ProteinGym基准测试中，反向蒸馏的ESM-2变体在相同嵌入维度下优于各自的基线，其中反向蒸馏的150亿参数模型实现了最强的性能。该框架可推广到任何存在缩放挑战的模型家族。蛋白质语言模型是‘化学大模型’在生物化学领域的核心代表之一。本文直接解决了PLMs缩放的核心难题，并提出了一种确保性能单调提升的新训练框架，这对于构建和优化更强大的化学领域大模型具有直接且重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unlike the predictable scaling laws in natural language processing and computer vision, protein language models (PLMs) scale poorly: for many tasks, models within the same family plateau or even decrease in performance, with mid-sized models often outperforming the largest in the family. We introduce Reverse Distillation, a principled framework that decomposes large PLM representations into orthogonal subspaces guided by smaller models of the same family. The resulting embeddings have a nested, Matryoshka-style structure: the first k dimensions of a larger model's embedding are exactly the representation from the smaller model. This ensures that larger reverse-distilled models consistently outperform smaller ones. A motivating intuition is that smaller models, constrained by capacity, preferentially encode broadly-shared protein features. Reverse distillation isolates these shared features and orthogonally extracts additional contributions from larger models, preventing interference between the two. On ProteinGym benchmarks, reverse-distilled ESM-2 variants outperform their respective baselines at the same embedding dimensionality, with the reverse-distilled 15 billion parameter model achieving the strongest performance. Our framework is generalizable to any model family where scaling challenges persist. Code and trained models are available at this https URL .

</details>

---

### 58. [DECADE: A Temporally-Consistent Unsupervised Diffusion Model for Enhanced Rb-82 Dynamic Cardiac PET Image Denoising](https://arxiv.org/abs/2603.07759)

**基本信息**

- 🔗 arXiv: [`2603.07759`](https://arxiv.org/abs/2603.07759)
- 👥 作者: Yinchi Zhou, Liang Guo, Huidong Xie 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07759.pdf)

**💡 相关性分析**

满足标准2：论文提出的无监督、时间一致性扩散模型框架（DECADE）为科学仪器数据（如质谱）的噪声去除和信号增强提供了强大的方法论和工具参考，可用于改善‘质谱结构推理’任务的数据质量。

**📖 中文摘要**

该论文提出了DECADE，一种用于增强Rb-82动态心脏PET图像去噪的无监督扩散框架。DECADE在训练和迭代采样过程中都融入了时间一致性，使用噪声帧作为指导以保持定量准确性。该方法在西门子Vision 450和Biograph Vision Quadra扫描仪获取的数据集上进行了训练和评估。在Vision 450数据集上，DECADE持续产生高质量的动态和参数图像，同时降低了噪声并保持了心肌血流量（MBF）和心肌血流储备（MFR）。在Quadra数据集上，使用15%计数图像作为输入，全计数图像作为参考，DECADE在图像质量和K1/MBF量化方面优于基于UNet和其他扩散模型。所提出的框架能够在没有配对训练数据的情况下对Rb-82动态心脏PET进行有效的无监督去噪，支持更清晰的可视化，同时保持定量完整性。虽然应用领域是医学成像，但其提出的‘无监督’、‘时间一致性’扩散模型框架，对于处理科学仪器数据（如质谱）中的噪声和信号增强问题具有重要的方法论参考价值。质谱数据同样存在噪声高、信号复杂、需要保持定量关系（如峰强度比）的特点，DECADE框架的核心思想可直接迁移，用于开发质谱数据的去噪或信号增强工具，从而为‘质谱结构推理’提供更干净、更可靠的数据输入。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Rb-82 dynamic cardiac PET imaging is widely used for the clinical diagnosis of coronary artery disease (CAD), but its short half-life results in high noise levels that degrade dynamic frame quality and parametric imaging. The lack of paired clean-noisy training data, rapid tracer kinetics, and frame-dependent noise variations further limit the effectiveness of existing deep learning denoising methods. We propose DECADE (A Temporally-Consistent Unsupervised Diffusion model for Enhanced Rb-82 CArdiac PET DEnoising), an unsupervised diffusion framework that generalizes across early- to late-phase dynamic frames. DECADE incorporates temporal consistency during both training and iterative sampling, using noisy frames as guidance to preserve quantitative accuracy. The method was trained and evaluated on datasets acquired from Siemens Vision 450 and Siemens Biograph Vision Quadra scanners. On the Vision 450 dataset, DECADE consistently produced high-quality dynamic and parametric images with reduced noise while preserving myocardial blood flow (MBF) and myocardial flow reserve (MFR). On the Quadra dataset, using 15%-count images as input and full-count images as reference, DECADE outperformed UNet-based and other diffusion models in image quality and K1/MBF quantification. The proposed framework enables effective unsupervised denoising of Rb-82 dynamic cardiac PET without paired training data, supporting clearer visualization while maintaining quantitative integrity.

</details>

---

### 59. [Using GPUs And LLMs Can Be Satisfying for Nonlinear Real Arithmetic Problems](https://arxiv.org/abs/2603.07764)

**基本信息**

- 🔗 arXiv: [`2603.07764`](https://arxiv.org/abs/2603.07764)
- 👥 作者: Christopher Brix, Julia Walczak, Nils Lommen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07764.pdf)

**💡 相关性分析**

满足标准1：论文核心研究了利用大型语言模型（LLMs）与GPU加速协同解决复杂计算问题（非线性实数算术）的方法，这种“LLM增强科学计算”的范式与探索‘化学大模型’在加速或指导计算化学任务中的应用直接相关。

**📖 中文摘要**

该论文研究了如何利用GPU和大型语言模型（LLMs）来高效解决非线性实数算术（NRA）问题。作者扩展了先前基于梯度下降的思想，将LLMs和GPU加速相结合，获得了一种高效的技术。他们在新颖的SMT求解器GANRA中实现了这些发现。作者在两个不同的NRA基准上评估了GANRA，并展示了相对于先前最先进技术的显著改进。特别是在Sturm-MBO基准上，他们能够在不到先前最先进技术运行时间的1/20内，证明多出五倍以上实例的可满足性。这项工作展示了将LLMs与专用计算硬件（GPU）结合，用于解决复杂数学问题（如NRA）的潜力。虽然问题领域是数学求解，但其“LLM + GPU加速”协同解决复杂计算问题的范式，对于‘化学大模型’在解决计算化学难题（如量子化学计算、分子动力学模拟的加速或近似）方面具有重要的启示意义。它提供了一种利用大模型指导或增强科学计算流程的可能路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Solving quantifier-free non-linear real arithmetic (NRA) problems is a computationally hard task. To tackle this problem, prior work proposed a promising approach based on gradient descent. In this work, we extend their ideas and combine LLMs and GPU acceleration to obtain an efficient technique. We have implemented our findings in the novel SMT solver GANRA (GPU Accelerated solving of Nonlinear Real Arithmetic problems). We evaluate GANRA on two different NRA benchmarks and demonstrate significant improvements over the previous state of the art. In particular, on the Sturm-MBO benchmark, we can prove satisfiability for more than five times as many instances in less than 1/20th of the previous state-of-the-art runtime.

</details>

---

### 60. [Scaling Data Difficulty: Improving Coding Models via Reinforcement Learning on Fresh and Challenging Problems](https://arxiv.org/abs/2603.07779)

**基本信息**

- 🔗 arXiv: [`2603.07779`](https://arxiv.org/abs/2603.07779)
- 👥 作者: Zongqian Li, Tengchao Lv, Shaohan Huang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07779.pdf)

**💡 相关性分析**

满足标准2：论文提出的难度感知数据筛选框架和由此构建的MicroCoder数据集，为构建用于训练‘化学大模型’的高质量、高难度化学领域数据集（如反应预测、分子设计）提供了方法论和理念上的重要参考。

**📖 中文摘要**

该论文通过系统性数据处理和难度缩放，解决了下一代代码生成模型训练所需的高质量数据集面临的挑战。作者引入了一个四阶段数据处理框架，涵盖收集、处理、过滤和验证，并集成了通过基于LLM的预测-校准-选择框架实现的自动难度过滤。该框架利用跨五个加权维度的多维难度指标，在去除简单问题的同时保留具有挑战性的问题。由此产生的MicroCoder数据集包含来自不同平台的数万个经过筛选的真实竞争性编程问题，强调新颖性和难度。在严格未见过的LiveCodeBench上的评估表明，在300个训练步骤内，MicroCoder实现了比广泛使用的、规模相当的基线数据集大3倍的性能提升，并且在GRPO及其变体训练算法下都具有一致的优势。MicroCoder数据集在不同模型大小上对中等和困难问题带来了明显的改进，在模型能力最受挑战的领域实现了高达17.2%的相对性能增益。这些结果验证了难度感知的数据筛选能够提高模型在挑战性任务上的性能。虽然应用领域是代码生成，但其提出的“难度感知数据筛选”框架和“强调挑战性问题”的数据集构建理念，对于构建用于训练‘化学大模型’的高质量、具有挑战性的化学数据集（例如，包含复杂反应、罕见分子或困难性质预测任务的数据集）具有直接的借鉴意义。高质量数据是训练强大化学大模型的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training next-generation code generation models requires high-quality datasets, yet existing datasets face difficulty imbalance, format inconsistency, and data quality problems. We address these challenges through systematic data processing and difficulty scaling. We introduce a four-stage Data Processing Framework encompassing collection, processing, filtering, and verification, incorporating Automatic Difficulty Filtering via an LLM-based predict-calibrate-select framework that leverages multi-dimensional difficulty metrics across five weighted dimensions to retain challenging problems while removing simplistic ones. The resulting MicroCoder dataset comprises tens of thousands of curated real competitive programming problems from diverse platforms, emphasizing recency and difficulty. Evaluations on strictly unseen LiveCodeBench demonstrate that MicroCoder achieves 3x larger performance gains within 300 training steps compared to widely-used baseline datasets of comparable size, with consistent advantages under both GRPO and its variant training algorithms. The MicroCoder dataset delivers obvious improvements on medium and hard problems across different model sizes, achieving up to 17.2% relative gains in overall performance where model capabilities are most stretched. These results validate that difficulty-aware data curation improves model performance on challenging tasks, providing multiple insights for dataset creation in code generation.

</details>

---

### 61. [MINT: Molecularly Informed Training with Spatial Transcriptomics Supervision for Pathology Foundation Models](https://arxiv.org/abs/2603.07895)

**基本信息**

- 🔗 arXiv: [`2603.07895`](https://arxiv.org/abs/2603.07895)
- 👥 作者: Minsoo Lee, Jonghyun Kim, Juseung Yun 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07895.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用分子数据（空间转录组学）来增强和指导基于图像的AI模型（病理学基础模型）。这直接关联到‘化学大模型’的主题，即探索如何整合化学/分子信息来构建和优化大型AI模型。

**📖 中文摘要**

这篇论文提出了一种名为MINT（分子信息训练）的微调框架，旨在将空间转录组学（ST）的监督信号整合到预训练的组织病理学视觉Transformer（ViT）中。MINT的核心创新在于，它通过添加一个可学习的ST令牌来编码转录组信息，与形态学CLS令牌分开处理，从而防止灾难性遗忘。该框架在斑点和补丁两个空间尺度上进行基因表达回归，提供了跨尺度的互补监督。在577个公开可用的HEST样本上进行训练后，MINT在基因表达预测（HEST-Bench）和通用病理学任务（EVA）上都取得了最佳性能。这项工作展示了如何利用分子数据（空间转录组学）来增强基于形态学的视觉基础模型，这与化学信息学中利用多模态数据（如质谱与结构信息）构建更强大模型的目标高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pathology foundation models learn morphological representations through self-supervised pretraining on large-scale whole-slide images, yet they do not explicitly capture the underlying molecular state of the tissue. Spatial transcriptomics technologies bridge this gap by measuring gene expression in situ, offering a natural cross-modal supervisory signal. We propose MINT (Molecularly Informed Training), a fine-tuning framework that incorporates spatial transcriptomics supervision into pretrained pathology Vision Transformers. MINT appends a learnable ST token to the ViT input to encode transcriptomic information separately from the morphological CLS token, preventing catastrophic forgetting through DINO self-distillation and explicit feature anchoring to the frozen pretrained encoder. Gene expression regression at both spot-level (Visium) and patch-level (Xenium) resolutions provides complementary supervision across spatial scales. Trained on 577 publicly available HEST samples, MINT achieves the best overall performance on both HEST-Bench for gene expression prediction (mean Pearson r = 0.440) and EVA for general pathology tasks (0.803), demonstrating that spatial transcriptomics supervision complements morphology-centric self-supervised pretraining.

</details>

---

### 62. [Beyond Heuristic Prompting: A Concept-Guided Bayesian Framework for Zero-Shot Image Recognition](https://arxiv.org/abs/2603.07911)

**基本信息**

- 🔗 arXiv: [`2603.07911`](https://arxiv.org/abs/2603.07911)
- 👥 作者: Hui Liu, Kecheng Chen, Jialiang Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07911.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（LLM）来合成和利用结构化概念，以增强视觉模型的零样本推理能力。这直接关联到‘化学大模型’的主题，即探索如何利用大语言模型来处理和理解复杂的、结构化的领域知识（如化学概念）。

**📖 中文摘要**

这篇论文针对视觉语言模型（VLM）在零样本图像识别中的局限性，提出了一个基于贝叶斯框架的概念引导方法。作者认为，现有的提示工程方法通常是启发式的，并且难以适应目标类别。为了解决这个问题，他们将类别特定的“概念”作为潜在变量引入，将零样本预测重新构建为在概念空间上的边缘化。为了构建一个表达性强且高效的概念提议分布，他们设计了一个由大型语言模型（LLM）驱动的多阶段概念合成流程，以生成具有区分性和组合性的概念。该方法在多个零样本图像分类基准测试中取得了最先进的性能。这项工作展示了如何利用LLM生成结构化、语义丰富的概念来增强视觉模型的推理能力，这与构建能够理解和操作化学概念的“化学大模型”的研究方向高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language Models (VLMs), such as CLIP, have significantly advanced zero-shot image recognition. However, their performance remains limited by suboptimal prompt engineering and poor adaptability to target classes. While recent methods attempt to improve prompts through diverse class descriptions, they often rely on heuristic designs, lack versatility, and are vulnerable to outlier prompts. This paper enhances prompt by incorporating class-specific concepts. By treating concepts as latent variables, we rethink zero-shot image classification from a Bayesian perspective, casting prediction as marginalization over the concept space, where each concept is weighted by a prior and a test-image conditioned likelihood. This formulation underscores the importance of both a well-structured concept proposal distribution and the refinement of concept priors. To construct an expressive and efficient proposal distribution, we introduce a multi-stage concept synthesis pipeline driven by LLMs to generate discriminative and compositional concepts, followed by a Determinantal Point Process to enforce diversity. To mitigate the influence of outlier concepts, we propose a training-free, adaptive soft-trim likelihood, which attenuates their impact in a single forward pass. We further provide robustness guarantees and derive multi-class excess risk bounds for our framework. Extensive experiments demonstrate that our method consistently outperforms state-of-the-art approaches, validating its effectiveness in zero-shot image classification. Our code is available at this https URL .

</details>

---

### 63. [BRIDGE: Benchmark for multi-hop Reasoning In long multimodal Documents with Grounded Evidence](https://arxiv.org/abs/2603.07931)

**基本信息**

- 🔗 arXiv: [`2603.07931`](https://arxiv.org/abs/2603.07931)
- 👥 作者: Biao Xiang, Soyeon Caren Han, Yihao Ding
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07931.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于评估多跳推理和证据整合能力的多模态基准测试数据集（BRIDGE）。这为开发和评估能够处理复杂科学信息（类似于化学文献和质谱数据）的‘化学大模型’提供了重要的数据资源和评估工具。

**📖 中文摘要**

这篇论文介绍了BRIDGE，一个用于评估模型在长篇幅、多模态科学文档中进行多跳推理能力的基准测试。该数据集要求模型整合文本、表格和图表中的证据来回答问题，并支持链式和扇出式推理结构。与仅关注最终答案正确性的传统基准不同，BRIDGE提供了明确的、步骤级别的推理注释，允许对中间推理过程进行评估。论文通过实验揭示了当前最先进的大型语言模型（LLM）和多模态检索增强生成（RAG）系统在证据聚合和证据溯源方面存在系统性缺陷。BRIDGE为诊断模型在复杂、结构化文档中的推理失败提供了一个有针对性的测试平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-hop question answering (QA) is widely used to evaluate the reasoning capabilities of large language models, yet most benchmarks focus on final answer correctness and overlook intermediate reasoning, especially in long multimodal documents. We introduce BRIDGE, a benchmark for multi-hop reasoning over long scientific papers that require integrating evidence across text, tables, and figures. The dataset supports both chain-like and fan-out structures and provides explicit multi-hop reasoning annotations for step-level evaluation beyond answer accuracy. Experiments with state-of-the-art LLMs and multimodal retrieval-augmented generation (RAG) systems reveal systematic deficiencies in evidence aggregation and grounding that remain hidden under conventional answer-only evaluation. BRIDGE provides a targeted testbed for diagnosing reasoning failures in long multimodal documents.

</details>

---

### 64. [VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer](https://arxiv.org/abs/2603.07952)

**基本信息**

- 🔗 arXiv: [`2603.07952`](https://arxiv.org/abs/2603.07952)
- 👥 作者: Yanning Hou, Peiyuan Li, Zirui Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07952.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个无需文本分支、仅通过视觉Transformer学习“正常”与“异常”抽象概念的框架。这为构建专注于特定领域（如化学结构）表示学习的大模型提供了方法论上的参考，与‘化学大模型’中学习分子或光谱表示的研究主题相关。

**📖 中文摘要**

这篇论文提出了VisualAD，一个用于零样本异常检测（ZSAD）的纯视觉框架。与主流依赖视觉语言模型（如CLIP）和文本编码器的方法不同，VisualAD仅使用视觉Transformer（ViT）。它在冻结的主干网络中引入了两个可学习的令牌，分别直接编码“正常”和“异常”的概念。通过多层自注意力机制，这些令牌与图像块令牌交互，逐步获取高级别的正常和异常概念，同时引导图像块突出异常相关线索。此外，论文还引入了空间感知交叉注意力模块和轻量级自对齐函数来增强性能。VisualAD在涵盖工业和医学领域的13个零样本异常检测基准测试中取得了最先进的性能。这项工作探索了在不依赖跨模态对齐的情况下，如何让视觉模型学习抽象的概念表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Zero-shot anomaly detection (ZSAD) requires detecting and localizing anomalies without access to target-class anomaly samples. Mainstream methods rely on vision-language models (VLMs) such as CLIP: they build hand-crafted or learned prompt sets for normal and abnormal semantics, then compute image-text similarities for open-set discrimination. While effective, this paradigm depends on a text encoder and cross-modal alignment, which can lead to training instability and parameter redundancy. This work revisits the necessity of the text branch in ZSAD and presents VisualAD, a purely visual framework built on Vision Transformers. We introduce two learnable tokens within a frozen backbone to directly encode normality and abnormality. Through multi-layer self-attention, these tokens interact with patch tokens, gradually acquiring high-level notions of normality and anomaly while guiding patches to highlight anomaly-related cues. Additionally, we incorporate a Spatial-Aware Cross-Attention (SCA) module and a lightweight Self-Alignment Function (SAF): SCA injects fine-grained spatial information into the tokens, and SAF recalibrates patch features before anomaly scoring. VisualAD achieves state-of-the-art performance on 13 zero-shot anomaly detection benchmarks spanning industrial and medical domains, and adapts seamlessly to pretrained vision backbones such as the CLIP image encoder and DINOv2. Code: this https URL

</details>

---

### 65. [SGG-R$^{\rm 3}$: From Next-Token Prediction to End-to-End Unbiased Scene Graph Generation](https://arxiv.org/abs/2603.07961)

**基本信息**

- 🔗 arXiv: [`2603.07961`](https://arxiv.org/abs/2603.07961)
- 👥 作者: Jiaye Feng, Qixiang Yin, Yuankun Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07961.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个结合大语言模型（用于关系增强和思维链引导）和强化学习的结构化框架，以优化场景图生成任务。这直接关联到‘化学大模型’的主题，即探索如何利用大语言模型来增强和指导复杂结构化预测任务（如分子属性预测或质谱解析）的模型训练。

**📖 中文摘要**

这篇论文提出了SGG-R^3，一个用于端到端无偏场景图生成的结构化推理框架。该框架集成了任务特定的思维链引导的监督微调和基于组序列策略优化的强化学习。为了解决关系稀疏性和长尾分布问题，作者在监督微调阶段利用多模态大语言模型进行关系增强，并在强化学习阶段提出了一个新颖的双粒度奖励机制。该奖励机制通过基于频率的自适应权重来缓解长尾问题，并通过语义聚类来提高关系覆盖率。实验表明，SGG-R^3在两个基准测试上优于现有方法。这项工作展示了如何将大语言模型的生成和推理能力与特定任务的结构化训练相结合，以解决数据分布不平衡的问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scene Graph Generation (SGG) structures visual scenes as graphs of objects and their relations. While Multimodal Large Language Models (MLLMs) have advanced end-to-end SGG, current methods are hindered by both a lack of task-specific structured reasoning and the challenges of sparse, long-tailed relation distributions, resulting in incomplete scene graphs characterized by low recall and biased predictions. To address these issues, we introduce SGG-R$^{\rm 3}$, a structured reasoning framework that integrates task-specific chain-of-thought (CoT)-guided supervised fine-tuning (SFT) and reinforcement learning (RL) with group sequence policy optimization (GSPO), designed to engage in three sequential stages to achieve end-to-end unbiased scene graph generation. During the SFT phase, we propose a relation augmentation strategy by leveraging an MLLM and refined via embedding similarity filtering to alleviate relation sparsity. Subsequently, a stage-aligned reward scheme optimizes the procedural reasoning during RL. Specifically, we propose a novel dual-granularity reward which integrates fine-grained and coarse-grained relation rewards, simultaneously mitigating the long-tail issue via frequency-based adaptive weighting of predicates and improving relation coverage through semantic clustering. Experiments on two benchmarks show that SGG-R$^{\rm 3}$ achieves superior performance compared to existing methods, demonstrating the effectiveness and generalization of the framework.

</details>

---

### 66. [Structure-Preserving Graph Contrastive Learning for Mathematical Information Retrieval](https://arxiv.org/abs/2603.08012)

**基本信息**

- 🔗 arXiv: [`2603.08012`](https://arxiv.org/abs/2603.08012)
- 👥 作者: Chun-Hsi Ku, Hung-Hsuan Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08012.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于数学公式检索的图对比学习方法和变量替换增强技术，这为化学信息学中处理分子图结构、进行质谱结构推理或构建相关数据集提供了潜在的工具和方法论参考。

**📖 中文摘要**

本文提出了一种用于数学公式检索的图对比学习（GCL）方法，并引入了一种领域特定的图增强技术——变量替换。该方法旨在解决标准GCL增强技术可能扭曲数学公式语义含义的问题，特别是对于小型且高度结构化的图。变量替换技术能够保留核心代数关系和公式结构，从而提升检索性能。实验表明，这种简单的方法相比通用的增强策略能显著提高检索性能。该工作为数学信息检索提供了新的工具和方法，其提出的图增强技术和检索模型可作为化学信息学领域（特别是处理分子图或化学结构图）进行结构推理或数据增强的参考资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper introduces Variable Substitution as a domain-specific graph augmentation technique for graph contrastive learning (GCL) in the context of searching for mathematical formulas. Standard GCL augmentation techniques often distort the semantic meaning of mathematical formulas, particularly for small and highly structured graphs. Variable Substitution, on the other hand, preserves the core algebraic relationships and formula structure. To demonstrate the effectiveness of our technique, we apply it to a classic GCL-based retrieval model. Experiments show that this straightforward approach significantly improves retrieval performance compared to generic augmentation strategies. We release the code on GitHub.\footnote{ this https URL }.

</details>

---

### 67. [S2S-FDD: Bridging Industrial Time Series and Natural Language for Explainable Zero-shot Fault Diagnosis](https://arxiv.org/abs/2603.08048)

**基本信息**

- 🔗 arXiv: [`2603.08048`](https://arxiv.org/abs/2603.08048)
- 👥 作者: Baoxue Li, Chunhui Zhao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08048.pdf)

**💡 相关性分析**

满足标准1和标准2：论文核心研究内容是利用大型语言模型对复杂时序工业信号进行可解释的故障诊断和推理。这直接关联到“化学大模型”在复杂数据（如质谱数据）上的应用，以及“质谱结构推理”中所需的从信号到结构的解释性推理过程。其提出的框架和方法论可作为相关研究的参考。

**📖 中文摘要**

本文提出了一种名为S2S-FDD（信号到语义故障诊断）的框架，用于工业系统的零样本可解释故障诊断。该框架旨在弥合高维传感器信号与自然语言语义之间的鸿沟。其核心创新包括：1）设计了一个信号到语义算子，将抽象的时序信号转换为捕捉趋势、周期性和偏差的自然语言摘要；2）基于这些描述，设计了一种多轮树状结构诊断方法，通过参考历史维护文档和动态查询额外信号来执行故障诊断。该框架支持人机交互反馈以进行持续优化。实验在一个多相流过程上验证了该方法的可行性和有效性。这项工作展示了如何利用大型语言模型（LLMs）的泛化和推理能力来处理复杂的时序数据（如传感器信号），并为结果提供解释。这种将复杂数据（如质谱时序信号或分子描述符）转化为可解释语义并进行推理的框架，与“化学大模型”和“质谱结构推理”中涉及的数据处理、模型解释和知识推理高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fault diagnosis is critical for the safe operation of industrial systems. Conventional diagnosis models typically produce abstract outputs such as anomaly scores or fault categories, failing to answer critical operational questions like "Why" or "How to repair". While large language models (LLMs) offer strong generalization and reasoning abilities, their training on discrete textual corpora creates a semantic gap when processing high-dimensional, temporal industrial signals. To address this challenge, we propose a Signals-to-Semantics fault diagnosis (S2S-FDD) framework that bridges high-dimensional sensor signals with natural language semantics through two key innovations: We first design a Signal-to-Semantic operator to convert abstract time-series signals into natural language summaries, capturing trends, periodicity, and deviations. Based on the descriptions, we design a multi-turn tree-structured diagnosis method to perform fault diagnosis by referencing historical maintenance documents and dynamically querying additional signals. The framework further supports human-in-the-loop feedback for continuous refinement. Experiments on the multiphase flow process show the feasibility and effectiveness of the proposed method for explainable zero-shot fault diagnosis.

</details>

---

### 68. [Adversarial Domain Adaptation Enables Knowledge Transfer Across Heterogeneous RNA-Seq Datasets](https://arxiv.org/abs/2603.08062)

**基本信息**

- 🔗 arXiv: [`2603.08062`](https://arxiv.org/abs/2603.08062)
- 👥 作者: Kevin Dradjat, Massinissa Hamidi, Blaise Hanczar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08062.pdf)

**💡 相关性分析**

满足标准1和标准2：论文核心研究内容是针对异构生物医学数据集（RNA-seq）的领域自适应和知识迁移。这直接关联到化学信息学和质谱分析中常见的问题，即如何整合不同仪器、不同实验室产生的质谱数据，或利用大型质谱数据集训练模型并迁移到特定小数据集上。其提出的方法为解决质谱数据的异质性和构建更通用的化学大模型提供了技术参考。

**📖 中文摘要**

本研究提出了一种基于深度学习的对抗性领域自适应框架，用于实现跨异构RNA测序（RNA-seq）数据集的知识迁移，以进行癌症类型分类。该方法通过联合优化分类和领域对齐目标，学习一个领域不变的潜在空间。为确保在数据稀缺场景下的训练稳定性和鲁棒性，该框架采用对抗性训练和适当的正则化。论文评估了该框架在三个大规模转录组数据集（TCGA, ARCHS4, GTEx）上的性能，以评估其跨队列迁移知识的能力。实验结果表明，与无自适应基线相比，该方法在癌症和组织类型分类准确性上有一致的提升，特别是在低数据场景下。这项工作突出了领域自适应作为转录组学中数据高效知识转移的强大策略。这种处理异构生物医学数据集（如不同来源或预处理流程的质谱数据）并进行有效知识迁移的框架，与化学信息学和质谱分析中面临的数据整合与模型泛化挑战直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate phenotype prediction from RNA sequencing (RNA-seq) data is essential for diagnosis, biomarker discovery, and personalized medicine. Deep learning models have demonstrated strong potential to outperform classical machine learning approaches, but their performance relies on large, well-annotated datasets. In transcriptomics, such datasets are frequently limited, leading to over-fitting and poor generalization. Knowledge transfer from larger, more general datasets can alleviate this issue. However, transferring information across RNA-seq datasets remains challenging due to heterogeneous preprocessing pipelines and differences in target phenotypes. In this study, we propose a deep learning-based domain adaptation framework that enables effective knowledge transfer from a large general dataset to a smaller one for cancer type classification. The method learns a domain-invariant latent space by jointly optimizing classification and domain alignment objectives. To ensure stable training and robustness in data-scarce scenarios, the framework is trained with an adversarial approach with appropriate regularization. Both supervised and unsupervised approach variants are explored, leveraging labeled or unlabeled target samples. The framework is evaluated on three large-scale transcriptomic datasets (TCGA, ARCHS4, GTEx) to assess its ability to transfer knowledge across cohorts. Experimental results demonstrate consistent improvements in cancer and tissue type classification accuracy compared to non-adaptive baselines, particularly in low-data scenarios. Overall, this work highlights domain adaptation as a powerful strategy for data-efficient knowledge transfer in transcriptomics, enabling robust phenotype prediction under constrained data conditions.

</details>

---

### 69. [Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting](https://arxiv.org/abs/2603.08072)

**基本信息**

- 🔗 arXiv: [`2603.08072`](https://arxiv.org/abs/2603.08072)
- 👥 作者: Irene Iele, Floriano Caprio, Paolo Soda 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08072.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将量子机器学习模型应用于复杂多变量时间序列的预测。这为“化学大模型”探索利用量子计算等新兴计算范式来处理和分析质谱等化学时序数据，以提升模型性能或效率，提供了直接的技术参考和研究思路。

**📖 中文摘要**

本文提出了一种混合量子-经典架构，用于多变量临床时间序列预测，具体任务是联合预测心率、血氧饱和度、脉搏率和呼吸率在未来15、30和60秒的值。该架构在循环神经网络主干中集成了一个变分量子电路（VQC）。一个GRU编码器将历史观测窗口总结为潜在表示，然后将其投影到用于参数化VQC的量子角度中。量子层充当可学习的非线性特征混合器，在最终预测阶段之前建模跨变量交互。在BIDMC PPG和呼吸数据集上使用留一患者交叉验证协议进行评估的结果表明，与经典和深度学习基线相比，该方法具有竞争力的准确性，同时对噪声和缺失输入具有更强的鲁棒性。这些发现表明，混合量子层可以为小规模临床环境中的生理时间序列预测提供有用的归纳偏差。虽然应用领域是临床，但其核心方法——将量子计算模块集成到机器学习模型中以处理复杂时序数据并提升性能——为“化学大模型”探索新型计算架构（如量子机器学习）以处理质谱等化学数据提供了前瞻性思路和潜在的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Forecasting physiological signals can support proactive monitoring and timely clinical intervention by anticipating critical changes in patient status. In this work, we address multivariate multi-horizon forecasting of physiological time series by jointly predicting heart rate, oxygen saturation, pulse rate, and respiratory rate at forecasting horizons of 15, 30, and 60 seconds. We propose a hybrid quantum-classical architecture that integrates a Variational Quantum Circuit (VQC) within a recurrent neural backbone. A GRU encoder summarizes the historical observation window into a latent representation, which is then projected into quantum angles used to parameterize the VQC. The quantum layer acts as a learnable non-linear feature mixer, modeling cross-variable interactions before the final prediction stage. We evaluate the proposed approach on the BIDMC PPG and Respiration dataset under a Leave-One-Patient-Out protocol. The results show competitive accuracy compared with classical and deep learning baselines, together with greater robustness to noise and missing inputs. These findings suggest that hybrid quantum layers can provide useful inductive biases for physiological time series forecasting in small-cohort clinical settings.

</details>

---

### 70. [DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning](https://arxiv.org/abs/2603.08095)

**基本信息**

- 🔗 arXiv: [`2603.08095`](https://arxiv.org/abs/2603.08095)
- 👥 作者: Chi-Min Chan, Ehsan Hajiramezanali, Xiner Li 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08095.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是提升AI科学家在科学推理任务中的可靠性和效率，特别是通过新颖的训练框架优化过程奖励模型。这直接关联到“化学大模型”和“质谱结构推理”中至关重要的模型训练、奖励设计以及从噪声或弱监督数据中学习的问题，为解决相关挑战提供了高级方法论。

**📖 中文摘要**

本文针对科学推理任务中过程奖励模型（PRM）训练成本高昂的问题，提出了DC-W2S（双共识弱到强训练）框架，旨在利用丰富但嘈杂的“弱”监督来训练可靠的PRM。论文指出，现有的弱到强泛化理论缺乏从噪声数据中选择高质量训练信号的规范性指导。DC-W2S通过交叉弱监督者之间的自共识（SC）指标和嵌入空间中的邻域共识（NC）指标，将监督信号分层到不同的可靠性体系中。然后，采用课程学习策略，包括实例级平衡采样和标签级可靠性感知掩码，来指导训练过程。研究表明，DC-W2S能够在无需大量专家标注的情况下，为复杂推理训练出稳健的PRM，证明战略性的数据整理比在大规模噪声数据集上进行不加区分的训练更有效。这项工作聚焦于提升AI科学家的推理可靠性，其提出的用于优化训练信号质量和模型鲁棒性的框架，与构建能够进行可靠质谱结构推理或化学发现的“化学大模型”密切相关，为解决此类模型中奖励建模或训练数据质量的关键问题提供了方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In scientific reasoning tasks, the veracity of the reasoning process is as critical as the final outcome. While Process Reward Models (PRMs) offer a solution to the coarse-grained supervision problems inherent in Outcome Reward Models (ORMs), their deployment is hindered by the prohibitive cost of obtaining expert-verified step-wise labels. This paper addresses the challenge of training reliable PRMs using abundant but noisy "weak" supervision. We argue that existing Weak-to-Strong Generalization (W2SG) theories lack prescriptive guidelines for selecting high-quality training signals from noisy data. To bridge this gap, we introduce the Dual-Consensus Weak-to-Strong (DC-W2S) framework. By intersecting Self-Consensus (SC) metrics among weak supervisors with Neighborhood-Consensus (NC) metrics in the embedding space, we stratify supervision signals into distinct reliability regimes. We then employ a curriculum of instance-level balanced sampling and label-level reliability-aware masking to guide the training process. We demonstrate that DC-W2S enables the training of robust PRMs for complex reasoning without exhaustive expert annotation, proving that strategic data curation is more effective than indiscriminate training on large-scale noisy datasets.

</details>

---

### 71. [Tau-BNO: Brain Neural Operator for Tau Transport Model](https://arxiv.org/abs/2603.08108)

**基本信息**

- 🔗 arXiv: [`2603.08108`](https://arxiv.org/abs/2603.08108)
- 👥 作者: Nuutti Barron, Heng Rao, Urmi Saha 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08108.pdf)

**💡 相关性分析**

满足标准1和标准2：论文核心研究内容是为复杂的生物物理传输模型构建高效的深度学习代理（神经算子）。这直接关联到“化学大模型”中可能涉及的对计算密集型化学过程（如分子动力学、光谱模拟）进行快速近似的需求。其提出的框架可作为在化学领域构建类似代理模型的强大工具和方法论。

**📖 中文摘要**

本文提出了Tau-BNO，一个用于快速近似网络传输模型（NTM）动力学的脑神经算子代理框架。NTM是一个用于研究tau蛋白在脑内传播的复杂生物物理模型，由大型偏微分方程组定义，计算负担重。Tau-BNO结合了一个编码动力学参数的函数算子和一个保留初始状态信息的查询算子，同时通过保留方向性的谱核来近似各向异性传输。经验评估表明，该代理模型在多样化的生物物理机制下具有高预测精度（R²≈0.98），并且比最先进的序列模型（如Transformer和Mamba）性能提升89%。通过将模拟时间从数小时减少到数秒，该代理模型能够产生新的见解并生成新的假设。该框架易于扩展到更广泛的基于连接组的生物物理模型，展示了深度学习代理在加速大规模、计算密集型动力系统分析方面的变革性价值。这项工作虽然应用于神经科学，但其核心贡献——为复杂生物物理系统构建高效的深度学习代理——为化学信息学领域（如为分子动力学模拟、化学反应网络或质谱解析过程构建快速代理模型）提供了强有力的方法论工具，直接服务于“化学大模型”对高效计算工具的需求。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic modeling provides a biophysically grounded framework for studying the spread of pathological tau protein in tauopathies like Alzheimer's disease. Existing approaches typically model tau propagation as a diffusive process on the brain's structural connectome, reproducing macroscopic patterns but neglecting microscale cellular transport and reaction mechanisms. The Network Transport Model (NTM) was introduced to fill this gap, explaining how region-level progression of tau emerges from microscale biophysical processes. However, the NTM faces a common challenge for complex models defined by large systems of partial differential equations: the inability to perform parameter inference and mechanistic discovery due to high computational burden and slow model simulations. To overcome this barrier, we propose Tau-BNO, a Brain Neural Operator surrogate framework for rapidly approximating NTM dynamics that captures both intra-regional reaction kinetics and inter-regional network transport. Tau-BNO combines a function operator that encodes kinetic parameters with a query operator that preserves initial state information, while approximating anisotropic transport through a spectral kernel that retains directionality. Empirical evaluations demonstrate high predictive accuracy ($R^2\approx$ 0.98) across diverse biophysical regimes and an 89\% performance improvement over state-of-the-art sequence models like Transformers and Mamba, which lack inherent structural priors. By reducing simulation time from hours to seconds, we show that the surrogate model is capable of producing new insights and generating new hypotheses. This framework is readily extensible to a broader class of connectome-based biophysical models, showcasing the transformative value of deep learning surrogates to accelerate analysis of large-scale, computationally intensive dynamical systems.

</details>

---

### 72. [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://arxiv.org/abs/2603.08127)

**基本信息**

- 🔗 arXiv: [`2603.08127`](https://arxiv.org/abs/2603.08127)
- 👥 作者: Yougang Lyu, Xi Zhang, Xinhao Yi 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08127.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是构建一个能够进行端到端科学发现、并具备自我进化能力的多智能体AI科学家框架。这直接且核心地围绕“化学大模型”的愿景展开，即创建能够自主进行化学研究（包括质谱结构推理）的AI系统。其提出的架构、记忆模块和进化机制为相关系统的设计提供了具体的蓝图和高级范例。

**📖 中文摘要**

本文介绍了EvoScientist，一个不断进化的多智能体AI科学家框架，旨在通过持久记忆和自我进化持续改进科研策略。EvoScientist包含三个专门智能体：负责科学想法生成的研究员智能体（RA）、负责实验实现和执行的工程师智能体（EA），以及从先前交互中提炼可重用知识的进化管理智能体（EMA）。框架包含两个持久记忆模块：（i）构思记忆，总结来自顶级想法的可行研究方向，同时记录先前不成功的方向；（ii）实验记忆，捕获从代码搜索轨迹和最佳性能实现中衍生出的有效数据处理和模型训练策略。这些模块使RA和EA能够检索相关的先前策略，随着时间的推移提高想法质量和代码执行成功率。实验表明，EvoScientist在科学想法生成方面优于7个开源和商业最先进的系统，通过自动和人工评估实现了更高的新颖性、可行性、相关性和清晰度。EvoScientist还通过多智能体进化显著提高了代码执行成功率，展示了持久记忆对于端到端科学发现的有效性。这项工作代表了构建自动化、自适应化学研究平台（即“化学大模型”或AI化学家）的前沿方向，其架构和进化机制对于设计能够自主进行质谱数据解析、结构假设生成和实验规划的智能系统具有直接的启发和参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experimental execution. However, most state-of-the-art AI scientist systems rely on static, hand-designed pipelines and fail to adapt based on accumulated interaction histories. As a result, these systems overlook promising research directions, repeat failed experiments, and pursue infeasible ideas. To address this, we introduce EvoScientist, an evolving multi-agent AI scientist framework that continuously improves research strategies through persistent memory and self-evolution. EvoScientist comprises three specialized agents: a Researcher Agent (RA) for scientific idea generation, an Engineer Agent (EA) for experiment implementation and execution, and an Evolution Manager Agent (EMA) that distills insights from prior interactions into reusable knowledge. EvoScientist contains two persistent memory modules: (i) an ideation memory, which summarizes feasible research directions from top-ranked ideas while recording previously unsuccessful directions; and (ii) an experimentation memory, which captures effective data processing and model training strategies derived from code search trajectories and best-performing implementations. These modules enable the RA and EA to retrieve relevant prior strategies, improving idea quality and code execution success rates over time. Experiments show that EvoScientist outperforms 7 open-source and commercial state-of-the-art systems in scientific idea generation, achieving higher novelty, feasibility, relevance, and clarity via automatic and human evaluation. EvoScientist also substantially improves code execution success rates through multi-agent evolution, demonstrating persistent memory's effectiveness for end-to-end scientific discovery.

</details>

---

### 73. [Mitigating Homophily Disparity in Graph Anomaly Detection: A Scalable and Adaptive Approach](https://arxiv.org/abs/2603.08137)

**基本信息**

- 🔗 arXiv: [`2603.08137`](https://arxiv.org/abs/2603.08137)
- 👥 作者: Yunhui Liu, Qizhuo Xie, Yinfeng Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08137.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕图神经网络（GNN）方法，该方法在化学信息学中被广泛用于分子表示学习和结构推理，是构建化学大模型（如分子图神经网络）的关键技术之一。

**📖 中文摘要**

本文提出了一种名为SAGAD的可扩展自适应图异常检测框架，旨在解决图异常检测中的同质性差异和可扩展性挑战。该框架通过预计算多跳嵌入和应用重参数化的切比雪夫滤波器来提取低频和高频信息，从而高效地捕捉同质性和异质性模式。为了缓解节点级同质性差异，引入了异常上下文感知自适应融合机制，该机制根据每个节点的异常子图结构自适应地融合低通和高通嵌入。为了缓解类级差异，设计了频率偏好引导损失，鼓励异常节点比正常节点保留更多的高频信息。SAGAD支持小批量训练，实现了线性的时间和空间复杂度，并大幅减少了大规模图上的内存使用。该工作提出的图神经网络方法可用于建模复杂的分子结构关系，与化学信息学中利用图结构进行分子性质预测或结构推理的任务高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph anomaly detection (GAD) aims to identify nodes that deviate from normal patterns in structure or features. While recent GNN-based approaches have advanced this task, they struggle with two major challenges: 1) homophily disparity, where nodes exhibit varying homophily at both class and node levels; and 2) limited scalability, as many methods rely on costly whole-graph operations. To address them, we propose SAGAD, a Scalable and Adaptive framework for GAD. SAGAD precomputes multi-hop embeddings and applies reparameterized Chebyshev filters to extract low- and high-frequency information, enabling efficient training and capturing both homophilic and heterophilic patterns. To mitigate node-level homophily disparity, we introduce an Anomaly Context-Aware Adaptive Fusion, which adaptively fuses low- and high-pass embeddings using fusion coefficients conditioned on Rayleigh Quotient-guided anomalous subgraph structures for each node. To alleviate class-level disparity, we design a Frequency Preference Guidance Loss, which encourages anomalies to preserve more high-frequency information than normal nodes. SAGAD supports mini-batch training, achieves linear time and space complexity, and drastically reduces memory usage on large-scale graphs. Theoretically, SAGAD ensures asymptotic linear separability between normal and abnormal nodes under mild conditions. Extensive experiments on 10 benchmarks confirm SAGAD's superior accuracy and scalability over state-of-the-art methods.

</details>

---

### 74. [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](https://arxiv.org/abs/2603.08166)

**基本信息**

- 🔗 arXiv: [`2603.08166`](https://arxiv.org/abs/2603.08166)
- 👥 作者: Zhijun Wang, Ling Luo, Dinghao Pan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08166.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型（LLMs）进行生物医学关系抽取，这直接关联到化学信息学中利用AI模型（包括化学大模型）从文本中提取化学知识和结构信息的研究主题。

**📖 中文摘要**

本文提出了RexDrug，一个基于大语言模型的、推理增强的端到端关系抽取框架，用于从大规模生物医学文献中提取n元药物组合。现有方法主要关注二元相互作用，难以建模具有复杂兼容性逻辑和分布式证据的可变长度n元药物组合。RexDrug采用两阶段训练策略：首先，利用多智能体协作机制自动生成高质量的专家式推理轨迹用于监督微调；其次，应用强化学习与专门为药物组合提取定制的多维奖励函数，以进一步优化推理质量和提取准确性。在DrugComb数据集上的广泛实验表明，RexDrug在n元提取任务上始终优于最先进的基线方法。在DDI13语料库上的额外评估证实了其对二元药物-药物相互作用任务的泛化能力。该工作展示了利用大语言模型进行复杂生物医学关系抽取的能力，其框架和思路可迁移至化学信息学领域，用于从文献中提取化学结构、反应或性质信息。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus on binary interactions and struggle to model variable-length n-ary drug combinations, where complex compatibility logic and distributed evidence need to be considered. To address these limitations, we propose RexDrug, an end-to-end reasoning-enhanced relation extraction framework for n-ary drug combination extraction based on large language models. RexDrug adopts a two-stage training strategy. First, a multi-agent collaborative mechanism is utilized to automatically generate high-quality expert-like reasoning traces for supervised fine-tuning. Second, reinforcement learning with a multi-dimensional reward function specifically tailored for DCE is applied to further refine reasoning quality and extraction accuracy. Extensive experiments on the DrugComb dataset show that RexDrug consistently outperforms state-of-the-art baselines for n-ary extraction. Additional evaluation on the DDI13 corpus confirms its generalizability to binary drugdrug interaction tasks. Human expert assessment and automatic reasoning metrics further indicates that RexDrug produces coherent medical reasoning while accurately identifying complex therapeutic regimens. These results establish RexDrug as a scalable and reliable solution for complex biomedical relation extraction from unstructured text. The source code and data are available at this https URL

</details>

---

### 75. [MERLIN: Building Low-SNR Robust Multimodal LLMs for Electromagnetic Signals](https://arxiv.org/abs/2603.08174)

**基本信息**

- 🔗 arXiv: [`2603.08174`](https://arxiv.org/abs/2603.08174)
- 👥 作者: Junyu Shen, Zhendong She, Chenghanyu Zhang 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08174.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究多模态大语言模型（MLLMs）在特定科学领域（电磁信号）的应用，这与构建面向化学或质谱领域的“化学大模型”或“质谱大模型”主题直接相关。2) 论文贡献了大规模领域数据集（EM-100k）和评估基准（EM-Bench），这为相关领域（如质谱）构建类似数据资源提供了范例。

**📖 中文摘要**

本文针对电磁（EM）领域，提出了构建低信噪比鲁棒性多模态大语言模型（MLLMs）的三部分贡献，以应对该领域高质量配对数据集稀缺、缺乏系统性评估基准以及在低信噪比环境下模型性能严重下降的挑战。首先，构建并发布了EM-100k，一个包含超过10万个EM信号-文本对的大规模数据集。其次，提出了EM-Bench，一个涵盖从感知到推理的多样化下游任务的综合性基准。最后，提出了MERLIN，一个新颖的训练框架，旨在不仅将低层信号表示与高层语义文本对齐，还显式地增强模型在具有挑战性的低信噪比环境中的鲁棒性和性能。该工作展示了将多模态大模型范式应用于特定科学领域（如电磁信号处理）的路径，其方法论（构建领域数据集、基准和专用模型框架）对于在化学信息学和质谱分析领域开发类似的“质谱-文本”多模态大模型具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The paradigm of Multimodal Large Language Models (MLLMs) offers a promising blueprint for advancing the electromagnetic (EM) domain. However, prevailing approaches often deviate from the native MLLM paradigm, instead using task-specific or pipelined architectures that lead to fundamental limitations in model performance and generalization. Fully realizing the MLLM potential in EM domain requires overcoming three main challenges: (1) Data. The scarcity of high-quality datasets with paired EM signals and descriptive text annotations used for MLLMs pre-training; (2) Benchmark. The absence of comprehensive benchmarks to systematically evaluate and compare the performance of models on EM signal-to-text tasks; (3) Model. A critical fragility in low Signal-to-Noise Ratio (SNR) environments, where critical signal features can be obscured, leading to significant performance degradation. To address these challenges, we introduce a tripartite contribution to establish a foundation for MLLMs in the EM domain. First, to overcome data scarcity, we construct and release EM-100k, a large-scale dataset comprising over 100,000 EM signal-text pairs. Second, to enable rigorous and standardized evaluation, we propose EM-Bench, the most comprehensive benchmark featuring diverse downstream tasks spanning from perception to reasoning. Finally, to tackle the core modeling challenge, we present MERLIN, a novel training framework designed not only to align low-level signal representations with high-level semantic text, but also to explicitly enhance model robustness and performance in challenging low-SNR environments. Comprehensive experiments validate our method, showing that MERLIN is state-of-the-art in the EM-Bench and exhibits remarkable robustness in low-SNR settings.

</details>

---

### 76. [Practical Type Inference: High-Throughput Recovery of Real-World Structures and Function Signatures](https://arxiv.org/abs/2603.08225)

**基本信息**

- 🔗 arXiv: [`2603.08225`](https://arxiv.org/abs/2603.08225)
- 👥 作者: Lukas Seidel, Sam Thomas, Konrad Rieck
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08225.pdf)

**💡 相关性分析**

满足标准1：论文的核心是从数据中推断结构信息（类型、函数签名），其方法论和问题形式与“质谱结构推理”中从质谱信号推断分子结构具有高度的概念相似性，可视为跨领域的相关研究。

**📖 中文摘要**

本文提出了一种改进的n-gram方法（XTRIDE），用于从剥离的二进制文件中进行高效、高吞吐量的类型推断，以支持精确的反编译。该方法专注于实用性：高度优化的吞吐量和可操作的置信度分数使其能够部署在自动化管道中。与结构恢复领域的最新技术相比，该方法在实现相当性能的同时，速度提高了70到2300倍。由于推断基于真实世界的类型，该方法实现了完全正确的结构布局的最高比例。通过优化的训练方案，模型在DIRT数据集上的类型推断准确率总体达到90.15%，比当前最优水平高出5.09个百分点。此外，本文还展示了基于n-gram的类型预测可推广到函数签名恢复。虽然该工作主要面向软件逆向工程，但其核心——从低级数据（二进制字节）中推断高级结构信息（类型、函数签名）——与质谱结构推理中从质谱数据（低维信号）推断分子结构（高维图）在问题本质上高度相似。其高效的数据驱动推断方法（n-gram模型）和关注可部署性的设计思路，对开发高效的质谱解析算法具有启发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The recovery of types from stripped binaries is a key to exact decompilation, yet its practical realization suffers. For composite structures in particular, both layout and semantic fidelity are required to enable end-to-end reconstruction. Many existing approaches either synthesize layouts or infer names post-hoc, which weakens downstream usability. This is further aggravated by an excessive runtime overhead that is especially prohibitive in automated environments. We present XTRIDE, an improved n-gram-based approach that focuses on practicality: highly optimized throughput and actionable confidence scores allow for deployment in automated pipelines. When compared to the state of the art in struct recovery, our method achieves comparable performance while being between 70 and 2300 times faster. As our inference is grounded in real-world types, we achieve the highest ratio of fully-correct struct layouts. With an optimized training regimen, our model outperforms the current state of the art on the DIRT dataset by 5.09 percentage points, achieving 90.15% type inference accuracy overall. Furthermore, we show that n-gram-based type prediction generalizes to function signature recovery: conducting a case study on embedded firmware, we show that this efficient approach to function similarity can assist in typical reverse engineering tasks.

</details>

---

### 77. [FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use](https://arxiv.org/abs/2603.08262)

**基本信息**

- 🔗 arXiv: [`2603.08262`](https://arxiv.org/abs/2603.08262)
- 👥 作者: Jiaxuan Lu, Kong Wang, Yemin Wang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08262.pdf)

**💡 相关性分析**

满足标准2和3：1) 论文提出了一个用于评估领域特定（金融）大模型智能体工具使用能力的基准测试（FinToolBench），这为在化学信息学领域构建类似的“化学工具使用”基准或资源提供了范例（标准2）。2) 论文对LLM智能体在专业领域使用工具这一范式进行了系统性探索和评估，包含了对当前方法局限性的讨论，这与“化学大模型”如何集成领域工具的前沿讨论相关（标准3）。

**📖 中文摘要**

本文介绍了FinToolBench，这是首个专门用于评估金融工具学习智能体的真实世界、可运行的基准测试。与先前仅限于少量模拟工具的工作不同，FinToolBench建立了一个真实的生态系统，将760个可执行的金融工具与295个严格的、需要工具使用的查询相结合。论文提出了一个新颖的评估框架，超越了二元执行成功，从金融关键维度评估智能体：及时性、意图类型和监管领域对齐。此外，还提出了FATR，一个具有金融意识的工具检索和推理基线，以增强稳定性和合规性。该工作通过提供首个用于可审计、智能体化金融执行的测试平台，为金融领域的可信AI设立了新标准。虽然领域是金融，但其核心——评估和开发大语言模型（LLM）智能体使用外部工具（API）完成复杂领域任务的能力——与构建能够调用化学数据库、计算工具或谱图解析服务的“化学大模型”智能体在技术范式上完全一致。其基准构建方法、评估维度和基线模型对化学信息学领域开发类似的工具学习评估体系具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into the financial domain is driving a paradigm shift from passive information retrieval to dynamic, agentic interaction. While general-purpose tool learning has witnessed a surge in benchmarks, the financial sector, characterized by high stakes, strict compliance, and rapid data volatility, remains critically underserved. Existing financial evaluations predominantly focus on static textual analysis or document-based QA, ignoring the complex reality of tool execution. Conversely, general tool benchmarks lack the domain-specific rigor required for finance, often relying on toy environments or a negligible number of financial APIs. To bridge this gap, we introduce FinToolBench, the first real-world, runnable benchmark dedicated to evaluating financial tool learning agents. Unlike prior works limited to a handful of mock tools, FinToolBench establishes a realistic ecosystem coupling 760 executable financial tools with 295 rigorous, tool-required queries. We propose a novel evaluation framework that goes beyond binary execution success, assessing agents on finance-critical dimensions: timeliness, intent type, and regulatory domain alignment. Furthermore, we present FATR, a finance-aware tool retrieval and reasoning baseline that enhances stability and compliance. By providing the first testbed for auditable, agentic financial execution, FinToolBench sets a new standard for trustworthy AI in finance. The tool manifest, execution environment, and evaluation code will be open-sourced to facilitate future research.

</details>

---

### 78. [Deconstructing Multimodal Mathematical Reasoning: Towards a Unified Perception-Alignment-Reasoning Paradigm](https://arxiv.org/abs/2603.08291)

**基本信息**

- 🔗 arXiv: [`2603.08291`](https://arxiv.org/abs/2603.08291)
- 👥 作者: Tianyu Yang, Sihong Wu, Yilun Zhao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08291.pdf)

**💡 相关性分析**

满足标准3：论文是对多模态推理（特别是数学领域）的综述和系统性分析，其中提出的“感知-对齐-推理”范式、面临的挑战以及未来方向，与“化学大模型”和“质谱结构推理”中处理多模态数据（文本、图表、谱图）并进行复杂推理的研究主题高度相关，提供了重要的相关讨论和框架参考。

**📖 中文摘要**

本文对多模态数学推理（MMR）的最新研究进行了系统性分析。MMR旨在解决涉及文本和视觉模态的数学问题。当前模型在现实世界的视觉数学任务中仍面临重大挑战，经常误解图表，未能将数学符号与视觉证据对齐，并产生不一致的推理步骤。此外，现有评估主要关注检查最终答案，而不是验证每个中间步骤的正确性或可执行性。为了应对这些限制，越来越多的近期研究通过将结构化感知、显式对齐和可验证推理集成到统一框架中来解决这些问题。为了建立清晰的理解和比较不同MMR方法的路线图，本文围绕四个基本问题对它们进行了系统研究：（1）从多模态输入中提取什么，（2）如何表示和对齐文本和视觉信息，（3）如何进行推理，以及（4）如何评估整个推理过程的正确性。最后，讨论了开放挑战并展望了未来研究的有前景方向。该工作是一篇针对多模态推理（特别是数学领域）的综述和展望论文，其分析框架（感知-对齐-推理）和讨论的挑战（如符号-视觉对齐、可验证推理）完全适用于“化学大模型”和“质谱结构推理”领域。例如，理解化学图表（感知）、将质谱峰与分子子结构对齐（对齐）、进行化学逻辑推理（推理）是该主题的核心。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal Mathematical Reasoning (MMR) has recently attracted increasing attention for its capability to solve mathematical problems that involve both textual and visual modalities. However, current models still face significant challenges in real-world visual math tasks. They often misinterpret diagrams, fail to align mathematical symbols with visual evidence, and produce inconsistent reasoning steps. Moreover, existing evaluations mainly focus on checking final answers rather than verifying the correctness or executability of each intermediate step. To address these limitations, a growing body of recent research addresses these issues by integrating structured perception, explicit alignment, and verifiable reasoning within unified frameworks. To establish a clear roadmap for understanding and comparing different MMR approaches, we systematically study them around four fundamental questions: (1) What to extract from multimodal inputs, (2) How to represent and align textual and visual information, (3) How to perform the reasoning, and (4) How to evaluate the correctness of the overall reasoning process. Finally, we discuss open challenges and offer perspectives on promising directions for future research.

</details>

---

### 79. [Towards Effective and Efficient Graph Alignment without Supervision](https://arxiv.org/abs/2603.08526)

**基本信息**

- 🔗 arXiv: [`2603.08526`](https://arxiv.org/abs/2603.08526)
- 👥 作者: Songyang Chen, Youfang Lin, Yu Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08526.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图对齐（Graph Alignment），这是图表示学习和图神经网络（GNN）领域的一个基础问题。化学信息学中的化学大模型经常处理分子图，而图对齐技术可以用于分子相似性比较、反应预测或跨数据库的分子结构映射，这与“化学大模型”的主题直接相关。

**📖 中文摘要**

本文研究无监督图对齐问题，旨在无需锚节点对的情况下找到不同图之间的节点对应关系。作者指出了现有基于嵌入和最优传输（OT）的方法在精度-效率权衡上的局限性，并提出了一个新的“全局表示和对齐”范式。为此，他们提出了GlobAlign方法及其高效变体GlobAlign-E，该方法利用全局注意力机制和分层跨图传输成本来捕获超越局部图结构的长程和隐式节点依赖关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unsupervised graph alignment aims to find the node correspondence across different graphs without any anchor node pairs. Despite the recent efforts utilizing deep learning-based techniques, such as the embedding and optimal transport (OT)-based approaches, we observe their limitations in terms of model accuracy-efficiency tradeoff. By focusing on the exploitation of local and global graph information, we formalize them as the ``local representation, global alignment'' paradigm, and present a new ``global representation and alignment'' paradigm to resolve the mismatch between the two phases in the alignment process. We then propose \underline{Gl}obal representation and \underline{o}ptimal transport-\underline{b}ased \underline{Align}ment (\texttt{GlobAlign}), and its variant, \texttt{GlobAlign-E}, for better \underline{E}fficiency. Our methods are equipped with the global attention mechanism and a hierarchical cross-graph transport cost, able to capture long-range and implicit node dependencies beyond the local graph structure. Furthermore, \texttt{GlobAlign-E} successfully closes the time complexity gap between representative embedding and OT-based methods, reducing OT's cubic complexity to quadratic terms. Through extensive experiments, our methods demonstrate superior performance, with up to a 20\% accuracy improvement over the best competitor. Meanwhile, \texttt{GlobAlign-E} achieves the best efficiency, with an order of magnitude speedup against existing OT-based methods.

</details>

---

### 80. [PCFEx: Point Cloud Feature Extraction for Graph Neural Networks](https://arxiv.org/abs/2603.08540)

**基本信息**

- 🔗 arXiv: [`2603.08540`](https://arxiv.org/abs/2603.08540)
- 👥 作者: Abdullah Al Masud, Shi Xintong, Mondher Bouazizi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08540.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于3D点云（可视为图）的图神经网络（GNN）特征提取和架构。化学信息学中的化学大模型（如用于分子性质的GNN模型）和质谱结构推理（可能涉及将质谱数据转化为图结构进行推理）都严重依赖图神经网络技术。该论文提出的PCFEx方法和GNN架构为处理图结构数据提供了直接相关的技术思路和范例。

**📖 中文摘要**

本文提出了一种新颖的点云特征提取（PCFEx）技术，用于处理3D点云数据，并将其视为图结构。作者设计了一种图神经网络（GNN）架构来高效处理这些特征，并在毫米波雷达数据集上进行了评估，用于人体姿态估计（HPE）和人类活动识别（HAR）。该工作展示了将特征提取与GNN建模相结合的方法在点云处理精度提升方面的巨大潜力。虽然论文主要关注机器人感知，但其核心方法——为点云数据设计图神经网络特征提取和架构——与化学信息学中处理分子图（一种特殊的图结构）以及质谱数据潜在图表示的研究范式高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph neural networks (GNNs) have gained significant attention for their effectiveness across various domains. This study focuses on applying GNN to process 3D point cloud data for human pose estimation (HPE) and human activity recognition (HAR). We propose novel point cloud feature extraction (PCFEx) techniques to capture meaningful information at the point, edge, and graph levels of the point cloud by considering point cloud as a graph. Moreover, we introduce a GNN architecture designed to efficiently process these features. Our approach is evaluated on four most popular publicly available millimeter wave radar datasets, three for HPE and one for HAR. The results show substantial improvements, with significantly reduced errors in all three HPE benchmarks, and an overall accuracy of 98.8% in mmWave-based HAR, outperforming the existing state of the art models. This work demonstrates the great potential of feature extraction incorporated with GNN modeling approach to enhance the precision of point cloud processing.

</details>

---

### 81. [DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control](https://arxiv.org/abs/2603.08583)

**基本信息**

- 🔗 arXiv: [`2603.08583`](https://arxiv.org/abs/2603.08583)
- 👥 作者: Andrés Ortiz, Nicolás J. Gallego-Molina, Carmen Jiménez-Mesa 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是Kolmogorov-Arnold网络（KANs），这是一种新兴的神经网络架构，在科学发现和函数逼近方面显示出潜力，包括在物理和化学领域的应用。KANs作为可能替代或补充传统深度学习模型（如MLP）的选项，其改进架构（如本文的DFKAN）与探索用于化学和质谱数据分析的“化学大模型”的新颖模型架构主题直接相关。

**📖 中文摘要**

本文介绍了DualFlexKAN（DFKAN），一种灵活的Kolmogorov-Arnold网络（KANs）架构，具有双阶段机制，可独立控制线性前输入变换和线性后输出激活。这种解耦使得能够创建混合网络，以优化表达能力和计算成本之间的权衡。与标准公式不同，DFKAN支持多样的基函数族，并与可配置的正则化策略集成，以稳定训练动态。在回归基准、物理信息任务和函数逼近上的综合评估表明，DFKAN在准确性、收敛速度和梯度保真度方面优于MLP和传统KAN。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-Layer Perceptrons (MLPs) rely on pre-defined, fixed activation functions, imposing a static inductive bias that forces the network to approximate complex topologies solely through increased depth and width. Kolmogorov-Arnold Networks (KANs) address this limitation through edge-centric learnable functions, yet their formulation suffers from quadratic parameter scaling and architectural rigidity that hinders the effective integration of standard regularization techniques. This paper introduces the DualFlexKAN (DFKAN), a flexible architecture featuring a dual-stage mechanism that independently controls pre-linear input transformations and post-linear output activations. This decoupling enables hybrid networks that optimize the trade-off between expressiveness and computational cost. Unlike standard formulations, DFKAN supports diverse basis function families, including orthogonal polynomials, B-splines, and radial basis functions, integrated with configurable regularization strategies that stabilize training dynamics. Comprehensive evaluations across regression benchmarks, physics-informed tasks, and function approximation demonstrate that DFKAN outperforms both MLPs and conventional KANs in accuracy, convergence speed, and gradient fidelity. The proposed hybrid configurations achieve superior performance with one to two orders of magnitude fewer parameters than standard KANs, effectively mitigating the parameter explosion problem while preserving KAN-style expressiveness. DFKAN provides a principled, scalable framework for incorporating adaptive non-linearities, proving particularly advantageous for data-efficient learning and interpretable function discovery in scientific applications.

</details>

---

### 82. [Integral Formulas for Vector Spherical Tensor Products](https://arxiv.org/abs/2603.08630)

**基本信息**

- 🔗 arXiv: [`2603.08630`](https://arxiv.org/abs/2603.08630)
- 👥 作者: Valentin Heyraud, Zachary Weller-Davies, Jules Tilly
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08630.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是SO(3)-等变神经网络中的张量积操作。化学信息学中的许多化学大模型（特别是用于分子3D结构的模型）需要具备旋转等变性，而SO(3)-等变神经网络是该领域的核心架构之一。本文对等变操作中关键组件（张量积）的改进和高效实现，直接与构建更高效、更强大的化学等变模型相关。

**📖 中文摘要**

本文推导了向量球面张量积（Vector Spherical Tensor Product）的积分公式，该张量积是Xie等人最近引入的，将Gaunt张量积推广到反对称耦合。作者获得了反对称类似Gaunt系数的显式闭式表达式，这使得能够使用单个向量球面张量积来模拟Clebsch-Gordan张量积，从而将所需的张量积评估减少9倍。这些结果实现了向量球面张量积的高效实用实现，为SO(3)-等变神经网络中这一广义Gaunt张量积的应用铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We derive integral formulas that simplify the Vector Spherical Tensor Product recently introduced by Xie et al., which generalizes the Gaunt tensor product to antisymmetric couplings. In particular, we obtain explicit closed-form expressions for the antisymmetric analogues of the Gaunt coefficients. This enables us to simulate the Clebsch-Gordan tensor product using a single Vector Spherical Tensor Product, yielding a $9\times$ reduction in the required tensor product evaluations. Our results enable efficient and practical implementations of the Vector Spherical Tensor Product, paving the way for applications of this generalization of Gaunt tensor products in $\mathrm{SO}(3)$-equivariant neural networks. Moreover, we discuss how the Gaunt and the Vector Spherical Tensor Products allow to control the expressivity-runtime tradeoff associated with the usual Clebsch-Gordan Tensor Products. Finally, we investigate low rank decompositions of the normalizations of the considered tensor products in view of their use in equivariant neural networks.

</details>

---

### 83. [Group Entropies and Mirror Duality: A Class of Flexible Mirror Descent Updates for Machine Learning](https://arxiv.org/abs/2603.08651)

**基本信息**

- 🔗 arXiv: [`2603.08651`](https://arxiv.org/abs/2603.08651)
- 👥 作者: Andrzej Cichocki, Piergiulio Tempesta
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08651.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习优化算法的新框架，特别是基于群熵理论的镜像下降算法。虽然不直接处理化学或质谱数据，但优化算法是训练任何“化学大模型”的基础。本文提出的通用、灵活的优化框架，为训练复杂模型（包括化学领域的模型）提供了新的算法工具和理论视角，属于支撑性技术。

**📖 中文摘要**

本文引入了一个连接形式群论、群熵与现代机器学习的综合理论和算法框架，为无限、灵活的镜像下降（MD）优化算法家族铺平了道路。该方法利用群熵的丰富结构，群熵是由群组合律控制的一般化熵泛函，涵盖并显著扩展了所有迹形式熵（如香农、Tsallis和Kaniadakis族）。通过利用MD中的群论镜像映射（或链接函数），作者实现了高度灵活和可适应的MD更新，可以针对不同的数据几何和统计分布进行定制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a comprehensive theoretical and algorithmic framework that bridges formal group theory and group entropies with modern machine learning, paving the way for an infinite, flexible family of Mirror Descent (MD) optimization algorithms. Our approach exploits the rich structure of group entropies, which are generalized entropic functionals governed by group composition laws, encompassing and significantly extending all trace-form entropies such as the Shannon, Tsallis, and Kaniadakis families. By leveraging group-theoretical mirror maps (or link functions) in MD, expressed via multi-parametric generalized logarithms and their inverses (group exponentials), we achieve highly flexible and adaptable MD updates that can be tailored to diverse data geometries and statistical distributions. To this end, we introduce the notion of \textit{mirror duality}, which allows us to seamlessly switch or interchange group-theoretical link functions with their inverses, subject to specific learning rate constraints. By tuning or learning the hyperparameters of the group logarithms enables us to adapt the model to the statistical properties of the training distribution, while simultaneously ensuring desirable convergence characteristics via fine-tuning. This generality not only provides greater flexibility and improved convergence properties, but also opens new perspectives for applications in machine learning and deep learning by expanding the design of regularizers and natural gradient algorithms. We extensively evaluate the validity, robustness, and performance of the proposed updates on large-scale, simplex-constrained quadratic programming problems.

</details>

---

### 84. [Quantum Deep Learning: A Comprehensive Review](https://arxiv.org/abs/2603.06644)

**基本信息**

- 🔗 arXiv: [`2603.06644`](https://arxiv.org/abs/2603.06644)
- 👥 作者: Yanjun Ji, Zhao-Yun Chen, Marco Roth 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06644.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对“量子深度学习”这一前沿交叉领域的综述。虽然主题是量子机器学习，但其深度涵盖了深度学习与量子计算的结合，这代表了“大模型”未来可能的发展方向之一（量子增强的AI）。对于关注“化学大模型”未来演进（如量子化学计算与AI的结合）的研究者，这篇综述提供了重要的相关讨论和展望。

**📖 中文摘要**

本文对量子深度学习（QDL）进行了全面回顾。QDL探索使用量子和量子启发资源，以确定在特定资源约束下，如何基于深度学习核心能力（如表达能力、泛化性和可扩展性）进行增强。本综述提供了QDL的操作定义，并引入了包含四种主要范式的分类法：混合量子-经典模型、量子深度神经网络、用于深度学习原语的量子算法以及量子启发的经典算法。理论原理与超导、离子阱、光子、半导体自旋和中性原子系统以及量子退火器中的先进架构、软件工具链和实验演示相联系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum deep learning (QDL) explores the use of both quantum and quantum-inspired resources to determine when deep learning's core capabilities, such as expressivity, generalization, and scalability, can be enhanced based on specific resource constraints. Distinct from broader quantum machine learning, QDL emphasizes compositional depth at the pipeline level and the integration of quantum or quantum-inspired components within end-to-end workflows. This review provides an operational definition of QDL and introduces a taxonomy comprising four primary paradigms: hybrid quantum-classical models, quantum deep neural networks, quantum algorithms for deep learning primitives, and quantum-inspired classical algorithms. Theoretical principles are connected to advanced architectures, software toolchains, and experimental demonstrations across superconducting, trapped-ion, photonic, semiconductor spin, and neutral-atom systems, as well as quantum annealers. Claims of quantum advantage are critically assessed by distinguishing provable complexity-theoretic separations from empirical observations. The analysis characterizes trade-offs between model expressivity, trainability, and classical simulability, while systematically detailing the bottlenecks imposed by optimization landscapes, input-output access models, and hardware constraints. Applications are surveyed in domains encompassing image classification, natural language processing, scientific discovery, quantum data processing, and quantum optimal control, underscoring fair benchmarking against optimized classical counterparts and a comprehensive assessment of resource requirements. This review serves as a tutorial entry point for graduate students while guiding readers to specialized literature. It concludes with a verification-aware roadmap to transition QDL from near-term demonstrations to scalable and fault-tolerant implementations.

</details>

---

### 85. [GNN For Muon Particle Momentum estimation](https://arxiv.org/abs/2603.06675)

**基本信息**

- 🔗 arXiv: [`2603.06675`](https://arxiv.org/abs/2603.06675)
- 👥 作者: Vishak K Bhat, Eric A. F. Reinhardt, Sergei Gleyzer
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06675.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用图神经网络（GNN）解决高能物理中的粒子动量估计问题。GNN是构建“化学大模型”处理分子图数据的核心技术。该论文展示了GNN在科学计算（物理学）中处理复杂关系数据的应用实例，其方法（图构建、GNN应用）与化学信息学中利用GNN处理分子图在方法论上高度同源，直接相关。

**📖 中文摘要**

本文探索使用图神经网络（GNNs）进行μ子粒子动量估计的任务。作者提出了两种图构建方法，并应用GNN模型来利用数据固有的图结构。论文首先表明，GNN在平均绝对误差（MAE）方面优于传统模型（如TabNet），证明了其在捕获数据内复杂依赖关系方面的有效性。其次，论文表明节点特征的维度对GNN的效率至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Due to a high rate of overall data generation relative to data generation of interest, the CMS experiment at the Large Hadron Collider uses a combination of hardware- and software-based triggers to select data for capture. Accurate momentum calculation is crucial for improving the efficiency of the CMS trigger systems, enabling better classification of low- and high- momentum particles and reducing false triggers. This paper explores the use of Graph Neural Networks (GNNs) for the momentum estimation task. We present two graph construction methods and apply a GNN model to leverage the inherent graph structure of the data. In this paper firstly, we show that the GNN outperforms traditional models like TabNet in terms of Mean Absolute Error (MAE), demonstrating its effectiveness in capturing complex dependencies within the data. Secondly we show that the dimension of the node feature is crucial for the efficiency of GNN.

</details>

---

### 86. [ViroGym: Realistic Large-Scale Benchmarks for Evaluating Viral Proteins](https://arxiv.org/abs/2603.06740)

**基本信息**

- 🔗 arXiv: [`2603.06740`](https://arxiv.org/abs/2603.06740)
- 👥 作者: Yichen Zhou, Jonathan Golob, Amir Karimi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06740.pdf)

**💡 相关性分析**

满足标准2：论文提供了大规模、系统化的病毒蛋白质变体效应数据集（ViroGym），该数据集可用于训练和评估化学/生物大模型（如蛋白质语言模型），这与‘化学大模型’主题高度相关。

**📖 中文摘要**

本文介绍了ViroGym，一个用于评估病毒蛋白质变体效应预测的综合基准。它包含来自真核病毒的79个深度突变扫描（DMS）实验，总计超过55万个突变氨基酸序列，以及流感病毒中和任务和SARS-CoV-2的真实世界预测任务。该工作系统地评估了蛋白质语言模型（pLMs）在病毒蛋白质上的性能，为疫苗抗原选择提供了一个框架。虽然论文核心是评估pLMs在病毒蛋白质上的功能预测，但其构建的ViroGym基准数据集和评估框架，为训练和评估更广泛的化学/生物大模型（特别是蛋白质语言模型）提供了重要的数据资源和基准测试平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (pLMs) have shown strong potential in prediction of the functional effects of missense variants in zero-shot settings. Despite this progress, benchmarking pLMs for viral proteins remains limited and systematic strategies for integrating in silico metrics with in vitro validation to guide antigen and target selection are underdeveloped. Here, we introduce ViroGym, a comprehensive benchmark designed to evaluate variant effect prediction in viral proteins and to facilitate selecting rational antigen candidates. We curated 79 deep mutational scanning (DMS) assays encompassing eukaryotic viruses, collectively comprising 552,937 mutated amino acid sequences across 7 distinct phenotypic readouts, and 21 influenza virus neutralisation tasks and a real-world predictive task for SARS-CoV-2. We benchmark well-established pLMs on fitness landscapes, antigenic diversity, and pandemic forecasting to provide a framework for vaccine selection, and show that pLMs selected using in vitro experimental data excel at predicting dominant circulating mutations in real world.

</details>

---

### 87. [How Private Are DNA Embeddings? Inverting Foundation Model Representations of Genomic Sequences](https://arxiv.org/abs/2603.06950)

**基本信息**

- 🔗 arXiv: [`2603.06950`](https://arxiv.org/abs/2603.06950)
- 👥 作者: Sofiane Ouaari, Jules Kreuer, Nico Pfeifer
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06950.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕‘化学大模型’的一个具体子类——DNA基础模型（一种用于基因组序列的大模型）展开，深入分析了其隐私安全特性。

**📖 中文摘要**

本文研究了DNA基础模型（如DNABERT-2, Evo 2, Nucleotide Transformer v2）在模型反转攻击下的隐私脆弱性。攻击者试图从模型输出的嵌入向量中重建敏感的原始DNA序列。论文评估了不同嵌入方式（如逐令牌嵌入、平均池化嵌入）的重建质量，发现某些模型和设置下可以实现近乎完美的序列重建。这项工作强调了在基因组基础模型广泛部署于嵌入即服务（EaaS）框架之前，进行隐私感知设计的紧迫性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

DNA foundation models have become transformative tools in bioinformatics and healthcare applications. Trained on vast genomic datasets, these models can be used to generate sequence embeddings, dense vector representations that capture complex genomic information. These embeddings are increasingly being shared via Embeddings-as-a-Service (EaaS) frameworks to facilitate downstream tasks, while supposedly protecting the privacy of the underlying raw sequences. However, as this practice becomes more prevalent, the security of these representations is being called into question. This study evaluates the resilience of DNA foundation models to model inversion attacks, whereby adversaries attempt to reconstruct sensitive training data from model outputs. In our study, the model's output for reconstructing the DNA sequence is a zero-shot embedding, which is then fed to a decoder. We evaluated the privacy of three DNA foundation models: DNABERT-2, Evo 2, and Nucleotide Transformer v2 (NTv2). Our results show that per-token embeddings allow near-perfect sequence reconstruction across all models. For mean-pooled embeddings, reconstruction quality degrades as sequence length increases, though it remains substantially above random baselines. Evo 2 and NTv2 prove to be most vulnerable, especially for shorter sequences with reconstruction similarities > 90%, while DNABERT-2's BPE tokenization provides the greatest resilience. We found that the correlation between embedding similarity and sequence similarity was a key predictor of reconstruction success. Our findings emphasize the urgent need for privacy-aware design in genomic foundation models prior to their widespread deployment in EaaS settings. Training code, model weights and evaluation pipeline are released on: this https URL .

</details>

---

### 88. [A Miniature Brain Transformer: Thalamic Gating, Hippocampal Lateralization, Amygdaloid Salience, and Prefrontal Working Memory in Attention-Coupled Latent Memory](https://arxiv.org/abs/2603.07217)

**基本信息**

- 🔗 arXiv: [`2603.07217`](https://arxiv.org/abs/2603.07217)
- 👥 作者: Hong Jeong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07217.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一种新型的、受神经科学启发的变换器架构（一种特定的大模型），这直接属于‘化学大模型’（广义上包括生物信息学相关模型）的研究范畴，探索了模型结构和记忆机制。

**📖 中文摘要**

本文提出了一种受大脑结构启发的微型脑变换器架构，扩展了注意力耦合潜在记忆框架。它模拟了丘脑中继、杏仁核显著性模块、前额叶工作记忆缓冲区和快速小脑通路等脑区功能，并通过抑制性胼胝体交叉对话耦合侧化的海马体。该模型在MQAR（多查询关联回忆）和模算术两个领域基准上进行了评估。研究发现，功能侧化需要前额叶工作记忆缓冲区和抑制性反馈的协同作用，其充当了对称性破缺器。这项工作为序列模型中的分层持久记忆提供了一个神经生物学动机的蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a miniature brain transformer architecture that extends the attention-coupled latent memory framework with four additional brain-region analogues: a thalamic relay, an amygdaloid salience module, a prefrontal working-memory (PFC) buffer, and a cerebellar fast-path, all coupled by inhibitory callosal cross-talk between lateralized hippocampal banks. We evaluate on a two-domain benchmark -- MQAR (Multi-Query Associative Recall; episodic domain) and modular arithmetic (+1 mod 10; rule-based domain) -- using a seven-variant additive ablation. The central empirical finding is a surprise: inhibitory callosal coupling alone never lateralizes the banks (variants 1-5 maintain D_sep ~ 0.25 and P_ct ~ 0.25 for all 30 epochs). Functional lateralization requires the synergy of PFC and inhibition: only when the PFC buffer is added (variant 6) does a sharp, discontinuous phase transition fire -- at epoch 11 for the PFC-only variant and epoch 10 for the full model -- collapsing P_ct from 0.25 to ~0.002 and more than doubling D_sep from 0.251 to 0.501 in a single gradient step. The PFC buffer acts as a symmetry-breaker: its slowly drifting domain context creates the initial asymmetry that the inhibitory feedback loop then amplifies irreversibly. The cerebellar fast-path accelerates the transition by one epoch (epoch 10 vs. epoch 11) with no asymptotic change, confirming its convergence-acceleration role. The result constitutes a novel, falsifiable prediction -- no lateralization without working memory context -- and a principled, neurobiologically motivated blueprint for hierarchical persistent memory in sequence models.

</details>

---

### 89. [AI-Driven Phase Identification from X-ray Hyperspectral Imaging of cycled Na-ion Cathode Materials](https://arxiv.org/abs/2603.07666)

**基本信息**

- 🔗 arXiv: [`2603.07666`](https://arxiv.org/abs/2603.07666)
- 👥 作者: Fayçal Adrar, Nicolas Folastre, Chloé Pablos 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07666.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心是开发AI方法（基于GMVAE）分析电池材料的化学相变，属于AI在化学材料科学中的应用，与‘化学大模型’主题相关。2) 提出的AI处理流程和GMVAE方法本身，可作为分析复杂化学成像数据的工具，与主题相关。

**📖 中文摘要**

本文开发了一种人工智能驱动的方法，用于在稀疏采样条件下处理高光谱数据，以生成纳米级分辨率的多相图。该方法应用于扫描透射X射线显微镜（STXM）数据，以确定NaxV2(PO4)2F3正极材料单个颗粒在不同荷电状态下的相分布和共存情况。该方法结合了高斯混合变分自编码器（GMVAE）算法和皮尔逊相关系数，以识别钠含量并绘制其空间分布。该方法揭示了单个颗粒内的纳米级相异质性和演化，并通过识别模糊区域、错误分配和位于晶界的过渡相，提高了相检测的可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Na-ion batteries have emerged as viable candidates for large-scale energy storage applica- tions due to resource abundance and cost advantages. The constraints imposed on their performance and durability, for instance, by complex phase transformations in positive electrode materials during electrochemical cycling, can be addressed and are thus not detrimental to their development. However, diffusion-limited Na-ion transport can drive spatially heterogeneous phase nucleation and propagation, leading to multiphase coexis- tence and locally non-uniform electrochemical activity, generating complex reaction path- ways that challenge both mechanistic understanding and predictive material optimization. These challenges can be addressed by investigating single-crystalline regions of materials, i.e. down to the scale of individual particles, although such analyses are often constrained by energetically and/or spatially sparse hyperspectral datasets. Here, we developed an AI-driven method to process hyperspectral data under sparse sampling conditions and generate multiphase maps with nanometer-scale resolution over a micrometer-scale field of view. We applied this processing on scanning transmission X-ray microscopy (STXM) data to determine the distribution and coexistence of phases in individual particles of NaxV2(PO4)2F3 cathode materials, at different states of charge. The methodology relies on a workflow which combines a Gaussian mixture variational autoencoder (GMVAE) algorithm with the Pearson corre- lation coefficient to identify the sodium content and map their spatial distribution. Our approach reveals nanoscale phase heterogeneity and evolution within individual particles, and improves the reliability of phase detection by identifying ambiguity zones, false assign- ments, and transition phases localized at grain boundaries.

</details>

---

### 90. [AI Agents, Language, Deep Learning and the Next Revolution in Science](https://arxiv.org/abs/2603.07940)

**基本信息**

- 🔗 arXiv: [`2603.07940`](https://arxiv.org/abs/2603.07940)
- 👥 作者: Ke Li, Beijiang Liu, Bruce Mellado 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07940.pdf)

**💡 相关性分析**

满足标准1和3：1) 论文核心探讨了AI智能体（基于大语言模型）如何变革科学研究范式，这直接关联到‘化学大模型’在科研中的应用前景。3) 论文具有综述和展望性质，讨论了AI智能体作为下一代科学方法的愿景，对相关领域有重要的前瞻性讨论。

**📖 中文摘要**

本文提出，由大型语言模型和多模态学习驱动的、人类监督的AI智能体，代表了科学方法的下一次演进。这些智能体可以解释科学意图、设计和执行分析工作流，并通过特定领域语言确保可追溯性。论文以粒子物理为例，介绍了中国科学院高能物理研究所的Dr. Sai系统，这是一个部署于CEPC对撞机研究中的多智能体推理框架。这种新兴方法并不取代人类科学家，而是扩展了他们的认知范围，使发现能够随复杂性而扩展，并重新定义了智能机器时代知识生产的方式。其意义超越了粒子物理学，为所有面临相同复杂性上限的数据驱动科学提供了蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern science is reaching a critical inflection point. Instruments across disciplines, from particle physics and astronomy to genomics and climate modeling, now produce data of such scale, diversity, and interdependence that traditional analytical methods can no longer keep pace. This growing imbalance between data generation and data understanding signals the need for a new scientific paradigm. We propose that intelligent, human-supervised AI agents operating over deep-learning algorithms, represent the next evolution of the scientific method. Built upon large language models and multimodal learning, these agents can interpret scientific intent, design and execute analytical workflows, and ensure traceability through domain-specific languages that preserve human oversight and accountability. Particle physics, a historic incubator of computational innovation, offers the ideal testbed for this transition. At the Institute of High Energy Physics of the Chinese Academy of Sciences, the Dr. Sai system embodies this vision, a multi-agent reasoning framework deployed within collider research at the CEPC. This emerging approach does not replace human scientists but extends their cognitive reach, enabling discovery to scale with complexity and redefining how knowledge itself is produced in the age of intelligent machines. The significance of this paradigm transcends particle physics, offering a blueprint for all data-driven sciences facing the same complexity ceiling.

</details>

---

### 91. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进机器学习原子间势（MLIPs），这是计算化学和材料科学中一类非常重要的‘化学大模型’。论文通过引入MoE架构来提升这类模型的表达能力和效率，直接围绕该主题展开。

**📖 中文摘要**

本文系统地为机器学习原子间势（MLIPs）开发了混合专家（MoE）和混合线性专家（MoLE）架构，并分析了路由策略和专家设计的影响。研究表明，稀疏激活与共享专家相结合能带来显著的性能提升，并且当存在共享专家时，非线性MoE formulations优于MoLE。此外，元素级路由 consistently优于构型级路由。最终的元素级MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、具有化学可解释性的专家专业化，表明模型有效地捕捉了元素特定的化学特征以实现精确的原子间建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 92. [Characterization and upgrade of a quantum graph neural network for charged particle tracking](https://arxiv.org/abs/2603.08667)

**基本信息**

- 🔗 arXiv: [`2603.08667`](https://arxiv.org/abs/2603.08667)
- 👥 作者: Matteo Argenton, Laura Cappelli, Concezio Bozzi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08667.pdf)

**💡 相关性分析**

满足标准1：论文研究用于高能物理中粒子径迹重建的量子图神经网络（QGNN）。虽然涉及量子计算，但其核心是探索新型的、基于图的神经网络模型（一种特定架构的模型）解决物理数据分析问题，与‘化学大模型’（广义的科学计算模型）主题相关。

**📖 中文摘要**

本文描述并升级了用于带电粒子径迹重建的量子图神经网络（QGNN）架构。该模型在模拟的高亮度数据集上运行，对相邻探测器层之间可能的命中点连接进行分类。QGNN被设计为混合架构，在经典前馈网络之间交错参数化量子电路。作者描述了经典组件和量子组件之间的相互作用，报告了对原始设计的主要升级，并提供了训练行为改进的新证据。这项工作代表了量子机器学习模型在高能物理任务中作为潜在新方法的探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the forthcoming years the LHC experiments are going to be upgraded to benefit from the substantial increase of the LHC instantaneous luminosity, which will lead to larger, denser events, and, consequently, greater complexity in reconstructing charged particle tracks, motivating frontier research in new technologies. Quantum machine learning models are being investigated as potential new approaches to high energy physics (HEP) tasks. We characterize and upgrade a quantum graph neural network (QGNN) architecture for charged particle track reconstruction on a simulated high luminosity dataset. The model operates on a set of event graphs, each built from the hits generated in tracking detector layers by particles produced in proton collisions, performing a classification of the possible hit connections between adjacent layers. In this approach the QGNN is designed as a hybrid architecture, interleaving classical feedforward networks with parametrized quantum circuits. We characterize the interplay between the classical and quantum components. We report on the principal upgrades to the original design, and present new evidence of improved training behavior, specifically in terms of convergence toward the final trained configuration.

</details>

---

### 93. [Multi-Scale Distillation for RGB-D Anomaly Detection on the PD-REAL Dataset](https://arxiv.org/abs/2311.04095)

**基本信息**

- 🔗 arXiv: [`2311.04095`](https://arxiv.org/abs/2311.04095)
- 👥 作者: Jianjian Qin, Chao Zhang, Chunzhi Gu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2311.04095.pdf)

**💡 相关性分析**

满足标准2：论文贡献了一个新颖的、成本可控的3D异常检测数据集PD-REAL。虽然应用场景是视觉检测，但其构建多模态（RGB-D）数据集的理念和方法，对于需要3D结构信息的化学信息学或质谱分析相关模型（例如，处理3D分子结构或光谱图像）的数据集构建具有参考价值。

**📖 中文摘要**

本文提出了PD-REAL数据集，一个用于3D领域无监督异常检测（AD）的大规模数据集，完全由15个物体类别的橡皮泥模型组成。为了展示3D信息的有用性，使用商用RealSense相机捕获RGB和深度图像。与现有的3D AD数据集相比，PD-REAL的数据采集成本显著更低、易于扩展且更容易控制变量。此外，论文还引入了用于多模态异常检测的、具有分层蒸馏的多尺度师生框架。该架构克服了单尺度蒸馏方法通常难以协调全局上下文与局部特征的固有局限性。利用来自教师网络的多级指导，学生网络可以有效地捕获更丰富的特征以进行异常检测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present PD-REAL, a novel large-scale dataset for unsupervised anomaly detection (AD) in the 3D domain. It is motivated by the fact that 2D-only representations in the AD task may fail to capture the geometric structures of anomalies due to uncertainty in lighting conditions or shooting angles. PD-REAL consists entirely of Play-Doh models for 15 object categories and focuses on the analysis of potential benefits from 3D information in a controlled environment. Specifically, objects are first created with six types of anomalies, such as \textit{dent}, \textit{crack}, or \textit{perforation}, and then photographed under different lighting conditions to mimic real-world inspection scenarios. To demonstrate the usefulness of 3D information, we use a commercially available RealSense camera to capture RGB and depth images. Compared to the existing 3D dataset for AD tasks, the data acquisition of PD-REAL is significantly cheaper, easily scalable, and easier to control variables. \qin{Furthermore, we introduce a multi-scale teacher--student framework with hierarchical distillation for multimodal anomaly detection. This architecture overcomes the inherent limitation of single-scale distillation approaches, which often struggle to reconcile global context with local features. Leveraging multi-level guidance from the teacher network, the student network can effectively capture richer features for anomaly detection. Extensive evaluations with our method and state-of-the-art AD algorithms on our dataset qualitatively and quantitatively demonstrate the higher detection accuracy of our method. }Our dataset can be downloaded from this https URL

</details>

---

### 94. [LoRA-Ensemble: Efficient Uncertainty Modelling for Self-Attention Networks](https://arxiv.org/abs/2405.14438)

**基本信息**

- 🔗 arXiv: [`2405.14438`](https://arxiv.org/abs/2405.14438)
- 👥 作者: Dominik J. Mühlematter, Michelle Halbheer, Alexander Becker 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.14438.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种改进大模型（特别是基于Transformer的自注意力网络）不确定性建模和校准的新方法（LoRA-Ensemble）。这直接针对大模型在实际应用中的关键问题（可靠性和校准），属于‘化学大模型’技术栈中模型优化和改进的重要研究方向。

**📖 中文摘要**

本文介绍了LoRA-Ensemble，一种用于自注意力网络的高效参数集成方法。它基于最初为高效LLM微调开发的低秩适应（LoRA），并将其扩展为一种隐式集成方案，其中所有集成成员共享相同的预训练自注意力网络，但具有用于注意力投影的个体低秩矩阵。所得到的方法不仅优于最先进的隐式技术（如BatchEnsemble），甚至在准确性上匹配或超过了显式集成，同时实现了更好的校准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Numerous real-world decisions rely on machine learning algorithms and require calibrated uncertainty estimates. However, modern methods often yield overconfident, uncalibrated predictions. The dominant approach to quantifying the uncertainty inherent in the model is to train an ensemble of separate predictors and measure their empirical variance. In an explicit implementation, the ensemble has a high computational cost and memory footprint, especially if the base model itself is already large, like modern transformers. This motivates efforts to develop implicit ensemble methods that emulate the ensemble without explicitly instantiating all its members. We introduce LoRA-Ensemble, a parameter-efficient ensembling method for self-attention networks. It is based on Low-Rank Adaptation (LoRA), originally developed for efficient LLM fine-tuning, and extends it into an implicit ensembling scheme, where all ensemble members share the same, pre-trained self-attention network, but have individual low-rank matrices for the attention projections. The resulting method not only outperforms state-of-the-art implicit techniques like BatchEnsemble, but even matches or exceeds the accuracy of an Explicit Ensemble, while at the same time achieving superior calibration.

</details>

---

### 95. [BNEM: A Boltzmann Sampler Based on Bootstrapped Noised Energy Matching](https://arxiv.org/abs/2409.09787)

**基本信息**

- 🔗 arXiv: [`2409.09787`](https://arxiv.org/abs/2409.09787)
- 👥 作者: RuiKang OuYang, Bo Qiang, José Miguel Hernández-Lobato
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.09787.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从能量函数中学习的扩散模型采样器（BNEM），这直接属于生成模型/化学大模型的研究范畴，其方法可应用于分子生成和采样等化学信息学任务。

**📖 中文摘要**

本文提出了一种基于扩散的采样器BNEM，用于从给定的能量函数（如分子动力学中的玻尔兹曼分布）生成独立同分布样本。该方法通过学习噪声数据的能量，提出了Noised Energy Matching (NEM)采样器，理论上具有更低的方差和更高的复杂度。进一步，通过应用一种新颖的自举技术来平衡偏差和方差，形成了BNEM。论文在二维40高斯混合模型和4粒子双阱势等系统上进行了评估。该方法的核心是学习一个能够从能量函数（而非数据）中采样的神经采样器，这与化学信息学中用于分子生成和性质预测的生成模型（化学大模型）在方法论上高度相关，特别是其扩散模型框架和能量函数学习的思想，可直接应用于分子构象采样、性质优化等任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing an efficient sampler capable of generating independent and identically distributed (IID) samples from a Boltzmann distribution is a crucial challenge in scientific research, e.g. molecular dynamics. In this work, we intend to learn neural samplers given energy functions instead of data sampled from the Boltzmann distribution. By learning the energies of the noised data, we propose a diffusion-based sampler, Noised Energy Matching, which theoretically has lower variance and more complexity compared to related works. Furthermore, a novel bootstrapping technique is applied to NEM to balance between bias and variance. We evaluate NEM and BNEM on a 2-dimensional 40 Gaussian Mixture Model (GMM) and a 4-particle double-well potential (DW-4). The experimental results demonstrate that BNEM can achieve state-of-the-art performance while being more robust.

</details>

---

### 96. [Open-World Reinforcement Learning over Long Short-Term Imagination](https://arxiv.org/abs/2410.03618)

**基本信息**

- 🔗 arXiv: [`2410.03618`](https://arxiv.org/abs/2410.03618)
- 👥 作者: Jiajian Li, Qi Wang, Yunbo Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.03618.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建一个用于决策的“世界模型”，这与化学信息学中旨在学习化学空间规律和进行性质/反应预测的“化学大模型”在核心概念（学习复杂系统的表示与动态）上高度相关。

**📖 中文摘要**

本文提出了LS-Imagine，一种用于开放世界视觉强化学习的方法。其核心是构建一个“长短时世界模型”，通过模拟目标条件的状态跳转和计算相应的可达性图，将长期价值整合到行为学习中。该方法在MineDojo环境中超越了现有技术。虽然论文主要关注强化学习，但其构建“世界模型”的核心思想——学习一个能够预测未来状态和奖励的模型——与化学信息学中旨在学习分子结构、性质与反应之间复杂映射关系的“化学大模型”在概念上相通。这类模型旨在对化学空间进行建模和推理，可以视为一种特定领域的“世界模型”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training visual reinforcement learning agents in a high-dimensional open world presents significant challenges. While various model-based methods have improved sample efficiency by learning interactive world models, these agents tend to be "short-sighted", as they are typically trained on short snippets of imagined experiences. We argue that the primary challenge in open-world decision-making is improving the exploration efficiency across a vast state space, especially for tasks that demand consideration of long-horizon payoffs. In this paper, we present LS-Imagine, which extends the imagination horizon within a limited number of state transition steps, enabling the agent to explore behaviors that potentially lead to promising long-term feedback. The foundation of our approach is to build a $\textit{long short-term world model}$. To achieve this, we simulate goal-conditioned jumpy state transitions and compute corresponding affordance maps by zooming in on specific areas within single images. This facilitates the integration of direct long-term values into behavior learning. Our method demonstrates significant improvements over state-of-the-art techniques in MineDojo.

</details>

---

### 97. [Transformers as Implicit State Estimators: In-Context Learning in Dynamical Systems](https://arxiv.org/abs/2410.16546)

**基本信息**

- 🔗 arXiv: [`2410.16546`](https://arxiv.org/abs/2410.16546)
- 👥 作者: Usman Akram, Haris Vikalo
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.16546.pdf)

**💡 相关性分析**

满足标准1：论文的核心展示了Transformer模型通过上下文学习进行隐式状态估计以预测系统输出的能力。这种从序列数据（输入-输出对）中推断隐藏状态（如分子结构）的范式，与“质谱结构推理”任务（从质谱数据序列推断分子结构）在问题定义和解决思路上直接相关。

**📖 中文摘要**

本文展示了在上下文学习（ICL）设置下，Transformer模型能够隐式推断动态系统的隐藏状态，从而预测其输出，而无需在测试时进行梯度更新或明确的系统模型知识。具体来说，当提供过去输入-输出对的短上下文和可选系统参数时，冻结的Transformer可以准确预测当前输出。在线性高斯状态下，其预测与卡尔曼滤波器非常匹配；在非线性状态下，其性能接近扩展卡尔曼滤波器和粒子滤波器。这一发现表明，Transformer的上下文学习为动态系统的输出预测提供了一种灵活的非参数替代方案，其基础是隐式的潜在状态估计。这种“隐式状态估计”和“序列建模”的能力，与质谱结构推理中从质谱数据序列推断分子结构（一种隐式状态）的任务在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting the behavior of a dynamical system from noisy observations of its past outputs is a classical problem encountered across engineering and science. For linear systems with Gaussian inputs, the Kalman filter -- the best linear minimum mean-square error estimator of the state trajectory -- is optimal in the Bayesian sense. For nonlinear systems, Bayesian filtering is typically approached using suboptimal heuristics such as the Extended Kalman Filter (EKF), or numerical methods such as particle filtering (PF). In this work, we show that transformers, employed in an in-context learning (ICL) setting, can implicitly infer hidden states in order to predict the outputs of a wide family of dynamical systems, without test-time gradient updates or explicit knowledge of the system model. Specifically, when provided with a short context of past input-output pairs and, optionally, system parameters, a frozen transformer accurately predicts the current output. In linear-Gaussian regimes, its predictions closely match those of the Kalman filter; in nonlinear regimes, its performance approaches that of EKF and PF. Moreover, prediction accuracy degrades gracefully when key parameters, such as the state-transition matrix, are withheld from the context, demonstrating robustness and implicit parameter inference. These findings suggest that transformer in-context learning provides a flexible, non-parametric alternative for output prediction in dynamical systems, grounded in implicit latent-state estimation.

</details>

---

### 98. [Noise-Aware System Identification for High-Dimensional Stochastic Dynamics](https://arxiv.org/abs/2411.00002)

**基本信息**

- 🔗 arXiv: [`2411.00002`](https://arxiv.org/abs/2411.00002)
- 👥 作者: Ziheng Guo, Igor Cialenco, Ming Zhong
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.00002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从数据中学习随机动力系统的模型（包括漂移和噪声），这属于更广泛的“从数据中学习模型”范畴，与化学信息学中利用机器学习从化学数据中构建预测模型（化学大模型）的目标直接相关。其处理高维和复杂噪声的方法也对质谱数据分析有借鉴意义。

**📖 中文摘要**

本文提出了一个噪声感知的系统辨识框架，用于从轨迹数据中联合恢复随机动力系统的确定性漂移和完整的噪声结构，无需对噪声模型进行先验假设。该方法适用于广泛的随机动力学，包括有色噪声和乘性噪声，并能高效扩展到高维系统。论文在多种系统上进行了数值实验验证。该框架的核心是“从数据中学习动力学模型”，这与化学信息学和计算化学中从分子动力学模拟或实验数据中学习力场、反应网络或分子性质预测模型的目标一致。特别是，处理高维、复杂噪声的能力对于从嘈杂的实验数据（如质谱）中学习可靠的模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Stochastic dynamical systems are ubiquitous in physics, biology, and engineering, where both deterministic drifts and random fluctuations govern system behavior. Learning these dynamics from data is particularly challenging in high-dimensional settings with complex, correlated, or state-dependent noise. We introduce a noise-aware system identification framework that jointly recovers the deterministic drift and full noise structure directly from the trajectory data, without requiring prior assumptions on the noise model. Our method accommodates a broad class of stochastic dynamics, including colored and multiplicative noise, that scales efficiently to high-dimensional systems, and accurately reconstructs the underlying dynamics. Numerical experiments on diverse systems validate the approach and highlight its potential for data-driven modeling in complex stochastic environments.

</details>

---

### 99. [Input-Adaptive Generative Dynamics in Diffusion Models](https://arxiv.org/abs/2411.15199)

**基本信息**

- 🔗 arXiv: [`2411.15199`](https://arxiv.org/abs/2411.15199)
- 👥 作者: Yucheng Xing, Xiaodong Liu, Xin Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.15199.pdf)

**💡 相关性分析**

满足标准1：论文的核心是改进扩散模型的生成过程，使其适应输入条件。这种“条件化”和“自适应生成”的思想可直接应用于化学信息学中的“化学大模型”，例如开发能够根据特定约束（如质谱峰值、目标性质）自适应生成分子的扩散模型。

**📖 中文摘要**

本文研究了扩散模型的输入自适应生成动力学。与通常所有样本共享固定去噪轨迹不同，该框架允许生成过程根据每个样本的生成要求进行调整。为此，作者在不同时间跨度和噪声调度下训练扩散主干网络，使其能够在不同的输入自适应轨迹下一致运行。在条件图像生成上的实验表明，扩散轨迹可以随输入变化，同时保持生成质量并减少平均采样步数。这项工作为扩散过程提供了概念证明，表明其可以从输入自适应性中受益。该方法的核心思想——使生成过程（去噪轨迹）适应输入的具体条件——对于“化学大模型”中的分子生成任务具有启发意义。例如，在基于质谱数据生成候选分子结构时，可以根据谱图特征（如复杂度、信噪比）自适应调整生成策略，以提高效率和准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models typically generate data through a fixed denoising trajectory that is shared across all samples. However, generation targets can differ in complexity, suggesting that a single pre-defined diffusion process may not be optimal for every input. In this work, we investigate input-adaptive generative dynamics for diffusion models, where the generation process itself adapts to the conditions of each sample. Instead of relying on a fixed diffusion trajectory, the proposed framework allows the generative dynamics to adjust across inputs according to their generation requirements. To enable this behavior, we train the diffusion backbone under varying horizons and noise schedules, so that it can operate consistently under different input-adaptive trajectories. Experiments on conditional image generation show that diffusion trajectories can vary across inputs while maintaining generation quality and reducing the average number of sampling steps. These results provide a proof of the concept that diffusion processes can benefit from input-adaptive generative dynamics rather than relying on a single fixed trajectory.

</details>

---

### 100. [From Pixels to Predicates: Learning Symbolic World Models via Pretrained Vision-Language Models](https://arxiv.org/abs/2501.00296)

**基本信息**

- 🔗 arXiv: [`2501.00296`](https://arxiv.org/abs/2501.00296)
- 👥 作者: Ashay Athalye, Nishanth Kumar, Tom Silver 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.00296.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用视觉-语言模型从图像中提取符号谓词并构建可推理的符号世界模型。这种“从原始数据到符号表示再到推理”的框架，与“质谱结构推理”任务（从质谱信号到分子结构符号表示）在问题抽象和解决路径上直接相关。

**📖 中文摘要**

本文旨在通过少量短视距的图像序列演示，学习抽象的符号世界模型，以解决复杂机器人领域的长视距决策问题。关键组件是一组定义对象属性和关系的符号谓词。作者利用预训练的视觉-语言模型（VLM）来提出大量可能与决策相关的视觉谓词，并直接从相机图像中评估这些谓词。在训练时，将提出的谓词和演示输入到一个基于优化的模型学习算法中，以获得一个基于所提出谓词紧凑子集定义的抽象符号世界模型。在测试时，给定新环境中的新目标，使用VLM构建当前世界状态的符号描述，然后使用基于搜索的规划算法找到实现目标的低层技能序列。该方法的核心是使用VLM从像素中提取和评估符号谓词，进而构建可规划的符号模型。这种“从感知到符号表示再到推理”的范式，与“质谱结构推理”中从原始谱图数据（像素/信号）提取特征，再推理出符号化的分子结构（如SMILES）的任务流程高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Our aim is to learn to solve long-horizon decision-making problems in complex robotics domains given low-level skills and a handful of short-horizon demonstrations containing sequences of images. To this end, we focus on learning abstract symbolic world models that facilitate zero-shot generalization to novel goals via planning. A critical component of such models is the set of symbolic predicates that define properties of and relationships between objects. In this work, we leverage pretrained vision-language models (VLMs) to propose a large set of visual predicates potentially relevant for decision-making, and to evaluate those predicates directly from camera images. At training time, we pass the proposed predicates and demonstrations into an optimization-based model-learning algorithm to obtain an abstract symbolic world model that is defined in terms of a compact subset of the proposed predicates. At test time, given a novel goal in a novel setting, we use the VLM to construct a symbolic description of the current world state, and then use a search-based planning algorithm to find a sequence of low-level skills that achieves the goal. We demonstrate empirically across experiments in both simulation and the real world that our method can generalize aggressively, applying its learned world model to solve problems with a wide variety of object types, arrangements, numbers of objects, and visual backgrounds, as well as novel goals and much longer horizons than those seen at training time.

</details>

---

### 101. [Strengthening Generative Robot Policies through Predictive World Modeling](https://arxiv.org/abs/2502.00622)

**基本信息**

- 🔗 arXiv: [`2502.00622`](https://arxiv.org/abs/2502.00622)
- 👥 作者: Han Qi, Haocheng Yin, Aris Zhu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.00622.pdf)

**💡 相关性分析**

满足标准1：论文提出的GPC框架集成了生成扩散模型和预测世界模型，用于序列决策。这种“生成+预测+规划”的范式是构建复杂决策系统（包括化学大模型，如用于分子设计和优化的系统）的核心方法论之一，具有高度的概念相关性。

**📖 中文摘要**

本文提出了生成预测控制（GPC），一个学习控制框架，它结合了生成扩散策略和预测世界模型。具体包括：（i）从专家演示中克隆一个基于扩散的生成策略；（ii）从专家演示和随机探索中训练一个预测性的动作条件世界模型；（iii）合成一个在线规划器，该规划器使用（ii）中的世界模型展望未来，对（i）中的动作提议进行排序和优化。该框架在多种机器人操作任务上进行了验证。虽然应用于机器人，但其核心组件——**生成模型（扩散策略）**和**预测模型（世界模型）**的结合——是构建能够进行序列决策的“大模型”的典型架构。这种架构可以类比于化学信息学中，使用生成模型（如扩散模型）提出候选分子，同时使用预测模型（如性质预测器）评估和优化这些候选分子，以实现目标导向的分子设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present generative predictive control (GPC), a learning control framework that (i) clones a generative diffusion-based policy from expert demonstrations, (ii) trains a predictive action-conditioned world model from both expert demonstrations and random explorations, and (iii) synthesizes an online planner that ranks and optimizes the action proposals from (i) by looking ahead into the future using the world model from (ii). Across a variety of robotic manipulation tasks, we demonstrate that GPC consistently outperforms behavior cloning in both state-based and vision-based settings, in simulation and in the real world.

</details>

---

### 102. [Prompt-SID: Learning Structural Representation Prompt via Latent Diffusion for Single-Image Denoising](https://arxiv.org/abs/2502.06432)

**基本信息**

- 🔗 arXiv: [`2502.06432`](https://arxiv.org/abs/2502.06432)
- 👥 作者: Huaqiu Li, Wang Zhang, Xiaowan Hu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.06432.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种利用扩散模型生成结构提示，并通过提示学习引导图像去噪的新方法。这种“扩散模型生成提示”和“提示引导推理”的技术路线，为“质谱结构推理”任务提供了新颖的方法论启示，即可用类似框架从质谱生成结构提示，再推理分子。

**📖 中文摘要**

本文提出了Prompt-SID，一个基于提示学习的单图像去噪框架，强调结构细节的保留。该方法通过下采样图像对以自监督方式进行训练。它通过结构编码捕获原始尺度图像信息，并将此提示集成到去噪器中。为此，作者提出了一个基于潜在扩散过程的结构表示生成模型，并在基于Transformer的去噪器架构中设计了一个结构注意力模块来解码提示。此外，还引入了尺度回放训练机制。论文在合成、真实世界和荧光成像数据集上进行了实验。该方法的核心创新在于使用**扩散模型生成结构提示**，并利用**提示学习**来指导去噪过程。这种“使用扩散模型生成指导性提示”的技术，可以迁移到“质谱结构推理”任务中，例如，使用扩散模型从质谱数据生成一个关于潜在分子结构的“提示”或“先验”，再引导一个推理模型生成具体的分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many studies have concentrated on constructing supervised models utilizing paired datasets for image denoising, which proves to be expensive and time-consuming. Current self-supervised and unsupervised approaches typically rely on blind-spot networks or sub-image pairs sampling, resulting in pixel information loss and destruction of detailed structural information, thereby significantly constraining the efficacy of such methods. In this paper, we introduce Prompt-SID, a prompt-learning-based single image denoising framework that emphasizes preserving of structural details. This approach is trained in a self-supervised manner using downsampled image pairs. It captures original-scale image information through structural encoding and integrates this prompt into the denoiser. To achieve this, we propose a structural representation generation model based on the latent diffusion process and design a structural attention module within the transformer-based denoiser architecture to decode the prompt. Additionally, we introduce a scale replay training mechanism, which effectively mitigates the scale gap from images of different resolutions. We conduct comprehensive experiments on synthetic, real-world, and fluorescence imaging datasets, showcasing the remarkable effectiveness of Prompt-SID. Our code will be released at this https URL .

</details>

---

### 103. [Characterizing Nonlinear Dynamics via Smooth Prototype Equivalences](https://arxiv.org/abs/2503.10336)

**基本信息**

- 🔗 arXiv: [`2503.10336`](https://arxiv.org/abs/2503.10336)
- 👥 作者: Roy Friedman, Noa Moriel, Matthew Ricci 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.10336.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个用于分析和分类动力学系统行为的框架（SPE），其核心是学习系统的表示并与原型匹配。这类似于化学信息学中从分子动力学数据中学习分子行为模式、识别稳定状态或反应中间体的任务，属于“化学大模型”中对复杂化学系统进行建模和分析的一个方面。

**📖 中文摘要**

本文提出了平滑原型等价（SPE）框架，用于通过可逆神经网络将稀疏观测匹配到原型行为，这些网络对平滑相空间变形进行建模。SPE可以通过从原型空间到数据空间的 learned mapping 来定位描述观测动力学长期行为的不变集。此外，SPE可以通过比较变形测量值与原型动力学的数据残差来对动力学状态进行分类。该方法在振荡系统分类方面优于现有技术，并且能够以无方程的方式有效识别不变结构（如极限环和固定点），即使只观测到相空间的一小部分噪声子集。该方法的核心是学习**动力学系统的表示和分类**。在化学信息学中，分子动力学模拟产生的时间序列数据（如构象变化、能量轨迹）的分析与此类似。SPE框架可用于从有限的分子动力学观测中识别和分类分子的稳定构象或反应路径，这属于化学大模型中对分子动态行为建模的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Characterizing the long term behavior of dynamical systems given limited measurements is a common challenge throughout the physical and biological sciences. This is a challenging task due to the sparsity and noise inherent to empirical observations, as well as the variability of possible long-term dynamics. We address this by introducing smooth prototype equivalences (SPE), a framework for matching sparse observations to prototypical behaviors using invertible neural networks which model smooth phase space deformations. SPE can localize the invariant sets describing long-term behavior of the observed dynamics through the learned mapping from prototype space to data space. Furthermore, SPE can classify dynamical regimes by comparing the data residual of the deformed measurements to prototype dynamics. Our method outperforms existing techniques in the classification of oscillatory systems and can efficiently identify invariant structures like limit cycles and fixed points in an equation-free manner, even when only a small, noisy subset of the phase space is observed. SPE further reveals driving genes in synthetic oscillators such as the repressilator regulatory circuit, and traces cyclic biological processes like the cell cycle trajectory directly from experimental high-dimensional single-cell gene expression data.

</details>

---

### 104. [Causal Retrieval with Semantic Consideration](https://arxiv.org/abs/2504.04700)

**基本信息**

- 🔗 arXiv: [`2504.04700`](https://arxiv.org/abs/2504.04700)
- 👥 作者: Hyunseo Shin, Wonseok Hwang
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.04700.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个能够理解并检索因果关系的检索模型（CAWAI）。这种对深层关系（尤其是因果关系）的建模能力，对于构建能够进行科学推理、解释质谱-结构关系或分子性质-结构关系的“化学大模型”至关重要，直接相关于主题所需的深度推理能力。

**📖 中文摘要**

本文提出了CAWAI，一个在语义和因果关系双重目标下训练的检索模型，旨在解决现有信息检索模型主要关注表层语义匹配而忽视更深层关系结构（如因果关系）的问题。CAWAI在多样化的因果检索任务上，特别是在大规模检索设置下，优于各种模型，并在科学领域QA任务上表现出强大的零样本泛化能力。该研究针对的是提升检索系统对复杂查询意图（包括因果关系）的理解能力。在化学信息学和质谱分析领域，许多研究问题本质上是因果或机制性的，例如，“某种官能团如何影响质谱中的碎片化模式？”或“分子结构如何导致其生物活性？”。一个能够更好理解并检索因果关系的模型，对于构建能够回答此类科学问题、辅助质谱解析或分子设计的智能系统（化学大模型）至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in large language models (LLMs) have significantly enhanced the performance of conversational AI systems. To extend their capabilities to knowledge-intensive domains such as biomedical and legal fields, where the accuracy is critical, LLMs are often combined with information retrieval (IR) systems to generate responses based on retrieved documents. However, for IR systems to effectively support such applications, they must go beyond simple semantic matching and accurately capture diverse query intents, including causal relationships. Existing IR models primarily focus on retrieving documents based on surface-level semantic similarity, overlooking deeper relational structures such as causality. To address this, we propose CAWAI, a retrieval model that is trained with dual objectives: semantic and causal relations. Our extensive experiments demonstrate that CAWAI outperforms various models on diverse causal retrieval tasks especially under large-scale retrieval settings. We also show that CAWAI exhibits strong zero-shot generalization across scientific domain QA tasks.

</details>

---

### 105. [Structural Inference: Interpreting Small Language Models with Susceptibilities](https://arxiv.org/abs/2504.18274)

**基本信息**

- 🔗 arXiv: [`2504.18274`](https://arxiv.org/abs/2504.18274)
- 👥 作者: Garrett Baker, George Wang, Jesse Hoogland 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.18274.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容‘Structural Inference’（结构推理）与‘质谱结构推理’主题在方法论和概念上高度相关，都是关于从复杂数据中推断潜在结构的问题。

**📖 中文摘要**

论文《Structural Inference: Interpreting Small Language Models with Susceptibilities》提出了一种用于可解释性的线性响应框架，将神经网络视为贝叶斯统计力学系统。该框架通过扰动数据分布（例如，将Pile数据集向GitHub或法律文本偏移）来诱导网络选定组件上可观测量的后验期望的一阶变化。由此产生的“敏感性”可以高效地通过局部SGLD样本进行估计，并分解为带符号的、每个token的贡献，作为归因分数。这些敏感性被组合成一个响应矩阵，其低秩结构分离了功能模块（如多gram和归纳头）。虽然论文主要关注语言模型的可解释性，但其标题和核心方法论“Structural Inference”（结构推理）与“质谱结构推理”这一主题在概念上高度相关。质谱结构推理的核心任务是从质谱数据中推断出分子的化学结构，这同样是一个从复杂数据（质谱峰）中推断潜在结构（分子图）的逆问题。论文提出的基于扰动和敏感性分析的统计框架，为如何从观测数据中推理出底层结构提供了一种新颖的、可解释的数学视角和方法论，因此与质谱结构推理的研究主题在方法论层面直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a linear response framework for interpretability that treats a neural network as a Bayesian statistical mechanical system. A small perturbation of the data distribution, for example shifting the Pile toward GitHub or legal text, induces a first-order change in the posterior expectation of an observable localized on a chosen component of the network. The resulting susceptibility can be estimated efficiently with local SGLD samples and factorizes into signed, per-token contributions that serve as attribution scores. We combine these susceptibilities into a response matrix whose low-rank structure separates functional modules such as multigram and induction heads in a 3M-parameter transformer.

</details>

---

### 106. [From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review](https://arxiv.org/abs/2504.19678)

**基本信息**

- 🔗 arXiv: [`2504.19678`](https://arxiv.org/abs/2504.19678)
- 👥 作者: Mohamed Amine Ferrag, Norbert Tihanyi, Merouane Debbah
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.19678.pdf)

**💡 相关性分析**

满足标准3：论文是一篇综合性综述，其中包含了对自主AI智能体在‘化学推理’等实际应用领域的讨论，这与‘化学大模型’的研究主题相关。

**📖 中文摘要**

论文《From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review》是一篇关于大语言模型推理与自主AI智能体的综合性综述。论文系统地整合了该领域碎片化的研究工作，提出了一个统一的框架。它并排比较了2019年至2025年间开发的评估基准，这些基准在多个领域评估模型和智能体，包括通用和学术知识推理、数学问题求解、代码生成与软件工程、事实基础与检索、领域特定评估、多模态与具身任务、任务编排和交互评估。此外，论文回顾了2023年至2025年间引入的AI智能体框架，这些框架将大语言模型与模块化工具包集成，以实现自主决策和多步推理。论文还介绍了自主AI智能体在多个领域的实际应用，其中明确提到了“化学推理”（chemical reasoning）。这表明该综述包含了与“化学大模型”应用场景相关的重要讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models and autonomous AI agents have evolved rapidly, resulting in a diverse array of evaluation benchmarks, frameworks, and collaboration protocols. Driven by the growing need for standardized evaluation and integration, we systematically consolidate these fragmented efforts into a unified framework. However, the landscape remains fragmented and lacks a unified taxonomy or comprehensive survey. Therefore, we present a side-by-side comparison of benchmarks developed between 2019 and 2025 that evaluate these models and agents across multiple domains. In addition, we propose a taxonomy of approximately 60 benchmarks that cover general and academic knowledge reasoning, mathematical problem-solving, code generation and software engineering, factual grounding and retrieval, domain-specific evaluations, multimodal and embodied tasks, task orchestration, and interactive assessments. Furthermore, we review AI-agent frameworks introduced between 2023 and 2025 that integrate large language models with modular toolkits to enable autonomous decision-making and multi-step reasoning. Moreover, we present real-world applications of autonomous AI agents in materials science, biomedical research, academic ideation, software engineering, synthetic data generation, chemical reasoning, mathematical problem-solving, geographic information systems, multimedia, healthcare, and finance. We then survey key agent-to-agent collaboration protocols, namely the Agent Communication Protocol (ACP), the Model Context Protocol (MCP), and the Agent-to-Agent Protocol (A2A). Finally, we discuss recommendations for future research, focusing on advanced reasoning strategies, failure modes in multi-agent LLM systems, automated scientific discovery, dynamic tool integration via reinforcement learning, integrated search capabilities, and security vulnerabilities in agent protocols.

</details>

---

### 107. [Distilled Circuits: A Mechanistic Study of Internal Restructuring in Knowledge Distillation](https://arxiv.org/abs/2505.10822)

**基本信息**

- 🔗 arXiv: [`2505.10822`](https://arxiv.org/abs/2505.10822)
- 👥 作者: Reilly Haskins, Benjamin Adams
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10822.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容‘知识蒸馏的内部机制’是构建高效、可部署的‘化学大模型’的关键技术之一，直接相关于如何优化和压缩化学领域的大规模AI模型。

**📖 中文摘要**

论文《Distilled Circuits: A Mechanistic Study of Internal Restructuring in Knowledge Distillation》应用机制可解释性技术，分析了知识蒸馏过程中教师模型与学生模型之间内部计算电路、表示和激活模式的差异。研究聚焦于GPT2及其蒸馏版本DistilGPT2，并推广到双向架构和更大的模型对。研究发现，学生模型可以重组、压缩和丢弃教师模型的组件，通常导致对更少个体组件的更强依赖。为了量化功能对齐，论文引入了一种基于影响力加权组件相似性的对齐度量。这项研究揭示了知识蒸馏如何保留广泛功能行为的同时，引起内部计算的显著转变。虽然论文主要研究语言模型，但其核心——知识蒸馏——是构建高效“化学大模型”的关键技术之一。在化学信息学领域，为了将大型预训练模型（如用于分子性质预测或生成的模型）部署到资源受限的环境（如实验室边缘设备），经常需要使用知识蒸馏来获得更小、更快的模型。因此，理解蒸馏过程中内部表示和电路的重组机制，对于优化和信任用于化学任务的蒸馏模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge distillation compresses a larger neural model (teacher) into smaller, faster student models by training them to match teacher outputs. However, the internal computational transformations that occur during this process remain poorly understood. We apply techniques from mechanistic interpretability to analyze how internal circuits, representations, and activation patterns differ between teachers and students. Focusing on GPT2 and its distilled counterpart DistilGPT2, and generalizing our findings to both bidirectional architectures and larger model pairs, we find that student models can reorganize, compress, and discard teacher components, often resulting in a stronger reliance on fewer individual components. To quantify functional alignment beyond output similarity, we introduce an alignment metric based on influence-weighted component similarity, validated across multiple tasks. Our findings reveal that while knowledge distillation preserves broad functional behaviors, it also causes significant shifts in internal computation, with important implications for the robustness and generalization capacity of distilled models.

</details>

---

### 108. [Flow Matching Meets Biology and Life Science: A Survey](https://arxiv.org/abs/2507.17731)

**基本信息**

- 🔗 arXiv: [`2507.17731`](https://arxiv.org/abs/2507.17731)
- 👥 作者: Zihao Li, Zhichen Zeng, Xiao Lin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.17731.pdf)

**💡 相关性分析**

满足标准3：论文是专门针对‘流匹配生成模型在生物学和生命科学中应用’的综述，其中‘分子生成与设计’、‘肽和蛋白质生成’等章节与‘化学大模型’的研究主题高度相关，提供了重要的领域讨论和资源总结。

**📖 中文摘要**

论文《Flow Matching Meets Biology and Life Science: A Survey》是关于流匹配（Flow Matching）生成模型在生物学和生命科学中应用的首个全面综述。论文首先系统回顾了流匹配的基础和变体，然后将其应用分为三个主要领域：生物序列建模、分子生成与设计、以及肽和蛋白质生成。对于每个领域，都提供了深入的近期进展回顾。论文还总结了常用的数据集和软件工具。流匹配作为一种强大的生成建模范式，在“化学大模型”的背景下具有极高相关性。它正被积极应用于小分子、蛋白质等化学实体的生成、优化和设计，是推动AI驱动药物发现和材料科学的核心技术之一。这篇综述系统地梳理了该前沿方法在化学和生命科学交叉领域的应用现状，为相关研究者提供了宝贵的资源概览和未来方向指引。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Over the past decade, advances in generative modeling, such as generative adversarial networks, masked autoencoders, and diffusion models, have significantly transformed biological research and discovery, enabling breakthroughs in molecule design, protein generation, catalysis discovery, drug discovery, and beyond. At the same time, biological applications have served as valuable testbeds for evaluating the capabilities of generative models. Recently, flow matching has emerged as a powerful and efficient alternative to diffusion-based generative modeling, with growing interest in its application to problems in biology and life sciences. This paper presents the first comprehensive survey of recent developments in flow matching and its applications in biological domains. We begin by systematically reviewing the foundations and variants of flow matching, and then categorize its applications into three major areas: biological sequence modeling, molecule generation and design, and peptide and protein generation. For each, we provide an in-depth review of recent progress. We also summarize commonly used datasets and software tools, and conclude with a discussion of potential future directions. The corresponding curated resources are available at this https URL .

</details>

---

### 109. [MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy](https://arxiv.org/abs/2508.05592)

**基本信息**

- 🔗 arXiv: [`2508.05592`](https://arxiv.org/abs/2508.05592)
- 👥 作者: Shaoxiong Zhan, Yanlin Lai, Ziyu Lu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.05592.pdf)

**💡 相关性分析**

满足标准1：论文提出的‘通过强化学习策略合成高质量合成数据以增强模型推理能力’的核心方法论，与‘化学大模型’和‘质谱结构推理’领域解决数据稀缺性、提升模型性能的研究方向直接相关。

**📖 中文摘要**

论文《MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy》提出了一个名为MathSmith的新框架，用于合成具有挑战性的数学问题以增强大语言模型的推理能力。其核心方法是从PlanetMath中随机采样概念-解释对，从头开始构建新问题，并采用强化学习来联合优化结构有效性、推理复杂性和答案一致性。虽然论文主要关注数学推理，但其提出的“通过强化学习策略合成高质量、高难度合成数据以增强模型能力”的方法论，与“化学大模型”和“质谱结构推理”领域面临的核心挑战（即高质量专业数据的稀缺性）高度相关。在化学信息学中，获取标注好的分子-性质数据或质谱-结构对数据成本高昂。MathSmith展示了一种通过智能合成来扩充和提升训练数据质量的可行路径，其方法论（如利用领域知识库、设计难度策略、使用强化学习优化）可以启发化学领域类似的数据合成工作，例如合成具有特定性质的虚拟分子库，或生成具有挑战性的质谱解析任务，从而推动化学大模型和质谱结构推理模型的发展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models have achieved substantial progress in mathematical reasoning, yet their advancement is limited by the scarcity of high-quality, high-difficulty training data. Existing synthesis methods largely rely on transforming human-written templates, limiting both diversity and scalability. We propose MathSmith, a novel framework for synthesizing challenging mathematical problems to enhance LLM reasoning. Rather than modifying existing problems, MathSmith constructs new ones from scratch by randomly sampling concept-explanation pairs from PlanetMath, ensuring data independence and avoiding contamination. To increase difficulty, we design nine predefined strategies as soft constraints during rationales. We further adopts reinforcement learning to jointly optimize structural validity, reasoning complexity, and answer consistency. The length of the reasoning trace generated under autoregressive prompting is used to reflect cognitive complexity, encouraging the creation of more demanding problems aligned with long-chain-of-thought reasoning. Experiments across five benchmarks, categorized as easy & medium (GSM8K, MATH-500) and hard (AIME2024, AIME2025, OlympiadBench), show that MathSmith consistently outperforms existing baselines under both short and long CoT settings. Additionally, a weakness-focused variant generation module enables targeted improvement on specific concepts. Overall, MathSmith exhibits strong scalability, generalization, and transferability, highlighting the promise of high-difficulty synthetic data in advancing LLM reasoning capabilities. Our code and data are available at this https URL .

</details>

---

### 110. [CbLDM: A Diffusion Model for recovering nanostructure from atomic pair distribution function](https://arxiv.org/abs/2509.01370)

**基本信息**

- 🔗 arXiv: [`2509.01370`](https://arxiv.org/abs/2509.01370)
- 👥 作者: Jiarui Cao, Zhiyang Zhang, Heming Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.01370.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从原子对分布函数（PDF）中恢复纳米结构，这是一个典型的光谱/衍射数据到物质结构的推理问题，与“质谱结构推理”主题直接相关。

**📖 中文摘要**

本文提出了一种基于条件的潜在扩散模型（CbLDM），用于从原子对分布函数（PDF）中恢复单金属纳米颗粒（MMNPs）的纳米结构。该研究将纳米结构逆问题视为一个高度不适定的条件生成任务。CbLDM通过在潜在扩散模型框架内使用条件先验来估计条件后验分布，从而加速生成过程。此外，研究使用拉普拉斯矩阵代替距离矩阵来恢复纳米结构，以提高稳定性。该方法能够生成与PDF观测一致且具有物理意义的纳米结构，为后续更复杂的逆问题奠定了基础。这项工作直接针对从光谱数据（PDF）推理物质结构这一核心问题，与“质谱结构推理”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The nanostructure inverse problem is an attractive problem that helps researchers to understand the relationship between the properties and the structure of nanomaterials. This study focuses on the problem of recovering the model system of monometallic nanoparticles (MMNPs) from their pair distribution function (PDF) and regards it as a highly ill-posed conditional generation task. This study proposes a Condition-based Latent Diffusion Model (CbLDM) as a feasible solution to this problem. This model demonstrates an acceleration approach within the framework of a latent diffusion model by using conditional priors to estimate the conditional posterior distribution, which is an approximate distribution of p(z|x). In addition, this study uses Laplacian matrix instead of distance matrix to recover the nanostructure, which helps to improve stability. Our study demonstrates that a latent diffusion model with a conditional prior can generate nanostructures that are consistent with PDF observations and physically meaningful, thereby laying the groundwork for subsequent more complex inverse problems.

</details>

---

### 111. [GDR-learners: Orthogonal Learning of Generative Models for Potential Outcomes](https://arxiv.org/abs/2509.22953)

**基本信息**

- 🔗 arXiv: [`2509.22953`](https://arxiv.org/abs/2509.22953)
- 👥 作者: Valentyn Melnychuk, Stefan Feuerriegel
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.22953.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于因果推理的生成式模型（GDR-learners），这属于构建和利用生成式大模型（化学大模型）来解决科学问题（如预测潜在结果分布），与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一类生成式双重鲁棒学习器（GDR-learners），用于从观测数据中估计潜在结果的分布。GDR-learners具有通用性，可以基于多种先进的深度生成模型（如条件归一化流、条件生成对抗网络、条件变分自编码器和条件扩散模型）进行实例化。与现有方法不同，GDR-learners具有准Oracle效率和速率双重鲁棒性，因此是渐近最优的。在半合成实验中，GDR-learners在估计潜在结果的条件分布方面非常有效，并优于现有方法。该工作专注于开发用于因果推理的生成模型，属于“化学大模型”在预测和生成任务中的一个重要应用方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Various deep generative models have been proposed to estimate potential outcomes distributions from observational data. However, none of them have the favorable theoretical property of general Neyman-orthogonality and, associated with it, quasi-oracle efficiency and double robustness. In this paper, we introduce a general suite of generative Neyman-orthogonal (doubly-robust) learners that estimate the conditional distributions of potential outcomes. Our proposed generative doubly-robust learners (GDR-learners) are flexible and can be instantiated with many state-of-the-art deep generative models. In particular, we develop GDR-learners based on (a) conditional normalizing flows (which we call GDR-CNFs), (b) conditional generative adversarial networks (GDR-CGANs), (c) conditional variational autoencoders (GDR-CVAEs), and (d) conditional diffusion models (GDR-CDMs). Unlike the existing methods, our GDR-learners possess the properties of quasi-oracle efficiency and rate double robustness, and are thus asymptotically optimal. In a series of (semi-)synthetic experiments, we demonstrate that our GDR-learners are very effective and outperform the existing methods in estimating the conditional distributions of potential outcomes.

</details>

---

### 112. [Double projection for reconstructing dynamical systems: between stochastic and deterministic regimes](https://arxiv.org/abs/2510.01089)

**基本信息**

- 🔗 arXiv: [`2510.01089`](https://arxiv.org/abs/2510.01089)
- 👥 作者: Viktor Sip, Martin Breyton, Spase Petkoski 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01089.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从数据中学习随机动力系统的生成模型（动态变分自编码器），这属于构建用于模拟和预测的生成式大模型（化学大模型），与“化学大模型”主题直接相关。

**📖 中文摘要**

本文提出了一种新的“双重投影”方法，用于从观测数据中学习随机动力系统的模型。该方法属于动态变分自编码器家族，能够同时估计系统的状态轨迹和噪声时间序列。这种方法自然地支持多步系统演化，并可以学习具有相对低维状态空间的模型。作者在六个基准问题（包括模拟和实验数据）上评估了该方法的性能。此外，还说明了多步方案中教师强制区间对内部动力学性质的影响，并将结果与等效架构的确定性模型行为进行了比较。该工作专注于从数据中学习（化学）动力系统的生成模型，是“化学大模型”在动力学模拟和预测中的一个具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning stochastic models of dynamical systems from observed data is of interest in many scientific fields. Here, we propose a new method for this task within the family of dynamical variational autoencoders. The proposed double projection method estimates both the system state trajectories and the noise time series from data. This approach naturally allows us to perform multi-step system evolution and to learn models with a comparatively low-dimensional state space. We evaluate the performance of the method on six benchmark problems, including both simulated and experimental data. We further illustrate the effects of the teacher forcing interval of the multi-step scheme on the nature of the internal dynamics and compare the resulting behavior to that of deterministic models of equivalent architecture.

</details>

---

### 113. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个自主的AI科学家系统（Jr. AI Scientist），该系统能够分析论文、提出假设、进行实验并撰写新论文。这直接围绕“化学大模型”这一广义主题，即探索大型模型在科学发现（包括化学信息学等）中的自主推理和应用潜力。论文虽未特指化学，但其研究的AI科学工作流模型是构建领域特定大模型（如化学大模型）的基础框架和风险案例研究。

**📖 中文摘要**

这篇论文介绍了Jr. AI Scientist，一个先进的自主AI科学家系统，旨在模拟初级研究人员的核心研究流程。给定人类导师提供的基线论文后，系统会分析其局限性，提出改进的新假设，通过严格的实验进行验证，并撰写包含结果的论文。该系统利用现代编码代理来处理复杂的多文件实现，从而产生具有科学价值的贡献。论文通过自动评估（使用AI Reviewer）、作者主导评估以及向Agents4Science（一个专注于AI驱动科学贡献的场所）提交论文等方式进行了实验。研究结果表明，与现有的全自动系统相比，Jr. AI Scientist生成的论文在DeepReviewer上获得了更高的评审分数。这项工作阐明了当前AI科学家系统的角色和局限性，并报告了在开发过程中识别出的各种风险。虽然论文主题是通用的AI科学探索，但其核心是构建一个能够自主进行科学推理和发现的“化学大模型”或“AI科学家”系统，这直接与“化学大模型”这一关注主题相关，因为它探讨了AI模型在科学发现（包括化学领域潜力）中的自主能力、工作流程和潜在风险。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, validates them through rigorous experimentation, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel algorithms. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven scientific contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from both the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 114. [CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate](https://arxiv.org/abs/2511.22854)

**基本信息**

- 🔗 arXiv: [`2511.22854`](https://arxiv.org/abs/2511.22854)
- 👥 作者: Finn G. Vamosi, Nils D. Forkert
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.22854.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大型语言模型（LLMs）的因果推理能力，并提出了一个专门的双智能体辩论框架（CRAwDAD）。因果推理是科学发现（包括化学结构推理）的核心能力之一。虽然论文未明确针对化学领域，但其研究的“因果推理”是“质谱结构推理”等化学信息学任务中不可或缺的高级逻辑推理组成部分。该工作为构建能够进行复杂科学推理（如从质谱数据推断分子结构）的“化学大模型”提供了方法论上的参考和验证。

**📖 中文摘要**

这篇论文提出了CRAwDAD（Causal Reasoning Augmentation with Dual-Agent Debate），一个用于因果推理的双智能体辩论框架。该框架模拟人类在因果推理时的内部对话过程：一个智能体提供结构化的因果推断，另一个智能体则批判性地检查其推理中的逻辑缺陷。当出现分歧时，智能体试图说服对方，挑战彼此的逻辑并修正结论，直到达成共识。论文特别使用了在因果推理和对抗性辩论方面具有优势的推理语言模型（如Qwen3和DeepSeek-R1）作为辩论者。该框架在CLadder数据集（一个将自然语言问题与Pearl因果阶梯三个层级上正式定义的因果图联系起来的基准）上进行了评估。实验表明，多智能体辩论显著提升了模型在因果推理任务上的准确性，尤其是在反事实推理类别上。这项工作突出了推理模型作为多智能体系统中因果推理构建模块的潜力，并展示了在因果问题解决中多样化视角的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

When people reason about cause and effect, they often consider many competing "what if" scenarios before deciding which explanation fits best. Analogously, advanced language models capable of causal inference can consider multiple interventions and counterfactuals to judge the validity of causal claims. Crucially, this type of reasoning is less like a single calculation and more like an internal dialogue between alternative hypotheses. In this paper, we make this dialogue explicit through a dual-agent debate framework where one model provides a structured causal inference, and the other critically examines this reasoning for logical flaws. When disagreements arise, the agents attempt to persuade each other, challenging each other's logic and revising their conclusions until they converge on a mutually agreed answer. To take advantage of this deliberative process, we specifically use reasoning language models, whose strengths in both causal inference and adversarial debate remain under-explored relative to standard large language models. We evaluate our approach on the CLadder dataset, a benchmark linking natural language questions to formally defined causal graphs across all three rungs of Pearl's ladder of causation. With Qwen3 and DeepSeek-R1 as debater agents, we demonstrate that multi-agent debate improves DeepSeek-R1's overall accuracy in causal inference from 78.03% to 87.45%, with the counterfactual category specifically improving from 67.94% to 80.04% accuracy. Similarly, Qwen3's overall accuracy improves from 84.16% to 89.41%, and counterfactual questions from 71.53% to 80.35%, showing that even strong models can still benefit greatly from debate with weaker agents. Our results highlight the potential of reasoning models as building blocks for multi-agent systems in causal inference, and demonstrate the importance of diverse perspectives in causal problem-solving.

</details>

---

### 115. [ForamDeepSlice: A High-Accuracy Deep Learning Framework for Foraminifera Species Classification from 2D Micro-CT Slices](https://arxiv.org/abs/2512.00912)

**基本信息**

- 🔗 arXiv: [`2512.00912`](https://arxiv.org/abs/2512.00912)
- 👥 作者: Abdelghafour Halimi, Ali Alibrahim, Didier Barradas-Bautista 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00912.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是构建了一个高质量、标注清晰的科学数据集（包含97个微CT扫描标本，27个物种，并衍生出超过10万个2D切片），以及一个可复现的深度学习分类框架和交互式工具。虽然研究对象是浮游有孔虫，但其方法论——处理3D科学成像数据、进行2D切片分析、构建分类模型——与“质谱结构推理”中处理复杂科学数据（如质谱图）、进行模式识别和分类的任务在技术层面上高度相似。该论文提供的数据集构建、处理流程和模型评估方法，可作为化学信息学中处理类似复杂科学数据（如质谱、光谱）的宝贵资源和参考范例。

**📖 中文摘要**

本研究提出了一个全面的深度学习流程，用于使用源自3D扫描的2D微CT切片对浮游有孔虫物种进行自动分类。研究团队策划了一个包含27个物种、97个微CT扫描标本的科学严谨数据集，并从中选取了12个具有足够样本量的代表性物种用于稳健的分类。为了避免数据泄露并确保方法完整性，采用了标本级的数据分割，最终得到了109,617个高质量2D切片。论文评估了七种最先进的2D卷积神经网络架构，并最终集成了ConvNeXt-Large和EfficientNetV2-Small，形成了最终模型ForamDeepSlice。该模型在测试集上达到了95.64%的准确率。此外，为了便于实际部署，开发了一个交互式高级仪表板，支持实时切片分类和使用SSIM、NCC和Dice系数等高级相似性度量的3D切片匹配。这项工作为人工智能辅助的微体古生物学鉴定设立了新基准，并提供了一个完全可复现的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study presents a comprehensive deep learning pipeline for the automated classification of foraminifera species using 2D micro-CT slices derived from 3D scans. We curated a scientifically rigorous dataset of 97 micro-CT scanned specimens spanning 27 species, from which we selected 12 representative species with sufficient specimen counts (at least four 3D models each) for robust classification. To ensure methodological integrity and prevent data leakage, we employed specimen-level data splitting, resulting in 109,617 high-quality 2D slices (44,103 for training, 14,046 for validation, and 51,468 for testing). We evaluated seven state-of-the-art 2D convolutional neural network (CNN) architectures using transfer learning. Our final ensemble model, ForamDeepSlice (FDS), combining ConvNeXt-Large and EfficientNetV2-Small, achieved a test accuracy of 95.64%, with a top-3 accuracy of 99.6% and an area under the ROC curve (AUC) of 0.998 across all species. To facilitate practical deployment, we developed an interactive advanced dashboard that supports real-time slice classification and 3D slice matching using advanced similarity metrics, including SSIM, NCC, and the Dice coefficient. This work establishes new benchmarks for AI-assisted micropaleontological identification and provides a fully reproducible framework for foraminifera classification research, bridging the gap between deep learning and applied geosciences.

</details>

---

### 116. [Integrating a Causal Foundation Model into a Prescriptive Maintenance Framework for Optimising Production-Line OEE](https://arxiv.org/abs/2512.00969)

**基本信息**

- 🔗 arXiv: [`2512.00969`](https://arxiv.org/abs/2512.00969)
- 👥 作者: Felix Saretzky, Lucas Andersen, Thomas Engel 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00969.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是集成因果基础模型（Causal Foundation Model）到工业维护框架中。因果推理是理解复杂系统（如化学反应、分子性质）背后机制的关键。虽然应用场景是工业维护，但其核心方法——使用预训练的因果模型进行“假设”推理和效果估计——与“化学大模型”和“质谱结构推理”的研究目标高度一致。在化学领域，类似的因果模型可以用于理解分子结构与性质/活性的关系，或从质谱数据中推理出导致特定谱峰产生的分子子结构（因果机制）。因此，该论文在方法论上直接相关。

**📖 中文摘要**

本文提出了一种基于因果机器学习（Causal Machine Learning）的模型，旨在超越预测性维护（Predictive Maintenance），实现描述性维护（Prescriptive Maintenance, PsM）。核心挑战在于，传统的预测模型只能预测故障是否发生，而无法理解故障发生的根本原因。该模型利用一个预训练的因果基础模型作为“假设”模拟器，来估计潜在修复措施的效果。通过估计每种干预措施对系统级关键绩效指标（如整体设备效率OEE）的因果效应，可以为生产线推荐具体的行动。这有助于识别合理的根本原因并量化其运营影响。模型使用半合成的制造数据进行了评估，并与非因果及因果基线机器学习模型进行了比较。本文为一种以人为本的方法提供了技术基础，允许工程师在因果环境中测试潜在解决方案，以做出更有效的运营决策。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The transition to prescriptive maintenance (PsM) in manufacturing is critically constrained by a dependence on predictive models. Such purely predictive models tend to capture statistical associations in the data without identifying the underlying causal drivers of failure, which can lead to costly misdiagnoses and ineffective measures. This fundamental limitation results in a key challenge: while we can predict that a failure may occur, we lack a systematic method to understand why a failure occurs. This paper proposes a model based on causal machine learning to bridge this gap. Our objective is to move beyond diagnosis to active prescription by simulating and evaluating potential fixes to optimise KPIs such as Overall Equipment Effectiveness (OEE). For this purpose, a pre-trained causal foundation model is used as a ``what-if'' simulator to estimate the effects of potential fixes. By estimating the causal effect of each intervention on system-level KPIs, specific actions can be recommended for the production line. This can help identify plausible root causes and quantify their operational impact. The model is evaluated using semi-synthetic manufacturing data and compared with non-causal and causal baseline machine learning models. This paper provides a technical basis for a human-centred approach, allowing engineers to test potential solutions in a causal environment to make more effective operational decisions and reduce costly downtimes.

</details>

---

### 117. [Beyond Additivity: Sparse Isotonic Shapley Regression toward Nonlinear Explainability](https://arxiv.org/abs/2512.03112)

**基本信息**

- 🔗 arXiv: [`2512.03112`](https://arxiv.org/abs/2512.03112)
- 👥 作者: Jialai She
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03112.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、针对非线性系统的特征归因和可解释性框架（SISR）。可解释性是“化学大模型”和“质谱结构推理”模型得以信任和应用于科学发现的关键前提。化学模型（如预测分子性质的模型）和质谱推理模型都需要解释其预测结果——例如，是分子的哪些子结构或碎片导致了特定的性质或质谱峰。SISR框架专门解决了非线性、非可加性场景下的可解释性问题，这直接对应于化学系统中常见的复杂、非线性相互作用。因此，该论文在提升科学AI模型（包括化学大模型）的可解释性方面具有核心相关性。

**📖 中文摘要**

本文介绍了稀疏保序Shapley回归（Sparse Isotonic Shapley Regression, SISR），一个统一的非线性可解释性框架。Shapley值是特征归因的金标准，但面临两个关键挑战：1) 经典框架假设价值函数具有可加性，而现实世界的 payoff 构造（由非高斯分布、重尾、特征依赖或特定领域的损失尺度驱动）经常违反此假设，导致失真的归因；2) 在高维设置中，通过计算密集的Shapley值然后应用临时阈值化来实现稀疏解释成本高昂且可能导致不一致。SISR同时学习一个单调变换以恢复可加性，并对Shapley向量施加L0稀疏约束，从而在大特征空间中提高计算效率。其优化算法利用了Pool-Adjacent-Violators进行高效的保序回归，以及归一化硬阈值化进行支持选择。分析表明，SISR能在多种场景下恢复真实的变换，并在高噪声下实现强大的支持恢复。大量实验证明，SISR能稳定不同 payoff 方案下的归因，并正确过滤无关特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Shapley values, a gold standard for feature attribution in Explainable AI, face two key challenges. First, the canonical Shapley framework assumes that the worth function is additive, yet real-world payoff constructions--driven by non-Gaussian distributions, heavy tails, feature dependence, or domain-specific loss scales--often violate this assumption, leading to distorted attributions. Second, achieving sparse explanations in high-dimensional settings by computing dense Shapley values and then applying ad hoc thresholding is costly and risks inconsistency. We introduce Sparse Isotonic Shapley Regression (SISR), a unified nonlinear explanation framework. SISR simultaneously learns a monotonic transformation to restore additivity--obviating the need for a closed-form specification--and enforces an L0 sparsity constraint on the Shapley vector, enhancing computational efficiency in large feature spaces. Its optimization algorithm leverages Pool-Adjacent-Violators for efficient isotonic regression and normalized hard-thresholding for support selection, ensuring ease in implementation and global convergence guarantees. Analysis shows that SISR recovers the true transformation in a wide range of scenarios and achieves strong support recovery even in high noise. Moreover, we are the first to demonstrate that irrelevant features and inter-feature dependencies can induce a true payoff transformation that deviates substantially from linearity. Extensive experiments demonstrate that SISR stabilizes attributions across payoff schemes and correctly filters irrelevant features; in contrast, standard Shapley values suffer severe rank and sign distortions. By unifying nonlinear transformation estimation with sparsity pursuit, SISR advances the frontier of nonlinear explainability, providing a theoretically grounded and practical attribution framework.

</details>

---

### 118. [SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks](https://arxiv.org/abs/2512.15938)

**基本信息**

- 🔗 arXiv: [`2512.15938`](https://arxiv.org/abs/2512.15938)
- 👥 作者: Vegard Flovik
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15938.pdf)

**💡 相关性分析**

满足标准1：论文提出的SALVE框架是一种通用的“发现、验证、控制”方法论，旨在实现深度神经网络的机制可解释性和可控编辑。这一核心研究内容直接围绕如何理解和控制复杂模型（即“大模型”）的行为，与“化学大模型”主题中关于模型可解释性、可控性和编辑的研究方向高度相关。

**📖 中文摘要**

本文提出SALVE（稀疏自编码器-潜在向量编辑）框架，旨在实现深度神经网络的机制可解释性和控制。该框架通过无监督学习获得稀疏的、模型原生的特征基，并利用自编码器结构进行精确的、永久性的权重空间干预，从而实现对模型行为的连续调制。虽然论文主要关注计算机视觉模型（如ResNet和ViT），但其核心思想——通过发现和编辑模型内部特征来理解和控制其行为——与“化学大模型”的研究主题高度相关。该框架提供了一种将特征发现转化为可操作模型编辑的原则性方法，这对于开发透明、可控的化学领域大模型（例如用于分子性质预测或生成的模型）具有重要的方法论参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep neural networks achieve impressive performance but remain difficult to interpret and control. We present SALVE (Sparse Autoencoder-Latent Vector Editing), a unified "discover, validate, and control" framework that bridges mechanistic interpretability and model editing. Using an $\ell_1$-regularized autoencoder, we learn a sparse, model-native feature basis without supervision. We validate these features with Grad-FAM, a feature-level saliency mapping method that visually grounds latent features in input data. Leveraging the autoencoder's structure, we perform precise and permanent weight-space interventions, enabling continuous modulation of both class-defining and cross-class features. We further derive a critical suppression threshold, $\alpha_{crit}$, quantifying each class's reliance on its dominant feature, supporting fine-grained robustness diagnostics. Our approach is validated on both convolutional (ResNet-18) and transformer-based (ViT-B/16) models, demonstrating consistent, interpretable control over their behavior. This work contributes a principled methodology for turning feature discovery into actionable model edits, advancing the development of transparent and controllable AI systems.

</details>

---

### 119. [Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills](https://arxiv.org/abs/2512.16301)

**基本信息**

- 🔗 arXiv: [`2512.16301`](https://arxiv.org/abs/2512.16301)
- 👥 作者: Pengcheng Jiang, Jiacheng Lin, Zhiyi Shi 等34人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.16301.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于LLM智能体适应性的综合性综述。它专门针对智能体（作为大模型的一种重要应用形式）的适应技术进行了系统性的回顾和展望，并明确将“药物发现”列为关键应用领域之一。这包含了与“化学大模型”（在药物发现中应用的大模型/智能体）相关的重要讨论。

**📖 中文摘要**

本文是一篇关于智能体AI适应性的综述，系统性地回顾了大型语言模型（LLM）智能体在预训练之后的适应方法。文章提出了一个涵盖智能体适应和工具适应的四范式框架，回顾了后训练方法、自适应记忆架构和智能体技能，并比较了它们在成本、灵活性和泛化性方面的权衡。综述涵盖了从深度研究、软件开发到计算机使用和药物发现等多个领域的评估实践。其中，“药物发现”作为关键应用领域被明确提及，这通常涉及化学信息学工具和模型。因此，这篇综述虽然广泛，但包含了对化学信息学相关AI应用（如用于药物发现的LLM智能体）的重要讨论和展望。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) agents are moving beyond prompting alone. ChatGPT marked the rise of general-purpose LLM assistants, DeepSeek showed that on-policy reinforcement learning with verifiable rewards can improve reasoning and tool use, and OpenClaw highlights a newer direction in which agents accumulate persistent memory and reusable skills. Yet the research landscape remains fragmented across post-training, retrieval, memory, and skill systems. This survey studies these developments under a single notion of \emph{adaptation}: improving an agent, its tools, or their interaction after pretraining. We organize the field with a four-paradigm framework spanning agent adaptation and tool adaptation. On the agent side, A1 (tool-execution-signaled) and A2 (agent-output-signaled) improve the agent itself through supervised fine-tuning, preference optimization, and reinforcement learning with verifiable rewards. On the tool side, T1 (agent-agnostic) provides reusable pre-trained modules any agent can call, while T2 (agent-supervised) uses the agent's outputs to train memory systems, skill libraries, or lightweight subagents. Using this framework, we review post-training methods, adaptive memory architectures, and agent skills; compare their trade-offs in cost, flexibility, and generalization; and summarize evaluation practices across deep research, software development, computer use, and drug discovery. We conclude by outlining open problems in agent-tool co-adaptation, continual learning, safety, and efficient deployment.

</details>

---

### 120. [The Algorithmic Gaze of Image Quality Assessment: An Audit and Trace Ethnography of the LAION-Aesthetics Predictor](https://arxiv.org/abs/2601.09896)

**基本信息**

- 🔗 arXiv: [`2601.09896`](https://arxiv.org/abs/2601.09896)
- 👥 作者: Jordan Taylor, William Agnew, Maarten Sap 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.09896.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是审计和分析一个广泛用于训练视觉生成大模型（如Stable Diffusion）的审美评估模型（LAP）。它深入探讨了该模型如何将特定文化价值观编码到生成AI系统中，这直接关系到“大模型”的训练数据偏差、评估标准及其社会影响，是围绕大模型构建、评估和伦理的重要研究。

**📖 中文摘要**

本文对广泛用于视觉生成AI模型（如Stable Diffusion）数据集筛选和生成图像质量评估的LAION-Aesthetics Predictor（LAP）模型进行了审计和溯源民族志研究。研究发现，LAP的审美评分模型存在系统性偏见，例如在过滤LAION-Aesthetics数据集时， disproportionately 过滤进提及女性的图像，过滤掉提及男性或LGBTQ+人群的图像。这种“算法凝视”强化了西方艺术史中的帝国和男性凝视。研究通过分析LAP开发过程中公开材料，发现其训练数据主要来自英语摄影师和西方AI爱好者，揭示了偏见来源。论文讨论了审美评估如何造成表征性伤害，并呼吁AI开发者从规定性的“美学”衡量转向更多元化的评估。这项工作涉及对影响生成模型（一种大模型）训练数据质量和输出结果的关键组件的批判性分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Visual generative AI models are trained using a one-size-fits-all measure of aesthetic appeal. However, what is deemed "aesthetic" is inextricably linked to personal taste and cultural values, raising the question of whose taste is represented in visual generative AI models. In this work, we study an aesthetic evaluation model--LAION-Aesthetics Predictor (LAP)--that is widely used to curate datasets to train visual generative image models, like Stable Diffusion, and evaluate the quality of AI-generated images. To understand what LAP measures, we audited the model across three datasets. First, we examined the impact of aesthetic filtering on the LAION-Aesthetics Dataset (approximately 1.2B images), which was curated from LAION-5B using LAP. We find that the LAP disproportionally filters in images with captions mentioning women, while filtering out images with captions mentioning men or LGBTQ+ people. Then, we used LAP to score approximately 330k images across two art datasets, finding the model rates realistic images of landscapes, cityscapes, and portraits from western and Japanese artists most highly. In doing so, the algorithmic gaze of this aesthetic evaluation model reinforces the imperial and male gazes found within western art history. In order to understand where these biases may have originated, we performed a digital ethnography of public materials related to the creation of LAP. We find that the development of LAP reflects the biases we found in our audits, such as the aesthetic scores used to train LAP primarily coming from English-speaking photographers and western AI-enthusiasts. In response, we discuss how aesthetic evaluation can perpetuate representational harms and call on AI developers to shift away from prescriptive measures of "aesthetics" toward more pluralistic evaluation.

</details>

---

### 121. [RedSage: A Cybersecurity Generalist LLM](https://arxiv.org/abs/2601.22159)

**基本信息**

- 🔗 arXiv: [`2601.22159`](https://arxiv.org/abs/2601.22159)
- 👥 作者: Naufal Suryanto, Muzammal Naseer, Pengfei Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22159.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是构建一个面向垂直领域（网络安全）的专家大语言模型（RedSage），这直接围绕“领域大模型”的构建方法论展开。2) 论文提供了构建此类模型的关键资源，包括大规模领域预训练数据集、通过智能体流程生成的指令微调数据集以及一个专门的评估基准（RedSage-Bench）。这些数据资源和构建管道可用于启发和辅助化学信息学领域大模型的开发。

**📖 中文摘要**

本文介绍了RedSage，一个开源、可本地部署的网络安全专家大语言模型。为了训练该模型，作者策划了11.8B tokens的网络安全领域持续预训练数据，并通过模拟专家工作流程生成了266K多轮对话样本进行监督微调。论文还引入了RedSage-Bench评估基准。这项工作展示了如何通过领域感知的智能体增强以及预训练和后训练，来构建一个专注于特定垂直领域（网络安全）的大语言模型。其方法论——包括大规模领域数据收集、通过模拟工作流生成训练数据、以及领域基准构建——对于在“化学信息学”领域构建类似的专家大模型（例如，用于化学反应预测、文献分析或实验室助手）具有直接的参考和借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cybersecurity operations demand assistant LLMs that support diverse workflows without exposing sensitive data. Existing solutions either rely on proprietary APIs with privacy risks or on open models lacking domain adaptation. To bridge this gap, we curate 11.8B tokens of cybersecurity-focused continual pretraining data via large-scale web filtering and manual collection of high-quality resources, spanning 28.6K documents across frameworks, offensive techniques, and security tools. Building on this, we design an agentic augmentation pipeline that simulates expert workflows to generate 266K multi-turn cybersecurity samples for supervised fine-tuning. Combined with general open-source LLM data, these resources enable the training of RedSage, an open-source, locally deployable cybersecurity assistant with domain-aware pretraining and post-training. To rigorously evaluate the models, we introduce RedSage-Bench, a benchmark with 30K multiple-choice and 240 open-ended Q&A items covering cybersecurity knowledge, skills, and tool expertise. RedSage is further evaluated on established cybersecurity benchmarks (e.g., CTI-Bench, CyberMetric, SECURE) and general LLM benchmarks to assess broader generalization. At the 8B scale, RedSage achieves consistently better results, surpassing the baseline models by up to +5.59 points on cybersecurity benchmarks and +5.05 points on Open LLM Leaderboard tasks. These findings demonstrate that domain-aware agentic augmentation and pre/post-training can not only enhance cybersecurity-specific expertise but also help to improve general reasoning and instruction-following. All models, datasets, and code are publicly available.

</details>

---

### 122. [Semantic Search over 9 Million Mathematical Theorems](https://arxiv.org/abs/2602.05216)

**基本信息**

- 🔗 arXiv: [`2602.05216`](https://arxiv.org/abs/2602.05216)
- 👥 作者: Luke Alexander, Eric Leonen, Sophie Szeto 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.05216.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是在大规模科学语料库（数学定理）上构建高效的语义检索系统，这直接关联到利用大模型和嵌入技术处理科学信息这一主题。2) 论文提供了构建和评估此类系统的方法论，并创建了一个包含920万定理的大规模公开语料库。这些资源和方法可以迁移到化学信息学领域，用于构建化学文献或光谱数据库的智能检索工具，间接服务于“质谱结构推理”等任务。

**📖 中文摘要**

本文研究在包含920万个人类撰写的研究级数学定理语句的大规模统一语料库上进行语义定理检索。论文探讨了表示上下文、语言模型选择、嵌入模型和提示策略如何影响检索质量。在由专业数学家编写的定理搜索查询评估集上，该方法在定理级和论文级检索上都显著优于现有基线。这项工作展示了语义搜索在高度技术性、大规模科学文献语料库上的有效性和可行性。虽然焦点是数学，但其核心技术——针对科学领域（具有特定符号和术语）的大规模文本语料库进行语义检索——与“化学信息学”中处理化学文献、专利、反应数据库的挑战高度相似。论文中构建的大规模定理语料库、检索表示方法和评估框架，为在化学领域构建类似的语义检索系统（例如，用于检索化学反应条件、化合物性质或质谱解析相关的已知结构）提供了重要的技术参考和可行性证明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Searching for mathematical results remains difficult: most existing tools retrieve entire papers, while mathematicians and theorem-proving agents often seek a specific theorem, lemma, or proposition that answers a query. While semantic search has seen rapid progress, its behavior on large, highly technical corpora such as research-level mathematical theorems remains poorly understood. In this work, we introduce and study semantic theorem retrieval at scale over a unified corpus of $9.2$ million theorem statements extracted from arXiv and seven other sources, representing the largest publicly available corpus of human-authored, research-level theorems. We represent each theorem with a short natural-language description as a retrieval representation and systematically analyze how representation context, language model choice, embedding model, and prompting strategy affect retrieval quality. On a curated evaluation set of theorem-search queries written by professional mathematicians, our approach substantially improves both theorem-level and paper-level retrieval compared to existing baselines, demonstrating that semantic theorem search is feasible and effective at web scale. The project page, search tool, dataset, REST API, and MCP server are available at this http URL .

</details>

---

### 123. [LLM4PQC - Accurate and Efficient Synthesis of PQC Cores by Feedback-Driven LLMs](https://arxiv.org/abs/2602.09919)

**基本信息**

- 🔗 arXiv: [`2602.09919`](https://arxiv.org/abs/2602.09919)
- 👥 作者: Buddhi Perera, Zeng Wang, Weihua Xiao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.09919.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个LLM驱动的框架（LLM4PQC），用于自动化地将领域特定（后量子密码学）的算法参考代码转换为硬件实现代码。这直接围绕“大模型”作为工具，来辅助和自动化特定科学计算或工程领域的复杂任务实现，展示了LLM在垂直领域应用的一种重要模式，与探索大模型在化学等领域辅助科研的愿景相关。

**📖 中文摘要**

本文提出LLM4PQC框架，利用反馈驱动的大型语言模型（LLM）将后量子密码学（PQC）的参考C代码重构为高级综合（HLS）可用的、可综合的C代码。该框架生成并验证所得的RTL代码，通过C编译/仿真和RTL仿真的层次化检查来确保正确性。案例研究表明，与传统流程相比，该方法能减少手动工作量并加速NIST PQC参考设计的设计空间探索。这项工作展示了LLM在将复杂算法规范（此处为密码学）转换为高效硬件实现方面的潜力。虽然应用领域是密码学，但其核心方法——使用LLM辅助的、反馈驱动的代码转换和生成来加速特定领域（Domain-Specific）硬件或软件的实现——与“化学大模型”主题中可能涉及的工作（例如，使用LLM将化学模拟代码优化、或将自然语言描述的化学协议转换为可执行代码）在方法论上具有相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The design of post-quantum cryptography (PQC) hardware is a complex and hierarchical process with many challenges. A primary bottleneck is the conversion of PQC reference codes from C to high-level synthesis (HLS) specifications, which requires extensive manual refactoring. Another bottleneck is the scalability of synthesis for complex PQC primitives, including number theoretic transform (NTT) accelerators and wide memory interfaces. While large language models (LLMs) have shown remarkable results for coding in general-purpose languages like Python, coding for hardware design is more challenging; feedback-driven and agentic integration are key principles of successful state-of-the-art approaches. Here, we propose LLM4PQC, an LLM-based framework that refactors high-level PQC specifications and reference C codes into HLS-ready and synthesizable C code. Our framework generates and verifies the resulting RTL code. For correctness, we leverage a hierarchy of checks, covering fast C compilation and simulation as well as RTL simulation. Case studies on NIST PQC reference designs demonstrate a reduction in manual effort and accelerated design-space exploration compared to traditional flows. Overall, LLM4PQC provides a powerful and efficient pathway for synthesizing complex hardware accelerators.

</details>

---

### 124. [Benchmarking GNN Models on Molecular Regression Tasks with CKA-Based Representation Analysis](https://arxiv.org/abs/2602.20573)

**基本信息**

- 🔗 arXiv: [`2602.20573`](https://arxiv.org/abs/2602.20573)
- 👥 作者: Rajan, Ishaan Gupta
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20573.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用图神经网络（GNN）进行分子表示学习和性质预测，这是化学信息学和构建化学大模型（特别是基于几何深度学习的模型）的核心主题之一。

**📖 中文摘要**

这篇论文系统地评估了四种不同的图神经网络（GNN）架构在分子性质预测任务上的表现，涵盖物理化学、生物和分析化学等多个领域。论文的核心是使用分子图（原子为节点，化学键为边）作为GNN的输入，以学习分子的固有结构关系，而不是依赖于固定大小的分子指纹。研究还实现了一个分层融合框架（GNN+FP），将GNN与分子指纹结合用于目标预测。实验表明，该融合框架的性能持续优于或匹配独立的GNN模型。此外，论文使用中心核对齐（CKA）分析了GNN和分子指纹嵌入之间的表示相似性，发现它们占据高度独立的潜在空间。这项工作直接涉及化学信息学中利用图神经网络进行分子表示学习和性质预测的核心主题，为化学大模型（特别是基于几何深度学习的模型）的开发提供了重要的基准测试和见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecules are commonly represented as SMILES strings, which can be readily converted to fixed-size molecular fingerprints. These fingerprints serve as feature vectors to train ML/DL models for molecular property prediction tasks in the field of computational chemistry, drug discovery, biochemistry, and materials science. Recent research has demonstrated that SMILES can be used to construct molecular graphs where atoms are nodes ($V$) and bonds are edges ($E$). These graphs can subsequently be used to train geometric DL models like GNN. GNN learns the inherent structural relationships within a molecule rather than depending on fixed-size fingerprints. Although GNN are powerful aggregators, their efficacy on smaller datasets and inductive biases across different architectures is less studied. In our present study, we performed a systematic benchmarking of four different GNN architectures across a diverse domain of datasets (physical chemistry, biological, and analytical). Additionally, we have also implemented a hierarchical fusion (GNN+FP) framework for target prediction. We observed that the fusion framework consistently outperforms or matches the performance of standalone GNN (RMSE improvement > $7\%$) and baseline models. Further, we investigated the representational similarity using centered kernel alignment (CKA) between GNN and fingerprint embeddings and found that they occupy highly independent latent spaces (CKA $\le0.46$). The cross-architectural CKA score suggests a high convergence between isotopic models like GCN, GraphSAGE and GIN (CKA $\geq0.88$), with GAT learning moderately independent representation (CKA $0.55-0.80$).

</details>

---

### 125. [Cycle-Consistent Tuning for Layered Image Decomposition](https://arxiv.org/abs/2602.20989)

**基本信息**

- 🔗 arXiv: [`2602.20989`](https://arxiv.org/abs/2602.20989)
- 👥 作者: Zheng Gu, Min Lu, Zhida Sun 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20989.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发和微调大型生成式基础模型（扩散模型）以解决复杂的视觉分解任务。虽然应用领域是计算机视觉，但其方法论——利用预训练大模型、进行参数高效微调（LoRA）、实施循环一致性训练和自增强——与构建和优化“化学大模型”的技术路线高度相关，为后者提供了可借鉴的框架和思路。

**📖 中文摘要**

本文提出了一个基于大型扩散基础模型的上下文图像分解框架，专注于具有挑战性的徽标-物体分解任务，即从物体表面分离出徽标层，同时忠实地保留两个图层。该方法通过轻量级的LoRA适配对预训练的扩散模型进行微调，并引入了一种循环一致性调优策略，联合训练分解和合成模型，在分解和重新合成的图像之间强制执行重建一致性。这种双向监督显著增强了在图层表现出复杂交互情况下的鲁棒性。此外，还引入了一个渐进式自我改进过程，通过迭代地使用模型生成的高质量示例来增强训练集，从而优化性能。这项工作展示了如何利用生成式AI大模型（扩散模型）解决复杂的视觉分解问题，其方法论（微调、循环一致性、自增强）对于构建和理解能够处理复杂化学/质谱数据的“化学大模型”具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Disentangling visual layers in real-world images is a persistent challenge in vision and graphics, as such layers often involve non-linear and globally coupled interactions, including shading, reflection, and perspective distortion. In this work, we present an in-context image decomposition framework that leverages large diffusion foundation models for layered separation. We focus on the challenging case of logo-object decomposition, where the goal is to disentangle a logo from the surface on which it appears while faithfully preserving both layers. Our method fine-tunes a pretrained diffusion model via lightweight LoRA adaptation and introduces a cycle-consistent tuning strategy that jointly trains decomposition and composition models, enforcing reconstruction consistency between decomposed and recomposed images. This bidirectional supervision substantially enhances robustness in cases where the layers exhibit complex interactions. Furthermore, we introduce a progressive self-improving process, which iteratively augments the training set with high-quality model-generated examples to refine performance. Extensive experiments demonstrate that our approach achieves accurate and coherent decompositions and also generalizes effectively across other decomposition types, suggesting its potential as a unified framework for layered image decomposition.

</details>

---

### 126. [Autoregressive Visual Decoding from EEG Signals](https://arxiv.org/abs/2602.22555)

**基本信息**

- 🔗 arXiv: [`2602.22555`](https://arxiv.org/abs/2602.22555)
- 👥 作者: Sicheng Dai, Hongwang Xiao, Shan Yu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22555.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个从EEG信号到图像的自回归生成模型框架。虽然领域是神经科学，但其核心技术——使用预训练模型进行表示对齐、并采用分层自回归生成模型进行跨模态推理——与“质谱结构推理”任务（从质谱数据生成或推断分子结构）在问题形式和技术路线上高度相似，为后者提供了重要的方法论参考。

**📖 中文摘要**

本研究提出了AVDE，一个从脑电图（EEG）信号进行视觉解码的轻量高效框架。首先，利用预训练的EEG模型LaBraM，并通过对比学习对其进行微调，以对齐EEG和图像表示。其次，采用基于“下一尺度预测”策略的自回归生成框架：使用预训练的VQ-VAE将图像编码为多尺度令牌映射，并训练一个Transformer以EEG嵌入作为最粗糙的表示，自回归地预测更细尺度的令牌。这种设计在保持重建图像与输入EEG信号直接联系的同时，实现了连贯的生成。在两个数据集上的实验表明，AVDE在图像检索和重建任务上均优于先前的最先进方法，且仅使用10%的参数。这项工作展示了如何利用预训练模型和自回归生成架构构建高效的跨模态解码系统。其技术路径（预训练模型对齐、分层自回归生成）对于构建能够从复杂数据（如质谱）推理出结构信息的“质谱结构推理”模型具有方法论上的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalogram (EEG) signals have become a popular medium for decoding visual information due to their cost-effectiveness and high temporal resolution. However, current approaches face significant challenges in bridging the modality gap between EEG and image data. These methods typically rely on complex adaptation processes involving multiple stages, making it hard to maintain consistency and manage compounding errors. Furthermore, the computational overhead imposed by large-scale diffusion models limit their practicality in real-world brain-computer interface (BCI) applications. In this work, we present AVDE, a lightweight and efficient framework for visual decoding from EEG signals. First, we leverage LaBraM, a pre-trained EEG model, and fine-tune it via contrastive learning to align EEG and image representations. Second, we adopt an autoregressive generative framework based on a "next-scale prediction" strategy: images are encoded into multi-scale token maps using a pre-trained VQ-VAE, and a transformer is trained to autoregressively predict finer-scale tokens starting from EEG embeddings as the coarsest representation. This design enables coherent generation while preserving a direct connection between the input EEG signals and the reconstructed images. Experiments on two datasets show that AVDE outperforms previous state-of-the-art methods in both image retrieval and reconstruction tasks, while using only 10% of the parameters. In addition, visualization of intermediate outputs shows that the generative process of AVDE reflects the hierarchical nature of human visual perception. These results highlight the potential of autoregressive models as efficient and interpretable tools for practical BCI applications.

</details>

---

### 127. [Embedding interpretable $\ell_1$-regression into neural networks for uncovering temporal structure in cell imaging](https://arxiv.org/abs/2603.02899)

**基本信息**

- 🔗 arXiv: [`2603.02899`](https://arxiv.org/abs/2603.02899)
- 👥 作者: Fabian Kabus, Maren Hackenberg, Julia Hindel 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02899.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将可解释的稀疏统计模型（ℓ1-VAR）嵌入到神经网络中，以同时获得强大的学习能力和模型可解释性。这种方法论创新对于构建下一代“化学大模型”至关重要，因为化学领域不仅需要高预测精度，还需要理解模型决策背后的物理化学因素（即可解释性）。该工作为如何将领域知识（如稀疏性）以可微分的方式整合进大模型提供了具体范例。

**📖 中文摘要**

本研究提出了一种将经典的、可解释的统计回归技术（具体是ℓ1正则化的向量自回归模型，VAR）嵌入到卷积自编码器神经网络中的方法，旨在结合两者的优势。该框架应用于双光子钙成像数据，以提取稀疏的自回归动态。卷积自编码器提供降维以实现可处理的时序建模，而跳连连接则单独处理非稀疏的静态空间信息，将有稀疏结构的动态选择性地引导至ℓ1正则化的VAR模型中。通过微分分段线性解路径来实现ℓ1正则化回归参数的估计。这种方法使得神经网络能够学习非稀疏结构，同时通过嵌入的统计模型提供可解释性，并识别驱动观测动态的因素。这项工作展示了如何将可解释的稀疏回归模型与深度学习架构深度融合，为在化学信息学中开发兼具强大学习能力和物理解释性的“化学大模型”提供了创新的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While artificial neural networks excel in unsupervised learning of non-sparse structure, classical statistical regression techniques offer better interpretability, in particular when sparseness is enforced by $\ell_1$ regularization, enabling identification of which factors drive observed dynamics. We investigate how these two types of approaches can be optimally combined, exemplarily considering two-photon calcium imaging data where sparse autoregressive dynamics are to be extracted. We propose embedding a vector autoregressive (VAR) model as an interpretable regression technique into a convolutional autoencoder, which provides dimension reduction for tractable temporal modeling. A skip connection separately addresses non-sparse static spatial information, selectively channeling sparse structure into the $\ell_1$-regularized VAR. $\ell_1$-estimation of regression parameters is enabled by differentiating through the piecewise linear solution path. This is contrasted with approaches where the autoencoder does not adapt to the VAR model. Having an embedded statistical model also enables a testing approach for comparing temporal sequences from the same observational unit. Additionally, contribution maps visualize which spatial regions drive the learned dynamics.

</details>

---

### 128. [Information Routing in Atomistic Foundation Models: How Task Alignment and Equivariance Shape Linear Disentanglement](https://arxiv.org/abs/2603.03155)

**基本信息**

- 🔗 arXiv: [`2603.03155`](https://arxiv.org/abs/2603.03155)
- 👥 作者: Joshua Steier
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03155.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学大模型（特别是原子级基础模型）的表征学习、信息解耦和任务对齐，这是化学信息学中构建和理解大模型的关键主题。

**📖 中文摘要**

本文研究了原子级基础模型（Atomistic Foundation Models）中分子性质预测模型的表征组织方式。核心问题是探究模型如何在其表示中分离几何信息和组成信息。作者引入了组合探针分解（Compositional Probe Decomposition, CPD）方法，通过线性投影移除组成信号，并测量剩余表示中几何信息的可访问性。研究发现，任务对齐是决定模型能否实现线性解耦（即几何与组成信息分离）的主导因素。例如，在QM9数据集上，针对HOMO-LUMO能隙训练的模型，其几何信息可访问性远高于针对能量训练的模型。此外，研究还揭示了在MACE等模型中，信息会根据对称类型（如标量通道编码HOMO-LUMO能隙，矢量通道编码偶极矩）进行路由。这项工作直接关联到化学大模型（特别是原子级基础模型）的表征学习、可解释性以及如何为下游任务（如性质预测）构建更有效的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

What determines whether a molecular property prediction model organizes its representations so that geometric and compositional information can be cleanly separated? We introduce Compositional Probe Decomposition (CPD), which linearly projects out composition signal and measures how much geometric information remains accessible to a Ridge probe. We validate CPD with four independent checks, including a structural isomer benchmark where compositional projections score at chance while geometric residuals reach 94.6\% pairwise classification accuracy. Across ten models from five architectural families on QM9, we find a \emph{linear accessibility gradient}: models differ by $6.6\times$ in geometric information accessible after composition removal ($R^2_{\mathrm{geom}}$ from 0.081 to 0.533 for HOMO-LUMO gap). Three factors explain this gradient. Task alignment dominates: models trained on HOMO-LUMO gap ($R^2_{\mathrm{geom}}$ 0.44--0.53) outscore energy-trained models by $\sim$0.25 $R^2$ regardless of architecture. Within-architecture ablations on two independent architectures confirm this: PaiNN drops from 0.53 to 0.31 when retrained on energy, and MACE drops from 0.44 to 0.08. Data diversity partially compensates for misaligned objectives, with MACE pretrained on MPTraj (0.36) outperforming QM9-only energy models. Inside MACE's representations, information routes by symmetry type: $L{=}1$ (vector) channels preferentially encode dipole moment ($R^2 = 0.59$ vs.\ 0.38 in $L{=}0$), while $L{=}0$ (scalar) channels encode HOMO-LUMO gap ($R^2 = 0.76$ vs.\ 0.34 in $L{=}1$). This pattern is absent in ViSNet. We also show that nonlinear probes produce misleading results on residualized representations, recovering $R^2 = 0.68$--$0.95$ on a purely compositional target, and recommend linear probes for this setting.

</details>

---

### 129. [Representing local protein environments with machine learning force fields](https://arxiv.org/abs/2505.23354)

**基本信息**

- 🔗 arXiv: [`2505.23354`](https://arxiv.org/abs/2505.23354)
- 👥 作者: Meital Bojan, Sanketh Vedula, Advaith Maddipatla 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.23354.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用原子级基础模型（一种化学大模型）来学习蛋白质局部环境的表示，并将其应用于化学位移预测，直接关联化学大模型在分子表示和性质预测中的应用。

**📖 中文摘要**

本文提出了一种基于原子级基础模型（Atomistic Foundation Models, AFMs）中间特征的新型局部蛋白质环境表示方法。作者证明，这种嵌入能够有效捕捉局部结构特征（如二级结构基序）和化学特征（如氨基酸身份和质子化状态）。该表示空间具有有意义的内部结构，使得构建基于数据驱动的生物分子环境分布先验成为可能。作为应用案例，在生物分子核磁共振波谱学中，该表示实现了首个物理信息化的化学位移预测器，并达到了最先进的精度。这项工作展示了原子级基础模型及其涌现表示在传统分子模拟之外的蛋白质建模中的有效性，为构建蛋白质环境的有效功能表示开辟了新途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The local structure of a protein strongly impacts its function and interactions with other molecules. Therefore, a concise, informative representation of a local protein environment is essential for modeling and designing proteins and biomolecular interactions. However, these environments' extensive structural and chemical variability makes them challenging to model, and such representations remain under-explored. In this work, we propose a novel representation for a local protein environment derived from the intermediate features of atomistic foundation models (AFMs). We demonstrate that this embedding effectively captures both local structure (e.g., secondary motifs), and chemical features (e.g., amino-acid identity and protonation state). We further show that the AFM-derived representation space exhibits meaningful structure, enabling the construction of data-driven priors over the distribution of biomolecular environments. Finally, in the context of biomolecular NMR spectroscopy, we demonstrate that the proposed representations enable a first-of-its-kind physics-informed chemical shift predictor that achieves state-of-the-art accuracy. Our results demonstrate the surprising effectiveness of atomistic foundation models and their emergent representations for protein modeling beyond traditional molecular simulations. We believe this will open new lines of work in constructing effective functional representations for protein environments.

</details>

---

### 130. [RadDiff: Retrieval-Augmented Denoising Diffusion for Protein Inverse Folding](https://arxiv.org/abs/2512.00126)

**基本信息**

- 🔗 arXiv: [`2512.00126`](https://arxiv.org/abs/2512.00126)
- 👥 作者: Jin Han, Tianfan Fu, Wu-Jun Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00126.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合检索增强和扩散模型的化学大模型（RadDiff）来解决蛋白质逆折叠这一核心化学信息学问题。

**📖 中文摘要**

本文提出了RadDiff，一种用于蛋白质逆折叠（根据目标蛋白质结构设计氨基酸序列）的新方法。RadDiff结合了检索增强和去噪扩散模型。其核心创新在于设计了一种检索增强机制，从不断增长的自然蛋白质数据库中捕获最新的蛋白质知识；以及一个知识感知的扩散模型，通过一个轻量级模块将这些知识整合到扩散过程中。实验结果表明，RadDiff在CATH、TS50和PDB2022数据集上 consistently 优于现有方法，序列恢复率提升高达19%。该方法生成的序列具有高度的可折叠性，并能随数据库规模有效扩展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein inverse folding, the design of an amino acid sequence based on a target protein structure, is a fundamental problem of computational protein engineering. Existing methods either generate sequences without leveraging external knowledge or relying on protein language models~(PLMs). The former omits the knowledge stored in natural protein data, while the latter is parameter-inefficient and inflexible to adapt to ever-growing protein data. To overcome the above drawbacks, in this paper we propose a novel method, called $\underline{\text{r}}$etrieval-$\underline{\text{a}}$ugmented $\underline{\text{d}}$enoising $\underline{\text{diff}}$usion~($\mbox{RadDiff}$), for protein inverse folding. In RadDiff, a novel retrieval-augmentation mechanism is designed to capture the up-to-date protein knowledge. We further design a knowledge-aware diffusion model that integrates this protein knowledge into the diffusion process via a lightweight module. Experimental results on the CATH, TS50, and PDB2022 datasets show that $\mbox{RadDiff}$ consistently outperforms existing methods, improving sequence recovery rate by up to 19\%. Experimental results also demonstrate that RadDiff generates highly foldable sequences and scales effectively with database size.

</details>

---

### 131. [From Mice to Trains: Amortized Bayesian Inference on Graph Data](https://arxiv.org/abs/2601.02241)

**基本信息**

- 🔗 arXiv: [`2601.02241`](https://arxiv.org/abs/2601.02241)
- 👥 作者: Svenja Jedhoff, Elizaveta Semenova, Aura Raulo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.02241.pdf)

**💡 相关性分析**

满足标准1：论文提出的摊销贝叶斯推断框架应用于图数据，包括分子图等化学信息学中的典型数据结构，属于化学大模型（图神经网络）在推断任务中的应用范畴。

**📖 中文摘要**

本文提出了一种适用于图结构数据的摊销贝叶斯推断（ABI）框架。该框架将置换不变的图编码器与灵活的神经后验估计器相结合，形成一个两模块流程：一个摘要网络将属性图映射为固定长度的表示，一个推断网络近似参数的后验分布。作者在合成数据和两个真实世界领域（生物学和物流）上评估了该方法的恢复能力和校准性能。虽然论文主题宽泛，但其在生物学领域的应用示例（如分子图）与化学信息学相关，展示了如何利用图神经网络和摊销推断对化学系统（如分子）的参数进行后验估计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graphs arise across diverse domains, from biology and chemistry to social and information networks, as well as in transportation and logistics. Inference on graph-structured data requires methods that are permutation-invariant, scalable across varying sizes and sparsities, and capable of capturing complex long-range dependencies, making posterior estimation on graph parameters particularly challenging. Amortized Bayesian Inference (ABI) is a simulation-based framework that employs generative neural networks to enable fast, likelihood-free posterior inference. We adapt ABI to graph data to address these challenges to perform inference on node-, edge-, and graph-level parameters. Our approach couples permutation-invariant graph encoders with flexible neural posterior estimators in a two-module pipeline: a summary network maps attributed graphs to fixed-length representations, and an inference network approximates the posterior over parameters. In this setting, several neural architectures can serve as the summary network. In this work we evaluate multiple architectures and assess their performance on controlled synthetic settings and two real-world domains - biology and logistics - in terms of recovery and calibration.

</details>

---

## 📊 数据统计
- 累计运行天数：21
- 累计论文数量：1550

## 📝 历史记录

> 暂无历史数据

