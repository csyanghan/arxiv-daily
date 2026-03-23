# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-23 01:28:45

## 📅 2026-03-23 (今日最新)

**相关论文数：88**

### 1. [InfoMamba: An Attention-Free Hybrid Mamba-Transformer Model](https://arxiv.org/abs/2603.18031)

**基本信息**

- 🔗 arXiv: [`2603.18031`](https://arxiv.org/abs/2603.18031)
- 👥 作者: Youjin Wang, Jiaqiao Zhao, Rong Fu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18031.pdf)

**💡 相关性分析**

满足标准1：论文提出的InfoMamba混合架构（结合SSM与全局接口）为构建高效、可扩展的化学大模型（如用于分子序列或光谱序列建模）提供了核心的技术思路和模型设计范例。

**📖 中文摘要**

本文提出了InfoMamba，一种无需注意力的混合Mamba-Transformer模型，旨在解决序列建模中细粒度局部建模与长程依赖捕获的平衡问题。该模型用概念瓶颈线性过滤层替代了token级别的自注意力，并通过信息最大化融合（IMF）将其与选择性循环流集成。虽然论文主要关注通用序列建模任务（如分类、密集预测），但其核心架构创新——结合状态空间模型（SSM）与全局接口——为构建高效的化学大模型（例如用于分子序列或光谱序列建模）提供了有前景的技术路径。该工作满足标准1，因为它提出的混合架构是构建高效、可扩展化学大模型的一种潜在核心方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Balancing fine-grained local modeling with long-range dependency capture under computational constraints remains a central challenge in sequence modeling. While Transformers provide strong token mixing, they suffer from quadratic complexity, whereas Mamba-style selective state-space models (SSMs) scale linearly but often struggle to capture high-rank and synchronous global interactions. We present a consistency boundary analysis that characterizes when diagonal short-memory SSMs can approximate causal attention and identifies structural gaps that remain. Motivated by this analysis, we propose InfoMamba, an attention-free hybrid architecture. InfoMamba replaces token-level self-attention with a concept bottleneck linear filtering layer that serves as a minimal-bandwidth global interface and integrates it with a selective recurrent stream through information-maximizing fusion (IMF). IMF dynamically injects global context into the SSM dynamics and encourages complementary information usage through a mutual-information-inspired objective. Extensive experiments on classification, dense prediction, and non-vision tasks show that InfoMamba consistently outperforms strong Transformer and SSM baselines, achieving competitive accuracy-efficiency trade-offs while maintaining near-linear scaling.

</details>

---

### 2. [Adapting Methods for Domain-Specific Japanese Small LMs: Scale, Architecture, and Quantization](https://arxiv.org/abs/2603.18037)

**基本信息**

- 🔗 arXiv: [`2603.18037`](https://arxiv.org/abs/2603.18037)
- 👥 作者: Takato Yasuno
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18037.pdf)

**💡 相关性分析**

满足标准1：论文提出的构建领域特定小语言模型的系统性方法论（包括规模确定、模型选择和量化）可直接应用于化学信息学领域，为构建专业、高效的化学大模型提供了可操作的指导框架。

**📖 中文摘要**

本文提出了一种系统性的方法，使用QLoRA微调来构建领域特定的日语小语言模型。研究探讨了三个核心问题：最佳训练规模、基础模型选择和架构感知量化。虽然论文以日语领域为例，但其方法论（包括规模学习实验、模型比较和量化策略）具有普适性。该框架为在化学信息学等低资源技术领域构建专业、紧凑的化学大模型（例如用于解析日语化学文献或生成特定领域文本）提供了可操作的指导。论文满足标准1，因为它为构建领域特定（可引申至化学领域）的语言模型提供了系统的方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents a systematic methodology for building domain-specific Japanese small language models using QLoRA fine-tuning. We address three core questions: optimal training scale, base-model selection, and architecture-aware quantization. Stage 1 (Training scale): Scale-learning experiments (1k--5k samples) identify n=4,000 as optimal, where test-set NLL reaches minimum (1.127) before overfitting at 5k samples. Stage 2 (Compare finetuned SLMs): Comparing four Japanese LLMs shows that Llama-3 models with Japanese continual pre-training (Swallow-8B, ELYZA-JP-8B) outperform multilingual models (Qwen2.5-7B). Stage 3 (Quantization): Llama-3 architectures improve under Q4_K_M quantization, while GQA architectures degrade severely (Qwen2.5: -0.280 points). Production recommendation: Swallow-8B Q4_K_M achieves 2.830/3 score, 8.9 s/question, 4.9 GB size. The methodology generalizes to low-resource technical domains and provides actionable guidance for compact Japanese specialist LMs on consumer hardware.

</details>

---

### 3. [Continually self-improving AI](https://arxiv.org/abs/2603.18073)

**基本信息**

- 🔗 arXiv: [`2603.18073`](https://arxiv.org/abs/2603.18073)
- 👥 作者: Zitong Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（持续自我改进的AI、合成数据增强、算法空间搜索）直接围绕如何构建和进化更强大的大模型，这些思路对于克服化学大模型面临的数据稀缺、知识获取和算法创新等挑战具有核心指导意义。

**📖 中文摘要**

本文探讨了实现持续自我改进AI的愿景，旨在突破当前语言模型在数据效率、人类数据依赖和训练算法方面的限制。论文提出了三个章节：1）使用合成数据方法从小型语料库中高效获取知识；2）利用固定的人类数据自生成合成数据以引导基础预训练能力；3）通过在算法空间进行测试时搜索，超越人类设计的训练范式。这些研究方向与“化学大模型”的主题高度相关，因为化学领域同样面临高质量数据稀缺、领域知识获取效率低以及需要探索超越人类设计的新型分子生成或性质预测算法等挑战。该工作为化学大模型的持续学习和自我进化提供了前瞻性的研究思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern language model-based AI systems are remarkably powerful, yet their capabilities remain fundamentally capped by their human creators in three key ways. First, although a model's weights can be updated via fine-tuning, acquiring new knowledge from small, specialized corpora after pretraining remains highly data-inefficient. Second, the training of these systems relies heavily on finite, human-generated data from across history. Third, the pipelines used to train AI models are confined by the algorithms that human researchers can discover and explore. This thesis takes a small step toward overcoming these inherent limitations, presenting three chapters aimed at breaking these dependencies to create continually self-improving AI. First, to overcome this data-efficiency barrier in knowledge acquisition, we propose a synthetic data approach that diversifies and amplifies small corpora into rich knowledge representations, enabling a model to effectively update its parameters from limited source material. Second, to reduce reliance on human data, we show that given a fixed amount of such data, the model can self-generate synthetic data to bootstrap its fundamental pretraining capabilities without distillation from any off-the-shelf, instruction-tuned LM. Finally, to transcend human-engineered training paradigms, we demonstrate that by scaling search during test time over the space of algorithms, AI can search over a larger space of learning algorithm configurations than human researchers can explore manually.

</details>

---

### 4. [Lightweight Adaptation for LLM-based Technical Service Agent: Latent Logic Augmentation and Robust Noise Reduction](https://arxiv.org/abs/2603.18074)

**基本信息**

- 🔗 arXiv: [`2603.18074`](https://arxiv.org/abs/2603.18074)
- 👥 作者: Yi Yu, Junzhuo Ma, Chenghuang Shen 等18人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18074.pdf)

**💡 相关性分析**

满足标准1：论文提出的轻量级适配框架（潜在逻辑增强、噪声减少、混合奖励）为解决化学大模型在复杂化学任务（如实验规划、结构推理）中进行领域特定微调时面临的监督模糊、决策逻辑不透明和训练效率问题提供了直接相关的技术方案。

**📖 中文摘要**

本文提出了一个用于技术服务领域大语言模型轻量级适配的框架，以解决人类演示中缺乏显式认知链和有效响应多样性导致的模糊性问题。框架包含三个关键贡献：潜在逻辑增强、鲁棒噪声减少和轻量级适配（混合奖励机制）。虽然应用场景是云服务，但其解决的核心问题——如何让大模型在复杂、模糊的领域任务中内化潜在决策逻辑并实现高效、稳定的对齐——与“化学大模型”的领域适配需求高度一致。例如，让化学大模型学习复杂的实验操作流程或结构解析规则时，同样面临监督信号不明确和响应多样性问题。该框架为化学大模型的领域微调提供了可行的技术方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting Large Language Models in complex technical service domains is constrained by the absence of explicit cognitive chains in human demonstrations and the inherent ambiguity arising from the diversity of valid responses. These limitations severely hinder agents from internalizing latent decision dynamics and generalizing effectively. Moreover, practical adaptation is often impeded by the prohibitive resource and time costs associated with standard training paradigms. To overcome these challenges and guarantee computational efficiency, we propose a lightweight adaptation framework comprising three key contributions. (1) Latent Logic Augmentation: We introduce Planning-Aware Trajectory Modeling and Decision Reasoning Augmentation to bridge the gap between surface-level supervision and latent decision logic. These approaches strengthen the stability of Supervised Fine-Tuning alignment. (2) Robust Noise Reduction: We construct a Multiple Ground Truths dataset through a dual-filtering method to reduce the noise by validating diverse responses, thereby capturing the semantic diversity. (3) Lightweight Adaptation: We design a Hybrid Reward mechanism that fuses an LLM-based judge with a lightweight relevance-based Reranker to distill high-fidelity reward signals while reducing the computational cost compared to standard LLM-as-a-Judge reinforcement learning. Empirical evaluations on real-world Cloud service tasks, conducted across semantically diverse settings, demonstrate that our framework achieves stability and performance gains through Latent Logic Augmentation and Robust Noise Reduction. Concurrently, our Hybrid Reward mechanism achieves alignment comparable to standard LLM-as-a-judge methods with reduced training time, underscoring the practical value for deploying technical service agents.

</details>

---

### 5. [CytoSyn: a Foundation Diffusion Model for Histopathology -- Tech Report](https://arxiv.org/abs/2603.18089)

**基本信息**

- 🔗 arXiv: [`2603.18089`](https://arxiv.org/abs/2603.18089)
- 👥 作者: Thomas Duboudin, Xavier Fontaine, Etienne Andrier 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18089.pdf)

**💡 相关性分析**

满足标准1：论文的核心工作是构建一个面向特定科学领域（组织病理学）的生成式基础模型。这为在化学领域构建类似的生成式大模型（如用于分子、反应或光谱生成）提供了直接相关的技术范例、训练方法和评估基准。

**📖 中文摘要**

本文介绍了CytoSyn，一个用于组织病理学的最先进基础潜在扩散模型，能够生成高度逼真和多样化的H&E染色图像。该模型在超过10,000张TCGA诊断全切片图像上训练，涵盖32种癌症类型。虽然论文聚焦于医学图像生成，但其核心贡献——构建一个针对特定科学领域（组织病理学）的大规模、高质量生成式基础模型——为“化学大模型”主题提供了一个强有力的范例。在化学领域，类似地可以构建用于生成分子结构、反应路径或光谱数据的生成式基础模型。该工作展示了如何为数据密集的科学领域构建和评估生成式大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational pathology has made significant progress in recent years, fueling advances in both fundamental disease understanding and clinically ready tools. This evolution is driven by the availability of large amounts of digitized slides and specialized deep learning methods and models. Multiple self-supervised foundation feature extractors have been developed, enabling downstream predictive applications from cell segmentation to tumor sub-typing and survival analysis. In contrast, generative foundation models designed specifically for histopathology remain scarce. Such models could address tasks that are beyond the capabilities of feature extractors, such as virtual staining. In this paper, we introduce CytoSyn, a state-of-the-art foundation latent diffusion model that enables the guided generation of highly realistic and diverse histopathology H&E-stained images, as shown in an extensive benchmark. We explored methodological improvements, training set scaling, sampling strategies and slide-level overfitting, culminating in the improved CytoSyn-v2, and compared our work to PixCell, a state-of-the-art model, in an in-depth manner. This comparison highlighted the strong sensitivity of both diffusion models and performance metrics to preprocessing-specific details such as JPEG compression. Our model has been trained on a dataset obtained from more than 10,000 TCGA diagnostic whole-slide images of 32 different cancer types. Despite being trained only on oncology slides, it maintains state-of-the-art performance generating inflammatory bowel disease images. To support the research community, we publicly release CytoSyn's weights, its training and validation datasets, and a sample of synthetic images in this repository: this https URL .

</details>

---

### 6. [MOSS-TTS Technical Report](https://arxiv.org/abs/2603.18090)

**基本信息**

- 🔗 arXiv: [`2603.18090`](https://arxiv.org/abs/2603.18090)
- 👥 作者: Yitian Gong, Botian Jiang, Yiwei Zhao 等26人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18090.pdf)

**💡 相关性分析**

满足标准1：论文系统性地阐述了一个多模态生成式基础模型（MOSS-TTS）的完整构建方法论，包括tokenization、架构设计和训练策略。这套方法论为构建化学领域的多模态大模型（处理分子、光谱、文本）提供了直接相关的技术蓝图和设计思路。

**📖 中文摘要**

本技术报告介绍了MOSS-TTS，一个基于可扩展配方（离散音频token、自回归建模、大规模预训练）构建的语音生成基础模型。报告详细阐述了其设计、训练方法和经验特性。虽然主题是语音合成，但论文系统性地展示了一个“从tokenizer到生成器”的完整基础模型构建流水线，包括tokenizer设计（MOSS-Audio-Tokenizer）、模型架构选择（强调结构简单性与可扩展性的MOSS-TTS vs. 更高建模效率的MOSS-TTS-Local-Transformer）以及支持的各种控制功能。这套方法论对于构建化学领域的多模态大模型（例如，处理分子结构、光谱和文本）具有重要的参考价值，展示了如何为复杂序列数据设计和训练生成式基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This technical report presents MOSS-TTS, a speech generation foundation model built on a scalable recipe: discrete audio tokens, autoregressive modeling, and large-scale pretraining. Built on MOSS-Audio-Tokenizer, a causal Transformer tokenizer that compresses 24 kHz audio to 12.5 fps with variable-bitrate RVQ and unified semantic-acoustic representations, we release two complementary generators: MOSS-TTS, which emphasizes structural simplicity, scalability, and long-context/control-oriented deployment, and MOSS-TTS-Local-Transformer, which introduces a frame-local autoregressive module for higher modeling efficiency, stronger speaker preservation, and a shorter time to first audio. Across multilingual and open-domain settings, MOSS-TTS supports zero-shot voice cloning, token-level duration control, phoneme-/pinyin-level pronunciation control, smooth code-switching, and stable long-form generation. This report summarizes the design, training recipe, and empirical characteristics of the released models.

</details>

---

### 7. [Adaptive Domain Models: Bayesian Evolution, Warm Rotation, and Principled Training for Geometric and Neuromorphic AI](https://arxiv.org/abs/2603.18104)

**基本信息**

- 🔗 arXiv: [`2603.18104`](https://arxiv.org/abs/2603.18104)
- 👥 作者: Houston Haynes
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18104.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种全新的模型训练与部署架构，旨在实现高效、精确且保持领域几何结构（可引申至化学分子结构对称性）的训练。这为构建下一代高性能、低开销且具有可验证性的化学大模型提供了核心的基础设施创新思路。

**📖 中文摘要**

本文提出了一种名为“自适应领域模型”的替代性训练架构，旨在解决传统基于IEEE-754算术和反向模式自动微分的AI训练基础设施带来的内存开销、优化器复杂性和几何属性退化等问题。该架构结合了维度类型系统、确定性内存管理框架、程序超图和b-posit 2026算术标准，实现了深度无关的训练内存占用、保持几何等级的权重更新和精确梯度累积。论文还引入了贝叶斯蒸馏和热旋转等机制。虽然论文涉及几何和神经形态AI，但其核心贡献——一种新的、更高效、更精确且保持领域结构（如化学中的对称性）的模型训练与部署范式——与构建高性能、可验证的化学大模型高度相关。该工作为化学大模型的训练基础设施创新提供了前瞻性方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Prevailing AI training infrastructure assumes reverse-mode automatic differentiation over IEEE-754 arithmetic. The memory overhead of training relative to inference, optimizer complexity, and structural degradation of geometric properties through training are consequences of this arithmetic substrate. This paper develops an alternative training architecture grounded in three prior results: the Dimensional Type System and Deterministic Memory Management framework [6], which establishes stack-eligible gradient allocation and exact quire accumulation as design-time verifiable properties; the Program Hypergraph [8], which establishes grade preservation through geometric algebra computations as a type-level invariant; and the b-posit 2026 standard [10], which makes posit arithmetic tractable across hardware targets conventionally considered inference-only. Their composition enables depth-independent training memory bounded to approximately twice the inference footprint, grade-preserving weight updates, and exact gradient accumulation, applicable uniformly to loss-function-optimized and spike-timing-dependent neuromorphic models. We introduce Bayesian distillation, a mechanism by which the latent prior structure of a general-purpose model is extracted through the ADM training regime, resolving the data-scarcity bootstrapping problem for domain-specific training. For deployment, we introduce warm rotation, an operational pattern in which an updated model transitions into an active inference pathway without service interruption, with structural correctness formalized through PHG certificates and signed version records. The result is a class of domain-specific AI systems that are smaller and more precise than general-purpose models, continuously adaptive, verifiably correct with respect to the physical structure of their domains, and initializable from existing models.

</details>

---

### 8. [A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective](https://arxiv.org/abs/2603.18126)

**基本信息**

- 🔗 arXiv: [`2603.18126`](https://arxiv.org/abs/2603.18126)
- 👥 作者: Zhengze Xiao, Xuanzhe Ding, Yuyang Lou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18126.pdf)

**💡 相关性分析**

满足标准1：论文对NNVMC（一种用于量子化学/物理的科学计算大模型）进行了深入的计算工作负载分析。其分析框架、性能瓶颈识别和优化讨论，对于理解和优化用于“质谱结构推理”的复杂概率模型或化学大模型具有直接的相关性和指导意义。

**📖 中文摘要**

本文从计算工作负载特征的角度，对神经网络变分蒙特卡洛方法进行了综述和实证GPU表征分析。NNVMC是解决量子多体问题的一种有前景的范式，它将变分蒙特卡洛与表达性神经网络波函数拟设相结合。论文分析了四种代表性拟设（PauliNet, FermiNet, Psiformer, Orbformer）的模型级运行时/内存趋势和内核级行为。虽然应用领域是量子物理，但NNVMC本质上是一种用于学习高维复杂系统（如分子电子结构）概率分布的深度生成模型。该综述深入剖析了这类科学计算大模型在GPU上的性能瓶颈和优化机会，其分析框架和结论对于理解和优化用于“质谱结构推理”或分子性质预测的类似复杂概率模型具有重要参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Network Variational Monte Carlo (NNVMC) has emerged as a promising paradigm for solving quantum many-body problems by combining variational Monte Carlo with expressive neural-network wave-function ansätze. Although NNVMC can achieve competitive accuracy with favorable asymptotic scaling, practical deployment remains limited by high runtime and memory cost on modern graphics processing units (GPUs). Compared with language and vision workloads, NNVMC execution is shaped by physics-specific stages, including Markov-Chain Monte Carlo sampling, wave-function construction, and derivative/Laplacian evaluation, which produce heterogeneous kernel behavior and nontrivial bottlenecks. This paper provides a workload-oriented survey and empirical GPU characterization of four representative ansätze: PauliNet, FermiNet, Psiformer, and Orbformer. Using a unified profiling protocol, we analyze model-level runtime and memory trends and kernel-level behavior through family breakdown, arithmetic intensity, roofline positioning, and hardware utilization counters. The results show that end-to-end performance is often constrained by low-intensity elementwise and data-movement kernels, while the compute/memory balance varies substantially across ansätze and stages. Based on these findings, we discuss algorithm--hardware co-design implications for scalable NNVMC systems, including phase-aware scheduling, memory-centric optimization, and heterogeneous acceleration.

</details>

---

### 9. [How LLMs Distort Our Written Language](https://arxiv.org/abs/2603.18161)

**基本信息**

- 🔗 arXiv: [`2603.18161`](https://arxiv.org/abs/2603.18161)
- 👥 作者: Marwa Abdulhai, Isadora White, Yanming Wan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18161.pdf)

**💡 相关性分析**

满足标准3：论文虽然不是专门针对化学大模型的综述，但它包含了对大语言模型如何系统性地影响专业内容生成（如科学写作）的重要讨论和实证分析。这对于思考化学大模型在科研写作、知识记录中的应用伦理和潜在风险具有重要的相关性和展望价值。

**📖 中文摘要**

本文通过用户研究和数据分析，探讨了大语言模型如何扭曲人类的书面语言。研究发现，广泛使用LLM会导致文章在回答主题问题时保持中立的比例大幅增加，并显著改变文本的语义含义。虽然论文主要关注通用写作，但其揭示的LLM对内容语义的系统性影响，对于“化学大模型”的应用具有重要警示意义。在化学领域，使用LLM辅助撰写研究报告、论文或实验记录时，同样需要警惕模型可能引入的偏见、模糊化关键发现或扭曲科学论述的准确性和创造性。该工作从社会技术角度审视了大模型的影响，是相关主题的重要讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are used by over a billion people globally, most often to assist with writing. In this work, we demonstrate that LLMs not only alter the voice and tone of human writing, but also consistently alter the intended meaning. First, we conduct a human user study to understand how people actually interact with LLMs when using them for writing. Our findings reveal that extensive LLM use led to a nearly 70% increase in essays that remained neutral in answering the topic question. Significantly more heavy LLM users reported that the writing was less creative and not in their voice. Next, using a dataset of human-written essays that was collected in 2021 before the widespread release of LLMs, we study how asking an LLM to revise the essay based on the human-written feedback in the dataset induces large changes in the resulting content and meaning. We find that even when LLMs are prompted with expert feedback and asked to only make grammar edits, they still change the text in a way that significantly alters its semantic meaning. We then examine LLM-generated text in the wild, specifically focusing on the 21% of AI-generated scientific peer reviews at a recent top AI conference. We find that LLM-generated reviews place significantly less weight on clarity and significance of the research, and assign scores that, on average, are a full point this http URL findings highlight a misalignment between the perceived benefit of AI use and an implicit, consistent effect on the semantics of human writing, motivating future work on how widespread AI writing will affect our cultural and scientific institutions.

</details>

---

### 10. [Modeling the human lexicon under temperature variations: linguistic factors, diversity and typicality in LLM word associations](https://arxiv.org/abs/2603.18171)

**基本信息**

- 🔗 arXiv: [`2603.18171`](https://arxiv.org/abs/2603.18171)
- 👥 作者: Maria Andueza Rodriguez, Marie Candito, Richard Huyghe
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18171.pdf)

**💡 相关性分析**

满足标准3：论文通过系统的实验分析了LLM词汇联想的特性，其研究范式（模型与人类认知对比）和关于模型规模、温度影响输出行为的结论，为评估化学大模型在化学概念空间中的表征质量和生成行为提供了重要的方法论参考和相关讨论。

**📖 中文摘要**

本研究通过比较人类和LLM生成的词汇联想，评估了模型捕捉人类词汇模式的能力。研究使用了SWOW数据集中的英语线索-反应对，并生成了来自三个LLM在不同温度设置下的新联想。论文考察了词频和具体性等词汇因素的影响，以及LLM反应与人类反应相比的变异性和典型性。研究发现，较大的模型倾向于模拟单一的“原型”人类参与者，而较小的模型产生更多变但不太典型的反应。这项研究对于理解大语言模型的内部词汇表征和生成行为具有重要意义。虽然不直接针对化学，但其研究范式（比较模型与人类在特定认知任务上的表现）和关于模型大小、温度对输出特性影响的结论，对于设计和评估“化学大模型”在化学概念联想、术语生成或结构描述等方面的能力具有方法论上的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) achieve impressive results in terms of fluency in text generation, yet the nature of their linguistic knowledge - in particular the human-likeness of their internal lexicon - remains uncertain. This study compares human and LLM-generated word associations to evaluate how accurately models capture human lexical patterns. Using English cue-response pairs from the SWOW dataset and newly generated associations from three LLMs (Mistral-7B, Llama-3.1-8B, and Qwen-2.5-32B) across multiple temperature settings, we examine (i) the influence of lexical factors such as word frequency and concreteness on cue-response pairs, and (ii) the variability and typicality of LLM responses compared to human responses. Results show that all models mirror human trends for frequency and concreteness but differ in response variability and typicality. Larger models such as Qwen tend to emulate a single "prototypical" human participant, generating highly typical but minimally variable responses, while smaller models such as Mistral and Llama produce more variable yet less typical responses. Temperature settings further influence this trade-off, with higher values increasing variability but decreasing typicality. These findings highlight both the similarities and differences between human and LLM lexicons, emphasizing the need to account for model size and temperature when probing LLM lexical representations.

</details>

---

### 11. [GRAFITE: Generative Regression Analysis Framework for Issue Tracking and Evaluation](https://arxiv.org/abs/2603.18173)

**基本信息**

- 🔗 arXiv: [`2603.18173`](https://arxiv.org/abs/2603.18173)
- 👥 作者: Ja Young Lee, Mírian Silva, Mohamed Nasr 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18173.pdf)

**💡 相关性分析**

满足标准2：论文提出的GRAFITE平台是一个用于持续评估和追踪大模型性能的工具/系统。该平台可作为评估化学大模型在特定化学任务（如结构推理、性质预测）上表现的数据集构建、测试和比较框架，提供了重要的评估资源和方法。

**📖 中文摘要**

本文介绍了GRAFITE，一个通过问题跟踪和评估进行持续LLM评估的平台。该平台旨在解决由于基准数据在训练过程中过度暴露而导致的模型性能虚高风险。GRAFITE允许基于用户反馈随时间构建模型问题库，并提供使用LLM-as-a-judge进行质量保证测试的流水线，以评估LLM针对这些问题的表现。该平台支持多个模型的并排比较，便于检测不同版本之间的回归。虽然平台是通用的，但其核心功能——系统性、持续地评估和追踪大模型在特定问题或任务上的表现——对于“化学大模型”的开发和评估至关重要。化学领域需要评估模型在特定反应预测、性质计算或安全筛查等方面的性能，GRAFITE为此类评估提供了一个可行的技术框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are largely motivated by their performance on popular topics and benchmarks at the time of their release. However, over time, contamination occurs due to significant exposure of benchmark data during training. This poses a risk of model performance inflation if testing is not carefully executed. To address this challenge, we present GRAFITE, a continuous LLM evaluation platform through a comprehensive system for maintaining and evaluating model issues. Our approach enables building a repository of model problems based on user feedback over time and offers a pipeline for assessing LLMs against these issues through quality assurance (QA) tests using LLM-as-a-judge. The platform enables side-by-side comparison of multiple models, facilitating regression detection across different releases. The platform is available at this https URL . The demo video is available at this http URL .

</details>

---

### 12. [CWoMP: Morpheme Representation Learning for Interlinear Glossing](https://arxiv.org/abs/2603.18184)

**基本信息**

- 🔗 arXiv: [`2603.18184`](https://arxiv.org/abs/2603.18184)
- 👥 作者: Morris Alper, Enora Rice, Bhargav Shandilya 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18184.pdf)

**💡 相关性分析**

满足标准1：论文提出的CWoMP方法（基于原子单元表示学习和检索的序列生成）与“质谱结构推理”任务的核心挑战（将质谱碎片视为原子单元，推理出分子序列/结构）在方法论上直接相关，为后者提供了一种创新的技术思路。

**📖 中文摘要**

本文提出了CWoMP，一种用于语际注音任务的语素表示学习方法。与将注音视为字符序列的现有方法不同，CWoMP将语素视为具有学习表示的原子的形义单元。该方法使用对比训练的编码器将上下文中的单词与其组成语素在共享嵌入空间中对齐，然后自回归解码器通过从这些嵌入的可变词典中检索条目来生成语素序列。该方法在低资源语言上表现出色，且效率显著更高。虽然应用于语言学，但其核心思想——学习离散的、可解释的原子单元（语素）的表示，并通过检索生成序列——与“质谱结构推理”中学习质谱碎片（作为原子单元）的表示并推理分子结构的过程在方法论上高度相似。该工作为质谱解析提供了一种新颖的、基于表示学习和检索的生成范式灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Interlinear glossed text (IGT) is a standard notation for language documentation which is linguistically rich but laborious to produce manually. Recent automated IGT methods treat glosses as character sequences, neglecting their compositional structure. We propose CWoMP (Contrastive Word-Morpheme Pretraining), which instead treats morphemes as atomic form-meaning units with learned representations. A contrastively trained encoder aligns words-in-context with their constituent morphemes in a shared embedding space; an autoregressive decoder then generates the morpheme sequence by retrieving entries from a mutable lexicon of these embeddings. Predictions are interpretable--grounded in lexicon entries--and users can improve results at inference time by expanding the lexicon without retraining. We evaluate on diverse low-resource languages, showing that CWoMP outperforms existing methods while being significantly more efficient, with particularly strong gains in extremely low-resource settings.

</details>

---

### 13. [Retrieval-Augmented LLMs for Security Incident Analysis](https://arxiv.org/abs/2603.18196)

**基本信息**

- 🔗 arXiv: [`2603.18196`](https://arxiv.org/abs/2603.18196)
- 👥 作者: Xavier Cadet, Aditya Vikram Singh, Harsh Mamania 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18196.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于查询过滤和RAG增强LLM推理的安全事件分析框架，其技术架构（特征提取、上下文检索、多步推理、序列重建）与“质谱结构推理”的任务需求（碎片提取、知识检索、结构推导）高度一致，提供了直接相关的系统设计范例。

**📖 中文摘要**

本文提出了一个基于RAG的系统，用于通过基于查询的过滤和LLM语义推理进行安全事件分析。该系统使用带有相关MITRE ATT&CK技术的查询库从原始日志中提取指标，然后检索相关上下文以回答取证问题并重建攻击序列。论文在恶意软件流量事件和多阶段Active Directory攻击上评估了该系统。虽然应用于网络安全，但其技术框架——结合领域特定查询（可引申为化学规则或碎片模式）进行信息提取，并利用RAG增强的LLM进行多步推理和序列重建——与“质谱结构推理”的任务流程高度吻合。质谱解析同样需要从原始数据（质谱图）中提取特征（碎片离子），并基于化学知识库进行多步推理以确定分子结构。该工作为构建基于LLM和RAG的质谱解析系统提供了直接的技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Investigating cybersecurity incidents requires collecting and analyzing evidence from multiple log sources, including intrusion detection alerts, network traffic records, and authentication events. This process is labor-intensive: analysts must sift through large volumes of data to identify relevant indicators and piece together what happened. We present a RAG-based system that performs security incident analysis through targeted query-based filtering and LLM semantic reasoning. The system uses a query library with associated MITRE ATT\&CK techniques to extract indicators from raw logs, then retrieves relevant context to answer forensic questions and reconstruct attack sequences. We evaluate the system with five LLM providers on malware traffic incidents and multi-stage Active Directory attacks. We find that LLM models have different performance and tradeoffs, with Claude Sonnet~4 and DeepSeek~V3 achieving 100\% recall across all four malware scenarios, while DeepSeek costs 15$\times$ less (\$0.008 vs.\ \$0.12 per analysis). Attack step detection on Active Directory scenarios reaches 100\% precision and 82\% recall. Ablation studies confirm that a RAG architecture is essential: LLM baselines without RAG-enhanced context correctly identify victim hosts but miss all attack infrastructure including malicious domains and command-and-control servers. These results demonstrate that combining targeted query-based filtering with RAG-based retrieval enables accurate, cost-effective security analysis within LLM context limits.

</details>

---

### 14. [How Psychological Learning Paradigms Shaped and Constrained Artificial Intelligence](https://arxiv.org/abs/2603.18203)

**基本信息**

- 🔗 arXiv: [`2603.18203`](https://arxiv.org/abs/2603.18203)
- 👥 作者: Alex Anvi Eponon, Ildar Batyrshin, Christian E. Maldonado-Sifuentes 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18203.pdf)

**💡 相关性分析**

满足标准3：论文从认知科学和AI范式演变的角度进行了深入的综述和展望，分析了现有大模型范式的局限性，并提出了新的架构思考。这对于反思和展望“化学大模型”应具备的认知能力、知识表示和推理架构包含了重要的相关讨论和前瞻性观点。

**📖 中文摘要**

本文探讨了心理学学习范式（行为主义、认知主义、建构主义）如何塑造并制约了人工智能的发展，并指出了每种AI范式继承了其心理学理论基础的结构性局限。论文进一步分析了东西方对机械学习理解的差异，并提出了ReSynth三模块框架，将推理、目的和知识分离为架构上独立的组件。虽然是从宏观的AGI和认知科学角度出发，但其对现有AI范式局限性的深刻剖析以及对新架构的思考，对于“化学大模型”的顶层设计具有重要的启发意义。它促使研究者思考：当前用于化学任务的模型是否受限于其底层学习范式？如何设计一个能更好地适应化学领域系统性、组合性推理需求的大模型架构？该工作提供了重要的概念性框架和未来方向展望。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The dominant paradigms of artificial intelligence were shaped by learning theories from psychology: behaviorism inspired reinforcement learning, cognitivism gave rise to deep learning and memory-augmented architectures, and constructivism influenced curriculum learning and compositional approaches. This paper argues that each AI paradigm inherited not only the strengths but the structural limitations of the psychological theory that inspired it. Reinforcement learning cannot account for the internal structure of knowledge, deep learning compresses representations into opaque parameter spaces resistant to principled update, and current integrative approaches lack a formal account of how new understanding is constructed from existing components. The paper further examines a cross-cultural divergence in the interpretation of rote learning, arguing that the Eastern conception of memorization as a structured, multi-phase precursor to understanding offers an underexploited bridge between psychological theory and AI methodology. Drawing on the systematicity debate and critique of Aizawa of both classicism and connectionism, this paper introduces ReSynth, a trimodular framework that separates reasoning (Intellect), purpose (Identity), and knowledge (Memory) as architecturally independent components. The paper traces the genealogy from psychological paradigm to AI method, diagnoses the inherited limitations at each stage, and argues that adaptability, the central challenge of artificial general intelligence requires a representational architecture in which systematic behavior is a necessary consequence rather than an accidental property.

</details>

---

### 15. [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](https://arxiv.org/abs/2603.18256)

**基本信息**

- 🔗 arXiv: [`2603.18256`](https://arxiv.org/abs/2603.18256)
- 👥 作者: Philippe Formont, Maxime Darrin, Ismail Ben Ayed 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18256.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学大模型（用于分子生成的推理LLMs）和分子设计/生成（与质谱结构推理高度相关的任务）展开。

**📖 中文摘要**

本文介绍了MolRGen，这是一个用于训练和评估基于推理的大语言模型（LLMs）进行从头分子生成的大规模基准和数据集。该研究旨在弥补现有方法的空白，这些方法要么侧重于评估，要么依赖于需要已知属性修饰的分子对等真实标签的监督训练。MolRGen提出了一个用于从头分子生成和属性预测的评估和训练设置，其中目标是生成优化期望得分的新分子，而无需事先了解高分候选分子。作者还引入了一种新颖的多样性感知top-k分数，以捕捉生成分子的质量和多样性。他们展示了该设置可用于训练LLMs进行分子生成，使用强化学习训练了一个240亿参数的LLM，并对其性能和局限性进行了详细分析。这项工作直接围绕化学大模型（特别是用于分子设计的LLMs）和分子生成（这是化学信息学和质谱结构推理的核心任务）展开。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in reasoning-based large language models (LLMs) have demonstrated substantial improvements in complex problem-solving tasks. Motivated by these advances, several works have explored the application of reasoning LLMs to drug discovery and molecular design. However, most existing approaches either focus on evaluation or rely on training setups that require ground-truth labels, such as molecule pairs with known property modifications. Such supervision is unavailable in \textit{de novo} molecular generation, where the objective is to generate novel molecules that optimize a desirability score without prior knowledge of high-scoring candidates. To bridge this gap, we introduce MolRGen, a large-scale benchmark and dataset for training and evaluating reasoning-based LLMs on \textit{de novo} molecular generation. Our contributions are threefold. First, we propose a setting to evaluate and train models for \textit{de novo} molecular generation and property prediction. Second, we introduce a novel diversity-aware top-$k$ score that captures both the quality and diversity of generated molecules. Third, we show our setting can be used to train LLMs for molecular generation, training a 24B LLM with reinforcement learning, and we provide a detailed analysis of its performance and limitations.

</details>

---

### 16. [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297)

**基本信息**

- 🔗 arXiv: [`2603.18297`](https://arxiv.org/abs/2603.18297)
- 👥 作者: Zijin Gu, Tatiana Likhomanenko, Vimal Thilak 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18297.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕质谱结构推理，提出了一个名为FlowMS的新框架，用于从质谱进行从头分子结构解析。

**📖 中文摘要**

本文提出了FlowMS，这是首个用于谱图条件从头分子生成的离散流匹配框架。该工作解决了从质谱（MS）进行从头结构解析的挑战。FlowMS通过概率空间中的迭代精炼生成分子图，同时强制执行化学式约束，并以来自预训练公式Transformer编码器的谱图嵌入为条件。该方法在NPLIB1基准测试的6个指标中的5个上实现了最先进的性能，包括9.15%的top-1准确率（相对于DiffMS有9.7%的相对改进）和7.96的top-10 MCES（相对于MS-BART有4.2%的改进）。可视化结果进一步表明，FlowMS生成了结构上合理的候选分子，与真实结构非常相似。这些结果确立了离散流匹配作为基于质谱的结构解析（应用于代谢组学和天然产物发现）的一个有前景的范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Mixture-of-Experts (MoE) architectures enable efficient scaling by activating only a subset of parameters for each input. However, conventional MoE routing selects each layer's experts independently, creating N^L possible expert paths -- for N experts across L layers. This far exceeds typical training set sizes, leading to statistical inefficiency as the model may not learn meaningful structure over such a vast path space. To constrain it, we propose \pathmoe, which shares router parameters across consecutive layers. Experiments on 0.9B and 16B parameter models demonstrate consistent improvements on perplexity and downstream tasks over independent routing, while eliminating the need for auxiliary load balancing losses. Analysis reveals that tokens following the same path naturally cluster by linguistic function, with \pathmoe{} producing more concentrated groups, better cross-layer consistency, and greater robustness to routing perturbations. These results offer a new perspective for understanding MoE architectures through the lens of expert paths.

</details>

---

### 17. [Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information](https://arxiv.org/abs/2603.18359)

**基本信息**

- 🔗 arXiv: [`2603.18359`](https://arxiv.org/abs/2603.18359)
- 👥 作者: Shih-Heng Wang, Tiantian Feng, Aditya Kommineni 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18359.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（使用稀疏自编码器解释神经模型的内部表示）与理解和解释化学大模型（这是化学信息学和质谱分析中模型发展的关键方面）的研究主题高度相关。

**📖 中文摘要**

本文研究了神经音频编解码器（NACs）如何编码语言和副语言信息，并专注于一个具有挑战性的副语言属性——口音。作者采用稀疏自编码器（SAEs）将密集的NAC表示分解为稀疏、可解释的激活。他们提出了一个量化NAC可解释性的框架，并在16种SAE配置下评估了四种NAC模型。结果表明，声学导向的NACs主要在稀疏表示的激活幅度中编码口音信息，而语音导向的NACs则更多地依赖于激活位置。这项工作通过可解释性方法（SAEs）深入探究了神经编码模型（NACs）的内部表示，这与理解化学大模型（如用于分子表示的模型）的内部工作机制在方法论和精神上高度相关。虽然应用领域是音频，但其核心——分析复杂神经模型如何编码特定信息——与化学信息学中理解模型如何编码分子结构或质谱特征的研究主题直接平行。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented NACs encode accent information primarily in activation magnitudes of sparse representations, whereas phonetic-oriented NACs rely more on activation positions, and that low-bitrate EnCodec variants show higher interpretability.

</details>

---

### 18. [TENSURE: Fuzzing Sparse Tensor Compilers (Registered Report)](https://arxiv.org/abs/2603.18372)

**基本信息**

- 🔗 arXiv: [`2603.18372`](https://arxiv.org/abs/2603.18372)
- 👥 作者: Kabilan Mahathevan, Yining Zhang, Muhammad Ali Gulzar 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18372.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于测试稀疏张量编译器的新框架和基准（TENSURE），稀疏张量是在科学计算和化学信息学中常见的数据结构。该工具和基准可作为相关领域开发和评估计算工具的资源。

**📖 中文摘要**

本文提出了TENSURE，这是首个专门为测试稀疏张量编译器（STCs）而设计的可扩展黑盒模糊测试框架。STCs是优化高维数据分析和机器学习工作负载的关键基础设施。TENSURE使用爱因斯坦求和（Einsum）符号作为通用输入抽象，能够生成复杂、非常规的张量收缩，以暴露STCs代码生成阶段的边界情况。它提出了一种新颖的基于约束的生成算法，保证合成内核100%的语义有效性，显著优于基线语法模糊测试器约3.3%的有效性率。该框架引入了语义保留的变异操作符，利用代数交换性和存储格式的异质性进行蜕变测试。对TACO和Finch这两个最先进系统的评估揭示了广泛的脆弱性。这项工作为稀疏编译生态系统提供了专门的测试工具。虽然主要关注编译器测试，但其核心是处理和分析“稀疏张量”这种在科学计算（包括化学模拟和可能的大规模化学数据分析）中常见的数据结构。开发用于此类数据结构的工具和基准与化学信息学的基础设施建设相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Tensor Compilers (STCs) have emerged as critical infrastructure for optimizing high-dimensional data analytics and machine learning workloads. The STCs must synthesize complex, irregular control flow for various compressed storage formats directly from high-level declarative specifications, thereby making them highly susceptible to subtle correctness defects. Existing testing frameworks, which rely on mutating computation graphs restricted to a standard vocabulary of operators, fail to exercise the arbitrary loop synthesis capabilities of these compilers. Furthermore, generic grammar-based fuzzers struggle to generate valid inputs due to the strict rules governing how indices are reused across multiple tensors. In this paper, we present TENSURE, the first extensible black-box fuzzing framework specifically designed for the testing of STCs. TENSURE leverages Einstein Summation (Einsum) notation as a general input abstraction, enabling the generation of complex, unconventional tensor contractions that expose corner cases in the code-generation phases of STCs. We propose a novel constraint-based generation algorithm that guarantees 100% semantic validity of synthesized kernels, significantly outperforming the ~3.3% validity rate of baseline grammar fuzzers. To enable metamorphic testing without a trusted reference, we introduce a set of semantic-preserving mutation operators that exploit algebraic commutativity and heterogeneity in storage formats. Our evaluation on two state-of-the-art systems, TACO and Finch, reveals widespread fragility, particularly in TACO, where TENSURE exposed crashes or silent miscompilations in a majority of generated test cases. These findings underscore the critical need for specialized testing tools in the sparse compilation ecosystem.

</details>

---

### 19. [Mathematical Foundations of Deep Learning](https://arxiv.org/abs/2603.18387)

**基本信息**

- 🔗 arXiv: [`2603.18387`](https://arxiv.org/abs/2603.18387)
- 👥 作者: Xiaojing Ye
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18387.pdf)

**💡 相关性分析**

满足标准3：论文（书籍草稿）是一份综述性材料，系统地涵盖了生成模型和强化学习等主题，这些是构建化学领域大模型的核心理论基础，因此包含了对关注主题重要的相关讨论。

**📖 中文摘要**

本文是一本关于深度学习数学原理的书籍草稿。它提供了对现代深度学习背后数学原理的全面而严谨的处理。该书涵盖了核心理论主题，从深度神经网络的近似能力、最优控制和强化学习的理论与算法（与深度学习技术相结合），到推动当今人工智能进步的当代生成模型。虽然不专门针对化学，但该书系统地涵盖了生成模型和强化学习等主题，这些正是构建“化学大模型”（例如用于分子生成的生成模型或用于逆合成的强化学习智能体）所依赖的核心数学和算法基础。对于在化学信息学领域从事大模型研究和开发的研究人员来说，这是一份宝贵的教育资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This draft book offers a comprehensive and rigorous treatment of the mathematical principles underlying modern deep learning. The book spans core theoretical topics, from the approximation capabilities of deep neural networks, the theory and algorithms of optimal control and reinforcement learning integrated with deep learning techniques, to contemporary generative models that drive today's advances in artificial intelligence.

</details>

---

### 20. [Seeking Universal Shot Language Understanding Solutions](https://arxiv.org/abs/2603.18448)

**基本信息**

- 🔗 arXiv: [`2603.18448`](https://arxiv.org/abs/2603.18448)
- 👥 作者: Haoxin Liu, Harshavardhan Kamarthi, Zhiyuan Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18448.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于评估和提升视觉语言模型在复杂、主观的视觉语言理解任务（镜头语言理解）上性能的基准和解决方案。这与“化学大模型”主题中关于构建和评估能够处理复杂科学数据（如质谱、分子结构）的通用或领域大模型的研究目标直接相关，都涉及模型能力评估、数据构建和性能提升。

**📖 中文摘要**

这篇论文提出了SLU-SUITE，一个用于镜头语言理解（SLU）的综合训练和评估套件，包含33个任务、跨越六个电影维度的49万个人工标注的问答对。论文旨在解决视觉语言模型（VLMs）在SLU任务上与电影专家判断存在差异的问题。研究从模型和数据两个角度分析了VLM在SLU中的瓶颈，并提出了两种互补的通用SLU解决方案：UniShot（一个通过动态平衡数据混合训练的通用模型）和AgentShots（一个最大化各维度性能的专家集群）。这项工作为理解和提升模型在复杂视觉语言任务（如电影分析）上的能力提供了重要的数据集、基准和分析框架，与构建更强大的、能够处理复杂语义的“化学大模型”在方法论和挑战上具有高度相关性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Shot language understanding (SLU) is crucial for cinematic analysis but remains challenging due to its diverse cinematographic dimensions and subjective expert judgment. While vision-language models (VLMs) have shown strong ability in general visual understanding, recent studies reveal judgment discrepancies between VLMs and film experts on SLU tasks. To address this gap, we introduce SLU-SUITE, a comprehensive training and evaluation suite containing 490K human-annotated QA pairs across 33 tasks spanning six film-grounded dimensions. Using SLU-SUITE, we originally observe two insights into VLM-based SLU from: the model side, which diagnoses key bottlenecks of modules; the data side, which quantifies cross-dimensional influences among tasks. These findings motivate our universal SLU solutions from two complementary paradigms: UniShot, a balanced one-for-all generalist trained via dynamic-balanced data mixing, and AgentShots, a prompt-routed expert cluster that maximizes peak dimension performance. Extensive experiments show that our models outperform task-specific ensembles on in-domain tasks and surpass leading commercial VLMs by 22% on out-of-domain tasks.

</details>

---

### 21. [Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images](https://arxiv.org/abs/2603.18461)

**基本信息**

- 🔗 arXiv: [`2603.18461`](https://arxiv.org/abs/2603.18461)
- 👥 作者: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18461.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合了生物学先验知识（细胞类型原型）和深度学习的方法，从图像中预测分子水平的信息（基因表达）。这与“质谱结构推理”主题高度相关，因为两者都属于“从复杂数据中推断分子或化学结构/属性”这一核心问题。CPNN利用外部结构化生物数据（单细胞RNA-seq）来指导模型预测的思路，与质谱分析中利用已知质谱库或化学规则来辅助结构解析的理念相通。

**📖 中文摘要**

该论文提出了一种细胞类型原型信息神经网络（CPNN），用于从病理学图像中估计基因表达谱。该方法的关键创新在于利用公开可用的单细胞RNA测序数据集来估计细胞类型原型（即反映稳定基因共变关系的平均表达谱）。CPNN直接从图像中学习细胞类型组成权重，并建模原型与观测到的批量或空间表达之间的关系，从而提供了一个有生物学基础且结构正则化的预测框架。论文在三个切片级数据集和三个斑块级空间转录组数据集上进行了评估，结果表明CPNN在斯皮尔曼相关性方面达到了最高性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Estimating slide- and patch-level gene expression profiles from pathology images enables rapid and low-cost molecular analysis with broad clinical impact. Despite strong results, existing approaches treat gene expression as a mere slide- or spot-level signal and do not incorporate the fact that the measured expression arises from the aggregation of underlying cell-level expression. To explicitly introduce this missing cell-resolved guidance, we propose a Cell-type Prototype-informed Neural Network (CPNN) that leverages publicly available single-cell RNA-sequencing datasets. Since single-cell measurements are noisy and not paired with histology images, we first estimate cell-type prototypes-mean expression profiles that reflect stable gene-gene co-variation this http URL then learns cell-type compositional weights directly from images and models the relationship between prototypes and observed bulk or spatial expression, providing a biologically grounded and structurally regularized prediction framework. We evaluate CPNN on three slide-level datasets and three patch-level spatial transcriptomics datasets. Across all settings, CPNN achieves the highest performance in terms of Spearman correlation. Moreover, by visualizing the inferred compositional weights, our framework provides interpretable insights into which cell types drive the predicted expression. Code is publicly available at this https URL .

</details>

---

### 22. [A Faster Deterministic Algorithm for Kidney Exchange via Representative Set](https://arxiv.org/abs/2603.18471)

**基本信息**

- 🔗 arXiv: [`2603.18471`](https://arxiv.org/abs/2603.18471)
- 👥 作者: Kangyi Tian, Mingyu Xiao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18471.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为CAPSUL的新基准数据集，该数据集整合了蛋白质的3D结构信息和详细的亚细胞定位注释。这为开发能够利用结构信息进行生物分子属性预测的模型（可视为生物领域的“大模型”）提供了重要的数据资源。虽然领域是生物信息学，但其“整合多模态数据（序列、结构、注释）构建基准以推动模型发展”的核心范式，与化学信息学中构建用于分子性质预测或质谱解析的基准数据集的目标完全一致。

**📖 中文摘要**

这篇论文介绍了CAPSUL，一个用于蛋白质亚细胞定位的综合人类蛋白质基准。该基准的数据集整合了多样化的3D结构表示和由领域专家精心策划的细粒度亚细胞定位注释。论文评估了多种最先进的基于序列和基于结构的模型，展示了结构特征在此任务中的重要性。此外，论文还探索了重加权和单标签分类策略，以促进未来基于结构的方法研究。通过一个关于高尔基体的案例研究，展示了基于结构的方法强大的可解释性，发现了一个决定性的定位模式α-螺旋。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Kidney Exchange Problem is a prominent challenge in healthcare and economics, arising in the context of organ transplantation. It has been extensively studied in artificial intelligence and optimization. In a kidney exchange, a set of donor-recipient pairs and altruistic donors are considered, with the goal of identifying a sequence of exchange -- comprising cycles or chains starting from altruistic donors -- such that each donor provides a kidney to the compatible recipient in the next donor-recipient pair. Due to constraints in medical resources, some limits are often imposed on the lengths of these cycles and chains. These exchanges create a network of transplants aimed at maximizing the total number, $t$, of successful transplants. Recently, this problem was deterministically solved in $O^*(14.34^t)$ time (IJCAI 2024). In this paper, we introduce the representative set technique for the Kidney Exchange Problem, showing that the problem can be deterministically solved in $O^*(6.855^t)$ time.

</details>

---

### 23. [Leveraging Large Language Models for Generalizing Peephole Optimizations](https://arxiv.org/abs/2603.18477)

**基本信息**

- 🔗 arXiv: [`2603.18477`](https://arxiv.org/abs/2603.18477)
- 👥 作者: Chunhao Liao, Hongxu Xu, Xintong Zhou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18477.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索并利用大语言模型（LLMs）的语义抽象和探索推理能力，来自动化并改进一个特定领域（编译器优化）的复杂规则生成任务。这直接体现了“化学大模型”主题的一个核心应用方向：利用大模型的高级语义理解和生成能力，辅助或自动化化学领域的复杂任务，例如反应条件优化、合成路线设计或质谱解析规则的生成。论文展示了LLM在结构化、逻辑严密的领域内进行推理和生成的潜力。

**📖 中文摘要**

论文提出了LPG（大语言模型辅助的窥孔优化泛化）框架，该框架利用大语言模型（LLMs）来泛化编译器中的窥孔优化。LPG采用一个闭环工作流程，集成了LLM驱动的符号常量泛化、结构泛化、约束松弛和位宽/精度泛化，并辅以语法验证、语义验证和盈利性检查的反馈。论文在从LLVM生态系统中提取的真实世界窥孔优化问题上进行了评估，LPG成功泛化了102个优化中的90个。在可与Hydra直接比较的整数优化子集上，LPG泛化了81个中的74个，而Hydra仅泛化了35个。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Peephole optimizations are a core component of modern optimizing compilers. It rewrites specific instruction into semantically equivalent but more efficient forms. In practice, creating a new peephole optimization often starts from a concrete optimization instance and requires lifting it into a more general rewrite rule that matches a wider range of instruction patterns. This generalization step is critical to optimization effectiveness, but it is also difficult: producing rules that are both correct and sufficiently general typically demands substantial manual effort and domain expertise. Existing approaches such as Hydra attempt to automate this task with program synthesis, but their generalization capability is often limited by search-space explosion, under-generalization, and restricted support for diverse instruction domains. We present LPG, large language model aided peephole optimization generalization, a framework that uses large language models (LLMs) to generalize peephole optimizations. The design of LPG is motivated by the observation that LLMs are effective at semantic abstraction and exploratory reasoning, while formal analyses are necessary to ensure that generated rules are sound and profitable. Based on this observation, LPG adopts a closed-loop workflow that integrates LLM-driven symbolic constant generalization, structural generalization, constraint relaxation, and bitwidth/precision generalization with feedback from syntactic validation, semantic verification, and profitability checking. We evaluate LPG on real-world peephole optimization issues drawn from the LLVM ecosystem. Overall, LPG successfully generalizes 90 out of 102 optimizations. On the integer-focused subset that is directly comparable to Hydra, LPG generalizes 74 out of 81 optimizations, whereas Hydra generalizes 35.

</details>

---

### 24. [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505)

**基本信息**

- 🔗 arXiv: [`2603.18505`](https://arxiv.org/abs/2603.18505)
- 👥 作者: Jingzhi Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18505.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对AI驱动蛋白质科学发展的全面综述，特别强调了从静态结构预测到生成动态构象和复杂相互作用的范式转变。其中关于“生成框架”（包括扩散模型和流匹配）捕获与热力学系综一致的构象分布，以及“统一多模态表示”整合序列、几何和文本知识等内容，与“化学大模型”和“质谱结构推理”主题高度相关。它为化学领域类似的研究（如生成式分子设计、从光谱数据推断动态分子结构）提供了重要的跨领域见解、方法学参考和未来展望。

**📖 中文摘要**

这篇综述论文系统地审视了人工智能驱动的蛋白质科学在五个相互关联的维度上的范式转变：统一的多模态表示、静态预测的改进、生成框架、异质相互作用的预测以及功能推断。论文批判性地分析了当前的瓶颈，包括数据分布偏差、有限的机制可解释性以及几何指标与生物物理现实之间的脱节，同时确定了未来朝向物理一致的生成模型、多模态基础架构和实验闭环系统的方向。这篇综述标志着人工智能从结构分析工具向能够理解并最终重写生命动态语言的通用模拟器的转变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular interactions. This review systematically examines the paradigm shift in AI driven protein science across five interconnected dimensions: unified multimodal representations that integrate sequences, geometries, and textual knowledge; refinement of static prediction through MSA free architectures and all atom complex modeling; generative frameworks, including diffusion models and flow matching, that capture conformational distributions consistent with thermodynamic ensembles; prediction of heterogeneous interactions spanning protein ligand, protein nucleic acid, and protein protein complexes; and functional inference of fitness landscapes, mutational effects, and text guided property prediction. We critically analyze current bottlenecks, including data distribution biases, limited mechanistic interpretability, and the disconnect between geometric metrics and biophysical reality, while identifying future directions toward physically consistent generative models, multimodal foundation architectures, and experimental closed loop systems. This methodological transformation marks artificial intelligence's transition from a structural analysis tool into a universal simulator capable of understanding and ultimately rewriting the dynamic language of life.

</details>

---

### 25. [SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks](https://arxiv.org/abs/2603.18548)

**基本信息**

- 🔗 arXiv: [`2603.18548`](https://arxiv.org/abs/2603.18548)
- 👥 作者: Amanda A. Howard, Nicholas Zolman, Bruno Jacob 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18548.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合了可解释神经网络（KAN）和符号回归（SINDy）的新方法，用于从数据中发现可解释的、稀疏的动力学方程。这直接与“化学大模型”中追求模型可解释性和从数据中发现物理/化学规律的研究方向相关。在质谱分析中，从复杂光谱数据中推导出反映分子碎裂规律的解析表达式或简化模型也是一个重要的目标，因此该方法论具有潜在的相关性。

**📖 中文摘要**

本文提出了SINDy-KANs方法，该方法同时训练一个Kolmogorov-Arnold网络（KAN）和一个类似SINDy（非线性动力学稀疏识别）的表征，以提高KAN表征的可解释性。SINDy应用于每个激活函数的层面，同时保持通过深度KAN实现的函数组合能力。作者将方法应用于一系列符号回归任务，包括动力系统，以展示在不同系统中准确的方程发现能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method to a number of symbolic regression tasks, including dynamical systems, to show accurate equation discovery across a range of systems.

</details>

---

### 26. [Elastic Weight Consolidation Done Right for Continual Learning](https://arxiv.org/abs/2603.18596)

**基本信息**

- 🔗 arXiv: [`2603.18596`](https://arxiv.org/abs/2603.18596)
- 👥 作者: Xuan Liu, Xiaobin Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18596.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕模型权重重要性估计和修正方法展开，该方法论对于构建、理解和优化复杂的“化学大模型”（如用于性质预测、反应生成的深度学习模型）具有直接的相关性，涉及模型的可解释性、稳定性和知识迁移。

**📖 中文摘要**

本文对持续学习中的权重正则化方法进行了系统性分析，重点关注了基于梯度的权重重要性估计方法，如弹性权重巩固（EWC）。作者发现EWC及其变体在估计权重重要性时存在根本性的错位，导致性能不佳。为此，他们提出了一种名为Logits Reversal（LR）的简单而有效的修改，以纠正EWC的重要性估计。该研究通过在各种持续学习任务和数据集上的广泛实验，验证了所提方法的有效性。虽然论文主要关注持续学习中的权重正则化，但其核心方法——通过分析模型梯度（Fisher信息矩阵）来理解和修正模型行为——与化学信息学中构建和理解“化学大模型”时面临的模型可解释性、稳定性及知识保留等挑战在方法论上高度相关。该论文提出的梯度分析和修正框架，为开发和优化复杂的、需要持续适应新数据或任务的化学大模型提供了潜在的技术思路和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight regularization methods in continual learning (CL) alleviate catastrophic forgetting by assessing and penalizing changes to important model weights. Elastic Weight Consolidation (EWC) is a foundational and widely used approach within this framework that estimates weight importance based on gradients. However, it has consistently shown suboptimal performance. In this paper, we conduct a systematic analysis of importance estimation in EWC from a gradient-based perspective. For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios. Our analysis also reveals that Memory Aware Synapses (MAS), a variant of EWC, imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection. Consequently, both EWC and its variants exhibit fundamental misalignments in estimating weight importance, leading to inferior performance. To tackle these issues, we propose the Logits Reversal (LR) operation, a simple yet effective modification that rectifies EWC's importance estimation. Specifically, reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection. Extensive experiments across various CL tasks and datasets show that the proposed method significantly outperforms existing EWC and its variants. Therefore, we refer to it as EWC Done Right (EWC-DR).

</details>

---

### 27. [GEAR: Geography-knowledge Enhanced Analog Recognition Framework in Extreme Environments](https://arxiv.org/abs/2603.18626)

**基本信息**

- 🔗 arXiv: [`2603.18626`](https://arxiv.org/abs/2603.18626)
- 👥 作者: Zelin Liu, Bocheng Li, Yuling Zhou 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18626.pdf)

**💡 相关性分析**

满足标准1：论文提出的形态集成孪生图网络（MSG-Net）是一种用于处理复杂结构数据的图神经网络方法。该方法可直接应用于“质谱结构推理”任务，因为分子结构推理本质上是将质谱数据映射到分子图结构，图神经网络是该领域的核心模型范式。

**📖 中文摘要**

本文提出了GEAR框架，用于在极端环境（如马里亚纳海沟和青藏高原）中进行跨域地形相似性检索，以识别结构同源的陆地类似物。该框架的核心创新之一是设计了一种基于图神经网络的模型——形态集成孪生图网络（MSG-Net）。该模型利用地貌学指标进行精细识别。实验表明，MSG-Net提取的特征与生物数据存在显著相关性，为未来的生物分析提供了证据。虽然论文的应用场景是地理学，但其核心技术——使用图神经网络（GNN）处理具有复杂结构和关系的科学数据（此处为地形数据）——与“质谱结构推理”高度相关。在质谱分析中，分子结构可以自然地表示为图（原子为节点，化学键为边），图神经网络正是当前进行质谱谱图到分子结构推理的最先进和核心方法之一。因此，该论文提出的MSG-Net架构及其在复杂科学数据上的应用，为质谱结构推理任务提供了新的模型设计思路和验证案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Mariana Trench and the Qinghai-Tibet Plateau exhibit significant similarities in geological origins and microbial metabolic functions. Given that deep-sea biological sampling faces prohibitive costs, recognizing structurally homologous terrestrial analogs of the Mariana Trench on the Qinghai-Tibet Plateau is of great significance. Yet, no existing model adequately addresses cross-domain topographic similarity retrieval, either neglecting geographical knowledge or sacrificing computational efficiency. To address these challenges, we present \underline{\textbf{G}}eography-knowledge \underline{\textbf{E}}nhanced \underline{\textbf{A}}nalog \underline{\textbf{R}}ecognition (\textbf{GEAR}) Framework, a three-stage pipeline designed to efficiently retrieve analogs from 2.5 million square kilometers of the Qinghai-Tibet Plateau: (1) Skeleton guided Screening and Clipping: Recognition of candidate valleys and initial screening based on size and linear morphological criteria. (2) Physics aware Filtering: The Topographic Waveform Comparator (TWC) and Morphological Texture Module (MTM) evaluate the waveform and texture and filter out inconsistent candidate valleys. (3) Graph based Fine Recognition: We design a \underline{\textbf{M}}orphology-integrated \underline{\textbf{S}}iamese \underline{\textbf{G}}raph \underline{\textbf{N}}etwork (\textbf{MSG-Net}) based on geomorphological metrics. Correspondingly, we release an expert-annotated topographic similarity dataset targeting tectonic collision zones. Experiments demonstrate the effectiveness of every stage. Besides, MSG-Net achieved an F1-Score 1.38 percentage points higher than the SOTA baseline. Using features extracted by MSG-Net, we discovered a significant correlation with biological data, providing evidence for future biological analysis.

</details>

---

### 28. [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660)

**基本信息**

- 🔗 arXiv: [`2603.18660`](https://arxiv.org/abs/2603.18660)
- 👥 作者: Peihang Wu, Zehong Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18660.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对多模态计算病理学的综述，其中包含对自监督表示学习和令牌压缩等重要技术的深入讨论。这些技术是构建“化学大模型”（如分子预训练模型）和进行“质谱结构推理”（如谱图表征学习）的核心方法论，因此提供了重要的相关讨论和展望。

**📖 中文摘要**

本文是一篇关于多模态计算病理学的综述性文章，系统性地分析了该领域的四个研究方向。其中，第一个方向专门讨论了全切片图像（WSI）的自监督表示学习和结构感知的令牌压缩技术。文章指出，WSI的极高分辨率给视觉学习带来了计算挑战，而有限的专家标注约束了监督方法的发展。因此，自监督学习在从海量无标注病理图像中学习通用表示方面至关重要。同时，为了处理千兆像素的图像，需要对图像令牌进行压缩以进行跨尺度建模。这些技术挑战和解决方案（自监督表示学习、令牌压缩）与“化学大模型”和“质谱结构推理”领域面临的问题高度相似。在化学信息学中，构建大模型同样需要从海量无标注分子数据（如SMILES、分子图、质谱谱图）中进行自监督预训练，并且需要高效处理高维、序列或图结构的数据表示。该综述为化学领域开发类似的基础模型提供了可借鉴的技术路线和分析框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Whole slide imaging (WSI) has transformed digital pathology by enabling computational analysis of gigapixel histopathology images. Recent foundation model advances have accelerated progress in computational pathology, facilitating joint reasoning across pathology images, clinical reports, and structured data. Despite this progress, challenges remain: the extreme resolution of WSIs creates computational hurdles for visual learning; limited expert annotations constrain supervised approaches; integrating multimodal information while preserving biological interpretability remains difficult; and the opacity of modeling ultra-long visual sequences hinders clinical transparency. This review comprehensively surveys recent advances in multimodal computational pathology. We systematically analyze four research directions: (1) self-supervised representation learning and structure-aware token compression for WSIs; (2) multimodal data generation and augmentation; (3) parameter-efficient adaptation and reasoning-enhanced few-shot learning; and (4) multi-agent collaborative reasoning for trustworthy diagnosis. We specifically examine how token compression enables cross-scale modeling and how multi-agent mechanisms simulate a pathologist's "Chain of Thought" across magnifications to achieve uncertainty-aware evidence fusion. Finally, we discuss open challenges and argue that future progress depends on unified multimodal frameworks integrating high-resolution visual data with clinical and biomedical knowledge to support interpretable and safe AI-assisted diagnosis.

</details>

---

### 29. [STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation](https://arxiv.org/abs/2603.18688)

**基本信息**

- 🔗 arXiv: [`2603.18688`](https://arxiv.org/abs/2603.18688)
- 👥 作者: Chen Zhang, Liwei Liu, Jun Tao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18688.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是针对科学时间序列的预训练表示学习框架（STEP）。这直接与“化学大模型”的主题相关，因为质谱数据是一种重要的科学时间序列，该框架为构建质谱预训练模型提供了方法论。同时，该框架本身可被视为一种用于科学数据（包括质谱）表示学习的“工具”或“资源”。

**📖 中文摘要**

本文提出了STEP框架，一个用于科学时间序列编码器预训练的跨域蒸馏框架。科学时间序列通常具有稀疏、高度异构和数据规模有限的特点，使得统一的表示学习面临挑战。STEP框架通过自适应分块处理极长序列，利用统计补偿方案适应不同的数值尺度，并关键地通过跨域蒸馏整合来自多个相关领域（如音频、通用时间序列、脑信号）基础模型的知识，以学习适用于科学信号的通用、可迁移特征。该研究在七个科学时间序列任务上进行了实验验证。虽然应用领域不同，但STEP框架解决的核心问题——如何利用有限、异构的科学数据训练出强大的表示学习模型——与化学信息学中构建“化学大模型”和进行“质谱结构推理”所面临的挑战完全一致。质谱数据本身就是一种特殊的时间序列/频谱序列，STEP中处理序列长度、数值尺度异构性以及利用预训练模型进行知识迁移的方法，为开发针对质谱数据的预训练模型提供了直接且宝贵的技术蓝图和思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientific tasks and their complementary strengths. Based on this observation, we propose STEP, a Scientific Time Series Encoder Pretraining framework via cross domain distillation. STEP introduces adaptive patching to handle extreme-length sequences and a statistics compensation scheme to accommodate diverse numerical scales. It further leverages cross-domain distillation to integrate knowledge from multiple foundation models into a unified encoder. By combining complementary representations across different domains, STEP learns general-purpose and transferable features tailored for scientific signals. Experiments on seven scientific time series tasks demonstrate that STEP provides both an effective structure and an effective pretraining paradigm, taking a STEP toward scientific time series representation learning.

</details>

---

### 30. [CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks](https://arxiv.org/abs/2603.18736)

**基本信息**

- 🔗 arXiv: [`2603.18736`](https://arxiv.org/abs/2603.18736)
- 👥 作者: Hao Wang, Licheng Pan, Zhichao Chen 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18736.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对有噪声和偏差的观测数据设计无偏的模型学习框架（CausalRM）。该方法论对于利用真实世界中存在噪声和系统偏差的化学数据（如质谱数据、生物测定数据）来训练“化学大模型”或“质谱结构推理”模型具有直接的相关性和应用潜力。

**📖 中文摘要**

本文提出了CausalRM，一个基于因果理论的奖励建模框架，用于从观测性用户反馈（如点击、复制、点赞）中进行强化学习人类反馈（RLHF）。论文指出了当前从观测反馈学习奖励模型的两个根本挑战：反馈噪声和用户偏好偏差。CausalRM通过显式建模标注错误生成过程来设计噪声感知的代理损失项，并利用倾向得分对训练样本进行重新加权以消除用户偏好偏差。该框架旨在从有噪声和有偏的观测数据中学习无偏的奖励模型。这项研究虽然针对的是NLP中的RLHF，但其核心方法论——使用因果推理和倾向得分校正来处理有噪声、有偏的观测数据以学习更准确的模型——与化学信息学和质谱分析中的关键问题高度相关。例如，在质谱结构推理中，训练数据可能来自不同仪器、不同实验条件，存在系统偏差和噪声；在构建化学大模型时，使用的生物活性数据等也可能存在类似的观测偏差。CausalRM提供了一种严谨的数学框架来应对这些挑战，为改进化学领域的模型训练和数据利用提供了重要的技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite the success of reinforcement learning from human feedback (RLHF) in aligning language models, current reward modeling heavily relies on experimental feedback data collected from human annotators under controlled and costly conditions. In this work, we introduce observational reward modeling -- learning reward models with observational user feedback (e.g., clicks, copies, and upvotes) -- as a scalable and cost-effective alternative. We identify two fundamental challenges in this setting: (1) observational feedback is noisy due to annotation errors, which deviates it from true user preference; (2) observational feedback is biased by user preference, where users preferentially provide feedback on responses they feel strongly about, which creats a distribution shift between training and inference data. To address these challenges, we propose CausalRM, a causal-theoretic reward modeling framework that aims to learn unbiased reward models from observational feedback. To tackle challenge (1), CausalRM introduces a noise-aware surrogate loss term that is provably equivalent to the primal loss under noise-free conditions by explicitly modeling the annotation error generation process. To tackle challenge (2), CausalRM uses propensity scores -- the probability of a user providing feedback for a given response -- to reweight training samples, yielding a loss function that eliminates user preference bias. Extensive experiments across diverse LLM backbones and benchmark datasets validate that CausalRM effectively learns accurate reward signals from noisy and biased observational feedback and delivers substantial performance improvements on downstream RLHF tasks -- including a 49.2% gain on WildGuardMix and a 32.7% improvement on HarmBench. Code is available on our project website.

</details>

---

### 31. [dTRPO: Trajectory Reduction in Policy Optimization of Diffusion Large Language Models](https://arxiv.org/abs/2603.18806)

**基本信息**

- 🔗 arXiv: [`2603.18806`](https://arxiv.org/abs/2603.18806)
- 👥 作者: Wenxuan Zhang, Lemeng Wu, Changsheng Zhao 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散大语言模型（dLLMs）的策略优化，这属于生成式大模型的一种。其提出的dTRPO方法旨在改进这类模型的生成质量和效率，与“化学大模型”主题中利用生成模型进行化学任务（如分子生成、性质预测）的研究直接相关。

**📖 中文摘要**

本文提出了一种名为dTRPO（轨迹缩减策略优化）的新方法，旨在改进扩散大语言模型（dLLMs）的策略优化。论文的核心是解决dLLMs与人类偏好对齐的挑战，通过理论证明和算法设计，显著降低了轨迹概率计算的开销，从而实现了可扩展的离线策略训练。该方法在指令跟随和推理基准测试中，显著提升了dLLMs的核心性能（例如在STEM任务上提升高达9.6%）。虽然论文主要关注语言模型，但其核心方法——对扩散模型（一种生成模型）进行策略优化以改进其输出——与“化学大模型”主题中利用生成模型（如扩散模型）进行分子设计或性质预测的研究范式高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion Large Language Models (dLLMs) introduce a new paradigm for language generation, which in turn presents new challenges for aligning them with human preferences. In this work, we aim to improve the policy optimization for dLLMs by reducing the cost of the trajectory probability calculation, thereby enabling scaled-up offline policy training. We prove that: (i) under reference policy regularization, the probability ratio of the newly unmasked tokens is an unbiased estimate of that of intermediate diffusion states, and (ii) the probability of the full trajectory can be effectively estimated with a single forward pass of a re-masked final state. By integrating these two trajectory reduction strategies into a policy optimization objective, we propose Trajectory Reduction Policy Optimization (dTRPO). We evaluate dTRPO on 7B dLLMs across instruction-following and reasoning benchmarks. Results show that it substantially improves the core performance of state-of-the-art dLLMs, achieving gains of up to 9.6% on STEM tasks, up to 4.3% on coding tasks, and up to 3.0% on instruction-following tasks. Moreover, dTRPO exhibits strong training efficiency due to its offline, single-forward nature, and achieves improved generation efficiency through high-quality outputs.

</details>

---

### 32. [Seasoning Generative Models for a Generalization Aftertaste](https://arxiv.org/abs/2603.18817)

**基本信息**

- 🔗 arXiv: [`2603.18817`](https://arxiv.org/abs/2603.18817)
- 👥 作者: Hisham Husain, Valentin De Bortoli, Richard Nock
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18817.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于生成模型（包括扩散模型）的泛化理论和方法改进。虽然未直接应用于化学领域，但其研究的生成模型精炼和泛化理论是构建和优化“化学大模型”（尤其是基于扩散模型的分子生成器）的重要理论基础。

**📖 中文摘要**

本文探讨了使用判别器来训练或微调生成模型的理论框架。论文扩展了与f-散度相关的强对偶性结果，提出了一种判别器引导的通用方法，可以用于“精炼”任何生成模型。作者证明，经过这种精炼的生成模型在泛化能力上相比其未精炼的版本有可证明的提升。论文的分析揭示了泛化能力的提升基于用于精炼的判别器集合的Rademacher复杂度。该工作为包括基于分数的扩散方法在内的现有经验成功方法提供了理论验证。这为理解和改进生成模型（包括扩散模型）的泛化性能提供了理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The use of discriminators to train or fine-tune generative models has proven to be a rather successful framework. A notable example is Generative Adversarial Networks (GANs) that minimize a loss incurred by training discriminators along with other paradigms that boost generative models via discriminators that satisfy weak learner constraints. More recently, even diffusion models have shown advantages with some kind of discriminator guidance. In this work, we extend a strong-duality result related to $f$-divergences which gives rise to a discriminator-guided recipe that allows us to \textit{refine} any generative model. We then show that the refined generative models provably improve generalization, compared to its non-refined counterpart. In particular, our analysis reveals that the gap in generalization is improved based on the Rademacher complexity of the discriminator set used for refinement. Our recipe subsumes a recently introduced score-based diffusion approach (Kim et al., 2022) that has shown great empirical success, however allows us to shed light on the generalization guarantees of this method by virtue of our analysis. Thus, our work provides a theoretical validation for existing work, suggests avenues for new algorithms, and contributes to our understanding of generalization in generative models at large.

</details>

---

### 33. [Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827)

**基本信息**

- 🔗 arXiv: [`2603.18827`](https://arxiv.org/abs/2603.18827)
- 👥 作者: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于预测的机器学习模型集成框架。虽然应用于金融领域，但其方法论——集成多种模型、优化超参数、特征分析——与构建用于化学信息学预测任务（如分子性质预测、活性分类）的“化学大模型”或模型集成策略在技术路线上高度相关。

**📖 中文摘要**

本文提出了一种优化的贪婪加权集成框架，用于金融贷款违约预测。该框架集成了多种机器学习分类器（如LightGBM、XGBoost等），首先使用粒子群优化算法优化超参数，然后通过正则化贪婪加权机制和基于神经网络的元学习器（堆叠集成）来组合模型预测。在Lending Club数据集上的实验表明，该框架相比单一分类器提升了预测性能。特征分析使用递归特征消除法识别出最具影响力的预测因子。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An investigation, from a gender perspective, of how students view the ethical implications and societal effects of artificial intelligence is conducted, examining concepts that could have a big influence on how artificial intelligence may be taught in the future. For this, we conducted a survey on a cohort of 230 second year computer science students to reveal their opinions. The results revealed that AI, from the students' perspective, will significantly impact daily life, particularly in areas such as medicine, education, or media. Men are more aware of potential changes in Computer Science, autonomous driving, image and video processing, and chatbot usage, while women mention more the impact on social media. Both men and women perceive potential threats in the same manner, with men more aware of war, AI controlled drones, terrain recognition, and information war. Women seem to have a stronger tendency towards ethical considerations and helping others.

</details>

---

### 34. [Statistical Characteristic-Guided Denoising for Rapid High-Resolution Transmission Electron Microscopy Imaging](https://arxiv.org/abs/2603.18834)

**基本信息**

- 🔗 arXiv: [`2603.18834`](https://arxiv.org/abs/2603.18834)
- 👥 作者: Hesong Li, Ziqi Wu, Ruiwen Shao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18834.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门针对HRTEM成像的去噪方法和生成的数据集。虽然主要应用于材料科学成像，但HRTEM是分析材料结构（包括一些化学物质）的关键工具。其提出的去噪方法和数据集可作为“质谱结构推理”或更广泛的“光谱/谱图分析”领域的有价值资源或工具，因为处理噪声、从复杂信号中提取清晰结构信息是这些领域的共同挑战。

**📖 中文摘要**

本文提出了一种统计特征引导的去噪网络，用于快速高分辨率透射电子显微镜（HRTEM）成像。该方法利用统计特征在空间域和频域引导去噪过程，以解决原子尺度成核动力学观测中因快速成像导致的严重噪声问题。论文还开发了一种HRTEM专用的噪声校准方法，并生成了一个包含无序结构和真实HRTEM图像噪声的数据集，以确保模型在真实图像上的去噪性能。实验表明，该方法在HRTEM图像去噪和下游定位任务中优于现有技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

High-Resolution Transmission Electron Microscopy (HRTEM) enables atomic-scale observation of nucleation dynamics, which boosts the studies of advanced solid materials. Nonetheless, due to the millisecond-scale rapid change of nucleation, it requires short-exposure rapid imaging, leading to severe noise that obscures atomic positions. In this work, we propose a statistical characteristic-guided denoising network, which utilizes statistical characteristics to guide the denoising process in both spatial and frequency domains. In the spatial domain, we present spatial deviation-guided weighting to select appropriate convolution operations for each spatial position based on deviation characteristic. In the frequency domain, we present frequency band-guided weighting to enhance signals and suppress noise based on band characteristics. We also develop an HRTEM-specific noise calibration method and generate a dataset with disordered structures and realistic HRTEM image noises. It can ensure the denoising performance of models on real images for nucleation observation. Experiments on synthetic and real data show our method outperforms the state-of-the-art methods in HRTEM image denoising, with effectiveness in the localization downstream task. Code will be available at this https URL .

</details>

---

### 35. [Pore-scale modeling of capillary-driven binder migration during battery electrode drying](https://arxiv.org/abs/2603.18860)

**基本信息**

- 🔗 arXiv: [`2603.18860`](https://arxiv.org/abs/2603.18860)
- 👥 作者: Marcel Weichel, Martin Reder, Gerit Mühlberg 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18860.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用计算模型（孔隙尺度连续体模型）模拟电池电极制造过程中的化学物理过程（粘结剂迁移）。这属于计算化学和材料模拟的范畴，与利用“化学大模型”或计算模型来理解和优化化学材料制备过程的研究主题相关。

**📖 中文摘要**

本文提出了一个孔隙尺度连续体模型，用于模拟钠离子电池硬碳电极干燥过程中毛细管驱动的粘结剂迁移。该模型明确描述了孔隙排空过程中的毛细管驱动传输，并应用于具有不同平均粒径的硬碳微观结构。模拟揭示了颗粒尺寸、蒸发速率和表面张力等因素对粘结剂分布均匀性的影响。该工作强调了显式描述毛细管传输和微观结构效应对于准确预测粘结剂迁移的重要性，为优化电极干燥工艺提供了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sodium-ion batteries employing hard carbon electrodes are considered a drop-in technology for lithium-ion batteries. Electrode drying is a critical manufacturing step, as binder migration during pore emptying impacts the mechanical integrity and electrical performance of the electrode. Existing modeling approaches predominantly rely on the film shrinkage phase in a one dimensional way or neglect the capillary transport, resulting in a lack of physically consistent microstructure resolved predictions of binder migration. In this work, a spatially resolved pore scale continuum model is extended to explicitly describe capillary driven binder transport during pore emptying. The model is applied to hard carbon microstructures with varying mean particle diameters. The simulations reveal that smaller particle sizes lead to a more homogeneous binder distribution, whereas higher evaporation rates and increased surface tension promote stronger binder gradients. Variations in solvent viscosity show only a minor influence on binder migration, as long as no hydrophilic or hydrophobic behavior is present. Finally, the simulations demonstrate that an explicit description of capillary transport and microstructural effects is essential for accurately predicting binder migration and provides a basis for the targeted optimization of electrode drying processes.

</details>

---

### 36. [RadioDiff-FS: Physics-Informed Manifold Alignment in Few-Shot Diffusion Models for High-Fidelity Radio Map Construction](https://arxiv.org/abs/2603.18865)

**基本信息**

- 🔗 arXiv: [`2603.18865`](https://arxiv.org/abs/2603.18865)
- 👥 作者: Xiucheng Wang, Zixuan Guo, Nan Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18865.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于扩散模型的生成框架（RadioDiff-FS），用于生成复杂的物理场数据（无线电地图）。扩散模型是当前“化学大模型”中用于分子生成和谱图预测的重要技术之一。该工作展示了扩散模型在生成具有物理约束的结构化数据方面的应用，其方法论对构建用于“质谱结构推理”的生成模型具有参考价值。

**📖 中文摘要**

本文提出了RadioDiff-FS，一个基于扩散模型的少样本学习框架，用于高保真无线电地图（RM）构建。该框架将预训练的主路径生成器适配到多径丰富的目标域，仅需少量高保真样本。其理论依据是将多径RM分解为主导的主路径分量和方向稀疏的残差，并引入了方向一致性损失（DCL）来约束扩散分数沿着物理上合理的传播方向更新。实验表明，该方法在静态和动态RM上显著降低了归一化均方误差（NMSE）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Radio maps (RMs) provide spatially continuous propagation characterizations essential for 6G network planning, but high-fidelity RM construction remains challenging. Rigorous electromagnetic solvers incur prohibitive computational latency, while data-driven models demand massive labeled datasets and generalize poorly from simplified simulations to complex multipath environments. This paper proposes RadioDiff-FS, a few-shot diffusion framework that adapts a pre-trained main-path generator to multipath-rich target domains with only a small number of high-fidelity samples. The adaptation is grounded in a theoretical decomposition of the multipath RM into a dominant main-path component and a directionally sparse residual. This decomposition shows that the cross-domain shift corresponds to a bounded and geometrically structured feature translation rather than an arbitrary distribution change. A Direction-Consistency Loss (DCL) is then introduced to constrain diffusion score updates along physically plausible propagation directions, suppressing phase-inconsistent artifacts that arise in the low-data regime. Experiments show that RadioDiff-FS reduces NMSE by 59.5% on static RMs and by 74.0% on dynamic RMs relative to the vanilla diffusion baseline, achieving an SSIM of 0.9752 and a PSNR of 36.37 dB under severely limited supervision.

</details>

---

### 37. [MultihopSpatial: Multi-hop Compositional Spatial Reasoning Benchmark for Vision-Language Model](https://arxiv.org/abs/2603.18892)

**基本信息**

- 🔗 arXiv: [`2603.18892`](https://arxiv.org/abs/2603.18892)
- 👥 作者: Youngwan Lee, Soojin Jang, Yoorhim Cho 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18892.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于评估和训练视觉-语言模型空间推理能力的基准（MultihopSpatial）和训练语料库（MultihopSpatial-Train）。虽然应用于视觉领域，但其核心——构建复杂推理任务的数据集和评估框架——与开发用于“化学大模型”或“质谱结构推理”的评估基准和方法论在理念上相通，都是为AI模型在特定领域的复杂推理能力提供数据和测试标准。

**📖 中文摘要**

本文提出了MultihopSpatial，一个用于评估视觉-语言模型（VLMs）多跳组合空间推理能力的综合基准。该基准包含1至3跳的复杂查询，并引入了Acc@50IoU指标，同时评估推理能力和精确的视觉定位（边界框预测）。此外，论文还提供了MultihopSpatial-Train，一个用于培养空间智能的大规模训练语料库。对37个最先进VLM的评估表明，组合空间推理仍然是一个巨大的挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Spatial reasoning is foundational for Vision-Language Models (VLMs), particularly when deployed as Vision-Language-Action (VLA) agents in physical environments. However, existing benchmarks predominantly focus on elementary, single-hop relations, neglecting the multi-hop compositional reasoning and precise visual grounding essential for real-world scenarios. To address this, we introduce MultihopSpatial, offering three key contributions: (1) A comprehensive benchmark designed for multi-hop and compositional spatial reasoning, featuring 1- to 3-hop complex queries across diverse spatial perspectives. (2) Acc@50IoU, a complementary metric that simultaneously evaluates reasoning and visual grounding by requiring both answer selection and precise bounding box prediction - capabilities vital for robust VLA deployment. (3) MultihopSpatial-Train, a dedicated large-scale training corpus to foster spatial intelligence. Extensive evaluation of 37 state-of-the-art VLMs yields eight key insights, revealing that compositional spatial reasoning remains a formidable challenge. Finally, we demonstrate that reinforcement learning post-training on our corpus enhances both intrinsic VLM spatial reasoning and downstream embodied manipulation performance.

</details>

---

### 38. [Translating MRI to PET through Conditional Diffusion Models with Enhanced Pathology Awareness](https://arxiv.org/abs/2603.18896)

**基本信息**

- 🔗 arXiv: [`2603.18896`](https://arxiv.org/abs/2603.18896)
- 👥 作者: Yitong Li, Igor Yakushev, Dennis M. Hedderich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18896.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于条件扩散模型的跨模态医学图像生成框架（PASTA）。扩散模型是生成式AI和“化学大模型”中的关键技术。该工作展示了如何利用扩散模型从一种模态数据（MRI）生成另一种富含化学/功能信息的模态数据（PET），这种“从A推理B”的模式与“质谱结构推理”（从质谱数据推理分子结构）在问题形式上高度相似，都是基于某种信号/数据生成或推断出具有丰富化学信息的结构/图像。

**📖 中文摘要**

本文提出了PASTA，一个基于条件扩散模型的新型图像翻译框架，用于从磁共振成像（MRI）生成合成正电子发射断层扫描（PET）图像，特别增强了其对病理信息的感知能力。PASTA通过其高度交互的双臂架构和多模态条件集成，保留了结构和病理细节。此外，引入了循环交换一致性和体积生成策略，显著提升了生成高质量3D PET图像的能力。定性和定量结果表明，合成的PET扫描具有高质量和病理感知能力，用于阿尔茨海默病诊断时，其性能比MRI提升了4%，几乎达到真实PET的水平。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a widely recognized technique for diagnosing neurodegenerative diseases, offering critical functional insights. However, its high costs and radiation exposure hinder its widespread use. In contrast, magnetic resonance imaging (MRI) does not involve such limitations. While MRI also detects neurodegenerative changes, it is less sensitive for diagnosis compared to PET. To overcome such limitations, one approach is to generate synthetic PET from MRI. Recent advances in generative models have paved the way for cross-modality medical image translation; however, existing methods largely emphasize structural preservation while neglecting the critical need for pathology awareness. To address this gap, we propose PASTA, a novel image translation framework built on conditional diffusion models with enhanced pathology awareness. PASTA surpasses state-of-the-art methods by preserving both structural and pathological details through its highly interactive dual-arm architecture and multi-modal condition integration. Additionally, we introduce a novel cycle exchange consistency and volumetric generation strategy that significantly enhances PASTA's ability to produce high-quality 3D PET images. Our qualitative and quantitative results demonstrate the high quality and pathology awareness of the synthesized PET scans. For Alzheimer's diagnosis, the performance of these synthesized scans improves over MRI by 4%, almost reaching the performance of actual PET. Our code is available at this https URL .

</details>

---

### 39. [Neural Galerkin Normalizing Flow for Transition Probability Density Functions of Diffusion Models](https://arxiv.org/abs/2603.18907)

**基本信息**

- 🔗 arXiv: [`2603.18907`](https://arxiv.org/abs/2603.18907)
- 👥 作者: Riccardo Saporiti, Fabio Nobile
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18907.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于归一化流（一种生成模型）和神经伽辽金方法的框架，用于求解描述扩散过程的Fokker-Planck方程并近似其转移概率密度。归一化流是生成模型的一种，常用于密度估计和生成。该工作将生成模型（归一化流）与物理方程求解相结合，属于科学机器学习（AI for Science）的范畴，与利用“化学大模型”解决化学动力学、分子模拟等问题的研究范式直接相关。

**📖 中文摘要**

本文提出了一种新的神经伽辽金归一化流框架，用于近似参数化初始质量位置的扩散过程的转移概率密度函数（通过求解相应的Fokker-Planck方程）。该框架通过使用归一化流，将解表示为参考随机过程转移概率密度函数的变换，从而确保近似是结构保持的，并自动满足正性和质量守恒约束。通过将神经伽辽金方案扩展到归一化流的背景中，推导出了归一流参数时间演化的常微分方程组。自适应采样用于在有意义的位置评估Fokker-Planck残差。该方法可作为随机微分方程相关许多查询问题（如贝叶斯推断、模拟）的有前途的代理模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Neural Galerkin Normalizing Flow framework to approximate the transition probability density function of a diffusion process by solving the corresponding Fokker-Planck equation with an atomic initial distribution, parametrically with respect to the location of the initial mass. By using Normalizing Flows, we look for the solution as a transformation of the transition probability density function of a reference stochastic process, ensuring that our approximation is structure-preserving and automatically satisfies positivity and mass conservation constraints. By extending Neural Galerkin schemes to the context of Normalizing Flows, we derive a system of ODEs for the time evolution of the Normalizing Flow's parameters. Adaptive sampling routines are used to evaluate the Fokker-Planck residual in meaningful locations, which is of vital importance to address high-dimensional PDEs. Numerical results show that this strategy captures key features of the true solution and enforces the causal relationship between the initial datum and the density function at subsequent times. After completing an offline training phase, online evaluation becomes significantly more cost-effective than solving the PDE from scratch. The proposed method serves as a promising surrogate model, which could be deployed in many-query problems associated with stochastic differential equations, like Bayesian inference, simulation, and diffusion bridge generation.

</details>

---

### 40. [Theoretical Analyses of Detectors for Additive Noise Channels with Mean-Variance Uncertainty under Nonlinear Expectation Theory](https://arxiv.org/abs/2603.18937)

**基本信息**

- 🔗 arXiv: [`2603.18937`](https://arxiv.org/abs/2603.18937)
- 👥 作者: Wen-Xuan Lang, Guiying Yan, Zhi-Ming Ma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18937.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是在模型不确定性下，为加性噪声信道开发最优检测器。虽然应用于通信领域，但其处理信号、噪声和不确定性的数学框架与“质谱结构推理”中从噪声质谱数据中检测和识别分子信号（即“检测”分子结构）所面临的核心挑战在本质上相似。两者都需要在噪声和模型不确定性的条件下进行最优决策或推断。

**📖 中文摘要**

本文在非线性期望理论下，将加性噪声信道检测器的分析扩展到概率模型不确定的情况。论文考虑了两种分布不确定性：一种具有均值不确定性但具有方差不确定性，另一种同时具有均值和方差不确定性。推导了在这两种场景下，二元输入加性噪声信道在非线性期望最优准则下的最优检测器，并给出了其显式形式。研究发现，均值不确定性显著影响最优检测器的形式，而方差不确定性则不影响。此外，提出了一种信道噪声不确定参数的估计方法。最后，给出了新推导的最优检测器的理论分析和模拟性能结果，并与基于确定性概率模型的经典信息论最优检测器性能进行了比较。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In classical information theory, both the form and performance of the optimal detector for additive noise channels can be precisely derived, based on the assumption that the channel noise follows a specific probability distribution or a mixture of known distributions, or that the exact distribution exists but is unknown. In this paper, we extend the analyses of detectors for additive noise channel to the situation where the probability model for analyzing channels is uncertain, utilizing nonlinear expectation theory. We consider two types of distribution uncertainties: one with no mean uncertainty but with variance uncertainty, and another with both mean and variance uncertainties. We derive the optimal detectors for binary input additive noise channel under the nonlinear expectation optimal criterion for both scenarios and provide their explicit forms. Our findings reveal that mean uncertainty significantly influences the form of the optimal detector, whereas variance uncertainty does not. Additionally, we propose an estimation method for the uncertain parameters of the channel noise. Finally, we present theoretical analyses and simulated performance results of the newly derived optimal detectors, and compare these results with the performance of optimal detector under classical information theory, which assumes a deterministic probability model. The results of experiments show that our new detection methods outperform conventional methods in most scenarios with uncertain probability models, showing the practical relevance of our theoretical contributions.

</details>

---

### 41. [BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery](https://arxiv.org/abs/2603.18957)

**基本信息**

- 🔗 arXiv: [`2603.18957`](https://arxiv.org/abs/2603.18957)
- 👥 作者: Sijian Fan, Liyan Xiong, Dayuan Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18957.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的机器学习模型（BVSIMC），用于药物发现中的预测任务（耐药性预测、药物-疾病关联预测），并集成了侧边特征（化学性质、基因组信息）和变量选择。这直接属于“化学信息学”和“AI辅助药物发现”领域，是构建用于化学和生物医学预测的“化学大模型”或预测模型的具体实践。

**📖 中文摘要**

本文提出了BVSIMC（贝叶斯变量选择引导的归纳矩阵补全），一种新的贝叶斯模型，用于在药物发现中从侧边特征（如药物的化学性质和疾病的基因组信息）进行变量选择。通过学习稀疏的潜在嵌入，BVSIMC提高了预测准确性和可解释性。通过模拟研究和两个药物发现应用验证了该方法：1) 预测结核分枝杆菌的耐药性，2) 预测计算药物重定位中的新药-疾病关联。在合成和真实数据上，BVSIMC在预测方面优于其他几种最先进的方法。在两个真实例子中，BVSIMC进一步揭示了最具临床意义的侧边特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in drug discovery have demonstrated that incorporating side information (e.g., chemical properties about drugs and genomic information about diseases) often greatly improves prediction performance. However, these side features can vary widely in relevance and are often noisy and high-dimensional. We propose Bayesian Variable Selection-Guided Inductive Matrix Completion (BVSIMC), a new Bayesian model that enables variable selection from side features in drug discovery. By learning sparse latent embeddings, BVSIMC improves both predictive accuracy and interpretability. We validate our method through simulation studies and two drug discovery applications: 1) prediction of drug resistance in Mycobacterium tuberculosis, and 2) prediction of new drug-disease associations in computational drug repositioning. On both synthetic and real data, BVSIMC outperforms several other state-of-the-art methods in terms of prediction. In our two real examples, BVSIMC further reveals the most clinically meaningful side features.

</details>

---

### 42. [CRAFT: Aligning Diffusion Models with Fine-Tuning Is Easier Than You Think](https://arxiv.org/abs/2603.18991)

**基本信息**

- 🔗 arXiv: [`2603.18991`](https://arxiv.org/abs/2603.18991)
- 👥 作者: Zening Sun, Zhengpeng Xie, Lichen Bai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18991.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对扩散模型（一种重要的生成模型）提出了一种新的、高效的微调对齐方法（CRAFT）。扩散模型是“化学大模型”中用于分子生成和性质预测的关键技术之一。改进扩散模型的微调效率和质量，直接有助于构建更优的化学领域生成模型。

**📖 中文摘要**

本文提出了CRAFT（复合奖励辅助微调），一种轻量级但强大的扩散模型微调范式。它首先利用复合奖励过滤（CRF）技术构建高质量且一致的训练数据集，然后执行增强版的监督微调（SFT）。论文还从理论上证明，CRAFT实际上优化了基于组的强化学习的下界，从而在选定数据的SFT和强化学习之间建立了原则性的联系。大量实验结果表明，仅使用100个样本的CRAFT可以轻松超越使用数千个偏好配对样本的最新偏好优化方法，并且收敛速度比基线偏好优化方法快11-220倍。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Aligning Diffusion models has achieved remarkable breakthroughs in generating high-quality, human preference-aligned images. Existing techniques, such as supervised fine-tuning (SFT) and DPO-style preference optimization, have become principled tools for fine-tuning diffusion models. However, SFT relies on high-quality images that are costly to obtain, while DPO-style methods depend on large-scale preference datasets, which are often inconsistent in quality. Beyond data dependency, these methods are further constrained by computational inefficiency. To address these two challenges, we propose Composite Reward Assisted Fine-Tuning (CRAFT), a lightweight yet powerful fine-tuning paradigm that requires significantly reduced training data while maintaining computational efficiency. It first leverages a Composite Reward Filtering (CRF) technique to construct a high-quality and consistent training dataset and then perform an enhanced variant of SFT. We also theoretically prove that CRAFT actually optimizes the lower bound of group-based reinforcement learning, establishing a principled connection between SFT with selected data and reinforcement learning. Our extensive empirical results demonstrate that CRAFT with only 100 samples can easily outperform recent SOTA preference optimization methods with thousands of preference-paired samples. Moreover, CRAFT can even achieve 11-220$\times$ faster convergences than the baseline preference optimization methods, highlighting its extremely high efficiency.

</details>

---

### 43. [Foundations of Schrödinger Bridges for Generative Modeling](https://arxiv.org/abs/2603.18992)

**基本信息**

- 🔗 arXiv: [`2603.18992`](https://arxiv.org/abs/2603.18992)
- 👥 作者: Sophia Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18992.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于薛定谔桥数学基础及其与生成模型（包括扩散模型）联系的系统性阐述。薛定谔桥是理解扩散模型等生成模型的理论基础之一。因此，这篇论文属于针对生成模型（“化学大模型”的核心技术之一）的理论综述和展望，提供了重要的相关讨论和理论基础。

**📖 中文摘要**

本文系统性地阐述了薛定谔桥问题的数学基础，并将其与现代生成建模（包括扩散模型、基于分数的模型和流匹配）联系起来。薛定谔桥为这些方法提供了一个统一的原则，将问题框架化为在边际分布约束下确定一个最优的随机桥，使其与预定义的参考过程的熵偏差最小。论文从最优传输、随机控制和路径空间优化等角度出发，重点介绍了其动态公式及其与现代生成建模的直接联系，并构建了一个从第一性原理构建薛定谔桥的综合工具包。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

At the core of modern generative modeling frameworks, including diffusion models, score-based models, and flow matching, is the task of transforming a simple prior distribution into a complex target distribution through stochastic paths in probability space. Schrödinger bridges provide a unifying principle underlying these approaches, framing the problem as determining an optimal stochastic bridge between marginal distribution constraints with minimal-entropy deviations from a pre-defined reference process. This guide develops the mathematical foundations of the Schrödinger bridge problem, drawing on optimal transport, stochastic control, and path-space optimization, and focuses on its dynamic formulation with direct connections to modern generative modeling. We build a comprehensive toolkit for constructing Schrödinger bridges from first principles, and show how these constructions give rise to generalized and task-specific computational methods.

</details>

---

### 44. [SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141)

**基本信息**

- 🔗 arXiv: [`2603.19141`](https://arxiv.org/abs/2603.19141)
- 👥 作者: Mingxing Zhang, Nicola Rossberg, Simone Innocente 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19141.pdf)

**💡 相关性分析**

满足标准2：论文提出的SHAPCA框架专门用于处理和分析光谱数据（如化学或生物医学光谱），这是一种典型的化学信息学数据类型。该框架提供了从高维光谱数据中提取稳定、可解释特征的工具和方法，这些工具和方法可直接应用于化学信息学领域，用于构建和理解基于机器学习的化学分析模型。

**📖 中文摘要**

本文提出了一种名为SHAPCA的可解释机器学习流程，用于处理高维、强共线性的光谱数据（如化学或生物医学光谱）。该流程结合了主成分分析（PCA）进行降维和SHAP（Shapley Additive exPlanations）进行事后解释，旨在为模型预测提供稳定、一致且可解释的特征重要性分析。SHAPCA能够将解释映射回原始输入空间（即光谱波段），使研究人员和从业者能够将模型决策与潜在的生物或化学组分联系起来。该研究通过数值分析证明了该方法在多次运行中具有更高的解释一致性和稳定性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

</details>

---

### 45. [Generative Replica-Exchange: A Flow-based Framework for Accelerating Replica Exchange Simulations](https://arxiv.org/abs/2603.18076)

**基本信息**

- 🔗 arXiv: [`2603.18076`](https://arxiv.org/abs/2603.18076)
- 👥 作者: Shengjie Huang, Sijie Yang, Jianqiao Yi 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18076.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕开发一种用于加速分子模拟的生成模型（GREX），这直接属于“化学大模型”主题，旨在解决计算化学中的采样挑战。

**📖 中文摘要**

本文提出了生成式副本交换（GREX），这是一种将深度生成模型（特别是归一化流）集成到副本交换（REX）模拟框架中的新方法。GREX旨在通过消除对大量中间温度副本的需求来加速分子模拟。该方法利用训练好的归一化流按需生成高温构型，并使用势能作为约束将其直接映射到目标分布。这项工作与化学信息学中开发用于加速分子模拟和采样的新型生成模型（化学大模型）高度相关。它展示了一个将生成式AI与物理驱动模拟相结合的框架，可用于探索分子构象空间和自由能景观。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Replica exchange (REX) is one of the most widely used enhanced sampling methodologies, yet its efficiency is limited by the requirement for a large number of intermediate temperature replicas. Here we present Generative Replica Exchange (GREX), which integrates deep generative models into the REX framework to eliminate this temperature ladder. Drawing inspiration from reservoir replica exchange (res-REX), GREX utilizes trained normalizing flows to generate high-temperature configurations on demand and map them directly to the target distribution using the potential energy as a constraint, without requiring target-temperature training data. This approach reduces production simulations to a single replica at the target temperature while maintaining thermodynamic rigor through Metropolis exchange acceptance. We validate GREX on three benchmark systems of increasing complexity, highlighting its superior efficiency and practical applicability for molecular simulations.

</details>

---

### 46. [Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows](https://arxiv.org/abs/2603.18205)

**基本信息**

- 🔗 arXiv: [`2603.18205`](https://arxiv.org/abs/2603.18205)
- 👥 作者: Dominic Schuh, Lena Funcke, Janik Kreit 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用归一化流（一种生成模型/化学大模型）来解决量子化学和凝聚态物理中一个基础且具有挑战性的问题（哈伯德模型的符号问题），属于化学大模型在基础科学计算中的应用。

**📖 中文摘要**

本文解决了掺杂哈伯德模型在有限化学势下的符号问题，这是理解掺杂相关系统的基石。作者扩展了在零掺杂（半填充）情况下使用归一化流的最新进展，通过引入退火方案实现对有限化学势情况的遍历采样。与在电荷基中使用的混合蒙特卡罗方法相比，该方法在减少统计不确定性的同时，能准确再现精确对角化结果。这项工作展示了归一化流（一种生成模型）在解决量子多体物理中关键计算瓶颈方面的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hubbard model at finite chemical potential is a cornerstone for understanding doped correlated systems, but simulations are severely limited by the sign problem. In the auxiliary-field formulation, the spin basis mitigates the sign problem, yet severe ergodicity issues have limited its use. We extend recent advances with normalizing flows at half-filling to finite chemical potential by introducing an annealing scheme enabling ergodic sampling. Compared to state-of-the-art hybrid Monte Carlo in the charge basis, our approach accurately reproduces exact diagonalization results while reducing statistical uncertainties by an order of magnitude, opening a new path for simulations of doped correlated systems.

</details>

---

### 47. [A Hybrid Conditional Diffusion-DeepONet Framework for High-Fidelity Stress Prediction in Hyperelastic Materials](https://arxiv.org/abs/2603.18225)

**基本信息**

- 🔗 arXiv: [`2603.18225`](https://arxiv.org/abs/2603.18225)
- 👥 作者: Purna Vindhya Kota, Meer Mehran Rashid, Somdatta Goswami 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18225.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法依赖于条件扩散模型（cDDPM），这是一种生成模型，用于解决材料科学中的物理场预测问题。这属于生成模型（大模型）在科学计算和化学/材料建模中的应用范畴。

**📖 中文摘要**

本文提出了一种混合条件扩散-DeepONet框架（cDDPM-DeepONet），用于超弹性材料中高保真应力预测。该框架将应力形态与幅值解耦：一个基于UNet的条件去噪扩散概率模型（cDDPM）生成归一化的冯·米塞斯应力场，而一个改进的DeepONet预测全局缩放参数。这种方法允许扩散模型专注于空间结构，同时算子网络校正全局幅度，从而减轻光谱和缩放偏差。该工作展示了扩散模型（一种强大的生成模型）与神经算子相结合，用于解决具有复杂微观结构的材料中的物理场预测问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting stress fields in hyperelastic materials with complex microstructures remains challenging for traditional deep learning surrogates, which struggle to capture both sharp stress concentrations and the wide dynamic range of stress magnitudes. Convolutional architectures such as UNet tend to oversmooth high-frequency gradients, while neural operators like DeepONet exhibit spectral bias and underpredict localized extremes. Diffusion models can recover fine-scale structure but often introduce low-frequency amplitude drift, degrading physical scaling. To address these limitations, we propose a hybrid surrogate framework, cDDPM-DeepONet, that decouples stress morphology from magnitude. A conditional denoising diffusion probabilistic model (cDDPM), built on a UNet backbone, generates normalized von Mises stress fields conditioned on geometry and loading. In parallel, a modified DeepONet predicts global scaling parameters (minimum and maximum stress), enabling reconstruction of full-resolution physical stress maps. This separation allows the diffusion model to focus on spatial structure while the operator network corrects global amplitude, mitigating spectral and scaling biases. We evaluate the framework on nonlinear hyperelastic datasets with single and multiple polygonal voids. The proposed model consistently outperforms UNet, DeepONet, and standalone cDDPM baselines by one to two orders of magnitude. Spectral analysis shows strong agreement with finite element solutions across all wavenumbers, preserving both global behavior and localized stress concentrations.

</details>

---

### 48. [Nonlinear Incompressible Shear Wave Models in Hyperelasticity and Viscoelasticity Frameworks, with Applications to Love Waves](https://arxiv.org/abs/2603.18296)

**基本信息**

- 🔗 arXiv: [`2603.18296`](https://arxiv.org/abs/2603.18296)
- 👥 作者: Shawn Samuel Carl McAdam, Samuel Opoku Agyemang, Alexei Cheviakov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18296.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕为一大类材料（包括超粘弹性材料）建立通用的波传播模型。虽然不直接使用“大模型”，但其对材料本构关系的建模是计算化学和材料科学中物理信息模型的基础，与基于物理的化学信息学模型相关。

**📖 中文摘要**

本文提出了不可压缩超弹性材料中剪切位移的通用方程，并将其应用于描述在具有不同机械性能的材料界面上传播的非线性Love型波。该模型适用于一大类超粘弹性材料。对于三次Yeoh模型，剪切波方程包含三次和五次微分多项式项，以及以材料位移的混合导数项形式出现的粘弹性贡献。这项工作为理解和模拟复杂材料（如生物组织或聚合物）中的波传播提供了理论基础，这些材料的力学响应通常通过超弹性本构模型来描述。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General equations describing shear displacements in incompressible hyperelastic materials, holding for an arbitrary form of strain energy density function, are presented and applied to the description of nonlinear Love-type waves propagating on an interface between materials with different mechanical properties. The model is valid for a broad class of hyper-viscoelastic materials. For a cubic Yeoh model, shear wave equations contain cubic and quintic differential polynomial terms, including viscoelasticity contributions in terms of dispersion terms that include mixed derivatives $u_{xxt}$ of the material displacement. Full (2+1)-dimensional numerical simulations of waves propagating in the bulk of a two-layered solid are undertaken and analyzed with respect to the source position and mechanical properties of the layers. Interfacial nonlinear Love waves and free upper surface shear waves are tracked; it is demonstrated that in the fully nonlinear case, the variable wave speed of interface and surface waves generally satisfies the linear Love wave existence condition $c_1 < \abs{v} < c_2$, while tending to the larger material wave speed $c_1$ or $c_2$ for large times.

</details>

---

### 49. [An SO(3)-equivariant reciprocal-space neural potential for long-range interactions](https://arxiv.org/abs/2603.18389)

**基本信息**

- 🔗 arXiv: [`2603.18389`](https://arxiv.org/abs/2603.18389)
- 👥 作者: Linfeng Zhang, Taoyong Cui, Dongzhan Zhou 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的等变神经原子间势（EquiEwald），这是一种专门用于分子和材料模拟的机器学习模型（化学大模型）。它直接解决了当前模型在捕获长程相互作用方面的局限性，是化学大模型领域的前沿工作。

**📖 中文摘要**

本文介绍了EquiEwald，一种统一的神经原子间势，它将受Ewald启发的倒空间公式嵌入到不可约SO(3)等变框架中。通过学习的等变k空间滤波器和等变逆变换在倒空间中进行等变消息传递，EquiEwald能够捕获各向异性、张量化的长程关联，同时不牺牲物理一致性。在周期性和非周期性基准测试中，EquiEwald捕获了与从头算参考数据一致的长程静电行为，并持续提高了能量和力的准确性、数据效率以及长程外推能力。这项工作代表了机器学习原子间势（MLIPs）发展的一个重要进步，MLIPs是化学信息学和计算材料科学中“化学大模型”的核心组成部分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Long-range electrostatic and polarization interactions play a central role in molecular and condensed-phase systems, yet remain fundamentally incompatible with locality-based machine-learning interatomic potentials. Although modern SO(3)-equivariant neural potentials achieve high accuracy for short-range chemistry, they cannot represent the anisotropic, slowly decaying multipolar correlations governing realistic materials, while existing long-range extensions either break SO(3) equivariance or fail to maintain energy-force consistency. Here we introduce EquiEwald, a unified neural interatomic potential that embeds an Ewald-inspired reciprocal-space formulation within an irreducible SO(3)-equivariant framework. By performing equivariant message passing in reciprocal space through learned equivariant k-space filters and an equivariant inverse transform, EquiEwald captures anisotropic, tensorial long-range correlations without sacrificing physical consistency. Across periodic and aperiodic benchmarks, EquiEwald captures long-range electrostatic behavior consistent with ab initio reference data and consistently improves energy and force accuracy, data efficiency, and long-range extrapolation. These results establish EquiEwald as a physically principled paradigm for long-range-capable machine-learning interatomic potentials.

</details>

---

### 50. [Multi-Domain Causal Empirical Bayes Under Linear Mixing](https://arxiv.org/abs/2603.18404)

**基本信息**

- 🔗 arXiv: [`2603.18404`](https://arxiv.org/abs/2603.18404)
- 👥 作者: Bohan Wu, Julius von Kügelgen, David M. Blei
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18404.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是因果表示学习，这是一种从观测数据中推断潜在变量（如分子结构或性质）之间因果关系的方法论。这与“质谱结构推理”中从质谱数据推断分子结构的逆问题在本质上相似，都是基于数据的结构推断。

**📖 中文摘要**

本文探讨了使用经验贝叶斯（EB）从多领域数据中估计因果表示。具体考虑了多个领域的数据，其中领域间的差异通过共享底层因果模型中的干预来建模。多领域因果表示学习自然提出了一个同时推理的问题，而经验贝叶斯正是为解决此类问题而设计的。作者提出了一种EB f-建模算法，通过利用领域内和领域间的不变结构来提高学习到的因果变量的质量。具体考虑了一个线性测量模型和由共享无环结构因果模型产生的干预先验。这项工作与从观测数据中推断分子结构或反应网络等化学信息学问题在方法论上相关，都属于从数据中学习因果关系的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Causal representation learning (CRL) aims to learn low-dimensional causal latent variables from high-dimensional observations. While identifiability has been extensively studied for CRL, estimation has been less explored. In this paper, we explore the use of empirical Bayes (EB) to estimate causal representations. In particular, we consider the problem of learning from data from multiple domains, where differences between domains are modeled by interventions in a shared underlying causal model. Multi-domain CRL naturally poses a simultaneous inference problem that EB is designed to tackle. Here, we propose an EB $f$-modeling algorithm that improves the quality of learned causal variables by exploiting invariant structure within and across domains. Specifically, we consider a linear measurement model and interventional priors arising from a shared acyclic SCM. When the graph and intervention targets are known, we develop an EM-style algorithm based on causally structured score matching. We further discuss EB $\rmg$-modeling in the context of existing CRL approaches. In experiments on synthetic data, our proposed method achieves more accurate estimation than other methods for CRL.

</details>

---

### 51. [Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement](https://arxiv.org/abs/2603.18497)

**基本信息**

- 🔗 arXiv: [`2603.18497`](https://arxiv.org/abs/2603.18497)
- 👥 作者: Quilee Simeon
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18497.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种从部分观测数据中推断网络（图）结构的方法。这与“质谱结构推理”的核心挑战——从质谱信号（部分观测）推断分子图结构（原子连接性）——在问题形式上高度相关，都属于基于数据的图结构逆推问题。

**📖 中文摘要**

本文提出了一种基于协方差的方法，用于从跨多个记录会话的稀疏、部分观测中估计递归神经网络的权重矩阵。通过积累不同神经元子集被观测到的会话间的成对协方差估计，可以在不需要同时记录所有神经元的情况下重建完整的连接矩阵。一个格兰杰因果细化步骤通过投影梯度下降强制执行生物学约束。这项工作为从神经活动数据中推断网络连接性提供了一个计算框架。虽然应用于神经科学，但其从部分、多会话观测中推断网络结构的核心方法论与从碎片化质谱数据（如MS/MS谱图）中推断分子连接性（化学结构）的问题具有概念上的相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inferring the connectivity of neural circuits from incomplete observations is a fundamental challenge in neuroscience. We present a covariance-based method for estimating the weight matrix of a recurrent neural network from sparse, partial measurements across multiple recording sessions. By accumulating pairwise covariance estimates across sessions where different subsets of neurons are observed, we reconstruct the full connectivity matrix without requiring simultaneous recording of all neurons. A Granger-causality refinement step enforces biological constraints via projected gradient descent. Through systematic experiments on synthetic networks modeling small brain circuits, we characterize a fundamental control-estimation tradeoff: stimulation aids identifiability but disrupts intrinsic dynamics, with the optimal level depending on measurement density. We discover that the ``incorrect'' linear approximation acts as implicit regularization -- outperforming the oracle estimator with known nonlinearity at all operating regimes -- and provide an exact characterization via the Stein--Price identity.

</details>

---

### 52. [End-to-End QGAN-Based Image Synthesis via Neural Noise Encoding and Intensity Calibration](https://arxiv.org/abs/2603.18554)

**基本信息**

- 🔗 arXiv: [`2603.18554`](https://arxiv.org/abs/2603.18554)
- 👥 作者: Xue Yang, Rigui Zhou, Shizheng Jia 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18554.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子生成对抗网络（QGAN），这是生成模型（大模型）在量子计算硬件上的实现。虽然应用是图像生成，但其框架和方法对将来开发用于分子或材料设计的量子化学大模型具有启发性。

**📖 中文摘要**

本文提出了ReQGAN，一个用于图像合成的端到端量子生成对抗网络框架。ReQGAN使用单个D量子电路合成整个N=2^D像素的图像，克服了阻碍直接像素生成的两个基本瓶颈：1）僵化的经典到量子噪声接口；2）归一化量子统计量与所需像素强度空间之间的输出失配。作者引入了可学习的神经噪声编码器用于自适应状态准备，以及可微强度校准模块以将测量结果映射到稳定、视觉有意义的像素域。这项工作代表了量子机器学习在生成建模方面的探索，是“化学大模型”在量子计算范式下的一个潜在实例，未来可能应用于生成分子结构或材料。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Generative Adversarial Networks (QGANs) offer a promising path for learning data distributions on near-term quantum devices. However, existing QGANs for image synthesis avoid direct full-image generation, relying on classical post-processing or patch-based methods. These approaches dilute the quantum generator's role and struggle to capture global image semantics. To address this, we propose ReQGAN, an end-to-end framework that synthesizes an entire N=2^D-pixel image using a single D-qubit quantum circuit. ReQGAN overcomes two fundamental bottlenecks hindering direct pixel generation: (1) the rigid classical-to-quantum noise interface and (2) the output mismatch between normalized quantum statistics and the desired pixel-intensity space. We introduce a learnable Neural Noise Encoder for adaptive state preparation and a differentiable Intensity Calibration module to map measurements to a stable, visually meaningful pixel domain. Experiments on MNIST and Fashion-MNIST demonstrate that ReQGAN achieves stable training and effective image synthesis under stringent qubit budgets, with ablation studies verifying the contribution of each component.

</details>

---

### 53. [DeePAW: A universal machine learning model for orbital-free ab initio calculations](https://arxiv.org/abs/2603.18650)

**基本信息**

- 🔗 arXiv: [`2603.18650`](https://arxiv.org/abs/2603.18650)
- 👥 作者: Tianhao Su, Shunbo Hu, Yue Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18650.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发DeePAW，一种用于无轨道密度泛函理论的通用机器学习势能模型。这是化学信息学和计算材料科学中“化学大模型”的典型代表，旨在用AI替代或加速传统的量子化学计算。

**📖 中文摘要**

本文提出了深度增强方式模型（DeePAW），这是一种用于无轨道（OF）从头算计算的通用机器学习模型，基于密度泛函理论（DFT）。DeePAW是目前最好的OFDFT ML模型，覆盖元素数量最多，对多样晶体结构的应用能力最广，并且在不进一步微调的情况下实现了最高的预测精度。DeePAW的科学优点和创新源于新颖的SE(3)-等变双消息传递神经网络。除了预测电子密度分布，DeePAW还能预测晶体的形成能。这项工作为多尺度材料建模开辟了一条超越传统电子结构计算方法的有效途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing universal machine learning models for ab initio calculations is the frontier of materials cutting edge research in the new era of artificial intelligence. Here, we present the Deep Augment Way model (DeePAW) that is a universal machine learning (ML) model for orbital-free (OF) ab initio calculations, based on the density functional theory (DFT). DeePAW is currently the best OFDFT ML model according to the three criterions, 1) covering the largest number of elements, 2) having the widest application capability to diverse crystal structures, and 3) achieving the highest prediction accuracy without further fine-tuning. These scientific merits and innovations of DeePAW are stemmed from the novel SE(3)-equivariant double massage passing neuron networks. Besides predicting electron density distributions, DeePAW predicts formation energies of crystals as well and therefore paves an efficient avenue for multiscale materials modeling beyond conventional electronic structure calculation methods.

</details>

---

### 54. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](https://arxiv.org/abs/2603.18864)

**基本信息**

- 🔗 arXiv: [`2603.18864`](https://arxiv.org/abs/2603.18864)
- 👥 作者: Samuel Del Fré, Gilberto A. Alou Angulo, Maurice Monnerville 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18864.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为气-表面散射系统开发机器学习原子间势（MLIP）。MLIP是化学大模型在分子动力学模拟中的关键应用。此外，其数据驱动的工作流程（描述符分析、主动学习）是构建高质量化学大模型的代表性方法。

**📖 中文摘要**

本文为气-表面散射动力学构建了一个数据驱动的工作流程，用于构建机器学习原子间势（MLIP），以一氧化氮（NO）在石墨上的散射作为基准系统。该工作流程从初始的从头算分子动力学数据集开始，使用SOAP描述符描述局部原子环境，并通过主成分分析在降维的特征空间中进行分析。然后使用最远点采样构建紧凑的训练集，并通过基于委员会的主动学习策略，利用从扩展入射能量和表面温度范围的分子动力学模拟中提取的额外构型来细化最终的深度势能模型。最终的MLIP以远低于AIMD的计算成本实现了大规模NO散射分子动力学模拟。这项工作展示了为气-表面相互作用构建MLIP的高效且可转移的策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate atomistic simulations of gas-surface scattering require potential energy surfaces that remain reliable over broad configurational and energetic ranges while retaining the efficiency needed for extensive trajectory sampling. Here, we develop a data-driven workflow for constructing a machine-learning interatomic potential (MLIP) tailored to gas-surface scattering dynamics, using nitric oxide (NO) scattering from highly oriented pyrolytic graphite (HOPG) as a benchmark system. Starting from an initial ab initio molecular dynamics (AIMD) dataset, local atomic environments are described by SOAP descriptors and analyzed in a reduced feature space obtained through principal component analysis. Farthest point sampling is then used to build a compact training set, and the resulting Deep Potential model is refined through a query-by-committee active-learning strategy using additional configurations extracted from molecular dynamics simulations over extended ranges of incident energies and surface temperatures. The final MLIP reproduces reference energies and forces with high fidelity and enables large-scale molecular dynamics simulations of NO scattering from graphite at a computational cost far below that of AIMD. The simulations provide detailed insight into adsorption energetics, trapping versus direct scattering probabilities, translational energy loss, angular distributions, and rotational excitation. Overall, the results reproduce the main experimental trends and demonstrate that descriptor-guided sampling combined with active learning offers an efficient and transferable strategy for constructing MLIPs for gas-surface interactions.

</details>

---

### 55. [Improving moment tensor solutions under Earth structure uncertainty with simulation-based inference](https://arxiv.org/abs/2603.18925)

**基本信息**

- 🔗 arXiv: [`2603.18925`](https://arxiv.org/abs/2603.18925)
- 👥 作者: A. A. Saoulis, T.-S. Pham, A. M. G. Ferreira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18925.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法是利用模拟推理（SBI）这一机器学习技术来解决地球物理学中的逆问题（矩张量反演）。这与“质谱结构推理”同属基于数据的逆问题求解范畴，方法论上具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian inference represents a principled way to incorporate Earth structure uncertainty in full-waveform moment tensor inversions, but traditional approaches generally require significant approximations that risk biasing the resulting solutions. We introduce a robust method for handling theory errors using simulation-based inference (SBI), a machine learning approach that empirically models their impact on the observations. This framework retains the rigour of Bayesian inference while avoiding restrictive assumptions about the functional form of the uncertainties. We begin by demonstrating that the common Gaussian parametrisation of theory errors breaks down under minor ($1-3 \%$) 1-D Earth model uncertainty. To address this issue, we develop two formalisms for utilising SBI to improve the quality of the moment tensor solutions: one using physics-based insights into the theory errors, and another utilising an end-to-end deep learning algorithm. We then compare the results of moment tensor inversion with the standard Gaussian approach and SBI, and demonstrate that Gaussian assumptions induce bias and significantly under-report moment tensor uncertainties. We also show that these effects are particularly problematic when inverting short period data and for shallow, isotropic events. On the other hand, SBI produces more reliable, better calibrated posteriors of the earthquake source mechanism. Finally, we successfully apply our methodology to two well studied moderate magnitude earthquakes: one from the 1997 Long Valley Caldera volcanic earthquake sequence, and the 2020 Zagreb earthquake.

</details>

---

### 56. [BSTModelKit.jl: A Julia Package for Constructing, Solving, and Analyzing Biochemical Systems Theory Models](https://arxiv.org/abs/2603.19115)

**基本信息**

- 🔗 arXiv: [`2603.19115`](https://arxiv.org/abs/2603.19115)
- 👥 作者: Sandra Vadhin, Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19115.pdf)

**💡 相关性分析**

满足标准2：论文介绍了一个用于构建和分析生化系统理论模型的软件包（BSTModelKit.jl）。这提供了可用于化学信息学和系统生物学研究的数据处理、模型构建和模拟工具，符合“数据资源相关”标准。

**📖 中文摘要**

本文介绍了BSTModelKit.jl，一个用于构建、求解和分析生化系统理论（BST）模型的开源Julia软件包。该包实现了S-system表示法，这是一种用于建模代谢和调控网络的规范幂律形式主义。BSTModelKit.jl提供了声明式模型规范格式、通过常微分方程（ODE）积分的动态模拟、稳态计算以及使用Morris和Sobol方法的全局敏感性分析。该软件包利用Julia科学计算生态系统，特别是SciML微分方程求解器套件，提供高效灵活的模型分析工具。生化系统理论模型是系统生物学中用于建模生化网络的一类重要模型，属于化学信息学中计算模型的一个分支。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present this http URL , an open-source Julia package for constructing, solving, and analyzing Biochemical Systems Theory (BST) models of biochemical networks. The package implements S-system representations, a canonical power-law formalism for modeling metabolic and regulatory networks. this http URL provides a declarative model specification format, dynamic simulation via ordinary differential equation (ODE) integration, steady-state computation, and global sensitivity analysis using the Morris and Sobol methods. The package leverages the Julia scientific computing ecosystem, in particular the SciML suite of differential equation solvers, to provide efficient and flexible model analysis tools. We describe the mathematical formulation, software design, and demonstrate the package capabilities with illustrative examples.

</details>

---

### 57. [Variational and Annealing-Based Approaches to Quantum Combinatorial Optimization](https://arxiv.org/abs/2603.19117)

**基本信息**

- 🔗 arXiv: [`2603.19117`](https://arxiv.org/abs/2603.19117)
- 👥 作者: Hala Hawashin, Deep Nath, Marco Alberto Javarone
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19117.pdf)

**💡 相关性分析**

满足标准3：论文是一篇综述/展望性文章，系统回顾了量子计算在组合优化中的应用，包括量子退火、QAOA、QRL和QGM等多种算法。这为化学信息学领域的研究者提供了关于如何利用新兴量子算法解决化学中优化问题的前瞻性视角和讨论。

**📖 中文摘要**

本文回顾了用于组合优化的量子方法，旨在连接理论发展和工业相关性。首先调查了主要的量子算法家族，包括量子退火、量子近似优化算法（QAOA）、量子强化学习（QRL）和量子生成建模（QGM）。然后检查了量子技术目前显示出量子优势证据的问题类别，并借鉴了QOBLIB、QUARK、QASMBench和QED-C等已建立的基准测试计划。这些工作展示了量子计算在解决优化问题方面的潜力，而优化问题在化学信息学中广泛存在，如分子构象搜索、反应路径优化和材料设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we review quantum approaches to combinatorial optimization, with the aim of bridging theoretical developments and industrial relevance. We first survey the main families of quantum algorithms, including Quantum Annealing, the Quantum Approximate Optimization Algorithm (QAOA), Quantum Reinforcement Learning (QRL), and Quantum Generative Modeling (QGM). We then examine the problem classes where quantum technologies currently show evidence of quantum advantage, drawing on established benchmarking initiatives such as QOBLIB, QUARK, QASMBench, and QED-C. These problem classes are subsequently mapped to representative industrial domains, including logistics, finance, and telecommunications. Our analysis indicates that quantum annealing currently exhibits the highest level of operational maturity, while QAOA shows promising potential on NISQ-era hardware. In contrast, QRL and QGM emerge as longer-term research directions with significant potential for future industrial impact.

</details>

---

### 58. [Quantum block encoding for semiseparable matrices](https://arxiv.org/abs/2603.19130)

**基本信息**

- 🔗 arXiv: [`2603.19130`](https://arxiv.org/abs/2603.19130)
- 👥 作者: Giacomo Antonioli, Paola Boito, Gianna M. Del Corso 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19130.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对特定结构矩阵（一对半可分矩阵）设计高效的量子块编码方案。量子块编码是实现量子线性代数算法（可用于量子机器学习、量子化学模拟等）的基础组件，属于支撑未来“化学大模型”在量子计算机上运行的底层技术。

**📖 中文摘要**

量子块编码（QBE）是大多数量子算法开发的关键步骤，因为它将给定矩阵嵌入到合适的更大酉矩阵中。历史上，高效QBE技术的发展主要集中在稀疏矩阵上；较少努力投入到数据稀疏（例如，秩结构）矩阵。在这项工作中，我们研究了一种特殊的秩结构情况，即一对半可分矩阵。我们提出了一种新的块编码方法，该方法依赖于将给定矩阵因式分解为三角因子和对角因子的乘积。为了编码矩阵，该算法需要2log(N)+7个辅助量子比特。这个过程需要多对数时间，并且误差为O(N^2)，其中N是矩阵大小。量子块编码是量子线性代数算法的基础，这些算法在量子机器学习、量子化学模拟中具有潜在应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum block encoding (QBE) is a crucial step in the development of most quantum algorithms, as it provides an embedding of a given matrix into a suitable larger unitary matrix. Historically, the development of efficient techniques for QBE has mostly focused on sparse matrices; less effort has been devoted to data-sparse (e.g., rank-structured) matrices. In this work we examine a particular case of rank structure, namely, one-pair semiseparable matrices. We present a new block encoding approach that relies on a suitable factorization of the given matrix as the product of triangular and diagonal factors. To encode the matrix, the algorithm needs $2\log(N)+7$ ancillary qubits. This process takes polylogarithmic time and has an error of $\mathcal{O}(N^2)$, where $N$ is the matrix size.

</details>

---

### 59. [CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions](https://arxiv.org/abs/2403.17210)

**基本信息**

- 🔗 arXiv: [`2403.17210`](https://arxiv.org/abs/2403.17210)
- 👥 作者: Azmine Toushik Wasi, Taki Hasan Rafi, Raima Islam 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2403.17210.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的深度图学习框架（CADGL）用于药物-药物相互作用预测。图神经网络是处理分子图结构数据的核心模型，属于化学信息学中“化学大模型”的重要分支。

**📖 中文摘要**

本文提出了CADGL，一个用于预测药物-药物相互作用（DDIs）的情境感知深度图学习框架。DDIs研究是药物开发过程中的关键环节。CADGL基于定制的变分图自编码器（VGAE），使用两个情境预处理器从两个不同角度（局部邻域和分子情境）在异质图结构中提取特征。我们定制的VGAE由图像编码器、潜在信息编码器和MLP解码器组成。CADGL超越了其他最先进的DDI预测模型，擅长预测具有临床价值的新型DDIs。这项工作展示了图神经网络（一种重要的深度学习架构）在化学信息学核心任务——药物相互作用预测中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Examining Drug-Drug Interactions (DDIs) is a pivotal element in the process of drug development. DDIs occur when one drug's properties are affected by the inclusion of other drugs. Detecting favorable DDIs has the potential to pave the way for creating and advancing innovative medications applicable in practical settings. However, existing DDI prediction models continue to face challenges related to generalization in extreme cases, robust feature extraction, and real-life application possibilities. We aim to address these challenges by leveraging the effectiveness of context-aware deep graph learning by introducing a novel framework named CADGL. Based on a customized variational graph autoencoder (VGAE), we capture critical structural and physio-chemical information using two context preprocessors for feature extraction from two different perspectives: local neighborhood and molecular context, in a heterogeneous graphical structure. Our customized VGAE consists of a graph encoder, a latent information encoder, and an MLP decoder. CADGL surpasses other state-of-the-art DDI prediction models, excelling in predicting clinically valuable novel DDIs, supported by rigorous case studies. CADGL is vailable at: this https URL

</details>

---

### 60. [Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset](https://arxiv.org/abs/2407.17869)

**基本信息**

- 🔗 arXiv: [`2407.17869`](https://arxiv.org/abs/2407.17869)
- 👥 作者: Yiming Ma, Jianzhi Teng, Xinjie Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.17869.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成模型（流匹配）解决逆椭圆偏振问题，这是一个从测量信号反推材料参数的逆问题。其问题范式（不适定逆问题、需要物理约束、使用生成模型）与“质谱结构推理”（从质谱信号反推分子结构）在方法论和挑战上高度相似，属于同一类科学逆问题求解。

**📖 中文摘要**

逆椭圆偏振法，即从测量的相位差Δ和振幅比Ψ重建光学常数和薄膜厚度，是一个本质上不适定的问题。传统解决方案依赖于缓慢的、专家驱动的迭代拟合，而机器学习方法的发展由于缺乏大规模、物理一致的数据集而受到严重限制。为了弥补这一差距，作者引入了EllipBench，一个包含超过800万个高精度样本的综合基准，涵盖98种薄膜材料和5种基底。在此基准之上，作者系统地评估了广泛的方法，并进一步提出了解耦条件流匹配（DCFM）框架。DCFM明确解耦了几何薄膜厚度，并将其作为稳健的物理条件来指导一个连续的向量场，用于建模波长相关光学常数的逆概率分布。这项工作展示了生成模型（流匹配）在解决材料表征逆问题中的应用。虽然应用领域是光学测量，但其“从测量数据反推材料参数”的逆问题范式与“质谱结构推理”高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse ellipsometry, i.e., reconstructing optical constants and film thickness from the measured phase difference $\Delta$ and amplitude ratio $\Psi$, is a fundamentally ill-posed problem. Traditional solutions rely on slow, expert-driven iterative fitting, while the development of machine learning approaches has been severely limited by the lack of large-scale, physically consistent datasets. To address this gap, we introduce \textbf{EllipBench}, a comprehensive benchmark comprising over 8 million high-precision samples spanning 98 thin-film materials and 5 substrates. Building upon this benchmark, we conduct a systematic evaluation of a broad spectrum of methods, including traditional machine learning models, deep neural networks, and Physics-Informed Neural Networks, and show that existing paradigms consistently struggle to fully resolve the inverse ellipsometry task. To better capture its inherent ambiguity, we further propose a novel \textbf{Decoupled Conditional Flow Matching (DCFM)} framework. Rather than formulating the problem as deterministic point-to-point regression, DCFM explicitly decouples geometric film thickness and incorporates it as a robust physical condition to guide a continuous vector field for modeling the inverse probability distribution of wavelength-dependent optical constants. Combined with a gradient detachment strategy and physics-based constraints, our joint architecture effectively mitigates intrinsic physical ambiguities and delivers a robust and accurate solution for inverse ellipsometry.

</details>

---

### 61. [Biased AI can Influence Political Decision-Making](https://arxiv.org/abs/2410.06415)

**基本信息**

- 🔗 arXiv: [`2410.06415`](https://arxiv.org/abs/2410.06415)
- 👥 作者: Jillian Fisher, Shangbin Feng, Robert Aron 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.06415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（Cliqueformer架构）在化学设计任务上进行了应用和验证，直接关联到利用大模型（Transformer）进行化学空间探索和优化的‘化学大模型’主题。

**📖 中文摘要**

论文《Cliqueformer: Model-Based Optimization with Structured Transformers》提出了一种基于Transformer的架构Cliqueformer，用于解决基于模型的优化（MBO）问题。该架构通过学习黑盒函数的结构（通过功能图模型）来处理分布偏移，而无需依赖显式的保守方法。论文在多个领域（包括化学和遗传设计任务）中展示了其性能优于现有方法。虽然论文主要关注通用的MBO框架，但其明确将化学设计任务作为关键应用领域之一。这表明Cliqueformer所代表的结构化Transformer方法可以应用于化学空间的探索和优化，这与“化学大模型”主题中利用先进机器学习模型（如Transformer）解决化学问题的研究方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As modern large language models (LLMs) become integral to everyday tasks, concerns about their inherent biases and their potential impact on human decision-making have emerged. While bias in models are well-documented, less is known about how these biases influence human decisions. This paper presents two interactive experiments investigating the effects of partisan bias in LLMs on political opinions and decision-making. Participants interacted freely with either a biased liberal, biased conservative, or unbiased control model while completing these tasks. We found that participants exposed to partisan biased models were significantly more likely to adopt opinions and make decisions which matched the LLM's bias. Even more surprising, this influence was seen when the model bias and personal political partisanship of the participant were opposite. However, we also discovered that prior knowledge of AI was weakly correlated with a reduction of the impact of the bias, highlighting the possible importance of AI education for robust mitigation of bias effects. Our findings not only highlight the critical effects of interacting with biased LLMs and its ability to impact public discourse and political conduct, but also highlights potential techniques for mitigating these risks in the future.

</details>

---

### 62. [Degrees of Freedom of Cache-Aided Interference Channels Assisted by Active Intelligent Reflecting Surfaces](https://arxiv.org/abs/2411.17559)

**基本信息**

- 🔗 arXiv: [`2411.17559`](https://arxiv.org/abs/2411.17559)
- 👥 作者: Abolfazl Changizi, Ali H. Abdollahi Bafghi, Mahtab Mirmohseni 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.17559.pdf)

**💡 相关性分析**

不相关。论文核心是无线通信理论，与化学信息学或质谱分析无直接关联。其优化方法虽具一般性，但未应用于或讨论目标领域，不符合任何相关性标准。

**📖 中文摘要**

论文《Degrees of Freedom of Cache-Aided Interference Channels Assisted by Active Intelligent Reflecting Surfaces》研究无线通信网络中缓存辅助的干扰信道。虽然论文主题是通信和信息论，但其核心方法涉及联合设计内容放置、传输阶段和智能反射面系数。这种对系统状态（缓存内容、信道条件）进行联合优化以最大化性能（自由度）的框架，在方法论上与“化学大模型”和“质谱结构推理”中可能涉及的复杂系统建模与优化有抽象层面的相似性。然而，这种关联性较弱且间接。论文并未直接提供化学或质谱数据、工具，也未讨论相关主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper studies cache-aided wireless networks in the presence of active intelligent reflecting surfaces (IRSs) from an information-theoretic perspective. Specifically, we investigate interference management in a cache-aided wireless network assisted by an active IRS to enhance the achievable degrees of freedom (DoF). To this end, we jointly design the content placement, delivery phase, and IRS coefficients, and propose a one-shot achievability scheme. Our scheme exploits transmitters' cooperation, cache contents, interference alignment, and IRS capabilities, based on the network parameters. We derive the achievable one-shot sum-DoF for different cache sizes, network configurations, and numbers of IRS elements, followed by an upper bound. Our results highlight the potential of deploying an IRS in cache-aided wireless communication systems. In particular, they underscore the enhancement of achievable DoF for various parameter regimes, especially when cache sizes are inadequate. Notably, we show that access to an IRS with a sufficient number of elements enables the achievement of the maximum possible DoF for various parameter regimes of interest.

</details>

---

### 63. [Is Contrastive Distillation Enough for Learning Comprehensive 3D Representations?](https://arxiv.org/abs/2412.08973)

**基本信息**

- 🔗 arXiv: [`2412.08973`](https://arxiv.org/abs/2412.08973)
- 👥 作者: Yifan Zhang, Junhui Hou
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.08973.pdf)

**💡 相关性分析**

不相关。论文专注于计算机视觉中的3D表示学习，其方法、任务和评估均围绕视觉数据展开，与化学信息学或质谱分析无直接联系。

**📖 中文摘要**

论文《Is Contrastive Distillation Enough for Learning Comprehensive 3D Representations?》提出了一种新的跨模态全面表示学习框架CMCR，用于3D表示学习。该框架通过引入掩码图像建模和占用估计任务来学习更全面的模态特定特征，并提出了一个新颖的多模态统一码本。虽然论文主要关注3D视觉（如图像到LiDAR），但其核心思想——通过改进的对比学习和多模态融合来学习更全面、更有效的表示——在方法论上与“化学大模型”中学习分子或材料的稳健表示有潜在相通之处。然而，论文并未在化学或质谱领域进行任何应用或讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cross-modal contrastive distillation has recently been explored for learning effective 3D representations. However, existing methods focus primarily on modality-shared features, neglecting the modality-specific features during the pre-training process, which leads to suboptimal representations. In this paper, we theoretically analyze the limitations of current contrastive methods for 3D representation learning and propose a new framework, namely CMCR (Cross-Modal Comprehensive Representation Learning), to address these shortcomings. Our approach improves upon traditional methods by better integrating both modality-shared and modality-specific features. Specifically, we introduce masked image modeling and occupancy estimation tasks to guide the network in learning more comprehensive modality-specific features. Furthermore, we propose a novel multi-modal unified codebook that learns an embedding space shared across different modalities. Besides, we introduce geometry-enhanced masked image modeling to further boost 3D representation learning. Extensive experiments demonstrate that our method mitigates the challenges faced by traditional approaches and consistently outperforms existing image-to-LiDAR contrastive distillation methods in downstream tasks. Code will be available at this https URL .

</details>

---

### 64. [DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models](https://arxiv.org/abs/2503.16426)

**基本信息**

- 🔗 arXiv: [`2503.16426`](https://arxiv.org/abs/2503.16426)
- 👥 作者: Keyan Chen, Chenyang Liu, Bowen Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.16426.pdf)

**💡 相关性分析**

不相关。论文的研究领域是遥感图像处理，其提出的模型架构和预训练方法专门针对地理空间图像的特性，与化学信息学或质谱分析的主题无关。

**📖 中文摘要**

论文《DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models》提出了一种为遥感图像定制的视觉基础模型DynamicVis。它采用动态区域感知的状态空间模型（SSM）来自适应地处理相关令牌，大幅减少计算复杂度。其预训练范式旨在从密集背景中解耦稀疏的前景实例。虽然论文专注于遥感图像分析，但其核心创新——设计高效、适应数据稀疏特性的基础模型架构——在理念上与为特定科学领域（如化学）构建高效、专业的大模型有共通之处。然而，论文未涉及化学或质谱数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The advancement of RS technology has enabled high-resolution Earth observation; however, interpreting these images using modern VFMs remains a significant challenge. Unlike object-centric natural images, RS imagery is fundamentally characterized by extreme target sparsity and massive spatial redundancy. Key objects of interest (e.g., ships, vehicles) often occupy less than 1% of the spatial extent, surrounded by vast, target-free backgrounds. Existing VFMs predominantly rely on uniform dense processing (e.g., ViTs) and pixel-reconstruction pre-training paradigms (e.g., MAE). These approaches inherently waste substantial computational capacity on modeling redundant backgrounds and inadvertently dilute the feature representations of small, sparse targets. To bridge this structural misalignment, we propose DynamicVis, a visual foundation model explicitly tailored to the sparse nature of RS imagery. Architecturally, DynamicVis introduces a Dynamic Region-Aware SSM that bypasses uniform computation. It adaptively routes and incrementally models only task-relevant, high-salience tokens while employing a parameter-free integration for background context, drastically reducing the complexity of processing ultra-long 2D token sequences ($\sim$100,000). Crucially, to equip the network with robust spatial-selection capabilities, we propose a novel Region-Level Meta-Embedding Multi-Instance Learning (MIL) pre-training paradigm. Trained on a million-scale dataset, this paradigm explicitly disentangles sparse foreground instances from dense backgrounds in the latent semantic space, overcoming the semantic ambiguity of conventional pixel-reconstruction methods. Extensive evaluations across nine diverse downstream tasks reveal that DynamicVis exhibits exceptional efficacy, particularly dominating in sparse-target and instance-level perception tasks (e.g., small object detection, and change detection).

</details>

---

### 65. [Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks](https://arxiv.org/abs/2504.12441)

**基本信息**

- 🔗 arXiv: [`2504.12441`](https://arxiv.org/abs/2504.12441)
- 👥 作者: Asutay Ozmen, João P. Hespanha, Katie Byl
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.12441.pdf)

**💡 相关性分析**

不相关。论文的研究对象是机器人系统中的摩擦建模，属于机器人学与控制领域。尽管其PINN方法具有一般性，但未应用于或关联到化学或质谱分析。

**📖 中文摘要**

论文《Learning Transferable Friction Models and LuGre Identification Via Physics-Informed Neural Networks》提出了一种物理信息摩擦估计框架，用于机器人学。该框架将成熟的摩擦模型与可学习组件集成，仅需少量通用测量数据即可实现物理一致且灵活的摩擦建模，并展示了学习模型在不同系统间的可迁移性。虽然论文应用在机器人控制，但其核心方法——结合物理先验与神经网络学习可迁移的、解释性强的模型——与“化学大模型”中构建融合物理化学知识的、可泛化的分子或性质预测模型在方法论精神上相似。然而，论文未在化学领域进行任何应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurately modeling friction in robotics remains a core challenge, as robotics simulators like MuJoCo and PyBullet use simplified friction models or heuristics to balance computational efficiency with accuracy, where these simplifications and approximations can lead to substantial differences between simulated and physical performance. In this paper, we present a physics-informed friction estimation framework that enables the integration of well-established friction models with learnable components, requiring only minimal, generic measurement data. Our approach enforces physical consistency yet retains the flexibility to capture complex friction phenomena. We demonstrate, on an underactuated and nonlinear system, that the learned friction models, trained solely on small and noisy datasets, accurately reproduce dynamic friction properties with significantly higher fidelity than the simplified models commonly used in robotics simulators. Crucially, we show that our approach enables the learned models to be transferable to systems they are not trained on. This ability to generalize across multiple systems streamlines friction modeling for complex, underactuated tasks, offering a scalable and interpretable path toward improving friction model accuracy in robotics and control.

</details>

---

### 66. [Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability](https://arxiv.org/abs/2505.03530)

**基本信息**

- 🔗 arXiv: [`2505.03530`](https://arxiv.org/abs/2505.03530)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03530.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深度生成模型（VAE）的机制可解释性，并提供了系统的因果干预框架。生成模型（包括VAE）是构建“化学大模型”（如用于分子生成、性质预测的模型）的关键技术之一。因此，该论文直接关联到理解和改进化学大模型中可能采用的生成模型组件。

**📖 中文摘要**

论文《Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability》为变分自编码器（VAE）的机制可解释性引入了一个全面的因果干预框架。该框架开发了识别和分析VAE中“电路模体”的技术，通过不同层次的干预来研究语义因子如何通过网络层编码、处理和分离。论文在具有已知因果关系的合成数据集和标准解纠缠基准上进行了应用和评估。这项工作推进了对生成模型的机制理解，并为构建更透明、可控的VAE架构提供了工具。VAE是生成模型的重要类别，在化学信息学中可用于分子生成、表示学习等任务。因此，这篇关于VAE机制可解释性的论文，为理解和改进可能在“化学大模型”中使用的生成模型组件提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic interpretability of deep learning models has emerged as a crucial research direction for understanding the functioning of neural networks. While significant progress has been made in interpreting discriminative models like transformers, understanding generative models such as Variational Autoencoders (VAEs) remains challenging. This paper introduces a comprehensive causal intervention framework for mechanistic interpretability of VAEs. We develop techniques to identify and analyze "circuit motifs" in VAEs, examining how semantic factors are encoded, processed, and disentangled through the network layers. Our approach uses targeted interventions at different levels: input manipulations, latent space perturbations, activation patching, and causal mediation analysis. We apply our framework to both synthetic datasets with known causal relationships and standard disentanglement benchmarks. Results show that our interventions can successfully isolate functional circuits, map computational graphs to causal graphs of semantic factors, and distinguish between polysemantic and monosemantic units. Furthermore, we introduce metrics for causal effect strength, intervention specificity, and circuit modularity that quantify the interpretability of VAE components. Experimental results demonstrate clear differences between VAE variants, with FactorVAE achieving higher disentanglement scores (0.084) and effect strengths (mean 4.59) compared to standard VAE (0.064, 3.99) and Beta-VAE (0.051, 3.43). Our framework advances the mechanistic understanding of generative models and provides tools for more transparent and controllable VAE architectures.

</details>

---

### 67. [MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models](https://arxiv.org/abs/2505.10294)

**基本信息**

- 🔗 arXiv: [`2505.10294`](https://arxiv.org/abs/2505.10294)
- 👥 作者: Guillaume Balezo, Roger Trullo, Albert Pla Planas 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.10294.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大模型（ViT）从一种测量数据（H&E图像）推理出更丰富的生物标记信息（mIF信号）。这种跨模态推理的范式与“质谱结构推理”中从质谱数据推断分子结构的核心问题高度相似，属于同一类“从测量数据推理底层结构/属性”的研究主题。

**📖 中文摘要**

论文《MIPHEI-ViT: Multiplex Immunofluorescence Prediction from H&E Images using ViT Foundation Models》提出MIPHEI模型，利用ViT病理基础模型作为编码器，从H&E组织病理学图像预测多重免疫荧光（mIF）信号。该模型针对包括免疫细胞谱系（如T细胞、B细胞、髓系细胞）在内的综合标记物面板进行预测。论文在多个公共数据集上进行了训练和验证。虽然该研究属于计算病理学和医学图像分析领域，但其核心是开发一个基于Transformer基础模型的、能够从一种模态（H&E图像）预测另一种更丰富模态（mIF信号）的跨模态预测框架。这种“从A预测B”的范式，与“质谱结构推理”中从质谱数据推断分子结构在问题形式上具有类比性。两者都涉及从复杂、高维的测量数据中解码出更结构化、更具语义的信息。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathological analysis is a cornerstone of cancer diagnosis, with Hematoxylin and Eosin (H&E) staining routinely acquired for every patient to visualize cell morphology and tissue architecture. On the other hand, multiplex immunofluorescence (mIF) enables more precise cell type identification via proteomic markers, but has yet to achieve widespread clinical adoption due to cost and logistical constraints. To bridge this gap, we introduce MIPHEI (Multiplex Immunofluorescence Prediction from H&E Images), a U-Net-inspired architecture that leverages a ViT pathology foundation model as encoder to predict mIF signals from H&E images using rich pretrained representations. MIPHEI targets a comprehensive panel of markers spanning nuclear content, immune lineages (T cells, B cells, myeloid), epithelium, stroma, vasculature, and proliferation. We train our model using the publicly available OrionCRC dataset of restained H&E and mIF images from colorectal cancer tissue, and validate it on five independent datasets: HEMIT, PathoCell, IMMUcan, Lizard and PanNuke. On OrionCRC test set, MIPHEI achieves accurate cell-type classification from H&E alone, with F1 scores of 0.93 for Pan-CK, 0.83 for alpha-SMA, 0.68 for CD3e, 0.36 for CD20, and 0.28 for CD68, substantially outperforming both a state-of-the-art baseline and a random classifier for most markers. Our results indicate that, for some molecular markers, our model captures the complex relationships between nuclear morphologies in their tissue context, as visible in H&E images and molecular markers defining specific cell types. MIPHEI offers a promising step toward enabling cell-type-aware analysis of large-scale H&E datasets, in view of uncovering relationships between spatial cellular organization and patient outcomes.

</details>

---

### 68. [RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval](https://arxiv.org/abs/2506.08625)

**基本信息**

- 🔗 arXiv: [`2506.08625`](https://arxiv.org/abs/2506.08625)
- 👥 作者: Minhae Oh, Jeonghye Kim, Nakyung Lee 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08625.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升LLM在科学推理任务中的能力，其提出的逐步检索增强框架（RAISE）直接针对大模型在需要专业知识和复杂推理的场景下的局限性。这完全契合“化学大模型”主题中关于如何让大模型更好地进行化学领域推理和研究的关键研究方向。

**📖 中文摘要**

论文《RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval》提出了RAISE框架，通过逐步检索增强大型语言模型（LLMs）的科学推理能力。该框架分为问题分解、逻辑查询生成和逻辑检索三个步骤，旨在从外部语料库中检索逻辑相关的文档以支持复杂的科学推理。论文在科学推理基准上进行了评估，表明RAISE consistently outperforms other baselines。虽然论文关注一般科学推理，但其核心方法——通过检索增强来提升LLM在需要领域术语和最新知识的长链推理任务中的表现——与“化学大模型”面临的挑战（如需要准确的化学知识、处理复杂分子推理）直接相关。RAISE框架为构建更可靠、知识丰富的化学领域大模型提供了一种可行的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific reasoning requires not only long-chain reasoning processes, but also knowledge of domain-specific terminologies and adaptation to updated findings. To deal with these challenges for scientific reasoning, we introduce RAISE, a step-by-step retrieval-augmented framework which retrieves logically relevant documents from in-the-wild corpus. RAISE is divided into three steps: problem decomposition, logical query generation, and logical retrieval. We observe that RAISE consistently outperforms other baselines on scientific reasoning benchmarks. We analyze that unlike other baselines, RAISE retrieves documents that are not only similar in terms of the domain knowledge, but also documents logically more relevant.

</details>

---

### 69. [Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning](https://arxiv.org/abs/2506.16931)

**基本信息**

- 🔗 arXiv: [`2506.16931`](https://arxiv.org/abs/2506.16931)
- 👥 作者: Jiaqi Chen, Mingfeng Fan, Xuefeng Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.16931.pdf)

**💡 相关性分析**

不相关。论文的研究问题是机器人学中的组合优化和路径规划，其多模态融合方法针对的是空间坐标和图拓扑，与化学分子表示和质谱数据有本质区别。

**📖 中文摘要**

论文《Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning》提出了多模态融合学习（MMFL）框架，用于解决机器人任务规划中的广义旅行商问题（GTSP）。该框架利用图和图像两种表示来捕捉问题的互补方面，并学习一个能够实时生成高质量任务规划方案的策略。具体包括一个基于坐标的图像构建器、自适应分辨率缩放策略以及一个带有专用瓶颈的多模态融合模块。虽然论文应用在机器人路径规划，但其核心创新——融合不同模态（图结构、空间图像）的信息以更好地解决组合优化问题——在方法论上与“化学大模型”可能面临的挑战（如融合分子图、序列、3D结构等多种表示以进行分子优化或设计）有概念上的关联。然而，论文未涉及任何化学应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Effective and efficient task planning is essential for mobile robots, especially in applications like warehouse retrieval and environmental monitoring. These tasks often involve selecting one location from each of several target clusters, forming a Generalized Traveling Salesman Problem (GTSP) that remains challenging to solve both accurately and efficiently. To address this, we propose a Multimodal Fused Learning (MMFL) framework that leverages both graph and image-based representations to capture complementary aspects of the problem, and learns a policy capable of generating high-quality task planning schemes in real time. Specifically, we first introduce a coordinate-based image builder that transforms GTSP instances into spatially informative representations. We then design an adaptive resolution scaling strategy to enhance adaptability across different problem scales, and develop a multimodal fusion module with dedicated bottlenecks that enables effective integration of geometric and spatial features. Extensive experiments show that our MMFL approach significantly outperforms state-of-the-art methods across various GTSP instances while maintaining the computational efficiency required for real-time robotic applications. Physical robot tests further validate its practical effectiveness in real-world scenarios.

</details>

---

### 70. [A Crowdsensing Intrusion Detection Dataset For Decentralized Federated Learning Models](https://arxiv.org/abs/2507.13313)

**基本信息**

- 🔗 arXiv: [`2507.13313`](https://arxiv.org/abs/2507.13313)
- 👥 作者: Chao Feng, Alberto Huertas Celdran, Jing Han 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.13313.pdf)

**💡 相关性分析**

不相关。尽管论文提供了数据集（满足标准2的形式），但该数据集的内容（物联网设备行为日志）与“化学大模型”和“质谱结构推理”主题所需的数据类型（化学结构、质谱数据、分子描述符等）完全无关，因此不具备实质相关性。

**📖 中文摘要**

论文《A Crowdsensing Intrusion Detection Dataset For Decentralized Federated Learning Models》介绍了一个用于去中心化联邦学习（DFL）的物联网群智感知恶意软件检测数据集，并进行了实验研究。该数据集包含来自系统调用、文件系统活动、资源使用、内核事件、I/O事件和网络记录的行为记录，总计2158万条原始记录，被聚合为34.2万条数据记录用于模型训练和评估。论文在DFL平台上比较了传统机器学习、集中式联邦学习和去中心化联邦学习。虽然论文主题是网络安全和联邦学习，但其主要贡献是发布了一个新的、标注好的行为数据集。根据相关性标准，提供数据集（数据资源）的论文应被考虑。然而，该数据集专门针对物联网设备恶意软件检测的行为日志，与化学信息学或质谱分析所需的化学结构、质谱图谱、分子性质等数据类型完全不同，无法用于指定的研究主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper introduces a dataset and an experimental study on Decentralized Federated Learning (DFL) for Internet of Things (IoT) crowdsensing malware detection. The dataset comprises behavioral records from benign and eight malware attacks. A total of 21,582,484 original records were collected from system calls, file system activities, resource usage, kernel events, input/output events, and network records. These records were aggregated into 30-second windows, resulting in 342,106 data records used for model training and evaluation. Experiments on the DFL platform compare traditional Machine Learning (ML), Centralized Federated Learning (CFL), and DFL across different node counts, topologies, and data distributions. Results show that DFL maintains competitive performance while preserving data locality, outperforming CFL in most settings. This dataset provides a solid foundation for studying the security of IoT crowdsensing environments.

</details>

---

### 71. [Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection](https://arxiv.org/abs/2507.16861)

**基本信息**

- 🔗 arXiv: [`2507.16861`](https://arxiv.org/abs/2507.16861)
- 👥 作者: Xiang Li, Zhangchi Hu, Xiao Xu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.16861.pdf)

**💡 相关性分析**

不相关。论文的研究领域是自动驾驶的多传感器融合（LiDAR和相机），其提出的方法专门针对空间几何对齐问题，与化学信息学中的质谱数据对齐或分子表示融合有本质不同。

**📖 中文摘要**

论文《Look Before You Fuse: 2D-Guided Cross-Modal Alignment for Robust 3D Detection》专注于自动驾驶中的3D目标检测，旨在解决LiDAR和相机特征在鸟瞰图（BEV）表示中的空间未对齐问题。论文提出了利用2D目标先验进行跨模态特征预对齐的方法，包括先验引导深度校准（PGDC）、不连续性感知几何融合（DAGF）和结构引导深度调制器（SGDM）。其核心动机是利用2D检测器可靠识别的物体-背景边界信息来指导3D感知中的特征融合。虽然论文属于自动驾驶感知领域，但其解决“跨模态对齐”这一核心问题的思路——即利用一种模态（2D图像）的可靠信息来校准和增强另一种模态（3D点云）的特征，以实现更稳健的融合——与“质谱结构推理”中可能面临的挑战（如对齐质谱数据与其他分子表示形式）在问题抽象层面有相似性。然而，论文未涉及任何化学或质谱数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating LiDAR and camera inputs into a unified Bird's-Eye-View (BEV) representation is crucial for enhancing 3D perception capabilities of autonomous vehicles. However, existing methods suffer from spatial misalignment between LiDAR and camera features, which causes inaccurate depth supervision in camera branch and erroneous fusion during cross-modal feature aggregation. The root cause of this misalignment lies in projection errors, stemming from calibration inaccuracies and rolling shutter effect. The key insight of this work is that locations of these projection errors are not random but highly predictable, as they are concentrated at object-background boundaries which 2D detectors can reliably identify. Based on this, our main motivation is to utilize 2D object priors to pre-align cross-modal features before fusion. To address local misalignment, we propose Prior Guided Depth Calibration (PGDC), which leverages 2D priors to alleviate misalignment and preserve correct cross-modal feature pairs. To resolve global misalignment, we introduce Discontinuity Aware Geometric Fusion (DAGF) to suppress residual noise from PGDC and explicitly enhance sharp depth transitions at object-background boundaries, yielding a structurally aware representation. To effectively utilize these aligned representations, we incorporate Structural Guidance Depth Modulator (SGDM), using a gated attention mechanism to efficiently fuse aligned depth and image features. Our method achieves SOTA performance on nuScenes validation dataset, with its mAP and NDS reaching 71.5% and 73.6% respectively. Additionally, on the Argoverse 2 validation set, we achieve a competitive mAP of 41.7%.

</details>

---

### 72. [Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions](https://arxiv.org/abs/2508.17303)

**基本信息**

- 🔗 arXiv: [`2508.17303`](https://arxiv.org/abs/2508.17303)
- 👥 作者: Dhiraj S Kori, Abhinav Chandraker, Syed Abdur Rahman 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.17303.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用物理信息神经网络（PINN）解决材料科学中的关键预测问题（疲劳寿命）。PINN是构建“化学大模型”的重要技术路径之一，用于将物理化学定律融入数据驱动的模型中。该论文展示了PINN在复杂科学预测任务中的有效应用，直接关联到利用先进机器学习模型（大模型）解决化学、材料科学问题的主题。

**📖 中文摘要**

论文《Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions》提出了一种物理信息神经网络（PINN）框架，用于预测核反应堆中使用的辐照后奥氏体和铁素体/马氏体钢的低周疲劳寿命。该框架将疲劳寿命控制的物理约束嵌入损失函数，在495个应变控制疲劳数据点上进行了训练。论文展示了PINN相对于传统机器学习方法的优越性，并进行了可解释性分析。这项工作属于计算材料学和核工程领域。虽然应用特定，但其核心方法——PINN——是科学机器学习（SciML）的代表性技术之一，在化学、材料科学中广泛应用于构建融合物理知识的预测模型。因此，这篇论文作为PINN在材料性能预测中的一个成功案例，其方法论对“化学大模型”中构建物理信息驱动的化学性质预测模型具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study proposes a Physics-Informed Neural Network (PINN) framework to predict the low-cycle fatigue (LCF) life of irradiated austenitic and ferritic/martensitic (F/M) steels used in nuclear reactors. These materials undergo cyclic loading, neutron irradiation, and elevated temperatures, leading to complex degradation mechanisms that are difficult to capture with conventional empirical or purely data-driven models. The proposed PINN embeds fatigue-life governing physical constraints into the loss function, enabling physically consistent learning while improving predictive accuracy, reliability, and generalizability. The model was trained on 495 strain-controlled fatigue data points spanning irradiated and unirradiated conditions. Compared with traditional machine learning approaches, including Random Forest, Gradient Boosting, eXtreme Gradient Boosting, and conventional neural networks, the PINN demonstrated superior performance. SHapley Additive exPlanations (SHAP) analysis identified strain amplitude, irradiation dose, and test temperature as the dominant features, each exhibiting physically meaningful inverse correlations with fatigue life. Univariate and multivariate analyses revealed clear alloy-specific degradation characteristics. Austenitic steels exhibited strong nonlinear coupling among strain amplitude, irradiation dose, and temperature, resulting in pronounced fatigue degradation under combined loading. In contrast, F/M steels demonstrated comparatively stable irradiation responses, including dose-saturation behavior, but showed sensitivity to elevated temperatures beyond tempering thresholds. Overall, the proposed PINN framework serves as a reliable and interpretable tool for reactor-relevant fatigue assessment, enabling performance evaluation for advanced nuclear applications.

</details>

---

### 73. [Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning](https://arxiv.org/abs/2509.08759)

**基本信息**

- 🔗 arXiv: [`2509.08759`](https://arxiv.org/abs/2509.08759)
- 👥 作者: Mominul Rubel, Adam Meyers, Gabriel Nicolosi
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.08759.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新型的、基于傅里叶级数表示的神经网络架构（FLM），专门用于科学机器学习。这直接关联到“化学大模型”主题中关于为化学科学问题设计和开发新型、高效、可解释的基础模型架构的研究方向。

**📖 中文摘要**

论文《Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning》引入了傅里叶学习机（FLM），一种设计用于表示多维非调和傅里叶级数的神经网络架构。FLM使用具有余弦激活函数的前馈结构，将级数的频率、振幅和相移作为可训练参数进行学习。该设计允许模型创建适应周期和非周期函数的问题特定谱基。论文在包括偏微分方程（PDE）和最优控制问题（OCP）在内的多个科学计算问题上评估了FLM的性能。FLM作为一种新型的、具有明确频谱解释的神经网络架构，是科学机器学习（SciML）中的基础模型创新。SciML是构建“化学大模型”的核心方法论领域，旨在为科学问题设计专用的神经网络架构。因此，这篇提出新型科学机器学习基础架构的论文，与“化学大模型”主题中关于模型架构创新的研究直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Fourier Learning Machine (FLM), a neural network (NN) architecture designed to represent a multidimensional nonharmonic Fourier series. The FLM uses a simple feedforward structure with cosine activation functions to learn the frequencies, amplitudes, and phase shifts of the series as trainable parameters. This design allows the model to create a problem-specific spectral basis adaptable to both periodic and nonperiodic functions. Unlike previous Fourier-inspired NN models, the FLM is the first architecture able to represent a multidimensional Fourier series with a complete set of basis functions in separable form, doing so by using a standard Multilayer Perceptron-like architecture. A one-to-one correspondence between the Fourier coefficients and amplitudes and phase-shifts is demonstrated, allowing for the translation between a full, separable basis form and the cosine phase-shifted one. Additionally, we evaluate the performance of FLMs on several scientific computing problems, including benchmark Partial Differential Equations (PDEs) and a family of Optimal Control Problems (OCPs). Computational experiments show that the performance of FLMs is comparable, and often superior, to that of established architectures like SIREN and vanilla feedforward NNs.

</details>

---

### 74. [Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity](https://arxiv.org/abs/2601.18032)

**基本信息**

- 🔗 arXiv: [`2601.18032`](https://arxiv.org/abs/2601.18032)
- 👥 作者: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18032.pdf)

**💡 相关性分析**

满足标准2：论文构建了一个高质量的介电弹性体数据集，并提出了一个利用预训练聚合物表示（化学大模型）的多模态学习框架，为化学大模型在材料发现中的应用提供了数据资源和工具。

**📖 中文摘要**

本文聚焦于高性能介电弹性体的开发，这是一个化学信息学中的材料设计问题。论文的核心贡献在于构建了一个高质量的丙烯酸酯基介电弹性体数据集，该数据集系统地整合了分子序列、介电和机械性能。更重要的是，论文提出了一个多模态学习框架，该框架利用大规模预训练的聚合物表示（即化学大模型）来迁移化学和结构知识。通过利用这些预训练嵌入，该框架能够在数据稀缺的情况下，对介电和机械性能进行准确的少样本预测，从而加速数据高效的软高介电常数弹性体的发现。这项工作直接提供了用于化学大模型应用的数据集和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggregating experimental results from the past decade. Building on this dataset, we propose a multimodal learning framework leveraging large-scale pretrained polymer representations. These pretrained embeddings transfer chemical and structural knowledge from vast polymer corpora, enabling accurate few-shot prediction of dielectric and mechanical properties and accelerating data-efficient discovery of soft high-$k$ dielectric elastomers. Our data and implementation are publicly available at: this https URL

</details>

---

### 75. [Sheaf Neural Networks and biomedical applications](https://arxiv.org/abs/2602.00159)

**基本信息**

- 🔗 arXiv: [`2602.00159`](https://arxiv.org/abs/2602.00159)
- 👥 作者: Aneeqa Mehrab, Jan Willem Van Looy, Pietro Demurtas 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00159.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图神经网络（SNN）及其在生物医学图谱上的应用。图神经网络是化学信息学（用于分子图）和质谱结构推理（用于谱图表示）中的核心方法之一，因此该研究直接相关。

**📖 中文摘要**

本文介绍了层神经网络（SNN）的理论和数学模型，并将其应用于生物医学领域的一个具体案例研究。虽然论文主题是图神经网络（GNN）的变体，但其核心应用场景是生物医学问题，例如分析生物分子网络或生物医学图谱。在化学信息学和质谱分析领域，图神经网络是用于分子表示学习和质谱结构推理的常用工具。论文通过案例展示了SNN在生物医学图谱上的有效性，并声称其性能优于流行的图卷积网络（GCN）、图注意力网络（GAT）和GraphSage。这表明SNN作为一种新的图表示学习方法，有潜力被应用于分子图分析或质谱谱图推理等任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The purpose of this paper is to elucidate the theory and mathematical modelling behind the sheaf neural network (SNN) algorithm and then show how SNN can effectively answer to biomedical questions in a concrete case study and outperform the most popular graph neural networks (GNNs) as graph convolutional networks (GCNs), graph attention networks (GAT) and GraphSage.

</details>

---

### 76. [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](https://arxiv.org/abs/2603.03686)

**基本信息**

- 🔗 arXiv: [`2603.03686`](https://arxiv.org/abs/2603.03686)
- 👥 作者: Jiangyu Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03686.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是用于自动化化学配方设计的神经符号框架，这直接属于化学信息学中的“化学大模型”应用范畴，即利用AI模型进行分子/材料设计与发现。

**📖 中文摘要**

本文提出了AI4S-SDS，一个用于自动化化学配方设计的神经符号框架。该框架集成了多智能体协作和定制的蒙特卡洛树搜索（MCTS）引擎，旨在解决高维组合空间（离散组成选择和连续几何约束）的导航问题。为了克服大型语言模型（LLM）智能体在长程推理和上下文窗口限制方面的挑战，论文引入了稀疏状态存储和动态路径重建机制。更重要的是，该框架通过一个可微物理引擎，将符号推理与物理可行性（热力学约束）桥接起来，使用混合归一化损失和稀疏诱导正则化来优化连续混合比例。论文的实证结果表明，该框架在采用的基于HSP的物理约束下实现了完全有效性，并显著提高了探索多样性。在初步的光刻实验中，该框架识别出一种新型光刻胶显影剂配方，其性能与商业基准相比具有竞争力或更优。这项工作展示了面向科学发现的、多样性驱动的神经符号搜索在化学配方设计（化学信息学的一个核心问题）中的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.

</details>

---

### 77. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是用于材料发现和优化的新型AI模型（CliqueFlowmer），这直接属于“化学大模型”的应用范畴（标准1）。同时，论文开源了代码，为相关研究提供了工具资源（标准2）。

**📖 中文摘要**

本文针对计算材料发现（CMD）中的优化问题，提出了一种基于离线模型优化（MBO）的新技术。与流行的生成建模方法不同，该方法将目标材料属性的直接优化融合到生成过程中。为此，论文引入了一个领域特定模型CliqueFlowmer，该模型将基于clique的最新MBO进展融入Transformer和流生成中。验证结果表明，CliqueFlowmer产生的材料性能显著优于生成基线。这项工作为专门的材料优化问题提供了新的解决方案，并开源了代码以支持跨学科研究。这直接关联到化学信息学中利用AI模型（如Transformer）进行材料设计和性质预测的核心任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 78. [A Unified View of Drifting and Score-Based Models](https://arxiv.org/abs/2603.07514)

**基本信息**

- 🔗 arXiv: [`2603.07514`](https://arxiv.org/abs/2603.07514)
- 👥 作者: Chieh-Hsin Lai, Bac Nguyen, Naoki Murata 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07514.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型（漂移模型和基于分数的模型）的理论统一与联系。生成模型是构建“化学大模型”（用于分子生成、设计）的核心技术之一，因此该理论研究直接相关。

**📖 中文摘要**

本文探讨了漂移模型（Drifting Models）与基于分数的模型（如扩散模型）之间的理论联系。论文表明，对于高斯核，漂移模型的总体均值漂移场恰好对应于高斯平滑后的数据分布与模型分布之间的分数差异。这一恒等式源于Tweedie公式，意味着高斯核漂移正是在平滑分布上的分数匹配式目标。此外，论文还将漂移模型与分布匹配蒸馏（DMD）联系起来：两种方法都使用分数失配传输方向，但漂移模型从核邻域非参数地实现分数信号，而DMD使用预训练的扩散教师模型。这项工作从理论层面统一了两种生成模型范式，对于理解和发展用于分子生成或谱图生成的生成模型（化学大模型的重要组成部分）具有基础意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drifting models train one-step generators by optimizing a mean-shift discrepancy induced by a kernel between the data and model distributions, with Laplace kernels used by default in practice. At each point, this discrepancy compares the kernel-weighted displacement toward nearby data samples with the corresponding displacement toward nearby model samples, yielding a transport direction for generated samples. In this paper, we make its relationship to the score-matching principle behind diffusion models precise by showing that drifting admits a score-based formulation on kernel-smoothed distributions. For Gaussian kernels, the population mean-shift field coincides with the score difference between the Gaussian-smoothed data and model distributions. This identity follows from Tweedie's formula, which links the score of a Gaussian-smoothed density to the corresponding conditional mean, and implies that Gaussian-kernel drifting is exactly a score-matching-style objective on smoothed distributions. It also clarifies the connection to Distribution Matching Distillation (DMD): both methods use score-mismatch transport directions, but drifting realizes the score signal nonparametrically from kernel neighborhoods, whereas DMD uses a pretrained diffusion teacher. Beyond Gaussians, we derive an exact decomposition for general radial kernels, and for the Laplace kernel we prove rigorous error bounds showing that drifting remains an accurate proxy for score matching in low-temperature and high-dimensional regimes.

</details>

---

### 79. [Nonparametric Variational Differential Privacy via Embedding Parameter Clipping](https://arxiv.org/abs/2603.09583)

**基本信息**

- 🔗 arXiv: [`2603.09583`](https://arxiv.org/abs/2603.09583)
- 👥 作者: Dina El Zein, Shashi Kumar, James Henderson
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09583.pdf)

**💡 相关性分析**

满足标准3：论文的核心是改进隐私保护机器学习框架（NVDP）。虽然应用场景是语言模型，但论文讨论的隐私保护机器学习技术、变分方法和理论分析，对于在化学信息学和质谱分析中处理敏感数据（如专利分子结构、临床质谱数据）具有重要的相关性和前瞻性讨论价值。

**📖 中文摘要**

本文针对非参数变分差分隐私（NVDP）框架中存在的潜在表示漂移问题，提出了一种基于理论推导的参数裁剪策略。NVDP框架为构建隐私保护的语言模型提供了基础，而本文的工作旨在通过直接约束后验分布的参数来改善其隐私-效用权衡。该方法从最小化Rényi散度上界的目标中数学推导而来，对后验均值、方差和混合权重参数产生了具体的、有理论依据的约束。实验表明，应用该技术的模型在实现更严格隐私界限（意味着更强的隐私性）的同时，在多个下游任务上获得了更高的性能。这项工作提出了一种简单有效的方法来改善变分模型中的隐私-效用权衡，使其更加鲁棒和实用。虽然主要应用于语言模型，但其核心的隐私保护机器学习框架和技术（如变分信息瓶颈、Rényi散度）同样适用于需要隐私保护的化学或生物医学数据（如分子数据、质谱数据）的分析与建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The nonparametric variational information bottleneck (NVIB) provides the foundation for nonparametric variational differential privacy (NVDP), a framework for building privacy-preserving language models. However, the learned latent representations can drift into regions with high information content, leading to poor privacy guarantees, but also low utility due to numerical instability during training. In this work, we introduce a principled parameter clipping strategy to directly address this issue. Our method is mathematically derived from the objective of minimizing the Rényi Divergence (RD) upper bound, yielding specific, theoretically grounded constraints on the posterior mean, variance, and mixture weight parameters. We apply our technique to an NVIB based model and empirically compare it against an unconstrained baseline. Our findings demonstrate that the clipped model consistently achieves tighter RD bounds, implying stronger privacy, while simultaneously attaining higher performance on several downstream tasks. This work presents a simple yet effective method for improving the privacy-utility trade-off in variational models, making them more robust and practical.

</details>

---

### 80. [Thousand-GPU Large-Scale Training and Optimization Recipe for AI-Native Cloud Embodied Intelligence Infrastructure](https://arxiv.org/abs/2603.11101)

**基本信息**

- 🔗 arXiv: [`2603.11101`](https://arxiv.org/abs/2603.11101)
- 👥 作者: Yongjian Guo, Yunxuan Ma, Haoran Sun 等25人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11101.pdf)

**💡 相关性分析**

满足标准3：论文的核心是提出一种通过合成智能体轨迹来增强LLM代码生成能力的新范式。虽然直接应用是代码生成，但其关于从静态结构数据中重建推理轨迹、利用多智能体模拟和思维链优化的方法论，对于构建能够进行复杂化学推理（如逆合成分析、反应机理推理）的“化学大模型”具有重要的相关性和前瞻性讨论价值。

**📖 中文摘要**

本文提出了一种通过逆向工程软件开发生命周期来增强大型语言模型（LLM）代码生成能力的新范式。论文认为，标准的预训练数据（静态软件仓库）只代表了复杂智力过程的终端状态，抽象掉了中间的规划、调试和迭代细化步骤。为了弥补这一差距，论文提出了“通过重建来理解”的范式，即利用多智能体模拟，基于源代码仓库的结构现实（如依赖图和文件层次结构）来合成这些潜在的智能体轨迹（规划、推理、调试步骤）。此外，为了确保合成数据的逻辑严谨性，论文采用了一种基于搜索的优化技术，迭代地细化思维链推理，以最大化生成代码的可能性。实验结果表明，在这些重建的轨迹上进行持续预训练，显著增强了Llama-3-8B在多样化基准测试中的性能。这项工作为改进代码生成LLM提供了一种新方法，而代码生成和分子/反应SMILES生成在序列生成和结构推理方面存在共性，因此该研究对开发用于化学信息学（如逆合成规划、分子设计）的“化学大模型”具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Embodied intelligence is a key step towards Artificial General Intelligence (AGI), yet its development faces multiple challenges including data, frameworks, infrastructure, and evaluation systems. To address these issues, we have, for the first time in the industry, launched a cloud-based, thousand-GPU distributed training platform for embodied intelligence, built upon the widely adopted LeRobot framework, and have systematically overcome bottlenecks across the entire pipeline. At the data layer, we have restructured the data pipeline to optimize the flow of embodied training data. In terms of training, for the GR00T-N1.5 model, utilizing thousand-GPU clusters and data at the scale of hundreds of millions, the single-round training time has been reduced from 15 hours to just 22 minutes, achieving a 40-fold speedup. At the model layer, by combining variable-length FlashAttention and Data Packing, we have moved from sample redundancy to sequence integration, resulting in a 188% speed increase; {\pi}-0.5 attention optimization has accelerated training by 165%; and FP8 quantization has delivered a 140% speedup. On the infrastructure side, relying on high-performance storage, a 3.2T RDMA network, and a Ray-driven elastic AI data lake, we have achieved deep synergy among data, storage, communication, and computation. We have also built an end-to-end evaluation system, creating a closed loop from training to simulation to assessment. This framework has already been fully validated on thousand-GPU clusters, laying a crucial technical foundation for the development and application of next-generation autonomous intelligent robots, and is expected to accelerate the arrival of the era of human-machine integration.

</details>

---

### 81. [Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining](https://arxiv.org/abs/2603.11103)

**基本信息**

- 🔗 arXiv: [`2603.11103`](https://arxiv.org/abs/2603.11103)
- 👥 作者: Zhiyuan Zeng, Yichi Zhang, Yong Shan 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11103.pdf)

**💡 相关性分析**

满足标准3：论文的核心是提出一种通过合成智能体轨迹来增强LLM代码生成能力的新范式。虽然直接应用是代码生成，但其关于从静态结构数据中重建推理轨迹、利用多智能体模拟和思维链优化的方法论，对于构建能够进行复杂化学推理（如逆合成分析、反应机理推理）的“化学大模型”具有重要的相关性和前瞻性讨论价值。

**📖 中文摘要**

本文提出了一种通过逆向工程软件开发生命周期来增强大型语言模型（LLM）代码生成能力的新范式。论文认为，标准的预训练数据（静态软件仓库）只代表了复杂智力过程的终端状态，抽象掉了中间的规划、调试和迭代细化步骤。为了弥补这一差距，论文提出了“通过重建来理解”的范式，即利用多智能体模拟，基于源代码仓库的结构现实（如依赖图和文件层次结构）来合成这些潜在的智能体轨迹（规划、推理、调试步骤）。此外，为了确保合成数据的逻辑严谨性，论文采用了一种基于搜索的优化技术，迭代地细化思维链推理，以最大化生成代码的可能性。实验结果表明，在这些重建的轨迹上进行持续预训练，显著增强了Llama-3-8B在多样化基准测试中的性能。这项工作为改进代码生成LLM提供了一种新方法，而代码生成和分子/反应SMILES生成在序列生成和结构推理方面存在共性，因此该研究对开发用于化学信息学（如逆合成规划、分子设计）的“化学大模型”具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have achieved remarkable success in code generation, they often struggle with the deep, long-horizon reasoning required for complex software engineering. We attribute this limitation to the nature of standard pre-training data: static software repositories represent only the terminal state of an intricate intellectual process, abstracting away the intermediate planning, debugging, and iterative refinement. To bridge this gap, we propose a novel paradigm: understanding via reconstruction. We hypothesize that reverse-engineering the latent agentic trajectories -- the planning, reasoning, and debugging steps -- behind static repositories provides a far richer supervision signal than raw code alone. To operationalize this, we introduce a framework that synthesizes these trajectories using a multi-agent simulation. This process is grounded in the structural realities of the source repositories (e.g., dependency graphs and file hierarchies) to ensure fidelity. Furthermore, to guarantee the logical rigor of the synthetic data, we employ a search-based optimization technique that iteratively refines the Chain-of-Thought (CoT) reasoning to maximize the likelihood of the ground-truth code. Empirical results demonstrate that continuous pre-training on these reconstructed trajectories significantly enhances Llama-3-8B's performance across diverse benchmarks, including long-context understanding, coding proficiency, and agentic capabilities.

</details>

---

### 82. [Multimodal OCR: Parse Anything from Documents](https://arxiv.org/abs/2603.13032)

**基本信息**

- 🔗 arXiv: [`2603.13032`](https://arxiv.org/abs/2603.13032)
- 👥 作者: Handong Zheng, Yumeng Li, Kaile Zhang 等25人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13032.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了一个用于解析文档中文本和图形的多模态OCR框架和模型，并构建了相应的数据引擎。这为化学信息学和质谱分析领域提供了从科学文献中自动化提取结构化信息（如分子结构、谱图、数据表格）的强大工具和潜在数据集（标准2）。同时，该研究关于多模态文档理解的方向，对于构建能够处理化学多模态数据（文本+结构图+谱图）的大模型具有重要的相关性和前瞻性讨论价值（标准3）。

**📖 中文摘要**

本文提出了多模态OCR（MOCR）范式，将文档中的文本和图形（如图表、表格、图标）联合解析为统一的文本表示。与仅关注文本识别的传统OCR不同，该方法将视觉元素视为一等解析目标，从而在解析文档时保留跨元素的语义关系。论文构建了一个从PDF、渲染的网页和原生SVG资产中提取的综合数据引擎，并通过分阶段预训练和监督微调训练了一个紧凑的3B参数模型（称为 this http URL ）。评估表明，该模型在文档解析和结构化图形解析任务上均表现出色。这项工作展示了构建大规模图像到代码语料库用于多模态预训练的可扩展路径。对于化学信息学和质谱分析，该技术可用于解析科学文献中的化学结构图、反应示意图、质谱谱图以及包含复杂表格数据的实验部分，从而为构建领域特定的多模态大模型（能够理解化学图形和文本）提供数据和技术基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Multimodal OCR (MOCR), a document parsing paradigm that jointly parses text and graphics into unified textual representations. Unlike conventional OCR systems that focus on text recognition and leave graphical regions as cropped pixels, our method, termed this http URL , treats visual elements such as charts, diagrams, tables, and icons as first-class parsing targets, enabling systems to parse documents while preserving semantic relationships across elements. It offers several advantages: (1) it reconstructs both text and graphics as structured outputs, enabling more faithful document reconstruction; (2) it supports end-to-end training over heterogeneous document elements, allowing models to exploit semantic relations between textual and visual components; and (3) it converts previously discarded graphics into reusable code-level supervision, unlocking multimodal supervision embedded in existing documents. To make this paradigm practical at scale, we build a comprehensive data engine from PDFs, rendered webpages, and native SVG assets, and train a compact 3B-parameter model through staged pretraining and supervised fine-tuning. We evaluate this http URL from two perspectives: document parsing and structured graphics parsing. On document parsing benchmarks, it ranks second only to Gemini 3 Pro on our OCR Arena Elo leaderboard, surpasses existing open-source document parsing systems, and sets a new state of the art of 83.9 on olmOCR Bench. On structured graphics parsing, our model achieves higher reconstruction quality than Gemini 3 Pro across image-to-SVG benchmarks, demonstrating strong performance on charts, UI layouts, scientific figures, and chemical diagrams. These results show a scalable path toward building large-scale image-to-code corpora for multimodal pretraining. Code and models are publicly available at this https URL .

</details>

---

### 83. [To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation](https://arxiv.org/abs/2603.15159)

**基本信息**

- 🔗 arXiv: [`2603.15159`](https://arxiv.org/abs/2603.15159)
- 👥 作者: Yitong Zhang, Chengze Li, Ruize Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15159.pdf)

**💡 相关性分析**

满足标准3：论文的核心是解决让LLM有效利用私有API/工具库的问题。虽然应用场景是通用代码生成，但其提出的通过合成数据教导模型使用特定工具的方法论，对于构建能够调用化学信息学工具、质谱分析软件或数据库的“化学大模型”或“质谱分析助手”具有非常重要的相关性和前瞻性指导意义。

**📖 中文摘要**

本文针对私有库导向的代码生成任务，提出了PriCoder方法，通过自动合成数据来教导大型语言模型（LLM）调用私有库API。现有方法主要依赖于在推理时检索私有库API文档并将相关知识注入上下文，但研究表明这并不足够。PriCoder将私有库数据合成建模为图的构建，并交替使用两个图算子：（1）渐进图演化，从基本样本逐步合成更多样化的训练样本；（2）多维图剪枝，通过严格的过滤流程提高数据质量。实验表明，PriCoder显著提高了私有库导向的代码生成能力。虽然论文聚焦于代码生成，但其核心问题——如何让AI模型有效利用特定领域（私有）的API或知识库——与化学信息学和质谱分析高度相关。例如，让化学大模型调用专业的化学信息学工具包（如RDKit）、质谱数据库搜索API或光谱模拟软件，是构建实用化学AI助手的关键。PriCoder提供的方法论（通过合成数据教导模型使用特定工具）可直接应用于教导化学大模型使用领域专用工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability. Our code and benchmarks are publicly available at this https URL .

</details>

---

### 84. [Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences](https://arxiv.org/abs/2603.16313)

**基本信息**

- 🔗 arXiv: [`2603.16313`](https://arxiv.org/abs/2603.16313)
- 👥 作者: Hugo Math
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16313.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（利用大语言模型和序列建模框架进行高维事件序列的预测、发现和推理）与“化学大模型”和“质谱结构推理”主题直接相关。其提出的将复杂序列数据视为语言并用LLM进行建模和解释的范式，为构建用于质谱解析的化学大模型提供了方法论上的参考。

**📖 中文摘要**

论文提出了一种用于高维事件序列（如车辆诊断故障码）的统一框架，将事件序列建模、因果发现和大语言模型（LLM）整合在一起。该框架旨在实现从预测到因果理解再到推理的渐进式过渡。虽然论文主要关注汽车诊断，但其核心方法——利用Transformer架构进行预测性维护、可扩展的因果发现以及使用多智能体系统自动合成布尔规则——与化学信息学和质谱分析领域高度相关。具体而言，论文中提出的“将诊断序列视为一种可以建模、预测和解释的语言”的范式转变，以及利用LLM进行自动化规则合成的思想，可以直接应用于质谱数据的结构推理任务。例如，质谱图可以视为一种由碎片离子峰组成的“事件序列”，该框架可用于学习谱图与分子结构之间的复杂依赖关系，并可能自动推导出结构解析规则。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>

---

### 85. [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](https://arxiv.org/abs/2603.17380)

**基本信息**

- 🔗 arXiv: [`2603.17380`](https://arxiv.org/abs/2603.17380)
- 👥 作者: Shuizhou Chen, Lang Yu, Kedu Jin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17380.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于生物系统的大规模基础模型（SCALE），其架构基于LLaMA等大语言模型。这直接体现了“化学大模型”主题中关于构建领域专用大型模型的思想和方法。该模型的设计理念和技术路线可为化学信息学领域构建类似的大模型提供借鉴。

**📖 中文摘要**

论文提出了SCALE，一个用于虚拟细胞扰动预测的大规模基础模型。该模型将扰动预测表述为条件传输问题，并使用一个结合了LLaMA编码器和端点导向监督的集合感知流架构来实现。虽然应用领域是计算生物学，但该模型的核心技术创新——利用基于LLaMA的编码器进行细胞编码，以及构建可扩展的基础模型框架——与“化学大模型”的主题高度契合。在化学领域，类似的架构和思想可以迁移用于构建预测分子性质、反应结果或质谱谱图的通用大模型。此外，论文强调的“可扩展基础设施、稳定传输建模和生物学忠实评估的协同设计”理念，对于开发面向化学和质谱分析的大模型同样具有重要的指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Virtual cell models aim to enable in silico experimentation by predicting how cells respond to genetic, chemical, or cytokine perturbations from single-cell measurements. In practice, however, large-scale perturbation prediction remains constrained by three coupled bottlenecks: inefficient training and inference pipelines, unstable modeling in high-dimensional sparse expression space, and evaluation protocols that overemphasize reconstruction-like accuracy while underestimating biological fidelity. In this work we present a specialized large-scale foundation model SCALE for virtual cell perturbation prediction that addresses the above limitations jointly. First, we build a BioNeMo-based training and inference framework that substantially improves data throughput, distributed scalability, and deployment efficiency, yielding 12.51* speedup on pretrain and 1.29* on inference over the prior SOTA pipeline under matched system settings. Second, we formulate perturbation prediction as conditional transport and implement it with a set-aware flow architecture that couples LLaMA-based cellular encoding with endpoint-oriented supervision. This design yields more stable training and stronger recovery of perturbation effects. Third, we evaluate the model on Tahoe-100M using a rigorous cell-level protocol centered on biologically meaningful metrics rather than reconstruction alone. On this benchmark, our model improves PDCorr by 12.02% and DE Overlap by 10.66% over STATE. Together, these results suggest that advancing virtual cells requires not only better generative objectives, but also the co-design of scalable infrastructure, stable transport modeling, and biologically faithful evaluation.

</details>

---

### 86. [Cell-cell Communication Inference and Analysis: Biological Mechanisms, Computational Approaches, and Future Opportunities](https://arxiv.org/abs/2512.03497)

**基本信息**

- 🔗 arXiv: [`2512.03497`](https://arxiv.org/abs/2512.03497)
- 👥 作者: Xiangzheng Cheng, Haili Huang, Ye Su 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03497.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对细胞间通讯推断这一领域的综述，系统性地回顾和分类了超过140种计算方法。这种对某个领域计算方法进行全面梳理和展望的综述形式，与“化学大模型”和“质谱结构推理”领域对方法学进行总结和展望的需求是类似的，提供了重要的相关讨论和领域视角。

**📖 中文摘要**

论文是关于从单细胞和空间组学数据中推断和分析细胞间通讯（CCC）的计算方法的综述。它介绍了CCC的生物学机制和建模策略，并重点概述了140多种从单细胞和空间转录组数据推断CCC的计算方法，强调了方法框架和生物学问题的多样性。虽然领域是计算生物学，但论文中系统梳理的“整合先验知识（如配体-受体相互作用）或通过从头计算方法”的技术路线，与化学信息学中整合已知化学反应规则或从头学习分子转化规律的研究范式相通。此外，对大量计算方法进行系统性分类和总结的综述工作本身，为如何组织和发展“化学大模型”或“质谱结构推理”领域的计算方法生态提供了范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In multicellular organisms, cells coordinate their activities through cell-cell communication (CCC), which is crucial for development, tissue homeostasis, and disease progression. Recent advances in single-cell and spatial omics technologies provide unprecedented opportunities to systematically infer and analyze CCC from these omics data, either by integrating prior knowledge of ligand-receptor interactions (LRIs) or through de novo approaches. A variety of computational methods have been developed, focusing on methodological innovations, accurate modeling of complex signaling mechanisms, and investigation of broader biological questions. These advances have greatly enhanced our ability to analyze CCC and generate biological hypotheses. Here, we introduce the biological mechanisms and modeling strategies of CCC, and provide a focused overview of more than 140 computational methods for inferring CCC from single-cell and spatial transcriptomic data, emphasizing the diversity in methodological frameworks and biological questions. Finally, we discuss the current challenges and future opportunities in this rapidly evolving field, and summarize available methods in an interactive online resource ( this https URL ) to facilitate more efficient method comparison and selection.

</details>

---

### 87. [Generalization of Long-Range Machine Learning Potentials in Complex Chemical Spaces](https://arxiv.org/abs/2512.10989)

**基本信息**

- 🔗 arXiv: [`2512.10989`](https://arxiv.org/abs/2512.10989)
- 👥 作者: Michal Sanocki, Julija Zavadlav
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10989.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升机器学习原子间势（MLIP）在复杂化学空间中的泛化能力，这直接关系到构建通用、可靠的“化学大模型”。论文提出的评估框架和关于长程相互作用重要性的结论，对于设计和训练化学领域的基础模型具有重要参考价值。

**📖 中文摘要**

论文系统地评估了不同具有长程修正的机器学习原子间势（MLIP）架构在多样化化学空间中的泛化能力。研究表明，长程建模方案对于实现可泛化的MLIP至关重要，不仅能提高分布内性能，更重要的是能显著提升对化学空间未见区域的迁移能力。论文引入了有偏的训练-测试分割策略来严格评估模型在化学空间不同区域的性能。虽然主要应用在金属-有机框架材料上，但其关于机器学习势函数在复杂化学空间中泛化问题的研究，与“化学大模型”的主题紧密相关。构建能够准确、稳健地跨越广阔化学空间的分子表示和势函数模型，是化学大模型的核心挑战之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vastness of chemical space makes generalization a central challenge in the development of machine learning interatomic potentials (MLIPs). While MLIPs could enable large-scale atomistic simulations with near-quantum accuracy, their usefulness is often limited by poor transferability to out-of-distribution samples. Here, we systematically evaluate different MLIP architectures with long-range corrections across diverse chemical spaces and show that such schemes are essential, not only for improving in-distribution performance but, more importantly, for enabling significant gains in transferability to unseen regions of chemical space. To enable a more rigorous benchmarking, we introduce biased train-test splitting strategies, which explicitly test the model performance in significantly different regions of chemical space. Together, our findings highlight the importance of long-range modeling for achieving generalizable MLIPs and provide a framework for diagnosing systematic failures across chemical space. Although we demonstrate our methodology on metal-organic frameworks, it is broadly applicable to other materials, offering insights into the design of more robust and transferable MLIPs.

</details>

---

### 88. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是整合机器学习、高性能计算和量子计算来推动下一代药物发现，这直接涉及构建下一代“化学大模型”所需的技术栈和计算范式。论文中关于量子计算加速数据生成、机器学习模型实现量子精度模拟的讨论，为化学大模型的发展指明了前沿方向。

**📖 中文摘要**

论文探讨了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何为下一代药物发现带来变革。它详细阐述了高性能量子计算（HPQC）如何利用混合QPU-GPU架构，最终成为量子化学数据的加速器，从而实现真正的化学精度。论文将机器学习基础模型（如FeNNix-Bio1）定位为连接量子精度与计算可扩展性的关键。虽然焦点是药物发现，但其中关于整合量子力学、机器学习和高性能计算以突破计算瓶颈的论述，与“化学大模型”的愿景高度一致。构建能够进行高精度量子化学计算的化学大模型，正是该融合趋势的目标之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

## 📊 数据统计
- 累计运行天数：46
- 累计论文数量：3321

## 📝 历史记录

> 暂无历史数据

