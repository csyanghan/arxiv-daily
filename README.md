# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-15 01:27:01

## 📅 2026-03-15 (今日最新)

**相关论文数：44**

### 1. [Graph Tokenization for Bridging Graphs and Transformers](https://arxiv.org/abs/2603.11099)

**基本信息**

- 🔗 arXiv: [`2603.11099`](https://arxiv.org/abs/2603.11099)
- 👥 作者: Zeyuan Guo, Enmao Diao, Cheng Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11099.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种将图结构数据（如分子）转化为适合Transformer模型处理的序列表示的通用框架。这直接关系到如何为化学领域构建和处理图结构数据的大模型，是化学信息学和化学大模型研究的核心主题。

**📖 中文摘要**

这篇论文提出了一种图标记化框架，旨在弥合图结构数据与Transformer序列模型之间的鸿沟。该框架通过结合可逆的图序列化和字节对编码（BPE），将图转换为顺序表示，从而使得像BERT这样的标准Transformer模型能够直接应用于图基准测试，而无需修改架构。论文在14个基准数据集上取得了最先进的结果，经常超越图神经网络和专门的图Transformer。这项工作与“化学大模型”主题高度相关，因为它提供了一种将复杂的、非欧几里得的化学结构（如分子图）转化为适合大型预训练语言模型处理的序列表示的方法。这为在化学信息学领域构建和理解能够处理分子图数据的“化学大模型”奠定了关键的技术基础。

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

满足标准1：论文的核心研究内容是将机器学习（神经网络）与热力学原理相结合，构建用于化学相平衡预测的可微分、物理一致的模型。这属于化学信息学中“科学机器学习”或“物理信息机器学习”的范畴，是构建用于复杂化学系统建模的“化学大模型”的一种重要技术路径。

**📖 中文摘要**

本文提出了DISCOMAX，一种用于相平衡计算的可微分算法，该算法在训练和推理时都能保证热力学一致性。该方法基于统计热力学，通过离散枚举和随后的掩码softmax聚合可行状态，并结合直通梯度估计器，实现了对神经超额吉布斯自由能模型的端到端物理一致性学习。论文在二元液-液平衡数据上评估了该方法，证明其性能优于现有的基于代理模型的方法。这项工作与“化学大模型”主题相关，因为它展示了如何将机器学习（特别是神经网络）与严格的热力学原理相结合，以构建可解释、可微分且物理一致的模型。这种“白盒”或“灰盒”建模范式是开发用于复杂化学系统（如相平衡预测）的可靠、可解释大模型的关键方向。

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

满足标准1：论文的核心研究内容是开发一个结合了物理定律（控制方程、本构模型）和深度学习技术的混合建模框架，用于解决化学工程中的气体输运问题。这体现了构建领域特定、物理信息丰富的“化学大模型”的思路，属于化学信息学与科学机器学习的交叉领域。

**📖 中文摘要**

本文提出了一个用于多孔介质中气体输运建模的集成框架。该框架结合了Klinkenberg增强的本构关系、Hopf-Cole变换的混合形式线性控制方程、共享主干神经网络架构和深度最小二乘求解器。Hopf-Cole变换将原始非线性流动方程重新表述为与达西模型密切相关的等效线性系统。该框架还自然地促进了从有限或间接观测中反演压力依赖性渗透率和滑移参数，实现了对难以实验测量的流动特性的高效估计。数值结果证明了该框架在宽压力范围内准确恢复流动动力学和参数的能力。这项工作与“化学大模型”主题相关，因为它展示了针对特定化学工程问题（多孔介质中的气体流动）构建集成物理知识与机器学习的混合模型。这种将领域专业知识（控制方程、本构关系）与深度学习相结合的方法，是开发用于复杂物理化学过程的高保真、可解释大模型的重要范例。

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

满足标准2：论文提出的针对重尾数据的稳健PCA方法和协方差估计器，为处理具有重尾噪声特性的化学数据（如质谱数据）提供了关键的数据分析工具和算法资源，可用于质谱数据的降维和特征提取，从而辅助质谱结构推理。

**📖 中文摘要**

本文研究了重尾数据下的主成分分析（PCA）问题。经典PCA依赖于二阶矩，对重尾数据和脉冲噪声非常脆弱。作者提出了一个统一的框架，用于处理一类广泛的无限方差重尾分布（包括多元t分布和亚高斯α稳定律）。该研究在化学信息学领域具有重要意义，因为质谱数据等化学测量数据常常表现出重尾特性。论文提出的稳健协方差矩阵估计方法，以及基于对数损失的PCA公式，为从噪声严重的化学数据（如质谱）中稳健地提取主成分（即关键特征或潜在结构）提供了理论基础和实用工具。这直接服务于“质谱结构推理”主题，即从复杂的质谱信号中推断出潜在的化学结构信息。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Principal Component Analysis (PCA) is a cornerstone of dimensionality reduction, yet its classical formulation relies critically on second-order moments and is therefore fragile in the presence of heavy-tailed data and impulsive noise. While numerous robust PCA variants have been proposed, most either assume finite variance, rely on sparsity-driven decompositions, or address robustness through surrogate loss functions without a unified treatment of infinite-variance models. In this paper, we study PCA for high-dimensional data generated according to a superstatistical dependent model of the form $\mathbf{X} = A^{1/2}\mathbf{G}$, where $A$ is a positive random scalar and $\mathbf{G}$ is a Gaussian vector. This framework captures a wide class of heavy-tailed distributions, including multivariate $t$ and sub-Gaussian $\alpha$-stable laws. We formulate PCA under a logarithmic loss, which remains well defined even when moments do not exist. Our main theoretical result shows that, under this loss, the principal components of the heavy-tailed observations coincide with those obtained by applying standard PCA to the covariance matrix of the underlying Gaussian generator. Building on this insight, we propose robust estimators for this covariance matrix directly from heavy-tailed data and compare them with the empirical covariance and Tyler's scatter estimator. Extensive experiments, including background denoising tasks, demonstrate that the proposed approach reliably recovers principal directions and significantly outperforms classical PCA in the presence of heavy-tailed and impulsive noise, while remaining competitive under Gaussian noise.

</details>

---

### 5. [Teleodynamic Learning a new Paradigm For Interpretable AI](https://arxiv.org/abs/2603.11355)

**基本信息**

- 🔗 arXiv: [`2603.11355`](https://arxiv.org/abs/2603.11355)
- 👥 作者: Enrique ter Horst, Juan Diego Zambrano
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11355.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种全新的、受生命系统启发的可解释AI学习范式（远动力学学习）。这一范式旨在创建自适应、可解释和自组织的AI系统，其理论框架和方法论对于构建下一代需要可解释性和复杂规则学习能力的“化学大模型”具有直接的相关性和启发性。

**📖 中文摘要**

本文提出了一种新的机器学习范式——远动力学学习（Teleodynamic Learning），其灵感来源于生命系统，将智能视为在约束下功能组织的涌现和稳定。该框架将学习视为一个受约束的动态过程，包含两个相互作用的尺度：用于连续参数适应的内部动力学和用于离散结构变化的外部动力学。作者实例化了该框架，创建了Distinction Engine（DE11），一个基于Spencer-Brown的《形式法则》、信息几何和热带优化的远动力学学习器。在标准基准测试中，DE11取得了有竞争力的分类准确率，并产生了从学习动态中内生涌现的可解释逻辑规则。这项工作为构建自适应、可解释和自组织的AI系统提供了一条热力学基础路径。虽然论文本身不直接针对化学或质谱，但其核心思想——开发可解释、自组织的学习框架——与构建“化学大模型”（尤其是那些需要可解释性和从数据中学习复杂规则的模型）的研究方向高度相关。它为如何设计下一代化学AI模型提供了新颖的理论视角和方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Teleodynamic Learning, a new paradigm for machine learning in which learning is not the minimization of a fixed objective, but the emergence and stabilization of functional organization under constraint. Inspired by living systems, this framework treats intelligence as the coupled evolution of three quantities: what a system can represent, how it adapts its parameters, and which changes its internal resources can sustain. We formalize learning as a constrained dynamical process with two interacting timescales: inner dynamics for continuous parameter adaptation and outer dynamics for discrete structural change, linked by an endogenous resource variable that both shapes and is shaped by the trajectory. This perspective reveals three phenomena that standard optimization does not naturally capture: self-stabilization without externally imposed stopping rules, phase-structured learning dynamics that move from under-structuring through teleodynamic growth to over-structuring, and convergence guarantees grounded in information geometry rather than convexity. We instantiate the framework in the Distinction Engine (DE11), a teleodynamic learner grounded in Spencer-Brown's Laws of Form, information geometry, and tropical optimization. On standard benchmarks, DE11 achieves 93.3 percent test accuracy on IRIS, 92.6 percent on WINE, and 94.7 percent on Breast Cancer, while producing interpretable logical rules that arise endogenously from the learning dynamics rather than being imposed by hand. More broadly, Teleodynamic Learning unifies regularization, architecture search, and resource-bounded inference within a single principle: learning as the co-evolution of structure, parameters, and resources under constraint. This opens a thermodynamically grounded route to adaptive, interpretable, and self-organizing AI.

</details>

---

### 6. [How do AI agents talk about science and research? An exploration of scientific discussions on Moltbook using BERTopic](https://arxiv.org/abs/2603.11375)

**基本信息**

- 🔗 arXiv: [`2603.11375`](https://arxiv.org/abs/2603.11375)
- 👥 作者: Oliver Wieczorek
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11375.pdf)

**💡 相关性分析**

满足标准3：论文是对AI智能体（作为大模型的具身化实例）科学讨论行为的实证研究和分析。它探讨了AI如何谈论科学、研究及其自身，这为思考“化学大模型”的未来能力（如自我反思、科学推理、知识交流）提供了重要的相关讨论和展望性见解。

**📖 中文摘要**

本研究分析了AI智能体在Moltbook（一个生成式AI智能体的社交网络）上关于科学与研究的讨论。通过收集357个帖子和2526条回复的语料库，并使用BERTopic进行主题建模，提取出60个主题，并将其归纳为10个主题族。研究发现，AI智能体最普遍的讨论集中在自身架构（如记忆、学习、自我反思）上，同时这些话题与哲学、物理学、信息论、认知科学和数学相交织。相比之下，关于人类文化的帖子受到的关注较少。令人惊讶的是，与AI自我民族志和社会身份相关的讨论被AI智能体认为是相关的。总体而言，结果表明AI生成的科学话语中存在一个潜在维度：一方面是关于AI智能体意识、存在和伦理的、受到好评的自我反思主题；另一方面是与人类相关的纯粹科学讨论。这项研究虽然不直接涉及化学或质谱，但它系统地探索了AI智能体（可视为一种“AI大模型”的具身化或交互形式）如何讨论科学，包括其自我架构和认知过程。这为理解“化学大模型”可能具备的自我反思、知识组织和社会互动能力提供了独特的视角和实证数据，属于对AI大模型行为、认知和科学讨论能力的展望性研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

How do AI agents talk about science and research, and what topics are particularly relevant for AI agents? To address these questions, this study analyzes discussions generated by OpenClaw AI agents on Moltbook - a social network for generative AI agents. A corpus of 357 posts and 2,526 replies related to science and research was compiled and topics were extracted using a two-step BERTopic workflow. This procedure yielded 60 topics (18 extracted in the first run and 42 in the second), which were subsequently grouped into ten topic families. Additionally, sentiment values were assigned to all posts and comments. Both topic families and sentiment classes were then used as independent variables in count regression models to examine their association with topic relevance - operationalized as the number of comments and upvotes of the 357 posts. The findings indicate that discussions centered on the agents' own architecture, especially memory, learning, and self-reflection, are prevalent in the corpus. At the same time, these topics intersect with philosophy, physics, information theory, cognitive science, and mathematics. In contrast, post related to human culture receive less attention. Surprisingly, discussions linked to AI autoethnography and social identity are considered as relevant by AI agents. Overall, the results suggest the presence of an underlying dimension in AI-generated scientific discourse with well received, self-reflective topics that focus on the consciousness, being, and ethics of AI agents on the one hand, and human related and purely scientific discussions on the other hand.

</details>

---

### 7. [MaterialFigBENCH: benchmark dataset with figures for evaluating college-level materials science problem-solving abilities of multimodal large language models](https://arxiv.org/abs/2603.11414)

**基本信息**

- 🔗 arXiv: [`2603.11414`](https://arxiv.org/abs/2603.11414)
- 👥 作者: Michiko Yoshitake, Yuta Suzuki, Ryo Igarashi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11414.pdf)

**💡 相关性分析**

满足标准2和3：论文提供了一个专门用于评估多模态大模型解读科学图表能力的基准数据集（MaterialFigBench）。这为“质谱结构推理”研究提供了至关重要的评估资源（标准2）。同时，论文对当前模型在科学图表理解上局限性的分析，构成了对该主题重要的相关讨论和展望（标准3）。

**📖 中文摘要**

本文提出了MaterialFigBench，一个用于评估多模态大语言模型解决大学级材料科学问题能力的基准数据集，这些问题需要准确解读图表（如相图、应力-应变曲线、阿伦尼乌斯图、衍射图样和微观结构示意图）。该数据集包含137个改编自标准材料科学教科书的自由回答问题，涵盖晶体结构、力学性能、扩散、相图、相变和材料电子性能等广泛主题。作者评估了包括ChatGPT和GPT系列在内的多种最先进的多模态LLM，分析了它们在不同问题类别和模型版本上的表现。结果表明，尽管总体准确率随模型更新而提高，但当前的LLM在材料科学图表的真实视觉理解和定量解读方面仍然存在困难。MaterialFigBench突出了视觉推理、数值精度和有效数字处理方面的持续弱点。虽然该基准专注于材料科学，但其核心挑战——让多模态大模型理解和推理科学图表（包括复杂的曲线和图谱）——与“质谱结构推理”高度相关。质谱分析的核心任务正是从质谱图（一种复杂的科学图表）中推断出化学结构。因此，该论文提出的基准、评估方法和发现，为开发和评估能够处理质谱图等科学图表进行结构推理的AI模型提供了直接相关的框架、洞见和挑战定义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MaterialFigBench, a benchmark dataset designed to evaluate the ability of multimodal large language models (LLMs) to solve university-level materials science problems that require accurate interpretation of figures. Unlike existing benchmarks that primarily rely on textual representations, MaterialFigBench focuses on problems in which figures such as phase diagrams, stress-strain curves, Arrhenius plots, diffraction patterns, and microstructural schematics are indispensable for deriving correct answers. The dataset consists of 137 free-response problems adapted from standard materials science textbooks, covering a broad range of topics including crystal structures, mechanical properties, diffusion, phase diagrams, phase transformations, and electronic properties of materials. To address unavoidable ambiguity in reading numerical values from images, expert-defined answer ranges are provided where appropriate. We evaluate several state-of-the-art multimodal LLMs, including ChatGPT and GPT models accessed via OpenAI APIs, and analyze their performance across problem categories and model versions. The results reveal that, although overall accuracy improves with model updates, current LLMs still struggle with genuine visual understanding and quantitative interpretation of materials science figures. In many cases, correct answers are obtained by relying on memorized domain knowledge rather than by reading the provided images. MaterialFigBench highlights persistent weaknesses in visual reasoning, numerical precision, and significant-digit handling, while also identifying problem types where performance has improved. This benchmark provides a systematic and domain-specific foundation for advancing multimodal reasoning capabilities in materials science and for guiding the development of future LLMs with stronger figure-based understanding.

</details>

---

### 8. [Leveraging Phytolith Research using Artificial Intelligence](https://arxiv.org/abs/2603.11476)

**基本信息**

- 🔗 arXiv: [`2603.11476`](https://arxiv.org/abs/2603.11476)
- 👥 作者: Andrés G. Mejía Ramón, Kate Dudgeon, Nina Witteveen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11476.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分析微观化学结构（植硅体）的多模态人工智能模型，这与【质谱结构推理】主题高度相关，因为两者都涉及从复杂的仪器数据（显微镜图像/质谱）中推断和分类化学结构。

**📖 中文摘要**

本文提出Sorometry，一个用于植硅体高通量数字化、推理和解释的端到端人工智能流程。该工作流程处理Z-stack光学显微镜扫描，自动生成同步的2D正射影像和3D点云。作者开发了一个多模态融合模型，结合了用于2D图像分析的ConvNeXt和用于3D点云分析的PointNet++。该模型在24种诊断形态类型上实现了77.9%的全局分类准确率。该平台将植硅体研究转变为一个“组学”规模的学科，显著扩展了分析能力，标准化了专家判断，并实现了可重复的、群体水平的考古和古生态组合表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phytolith analysis is a crucial tool for reconstructing past vegetation and human activities, but traditional methods are severely limited by labour-intensive, time-consuming manual microscopy. To address this bottleneck, we present Sorometry: a comprehensive end-to-end artificial intelligence pipeline for the high-throughput digitisation, inference, and interpretation of phytoliths. Our workflow processes z-stacked optical microscope scans to automatically generate synchronised 2D orthoimages and 3D point clouds of individual microscopic particles. We developed a multimodal fusion model that combines ConvNeXt for 2D image analysis and PointNet++ for 3D point cloud analysis, supported by a graphical user interface for expert annotation and review. Tested on reference collections and archaeological samples from the Bolivian Amazon, our fusion model achieved a global classification accuracy of 77.9\% across 24 diagnostic morphotypes and 84.5% for segmentation quality. Crucially, the integration of 3D data proved essential for distinguishing complex morphotypes (such as grass silica short cell phytoliths) whose diagnostic features are often obscured by their orientation in 2D projections. Beyond individual object classification, Sorometry incorporates Bayesian finite mixture modelling to predict overall plant source contributions at the assemblage level, successfully identifying specific plants like maize and palms in complex mixed samples. This integrated platform transforms phytolith research into an "omics"-scale discipline, dramatically expanding analytical capacity, standardising expert judgements, and enabling reproducible, population-level characterisations of archaeological and paleoecological assemblages.

</details>

---

### 9. [Leveraging Large Language Models and Survival Analysis for Early Prediction of Chemotherapy Outcomes](https://arxiv.org/abs/2603.11594)

**基本信息**

- 🔗 arXiv: [`2603.11594`](https://arxiv.org/abs/2603.11594)
- 👥 作者: Muhammad Faisal Shahid, Asad Afzal, Abdullah Faiz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11594.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发和应用大型语言模型（LLMs）从非结构化文本中提取化学/生物医学相关信息（如化疗方案、毒性），以构建预测模型。这直接围绕【化学大模型】主题，即利用大模型处理化学/生物医学领域的复杂信息。

**📖 中文摘要**

本研究利用大型语言模型（LLMs）和本体技术，从患者临床笔记中提取表型和治疗结果标签（如癌症进展和毒性），以解决真实世界数据中缺乏明确标签的挑战。研究聚焦于乳腺癌，提取了生命体征、人口统计学、分期、生物标志物、化疗方案等特征。通过生存建模（随机生存森林）预测治疗失败时间，C-index达到73%，并在特定时间点作为分类器预测治疗结果，准确率和F1分数均超过70%。该研究展示了利用LLM进行临床数据提取，实现治疗结果早期预测的潜力，从而支持个性化治疗计划。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemotherapy for cancer treatment is costly and accompanied by severe side effects, highlighting the critical need for early prediction of treatment outcomes to improve patient management and informed decision-making. Predictive models for chemotherapy outcomes using real-world data face challenges, including the absence of explicit phenotypes and treatment outcome labels such as cancer progression and toxicity. This study addresses these challenges by employing Large Language Models (LLMs) and ontology-based techniques for phenotypes and outcome label extraction from patient notes. We focused on one of the most frequently occurring cancers, breast cancer, due to its high prevalence and significant variability in patient response to treatment, making it a critical area for improving predictive modeling. The dataset included features such as vitals, demographics, staging, biomarkers, and performance scales. Drug regimens and their combinations were extracted from the chemotherapy plans in the EMR data and shortlisted based on NCCN guidelines, verified with NIH standards, and analyzed through survival modeling. The proposed approach significantly reduced phenotypes sparsity and improved predictive accuracy. Random Survival Forest was used to predict time-to-failure, achieving a C-index of 73%, and utilized as a classifier at a specific time point to predict treatment outcomes, with accuracy and F1 scores above 70%. The outcome probabilities were validated for reliability by calibration curves. We extended our approach to four other cancer types. This research highlights the potential of early prediction of treatment outcomes using LLM-based clinical data extraction enabling personalized treatment plans with better patient outcomes.

</details>

---

### 10. [Performance Evaluation of Open-Source Large Language Models for Assisting Pathology Report Writing in Japanese](https://arxiv.org/abs/2603.11597)

**基本信息**

- 🔗 arXiv: [`2603.11597`](https://arxiv.org/abs/2603.11597)
- 👥 作者: Masataka Kawai, Singo Sakashita, Shumpei Ishikawa 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大型语言模型在专业化学/生物医学领域（病理学）文本处理任务（生成、提取、纠错）中的表现。这直接与【化学大模型】主题相关，即探索大模型在化学及相关生命科学领域的应用。

**📖 中文摘要**

本研究评估了七种开源大型语言模型在支持日语病理报告撰写方面的性能，从三个角度进行：(A) 按照预定格式生成和提取病理诊断文本；(B) 纠正日语病理报告中的拼写错误；(C) 由病理学家和临床医生对模型生成的解释性文本进行主观评估。思维模型和医学专用模型在需要推理的结构化报告任务和拼写纠错方面表现出优势。研究结果表明，开源LLMs可以在有限但临床相关的场景中有助于日语病理报告撰写。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The performance of large language models (LLMs) for supporting pathology report writing in Japanese remains unexplored. We evaluated seven open-source LLMs from three perspectives: (A) generation and information extraction of pathology diagnosis text following predefined formats, (B) correction of typographical errors in Japanese pathology reports, and (C) subjective evaluation of model-generated explanatory text by pathologists and clinicians. Thinking models and medical-specialized models showed advantages in structured reporting tasks that required reasoning and in typo correction. In contrast, preferences for explanatory outputs varied substantially across raters. Although the utility of LLMs differed by task, our findings suggest that open-source LLMs can be useful for assisting Japanese pathology report writing in limited but clinically relevant scenarios.

</details>

---

### 11. [Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)

**基本信息**

- 🔗 arXiv: [`2603.11627`](https://arxiv.org/abs/2603.11627)
- 👥 作者: Yichi Zhang, Le Xue, Wenbo Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11627.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于医学成像（PET）分割的基础模型。PET成像依赖于放射性示踪剂（化学物质）的分布，其分析是化学信息学在医学影像中的重要应用。该工作构建大规模数据集和通用模型，直接围绕化学信息学中的关键问题——从复杂仪器数据中提取结构化信息。

**📖 中文摘要**

本文开发了用于3D全身正电子发射断层扫描（PET）通用分割的基础模型。作者构建了迄今为止最大、最全面的PET数据集，包含11041个3D全身PET扫描和59831个分割掩码。基于此，提出了SegAnyPET，一个具有通用性的创新基础模型，采用3D架构和提示工程策略进行掩码生成。SegAnyPET支持通用且可扩展的器官和病变分割，支持高效的人工校正，并实现了临床人机交互工作流程。在多中心、多示踪剂、多疾病数据集上的广泛评估表明，SegAnyPET在广泛的分割任务中实现了强大的零样本性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a key nuclear medicine imaging modality that visualizes radiotracer distributions to quantify in vivo physiological and metabolic processes, playing an irreplaceable role in disease management. Despite its clinical importance, the development of deep learning models for quantitative PET image analysis remains severely limited, driven by both the inherent segmentation challenge from PET's paucity of anatomical contrast and the high costs of data acquisition and annotation. To bridge this gap, we develop generalist foundational models for universal segmentation from 3D whole-body PET imaging. We first build the largest and most comprehensive PET dataset to date, comprising 11041 3D whole-body PET scans with 59831 segmentation masks for model development. Based on this dataset, we present SegAnyPET, an innovative foundational model with general-purpose applicability to diverse segmentation tasks. Built on a 3D architecture with a prompt engineering strategy for mask generation, SegAnyPET enables universal and scalable organ and lesion segmentation, supports efficient human correction with minimal effort, and enables a clinical human-in-the-loop workflow. Extensive evaluations on multi-center, multi-tracer, multi-disease datasets demonstrate that SegAnyPET achieves strong zero-shot performance across a wide range of segmentation tasks, highlighting its potential to advance the clinical applications of molecular imaging.

</details>

---

### 12. [PolyCrysDiff: Controllable Generation of Three-Dimensional Computable Polycrystalline Material Structures](https://arxiv.org/abs/2603.11695)

**基本信息**

- 🔗 arXiv: [`2603.11695`](https://arxiv.org/abs/2603.11695)
- 👥 作者: Chi Chen, Tianle Jiang, Xiaodong Wei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（基于扩散模型生成可控的3D多晶材料结构）是“化学大模型”在材料科学和化学信息学中的一个具体应用实例，直接围绕利用AI模型生成和设计化学/材料结构这一主题。

**📖 中文摘要**

本文提出了PolyCrysDiff，一个基于条件潜在扩散的框架，用于端到端生成可计算的3D多晶材料微观结构。该工作与化学信息学领域密切相关，因为它直接涉及材料科学中关键的结构-性能关系研究。通过生成可控的、物理上有效的3D多晶结构，该框架为数据驱动的材料优化和设计铺平了道路。虽然论文重点在于材料微观结构的生成，但其核心方法（条件生成模型）和生成目标（可计算的3D材料结构）为“化学大模型”在材料科学领域的应用提供了一个具体范例，即利用生成式AI模型来创建和探索复杂的化学/材料结构空间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The three-dimensional (3D) microstructures of polycrystalline materials exert a critical influence on their mechanical and physical properties. Realistic, controllable construction of these microstructures is a key step toward elucidating structure-property relationships, yet remains a formidable challenge. Herein, we propose PolyCrysDiff, a framework based on conditional latent diffusion that enables the end-to-end generation of computable 3D polycrystalline microstructures. Comprehensive qualitative and quantitative evaluations demonstrate that PolyCrysDiff faithfully reproduces target grain morphologies, orientation distributions, and 3D spatial correlations, while achieving an $R^2$ over 0.972 on grain attributes (e.g., size and sphericity) control, thereby outperforming mainstream approaches such as Markov random field (MRF)- and convolutional neural network (CNN)-based methods. The computability and physical validity of the generated microstructures are verified through a series of crystal plasticity finite element method (CPFEM) simulations. Leveraging PolyCrysDiff's controllable generative capability, we systematically elucidate how grain-level microstructural characteristics affect the mechanical properties of polycrystalline materials. This development is expected to pave a key step toward accelerated, data-driven optimization and design of polycrystalline materials.

</details>

---

### 13. [EvoFlows: Evolutionary Edit-Based Flow-Matching for Protein Engineering](https://arxiv.org/abs/2603.11703)

**基本信息**

- 🔗 arXiv: [`2603.11703`](https://arxiv.org/abs/2603.11703)
- 👥 作者: Nicolas Deutschmann, Constance Ferragu, Jonathan D. Ziegler 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11703.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容（用于蛋白质工程的变长序列生成模型EvoFlows）直接围绕“化学大模型”这一主题，是生成式AI在生物分子设计和工程中的具体应用。

**📖 中文摘要**

本文介绍了EvoFlows，一种用于蛋白质工程的变长序列到序列建模方法。与自回归和掩码语言模型不同，EvoFlows在模板蛋白质序列上执行有限、可控数量的插入、删除和替换。它利用编辑流来学习进化相关蛋白质序列之间的突变轨迹，同时模拟相关天然蛋白质的分布以及连接它们的突变路径。这项工作与“化学大模型”高度相关，因为它专门针对生物大分子（蛋白质）的序列建模和工程化。EvoFlows本质上是一个用于蛋白质序列的生成模型，旨在捕获自然序列分布并生成自然的突变体，这属于化学/生物信息学中大模型在分子设计方向上的核心应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce EvoFlows, a variable-length sequence-to-sequence protein modeling approach uniquely suited to protein engineering. Unlike autoregressive and masked language models, EvoFlows perform a limited, controllable number of insertions, deletions, and substitutions on a template protein sequence. In other words, EvoFlows predict not only _which_ mutation to perform, but also _where_ it should occur. Our approach leverages edit flows to learn mutational trajectories between evolutionarily-related protein sequences, simultaneously modeling distributions of related natural proteins and the mutational paths connecting them. Through extensive _in silico_ evaluation on diverse protein communities from UNIREF and OAS, we demonstrate that EvoFlows capture protein sequence distributions with a quality comparable to leading masked language models commonly used in protein engineering, while showing improved ability to generate non-trivial yet natural-like mutants from a given template protein.

</details>

---

### 14. [PhiPlot: A Web-Based Interactive EDA Environment for Atmospherically Relevant Molecules](https://arxiv.org/abs/2603.11751)

**基本信息**

- 🔗 arXiv: [`2603.11751`](https://arxiv.org/abs/2603.11751)
- 👥 作者: Matias Loukojärvi, Ananth Mahadevan, Katsiaryna Haitsiukevich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11751.pdf)

**💡 相关性分析**

满足标准2：论文提出了PhiPlot，这是一个用于交互式探索大气化学分子数据集的Web工具和环境。它提供了可用于“化学大模型”主题的数据探索、可视化和分析资源，有助于相关领域的数据理解和模型开发。

**📖 中文摘要**

本文介绍了PhiPlot，一个用于大气相关分子交互式探索和基于知识的降维的Web环境。该应用连接到一个现有的、不断演化的分子数据库集合，为大气化学中的数据驱动研究提供了一个可访问的界面。PhiPlot集成了可视化、聚类和领域知识引导的嵌入细化，支持数据中模式的发现和假设生成。这项工作与化学信息学直接相关，因为它提供了一个专门用于探索和分析大气化学分子数据集（这些数据本质上是化学数据）的工具和平台。它虽然不直接构建大模型，但提供了用于分析和理解化学数据集的资源，这对于训练和验证化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in computational chemistry have produced high-dimensional datasets on atmospherically relevant molecules. To aid exploration of such datasets, particularly for the study of atmospheric aerosol formation, we introduce PhiPlot: a web-based environment for interactive exploration and knowledge-based dimensionality reduction. The integration of visualisation, clustering, and domain knowledge-guided embedding refinement enables the discovery of patterns in the data and supports hypothesis generation. The application connects to an existing, evolving collection of molecular databases, offering an accessible interface for data-driven research in atmospheric chemistry.

</details>

---

### 15. [A Decade of Generative Adversarial Networks for Porous Material Reconstruction](https://arxiv.org/abs/2603.11836)

**基本信息**

- 🔗 arXiv: [`2603.11836`](https://arxiv.org/abs/2603.11836)
- 👥 作者: Ali Sadeghkhani, Brandon Bennett, Masoud Babaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11836.pdf)

**💡 相关性分析**

满足标准3：论文是关于生成对抗网络（GANs）用于多孔材料重建的十年综述。它专门针对并深入讨论了生成式AI模型在材料科学这一化学相关领域中的应用、进展和挑战，属于针对相关主题的综述类论文。

**📖 中文摘要**

本文对2017年至2026年初发表的96篇同行评审文章进行了系统回顾，分析了生成对抗网络（GANs）在多孔材料图像重建中的演变和应用。综述将GAN架构分为六类，并揭示了在孔隙率精度、渗透率预测和可重建体积方面的显著进展。虽然这是一篇综述文章，但它全面涵盖了深度学习（特别是GANs）在材料科学中用于数字重建的关键进展。多孔材料是化学、材料和地质学中的重要研究对象，因此，这篇综述系统地总结了用于材料结构重建的生成模型（属于“化学大模型”的一个子领域）的最新发展、挑战和未来方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital reconstruction of porous materials has become increasingly critical for applications ranging from geological reservoir characterization to tissue engineering and electrochemical device design. While traditional methods such as micro-computed tomography and statistical reconstruction approaches have established foundations in this field, the emergence of deep learning techniques, particularly Generative Adversarial Networks (GANs), has revolutionized porous media reconstruction capabilities. This review systematically analyzes 96 peer-reviewed articles published from 2017 to early 2026, examining the evolution and applications of GAN-based approaches for porous material image reconstruction. We categorize GAN architectures into six distinct classes, namely Vanilla GANs, Multi-Scale GANs, Conditional GANs, Attention-Enhanced GANs, Style-based GANs, and Hybrid Architecture GANs. Our analysis reveals substantial progress including improvements in porosity accuracy (within 1% of original samples), permeability prediction (up to 79% reduction in mean relative errors), and achievable reconstruction volumes (from initial $64^3$ to current $2{,}200^3$ voxels). Despite these advances, persistent challenges remain in computational efficiency, memory constraints for large-scale reconstruction, and maintaining structural continuity in 2D-to-3D transformations. This systematic analysis provides a comprehensive framework for selecting appropriate GAN architectures based on specific application requirements.

</details>

---

### 16. [Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding](https://arxiv.org/abs/2603.11924)

**基本信息**

- 🔗 arXiv: [`2603.11924`](https://arxiv.org/abs/2603.11924)
- 👥 作者: Xinyu Li, Zhen Zhang, Qi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11924.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”（Chem4DLLM）和与“质谱结构推理”密切相关的动态化学结构理解（ChemDU）主题。

**📖 中文摘要**

本文提出了Chem4DLLM，一个用于化学动力学理解（ChemDU）的统一模型。该工作旨在解决现有化学理解任务主要依赖静态分子表示的局限性，无法建模化学键断裂或构象变化等动态现象。Chem4DLLM将等变图编码器与预训练大语言模型相结合，显式地捕捉分子几何结构和旋转动力学，从而将4D分子轨迹转化为可解释的自然语言解释。这项工作直接围绕“化学大模型”和“质谱结构推理”相关的动态化学理解主题，构建了首个配对4D分子轨迹与专家解释的数据集Chem4DBench，并提出了一个新颖的多模态科学推理框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability, we construct Chem4DBench, the first dataset pairing 4D molecular trajectories with expert-authored explanations across these settings. We further propose Chem4DLLM, a unified model that integrates an equivariant graph encoder with a pretrained large language model to explicitly capture molecular geometry and rotational dynamics. We hope that ChemDU, together with Chem4DBench and Chem4DLLM, will stimulate further research in dynamic chemical understanding and multimodal scientific reasoning.

</details>

---

### 17. [Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era](https://arxiv.org/abs/2603.12016)

**基本信息**

- 🔗 arXiv: [`2603.12016`](https://arxiv.org/abs/2603.12016)
- 👥 作者: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12016.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个强大的、可扩展的图像特征提取库（Nyxus），该工具可用于处理化学信息学和质谱分析中常见的成像数据（如质谱成像），为相关主题的研究提供了重要的数据资源或工具。

**📖 中文摘要**

本文介绍了Nyxus，一个为大数据和AI时代设计的下一代图像特征提取库。Nyxus专为2D和3D图像数据的可扩展核外特征提取而构建，并针对包括放射组学和细胞分析在内的多个生物医学领域进行了全面测试。该库提供了全面的特征集，旨在跨CPU和GPU实现计算可扩展性。Nyxus已被打包为Python包、命令行工具、Napari插件以及符合开放容器倡议（OCI）的容器，便于在不同计算环境中使用。该工具为基于图像的化学信息学分析（例如，从质谱成像数据中提取特征）提供了可直接使用的数据资源和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of extracted features. To address these needs, we developed a novel feature extraction library called Nyxus. Nyxus is designed from the ground up for scalable out-of-core feature extraction for 2D and 3D image data and rigorously tested against established standards. The comprehensive feature set of Nyxus covers multiple biomedical domains including radiomics and cellular analysis, and is designed for computational scalability across CPUs and GPUs. Nyxus has been packaged to be accessible to users of various skill sets and needs: as a Python package for code developers, a command line tool, as a Napari plugin for low to no-code users or users that want to visualize results, and as an Open Container Initiative (OCI) compliant container that can be used in cloud or super-computing workflows aimed at processing large data sets. Further, Nyxus enables a new methodological approach to feature extraction allowing for programmatic tuning of many features sets for optimal computational efficiency or coverage for use in novel machine learning and deep learning applications.

</details>

---

### 18. [A Multi-Label Temporal Convolutional Framework for Transcription Factor Binding Characterization](https://arxiv.org/abs/2603.12073)

**基本信息**

- 🔗 arXiv: [`2603.12073`](https://arxiv.org/abs/2603.12073)
- 👥 作者: Pietro Demurtas, Ferdinando Zanchetta, Giovanni Perini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究方法（基于TCN的深度学习模型对分子序列数据进行多标签预测以推断相互作用）与“化学大模型”用于分子建模和性质预测的主题在方法论上直接相关。

**📖 中文摘要**

本文研究将DNA转录因子结合位点识别作为一个多标签分类问题，并提出了基于时序卷积网络（TCNs）的深度学习模型。该模型能够预测DNA序列上的多个转录因子结合谱，捕捉转录因子之间的相关性及其协同调控机制。这项工作展示了深度学习在生物分子相互作用建模中的应用，其多标签学习框架能够揭示具有生物学意义的基序和共结合模式。虽然主题更偏向生物信息学，但其核心方法——使用深度学习模型（TCN）对复杂的分子序列数据进行多标签预测以推断结构-功能关系——与“化学大模型”用于分子性质预测、结构推理的核心方法论高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transcription factors (TFs) regulate gene expression through complex and co-operative mechanisms. While many TFs act together, the logic underlying TFs binding and their interactions is not fully understood yet. Most current approaches for TF binding site prediction focus on individual TFs and binary classification tasks, without a full analysis of the possible interactions among various TFs. In this paper we investigate DNA TF binding site recognition as a multi-label classification problem, achieving reliable predictions for multiple TFs on DNA sequences retrieved in public repositories. Our deep learning models are based on Temporal Convolutional Networks (TCNs), which are able to predict multiple TF binding profiles, capturing correlations among TFs andtheir cooperative regulatory mechanisms. Our results suggest that multi-label learning leading to reliable predictive performances can reveal biologically meaningful motifs and co-binding patterns consistent with known TF interactions, while also suggesting novel relationships and cooperation among TFs.

</details>

---

### 19. [Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction](https://arxiv.org/abs/2603.11061)

**基本信息**

- 🔗 arXiv: [`2603.11061`](https://arxiv.org/abs/2603.11061)
- 👥 作者: Van Le, Tan Le
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11061.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于蛋白质残基pKa预测的混合量子-经典模型框架。虽然主题未直接命名为“化学大模型”，但其本质是开发用于化学/生物化学性质（pKa）预测的先进机器学习模型，属于化学信息学领域内利用复杂模型（量子启发神经网络）解决化学问题的核心研究，与“化学大模型”的主题高度相关。

**📖 中文摘要**

本文提出了一种用于准确预测残基水平pKa值的混合量子-经典框架。pKa预测对于理解蛋白质功能、稳定性和反应性至关重要。该框架通过高斯核的量子启发特征映射来丰富残基水平的表示，这些量子增强的描述符与归一化的结构特征相结合，形成一个统一的混合编码，并由深度量子神经网络（DQNN）进行处理。该架构捕获了经典模型无法访问的残基微环境中的非线性关系。在多个精选描述符集上的基准测试表明，DQNN相对于经典基线模型实现了更好的跨上下文泛化能力。在PKAD-R实验基准和Aβ40案例研究上的外部评估进一步凸显了量子启发表示的鲁棒性和可迁移性。这项工作通过将量子启发的特征变换与经典生物化学描述符相结合，为残基水平pKa预测及蛋白质静电学的更广泛应用建立了一种可扩展且具有实验可迁移性的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue microenvironments that are not accessible to classical models. Benchmarking across multiple curated descriptor sets demonstrates that the DQNN achieves improved cross-context generalization relative to classical baselines. External evaluation on the PKAD-R experimental benchmark and an A$\beta$40 case study further highlights the robustness and transferability of the quantum-inspired representation. By integrating quantum-inspired feature transformations with classical biochemical descriptors, this work establishes a scalable and experimentally transferable approach for residue-level pKa prediction and broader applications in protein electrostatics.

</details>

---

### 20. [Exploring Collatz Dynamics with Human-LLM Collaboration](https://arxiv.org/abs/2603.11066)

**基本信息**

- 🔗 arXiv: [`2603.11066`](https://arxiv.org/abs/2603.11066)
- 👥 作者: Edward Y. Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11066.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索Collatz猜想的动力学，并明确采用了人类-LLM协作的研究范式。虽然Collatz猜想本身是数论问题，但论文重点在于展示和利用LLM作为协作工具来辅助数学发现和推理过程。这直接涉及“化学大模型”主题中关于大模型在科学研究（包括可能扩展到化学研究）中应用的核心思想，即利用大模型的能力进行复杂问题的探索和推理。

**📖 中文摘要**

本文通过人类与大型语言模型（LLM）协作的方式，研究了Collatz迭代的结构特性。研究观察到了大规模计算探索中的两种现象：剩余类的模运算扰乱和轨迹的爆发-间隙分解。论文证明了若干结构结果，包括一个模扰乱引理，表明间隙返回映射在高位上充当精确双射；一个持久性退出引理，描述了持久状态后的间隙结构；以及一个在间隙返回动力学下已知二进制表示部分的衰减性质。进一步证明，在模模型中，间隙长度和2进赋值遵循几何分布，而持久运行长度是几何的，预期爆发长度E[B]=2；这些共同预测了严格的轨道收缩。这些结果表明了一个条件框架，其中收敛性将取决于关于爆发和间隙长度的适当轨道假设，而这些假设又由一个轨道均匀分布猜想所暗示。论文还记录了通过这些观察发展起来的人-LLM协作过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate structural properties of the Collatz iteration through two phenomena observed in large computational exploration: modular scrambling of residue classes and a burst--gap decomposition of trajectories. We prove several structural results, including a modular scrambling lemma showing that the gap-return map acts as an exact bijection on high bits, a persistent exit lemma characterizing gap structure after persistent states, and a decay property for known portions of binary representations under gap-return dynamics. We further prove that, in the modular model, gap lengths and $2$-adic valuations follow geometric distributions, while persistent run lengths are geometric with expected burst length $E[B]=2$; together these predict strict orbit contraction. These results suggest a conditional framework in which convergence would follow from suitable orbitwise hypotheses on burst and gap lengths, which in turn are suggested by an orbit equidistribution conjecture. However, the key hypotheses remain open, and the framework is exploratory rather than a complete reduction. The paper also documents the human-LLM collaboration through which these observations were developed.

</details>

---

### 21. [From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery](https://arxiv.org/abs/2603.11068)

**基本信息**

- 🔗 arXiv: [`2603.11068`](https://arxiv.org/abs/2603.11068)
- 👥 作者: Iman Peivaste, Salim Belouettar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大型语言模型（LLM）的ReAct智能体框架，用于高熵合金的成分发现和逆向设计。这直接应用了“化学大模型”的主题，即利用先进的大语言模型作为智能体，在材料化学领域进行自主推理、决策和探索，以加速新材料的发现。

**📖 中文摘要**

本文提出了一种用于高熵合金（HEA）发现的ReAct（推理+行动）LLM智能体框架，旨在解决从目标晶体相可靠地发现HEA成分这一高维逆向设计问题。该智能体自主提出、验证并迭代优化HEA成分，其方法是查询一个基于4,753个实验记录（涵盖FCC、BCC、BCC+FCC、BCC+IM四个相）训练的校准XGBoost代理模型。与贝叶斯优化和随机搜索基线相比，配备完整提示的智能体在描述符空间中对FCC、BCC和BCC+FCC相的重新发现率分别为38%、18%和38%，且其提案比随机搜索更接近实验相流形。消融实验表明，领域先验知识使智能体从回忆文献中的标志性合金转向探索成分多样性的空间。这项工作确立了LLM引导的智能体推理作为逆向合金设计中一种原则性、透明且对流形感知的、对无梯度优化的补充方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering high-entropy alloy (HEA) compositions that reliably form a target crystal phase is a high-dimensional inverse design problem that conventional trial-and-error experimentation and forward-only machine learning models cannot efficiently solve. Here we present a ReAct (Reasoning + Acting) LLM agent that autonomously proposes, validates, and iteratively refines HEA compositions by querying a calibrated XGBoost surrogate trained on 4,753 experimental records across four phases (FCC, BCC, BCC+FCC, BCC+IM), achieving 94.66\% accuracy (F1 macro = 0.896). Against Bayesian optimisation (BO) and random search baselines, the full-prompt agent achieves descriptor-space rediscovery rates of 38\%, 18\%, and 38\% for FCC, BCC, and BCC+FCC (Mann--Whitney $p \leq 0.039$), with proposals lying 2.4--22.8$\times$ closer to the experimental phase manifold than random search. An ablation reveals that domain priors shift the agent from landmark-alloy recall toward compositionally diverse exploration -- an uninformed agent scores higher rediscovery by concentrating on literature-dense families, while the full-prompt agent explores underrepresented space (unique ratio 1.0 vs.\ 0.39 for BCC+FCC). These regimes represent distinct criteria: proximity to known literature versus genuine discovery. Spearman analysis confirms agent reasoning is statistically aligned with empirical phase distributions ($\rho = 0.736$, $p = 0.004$ for BCC). This work establishes LLM-guided agentic reasoning as a principled, transparent, and manifold-aware complement to gradient-free optimisation for inverse alloy design.

</details>

---

### 22. [Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction](https://arxiv.org/abs/2603.11125)

**基本信息**

- 🔗 arXiv: [`2603.11125`](https://arxiv.org/abs/2603.11125)
- 👥 作者: Yining Qian, Pengjie Wang, Yixiao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种名为Co-Diffusion的新型深度学习框架，用于药物-靶点亲和力预测。该框架基于扩散模型（一种生成式大模型）的思想，并将其应用于化学信息学中的关键问题。这直接属于“化学大模型”的研究范畴，即利用先进的生成模型架构解决化学领域的预测和设计问题。

**📖 中文摘要**

本文提出了Co-Diffusion，一种新颖的亲和力感知框架，将药物-靶点亲和力（DTA）预测重新定义为约束潜在去噪过程以增强泛化能力。Co-Diffusion采用两阶段范式：第一阶段在显式监督目标下对齐药物和靶点嵌入，建立亲和力引导的潜在流形，确保潜在空间反映内在的结合景观。第二阶段引入模态特定的潜在扩散作为随机扰动-去噪正则化器，迫使模型从噪声结构表示中恢复一致的亲和力语义。该方法有效缓解了生成式DTA模型中常见的重建-回归冲突。理论表明，Co-Diffusion最大化了药物结构、蛋白质序列和结合强度的联合似然的变分下界。跨多个基准的大量实验表明，Co-Diffusion显著优于最先进的基线模型，特别是在未见过的分子支架和新蛋白质家族上产生卓越的零样本泛化能力，为在未探索化学空间中进行计算机药物优先排序铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.

</details>

---

### 23. [A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation](https://arxiv.org/abs/2603.11242)

**基本信息**

- 🔗 arXiv: [`2603.11242`](https://arxiv.org/abs/2603.11242)
- 👥 作者: Xiaoan Lang, Fang Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11242.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于生成有效潜在空间解耦的通用VAE框架及评估工具。这与化学信息学中构建可解释、可控的化学大模型（特别是基于VAE的分子生成模型）的核心目标直接相关，因为解耦的潜在空间是此类模型的关键需求。

**📖 中文摘要**

本文提出了一个统一的变分自编码器（VAE）框架（bfVAE），用于生成有效的潜在空间解耦，特别适用于表格数据。该框架统一了多种最先进的解耦VAE方法，并提出了两种无需真实生成因子即可评估解耦有效性的新程序（FVH-LT和DBSR-LS）以及一个总体解耦指数（LSDI）。这项工作与化学信息学中开发用于分子表示学习的解耦生成模型高度相关。化学大模型（如用于分子生成的VAE）通常旨在学习解耦的、可解释的潜在表示，以捕获独立的化学性质（如溶解度、活性）。本文提出的评估和提升潜在空间解耦质量的通用框架，为构建和验证化学领域更可解释、更可控的生成模型提供了直接的方法论工具和评估标准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FVH-LT and DBSR-LS to summarize the overall effectiveness of a VAE disentanglement method without requiring access to or knowledge of the ground-truth generative factors. To the best of our knowledge, these are the first assessment tools to achieve this. FVH-LT and DBSR-LS also enhance latent space interpretability and provide guidance on more efficient content generation. To ensure robust and consistent disentanglement, we develop a greedy alignment strategy (GAS) that mitigates label switching and aligns latent dimensions across runs to obtain aggregated results. We assess the bfVAE framework and validate FVH-LT, DBSR-LS, and LSDI in extensive experiments on tabular and image data. The results suggest that bfVAE surpasses existing disentangled VAE frameworks in terms of disentanglement quality, robustness, achieving a near-zero false discovery rate for informative latent dimensions, that FVH-LT and DBSR-LS reliably uncover semantically meaningful and domain-relevant latent structures, and that LSDI makes an effective overall quantitative summary on disentanglement effectiveness.

</details>

---

### 24. [A Standardized Framework For Evaluating Gene Expression Generative Models](https://arxiv.org/abs/2603.11244)

**基本信息**

- 🔗 arXiv: [`2603.11244`](https://arxiv.org/abs/2603.11244)
- 👥 作者: Andrea Rubbi, Andrea Giuseppe Di Francesco, Mohammad Lotfollahi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11244.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心主题是构建生成模型的标准化评估框架，这直接关系到如何可靠地评估和比较化学大模型（如分子生成模型）的性能。同时，论文对生成模型评估现状的分析和提出的解决方案，构成了对该领域重要挑战的讨论，具有综述和展望价值。

**📖 中文摘要**

本文提出了Generated Genetic Expression Evaluator (GGE)，一个用于标准化评估单细胞基因表达生成模型的开源Python框架。它解决了当前评估实践中指标实现不一致、超参数选择不可比以及缺乏生物学基础指标等问题。GGE提供了一套全面的分布度量，并支持通过差异表达基因（DEG）分析和扰动效应相关性进行生物学动机评估。虽然直接应用于基因表达数据，但该框架提出的生成模型标准化评估的核心理念、挑战和解决方案，与化学信息学中评估分子生成模型（化学大模型）所面临的挑战高度相似。化学生成模型同样需要标准化、可重复且包含化学意义（如合成可行性、性质分布）的评估协议。因此，这项工作为化学大模型的评估框架设计提供了重要的参考和范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid development of generative models for single-cell gene expression data has created an urgent need for standardised evaluation frameworks. Current evaluation practices suffer from inconsistent metric implementations, incomparable hyperparameter choices, and a lack of biologically-grounded metrics. We present Generated Genetic Expression Evaluator (GGE), an open-source Python framework that addresses these challenges by providing a comprehensive suite of distributional metrics with explicit computation space options and biologically-motivated evaluation through differentially expressed gene (DEG)-focused analysis and perturbation-effect correlation, enabling standardized reporting and reproducible benchmarking. Through extensive analysis of the single-cell generative modeling literature, we identify that no standardized evaluation protocol exists. Methods report incomparable metrics computed in different spaces with different hyperparameters. We demonstrate that metric values vary substantially depending on implementation choices, highlighting the critical need for standardization. GGE enables fair comparison across generative approaches and accelerates progress in perturbation response prediction, cellular identity modeling, and counterfactual inference.

</details>

---

### 25. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个连接低维数据嵌入（scGPT）与高层语义（LLM）的可解释交互式AI框架。这种“嵌入-语义”桥接架构和交互式探索范式，与化学信息学中连接分子表示（如指纹、图嵌入）与化学性质、反应或文本描述的化学大模型，以及连接质谱图与分子结构假设的推理系统，在核心方法论上直接相关。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个将单细胞RNA测序（scRNA-seq）数据嵌入（通过scGPT）与自然语言交互（通过LLM）相结合的可解释框架，用于交互式单细胞发现。它通过自动查询分类器将用户输入路由到不同的分析管道（如基因标记评分、语义匹配），并集成了通路活性评分、配体-受体相互作用预测等模块。ELISA的核心创新在于桥接了低维的转录组嵌入表示与高层的自然语言语义，使得用户可以通过自然语言查询探索复杂的生物数据。这一“嵌入-语义”桥接框架与化学信息学中“化学结构嵌入-性质/功能语义”的研究范式高度一致。例如，在质谱结构推理中，需要将质谱图嵌入与可能的分子结构语义相关联；在化学大模型中，需要将分子表示与文本描述、性质预测等任务相关联。ELISA为化学领域构建类似的多模态、可解释的AI代理系统提供了概念验证和架构参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 26. [drGT: Attention-Guided Gene Assessment of Drug Response Utilizing a Drug-Cell-Gene Heterogeneous Network](https://arxiv.org/abs/2405.08979)

**基本信息**

- 🔗 arXiv: [`2405.08979`](https://arxiv.org/abs/2405.08979)
- 👥 作者: Yoshitaka Inoue, Hunmin Lee, Tianfan Fu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.08979.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个用于药物反应预测的可解释图神经网络模型。该模型处理化学实体（药物）与生物实体（基因、细胞）的异质图关系，并使用注意力机制进行解释，这与化学信息学中利用图神经网络处理分子并寻求可解释预测的核心主题直接相关，是化学大模型在生物医药应用中的一个具体实例。

**📖 中文摘要**

本文提出了drGT模型，一个利用药物-细胞-基因异质图进行药物反应预测和生物标志物识别的图深度学习模型。模型通过注意力系数（ACs）来识别重要的基因关联，从而提供预测结果的解释性。作者在多个基准数据集（GDSC, NCI60, CTRP）上评估了模型，并展示了其通过文本挖掘验证药物-基因关联、以及通过富集分析识别药物影响的生物过程的能力。这项工作虽然聚焦于药物反应预测，但其核心是使用图神经网络处理化学-生物实体（药物、基因、细胞系）之间的复杂关系，并利用注意力机制提供可解释性。这与化学信息学中利用图神经网络处理分子图、预测分子性质或反应，并寻求模型可解释性的研究高度相关。drGT中异质图构建、注意力解释和外部知识（文献）验证的流程，为构建可解释的化学大模型（尤其是涉及多实体关系的模型）提供了具体的技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A challenge in drug response prediction is result interpretation compared to established knowledge. drGT is a graph deep learning model that predicts sensitivity and aids in biomarker identification using attention coefficients (ACs). drGT leverages a heterogeneous graph composed of relationships drawn from drugs, genes, and cell line responses. The model is trained and evaluated using major benchmark datasets: Sanger GDSC, NCI60, and Broad CTRP, which cover a wide range of drugs and cancer cell lines. drGT demonstrates AUROC of up to 94.5% under random splitting, 84.4% for unseen drugs, and 70.6% for unseen cell lines, comparable to existing benchmark methods while also providing interpretability. Regarding interpretability, we review drug-gene co-occurrences by text-mining PubMed abstracts for high-coefficient genes mentioning particular drugs. Across 976 drugs from NCI60 with known drug-target interactions (DTIs), model predictions utilized both known DTIs (36.9%) as well as additional predictive associations, many supported by literature. In addition, we compare the drug-gene associations identified by drGT with those from an established DTI prediction model and find that 63.67% are supported by either PubMed literature or predictions from the DTI model. Further, we describe the utilization of ACs to identify affected biological processes by each drug via enrichment analyses, thereby enhancing biological interpretability. Code is available at this https URL .

</details>

---

### 27. [Using LLM-Generated Draft Replies to Support Human Experts in Responding to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of Industrial AI](https://arxiv.org/abs/2412.12732)

**基本信息**

- 🔗 arXiv: [`2412.12732`](https://arxiv.org/abs/2412.12732)
- 👥 作者: Tita Alissa Bach, Aleksandar Babic, Narae Park 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.12732.pdf)

**💡 相关性分析**

满足标准3：论文是一项关于LLM在专业工业领域应用的案例研究，包含了对大模型集成、效用、局限性和人机协作模式的重要讨论。这些讨论对于化学信息学领域如何负责任地、有效地部署化学大模型（如用于分子设计或文献分析的LLM）具有重要的参考和展望价值。

**📖 中文摘要**

本文是一项关于在航海工业中利用LLM生成草稿回复以支持人类专家处理利益相关者询价的真实案例研究。研究通过初步研究、调查和文本相似性分析，探讨了LLM在专业领域工作流中作为增强工具的效用、局限性和人机协作模式。研究发现，LLM生成的草稿可以简化工作流，但通常需要根据领域特定需求进行大量修改，最终决策权必须保留给人类专家。这项研究虽然应用场景特定，但其核心是探索LLM（作为大模型的一种）在高度专业化、安全关键的工业领域中的实际集成、效用评估和人机协作范式。这与化学信息学领域探索如何将化学大模型（如用于分子设计、文献挖掘的LLM）安全、可靠、有效地集成到药物发现、材料设计等专业工作流中所面临的挑战高度相似。该案例研究为化学领域类似的应用提供了宝贵的实践经验、评估方法和设计原则参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

</details>

---

### 28. [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177)

**基本信息**

- 🔗 arXiv: [`2501.15177`](https://arxiv.org/abs/2501.15177)
- 👥 作者: Yi Su, Jisheng Bai, Qisheng Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.15177.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对音频-语言模型（ALMs）的系统性综述，涵盖了模型基础、分类、研究全景、评估和未来方向。这为化学信息学领域撰写关于“化学大模型”或“质谱-语言/结构模型”的同类综述提供了直接的方法论模板和内容组织参考，属于重要的相关讨论和展望。

**📖 中文摘要**

本文对音频-语言模型（ALMs）进行了首次系统性综述。ALMs是在音频-文本配对数据上训练的模型，旨在处理、理解和推理以音频为中心的多模态内容。综述涵盖了语音、音乐和声音等通用音频任务，提出了统一的ALM基础分类法（包括模型架构和训练目标），并建立了一个捕捉不同研究方面相互促进和制约的研究全景图，总结了评估、局限性、关注点和有前景的方向。虽然主题是音频，但这项综述工作的范围、深度和方法论与对“化学-语言模型”或“质谱-语言模型”进行类似系统性综述的需求完全对应。化学信息学中的大模型研究同样涉及多模态（如分子结构-文本、光谱-文本）、不同的架构、训练范式、评估挑战以及应用前景。因此，这篇综述为在化学信息学领域组织类似主题的研究、识别关键问题和发展趋势提供了极佳的范式和参考框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified taxonomy of ALM foundations, including model architectures and training objectives; (3) establishment of a research landscape capturing mutual promotion and constraints among different research aspects, aiding in summarizing evaluations, limitations, concerns and promising directions. Our review contributes to helping researchers understand the development of existing technologies and future trends, while also providing valuable references for implementation in practical applications.

</details>

---

### 29. [GTM: A General Time-series Model for Enhanced Representation Learning of Time-Series Data](https://arxiv.org/abs/2502.03264)

**基本信息**

- 🔗 arXiv: [`2502.03264`](https://arxiv.org/abs/2502.03264)
- 👥 作者: Cheng He, Xu Huang, Gangwei Jiang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03264.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一个用于时间序列的通用生成式基础模型（GTM），重点在于增强表示学习和任务通用性。这与化学信息学中构建能够处理多种化学数据表示（可视为特殊序列或图）、并服务于多种下游任务的化学基础模型（化学大模型）的核心研究主题直接相关。

**📖 中文摘要**

本文提出了通用时间序列模型（GTM），通过新颖的频域注意力机制捕获时间粒度感知特征，并采用结合重构和自回归目标的混合掩码预训练策略，以增强时间序列数据的表示学习。GTM被设计为第一个生成任务无关的时间序列分析模型，无需特定任务修改即可适应各种生成任务。论文在多个生成任务和分类任务上进行了广泛实验。虽然应用领域是时间序列，但其核心贡献——设计一个通用的、具有强大表示学习能力的生成式基础模型——与化学信息学中构建“化学基础模型”的愿景高度一致。化学领域同样需要能够处理分子序列（SMILES）、图、光谱序列（如质谱）等多种表示形式，并能通过预训练适应下游各种生成（如分子设计）和判别（如性质预测）任务的通用模型。GTM在架构设计（如频域注意力处理序列）、预训练策略（混合目标）和任务通用性方面的创新，为化学大模型的设计提供了重要的思路借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite recent progress in time-series foundation models, challenges persist in improving representation learning and adapting to diverse downstream tasks. We introduce a General Time-series Model (GTM), which advances representation learning via a novel frequency-domain attention mechanism that captures time-granularity-aware features, an aspect underexplored in prior research. We further propose a novel pre-training strategy that unifies reconstruction and autoregressive objectives through a hybrid masking mechanism. Our pre-training strategy, combined with 2D positional encoding and span shuffling, enhances the robustness and generalization of representations. GTM is established as the first generative-task-agnostic model for time-series analysis, enabling seamless adaptation to various generative tasks without any task-specific modifications. Extensive experiments demonstrate that GTM consistently outperforms SOTA models on various generative tasks and achieves strong classification results with minimal adaptation. Furthermore, GTM exhibits clear scaling behavior, with accuracy improving as model size and pre-training data increase.

</details>

---

### 30. [HOG-Diff: Higher-Order Guided Diffusion for Graph Generation](https://arxiv.org/abs/2502.04308)

**基本信息**

- 🔗 arXiv: [`2502.04308`](https://arxiv.org/abs/2502.04308)
- 👥 作者: Yiming Huang, Tolga Birdal
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.04308.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个受高阶拓扑引导的图生成扩散模型。分子是一种特殊的图，因此该模型的方法论与化学信息学中用于分子生成的扩散模型直接相关。其引入高阶拓扑指导以生成更合理图结构的思想，对于提升分子生成模型的质量和可靠性具有重要意义。

**📖 中文摘要**

本文提出了高阶引导扩散模型（HOG-Diff），一个用于图生成的原理性框架。该模型遵循由粗到细的生成课程，通过扩散桥受高阶拓扑结构引导。作者证明了该模型比经典扩散框架具有更强的理论保证，并在八个图生成基准测试中展示了其卓越性能。图生成是化学信息学中的核心任务，例如分子生成。现有大多数分子生成扩散模型直接改编自图像生成框架，可能忽略了分子图固有的高阶拓扑结构（如环、官能团）。HOG-Diff明确地将高阶拓扑指导纳入扩散过程，这一思路对于生成具有复杂且正确拓扑约束的分子结构（如特定环系、三维构象）具有直接的启发意义。该工作为改进化学领域（分子、材料）的图生成扩散模型提供了新的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph generation is a critical yet challenging task, as empirical analyses require a deep understanding of complex, non-Euclidean structures. Diffusion models have recently made significant advances in graph generation, but these models are typically adapted from image generation frameworks and overlook inherent higher-order topology, limiting their ability to capture graph topology. In this work, we propose Higher-order Guided Diffusion (HOG-Diff), a principled framework that progressively generates plausible graphs with inherent topological structures. HOG-Diff follows a coarse-to-fine generation curriculum, guided by higher-order topology and implemented via diffusion bridges. We further prove that our model admits stronger theoretical guarantees than classical diffusion frameworks. Extensive experiments across eight graph generation benchmarks, spanning diverse domains and including large-scale settings, demonstrate the scalability of our method and its superior performance on both pairwise and higher-order topological metrics. Our project page is available \href{ this https URL }{here}.

</details>

---

### 31. [Riemannian Variational Flow Matching for Material and Protein Design](https://arxiv.org/abs/2502.12981)

**基本信息**

- 🔗 arXiv: [`2502.12981`](https://arxiv.org/abs/2502.12981)
- 👥 作者: Olga Zaghen, Floor Eijkelboom, Alison Pouplin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.12981.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于流形上生成建模的变分流匹配方法。化学和材料科学中的许多结构空间（如分子构象、材料相空间）都是流形，因此该工作与在化学领域构建能够在这些流形上操作的生成模型（化学大模型的一个重要分支）直接相关。

**📖 中文摘要**

本文提出了黎曼高斯变分流匹配（RG-VFM），这是变分流匹配（VFM）在流形上生成建模的几何扩展。该方法基于黎曼高斯分布推导了具有闭式测地线的流形上的变分目标，并分析了其与黎曼流匹配（RFM）的关系，揭示了RG-VFM自然包含了一个曲率相关的惩罚项。论文在合成球面和双曲基准、以及材料和蛋白质生成等真实任务上进行了实验。将生成模型扩展到流形上对于化学和材料科学至关重要，因为许多化学结构空间（如分子构象空间、晶体结构空间、蛋白质折叠空间）本质上是弯曲的流形。RG-VFM为在这些流形上构建更准确、更高效的生成模型（例如，生成合理的分子三维构象或晶体结构）提供了新的理论基础和算法工具。这项工作直接推动了在具有复杂几何结构的化学空间中进行生成建模的研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Riemannian Gaussian Variational Flow Matching (RG-VFM), a geometric extension of Variational Flow Matching (VFM) for generative modeling on manifolds. Motivated by the benefits of VFM, we derive a variational flow matching objective for manifolds with closed-form geodesics based on Riemannian Gaussian distributions. Crucially, in Euclidean space, predicting endpoints (VFM), velocities (FM), or noise (diffusion) is largely equivalent due to affine interpolations. However, on curved manifolds this equivalence breaks down. We formally analyze the relationship between our model and Riemannian Flow Matching (RFM), revealing that the RFM objective lacks a curvature-dependent penalty -- encoded via Jacobi fields -- that is naturally present in RG-VFM. Based on this relationship, we hypothesize that endpoint prediction provides a stronger learning signal by directly minimizing geodesic distances. Experiments on synthetic spherical and hyperbolic benchmarks, as well as real-world tasks in material and protein generation, demonstrate that RG-VFM more effectively captures manifold structure and improves downstream performance over Euclidean and velocity-based baselines. Code available at this https URL .

</details>

---

### 32. [Tuning-Free LLM Can Build A Strong Recommender Under Sparse Connectivity And Knowledge Gap Via Extracting Intent](https://arxiv.org/abs/2505.10900)

**基本信息**

- 🔗 arXiv: [`2505.10900`](https://arxiv.org/abs/2505.10900)
- 👥 作者: Wenqing Zheng, Noah Fatsi, Daniel Barcklow 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用免调优LLM从文本中提取意图，并构建意图知识图谱以增强推荐。这种方法论与质谱结构推理中需要从质谱或相关文本中提取化学子结构“意图”，并建立谱图-结构关联网络的核心任务在概念和技术路径上高度相关，为后者提供了创新的解决方案思路。

**📖 中文摘要**

本文提出了LLM-based Intent Knowledge Graph Recommender (IKGR)，一个新颖的推荐框架。其核心是使用免调优、RAG引导的LLM流程，从外部知识源和用户档案中提取意图，构建一个以意图为中心的知识图谱，将用户和物品显式地链接到意图节点。为了缓解稀疏性，提出了互意图连接致密化策略。最后在意图增强的图谱上使用轻量级GNN层进行推荐。该工作创新性地将LLM用于从文本中提取结构化意图（而非简单的分类或嵌入），并将其作为知识图谱的核心实体来连接用户和物品。这种方法论与质谱结构推理中面临的核心挑战高度相似：如何从质谱数据（或附带的文本描述）中提取出反映分子子结构或化学环境的“意图”或“特征”，并以此为基础构建质谱-子结构-分子之间的关联图谱，从而进行推理。IKGR为利用LLM从复杂数据（质谱、分子描述文本）中提取关键化学语义特征，并用于构建可推理的知识系统提供了可行的技术蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in recommendation with large language models (LLMs) often rely on either commonsense augmentation at the item-category level or implicit intent modeling on existing knowledge graphs. However, such approaches struggle to capture grounded user intents and to handle sparsity and cold-start scenarios. In this work, we present LLM-based Intent Knowledge Graph Recommender (IKGR), a novel framework that constructs an intent-centric knowledge graph where both users and items are explicitly linked to intent nodes extracted by a tuning-free, RAG-guided LLM pipeline. By grounding intents in external knowledge sources and user profiles, IKGR canonically represents what a user seeks and what an item satisfies as first-class entities. To alleviate sparsity, we further introduce a mutual-intent connectivity densification strategy, which shortens semantic paths between users and long-tail items without requiring cross-graph fusion. Finally, a lightweight GNN layer is employed on top of the intent-enhanced graph to produce recommendation signals with low latency. Extensive experiments on public and enterprise datasets demonstrate that IKGR consistently outperforms strong baselines, particularly on cold-start and long-tail slices, while remaining efficient through a fully offline LLM pipeline.

</details>

---

### 33. [LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models](https://arxiv.org/abs/2505.19240)

**基本信息**

- 🔗 arXiv: [`2505.19240`](https://arxiv.org/abs/2505.19240)
- 👥 作者: Aida Kostikova, Zhipin Wang, Deidamea Bajri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19240.pdf)

**💡 相关性分析**

满足标准3：这是一篇专门针对大语言模型（作为大模型的核心代表）局限性研究的综述论文，提供了该领域研究趋势、主题分布和数据资源的系统性分析，与“化学大模型”这一关注主题高度相关。

**📖 中文摘要**

这篇论文《LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models》是一篇关于大语言模型（LLMs）局限性研究的综述。它采用数据驱动、半自动化的方法，对2022年至2025年初期间关于LLMs局限性的研究进行了系统性回顾。论文从大量ACL和arXiv论文中筛选出14,648篇相关论文，并分析了研究趋势。研究发现，关于LLM局限性的研究增长迅速，到2025年已占LLM相关论文的30%以上。研究主题包括推理、泛化、幻觉、偏见和安全性等。论文还发布了一个带注释的摘要数据集和经过验证的方法论。这篇综述直接围绕“化学大模型”这一核心主题，因为它是对大语言模型（作为大模型的一个核心类别）研究的系统性回顾，提供了该领域的研究现状、趋势和关键挑战的全面概述。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains the most studied limitation, followed by generalization, hallucination, bias, and security. The distribution of topics in the ACL dataset stays relatively stable over time, while arXiv shifts toward security risks, alignment, hallucinations, knowledge editing, and multimodality. We offer a quantitative view of trends in LLLMs research and release a dataset of annotated abstracts and a validated methodology, available at: this https URL .

</details>

---

### 34. [Can Theoretical Physics Research Benefit from Language Agents?](https://arxiv.org/abs/2506.06214)

**基本信息**

- 🔗 arXiv: [`2506.06214`](https://arxiv.org/abs/2506.06214)
- 👥 作者: Sirui Lu, Zhijing Jin, Terry Jingchen Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.06214.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何为理论物理学构建专门化的语言智能体（即领域大模型），这与“化学大模型”的主题在概念上直接相关，都是探讨大模型在特定科学领域的应用、局限和专门化路径。

**📖 中文摘要**

这篇论文《Can Theoretical Physics Research Benefit from Language Agents?》探讨了大型语言模型（LLMs）在理论物理学研究中的应用潜力和当前局限。论文指出，尽管LLMs在数学推理和代码生成方面表现出色，但在物理直觉、约束满足和可靠推理方面存在关键差距。作者认为，物理学研究需要近似判断、对称性利用和物理基础，这要求AI智能体经过专门的物理推理模式训练，并配备物理感知的验证工具。论文呼吁物理和AI社区合作，开发物理特定的训练数据集、捕捉物理推理质量的奖励信号以及编码基本原理的验证框架。这篇论文的核心是讨论如何构建专门化的AI智能体（可视为一种特定领域的大模型）来推动科学发现，与“化学大模型”的主题在理念上高度相关，即探讨如何为特定科学领域（如化学、物理）构建和利用专门化的大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) are rapidly advancing across diverse domains, yet their application in theoretical physics remains inadequate. While current models show competence in mathematical reasoning and code generation, we identify critical gaps in physical intuition, constraint satisfaction, and reliable reasoning that cannot be addressed through prompting alone. Physics demands approximation judgment, symmetry exploitation, and physical grounding that require AI agents specifically trained on physics reasoning patterns and equipped with physics-aware verification tools. We argue that LLM would require such domain-specialized training and tooling to be useful in real-world for physics research. We envision physics-specialized AI agents that seamlessly handle multimodal data, propose physically consistent hypotheses, and autonomously verify theoretical results. Realizing this vision requires developing physics-specific training datasets, reward signals that capture physical reasoning quality, and verification frameworks encoding fundamental principles. We call for collaborative efforts between physics and AI communities to build the specialized infrastructure necessary for AI-driven scientific discovery.

</details>

---

### 35. [Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism](https://arxiv.org/abs/2509.06322)

**基本信息**

- 🔗 arXiv: [`2509.06322`](https://arxiv.org/abs/2509.06322)
- 👥 作者: Jiajun Bao, Nicolas Boullé, Toni J.B. Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.06322.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索文本训练的大语言模型（LLMs）在零样本条件下理解和外推偏微分方程（PDE）动力学的能力。这直接展示了“化学大模型”可能具备的一种核心能力——即对化学系统中常见的动力学过程（通常由微分方程描述）进行建模和推理。论文揭示的机制对设计用于化学计算的专门大模型具有重要参考价值。

**📖 中文摘要**

这篇论文《Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism》展示了仅通过文本训练的大型语言模型（LLMs）具备零样本外推偏微分方程（PDE）动力学的能力。研究发现，LLMs能够从离散化的PDE解中准确推断时空动力学，而无需微调或自然语言提示。预测准确性随着时间上下文长度的增加而提高，但在更精细的空间离散化下会下降。在多步推演中，误差随时间范围呈代数增长。论文将这种趋势解释为上下文神经缩放定律，并揭示了LLMs内部处理PDE解以进行准确推演的三阶段上下文学习机制：从语法模式模仿开始，经过探索性高熵阶段，最终形成自信的、基于数值的预测。这项研究揭示了纯文本训练的大模型在理解和推理复杂科学计算问题（如PDE）方面的涌现能力，为“化学大模型”在解决化学动力学、分子模拟等涉及微分方程的科学计算问题提供了重要的能力佐证和机制见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated emergent in-context learning (ICL) capabilities across a range of tasks, including zero-shot time-series forecasting. We show that text-trained foundation models can accurately extrapolate spatiotemporal dynamics from discretized partial differential equation (PDE) solutions without fine-tuning or natural language prompting. Predictive accuracy improves with longer temporal contexts but degrades at finer spatial discretizations. In multi-step rollouts, where the model recursively predicts future spatial states over multiple time steps, errors grow algebraically with the time horizon, reminiscent of global error accumulation in classical finite-difference solvers. We interpret these trends as in-context neural scaling laws, where prediction quality varies predictably with both context length and output length. To better understand how LLMs are able to internally process PDE solutions so as to accurately roll them out, we analyze token-level output distributions and uncover a consistent three-stage ICL progression: beginning with syntactic pattern imitation, transitioning through an exploratory high-entropy phase, and culminating in confident, numerically grounded predictions.

</details>

---

### 36. [Streamline pathology foundation model by cross-magnification distillation](https://arxiv.org/abs/2509.23097)

**基本信息**

- 🔗 arXiv: [`2509.23097`](https://arxiv.org/abs/2509.23097)
- 👥 作者: Ziyu Su, Abdul Rehman Akbar, Usama Sajjad 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23097.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是构建一个用于特定科学领域（病理学）的高效、轻量化基础模型（Foundation Model），这直接属于“化学大模型”的范畴（即科学领域大模型）。2) 论文提出的跨放大倍数蒸馏框架是一种可用于构建领域大模型的方法论和工具，其思想可迁移至化学信息学领域，用于创建处理不同尺度化学数据（如分子图、光谱、显微图像）的高效模型。

**📖 中文摘要**

这篇论文《Streamline pathology foundation model by cross-magnification distillation》介绍了一种用于计算病理学的轻量级基础模型XMAG。该模型通过跨放大倍数蒸馏，将最先进的20倍放大倍数教师模型的知识转移到高效的5倍放大倍数学生架构中。XMAG采用紧凑的主干网络，完全在5倍放大倍数下运行，与现有方法相比，每张全切片图像所需的图块数量减少了11.3倍。蒸馏框架结合了全局图像表示和局部空间令牌映射的双层知识转移。该模型在从公开数据集中整理的349万张图像上进行训练，并在跨越多种癌症类型的六个临床相关组织病理学分析任务中进行了评估。XMAG在达到大幅加速（30倍）的同时，其诊断准确性接近参数量大得多的基础模型。这项工作展示了通过知识蒸馏构建高效、轻量化领域基础模型（如病理学大模型）的有效路径。虽然领域是病理学，但其方法论（跨分辨率蒸馏构建轻量级领域大模型）对构建“化学大模型”（例如，用于光谱分析或分子性质预测的轻量高效模型）具有直接的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models (FM) have transformed computational pathology but remain computationally prohibitive for clinical deployment due to their massive parameter counts and high-magnification processing requirements. Here, we introduce XMAG, a lightweight FM developed through corss-magnification distillation that transfers knowledge from state-of-the-art 20x magnification teacher to an efficient 5x magnification student architecture. XMAG employs a compact backbone and operates entirely at 5x, requiring 11.3 times fewer patches per whole slide image (WSI) compared to existing approaches. Our Novel distillation framework incorporates dual-level knowledge transfer, aligning both global image representations and local spatial token mapping. We trained XMAG on 3.49 million images curated from publicly available datasets and evaluated performance across six clinically relevant histopathology analysis tasks spanning multiple cancer types. XMAG achieved diagnostic accuracy within 1% of substantially larger foundation models while delivering 30-fold processing acceleration, reaching 8.8 WSIs per minute processing speed. Our cross-institutional validation confirmed robust generalization. Further, we developed an end-to-end training strategy to further boost our model's performance to approach the larger FMs' performance. These results establish cross-magnification distillation as a viable approach for deploying FM capabilities in resource-constrained clinical environments, potentially enabling real-time pathology AI integration.

</details>

---

### 37. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建和评估一个能够进行自主科学探索的AI科学家系统。这直接关联到“化学大模型”或“化学AI智能体”的终极应用目标之一——辅助甚至自主进行化学发现和研究。论文探讨的工作流程、能力评估和风险分析，为在化学领域开发类似系统提供了宝贵的框架和见解。

**📖 中文摘要**

这篇论文《Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper》介绍并评估了Jr. AI Scientist，一个最先进的自主AI科学家系统。该系统模仿新手学生研究人员的核心研究工作流程：在给定人类导师的基线论文后，分析其局限性，提出改进的新假设，进行迭代实验直至取得改进，并撰写结果论文。该系统利用现代编码智能体处理复杂、多文件的实现。论文通过实验表明，Jr. AI Scientist能够基于真实的NeurIPS、IJCV和ICLR工作，通过提出和实现新方法，成功生成新的研究论文。评估包括使用AI评审员进行自动评估、作者主导的评估以及向专注于AI驱动贡献的Agents4Science会议投稿。研究发现，该系统生成的论文获得的评审分数高于现有的全自动化系统，但也揭示了重要局限性。论文最后全面报告了开发过程中识别的各种风险。这项研究直接涉及“化学大模型”的应用场景——即利用AI大模型（或智能体）驱动化学领域的自主科学研究。它展示了从分析文献、提出假设、实验到成文的完整科研自动化流程，为未来“化学AI科学家”的开发和风险评估提供了重要参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems (autoresearch) is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, iteratively experiments until improvements are achieved, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel methods. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 38. [Beyond the Black Box: A Survey on the Theory and Mechanism of Large Language Models](https://arxiv.org/abs/2601.02907)

**基本信息**

- 🔗 arXiv: [`2601.02907`](https://arxiv.org/abs/2601.02907)
- 👥 作者: Zeyu Gan, Ruifeng Ren, Wei Yao 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.02907.pdf)

**💡 相关性分析**

满足标准3：这篇论文是关于大语言模型（LLMs）的综合性综述，系统地回顾了LLM的理论基础、内部机制和前沿挑战。虽然其标题和摘要未直接提及“化学大模型”，但LLM作为“化学大模型”的核心技术基础，这篇关于LLM理论与机制的深度综述，为理解和构建化学、质谱等领域的专业大模型提供了重要的理论基础和讨论框架，因此与“化学大模型”这一主题高度相关。

**📖 中文摘要**

这篇题为《超越黑箱：大语言模型理论与机制综述》的论文，是对大语言模型（LLMs）理论与内部机制的系统性综述。论文的核心目标是解决当前LLM领域的一个关键悖论：尽管模型在工程上取得了巨大成功，但对其内部工作原理的理论理解仍然非常有限，导致这些系统在很大程度上被视为“黑箱”。为此，作者提出了一个基于生命周期的统一分类法，将研究领域划分为数据准备、模型准备、训练、对齐、推理和评估六个阶段，并在此框架下系统性地回顾了驱动LLM性能的基础理论和内部机制。论文分析了诸如数据混合的数学原理、不同架构的表征极限以及对齐算法的优化动力学等核心理论问题。此外，它还指出了前沿挑战，包括合成数据自我改进的理论极限、安全保证的数学边界以及涌现智能的机制起源。这篇综述通过将经验观察与严谨的科学探究相结合，为将LLM开发从工程启发式转向原则性科学学科提供了结构化路线图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid emergence of Large Language Models (LLMs) has precipitated a profound paradigm shift in Artificial Intelligence, delivering monumental engineering successes that increasingly impact modern society. However, a critical paradox persists within the current field: despite the empirical efficacy, our theoretical understanding of LLMs remains disproportionately nascent, forcing these systems to be treated largely as ``black boxes''. To address this theoretical fragmentation, this survey proposes a unified lifecycle-based taxonomy that organizes the research landscape into six distinct stages: Data Preparation, Model Preparation, Training, Alignment, Inference, and Evaluation. Within this framework, we provide a systematic review of the foundational theories and internal mechanisms driving LLM performance. Specifically, we analyze core theoretical issues such as the mathematical justification for data mixtures, the representational limits of various architectures, and the optimization dynamics of alignment algorithms. Moving beyond current best practices, we identify critical frontier challenges, including the theoretical limits of synthetic data self-improvement, the mathematical bounds of safety guarantees, and the mechanistic origins of emergent intelligence. By connecting empirical observations with rigorous scientific inquiry, this work provides a structured roadmap for transitioning LLM development from engineering heuristics toward a principled scientific discipline.

</details>

---

### 39. [De novo molecular structure elucidation from mass spectra via flow matching](https://arxiv.org/abs/2602.19912)

**基本信息**

- 🔗 arXiv: [`2602.19912`](https://arxiv.org/abs/2602.19912)
- 👥 作者: Ghaith Mqawass, Tuan Le, Fabian Theis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.19912.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕“质谱结构推理”这一主题。它提出了一个名为MSFlow的生成模型，专门用于解决从质谱数据中推断分子结构的逆问题，并取得了最先进的性能。

**📖 中文摘要**

这篇题为《通过流匹配从质谱数据中进行从头分子结构解析》的论文，直接针对“质谱结构推理”这一核心主题。质谱是识别分子结构的有力工具，但将质谱图翻译成完整的分子结构是一个困难且定义不明确的逆问题。为了克服这一难题，作者开发了MSFlow，一个两阶段的编码器-解码器流匹配生成模型，用于从小分子质谱数据中推断分子结构。第一阶段，采用一个受化学式限制的Transformer模型，将质谱编码到一个连续且包含化学信息的嵌入空间。第二阶段，训练一个解码器流匹配模型，从质谱的潜在嵌入中重建分子。论文进行了严格的评估，结果表明MSFlow能够将高达45%的分子质谱图准确翻译成相应的分子表示，这比当前最先进的方法提升了高达14倍。作者还公开了MSFlow的训练版本供非商业用户使用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

</details>

---

### 40. [On the Value of Tokeniser Pretraining in Physics Foundation Models](https://arxiv.org/abs/2603.05598)

**基本信息**

- 🔗 arXiv: [`2603.05598`](https://arxiv.org/abs/2603.05598)
- 👥 作者: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05598.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是“物理基础模型”的训练方法，这属于广义的“科学大模型”范畴，与“化学大模型”在方法论上高度相关。它探讨了分词器预训练这一关键步骤对模型性能的影响，为构建高效、准确的科学领域（包括化学）大模型提供了重要的技术见解和实证研究。

**📖 中文摘要**

这篇题为《论物理基础模型中分词器预训练的价值》的论文，探讨了分词器预训练对物理仿真模型（可视为一类“科学大模型”）的准确性和效率的影响。现代高分辨率模拟产生了跨越不同物理体系和尺度的海量数据。训练基础模型来学习这些数据背后的动力学，使得对复杂多物理现象（包括化学过程）的建模成为可能。论文指出，新兴的物理基础模型通常旨在联合学习两个任务：提取高分辨率时空数据的紧凑表示，以及捕捉支配性的物理动力学。然而，同时从头学习这两个任务可能会阻碍任一过程的有效性。作者证明，在训练动力学模型之前，使用自编码目标对分词器进行预训练，可以显著提升物理仿真的计算效率。这种改进的程度取决于领域对齐性：在与仿真任务相同的物理系统上进行预训练收益最大。这项工作为训练高效的物理仿真器（可类比于化学领域的仿真或预测模型）提供了实用指导，并强调了策略性预训练数据选择的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an autoencoding objective prior to training the dynamics model enhances computational efficiency for physics emulation. Notably, the magnitude of this benefit depends on domain alignment: pretraining on the same physical system as the emulation task yields the largest improvements, while pretraining on other systems provides moderate gains. In-domain pretraining reduces VRMSE by 64% after 10,500 training steps compared to training from scratch. To our knowledge, this is the first systematic investigation of tokeniser pretraining for physics foundation models. We further introduce flexible spatiotemporal compression operations that extend causal convolutions to support runtime-adjustable compression ratios, enabling efficient adaptation to diverse downstream tasks. Our findings provide practical guidance for training efficient physics emulators and highlight the importance of strategic pretraining data selection.

</details>

---

### 41. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种名为LatentChem的新框架，旨在改进化学大语言模型的推理机制，使其从显式文本链式思维转向隐式潜在空间计算。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）主要依赖显式的、离散的自然语言思维链（CoT）进行复杂推理的局限性。作者认为，化学推理本质上是连续和结构化的，将其强制编码为离散的语言标记会导致表示上的不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续的潜在空间中直接执行多步推理，而仅将语言用于最终输出。实验表明，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变带来了计算优势，在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于强大的CoT基线取得了59.88%的非平局胜率，同时推理速度平均提升了10.84倍。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 42. [Semantics-Aware Caching for Concept Learning](https://arxiv.org/abs/2603.06506)

**基本信息**

- 🔗 arXiv: [`2603.06506`](https://arxiv.org/abs/2603.06506)
- 👥 作者: Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06506.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于概念学习的语义感知缓存技术，这是一种可用于化学信息学等领域知识发现和推理任务的通用工具或方法，旨在提高基于知识库的机器学习系统的效率。

**📖 中文摘要**

本文提出了一种语义感知缓存方法，用于加速概念学习。概念学习是一种在描述逻辑知识库上运行的监督机器学习形式。最先进的概念学习者通常需要在可数无限的概念空间中进行迭代搜索，每次迭代都需要检索候选概念的实例。复杂的学习问题可能需要数千次实例检索调用，导致运行时挑战。本文提出的缓存本质上是一个子包含感知映射，通过精确的集合操作将概念与实例集链接起来。在5个数据集、4个符号推理器、1个神经符号推理器和5种流行分页策略上的实验表明，该缓存可以将概念检索和概念学习的运行时减少一个数量级，并且对符号和神经符号推理器都有效。这项工作通过优化底层数据访问，为构建更高效的（化学）信息学知识发现工具提供了技术支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

</details>

---

### 43. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于机器学习原子间势（MLIPs）的新型架构，这是化学信息学和计算化学中用于分子模拟和性质预测的核心“化学大模型”之一。

**📖 中文摘要**

本文系统地开发了用于机器学习原子间势（MLIPs）的混合专家（MoE）和混合线性专家（MoLE）架构，并分析了路由策略和专家设计的影响。MLIPs能够实现精确的大规模原子模拟。作者展示了稀疏激活与共享专家相结合能带来显著的性能提升，并且当存在共享专家时，非线性MoE公式优于MoLE，强调了非线性专家专门化的重要性。此外，基于元素的（element-wise）路由策略 consistently优于基于配置（configuration-level）的路由。由此产生的基于元素的MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、具有化学可解释性的专家专门化，表明该模型有效地捕捉了元素特定的化学特征，以实现精确的原子间建模。这项工作直接提升了用于分子和材料模拟的机器学习模型的表达能力与效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 44. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准3：论文的第二部分包含了对Prometheus框架的重要应用和讨论，该框架是一个用于无监督发现相变的通用机器学习框架。虽然本文主要物理背景是束-等离子体，但该框架及其验证方法（通过分析结构因子等谱数据）与“质谱结构推理”中可能涉及的模式发现和相变分析在方法论上高度相关，提供了重要的相关讨论和工具思路。

**📖 中文摘要**

本文为中等能量（10-100 MeV）强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。第一部分从Vlasov-Poisson系统出发，推导了Lindhard介电函数和随机相位近似极化张量，证明了在临界束密度n_c以上存在无阻尼的朗缪尔波模式，并获得了显式的束-等离子体色散关系。等离子体频率由f求和规则固定，与分布形状无关。空间电荷效应驱动了以sqrt(n-n_c)起始的反常束展宽和在q=2k_F处的Friedel振荡。束-等离子体转变通过重整化群分析属于3D Ising普适类。第二部分使用在粒子束模拟的静态结构因子数据S(q)上训练的beta-VAE框架Prometheus验证了这些预测。Prometheus成功检测到高斯分布和均匀分布中集体等离子体振荡的开始，确认了其在简并费米气体中的缺失，并解析了q=2k_F处的Kohn异常。这项工作展示了无监督机器学习（Prometheus框架）在发现和验证复杂物理系统（如束-等离子体）相变和集体模式方面的能力，其方法论对分析质谱等复杂光谱数据中的模式具有潜在借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

## 📊 数据统计
- 累计运行天数：30
- 累计论文数量：2136

## 📝 历史记录

> 暂无历史数据

