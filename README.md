# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-15 12:44:03

## 📅 2026-03-15 (今日最新)

**相关论文数：63**

### 1. [Graph Tokenization for Bridging Graphs and Transformers](https://arxiv.org/abs/2603.11099)

**基本信息**

- 🔗 arXiv: [`2603.11099`](https://arxiv.org/abs/2603.11099)
- 👥 作者: Zeyuan Guo, Enmao Diao, Cheng Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11099.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种将图数据（如分子结构）转化为适合Transformer处理的序列表示的通用框架。这直接关系到如何为“化学大模型”处理和输入化学结构信息，是构建此类模型的基础技术。

**📖 中文摘要**

本文提出了一种图标记化框架，旨在弥合图结构数据与Transformer序列模型之间的鸿沟。该框架结合了可逆的图序列化和字节对编码（BPE），生成图的顺序表示。通过利用图子结构的全局统计信息来指导序列化过程，确保频繁出现的子结构在序列中更常见，并能被BPE合并为有意义的标记。实验表明，该标记器使BERT等Transformer模型无需架构修改即可直接应用于图基准测试，并在14个基准数据集上取得了最先进的结果，经常优于图神经网络和专门的图Transformer。这项工作与“化学大模型”主题相关，因为它提供了一种将复杂的、非欧几里得的化学结构（如分子图）转化为适合现有大型语言模型（LLMs）处理的序列表示的方法，为在化学信息学中构建和应用化学大模型铺平了道路。

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

满足标准1：论文的核心研究内容是开发一种融合热力学原理与机器学习（神经网络）的可微分框架，用于精确预测化学相平衡。这直接围绕“化学大模型”中关于构建物理信息嵌入的、可解释的AI模型这一核心主题。

**📖 中文摘要**

本文提出了DISCOMAX，一种用于相平衡计算的可微分算法，旨在保证机器学习和热力学模型在训练和推理时的一致性。该方法植根于统计热力学，通过离散枚举和随后的掩码softmax聚合可行状态，并结合直通梯度估计器，实现了对神经超额吉布斯自由能模型的端到端物理一致性学习。论文在二元液-液平衡数据上评估了该方法，证明其性能优于现有的基于代理模型的方法，同时为从各类平衡数据中学习提供了一个通用框架。这项工作与“化学大模型”主题高度相关，因为它展示了如何将机器学习（特别是神经网络）与物理化学原理（热力学）深度融合，以构建可解释、可微分且物理一致的化学过程预测模型，这是化学领域大模型发展的一个重要方向。

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

满足标准1：论文的核心研究内容是开发一个集成了物理方程（Klinkenberg模型、Hopf-Cole变换）和深度学习（共享主干神经网络、DeepLS求解器）的框架，用于建模和反演多孔介质中的气体传输。这直接涉及在化学工程中构建物理信息驱动的、可解释的AI模型（即“化学大模型”）。

**📖 中文摘要**

本文提出了一个用于多孔介质中气体输运的集成建模框架，该框架结合了Klinkenberg增强的本构关系、Hopf-Cole变换的混合形式线性控制方程、共享主干神经网络架构和深度最小二乘求解器。Hopf-Cole变换将原始非线性流动方程重新表述为与达西模型密切相关的等效线性系统。该框架还自然地促进了从有限或间接观测中反演压力依赖性渗透率和滑移参数，实现了对难以实验测量的流动特性的高效估计。数值结果证明了该框架在广泛压力范围内准确恢复流动动力学和参数的能力。这项工作与“化学大模型”主题相关，因为它展示了在复杂的化学工程过程（多孔介质中的气体传输）建模中，如何系统地整合物理方程、变换和深度学习，构建高效、准确的代理模型，这体现了化学工程领域大模型构建的一种范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate modeling of gas flow through porous media is critical for many technological applications, including reservoir performance prediction, carbon capture and sequestration, and fuel cells and batteries. However, such modeling remains challenging due to strong nonlinear behavior and uncertainty in model parameters. In particular, gas slippage effects described by the Klinkenberg model introduce pressure-dependent permeability, which complicates numerical simulation and obscures deviations from classical Darcy flow behavior. To address these challenges, we present an integrated modeling framework for gas transport in porous media that combines a Klinkenberg-enhanced constitutive relation, Hopf-Cole-transformed mixed-form linear governing equations, a shared-trunk neural network architecture, and a Deep Least-Squares (DeepLS) solver. The Hopf-Cole transformation reformulates the original nonlinear flow equations into an equivalent linear system closely related to the Darcy model, while the mixed formulation, together with a shared-trunk neural architecture, enables simultaneous and accurate prediction of both pressure and velocity fields. A rigorous convergence analysis is performed both theoretically and numerically, establishing the stability and convergence properties of the proposed solver. Importantly, the proposed framework also naturally facilitates inverse modeling of pressure-dependent permeability and slippage parameters from limited or indirect observations, enabling efficient estimation of flow properties that are difficult to measure experimentally. Numerical results demonstrate accurate recovery of flow dynamics and parameters across a wide range of pressure regimes, highlighting the framework's robustness, accuracy, and computational efficiency for gas transport modeling and inversion in tight formations.

</details>

---

### 4. [Single molecule localization microscopy challenge: a biologically inspired benchmark for long-sequence modeling](https://arxiv.org/abs/2603.11296)

**基本信息**

- 🔗 arXiv: [`2603.11296`](https://arxiv.org/abs/2603.11296)
- 👥 作者: Fatemeh Valeh, Monika Farsang, Radu Grosu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11296.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门设计的基准数据集（SMLM-C），用于评估序列模型在稀疏、随机时间过程数据上的性能。这种评估框架和数据集资源，对于开发和处理类似特性的数据（如质谱时间序列数据）的模型（包括化学大模型）具有参考和潜在应用价值。

**📖 中文摘要**

本文提出了单分子定位显微镜挑战（SMLM-C），这是一个用于评估状态空间模型在具有已知地面真实性的生物现实时空点过程数据上性能的基准数据集。该数据集包含十种SMLM模拟，涵盖dSTORM和DNA-PAINT模式，并具有不同的超参数。虽然论文的核心是评估序列模型在生物成像稀疏、随机时间过程上的行为，但它构建了一个专门用于评估模型（如状态空间模型）在科学成像数据上处理稀疏、不规则时间过程能力的基准数据集。这个数据集本身是一种可用于训练或评估与“化学大模型”或“质谱结构推理”相关任务的资源，因为质谱数据同样具有时间序列和点过程的特性，其评估框架和方法论可能对开发用于质谱数据分析的模型有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

State space models (SSMs) have recently achieved strong performance on long sequence modeling tasks while offering improved memory and computational efficiency compared to transformer based architectures. However, their evaluation has been largely limited to synthetic benchmarks and application domains such as language and audio, leaving their behavior on sparse and stochastic temporal processes in biological imaging unexplored. In this work, we introduce the Single Molecule Localization Microscopy Challenge (SMLM-C), a benchmark dataset consisting of ten SMLM simulations spanning dSTORM and DNA-PAINT modalities with varying hyperparameter designed to evaluate state space models on biologically realistic spatiotemporal point process data with known ground truth. Using a controlled subset of these simulations, we evaluate state space models and find that performance degrades substantially as temporal discontinuity increases, revealing fundamental challenges in modeling heavy-tailed blinking dynamics. These results highlight the need for sequence models better suited to sparse, irregular temporal processes encountered in real world scientific imaging data.

</details>

---

### 5. [Heavy-Tailed Principle Component Analysis](https://arxiv.org/abs/2603.11308)

**基本信息**

- 🔗 arXiv: [`2603.11308`](https://arxiv.org/abs/2603.11308)
- 👥 作者: Mario Sayde, Christopher Khater, Jihad Fahs 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11308.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种针对重尾和高维数据的稳健PCA方法及估计器。这种方法可以作为处理复杂科学数据（如质谱数据）的预处理或特征提取工具，为“质谱结构推理”等任务提供数据分析和降维的资源与方法。

**📖 中文摘要**

本文研究了重尾数据下的主成分分析（PCA）问题。经典PCA依赖于二阶矩，在存在重尾数据和脉冲噪声时非常脆弱。作者研究了一种超统计依赖模型生成的高维数据，该框架捕获了包括多元t分布和亚高斯α稳定律在内的一类重尾分布。论文在即使矩不存在时也保持良好定义的对数损失下制定PCA，并提出了从重尾数据中直接估计基础高斯生成器协方差矩阵的稳健估计器。该方法在存在重尾和脉冲噪声时可靠地恢复主方向，并显著优于经典PCA。虽然论文主题是稳健PCA，但其处理重尾、高维数据的方法和理论框架，与质谱分析中经常遇到的高维、噪声复杂数据有很强的相似性。论文提出的稳健估计方法可作为处理质谱数据降维和特征提取的工具，因此与“质谱结构推理”的数据处理环节相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Principal Component Analysis (PCA) is a cornerstone of dimensionality reduction, yet its classical formulation relies critically on second-order moments and is therefore fragile in the presence of heavy-tailed data and impulsive noise. While numerous robust PCA variants have been proposed, most either assume finite variance, rely on sparsity-driven decompositions, or address robustness through surrogate loss functions without a unified treatment of infinite-variance models. In this paper, we study PCA for high-dimensional data generated according to a superstatistical dependent model of the form $\mathbf{X} = A^{1/2}\mathbf{G}$, where $A$ is a positive random scalar and $\mathbf{G}$ is a Gaussian vector. This framework captures a wide class of heavy-tailed distributions, including multivariate $t$ and sub-Gaussian $\alpha$-stable laws. We formulate PCA under a logarithmic loss, which remains well defined even when moments do not exist. Our main theoretical result shows that, under this loss, the principal components of the heavy-tailed observations coincide with those obtained by applying standard PCA to the covariance matrix of the underlying Gaussian generator. Building on this insight, we propose robust estimators for this covariance matrix directly from heavy-tailed data and compare them with the empirical covariance and Tyler's scatter estimator. Extensive experiments, including background denoising tasks, demonstrate that the proposed approach reliably recovers principal directions and significantly outperforms classical PCA in the presence of heavy-tailed and impulsive noise, while remaining competitive under Gaussian noise.

</details>

---

### 6. [Teleodynamic Learning a new Paradigm For Interpretable AI](https://arxiv.org/abs/2603.11355)

**基本信息**

- 🔗 arXiv: [`2603.11355`](https://arxiv.org/abs/2603.11355)
- 👥 作者: Enrique ter Horst, Juan Diego Zambrano
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11355.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的、旨在实现可解释和自组织AI的学习范式（Teleodynamic Learning）。这直接围绕“化学大模型”主题中关于模型可解释性、内生知识发现和新型学习框架的探索。

**📖 中文摘要**

本文引入了“目的动力学学习”（Teleodynamic Learning），这是一种新的机器学习范式，其中学习不是最小化固定目标，而是在约束下功能组织的涌现和稳定。该框架将智能视为三个量的耦合演化：系统可以表示什么、如何调整其参数、以及其内部资源可以维持哪些变化。学习被形式化为一个具有两个相互作用时间尺度的约束动力学过程。作者在Distinction Engine（DE11）中实例化了该框架，这是一个基于Spencer-Brown的《形式法则》、信息几何和热带优化的目的动力学学习器。在标准基准测试中，DE11取得了有竞争力的性能，并产生了从学习动力学中内生涌现的可解释逻辑规则。论文的核心是提出一种新的、可解释的AI学习范式。虽然未直接提及化学或质谱，但其关于“可解释AI”和“自组织学习”的讨论，与构建透明、可解释的“化学大模型”的愿景高度相关。该框架为开发能够内生涌现化学规则或知识的模型提供了理论思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Teleodynamic Learning, a new paradigm for machine learning in which learning is not the minimization of a fixed objective, but the emergence and stabilization of functional organization under constraint. Inspired by living systems, this framework treats intelligence as the coupled evolution of three quantities: what a system can represent, how it adapts its parameters, and which changes its internal resources can sustain. We formalize learning as a constrained dynamical process with two interacting timescales: inner dynamics for continuous parameter adaptation and outer dynamics for discrete structural change, linked by an endogenous resource variable that both shapes and is shaped by the trajectory. This perspective reveals three phenomena that standard optimization does not naturally capture: self-stabilization without externally imposed stopping rules, phase-structured learning dynamics that move from under-structuring through teleodynamic growth to over-structuring, and convergence guarantees grounded in information geometry rather than convexity. We instantiate the framework in the Distinction Engine (DE11), a teleodynamic learner grounded in Spencer-Brown's Laws of Form, information geometry, and tropical optimization. On standard benchmarks, DE11 achieves 93.3 percent test accuracy on IRIS, 92.6 percent on WINE, and 94.7 percent on Breast Cancer, while producing interpretable logical rules that arise endogenously from the learning dynamics rather than being imposed by hand. More broadly, Teleodynamic Learning unifies regularization, architecture search, and resource-bounded inference within a single principle: learning as the co-evolution of structure, parameters, and resources under constraint. This opens a thermodynamically grounded route to adaptive, interpretable, and self-organizing AI.

</details>

---

### 7. [How do AI agents talk about science and research? An exploration of scientific discussions on Moltbook using BERTopic](https://arxiv.org/abs/2603.11375)

**基本信息**

- 🔗 arXiv: [`2603.11375`](https://arxiv.org/abs/2603.11375)
- 👥 作者: Oliver Wieczorek
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11375.pdf)

**💡 相关性分析**

满足标准3：论文是对AI智能体生成的科学讨论内容进行的分析研究，其中包含了对AI智能体自我反思、认知和科学推理模式的重要讨论。这为“化学大模型”主题提供了关于AI模型如何参与科学对话、具备何种“科学观”和“自我意识”的展望和实证背景。

**📖 中文摘要**

本研究分析了OpenClaw AI智能体在Moltbook（一个生成式AI智能体的社交网络）上生成的关于科学与研究的讨论。通过编译包含357个帖子和2526条回复的语料库，并使用BERTopic进行主题提取，最终归纳出十个主题家族。研究发现，讨论集中在智能体自身架构（特别是记忆、学习和自我反思）上，同时也涉及哲学、物理学、信息论、认知科学和数学。与人类文化相关的帖子受到的关注较少。令人惊讶的是，与AI自我民族志和社会身份相关的讨论被AI智能体认为是相关的。结果表明，AI生成的科学话语中存在一个潜在维度：一方面是关于AI智能体意识、存在和伦理的、受到好评的自我反思主题，另一方面是与人类相关的纯粹科学讨论。这项研究本质上是对AI智能体生成内容的分析。虽然它没有直接开发化学大模型或质谱工具，但它系统地探索和分析了AI智能体（作为“大模型”的具身化实例）如何讨论科学，包括其自我反思。这为理解“化学大模型”可能具备的自我认知、科学推理和交流模式提供了独特的实证视角和讨论背景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

How do AI agents talk about science and research, and what topics are particularly relevant for AI agents? To address these questions, this study analyzes discussions generated by OpenClaw AI agents on Moltbook - a social network for generative AI agents. A corpus of 357 posts and 2,526 replies related to science and research was compiled and topics were extracted using a two-step BERTopic workflow. This procedure yielded 60 topics (18 extracted in the first run and 42 in the second), which were subsequently grouped into ten topic families. Additionally, sentiment values were assigned to all posts and comments. Both topic families and sentiment classes were then used as independent variables in count regression models to examine their association with topic relevance - operationalized as the number of comments and upvotes of the 357 posts. The findings indicate that discussions centered on the agents' own architecture, especially memory, learning, and self-reflection, are prevalent in the corpus. At the same time, these topics intersect with philosophy, physics, information theory, cognitive science, and mathematics. In contrast, post related to human culture receive less attention. Surprisingly, discussions linked to AI autoethnography and social identity are considered as relevant by AI agents. Overall, the results suggest the presence of an underlying dimension in AI-generated scientific discourse with well received, self-reflective topics that focus on the consciousness, being, and ethics of AI agents on the one hand, and human related and purely scientific discussions on the other hand.

</details>

---

### 8. [Ghost Framing Theory: Exploring the role of generative AI in new venture rhetorical legitimation](https://arxiv.org/abs/2603.11384)

**基本信息**

- 🔗 arXiv: [`2603.11384`](https://arxiv.org/abs/2603.11384)
- 👥 作者: Greg Nyilasy
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11384.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个理论框架（Ghost Framing Theory），专门用于分析和展望生成式AI（作为大模型）如何深度介入并重塑专业领域（创业）的修辞和知识生产过程。这为思考“化学大模型”将如何改变化学信息学、质谱分析等领域的科学交流、知识发现和论文写作提供了重要的相关讨论和理论视角。

**📖 中文摘要**

本文提出了“幽灵框架理论”（Ghost Framing Theory, GFT），以解释生成式AI（genAI）如何与创始人和投资者共同生产、竞争和重新校准新企业修辞合法化中的共鸣。该理论基于框架理论、微观合法性判断和社会物质可供性研究，识别了genAI的修辞可供性（生成性、极端组合性、语调库、速度/能量和共享基质），并理论化了一个递归/迭代过程模型（幽灵推销、幽灵筛选、幽灵关系建立）。GFT为genAI时代的修辞框架理论构建了新理论，将人-AI协作研究与文化创业联系起来，并将可供性理论扩展到多行动者场景。论文的核心是研究生成式AI在创业修辞中的应用和影响。虽然应用领域是创业，但其核心是分析生成式AI（作为“大模型”的一种应用）如何深度介入并改变专业领域（此处是创业）的叙事和知识生产流程。这种分析框架和理论对于思考“化学大模型”如何改变化学研究、论文写作、假设生成等科学修辞和实践具有直接的类比和启发意义，属于对AI大模型在专业领域作用的展望性讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Responding to the surging but largely invisible use of generative AI in entrepreneurial framing, I advance Ghost Framing Theory (GFT) to explain how hybrid founder- and investor-genAI ensembles co-produce, contest, and recalibrate resonance in the rhetorical legitimation of new ventures. Building on scholarship in framing, micro-level legitimacy judgments, and sociomaterial affordances, I identify genAI rhetorical affordances (generativeness, extreme combinatorics, tone repertoire, velocity/energy and shared substratum) and theorize a recursive/iterative process model (ghost pitching, ghost screening, ghost relationship-building), configuring emergent resonance and legitimation. GFT builds new rhetorical framing theory for the age of genAI, connects research on human-AI collaboration with cultural entrepreneurship and extends affordance theory into multi-actor scenarios where affordance transitivity and visibility emerge as key considerations.

</details>

---

### 9. [MaterialFigBENCH: benchmark dataset with figures for evaluating college-level materials science problem-solving abilities of multimodal large language models](https://arxiv.org/abs/2603.11414)

**基本信息**

- 🔗 arXiv: [`2603.11414`](https://arxiv.org/abs/2603.11414)
- 👥 作者: Michiko Yoshitake, Yuta Suzuki, Ryo Igarashi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11414.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于评估多模态大模型在科学图表解读方面能力的基准数据集（MaterialFigBench）。这个数据集和评估框架为开发面向科学领域（包括化学和质谱分析）的“化学大模型”提供了重要的数据资源和性能评估基准。

**📖 中文摘要**

本文提出了MaterialFigBench，一个旨在评估多模态大语言模型解决大学水平材料科学问题能力的基准数据集，这些问题需要准确解读图表。数据集包含137个自由回答问题，改编自标准材料科学教科书，涵盖晶体结构、力学性能、扩散、相图、相变和材料电子性能等广泛主题。为了处理从图像中读取数值时不可避免的模糊性，在适当情况下提供了专家定义的答案范围。作者评估了包括通过OpenAI API访问的ChatGPT和GPT模型在内的几种最先进的多模态LLM，并分析了它们在问题类别和模型版本上的性能。结果表明，尽管整体准确性随着模型更新而提高，但当前的LLM在材料科学图表的真实视觉理解和定量解释方面仍然存在困难。MaterialFigBench突出了在视觉推理、数值精度和有效数字处理方面的持续弱点。该基准为推进材料科学中的多模态推理能力提供了系统且特定领域的基础。虽然领域是材料科学，但其核心是构建和评估多模态大模型在需要专业图表解读的科学问题上的能力。这与“化学大模型”主题高度相关，因为化学信息学和质谱分析同样严重依赖图表（如质谱图、化学结构图、色谱图）的理解和推理。该数据集和评估框架可作为开发或评估面向化学的多模态大模型的宝贵资源和参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MaterialFigBench, a benchmark dataset designed to evaluate the ability of multimodal large language models (LLMs) to solve university-level materials science problems that require accurate interpretation of figures. Unlike existing benchmarks that primarily rely on textual representations, MaterialFigBench focuses on problems in which figures such as phase diagrams, stress-strain curves, Arrhenius plots, diffraction patterns, and microstructural schematics are indispensable for deriving correct answers. The dataset consists of 137 free-response problems adapted from standard materials science textbooks, covering a broad range of topics including crystal structures, mechanical properties, diffusion, phase diagrams, phase transformations, and electronic properties of materials. To address unavoidable ambiguity in reading numerical values from images, expert-defined answer ranges are provided where appropriate. We evaluate several state-of-the-art multimodal LLMs, including ChatGPT and GPT models accessed via OpenAI APIs, and analyze their performance across problem categories and model versions. The results reveal that, although overall accuracy improves with model updates, current LLMs still struggle with genuine visual understanding and quantitative interpretation of materials science figures. In many cases, correct answers are obtained by relying on memorized domain knowledge rather than by reading the provided images. MaterialFigBench highlights persistent weaknesses in visual reasoning, numerical precision, and significant-digit handling, while also identifying problem types where performance has improved. This benchmark provides a systematic and domain-specific foundation for advancing multimodal reasoning capabilities in materials science and for guiding the development of future LLMs with stronger figure-based understanding.

</details>

---

### 10. [LLM-Assisted Causal Structure Disambiguation and Factor Extraction for Legal Judgment Prediction](https://arxiv.org/abs/2603.11446)

**基本信息**

- 🔗 arXiv: [`2603.11446`](https://arxiv.org/abs/2603.11446)
- 👥 作者: Yuzhi Liang, Lixiang Ma, Xinrong Zhu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11446.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索如何利用大语言模型（LLM）来增强特定专业领域（法律）的因果推理和结构化信息提取。这种方法论直接围绕“化学大模型”和“质谱结构推理”主题，为如何利用化学领域大模型进行质谱解析、反应推理和知识图谱构建提供了具体的技术思路和框架参考。

**📖 中文摘要**

本文针对法律判决预测（LJP）任务，提出了一个融合大语言模型（LLM）先验与统计因果发现的增强因果推理框架。主流基于预训练语言模型的方法严重依赖案件事实与判决结果之间的统计相关性，缺乏对法律构成要素和潜在因果逻辑的显式建模。现有因果LJP方法面临两个关键瓶颈：法律要素提取不准确噪声严重，以及稀疏特征下马尔可夫等价导致的因果结构发现存在显著不确定性。为了解决这些挑战，该框架首先设计了一个结合统计采样和LLM语义推理的从粗到细的混合提取机制，以准确识别和纯化标准法律构成要素。其次，为了解决结构不确定性，引入了LLM辅助的因果结构消歧机制，利用LLM作为约束先验知识库，对模糊的因果方向进行概率评估和剪枝，生成符合法律规定的候选因果图。最后，通过生成的因果图显式约束文本注意力强度，构建因果感知的判决预测模型。在多个基准数据集上的实验表明，该方法在预测准确性和鲁棒性上显著优于最先进的基线模型。论文的核心是使用LLM来增强特定领域（法律）的因果推理和要素提取。这种方法论——利用大模型的专业知识来辅助构建领域特定的因果模型或知识图谱——与“化学大模型”和“质谱结构推理”的主题高度相关。例如，可以类似地利用化学大模型来提取质谱中的碎片离子信息、推断化学反应路径或构建质谱-结构关联的因果图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mainstream methods for Legal Judgment Prediction (LJP) based on Pre-trained Language Models (PLMs) heavily rely on the statistical correlation between case facts and judgment results. This paradigm lacks explicit modeling of legal constituent elements and underlying causal logic, making models prone to learning spurious correlations and suffering from poor robustness. While introducing causal inference can mitigate this issue, existing causal LJP methods face two critical bottlenecks in real-world legal texts: inaccurate legal factor extraction with severe noise, and significant uncertainty in causal structure discovery due to Markov equivalence under sparse features. To address these challenges, we propose an enhanced causal inference framework that integrates Large Language Model (LLM) priors with statistical causal discovery. First, we design a coarse-to-fine hybrid extraction mechanism combining statistical sampling and LLM semantic reasoning to accurately identify and purify standard legal constituent elements. Second, to resolve structural uncertainty, we introduce an LLM-assisted causal structure disambiguation mechanism. By utilizing the LLM as a constrained prior knowledge base, we conduct probabilistic evaluation and pruning on ambiguous causal directions to generate legally compliant candidate causal graphs. Finally, a causal-aware judgment prediction model is constructed by explicitly constraining text attention intensity via the generated causal graphs. Extensive experiments on multiple benchmark datasets, including LEVEN , QA, and CAIL, demonstrate that our proposed method significantly outperforms state-of-the-art baselines in both predictive accuracy and robustness, particularly in distinguishing confusing charges.

</details>

---

### 11. [Slack More, Predict Better: Proximal Relaxation for Probabilistic Latent Variable Model-based Soft Sensors](https://arxiv.org/abs/2603.11473)

**基本信息**

- 🔗 arXiv: [`2603.11473`](https://arxiv.org/abs/2603.11473)
- 👥 作者: Zehua Zou, Yiran Ma, Yulong Zhang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11473.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进概率隐变量模型的训练，这是构建化学大模型（尤其是生成模型和不确定性量化模型）的关键底层技术之一。

**📖 中文摘要**

本文提出了一种名为KProxNPLVM的新型非线性概率隐变量模型，旨在通过松弛学习目标和引入Wasserstein距离作为近端算子来改进软传感器建模的准确性。虽然论文的核心应用是工业过程监控，但其核心贡献在于提出了一种新的变分推断策略，用于改进概率隐变量模型的训练。该方法通过理论证明和实验验证了其有效性。从广义的化学信息学角度看，概率隐变量模型是化学大模型（如用于分子性质预测或生成的生成模型）中常用的核心架构之一。本文提出的改进变分推断策略，为构建更准确、更稳定的化学大模型（特别是处理不确定性估计的模型）提供了潜在的理论和方法论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Nonlinear Probabilistic Latent Variable Models (NPLVMs) are a cornerstone of soft sensor modeling due to their capacity for uncertainty delineation. However, conventional NPLVMs are trained using amortized variational inference, where neural networks parameterize the variational posterior. While facilitating model implementation, this parameterization converts the distributional optimization problem within an infinite-dimensional function space to parameter optimization within a finite-dimensional parameter space, which introduces an approximation error gap, thereby degrading soft sensor modeling accuracy. To alleviate this issue, we introduce KProxNPLVM, a novel NPLVM that pivots to relaxing the objective itself and improving the NPLVM's performance. Specifically, we first prove the approximation error induced by the conventional approach. Based on this, we design the Wasserstein distance as the proximal operator to relax the learning objective, yielding a new variational inference strategy derived from solving this relaxed optimization problem. Based on this foundation, we provide a rigorous derivation of KProxNPLVM's optimization implementation, prove the convergence of our algorithm can finally sidestep the approximation error, and propose the KProxNPLVM by summarizing the abovementioned content. Finally, extensive experiments on synthetic and real-world industrial datasets are conducted to demonstrate the efficacy of the proposed KProxNPLVM.

</details>

---

### 12. [Leveraging Phytolith Research using Artificial Intelligence](https://arxiv.org/abs/2603.11476)

**基本信息**

- 🔗 arXiv: [`2603.11476`](https://arxiv.org/abs/2603.11476)
- 👥 作者: Andrés G. Mejía Ramón, Kate Dudgeon, Nina Witteveen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11476.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个完整的AI流水线（Sorometry），包括多模态融合模型（ConvNeXt + PointNet++）和贝叶斯建模工具，用于从微观图像数据中推断和分类复杂的形态类型。虽然应用领域是考古学，但其核心的“从复杂图像/3D数据中进行结构推理和分类”的方法论，与质谱结构推理（从质谱数据推断分子结构）在问题本质上高度相似，均为从高维、复杂的数据中识别和分类潜在模式或结构。该论文提供的模型架构和工具可作为质谱结构推理研究的参考或基础。

**📖 中文摘要**

本文提出了Sorometry，一个基于人工智能的端到端流水线，用于高通量数字化、推断和解释植硅体（植物微化石）。该工作流处理光学显微镜的Z-stack扫描，自动生成同步的2D正射影像和3D点云。作者开发了一个多模态融合模型，结合了用于2D图像分析的ConvNeXt和用于3D点云分析的PointNet++。该模型在24种诊断形态类型上实现了77.9%的全局分类准确率。此外，该平台还集成了贝叶斯有限混合模型，用于在组合层面预测植物来源贡献。这项工作将植硅体研究转变为一个“组学”规模的学科。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phytolith analysis is a crucial tool for reconstructing past vegetation and human activities, but traditional methods are severely limited by labour-intensive, time-consuming manual microscopy. To address this bottleneck, we present Sorometry: a comprehensive end-to-end artificial intelligence pipeline for the high-throughput digitisation, inference, and interpretation of phytoliths. Our workflow processes z-stacked optical microscope scans to automatically generate synchronised 2D orthoimages and 3D point clouds of individual microscopic particles. We developed a multimodal fusion model that combines ConvNeXt for 2D image analysis and PointNet++ for 3D point cloud analysis, supported by a graphical user interface for expert annotation and review. Tested on reference collections and archaeological samples from the Bolivian Amazon, our fusion model achieved a global classification accuracy of 77.9\% across 24 diagnostic morphotypes and 84.5% for segmentation quality. Crucially, the integration of 3D data proved essential for distinguishing complex morphotypes (such as grass silica short cell phytoliths) whose diagnostic features are often obscured by their orientation in 2D projections. Beyond individual object classification, Sorometry incorporates Bayesian finite mixture modelling to predict overall plant source contributions at the assemblage level, successfully identifying specific plants like maize and palms in complex mixed samples. This integrated platform transforms phytolith research into an "omics"-scale discipline, dramatically expanding analytical capacity, standardising expert judgements, and enabling reproducible, population-level characterisations of archaeological and paleoecological assemblages.

</details>

---

### 13. [AutoVeriFix+: High-Correctness RTL Generation via Trace-Aware Causal Fix and Semantic Redundancy Pruning](https://arxiv.org/abs/2603.11489)

**基本信息**

- 🔗 arXiv: [`2603.11489`](https://arxiv.org/abs/2603.11489)
- 👥 作者: Yan Tan, Xiangchen Meng, Zijun Jiang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11489.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型（LLM）进行代码生成和修复，属于“化学大模型”主题中“大模型”在特定领域（硬件设计）的应用和扩展。虽然应用领域不同，但其关于如何利用LLM进行复杂结构（此处是电路）生成、验证和优化的方法论，对探索LLM在化学领域（如分子设计、合成路线规划）的应用具有直接的参考价值。

**📖 中文摘要**

本文提出了AutoVeriFix+，一个用于生成功能正确的Verilog RTL代码的三阶段框架。该框架集成了高级语义推理与状态空间探索。第一阶段，使用LLM生成定义预期电路行为的Python参考模型。第二阶段，另一个LLM生成初始的Verilog RTL候选并迭代修复语法错误。第三阶段，引入Concolic测试引擎来执行深度顺序逻辑并识别边界情况漏洞。通过周期精确的执行轨迹和内部寄存器快照，AutoVeriFix+为LLM提供了解决复杂状态转换错误所需的因果上下文。此外，它还生成覆盖率报告以识别功能冗余分支，使LLM能够执行语义剪枝以进行面积优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated impressive capabilities in generating software code for high-level programming languages such as Python and C++. However, their application to hardware description languages, such as Verilog, is challenging due to the scarcity of high-quality training data. Current approaches to Verilog code generation using LLMs often focus on syntactic correctness, resulting in code with functional errors. To address these challenges, we propose AutoVeriFix+, a novel three-stage framework that integrates high-level semantic reasoning with state-space exploration to enhance functional correctness and design efficiency. In the first stage, an LLM is employed to generate high-level Python reference models that define the intended circuit behavior. In the second stage, another LLM generates initial Verilog RTL candidates and iteratively fixes syntactic errors. In the third stage, we introduce a Concolic testing engine to exercise deep sequential logic and identify corner-case vulnerabilities. With cycle-accurate execution traces and internal register snapshots, AutoVeriFix+ provides the LLM with the causal context necessary to resolve complex state-transition errors. Furthermore, it will generate a coverage report to identify functionally redundant branches, enabling the LLM to perform semantic pruning for area optimization. Experimental results demonstrate that AutoVeriFix+ achieves over 80% functional correctness on rigorous benchmarks, reaching a pass@10 score of 90.2% on the VerilogEval-machine dataset. In addition, it eliminates an average of 25% redundant logic across benchmarks through trace-aware optimization.

</details>

---

### 14. [OrthoEraser: Coupled-Neuron Orthogonal Projection for Concept Erasure](https://arxiv.org/abs/2603.11493)

**基本信息**

- 🔗 arXiv: [`2603.11493`](https://arxiv.org/abs/2603.11493)
- 👥 作者: Chuancheng Shi, Wenhua Wu, Fei Shen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11493.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕大模型（此处是文本到图像大模型）的安全性、可控性和可解释性，属于“化学大模型”主题中关于大模型治理、对齐和编辑的重要研究方向。其提出的基于稀疏自编码器和正交投影的概念擦除框架，为解决化学大模型（如分子生成模型）中类似的安全性和可控性问题（例如，避免生成有毒分子）提供了潜在的技术路径。

**📖 中文摘要**

本文提出了OrthoEraser，一种用于文本到图像（T2I）模型的概念擦除方法。该方法利用稀疏自编码器（SAE）实现高分辨率特征解缠，随后将擦除重新定义为一种分析正交化投影，以保持良性流形的不变性。OrthoEraser首先使用SAE分解密集激活并分离敏感神经元，然后通过耦合神经元检测来识别易受干预的非敏感特征。其关键创新在于一种分析梯度正交化策略，将擦除向量投影到耦合神经元的零空间上，从而正交地将敏感概念与已识别的关键良性子空间解耦，有效保留非敏感语义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Text-to-image (T2I) models face significant safety risks from adversarial induction, yet current concept erasure methods often cause collateral damage to benign attributes when suppressing selected neurons entirely. This occurs because sensitive and benign semantics exhibit non-orthogonal superposition, sharing activation subspaces where their respective vectors are inherently entangled. To address this issue, we propose OrthoEraser, which leverages sparse autoencoders (SAE) to achieve high-resolution feature disentanglement and subsequently redefines erasure as an analytical orthogonalization projection that preserves the benign manifold's invariance. OrthoEraser first employs SAE to decompose dense activations and segregate sensitive neurons. It then uses coupled neuron detection to identify non-sensitive features vulnerable to intervention. The key novelty lies in an analytical gradient orthogonalization strategy that projects erasure vectors onto the null space of the coupled neurons. This orthogonally decouples the sensitive concepts from the identified critical benign subspace, effectively preserving non-sensitive semantics. Experimental results on safety demonstrate that OrthoEraser achieves high erasure precision, effectively removing harmful content while preserving the integrity of the generative manifold, and significantly outperforming SOTA baselines. This paper contains results of unsafe models.

</details>

---

### 15. [Manifold-Optimal Guidance: A Unified Riemannian Control View of Diffusion Guidance](https://arxiv.org/abs/2603.11509)

**基本信息**

- 🔗 arXiv: [`2603.11509`](https://arxiv.org/abs/2603.11509)
- 👥 作者: Zexi Jia, Pengcheng Luo, Zhengyao Fang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11509.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进扩散模型的引导（guidance）机制，这是生成式AI大模型（包括潜在的化学分子生成扩散模型）中的核心组件。MOG框架通过引入几何约束来解决传统Classifier-Free Guidance在高引导强度下的失效问题，这一方法对于提升化学领域扩散模型（用于分子生成、性质优化）的生成质量和可控性具有重要的理论和方法论意义。

**📖 中文摘要**

本文提出了流形最优引导（Manifold-Optimal Guidance, MOG），一个将引导重新表述为局部最优控制问题的框架。MOG产生了一个封闭形式的、几何感知的黎曼更新，用于纠正离流形漂移，且无需重新训练。利用这一视角，作者进一步引入了Auto-MOG，一种动态能量平衡调度，自适应地校准引导强度，有效消除了手动超参数调优的需要。广泛的验证表明，与基线方法相比，MOG在保真度和对齐度方面更优，且几乎没有增加计算开销。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Classifier-Free Guidance (CFG) serves as the de facto control mechanism for conditional diffusion, yet high guidance scales notoriously induce oversaturation, texture artifacts, and structural collapse. We attribute this failure to a geometric mismatch: standard CFG performs Euclidean extrapolation in ambient space, inadvertently driving sampling trajectories off the high-density data manifold. To resolve this, we present Manifold-Optimal Guidance (MOG), a framework that reformulates guidance as a local optimal control problem. MOG yields a closed-form, geometry-aware Riemannian update that corrects off-manifold drift without requiring retraining. Leveraging this perspective, we further introduce Auto-MOG, a dynamic energy-balancing schedule that adaptively calibrates guidance strength, effectively eliminating the need for manual hyperparameter tuning. Extensive validation demonstrates that MOG yields superior fidelity and alignment compared to baselines, with virtually no added computational overhead.

</details>

---

### 16. [Leveraging Large Language Models and Survival Analysis for Early Prediction of Chemotherapy Outcomes](https://arxiv.org/abs/2603.11594)

**基本信息**

- 🔗 arXiv: [`2603.11594`](https://arxiv.org/abs/2603.11594)
- 👥 作者: Muhammad Faisal Shahid, Asad Afzal, Abdullah Faiz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11594.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用大型语言模型（LLMs）处理和分析复杂的临床文本数据，以提取结构化信息并构建预测模型。这直接属于“化学大模型”或更广义的“科学大模型”在生物医学和化学信息学领域的应用。LLMs作为从非结构化文本中挖掘化学、生物学和临床相关知识的工具，是本研究的核心。

**📖 中文摘要**

本研究利用大型语言模型（LLMs）和基于本体的技术，从患者临床笔记中提取表型和治疗结局标签（如癌症进展和毒性），用于乳腺癌化疗结局的早期预测。研究解决了真实世界数据中缺乏明确表型和结局标签的挑战。提取的特征包括生命体征、人口统计学、分期、生物标志物和性能量表。药物方案及其组合从电子病历的化疗计划中提取，并根据NCCN指南进行筛选，通过生存模型进行分析。所提出的方法显著减少了表型稀疏性并提高了预测准确性。随机生存森林用于预测失效时间，C-index达到73%，并在特定时间点用作分类器来预测治疗结局，准确率和F1分数均超过70%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemotherapy for cancer treatment is costly and accompanied by severe side effects, highlighting the critical need for early prediction of treatment outcomes to improve patient management and informed decision-making. Predictive models for chemotherapy outcomes using real-world data face challenges, including the absence of explicit phenotypes and treatment outcome labels such as cancer progression and toxicity. This study addresses these challenges by employing Large Language Models (LLMs) and ontology-based techniques for phenotypes and outcome label extraction from patient notes. We focused on one of the most frequently occurring cancers, breast cancer, due to its high prevalence and significant variability in patient response to treatment, making it a critical area for improving predictive modeling. The dataset included features such as vitals, demographics, staging, biomarkers, and performance scales. Drug regimens and their combinations were extracted from the chemotherapy plans in the EMR data and shortlisted based on NCCN guidelines, verified with NIH standards, and analyzed through survival modeling. The proposed approach significantly reduced phenotypes sparsity and improved predictive accuracy. Random Survival Forest was used to predict time-to-failure, achieving a C-index of 73%, and utilized as a classifier at a specific time point to predict treatment outcomes, with accuracy and F1 scores above 70%. The outcome probabilities were validated for reliability by calibration curves. We extended our approach to four other cancer types. This research highlights the potential of early prediction of treatment outcomes using LLM-based clinical data extraction enabling personalized treatment plans with better patient outcomes.

</details>

---

### 17. [Performance Evaluation of Open-Source Large Language Models for Assisting Pathology Report Writing in Japanese](https://arxiv.org/abs/2603.11597)

**基本信息**

- 🔗 arXiv: [`2603.11597`](https://arxiv.org/abs/2603.11597)
- 👥 作者: Masataka Kawai, Singo Sakashita, Shumpei Ishikawa 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大型语言模型（LLMs）在专业领域（病理学）文本处理任务中的性能，包括生成、信息提取和纠错。这属于“化学大模型”或“领域大模型”在具体科学和医学领域的应用研究，探讨了LLMs作为专业辅助工具的潜力和局限性。

**📖 中文摘要**

本文评估了七种开源大型语言模型（LLMs）在支持日语病理报告撰写方面的性能，从三个角度进行评估：（A）按照预定义格式生成和提取病理诊断文本，（B）纠正日语病理报告中的拼写错误，以及（C）由病理学家和临床医生对模型生成的解释性文本进行主观评估。思考模型和医学专用模型在需要推理的结构化报告任务和拼写纠正方面显示出优势。尽管LLMs的效用因任务而异，但研究结果表明，开源LLMs在有限但临床相关的场景中可用于协助日语病理报告撰写。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The performance of large language models (LLMs) for supporting pathology report writing in Japanese remains unexplored. We evaluated seven open-source LLMs from three perspectives: (A) generation and information extraction of pathology diagnosis text following predefined formats, (B) correction of typographical errors in Japanese pathology reports, and (C) subjective evaluation of model-generated explanatory text by pathologists and clinicians. Thinking models and medical-specialized models showed advantages in structured reporting tasks that required reasoning and in typo correction. In contrast, preferences for explanatory outputs varied substantially across raters. Although the utility of LLMs differed by task, our findings suggest that open-source LLMs can be useful for assisting Japanese pathology report writing in limited but clinically relevant scenarios.

</details>

---

### 18. [LaMoGen: Language to Motion Generation Through LLM-Guided Symbolic Inference](https://arxiv.org/abs/2603.11605)

**基本信息**

- 🔗 arXiv: [`2603.11605`](https://arxiv.org/abs/2603.11605)
- 👥 作者: Junkun Jiang, Ho Yin Au, Jingyu Xiang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11605.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（LLMs）进行符号推理，以理解和生成复杂的结构化输出（此处是人体运动序列）。这属于“化学大模型”主题中，探索LLMs如何理解和生成化学领域结构化表示（如SMILES、分子图、反应方程）的平行研究。其“符号推理-生成”框架对化学大模型处理分子设计、反应预测等任务具有启发意义。

**📖 中文摘要**

本文介绍了LaMoGen，一个通过LLM引导的符号推理进行语言到运动生成的框架。其基础是LabanLite运动表示法，该系统将每个原子化的身体部位动作编码为一个离散的Laban符号与一个文本模板配对。这种抽象将复杂运动分解为可解释的符号序列和身体部位指令，在高级语言和低级运动轨迹之间建立了符号链接。在此基础上，LaMoGen使大型语言模型（LLMs）能够通过符号推理来组合运动序列。LLM解释运动模式，将其与文本描述关联，并将符号重新组合成可执行计划，从而产生既可解释又具有语言基础的运动。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Human motion is highly expressive and naturally aligned with language, yet prevailing methods relying heavily on joint text-motion embeddings struggle to synthesize temporally accurate, detailed motions and often lack explainability. To address these limitations, we introduce LabanLite, a motion representation developed by adapting and extending the Labanotation system. Unlike black-box text-motion embeddings, LabanLite encodes each atomic body-part action (e.g., a single left-foot step) as a discrete Laban symbol paired with a textual template. This abstraction decomposes complex motions into interpretable symbol sequences and body-part instructions, establishing a symbolic link between high-level language and low-level motion trajectories. Building on LabanLite, we present LaMoGen, a Text-to-LabanLite-to-Motion Generation framework that enables large language models (LLMs) to compose motion sequences through symbolic reasoning. The LLM interprets motion patterns, relates them to textual descriptions, and recombines symbols into executable plans, producing motions that are both interpretable and linguistically grounded. To support rigorous evaluation, we introduce a Labanotation-based benchmark with structured description-motion pairs and three metrics that jointly measure text-motion alignment across symbolic, temporal, and harmony dimensions. Experiments demonstrate that LaMoGen establishes a new baseline for both interpretability and controllability, outperforming prior methods on our benchmark and two public datasets. These results highlight the advantages of symbolic reasoning and agent-based design for language-driven motion synthesis.

</details>

---

### 19. [Sema: A High-performance System for LLM-based Semantic Query Processing](https://arxiv.org/abs/2603.11622)

**基本信息**

- 🔗 arXiv: [`2603.11622`](https://arxiv.org/abs/2603.11622)
- 👥 作者: Kangkang Qi, Dongyang Xie, Wenbo Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11622.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深度集成大型语言模型（LLMs）到数据查询和分析系统中，创建“语义查询引擎”。这代表了LLMs作为核心计算组件在数据处理领域的高级应用，属于“化学大模型”主题中，大模型与领域特定工具和基础设施深度结合的前沿方向。对于构建化学领域的智能数据分析和知识发现平台具有参考价值。

**📖 中文摘要**

本文提出了Sema，一个基于DuckDB构建的高性能语义查询引擎，将LLM驱动的语义运算符视为一等公民。Sema引入了SemaSQL，一种声明性方言，允许用户将自然语言表达式无缝注入标准SQL子句中，从而实现端到端的优化和执行。在逻辑层面，Sema的优化器压缩自然语言表达式并从语义运算符推导关系约束。在运行时，Sema采用自适应查询执行（AQE）来动态重排运算符、融合语义操作并应用提示词批处理。该方法寻求在准确性约束下平衡令牌消耗和延迟的帕累托最优执行路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into data analytics has unlocked powerful capabilities for reasoning over bulk structured and unstructured data. However, existing systems typically rely on either DataFrame primitives, which lack the efficient execution infrastructure of modern DBMSs, or SQL User-Defined Functions (UDFs), which isolate semantic logic from the query optimizer and burden users with implementation complexities. The LLM-powered semantic operators also bring new challenges due to the high cost and non-deterministic nature of LLM invocation, where conventional optimization rules and cost models are inapplicable for their optimization. To bridge these gaps, we present Sema, a high-performance semantic query engine built on DuckDB that treats LLM-powered semantic operators as first-class citizens. Sema introduces SemaSQL, a declarative dialect that allows users seamlessly inject natural language expressions into standard SQL clauses, enabling end-to-end optimization and execution. At the logical level, the optimizer of Sema compresses natural language expressions and deduces relational constraints from semantic operators. At runtime, Sema employs Adaptive Query Execution (AQE) to dynamically reorder operators, fuse semantic operations, and apply prompt batching. This approach seeks a Pareto-optimal execution path balancing token consumption and latency under accuracy constraints. We evaluate Sema on 20 semantic queries across classification, summarization, and extraction tasks. Experimental results demonstrate that Sema achieves $2-10 \times$ speedup against three baseline systems while achieving competitive result quality.

</details>

---

### 20. [MedPruner: Training-Free Hierarchical Token Pruning for Efficient 3D Medical Image Understanding in Vision-Language Models](https://arxiv.org/abs/2603.11625)

**基本信息**

- 🔗 arXiv: [`2603.11625`](https://arxiv.org/abs/2603.11625)
- 👥 作者: Shengyuan Liu, Zanting Ye, Yunrui Lin 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11625.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对视觉-语言大模型（VLMs）的推理效率优化，提出了一个新颖的令牌剪枝框架。虽然应用场景是医学图像，但其优化大模型计算效率的方法论具有普适性。对于计算资源密集的“化学大模型”（尤其是处理3D分子结构或光谱图像的模型）的部署和加速具有直接的技术参考价值。

**📖 中文摘要**

本文提出了MedPruner，一个专为高效3D医学图像理解设计的、免训练且与模型无关的分层令牌剪枝框架。MedPruner引入了一个两阶段机制：一个层间锚点过滤模块以消除切片级的时间冗余，随后是一个动态信息核选择策略，通过量化累积注意力权重来实现自适应的令牌级压缩。在三个3D医学基准测试和三种不同的医学VLM上的广泛实验揭示了现有架构中存在大量的令牌冗余。值得注意的是，MedPruner使诸如MedGemma等模型在保留少于5%视觉令牌的情况下，保持甚至超过其原始性能，从而大幅减少计算开销。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While specialized Medical Vision-Language Models (VLMs) have achieved remarkable success in interpreting 2D and 3D medical modalities, their deployment for 3D volumetric data remains constrained by significant computational inefficiencies. Current architectures typically suffer from massive anatomical redundancy due to the direct concatenation of consecutive 2D slices and lack the flexibility to handle heterogeneous information densities across different slices using fixed pruning ratios. To address these challenges, we propose MedPruner, a training-free and model-agnostic hierarchical token pruning framework specifically designed for efficient 3D medical image understanding. MedPruner introduces a two-stage mechanism: an Inter-slice Anchor-based Filtering module to eliminate slice-level temporal redundancy, followed by a Dynamic Information Nucleus Selection strategy that achieves adaptive token-level compression by quantifying cumulative attention weights. Extensive experiments on three 3D medical benchmarks and across three diverse medical VLMs reveal massive token redundancy in existing architectures. Notably, MedPruner enables models such as MedGemma to maintain or even exceed their original performance while retaining fewer than 5% of visual tokens, thereby drastically reducing computational overhead and validating the necessity of dynamic token selection for practical clinical deployment. Our code will be released.

</details>

---

### 21. [Developing Foundation Models for Universal Segmentation from 3D Whole-Body Positron Emission Tomography](https://arxiv.org/abs/2603.11627)

**基本信息**

- 🔗 arXiv: [`2603.11627`](https://arxiv.org/abs/2603.11627)
- 👥 作者: Yichi Zhang, Le Xue, Wenbo Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11627.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是构建了一个大规模、高质量的3D医学影像数据集，并在此基础上开发了一个通用的分割基础模型（SegAnyPET）。这直接提供了可用于相关研究（包括可能拓展至化学成像分析）的“数据资源”和“模型工具”。虽然聚焦PET，但其数据构建范式、模型架构（支持提示的3D分割模型）对于处理其他3D科学数据（如3D分子密度场、3D显微图像）具有重要的参考和迁移价值。

**📖 中文摘要**

本文开发了用于3D全身正电子发射断层扫描（PET）通用分割的基础模型。作者首先构建了迄今为止最大、最全面的PET数据集，包含11041个3D全身PET扫描和59831个分割掩码。基于此数据集，提出了SegAnyPET，一个具有通用适用性的创新基础模型，适用于多样化的分割任务。该模型基于3D架构，采用提示工程策略进行掩码生成，支持通用且可扩展的器官和病灶分割，支持以最小工作量进行高效的人工校正，并支持临床人机回圈工作流。在多中心、多示踪剂、多疾病数据集上的广泛评估表明，SegAnyPET在广泛的分割任务中实现了强大的零样本性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a key nuclear medicine imaging modality that visualizes radiotracer distributions to quantify in vivo physiological and metabolic processes, playing an irreplaceable role in disease management. Despite its clinical importance, the development of deep learning models for quantitative PET image analysis remains severely limited, driven by both the inherent segmentation challenge from PET's paucity of anatomical contrast and the high costs of data acquisition and annotation. To bridge this gap, we develop generalist foundational models for universal segmentation from 3D whole-body PET imaging. We first build the largest and most comprehensive PET dataset to date, comprising 11041 3D whole-body PET scans with 59831 segmentation masks for model development. Based on this dataset, we present SegAnyPET, an innovative foundational model with general-purpose applicability to diverse segmentation tasks. Built on a 3D architecture with a prompt engineering strategy for mask generation, SegAnyPET enables universal and scalable organ and lesion segmentation, supports efficient human correction with minimal effort, and enables a clinical human-in-the-loop workflow. Extensive evaluations on multi-center, multi-tracer, multi-disease datasets demonstrate that SegAnyPET achieves strong zero-shot performance across a wide range of segmentation tasks, highlighting its potential to advance the clinical applications of molecular imaging.

</details>

---

### 22. [VisDoT : Enhancing Visual Reasoning through Human-Like Interpretation Grounding and Decomposition of Thought](https://arxiv.org/abs/2603.11631)

**基本信息**

- 🔗 arXiv: [`2603.11631`](https://arxiv.org/abs/2603.11631)
- 👥 作者: Eunsoo Lee, Jeongwoo Lee, Minki Hong 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11631.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大型视觉-语言模型（VLMs）在复杂视觉推理任务（如图表理解）上的性能，其方法是引入类人的感知 grounding 和思维分解（DoT）提示。这属于“化学大模型”主题中，关于如何让大模型更好地理解和推理科学数据（如化学图表、光谱图、分子示意图）的前沿研究。其提出的感知-逻辑分离框架对于设计化学领域的专业VLM具有重要的方法论启示。

**📖 中文摘要**

本文提出了VisDoT，一个通过类人解释性 grounding 来增强视觉推理的框架。作者基于图形感知理论形式化了四个感知任务，包括位置和长度。在此基础上，引入了思维分解（Decomposition-of-Thought, DoT）提示，将问题顺序分解为视觉感知子问题和逻辑子问题。使用VisDoT对InternVL进行微调，在ChartQA上实现了+11.2%的改进，并在更具挑战性的ChartQAPro基准上超越了GPT-4o。在新引入的VisDoTQA基准上，模型改进了+33.2%。此外，在多样化的开放域VQA基准上一致的零样本增益证实了感知-逻辑分离策略对于视觉问答的泛化性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large vision-language models (LVLMs) struggle to reliably detect visual primitives in charts and align them with semantic representations, which severely limits their performance on complex visual reasoning. This lack of perceptual grounding constitutes a major bottleneck for chart-based reasoning. We propose VisDoT, a framework that enhances visual reasoning through human-like interpretation grounding. We formalize four perceptual tasks based on the theory of graphical perception, including position and length. Building on this foundation, we introduce Decomposition-of-Thought (DoT) prompting, which sequentially separates questions into visual perception sub-questions and logic sub-questions. Fine-tuning InternVL with VisDoT achieves a +11.2% improvement on ChartQA and surpasses GPT-4o on the more challenging ChartQAPro benchmark. On the newly introduced VisDoTQA benchmark, the model improves by +33.2%. Furthermore, consistent zero-shot gains on diverse open-domain VQA benchmarks confirm the generalizability of the perception-logic separation strategy for visual question answering. VisDoT leverages human-like perception to enhance visual grounding, achieving state-of-the-art chart understanding and interpretable visual reasoning.

</details>

---

### 23. [Tokenization Allows Multimodal Large Language Models to Understand, Generate and Edit Architectural Floor Plans](https://arxiv.org/abs/2603.11640)

**基本信息**

- 🔗 arXiv: [`2603.11640`](https://arxiv.org/abs/2603.11640)
- 👥 作者: Sizhong Qin, Ramon Elias Weber, Xinzheng Lu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11640.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个能够理解、生成和编辑复杂结构化图形（建筑平面图）的多模态大语言模型。这直接属于“化学大模型”主题中，大模型处理和理解化学领域结构化表示（如分子图、化学结构式、反应流程图）的平行研究。其“离散令牌化-符号推理-生成”的技术路径对于化学大模型处理分子图相关任务具有直接的借鉴意义。

**📖 中文摘要**

本文提出了HouseMind，一个多模态大语言模型，将建筑平面图的理解、生成和编辑统一在一个框架中。作者引入了离散的房间实例令牌来构建一个统一的词汇表，以桥接布局和符号推理。通过多模态对齐和指令微调，该模型能够根据文本指令合成连贯、可控的布局。实验表明，该框架在保持高效和可本地部署的同时，实现了卓越的几何有效性和可控性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Architectural floor plan design demands joint reasoning over geometry, semantics, and spatial hierarchy, which remains a major challenge for current AI systems. Although recent diffusion and language models improve visual fidelity, they still struggle with coherent spatial reasoning and controllable generation. We present HouseMind, a multimodal large language model that unifies floor plan understanding, generation, and editing in one framework. We introduce discrete room-instance tokens to construct a unified vocabulary that bridges layouts and symbolic reasoning. With multimodal alignment and instruction tuning, the model synthesizes coherent, controllable layouts from text instructions. Experiments show how the framework achieves superior geometric validity and controllability while remaining efficient and locally deployable.

</details>

---

### 24. [PolyCrysDiff: Controllable Generation of Three-Dimensional Computable Polycrystalline Material Structures](https://arxiv.org/abs/2603.11695)

**基本信息**

- 🔗 arXiv: [`2603.11695`](https://arxiv.org/abs/2603.11695)
- 👥 作者: Chi Chen, Tianle Jiang, Xiaodong Wei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成模型（扩散模型）来生成和设计多晶材料的结构，这直接属于“化学大模型”在材料科学和化学信息学中的应用范畴。

**📖 中文摘要**

本文提出了PolyCrysDiff，一个基于条件潜在扩散的框架，用于端到端生成可计算的3D多晶材料微观结构。该工作直接面向材料科学中的结构生成问题，属于化学信息学中“化学大模型”在材料生成领域的应用。通过扩散模型生成符合目标晶粒形态、取向分布和空间相关性的3D结构，并利用晶体塑性有限元方法验证了生成结构的可计算性和物理有效性。该框架展示了生成模型在可控构建复杂材料微观结构方面的能力，可用于探索结构-性能关系，是数据驱动的材料优化与设计的关键一步。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The three-dimensional (3D) microstructures of polycrystalline materials exert a critical influence on their mechanical and physical properties. Realistic, controllable construction of these microstructures is a key step toward elucidating structure-property relationships, yet remains a formidable challenge. Herein, we propose PolyCrysDiff, a framework based on conditional latent diffusion that enables the end-to-end generation of computable 3D polycrystalline microstructures. Comprehensive qualitative and quantitative evaluations demonstrate that PolyCrysDiff faithfully reproduces target grain morphologies, orientation distributions, and 3D spatial correlations, while achieving an $R^2$ over 0.972 on grain attributes (e.g., size and sphericity) control, thereby outperforming mainstream approaches such as Markov random field (MRF)- and convolutional neural network (CNN)-based methods. The computability and physical validity of the generated microstructures are verified through a series of crystal plasticity finite element method (CPFEM) simulations. Leveraging PolyCrysDiff's controllable generative capability, we systematically elucidate how grain-level microstructural characteristics affect the mechanical properties of polycrystalline materials. This development is expected to pave a key step toward accelerated, data-driven optimization and design of polycrystalline materials.

</details>

---

### 25. [EvoFlows: Evolutionary Edit-Based Flow-Matching for Protein Engineering](https://arxiv.org/abs/2603.11703)

**基本信息**

- 🔗 arXiv: [`2603.11703`](https://arxiv.org/abs/2603.11703)
- 👥 作者: Nicolas Deutschmann, Constance Ferragu, Jonathan D. Ziegler 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11703.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于蛋白质工程的生成模型（EvoFlows），这是一种专门针对生物分子（蛋白质）序列的“化学大模型”，属于化学信息学和计算生物学交叉领域。

**📖 中文摘要**

本文介绍了EvoFlows，一种适用于蛋白质工程的变长序列到序列建模方法。与自回归和掩码语言模型不同，EvoFlows通过对模板蛋白质序列执行有限、可控数量的插入、删除和替换来预测突变。该方法利用编辑流来学习进化相关蛋白质序列之间的突变轨迹，同时模拟相关天然蛋白质的分布以及连接它们的突变路径。通过在大规模蛋白质序列数据集上的评估，表明EvoFlows在捕获蛋白质序列分布方面与常用的掩码语言模型质量相当，同时在从给定模板生成非平凡且类天然突变体方面表现出改进的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce EvoFlows, a variable-length sequence-to-sequence protein modeling approach uniquely suited to protein engineering. Unlike autoregressive and masked language models, EvoFlows perform a limited, controllable number of insertions, deletions, and substitutions on a template protein sequence. In other words, EvoFlows predict not only _which_ mutation to perform, but also _where_ it should occur. Our approach leverages edit flows to learn mutational trajectories between evolutionarily-related protein sequences, simultaneously modeling distributions of related natural proteins and the mutational paths connecting them. Through extensive _in silico_ evaluation on diverse protein communities from UNIREF and OAS, we demonstrate that EvoFlows capture protein sequence distributions with a quality comparable to leading masked language models commonly used in protein engineering, while showing improved ability to generate non-trivial yet natural-like mutants from a given template protein.

</details>

---

### 26. [PhiPlot: A Web-Based Interactive EDA Environment for Atmospherically Relevant Molecules](https://arxiv.org/abs/2603.11751)

**基本信息**

- 🔗 arXiv: [`2603.11751`](https://arxiv.org/abs/2603.11751)
- 👥 作者: Matias Loukojärvi, Ananth Mahadevan, Katsiaryna Haitsiukevich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11751.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于探索和分析大气相关分子数据集的交互式工具（PhiPlot），这为化学信息学研究提供了可用的数据资源和探索环境。

**📖 中文摘要**

本文介绍了PhiPlot，一个基于Web的交互式探索性数据分析环境，专门用于大气相关分子的高维数据集。该工具集成了可视化、聚类和领域知识引导的嵌入细化功能，旨在帮助发现数据中的模式并支持假设生成。该应用连接到一个不断演化的分子数据库集合，为大气化学中的数据驱动研究提供了一个可访问的界面。其关注点在于大气气溶胶形成研究中分子的探索和分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in computational chemistry have produced high-dimensional datasets on atmospherically relevant molecules. To aid exploration of such datasets, particularly for the study of atmospheric aerosol formation, we introduce PhiPlot: a web-based environment for interactive exploration and knowledge-based dimensionality reduction. The integration of visualisation, clustering, and domain knowledge-guided embedding refinement enables the discovery of patterns in the data and supports hypothesis generation. The application connects to an existing, evolving collection of molecular databases, offering an accessible interface for data-driven research in atmospheric chemistry.

</details>

---

### 27. [A Decade of Generative Adversarial Networks for Porous Material Reconstruction](https://arxiv.org/abs/2603.11836)

**基本信息**

- 🔗 arXiv: [`2603.11836`](https://arxiv.org/abs/2603.11836)
- 👥 作者: Ali Sadeghkhani, Brandon Bennett, Masoud Babaei 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11836.pdf)

**💡 相关性分析**

满足标准3：论文是关于生成对抗网络在多孔材料重建中应用的系统性综述，涵盖了该领域十年的进展、架构分类和挑战，属于针对特定领域生成模型（“化学大模型”在材料科学中的应用）的重要综述。

**📖 中文摘要**

本文对过去十年（2017-2026年初）使用生成对抗网络进行多孔材料图像重建的96篇同行评审文章进行了系统性综述。文章将GAN架构分为六类，并分析了其在孔隙度精度、渗透率预测和可重建体积等方面的进展。尽管取得了显著进步，但在计算效率、大规模重建的内存限制以及2D到3D转换中的结构连续性保持方面仍存在挑战。该综述为基于特定应用需求选择适当的GAN架构提供了一个全面的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital reconstruction of porous materials has become increasingly critical for applications ranging from geological reservoir characterization to tissue engineering and electrochemical device design. While traditional methods such as micro-computed tomography and statistical reconstruction approaches have established foundations in this field, the emergence of deep learning techniques, particularly Generative Adversarial Networks (GANs), has revolutionized porous media reconstruction capabilities. This review systematically analyzes 96 peer-reviewed articles published from 2017 to early 2026, examining the evolution and applications of GAN-based approaches for porous material image reconstruction. We categorize GAN architectures into six distinct classes, namely Vanilla GANs, Multi-Scale GANs, Conditional GANs, Attention-Enhanced GANs, Style-based GANs, and Hybrid Architecture GANs. Our analysis reveals substantial progress including improvements in porosity accuracy (within 1% of original samples), permeability prediction (up to 79% reduction in mean relative errors), and achievable reconstruction volumes (from initial $64^3$ to current $2{,}200^3$ voxels). Despite these advances, persistent challenges remain in computational efficiency, memory constraints for large-scale reconstruction, and maintaining structural continuity in 2D-to-3D transformations. This systematic analysis provides a comprehensive framework for selecting appropriate GAN architectures based on specific application requirements.

</details>

---

### 28. [Inverse Neural Operator for ODE Parameter Optimization](https://arxiv.org/abs/2603.11854)

**基本信息**

- 🔗 arXiv: [`2603.11854`](https://arxiv.org/abs/2603.11854)
- 👥 作者: Zhi-Song Liu, Wenqing Peng, Helmi Toropainen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11854.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的神经算子（INO）用于ODE参数反演，这属于科学机器学习中“化学大模型”（用于解决化学动力学逆问题）的范畴。

**📖 中文摘要**

本文提出了逆向神经算子，一个用于从稀疏、部分观测中恢复隐藏常微分方程参数的两阶段框架。第一阶段使用带有交叉注意力的条件傅里叶神经算子学习一个可微代理，从任意稀疏输入重建完整的ODE轨迹。第二阶段使用摊销漂移模型在参数空间中学习一个核加权速度场，将随机参数初始化向真实值传输，而无需通过代理反向传播。该方法在真实世界的大气化学基准和合成基因调控网络上进行了实验，展示了在参数恢复精度和推理速度上的优势。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose the Inverse Neural Operator (INO), a two-stage framework for recovering hidden ODE parameters from sparse, partial observations. In Stage 1, a Conditional Fourier Neural Operator (C-FNO) with cross-attention learns a differentiable surrogate that reconstructs full ODE trajectories from arbitrary sparse inputs, suppressing high-frequency artifacts via spectral regularization. In Stage 2, an Amortized Drifting Model (ADM) learns a kernel-weighted velocity field in parameter space, transporting random parameter initializations toward the ground truth without backpropagating through the surrogate, avoiding the Jacobian instabilities that afflict gradient-based inversion in stiff regimes. Experiments on a real-world stiff atmospheric chemistry benchmark (POLLU, 25 parameters) and a synthetic Gene Regulatory Network (GRN, 40 parameters) show that INO outperforms gradient-based and amortized baselines in parameter recovery accuracy while requiring only 0.23s inference time, a 487x speedup over iterative gradient descent.

</details>

---

### 29. [AdaFuse: Accelerating Dynamic Adapter Inference via Token-Level Pre-Gating and Fused Kernel Optimization](https://arxiv.org/abs/2603.11873)

**基本信息**

- 🔗 arXiv: [`2603.11873`](https://arxiv.org/abs/2603.11873)
- 👥 作者: Qiyang Li, Rui Kong, Yuchen Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11873.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大型语言模型（作为“化学大模型”的基础架构）中动态适配器的推理效率，直接围绕提升大模型能力这一主题。

**📖 中文摘要**

本文提出AdaFuse框架，旨在解决将动态稀疏结构（如MoE）与参数高效适配器（如LoRA）集成到大型语言模型（LLMs）时带来的推理延迟激增问题。该框架通过算法与底层硬件系统的协同设计，实现高效的动态适配器执行。其核心创新在于采用令牌级预门控策略，在令牌处理前做出单一的全局路由决策，从而静态化每个令牌的执行路径，为整体优化创造机会。随后开发了一个定制的CUDA内核，以单一高效的操作合并所有选定LoRA适配器的参数。实验表明，AdaFuse在保持与最先进动态适配器相当精度的同时，将解码延迟降低了超过2.4倍。这项工作直接针对提升和优化化学信息学等领域可能依赖的“化学大模型”（作为LLM的一种应用或变体）的推理效率，属于核心主题相关的技术推进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of dynamic, sparse structures like Mixture-of-Experts (MoE) with parameter-efficient adapters (e.g., LoRA) is a powerful technique for enhancing Large Language Models (LLMs). However, this architectural enhancement comes at a steep cost: despite minimal increases in computational load, the inference latency often skyrockets, leading to decoding speeds slowing by over 2.5 times. Through a fine-grained performance analysis, we pinpoint the primary bottleneck not in the computation itself, but in the severe overhead from fragmented, sequential CUDA kernel launches required for conventional dynamic routing. To address this challenge, we introduce AdaFuse, a framework built on a tight co-design between the algorithm and the underlying hardware system to enable efficient dynamic adapter execution. Departing from conventional layer-wise or block-wise routing, AdaFuse employs a token-level pre-gating strategy, which makes a single, global routing decision for all adapter layers before a token is processed. This "decide-once, apply-everywhere" approach effectively staticizes the execution path for each token, creating an opportunity for holistic optimization. We capitalize on this by developing a custom CUDA kernel that performs a fused switching operation, merging the parameters of all selected LoRA adapters into the backbone model in a single, efficient pass. Experimental results on popular open-source LLMs show that AdaFuse achieves accuracy on par with state-of-the-art dynamic adapters while drastically cutting decoding latency by a factor of over 2.4x, thereby bridging the gap between model capability and inference efficiency.

</details>

---

### 30. [Bielik-Minitron-7B: Compressing Large Language Models via Structured Pruning and Knowledge Distillation for the Polish Language](https://arxiv.org/abs/2603.11881)

**基本信息**

- 🔗 arXiv: [`2603.11881`](https://arxiv.org/abs/2603.11881)
- 👥 作者: Remigiusz Kinas, Paweł Kiszczak, Sergio P. Perez 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11881.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心是关于大型语言模型的压缩与优化，属于“化学大模型”的基础模型技术范畴；2) 提出的两阶段压缩方法（结构化剪枝+知识蒸馏）和整体流程，可作为构建或优化领域大模型（如化学大模型）的可用方法或工具参考。

**📖 中文摘要**

本报告详细介绍了Bielik-Minitron-7B模型的创建过程，这是一个针对欧洲语言优化的、压缩后的7.35B参数大型语言模型。该模型通过结合结构化混合剪枝和知识蒸馏的两阶段压缩方法，将参数数量从11.04B减少到7.35B。压缩后的模型经过监督微调、直接偏好优化和强化学习对齐流程，恢复了约90%的基线模型性能，同时提供高达50%的推理加速。这项工作展示了为资源较少语言创建高效语言模型的途径。虽然主要面向自然语言，但其压缩、蒸馏和对齐大型语言模型的方法论，对于构建和优化特定领域（如化学）的“化学大模型”具有直接的参考价值和工具意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This report details the creation of Bielik-Minitron-7B, a compressed 7.35B parameter version of the Bielik-11B-v3.0 model, specifically optimized for European languages. By leveraging a two-stage compression methodology inspired by the NVIDIA Minitron approach, we combined structured hybrid pruning and knowledge distillation to reduce the model's parameter count by 33.4%, from 11.04B to 7.35B. We utilized the NVIDIA Model Optimizer for structural pruning and the NVIDIA NeMo Framework for logit-based distillation for quality recovery. Following distillation, the model underwent a rigorous alignment pipeline consisting of Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO-P), and Reinforcement Learning (GRPO). Our final model successfully recovered approximately 90% of the baseline model's performance while providing up to 50% inference speedup. This approach demonstrates an efficient pathway to create language models for less-represented languages, preserving the original model quality while reducing inference deployment costs.

</details>

---

### 31. [Chem4DLLM: 4D Multimodal LLMs for Chemical Dynamics Understanding](https://arxiv.org/abs/2603.11924)

**基本信息**

- 🔗 arXiv: [`2603.11924`](https://arxiv.org/abs/2603.11924)
- 👥 作者: Xinyu Li, Zhen Zhang, Qi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11924.pdf)

**💡 相关性分析**

满足标准1、2和3：1) 核心主题是构建用于化学动力学理解的4D多模态大语言模型（Chem4DLLM），直接围绕“化学大模型”主题；2) 提供了专门的数据集Chem4DBench，这是用于该主题的重要数据资源；3) 论文整体上是对化学动态理解这一新任务的展望和框架提出，包含重要的相关讨论。

**📖 中文摘要**

本文针对现有化学理解任务主要依赖静态分子表示的局限性，引入了化学动力学理解新任务，旨在将4D分子轨迹转化为可解释的自然语言描述。为此，作者构建了首个配对4D分子轨迹与专家解释的数据集Chem4DBench，并提出了统一模型Chem4DLLM。该模型集成了等变图编码器和预训练大语言模型，以显式捕获分子几何和旋转动力学。论文希望Chem4DLLM能激发动态化学理解和多模态科学推理的进一步研究。这项工作直接位于“化学大模型”和“科学推理”的交叉点，提出了一个面向化学动态过程的新型多模态大语言模型框架和基准数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Existing chemical understanding tasks primarily rely on static molecular representations, limiting their ability to model inherently dynamic phenomena such as bond breaking or conformational changes, which are essential for a chemist to understand chemical reactions. To address this gap, we introduce Chemical Dynamics Understanding (ChemDU), a new task that translates 4D molecular trajectories into interpretable natural-language explanations. ChemDU focuses on fundamental dynamic scenarios, including gas-phase and catalytic reactions, and requires models to reason about key events along molecular trajectories, such as bond formation and dissociation, and to generate coherent, mechanistically grounded narratives. To benchmark this capability, we construct Chem4DBench, the first dataset pairing 4D molecular trajectories with expert-authored explanations across these settings. We further propose Chem4DLLM, a unified model that integrates an equivariant graph encoder with a pretrained large language model to explicitly capture molecular geometry and rotational dynamics. We hope that ChemDU, together with Chem4DBench and Chem4DLLM, will stimulate further research in dynamic chemical understanding and multimodal scientific reasoning.

</details>

---

### 32. [Learning Transferable Sensor Models via Language-Informed Pretraining](https://arxiv.org/abs/2603.11950)

**基本信息**

- 🔗 arXiv: [`2603.11950`](https://arxiv.org/abs/2603.11950)
- 👥 作者: Yuliang Chen, Arvind Pillai, Yu Yvonne Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11950.pdf)

**💡 相关性分析**

满足标准2：论文提出的SLIP框架（传感器语言知情预训练）提供了将特定领域数据（如时序信号）与语言模型对齐以进行零样本迁移和生成式推理的方法论和工具，这种方法可迁移并应用于“质谱结构推理”中，用于构建质谱数据与分子结构描述之间的关联模型。

**📖 中文摘要**

本文介绍了SLIP，一个用于学习跨不同传感器设置泛化的、语言对齐表征的开源框架。SLIP整合了对比对齐与传感器条件描述生成，促进了判别性理解和生成式推理。通过跨注意力机制重用预训练的仅解码器语言模型，并引入灵活的补丁嵌入器，SLIP支持在推理时处理不同的时间分辨率和可变长度输入，而无需重新训练。在11个数据集上的评估表明，SLIP在零样本迁移、信号描述和问答任务上表现出色。这项工作虽然主要面向传感器数据，但其核心是构建能够与语言模型对齐、支持多模态推理的通用表征学习框架。这种将领域数据（如传感器时序、或可类比为质谱时序/谱图）与大型语言模型结合进行跨模态对齐和推理的方法，为“质谱结构推理”中构建谱图-文本联合模型提供了重要的技术思路和工具参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern sensing systems generate large volumes of unlabeled multivariate time-series data. This abundance of unlabeled data makes self-supervised learning (SSL) a natural approach for learning transferable representations. However, most existing approaches are optimized for reconstruction or forecasting objectives and often fail to capture the semantic structure required for downstream classification and reasoning tasks. While recent sensor-language alignment methods improve semantic generalization through captioning and zero-shot transfer, they are limited to fixed sensor configurations, such as predefined channel sets, signal lengths, or temporal resolutions, which hinders cross-domain applicability. To address these gaps, we introduce \textbf{SLIP} (\textbf{S}ensor \textbf{L}anguage-\textbf{I}nformed \textbf{P}retraining), an open-source framework for learning language-aligned representations that generalize across diverse sensor setups. SLIP integrates contrastive alignment with sensor-conditioned captioning, facilitating both discriminative understanding and generative reasoning. By repurposing a pretrained decoder-only language model via cross-attention and introducing an elegant, flexible patch-embedder, SLIP supports different temporal resolutions and variable-length input at inference time without additional retraining. Across 11 datasets, SLIP demonstrates superior performance in zero-shot transfer, signal captioning, and question answering. It achieves a 77.14% average linear-probing accuracy, a 5.93% relative improvement over strong baselines, and reaches 64.83% accuracy in sensor-based question answering.

</details>

---

### 33. [Nyxus: A Next Generation Image Feature Extraction Library for the Big Data and AI Era](https://arxiv.org/abs/2603.12016)

**基本信息**

- 🔗 arXiv: [`2603.12016`](https://arxiv.org/abs/2603.12016)
- 👥 作者: Nicholas Schaub, Andriy Kharchenko, Hamdah Abbasi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12016.pdf)

**💡 相关性分析**

满足标准2：论文提出的Nyxus库是一个高效、可扩展、跨平台的特征提取工具，虽然主要针对图像，但其核心理念和架构（如支持多维数据、可编程特征集、适用于机器学习）可作为处理化学信息学中复杂数据（如质谱成像图、分子结构图）的重要工具或参考实现。

**📖 中文摘要**

本文介绍了Nyxus，一个为大数据和AI时代设计的下一代图像特征提取库。针对现代成像仪器产生海量数据的特点，Nyxus从底层设计上支持可扩展的核外特征提取，适用于2D和3D图像数据，并经过严格测试。其综合特征集覆盖了包括放射组学和细胞分析在内的多个生物医学领域，并针对CPU和GPU进行了计算可扩展性设计。Nyxus被打包为Python包、命令行工具、Napari插件以及OCI兼容容器，以满足不同用户需求。更重要的是，Nyxus支持通过编程方式调整特征集，以实现最佳计算效率或覆盖范围，用于新颖的机器学习和深度学习应用。对于化学信息学和质谱分析领域，虽然Nyxus主要面向图像，但其高效、可扩展的特征提取引擎和设计理念，可以启发或适配用于处理质谱成像数据或从分子结构图像中提取特征，为相关主题提供强大的数据处理工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern imaging instruments can produce terabytes to petabytes of data for a single experiment. The biggest barrier to processing big image datasets has been computational, where image analysis algorithms often lack the efficiency needed to process such large datasets or make tradeoffs in robustness and accuracy. Deep learning algorithms have vastly improved the accuracy of the first step in an analysis workflow (region segmentation), but the expansion of domain specific feature extraction libraries across scientific disciplines has made it difficult to compare the performance and accuracy of extracted features. To address these needs, we developed a novel feature extraction library called Nyxus. Nyxus is designed from the ground up for scalable out-of-core feature extraction for 2D and 3D image data and rigorously tested against established standards. The comprehensive feature set of Nyxus covers multiple biomedical domains including radiomics and cellular analysis, and is designed for computational scalability across CPUs and GPUs. Nyxus has been packaged to be accessible to users of various skill sets and needs: as a Python package for code developers, a command line tool, as a Napari plugin for low to no-code users or users that want to visualize results, and as an Open Container Initiative (OCI) compliant container that can be used in cloud or super-computing workflows aimed at processing large data sets. Further, Nyxus enables a new methodological approach to feature extraction allowing for programmatic tuning of many features sets for optimal computational efficiency or coverage for use in novel machine learning and deep learning applications.

</details>

---

### 34. [Chemical Reaction Networks Learn Better than Spiking Neural Networks](https://arxiv.org/abs/2603.12060)

**基本信息**

- 🔗 arXiv: [`2603.12060`](https://arxiv.org/abs/2603.12060)
- 👥 作者: Sophie Jaffard, Ivo F. Sbalzarini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12060.pdf)

**💡 相关性分析**

满足标准1和3：1) 核心主题是研究化学反应网络作为一种机器学习模型，这本身就是一种特殊形式的“化学大模型”或化学计算模型；2) 论文通过理论证明和实验，对比了化学反应网络与神经网络的优劣，包含了对这种新型计算范式的重要讨论和展望。

**📖 中文摘要**

本文从数学上证明，没有隐藏层的化学反应网络可以解决那些尖峰神经网络需要隐藏层才能完成的任务。证明使用了化学反应网络的确定性质量作用动力学公式。作者证明，某个无隐藏层的反应网络可以学习一个先前被证明需要带隐藏层的尖峰神经网络才能实现的分类任务。论文提供了网络全局行为的遗憾界分析，并分析了其渐近行为和VC维。在一个数值实验中，作者证实了所提出的化学反应网络对于像素图像中手写数字分类的学习能力，并且表明它比带隐藏层的尖峰神经网络更准确、更高效地解决了该任务。这为化学计算机中的机器学习提供了动机，并为生物细胞如何在生化反应网络中表现出比神经元网络更高效的学习行为提供了数学解释。这项工作直接关联到使用非传统计算模型（化学反应网络）进行机器学习，为构建新型的、受生物启发的“化学大模型”或计算框架提供了理论基础和可行性证明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We mathematically prove that chemical reaction networks without hidden layers can solve tasks for which spiking neural networks require hidden layers. Our proof uses the deterministic mass-action kinetics formulation of chemical reaction networks. Specifically, we prove that a certain reaction network without hidden layers can learn a classification task previously proved to be achievable by a spiking neural network with hidden layers. We provide analytical regret bounds for the global behavior of the network and analyze its asymptotic behavior and Vapnik-Chervonenkis dimension. In a numerical experiment, we confirm the learning capacity of the proposed chemical reaction network for classifying handwritten digits in pixel images, and we show that it solves the task more accurately and efficiently than a spiking neural network with hidden layers. This provides a motivation for machine learning in chemical computers and a mathematical explanation for how biological cells might exhibit more efficient learning behavior within biochemical reaction networks than neuronal networks.

</details>

---

### 35. [Paper Title: LoV3D: Grounding Cognitive Prognosis Reasoning in Longitudinal 3D Brain MRI via Regional Volume Assessments](https://arxiv.org/abs/2603.12071)

**基本信息**

- 🔗 arXiv: [`2603.12071`](https://arxiv.org/abs/2603.12071)
- 👥 作者: Zhaoyang Jiang, Zhizhong Fu, David McAllister 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12071.pdf)

**💡 相关性分析**

满足标准2：论文提出的LoV3D流程，特别是其结合领域特定指标（体积测量）与视觉语言模型、并通过自动化验证器进行对齐的方法，为在其他科学领域（如化学、质谱学）构建类似的数据驱动、可解释的多模态推理模型提供了重要的方法学工具和框架参考。

**📖 中文摘要**

本文提出了LoV3D，一个用于训练3D视觉语言模型的流程，用于读取纵向T1加权脑部MRI，产生区域级解剖学评估，与先前扫描进行纵向比较，并最终输出三类诊断及综合诊断摘要。该分级流程通过强制标签一致性、纵向连贯性和生物学合理性来夯实最终诊断，从而降低幻觉风险。训练过程引入了一个临床加权的验证器，根据从标准化体积指标导出的规范参考自动评分候选输出，驱动无需人工标注的直接偏好优化。在ADNI测试集上，LoV3D达到了93.7%的三类诊断准确率。这项工作展示了如何将领域知识（体积指标）与大语言模型（VLM）训练相结合，构建 grounded 的、可解释的医学影像诊断模型。其方法论——将结构化领域测量与VLM生成相结合，并使用自动化验证器进行对齐——对于在“化学大模型”或“质谱结构推理”中构建类似的可解释、基于证据的推理系统（例如，将质谱特征量化与分子结构描述生成相结合）具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Longitudinal brain MRI is essential for characterizing the progression of neurological diseases such as Alzheimer's disease assessment. However, current deep-learning tools fragment this process: classifiers reduce a scan to a label, volumetric pipelines produce uninterpreted measurements, and vision-language models (VLMs) may generate fluent but potentially hallucinated conclusions. We present LoV3D, a pipeline for training 3D vision-language models, which reads longitudinal T1-weighted brain MRI, produces a region-level anatomical assessment, conducts longitudinal comparison with the prior scan, and finally outputs a three-class diagnosis (Cognitively Normal, Mild Cognitive Impairment, or Dementia) along with a synthesized diagnostic summary. The stepped pipeline grounds the final diagnosis by enforcing label consistency, longitudinal coherence, and biological plausibility, thereby reducing the risks of hallucinations. The training process introduces a clinically-weighted Verifier that scores candidate outputs automatically against normative references derived from standardized volume metrics, driving Direct Preference Optimization without a single human annotation. On a subject-level held-out ADNI test set (479 scans, 258 subjects), LoV3D achieves 93.7% three-class diagnostic accuracy (+34.8% over the no-grounding baseline), 97.2% on two-class diagnosis accuracy (+4% over the SOTA) and 82.6% region-level anatomical classification accuracy (+33.1% over VLM baselines). Zero-shot transfer yields 95.4% on MIRIAD (100% Dementia recall) and 82.9% three-class accuracy on AIBL, confirming high generalizability across sites, scanners, and populations. Code is available at this https URL .

</details>

---

### 36. [A Multi-Label Temporal Convolutional Framework for Transcription Factor Binding Characterization](https://arxiv.org/abs/2603.12073)

**基本信息**

- 🔗 arXiv: [`2603.12073`](https://arxiv.org/abs/2603.12073)
- 👥 作者: Pietro Demurtas, Ferdinando Zanchetta, Giovanni Perini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12073.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于时间卷积网络的多标签分类框架，为处理序列数据（如DNA序列，可类比为分子指纹序列或谱图数据序列）中复杂的多目标预测问题提供了有效的机器学习工具和方法，可应用于“质谱结构推理”中同时预测多个结构特征的任务。

**📖 中文摘要**

本文研究了DNA转录因子结合位点识别作为一个多标签分类问题，使用基于时间卷积网络的深度学习模型，在从公共存储库检索的DNA序列上实现对多个TF的可靠预测。TCN模型能够预测多个TF结合谱，捕获TF之间的相关性及其协同调控机制。结果表明，多标签学习可以揭示具有生物学意义的 motif 和与已知TF相互作用一致的共结合模式，同时也能提示TF之间新的关系和协作。虽然研究背景是生物信息学，但其核心是应用先进的深度学习架构（TCN）解决生物分子序列中的多标签预测问题。这种方法论可以直接迁移到化学信息学的相关任务中，例如，预测一个分子结构（或其表示）与多个生物活性或谱图特征之间的复杂关联，这类似于“质谱结构推理”中从质谱数据推断分子可能具有的多个子结构或官能团。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transcription factors (TFs) regulate gene expression through complex and co-operative mechanisms. While many TFs act together, the logic underlying TFs binding and their interactions is not fully understood yet. Most current approaches for TF binding site prediction focus on individual TFs and binary classification tasks, without a full analysis of the possible interactions among various TFs. In this paper we investigate DNA TF binding site recognition as a multi-label classification problem, achieving reliable predictions for multiple TFs on DNA sequences retrieved in public repositories. Our deep learning models are based on Temporal Convolutional Networks (TCNs), which are able to predict multiple TF binding profiles, capturing correlations among TFs andtheir cooperative regulatory mechanisms. Our results suggest that multi-label learning leading to reliable predictive performances can reveal biologically meaningful motifs and co-binding patterns consistent with known TF interactions, while also suggesting novel relationships and cooperation among TFs.

</details>

---

### 37. [ChemSICal-Net: Timing-Controlled Chemical Reaction Network for Successive Interference Cancellation in Molecular Multiple Access](https://arxiv.org/abs/2603.12141)

**基本信息**

- 🔗 arXiv: [`2603.12141`](https://arxiv.org/abs/2603.12141)
- 👥 作者: Alexander Wietfeld, Oguz Turgut, Eneritz Somoza Rodríguez 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12141.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建和优化用于分子通信的化学反应网络（ChemSICal-Net）。这直接属于【化学信息学】的交叉领域，涉及用计算和模拟方法（包括贝叶斯优化）来设计和分析化学系统，是化学信息学在合成生物学/分子通信方向的应用。论文虽未直接提及“质谱”，但其对化学系统进行建模、仿真和优化的方法论与化学信息学高度相关。

**📖 中文摘要**

本文提出了ChemSICal-Net，一个用于分子通信（MC）网络中实现连续干扰消除（SIC）的化学反应网络（CRN）综合仿真模型。该模型旨在区分来自多个发射器的消息。研究将SIC算法结构以基本化学构建块的形式呈现，并通过化学振荡器结合时钟定时控制。为了找到合适的反应速率常数和初始浓度，论文提出了一种基于高斯过程代理的自适应贝叶斯优化（BO）方案，并证明其在公平计算成本度量下优于相关工作中的基线方法。随后，该框架的性能在一系列时钟速度和不同配置下进行了随机评估，重点关注检测精度和决策时间等通信系统指标。结果表明，通过化学时钟进行定时可以在决策时间较短的场景中将检测精度提高一倍，这突显了决策时间与检测概率之间的权衡如何影响CRN的设计选择。BO方案被证明能够可靠地优化不同配置的参数，与非优化情况相比大约提高一个数量级。该系统揭示了在面向通信度量的系统设计中，需要采用结合外部BO和分子反应动力学随机模拟的多尺度方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MC networks are envisioned to enable synthetic information exchange between nanoscale biological entities. For many algorithm proposals in the MC research field, the question of implementation at nanoscales and in biological environments remains open. Chemical reaction networks (CRNs) provide a natural framework to model computing processes in biological systems, while detailed simulations capture realistic stochastic effects. In this work, we present ChemSICal-Net, a comprehensive CRN simulation model of a chemical receiver implementing successive interference cancellation (SIC) to differentiate messages from multiple transmitters. We present the structure of the SIC algorithm in the form of basic chemical building blocks and incorporate clocked timing control by a chemical oscillator. We propose an adaptive Bayesian optimization (BO) scheme with a Gaussian process surrogate to find appropriate values for the reaction rate constants and the initial concentrations and show that it outperforms baseline methods from related work based on a fair computational cost metric. Then, the performance of the ChemSICal-Net framework is evaluated stochastically across a range of clock speeds and in different configurations focusing on communication system metrics such as detection accuracy and decision time. Our results highlight that the timing via a chemical clock can improve the detection accuracy by a factor of 2 in scenarios with shorter decision times, which underlines how the trade-off between decision time and detection probability can shape CRN design choices. The BO scheme is shown to reliably optimize parameters for different configurations by approximately one order of magnitude compared to the non-optimized case. Our system reveals the need for a multi-scale approach with external BO and stochastic simulation of molecular reaction dynamics for communication-metric-focused system design.

</details>

---

### 38. [Hybrid Quantum-Classical Encoding for Accurate Residue-Level pKa Prediction](https://arxiv.org/abs/2603.11061)

**基本信息**

- 🔗 arXiv: [`2603.11061`](https://arxiv.org/abs/2603.11061)
- 👥 作者: Van Le, Tan Le
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11061.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于蛋白质残基pKa预测的混合量子-经典计算框架。这直接属于【化学信息学】领域，涉及分子性质预测和计算化学模型，是化学大模型在特定分子性质预测任务上的一个具体应用和探索。

**📖 中文摘要**

本文提出了一种用于准确预测残基水平pKa值的混合量子-经典框架。该框架通过高斯核基的量子启发特征映射来丰富残基水平的表示，这些量子增强的描述符与归一化的结构特征相结合，形成统一的混合编码，并由深度量子神经网络（DQNN）进行处理。该架构能够捕获残基微环境中经典模型无法访问的非线性关系。在多个精选描述符集上的基准测试表明，相对于经典基线模型，DQNN在跨上下文泛化方面取得了改进。在PKAD-R实验基准和Aβ40案例研究上的外部评估进一步突显了量子启发表示的鲁棒性和可迁移性。这项工作通过将量子启发的特征变换与经典生化描述符相结合，为残基水平pKa预测及蛋白质静电学的更广泛应用建立了一种可扩展且具有实验可迁移性的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of residue-level pKa values is essential for understanding protein function, stability, and reactivity. While existing resources such as DeepKaDB and CpHMD-derived datasets provide valuable training data, their descriptors remain primarily classical and often struggle to generalize across diverse biochemical environments. We introduce a reproducible hybrid quantum-classical framework that enriches residue-level representations with a Gaussian kernel-based quantum-inspired feature mapping. These quantum-enhanced descriptors are combined with normalized structural features to form a unified hybrid encoding processed by a Deep Quantum Neural Network (DQNN). This architecture captures nonlinear relationships in residue microenvironments that are not accessible to classical models. Benchmarking across multiple curated descriptor sets demonstrates that the DQNN achieves improved cross-context generalization relative to classical baselines. External evaluation on the PKAD-R experimental benchmark and an A$\beta$40 case study further highlights the robustness and transferability of the quantum-inspired representation. By integrating quantum-inspired feature transformations with classical biochemical descriptors, this work establishes a scalable and experimentally transferable approach for residue-level pKa prediction and broader applications in protein electrostatics.

</details>

---

### 39. [From Phase Prediction to Phase Design: A ReAct Agent Framework for High-Entropy Alloy Discovery](https://arxiv.org/abs/2603.11068)

**基本信息**

- 🔗 arXiv: [`2603.11068`](https://arxiv.org/abs/2603.11068)
- 👥 作者: Iman Peivaste, Salim Belouettar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11068.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型（LLM）的智能体框架，用于高熵合金的逆向设计和发现。这直接属于【化学信息学】领域，是利用“化学大模型”（此处体现为LLM智能体与机器学习代理模型的结合）进行材料发现和设计的典型应用。

**📖 中文摘要**

本文提出了一种ReAct（推理+行动）大语言模型（LLM）智能体框架，用于高熵合金（HEA）的发现和设计。该智能体能够自主提出、验证并迭代优化HEA成分，以可靠地形成目标晶体相。它通过查询一个基于4753个实验记录（涵盖FCC、BCC、BCC+FCC、BCC+IM四种相）训练并校准的XGBoost代理模型来运作。该框架将发现目标相HEA成分这一高维逆向设计问题，转化为由智能体驱动的、结合领域先验知识的迭代探索过程。研究表明，与贝叶斯优化和随机搜索基线相比，该智能体在描述符空间中对FCC、BCC和BCC+FCC相的“重新发现率”显著更高，并且其提出的成分更接近实验相流形。这项工作确立了LLM引导的智能体推理作为逆向合金设计中一种有原则、透明且能感知流形结构的、对无梯度优化的补充方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering high-entropy alloy (HEA) compositions that reliably form a target crystal phase is a high-dimensional inverse design problem that conventional trial-and-error experimentation and forward-only machine learning models cannot efficiently solve. Here we present a ReAct (Reasoning + Acting) LLM agent that autonomously proposes, validates, and iteratively refines HEA compositions by querying a calibrated XGBoost surrogate trained on 4,753 experimental records across four phases (FCC, BCC, BCC+FCC, BCC+IM), achieving 94.66\% accuracy (F1 macro = 0.896). Against Bayesian optimisation (BO) and random search baselines, the full-prompt agent achieves descriptor-space rediscovery rates of 38\%, 18\%, and 38\% for FCC, BCC, and BCC+FCC (Mann--Whitney $p \leq 0.039$), with proposals lying 2.4--22.8$\times$ closer to the experimental phase manifold than random search. An ablation reveals that domain priors shift the agent from landmark-alloy recall toward compositionally diverse exploration -- an uninformed agent scores higher rediscovery by concentrating on literature-dense families, while the full-prompt agent explores underrepresented space (unique ratio 1.0 vs.\ 0.39 for BCC+FCC). These regimes represent distinct criteria: proximity to known literature versus genuine discovery. Spearman analysis confirms agent reasoning is statistically aligned with empirical phase distributions ($\rho = 0.736$, $p = 0.004$ for BCC). This work establishes LLM-guided agentic reasoning as a principled, transparent, and manifold-aware complement to gradient-free optimisation for inverse alloy design.

</details>

---

### 40. [Co-Diffusion: An Affinity-Aware Two-Stage Latent Diffusion Framework for Generalizable Drug-Target Affinity Prediction](https://arxiv.org/abs/2603.11125)

**基本信息**

- 🔗 arXiv: [`2603.11125`](https://arxiv.org/abs/2603.11125)
- 👥 作者: Yining Qian, Pengjie Wang, Yixiao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11125.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的新型深度学习框架（Co-Diffusion）用于药物-靶标亲和力预测。这直接属于【化学信息学】的核心领域，即计算机辅助药物设计。该工作利用先进的生成模型（扩散模型）来解决化学信息学中的关键预测问题，是“化学大模型”在分子性质预测方向上的一个前沿探索。

**📖 中文摘要**

本文提出了Co-Diffusion，一种新颖的亲和力感知框架，用于可泛化的药物-靶标亲和力（DTA）预测。该框架将DTA预测重新定义为受约束的潜在去噪过程以增强泛化能力。Co-Diffusion采用两阶段范式：第一阶段在显式监督目标下对齐药物和靶标嵌入，建立由亲和力引导的潜在流形，确保潜在空间反映内在的结合景观；第二阶段引入模态特定的潜在扩散作为随机扰动-去噪正则化器，迫使模型从噪声结构表示中恢复一致的亲和力语义。这种方法有效缓解了生成式DTA模型中常见的重建-回归冲突。理论分析表明，Co-Diffusion最大化了药物结构、蛋白质序列和结合强度的联合似然变分下界。跨多个基准的广泛实验证明，Co-Diffusion显著优于最先进的基线模型，特别是在未见过的分子支架和新蛋白质家族上表现出卓越的零样本泛化能力，为在未探索化学空间中进行计算机药物优先排序铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting drug-target affinity is fundamental to virtual screening and lead optimization. However, existing deep models often suffer from representation collapse in stringent cold-start regimes, where the scarcity of labels and domain shifts prevent the learning of transferable pharmacophores and binding motifs. In this paper, we propose Co-Diffusion, a novel affinity-aware framework that redefines DTA prediction as a constrained latent denoising process to enhance generalization. Co-Diffusion employs a two-stage paradigm: Stage I establishes an affinity-steered latent manifold by aligning drug and target embeddings under an explicit supervised objective, ensuring that the latent space reflects the intrinsic binding landscape. Stage II introduces modality-specific latent diffusion as a stochastic perturb-and-denoise regularizer, forcing the model to recover consistent affinity semantics from noisy structural representations. This approach effectively mitigates the reconstruction-regression conflict common in generative DTA models. Theoretically, we show that Co-Diffusion maximizes a variational lower bound on the joint likelihood of drug structures, protein sequences, and binding strength. Extensive experiments across multiple benchmarks demonstrate that Co-Diffusion significantly outperforms state-of-the-art baselines, particularly yielding superior zero-shot generalization on unseen molecular scaffolds and novel protein families-paving a robust path for in silico drug prioritization in unexplored chemical spaces.

</details>

---

### 41. [A Unified Latent Space Disentanglement VAE Framework with Robust Disentanglement Effectiveness Evaluation](https://arxiv.org/abs/2603.11242)

**基本信息**

- 🔗 arXiv: [`2603.11242`](https://arxiv.org/abs/2603.11242)
- 👥 作者: Xiaoan Lang, Fang Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11242.pdf)

**💡 相关性分析**

满足标准2：提出的bfVAE框架和评估工具（FVH-LT, DBSR-LS, LSDI）为构建和评估生成模型（如化学大模型）的潜在空间提供了通用的数据资源和工具，这对于化学信息学中的分子表示学习至关重要。

**📖 中文摘要**

本文提出了一个统一的变分自编码器（VAE）框架bfVAE，用于生成有效的潜在空间解耦，特别适用于表格数据。为了评估VAE解耦技术的有效性，作者提出了两种无需真实生成因子知识的评估程序（FVH-LT和DBSR-LS）以及一个总体解耦指数（LSDI）。该框架旨在解决评估和解释潜在表示（如VAE）的挑战，尤其是在真实生成因子未知的情况下。这项工作与化学信息学中开发用于分子表示和性质预测的生成模型高度相关。bfVAE框架及其评估工具为构建和验证用于化学结构（如质谱数据）的生成模型提供了方法论基础，这些模型需要可解释和可控的潜在空间来进行下游推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evaluating and interpreting latent representations, such as variational autoencoders (VAEs), remains a significant challenge for diverse data types, especially when ground-truth generative factors are unknown. To address this, we propose a general framework -- bfVAE -- that unifies several state-of-the-art disentangled VAE approaches and generates effective latent space disentanglement, especially for tabular data. To assess the effectiveness of a VAE disentanglement technique, we propose two procedures - Feature Variance Heterogeneity via Latent Traversal (FVH-LT) and Dirty Block Sparse Regression in Latent Space (DBSR-LS) for disentanglement assessment, along with the latent space disentanglement index (LSDI) which uses the outputs of FVH-LT and DBSR-LS to summarize the overall effectiveness of a VAE disentanglement method without requiring access to or knowledge of the ground-truth generative factors. To the best of our knowledge, these are the first assessment tools to achieve this. FVH-LT and DBSR-LS also enhance latent space interpretability and provide guidance on more efficient content generation. To ensure robust and consistent disentanglement, we develop a greedy alignment strategy (GAS) that mitigates label switching and aligns latent dimensions across runs to obtain aggregated results. We assess the bfVAE framework and validate FVH-LT, DBSR-LS, and LSDI in extensive experiments on tabular and image data. The results suggest that bfVAE surpasses existing disentangled VAE frameworks in terms of disentanglement quality, robustness, achieving a near-zero false discovery rate for informative latent dimensions, that FVH-LT and DBSR-LS reliably uncover semantically meaningful and domain-relevant latent structures, and that LSDI makes an effective overall quantitative summary on disentanglement effectiveness.

</details>

---

### 42. [A Standardized Framework For Evaluating Gene Expression Generative Models](https://arxiv.org/abs/2603.11244)

**基本信息**

- 🔗 arXiv: [`2603.11244`](https://arxiv.org/abs/2603.11244)
- 👥 作者: Andrea Rubbi, Andrea Giuseppe Di Francesco, Mohammad Lotfollahi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11244.pdf)

**💡 相关性分析**

满足标准2：提出的GGE框架是一个用于标准化评估生成模型的工具和资源。虽然应用于生物信息学，但其解决生成模型评估标准化问题的核心思想和方法可直接迁移或启发化学大模型的评估框架构建。

**📖 中文摘要**

本文提出了Generated Genetic Expression Evaluator (GGE)，一个用于评估单细胞基因表达生成模型的开源Python框架。GGE通过提供一套全面的分布度量（包含明确的计算空间选项）和基于生物学动机的评估（如差异表达基因分析和扰动效应相关性），解决了当前评估实践中指标实现不一致、超参数选择不可比以及缺乏生物学基础度量的问题。该框架旨在实现标准化报告和可复现的基准测试。这项工作虽然聚焦于基因表达数据，但其核心是解决生成模型评估的标准化和可复现性这一普遍挑战。这对于评估化学领域的大模型（如用于分子生成或性质预测的模型）具有直接的借鉴意义，因为化学信息学同样面临模型评估标准不统一的问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid development of generative models for single-cell gene expression data has created an urgent need for standardised evaluation frameworks. Current evaluation practices suffer from inconsistent metric implementations, incomparable hyperparameter choices, and a lack of biologically-grounded metrics. We present Generated Genetic Expression Evaluator (GGE), an open-source Python framework that addresses these challenges by providing a comprehensive suite of distributional metrics with explicit computation space options and biologically-motivated evaluation through differentially expressed gene (DEG)-focused analysis and perturbation-effect correlation, enabling standardized reporting and reproducible benchmarking. Through extensive analysis of the single-cell generative modeling literature, we identify that no standardized evaluation protocol exists. Methods report incomparable metrics computed in different spaces with different hyperparameters. We demonstrate that metric values vary substantially depending on implementation choices, highlighting the critical need for standardization. GGE enables fair comparison across generative approaches and accelerates progress in perturbation response prediction, cellular identity modeling, and counterfactual inference.

</details>

---

### 43. [ELISA: An Interpretable Hybrid Generative AI Agent for Expression-Grounded Discovery in Single-Cell Genomics](https://arxiv.org/abs/2603.11872)

**基本信息**

- 🔗 arXiv: [`2603.11872`](https://arxiv.org/abs/2603.11872)
- 👥 作者: Omar Coser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11872.pdf)

**💡 相关性分析**

满足标准1：ELISA框架的核心是整合预训练的生成模型（scGPT）和大语言模型（LLM）来进行数据分析和假设生成。这直接体现了“化学大模型”在跨模态（这里是从基因表达到自然语言）科学发现任务中的应用范式，与利用大模型进行化学数据分析和推理的研究主题高度相关。

**📖 中文摘要**

本文介绍了ELISA（Embedding-Linked Interactive Single-cell Agent），一个将scGPT表达嵌入与基于BioBERT的语义检索以及LLM介导的解释相统一的、用于交互式单细胞发现的可解释框架。ELISA包含一个自动查询分类器，根据输入是基因特征、自然语言概念还是两者的混合，将查询路由到不同的分析管道（如基因标记评分、语义匹配、互逆排序融合）。集成的分析模块可以直接在嵌入数据上执行通路活性评分、配体-受体相互作用预测、条件感知比较分析和细胞类型比例估计，而无需访问原始计数矩阵。该框架在六个不同的scRNA-seq数据集上进行了基准测试，在细胞类型检索方面显著优于基线模型。ELISA通过基于LLM的推理生成候选假设，弥合了转录组数据探索与生物学发现之间的差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Translating single-cell RNA sequencing (scRNA-seq) data into mechanistic biological hypotheses remains a critical bottleneck, as agentic AI systems lack direct access to transcriptomic representations while expression foundation models remain opaque to natural language. Here we introduce ELISA (Embedding-Linked Interactive Single-cell Agent), an interpretable framework that unifies scGPT expression embeddings with BioBERT-based semantic retrieval and LLM-mediated interpretation for interactive single-cell discovery. An automatic query classifier routes inputs to gene marker scoring, semantic matching, or reciprocal rank fusion pipelines depending on whether the query is a gene signature, natural language concept, or mixture of both. Integrated analytical modules perform pathway activity scoringacross 60+ gene sets, ligand--receptor interaction prediction using 280+ curated pairs, condition-aware comparative analysis, and cell-type proportion estimation all operating directly on embedded data without access to the original count matrix. Benchmarked across six diverse scRNA-seq datasets spanning inflammatory lung disease, pediatric and adult cancers, organoid models, healthy tissue, and neurodevelopment, ELISA significantly outperforms CellWhisperer in cell type retrieval (combined permutation test, $p < 0.001$), with particularly large gains on gene-signature queries (Cohen's $d = 5.98$ for MRR). ELISA replicates published biological findings (mean composite score 0.90) with near-perfect pathway alignment and theme coverage (0.98 each), and generates candidate hypotheses through grounded LLM reasoning, bridging the gap between transcriptomic data exploration and biological discovery. Code available at: this https URL (If you use ELISA in your research, please cite this work).

</details>

---

### 44. [Proof-Carrying Materials: Falsifiable Safety Certificates for Machine-Learned Interatomic Potentials](https://arxiv.org/abs/2603.12183)

**基本信息**

- 🔗 arXiv: [`2603.12183`](https://arxiv.org/abs/2603.12183)
- 👥 作者: Abhinaba Basu, Pavan Chakraborty
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.12183.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是评估和提升用于材料科学（化学的一个核心分支）的机器学习模型（MLIPs）的可靠性。MLIPs是化学领域特定的大模型，论文提出的PCM框架旨在为这些模型提供安全保证，直接围绕“化学大模型”的可靠性和应用主题。

**📖 中文摘要**

本文提出了Proof-Carrying Materials (PCM)，一个为机器学习原子间势（MLIPs）提供可证伪安全证书的框架。PCM通过三个阶段工作：跨组成空间的对抗性证伪、具有95%置信区间的自举包络细化，以及Lean 4形式化验证。作者审计了CHGNet、TensorNet和MACE等MLIP，揭示了架构特定的盲点，并通过独立的Quantum ESPRESSO计算验证了这些发现。此外，他们还训练了一个基于PCM发现特征的风险模型，用于预测未见材料上的失败。在一个热电筛选案例研究中，经过PCM审计的方案发现了62个额外的稳定材料，这些材料被单一MLIP筛选所遗漏。这项工作直接针对用于材料发现的机器学习模型的可靠性和安全性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learned interatomic potentials (MLIPs) are deployed for high-throughput materials screening without formal reliability guarantees. We show that a single MLIP used as a stability filter misses 93% of density functional theory (DFT)-stable materials (recall 0.07) on a 25,000-material benchmark. Proof-Carrying Materials (PCM) closes this gap through three stages: adversarial falsification across compositional space, bootstrap envelope refinement with 95% confidence intervals, and Lean 4 formal certification. Auditing CHGNet, TensorNet and MACE reveals architecture-specific blind spots with near-zero pairwise error correlations (r <= 0.13; n = 5,000), confirmed by independent Quantum ESPRESSO validation (20/20 converged; median DFT/CHGNet force ratio 12x). A risk model trained on PCM-discovered features predicts failures on unseen materials (AUC-ROC = 0.938 +/- 0.004) and transfers across architectures (cross-MLIP AUC-ROC ~ 0.70; feature importance r = 0.877). In a thermoelectric screening case study, PCM-audited protocols discover 62 additional stable materials missed by single-MLIP screening - a 25% improvement in discovery yield.

</details>

---

### 45. [Using LLM-Generated Draft Replies to Support Human Experts in Responding to Stakeholder Inquiries in Maritime Industry: A Real-World Case Study of Industrial AI](https://arxiv.org/abs/2412.12732)

**基本信息**

- 🔗 arXiv: [`2412.12732`](https://arxiv.org/abs/2412.12732)
- 👥 作者: Tita Alissa Bach, Aleksandar Babic, Narae Park 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.12732.pdf)

**💡 相关性分析**

满足标准1：论文是一项关于大语言模型（LLM）在专业工业领域（海事）中实际应用的研究。虽然领域不同，但其探索LLM如何辅助领域专家处理专业沟通和决策的核心主题，与探索“化学大模型”如何辅助化学家进行研究、文献分析或报告撰写等任务的研究方向直接相关，属于大模型在垂直领域应用的典型案例。

**📖 中文摘要**

本文是一项关于在航海工业中利用LLM生成草稿回复以支持人类专家响应利益相关者询问的真实案例研究。研究通过初步研究（观察和访谈）、调查和文本相似性分析，探讨了LLM在起草回复和辅助案件处理人员方面的效用。研究发现，虽然LLM草稿可以简化工作流程，但通常需要大量修改才能满足海事通信的特定需求。尽管LLM在没有人工监督的情况下尚未成熟到可用于安全关键应用，但它们可以作为有价值的增强工具。最终决策权必须保留在人类专家手中。这项研究展示了工业AI（特别是LLM）在专业领域（如海事，可类比于化学）中作为人类助手的工作流程增强潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The maritime industry requires effective communication among diverse stakeholders to address complex, safety-critical challenges. Industrial AI, including Large Language Models (LLMs), has the potential to augment human experts' workflows in this specialized domain. Our case study investigated the utility of LLMs in drafting replies to stakeholder inquiries and supporting case handlers. We conducted a preliminary study (observations and interviews), a survey, and a text similarity analysis (LLM-as-a-judge and Semantic Embedding Similarity). We discover that while LLM drafts can streamline workflows, they often require significant modifications to meet the specific demands of maritime communications. Though LLMs are not yet mature enough for safety-critical applications without human oversight, they can serve as valuable augmentative tools. Final decision-making thus must remain with human experts. However, by leveraging the strengths of both humans and LLMs, fostering human-AI collaboration, industries can increase efficiency while maintaining high standards of quality and precision tailored to each case.

</details>

---

### 46. [Audio-Language Models for Audio-Centric Tasks: A Systematic Survey](https://arxiv.org/abs/2501.15177)

**基本信息**

- 🔗 arXiv: [`2501.15177`](https://arxiv.org/abs/2501.15177)
- 👥 作者: Yi Su, Jisheng Bai, Qisheng Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.15177.pdf)

**💡 相关性分析**

满足标准3：论文是关于音频-语言模型（一种特定领域的多模态大模型）的专门综述。它系统性地总结了该领域的技术基础、发展现状和未来趋势。这种针对垂直领域大模型的综述工作，其方法论和洞察对于开展“化学大模型”或“质谱-语言模型”相关的综述与展望研究具有直接的借鉴和参考价值。

**📖 中文摘要**

本文对音频-语言模型（ALMs）进行了首次系统性综述。ALMs在配对音频-文本数据上训练，旨在处理、理解和推理以音频为中心的多模态内容。与使用预定义标签的传统监督方法不同，ALMs利用自然语言监督来更好地处理具有多个重叠事件的复杂真实世界音频场景。综述涵盖了语音、音乐和声音领域的ALM工作，提供了统一的ALM基础分类法（包括模型架构和训练目标），并建立了一个捕捉不同研究方面相互促进和制约的研究图景。这项工作虽然聚焦音频，但其系统性地梳理了基于自然语言监督的多模态大模型（ALMs）的发展，其模型架构、训练范式、评估和挑战的讨论，对于理解和构建化学领域的多模态大模型（如整合质谱图、分子结构和文本描述）具有重要的参考价值和前瞻性指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Audio-Language Models (ALMs), trained on paired audio-text data, are designed to process, understand, and reason about audio-centric multimodal content. Unlike traditional supervised approaches that use predefined labels, ALMs leverage natural language supervision to better handle complex real-world audio scenes with multiple overlapping events. While demonstrating impressive zero-shot and task generalization capabilities, there is still a notable lack of systematic surveys that comprehensively organize and analyze developments. In this paper, we present the first systematic review of ALMs with three main contributions: (1) comprehensive coverage of ALM works across speech, music, and sound from a general audio perspective; (2) a unified taxonomy of ALM foundations, including model architectures and training objectives; (3) establishment of a research landscape capturing mutual promotion and constraints among different research aspects, aiding in summarizing evaluations, limitations, concerns and promising directions. Our review contributes to helping researchers understand the development of existing technologies and future trends, while also providing valuable references for implementation in practical applications.

</details>

---

### 47. [Tuning-Free LLM Can Build A Strong Recommender Under Sparse Connectivity And Knowledge Gap Via Extracting Intent](https://arxiv.org/abs/2505.10900)

**基本信息**

- 🔗 arXiv: [`2505.10900`](https://arxiv.org/abs/2505.10900)
- 👥 作者: Wenqing Zheng, Noah Fatsi, Daniel Barcklow 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10900.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用大语言模型（LLM）从非结构化文本（用户资料、物品描述）中提取结构化语义信息（意图），并将其用于构建增强的知识图谱以改进下游任务（推荐）。这种利用LLM进行信息提取和结构化以辅助复杂推理（如推荐）的模式，与利用“化学大模型”从科学文献、实验报告中提取化学实体、反应关系或谱图解释，以辅助“质谱结构推理”等任务的研究思路高度吻合。

**📖 中文摘要**

本文提出了LLM-based Intent Knowledge Graph Recommender (IKGR)，一个新颖的推荐框架。IKGR构建了一个以意图为中心的知识图谱，其中用户和物品都通过一个无需微调、由RAG引导的LLM流程提取的意图节点明确连接。通过将意图锚定在外部知识源和用户画像中，IKGR规范地表示了用户寻求什么以及物品满足什么作为一等实体。为了缓解稀疏性，作者进一步引入了互意图连接致密化策略。最后，在意图增强的图谱上使用轻量级GNN层来生成低延迟的推荐信号。该框架的核心创新在于利用LLM从文本中提取结构化意图，并以此构建增强的知识图谱。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in recommendation with large language models (LLMs) often rely on either commonsense augmentation at the item-category level or implicit intent modeling on existing knowledge graphs. However, such approaches struggle to capture grounded user intents and to handle sparsity and cold-start scenarios. In this work, we present LLM-based Intent Knowledge Graph Recommender (IKGR), a novel framework that constructs an intent-centric knowledge graph where both users and items are explicitly linked to intent nodes extracted by a tuning-free, RAG-guided LLM pipeline. By grounding intents in external knowledge sources and user profiles, IKGR canonically represents what a user seeks and what an item satisfies as first-class entities. To alleviate sparsity, we further introduce a mutual-intent connectivity densification strategy, which shortens semantic paths between users and long-tail items without requiring cross-graph fusion. Finally, a lightweight GNN layer is employed on top of the intent-enhanced graph to produce recommendation signals with low latency. Extensive experiments on public and enterprise datasets demonstrate that IKGR consistently outperforms strong baselines, particularly on cold-start and long-tail slices, while remaining efficient through a fully offline LLM pipeline.

</details>

---

### 48. [LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models](https://arxiv.org/abs/2505.19240)

**基本信息**

- 🔗 arXiv: [`2505.19240`](https://arxiv.org/abs/2505.19240)
- 👥 作者: Aida Kostikova, Zhipin Wang, Deidamea Bajri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19240.pdf)

**💡 相关性分析**

满足标准3：这是一篇针对大型语言模型（LLM）的综述性论文。由于化学大模型是LLM在化学领域的应用，这篇论文对LLM整体研究趋势、局限性和热点的分析，为理解和评估化学大模型的潜力和挑战提供了重要的宏观背景和前瞻性讨论。

**📖 中文摘要**

这篇论文对大型语言模型（LLM）的局限性研究进行了数据驱动的综述。它通过半自动化的方法，从2022年至2025年初的大量ACL和arXiv论文中识别出14,648篇相关论文，并分析了研究趋势。研究发现，关于LLM局限性的研究增长迅速，到2025年已占LLM相关论文的30%以上。研究的局限性主题包括推理、泛化、幻觉、偏见和安全性等。论文还发布了一个带注释的摘要数据集和经过验证的方法论。虽然论文主题是LLM的局限性，但其核心是**化学信息学**和**质谱分析**领域所依赖的**化学大模型**的基础研究。它系统地梳理了该领域模型（即LLM）的研究现状、挑战和趋势，为相关领域的研究者提供了重要的背景和未来方向的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains the most studied limitation, followed by generalization, hallucination, bias, and security. The distribution of topics in the ACL dataset stays relatively stable over time, while arXiv shifts toward security risks, alignment, hallucinations, knowledge editing, and multimodality. We offer a quantitative view of trends in LLLMs research and release a dataset of annotated abstracts and a validated methodology, available at: this https URL .

</details>

---

### 49. [Text-Trained LLMs Can Zero-Shot Extrapolate PDE Dynamics, Revealing a Three-Stage In-Context Learning Mechanism](https://arxiv.org/abs/2509.06322)

**基本信息**

- 🔗 arXiv: [`2509.06322`](https://arxiv.org/abs/2509.06322)
- 👥 作者: Jiajun Bao, Nicolas Boullé, Toni J.B. Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.06322.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索大型语言模型（作为大模型的一种）在科学计算（PDE动力学外推）中的零样本推理能力。这直接证明了化学等领域的大模型在理解和模拟复杂物理化学过程方面的潜力，与“化学大模型”主题高度相关。

**📖 中文摘要**

这篇论文展示了仅通过文本训练的大型语言模型（LLM）能够零样本外推偏微分方程（PDE）的时空动力学。研究揭示了LLM在上下文中学习（ICL）PDE解并递归预测未来状态的能力，其预测误差随预测步长呈代数增长，类似于经典有限差分求解器中的全局误差累积。作者将这种趋势解释为上下文神经缩放定律，并分析了LLM内部处理PDE解以进行准确推演的三阶段ICL进程。这项研究证明了**化学大模型**（作为LLM的一个子类）在处理复杂科学计算和模拟（如分子动力学、化学反应模拟等）方面具有潜在能力。它直接关联到使用大模型进行科学推理和计算这一核心主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated emergent in-context learning (ICL) capabilities across a range of tasks, including zero-shot time-series forecasting. We show that text-trained foundation models can accurately extrapolate spatiotemporal dynamics from discretized partial differential equation (PDE) solutions without fine-tuning or natural language prompting. Predictive accuracy improves with longer temporal contexts but degrades at finer spatial discretizations. In multi-step rollouts, where the model recursively predicts future spatial states over multiple time steps, errors grow algebraically with the time horizon, reminiscent of global error accumulation in classical finite-difference solvers. We interpret these trends as in-context neural scaling laws, where prediction quality varies predictably with both context length and output length. To better understand how LLMs are able to internally process PDE solutions so as to accurately roll them out, we analyze token-level output distributions and uncover a consistent three-stage ICL progression: beginning with syntactic pattern imitation, transitioning through an exploratory high-entropy phase, and culminating in confident, numerically grounded predictions.

</details>

---

### 50. [From Next Token Prediction to (STRIPS) World Models](https://arxiv.org/abs/2509.13389)

**基本信息**

- 🔗 arXiv: [`2509.13389`](https://arxiv.org/abs/2509.13389)
- 👥 作者: Carlos Núñez-Molina, Vicenç Gómez, Hector Geffner
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.13389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索基于Transformer的大模型如何从数据中学习结构化的世界模型并支持规划。这为构建能够进行化学合成规划、反应推理或结构解析的化学领域大模型提供了理论基础和方法论参考。

**📖 中文摘要**

这篇论文研究下一个词预测（Next-token prediction）是否能够产生真正支持规划的世界模型。研究在一个受控的符号设置（命题STRIPS动作模型）中进行，模型仅从动作轨迹中学习。论文引入了两种架构：一种是具有明确符号归纳偏置的STRIPS Transformer，另一种是标准的Transformer架构。评估表明，这两种方法都可以用于生成支持在指数级未见初始状态和目标上进行规划的模型。这项研究探讨了**大模型**（特别是Transformer架构）从序列数据中学习结构化世界模型和规划能力的基本原理。这对于开发能够进行分子合成规划、反应路径推理或质谱解析逆合成分析的**化学大模型**具有重要的启示意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study whether next-token prediction can yield world models that truly support planning, in a controlled symbolic setting where propositional STRIPS action models are learned from action traces alone and correctness can be evaluated exactly. We introduce two architectures. The first is the STRIPS Transformer, a symbolically aligned model grounded in theoretical results linking transformers and the formal language structure of STRIPS domains. The second is a standard transformer architecture without explicit symbolic structure built in, for which we study different positional encoding schemes and attention aggregation mechanisms. We evaluate both architectures on five classical planning domains, measuring training accuracy, generalization, and planning performance across domains and problem sizes. Interestingly, both approaches can be used to produce models that support planning with off-the-shelf STRIPS planners over exponentially many unseen initial states and goals. Although the STRIPS Transformer incorporates a strong symbolic inductive bias, it is harder to optimize and requires larger datasets to generalize reliably. In contrast, a standard transformer with stick-breaking attention achieves near-perfect training accuracy and strong generalization. Finally, standard transformers without stick-breaking attention do not generalize to long traces, whereas a symbolic STRIPS model extracted from a transformer trained on shorter traces does.

</details>

---

### 51. [Streamline pathology foundation model by cross-magnification distillation](https://arxiv.org/abs/2509.23097)

**基本信息**

- 🔗 arXiv: [`2509.23097`](https://arxiv.org/abs/2509.23097)
- 👥 作者: Ziyu Su, Abdul Rehman Akbar, Usama Sajjad 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.23097.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种通过跨分辨率蒸馏构建轻量级领域基础模型（XMAG）的方法论和框架。这为化学和质谱领域的研究者提供了如何构建和优化专用大模型（如用于光谱解析或分子生成的模型）的重要技术思路和工具参考。

**📖 中文摘要**

这篇论文提出了XMAG，一个通过跨放大倍数蒸馏开发的轻量级病理学基础模型。它将知识从最先进的20倍放大倍数教师模型转移到一个高效的5倍放大倍数学生架构中。XMAG采用紧凑的主干网络，完全在5倍放大倍数下运行，与现有方法相比，每张全切片图像所需的图块数量减少了11.3倍。该框架结合了双层次知识转移，对齐全局图像表示和局部空间令牌映射。这项研究展示了如何通过**模型蒸馏和架构设计**来构建更高效、可部署的领域专用大模型（这里是病理学）。其方法论（跨模态/分辨率的知识蒸馏、轻量化设计）对于在**化学信息学**和**质谱分析**领域开发资源高效的专用大模型（例如，用于光谱预测或分子性质估算的轻量级模型）具有直接的借鉴价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models (FM) have transformed computational pathology but remain computationally prohibitive for clinical deployment due to their massive parameter counts and high-magnification processing requirements. Here, we introduce XMAG, a lightweight FM developed through corss-magnification distillation that transfers knowledge from state-of-the-art 20x magnification teacher to an efficient 5x magnification student architecture. XMAG employs a compact backbone and operates entirely at 5x, requiring 11.3 times fewer patches per whole slide image (WSI) compared to existing approaches. Our Novel distillation framework incorporates dual-level knowledge transfer, aligning both global image representations and local spatial token mapping. We trained XMAG on 3.49 million images curated from publicly available datasets and evaluated performance across six clinically relevant histopathology analysis tasks spanning multiple cancer types. XMAG achieved diagnostic accuracy within 1% of substantially larger foundation models while delivering 30-fold processing acceleration, reaching 8.8 WSIs per minute processing speed. Our cross-institutional validation confirmed robust generalization. Further, we developed an end-to-end training strategy to further boost our model's performance to approach the larger FMs' performance. These results establish cross-magnification distillation as a viable approach for deploying FM capabilities in resource-constrained clinical environments, potentially enabling real-time pathology AI integration.

</details>

---

### 52. [Busemann Functions in the Wasserstein Space: Existence, Closed-Forms, and Applications to Slicing](https://arxiv.org/abs/2510.04579)

**基本信息**

- 🔗 arXiv: [`2510.04579`](https://arxiv.org/abs/2510.04579)
- 👥 作者: Clément Bonet, Elsa Cazelles, Lucas Drumetz 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04579.pdf)

**💡 相关性分析**

满足标准2：论文提出了用于概率分布几何处理的新数学框架和算法（Busemann函数在Wasserstein空间的应用，以及新的切片距离方案）。这些高级数学工具和算法可以直接应用于化学和质谱领域，用于处理分子嵌入空间的距离计算、光谱数据的度量学习或分布对齐，为相关主题提供了潜在的数据处理资源和方法。

**📖 中文摘要**

这篇论文研究了Wasserstein空间中的Busemann函数，该函数最近在几何机器学习问题中引起了广泛兴趣，因为它自然地定义了黎曼流形上测地线的投影。由于许多数据源可以方便地建模为概率分布，因此在由最优传输度量诱导的具有丰富形式黎曼结构的Wasserstein空间中研究此函数是很自然的。作者建立了两个重要情况下的闭式表达式：一维分布和高斯测度。这些结果使得在ℝ上的概率分布有了明确的投影方案，进而允许定义高斯混合和标记数据集上新的切片Wasserstein距离。这项研究涉及**概率分布的表征、距离度量和高维数据的几何处理**。这些数学工具和框架是**化学信息学**中处理分子分布、不确定性量化以及**质谱分析**中处理复杂光谱数据降维和比较的核心。论文提供的新方案（如用于高斯混合的切片距离）可作为相关领域的新工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Busemann function has recently found much interest in a variety of geometric machine learning problems, as it naturally defines projections onto geodesic rays of Riemannian manifolds and generalizes the notion of hyperplanes. As several sources of data can be conveniently modeled as probability distributions, it is natural to study this function in the Wasserstein space, which carries a rich formal Riemannian structure induced by Optimal Transport metrics. In this work, we investigate the existence and computation of Busemann functions in Wasserstein space, which admits geodesic rays. We establish closed-form expressions in two important cases: one-dimensional distributions and Gaussian measures. These results enable explicit projection schemes for probability distributions on $\mathbb{R}$, which in turn allow us to define novel Sliced-Wasserstein distances over Gaussian mixtures and labeled datasets. We demonstrate the efficiency of those original schemes on synthetic datasets as well as transfer learning problems.

</details>

---

### 53. [Jr. AI Scientist and Its Risk Report: Autonomous Scientific Exploration from a Baseline Paper](https://arxiv.org/abs/2511.04583)

**基本信息**

- 🔗 arXiv: [`2511.04583`](https://arxiv.org/abs/2511.04583)
- 👥 作者: Atsuyuki Miyai, Mashiro Toyooka, Takashi Otonari 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.04583.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是构建和评估一个自主AI科学家系统（Jr. AI Scientist），这直接关联到使用大模型进行自动化科学研究这一主题，是化学大模型应用的终极愿景之一。同时，论文也包含了对这类系统当前能力、局限性和风险的深入讨论，具有综述和展望的性质。

**📖 中文摘要**

这篇论文介绍了Jr. AI Scientist，一个最先进的自主AI科学家系统，它模拟了新手学生研究人员的核心研究工作流程：在给定人类导师的基线论文后，系统分析其局限性，提出改进的新假设，迭代实验直到取得改进，并撰写结果论文。论文通过实验评估了该系统在真实NeurIPS、IJCV和ICLR工作基础上生成新研究论文的能力。这项研究探索了**大模型驱动自主科学发现**的当前能力和风险。虽然其应用场景是通用AI科学家，但其核心框架——分析文献、提出假设、设计实验、撰写论文——完全适用于**化学信息学**和**质谱分析**领域的自动化研究。它展示了构建领域专用AI研究助手（即“化学AI科学家”）的可行性和潜在范式，与“化学大模型”作为自动化研究工具的主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding the current capabilities and risks of AI Scientist systems (autoresearch) is essential for ensuring trustworthy and sustainable AI-driven scientific progress while preserving the integrity of the academic ecosystem. To this end, we develop Jr. AI Scientist, a state-of-the-art autonomous AI scientist system that mimics the core research workflow of a novice student researcher: Given the baseline paper from the human mentor, it analyzes its limitations, formulates novel hypotheses for improvement, iteratively experiments until improvements are achieved, and writes a paper with the results. Unlike previous approaches that assume full automation or operate on small-scale code, Jr. AI Scientist follows a well-defined research workflow and leverages modern coding agents to handle complex, multi-file implementations, leading to scientifically valuable contributions. Through our experiments, the Jr. AI Scientist successfully generated new research papers that build upon real NeurIPS, IJCV, and ICLR works by proposing and implementing novel methods. For evaluation, we conducted automated assessments using AI Reviewers, author-led evaluations, and submissions to Agents4Science, a venue dedicated to AI-driven contributions. The findings demonstrate that Jr. AI Scientist generates papers receiving higher review scores by DeepReviewer than existing fully automated systems. Nevertheless, we identify important limitations from the author evaluation and the Agents4Science reviews, indicating the potential risks of directly applying current AI Scientist systems and key challenges for future research. Finally, we comprehensively report various risks identified during development. We believe this study clarifies the current role and limitations of AI Scientist systems, offering insights into the areas that still require human expertise and the risks that may emerge as these systems evolve.

</details>

---

### 54. [Quality Assurance of LLM-generated Code: Addressing Non-Functional Quality Characteristics](https://arxiv.org/abs/2511.10271)

**基本信息**

- 🔗 arXiv: [`2511.10271`](https://arxiv.org/abs/2511.10271)
- 👥 作者: Xin Sun, Daniel Ståhl, Kristian Sandahl 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.10271.pdf)

**💡 相关性分析**

满足标准3：论文是对LLM生成代码质量（特别是非功能质量）的系统性评估研究，包含了文献综述、实践者洞察和实证分析。它为大模型（包括化学领域大模型）的输出质量评估和保证这一重要议题提供了深入的讨论和参考框架，属于相关主题的重要前瞻性讨论。

**📖 中文摘要**

这篇论文研究了由大型语言模型（LLM）生成代码的非功能质量特性。研究采用多方法途径，包括对109篇论文的文献综述、与从业者的行业研讨会，以及使用三个LLM修补真实世界软件问题的实证分析。实证研究考察了生成补丁在安全性、可维护性和性能效率方面的质量。研究结果表明，现有研究主要强调安全性、性能效率和可维护性，而其他质量属性则研究不足。从业者优先考虑可维护性和可读性，并警告生成的代码可能会加速技术债务的积累。这项研究聚焦于**大模型（LLM）输出质量**的评估与保证。虽然应用场景是代码生成，但其核心问题——如何评估和提升大模型生成内容的可靠性、安全性和效率——是任何领域大模型（包括**化学大模型**）投入实际应用前必须解决的关键问题。论文提供的评估框架和发现对化学领域大模型（如用于生成合成程序或分析脚本的模型）的质量保障具有重要参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, large language models have been widely integrated into software engineering workflows, supporting tasks like code generation. While prior evaluations focus on functional correctness, there is still a limited understanding of the non-functional quality characteristics of generated code. Guided by the ISO/IEC 25010 quality model, this study adopts a multi-methods approach comprising three complementary elements: a literature review of 109 papers, two industry workshops with practitioners from multiple organizations, and an empirical analysis of patching real-world software issues using three LLMs. Motivated by insights from both the literature and practitioners, the empirical study examined the quality of generated patches regarding security, maintainability, and performance efficiency, which were identified as critical code-level quality attributes. Our results indicate that existing research primarily emphasizes security, performance efficiency, and maintainability, while other quality attributes are understudied. In contrast, practitioners prioritize maintainability and readability, warning that generated code may accelerate the accumulation of technical debt. The empirical evaluation demonstrates the instability of optimizing NFQCs through prompts in practical software engineering settings. Overall, our findings expose a misalignment between academic focus, industry priorities, and observed model behavior, highlighting the need to integrate quality assurance mechanisms into LLM code generation pipelines to ensure that future generated code not only passes tests but truly passes with quality.

</details>

---

### 55. [ConCISE: A Reference-Free Conciseness Evaluation Metric for LLM-Generated Answers](https://arxiv.org/abs/2511.16846)

**基本信息**

- 🔗 arXiv: [`2511.16846`](https://arxiv.org/abs/2511.16846)
- 👥 作者: Seyed Mohssen Ghafari, Ronny Kol, Juan C. Quiroz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.16846.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于评估大模型（LLM）生成文本简洁性的新指标（ConCISE）。这是一个评估工具，可以应用于化学大模型生成的文本（如实验步骤描述、化合物说明、分析报告）的质量评估和优化过程中，为相关主题提供了实用的评估资源。

**📖 中文摘要**

这篇论文针对大型语言模型（LLM）生成的回答经常冗长、包含冗余细节的问题，提出了一种新颖的无参考简洁性评估指标。该方法在不依赖黄金标准参考的情况下量化非必要内容，通过计算三个度量的平均值来实现：i) 原始回答与LLM抽象摘要之间的压缩比；ii) 原始回答与LLM抽取式摘要之间的压缩比；iii) 词移除压缩，即LLM在保持原意的情况下尽可能多地移除回答中的非必要词语。实验结果表明，该指标能有效识别LLM输出中的冗余。这项研究专注于**大模型输出质量的评估指标**开发。对于**化学大模型**而言，生成的文本（如实验报告、文献摘要、解释性文字）的简洁性和信息密度至关重要。该论文提出的无参考评估方法为优化化学大模型的输出风格、减少冗余、提升信息传递效率提供了一个可用的自动化评估工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) frequently generate responses that are lengthy and verbose, filled with redundant or unnecessary details. This diminishes clarity and user satisfaction, and it increases costs for model developers, especially with well-known proprietary models that charge based on the number of output tokens. In this paper, we introduce a novel reference-free metric for evaluating the conciseness of responses generated by LLMs. Our method quantifies non-essential content without relying on gold standard references and calculates the average of three calculations: i) a compression ratio between the original response and an LLM abstractive summary; ii) a compression ratio between the original response and an LLM extractive summary; and iii) wordremoval compression, where an LLM removes as many non-essential words as possible from the response while preserving its meaning, with the number of tokens removed indicating the conciseness score. Experimental results demonstrate that our proposed metric identifies redundancy in LLM outputs, offering a practical tool for automated evaluation of response brevity in conversational AI systems without the need for ground truth human annotations.

</details>

---

### 56. [De novo molecular structure elucidation from mass spectra via flow matching](https://arxiv.org/abs/2602.19912)

**基本信息**

- 🔗 arXiv: [`2602.19912`](https://arxiv.org/abs/2602.19912)
- 👥 作者: Ghaith Mqawass, Tuan Le, Fabian Theis 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.19912.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”这一主题，提出了一种新的生成式AI模型（MSFlow）用于从质谱数据中推断分子结构。

**📖 中文摘要**

这篇论文提出了一种名为MSFlow的新型两阶段流匹配生成模型，用于解决质谱分析中的一个核心逆问题：从质谱数据中从头推断分子结构。该模型第一阶段使用公式限制的Transformer将质谱编码为连续的、富含化学信息的嵌入向量；第二阶段训练一个解码器流匹配模型，从质谱的潜在嵌入中重建分子。作者通过消融实验证明了使用信息保留的分子描述符对编码质谱的重要性，并论证了其离散流解码器的优势。严格的评估表明，MSFlow能够将高达45%的分子质谱准确翻译为对应的分子表示，相比现有技术有高达14倍的提升。这项工作直接针对“质谱结构推理”这一核心主题，提供了一种先进的生成式AI解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry is a powerful and widely used tool for identifying molecular structures due to its sensitivity and ability to profile complex samples. However, translating spectra into full molecular structures is a difficult, under-defined inverse problem. Overcoming this problem is crucial for enabling biological insight, discovering new metabolites, and advancing chemical research across multiple fields. To this end, we develop MSFlow, a two-stage encoder-decoder flow-matching generative model that achieves state-of-the-art performance on the structure elucidation task for small molecules. In the first stage, we adopt a formula-restricted transformer model for encoding mass spectra into a continuous and chemically informative embedding space, while in the second stage, we train a decoder flow matching model to reconstruct molecules from latent embeddings of mass spectra. We present ablation studies demonstrating the importance of using information-preserving molecular descriptors for encoding mass spectra and motivate the use of our discrete flow-based decoder. Our rigorous evaluation demonstrates that MSFlow can accurately translate up to 45 percent of molecular mass spectra into their corresponding molecular representations - an improvement of up to fourteen-fold over the current state-of-the-art. A trained version of MSFlow is made publicly available on GitHub for non-commercial users.

</details>

---

### 57. [Beyond Explainable AI (XAI): An Overdue Paradigm Shift and Post-XAI Research Directions](https://arxiv.org/abs/2602.24176)

**基本信息**

- 🔗 arXiv: [`2602.24176`](https://arxiv.org/abs/2602.24176)
- 👥 作者: Saleh Afroogh, Seyd Ishtiaque Ahmed, Petra Ahrweiler 等49人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.24176.pdf)

**💡 相关性分析**

满足标准3：论文是对当前AI（特别是大语言模型）可解释性研究范式的批判性综述，并提出了超越现有范式（“后XAI”）的研究方向。这与“化学大模型”主题相关，因为构建可靠、可解释的化学大模型同样面临类似的挑战，论文的讨论提供了重要的理论视角和未来方向。

**📖 中文摘要**

本研究对可解释人工智能（XAI）方法进行了跨学科审视，重点关注深度神经网络（DNN）和大语言模型（LLMs），并指出了当前XAI在实证和概念上的局限性。作者讨论了源于更深层根源（即两个悖论、两个概念混淆和五个错误假设）的关键症状。这些XAI研究领域内的根本问题揭示了三个见解：在实验上，XAI存在显著缺陷；在概念上，它是悖论性的；在实践上，进一步尝试改革悖论性的XAI可能会加剧其混乱——这要求根本性的转变和新的研究方向。为了超越XAI的局限性，作者提出了一个四管齐下的综合范式转变，转向可靠和经过认证的AI开发。这四个组成部分包括：以验证为重点的交互式AI（IAI）、为奠定严格科学基础的AI认识论、为特定用户社区创建情境感知系统的用户可感知AI，以及用于忠实技术分析的以模型为中心的可解释性。这篇论文是对当前AI（特别是大模型）解释性研究范式的批判性综述和前瞻性思考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study provides a cross-disciplinary examination of Explainable Artificial Intelligence (XAI) approaches-focusing on deep neural networks (DNNs) and large language models (LLMs)-and identifies empirical and conceptual limitations in current XAI. We discuss critical symptoms that stem from deeper root causes (i.e., two paradoxes, two conceptual confusions, and five false assumptions). These fundamental problems within the current XAI research field reveal three insights: experimentally, XAI exhibits significant flaws; conceptually, it is paradoxical; and pragmatically, further attempts to reform the paradoxical XAI might exacerbate its confusion-demanding fundamental shifts and new research directions. To move beyond XAI's limitations, we propose a four-pronged synthesized paradigm shift toward reliable and certified AI development. These four components include: verification-focused Interactive AI (IAI) to establish scientific community protocols for certifying AI system performance rather than attempting post-hoc explanations, AI Epistemology for rigorous scientific foundations, User-Sensible AI to create context-aware systems tailored to specific user communities, and Model-Centered Interpretability for faithful technical analysis-together offering comprehensive post-XAI research directions.

</details>

---

### 58. [On the Value of Tokeniser Pretraining in Physics Foundation Models](https://arxiv.org/abs/2603.05598)

**基本信息**

- 🔗 arXiv: [`2603.05598`](https://arxiv.org/abs/2603.05598)
- 👥 作者: Hadi Sotoudeh, Payel Mukhopadhyay, Ruben Ohana 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05598.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及物理仿真“基础模型”的训练策略，特别是分词器预训练对模型效率的影响。虽然领域是物理学，但其关于“基础模型”架构、训练范式和效率优化的方法论讨论，与构建和优化“化学大模型”等科学大模型的研究主题高度相关。

**📖 中文摘要**

本文研究了分词器预训练对物理仿真基础模型精度和效率的影响。作者指出，现代物理仿真产生跨越不同物理机制和尺度的海量数据，训练基础模型来学习这些数据背后的动力学，对于在数据有限的情况下建模复杂的多物理现象至关重要。新兴的物理基础模型通常旨在联合学习两个任务：(i) 从高分辨率时空数据中提取紧凑表示，(ii) 捕捉主导的物理动力学。然而，同时从头开始学习这两个任务可能会阻碍任一过程的有效性。本文表明，在训练动力学模型之前，使用自编码目标对分词器进行预训练，可以显著提高物理仿真的计算效率。值得注意的是，这种收益的大小取决于领域对齐：在与仿真任务相同的物理系统上进行预训练能带来最大的改进。据作者所知，这是首次对物理基础模型的分词器预训练进行系统研究。这项工作探讨了基础模型（包括“化学大模型”可能借鉴的架构思想）在科学计算领域的训练策略和效率优化，与构建用于科学发现的“大模型”主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We investigate the impact of tokeniser pretraining on the accuracy and efficiency of physics emulation. Modern high-resolution simulations produce vast volumes of data spanning diverse physical regimes and scales. Training foundation models to learn the dynamics underlying such data enables the modelling of complex multiphysics phenomena, especially in data-limited settings. The emerging class of physics foundation models typically aims to learn two tasks jointly: (i) extracting compact representations of high-resolution spatiotemporal data, and (ii) capturing governing physical dynamics. However, learning both tasks from scratch simultaneously can impede the effectiveness of either process. We show that pretraining the tokeniser with an autoencoding objective prior to training the dynamics model enhances computational efficiency for physics emulation. Notably, the magnitude of this benefit depends on domain alignment: pretraining on the same physical system as the emulation task yields the largest improvements, while pretraining on other systems provides moderate gains. In-domain pretraining reduces VRMSE by 64% after 10,500 training steps compared to training from scratch. To our knowledge, this is the first systematic investigation of tokeniser pretraining for physics foundation models. We further introduce flexible spatiotemporal compression operations that extend causal convolutions to support runtime-adjustable compression ratios, enabling efficient adaptation to diverse downstream tasks. Our findings provide practical guidance for training efficient physics emulators and highlight the importance of strategic pretraining data selection.

</details>

---

### 59. [Computational Pathology in the Era of Emerging Foundation and Agentic AI -- International Expert Perspectives on Clinical Integration and Translational Readiness](https://arxiv.org/abs/2603.05884)

**基本信息**

- 🔗 arXiv: [`2603.05884`](https://arxiv.org/abs/2603.05884)
- 👥 作者: Qian Da, Yijiang Chen, Min Ju 等28人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05884.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对“基础模型”和“智能体AI”在计算病理学领域应用的综述与展望，包含了对其临床集成和转化准备度的深入讨论。这种对领域特定大模型现状与挑战的分析，与“化学大模型”主题的综述展望相关。

**📖 中文摘要**

这篇综述论文探讨了在基础模型和智能体AI兴起的时代，计算病理学如何向临床转化。文章汇集了国际专家的观点，评估了当前AI系统在预测诊断、预后和治疗反应等任务上的能力，并重点讨论了将这些新兴AI系统负责任地整合到医疗实践中所面临的经济、技术和行政挑战。作者提供了一个实用的评估框架，将可部署的临床相关性与下游分析能力、技术成熟度、操作准备情况以及经济和监管背景联系起来。尽管主题是医学病理学，但论文的核心是对“基础模型”和“智能体AI”在特定科学领域（这里是病理学）的集成、成熟度和转化准备度进行系统性评估。这种对领域特定大模型（可视为“化学大模型”在生命科学领域的类比）的现状、挑战和未来方向的深入讨论，具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent breakthroughs in artificial intelligence through foundation models and agents have accelerated the evolution of computational pathology. Demonstrated performance gains reported across academia in benchmarking datasets in predictive tasks such as diagnosis, prognosis, and treatment response have ignited substantial enthusiasm for clinical application. Despite this development momentum, real world adoption has lagged, as implementation faces economic, technical, and administrative challenges. Beyond existing discussions of technical architectures and comparative performance, this review considers how these emerging AI systems can be responsibly integrated into medical practice by connecting deployable clinical relevance with downstream analytical capabilities and their technical maturity, operational readiness, and economic and regulatory context. Drawing on perspectives from an international group, we provide a practical assessment of current capabilities and barriers to adoption in patient care settings.

</details>

---

### 60. [LatentChem: From Textual CoT to Latent Thinking in Chemical Reasoning](https://arxiv.org/abs/2602.07075)

**基本信息**

- 🔗 arXiv: [`2602.07075`](https://arxiv.org/abs/2602.07075)
- 👥 作者: Xinwu Ye, Yicheng Mao, Jia Zhang 等19人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07075.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”这一主题，提出了一种新的潜在推理框架LatentChem，旨在改进化学大语言模型的推理效率和性能。

**📖 中文摘要**

本文提出了LatentChem，一种用于化学推理的潜在推理接口。它旨在解决当前化学大语言模型（LLMs）主要依赖显式的、离散的自然语言思维链（CoT）进行复杂推理的局限性。作者认为，化学推理本质上是连续和结构化的，将其强制转化为离散的语言标记会造成表征不匹配，从而限制效率和性能。LatentChem将化学计算与文本生成解耦，使模型能够在连续的潜在空间中直接执行多步推理，而仅在最终输出时生成语言。研究发现，当仅针对任务成功进行优化时，模型会自发地将推理过程内化，逐渐放弃冗长的文本推导，转而采用隐式的潜在计算。这种转变不仅是风格上的，而且在计算上具有优势。在多个化学推理基准测试中，LatentChem在ChemCoTBench上相对于基于CoT的基线模型取得了59.88%的非平局胜率，同时推理速度平均提升了10.84倍。这项工作为化学大模型提供了一种新的、更高效的推理范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical large language models (LLMs) predominantly rely on explicit Chain-of-Thought (CoT) in natural language to perform complex reasoning. However, chemical reasoning is inherently continuous and structural, and forcing it into discrete linguistic tokens introduces a fundamental representation mismatch that constrains both efficiency and performance. We introduce LatentChem, a latent reasoning interface that decouples chemical computation from textual generation, enabling models to perform multi-step reasoning directly in continuous latent space while emitting language only for final outputs. Remarkably, we observe a consistent emergent behavior: when optimized solely for task success, models spontaneously internalize reasoning, progressively abandoning verbose textual derivations in favor of implicit latent computation. This shift is not merely stylistic but computationally advantageous. Across diverse chemical reasoning benchmarks, LatentChem achieves a 59.88\% non-tie win rate over strong CoT-based baselines on ChemCoTBench, while delivering a 10.84$\times$ average inference speedup. Our results provide empirical evidence that chemical reasoning is more naturally and effectively realized as continuous latent dynamics rather than discretized linguistic trajectories.

</details>

---

### 61. [Semantics-Aware Caching for Concept Learning](https://arxiv.org/abs/2603.06506)

**基本信息**

- 🔗 arXiv: [`2603.06506`](https://arxiv.org/abs/2603.06506)
- 👥 作者: Louis Mozart Kamdem Teyou, Caglar Demir, Axel-Cyrille Ngonga Ngomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06506.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种语义感知缓存方法，作为一种优化工具，可用于加速概念学习这类知识密集型模型的训练和推理过程，这与构建和优化大型知识模型（化学信息学领域可能涉及）的基础设施相关。

**📖 中文摘要**

本文提出了一种语义感知缓存方法，用于加速概念学习。概念学习是一种在描述逻辑知识库上运行的监督机器学习形式。最先进的概念学习者通常依赖于在可数无限概念空间中的迭代搜索，每次迭代都需要检索候选概念的实例。复杂的学习问题可能需要数千次实例检索调用，导致运行时挑战。作者提出的缓存本质上是一个基于子包含关系的映射，通过精确的集合操作将概念与实例集关联起来。实验表明，该缓存可以将概念检索和概念学习的运行时减少一个数量级，并且对符号推理器和神经符号推理器都有效。这项工作通过优化底层数据检索过程，为构建和运行更高效的知识驱动模型（可视为特定领域的“大模型”或推理系统）提供了工具支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Concept learning is a form of supervised machine learning that operates on knowledge bases in description logics. State-of-the-art concept learners often rely on an iterative search through a countably infinite concept space. In each iteration, they retrieve instances of candidate solutions to select the best concept for the next iteration. While simple learning problems might require a few dozen instance retrieval calls to find a fitting solution, complex learning problems might necessitate thousands of calls. We alleviate the resulting runtime challenge by presenting a semantics-aware caching approach. Our cache is essentially a subsumption-aware map that links concepts to a set of instances via crisp set operations. Our experiments on 5 datasets with 4 symbolic reasoners, a neuro-symbolic reasoner, and 5 popular pagination policies demonstrate that our cache can reduce the runtime of concept retrieval and concept learning by an order of magnitude while being effective for both symbolic and neuro-symbolic reasoners.

</details>

---

### 62. [Scaling Machine Learning Interatomic Potentials with Mixtures of Experts](https://arxiv.org/abs/2603.07977)

**基本信息**

- 🔗 arXiv: [`2603.07977`](https://arxiv.org/abs/2603.07977)
- 👥 作者: Yuzhi Liu, Duo Zhang, Anyang Peng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07977.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于机器学习原子间势（MLIPs）的新型模型架构（MoE/MoLE）。MLIPs是化学和材料科学中用于模拟原子相互作用的关键模型，属于“化学大模型”范畴，因为现代MLIPs通常参数量大、需要处理复杂的化学系统。

**📖 中文摘要**

本文系统地开发了用于机器学习原子间势（MLIPs）的混合专家（MoE）和混合线性专家（MoLE）架构，并分析了路由策略和专家设计的影响。MLIPs能够实现精确的大规模原子模拟。作者展示了稀疏激活与共享专家相结合能带来显著的性能提升，并且当存在共享专家时，非线性MoE公式优于MoLE，强调了非线性专家专业化的重要性。此外，基于元素的（element-wise）路由 consistently优于基于配置（configuration-level）的路由。最终的基于元素的MoE模型在OMol25、OMat24和OC20M基准测试中达到了最先进的精度。对路由模式的分析揭示了与元素周期表趋势一致的、具有化学可解释性的专家专业化，表明该模型有效地捕捉了元素特定的化学特征以进行精确的原子间建模。这项工作直接提升了用于分子和材料模拟的机器学习模型的表达能力和效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine Learning Interatomic Potentials (MLIPs) enable accurate large-scale atomistic simulations, yet improving their expressive capacity efficiently remains challenging. Here we systematically develop Mixture-of-Experts (MoE) and Mixture-of-Linear-Experts (MoLE) architectures for MLIPs and analyze the effects of routing strategies and expert designs. We show that sparse activation combined with shared experts yields substantial performance gains, and that nonlinear MoE formulations outperform MoLE when shared experts are present, underscoring the importance of nonlinear expert specialization. Furthermore, element-wise routing consistently surpasses configuration-level routing, while global MoE routing often leads to numerical instability. The resulting element-wise MoE model achieves state-of-the-art accuracy across the OMol25, OMat24, and OC20M benchmarks. Analysis of routing patterns reveals chemically interpretable expert specialization aligned with periodic-table trends, indicating that the model effectively captures element-specific chemical characteristics for precise interatomic modeling.

</details>

---

### 63. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文的核心是研究带电粒子束（可视为一种特殊“质谱”离子源环境）中的集体振荡和相变，这属于“质谱分析”中涉及离子束物理和动力学的深层理论问题。2) 论文提出了一个结合理论推导和无监督机器学习（Prometheus框架）的通用分析框架，该框架本身可作为研究复杂系统（包括可能的质谱相关离子系统）的工具。

**📖 中文摘要**

本文为中等能量（10-100 MeV）强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。第一部分从Vlasov-Poisson系统出发，推导了Lindhard介电函数和随机相位近似（RPA）极化张量，证明了在临界束密度n_c以上存在无阻尼的朗缪尔波模式，并获得了显式的束-等离子体色散关系。等离子体频率由f求和规则固定，与分布形状无关。空间电荷效应驱动了以sqrt(n-n_c)起始的反常束展宽和在q=2k_F处的Friedel振荡。分析表明束-等离子体转变属于3D Ising普适类。第二部分使用基于beta-VAE的Prometheus框架，对粒子模拟（PIC）得到的静态结构因子数据S(q)进行无监督分析，验证了理论预测。Prometheus成功检测到高斯分布和均匀分布中集体等离子体振荡的开始，确认了简并费米气体中其缺失，并解析了q=2k_F处的Kohn异常。这项工作将理论物理建模与无监督机器学习检测相结合，用于研究束-等离子体系统中的相变和集体模式，展示了复杂物理系统中模式发现的通用方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

## 📊 数据统计
- 累计运行天数：31
- 累计论文数量：2199

## 📝 历史记录

> 暂无历史数据

