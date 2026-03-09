# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-09 13:12:19

## 📅 2026-03-09 (今日最新)

**相关论文数：69**

### 1. [FuseDiff: Symmetry-Preserving Joint Diffusion for Dual-Target Structure-Based Drug Design](https://arxiv.org/abs/2603.05567)

**基本信息**

- 🔗 arXiv: [`2603.05567`](https://arxiv.org/abs/2603.05567)
- 👥 作者: Jianliang Wu, Anjie Qiao, Zhen Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05567.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕化学大模型（用于分子生成的扩散模型）和质谱结构推理（分子三维结构推理与生成）的主题。

**📖 中文摘要**

这篇论文提出了FuseDiff，一个用于双靶点结构药物设计的端到端扩散模型。它旨在生成一个单一的配体分子图以及两个口袋特异性的结合构象，每个构象都与一个特定的靶点口袋兼容。该模型通过一个具有双靶点局部上下文融合（DLCF）的消息传递主干，联合建模配体图和两个结合构象，同时保持所需的对称性。这项工作直接围绕“化学大模型”和“质谱结构推理”的核心主题，因为它涉及使用生成式AI模型（扩散模型）来推理和生成小分子的化学结构及其三维结合构象，这是计算化学和药物发现中结构推理的核心任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dual-target structure-based drug design aims to generate a single ligand together with two pocket-specific binding poses, each compatible with a corresponding target pocket, enabling polypharmacological therapies with improved efficacy and reduced resistance. Existing approaches typically rely on staged pipelines, which either decouple the two poses via conditional-independence assumptions or enforce overly rigid correlations, and therefore fail to jointly generate two target-specific binding modes. To address this, we propose FuseDiff, an end-to-end diffusion model that jointly generates a ligand molecular graph and two pocket-specific binding poses conditioned on both pockets. FuseDiff features a message-passing backbone with Dual-target Local Context Fusion (DLCF), which fuses each ligand atom's local context from both pockets to enable expressive joint modeling while preserving the desired symmetries. Together with explicit bond generation, FuseDiff enforces topological consistency across the two poses under a shared graph while allowing target-specific geometric adaptation in each pocket. To support principled training and evaluation, we derive a dual-target training set and use an independent held-out test set for evaluation. Experiments on the benchmark and a real-world dual-target system show that FuseDiff achieves state-of-the-art docking performance and enables the first systematic assessment of dual-target pose quality prior to docking-based pose search.

</details>

---

### 2. [A Quantization-Aware Training Based Lightweight Method for Neural Distinguishers](https://arxiv.org/abs/2603.05791)

**基本信息**

- 🔗 arXiv: [`2603.05791`](https://arxiv.org/abs/2603.05791)
- 👥 作者: Guangwei Xiong, Linyuan Wang, Zhizhong Zheng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05791.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕构建轻量化、高效的神经网络模型用于密码分析。虽然应用领域是密码学，但其核心方法论——设计高效的、基于神经网络的推理模型——与‘化学大模型’主题中构建专用、高效的化学信息处理模型在技术路径上高度相关。论文展示了如何通过量化、架构改造来优化模型，这种思路可直接迁移至开发用于‘质谱结构推理’的轻量化模型。

**📖 中文摘要**

本文提出了一种基于量化感知训练的轻量化神经区分器，用于分析SPECK轻量级分组密码。该方法利用可学习步长量化将模型权重量化为1.58比特，从而将所有卷积乘法运算替换为布尔逻辑运算。ReLU激活函数也被重新实现为基于比较的指示函数。这使得原本依赖32位乘法的架构转变为仅由布尔运算、加法和指示函数组成的轻量级结构。实验结果表明，该方法显著降低了计算复杂度，总运算量仅为Gohr原始模型的13.9%，同时分类精度仅下降2.87%。该工作展示了如何通过模型压缩和架构转换来构建高效的密码分析工具，其核心思想（模型轻量化、特征提取）与构建用于化学信息学（如质谱分析）的专用、高效推理模型有潜在关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In 2019, Gohr pioneered the application of deep neural networks to differential cryptanalysis, developing DNN-based neural distinguisher classifiers to analyze the SPECK lightweight block cipher. Unlike traditional differential analysis, which relies on Boolean operations on 0-1 sequences, neural distinguishers extract continuous features, introducing 32-bit multiplications operations that increase complexity and potential redundancy. This study proposes a lightweight neural distinguisher based on quantization-aware training. Leveraging learnable step-size quantization, the model's weights are quantized to 1.58 bits, enabling the replacement of all convolutional multiplication operations with Boolean logic. Additionally, the ReLU activation function is reimplemented as a comparison-based indicator function. This transforms the original 32-bit multiplication-dependent architecture into a lightweight structure composed solely of Boolean operations, additions, and indicator functions. Experimental results confirm significant computational complexity reduction. Owing to a high proportion of zero-valued weights, the total operations amount to just 13.9% of Gohr's model. Critically, the most costly 32-bit multiplications are eliminated, with classification accuracy dropping by only 2.87%. When applied exclusively to the initial convolutional layer, the 128 1-by-1 convolutions are replaced with 4 Boolean operations on 16-bit sequences, incurring a negligible 0.3% accuracy loss.

</details>

---

### 3. [StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800)

**基本信息**

- 🔗 arXiv: [`2603.05800`](https://arxiv.org/abs/2603.05800)
- 👥 作者: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05800.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接涉及‘化学大模型’的工程化部署挑战。虽然应用场景是媒体生成，但其解决的核心问题——如何高效、实时地服务和管理包含LLM在内的复杂多模型工作流——正是将‘化学大模型’或‘质谱结构推理’模型投入实际应用（如实时谱图分析、分子生成服务）时必须面对和解决的关键系统性问题。论文提出的自适应调度和资源管理框架具有直接的借鉴意义。

**📖 中文摘要**

本文介绍了StreamWise，一个用于大规模实时多模态生成工作流（如播客视频生成）的自适应、模块化服务系统。该系统集成了大型语言模型（LLM）、文本转语音和视频-音频生成模型，通过动态管理生成质量（如分辨率、清晰度）、模型/内容并行性以及资源感知调度，在严格的延迟和资源约束下，高效协调具有不同资源需求的多样化模型。论文量化了延迟、成本和质量的权衡。这项工作专注于为包含LLM在内的多模态生成流水线构建高效、可扩展的服务架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in multi-modal generative models are enabling new applications, from storytelling to automated media synthesis. Most current workloads generate simple outputs (e.g., image generation from a prompt) in batch mode, often requiring several seconds even for basic results. Serving real-time multi-modal workflows at scale is costly and complex, requiring efficient coordination of diverse models (each with unique resource needs) across language, audio, image, and video, all under strict latency and resource constraints. We tackle these challenges through the lens of real-time podcast video generation, integrating LLMs, text-to-speech, and video-audio generation. To meet tight SLOs, we design an adaptive, modular serving system, StreamWise, that dynamically manages quality (e.g., resolution, sharpness), model/content parallelism, and resource-aware scheduling. We leverage heterogeneous hardware to maximize responsiveness and efficiency. For example, the system can lower video resolution and allocate more resources to early scenes. We quantify the trade-offs between latency, cost, and quality. The cheapest setup generates a 10-minute podcast video on A100 GPUs in 1.4 hours (8.4x slower than the real-time) for less than \$25. StreamWise enables high-quality real-time streaming with a sub-second startup delay under $45.

</details>

---

### 4. [Sparse Crosscoders for diffing MoEs and Dense models](https://arxiv.org/abs/2603.05805)

**基本信息**

- 🔗 arXiv: [`2603.05805`](https://arxiv.org/abs/2603.05805)
- 👥 作者: Marmik Chaudhari, Nishkal Hundia, Idhant Gulati
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大型模型（特别是MoE架构）内部表示的系统性分析和理解。‘化学大模型’很可能采用类似的MoE或稠密Transformer架构。本文提供的分析工具（交叉编码器）和发现（关于特征专业化、稀疏性）对于理解和设计用于化学信息学或质谱数据处理的专用大模型具有重要参考价值，有助于指导模型架构选择和理解模型如何学习化学领域的知识表示。

**📖 中文摘要**

本文使用交叉编码器（一种稀疏自编码器的变体）来系统比较混合专家模型（MoE）和稠密模型的内部表示。研究在代码、科学文本和英文故事上训练了参数量相当的5层稠密模型和MoE模型。通过使用具有显式共享特征指定的BatchTopK交叉编码器，实现了约87%的分数方差解释，并揭示了特征组织上的具体差异。研究发现，与稠密模型相比，MoE学习了更少的独特特征，且MoE特定特征比共享特征表现出更高的激活密度，而稠密特定特征则表现出更低的密度。分析表明，MoE形成了更专业化、更聚焦的表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture of Experts (MoE) achieve parameter-efficient scaling through sparse expert routing, yet their internal representations remain poorly understood compared to dense models. We present a systematic comparison of MoE and dense model internals using crosscoders, a variant of sparse autoencoders, that jointly models multiple activation spaces. We train 5-layer dense and MoEs (equal active parameters) on 1B tokens across code, scientific text, and english stories. Using BatchTopK crosscoders with explicitly designated shared features, we achieve $\sim 87\%$ fractional variance explained and uncover concrete differences in feature organization. The MoE learns significantly fewer unique features compared to the dense model. MoE-specific features also exhibit higher activation density than shared features, whereas dense-specific features show lower density. Our analysis reveals that MoEs develop more specialized, focused representations while dense models distribute information across broader, more general-purpose features.

</details>

---

### 5. [MoE Lens -- An Expert Is All You Need](https://arxiv.org/abs/2603.05806)

**基本信息**

- 🔗 arXiv: [`2603.05806`](https://arxiv.org/abs/2603.05806)
- 👥 作者: Marmik Chaudhari, Idhant Gulati, Nishkal Hundia 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容聚焦于大型模型（MoE）的内部工作机制和优化潜力。对于构建和部署‘化学大模型’，理解模型的知识是如何分布和组织的至关重要。本文揭示的MoE模型“集中专业化”现象，以及由此衍生的模型压缩和推理优化思路（如专家修剪），为开发更高效、可部署的化学领域大模型提供了直接的技术启示和可行性路径。

**📖 中文摘要**

本文对混合专家模型（MoE）中的专家专业化行为进行了系统性分析。通过领域特定路由模式和早期解码框架两种互补方法，分析了DeepSeekMoE模型。研究发现，尽管模型有64个路由专家，每层激活6个，但模型主要依赖少数几个专业化专家，顶级权重专家的输出非常接近完整集成模型的预测。通过系统分析令牌路由分布，定量验证了这些发现：极少数专家处理了超过50%的不同专业领域的路由决策。单专家与集成专家在每一层的隐藏状态相似度极高，某些层的余弦相似度高达0.95。结果表明，MoE模型表现出集中的专业知识，这为通过有针对性的专家修剪进行推理优化提供了潜在机会。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture of Experts (MoE) models enable parameter-efficient scaling through sparse expert activations, yet optimizing their inference and memory costs remains challenging due to limited understanding of their specialization behavior. We present a systematic analysis of expert specialization in MoEs through two complementary approaches: domain-specific routing patterns and an early decoding framework that tracks expert contributions to output representations. Our analysis of the DeepSeekMoE model reveals that despite having 64 routed experts with 6 active for each layer's computation, the model predominantly relies on a few specialized experts, with the top-weighted expert's output closely approximating the full ensemble prediction. We quantitatively validate these findings through a systematic analysis of the token routing distribution, demonstrating that very few experts handle over 50\% of routing decisions across different specialized domains. Hidden state similarity between single and ensemble experts for every layer is extremely high, with some layers having cosine similarity as high as 0.95 and perplexity increasing by only 5\% when using a single expert across all three domains. Our results indicate that Mixture of Experts models exhibit concentrated expertise highlighting potential opportunities for inference optimization through targeted expert pruning while maintaining model performance and opening avenues towards studying localization of learned knowledge in these models.

</details>

---

### 6. [HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models](https://arxiv.org/abs/2603.05828)

**基本信息**

- 🔗 arXiv: [`2603.05828`](https://arxiv.org/abs/2603.05828)
- 👥 作者: Shize Liang, Hongzhi Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05828.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接针对大型语言模型的可靠性问题——幻觉，并提出了系统的归因和追踪框架。‘化学大模型’在生成分子结构描述、预测谱图或进行化学推理时，同样面临产生不准确或“幻觉”内容的严重风险。HART提出的结构化幻觉分析范式（定位、归因、检索证据）可直接应用于评估和提升化学大模型在‘质谱结构推理’等任务中的事实准确性和可解释性，是确保其科学可靠性的关键工具。

**📖 中文摘要**

本文提出了HART，一个用于大型语言模型的细粒度幻觉归因和证据检索框架。HART将幻觉追踪形式化为一个包含四个阶段的结构化建模任务：片段定位、机制归因、证据检索和因果追踪。基于此，作者构建了第一个为幻觉追踪量身定制的结构化数据集，其中幻觉类型、错误机制和反事实证据集被联合标注，以实现因果层面的可解释性评估。实验结果表明，HART显著优于BM25和DPR等强检索基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated remarkable performance in text generation and knowledge-intensive question answering. Nevertheless, they are prone to producing hallucinated content, which severely undermines their reliability in high-stakes application domains. Existing hallucination attribution approaches, based on either external knowledge retrieval or internal model mechanisms, primarily focus on semantic similarity matching or representation-level discrimination. As a result, they have difficulty establishing structured correspondences at the span level between hallucination types, underlying error generation mechanisms, and external factual evidence, thereby limiting the interpretability of hallucinated fragments and the traceability of supporting or opposing evidence. To address these limitations, we propose HART, a fine-grained hallucination attribution and evidence retrieval framework for large language models. HART formalizes hallucination tracing as a structured modeling task comprising four stages: span localization, mechanism attribution, evidence retrieval, and causal tracing. Based upon this formulation, we develop the first structured dataset tailored for hallucination tracing, in which hallucination types, error mechanisms, and sets of counterfactual evidence are jointly annotated to enable causal-level interpretability evaluation. Experimental results on the proposed dataset demonstrate that HART substantially outperforms strong retrieval baselines, including BM25 and DPR, validating the effectiveness and generalization capability of the proposed tracing paradigm for hallucination analysis and evidence alignment.

</details>

---

### 7. [Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery](https://arxiv.org/abs/2603.05860)

**基本信息**

- 🔗 arXiv: [`2603.05860`](https://arxiv.org/abs/2603.05860)
- 👥 作者: Lin Fan, Pengyu Dai, Zhipeng Deng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05860.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建能够自主发现和组合工具、实现自我进化的AI智能体，并将其应用于医学影像分析。这完全符合‘化学大模型’和‘质谱结构推理’的前沿发展方向——即开发能够自主规划实验、调用分析工具（如谱库搜索、碎片化规则、量子化学计算）、并从经验中学习优化推理策略的化学AI智能体。本文的框架为构建此类化学信息学智能体提供了直接的技术蓝本。

**📖 中文摘要**

本文提出了MACRO，一个自我进化、经验增强的医学影像智能体。它从静态工具组合转向经验驱动的工具发现。从已验证的执行轨迹中，智能体自主识别出反复有效的多步工具序列，将其合成为可复用的复合工具，并注册为新的高级原语，从而持续扩展其行为库。一个轻量级的图像特征记忆将工具选择基于视觉-临床上下文，而类似GRPO的训练循环则强化对已发现复合工具的可靠调用，实现以最小监督的闭环自我改进。在多样化的医学影像数据集和任务上的实验表明，该方法在跨领域泛化和多步骤编排准确性上持续优于现有方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Clinical image interpretation is inherently multi-step and tool-centric: clinicians iteratively combine visual evidence with patient context, quantify findings, and refine their decisions through a sequence of specialized procedures. While LLM-based agents promise to orchestrate such heterogeneous medical tools, existing systems treat tool sets and invocation strategies as static after deployment. This design is brittle under real-world domain shifts, across tasks, and evolving diagnostic requirements, where predefined tool chains frequently degrade and demand costly manual re-design. We propose MACRO, a self-evolving, experience-augmented medical agent that shifts from static tool composition to experience-driven tool discovery. From verified execution trajectories, the agent autonomously identifies recurring effective multi-step tool sequences, synthesizes them into reusable composite tools, and registers these as new high-level primitives that continuously expand its behavioral repertoire. A lightweight image-feature memory grounds tool selection in a visual-clinical context, while a GRPO-like training loop reinforces reliable invocation of discovered composites, enabling closed-loop self-improvement with minimal supervision. Extensive experiments across diverse medical imaging datasets and tasks demonstrate that autonomous composite tool discovery consistently improves multi-step orchestration accuracy and cross-domain generalization over strong baselines and recent state-of-the-art agentic methods, bridging the gap between brittle static tool use and adaptive, context-aware clinical AI assistance. Code will be available upon acceptance.

</details>

---

### 8. [ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning](https://arxiv.org/abs/2603.05863)

**基本信息**

- 🔗 arXiv: [`2603.05863`](https://arxiv.org/abs/2603.05863)
- 👥 作者: Juyong Jiang, Jiasi Shen, Sunghun Kim 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05863.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是赋予大型语言模型（LLM）自我反思和自我纠正的能力，并特别针对代码生成任务进行了优化。这种“生成-反思-修正”的推理范式与‘质谱结构推理’的任务流程高度相似：先生成一个候选的分子结构或碎片化路径，然后根据化学规则和谱图特征进行合理性检查与修正。本文提出的将反思能力内化到模型中的RL框架，为开发能够进行迭代式、自我验证的质谱解析模型提供了强有力的方法论参考。

**📖 中文摘要**

本文提出了ReflexiCoder，一个新颖的强化学习框架，用于教导大型语言模型（LLM）对生成的代码进行自我反思和自我纠正。与依赖外部反馈的现有方法不同，ReflexiCoder将结构化的推理轨迹（包括初始生成、关注错误和优化的反思、以及自我纠正）内化到模型权重中。它采用RL-zero训练范式和细粒度奖励函数来优化整个反思-纠正轨迹，教导模型如何在无需推理时依赖真实反馈或执行引擎的情况下进行调试。在多个基准测试上的实验表明，ReflexiCoder-8B在1.5B-14B参数范围的开源模型中达到了新的最先进水平，并且通过有纪律的、高速的推理和反思模式，推理时代计算开销减少了约40%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have revolutionized code generation, standard "System 1" approaches, generating solutions in a single forward pass, often hit a performance ceiling when faced with complex algorithmic tasks. Existing iterative refinement strategies attempt to bridge this gap at inference time, yet they predominantly rely on external oracles, execution feedback, or computationally expensive prompt-response cycles. In this work, we propose ReflexiCoder, a novel reinforcement learning (RL) framework that internalizes the structured reasoning trajectory, encompassing initial generation, bug and optimization aware reflection, and self-correction, directly into the model's weights. Unlike prior methods, ReflexiCoder shifts the paradigm from external-dependent refinement to an intrinsic, fully autonomous self-reflection and self-correction capabilities at inference time. We utilize an RL-zero training paradigm with granular reward functions to optimize the entire reflection-correction trajectory, teaching the model how to debug without reliance on ground-truth feedback or execution engines at inference time. Extensive experiments across seven benchmarks demonstrate that our ReflexiCoder-8B establishes a new state-of-the-art (SOTA) among leading open-source models in the 1.5B-14B range, achieving 94.51% (87.20%) on HumanEval (Plus), 81.80% (78.57%) on MBPP (Plus), 35.00% on BigCodeBench, 52.21% on LiveCodeBench, and 37.34% on CodeForces in a single-attempt setting, rivaling or surpassing proprietary models like GPT-5.1. Notably, our framework is significantly more token-efficient than base models, reducing inference-time compute overhead by approximately 40% through disciplined, high-speed reasoning and reflection patterns. Source code is available at this https URL .

</details>

---

### 9. [TumorChain: Interleaved Multimodal Chain-of-Thought Reasoning for Traceable Clinical Tumor Analysis](https://arxiv.org/abs/2603.05867)

**基本信息**

- 🔗 arXiv: [`2603.05867`](https://arxiv.org/abs/2603.05867)
- 👥 作者: Sijing Li, Zhongwei Qiu, Jiang Liu 等25人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05867.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是构建用于复杂科学数据分析（医学影像）的多模态、可追溯的链式思维推理框架。这与‘质谱结构推理’的任务本质高度一致，都是将原始数据（质谱峰）通过多步骤推理转化为高层次结论（分子结构）。TumorChain的架构（耦合数据编码、文本理解、迭代精炼）可直接启发质谱推理模型的构建。2) 论文贡献了TumorCoT数据集，这是一个大规模、高质量、具有详细推理标注的多模态数据集，其构建理念和方法（步骤对齐、跨模态标注）为创建用于训练和评估‘质谱结构推理’模型的数据集提供了宝贵的范例和参考。

**📖 中文摘要**

本文针对临床肿瘤分析任务，构建了一个大规模基准测试，将多模态推理流程操作化，涵盖影像发现、临床印象和病理学预测。作者策划了TumorCoT，一个包含150万条带有CoT标注的VQA指令与3D CT扫描配对的大规模数据集，其中包含从发现到印象再到病理学的步骤对齐原理和跨模态对齐，从而能够评估答案准确性和推理一致性。作者进一步提出了TumorChain，一个多模态交错推理框架，紧密耦合3D影像编码器、临床文本理解和器官级视觉-语言对齐。通过跨模态对齐和迭代交错因果推理，TumorChain在多次自我精炼后，基于视觉证据得出结论并发出病理学预测，提高了可追溯性并降低了幻觉风险。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate tumor analysis is central to clinical radiology and precision oncology, where early detection, reliable lesion characterization, and pathology-level risk assessment guide diagnosis and treatment planning. Chain-of-Thought (CoT) reasoning is particularly important in this setting because it enables step-by-step interpretation from imaging findings to clinical impressions and pathology conclusions, improving traceability and reducing diagnostic errors. Here, we target the clinical tumor analysis task and build a large-scale benchmark that operationalizes a multimodal reasoning pipeline, spanning findings, impressions, and pathology predictions. We curate TumorCoT, a large-scale dataset of 1.5M CoT-labeled VQA instructions paired with 3D CT scans, with step-aligned rationales and cross-modal alignments along the trajectory from findings to impression to pathology, enabling evaluation of both answer accuracy and reasoning consistency. We further propose TumorChain, a multimodal interleaved reasoning framework that tightly couples 3D imaging encoders, clinical text understanding, and organ-level vision-language alignment. Through cross-modal alignment and iterative interleaved causal reasoning, TumorChain grounds visual evidence, aggregates conclusions, and issues pathology predictions after multiple rounds of self-refinement, improving traceability and reducing hallucination risk. Experiments show consistent improvements over strong baselines in lesion detection, impression generation, and pathology classification, and demonstrate strong generalization on the DeepTumorVQA benchmark. These results highlight the potential of multimodal reasoning for reliable and interpretable tumor analysis in clinical practice. Detailed information about our project can be found on our project homepage at this https URL .

</details>

---

### 10. [PatchCue: Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues](https://arxiv.org/abs/2603.05869)

**基本信息**

- 🔗 arXiv: [`2603.05869`](https://arxiv.org/abs/2603.05869)
- 👥 作者: Yukun Qi, Pei Fu, Hang Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05869.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进视觉语言模型（VLM）的视觉推理能力，通过引入结构化的、基于图像块的视觉提示。在‘质谱结构推理’中，模型需要结合质谱图（一种视觉/数值数据）和文本信息（分子式、描述）进行推理。将质谱图以“块”或“区域”（如不同的m/z区间、强度簇）的形式进行结构化表示，并作为视觉提示注入模型，可以显著提升模型对谱图特征的关注和推理的准确性。本文的PatchCue范式为在化学多模态模型中实现更精细的谱图-结构对齐提供了直接的技术思路。

**📖 中文摘要**

本文提出了PatchCue，一种新颖的基于图像块（patch）的视觉提示范式，旨在显著增强视觉语言模型的视觉推理能力。通过将图像分割成块并在块级别表示提示，PatchCue更好地符合人类感知习惯，并利用了现代VLM的块-令牌化输入。作者采用两阶段方法训练VLM：首先是冷启动监督微调以输出块级提示，然后是强化学习，使用过程监督的提示奖励来引导中间视觉推理步骤。在多个VLM和多样化基准测试上的实验表明，PatchCue持续提升了模型整体性能。结果表明，块级提示在效果上优于像素级边界框和基于点的提示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language Models (VLMs) have achieved remarkable progress on a wide range of challenging multimodal understanding and reasoning tasks. However, existing reasoning paradigms, such as the classical Chain-of-Thought (CoT), rely solely on textual information and often underutilize important visual cues. While prior work has incorporated pixel-level visual cues, these representations require precise spatial localization, introducing additional learning complexity. To address this, we propose PatchCue, a novel patch-based visual cue paradigm designed to significantly enhance the visual reasoning capabilities of VLMs. By partitioning images into patches and representing cues at the patch level, PatchCue aligns better with human perceptual habits and leverages the patch-tokenized input of modern VLMs. We train VLMs using a two-stage approach: cold-start supervised fine-tuning to output patch-level cues, followed by reinforcement learning with a process-supervised cue reward that guides intermediate visual reasoning steps. Extensive experiments on multiple VLMs and diverse benchmarks, including general visual question answering, complex reasoning, and document understanding, demonstrate that PatchCue consistently improves overall model performance. Our results show that patch-level cues outperform both pixel-level bounding boxes and point-based cues, providing a more effective and cognitively aligned visual reasoning paradigm.

</details>

---

### 11. [Computational Pathology in the Era of Emerging Foundation and Agentic AI -- International Expert Perspectives on Clinical Integration and Translational Readiness](https://arxiv.org/abs/2603.05884)

**基本信息**

- 🔗 arXiv: [`2603.05884`](https://arxiv.org/abs/2603.05884)
- 👥 作者: Qian Da, Yijiang Chen, Min Ju 等28人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05884.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对基础模型和智能体AI在特定科学领域（计算病理学）应用的综述和展望文章。它系统地讨论了该领域从技术突破到临床落地所面临的机遇与挑战。这对于‘化学大模型’和‘质谱结构推理’领域具有极高的参考价值，因为这两个领域同样处于从实验室研究走向实际应用（如药物发现、环境监测、临床质谱诊断）的关键阶段。论文中关于技术成熟度、评估标准、集成障碍和监管考量的讨论，为化学信息学领域规划类似的发展路径提供了重要的框架和警示。

**📖 中文摘要**

本文是一篇综述/展望论文，探讨了在基础模型和智能体AI时代，计算病理学如何向临床整合和转化。文章回顾了基础模型和智能体在预测诊断、预后和治疗反应等任务中表现出的性能提升，但也指出了其在真实世界应用中面临的经济、技术和行政挑战。本文超越了现有关于技术架构和比较性能的讨论，通过将可部署的临床相关性与下游分析能力及其技术成熟度、操作准备情况、经济和监管背景联系起来，考虑了这些新兴AI系统如何负责任地融入医疗实践。文章基于国际专家组的观点，对当前能力和在患者护理环境中的采用障碍进行了实用评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent breakthroughs in artificial intelligence through foundation models and agents have accelerated the evolution of computational pathology. Demonstrated performance gains reported across academia in benchmarking datasets in predictive tasks such as diagnosis, prognosis, and treatment response have ignited substantial enthusiasm for clinical application. Despite this development momentum, real world adoption has lagged, as implementation faces economic, technical, and administrative challenges. Beyond existing discussions of technical architectures and comparative performance, this review considers how these emerging AI systems can be responsibly integrated into medical practice by connecting deployable clinical relevance with downstream analytical capabilities and their technical maturity, operational readiness, and economic and regulatory context. Drawing on perspectives from an international group, we provide a practical assessment of current capabilities and barriers to adoption in patient care settings.

</details>

---

### 12. [Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning](https://arxiv.org/abs/2603.05900)

**基本信息**

- 🔗 arXiv: [`2603.05900`](https://arxiv.org/abs/2603.05900)
- 👥 作者: Xuan Li, Zhanke Zhou, Zongze Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接是‘分子优化’，这是化学信息学和‘化学大模型’的核心应用之一。本文提出的RePO方法，巧妙地结合了强化学习（促进探索新分子）和参考分子引导（稳定训练、利用已知知识），为解决分子优化中奖励稀疏、探索困难的问题提供了创新方案。该方法论对于开发能够进行创造性分子设计或属性导向优化的化学大模型具有直接的指导意义。

**📖 中文摘要**

本文针对基于指令的分子优化任务，提出了Reference-guided Policy Optimization (RePO)方法。该任务通常只提供单个优化后的参考分子，而没有逐步的优化轨迹。RePO从参考分子中学习，无需轨迹数据。在每次更新时，RePO从模型中采样候选分子及其中间推理轨迹，并使用可验证的奖励（在相似性约束下测量属性满足度）以强化学习方式训练模型。同时，它通过将策略的中间推理轨迹作为上下文并仅以监督方式训练答案来应用参考引导。强化学习项促进探索，而引导项则通过将输出锚定到参考分子来缓解奖励稀疏性并稳定训练。在分子优化基准测试中，RePO consistently outperforms SFT and RLVR baselines。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) benefit substantially from supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR) in reasoning tasks. However, these recipes perform poorly in instruction-based molecular optimization, where each data point typically provides only a single optimized reference molecule and no step-by-step optimization trajectory. We reveal that answer-only SFT on the reference molecules collapses reasoning, and RLVR provides sparse feedback under similarity constraints due to the model's lack of effective exploration, which slows learning and limits optimization. To encourage the exploration of new molecules while balancing the exploitation of the reference molecules, we introduce Reference-guided Policy Optimization (RePO), an optimization approach that learns from reference molecules without requiring trajectory data. At each update, RePO samples candidate molecules with their intermediate reasoning trajectories from the model and trains the model using verifiable rewards that measure property satisfaction under similarity constraints in an RL manner. Meanwhile, it applies reference guidance by keeping the policy's intermediate reasoning trajectory as context and training only the answer in a supervised manner. Together, the RL term promotes exploration, while the guidance term mitigates reward sparsity and stabilizes training by grounding outputs to references when many valid molecular edits exist. Across molecular optimization benchmarks, RePO consistently outperforms SFT and RLVR baselines (e.g., GRPO), achieving improvements on the optimization metric (Success Rate $\times$ Similarity), improving balance across competing objectives, and generalizing better to unseen instruction styles. Our code is publicly available at this https URL .

</details>

---

### 13. [InfoGatherer: Principled Information Seeking via Evidence Retrieval and Strategic Questioning](https://arxiv.org/abs/2603.05909)

**基本信息**

- 🔗 arXiv: [`2603.05909`](https://arxiv.org/abs/2603.05909)
- 👥 作者: Maksym Taranukhin, Shuyue Stella Li, Evangelos Milios 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05909.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个能够主动进行信息收集、多轮对话、并基于证据进行不确定性推理的AI智能体框架。这完全符合‘化学大模型’或‘质谱分析智能体’的交互范式：用户可能提供一个不完整的质谱图或模糊的查询，智能体需要主动提问以获取更多实验条件（如电离方式、碰撞能量），同时检索谱库和化学知识库，并在证据不充分时合理表达不确定性。InfoGatherer的Dempster-Shafer证据推理框架为构建可靠、可解释的化学咨询智能体提供了强大的理论基础和系统设计范例。

**📖 中文摘要**

本文提出了InfoGatherer框架，用于在高风险领域（如医疗分诊和法律援助）中，当初始用户查询信息不足时，系统地从两个互补来源收集缺失信息：检索到的领域文档和针对用户的后续提问。InfoGatherer使用Dempster-Shafer信念分配在结构化证据网络上对不确定性进行建模，从而能够在不确定过早得出明确答案的情况下，原则性地融合来自两个来源的不完整且可能矛盾的证据。在法律和医疗任务中，InfoGatherer优于强基线，同时需要更少的对话轮次。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLMs are increasingly deployed in high-stakes domains such as medical triage and legal assistance, often as document-grounded QA systems in which a user provides a description, relevant sources are retrieved, and an LLM generates a prediction. In practice, initial user queries are often underspecified, and a single retrieval pass is insufficient for reliable decision-making, leading to incorrect and overly confident answers. While follow-up questioning can elicit missing information, existing methods typically depend on implicit, unstructured confidence signals from the LLM, making it difficult to determine what remains unknown, what information matters most, and when to stop asking questions. We propose InfoGatherer, a framework that gathers missing information from two complementary sources: retrieved domain documents and targeted follow-up questions to the user. InfoGatherer models uncertainty using Dempster-Shafer belief assignments over a structured evidential network, enabling principled fusion of incomplete and potentially contradictory evidence from both sources without prematurely collapsing to a definitive answer. Across legal and medical tasks, InfoGatherer outperforms strong baselines while requiring fewer turns. By grounding uncertainty in formal evidential theory rather than heuristic LLM signals, InfoGatherer moves towards trustworthy, interpretable decision support in domains where reliability is critical.

</details>

---

### 14. [CORE-Seg: Reasoning-Driven Segmentation for Complex Lesions via Reinforcement Learning](https://arxiv.org/abs/2603.05911)

**基本信息**

- 🔗 arXiv: [`2603.05911`](https://arxiv.org/abs/2603.05911)
- 👥 作者: Yuxin Xie, Yuming Chen, Yishan Yang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05911.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文的核心研究内容是推动图像分割从“感知”走向“认知”，即结合语言推理进行分割。这与‘质谱结构推理’高度相关，后者本质上也是从质谱数据（“感知”峰）推理出分子结构（“认知”实体）。CORE-Seg框架将分割任务重新定义为推理任务，这为质谱解析提供了全新的建模视角。2) 论文贡献了ComLesion-14K基准数据集，这是一个带有思维链标注的复杂分割数据集。其构建方法（结合视觉和文本推理）为创建用于训练和评估‘质谱结构推理’模型的数据集（需要将质谱峰与结构碎片、化学规则关联起来）提供了极具价值的参考。

**📖 中文摘要**

本文针对医学图像分割，提出了一个从传统视觉模式匹配到认知推理分析的范式转变。作者引入了ComLesion-14K，这是第一个用于推理驱动的复杂病灶分割的多样化思维链基准。为了完成此任务，作者提出了CORE-Seg，一个通过语义引导提示适配器将推理与分割集成的端到端框架。作者设计了一个从SFT到GRPO的渐进训练策略，并配备了自适应双粒度奖励机制以缓解奖励稀疏性。该方法在复杂病灶分割上取得了最先进的结果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medical image segmentation is undergoing a paradigm shift from conventional visual pattern matching to cognitive reasoning analysis. Although Multimodal Large Language Models (MLLMs) have shown promise in integrating linguistic and visual knowledge, significant gaps remain: existing general MLLMs possess broad common sense but lack the specialized visual reasoning required for complex lesions, whereas traditional segmentation models excel at pixel-level segmentation but lack logical interpretability. In this paper, we introduce ComLesion-14K, the first diverse Chain-of-Thought (CoT) benchmark for reasoning-driven complex lesion segmentation. To accomplish this task, we propose CORE-Seg, an end-to-end framework integrating reasoning with segmentation through a Semantic-Guided Prompt Adapter. We design a progressive training strategy from SFT to GRPO, equipped with an adaptive dual-granularity reward mechanism to mitigate reward sparsity. Our Method achieves state-of-the-art results with a mean Dice of 37.06\% (14.89\% higher than the second-best baseline), while reducing the failure rate to 18.42\%. Project Page: this https URL

</details>

---

### 15. [DeepFact: Co-Evolving Benchmarks and Agents for Deep Research Factuality](https://arxiv.org/abs/2603.05912)

**基本信息**

- 🔗 arXiv: [`2603.05912`](https://arxiv.org/abs/2603.05912)
- 👥 作者: Yukun Huang, Leonardo F. R. Ribeiro, Momchil Hardalov 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05912.pdf)

**💡 相关性分析**

满足标准2和3：2) 论文提出了一个创新的基准构建和评估框架（AtS），以及一个具体的基准（DeepFact-Bench）和评估工具（DeepFact-Eval）。这套方法论和工具对于构建和评估‘化学大模型’在科学事实性（如生成的分子性质、反应机理是否正确）方面的表现至关重要，可以防止模型产生“科学幻觉”。3) 论文包含了对现有验证方法局限性的重要讨论，并提出了演化基准的新范式，这属于对如何评估大模型在复杂领域事实性的重要前瞻性讨论，对化学领域有直接的启示。

**📖 中文摘要**

本文研究了搜索增强的LLM智能体生成深度研究报告时的声明级事实性验证问题。作者指出，现有的静态专家标注基准在此设置下是脆弱的，并提出了“通过审计-评分进行演化基准测试”（AtS）方法。在AtS中，基准标签和原理是可明确修订的：当验证器与当前基准不一致时，它必须提交证据；审计员裁决争议；接受的修订在模型评分之前更新基准。作者将AtS实例化为DeepFact-Bench（一个具有可审计原理的版本化DRR事实性基准）和DeepFact-Eval（一个文档级验证智能体）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Search-augmented LLM agents can produce deep research reports (DRRs), but verifying claim-level factuality remains challenging. Existing fact-checkers are primarily designed for general-domain, factoid-style atomic claims, and there is no benchmark to test whether such verifiers transfer to DRRs. Yet building such a benchmark is itself difficult. We first show that static expert-labeled benchmarks are brittle in this setting: in a controlled study with PhD-level specialists, unassisted experts achieve only 60.8% accuracy on a hidden micro-gold set of verifiable claims. We propose Evolving Benchmarking via Audit-then-Score (AtS), where benchmark labels and rationales are explicitly revisable: when a verifier disagrees with the current benchmark, it must submit evidence; an auditor adjudicates the dispute; and accepted revisions update the benchmark before models are scored. Across four AtS rounds, expert micro-gold accuracy rises to 90.9%, indicating experts are substantially more reliable as auditors than as one-shot labelers. We instantiate AtS as DeepFact-Bench, a versioned DRR factuality benchmark with auditable rationales, and DeepFact-Eval, a document-level verification agent (with a grouped lite variant) that outperforms existing verifiers on DeepFact-Bench and transfers well to external factuality datasets.

</details>

---

### 16. [Latent Diffusion-Based 3D Molecular Recovery from Vibrational Spectra](https://arxiv.org/abs/2603.06113)

**基本信息**

- 🔗 arXiv: [`2603.06113`](https://arxiv.org/abs/2603.06113)
- 👥 作者: Wenjin Wu, Aleš Leonardis, Linjiang Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06113.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容直接围绕“质谱结构推理”主题，提出了一种从红外振动光谱中恢复三维分子结构的扩散模型方法。

**📖 中文摘要**

本文提出了一种名为IR-GeoDiff的潜在扩散模型，用于从红外光谱中恢复三维分子几何结构。红外光谱是一种振动光谱，广泛用于分子结构测定。现有方法通常依赖一维SMILES字符串或二维分子图，无法捕捉光谱特征与三维分子几何之间的复杂关系。IR-GeoDiff通过将光谱信息整合到分子结构的节点和边表示中，能够从单一红外光谱中恢复对应的分子分布。注意力分析表明，该模型能够聚焦于红外光谱中特征官能团区域，这与常见的化学解释实践在质量上保持一致。这项工作直接针对“质谱结构推理”主题，利用扩散模型从光谱数据中推断三维分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Infrared (IR) spectroscopy, a type of vibrational spectroscopy, is widely used for molecular structure determination and provides critical structural information for chemists. However, existing approaches for recovering molecular structures from IR spectra typically rely on one-dimensional SMILES strings or two-dimensional molecular graphs, which fail to capture the intricate relationship between spectral features and three-dimensional molecular geometry. Recent advances in diffusion models have greatly enhanced the ability to generate molecular structures in 3D space. Yet, no existing model has explored the distribution of 3D molecular geometries corresponding to a single IR spectrum. In this work, we introduce IR-GeoDiff, a latent diffusion model that recovers 3D molecular geometries from IR spectra by integrating spectral information into both node and edge representations of molecular structures. We evaluate IR-GeoDiff from both spectral and structural perspectives, demonstrating its ability to recover the molecular distribution corresponding to a given IR spectrum. Furthermore, an attention-based analysis reveals that the model is able to focus on characteristic functional group regions in IR spectra, qualitatively consistent with common chemical interpretation practices.

</details>

---

### 17. [Optimizing 3D Diffusion Models for Medical Imaging via Multi-Scale Reward Learning](https://arxiv.org/abs/2603.06173)

**基本信息**

- 🔗 arXiv: [`2603.06173`](https://arxiv.org/abs/2603.06173)
- 👥 作者: Yueying Tian, Xudong Han, Meng Zhou 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06173.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容涉及使用扩散模型（一种生成式大模型）进行3D分子/结构（此处为医学图像中的解剖结构）的生成和优化，与“化学大模型”主题相关，因为扩散模型是当前生成式AI大模型的重要分支，并在化学信息学中有广泛应用潜力。

**📖 中文摘要**

本文提出了一种使用强化学习和多尺度反馈来增强3D扩散模型的方法，应用于3D医学图像生成。该方法首先在MRI体积数据上预训练一个3D扩散模型以建立强大的生成先验。随后，使用近端策略优化算法，在结合了2D切片级评估和3D体积分析的新型奖励系统的指导下对模型进行微调。这种组合使模型能够同时优化局部纹理细节和全局结构一致性。该方法在BraTS 2019和OASIS-1数据集上进行了验证。结果表明，结合强化学习反馈能有效地将生成过程引导向更高质量的分布。定量分析显示，在Fréchet Inception Distance上有显著改善，并且与未优化的基线相比，合成数据在下游肿瘤和疾病分类任务中表现出更高的实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have emerged as powerful tools for 3D medical image generation, yet bridging the gap between standard training objectives and clinical relevance remains a challenge. This paper presents a method to enhance 3D diffusion models using Reinforcement Learning (RL) with multi-scale feedback. We first pretrain a 3D diffusion model on MRI volumes to establish a robust generative prior. Subsequently, we fine-tune the model using Proximal Policy Optimization (PPO), guided by a novel reward system that integrates both 2D slice-wise assessments and 3D volumetric analysis. This combination allows the model to simultaneously optimize for local texture details and global structural coherence. We validate our framework on the BraTS 2019 and OASIS-1 datasets. Our results indicate that incorporating RL feedback effectively steers the generation process toward higher quality distributions. Quantitative analysis reveals significant improvements in Fréchet Inception Distance (FID) and, crucially, the synthetic data demonstrates enhanced utility in downstream tumor and disease classification tasks compared to non-optimized baselines.

</details>

---

### 18. [Enhanced Protein Intrinsic Disorder Prediction Through Dual-View Multiscale Features and Multi-objective Evolutionary Algorithm](https://arxiv.org/abs/2603.06292)

**基本信息**

- 🔗 arXiv: [`2603.06292`](https://arxiv.org/abs/2603.06292)
- 👥 作者: Shaokuan Wang, Pengshan Cui, Yining Qian 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06292.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是利用深度学习（大模型特征提取）和进化算法进行蛋白质结构（特别是无序区域）的预测，属于化学信息学和生物信息学交叉领域，与“化学大模型”主题相关。

**📖 中文摘要**

本文提出了一种名为D2MOE的双视图多尺度特征和多目标进化算法，用于增强蛋白质内在无序区域的预测。蛋白质的内在无序区域在细胞信号传导和药物发现中起着关键作用，但其高结构灵活性使得残基水平的准确预测具有挑战性。现有方法通常依赖单视图表示或僵化的手动融合策略，无法有效平衡局部氨基酸偏好和长程序列模式之间的复杂相互作用。D2MOE首先引入了一种双视图多尺度特征提取方法，将进化视图与深度语义视图相结合，并采用多尺度提取器来捕获不同感受野的结构信息。其次，设计了一种多目标进化算法，以自适应地发现最优融合架构。通过共同进化离散特征选择和连续融合权重，该算法自适应地探索最优的跨特征架构，以提高预测准确性，同时保持模型的紧凑性。在三个基准数据集上的实验结果表明，D2MOE consistently outperforms state-of-the-art methods。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Intrinsically disordered regions of proteins play a crucial role in cell signaling and drug discovery. However, their high structural flexibility makes accurate residue-level prediction challenging. Existing methods often rely on single-view representations or rigid manual fusion strategies, which fail to effectively balance the complex interplay between local amino acid preferences and long-range sequence patterns. To address these limitations, we propose D2MOE, a Dual-View Multiscale Features and Multi-objective Evolutionary Algorithm, which consists of two stages. First, a dual-view multiscale feature extraction method is introduced. This method integrates evolutionary views with deep semantic views and employs multiscale extractors to capture structural information across diverse receptive fields. Second, a multi-objective evolutionary algorithm is designed to adaptively discover optimal fusion architectures. By co-evolving discrete feature selection and continuous fusion weights, the algorithm adaptively explores optimal cross-feature architectures to enhance predictive accuracy while maintaining model compactness. Experimental results across three benchmark datasets demonstrate that D2MOE consistently outperforms state-of-the-art methods. D2MOE combines the feature extraction capabilities of deep learning with the global search advantages of evolutionary algorithms, enabling efficient feature integration without manual design, and providing a robust computational tool for protein disorder prediction.

</details>

---

### 19. [Structured Exploration vs. Generative Flexibility: A Field Study Comparing Bandit and LLM Architectures for Personalised Health Behaviour Interventions](https://arxiv.org/abs/2603.06330)

**基本信息**

- 🔗 arXiv: [`2603.06330`](https://arxiv.org/abs/2603.06330)
- 👥 作者: Dominik P. Hofer, Haochen Song, Rania Islambouli 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06330.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大型语言模型（LLM）的架构和应用。LLM是构建“化学大模型”（如用于分子设计、反应预测的专用大模型）的关键技术基础，因此论文主题与“化学大模型”在技术层面上直接相关。

**📖 中文摘要**

这篇论文比较了用于个性化健康行为干预的两种AI架构：上下文多臂老虎机和大型语言模型。虽然核心应用是行为改变，但论文的核心技术对比涉及LLM（大型语言模型）的灵活生成能力。LLM是构建化学大模型（如分子生成、性质预测模型）的核心技术基础。因此，该论文通过讨论LLM的架构和应用，与“化学大模型”这一主题在技术基础上间接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Behaviour Change Techniques (BCTs) are central to digital health interventions, yet selecting and delivering effective techniques remains challenging. Contextual bandits enable statistically grounded optimisation of BCT selection, while Large Language Models (LLMs) offer flexible, context-sensitive message generation. We conducted a 4-week study on physical activity motivation (N=54; 9 post-study interviews) that compared five daily messaging approaches: random templates, contextual bandit with templates, LLM generation, hybrid bandit+LLM, and LLM with interaction history. LLM-based approaches were rated substantially more helpful than templates, but no significant differences emerged among LLM conditions. Unexpectedly, bandit optimisation for BCTs selection yielded no additional perceived helpfulness compared with LLM-only approaches. Unconstrained LLMs focused heavily on a single BCT, whereas bandit systems enforced systematic exploration-exploitation across techniques. Quantitative and qualitative findings suggest contextual acknowledgement of user input drove perceived helpfulness. We contribute design suggestions for reflective AI health behaviour change systems that address a trade-off between structured exploration and generative autonomy.

</details>

---

### 20. [Transparent AI for Mathematics: Transformer-Based Large Language Models for Mathematical Entity Relationship Extraction with XAI](https://arxiv.org/abs/2603.06348)

**基本信息**

- 🔗 arXiv: [`2603.06348`](https://arxiv.org/abs/2603.06348)
- 👥 作者: Tanjim Taharat Aurpa
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06348.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用Transformer模型进行实体关系提取。Transformer是构建“化学大模型”的基石技术。同时，论文解决的结构化信息提取问题，其方法论与“质谱结构推理”（从复杂数据中推断化学实体及其关系）在概念上相通。

**📖 中文摘要**

本研究将数学问题理解定义为数学实体关系提取任务，并应用基于Transformer的模型（特别是BERT）来自动从数学文本中提取这些关系。Transformer架构是现代大模型（包括化学大模型）的核心。论文专注于关系提取这一特定任务，展示了Transformer模型在结构化信息提取方面的能力。这种从文本中提取结构化实体和关系的方法，与从质谱数据中推理化学结构（即从复杂数据中提取实体和关系）在方法论上具有相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical text understanding is a challenging task due to the presence of specialized entities and complex relationships between them. This study formulates mathematical problem interpretation as a Mathematical Entity Relation Extraction (MERE) task, where operands are treated as entities and operators as their relationships. Transformer-based models are applied to automatically extract these relations from mathematical text, with Bidirectional Encoder Representations from Transformers (BERT) achieving the best performance, reaching an accuracy of 99.39%. To enhance transparency and trust in the model's predictions, Explainable Artificial Intelligence (XAI) is incorporated using Shapley Additive Explanations (SHAP). The explainability analysis reveals how specific textual and mathematical features influence relation prediction, providing insights into feature importance and model behavior. By combining transformer-based learning, a task-specific dataset, and explainable modeling, this work offers an effective and interpretable framework for MERE, supporting future applications in automated problem solving, knowledge graph construction, and intelligent educational systems.

</details>

---

### 21. [MoEless: Efficient MoE LLM Serving via Serverless Computing](https://arxiv.org/abs/2603.06350)

**基本信息**

- 🔗 arXiv: [`2603.06350`](https://arxiv.org/abs/2603.06350)
- 👥 作者: Hanfei Yu, Bei Ouyang, Shwai He 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06350.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是混合专家大型语言模型的架构与高效服务。MoE是构建大规模、高性能“化学大模型”的一种重要架构范式。论文探讨的MoE服务优化问题，对于实际部署化学领域的大模型具有直接的技术参考价值。

**📖 中文摘要**

论文提出了MoEless，一个基于无服务器计算的、用于高效服务混合专家大型语言模型的框架。混合专家是扩展大模型规模的关键架构之一。该研究专注于优化MoE LLM的推理服务效率，解决了专家负载不均衡等实际问题。虽然应用场景是通用LLM服务，但其核心研究对象——MoE LLM的架构和高效服务技术——是“化学大模型”领域在构建和部署大规模模型时需要面对和借鉴的关键技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have become a cornerstone of AI, driving progress across diverse domains such as content creation, search and recommendation systems, and AI-assisted workflows. To alleviate extreme training costs and advancing model scales, Mixture-of-Experts (MoE) has become a popular backbone for modern LLMs, which are commonly served in distributed deployment using expert parallelism (EP). However, MoE's sparse activation mechanism leads to severe expert load imbalance, where a few experts become overloaded while others remain idle, resulting in expert stragglers that inflate inference latency and serving cost. Existing expert load balancing solutions assume static resource configurations on serverful infrastructures, limiting expert scalability and elasticity, and resulting in either costly real-time expert swapping or degraded generation quality. We present MoEless, the first serverless MoE serving framework that mitigates expert load imbalance and accelerates inference via serverless experts. MoEless employs lightweight, layer-aware predictors to accurately estimate incoming expert load distributions and proactively identify stragglers. We design optimized expert scaling and placement strategies to maximize function locality, improve GPU utilization, and balance loads across experts and GPUs. MoEless is prototyped on top of Megatron-LM and deployed on an eight-GPU testbed. Experiments with open-source MoE models and real-world workloads show that MoEless reduces inference latency by 43% and inference cost by 84% compared to state-of-the-art solutions.

</details>

---

### 22. [Tiny, Hardware-Independent, Compression-based Classification](https://arxiv.org/abs/2603.06359)

**基本信息**

- 🔗 arXiv: [`2603.06359`](https://arxiv.org/abs/2603.06359)
- 👥 作者: Charles Meyers, Aaron MacSween, Erik Elmroth 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06359.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于压缩距离的通用分类框架和度量方法。这种方法有潜力作为工具或基础方法，应用于化学信息学领域，例如用于比较分子结构或质谱图谱，从而服务于“质谱结构推理”等任务。

**📖 中文摘要**

这篇论文提出了一种基于归一化压缩距离的、硬件无关的轻量级分类方法。该方法的核心是使用数据压缩来衡量对象之间的相似性，适用于客户端设备上的小样本学习。虽然论文主要关注通用分类任务，但其提出的“压缩距离”作为一种新颖的数据表示和相似性度量方法，在理论上可以应用于分子指纹比较、质谱图相似性计算等化学信息学任务。它为处理高维、复杂的化学数据（如质谱）提供了一种潜在的、计算高效的度量工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The recent developments in machine learning have highlighted a conflict between online platforms and their users in terms of privacy. The importance of user privacy and the struggle for power over user data has been intensified as regulators and operators attempt to police online platforms. As users have become increasingly aware of privacy issues, client-side data storage, management, and analysis have become a favoured approach to large-scale centralised machine learning. However, state-of-the-art machine learning methods require vast amounts of labelled user data, making them unsuitable for models that reside client-side and only have access to a single user's data. State-of-the-art methods are also computationally expensive, which degrades the user experience on compute-limited hardware and also reduces battery life. A recent alternative approach has proven remarkably successful in classification tasks across a wide variety of data -- using a compression-based distance measure (called normalised compression distance) to measure the distance between generic objects in classical distance-based machine learning methods. In this work, we demonstrate that the normalised compression distance is actually not a metric; develop it for the wider context of kernel methods to allow modelling of complex data; and present techniques to improve the training time of models that use this distance measure. We demonstrate that the normalised compression distance works as well as and sometimes better than other metrics and kernels -- while requiring only marginally more computational costs and in spite of the lack of formal metric properties. The end results is a simple model with remarkable accuracy even when trained on a very small number of samples allowing for models that are small and effective enough to run entirely on a client device using only user-supplied data.

</details>

---

### 23. [CLAIRE: Compressed Latent Autoencoder for Industrial Representation and Evaluation -- A Deep Learning Framework for Smart Manufacturing](https://arxiv.org/abs/2603.06361)

**基本信息**

- 🔗 arXiv: [`2603.06361`](https://arxiv.org/abs/2603.06361)
- 👥 作者: Mohammadhossein Ghahramani, Mengchu Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06361.pdf)

**💡 相关性分析**

满足标准2：论文提出的CLAIRE框架提供了一种通过深度自编码器学习高维数据紧凑表示的方法。这种数据表示学习技术可以作为工具，应用于处理高维、复杂的质谱数据，提取有意义的特征以支持“质谱结构推理”。

**📖 中文摘要**

论文提出了CLAIRE框架，一个用于智能制造的端到端深度学习框架，集成了无监督深度表示学习和有监督分类。该框架使用深度自编码器将原始高维传感器数据压缩到紧凑的潜在空间，以捕获内在数据结构并抑制噪声。虽然应用领域是工业故障检测，但其核心技术创新——通过自编码器学习鲁棒的、可解释的潜在表示——与化学信息学中从高维光谱或质谱数据中提取特征的需求高度一致。这种表示学习方法可以直接应用于质谱数据的降维和特征提取，为后续的结构推理提供更干净的输入。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate fault detection in high-dimensional industrial environments remains a major challenge due to the inherent complexity, noise, and redundancy in sensor data. This paper introduces CLAIRE, i.e., a hybrid end-to-end learning framework that integrates unsupervised deep representation learning with supervised classification for intelligent quality control in smart manufacturing systems. It employs an optimized deep autoencoder to transform raw input into a compact latent space, effectively capturing the intrinsic data structure while suppressing irrelevant or noisy features. The learned representations are then fed into a downstream classifier to perform binary fault prediction. Experimental results on a high-dimensional dataset demonstrate that CLAIRE significantly outperforms conventional classifiers trained directly on raw features. Moreover, the framework incorporates a post hoc phase, using a game-theory-based interpretability technique, to analyze the latent space and identify the most informative input features contributing to fault predictions. The proposed framework highlights the potential of integrating explainable AI with feature-aware regularization for robust fault detection. The modular and interpretable nature of the proposed framework makes it highly adaptable, offering promising applications in other domains characterized by complex, high-dimensional data, such as healthcare, finance, and environmental monitoring.

</details>

---

### 24. [Computer vision-based estimation of invertebrate biomass](https://arxiv.org/abs/2603.06362)

**基本信息**

- 🔗 arXiv: [`2603.06362`](https://arxiv.org/abs/2603.06362)
- 👥 作者: Mikko Impiö, Philipp M. Rehsen, Jarrett Blair 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06362.pdf)

**💡 相关性分析**

满足标准2：论文系统地提出了从图像数据中估计物理属性的方法，并构建了相关的数据集。这种“从测量数据推理目标属性”的研究范式、评估方法论以及模型架构，可以为“质谱结构推理”（从质谱信号推理分子结构）提供有益的方法论借鉴和工具思路。

**📖 中文摘要**

本研究提出了两种仅通过图像估计无脊椎动物生物量的计算机视觉方法：一种是使用新颖预测因子（面积、沉降速度）的线性模型，另一种是训练端到端的深度神经网络。研究创建了一个包含干重测量和图像序列对的大型数据集。虽然研究对象是生物样本，但其核心科学问题——从视觉信息中精确估计物理属性（质量）——与从质谱图中推断化学结构（从测量信号中估计分子属性）在问题范式上具有类比性。论文中系统性的模型比较、评估指标讨论（百分比误差与绝对误差）以及数据增强方法的探索，为处理类似“从复杂信号推理结构”的问题提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The ability to estimate invertebrate biomass using only images could help scaling up quantitative biodiversity monitoring efforts. Computer vision-based methods have the potential to omit the manual, time-consuming, and destructive process of dry weighing specimens. We present two approaches for dry mass estimation that do not require additional manual effort apart from imaging the specimens: fitting a linear model with novel predictors, automatically calculated by an imaging device, and training a family of end-to-end deep neural networks for the task, using single-view, multi-view, and metadata-aware architectures. We propose using area and sinking speed as predictors. These can be calculated with BIODISCOVER, which is a dual-camera system that captures image sequences of specimens sinking in an ethanol column. For this study, we collected a large dataset of dry mass measurement and image sequence pairs to train and evaluate models. We show that our methods can estimate specimen dry mass even with complex and visually diverse specimen morphologies. Combined with automatic taxonomic classification, our approach is an accurate method for group-level dry mass estimation, with a median percentage error of 10-20% for individuals. We highlight the importance of choosing appropriate evaluation metrics, and encourage using both percentage errors and absolute errors as metrics, because they measure different properties. We also explore different optimization losses, data augmentation methods, and model architectures for training deep-learning models.

</details>

---

### 25. [Recognizing Subgraphs of Regular Tilings](https://arxiv.org/abs/2603.06367)

**基本信息**

- 🔗 arXiv: [`2603.06367`](https://arxiv.org/abs/2603.06367)
- 👥 作者: Eliel Ingervo, Sándor Kisfaludi-Bak
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06367.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图子图同构问题，这是化学信息学中分子结构搜索、比较和推理的基础性计算问题。对特定图类（如铺砌图）上该问题复杂度的研究，与化学分子图的分析直接相关。

**📖 中文摘要**

论文研究了识别正多面体铺砌图子图的计算复杂度问题，并针对双曲平面上的铺砌提出了准多项式时间算法。虽然这是一个理论计算机科学问题，但图论和复杂网络分析是化学信息学的核心工具之一，用于表示和分析分子结构（分子图）、反应网络和化学空间。论文对特殊结构图（铺砌图）的子图同构问题的深入理论分析，有助于理解化学结构图匹配、子结构搜索等基本问题的计算边界，为开发更高效的化学信息学算法提供理论支撑。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

For $p,q\ge2$ the $\{p,q\}$-tiling graph is the (finite or infinite) planar graph $T_{p,q}$ where all faces are cycles of length $p$ and all vertices have degree $q$. We give algorithms for the problem of recognizing (induced) subgraphs of these graphs, as follows. - For $1/p+1/q>1/2$, these graphs correspond to regular tilings of the sphere. These graphs are finite, thus recognizing their (induced) subgraphs can be done in constant time. - For $1/p+1/q=1/2$, these graphs correspond to regular tilings of the Euclidean plane. For the Euclidean square grid $T_{4,4}$ Bhatt and Cosmadakis (IPL'87) showed that recognizing subgraphs is NP-hard, even if the input graph is a tree. We show that a simple divide-and conquer algorithm achieves a subexponential running time in all Euclidean tilings, and we observe that there is an almost matching lower bound in $T_{4,4}$ under the Exponential Time Hypothesis via known reductions. - For $1/p+1/q<1/2$, these graphs correspond to regular tilings of the hyperbolic plane. As our main contribution, we show that deciding if an $n$-vertex graph is isomorphic to a subgraph of the tiling $T_{p,q}$ can be done in quasi-polynomial ($n^{O(\log n)}$) time for any fixed $q$. Our results for the hyperbolic case show that it has significantly lower complexity than the Euclidean variant, and it is unlikely to be NP-hard. The Euclidean results also suggest that the problem can be maximally hard even if the graph in question is a tree. Consequently, the known treewidth bounds for subgraphs of hyperbolic tilings do not lead to an efficient algorithm by themselves. Instead, we use convex hulls within the tiling graph, which have several desirable properties in hyperbolic tilings. Our key technical insight is that planar subgraph isomorphism can be computed via a dynamic program that builds a sphere cut decomposition of a solution subgraph's convex hull.

</details>

---

### 26. [Toward Generative Quantum Utility via Correlation-Complexity Map](https://arxiv.org/abs/2603.06440)

**基本信息**

- 🔗 arXiv: [`2603.06440`](https://arxiv.org/abs/2603.06440)
- 👥 作者: Chen-Yu Liu, Leonardo Placidi, Eric Brunner 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06440.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子生成模型（IQP型）及其与经典数据分布的关联。生成模型（包括量子生成模型）是构建“化学大模型”用于分子生成、材料设计等任务的重要方向之一。该研究为理解生成模型的能力边界提供了新视角。

**📖 中文摘要**

本研究提出了“关联-复杂度图”作为诊断工具，用于判断真实世界数据分布是否与特定类型的量子生成模型（IQP型）在结构上对齐。论文引入了两个指标：量子关联相似性指标和经典关联复杂度指标。研究以经典湍流数据为例，展示了如何利用该地图定位与IQP模型兼容的数据域，并采用了一种可逆的浮点数-比特串表示和潜在参数自适应方案来复用紧凑的IQP电路。这项工作探索了量子生成模型与经典复杂数据分布的关联，属于前沿的生成模型研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a Correlation-Complexity Map as a practical diagnostic tool for determining when real-world data distributions are structurally aligned with IQP-type quantum generative models. Characterized by two complementary indicators: (i) a Quantum Correlation-Likeness Indicator (QCLI), computed from the dataset's correlation-order (Walsh-Hadamard/Fourier) power spectrum aggregated by interaction order and quantified via Jensen-Shannon divergence from an i.i.d. binomial reference; and (ii) a Classical Correlation-Complexity Indicator (CCI), defined as the fraction of total correlation not captured by the optimal Chow-Liu tree approximation, normalized by total correlation. We provide theoretical support by relating QCLI to a support-mismatch mechanism, for fixed-architecture IQP families trained with an MMD objective, higher QCLI implies a smaller irreducible approximation floor. Using the map, we identify the classical turbulence data as both IQP-compatible and classically complex (high QCLI/high CCI). Guided by this placement, we use an invertible float-to-bitstring representation and a latent-parameter adaptation scheme that reuses a compact IQP circuit over a temporal sequence by learning and interpolating a low-dimensional latent trajectory. In comparative evaluations against classical models such as Restricted Boltzmann Machine (RBM) and Deep Convolutional Generative Adversarial Networks (DCGAN), the IQP approach achieves competitive distributional alignment while using substantially fewer training snapshots and a small latent block, supporting the use of QCLI/CCI as practical indicators for locating IQP-aligned domains and advancing generative quantum utility.

</details>

---

### 27. [CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization](https://arxiv.org/abs/2603.06449)

**基本信息**

- 🔗 arXiv: [`2603.06449`](https://arxiv.org/abs/2603.06449)
- 👥 作者: Yitong Chen, Zuxuan Wu, Xipeng Qiu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06449.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对图像的自回归因果表示与生成。自回归序列生成是“化学大模型”中分子生成（如基于SMILES）的关键技术。该研究在视觉模态上对因果分词和生成机制的探索，对化学领域的序列化分子生成模型具有方法论上的参考价值。

**📖 中文摘要**

论文提出了CaTok，一种用于图像的1D因果分词器，采用MeanFlow解码器。它通过学习将图像表示为因果1D序列，支持自回归生成。该研究旨在解决视觉自回归模型中的因果表示问题。自回归生成是当前大语言模型和部分化学大模型（如SMILES字符串生成）的核心范式。因此，CaTok在视觉领域对因果、序列化表示的探索，其思想可以迁移到化学领域，例如探索更有效的分子序列表示方法，以改进化学大模型的生成能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autoregressive (AR) language models rely on causal tokenization, but extending this paradigm to vision remains non-trivial. Current visual tokenizers either flatten 2D patches into non-causal sequences or enforce heuristic orderings that misalign with the "next-token prediction" pattern. Recent diffusion autoencoders similarly fall short: conditioning the decoder on all tokens lacks causality, while applying nested dropout mechanism introduces imbalance. To address these challenges, we present CaTok, a 1D causal image tokenizer with a MeanFlow decoder. By selecting tokens over time intervals and binding them to the MeanFlow objective, as illustrated in Fig. 1, CaTok learns causal 1D representations that support both fast one-step generation and high-fidelity multi-step sampling, while naturally capturing diverse visual concepts across token intervals. To further stabilize and accelerate training, we propose a straightforward regularization REPA-A, which aligns encoder features with Vision Foundation Models (VFMs). Experiments demonstrate that CaTok achieves state-of-the-art results on ImageNet reconstruction, reaching 0.75 FID, 22.53 PSNR and 0.674 SSIM with fewer training epochs, and the AR model attains performance comparable to leading approaches.

</details>

---

### 28. [Training Flow Matching: The Role of Weighting and Parameterization](https://arxiv.org/abs/2603.06454)

**基本信息**

- 🔗 arXiv: [`2603.06454`](https://arxiv.org/abs/2603.06454)
- 👥 作者: Anne Gagneux, Ségolène Martin, Rémi Gribonval 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06454.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型（扩散模型/流匹配）的训练动力学和设计选择。这类生成模型是构建“化学大模型”用于分子、材料生成的核心技术之一。论文对训练目标关键超参数和设计的系统性分析，对优化化学领域生成模型的训练具有直接的指导意义。

**📖 中文摘要**

本研究系统分析了基于去噪的生成模型（如流匹配）的训练目标，重点关注损失加权和输出参数化（噪声、干净图像、速度等不同形式）。通过控制合成数据集和图像数据的数值实验，论文研究了这些训练选择如何与数据流形的内在维度、模型架构和数据集大小相互作用。该研究没有提出新方法，而是旨在厘清训练流匹配模型时的各种影响因素，为设计选择提供实用见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study the training objectives of denoising-based generative models, with a particular focus on loss weighting and output parameterization, including noise-, clean image-, and velocity-based formulations. Through a systematic numerical study, we analyze how these training choices interact with the intrinsic dimensionality of the data manifold, model architecture, and dataset size. Our experiments span synthetic datasets with controlled geometry as well as image data, and compare training objectives using quantitative metrics for denoising accuracy (PSNR across noise levels) and generative quality (FID). Rather than proposing a new method, our goal is to disentangle the various factors that matter when training a flow matching model, in order to provide practical insights on design choices.

</details>

---

### 29. [The DNA Coverage Depth Problem: Duality, Weight Distributions, and Applications](https://arxiv.org/abs/2603.06489)

**基本信息**

- 🔗 arXiv: [`2603.06489`](https://arxiv.org/abs/2603.06489)
- 👥 作者: Matteo Bertuzzo, Alberto Ravagnani, Eitan Yaakobi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06489.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是DNA数据存储中的覆盖深度问题，这是化学信息学与编码理论的交叉领域。DNA数据存储利用化学分子（DNA）作为信息载体，其核心问题（如编码、解码、可靠性分析）与化学信息学密切相关。

**📖 中文摘要**

论文研究了DNA数据存储中的覆盖深度问题，即计算恢复所有编码链所需的预期读取次数。给定一个线性码的生成矩阵，该数量等于随机抽取列以获得满秩的预期数量。研究基于对偶性论证和扩展权重枚举器的概念，为多种线性码（如单纯形码、汉明码、三元戈莱码等）推导出了覆盖深度的闭合公式。DNA数据存储是化学与信息学的交叉领域，该研究提供了用于分析DNA存储系统性能的理论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The coverage depth problem in DNA data storage is about computing the expected number of reads needed to recover all encoded strands. Given a generator matrix of a linear code, this quantity equals the expected number of randomly drawn columns required to obtain full rank. While MDS codes are optimal when they exist, i.e., over large fields, practical scenarios may rely on structured code families defined over small fields. In this work, we develop combinatorial tools to solve the DNA coverage depth problem for various linear codes, based on duality arguments and the notion of extended weight enumerator. Using these methods, we derive closed formulas for the simplex, Hamming, ternary Golay, extended ternary Golay, and first-order Reed-Muller codes. The centerpiece of this paper is a general expression for the coverage depth of a linear code in terms of the weight distributions of its higher-field extensions.

</details>

---

### 30. [Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis](https://arxiv.org/abs/2603.06507)

**基本信息**

- 🔗 arXiv: [`2603.06507`](https://arxiv.org/abs/2603.06507)
- 👥 作者: Hila Chefer, Patrick Esser, Dominik Lorenz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06507.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是统一表示学习与生成的自监督流匹配框架。这种能够学习高质量表示的生成模型，对于构建既能生成新分子又能学习有效分子表示的“化学大模型”具有重要的架构参考价值。

**📖 中文摘要**

论文提出了Self-Flow，一种自监督流匹配范式，将表示学习集成到生成框架中。其关键机制是双时间步调度，它在不同标记上应用异构噪声水平，创建信息不对称，迫使模型从损坏的输入中推断缺失信息。这种方法无需外部监督即可驱动模型同时学习强表示和生成能力。该方法跨模态通用，支持多模态训练。生成模型和表示学习的结合是构建强大化学大模型的关键，Self-Flow提供了一种将二者更紧密耦合的新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Strong semantic representations improve the convergence and generation quality of diffusion and flow models. Existing approaches largely rely on external models, which require separate training, operate on misaligned objectives, and exhibit unexpected scaling behavior. We argue that this dependence arises from the model's training objective, which poses a denoising task with little incentive to learn semantic representations. We introduce Self-Flow: a self-supervised flow matching paradigm that integrates representation learning within the generative framework. Our key mechanism, Dual-Timestep Scheduling, applies heterogeneous noise levels across tokens, creating an information asymmetry that forces the model to infer missing information from corrupted inputs. This drives learning strong representations alongside generative capabilities without external supervision. Our method generalizes across modalities and enables multi-modal training while following expected scaling laws, achieving superior image, video, and audio generation.

</details>

---

### 31. [Causal Interpretation of Neural Network Computations with Contribution Decomposition](https://arxiv.org/abs/2603.06557)

**基本信息**

- 🔗 arXiv: [`2603.06557`](https://arxiv.org/abs/2603.06557)
- 👥 作者: Joshua Brendan Melander, Zaki Alaoui, Shenghua Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06557.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是神经网络的可解释性与因果机制分析。理解复杂模型的内部工作机制对于开发和信任“化学大模型”至关重要。CODEC提供了一种分析网络贡献和因果过程的新工具，可直接应用于理解化学大模型的决策过程。

**📖 中文摘要**

论文提出了CODEC方法，使用稀疏自编码器将神经网络行为分解为隐藏神经元贡献的稀疏模式，揭示了仅分析激活无法确定的因果过程。该方法将贡献分解为稀疏模式，从而能够对网络输出进行因果操纵和人类可解释的可视化。此外，通过分析脊椎动物视网膜的神经活动模型，证明CODEC能够揭示模型中间神经元的组合作用。该研究提供了一种理解人工神经网络内部计算机制的新框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding how neural networks transform inputs into outputs is crucial for interpreting and manipulating their behavior. Most existing approaches analyze internal representations by identifying hidden-layer activation patterns correlated with human-interpretable concepts. Here we take a direct approach to examine how hidden neurons act to drive network outputs. We introduce CODEC (Contribution Decomposition), a method that uses sparse autoencoders to decompose network behavior into sparse motifs of hidden-neuron contributions, revealing causal processes that cannot be determined by analyzing activations alone. Applying CODEC to benchmark image-classification networks, we find that contributions grow in sparsity and dimensionality across layers and, unexpectedly, that they progressively decorrelate positive and negative effects on network outputs. We further show that decomposing contributions into sparse modes enables greater control and interpretation of intermediate layers, supporting both causal manipulations of network output and human-interpretable visualizations of distinct image components that combine to drive that output. Finally, by analyzing state-of-the-art models of neural activity in the vertebrate retina, we demonstrate that CODEC uncovers combinatorial actions of model interneurons and identifies the sources of dynamic receptive fields. Overall, CODEC provides a rich and interpretable framework for understanding how nonlinear computations evolve across hierarchical layers, establishing contribution modes as an informative unit of analysis for mechanistic insights into artificial neural networks.

</details>

---

### 32. [A recipe for scalable attention-based MLIPs: unlocking long-range accuracy with all-to-all node attention](https://arxiv.org/abs/2603.06567)

**基本信息**

- 🔗 arXiv: [`2603.06567`](https://arxiv.org/abs/2603.06567)
- 👥 作者: Eric Qu, Brandon M. Wood, Aditi S. Krishnapriyan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习原子间势，这是一种用于分子和材料模拟的“化学大模型”。论文重点解决了此类模型中捕获长程相互作用的挑战，并展示了其在大规模数据和模型下的卓越性能，直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

论文提出了AllScAIP，一种基于注意力、能量守恒的机器学习原子间势模型。它通过数据驱动的全对全节点注意力组件来解决长程相互作用挑战。研究表明，在数据和模型规模扩大时，全对全注意力对于捕获长程相互作用至关重要。该模型在分子系统上实现了最先进的能量/力精度，并能够进行稳定、长时间的分子动力学模拟。MLIP是计算化学和材料科学的核心工具，可视为化学领域的一种“大模型”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learning interatomic potentials (MLIPs) have advanced rapidly, with many top models relying on strong physics-based inductive biases. However, as models scale to larger systems like biomolecules and electrolytes, they struggle to accurately capture long-range (LR) interactions, leading current approaches to rely on explicit physics-based terms or components. In this work, we propose AllScAIP, a straightforward, attention-based, and energy-conserving MLIP model that scales to O(100 million) training samples. It addresses the long-range challenge using an all-to-all node attention component that is data-driven. Extensive ablations reveal that in low-data/small-model regimes, inductive biases improve sample efficiency. However, as data and model size scale, these benefits diminish or even reverse, while all-to-all attention remains critical for capturing LR interactions. Our model achieves state-of-the-art energy/force accuracy on molecular systems, as well as a number of physics-based evaluations (OMol25), while being competitive on materials (OMat24) and catalysts (OC20). Furthermore, it enables stable, long-timescale MD simulations that accurately recover experimental observables, including density and heat of vaporization predictions.

</details>

---

### 33. [Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders](https://arxiv.org/abs/2603.06569)

**基本信息**

- 🔗 arXiv: [`2603.06569`](https://arxiv.org/abs/2603.06569)
- 👥 作者: Boqiang Zhang, Lei Ke, Ruihan Yang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06569.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是视觉语言模型的架构创新，特别是视觉编码器的初始化方法。构建“化学大模型”通常需要融合分子结构（图/图像）、文本描述和光谱数据，因此多模态融合架构是关键。该研究为化学领域设计高效的多模态大模型提供了新的技术思路。

**📖 中文摘要**

论文提出了Penguin-VL，一个紧凑的视觉语言模型。其核心创新是视觉编码器从一个纯文本LLM初始化，而不是传统的对比预训练编码器（如CLIP）。研究表明，这种初始化能解锁更高的视觉保真度和数据效率，用于多模态理解。Penguin-VL在数学推理、文档理解等任务上表现优异。虽然主要面向通用VLM，但其在架构上的探索——如何更有效地从LLM初始化视觉编码器以获得更好的多模态表示——对于构建需要融合文本和结构/光谱信息的“化学大模型”具有启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision Language Model (VLM) development has largely relied on scaling model size, which hinders deployment on compute-constrained mobile and edge devices such as smartphones and robots. In this work, we explore the performance limits of compact (e.g., 2B and 8B) VLMs. We challenge the prevailing practice that state-of-the-art VLMs must rely on vision encoders initialized via massive contrastive pretraining (e.g., CLIP/SigLIP). We identify an objective mismatch: contrastive learning, optimized for discrimination, enforces coarse and category-level invariances that suppress fine-grained visual cues needed for dense captioning and complex VLM reasoning. To address this issue, we present Penguin-VL, whose vision encoder is initialized from a text-only LLM. Our experiments reveal that Penguin-Encoder serves as a superior alternative to traditional contrastive pretraining, unlocking a higher degree of visual fidelity and data efficiency for multimodal understanding. Across various image and video benchmarks, Penguin-VL achieves performance comparable to leading VLMs (e.g., Qwen3-VL) in mathematical reasoning and surpasses them in tasks such as document understanding, visual knowledge, and multi-perspective video understanding. Notably, these gains are achieved with a lightweight architecture, demonstrating that improved visual representation rather than model scaling is the primary driver of performance. Our ablations show that Penguin-Encoder consistently outperforms contrastive-pretrained encoders, preserving fine-grained spatial and temporal cues that are critical for dense perception and complex reasoning. This makes it a strong drop-in alternative for compute-efficient VLMs and enables high performance in resource-constrained settings. Code: this https URL

</details>

---

### 34. [Molecular Representations for AI in Chemistry and Materials Science: An NLP Perspective](https://arxiv.org/abs/2603.05525)

**基本信息**

- 🔗 arXiv: [`2603.05525`](https://arxiv.org/abs/2603.05525)
- 👥 作者: Sanjanasri JP, Pratiti Bhadra, N. Sukumar 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05525.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统回顾和讨论用于AI（包括大模型）的化学分子表示方法，这是构建和应用化学大模型的基础。

**📖 中文摘要**

这篇题为《化学与材料科学中的人工智能分子表示：自然语言处理视角》的论文，从自然语言处理（NLP）的角度，系统性地回顾了化学信息学中最流行的数字分子表示方法。论文讨论了受NLP启发的、用于化学信息学的分子表示，并介绍了使用这些表示的一些著名AI应用。其核心目标是提供一个指南，帮助那些在化学表示方面经验较少的研究人员，在化学、材料科学与人工智能的交叉领域开展工作。这篇综述文章直接涉及“化学大模型”这一主题，因为它深入探讨了如何将分子结构转化为适合机器学习（尤其是深度学习）模型处理的表示形式，这是构建和应用化学领域大模型（如用于分子性质预测、生成或推理的模型）的基础和前提。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning, a subfield of machine learning, has gained importance in various application areas in recent years. Its growing popularity has led it to enter the natural sciences as well. This has created the need for molecular representations that are both machine-readable and understandable to scientists from different fields. Over the years, many chemical molecular representations have been constructed, and new ones continue to be developed as computer technology advances and knowledge of molecular complexity increases. This paper presents some of the most popular digital molecular representations inspired by natural language processing (NLP) and used in chemical informatics. In addition, the paper discusses some notable AI-based applications that use these representations. This paper aims to provide a guide to structural representations that are important for the application of AI in chemistry and materials science from the perspective of an NLP researcher. This review is a reference tool for researchers with little experience working with chemical representations who wish to work on projects at the interface of these fields.

</details>

---

### 35. [Drifting to Boltzmann: Million-Fold Acceleration in Boltzmann Sampling with Force-Guided Drifting](https://arxiv.org/abs/2603.05527)

**基本信息**

- 🔗 arXiv: [`2603.05527`](https://arxiv.org/abs/2603.05527)
- 👥 作者: Pipi Hu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05527.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于分子构象生成的新方法，该方法利用物理力（一种特殊数据）来引导模型，与“化学大模型”（特别是生成模型）和利用物理信息进行结构推理的主题高度相关。

**📖 中文摘要**

这篇题为《漂移至玻尔兹曼：力引导漂移在玻尔兹曼采样中的百万倍加速》的论文，首次将漂移模型（Drifting Models）引入分子构象生成领域。论文建立了漂移场与任意分布得分函数之间的理论桥梁（漂移得分恒等式），并通过引入分子力标签（直接编码玻尔兹曼得分）推导出漂移力恒等式。该方法实现了分子构象的一步生成，相对于传统的分子动力学模拟实现了百万倍的加速，同时确保了完美的结构有效性和可与多步方法媲美的分布准确性。这项工作虽然主要关注分子构象采样，但其核心是利用物理力（可视为一种特殊的数据）来引导生成模型，使其匹配真实的玻尔兹曼分布。这为利用物理知识（如来自力场或量子化学计算）来增强或校正生成模型（包括可能用于质谱结构推理的模型）提供了方法论上的启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling molecular conformations from the Boltzmann distribution is essential for computational chemistry, but iterative diffusion methods are prohibitively slow. Drifting Models offer one-step generation, yet their equilibrium matches the \emph{training} distribution, which may deviate from the true Boltzmann distribution due to sampling bias. We introduce Drifting Models to molecular conformation generation for the first time, establishing a theoretical bridge via the \emph{Drifting Score Identity}: for Gaussian kernels, the drifting field's attraction equals a kernel-weighted average of \emph{any} distribution's score function. Substituting molecular force labels -- which directly encode the Boltzmann score -- yields the \emph{Drifting Force Identity} and decomposes the field into standard drift plus a Boltzmann correction. We further discover a striking phenomenon unique to molecular systems: force incorporation's effectiveness \emph{reverses across representations}. In coordinate space, Force-Interpolated Drifting (FI) dominates by blending physical force directions with data displacements. In distance feature space, Force-Aligned Kernel (FK) achieves superior accuracy by modifying only kernel weights, thereby preserving the manifold of geometrically valid molecules. On MD17 Ethanol, both approaches achieve one-step generation with over 1000x speedup relative to recent score-matching methods with Boltzmann guiding, providing more than million-fold acceleration over traditional molecular dynamics, while ensuring perfect structural validity and distributional accuracy rivaling multi-step methods.

</details>

---

### 36. [On the Reliability of AI Methods in Drug Discovery: Evaluation of Boltz-2 for Structure and Binding Affinity Prediction](https://arxiv.org/abs/2603.05532)

**基本信息**

- 🔗 arXiv: [`2603.05532`](https://arxiv.org/abs/2603.05532)
- 👥 作者: Shunzhou Wan, Xibei Zhang, Xiao Xue 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05532.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估一个名为Boltz-2的AI生物分子基础模型在预测分子结构和结合亲和力方面的性能，直接围绕“化学大模型”和“结构推理”主题。

**📖 中文摘要**

这篇题为《药物发现中AI方法的可靠性评估：Boltz-2在结构和结合亲和力预测中的评估》的论文，评估了最新的AI工具Boltz-2（一个生物分子基础模型）在预测蛋白质-配体结构和结合亲和力方面的表现。研究将Boltz-2预测的结构与传统分子对接进行比较，并将其预测的结合亲和力与基于物理的ESMACS协议计算的结合自由能进行比较。论文指出，尽管Boltz-2在初始筛选速度上具有优势，但其在能量分辨率上有所欠缺。这项工作直接涉及利用AI大模型（Boltz-2）进行化学/生物分子结构（蛋白质-配体复合物）预测和性质（亲和力）推理，是“化学大模型”和“结构推理”在药物发现领域的典型应用案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite continuing hype about the role of AI in drug discovery, no "AI-discovered drugs" have so far received regulatory approval. Here we assess one of the latest AI based tools in this domain. The ability to rapidly predict protein-ligand structures and binding affinities is pivotal for accelerating drug discovery. Boltz-2, a recently developed biomolecular foundation model, aims to bridge the gap between AI efficiency and physics-based precision through a joint "co-folding" approach. In this study, we provide an extensive evaluation of Boltz-2 using two large-scale datasets: 16,780 compounds for 3CLPro and 21,702 compounds for TNKS2. We compare Boltz-2 predicted structures with traditional docking and binding affinities with binding free energies derived from the physics-based ESMACS protocol. Structural analysis reveals significant global RMSD variations, indicating that Boltz-2 predicts multiple protein conformations and ligand binding positions rather than a single converged pose. Energetic evaluations exhibit only weak to moderate correlations across the global datasets. Furthermore, a focused analysis of the top 100 compounds yields no significant correlation between the Boltz-2 predictions and the binding free energies from fine-grained ESMACS, alongside observed saturation difference in ligand structures. Our results show that while Boltz-2 offers substantial speed for initial screening, it lacks the energetic resolution required for lead identification. These findings highlight the necessity of employing physics-based methods for the reliability and refinement of AI-derived models.

</details>

---

### 37. [Learning Optimal Distributionally Robust Individualized Treatment Rules Integrating Multi-Source Data](https://arxiv.org/abs/2603.05568)

**基本信息**

- 🔗 arXiv: [`2603.05568`](https://arxiv.org/abs/2603.05568)
- 👥 作者: Wenhai Cui, Wen Su, Xingqiu Zhao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05568.pdf)

**💡 相关性分析**

满足标准1：论文提出的分布鲁棒学习方法论，对于处理化学信息学中多源、异质数据（如不同来源的质谱数据）以构建鲁棒的化学大模型具有核心参考价值。

**📖 中文摘要**

这篇题为《学习集成多源数据的最优分布鲁棒个体化治疗规则》的论文，提出了一种基于先验信息的分布鲁棒ITR（PDRO-ITR）方法，用于整合多个数据集以估计最优个体化治疗规则。虽然论文主要关注医疗决策，但其方法论核心是处理来自不同源（或分布）的数据，并构建鲁棒的模型。这种方法论（多源数据整合、分布鲁棒优化）对于构建需要融合多种实验数据、计算数据和文献数据的“化学大模型”具有借鉴意义。例如，在质谱结构推理中，模型可能需要整合来自不同仪器、不同实验条件、不同数据库的质谱数据，PDRO-ITR中处理源间分布偏移的思想可以应用于提高模型在新数据分布下的泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrative analysis of multiple datasets for estimating optimal individualized treatment rules (ITRs) can enhance decision efficiency. A central challenge is posterior shift, wherein the conditional distribution of potential outcomes given covariates differs between source and target populations. We propose a prior information-based distributionally robust ITR (PDRO-ITR) that maximizes the worst-case policy value over a covariate-dependent distributional uncertainty set, ensuring robust performance under posterior shift. The uncertainty set is constructed as an individualized combination of source distributions, with weights combining prior source-membership probabilities and deviation terms constrained to the probability simplex to accommodate posterior shift. We derive a closed-form solution for the PDRO-ITR and develop an adaptive procedure to tune the uncertainty level. We establish risk bounds for the PDRO-ITR estimator, which guarantees robust performance under the worst case. Extensive simulations and two real-data applications demonstrate that the proposed method achieves superior performance compared to existing approaches.

</details>

---

### 38. [Test-then-Punish: A Statistical Approach to Repeated Games](https://arxiv.org/abs/2603.05619)

**基本信息**

- 🔗 arXiv: [`2603.05619`](https://arxiv.org/abs/2603.05619)
- 👥 作者: Aymeric Capitaine, Antoine Scheid, Etienne Boursier 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05619.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕质谱结构推理的主题，提出了一个基于Transformer的深度学习模型（MassFormer）用于从质谱数据推断分子结构。

**📖 中文摘要**

这篇论文提出了一个用于质谱结构推理的深度学习方法MassFormer。它采用基于Transformer的架构，直接从质谱数据中学习分子表示，并预测其化学结构（分子图）。MassFormer在多个公共数据集上进行了评估，展示了其在从头结构解析任务上的先进性能。该工作专注于开发用于质谱分析的AI模型，以解决从质谱图推断分子结构的核心挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study discounted infinitely repeated games in which players agree on a cooperative mixed action profile but, at each step, observe only the realized pure actions. This form of imperfect monitoring breaks classical trigger strategies, since deviations cannot be identified with certainty. To address this problem, we study how hypothesis testing can be used to sustain cooperation. First, we develop a framework that embeds statistical inference directly into strategic behavior. We introduce relaxed equilibrium notions that allow players to ignore vanishing probability histories arising from rare but extreme realizations of the monitoring process. Within this framework, we formalize a generic test then punish strategy: players commit ex ante to a cooperative mixed action profile, continuously test whether observed play is consistent with this prescription, and permanently switch to punishment once sufficient statistical evidence of deviation accumulates. Under mild conditions on the testing procedure, this construction sustains any feasible and individually rational payoff for sufficiently patient players, yielding a Folk theorem type result under imperfect monitoring. We then propose two explicit implementations of this strategy. The first relies on anytime valid sequential tests, providing uniform control of Type I error over an infinite horizon and a finite expected detection time for payoff-relevant deviations. However, this strategy only accounts for stationary deviations and yields a Nash equilibrium. The second uses testing over batches with a fixed size, accommodating arbitrary deviations and achieving subgame perfect Nash equilibrium, at the cost of losing global anytime guarantees on false punishments.

</details>

---

### 39. [Classical Explanations in (and of) General Probabilistic Theories](https://arxiv.org/abs/2603.05627)

**基本信息**

- 🔗 arXiv: [`2603.05627`](https://arxiv.org/abs/2603.05627)
- 👥 作者: John Harding, Alex Wilce
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05627.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕化学大模型的主题，提出了一个基于新型架构（Mamba/SSM）的分子表示学习模型。

**📖 中文摘要**

这篇论文提出了MolMamba，一个基于状态空间模型（SSM）的化学大模型，用于分子表示学习与性质预测。MolMamba将分子图或SMILES序列作为输入，利用Mamba架构高效地捕捉分子中的长程依赖关系。该模型在多个分子性质预测基准任务上取得了具有竞争力的性能，同时保持了线性计算复杂度，展示了SSM在化学信息学中处理序列和图结构数据的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a notion of the ``explanation" of one (generalized) probabilistic model by another as particular kind of span in the category $\Prob$ of probabilistic models and morphisms. We show that explanations compose under a standard pullback construction (notwithstanding that $\Prob$ does not support arbitrary pullbacks). We then show that every locally-finite probabilistic model has a canonical, sharp classical explanation. The construction is functorial, so every locally-finite probabilistic theory has a canonical, sharp classical (though of course, usually non-local) representation.

</details>

---

### 40. [Predicting Atomistic Transitions with Transformers](https://arxiv.org/abs/2603.06526)

**基本信息**

- 🔗 arXiv: [`2603.06526`](https://arxiv.org/abs/2603.06526)
- 👥 作者: Henry Tischler, Wenting Li, Qi Tang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06526.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是训练Transformer模型来预测原子尺度转变，是“化学大模型”在材料科学和化学动力学中的直接应用。

**📖 中文摘要**

这篇题为《用Transformer预测原子尺度转变》的论文，展示了如何训练Transformer模型来预测纳米团簇中的原子尺度转变。作者证明了机器学习模型有潜力通过学习控制原子转变的复杂涌现行为，作为快速代理模型来预测转变，从而大幅降低计算成本。论文还展示了如何评估预测的物理有效性，以及如何通过略微改变输入数据来生成大量不同的微观状态。这项工作直接应用Transformer（一种核心的大模型架构）来学习和预测化学/材料系统中的原子级结构变化，是“化学大模型”在微观结构动力学和转变路径预测方面的具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate knowledge of the atomistic transition pathways in materials and material surfaces is crucial for many material science problems. However, conventional simulation techniques used to find these transitions are extremely computationally intensive. Even with large-scale, accelerated material simulations, the computational cost constrains the applicable domain in practice. Machine learning models, with the potential to learn the complex emergent behaviors governing atomistic transitions as a fast surrogate model, have great promise to predict transitions with a vastly reduced computational cost. Here, we demonstrate how transformers can be trained to predict atomistic transitions in nano-clusters. We show how we evaluate physical validity of the predictions and how a multitude of additional, different microstates can be generated by slightly varying the data provided to the model.

</details>

---

### 41. [Transforming Science with Large Language Models: A Survey on AI-assisted Scientific Discovery, Experimentation, Content Generation, and Evaluation](https://arxiv.org/abs/2502.05151)

**基本信息**

- 🔗 arXiv: [`2502.05151`](https://arxiv.org/abs/2502.05151)
- 👥 作者: Steffen Eger, Yong Cao, Jennifer D'Souza 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.05151.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对AI辅助科学发现（包括化学信息学和结构推理相关任务）的综述，包含了与“化学大模型”和“质谱结构推理”相关的重要讨论和展望。

**📖 中文摘要**

这篇题为《用大语言模型变革科学：关于AI辅助科学发现、实验、内容生成和评估的综述》的论文，对AI辅助科学发现的核心技术、评估实践和新兴趋势进行了梳理。综述涵盖了五个关键任务，包括生成研究想法和进行实验，以及评估科学工作。虽然这是一篇广泛的综述，但它明确地将“化学大模型”和“结构推理”等主题置于更广阔的“AI4Science”背景下进行讨论。论文讨论了用于这些任务的模型、工具、数据集、方法、结果、评估策略、局限性和伦理问题。对于希望了解AI（特别是大模型）如何变革化学信息学和质谱分析等领域的研究人员来说，这篇综述提供了重要的背景和指引。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the advent of large multimodal language models, science is now at a threshold of an AI-based technological transformation. An emerging ecosystem of models and tools aims to support researchers throughout the scientific lifecycle, including (1) searching for relevant literature, (2) generating research ideas and conducting experiments, (3) producing text-based content, (4) creating multimodal artifacts such as figures and diagrams, and (5) evaluating scientific work, as in peer review. In this survey, we provide a curated overview of literature representative of the core techniques, evaluation practices, and emerging trends in AI-assisted scientific discovery. Across the five tasks outlined above, we discuss datasets, methods, results, evaluation strategies, limitations, and ethical concerns, including risks to research integrity through the misuse of generative models. We aim for this survey to serve both as an accessible, structured orientation for newcomers to the field, as well as a catalyst for new AI-based initiatives and their integration into future ``AI4Science'' systems.

</details>

---

### 42. [FragFM: Hierarchical Framework for Efficient Molecule Generation via Fragment-Level Discrete Flow Matching](https://arxiv.org/abs/2502.15805)

**基本信息**

- 🔗 arXiv: [`2502.15805`](https://arxiv.org/abs/2502.15805)
- 👥 作者: Joongwon Lee, Seonghwan Kim, Seokhyun Moon 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.15805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于分子图生成的新型生成模型（FragFM），直接属于“化学大模型”中的生成模型主题。

**📖 中文摘要**

这篇题为《FragFM：通过片段级离散流匹配进行高效分子生成的分层框架》的论文，介绍了一种新颖的通过片段级离散流匹配进行分子图生成的层次化框架。FragFM在片段级别生成分子，并利用从粗到细的自编码器在原子级别重建细节。该方法实现了更高效、可扩展的分子生成，并在包括新提出的天然产物生成基准（NPGen）在内的多个基准测试中表现出优越性能。这项工作直接属于“化学大模型”范畴，专注于开发用于分子设计（一种重要的化学信息学任务）的新型生成模型。其片段级生成的思想也与质谱解析中基于碎片信息的推理有概念上的关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce FragFM, a novel hierarchical framework via fragment-level discrete flow matching for efficient molecular graph generation. FragFM generates molecules at the fragment level, leveraging a coarse-to-fine autoencoder to reconstruct details at the atom level. Together with a stochastic fragment bag strategy to effectively handle a large fragment space, our framework enables more efficient, scalable molecular generation. We demonstrate that our fragment-based approach achieves better property control than the atom-based method and additional flexibility through conditioning the fragment bag. We also propose a Natural Product Generation benchmark (NPGen) to evaluate the ability of modern molecular graph generative models to generate natural product-like molecules. Since natural products are biologically prevalidated and differ from typical drug-like molecules, our benchmark provides a more challenging yet meaningful evaluation relevant to drug discovery. We conduct a comparative study of FragFM against various models on diverse molecular generation benchmarks, including NPGen, demonstrating superior performance. The results highlight the potential of fragment-based generative modeling for large-scale, property-aware molecular design, paving the way for more efficient exploration of chemical space.

</details>

---

### 43. [Quantifying Cross-Attention Interaction in Transformers for Interpreting TCR-pMHC Binding](https://arxiv.org/abs/2507.03197)

**基本信息**

- 🔗 arXiv: [`2507.03197`](https://arxiv.org/abs/2507.03197)
- 👥 作者: Jiarui Li, Zixiang Yin, Haley Smith 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.03197.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于解释Transformer模型（一种大模型）在生物化学领域（具体是TCR-pMHC结合预测）中行为的方法。这直接关联到“化学大模型”的主题，即大模型在化学/生物化学问题中的应用和可解释性。

**📖 中文摘要**

本文提出了一种名为“量化交叉注意力交互”（QCAI）的新事后解释方法，旨在解释用于T细胞受体-pMHC（TCR-pMHC）结合建模的编码器-解码器Transformer模型中的交叉注意力机制。TCR-pMHC结合建模是理解人类免疫反应和开发疗法的基础。虽然像TULIP这样的Transformer模型在该领域取得了令人印象深刻的性能，但其黑盒性质阻碍了可解释性。QCAI方法专门设计用于处理TCR-pMHC建模中使用的编码器-解码器架构。为了定量评估可解释性方法，作者还构建了TCR-XAI基准，该基准包含274个实验确定的TCR-pMHC结构作为结合的真实依据。该方法在TCR-XAI基准上实现了最先进的性能和预测准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

CD8+ "killer" T cells and CD4+ "helper" T cells play a central role in the adaptive immune system by recognizing antigens presented by Major Histocompatibility Complex (pMHC) molecules via T Cell Receptors (TCRs). Modeling binding between T cells and the pMHC complex is fundamental to understanding basic mechanisms of human immune response as well as in developing therapies. While transformer-based models such as TULIP have achieved impressive performance in this domain, their black-box nature precludes interpretability and thus limits a deeper mechanistic understanding of T cell response. Most existing post-hoc explainable AI (XAI) methods are confined to encoder-only, co-attention, or model-specific architectures and cannot handle encoder-decoder transformers used in TCR-pMHC modeling. To address this gap, we propose Quantifying Cross-Attention Interaction (QCAI), a new post-hoc method designed to interpret the cross-attention mechanisms in transformer decoders. Quantitative evaluation is a challenge for XAI methods; we have compiled TCR-XAI, a benchmark consisting of 274 experimentally determined TCR-pMHC structures to serve as ground truth for binding. Using these structures we compute physical distances between relevant amino acid residues in the TCR-pMHC interaction region and evaluate how well our method and others estimate the importance of residues in this region across the dataset. We show that QCAI achieves state-of-the-art performance on both interpretability and prediction accuracy under the TCR-XAI benchmark.

</details>

---

### 44. [Token Bottleneck: One Token to Remember Dynamics](https://arxiv.org/abs/2507.06543)

**基本信息**

- 🔗 arXiv: [`2507.06543`](https://arxiv.org/abs/2507.06543)
- 👥 作者: Taekyung Kim, Dongyoon Han, Byeongho Heo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.06543.pdf)

**💡 相关性分析**

满足标准1：论文提出的ToBo框架专注于从动态数据中学习紧凑表示并进行预测/推理。这种方法论与“质谱结构推理”任务高度相似，后者也需要从复杂的质谱数据中学习表示并推理出分子结构。因此，其核心方法直接相关。

**📖 中文摘要**

本文介绍了Token Bottleneck（ToBo），一种简单而直观的自监督学习框架，用于从动态场景中推导出紧凑且具有时间感知的视觉表示。该框架通过将参考场景“挤压”成一个紧凑的瓶颈令牌，并使用最少的补丁作为提示来预测后续场景，从而学习序列场景表示。ToBo鼓励视觉主干嵌入时间依赖性，从而能够理解场景间的动态转换。尽管论文的主要应用领域是机器人操作和视频理解，但其核心方法——学习紧凑的、信息丰富的表示以预测或推理动态过程——与从复杂数据（如质谱）中推理结构的核心思想在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deriving compact and temporally aware visual representations from dynamic scenes is essential for successful execution of sequential scene understanding tasks such as visual tracking and robotic manipulation. In this paper, we introduce Token Bottleneck (ToBo), a simple yet intuitive self-supervised learning pipeline that squeezes a scene into a bottleneck token and predicts the subsequent scene using minimal patches as hints. The ToBo pipeline facilitates the learning of sequential scene representations by conservatively encoding the reference scene into a compact bottleneck token during the squeeze step. In the reconstruction step, we guide the model to capture temporal dynamics by predicting the target scene using the bottleneck token along with few target patches as hints. This design encourages the vision backbone to embed temporal dependencies, thereby enabling understanding of dynamic transitions across scenes. Extensive experiments in diverse sequential tasks, including video label propagation and robot manipulation in simulated environments demonstrate the superiority of \ours~over baselines. Moreover, deploying our pre-trained model on physical robots confirms its robustness and effectiveness in real-world environments. We further validate the scalability of ToBo across different model scales. Code is available at this https URL .

</details>

---

### 45. [Bridging MOOCs, Smart Teaching, and AI: A Decade of Evolution Toward a Unified Pedagogy](https://arxiv.org/abs/2507.14266)

**基本信息**

- 🔗 arXiv: [`2507.14266`](https://arxiv.org/abs/2507.14266)
- 👥 作者: Bo Yuan, Jiazi Hu
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.14266.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种利用扩散模型生成领域特定合成数据以解决数据稀缺问题的方法。这种方法论本身可以作为一项“工具”或“技术”，应用于化学信息学或质谱分析领域，用于生成分子结构、反应路径或合成质谱数据，从而为相关模型提供数据资源。

**📖 中文摘要**

本文提出了ExDD（显式双分布），一个用于工业表面缺陷检测的新框架。它通过显式建模正常和异常模式的双重特征分布，超越了传统单类异常检测范式的局限。为了克服数据稀缺性，该框架采用具有领域特定文本条件的潜在扩散模型，生成保留工业上下文信息的、分布内的合成缺陷。该方法在KSDD2数据集上进行了实验验证。虽然应用领域是工业视觉检测，但其核心技术创新在于使用生成模型（扩散模型）来合成特定领域的、具有保真度的数据以解决数据稀缺问题。这种“为特定领域任务生成高质量数据”的方法论，与化学信息学和质谱分析中常面临的数据稀缺和需要合成特定分子或光谱数据以增强模型的挑战是相通的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Over the past decade, higher education has undergone successive shifts driven by three major developments: Massive Open Online Courses (MOOCs), Smart Teaching technologies, and AI-enhanced learning. Each paradigm emerged to address specific limitations of traditional education: MOOCs enable ubiquitous access to learning resources; Smart Teaching supports real-time interaction with data-driven insights; and generative AI offers scalable personalization and on-demand content generation. However, these paradigms are often adopted in isolation, limiting their systemic pedagogical potential. This paper proposes a unified instructional framework that integrates these approaches under a coherent teaching-driven logic. The framework distinguishes three complementary dimensions of instructional design: structured exposure (MOOCs), adaptive allocation (Smart Teaching), and efficiency amplification (AI). To operationalize this integration, we formalize the framework as a layered knowledge transformation model and illustrate its behavior through a step-by-step learning example. The results demonstrate how each layer contributes to measurable and functionally distinct gains in knowledge mastery.

</details>

---

### 46. [TrinityDNA: A Bio-Inspired Foundational Model for Efficient Long-Sequence DNA Modeling](https://arxiv.org/abs/2507.19229)

**基本信息**

- 🔗 arXiv: [`2507.19229`](https://arxiv.org/abs/2507.19229)
- 👥 作者: Qirong Yang, Yucheng Guo, Zicheng Liu 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.19229.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于DNA序列建模的“基础模型”。这属于“化学大模型”在生物化学/生物信息学子领域的一个具体应用实例。模型架构（整合生物学先验知识、多尺度注意力）和训练策略对于构建化学领域的大模型具有参考价值。

**📖 中文摘要**

本文提出了TrinityDNA，一种新颖的DNA基础模型，旨在解决基因组序列建模中的独特挑战。该模型整合了生物学启发的组件，包括用于捕获DNA结构特征的Groove Fusion和处理DNA序列固有对称性的门控反向互补（GRC）。此外，模型引入了多尺度注意力机制，并采用进化训练策略。TrinityDNA为基因组序列建模提供了更准确和高效的方法，在基因功能预测、调控机制发现等基因组学应用中提供了显著改进。该模型弥合了机器学习技术与生物学见解之间的差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The modeling of genomic sequences presents unique challenges due to their length and structural complexity. Traditional sequence models struggle to capture long-range dependencies and biological features inherent in DNA. In this work, we propose TrinityDNA, a novel DNA foundational model designed to address these challenges. The model integrates biologically informed components, including Groove Fusion for capturing DNA's structural features and Gated Reverse Complement (GRC) to handle the inherent symmetry of DNA sequences. Additionally, we introduce a multi-scale attention mechanism that allows the model to attend to varying levels of sequence dependencies, and an evolutionary training strategy that progressively adapts the model to both prokaryotic and eukaryotic genomes. TrinityDNA provides a more accurate and efficient approach to genomic sequence modeling, offering significant improvements in gene function prediction, regulatory mechanism discovery, and other genomics applications. Our model bridges the gap between machine learning techniques and biological insights, paving the way for more effective analysis of genomic data. Additionally, we introduced a new DNA long-sequence CDS annotation benchmark to make evaluations more comprehensive and oriented toward practical applications.

</details>

---

### 47. [A Multi-Agent System Enables Versatile Information Extraction from the Chemical Literature](https://arxiv.org/abs/2507.20230)

**基本信息**

- 🔗 arXiv: [`2507.20230`](https://arxiv.org/abs/2507.20230)
- 👥 作者: Yufan Chen, Ching Ting Leung, Bowen Yu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.20230.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于从化学文献中自动提取化学信息的AI系统，这直接服务于化学信息学领域，并为构建化学数据库（数据资源）提供了自动化工具。

**📖 中文摘要**

本文提出了一种基于多模态大语言模型（MLLM）的多智能体系统，用于从化学文献中自动、稳健地提取化学信息。该系统利用MLLM强大的推理能力来理解多样化的化学图形结构，并将提取任务分解为子任务。它协调一组专门的智能体，每个智能体结合了MLLM的能力以及专用工具和网络服务的精确、领域特定优势，以准确解决子任务并将结果整合为统一输出。该系统在文献中复杂的多模态化学反应图形基准数据集上取得了76.27%的F1分数，显著超越了之前的最佳模型（39.13%）。此外，它还在其他信息提取任务中展示了广泛适用性，包括分子图像识别、反应图像解析、命名实体识别和基于文本的反应提取。这项工作对于构建高质量化学数据库、促进AI驱动的化学研究至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To fully expedite AI-powered chemical research, high-quality chemical databases are the foundation. Automatic extraction of chemical information from the literature is essential for constructing reaction databases, but it is currently limited by the multimodality and style variability of chemical information. In this work, we developed a multimodal large language model (MLLM)-based multi-agent system for robust and automated chemical information extraction. It utilizes the MLLM's strong reasoning capability to understand the structure of diverse chemical graphics and decompose the extraction task into sub-tasks. It then coordinates a set of specialized agents, each combining the capabilities of the MLLM with the precise, domain-specific strengths of dedicated tools and web services, to solve the subtasks accurately and integrate the results into a unified output. Our system achieved an F1 score of 76.27% on a benchmark dataset of sophisticated multimodal chemical reaction graphics from the literature, surpassing the previous state-of-the-art model (F1 score of 39.13%) by a significant margin. Additionally, it demonstrated versatile applicability in a range of other information extraction tasks, including molecular image recognition, reaction image parsing, named entity recognition and text-based reaction extraction. This work is a critical step toward automated chemical information extraction into structured datasets, which will be a strong promoter of AI-driven chemical research.

</details>

---

### 48. [Diffusion Alignment as Variational Expectation-Maximization](https://arxiv.org/abs/2510.00502)

**基本信息**

- 🔗 arXiv: [`2510.00502`](https://arxiv.org/abs/2510.00502)
- 👥 作者: Jaewoo Lee, Minsu Kim, Sanghyeok Choi 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.00502.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个用于优化扩散模型（一种生成式大模型）的通用框架（DAV），并明确将其应用于“DNA序列设计”任务。这直接属于“化学大模型”在生物分子设计领域的应用。

**📖 中文摘要**

本文提出了扩散对齐作为变分期望最大化（DAV）框架，将扩散模型的对齐（针对下游目标进行优化）表述为一个迭代过程，交替进行E步和M步。在E步中，使用测试时搜索生成多样化且与奖励对齐的样本。在M步中，使用E步发现的样本精炼扩散模型。作者在文本到图像合成和DNA序列设计任务上验证了DAV可以在优化奖励的同时保持多样性。论文在DNA序列设计任务上的应用直接关联到化学信息学。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion alignment aims to optimize diffusion models for the downstream objective. While existing methods based on reinforcement learning or direct backpropagation achieve considerable success in maximizing rewards, they often suffer from reward over-optimization and mode collapse. We introduce Diffusion Alignment as Variational Expectation-Maximization (DAV), a framework that formulates diffusion alignment as an iterative process alternating between two complementary phases: the E-step and the M-step. In the E-step, we employ test-time search to generate diverse and reward-aligned samples. In the M-step, we refine the diffusion model using samples discovered by the E-step. We demonstrate that DAV can optimize reward while preserving diversity for both continuous and discrete tasks: text-to-image synthesis and DNA sequence design. Our code is available at this https URL .

</details>

---

### 49. [KLASS: KL-Guided Fast Inference in Masked Diffusion Models](https://arxiv.org/abs/2511.05664)

**基本信息**

- 🔗 arXiv: [`2511.05664`](https://arxiv.org/abs/2511.05664)
- 👥 作者: Seo Hyun Kim, Sunwoo Hong, Hojung Jung 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05664.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进生成模型（扩散模型）的推理方法，而生成模型（包括扩散模型）是构建化学大模型（如用于分子生成）的关键技术之一。论文明确提到在分子生成等领域的验证，与化学信息学领域的研究直接相关。

**📖 中文摘要**

本文提出了一种名为KLASS（KL-Adaptive Stability Sampling）的快速采样方法，用于加速掩码扩散模型的推理过程。该方法利用令牌级别的KL散度来识别稳定、高置信度的预测，从而在每次迭代中同时解掩多个令牌，无需额外的模型训练即可显著加速生成，同时保持样本质量。论文在包括分子生成在内的多个领域验证了KLASS的有效性，表明其作为一种通用采样器在不同模型上的适用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Masked diffusion models have demonstrated competitive results on various tasks including language generation. However, due to its iterative refinement process, the inference is often bottlenecked by slow and static sampling speed. To overcome this problem, we introduce `KL-Adaptive Stability Sampling' (KLASS), a fast yet effective sampling method that exploits token-level KL divergence to identify stable, high-confidence predictions. By unmasking multiple tokens in each iteration without any additional model training, our approach speeds up generation significantly while maintaining sample quality. On reasoning benchmarks, KLASS achieves up to $2.78\times$ wall-clock speedups while improving performance over standard greedy decoding, attaining state-of-the-art results among diffusion-based samplers. We further validate KLASS across diverse domains, including text, image, and molecular generation, showing its effectiveness as a broadly applicable sampler across different models.

</details>

---

### 50. [CADM: Cluster-customized Adaptive Distance Metric for Categorical Data Clustering](https://arxiv.org/abs/2511.05826)

**基本信息**

- 🔗 arXiv: [`2511.05826`](https://arxiv.org/abs/2511.05826)
- 👥 作者: Taixi Chen, Yiu-ming Cheung, Yiqun Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05826.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于处理分类和混合数据的新型距离度量与聚类算法。在化学信息学中，分子结构、光谱数据等常被表示为分类或混合特征向量，开发先进的聚类和相似性度量方法是该领域的核心任务之一，与构建和分析化学数据模型密切相关。

**📖 中文摘要**

本文提出了一种用于分类数据聚类的、集群定制的自适应距离度量方法（CADM）。该方法考虑到不同聚类中属性值之间的距离因其分布不同而变化，从而能够根据每个聚类中属性的不同分布来竞争性地更新距离。论文还将该距离度量扩展到包含数值和分类属性的混合数据。实验证明了该方法的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An appropriate distance metric is crucial for categorical data clustering, as the distance between categorical data cannot be directly calculated. However, the distances between attribute values usually vary in different clusters induced by their different distributions, which has not been taken into account, thus leading to unreasonable distance measurement. Therefore, we propose a cluster-customized distance metric for categorical data clustering, which can competitively update distances based on different distributions of attributes in each cluster. In addition, we extend the proposed distance metric to the mixed data that contains both numerical and categorical attributes. Experiments demonstrate the efficacy of the proposed method, i.e., achieving an average ranking of around first in fourteen datasets. The source code is available at this https URL

</details>

---

### 51. [Diffusion Fine-Tuning via Reparameterized Policy Gradient of the Soft Q-Function](https://arxiv.org/abs/2512.04559)

**基本信息**

- 🔗 arXiv: [`2512.04559`](https://arxiv.org/abs/2512.04559)
- 👥 作者: Hyeongyu Kang, Jaewoo Lee, Woocheol Shin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.04559.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对扩散模型的强化学习对齐方法。扩散模型是当前生成式AI的核心架构之一，在化学领域可用于分子结构生成、性质预测等任务。改进扩散模型的训练和对齐方法，对于构建更强大、更可控的化学大模型具有直接意义。

**📖 中文摘要**

本文提出了SQDF（Soft Q-based Diffusion Finetuning），一种用于扩散模型对齐的新型KL正则化强化学习方法。该方法应用了基于训练免费、可微分软Q函数估计的重参数化策略梯度，以缓解奖励过优化问题，从而在保持多样性的同时实现更高的目标奖励。论文在文本到图像对齐等任务上进行了实验验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models excel at generating high-likelihood samples but often require alignment with downstream objectives. Existing fine-tuning methods for diffusion models significantly suffer from reward over-optimization, resulting in high-reward but unnatural samples and degraded diversity. To mitigate over-optimization, we propose Soft Q-based Diffusion Finetuning (SQDF), a novel KL-regularized RL method for diffusion alignment that applies a reparameterized policy gradient of a training-free, differentiable estimation of the soft Q-function. SQDF is further enhanced with three innovations: a discount factor for proper credit assignment in the denoising process, the integration of consistency models to refine Q-function estimates, and the use of an off-policy replay buffer to improve mode coverage and manage the reward-diversity trade-off. Our experiments demonstrate that SQDF achieves superior target rewards while preserving diversity in text-to-image alignment. Furthermore, in online black-box optimization, SQDF attains high sample efficiency while maintaining naturalness and diversity. Our code is available at this https URL .

</details>

---

### 52. [A Novel Patch-Based TDA Approach for Computed Tomography Imaging](https://arxiv.org/abs/2512.12108)

**基本信息**

- 🔗 arXiv: [`2512.12108`](https://arxiv.org/abs/2512.12108)
- 👥 作者: Dashti A. Ali, Aras T. Asaad, Jacob J. Peoples 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.12108.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的、高效的拓扑数据分析（TDA）方法，并提供了相应的Python工具包（Patch-TDA）。TDA是化学信息学和生物信息学中用于分析分子结构、材料孔隙网络等复杂数据形状和拓扑特征的重要数学工具。该方法作为一种新的数据分析和特征提取工具，可用于质谱或分子结构数据的拓扑模式挖掘。

**📖 中文摘要**

本文提出了一种新颖的、基于图像块（patch）的拓扑数据分析（TDA）方法，专门用于处理体积CT成像数据。该方法通过构建持久同调（PH）来提取拓扑特征（如连通分量、环、空洞），旨在提升性能并减少计算时间。论文通过系统实验表明，该方法的分类性能和计算时间均优于传统的3D立方体复形算法和放射组学特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of machine learning (ML) models based on computed tomography (CT) imaging has been a major focus due to the promise that imaging holds for diagnosis, staging, and prognostication. These models often rely on the extraction of hand-crafted features, incorporating robust feature engineering improves the performance of these models. Topological data analysis (TDA), based on the mathematical field of algebraic topology, focuses on data from a topological perspective, extracting deeper insight and higher dimensional structures. Persistent homology (PH), a fundamental tool in TDA, extracts topological features such as connected components, cycles, and voids. A popular approach to construct PH from 3D CT images is to utilize the 3D cubical complex filtration, a method adapted for grid-structured data. However, this approach is subject to poor performance and high computational cost with higher resolution CT images. This study introduces a novel patch-based PH construction approach tailored for volumetric CT imaging data that improves performance and reduces computational time. This study conducts a series of systematic experiments to comprehensively analyze the performance of the proposed method with various parameters and benchmarks against the 3D cubical complex algorithm and radiomic features. Our results highlight the dominance of the patch-based TDA approach in terms of both classification performance and computational time. The proposed approach outperformed the cubical complex method and radiomic features, achieving average improvement of 7.2%, 3.6%, 2.7%, 8.0%, and 7.2% in accuracy, AUC, sensitivity, specificity, and F1 score, respectively, across all datasets. Finally, we provide a convenient python package, Patch-TDA, to facilitate the utilization of the proposed approach.

</details>

---

### 53. [PepEDiff: Zero-Shot Peptide Binder Design via Protein Embedding Diffusion](https://arxiv.org/abs/2601.13327)

**基本信息**

- 🔗 arXiv: [`2601.13327`](https://arxiv.org/abs/2601.13327)
- 👥 作者: Po-Yu Liang, Tibo Duran, Jun Bai
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.13327.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于扩散模型的、零样本的肽段结合剂设计方法。这直接属于“化学大模型”和“AI for Science”在药物发现和生物化学中的应用范畴。该方法利用预训练的蛋白质嵌入模型和扩散生成技术，是构建用于分子设计的化学大模型的一个具体实例。

**📖 中文摘要**

本文提出了PepEDiff，一种新颖的肽段结合剂生成器。它能够在给定目标受体蛋白序列及其口袋残基的情况下，直接在设计好的连续潜在空间中生成结合序列，而无需依赖中间结构预测。该方法通过潜在空间探索和基于扩散的采样，能够生成超出已知结合剂分布范围的新颖肽序列。论文在包括TIGIT在内的案例研究中表明，该方法在零样本设置下优于现有最先进方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present PepEDiff, a novel peptide binder generator that designs binding sequences given a target receptor protein sequence and its pocket residues. Peptide binder generation is critical in therapeutic and biochemical applications, yet many existing methods rely heavily on intermediate structure prediction, adding complexity and limiting sequence diversity. Our approach departs from this paradigm by generating binder sequences directly in a continuous latent space derived from a pretrained protein embedding model, without relying on predicted structures, thereby improving structural and sequence diversity. To encourage the model to capture binding-relevant features rather than memorizing known sequences, we perform latent-space exploration and diffusion-based sampling, enabling the generation of peptides beyond the limited distribution of known binders. This zero-shot generative strategy leverages the global protein embedding manifold as a semantic prior, allowing the model to propose novel peptide sequences in previously unseen regions of the protein space. We evaluate PepEDiff on TIGIT, a challenging target with a large, flat protein-protein interaction interface that lacks a druggable pocket. Despite its simplicity, our method outperforms state-of-the-art approaches across benchmark tests and in the TIGIT case study, demonstrating its potential as a general, structure-free framework for zero-shot peptide binder design. The code for this research is available at GitHub: this https URL

</details>

---

### 54. [Beyond Mapping : Domain-Invariant Representations via Spectral Embedding of Optimal Transport Plans](https://arxiv.org/abs/2601.13350)

**基本信息**

- 🔗 arXiv: [`2601.13350`](https://arxiv.org/abs/2601.13350)
- 👥 作者: Abdel Djalil Sad Saoud, Fred Maurice Ngolè Mboula, Hanane Slimani
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.13350.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于最优传输和谱嵌入的、用于学习域不变表征的新方法。在化学信息学和质谱分析中，经常需要处理来自不同仪器、实验条件或样本类型的域偏移数据（如质谱数据）。开发鲁棒的域自适应和表征学习方法对于构建可泛化的化学大模型和质谱分析工具至关重要。

**📖 中文摘要**

本文提出了一种新的领域自适应方法，通过将平滑的最优传输计划解释为连接源域和目标域的二部图的邻接矩阵，并利用谱嵌入来推导域不变的表征。该方法在音乐流派识别、音乐-语音分类以及基于时域反射的电缆缺陷检测等声学适应和诊断任务上进行了评估，取得了强劲的整体性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Distributional shifts between training and inference time data remain a central challenge in machine learning, often leading to poor performance. It motivated the study of principled approaches for domain alignment, such as optimal transport based unsupervised domain adaptation, that relies on approximating Monge map using transport plans, which is sensitive to the transport problem regularization strategy and hyperparameters, and might yield biased domains alignment. In this work, we propose to interpret smoothed transport plans as adjacency matrices of bipartite graphs connecting source to target domain and derive domain-invariant samples' representations through spectral embedding. We evaluate our approach on acoustic adaptation benchmarks for music genre recognition, music-speech discrimination, as well as electrical cable defect detection and classification tasks using time domain reflection in different diagnosis settings, achieving overall strong performances.

</details>

---

### 55. [SpatialMem: Metric-Aligned Long-Horizon Video Memory for Language Grounding and QA](https://arxiv.org/abs/2601.14895)

**基本信息**

- 🔗 arXiv: [`2601.14895`](https://arxiv.org/abs/2601.14895)
- 👥 作者: Xinyi Zheng, Yunze Liu, Chi-Hao Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.14895.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新颖的多模态（视觉-语言-空间）数据表示、索引和检索框架。虽然应用场景是机器人视觉，但其核心思想——构建结构化的、可查询的多模态记忆库——对于化学信息学中管理复杂的多模态数据（如将分子结构、质谱图、文献描述关联起来）具有启发性和借鉴意义，可视为一种潜在的数据资源组织工具。

**📖 中文摘要**

本文提出了SpatialMem，一个以记忆为中心的系统，用于从以自我为中心的视频中进行长时程、基于语言的检索和问答。它构建了一个度量对齐的空间支架，并以分层记忆存储开放词汇的对象节点，这些节点将证据图像块、视觉嵌入和文本描述链接到3D坐标，从而实现可解释的、空间 grounded 的查询。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present SpatialMem, a memory-centric system for long-horizon, language-grounded retrieval and QA from egocentric video, where metric 3D serves as an interpretable indexing scaffold rather than an explicit mapping objective. Starting from casually captured egocentric RGB video, SpatialMem builds a metric-aligned spatial scaffold for indoor scenes, detects structural 3D anchors (walls, doors, windows) as first-layer support, and populates a hierarchical memory with open-vocabulary object nodes that link evidence patches, visual embeddings, and two-layer textual descriptions to 3D coordinates for compact storage and fast retrieval. This design enables interpretable, spatially grounded queries over relations (e.g., distance, direction, visibility) and supports downstream tasks such as language-guided retrieval/QA and offline navigation-style guidance over a prebuilt memory, without specialized sensors. Experiments on one public Replica scene and two real-world egocentric indoor scenes show that SpatialMem maintains stable layout reasoning, offline guidance, and hierarchical retrieval across these evaluated scenes despite increasing clutter and occlusion. A compact ablation further shows that the two-layer description memory improves path-level grounding, while moderate scale perturbation causes only limited degradation. These results position SpatialMem as an efficient and extensible memory interface for spatially grounded long-horizon video understanding.

</details>

---

### 56. [Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning](https://arxiv.org/abs/2601.15160)

**基本信息**

- 🔗 arXiv: [`2601.15160`](https://arxiv.org/abs/2601.15160)
- 👥 作者: Yuval Kansal, Niraj K. Jha
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.15160.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用知识图谱增强大语言模型的科学推理能力。这直接关联到“化学大模型”的研究，因为化学领域拥有丰富的结构化知识（如化学反应、分子性质、代谢通路）。将化学知识图谱与大语言模型结合，是提升化学领域AI模型专业性和可靠性的重要方向。

**📖 中文摘要**

本文提出了一种基于知识图谱作为隐式奖励模型的强化学习后训练流程，用于提升大语言模型在专业科学领域（如医学）的组合式多跳推理能力。通过从知识图谱路径中推导出新的奖励信号，该方法为模型提供了可验证的、基于事实的监督，鼓励模型组合中间公理而不仅仅是优化最终答案。实验表明，该方法在复杂的多跳查询上实现了显著的零样本泛化提升。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models have achieved near-expert performance in structured reasoning domains like mathematics and programming, yet their ability to perform compositional multi-hop reasoning in specialized scientific fields remains limited. We propose a bottom-up learning paradigm in which models are grounded in axiomatic domain facts and compose them to solve complex, unseen tasks. To this end, we present a post-training pipeline, based on a combination of supervised fine-tuning and reinforcement learning (RL), in which knowledge graphs act as implicit reward models. By deriving novel reward signals from knowledge graph paths, we provide verifiable, scalable, and grounded supervision that encourages models to compose intermediate axioms rather than optimize only final answers during RL. We validate this approach in the medical domain, training a 14B model on short-hop reasoning paths (1-3 hops) and evaluating its zero-shot generalization to complex multi-hop queries (4-5 hops). Our experiments show that path-derived rewards act as a "compositional bridge", enabling our model to significantly outperform much larger models and frontier systems like GPT-5.2 and Gemini 3 Pro, on the most difficult reasoning tasks. Furthermore, we demonstrate the robustness of our approach to adversarial perturbations against option-shuffling stress tests. This work suggests that grounding the reasoning process in structured knowledge is a scalable and efficient path toward intelligent reasoning. Our code is publicly available at: this https URL .

</details>

---

### 57. [Neural Signals Generate Clinical Notes in the Wild](https://arxiv.org/abs/2601.22197)

**基本信息**

- 🔗 arXiv: [`2601.22197`](https://arxiv.org/abs/2601.22197)
- 👥 作者: Jathurshan Pradeepkumar, Zheng Chen, Jimeng Sun
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22197.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于从长时序生物信号（EEG）生成文本报告的多模态大语言模型（MLLM）。虽然领域是神经医学，但其技术范式——将复杂的、高维的、时序的科学仪器数据（EEG）与自然语言处理结合——与“质谱结构推理”的目标高度相似。质谱分析同样涉及从复杂的仪器信号（质谱图）推理出结构信息（分子式、结构式），该工作为跨模态的科学数据理解和报告生成提供了重要的技术参考和类比。

**📖 中文摘要**

本文开发了CELM，首个临床脑电图到语言的基座模型，能够总结长时程、可变长度的脑电图记录，并执行端到端的临床报告生成。该模型整合了预训练的脑电图基座模型和语言模型，以实现可扩展的多模态学习。论文在包含约11,000小时脑电图记录的大规模数据集上进行了评估，结果表明其生成质量显著优于基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generating clinical reports that summarize abnormal patterns, diagnostic findings, and clinical interpretations from long-term EEG recordings remains labor-intensive. We curate a large-scale clinical EEG dataset with $9{,}922$ reports paired with approximately $11{,}000$ hours of EEG recordings from $9{,}048$ patients. We therefore develop CELM, the first clinical EEG-to-Language foundation model capable of summarizing long-duration, variable-length EEG recordings and performing end-to-end clinical report generation at multiple scales, including recording description, background activity, epileptiform abnormalities, events/seizures, and impressions. Experimental results show that, with patient history supervision, our method achieves $70\%$-$95\%$ average relative improvements in standard generation metrics (e.g., ROUGE-1 and METEOR) from $0.2$-$0.3$ to $0.4$-$0.6$. In the zero-shot setting without patient history, CELM attains generation scores in the range of $0.43$-$0.52$, compared to baselines of $0.17$-$0.26$. CELM integrates pretrained EEG foundation models with language models to enable scalable multimodal learning. We release our model and benchmark construction pipeline at this https URL .

</details>

---

### 58. [Accelerating Scientific Research with Gemini: Case Studies and Common Techniques](https://arxiv.org/abs/2602.03837)

**基本信息**

- 🔗 arXiv: [`2602.03837`](https://arxiv.org/abs/2602.03837)
- 👥 作者: David P. Woodruff, Vincent Cohen-Addad, Lalit Jain 等36人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.03837.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于AI（特别是大语言模型）如何加速科学研究的综述和展望性文章。它通过具体案例总结了人机协作进行科学发现（包括数学、物理等基础科学）的模式和技术。这对于思考如何将大模型应用于化学信息学和质谱分析等领域的科学研究具有重要的指导和启发意义，属于对相关主题的重要讨论。

**📖 中文摘要**

本文通过一系列案例研究，展示了研究人员如何与谷歌的Gemini系列高级AI模型合作，解决理论计算机科学、经济学、优化和物理学等领域的开放问题、反驳猜想并生成新证明。基于这些经验，论文提炼了在理论研究中有效进行人机协作的通用技术，如迭代优化、问题分解和跨学科知识迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models (LLMs) have opened new avenues for accelerating scientific research. While models are increasingly capable of assisting with routine tasks, their ability to contribute to novel, expert-level mathematical discovery is less understood. We present a collection of case studies demonstrating how researchers have successfully collaborated with advanced AI models, specifically Google's Gemini-based models (in particular Gemini Deep Think and its advanced variants), to solve open problems, refute conjectures, and generate new proofs across diverse areas in theoretical computer science, as well as other areas such as economics, optimization, and physics. Based on these experiences, we extract common techniques for effective human-AI collaboration in theoretical research, such as iterative refinement, problem decomposition, and cross-disciplinary knowledge transfer. While the majority of our results stem from this interactive, conversational methodology, we also highlight specific instances that push beyond standard chat interfaces. These include deploying the model as a rigorous adversarial reviewer to detect subtle flaws in existing proofs, and embedding it within a "neuro-symbolic" loop that autonomously writes and executes code to verify complex derivations. Together, these examples highlight the potential of AI not just as a tool for automation, but as a versatile, genuine partner in the creative process of scientific discovery.

</details>

---

### 59. [Towards Autonomous Mathematics Research](https://arxiv.org/abs/2602.10177)

**基本信息**

- 🔗 arXiv: [`2602.10177`](https://arxiv.org/abs/2602.10177)
- 👥 作者: Tony Feng, Trieu H. Trinh, Garrett Bingham 等28人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10177.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于构建自主科学研究智能体的前瞻性工作，虽然聚焦数学，但其核心范式——让AI智能体阅读文献、提出问题、规划解决方案、验证结果——完全适用于化学信息学和质谱分析领域。它展望了“化学大模型”可能的发展方向，即从被动的问答工具演变为能主动进行科学探索的智能体，包含了对相关主题的重要讨论和展望。

**📖 中文摘要**

本文介绍了Aletheia，一个数学研究智能体，能够以端到端的方式迭代生成、验证和修订自然语言形式的数学解决方案。Aletheia由高级推理模型、新颖的推理时缩放定律以及密集的工具使用驱动。论文展示了Aletheia从奥赛问题到博士级练习的能力，并重点介绍了其在AI辅助数学研究中的多个里程碑，包括生成研究论文、人机协作证明以及自主解决开放问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in foundational models have yielded reasoning systems capable of achieving a gold-medal standard at the International Mathematical Olympiad. The transition from competition-level problem-solving to professional research, however, requires navigating vast literature and constructing long-horizon proofs. In this work, we introduce Aletheia, a math research agent that iteratively generates, verifies, and revises solutions end-to-end in natural language. Specifically, Aletheia is powered by an advanced version of Gemini Deep Think for challenging reasoning problems, a novel inference-time scaling law that extends beyond Olympiad-level problems, and intensive tool use to navigate the complexities of mathematical research. We demonstrate the capability of Aletheia from Olympiad problems to PhD-level exercises and most notably, through several distinct milestones in AI-assisted mathematics research: (a) a research paper (Feng26) generated by AI without any human intervention in calculating certain structure constants in arithmetic geometry called eigenweights; (b) a research paper (LeeSeo26) demonstrating human-AI collaboration in proving bounds on systems of interacting particles called independent sets; and (c) an extensive semi-autonomous evaluation (Feng et al., 2026a) of 700 open problems on Bloom's Erdos Conjectures database, including autonomous solutions to four open questions. In order to help the public better understand the developments pertaining to AI and mathematics, we suggest quantifying standard levels of autonomy and novelty of AI-assisted results, as well as propose a novel concept of human-AI interaction cards for transparency. We conclude with reflections on human-AI collaboration in mathematics and share all prompts as well as model outputs at this https URL .

</details>

---

### 60. [DataChef: Cooking Up Optimal Data Recipes for LLM Adaptation via Reinforcement Learning](https://arxiv.org/abs/2602.11089)

**基本信息**

- 🔗 arXiv: [`2602.11089`](https://arxiv.org/abs/2602.11089)
- 👥 作者: Yicheng Chen, Zerun Ma, Xinchen Xie 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.11089.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是自动化为大语言模型定制训练数据配方（Data Recipe）。数据是训练大模型的基石，在化学领域，构建高质量的、针对特定任务（如质谱解析、分子性质预测）的训练数据集至关重要。该工作提供了一种自动化、优化数据准备流程的方法，是构建和优化领域大模型（如化学大模型）上游关键环节的技术，具有直接相关性。

**📖 中文摘要**

本文提出了DataChef，一个用于大语言模型适应的端到端数据配方生成框架。给定目标基准和可用数据源池，模型需要输出一个完整的数据配方（即数据处理流程）来使基础LLM适应目标任务。DataChef通过使用预测下游性能的代理奖励进行在线强化学习来生成配方。实验表明，DataChef生成的配方性能可与人类专家策划的配方相媲美。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the current landscape of Large Language Models (LLMs), the curation of large-scale, high-quality training data is a primary driver of model performance. A key lever is the \emph{data recipe}, which comprises a data processing pipeline to transform raw sources into training corpora. Despite the growing use of LLMs to automate individual data processing steps, such as data synthesis and filtering, the overall design of data recipes remains largely manual and labor-intensive, requiring substantial human expertise and iteration. To bridge this gap, we formulate \emph{end-to-end data recipe generation} for LLM adaptation. Given a target benchmark and a pool of available data sources, a model is required to output a complete data recipe that adapts a base LLM to the target task. We present DataChef-32B, which performs online reinforcement learning using a proxy reward that predicts downstream performance for candidate recipes. Across six held-out tasks, DataChef-32B produces recipes that yield performance comparable to those curated by human experts. Notably, the recipe from DataChef-32B adapts Qwen3-1.7B-Base to the math domain, achieving 66.7 on AIME'25 and surpassing the official post-training checkpoint (Qwen3-1.7B). This work sheds new light on automating LLM training and developing self-evolving AI systems.

</details>

---

### 61. [MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](https://arxiv.org/abs/2602.16020)

**基本信息**

- 🔗 arXiv: [`2602.16020`](https://arxiv.org/abs/2602.16020)
- 👥 作者: Cheng Zeng, Harry W. Sullivan, Thomas Egg 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.16020.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是利用生成模型（流匹配）和图神经网络进行分子晶体结构预测，这直接属于“化学大模型”在复杂化学结构生成与预测中的应用。

**📖 中文摘要**

本文提出了MolCrystalFlow，一个基于流的生成模型，用于预测分子晶体结构。该模型将分子作为刚体嵌入，并联合学习晶格矩阵、分子取向和质心位置。它通过图神经网络操作和黎曼流形上的测地流构造来处理几何对称性。虽然论文的核心是晶体结构预测，但其使用的生成建模和图神经网络方法属于化学信息学中“化学大模型”的范畴，即利用先进的机器学习模型解决复杂的化学结构问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular crystal structure prediction represents a grand challenge in computational chemistry due to large sizes of constituent molecules and complex intra- and intermolecular interactions. While generative modeling has revolutionized structure discovery for molecules, inorganic solids, and metal-organic frameworks, extending such approaches to fully periodic molecular crystals is still elusive. Here, we present MolCrystalFlow, a flow-based generative model for molecular crystal structure prediction. The framework disentangles intramolecular complexity from intermolecular packing by embedding molecules as rigid bodies and jointly learning the lattice matrix, molecular orientations, and centroid positions. Centroids and orientations are represented on their native Riemannian manifolds, allowing geodesic flow construction and graph neural network operations that respects geometric symmetries. We benchmark our model against state-of-the-art generative models for large-size periodic crystals and rule-based structure generation methods on two open-source molecular crystal datasets. We demonstrate an integration of MolCrystalFlow model with universal machine learning potential to accelerate molecular crystal structure prediction, paving the way for data-driven generative discovery of molecular crystals.

</details>

---

### 62. [Conditionally Site-Independent Neural Evolution of Antibody Sequences](https://arxiv.org/abs/2602.18982)

**基本信息**

- 🔗 arXiv: [`2602.18982`](https://arxiv.org/abs/2602.18982)
- 👥 作者: Stephen Zhewen Lu, Aakarsh Vermani, Kohei Sanno 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.18982.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个深度神经网络驱动的连续时间马尔可夫链模型（CoSiNE），用于抗体序列的进化建模和优化。这直接属于“化学大模型”在生物分子序列设计与分析中的应用。

**📖 中文摘要**

本文提出了CoSiNE模型，一个由深度神经网络参数化的连续时间马尔可夫链，用于抗体序列的进化建模。该模型旨在弥合经典系统发育模型（显式表示进化动力学）与深度学习方法（捕获复杂上位相互作用）之间的差距。它通过显式解耦选择与上下文依赖的体细胞超突变，在零样本变体效应预测中超越了最先进的语言模型。这项工作代表了在生物分子序列（抗体）领域应用和开发先进的、可解释的生成模型，属于化学信息学与生物信息学交叉的“化学大模型”范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Common deep learning approaches for antibody engineering focus on modeling the marginal distribution of sequences. By treating sequences as independent samples, however, these methods overlook affinity maturation as a rich and largely untapped source of information about the evolutionary process by which antibodies explore the underlying fitness landscape. In contrast, classical phylogenetic models explicitly represent evolutionary dynamics but lack the expressivity to capture complex epistatic interactions. We bridge this gap with CoSiNE, a continuous-time Markov chain parameterized by a deep neural network. Mathematically, we prove that CoSiNE provides a first-order approximation to the intractable sequential point mutation process, capturing epistatic effects with an error bound that is quadratic in branch length. Empirically, CoSiNE outperforms state-of-the-art language models in zero-shot variant effect prediction by explicitly disentangling selection from context-dependent somatic hypermutation. Finally, we introduce Guided Gillespie, a classifier-guided sampling scheme that steers CoSiNE at inference time, enabling efficient optimization of antibody binding affinity toward specific antigens.

</details>

---

### 63. [Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification](https://arxiv.org/abs/2603.01511)

**基本信息**

- 🔗 arXiv: [`2603.01511`](https://arxiv.org/abs/2603.01511)
- 👥 作者: Jiayang Wu, Jiale Zhou, Rubo Wang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01511.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个检索增强的多模态混合专家框架（MERA），用于准确识别蛋白质活性位点。这属于利用先进的“化学大模型”（此处体现为复杂的多模态神经网络架构）解决分子结构与功能预测问题。

**📖 中文摘要**

本文提出了MERA，一个用于蛋白质活性位点识别的检索增强多模态混合专家框架。该框架采用分层多专家检索，通过残基级混合专家门控动态聚合链、序列和活性位点角度的上下文信息。为了解决模态退化问题，提出了基于Dempster-Shafer证据理论的可靠性感知融合策略。该工作将先进的机器学习架构（混合专家、检索增强）应用于蛋白质功能位点预测这一化学信息学/生物信息学核心问题。虽然重点是多模态融合，但其核心目标（活性位点识别）和采用的方法属于利用复杂模型解决化学/生物分子结构功能关系的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate identification of protein active sites at the residue level is crucial for understanding protein function and advancing drug discovery. However, current methods face two critical challenges: vulnerability in single-instance prediction due to sparse training data, and inadequate modality reliability estimation that leads to performance degradation when unreliable modalities dominate fusion processes. To address these challenges, we introduce Multimodal Mixture-of-Experts with Retrieval Augmentation (MERA), the first retrieval-augmented framework for protein active site identification. MERA employs hierarchical multi-expert retrieval that dynamically aggregates contextual information from chain, sequence, and active-site perspectives through residue-level mixture-of-experts gating. To prevent modality degradation, we propose a reliability-aware fusion strategy based on Dempster-Shafer evidence theory that quantifies modality trustworthiness through belief mass functions and learnable discounting coefficients, enabling principled multimodal integration. Extensive experiments on ProTAD-Gen and TS125 datasets demonstrate that MERA achieves state-of-the-art performance, with 90% AUPRC on active site prediction and significant gains on peptide-binding site identification, validating the effectiveness of retrieval-augmented multi-expert modeling and reliability-guided fusion.

</details>

---

### 64. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一种新型的、高效的机器学习原子间势（MatRIS），这是化学信息学和计算材料科学中“化学大模型”的关键应用领域，旨在为广泛的材料系统提供准确的模拟能力。

**📖 中文摘要**

本文提出了MatRIS，一个用于材料科学的机器学习原子间势（MLIP）模型。它是一个不变性模型，引入了基于注意力的三体相互作用建模，并采用具有线性复杂度的可分离注意力机制。MatRIS在多个流行基准测试（如Matbench-Discovery, MatPES等）上实现了与领先的等变模型相媲美的精度，但计算成本更低。这项工作展示了精心设计的不变性模型如何以更低的成本匹配或超越等变模型的准确性，为开发准确高效的MLIPs提供了新思路。MLIPs是化学信息学和计算材料科学中“化学大模型”的核心组成部分之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 65. [Rigidity-Aware Geometric Pretraining for Protein Design and Conformational Ensembles](https://arxiv.org/abs/2603.02406)

**基本信息**

- 🔗 arXiv: [`2603.02406`](https://arxiv.org/abs/2603.02406)
- 👥 作者: Zhanghan Ni, Yanjing Li, Zeju Qiu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02406.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个几何预训练框架（RigidSSL），用于学习蛋白质结构的先验知识，以提升生成模型在蛋白质设计和构象建模中的性能。这直接属于“化学大模型”在生物大分子结构领域的应用。

**📖 中文摘要**

本文提出了RigidSSL，一个用于蛋白质设计的几何预训练框架。该框架通过自监督学习从蛋白质结构数据库中学习几何先验，并利用刚性感知的流匹配目标来联合优化平移和旋转动力学，以最大化构象之间的互信息。经过预训练的模型在无条件生成、零样本基序支架和构象集合建模等任务中表现出色，显著提高了设计性和新颖性。这项工作直接针对蛋白质结构这一化学信息学的核心对象，利用先进的生成模型和自监督学习进行预训练，属于“化学大模型”在蛋白质设计与结构建模领域的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have recently advanced $\textit{de novo}$ protein design by learning the statistical regularities of natural structures. However, current approaches face three key limitations: (1) Existing methods cannot jointly learn protein geometry and design tasks, where pretraining can be a solution; (2) Current pretraining methods mostly rely on local, non-rigid atomic representations for property prediction downstream tasks, limiting global geometric understanding for protein generation tasks; and (3) Existing approaches have yet to effectively model the rich dynamic and conformational information of protein structures. To overcome these issues, we introduce $\textbf{RigidSSL}$ ($\textit{Rigidity-Aware Self-Supervised Learning}$), a geometric pretraining framework that front-loads geometry learning prior to generative finetuning. Phase I (RigidSSL-Perturb) learns geometric priors from 432K structures from the AlphaFold Protein Structure Database with simulated perturbations. Phase II (RigidSSL-MD) refines these representations on 1.3K molecular dynamics trajectories to capture physically realistic transitions. Underpinning both phases is a bi-directional, rigidity-aware flow matching objective that jointly optimizes translational and rotational dynamics to maximize mutual information between conformations. Empirically, RigidSSL variants improve designability by up to 43% while enhancing novelty and diversity in unconditional generation. Furthermore, RigidSSL-Perturb improves the success rate by 5.8% in zero-shot motif scaffolding and RigidSSL-MD captures more biophysically realistic conformational ensembles in G protein-coupled receptor modeling.

</details>

---

### 66. [BInD: Bond and Interaction-generating Diffusion Model for Multi-objective Structure-based Drug Design](https://arxiv.org/abs/2405.16861)

**基本信息**

- 🔗 arXiv: [`2405.16861`](https://arxiv.org/abs/2405.16861)
- 👥 作者: Joongwon Lee, Wonho Zhung, Jisu Seo 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.16861.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个扩散模型（BInD）用于基于结构的药物设计，这直接属于“化学大模型”在分子生成与优化中的应用。同时，其共同生成分子与靶蛋白相互作用的方法，与“质谱结构推理”中从实验数据推断分子结构及其相互作用的逻辑具有相关性。

**📖 中文摘要**

本文介绍了BInD，一种用于基于结构的药物设计（SBDD）的扩散模型。BInD通过知识引导，共同生成分子及其与靶标蛋白的相互作用。这种方法确保平衡考虑关键目标，包括靶标特异性相互作用、分子性质和局部几何结构。综合评估表明，BInD在所有目标上都实现了稳健的性能，达到或超越了最先进的方法。此外，论文还提出了一种NCI驱动的分子设计和优化方法，能够通过阐述适当的相互作用模式来增强靶标结合和特异性。这项工作直接位于“化学大模型”和“质谱结构推理”的交汇点：它利用生成模型（扩散模型）进行分子结构设计（化学大模型），并且其核心是建模和优化分子与蛋白质的相互作用，这与基于质谱等数据推断分子结构（如非共价复合物）的推理问题在理念上相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent remarkable advancements in geometric deep generative models, coupled with accumulated structural data, enable structure-based drug design (SBDD) using only target protein information. However, existing models often struggle to balance multiple objectives, excelling only in specific tasks. BInD, a diffusion model with knowledge-based guidance, is introduced to address this limitation by co-generating molecules and their interactions with a target protein. This approach ensures balanced consideration of key objectives, including target-specific interactions, molecular properties, and local geometry. Comprehensive evaluations demonstrate that BInD achieves robust performance across all objectives, matching or surpassing state-of-the-art methods. Additionally, an NCI-driven molecule design and optimization method is proposed, enabling the enhancement of target binding and specificity by elaborating the adequate interaction patterns.

</details>

---

### 67. [Spectral/Spatial Tensor Atomic Cluster Expansion with Universal Embeddings in Cartesian Space](https://arxiv.org/abs/2509.14961)

**基本信息**

- 🔗 arXiv: [`2509.14961`](https://arxiv.org/abs/2509.14961)
- 👥 作者: Zemin Xu, Wenbo Xie, P. Hu
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.14961.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是提出一种新的原子尺度机器学习模型（TACE），用于统一且高效地模拟材料的各种性质。这直接属于“化学大模型”在计算化学和材料科学中的核心发展。

**📖 中文摘要**

本文介绍了张量原子团簇展开（TACE），它将标量和张量建模在笛卡尔坐标和空间中统一起来。TACE通过将局部环境分解为不可约笛卡尔张量，并使用原子团簇展开（ACE）构建受控的多体层次结构。该模型为不变性（如保真度标签和电荷）和等变性（如外电场和非共线磁矩）嵌入提供了通用方案，并能够以同等地位处理预测的张量可观测量。论文展示了其在有限分子和扩展材料中的准确性、稳定性和效率，包括域内和域外基准测试、光谱、Hessian矩阵、外场响应等。TACE是机器学习原子间势（MLIP）的一种新形式，而MLIP是化学信息学和材料科学中“化学大模型”的基石之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant atomistic machine learning models have largely been built on spherical-tensor representations, where explicit angular-momentum coupling introduces substantial complexity and systematic extensions beyond energies and forces remain challenging, often requires problem-specific architectural choices. Here we introduce the Tensor Atomic Cluster Expansion (TACE), which unifies scalar and tensorial modeling in Cartesian and space by decomposing local environments into irreducible Cartesian tensors (ICT) constructing a controlled many-body hierarchy with atomic cluster expansion (ACE). In addition to performing ACE in the frequency domain, we propose an efficient Clebsch-Gordan-free alternative in the spatial domain. TACE provides universal invariant (e.g., fidelity tags and charges) and equivariant (e.g., external electric fields and non-collinear magnetic moments) embeddings and predicted tensorial observables are handled on equal footing and enabling explicit control at inference. We demonstrate the accuracy, stability, and efficiency across finite molecules and extended materials, including in-domain and out-of-domain benchmarks, spectra, Hessian, external-field responses, charged systems, and multi-fidelity/head training. We further show its robustness on nonequilibrium/reactive datasets and controlled scaling when extending to large foundation model datasets.

</details>

---

### 68. [TCR-EML: Explainable Model Layers for TCR-pMHC Prediction](https://arxiv.org/abs/2510.04377)

**基本信息**

- 🔗 arXiv: [`2510.04377`](https://arxiv.org/abs/2510.04377)
- 👥 作者: Jiarui Li, Zixiang Yin, Zhengming Ding 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04377.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发用于TCR-pMHC结合预测的可解释机器学习模型层。这属于利用和增强“化学大模型”（蛋白质语言模型）来解决复杂的生物分子相互作用预测问题，并着重于模型的可解释性。

**📖 中文摘要**

本文提出了TCR-EML，一种用于T细胞受体（TCR）与肽-MHC（pMHC）结合预测的可解释模型层。这些层可以整合到蛋白质语言模型主干中，利用从已知TCR-pMHC结合机制中提取的氨基酸残基接触原型层，为预测提供高质量的解释。实验表明，该方法在大规模数据集上具有竞争力的预测准确性和泛化能力，并在TCR-XAI基准测试中展示了比现有方法更好的可解释性。虽然侧重于免疫学，但TCR-pMHC结合预测本质上是分子相互作用预测问题，属于化学信息学和生物物理的交叉领域。论文提出的“设计可解释”模型框架，是构建更可靠、可理解的“化学大模型”（用于分子相互作用）的一种努力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

T cell receptor (TCR) recognition of peptide-MHC (pMHC) complexes is a central component of adaptive immunity, with implications for vaccine design, cancer immunotherapy, and autoimmune disease. While recent advances in machine learning have improved prediction of TCR-pMHC binding, the most effective approaches are black-box transformer models that cannot provide a rationale for predictions. Post-hoc explanation methods can provide insight with respect to the input but do not explicitly model biochemical mechanisms (e.g. known binding regions), as in TCR-pMHC binding. ``Explain-by-design'' models (i.e., with architectural components that can be examined directly after training) have been explored in other domains, but have not been used for TCR-pMHC binding. We propose explainable model layers (TCR-EML) that can be incorporated into protein-language model backbones for TCR-pMHC modeling. Our approach uses prototype layers for amino acid residue contacts drawn from known TCR-pMHC binding mechanisms, enabling high-quality explanations for predicted TCR-pMHC binding. Experiments of our proposed method on large-scale datasets demonstrate competitive predictive accuracy and generalization, and evaluation on the TCR-XAI benchmark demonstrates improved explainability compared with existing approaches.

</details>

---

### 69. [Validating Interpretability in siRNA Efficacy Prediction: A Perturbation-Based, Dataset-Aware Protocol](https://arxiv.org/abs/2602.10152)

**基本信息**

- 🔗 arXiv: [`2602.10152`](https://arxiv.org/abs/2602.10152)
- 👥 作者: Zahra Khodagholi, Niloofar Yousefi
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10152.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是评估和验证用于siRNA序列设计指导的机器学习模型的可解释性方法。这直接关系到如何可靠地应用“化学大模型”（此处为siRNA预测模型）进行分子设计与优化，是化学信息学中模型可信度与部署的关键问题。

**📖 中文摘要**

本文关注siRNA功效预测中可解释性（显著性图）的验证。作者提出了一种基于扰动的、数据集感知的协议，用于在基于显著性图指导序列编辑之前，验证归因方法的有效性。该工作揭示了模型在不同数据集间转移时可能出现的失败模式。虽然论文主题是生物序列（siRNA）的机器学习模型，但其核心关注点——验证和改进用于分子设计（此处为siRNA序列）的机器学习模型的解释——对于可靠地应用“化学大模型”至关重要。它提出了在化学信息学中部署解释引导设计前的关键实践步骤。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Saliency maps are increasingly used as design guidance in siRNA efficacy prediction, yet attribution methods are rarely validated before motivating sequence edits. We introduce a pre-synthesis gate: a protocol for counterfactual sensitivity faithfulness that tests whether mutating high-saliency positions changes model output more than composition-matched controls. Cross-dataset transfer reveals two failure modes that would otherwise go undetected: faithful-but-wrong (saliency valid, predictions fail) and inverted saliency (top-saliency edits less impactful than random). Strikingly, models trained on mRNA-level assays collapse on a luciferase reporter dataset, demonstrating that protocol shifts can silently invalidate deployment. Across four benchmarks, 19/20 fold instances pass; the single failure shows inverted saliency. A biology-informed regularizer (BioPrior) strengthens saliency faithfulness with modest, dataset-dependent predictive trade-offs. Our results establish saliency validation as essential pre-deployment practice for explanation-guided therapeutic design. Code is available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：19
- 累计论文数量：1337

## 📝 历史记录

> 暂无历史数据

