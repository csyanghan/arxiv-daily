# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-16 01:29:20

## 📅 2026-03-16 (今日最新)

**相关论文数：53**

### 1. [Graph Tokenization for Bridging Graphs and Transformers](https://arxiv.org/abs/2603.11099)

**基本信息**

- 🔗 arXiv: [`2603.11099`](https://arxiv.org/abs/2603.11099)
- 👥 作者: Zeyuan Guo, Enmao Diao, Cheng Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11099.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何将图结构数据适配到Transformer大模型框架中，提出了一种通用的图标记化方法。这直接与“化学大模型”主题相关，因为化学分子通常表示为图，该方法为构建能够处理分子图等复杂结构数据的化学大模型提供了关键技术思路。

**📖 中文摘要**

本文提出了一种图标记化框架，旨在弥合图结构数据与Transformer序列模型之间的鸿沟。该框架结合了可逆的图序列化方法和在大语言模型中广泛采用的字节对编码（BPE）标记器，将图转换为序列表示。通过利用图子结构的全局统计信息来指导序列化过程，确保频繁出现的子结构在序列中更常见，从而能被BPE合并为有意义的标记。实验表明，该标记器使得BERT等Transformer模型无需架构修改即可直接应用于图基准测试，并在14个基准数据集上取得了最先进的结果，经常优于图神经网络和专门的图Transformer。这项工作为将图数据整合到序列模型生态系统中提供了桥梁，与“化学大模型”主题相关，因为它展示了如何将复杂的结构化数据（如图）适配到基于Transformer的大模型框架中，这种通用方法对处理化学分子图等结构化数据具有潜在启发意义。

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

满足标准1：论文的核心研究内容是将机器学习（特别是深度学习）与热力学相平衡计算相结合，开发可微分的物理一致性模型。这直接属于化学信息学领域，并且其构建“神经gE模型”的方法与利用大模型或复杂模型处理化学问题的“化学大模型”主题在精神上高度相关。

**📖 中文摘要**

本文提出了DISCOMAX，一种用于相平衡计算的可微分算法，旨在保证机器学习和热力学模型在训练和推理时的一致性。该方法基于统计热力学，通过离散枚举和随后的掩码softmax聚合可行状态，并结合直通梯度估计器，实现了对神经超额吉布斯自由能模型的端到端物理一致性学习。研究在二元液-液相平衡数据上评估了该方法，证明其性能优于现有的基于代理模型的方法，同时为从不同类型的平衡数据中学习提供了一个通用框架。这项工作属于化学信息学领域，专注于将机器学习与物理模型结合以解决热力学预测问题。

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

满足标准1：论文的核心研究内容是开发一个集成了物理方程（Hopf-Cole变换）和深度学习（共享主干神经网络、DeepLS求解器）的框架，用于解决多孔介质中的非线性气体流动问题。这属于化学工程与机器学习交叉的化学信息学范畴，其构建复杂、可解释的混合模型的方法与“化学大模型”主题中利用AI解决复杂化学系统问题的方向一致。

**📖 中文摘要**

本文提出了一个用于多孔介质中气体流动建模的集成框架，该框架结合了Klinkenberg增强的本构关系、Hopf-Cole变换的混合形式线性控制方程、共享主干神经网络架构和深度最小二乘求解器。Hopf-Cole变换将原始非线性流动方程重新表述为与达西模型密切相关的等效线性系统。该框架还自然地促进了从有限或间接观测中反演压力依赖性渗透率和滑移参数，实现了对难以通过实验测量的流动特性的高效估计。数值结果证明了该框架在宽压力范围内准确恢复流动动力学和参数的能力，突出了其在致密地层中气体输运建模和反演方面的鲁棒性、准确性和计算效率。这项工作展示了机器学习与物理驱动模型在复杂化学工程问题中的深度结合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate modeling of gas flow through porous media is critical for many technological applications, including reservoir performance prediction, carbon capture and sequestration, and fuel cells and batteries. However, such modeling remains challenging due to strong nonlinear behavior and uncertainty in model parameters. In particular, gas slippage effects described by the Klinkenberg model introduce pressure-dependent permeability, which complicates numerical simulation and obscures deviations from classical Darcy flow behavior. To address these challenges, we present an integrated modeling framework for gas transport in porous media that combines a Klinkenberg-enhanced constitutive relation, Hopf-Cole-transformed mixed-form linear governing equations, a shared-trunk neural network architecture, and a Deep Least-Squares (DeepLS) solver. The Hopf-Cole transformation reformulates the original nonlinear flow equations into an equivalent linear system closely related to the Darcy model, while the mixed formulation, together with a shared-trunk neural architecture, enables simultaneous and accurate prediction of both pressure and velocity fields. A rigorous convergence analysis is performed both theoretically and numerically, establishing the stability and convergence properties of the proposed solver. Importantly, the proposed framework also naturally facilitates inverse modeling of pressure-dependent permeability and slippage parameters from limited or indirect observations, enabling efficient estimation of flow properties that are difficult to measure experimentally. Numerical results demonstrate accurate recovery of flow dynamics and parameters across a wide range of pressure regimes, highlighting the framework's robustness, accuracy, and computational efficiency for gas transport modeling and inversion in tight formations.

</details>

---

### 4. [Slack More, Predict Better: Proximal Relaxation for Probabilistic Latent Variable Model-based Soft Sensors](https://arxiv.org/abs/2603.11473)

**基本信息**

- 🔗 arXiv: [`2603.11473`](https://arxiv.org/abs/2603.11473)
- 👥 作者: Zehua Zou, Yiran Ma, Yulong Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11473.pdf)

**💡 相关性分析**

满足标准1：论文提出的新型非线性概率隐变量模型（NPLVM）及其变分推断策略，其核心方法论与构建稳健、可解释的化学过程或分子性质预测大模型的研究直接相关。

**📖 中文摘要**

本文提出了一种名为KProxNPLVM的新型非线性概率隐变量模型，旨在改进软传感器建模的准确性。该模型的核心创新在于通过引入Wasserstein距离作为近端算子来松弛学习目标，从而推导出一种新的变分推断策略。虽然论文主要关注工业过程建模，但其提出的概率隐变量模型框架、变分推断方法以及对模型性能的改进，与“化学大模型”主题中构建稳健、可解释的化学过程或分子性质预测模型的研究方向在方法论上高度相关。该模型处理不确定性、进行分布优化的能力，可被视为构建复杂化学系统大模型的一个基础组件。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Nonlinear Probabilistic Latent Variable Models (NPLVMs) are a cornerstone of soft sensor modeling due to their capacity for uncertainty delineation. However, conventional NPLVMs are trained using amortized variational inference, where neural networks parameterize the variational posterior. While facilitating model implementation, this parameterization converts the distributional optimization problem within an infinite-dimensional function space to parameter optimization within a finite-dimensional parameter space, which introduces an approximation error gap, thereby degrading soft sensor modeling accuracy. To alleviate this issue, we introduce KProxNPLVM, a novel NPLVM that pivots to relaxing the objective itself and improving the NPLVM's performance. Specifically, we first prove the approximation error induced by the conventional approach. Based on this, we design the Wasserstein distance as the proximal operator to relax the learning objective, yielding a new variational inference strategy derived from solving this relaxed optimization problem. Based on this foundation, we provide a rigorous derivation of KProxNPLVM's optimization implementation, prove the convergence of our algorithm can finally sidestep the approximation error, and propose the KProxNPLVM by summarizing the abovementioned content. Finally, extensive experiments on synthetic and real-world industrial datasets are conducted to demonstrate the efficacy of the proposed KProxNPLVM.

</details>

---

### 5. [Leveraging Phytolith Research using Artificial Intelligence](https://arxiv.org/abs/2603.11476)

**基本信息**

- 🔗 arXiv: [`2603.11476`](https://arxiv.org/abs/2603.11476)
- 👥 作者: Andrés G. Mejía Ramón, Kate Dudgeon, Nina Witteveen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11476.pdf)

**💡 相关性分析**

满足标准1：论文开发的多模态AI流水线，用于从微观粒子（植硅体）的2D/3D数据中自动分类和推断来源，其技术路径（特征提取、分类、混合物解析）与“质谱结构推理”中从质谱数据推断分子结构的核心任务直接相关。

**📖 中文摘要**

本文介绍了Sorometry，一个基于人工智能的端到端流水线，用于高通量数字化、推断和解释植硅体（植物微化石）。该工作流结合了2D图像和3D点云的多模态融合模型（ConvNeXt和PointNet++），并集成了贝叶斯有限混合模型来预测植物来源贡献。虽然应用领域是考古学和古生态学，但该研究在方法论上高度相关：它开发了一个完整的AI驱动流程，用于从复杂的微观粒子数据（此处为植硅体）中自动提取、分类和解释结构信息。其多模态模型融合、3D结构分析以及从混合样本中推断来源的方法，与“质谱结构推理”中从复杂质谱数据推断分子结构的核心挑战在技术路径上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phytolith analysis is a crucial tool for reconstructing past vegetation and human activities, but traditional methods are severely limited by labour-intensive, time-consuming manual microscopy. To address this bottleneck, we present Sorometry: a comprehensive end-to-end artificial intelligence pipeline for the high-throughput digitisation, inference, and interpretation of phytoliths. Our workflow processes z-stacked optical microscope scans to automatically generate synchronised 2D orthoimages and 3D point clouds of individual microscopic particles. We developed a multimodal fusion model that combines ConvNeXt for 2D image analysis and PointNet++ for 3D point cloud analysis, supported by a graphical user interface for expert annotation and review. Tested on reference collections and archaeological samples from the Bolivian Amazon, our fusion model achieved a global classification accuracy of 77.9\% across 24 diagnostic morphotypes and 84.5% for segmentation quality. Crucially, the integration of 3D data proved essential for distinguishing complex morphotypes (such as grass silica short cell phytoliths) whose diagnostic features are often obscured by their orientation in 2D projections. Beyond individual object classification, Sorometry incorporates Bayesian finite mixture modelling to predict overall plant source contributions at the assemblage level, successfully identifying specific plants like maize and palms in complex mixed samples. This integrated platform transforms phytolith research into an "omics"-scale discipline, dramatically expanding analytical capacity, standardising expert judgements, and enabling reproducible, population-level characterisations of archaeological and paleoecological assemblages.

</details>

---

### 6. [AutoVeriFix+: High-Correctness RTL Generation via Trace-Aware Causal Fix and Semantic Redundancy Pruning](https://arxiv.org/abs/2603.11489)

**基本信息**

- 🔗 arXiv: [`2603.11489`](https://arxiv.org/abs/2603.11489)
- 👥 作者: Yan Tan, Xiangchen Meng, Zijun Jiang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11489.pdf)

**💡 相关性分析**

满足标准1：论文提出的结合LLM生成与基于执行轨迹的验证/修正框架，其方法论与构建能够进行可靠推理和迭代修正的“化学大模型”（例如，用于分子设计或谱图解析）的研究方向直接相关。

**📖 中文摘要**

本文提出了AutoVeriFix+，一个用于生成功能正确的Verilog RTL代码的三阶段框架。该框架利用大语言模型生成高级Python参考模型和初始Verilog代码，并引入Concolic测试引擎来执行深度时序逻辑并识别边界情况漏洞。通过提供周期精确的执行轨迹和内部寄存器快照，该框架为LLM提供了修复复杂状态转移错误所需的因果上下文。虽然应用领域是硬件设计，但其核心是开发一个结合LLM高级语义推理和具体执行验证（通过轨迹分析）的系统，以提升生成代码的功能正确性。这种方法论——即利用LLM进行生成，并结合领域特定的验证和反馈机制进行迭代修正——对于构建能够可靠推理化学结构或质谱数据的“化学大模型”具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated impressive capabilities in generating software code for high-level programming languages such as Python and C++. However, their application to hardware description languages, such as Verilog, is challenging due to the scarcity of high-quality training data. Current approaches to Verilog code generation using LLMs often focus on syntactic correctness, resulting in code with functional errors. To address these challenges, we propose AutoVeriFix+, a novel three-stage framework that integrates high-level semantic reasoning with state-space exploration to enhance functional correctness and design efficiency. In the first stage, an LLM is employed to generate high-level Python reference models that define the intended circuit behavior. In the second stage, another LLM generates initial Verilog RTL candidates and iteratively fixes syntactic errors. In the third stage, we introduce a Concolic testing engine to exercise deep sequential logic and identify corner-case vulnerabilities. With cycle-accurate execution traces and internal register snapshots, AutoVeriFix+ provides the LLM with the causal context necessary to resolve complex state-transition errors. Furthermore, it will generate a coverage report to identify functionally redundant branches, enabling the LLM to perform semantic pruning for area optimization. Experimental results demonstrate that AutoVeriFix+ achieves over 80% functional correctness on rigorous benchmarks, reaching a pass@10 score of 90.2% on the VerilogEval-machine dataset. In addition, it eliminates an average of 25% redundant logic across benchmarks through trace-aware optimization.

</details>

---

### 7. [Gen-Fab: A Variation-Aware Generative Model for Predicting Fabrication Variations in Nanophotonic Devices](https://arxiv.org/abs/2603.11505)

**基本信息**

- 🔗 arXiv: [`2603.11505`](https://arxiv.org/abs/2603.11505)
- 👥 作者: Rambod Azimi, Yuri Grinberg, Dan-Xia Xu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11505.pdf)

**💡 相关性分析**

满足标准1：论文提出的生成模型（Gen-Fab）用于从设计布局预测制造后的物理结构及其不确定性，其生成式建模和不确定性量化的核心任务，与“化学大模型”和“质谱结构推理”中从输入（如分子式、谱图）生成或预测可能结构及其分布的任务直接相关。

**📖 中文摘要**

本文提出了Gen-Fab，一个基于条件生成对抗网络（cGAN）的生成模型，用于预测和建模硅光子器件制造过程中的纳米级变化（如过刻蚀、欠刻蚀）。该模型以设计布局（GDS格式）为输入，生成类似于扫描电子显微镜图像的高分辨率预测，捕捉工艺变化的范围。这项工作本质上是在创建制造过程的“数字孪生”，能够预测设计对应的可能物理实现及其不确定性。这种从设计到可能物理结构的生成式建模，与“化学大模型”中预测分子结构与其性质关系，或“质谱结构推理”中从谱图反推可能分子结构的生成任务，在概念和技术上高度契合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Silicon photonic devices often exhibit fabrication-induced variations such as over-etching, underetching, and corner rounding, which can significantly alter device performance. These variations are non-uniform and are influenced by feature size and shape. Accurate digital twins are therefore needed to predict the range of possible fabricated outcomes for a given design. In this paper, we introduce Gen-Fab, a conditional generative adversarial network (cGAN) based on Pix2Pix to predict and model uncertainty in photonic fabrication outcomes. The proposed method takes a design layout (in GDS format) as input and produces diverse high-resolution predictions similar to scanning electron microscope (SEM) images of fabricated devices, capturing the range of process variations at the nanometer scale. To enable one-to-many mapping, we inject a latent noise vector at the model bottleneck. We compare Gen-Fab against three baselines: (1) a deterministic U-Net predictor, (2) an inference-time Monte Carlo Dropout U-Net, and (3) an ensemble of varied U-Nets. Evaluations on an out-of-distribution dataset of fabricated photonic test structures demonstrate that Gen-Fab outperforms all baselines in both accuracy and uncertainty modeling. An additional distribution shift analysis further confirms its strong generalization to unseen fabrication geometries. Gen-Fab achieves the highest intersection-over-union (IoU) score of 89.8%, outperforming the deterministic U-Net (85.3%), the MC-Dropout U-Net (83.4%), and varying U-Nets (85.8%). It also better aligns with the distribution of real fabrication outcomes, achieving lower Kullback-Leibler divergence and Wasserstein distance.

</details>

---

### 8. [Leveraging Large Language Models and Survival Analysis for Early Prediction of Chemotherapy Outcomes](https://arxiv.org/abs/2603.11594)

**基本信息**

- 🔗 arXiv: [`2603.11594`](https://arxiv.org/abs/2603.11594)
- 👥 作者: Muhammad Faisal Shahid, Asad Afzal, Abdullah Faiz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11594.pdf)

**💡 相关性分析**

满足标准2：论文展示了利用大语言模型从非结构化文本中提取结构化医学知识（表型、结局）以构建预测模型数据集的完整流程。该方法论可直接迁移至化学信息学领域，用于从科学文本中提取化学结构、性质、谱图关联等数据，为相关主题的研究提供数据资源构建工具。

**📖 中文摘要**

本研究利用大语言模型和本体技术，从乳腺癌患者的电子病历中提取表型特征和治疗结局标签（如癌症进展、毒性），以构建早期化疗结果预测模型。研究采用随机生存森林模型预测生存时间，并将其用作分类器在特定时间点预测治疗结果。论文的核心贡献在于利用LLM解决临床数据中表型稀疏和标签缺失的挑战，从而为构建预测模型提供高质量的数据基础。这种方法——即利用LLM从非结构化文本中提取结构化、可计算的医学知识——为化学信息学领域提供了直接参考：可以类似地利用LLM从科学文献、实验报告或专利中自动提取化学实体、反应、性质及谱图数据，从而构建用于“化学大模型”训练或“质谱结构推理”的高质量数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemotherapy for cancer treatment is costly and accompanied by severe side effects, highlighting the critical need for early prediction of treatment outcomes to improve patient management and informed decision-making. Predictive models for chemotherapy outcomes using real-world data face challenges, including the absence of explicit phenotypes and treatment outcome labels such as cancer progression and toxicity. This study addresses these challenges by employing Large Language Models (LLMs) and ontology-based techniques for phenotypes and outcome label extraction from patient notes. We focused on one of the most frequently occurring cancers, breast cancer, due to its high prevalence and significant variability in patient response to treatment, making it a critical area for improving predictive modeling. The dataset included features such as vitals, demographics, staging, biomarkers, and performance scales. Drug regimens and their combinations were extracted from the chemotherapy plans in the EMR data and shortlisted based on NCCN guidelines, verified with NIH standards, and analyzed through survival modeling. The proposed approach significantly reduced phenotypes sparsity and improved predictive accuracy. Random Survival Forest was used to predict time-to-failure, achieving a C-index of 73%, and utilized as a classifier at a specific time point to predict treatment outcomes, with accuracy and F1 scores above 70%. The outcome probabilities were validated for reliability by calibration curves. We extended our approach to four other cancer types. This research highlights the potential of early prediction of treatment outcomes using LLM-based clinical data extraction enabling personalized treatment plans with better patient outcomes.

</details>

---

### 9. [Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)

**基本信息**

- 🔗 arXiv: [`2603.11627`](https://arxiv.org/abs/2603.11627)
- 👥 作者: Yichi Zhang, Le Xue, Wenbo Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11627.pdf)

**💡 相关性分析**

满足标准2和3：1) 论文构建了大规模、高质量的3D PET医学影像数据集，其数据收集、标注和整理范式为化学信息学领域构建类似的多模态（如分子、谱图、文本）数据集提供了直接参考（标准2）。2) 论文提出的通用分割基础模型SegAnyPET，其设计理念（通用性、提示驱动）对于思考如何构建化学领域的通用基础模型（如通用分子表示模型）具有重要的前瞻性和讨论价值（标准3）。

**📖 中文摘要**

本文致力于为3D全身正电子发射断层扫描（PET）图像开发通用的分割基础模型。作者构建了迄今为止最大、最全面的PET数据集（包含11041个扫描和59831个分割掩码），并在此基础上提出了SegAnyPET模型。该模型基于3D架构和提示工程策略，支持对器官和病变的通用、可扩展分割，并支持高效的人工校正。这项工作在医学影像领域示范了如何构建大规模、高质量的数据集以及基于此训练通用分割基础模型。其数据构建范式、模型设计思路（通用性、提示工程）以及推动临床应用的目标，为“化学大模型”和“质谱结构推理”领域提供了重要启示：即如何系统性地构建跨分子、谱图、性质的多模态化学数据集，并训练能够处理多样化下游任务的基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a key nuclear medicine imaging modality that visualizes radiotracer distributions to quantify in vivo physiological and metabolic processes, playing an irreplaceable role in disease management. Despite its clinical importance, the development of deep learning models for quantitative PET image analysis remains severely limited, driven by both the inherent segmentation challenge from PET's paucity of anatomical contrast and the high costs of data acquisition and annotation. To bridge this gap, we develop generalist foundational models for universal segmentation from 3D whole-body PET imaging. We first build the largest and most comprehensive PET dataset to date, comprising 11041 3D whole-body PET scans with 59831 segmentation masks for model development. Based on this dataset, we present SegAnyPET, an innovative foundational model with general-purpose applicability to diverse segmentation tasks. Built on a 3D architecture with a prompt engineering strategy for mask generation, SegAnyPET enables universal and scalable organ and lesion segmentation, supports efficient human correction with minimal effort, and enables a clinical human-in-the-loop workflow. Extensive evaluations on multi-center, multi-tracer, multi-disease datasets demonstrate that SegAnyPET achieves strong zero-shot performance across a wide range of segmentation tasks, highlighting its potential to advance the clinical applications of molecular imaging.

</details>

---

### 10. [PolyCrysDiff: Controllable Generation of Three-Dimensional Computable Polycrystalline Material Structures](https://arxiv.org/abs/2603.11695)

**基本信息**

- 🔗 arXiv: [`2603.11695`](https://arxiv.org/abs/2603.11695)
- 👥 作者: Chi Chen, Tianle Jiang, Xiaodong Wei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成式AI模型（扩散模型）来生成和设计多晶材料的三维微观结构。这直接属于‘化学大模型’主题，即利用先进的人工智能模型解决化学和材料科学中的复杂问题。

**📖 中文摘要**

本文提出了PolyCrysDiff，一个基于条件潜在扩散的框架，用于端到端生成可计算的3D多晶材料微观结构。该工作直接面向材料科学中的结构生成问题，属于化学信息学中利用生成模型（如扩散模型）进行材料结构设计与推理的核心范畴。论文展示了如何通过生成模型控制晶粒形态、取向分布和空间相关性，并利用晶体塑性有限元方法验证生成结构的物理有效性。这项工作为阐明多晶材料的结构-性能关系提供了关键工具，是化学大模型在材料科学领域生成与设计方面的典型应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The three-dimensional (3D) microstructures of polycrystalline materials exert a critical influence on their mechanical and physical properties. Realistic, controllable construction of these microstructures is a key step toward elucidating structure-property relationships, yet remains a formidable challenge. Herein, we propose PolyCrysDiff, a framework based on conditional latent diffusion that enables the end-to-end generation of computable 3D polycrystalline microstructures. Comprehensive qualitative and quantitative evaluations demonstrate that PolyCrysDiff faithfully reproduces target grain morphologies, orientation distributions, and 3D spatial correlations, while achieving an $R^2$ over 0.972 on grain attributes (e.g., size and sphericity) control, thereby outperforming mainstream approaches such as Markov random field (MRF)- and convolutional neural network (CNN)-based methods. The computability and physical validity of the generated microstructures are verified through a series of crystal plasticity finite element method (CPFEM) simulations. Leveraging PolyCrysDiff's controllable generative capability, we systematically elucidate how grain-level microstructural characteristics affect the mechanical properties of polycrystalline materials. This development is expected to pave a key step toward accelerated, data-driven optimization and design of polycrystalline materials.

</details>

---

### 11. [EvoFlows: Evolutionary Edit-Based Flow-Matching for Protein Engineering](https://arxiv.org/abs/2603.11703)

**基本信息**

- 🔗 arXiv: [`2603.11703`](https://arxiv.org/abs/2603.11703)
- 👥 作者: Nicolas Deutschmann, Constance Ferragu, Jonathan D. Ziegler 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11703.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的生成模型（EvoFlows）用于蛋白质工程，这直接属于‘化学大模型’主题在生物分子（蛋白质）序列设计与优化方面的应用。

**📖 中文摘要**

本文介绍了EvoFlows，一种用于蛋白质工程的变长序列到序列建模方法。与自回归和掩码语言模型不同，EvoFlows通过对模板蛋白质序列执行有限、可控数量的插入、删除和替换来预测突变。该方法利用编辑流来学习进化相关蛋白质序列之间的突变轨迹，同时模拟相关天然蛋白质的分布以及连接它们的突变路径。通过在大规模蛋白质序列数据集上的评估，表明EvoFlows在捕获蛋白质序列分布方面与常用的掩码语言模型质量相当，同时在从给定模板生成非平凡且类天然突变体方面表现出改进的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce EvoFlows, a variable-length sequence-to-sequence protein modeling approach uniquely suited to protein engineering. Unlike autoregressive and masked language models, EvoFlows perform a limited, controllable number of insertions, deletions, and substitutions on a template protein sequence. In other words, EvoFlows predict not only _which_ mutation to perform, but also _where_ it should occur. Our approach leverages edit flows to learn mutational trajectories between evolutionarily-related protein sequences, simultaneously modeling distributions of related natural proteins and the mutational paths connecting them. Through extensive _in silico_ evaluation on diverse protein communities from UNIREF and OAS, we demonstrate that EvoFlows capture protein sequence distributions with a quality comparable to leading masked language models commonly used in protein engineering, while showing improved ability to generate non-trivial yet natural-like mutants from a given template protein.

</details>

---

### 12. [PhiPlot: A Web-Based Interactive EDA Environment for Atmospherically Relevant Molecules](https://arxiv.org/abs/2603.11751)

**基本信息**

- 🔗 arXiv: [`2603.11751`](https://arxiv.org/abs/2603.11751)
- 👥 作者: Matias Loukojärvi, Ananth Mahadevan, Katsiaryna Haitsiukevich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11751.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个专门用于探索大气化学相关分子数据集的交互式工具（PhiPlot）。这为化学信息学领域的研究人员提供了可用于分析分子数据、进行知识发现和数据驱动的假设生成的资源，与‘化学大模型’主题中数据分析和工具开发的方向相关。

**📖 中文摘要**

本文介绍了PhiPlot，一个用于大气相关分子高维数据集交互式探索和基于知识的降维的Web环境。该工具集成了可视化、聚类和领域知识引导的嵌入细化功能，旨在帮助发现数据中的模式并支持假设生成。该应用连接到一个不断演化的分子数据库集合，为大气化学中的数据驱动研究提供了一个可访问的界面。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in computational chemistry have produced high-dimensional datasets on atmospherically relevant molecules. To aid exploration of such datasets, particularly for the study of atmospheric aerosol formation, we introduce PhiPlot: a web-based environment for interactive exploration and knowledge-based dimensionality reduction. The integration of visualisation, clustering, and domain knowledge-guided embedding refinement enables the discovery of patterns in the data and supports hypothesis generation. The application connects to an existing, evolving collection of molecular databases, offering an accessible interface for data-driven research in atmospheric chemistry.

</details>

---

### 13. [OMNIA: Closing the Loop by Leveraging LLMs for Knowledge Graph Completion](https://arxiv.org/abs/2603.11820)

**基本信息**

- 🔗 arXiv: [`2603.11820`](https://arxiv.org/abs/2603.11820)
- 👥 作者: Frédéric Ieng, Soror Sahri, Mourad Ouzzani 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11820.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进知识图谱的构建和补全，其中关键环节是利用大型语言模型进行语义验证。知识图谱是化学信息学中组织化学知识（如分子、反应、性质）的核心数据结构，因此这项工作与利用大模型处理化学信息密切相关。

**📖 中文摘要**

本文提出了OMNIA，一个用于知识图谱补全的两阶段方法，它结合了结构推理和语义推理。该方法首先通过在知识图谱内部对语义相关的实体和关系进行聚类来生成候选三元组，然后通过轻量级嵌入过滤和基于大型语言模型的语义验证来验证它们。OMNIA专门针对大型语言模型生成的图谱中最常见的隐式语义，并在多个数据集上进行了评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge Graphs (KGs) are widely used to represent structured knowledge, yet their automatic construction, especially with Large Language Models (LLMs), often results in incomplete or noisy outputs. Knowledge Graph Completion (KGC) aims to infer and add missing triples, but most existing methods either rely on structural embeddings that overlook semantics or language models that ignore the graph's structure and depend on external sources. In this work, we present OMNIA, a two-stage approach that bridges structural and semantic reasoning for KGC. It first generates candidate triples by clustering semantically related entities and relations within the KG, then validates them through lightweight embedding filtering followed by LLM-based semantic validation. OMNIA performs on the internal KG, without external sources, and specifically targets implicit semantics that are most frequent in LLM-generated graphs. Extensive experiments on multiple datasets demonstrate that OMNIA significantly improves F1-score compared to traditional embedding-based models. These results highlight OMNIA's effectiveness and efficiency, as its clustering and filtering stages reduce both search space and validation cost while maintaining high-quality completion.

</details>

---

### 14. [A Decade of Generative Adversarial Networks for Porous Material Reconstruction](https://arxiv.org/abs/2603.11836)

**基本信息**

- 🔗 arXiv: [`2603.11836`](https://arxiv.org/abs/2603.11836)
- 👥 作者: Ali Sadeghkhani, Brandon Bennett, Masoud Babaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11836.pdf)

**💡 相关性分析**

满足标准3：这篇论文是一篇关于生成对抗网络在多孔材料重建中应用的系统性综述。它全面总结了该领域过去十年的进展、方法分类和挑战，为‘化学大模型’主题中生成模型在材料科学（多孔材料）这一具体方向的研究提供了重要的综述和展望。

**📖 中文摘要**

本文系统回顾了2017年至2026年初发表的96篇同行评审文章，分析了生成对抗网络在多孔材料图像重建中的演变和应用。综述将GAN架构分为六类，并揭示了在孔隙度准确性、渗透率预测和可重建体积方面的显著进展。尽管面临计算效率和2D到3D转换中结构连续性等挑战，但该分析为基于特定应用需求选择适当的GAN架构提供了一个全面的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital reconstruction of porous materials has become increasingly critical for applications ranging from geological reservoir characterization to tissue engineering and electrochemical device design. While traditional methods such as micro-computed tomography and statistical reconstruction approaches have established foundations in this field, the emergence of deep learning techniques, particularly Generative Adversarial Networks (GANs), has revolutionized porous media reconstruction capabilities. This review systematically analyzes 96 peer-reviewed articles published from 2017 to early 2026, examining the evolution and applications of GAN-based approaches for porous material image reconstruction. We categorize GAN architectures into six distinct classes, namely Vanilla GANs, Multi-Scale GANs, Conditional GANs, Attention-Enhanced GANs, Style-based GANs, and Hybrid Architecture GANs. Our analysis reveals substantial progress including improvements in porosity accuracy (within 1% of original samples), permeability prediction (up to 79% reduction in mean relative errors), and achievable reconstruction volumes (from initial $64^3$ to current $2{,}200^3$ voxels). Despite these advances, persistent challenges remain in computational efficiency, memory constraints for large-scale reconstruction, and maintaining structural continuity in 2D-to-3D transformations. This systematic analysis provides a comprehensive framework for selecting appropriate GAN architectures based on specific application requirements.

</details>

---

### 15. [Inverse Neural Operator for ODE Parameter Optimization](https://arxiv.org/abs/2603.11854)

**基本信息**

- 🔗 arXiv: [`2603.11854`](https://arxiv.org/abs/2603.11854)
- 👥 作者: Zhi-Song Liu, Wenqing Peng, Helmi Toropainen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11854.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的神经算子框架，用于从观测数据中逆向推断化学/生物系统的动力学参数（如大气化学、基因调控网络）。这属于‘化学大模型’主题中利用深度学习模型解决化学动力学逆问题的范畴。

**📖 中文摘要**

本文提出了逆向神经算子，一个用于从稀疏、部分观测中恢复隐藏常微分方程参数的两阶段框架。第一阶段，一个带有交叉注意力的条件傅里叶神经算子学习一个可微的代理模型，从任意稀疏输入重建完整的ODE轨迹。第二阶段，一个摊销漂移模型在参数空间中学习一个核加权的速度场，将随机参数初始化向真实值传输，而无需通过代理模型反向传播。该方法在一个真实世界的大气化学基准和一个合成基因调控网络上进行了实验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Inverse Neural Operator (INO), a two-stage framework for recovering hidden ODE parameters from sparse, partial observations. In Stage 1, a Conditional Fourier Neural Operator (C-FNO) with cross-attention learns a differentiable surrogate that reconstructs full ODE trajectories from arbitrary sparse inputs, suppressing high-frequency artifacts via spectral regularization. In Stage 2, an Amortized Drifting Model (ADM) learns a kernel-weighted velocity field in parameter space, transporting random parameter initializations toward the ground truth without backpropagating through the surrogate, avoiding the Jacobian instabilities that afflict gradient-based inversion in stiff regimes. Experiments on a real-world stiff atmospheric chemistry benchmark (POLLU, 25 parameters) and a synthetic Gene Regulatory Network (GRN, 40 parameters) show that INO outperforms gradient-based and amortized baselines in parameter recovery accuracy while requiring only 0.23s inference time, a 487x speedup over iterative gradient descent.

</details>

---

### 16. [AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization](https://arxiv.org/abs/2603.11873)

**基本信息**

- 🔗 arXiv: [`2603.11873`](https://arxiv.org/abs/2603.11873)
- 👥 作者: Qiyang Li, Rui Kong, Yuchen Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11873.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大型语言模型的动态适配器推理，这直接关系到构建和部署更高效的“化学大模型”，属于核心主题相关。

**📖 中文摘要**

本文提出AdaFuse框架，旨在加速大型语言模型（LLM）中动态适配器（如LoRA）的推理过程。该框架通过令牌级预门控策略和融合内核优化，解决了动态稀疏结构（如MoE）与参数高效适配器集成时导致的推理延迟激增问题。其核心创新在于将路由决策提前并静态化，从而允许对选定适配器的参数进行一次性融合操作。这项工作直接涉及“化学大模型”主题，因为它专注于提升大语言模型（作为化学信息学中潜在的基础模型或工具）的推理效率和架构优化，属于核心主题相关的改进方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of dynamic, sparse structures like Mixture-of-Experts (MoE) with parameter-efficient adapters (e.g., LoRA) is a powerful technique for enhancing Large Language Models (LLMs). However, this architectural enhancement comes at a steep cost: despite minimal increases in computational load, the inference latency often skyrockets, leading to decoding speeds slowing by over 2.5 times. Through a fine-grained performance analysis, we pinpoint the primary bottleneck not in the computation itself, but in the severe overhead from fragmented, sequential CUDA kernel launches required for conventional dynamic routing. To address this challenge, we introduce AdaFuse, a framework built on a tight co-design between the algorithm and the underlying hardware system to enable efficient dynamic adapter execution. Departing from conventional layer-wise or block-wise routing, AdaFuse employs a token-level pre-gating strategy, which makes a single, global routing decision for all adapter layers before a token is processed. This "decide-once, apply-everywhere" approach effectively staticizes the execution path for each token, creating an opportunity for holistic optimization. We capitalize on this by developing a custom CUDA kernel that performs a fused switching operation, merging the parameters of all selected LoRA adapters into the backbone model in a single, efficient pass. Experimental results on popular open-source LLMs show that AdaFuse achieves accuracy on par with state-of-the-art dynamic adapters while drastically cutting decoding latency by a factor of over 2.4x, thereby bridging the gap between model capability and inference efficiency.

</details>

---

### 17. [Bielik-Minitron-7B: Compressing Large Language Models via Structured Pruning and Knowledge Distillation for the Polish Language](https://arxiv.org/abs/2603.11881)

**基本信息**

- 🔗 arXiv: [`2603.11881`](https://arxiv.org/abs/2603.11881)
- 👥 作者: Remigiusz Kinas, Paweł Kiszczak, Sergio P. Perez 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11881.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种大语言模型的压缩、知识蒸馏和对齐方法学，这为构建领域专用的“化学大模型”提供了可借鉴的技术工具和资源（方法论）。

**📖 中文摘要**

本文详细介绍了Bielik-Minitron-7B模型的创建过程，这是一个通过结构化剪枝和知识蒸馏从11B参数模型压缩而来的7.35B参数模型，专门针对波兰语等欧洲语言进行了优化。该工作展示了一种高效的大语言模型压缩和部署路径，在保持原始模型大部分性能的同时显著提升了推理速度。虽然其应用领域是自然语言处理，但所采用的两阶段压缩方法论（结构化混合剪枝与知识蒸馏）以及模型对齐流程（SFT、DPO、GRPO）对于构建和优化特定领域（如化学）的大模型具有重要的参考价值，属于可用于大模型构建的数据资源或工具方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This report details the creation of Bielik-Minitron-7B, a compressed 7.35B parameter version of the Bielik-11B-v3.0 model, specifically optimized for European languages. By leveraging a two-stage compression methodology inspired by the NVIDIA Minitron approach, we combined structured hybrid pruning and knowledge distillation to reduce the model's parameter count by 33.4%, from 11.04B to 7.35B. We utilized the NVIDIA Model Optimizer for structural pruning and the NVIDIA NeMo Framework for logit-based distillation for quality recovery. Following distillation, the model underwent a rigorous alignment pipeline consisting of Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO-P), and Reinforcement Learning (GRPO). Our final model successfully recovered approximately 90% of the baseline model's performance while providing up to 50% inference speedup. This approach demonstrates an efficient pathway to create language models for less-represented languages, preserving the original model quality while reducing inference deployment costs.

</details>

---

### 18. [Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding](https://arxiv.org/abs/2603.11924)

**基本信息**

- 🔗 arXiv: [`2603.11924`](https://arxiv.org/abs/2603.11924)
- 👥 作者: Xinyu Li, Zhen Zhang, Qi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11924.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建用于化学动力学理解的4D多模态大语言模型（Chem4DLLM），并引入了新的任务（ChemDU）和基准数据集（Chem4DBench），这直接围绕“化学大模型”主题，并且其动态理解能力与“质谱结构推理”中需要推理结构变化过程密切相关。

**📖 中文摘要**

本文提出了Chem4DLLM，一个用于化学动力学理解（ChemDU）的4D多模态大语言模型。该模型旨在解决现有化学理解任务主要依赖静态分子表示的局限性，能够将4D分子轨迹（包含几何和旋转动力学信息）转化为可解释的自然语言解释。作者构建了首个配对4D分子轨迹与专家解释的数据集Chem4DBench，并提出了一个统一的模型架构，该架构集成了等变图编码器和预训练大语言模型，以显式捕获分子几何和旋转动力学。这项工作直接位于“化学大模型”和“质谱结构推理”的交叉点：它旨在构建一个能够理解和推理动态化学过程（可能涉及质谱中观测到的碎片化过程）的化学领域大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability, we construct Chem4DBench, the first dataset pairing 4D molecular trajectories with expert-authored explanations across these settings. We further propose Chem4DLLM, a unified model that integrates an equivariant graph encoder with a pretrained large language model to explicitly capture molecular geometry and rotational dynamics. We hope that ChemDU, together with Chem4DBench and Chem4DLLM, will stimulate further research in dynamic chemical understanding and multimodal scientific reasoning.

</details>

---

### 19. [Learning Transferable Sensor Models via Language-Informed Pretraining](https://arxiv.org/abs/2603.11950)

**基本信息**

- 🔗 arXiv: [`2603.11950`](https://arxiv.org/abs/2603.11950)
- 👥 作者: Yuliang Chen, Arvind Pillai, Yu Yvonne Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11950.pdf)

**💡 相关性分析**

满足标准2：论文提出的SLIP框架为从多变量时间序列（如质谱信号）中学习语言对齐的可迁移表征提供了一种通用的、开源的方法论和工具，这可用于构建质谱数据理解模型或增强化学大模型的多模态能力。

**📖 中文摘要**

本文提出了SLIP（传感器语言信息预训练）框架，用于从多变量时间序列数据中学习可迁移的、与语言对齐的表征。该框架结合了对比对齐和传感器条件描述生成，支持不同时间分辨率和可变长度输入，无需重新训练即可进行推理。SLIP在包括零样本迁移、信号描述和问答在内的11个数据集上展示了卓越性能。虽然主要应用于通用传感器数据，但其核心思想——通过语言对齐学习跨域可迁移的表征——对于化学和质谱领域至关重要。例如，质谱数据本质上是多变量时间序列/信号，SLIP的方法论可以为构建能够理解质谱信号语义、进行零样本推理或跨仪器泛化的“化学大模型”或质谱分析工具提供重要的技术框架和灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern sensing systems generate large volumes of unlabeled multivariate time-series data. This abundance of unlabeled data makes self-supervised learning (SSL) a natural approach for learning transferable representations. However, most existing approaches are optimized for reconstruction or forecasting objectives and often fail to capture the semantic structure required for downstream classification and reasoning tasks. While recent sensor-language alignment methods improve semantic generalization through captioning and zero-shot transfer, they are limited to fixed sensor configurations, such as predefined channel sets, signal lengths, or temporal resolutions, which hinders cross-domain applicability. To address these gaps, we introduce \textbf{SLIP} (\textbf{S}ensor \textbf{L}anguage-\textbf{I}nformed \textbf{P}retraining), an open-source framework for learning language-aligned representations that generalize across diverse sensor setups. SLIP integrates contrastive alignment with sensor-conditioned captioning, facilitating both discriminative understanding and generative reasoning. By repurposing a pretrained decoder-only language model via cross-attention and introducing an elegant, flexible patch-embedder, SLIP supports different temporal resolutions and variable-length input at inference time without additional retraining. Across 11 datasets, SLIP demonstrates superior performance in zero-shot transfer, signal captioning, and question answering. It achieves a 77.14% average linear-probing accuracy, a 5.93% relative improvement over strong baselines, and reaches 64.83% accuracy in sensor-based question answering.

</details>

---

### 20. [Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era](https://arxiv.org/abs/2603.12016)

**基本信息**

- 🔗 arXiv: [`2603.12016`](https://arxiv.org/abs/2603.12016)
- 👥 作者: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12016.pdf)

**💡 相关性分析**

满足标准2：Nyxus作为一个高效、可扩展的图像特征提取库，提供了可用于化学信息学（如质谱成像）分析的数据处理工具和特征资源，有助于从复杂化学图像中生成可用于模型训练的结构化数据。

**📖 中文摘要**

本文介绍了Nyxus，一个为大数据和AI时代设计的下一代图像特征提取库。Nyxus针对2D和3D图像数据进行了可扩展的核外特征提取优化，并经过了严格的测试。其全面的特征集覆盖了包括放射组学和细胞分析在内的多个生物医学领域，并设计为在CPU和GPU上具有计算可扩展性。该库以多种形式提供（Python包、命令行工具、Napari插件、OCI容器），旨在满足不同用户的需求。虽然Nyxus主要面向生物医学图像分析，但其高效、可扩展的特征提取能力对于化学信息学和质谱分析领域同样具有重要价值。例如，在质谱成像（MSI）中，产生的也是2D/3D图像数据（每个像素点对应一个质谱），Nyxus可以用于从这些化学图像中提取大量定量特征，为后续的化学大模型训练或质谱结构推理提供丰富的数据资源（特征集）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of extracted features. To address these needs, we developed a novel feature extraction library called Nyxus. Nyxus is designed from the ground up for scalable out-of-core feature extraction for 2D and 3D image data and rigorously tested against established standards. The comprehensive feature set of Nyxus covers multiple biomedical domains including radiomics and cellular analysis, and is designed for computational scalability across CPUs and GPUs. Nyxus has been packaged to be accessible to users of various skill sets and needs: as a Python package for code developers, a command line tool, as a Napari plugin for low to no-code users or users that want to visualize results, and as an Open Container Initiative (OCI) compliant container that can be used in cloud or super-computing workflows aimed at processing large data sets. Further, Nyxus enables a new methodological approach to feature extraction allowing for programmatic tuning of many features sets for optimal computational efficiency or coverage for use in novel machine learning and deep learning applications.

</details>

---

### 21. [Chemical Reaction Networks Learn Better than Spiking Neural Networks](https://arxiv.org/abs/2603.12060)

**基本信息**

- 🔗 arXiv: [`2603.12060`](https://arxiv.org/abs/2603.12060)
- 👥 作者: Sophie Jaffard, Ivo F. Sbalzarini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12060.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是证明和探索化学反应网络作为一种计算模型的学习能力，这直接关联到构建基于化学系统的“模型”，是“化学大模型”主题下一种非常规但基础性的研究方向。

**📖 中文摘要**

本文从数学上证明，在没有隐藏层的化学反应网络（CRN）可以解决需要尖峰神经网络（SNN）具备隐藏层才能完成的任务。研究使用确定性质量作用动力学公式来描述CRN，并提供了网络全局行为的解析遗憾界，分析了其渐近行为和VC维。数值实验证实了所提出的化学反应网络对于像素图像分类的学习能力，并且比带有隐藏层的SNN更准确、更高效。这项工作为化学计算机中的机器学习提供了动机，并为生化反应网络可能表现出比神经元网络更高效的学习行为提供了数学解释。它直接关联到使用非传统计算框架（化学系统）构建“模型”，虽然不同于典型的深度学习大模型，但拓展了“模型”的内涵，属于利用化学系统进行信息处理的“化学大模型”的一种新颖且基础的理论探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We mathematically prove that chemical reaction networks without hidden layers can solve tasks for which spiking neural networks require hidden layers. Our proof uses the deterministic mass-action kinetics formulation of chemical reaction networks. Specifically, we prove that a certain reaction network without hidden layers can learn a classification task previously proved to be achievable by a spiking neural network with hidden layers. We provide analytical regret bounds for the global behavior of the network and analyze its asymptotic behavior and Vapnik-Chervonenkis dimension. In a numerical experiment, we confirm the learning capacity of the proposed chemical reaction network for classifying handwritten digits in pixel images, and we show that it solves the task more accurately and efficiently than a spiking neural network with hidden layers. This provides a motivation for machine learning in chemical computers and a mathematical explanation for how biological cells might exhibit more efficient learning behavior within biochemical reaction networks than neuronal networks.

</details>

---

### 22. [Paper Title: LoV3D: Grounding Cognitive Prognosis Reasoning in Longitudinal 3D Brain MRI via Regional Volume Assessments](https://arxiv.org/abs/2603.12071)

**基本信息**

- 🔗 arXiv: [`2603.12071`](https://arxiv.org/abs/2603.12071)
- 👥 作者: Zhaoyang Jiang, Zhizhong Fu, David McAllister 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12071.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种将领域专业知识（脑部体积指标）与大语言模型训练和验证相结合的方法论框架（LoV3D），这为构建可靠、可解释且基于专业知识的“化学大模型”提供了重要的技术工具和设计思路。

**📖 中文摘要**

本文提出了LoV3D，一个用于训练3D视觉语言模型的流程，该模型能够读取纵向3D脑部MRI，生成区域级解剖学评估，与先前扫描进行纵向比较，并最终输出诊断（认知正常、轻度认知障碍或痴呆）以及综合诊断摘要。该流程通过强制标签一致性、纵向连贯性和生物学合理性来确保最终诊断的可靠性，从而减少幻觉风险。训练过程引入了一个临床加权的验证器，根据从标准化体积指标得出的规范参考自动评分候选输出，驱动直接偏好优化而无需人工标注。这项工作展示了如何将大语言模型与专业的3D医学影像分析相结合，构建一个可解释、可靠的领域专用AI系统。虽然应用在神经影像学，但其方法论——将领域知识（体积指标）与大语言模型对齐和验证相结合——对于构建可靠、可解释的“化学大模型”（例如，用于质谱解析或分子性质预测）具有重要的借鉴意义，属于构建领域大模型的方法论资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Longitudinal brain MRI is essential for characterizing the progression of neurological diseases such as Alzheimer's disease assessment. However, current deep-learning tools fragment this process: classifiers reduce a scan to a label, volumetric pipelines produce uninterpreted measurements, and vision-language models (VLMs) may generate fluent but potentially hallucinated conclusions. We present LoV3D, a pipeline for training 3D vision-language models, which reads longitudinal T1-weighted brain MRI, produces a region-level anatomical assessment, conducts longitudinal comparison with the prior scan, and finally outputs a three-class diagnosis (Cognitively Normal, Mild Cognitive Impairment, or Dementia) along with a synthesized diagnostic summary. The stepped pipeline grounds the final diagnosis by enforcing label consistency, longitudinal coherence, and biological plausibility, thereby reducing the risks of hallucinations. The training process introduces a clinically-weighted Verifier that scores candidate outputs automatically against normative references derived from standardized volume metrics, driving Direct Preference Optimization without a single human annotation. On a subject-level held-out ADNI test set (479 scans, 258 subjects), LoV3D achieves 93.7% three-class diagnostic accuracy (+34.8% over the no-grounding baseline), 97.2% on two-class diagnosis accuracy (+4% over the SOTA) and 82.6% region-level anatomical classification accuracy (+33.1% over VLM baselines). Zero-shot transfer yields 95.4% on MIRIAD (100% Dementia recall) and 82.9% three-class accuracy on AIBL, confirming high generalizability across sites, scanners, and populations. Code is available at this https URL .

</details>

---

### 23. [A Multi-Label Temporal Convolutional Framework for Transcription Factor Binding Characterization](https://arxiv.org/abs/2603.12073)

**基本信息**

- 🔗 arXiv: [`2603.12073`](https://arxiv.org/abs/2603.12073)
- 👥 作者: Pietro Demurtas, Ferdinando Zanchetta, Giovanni Perini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12073.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于TCN的多标签深度学习框架，为从序列数据（如DNA序列，类比质谱信号）中协同预测多个标签（如TF结合，类比化学子结构）提供了方法工具，可用于“质谱结构推理”模型的开发。

**📖 中文摘要**

本文研究了DNA转录因子结合位点识别作为一个多标签分类问题，使用基于时间卷积网络（TCNs）的深度学习模型来预测DNA序列上的多个TF结合谱。该方法能够捕获TF之间的相关性及其协同调控机制，从而揭示具有生物学意义的基序和共结合模式。虽然研究领域是生物信息学，但其核心技术——使用深度学习模型（TCN）处理序列数据以进行多标签预测和发现协同模式——与化学信息学和质谱分析中的关键问题高度相关。例如，在质谱结构推理中，需要从质谱信号（一种序列/谱图数据）中同时推断出多种结构特征（如官能团、子结构），这也是一个多标签学习问题。因此，该论文提出的模型架构和方法为“质谱结构推理”任务提供了潜在的可借鉴技术框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transcription factors (TFs) regulate gene expression through complex and co-operative mechanisms. While many TFs act together, the logic underlying TFs binding and their interactions is not fully understood yet. Most current approaches for TF binding site prediction focus on individual TFs and binary classification tasks, without a full analysis of the possible interactions among various TFs. In this paper we investigate DNA TF binding site recognition as a multi-label classification problem, achieving reliable predictions for multiple TFs on DNA sequences retrieved in public repositories. Our deep learning models are based on Temporal Convolutional Networks (TCNs), which are able to predict multiple TF binding profiles, capturing correlations among TFs andtheir cooperative regulatory mechanisms. Our results suggest that multi-label learning leading to reliable predictive performances can reveal biologically meaningful motifs and co-binding patterns consistent with known TF interactions, while also suggesting novel relationships and cooperation among TFs.

</details>

---

### 24. [Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction](https://arxiv.org/abs/2603.11061)

**基本信息**

- 🔗 arXiv: [`2603.11061`](https://arxiv.org/abs/2603.11061)
- 👥 作者: Van Le, Tan Le
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11061.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质残基pKa预测的混合量子-经典模型框架。虽然主题未直接命名为“化学大模型”或“质谱结构推理”，但其核心是开发用于化学/生物分子性质预测的先进计算模型（一种特定类型的化学信息学模型），这与“化学大模型”的主题在广义上相关，即利用先进的计算模型（包括量子启发方法）解决化学信息学问题。

**📖 中文摘要**

本文提出了一种用于准确预测残基水平pKa值的混合量子-经典框架。pKa预测对于理解蛋白质功能、稳定性和反应性至关重要。该工作通过高斯核基的量子启发特征映射来丰富残基水平的表示，这些量子增强的描述符与归一化的结构特征相结合，形成统一的混合编码，并由深度量子神经网络（DQNN）处理。该架构捕获了经典模型无法访问的残基微环境中的非线性关系。在多个精选描述符集上的基准测试表明，DQNN相对于经典基线实现了更好的跨上下文泛化能力。在PKAD-R实验基准和Aβ40案例研究上的外部评估进一步突出了量子启发表示的鲁棒性和可迁移性。这项工作通过将量子启发的特征变换与经典生化描述符相结合，为残基水平pKa预测和蛋白质静电学的更广泛应用建立了一种可扩展且具有实验可迁移性的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue microenvironments that are not accessible to classical models. Benchmarking across multiple curated descriptor sets demonstrates that the DQNN achieves improved cross-context generalization relative to classical baselines. External evaluation on the PKAD-R experimental benchmark and an A$\beta$40 case study further highlights the robustness and transferability of the quantum-inspired representation. By integrating quantum-inspired feature transformations with classical biochemical descriptors, this work establishes a scalable and experimentally transferable approach for residue-level pKa prediction and broader applications in protein electrostatics.

</details>

---

### 25. [Exploring Collatz Dynamics with Human-LLM Collaboration](https://arxiv.org/abs/2603.11066)

**基本信息**

- 🔗 arXiv: [`2603.11066`](https://arxiv.org/abs/2603.11066)
- 👥 作者: Edward Y. Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11066.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索人类与大型语言模型（LLM）在数学研究（Collatz猜想）中的协作。虽然研究领域是数学，但其核心方法论是开发和利用“人类-LLM协作”这一新型研究范式，LLM在此作为研究助手和推理伙伴。这直接涉及“大模型”（LLM）在科学研究（包括数学和潜在的科学发现）中的应用，与“化学大模型”主题中“大模型在科学领域的应用”这一广义内涵相关。

**📖 中文摘要**

本文通过人类与大型语言模型（LLM）协作的方式，探索了Collatz迭代的结构特性。研究观察了大规模计算探索中出现的两种现象：剩余类的模运算扰乱和轨迹的爆发-间隙分解。论文证明了若干结构结果，包括一个模扰乱引理，表明间隙返回映射在高位上充当精确双射；一个持久退出引理，描述了持久状态后的间隙结构；以及一个在间隙返回动力学下二进制表示已知部分的衰减性质。进一步证明，在模模型中，间隙长度和2进赋值遵循几何分布，而持久运行长度是几何的，预期爆发长度E[B]=2；这些共同预测了严格的轨道收缩。这些结果表明了一个条件框架，其中收敛性将取决于关于爆发和间隙长度的适当轨道假设，而这些假设又由一个轨道均匀分布猜想所暗示。论文还记录了通过这些观察得以发展的人类-LLM协作过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate structural properties of the Collatz iteration through two phenomena observed in large computational exploration: modular scrambling of residue classes and a burst--gap decomposition of trajectories. We prove several structural results, including a modular scrambling lemma showing that the gap-return map acts as an exact bijection on high bits, a persistent exit lemma characterizing gap structure after persistent states, and a decay property for known portions of binary representations under gap-return dynamics. We further prove that, in the modular model, gap lengths and $2$-adic valuations follow geometric distributions, while persistent run lengths are geometric with expected burst length $E[B]=2$; together these predict strict orbit contraction. These results suggest a conditional framework in which convergence would follow from suitable orbitwise hypotheses on burst and gap lengths, which in turn are suggested by an orbit equidistribution conjecture. However, the key hypotheses remain open, and the framework is exploratory rather than a complete reduction. The paper also documents the human-LLM collaboration through which these observations were developed.

</details>

---

### 26. [From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery](https://arxiv.org/abs/2603.11068)

**基本信息**

- 🔗 arXiv: [`2603.11068`](https://arxiv.org/abs/2603.11068)
- 👥 作者: Iman Peivaste, Salim Belouettar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大型语言模型（LLM）的ReAct智能体框架，用于材料科学（高熵合金）的逆向设计。这直接涉及“化学大模型”主题，即利用大模型（LLM）解决化学和材料科学中的复杂发现与设计问题。

**📖 中文摘要**

本文提出了一种用于高熵合金（HEA）发现的ReAct（推理+行动）LLM智能体框架，以解决从目标晶体相可靠地发现HEA成分这一高维逆向设计问题。该智能体自主提出、验证并迭代优化HEA成分，其方法是查询一个基于4,753个实验记录（涵盖FCC、BCC、BCC+FCC、BCC+IM四个相）训练的校准XGBoost代理模型。与贝叶斯优化和随机搜索基线相比，完整提示的智能体在描述符空间中对FCC、BCC和BCC+FCC相的重新发现率分别为38%、18%和38%，且其提案比随机搜索更接近实验相流形。消融实验表明，领域先验知识将智能体从对文献密集合金的回忆转向对成分多样性的探索。斯皮尔曼分析证实智能体的推理与经验相分布在统计上一致。这项工作确立了LLM引导的智能体推理作为逆向合金设计中一种原则性、透明且对流形感知的、对无梯度优化的补充方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering high-entropy alloy (HEA) compositions that reliably form a target crystal phase is a high-dimensional inverse design problem that conventional trial-and-error experimentation and forward-only machine learning models cannot efficiently solve. Here we present a ReAct (Reasoning + Acting) LLM agent that autonomously proposes, validates, and iteratively refines HEA compositions by querying a calibrated XGBoost surrogate trained on 4,753 experimental records across four phases (FCC, BCC, BCC+FCC, BCC+IM), achieving 94.66\% accuracy (F1 macro = 0.896). Against Bayesian optimisation (BO) and random search baselines, the full-prompt agent achieves descriptor-space rediscovery rates of 38\%, 18\%, and 38\% for FCC, BCC, and BCC+FCC (Mann--Whitney $p \leq 0.039$), with proposals lying 2.4--22.8$\times$ closer to the experimental phase manifold than random search. An ablation reveals that domain priors shift the agent from landmark-alloy recall toward compositionally diverse exploration -- an uninformed agent scores higher rediscovery by concentrating on literature-dense families, while the full-prompt agent explores underrepresented space (unique ratio 1.0 vs.\ 0.39 for BCC+FCC). These regimes represent distinct criteria: proximity to known literature versus genuine discovery. Spearman analysis confirms agent reasoning is statistically aligned with empirical phase distributions ($\rho = 0.736$, $p = 0.004$ for BCC). This work establishes LLM-guided agentic reasoning as a principled, transparent, and manifold-aware complement to gradient-free optimisation for inverse alloy design.

</details>

---

### 27. [Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction](https://arxiv.org/abs/2603.11125)

**基本信息**

- 🔗 arXiv: [`2603.11125`](https://arxiv.org/abs/2603.11125)
- 👥 作者: Yining Qian, Pengjie Wang, Yixiao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种名为Co-Diffusion的新型深度学习框架，用于药物-靶标亲和力（DTA）预测。这是化学信息学和计算药物发现的核心问题。该框架基于扩散模型（一种生成式大模型）的思想进行构建，并将其应用于分子表示学习和性质预测。这直接与“化学大模型”主题相关，即利用先进的生成式模型（扩散模型）解决化学信息学中的关键预测任务。

**📖 中文摘要**

本文提出了Co-Diffusion，一种新颖的亲和力感知框架，用于可泛化的药物-靶标亲和力（DTA）预测。DTA预测对于虚拟筛选和先导化合物优化至关重要。Co-Diffusion将DTA预测重新定义为约束潜在去噪过程以增强泛化能力。它采用两阶段范式：第一阶段在显式监督目标下对齐药物和靶标嵌入，建立亲和力引导的潜在流形，确保潜在空间反映内在的结合景观；第二阶段引入模态特定的潜在扩散作为随机扰动-去噪正则化器，迫使模型从噪声结构表示中恢复一致的亲和力语义。这种方法有效缓解了生成式DTA模型中常见的重建-回归冲突。理论分析表明，Co-Diffusion最大化了药物结构、蛋白质序列和结合强度的联合似然的变分下界。跨多个基准的大量实验表明，Co-Diffusion显著优于最先进的基线方法，特别是在未见过的分子支架和新蛋白质家族上表现出卓越的零样本泛化能力，为在未探索化学空间中进行计算机药物优先排序开辟了稳健的路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.

</details>

---

### 28. [A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation](https://arxiv.org/abs/2603.11242)

**基本信息**

- 🔗 arXiv: [`2603.11242`](https://arxiv.org/abs/2603.11242)
- 👥 作者: Xiaoan Lang, Fang Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11242.pdf)

**💡 相关性分析**

满足标准2：提出的bfVAE框架和评估工具（FVH-LT, DBSR-LS, LSDI）为构建和评估化学信息学中可能用于分子表示学习的解纠缠模型提供了通用的数据资源和工具。

**📖 中文摘要**

本文提出了一个统一的变分自编码器（VAE）框架（bfVAE），用于生成有效的潜在空间解纠缠，特别适用于表格数据。该框架统一了多种最先进的解纠缠VAE方法，并提出了两种无需真实生成因子即可评估解纠缠有效性的新程序（FVH-LT和DBSR-LS）以及一个总体解纠缠指数（LSDI）。此外，还开发了一种贪婪对齐策略（GAS）以确保解纠缠的鲁棒性和一致性。该工作在表格和图像数据上进行了广泛实验，结果表明bfVAE在解纠缠质量、鲁棒性和信息性潜在维度的低错误发现率方面超越了现有框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FVH-LT and DBSR-LS to summarize the overall effectiveness of a VAE disentanglement method without requiring access to or knowledge of the ground-truth generative factors. To the best of our knowledge, these are the first assessment tools to achieve this. FVH-LT and DBSR-LS also enhance latent space interpretability and provide guidance on more efficient content generation. To ensure robust and consistent disentanglement, we develop a greedy alignment strategy (GAS) that mitigates label switching and aligns latent dimensions across runs to obtain aggregated results. We assess the bfVAE framework and validate FVH-LT, DBSR-LS, and LSDI in extensive experiments on tabular and image data. The results suggest that bfVAE surpasses existing disentangled VAE frameworks in terms of disentanglement quality, robustness, achieving a near-zero false discovery rate for informative latent dimensions, that FVH-LT and DBSR-LS reliably uncover semantically meaningful and domain-relevant latent structures, and that LSDI makes an effective overall quantitative summary on disentanglement effectiveness.

</details>

---

### 29. [A Standardized Framework For Evaluating Gene Expression Generative Models](https://arxiv.org/abs/2603.11244)

**基本信息**

- 🔗 arXiv: [`2603.11244`](https://arxiv.org/abs/2603.11244)
- 👥 作者: Andrea Rubbi, Andrea Giuseppe Di Francesco, Mohammad Lotfollahi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11244.pdf)

**💡 相关性分析**

满足标准2：提出的GGE框架为生成模型（包括可能用于化学或生物分子数据生成的模型）的评估提供了标准化的工具和度量套件，属于重要的数据资源/工具。

**📖 中文摘要**

本文提出了Generated Genetic Expression Evaluator (GGE)，一个用于单细胞基因表达数据生成模型标准化评估的开源Python框架。GGE通过提供一套全面的分布度量（包含明确的计算空间选项）和基于差异表达基因（DEG）分析及扰动效应相关性的生物学动机评估，解决了当前评估实践中指标实现不一致、超参数选择不可比以及缺乏生物学基础度量的问题。该框架支持标准化报告和可复现的基准测试，旨在加速扰动响应预测、细胞身份建模和反事实推理等领域的进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid development of generative models for single-cell gene expression data has created an urgent need for standardised evaluation frameworks. Current evaluation practices suffer from inconsistent metric implementations, incomparable hyperparameter choices, and a lack of biologically-grounded metrics. We present Generated Genetic Expression Evaluator (GGE), an open-source Python framework that addresses these challenges by providing a comprehensive suite of distributional metrics with explicit computation space options and biologically-motivated evaluation through differentially expressed gene (DEG)-focused analysis and perturbation-effect correlation, enabling standardized reporting and reproducible benchmarking. Through extensive analysis of the single-cell generative modeling literature, we identify that no standardized evaluation protocol exists. Methods report incomparable metrics computed in different spaces with different hyperparameters. We demonstrate that metric values vary substantially depending on implementation choices, highlighting the critical need for standardization. GGE enables fair comparison across generative approaches and accelerates progress in perturbation response prediction, cellular identity modeling, and counterfactual inference.

</details>

---

### 30. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：论文核心内容围绕构建一个结合了表达嵌入模型（scGPT）和大语言模型（LLM）的交互式智能体框架，用于单细胞数据的探索和假设生成，直接涉及化学信息学/生物信息学中的大模型（表达嵌入模型和LLM）应用。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个将scGPT表达嵌入与基于BioBERT的语义检索以及LLM介导的解释相统一的可解释框架，用于交互式单细胞发现。该框架通过自动查询分类器将输入路由到不同的分析流程（基因标记评分、语义匹配或混合），并集成了跨60多个基因集的通路活性评分、使用280多个配体-受体对预测相互作用、条件感知比较分析和细胞类型比例估计等模块，所有操作直接在嵌入数据上进行而无需原始计数矩阵。在六个不同的scRNA-seq数据集上的基准测试表明，ELISA在细胞类型检索方面显著优于CellWhisperer，并能复现已发表的生物学发现，在通路对齐和主题覆盖方面接近完美。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 31. [Proof-Carrying Materials: Falsifiable Safety Certificates for Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2603.12183)

**基本信息**

- 🔗 arXiv: [`2603.12183`](https://arxiv.org/abs/2603.12183)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12183.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容是利用形式化方法和大模型（风险模型）来验证和提升用于材料发现的机器学习原子间势（MLIP）的可靠性，直接涉及化学信息学中的大模型（MLIP）以及为其提供安全评估的工具/框架。

**📖 中文摘要**

本文提出了Proof-Carrying Materials (PCM)，一个为机器学习原子间势（MLIP）提供可证伪安全证书的框架。PCM通过三个阶段工作：跨组成空间的对抗性证伪、具有95%置信区间的引导包络细化以及Lean 4形式化验证。该工作审计了CHGNet、TensorNet和MACE等MLIP，揭示了架构特定的盲点，并训练了一个风险模型来预测未见材料的失败。在一个热电材料筛选的案例研究中，经过PCM审计的方案发现了62种被单一MLIP筛选漏掉的稳定材料，将发现率提高了25%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learned interatomic potentials (MLIPs) are deployed for high-throughput materials screening without formal reliability guarantees. We show that a single MLIP used as a stability filter misses 93% of density functional theory (DFT)-stable materials (recall 0.07) on a 25,000-material benchmark. Proof-Carrying Materials (PCM) closes this gap through three stages: adversarial falsification across compositional space, bootstrap envelope refinement with 95% confidence intervals, and Lean 4 formal certification. Auditing CHGNet, TensorNet and MACE reveals architecture-specific blind spots with near-zero pairwise error correlations (r <= 0.13; n = 5,000), confirmed by independent Quantum ESPRESSO validation (20/20 converged; median DFT/CHGNet force ratio 12x). A risk model trained on PCM-discovered features predicts failures on unseen materials (AUC-ROC = 0.938 +/- 0.004) and transfers across architectures (cross-MLIP AUC-ROC ~ 0.70; feature importance r = 0.877). In a thermoelectric screening case study, PCM-audited protocols discover 62 additional stable materials missed by single-MLIP screening - a 25% improvement in discovery yield.

</details>

---

### 32. [drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network](https://arxiv.org/abs/2405.08979)

**基本信息**

- 🔗 arXiv: [`2405.08979`](https://arxiv.org/abs/2405.08979)
- 👥 作者: Yoshitaka Inoue, Hunmin Lee, Tianfan Fu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08979.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是构建一个基于图神经网络和大规模生物医学知识（药物-基因-细胞系网络）的深度学习模型，用于药物响应预测和生物标志物发现，属于化学信息学中利用图模型进行分子性质预测和关系推理的范畴。

**📖 中文摘要**

本文提出了drGT，一个利用注意力系数（ACs）预测药物敏感性并辅助生物标志物识别的图深度学习模型。drGT利用从药物、基因和细胞系响应中提取的关系构建的异质图进行训练和评估。模型在Sanger GDSC、NCI60和Broad CTRP等主要基准数据集上进行了评估，在随机拆分、未见药物和未见细胞线设置下均取得了有竞争力的性能，同时提供了可解释性。通过文本挖掘PubMed摘要，验证了模型高系数基因与特定药物共现的文献支持。此外，还利用ACs通过富集分析识别每种药物影响的生物过程，从而增强了生物学可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A challenge in drug response prediction is result interpretation compared to established knowledge. drGT is a graph deep learning model that predicts sensitivity and aids in biomarker identification using attention coefficients (ACs). drGT leverages a heterogeneous graph composed of relationships drawn from drugs, genes, and cell line responses. The model is trained and evaluated using major benchmark datasets: Sanger GDSC, NCI60, and Broad CTRP, which cover a wide range of drugs and cancer cell lines. drGT demonstrates AUROC of up to 94.5% under random splitting, 84.4% for unseen drugs, and 70.6% for unseen cell lines, comparable to existing benchmark methods while also providing interpretability. Regarding interpretability, we review drug-gene co-occurrences by text-mining PubMed abstracts for high-coefficient genes mentioning particular drugs. Across 976 drugs from NCI60 with known drug-target interactions (DTIs), model predictions utilized both known DTIs (36.9%) as well as additional predictive associations, many supported by literature. In addition, we compare the drug-gene associations identified by drGT with those from an established DTI prediction model and find that 63.67% are supported by either PubMed literature or predictions from the DTI model. Further, we describe the utilization of ACs to identify affected biological processes by each drug via enrichment analyses, thereby enhancing biological interpretability. Code is available at this https URL .

</details>

---

### 33. [Using LLM-Generated Draft Replies to Support Human Experts in Responding to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of Industrial AI](https://arxiv.org/abs/2412.12732)

**基本信息**

- 🔗 arXiv: [`2412.12732`](https://arxiv.org/abs/2412.12732)
- 👥 作者: Tita Alissa Bach, Aleksandar Babic, Narae Park 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.12732.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是评估大型语言模型（LLM）在专业领域（航运业）中作为人类专家辅助工具的实际应用、效用和局限性，直接涉及大模型（LLM）在工业场景中的应用研究。

**📖 中文摘要**

本文通过一个真实世界的案例研究，探讨了在航运业中利用LLM生成草稿回复来支持人类专家处理利益相关者查询的效用。研究包括初步研究（观察和访谈）、调查和文本相似性分析。研究发现，虽然LLM草稿可以简化工作流程，但通常需要进行重大修改才能满足海事通信的特定需求。尽管LLM在没有人工监督的情况下尚未成熟到可用于安全关键应用，但它们可以作为有价值的增强工具。最终决策权必须保留在人类专家手中。通过利用人类和LLM的优势，促进人机协作，行业可以在保持高质量和精确度的同时提高效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

</details>

---

### 34. [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177)

**基本信息**

- 🔗 arXiv: [`2501.15177`](https://arxiv.org/abs/2501.15177)
- 👥 作者: Yi Su, Jisheng Bai, Qisheng Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.15177.pdf)

**💡 相关性分析**

满足标准3：论文是专门针对音频-语言模型（ALMs）这一特定类型大模型的系统性综述，涵盖了其基础、发展和未来趋势，属于针对大模型主题的综述类论文。

**📖 中文摘要**

本文对音频-语言模型（ALMs）进行了首次系统性综述。ALMs在配对音频-文本数据上训练，旨在处理、理解和推理以音频为中心的多模态内容。与使用预定义标签的传统监督方法不同，ALMs利用自然语言监督来更好地处理具有多个重叠事件的复杂真实世界音频场景。论文提出了三个主要贡献：（1）从通用音频角度全面覆盖了跨语音、音乐和声音的ALM工作；（2）建立了ALM基础（包括模型架构和训练目标）的统一分类法；（3）建立了一个捕捉不同研究方面相互促进和制约的研究图景，有助于总结评估、局限性、关注点和有前景的方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified taxonomy of ALM foundations, including model architectures and training objectives; (3) establishment of a research landscape capturing mutual promotion and constraints among different research aspects, aiding in summarizing evaluations, limitations, concerns and promising directions. Our review contributes to helping researchers understand the development of existing technologies and future trends, while also providing valuable references for implementation in practical applications.

</details>

---

### 35. [GTM: A General Time-series Model for Enhanced Representation Learning of Time-Series Data](https://arxiv.org/abs/2502.03264)

**基本信息**

- 🔗 arXiv: [`2502.03264`](https://arxiv.org/abs/2502.03264)
- 👥 作者: Cheng He, Xu Huang, Gangwei Jiang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03264.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是提出一种新型的、生成任务无关的通用时间序列大模型（GTM），涉及新颖的注意力机制和预训练策略，直接围绕大模型（特别是时间序列领域）的架构设计和训练方法展开。

**📖 中文摘要**

本文提出了通用时间序列模型（GTM），通过一种新颖的频域注意力机制（捕捉时间粒度感知特征）和一种结合了重构与自回归目标的统一预训练策略（通过混合掩码机制实现）来推进时间序列的表示学习。GTM被确立为第一个用于时间序列分析的生成任务无关模型，无需任何任务特定修改即可无缝适应各种生成任务。大量实验表明，GTM在各种生成任务上始终优于SOTA模型，并且通过最小化适应实现了强大的分类结果。此外，GTM表现出清晰的缩放行为，随着模型大小和预训练数据的增加，准确性得到提高。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite recent progress in time-series foundation models, challenges persist in improving representation learning and adapting to diverse downstream tasks. We introduce a General Time-series Model (GTM), which advances representation learning via a novel frequency-domain attention mechanism that captures time-granularity-aware features, an aspect underexplored in prior research. We further propose a novel pre-training strategy that unifies reconstruction and autoregressive objectives through a hybrid masking mechanism. Our pre-training strategy, combined with 2D positional encoding and span shuffling, enhances the robustness and generalization of representations. GTM is established as the first generative-task-agnostic model for time-series analysis, enabling seamless adaptation to various generative tasks without any task-specific modifications. Extensive experiments demonstrate that GTM consistently outperforms SOTA models on various generative tasks and achieves strong classification results with minimal adaptation. Furthermore, GTM exhibits clear scaling behavior, with accuracy improving as model size and pre-training data increase.

</details>

---

### 36. [HOG-Diff: Higher-Order Guided Diffusion for Graph Generation](https://arxiv.org/abs/2502.04308)

**基本信息**

- 🔗 arXiv: [`2502.04308`](https://arxiv.org/abs/2502.04308)
- 👥 作者: Yiming Huang, Tolga Birdal
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.04308.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是提出一种新的基于扩散模型的图生成框架（HOG-Diff），该框架 explicitly 利用高阶拓扑信息来引导生成过程，属于图生成大模型的研究范畴，与化学信息学中分子图生成高度相关。

**📖 中文摘要**

本文提出了高阶引导扩散（HOG-Diff），一个用于图生成的原理性框架，通过扩散桥逐步生成具有固有拓扑结构的合理图。HOG-Diff遵循由高阶拓扑引导的从粗到细的生成课程。作者进一步证明该模型比经典扩散框架具有更强的理论保证。在跨越不同领域的八个图生成基准测试上的大量实验表明，该方法具有可扩展性，并且在成对和高阶拓扑度量上均表现出优越性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation is a critical yet challenging task, as empirical analyses require a deep understanding of complex, non-Euclidean structures. Diffusion models have recently made significant advances in graph generation, but these models are typically adapted from image generation frameworks and overlook inherent higher-order topology, limiting their ability to capture graph topology. In this work, we propose Higher-order Guided Diffusion (HOG-Diff), a principled framework that progressively generates plausible graphs with inherent topological structures. HOG-Diff follows a coarse-to-fine generation curriculum, guided by higher-order topology and implemented via diffusion bridges. We further prove that our model admits stronger theoretical guarantees than classical diffusion frameworks. Extensive experiments across eight graph generation benchmarks, spanning diverse domains and including large-scale settings, demonstrate the scalability of our method and its superior performance on both pairwise and higher-order topological metrics. Our project page is available \href{ this https URL }{here}.

</details>

---

### 37. [Riemannian Variational Flow Matching for Material and Protein Design](https://arxiv.org/abs/2502.12981)

**基本信息**

- 🔗 arXiv: [`2502.12981`](https://arxiv.org/abs/2502.12981)
- 👥 作者: Olga Zaghen, Floor Eijkelboom, Alison Pouplin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.12981.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是提出一种新的用于流形（如分子构象空间）上生成建模的几何深度学习框架（RG-VFM），直接涉及用于分子和材料设计的生成式大模型方法。

**📖 中文摘要**

本文提出了黎曼高斯变分流匹配（RG-VFM），一种用于流形上生成建模的变分流匹配（VFM）的几何扩展。该工作基于具有闭式测地线的黎曼流形上的黎曼高斯分布推导了变分流匹配目标。作者形式化分析了该模型与黎曼流匹配（RFM）的关系，揭示了RFM目标缺乏一个曲率相关的惩罚项，而该惩罚项通过雅可比场自然编码在RG-VFM中。在合成球形和双曲基准以及材料和蛋白质生成的真实世界任务上的实验表明，RG-VFM能更有效地捕捉流形结构，并比欧几里得和基于速度的基线方法提高下游性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Riemannian Gaussian Variational Flow Matching (RG-VFM), a geometric extension of Variational Flow Matching (VFM) for generative modeling on manifolds. Motivated by the benefits of VFM, we derive a variational flow matching objective for manifolds with closed-form geodesics based on Riemannian Gaussian distributions. Crucially, in Euclidean space, predicting endpoints (VFM), velocities (FM), or noise (diffusion) is largely equivalent due to affine interpolations. However, on curved manifolds this equivalence breaks down. We formally analyze the relationship between our model and Riemannian Flow Matching (RFM), revealing that the RFM objective lacks a curvature-dependent penalty -- encoded via Jacobi fields -- that is naturally present in RG-VFM. Based on this relationship, we hypothesize that endpoint prediction provides a stronger learning signal by directly minimizing geodesic distances. Experiments on synthetic spherical and hyperbolic benchmarks, as well as real-world tasks in material and protein generation, demonstrate that RG-VFM more effectively captures manifold structure and improves downstream performance over Euclidean and velocity-based baselines. Code available at this https URL .

</details>

---

### 38. [OrchMLLM: Orchestrate Multimodal Data with Batch Post-Balancing to Accelerate Multimodal Large Language Model Training](https://arxiv.org/abs/2503.23830)

**基本信息**

- 🔗 arXiv: [`2503.23830`](https://arxiv.org/abs/2503.23830)
- 👥 作者: Yijie Zheng, Bangjun Xiao, Lei Shi 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.23830.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是解决多模态大语言模型（MLLM）训练中的效率和可扩展性挑战，提出了新的训练框架和调度策略，直接围绕大模型（特别是多模态大模型）的训练系统优化展开。

**📖 中文摘要**

本文介绍了OrchMLLM，一个旨在缓解多模态大语言模型（MLLM）训练中因模态组成不连贯而导致的低效问题的综合框架。首先，提出了批处理后平衡调度器技术，以消除顺序数据中的小批量不平衡。此外，将MLLM全局协调器集成到训练框架中，以协调多模态数据并解决模态组成不连贯引起的问题。评估显示，OrchMLLM在训练具有三种模态的840亿参数MLLM时，在2560个H100 GPU上实现了41.6%的模型FLOPs利用率（MFU），吞吐量比Megatron-LM高出3.1倍。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal large language models (MLLMs), such as GPT-4o, are garnering significant attention. During the exploration of MLLM training, we identified Modality Composition Incoherence, a phenomenon that the proportion of a certain modality varies dramatically across different examples. It exacerbates the challenges of addressing mini-batch imbalances, which lead to uneven GPU utilization between Data Parallel (DP) instances and severely degrades the efficiency and scalability of MLLM training, ultimately affecting training speed and hindering further research on MLLMs. To address these challenges, we introduce OrchMLLM, a comprehensive framework designed to mitigate the inefficiencies in MLLM training caused by Modality Composition Incoherence. First, we propose Batch Post-Balancing Dispatcher, a technique that efficiently eliminates mini-batch imbalances in sequential data. Additionally, we integrate MLLM Global Orchestrator into the training framework to orchestrate multimodal data and tackle the issues arising from Modality Composition Incoherence. We evaluate OrchMLLM across various MLLM sizes, demonstrating its efficiency and scalability. Experimental results reveal that OrchMLLM achieves a Model FLOPs Utilization (MFU) of $41.6\%$ when training an 84B MLLM with three modalities on $2560$ H100 GPUs, outperforming Megatron-LM by up to $3.1\times$ in throughput.

</details>

---

### 39. [Tuning-Free LLM Can Build A Strong Recommender Under Sparse Connectivity And Knowledge Gap Via Extracting Intent](https://arxiv.org/abs/2505.10900)

**基本信息**

- 🔗 arXiv: [`2505.10900`](https://arxiv.org/abs/2505.10900)
- 👥 作者: Wenqing Zheng, Noah Fatsi, Daniel Barcklow 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10900.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是构建一个结合了大型语言模型（LLM，用于意图提取）、知识图谱和图神经网络（GNN）的推荐系统框架，直接涉及大模型（LLM）在信息检索和推理任务中的应用。

**📖 中文摘要**

本文提出了LLM-based Intent Knowledge Graph Recommender (IKGR)，一个新颖的推荐框架，它构建了一个以意图为中心的知识图谱，其中用户和物品都通过一个免调优、RAG引导的LLM流程提取的意图节点显式连接。通过将意图锚定在外部知识源和用户画像中，IKGR规范地表示了用户寻求什么和物品满足什么作为一等实体。为了缓解稀疏性，进一步引入了相互意图连接致密化策略，该策略缩短了用户和长尾物品之间的语义路径，而无需跨图融合。最后，在意图增强的图谱上采用轻量级GNN层来生成低延迟的推荐信号。在公共和企业数据集上的大量实验表明，IKGR始终优于强基线模型，特别是在冷启动和长尾数据切片上，同时通过完全离线的LLM流程保持高效。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in recommendation with large language models (LLMs) often rely on either commonsense augmentation at the item-category level or implicit intent modeling on existing knowledge graphs. However, such approaches struggle to capture grounded user intents and to handle sparsity and cold-start scenarios. In this work, we present LLM-based Intent Knowledge Graph Recommender (IKGR), a novel framework that constructs an intent-centric knowledge graph where both users and items are explicitly linked to intent nodes extracted by a tuning-free, RAG-guided LLM pipeline. By grounding intents in external knowledge sources and user profiles, IKGR canonically represents what a user seeks and what an item satisfies as first-class entities. To alleviate sparsity, we further introduce a mutual-intent connectivity densification strategy, which shortens semantic paths between users and long-tail items without requiring cross-graph fusion. Finally, a lightweight GNN layer is employed on top of the intent-enhanced graph to produce recommendation signals with low latency. Extensive experiments on public and enterprise datasets demonstrate that IKGR consistently outperforms strong baselines, particularly on cold-start and long-tail slices, while remaining efficient through a fully offline LLM pipeline.

</details>

---

### 40. [LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models](https://arxiv.org/abs/2505.19240)

**基本信息**

- 🔗 arXiv: [`2505.19240`](https://arxiv.org/abs/2505.19240)
- 👥 作者: Aida Kostikova, Zhipin Wang, Deidamea Bajri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19240.pdf)

**💡 相关性分析**

满足标准3：这是一篇专门针对大型语言模型（作为“化学大模型”的上位概念）研究趋势的综述论文，其数据驱动的方法和对研究主题演变的讨论，为理解化学领域大模型的发展、面临的挑战（如幻觉、泛化）和未来方向提供了重要的宏观视角和背景知识。

**📖 中文摘要**

这篇论文是一项关于大型语言模型（LLM）局限性研究的数据驱动综述。它通过半自动化的方法，系统性地回顾了从2022年到2025年初关于LLM局限性的研究。论文从大量ACL和arXiv论文中识别出14,648篇相关论文，并分析了研究趋势，例如推理、泛化、幻觉、偏见和安全性等主题的演变。虽然论文主题是LLM的局限性，但其作为一项大规模、系统性的综述，为理解“化学大模型”等AI模型的发展、能力边界和潜在风险提供了重要的背景知识和讨论框架。它提供了一个量化视角来审视AI模型研究领域的演变，这与关注主题中“化学大模型”的宏观发展脉络和未来展望高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains the most studied limitation, followed by generalization, hallucination, bias, and security. The distribution of topics in the ACL dataset stays relatively stable over time, while arXiv shifts toward security risks, alignment, hallucinations, knowledge editing, and multimodality. We offer a quantitative view of trends in LLLMs research and release a dataset of annotated abstracts and a validated methodology, available at: this https URL .

</details>

---

### 41. [Can Theoretical Physics Research Benefit from Language Agents?](https://arxiv.org/abs/2506.06214)

**基本信息**

- 🔗 arXiv: [`2506.06214`](https://arxiv.org/abs/2506.06214)
- 👥 作者: Sirui Lu, Zhijing Jin, Terry Jingchen Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06214.pdf)

**💡 相关性分析**

满足标准3：论文虽然以物理学为例，但其核心是关于如何为特定科学领域构建专业化、可验证的AI研究智能体的重要讨论和展望。这直接映射到“化学大模型”的研究目标，即开发能够进行可靠化学推理和发现的领域专用AI模型。论文提出的专业化训练、验证框架等思路，对化学信息学领域的大模型发展具有重要的借鉴和启发意义。

**📖 中文摘要**

这篇论文探讨了语言智能体（Language Agents）在理论物理学研究中的应用潜力与当前局限。文章指出，尽管当前大语言模型在数学推理和代码生成方面表现出色，但在物理直觉、约束满足和可靠推理方面存在关键差距。作者认为，要在真实的物理研究中发挥作用，AI智能体需要经过领域专业化训练，并配备物理感知的验证工具。论文呼吁物理和AI社区合作，开发包含物理推理模式的专用训练数据集、捕捉物理推理质量的奖励信号以及编码基本原理的验证框架。虽然主题是物理学，但其核心论点是关于如何为特定科学领域（如化学）构建专业化、可验证的AI研究智能体，这与“化学大模型”的研究目标（构建用于化学发现的可靠AI模型）在方法论和愿景上高度一致。

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

满足标准1：论文的核心研究内容直接展示了大型语言模型（作为“化学大模型”的一种基础架构）在科学计算和复杂系统推理方面的能力。这种从数据序列中学习并预测物理/化学系统动态的能力，是“化学大模型”和“质谱结构推理”等任务的核心。论文为理解大模型如何从数据中学习科学规律提供了重要案例。

**📖 中文摘要**

这篇论文展示了仅通过文本训练的大型语言模型（LLMs）能够零样本外推偏微分方程（PDE）的时空动力学。研究证明，LLMs可以在没有微调或自然语言提示的情况下，仅从离散化的PDE解中准确预测未来的时空状态。预测准确性随上下文长度增加而提高，并表现出与经典有限差分求解器类似的误差累积规律。作者进一步分析了LLMs处理PDE解的内部机制，揭示了一个三阶段的上下文学习过程：从语法模式模仿开始，经过探索性的高熵阶段，最终形成自信的、基于数值的预测。这项研究揭示了纯文本训练的通用大模型在理解和推理复杂科学计算问题（如微分方程动力学）方面涌现出的强大能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated emergent in-context learning (ICL) capabilities across a range of tasks, including zero-shot time-series forecasting. We show that text-trained foundation models can accurately extrapolate spatiotemporal dynamics from discretized partial differential equation (PDE) solutions without fine-tuning or natural language prompting. Predictive accuracy improves with longer temporal contexts but degrades at finer spatial discretizations. In multi-step rollouts, where the model recursively predicts future spatial states over multiple time steps, errors grow algebraically with the time horizon, reminiscent of global error accumulation in classical finite-difference solvers. We interpret these trends as in-context neural scaling laws, where prediction quality varies predictably with both context length and output length. To better understand how LLMs are able to internally process PDE solutions so as to accurately roll them out, we analyze token-level output distributions and uncover a consistent three-stage ICL progression: beginning with syntactic pattern imitation, transitioning through an exploratory high-entropy phase, and culminating in confident, numerically grounded predictions.

</details>

---

### 43. [From Next Token Prediction to (STRIPS) World Models](https://arxiv.org/abs/2509.13389)

**基本信息**

- 🔗 arXiv: [`2509.13389`](https://arxiv.org/abs/2509.13389)
- 👥 作者: Carlos Núñez-Molina, Vicenç Gómez, Hector Geffner
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.13389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索基于下一个词预测的大语言模型学习结构化世界模型和规划能力的根本机制。这种从序列数据中推断出可操作的动作模型和规划的能力，是高级“化学大模型”实现自动化合成设计、反应预测等任务所需的核心能力之一。研究为此提供了理论基础和架构探索。

**📖 中文摘要**

这篇论文研究下一个词预测（Next-Token Prediction）能否产生真正支持规划的世界模型。研究在一个受控的符号设置中进行，从动作轨迹中学习命题STRIPS动作模型，并可以精确评估正确性。论文引入了两种架构：一种是基于理论结果与Transformer形式语言结构对齐的STRIPS Transformer；另一种是没有显式符号结构的标准Transformer。评估表明，两种方法都可以用于生成支持规划的模型。这项研究探讨了大语言模型（基于下一个词预测）学习结构化世界表示和规划能力的根本机制，这对于构建能够进行化学合成规划或分子设计推理的“化学大模型”具有基础性意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study whether next-token prediction can yield world models that truly support planning, in a controlled symbolic setting where propositional STRIPS action models are learned from action traces alone and correctness can be evaluated exactly. We introduce two architectures. The first is the STRIPS Transformer, a symbolically aligned model grounded in theoretical results linking transformers and the formal language structure of STRIPS domains. The second is a standard transformer architecture without explicit symbolic structure built in, for which we study different positional encoding schemes and attention aggregation mechanisms. We evaluate both architectures on five classical planning domains, measuring training accuracy, generalization, and planning performance across domains and problem sizes. Interestingly, both approaches can be used to produce models that support planning with off-the-shelf STRIPS planners over exponentially many unseen initial states and goals. Although the STRIPS Transformer incorporates a strong symbolic inductive bias, it is harder to optimize and requires larger datasets to generalize reliably. In contrast, a standard transformer with stick-breaking attention achieves near-perfect training accuracy and strong generalization. Finally, standard transformers without stick-breaking attention do not generalize to long traces, whereas a symbolic STRIPS model extracted from a transformer trained on shorter traces does.

</details>

---

### 44. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是构建和评估一个能够自主进行科学探索（包括分析、假设、实验、写作）的AI智能体系统。这代表了“化学大模型”或“AI for Science”发展的一个前沿方向和具体实例。同时，论文也对这类系统的当前能力、局限性和风险进行了全面的讨论和展望，属于相关主题的重要进展评述。

**📖 中文摘要**

这篇论文介绍了Jr. AI Scientist，一个最先进的自主AI科学家系统，它模拟了新手学生研究人员的核心研究工作流程：在给定人类导师的基线论文后，系统分析其局限性，提出改进的新假设，进行迭代实验直到取得改进，并撰写结果论文。论文通过实验证明，该系统能够基于真实的NeurIPS、IJCV和ICLR工作，通过提出和实现新方法生成新的研究论文。评估包括使用AI评审员进行自动评估、作者主导的评估以及向专注于AI驱动贡献的Agents4Science会议投稿。研究旨在澄清当前AI科学家系统的能力和局限性，并报告了开发过程中识别的各种风险。

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

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一种从质谱数据中从头推断分子结构的生成模型。

**📖 中文摘要**

这篇论文提出了一种名为MSFlow的新型生成模型，用于解决质谱分析中的一个核心挑战：从质谱数据中从头推断分子结构。该模型采用两阶段编码器-解码器流程匹配架构。第一阶段使用一个受化学式限制的Transformer模型，将质谱编码到一个连续且富含化学信息的嵌入空间中。第二阶段训练一个解码器流程匹配模型，从质谱的潜在嵌入中重建分子。作者通过消融研究证明了使用信息保留的分子描述符对编码质谱的重要性，并论证了其离散流基解码器的优势。严格的评估表明，MSFlow能够将高达45%的分子质谱准确翻译成相应的分子表示，这比当前最先进方法的性能提升了高达14倍。这项工作直接针对“质谱结构推理”这一核心主题，为小分子的结构解析提供了最先进的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

</details>

---

### 46. [Beyond Explainable AI (XAI): An Overdue Paradigm Shift and Post-XAI Research Directions](https://arxiv.org/abs/2602.24176)

**基本信息**

- 🔗 arXiv: [`2602.24176`](https://arxiv.org/abs/2602.24176)
- 👥 作者: Saleh Afroogh, Seyd Ishtiaque Ahmed, Petra Ahrweiler 等49人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.24176.pdf)

**💡 相关性分析**

满足标准3：论文是一篇批判性综述，不仅分析了当前XAI的局限，还提出了超越XAI的新研究范式。其中关于模型可靠性、认证、交互式AI和以模型为中心的分析等讨论，对于“化学大模型”的可信度评估、与专家协作以及内部机制理解等主题具有重要的相关性和前瞻性。

**📖 中文摘要**

本研究对可解释人工智能（XAI）方法进行了跨学科审视，重点关注深度神经网络（DNN）和大语言模型（LLM），并指出了当前XAI在实证和概念上的局限性。作者讨论了源于更深层根源（即两个悖论、两个概念混淆和五个错误假设）的关键症状。这些XAI研究领域内的根本问题揭示了三个见解：在实验上，XAI存在显著缺陷；在概念上，它是悖论性的；在实践上，进一步尝试改革这个悖论性的XAI可能会加剧其混乱——这要求根本性的转变和新的研究方向。为了超越XAI的局限性，作者提出了一个四管齐下的综合范式转变，朝着可靠和经过认证的AI发展。这四个组成部分包括：以验证为重点的交互式AI（IAI）、为奠定严格科学基础的AI认识论、为特定用户社区创建情境感知系统的用户可感知AI，以及用于忠实技术分析的以模型为中心的可解释性——共同为后XAI研究提供了全面的方向。虽然论文主要批评XAI，但其提出的新研究方向（如IAI、模型中心的可解释性）直接关系到如何构建更可靠、可认证的AI系统，这对“化学大模型”的开发和评估具有重要指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study provides a cross-disciplinary examination of Explainable Artificial Intelligence (XAI) approaches-focusing on deep neural networks (DNNs) and large language models (LLMs)-and identifies empirical and conceptual limitations in current XAI. We discuss critical symptoms that stem from deeper root causes (i.e., two paradoxes, two conceptual confusions, and five false assumptions). These fundamental problems within the current XAI research field reveal three insights: experimentally, XAI exhibits significant flaws; conceptually, it is paradoxical; and pragmatically, further attempts to reform the paradoxical XAI might exacerbate its confusion-demanding fundamental shifts and new research directions. To move beyond XAI's limitations, we propose a four-pronged synthesized paradigm shift toward reliable and certified AI development. These four components include: verification-focused Interactive AI (IAI) to establish scientific community protocols for certifying AI system performance rather than attempting post-hoc explanations, AI Epistemology for rigorous scientific foundations, User-Sensible AI to create context-aware systems tailored to specific user communities, and Model-Centered Interpretability for faithful technical analysis-together offering comprehensive post-XAI research directions.

</details>

---

### 47. [On the Value of Tokeniser Pretraining in Physics Foundation Models](https://arxiv.org/abs/2603.05598)

**基本信息**

- 🔗 arXiv: [`2603.05598`](https://arxiv.org/abs/2603.05598)
- 👥 作者: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05598.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及基础模型的架构设计和表示学习，特别是分词器的预训练策略，这与构建和优化“化学大模型”所面临的模型效率、表示能力等核心挑战直接相关。

**📖 中文摘要**

本文研究了分词器预训练对物理仿真基础模型精度和效率的影响。现代高分辨率模拟产生了跨越不同物理体系和尺度的海量数据。训练基础模型来学习这些数据背后的动力学，使得对复杂多物理现象（尤其是在数据有限的情况下）的建模成为可能。新兴的物理基础模型通常旨在联合学习两个任务：(i) 从高分辨率时空数据中提取紧凑表示，以及 (ii) 捕捉支配性的物理动力学。然而，同时从头开始学习这两个任务可能会阻碍任一过程的有效性。作者表明，在训练动力学模型之前，使用自编码目标对分词器进行预训练，可以增强物理仿真的计算效率。值得注意的是，这种益处的程度取决于领域对齐：在与仿真任务相同的物理系统上进行预训练能带来最大的改进，而在其他系统上进行预训练则提供适度的收益。据作者所知，这是首次对物理基础模型的分词器预训练进行系统研究。这项工作为训练高效的物理仿真器提供了实用指导，并强调了策略性预训练数据选择的重要性。虽然论文主要关注物理仿真，但其核心方法——使用预训练的分词器（一种特定类型的模型组件）来提升下游任务性能——与“化学大模型”中模型架构、表示学习和效率优化的主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an autoencoding objective prior to training the dynamics model enhances computational efficiency for physics emulation. Notably, the magnitude of this benefit depends on domain alignment: pretraining on the same physical system as the emulation task yields the largest improvements, while pretraining on other systems provides moderate gains. In-domain pretraining reduces VRMSE by 64% after 10,500 training steps compared to training from scratch. To our knowledge, this is the first systematic investigation of tokeniser pretraining for physics foundation models. We further introduce flexible spatiotemporal compression operations that extend causal convolutions to support runtime-adjustable compression ratios, enabling efficient adaptation to diverse downstream tasks. Our findings provide practical guidance for training efficient physics emulators and highlight the importance of strategic pretraining data selection.

</details>

---

### 48. [Computational Pathology in the Era of Emerging Foundation and Agentic AI -- International Expert Perspectives on Clinical Integration and Translational Readiness](https://arxiv.org/abs/2603.05884)

**基本信息**

- 🔗 arXiv: [`2603.05884`](https://arxiv.org/abs/2603.05884)
- 👥 作者: Qian Da, Yijiang Chen, Min Ju 等28人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05884.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对基础模型和智能体AI在专业领域（病理学）应用的综述，其中包含了对模型评估、临床整合、技术成熟度和监管等重要议题的深入讨论，这些讨论与“化学大模型”的开发、评估和实际应用所面临的挑战高度相关，提供了重要的跨领域见解。

**📖 中文摘要**

这篇综述文章探讨了在基础模型和智能体AI兴起的时代，计算病理学如何向临床整合和转化准备迈进。文章汇集了国际专家的观点，对当前AI系统在患者护理环境中的能力和采用障碍进行了实践性评估。它超越了现有关于技术架构和比较性能的讨论，通过将可部署的临床相关性与下游分析能力及其技术成熟度、操作准备度、经济和监管背景联系起来，考虑了这些新兴AI系统如何负责任地整合到医疗实践中。文章特别关注了预测任务（如诊断、预后和治疗反应）中基准数据集所报告的性能提升，以及由此引发的临床应用热情。虽然主题是病理学，但文章深入讨论了基础模型和智能体AI的整合、评估、部署挑战和监管考虑，这些讨论对于任何领域（包括化学信息学）中构建和应用“化学大模型”都具有普遍的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent breakthroughs in artificial intelligence through foundation models and agents have accelerated the evolution of computational pathology. Demonstrated performance gains reported across academia in benchmarking datasets in predictive tasks such as diagnosis, prognosis, and treatment response have ignited substantial enthusiasm for clinical application. Despite this development momentum, real world adoption has lagged, as implementation faces economic, technical, and administrative challenges. Beyond existing discussions of technical architectures and comparative performance, this review considers how these emerging AI systems can be responsibly integrated into medical practice by connecting deployable clinical relevance with downstream analytical capabilities and their technical maturity, operational readiness, and economic and regulatory context. Drawing on perspectives from an international group, we provide a practical assessment of current capabilities and barriers to adoption in patient care settings.

</details>

---

### 49. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种新的潜在推理框架LatentChem，旨在改进化学大语言模型的推理效率和性能。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）主要依赖显式自然语言思维链（CoT）进行复杂推理的局限性。作者认为，化学推理本质上是连续和结构化的，将其强制编码为离散的语言标记会导致表示上的不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续的潜在空间中直接执行多步推理，而仅在最终输出时生成语言。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，而且在计算上具有优势。在多个化学推理基准测试中，LatentChem相对于基于CoT的基线模型取得了显著优势，同时实现了显著的推理加速。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 50. [Semantics-Aware Caching for Concept Learning](https://arxiv.org/abs/2603.06506)

**基本信息**

- 🔗 arXiv: [`2603.06506`](https://arxiv.org/abs/2603.06506)
- 👥 作者: Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06506.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种语义感知缓存方法，作为一种优化工具，可以显著提升概念学习（一种知识推理任务）中实例检索的效率。这种工具对于构建需要高效访问和推理大规模化学知识库的“化学大模型”具有直接的应用价值，提供了可用的技术资源。

**📖 中文摘要**

概念学习是一种在描述逻辑知识库上运行的监督机器学习形式。最先进的概念学习者通常依赖于在可数无限概念空间中的迭代搜索。在每次迭代中，它们检索候选解决方案的实例以选择用于下一次迭代的最佳概念。虽然简单的学习问题可能只需要几十次实例检索调用就能找到合适的解决方案，但复杂的学习问题可能需要数千次调用。为了缓解由此产生的运行时挑战，本文提出了一种语义感知缓存方法。该缓存本质上是一个子包含感知映射，通过清晰的集合操作将概念链接到一组实例。在5个数据集、4个符号推理器、1个神经符号推理器和5种流行分页策略上的实验表明，该缓存可以将概念检索和概念学习的运行时减少一个数量级，并且对符号和神经符号推理器都有效。这项工作通过优化底层推理过程，提升了概念学习（一种知识表示和推理任务）的效率，这对于构建能够处理复杂化学知识的“化学大模型”具有支撑作用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

</details>

---

### 51. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发用于化学模拟的机器学习模型（MLIPs），并引入了专家混合（MoE）这一先进的机器学习架构来提升其性能，与“化学大模型”主题高度相关。

**📖 中文摘要**

本文系统地开发了用于机器学习原子间势（MLIPs）的专家混合（MoE）和线性专家混合（MoLE）架构。MLIPs能够实现精确的大规模原子模拟，但高效提升其表达能力仍然是一个挑战。作者分析了路由策略和专家设计的影响，表明稀疏激活与共享专家相结合能带来显著的性能提升。当存在共享专家时，非线性MoE公式优于MoLE，这突显了非线性专家专业化的重要性。此外，基于元素的（element-wise）路由策略持续优于基于构型的（configuration-level）路由。由此产生的基于元素的MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、具有化学可解释性的专家专业化，表明该模型有效地捕捉了元素特定的化学特征，用于精确的原子间建模。这项工作通过先进的模型架构（MoE）提升了化学模拟中关键工具（MLIPs）的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 52. [A Variational Latent Equilibrium for Learning in Neuronal Circuits](https://arxiv.org/abs/2603.09600)

**基本信息**

- 🔗 arXiv: [`2603.09600`](https://arxiv.org/abs/2603.09600)
- 👥 作者: Simon Brandt, Paul Haider, Walter Senn 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09600.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个统一的、生物学上更合理的深度学习理论框架，旨在替代BPTT。虽然不直接针对化学或质谱，但其关于如何构建能够有效处理复杂时空模式的“大模型”的核心讨论，对“化学大模型”和“质谱结构推理”等领域中模型架构和训练范式的设计具有重要的启发和展望意义。

**📖 中文摘要**

本文提出了一个用于神经元回路学习的变分潜在平衡（Variational Latent Equilibrium）形式化方法。大脑在识别和生成复杂时空模式方面仍然无与伦比，而当前的深度学习算法（如通过时间的反向传播BPTT）在很大程度上与我们目前对大脑回路和动力学的理解相悖。作者的工作旨在以一种受控的、生物学上合理的方式来近似BPTT。该方法基于能量守恒和极值作用原理，构建并统一扩展了几种先前基于局部、时间连续、无相位时空信用分配的方法。起点是一个神经元状态的前瞻性能量函数，从中计算出时间连续神经元网络的实时误差动态。在一般情况下，这为神经元网络提供了伴随方法结果的简单推导，即BPTT的时间连续等价形式。通过一些修改，可以将其转变为一组完全局部（在空间和时间上）的神经元和突触动力学方程。该理论为大脑中的时空深度学习提供了一个严格的框架，同时为能够执行这些计算的物理回路提供了蓝图。这项工作为构建更接近生物机制的、能够处理复杂时空模式（如化学信号或质谱序列）的“大模型”提供了理论基础和设计思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Brains remain unrivaled in their ability to recognize and generate complex spatiotemporal patterns. While AI is able to reproduce some of these capabilities, deep learning algorithms remain largely at odds with our current understanding of brain circuitry and dynamics. This is prominently the case for backpropagation through time (BPTT), the go-to algorithm for learning complex temporal dependencies. In this work we propose a general formalism to approximate BPTT in a controlled, biologically plausible manner. Our approach builds on, unifies and extends several previous approaches to local, time-continuous, phase-free spatiotemporal credit assignment based on principles of energy conservation and extremal action. Our starting point is a prospective energy function of neuronal states, from which we calculate real-time error dynamics for time-continuous neuronal networks. In the general case, this provides a simple and straightforward derivation of the adjoint method result for neuronal networks, the time-continuous equivalent to BPTT. With a few modifications, we can turn this into a fully local (in space and time) set of equations for neuron and synapse dynamics. Our theory provides a rigorous framework for spatiotemporal deep learning in the brain, while simultaneously suggesting a blueprint for physical circuits capable of carrying out these computations. These results reframe and extend the recently proposed Generalized Latent Equilibrium (GLE) model.

</details>

---

### 53. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容涉及使用无监督机器学习框架（Prometheus）来发现和验证复杂物理化学系统（束-等离子体）中的相变和集体振荡模式。这既是对“化学大模型”（广义上指用于化学物理问题的复杂模型）应用的前沿探索，也包含了重要的相关讨论（验证理论预测）。

**📖 中文摘要**

本文为中等能量（10-100 MeV）强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。论文第一部分基于Vlasov-Poisson系统建立了动力学场论，推导了三种束分布函数的Lindhard介电函数和随机相位近似（RPA）极化张量。通过介电函数证明了在临界束密度n_c以上存在无阻尼的朗缪尔波模式，获得了显式的束-等离子体色散关系，并证明了朗道阻尼在粒子-空穴连续谱之上消失。等离子体频率Ω_p^2由f求和定则固定，与分布形状无关；更高的色散系数依赖于速度矩。空间电荷效应驱动了以sqrt(n-n_c)起始的异常束展宽和在q=2k_F处的Friedel振荡。束-等离子体转变通过重整化群分析属于3D Ising普适类。第二部分使用Prometheus（一个在粒子束模拟的静态结构因子数据S(q)上训练的beta-VAE）验证了这些预测。Prometheus检测到了高斯分布和均匀分布中集体等离子体振荡的开始，确认了它们在简并费米气体（n_c -> 0）中的缺失，并解析了在q=2k_F处的Kohn异常。这项工作将理论物理建模与无监督机器学习（Prometheus框架）相结合，用于发现和验证复杂物理系统中的相变和集体模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

## 📊 数据统计
- 累计运行天数：32
- 累计论文数量：2252

## 📝 历史记录

> 暂无历史数据

