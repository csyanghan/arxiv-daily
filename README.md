# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-22 01:28:12

## 📅 2026-03-22 (今日最新)

**相关论文数：66**

### 1. [Continually self-improving AI](https://arxiv.org/abs/2603.18073)

**基本信息**

- 🔗 arXiv: [`2603.18073`](https://arxiv.org/abs/2603.18073)
- 👥 作者: Zitong Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何使大型模型（特别是语言模型）实现持续的自我改进，这直接关联到“化学大模型”主题中关于模型构建、能力提升和适应性的核心问题。

**📖 中文摘要**

这篇论文探讨了如何使人工智能系统实现持续的自我改进，从而超越对人类创造者的依赖。论文提出了三个关键步骤来打破这种依赖：1）通过合成数据方法，将小型专业语料库多样化和放大为丰富的知识表示，使模型能够从有限的源材料中高效地更新其参数，从而克服知识获取中的数据效率障碍。2）通过模型自生成合成数据来引导其基础预训练能力，减少对有限人类数据的依赖。3）通过在算法空间中进行大规模的测试时搜索，使AI能够探索比人类研究人员手动探索更大的学习算法配置空间。虽然论文主要关注语言模型，但其核心主题——通过合成数据、自生成数据和算法搜索实现AI的自我改进——直接与“化学大模型”这一更广泛的研究主题相关，即如何构建和持续改进用于科学领域（如化学）的大型、自适应的基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern language model-based AI systems are remarkably powerful, yet their capabilities remain fundamentally capped by their human creators in three key ways. First, although a model's weights can be updated via fine-tuning, acquiring new knowledge from small, specialized corpora after pretraining remains highly data-inefficient. Second, the training of these systems relies heavily on finite, human-generated data from across history. Third, the pipelines used to train AI models are confined by the algorithms that human researchers can discover and explore. This thesis takes a small step toward overcoming these inherent limitations, presenting three chapters aimed at breaking these dependencies to create continually self-improving AI. First, to overcome this data-efficiency barrier in knowledge acquisition, we propose a synthetic data approach that diversifies and amplifies small corpora into rich knowledge representations, enabling a model to effectively update its parameters from limited source material. Second, to reduce reliance on human data, we show that given a fixed amount of such data, the model can self-generate synthetic data to bootstrap its fundamental pretraining capabilities without distillation from any off-the-shelf, instruction-tuned LM. Finally, to transcend human-engineered training paradigms, we demonstrate that by scaling search during test time over the space of algorithms, AI can search over a larger space of learning algorithm configurations than human researchers can explore manually.

</details>

---

### 2. [Lightweight Adaptation for LLM-based Technical Service Agent: Latent Logic Augmentation and Robust Noise Reduction](https://arxiv.org/abs/2603.18074)

**基本信息**

- 🔗 arXiv: [`2603.18074`](https://arxiv.org/abs/2603.18074)
- 👥 作者: Yi Yu, Junzhuo Ma, Chenghuang Shen 等18人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18074.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于大型语言模型在复杂技术领域的适配和优化。虽然应用场景是云服务，但其提出的轻量级适配框架、潜在逻辑增强和噪声降低方法，对于构建和优化应用于“化学信息学”等科学领域的“化学大模型”或专业代理具有直接的参考价值和相关性。

**📖 中文摘要**

本文提出了一个用于在复杂技术服务领域（如云服务）适配大型语言模型（LLM）的轻量级框架。该框架旨在解决在缺乏显式认知链的人类演示和有效响应多样性的情况下，代理难以内化潜在决策逻辑并有效泛化的问题。框架包含三个关键贡献：1）潜在逻辑增强：通过规划感知轨迹建模和决策推理增强，弥合表层监督与潜在决策逻辑之间的差距。2）鲁棒噪声降低：通过双重过滤方法构建多真实答案数据集，以捕获语义多样性并减少噪声。3）轻量级适配：设计了一个混合奖励机制，融合基于LLM的评判器和轻量级相关性重排器，以提取高保真奖励信号，同时降低计算成本。该框架在真实世界的云服务任务上进行了评估，展示了其在语义多样化设置下的稳定性和性能提升。这项工作为在专业领域（如化学信息学）部署高效、鲁棒的技术服务代理提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting Large Language Models in complex technical service domains is constrained by the absence of explicit cognitive chains in human demonstrations and the inherent ambiguity arising from the diversity of valid responses. These limitations severely hinder agents from internalizing latent decision dynamics and generalizing effectively. Moreover, practical adaptation is often impeded by the prohibitive resource and time costs associated with standard training paradigms. To overcome these challenges and guarantee computational efficiency, we propose a lightweight adaptation framework comprising three key contributions. (1) Latent Logic Augmentation: We introduce Planning-Aware Trajectory Modeling and Decision Reasoning Augmentation to bridge the gap between surface-level supervision and latent decision logic. These approaches strengthen the stability of Supervised Fine-Tuning alignment. (2) Robust Noise Reduction: We construct a Multiple Ground Truths dataset through a dual-filtering method to reduce the noise by validating diverse responses, thereby capturing the semantic diversity. (3) Lightweight Adaptation: We design a Hybrid Reward mechanism that fuses an LLM-based judge with a lightweight relevance-based Reranker to distill high-fidelity reward signals while reducing the computational cost compared to standard LLM-as-a-Judge reinforcement learning. Empirical evaluations on real-world Cloud service tasks, conducted across semantically diverse settings, demonstrate that our framework achieves stability and performance gains through Latent Logic Augmentation and Robust Noise Reduction. Concurrently, our Hybrid Reward mechanism achieves alignment comparable to standard LLM-as-a-judge methods with reduced training time, underscoring the practical value for deploying technical service agents.

</details>

---

### 3. [CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report](https://arxiv.org/abs/2603.18089)

**基本信息**

- 🔗 arXiv: [`2603.18089`](https://arxiv.org/abs/2603.18089)
- 👥 作者: Thomas Duboudin, Xavier Fontaine, Etienne Andrier 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18089.pdf)

**💡 相关性分析**

满足标准2：论文提出了CytoSyn，一个用于组织病理学图像生成的基础扩散模型，并公开了其权重和数据集。虽然领域是医学影像，但其作为“基础模型”的构建方法、大规模数据集的使用以及生成高质量科学图像的能力，为“化学大模型”主题（特别是涉及分子结构、光谱图像生成或数据增强的模型）提供了重要的数据资源和方法论参考。

**📖 中文摘要**

本文介绍了CytoSyn，一个用于组织病理学的最先进基础潜在扩散模型。该模型能够生成高度逼真且多样化的H&E染色组织病理学图像。论文探索了方法改进、训练集缩放、采样策略和载玻片级过拟合等问题，并推出了改进版CytoSyn-v2。该模型在超过10,000张TCGA诊断性全切片图像（涵盖32种不同癌症类型）的数据集上进行训练。尽管仅在肿瘤学切片上训练，它在生成炎症性肠病图像方面仍保持了最先进的性能。作者公开了模型权重、训练和验证数据集以及合成图像样本。这项工作为计算病理学领域提供了一个强大的生成式基础模型，能够执行特征提取器无法完成的任务（如虚拟染色）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational pathology has made significant progress in recent years, fueling advances in both fundamental disease understanding and clinically ready tools. This evolution is driven by the availability of large amounts of digitized slides and specialized deep learning methods and models. Multiple self-supervised foundation feature extractors have been developed, enabling downstream predictive applications from cell segmentation to tumor sub-typing and survival analysis. In contrast, generative foundation models designed specifically for histopathology remain scarce. Such models could address tasks that are beyond the capabilities of feature extractors, such as virtual staining. In this paper, we introduce CytoSyn, a state-of-the-art foundation latent diffusion model that enables the guided generation of highly realistic and diverse histopathology H&E-stained images, as shown in an extensive benchmark. We explored methodological improvements, training set scaling, sampling strategies and slide-level overfitting, culminating in the improved CytoSyn-v2, and compared our work to PixCell, a state-of-the-art model, in an in-depth manner. This comparison highlighted the strong sensitivity of both diffusion models and performance metrics to preprocessing-specific details such as JPEG compression. Our model has been trained on a dataset obtained from more than 10,000 TCGA diagnostic whole-slide images of 32 different cancer types. Despite being trained only on oncology slides, it maintains state-of-the-art performance generating inflammatory bowel disease images. To support the research community, we publicly release CytoSyn's weights, its training and validation datasets, and a sample of synthetic images in this repository: this https URL .

</details>

---

### 4. [MOSS-TTS Technical Report](https://arxiv.org/abs/2603.18090)

**基本信息**

- 🔗 arXiv: [`2603.18090`](https://arxiv.org/abs/2603.18090)
- 👥 作者: Yitian Gong, Botian Jiang, Yiwei Zhao 等26人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18090.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个语音生成领域的“基础模型”（MOSS-TTS）。虽然领域是语音，但其作为“基础模型”的设计理念、架构（离散令牌、自回归建模、大规模预训练）和追求的能力（可控生成、多语言），与“化学大模型”主题中关于构建通用、可控、可扩展的科学领域基础模型的研究目标高度相关，提供了跨领域的模型构建范式参考。

**📖 中文摘要**

本技术报告介绍了MOSS-TTS，一个基于可扩展配方构建的语音生成基础模型：离散音频令牌、自回归建模和大规模预训练。基于MOSS-Audio-Tokenizer（一种将24 kHz音频压缩到12.5 fps的因果Transformer分词器），报告发布了两款互补的生成器：MOSS-TTS（强调结构简单性、可扩展性和长上下文/控制导向部署）和MOSS-TTS-Local-Transformer（引入了帧局部自回归模块以提高建模效率）。MOSS-TTS支持多语言和开放域设置下的零样本语音克隆、令牌级时长控制、音素/拼音级发音控制、流畅的语码转换和稳定的长文本生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This technical report presents MOSS-TTS, a speech generation foundation model built on a scalable recipe: discrete audio tokens, autoregressive modeling, and large-scale pretraining. Built on MOSS-Audio-Tokenizer, a causal Transformer tokenizer that compresses 24 kHz audio to 12.5 fps with variable-bitrate RVQ and unified semantic-acoustic representations, we release two complementary generators: MOSS-TTS, which emphasizes structural simplicity, scalability, and long-context/control-oriented deployment, and MOSS-TTS-Local-Transformer, which introduces a frame-local autoregressive module for higher modeling efficiency, stronger speaker preservation, and a shorter time to first audio. Across multilingual and open-domain settings, MOSS-TTS supports zero-shot voice cloning, token-level duration control, phoneme-/pinyin-level pronunciation control, smooth code-switching, and stable long-form generation. This report summarizes the design, training recipe, and empirical characteristics of the released models.

</details>

---

### 5. [HWE-Bench: Can Language Models Perform Board-level Schematic Designs?](https://arxiv.org/abs/2603.18102)

**基本信息**

- 🔗 arXiv: [`2603.18102`](https://arxiv.org/abs/2603.18102)
- 👥 作者: Weibo Qiu, Yinhao Xiao, Runyu Pan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18102.pdf)

**💡 相关性分析**

满足标准1和2：1）论文的核心研究内容是评估和推动LLM在复杂工程设计（电路设计）中的能力，这属于“大模型”在专业科学和工程领域应用的前沿探索，与“化学大模型”在化学设计、合成规划等任务中的应用研究主题高度相似。2）论文提出了HWE-Bench评估框架和相关数据集（任务和知识库），这为评估专业领域大模型的能力提供了重要的“数据资源”和基准工具，其方法论可借鉴用于构建化学领域的类似评估基准。

**📖 中文摘要**

本文提出了HWE-Bench，一个评估大型语言模型（LLM）执行板级电路设计能力的框架。该基准包含从开源和众包平台收集的300个板级设计任务，涵盖8个应用领域，并辅以一个包含2,914份真实集成电路数据手册的知识库。对于每个任务，LLM需要根据提供的电路功能要求和一组组件数据手册，从头开始生成原理图。生成的原理图将根据静态电气规则进行检查，然后传递给电路模拟器以验证其动态行为。评估表明，尽管当前模型实现了初步的工程可用性和文档理解能力，但它们缺乏物理直觉，表现最佳的模型总体通过率仅为8.15%。这项工作旨在为开发实用的电子设计自动化（EDA）代理铺平道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated significant potential in various engineering tasks, including software development, digital logic generation, and companion document maintenance. However, their ability to perform board-level circuit design is understudied, as this task requires a synergized understanding of real-world physics and Integrated Circuit (IC) datasheets, the latter comprising detailed specifications for individual components. To address this challenge, we propose \hweb, an evaluation framework that benchmarks the ability of LLMs to perform such designs. It consists of 300 board-level design tasks pulled from open-source and crowdsourcing platforms such as GitHub and OSHWLab, covering 8 application domains, and is complemented with a knowledge base of 2,914 real IC datasheets. For each task, the LLMs are tasked with generating a schematic from scratch, using the provided circuit functional requirements and a set of component datasheets as input. The resulting schematic will be checked against a static electrical rules, and then passed to a circuit simulator to verify its dynamic behavior. Our evaluation show that although current models achieve initial engineering usability and documentation understanding, they lack physical intuition, as the top-performing model achieved an overall pass rate of 8.15\%. We envision that advancements on \hweb\ will pave the way for the development of practical Electronic Design Automation (EDA) agents, revolutionizing the field of board-level design.

</details>

---

### 6. [Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI](https://arxiv.org/abs/2603.18104)

**基本信息**

- 🔗 arXiv: [`2603.18104`](https://arxiv.org/abs/2603.18104)
- 👥 作者: Houston Haynes
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18104.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的、更高效且能保持领域结构（如几何属性）的AI模型训练和部署架构。虽然不特定于化学，但其关注点——为专业领域（如几何和神经形态AI）构建可验证、自适应、资源高效的模型——与“化学大模型”主题中关于开发适用于化学领域、计算高效、可解释且能持续学习的基础模型的研究目标高度一致。

**📖 中文摘要**

本文提出了一种替代性的训练架构，旨在解决主流AI训练基础设施（基于IEEE-754算术的反向模式自动微分）带来的内存开销、优化器复杂性和几何属性退化等问题。该架构基于三个先前成果的组合：维度类型系统和确定性内存管理框架（实现堆栈可分配的梯度分配）、程序超图（保持几何代数计算中的等级不变性）以及b-posit 2026标准（使posit算术在不同硬件目标上易于处理）。它们的组合实现了深度无关的训练内存边界、保持等级不变的权重更新和精确的梯度累积。论文引入了贝叶斯蒸馏机制，通过该训练机制从通用模型中提取潜在先验结构，以解决领域特定训练中的数据稀缺引导问题。此外，还引入了热轮换操作模式，使更新后的模型能够在不中断服务的情况下过渡到活动推理路径。目标是产生一类领域特定的AI系统，这些系统比通用模型更小、更精确、持续自适应、可验证正确，并且可从现有模型初始化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Prevailing AI training infrastructure assumes reverse-mode automatic differentiation over IEEE-754 arithmetic. The memory overhead of training relative to inference, optimizer complexity, and structural degradation of geometric properties through training are consequences of this arithmetic substrate. This paper develops an alternative training architecture grounded in three prior results: the Dimensional Type System and Deterministic Memory Management framework [6], which establishes stack-eligible gradient allocation and exact quire accumulation as design-time verifiable properties; the Program Hypergraph [8], which establishes grade preservation through geometric algebra computations as a type-level invariant; and the b-posit 2026 standard [10], which makes posit arithmetic tractable across hardware targets conventionally considered inference-only. Their composition enables depth-independent training memory bounded to approximately twice the inference footprint, grade-preserving weight updates, and exact gradient accumulation, applicable uniformly to loss-function-optimized and spike-timing-dependent neuromorphic models. We introduce Bayesian distillation, a mechanism by which the latent prior structure of a general-purpose model is extracted through the ADM training regime, resolving the data-scarcity bootstrapping problem for domain-specific training. For deployment, we introduce warm rotation, an operational pattern in which an updated model transitions into an active inference pathway without service interruption, with structural correctness formalized through PHG certificates and signed version records. The result is a class of domain-specific AI systems that are smaller and more precise than general-purpose models, continuously adaptive, verifiably correct with respect to the physical structure of their domains, and initializable from existing models.

</details>

---

### 7. [A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective](https://arxiv.org/abs/2603.18126)

**基本信息**

- 🔗 arXiv: [`2603.18126`](https://arxiv.org/abs/2603.18126)
- 👥 作者: Zhengze Xiao, Xuanzhe Ding, Yuyang Lou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18126.pdf)

**💡 相关性分析**

满足标准1和3：1）论文的核心研究内容是神经网络变分蒙特卡洛（NNVMC），这是一种将深度学习（神经网络）应用于量子化学和物理核心问题（求解多体波函数）的前沿方法。这直接属于“化学大模型”在计算化学和量子模拟中的具体应用和核心研究内容。2）本文是一篇综述性质的论文，系统性地分析了不同NNVMC拟设的计算特性和瓶颈，并展望了未来的协同设计方向，因此也“包含重要的相关讨论”。

**📖 中文摘要**

本文从计算工作负载特征的角度，对神经网络变分蒙特卡洛（NNVMC）方法进行了综述和实证GPU表征分析。NNVMC通过将变分蒙特卡洛与表达性神经网络波函数拟设相结合，已成为解决量子多体问题的一种有前景的范式。论文分析了四种代表性拟设（PauliNet, FermiNet, Psiformer, Orbformer）的模型级运行时和内存趋势，以及通过家族分解、算术强度、屋顶线定位和硬件利用率计数器分析的核级行为。结果表明，端到端性能通常受低强度元素级和数据移动内核的限制，而计算/内存平衡在不同拟设和阶段之间存在显著差异。基于这些发现，论文讨论了可扩展NNVMC系统的算法-硬件协同设计意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Network Variational Monte Carlo (NNVMC) has emerged as a promising paradigm for solving quantum many-body problems by combining variational Monte Carlo with expressive neural-network wave-function ansätze. Although NNVMC can achieve competitive accuracy with favorable asymptotic scaling, practical deployment remains limited by high runtime and memory cost on modern graphics processing units (GPUs). Compared with language and vision workloads, NNVMC execution is shaped by physics-specific stages, including Markov-Chain Monte Carlo sampling, wave-function construction, and derivative/Laplacian evaluation, which produce heterogeneous kernel behavior and nontrivial bottlenecks. This paper provides a workload-oriented survey and empirical GPU characterization of four representative ansätze: PauliNet, FermiNet, Psiformer, and Orbformer. Using a unified profiling protocol, we analyze model-level runtime and memory trends and kernel-level behavior through family breakdown, arithmetic intensity, roofline positioning, and hardware utilization counters. The results show that end-to-end performance is often constrained by low-intensity elementwise and data-movement kernels, while the compute/memory balance varies substantially across ansätze and stages. Based on these findings, we discuss algorithm--hardware co-design implications for scalable NNVMC systems, including phase-aware scheduling, memory-centric optimization, and heterogeneous acceleration.

</details>

---

### 8. [Modeling the human lexicon under temperature variations: linguistic factors, diversity and typicality in LLM word associations](https://arxiv.org/abs/2603.18171)

**基本信息**

- 🔗 arXiv: [`2603.18171`](https://arxiv.org/abs/2603.18171)
- 👥 作者: Maria Andueza Rodriguez, Marie Candito, Richard Huyghe
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18171.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和比较不同大型语言模型（LLM）的内部词汇表征与人类词汇知识的相似性和差异性。这直接关联到“化学大模型”主题中的一个基础且关键的问题：这些模型是否真正理解和内化了专业领域（如化学）的知识结构，还是仅仅在模仿表面模式。该研究为评估化学领域大模型的知识质量提供了方法论参考。

**📖 中文摘要**

本研究通过比较人类和LLM生成的词汇联想，评估模型捕捉人类词汇模式的能力。使用来自SWOW数据集的英语提示-反应对，以及从三个LLM（Mistral-7B, Llama-3.1-8B, Qwen-2.5-32B）在多个温度设置下新生成的联想，论文考察了（i）词频和具体性等词汇因素对提示-反应对的影响，以及（ii）LLM反应与人类反应相比的变异性和典型性。结果表明，所有模型都反映了人类在频率和具体性上的趋势，但在反应变异性和典型性上存在差异。较大的模型（如Qwen）倾向于模拟单一的“原型”人类参与者，产生高度典型但变异最小的反应，而较小的模型（如Mistral和Llama）产生更多变但不太典型的反应。温度设置进一步影响了这种权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) achieve impressive results in terms of fluency in text generation, yet the nature of their linguistic knowledge - in particular the human-likeness of their internal lexicon - remains uncertain. This study compares human and LLM-generated word associations to evaluate how accurately models capture human lexical patterns. Using English cue-response pairs from the SWOW dataset and newly generated associations from three LLMs (Mistral-7B, Llama-3.1-8B, and Qwen-2.5-32B) across multiple temperature settings, we examine (i) the influence of lexical factors such as word frequency and concreteness on cue-response pairs, and (ii) the variability and typicality of LLM responses compared to human responses. Results show that all models mirror human trends for frequency and concreteness but differ in response variability and typicality. Larger models such as Qwen tend to emulate a single "prototypical" human participant, generating highly typical but minimally variable responses, while smaller models such as Mistral and Llama produce more variable yet less typical responses. Temperature settings further influence this trade-off, with higher values increasing variability but decreasing typicality. These findings highlight both the similarities and differences between human and LLM lexicons, emphasizing the need to account for model size and temperature when probing LLM lexical representations.

</details>

---

### 9. [CWoMP: Morpheme Representation Learning for Interlinear Glossing](https://arxiv.org/abs/2603.18184)

**基本信息**

- 🔗 arXiv: [`2603.18184`](https://arxiv.org/abs/2603.18184)
- 👥 作者: Morris Alper, Enora Rice, Bhargav Shandilya 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18184.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的、基于对比学习和语素原子化表示的自然语言处理模型（CWoMP）。虽然应用场景是语言学的语际 glossing，但其核心创新——学习可解释的、原子化的形式-意义单元表示，并支持通过扩展外部知识库（词典）来改进模型而不重新训练——与“化学大模型”和“质谱结构推理”主题高度相关。例如，在质谱解析中，可以将质谱峰或子结构视为“原子单元”，学习其表示，并通过扩展已知的质谱-结构对应知识库来增强推理能力。该工作为构建可解释、可更新的科学领域模型提供了新颖的架构思路。

**📖 中文摘要**

本文提出了CWoMP（对比性词-语素预训练），一种用于语际 glossing（IGT）的语素表示学习方法。与将gloss视为字符序列的现有自动IGT方法不同，CWoMP将语素视为具有学习表示的原子形式-意义单元。一个对比训练的编码器将上下文中的单词与其组成语素在共享嵌入空间中对齐；然后，自回归解码器通过从这些嵌入的可变词典中检索条目来生成语素序列。预测是可解释的——基于词典条目——用户可以通过扩展词典在推理时改进结果，而无需重新训练。论文在多种低资源语言上进行了评估，表明CWoMP在显著提高效率的同时，性能优于现有方法，在极低资源设置下表现尤其出色。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Interlinear glossed text (IGT) is a standard notation for language documentation which is linguistically rich but laborious to produce manually. Recent automated IGT methods treat glosses as character sequences, neglecting their compositional structure. We propose CWoMP (Contrastive Word-Morpheme Pretraining), which instead treats morphemes as atomic form-meaning units with learned representations. A contrastively trained encoder aligns words-in-context with their constituent morphemes in a shared embedding space; an autoregressive decoder then generates the morpheme sequence by retrieving entries from a mutable lexicon of these embeddings. Predictions are interpretable--grounded in lexicon entries--and users can improve results at inference time by expanding the lexicon without retraining. We evaluate on diverse low-resource languages, showing that CWoMP outperforms existing methods while being significantly more efficient, with particularly strong gains in extremely low-resource settings.

</details>

---

### 10. [Retrieval-Augmented LLMs for Security Incident Analysis](https://arxiv.org/abs/2603.18196)

**基本信息**

- 🔗 arXiv: [`2603.18196`](https://arxiv.org/abs/2603.18196)
- 👥 作者: Xavier Cadet, Aditya Vikram Singh, Harsh Mamania 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18196.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个基于大型语言模型（LLM）和检索增强生成（RAG）的自动化分析系统，用于处理多源、复杂的领域数据（安全日志）并完成推理任务（事件重建）。这种方法论——结合领域知识库（查询库、MITRE ATT&CK）、信息检索和LLM推理——与“质谱结构推理”主题高度相关。在质谱解析中，同样需要从复杂的质谱数据中提取特征（“指标”），检索已知的质谱库或结构数据库（“知识库”），并利用模型进行结构推导。该工作为构建用于科学数据分析的智能代理系统提供了可借鉴的技术框架。

**📖 中文摘要**

本文提出了一个基于检索增强生成（RAG）的系统，用于通过基于查询的定向过滤和LLM语义推理进行安全事件分析。该系统使用一个与MITRE ATT&CK技术相关的查询库从原始日志中提取指标，然后检索相关上下文以回答取证问题并重建攻击序列。论文在恶意软件流量事件和多阶段Active Directory攻击上使用五个LLM提供商评估了该系统。研究发现，LLM模型具有不同的性能和权衡，其中Claude Sonnet 4和DeepSeek V3在所有四种恶意软件场景中实现了100%的召回率。在Active Directory场景上的攻击步骤检测达到了100%的精确度和82%的召回率。消融研究证实，RAG架构是必不可少的：没有RAG增强上下文的LLM基线可以正确识别受害主机，但会遗漏所有攻击基础设施。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Investigating cybersecurity incidents requires collecting and analyzing evidence from multiple log sources, including intrusion detection alerts, network traffic records, and authentication events. This process is labor-intensive: analysts must sift through large volumes of data to identify relevant indicators and piece together what happened. We present a RAG-based system that performs security incident analysis through targeted query-based filtering and LLM semantic reasoning. The system uses a query library with associated MITRE ATT\&CK techniques to extract indicators from raw logs, then retrieves relevant context to answer forensic questions and reconstruct attack sequences. We evaluate the system with five LLM providers on malware traffic incidents and multi-stage Active Directory attacks. We find that LLM models have different performance and tradeoffs, with Claude Sonnet~4 and DeepSeek~V3 achieving 100\% recall across all four malware scenarios, while DeepSeek costs 15$\times$ less (\$0.008 vs.\ \$0.12 per analysis). Attack step detection on Active Directory scenarios reaches 100\% precision and 82\% recall. Ablation studies confirm that a RAG architecture is essential: LLM baselines without RAG-enhanced context correctly identify victim hosts but miss all attack infrastructure including malicious domains and command-and-control servers. These results demonstrate that combining targeted query-based filtering with RAG-based retrieval enables accurate, cost-effective security analysis within LLM context limits.

</details>

---

### 11. [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](https://arxiv.org/abs/2603.18256)

**基本信息**

- 🔗 arXiv: [`2603.18256`](https://arxiv.org/abs/2603.18256)
- 👥 作者: Philippe Formont, Maxime Darrin, Ismail Ben Ayed 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18256.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用基于推理的大语言模型进行从头分子生成，这是“化学大模型”在药物发现和分子设计领域的具体应用。

**📖 中文摘要**

本文介绍了MolRGen，这是一个用于训练和评估基于推理的大语言模型（LLM）进行从头分子生成的大规模基准和数据集。该研究旨在弥补现有方法在监督需求上的不足，这些方法通常需要已知属性修饰的分子对作为标签，而这种监督在从头分子生成（目标是生成优化期望得分的新分子）中是不可用的。MolRGen提出了一个用于评估和训练从头分子生成和属性预测模型的设置，并引入了一种新颖的多样性感知top-k评分，以捕捉生成分子的质量和多样性。此外，该研究展示了如何使用强化学习训练一个24B参数的LLM进行分子生成，并对其性能和局限性进行了详细分析。这项工作直接针对化学信息学中的“化学大模型”主题，特别是利用推理LLM进行分子设计和生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in reasoning-based large language models (LLMs) have demonstrated substantial improvements in complex problem-solving tasks. Motivated by these advances, several works have explored the application of reasoning LLMs to drug discovery and molecular design. However, most existing approaches either focus on evaluation or rely on training setups that require ground-truth labels, such as molecule pairs with known property modifications. Such supervision is unavailable in \textit{de novo} molecular generation, where the objective is to generate novel molecules that optimize a desirability score without prior knowledge of high-scoring candidates. To bridge this gap, we introduce MolRGen, a large-scale benchmark and dataset for training and evaluating reasoning-based LLMs on \textit{de novo} molecular generation. Our contributions are threefold. First, we propose a setting to evaluate and train models for \textit{de novo} molecular generation and property prediction. Second, we introduce a novel diversity-aware top-$k$ score that captures both the quality and diversity of generated molecules. Third, we show our setting can be used to train LLMs for molecular generation, training a 24B LLM with reinforcement learning, and we provide a detailed analysis of its performance and limitations.

</details>

---

### 12. [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297)

**基本信息**

- 🔗 arXiv: [`2603.18297`](https://arxiv.org/abs/2603.18297)
- 👥 作者: Zijin Gu, Tatiana Likhomanenko, Vimal Thilak 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18297.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一种新的深度学习框架（离散流匹配）用于从质谱数据中进行从头分子结构解析。

**📖 中文摘要**

本文提出了FlowMS，这是首个用于谱图条件从头分子生成的离散流匹配框架。该框架通过概率空间中的迭代精炼来生成分子图，同时强制执行化学式约束，并基于预训练的公式Transformer编码器提供的谱图嵌入进行条件生成。该方法在NPLIB1基准测试的6项指标中的5项上达到了最先进的性能，包括9.15%的top-1准确率（相对于DiffMS有9.7%的相对改进）和7.96的top-10 MCES（相对于MS-BART有4.2%的改进）。FlowMS将离散流匹配确立为基于质谱的结构解析（如代谢组学和天然产物发现）的一个有前景的新范式。这项工作直接解决了“质谱结构推理”的核心挑战，即从质谱数据中推断分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Mixture-of-Experts (MoE) architectures enable efficient scaling by activating only a subset of parameters for each input. However, conventional MoE routing selects each layer's experts independently, creating N^L possible expert paths -- for N experts across L layers. This far exceeds typical training set sizes, leading to statistical inefficiency as the model may not learn meaningful structure over such a vast path space. To constrain it, we propose \pathmoe, which shares router parameters across consecutive layers. Experiments on 0.9B and 16B parameter models demonstrate consistent improvements on perplexity and downstream tasks over independent routing, while eliminating the need for auxiliary load balancing losses. Analysis reveals that tokens following the same path naturally cluster by linguistic function, with \pathmoe{} producing more concentrated groups, better cross-layer consistency, and greater robustness to routing perturbations. These results offer a new perspective for understanding MoE architectures through the lens of expert paths.

</details>

---

### 13. [Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information](https://arxiv.org/abs/2603.18359)

**基本信息**

- 🔗 arXiv: [`2603.18359`](https://arxiv.org/abs/2603.18359)
- 👥 作者: Shih-Heng Wang, Tiantian Feng, Aditya Kommineni 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18359.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（使用稀疏自编码器解释深度神经表示）与理解和解释“化学大模型”内部表示的研究主题高度相关，可视为该主题在另一个领域（音频）的平行应用。

**📖 中文摘要**

本文研究了神经音频编解码器（NACs）如何编码语言和副语言信息，并致力于通过稀疏自编码器（SAEs）提高其表示的 interpretability。研究聚焦于一个具有挑战性的副语言属性——口音，并提出了一个量化NAC可解释性的框架。作者评估了四种NAC模型在16种SAE配置下的表现，使用相对性能指数进行比较。结果表明，DAC和SpeechTokenizer获得了最高的可解释性。进一步分析揭示，声学导向的NAC主要通过稀疏表示的激活幅度编码口音信息，而语音导向的NAC则更依赖激活位置，并且低比特率的EnCodec变体显示出更高的可解释性。虽然论文主要关注音频，但其核心方法论——使用稀疏自编码器分解和解释深度神经表示的复杂信息——与化学信息学中理解“化学大模型”（如分子表示模型）内部工作机制的研究目标高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented NACs encode accent information primarily in activation magnitudes of sparse representations, whereas phonetic-oriented NACs rely more on activation positions, and that low-bitrate EnCodec variants show higher interpretability.

</details>

---

### 14. [Synthetic Data Generation for Training Diversified Commonsense Reasoning Models](https://arxiv.org/abs/2603.18361)

**基本信息**

- 🔗 arXiv: [`2603.18361`](https://arxiv.org/abs/2603.18361)
- 👥 作者: Tianhui Zhang, Bei Peng, Danushka Bollegala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18361.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种生成合成数据的方法论，可用于创建训练多样化生成模型（如化学领域的分子生成大模型）所需的数据集，这为相关主题提供了数据资源构建思路。

**📖 中文摘要**

本文针对训练多样化常识推理模型缺乏大规模高质量训练数据的问题，提出了一种两阶段方法来创建首个合成数据集CommonSyn。该数据集用于多样化生成式常识推理（GCR）。研究表明，在合成数据上微调的模型，与在人工标注数据集上微调的模型相比，能够同时提高生成多样性和质量。这项工作通过生成合成数据来解决资源瓶颈，直接支持“化学大模型”中一个关键子方向的发展：即训练能够产生多样化、高质量输出的生成模型。虽然论文以通用对话代理为背景，但其解决数据稀缺问题的方法论（合成数据生成）和提升模型多样化输出的目标，对于化学领域训练能够生成多样化、合理分子结构的“化学大模型”具有直接的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Conversational agents are required to respond to their users not only with high quality (i.e. commonsense bearing) responses, but also considering multiple plausible alternative scenarios, reflecting the diversity in their responses. Despite the growing need to train diverse commonsense generators, the progress of this line of work has been significantly hindered by the lack of large-scale high-quality diverse commonsense training datasets. Due to the high annotation costs, existing Generative Commonsense Reasoning (GCR) datasets are created using a small number of human annotators, covering only a narrow set of commonsense scenarios. To address this training resource gap, we propose a two-stage method to create the first-ever synthetic dataset CommonSyn for diversified (GCR). The model fine-tuned on our synthetic data jointly increase both generation diversity and quality compared with vanilla models and the model fine-tuned on human-crafted dataset across different size Large Language Models (LLMs)

</details>

---

### 15. [Seeking Universal Shot Language Understanding Solutions](https://arxiv.org/abs/2603.18448)

**基本信息**

- 🔗 arXiv: [`2603.18448`](https://arxiv.org/abs/2603.18448)
- 👥 作者: Haoxin Liu, Harshavardhan Kamarthi, Zhiyuan Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18448.pdf)

**💡 相关性分析**

满足标准3：论文构建了一个大规模、多任务的视觉语言理解基准套件（SLU-SUITE），并提出了通用解决方案。虽然其直接应用领域是电影分析，但其核心方法论——构建高质量、多维度标注的数据集以训练和评估视觉语言模型在专业领域的理解能力——与化学信息学和质谱分析中构建用于化学大模型或质谱结构推理的视觉语言基准高度相关。论文的讨论为如何系统性地评估和提升模型在专业视觉领域的理解能力提供了重要参考。

**📖 中文摘要**

本文介绍了SLU-SUITE，一个用于镜头语言理解（SLU）的综合训练与评估套件，包含33个任务、跨越六个电影维度的49万个人工标注的问答对。SLU-SUITE旨在解决当前视觉语言模型（VLMs）在SLU任务上与电影专家判断存在差异的问题。该研究从模型和数据两个角度分析了VLM在SLU任务上的瓶颈，并提出了两种互补的通用SLU解决方案：UniShot（通过动态平衡数据混合训练的通用模型）和AgentShots（最大化各维度性能的专家集群）。这项工作提供了一个大规模、多维度、高质量的数据集和基准，可用于训练和评估面向化学信息学（如分子结构可视化分析）和质谱分析（如光谱图模式识别）等领域的视觉语言模型，提升其在复杂、专业视觉推理任务上的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Shot language understanding (SLU) is crucial for cinematic analysis but remains challenging due to its diverse cinematographic dimensions and subjective expert judgment. While vision-language models (VLMs) have shown strong ability in general visual understanding, recent studies reveal judgment discrepancies between VLMs and film experts on SLU tasks. To address this gap, we introduce SLU-SUITE, a comprehensive training and evaluation suite containing 490K human-annotated QA pairs across 33 tasks spanning six film-grounded dimensions. Using SLU-SUITE, we originally observe two insights into VLM-based SLU from: the model side, which diagnoses key bottlenecks of modules; the data side, which quantifies cross-dimensional influences among tasks. These findings motivate our universal SLU solutions from two complementary paradigms: UniShot, a balanced one-for-all generalist trained via dynamic-balanced data mixing, and AgentShots, a prompt-routed expert cluster that maximizes peak dimension performance. Extensive experiments show that our models outperform task-specific ensembles on in-domain tasks and surpass leading commercial VLMs by 22% on out-of-domain tasks.

</details>

---

### 16. [Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images](https://arxiv.org/abs/2603.18461)

**基本信息**

- 🔗 arXiv: [`2603.18461`](https://arxiv.org/abs/2603.18461)
- 👥 作者: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18461.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种整合单细胞RNA测序数据（细胞类型原型）与病理图像分析的方法（CPNN）。单细胞RNA测序数据是化学信息学和系统生物学中至关重要的分子水平数据集。该方法框架展示了如何利用外部、结构化的化学/生物学数据资源来增强视觉模型的预测能力和可解释性，这与“数据资源相关”标准高度契合，为化学信息学中多模态数据融合提供了范例。

**📖 中文摘要**

本文提出了一种细胞类型原型信息神经网络（CPNN），用于从病理图像中估计基因表达谱。该方法的关键创新在于利用公开可用的单细胞RNA测序数据来估计细胞类型原型（即稳定的基因-基因共变模式下的平均表达谱）。CPNN直接从图像中学习细胞类型组成权重，并建模原型与观测到的批量或空间表达之间的关系，从而提供了一个基于生物学基础且结构正则化的预测框架。该方法在三个切片级数据集和三个空间转录组学数据集上进行了评估，均取得了最高的斯皮尔曼相关性性能。这项工作展示了如何将单细胞测序数据（一种重要的生物化学数据资源）与视觉模型相结合，实现从图像到分子表达的可解释性预测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Estimating slide- and patch-level gene expression profiles from pathology images enables rapid and low-cost molecular analysis with broad clinical impact. Despite strong results, existing approaches treat gene expression as a mere slide- or spot-level signal and do not incorporate the fact that the measured expression arises from the aggregation of underlying cell-level expression. To explicitly introduce this missing cell-resolved guidance, we propose a Cell-type Prototype-informed Neural Network (CPNN) that leverages publicly available single-cell RNA-sequencing datasets. Since single-cell measurements are noisy and not paired with histology images, we first estimate cell-type prototypes-mean expression profiles that reflect stable gene-gene co-variation this http URL then learns cell-type compositional weights directly from images and models the relationship between prototypes and observed bulk or spatial expression, providing a biologically grounded and structurally regularized prediction framework. We evaluate CPNN on three slide-level datasets and three patch-level spatial transcriptomics datasets. Across all settings, CPNN achieves the highest performance in terms of Spearman correlation. Moreover, by visualizing the inferred compositional weights, our framework provides interpretable insights into which cell types drive the predicted expression. Code is publicly available at this https URL .

</details>

---

### 17. [Cognitive Mismatch in Multimodal Large Language Models for Discrete Symbol Understanding](https://arxiv.org/abs/2603.18472)

**基本信息**

- 🔗 arXiv: [`2603.18472`](https://arxiv.org/abs/2603.18472)
- 👥 作者: Yinghui Li, Jiayi Kuang, Peng Xing 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18472.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕多模态大模型（属于“化学大模型”的广义范畴）在理解化学结构等科学符号方面的能力进行评估和诊断。它明确将化学结构作为关键的测试领域，旨在揭示当前大模型在科学符号理解上的根本性缺陷，这与“化学大模型”主题高度相关。

**📖 中文摘要**

本文研究了多模态大语言模型（MLLMs）在处理离散符号（如数学公式、化学结构、语言字符）方面的能力，并引入了一个全面的基准来评估MLLMs在语言、文化、数学、物理和化学五个领域中的“离散语义空间”导航能力。研究发现了一个反直觉的现象：模型在基本符号识别上经常失败，却在复杂推理任务上成功，这表明它们依赖的是语言概率而非真正的视觉感知。通过揭示这种“认知不匹配”，该工作凸显了当前AI在真正感知和理解支撑科学发现与抽象思维的符号语言方面存在显著差距。论文特别将化学结构列为需要精确、深入解释的离散符号领域之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Multimodal Large Language Models (MLLMs) have achieved remarkable success in interpreting natural scenes, their ability to process discrete symbols -- the fundamental building blocks of human cognition -- remains a critical open question. Unlike continuous visual data, symbols such as mathematical formulas, chemical structures, and linguistic characters require precise, deeper interpretation. This paper introduces a comprehensive benchmark to evaluate how top-tier MLLMs navigate these "discrete semantic spaces" across five domains: language, culture, mathematics, physics, and chemistry. Our investigation uncovers a counterintuitive phenomenon: models often fail at basic symbol recognition yet succeed in complex reasoning tasks, suggesting they rely on linguistic probability rather than true visual perception. By exposing this "cognitive mismatch", we highlight a significant gap in current AI capabilities: the struggle to truly perceive and understand the symbolic languages that underpin scientific discovery and abstract thought. This work offers a roadmap for developing more rigorous, human-aligned intelligent systems.

</details>

---

### 18. [Leveraging Large Language Models for Generalizing Peephole Optimizations](https://arxiv.org/abs/2603.18477)

**基本信息**

- 🔗 arXiv: [`2603.18477`](https://arxiv.org/abs/2603.18477)
- 👥 作者: Chunhao Liao, Hongxu Xu, Xintong Zhou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18477.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型（LLM）来自动化程序优化规则的泛化。虽然应用领域是编译器优化，但其核心是探索和利用“化学大模型”所代表的通用大模型在结构化模式识别、规则提取和泛化方面的能力。这属于大模型在专业领域（此处为程序分析）应用的研究，与“化学大模型”主题在方法论层面相关。

**📖 中文摘要**

本文提出了LPG（大语言模型辅助的窥孔优化泛化）框架，该框架利用大语言模型（LLMs）来泛化窥孔优化（一种编译器优化技术）。LPG采用一个闭环工作流，集成了LLM驱动的符号常量泛化、结构泛化、约束松弛和位宽/精度泛化，并通过语法验证、语义验证和收益检查进行反馈。作者在从LLVM生态系统中提取的真实世界窥孔优化问题上评估了LPG，结果表明LPG成功泛化了102个优化中的90个。这项工作展示了LLMs在理解和泛化程序模式方面的能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Peephole optimizations are a core component of modern optimizing compilers. It rewrites specific instruction into semantically equivalent but more efficient forms. In practice, creating a new peephole optimization often starts from a concrete optimization instance and requires lifting it into a more general rewrite rule that matches a wider range of instruction patterns. This generalization step is critical to optimization effectiveness, but it is also difficult: producing rules that are both correct and sufficiently general typically demands substantial manual effort and domain expertise. Existing approaches such as Hydra attempt to automate this task with program synthesis, but their generalization capability is often limited by search-space explosion, under-generalization, and restricted support for diverse instruction domains. We present LPG, large language model aided peephole optimization generalization, a framework that uses large language models (LLMs) to generalize peephole optimizations. The design of LPG is motivated by the observation that LLMs are effective at semantic abstraction and exploratory reasoning, while formal analyses are necessary to ensure that generated rules are sound and profitable. Based on this observation, LPG adopts a closed-loop workflow that integrates LLM-driven symbolic constant generalization, structural generalization, constraint relaxation, and bitwidth/precision generalization with feedback from syntactic validation, semantic verification, and profitability checking. We evaluate LPG on real-world peephole optimization issues drawn from the LLVM ecosystem. Overall, LPG successfully generalizes 90 out of 102 optimizations. On the integer-focused subset that is directly comparable to Hydra, LPG generalizes 74 out of 81 optimizations, whereas Hydra generalizes 35.

</details>

---

### 19. [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505)

**基本信息**

- 🔗 arXiv: [`2603.18505`](https://arxiv.org/abs/2603.18505)
- 👥 作者: Jingzhi Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18505.pdf)

**💡 相关性分析**

满足标准3：论文是一篇专门针对AI在蛋白质科学（化学和生命科学的核心领域）中应用的综述。它详细讨论了生成式AI模型（如扩散模型）、多模态表示学习、以及从结构到功能的推理，这些内容与“化学大模型”和“质谱结构推理”（后者可视为蛋白质/分子结构解析的一种技术）的研究前沿高度重叠。该综述提供了该领域重要的相关讨论和未来展望。

**📖 中文摘要**

本文是一篇系统性综述，全面审视了人工智能驱动的蛋白质科学从静态结构预测向动态构象集合和复杂生物分子相互作用建模的范式转变。综述涵盖了五个相互关联的维度：统一的多模态表示（整合序列、几何和文本知识）；通过无MSA架构和全原子复合物建模改进静态预测；生成式框架（包括扩散模型和流匹配）以捕获与热力学集合一致的构象分布；异质相互作用（蛋白质-配体、蛋白质-核酸、蛋白质-蛋白质复合物）的预测；以及对适应度景观、突变效应和文本引导属性预测的功能推断。文章批判性分析了当前瓶颈，并指出了未来方向，如物理一致的生成模型、多模态基础架构和实验闭环系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular interactions. This review systematically examines the paradigm shift in AI driven protein science across five interconnected dimensions: unified multimodal representations that integrate sequences, geometries, and textual knowledge; refinement of static prediction through MSA free architectures and all atom complex modeling; generative frameworks, including diffusion models and flow matching, that capture conformational distributions consistent with thermodynamic ensembles; prediction of heterogeneous interactions spanning protein ligand, protein nucleic acid, and protein protein complexes; and functional inference of fitness landscapes, mutational effects, and text guided property prediction. We critically analyze current bottlenecks, including data distribution biases, limited mechanistic interpretability, and the disconnect between geometric metrics and biophysical reality, while identifying future directions toward physically consistent generative models, multimodal foundation architectures, and experimental closed loop systems. This methodological transformation marks artificial intelligence's transition from a structural analysis tool into a universal simulator capable of understanding and ultimately rewriting the dynamic language of life.

</details>

---

### 20. [SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks](https://arxiv.org/abs/2603.18548)

**基本信息**

- 🔗 arXiv: [`2603.18548`](https://arxiv.org/abs/2603.18548)
- 👥 作者: Amanda A. Howard, Nicholas Zolman, Bruno Jacob 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18548.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是结合Kolmogorov-Arnold网络（KANs，一种新型神经网络架构）与稀疏识别非线性动力学（SINDy）来发现可解释的数学模型。这属于“化学大模型”范畴内对模型可解释性、以及从数据中发现物理/化学规律（类似于从质谱数据推理结构）的新方法探索。论文展示了如何利用新型网络架构提升模型在科学发现任务中的性能，与主题直接相关。

**📖 中文摘要**

本文提出了SINDy-KANs方法，将稀疏识别非线性动力学（SINDy）与Kolmogorov-Arnold网络（KANs）相结合。该方法同时训练一个KAN和一个类似SINDy的表征，通过在每个激活函数级别应用SINDy来增加KAN表征的可解释性，同时保持深度KAN可能实现的函数组合。作者将该方法应用于一系列符号回归任务，包括动力系统，以展示其在各种系统中准确的方程发现能力。KANs作为一种新兴的可解释机器学习架构，与SINDy（一种从数据中发现稀疏方程的系统识别方法）的结合，为从数据中学习可解释的数学模型提供了新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method to a number of symbolic regression tasks, including dynamical systems, to show accurate equation discovery across a range of systems.

</details>

---

### 21. [CAPSUL: A Comprehensive Human Protein Benchmark for Subcellular Localization](https://arxiv.org/abs/2603.18571)

**基本信息**

- 🔗 arXiv: [`2603.18571`](https://arxiv.org/abs/2603.18571)
- 👥 作者: Yicheng Hu, Xinyu Lin, Shulin Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18571.pdf)

**💡 相关性分析**

满足标准2：论文提出了CAPSUL基准，这是一个专门为蛋白质亚细胞定位任务构建的、整合了3D结构信息的数据集。蛋白质3D结构是化学信息学和结构生物学的核心数据。该基准的发布为训练和评估能够利用3D结构信息的化学大模型（特别是用于蛋白质相关任务）提供了重要的数据资源。

**📖 中文摘要**

本文引入了CAPSUL基准，一个用于蛋白质亚细胞定位的综合人类蛋白质基准。该基准的数据集整合了多样化的3D结构表示与由领域专家精心策划的细粒度亚细胞定位注释。作者使用各种最先进的基于序列和基于结构的模型评估了这个基准，展示了在该任务中引入结构特征的重要性。此外，作者还通过案例研究展示了基于结构的方法的强大可解释性，例如在高尔基体定位中通过注意力机制发现了一个决定性的定位模式α-螺旋。这项工作为在蛋白质亚细胞定位任务中应用基于结构的方法提供了理论基础和实用评估工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Subcellular localization is a crucial biological task for drug target identification and function annotation. Although it has been biologically realized that subcellular localization is closely associated with protein structure, no existing dataset offers comprehensive 3D structural information with detailed subcellular localization annotations, thus severely hindering the application of promising structure-based models on this task. To address this gap, we introduce a new benchmark called $\mathbf{CAPSUL}$, a $\mathbf{C}$omprehensive hum$\mathbf{A}$n $\mathbf{P}$rotein benchmark for $\mathbf{SU}$bcellular $\mathbf{L}$ocalization. It features a dataset that integrates diverse 3D structural representations with fine-grained subcellular localization annotations carefully curated by domain experts. We evaluate this benchmark using a variety of state-of-the-art sequence-based and structure-based models, showcasing the importance of involving structural features in this task. Furthermore, we explore reweighting and single-label classification strategies to facilitate future investigation on structure-based methods for this task. Lastly, we showcase the powerful interpretability of structure-based methods through a case study on the Golgi apparatus, where we discover a decisive localization pattern $\alpha$-helix from attention mechanisms, demonstrating the potential for bridging the gap with intuitive biological interpretability and paving the way for data-driven discoveries in cell biology.

</details>

---

### 22. [Elastic Weight Consolidation Done Right for Continual Learning](https://arxiv.org/abs/2603.18596)

**基本信息**

- 🔗 arXiv: [`2603.18596`](https://arxiv.org/abs/2603.18596)
- 👥 作者: Xuan Liu, Xiaobin Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18596.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（分析并修正基于梯度的模型权重重要性估计方法）直接为构建和优化“化学大模型”提供了关键的理论工具和方法论。化学大模型作为复杂的深度学习模型，同样面临模型稳定性、灾难性遗忘和参数重要性评估的挑战，本文的研究可直接应用于此类模型的持续学习和适应过程。

**📖 中文摘要**

本文对持续学习中的权重正则化方法进行了系统性分析，重点关注了基于梯度的权重重要性估计。论文的核心是分析弹性权重巩固（EWC）及其变体在估计权重重要性时存在的根本性错位问题，并提出了Logits Reversal（LR）操作来修正EWC的重要性估计。虽然论文主要关注通用机器学习模型的持续学习，但其核心方法——通过分析模型梯度（Fisher信息矩阵）来理解和修正模型参数的重要性——与构建和优化“化学大模型”高度相关。化学大模型（如用于分子性质预测或生成的深度学习模型）同样面临灾难性遗忘和模型稳定性问题。本文提出的分析框架和修正方法（LR操作）为如何评估和稳定大模型中关键参数（可能对应特定的化学功能或结构特征）提供了直接的理论工具和方法论启示，可应用于化学信息学领域大模型的持续学习和适应新数据场景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight regularization methods in continual learning (CL) alleviate catastrophic forgetting by assessing and penalizing changes to important model weights. Elastic Weight Consolidation (EWC) is a foundational and widely used approach within this framework that estimates weight importance based on gradients. However, it has consistently shown suboptimal performance. In this paper, we conduct a systematic analysis of importance estimation in EWC from a gradient-based perspective. For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios. Our analysis also reveals that Memory Aware Synapses (MAS), a variant of EWC, imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection. Consequently, both EWC and its variants exhibit fundamental misalignments in estimating weight importance, leading to inferior performance. To tackle these issues, we propose the Logits Reversal (LR) operation, a simple yet effective modification that rectifies EWC's importance estimation. Specifically, reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection. Extensive experiments across various CL tasks and datasets show that the proposed method significantly outperforms existing EWC and its variants. Therefore, we refer to it as EWC Done Right (EWC-DR).

</details>

---

### 23. [GEAR: Geography-knowledge Enhanced Analog Recognition Framework in Extreme Environments](https://arxiv.org/abs/2603.18626)

**基本信息**

- 🔗 arXiv: [`2603.18626`](https://arxiv.org/abs/2603.18626)
- 👥 作者: Zelin Liu, Bocheng Li, Yuling Zhou 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18626.pdf)

**💡 相关性分析**

满足标准1：论文提出的形态集成孪生图网络（MSG-Net）是图神经网络的一种创新应用，用于处理结构化科学数据并关联下游任务。这直接与“质谱结构推理”的核心技术（使用图神经网络从质谱数据推断分子图结构）相关，为后者提供了模型架构和方法论上的参考。

**📖 中文摘要**

本文提出了GEAR框架，用于在极端环境（如马里亚纳海沟和青藏高原）中进行跨域地形相似性检索，以识别结构同源的陆地类似物。该框架的核心创新之一是设计了一种基于图神经网络的形态集成孪生图网络（MSG-Net），该网络基于地貌学指标进行建模。论文明确指出，使用MSG-Net提取的特征与生物数据存在显著相关性，这为未来的生物分析提供了证据。虽然论文主要应用于地理学和生物学领域，但其核心方法——使用图神经网络（GNN）处理复杂的、结构化的科学数据（地形特征），并建立与下游科学任务（生物分析）的关联——与“质谱结构推理”高度相关。在质谱分析中，分子结构可以自然地表示为图（原子为节点，化学键为边），图神经网络正是进行质谱到结构推理的主流和核心方法。本文提出的MSG-Net架构及其在跨域相似性检索和特征关联分析上的成功应用，为质谱结构推理中图神经网络模型的设计和优化提供了有价值的参考范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Mariana Trench and the Qinghai-Tibet Plateau exhibit significant similarities in geological origins and microbial metabolic functions. Given that deep-sea biological sampling faces prohibitive costs, recognizing structurally homologous terrestrial analogs of the Mariana Trench on the Qinghai-Tibet Plateau is of great significance. Yet, no existing model adequately addresses cross-domain topographic similarity retrieval, either neglecting geographical knowledge or sacrificing computational efficiency. To address these challenges, we present \underline{\textbf{G}}eography-knowledge \underline{\textbf{E}}nhanced \underline{\textbf{A}}nalog \underline{\textbf{R}}ecognition (\textbf{GEAR}) Framework, a three-stage pipeline designed to efficiently retrieve analogs from 2.5 million square kilometers of the Qinghai-Tibet Plateau: (1) Skeleton guided Screening and Clipping: Recognition of candidate valleys and initial screening based on size and linear morphological criteria. (2) Physics aware Filtering: The Topographic Waveform Comparator (TWC) and Morphological Texture Module (MTM) evaluate the waveform and texture and filter out inconsistent candidate valleys. (3) Graph based Fine Recognition: We design a \underline{\textbf{M}}orphology-integrated \underline{\textbf{S}}iamese \underline{\textbf{G}}raph \underline{\textbf{N}}etwork (\textbf{MSG-Net}) based on geomorphological metrics. Correspondingly, we release an expert-annotated topographic similarity dataset targeting tectonic collision zones. Experiments demonstrate the effectiveness of every stage. Besides, MSG-Net achieved an F1-Score 1.38 percentage points higher than the SOTA baseline. Using features extracted by MSG-Net, we discovered a significant correlation with biological data, providing evidence for future biological analysis.

</details>

---

### 24. [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660)

**基本信息**

- 🔗 arXiv: [`2603.18660`](https://arxiv.org/abs/2603.18660)
- 👥 作者: Peihang Wu, Zehong Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18660.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对计算病理学的综述，但其系统分析的技术方向（如自监督表示学习、令牌压缩、多模态整合）是构建“化学大模型”和处理“质谱结构推理”等高维科学数据的通用且核心的前沿技术。论文提供了重要的相关技术讨论和领域进展展望。

**📖 中文摘要**

本文是一篇关于多模态计算病理学的综述，系统性地分析了该领域的四个研究方向。其中，第一个方向“全切片图像的自监督表示学习和结构感知的令牌压缩”与“化学大模型”和“质谱结构推理”均有潜在关联。1) 对于化学大模型：综述中讨论的自监督学习、令牌压缩和参数高效适应等策略，是构建和训练大规模科学模型（包括化学模型）的通用且关键的技术。这些技术如何应用于高分辨率、多模态的科学数据（如病理图像），其经验可直接迁移至处理复杂的化学数据（如分子图、光谱序列）。2) 对于质谱结构推理：质谱数据也是一种高维、序列化的科学数据。综述中针对全切片图像提出的“结构感知令牌压缩”技术，其思想（在压缩表示时保留关键结构信息）对于处理长序列质谱数据、提取关键特征以用于结构推理具有启发意义。此外，综述对多模态信息整合和模型可解释性的讨论也与构建端到端的质谱分析系统相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Whole slide imaging (WSI) has transformed digital pathology by enabling computational analysis of gigapixel histopathology images. Recent foundation model advances have accelerated progress in computational pathology, facilitating joint reasoning across pathology images, clinical reports, and structured data. Despite this progress, challenges remain: the extreme resolution of WSIs creates computational hurdles for visual learning; limited expert annotations constrain supervised approaches; integrating multimodal information while preserving biological interpretability remains difficult; and the opacity of modeling ultra-long visual sequences hinders clinical transparency. This review comprehensively surveys recent advances in multimodal computational pathology. We systematically analyze four research directions: (1) self-supervised representation learning and structure-aware token compression for WSIs; (2) multimodal data generation and augmentation; (3) parameter-efficient adaptation and reasoning-enhanced few-shot learning; and (4) multi-agent collaborative reasoning for trustworthy diagnosis. We specifically examine how token compression enables cross-scale modeling and how multi-agent mechanisms simulate a pathologist's "Chain of Thought" across magnifications to achieve uncertainty-aware evidence fusion. Finally, we discuss open challenges and argue that future progress depends on unified multimodal frameworks integrating high-resolution visual data with clinical and biomedical knowledge to support interpretable and safe AI-assisted diagnosis.

</details>

---

### 25. [STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation](https://arxiv.org/abs/2603.18688)

**基本信息**

- 🔗 arXiv: [`2603.18688`](https://arxiv.org/abs/2603.18688)
- 👥 作者: Chen Zhang, Liwei Liu, Jun Tao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18688.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容（为稀疏、异构的科学时间序列设计预训练框架）直接针对“质谱结构推理”中的数据挑战（质谱是一种科学时间序列）。2) 论文提出的STEP框架本身是一种用于学习科学时间序列通用表征的工具和方法，可直接作为“质谱结构推理”任务的基础编码器或特征提取器。

**📖 中文摘要**

本文提出了STEP框架，一个用于科学时间序列编码器预训练的跨域蒸馏框架。科学时间序列（如质谱信号）通常具有稀疏、异构和数据规模有限的特点，这与论文试图解决的问题高度一致。STEP框架系统地评估了来自相关领域（如音频、通用时间序列、脑信号）的预训练基础模型向科学任务的迁移能力和互补性，并提出通过跨域蒸馏将多个基础模型的知识整合到一个统一的编码器中。这项工作与“质谱结构推理”直接相关：质谱正是一种典型的科学时间序列数据。STEP框架所解决的挑战（数据稀疏、异构、小规模）正是质谱分析中常遇到的问题。其方法论——利用相关领域预训练模型的知识、通过自适应分块处理极端长度序列、通过统计补偿适应不同数值尺度——为构建用于质谱分析的通用、可迁移的深度表示学习模型提供了直接的技术路线和解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientific tasks and their complementary strengths. Based on this observation, we propose STEP, a Scientific Time Series Encoder Pretraining framework via cross domain distillation. STEP introduces adaptive patching to handle extreme-length sequences and a statistics compensation scheme to accommodate diverse numerical scales. It further leverages cross-domain distillation to integrate knowledge from multiple foundation models into a unified encoder. By combining complementary representations across different domains, STEP learns general-purpose and transferable features tailored for scientific signals. Experiments on seven scientific time series tasks demonstrate that STEP provides both an effective structure and an effective pretraining paradigm, taking a STEP toward scientific time series representation learning.

</details>

---

### 26. [Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN](https://arxiv.org/abs/2603.18766)

**基本信息**

- 🔗 arXiv: [`2603.18766`](https://arxiv.org/abs/2603.18766)
- 👥 作者: Marcio Augusto Sampaio, Paulo Henrique Ranazzi, Martin Julian Blunt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18766.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究方法（集成VAE-GAN深度生成模型进行复杂非高斯科学参数的表征与反演）直接与“化学大模型”（分子生成与表征）和“质谱结构推理”（从数据反演结构）的技术内核相关，为解决化学领域的类似问题提供了可迁移的模型框架和算法思路。

**📖 中文摘要**

本文研究将深度生成模型VAE-GAN与集成平滑器数据同化方法（ESMDA）相结合，用于石油储层模拟中的历史匹配和参数反演。核心创新在于利用VAE-GAN对非高斯分布的储层属性（如渗透率）进行参数化，即将复杂的非高斯参数映射到高斯潜空间进行同化更新，再映射回原始域。虽然应用领域是地质建模，但其核心技术——使用深度生成模型（VAE-GAN）对复杂、非高斯分布的科学实体进行表征、压缩和重建——与“化学大模型”和“质谱结构推理”高度相关。在化学信息学中，分子结构、性质分布也常是非高斯的。本文的方法为：1) 化学大模型：提供了如何利用混合生成模型（结合VAE的编码能力和GAN的生成质量）来学习和生成符合化学规则的分子结构分布。2) 质谱结构推理：提供了从观测数据（如生产曲线）反演底层复杂参数（如储层属性）的框架，这与从质谱数据反演分子结构是类似的逆问题。论文验证了VAE-GAN在同时保证生成质量和数据匹配方面的优势，这对化学领域的生成和推理任务具有重要参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Currently, the methods called Iterative Ensemble Smoothers, especially the method called Ensemble Smoother with Multiple Data Assimilation (ESMDA) can be considered state-of-the-art for history matching in petroleum reservoir simulation. However, this approach has two important limitations: the use of an ensemble with finite size to represent the distributions and the Gaussian assumption in parameter and data uncertainties. This latter is particularly important because many reservoir properties have non-Gaussian distributions. Parameterization involves mapping non-Gaussian parameters to a Gaussian field before the update and then mapping them back to the original domain to forward the ensemble through the reservoir simulator. A promising approach to perform parameterization is through deep learning models. Recent studies have shown that Generative Adversarial Networks (GAN) performed poorly concerning data assimilation, but generated more geologically plausible realizations of the reservoir, while the Variational Autoencoder (VAE) performed better than the GAN in data assimilation, but generated less geologically realistic models. This work is innovative in combining the strengths of both to implement a deep learning model called Variational Autoencoder Generative Adversarial Network (VAE-GAN) integrated with ESMDA. The methodology was applied in two case studies, one case being categorical and the other with continuous values of permeability. Our findings demonstrate that by applying the VAE-GAN model we can obtain high quality reservoir descriptions (just like GANs) and a good history matching on the production curves (just like VAEs) simultaneously.

</details>

---

### 27. [dTRPO: Trajectory Reduction in Policy Optimization of Diffusion Large Language Models](https://arxiv.org/abs/2603.18806)

**基本信息**

- 🔗 arXiv: [`2603.18806`](https://arxiv.org/abs/2603.18806)
- 👥 作者: Wenxuan Zhang, Lemeng Wu, Changsheng Zhao 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学领域中的“化学大模型”（具体为扩散大语言模型，dLLMs）的优化方法展开。

**📖 中文摘要**

本文提出了一种名为dTRPO（轨迹缩减策略优化）的新方法，旨在改进扩散大语言模型（dLLMs）的策略优化。dLLMs是一种用于语言生成的新范式，其对齐人类偏好面临挑战。dTRPO的核心是通过减少轨迹概率计算成本来扩展离线策略训练。作者证明，在参考策略正则化下，新解掩码标记的概率比是中间扩散状态概率比的无偏估计，并且完整轨迹的概率可以通过对重新掩码的最终状态进行单次前向传递来有效估计。通过将这两种轨迹缩减策略整合到策略优化目标中，dTRPO在指令遵循和推理基准测试中显著提升了最先进dLLMs的核心性能，在STEM任务上提升高达9.6%，在编码任务上提升高达4.3%，在指令遵循任务上提升高达3.0%。此外，由于其离线和单次前向的特性，dTRPO展现出强大的训练效率，并通过高质量输出提高了生成效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion Large Language Models (dLLMs) introduce a new paradigm for language generation, which in turn presents new challenges for aligning them with human preferences. In this work, we aim to improve the policy optimization for dLLMs by reducing the cost of the trajectory probability calculation, thereby enabling scaled-up offline policy training. We prove that: (i) under reference policy regularization, the probability ratio of the newly unmasked tokens is an unbiased estimate of that of intermediate diffusion states, and (ii) the probability of the full trajectory can be effectively estimated with a single forward pass of a re-masked final state. By integrating these two trajectory reduction strategies into a policy optimization objective, we propose Trajectory Reduction Policy Optimization (dTRPO). We evaluate dTRPO on 7B dLLMs across instruction-following and reasoning benchmarks. Results show that it substantially improves the core performance of state-of-the-art dLLMs, achieving gains of up to 9.6% on STEM tasks, up to 4.3% on coding tasks, and up to 3.0% on instruction-following tasks. Moreover, dTRPO exhibits strong training efficiency due to its offline, single-forward nature, and achieves improved generation efficiency through high-quality outputs.

</details>

---

### 28. [Seasoning Generative Models for a Generalization Aftertaste](https://arxiv.org/abs/2603.18817)

**基本信息**

- 🔗 arXiv: [`2603.18817`](https://arxiv.org/abs/2603.18817)
- 👥 作者: Hisham Husain, Valentin De Bortoli, Richard Nock
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18817.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕生成模型（包括扩散模型）的泛化理论，属于“化学大模型”相关的基础模型理论与方法范畴。

**📖 中文摘要**

本文探讨了使用判别器来训练或微调生成模型（如生成对抗网络和扩散模型）的框架。作者扩展了一个与f-散度相关的强对偶性结果，从而产生了一个判别器引导的“精炼”方法，该方法可以改进任何生成模型。理论分析表明，与未经精炼的模型相比，精炼后的生成模型可以证明性地改善泛化能力，其泛化差距的改进基于用于精炼的判别器集合的Rademacher复杂度。该工作为现有的基于分数的扩散方法（已在实证中取得巨大成功）提供了理论验证，并有助于从整体上理解生成模型的泛化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The use of discriminators to train or fine-tune generative models has proven to be a rather successful framework. A notable example is Generative Adversarial Networks (GANs) that minimize a loss incurred by training discriminators along with other paradigms that boost generative models via discriminators that satisfy weak learner constraints. More recently, even diffusion models have shown advantages with some kind of discriminator guidance. In this work, we extend a strong-duality result related to $f$-divergences which gives rise to a discriminator-guided recipe that allows us to \textit{refine} any generative model. We then show that the refined generative models provably improve generalization, compared to its non-refined counterpart. In particular, our analysis reveals that the gap in generalization is improved based on the Rademacher complexity of the discriminator set used for refinement. Our recipe subsumes a recently introduced score-based diffusion approach (Kim et al., 2022) that has shown great empirical success, however allows us to shed light on the generalization guarantees of this method by virtue of our analysis. Thus, our work provides a theoretical validation for existing work, suggests avenues for new algorithms, and contributes to our understanding of generalization in generative models at large.

</details>

---

### 29. [Pore-scale modeling of capillary-driven binder migration during battery electrode drying](https://arxiv.org/abs/2603.18860)

**基本信息**

- 🔗 arXiv: [`2603.18860`](https://arxiv.org/abs/2603.18860)
- 👥 作者: Marcel Weichel, Martin Reder, Gerit Mühlberg 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18860.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学与材料科学交叉领域的微观过程建模，涉及电池电极制造（化学过程）的模拟与优化，与化学信息学中的计算建模主题高度相关。

**📖 中文摘要**

本文提出了一个空间分辨的孔隙尺度连续介质模型，用于模拟钠离子电池硬碳电极干燥过程中，由毛细作用驱动的粘结剂迁移。电极干燥是制造过程中的关键步骤，因为孔隙排空期间的粘结剂迁移会影响电极的机械完整性和电化学性能。现有模型主要依赖一维薄膜收缩阶段或忽略毛细传输，缺乏对粘结剂迁移的物理一致、微观结构解析的预测。该模型被应用于具有不同平均粒径的硬碳微观结构。模拟结果表明，较小的颗粒尺寸导致更均匀的粘结剂分布，而较高的蒸发速率和增加的表面张力会促进更强的粘结剂梯度。溶剂粘度的变化对粘结剂迁移影响较小。最终，模拟证明了对毛细传输和微观结构效应的显式描述对于准确预测粘结剂迁移至关重要，并为电极干燥过程的针对性优化提供了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sodium-ion batteries employing hard carbon electrodes are considered a drop-in technology for lithium-ion batteries. Electrode drying is a critical manufacturing step, as binder migration during pore emptying impacts the mechanical integrity and electrical performance of the electrode. Existing modeling approaches predominantly rely on the film shrinkage phase in a one dimensional way or neglect the capillary transport, resulting in a lack of physically consistent microstructure resolved predictions of binder migration. In this work, a spatially resolved pore scale continuum model is extended to explicitly describe capillary driven binder transport during pore emptying. The model is applied to hard carbon microstructures with varying mean particle diameters. The simulations reveal that smaller particle sizes lead to a more homogeneous binder distribution, whereas higher evaporation rates and increased surface tension promote stronger binder gradients. Variations in solvent viscosity show only a minor influence on binder migration, as long as no hydrophilic or hydrophobic behavior is present. Finally, the simulations demonstrate that an explicit description of capillary transport and microstructural effects is essential for accurately predicting binder migration and provides a basis for the targeted optimization of electrode drying processes.

</details>

---

### 30. [RadioDiff-FS: Physics-Informed Manifold Alignment in Few-Shot Diffusion Models for High-Fidelity Radio Map Construction](https://arxiv.org/abs/2603.18865)

**基本信息**

- 🔗 arXiv: [`2603.18865`](https://arxiv.org/abs/2603.18865)
- 👥 作者: Xiucheng Wang, Zixuan Guo, Nan Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18865.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散模型（一种重要的生成式大模型）的少样本领域自适应方法，属于“化学大模型”可应用的生成模型方法论范畴。

**📖 中文摘要**

本文提出了RadioDiff-FS，一个基于扩散模型的少样本学习框架，用于高保真无线电地图构建。无线电地图对于6G网络规划至关重要，但高保真构建具有挑战性。严格的电磁求解器计算延迟高，而数据驱动模型需要大量标注数据且从简化模拟到复杂多径环境的泛化能力差。RadioDiff-FS将预训练的主路径生成器适配到多径丰富的目标域，仅需少量高保真样本。该适配基于一个理论分解：将多径无线电地图分解为主导的主路径分量和方向稀疏的残差。该分解表明跨域偏移对应于有界且几何结构化的特征平移，而非任意的分布变化。作者引入了方向一致性损失来约束扩散分数沿着物理上合理的传播方向更新，从而抑制低数据状态下出现的相位不一致伪影。实验表明，RadioDiff-FS在静态和动态无线电地图上相对于原始扩散基线显著降低了归一化均方误差。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Radio maps (RMs) provide spatially continuous propagation characterizations essential for 6G network planning, but high-fidelity RM construction remains challenging. Rigorous electromagnetic solvers incur prohibitive computational latency, while data-driven models demand massive labeled datasets and generalize poorly from simplified simulations to complex multipath environments. This paper proposes RadioDiff-FS, a few-shot diffusion framework that adapts a pre-trained main-path generator to multipath-rich target domains with only a small number of high-fidelity samples. The adaptation is grounded in a theoretical decomposition of the multipath RM into a dominant main-path component and a directionally sparse residual. This decomposition shows that the cross-domain shift corresponds to a bounded and geometrically structured feature translation rather than an arbitrary distribution change. A Direction-Consistency Loss (DCL) is then introduced to constrain diffusion score updates along physically plausible propagation directions, suppressing phase-inconsistent artifacts that arise in the low-data regime. Experiments show that RadioDiff-FS reduces NMSE by 59.5% on static RMs and by 74.0% on dynamic RMs relative to the vanilla diffusion baseline, achieving an SSIM of 0.9752 and a PSNR of 36.37 dB under severely limited supervision.

</details>

---

### 31. [MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model](https://arxiv.org/abs/2603.18892)

**基本信息**

- 🔗 arXiv: [`2603.18892`](https://arxiv.org/abs/2603.18892)
- 👥 作者: Youngwan Lee, Soojin Jang, Yoorhim Cho 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18892.pdf)

**💡 相关性分析**

满足标准3：论文是专门针对视觉语言模型（VLMs）空间推理能力的综述与基准构建工作，包含了对该主题的重要讨论和评估，属于大模型（视觉大模型）能力评估与分析的范畴。

**📖 中文摘要**

本文介绍了MultihopSpatial，一个用于评估视觉语言模型（VLMs）多跳组合空间推理能力的综合基准。空间推理是VLMs的基础能力，尤其是当它们作为视觉-语言-动作代理部署在物理环境中时。现有基准主要关注基本的单跳关系，忽略了现实场景中至关重要的多跳组合推理和精确视觉 grounding。MultihopSpatial提供了三个关键贡献：(1) 一个为多跳和组合空间推理设计的综合基准，包含跨不同空间视角的1到3跳复杂查询。(2) Acc@50IoU，一个同时评估推理和视觉 grounding 的补充指标，要求模型既选择答案又预测精确的边界框——这对于稳健的VLA部署至关重要。(3) MultihopSpatial-Train，一个专门的大规模训练语料库，旨在培养空间智能。对37个最先进VLM的广泛评估得出了八个关键见解，揭示了组合空间推理仍然是一个巨大的挑战。最后，作者证明在该语料库上进行强化学习后训练可以同时提升VLM的内在空间推理能力和下游具身操作性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Spatial reasoning is foundational for Vision-Language Models (VLMs), particularly when deployed as Vision-Language-Action (VLA) agents in physical environments. However, existing benchmarks predominantly focus on elementary, single-hop relations, neglecting the multi-hop compositional reasoning and precise visual grounding essential for real-world scenarios. To address this, we introduce MultihopSpatial, offering three key contributions: (1) A comprehensive benchmark designed for multi-hop and compositional spatial reasoning, featuring 1- to 3-hop complex queries across diverse spatial perspectives. (2) Acc@50IoU, a complementary metric that simultaneously evaluates reasoning and visual grounding by requiring both answer selection and precise bounding box prediction - capabilities vital for robust VLA deployment. (3) MultihopSpatial-Train, a dedicated large-scale training corpus to foster spatial intelligence. Extensive evaluation of 37 state-of-the-art VLMs yields eight key insights, revealing that compositional spatial reasoning remains a formidable challenge. Finally, we demonstrate that reinforcement learning post-training on our corpus enhances both intrinsic VLM spatial reasoning and downstream embodied manipulation performance.

</details>

---

### 32. [Neural Galerkin Normalizing Flow for Transition Probability Density Functions of Diffusion Models](https://arxiv.org/abs/2603.18907)

**基本信息**

- 🔗 arXiv: [`2603.18907`](https://arxiv.org/abs/2603.18907)
- 👥 作者: Riccardo Saporiti, Fabio Nobile
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18907.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用归一化流（一种生成模型）和神经伽辽金方法求解Fokker-Planck方程，属于生成模型（化学大模型相关技术）在科学计算和概率密度估计中的应用。

**📖 中文摘要**

本文提出了一个新的神经伽辽金归一化流框架，用于通过求解相应的Fokker-Planck方程来近似扩散过程的转移概率密度函数，参数化地处理初始质量的位置。通过使用归一化流，作者将解寻找为参考随机过程转移概率密度函数的变换，确保近似是结构保持的，并自动满足正性和质量守恒约束。通过将神经伽辽金方案扩展到归一化流的背景下，作者推导出了归一化流参数时间演化的常微分方程组。自适应采样例程用于在有意义的位置评估Fokker-Planck残差，这对于处理高维偏微分方程至关重要。数值结果表明，该策略捕捉了真实解的关键特征，并加强了初始数据与后续时间密度函数之间的因果关系。在完成离线训练阶段后，在线评估变得比从头求解偏微分方程成本效益高得多。所提出的方法作为一个有前景的代理模型，可用于与随机微分方程相关的许多查询问题，如贝叶斯推断、模拟和扩散桥生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Neural Galerkin Normalizing Flow framework to approximate the transition probability density function of a diffusion process by solving the corresponding Fokker-Planck equation with an atomic initial distribution, parametrically with respect to the location of the initial mass. By using Normalizing Flows, we look for the solution as a transformation of the transition probability density function of a reference stochastic process, ensuring that our approximation is structure-preserving and automatically satisfies positivity and mass conservation constraints. By extending Neural Galerkin schemes to the context of Normalizing Flows, we derive a system of ODEs for the time evolution of the Normalizing Flow's parameters. Adaptive sampling routines are used to evaluate the Fokker-Planck residual in meaningful locations, which is of vital importance to address high-dimensional PDEs. Numerical results show that this strategy captures key features of the true solution and enforces the causal relationship between the initial datum and the density function at subsequent times. After completing an offline training phase, online evaluation becomes significantly more cost-effective than solving the PDE from scratch. The proposed method serves as a promising surrogate model, which could be deployed in many-query problems associated with stochastic differential equations, like Bayesian inference, simulation, and diffusion bridge generation.

</details>

---

### 33. [Theoretical Analyses of Detectors for Additive Noise Channels with Mean-Variance Uncertainty under Nonlinear Expectation Theory](https://arxiv.org/abs/2603.18937)

**基本信息**

- 🔗 arXiv: [`2603.18937`](https://arxiv.org/abs/2603.18937)
- 👥 作者: Wen-Xuan Lang, Guiying Yan, Zhi-Ming Ma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18937.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕在模型不确定性下的信号检测理论，属于化学信息学和质谱分析中数据处理与信号推断的基础方法论范畴，与“质谱结构推理”中处理噪声和不确定性的思想相通。

**📖 中文摘要**

本文在非线性期望理论的框架下，将加性噪声信道的最优检测器分析扩展到信道噪声概率模型不确定的情况。作者考虑了两种类型的不确定性：一种是无均值不确定性但有方差不确定性，另一种是均值和方差均存在不确定性。作者推导了在这两种情况下，基于非线性期望最优准则的二进制输入加性噪声信道的最优检测器，并给出了其显式形式。研究发现，均值不确定性显著影响最优检测器的形式，而方差不确定性则不影响。此外，作者提出了一种信道噪声不确定参数的估计方法。最后，作者给出了新推导的最优检测器的理论分析和模拟性能结果，并将其与基于确定性概率模型的经典信息论中的最优检测器性能进行了比较。实验结果表明，在大多数具有不确定概率模型的场景中，新的检测方法优于传统方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In classical information theory, both the form and performance of the optimal detector for additive noise channels can be precisely derived, based on the assumption that the channel noise follows a specific probability distribution or a mixture of known distributions, or that the exact distribution exists but is unknown. In this paper, we extend the analyses of detectors for additive noise channel to the situation where the probability model for analyzing channels is uncertain, utilizing nonlinear expectation theory. We consider two types of distribution uncertainties: one with no mean uncertainty but with variance uncertainty, and another with both mean and variance uncertainties. We derive the optimal detectors for binary input additive noise channel under the nonlinear expectation optimal criterion for both scenarios and provide their explicit forms. Our findings reveal that mean uncertainty significantly influences the form of the optimal detector, whereas variance uncertainty does not. Additionally, we propose an estimation method for the uncertain parameters of the channel noise. Finally, we present theoretical analyses and simulated performance results of the newly derived optimal detectors, and compare these results with the performance of optimal detector under classical information theory, which assumes a deterministic probability model. The results of experiments show that our new detection methods outperform conventional methods in most scenarios with uncertain probability models, showing the practical relevance of our theoretical contributions.

</details>

---

### 34. [BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery](https://arxiv.org/abs/2603.18957)

**基本信息**

- 🔗 arXiv: [`2603.18957`](https://arxiv.org/abs/2603.18957)
- 👥 作者: Sijian Fan, Liyan Xiong, Dayuan Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18957.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学中的关键任务——药物发现（包括耐药性预测和药物重定位），提出了一种新的贝叶斯矩阵补全与变量选择模型，用于整合和分析化学/生物侧边信息。

**📖 中文摘要**

本文提出了BVSIMC（贝叶斯变量选择引导的归纳矩阵补全），一种新的贝叶斯模型，用于在药物发现中从侧边特征中进行变量选择。通过学习稀疏的潜在嵌入，BVSIMC提高了预测准确性和可解释性。作者通过模拟研究和两个药物发现应用验证了该方法：1) 预测结核分枝杆菌的耐药性，2) 预测计算药物重定位中的新药-疾病关联。在合成数据和真实数据上，BVSIMC在预测方面优于其他几种最先进的方法。在两个真实例子中，BVSIMC进一步揭示了最具临床意义的侧边特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in drug discovery have demonstrated that incorporating side information (e.g., chemical properties about drugs and genomic information about diseases) often greatly improves prediction performance. However, these side features can vary widely in relevance and are often noisy and high-dimensional. We propose Bayesian Variable Selection-Guided Inductive Matrix Completion (BVSIMC), a new Bayesian model that enables variable selection from side features in drug discovery. By learning sparse latent embeddings, BVSIMC improves both predictive accuracy and interpretability. We validate our method through simulation studies and two drug discovery applications: 1) prediction of drug resistance in Mycobacterium tuberculosis, and 2) prediction of new drug-disease associations in computational drug repositioning. On both synthetic and real data, BVSIMC outperforms several other state-of-the-art methods in terms of prediction. In our two real examples, BVSIMC further reveals the most clinically meaningful side features.

</details>

---

### 35. [CRAFT: Aligning Diffusion Models with Fine-Tuning Is Easier Than You Think](https://arxiv.org/abs/2603.18991)

**基本信息**

- 🔗 arXiv: [`2603.18991`](https://arxiv.org/abs/2603.18991)
- 👥 作者: Zening Sun, Zhengpeng Xie, Lichen Bai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18991.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散模型（一种重要的生成式大模型）的高效对齐与微调方法，直接属于“化学大模型”中模型优化与训练的前沿议题。

**📖 中文摘要**

本文提出了CRAFT（复合奖励辅助微调），一种轻量级但强大的扩散模型微调范式，该范式在保持计算效率的同时显著减少了训练数据需求。扩散模型对齐在生成高质量、符合人类偏好的图像方面取得了显著突破。现有技术，如监督微调（SFT）和DPO风格的偏好优化，已成为微调扩散模型的原理性工具。然而，SFT依赖于高质量图像（获取成本高），而DPO风格的方法依赖于大规模偏好数据集（质量往往不一致）。除了数据依赖性，这些方法还受到计算效率低下的限制。CRAFT首先利用复合奖励过滤技术构建高质量且一致的训练数据集，然后执行增强版的SFT。作者还从理论上证明，CRAFT实际上优化了基于组的强化学习的下界，从而在选定数据的SFT和强化学习之间建立了原理性的联系。广泛的实证结果表明，仅使用100个样本的CRAFT可以轻松超越使用数千个偏好配对样本的最新SOTA偏好优化方法。此外，CRAFT甚至可以实现比基线偏好优化方法快11-220倍的收敛速度，突显了其极高的效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Aligning Diffusion models has achieved remarkable breakthroughs in generating high-quality, human preference-aligned images. Existing techniques, such as supervised fine-tuning (SFT) and DPO-style preference optimization, have become principled tools for fine-tuning diffusion models. However, SFT relies on high-quality images that are costly to obtain, while DPO-style methods depend on large-scale preference datasets, which are often inconsistent in quality. Beyond data dependency, these methods are further constrained by computational inefficiency. To address these two challenges, we propose Composite Reward Assisted Fine-Tuning (CRAFT), a lightweight yet powerful fine-tuning paradigm that requires significantly reduced training data while maintaining computational efficiency. It first leverages a Composite Reward Filtering (CRF) technique to construct a high-quality and consistent training dataset and then perform an enhanced variant of SFT. We also theoretically prove that CRAFT actually optimizes the lower bound of group-based reinforcement learning, establishing a principled connection between SFT with selected data and reinforcement learning. Our extensive empirical results demonstrate that CRAFT with only 100 samples can easily outperform recent SOTA preference optimization methods with thousands of preference-paired samples. Moreover, CRAFT can even achieve 11-220$\times$ faster convergences than the baseline preference optimization methods, highlighting its extremely high efficiency.

</details>

---

### 36. [Foundations of Schrödinger Bridges for Generative Modeling](https://arxiv.org/abs/2603.18992)

**基本信息**

- 🔗 arXiv: [`2603.18992`](https://arxiv.org/abs/2603.18992)
- 👥 作者: Sophia Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18992.pdf)

**💡 相关性分析**

满足标准3：论文是对薛定谔桥理论及其在生成式建模中应用的系统性综述与教程，属于“化学大模型”所依赖的生成模型基础理论的深度讨论与展望。

**📖 中文摘要**

本文深入探讨了薛定谔桥问题的数学基础，及其与现代生成式建模（包括扩散模型、基于分数的模型和流匹配）的内在联系。在现代生成式建模框架的核心，是通过概率空间中的随机路径将简单的先验分布转换为复杂的目标分布。薛定谔桥提供了一个统一的原则，将问题框架化为在边际分布约束下确定一个最优的随机桥，该桥与预定义的参考过程具有最小熵偏差。本指南利用最优传输、随机控制和路径空间优化等工具，发展了薛定谔桥问题的数学基础，并侧重于其与现代生成式建模直接相关的动态公式。作者从第一性原理出发，构建了一个用于构建薛定谔桥的综合工具包，并展示了这些构造如何产生广义的和任务特定的计算方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

At the core of modern generative modeling frameworks, including diffusion models, score-based models, and flow matching, is the task of transforming a simple prior distribution into a complex target distribution through stochastic paths in probability space. Schrödinger bridges provide a unifying principle underlying these approaches, framing the problem as determining an optimal stochastic bridge between marginal distribution constraints with minimal-entropy deviations from a pre-defined reference process. This guide develops the mathematical foundations of the Schrödinger bridge problem, drawing on optimal transport, stochastic control, and path-space optimization, and focuses on its dynamic formulation with direct connections to modern generative modeling. We build a comprehensive toolkit for constructing Schrödinger bridges from first principles, and show how these constructions give rise to generalized and task-specific computational methods.

</details>

---

### 37. [SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141)

**基本信息**

- 🔗 arXiv: [`2603.19141`](https://arxiv.org/abs/2603.19141)
- 👥 作者: Mingxing Zhang, Nicola Rossberg, Simone Innocente 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19141.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于光谱数据分析的可解释机器学习框架（SHAPCA）。光谱数据（如质谱）是化学信息学和质谱分析的核心数据类型，该框架提供了处理此类高维、共线性数据的工具和方法，可用于构建或分析质谱结构推理模型。

**📖 中文摘要**

本文提出SHAPCA，一个用于光谱数据的可解释机器学习流程。该流程结合主成分分析（PCA）进行降维和SHAP（Shapley Additive exPlanations）进行事后解释，旨在解决光谱数据的高维度和强共线性带来的模型可解释性挑战。SHAPCA能够在原始输入空间（即光谱波段）提供解释，使从业者能够将预测结果与生物组分联系起来。该框架支持全局和局部分析，揭示了驱动整体模型行为的光谱波段以及影响单个预测的实例特定特征。数值分析证明了结果的可解释性以及不同运行间更高的一致性。这项工作直接与化学信息学相关，因为它处理的是化学和生物医学分析中常见的光谱数据集（如质谱、红外光谱），并专注于提高此类数据上机器学习模型的稳定性和可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

</details>

---

### 38. [UGID: Unified Graph Isomorphism for Debiasing Large Language Models](https://arxiv.org/abs/2603.19144)

**基本信息**

- 🔗 arXiv: [`2603.19144`](https://arxiv.org/abs/2603.19144)
- 👥 作者: Zikang Ding, Junchi Yao, Junhao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19144.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通过建模和约束模型内部计算图（图同构）来理解和控制大模型行为的新框架（UGID）。这种方法论对于构建可控、可解释的“化学大模型”（例如用于分子性质预测或结构解析的模型）具有直接的相关性，因为化学领域模型同样需要处理复杂的内部表示和推理过程。

**📖 中文摘要**

本文提出UGID（统一图同构去偏），一种针对大语言模型内部表示层面的去偏框架。UGID将Transformer建模为一个结构化的计算图，其中注意力机制定义图的边，隐藏状态定义图的节点。去偏被表述为在反事实输入上强制图结构不变性，只允许敏感属性存在差异。UGID联合约束偏见敏感区域的注意力路由和隐藏表示，有效防止偏见在架构组件间迁移。为了在不降低通用能力的情况下实现有效的行为对齐，引入了对敏感逻辑的空间约束和基于选择性锚点的目标以保留定义语义。大量实验表明UGID有效减少了分布内和分布外设置下的偏见。该研究虽然针对LLM，但其核心思想——通过建模和约束模型内部计算图的结构来控制和理解模型行为——与构建可控、可解释的“化学大模型”高度相关。例如，在质谱结构推理中，理解模型如何根据质谱数据推断分子结构需要类似的内部表示分析和约束技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) exhibit pronounced social biases. Output-level or data-optimization--based debiasing methods cannot fully resolve these biases, and many prior works have shown that biases are embedded in internal representations. We propose \underline{U}nified \underline{G}raph \underline{I}somorphism for \underline{D}ebiasing large language models (\textit{\textbf{UGID}}), an internal-representation--level debiasing framework for large language models that models the Transformer as a structured computational graph, where attention mechanisms define the routing edges of the graph and hidden states define the graph nodes. Specifically, debiasing is formulated as enforcing invariance of the graph structure across counterfactual inputs, with differences allowed only on sensitive attributes. \textit{\textbf{UGID}} jointly constrains attention routing and hidden representations in bias-sensitive regions, effectively preventing bias migration across architectural components. To achieve effective behavioral alignment without degrading general capabilities, we introduce a log-space constraint on sensitive logits and a selective anchor-based objective to preserve definitional semantics. Extensive experiments on large language models demonstrate that \textit{\textbf{UGID}} effectively reduces bias under both in-distribution and out-of-distribution settings, significantly reduces internal structural discrepancies, and preserves model safety and utility.

</details>

---

### 39. [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](https://arxiv.org/abs/2603.19183)

**基本信息**

- 🔗 arXiv: [`2603.19183`](https://arxiv.org/abs/2603.19183)
- 👥 作者: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19183.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心是使用稀疏自编码器（SAE）对多模态大模型（VLA）进行机制可解释性分析，这属于大模型内部表示和推理过程研究的重要部分。虽然应用场景是机器人，但该方法论（SAE分析、特征操控）对于理解和改进“化学大模型”和“质谱结构推理”模型具有直接的借鉴意义，可视为相关的重要讨论和方法。

**📖 中文摘要**

本文应用机制可解释性技术来理解视觉-语言-动作（VLA）模型的内部工作机制。为了探测内部表示，作者在VLA的隐藏层激活上训练稀疏自编码器（SAE）。SAE学习一个稀疏字典，其特征作为模型计算的紧凑、可解释的基础。研究发现，大多数提取的SAE特征对应于特定训练演示中的记忆序列，但也有一些特征对应于可解释的、通用的、可操控的运动基元和语义属性。作者提出了一个指标，根据特征是代表可泛化的可转移基元还是特定于情节的记忆来对特征进行分类。通过LIBERO基准测试上的操控实验验证了这些发现，表明单个SAE特征可以因果性地影响机器人行为。这项工作提供了第一个机制证据，表明VLA可以跨任务和场景学习可泛化的特征。该研究展示了如何使用SAE等工具来分析和操控复杂多模态模型的内部表示，这种方法论同样适用于分析和理解“化学大模型”的内部工作机制，例如模型如何从质谱数据中学习并推理出分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for general-purpose robot manipulation. However, their generalization is inconsistent: while these models can perform impressively in some settings, fine-tuned variants often fail on novel objects, scenes, and instructions. We apply mechanistic interpretability techniques to better understand the inner workings of VLA models. To probe internal representations, we train Sparse Autoencoders (SAEs) on hidden layer activations of the VLA. SAEs learn a sparse dictionary whose features act as a compact, interpretable basis for the model's computation. We find that the large majority of extracted SAE features correspond to memorized sequences from specific training demonstrations. However, some features correspond to interpretable, general, and steerable motion primitives and semantic properties, offering a promising glimpse toward VLA generalizability. We propose a metric to categorize features according to whether they represent generalizable transferable primitives or episode-specific memorization. We validate these findings through steering experiments on the LIBERO benchmark. We show that individual SAE features causally influence robot behavior. Steering general features induces behaviors consistent with their semantic meaning and can be applied across tasks and scenes. This work provides the first mechanistic evidence that VLAs can learn generalizable features across tasks and scenes. We observe that supervised fine-tuning on small robotics datasets disproportionately amplifies memorization. In contrast, training on larger, more diverse datasets (e.g., DROID) or using knowledge insulation promotes more general features. We provide an open-source codebase and user-friendly interface for activation collection, SAE training, and feature steering. Our project page is located at this http URL

</details>

---

### 40. [MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185)

**基本信息**

- 🔗 arXiv: [`2603.19185`](https://arxiv.org/abs/2603.19185)
- 👥 作者: Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19185.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估扩散模型（一种重要的生成模型架构）在合成数据生成中的隐私性。扩散模型是构建“化学大模型”（如用于分子生成或性质预测的模型）的关键技术之一，因此该研究直接与化学大模型的主题相关。

**📖 中文摘要**

本文介绍了MIDST挑战赛，旨在定量评估由扩散模型生成的合成表格数据的隐私增益，特别关注其对成员推理攻击（MIA）的抵抗力。鉴于表格数据的异质性和复杂性，研究探索了多个目标模型进行MIA，包括用于混合数据类型单表的扩散模型和具有互连约束的多关系表。MIDST的一个关键成果是启发了针对这些目标扩散模型的新型黑盒和白盒MIA的开发，从而能够全面评估其隐私效能。虽然论文主要关注隐私和合成数据生成，但扩散模型是生成式AI和“化学大模型”潜在架构的重要组成部分。该研究对评估生成模型（包括可能用于分子生成或质谱模拟的模型）的隐私性和稳健性具有方法论意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at this https URL

</details>

---

### 41. [Biased AI can Influence Political Decision-Making](https://arxiv.org/abs/2410.06415)

**基本信息**

- 🔗 arXiv: [`2410.06415`](https://arxiv.org/abs/2410.06415)
- 👥 作者: Jillian Fisher, Shangbin Feng, Robert Aron 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.06415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（Cliqueformer架构）在化学设计任务上进行了评估和应用，这直接关联到利用大模型进行化学设计与优化的主题，即"化学大模型"的应用范畴。

**📖 中文摘要**

论文标题为"Cliqueformer: Model-Based Optimization with Structured Transformers"。该研究提出了一种基于Transformer的架构Cliqueformer，用于解决模型驱动的优化问题。它通过学习黑盒函数的结构（通过功能图模型）来处理分布偏移，而无需依赖显式的保守方法。研究在多个领域进行了评估，包括化学和遗传设计任务。虽然论文主要关注通用的模型驱动优化框架，但其明确提到在化学设计任务上的应用，这使其与"化学大模型"这一主题间接相关。化学大模型的核心目标之一正是为了分子/材料的设计与优化，Cliqueformer提供了一种利用Transformer结构和函数结构知识进行此类优化的方法，可被视为一种服务于化学设计目标的特定模型架构或方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As modern large language models (LLMs) become integral to everyday tasks, concerns about their inherent biases and their potential impact on human decision-making have emerged. While bias in models are well-documented, less is known about how these biases influence human decisions. This paper presents two interactive experiments investigating the effects of partisan bias in LLMs on political opinions and decision-making. Participants interacted freely with either a biased liberal, biased conservative, or unbiased control model while completing these tasks. We found that participants exposed to partisan biased models were significantly more likely to adopt opinions and make decisions which matched the LLM's bias. Even more surprising, this influence was seen when the model bias and personal political partisanship of the participant were opposite. However, we also discovered that prior knowledge of AI was weakly correlated with a reduction of the impact of the bias, highlighting the possible importance of AI education for robust mitigation of bias effects. Our findings not only highlight the critical effects of interacting with biased LLMs and its ability to impact public discourse and political conduct, but also highlights potential techniques for mitigating these risks in the future.

</details>

---

### 42. [Degrees of Freedom of Cache-Aided Interference Channels Assisted by Active Intelligent Reflecting Surfaces](https://arxiv.org/abs/2411.17559)

**基本信息**

- 🔗 arXiv: [`2411.17559`](https://arxiv.org/abs/2411.17559)
- 👥 作者: Abolfazl Changizi, Ali H. Abdollahi Bafghi, Mahtab Mirmohseni 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.17559.pdf)

**💡 相关性分析**

不相关。论文核心研究内容是无线通信中的缓存和干扰管理，与"化学大模型"或"质谱结构推理"无任何关联。

**📖 中文摘要**

论文标题为"Degrees of Freedom of Cache-Aided Interference Channels Assisted by Active Intelligent Reflecting Surfaces"。该研究从信息论角度研究了由主动智能反射面辅助的缓存无线网络。它联合设计了内容放置、传输阶段和IRS系数，并提出了一种单次可达方案。该方案利用了发射机合作、缓存内容、干扰对齐和IRS能力。研究推导了不同缓存大小、网络配置和IRS元素数量下的可实现单次和自由度，并给出了上界。论文属于无线通信领域，与化学信息学或质谱分析无直接关联。其内容完全不涉及化学结构、分子数据、质谱或相关的大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper studies cache-aided wireless networks in the presence of active intelligent reflecting surfaces (IRSs) from an information-theoretic perspective. Specifically, we investigate interference management in a cache-aided wireless network assisted by an active IRS to enhance the achievable degrees of freedom (DoF). To this end, we jointly design the content placement, delivery phase, and IRS coefficients, and propose a one-shot achievability scheme. Our scheme exploits transmitters' cooperation, cache contents, interference alignment, and IRS capabilities, based on the network parameters. We derive the achievable one-shot sum-DoF for different cache sizes, network configurations, and numbers of IRS elements, followed by an upper bound. Our results highlight the potential of deploying an IRS in cache-aided wireless communication systems. In particular, they underscore the enhancement of achievable DoF for various parameter regimes, especially when cache sizes are inadequate. Notably, we show that access to an IRS with a sufficient number of elements enables the achievement of the maximum possible DoF for various parameter regimes of interest.

</details>

---

### 43. [DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models](https://arxiv.org/abs/2503.16426)

**基本信息**

- 🔗 arXiv: [`2503.16426`](https://arxiv.org/abs/2503.16426)
- 👥 作者: Keyan Chen, Chenyang Liu, Bowen Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.16426.pdf)

**💡 相关性分析**

不相关。论文研究的是遥感图像的视觉基础模型，虽然涉及"大模型"和特定领域的模型设计，但其领域（遥感）和任务（视觉感知）与指定的化学信息学和质谱分析主题无关。

**📖 中文摘要**

论文标题为"DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models"。该研究针对遥感图像中目标极度稀疏和空间冗余巨大的特点，提出了一个名为DynamicVis的视觉基础模型。它引入了一个动态区域感知的状态空间模型，自适应地路由和增量建模仅与任务相关的高显著性token，同时采用参数无关的集成来处理背景上下文，从而大幅降低了处理超长2D token序列的复杂度。为了赋予网络强大的空间选择能力，研究提出了一种新颖的区域级元嵌入多实例学习预训练范式。该模型在包括小目标检测和变化检测在内的九个下游任务上进行了广泛评估。论文属于计算机视觉和遥感领域，核心是设计高效的视觉基础模型来处理特定类型的图像数据。其内容不涉及化学分子、质谱数据或相关的推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The advancement of RS technology has enabled high-resolution Earth observation; however, interpreting these images using modern VFMs remains a significant challenge. Unlike object-centric natural images, RS imagery is fundamentally characterized by extreme target sparsity and massive spatial redundancy. Key objects of interest (e.g., ships, vehicles) often occupy less than 1% of the spatial extent, surrounded by vast, target-free backgrounds. Existing VFMs predominantly rely on uniform dense processing (e.g., ViTs) and pixel-reconstruction pre-training paradigms (e.g., MAE). These approaches inherently waste substantial computational capacity on modeling redundant backgrounds and inadvertently dilute the feature representations of small, sparse targets. To bridge this structural misalignment, we propose DynamicVis, a visual foundation model explicitly tailored to the sparse nature of RS imagery. Architecturally, DynamicVis introduces a Dynamic Region-Aware SSM that bypasses uniform computation. It adaptively routes and incrementally models only task-relevant, high-salience tokens while employing a parameter-free integration for background context, drastically reducing the complexity of processing ultra-long 2D token sequences ($\sim$100,000). Crucially, to equip the network with robust spatial-selection capabilities, we propose a novel Region-Level Meta-Embedding Multi-Instance Learning (MIL) pre-training paradigm. Trained on a million-scale dataset, this paradigm explicitly disentangles sparse foreground instances from dense backgrounds in the latent semantic space, overcoming the semantic ambiguity of conventional pixel-reconstruction methods. Extensive evaluations across nine diverse downstream tasks reveal that DynamicVis exhibits exceptional efficacy, particularly dominating in sparse-target and instance-level perception tasks (e.g., small object detection, and change detection).

</details>

---

### 44. [Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks](https://arxiv.org/abs/2504.12441)

**基本信息**

- 🔗 arXiv: [`2504.12441`](https://arxiv.org/abs/2504.12441)
- 👥 作者: Asutay Ozmen, João P. Hespanha, Katie Byl
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.12441.pdf)

**💡 相关性分析**

不相关。论文核心是机器人中的摩擦建模与物理信息神经网络，与化学信息学或质谱分析无关。

**📖 中文摘要**

论文标题为"Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks"。该研究提出了一个物理信息摩擦估计框架，将成熟的摩擦模型与可学习组件集成，仅需最小化、通用的测量数据。该方法强制执行物理一致性，同时保留捕捉复杂摩擦现象的灵活性。研究在一个欠驱动和非线性系统上进行了演示，表明仅在小规模噪声数据集上训练的学得摩擦模型，能够以比机器人模拟器中常用的简化模型高得多的保真度再现动态摩擦特性。关键的是，研究表明学得的模型可以迁移到未经训练的系统上。这种跨系统的泛化能力简化了复杂、欠驱动任务的摩擦建模。论文属于机器人学和控制系统领域，专注于物理模型的机器学习。其内容不涉及化学或质谱数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurately modeling friction in robotics remains a core challenge, as robotics simulators like MuJoCo and PyBullet use simplified friction models or heuristics to balance computational efficiency with accuracy, where these simplifications and approximations can lead to substantial differences between simulated and physical performance. In this paper, we present a physics-informed friction estimation framework that enables the integration of well-established friction models with learnable components, requiring only minimal, generic measurement data. Our approach enforces physical consistency yet retains the flexibility to capture complex friction phenomena. We demonstrate, on an underactuated and nonlinear system, that the learned friction models, trained solely on small and noisy datasets, accurately reproduce dynamic friction properties with significantly higher fidelity than the simplified models commonly used in robotics simulators. Crucially, we show that our approach enables the learned models to be transferable to systems they are not trained on. This ability to generalize across multiple systems streamlines friction modeling for complex, underactuated tasks, offering a scalable and interpretable path toward improving friction model accuracy in robotics and control.

</details>

---

### 45. [Faster multivariate integration in D-modules](https://arxiv.org/abs/2504.12724)

**基本信息**

- 🔗 arXiv: [`2504.12724`](https://arxiv.org/abs/2504.12724)
- 👥 作者: Hadrien Brochet, Frédéric Chyzak, Pierre Lairez
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.12724.pdf)

**💡 相关性分析**

不相关。论文是纯数学和符号计算研究，专注于微分模中的积分算法，与指定的应用领域无关。

**📖 中文摘要**

论文标题为"Faster multivariate integration in D-modules"。该研究提出了一种解决全纯积分背景下约化问题的新算法，进而为带参数积分提供了一种方法。该方法将Griffiths-Dwork约化技术扩展到全纯系统，并在Julia中实现。虽然目前在D-有限情况下尚未超越创造性伸缩求和方法，但它增强了全纯框架内的计算能力。作为一个应用，研究推导了一个先前无法获得的关于8-正则图生成级数的微分方程。论文属于数学领域，具体是符号计算和微分代数，涉及积分和微分方程。其内容与化学信息学或质谱分析没有直接联系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a new algorithm for solving the reduction problem in the context of holonomic integrals, which in turn provides an approach to integration with parameters. Our method extends the Griffiths--Dwork reduction technique to holonomic systems and is implemented in Julia. While not yet outperforming creative telescoping in D-finite cases, it enhances computational capabilities within the holonomic framework. As an application, we derive a previously unattainable differential equation for the generating series of 8-regular graphs.

</details>

---

### 46. [Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability](https://arxiv.org/abs/2505.03530)

**基本信息**

- 🔗 arXiv: [`2505.03530`](https://arxiv.org/abs/2505.03530)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03530.pdf)

**💡 相关性分析**

不相关。论文专注于生成模型（VAE）的通用机制可解释性方法，并未将其应用于化学或质谱数据，也未提供针对这些领域的特定资源或工具。

**📖 中文摘要**

论文标题为"Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability"。该研究为变分自编码器的机制可解释性引入了一个全面的因果干预框架。研究开发了技术来识别和分析VAE中的"电路基元"，检查语义因子如何通过网络层进行编码、处理和分离。该方法在不同级别使用针对性干预：输入操作、潜在空间扰动、激活修补和因果中介分析。该框架应用于具有已知因果关系的合成数据集和标准的解纠缠基准测试。结果表明，干预可以成功隔离功能电路，将计算图映射到语义因子的因果图，并区分多义和单义单元。此外，研究引入了因果效应强度、干预特异性和电路模块化的度量，以量化VAE组件的可解释性。实验结果表明了不同VAE变体之间的明显差异。该框架推进了对生成模型的机制理解，并为更透明和可控的VAE架构提供了工具。论文属于机器学习可解释性领域，虽然涉及生成模型（VAE），但其核心是模型内部的因果机制分析，而非针对化学或质谱数据的特定应用或模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic interpretability of deep learning models has emerged as a crucial research direction for understanding the functioning of neural networks. While significant progress has been made in interpreting discriminative models like transformers, understanding generative models such as Variational Autoencoders (VAEs) remains challenging. This paper introduces a comprehensive causal intervention framework for mechanistic interpretability of VAEs. We develop techniques to identify and analyze "circuit motifs" in VAEs, examining how semantic factors are encoded, processed, and disentangled through the network layers. Our approach uses targeted interventions at different levels: input manipulations, latent space perturbations, activation patching, and causal mediation analysis. We apply our framework to both synthetic datasets with known causal relationships and standard disentanglement benchmarks. Results show that our interventions can successfully isolate functional circuits, map computational graphs to causal graphs of semantic factors, and distinguish between polysemantic and monosemantic units. Furthermore, we introduce metrics for causal effect strength, intervention specificity, and circuit modularity that quantify the interpretability of VAE components. Experimental results demonstrate clear differences between VAE variants, with FactorVAE achieving higher disentanglement scores (0.084) and effect strengths (mean 4.59) compared to standard VAE (0.064, 3.99) and Beta-VAE (0.051, 3.43). Our framework advances the mechanistic understanding of generative models and provides tools for more transparent and controllable VAE architectures.

</details>

---

### 47. [MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models](https://arxiv.org/abs/2505.10294)

**基本信息**

- 🔗 arXiv: [`2505.10294`](https://arxiv.org/abs/2505.10294)
- 👥 作者: Guillaume Balezo, Roger Trullo, Albert Pla Planas 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10294.pdf)

**💡 相关性分析**

不相关。论文研究的是医学图像（组织病理学）的跨模态预测，与化学分子、质谱数据或相关的大模型无关。

**📖 中文摘要**

论文标题为"MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models"。该研究引入了MIPHEI，一种受U-Net启发的架构，利用ViT病理学基础模型作为编码器，从H&E图像预测多重免疫荧光信号。MIPHEI针对一个全面的标记物面板，涵盖核内容、免疫谱系、上皮、间质、血管系统和增殖。模型使用公开的OrionCRC数据集（结直肠癌组织的重染色H&E和mIF图像）进行训练，并在五个独立数据集上进行了验证。结果表明，对于某些分子标记物，该模型能够捕捉H&E图像中可见的核形态与其组织背景之间，以及定义特定细胞类型的分子标记物之间的复杂关系。MIPHEI为大规模H&E数据集的细胞类型感知分析提供了有希望的一步。论文属于计算病理学和医学图像分析领域，核心是利用基础模型进行跨模态（H&E到mIF）预测。其内容与化学信息学或质谱分析无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathological analysis is a cornerstone of cancer diagnosis, with Hematoxylin and Eosin (H&E) staining routinely acquired for every patient to visualize cell morphology and tissue architecture. On the other hand, multiplex immunofluorescence (mIF) enables more precise cell type identification via proteomic markers, but has yet to achieve widespread clinical adoption due to cost and logistical constraints. To bridge this gap, we introduce MIPHEI (Multiplex Immunofluorescence Prediction from H&E Images), a U-Net-inspired architecture that leverages a ViT pathology foundation model as encoder to predict mIF signals from H&E images using rich pretrained representations. MIPHEI targets a comprehensive panel of markers spanning nuclear content, immune lineages (T cells, B cells, myeloid), epithelium, stroma, vasculature, and proliferation. We train our model using the publicly available OrionCRC dataset of restained H&E and mIF images from colorectal cancer tissue, and validate it on five independent datasets: HEMIT, PathoCell, IMMUcan, Lizard and PanNuke. On OrionCRC test set, MIPHEI achieves accurate cell-type classification from H&E alone, with F1 scores of 0.93 for Pan-CK, 0.83 for alpha-SMA, 0.68 for CD3e, 0.36 for CD20, and 0.28 for CD68, substantially outperforming both a state-of-the-art baseline and a random classifier for most markers. Our results indicate that, for some molecular markers, our model captures the complex relationships between nuclear morphologies in their tissue context, as visible in H&E images and molecular markers defining specific cell types. MIPHEI offers a promising step toward enabling cell-type-aware analysis of large-scale H&E datasets, in view of uncovering relationships between spatial cellular organization and patient outcomes.

</details>

---

### 48. [RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval](https://arxiv.org/abs/2506.08625)

**基本信息**

- 🔗 arXiv: [`2506.08625`](https://arxiv.org/abs/2506.08625)
- 👥 作者: Minhae Oh, Jeonghye Kim, Nakyung Lee 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08625.pdf)

**💡 相关性分析**

不相关。论文提出的是一个通用的、用于增强LLM科学推理能力的检索增强框架，并非专门为化学或质谱设计，也未提供针对这些领域的特定数据集、资源或工具。

**📖 中文摘要**

论文标题为"RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval"。该研究针对科学推理需要长链推理过程、领域特定术语知识以及适应最新发现的挑战，引入了RAISE，一个逐步检索增强的框架，用于从开放语料库中检索逻辑相关的文档。RAISE分为三个步骤：问题分解、逻辑查询生成和逻辑检索。研究表明，RAISE在科学推理基准测试中 consistently 优于其他基线方法。分析发现，与其他基线不同，RAISE检索的文档不仅在领域知识上相似，而且在逻辑上更相关。论文属于自然语言处理和大型语言模型领域，专注于通过检索增强来提升LLM的科学推理能力。虽然"科学推理"是一个宽泛的术语，可能涵盖化学，但论文并未专门针对化学信息学或质谱分析。其提出的框架是通用的，可用于任何科学领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific reasoning requires not only long-chain reasoning processes, but also knowledge of domain-specific terminologies and adaptation to updated findings. To deal with these challenges for scientific reasoning, we introduce RAISE, a step-by-step retrieval-augmented framework which retrieves logically relevant documents from in-the-wild corpus. RAISE is divided into three steps: problem decomposition, logical query generation, and logical retrieval. We observe that RAISE consistently outperforms other baselines on scientific reasoning benchmarks. We analyze that unlike other baselines, RAISE retrieves documents that are not only similar in terms of the domain knowledge, but also documents logically more relevant.

</details>

---

### 49. [PGLib-CO2: A Power Grid Library for Real-Time Computation and Optimization of Carbon Emissions](https://arxiv.org/abs/2506.14662)

**基本信息**

- 🔗 arXiv: [`2506.14662`](https://arxiv.org/abs/2506.14662)
- 👥 作者: Young-ho Cho, Min-Seung Ko, Hao Zhu
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.14662.pdf)

**💡 相关性分析**

不相关。论文核心是电力系统碳排放的建模、计算和优化，提供了一个相关的数据集和计算工具，但领域是能源工程，而非化学或质谱。

**📖 中文摘要**

论文标题为"PGLib-CO2: A Power Grid Library for Real-Time Computation and Optimization of Carbon Emissions"。该工作引入了PGLib-CO2，一个开源扩展，用于丰富标准的电网测试用例，添加CO2和CO2当量排放强度因子，以实现真实的、发电机级别的碳分析，并扩展了燃料类型列表。使用标准化数据，PGLib-CO2允许增强计算关键碳排放指标的算法。研究首先利用可微分编程范式，通过将基于最优潮流的电网调度视为一个可微分层来计算LMCE。该方法为一般凸成本函数提供了严格的边际敏感性，消除了使用微小增量变化进行数值扰动的需要。此外，为了加速实时LMCE计算，研究开发了一种基于MPP的方法，将优化负担转移到识别最优潮流临界区域的离线阶段。由于每个临界区域都由一个预先计算好的仿射调度函数表征，在线阶段简化为识别区域，然后高效评估区域特定的LMCE值。数值评估表明，可微分LMCE计算获得了精确的敏感性信息，而基于MPP的方法比直接优化方法更快地检索LMCE信号。通过将高保真数据与先进的参数计算相结合，PGLib-CO2为未来可持续电力系统运营研究提供了一个可重复且计算高效的基础。论文属于电力系统工程和可持续能源领域，专注于电网碳排放建模与优化。其内容与化学信息学或质谱分析无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Achieving a sustainable electricity infrastructure requires the explicit integration of carbon emissions into power system modeling and optimization. However, existing open-source test cases for power system research lack generator-level carbon profiling, preventing the benchmark of carbon-aware operational strategies. To address this gap, this work introduces PGLib-CO2, an open-source extension to the PGLib-OPF test case library. The proposed PGLib-CO2 enriches standard grid test cases with CO2 and CO2-equivalent emission intensity factors to achieve realistic, generator-level carbon profiling with an expanded list of fuel types. Using the standardized data, PGLib-CO2 allows us to enhance the algorithms for computing key carbon emission metrics. We first utilize the differentiable programming paradigm for computing LMCE by treating the OPF-based grid dispatch as a differentiable layer. This method provides a rigorous marginal sensitivity for general convex cost functions, eliminating the need of using a small incremental change in numerical perturbation. Moreover, to accelerate the real-time LMCE computation, we develop an MPP-based approach that shifts the optimization burden to offline phase of identifying the OPF critical regions. Since each critical region is characterized by a pre-computed affine dispatch function, the online phase reduces to identifying the region followed by efficiently evaluating the region-specific LMCE values. Numerical evaluations on IEEE test systems demonstrate that the differentiable LMCE computation attains the precise sensitivity information, and the MPP-based approach retrieves the LMCE signals faster than the direct optimization approach. By bridging high-fidelity data with advanced parametric computation, PGLib-CO2 provides a reproducible and computationally efficient foundation for future research in sustainable power system operations.

</details>

---

### 50. [A Crowdsensing Intrusion Detection Dataset For Decentralized Federated Learning Models](https://arxiv.org/abs/2507.13313)

**基本信息**

- 🔗 arXiv: [`2507.13313`](https://arxiv.org/abs/2507.13313)
- 👥 作者: Chao Feng, Alberto Huertas Celdran, Jing Han 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.13313.pdf)

**💡 相关性分析**

不相关。论文提供了一个用于网络安全（恶意软件检测）和联邦学习研究的数据集，与化学或质谱领域无关。

**📖 中文摘要**

论文标题为"A Crowdsensing Intrusion Detection Dataset For Decentralized Federated Learning Models"。该论文介绍了一个数据集和一项关于去中心化联邦学习用于物联网群智感知恶意软件检测的实验研究。该数据集包含来自良性程序和八种恶意软件攻击的行为记录。总共收集了21,582,484条原始记录，涵盖系统调用、文件系统活动、资源使用、内核事件、输入/输出事件和网络记录。这些记录被聚合成30秒的窗口，产生了342,106条用于模型训练和评估的数据记录。在DFL平台上的实验比较了传统机器学习、集中式联邦学习和去中心化联邦学习在不同节点数量、拓扑结构和数据分布下的性能。结果表明，DFL在保持数据本地性的同时保持了有竞争力的性能，在大多数设置下优于CFL。该数据集为研究物联网群智感知环境的安全性提供了坚实的基础。论文属于网络安全和物联网领域，专注于入侵检测和联邦学习。其内容与化学信息学或质谱分析无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper introduces a dataset and an experimental study on Decentralized Federated Learning (DFL) for Internet of Things (IoT) crowdsensing malware detection. The dataset comprises behavioral records from benign and eight malware attacks. A total of 21,582,484 original records were collected from system calls, file system activities, resource usage, kernel events, input/output events, and network records. These records were aggregated into 30-second windows, resulting in 342,106 data records used for model training and evaluation. Experiments on the DFL platform compare traditional Machine Learning (ML), Centralized Federated Learning (CFL), and DFL across different node counts, topologies, and data distributions. Results show that DFL maintains competitive performance while preserving data locality, outperforming CFL in most settings. This dataset provides a solid foundation for studying the security of IoT crowdsensing environments.

</details>

---

### 51. [GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM](https://arxiv.org/abs/2507.13323)

**基本信息**

- 🔗 arXiv: [`2507.13323`](https://arxiv.org/abs/2507.13323)
- 👥 作者: Kyeongjin Ahn, Sungwon Han, Seungeon Lee 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.13323.pdf)

**💡 相关性分析**

不相关。论文研究的是利用LLM和多模态数据（卫星图像、文本）进行社会经济指标估计，领域是社会科学和地理空间分析，与化学或质谱无关。

**📖 中文摘要**

论文标题为"GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM"。该研究引入了GeoReg，一个回归模型，整合了包括卫星图像和基于网络的地理空间信息在内的多样化数据源，以估计社会经济指标，即使是对于数据稀缺的地区（如发展中国家）也是如此。该方法利用大型语言模型的先验知识来解决标记数据稀缺的问题，语言模型作为数据工程师，通过提取信息丰富的特征，使得在少样本设置下能够进行有效的估计。具体来说，模型获取数据特征与目标指标之间的上下文关系，将其相关性分类为正相关、负相关、混合相关或不相关。然后，这些特征被输入到线性估计器中，每个类别都有定制的权重约束。为了捕捉非线性模式，模型还识别有意义的特征交互，并将其与非线性变换一起整合。在三个处于不同发展阶段的国家进行的实验表明，该模型在估计社会经济指标方面优于基线方法，即使对于数据可用性有限的低收入国家也是如此。论文属于计算社会科学和地理空间人工智能领域，专注于利用多模态数据和LLM进行社会经济指标估计。其内容与化学信息学或质谱分析无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Socio-economic indicators like regional GDP, population, and education levels, are crucial to shaping policy decisions and fostering sustainable development. This research introduces GeoReg a regression model that integrates diverse data sources, including satellite imagery and web-based geospatial information, to estimate these indicators even for data-scarce regions such as developing countries. Our approach leverages the prior knowledge of large language model to address the scarcity of labeled data, with the language model functioning as a data engineer by extracting informative features to enable effective estimation in few-shot settings. Specifically, our model obtains contextual relationships between data features and the target indicator, categorizing their correlations as positive, negative, mixed, or irrelevant. These features are then fed into the linear estimator with tailored weight constraints for each category. To capture nonlinear patterns, the model also identifies meaningful feature interactions and integrates them, along with nonlinear transformations. Experiments across three countries at different stages of development demonstrate that our model outperforms baselines in estimating socio-economic indicators, even for low-income countries with limited data availability.

</details>

---

### 52. [Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions](https://arxiv.org/abs/2508.17303)

**基本信息**

- 🔗 arXiv: [`2508.17303`](https://arxiv.org/abs/2508.17303)
- 👥 作者: Dhiraj S Kori, Abhinav Chandraker, Syed Abdur Rahman 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.17303.pdf)

**💡 相关性分析**

不相关。论文应用物理信息神经网络解决核材料疲劳寿命预测问题，属于材料科学与核工程交叉领域，与化学信息学或质谱分析的主题无关。

**📖 中文摘要**

论文标题为"Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions"。该研究提出了一个物理信息神经网络框架，用于预测核反应堆中使用的辐照奥氏体和铁素体/马氏体钢的低周疲劳寿命。这些材料经历循环载荷、中子辐照和高温，导致复杂的退化机制，难以用传统的经验或纯数据驱动模型捕捉。所提出的PINN将疲劳寿命控制的物理约束嵌入到损失函数中，从而实现物理一致的学习，同时提高预测准确性、可靠性和泛化能力。该模型在495个涵盖辐照和未辐照条件的应变控制疲劳数据点上进行了训练。与包括随机森林、梯度提升、极限梯度提升和传统神经网络在内的传统机器学习方法相比，PINN表现出优越的性能。SHAP分析确定了应变幅、辐照剂量和测试温度为主导特征，每个特征与疲劳寿命都呈现出物理上有意义的负相关。单变量和多变量分析揭示了清晰的合金特异性退化特征。数值研究表明，所提出的PINN框架是反应堆相关疲劳评估的可靠且可解释的工具。论文属于材料科学和核工程领域，专注于利用物理信息神经网络预测材料在极端环境下的疲劳寿命。其内容与化学信息学或质谱分析无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study proposes a Physics-Informed Neural Network (PINN) framework to predict the low-cycle fatigue (LCF) life of irradiated austenitic and ferritic/martensitic (F/M) steels used in nuclear reactors. These materials undergo cyclic loading, neutron irradiation, and elevated temperatures, leading to complex degradation mechanisms that are difficult to capture with conventional empirical or purely data-driven models. The proposed PINN embeds fatigue-life governing physical constraints into the loss function, enabling physically consistent learning while improving predictive accuracy, reliability, and generalizability. The model was trained on 495 strain-controlled fatigue data points spanning irradiated and unirradiated conditions. Compared with traditional machine learning approaches, including Random Forest, Gradient Boosting, eXtreme Gradient Boosting, and conventional neural networks, the PINN demonstrated superior performance. SHapley Additive exPlanations (SHAP) analysis identified strain amplitude, irradiation dose, and test temperature as the dominant features, each exhibiting physically meaningful inverse correlations with fatigue life. Univariate and multivariate analyses revealed clear alloy-specific degradation characteristics. Austenitic steels exhibited strong nonlinear coupling among strain amplitude, irradiation dose, and temperature, resulting in pronounced fatigue degradation under combined loading. In contrast, F/M steels demonstrated comparatively stable irradiation responses, including dose-saturation behavior, but showed sensitivity to elevated temperatures beyond tempering thresholds. Overall, the proposed PINN framework serves as a reliable and interpretable tool for reactor-relevant fatigue assessment, enabling performance evaluation for advanced nuclear applications.

</details>

---

### 53. [Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning](https://arxiv.org/abs/2509.08759)

**基本信息**

- 🔗 arXiv: [`2509.08759`](https://arxiv.org/abs/2509.08759)
- 👥 作者: Mominul Rubel, Adam Meyers, Gabriel Nicolosi
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.08759.pdf)

**💡 相关性分析**

不相关。论文提出了一种通用的、基于傅里叶表示的神经网络架构，用于科学机器学习，但其应用示例（PDEs, OCPs）和核心贡献与化学信息学或质谱分析无特定关联。

**📖 中文摘要**

论文标题为"Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning"。该研究引入了傅里叶学习机，一种神经网络架构，旨在表示多维非调和傅里叶级数。FLM使用具有余弦激活函数的简单前馈结构，将级数的频率、振幅和相移作为可训练参数进行学习。这种设计允许模型创建适应周期和非周期函数的问题特定谱基。与先前受傅里叶启发的NN模型不同，FLM是第一个能够以可分离形式表示具有完整基函数集的多维傅里叶级数的架构，这是通过使用标准的类似多层感知器的架构实现的。研究证明了傅里叶系数与振幅和相移之间的一一对应关系，允许在完整的、可分离的基形式与余弦相移形式之间进行转换。此外，研究评估了FLM在几个科学计算问题上的性能，包括基准偏微分方程和一系列最优控制问题。计算实验表明，FLM的性能与SIREN和普通前馈NN等成熟架构相当，且通常更优。论文属于科学机器学习和神经网络架构设计领域，提出了一种新型的、基于傅里叶表示的通用神经网络。虽然具有通用性，可用于各种科学计算问题，但论文并未专门针对化学或质谱数据进行应用或优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Fourier Learning Machine (FLM), a neural network (NN) architecture designed to represent a multidimensional nonharmonic Fourier series. The FLM uses a simple feedforward structure with cosine activation functions to learn the frequencies, amplitudes, and phase shifts of the series as trainable parameters. This design allows the model to create a problem-specific spectral basis adaptable to both periodic and nonperiodic functions. Unlike previous Fourier-inspired NN models, the FLM is the first architecture able to represent a multidimensional Fourier series with a complete set of basis functions in separable form, doing so by using a standard Multilayer Perceptron-like architecture. A one-to-one correspondence between the Fourier coefficients and amplitudes and phase-shifts is demonstrated, allowing for the translation between a full, separable basis form and the cosine phase-shifted one. Additionally, we evaluate the performance of FLMs on several scientific computing problems, including benchmark Partial Differential Equations (PDEs) and a family of Optimal Control Problems (OCPs). Computational experiments show that the performance of FLMs is comparable, and often superior, to that of established architectures like SIREN and vanilla feedforward NNs.

</details>

---

### 54. [EDMD-Based Robust Observer Synthesis for Nonlinear Systems](https://arxiv.org/abs/2509.09812)

**基本信息**

- 🔗 arXiv: [`2509.09812`](https://arxiv.org/abs/2509.09812)
- 👥 作者: Xiuzhen Ye, Wentao Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.09812.pdf)

**💡 相关性分析**

不相关。论文研究的是通用非线性系统的数据驱动鲁棒状态观测器设计，属于控制理论领域，与化学或质谱无关。

**📖 中文摘要**

论文标题为"EDMD-Based Robust Observer Synthesis for Nonlinear Systems"。该研究提出了一种数据驱动的方法，用于设计连续时间非线性系统的状态观测器，其中使用扩展动态模式分解程序来识别一个近似的线性提升模型。由于在由字典函数张成的有限维空间上的这种模型存在不可避免的失配，研究首先基于线性-径向核的再生核希尔伯特空间理论，建立了近似线性模型中非线性误差的大小由提升状态扇形界定的结论。该扇形界包括由于有限字典引起的确定性部分和由于随机数据样本引起的随机部分，观测器设计需要在鲁棒公式中同时考虑这两种误差。因此，观测器综合是使用线性矩阵不等式执行的，由观测误差的期望指数衰减率（当系统渐近稳定时）或从建模误差到观测误差的L2增益指定。数值研究证明了所提出方法的有效性和灵活性。因此，这项工作在Koopman算子理论框架中，明确地初步使用了线性系统理论进行非线性状态观测。论文属于控制系统和非线性观测器设计领域，专注于利用EDMD和Koopman算子理论进行数据驱动的鲁棒观测器设计。其内容与化学信息学或质谱分析无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents a data-driven approach for designing state observers for continuous-time nonlinear systems, where an extended dynamic mode decomposition (EDMD) procedure is used to identify an approximate linear lifted model. Since such a model on a finite-dimensional space spanned by the dictionary functions has an inevitable mismatch, we first establish, based on our theory of reproducing kernel Hilbert space with a linear-radial kernel, that the nonlinear error magnitude in the approximate linear model is sectorially bounded by the lifted state. The sector bound comprises a deterministic part due to the finite dictionary and a stochastic part due to the random data samples, and the observer design needs to account for both of these errors in a robust formulation. Hence, the observer synthesis is performed using linear matrix inequalities (LMIs), specified by the desired exponential decay rate of the observation error (when the system is asymptotically stable) or the L2-gain from the modeling error to the observation error. Numerical studies demonstrate the effectiveness and flexibility of the proposed method. As such, this work entails an explicit elementary use of linear systems theory for nonlinear state observation in a Koopman operator-theoretic framework.

</details>

---

### 55. [Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity](https://arxiv.org/abs/2601.18032)

**基本信息**

- 🔗 arXiv: [`2601.18032`](https://arxiv.org/abs/2601.18032)
- 👥 作者: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18032.pdf)

**💡 相关性分析**

满足标准2：论文构建了一个用于化学信息学/材料发现的专用数据集，并提出了一个利用预训练聚合物表示（化学大模型）的多模态学习框架，为相关主题提供了数据资源和工具方法。

**📖 中文摘要**

本文聚焦于软高介电常数弹性体的开发，这是一个化学信息学与材料发现交叉领域的关键问题。论文的核心贡献在于构建了一个高质量的丙烯酸酯基介电弹性体数据集，系统整合了分子序列、介电和机械性能。更重要的是，它提出了一个多模态学习框架，该框架利用大规模预训练的聚合物表示（即化学大模型）来迁移化学和结构知识。通过使用这些预训练嵌入，该框架能够在数据稀缺的情况下，准确预测弹性体的介电和机械性能，从而加速数据高效的材料发现。这项工作直接提供了用于化学大模型应用的数据集和工具，并展示了如何利用预训练模型解决化学信息学中的具体问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggregating experimental results from the past decade. Building on this dataset, we propose a multimodal learning framework leveraging large-scale pretrained polymer representations. These pretrained embeddings transfer chemical and structural knowledge from vast polymer corpora, enabling accurate few-shot prediction of dielectric and mechanical properties and accelerating data-efficient discovery of soft high-$k$ dielectric elastomers. Our data and implementation are publicly available at: this https URL

</details>

---

### 56. [Sheaf Neural Networks and biomedical applications](https://arxiv.org/abs/2602.00159)

**基本信息**

- 🔗 arXiv: [`2602.00159`](https://arxiv.org/abs/2602.00159)
- 👥 作者: Aneeqa Mehrab, Jan Willem Van Looy, Pietro Demurtas 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00159.pdf)

**💡 相关性分析**

满足标准2：论文提出的层神经网络（SNN）作为一种新的图表示学习模型，可用于处理分子结构等图数据，为化学信息学中的结构推理任务提供了潜在的工具和方法。

**📖 中文摘要**

本文介绍了层神经网络（SNN）的理论和数学模型，并将其应用于生物医学问题。虽然论文主题是图神经网络的一种变体，但其核心应用场景是生物医学领域，例如可能涉及生物分子结构分析。论文声称SNN在具体案例研究中能够有效回答生物医学问题，并且性能优于流行的图神经网络（如GCN、GAT、GraphSage）。考虑到质谱结构推理等任务常涉及分子图或生物网络的分析，SNN作为一种新的图表示学习方法，其理论和模型可能为处理此类结构化化学/生物数据提供新的工具和视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The purpose of this paper is to elucidate the theory and mathematical modelling behind the sheaf neural network (SNN) algorithm and then show how SNN can effectively answer to biomedical questions in a concrete case study and outperform the most popular graph neural networks (GNNs) as graph convolutional networks (GCNs), graph attention networks (GAT) and GraphSage.

</details>

---

### 57. [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](https://arxiv.org/abs/2603.03686)

**基本信息**

- 🔗 arXiv: [`2603.03686`](https://arxiv.org/abs/2603.03686)
- 👥 作者: Jiangyu Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03686.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是自动化化学配方设计，这是一个典型的化学信息学与AI交叉领域的问题。其提出的神经符号框架（AI4S-SDS）直接围绕利用AI模型（如LLM智能体）和优化算法进行化学发现这一主题。

**📖 中文摘要**

本文提出了AI4S-SDS，一个用于自动化化学配方设计的神经符号框架。该框架集成了多智能体协作和定制的蒙特卡洛树搜索（MCTS）引擎，旨在解决化学配方设计这一高维组合空间导航问题。论文明确针对“化学配方自动化设计”这一化学信息学核心任务，并引入了创新的搜索和优化机制。特别是，它通过可微物理引擎将符号推理与物理可行性（如热力学约束）联系起来，用于优化连续的混合比例。这项工作代表了利用AI（特别是结合搜索与学习的智能体框架）进行科学发现（包括化学发现）的前沿方向，与“化学大模型”所追求的自动化、智能化化学研究目标高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.

</details>

---

### 58. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容是使用AI模型（CliqueFlowmer）进行材料发现与优化，属于化学信息学范畴。同时，它提出了一种新的模型和优化框架，为相关领域提供了工具和方法。

**📖 中文摘要**

本文提出了CliqueFlowmer，一种基于离线模型优化（MBO）的计算材料发现（CMD）技术。论文批评了流行的生成建模方法在材料空间探索上的局限性，并提出了一种将目标材料属性的直接优化融合到生成过程中的新方法。CliqueFlowmer结合了基于团的MBO最新进展与Transformer和流生成模型。论文验证了该模型在材料优化方面的能力，并表明其生成的材料性能显著优于生成式基线。这项工作直接针对“材料发现”这一化学信息学的核心应用，提出了一种新的、与生成模型不同的AI驱动优化范式，为化学大模型在逆向设计和属性优化方面的应用提供了新的思路和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 59. [Deep Expert Injection for Anchoring Retinal VLMs with Domain-Specific Knowledge](https://arxiv.org/abs/2603.07131)

**基本信息**

- 🔗 arXiv: [`2603.07131`](https://arxiv.org/abs/2603.07131)
- 👥 作者: Shuai Lu, Meng Wang, Jia Guo 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07131.pdf)

**💡 相关性分析**

满足标准3：论文虽然应用在医学领域，但其核心方法论（深度专家注入、双流编码、知识锚定）是针对解决大模型缺乏领域知识、产生幻觉这一普遍问题的创新性讨论。这种将领域知识系统整合进大模型的技术路线，对“化学大模型”和“质谱结构推理”模型的构建具有重要的前瞻性和指导意义，属于重要的相关讨论。

**📖 中文摘要**

本文针对大型视觉语言模型（LVLM）在眼科自动诊断中缺乏领域知识的问题，提出了EyExIn框架。该框架通过“深度专家注入”机制，将专家知识锚定到视网膜VLM中。其核心创新包括专家感知的双流编码策略（将视觉表示解耦为通用解剖上下文和专用病理语义流）、语义自适应门控融合模块以及自适应深度专家注入机制。这些设计旨在弥补感知差距和推理差距，确保模型推理严格基于视觉证据，减少幻觉。虽然应用领域是医学影像，但其方法论——即如何将领域专家知识系统性地注入并约束大规模预训练模型的行为——对于“化学大模型”或“质谱结构推理”模型具有重要的借鉴意义。例如，在质谱解析中，注入光谱学规则或化学知识约束模型推理，是提升模型可靠性和领域适应性的关键思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Vision Language Models (LVLMs) show immense potential for automated ophthalmic diagnosis. However, their clinical deployment is severely hindered by lacking domain-specific knowledge. In this work, we identify two structural deficiencies hindering reliable medical reasoning: 1) the Perception Gap, where general-purpose visual encoders fail to resolve fine-grained pathological cues (e.g., microaneurysms); and 2) the Reasoning Gap, where sparse visual evidence is progressively overridden by massive language priors in deeper transformer layers, leading to ungrounded hallucinations. To bridge these gaps, we propose EyExIn, a data-efficient framework designed to anchor retinal VLMs with expert knowledge via a Deep Expert Injection mechanism. Our architecture employs an Expert-Aware Dual-Stream encoding strategy that decouples visual representation into a general stream for anatomical context and a specialized expert stream for pathological semantics. To ensure high-fidelity integration, we design a Semantic-Adaptive Gated Fusion module, which dynamically amplifies subtle lesion signals while filtering irrelevant background noise. Furthermore, we introduce Adaptive Deep Expert Injection to embed persistent "Vision Anchors" by integrating fused visual features as residual biases directly into intermediate LLM layers. This mechanism creates a visual shortcut that forces the reasoning stack to remain strictly grounded in visual evidence. Extensive experiments across four benchmarks demonstrate that our model consistently outperforms massive proprietary systems. EyExIn significantly enhances domain-specific knowledge embedding and achieves state-of-the-art precision in ophthalmic visual question answering, advancing the development of trustworthy ophthalmic AI.

</details>

---

### 60. [Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining](https://arxiv.org/abs/2603.11103)

**基本信息**

- 🔗 arXiv: [`2603.11103`](https://arxiv.org/abs/2603.11103)
- 👥 作者: Zhiyuan Zeng, Yichi Zhang, Yong Shan 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11103.pdf)

**💡 相关性分析**

满足标准3：论文的核心是探讨如何通过合成“推理轨迹”数据来提升大模型的复杂推理能力。这一前瞻性的训练范式讨论，对于旨在解决“质谱结构推理”这种需要多步、因果推理的化学大模型的构建和训练，提供了重要的方法论参考和方向性启示。

**📖 中文摘要**

本文针对大语言模型在复杂软件工程中深度、长视野推理的不足，提出了一种新的预训练范式：“通过重建来理解”。论文认为，标准的预训练数据（静态代码仓库）只代表了复杂智力过程的最终状态，而抽象掉了中间的规划、调试和迭代细化步骤。为了弥补这一差距，论文引入了一个框架，通过多智能体模拟来合成这些潜在的智能体轨迹（即规划、推理和调试步骤）。这些轨迹以源代码仓库的结构现实（如依赖图和文件层次结构）为基础，并通过基于搜索的优化技术进行迭代细化，以最大化真实代码的可能性。实验表明，在这些重建的轨迹上进行持续预训练，能显著增强LLaMA-3-8B在多种任务上的性能。这项研究从“如何让大模型学习更深层次的推理过程”这一根本问题出发，其思想对于训练用于“质谱结构推理”或“化学合成规划”等需要复杂、多步推理的化学大模型具有直接的启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have achieved remarkable success in code generation, they often struggle with the deep, long-horizon reasoning required for complex software engineering. We attribute this limitation to the nature of standard pre-training data: static software repositories represent only the terminal state of an intricate intellectual process, abstracting away the intermediate planning, debugging, and iterative refinement. To bridge this gap, we propose a novel paradigm: understanding via reconstruction. We hypothesize that reverse-engineering the latent agentic trajectories -- the planning, reasoning, and debugging steps -- behind static repositories provides a far richer supervision signal than raw code alone. To operationalize this, we introduce a framework that synthesizes these trajectories using a multi-agent simulation. This process is grounded in the structural realities of the source repositories (e.g., dependency graphs and file hierarchies) to ensure fidelity. Furthermore, to guarantee the logical rigor of the synthetic data, we employ a search-based optimization technique that iteratively refines the Chain-of-Thought (CoT) reasoning to maximize the likelihood of the ground-truth code. Empirical results demonstrate that continuous pre-training on these reconstructed trajectories significantly enhances Llama-3-8B's performance across diverse benchmarks, including long-context understanding, coding proficiency, and agentic capabilities.

</details>

---

### 61. [Reversible Lifelong Model Editing via Semantic Routing-Based LoRA](https://arxiv.org/abs/2603.11239)

**基本信息**

- 🔗 arXiv: [`2603.11239`](https://arxiv.org/abs/2603.11239)
- 👥 作者: Haihua Luo, Xuming Ran, Tommi Kärkkäinen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11239.pdf)

**💡 相关性分析**

满足标准3：论文提出的可逆、终身模型编辑框架（SoLA），是针对大模型知识更新与修正这一核心挑战的前沿研究。该技术讨论对于构建能够持续学习新化学知识、修正推理错误的“化学大模型”或“质谱解析模型”具有重要的相关性和指导价值。

**📖 中文摘要**

本文提出了SoLA，一个基于语义路由的LoRA框架，用于大语言模型的终身模型编辑。SoLA将每次编辑封装为一个独立的LoRA模块，并通过语义路由动态激活相关模块，避免了持续更新导致的语义漂移和灾难性遗忘。更重要的是，SoLA支持通过从语义路由中移除键来精确撤销特定编辑，从而恢复模型的原始行为。论文声称这种可逆的回滚编辑能力在现有文献中是首次实现。模型编辑是使大模型（包括化学大模型）能够持续学习新知识、修正错误而不损害原有能力的关键技术。SoLA提出的可逆、模块化编辑框架，为化学大模型在吸收新实验数据、修正错误谱图解析规则等方面的安全、可控更新提供了潜在的技术解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The dynamic evolution of real-world necessitates model editing within Large Language Models. While existing methods explore modular isolation or parameter-efficient strategies, they still suffer from semantic drift or knowledge forgetting due to continual updating. To address these challenges, we propose SoLA, a Semantic routing-based LoRA framework for lifelong model editing. In SoLA, each edit is encapsulated as an independent LoRA module, which is frozen after training and mapped to input by semantic routing, allowing dynamic activation of LoRA modules via semantic matching. This mechanism avoids semantic drift caused by cluster updating and mitigates catastrophic forgetting from parameter sharing. More importantly, SoLA supports precise revocation of specific edits by removing key from semantic routing, which restores model's original behavior. To our knowledge, this reversible rollback editing capability is the first to be achieved in existing literature. Furthermore, SoLA integrates decision-making process into edited layer, eliminating the need for auxiliary routing networks and enabling end-to-end decision-making process. Extensive experiments demonstrate that SoLA effectively learns and retains edited knowledge, achieving accurate, efficient, and reversible lifelong model editing.

</details>

---

### 62. [To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation](https://arxiv.org/abs/2603.15159)

**基本信息**

- 🔗 arXiv: [`2603.15159`](https://arxiv.org/abs/2603.15159)
- 👥 作者: Yitong Zhang, Chengze Li, Ruize Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15159.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了教导LLMs使用私有API的方法论（PriCoder）和自动合成训练数据的技术，这为构建能够调用化学领域专用工具和数据库的“化学大模型”提供了重要的工具和训练思路。同时，该研究也包含了对如何让大模型适应领域特定工具这一重要问题的深入讨论。

**📖 中文摘要**

本文针对大语言模型在私有库导向的代码生成任务上的局限性，提出了PriCoder方法。该方法通过自动合成数据来教导LLMs调用私有库API。PriCoder将私有库数据合成建模为图构建问题，并交替使用两个图算子：渐进式图演化（提高数据多样性）和多维图剪枝（提高数据质量）。论文构建了两个基于新发布库的基准进行严格评估。实验表明，PriCoder能显著提升模型在私有库代码生成上的能力，同时对通用代码生成能力影响甚微。这项研究直接解决了AI模型（特别是代码生成模型）如何有效利用特定领域、非公开API（可类比为化学领域的专用软件包或数据库）的关键问题。其数据合成和模型训练方法，对于训练能够熟练调用化学信息学专用工具包（如RDKit）、数据库或模拟软件的“化学大模型”具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability. Our code and benchmarks are publicly available at this https URL .

</details>

---

### 63. [Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences](https://arxiv.org/abs/2603.16313)

**基本信息**

- 🔗 arXiv: [`2603.16313`](https://arxiv.org/abs/2603.16313)
- 👥 作者: Hugo Math
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16313.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用大语言模型（LLM）和Transformer架构对高维事件序列进行建模、预测和推理。这直接关联到“化学大模型”主题，因为其方法论（将序列数据视为语言并用LLM处理）可迁移至化学序列（如SMILES、质谱峰）的分析和结构推理。

**📖 中文摘要**

本文提出了一种用于高维事件序列（如车辆诊断故障码）的统一框架，将事件序列建模、因果发现和大语言模型（LLM）相结合。论文的核心是将诊断序列视为一种可以建模、预测和解释的语言。虽然论文主要关注工业故障诊断，但其核心方法论——将高维事件序列视为语言，并使用Transformer架构和LLM进行建模、预测和规则合成——与“化学大模型”的主题高度相关。该框架展示了如何利用大语言模型技术处理复杂的、高维度的序列数据，并从中推理出结构化的知识（如布尔规则），这种方法论可以类比并应用于化学信息学领域，例如将质谱或分子序列视为“语言”，并利用大模型进行结构推理和知识发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>

---

### 64. [Cell-cell Communication Inference and Analysis: Biological Mechanisms, Computational Approaches, and Future Opportunities](https://arxiv.org/abs/2512.03497)

**基本信息**

- 🔗 arXiv: [`2512.03497`](https://arxiv.org/abs/2512.03497)
- 👥 作者: Xiangzheng Cheng, Haili Huang, Ye Su 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03497.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对从单细胞和空间转录组数据推断细胞间通信（CCC）这一领域的综述。它系统性地回顾和比较了大量（超过140种）相关的计算模型、工具和资源，并讨论了未来的研究方向。虽然主题偏向生物信息学，但其核心是计算模型在复杂化学/生物系统（细胞通信网络）推理中的应用，与“化学大模型”和“质谱结构推理”在方法论（从数据中推理复杂结构/关系）上有共通之处，且作为综述提供了重要的领域概览和资源索引。

**📖 中文摘要**

本文对从单细胞和空间组学数据推断细胞间通信（CCC）的计算方法进行了全面综述。文章介绍了CCC的生物学机制和建模策略，并重点概述了140多种计算方法，强调了方法框架和生物学问题的多样性。最后，讨论了当前挑战和未来机遇，并总结了一个在线交互资源以方便方法比较和选择。这篇综述系统地梳理了利用计算模型（包括基于知识库和从头推断的方法）从高通量生物数据中解析细胞通信网络这一前沿领域，涵盖了大量的数据资源和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In multicellular organisms, cells coordinate their activities through cell-cell communication (CCC), which is crucial for development, tissue homeostasis, and disease progression. Recent advances in single-cell and spatial omics technologies provide unprecedented opportunities to systematically infer and analyze CCC from these omics data, either by integrating prior knowledge of ligand-receptor interactions (LRIs) or through de novo approaches. A variety of computational methods have been developed, focusing on methodological innovations, accurate modeling of complex signaling mechanisms, and investigation of broader biological questions. These advances have greatly enhanced our ability to analyze CCC and generate biological hypotheses. Here, we introduce the biological mechanisms and modeling strategies of CCC, and provide a focused overview of more than 140 computational methods for inferring CCC from single-cell and spatial transcriptomic data, emphasizing the diversity in methodological frameworks and biological questions. Finally, we discuss the current challenges and future opportunities in this rapidly evolving field, and summarize available methods in an interactive online resource ( this https URL ) to facilitate more efficient method comparison and selection.

</details>

---

### 65. [Generalization of Long-Range Machine Learning Potentials in Complex Chemical Spaces](https://arxiv.org/abs/2512.10989)

**基本信息**

- 🔗 arXiv: [`2512.10989`](https://arxiv.org/abs/2512.10989)
- 👥 作者: Michal Sanocki, Julija Zavadlav
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10989.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升机器学习原子间势（MLIP）在复杂化学空间中的泛化能力，这是构建通用、可靠的“化学大模型”（特别是用于分子模拟和性质预测的模型）的关键挑战。论文直接探讨了模型架构（长程修正）和评估策略如何影响化学空间中的泛化性能。

**📖 中文摘要**

本文系统地评估了不同具有长程修正的机器学习原子间势（MLIP）架构在多样化化学空间中的泛化能力。研究指出，长程建模方案对于实现可泛化的MLIP至关重要，不仅提高了分布内性能，更重要的是显著提升了模型在未见化学区域（分布外）的迁移能力。为了进行更严格的基准测试，论文引入了有偏的训练-测试分割策略，以明确测试模型在化学空间显著不同区域的表现。这项工作直接针对“化学大模型”中的一个核心挑战——如何在广阔的化学空间中实现模型的泛化。其研究框架和结论为设计更稳健、可迁移的化学机器学习模型（可视为特定领域的化学基础模型）提供了重要见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vastness of chemical space makes generalization a central challenge in the development of machine learning interatomic potentials (MLIPs). While MLIPs could enable large-scale atomistic simulations with near-quantum accuracy, their usefulness is often limited by poor transferability to out-of-distribution samples. Here, we systematically evaluate different MLIP architectures with long-range corrections across diverse chemical spaces and show that such schemes are essential, not only for improving in-distribution performance but, more importantly, for enabling significant gains in transferability to unseen regions of chemical space. To enable a more rigorous benchmarking, we introduce biased train-test splitting strategies, which explicitly test the model performance in significantly different regions of chemical space. Together, our findings highlight the importance of long-range modeling for achieving generalizable MLIPs and provide a framework for diagnosing systematic failures across chemical space. Although we demonstrate our methodology on metal-organic frameworks, it is broadly applicable to other materials, offering insights into the design of more robust and transferable MLIPs.

</details>

---

### 66. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准1和标准3：论文的核心研究内容直接围绕整合机器学习（ML）和量子计算（QC）来构建下一代药物发现的计算框架，这本质上是构建更强大的“化学大模型”（量子精度）的愿景。同时，论文也具有显著的综述和展望性质，它系统性地分析了HPC、ML、QC融合的趋势、挑战和未来机遇，为下一代化学信息学和计算化学模型的发展指明了方向。

**📖 中文摘要**

本文探讨了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何彻底改变药物发现范式。论文指出，机器学习基础模型（如FeNNix-Bio1）能够实现量子精度的模拟，但其数据生成仍受限于经典计算。而高性能量子计算（HPQC）利用混合QPU-GPU架构，将成为量子化学数据的终极加速器，实现真正的化学精度。文章详细阐述了这种三方融合如何优化从系统准备到ML驱动的高保真模拟的整个药物发现流程，并将量子增强采样定位为超越GPU的下一代前沿技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

## 📊 数据统计
- 累计运行天数：44
- 累计论文数量：3164

## 📝 历史记录

> 暂无历史数据

