# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-11 01:24:27

## 📅 2026-03-11 (今日最新)

**相关论文数：111**

### 1. [Hierarchical Latent Structures in Data Generation Process Unify Mechanistic Phenomena across Scale](https://arxiv.org/abs/2603.06592)

**基本信息**

- 🔗 arXiv: [`2603.06592`](https://arxiv.org/abs/2603.06592)
- 👥 作者: Jonas Rohweder, Subhabrata Dutta, Iryna Gurevych
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06592.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕理解大型语言模型（作为“化学大模型”在化学信息学领域的类比和基础技术）内部机制现象的出现原理，这直接与“化学大模型”主题中关于模型机理和可解释性的研究相关。

**📖 中文摘要**

本文探讨了Transformer语言模型中几种看似无关的机制现象（如归纳头、函数向量和九头蛇效应）的统一出现原理。作者提出，数据生成过程中的层次结构是解释这些现象出现的“X因素”。他们使用概率上下文无关文法（PCFG）生成合成语料库，作为网络规模文本语料库的高效代理，并研究了在这些合成数据以及真实语言模型检查点中这些机制的出现情况。研究发现，数据生成过程中的层次结构在语言模型的训练动态中扮演着关键角色，为这些机制现象提供了统一的解释。这项工作为未来的可解释性研究提供了高效的工具，并首次为LLM中看似无关的机制现象提供了统一的解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Contemporary studies have uncovered many puzzling phenomena in the neural information processing of Transformer-based language models. Building a robust, unified understanding of these phenomena requires disassembling a model within the scope of its training. While the intractable scale of pretraining corpora limits a bottom-up investigation in this direction, simplistic assumptions of the data generation process limit the expressivity and fail to explain complex patterns. In this work, we use probabilistic context-free grammars (PCFGs) to generate synthetic corpora that are faithful and computationally efficient proxies for web-scale text corpora. We investigate the emergence of three mechanistic phenomena: induction heads, function vectors, and the Hydra effect, under our designed data generation process, as well as in the checkpoints of real-world language models. Our findings suggest that hierarchical structures in the data generation process serve as the X-factor in explaining the emergence of these phenomena. We provide the theoretical underpinnings of the role played by hierarchy in the training dynamics of language models. In a nutshell, our work is the first of its kind to provide a unified explanation behind the emergence of seemingly unrelated mechanistic phenomena in LLMs, augmented with efficient synthetic tooling for future interpretability research.

</details>

---

### 2. [Advances in GRPO for Generation Models: A Survey](https://arxiv.org/abs/2603.06623)

**基本信息**

- 🔗 arXiv: [`2603.06623`](https://arxiv.org/abs/2603.06623)
- 👥 作者: Zexiang Liu, Xianglong He, Yangguang Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06623.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对生成模型（包括扩散模型等，这些是构建“化学大模型”如分子生成模型的重要技术基础）强化学习对齐方法的综述。它系统地回顾和展望了Flow-GRPO框架及其发展，这与“化学大模型”主题中关于模型训练、优化和对齐的前沿方法论讨论直接相关。

**📖 中文摘要**

本文对Flow-GRPO（Group Relative Policy Optimization的流匹配扩展）及其在生成模型对齐方面的后续发展进行了全面综述。Flow-GRPO使得生成系统能够进行稳定的强化学习对齐。本调查从两个主要维度组织现有工作：首先，分析超越原始框架的方法论进展，包括奖励信号设计、信用分配、采样效率、多样性保持、奖励黑客缓解和奖励模型构建。其次，考察基于GRPO的对齐方法在各种生成范式和模态中的扩展，包括文生图、视频生成、图像编辑、语音和音频、3D建模、具身视觉-语言-动作系统、统一多模态模型、自回归和掩码扩散模型以及修复任务。通过综合理论见解和实际应用，本调查强调了Flow-GRPO作为现代生成模型的通用对齐框架，并概述了可扩展和稳健的基于强化的生成所面临的关键开放挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large-scale flow matching models have achieved strong performance across generative tasks such as text-to-image, video, 3D, and speech synthesis. However, aligning their outputs with human preferences and task-specific objectives remains challenging. Flow-GRPO extends Group Relative Policy Optimization (GRPO) to generation models, enabling stable reinforcement learning alignment for generative systems. Since its introduction, Flow-GRPO has triggered rapid research growth, spanning methodological refinements and diverse application domains. This survey provides a comprehensive review of Flow-GRPO and its subsequent developments. We organize existing work along two primary dimensions. First, we analyze methodological advances beyond the original framework, including reward signal design, credit assignment, sampling efficiency, diversity preservation, reward hacking mitigation, and reward model construction. Second, we examine extensions of GRPO-based alignment across generative paradigms and modalities, including text-to-image, video generation, image editing, speech and audio, 3D modeling, embodied vision-language-action systems, unified multimodal models, autoregressive and masked diffusion models, and restoration tasks. By synthesizing theoretical insights and practical adaptations, this survey highlights Flow-GRPO as a general alignment framework for modern generative models and outlines key open challenges for scalable and robust reinforcement-based generation.

</details>

---

### 3. [Unmixing microinfrared spectroscopic images of cross-sections of historical oil paintings](https://arxiv.org/abs/2603.06673)

**基本信息**

- 🔗 arXiv: [`2603.06673`](https://arxiv.org/abs/2603.06673)
- 👥 作者: Shivam Pande, Nicolas Nadisic, Francisco Mederos-Henry 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06673.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于分析复杂混合物（历史油画横截面）光谱图像的新型无监督深度学习框架。该方法的核心是处理和分析高维光谱数据，这与“质谱结构推理”主题中处理复杂质谱数据、进行物质识别和解析混合物成分的核心任务在技术层面高度相关，提供了可用于类似复杂光谱/质谱数据分析的算法工具和思路。

**📖 中文摘要**

本文提出了一种用于分析历史油画横截面的衰减全反射傅里叶变换红外显微光谱（ATR-μFTIR）高光谱图像（HSI）的无监督盲源分离方法。该方法旨在解决文化遗产科学中材料表征的挑战，其中光谱通常是多种物质在异质、多层和降解样品中的混合物。当前工作流程严重依赖与参考库的手动比较，速度慢、主观且难以扩展。作者引入了一种基于卷积神经网络（CNN）自编码器的无监督方法，用于ATR-μFTIR HSI的盲源分离，通过基于补丁的建模利用局部空间结构来估计端元光谱及其丰度图。为了减少对超过1500个波段中大气和采集伪影的敏感性，该方法采用了加权光谱角距离（WSAD）损失函数。该方法在根特祭坛画（归因于范艾克兄弟）的横截面ATR-μFTIR数据上进行了演示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Spectroscopic imaging (SI) has become central to heritage science because it enables non-invasive, spatially resolved characterisation of materials in artefacts. In particular, attenuated total reflection Fourier transform infrared microscopy (ATR-$\mu$FTIR) is widely used to analyse painting cross-sections, where a spectrum is recorded at each pixel to form a hyperspectral image (HSI). Interpreting these data is difficult: spectra are often mixtures of several species in heterogeneous, multi-layered and degraded samples, and current practice still relies heavily on manual comparison with reference libraries. This workflow is slow, subjective and hard to scale. We propose an unsupervised CNN autoencoder for blind unmixing of ATR-$\mu$FTIR HSIs, estimating endmember spectra and their abundance maps while exploiting local spatial structure through patch-based modelling. To reduce sensitivity to atmospheric and acquisition artefacts across $>1500$ bands, we introduce a weighted spectral angle distance (WSAD) loss with automatic band-reliability weights derived from robust measures of spatial flatness, neighbour agreement and spectral roughness. Compared with standard SAD training, WSAD improves interpretability in contamination-prone spectral regions. We demonstrate the method on an ATR-$\mu$FTIR cross-section from the Ghent Altarpiece attributed to the Van Eyck brothers.

</details>

---

### 4. [Chart Deep Research in LVLMs via Parallel Relative Policy Optimization](https://arxiv.org/abs/2603.06677)

**基本信息**

- 🔗 arXiv: [`2603.06677`](https://arxiv.org/abs/2603.06677)
- 👥 作者: Jiajin Tang, Gaoyang, Wenjie Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06677.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升多模态大语言模型（MLMs）在图表数据上的深度推理和分析能力。这直接涉及“化学大模型”主题，因为化学领域广泛使用图表（如分子结构图、光谱图）进行研究和交流，提升模型在此类结构化数据上的复杂推理能力对化学信息学至关重要。论文提出的训练和评估框架对此有直接贡献。

**📖 中文摘要**

本文针对图表数据智能在深度研究能力上的局限性，提出了PRPO（Parallel Relative Policy Optimization）框架和MCDR-Bench评估基准。现有方法主要解决视觉识别或事实问答等浅层任务，而非深度研究所需的复杂推理和高级数据分析。PRPO通过跨奖励维度的并行优化和跨数据类型的能力划分，有效解耦了异构数据和多维奖励信号之间的冲突。MCDR-Bench基于“错误唯一性原则”，通过可控错误注入将主观生成评估转化为客观错误识别，从而实现对深度研究能力的可量化评估。实验验证表明，PRPO和MCDR-Bench共同建立了一个统一的框架，通过增强的协作训练和客观评估系统地推进了图表深度研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the rapid advancement of data science, charts have evolved from simple numerical presentation tools to essential instruments for insight discovery and decision-making support. However, current chart data intelligence exhibits significant limitations in deep research capabilities, with existing methods predominantly addressing shallow tasks such as visual recognition or factual question-answering, rather than the complex reasoning and high-level data analysis that deep research requires. This limitation stems from two primary technical bottlenecks: at the training level, existing post-training techniques exhibit deficiencies in handling multi-dimensional reward signal interference and heterogeneous data gradient conflicts, preventing models from achieving balanced development across multiple capability dimensions; at the evaluation level, current methods remain limited to factual retrieval and basic computation, failing to assess end-to-end analytic reasoning and other deep research capabilities. To address the training challenge, we propose PRPO, which performs parallel optimization across reward dimensions and capability partitioning across data types, effectively disentangling conflicts between heterogeneous data and multi-dimensional reward signals while ensuring optimization stability. For the evaluation challenge, we construct MCDR-Bench based on the ``error uniqueness principle," transforming subjective generation assessment into objective error identification through controllable error injection, enabling quantifiable evaluation of deep research capabilities. Experimental validation confirms that the proposed PRPO and MCDR-Bench jointly establish a unified framework that systematically advances chart deep research through enhanced collaborative training and objective evaluation.

</details>

---

### 5. [One step further with Monte-Carlo sampler to guide diffusion better](https://arxiv.org/abs/2603.06685)

**基本信息**

- 🔗 arXiv: [`2603.06685`](https://arxiv.org/abs/2603.06685)
- 👥 作者: Minsi Ren, Wenhao Deng, Ruiqi Feng 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06685.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进扩散模型的条件生成和引导采样算法。扩散模型是构建“化学大模型”（如分子生成、性质预测模型）的关键生成技术之一。论文提出的ABMS方法旨在提高条件生成的准确性和一致性，这与优化化学领域生成模型性能的目标直接相关。

**📖 中文摘要**

本文针对基于随机微分方程（SDE）的生成模型在条件生成中面临的梯度估计误差问题，提出了一种称为ABMS（Additional Backward denoising step and Monte-Carlo Sampling）的即插即用调整策略。该方法通过执行额外的反向去噪步骤和蒙特卡洛采样，以实现更好的引导扩散。作者提供了理论分析，并提出了采用双重焦点评估框架，以突出现有方法中普遍存在的跨条件干扰问题。实验在多种任务设置和数据类型上进行，主要包括条件在线手写轨迹生成、图像逆问题（修复、超分辨率和高斯去模糊）、分子逆向设计等。结果表明，该方法可以有效地与高阶采样器结合使用，并在所有不同场景中一致地提高了生成样本的质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Stochastic differential equation (SDE)-based generative models have achieved substantial progress in conditional generation via training-free differentiable loss-guided approaches. However, existing methodologies utilizing posterior sam- pling typically confront a substantial estimation error, which results in inaccu- rate gradients for guidance and leading to inconsistent generation results. To mitigate this issue, we propose that performing an additional backward denois- ing step and Monte-Carlo sampling (ABMS) can achieve better guided diffu- sion, which is a plug-and-play adjustment strategy. To verify the effectiveness of our method, we provide theoretical analysis and propose the adoption of a dual-focus evaluation framework, which further serves to highlight the critical problem of cross-condition interference prevalent in existing approaches. We conduct experiments across various task settings and data types, mainly includ- ing conditional online handwritten trajectory generation, image inverse problems (inpainting, super resolution and gaussian deblurring) molecular inverse design and so on. Experimental results demonstrate that our approach can be effec- tively used with higher order samplers and consistently improves the quality of generation samples across all the different scenarios.

</details>

---

### 6. [High-Resolution Image Reconstruction with Unsupervised Learning and Noisy Data Applied to Ion-Beam Dynamics for Particle Accelerators](https://arxiv.org/abs/2603.06689)

**基本信息**

- 🔗 arXiv: [`2603.06689`](https://arxiv.org/abs/2603.06689)
- 👥 作者: Francis Osswald, Mohammed Chahbaoui, Xinyi Liang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06689.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于处理低信噪比科学图像（束流发射度图像）的无监督深度学习重建方法。该方法的核心挑战——从噪声数据中恢复高保真结构信息——与“质谱结构推理”主题中从嘈杂、复杂的质谱数据中推断化合物结构的核心任务在问题本质上高度相似。论文提供的算法框架和思路（如无监督学习、噪声鲁棒性）可用于启发或适配质谱数据的处理和分析。

**📖 中文摘要**

本文针对高能物理加速器中束流诊断的图像重建问题，提出了一种基于卷积滤波和神经网络的无监督学习框架，用于在低信噪比条件下对束流发射度图像进行去噪和高保真重建。现代设施需要精确检测束流光晕结构以控制损失，而传统的分析工具已达到其性能极限。本文回顾了现有的用于数据清洗、轮廓提取和发射度重建的图像处理技术，并引入了一种新颖的方法。尽管缺乏训练数据集，所提出的无监督框架在低信噪比条件下实现了鲁棒的去噪和束流发射度图像的高保真重建。该方法将可测量幅度扩展到七个标准差以上，实现了前所未有的光晕分辨率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Image reconstruction in the presence of severe degradation remains a challenging inverse problem, particularly in beam diagnostics for high-energy physics accelerators. As modern facilities demand precise detection of beam halo structures to control losses, traditional analysis tools have reached their performance limits. This work reviews existing image-processing techniques for data cleaning, contour extraction, and emittance reconstruction, and introduces a novel approach based on convolutional filtering and neural networks with optimized early-stopping strategies in order to control overfitting. Despite the absence of training datasets, the proposed unsupervised framework achieves robust denoising and high-fidelity reconstruction of beam emittance images under low signal-to-noise conditions. The method extends measurable amplitudes beyond seven standard deviations, enabling unprecedented halo resolution.

</details>

---

### 7. [ProtAlign: Contrastive learning paradigm for Sequence and structure alignment](https://arxiv.org/abs/2603.06722)

**基本信息**

- 🔗 arXiv: [`2603.06722`](https://arxiv.org/abs/2603.06722)
- 👥 作者: Aditya Ranganath, Hasin Us Sami, Kowshik Thopalli 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06722.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学中的蛋白质序列与结构对齐问题，这是化学大模型（特别是用于生物分子）和结构推理（从序列推断结构或反之）的关键子领域。

**📖 中文摘要**

本文提出了一种名为ProtAlign的序列结构对比对齐框架，旨在解决蛋白质语言模型通常只考虑序列与文本描述对齐，而忽略结构信息的问题。该框架通过学习一个共享的嵌入空间，使蛋白质在序列和结构两种模态下具有一致的表示。通过在大规模序列与实验解析或预测结构对上进行训练，模型最大化匹配序列结构对之间的一致性，同时推开不相关的对。这种对齐支持跨模态检索（例如，给定序列寻找结构邻居），并改进下游预测任务，如功能注释和稳定性估计。该研究展示了对比学习可以作为连接蛋白质序列和结构的强大桥梁，为理解和设计蛋白质提供统一的表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models often take into consideration the alignment between a protein sequence and its textual description. However, they do not take structural information into consideration. Traditional methods treat sequence and structure separately, limiting the ability to exploit the alignment between the structure and protein sequence embeddings. In this paper, we introduce a sequence structure contrastive alignment framework, which learns a shared embedding space where proteins are represented consistently across modalities. By training on large-scale pairs of sequences and experimentally resolved or predicted structures, the model maximizes agreement between matched sequence structure pairs while pushing apart unrelated pairs. This alignment enables cross-modal retrieval (e.g., finding structural neighbors given a sequence), improves downstream prediction tasks such as function annotation and stability estimation, and provides interpretable links between sequence variation and structural organization. Our results demonstrate that contrastive learning can serve as a powerful bridge between protein sequences and structures, offering a unified representation for understanding and engineering proteins.

</details>

---

### 8. [Property-driven Protein Inverse Folding With Multi-Objective Preference Alignment](https://arxiv.org/abs/2603.06748)

**基本信息**

- 🔗 arXiv: [`2603.06748`](https://arxiv.org/abs/2603.06748)
- 👥 作者: Xiaoyang Hou, Junqi Liu, Chence Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06748.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是化学信息学中的蛋白质序列设计，这是化学大模型（用于分子生成与优化）和结构推理（从蛋白质骨架逆推序列）的核心应用领域。

**📖 中文摘要**

本文介绍了ProtAlign，一个多目标偏好对齐框架，用于微调预训练的蛋白质逆折叠模型，以在保持结构保真度的同时满足多种可开发性目标（如溶解度、热稳定性、表达水平）。蛋白质序列设计需要在可设计性（恢复目标骨架的能力）与这些通常相互竞争的可开发性属性之间取得平衡。现有方法通过事后突变、推理时偏置或在特定属性子集上重新训练来解决这些问题，但这些方法依赖于目标且需要大量领域专业知识。ProtAlign采用半在线直接偏好优化策略，利用灵活的偏好边界来缓解竞争目标之间的冲突，并使用计算机属性预测器构建偏好对。应用于广泛使用的ProteinMPNN骨架，所得模型MoMPNN在包括CATH 4.3晶体结构、从头生成的骨架和真实世界结合剂设计场景在内的任务中，在不损害可设计性的情况下增强了可开发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequence design must balance designability, defined as the ability to recover a target backbone, with multiple, often competing, developability properties such as solubility, thermostability, and expression. Existing approaches address these properties through post hoc mutation, inference-time biasing, or retraining on property-specific subsets, yet they are target dependent and demand substantial domain expertise or careful hyperparameter tuning. In this paper, we introduce ProtAlign, a multi-objective preference alignment framework that fine-tunes pretrained inverse folding models to satisfy diverse developability objectives while preserving structural fidelity. ProtAlign employs a semi-online Direct Preference Optimization strategy with a flexible preference margin to mitigate conflicts among competing objectives and constructs preference pairs using in silico property predictors. Applied to the widely used ProteinMPNN backbone, the resulting model MoMPNN enhances developability without compromising designability across tasks including sequence design for CATH 4.3 crystal structures, de novo generated backbones, and real-world binder design scenarios, making it an appealing framework for practical protein sequence design.

</details>

---

### 9. [Failure Detection in Chemical Processes using Symbolic Machine Learning: A Case Study on Ethylene Oxidation](https://arxiv.org/abs/2603.06767)

**基本信息**

- 🔗 arXiv: [`2603.06767`](https://arxiv.org/abs/2603.06767)
- 👥 作者: Julien Amblard, Niklas Groll, Matthew Tait 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06767.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是化学过程工业中的故障预测，这是化学信息学的一个具体应用。虽然不直接涉及质谱，但其使用的符号机器学习方法在化学领域的数据分析和模型构建中具有相关性，属于广义的化学信息学范畴。

**📖 中文摘要**

本文研究了在化学过程中使用符号机器学习预测故障的方法，并以乙烯氧化过程为背景进行了可行性研究。化学过程工业中，安全性至关重要，但大规模神经网络方法往往因其脆弱性、缺乏可解释性和可解释性而不适用。此外，该领域包含历史故障的开源真实世界数据集稀缺。我们的方法基于一个最先进的符号机器学习系统，该系统能够从上下文相关的噪声示例中学习概率规则形式的预测模型。该系统是一个通用符号学习器，使我们的方法独立于任何特定的化学过程。为了解决缺乏真实世界故障数据的问题，我们利用化学过程模拟器生成的数据进行可行性研究。实验结果表明，符号机器学习在预测性能上可以超越随机森林和多层感知机等基线方法，同时通过生成紧凑的、基于规则的预测模型来保持可解释性。最后，我们解释了如何将此类学习到的基于规则的模型集成到智能体中，以在潜在故障期间协助化工厂操作员进行决策。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Over the past decade, Artificial Intelligence has significantly advanced, mostly driven by large-scale neural approaches. However, in the chemical process industry, where safety is critical, these methods are often unsuitable due to their brittleness, and lack of explainability and interpretability. Furthermore, open-source real-world datasets containing historical failures are scarce in this domain. In this paper, we investigate an approach for predicting failures in chemical processes using symbolic machine learning and conduct a feasibility study in the context of an ethylene oxidation process. Our method builds on a state-of-the-art symbolic machine learning system capable of learning predictive models in the form of probabilistic rules from context-dependent noisy examples. This system is a general-purpose symbolic learner, which makes our approach independent of any specific chemical process. To address the lack of real-world failure data, we conduct our feasibility study leveraging data generated from a chemical process simulator. Experimental results show that symbolic machine learning can outperform baseline methods such as random forest and multilayer perceptron, while preserving interpretability through the generation of compact, rule-based predictive models. Finally, we explain how such learned rule-based models could be integrated into agents to assist chemical plant operators in decision-making during potential failures.

</details>

---

### 10. [Joint 3D Gravity and Magnetic Inversion via Rectified Flow and Ginzburg-Landau Guidance](https://arxiv.org/abs/2603.06829)

**基本信息**

- 🔗 arXiv: [`2603.06829`](https://arxiv.org/abs/2603.06829)
- 👥 作者: Dhruman Gupta, Yashas Shende, Aritra Das 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06829.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决一个地球物理领域的反问题（从观测数据推断地下结构），其使用的机器学习框架（整流流、正则化、引导）在方法论上与化学信息学中解决质谱结构推理（从质谱数据推断分子结构）这一反问题高度相关。

**📖 中文摘要**

本文介绍了一种新颖的框架，将3D重力和磁力联合反演重新表述为在Noddyverse数据集（最大的基于物理学的反演数据集）上的整流流问题。给定表面上的磁力和重力数据，联合重建产生它们的底层密度是一个不适定的反问题。虽然多个属性的联合反演缓解了磁力和重力数据中的非唯一性问题，但确定性算法收敛到单个正则化解，因此无法捕捉可能的解分布。同样，大多数基于机器学习的技术预测单个解而不对整个分布进行建模。我们引入了一个基于Ginzburg-Landau理论的广义伊辛模型正则化器，有助于矿石识别，从而实现物理感知训练。我们还提出了一种基于GL理论的引导方法，可以作为即插即用模块与现有的无条件去噪器一起使用。该框架旨在通过整流流和物理引导，从地球物理数据中更稳健地推断地下结构，这与从光谱数据推断分子结构（质谱结构推理）在反问题求解的机器学习方法上具有概念相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Subsurface ore detection is of paramount importance given the gradual depletion of shallow mineral resources in recent years. It is crucial to explore approaches that go beyond the limitations of traditional geological exploration methods. One such promising new method is joint magnetic and gravitational inversion. Given magnetic and gravitational data on a surface, jointly reconstructing the underlying densities that generate them remains an ill-posed inverse problem. Although joint inversion of multiple properties mitigates the non-uniqueness problem in magnetic and gravitational data, deterministic algorithms converge to a single regularized solution and thus do not capture the distribution of possible solutions. Similarly, most machine learning based techniques predict a single solution without modelling the entire distribution. In this paper, we introduce a novel framework that reframes 3D gravity and magnetic joint inversion as a rectified flow on the Noddyverse dataset, the largest physics-based dataset for inversion. We introduce a Ginzburg-Landau (GL) regularizer, a generalized version of the Ising model that aids in ore identification, enabling physics-aware training. We also propose a guidance methodology based on GL theory that can be used as a plug-and-play module with existing unconditional denoisers. Lastly, we also train and release a VAE for the 3D densities, which facilitates downstream work in the field.

</details>

---

### 11. [Symmetry-Constrained Language-Guided Program Synthesis for Discovering Governing Equations from Noisy and Partial Observations](https://arxiv.org/abs/2603.06869)

**基本信息**

- 🔗 arXiv: [`2603.06869`](https://arxiv.org/abs/2603.06869)
- 👥 作者: Mirza Samad Ahmed Baig, Syeda Anshrah Gillani
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06869.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用语言模型引导的程序合成从数据中发现符号方程，这直接属于“化学大模型”中利用AI进行科学发现和建模的范畴。该方法论对于从质谱等复杂数据中推导出化学规律或分子特征方程具有潜在应用价值。

**📖 中文摘要**

本文介绍了SymLang，一个统一的框架，用于从嘈杂和部分观测中发现紧凑的控制方程。该框架结合了三个先前独立的思想：(i) 类型化的对称性约束语法，将量纲分析、群论不变性和奇偶约束编码为硬生产规则，平均在拟合之前消除了71.3%的候选表达式树；(ii) 语言模型引导的程序合成，其中微调后的70亿参数提议器，以可解释的数据描述符为条件，高效地导航受约束的搜索空间；(iii) 结合块bootstrap稳定性分析的最小描述长度正则化贝叶斯模型选择，量化结构不确定性而不是承诺于单个最佳方程。在涵盖经典力学、电动力学、热力学、种群动力学和非线性振荡器的133个动力系统中，SymLang在10%观测噪声下实现了83.7%的精确结构恢复率，比次优基线提高了22.4个百分点，同时将分布外外推误差降低了61%，并几乎消除了守恒定律违规。该框架完全开源且可复现，提供了从原始数据到可解释、物理可审计的符号定律的原则性途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering compact governing equations from experimental observations is one of the defining objectives of quantitative science, yet practical discovery pipelines routinely fail when measurements are noisy, relevant state variables are unobserved, or multiple symbolic structures explain the data equally well within statistical uncertainty. Here we introduce SymLang (Symmetry-constrained Language-guided equation discovery), a unified framework that brings together three previously separate ideas: (i) typed symmetry-constrained grammars that encode dimensional analysis, group-theoretic invariance, and parity constraints as hard production rules, eliminating on average 71.3% of candidate expression trees before any fitting; (ii) language-model-guided program synthesis in which a fine-tuned 7B-parameter proposer, conditioned on interpretable data descriptors, efficiently navigates the constrained search space; and (iii) MDL-regularized Bayesian model selection coupled with block-bootstrap stability analysis that quantifies structural uncertainty rather than committing to a single best equation. Across 133 dynamical systems spanning classical mechanics, electrodynamics, thermodynamics, population dynamics, and nonlinear oscillators, SymLang achieves an exact structural recovery rate of 83.7% under 10% observational noise - a 22.4 percentage-point improvement over the next-best baseline - while reducing out-of-distribution extrapolation error by 61% and near-eliminating conservation-law violations (3.1 x 10-3 vs. 187.3 x 10-3 physical drift for the closest competitor). In all tested regimes the framework correctly identifies structural degeneracy, reporting it explicitly rather than returning a confidently wrong single equation. The framework is fully open-source and reproducible, providing a principled pathway from raw data to interpretable, physically auditable symbolic laws.

</details>

---

### 12. [Kernel Methods for Some Transport Equations with Application to Learning Kernels for the Approximation of Koopman Eigenfunctions: A Unified Approach via Variational Methods, Green's Functions and the Method of Characteristics](https://arxiv.org/abs/2603.06872)

**基本信息**

- 🔗 arXiv: [`2603.06872`](https://arxiv.org/abs/2603.06872)
- 👥 作者: Boumediene Hamzi, Houman Owhadi, Umesh Vaidya
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于Koopman算子（一种用于分析动力系统的大模型/表示学习工具）特征函数近似的核方法。Koopman算子在化学动力学和分子模拟中用于分析高维动力系统，与“化学大模型”主题相关。同时，其框架也适用于一般输运方程，在方法论上具有广泛的应用潜力。

**📖 中文摘要**

本文提出了一个统一的理论和计算框架，用于构建针对输运方程并适应非线性动力系统Koopman特征函数的再生核。这些特征函数满足一个输运型偏微分方程，我们通过三种基于分析的方法来求逆：(i) 再生核希尔伯特空间中的Lions型变分原理，(ii) 与格林函数卷积，以及(iii) 沿特征流通过拉普拉斯变换构造的预解算子。我们证明在温和的光滑性和因果性假设下，这三种构造产生相同的核。我们进一步证明，当相关的核特征函数位于RKHS中时，它们会收敛到真实的Koopman特征函数。我们的方法通过一个无网格的凸优化框架数值实现，并通过边界正则化增强以处理特征函数爆炸。一个多核学习方案通过残差最小化自动选择核。该框架同样适用于更广泛的线性输运PDE，包括平流方程、连续性方程和Liouville方程。该研究为近似输运方程（包括Koopman算子）的特征函数开发了新方案，并引入了一种数据驱动的方法来学习为这些近似量身定制的核。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a unified theoretical and computational framework for constructing reproducing kernels tailored to transport equations and adapted to Koopman eigenfunctions of nonlinear dynamical systems. These eigenfunctions satisfy a transport-type partial differential equation (PDE) that we invert using three analytically grounded methods: (i) A Lions-type variational principle in a reproducing kernel Hilbert space (RKHS), (ii) convolution with a Green's function, and (iii) a resolvent operator constructed via Laplace transforms along characteristic flows. We prove that these three constructions yield identical kernels under mild smoothness and causality assumptions. We further show that the associated kernel eigenfunctions (Mercer modes) converge in L^2 to true Koopman eigenfunctions when the latter lie in the RKHS. Our approach is numerically realized through a mesh-free, convex optimization framework, enhanced with boundary regularization to handle eigenfunction blow-up. A multiple-kernel learning (MKL) scheme selects kernels automatically via residual minimization. Finally, we demonstrate that the same framework applies verbatim to a broader class of linear transport PDEs, including the advection, continuity, and Liouville equations. The unification of variational principles, Green's functions, and the method of characteristics enables the development of novel schemes for approximating eigenfunctions of transport equations, including those of the Koopman operator, and introduces a data-driven approach for learning kernels tailored to these approximations. Numerical experiments confirm the practical utility and robustness of the method.

</details>

---

### 13. [NuNext: Reframing Nucleus Detection as Next-Point Detection](https://arxiv.org/abs/2603.07098)

**基本信息**

- 🔗 arXiv: [`2603.07098`](https://arxiv.org/abs/2603.07098)
- 👥 作者: Zhongyi Shui, Honglin Li, Xiaozhong Ji 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07098.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法（NuNext）利用多模态大语言模型直接预测细胞核坐标，这体现了“化学大模型”（广义上指用于科学问题的大模型）在生物医学图像分析中的一种应用范式。虽然应用领域不同，但其“大模型驱动结构化输出生成”的核心方法与关注主题中的方法论精神相关。

**📖 中文摘要**

本文提出了一种新颖的细胞核检测方法NuNext，将细胞核检测任务重新定义为下一个点预测问题。该方法的核心是开发了一个多模态大语言模型，能够直接从输入的组织病理学图像中输出前景细胞核的质心坐标。模型训练分为两个阶段：监督学习阶段和强化微调阶段。在监督学习阶段，作者提出了空间感知的软监督来放松严格的质心匹配，并采用视觉思维链策略来整合有助于坐标预测的视觉先验。在强化微调阶段，设计了分布匹配奖励、低方差组过滤和细粒度优势塑造来进一步提升模型的检测质量。这项工作展示了将大语言模型（作为化学信息学/生物信息学中“化学大模型”概念在特定生物医学图像分析任务中的一种应用实例）直接用于生成结构化坐标输出的潜力，虽然其直接应用领域是生物医学图像，但其“将检测任务重构为语言模型驱动的坐标生成问题”的核心思想，与“化学大模型”用于分子结构生成或“质谱结构推理”中从谱图数据生成分子结构的思想在方法论层面有相似之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Nucleus detection in histopathology is pivotal for a wide range of clinical applications. Existing approaches either regress nuclear proxy maps that require complex post-processing, or employ dense anchors or queries that introduce severe foreground-background imbalance. In this work, we reformulate nucleus detection as next-point prediction, wherein a multimodal large language model is developed to directly output foreground nucleus centroids from the input image. The model is trained in two stages. In the supervised learning stage, we propose spatial-aware soft supervision to relax strict centroid matching and a chain-of-visual-thought strategy to incorporate visual priors that facilitate coordinate prediction. In the reinforcement fine-tuning stage, we design distribution matching reward, low-variance group filtering, and fine-grained advantage shaping to further improve the model's detection quality. Extensive experiments on nine widely used benchmarks demonstrate the superiority of our method. Code will be released soon.

</details>

---

### 14. [Toward Multimodal Industrial Fault Analysis: A Single-Speed Chain Conveyor Dataset with Audio and Vibration Signals](https://arxiv.org/abs/2603.07130)

**基本信息**

- 🔗 arXiv: [`2603.07130`](https://arxiv.org/abs/2603.07130)
- 👥 作者: Zhang Chen, Yucong Zhang, Xiaoxiao Miao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07130.pdf)

**💡 相关性分析**

满足标准2：论文贡献了一个专注于工业故障分析的多模态数据集，其中包含音频和振动信号。虽然其直接应用是机械故障诊断，但该数据集作为多模态时序信号资源，其构建理念、评估协议和基线方法，对于“化学大模型”或“质谱结构推理”领域研究多模态数据融合（例如，结合质谱、光谱、文本信息）或处理时序/频谱信号具有参考价值，可被视为一种相关数据资源范例。

**📖 中文摘要**

本文介绍了一个用于工业故障分析的多模态数据集，该数据集采集自单速链式输送机系统，包含音频和振动信号。数据集涵盖了正常运行状态和四种代表性故障类型，并在多种速度、负载以及清洁/工厂噪声条件下采集。该数据集明确设计用于支持通道级分析和多模态融合研究。作者为仅使用正常数据训练的无监督故障检测和使用平衡数据集分割的监督故障分类建立了标准化的评估协议，并提供了一个统一的通道级kNN基线，用于在不进行任务特定训练的情况下公平比较表示质量。该数据集为鲁棒的多模态工业故障分析提供了一个实用且可扩展的基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a multimodal industrial fault analysis dataset collected from a single-speed chain conveyor (SSCC) system, targeting system-level fault detection in production lines. The dataset consists of multimodal signals, including three audio and four vibration channels. It covers normal operation and four representative fault types under multiple speeds, loads, and both clean and realistic factory-noise conditions reproduced on-site. It is explicitly designed to support channel-wise analysis and multimodal fusion research. We establish standardized evaluation protocols for unsupervised fault detection with normal-only training and supervised fault classification with balanced dataset splits across different operating conditions and fault types. A unified channel-wise kNN baseline is provided to enable fair comparison of representation quality without task-specific training. The dataset offers a practical and extensible benchmark for robust multimodal industrial fault analysis.

</details>

---

### 15. [Towards Objective Gastrointestinal Auscultation: Automated Segmentation and Annotation of Bowel Sound Patterns](https://arxiv.org/abs/2603.07215)

**基本信息**

- 🔗 arXiv: [`2603.07215`](https://arxiv.org/abs/2603.07215)
- 👥 作者: Zahra Mansour, Verena Uslar, Dirk Weyhe 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07215.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于肠道声音自动分析的完整流程，包括事件检测和基于预训练Transformer模型的分类。虽然应用领域是医学声学，但其核心是处理和分析复杂的、信息稀疏的时序/频谱信号（肠道声音），并从中识别有意义的模式。这种方法论与“质谱结构推理”中从质谱信号（也是一种复杂的频谱信号）推断分子结构在信号处理、特征提取和模式识别层面具有高度的相似性和可借鉴性。

**📖 中文摘要**

本文提出了一种用于肠道声音自动分割和分类的流程，旨在实现胃肠道听诊的客观化和定量化。研究使用可穿戴声学传感器采集肠道声音信号，并开发了基于能量的时间检测算法来检测声音事件。检测到的声音片段随后使用预训练的音频频谱图Transformer模型进行分类。该研究构建了一个包含手动标注数据的数据集用于训练自动标注算法，该算法将手动标注时间减少了约70%。这项工作展示了如何利用深度学习模型（AST）对生物声学信号进行自动分析和模式识别，最终目标是提供客观的诊断工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bowel sounds (BS) are typically momentary and have low amplitude, making them difficult to detect accurately through manual auscultation. This leads to significant variability in clinical assessment. Digital acoustic sensors allow the acquisition of high-quality BS and enable automated signal analysis, offering the potential to provide clinicians with both objective and quantitative feedback on bowel activity. This study presents an automated pipeline for bowel sound segmentation and classification using a wearable acoustic SonicGuard sensor. BS signals from 83 subjects were recorded using a SonicGuard sensor. Data from 40 subjects were manually annotated by clinical experts and used to train an automatic annotation algorithm, while the remaining subjects were used for further model evaluation. An energy-based event detection algorithm was developed to detect BS events. Detected sound segments were then classified into BS patterns using a pretrained Audio Spectrogram Transformer (AST) model. Model performance was evaluated separately for healthy individuals and patients. The best configuration used two specialized models, one trained on healthy subjects and one on patients, achieving (accuracy: 0.97, AUROC: 0.98) for healthy group and (accuracy: 0.96, AUROC: 0.98) for patient group. The auto-annotation method reduced manual labeling time by approximately 70%, and expert review showed that less than 12% of automatically detected segments required correction. The proposed automated segmentation and classification system enables quantitative assessment of bowel activity, providing clinicians with an objective diagnostic tool that may improve the diagnostic of gastrointestinal function and support the annotation of large-scale datasets.

</details>

---

### 16. [Retrieval-Augmented Generation for Predicting Cellular Responses to Gene Perturbation](https://arxiv.org/abs/2603.07233)

**基本信息**

- 🔗 arXiv: [`2603.07233`](https://arxiv.org/abs/2603.07233)
- 👥 作者: Andrea Giuseppe Di Francesco, Andrea Rubbi, Pietro Liò
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07233.pdf)

**💡 相关性分析**

满足标准1：论文的核心贡献PT-RAG是一个检索增强生成框架，专门为预测细胞对基因扰动的反应而设计。这直接属于“化学信息学”和计算生物学交叉领域的研究。其将RAG范式应用于生物分子数据推理的方法创新，与“化学大模型”和“质谱结构推理”中利用外部知识增强模型推理能力的研究主题高度相关。

**📖 中文摘要**

本文提出了PT-RAG，一个用于预测细胞对基因扰动反应的新型检索增强生成框架。该框架将检索增强生成范式从传统的语言模型应用扩展到细胞生物学领域。与为标准文本检索设计的RAG系统不同，扰动检索缺乏既定的相似性度量，需要学习什么构成相关上下文，这使得可微分检索至关重要。PT-RAG通过一个两阶段流程解决这个问题：首先使用GenePT嵌入检索候选扰动，然后通过Gumbel-Softmax离散采样，根据细胞状态和输入扰动自适应地细化选择。这种细胞类型感知的可微分检索实现了检索目标与生成的端到端联合优化。在Replogle-Nadig单基因扰动数据集上的实验表明，PT-RAG在相同实验条件下优于STATE和普通RAG。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting how cells respond to genetic perturbations is fundamental to understanding gene function, disease mechanisms, and therapeutic development. While recent deep learning approaches have shown promise in modeling single-cell perturbation responses, they struggle to generalize across cell types and perturbation contexts due to limited contextual information during generation. We introduce PT-RAG (Perturbation-aware Two-stage Retrieval-Augmented Generation), a novel framework that extends Retrieval-Augmented Generation beyond traditional language-model applications to cellular biology. Unlike standard RAG systems designed for text retrieval with pre-trained LLMs, perturbation retrieval lacks established similarity metrics and requires learning what constitutes relevant context, making differentiable retrieval essential. PT-RAG addresses this through a two-stage pipeline: first, retrieving candidate perturbations $K$ using GenePT embeddings, then adaptively refining the selection through Gumbel-Softmax discrete sampling conditioned on both the cell state and the input perturbation. This cell-type-aware differentiable retrieval enables end-to-end optimization of the retrieval objective jointly with generation. On the Replogle-Nadig single-gene perturbation dataset, we demonstrate that PT-RAG outperforms both STATE and vanilla RAG under identical experimental conditions, with the strongest gains in distributional similarity metrics ($W_1$, $W_2$). Notably, vanilla RAG's dramatic failure is itself a key finding: it demonstrates that differentiable, cell-type-aware retrieval is essential in this domain, and that naive retrieval can actively harm performance. Our results establish retrieval-augmented generation as a promising paradigm for modelling cellular responses to gene perturbation. The code to reproduce our experiments is available at this https URL .

</details>

---

### 17. [Turning Time Series into Algebraic Equations: Symbolic Machine Learning for Interpretable Modeling of Chaotic Time Series](https://arxiv.org/abs/2603.07261)

**基本信息**

- 🔗 arXiv: [`2603.07261`](https://arxiv.org/abs/2603.07261)
- 👥 作者: Madhurima Panja, Grace Younes, Tanujit Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07261.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究是开发可解释的符号机器学习模型用于时间序列预测。虽然应用场景是混沌时间序列，但其“从数据中学习可解释的代数方程/符号表达式”的核心方法论，与“化学信息学”中长期追求的目标——从化学数据（如质谱、分子描述符）中发现可解释的定量构效关系或反应规则——在本质上是一致的。因此，该论文的方法对“化学大模型”（追求可解释性）和“质谱结构推理”（寻求谱图与结构之间的可解释映射）具有重要的方法论参考价值。

**📖 中文摘要**

本文针对混沌时间序列预测的难题，提出了两种可解释的符号预测器，用于从混沌时间序列数据中学习显式的、可解释的代数方程。符号神经预测器（SyNF）将基于神经网络的方程学习架构适配到预测场景，实现完全可微分的紧凑且可解释的代数关系发现。符号树预测器（SyTF）基于进化符号回归，直接在精度-复杂度权衡下搜索方程结构。这两种方法旨在提供透明方程，以揭示潜在动力学的显著方面，而不仅仅是黑箱预测。在132个低维混沌吸引子基准和两个真实世界混沌时间序列上的实验表明，符号预测器在获得有竞争力的一步超前预测精度的同时，提供了可解释的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chaotic time series are notoriously difficult to forecast. Small uncertainties in initial conditions amplify rapidly, while strong nonlinearities and regime dependent variability constrain predictability. Although modern deep learning often delivers strong short horizon accuracy, its black box nature limits scientific insight and practical trust in settings where understanding the underlying dynamics matters. To address this gap, we propose two complementary symbolic forecasters that learn explicit, interpretable algebraic equations from chaotic time series data. Symbolic Neural Forecaster (SyNF) adapts a neural network based equation learning architecture to the forecasting setting, enabling fully differentiable discovery of compact and interpretable algebraic relations. The Symbolic Tree Forecaster (SyTF) builds on evolutionary symbolic regression to search directly over equation structures under a principled accuracy complexity trade off. We evaluate both approaches in a rolling window nowcasting setting with one step ahead forecasting using several accuracy metrics and compare against a broad suite of baselines spanning classical statistical models, tree ensembles, and modern deep learning architectures. Numerical experiments cover a benchmark of 132 low dimensional chaotic attractors and two real world chaotic time series, namely weekly dengue incidence in San Juan and the Nino 3.4 sea surface temperature index. Across datasets, symbolic forecasters achieve competitive one step ahead accuracy while providing transparent equations that reveal salient aspects of the underlying dynamics.

</details>

---

### 18. [AutoDataset: A Lightweight System for Continuous Dataset Discovery and Search](https://arxiv.org/abs/2603.07271)

**基本信息**

- 🔗 arXiv: [`2603.07271`](https://arxiv.org/abs/2603.07271)
- 👥 作者: Junzhe Yang, Xinghao Chen, Yunuo Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07271.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个自动化系统（AutoDataset），用于从arXiv等来源持续发现和索引新发布的数据集，这为化学信息学和质谱分析领域的研究者提供了获取相关数据集（如化学或质谱数据集）的宝贵工具和资源。

**📖 中文摘要**

这篇论文介绍了AutoDataset，一个用于实时数据集发现和检索的轻量级自动化系统。该系统通过持续监控arXiv，直接从新发表的研究论文中检测和索引数据集。它采用了一个低开销的多阶段流程：首先，一个轻量级分类器快速筛选标题和摘要，以识别发布数据集的论文；然后，解析PDF以提取数据集描述和URL；最后，使用密集语义检索器对结构化记录进行索引，以实现低延迟的自然语言搜索。该系统作为一个实时系统部署，持续接收新论文并提供最新的数据集发现服务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The continuous expansion of task-specific datasets has become a major driver of progress in machine learning. However, discovering newly released datasets remains difficult, as existing platforms largely depend on manual curation or community submissions, leading to limited coverage and substantial delays. To address this challenge, we introduce AutoDataset, a lightweight, automated system for real-time dataset discovery and retrieval. AutoDataset adopts a paper-first approach by continuously monitoring arXiv to detect and index datasets directly from newly published research. The system operates through a low-overhead multi-stage pipeline. First, a lightweight classifier rapidly filters titles and abstracts to identify papers releasing datasets, achieving an F1 score of 0.94 with an inference latency of 11 ms. For identified papers, we parse PDFs with GROBID and apply a sentence-level extractor to extract dataset descriptions. Dataset URLs are extracted from the paper text with an automated fallback to LaTeX source analysis when needed. Finally, the structured records are indexed using a dense semantic retriever, enabling low-latency natural language search. We deploy AutoDataset as a live system that continuously ingests new papers and provides up-to-date dataset discovery. In practice, it has been shown to significantly reduce the time required for researchers to locate newly released datasets, improving dataset discovery efficiency by up to 80%.

</details>

---

### 19. [Variational Flow Maps: Make Some Noise for One-Step Conditional Generation](https://arxiv.org/abs/2603.07276)

**基本信息**

- 🔗 arXiv: [`2603.07276`](https://arxiv.org/abs/2603.07276)
- 👥 作者: Abbas Mammadov, So Takao, Bohan Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07276.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕生成模型（流映射）及其在条件生成和逆问题求解中的应用。虽然未明确提及化学或质谱，但其提出的“学习初始噪声以进行条件生成”的框架，在概念上与“质谱结构推理”这类需要从观测数据（质谱）反推结构（分子）的逆问题高度相关，为这类推理任务提供了潜在的方法论。

**📖 中文摘要**

这篇论文提出了变分流映射（Variational Flow Maps, VFMs），这是一个用于条件生成（包括解决逆问题）的框架。该框架的核心思想是将条件生成从“引导采样路径”转变为“学习合适的初始噪声”。具体来说，给定一个观测值，模型学习一个噪声适配器，该适配器输出一个噪声分布，使得通过流映射映射到数据空间后，生成的样本能够符合观测值和数据先验。论文开发了一个原则性的变分目标来联合训练噪声适配器和流映射，从而在单步或少数步骤内实现从复杂数据后验中采样。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow maps enable high-quality image generation in a single forward pass. However, unlike iterative diffusion models, their lack of an explicit sampling trajectory impedes incorporating external constraints for conditional generation and solving inverse problems. We put forth Variational Flow Maps, a framework for conditional sampling that shifts the perspective of conditioning from "guiding a sampling path", to that of "learning the proper initial noise". Specifically, given an observation, we seek to learn a noise adapter model that outputs a noise distribution, so that after mapping to the data space via flow map, the samples respect the observation and data prior. To this end, we develop a principled variational objective that jointly trains the noise adapter and the flow map, improving noise-data alignment, such that sampling from complex data posterior is achieved with a simple adapter. Experiments on various inverse problems show that VFMs produce well-calibrated conditional samples in a single (or few) steps. For ImageNet, VFM attains competitive fidelity while accelerating the sampling by orders of magnitude compared to alternative iterative diffusion/flow models. Code is available at this https URL

</details>

---

### 20. [LLM-FK: Multi-Agent LLM Reasoning for Foreign Key Detection in Large-Scale Complex Databases](https://arxiv.org/abs/2603.07278)

**基本信息**

- 🔗 arXiv: [`2603.07278`](https://arxiv.org/abs/2603.07278)
- 👥 作者: Zijian Tang, Ying Zhang, Sibo Cai 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07278.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用多智能体大语言模型（LLM）进行复杂推理（外键检测）。虽然应用领域是数据库，但其核心方法论——利用多智能体LLM协作进行结构化推理和知识注入——与“化学大模型”领域探索的、利用LLM进行复杂化学推理（如分子性质预测、反应规划）的研究范式高度一致，属于大模型在结构化、知识密集型任务中的应用。

**📖 中文摘要**

这篇论文提出了LLM-FK，一个用于大规模复杂数据库中外键检测的多智能体大语言模型推理框架。该框架协调四个专门的智能体：分析器（分解问题并剪枝搜索空间）、解释器（注入自增强的领域知识）、精炼器（构建紧凑的结构表示并进行多视角思维链推理）和验证器（通过整体冲突解决策略强制执行模式范围的一致性）。实验表明，LLM-FK在基准数据集上取得了优异的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Detecting missing foreign keys (FKs) requires accurately modeling semantic dependencies across database schemas, which conventional heuristic-based methods are fundamentally limited in capturing. We propose LLM-FK, the first fully automated multi-agent framework for FK detection, designed to address three core challenges that hinder naive LLM-based solutions in large-scale complex databases: combinatorial search space explosion, ambiguous inference under limited context, and global inconsistency arising from isolated local predictions. LLM-FK coordinates four specialized agents: a Profiler that decomposes the FK detection problem into the task of validating FK candidate column pairs and prunes the search space via a unique-key-driven schema decomposition strategy; an Interpreter that injects self-augmented domain knowledge; a Refiner that constructs compact structural representations and performs multi-perspective chain-of-thought reasoning; and a Verifier that enforces schema-wide consistency through a holistic conflict resolution strategy. Experiments on five benchmark datasets demonstrate that LLM-FK consistently achieves F1-scores above 93%, surpassing existing baselines by 15% on the large-scale MusicBrainz database, while reducing the candidate search space by two to three orders of magnitude without losing true FKs and maintaining robustness under challenging conditions like missing data. These results demonstrate the effectiveness and scalability of LLM-FK in real-world databases.

</details>

---

### 21. [Learning Concept Bottleneck Models from Mechanistic Explanations](https://arxiv.org/abs/2603.07343)

**基本信息**

- 🔗 arXiv: [`2603.07343`](https://arxiv.org/abs/2603.07343)
- 👥 作者: Antonio De Santis, Schrasing Tong, Marco Brambilla 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07343.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进概念瓶颈模型（CBM），这是一种旨在实现事前可解释性的人工智能模型。其提出的方法（使用SAEs提取模型内部概念并用多模态LLM标注）涉及大语言模型（LLM）在理解和标注机器学习模型内部表示方面的应用，这与“化学大模型”领域关注的可解释AI、以及将领域知识（如化学概念）注入模型的研究方向相关。

**📖 中文摘要**

这篇论文提出了机理概念瓶颈模型（Mechanistic CBM, M-CBM），一种新颖的CBM流程，直接从黑盒模型自身学习到的概念构建瓶颈层。这些概念通过稀疏自编码器（SAEs）提取，并使用多模态LLM在选定的图像子集上进行命名和注释。M-CBM旨在解决传统CBM中预定义概念预测能力不足或无法从可用数据中学习的问题。通过在多样化数据集上的实验，M-CBM在匹配的稀疏度下持续超越先前的CBMs，同时改进了概念预测并提供了简洁的解释。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept Bottleneck Models (CBMs) aim for ante-hoc interpretability by learning a bottleneck layer that predicts interpretable concepts before the decision. State-of-the-art approaches typically select which concepts to learn via human specification, open knowledge graphs, prompting an LLM, or using general CLIP concepts. However, concepts defined a-priori may not have sufficient predictive power for the task or even be learnable from the available data. As a result, these CBMs often significantly trail their black-box counterpart when controlling for information leakage. To address this, we introduce a novel CBM pipeline named Mechanistic CBM (M-CBM), which builds the bottleneck directly from a black-box model's own learned concepts. These concepts are extracted via Sparse Autoencoders (SAEs) and subsequently named and annotated on a selected subset of images using a Multimodal LLM. For fair comparison and leakage control, we also introduce the Number of Contributing Concepts (NCC), a decision-level sparsity metric that extends the recently proposed NEC metric. Across diverse datasets, we show that M-CBMs consistently surpass prior CBMs at matched sparsity, while improving concept predictions and providing concise explanations. Our code is available at this https URL .

</details>

---

### 22. [Latent Generative Models with Tunable Complexity for Compressed Sensing and other Inverse Problems](https://arxiv.org/abs/2603.07357)

**基本信息**

- 🔗 arXiv: [`2603.07357`](https://arxiv.org/abs/2603.07357)
- 👥 作者: Sean Gunn, Jorio Cocola, Oliver De Candido 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07357.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于生成模型（扩散模型、归一化流、VAE）的“可调复杂度先验”，以更好地解决逆问题（如压缩感知、去噪）。逆问题求解是“质谱结构推理”的核心（从质谱数据反推分子结构）。因此，该论文提出的方法论直接适用于质谱结构推理这类逆问题，为其提供了新的生成模型先验设计思路。

**📖 中文摘要**

这篇论文为扩散模型、归一化流和变分自编码器开发了可调复杂度的先验，利用嵌套丢弃技术。研究表明，在包括压缩感知、修复、去噪和相位恢复等任务中，可调先验始终比固定复杂度的基线实现更低的重建误差。在线性去噪设置中，论文提供了理论分析，明确描述了最优调优参数如何依赖于噪声和模型结构。这项工作展示了可调复杂度生成先验的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have emerged as powerful priors for solving inverse problems. These models typically represent a class of natural signals using a single fixed complexity or dimensionality. This can be limiting: depending on the problem, a fixed complexity may result in high representation error if too small, or overfitting to noise if too large. We develop tunable-complexity priors for diffusion models, normalizing flows, and variational autoencoders, leveraging nested dropout. Across tasks including compressed sensing, inpainting, denoising, and phase retrieval, we show empirically that tunable priors consistently achieve lower reconstruction errors than fixed-complexity baselines. In the linear denoising setting, we provide a theoretical analysis that explicitly characterizes how the optimal tuning parameter depends on noise and model structure. This work demonstrates the potential of tunable-complexity generative priors and motivates both the development of supporting theory and their application across a wide range of inverse problems.

</details>

---

### 23. [ConfHit: Conformal Generative Design with Oracle Free Guarantees](https://arxiv.org/abs/2603.07371)

**基本信息**

- 🔗 arXiv: [`2603.07371`](https://arxiv.org/abs/2603.07371)
- 👥 作者: Siddhartha Laghuvarapu, Ying Jin, Jimeng Sun
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07371.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将保形预测（一种提供统计保证的框架）与生成模型相结合，用于分子设计等科学发现任务。这直接与“化学大模型”和“质谱结构推理”相关，因为后者本质上涉及从数据（如质谱）生成或筛选候选分子结构，而ConfHit提供的统计可靠性保证正是该领域实际应用（如药物发现）所迫切需要的。

**📖 中文摘要**

这篇论文介绍了ConfHit，一个用于生成设计的保形预测框架，旨在提供在预算有限、缺乏实验验证（oracle）和存在分布偏移条件下的有效性保证。ConfHit形式化了两个核心问题：（i）认证：能否以用户指定的置信水平保证生成的一批候选物中至少包含一个“命中”（例如，具有所需属性的分子）；（ii）设计：生成过程能否被优化为一个紧凑的集合而不削弱这种保证。该框架利用历史样本和生成样本之间的加权可交换性来消除对实验验证的需求，并构建了多样本密度比加权保形p值来量化对“命中”的统计置信度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of deep generative models in scientific discovery requires not only the ability to generate novel candidates but also reliable guarantees that these candidates indeed satisfy desired properties. Recent conformal-prediction methods offer a path to such guarantees, but its application to generative modeling in drug discovery is limited by budget constraints, lack of oracle access, and distribution shift. To this end, we introduce ConfHit, a distribution-free framework that provides validity guarantees under these conditions. ConfHit formalizes two central questions: (i) Certification: whether a generated batch can be guaranteed to contain at least one hit with a user-specified confidence level, and (ii) Design: whether the generation can be refined to a compact set without weakening this guarantee. ConfHit leverages weighted exchangeability between historical and generated samples to eliminate the need for an experimental oracle, constructs multiple-sample density-ratio weighted conformal p-value to quantify statistical confidence in hits, and proposes a nested testing procedure to certify and refine candidate sets of multiple generated samples while maintaining statistical guarantees. Across representative generative molecule design tasks and a broad range of methods, ConfHit consistently delivers valid coverage guarantees at multiple confidence levels while maintaining compact certified sets, establishing a principled and reliable framework for generative modeling.

</details>

---

### 24. [SoK: Agentic Retrieval-Augmented Generation (RAG): Taxonomy, Architectures, Evaluation, and Research Directions](https://arxiv.org/abs/2603.07379)

**基本信息**

- 🔗 arXiv: [`2603.07379`](https://arxiv.org/abs/2603.07379)
- 👥 作者: Saroj Mishra, Suman Niroula, Umesh Yadav 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07379.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对“智能体化检索增强生成”（Agentic RAG）的系统性综述（SoK）。RAG是当前大模型（包括化学大模型）增强知识获取和推理能力的关键技术。这篇论文对该领域的架构、评估和风险进行了全面的梳理和展望，为包括化学信息学在内的领域研究者理解和构建更可靠、可扩展的基于大模型的智能系统提供了重要的综述和讨论。

**📖 中文摘要**

这篇系统知识（SoK）论文为“智能体化检索增强生成”（Agentic RAG）提供了首个统一框架。论文将智能体化检索-生成循环形式化为有限视界部分可观测马尔可夫决策过程，明确建模其控制策略和状态转移。在此基础上，论文开发了一个全面的分类法和模块化架构分解，按规划机制、检索编排、记忆范式和工具调用行为对系统进行分类。论文进一步分析了传统静态评估实践的关键局限性，并识别了自主循环固有的系统性风险。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-Augmented Generation (RAG) systems are increasingly evolving into agentic architectures where large language models autonomously coordinate multi-step reasoning, dynamic memory management, and iterative retrieval strategies. Despite rapid industrial adoption, current research lacks a systematic understanding of Agentic RAG as a sequential decision-making system, leading to highly fragmented architectures, inconsistent evaluation methodologies, and unresolved reliability risks. This Systematization of Knowledge (SoK) paper provides the first unified framework for understanding these autonomous systems. We formalize agentic retrieval-generation loops as finite-horizon partially observable Markov decision processes, explicitly modeling their control policies and state transitions. Building upon this formalization, we develop a comprehensive taxonomy and modular architectural decomposition that categorizes systems by their planning mechanisms, retrieval orchestration, memory paradigms, and tool-invocation behaviors. We further analyze the critical limitations of traditional static evaluation practices and identify severe systemic risks inherent to autonomous loops, including compounding hallucination propagation, memory poisoning, retrieval misalignment, and cascading tool-execution vulnerabilities. Finally, we outline key doctoral-scale research directions spanning stable adaptive retrieval, cost-aware orchestration, formal trajectory evaluation, and oversight mechanisms, providing a definitive roadmap for building reliable, controllable, and scalable agentic retrieval systems.

</details>

---

### 25. [Interpretable Aneurysm Classification via 3D Concept Bottleneck Models: Integrating Morphological and Hemodynamic Clinical Features](https://arxiv.org/abs/2603.07399)

**基本信息**

- 🔗 arXiv: [`2603.07399`](https://arxiv.org/abs/2603.07399)
- 👥 作者: Toqa Khaled, Ahmad Al-Kabbany
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07399.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是概念瓶颈模型（CBM）在3D医学影像分析中的应用。CBM是一种旨在实现事前可解释性的人工智能模型，通过将预测与人类可理解的概念（如形态特征）相关联。虽然应用领域是医学，但其核心方法论——构建可解释的、基于概念的深度学习模型——与“化学大模型”领域中对可解释AI、以及将化学知识（如官能团、子结构）作为概念注入模型的研究方向高度相关。

**📖 中文摘要**

这篇论文提出了一个端到端的3D概念瓶颈框架，用于颅内动脉瘤的分类和评估。该框架将高维神经影像特征映射到一组离散的、人类可理解的形态学和血流动力学概念上。通过使用预训练的3D ResNet/DenseNet骨干网络提取特征，并通过一个代表临床概念的软瓶颈层进行处理，模型使用联合损失函数进行优化。结果表明，该框架在保持高预测准确率（峰值达93.33%）的同时，提供了事前可解释性，证明了在不牺牲可解释性的情况下实现高性能的可行性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We are concerned with the challenge of reliably classifying and assessing intracranial aneurysms using deep learning without compromising clinical transparency. While traditional black-box models achieve high predictive accuracy, their lack of inherent interpretability remains a significant barrier to clinical adoption and regulatory approval. Explainability is paramount in medical modeling to ensure that AI-driven diagnoses align with established neurosurgical principles. Unlike traditional eXplainable AI (XAI) methods -- such as saliency maps, which often provide post-hoc, non-causal visual correlations -- Concept Bottleneck Models (CBMs) offer a robust alternative by constraining the model's internal logic to human-understandable clinical indices. In this article, we propose an end-to-end 3D Concept Bottleneck framework that maps high-dimensional neuroimaging features to a discrete set of morphological and hemodynamic concepts for aneurysm identification. We implemented this pipeline using a pre-trained 3D ResNet-34 backbone and a 3D DenseNet-121 to extract features from CTA volumes, which were subsequently processed through a soft bottleneck layer representing human-interpretable clinical concepts. The model was optimized using a joint-loss function to balance diagnostic focal loss and concept mean squared error (MSE), validated via stratified five-fold cross-validation. Our results demonstrate a peak task classification accuracy of 93.33% +/- 4.5% for the ResNet-34 architecture and 91.43% +/- 5.8% for the DenseNet-121 model. Furthermore, the implementation of 8-pass Test-Time Augmentation (TTA) yielded a robust mean accuracy of 88.31%, ensuring diagnostic stability during inference. By maintaining an accuracy-generalization gap of less than 0.04, this framework proves that high predictive performance can be achieved without sacrificing interpretability.

</details>

---

### 26. [Context Channel Capacity: An Information-Theoretic Framework for Understanding Catastrophic Forgetting](https://arxiv.org/abs/2603.07415)

**基本信息**

- 🔗 arXiv: [`2603.07415`](https://arxiv.org/abs/2603.07415)
- 👥 作者: Ran Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从信息论角度理解并解决持续学习中的灾难性遗忘问题，提出了“上下文通道容量”这一理论框架。虽然不直接针对化学或质谱，但其对“大模型”（此处指神经网络架构）在持续学习场景下行为机理的深入分析和提出的设计原则（“架构优于算法”），对于构建能够持续学习新化学知识或质谱推理任务而不遗忘的“化学大模型”具有重要的理论指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Catastrophic forgetting remains a central challenge in continual learning (CL), yet lacks a unified information-theoretic explanation for why some architectures forget catastrophically while others do not. We introduce \emph{Context Channel Capacity} ($C_\mathrm{ctx}$), the mutual information between a CL architecture's context signal and its generated parameters, and prove that zero forgetting requires $C_\mathrm{ctx} \geq H(T)$, where $H(T)$ is the task identity entropy. We establish an \emph{Impossibility Triangle} -- zero forgetting, online learning, and finite parameters cannot be simultaneously satisfied by sequential state-based learners -- and show that conditional regeneration architectures (HyperNetworks) bypass this triangle by redefining parameters as function values rather than states. We validate this framework across 8 CL methods on Split-MNIST (1,130+ experiments over 86 days, 4 seeds each), showing that $C_\mathrm{ctx}$ perfectly predicts forgetting behavior: methods with $C_\mathrm{ctx} = 0$ (NaiveSGD, EWC, SI, LwF, CFlow) exhibit catastrophic forgetting (6--97\%), while methods with $C_\mathrm{ctx} \approx 1$ (HyperNetwork) achieve zero forgetting (98.8\% ACC). We further propose \emph{Wrong-Context Probing} (P5), a practical diagnostic protocol for measuring $C_\mathrm{ctx}$, and extend the framework to CIFAR-10 via a novel \emph{Gradient Context Encoder} that closes the oracle gap from 23.3pp to 0.7pp. A systematic taxonomy of 15+ closed research directions -- including the Hebbian null result (frozen random features outperform learned features), CFlow's $\theta_0$-memorizer phenomenon, and the $S_N$ symmetry barrier to column specialization -- provides the community with precisely diagnosed negative results. Our central design principle: \emph{architecture over algorithm} -- the context pathway must be structurally unbypassable.

</details>

---

### 27. [OrthoFormer: Instrumental Variable Estimation in Transformer Hidden States via Neural Control Functions](https://arxiv.org/abs/2603.07431)

**基本信息**

- 🔗 arXiv: [`2603.07431`](https://arxiv.org/abs/2603.07431)
- 👥 作者: Charles Luo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07431.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进Transformer架构，使其能够进行因果推断而非仅仅相关性学习，通过嵌入工具变量估计和神经控制函数来实现。这对于“化学大模型”和“质谱结构推理”至关重要，因为这两个领域都严重依赖从观测数据（如分子描述符、质谱峰）中推断因果关系（如结构-性质关系、谱峰-子结构关系），而不仅仅是拟合关联模式。该论文为构建具有更强因果推理能力的领域大模型提供了创新的架构思路。

**📖 中文摘要**

这篇论文提出了OrthoFormer，一种将工具变量估计直接嵌入Transformer块中的因果基础架构。该框架基于四个理论支柱：结构方向性、表示正交性、因果稀疏性和端到端一致性。论文证明，对于任何有效的工具变量滞后，OrthoFormer的偏差严格小于OLS，并且残差偏差以几何速率衰减。该研究将序列建模从相关性学习转向因果学习，对在分布偏移下的鲁棒性、可解释性和可靠决策具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transformer architectures excel at sequential modeling yet remain fundamentally limited by correlational learning - they capture spurious associations induced by latent confounders rather than invariant causal mechanisms. We identify this as an epistemological challenge: standard Transformers conflate static background factors (intrinsic identity, style, context) with dynamic causal flows (state evolution, mechanism), leading to catastrophic out-of-distribution failure. We propose OrthoFormer, a causally grounded architecture that embeds instrumental variable estimation directly into Transformer blocks via neural control functions. Our framework rests on four theoretical pillars: Structural Directionality (time-arrow enforcement), Representation Orthogonality (latent-noise separation), Causal Sparsity (Markov Blanket approximation), and End-to-End Consistency (gradient- detached stage separation). We prove that OrthoFormer achieves bias strictly less than OLS for any valid instrument lag, with residual bias decaying geometrically as O(\r{ho}k ). We characterize the bias-variance-exogeneity trilemma inherent in self-instrumenting and identify the neural forbidden regression - where removing gradient detachment improves prediction loss while destroying causal validity. Experiments confirm all theoretical predictions. OrthoFormer represents a paradigm shift from correlational to causal sequence modeling, with implications for robustness, interpretability, and reliable decision-making under distribution shift.

</details>

---

### 28. [Data Agent: Learning to Select Data via End-to-End Dynamic Optimization](https://arxiv.org/abs/2603.07433)

**基本信息**

- 🔗 arXiv: [`2603.07433`](https://arxiv.org/abs/2603.07433)
- 👥 作者: Suorong Yang, Fangjian Su, Hai Gan 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07433.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用强化学习智能体（Agent）来动态选择训练数据，以优化模型训练效率。这属于“大模型”训练优化方法学的研究。虽然应用是通用的，但其提出的“智能体化”数据选择框架，对于训练数据量大、标注成本高的“化学大模型”或质谱分析模型具有直接的应用价值，可以帮助更高效地利用化学或质谱数据集进行模型训练。

**📖 中文摘要**

这篇论文提出了Data Agent，一个端到端的动态数据选择框架，将数据选择表述为一个训练感知的顺序决策问题。智能体学习一个样本级的选择策略，该策略与模型优化共同进化，并由一个复合奖励指导，该奖励整合了基于损失的难度信号和基于置信度的不确定性信号。奖励信号捕获了优化影响和信息增益的互补目标，并带有无需调参的自适应加权机制。大量实验表明，Data Agent在广泛的数据集和架构上持续加速训练，同时保持或提高性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dynamic Data selection aims to accelerate training by prioritizing informative samples during online training. However, existing methods typically rely on task-specific handcrafted metrics or static/snapshot-based criteria to estimate sample importance, limiting scalability across learning paradigms and making it difficult to capture the evolving utility of data throughout training. To address this challenge, we propose Data Agent, an end-to-end dynamic data selection framework that formulates data selection as a training-aware sequential decision-making problem. The agent learns a sample-wise selection policy that co-evolves with model optimization, guided by a composite reward that integrates loss-based difficulty and confidence-based uncertainty signals. The reward signals capture complementary objectives of optimization impact and information gain, together with a tuning-free adaptive weighting mechanism that balances these signals over training. Extensive experiments across a wide range of datasets and architectures demonstrate that Data Agent consistently accelerates training while preserving or improving performance, e.g., reducing costs by over 50\% on ImageNet-1k and MMLU with lossless performance. Moreover, its dataset-agnostic formulation and modular reward make it plug-and-play across tasks and scenarios, e.g., robustness to noisy datasets, highlighting its potential in real-world scenarios.

</details>

---

### 29. [Med-Evo: Test-time Self-evolution for Medical Multimodal Large Language Models](https://arxiv.org/abs/2603.07443)

**基本信息**

- 🔗 arXiv: [`2603.07443`](https://arxiv.org/abs/2603.07443)
- 👥 作者: Dunyuan Xu, Xikai Yang, Juzheng Miao 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07443.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对医学多模态大语言模型（MLLMs）的自进化（Self-evolution）框架，利用无标签强化学习进行持续改进。这直接属于“大模型”能力提升和适应特定领域（此处为医学）的方法论研究。其核心思想（利用模型自身生成的数据进行强化学习优化）可以迁移到“化学大模型”或“质谱分析”领域，用于在缺乏大量标注数据的情况下持续优化领域专用的大模型。

**📖 中文摘要**

这篇论文提出了Med-Evo，首个用于医学多模态大语言模型（MLLMs）的自进化框架，该框架利用无标签强化学习来提升模型性能，而无需额外的标注数据。框架引入了两个关键创新：（1）特征驱动伪标签，从所有异构候选响应中识别语义质心以选择伪标签；（2）硬-软奖励，结合精确匹配与令牌级评估和语义相似性来提供分层奖励。在三个医学VQA基准和两个基础MLLM上的实验表明，该方法优于现有技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medical Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities across diverse healthcare tasks. However, current post-training strategies, such as supervised fine-tuning and reinforcement learning, heavily depend on substantial annotated data while overlooking the potential of unlabeled test data for model enhancement. This limitation becomes particularly pronounced in medical domains, where acquiring extensive labeled medical data is difficult due to the strict data sensitivity and annotation complexity. Moreover, leveraging test data poses challenges in generating reliable supervision signals from unlabeled samples and maintaining stable self-evolution. To address these limitations, we propose Med-Evo, the first self-evolution framework for medical MLLMs that utilizes label-free reinforcement learning to promote model performance without requiring additional labeled data. Our framework introduces two key innovations: $1)$ Feature-driven Pseudo Labeling (FPL) that identifies semantic centroids from all heterogeneous candidate responses to select pseudo labels in each rollout, and $2)$ Hard-Soft Reward (HSR) that combines exact match with token-level assessment and semantic similarity to provide hierarchical reward. Experiments on three medical VQA benchmarks and two base MLLMs show clear advantages of our approach over SOTA methods, with significant improvements of 10.43\% accuracy and 4.68\% recall on the SLAKE dataset using Qwen2.5-VL, showing the effectiveness of our method.

</details>

---

### 30. [Contact-Guided 3D Genome Structure Generation of E. coli via Diffusion Transformers](https://arxiv.org/abs/2603.07472)

**基本信息**

- 🔗 arXiv: [`2603.07472`](https://arxiv.org/abs/2603.07472)
- 👥 作者: Mingxin Zhang, Xiaofeng Dai, Yu Yao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07472.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散Transformer的生成模型，用于从Hi-C数据生成3D基因组结构。这直接属于'化学大模型'（特别是生成模型在生物化学/结构生物学中的应用）和'质谱结构推理'（虽然本文使用Hi-C而非质谱，但其核心是'结构推理'，即从实验数据推断分子三维结构）的范畴。

**📖 中文摘要**

本研究提出了一种基于条件扩散-Transformer的框架，用于生成由Hi-C接触图引导的大肠杆菌基因组三维构象集合。该研究将基因组重建问题表述为一个条件生成建模问题，旨在采样出具有异质性的构象，其集合平均的接触与输入的Hi-C数据一致。研究构建了一个合成数据集，使用粗粒度分子动力学模拟在环状拓扑下生成染色质集合和相应的Hi-C图谱。模型在潜在扩散设置下运行，使用变分自编码器来保持每个bin的对齐并支持复制感知表示。Hi-C信息通过基于Transformer的编码器和交叉注意力注入，强制执行从Hi-C到结构的物理可解释的单向约束。该模型使用流匹配目标进行训练以实现稳定优化。在保留的集合上，生成的结构重现了输入的Hi-C距离衰减和结构相关性指标，同时保持了显著的构象多样性，证明了基于扩散的生成建模在集合水平3D基因组重建中的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this study, we present a conditional diffusion-transformer framework for generating ensembles of three-dimensional Escherichia coli genome conformations guided by Hi-C contact maps. Instead of producing a single deterministic structure, we formulate genome reconstruction as a conditional generative modeling problem that samples heterogeneous conformations whose ensemble-averaged contacts are consistent with the input Hi-C data. A synthetic dataset is constructed using coarse-grained molecular dynamics simulations to generate chromatin ensembles and corresponding Hi-C maps under circular topology. Our models operate in a latent diffusion setting with a variational autoencoder that preserves per-bin alignment and supports replication-aware representations. Hi-C information is injected through a transformer-based encoder and cross-attention, enforcing a physically interpretable one-way constraint from Hi-C to structure. The model is trained using a flow-matching objective for stable optimization. On held-out ensembles, generated structures reproduce the input Hi-C distance-decay and structural correlation metrics while maintaining substantial conformational diversity, demonstrating the effectiveness of diffusion-based generative modeling for ensemble-level 3D genome reconstruction.

</details>

---

### 31. [High-Fidelity Medical Shape Generation via Skeletal Latent Diffusion](https://arxiv.org/abs/2603.07504)

**基本信息**

- 🔗 arXiv: [`2603.07504`](https://arxiv.org/abs/2603.07504)
- 👥 作者: Guoqing Zhang, Jingyun Yang, Siqi Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07504.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的生成框架（骨骼潜在扩散框架），用于医学解剖形状的生成。这直接属于'化学大模型'（生成模型在化学/生物分子结构领域的应用）的范畴。

**📖 中文摘要**

解剖形状建模是医学数据分析中的一个基本问题。然而，解剖结构的几何复杂性和拓扑可变性给精确的解剖形状生成带来了重大挑战。在这项工作中，我们提出了一个骨骼潜在扩散框架，该框架明确地结合了结构先验，以实现高效且高保真的医学形状生成。我们引入了一个形状自编码器，其中编码器通过可微分的骨架化模块捕获全局几何信息，并将局部表面特征聚合为形状潜在表示；解码器则在稀疏采样的坐标上预测相应的隐式场。新的形状通过潜在空间扩散模型生成，随后进行神经隐式解码和网格提取。为了解决医学形状数据有限的问题，我们构建了一个大规模数据集《MedSDF》，包含多个解剖类别的表面点云和相应的有符号距离场。在MedSDF和血管数据集上的大量实验表明，与现有方法相比，所提出的方法在保持更高计算效率的同时，实现了卓越的重建和生成质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anatomy shape modeling is a fundamental problem in medical data analysis. However, the geometric complexity and topological variability of anatomical structures pose significant challenges to accurate anatomical shape generation. In this work, we propose a skeletal latent diffusion framework that explicitly incorporates structural priors for efficient and high-fidelity medical shape generation. We introduce a shape auto-encoder in which the encoder captures global geometric information through a differentiable skeletonization module and aggregates local surface features into shape latents, while the decoder predicts the corresponding implicit fields over sparsely sampled coordinates. New shapes are generated via a latent-space diffusion model, followed by neural implicit decoding and mesh extraction. To address the limited availability of medical shape data, we construct a large-scale dataset, \textit{MedSDF}, comprising surface point clouds and corresponding signed distance fields across multiple anatomical categories. Extensive experiments on MedSDF and vessel datasets demonstrate that the proposed method achieves superior reconstruction and generation quality while maintaining a higher computational efficiency compared with existing approaches. Code is available at: this https URL .

</details>

---

### 32. [A Unified View of Drifting and Score-Based Models](https://arxiv.org/abs/2603.07514)

**基本信息**

- 🔗 arXiv: [`2603.07514`](https://arxiv.org/abs/2603.07514)
- 👥 作者: Chieh-Hsin Lai, Bac Nguyen, Naoki Murata 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07514.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对漂移模型（一种生成模型）与分数匹配原理（扩散模型的基础）之间关系的理论分析。这直接属于'化学大模型'（生成模型的理论基础）的范畴。

**📖 中文摘要**

漂移模型通过优化由核函数在数据分布和模型分布之间诱导的均值漂移差异来训练一步生成器，在实践中默认使用拉普拉斯核。在每一点上，这种差异比较了朝向附近数据样本的核加权位移与朝向附近模型样本的相应位移，从而为生成的样本产生一个传输方向。在本文中，我们通过展示漂移模型在核平滑分布上允许一个基于分数的公式，来精确阐明其与扩散模型背后的分数匹配原理的关系。对于高斯核，总体均值漂移场与高斯平滑后的数据和模型分布之间的分数差一致。这一恒等式源于Tweedie公式，该公式将高斯平滑密度的分数与相应的条件均值联系起来，并意味着高斯核漂移正是平滑分布上的分数匹配式目标。这也澄清了与分布匹配蒸馏（DMD）的联系：两种方法都使用分数失配传输方向，但漂移模型通过核邻域非参数地实现分数信号，而DMD使用预训练的扩散教师模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drifting models train one-step generators by optimizing a mean-shift discrepancy induced by a kernel between the data and model distributions, with Laplace kernels used by default in practice. At each point, this discrepancy compares the kernel-weighted displacement toward nearby data samples with the corresponding displacement toward nearby model samples, yielding a transport direction for generated samples. In this paper, we make its relationship to the score-matching principle behind diffusion models precise by showing that drifting admits a score-based formulation on kernel-smoothed distributions. For Gaussian kernels, the population mean-shift field coincides with the score difference between the Gaussian-smoothed data and model distributions. This identity follows from Tweedie's formula, which links the score of a Gaussian-smoothed density to the corresponding conditional mean, and implies that Gaussian-kernel drifting is exactly a score-matching-style objective on smoothed distributions. It also clarifies the connection to Distribution Matching Distillation (DMD): both methods use score-mismatch transport directions, but drifting realizes the score signal nonparametrically from kernel neighborhoods, whereas DMD uses a pretrained diffusion teacher. Beyond Gaussians, we derive an exact decomposition for general radial kernels, and for the Laplace kernel we prove rigorous error bounds showing that drifting remains an accurate proxy for score matching in low-temperature and high-dimensional regimes.

</details>

---

### 33. [Generative prediction of laser-induced rocket ignition with dynamic latent space representations](https://arxiv.org/abs/2603.07525)

**基本信息**

- 🔗 arXiv: [`2603.07525`](https://arxiv.org/abs/2603.07525)
- 👥 作者: Tony Zahtila, Ettore Saetta, Murray Cutforth 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07525.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合卷积自编码器和神经ODE的数据驱动代理模型，用于快速预测激光点火火箭发动机的复杂多物理场过程。这属于'化学大模型'（机器学习模型在复杂化学/燃烧系统建模中的应用）的范畴。

**📖 中文摘要**

激光点火火箭发动机的精确且可预测的尺度解析模拟非常耗时，因为该问题包括湍流燃料-氧化剂混合动力学、激光诱导的能量沉积和高速火焰增长。这与主要由激光操作条件和目标位置构成的大设计空间相结合。为了实现快速探索和不确定性量化，我们提出了一种数据驱动的代理建模方法，该方法将卷积自编码器（cAE）与神经常微分方程（神经ODE）相结合。将基于机器学习的代理模型应用于前沿的多物理场湍流模拟是当前代理模型部署向增加现实世界复杂性范式转变的一部分。顺序上，cAE将高维流场空间压缩到低维潜在空间，其中系统的时间动力学通过神经ODE学习。一旦训练完成，该模型可以从初始条件和指定的操作输入快速生成时空预测。通过学习一个代理来替代整个时间演化的模拟，预测一次点火试验的成本降低了几个数量级，从而允许高效地探索输入参数空间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate and predictive scale-resolving simulations of laser-ignited rocket engines are highly time-consuming because the problem includes turbulent fuel-oxidizer mixing dynamics, laser-induced energy deposition, and high-speed flame growth. This is conflated with the large design space primarily corresponding to the laser operating conditions and target location. To enable rapid exploration and uncertainty quantification, we propose a data-driven surrogate modeling approach that combines convolutional autoencoders (cAEs) with neural ordinary differential equations (neural ODEs). The present target application of an ML-based surrogate model to leading-edge multi-physics turbulence simulation is part of a paradigm shift in the deployment of surrogate models towards increasing real-world complexity. Sequentially, the cAE spatially compresses high-dimensional flow fields into a low-dimensional latent space, wherein the system's temporal dynamics are learned via neural ODEs. Once trained, the model generates fast spatiotemporal predictions from initial conditions and specified operating inputs. By learning a surrogate to replace the entirety of the time-evolving simulation, the cost of predicting an ignition trial is reduced by several orders of magnitude, allowing efficient exploration of the input parameter space. Further, as the current framework yields a spatiotemporal field prediction, appraisal of the model output's physical grounding is more tractable. This approach marks a significant step toward real-time digital twins for laser-ignited rocket combustors and represents surrogate modeling in a complex system context.

</details>

---

### 34. [Brain-WM: Brain Glioblastoma World Model](https://arxiv.org/abs/2603.07562)

**基本信息**

- 🔗 arXiv: [`2603.07562`](https://arxiv.org/abs/2603.07562)
- 👥 作者: Chenhui Wang, Boyun Zheng, Liuxin Bao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07562.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个生成式世界模型（Brain-WM），用于模拟胶质母细胞瘤在治疗干预下的演变并生成未来的MRI图像。这直接属于'化学大模型'（生成模型在生物医学/药物发现相关领域的应用）的范畴。

**📖 中文摘要**

在变化治疗干预下精确预测胶质母细胞瘤（GBM）的预后对于优化临床结果至关重要。虽然生成式人工智能在模拟GBM演变方面显示出潜力，但现有方法通常将干预视为静态条件输入而非动态决策变量。因此，它们未能捕捉肿瘤演变和治疗反应之间复杂的、相互的相互作用。为了弥补这一差距，我们提出了Brain-WM，这是一个开创性的脑GBM世界模型，它统一了下一步治疗预测和未来MRI生成，从而捕捉肿瘤和治疗之间的协同进化动力学。具体来说，Brain-WM将时空动力学编码到一个共享的潜在空间中，用于联合自回归治疗预测和基于流的未来MRI生成。然后，Brain-WM没有采用传统的单一框架，而是采用了一种新颖的Y形混合Transformer（MoT）架构。这种设计在结构上解耦了异构目标，成功利用了跨任务协同作用，同时防止了特征崩溃。最后，一个协同的多时间点掩码对齐目标明确地将潜在表示锚定到基于解剖学的肿瘤结构和进展感知语义上。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Precise prognostic modeling of glioblastoma (GBM) under varying treatment interventions is essential for optimizing clinical outcomes. While generative AI has shown promise in simulating GBM evolution, existing methods typically treat interventions as static conditional inputs rather than dynamic decision variables. Consequently, they fail to capture the complex, reciprocal interplay between tumor evolution and treatment response. To bridge this gap, we present Brain-WM, a pioneering brain GBM world model that unifies next-step treatment prediction and future MRI generation, thereby capturing the co-evolutionary dynamics between tumor and treatment. Specifically, Brain-WM encodes spatiotemporal dynamics into a shared latent space for joint autoregressive treatment prediction and flow-based future MRI generation. Then, instead of a conventional monolithic framework, Brain-WM adopts a novel Y-shaped Mixture-of-Transformers (MoT) architecture. This design structurally disentangles heterogeneous objectives, successfully leveraging cross-task synergies while preventing feature collapse. Finally, a synergistic multi-timepoint mask alignment objective explicitly anchors latent representations to anatomically grounded tumor structures and progression-aware semantics. Extensive validation on internal and external multi-institutional cohorts demonstrates the superiority of Brain-WM, achieving 91.5% accuracy in treatment planning and SSIMs of 0.8524, 0.8581, and 0.8404 for FLAIR, T1CE, and T2W sequences, respectively. Ultimately, Brain-WM offers a robust clinical sandbox for optimizing patient healthcare. The source code is made available at this https URL .

</details>

---

### 35. [Analysis-Driven Procedural Generation of an Engine Sound Dataset with Embedded Control Annotations](https://arxiv.org/abs/2603.07584)

**基本信息**

- 🔗 arXiv: [`2603.07584`](https://arxiv.org/abs/2603.07584)
- 👥 作者: Robin Doerfler, Lonce Wyse
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07584.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出了一个生成高质量、带标注的发动机声音数据的框架，并发布了由此产生的大规模数据集（Procedural Engine Sounds Dataset）。这提供了可用于'化学大模型'（特别是音频/振动信号处理、分子振动光谱相关模型）和'质谱结构推理'（作为信号生成和标注的类比）研究的数据集和工具。

**📖 中文摘要**

计算发动机声音建模是汽车音频行业的核心，特别是对于主动声音设计、虚拟原型制作和新兴的数据驱动发动机声音合成方法。这些应用需要大量具有精确时间对齐的操作状态标注的标准化、干净音频录音：由于成本高、专用测量设备要求以及不可避免的噪声污染，此类数据难以获得。我们提出了一个分析驱动的框架，用于生成具有样本精确控制标注的发动机音频。该方法通过音高自适应频谱分析从真实录音中提取谐波结构，然后驱动一个扩展的参数化谐波加噪声合成器。利用这个框架，我们生成了程序化发动机声音数据集（19小时，5,935个文件），这是一组具有样本精确的RPM和扭矩标注的发动机音频信号，涵盖了广泛的操作条件、信号复杂性和谐波轮廓。与真实录音的比较验证了合成数据保留了特征性的谐波结构，基线实验证实了其适用于基于学习的参数估计和合成任务。该数据集公开发布，以支持发动机音色分析、控制参数估计、声学建模和神经生成网络的研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational engine sound modeling is central to the automotive audio industry, particularly for active sound design, virtual prototyping, and emerging data-driven engine sound synthesis methods. These applications require large volumes of standardized, clean audio recordings with precisely time-aligned operating-state annotations: data that is difficult to obtain due to high costs, specialized measurement equipment requirements, and inevitable noise contamination. We present an analysis-driven framework for generating engine audio with sample-accurate control annotations. The method extracts harmonic structures from real recordings through pitch-adaptive spectral analysis, which then drive an extended parametric harmonic-plus-noise synthesizer. With this framework, we generate the Procedural Engine Sounds Dataset (19 hours, 5,935 files), a set of engine audio signals with sample-accurate RPM and torque annotations, spanning a wide range of operating conditions, signal complexities, and harmonic profiles. Comparison against real recordings validates that the synthesized data preserves characteristic harmonic structures, and baseline experiments confirm its suitability for learning-based parameter estimation and synthesis tasks. The dataset is released publicly to support research on engine timbre analysis, control parameter estimation, acoustic modeling and neural generative networks.

</details>

---

### 36. [TT-Sparse: Learning Sparse Rule Models with Differentiable Truth Tables](https://arxiv.org/abs/2603.07606)

**基本信息**

- 🔗 arXiv: [`2603.07606`](https://arxiv.org/abs/2603.07606)
- 👥 作者: Hans Farrell Soegeng, Sarthak Ketanbhai Modi, Thomas Peyrin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07606.pdf)

**💡 相关性分析**

满足标准1：论文提出的可微真值表和稀疏规则学习框架，其核心思想（学习可解释的、结构化的模型）与构建可解释的“化学大模型”这一主题在方法论上直接相关。

**📖 中文摘要**

本文提出TT-Sparse，一种利用可微真值表作为节点来学习稀疏、有效连接的灵活神经构建模块。虽然论文的核心是开发可解释的机器学习模型，但其提出的方法（利用可微真值表学习稀疏规则）在概念上与构建可解释的“化学大模型”相关。该方法旨在从数据中提取紧凑、全局可解释的布尔公式（DNF/CNF），这种从复杂数据中学习结构化、可解释规则的思想，可以类比或应用于化学信息学领域，例如从质谱或分子数据中推导出可解释的预测或推理规则。因此，该论文提供了一种潜在的、可用于化学大模型构建的机器学习工具或方法论思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Interpretable machine learning is essential in high-stakes domains where decision-making requires accountability, transparency, and trust. While rule-based models offer global and exact interpretability, learning rule sets that simultaneously achieve high predictive performance and low, human-understandable complexity remains challenging. To address this, we introduce TT-Sparse, a flexible neural building block that leverages differentiable truth tables as nodes to learn sparse, effective connections. A key contribution of our approach is a new soft TopK operator with straight-through estimation for learning discrete, cardinality-constrained feature selection in an end-to-end differentiable manner. Crucially, the forward pass remains sparse, enabling efficient computation and exact symbolic rule extraction. As a result, each node (and the entire model) can be transformed exactly into compact, globally interpretable DNF/CNF Boolean formulas via Quine-McCluskey minimization. Extensive empirical results across 28 datasets spanning binary, multiclass, and regression tasks show that the learned sparse rules exhibit superior predictive performance with lower complexity compared to existing state-of-the-art methods.

</details>

---

### 37. [Partial Differential Equations in the Age of Machine Learning: A Critical Synthesis of Classical, Machine Learning, and Hybrid Methods](https://arxiv.org/abs/2603.07655)

**基本信息**

- 🔗 arXiv: [`2603.07655`](https://arxiv.org/abs/2603.07655)
- 👥 作者: Mohammad Nooraiepour, Jakub Wiktor Both, Teeratorn Kadeethum 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07655.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于PDE求解方法的批判性综述，其中包含了对机器学习方法（包括基础模型）与经典方法融合的深入讨论和评估。这些讨论对于如何设计和发展融合物理化学知识的“化学大模型”提供了重要的理论框架和前瞻性视角。

**📖 中文摘要**

本文是一篇关于偏微分方程（PDE）求解方法的批判性综述，系统比较了经典数值方法和机器学习方法。论文建立了一个统一的评估框架，围绕六个基本计算挑战组织内容。它评估了经典方法在结构保持、严格收敛理论和可扩展求解器设计方面的特性，并精确描述了它们在高维和几何复杂场景中的持久局限性。同时，论文按照物理知识融入的程度对机器学习方法进行了分类，并进行了同样的批判性评估。文章进一步评估了新兴前沿，包括基础模型、可微分编程、量子算法和百亿亿次协同设计。虽然主题是PDE，但文中对“机器学习方法”和“基础模型”的深入讨论和分类，特别是关于如何将物理知识（先验）与数据驱动方法结合的探讨，对于思考如何构建融合领域知识的“化学大模型”（例如，用于求解化学动力学PDE或从物理原理增强分子表示）具有重要的参考价值和前瞻性指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Partial differential equations (PDEs) govern physical phenomena across the full range of scientific scales, yet their computational solution remains one of the defining challenges of modern science. This critical review examines two mature but epistemologically distinct paradigms for PDE solution, classical numerical methods and machine learning approaches, through a unified evaluative framework organized around six fundamental computational challenges. Classical methods are assessed for their structure-preserving properties, rigorous convergence theory, and scalable solver design; their persistent limitations in high-dimensional and geometrically complex settings are characterized precisely. Machine learning approaches are introduced under a taxonomy organized by the degree to which physical knowledge is incorporated and subjected to the same critical evaluation applied to classical methods. Classical methods are deductive -- errors are bounded by quantities derivable from PDE structure and discretization parameters -- while machine learning methods are inductive -- accuracy depends on statistical proximity to the training distribution. This epistemological distinction is the primary criterion governing responsible method selection. We identify three genuine complementarities between the paradigms and develop principles for hybrid design, including a framework for the structure inheritance problem that addresses when classical guarantees propagate through hybrid couplings, and an error budget decomposition that separates discretization, neural approximation, and coupling contributions. We further assess emerging frontiers, including foundation models, differentiable programming, quantum algorithms, and exascale co-design, evaluating each against the structural constraints that determine whether current barriers are fundamental or contingent on engineering progress.

</details>

---

### 38. [Memory for Autonomous LLM Agents:Mechanisms, Evaluation, and Emerging Frontiers](https://arxiv.org/abs/2603.07670)

**基本信息**

- 🔗 arXiv: [`2603.07670`](https://arxiv.org/abs/2603.07670)
- 👥 作者: Pengfei Du
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07670.pdf)

**💡 相关性分析**

满足标准3：论文是关于LLM智能体记忆的综合性综述，其系统化的分析框架（记忆的写入、管理、读取机制，评估基准的演变等）为构建具有长期记忆和持续学习能力的“化学大模型”或化学领域智能体提供了重要的设计原则和评估参考。

**📖 中文摘要**

本文是关于大型语言模型（LLM）智能体中记忆机制的系统性综述，涵盖了从2022年到2026年初的工作。文章将智能体记忆形式化为一个与感知和动作紧密耦合的“写入-管理-读取”循环，并引入了一个跨越时间范围、表示基底和控制策略的三维分类法。文章深入研究了五种机制家族，并追踪了从静态回忆基准测试到交织记忆与决策的多会话智能体测试的评估侧重点转变。虽然综述主要围绕LLM智能体的通用记忆，但其对智能体架构、记忆表示、检索以及如何使模型具备持续学习能力的系统性梳理，对于构建能够处理复杂化学数据（如连续的实验数据流、文献知识）、进行多步推理（如逆合成分析）的“化学大模型”或“化学智能体”具有重要的借鉴意义。该综述提供了设计此类系统所需的关键组件和评估思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) agents increasingly operate in settings where a single context window is far too small to capture what has happened, what was learned, and what should not be repeated. Memory -- the ability to persist, organize, and selectively recall information across interactions -- is what turns a stateless text generator into a genuinely adaptive agent. This survey offers a structured account of how memory is designed, implemented, and evaluated in modern LLM-based agents, covering work from 2022 through early 2026. We formalize agent memory as a \emph{write--manage--read} loop tightly coupled with perception and action, then introduce a three-dimensional taxonomy spanning temporal scope, representational substrate, and control policy. Five mechanism families are examined in depth: context-resident compression, retrieval-augmented stores, reflective self-improvement, hierarchical virtual context, and policy-learned management. On the evaluation side, we trace the shift from static recall benchmarks to multi-session agentic tests that interleave memory with decision-making, analyzing four recent benchmarks that expose stubborn gaps in current systems. We also survey applications where memory is the differentiating factor -- personal assistants, coding agents, open-world games, scientific reasoning, and multi-agent teamwork -- and address the engineering realities of write-path filtering, contradiction handling, latency budgets, and privacy governance. The paper closes with open challenges: continual consolidation, causally grounded retrieval, trustworthy reflection, learned forgetting, and multimodal embodied memory.

</details>

---

### 39. [Scalable Training of Mixture-of-Experts Models with Megatron Core](https://arxiv.org/abs/2603.07685)

**基本信息**

- 🔗 arXiv: [`2603.07685`](https://arxiv.org/abs/2603.07685)
- 👥 作者: Zijie Yan, Hongxiao Bai, Xin Yao 等43人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07685.pdf)

**💡 相关性分析**

满足标准2：论文详细介绍了大规模混合专家模型（MoE）的训练框架和优化技术。MoE是构建超大规模模型（如“化学大模型”）的核心架构之一，该论文提供的开源框架、优化策略和性能数据，为训练此类模型提供了重要的工具、资源和实践经验。

**📖 中文摘要**

本文介绍了使用Megatron Core框架可扩展训练混合专家模型（MoE）的系统优化方案。MoE模型通过稀疏激活实现了参数规模的极大扩展，是构建超大规模模型（包括可能的大规模化学模型）的关键技术之一。论文详细阐述了在内存、通信和计算方面的集成优化，包括细粒度重计算、卸载、优化的调度器、重叠、分组GEMM、融合、CUDA图等。报告还提供了在NVIDIA GB300和GB200上训练DeepSeek-V3-685B和Qwen3-235B等大型MoE模型的实际性能数据。对于旨在构建超大规模“化学大模型”的研究而言，本文提供了关于如何高效训练此类模型的关键系统工程细节、实践经验和技术指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scaling Mixture-of-Experts (MoE) training introduces systems challenges absent in dense models. Because each token activates only a subset of experts, this sparsity allows total parameters to grow much faster than per-token computation, creating coupled constraints across memory, communication, and computation. Optimizing one dimension often shifts pressure to another, demanding co-design across the full system stack. We address these challenges for MoE training through integrated optimizations spanning memory (fine-grained recomputation, offloading, etc.), communication (optimized dispatchers, overlapping, etc.), and computation (Grouped GEMM, fusions, CUDA Graphs, etc.). The framework also provides Parallel Folding for flexible multi-dimensional parallelism, low-precision training support for FP8 and NVFP4, and efficient long-context training. On NVIDIA GB300 and GB200, it achieves 1,233/1,048 TFLOPS/GPU for DeepSeek-V3-685B and 974/919 TFLOPS/GPU for Qwen3-235B. As a performant, scalable, and production-ready open-source solution, it has been used across academia and industry for training MoE models ranging from billions to trillions of parameters on clusters scaling up to thousands of GPUs. This report explains how these techniques work, their trade-offs, and their interactions at the systems level, providing practical guidance for scaling MoE models with Megatron Core.

</details>

---

### 40. [Reverse Distillation: Consistently Scaling Protein Language Model Representations](https://arxiv.org/abs/2603.07710)

**基本信息**

- 🔗 arXiv: [`2603.07710`](https://arxiv.org/abs/2603.07710)
- 👥 作者: Darius Catrina, Christian Bepler, Samuel Sledzieski 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07710.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容直接围绕提升蛋白质语言模型（一类重要的化学大模型）的缩放性能，提出了“反向蒸馏”这一新方法（标准1）。同时，该方法具有通用性，可为其他化学模型家族提供解决缩放问题的工具性思路（标准2）。

**📖 中文摘要**

本文针对蛋白质语言模型（PLM）缩放性能不佳的问题，提出了“反向蒸馏”框架。该框架将大型PLM的表征分解为以同家族小型模型为指导的正交子空间，从而确保缩放后的模型性能一致优于小型模型。论文在ProteinGym基准上进行了验证，表明经过反向蒸馏的ESM-2变体在相同嵌入维度下优于基线，且150亿参数模型实现了最强性能。虽然论文聚焦于蛋白质序列，但蛋白质语言模型是“化学大模型”在生物分子领域的一个重要分支和典型代表。论文解决的模型缩放不一致问题，以及提出的“反向蒸馏”方法，对于所有旨在通过缩放提升性能的化学领域大模型（包括小分子、聚合物等）都具有直接的启发性和应用价值。该方法为构建更可靠、可扩展的化学大模型提供了一种新颖的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unlike the predictable scaling laws in natural language processing and computer vision, protein language models (PLMs) scale poorly: for many tasks, models within the same family plateau or even decrease in performance, with mid-sized models often outperforming the largest in the family. We introduce Reverse Distillation, a principled framework that decomposes large PLM representations into orthogonal subspaces guided by smaller models of the same family. The resulting embeddings have a nested, Matryoshka-style structure: the first k dimensions of a larger model's embedding are exactly the representation from the smaller model. This ensures that larger reverse-distilled models consistently outperform smaller ones. A motivating intuition is that smaller models, constrained by capacity, preferentially encode broadly-shared protein features. Reverse distillation isolates these shared features and orthogonally extracts additional contributions from larger models, preventing interference between the two. On ProteinGym benchmarks, reverse-distilled ESM-2 variants outperform their respective baselines at the same embedding dimensionality, with the reverse-distilled 15 billion parameter model achieving the strongest performance. Our framework is generalizable to any model family where scaling challenges persist. Code and trained models are available at this https URL .

</details>

---

### 41. [Large Language Model for Discrete Optimization Problems: Evaluation and Step-by-step Reasoning](https://arxiv.org/abs/2603.07733)

**基本信息**

- 🔗 arXiv: [`2603.07733`](https://arxiv.org/abs/2603.07733)
- 👥 作者: Tianhao Qian, Guilin Qi, Z.Y. Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07733.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是评估大语言模型解决离散优化问题的能力。化学中的许多核心问题（如合成路线设计、分子性质优化）都属于离散优化范畴，因此该研究直接关联到“化学大模型”在解决化学领域复杂推理和规划任务方面的核心能力评估与提升。

**📖 中文摘要**

本文研究了不同大语言模型（包括Llama-3系列和ChatGPT）在解决离散优化问题方面的能力。作者构建了包含多种离散优化问题类型和广泛参数范围的自然语言数据集进行测试。实验比较了强模型与弱模型、思维链（CoT）与非思维链方法在不同数据集上的表现。虽然论文的评估领域是通用的离散优化，但其核心——探索大语言模型解决复杂、结构化问题的能力（包括推理、规划、搜索）——与“化学大模型”需要具备的核心能力高度相关。例如，化学中的逆合成规划、分子优化、实验条件搜索等本质都是复杂的组合优化问题。该论文对LLM在此类任务上能力的系统性评估（包括CoT的有效性、数据集构建的影响等），为评估和提升化学大模型在解决化学优化问题方面的性能提供了重要的方法论参考和基准测试思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work investigated the capabilities of different models, including the Llama-3 series of models and CHATGPT, with different forms of expression in solving discrete optimization problems by testing natural language datasets. In contrast to formal datasets with a limited scope of parameters, our dataset included a variety of problem types in discrete optimization problems and featured a wide range of parameter magnitudes, including instances with large parameter sets, integrated with augmented data. It aimed to (1) provide an overview of LLMs' ability in large-scale problems, (2) offer suggestions to those who want to solve discrete optimization problems automatically, and (3) regard the performance as a benchmark for future research. These datasets included original, expanded and augmented datasets. Among these three datasets, the original and augmented ones aimed for evaluation while the expanded one may help finetune a new model. In the experiment, comparisons were made between strong and week models, CoT methods and No-CoT methods on various datasets. The result showed that stronger model performed better reasonably. Contrary to general agreement, it also showed that CoT technique was not always effective regarding the capability of models and disordered datasets improved performance of models on easy to-understand problems, even though they were sometimes with high variance, a manifestation of instability. Therefore, for those who seek to enhance the automatic resolution of discrete optimization problems, it is recommended to consult the results, including the line charts presented in the Appendix, as well as the conclusions drawn in this study for relevant suggestions.

</details>

---

### 42. [MedQ-Deg: A Multidimensional Benchmark for Evaluating MLLMs Across Medical Image Quality Degradations](https://arxiv.org/abs/2603.07769)

**基本信息**

- 🔗 arXiv: [`2603.07769`](https://arxiv.org/abs/2603.07769)
- 👥 作者: Jiyao Liu, Junzhi Ning, Chenglong Ma 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07769.pdf)

**💡 相关性分析**

满足标准2：论文提出的MedQ-Deg基准虽然针对医学，但其系统化的多维评估框架（涵盖多种退化类型、能力维度和校准指标）为评估“化学大模型”和“质谱结构推理”模型在噪声、低质量数据下的鲁棒性提供了重要的方法论参考和潜在的评估工具资源。

**📖 中文摘要**

本文提出了MedQ-Deg，一个用于评估多模态大语言模型在医学图像质量退化下性能的多维基准。该基准涵盖了18种退化类型、30种细粒度能力维度和7种成像模态，包含近2.5万个问答对。虽然该基准针对医学领域，但其构建思路——系统性地评估模型在数据质量受损（如图像退化）下的鲁棒性——对于“化学大模型”和“质谱结构推理”具有重要的借鉴意义。在化学信息学中，质谱数据常存在噪声、基线漂移、分辨率差异等问题；分子图像或结构数据也可能不完整或低质量。一个可靠的化学大模型需要对此类数据退化具有鲁棒性。MedQ-Deg提供的多维评估框架、退化严重度校准方法以及新提出的“校准偏移”指标，为设计和评估化学领域大模型的数据鲁棒性提供了一个优秀的范本和潜在的评估工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite impressive performance on standard benchmarks, multimodal large language models (MLLMs) face critical challenges in real-world clinical environments where medical images inevitably suffer various quality degradations. Existing benchmarks exhibit two key limitations: (1) absence of large-scale, multidimensional assessment across medical image quality gradients and (2) no systematic confidence calibration analysis. To address these gaps, we present MedQ-Deg, a comprehensive benchmark for evaluating medical MLLMs under image quality degradations. MedQ-Deg provides multi-dimensional evaluation spanning 18 distinct degradation types, 30 fine-grained capability dimensions, and 7 imaging modalities, with 24,894 question-answer pairs. Each degradation is implemented at 3 severity degrees, calibrated by expert radiologists. We further introduce Calibration Shift metric, which quantifies the gap between a model's perceived confidence and actual performance to assess metacognitive reliability under degradation. Our comprehensive evaluation of 40 mainstream MLLMs reveals several critical findings: (1) overall model performance degrades systematically as degradation severity increases, (2) models universally exhibit the AI Dunning-Kruger Effect, maintaining inappropriately high confidence despite severe accuracy collapse, and (3) models display markedly differentiated behavioral patterns across capability dimensions, imaging modalities, and degradation types. We hope MedQ-Deg drives progress toward medical MLLMs that are robust and trustworthy in real clinical practice.

</details>

---

### 43. [Fusion Complexity Inversion: Why Simpler Cross View Modules Outperform SSMs and Cross View Attention Transformers for Pasture Biomass Regression](https://arxiv.org/abs/2603.07819)

**基本信息**

- 🔗 arXiv: [`2603.07819`](https://arxiv.org/abs/2603.07819)
- 👥 作者: Mridankan Mandal
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07819.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕评估和比较不同视觉基础模型（包括DINOv3等大模型）在特定领域（农业）的回归任务上的表现，这与“化学大模型”主题中评估和利用大型预训练模型解决科学问题的研究方向直接相关。

**📖 中文摘要**

这篇论文系统评估了视觉基础模型在农业回归任务（具体为牧场生物量估计）上的适应性。研究在CSIRO牧场生物量基准数据集上，测试了从EfficientNet到DINOv3-ViT-L的四种骨干网络、五种跨视图融合机制以及元数据组合。论文的核心发现是“融合复杂性反转”原则：在稀缺的农业数据上，简单的两层门控深度卷积（R^2 = 0.903）在性能上超越了复杂的跨视图注意力Transformer（0.833）、双向SSM（0.819）和完整Mamba模型（0.793）。研究为稀疏农业基准提供了可操作的指导方针，即应优先考虑骨干网络质量而非融合复杂性，并倾向于使用局部模块而非全局替代方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate estimation of pasture biomass from agricultural imagery is critical for sustainable livestock management, yet existing methods are limited by the small, imbalanced, and sparsely annotated datasets typical of real world monitoring. In this study, adaptation of vision foundation models to agricultural regression is systematically evaluated on the CSIRO Pasture Biomass benchmark, a 357 image dual view dataset with laboratory validated, component wise ground truth for five biomass targets, through 17 configurations spanning four backbones (EfficientNet-B3 to DINOv3-ViT-L), five cross view fusion mechanisms, and a 4x2 metadata factorial. A counterintuitive principle, termed "fusion complexity inversion", is uncovered: on scarce agricultural data, a two layer gated depthwise convolution (R^2 = 0.903) outperforms cross view attention transformers (0.833), bidirectional SSMs (0.819), and full Mamba (0.793, below the no fusion baseline). Backbone pretraining scale is found to monotonically dominate all architectural choices, with the DINOv2 -> DINOv3 upgrade alone yielding +5.0 R^2 points. Training only metadata (species, state, and NDVI) is shown to create a universal ceiling at R^2 ~ 0.829, collapsing an 8.4 point fusion spread to 0.1 points. Actionable guidelines for sparse agricultural benchmarks are established: backbone quality should be prioritized over fusion complexity, local modules preferred over global alternatives, and features unavailable at inference excluded.

</details>

---

### 44. [MINT: Molecularly Informed Training with Spatial Transcriptomics Supervision for Pathology Foundation Models](https://arxiv.org/abs/2603.07895)

**基本信息**

- 🔗 arXiv: [`2603.07895`](https://arxiv.org/abs/2603.07895)
- 👥 作者: Minsoo Lee, Jonghyun Kim, Juseung Yun 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07895.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个利用空间转录组学数据（一种高通量分子表型数据）来增强视觉基础模型（病理学ViT）的框架。这直接涉及利用多模态分子数据来构建和优化“化学大模型”在生物医学领域的应用。

**📖 中文摘要**

本文提出了MINT（分子信息训练）框架，旨在将空间转录组学（ST）的监督信号整合到预训练的病理学视觉Transformer（ViT）中，以增强其表示能力。MINT在ViT输入中添加了一个可学习的ST令牌，用于编码转录组信息，与形态学CLS令牌分开。通过DINO自蒸馏和显式特征锚定到冻结的预训练编码器来防止灾难性遗忘。该框架在斑点级（Visium）和斑块级（Xenium）分辨率上进行基因表达回归，提供跨空间尺度的互补监督。在577个公开可用的HEST样本上训练后，MINT在基因表达预测（HEST-Bench）和通用病理学任务（EVA）上都取得了最佳性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pathology foundation models learn morphological representations through self-supervised pretraining on large-scale whole-slide images, yet they do not explicitly capture the underlying molecular state of the tissue. Spatial transcriptomics technologies bridge this gap by measuring gene expression in situ, offering a natural cross-modal supervisory signal. We propose MINT (Molecularly Informed Training), a fine-tuning framework that incorporates spatial transcriptomics supervision into pretrained pathology Vision Transformers. MINT appends a learnable ST token to the ViT input to encode transcriptomic information separately from the morphological CLS token, preventing catastrophic forgetting through DINO self-distillation and explicit feature anchoring to the frozen pretrained encoder. Gene expression regression at both spot-level (Visium) and patch-level (Xenium) resolutions provides complementary supervision across spatial scales. Trained on 577 publicly available HEST samples, MINT achieves the best overall performance on both HEST-Bench for gene expression prediction (mean Pearson r = 0.440) and EVA for general pathology tasks (0.803), demonstrating that spatial transcriptomics supervision complements morphology-centric self-supervised pretraining.

</details>

---

### 45. [EveryQuery: Zero-Shot Clinical Prediction via Task-Conditioned Pretraining over Electronic Health Records](https://arxiv.org/abs/2603.07900)

**基本信息**

- 🔗 arXiv: [`2603.07900`](https://arxiv.org/abs/2603.07900)
- 👥 作者: Payal Chandak, Gregory Kondas, Isaac Kohane 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07900.pdf)

**💡 相关性分析**

满足标准1：论文的核心是提出并验证一种新型的、基于任务条件预训练的EHR基础模型（EveryQuery）。这属于“化学大模型”主题在医疗健康信息学领域的直接应用，专注于开发能够进行零样本推理的专用领域大模型。

**📖 中文摘要**

本文介绍了EveryQuery，一种基于电子健康记录（EHR）的基础模型，通过任务条件预训练实现零样本临床预测。与现有基于自回归生成未来事件再进行统计的方法不同，EveryQuery将患者历史和指定临床任务的结构化查询作为输入，通过单次前向传播直接估计未来窗口内结果发生的可能性。该模型通过在随机采样的查询任务和患者上下文组合上进行预训练，使其能够对查询空间内的任意任务进行零样本预测，而无需微调、线性探测或轨迹生成。在MIMIC-IV数据集上的实验表明，EveryQuery在39个随机抽样的预测任务中，有82%的任务上优于自回归基线，平均AUC提升+0.16。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models pretrained on electronic health records (EHR) have demonstrated zero-shot clinical prediction capabilities by generating synthetic patient futures and aggregating statistics over sampled trajectories. However, this autoregressive inference procedure is computationally expensive, statistically noisy, and not natively promptable because users cannot directly condition predictions on specific clinical questions. In this preliminary work, we introduce EveryQuery, an EHR foundation model that achieves zero-shot inference through task-conditioned pre-training. Rather than generating future events, EveryQuery takes as input a patient's history and a structured query specifying a clinical task, and directly estimates the likelihood of the outcome occurring in the future window via a single forward pass. EveryQuery realizes this capability by pre-training over randomly sampled combinations of query tasks and patient contexts, directly training the model to produce correct answers to arbitrary input prompts. This enables zero-shot prediction for any task in the query space without finetuning, linear probing, or trajectory generation. On MIMIC-IV, EveryQuery outperforms an autoregressive baseline on 82% of 39 randomly sampled prediction tasks, with a mean AUC improvement of +0.16 (95% CI: [0.10,0.22]). This advantage remains consistent on tasks that were explicitly held out from the pre-training distribution. Further, EveryQuery's performance gains are most pronounced for rare clinical events, affirming and demonstrating a solution to the fundamental limitation of autoregressive inference for low-prevalence outcomes. However, at present, EveryQuery underperforms on tasks requiring disjunctive reasoning over multiple codes, such as 30-day readmission, exposing a concrete expressiveness limitation of the current query language.

</details>

---

### 46. [Unsupervised Domain Adaptation for Audio Deepfake Detection with Modular Statistical Transformations](https://arxiv.org/abs/2603.07935)

**基本信息**

- 🔗 arXiv: [`2603.07935`](https://arxiv.org/abs/2603.07935)
- 👥 作者: Urawee Thani, Gagandeep Singh, Priyanka Singh
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07935.pdf)

**💡 相关性分析**

满足标准2：论文提出并评估了一个用于音频深度伪造检测的模块化处理流水线，其中核心组件是预训练的Wav2Vec 2.0模型。该工作提供了将预训练音频模型（可视为一种基础模型）与特定领域后处理技术结合的工具和框架，属于为相关主题提供可用工具和方法的数据资源/工具类别。

**📖 中文摘要**

本文提出了一种用于音频深度伪造检测的无监督域自适应模块化流水线。该方法结合了预训练的Wav2Vec 2.0嵌入和一系列统计变换（包括功率变换、ANOVA特征选择、联合PCA和CORAL对齐），以提高模型在未标记目标数据上的跨域泛化能力，而无需重新训练检测模型。研究在两个跨域迁移场景（ASVspoof 2019 LA 到 Fake-or-Real 以及反向）上进行了评估。该流水线提供了透明性和模块化，适用于需要可解释决策的部署场景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio deepfake detection systems trained on one dataset often fail when deployed on data from different sources due to distributional shifts in recording conditions, synthesis methods, and acoustic environments. We present a modular pipeline for unsupervised domain adaptation that combines pre-trained Wav2Vec 2.0 embeddings with statistical transformations to improve cross-domain generalization without requiring labeled target data. Our approach applies power transformation for feature normalization, ANOVA-based feature selection, joint PCA for domain-agnostic dimensionality reduction, and CORAL alignment to match source and target covariance structures before classification via logistic regression. We evaluate on two cross-domain transfer scenarios: ASVspoof 2019 LA to Fake-or-Real (FoR) and FoR to ASVspoof, achieving 62.7--63.6\% accuracy with balanced performance across real and fake classes. Systematic ablation experiments reveal that feature selection (+3.5%) and CORAL alignment (+3.2%) provide the largest individual contributions, with the complete pipeline improving accuracy by 10.7% over baseline. While performance is modest compared to within-domain detection (94-96%), our pipeline offers transparency and modularity, making it suitable for deployment scenarios requiring interpretable decisions.

</details>

---

### 47. [VisualAD: Language-Free Zero-Shot Anomaly Detection via Vision Transformer](https://arxiv.org/abs/2603.07952)

**基本信息**

- 🔗 arXiv: [`2603.07952`](https://arxiv.org/abs/2603.07952)
- 👥 作者: Yanning Hou, Peiyuan Li, Zirui Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07952.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心研究围绕改进基于视觉基础模型（ViT, CLIP, DINOv2）的零样本检测任务，是“化学大模型”在视觉异常检测领域的应用实例。2) 提出的VisualAD框架本身是一个新的、无需文本分支的检测工具，为相关领域提供了另一种模型架构选择。

**📖 中文摘要**

本文提出了VisualAD，一个纯粹的视觉零样本异常检测（ZSAD）框架，基于视觉Transformer（ViT），完全移除了对文本编码器的依赖。该方法在冻结的骨干网络中引入了两个可学习的令牌，分别直接编码正常和异常概念。通过多层自注意力，这些令牌与图像块令牌交互，逐步获取高级别的正常/异常概念，同时引导图像块突出异常相关线索。此外，还加入了空间感知交叉注意力模块和轻量级自对齐函数来增强性能。VisualAD在涵盖工业和医疗领域的13个零样本异常检测基准上达到了最先进的性能，并且可以无缝适配CLIP图像编码器和DINOv2等预训练视觉骨干网络。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Zero-shot anomaly detection (ZSAD) requires detecting and localizing anomalies without access to target-class anomaly samples. Mainstream methods rely on vision-language models (VLMs) such as CLIP: they build hand-crafted or learned prompt sets for normal and abnormal semantics, then compute image-text similarities for open-set discrimination. While effective, this paradigm depends on a text encoder and cross-modal alignment, which can lead to training instability and parameter redundancy. This work revisits the necessity of the text branch in ZSAD and presents VisualAD, a purely visual framework built on Vision Transformers. We introduce two learnable tokens within a frozen backbone to directly encode normality and abnormality. Through multi-layer self-attention, these tokens interact with patch tokens, gradually acquiring high-level notions of normality and anomaly while guiding patches to highlight anomaly-related cues. Additionally, we incorporate a Spatial-Aware Cross-Attention (SCA) module and a lightweight Self-Alignment Function (SAF): SCA injects fine-grained spatial information into the tokens, and SAF recalibrates patch features before anomaly scoring. VisualAD achieves state-of-the-art performance on 13 zero-shot anomaly detection benchmarks spanning industrial and medical domains, and adapts seamlessly to pretrained vision backbones such as the CLIP image encoder and DINOv2. Code: this https URL

</details>

---

### 48. [Structure-Preserving Graph Contrastive Learning for Mathematical Information Retrieval](https://arxiv.org/abs/2603.08012)

**基本信息**

- 🔗 arXiv: [`2603.08012`](https://arxiv.org/abs/2603.08012)
- 👥 作者: Chun-Hsi Ku, Hung-Hsuan Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08012.pdf)

**💡 相关性分析**

满足标准2：论文提出的‘变量替换’图增强技术是一种专门针对结构化图（如数学公式、分子图）的数据处理方法，可直接作为工具或方法用于化学信息学领域，特别是为化学大模型处理分子结构数据提供了新的数据增强和表示学习资源。

**📖 中文摘要**

本文提出了一种用于数学公式检索的图对比学习方法。针对数学公式这类高度结构化的小型图，标准的图对比学习增强技术往往会扭曲其语义含义。为此，作者引入了“变量替换”这一领域特定的图增强技术，该技术能够保持核心代数关系和公式结构。该方法应用于经典的基于图对比学习的检索模型，实验表明，与通用增强策略相比，这种简单的方法显著提高了检索性能。这项工作为化学信息学领域（特别是化学大模型）提供了重要的数据资源和方法论工具，因为分子结构（如SMILES、分子图）与数学公式具有相似的结构化图表示，该方法可直接应用于分子表示学习和检索任务，为构建或增强化学大模型所需的数据处理流程提供了新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper introduces Variable Substitution as a domain-specific graph augmentation technique for graph contrastive learning (GCL) in the context of searching for mathematical formulas. Standard GCL augmentation techniques often distort the semantic meaning of mathematical formulas, particularly for small and highly structured graphs. Variable Substitution, on the other hand, preserves the core algebraic relationships and formula structure. To demonstrate the effectiveness of our technique, we apply it to a classic GCL-based retrieval model. Experiments show that this straightforward approach significantly improves retrieval performance compared to generic augmentation strategies. We release the code on GitHub.\footnote{ this https URL }.

</details>

---

### 49. [S2S-FDD: Bridging Industrial Time Series and Natural Language for Explainable Zero-shot Fault Diagnosis](https://arxiv.org/abs/2603.08048)

**基本信息**

- 🔗 arXiv: [`2603.08048`](https://arxiv.org/abs/2603.08048)
- 👥 作者: Baoxue Li, Chunhui Zhao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08048.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是将高维时序信号（可类比质谱数据）通过自然语言描述与大语言模型结合进行推理和诊断，这直接围绕“化学大模型”和“质谱结构推理”主题，为解决质谱数据的智能化解析提供了方法论框架和工具思路。

**📖 中文摘要**

本文提出S2S-FDD框架，用于工业系统的零样本可解释故障诊断。该框架的核心创新在于设计了一个“信号到语义”算子，将高维、时序的传感器信号（如振动、温度）转换为自然语言描述，从而弥合了原始数据与大型语言模型（LLM）理解能力之间的语义鸿沟。基于这些描述，框架通过一个多轮树状结构诊断方法，参考历史维护文档并动态查询额外信号来进行故障诊断。该工作虽然面向工业设备，但其核心思想——将复杂的、非结构化的科学仪器数据（如质谱、色谱）转化为结构化文本描述，再利用大语言模型进行推理——与“质谱结构推理”和“化学大模型”的研究主题高度相关。它为如何利用大模型处理和分析质谱等复杂科学数据提供了一个可行的技术框架和思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fault diagnosis is critical for the safe operation of industrial systems. Conventional diagnosis models typically produce abstract outputs such as anomaly scores or fault categories, failing to answer critical operational questions like "Why" or "How to repair". While large language models (LLMs) offer strong generalization and reasoning abilities, their training on discrete textual corpora creates a semantic gap when processing high-dimensional, temporal industrial signals. To address this challenge, we propose a Signals-to-Semantics fault diagnosis (S2S-FDD) framework that bridges high-dimensional sensor signals with natural language semantics through two key innovations: We first design a Signal-to-Semantic operator to convert abstract time-series signals into natural language summaries, capturing trends, periodicity, and deviations. Based on the descriptions, we design a multi-turn tree-structured diagnosis method to perform fault diagnosis by referencing historical maintenance documents and dynamically querying additional signals. The framework further supports human-in-the-loop feedback for continuous refinement. Experiments on the multiphase flow process show the feasibility and effectiveness of the proposed method for explainable zero-shot fault diagnosis.

</details>

---

### 50. [Adversarial Domain Adaptation Enables Knowledge Transfer Across Heterogeneous RNA-Seq Datasets](https://arxiv.org/abs/2603.08062)

**基本信息**

- 🔗 arXiv: [`2603.08062`](https://arxiv.org/abs/2603.08062)
- 👥 作者: Kevin Dradjat, Massinissa Hamidi, Blaise Hanczar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08062.pdf)

**💡 相关性分析**

满足标准2：论文提出的对抗性领域自适应框架是一种可用于处理高维、小样本科学数据（如质谱数据）的工具和方法，为化学信息学中构建鲁棒的、可迁移的化学大模型提供了重要的技术资源和实现思路。

**📖 中文摘要**

本研究提出了一种基于对抗性领域自适应的深度学习框架，用于在转录组学（RNA-seq）数据之间进行有效的知识迁移，以解决小样本癌症类型分类问题。该方法通过联合优化分类和领域对齐目标，学习一个领域不变的潜在空间，从而实现从大型通用数据集（如TCGA）到小型特定数据集的知识转移。论文评估了该框架在多个大规模转录组学数据集上的性能，证明了其在数据稀缺场景下提高分类准确性的有效性。这项工作与化学信息学高度相关，因为质谱数据与转录组数据同属高维、小样本的生物医学组学数据，面临相似的数据异构性和标注稀缺挑战。论文提出的领域自适应框架为构建和优化用于质谱数据分析的化学大模型提供了关键的技术路径和工具资源，特别是在利用已有大型质谱数据库（如GNPS）来增强特定小样本任务模型性能方面具有直接应用价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate phenotype prediction from RNA sequencing (RNA-seq) data is essential for diagnosis, biomarker discovery, and personalized medicine. Deep learning models have demonstrated strong potential to outperform classical machine learning approaches, but their performance relies on large, well-annotated datasets. In transcriptomics, such datasets are frequently limited, leading to over-fitting and poor generalization. Knowledge transfer from larger, more general datasets can alleviate this issue. However, transferring information across RNA-seq datasets remains challenging due to heterogeneous preprocessing pipelines and differences in target phenotypes. In this study, we propose a deep learning-based domain adaptation framework that enables effective knowledge transfer from a large general dataset to a smaller one for cancer type classification. The method learns a domain-invariant latent space by jointly optimizing classification and domain alignment objectives. To ensure stable training and robustness in data-scarce scenarios, the framework is trained with an adversarial approach with appropriate regularization. Both supervised and unsupervised approach variants are explored, leveraging labeled or unlabeled target samples. The framework is evaluated on three large-scale transcriptomic datasets (TCGA, ARCHS4, GTEx) to assess its ability to transfer knowledge across cohorts. Experimental results demonstrate consistent improvements in cancer and tissue type classification accuracy compared to non-adaptive baselines, particularly in low-data scenarios. Overall, this work highlights domain adaptation as a powerful strategy for data-efficient knowledge transfer in transcriptomics, enabling robust phenotype prediction under constrained data conditions.

</details>

---

### 51. [Synthetic Defect Image Generation for Power Line Insulator Inspection Using Multimodal Large Language Models](https://arxiv.org/abs/2603.08069)

**基本信息**

- 🔗 arXiv: [`2603.08069`](https://arxiv.org/abs/2603.08069)
- 👥 作者: Xuesong Wang, Caisheng Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08069.pdf)

**💡 相关性分析**

满足标准2：论文提出的利用多模态大语言模型进行领域特定数据合成和增强的管道，是一种通用的数据资源生成工具，可直接应用于化学信息学领域，为化学大模型的训练或质谱结构推理任务生成所需的合成数据或增强现有数据集。

**📖 中文摘要**

本文针对电力线绝缘子缺陷分类中真实缺陷样本稀缺的问题，提出利用现成的多模态大语言模型（MLLM）作为免训练的图像生成器，从视觉参考和文本提示合成缺陷图像，以进行数据增强。其流程包括双参考条件生成、轻量级人工验证和提示词优化，并采用基于嵌入距离的合成数据选择策略。在低训练数据场景下，使用合成数据增强能显著提升分类器的F1分数。这项工作虽然应用在计算机视觉领域，但其核心方法论——利用大模型（特别是多模态大模型）根据文本和视觉线索生成或增强特定领域的科学数据——与化学信息学高度相关。例如，该方法可以迁移用于根据分子结构图和文本描述生成特定的质谱图或分子性质数据，为“化学大模型”和“质谱结构推理”研究提供宝贵的数据生成与增强工具和资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Utility companies increasingly rely on drone imagery for post-event and routine inspection, but training accurate defect-type classifiers remains difficult because defect examples are rare and inspection datasets are often limited or proprietary. We address this data-scarcity setting by using an off-the-shelf multimodal large language model (MLLM) as a training-free image generator to synthesize defect images from visual references and text prompts. Our pipeline increases diversity via dual-reference conditioning, improves label fidelity with lightweight human verification and prompt refinement, and filters the resulting synthetic pool using an embedding-based selection rule based on distances to class centroids computed from the real training split. We evaluate on ceramic insulator defect-type classification (shell vs. glaze) using a public dataset with a realistic low training-data regime (104 real training images; 152 validation; 308 test). Augmenting the 10% real training set with embedding-selected synthetic images improves test F1 score (harmonic mean of precision and recall) from 0.615 to 0.739 (20% relative), corresponding to an estimated 4--5x data-efficiency gain, and the gains persist with stronger backbone models and frozen-feature linear-probe baselines. These results suggest a practical, low-barrier path for improving defect recognition when collecting additional real defects is slow or infeasible.

</details>

---

### 52. [Hybrid Quantum Neural Network for Multivariate Clinical Time Series Forecasting](https://arxiv.org/abs/2603.08072)

**基本信息**

- 🔗 arXiv: [`2603.08072`](https://arxiv.org/abs/2603.08072)
- 👥 作者: Irene Iele, Floriano Caprio, Paolo Soda 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08072.pdf)

**💡 相关性分析**

满足标准2：论文探索的混合量子-经典神经网络架构是一种新颖的计算工具，可用于分析复杂的科学时序数据（如质谱流数据或分子模拟轨迹），为化学大模型的新型架构设计和质谱数据的深度分析提供了潜在的技术资源和研究方向。

**📖 中文摘要**

本文提出了一种混合量子-经典神经网络架构，用于多变量临床时间序列预测。该架构在循环神经网络（GRU）主干中集成了一个变分量子电路，作为可学习的非线性特征混合器，用于建模跨变量交互。量子层由历史观测的潜在表示参数化。论文在生理信号预测任务上评估了该方法的性能。这项工作的相关性在于其探索了新型计算架构（量子机器学习）在复杂时序数据分析中的应用。虽然应用场景是临床数据，但其处理高维、相关时序信号的核心技术（混合量子-经典模型、特征交互建模）与处理质谱时序数据或分子动力学模拟数据有相通之处。它为化学信息学和质谱分析领域探索利用前沿计算模型（作为化学大模型的一种可能架构或组件）进行数据分析和推理提供了前瞻性的视角和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Forecasting physiological signals can support proactive monitoring and timely clinical intervention by anticipating critical changes in patient status. In this work, we address multivariate multi-horizon forecasting of physiological time series by jointly predicting heart rate, oxygen saturation, pulse rate, and respiratory rate at forecasting horizons of 15, 30, and 60 seconds. We propose a hybrid quantum-classical architecture that integrates a Variational Quantum Circuit (VQC) within a recurrent neural backbone. A GRU encoder summarizes the historical observation window into a latent representation, which is then projected into quantum angles used to parameterize the VQC. The quantum layer acts as a learnable non-linear feature mixer, modeling cross-variable interactions before the final prediction stage. We evaluate the proposed approach on the BIDMC PPG and Respiration dataset under a Leave-One-Patient-Out protocol. The results show competitive accuracy compared with classical and deep learning baselines, together with greater robustness to noise and missing inputs. These findings suggest that hybrid quantum layers can provide useful inductive biases for physiological time series forecasting in small-cohort clinical settings.

</details>

---

### 53. [DC-W2S: Dual-Consensus Weak-to-Strong Training for Reliable Process Reward Modeling in Biological Reasoning](https://arxiv.org/abs/2603.08095)

**基本信息**

- 🔗 arXiv: [`2603.08095`](https://arxiv.org/abs/2603.08095)
- 👥 作者: Chi-Min Chan, Ehsan Hajiramezanali, Xiner Li 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08095.pdf)

**💡 相关性分析**

满足标准2：论文提出的DC-W2S框架是一种利用弱监督数据训练可靠过程奖励模型的方法论工具，可直接应用于化学信息学领域，用于训练化学大模型执行需要多步推理的任务（如质谱结构解析、反应预测），提供了数据高效利用的解决方案。

**📖 中文摘要**

本文针对科学推理任务中过程奖励模型训练依赖昂贵专家标注的问题，提出了DC-W2S框架。该框架利用大量但嘈杂的“弱”监督信号来训练可靠的过程奖励模型。其核心是通过交集自我共识和邻域共识指标，将监督信号分层为不同的可靠性区域，并采用课程学习策略指导训练。该方法证明了通过策略性的数据管理，可以在没有大量专家标注的情况下训练出稳健的过程奖励模型。这项工作与“化学大模型”的研究紧密相关，特别是在如何利用不完美或弱标注的科学数据（如化学反应路径、谱图解析步骤）来训练或优化用于化学推理的大模型方面。它为化学领域构建能够进行复杂、可解释推理（如逆合成分析、质谱解析）的大模型提供了重要的训练方法论和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In scientific reasoning tasks, the veracity of the reasoning process is as critical as the final outcome. While Process Reward Models (PRMs) offer a solution to the coarse-grained supervision problems inherent in Outcome Reward Models (ORMs), their deployment is hindered by the prohibitive cost of obtaining expert-verified step-wise labels. This paper addresses the challenge of training reliable PRMs using abundant but noisy "weak" supervision. We argue that existing Weak-to-Strong Generalization (W2SG) theories lack prescriptive guidelines for selecting high-quality training signals from noisy data. To bridge this gap, we introduce the Dual-Consensus Weak-to-Strong (DC-W2S) framework. By intersecting Self-Consensus (SC) metrics among weak supervisors with Neighborhood-Consensus (NC) metrics in the embedding space, we stratify supervision signals into distinct reliability regimes. We then employ a curriculum of instance-level balanced sampling and label-level reliability-aware masking to guide the training process. We demonstrate that DC-W2S enables the training of robust PRMs for complex reasoning without exhaustive expert annotation, proving that strategic data curation is more effective than indiscriminate training on large-scale noisy datasets.

</details>

---

### 54. [Tau-BNO: Brain Neural Operator for Tau Transport Model](https://arxiv.org/abs/2603.08108)

**基本信息**

- 🔗 arXiv: [`2603.08108`](https://arxiv.org/abs/2603.08108)
- 👥 作者: Nuutti Barron, Heng Rao, Urmi Saha 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08108.pdf)

**💡 相关性分析**

满足标准2：论文提出的神经算子代理框架是一种用于加速复杂科学计算模型（可类比化学动力学模型、分子模拟）的强大工具，为化学信息学中构建高效、可微的物理信息化学大模型或质谱模拟器提供了关键的技术资源和实现路径。

**📖 中文摘要**

本文提出Tau-BNO，一个用于快速近似复杂生物物理模型（网络传输模型，NTM）动力学的脑神经算子代理框架。NTM用于模拟tau蛋白在脑连接组上的传播，是一个由偏微分方程定义的大规模复杂系统，直接模拟计算成本高昂。Tau-BNO结合了编码动力学参数的函数算子和保留初始状态信息的查询算子，并通过保留方向性的谱核来近似各向异性传输。该代理模型将模拟时间从数小时减少到数秒，实现了大规模计算密集型动力学系统的高效分析。这项工作与化学信息学高度相关，因为许多化学过程（如分子扩散、反应动力学、质谱离子碎裂模拟）同样由复杂的微分方程描述，计算成本高。论文提出的神经算子代理框架为化学领域构建快速、可微分的物理信息模型提供了强大的工具资源，这些模型可以作为“化学大模型”的组成部分，用于加速分子模拟、谱图预测等任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic modeling provides a biophysically grounded framework for studying the spread of pathological tau protein in tauopathies like Alzheimer's disease. Existing approaches typically model tau propagation as a diffusive process on the brain's structural connectome, reproducing macroscopic patterns but neglecting microscale cellular transport and reaction mechanisms. The Network Transport Model (NTM) was introduced to fill this gap, explaining how region-level progression of tau emerges from microscale biophysical processes. However, the NTM faces a common challenge for complex models defined by large systems of partial differential equations: the inability to perform parameter inference and mechanistic discovery due to high computational burden and slow model simulations. To overcome this barrier, we propose Tau-BNO, a Brain Neural Operator surrogate framework for rapidly approximating NTM dynamics that captures both intra-regional reaction kinetics and inter-regional network transport. Tau-BNO combines a function operator that encodes kinetic parameters with a query operator that preserves initial state information, while approximating anisotropic transport through a spectral kernel that retains directionality. Empirical evaluations demonstrate high predictive accuracy ($R^2\approx$ 0.98) across diverse biophysical regimes and an 89\% performance improvement over state-of-the-art sequence models like Transformers and Mamba, which lack inherent structural priors. By reducing simulation time from hours to seconds, we show that the surrogate model is capable of producing new insights and generating new hypotheses. This framework is readily extensible to a broader class of connectome-based biophysical models, showcasing the transformative value of deep learning surrogates to accelerate analysis of large-scale, computationally intensive dynamical systems.

</details>

---

### 55. [EvoScientist: Towards Multi-Agent Evolving AI Scientists for End-to-End Scientific Discovery](https://arxiv.org/abs/2603.08127)

**基本信息**

- 🔗 arXiv: [`2603.08127`](https://arxiv.org/abs/2603.08127)
- 👥 作者: Yougang Lyu, Xi Zhang, Xinhao Yi 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08127.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是构建一个用于端到端科学发现的多智能体大模型系统，这直接围绕“化学大模型”的应用主题。同时，它提供了一整套系统架构、记忆模块和训练策略，可作为构建化学领域专用AI科学家（如用于质谱结构推理）的宝贵工具资源和设计参考。

**📖 中文摘要**

本文介绍了EvoScientist，一个通过持久记忆和自我进化持续改进研究策略的演化多智能体AI科学家框架。它包含研究智能体、工程智能体和进化管理智能体，并拥有构思记忆和实验记忆两个持久记忆模块，用于存储和复用成功的研究方向和代码策略。实验表明，EvoScientist在科学想法生成和代码执行成功率方面优于现有系统。这项工作是“化学大模型”和“AI for Science”的尖端体现。它直接构建了一个用于端到端科学发现的多智能体大模型系统，其架构、记忆机制和进化策略为设计和实现专门用于化学发现（如新材料设计、反应优化）或质谱数据自动解析（如未知物结构鉴定）的AI科学家系统提供了完整的蓝图、方法论和工具资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The increasing adoption of Large Language Models (LLMs) has enabled AI scientists to perform complex end-to-end scientific discovery tasks requiring coordination of specialized roles, including idea generation and experimental execution. However, most state-of-the-art AI scientist systems rely on static, hand-designed pipelines and fail to adapt based on accumulated interaction histories. As a result, these systems overlook promising research directions, repeat failed experiments, and pursue infeasible ideas. To address this, we introduce EvoScientist, an evolving multi-agent AI scientist framework that continuously improves research strategies through persistent memory and self-evolution. EvoScientist comprises three specialized agents: a Researcher Agent (RA) for scientific idea generation, an Engineer Agent (EA) for experiment implementation and execution, and an Evolution Manager Agent (EMA) that distills insights from prior interactions into reusable knowledge. EvoScientist contains two persistent memory modules: (i) an ideation memory, which summarizes feasible research directions from top-ranked ideas while recording previously unsuccessful directions; and (ii) an experimentation memory, which captures effective data processing and model training strategies derived from code search trajectories and best-performing implementations. These modules enable the RA and EA to retrieve relevant prior strategies, improving idea quality and code execution success rates over time. Experiments show that EvoScientist outperforms 7 open-source and commercial state-of-the-art systems in scientific idea generation, achieving higher novelty, feasibility, relevance, and clarity via automatic and human evaluation. EvoScientist also substantially improves code execution success rates through multi-agent evolution, demonstrating persistent memory's effectiveness for end-to-end scientific discovery.

</details>

---

### 56. [Mitigating Homophily Disparity in Graph Anomaly Detection: A Scalable and Adaptive Approach](https://arxiv.org/abs/2603.08137)

**基本信息**

- 🔗 arXiv: [`2603.08137`](https://arxiv.org/abs/2603.08137)
- 👥 作者: Yunhui Liu, Qizhuo Xie, Yinfeng Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08137.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕图神经网络（GNN）方法展开，该方法在化学信息学中被广泛用于分子表示学习和性质预测，是构建化学大模型（如分子图神经网络）和进行结构推理（如从质谱数据推断分子结构）的关键技术基础。

**📖 中文摘要**

本文提出了一种名为SAGAD的可扩展自适应图异常检测框架，旨在解决图异常检测中的同质性差异和可扩展性挑战。该框架通过预计算多跳嵌入和应用重参数化的切比雪夫滤波器来提取低频和高频信息，从而高效地捕捉同质性和异质性模式。为了缓解节点级同质性差异，引入了异常上下文感知自适应融合模块，该模块根据每个节点的异常子图结构自适应地融合低通和高通嵌入。为了缓解类级差异，设计了频率偏好引导损失，鼓励异常节点比正常节点保留更多高频信息。SAGAD支持小批量训练，实现了线性的时间和空间复杂度，并大幅减少了大规模图上的内存使用。该论文提出的图神经网络方法（特别是用于处理图结构数据和学习节点表示的技术）与化学信息学中分子图表示学习和结构推理的核心任务高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph anomaly detection (GAD) aims to identify nodes that deviate from normal patterns in structure or features. While recent GNN-based approaches have advanced this task, they struggle with two major challenges: 1) homophily disparity, where nodes exhibit varying homophily at both class and node levels; and 2) limited scalability, as many methods rely on costly whole-graph operations. To address them, we propose SAGAD, a Scalable and Adaptive framework for GAD. SAGAD precomputes multi-hop embeddings and applies reparameterized Chebyshev filters to extract low- and high-frequency information, enabling efficient training and capturing both homophilic and heterophilic patterns. To mitigate node-level homophily disparity, we introduce an Anomaly Context-Aware Adaptive Fusion, which adaptively fuses low- and high-pass embeddings using fusion coefficients conditioned on Rayleigh Quotient-guided anomalous subgraph structures for each node. To alleviate class-level disparity, we design a Frequency Preference Guidance Loss, which encourages anomalies to preserve more high-frequency information than normal nodes. SAGAD supports mini-batch training, achieves linear time and space complexity, and drastically reduces memory usage on large-scale graphs. Theoretically, SAGAD ensures asymptotic linear separability between normal and abnormal nodes under mild conditions. Extensive experiments on 10 benchmarks confirm SAGAD's superior accuracy and scalability over state-of-the-art methods.

</details>

---

### 57. [Training event-based neural networks with exact gradients via Differentiable ODE Solving in JAX](https://arxiv.org/abs/2603.08146)

**基本信息**

- 🔗 arXiv: [`2603.08146`](https://arxiv.org/abs/2603.08146)
- 👥 作者: Lukas König, Manuel Kuhn, David Kappel 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08146.pdf)

**💡 相关性分析**

满足标准1：论文提出的Eventax框架专注于为复杂动态系统（由ODE定义）构建和训练可扩展的神经网络模型。这种构建和训练“大模型”（尽管是神经形态计算领域）的方法论、框架设计思想（灵活性、可扩展性、精确梯度计算）可直接类比并应用于化学信息学领域，用于开发模拟化学过程或进行质谱信号生成的“化学大模型”。

**📖 中文摘要**

本文介绍了Eventax框架，这是一个基于JAX构建的、用于训练事件驱动神经网络的框架。它通过结合可微数值ODE求解器和基于事件的尖峰处理，为任何由ODE定义的神经元模型计算相对于前向模拟的精确梯度。该框架提供了一个简单的API，用户只需指定神经元动力学、尖峰条件和重置规则。Eventax优先考虑建模灵活性，支持广泛的神经元模型、损失函数和网络架构，并且易于扩展。论文在多个基准测试（包括Yin-Yang和MNIST）上进行了演示，使用了多种神经元模型，如LIF、QIF、EIF、Izhikevich和事件门控循环单元（EGRU），展示了其在用精确梯度训练事件驱动架构方面的实用性。虽然论文主要关注神经科学计算模型，但其核心贡献——一个灵活、可扩展的、用于训练复杂动态系统（由ODE定义）的框架——与化学信息学中构建和训练用于模拟化学反应动力学、分子动力学或质谱生成过程的“化学大模型”在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing frameworks for gradient-based training of spiking neural networks face a trade-off: discrete-time methods using surrogate gradients support arbitrary neuron models but introduce gradient bias and constrain spike-time resolution, while continuous-time methods that compute exact gradients require analytical expressions for spike times and state evolution, restricting them to simple neuron types such as Leaky Integrate and Fire (LIF). We introduce the Eventax framework, which resolves this trade-off by combining differentiable numerical ODE solvers with event-based spike handling. Built in JAX, our frame-work uses Diffrax ODE-solvers to compute gradients that are exact with respect to the forward simulation for any neuron model defined by ODEs . It also provides a simple API where users can specify just the neuron dynamics, spike conditions, and reset rules. Eventax prioritises modelling flexibility, supporting a wide range of neuron models, loss functions, and network architectures, which can be easily extended. We demonstrate Eventax on multiple benchmarks, including Yin-Yang and MNIST, using diverse neuron models such as Leaky Integrate-and-fire (LIF), Quadratic Integrate-and-fire (QIF), Exponential integrate-and-fire (EIF), Izhikevich and Event-based Gated Recurrent Unit (EGRU) with both time-to-first-spike and state-based loss functions, demonstrating its utility for prototyping and testing event-based architectures trained with exact gradients. We also demonstrate the application of this framework for more complex neuron types by implementing a multi-compartment neuron that uses a model of dendritic spikes in human layer 2/3 cortical Pyramidal neurons for computation. Code available at this https URL .

</details>

---

### 58. [Learning Hierarchical Knowledge in Text-Rich Networks with Taxonomy-Informed Representation Learning](https://arxiv.org/abs/2603.08159)

**基本信息**

- 🔗 arXiv: [`2603.08159`](https://arxiv.org/abs/2603.08159)
- 👥 作者: Yunhui Liu, Yongchao Liu, Yinfeng Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08159.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及利用大语言模型（LLM）进行知识提炼和结构化，并将其与图表示学习结合，用于学习文本丰富网络的层次化表示。这种方法论与化学信息学中利用LLMs处理化学文献、构建化学知识图谱，以及将文本信息与分子图结构相结合以增强“化学大模型”的表示和推理能力高度相关。

**📖 中文摘要**

本文提出了TIER（层次化分类法信息文本丰富网络表示学习）方法，用于在文本丰富网络中学习层次化知识结构。TIER首先通过相似性引导的对比学习构建一个利于聚类的嵌入空间，然后在其上执行层次化K-Means聚类，并利用大语言模型进行聚类精化，从而构建一个隐式的层次化分类法。利用生成的分类法，TIER引入了一种基于同调相关系数的正则化损失，使学习到的嵌入与层次结构对齐。通过学习同时尊重细粒度和粗粒度语义的表示，TIER能够对现实世界的文本丰富网络进行更可解释和结构化的建模。该方法在多个不同领域的数据集上显著优于现有方法。论文的核心是结合大语言模型（LLM）和图表示学习来构建和利用层次化知识结构，这直接涉及“化学大模型”（此处LLM作为知识提炼和结构构建工具）在图结构化化学数据（如分子-文本关联网络）上的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hierarchical knowledge structures are ubiquitous across real-world domains and play a vital role in organizing information from coarse to fine semantic levels. While such structures have been widely used in taxonomy systems, biomedical ontologies, and retrieval-augmented generation, their potential remains underexplored in the context of Text-Rich Networks (TRNs), where each node contains rich textual content and edges encode semantic relationships. Existing methods for learning on TRNs often focus on flat semantic modeling, overlooking the inherent hierarchical semantics embedded in textual documents. To this end, we propose TIER (Hierarchical \textbf{T}axonomy-\textbf{I}nformed R\textbf{E}presentation Learning on Text-\textbf{R}ich Networks), which first constructs an implicit hierarchical taxonomy and then integrates it into the learned node representations. Specifically, TIER employs similarity-guided contrastive learning to build a clustering-friendly embedding space, upon which it performs hierarchical K-Means followed by LLM-powered clustering refinement to enable semantically coherent taxonomy construction. Leveraging the resulting taxonomy, TIER introduces a cophenetic correlation coefficient-based regularization loss to align the learned embeddings with the hierarchical structure. By learning representations that respect both fine-grained and coarse-grained semantics, TIER enables more interpretable and structured modeling of real-world TRNs. We demonstrate that our approach significantly outperforms existing methods on multiple datasets across diverse domains, highlighting the importance of hierarchical knowledge learning for TRNs.

</details>

---

### 59. [Covenant-72B: Pre-Training a 72B LLM with Trustless Peers Over-the-Internet](https://arxiv.org/abs/2603.08163)

**基本信息**

- 🔗 arXiv: [`2603.08163`](https://arxiv.org/abs/2603.08163)
- 👥 作者: Joel Lidin, Amir Sarfi, Erfan Miahi 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08163.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大规模语言模型（LLM）的预训练，即“大模型”的构建。虽然论文未明确针对化学领域，但其关于大模型训练方法、分布式架构和协作机制的研究，为构建领域特定的“化学大模型”（如用于化学文献理解、分子设计或反应预测的大模型）提供了重要的技术参考和可行性证明。

**📖 中文摘要**

本报告描述了Covenant-72B，这是一个通过迄今为止最大规模的协作式、全局分布式预训练运行产生的大语言模型。该运行允许开放、无需许可的参与，并由实时区块链协议支持。研究团队采用了最先进的通信高效优化器SparseLoCo，支持动态参与。该模型在约1.1T tokens上进行了预训练，其性能与在相似或更高计算预算下完全集中预训练的模型具有竞争力。这项工作展示了完全民主化、非白名单参与的可行性，并在全局分布式预训练运行中达到了前所未有的规模。论文的核心是构建和训练一个大规模、分布式协作训练的大语言模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recently, there has been increased interest in globally distributed training, which has the promise to both reduce training costs and democratize participation in building large-scale foundation models. However, existing models trained in a globally distributed manner are relatively small in scale and have only been trained with whitelisted participants. Therefore, they do not yet realize the full promise of democratized participation. In this report, we describe Covenant-72B, an LLM produced by the largest collaborative globally distributed pre-training run (in terms of both compute and model scale), which simultaneously allowed open, permissionless participation supported by a live blockchain protocol. We utilized a state-of-the-art communication-efficient optimizer, SparseLoCo, supporting dynamic participation with peers joining and leaving freely. Our model, pre-trained on approximately 1.1T tokens, performs competitively with fully centralized models pre-trained on similar or higher compute budgets, demonstrating that fully democratized, non-whitelisted participation is not only feasible, but can be achieved at unprecedented scale for a globally distributed pre-training run.

</details>

---

### 60. [RexDrug: Reliable Multi-Drug Combination Extraction through Reasoning-Enhanced LLMs](https://arxiv.org/abs/2603.08166)

**基本信息**

- 🔗 arXiv: [`2603.08166`](https://arxiv.org/abs/2603.08166)
- 👥 作者: Zhijun Wang, Ling Luo, Dinghao Pan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08166.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用大语言模型（LLM）进行生物医学文本中的复杂关系提取和推理，特别是针对药物组合。这属于“化学大模型”在药物发现和药理研究领域的直接应用，涉及从非结构化文本中推理化学实体（药物）之间的关系，是化学信息学和生物信息学的交叉研究。

**📖 中文摘要**

本文提出了RexDrug，一个基于大语言模型的、用于从生物医学文献中自动提取n元药物组合的端到端推理增强关系提取框架。RexDrug采用两阶段训练策略。首先，利用多智能体协作机制自动生成高质量的专家式推理轨迹，用于监督微调。其次，应用强化学习与专门为药物组合提取设计的多维奖励函数，以进一步优化推理质量和提取准确性。在DrugComb数据集上的大量实验表明，RexDrug在n元提取任务上始终优于最先进的基线方法。在DDI13语料库上的额外评估证实了其对二元药物-药物相互作用任务的泛化能力。人类专家评估和自动推理指标进一步表明，RexDrug在准确识别复杂治疗方案的同时，能产生连贯的医学推理。该论文直接应用大语言模型解决生物医学文本中的复杂关系提取问题，特别是药物组合的推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated Drug Combination Extraction (DCE) from large-scale biomedical literature is crucial for advancing precision medicine and pharmacological research. However, existing relation extraction methods primarily focus on binary interactions and struggle to model variable-length n-ary drug combinations, where complex compatibility logic and distributed evidence need to be considered. To address these limitations, we propose RexDrug, an end-to-end reasoning-enhanced relation extraction framework for n-ary drug combination extraction based on large language models. RexDrug adopts a two-stage training strategy. First, a multi-agent collaborative mechanism is utilized to automatically generate high-quality expert-like reasoning traces for supervised fine-tuning. Second, reinforcement learning with a multi-dimensional reward function specifically tailored for DCE is applied to further refine reasoning quality and extraction accuracy. Extensive experiments on the DrugComb dataset show that RexDrug consistently outperforms state-of-the-art baselines for n-ary extraction. Additional evaluation on the DDI13 corpus confirms its generalizability to binary drugdrug interaction tasks. Human expert assessment and automatic reasoning metrics further indicates that RexDrug produces coherent medical reasoning while accurately identifying complex therapeutic regimens. These results establish RexDrug as a scalable and reliable solution for complex biomedical relation extraction from unstructured text. The source code and data are available at this https URL

</details>

---

### 61. [MERLIN: Building Low-SNR Robust Multimodal LLMs for Electromagnetic Signals](https://arxiv.org/abs/2603.08174)

**基本信息**

- 🔗 arXiv: [`2603.08174`](https://arxiv.org/abs/2603.08174)
- 👥 作者: Junyu Shen, Zhendong She, Chenghanyu Zhang 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08174.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门用于多模态大语言模型（此处为电磁信号-文本模型）预训练的大规模数据集EM-100k和综合性评估基准EM-Bench。虽然领域是电磁信号，但其构建“信号-文本”配对数据集和基准的方法论，为化学信息学中构建类似的“质谱-结构”或“光谱-分子描述”配对数据集和评估基准，以支持“质谱结构推理”或“化学大模型”的研究，提供了直接的参考范例和潜在的可迁移思路。

**📖 中文摘要**

本文针对电磁（EM）领域多模态大语言模型（MLLM）的发展，提出了一个三部分贡献。首先，为了克服数据稀缺，构建并发布了EM-100k，一个包含超过10万个EM信号-文本对的大规模数据集。其次，为了进行严格和标准化的评估，提出了EM-Bench，这是一个涵盖从感知到推理的多样化下游任务的综合性基准。最后，为了解决核心建模挑战，提出了MERLIN，一个新颖的训练框架，旨在不仅将低层信号表示与高层语义文本对齐，而且明确增强模型在具有挑战性的低信噪比环境中的鲁棒性和性能。综合实验验证了该方法，表明MERLIN在EM-Bench上达到了最先进的水平，并在低信噪比设置下表现出显著的鲁棒性。论文的核心是构建用于电磁信号理解的多模态大语言模型（MLLM），并提供了相应的数据集和基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The paradigm of Multimodal Large Language Models (MLLMs) offers a promising blueprint for advancing the electromagnetic (EM) domain. However, prevailing approaches often deviate from the native MLLM paradigm, instead using task-specific or pipelined architectures that lead to fundamental limitations in model performance and generalization. Fully realizing the MLLM potential in EM domain requires overcoming three main challenges: (1) Data. The scarcity of high-quality datasets with paired EM signals and descriptive text annotations used for MLLMs pre-training; (2) Benchmark. The absence of comprehensive benchmarks to systematically evaluate and compare the performance of models on EM signal-to-text tasks; (3) Model. A critical fragility in low Signal-to-Noise Ratio (SNR) environments, where critical signal features can be obscured, leading to significant performance degradation. To address these challenges, we introduce a tripartite contribution to establish a foundation for MLLMs in the EM domain. First, to overcome data scarcity, we construct and release EM-100k, a large-scale dataset comprising over 100,000 EM signal-text pairs. Second, to enable rigorous and standardized evaluation, we propose EM-Bench, the most comprehensive benchmark featuring diverse downstream tasks spanning from perception to reasoning. Finally, to tackle the core modeling challenge, we present MERLIN, a novel training framework designed not only to align low-level signal representations with high-level semantic text, but also to explicitly enhance model robustness and performance in challenging low-SNR environments. Comprehensive experiments validate our method, showing that MERLIN is state-of-the-art in the EM-Bench and exhibits remarkable robustness in low-SNR settings.

</details>

---

### 62. [Supporting Workflow Reproducibility by Linking Bioinformatics Tools across Papers and Executable Code](https://arxiv.org/abs/2603.08195)

**基本信息**

- 🔗 arXiv: [`2603.08195`](https://arxiv.org/abs/2603.08195)
- 👥 作者: Clémence Sebe, Olivier Ferret, Aurélie Névéol 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08195.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个自动化框架（CoPaLink）和相关的语料库，用于链接科学文献中的工具描述和可执行代码中的工具使用。虽然其直接应用领域是生物信息学工作流，但这种连接“文本描述”与“可执行工具/资源”的方法，对于化学信息学和质谱分析领域构建类似的资源链接系统（例如，将质谱数据分析方法论文中提到的算法、软件与实际的代码库、数据集链接起来）具有重要的参考价值，属于提供了一种可用于这些主题的工具或资源链接方法。

**📖 中文摘要**

本文提出了CoPaLink，一种自动化方法，用于将工作流代码中的生物信息学工具与其在已发表工作流描述中的提及链接起来。该方法集成了三个组件：用于识别科学文本中工具提及的命名实体识别（NER）、用于识别工作流代码中工具提及的NER，以及基于生物信息学知识库的实体链接。论文为所有三个步骤提出了方法，在基于Bioconda和Bioweb知识库的Nextflow工作流上评估时，实现了较高的个体F1值（84-89）和66的联合准确率。CoPaLink利用了带有标注工具注释的科学文章和工作流可执行代码的语料库，以弥合叙述性描述和工作流实现之间的差距。论文的核心是开发自动化工具，链接科学文本（论文）和可执行代码（工作流）中提到的生物信息学工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: The rapid growth of biological data has intensified the need for transparent, reproducible, and well-documented computational workflows. The ability to clearly connect the steps of a workflow in the code with their description in a paper would improve workflow understanding, support reproducibility, and facilitate reuse. This task requires the linking of Bioinformatics tools in workflow code with their mentions in a published workflow description. Results: We present CoPaLink, an automated approach that integrates three components: Named Entity Recognition (NER) for identifying tool mentions in scientific text, NER for tool mentions in workflow code, and entity linking grounded on Bioinformatics knowledge bases. We propose approaches for all three steps achieving a high individual F1-measure (84 - 89) and a joint accuracy of 66 when evaluated on Nextflow workflows using Bioconda and Bioweb Knowledge bases. CoPaLink leverages corpora of scientific articles and workflow executable code with curated tool annotations to bridge the gap between narrative descriptions and workflow implementations. Availability: The code is available at this https URL and this https URL . The corpora are also available at this https URL , this https URL and this https URL .

</details>

---

### 63. [FinToolBench: Evaluating LLM Agents for Real-World Financial Tool Use](https://arxiv.org/abs/2603.08262)

**基本信息**

- 🔗 arXiv: [`2603.08262`](https://arxiv.org/abs/2603.08262)
- 👥 作者: Jiaxuan Lu, Kong Wang, Yemin Wang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08262.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门用于评估大语言模型（LLM）智能体在特定领域（金融）工具使用能力的基准（FinToolBench），包括大量可执行工具和查询。这种构建领域特定、工具使用评估基准的方法论，对于化学信息学和质谱分析领域构建类似的评估基准（例如，评估LLM智能体使用化学数据库、质谱解析软件或分子模拟工具的能力）具有重要的借鉴意义，属于提供了可用于这些主题的评估框架和资源构建思路。

**📖 中文摘要**

本文介绍了FinToolBench，这是第一个专门用于评估金融工具学习智能体的真实世界、可运行的基准。FinToolBench建立了一个真实的生态系统，将760个可执行的金融工具与295个严格的、需要工具使用的查询相结合。论文提出了一个新颖的评估框架，超越了二元执行成功，从金融关键维度评估智能体：及时性、意图类型和监管领域对齐。此外，提出了FATR，一个金融感知的工具检索和推理基线，以增强稳定性和合规性。通过提供第一个用于可审计、智能体化金融执行的测试平台，FinToolBench为金融领域的可信AI设立了新标准。论文的核心是构建一个用于评估大语言模型智能体在真实金融工具使用场景中性能的基准和数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into the financial domain is driving a paradigm shift from passive information retrieval to dynamic, agentic interaction. While general-purpose tool learning has witnessed a surge in benchmarks, the financial sector, characterized by high stakes, strict compliance, and rapid data volatility, remains critically underserved. Existing financial evaluations predominantly focus on static textual analysis or document-based QA, ignoring the complex reality of tool execution. Conversely, general tool benchmarks lack the domain-specific rigor required for finance, often relying on toy environments or a negligible number of financial APIs. To bridge this gap, we introduce FinToolBench, the first real-world, runnable benchmark dedicated to evaluating financial tool learning agents. Unlike prior works limited to a handful of mock tools, FinToolBench establishes a realistic ecosystem coupling 760 executable financial tools with 295 rigorous, tool-required queries. We propose a novel evaluation framework that goes beyond binary execution success, assessing agents on finance-critical dimensions: timeliness, intent type, and regulatory domain alignment. Furthermore, we present FATR, a finance-aware tool retrieval and reasoning baseline that enhances stability and compliance. By providing the first testbed for auditable, agentic financial execution, FinToolBench sets a new standard for trustworthy AI in finance. The tool manifest, execution environment, and evaluation code will be open-sourced to facilitate future research.

</details>

---

### 64. [LAMUS: A Large-Scale Corpus for Legal Argument Mining from U.S. Caselaw using LLMs](https://arxiv.org/abs/2603.08286)

**基本信息**

- 🔗 arXiv: [`2603.08286`](https://arxiv.org/abs/2603.08286)
- 👥 作者: Serene Wang, Lavanya Pobbathi, Haihua Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08286.pdf)

**💡 相关性分析**

满足标准2：论文详细描述了一个利用大语言模型（LLM）自动化辅助构建大规模领域特定（法律）文本标注数据集（LAMUS）的流程和方法。这种数据构建方法论对于化学信息学和质谱分析领域具有极高的参考价值，可以应用于构建“质谱-分子结构”配对数据集、“化学文献-反应条件”标注数据集等，以支持化学大模型的训练和评估，属于提供了可用于这些主题的数据集构建工具和方法。

**📖 中文摘要**

本文介绍了LAMUS，一个从美国最高法院判决和德克萨斯州刑事上诉意见书中构建的句子级法律论据挖掘语料库。该数据集是使用一个以数据为中心的流程创建的，该流程结合了大规模案例收集、基于LLM的自动标注和有针对性的“人在回路”质量精化。我们将法律论据挖掘制定为一个六类句子分类任务，并在零样本、少样本和思维链提示策略下评估了多个通用和特定领域的语言模型，并以LegalBERT作为监督基线。结果表明，思维链提示显著提高了LLM性能，而特定领域模型表现出更稳定的零样本行为。LLM辅助的验证纠正了近20%的标注错误，提高了标签一致性。人类验证达到了0.85的Cohen's Kappa，确认了标注质量。LAMUS为未来的法律NLP研究提供了可扩展的资源和实证见解。论文的核心是使用大语言模型辅助构建了一个大规模、高质量的法律文本标注数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Legal argument mining aims to identify and classify the functional components of judicial reasoning, such as facts, issues, rules, analysis, and conclusions. Progress in this area is limited by the lack of large-scale, high-quality annotated datasets for U.S. caselaw, particularly at the state level. This paper introduces LAMUS, a sentence-level legal argument mining corpus constructed from U.S. Supreme Court decisions and Texas criminal appellate opinions. The dataset is created using a data-centric pipeline that combines large-scale case collection, LLM-based automatic annotation, and targeted human-in-the-loop quality refinement. We formulate legal argument mining as a six-class sentence classification task and evaluate multiple general-purpose and legal-domain language models under zero-shot, few-shot, and chain-of-thought prompting strategies, with LegalBERT as a supervised baseline. Results show that chain-of-thought prompting substantially improves LLM performance, while domain-specific models exhibit more stable zero-shot behavior. LLM-assisted verification corrects nearly 20% of annotation errors, improving label consistency. Human verification achieves Cohen's Kappa of 0.85, confirming annotation quality. LAMUS provides a scalable resource and empirical insights for future legal NLP research. All code and datasets can be accessed for reproducibility on GitHub at: this https URL

</details>

---

### 65. [Deconstructing Multimodal Mathematical Reasoning: Towards a Unified Perception-Alignment-Reasoning Paradigm](https://arxiv.org/abs/2603.08291)

**基本信息**

- 🔗 arXiv: [`2603.08291`](https://arxiv.org/abs/2603.08291)
- 👥 作者: Tianyu Yang, Sihong Wu, Yilun Zhao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08291.pdf)

**💡 相关性分析**

满足标准3：论文是一篇系统性的综述和展望文章，专门针对“多模态推理”这一主题进行了深入讨论，并提出了一个统一的分析框架（感知-对齐-推理范式）。虽然其直接应用是数学问题，但其核心主题——如何让AI模型结合文本和视觉信息进行复杂推理——与化学信息学和质谱分析中的核心挑战“质谱结构推理”（即结合质谱图（视觉/数值数据）和化学知识（文本）推断分子结构）在方法论上高度同构。因此，该论文包含了对“多模态推理”这一与“质谱结构推理”紧密相关主题的重要讨论和展望。

**📖 中文摘要**

多模态数学推理（MMR）最近因其解决涉及文本和视觉模态的数学问题的能力而受到越来越多的关注。然而，当前的模型在现实世界的视觉数学任务中仍然面临重大挑战。它们经常误解图表，未能将数学符号与视觉证据对齐，并产生不一致的推理步骤。此外，现有的评估主要关注检查最终答案，而不是验证每个中间步骤的正确性或可执行性。为了解决这些限制，最近越来越多的研究通过将结构化感知、显式对齐和可验证推理集成到统一框架中来应对这些问题。为了建立理解和比较不同MMR方法的清晰路线图，我们围绕四个基本问题对它们进行了系统研究：（1）从多模态输入中提取什么，（2）如何表示和对齐文本和视觉信息，（3）如何进行推理，以及（4）如何评估整个推理过程的正确性。最后，我们讨论了开放挑战，并展望了未来研究的有希望的方向。本文是一篇关于多模态数学推理的综述和展望论文。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal Mathematical Reasoning (MMR) has recently attracted increasing attention for its capability to solve mathematical problems that involve both textual and visual modalities. However, current models still face significant challenges in real-world visual math tasks. They often misinterpret diagrams, fail to align mathematical symbols with visual evidence, and produce inconsistent reasoning steps. Moreover, existing evaluations mainly focus on checking final answers rather than verifying the correctness or executability of each intermediate step. To address these limitations, a growing body of recent research addresses these issues by integrating structured perception, explicit alignment, and verifiable reasoning within unified frameworks. To establish a clear roadmap for understanding and comparing different MMR approaches, we systematically study them around four fundamental questions: (1) What to extract from multimodal inputs, (2) How to represent and align textual and visual information, (3) How to perform the reasoning, and (4) How to evaluate the correctness of the overall reasoning process. Finally, we discuss open challenges and offer perspectives on promising directions for future research.

</details>

---

### 66. [PCFEx: Point Cloud Feature Extraction for Graph Neural Networks](https://arxiv.org/abs/2603.08540)

**基本信息**

- 🔗 arXiv: [`2603.08540`](https://arxiv.org/abs/2603.08540)
- 👥 作者: Abdullah Al Masud, Shi Xintong, Mondher Bouazizi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08540.pdf)

**💡 相关性分析**

满足标准2：论文提出的图神经网络（GNN）架构和点云特征提取（PCFEx）技术，是构建和处理图结构数据（如分子图）的核心方法，可直接应用于化学大模型（用于分子表示学习）和质谱结构推理（用于谱图-结构关联建模）领域，提供了相关的模型工具思路。

**📖 中文摘要**

本文提出了一种新颖的点云特征提取（PCFEx）技术，用于处理3D点云数据以进行人体姿态估计（HPE）和人类活动识别（HAR）。该方法将点云视为图，并在点、边和图级别提取有意义的特征。作者进一步设计了一个图神经网络（GNN）架构来高效处理这些特征。该工作展示了将特征提取与GNN建模相结合的方法在增强点云处理精度方面的巨大潜力。虽然论文主要关注雷达点云和人体分析，但其核心贡献——用于点云处理的图神经网络特征提取方法——是通用的。图神经网络是构建化学大模型（用于分子图表示和性质预测）和质谱结构推理（用于将质谱数据与分子图结构关联）的关键技术之一。因此，该论文提出的GNN架构和特征提取技术为相关领域提供了可借鉴的方法论和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph neural networks (GNNs) have gained significant attention for their effectiveness across various domains. This study focuses on applying GNN to process 3D point cloud data for human pose estimation (HPE) and human activity recognition (HAR). We propose novel point cloud feature extraction (PCFEx) techniques to capture meaningful information at the point, edge, and graph levels of the point cloud by considering point cloud as a graph. Moreover, we introduce a GNN architecture designed to efficiently process these features. Our approach is evaluated on four most popular publicly available millimeter wave radar datasets, three for HPE and one for HAR. The results show substantial improvements, with significantly reduced errors in all three HPE benchmarks, and an overall accuracy of 98.8% in mmWave-based HAR, outperforming the existing state of the art models. This work demonstrates the great potential of feature extraction incorporated with GNN modeling approach to enhance the precision of point cloud processing.

</details>

---

### 67. [mmGAT: Pose Estimation by Graph Attention with Mutual Features from mmWave Radar Point Cloud](https://arxiv.org/abs/2603.08551)

**基本信息**

- 🔗 arXiv: [`2603.08551`](https://arxiv.org/abs/2603.08551)
- 👥 作者: Abdullah Al Masud, Shi Xintong, Mondher Bouazizi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08551.pdf)

**💡 相关性分析**

满足标准2：论文专注于利用图注意力网络（GAT）从点云数据中推理结构信息（人体姿态）。这种“从数据推理结构”的核心范式与“质谱结构推理”（从质谱数据推理分子结构）高度相似。其采用的图神经网络和注意力机制是解决此类结构推理问题的关键技术，为质谱结构推理提供了直接相关的模型架构参考。

**📖 中文摘要**

本文提出mmGAT模型，利用图注意力网络（GAT）处理毫米波雷达点云数据进行人体姿态估计。作者开发了一种独特的特征提取技术，以充分发挥GNN处理方法的潜力，旨在捕捉雷达点云的更精细细节以提升姿态估计性能。该模型在两个公开的毫米波雷达基准数据集上取得了最先进的成果。这项工作展示了GNN与注意力机制结合在从复杂点云数据中推理结构信息方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pose estimation and human action recognition (HAR) are pivotal technologies spanning various domains. While the image-based pose estimation and HAR are widely admired for their superior performance, they lack in privacy protection and suboptimal performance in low-light and dark environments. This paper exploits the capabilities of millimeter-wave (mmWave) radar technology for human pose estimation by processing radar data with Graph Neural Network (GNN) architecture, coupled with the attention mechanism. Our goal is to capture the finer details of the radar point cloud to improve the pose estimation performance. To this end, we present a unique feature extraction technique that exploits the full potential of the GNN processing method for pose estimation. Our model mmGAT demonstrates remarkable performance on two publicly available benchmark mmWave datasets and establishes new state of the art results in most scenarios in terms of human pose estimation. Our approach achieves a noteworthy reduction of pose estimation mean per joint position error (MPJPE) by 35.6% and PA-MPJPE by 14.1% from the current state of the art benchmark within this domain.

</details>

---

### 68. [DualFlexKAN: Dual-stage Kolmogorov-Arnold Networks with Independent Function Control](https://arxiv.org/abs/2603.08583)

**基本信息**

- 🔗 arXiv: [`2603.08583`](https://arxiv.org/abs/2603.08583)
- 👥 作者: Andrés Ortiz, Nicolás J. Gallego-Molina, Carmen Jiménez-Mesa 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是Kolmogorov-Arnold网络（KAN），这是一种新兴的、具有高表达能力和可解释性的神经网络架构。在化学信息学领域，探索新型神经网络模型（如KAN）用于分子性质预测、谱图分析等任务，是“化学大模型”研究方向的一个重要前沿分支。该论文对KAN的改进和系统性评估为此方向提供了直接相关的模型创新和研究参考。

**📖 中文摘要**

本文介绍了DualFlexKAN（DFKAN），一种灵活的Kolmogorov-Arnold网络（KAN）架构。KAN通过边缘可学习函数替代传统MLP的固定激活函数，提供了更强的表达能力和可解释性。DFKAN采用双阶段机制，独立控制线性前输入变换和线性后输出激活，支持混合网络配置以权衡表达能力和计算成本。该框架支持多种基函数族，并与可配置的正则化策略集成，在回归、物理信息任务和函数逼近基准测试中，以少一至两个数量级的参数优于MLP和传统KAN。DFKAN为在科学应用中融入自适应非线性和进行可解释函数发现提供了一个原则性、可扩展的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-Layer Perceptrons (MLPs) rely on pre-defined, fixed activation functions, imposing a static inductive bias that forces the network to approximate complex topologies solely through increased depth and width. Kolmogorov-Arnold Networks (KANs) address this limitation through edge-centric learnable functions, yet their formulation suffers from quadratic parameter scaling and architectural rigidity that hinders the effective integration of standard regularization techniques. This paper introduces the DualFlexKAN (DFKAN), a flexible architecture featuring a dual-stage mechanism that independently controls pre-linear input transformations and post-linear output activations. This decoupling enables hybrid networks that optimize the trade-off between expressiveness and computational cost. Unlike standard formulations, DFKAN supports diverse basis function families, including orthogonal polynomials, B-splines, and radial basis functions, integrated with configurable regularization strategies that stabilize training dynamics. Comprehensive evaluations across regression benchmarks, physics-informed tasks, and function approximation demonstrate that DFKAN outperforms both MLPs and conventional KANs in accuracy, convergence speed, and gradient fidelity. The proposed hybrid configurations achieve superior performance with one to two orders of magnitude fewer parameters than standard KANs, effectively mitigating the parameter explosion problem while preserving KAN-style expressiveness. DFKAN provides a principled, scalable framework for incorporating adaptive non-linearities, proving particularly advantageous for data-efficient learning and interpretable function discovery in scientific applications.

</details>

---

### 69. [Integral Formulas for Vector Spherical Tensor Products](https://arxiv.org/abs/2603.08630)

**基本信息**

- 🔗 arXiv: [`2603.08630`](https://arxiv.org/abs/2603.08630)
- 👥 作者: Valentin Heyraud, Zachary Weller-Davies, Jules Tilly
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08630.pdf)

**💡 相关性分析**

满足标准2：论文专注于SO(3)-等变神经网络中的张量积操作，这是构建具有旋转等变性的几何深度学习模型（包括用于分子3D结构的化学大模型）的核心数学工具。提出的向量球面张量积及其高效实现，为处理三维几何数据（如分子构象）的神经网络提供了关键的算法资源和计算工具，与化学大模型的研究直接相关。

**📖 中文摘要**

本文推导了简化最近由Xie等人引入的向量球面张量积（Vector Spherical Tensor Product）的积分公式。向量球面张量积将Gaunt张量积推广到反对称耦合。作者获得了反对称类似Gaunt系数的显式闭式表达式，从而能够使用单个向量球面张量积来模拟Clebsch-Gordan张量积，将所需的张量积计算量减少9倍。该结果实现了向量球面张量积的高效实用实现，为这种Gaunt张量积推广在SO(3)-等变神经网络中的应用铺平了道路。此外，论文讨论了Gaunt和向量球面张量积如何允许控制与通常的Clebsch-Gordan张量积相关的表达能力-运行时权衡，并研究了所考虑张量积的归一化的低秩分解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We derive integral formulas that simplify the Vector Spherical Tensor Product recently introduced by Xie et al., which generalizes the Gaunt tensor product to antisymmetric couplings. In particular, we obtain explicit closed-form expressions for the antisymmetric analogues of the Gaunt coefficients. This enables us to simulate the Clebsch-Gordan tensor product using a single Vector Spherical Tensor Product, yielding a $9\times$ reduction in the required tensor product evaluations. Our results enable efficient and practical implementations of the Vector Spherical Tensor Product, paving the way for applications of this generalization of Gaunt tensor products in $\mathrm{SO}(3)$-equivariant neural networks. Moreover, we discuss how the Gaunt and the Vector Spherical Tensor Products allow to control the expressivity-runtime tradeoff associated with the usual Clebsch-Gordan Tensor Products. Finally, we investigate low rank decompositions of the normalizations of the considered tensor products in view of their use in equivariant neural networks.

</details>

---

### 70. [GNN For Muon Particle Momentum estimation](https://arxiv.org/abs/2603.06675)

**基本信息**

- 🔗 arXiv: [`2603.06675`](https://arxiv.org/abs/2603.06675)
- 👥 作者: Vishak K Bhat, Eric A. F. Reinhardt, Sergei Gleyzer
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06675.pdf)

**💡 相关性分析**

满足标准2：论文应用图神经网络（GNN）解决高能物理中的粒子动量估计问题，其核心是将探测器数据构建为图并使用GNN进行回归预测。这种方法论与化学信息学中将分子表示为图并使用GNN预测分子性质（化学大模型的核心任务）以及将质谱峰关联为图并进行结构推理（质谱结构推理）在技术路径上高度一致。该工作为处理科学仪器产生的复杂结构化数据提供了GNN应用的实例和验证。

**📖 中文摘要**

本文探索使用图神经网络（GNN）进行μ子粒子动量估计的任务。由于大型强子对撞机CMS实验产生的数据总量远大于感兴趣的数据量，因此结合使用硬件和软件触发器来选择要捕获的数据。精确的动量计算对于提高CMS触发器系统的效率至关重要，从而能够更好地区分低动量和高动量粒子并减少误触发。作者提出了两种图构建方法，并应用GNN模型来利用数据固有的图结构。论文表明，GNN在平均绝对误差（MAE）方面优于传统模型（如TabNet），证明了其在捕捉数据内复杂依赖关系方面的有效性。同时指出节点特征的维度对GNN的效率至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Due to a high rate of overall data generation relative to data generation of interest, the CMS experiment at the Large Hadron Collider uses a combination of hardware- and software-based triggers to select data for capture. Accurate momentum calculation is crucial for improving the efficiency of the CMS trigger systems, enabling better classification of low- and high- momentum particles and reducing false triggers. This paper explores the use of Graph Neural Networks (GNNs) for the momentum estimation task. We present two graph construction methods and apply a GNN model to leverage the inherent graph structure of the data. In this paper firstly, we show that the GNN outperforms traditional models like TabNet in terms of Mean Absolute Error (MAE), demonstrating its effectiveness in capturing complex dependencies within the data. Secondly we show that the dimension of the node feature is crucial for the efficiency of GNN.

</details>

---

### 71. [ViroGym: Realistic Large-Scale Benchmarks for Evaluating Viral Proteins](https://arxiv.org/abs/2603.06740)

**基本信息**

- 🔗 arXiv: [`2603.06740`](https://arxiv.org/abs/2603.06740)
- 👥 作者: Yichen Zhou, Jonathan Golob, Amir Karimi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06740.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接应用了蛋白质语言模型（pLMs），这是化学/生物大模型在蛋白质序列分析领域的典型代表，与“化学大模型”主题直接相关。

**📖 中文摘要**

本文介绍了ViroGym，一个用于评估病毒蛋白质变体效应预测的综合基准。该研究利用蛋白质语言模型（pLMs）在零样本设置下预测错义变体的功能效应。虽然论文核心是病毒蛋白质的变体效应预测和疫苗候选选择，但其核心方法——使用蛋白质语言模型（pLMs）——属于“化学大模型”在生物分子领域的直接应用。pLMs是专门针对蛋白质序列训练的大规模预训练模型，是化学信息学和生物信息学中“大模型”的重要分支。因此，该论文提供了应用化学大模型（蛋白质语言模型）解决具体科学问题（病毒蛋白功能预测）的实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (pLMs) have shown strong potential in prediction of the functional effects of missense variants in zero-shot settings. Despite this progress, benchmarking pLMs for viral proteins remains limited and systematic strategies for integrating in silico metrics with in vitro validation to guide antigen and target selection are underdeveloped. Here, we introduce ViroGym, a comprehensive benchmark designed to evaluate variant effect prediction in viral proteins and to facilitate selecting rational antigen candidates. We curated 79 deep mutational scanning (DMS) assays encompassing eukaryotic viruses, collectively comprising 552,937 mutated amino acid sequences across 7 distinct phenotypic readouts, and 21 influenza virus neutralisation tasks and a real-world predictive task for SARS-CoV-2. We benchmark well-established pLMs on fitness landscapes, antigenic diversity, and pandemic forecasting to provide a framework for vaccine selection, and show that pLMs selected using in vitro experimental data excel at predicting dominant circulating mutations in real world.

</details>

---

### 72. [How Private Are DNA Embeddings? Inverting Foundation Model Representations of Genomic Sequences](https://arxiv.org/abs/2603.06950)

**基本信息**

- 🔗 arXiv: [`2603.06950`](https://arxiv.org/abs/2603.06950)
- 👥 作者: Sofiane Ouaari, Jules Kreuer, Nico Pfeifer
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06950.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究对象是DNA基础模型（DNA foundation models），这是专门处理DNA序列化学信息的大模型，直接围绕“化学大模型”主题展开，并深入探讨了其隐私特性。

**📖 中文摘要**

本研究评估了DNA基础模型（DNABERT-2, Evo 2, Nucleotide Transformer v2）对模型反转攻击的隐私脆弱性。这些模型在大量基因组数据上训练，能够生成捕获复杂基因组信息的序列嵌入。论文探讨了从这些嵌入中重建原始DNA序列的可能性，揭示了在嵌入即服务（EaaS）框架下共享这些表示所带来的隐私风险。DNA基础模型是专门针对DNA序列设计和训练的大规模预训练模型，属于“化学大模型”在基因组学领域的核心应用。论文的核心是分析和评估这类大模型的安全性与隐私性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

DNA foundation models have become transformative tools in bioinformatics and healthcare applications. Trained on vast genomic datasets, these models can be used to generate sequence embeddings, dense vector representations that capture complex genomic information. These embeddings are increasingly being shared via Embeddings-as-a-Service (EaaS) frameworks to facilitate downstream tasks, while supposedly protecting the privacy of the underlying raw sequences. However, as this practice becomes more prevalent, the security of these representations is being called into question. This study evaluates the resilience of DNA foundation models to model inversion attacks, whereby adversaries attempt to reconstruct sensitive training data from model outputs. In our study, the model's output for reconstructing the DNA sequence is a zero-shot embedding, which is then fed to a decoder. We evaluated the privacy of three DNA foundation models: DNABERT-2, Evo 2, and Nucleotide Transformer v2 (NTv2). Our results show that per-token embeddings allow near-perfect sequence reconstruction across all models. For mean-pooled embeddings, reconstruction quality degrades as sequence length increases, though it remains substantially above random baselines. Evo 2 and NTv2 prove to be most vulnerable, especially for shorter sequences with reconstruction similarities > 90%, while DNABERT-2's BPE tokenization provides the greatest resilience. We found that the correlation between embedding similarity and sequence similarity was a key predictor of reconstruction success. Our findings emphasize the urgent need for privacy-aware design in genomic foundation models prior to their widespread deployment in EaaS settings. Training code, model weights and evaluation pipeline are released on: this https URL .

</details>

---

### 73. [AI-Driven Phase Identification from X-ray Hyperspectral Imaging of cycled Na-ion Cathode Materials](https://arxiv.org/abs/2603.07666)

**基本信息**

- 🔗 arXiv: [`2603.07666`](https://arxiv.org/abs/2603.07666)
- 👥 作者: Fayçal Adrar, Nicolas Folastre, Chloé Pablos 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07666.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心是开发AI驱动的化学数据分析方法（GMVAE），属于化学信息学中模型应用的范畴；2) 论文提出的方法流程（GMVAE + 相关性分析）可被视为一种用于分析复杂化学光谱/成像数据的“工具”或“框架”，其思路可用于质谱等光谱数据的结构推理分析。

**📖 中文摘要**

本研究开发了一种AI驱动的方法，用于处理在稀疏采样条件下的X射线超光谱成像数据，以绘制钠离子电池正极材料NaxV2(PO4)2F3在不同荷电状态下的纳米级多相分布图。该方法的核心是结合高斯混合变分自编码器（GMVAE）算法和皮尔逊相关系数来识别钠含量并绘制其空间分布。这项工作展示了AI和机器学习模型（特别是GMVAE）在分析复杂的化学和材料科学数据（来自扫描透射X射线显微镜STXM）方面的强大能力。虽然模型规模可能不及“大模型”，但其工作流程（AI驱动处理、特征学习、分布映射）体现了化学信息学中数据驱动模型的核心思想，并且其处理的光谱数据与质谱分析在原理（光谱分析）和数据复杂性上具有可比性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Na-ion batteries have emerged as viable candidates for large-scale energy storage applica- tions due to resource abundance and cost advantages. The constraints imposed on their performance and durability, for instance, by complex phase transformations in positive electrode materials during electrochemical cycling, can be addressed and are thus not detrimental to their development. However, diffusion-limited Na-ion transport can drive spatially heterogeneous phase nucleation and propagation, leading to multiphase coexis- tence and locally non-uniform electrochemical activity, generating complex reaction path- ways that challenge both mechanistic understanding and predictive material optimization. These challenges can be addressed by investigating single-crystalline regions of materials, i.e. down to the scale of individual particles, although such analyses are often constrained by energetically and/or spatially sparse hyperspectral datasets. Here, we developed an AI-driven method to process hyperspectral data under sparse sampling conditions and generate multiphase maps with nanometer-scale resolution over a micrometer-scale field of view. We applied this processing on scanning transmission X-ray microscopy (STXM) data to determine the distribution and coexistence of phases in individual particles of NaxV2(PO4)2F3 cathode materials, at different states of charge. The methodology relies on a workflow which combines a Gaussian mixture variational autoencoder (GMVAE) algorithm with the Pearson corre- lation coefficient to identify the sodium content and map their spatial distribution. Our approach reveals nanoscale phase heterogeneity and evolution within individual particles, and improves the reliability of phase detection by identifying ambiguity zones, false assign- ments, and transition phases localized at grain boundaries.

</details>

---

### 74. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进机器学习原子间势（MLIPs），这是计算化学和材料科学中至关重要的“化学大模型”。论文提出的MoE架构是专门为扩展和提升这类模型性能而设计的，直接围绕“化学大模型”的架构创新主题。

**📖 中文摘要**

本文为机器学习原子间势（MLIPs）系统地开发了混合专家（MoE）和混合线性专家（MoLE）架构。MLIPs是用于大规模原子模拟的关键工具，能够以量子力学精度预测原子系统的能量和力。论文通过引入稀疏激活和共享专家，显著提升了MLIPs的表达能力和准确性，并在多个基准测试（OMol25, OMat24, OC20M）上达到了最先进的性能。这项工作直接针对化学和材料科学中的核心计算模型——原子间势，并通过先进的神经网络架构（MoE）对其进行扩展和增强。MLIPs本身就是化学领域特定的大参数模型，MoE架构的引入是构建更强大“化学大模型”的前沿方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 75. [LoRA-Ensemble: Efficient Uncertainty Modelling for Self-Attention Networks](https://arxiv.org/abs/2405.14438)

**基本信息**

- 🔗 arXiv: [`2405.14438`](https://arxiv.org/abs/2405.14438)
- 👥 作者: Dominik J. Mühlematter, Michelle Halbheer, Alexander Becker 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.14438.pdf)

**💡 相关性分析**

满足标准2：论文提出的LoRA-Ensemble方法是一种高效的模型集成与不确定性量化技术，基于Transformer架构和LoRA适配器。该技术可直接应用于“化学大模型”（通常基于Transformer），为其提供高效的校准和不确定性评估工具，属于可用于这些主题的工具方法。

**📖 中文摘要**

本文提出了LoRA-Ensemble，一种用于自注意力网络的高效集成方法，旨在量化模型预测的不确定性。该方法基于低秩自适应（LoRA），将其扩展为一种隐式集成方案，其中所有集成成员共享同一个预训练的自注意力网络，但拥有各自独立的低秩矩阵用于注意力投影。虽然论文的通用背景是机器学习模型的不确定性估计，但其核心方法LoRA最初是为大语言模型（LLMs）的高效微调而开发的，并且论文将其应用于自注意力网络（Transformer架构的核心）。Transformer是当今绝大多数“化学大模型”（如分子Transformer、蛋白质语言模型）的基础架构。因此，该论文提出的高效集成技术，对于在资源受限环境下部署和评估大型化学模型具有直接的方法学参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Numerous real-world decisions rely on machine learning algorithms and require calibrated uncertainty estimates. However, modern methods often yield overconfident, uncalibrated predictions. The dominant approach to quantifying the uncertainty inherent in the model is to train an ensemble of separate predictors and measure their empirical variance. In an explicit implementation, the ensemble has a high computational cost and memory footprint, especially if the base model itself is already large, like modern transformers. This motivates efforts to develop implicit ensemble methods that emulate the ensemble without explicitly instantiating all its members. We introduce LoRA-Ensemble, a parameter-efficient ensembling method for self-attention networks. It is based on Low-Rank Adaptation (LoRA), originally developed for efficient LLM fine-tuning, and extends it into an implicit ensembling scheme, where all ensemble members share the same, pre-trained self-attention network, but have individual low-rank matrices for the attention projections. The resulting method not only outperforms state-of-the-art implicit techniques like BatchEnsemble, but even matches or exceeds the accuracy of an Explicit Ensemble, while at the same time achieving superior calibration.

</details>

---

### 76. [BNEM: A Boltzmann Sampler Based on Bootstrapped Noised Energy Matching](https://arxiv.org/abs/2409.09787)

**基本信息**

- 🔗 arXiv: [`2409.09787`](https://arxiv.org/abs/2409.09787)
- 👥 作者: RuiKang OuYang, Bo Qiang, José Miguel Hernández-Lobato
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.09787.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的生成式采样器，用于从能量函数中采样。这直接关联到“化学大模型”主题，因为生成模型是构建化学大模型（用于分子设计、性质预测等）的核心技术之一。

**📖 中文摘要**

本文提出了一种基于扩散的采样器BNEM，用于从给定的能量函数（如分子动力学中的玻尔兹曼分布）生成独立同分布样本。该方法通过学习噪声数据的能量，提出了Noised Energy Matching (NEM)采样器，理论上具有更低的方差和更高的复杂度。进一步，通过应用一种新颖的自举技术来平衡偏差和方差，形成了BNEM。论文在二维40高斯混合模型和4粒子双阱势等系统上进行了评估。该方法的核心是学习一个神经采样器来模拟复杂的概率分布，这与化学信息学中用于分子生成和性质预测的生成模型（化学大模型）在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing an efficient sampler capable of generating independent and identically distributed (IID) samples from a Boltzmann distribution is a crucial challenge in scientific research, e.g. molecular dynamics. In this work, we intend to learn neural samplers given energy functions instead of data sampled from the Boltzmann distribution. By learning the energies of the noised data, we propose a diffusion-based sampler, Noised Energy Matching, which theoretically has lower variance and more complexity compared to related works. Furthermore, a novel bootstrapping technique is applied to NEM to balance between bias and variance. We evaluate NEM and BNEM on a 2-dimensional 40 Gaussian Mixture Model (GMM) and a 4-particle double-well potential (DW-4). The experimental results demonstrate that BNEM can achieve state-of-the-art performance while being more robust.

</details>

---

### 77. [Open-World Reinforcement Learning over Long Short-Term Imagination](https://arxiv.org/abs/2410.03618)

**基本信息**

- 🔗 arXiv: [`2410.03618`](https://arxiv.org/abs/2410.03618)
- 👥 作者: Jiajian Li, Qi Wang, Yunbo Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.03618.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个生成式世界模型（LS-Imagine），用于长时程的决策和探索。生成式世界模型是“化学大模型”的一种重要表现形式，用于学习化学空间或质谱数据的底层分布与规律。

**📖 中文摘要**

本文提出了LS-Imagine，一种用于开放世界视觉强化学习的方法。其核心是构建一个“长短时世界模型”，通过模拟目标条件下的跳跃状态转移和计算相应的可达性图，来整合长期价值到行为学习中。该方法在MineDojo等环境中展示了优于现有技术的性能。虽然论文主要关注强化学习，但其构建生成式世界模型（特别是用于预测和规划）的方法论，与构建用于化学或质谱数据理解的生成模型（化学大模型）在理念和技术路径上有相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training visual reinforcement learning agents in a high-dimensional open world presents significant challenges. While various model-based methods have improved sample efficiency by learning interactive world models, these agents tend to be "short-sighted", as they are typically trained on short snippets of imagined experiences. We argue that the primary challenge in open-world decision-making is improving the exploration efficiency across a vast state space, especially for tasks that demand consideration of long-horizon payoffs. In this paper, we present LS-Imagine, which extends the imagination horizon within a limited number of state transition steps, enabling the agent to explore behaviors that potentially lead to promising long-term feedback. The foundation of our approach is to build a $\textit{long short-term world model}$. To achieve this, we simulate goal-conditioned jumpy state transitions and compute corresponding affordance maps by zooming in on specific areas within single images. This facilitates the integration of direct long-term values into behavior learning. Our method demonstrates significant improvements over state-of-the-art techniques in MineDojo.

</details>

---

### 78. [Noise-Aware System Identification for High-Dimensional Stochastic Dynamics](https://arxiv.org/abs/2411.00002)

**基本信息**

- 🔗 arXiv: [`2411.00002`](https://arxiv.org/abs/2411.00002)
- 👥 作者: Ziheng Guo, Igor Cialenco, Ming Zhong
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.00002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从数据中学习随机动力学模型，这直接关联到“化学大模型”和“质谱结构推理”主题。在化学领域，从分子模拟数据或光谱数据学习分子势能面、反应动力学或质谱碎裂规律，正是构建化学大模型和进行结构推理的关键任务。

**📖 中文摘要**

本文介绍了一种噪声感知的系统辨识框架，用于从高维随机动力系统的轨迹数据中联合恢复确定性漂移和完整的噪声结构。该方法适用于广泛的随机动力学，包括有色噪声和乘性噪声，并能高效地扩展到高维系统。论文在多种系统上进行了数值实验验证。该方法的核心是从数据中学习复杂的随机动力学模型，这与化学信息学和质谱分析中从实验数据（如分子动力学模拟轨迹、质谱时间序列）推断潜在物理或化学模型的任务高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Stochastic dynamical systems are ubiquitous in physics, biology, and engineering, where both deterministic drifts and random fluctuations govern system behavior. Learning these dynamics from data is particularly challenging in high-dimensional settings with complex, correlated, or state-dependent noise. We introduce a noise-aware system identification framework that jointly recovers the deterministic drift and full noise structure directly from the trajectory data, without requiring prior assumptions on the noise model. Our method accommodates a broad class of stochastic dynamics, including colored and multiplicative noise, that scales efficiently to high-dimensional systems, and accurately reconstructs the underlying dynamics. Numerical experiments on diverse systems validate the approach and highlight its potential for data-driven modeling in complex stochastic environments.

</details>

---

### 79. [Input-Adaptive Generative Dynamics in Diffusion Models](https://arxiv.org/abs/2411.15199)

**基本信息**

- 🔗 arXiv: [`2411.15199`](https://arxiv.org/abs/2411.15199)
- 👥 作者: Yucheng Xing, Xiaodong Liu, Xin Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.15199.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进扩散模型这一重要的生成模型范式，使其生成过程具有输入自适应性。生成模型（尤其是扩散模型）是构建“化学大模型”的核心技术之一，用于分子生成、逆合成规划等。该工作对生成模型本身的改进，直接相关于化学大模型的能力提升。

**📖 中文摘要**

本文研究了扩散模型的输入自适应生成动力学。传统的扩散模型使用固定的去噪轨迹，而本文提出的框架允许生成过程根据每个样本的生成条件进行自适应调整。模型在不同时间跨度和噪声调度下进行训练，使其能够在不同的输入自适应轨迹下保持一致操作。在条件图像生成上的实验表明，该方法在保持生成质量的同时，可以减少平均采样步数。这项工作探索了生成模型（扩散模型）的自适应机制，其核心思想——使生成过程更灵活、高效——对于构建适应不同化学任务或质谱数据特性的“化学大模型”具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models typically generate data through a fixed denoising trajectory that is shared across all samples. However, generation targets can differ in complexity, suggesting that a single pre-defined diffusion process may not be optimal for every input. In this work, we investigate input-adaptive generative dynamics for diffusion models, where the generation process itself adapts to the conditions of each sample. Instead of relying on a fixed diffusion trajectory, the proposed framework allows the generative dynamics to adjust across inputs according to their generation requirements. To enable this behavior, we train the diffusion backbone under varying horizons and noise schedules, so that it can operate consistently under different input-adaptive trajectories. Experiments on conditional image generation show that diffusion trajectories can vary across inputs while maintaining generation quality and reducing the average number of sampling steps. These results provide a proof of the concept that diffusion processes can benefit from input-adaptive generative dynamics rather than relying on a single fixed trajectory.

</details>

---

### 80. [From Pixels to Predicates: Learning Symbolic World Models via Pretrained Vision-Language Models](https://arxiv.org/abs/2501.00296)

**基本信息**

- 🔗 arXiv: [`2501.00296`](https://arxiv.org/abs/2501.00296)
- 👥 作者: Ashay Athalye, Nishanth Kumar, Tom Silver 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.00296.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大规模预训练模型（VLMs）学习可解释的符号世界模型，并进行规划推理。这直接关联到“化学大模型”主题，因为化学领域同样致力于构建能够进行符号推理（如逆合成分析、反应预测）的大模型。同时，其从多模态数据（图像）中提取结构化信息的方法，也与“质谱结构推理”中从光谱数据推断分子结构的思想相通。

**📖 中文摘要**

本文旨在通过预训练的视觉语言模型（VLMs）学习抽象的符号世界模型，以解决机器人领域的长时程决策问题。关键组件是利用VLMs提出大量可能与决策相关的视觉谓词，并直接从相机图像中评估这些谓词。在训练时，通过基于优化的模型学习算法，从演示中学习一个由紧凑谓词子集定义的抽象符号世界模型。在测试时，利用VLM构建当前世界的符号描述，并使用基于搜索的规划算法找到实现目标的底层技能序列。该方法在模拟和真实世界实验中展示了强大的泛化能力。虽然应用于机器人，但其“从像素到符号”的学习范式、利用大规模预训练模型（VLMs）作为先验、以及学习可解释的符号模型进行推理和规划的核心技术，与化学信息学中“从光谱/结构到分子属性/反应”的符号推理、以及利用大模型先验进行化学知识提取和推理的研究主题高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Our aim is to learn to solve long-horizon decision-making problems in complex robotics domains given low-level skills and a handful of short-horizon demonstrations containing sequences of images. To this end, we focus on learning abstract symbolic world models that facilitate zero-shot generalization to novel goals via planning. A critical component of such models is the set of symbolic predicates that define properties of and relationships between objects. In this work, we leverage pretrained vision-language models (VLMs) to propose a large set of visual predicates potentially relevant for decision-making, and to evaluate those predicates directly from camera images. At training time, we pass the proposed predicates and demonstrations into an optimization-based model-learning algorithm to obtain an abstract symbolic world model that is defined in terms of a compact subset of the proposed predicates. At test time, given a novel goal in a novel setting, we use the VLM to construct a symbolic description of the current world state, and then use a search-based planning algorithm to find a sequence of low-level skills that achieves the goal. We demonstrate empirically across experiments in both simulation and the real world that our method can generalize aggressively, applying its learned world model to solve problems with a wide variety of object types, arrangements, numbers of objects, and visual backgrounds, as well as novel goals and much longer horizons than those seen at training time.

</details>

---

### 81. [Strengthening Generative Robot Policies through Predictive World Modeling](https://arxiv.org/abs/2502.00622)

**基本信息**

- 🔗 arXiv: [`2502.00622`](https://arxiv.org/abs/2502.00622)
- 👥 作者: Han Qi, Haocheng Yin, Aris Zhu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.00622.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法依赖于扩散模型这一生成模型来构建策略。生成模型是“化学大模型”的核心组成部分，用于分子生成、性质预测等。因此，该论文在方法论上与化学大模型主题相关。

**📖 中文摘要**

本文提出了生成预测控制（GPC），一个学习控制框架。其核心组成部分包括：（i）从专家演示中克隆一个基于扩散的生成策略；（ii）从专家演示和随机探索中训练一个预测性的动作条件世界模型；（iii）合成一个在线规划器，该规划器使用（ii）中的世界模型对未来进行前瞻，从而对（i）中生成的动作提议进行排序和优化。在多种机器人操作任务上，GPC在基于状态和基于视觉的设置中，在仿真和真实世界中都一致地优于行为克隆。该工作的核心是结合了生成模型（扩散策略）和世界模型进行决策，生成模型是构建“化学大模型”的关键技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present generative predictive control (GPC), a learning control framework that (i) clones a generative diffusion-based policy from expert demonstrations, (ii) trains a predictive action-conditioned world model from both expert demonstrations and random explorations, and (iii) synthesizes an online planner that ranks and optimizes the action proposals from (i) by looking ahead into the future using the world model from (ii). Across a variety of robotic manipulation tasks, we demonstrate that GPC consistently outperforms behavior cloning in both state-based and vision-based settings, in simulation and in the real world.

</details>

---

### 82. [Prompt-SID: Learning Structural Representation Prompt via Latent Diffusion for Single-Image Denoising](https://arxiv.org/abs/2502.06432)

**基本信息**

- 🔗 arXiv: [`2502.06432`](https://arxiv.org/abs/2502.06432)
- 👥 作者: Huaqiu Li, Wang Zhang, Xiaowan Hu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.06432.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法深度集成了扩散模型（一种生成模型）来学习结构表示。生成模型（扩散模型）是“化学大模型”的关键技术之一，用于学习化学空间的分布。该工作展示了如何将生成模型学到的表示用于提升下游任务性能，这与化学大模型的应用场景相关。

**📖 中文摘要**

本文提出了Prompt-SID，一个基于提示学习的单图像去噪框架，强调结构细节的保留。该方法通过基于潜在扩散过程的结构表示生成模型来捕获原始尺度图像信息，并将此提示集成到基于Transformer的去噪器中。此外，还引入了尺度回放训练机制。论文在合成、真实世界和荧光成像数据集上进行了综合实验。虽然应用于图像去噪，但其核心创新点——利用扩散模型生成结构表示作为提示，并集成到下游任务模型中——与化学信息学中利用生成模型（如扩散模型）学习分子或光谱的隐表示，并将其作为先验或提示用于下游属性预测、结构解析等任务，在技术路线上有相似之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many studies have concentrated on constructing supervised models utilizing paired datasets for image denoising, which proves to be expensive and time-consuming. Current self-supervised and unsupervised approaches typically rely on blind-spot networks or sub-image pairs sampling, resulting in pixel information loss and destruction of detailed structural information, thereby significantly constraining the efficacy of such methods. In this paper, we introduce Prompt-SID, a prompt-learning-based single image denoising framework that emphasizes preserving of structural details. This approach is trained in a self-supervised manner using downsampled image pairs. It captures original-scale image information through structural encoding and integrates this prompt into the denoiser. To achieve this, we propose a structural representation generation model based on the latent diffusion process and design a structural attention module within the transformer-based denoiser architecture to decode the prompt. Additionally, we introduce a scale replay training mechanism, which effectively mitigates the scale gap from images of different resolutions. We conduct comprehensive experiments on synthetic, real-world, and fluorescence imaging datasets, showcasing the remarkable effectiveness of Prompt-SID. Our code will be released at this https URL .

</details>

---

### 83. [Characterizing Nonlinear Dynamics via Smooth Prototype Equivalences](https://arxiv.org/abs/2503.10336)

**基本信息**

- 🔗 arXiv: [`2503.10336`](https://arxiv.org/abs/2503.10336)
- 👥 作者: Roy Friedman, Noa Moriel, Matthew Ricci 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.10336.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法是利用可逆神经网络（一种生成模型）来学习动力学系统的隐表示和映射。生成模型是“化学大模型”的核心技术。该工作将其应用于动力学系统分析，这与化学中分析分子动力学、反应网络或光谱时序数据有概念上的关联。

**📖 中文摘要**

本文介绍了平滑原型等价（SPE）框架，用于通过可逆神经网络将稀疏观测匹配到原型行为，这些网络模拟平滑的相空间变形。SPE可以通过从原型空间到数据空间的 learned mapping 来定位描述观测动力学长期行为的 invariant sets。此外，SPE可以通过比较变形测量值与原型动力学的数据残差来对动力学状态进行分类。该方法在振荡系统分类方面优于现有技术，并能以无方程方式有效识别极限环和不动点等不变结构。该方法的核心是利用生成模型（可逆神经网络）学习观测数据与原型动力学之间的映射，从而对复杂动力学进行表征和分类。这与化学信息学中利用生成模型学习分子构象空间、反应路径或质谱碎裂模式，并进行分类或预测的任务在方法论上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Characterizing the long term behavior of dynamical systems given limited measurements is a common challenge throughout the physical and biological sciences. This is a challenging task due to the sparsity and noise inherent to empirical observations, as well as the variability of possible long-term dynamics. We address this by introducing smooth prototype equivalences (SPE), a framework for matching sparse observations to prototypical behaviors using invertible neural networks which model smooth phase space deformations. SPE can localize the invariant sets describing long-term behavior of the observed dynamics through the learned mapping from prototype space to data space. Furthermore, SPE can classify dynamical regimes by comparing the data residual of the deformed measurements to prototype dynamics. Our method outperforms existing techniques in the classification of oscillatory systems and can efficiently identify invariant structures like limit cycles and fixed points in an equation-free manner, even when only a small, noisy subset of the phase space is observed. SPE further reveals driving genes in synthetic oscillators such as the repressilator regulatory circuit, and traces cyclic biological processes like the cell cycle trajectory directly from experimental high-dimensional single-cell gene expression data.

</details>

---

### 84. [More Bang for the Buck: Process Reward Modeling with Entropy-Driven Uncertainty](https://arxiv.org/abs/2503.22233)

**基本信息**

- 🔗 arXiv: [`2503.22233`](https://arxiv.org/abs/2503.22233)
- 👥 作者: Lang Cao, Renhong Chen, Yingtian Zou 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.22233.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进针对大语言模型（一种生成模型）推理过程的奖励模型。大语言模型是构建“化学大模型”的重要基础架构之一（如用于化学文献理解、反应预测的LLM）。该工作对提升LLM推理过程质量的研究，间接关联到化学领域对可靠、可解释化学大模型的需求。

**📖 中文摘要**

本文引入了熵驱动不确定性过程奖励模型（EDU-PRM），一种用于过程奖励建模的新型训练框架。它能够对复杂推理步骤进行动态的、不确定性对齐的分割，无需昂贵的手动步骤标注。与之前依赖静态分区和人工标注的过程奖励模型（PRM）不同，EDU-PRM自动将步骤边界锚定在具有高预测熵的标记处，有效捕获内在的逻辑转换，并促进对多样化推理路径的有效探索。在ProcessBench基准测试中，EDU-PRM优于强大的公共PRM基线。该工作的核心是改进对生成模型（大语言模型）推理过程的奖励建模。虽然应用于数学推理，但其“过程奖励建模”的思想与化学信息学中希望大模型不仅给出最终分子或反应，还能给出可信的推理链条（如逆合成分析步骤）的需求相关，属于提升化学大模型可解释性和可靠性的研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Entropy-Driven Uncertainty Process Reward Model (EDU-PRM), a novel entropy-driven training framework for process reward modeling that enables dynamic, uncertainty-aligned segmentation of complex reasoning steps, eliminating the need for costly manual step annotations. Unlike previous Process Reward Models (PRMs) that rely on static partitioning and human labeling, EDU-PRM automatically anchors step boundaries at tokens with high predictive entropy, effectively capturing intrinsic logical transitions and facilitating efficient exploration of diverse reasoning paths. On the ProcessBench benchmark, EDU-PRM outperforms strong public PRM baselines, such as Math-Shepherd PRM and Omega PRM, and EDU-PRM achieves comparable results with SOTA models while only using 1.5% training data. Furthermore, by leveraging our proposed EDU sampling strategy, we observe accuracy boosts from 64.7% to 67.3% for generative reasoning tasks, accompanied by a reduction of 32% in token usage. These findings underscore the potential of EDU-PRM as a scalable and annotation-efficient paradigm for process supervision in mathematical reasoning, paving the way for more efficient and robust approaches to complex mathematical problem solving.

</details>

---

### 85. [Causal Retrieval with Semantic Consideration](https://arxiv.org/abs/2504.04700)

**基本信息**

- 🔗 arXiv: [`2504.04700`](https://arxiv.org/abs/2504.04700)
- 👥 作者: Hyunseo Shin, Wonseok Hwang
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.04700.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发能够理解并检索因果关系的模型。这直接关联到“质谱结构推理”主题，因为质谱解析就是一个基于光谱特征与分子子结构之间因果关系进行推理的过程。一个强大的因果检索模型可以作为质谱结构推理系统的重要组成部分。

**📖 中文摘要**

本文提出了CAWAI，一个在语义和因果关系双重目标下训练的检索模型。现有的检索模型主要关注基于表层语义相似性的文档检索，忽略了因果关系等更深层次的关系结构。CAWAI旨在解决这个问题，使检索系统能够有效支持需要准确捕获因果关系的知识密集型领域（如生物医学、法律）应用。论文在多样的因果检索任务上进行了大量实验，证明了CAWAI的优越性。该工作专注于提升信息检索系统对深层关系（如因果关系）的理解能力。这与“质谱结构推理”任务高度相关，因为从质谱数据推断分子结构本质上是一个基于光谱特征与子结构/碎裂规则之间复杂（常包含因果）关系的推理过程。一个能够更好理解因果关系的检索模型，可以更好地支持基于质谱数据库的结构鉴定。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in large language models (LLMs) have significantly enhanced the performance of conversational AI systems. To extend their capabilities to knowledge-intensive domains such as biomedical and legal fields, where the accuracy is critical, LLMs are often combined with information retrieval (IR) systems to generate responses based on retrieved documents. However, for IR systems to effectively support such applications, they must go beyond simple semantic matching and accurately capture diverse query intents, including causal relationships. Existing IR models primarily focus on retrieving documents based on surface-level semantic similarity, overlooking deeper relational structures such as causality. To address this, we propose CAWAI, a retrieval model that is trained with dual objectives: semantic and causal relations. Our extensive experiments demonstrate that CAWAI outperforms various models on diverse causal retrieval tasks especially under large-scale retrieval settings. We also show that CAWAI exhibits strong zero-shot generalization across scientific domain QA tasks.

</details>

---

### 86. [Structural Inference: Interpreting Small Language Models with Susceptibilities](https://arxiv.org/abs/2504.18274)

**基本信息**

- 🔗 arXiv: [`2504.18274`](https://arxiv.org/abs/2504.18274)
- 👥 作者: Garrett Baker, George Wang, Jesse Hoogland 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.18274.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的主要研究内容“Structural Inference”（结构推理）与“质谱结构推理”在核心方法论和问题本质上高度相关，都是关于从复杂数据中推断底层结构。论文提出的贝叶斯统计力学框架和敏感性分析为结构推理问题提供了新颖的理论视角和计算工具。

**📖 中文摘要**

论文标题为“Structural Inference: Interpreting Small Language Models with Susceptibilities”。该研究为可解释性开发了一个线性响应框架，将神经网络视为贝叶斯统计力学系统。它通过扰动数据分布（例如，将Pile数据集向GitHub或法律文本偏移）来研究网络组件上可观测量的后验期望的一阶变化。由此产生的“敏感性”可以高效估计，并分解为有符号的、每个token的贡献，作为归因分数。这些敏感性被组合成一个响应矩阵，其低秩结构分离了功能模块（如多词头和归纳头）。虽然论文主要关注语言模型的可解释性，但其核心方法论“Structural Inference”（结构推理）与“质谱结构推理”这一主题在概念上高度相关。质谱结构推理的核心任务是从质谱数据中推断出化合物的分子结构，这同样是一个从复杂、高维数据（质谱峰）中推断底层“结构”（分子图）的逆问题。该论文提出的统计力学框架和敏感性分析，为如何从扰动数据中系统性地推断模型内部结构或数据生成结构提供了一种新颖的、可计算的理论视角。因此，该工作可以被视为为核心主题“质谱结构推理”提供了方法论层面的深刻启示和潜在的理论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a linear response framework for interpretability that treats a neural network as a Bayesian statistical mechanical system. A small perturbation of the data distribution, for example shifting the Pile toward GitHub or legal text, induces a first-order change in the posterior expectation of an observable localized on a chosen component of the network. The resulting susceptibility can be estimated efficiently with local SGLD samples and factorizes into signed, per-token contributions that serve as attribution scores. We combine these susceptibilities into a response matrix whose low-rank structure separates functional modules such as multigram and induction heads in a 3M-parameter transformer.

</details>

---

### 87. [From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review](https://arxiv.org/abs/2504.19678)

**基本信息**

- 🔗 arXiv: [`2504.19678`](https://arxiv.org/abs/2504.19678)
- 👥 作者: Mohamed Amine Ferrag, Norbert Tihanyi, Merouane Debbah
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.19678.pdf)

**💡 相关性分析**

满足标准3：综述展望相关。论文是一篇关于自主AI智能体的全面综述，其中明确将“化学推理”列为AI智能体的关键应用领域之一。这为“化学大模型”和“质谱结构推理”在AI智能体框架下的研究和发展提供了重要的背景讨论和未来展望。

**📖 中文摘要**

论文标题为“From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review”。这是一篇关于从大语言模型推理到自主AI智能体的全面综述。论文系统地整合了该领域分散的研究工作，提出了一个统一的框架。它并排比较了2019年至2025年间开发的评估基准，涵盖多个领域。此外，论文提出了一个包含约60个基准的分类法，覆盖通用和学术知识推理、数学问题求解、代码生成和软件工程、事实基础和检索、领域特定评估、多模态和具身任务、任务编排以及交互评估。论文还回顾了2023年至2025年间引入的AI智能体框架，这些框架将大语言模型与模块化工具包集成，以实现自主决策和多步推理。更重要的是，论文展示了自主AI智能体在多个领域的实际应用，其中明确列出了“化学推理”（chemical reasoning）。这表明该综述将化学领域的推理和问题求解视为AI智能体的一个重要应用场景，与“化学大模型”这一主题直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models and autonomous AI agents have evolved rapidly, resulting in a diverse array of evaluation benchmarks, frameworks, and collaboration protocols. Driven by the growing need for standardized evaluation and integration, we systematically consolidate these fragmented efforts into a unified framework. However, the landscape remains fragmented and lacks a unified taxonomy or comprehensive survey. Therefore, we present a side-by-side comparison of benchmarks developed between 2019 and 2025 that evaluate these models and agents across multiple domains. In addition, we propose a taxonomy of approximately 60 benchmarks that cover general and academic knowledge reasoning, mathematical problem-solving, code generation and software engineering, factual grounding and retrieval, domain-specific evaluations, multimodal and embodied tasks, task orchestration, and interactive assessments. Furthermore, we review AI-agent frameworks introduced between 2023 and 2025 that integrate large language models with modular toolkits to enable autonomous decision-making and multi-step reasoning. Moreover, we present real-world applications of autonomous AI agents in materials science, biomedical research, academic ideation, software engineering, synthetic data generation, chemical reasoning, mathematical problem-solving, geographic information systems, multimedia, healthcare, and finance. We then survey key agent-to-agent collaboration protocols, namely the Agent Communication Protocol (ACP), the Model Context Protocol (MCP), and the Agent-to-Agent Protocol (A2A). Finally, we discuss recommendations for future research, focusing on advanced reasoning strategies, failure modes in multi-agent LLM systems, automated scientific discovery, dynamic tool integration via reinforcement learning, integrated search capabilities, and security vulnerabilities in agent protocols.

</details>

---

### 88. [Multi-Domain Audio Question Answering Benchmark Toward Acoustic Content Reasoning](https://arxiv.org/abs/2505.07365)

**基本信息**

- 🔗 arXiv: [`2505.07365`](https://arxiv.org/abs/2505.07365)
- 👥 作者: Chao-Han Huck Yang, Sreyan Ghosh, Qing Wang 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.07365.pdf)

**💡 相关性分析**

满足标准3：综述展望相关。论文虽然聚焦音频，但其核心是构建一个用于评估模型“内容推理”能力的跨领域基准。这为“化学大模型”和“质谱结构推理”领域如何设计类似的、用于评估模型科学推理能力的基准或挑战赛提供了重要的方法论参考和前瞻性讨论。

**📖 中文摘要**

论文标题为“Multi-Domain Audio Question Answering Benchmark Toward Acoustic Content Reasoning”。该论文提出了DCASE 2025挑战赛的任务5：一个跨多个声音理解领域的音频问答（AQA）基准。该任务定义了三个QA子集（生物声学、时间声景和复杂QA），用于测试音频-语言模型在多样化声学场景上的交互式问答能力。论文描述了数据集构成（从海洋哺乳动物叫声到声景和复杂真实世界片段）、评估协议以及基线系统。该挑战赛旨在推动音频语言模型在音频理解和推理能力方面的发展，这对于使AI智能体能够有效感知和与世界交互至关重要。虽然论文主要关注音频领域，但其核心是构建一个用于评估模型“内容推理”能力的基准。这种对“推理”能力的强调和基准构建方法，与“化学大模型”和“质谱结构推理”中需要模型进行复杂科学推理（如从光谱推断结构）的目标在理念上是一致的。它为如何设计和评估面向复杂科学推理任务的模型（例如，质谱问答或结构推理基准）提供了可借鉴的范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Task 5 of the DCASE 2025 Challenge: an Audio Question Answering (AQA) benchmark spanning multiple domains of sound understanding. This task defines three QA subsets (Bioacoustics, Temporal Soundscapes, and Complex QA) to test audio-language models on interactive question-answering over diverse acoustic scenes. We describe the dataset composition (from marine mammal calls to soundscapes and complex real-world clips), the evaluation protocol (top-1 accuracy with answer-shuffling robustness), and baseline systems (Qwen2-Audio-7B, AudioFlamingo 2, Gemini-2-Flash). Preliminary results on the development set are compared, showing strong variation across models and subsets. This challenge aims to advance the audio understanding and reasoning capabilities of audio-language models toward human-level acuity, which are crucial for enabling AI agents to perceive and interact about the world effectively.

</details>

---

### 89. [Flow Matching Meets Biology and Life Science: A Survey](https://arxiv.org/abs/2507.17731)

**基本信息**

- 🔗 arXiv: [`2507.17731`](https://arxiv.org/abs/2507.17731)
- 👥 作者: Zihao Li, Zhichen Zeng, Xiao Lin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.17731.pdf)

**💡 相关性分析**

满足标准3：综述展望相关。论文是专门针对流匹配生成模型在生物学和生命科学（包括化学相关领域如分子设计、蛋白质生成）中应用的综述。这为“化学大模型”的研究，特别是基于新一代生成式AI（如流匹配）的化学模型开发，提供了全面的技术背景、现状总结和未来方向展望。

**📖 中文摘要**

论文标题为“Flow Matching Meets Biology and Life Science: A Survey”。这是一篇关于流匹配（Flow Matching）及其在生物学和生命科学中应用的首个全面综述。论文首先系统回顾了流匹配的基础和变体，然后将其应用分为三个主要领域：生物序列建模、分子生成与设计、以及肽和蛋白质生成。对于每个领域，都提供了深入的近期进展回顾。流匹配是一种强大且高效的生成建模方法，作为扩散模型的替代方案，在分子设计、蛋白质生成等化学和生命科学关键领域显示出巨大潜力。该综述系统地总结了流匹配在这些领域的应用，这与“化学大模型”主题高度相关，因为化学大模型的核心任务之一就是分子生成、性质预测和结构设计。论文中涵盖的“分子生成与设计”以及“肽和蛋白质生成”部分，直接对应了化学信息学和计算化学中的核心问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Over the past decade, advances in generative modeling, such as generative adversarial networks, masked autoencoders, and diffusion models, have significantly transformed biological research and discovery, enabling breakthroughs in molecule design, protein generation, catalysis discovery, drug discovery, and beyond. At the same time, biological applications have served as valuable testbeds for evaluating the capabilities of generative models. Recently, flow matching has emerged as a powerful and efficient alternative to diffusion-based generative modeling, with growing interest in its application to problems in biology and life sciences. This paper presents the first comprehensive survey of recent developments in flow matching and its applications in biological domains. We begin by systematically reviewing the foundations and variants of flow matching, and then categorize its applications into three major areas: biological sequence modeling, molecule generation and design, and peptide and protein generation. For each, we provide an in-depth review of recent progress. We also summarize commonly used datasets and software tools, and conclude with a discussion of potential future directions. The corresponding curated resources are available at this https URL .

</details>

---

### 90. [MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy](https://arxiv.org/abs/2508.05592)

**基本信息**

- 🔗 arXiv: [`2508.05592`](https://arxiv.org/abs/2508.05592)
- 👥 作者: Shaoxiong Zhan, Yanlin Lai, Ziyu Lu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.05592.pdf)

**💡 相关性分析**

满足标准2：数据资源相关。论文提出了一种创新的、基于强化学习的合成高难度训练数据的方法（MathSmith框架）。该方法论和框架本身可以视为一种“工具”或“资源生成方法”，能够被适配和应用于“化学大模型”和“质谱结构推理”领域，以生成用于模型训练和评估的、具有挑战性的合成数据集，从而缓解该领域高质量数据稀缺的问题。

**📖 中文摘要**

论文标题为“MathSmith: Towards Extremely Hard Mathematical Reasoning by Forging Synthetic Problems with a Reinforced Policy”。该论文提出了MathSmith框架，用于合成极具挑战性的数学问题以增强大语言模型的推理能力。其核心方法是从PlanetMath中随机采样概念-解释对，从头开始构建新问题，并使用强化学习联合优化结构有效性、推理复杂性和答案一致性。推理轨迹的长度被用来反映认知复杂性，鼓励创建需要长链思维推理的难题。论文在多个数学推理基准上进行了实验。虽然论文聚焦数学领域，但其核心贡献——一种通过强化学习策略合成高质量、高难度训练数据的方法——对于“化学大模型”和“质谱结构推理”领域具有极高的借鉴价值。化学和质谱推理同样面临高质量、复杂标注数据稀缺的问题。MathSmith提出的从知识源（如化学知识库）采样、结合领域特定约束（如反应规则、光谱-结构关系）、并通过强化学习优化数据质量和难度的范式，可以直接迁移应用于生成用于训练化学推理大模型的合成数据，例如合成复杂的质谱解析问题或化学反应预测问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models have achieved substantial progress in mathematical reasoning, yet their advancement is limited by the scarcity of high-quality, high-difficulty training data. Existing synthesis methods largely rely on transforming human-written templates, limiting both diversity and scalability. We propose MathSmith, a novel framework for synthesizing challenging mathematical problems to enhance LLM reasoning. Rather than modifying existing problems, MathSmith constructs new ones from scratch by randomly sampling concept-explanation pairs from PlanetMath, ensuring data independence and avoiding contamination. To increase difficulty, we design nine predefined strategies as soft constraints during rationales. We further adopts reinforcement learning to jointly optimize structural validity, reasoning complexity, and answer consistency. The length of the reasoning trace generated under autoregressive prompting is used to reflect cognitive complexity, encouraging the creation of more demanding problems aligned with long-chain-of-thought reasoning. Experiments across five benchmarks, categorized as easy & medium (GSM8K, MATH-500) and hard (AIME2024, AIME2025, OlympiadBench), show that MathSmith consistently outperforms existing baselines under both short and long CoT settings. Additionally, a weakness-focused variant generation module enables targeted improvement on specific concepts. Overall, MathSmith exhibits strong scalability, generalization, and transferability, highlighting the promise of high-difficulty synthetic data in advancing LLM reasoning capabilities. Our code and data are available at this https URL .

</details>

---

### 91. [CbLDM: A Diffusion Model for recovering nanostructure from atomic pair distribution function](https://arxiv.org/abs/2509.01370)

**基本信息**

- 🔗 arXiv: [`2509.01370`](https://arxiv.org/abs/2509.01370)
- 👥 作者: Jiarui Cao, Zhiyang Zhang, Heming Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.01370.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种扩散模型（CbLDM），用于从原子对分布函数（PDF）中恢复纳米材料的结构。这直接属于‘质谱结构推理’主题的范畴，即从谱学数据推断化学结构，是化学信息学和计算化学中的核心问题。

**📖 中文摘要**

本研究提出了一种基于条件的潜在扩散模型（CbLDM），用于从原子对分布函数（PDF）中恢复单金属纳米颗粒（MMNPs）的纳米结构。该工作将纳米结构逆问题视为一个高度不适定的条件生成任务。CbLDM通过使用条件先验来估计条件后验分布，从而在潜在扩散模型框架内加速求解。此外，研究使用拉普拉斯矩阵代替距离矩阵来恢复纳米结构，以提高稳定性。实验表明，该模型能够生成与PDF观测结果一致且具有物理意义的纳米结构。这项工作直接针对化学信息学中的一个核心问题——从光谱数据（PDF）推理物质结构，为后续更复杂的逆问题奠定了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The nanostructure inverse problem is an attractive problem that helps researchers to understand the relationship between the properties and the structure of nanomaterials. This study focuses on the problem of recovering the model system of monometallic nanoparticles (MMNPs) from their pair distribution function (PDF) and regards it as a highly ill-posed conditional generation task. This study proposes a Condition-based Latent Diffusion Model (CbLDM) as a feasible solution to this problem. This model demonstrates an acceleration approach within the framework of a latent diffusion model by using conditional priors to estimate the conditional posterior distribution, which is an approximate distribution of p(z|x). In addition, this study uses Laplacian matrix instead of distance matrix to recover the nanostructure, which helps to improve stability. Our study demonstrates that a latent diffusion model with a conditional prior can generate nanostructures that are consistent with PDF observations and physically meaningful, thereby laying the groundwork for subsequent more complex inverse problems.

</details>

---

### 92. [GDR-learners: Orthogonal Learning of Generative Models for Potential Outcomes](https://arxiv.org/abs/2509.22953)

**基本信息**

- 🔗 arXiv: [`2509.22953`](https://arxiv.org/abs/2509.22953)
- 👥 作者: Valentyn Melnychuk, Stefan Feuerriegel
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.22953.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一系列基于深度生成模型（包括扩散模型）的框架，用于从数据中学习并生成潜在结果的分布。这直接与‘化学大模型’主题相关，因为生成模型（如扩散模型、GANs、VAEs）是构建用于分子设计、性质预测和反应推理的化学大模型的核心技术之一。

**📖 中文摘要**

本文提出了一类生成式双重稳健学习器（GDR-learners），用于从观测数据中估计潜在结果的分布。该框架是通用的，可以基于多种最先进的深度生成模型进行实例化，包括条件归一化流（GDR-CNFs）、条件生成对抗网络（GDR-CGANs）、条件变分自编码器（GDR-CVAEs）和条件扩散模型（GDR-CDMs）。与现有方法不同，GDR-learners具有准Oracle效率和速率双重稳健性，因此是渐近最优的。在半合成实验中，GDR-learners在估计潜在结果的条件分布方面优于现有方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Various deep generative models have been proposed to estimate potential outcomes distributions from observational data. However, none of them have the favorable theoretical property of general Neyman-orthogonality and, associated with it, quasi-oracle efficiency and double robustness. In this paper, we introduce a general suite of generative Neyman-orthogonal (doubly-robust) learners that estimate the conditional distributions of potential outcomes. Our proposed generative doubly-robust learners (GDR-learners) are flexible and can be instantiated with many state-of-the-art deep generative models. In particular, we develop GDR-learners based on (a) conditional normalizing flows (which we call GDR-CNFs), (b) conditional generative adversarial networks (GDR-CGANs), (c) conditional variational autoencoders (GDR-CVAEs), and (d) conditional diffusion models (GDR-CDMs). Unlike the existing methods, our GDR-learners possess the properties of quasi-oracle efficiency and rate double robustness, and are thus asymptotically optimal. In a series of (semi-)synthetic experiments, we demonstrate that our GDR-learners are very effective and outperform the existing methods in estimating the conditional distributions of potential outcomes.

</details>

---

### 93. [ExGS: Extreme 3D Gaussian Compression with Diffusion Priors](https://arxiv.org/abs/2509.24758)

**基本信息**

- 🔗 arXiv: [`2509.24758`](https://arxiv.org/abs/2509.24758)
- 👥 作者: Jiaqi Chen, Xinhao Ji, Yuanyuan Gao 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.24758.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法GaussPainter利用了扩散模型的先验知识来恢复和增强3D场景表示。扩散模型是当前生成式AI和‘化学大模型’（用于分子生成、构象采样等）中的关键技术。虽然应用领域是3D视觉，但其核心的扩散模型方法论与构建化学领域大模型的技术栈高度相关。

**📖 中文摘要**

本文提出了ExGS，一个用于极端压缩3D高斯溅射（3DGS）场景的前馈框架。该框架将通用高斯压缩（UGC）与GaussPainter相结合。UGC执行无重新优化的剪枝，以大幅减少高斯基元，而GaussPainter则利用强大的扩散先验，通过掩码引导的细化来从严重剪枝的高斯场景中恢复高质量的渲染结果。与传统的修复不同，GaussPainter不仅填充缺失区域，还增强可见像素，从而显著改善退化的渲染效果。该框架采用轻量级VAE和一步扩散设计，实现实时恢复。实验表明，ExGS可以在实现超过100倍压缩的同时保持保真度，并在具有挑战性的条件下显著提高图像质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural scene representations, such as 3D Gaussian Splatting (3DGS), have enabled high-quality neural rendering; however, their large storage and transmission costs hinder deployment in resource-constrained environments. Existing compression methods either rely on costly optimization, which is slow and scene-specific, or adopt training-free pruning and quantization, which degrade rendering quality under high compression ratios. In contrast, recent data-driven approaches provide a promising direction to overcome this trade-off, enabling efficient compression while preserving high rendering quality. We introduce ExGS, a novel feed-forward framework that unifies Universal Gaussian Compression (UGC) with GaussPainter for Extreme 3DGS compression. UGC performs re-optimization-free pruning to aggressively reduce Gaussian primitives while retaining only essential information, whereas GaussPainter leverages powerful diffusion priors with mask-guided refinement to restore high-quality renderings from heavily pruned Gaussian scenes. Unlike conventional inpainting, GaussPainter not only fills in missing regions but also enhances visible pixels, yielding substantial improvements in degraded renderings. To ensure practicality, it adopts a lightweight VAE and a one-step diffusion design, enabling real-time restoration. Our framework can even achieve over 100X compression (reducing a typical 354.77 MB model to about 3.31 MB) while preserving fidelity and significantly improving image quality under challenging conditions. These results highlight the central role of diffusion priors in bridging the gap between extreme compression and high-quality neural rendering. Our code repository will be released at: this https URL

</details>

---

### 94. [Double projection for reconstructing dynamical systems: between stochastic and deterministic regimes](https://arxiv.org/abs/2510.01089)

**基本信息**

- 🔗 arXiv: [`2510.01089`](https://arxiv.org/abs/2510.01089)
- 👥 作者: Viktor Sip, Martin Breyton, Spase Petkoski 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01089.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于变分自编码器（VAE）框架的生成模型，用于从数据中学习随机动力系统。生成模型（如VAE）是构建‘化学大模型’用于分子表示学习、动力学模拟和不确定性量化的重要基础技术。该方法专注于从时间序列数据中学习生成模型，与化学中从分子动力学轨迹或光谱时间序列学习模型的问题在方法论上相通。

**📖 中文摘要**

本文提出了一种新的双投影方法，用于从观测数据中学习随机动力系统的模型，属于动态变分自编码器（DVAEs）家族。该方法同时估计系统状态轨迹和噪声时间序列。这种设计自然地允许执行多步系统演化，并学习具有相对低维状态空间的模型。该方法在六个基准问题（包括模拟和实验数据）上进行了评估。研究进一步说明了多步方案中教师强制区间对内部动力学性质的影响，并将结果行为与等效架构的确定性模型进行了比较。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning stochastic models of dynamical systems from observed data is of interest in many scientific fields. Here, we propose a new method for this task within the family of dynamical variational autoencoders. The proposed double projection method estimates both the system state trajectories and the noise time series from data. This approach naturally allows us to perform multi-step system evolution and to learn models with a comparatively low-dimensional state space. We evaluate the performance of the method on six benchmark problems, including both simulated and experimental data. We further illustrate the effects of the teacher forcing interval of the multi-step scheme on the nature of the internal dynamics and compare the resulting behavior to that of deterministic models of equivalent architecture.

</details>

---

### 95. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个自主的AI科学家系统（Jr. AI Scientist），该系统能够分析基线工作、提出假设、进行实验并撰写论文。这直接围绕“化学大模型”的主题，即构建能够进行自主科学推理和发现的大型AI模型，是化学信息学智能化研究的前沿方向。

**📖 中文摘要**

这篇论文介绍了Jr. AI Scientist，一个先进的自主AI科学家系统，旨在模拟初级研究人员的核心研究流程。该系统接收人类导师提供的基线论文，分析其局限性，提出改进的新假设，通过严格的实验进行验证，并撰写包含结果的论文。论文的核心是开发一个能够自主进行科学探索的AI系统，这直接涉及构建能够理解和推理复杂科学问题（如化学结构）的“大模型”。虽然论文以NeurIPS、IJCV和ICLR的计算机科学工作为例，但其提出的自主研究框架、假设生成和验证流程，与构建用于“化学大模型”和“质谱结构推理”的自主AI系统的目标高度相关。该系统展示了AI模型如何被用于推动科学发现，这正是化学信息学和质谱分析领域智能化发展的核心方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, validates them through rigorous experimentation, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel algorithms. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven scientific contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from both the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 96. [CRAwDAD: Causal Reasoning Augmentation with Dual-Agent Debate](https://arxiv.org/abs/2511.22854)

**基本信息**

- 🔗 arXiv: [`2511.22854`](https://arxiv.org/abs/2511.22854)
- 👥 作者: Finn G. Vamosi, Nils D. Forkert
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.22854.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于多智能体辩论的因果推理增强框架（CRAwDAD）。虽然应用领域是通用因果推理，但其核心方法——利用大型语言模型进行结构化推理、假设生成和辩论以解决复杂问题——与构建“化学大模型”进行分子性质预测、反应路径推理或“质谱结构推理”中从谱图推断分子结构的逻辑过程在方法论上高度同源。该研究为如何让AI模型进行更可靠、可解释的复杂推理提供了重要思路，这正是化学信息学中模型发展的关键需求。

**📖 中文摘要**

这篇论文提出了CRAwDAD框架，通过双智能体辩论来增强因果推理。该框架让一个智能体提供结构化的因果推断，另一个智能体则批判性地审查其逻辑缺陷。当出现分歧时，智能体试图说服对方，挑战对方的逻辑并修正结论，直到达成共识。论文在CLadder数据集上进行了评估，该数据集将自然语言问题与形式化定义的因果图联系起来，涵盖了Pearl因果阶梯的所有三个层级。研究使用了Qwen3和DeepSeek-R1作为辩论智能体，结果表明多智能体辩论显著提高了模型在因果推理任务上的准确性。这项工作突出了推理模型作为多智能体系统在因果推断中的潜力，并展示了在因果问题解决中多样化视角的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

When people reason about cause and effect, they often consider many competing "what if" scenarios before deciding which explanation fits best. Analogously, advanced language models capable of causal inference can consider multiple interventions and counterfactuals to judge the validity of causal claims. Crucially, this type of reasoning is less like a single calculation and more like an internal dialogue between alternative hypotheses. In this paper, we make this dialogue explicit through a dual-agent debate framework where one model provides a structured causal inference, and the other critically examines this reasoning for logical flaws. When disagreements arise, the agents attempt to persuade each other, challenging each other's logic and revising their conclusions until they converge on a mutually agreed answer. To take advantage of this deliberative process, we specifically use reasoning language models, whose strengths in both causal inference and adversarial debate remain under-explored relative to standard large language models. We evaluate our approach on the CLadder dataset, a benchmark linking natural language questions to formally defined causal graphs across all three rungs of Pearl's ladder of causation. With Qwen3 and DeepSeek-R1 as debater agents, we demonstrate that multi-agent debate improves DeepSeek-R1's overall accuracy in causal inference from 78.03% to 87.45%, with the counterfactual category specifically improving from 67.94% to 80.04% accuracy. Similarly, Qwen3's overall accuracy improves from 84.16% to 89.41%, and counterfactual questions from 71.53% to 80.35%, showing that even strong models can still benefit greatly from debate with weaker agents. Our results highlight the potential of reasoning models as building blocks for multi-agent systems in causal inference, and demonstrate the importance of diverse perspectives in causal problem-solving.

</details>

---

### 97. [Integrating a Causal Foundation Model into a Prescriptive Maintenance Framework for Optimising Production-Line OEE](https://arxiv.org/abs/2512.00969)

**基本信息**

- 🔗 arXiv: [`2512.00969`](https://arxiv.org/abs/2512.00969)
- 👥 作者: Felix Saretzky, Lucas Andersen, Thomas Engel 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00969.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是集成一个“因果基础模型”到决策框架中，用于模拟干预效果和优化结果。这直接涉及“大模型”（此处特指因果基础模型）在复杂系统建模和推理中的应用。虽然应用场景是工业维护，但其核心技术——利用预训练的基础模型进行因果推理和“假设分析”——与化学信息学中利用大模型进行分子设计、性质预测或反应结果推理（可视为对化学系统的干预分析）在方法论上高度相关。

**📖 中文摘要**

这篇论文提出了一种基于因果机器学习（Causal ML）的模型，旨在将制造业中的预测性维护升级为规范性维护。该模型的核心是使用一个预训练的因果基础模型作为“假设”模拟器，来估计潜在维修措施对系统级关键绩效指标（如整体设备效率OEE）的影响。通过估计每种干预措施的因果效应，模型可以为生产线推荐具体的行动方案，帮助识别可能的根本原因并量化其运营影响。论文使用半合成的制造数据对模型进行了评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The transition to prescriptive maintenance (PsM) in manufacturing is critically constrained by a dependence on predictive models. Such purely predictive models tend to capture statistical associations in the data without identifying the underlying causal drivers of failure, which can lead to costly misdiagnoses and ineffective measures. This fundamental limitation results in a key challenge: while we can predict that a failure may occur, we lack a systematic method to understand why a failure occurs. This paper proposes a model based on causal machine learning to bridge this gap. Our objective is to move beyond diagnosis to active prescription by simulating and evaluating potential fixes to optimise KPIs such as Overall Equipment Effectiveness (OEE). For this purpose, a pre-trained causal foundation model is used as a ``what-if'' simulator to estimate the effects of potential fixes. By estimating the causal effect of each intervention on system-level KPIs, specific actions can be recommended for the production line. This can help identify plausible root causes and quantify their operational impact. The model is evaluated using semi-synthetic manufacturing data and compared with non-causal and causal baseline machine learning models. This paper provides a technical basis for a human-centred approach, allowing engineers to test potential solutions in a causal environment to make more effective operational decisions and reduce costly downtimes.

</details>

---

### 98. [SETUP: Sentence-level English-To-Uniform Meaning Representation Parser](https://arxiv.org/abs/2512.07068)

**基本信息**

- 🔗 arXiv: [`2512.07068`](https://arxiv.org/abs/2512.07068)
- 👥 作者: Emma Markle, Javier Gutierrez Bach, Shira Wein
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.07068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发文本到结构化语义表示（UMR图）的解析器。UMR旨在捕获语言的核心含义并适用于多种语言。这项研究属于自然语言处理中“语义解析”或“结构预测”的范畴，是构建能够深度理解文本（包括科学文献、实验描述）的“大模型”的基础能力之一。在化学信息学中，从文献中自动提取化学反应、分子性质等信息需要类似的深度语义理解技术，因此该论文与构建具有高级语言理解能力的化学领域大模型主题相关。

**📖 中文摘要**

这篇论文介绍了SETUP，一个用于英语文本到统一意义表示（UMR）解析的系统。UMR是一种新颖的基于图的语义表示，旨在捕获文本的核心含义，其标注模式具有灵活性，可以标注包括低资源语言在内的世界各种语言。论文提出了两种英语文本到UMR解析的方法：一种是对现有的抽象意义表示（AMR）解析器进行微调，另一种是利用从通用依存关系（UD）转换而来的工具。研究结果表明，SETUP模型在AnCast和SMATCH++指标上取得了显著提升，朝着自动UMR解析迈出了重要一步。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Uniform Meaning Representation (UMR) is a novel graph-based semantic representation which captures the core meaning of a text, with flexibility incorporated into the annotation schema such that the breadth of the world's languages can be annotated (including low-resource languages). While UMR shows promise in enabling language documentation, improving low-resource language technologies, and adding interpretability, the downstream applications of UMR can only be fully explored when text-to-UMR parsers enable the automatic large-scale production of accurate UMR graphs at test time. Prior work on text-to-UMR parsing is limited to date. In this paper, we introduce two methods for English text-to-UMR parsing, one of which fine-tunes existing parsers for Abstract Meaning Representation and the other, which leverages a converter from Universal Dependencies, using prior work as a baseline. Our best-performing model, which we call SETUP, achieves an AnCast score of 84 and a SMATCH++ score of 91, indicating substantial gains towards automatic UMR parsing.

</details>

---

### 99. [SALVE: Sparse Autoencoder-Latent Vector Editing for Mechanistic Control of Neural Networks](https://arxiv.org/abs/2512.15938)

**基本信息**

- 🔗 arXiv: [`2512.15938`](https://arxiv.org/abs/2512.15938)
- 👥 作者: Vegard Flovik
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15938.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕构建可解释、可控制的AI模型框架，其方法论（学习稀疏特征基并进行干预）与“化学大模型”主题中构建可解释、可控的专业领域大模型的研究方向直接相关。

**📖 中文摘要**

本文提出了SALVE（稀疏自编码器-潜在向量编辑）框架，旨在实现深度神经网络的机制可解释性和控制。该框架通过无监督的L1正则化自编码器学习一个稀疏的、模型原生的特征基。这些特征通过Grad-FAM方法进行验证，该方法将潜在特征在输入数据中进行可视化定位。利用自编码器的结构，该框架可以在权重空间进行精确且永久性的干预，从而实现对类定义特征和跨类特征的连续调制。该工作在卷积网络（ResNet-18）和基于Transformer的模型（ViT-B/16）上均得到验证。虽然论文主要关注通用神经网络的可解释性，但其核心方法——学习一个稀疏的、可解释的潜在特征空间，并利用该空间进行模型行为的精确控制——与构建可解释、可控制的“化学大模型”这一主题在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep neural networks achieve impressive performance but remain difficult to interpret and control. We present SALVE (Sparse Autoencoder-Latent Vector Editing), a unified "discover, validate, and control" framework that bridges mechanistic interpretability and model editing. Using an $\ell_1$-regularized autoencoder, we learn a sparse, model-native feature basis without supervision. We validate these features with Grad-FAM, a feature-level saliency mapping method that visually grounds latent features in input data. Leveraging the autoencoder's structure, we perform precise and permanent weight-space interventions, enabling continuous modulation of both class-defining and cross-class features. We further derive a critical suppression threshold, $\alpha_{crit}$, quantifying each class's reliance on its dominant feature, supporting fine-grained robustness diagnostics. Our approach is validated on both convolutional (ResNet-18) and transformer-based (ViT-B/16) models, demonstrating consistent, interpretable control over their behavior. This work contributes a principled methodology for turning feature discovery into actionable model edits, advancing the development of transparent and controllable AI systems.

</details>

---

### 100. [Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills](https://arxiv.org/abs/2512.16301)

**基本信息**

- 🔗 arXiv: [`2512.16301`](https://arxiv.org/abs/2512.16301)
- 👥 作者: Pengcheng Jiang, Jiacheng Lin, Zhiyi Shi 等34人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.16301.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于智能体AI适应性的综述，其中明确包含了对“药物发现”这一化学信息学核心领域的相关讨论和评估实践的总结，与“化学大模型”主题相关。

**📖 中文摘要**

本文是一篇关于智能体AI适应性的综述，系统性地回顾了大型语言模型（LLM）智能体在预训练之后的改进方法。文章提出了一个涵盖智能体适应和工具适应的四范式框架，并回顾了后训练方法、自适应记忆架构和智能体技能。综述还比较了这些方法在成本、灵活性和泛化性方面的权衡，并总结了在深度研究、软件开发、计算机使用和药物发现等领域的评估实践。文章明确指出其综述范围包括“药物发现”领域，这是化学信息学的核心应用场景之一。因此，这篇综述对理解如何通过后训练、记忆和技能库来适应和提升在科学发现（如化学、药物研发）中使用的LLM智能体具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) agents are moving beyond prompting alone. ChatGPT marked the rise of general-purpose LLM assistants, DeepSeek showed that on-policy reinforcement learning with verifiable rewards can improve reasoning and tool use, and OpenClaw highlights a newer direction in which agents accumulate persistent memory and reusable skills. Yet the research landscape remains fragmented across post-training, retrieval, memory, and skill systems. This survey studies these developments under a single notion of \emph{adaptation}: improving an agent, its tools, or their interaction after pretraining. We organize the field with a four-paradigm framework spanning agent adaptation and tool adaptation. On the agent side, A1 (tool-execution-signaled) and A2 (agent-output-signaled) improve the agent itself through supervised fine-tuning, preference optimization, and reinforcement learning with verifiable rewards. On the tool side, T1 (agent-agnostic) provides reusable pre-trained modules any agent can call, while T2 (agent-supervised) uses the agent's outputs to train memory systems, skill libraries, or lightweight subagents. Using this framework, we review post-training methods, adaptive memory architectures, and agent skills; compare their trade-offs in cost, flexibility, and generalization; and summarize evaluation practices across deep research, software development, computer use, and drug discovery. We conclude by outlining open problems in agent-tool co-adaptation, continual learning, safety, and efficient deployment.

</details>

---

### 101. [Thermodynamics a la Souriau on Kähler Non Compact Symmetric Spaces for Cartan Neural Networks](https://arxiv.org/abs/2512.16772)

**基本信息**

- 🔗 arXiv: [`2512.16772`](https://arxiv.org/abs/2512.16772)
- 👥 作者: Pietro G. Fré, Alexander S. Sorin, Mario Trigiante
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.16772.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将广义热力学的几何框架与一种新型神经网络（Cartan神经网络）的数学模型相结合，这属于为科学领域（如化学）大模型构建数学和物理基础的理论研究，与“化学大模型”主题相关。

**📖 中文摘要**

本文探讨了在非紧致对称空间上，基于Souriau方法的广义热力学的几何表述，并将其与新型Cartan神经网络中隐藏层的数学模型联系起来。论文的主要结果是证明了只有在Kähler对称空间上才支持吉布斯概率分布，并解决了确定分区函数收敛的温度空间（即李代数元素集合）问题。作者进一步声称，Rao、Chentsov、Amari的信息几何与Ruppeiner和Lychagin的热力学几何是同一事物。本文所建立的框架提供的吉布斯概率分布具有在完整对称群作用下的协变性。虽然论文高度理论化且涉及微分几何，但其明确将抽象的几何热力学框架与一种新型神经网络（Cartan神经网络）的隐藏层建模联系起来。这种为神经网络建立严格数学和物理基础的工作，属于“化学大模型”或更广义的“科学大模型”底层理论探索的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we clarify several issues concerning the abstract geometrical formulation of thermodynamics on non compact symmetric spaces $\mathrm{U/H}$ that are the mathematical model of hidden layers in the new paradigm of Cartan Neural Networks. We introduce a distinction between the generalized thermodynamics associated with Dynamical Systems and the challenging proposal of Gibbs probability distributions on $\mathrm{U/H}$ provided by generalized thermodynamics {à} la Souriau. Main result is the proof that $\mathrm{U/H}$.s supporting Gibbs distributions are only the Kähler ones. For the latter, we solve the problem of determining the space of temperatures, namely of Lie algebra elements for which the partition function converges. The space of generalized temperatures is the orbit under the adjoint action of $\mathrm{U}$ of a positivity domain in the Cartan subalgebra $C_c\subset\mathbb{H}$ of the maximal compact subalgebra $\mathbb{H}\subset\mathbb{U}$. We illustrate how our explicit constructions for the Poincaré and Siegel planes might be extended to the whole class of Calabi-Vesentini manifolds utilizing Paint Group symmetry. Furthermore we claim that Rao's, Chentsov's, Amari's Information Geometry and the thermodynamical geometry of Ruppeiner and Lychagin are the very same thing. The most important property of the Gibbs probability distributions provided by the here introduced setup is their covariance with respect to the action of the full group of symmetries $\mathrm{U}$. The partition function is invariant against $\mathrm{U}$ transformations and the set of its arguments, namely the generalized temperatures, can be always reduced to a minimal set whose cardinality is equal to the rank of the compact denominator group $\mathrm{H}\subset \mathrm{U}$.

</details>

---

### 102. [RedSage: A Cybersecurity Generalist LLM](https://arxiv.org/abs/2601.22159)

**基本信息**

- 🔗 arXiv: [`2601.22159`](https://arxiv.org/abs/2601.22159)
- 👥 作者: Naufal Suryanto, Muzammal Naseer, Pengfei Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22159.pdf)

**💡 相关性分析**

满足标准2和3：论文提供了构建领域专家大模型（RedSage）的完整方法论、数据集生成流程和评估基准，可作为构建“化学大模型”或“质谱分析大模型”的重要参考资源（标准2）。同时，论文也包含了对领域大模型训练和评估方法的讨论，具有综述和展望性质（标准3）。

**📖 中文摘要**

本文提出了RedSage，一个开源、可本地部署的网络安全专家大语言模型。为了训练该模型，作者策划了118亿标记的网络安全领域持续预训练数据，并通过模拟专家工作流程生成了26.6万轮多轮对话样本用于监督微调。为了评估模型，作者引入了RedSage-Bench基准，包含3万道多项选择题和240道开放式问答题，涵盖网络安全知识、技能和工具专业知识。RedSage还在现有的网络安全基准（如CTI-Bench, CyberMetric, SECURE）和通用LLM基准上进行了评估。在8B规模上，RedSage在网络安全基准和通用任务上均显著超越基线模型。这项工作展示了通过领域感知的智能体增强和预训练/后训练，不仅可以增强特定领域的专业知识，还能提高通用推理和指令遵循能力。虽然领域是网络安全，但其方法论——大规模收集领域数据、通过模拟工作流生成高质量指令数据、进行领域适应训练和全面评估——为构建“化学大模型”或“质谱分析大模型”提供了完整、可借鉴的技术路线图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cybersecurity operations demand assistant LLMs that support diverse workflows without exposing sensitive data. Existing solutions either rely on proprietary APIs with privacy risks or on open models lacking domain adaptation. To bridge this gap, we curate 11.8B tokens of cybersecurity-focused continual pretraining data via large-scale web filtering and manual collection of high-quality resources, spanning 28.6K documents across frameworks, offensive techniques, and security tools. Building on this, we design an agentic augmentation pipeline that simulates expert workflows to generate 266K multi-turn cybersecurity samples for supervised fine-tuning. Combined with general open-source LLM data, these resources enable the training of RedSage, an open-source, locally deployable cybersecurity assistant with domain-aware pretraining and post-training. To rigorously evaluate the models, we introduce RedSage-Bench, a benchmark with 30K multiple-choice and 240 open-ended Q&A items covering cybersecurity knowledge, skills, and tool expertise. RedSage is further evaluated on established cybersecurity benchmarks (e.g., CTI-Bench, CyberMetric, SECURE) and general LLM benchmarks to assess broader generalization. At the 8B scale, RedSage achieves consistently better results, surpassing the baseline models by up to +5.59 points on cybersecurity benchmarks and +5.05 points on Open LLM Leaderboard tasks. These findings demonstrate that domain-aware agentic augmentation and pre/post-training can not only enhance cybersecurity-specific expertise but also help to improve general reasoning and instruction-following. All models, datasets, and code are publicly available.

</details>

---

### 103. [Extracting Recurring Vulnerabilities from Black-Box LLM-Generated Software](https://arxiv.org/abs/2602.04894)

**基本信息**

- 🔗 arXiv: [`2602.04894`](https://arxiv.org/abs/2602.04894)
- 👥 作者: Tomer Kordonsky, Maayan Yamin, Noam Benzimra 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.04894.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和量化LLM在代码生成任务中产生可预测错误（漏洞）模式的能力。这种对LLM输出系统性错误的分析方法，与评估“化学大模型”或“质谱结构推理”模型输出可靠性和可重复性的研究主题在方法论上直接相关。

**📖 中文摘要**

本文研究了LLM生成代码中反复出现的漏洞模式，并引入了特征-安全表（FSTab）框架。FSTab包含两个组件：首先，它支持一种黑盒攻击，仅通过观察前端特征和了解源LLM的知识，就能预测后端可能存在的漏洞，而无需访问后端或源代码。其次，它提供了一个以模型为中心的评估，量化模型在不同程序、语义保留的重述和应用领域中重复相同漏洞的一致性。作者在包括GPT-5.2、Claude-4.5 Opus和Gemini-3 Pro在内的先进代码LLM上进行了评估。结果表明，即使目标领域被排除在训练之外，FSTab也能实现高达94%的攻击成功率和93%的漏洞覆盖率。这项研究揭示了LLM生成软件中一个未被充分探索的攻击面。虽然主要关注代码安全，但其核心方法——分析LLM输出中的可预测模式（在这里是漏洞），与“化学大模型”或“质谱分析大模型”输出结果的可预测性、可靠性分析在方法论上相通。对于旨在生成可靠化学结构或质谱解析结果的大模型，评估其输出中的系统性错误模式至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLMs are increasingly used for code generation, but their outputs often follow recurring templates that can induce predictable vulnerabilities. We study vulnerability persistence in LLM-generated software and introduce Feature--Security Table (FSTab) with two components. First, FSTab enables a black-box attack that predicts likely backend vulnerabilities from observable frontend features and knowledge of the source LLM, without access to the backend or source code. Second, FSTab provides a model-centric evaluation that quantifies how consistently a model reproduces the same vulnerabilities across programs, semantics-preserving rephrasings, and application domains. We evaluate FSTab on state-of-the-art code LLMs, including GPT-5.2, Claude-4.5 Opus, and Gemini-3 Pro, across diverse application domains. Our results show strong cross-domain transfer: even when the target domain is excluded from training, FSTab achieves up to 94% attack success and 93% vulnerability coverage on Internal Tools (Claude-4.5 Opus). These findings expose an underexplored attack surface in LLM-generated software and highlight the security risks of code generation. Our code is available at this https URL

</details>

---

### 104. [Semantic Search over 9 Million Mathematical Theorems](https://arxiv.org/abs/2602.05216)

**基本信息**

- 🔗 arXiv: [`2602.05216`](https://arxiv.org/abs/2602.05216)
- 👥 作者: Luke Alexander, Eric Leonen, Sophie Szeto 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.05216.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了目前最大的公开数学定理语料库（920万条），并提供了有效的语义检索方法。这为“化学大模型”主题中构建类似的大规模、结构化化学领域数据集（如化合物、反应、质谱数据）以及开发领域语义检索工具提供了重要的数据资源和方法参考。

**📖 中文摘要**

本文介绍并研究了在统一语料库上进行大规模数学定理语义检索。该语料库包含从arXiv和其他七个来源提取的920万个定理陈述，是最大的公开可用的人类撰写的研究级定理语料库。作者将每个定理用简短的自然语言描述表示为检索表示，并系统分析了表示上下文、语言模型选择、嵌入模型和提示策略如何影响检索质量。在一个由专业数学家编写的定理搜索查询评估集上，该方法在定理级和论文级检索上都显著优于现有基线，证明了语义定理搜索在网络规模上是可行且有效的。虽然领域是数学，但其核心贡献——构建大规模、高质量的科学领域（数学定理）结构化语料库，并开发有效的语义检索方法——与“化学信息学”中构建化学知识库（如反应、性质、谱图）并实现高效检索的需求高度一致。这项工作为构建“化学大模型”所需的数据基础设施（即大规模、结构化的化学知识数据集）和检索增强生成（RAG）中的检索组件提供了直接参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Searching for mathematical results remains difficult: most existing tools retrieve entire papers, while mathematicians and theorem-proving agents often seek a specific theorem, lemma, or proposition that answers a query. While semantic search has seen rapid progress, its behavior on large, highly technical corpora such as research-level mathematical theorems remains poorly understood. In this work, we introduce and study semantic theorem retrieval at scale over a unified corpus of $9.2$ million theorem statements extracted from arXiv and seven other sources, representing the largest publicly available corpus of human-authored, research-level theorems. We represent each theorem with a short natural-language description as a retrieval representation and systematically analyze how representation context, language model choice, embedding model, and prompting strategy affect retrieval quality. On a curated evaluation set of theorem-search queries written by professional mathematicians, our approach substantially improves both theorem-level and paper-level retrieval compared to existing baselines, demonstrating that semantic theorem search is feasible and effective at web scale. The project page, search tool, dataset, REST API, and MCP server are available at this http URL .

</details>

---

### 105. [LLM4PQC - Accurate and Efficient Synthesis of PQC Cores by Feedback-Driven LLMs](https://arxiv.org/abs/2602.09919)

**基本信息**

- 🔗 arXiv: [`2602.09919`](https://arxiv.org/abs/2602.09919)
- 👥 作者: Buddhi Perera, Zeng Wang, Weihua Xiao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.09919.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个LLM驱动的框架，用于自动化特定领域（后量子密码学）的代码生成和转换任务。这种将LLM作为领域专家工具，结合领域知识实现工作流自动化的范式，与利用“化学大模型”自动化化学信息学或质谱分析中的计算任务（如模拟、数据分析、流程编排）的研究主题直接相关。

**📖 中文摘要**

本文提出了LLM4PQC，一个基于LLM的框架，用于将后量子密码学（PQC）的高级规范和参考C代码重构为可供高层次综合（HLS）使用的、可综合的C代码。该框架生成并验证生成的RTL代码。为了确保正确性，它利用了一个分层的检查机制，涵盖快速的C编译和模拟以及RTL模拟。在NIST PQC参考设计上的案例研究表明，与传统流程相比，该方法减少了人工工作量并加速了设计空间探索。虽然应用领域是硬件设计，但该论文的核心贡献是展示了一个利用反馈驱动和智能体集成的LLM框架，来自动化地将领域特定（此处为密码学）的参考代码和规范转换为可执行的、可验证的硬件描述。这种方法论——使用LLM作为领域专家助手，结合领域知识（如PQC算法）和严格的验证流程来自动化复杂的设计任务——完全可以迁移到“化学信息学”和“质谱分析”领域。例如，利用LLM将化学模拟的算法描述或质谱数据处理流程自动转换为可执行代码或工作流。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The design of post-quantum cryptography (PQC) hardware is a complex and hierarchical process with many challenges. A primary bottleneck is the conversion of PQC reference codes from C to high-level synthesis (HLS) specifications, which requires extensive manual refactoring. Another bottleneck is the scalability of synthesis for complex PQC primitives, including number theoretic transform (NTT) accelerators and wide memory interfaces. While large language models (LLMs) have shown remarkable results for coding in general-purpose languages like Python, coding for hardware design is more challenging; feedback-driven and agentic integration are key principles of successful state-of-the-art approaches. Here, we propose LLM4PQC, an LLM-based framework that refactors high-level PQC specifications and reference C codes into HLS-ready and synthesizable C code. Our framework generates and verifies the resulting RTL code. For correctness, we leverage a hierarchy of checks, covering fast C compilation and simulation as well as RTL simulation. Case studies on NIST PQC reference designs demonstrate a reduction in manual effort and accelerated design-space exploration compared to traditional flows. Overall, LLM4PQC provides a powerful and efficient pathway for synthesizing complex hardware accelerators.

</details>

---

### 106. [Benchmarking GNN Models on Molecular Regression Tasks with CKA-Based Representation Analysis](https://arxiv.org/abs/2602.20573)

**基本信息**

- 🔗 arXiv: [`2602.20573`](https://arxiv.org/abs/2602.20573)
- 👥 作者: Rajan, Ishaan Gupta
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.20573.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用图神经网络（GNN）进行分子属性预测和表示分析，这是化学信息学和构建化学领域大模型（用于分子表示）的关键组成部分。

**📖 中文摘要**

本文系统性地对四种不同的图神经网络（GNN）架构在分子回归任务上进行了基准测试，涵盖了物理化学、生物和分析化学等多个领域的数据集。研究重点在于评估GNN在分子属性预测任务中的表现，并探讨了不同架构的归纳偏置。此外，作者还实现了一种分层融合（GNN+分子指纹）框架，该框架在目标预测任务中表现优于或匹配独立的GNN模型。论文进一步使用中心核对齐（CKA）分析了GNN嵌入与分子指纹嵌入之间的表示相似性，发现它们占据高度独立的潜在空间。这项工作直接涉及使用图神经网络进行分子表示学习，这是化学信息学和化学大模型（用于分子性质预测）的核心技术之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecules are commonly represented as SMILES strings, which can be readily converted to fixed-size molecular fingerprints. These fingerprints serve as feature vectors to train ML/DL models for molecular property prediction tasks in the field of computational chemistry, drug discovery, biochemistry, and materials science. Recent research has demonstrated that SMILES can be used to construct molecular graphs where atoms are nodes ($V$) and bonds are edges ($E$). These graphs can subsequently be used to train geometric DL models like GNN. GNN learns the inherent structural relationships within a molecule rather than depending on fixed-size fingerprints. Although GNN are powerful aggregators, their efficacy on smaller datasets and inductive biases across different architectures is less studied. In our present study, we performed a systematic benchmarking of four different GNN architectures across a diverse domain of datasets (physical chemistry, biological, and analytical). Additionally, we have also implemented a hierarchical fusion (GNN+FP) framework for target prediction. We observed that the fusion framework consistently outperforms or matches the performance of standalone GNN (RMSE improvement > $7\%$) and baseline models. Further, we investigated the representational similarity using centered kernel alignment (CKA) between GNN and fingerprint embeddings and found that they occupy highly independent latent spaces (CKA $\le0.46$). The cross-architectural CKA score suggests a high convergence between isotopic models like GCN, GraphSAGE and GIN (CKA $\geq0.88$), with GAT learning moderately independent representation (CKA $0.55-0.80$).

</details>

---

### 107. [On Sample-Efficient Generalized Planning via Learned Transition Models](https://arxiv.org/abs/2602.23148)

**基本信息**

- 🔗 arXiv: [`2602.23148`](https://arxiv.org/abs/2602.23148)
- 👥 作者: Nitin Gupta, Vishal Pallagani, John A. Aydin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.23148.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是学习世界模型（转移模型）以实现高效的规划，这与构建能够进行复杂推理和规划的大模型（包括可能应用于科学发现的模型）的主题在方法论上高度相关。

**📖 中文摘要**

本文研究如何通过学习的转移模型来提高广义规划的样本效率。作者将广义规划表述为一个转移模型学习问题，其中神经模型显式地近似状态转移函数，并通过展开符号状态轨迹来生成计划。与直接预测动作序列的Transformer方法不同，该方法通过自回归预测中间世界状态来学习领域动态作为一个隐式的世界模型。研究评估了多种状态表示和神经架构（包括关系图编码），结果表明学习显式转移模型在多个领域中比直接动作序列预测具有更高的样本效率和更好的分布外泛化能力。这项工作涉及学习世界模型以进行规划，其方法论（学习状态转移）与构建能够进行推理和规划的化学或科学大模型在理念上相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generalized planning studies the construction of solution strategies that generalize across families of planning problems sharing a common domain model, formally defined by a transition function $\gamma : S \times A \rightarrow S$. Classical approaches achieve such generalization through symbolic abstractions and explicit reasoning over $\gamma$. In contrast, recent Transformer-based planners, such as PlanGPT and Plansformer, largely cast generalized planning as direct action-sequence prediction, bypassing explicit transition modeling. While effective on in-distribution instances, these approaches typically require large datasets and model sizes, and often suffer from state drift in long-horizon settings due to the absence of explicit world-state evolution. In this work, we formulate generalized planning as a transition-model learning problem, in which a neural model explicitly approximates the successor-state function $\hat{\gamma} \approx \gamma$ and generates plans by rolling out symbolic state trajectories. Instead of predicting actions directly, the model autoregressively predicts intermediate world states, thereby learning the domain dynamics as an implicit world model. To study size-invariant generalization and sample efficiency, we systematically evaluate multiple state representations and neural architectures, including relational graph encodings. Our results show that learning explicit transition models yields higher out-of-distribution satisficing-plan success than direct action-sequence prediction in multiple domains, while achieving these gains with significantly fewer training instances and smaller models. This is an extended version of a short paper accepted at ICAPS 2026 under the same title.

</details>

---

### 108. [Embedding interpretable $\ell_1$-regression into neural networks for uncovering temporal structure in cell imaging](https://arxiv.org/abs/2603.02899)

**基本信息**

- 🔗 arXiv: [`2603.02899`](https://arxiv.org/abs/2603.02899)
- 👥 作者: Fabian Kabus, Maren Hackenberg, Julia Hindel 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02899.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将可解释的稀疏回归模型嵌入神经网络，用于从科学数据（细胞成像）中学习动态结构。这种方法论对于构建可解释的、能够处理复杂科学数据（如质谱或化学数据）的大模型具有直接相关性。

**📖 中文摘要**

本文提出了一种将可解释的ℓ1回归嵌入到神经网络中的方法，旨在从细胞成像数据中揭示时间动态结构。具体而言，作者将向量自回归（VAR）模型作为可解释的回归技术嵌入到卷积自编码器中，自编码器负责降维，而ℓ1正则化的VAR模型则负责提取稀疏的自回归动态。通过跳过连接分别处理非稀疏的静态空间信息，将有选择地将稀疏结构引导至ℓ1正则化的VAR部分。该方法使得能够通过分段线性解路径进行ℓ1回归参数估计。这项工作展示了如何将经典的、可解释的统计模型（如稀疏VAR）与深度学习架构相结合，以从复杂的生物数据中提取有意义的动态模式。这种结合可解释性与表示学习的方法对于构建能够理解复杂系统动态的科学大模型具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While artificial neural networks excel in unsupervised learning of non-sparse structure, classical statistical regression techniques offer better interpretability, in particular when sparseness is enforced by $\ell_1$ regularization, enabling identification of which factors drive observed dynamics. We investigate how these two types of approaches can be optimally combined, exemplarily considering two-photon calcium imaging data where sparse autoregressive dynamics are to be extracted. We propose embedding a vector autoregressive (VAR) model as an interpretable regression technique into a convolutional autoencoder, which provides dimension reduction for tractable temporal modeling. A skip connection separately addresses non-sparse static spatial information, selectively channeling sparse structure into the $\ell_1$-regularized VAR. $\ell_1$-estimation of regression parameters is enabled by differentiating through the piecewise linear solution path. This is contrasted with approaches where the autoencoder does not adapt to the VAR model. Having an embedded statistical model also enables a testing approach for comparing temporal sequences from the same observational unit. Additionally, contribution maps visualize which spatial regions drive the learned dynamics.

</details>

---

### 109. [Information Routing in Atomistic Foundation Models: How Task Alignment and Equivariance Shape Linear Disentanglement](https://arxiv.org/abs/2603.03155)

**基本信息**

- 🔗 arXiv: [`2603.03155`](https://arxiv.org/abs/2603.03155)
- 👥 作者: Joshua Steier
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03155.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学大模型（原子级基础模型）的表示学习展开，探讨了模型如何组织几何和组成信息，这与“化学大模型”主题高度相关。

**📖 中文摘要**

本文研究了分子性质预测模型如何组织其表示，以便几何信息和组成信息能够被清晰地分离。作者引入了组成性探针分解（CPD）方法，通过线性投影去除组成信号，并测量剩余表示中几何信息的可访问性。研究在QM9数据集上评估了来自五个架构家族的十个模型，发现模型在去除组成信息后，其几何信息的可访问性存在显著差异（R²_geom从0.081到0.533）。关键影响因素包括任务对齐（例如，在HOMO-LUMO能隙上训练的模型表现优于在能量上训练的模型）、数据多样性以及表示内部的信息路由方式（例如，在MACE模型中，不同对称类型的通道优先编码不同的分子属性）。这项研究直接关联到化学大模型（特别是原子级基础模型）的表示学习，探讨了模型架构和训练目标如何影响其学习到的化学信息的结构化分离，这对于理解和设计用于分子性质预测和结构推理的化学AI模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

What determines whether a molecular property prediction model organizes its representations so that geometric and compositional information can be cleanly separated? We introduce Compositional Probe Decomposition (CPD), which linearly projects out composition signal and measures how much geometric information remains accessible to a Ridge probe. We validate CPD with four independent checks, including a structural isomer benchmark where compositional projections score at chance while geometric residuals reach 94.6\% pairwise classification accuracy. Across ten models from five architectural families on QM9, we find a \emph{linear accessibility gradient}: models differ by $6.6\times$ in geometric information accessible after composition removal ($R^2_{\mathrm{geom}}$ from 0.081 to 0.533 for HOMO-LUMO gap). Three factors explain this gradient. Task alignment dominates: models trained on HOMO-LUMO gap ($R^2_{\mathrm{geom}}$ 0.44--0.53) outscore energy-trained models by $\sim$0.25 $R^2$ regardless of architecture. Within-architecture ablations on two independent architectures confirm this: PaiNN drops from 0.53 to 0.31 when retrained on energy, and MACE drops from 0.44 to 0.08. Data diversity partially compensates for misaligned objectives, with MACE pretrained on MPTraj (0.36) outperforming QM9-only energy models. Inside MACE's representations, information routes by symmetry type: $L{=}1$ (vector) channels preferentially encode dipole moment ($R^2 = 0.59$ vs.\ 0.38 in $L{=}0$), while $L{=}0$ (scalar) channels encode HOMO-LUMO gap ($R^2 = 0.76$ vs.\ 0.34 in $L{=}1$). This pattern is absent in ViSNet. We also show that nonlinear probes produce misleading results on residualized representations, recovering $R^2 = 0.68$--$0.95$ on a purely compositional target, and recommend linear probes for this setting.

</details>

---

### 110. [Representing local protein environments with machine learning force fields](https://arxiv.org/abs/2505.23354)

**基本信息**

- 🔗 arXiv: [`2505.23354`](https://arxiv.org/abs/2505.23354)
- 👥 作者: Meital Bojan, Sanketh Vedula, Advaith Maddipatla 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.23354.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发和应用原子级基础模型（AFMs）来表征局部蛋白质环境，这属于“化学大模型”在生物分子领域的应用。

**📖 中文摘要**

本文提出了一种基于原子级基础模型（AFMs）中间特征的新型局部蛋白质环境表示方法。作者证明，这种嵌入能有效捕捉局部结构（如二级基序）和化学特征（如氨基酸身份和质子化状态）。AFM衍生的表示空间展现出有意义的结构，使得构建基于数据的生物分子环境分布先验成为可能。在生物分子核磁共振光谱学的背景下，该表示实现了首个物理信息化的化学位移预测器，并达到了最先进的精度。该工作展示了原子级基础模型及其涌现表示在传统分子模拟之外的蛋白质建模中的有效性，为构建蛋白质环境的功能性表示开辟了新途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The local structure of a protein strongly impacts its function and interactions with other molecules. Therefore, a concise, informative representation of a local protein environment is essential for modeling and designing proteins and biomolecular interactions. However, these environments' extensive structural and chemical variability makes them challenging to model, and such representations remain under-explored. In this work, we propose a novel representation for a local protein environment derived from the intermediate features of atomistic foundation models (AFMs). We demonstrate that this embedding effectively captures both local structure (e.g., secondary motifs), and chemical features (e.g., amino-acid identity and protonation state). We further show that the AFM-derived representation space exhibits meaningful structure, enabling the construction of data-driven priors over the distribution of biomolecular environments. Finally, in the context of biomolecular NMR spectroscopy, we demonstrate that the proposed representations enable a first-of-its-kind physics-informed chemical shift predictor that achieves state-of-the-art accuracy. Our results demonstrate the surprising effectiveness of atomistic foundation models and their emergent representations for protein modeling beyond traditional molecular simulations. We believe this will open new lines of work in constructing effective functional representations for protein environments.

</details>

---

### 111. [RadDiff: Retrieval-Augmented Denoising Diffusion for Protein Inverse Folding](https://arxiv.org/abs/2512.00126)

**基本信息**

- 🔗 arXiv: [`2512.00126`](https://arxiv.org/abs/2512.00126)
- 👥 作者: Jin Han, Tianfan Fu, Wu-Jun Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.00126.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合检索增强和扩散模型的化学大模型（RadDiff），用于解决蛋白质逆折叠这一核心化学信息学问题。

**📖 中文摘要**

本文提出了RadDiff，一种用于蛋白质逆折叠（根据目标蛋白质结构设计氨基酸序列）的新方法。RadDiff结合了检索增强机制和知识感知扩散模型。检索机制旨在捕获最新的蛋白质知识，而扩散模型则通过一个轻量级模块将这些知识整合到生成过程中。在CATH、TS50和PDB2022数据集上的实验表明，RadDiff consistently优于现有方法，序列恢复率提升高达19%。该方法能生成高度可折叠的序列，并能随数据库规模有效扩展。这项工作将扩散模型和外部知识检索应用于蛋白质序列设计，是化学大模型在蛋白质工程领域的一个重要进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein inverse folding, the design of an amino acid sequence based on a target protein structure, is a fundamental problem of computational protein engineering. Existing methods either generate sequences without leveraging external knowledge or relying on protein language models~(PLMs). The former omits the knowledge stored in natural protein data, while the latter is parameter-inefficient and inflexible to adapt to ever-growing protein data. To overcome the above drawbacks, in this paper we propose a novel method, called $\underline{\text{r}}$etrieval-$\underline{\text{a}}$ugmented $\underline{\text{d}}$enoising $\underline{\text{diff}}$usion~($\mbox{RadDiff}$), for protein inverse folding. In RadDiff, a novel retrieval-augmentation mechanism is designed to capture the up-to-date protein knowledge. We further design a knowledge-aware diffusion model that integrates this protein knowledge into the diffusion process via a lightweight module. Experimental results on the CATH, TS50, and PDB2022 datasets show that $\mbox{RadDiff}$ consistently outperforms existing methods, improving sequence recovery rate by up to 19\%. Experimental results also demonstrate that RadDiff generates highly foldable sequences and scales effectively with database size.

</details>

---

## 📊 数据统计
- 累计运行天数：22
- 累计论文数量：1661

## 📝 历史记录

> 暂无历史数据

