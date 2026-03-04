# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-04 13:07:52

## 📅 2026-03-04 (今日最新)

**相关论文数：89**

### 1. [RxnNano:Training Compact LLMs for Chemical Reaction and Retrosynthesis Prediction via Hierarchical Curriculum Learning](https://arxiv.org/abs/2603.02215)

**基本信息**

- 🔗 arXiv: [`2603.02215`](https://arxiv.org/abs/2603.02215)
- 👥 作者: Ran Li, Shimin Di, Haowei LI 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02215.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于化学反应和逆合成预测的紧凑型大语言模型（RxnNano），这直接围绕“化学大模型”这一重点关注主题。

**📖 中文摘要**

本文提出RxnNano，一个用于化学反应和逆合成预测的紧凑型大语言模型（LLM）框架。该工作通过分层课程学习，优先考虑化学理解而非模型规模，旨在将化学反应常识和拓扑原子映射逻辑等深层化学直觉灌输到模型中。其核心创新包括：1）潜在化学一致性目标，将反应建模为连续化学流形上的运动；2）分层认知课程，通过从语法掌握到语义推理的渐进阶段训练模型；3）原子映射排列不变性，迫使模型学习不变的关系拓扑。该0.5B参数的模型在严格基准测试中显著优于更大的微调LLM（>7B）和所有领域基线，Top-1准确率提高了23.5%。这项工作直接针对化学信息学中利用大模型（化学大模型）进行反应预测的核心主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical reaction prediction is pivotal for accelerating drug discovery and synthesis planning. Despite advances in data-driven models, current approaches are hindered by an overemphasis on parameter and dataset scaling. Some methods coupled with evaluation techniques that bypass fundamental challenges in reaction representation and fail to capture deep chemical intuition like reaction common sense and {topological atom mapping logic}. We argue that the core challenge lies in instilling these knowledge into the models. To this end, we propose a unified framework that prioritizes chemical understanding over scale through three key innovations: (1) a {Latent Chemical Consistency} objective that models reactions as movements on a continuous chemical manifold, ensuring reversible and physically plausible transformations; (2) a {Hierarchical Cognitive Curriculum} that trains the model through progressive stages, from syntax mastery to semantic reasoning, building robust chemical intuition; (3) {Atom-Map Permutation Invariance (AMPI)}, which force the model to learn invariant relational topology and balance multi-task learning. (4)and structured plan-based reasoning to improve the performance of the LLMs. Our compact {0.5B-parameter model}, \textbf{RxnNano} significantly outperforms fine-tuned LLMs ten times larger (>7B) and all the domain baselines, achieving a 23.5\% Top-1 accuracy improvement on rigorous benchmarks without test-time augmentation. this https URL .

</details>

---

### 2. [When Scaling Fails: Mitigating Audio Perception Decay of LALMs via Multi-Step Perception-Aware Reasoning](https://arxiv.org/abs/2603.02266)

**基本信息**

- 🔗 arXiv: [`2603.02266`](https://arxiv.org/abs/2603.02266)
- 👥 作者: Ruixiang Mao, Xiangnan Ma, Dan Chen 等15人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02266.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决大型音频-语言模型（LALMs）在复杂推理任务中的感知衰减问题，并提出了改进的推理范式。这涉及大模型在感知和推理任务中的应用，与“化学大模型”和“质谱结构推理”（作为一类需要从复杂信号中进行推理的任务）在方法论上相关。

**📖 中文摘要**

本文研究了大型音频-语言模型（LALMs）中的音频感知衰减现象，即随着推理长度增加，模型对音频输入的感知能力下降，从而损害推理性能。作者提出了MPAR²范式，通过强化学习鼓励动态感知推理，并将复杂问题分解为感知丰富的子问题，以缓解感知衰减。该工作引入了CAFE评估框架来精确量化音频推理错误。实验表明，MPAR²将CAFE上的感知性能从31.74%提升到63.51%，并在MMAU基准上实现了74.59%的准确率。这项研究涉及大型多模态模型在音频相关任务（如质谱分析中可能涉及的音频/信号处理）中的推理能力，与利用大模型进行结构推理的主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Test-Time Scaling has shown notable efficacy in addressing complex problems through scaling inference compute. However, within Large Audio-Language Models (LALMs), an unintuitive phenomenon exists: post-training models for structured reasoning trajectories results in marginal or even negative gains compared to post-training for direct answering. To investigate it, we introduce CAFE, an evaluation framework designed to precisely quantify audio reasoning errors. Evaluation results reveal LALMs struggle with perception during reasoning and encounter a critical bottleneck: reasoning performance suffers from audio perception decay as reasoning length extends. To address it, we propose MPAR$^2$, a paradigm that encourages dynamic perceptual reasoning and decomposes complex questions into perception-rich sub-problems. Leveraging reinforcement learning, MPAR$^2$ improves perception performance on CAFE from 31.74% to 63.51% and effectively mitigates perception decay, concurrently enhancing reasoning capabilities to achieve a significant 74.59% accuracy on the MMAU benchmark. Further analysis demonstrates that MPAR$^2$ reinforces LALMs to attend to audio input and dynamically adapts reasoning budget to match task complexity.

</details>

---

### 3. [Graph Attention Based Prioritization of Disease Responsible Genes from Multimodal Alzheimer's Network](https://arxiv.org/abs/2603.02273)

**基本信息**

- 🔗 arXiv: [`2603.02273`](https://arxiv.org/abs/2603.02273)
- 👥 作者: Binon Teji, Subhajit Bandyopadhyay, Swarup Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02273.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于图变换器（一种图神经网络与大模型思想的结合）的多模态框架，用于从生物网络中推理和优先排序疾病基因。这直接涉及利用先进的、基于注意力机制的模型（可视为特定领域的大模型）进行生物医学结构（网络、分子相互作用）的推理，与“化学大模型”和“质谱结构推理”（作为从复杂数据中推理结构的任务）在核心方法论上相关。

**📖 中文摘要**

本文提出NETRA，一个多模态图变换器框架，用于从阿尔茨海默病（AD）的多组学数据中优先排序疾病相关基因。该框架用注意力驱动的相关性评分取代了传统的启发式中心性度量。它整合了来自微阵列、单细胞RNA-seq和单核RNA-seq数据构建的基因调控网络，以及蛋白质-蛋白质相互作用、基因本体语义相似性等辅助生物网络。一个图变换器为基因分配NETRA分数，以量化其在疾病特定和上下文感知中的相关性。该工作展示了利用图神经网络和变换器模型（一种特定类型的大模型）从复杂的生物网络数据中学习和推理生物医学知识（如疾病机制），这与化学信息学中利用图模型进行分子性质预测或结构推理在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Prioritizing disease-associated genes is central to understanding the molecular mechanisms of complex disorders such as Alzheimer's disease (AD). Traditional network-based approaches rely on static centrality measures and often fail to capture cross-modal biological heterogeneity. We propose NETRA (Node Evaluation through Transformer-based Representation and Attention), a multimodal graph transformer framework that replaces heuristic centrality metrics with attention-driven relevance scoring. Using AD as a case study, gene regulatory networks are independently constructed from microarray, single-cell RNA-seq, and single-nucleus RNA-seq data. Random-walk sequences derived from these networks are used to train a BERT-based model for learning global gene embeddings, while modality-specific gene expression profiles are compressed using variational autoencoders. These representations are integrated with auxiliary biological networks, including protein-protein interactions, Gene Ontology semantic similarity, and diffusion-based gene similarity, into a unified multimodal graph. A graph transformer assigns NETRA scores that quantify gene relevance in a disease-specific and context-aware manner. Gene set enrichment analysis shows that NETRA achieves a normalized enrichment score of about 3.9 for the Alzheimer's disease pathway, substantially outperforming classical centrality measures and diffusion models. Top-ranked genes enrich multiple neurodegenerative pathways, recover a known late-onset AD susceptibility locus at chr12q13, and reveal conserved cross-disease gene modules. The framework preserves biologically realistic heavy-tailed network topology and is readily extensible to other complex disorders.

</details>

---

### 4. [Quantum-Inspired Fine-Tuning for Few-Shot AIGC Detection via Phase-Structured Reparameterization](https://arxiv.org/abs/2603.02281)

**基本信息**

- 🔗 arXiv: [`2603.02281`](https://arxiv.org/abs/2603.02281)
- 👥 作者: Kaiyang Xing, Han Fang, Zhaoyun Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02281.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大型语言模型（LLMs）的微调方法（Q-LoRA/H-LoRA），以提升其在少样本任务（如AIGC检测）上的性能。这直接涉及“化学大模型”领域关注的大模型适配、优化及其在分析任务中的应用。

**📖 中文摘要**

本文提出Q-LoRA和H-LoRA，一种量子启发的微调方案，用于改进少样本AI生成内容（AIGC）检测。该方法将轻量级量子神经网络（QNN）或经典的希尔伯特变换集成到低秩适配器（LoRA）中，以引入相位感知表示和范数约束变换等结构归纳偏置。实验表明，在少样本设置下，该方法在AIGC检测任务上比标准LoRA的准确率提高了5%以上。这项工作探索了将量子计算原理与大模型高效微调技术（LoRA）相结合，以提升模型在特定任务（如内容检测，可类比于质谱谱图真伪或来源分析）上的性能，属于大模型应用与优化的前沿交叉领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent studies show that quantum neural networks (QNNs) generalize well in few-shot regimes. To extend this advantage to large-scale tasks, we propose Q-LoRA, a quantum-enhanced fine-tuning scheme that integrates lightweight QNNs into the low-rank adaptation (LoRA) adapter. Applied to AI-generated content (AIGC) detection, Q-LoRA consistently outperforms standard LoRA under few-shot settings. We analyze the source of this improvement and identify two possible structural inductive biases from QNNs: (i) phase-aware representations, which encode richer information across orthogonal amplitude-phase components, and (ii) norm-constrained transformations, which stabilize optimization via inherent orthogonality. However, Q-LoRA incurs non-trivial overhead due to quantum simulation. Motivated by our analysis, we further introduce H-LoRA, a fully classical variant that applies the Hilbert transform within the LoRA adapter to retain similar phase structure and constraints. Experiments on few-shot AIGC detection show that both Q-LoRA and H-LoRA outperform standard LoRA by over 5% accuracy, with H-LoRA achieving comparable accuracy at significantly lower cost in this task.

</details>

---

### 5. [Characterizing Memorization in Diffusion Language Models: Generalized Extraction and Sampling Effects](https://arxiv.org/abs/2603.02333)

**基本信息**

- 🔗 arXiv: [`2603.02333`](https://arxiv.org/abs/2603.02333)
- 👥 作者: Xiaoyu Luo, Wenrui Yu, Qiongxiu Li 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02333.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统地表征和分析扩散语言模型（DLMs）的记忆化行为。扩散模型是当前生成式AI和大模型的重要分支，其在化学信息学中可用于分子生成、反应预测等。理解这类模型的记忆化特性对于开发可靠、安全的化学大模型至关重要。

**📖 中文摘要**

本文对扩散语言模型（DLMs）中的记忆化行为进行了系统的理论和实证表征。作者提出了一个广义的概率提取框架，将基于前缀的解码和基于扩散的生成在任意掩码模式和随机采样轨迹下统一起来。定理4.3建立了采样分辨率与记忆化之间的单调关系。广泛的实验验证了理论预测，并表明在相同的基于前缀的评估下，DLMs相比自回归语言模型（ARMs）表现出显著更低的基于记忆的个人身份信息泄露。这项研究虽然主要关注语言模型，但其对生成模型（如扩散模型）记忆化和数据提取风险的分析框架，对于化学信息学中可能使用类似生成模型（如用于分子生成或谱图生成的扩散模型）来保护敏感化学数据或防止过拟合具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autoregressive language models (ARMs) have been shown to memorize and occasionally reproduce training data verbatim, raising concerns about privacy and copyright liability. Diffusion language models (DLMs) have recently emerged as a competitive alternative, yet their memorization behavior remains largely unexplored due to fundamental differences in generation dynamics. To address this gap, we present a systematic theoretical and empirical characterization of memorization in DLMs. We propose a generalized probabilistic extraction framework that unifies prefix-conditioned decoding and diffusion-based generation under arbitrary masking patterns and stochastic sampling trajectories. Theorem 4.3 establishes a monotonic relationship between sampling resolution and memorization: increasing resolution strictly increases the probability of exact training data extraction, implying that autoregressive decoding corresponds to a limiting case of diffusion-based generation by setting the sampling resolution maximal. Extensive experiments across model scales and sampling strategies validate our theoretical predictions. Under aligned prefix-conditioned evaluations, we further demonstrate that DLMs exhibit substantially lower memorization-based leakage of personally identifiable information (PII) compared to ARMs.

</details>

---

### 6. [Preconditioned Score and Flow Matching](https://arxiv.org/abs/2603.02337)

**基本信息**

- 🔗 arXiv: [`2603.02337`](https://arxiv.org/abs/2603.02337)
- 👥 作者: Shadab Ahamed, Eshed Gal, Simon Ghyselincks 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02337.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进流匹配和扩散模型（一类重要的生成式大模型）的训练动力学和优化过程。这些模型在化学信息学中正被广泛用于分子设计、性质预测和反应生成，因此该研究直接关系到“化学大模型”的底层技术发展和性能提升。

**📖 中文摘要**

本文研究了流匹配和基于分数的扩散模型中，中间分布p_t的几何性质（由其协方差Σ_t表征）如何影响向量场的优化。作者提出了一种可逆的、标签条件的预处理映射，通过改善Σ_t的条件数来重塑p_t的几何形状，而不改变底层的生成模型。这种方法旨在避免优化停滞，使模型能够沿着先前被抑制的方向持续进展。在MNIST潜在流匹配和高分辨率数据集的实验中，预处理 consistently 产生了训练更好的模型。这项研究涉及生成模型（流匹配/扩散模型）训练动力学的核心问题，这些模型是构建化学大模型（用于分子、材料、反应生成）的关键技术。优化这些模型的训练对于其在化学领域的成功应用至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Flow matching and score-based diffusion train vector fields under intermediate distributions $p_t$, whose geometry can strongly affect their optimization. We show that the covariance $\Sigma_t$ of $p_t$ governs optimization bias: when $\Sigma_t$ is ill-conditioned, and gradient-based training rapidly fits high-variance directions while systematically under-optimizing low-variance modes, leading to learning that plateaus at suboptimal weights. We formalize this effect in analytically tractable settings and propose reversible, label-conditional \emph{preconditioning} maps that reshape the geometry of $p_t$ by improving the conditioning of $\Sigma_t$ without altering the underlying generative model. Rather than accelerating early convergence, preconditioning primarily mitigates optimization stagnation by enabling continued progress along previously suppressed directions. Across MNIST latent flow matching, and additional high-resolution datasets, we empirically track conditioning diagnostics and distributional metrics and show that preconditioning consistently yields better-trained models by avoiding suboptimal plateaus.

</details>

---

### 7. [Estimating Visual Attribute Effects in Advertising from Observational Data: A Deepfake-Informed Double Machine Learning Approach](https://arxiv.org/abs/2603.02359)

**基本信息**

- 🔗 arXiv: [`2603.02359`](https://arxiv.org/abs/2603.02359)
- 👥 作者: Yizhi Liu, Balaji Padmanabhan, Siva Viswanathan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02359.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合生成式AI（深度伪造）和双机器学习（DML）的框架，用于从图像数据中进行因果推断。生成式AI和大模型（视觉编码器）是该框架的核心组件。这种方法论对于化学信息学中利用大模型进行因果分析（如分子属性归因）具有直接的借鉴意义。

**📖 中文摘要**

本文提出DICE-DML框架，用于从观察数据中估计视觉属性（如肤色）在广告中的因果效应。该框架利用生成式AI（深度伪造）生成隔离了处理变量变化的图像对，并结合对抗学习和正交投影，从视觉编码器的纠缠表示中解耦处理信息和混杂因素。在模拟和真实Instagram数据上的实验表明，DICE-DML能有效控制混杂偏倚，获得有效的因果估计。这项工作展示了利用生成式AI和大模型（视觉编码器）进行因果推理的前沿方法。虽然应用场景是广告，但其核心方法论——使用生成模型创建反事实数据以辅助因果推断——对于化学信息学具有重要意义，例如，可用于评估分子结构修改对活性的因果效应，或分析质谱特征与样品来源的因果关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital advertising increasingly relies on visual content, yet marketers lack rigorous methods for understanding how specific visual attributes causally affect consumer engagement. This paper addresses a fundamental methodological challenge: estimating causal effects when the treatment, such as a model's skin tone, is an attribute embedded within the image itself. Standard approaches like Double Machine Learning (DML) fail in this setting because vision encoders entangle treatment information with confounding variables, producing severely biased estimates. We develop DICE-DML (Deepfake-Informed Control Encoder for Double Machine Learning), a framework that leverages generative AI to disentangle treatment from confounders. The approach combines three mechanisms: (1) deepfake-generated image pairs that isolate treatment variation; (2) DICE-Diff adversarial learning on paired difference vectors, where background signals cancel to reveal pure treatment fingerprints; and (3) orthogonal projection that geometrically removes treatment-axis components. In simulations with known ground truth, DICE-DML reduces root mean squared error by 73-97% compared to standard DML, with the strongest improvement (97.5%) at the null effect point, demonstrating robust Type I error control. Applying DICE-DML to 232,089 Instagram influencer posts, we estimate the causal effect of skin tone on engagement. Standard DML produces diagnostically invalid results (negative outcome R^2), while DICE-DML achieves valid confounding control (R^2 = 0.63) and estimates a marginally significant negative effect of darker skin tone (-522 likes; p = 0.062), substantially smaller than the biased standard estimate. Our framework provides a principled approach for causal inference with visual data when treatments and confounders coexist within images.

</details>

---

### 8. [Retrieving Patient-Specific Radiomic Feature Sets for Transparent Knee MRI Assessment](https://arxiv.org/abs/2603.02367)

**基本信息**

- 🔗 arXiv: [`2603.02367`](https://arxiv.org/abs/2603.02367)
- 👥 作者: Yaxi Chen, Simin Ni, Jingjing Zhang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02367.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于学习的、患者自适应的特征选择框架，用于医学图像分析。虽然应用领域是医学影像，但其“为单个样本动态检索最优特征集”的核心思想与“质谱结构推理”中为每个质谱图选择关键特征进行化合物识别的需求高度相关，属于机器学习在复杂数据分析中的高级应用。

**📖 中文摘要**

本文提出一种患者特定的放射组学特征集检索框架，用于膝关节MRI的透明化评估。与依赖群体级预定义特征集或边际排名top-k特征的传统方法不同，该框架预测每个受试者一个紧凑的特征集，目标是互补和多样化的证据。它采用两阶段检索策略：随机采样多样化的候选特征集，然后使用学习的评分函数对这些集进行排序，为特定患者选择高性能的特征集。该系统包括一个特征集评分器和一个执行最终诊断的分类器。在ACL撕裂检测和骨关节炎KL分级的任务中，该方法实现了有竞争力的诊断性能，同时保持了高透明度。这项工作展示了将机器学习（包括可能的表示学习模型）与可解释的放射组学特征相结合，用于医学图像分析。其“为每个样本动态选择最优特征子集”的思想，可以迁移到质谱数据分析中，为每个质谱样本选择最具判别力的峰或特征子集，从而辅助结构推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Classical radiomic features are designed to quantify image appearance and intensity patterns. Compared with end-to-end deep learning (DL) models trained for disease classification, radiomics pipelines with low-dimensional parametric classifiers offer enhanced transparency and interpretability, yet often underperform because of the reliance on population-level predefined feature sets. Recent work on adaptive radiomics uses DL to predict feature weights over a radiomic pool, then thresholds these weights to retain the top-k features from large radiomic pool F (often ~10^3). However, such marginal ranking can over-admit redundant descriptors and overlook complementary feature interactions. We propose a patient-specific feature-set selection framework that predicts a single compact feature set per subject, targeting complementary and diverse evidence rather than marginal top-k features. To overcome the intractable combinatorial search space of F choose k features, our method utilizes a 2-stage retrieval strategy: randomly sample diverse candidate feature sets, then rank these sets with a learned scoring function to select a high-performing feature set for the specific patient. The system consists of a feature-set scorer, and a classifier that performs the final diagnosis. We empirically show that the proposed two-stage retrieval approximates the original exhaustive all k-feature selection. Validating on tasks including ACL tear detection and KL grading for osteoarthritis, the experimental results achieve diagnostic performance, outperforming the top-k approach with the same k values, and competitive with end-to-end DL models while maintaining high transparency. The model generates auditable feature sets that link clinical outcomes to specific anatomical regions and radiomic families, allowing clinicians to inspect which anatomical structures and quantitative descriptors drive the prediction.

</details>

---

### 9. [COOL-MC: Verifying and Explaining RL Policies for Platelet Inventory Management](https://arxiv.org/abs/2603.02396)

**基本信息**

- 🔗 arXiv: [`2603.02396`](https://arxiv.org/abs/2603.02396)
- 👥 作者: Dennis Gross
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02396.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用一个结合了强化学习、模型检验和可解释AI的工具（COOL-MC）来验证和解释AI策略。这涉及大模型/机器学习模型的可信性、安全性和可解释性，这些是“化学大模型”在实际部署中必须考虑的关键问题。

**📖 中文摘要**

本文应用COOL-MC工具来验证和解释血小板库存管理强化学习（RL）策略。COOL-MC结合了RL、概率模型检验和可解释RL。通过构建策略诱导的离散时间马尔可夫链，该工具可以验证概率计算树逻辑（PCTL）属性并提供特征级解释。结果表明，训练后的策略在200步范围内实现了2.9%的缺货概率和1.1%的库存满（潜在浪费）概率。可解释性分析显示，该策略主要关注库存的年龄分布，并采用了多样化的补货策略。这项工作展示了将形式化验证和可解释人工智能（XAI）技术应用于由机器学习（特别是RL）生成的策略，以确保其在安全关键领域（如医疗供应链）的透明度和可靠性。这种方法论对于在化学信息学或质谱分析中部署基于大模型或RL的自动化决策系统（例如，自动化实验设计、谱图解析流程）具有重要的参考价值，有助于建立可信赖的AI系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Platelets expire within five days. Blood banks face uncertain daily demand and must balance ordering decisions between costly wastage from overstocking and life-threatening shortages from understocking. Reinforcement learning (RL) can learn effective ordering policies for this Markov decision process (MDP), but the resulting neural policies remain black boxes, hindering trust and adoption in safety-critical domains. We apply COOL-MC, a tool that combines RL with probabilistic model checking and explainable RL, to verify and explain a trained policy for the MDP on platelet inventory management inspired by Haijema et al. By constructing a policy-induced discrete-time Markov chain (which includes only the reachable states under the trained policy to reduce memory usage), we verify PCTL properties and provide feature-level explanations. Results show that the trained policy achieves a 2.9% stockout probability and a 1.1% inventory-full (potential wastage) probability within a 200-step horizon, primarily attends to the age distribution of inventory rather than other features such as day of week or pending orders. Action reachability analysis reveals that the policy employs a diverse replenishment strategy, with most order quantities reached quickly, while several are never selected. Counterfactual analysis shows that replacing medium-large orders with smaller ones leaves both safety probabilities nearly unchanged, indicating that these orders are placed in well-buffered inventory states. This first formal verification and explanation of an RL platelet inventory management policy demonstrates COOL-MC's value for transparent, auditable decision-making in safety-critical healthcare supply chain domains.

</details>

---

### 10. [Rigidity-Aware Geometric Pretraining for Protein Design and Conformational Ensembles](https://arxiv.org/abs/2603.02406)

**基本信息**

- 🔗 arXiv: [`2603.02406`](https://arxiv.org/abs/2603.02406)
- 👥 作者: Zhanghan Ni, Yanjing Li, Zeju Qiu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02406.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是开发一个用于蛋白质结构建模和设计的几何预训练框架（RigidSSL），这直接属于“化学大模型”在计算生物学和结构生物信息学中的应用。同时，该框架本身是一个新的工具和方法，可用于蛋白质相关的结构推理任务。

**📖 中文摘要**

本文提出RigidSSL，一个用于蛋白质设计和构象系综的刚性感知几何预训练框架。该框架旨在克服当前生成模型在联合学习蛋白质几何与设计任务、建模全局几何理解以及捕获丰富动态信息方面的局限性。RigidSSL包含两个阶段：第一阶段（RigidSSL-Perturb）从AlphaFold数据库的结构中学习几何先验；第二阶段（RigidSSL-MD）在分子动力学轨迹上细化这些表示以捕获物理真实的转变。核心是一个双向的、刚性感知的流匹配目标，共同优化平移和旋转动力学以最大化构象间的互信息。实验表明，RigidSSL变体在无条件生成中提高了可设计性、新颖性和多样性，在零样本基序支架中提高了成功率，并能在G蛋白偶联受体建模中捕获更生物物理真实的构象系综。这项工作直接针对利用大模型（特别是几何深度学习模型）进行蛋白质结构建模与设计，是“化学大模型”在生物分子领域的前沿应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have recently advanced $\textit{de novo}$ protein design by learning the statistical regularities of natural structures. However, current approaches face three key limitations: (1) Existing methods cannot jointly learn protein geometry and design tasks, where pretraining can be a solution; (2) Current pretraining methods mostly rely on local, non-rigid atomic representations for property prediction downstream tasks, limiting global geometric understanding for protein generation tasks; and (3) Existing approaches have yet to effectively model the rich dynamic and conformational information of protein structures. To overcome these issues, we introduce $\textbf{RigidSSL}$ ($\textit{Rigidity-Aware Self-Supervised Learning}$), a geometric pretraining framework that front-loads geometry learning prior to generative finetuning. Phase I (RigidSSL-Perturb) learns geometric priors from 432K structures from the AlphaFold Protein Structure Database with simulated perturbations. Phase II (RigidSSL-MD) refines these representations on 1.3K molecular dynamics trajectories to capture physically realistic transitions. Underpinning both phases is a bi-directional, rigidity-aware flow matching objective that jointly optimizes translational and rotational dynamics to maximize mutual information between conformations. Empirically, RigidSSL variants improve designability by up to 43\% while enhancing novelty and diversity in unconditional generation. Furthermore, RigidSSL-Perturb improves the success rate by 5.8\% in zero-shot motif scaffolding and RigidSSL-MD captures more biophysically realistic conformational ensembles in G protein-coupled receptor modeling. The code is available at: this https URL .

</details>

---

### 11. [From Fewer Samples to Fewer Bits: Reframing Dataset Distillation as Joint Optimization of Precision and Compactness](https://arxiv.org/abs/2603.02411)

**基本信息**

- 🔗 arXiv: [`2603.02411`](https://arxiv.org/abs/2603.02411)
- 👥 作者: My H. Dinh, Aditya Sant, Akshay Malhotra 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02411.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于数据集蒸馏的新框架（QuADD），该框架联合优化数据量化和样本选择。数据集蒸馏是大模型训练数据管理的前沿方向，对于构建高效的“化学大模型”训练流程具有潜在的重要价值。

**📖 中文摘要**

本文提出量化感知数据集蒸馏（QuADD），一个统一的框架，用于在固定比特预算下联合优化数据集的紧凑性和精度。QuADD在蒸馏循环中集成了一个可微分的量化模块，实现了合成样本和量化参数的端到端协同优化。该框架支持均匀和非均匀自适应量化。在图像分类和3GPP波束管理任务上的实验表明，QuADD在每比特准确率上超过了现有的数据集蒸馏和后量化基线，为信息高效的数据集蒸馏建立了新标准。这项工作涉及大模型训练数据的高效压缩和表示，虽然主要针对计算机视觉，但其“联合优化样本数量和精度”的核心思想可以迁移到化学信息学领域，例如，为训练化学大模型（如分子性质预测模型）创建高度压缩且信息保真的训练数据集，或者为质谱库构建紧凑的表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dataset Distillation (DD) compresses large datasets into compact synthetic ones that maintain training performance. However, current methods mainly target sample reduction, with limited consideration of data precision and its impact on efficiency. We propose Quantization-aware Dataset Distillation (QuADD), a unified framework that jointly optimizes dataset compactness and precision under fixed bit budgets. QuADD integrates a differentiable quantization module within the distillation loop, enabling end-to-end co-optimization of synthetic samples and quantization parameters. Guided by the rate-distortion perspective, we empirically analyze how bit allocation between sample count and precision influences learning performance. Our framework supports both uniform and adaptive non-uniform quantization, where the latter learns quantization levels from data to represent information-dense regions better. Experiments on image classification and 3GPP beam management tasks show that QuADD surpasses existing DD and post-quantized baselines in accuracy per bit, establishing a new standard for information-efficient dataset distillation.

</details>

---

### 12. [DINOv3 Visual Representations for Blueberry Perception Toward Robotic Harvesting](https://arxiv.org/abs/2603.02419)

**基本信息**

- 🔗 arXiv: [`2603.02419`](https://arxiv.org/abs/2603.02419)
- 👥 作者: Rui-Feng Wang, Daniel Petti, Yue Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02419.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统评估视觉基础模型（DINOv3，一种视觉大模型）在特定领域视觉任务中的迁移能力和局限性。这属于大模型在专业领域应用和评估的研究，与“化学大模型”在化学领域应用时面临的类似评估和迁移问题相关。

**📖 中文摘要**

本文评估了视觉基础模型DINOv3作为冻结骨干网络在蓝莓机器人收获相关视觉任务（包括果实和瘀伤分割、果实和簇检测）中的性能。研究发现，分割任务受益于稳定的补丁级表示并与骨干网络规模成比例扩展，而检测任务则受目标尺度变化、补丁离散化和定位兼容性的限制。簇检测的失败凸显了在建模由空间聚合定义的关系目标方面的局限性。总体而言，DINOv3最好被视为一个语义骨干网络，其有效性取决于与果实尺度和聚合结构对齐的下游空间建模。这项工作展示了将大规模预训练的视觉基础模型（一种视觉大模型）迁移到农业领域的具体应用和局限性分析。虽然应用领域不同，但其关于大模型作为特征提取器在不同粒度视觉任务中表现的系统性评估，对于化学信息学中考虑使用视觉大模型处理分子图像、光谱图像或微观结构图像具有方法论上的参考意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision Foundation Models trained via large-scale self-supervised learning have demonstrated strong generalization in visual perception; however, their practical role and performance limits in agricultural settings remain insufficiently understood. This work evaluates DINOv3 as a frozen backbone for blueberry robotic harvesting-related visual tasks, including fruit and bruise segmentation, as well as fruit and cluster detection. Under a unified protocol with lightweight decoders, segmentation benefits consistently from stable patch-level representations and scales with backbone size. In contrast, detection is constrained by target scale variation, patch discretization, and localization compatibility. The failure of cluster detection highlights limitations in modeling relational targets defined by spatial aggregation. Overall, DINOv3 is best viewed not as an end-to-end task model, but as a semantic backbone whose effectiveness depends on downstream spatial modeling aligned with fruit-scale and aggregation structures, providing guidance for blueberry robotic harvesting. Code and dataset will be available upon acceptance.

</details>

---

### 13. [AlphaFree: Recommendation Free from Users, IDs, and GNNs](https://arxiv.org/abs/2603.02653)

**基本信息**

- 🔗 arXiv: [`2603.02653`](https://arxiv.org/abs/2603.02653)
- 👥 作者: Minseo Jeon, Junwoo Jung, Daewon Gwak 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02653.pdf)

**💡 相关性分析**

满足标准1：论文提出的AlphaFree方法，核心是利用预训练语言模型的语言表示（LRs）替代传统标识符，并学习实体（如物品）的语义表示。这与化学大模型中利用文本或序列信息（如SMILES）来学习分子表示和进行下游预测的核心主题直接相关。

**📖 中文摘要**

本文提出了AlphaFree，一种新颖的推荐方法，旨在摆脱对用户嵌入、原始ID和图神经网络（GNN）的依赖。其核心思想包括：在没有用户嵌入的情况下动态推断偏好（用户无关），用预训练语言模型的语言表示（LRs）替代原始ID（ID无关），以及通过数据增强和对比学习捕捉协同信号，而无需GNN（GNN无关）。该方法与化学信息学中构建分子表示和预测性质的任务有概念上的相似性。特别是，使用预训练语言模型生成的语言表示来替代传统ID，这与化学大模型中利用分子SMILES或文本描述等序列表示来学习分子特征和结构的思想高度相关。论文提出的方法为如何利用高级语义表示（而非简单标识符）来增强模型对复杂实体（如分子或用户）的理解和泛化能力提供了新的视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Can we design effective recommender systems free from users, IDs, and GNNs? Recommender systems are central to personalized content delivery across domains, with top-K item recommendation being a fundamental task to retrieve the most relevant items from historical interactions. Existing methods rely on entrenched design conventions, often adopted without reconsideration, such as storing per-user embeddings (user-dependent), initializing features from raw IDs (ID-dependent), and employing graph neural networks (GNN-dependent). These dependencies incur several limitations, including high memory costs, cold-start and over-smoothing issues, and poor generalization to unseen interactions. In this work, we propose AlphaFree, a novel recommendation method free from users, IDs, and GNNs. Our main ideas are to infer preferences on-the-fly without user embeddings (user-free), replace raw IDs with language representations (LRs) from pre-trained language models (ID-free), and capture collaborative signals through augmentation with similar items and contrastive learning, without GNNs (GNN-free). Extensive experiments on various real-world datasets show that AlphaFree consistently outperforms its competitors, achieving up to around 40% improvements over non-LR-based methods and up to 5.7% improvements over LR-based methods, while significantly reducing GPU memory usage by up to 69% under high-dimensional LRs.

</details>

---

### 14. [Optimum Battery Depth of Discharge of Stand-alone Hybrid System Using the MOPSO Method](https://arxiv.org/abs/2603.02687)

**基本信息**

- 🔗 arXiv: [`2603.02687`](https://arxiv.org/abs/2603.02687)
- 👥 作者: Mohamad Izdin Hlal, Hussien Elharati, Ahmed Altaher
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02687.pdf)

**💡 相关性分析**

满足标准1：论文提出的BehaveSim方法，核心是通过分析算法的“问题解决轨迹”（即执行过程中的中间状态序列）来评估算法相似性。这种方法论与质谱结构推理中评估不同解析模型或推理路径的合理性和多样性高度相关，为比较复杂的化学信息学算法提供了新的视角和工具。

**📖 中文摘要**

本文提出了BehaveSim，一种通过算法在解决问题过程中产生的中间解序列（即问题解决轨迹，PSTrajs）来衡量算法相似性的新方法。该方法使用动态时间规整（DTW）来量化PSTrajs之间的对齐程度，从而能够区分那些尽管在语法或输出层面相似，但底层逻辑不同的算法。作者展示了该方法在两个关键应用中的效用：1）增强基于LLM的自动算法设计（LLM-AAD）框架，通过促进行为多样性来提升性能；2）对生成的算法进行基于行为的聚类分析，以系统化地分析问题解决策略。这项工作为评估AI生成的算法提供了新工具。在化学信息学领域，特别是在质谱结构推理中，经常需要比较和评估不同算法或模型对同一质谱数据的解释路径和中间推理步骤。BehaveSim提供了一种从“行为”层面（即推理过程）而非最终结果来评估算法相似性和多样性的方法论，这对于开发和评估复杂的化学结构解析算法具有重要参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents an optimized design of a Standalone Solar PV/Battery (SSPVB) system to address energy reliability and cost efficiency challenges in off-grid environments. The proposed system integrates a Multi-Objective Particle Swarm Optimization (MOPSO) approach and validates the results using the Non-Dominated Sorting Genetic Algorithm II (NSGA-II). The optimization process aims to minimize both the Cost of Energy (COE) and Loss of Load Probability (LLP), while examining the effects of Battery Depth of Discharge (DOD) on system reliability and lifecycle cost. Results indicate that an optimal DOD of approximately 70% yields a COE of 0.2059 USD/kWh with zero LLP, demonstrating strong reliability and cost-effectiveness. Comparative analysis shows that both MOPSO and NSGA-II methods achieve consistent outcomes, with MOPSO exhibiting faster convergence. The study provides valuable insights into optimal battery sizing for stand-alone systems, contributing to modern optimization practices in renewable energy applications.

</details>

---

### 15. [Deep learning-guided evolutionary optimization for protein design](https://arxiv.org/abs/2603.02753)

**基本信息**

- 🔗 arXiv: [`2603.02753`](https://arxiv.org/abs/2603.02753)
- 👥 作者: Erik Hartman, Di Tang, Johan Malmström
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02753.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用结合了进化搜索和贝叶斯优化的机器学习框架（BoGA）进行蛋白质设计。这直接属于化学大模型在分子设计、性质预测和优化方面的核心应用范畴。

**📖 中文摘要**

本文提出了BoGA（贝叶斯优化遗传算法）框架，该框架将进化搜索与贝叶斯优化相结合，以高效探索蛋白质序列空间，设计具有特定特性的新型蛋白质。BoGA将遗传算法作为随机提案生成器整合到代理模型循环中，根据先前的评估和代理模型预测对候选序列进行优先级排序，从而实现数据高效的优化。作者通过序列和结构设计任务的基准测试，以及针对肺炎链球菌关键毒力因子肺炎球菌溶血素设计肽结合剂的应用，展示了BoGA的实用性。BoGA加速了高置信度结合剂的发现，证明了其在多样化蛋白质设计目标中的潜力。这项工作直接涉及使用计算模型（结合了进化算法和贝叶斯优化）进行分子/蛋白质设计，这是化学大模型和AI驱动分子发现的核心应用领域之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Designing novel proteins with desired characteristics remains a significant challenge due to the large sequence space and the complexity of sequence-function relationships. Efficient exploration of this space to identify sequences that meet specific design criteria is crucial for advancing therapeutics and biotechnology. Here, we present BoGA (Bayesian Optimization Genetic Algorithm), a framework that combines evolutionary search with Bayesian optimization to efficiently navigate the sequence space. By integrating a genetic algorithm as a stochastic proposal generator within a surrogate modeling loop, BoGA prioritizes candidates based on prior evaluations and surrogate model predictions, enabling data-efficient optimization. We demonstrate the utility of BoGA through benchmarking on sequence and structure design tasks, followed by its application in designing peptide binders against pneumolysin, a key virulence factor of \textit{Streptococcus pneumoniae}. BoGA accelerates the discovery of high-confidence binders, demonstrating the potential for efficient protein design across diverse objectives. The algorithm is implemented within the BoPep suite and is available under an MIT license at \href{ this https URL }{GitHub}.

</details>

---

### 16. [EvoSkill: Automated Skill Discovery for Multi-Agent Systems](https://arxiv.org/abs/2603.02766)

**基本信息**

- 🔗 arXiv: [`2603.02766`](https://arxiv.org/abs/2603.02766)
- 👥 作者: Salaheddin Alzubi, Noah Provenzano, Jaydon Bingham 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02766.pdf)

**💡 相关性分析**

满足标准1：论文提出的EvoSkill框架专注于为多智能体系统自动发现和优化领域特定的“技能”（即工作流和代码）。这一“技能”构建和优化的概念，与在化学信息学中开发用于分子分析、谱图推理等任务的专用、可复用计算模块或代理的核心主题高度相关。

**📖 中文摘要**

本文提出了EvoSkill，一个通过迭代失败分析自动发现和精炼智能体技能的自进化框架。EvoSkill分析执行失败，提出新技能或对现有技能进行编辑，并将其物化为结构化的、可重用的技能文件夹。一个智能体程序的帕累托前沿管理着选择过程，只保留那些在底层模型保持不变的情况下能提高预留验证性能的技能。作者在OfficeQA和SealQA两个基准上评估了EvoSkill，均取得了显著的性能提升。此外，研究还探索了在一个任务上进化出的技能向另一个任务的零样本迁移能力。这项工作展示了通过自动化流程构建和优化领域特定“技能”（即可重用的工作流程和代码）来增强AI智能体专业能力的方法。在化学信息学和质谱分析领域，可以类比为自动构建和优化用于分子性质预测、谱图解析或反应规划的专用计算“工具”或“工作流”，这对于开发专业化的化学AI助手具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Coding agents are increasingly used as general-purpose problem solvers, but their flexibility does not by itself confer the domain expertise needed for specialized tasks. Recent work addresses this through \textit{agent skills}: reusable workflows, and code, that augment agents with domain-specific capabilities. Most skills today are hand-crafted, and existing evolutionary approaches optimize low-level artifacts (e.g. prompts \& code) that are tightly coupled to specific models and tasks. We introduce \textbf{EvoSkill}, a self-evolving framework that automatically discovers and refines agent skills through iterative failure analysis. EvoSkill analyzes execution failures, proposes new skills or edits to existing ones, and materializes them into structured, reusable skill folders. A Pareto frontier of agent programs governs selection, retaining only skills that improve held-out validation performance while the underlying model remains frozen. We evaluate EvoSkill on two benchmarks: OfficeQA, a grounded reasoning benchmark over U.S.\ Treasury data, where it improves exact-match accuracy by \textbf{7.3\%} (60.6\% $\to$ 67.9\%); and SealQA, a search-augmented QA benchmark with noisy retrieval, where it yields a \textbf{12.1\%} gain (26.6\% $\to$ 38.7\%). We also investigate the zero-shot transfer capabilties of skills evolved on one task to the other; in particular: skills evolved from SealQA transfers zero-shot to BrowseComp, improving accuracy by \textbf{5.3\%} without modification demonstrating that skill-level optimization produces transferable capabilities beyond the training task.

</details>

---

### 17. [Embedding interpretable $\ell_1$-regression into neural networks for uncovering temporal structure in cell imaging](https://arxiv.org/abs/2603.02899)

**基本信息**

- 🔗 arXiv: [`2603.02899`](https://arxiv.org/abs/2603.02899)
- 👥 作者: Fabian Kabus, Maren Hackenberg, Julia Hindel 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02899.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发一种结合神经网络和经典统计回归（ℓ1正则化VAR模型）的新方法，用于从质谱相关的细胞成像数据中提取稀疏的、可解释的动态结构。这直接关联到化学信息学和质谱分析中从复杂数据中推理结构模式的核心挑战。

**📖 中文摘要**

本文提出了一种将可解释的ℓ1回归嵌入到神经网络中的方法，用于从细胞成像数据中提取稀疏的自回归动态结构。该方法将向量自回归（VAR）模型作为可解释的回归技术嵌入到卷积自编码器中，利用自编码器进行降维，使ℓ1正则化的VAR模型能够处理高维时间序列数据。ℓ1正则化通过区分分段线性解路径来实现，从而识别出驱动观测动态的关键因素。该方法与那些自编码器不针对VAR模型进行调整的方法形成对比。此外，嵌入的统计模型还支持对同一观测单元的不同时间序列进行比较的测试方法，并通过贡献图可视化驱动学习动态的空间区域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While artificial neural networks excel in unsupervised learning of non-sparse structure, classical statistical regression techniques offer better interpretability, in particular when sparseness is enforced by $\ell_1$ regularization, enabling identification of which factors drive observed dynamics. We investigate how these two types of approaches can be optimally combined, exemplarily considering two-photon calcium imaging data where sparse autoregressive dynamics are to be extracted. We propose embedding a vector autoregressive (VAR) model as an interpretable regression technique into a convolutional autoencoder, which provides dimension reduction for tractable temporal modeling. A skip connection separately addresses non-sparse static spatial information, selectively channeling sparse structure into the $\ell_1$-regularized VAR. $\ell_1$-estimation of regression parameters is enabled by differentiating through the piecewise linear solution path. This is contrasted with approaches where the autoencoder does not adapt to the VAR model. Having an embedded statistical model also enables a testing approach for comparing temporal sequences from the same observational unit. Additionally, contribution maps visualize which spatial regions drive the learned dynamics.

</details>

---

### 18. [Speech recognition assisted by large language models to command software orally -- Application to an augmented and virtual reality web app for immersive molecular graphics](https://arxiv.org/abs/2603.02901)

**基本信息**

- 🔗 arXiv: [`2603.02901`](https://arxiv.org/abs/2603.02901)
- 👥 作者: Fabio Cortes Rodriguez, Luciano Abriata
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02901.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）构建一个交互式系统（语音用户界面），用于控制分子图形软件。这直接涉及化学信息学领域（分子图形、软件工具）和利用大模型（LLM）进行人机交互与任务执行，与“化学大模型”的应用主题相关。

**📖 中文摘要**

本项目成功开发、评估并集成了一个语音用户界面（VUI）到一个用于沉浸式分子图形的网络应用中。该应用提供增强现实（AR）和虚拟现实（VR）环境，用户可以用手操纵分子，但这意味着手无法通过常规的鼠标和键盘GUI来控制应用。本文开发的基于语音的VUI系统解决了这个问题，使得通过自然语音（或键入）命令轻松控制应用成为可能。为了实现这个VUI，我们评估了两种不同的自动语音识别（ASR）系统：Chrome的原生Speech API和OpenAI的Whisper v3。最终选择了Chrome的ASR。为了将转录的语音转换为软件命令，我们测试了两种由大型语言模型（LLM）驱动的方法：生成可执行代码或调用预定义函数。最终采用了由OpenAI的GPT-4o-mini驱动的函数调用方法。最终的VUI基于Chrome的ASR与我们基于LLM的函数调用模块的集成，使用户能够使用自然语言命令应用程序。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This project successfully developed, evaluated and integrated a Voice User Interface (VUI) into a web application that we are developing for immersive molecular graphics. Said app provides augmented and virtual reality (AR and VR) environments where users manipulate molecules with their hands, but this means the hands can't be used to control the app through a regular mouse- and keyboard-based GUI. The speech-based VUI system developed here alleviates this problem, making it easy to control the app via natural spoken (or typed) commands. To achieve this VUI we evaluated two distinct Automated Speech Recognition (ASR) systems: Chrome's native Speech API and OpenAI's Whisper v3. While Whisper offered broader browser compatibility, its tendency to "hallucinate" with specialized scientific jargon proved very problematic. Consequently, we selected Chrome's ASR for its stability, speed, and reliability. For translating transcribed speech into software commands, we tested two Large Language Model (LLM)-driven approaches: either generating executable code, or calling predefined functions. The function call method, powered by OpenAI's GPT-4o-mini, was ultimately adopted due to its superior safety, efficiency, and reliability over the more complex and error-prone code-generation approach. The resulting VUI is then based on an integration of Chrome's ASR with our LLM-based function-calling module, enabling users to command the application using natural language as shown in a video linked inside this report. We provide links to live examples demonstrating all the intermediate components, and details on how we crafted the LLM's prompt in order to teach it the function calls as well as ways to clean up the transcribed speech and to explain itself while generating function calls. For best demonstration of the final system, we provide a video example.

</details>

---

### 19. [Distributed Dynamic Invariant Causal Prediction in Environmental Time Series](https://arxiv.org/abs/2603.02902)

**基本信息**

- 🔗 arXiv: [`2603.02902`](https://arxiv.org/abs/2603.02902)
- 👥 作者: Ziruo Hao, Tao Yang, Xiaofeng Wu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02902.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于时间序列数据（可涵盖环境监测、化学过程等）的因果推理框架。虽然未明确提及质谱，但其处理高维、结构化时间序列数据以进行因果推断和预测的方法论，与化学信息学和质谱分析中从复杂时序数据（如色谱-质谱联用数据）中提取可靠模式和因果关系的研究目标高度相关。

**📖 中文摘要**

本文提出了分布式动态不变因果预测（DisDy-ICPT），一个从具有环境属性的时间序列数据中提取不变因果关系的框架。该框架旨在在分布式时间序列设置中学习动态因果关系，同时减轻空间混杂变量的影响，且无需数据通信。论文从理论上证明了在标准采样假设下，DisDy-ICPT能在有限通信轮数内恢复稳定的因果预测因子。在合成基准测试和环境分段的真实世界数据集上的实证评估表明，DisDy-ICPT在预测稳定性和准确性方面优于基线方法。该方法在碳监测和天气预报等领域有应用前景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The extraction of invariant causal relationships from time series data with environmental attributes is critical for robust decision-making in domains such as climate science and environmental monitoring. However, existing methods either emphasize dynamic causal analysis without leveraging environmental contexts or focus on static invariant causal inference, leaving a gap in distributed temporal settings. In this paper, we propose Distributed Dynamic Invariant Causal Prediction in Time-series (DisDy-ICPT), a novel framework that learns dynamic causal relationships over time while mitigating spatial confounding variables without requiring data communication. We theoretically prove that DisDy-ICPT recovers stable causal predictors within a bounded number of communication rounds under standard sampling assumptions. Empirical evaluations on synthetic benchmarks and environment-segmented real-world datasets show that DisDy-ICPT achieves superior predictive stability and accuracy compared to baseline methods A and B. Our approach offers promising applications in carbon monitoring and weather forecasting. Future work will extend DisDy-ICPT to online learning scenarios.

</details>

---

### 20. [Towards Accurate and Interpretable Time-series Forecasting: A Polynomial Learning Approach](https://arxiv.org/abs/2603.02906)

**基本信息**

- 🔗 arXiv: [`2603.02906`](https://arxiv.org/abs/2603.02906)
- 👥 作者: Bo Liu, Shao-Bo Lin, Changmiao Wang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02906.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、可解释的时间序列预测模型。虽然应用领域是通用预测，但其核心方法论——构建可解释的、基于特征交互的预测模型——与化学信息学和质谱分析中从复杂、高维数据（如光谱、色谱数据）中构建可解释预测模型的需求直接相关，是化学大模型可解释性研究的一个子方向。

**📖 中文摘要**

本文提出了可解释多项式学习（IPL）方法，用于时间序列预测。IPL通过多项式表示显式地建模原始特征及其任意阶的交互作用，将可解释性融入模型结构。这种设计保留了时间依赖性，提供了特征级别的可解释性，并通过调整多项式阶数在预测准确性和可解释性之间提供灵活的权衡。IPL在模拟数据和比特币价格数据上进行了评估，表明其在保持高预测精度的同时，相比广泛使用的可解释性方法具有更优的可解释性。在现场收集的天线数据上的实验进一步证明，IPL能产生更简单、更高效的早期预警机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Time series forecasting enables early warning and has driven asset performance management from traditional planned maintenance to predictive maintenance. However, the lack of interpretability in forecasting methods undermines users' trust and complicates debugging for developers. Consequently, interpretable time-series forecasting has attracted increasing research attention. Nevertheless, existing methods suffer from several limitations, including insufficient modeling of temporal dependencies, lack of feature-level interpretability to support early warning, and difficulty in simultaneously achieving the accuracy and interpretability. This paper proposes the interpretable polynomial learning (IPL) method, which integrates interpretability into the model structure by explicitly modeling original features and their interactions of arbitrary order through polynomial representations. This design preserves temporal dependencies, provides feature-level interpretability, and offers a flexible trade-off between prediction accuracy and interpretability by adjusting the polynomial degree. We evaluate IPL on simulated and Bitcoin price data, showing that it achieves high prediction accuracy with superior interpretability compared with widely used explainability methods. Experiments on field-collected antenna data further demonstrate that IPL yields simpler and more efficient early warning mechanisms.

</details>

---

### 21. [SAE as a Crystal Ball: Interpretable Features Predict Cross-domain Transferability of LLMs without Training](https://arxiv.org/abs/2603.02908)

**基本信息**

- 🔗 arXiv: [`2603.02908`](https://arxiv.org/abs/2603.02908)
- 👥 作者: Qi Zhang, Yifei Wang, Xiaohan Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02908.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和预测大语言模型（LLM）在不同领域间的可迁移性，并提出了一个基于稀疏自编码器（SAE）的评估框架。这直接关联到“化学大模型”主题中一个关键问题：如何评估和确保为化学领域定制或微调的大模型能够有效地迁移到新的、未见过的化学任务或数据集上。

**📖 中文摘要**

本文提出了基于稀疏自编码器（SAE）的可迁移性评分（STS），一种利用SAE来预测大语言模型（LLM）后训练可迁移性的新指标。以监督微调为例，STS识别SAE表示中发生偏移的维度，并计算它们与下游领域的相关性，从而能够在微调之前可靠地估计可迁移性。在多个模型和领域上的大量实验表明，STS能准确预测监督微调的可迁移性，与实际性能变化的皮尔逊相关系数高于0.7。此外，本文还初步尝试将STS扩展到强化学习。作者认为STS可以作为一个可解释的工具，用于指导LLM的后训练策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, pre-trained large language models have achieved remarkable success across diverse tasks. Besides the pivotal role of self-supervised pre-training, their effectiveness in downstream applications also depends critically on the post-training process, which adapts models to task-specific data and objectives. However, this process inevitably introduces model shifts that can influence performance in different domains, and how such shifts transfer remains poorly understood. To open up the black box, we propose the SAE-based Transferability Score (STS), a new metric that leverages sparse autoencoders (SAEs) to forecast post-training transferability. Taking supervised fine-tuning as an example, STS identifies shifted dimensions in SAE representations and calculates their correlations with downstream domains, enabling reliable estimation of transferability \textit{before} fine-tuning. Extensive experiments across multiple models and domains show that STS accurately predicts the transferability of supervised fine-tuning, achieving Pearson correlation coefficients above 0.7 with actual performance changes. Beyond this, we take an initial step toward extending STS to reinforcement learning. We believe that STS can serve as an {\color{black} interpretable} tool for guiding post-training strategies in LLMs. Code is available at this https URL .

</details>

---

### 22. [Eliciting Numerical Predictive Distributions of LLMs Without Autoregression](https://arxiv.org/abs/2603.02913)

**基本信息**

- 🔗 arXiv: [`2603.02913`](https://arxiv.org/abs/2603.02913)
- 👥 作者: Julianna Piskorz, Katarzyna Kobalczyk, Mihaela van der Schaar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02913.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索大语言模型（LLM）在数值预测任务中内部表示与不确定性之间的关系。这直接关联到“化学大模型”和“质谱结构推理”主题，因为化学和质谱分析中的许多任务（如性质预测、谱图解析）本质上是数值预测或回归问题。理解LLM如何编码和输出这类预测的不确定性，对于构建可靠、可解释的化学AI模型至关重要。

**📖 中文摘要**

本文研究了是否可以在不进行显式自回归生成的情况下，从大语言模型（LLM）的内部表示中恢复其数值预测的分布特性。为此，我们研究了一组回归探针，这些探针经过训练，可以直接从LLM的内部表示中预测其数值输出分布的统计函数（例如，均值、中位数、分位数）。我们的结果表明，LLM嵌入携带了关于其预测分布摘要统计信息（包括数值不确定性）的信息信号。这项研究提出了关于LLM如何在数值任务中内部编码不确定性的新问题，以及轻量级替代基于采样的不确定性感知数值预测方法的可行性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have recently been successfully applied to regression tasks -- such as time series forecasting and tabular prediction -- by leveraging their in-context learning abilities. However, their autoregressive decoding process may be ill-suited to continuous-valued outputs, where obtaining predictive distributions over numerical targets requires repeated sampling, leading to high computational cost and inference time. In this work, we investigate whether distributional properties of LLM predictions can be recovered without explicit autoregressive generation. To this end, we study a set of regression probes trained to predict statistical functionals (e.g., mean, median, quantiles) of the LLM's numerical output distribution directly from its internal representations. Our results suggest that LLM embeddings carry informative signals about summary statistics of their predictive distributions, including the numerical uncertainty. This investigation opens up new questions about how LLMs internally encode uncertainty in numerical tasks, and about the feasibility of lightweight alternatives to sampling-based approaches for uncertainty-aware numerical predictions.

</details>

---

### 23. [On the Structural Limitations of Weight-Based Neural Adaptation and the Role of Reversible Behavioral Learning](https://arxiv.org/abs/2603.02934)

**基本信息**

- 🔗 arXiv: [`2603.02934`](https://arxiv.org/abs/2603.02934)
- 👥 作者: Pardhu Sri Rushi Varma Konduru
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02934.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析大模型（如LLM）在适应新任务时其内部表示和行为发生的结构性变化，并提出了“可逆行为学习”的概念。这直接关联到“化学大模型”主题中一个重要的实践问题：如何在对化学大模型进行微调或领域适应时，避免灾难性遗忘或不可逆地损害其原有的、宝贵的化学知识表示，确保模型行为的可控性和可恢复性。

**📖 中文摘要**

本研究引入了结构不可逆性的概念，作为共享参数模型适应的一种特征。它指的是任务特定目标与模型表示身份的纠缠。我们表明，当参数被直接改变时，所得模型的行为会与原始模型产生分歧。这种分歧在没有显式参数快照的情况下无法确定性地逆转。我们引入了可逆行为学习，其中模型行为在结构上与身份参数分离，并可以通过显式的卸载过程确定性地卸载。我们还引入了可恢复性因子作为行为可恢复性的标准化度量，并提供基于模型分歧的额外诊断。实验表明，可逆模型适应在数值精度内实现了回滚，而共享参数突变则表现出持久的重置后分歧。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural models are usually adapted through changes in parameters shared among model components via fine-tuning, alignment-based training, and reinforcement learning. These changes have been found effective in short-term optimization. However, they result in long-term alterations in the model's base behavior. In this study, we introduce the concept of structural irreversibility as a characteristic of shared-parameter model adaptation. This concept refers to the intertwining of task-specific objectives with the representational identity of the model. We show that when parameters are directly mutated, the resulting model behaves divergently from the original model. This divergence cannot be reversed deterministically without an explicit parameter snapshot. We introduce reversible behavioral learning, in which model behaviors are structurally dissociated from identity parameters and can be deterministically unloaded through an explicit unload process. We also introduce the Recoverability Factor as a normalized measure of behavioral recoverability and provide additional diagnostics based on model divergence. Experiments show that reversible model adaptation achieves rollback within numerical precision, whereas shared-parameter mutation exhibits persistent post-reset divergence.

</details>

---

### 24. [Beyond One-Size-Fits-All: Adaptive Subgraph Denoising for Zero-Shot Graph Learning with Large Language Models](https://arxiv.org/abs/2603.02938)

**基本信息**

- 🔗 arXiv: [`2603.02938`](https://arxiv.org/abs/2603.02938)
- 👥 作者: Fengzhi Li, Liang Zhang, Yuan Zuo 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02938.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合大语言模型（LLM）和强化学习（RL）的框架，用于零样本图学习任务。虽然应用场景是通用图，但其方法论——利用LLM进行图结构推理和表示学习，并通过RL优化推理过程——与化学信息学中利用大模型进行分子图（一种特殊的图）的性质预测、反应推理或质谱谱图（可视为图结构）解析等任务在方法论上高度相关。

**📖 中文摘要**

本文针对零样本图学习任务，提出了GraphSSR框架，该框架通过自适应子图提取和去噪来改进基于大语言模型（LLM）的图推理。具体来说，我们提出了SSR（采样-选择-推理）流程，通过“采样-选择-推理”过程动态地为特定上下文定制子图提取，使模型能够自主过滤掉与任务无关的邻居，克服一刀切的问题。为了内化这种能力，我们开发了SSR-SFT，一种数据合成策略，用于生成高质量的SSR风格图推理轨迹，以对LLM进行监督微调。此外，我们提出了SSR-RL，一个两阶段强化学习框架，明确调节所提出的SSR流程内的采样和选择操作，以实现自适应子图去噪。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-based tasks in the zero-shot setting remain a significant challenge due to data scarcity and the inability of traditional Graph Neural Networks (GNNs) to generalize to unseen domains or label spaces. While recent advancements have transitioned toward leveraging Large Language Models (LLMs) as predictors to enhance GNNs, these methods often suffer from cross-modal alignment issues. A recent paradigm (i.e., Graph-R1) overcomes the aforementioned architectural dependencies by adopting a purely text-based format and utilizing LLM-based graph reasoning, showing improved zero-shot generalization. However, it employs a task-agnostic, one-size-fits-all subgraph extraction strategy, which inevitably introduces significant structural noise--irrelevant neighbors and edges--that distorts the LLMs' receptive field and leads to suboptimal predictions. To address this limitation, we introduce GraphSSR, a novel framework designed for adaptive subgraph extraction and denoising in zero-shot LLM-based graph reasoning. Specifically, we propose the SSR pipeline, which dynamically tailors subgraph extraction to specific contexts through a "Sample-Select-Reason" process, enabling the model to autonomously filter out task-irrelevant neighbors and overcome the one-size-fits-all issue. To internalize this capability, we develop SSR-SFT, a data synthesis strategy that generates high-quality SSR-style graph reasoning traces for supervised fine-tuning of LLMs. Furthermore, we propose SSR-RL, a two-stage reinforcement learning framework that explicitly regulates sampling and selection operations within the proposed SSR pipeline designed for adaptive subgraph denoising. By incorporating Authenticity-Reinforced and Denoising-Reinforced RL, we guide the model to achieve accurate predictions using parsimonious, denoised subgraphs for reasoning.

</details>

---

### 25. [ShipTraj-R1: Reinforcing Ship Trajectory Prediction in Large Language Models via Group Relative Policy Optimization](https://arxiv.org/abs/2603.02939)

**基本信息**

- 🔗 arXiv: [`2603.02939`](https://arxiv.org/abs/2603.02939)
- 👥 作者: Yang Zhan, Yunhao Li, Zhang Chao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02939.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型（LLM）和强化学习（GRPO）的轨迹预测框架。虽然应用领域是船舶轨迹，但其核心方法论——将序列预测问题重新表述为文本生成，并利用LLM的推理能力和强化学习进行优化——与化学信息学中利用大模型处理序列数据（如分子SMILES字符串、质谱峰序列）进行预测或生成的任务在技术路径上相似，属于大模型在结构化数据预测上的应用。

**📖 中文摘要**

本文提出了ShipTraj-R1，一个新颖的基于大语言模型（LLM）的框架，将船舶轨迹预测重新表述为文本到文本的生成问题。(1) 我们设计了一个包含冲突船舶轨迹信息的动态提示，以指导模型实现自适应思维链（CoT）推理。(2) 我们引入了一个全面的基于规则的奖励机制，以激励模型的推理格式和预测准确性。(3) 我们的ShipTraj-R1通过由领域特定提示和奖励引导的组相对策略优化（GRPO）机制进行强化，并利用Qwen3作为模型主干。在两个复杂且真实世界的海事数据集上的大量实验结果表明，与最先进的深度学习和基于LLM的基线相比，所提出的ShipTraj-R1实现了最小的误差。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in reinforcement fine-tuning have significantly improved the reasoning ability of large language models (LLMs). In particular, methods such as group relative policy optimization (GRPO) have demonstrated strong capabilities across various fields. However, applying LLMs to ship trajectory prediction remains largely unexplored. In this paper, we propose ShipTraj-R1, a novel LLM-based framework that reformulates ship trajectory prediction as a text-to-text generation problem. (1) We design a dynamic prompt containing trajectory information about conflicting ships to guide the model to achieve adaptive chain-of-thought (CoT) reasoning. (2) We introduce a comprehensive rule-based reward mechanism to incentivize the reasoning format and prediction accuracy of the model. (3) Our ShipTraj-R1 is reinforced through the GRPO mechanism guided by domain-specific prompts and rewards, and utilizes the Qwen3 as the model backbone. Extensive experimental results on two complex and real-world maritime datasets show that the proposed ShipTraj-R1 achieves the least error compared with state-of-the-art deep learning and LLM-based baselines.

</details>

---

### 26. [ACE-Merging: Data-Free Model Merging with Adaptive Covariance Estimation](https://arxiv.org/abs/2603.02945)

**基本信息**

- 🔗 arXiv: [`2603.02945`](https://arxiv.org/abs/2603.02945)
- 👥 作者: Bo Xu, Haotian Wu, Hehai Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02945.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种无需原始训练数据即可合并多个任务特定模型（专家模型）的方法。这直接关联到“化学大模型”主题中的一个重要挑战：如何将针对不同化学子领域（如有机合成、代谢组学、材料设计）训练的多个专家模型有效地整合成一个通用的、能力全面的化学大模型，同时避免灾难性遗忘和负迁移。ACE-Merging为此提供了一种潜在的解决方案。

**📖 中文摘要**

本文提出了ACE-Merging（自适应协方差估计模型合并），一个无需数据访问、重新训练或架构修改的模型合并框架。我们的方法基于一个理论分析，表明每个任务输入协方差（最优合并的关键因素）可以从其微调模型的参数差异中隐式估计，即使在完全无数据的情况下。基于这一见解，我们引入了ACE-Merging，一个自适应协方差估计框架，可有效减轻任务间干扰。我们的方法提供了一个原理性的闭式解，与先前的迭代或启发式方法形成对比。在视觉和语言基准测试上的大量实验表明，ACE-Merging在无数据方法中设立了新的最先进水平。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Model merging aims to combine multiple task-specific expert models into a single model while preserving generalization across diverse tasks. However, interference among experts, especially when they are trained on different objectives, often leads to significant performance degradation. Despite recent progress, resolving this interference without data access, retraining, or architectural modification remains a fundamental challenge. This paper provides a theoretical analysis demonstrating that the input covariance of each task, which is a key factor for optimal merging, can be implicitly estimated from the parameter differences of its fine-tuned model, even in a fully data-free setting. Building on this insight, we introduce \acem, an Adaptive Covariance Estimation framework that effectively mitigates inter-task interference. Our approach features a principled, closed-form solution that contrasts with prior iterative or heuristic methods. Extensive experiments on both vision and language benchmarks demonstrate that \acem sets a new state-of-the-art among data-free methods. It consistently outperforms existing baselines; for example, \acem achieves an average absolute improvement of 4\% over the previous methods across seven tasks on GPT-2. Owing to its efficient closed-form formulation, \acem delivers superior performance with a modest computational cost, providing a practical and theoretically grounded solution for model merging.

</details>

---

### 27. [Enhancing Physics-Informed Neural Networks with Domain-aware Fourier Features: Towards Improved Performance and Interpretable Results](https://arxiv.org/abs/2603.02948)

**基本信息**

- 🔗 arXiv: [`2603.02948`](https://arxiv.org/abs/2603.02948)
- 👥 作者: Alberto Miño Calero, Luis Salamanca, Konstantinos E. Tatsis
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02948.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进物理信息神经网络（PINNs），通过引入领域感知的输入编码（DaFFs）来提升其训练效率和可解释性。虽然PINNs是科学机器学习的一个通用工具，但其在化学和材料科学中有着广泛应用，例如求解控制化学反应或材料行为的偏微分方程。因此，这项提升PINNs性能的工作与化学信息学中利用深度学习解决物理化学问题的研究方向相关。

**📖 中文摘要**

本文提出了一种新颖的建模方法，该方法依赖于使用领域感知傅里叶特征（DaFFs）对输入空间进行位置编码。这些特征封装了所有领域特定的特征，如几何形状和边界条件，并且与随机傅里叶特征（RFFs）不同，它消除了对显式边界条件损失项和损失平衡方案的需求，同时简化了优化过程并降低了训练相关的计算成本。我们进一步开发了一个针对PINNs定制的基于LRP的可解释性框架，能够提取输入空间的相关性归因分数。研究表明，PINN-DaFFs相比普通PINNs和基于RFFs的PINNs，实现了数量级更低的误差，并允许更快的收敛。此外，LRP分析表明，所提出的方法能产生更物理一致的特征归因。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Physics-Informed Neural Networks (PINNs) incorporate physics into neural networks by embedding partial differential equations (PDEs) into their loss function. Despite their success in learning the underlying physics, PINN models remain difficult to train and interpret. In this work, a novel modeling approach is proposed, which relies on the use of Domain-aware Fourier Features (DaFFs) for the positional encoding of the input space. These features encapsulate all the domain-specific characteristics, such as the geometry and boundary conditions, and unlike Random Fourier Features (RFFs), eliminate the need for explicit boundary condition loss terms and loss balancing schemes, while simplifying the optimization process and reducing the computational cost associated with training. We further develop an LRP-based explainability framework tailored to PINNs, enabling the extraction of relevance attribution scores for the input space. It is demonstrated that PINN-DaFFs achieve orders-of-magnitude lower errors and allow faster convergence compared to vanilla PINNs and RFFs-based PINNs. Furthermore, LRP analysis reveals that the proposed leads to more physically consistent feature attributions, while PINN-RFFs and vanilla PINNs display more scattered and less physics-relevant patterns. These results demonstrate that DaFFs not only enhance PINNs' accuracy and efficiency but also improve interpretability, laying the ground for more robust and informative physics-informed learning.

</details>

---

### 28. [Architecting Trust in Artificial Epistemic Agents](https://arxiv.org/abs/2603.02960)

**基本信息**

- 🔗 arXiv: [`2603.02960`](https://arxiv.org/abs/2603.02960)
- 👥 作者: Nahema Marchal, Stephanie Chan, Matija Franklin 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02960.pdf)

**💡 相关性分析**

满足标准3：论文是一篇展望/观点性文章，专门讨论了大语言模型作为“认知主体”所带来的社会、伦理和治理挑战，并提出了一个确保其可信度和与人类认知目标一致的框架。这直接关联到“化学大模型”主题的宏观层面：当化学大模型被用于科学发现、实验设计、文献分析等认知密集型任务时，如何确保其可靠性、可解释性以及符合科学规范，本文的讨论提供了重要的相关视角和原则。

**📖 中文摘要**

本文认为，大型语言模型越来越多地充当认知主体——能够1）自主追求认知目标，2）积极塑造我们共享知识环境的实体。它们策划我们接收的信息，常常取代传统的基于搜索的方法，并经常被用来生成个人化和高度专业化的建议。因此，它们如何执行这些功能，包括它们是否可靠以及是否恰当地校准到个人和集体的认知规范，对我们所做的选择具有高度影响。我们主张，认知AI主体对知识创造、策划和综合实践的潜在影响，特别是在复杂的多主体交互背景下，创造了新的信息相互依赖性，需要对AI的评估和治理进行根本性转变。为了确保有益的人-AI知识生态系统，我们提出了一个以建立和培养认知AI主体的可信度为中心的框架；使这些AI主体与人类认知目标保持一致；并加强周围的社会认知基础设施。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models increasingly function as epistemic agents -- entities that can 1) autonomously pursue epistemic goals and 2) actively shape our shared knowledge environment. They curate the information we receive, often supplanting traditional search-based methods, and are frequently used to generate both personal and deeply specialized advice. How they perform these functions, including whether they are reliable and properly calibrated to both individual and collective epistemic norms, is therefore highly consequential for the choices we make. We argue that the potential impact of epistemic AI agents on practices of knowledge creation, curation and synthesis, particularly in the context of complex multi-agent interactions, creates new informational interdependencies that necessitate a fundamental shift in evaluation and governance of AI. While a well-calibrated ecosystem could augment human judgment and collective decision-making, poorly aligned agents risk causing cognitive deskilling and epistemic drift, making the calibration of these models to human norms a high-stakes necessity. To ensure a beneficial human-AI knowledge ecosystem, we propose a framework centered on building and cultivating the trustworthiness of epistemic AI agents; aligning AI these agents with human epistemic goals; and reinforcing the surrounding socio-epistemic infrastructure. In this context, trustworthy AI agents must demonstrate epistemic competence, robust falsifiability, and epistemically virtuous behaviors, supported by technical provenance systems and "knowledge sanctuaries" designed to protect human resilience. This normative roadmap provides a path toward ensuring that future AI systems act as reliable partners in a robust and inclusive knowledge ecosystem.

</details>

---

### 29. [Delegation and Verification Under AI](https://arxiv.org/abs/2603.02961)

**基本信息**

- 🔗 arXiv: [`2603.02961`](https://arxiv.org/abs/2603.02961)
- 👥 作者: Lingxiao Huang, Wenyang Xiao, Nisheeth K. Vishnoi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02961.pdf)

**💡 相关性分析**

满足标准3：论文通过数学模型探讨了AI（可视为一种大模型辅助工具）如何影响人类工作者的技能发展和决策质量。这虽然不是直接关于化学大模型的技术论文，但其核心讨论——人类与AI在专业任务（如化学分析、结构解析）中的协作模式、委托决策以及对人类专业能力的长远影响——为“化学大模型”在科研和工业场景中的部署和应用提供了重要的社会学和经济学层面的相关讨论和警示。

**📖 中文摘要**

随着AI系统进入制度性工作流程，工作者必须决定是否将任务执行委托给AI，以及投入多少精力来验证AI输出，而机构则使用可能偏离工作者私人成本的结果标准来评估工作者。我们将委托和验证建模为理性工作者优化问题的解决方案，并通过在由此产生的最优行动处评估机构中心的效用（与工作者的目标不同）来定义工作者质量。我们正式描述了最优工作者工作流程，并表明AI会引发相变，其中验证能力的任意微小差异会导致截然不同的行为。因此，AI可以放大具有强大验证可靠性的工作者，同时降低那些理性地过度委托并减少监督的工作者的机构工作者质量，即使基线任务成功率有所提高且不存在行为偏差。这些结果确定了AI重塑机构工作者质量并放大具有不同验证可靠性的工作者之间质量差异的结构性机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As AI systems enter institutional workflows, workers must decide whether to delegate task execution to AI and how much effort to invest in verifying AI outputs, while institutions evaluate workers using outcome-based standards that may misalign with workers' private costs. We model delegation and verification as the solution to a rational worker's optimization problem, and define worker quality by evaluating an institution-centered utility (distinct from the worker's objective) at the resulting optimal action. We formally characterize optimal worker workflows and show that AI induces *phase transitions*, where arbitrarily small differences in verification ability lead to sharply different behaviors. As a result, AI can amplify workers with strong verification reliability while degrading institutional worker quality for others who rationally over-delegate and reduce oversight, even when baseline task success improves and no behavioral biases are present. These results identify a structural mechanism by which AI reshapes institutional worker quality and amplifies quality disparities between workers with different verification reliability.

</details>

---

### 30. [Spatial Autoregressive Modeling of DINOv3 Embeddings for Unsupervised Anomaly Detection](https://arxiv.org/abs/2603.02974)

**基本信息**

- 🔗 arXiv: [`2603.02974`](https://arxiv.org/abs/2603.02974)
- 👥 作者: Ertunc Erdil, Nico Schulthess, Guney Tombak 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02974.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的无监督异常检测方法，该方法利用自回归模型显式建模图像块之间的空间关系。虽然应用在医学影像，但其方法论——处理高维、结构化数据（如图像/谱图）并检测异常模式——与化学信息学和质谱分析中的关键任务高度相关，例如在质谱成像中检测异常组织区域，或在高通量筛选中识别异常光谱。该方法为这些任务提供了一种新的技术思路。

**📖 中文摘要**

本文针对无监督异常检测（UAD）任务，提出了一个简单高效的框架，该框架使用二维自回归（AR）模型显式地建模图像块嵌入之间的空间和上下文依赖关系。我们的方法不是存储嵌入或聚类原型，而是通过AR卷积神经网络（CNN）学习规范分布的紧凑参数模型。在测试时，异常检测简化为通过网络的一次前向传递，实现了快速且内存高效的推理。我们在BMAD基准测试上评估了我们的方法，该基准包含三个医学成像数据集，并将其与现有工作（包括最近的基于DINO的方法）进行比较。实验结果表明，显式建模空间依赖关系在实现有竞争力的异常检测性能的同时，显著减少了推理时间和内存需求。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

DINO models provide rich patch-level representations that have recently enabled strong performance in unsupervised anomaly detection (UAD). Most existing methods extract patch embeddings from ``normal'' images and model them independently, ignoring spatial and neighborhood relationships between patches. This implicitly assumes that self-attention and positional encodings sufficiently encode contextual information within each patch embedding. In addition, the normative distribution is often modeled as memory banks or prototype-based representations, which require storing large numbers of features and performing costly comparisons at inference time, leading to substantial memory and computational overhead. In this work, we address both limitations by proposing a simple and efficient framework that explicitly models spatial and contextual dependencies between patch embeddings using a 2D autoregressive (AR) model. Instead of storing embeddings or clustering prototypes, our approach learns a compact parametric model of the normative distribution via an AR convolutional neural network (CNN). At test time, anomaly detection reduces to a single forward pass through the network and enables fast and memory-efficient inference. We evaluate our method on the BMAD benchmark, which comprises three medical imaging datasets, and compare it against existing work including recent DINO-based methods. Experimental results demonstrate that explicitly modeling spatial dependencies achieves competitive anomaly detection performance while substantially reducing inference time and memory requirements. Code is available at the project page: this https URL .

</details>

---

### 31. [MaBERT:A Padding Safe Interleaved Transformer Mamba Hybrid Encoder for Efficient Extended Context Masked Language Modeling](https://arxiv.org/abs/2603.03001)

**基本信息**

- 🔗 arXiv: [`2603.03001`](https://arxiv.org/abs/2603.03001)
- 👥 作者: Jinwoong Kim, Sangjin Park
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03001.pdf)

**💡 相关性分析**

满足标准1：论文提出的MaBERT混合编码器架构（Transformer与Mamba结合）旨在高效处理长上下文，这为构建能够处理复杂化学结构长序列数据的“化学大模型”提供了核心的模型架构思路和技术可能性。

**📖 中文摘要**

这篇论文提出了MaBERT，一种用于高效扩展上下文掩码语言建模的混合编码器。它通过交错Transformer层和Mamba层，在保持全局依赖建模能力的同时，实现了线性时间状态更新，从而显著提升了长序列处理的效率。虽然论文主要关注自然语言处理中的通用模型架构，但其核心创新——结合Transformer的全局建模能力和Mamba的线性效率来处理长序列——与构建能够处理复杂化学结构（如分子图或质谱序列）的“化学大模型”在技术路径上高度相关。这种高效的混合架构为解决化学信息学中常见的长序列或大图数据处理问题提供了有潜力的模型设计思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Self attention encoders such as Bidirectional Encoder Representations from Transformers(BERT) scale quadratically with sequence length, making long context modeling expensive. Linear time state space models, such as Mamba, are efficient; however, they show limitations in modeling global interactions and can suffer from padding induced state contamination. We propose MaBERT, a hybrid encoder that interleaves Transformer layers for global dependency modeling with Mamba layers for linear time state updates. This design alternates global contextual integration with fast state accumulation, enabling efficient training and inference on long inputs. To stabilize variable length batching, we introduce paddingsafe masking, which blocks state propagation through padded positions, and mask aware attention pooling, which aggregates information only from valid tokens. On GLUE, MaBERT achieves the best mean score on five of the eight tasks, with strong performance on the CoLA and sentence pair inference tasks. When extending the context from 512 to 4,096 tokens, MaBERT reduces training time and inference latency by 2.36x and 2.43x, respectively, relative to the average of encoder baselines, demonstrating a practical long context efficient encoder.

</details>

---

### 32. [OrchMAS: Orchestrated Reasoning with Multi Collaborative Heterogeneous Scientific Expert Structured Agents](https://arxiv.org/abs/2603.03005)

**基本信息**

- 🔗 arXiv: [`2603.03005`](https://arxiv.org/abs/2603.03005)
- 👥 作者: Yichao Feng, Haoran Luo, Zhenghong Lin 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03005.pdf)

**💡 相关性分析**

满足标准1：论文提出的OrchMAS框架是一个专门为科学领域（如化学、生物）设计的、支持多模型协作和动态推理的智能体系统。这种“科学专家智能体”框架与利用大模型进行复杂科学推理（如质谱结构解析）的研究主题直接相关，为构建领域专用的化学或质谱分析智能体提供了系统架构参考。

**📖 中文摘要**

这篇论文提出了OrchMAS，一个面向科学领域的、由多模型协作的异构科学专家结构化智能体框架。它采用两层编排架构，由一个编排模型动态构建领域感知的推理管道并实例化具有定制提示的专家智能体，另一个执行模型在生成的指令下执行每个步骤。该框架支持异构大语言模型集成，并能根据中间反馈迭代更新管道，实现动态重新规划和提示优化，从而增强科学推理的鲁棒性和专业性。该框架是模型无关的，支持不同能力或成本的大语言模型集成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-agent large language model frameworks are promising for complex multi step reasoning, yet existing systems remain weak for scientific and knowledge intensive domains due to static prompts and agent roles, rigid workflows, and homogeneous model reliance, leading to poor domain adaptation, limited reasoning flexibility, and high latency on heterogeneous or long-horizon scientific tasks. They also struggle to revise earlier decisions when intermediate reasoning diverges, reducing reliability in structured and calculation heavy settings. To address these limitations, we propose a scientific domain oriented interactive two tier multi model orchestration framework. A dedicated orchestration model analyzes each task, dynamically constructs a domain aware reasoning pipeline, and instantiates specialized expert agents with tailored prompts, while an execution model performs each step under generated role and instruction specifications. The orchestrator iteratively updates the pipeline based on intermediate feedback, enabling dynamic replanning, role reallocation, and prompt refinement across multi turn interactions, strengthening robustness and specialization for scientific reasoning through structured heterogeneous model collaboration. The framework is model agnostic and supports heterogeneous LLM integration with different capacities or costs, enabling flexible performance efficiency trade offs in practical scientific deployments. Experiments show consistent improvements over existing multi agent systems and strong baselines across diverse reasoning and scientific style benchmarks.

</details>

---

### 33. [Breaking the Prototype Bias Loop: Confidence-Aware Federated Contrastive Learning for Highly Imbalanced Clients](https://arxiv.org/abs/2603.03007)

**基本信息**

- 🔗 arXiv: [`2603.03007`](https://arxiv.org/abs/2603.03007)
- 👥 作者: Tian-Shuang Wu, Shen-Huan Lyu, Ning Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03007.pdf)

**💡 相关性分析**

满足标准1：论文的核心是解决联邦学习中的数据异质性和类别不平衡问题，并提出了一种改进的对比学习框架。虽然应用背景是通用机器学习，但其核心方法（对比学习、原型学习、处理不平衡数据）是构建和训练鲁棒的“化学大模型”或处理来自不同实验室、质量各异的“质谱数据”时可能面临的关键技术挑战。因此，其方法学与主题相关。

**📖 中文摘要**

这篇论文提出了CAFedCL，一个新颖的联邦对比学习框架，旨在解决高度不平衡客户端数据下的原型偏差循环问题。它通过置信度感知的聚合机制、少数类生成增强和几何一致性正则化来改进原型聚合并加强对比对齐。论文从理论角度提供了基于期望的分析，表明其聚合减少了估计方差，从而限制了全局原型漂移并确保收敛。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Local class imbalance and data heterogeneity across clients often trap prototype-based federated contrastive learning in a prototype bias loop: biased local prototypes induced by imbalanced data are aggregated into biased global prototypes, which are repeatedly reused as contrastive anchors, accumulating errors across communication rounds. To break this loop, we propose Confidence-Aware Federated Contrastive Learning (CAFedCL), a novel framework that improves the prototype aggregation mechanism and strengthens the contrastive alignment guided by prototypes. CAFedCL employs a confidence-aware aggregation mechanism that leverages predictive uncertainty to downweight high-variance local prototypes. In addition, generative augmentation for minority classes and geometric consistency regularization are integrated to stabilize the structure between classes. From a theoretical perspective, we provide an expectation-based analysis showing that our aggregation reduces estimation variance, thereby bounding global prototype drift and ensuring convergence. Extensive experiments under varying levels of class imbalance and data heterogeneity demonstrate that CAFedCL consistently outperforms representative federated baselines in both accuracy and client fairness.

</details>

---

### 34. [SEHFS: Structural Entropy-Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection](https://arxiv.org/abs/2603.03022)

**基本信息**

- 🔗 arXiv: [`2603.03022`](https://arxiv.org/abs/2603.03022)
- 👥 作者: Cheng Peng, Yonghao Li, Wanfu Gao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03022.pdf)

**💡 相关性分析**

满足标准1：论文提出的SEHFS方法专注于从多视图数据中学习高阶特征相关性并进行特征选择。在化学信息学中，分子可以用多种描述符（视图）表示，质谱数据也包含丰富的特征。学习这些特征之间的高阶、复杂相关性对于“化学大模型”理解分子性质或“质谱结构推理”至关重要。因此，该论文的方法与主题核心相关。

**📖 中文摘要**

这篇论文提出了SEHFS，一种用于多视图多标签特征选择的新方法。其核心思想是将特征图转换为结构熵最小化的编码树，以量化高阶依赖的信息成本，从而学习超越成对相关的高阶特征相关性。该方法采用基于信息论和矩阵方法融合的新框架，学习共享语义矩阵和视图特定贡献矩阵以重构全局视图矩阵，从而增强信息论方法并平衡全局和局部优化。论文从理论上建立了结构熵学习高阶相关性的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, multi-view multi-label learning (MVML) has attracted extensive attention due to its close alignment to real-world scenarios. Information-theoretic methods have gained prominence for learning nonlinear correlations. However, two key challenges persist: first, features in real-world data commonly exhibit high-order structural correlations, but existing information-theoretic methods struggle to learn such correlations; second, commonly relying on heuristic optimization, information-theoretic methods are prone to converging to local optima. To address these two challenges, we propose a novel method called Structural Entropy Guided High-Order Correlation Learning for Multi-View Multi-Label Feature Selection (SEHFS). The core idea of SEHFS is to convert the feature graph into a structural-entropy-minimizing encoding tree, quantifying the information cost of high-order dependencies and thus learning high-order feature correlations beyond pairwise correlations. Specifically, features exhibiting strong high-order redundancy are grouped into a single cluster within the encoding tree, while inter-cluster feaeture correlations are minimized, thereby eliminating redundancy both within and across clusters. Furthermore, a new framework based on the fusion of information theory and matrix methods is adopted, which learns a shared semantic matrix and view-specific contribution matrices to reconstruct a global view matrix, thereby enhancing the information-theoretic method and balancing the global and local optimization. The ability of structural entropy to learn high-order correlations is theoretically established, and and both experiments on eight datasets from various domains and ablation studies demonstrate that SEHFS achieves superior performance in feature selection.

</details>

---

### 35. [Step-Level Sparse Autoencoder for Reasoning Process Interpretation](https://arxiv.org/abs/2603.03031)

**基本信息**

- 🔗 arXiv: [`2603.03031`](https://arxiv.org/abs/2603.03031)
- 👥 作者: Xuan Yang, Jiayu Liu, Yuhang Lai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03031.pdf)

**💡 相关性分析**

满足标准1：论文专注于分析和解释大语言模型的推理过程，并提出了步级稀疏自编码器这一工具。理解大模型的内部推理机制对于构建可靠、可解释的“化学大模型”至关重要，尤其是在进行“质谱结构推理”等需要严谨逻辑链的科学任务时。该工作为大模型的可解释性研究提供了直接相关的方法。

**📖 中文摘要**

这篇论文提出了步级稀疏自编码器，作为一种分析工具，将大语言模型推理步骤的不同方面解耦为稀疏特征。通过精确控制步骤特征在其上下文中的稀疏性，在步骤重建中形成信息瓶颈，将增量信息与背景信息分离，并将其解耦为几个稀疏激活的维度。实验表明，提取的特征可以轻松预测表面信息以及更复杂的属性，如步骤的正确性和逻辑性。这些观察表明，大语言模型在生成过程中至少部分地知道这些属性，这为大语言模型的自我验证能力提供了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have achieved strong complex reasoning capabilities through Chain-of-Thought (CoT) reasoning. However, their reasoning patterns remain too complicated to analyze. While Sparse Autoencoders (SAEs) have emerged as a powerful tool for interpretability, existing approaches predominantly operate at the token level, creating a granularity mismatch when capturing more critical step-level information, such as reasoning direction and semantic transitions. In this work, we propose step-level sparse autoencoder (SSAE), which serves as an analytical tool to disentangle different aspects of LLMs' reasoning steps into sparse features. Specifically, by precisely controlling the sparsity of a step feature conditioned on its context, we form an information bottleneck in step reconstruction, which splits incremental information from background information and disentangles it into several sparsely activated dimensions. Experiments on multiple base models and reasoning tasks show the effectiveness of the extracted features. By linear probing, we can easily predict surface-level information, such as generation length and first token distribution, as well as more complicated properties, such as the correctness and logicality of the step. These observations indicate that LLMs should already at least partly know about these properties during generation, which provides the foundation for the self-verification ability of LLMs. The code is available at this https URL

</details>

---

### 36. [cPNN: Continuous Progressive Neural Networks for Evolving Streaming Time Series](https://arxiv.org/abs/2603.03040)

**基本信息**

- 🔗 arXiv: [`2603.03040`](https://arxiv.org/abs/2603.03040)
- 👥 作者: Federico Giannini, Giacomo Ziffer, Emanuele Della Valle
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03040.pdf)

**💡 相关性分析**

满足标准1：论文提出的cPNN方法专注于处理非平稳、演化的时间序列数据，并解决概念漂移和灾难性遗忘问题。在化学信息学中，质谱数据流、连续实验监测数据或随时间演化的分子性质数据集都可能表现出类似特性。构建能够持续学习、适应新数据而不遗忘旧知识的“化学大模型”需要此类技术。因此，其核心问题与方法与主题相关。

**📖 中文摘要**

这篇论文提出了连续渐进神经网络，一种用于处理演化流时间序列的解决方案。cPNN是渐进神经网络的连续版本，旨在驯服概念漂移、处理时间依赖性并绕过灾难性遗忘。该方法基于循环神经网络，并利用应用于具有时间依赖性的数据流的随机梯度下降。消融研究的结果显示了cPNN对新概念的快速适应性和对漂移的鲁棒性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dealing with an unbounded data stream involves overcoming the assumption that data is identically distributed and independent. A data stream can, in fact, exhibit temporal dependencies (i.e., be a time series), and data can change distribution over time (concept drift). The two problems are deeply discussed, and existing solutions address them separately: a joint solution is absent. In addition, learning multiple concepts implies remembering the past (a.k.a. avoiding catastrophic forgetting in Neural Networks' terminology). This work proposes Continuous Progressive Neural Networks (cPNN), a solution that tames concept drifts, handles temporal dependencies, and bypasses catastrophic forgetting. cPNN is a continuous version of Progressive Neural Networks, a methodology for remembering old concepts and transferring past knowledge to fit the new concepts quickly. We base our method on Recurrent Neural Networks and exploit the Stochastic Gradient Descent applied to data streams with temporal dependencies. Results of an ablation study show a quick adaptation of cPNN to new concepts and robustness to drifts.

</details>

---

### 37. [TikZilla: Scaling Text-to-TikZ with High-Quality Data and Reinforcement Learning](https://arxiv.org/abs/2603.03072)

**基本信息**

- 🔗 arXiv: [`2603.03072`](https://arxiv.org/abs/2603.03072)
- 👥 作者: Christian Greisinger, Steffen Eger
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03072.pdf)

**💡 相关性分析**

满足标准2：论文构建了DaTikZ-V4这一大规模、高质量的文本到科学图表生成数据集。虽然任务领域是图表生成，但其构建高质量、对齐良好的多模态数据集的流程和方法，对于创建用于“化学大模型”或“质谱结构推理”的训练数据（如文本-分子结构对、质谱-结构对）具有重要的参考价值。

**📖 中文摘要**

这篇论文提出了TikZilla，一个用于从文本描述生成高质量科学图表（TikZ程序）的两阶段训练流程。它构建了DaTikZ-V4数据集，并采用监督微调后接强化学习的策略。对于强化学习，它利用通过逆向图形训练的图像编码器来提供语义忠实的奖励信号。人类评估表明，TikZilla在图像质量上超越了其基础模型，并与GPT-5在基于图像的评估中表现相当。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are increasingly used to assist scientists across diverse workflows. A key challenge is generating high-quality figures from textual descriptions, often represented as TikZ programs that can be rendered as scientific images. Prior research has proposed a variety of datasets and modeling approaches for this task. However, existing datasets for Text-to-TikZ are too small and noisy to capture the complexity of TikZ, causing mismatches between text and rendered figures. Moreover, prior approaches rely solely on supervised fine-tuning (SFT), which does not expose the model to the rendered semantics of the figure, often resulting in errors such as looping, irrelevant content, and incorrect spatial relations. To address these issues, we construct DaTikZ-V4, a dataset more than four times larger and substantially higher in quality than DaTikZ-V3, enriched with LLM-generated figure descriptions. Using this dataset, we train TikZilla, a family of small open-source Qwen models (3B and 8B) with a two-stage pipeline of SFT followed by reinforcement learning (RL). For RL, we leverage an image encoder trained via inverse graphics to provide semantically faithful reward signals. Extensive human evaluations with over 1,000 judgments show that TikZilla improves by 1.5-2 points over its base models on a 5-point scale, surpasses GPT-4o by 0.5 points, and matches GPT-5 in the image-based evaluation, while operating at much smaller model sizes. Code, data, and models will be made available.

</details>

---

### 38. [Odin: Multi-Signal Graph Intelligence for Autonomous Discovery in Knowledge Graphs](https://arxiv.org/abs/2603.03097)

**基本信息**

- 🔗 arXiv: [`2603.03097`](https://arxiv.org/abs/2603.03097)
- 👥 作者: Muyukani Kizito, Elizabeth Nyambere
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03097.pdf)

**💡 相关性分析**

满足标准1：Odin是一个用于知识图自主推理和发现的智能系统。在化学信息学中，分子知识图（如化合物-性质-反应-通路图）是核心资源。Odin所展示的、结合多信号（结构、语义、时间）进行图推理和模式发现的能力，与利用大模型或智能体在化学知识图上进行“质谱结构推理”或分子设计发现的研究目标高度契合。

**📖 中文摘要**

这篇论文提出了Odin，首个用于在知识图中自主发现有意义模式的生产级部署图智能引擎。它通过COMPASS评分引导探索，该评分结合了结构重要性、语义合理性、时间相关性和社区感知指导。该框架采用两时标架构，将快速关联检索与慢速推理动态耦合。Odin代表了首个在受监管生产环境中部署的自主发现系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Odin, the first production-deployed graph intelligence engine for autonomous discovery of meaningful patterns in knowledge graphs without prior specification. Unlike retrieval-based systems that answer predefined queries, Odin guides exploration through the COMPASS (Composite Oriented Multi-signal Path Assessment) score, a novel metric that combines (1) structural importance via Personalized PageRank, (2) semantic plausibility through Neural Probabilistic Logic Learning (NPLL) used as a discriminative filter rather than generative model, (3) temporal relevance with configurable decay, and (4) community-aware guidance through GNN-identified bridge entities and inter-community affinity scores. This multi-signal integration, particularly the bridge scoring mechanism, addresses the "echo chamber" problem where graph exploration becomes trapped in dense local communities. We formalize the autonomous discovery problem, prove theoretical properties of our scoring function, and demonstrate that beam search with multi-signal guidance achieves $O(b \cdot h)$ complexity while maintaining high recall compared to exhaustive exploration. To our knowledge, Odin represents the first autonomous discovery system deployed in regulated production environments (healthcare and insurance), demonstrating significant improvements in pattern discovery quality and analyst efficiency. Our approach maintains complete provenance traceability -- a critical requirement for regulated industries where hallucination is unacceptable.

</details>

---

### 39. [The Science Data Lake: A Unified Open Infrastructure Integrating 293 Million Papers Across Eight Scholarly Sources with Embedding-Based Ontology Alignment](https://arxiv.org/abs/2603.03126)

**基本信息**

- 🔗 arXiv: [`2603.03126`](https://arxiv.org/abs/2603.03126)
- 👥 作者: Jonas Wilinski
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03126.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了“科学数据湖”，这是一个大规模、多源集成的科学文献和元数据资源。对于“化学大模型”和“质谱结构推理”研究，获取高质量、大规模、结构化的化学文献和化合物数据至关重要。该资源为相关研究提供了宝贵的数据基础设施和数据集。

**📖 中文摘要**

这篇论文提出了科学数据湖，一个基于DuckDB和Parquet文件构建的可本地部署的基础设施，它通过DOI规范化统一了八个开放学术数据源，同时保留了源级模式。该资源包含约293万篇唯一可识别论文。此外，论文使用基于嵌入的ontology对齐方法，将OpenAlex主题映射到科学本体上。该资源是开源的，可通过HuggingFace远程查询，并包含适合基于大语言模型的研究智能体的结构化文档。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scholarly data are largely fragmented across siloed databases with divergent metadata and missing linkages among them. We present the Science Data Lake, a locally-deployable infrastructure built on DuckDB and simple Parquet files that unifies eight open sources - Semantic Scholar, OpenAlex, SciSciNet, Papers with Code, Retraction Watch, Reliance on Science, a preprint-to-published mapping, and Crossref - via DOI normalization while preserving source-level schemas. The resource comprises approximately 960GB of Parquet files spanning ~293 million uniquely identifiable papers across ~22 schemas and ~153 SQL views. An embedding-based ontology alignment using BGE-large sentence embeddings maps 4,516 OpenAlex topics to 13 scientific ontologies (~1.3 million terms), yielding 16,150 mappings covering 99.8% of topics ($\geq 0.65$ threshold) with $F1 = 0.77$ at the recommended $\geq 0.85$ operating point, outperforming TF-IDF, BM25, and Jaro-Winkler baselines on a 300-pair gold-standard evaluation. We validate through 10 automated checks, cross-source citation agreement analysis (pairwise Pearson $r = 0.76$ - $0.87$), and stratified manual annotation. Four vignettes demonstrate cross-source analyses infeasible with any single database. The resource is open source, deployable on a single drive or queryable remotely via HuggingFace, and includes structured documentation suitable for large language model (LLM) based research agents.

</details>

---

### 40. [FEAST: Retrieval-Augmented Multi-Hierarchical Food Classification for the FoodEx2 System](https://arxiv.org/abs/2603.03176)

**基本信息**

- 🔗 arXiv: [`2603.03176`](https://arxiv.org/abs/2603.03176)
- 👥 作者: Lorenzo Molfetta, Alessio Cocchieri, Stefano Fantazzini 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03176.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个用于复杂层次分类任务的检索增强生成框架。虽然应用领域是食品分类，但其核心方法——将复杂分类任务分解为多阶段流程、利用层次结构、进行深度度量学习以处理数据稀疏和细粒度标签——与化学信息学中处理层次化分子分类、谱图解析等任务面临相似的挑战。其方法学对构建化学领域的分类或解析模型具有参考价值。

**📖 中文摘要**

这篇论文提出了FEAST，一个新颖的检索增强框架，用于将FoodEx2食品分类任务分解为三阶段方法：基础术语识别、多标签方面预测和方面描述符分配。通过利用系统的层次结构指导训练并进行深度度量学习，FEAST学习区分性嵌入，以缓解数据稀疏性并改善对稀有和细粒度标签的泛化。在多语言FoodEx2基准测试上的评估表明，FEAST在稀有类别上的F1分数比先前基线提高了12-38%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hierarchical text classification (HTC) and extreme multi-label classification (XML) tasks face compounded challenges from complex label interdependencies, data sparsity, and extreme output dimensions. These challenges are exemplified in the European Food Safety Authority's FoodEx2 system-a standardized food classification framework essential for food consumption monitoring and contaminant exposure assessment across Europe. FoodEx2 coding transforms natural language food descriptions into a set of codes from multiple standardized hierarchies, but faces implementation barriers due to its complex structure. Given a food description (e.g., "organic yogurt''), the system identifies its base term ("yogurt''), all the applicable facet categories (e.g., "production method''), and then, every relevant facet descriptors to each category (e.g., "organic production''). While existing models perform adequately on well-balanced and semantically dense hierarchies, no work has been applied on the practical constraints imposed by the FoodEx2 system. The limited literature addressing such real-world scenarios further compounds these challenges. We propose FEAST (Food Embedding And Semantic Taxonomy), a novel retrieval-augmented framework that decomposes FoodEx2 classification into a three-stage approach: (1) base term identification, (2) multi-label facet prediction, and (3) facet descriptor assignment. By leveraging the system's hierarchical structure to guide training and performing deep metric learning, FEASTlearns discriminative embeddings that mitigate data sparsity and improve generalization on rare and fine-grained labels. Evaluated on the multilingual FoodEx2 benchmark, FEAST outperforms the prior European's CNN baseline F1 scores by 12-38 % on rare classes.

</details>

---

### 41. [Neuro-Symbolic Artificial Intelligence: A Task-Directed Survey in the Black-Box Models Era](https://arxiv.org/abs/2603.03177)

**基本信息**

- 🔗 arXiv: [`2603.03177`](https://arxiv.org/abs/2603.03177)
- 👥 作者: Giovanni Pio Delvecchio, Lorenzo Molfetta, Gianluca Moro
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03177.pdf)

**💡 相关性分析**

满足标准3：这篇论文是一篇关于“神经符号人工智能”的综述。神经符号AI结合了神经网络的感知能力和符号系统的推理能力，这正是构建能够进行严谨“质谱结构推理”或分子设计的“化学大模型”所追求的目标之一。该综述提供了与该主题相关的重要讨论和方法论概览。

**📖 中文摘要**

这篇论文对神经符号人工智能进行了任务导向的综述，探讨了在当今黑盒模型时代，如何通过结合符号系统来增强可解释性和推理能力。它审查了特定任务在NeSy领域的进展，旨在作为研究人员探索可解释的NeSy方法以解决现实任务和应用的资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of symbolic computing with neural networks has intrigued researchers since the first theorizations of Artificial intelligence (AI). The ability of Neuro-Symbolic (NeSy) methods to infer or exploit behavioral schema has been widely considered as one of the possible proxies for human-level intelligence. However, the limited semantic generalizability and the challenges in declining complex domains with pre-defined patterns and rules hinder their practical implementation in real-world scenarios. The unprecedented results achieved by connectionist systems since the last AI breakthrough in 2017 have raised questions about the competitiveness of NeSy solutions, with particular emphasis on the Natural Language Processing and Computer Vision fields. This survey examines task-specific advancements in the NeSy domain to explore how incorporating symbolic systems can enhance explainability and reasoning capabilities. Our findings are meant to serve as a resource for researchers exploring explainable NeSy methodologies for real-life tasks and applications. Reproducibility details and in-depth comments on each surveyed research work are made available at this https URL .

</details>

---

### 42. [Type-Aware Retrieval-Augmented Generation with Dependency Closure for Solver-Executable Industrial Optimization Modeling](https://arxiv.org/abs/2603.03180)

**基本信息**

- 🔗 arXiv: [`2603.03180`](https://arxiv.org/abs/2603.03180)
- 👥 作者: Y. Zhong, R. Huang, M. Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03180.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种将自然语言转换为可执行代码（特别是优化建模代码）的类型感知RAG方法。在化学信息学中，将自然语言描述的化学问题或实验协议转换为可计算的模型或模拟指令是一个重要方向。该方法中类型约束、依赖闭包和知识图的使用，对于构建能够可靠执行化学计算或推理的智能体系统具有直接相关性。

**📖 中文摘要**

这篇论文提出了一种类型感知的检索增强生成方法，用于将自然语言需求可靠地转换为求解器可执行的优化建模代码。与索引非结构化文本的现有RAG方法不同，该方法通过将异构源解析为类型化单元并在知识图中编码其数学依赖关系，构建了一个领域特定的类型化知识库。给定自然语言指令，它执行混合检索并通过依赖传播在图上计算最小依赖闭包上下文。该方法在电池生产的需求响应优化和柔性作业车间调度两个约束密集型工业案例上进行了验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated industrial optimization modeling requires reliable translation of natural-language requirements into solver-executable code. However, large language models often generate non-compilable models due to missing declarations, type inconsistencies, and incomplete dependency contexts. We propose a type-aware retrieval-augmented generation (RAG) method that enforces modeling entity types and minimal dependency closure to ensure executability. Unlike existing RAG approaches that index unstructured text, our method constructs a domain-specific typed knowledge base by parsing heterogeneous sources, such as academic papers and solver code, into typed units and encoding their mathematical dependencies in a knowledge graph. Given a natural-language instruction, it performs hybrid retrieval and computes a minimal dependency-closed context, the smallest set of typed symbols required for solver-executable code, via dependency propagation over the graph. We validate the method on two constraint-intensive industrial cases: demand response optimization in battery production and flexible job shop scheduling. In the first case, our method generates an executable model incorporating demand-response incentives and load-reduction constraints, achieving peak shaving while preserving profitability; conventional RAG baselines fail. In the second case, it consistently produces compilable models that reach known optimal solutions, demonstrating robust cross-domain generalization; baselines fail entirely. Ablation studies confirm that enforcing type-aware dependency closure is essential for avoiding structural hallucinations and ensuring executability, addressing a critical barrier to deploying large language models in complex engineering optimization tasks.

</details>

---

### 43. [Infinite dimensional generative sensing](https://arxiv.org/abs/2603.03196)

**基本信息**

- 🔗 arXiv: [`2603.03196`](https://arxiv.org/abs/2603.03196)
- 👥 作者: Paolo Angella, Vito Paolo Pastore, Matteo Santacesaria
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03196.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个无限维生成式压缩感知的理论框架。虽然背景是通用信号处理，但其核心——研究如何利用生成模型作为先验，从有限测量中高保真地恢复高维或函数空间中的信号——与从有限的质谱数据（测量）中推断完整的分子结构（高维对象）这一“质谱结构推理”核心问题在数学形式上高度相似。该理论框架为后者提供了潜在的理论基础和方法启示。

**📖 中文摘要**

这篇论文提出了一个用于希尔伯特空间中生成式压缩感知的严格框架。它将局部相干性的概念扩展到无限维设置，以推导出最优的、与分辨率无关的采样分布。得益于限制等距性质的推广，研究表明，当测量数量与先验的内在维度成正比时，稳定恢复成立。数值实验在达西流方程上验证了理论发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep generative models have become a standard for modeling priors for inverse problems, going beyond classical sparsity-based methods. However, existing theoretical guarantees are mostly confined to finite-dimensional vector spaces, creating a gap when the physical signals are modeled as functions in Hilbert spaces. This work presents a rigorous framework for generative compressed sensing in Hilbert spaces. We extend the notion of local coherence in an infinite-dimensional setting, to derive optimal, resolution-independent sampling distributions. Thanks to a generalization of the Restricted Isometry Property, we show that stable recovery holds when the number of measurements is proportional to the prior's intrinsic dimension (up to logarithmic factors), independent of the ambient dimension. Finally, numerical experiments on the Darcy flow equation validate our theoretical findings and demonstrate that in severely undersampled regimes, employing lower-resolution generators acts as an implicit regularizer, improving reconstruction stability.

</details>

---

### 44. [A Dynamical Theory of Sequential Retrieval in Input-Driven Hopfield Networks](https://arxiv.org/abs/2603.03201)

**基本信息**

- 🔗 arXiv: [`2603.03201`](https://arxiv.org/abs/2603.03201)
- 👥 作者: Simone Betteti, Giacomo Baggio, Sandro Zampieri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03201.pdf)

**💡 相关性分析**

满足标准1：论文专注于从动力学理论角度研究联想记忆模型中的顺序检索和推理能力。理解并建模顺序推理是构建能够进行多步“质谱结构推理”的化学大模型或智能体的关键。该工作为基于类似Hopfield网络的架构实现可靠的序列化科学推理提供了理论基础，与主题直接相关。

**📖 中文摘要**

这篇论文发展了Hopfield网络中顺序推理的动力学理论。它考虑了最近提出的输入驱动可塑性Hopfield网络，并分析了一个将快速关联检索与慢速推理动力学耦合的两时标架构。研究推导了自维持记忆转换的明确条件，包括增益阈值、逃逸时间和崩溃机制。这些结果为关联记忆模型中的顺序性提供了原则性的数学解释， bridging classical Hopfield dynamics and modern reasoning architectures.

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning is the ability to integrate internal states and external inputs in a meaningful and semantically consistent flow. Contemporary machine learning (ML) systems increasingly rely on such sequential reasoning, from language understanding to multi-modal generation, often operating over dictionaries of prototypical patterns reminiscent of associative memory models. Understanding retrieval and sequentiality in associative memory models provides a powerful bridge to gain insight into ML reasoning. While the static retrieval properties of associative memory models are well understood, the theoretical foundations of sequential retrieval and multi-memory integration remain limited, with existing studies largely relying on numerical evidence. This work develops a dynamical theory of sequential reasoning in Hopfield networks. We consider the recently proposed input-driven plasticity (IDP) Hopfield network and analyze a two-timescale architecture coupling fast associative retrieval with slow reasoning dynamics. We derive explicit conditions for self-sustained memory transitions, including gain thresholds, escape times, and collapse regimes. Together, these results provide a principled mathematical account of sequentiality in associative memory models, bridging classical Hopfield dynamics and modern reasoning architectures.

</details>

---

### 45. [AI-for-Science Low-code Platform with Bayesian Adversarial Multi-Agent Framework](https://arxiv.org/abs/2603.03233)

**基本信息**

- 🔗 arXiv: [`2603.03233`](https://arxiv.org/abs/2603.03233)
- 👥 作者: Zihang Zeng, Jiaquan Zhang, Pengze Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03233.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于科学任务的AI智能体框架，这直接涉及利用大模型（LLM）自动化科学工作流程，与“化学大模型”这一关注主题高度相关。

**📖 中文摘要**

本文提出了一个用于科学（AI4S）任务的低代码平台（LCP），该平台采用贝叶斯对抗多智能体框架。该框架协调三个基于大语言模型（LLM）的智能体：任务管理器、代码生成器和评估器，通过对抗循环和贝叶斯原则动态优化测试用例和代码。虽然论文主要关注通用科学代码生成，但其核心是构建一个能够处理科学领域（可能包括化学）复杂任务的AI系统。该框架展示了利用大语言模型和智能体协作自动化科学工作流程的潜力，这与“化学大模型”主题中利用AI模型解决化学问题的研究方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) demonstrate potentials for automating scientific code generation but face challenges in reliability, error propagation in multi-agent workflows, and evaluation in domains with ill-defined success metrics. We present a Bayesian adversarial multi-agent framework specifically designed for AI for Science (AI4S) tasks in the form of a Low-code Platform (LCP). Three LLM-based agents are coordinated under the Bayesian framework: a Task Manager that structures user inputs into actionable plans and adaptive test cases, a Code Generator that produces candidate solutions, and an Evaluator providing comprehensive feedback. The framework employs an adversarial loop where the Task Manager iteratively refines test cases to challenge the Code Generator, while prompt distributions are dynamically updated using Bayesian principles by integrating code quality metrics: functional correctness, structural alignment, and static analysis. This co-optimization of tests and code reduces dependence on LLM reliability and addresses evaluation uncertainty inherent to scientific tasks. LCP also streamlines human-AI collaboration by translating non-expert prompts into domain-specific requirements, bypassing the need for manual prompt engineering by practitioners without coding backgrounds. Benchmark evaluations demonstrate LCP's effectiveness in generating robust code while minimizing error propagation. The proposed platform is also tested on an Earth Science cross-disciplinary task and demonstrates strong reliability, outperforming competing models.

</details>

---

### 46. [Using Learning Progressions to Guide AI Feedback for Science Learning](https://arxiv.org/abs/2603.03249)

**基本信息**

- 🔗 arXiv: [`2603.03249`](https://arxiv.org/abs/2603.03249)
- 👥 作者: Xin Xia, Nejla Yuruk, Yun Wang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03249.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用AI（可视为一种特定领域的大模型应用）为化学学习任务生成反馈，是“化学大模型”主题在科学教育领域的一个具体应用案例。

**📖 中文摘要**

本研究探讨了如何利用学习进程（Learning Progressions, LP）来指导人工智能（AI）为科学学习（以化学任务为例）生成形成性反馈。研究比较了两种AI反馈生成流程：一种基于专家设计的任务特定评分标准，另一种基于从学习进程自动推导出的任务特定评分标准。实验结果表明，基于LP的流程生成的反馈在多个质量维度上与专家标准生成的反馈无显著差异。这项工作展示了将教育理论与大语言模型（作为生成反馈的AI）相结合，为特定学科（如化学）学习提供规模化支持的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative artificial intelligence (AI) offers scalable support for formative feedback, yet most AI-generated feedback relies on task-specific rubrics authored by domain experts. While effective, rubric authoring is time-consuming and limits scalability across instructional contexts. Learning progressions (LP) provide a theoretically grounded representation of students' developing understanding and may offer an alternative solution. This study examines whether an LP-driven rubric generation pipeline can produce AI-generated feedback comparable in quality to feedback guided by expert-authored task rubrics. We analyzed AI-generated feedback for written scientific explanations produced by 207 middle school students in a chemistry task. Two pipelines were compared: (a) feedback guided by a human expert-designed, task-specific rubric, and (b) feedback guided by a task-specific rubric automatically derived from a learning progression prior to grading and feedback generation. Two human coders evaluated feedback quality using a multi-dimensional rubric assessing Clarity, Accuracy, Relevance, Engagement and Motivation, and Reflectiveness (10 sub-dimensions). Inter-rater reliability was high, with percent agreement ranging from 89% to 100% and Cohen's kappa values for estimable dimensions (kappa = .66 to .88). Paired t-tests revealed no statistically significant differences between the two pipelines for Clarity (t1 = 0.00, p1 = 1.000; t2 = 0.84, p2 = .399), Relevance (t1 = 0.28, p1 = .782; t2 = -0.58, p2 = .565), Engagement and Motivation (t1 = 0.50, p1 = .618; t2 = -0.58, p2 = .565), or Reflectiveness (t = -0.45, p = .656). These findings suggest that the LP-driven rubric pipeline can serve as an alternative solution.

</details>

---

### 47. [Hybrid Machine Learning for Enhanced Prediction of Diffusion Coefficients in Liquids](https://arxiv.org/abs/2603.02761)

**基本信息**

- 🔗 arXiv: [`2603.02761`](https://arxiv.org/abs/2603.02761)
- 👥 作者: Jens Wagner, Zeno Romero, Kerstin Münnemann 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02761.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于预测化学物质扩散系数的机器学习模型，这是化学信息学中利用数据驱动方法解决化学问题的典型研究，与“化学大模型”主题相关。

**📖 中文摘要**

本文提出了一种新的混合机器学习方法（Enhanced Stokes-Einstein, ESE），用于预测分子在纯液体溶剂中的无限稀释扩散系数。该方法将斯托克斯-爱因斯坦方程与机器学习相结合，仅需输入分子的SMILES字符串即可进行预测，确保了物理一致性并实现了高精度。论文建立了一个广泛的文献数据汇编用于训练和验证，并提供了交互式网络接口。这项工作属于化学信息学领域，专注于利用机器学习模型预测关键的物理化学性质，是构建化学领域预测模型（可视为化学性质预测“大模型”的基础组件）的重要实践。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion coefficients are key thermophysical properties for modeling mass transport in liquids, but experimental data are scarce, making reliable prediction methods indispensable. In the present work, we introduce a new method for predicting diffusion coefficients of molecular components at infinite dilution in pure liquid solvents by integrating the Stokes-Einstein (SE) equation with machine learning (ML). Unlike previous ML approaches, the resulting hybrid Enhanced Stokes-Einstein (ESE) model provides strictly physically consistent predictions for diffusion coefficients as a function of temperature across a broad range of binary mixtures. Trained and validated using an extensive compilation of literature data for infinite-dilution diffusion coefficients in binary liquid systems, ESE achieves significantly higher prediction accuracies than the previous state-of-the-art model, SEGWE, while requiring only the SMILES strings encoding of the molecular formulae of the components of interest as additional inputs, which are always available. This simplicity makes ESE broadly applicable, e.g., for process design and optimization. The ESE model and its source code are fully disclosed and are directly accessible via an interactive web interface at this https URL .

</details>

---

### 48. [ChemFlow:A Hierarchical Neural Network for Multiscale Representation Learning in Chemical Mixtures](https://arxiv.org/abs/2603.02810)

**基本信息**

- 🔗 arXiv: [`2603.02810`](https://arxiv.org/abs/2603.02810)
- 👥 作者: Jinming Fan, Chao Qian, Wilhelm T. S. Huck 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02810.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于化学混合物性质预测的先进神经网络架构，这是化学信息学和化学大模型领域的前沿研究方向。

**📖 中文摘要**

本文提出了ChemFlow，一种用于化学混合物多尺度表示学习的层次化神经网络框架。该框架集成了原子、官能团和分子级别的特征，通过双向注意力机制促进跨层级的信息流动，并动态调整基于浓度和组成的表示，以预测复杂化学混合物的物理化学性质。ChemFlow在预测浓度依赖性和非依赖性系统性质方面均优于现有模型。这项工作直接针对化学信息学中的一个核心挑战——准确建模分子混合物，其提出的层次化架构和表示学习方法对于构建能够理解复杂化学系统的大模型具有重要价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of the physicochemical properties of molecular mixtures using graph neural networks remains a significant challenge, as it requires simultaneous embedding of intramolecular interactions while accounting for mixture composition (i.e., concentrations and ratios). Existing approaches are ill-equipped to emulate realistic mixture environments, where densely coupled interactions propagate across hierarchical levels - from atoms and functional groups to entire molecules - and where cross-level information exchange is continuously modulated by composition. To bridge the gap between isolated molecules and realistic chemical environments, we present ChemFlow, a novel hierarchical framework that integrates atomic, functional group, and molecular-level features, facilitating information flow across these levels to predict the behavior of complex chemical mixtures. ChemFlow employs an atomic-level feature fusion module, Chem-embed, to generate context-aware atomic representations influenced by the mixture state and atomic characteristics. Next, bidirectional group-to-molecule and molecule-to-group attention mechanisms enable ChemFlow to capture functional group interactions both within and across molecules in the mixture. By dynamically adjusting representations based on concentration and composition, ChemFlow excels at predicting concentration-dependent properties and significantly outperforms state-of-the-art models in both concentration-sensitive and concentration-independent systems. Extensive experiments demonstrate ChemFlow's superior accuracy and efficiency in modeling complex chemical mixtures.

</details>

---

### 49. [Sparse autoencoders reveal organized biological knowledge but minimal regulatory logic in single-cell foundation models: a comparative atlas of Geneformer and scGPT](https://arxiv.org/abs/2603.02952)

**基本信息**

- 🔗 arXiv: [`2603.02952`](https://arxiv.org/abs/2603.02952)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02952.pdf)

**💡 相关性分析**

满足标准3：论文是对生物医学领域基础模型（可视为一类科学大模型）内部表示和知识的系统性分析综述与讨论，其方法论和结论对“化学大模型”的可解释性研究具有重要的参考和展望价值。

**📖 中文摘要**

本研究对单细胞基础模型（Geneformer和scGPT）进行了系统的稀疏自编码器（SAE）分析，以探究这些模型内部编码的生物学知识。研究训练了大规模的SAE，生成了数万个可解释的特征，并发现这些特征具有丰富的生物学组织性，能够注释到基因本体、通路和蛋白质相互作用网络。然而，研究也指出，这些模型虽然内化了大量的生物学关联知识，但对因果调控逻辑的编码非常有限。这项工作展示了利用可解释性技术（如SAE）剖析生物医学领域基础模型内部表示的通用方法，其分析框架和结论对于理解和评估化学领域大模型（例如，用于分子性质预测或反应预测的模型）可能具有借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Background: Single-cell foundation models such as Geneformer and scGPT encode rich biological information, but whether this includes causal regulatory logic rather than statistical co-expression remains unclear. Sparse autoencoders (SAEs) can resolve superposition in neural networks by decomposing dense activations into interpretable features, yet they have not been systematically applied to biological foundation models. Results: We trained TopK SAEs on residual stream activations from all layers of Geneformer V2-316M (18 layers, d=1152) and scGPT whole-human (12 layers, d=512), producing atlases of 82525 and 24527 features, respectively. Both atlases confirm massive superposition, with 99.8 percent of features invisible to SVD. Systematic characterization reveals rich biological organization: 29 to 59 percent of features annotate to Gene Ontology, KEGG, Reactome, STRING, or TRRUST, with U-shaped layer profiles reflecting hierarchical abstraction. Features organize into co-activation modules (141 in Geneformer, 76 in scGPT), exhibit causal specificity (median 2.36x), and form cross-layer information highways (63 to 99.8 percent). When tested against genome-scale CRISPRi perturbation data, only 3 of 48 transcription factors (6.2 percent) show regulatory-target-specific feature responses. A multi-tissue control yields marginal improvement (10.4 percent, 5 of 48 TFs), establishing model representations as the bottleneck. Conclusions: These models have internalized organized biological knowledge, including pathway membership, protein interactions, functional modules, and hierarchical abstraction, yet they encode minimal causal regulatory logic. We release both feature atlases as interactive web platforms enabling exploration of more than 107000 features across 30 layers of two leading single-cell foundation models.

</details>

---

### 50. [From Reachability to Learnability: Geometric Design Principles for Quantum Neural Networks](https://arxiv.org/abs/2603.03071)

**基本信息**

- 🔗 arXiv: [`2603.03071`](https://arxiv.org/abs/2603.03071)
- 👥 作者: Vishal S. Ngairangbam, Michael Spannowsky
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03071.pdf)

**💡 相关性分析**

满足标准3：论文包含对模型表示几何和学习能力的深入理论分析与讨论，虽然针对量子模型，但其核心思想（几何设计原则、特征学习）对于理解和设计复杂的“化学大模型”具有重要的相关性和展望价值。

**📖 中文摘要**

本文从表示几何的角度研究了量子神经网络（QNN）的设计原则。论文指出，与经典深度学习不同，QNN的深度或状态可达性本身并不能保证其具备特征学习能力。通过将编码数据视为复投影空间中的嵌入流形，并分析无穷小酉操作，作者引入了经典到李代数映射和近似完全局部选择性准则。研究表明，要实现几何灵活性（即可学习的特征变形），QNN的参数必须与数据非平凡地共同依赖，并且需要参数化的纠缠方向。这项工作为设计更强大的QNN提供了几何指导原则。虽然主题是量子机器学习，但其关于模型表达能力和几何结构的分析，对于理解任何基于参数化变换的模型（包括某些化学大模型）的学习机制具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Classical deep networks are effective because depth enables adaptive geometric deformation of data representations. In quantum neural networks (QNNs), however, depth or state reachability alone does not guarantee this feature-learning capability. We study this question in the pure-state setting by viewing encoded data as an embedded manifold in $\mathbb{C}P^{2^n-1}$ and analysing infinitesimal unitary actions through Lie-algebra directions. We introduce Classical-to-Lie-algebra (CLA) maps and the criterion of almost Complete Local Selectivity (aCLS), which combines directional completeness with data-dependent local selectivity. Within this framework, we show that data-independent trainable unitaries are complete but non-selective, i.e. learnable rigid reorientations, whereas pure data encodings are selective but non-tunable, i.e. fixed deformations. Hence, geometric flexibility requires a non-trivial joint dependence on data and trainable weights. We further show that accessing high-dimensional deformations of many-qubit state manifolds requires parametrised entangling directions; fixed entanglers such as CNOT alone do not provide adaptive geometric control. Numerical examples validate that CLS-satisfying data re-uploading models outperform non-tunable schemes while requiring only a quarter of the gate operations. Thus, the resulting picture reframes QNN design from state reachability to controllable geometry of hidden quantum representations.

</details>

---

### 51. [Multiparty Quantum Key Agreement: Architectures, State-of-the-art, and Open Problems](https://arxiv.org/abs/2603.03225)

**基本信息**

- 🔗 arXiv: [`2603.03225`](https://arxiv.org/abs/2603.03225)
- 👥 作者: Malik Mouaji, Saif Al-Kuwari
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03225.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对多方量子密钥协商这一特定领域的综述文章，系统性地回顾和展望了该领域的技术发展、设计空间和开放问题。

**📖 中文摘要**

本文对多方量子密钥协商（MQKA）协议进行了全面综述，提出了一个基于网络架构、量子资源和安全模型三维正交轴的设计空间分析框架。论文将现有MQKA协议分类为不同的结构家族，映射到其底层量子资源，并分析了不同安全模型如何影响公平性和抗串谋性。此外，文章还指出了在可组合安全框架、网络原生集成、设备无关实现等方面的开放挑战，并提出了面向后NISQ时代量子互联网部署的研究路线图。这是一篇关于量子密码学特定领域的综述文章。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multiparty quantum key agreement (MQKA) enables $n \geq 3$ mutually distrustful users to establish a shared secret key through collaborative quantum protocols. In this paper, we provide a comprehensive review where we argue that MQKA is best understood as a design space organized along three orthogonal but tightly coupled axes: (1) network architecture, which determines how quantum states flow between participants; (2) quantum resources, which encode the physical degrees of freedom used for implementation; and (3) security model, which defines trust assumptions about devices and infrastructure. Rather than treating MQKA as a linear sequence of isolated protocols, we develop this three-axis perspective to reveal recurrent patterns, sharp trade-offs, and unexplored design spaces. We classify MQKA protocols into structural families, map them to underlying quantum resources, and analyze how different security models shape fairness and collusion resistance. We further identify open challenges in composable security frameworks, network native integration, device-independent implementations, and propose a research roadmap toward hybrid-resource, bosonic-code-encoded, and fairness-aware MQKA suitable for the future quantum internet deployments in the post-NISQ era.

</details>

---

### 52. [Learning Lagrangian Interaction Dynamics with Sampling-Based Model Order Reduction](https://arxiv.org/abs/2407.03925)

**基本信息**

- 🔗 arXiv: [`2407.03925`](https://arxiv.org/abs/2407.03925)
- 👥 作者: Hrishikesh Viswanath, Yue Chang, Aleksey Panas 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.03925.pdf)

**💡 相关性分析**

满足标准2：论文提出的GIOROM框架及其公开的代码和数据，为模拟物理系统（可类比于分子动力学或复杂化学系统）提供了一种新颖的降阶建模工具和数据集，这类数据资源和工具可用于构建或验证化学大模型，或辅助质谱分析中的动力学模拟。

**📖 中文摘要**

本文提出了一种基于采样的模型降阶框架（GIOROM），用于高效模拟由拉格朗日动力学控制的物理系统。该方法通过数据驱动的神经PDE算子直接在物理空间中的粒子上演化系统，从而减少活动自由度。为了能够在任意空间位置进行查询，作者引入了一种可学习的核参数化方法，利用时间演化样本粒子的局部空间信息来推断底层解流形。该方法在包括流体流动在内的多种拉格朗日体系中实现了高保真度评估，同时将输入维度降低了6.6倍至32倍。所有代码和数据均已公开。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Simulating physical systems governed by Lagrangian dynamics often entails solving partial differential equations (PDEs) over high-resolution spatial domains, leading to significant computational expense. Reduced-order modeling (ROM) mitigates this cost by evolving low-dimensional latent representations of the underlying system. While neural ROMs enable querying solutions from latent states at arbitrary spatial points, their latent states typically represent the global domain and struggle to capture localized, highly dynamic behaviors such as fluids. We propose a sampling-based reduction framework that evolves Lagrangian systems directly in physical space over the particles themselves, reducing the number of active degrees of freedom via data-driven neural PDE operators. To enable querying at arbitrary spatial locations, we introduce a learnable kernel parameterization that uses local spatial information from time-evolved sample particles to infer the underlying solution manifold. Empirically, our approach achieves a 6.6x to 32x reduction in input dimensionality while maintaining high-fidelity evaluations across diverse Lagrangian regimes, including fluid flows, granular media, and elastoplastic dynamics. We refer to this framework as GIOROM (Geometry-Informed Reduced-Order Modeling). All code and data are available at: this https URL

</details>

---

### 53. [Regularity and tailored regularization of Deep Neural Networks, with application to parametric PDEs in uncertainty quantification](https://arxiv.org/abs/2502.12496)

**基本信息**

- 🔗 arXiv: [`2502.12496`](https://arxiv.org/abs/2502.12496)
- 👥 作者: Alexander Keller, Frances Y. Kuo, Dirk Nuyens 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.12496.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕深度神经网络（作为大模型的一种）的数学理论、正则化及其在参数化PDE（可类比于化学中的薛定谔方程或分子动力学方程）求解中的应用。这直接涉及构建和理解用于科学计算的“化学大模型”的理论基础和性能保证。

**📖 中文摘要**

本文考虑使用平滑激活函数的深度神经网络作为高维函数的替代模型，这些函数评估成本高昂但具有一定平滑性。作者为标准（非周期）DNN以及新提出的周期DNN模型推导了关于其输入参数的所有混合导数的显式边界。通过限制网络参数以匹配目标函数的正则性特征，作者证明了DNN可以在N个定制构造的格点训练点上实现泛化误差界。该分析被应用于不确定性量化中的参数椭圆PDE流行模型。在数值实验中，作者通过添加定制正则化项来限制训练过程中的网络参数，并展示了对于模拟参数PDE问题的代数方程，采用定制正则化训练的DNN表现显著更好。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper we consider Deep Neural Networks (DNNs) with a smooth activation function as surrogates for high-dimensional functions that are somewhat smooth but costly to evaluate. We consider the standard (non-periodic) DNNs as well as propose a new model of periodic DNNs which are especially suited for a class of periodic target functions when Quasi-Monte Carlo lattice points are used as training points. The primary contribution of this paper is the derivation of explicit bounds for all mixed derivatives of DNNs with respect to their input parameters. The bounds depend on the neural network parameters as well as the choice of activation function, with explicit constants. These bounds are fully general and remain independent of both the target function and the training data. By imposing restrictions on the network parameters to match the regularity features of the target functions, we prove that DNNs with $N$ tailor-constructed lattice training points can achieve the generalization error (or $L_2$ approximation error) bound ${\tt tol} + \mathcal{O}(N^{-r/2})$, where ${\tt tol}\in (0,1)$ is the tolerance achieved by the training error in practice, and $r = 1/p^*$, with $p^*$ being the ``summability exponent'' of a sequence that characterises the decay of the input variables in the target functions, and with the implied constant independent of the dimensionality of the input data. We apply our analysis to popular models of parametric elliptic PDEs in uncertainty quantification. In our numerical experiments, we restrict the network parameters during training by adding tailored regularization terms, and we show that for an algebraic equation mimicking the parametric PDE problems the DNNs trained with tailored regularization perform significantly better.

</details>

---

### 54. [Unsupervised Representation Learning -- an Invariant Risk Minimization Perspective](https://arxiv.org/abs/2505.12506)

**基本信息**

- 🔗 arXiv: [`2505.12506`](https://arxiv.org/abs/2505.12506)
- 👥 作者: Yotam Norman, Ron Meir
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12506.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发无监督的不变表征学习框架（PICA和VIAE），这属于机器学习/深度学习模型构建的前沿领域。所提出的框架旨在学习跨环境稳健的、可解释的潜在表示，这与构建能够从异构化学数据（如不同仪器、条件获得的质谱数据）中学习通用表示的“化学大模型”的目标高度相关。

**📖 中文摘要**

本文提出了一种新颖的无监督不变风险最小化框架，将不变性概念扩展到没有标签可用的场景。传统IRM方法依赖带标签数据来学习跨环境分布偏移下稳健的表征，而本方法通过特征分布对齐重新定义不变性，从而能够从无标签数据中进行稳健的表征学习。作者引入了两种方法：主不变成分分析（PICA），一种在高斯假设下提取不变方向的线性方法；以及变分不变自编码器（VIAE），一种分离环境不变和环境依赖潜在因子的深度生成模型。该方法基于一种新颖的“无监督”结构因果模型，支持环境条件样本生成和干预。在合成数据集、MNIST修改版本和CelebA上的实验证明了该方法在捕获不变结构、保留相关信息以及跨环境泛化方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a novel unsupervised framework for \emph{Invariant Risk Minimization} (IRM), extending the concept of invariance to settings where labels are unavailable. Traditional IRM methods rely on labeled data to learn representations that are robust to distributional shifts across environments. In contrast, our approach redefines invariance through feature distribution alignment, enabling robust representation learning from unlabeled data. We introduce two methods within this framework: Principal Invariant Component Analysis (PICA), a linear method that extracts invariant directions under Gaussian assumptions, and Variational Invariant Autoencoder (VIAE), a deep generative model that separates environment-invariant and environment-dependent latent factors. Our approach is based on a novel ``unsupervised'' structural causal model and supports environment-conditioned sample-generation and intervention. Empirical evaluations on synthetic dataset, modified versions of MNIST, and CelebA demonstrate the effectiveness of our methods in capturing invariant structure, preserving relevant information, and generalizing across environments without access to labels.

</details>

---

### 55. [Deterministic Bounds and Random Estimates of Metric Tensors on Neuromanifolds](https://arxiv.org/abs/2505.13614)

**基本信息**

- 🔗 arXiv: [`2505.13614`](https://arxiv.org/abs/2505.13614)
- 👥 作者: Ke Sun
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13614.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深度神经网络（作为大模型的基础）参数空间的几何结构（神经流形）和Fisher信息度量。对模型参数空间几何和信息的量化理解，是分析和改进“化学大模型”等复杂模型的理论基础，直接关系到模型的可解释性、优化和泛化能力。

**📖 中文摘要**

本文研究了深度神经网络高维参数空间（神经流形）上由Fisher信息定义的独特度量张量。聚焦于神经分类器，作者回到一个低维的概率分布空间（称为核心空间），并检查其Fisher信息矩阵的谱和包络。将这些发现扩展到神经流形上度量张量的确定性边界。作者引入了一种基于Hutchinson迹方法的无偏随机估计器，并推导了相关边界。该估计器可以高效评估，每个批次只需一次反向传播，其标准差以真实值为界（最多缩放）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The high-dimensional parameter space of deep neural networks -- the neuromanifold -- is endowed with a unique metric tensor defined by the Fisher information. Reliable and scalable computation of this metric tensor is valuable for theorists and practitioners. Focusing on neural classifiers, we return to a low-dimensional space of probability distributions, which we call the core space, and examine the spectrum and envelopes of its Fisher information matrix. We extend our discoveries there to deterministic bounds for the metric tensor on the neuromanifold. We introduce an unbiased random estimator based on Hutchinson's trace method and derive related bounds. It can be evaluated efficiently with a single backward pass per batch, with a standard deviation bounded by the true value up to scaling.

</details>

---

### 56. [Automatic and Structure-Aware Sparsification of Hybrid Neural ODEs](https://arxiv.org/abs/2505.18996)

**基本信息**

- 🔗 arXiv: [`2505.18996`](https://arxiv.org/abs/2505.18996)
- 👥 作者: Bob Junyi Zou, Lu Tian
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.18996.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是“混合神经ODE”，这是一种将领域知识（机制模型）与神经网络相结合的特定类型模型。这种模型架构和优化方法（自动状态选择、结构稀疏化）对于构建集成物理化学原理与数据驱动学习的“化学大模型”（例如，用于反应预测或分子性质计算的混合模型）具有直接的启发和参考价值。

**📖 中文摘要**

本文提出了一个新的混合流程，用于机制神经ODE中的自动状态选择和结构优化。混合神经ODE将机制模型与神经ODE相结合，在数据稀缺的医疗保健设置中具有优势。然而，机制模型带来的过多潜在状态和相互作用可能导致训练效率低下和过拟合。为了解决这个问题，作者结合了领域知识引导的图修改和数据驱动的正则化，以稀疏化模型，在保留机制合理性的同时提高预测性能和稳定性。在合成数据和真实世界数据上的实验显示了改进的预测性能、鲁棒性和期望的稀疏性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hybrid neural ordinary differential equations (neural ODEs) integrate mechanistic models with neural ODEs, offering strong inductive bias and flexibility, and are particularly advantageous in data-scarce healthcare settings. However, excessive latent states and interactions from mechanistic models can lead to training inefficiency and over-fitting, limiting practical effectiveness of hybrid neural ODEs. In response, we propose a new hybrid pipeline for automatic state selection and structure optimization in mechanistic neural ODEs, combining domain-informed graph modifications with data-driven regularization to sparsify the model for improving predictive performance and stability while retaining mechanistic plausibility. Experiments on synthetic and real-world data show improved predictive performance and robustness with desired sparsity, establishing an effective solution for hybrid model reduction in healthcare applications.

</details>

---

### 57. [Learning of Population Dynamics: Inverse Optimization Meets JKO Scheme](https://arxiv.org/abs/2506.01502)

**基本信息**

- 🔗 arXiv: [`2506.01502`](https://arxiv.org/abs/2506.01502)
- 👥 作者: Mikhail Persiianov, Jiawei Chen, Petr Mokrov 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.01502.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发新的机器学习框架（iJKOnet）来学习“群体动力学”。虽然论文背景是通用粒子系统，但其方法论（结合JKO格式和逆优化）完全适用于学习分子群体在化学反应或相变中的演化动力学，这与“化学大模型”中模拟复杂系统行为的目标高度相关。

**📖 中文摘要**

本文提出了iJKOnet方法，将JKO框架与逆优化技术相结合来学习群体动力学。学习群体动力学涉及在给定离散时间点样本演化快照的情况下，恢复控制粒子演化的底层过程。最近的方法将其视为概率空间中的能量最小化问题，并利用著名的JKO方案进行高效时间离散化。iJKOnet方法依赖于传统的端到端对抗训练过程，不需要限制性的架构选择（例如输入凸神经网络）。作者为该方法的理论提供了保证，并证明了其性能优于先前基于JKO的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning population dynamics involves recovering the underlying process that governs particle evolution, given evolutionary snapshots of samples at discrete time points. Recent methods frame this as an energy minimization problem in probability space and leverage the celebrated JKO scheme for efficient time discretization. In this work, we introduce $\texttt{iJKOnet}$, an approach that combines the JKO framework with inverse optimization techniques to learn population dynamics. Our method relies on a conventional $\textit{end-to-end}$ adversarial training procedure and does not require restrictive architectural choices, e.g., input-convex neural networks. We establish theoretical guarantees for our methodology and demonstrate improved performance over prior JKO-based methods. The code of $\texttt{iJKOnet}$ is available at this https URL .

</details>

---

### 58. [Interaction Field Matching: Overcoming Limitations of Electrostatic Models](https://arxiv.org/abs/2506.02950)

**基本信息**

- 🔗 arXiv: [`2506.02950`](https://arxiv.org/abs/2506.02950)
- 👥 作者: Stepan I. Manukhov, Alexander Kolesov, Vladimir V. Palyulin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.02950.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的、受物理学启发的数据生成和迁移范式（IFM）。虽然论文以图像数据为例，但其核心思想——利用物理相互作用场（如强相互作用）的类比来构建生成模型——为开发新型的、具有物理意义的分子生成或质谱数据增强的“化学大模型”提供了创新的方法论视角。

**📖 中文摘要**

本文提出了交互场匹配（IFM），作为静电场匹配（EFM）的推广，允许使用超越静电场的通用交互场。受物理学中夸克和反夸克之间强相互作用的启发，作者设计了一种特定的交互场实现，解决了在EFM中建模静电场时出现的问题。作者在一系列玩具和图像数据迁移问题上展示了其性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electrostatic field matching (EFM) has recently appeared as a novel physics-inspired paradigm for data generation and transfer using the idea of an electric capacitor. However, it requires modeling electrostatic fields using neural networks, which is non-trivial because of the necessity to take into account the complex field outside the capacitor plates. In this paper, we propose Interaction Field Matching (IFM), a generalization of EFM which allows using general interaction fields beyond the electrostatic one. Furthermore, inspired by strong interactions between quarks and antiquarks in physics, we design a particular interaction field realization which solves the problems which arise when modeling electrostatic fields in EFM. We show the performance on a series of toy and image data transfer problems. Our code is available at this https URL

</details>

---

### 59. [RNE: plug-and-play diffusion inference-time control and energy-based training](https://arxiv.org/abs/2506.05668)

**基本信息**

- 🔗 arXiv: [`2506.05668`](https://arxiv.org/abs/2506.05668)
- 👥 作者: Jiajun He, José Miguel Hernández-Lobato, Yuanqi Du 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.05668.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对扩散模型提出一种新的理论框架（RNE），用于密度估计、推理时间控制和能量模型训练。扩散模型是当前生成式AI大模型的核心支柱之一。该工作提供的统一视角和增强控制能力，对于构建用于分子生成、质谱图生成或逆合成规划的“化学大模型”具有重要的方法论价值。

**📖 中文摘要**

本文介绍了Radon-Nikodym估计器（RNE），基于路径分布之间的“密度比”概念，揭示了边缘密度和转移核之间的基本联系，提供了一个灵活的即插即用框架，将（1）扩散密度估计、（2）推理时间控制和（3）基于能量的扩散训练统一在一个视角下。实验表明，RNE在推理时间控制应用（如退火和模型组合）中提供了强大的结果，并具有有前景的推理时间缩放性能，同时为训练基于能量的扩散模型实现了一种简单而高效的正则化。此外，RNE是模态无关的，不仅适用于连续扩散模型，也适用于其离散扩散对应模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models generate data by removing noise gradually, which corresponds to the time-reversal of a noising process. However, access to only the denoising kernels is often insufficient. In many applications, we need the knowledge of the marginal densities along the generation trajectory, which enables tasks such as inference-time control. To address this gap, in this paper, we introduce the Radon-Nikodym Estimator (RNE). Based on the concept of the \textit{density ratio} between path distributions, it reveals a fundamental connection between marginal densities and transition kernels, providing a flexible plug-and-play framework that unifies (1) diffusion density estimation, (2) inference-time control, and (3) energy-based diffusion training under a single perspective. Experiments demonstrate that RNE delivers strong results in inference-time control applications, such as annealing and model composition, with promising inference-time scaling performance, and achieves a simple yet efficient regularisation for training energy-based diffusion models. Additionally, our proposed RNE is modality-agnostic and applicable not only to continuous diffusion models but also to their discrete diffusion counterparts.

</details>

---

### 60. [Federated ADMM from Bayesian Duality](https://arxiv.org/abs/2506.13150)

**基本信息**

- 🔗 arXiv: [`2506.13150`](https://arxiv.org/abs/2506.13150)
- 👥 作者: Thomas Möllenhoff, Siddharth Swaroop, Finale Doshi-Velez 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.13150.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的贝叶斯框架来推广和增强联邦ADMM算法。联邦学习是训练跨机构、跨实验室大模型（如化学大模型）的关键分布式学习范式，而ADMM是其中重要的优化工具。这项工作通过贝叶斯视角提供了更强大、更灵活的优化方法，直接关系到如何高效、稳健地训练分布式“化学大模型”。

**📖 中文摘要**

本文提出了一种新的贝叶斯方法来推广联邦交替方向乘子法（ADMM）。作者展示了变分贝叶斯（VB）目标的解与一种对偶结构相关联，这种结构不仅类似于ADMM不动点的结构，而且推广了它。例如，当在各项同性高斯族上优化VB目标时，可以恢复类似ADMM的更新；而对于其他指数族分布，则获得新的非平凡扩展。这些扩展包括一个在二次目标上一步收敛的类牛顿变体，以及一个在深度异构情况下能带来高达7%准确率提升的类Adam变体。这项工作为推广ADMM和其他原始-对偶方法开辟了一条新的贝叶斯途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Bayesian approach to generalize the federated Alternating Direction Method of Multipliers (ADMM). We show that the solutions of variational-Bayesian (VB) objectives are associated with a duality structure that not only resembles the structure of ADMM's fixed-points but also generalizes it. For example, ADMM-like updates are recovered when the VB objective is optimized over the isotropic-Gaussian family, and new non-trivial extensions are obtained for other exponential-family distributions. These extensions include a Newton-like variant that converges in one step on quadratic objectives and an Adam-like variant that yields up to 7% accuracy boosts for deep heterogeneous cases. Our work opens a new Bayesian way to generalize ADMM and other primal-dual methods.

</details>

---

### 61. [Prior-based Noisy Text Data Filtering: Fast and Strong Alternative For Perplexity](https://arxiv.org/abs/2509.18577)

**基本信息**

- 🔗 arXiv: [`2509.18577`](https://arxiv.org/abs/2509.18577)
- 👥 作者: Yeongbin Seo, Gayoung Kim, Jaehyung Kim 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.18577.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效、可扩展的文本数据过滤方法，该方法可用于构建高质量、领域特定的训练数据集。对于训练化学大模型或处理质谱相关的文本/符号数据（如分子描述、光谱解释文本），这种数据预处理和清洗工具是重要的数据资源构建环节。

**📖 中文摘要**

这篇论文提出了一种基于先验的噪声文本数据过滤方法，作为困惑度（PPL）过滤的快速且强大的替代方案。该方法利用语料库级别的词频统计来估计词元先验，并基于词元先验的均值和标准差来过滤文档。其核心思想是，文档中词元的先验分布可以作为其语言质量的代理指标，而无需运行模型进行推理。该方法在20个下游基准测试中取得了最高的平均性能，同时将时间成本降低了超过1000倍。论文还展示了该方法对代码和数学等符号语言以及多语言语料库的适用性。虽然论文主要关注LLM预训练数据筛选，但其提出的基于统计先验的过滤框架，为构建高质量、领域特定的训练数据集（例如用于化学信息学或质谱分析领域的文本或符号数据）提供了一种高效、可扩展的工具。这符合“数据资源相关”的标准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As large language models (LLMs) are pretrained on massive web corpora, careful selection of data becomes essential to ensure effective and efficient learning. While perplexity (PPL)-based filtering has shown strong performance, it suffers from drawbacks: substantial time costs and inherent unreliability of the model when handling noisy or out-of-distribution samples. In this work, we propose a simple yet powerful alternative: a prior-based data filtering method that estimates token priors using corpus-level term frequency statistics, inspired by linguistic insights on word roles and lexical density. Our approach filters documents based on the mean and standard deviation of token priors, serving as a fast proxy to PPL while requiring no model inference. Despite its simplicity, the prior-based filter achieves the highest average performance across 20 downstream benchmarks, while reducing time cost by over 1000x compared to PPL-based filtering. We further demonstrate its applicability to symbolic languages such as code and math, and its dynamic adaptability to multilingual corpora without supervision

</details>

---

### 62. [Bridging Kolmogorov Complexity and Deep Learning: Asymptotically Optimal Description Length Objectives for Transformers](https://arxiv.org/abs/2509.22445)

**基本信息**

- 🔗 arXiv: [`2509.22445`](https://arxiv.org/abs/2509.22445)
- 👥 作者: Peter Shaw, James Cohan, Jacob Eisenstein 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.22445.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕为神经网络（特别是Transformer）建立理论框架以实现“最优压缩”和泛化。这直接关联到“化学大模型”主题中关于模型架构、训练目标（如高效学习分子表示）和泛化能力的基础研究。

**📖 中文摘要**

本文基于柯尔莫哥洛夫复杂性和最小描述长度（MDL）原理，为Transformer等神经网络引入了“渐近最优描述长度目标”的理论概念。作者证明，对于Transformer，存在这样的目标，其最小化器能在模型资源边界增加时，对任何数据集实现最优压缩（达到一个加性常数）。论文进一步构建并分析了一个基于自适应高斯混合先验的变分目标，使其易于处理且可微分。实证分析表明，该变分目标能在算法任务中选择低复杂度解并实现强泛化。这项工作为识别具有强渐近保证的描述长度目标提供了一个理论框架，为训练实现更高压缩和泛化能力的神经网络（包括可能用于分子表示、光谱数据建模的大模型）指明了一条潜在路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Minimum Description Length (MDL) principle offers a formal framework for applying Occam's razor in machine learning. However, its application to neural networks such as Transformers is challenging due to the lack of a principled, universal measure for model complexity. This paper introduces the theoretical notion of asymptotically optimal description length objectives, grounded in the theory of Kolmogorov complexity. We establish that a minimizer of such an objective achieves optimal compression, for any dataset, up to an additive constant, in the limit as model resource bounds increase. We prove that asymptotically optimal objectives exist for Transformers, building on a new demonstration of their computational universality. We further show that such objectives can be tractable and differentiable by constructing and analyzing a variational objective based on an adaptive Gaussian mixture prior. Our empirical analysis shows that this variational objective selects for a low-complexity solution with strong generalization on an algorithmic task, but standard optimizers fail to find such solutions from a random initialization, highlighting key optimization challenges. More broadly, by providing a theoretical framework for identifying description length objectives with strong asymptotic guarantees, we outline a potential path towards training neural networks that achieve greater compression and generalization.

</details>

---

### 63. [Death of the Novel(ty): Beyond n-Gram Novelty as a Metric for Textual Creativity](https://arxiv.org/abs/2509.22641)

**基本信息**

- 🔗 arXiv: [`2509.22641`](https://arxiv.org/abs/2509.22641)
- 👥 作者: Arkadiy Saakyan, Najoung Kim, Smaranda Muresan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.22641.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和批判用于衡量大语言模型（LLMs）生成能力（特别是创造性和新颖性）的指标。这直接关系到“化学大模型”主题中模型能力的评估，例如评估模型生成新颖、合理分子结构或反应路径的能力，需要超越简单n-gram匹配的、更全面的评估框架。

**📖 中文摘要**

本文批判性地评估了将n-gram新颖性作为衡量语言模型文本创造力和生成训练数据外文本能力的指标的充分性。基于创造力理论，作者指出创造力包含新颖性和适当性两个维度，而n-gram新颖性无法捕捉后者。通过对8618份人类和AI生成文本的专家标注进行分析，发现虽然n-gram新颖性与专家评判的创造力正相关，但约91%的高n-gram新颖性表达并未被判定为有创造力。此外，在开源LLM中，更高的n-gram新颖性与更低的实用性相关。研究还测试了LLM识别专家认为新颖或非实用表达的能力。这项工作对如何评估生成模型（包括大语言模型）的“创造性”输出提出了重要见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

N-gram novelty is widely used to evaluate language models' ability to generate text outside of their training data. More recently, it has also been adopted as a metric for measuring textual creativity. However, theoretical work on creativity suggests that this approach may be inadequate, as it does not account for creativity's dual nature: novelty (how original the text is) and appropriateness (how sensical and pragmatic it is). We investigate the relationship between this notion of creativity and n-gram novelty through 8,618 expert writer annotations of novelty, pragmaticality, and sensicality via close reading of human- and AI-generated text. We find that while n-gram novelty is positively associated with expert writer-judged creativity, approximately 91% of top-quartile n-gram novel expressions are not judged as creative, cautioning against relying on n-gram novelty alone. Furthermore, unlike in human-written text, higher n-gram novelty in open-source LLMs correlates with lower pragmaticality. In an exploratory study with frontier closed-source models, we additionally confirm that they are less likely to produce creative expressions than humans. Using our dataset, we test whether zero-shot, few-shot, and finetuned models are able to identify expressions perceived as novel by experts (a positive aspect of writing) or non-pragmatic (a negative aspect). Overall, frontier LLMs exhibit performance much higher than random but leave room for improvement, especially struggling to identify non-pragmatic expressions. We further find that LLM-as-a-Judge novelty ratings align with expert writer preferences in an out-of-distribution dataset, more so than an n-gram based metric.

</details>

---

### 64. [LaDiR: Latent Diffusion Enhances LLMs for Text Reasoning](https://arxiv.org/abs/2510.04573)

**基本信息**

- 🔗 arXiv: [`2510.04573`](https://arxiv.org/abs/2510.04573)
- 👥 作者: Haoqiang Kang, Yizhe Zhang, Nikki Lijing Kuang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04573.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、基于潜在扩散的推理框架来增强大语言模型的推理能力。这直接关联到“化学大模型”和“质谱结构推理”主题，因为复杂的化学推理（如逆合成分析、分子性质预测）和质谱解析都需要多步骤、可迭代、可规划的推理过程。LaDiR提供了一种可能适用于这些领域的新型推理架构范式。

**📖 中文摘要**

本文提出了LaDiR（潜在扩散推理器），一种新颖的推理框架，将连续潜在表示的表达能力与潜在扩散模型的迭代优化能力相结合，用于增强现有大语言模型（LLMs）的推理。该框架首先使用变分自编码器（VAE）构建一个结构化的潜在推理空间，将文本推理步骤编码为“思维块”标记。然后，利用一个潜在扩散模型去噪潜在思维块，该模型采用块间双向注意力掩码，支持长程规划和迭代优化。这种设计允许高效并行生成多样化的推理轨迹，使模型能够整体规划和修订推理过程。在数学推理和规划基准测试上的实验表明，LaDiR在准确性、多样性和可解释性上均优于现有的自回归、基于扩散和潜在推理方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) demonstrate their reasoning ability through chain-of-thought (CoT) generation. However, LLM's autoregressive decoding may limit the ability to revisit and refine earlier tokens in a holistic manner, which can also lead to inefficient exploration for diverse solutions. In this paper, we propose LaDiR (Latent Diffusion Reasoner), a novel reasoning framework that unifies the expressiveness of continuous latent representation with the iterative refinement capabilities of latent diffusion models for an existing LLM. We first construct a structured latent reasoning space using a Variational Autoencoder (VAE) that encodes text reasoning steps into blocks of thought tokens, preserving semantic information and interpretability while offering compact but expressive representations. Subsequently, we utilize a latent diffusion model that learns to denoise a block of latent thought tokens with a blockwise bidirectional attention mask, enabling longer horizon and iterative refinement with adaptive test-time compute. This design allows efficient parallel generation of diverse reasoning trajectories, allowing the model to plan and revise the reasoning process holistically. We conduct evaluations on a suite of mathematical reasoning and planning benchmarks. Empirical results show that LaDiR consistently improves accuracy, diversity, and interpretability over existing autoregressive, diffusion-based, and latent reasoning methods, revealing a new paradigm for text reasoning with latent diffusion.

</details>

---

### 65. [Off-Trajectory Reasoning: Can LLMs Collaborate on Reasoning Trajectory?](https://arxiv.org/abs/2510.06410)

**基本信息**

- 🔗 arXiv: [`2510.06410`](https://arxiv.org/abs/2510.06410)
- 👥 作者: Aochong Oliver Li, Tanya Goyal
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.06410.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和剖析大语言模型在复杂、协作式推理场景下的能力边界，特别是它们处理、评估和整合外部推理步骤的能力。这对于构建用于“化学大模型”或“质谱结构推理”的专家协作系统或迭代优化系统具有直接相关性，因为在这些领域，模型可能需要与人类专家或其他专业模型的推理进行交互和整合。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）在“轨迹外推理”方面的能力，即评估其他模型的局部推理过程是否有用并在此基础上进行构建的能力，这是多模型在共享推理轨迹上进行协作的关键前提。作者提出了两个测试来捕捉轨迹外推理的两个极端：可恢复性（测试LLMs能否从误导性推理痕迹的“干扰”中回溯）和可引导性（测试LLMs能否在更强协作者的正确推理基础上进行构建）。对15个开源LLMs（1.5B-32B）的评估揭示了一个反直觉的发现：基准测试上“更强”的LLMs在干扰下往往更脆弱。此外，所有测试模型都未能有效利用协作者的引导步骤来解决超出其固有能力的问题。论文还分析了后训练中三个因素对这些行为的影响。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning LLMs are trained to verbalize their reasoning process, yielding strong gains on complex tasks. This transparency also opens a promising direction: multiple reasoners can directly collaborate on each other's thinking within a shared trajectory, yielding better inference efficiency and exploration. A key prerequisite, however, is the ability to assess the usefulness and build on another model's partial thinking -- we call this off-trajectory reasoning. Our paper investigates a critical question: can standard solo-reasoning training pipelines deliver desired off-trajectory behaviors? We propose twin tests that capture the two extremes of the off-trajectory spectrum, namely Recoverability, which tests whether LLMs can backtrack from "distractions" induced by misleading reasoning traces, and Guidability, which tests their ability to build upon correct reasoning from stronger collaborators. Our study evaluates 15 open-weight LLMs (1.5B-32B) and reveals a counterintuitive finding -- "stronger" LLMs on benchmarks are often more fragile under distraction. Moreover, all models tested fail to effectively leverage guiding steps from collaborators on problems beyond their inherent capabilities with solve rates remaining under 9.2%. Finally, we conduct control studies to isolate the effects of three factors in post-training on these behaviors: the choice of distillation teacher, the use of RL, and data selection strategy. Our results provide actionable insights for training natively strong reasoning collaborators; e.g., we find that suboptimal recoverability behaviors of teacher models are transferred to distilled students even if the distillation trajectories are correct. Taken together, this work lays the groundwork for evaluating multi-model collaborations in shared reasoning trajectories and highlights the limitations of off-the-shelf reasoning LLMs.

</details>

---

### 66. [Mitigating Over-Refusal in Aligned Large Language Models via Inference-Time Activation Energy](https://arxiv.org/abs/2510.08646)

**基本信息**

- 🔗 arXiv: [`2510.08646`](https://arxiv.org/abs/2510.08646)
- 👥 作者: Eric Hanchen Jiang, Weixuan Ou, Run Liu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.08646.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过创新的推理时干预方法来解决大语言模型对齐中的关键挑战——过度拒绝。虽然主题是通用LLM安全，但其提出的“能量景观引导”框架作为一种模型行为控制机制，对于确保“化学大模型”在生成分子建议或分析光谱数据时的安全、可靠输出具有方法论上的参考价值，可以防止模型因过度保守而拒绝合理的查询或生成任务。

**📖 中文摘要**

本文提出了能量景观引导（ELS），一种无需微调的推理时干预框架，旨在缓解对齐后大语言模型（LLMs）的过度拒绝问题（即错误拒绝良性请求）。ELS训练一个轻量级的外部能量模型（EBM），为不良状态（错误拒绝或越狱）分配高能量，为理想状态（有帮助的响应或安全拒绝）分配低能量。在推理时，EBM将LLM的内部激活映射到一个能量景观，并使用能量函数的梯度实时引导隐藏状态向低能量区域移动。这种方法动态地引导模型行为，而不修改其参数。实验表明，ELS能将ORB-H基准上的合规率从57.3%提升到82.6%，同时保持基线安全性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Safety alignment of large language models currently faces a central challenge: existing alignment techniques often prioritize mitigating responses to harmful prompts at the expense of overcautious behavior, leading models to incorrectly refuse benign requests. A key goal of safe alignment is therefore to improve safety while simultaneously minimizing false refusals. In this work, we introduce Energy Landscape Steering (ELS), a novel, fine-tuning free framework designed to resolve this challenge through dynamic, inference-time intervention. We train a lightweight external Energy-Based Model (EBM) to assign high energy to undesirable states (false refusal or jailbreak) and low energy to desirable states (helpful response or safe reject). During inference, the EBM maps the LLM's internal activations to an energy landscape, and we use the gradient of the energy function to steer the hidden states toward low-energy regions in real time. This dynamically guides the model toward desirable behavior without modifying its parameters. By decoupling behavioral control from the model's core knowledge, ELS provides a flexible and computationally efficient solution. Extensive experiments across diverse models demonstrate its effectiveness, raising compliance on the ORB-H benchmark from 57.3 percent to 82.6 percent while maintaining baseline safety performance. Our work establishes a promising paradigm for building LLMs that simultaneously achieve high safety and low false refusal rates.

</details>

---

### 67. [Every Language Model Has a Forgery-Resistant Signature](https://arxiv.org/abs/2510.14086)

**基本信息**

- 🔗 arXiv: [`2510.14086`](https://arxiv.org/abs/2510.14086)
- 👥 作者: Matthew Finlayson, Xiang Ren, Swabha Swayamdipta
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.14086.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是发现并利用语言模型内在的几何特性（椭球约束）作为模型指纹和输出认证机制。这直接关联到“化学大模型”的可靠性、可追溯性和安全部署。例如，在生成分子结构或预测性质时，确保输出源自可信的、特定的专业模型，防止模型混淆或恶意篡改，是至关重要的。

**📖 中文摘要**

本文揭示了所有语言模型都具有一种难以伪造的签名——其输出位于高维椭球面上。这种椭球签名源于语言模型架构和参数施加的几何约束。作者展示了该签名可用于识别给定输出的源模型，并且具有难以伪造、自然存在、自包含和紧凑冗余的特性。论文评估了一种从小型模型中提取椭球的新技术，并讨论了其在生产级模型中的实际障碍。最后，作者利用椭球签名提出了一种语言模型输出验证协议，类似于密码学中的对称密钥消息认证系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The ubiquity of closed-weight language models with public-facing APIs has generated interest in forensic methods, both for extracting hidden model details (e.g., parameters) and for identifying models by their outputs. One successful approach to these goals has been to exploit the geometric constraints imposed by the language model architecture and parameters. In this work, we show that a lesser-known geometric constraint -- namely, that language model outputs lie on the surface of a high-dimensional ellipse -- functions as a signature for the model and can be used to identify the source model of a given output. This ellipse signature has unique properties that distinguish it from existing model-output association methods like language model fingerprints. In particular, the signature is hard to forge: without direct access to model parameters, it is practically infeasible to produce log-probabilities (logprobs) on the ellipse using currently known methods. Secondly, the signature is naturally occurring, since all language models have these elliptical constraints. Thirdly, the signature is self-contained, in that it is detectable without access to the model inputs or the full weights. Finally, the signature is compact and redundant, as it is independently detectable in each logprob output from the model. We evaluate a novel technique for extracting the ellipse from small models and discuss the practical hurdles that make it infeasible for production-scale models. Finally, we use ellipse signatures to propose a protocol for language model output verification, analogous to cryptographic symmetric-key message authentication systems.

</details>

---

### 68. [STARS: Synchronous Token Alignment for Robust Supervision in Large Language Models](https://arxiv.org/abs/2511.03827)

**基本信息**

- 🔗 arXiv: [`2511.03827`](https://arxiv.org/abs/2511.03827)
- 👥 作者: Mohammad Atif Quamar, Mohammad Areeb, Mikhail Kuznetsov 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.03827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一种新的、高效的解码时算法，以更可靠和系统高效的方式对齐大语言模型。这对于确保“化学大模型”在生成内容时的安全性、可靠性和符合领域规范（例如，不生成危险分子或不提供错误的谱图解析）具有直接意义。其提升吞吐量的特点也符合大规模部署化学模型的需求。

**📖 中文摘要**

本文提出了STARS（同步令牌对齐鲁棒监督），一种解码时算法，用于提升大语言模型（LLMs）的对齐可靠性。针对现有推理时对齐技术依赖模型不确定性进行分割所导致的（a）易受错误校准的自信幻觉影响和（b）由于异步、参差不齐的批处理导致的硬件利用率低这两个关键限制，STARS通过在固定时间间隔强制执行验证来引导生成，从而将分割与置信度解耦。这使得STARS能够实现锁步并行执行，并鲁棒地检测不确定性度量可能遗漏的错误。在HH-RLHF基准测试中，STARS实现了与最先进动态方法相竞争的对齐质量，同时严格限制了拒绝成本并最大化系统吞吐量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Aligning large language models (LLMs) with human values is crucial for safe deployment. Inference-time techniques offer granular control over generation; however, they rely on model uncertainty, meaning an internal estimate of how likely the model believes its next tokens or outputs are correct, for segmentation. We show that this introduces two critical limitations: (a) vulnerability to miscalibrated confident hallucinations and (b) poor hardware utilization due to asynchronous, ragged batch processing. Together, these issues reduce alignment reliability while increasing token and compute costs, which limits their practical scalability. To address these limitations, building on dynamic inference-time alignment methods, we introduce STARS, Synchronous Token Alignment for Robust Supervision, a decoding-time algorithm, which steers generation by enforcing verification at fixed-horizon intervals. By decoupling segmentation from confidence, STARS enables lockstep parallel execution and robustly detects errors that uncertainty metrics miss. On the HH-RLHF benchmark, we demonstrate that STARS achieves competitive alignment quality with that of state-of-the-art dynamic methods, while strictly bounding rejection costs and maximizing system throughput. Furthermore, it outperforms fine-tuning and several state-of-the-art inference-time decoding strategies by good margins, and establishes fixed-horizon sampling as a robust, system-efficient alternative for aligning LLMs at scale. The code is publicly available at this https URL .

</details>

---

### 69. [Continual Unlearning for Text-to-Image Diffusion Models: A Regularization Perspective](https://arxiv.org/abs/2511.07970)

**基本信息**

- 🔗 arXiv: [`2511.07970`](https://arxiv.org/abs/2511.07970)
- 👥 作者: Justin Lee, Zheda Mai, Jinsu Yoo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.07970.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对生成模型（扩散模型）的持续遗忘学习这一新兴且重要的问题。虽然以图像生成为例，但其提出的正则化和梯度投影方法为解决“化学大模型”或“质谱推理模型”中可能面临的类似问题（例如，需要从已部署模型中顺序移除有问题的训练数据或错误关联）提供了重要的方法论参考和理论基础。

**📖 中文摘要**

本文首次系统研究了文本到图像扩散模型中的持续遗忘学习问题，即按顺序处理多个遗忘请求。作者发现流行的遗忘方法在持续设置下会遭受快速的效用崩溃：仅经过几个请求后，模型就会忘记保留的知识并生成质量下降的图像。作者将这种失败归因于从预训练权重开始的累积参数漂移，并认为正则化对于解决此问题至关重要。为此，作者研究了一系列附加正则化器，以（1）减轻漂移，（2）保持与现有遗忘方法的兼容性。除了通用正则化器，作者还提出了一种梯度投影方法，将参数漂移约束在与其子空间正交的方向上，这显著提高了持续遗忘性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine unlearning--the ability to remove designated concepts from a pre-trained model--has advanced rapidly, particularly for text-to-image diffusion models. However, existing methods typically assume that unlearning requests arrive all at once, whereas in practice they often arrive sequentially. We present the first systematic study of continual unlearning in text-to-image diffusion models and show that popular unlearning methods suffer from rapid utility collapse: after only a few requests, models forget retained knowledge and generate degraded images. We trace this failure to cumulative parameter drift from the pre-training weights and argue that regularization is crucial to addressing it. To this end, we study a suite of add-on regularizers that (1) mitigate drift and (2) remain compatible with existing unlearning methods. Beyond generic regularizers, we show that semantic awareness is essential for preserving concepts close to the unlearning target, and propose a gradient-projection method that constrains parameter drift orthogonal to their subspace. This substantially improves continual unlearning performance and is complementary to other regularizers for further gains. Taken together, our study establishes continual unlearning as a fundamental challenge in text-to-image generation and provides insights, baselines, and open directions for advancing safe and accountable generative AI.

</details>

---

### 70. [TransactionGPT](https://arxiv.org/abs/2511.08939)

**基本信息**

- 🔗 arXiv: [`2511.08939`](https://arxiv.org/abs/2511.08939)
- 👥 作者: Yingtong Dou, Zhimeng Jiang, Tianyi Zhang 等29人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.08939.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是针对特定领域（交易数据）构建大规模基础模型，并设计了专门的3D-Transformer架构。这直接展示了“化学大模型”主题中“为特定科学领域构建专用大模型”的研究范式。同时，论文中构建的模型架构、训练方法和评估方案，为在化学信息学或质谱分析领域构建类似的基础模型（例如，用于分子序列、光谱图序列或反应轨迹的建模）提供了宝贵的经验、技术参考和潜在的架构灵感。

**📖 中文摘要**

本文提出了TransactionGPT（TGPT），一个为全球最大支付网络之一的消费者交易数据设计的基础模型。TGPT旨在理解和生成交易轨迹，同时支持各种下游预测和分类任务。论文引入了一种新颖的3D-Transformer架构，专门用于捕捉支付交易数据中的复杂动态。该架构包含了增强模态融合和计算效率的设计创新，并能无缝实现与下游目标的联合优化。在十亿级真实世界交易数据上训练的TGPT，在下游异常交易检测性能上显著优于竞争的生产模型，并在生成未来交易方面展现出优势。论文还评估了在TGPT中融入LLM衍生嵌入的效果，并与微调的LLMs进行性能比较，证明TGPT实现了更优的预测准确性以及更快的训练和推理速度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present TransactionGPT (TGPT), a foundation model for consumer transaction data within one of the world's largest payment networks. TGPT is designed to understand and generate transaction trajectories while simultaneously supporting a variety of downstream prediction and classification tasks. We introduce a novel 3D-Transformer architecture specifically tailored for capturing the complex dynamics in payment transaction data. This architecture incorporates design innovations that enhance modality fusion and computational efficiency, while seamlessly enabling joint optimization with downstream objectives. Trained on billion-scale real-world transactions, TGPT significantly improves downstream anomaly transaction detection performance against a competitive production model and exhibits advantages over baselines in generating future transactions. We conduct extensive empirical evaluations utilizing a diverse collection of company transaction datasets spanning multiple downstream tasks, thereby enabling a thorough assessment of TGPT's effectiveness and efficiency in comparison to established methodologies. Furthermore, we examine the incorporation of LLM-derived embeddings within TGPT and benchmark its performance against fine-tuned LLMs, demonstrating that TGPT achieves superior predictive accuracy as well as faster training and inference. We anticipate that the architectural innovations and practical guidelines from this work will advance foundation models for transaction-like data and catalyze future research in this emerging field.

</details>

---

### 71. [SURFACEBENCH: A Geometry-Aware Benchmark for Symbolic Surface Discovery](https://arxiv.org/abs/2511.10833)

**基本信息**

- 🔗 arXiv: [`2511.10833`](https://arxiv.org/abs/2511.10833)
- 👥 作者: Sanchit Kabra, Shobhnik Kriplani, Parshin Shojaee 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.10833.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于评估LLM等模型在符号回归（可视为一种科学大模型推理）任务上的基准数据集SURFACEBENCH，这为化学大模型在结构推理方面的能力评估提供了数据资源和工具。

**📖 中文摘要**

这篇论文介绍了SURFACEBENCH，一个用于三维曲面符号发现的首个几何感知基准。虽然其核心任务是符号回归和方程发现，但它明确评估了大型语言模型（LLM）在符号回归任务上的表现，并将其与进化算法和神经网络方法进行了比较。论文指出LLM方法在符号回归中显示出潜力，但现有基准主要评估低维标量函数，而SURFACEBENCH则专注于需要多变量耦合和几何结构推理的三维曲面。这直接关系到“化学大模型”主题，因为化学信息学和分子建模中，从光谱或结构数据中推断出符号化的数学关系（如势能面、结构-性质关系）是一个核心挑战。该基准提供了评估LLM等模型在复杂科学符号推理能力的数据集和评估框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equation discovery from data is a central challenge in machine learning for science, which requires the recovery of concise symbolic expressions that govern complex physical and geometric phenomena. Recent large language model (LLM) approaches have shown promise in symbolic regression, yet existing benchmarks predominantly evaluate low-dimensional scalar functions and rely on string-level or regression-based metrics that fail to capture structural and geometric equivalence. We introduce SURFACEBENCH, the first geometry-aware benchmark for symbolic discovery of three-dimensional surfaces. Unlike scalar curve-fitting tasks, SURFACEBENCH targets surface-level reasoning, where multi-variable coupling, coordinate transformations, and geometric structure must be inferred directly from data. The benchmark comprises 183 analytically constructed, science-inspired surface equations across 15 categories and three representation paradigms: explicit, implicit, and parametric forms. Each task includes variable semantics and synthetically sampled 3D data, and is designed to stress symbolic composition, structural ambiguity, and representational non-uniqueness while mitigating memorization. To evaluate discovery quality, SURFACEBENCH incorporates symbolic equivalence checks with geometric metrics of the object-space (Chamfer and Hausdorff distances) and regression-based error measures, allowing evaluation of functional fidelity beyond algebraic syntax. Empirical evaluation across evolutionary, neural, and LLM-driven frameworks reveals that no current method achieves consistent performance across representation types, with LLM-based approaches exhibiting strong structural priors but limited robustness in parameter calibration and multi-equation this http URL code and data are available at this link: this http URL .

</details>

---

### 72. [Agility Meets Stability: Versatile Humanoid Control with Heterogeneous Data](https://arxiv.org/abs/2511.17373)

**基本信息**

- 🔗 arXiv: [`2511.17373`](https://arxiv.org/abs/2511.17373)
- 👥 作者: Yixuan Pan, Ruoyi Qiao, Li Chen 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.17373.pdf)

**💡 相关性分析**

满足标准2：论文提出的LinkML是一个通用的数据建模框架，特别指出已应用于化学等领域。该框架可用于创建、标准化和共享化学信息学及质谱分析所需的数据集和模型，为相关主题的研究提供了重要的数据资源和工具基础。

**📖 中文摘要**

这篇论文介绍了LinkML（关联数据建模语言），一个用于简化数据创作、验证和共享的开源数据建模框架。LinkML可以描述从扁平列表到复杂的、相互关联的规范化数据模型。它提供了一种与具体技术架构无关的语法，用于描述模式、类和关系，使建模者能够构建定义明确、稳定且可选择与本体对齐的数据结构。论文特别提到LinkML在生物学、化学、生物医学等多个领域得到日益广泛的应用。对于“化学信息学”领域，标准化、可互操作的数据模型是构建高质量数据集、开发大模型和进行质谱数据分析的基础。LinkML作为一个通用框架，可以直接用于构建化学和质谱数据的标准化模式，从而为相关研究提供关键的数据资源支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Humanoid robots are envisioned to perform a wide range of tasks in human-centered environments, requiring controllers that combine agility with robust balance. Recent advances in locomotion and whole-body tracking have enabled impressive progress in either agile dynamic skills or stability-critical behaviors, but existing methods remain specialized, focusing on one capability while compromising the other. In this work, we introduce AMS (Agility Meets Stability), the first framework that unifies both dynamic motion tracking and extreme balance maintenance in a single policy. Our key insight is to leverage heterogeneous data sources: human motion capture datasets that provide rich, agile behaviors, and physically constrained synthetic balance motions that capture stability configurations. To reconcile the divergent optimization goals of agility and stability, we design a hybrid reward scheme that applies general tracking objectives across all data while injecting balance-specific priors only into synthetic motions. Further, an adaptive learning strategy with performance-driven sampling and motion-specific reward shaping enables efficient training across diverse motion distributions. We validate AMS extensively in simulation and on a real Unitree G1 humanoid. Experiments demonstrate that a single policy can execute agile skills such as dancing and running, while also performing zero-shot extreme balance motions like Ip Man's Squat, highlighting AMS as a versatile control paradigm for future humanoid applications.

</details>

---

### 73. [Quantized SO(3)-Equivariant Graph Neural Networks for Efficient Molecular Property Prediction](https://arxiv.org/abs/2601.02213)

**基本信息**

- 🔗 arXiv: [`2601.02213`](https://arxiv.org/abs/2601.02213)
- 👥 作者: Haoyu Zhou, Ping Xue, Hao Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.02213.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对分子3D结构的等变图神经网络（一种化学领域的大模型）进行量化加速，并在标准化学分子基准（QM9, rMD17）上进行评估，直接围绕化学大模型的效率优化主题。

**📖 中文摘要**

这篇论文提出了量化SO(3)-等变图神经网络（GNNs），用于高效的分子性质预测。SO(3)-等变GNNs是处理3D分子结构（如来自质谱或计算化学）的重要模型，能够保持旋转对称性，从而准确预测能量和力等性质。论文的核心是压缩和加速这类模型，使其能够部署在边缘设备上。研究在QM9和rMD17分子基准数据集上进行了实验，验证了量化模型在保持精度和物理对称性方面的有效性。这项工作直接针对“化学大模型”（具体是用于分子表示的3D GNNs）的部署效率问题，并且其应用的基准（QM9, rMD17）是化学信息学和分子机器学习领域的标准数据集。模型预测的性质（如能量）也与从质谱数据推断结构（质谱结构推理）的最终目标相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deploying 3D graph neural networks (GNNs) that are equivariant to 3D rotations (the group SO(3)) on edge devices is challenging due to their high computational cost. This paper addresses the problem by compressing and accelerating an SO(3)-equivariant GNN using low-bit quantization techniques. Specifically, we introduce three innovations for quantized equivariant transformers: (1) a magnitude-direction decoupled quantization scheme that separately quantizes the norm and orientation of equivariant (vector) features, (2) a branch-separated quantization-aware training strategy that treats invariant and equivariant feature channels differently in an attention-based $SO(3)$-GNN, and (3) a robustness-enhancing attention normalization mechanism that stabilizes low-precision attention computations. Experiments on the QM9 and rMD17 molecular benchmarks demonstrate that our 8-bit models achieve accuracy on energy and force predictions comparable to full-precision baselines with markedly improved efficiency. We also conduct ablation studies to quantify the contribution of each component to maintain accuracy and equivariance under quantization, using the Local error of equivariance (LEE) metric. The proposed techniques enable the deployment of symmetry-aware GNNs in practical chemistry applications with 2.37--2.73x faster inference and 4x smaller model size, without sacrificing accuracy or physical symmetry.

</details>

---

### 74. [Entropy Sentinel: Continuous LLM Accuracy Monitoring from Decoding Entropy Traces in STEM](https://arxiv.org/abs/2601.09001)

**基本信息**

- 🔗 arXiv: [`2601.09001`](https://arxiv.org/abs/2601.09001)
- 👥 作者: Pedro Memoli Buffa, Luciano Del Corro
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.09001.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于输出熵的LLM准确性监控方法，并在多个STEM推理基准上进行了评估。这为评估化学等领域大模型的推理性能和可靠性提供了一种工具和评估思路。

**📖 中文摘要**

这篇论文提出了Entropy Sentinel，一种通过解码熵迹来持续监控大型语言模型（LLM）在STEM领域准确性的方法。该方法从最终层的下一个token概率（top-k logprobs）计算输出熵分布，并用不同的统计量进行总结。一个轻量级分类器预测单个实例的正确性，平均预测概率则得到领域级别的准确性估计。研究在十个STEM推理基准上进行了评估。虽然论文的通用背景是LLM监控，但其评估领域是STEM（科学、技术、工程和数学），这高度涵盖了化学、物理等需要复杂推理的学科。论文中提到的“推理能力”和“STEM领域”与“化学大模型”所需的能力评估高度相关。该方法本身也可以被视为一种用于评估大模型在科学领域（包括化学）表现的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deploying LLMs raises two coupled challenges: (1) monitoring--estimating where a model underperforms as traffic and domains drift--and (2) improvement--prioritizing data acquisition to close the largest performance gaps. We test whether an inference-time signal can estimate slice-level accuracy under domain shift. For each response, we compute an output-entropy profile from final-layer next-token probabilities (from top-$k$ logprobs) and summarize it with different statistics. A lightweight classifier predicts instance correctness, and averaging predicted probabilities yields a domain-level accuracy estimate. We evaluate on ten STEM reasoning benchmarks with exhaustive train/test compositions ($k\in\{1,2,3,4\}$; all $\binom{10}{k}$ combinations), on different classifier models and features across nine LLMs from six families (3B--20B). Estimates often track held-out benchmark accuracy, and several models show near-monotonic ordering of domains, providing evidence for output-entropy profiles being an accessible signal for scalable monitoring and for targeted data acquisition.

</details>

---

### 75. [Hot-Start from Pixels: Low-Resolution Visual Tokens for Chinese Language Modeling](https://arxiv.org/abs/2601.09566)

**基本信息**

- 🔗 arXiv: [`2601.09566`](https://arxiv.org/abs/2601.09566)
- 👥 作者: Shuyang Xiang, Hao Guan
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.09566.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索视觉结构信息（低分辨率图像）作为语言建模的输入表示。这一思想与化学信息学中利用分子结构图、质谱谱图等视觉/结构数据进行模型构建和推理（化学大模型、质谱结构推理）的核心挑战直接相关，提供了跨领域的表示学习思路。

**📖 中文摘要**

这篇论文研究了使用低分辨率视觉输入（字符的灰度图像）作为中文语言建模的替代表示。研究发现，仅使用8x8像素的图像输入，模型能达到与基于索引token的基线模型相当的准确率。这项工作探索了超越离散符号的、基于视觉形态的字符表示，这对于处理像化学式、分子图或质谱图这类具有空间和结构信息的“语言”具有启发意义。虽然论文直接针对中文字符，但其核心思想——利用视觉/结构信息增强或替代离散表示——与“化学大模型”和“质谱结构推理”中处理分子结构图、谱图等非序列化、富含结构信息的数据高度相关。它为如何将化学结构（如2D分子图）编码为适合大模型处理的表示提供了新的视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models typically represent Chinese characters as discrete index-based tokens, largely ignoring their visual form. For logographic scripts, visual structure carries semantic and phonetic information, which may aid prediction. We investigate whether low-resolution visual inputs can serve as an alternative for character-level modeling. Instead of token IDs, our decoder receives grayscale images of individual characters, with resolutions as low as 8 x 8 pixels. Remarkably, these inputs achieve 39.2% accuracy, comparable to the index-based baseline of 39.1%. Such low-resource settings also exhibit a pronounced hot-start effect: by 0.4% of total training, accuracy reaches above 12%, while index-based models lag at below 6%. Overall, our results demonstrate that minimal visual structure can provide a robust and efficient signal for Chinese language modeling, offering an alternative perspective on character representation that complements traditional index-based approaches.

</details>

---

### 76. [Quantization-Aware Distillation for NVFP4 Inference Accuracy Recovery](https://arxiv.org/abs/2601.20088)

**基本信息**

- 🔗 arXiv: [`2601.20088`](https://arxiv.org/abs/2601.20088)
- 👥 作者: Meng Xin, Sweta Priyadarshi, Jingyu Xin 等29人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.20088.pdf)

**💡 相关性分析**

满足标准2：论文提出了量化感知蒸馏（QAD）这一通用方法，用于高效恢复量化后的大语言模型和视觉语言模型的精度。该方法为化学大模型在实际部署中的模型压缩和精度保持提供了重要的工具和技术参考。

**📖 中文摘要**

这篇技术报告提出了量化感知蒸馏（QAD）方法，用于恢复使用NVFP4（4位浮点）量化的大型语言模型（LLMs）和视觉语言模型（VLMs）的推理精度。报告展示了QAD在多个后训练模型（包括AceReason Nemotron, Nemotron 3 Nano等）上的有效性，能够将量化模型的精度恢复到接近BF16全精度的水平。虽然论文列举的模型不一定是化学专用模型，但QAD作为一种通用的、针对经过监督微调（SFT）、强化学习（RL）等复杂流程后训练的大模型的量化恢复方法，其技术对于部署化学领域的大模型（例如，用于分子性质预测、反应预测或质谱解析的大模型）具有直接的实用价值。高效、低精度的模型部署是化学大模型走向实际应用的关键环节。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This technical report presents quantization-aware distillation (QAD) and our best practices for recovering accuracy of NVFP4-quantized large language models (LLMs) and vision-language models (VLMs). QAD distills a full-precision teacher model into a quantized student model using a KL divergence loss. While applying distillation to quantized models is not a new idea, we observe key advantages of QAD for today's LLMs: 1. It shows remarkable effectiveness and stability for models trained through multi-stage post-training pipelines, including supervised fine-tuning (SFT), reinforcement learning (RL), and model merging, where traditional quantization-aware training (QAT) suffers from engineering complexity and training instability; 2. It is robust to data quality and coverage, enabling accuracy recovery without full training data. We evaluate QAD across multiple post-trained models including AceReason Nemotron, Nemotron 3 Nano, Nemotron Nano V2, Nemotron Nano V2 VL (VLM), and Llama Nemotron Super v1, showing consistent recovery to near-BF16 accuracy.

</details>

---

### 77. [WristMIR: Coarse-to-Fine Region-Aware Retrieval of Pediatric Wrist Radiographs with Radiology Report-Driven Learning](https://arxiv.org/abs/2602.07872)

**基本信息**

- 🔗 arXiv: [`2602.07872`](https://arxiv.org/abs/2602.07872)
- 👥 作者: Mert Sonmezer, Serge Vasylechko, Duygu Atasoy 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.07872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用多模态（图像+文本）数据和区域感知机制进行细粒度表示学习与检索。这种方法论与化学信息学中利用质谱图与化合物结构信息进行跨模态匹配和推理（质谱结构推理）的研究主题在技术层面上高度相关。

**📖 中文摘要**

这篇论文提出了WristMIR，一个用于儿科腕部X光片检索的区域感知框架。其核心创新在于利用放射学报告和骨特异性定位，在没有人工图像级标注的情况下学习细粒度的、具有临床意义的图像表示。方法包括使用MedGemma进行结构化报告挖掘以生成全局和区域级描述，并训练全局和局部对比编码器进行两阶段检索。虽然应用领域是医学影像，但其方法论——利用多模态数据（图像+文本报告）进行细粒度、结构化的表示学习，并应用于检索任务——与“化学大模型”和“质谱结构推理”有很强的类比性。例如，在质谱分析中，可以将质谱图与化合物结构描述（文本）或分子式关联起来，进行类似的跨模态检索和表示学习，以推断未知物质的结构。论文提供了一种可借鉴的技术框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieving wrist radiographs with analogous fracture patterns is challenging because clinically important cues are subtle, highly localized and often obscured by overlapping anatomy or variable imaging views. Progress is further limited by the scarcity of large, well-annotated datasets for case-based medical image retrieval. We introduce WristMIR, a region-aware pediatric wrist radiograph retrieval framework that leverages dense radiology reports and bone-specific localization to learn fine-grained, clinically meaningful image representations without any manual image-level annotations. Using MedGemma-based structured report mining to generate both global and region-level captions, together with pre-processed wrist images and bone-specific crops of the distal radius, distal ulna, and ulnar styloid, WristMIR jointly trains global and local contrastive encoders and performs a two-stage retrieval process: (1) coarse global matching to identify candidate exams, followed by (2) region-conditioned reranking aligned to a predefined anatomical bone region. WristMIR improves retrieval performance over strong vision-language baselines, raising image-to-text Recall@5 from 0.82% to 9.35%. Its embeddings also yield stronger fracture classification (AUROC 0.949, AUPRC 0.953). In region-aware evaluation, the two-stage design markedly improves retrieval-based fracture diagnosis, increasing mean $F_1$ from 0.568 to 0.753, and radiologists rate its retrieved cases as more clinically relevant, with mean scores rising from 3.36 to 4.35. These findings highlight the potential of anatomically guided retrieval to enhance diagnostic reasoning and support clinical decision-making in pediatric musculoskeletal imaging. The source code is publicly available at this https URL .

</details>

---

### 78. [MoToRec: Sparse-Regularized Multimodal Tokenization for Cold-Start Recommendation](https://arxiv.org/abs/2602.11062)

**基本信息**

- 🔗 arXiv: [`2602.11062`](https://arxiv.org/abs/2602.11062)
- 👥 作者: Jialin Liu, Zhaorui Zhang, Ray C.C. Cheung
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.11062.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是多模态数据的离散语义标记化与解耦表示学习。这一技术方向与化学信息学中处理分子结构、质谱等多模态数据，并构建适用于大模型的统一、可解释表示的挑战直接相关，为化学大模型和质谱结构推理提供了潜在的技术路径。

**📖 中文摘要**

这篇论文提出了MoToRec，一个通过稀疏正则化多模态标记化解决推荐系统中冷启动问题的框架。它将多模态推荐转化为离散语义标记化任务，核心是一个稀疏正则化的残差量化变分自编码器（RQ-VAE），用于生成离散的、可解释的标记组合，以促进解耦表示。虽然应用场景是推荐系统，但其核心技术——对多模态内容（如文本、图像）进行离散化、解耦的语义编码——对于“化学大模型”和“质谱结构推理”具有重要启示。在化学领域，分子、反应、谱图都是多模态数据（SMILES字符串、分子图、质谱/光谱向量）。MoToRec的离散标记化思想可以用于创建分子或谱图的语义词汇表，从而构建更适合大模型理解和推理的统一表示，这对于从质谱数据推断分子结构等任务可能非常有效。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph neural networks (GNNs) have revolutionized recommender systems by effectively modeling complex user-item interactions, yet data sparsity and the item cold-start problem significantly impair performance, particularly for new items with limited or no interaction history. While multimodal content offers a promising solution, existing methods result in suboptimal representations for new items due to noise and entanglement in sparse data. To address this, we transform multimodal recommendation into discrete semantic tokenization. We present Sparse-Regularized Multimodal Tokenization for Cold-Start Recommendation (MoToRec), a framework centered on a sparsely-regularized Residual Quantized Variational Autoencoder (RQ-VAE) that generates a compositional semantic code of discrete, interpretable tokens, promoting disentangled representations. MoToRec's architecture is enhanced by three synergistic components: (1) a sparsely-regularized RQ-VAE that promotes disentangled representations, (2) a novel adaptive rarity amplification that promotes prioritized learning for cold-start items, and (3) a hierarchical multi-source graph encoder for robust signal fusion with collaborative signals. Extensive experiments on three large-scale datasets demonstrate MoToRec's superiority over state-of-the-art methods in both overall and cold-start scenarios. Our work validates that discrete tokenization provides an effective and scalable alternative for mitigating the long-standing cold-start challenge.

</details>

---

### 79. [Function-Space Decoupled Diffusion for Forward and Inverse Modeling in Carbon Capture and Storage](https://arxiv.org/abs/2602.12274)

**基本信息**

- 🔗 arXiv: [`2602.12274`](https://arxiv.org/abs/2602.12274)
- 👥 作者: Xin Ju, Jiachen Yao, Anima Anandkumar 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.12274.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散模型和可微分神经算子进行复杂系统的正反演建模。该方法论与“质谱结构推理”的核心问题——从观测数据（质谱）反演生成模型（分子结构）——在数学和计算范式上高度一致，提供了创新的解决方案思路。

**📖 中文摘要**

这篇论文提出了Fun-DDPS，一个用于碳捕集与封存（CCS）中正演和反演建模的生成框架。它结合了函数空间扩散模型和可微分神经算子代理。方法学习地质参数（地质模型）的先验分布，并利用局部神经算子（LNO）代理为动力学场提供物理一致的指导。虽然应用领域是地球科学，但其核心方法——使用扩散模型学习复杂参数空间的先验，并结合物理代理模型进行条件生成和反演——与“化学大模型”和“质谱结构推理”有深刻的相似性。在质谱结构推理中，目标是从观测到的质谱（动态场）反推出分子结构（参数空间）。Fun-DDPS展示了一种将生成式先验（扩散模型）与物理/化学知识（通过可微分代理嵌入）相结合来解决高维、稀疏观测反演问题的强大范式，可直接启发质谱解析新方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate characterization of subsurface flow is critical for Carbon Capture and Storage (CCS) but remains challenged by the ill-posed nature of inverse problems with sparse observations. We present Function-space Decoupled Diffusion Posterior Sampling (Fun-DDPS), a generative framework that combines function-space diffusion models with differentiable neural operator surrogates for both forward and inverse modeling. Our approach learns a prior distribution over geological parameters (geomodel) using a single-channel diffusion model, then leverages a Local Neural Operator (LNO) surrogate to provide physics-consistent guidance for cross-field conditioning on the dynamics field. This decoupling allows the diffusion prior to robustly recover missing information in parameter space, while the surrogate provides efficient gradient-based guidance for data assimilation. We demonstrate Fun-DDPS on synthetic CCS modeling datasets, achieving two key results: (1) For forward modeling with only 25% observations, Fun-DDPS achieves 7.7% relative error compared to 86.9% for standard surrogates (an 11x improvement), proving its capability to handle extreme data sparsity where deterministic methods fail. (2) We provide the first rigorous validation of diffusion-based inverse solvers against asymptotically exact Rejection Sampling (RS) posteriors. Both Fun-DDPS and the joint-state baseline (Fun-DPS) achieve Jensen-Shannon divergence less than 0.06 against the ground truth. Crucially, Fun-DDPS produces physically consistent realizations free from the high-frequency artifacts observed in joint-state baselines, achieving this with 4x improved sample efficiency compared to rejection sampling.

</details>

---

### 80. [MedXIAOHE: A Comprehensive Recipe for Building Medical MLLMs](https://arxiv.org/abs/2602.12705)

**基本信息**

- 🔗 arXiv: [`2602.12705`](https://arxiv.org/abs/2602.12705)
- 👥 作者: Baorong Shi, Bo Cui, Boyuan Jiang 等20人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.12705.pdf)

**💡 相关性分析**

满足标准3：论文系统地介绍了构建一个专业领域（医学）多模态大模型的完整方案，包括数据处理、模型架构、训练策略和评估。这为“化学大模型”的构建提供了重要的、可迁移的综述性讨论和实践展望。

**📖 中文摘要**

这篇论文介绍了MedXIAOHE，一个旨在推进现实世界临床应用中通用医学理解和推理的医学视觉语言基础模型。论文详细阐述了其构建方法，包括实体感知的持续预训练框架、融合多样化医学推理模式的强化学习和工具增强的智能体训练，以及用于提高可靠性的用户偏好规则、证据推理和低幻觉长报告生成。虽然专注于医学领域，但MedXIAOHE作为一个大规模多模态大模型的完整构建“配方”，其设计选择、训练策略（特别是针对专业领域知识的注入和复杂推理能力的培养）和评估框架，对于构建“化学大模型”具有极高的参考价值。化学领域同样需要处理多模态数据（结构式、谱图、文本），并完成分子性质预测、反应结果推理、谱图解析等复杂任务。该论文为如何在专业科学领域构建可靠、可推理的大模型提供了实践指南。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present MedXIAOHE, a medical vision-language foundation model designed to advance general-purpose medical understanding and reasoning in real-world clinical applications. MedXIAOHE achieves state-of-the-art performance across diverse medical benchmarks and surpasses leading closed-source multimodal systems on multiple capabilities. To achieve this, we propose an entity-aware continual pretraining framework that organizes heterogeneous medical corpora to broaden knowledge coverage and reduce long-tail gaps (e.g., rare diseases). For medical expert-level reasoning and interaction, MedXIAOHE incorporates diverse medical reasoning patterns via reinforcement learning and tool-augmented agentic training, enabling multi-step diagnostic reasoning with verifiable decision traces. To improve reliability in real-world use, MedXIAOHE integrates user-preference rubrics, evidence-grounded reasoning, and low-hallucination long-form report generation, with improved adherence to medical instructions. We release this report to document our practical design choices, scaling insights, and evaluation framework, hoping to inspire further research.

</details>

---

### 81. [Rethinking the Role of LLMs in Time Series Forecasting](https://arxiv.org/abs/2602.14744)

**基本信息**

- 🔗 arXiv: [`2602.14744`](https://arxiv.org/abs/2602.14744)
- 👥 作者: Xin Qiu, Junlong Tong, Yirong Sun 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.14744.pdf)

**💡 相关性分析**

满足标准3：论文通过大规模实证研究，重新评估并肯定了LLMs在复杂预测任务中的作用和条件，并提供了模型设计指导。这为思考LLMs在化学预测和推理任务（化学大模型）中的有效性和应用方式提供了重要的综述性讨论和实证参考。

**📖 中文摘要**

这篇论文对大型语言模型（LLMs）在时间序列预测（TSF）中的作用进行了大规模重新评估。研究涵盖了80亿个观测值、17个预测场景、多个预测范围和对齐策略。结果表明，在适当的设置下（特别是跨域泛化和预对齐策略），LLMs确实能显著提升预测性能。论文强调了LLMs的预训练知识和模型架构的互补作用。这项研究虽然针对时间序列，但其核心结论——在跨域、数据混合分布的大规模场景下，完整的LLM架构变得不可或缺——对于“化学大模型”的研究具有重要启示。化学预测任务（如性质预测、反应产率预测）也常常面临分布外泛化、多任务学习等挑战。该研究为评估和设计化学领域的大模型（是否以及如何利用LLMs的先验知识和架构）提供了实证依据和设计指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been introduced to time series forecasting (TSF) to incorporate contextual knowledge beyond numerical signals. However, existing studies question whether LLMs provide genuine benefits, often reporting comparable performance without LLMs. We show that such conclusions stem from limited evaluation settings and do not hold at scale. We conduct a large-scale study of LLM-based TSF (LLM4TSF) across 8 billion observations, 17 forecasting scenarios, 4 horizons, multiple alignment strategies, and both in-domain and out-of-domain settings. Our results demonstrate that \emph{LLM4TS indeed improves forecasting performance}, with especially large gains in cross-domain generalization. Pre-alignment outperforming post-alignment in over 90\% of tasks. Both pretrained knowledge and model architecture of LLMs contribute and play complementary roles: pretraining is critical under distribution shifts, while architecture excels at modeling complex temporal dynamics. Moreover, under large-scale mixed distributions, a fully intact LLM becomes indispensable, as confirmed by token-level routing analysis and prompt-based improvements. Overall, Our findings overturn prior negative assessments, establish clear conditions under which LLMs are not only useful, and provide practical guidance for effective model design. We release our code at this https URL .

</details>

---

### 82. [UniTAF: A Modular Framework for Joint Text-to-Speech and Audio-to-Face Modeling](https://arxiv.org/abs/2602.15651)

**基本信息**

- 🔗 arXiv: [`2602.15651`](https://arxiv.org/abs/2602.15651)
- 👥 作者: Qiangong Zhou, Nagasaka Tomohiro
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.15651.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是多模态（语音、文本、视觉）任务的联合建模与内部特征共享。这一架构思想与化学信息学中构建统一模型来处理分子结构、描述文本和谱图数据（质谱结构推理）的多模态对齐与联合推理挑战直接相关。

**📖 中文摘要**

这篇论文提出了UniTAF，一个用于联合文本到语音（TTS）和音频到人脸（A2F）建模的模块化框架。其核心思想是将两个独立模型（TTS和A2F）合并为一个统一模型，以实现内部特征传递，从而提高从文本生成的音频和面部表情之间的一致性。论文从系统设计角度验证了重用TTS中间表示进行语音和面部表情联合建模的可行性。虽然应用领域是语音和动画，但其“联合建模”和“内部特征传递”的核心思想与“化学大模型”和“质谱结构推理”中多任务学习与多模态对齐的思想相通。例如，可以设想一个联合模型，同时处理分子描述文本、分子结构图和对应的质谱图，通过共享表示空间来增强从一种模态推理另一种模态的能力（如从质谱图生成结构描述）。该论文为这类多模态联合建模提供了工程实践参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work considers merging two independent models, TTS and A2F, into a unified model to enable internal feature transfer, thereby improving the consistency between audio and facial expressions generated from text. We also discuss the extension of the emotion control mechanism from TTS to the joint model. This work does not aim to showcase generation quality; instead, from a system design perspective, it validates the feasibility of reusing intermediate representations from TTS for joint modeling of speech and facial expressions, and provides engineering practice references for subsequent speech expression co-design. The project code has been open source at: this https URL

</details>

---

### 83. [Curriculum Learning for Efficient Chain-of-Thought Distillation via Structure-Aware Masking and GRPO](https://arxiv.org/abs/2602.17686)

**基本信息**

- 🔗 arXiv: [`2602.17686`](https://arxiv.org/abs/2602.17686)
- 👥 作者: Bowen Yu, Maolin Wang, Sheng Zhang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.17686.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大模型思维链推理能力的课程学习蒸馏方法。该方法旨在优化模型推理的效率和准确性，与“化学大模型”的模型压缩、效率提升及保持复杂科学推理能力的研究主题直接相关。

**📖 中文摘要**

这篇论文提出了一个用于高效思维链（CoT）蒸馏的三阶段课程学习框架。该框架旨在解决将大型教师模型的复杂推理能力蒸馏到紧凑学生模型中的挑战。方法包括：通过掩码乱序重建建立结构理解；在掩码完成任务上应用组相对策略优化（GRPO），让模型在准确性和简洁性之间找到平衡；针对持续失败案例，指导学生通过有针对性的重写内化教师知识。实验在数学推理数据集GSM8K上进行。这项工作直接针对“大模型”的推理能力蒸馏和效率优化。虽然评估领域是数学，但其提出的课程学习、GRPO优化等技术，对于蒸馏化学大模型（例如，用于分子推理或谱图解析的模型）的复杂推理能力具有直接的借鉴意义，有助于构建更小、更快但保持强推理能力的化学领域模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Distilling Chain-of-Thought (CoT) reasoning from large language models into compact student models presents a fundamental challenge: teacher rationales are often too verbose for smaller models to faithfully reproduce. Existing approaches either compress reasoning into single-step, losing the interpretability that makes CoT valuable. We present a three-stage curriculum learning framework that addresses this capacity mismatch through progressive skill acquisition. First, we establish structural understanding via masked shuffled reconstruction. Second, we apply Group Relative Policy Optimization (GRPO) on masked completion tasks, enabling the model to discover its own balance between accuracy and brevity. Third, we identify persistent failure cases and guide the student to internalize teacher knowledge through targeted rewriting, again optimized with GRPO. Experiments on GSM8K demonstrate that our approach enables Qwen2.5-3B-Base to achieve an 11.29 percent accuracy improvement while reducing output length by 27.4 percent, surpassing both instruction-tuned variants and prior distillation methods.

</details>

---

### 84. [Spilled Energy in Large Language Models](https://arxiv.org/abs/2602.18671)

**基本信息**

- 🔗 arXiv: [`2602.18671`](https://arxiv.org/abs/2602.18671)
- 👥 作者: Adrian Robert Minut, Hazem Dewidar, Iacopo Masi
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.18671.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于能量模型的、无需训练的LLM生成错误检测方法。这为评估“化学大模型”在分子结构生成、反应预测或质谱解析等任务中输出结果的可靠性和一致性提供了潜在的工具和度量标准。

**📖 中文摘要**

这篇论文将大型语言模型（LLM）的最终softmax分类器重新解释为基于能量的模型（EBM），并在推理时将序列到序列的概率链分解为多个相互作用的EBM。基于此，论文提出了两种无需训练、直接从输出logits导出的度量：“溢出能量”和“边缘化能量”，用于检测模型生成中的事实错误、偏见和幻觉。方法在多个基准和LLM（包括LLaMA, Mistral, Gemma, Qwen3）上进行了评估，展示了强大的幻觉检测和跨任务泛化能力。对于“化学大模型”而言，生成内容的可靠性（如正确的分子结构、反应路径或谱图解释）至关重要。该论文提供了一种无需额外训练、可解释的生成质量监控和错误检测工具，有助于评估和提高化学大模型在结构推理等任务中的输出可信度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We reinterpret the final Large Language Model (LLM) softmax classifier as an Energy-Based Model (EBM), decomposing the sequence-to-sequence probability chain into multiple interacting EBMs at inference. This principled approach allows us to track "energy spills" during decoding, which we empirically show correlate with factual errors, biases, and failures. Similar to Orgad et al. (2025), our method localizes the exact answer token and subsequently tests for hallucinations. Crucially, however, we achieve this without requiring trained probe classifiers or activation ablations. Instead, we introduce two completely training-free metrics derived directly from output logits: spilled energy, which captures the discrepancy between energy values across consecutive generation steps that should theoretically match, and marginalized energy, which is measurable at a single step. Evaluated on nine benchmarks across state-of-the-art LLMs (including LLaMA, Mistral, and Gemma) and on synthetic algebraic operations (Qwen3), our approach demonstrates robust, competitive hallucination detection and cross-task generalization. Notably, these results hold for both pretrained and instruction-tuned variants without introducing any training overhead. Code available at: this http URL

</details>

---

### 85. [RuCL: Stratified Rubric-Based Curriculum Learning for Multimodal Large Language Model Reasoning](https://arxiv.org/abs/2602.21628)

**基本信息**

- 🔗 arXiv: [`2602.21628`](https://arxiv.org/abs/2602.21628)
- 👥 作者: Yukun Chen, Jiaming Li, Longze Chen 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.21628.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对多模态大模型推理能力的分层课程学习框架。该方法通过结构化、渐进式的规则引导来优化模型推理，这一思路与训练化学大模型进行复杂的、多步骤的质谱结构推理或反应机理推理高度相关。

**📖 中文摘要**

这篇论文提出了分层规则课程学习（RuCL），一个用于增强多模态大语言模型（MLLMs）推理能力的新框架。针对现有基于规则的强化学习方法计算成本高、训练效率低的问题，RuCL生成具有广泛适用性的通用规则，并根据模型能力对其进行分层。通过动态调整训练过程中的规则权重，RuCL引导模型从掌握基础感知逐步过渡到处理高级逻辑推理。实验在多个视觉推理基准上进行。该框架虽然针对视觉语言模型，但其“规则分层”和“动态课程学习”的核心思想对于训练“化学大模型”处理复杂的多步推理任务（如从质谱数据逐步推断分子子结构）具有很高的参考价值。它提供了一种系统化的方法来注入领域知识（化学规则）并指导模型学习进程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has emerged as a prevailing paradigm for enhancing reasoning in Multimodal Large Language Models (MLLMs). However, relying solely on outcome supervision risks reward hacking, where models learn spurious reasoning patterns to satisfy final answer checks. While recent rubric-based approaches offer fine-grained supervision signals, they suffer from high computational costs of instance-level generation and inefficient training dynamics caused by treating all rubrics as equally learnable. In this paper, we propose Stratified Rubric-based Curriculum Learning (RuCL), a novel framework that reformulates curriculum learning by shifting the focus from data selection to reward design. RuCL generates generalized rubrics for broad applicability and stratifies them based on the model's competence. By dynamically adjusting rubric weights during training, RuCL guides the model from mastering foundational perception to tackling advanced logical reasoning. Extensive experiments on various visual reasoning benchmarks show that RuCL yields a remarkable +7.83% average improvement over the Qwen2.5-VL-7B model, achieving a state-of-the-art accuracy of 60.06%.

</details>

---

### 86. [DeepXiv-SDK: An Agentic Data Interface for Scientific Literature](https://arxiv.org/abs/2603.00084)

**基本信息**

- 🔗 arXiv: [`2603.00084`](https://arxiv.org/abs/2603.00084)
- 👥 作者: Hongjin Qian, Ziyi Xia, Ze Liu 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00084.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为DeepXiv-SDK的智能数据接口，专门用于高效访问和利用科学文献。它通过将非结构化文献数据（如PDF）转换为结构化JSON格式，并提供了丰富的检索工具和API，为化学信息学和质谱分析等领域的研究（包括化学大模型和质谱结构推理）提供了重要的数据资源支持。该工具计划扩展到chemRxiv等化学相关预印本库，直接服务于相关领域的数据需求。

**📖 中文摘要**

本文介绍了DeepXiv-SDK，这是一个为科学文献设计的智能数据接口，旨在解决LLM智能体在科学研究中面临的数据访问瓶颈。它将非结构化、面向人类的文献数据（如HTML网页和PDF文件）转换为规范化的JSON格式结构化表示，提高了数据的可用性，并支持渐进式访问。该SDK提供了一个服务层，包含现成的数据访问和临时检索工具，支持CLI、MCP和Python SDK等多种智能体使用方式。应用层则内置了一个智能体，封装了服务层的基本工具以支持复杂的数据访问需求。DeepXiv-SDK目前支持完整的ArXiv语料库，并计划扩展到PubMed Central、bioRxiv、medRxiv和chemRxiv等其他常见开放获取语料库。这项工作为化学信息学等领域的研究人员提供了一个高效、成本可控的文献数据访问和利用工具，有助于加速包括化学大模型和质谱分析在内的科学发现进程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-agents are increasingly used to accelerate the progress of scientific research. Yet a persistent bottleneck is data access: agents not only lack readily available tools for retrieval, but also have to work with unstrcutured, human-centric data on the Internet, such as HTML web-pages and PDF files, leading to excessive token consumption, limit working efficiency, and brittle evidence look-up. This gap motivates the development of \textit{an agentic data interface}, which is designed to enable agents to access and utilize scientific literature in a more effective, efficient, and cost-aware manner. In this paper, we introduce DeepXiv-SDK, which offers a three-layer agentic data interface for scientific literature. 1) Data Layer, which transforms unstructured, human-centric data into normalized and structured representations in JSON format, improving data usability and enabling progressive accessibility of the data. 2) Service Layer, which presents readily available tools for data access and ad-hoc retrieval. It also enables a rich form of agent usage, including CLI, MCP, and Python SDK. 3) Application Layer, which creates a built-in agent, packaging basic tools from the service layer to support complex data access demands. DeepXiv-SDK currently supports the complete ArXiv corpus, and is synchronized daily to incorporate new releases. It is designed to extend to all common open-access corpora, such as PubMed Central, bioRxiv, medRxiv, and chemRxiv. We release RESTful APIs, an open-source Python SDK, and a web demo showcasing deep search and deep research workflows. DeepXiv-SDK is free to use with registration.

</details>

---

### 87. [CoPeP: Benchmarking Continual Pretraining for Protein Language Models](https://arxiv.org/abs/2603.00253)

**基本信息**

- 🔗 arXiv: [`2603.00253`](https://arxiv.org/abs/2603.00253)
- 👥 作者: Darshan Patil, Pranshu Malviya, Mathieu Reymond 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.00253.pdf)

**💡 相关性分析**

满足标准2：论文提出了CoPeP基准，这是一个专门用于评估蛋白质语言模型（pLM）持续预训练性能的新基准。它提供了一个由UniProt知识库衍生的、跨越十年的蛋白质数据集序列，并定义了31个蛋白质理解任务的评估指标。这个基准和相关的数据集资源对于开发和评估化学信息学领域的“化学大模型”（特别是蛋白质相关的模型）具有直接价值，为模型在动态数据环境下的学习和适应能力提供了重要的评估工具和数据支持。

**📖 中文摘要**

本文提出了CoPeP基准，用于评估蛋白质语言模型（pLM）的持续预训练性能。蛋白质语言模型通过从进化统计中学习序列、结构和功能之间的关系，在加速治疗性药物发现方面显示出巨大潜力。这些模型从不断更新的蛋白质数据库中学习，其动态特性促使了持续学习的应用。CoPeP基准从UniProt知识库中整理了一个跨越十年的蛋白质数据集序列，并定义了31个蛋白质理解任务的评估指标。作者评估了包括回放、反学习和基于可塑性的方法在内的多种持续学习方法。研究发现，结合时间元信息可以将困惑度提高高达7%。这项工作为在真实世界的大规模应用中研究持续学习方法提供了一个重要的基准。对于化学信息学领域，特别是涉及蛋白质结构和功能预测的化学大模型研究，CoPeP基准提供了评估模型在动态数据流中持续学习能力的标准化框架和数据集资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (pLMs) have recently gained significant attention for their ability to uncover relationships between sequence, structure, and function from evolutionary statistics, thereby accelerating therapeutic drug discovery. These models learn from large protein databases that are continuously updated by the biology community and whose dynamic nature motivates the application of continual learning, not only to keep up with the ever-growing data, but also as an opportunity to take advantage of the temporal meta-information that is created during this process. As a result, we introduce the Continual Pretraining of Protein Language Models (CoPeP) benchmark, a novel benchmark for evaluating continual learning approaches on pLMs. Specifically, we curate a sequence of protein datasets derived from the UniProt Knowledgebase spanning a decade and define metrics to assess pLM performance across 31 protein understanding tasks. We evaluate several methods from the continual learning literature, including replay, unlearning, and plasticity-based methods, some of which have never been applied to models and data of this scale. Our findings reveal that incorporating temporal meta-information improves perplexity by up to 7% even when compared to training on data from all tasks jointly. Moreover, even at scale, several continual learning methods outperform naive continual pretraining. The CoPeP benchmark offers an exciting opportunity to study these methods at scale in an impactful real-world application.

</details>

---

### 88. [BioChemInsight: An Online Platform for Automated Extraction of Chemical Structures and Activity Data from Patents](https://arxiv.org/abs/2504.10525)

**基本信息**

- 🔗 arXiv: [`2504.10525`](https://arxiv.org/abs/2504.10525)
- 👥 作者: Zhe Wang, Fangtian Fu, Wei Zhang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.10525.pdf)

**💡 相关性分析**

满足标准2：论文提出了BioChemInsight平台，这是一个专门用于从专利中自动、高效地提取化学结构及其对应生物活性数据的工具。它提供了一个开源流水线，能够将非结构化的专利文档转化为结构化的化学信息数据。这对于化学信息学领域构建大规模、高质量的化学数据集至关重要，这些数据集是训练“化学大模型”和进行“质谱结构推理”研究的基础资源。该工具显著降低了相关数据获取和预处理的成本与时间。

**📖 中文摘要**

本文介绍了BioChemInsight，一个用于从专利中自动提取化学结构及其生物活性数据的在线平台。该平台整合了DECIMER Segmentation（用于化学结构识别）、GLM-4.5V（用于化合物标识符关联）、PaddleOCR和GLM-4（用于生物活性提取和单位归一化），形成了一个开源流水线。在涵盖15个治疗靶点的181项专利上进行的评估显示，该系统在化学结构识别、生物活性数据提取和化合物标识符关联三个关键任务上的平均提取准确率超过90%。分析表明，专利覆盖的化学空间与公共数据库ChEMBL中的化学空间在很大程度上是互补的。因此，通过实现系统的专利挖掘，BioChemInsight提供了获取在ChEMBL中代表性不足的化学信息的途径。这扩展了可探索的化合物-靶点相互作用的范围，丰富了定量构效关系建模和靶向筛选的数据基础，并将数据预处理时间从数周缩短到数小时。该工具对于化学信息学和药物发现领域的研究人员，特别是那些需要大规模化学结构和活性数据进行模型训练（如化学大模型）或质谱结构推理的研究，是一个重要的数据资源获取工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The automated extraction of chemical structures and their corresponding bioactivity data is essential for accelerating drug discovery and enabling data-driven research. Current optical chemical structure recognition tools lack the capability to autonomously link molecular structures with their bioactivity profiles, posing a significant bottleneck in structure-activity relationship analysis. To address this, we present BioChemInsight, an open-source pipeline that integrates DECIMER Segmentation with MolNexTR for chemical structure recognition, GLM-4.5V for compound identifier association, and PaddleOCR combined with GLM-4.6 for bioactivity extraction and unit normalization. We evaluated BioChemInsight on 181 patents covering 15 therapeutic targets. The system achieved an average extraction accuracy of above 90% across three key tasks: chemical structure recognition, bioactivity data extraction, and compound identifier association. Our analysis indicates that the chemical space covered by patents is largely complementary to that contained in established public database ChEMBL. Consequently, by enabling systematic patent mining, BioChemInsight provides access to chemical information underrepresented in ChEMBL. This capability expands the landscape of explorable compound-target interactions, enriches the data foundation for quantitative structure-activity relationship modeling and targeted screening, and reduces data preprocessing time from weeks to hours. BioChemInsight is available at this https URL .

</details>

---

### 89. [Sustainable Materials Discovery in the Era of Artificial Intelligence](https://arxiv.org/abs/2601.21527)

**基本信息**

- 🔗 arXiv: [`2601.21527`](https://arxiv.org/abs/2601.21527)
- 👥 作者: Sajid Mannan, Rupert J. Myers, Rohit Batra 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.21527.pdf)

**💡 相关性分析**

满足标准3：论文是一篇前瞻性讨论，系统性地探讨了如何将人工智能（特别是机器学习和大模型）与可持续性评估（生命周期评估）整合到材料发现流程中。它虽然没有直接报告一个具体的化学大模型，但深入讨论了该领域面临的核心挑战（数据、尺度、不确定性）并提出了一个统一的ML-LCA框架。这对于“化学大模型”在材料科学领域的未来发展方向、评估标准和设计原则提供了重要的综述和展望，属于对相关主题的重要讨论。

**📖 中文摘要**

本文探讨了在人工智能时代实现可持续材料发现的框架。作者指出，当前的人工智能材料发现工作流通常优先优化性能，而将可持续性评估推迟到合成后阶段，这可能导致资源被投入到潜在不可持续的解决方案中。为了克服原子尺度设计与生命周期评估之间的脱节，作者提出了一个统一的ML-LCA框架，旨在将上游的机器学习辅助材料发现与下游的生命周期评估整合起来。该框架包含五个组成部分：用于构建材料-环境知识库的信息提取、连接性质与可持续性指标的标准化数据库、桥接原子性质与生命周期影响的多尺度模型、具有不确定性量化的制造路径集成预测，以及支持同时优化性能与可持续性的不确定性感知优化。通过涵盖玻璃、水泥、半导体光刻胶和聚合物的案例研究，作者论证了该框架的必要性和可行性。这项工作为“化学大模型”在材料发现领域的应用提供了一个重要的前瞻性视角，即如何将可持续性指标作为设计约束或优化目标整合到模型训练和材料生成过程中，从而引导发现“设计即可持续”的材料，而不仅仅是高性能材料。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Artificial intelligence (AI) has transformed materials discovery, enabling rapid exploration of chemical space through generative models and surrogate screening. Yet current AI workflows optimize performance first, deferring sustainability to post synthesis assessment. This creates inefficiency by the time environmental burdens are quantified, resources have been invested in potentially unsustainable solutions. The disconnect between atomic scale design and lifecycle assessment (LCA) reflects fundamental challenges, data scarcity across heterogeneous sources, scale gaps from atoms to industrial systems, uncertainty in synthesis pathways, and the absence of frameworks that co-optimize performance with environmental impact. We propose to integrate upstream machine learning (ML) assisted materials discovery with downstream lifecycle assessment into a uniform ML-LCA environment. The framework ML-LCA integrates five components, information extraction for building materials-environment knowledge bases, harmonized databases linking properties to sustainability metrics, multi-scale models bridging atomic properties to lifecycle impacts, ensemble prediction of manufacturing pathways with uncertainty quantification, and uncertainty-aware optimization enabling simultaneous performance-sustainability navigation. Case studies spanning glass, cement, semiconductor photoresists, and polymers demonstrate both necessity and feasibility while identifying material-specific integration challenges. Realizing ML-LCA demands coordinated advances in data infrastructure, ex-ante assessment methodologies, multi-objective optimization, and regulatory alignment enabling the discovery of materials that are sustainable by design rather than by chance.

</details>

---

## 📊 数据统计
- 累计运行天数：9
- 累计论文数量：608

## 📝 历史记录

> 暂无历史数据

