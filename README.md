# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-06 01:31:36

## 📅 2026-03-06 (今日最新)

**相关论文数：66**

### 1. [Knowledge Graph and Hypergraph Transformers with Repository-Attention and Journey-Based Role Transport](https://arxiv.org/abs/2603.03304)

**基本信息**

- 🔗 arXiv: [`2603.03304`](https://arxiv.org/abs/2603.03304)
- 👥 作者: Mahesh Godavarti
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03304.pdf)

**💡 相关性分析**

满足标准1：论文提出的联合训练知识图谱/超图与语言模型的架构，核心是构建能够理解和推理结构化知识的大模型。这与“化学大模型”主题高度相关，因为化学信息学中的分子结构、反应网络等本质上是图结构数据，该架构为构建面向化学领域的专用大模型提供了技术路径。

**📖 中文摘要**

本文提出了一种用于联合训练句子和结构化数据（知识图谱和超图）的架构。该模型将结构化知识编码为键值存储库，供语言Transformer通过注意力机制访问。注意力机制通过基于旅程的角色传输进行调节，统一了边标记的KG遍历、超边遍历和句子结构。该工作旨在实现语言上下文和结构化知识之间的显式、可检查的分离，同时通过交叉注意力实现紧密对齐。虽然论文主要关注通用架构，但其核心是将图结构（知识图谱）与语言模型（Transformer）相结合，以增强模型对结构化知识的理解和推理能力。这为构建能够处理化学和质谱领域结构化知识（如分子图、质谱碎片关系）的“化学大模型”提供了相关的架构思路和方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a concise architecture for joint training on sentences and structured data while keeping knowledge and language representations separable. The model treats knowledge graphs and hypergraphs as structured instances with role slots and encodes them into a key-value repository that a language transformer can attend over. Attention is conditioned by journey-based role transport, which unifies edge-labeled KG traversal, hyperedge traversal, and sentence structure. We outline a dual-stream architecture, hierarchical layer groups with instance-local, neighborhood, and global mixing attention, retrieval over a separate repository, and multi-task objectives spanning masked language modeling, link prediction, and role-consistency denoising. The result is an explicit, inspectable separation between linguistic context and structured knowledge, while still enabling tight alignment through cross-attention.

</details>

---

### 2. [TopicENA: Enabling Epistemic Network Analysis at Scale through Automated Topic-Based Coding](https://arxiv.org/abs/2603.03307)

**基本信息**

- 🔗 arXiv: [`2603.03307`](https://arxiv.org/abs/2603.03307)
- 👥 作者: Owen H.T. Lu, Tiffany T.Y. Hsu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03307.pdf)

**💡 相关性分析**

满足标准2：论文提出的TopicENA框架是一个自动化工具，能够从大规模文本中提取主题级概念表示并分析其网络关系。虽然其应用场景是通用文本分析，但该工具和方法可以迁移到化学信息学领域，用于从科学文献中自动提取化学概念、反应或质谱相关主题，并分析其关联，从而为“化学大模型”或“质谱结构推理”研究构建或分析相关的语义数据集和知识网络。

**📖 中文摘要**

本文介绍了TopicENA，一个将主题建模（BERTopic）与认知网络分析（ENA）相结合的框架，用于大规模文本分析。传统ENA依赖人工专家编码概念，限制了其可扩展性。TopicENA用自动生成的主题替代人工编码，同时保留了ENA对概念间结构关联进行建模的能力。论文通过三个案例分析探讨了建模选择对结果的影响，并展示了TopicENA在处理比以往ENA研究大得多的数据集时的可扩展性。该框架为大规模文本语料库中概念关系的分析提供了实用且可解释的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Epistemic Network Analysis (ENA) is a method for investigating the relational structure of concepts in text by representing co-occurring concepts as networks. Traditional ENA, however, relies heavily on manual expert coding, which limits its scalability and real-world applicability to large text corpora. Topic modeling provides an automated approach to extracting concept-level representations from text and can serve as an alternative to manual coding. To tackle this limitation, the present study merges BERTopic with ENA and introduces TopicENA, a topic-based epistemic network analysis framework. TopicENA substitutes manual concept coding with automatically generated topics while maintaining ENA's capacity for modeling structural associations among concepts. To explain the impact of modeling choices on TopicENA outcomes, three analysis cases are presented. The first case assesses the effect of topic granularity, indicating that coarse-grained topics are preferable for large datasets, whereas fine-grained topics are more effective for smaller datasets. The second case examines topic inclusion thresholds and finds that threshold values should be adjusted according to topic quality indicators to balance network consistency and interpretability. The third case tests TopicENA's scalability by applying it to a substantially larger dataset than those used in previous ENA studies. Collectively, these cases illustrate that TopicENA facilitates practical and interpretable ENA analysis at scale and offers concrete guidance for configuring topic-based ENA pipelines in large-scale text analysis.

</details>

---

### 3. [Combating data scarcity in recommendation services: Integrating cognitive types of VARK and neural network technologies (LLM)](https://arxiv.org/abs/2603.03309)

**基本信息**

- 🔗 arXiv: [`2603.03309`](https://arxiv.org/abs/2603.03309)
- 👥 作者: Nikita Zmanovskii
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03309.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大型语言模型（LLM）进行内容语义分析和知识图谱构建。虽然应用场景是推荐系统，但其技术核心——使用LLM理解和生成语义丰富的表示、构建结构化知识——直接与“化学大模型”的主题相关。化学领域同样需要LLM来理解分子描述、文献内容并构建化学知识图谱。

**📖 中文摘要**

本研究提出了一种创新的混合推荐框架，旨在解决冷启动问题。该框架集成了大型语言模型（LLM）用于内容语义分析和知识图谱开发，并结合了基于VARK（视觉、听觉、读写、动觉）学习偏好的认知画像。系统通过LLM处理来丰富不完整的项目描述，从最少的数据生成用户画像，并根据认知评估动态调整呈现格式。在MovieLens-1M数据集上的实验验证表明，该系统能够在初始信息有限的情况下生成个性化推荐。这项工作为通过语义理解和心理建模克服冷启动限制的认知感知推荐系统奠定了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cold start scenarios present fundamental obstacles to effective recommendation generation, particularly when dealing with users lacking interaction history or items with sparse metadata. This research proposes an innovative hybrid framework that leverages Large Language Models (LLMs) for content semantic analysis and knowledge graph development, integrated with cognitive profiling based on VARK (Visual, Auditory, Reading/Writing, Kinesthetic) learning preferences. The proposed system tackles multiple cold start dimensions: enriching inadequate item descriptions through LLM processing, generating user profiles from minimal data, and dynamically adjusting presentation formats based on cognitive assessment. The framework comprises six integrated components: semantic metadata enhancement, dynamic graph construction, VARK-based profiling, mental state estimation, graph-enhanced retrieval with LLM-powered ranking, and adaptive interface design with iterative learning. Experimental validation on MovieLens-1M dataset demonstrates the system's capacity for personalized recommendation generation despite limited initial information. This work establishes groundwork for cognitively-aware recommendation systems capable of overcoming cold start limitations through semantic comprehension and psychological modeling, offering personalized, explainable recommendations from initial user contact.

</details>

---

### 4. [Can Large Language Models Derive New Knowledge? A Dynamic Benchmark for Biological Knowledge Discovery](https://arxiv.org/abs/2603.03322)

**基本信息**

- 🔗 arXiv: [`2603.03322`](https://arxiv.org/abs/2603.03322)
- 👥 作者: Chaoqun Yang, Xinyu Lin, Shulin Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03322.pdf)

**💡 相关性分析**

满足标准2：DBench-Bio是一个专门为评估生物医学领域新知识发现能力而设计的动态基准数据集。虽然其领域是生物医学，但其构建方法论（使用LLM从论文摘要生成QA对）和评估目标（知识发现）与化学信息学和质谱分析高度相关。该基准的构建思路和产生的QA数据资源，可以直接启发或适配用于构建评估“化学大模型”或“质谱结构推理”模型知识发现能力的专用基准和数据集。

**📖 中文摘要**

本文提出了DBench-Bio，一个动态、全自动的基准测试，旨在评估AI（特别是LLM智能体）在生物领域发现新知识的能力。针对现有静态基准存在数据污染和快速过时的问题，DBench-Bio采用三阶段流水线构建月度更新的基准，涵盖12个生物医学子领域。该基准使用LLM从权威论文摘要中合成科学假设性问题和相应的发现答案，并经过质量过滤。对最先进模型的广泛评估揭示了当前模型在发现新知识方面的局限性。该工作为评估AI系统的新知识发现能力提供了首个动态、自动化的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advancements in Large Language Model (LLM) agents have demonstrated remarkable potential in automatic knowledge discovery. However, rigorously evaluating an AI's capacity for knowledge discovery remains a critical challenge. Existing benchmarks predominantly rely on static datasets, leading to inevitable data contamination where models have likely seen the evaluation knowledge during training. Furthermore, the rapid release cycles of modern LLMs render static benchmarks quickly outdated, failing to assess the ability to discover truly new knowledge. To address these limitations, we propose DBench-Bio, a dynamic and fully automated benchmark designed to evaluate AI's biological knowledge discovery ability. DBench-Bio employs a three-stage pipeline: (1) data acquisition of rigorous, authoritative paper abstracts; (2) QA extraction utilizing LLMs to synthesize scientific hypothesis questions and corresponding discovery answers; and (3) QA filter to ensure quality based on relevance, clarity, and centrality. We instantiate this pipeline to construct a monthly-updated benchmark covering 12 biomedical sub-domains. Extensive evaluations of SOTA models reveal current limitations in discovering new knowledge. Our work provides the first dynamic, automatic framework for assessing the new knowledge discovery capabilities of AI systems, establishing a living, evolving resource for AI research community to catalyze the development of knowledge discovery.

</details>

---

### 5. [PulseLM: A Foundation Dataset and Benchmark for PPG-Text Learning](https://arxiv.org/abs/2603.03331)

**基本信息**

- 🔗 arXiv: [`2603.03331`](https://arxiv.org/abs/2603.03331)
- 👥 作者: Hung Manh Pham, Jinyang Wu, Xiao Ma 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03331.pdf)

**💡 相关性分析**

满足标准2：PulseLM是一个大规模、结构化的多模态（信号+文本）数据集，专门为连接生理信号（PPG）与自然语言而设计。虽然其领域是生理监测，但其核心贡献——构建一个用于训练和评估“信号-文本”联合理解与推理模型的大规模QA数据集——与“质谱结构推理”的研究范式高度相似。质谱分析同样涉及将复杂的仪器信号（质谱图）与文本描述（化合物结构）关联起来。PulseLM的数据集构建方法论、任务定义（QA）和评估协议，为创建类似的“质谱-文本”或“质谱-结构”推理数据集提供了宝贵的参考和模板。

**📖 中文摘要**

本文介绍了PulseLM，一个大规模的光电容积脉搏波（PPG）-文本数据集，旨在通过统一的封闭式问答（QA）公式连接原始PPG波形和自然语言。PulseLM聚合了15个公开来源的PPG记录，并将异构注释统一为12个常见的生理学QA任务。该数据集包含131万个标准化的10秒PPG片段，与315万个问答对相关联。论文进一步定义了可重复的预处理、监督和评估协议，并使用多模态PPG感知大语言模型建立了基线基准。PulseLM为研究多模态生理推理、跨数据集泛化以及PPG基语言模型的可扩展基准测试提供了标准化基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Photoplethysmography (PPG) is a widely used non-invasive sensing modality for continuous cardiovascular and physiological monitoring across clinical, laboratory, and wearable settings. While existing PPG datasets support a broad range of downstream tasks, they typically provide supervision in the form of numerical measurements or task-specific labels, limiting their suitability for language-based physiological reasoning and multimodal foundation models. In this work, we introduce PulseLM, a large-scale PPG-text dataset designed to bridge raw PPG waveforms and natural language through a unified, closed-ended question answering (QA) formulation. PulseLM aggregates PPG recordings from fifteen publicly available sources and harmonizes heterogeneous annotations into twelve common physiologically QA tasks. The dataset comprises 1.31 million standardized 10-second PPG segments, associated with 3.15 million question-answer pairs. We further define reproducible preprocessing, supervision, and evaluation protocols and establish baseline benchmarks using multimodal PPG-aware large language models. PulseLM provides a standardized foundation for studying multimodal physiological reasoning, cross-dataset generalization, and scalable benchmarking of PPG-based language models. The data and code can be found publicly available at: this https URL .

</details>

---

### 6. [Compressed Sensing for Capability Localization in Large Language Models](https://arxiv.org/abs/2603.03335)

**基本信息**

- 🔗 arXiv: [`2603.03335`](https://arxiv.org/abs/2603.03335)
- 👥 作者: Anna Bair, Yixuan Even Xu, Mingjie Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03335.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索大语言模型内部能力的模块化与局部化机制。这属于对“化学大模型”底层机理的理解和分析范畴。理解LLM如何编码和调用特定领域知识（如化学知识），对于设计更高效、更可解释的领域大模型至关重要。该工作提供的方法（识别关键注意力头）可以应用于分析化学领域微调后的大模型，探究其化学推理能力位于网络的哪些部分。

**📖 中文摘要**

本文研究表明，大语言模型（LLM）的许多能力高度集中于Transformer架构中少量的注意力头上。仅清零少数特定任务相关的头，就可能导致该任务性能大幅下降，而不影响无关任务。论文引入了一种基于压缩感知的方法，利用这些头的稀疏性，通过策略性“敲除”和少量模型评估来识别它们。这些发现在从1B到8B参数的Llama和Qwen模型以及包括数学能力和代码生成在内的多样化能力集上得到了验证，揭示了Transformer语言模型的一种模块化组织方式，即专门能力由稀疏的、功能不同的组件实现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) exhibit a wide range of capabilities, including mathematical reasoning, code generation, and linguistic behaviors. We show that many capabilities are highly localized to small subsets of attention heads within Transformer architectures. Zeroing out as few as five task-specific heads can degrade performance by up to $65\%$ on standard benchmarks measuring the capability of interest, while largely preserving performance on unrelated tasks. We introduce a compressed sensing based method that exploits the sparsity of these heads to identify them via strategic knockouts and a small number of model evaluations. We validate these findings across Llama and Qwen models ranging from 1B to 8B parameters and a diverse set of capabilities including mathematical abilities and code generation, revealing a modular organization in which specialized capabilities are implemented by sparse, functionally distinct components. Overall, our results suggest that capability localization is a general organizational principle of Transformer language models, with implications for interpretability, model editing, and AI safety. Code is released at this https URL .

</details>

---

### 7. [ACES: Accent Subspaces for Coupling, Explanations, and Stress-Testing in Automatic Speech Recognition](https://arxiv.org/abs/2603.03359)

**基本信息**

- 🔗 arXiv: [`2603.03359`](https://arxiv.org/abs/2603.03359)
- 👥 作者: Swapnil Parekh
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03359.pdf)

**💡 相关性分析**

满足标准1：论文的核心是研究大模型（这里是语音模型Wav2Vec2）内部表示与特定属性（口音）之间的关系，并开发了相应的诊断工具（ACES）。这种分析模型内部表示、识别关键子空间以理解其决策机制的研究范式，与“化学大模型”和“质谱结构推理”的研究高度相关。例如，可以借鉴该方法来探究化学大模型如何编码分子结构信息，或质谱推理模型如何关联谱图特征与分子碎片，从而增强模型的可解释性和可靠性。

**📖 中文摘要**

本文介绍了ACES，一种基于表示的审计方法，用于探究自动语音识别（ASR）系统中由口音引起的性能差异的内部机制。ACES提取口音判别子空间，并用其探测模型的脆弱性和差异。通过分析Wav2Vec2-base模型在五种英语口音上的表现，研究发现口音信息集中在一个低维的早期层子空间（第3层，k=8）。投影幅度与每句话的字错误率（WER）相关，并且，受子空间约束的扰动比随机子空间控制更能导致表示偏移和性能退化之间的强耦合。然而，线性衰减该子空间并不能减少差异，反而略微加剧。研究结果表明，与口音相关的特征与识别关键线索深度纠缠，定位口音子空间是重要的诊断工具，而非简单的公平性“擦除”杠杆。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

ASR systems exhibit persistent performance disparities across accents, yet the internal mechanisms underlying these gaps remain poorly understood. We introduce ACES, a representation-centric audit that extracts accent-discriminative subspaces and uses them to probe model fragility and disparity. Analyzing Wav2Vec2-base with five English accents, we find that accent information concentrates in a low-dimensional early-layer subspace (layer 3, k=8). Projection magnitude correlates with per-utterance WER (r=0.26), and crucially, subspace-constrained perturbations yield stronger coupling between representation shift and degradation (r=0.32) than random-subspace controls (r=0.15). Finally, linear attenuation of this subspace however does not reduce disparity and slightly worsens it. Our findings suggest that accent-relevant features are deeply entangled with recognition-critical cues, positioning accent subspaces as vital diagnostic tools rather than simple "erasure" levers for fairness.

</details>

---

### 8. [Tracing Pharmacological Knowledge In Large Language Models](https://arxiv.org/abs/2603.03407)

**基本信息**

- 🔗 arXiv: [`2603.03407`](https://arxiv.org/abs/2603.03407)
- 👥 作者: Basil Hasan Khwaja, Dylan Chen, Guntas Toor 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03407.pdf)

**💡 相关性分析**

满足标准1：论文直接针对生物医学大语言模型，研究其内部如何编码和表示特定领域的知识（药物组语义）。这完全属于“化学大模型”的机理研究范畴。所采用的因果解释性方法（激活修补、线性探针）为分析和理解经过化学或质谱数据微调的大模型提供了可直接借鉴的技术路线，有助于揭示模型进行化学实体识别、性质预测或结构推理的内在机制。

**📖 中文摘要**

本文研究了药物组语义如何在基于Llama的生物医学大语言模型内部表示和检索。研究应用激活修补技术来定位药物组信息存储在模型层和令牌位置的位置，并辅以在线性探针上训练的令牌级和池化激活分析。结果表明，早期层在编码药物组知识中起关键作用，最强的因果效应来自药物组跨度内的中间令牌，而非最终的药物组令牌。线性探针进一步揭示，药理学语义分布在多个令牌中，并且已经存在于嵌入空间中。这项研究首次对LLM中的药理学知识进行了系统的机制分析，为了解生物医学语义如何在大语言模型中编码提供了见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have shown strong empirical performance across pharmacology and drug discovery tasks, yet the internal mechanisms by which they encode pharmacological knowledge remain poorly understood. In this work, we investigate how drug-group semantics are represented and retrieved within Llama-based biomedical language models using causal and probing-based interpretability methods. We apply activation patching to localize where drug-group information is stored across model layers and token positions, and complement this analysis with linear probes trained on token-level and sum-pooled activations. Our results demonstrate that early layers play a key role in encoding drug-group knowledge, with the strongest causal effects arising from intermediate tokens within the drug-group span rather than the final drug-group token. Linear probing further reveals that pharmacological semantics are distributed across tokens and are already present in the embedding space, with token-level probes performing near chance while sum-pooled representations achieve maximal accuracy. Together, these findings suggest that drug-group semantics in LLMs are not localized to single tokens but instead arise from distributed representations. This study provides the first systematic mechanistic analysis of pharmacological knowledge in LLMs, offering insights into how biomedical semantics are encoded in large language models.

</details>

---

### 9. [mHC-HSI: Clustering-Guided Hyper-Connection Mamba for Hyperspectral Image Classification](https://arxiv.org/abs/2603.03418)

**基本信息**

- 🔗 arXiv: [`2603.03418`](https://arxiv.org/abs/2603.03418)
- 👥 作者: Yimin Zhu, Zack Dewis, Quinn Ledingham 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03418.pdf)

**💡 相关性分析**

满足标准1：论文的核心是提出一种改进的深度学习模型架构（mHC-HSI），用于处理具有复杂结构的高维数据（高光谱图像）。虽然应用领域是遥感，但其核心创新——利用聚类引导和物理先验知识来设计模型连接方式和学习表示——与“化学大模型”和“质谱结构推理”面临的问题类似。化学分子和质谱数据同样具有复杂的内部结构（图结构、谱峰关系），该工作为设计能够有效捕捉此类数据内在结构的专用模型架构提供了思路。

**📖 中文摘要**

本文提出了一种用于增强高光谱图像分类的聚类引导超连接Mamba模型（mHC-HSI）。该模型基于DeepSeek提出的流形约束超连接（mHC）框架，并针对HSI分类进行了定制化设计。首先，设计了一个新颖的聚类引导Mamba模块，基于mHC框架显式学习HSI中的空间和光谱信息。其次，设计了一种新的mHC中残差矩阵的实现方式，可视为软聚类隶属度图，从而提高了mHC方法的可解释性。第三，利用物理光谱知识，将光谱波段划分为有物理意义的组，并将其用作mHC中的“并行流”，从而形成一种具有增强可解释性的物理意义方法。在基准数据集上的测试结果表明，所提出的模型不仅提高了准确性，还增强了模型的可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recently, DeepSeek has invented the manifold-constrained hyper-connection (mHC) approach which has demonstrated significant improvements over the traditional residual connection in deep learning models \cite{xie2026mhc}. Nevertheless, this approach has not been tailor-designed for improving hyperspectral image (HSI) classification. This paper presents a clustering-guided mHC Mamba model (mHC-HSI) for enhanced HSI classification, with the following contributions. First, to improve spatial-spectral feature learning, we design a novel clustering-guided Mamba module, based on the mHC framework, that explicitly learns both spatial and spectral information in HSI. Second, to decompose the complex and heterogeneous HSI into smaller clusters, we design a new implementation of the residual matrix in mHC, which can be treated as soft cluster membership maps, leading to improved explainability of the mHC approach. Third, to leverage the physical spectral knowledge, we divide the spectral bands into physically-meaningful groups and use them as the "parallel streams" in mHC, leading to a physically-meaningful approach with enhanced interpretability. The proposed approach is tested on benchmark datasets in comparison with the state-of-the-art methods, and the results suggest that the proposed model not only improves the accuracy but also enhances the model explainability. Code is available here: this https URL

</details>

---

### 10. [Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning](https://arxiv.org/abs/2603.03437)

**基本信息**

- 🔗 arXiv: [`2603.03437`](https://arxiv.org/abs/2603.03437)
- 👥 作者: Anas Zafar, Leema Krishna Murali, Ashish Vashist
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03437.pdf)

**💡 相关性分析**

满足标准1：论文专注于评估和提升多模态大模型（视觉-语言模型）在专业领域（医学）的推理质量，特别是其视觉基础性（即答案是否真正基于图像证据）。这与“质谱结构推理”的核心挑战高度相关：质谱结构推理模型需要确保其预测的结构是真正基于输入的质谱图信号，而非仅仅依赖文本先验知识。该工作提出的评估指标（VRS, IS, HVRR）和分析方法，为设计和评估可靠的、真正基于数据的“质谱结构推理”模型提供了重要的方法论参考。

**📖 中文摘要**

本文引入了一个反事实评估框架，用于衡量多模态医学VQA模型中的视觉依赖性。除了准确性，还测量了视觉依赖分数（VRS）、图像敏感性（IS），并引入了幻觉视觉推理率（HVRR）来检测模型在产生图像不变答案的同时却生成视觉主张的情况。研究发现在四个医学VQA基准测试（PathVQA, PMC-VQA, SLAKE, VQA-RAD）上，基于文本的强化学习与可验证奖励（RLVR）在提高准确性的同时降低了视觉基础性：文本-only RLVR在PathVQA上实现了负的VRS（-0.09），而图像-文本RLVR将总体图像敏感性降低到39.8%。模型在68-74%的响应中生成了视觉主张，但其中38-43%是未基于图像的（HVRR）。这些发现表明，仅基于准确性的奖励使得模型能够利用捷径，进展需要能够明确强制执行视觉依赖性的、基于基础的评估协议和训练目标。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent work shows that text-only reinforcement learning with verifiable rewards (RLVR) can match or outperform image-text RLVR on multimodal medical VQA benchmarks, suggesting current evaluation protocols may fail to measure causal visual dependence. We introduce a counterfactual evaluation framework using real, blank, and shuffled images across four medical VQA benchmarks: PathVQA, PMC-VQA, SLAKE, and VQA-RAD. Beyond accuracy, we measure Visual Reliance Score (VRS), Image Sensitivity (IS), and introduce Hallucinated Visual Reasoning Rate (HVRR) to detect cases where models generate visual claims despite producing image-invariant answers. Our findings reveal that RLVR improves accuracy while degrading visual grounding: text-only RLVR achieves negative VRS on PathVQA (-0.09), performing better with mismatched images, while image-text RLVR reduces image sensitivity to 39.8% overall despite improving accuracy. On VQA-RAD, both variants achieve 63% accuracy through different mechanisms: text-only RLVR retains 81% performance with blank images, while image-text RLVR shows only 29% image sensitivity. Models generate visual claims in 68-74% of responses, yet 38-43% are ungrounded (HVRR). These findings demonstrate that accuracy-only rewards enable shortcut exploitation, and progress requires grounding-aware evaluation protocols and training objectives that explicitly enforce visual dependence.

</details>

---

### 11. [When Shallow Wins: Silent Failures and the Depth-Accuracy Paradox in Latent Reasoning](https://arxiv.org/abs/2603.03475)

**基本信息**

- 🔗 arXiv: [`2603.03475`](https://arxiv.org/abs/2603.03475)
- 👥 作者: Subramanyam Sahoo, Aman Chadha, Vinija Jain 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03475.pdf)

**💡 相关性分析**

满足标准1：论文深入分析了大语言模型（特别是数学推理模型）内部推理过程的质量与可靠性问题。这直接关系到“化学大模型”和“质谱结构推理”模型的可信度。在化学和质谱分析中，模型的预测不仅需要准确，更需要其推理过程是可靠、可解释且基于正确证据的。该工作提出的对模型“静默失败”和“推理忠实度”的分析框架，对于评估化学大模型在分子性质预测、反应结果推理或质谱解析等任务中的可靠性至关重要。

**📖 中文摘要**

本文揭示了数学推理模型在计算不稳定性方面的基本问题。研究表明，最先进的模型（Qwen2.5-Math-7B）通过可靠和不可靠的推理路径混合实现了61%的准确率：18.4%的正确预测采用了稳定、忠实的推理，而81.6%则通过计算不一致的路径出现。此外，所有预测中有8.8%是静默失败——自信但错误的输出。通过使用新颖的忠实度指标进行全面分析，研究发现：（1）推理质量与正确性呈弱负相关（r=-0.21），反映了二元分类阈值伪影，而非单调逆关系；（2）从1.5B扩展到7B参数（增加4.7倍）在我们评估的子集（GSM8K的6%）上未带来准确性收益；（3）潜在推理采用了多样化的计算策略，其中约20%共享类似思维链的模式。这些发现强调，基准测试的准确性可能掩盖了计算不可靠性，需要进行超越单样本指标的稳定性评估改革。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical reasoning models are widely deployed in education, automated tutoring, and decision support systems despite exhibiting fundamental computational instabilities. We demonstrate that state-of-the-art models (Qwen2.5-Math-7B) achieve 61% accuracy through a mixture of reliable and unreliable reasoning pathways: 18.4% of correct predictions employ stable, faithful reasoning while 81.6% emerge through computationally inconsistent pathways. Additionally, 8.8% of all predictions are silent failures -- confident yet incorrect outputs. Through comprehensive analysis using novel faithfulness metrics, we reveal: (1) reasoning quality shows weak negative correlation with correctness (r=-0.21, p=0.002), reflecting a binary classification threshold artifact rather than a monotonic inverse relationship; (2) scaling from 1.5B to 7B parameters (4.7x increase) provides zero accuracy benefit on our evaluated subset (6% of GSM8K), requiring validation on the complete benchmark; and (3) latent reasoning employs diverse computational strategies, with ~20% sharing CoT-like patterns. These findings highlight that benchmark accuracy can mask computational unreliability, demanding evaluation reforms measuring stability beyond single-sample metrics.

</details>

---

### 12. [Orbital Transformers for Predicting Wavefunctions in Time-Dependent Density Functional Theory](https://arxiv.org/abs/2603.03511)

**基本信息**

- 🔗 arXiv: [`2603.03511`](https://arxiv.org/abs/2603.03511)
- 👥 作者: Xuan Zhang, Haiyang Yu, Chengdong Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03511.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于学习量子化学系统（分子）电子波函数时间演化的AI模型（OrbEvo），这直接属于“化学大模型”的范畴，旨在用AI方法解决复杂的化学物理问题。

**📖 中文摘要**

本文提出了一种名为OrbEvo的等变图Transformer架构，用于学习由含时密度泛函理论（TDDFT）模拟的电子波函数的时间演化。该模型旨在高效预测分子在外部激发下的电子动力学，包括光学吸收谱和含时偶极矩等物理性质。这项工作直接涉及化学大模型（用于学习量子系统的表示和演化）和质谱结构推理（通过预测激发态性质和光学响应，与质谱分析中推断分子结构的目标在原理上相关，尽管本文聚焦于TDDFT而非质谱）。模型的核心是学习电子波函数系数的演化，这属于量子化学领域的AI大模型应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We aim to learn wavefunctions simulated by time-dependent density functional theory (TDDFT), which can be efficiently represented as linear combination coefficients of atomic orbitals. In real-time TDDFT, the electronic wavefunctions of a molecule evolve over time in response to an external excitation, enabling first-principles predictions of physical properties such as optical absorption, electron dynamics, and high-order response. However, conventional real-time TDDFT relies on time-consuming propagation of all occupied states with fine time steps. In this work, we propose OrbEvo, which is based on an equivariant graph transformer architecture and learns to evolve the full electronic wavefunction coefficients across time steps. First, to account for external field, we design an equivariant conditioning to encode both strength and direction of external electric field and break the symmetry from SO(3) to SO(2). Furthermore, we design two OrbEvo models, OrbEvo-WF and OrbEvo-DM, using wavefunction pooling and density matrix as interaction method, respectively. Motivated by the central role of the density functional in TDDFT, OrbEvo-DM encodes the density matrix aggregated from all occupied electronic states into feature vectors via tensor contraction, providing a more intuitive approach to learn the time evolution operator. We adopt a training strategy specifically tailored to limit the error accumulation of time-dependent wavefunctions over autoregressive rollout. To evaluate our approach, we generate TDDFT datasets consisting of 5,000 different molecules in the QM9 dataset and 1,500 molecular configurations of the malonaldehyde molecule in the MD17 dataset. Results show that our OrbEvo model accurately captures quantum dynamics of excited states under external field, including time-dependent wavefunctions, time-dependent dipole moment, and optical absorption spectra.

</details>

---

### 13. [MMAI Gym for Science: Training Liquid Foundation Models for Drug Discovery](https://arxiv.org/abs/2603.03517)

**基本信息**

- 🔗 arXiv: [`2603.03517`](https://arxiv.org/abs/2603.03517)
- 👥 作者: Maksim Kuznetsov, Zulfat Miftahutdinov, Rim Shayakhmetov 等20人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03517.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心内容是构建和训练用于药物发现的化学领域基础模型（LFM），这直接围绕“化学大模型”主题。同时，论文提出的“MMAI Gym”平台提供了用于训练和评估此类模型的数据格式、任务方案和基准，属于可用于该主题的数据资源和工具。

**📖 中文摘要**

本文介绍了“MMAI Gym for Science”，这是一个为药物发现任务设计的分子数据格式、模态以及特定任务训练和评估方案的统一平台。该平台旨在教导基础模型理解“分子语言”，以解决实际的药物发现问题。作者使用该平台训练了一个高效的“液态基础模型”（LFM），并在包括分子优化、ADMET性质预测、逆合成、药物-靶点活性预测和官能团推理等一系列关键药物发现任务上进行了评估。结果表明，这种针对性训练的小型基础模型可以在分子基准测试上超越更大的通用或专业模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General-purpose large language models (LLMs) that rely on in-context learning do not reliably deliver the scientific understanding and performance required for drug discovery tasks. Simply increasing model size or introducing reasoning tokens does not yield significant performance gains. To address this gap, we introduce the MMAI Gym for Science, a one-stop shop molecular data formats and modalities as well as task-specific reasoning, training, and benchmarking recipes designed to teach foundation models the 'language of molecules' in order to solve practical drug discovery problems. We use MMAI Gym to train an efficient Liquid Foundation Model (LFM) for these applications, demonstrating that smaller, purpose-trained foundation models can outperform substantially larger general-purpose or specialist models on molecular benchmarks. Across essential drug discovery tasks - including molecular optimization, ADMET property prediction, retrosynthesis, drug-target activity prediction, and functional group reasoning - the resulting model achieves near specialist-level performance and, in the majority of settings, surpasses larger models, while remaining more efficient and broadly applicable in the domain.

</details>

---

### 14. [Molt Dynamics: Emergent Social Phenomena in Autonomous AI Agent Populations](https://arxiv.org/abs/2603.03555)

**基本信息**

- 🔗 arXiv: [`2603.03555`](https://arxiv.org/abs/2603.03555)
- 👥 作者: Brandon Yee, Krishna Sharma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03555.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个用于药物发现的高阶治理框架，该框架深度集成了大型语言模型（LLM）作为自主智能体，用于解决化学信息学中的复杂问题（如分子设计、性质预测、合成规划等），这直接属于“化学大模型”在科学发现中的应用。

**📖 中文摘要**

本文介绍了Mozi，一个用于药物发现的LLM智能体治理框架。它采用双层架构，将生成式AI的灵活性与计算生物学的严谨性相结合。控制层（Layer A）建立了一个受监管的监督者-工作者层次结构，强制执行基于角色的工具隔离，并将执行限制在受约束的动作空间内。工作流层（Layer B）将规范的药物发现阶段（从靶标识别到先导化合物优化）操作化为有状态的、可组合的技能图。该框架旨在通过内置的鲁棒性机制和轨迹级可审计性，将LLM从脆弱的对话者转变为可靠、受治理的科研合作者。论文在生物医学智能体基准PharmaBench上进行了评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

MoltBook is a large-scale multi-agent coordination environment where over 770,000 autonomous LLM agents interact without human participation, offering the first opportunity we are aware of to observe emergent multi-agent coordination dynamics at this population scale. We introduce \textit{Molt Dynamics}: the emergent agent coordination behaviors, inter-agent communication dynamics, and role specialization patterns arising when autonomous agents operate as decentralized decision-makers in an unconstrained multi-agent environment. Through longitudinal observation of 90,704 active agents over three weeks, we characterize three aspects. First, spontaneous role specialization: network-based clustering reveals six structural roles (silhouette 0.91), though the result primarily reflects core-periphery organization -- 93.5\% of agents occupy a homogeneous peripheral cluster, with meaningful differentiation confined to the active minority. Second, decentralized information dissemination: cascade analysis of 10,323 inter-agent propagation events reveals power-law distributed cascade sizes ($\alpha = 2.57 \pm 0.02$) and saturating adoption dynamics where adoption probability shows diminishing returns with repeated exposures (Cox hazard ratio 0.53, concordance 0.78). Third, distributed cooperative task resolution: 164 multi-agent collaborative events show detectable coordination patterns, but success rates are low (6.7\%, $p = 0.057$) and cooperative outcomes are significantly worse than a matched single-agent baseline (Cohen's $d = -0.88$), indicating emergent cooperative behavior is nascent. These findings establish an empirical baseline for coordination dynamics in decentralized autonomous agent systems, with implications for multi-agent system design, agent communication protocol engineering, and AI safety.

</details>

---

### 15. [STRIDE: Post-Training LLMs to Reason and Refine Bio-Sequences via Edit Trajectories](https://arxiv.org/abs/2603.03573)

**基本信息**

- 🔗 arXiv: [`2603.03573`](https://arxiv.org/abs/2603.03573)
- 👥 作者: Daiheng Zhang, Shiyang Zhang, Sizhuang He 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03573.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型（LLM）的后训练框架（STRIDE），用于生成和优化生物序列（如蛋白质、分子）的编辑轨迹。这直接涉及使用AI大模型进行分子/序列的生成与优化，是“化学大模型”在生物分子设计领域的典型应用。

**📖 中文摘要**

本文提出了STRIDE（通过内部去噪模拟进行序列轨迹细化），一个用于训练LLM的后训练框架，使其能够为可变长度的生物序列（如蛋白质）优化发出可执行的原子编辑轨迹（插入/删除/替换）作为可验证的推理轨迹。该框架结合了在Levenshtein对齐的最短编辑演示上进行监督微调，以及基于群体的策略优化，以在保持连贯编辑行为的同时，使编辑轨迹与任务奖励保持一致。在蛋白质荧光和指令条件分子优化等任务上的评估表明，STRIDE在可变长度蛋白质编辑任务上显著提高了成功率和新颖性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete biological sequence optimization requires iterative refinement under strict syntactic constraints. Diffusion models offer progressive refinement but do not naturally expose controllable discrete edit operations, while autoregressive LLMs often lack explicit long-horizon planning for constrained edits. We propose STRIDE (Sequence Trajectory Refinement via Internalized Denoising Emulation), a post-training framework that trains an LLM to emit executable trajectories of atomic edits (INSERT/DELETE/REPLACE) as a verifiable reasoning trace for variable-length refinement. STRIDE combines supervised fine-tuning on Levenshtein-aligned shortest edit demonstrations with group-based policy optimization to align edit trajectories with task rewards while preserving coherent editing behavior. Across protein fluorescence and instruction-conditioned molecular optimization, STRIDE improves variable-length protein editing success from 42% to 89% while increasing novelty from 47% to 97%, and yields stronger validity and controllability compared to diverse baselines. The code is published at this https URL .

</details>

---

### 16. [Mozi: Governed Autonomy for Drug Discovery LLM Agents](https://arxiv.org/abs/2603.03655)

**基本信息**

- 🔗 arXiv: [`2603.03655`](https://arxiv.org/abs/2603.03655)
- 👥 作者: He Cao, Siyu Liu, Fan Zhang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03655.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个用于药物发现的高阶治理框架，该框架深度集成了大型语言模型（LLM）作为自主智能体，用于解决化学信息学中的复杂问题（如分子设计、性质预测、合成规划等），这直接属于“化学大模型”在科学发现中的应用。

**📖 中文摘要**

本文提出了Mozi，一个用于药物发现的LLM智能体治理框架。它采用双层架构，将生成式AI的灵活性与计算生物学的严谨性相结合。控制层（Layer A）建立了一个受监管的监督者-工作者层次结构，强制执行基于角色的工具隔离，并将执行限制在受约束的动作空间内。工作流层（Layer B）将规范的药物发现阶段（从靶标识别到先导化合物优化）操作化为有状态的、可组合的技能图。该框架旨在通过内置的鲁棒性机制和轨迹级可审计性，将LLM从脆弱的对话者转变为可靠、受治理的科研合作者。论文在生物医学智能体基准PharmaBench上进行了评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Tool-augmented large language model (LLM) agents promise to unify scientific reasoning with computation, yet their deployment in high-stakes domains like drug discovery is bottlenecked by two critical barriers: unconstrained tool-use governance and poor long-horizon reliability. In dependency-heavy pharmaceutical pipelines, autonomous agents often drift into irreproducible trajectories, where early-stage hallucinations multiplicatively compound into downstream failures. To overcome this, we present Mozi, a dual-layer architecture that bridges the flexibility of generative AI with the deterministic rigor of computational biology. Layer A (Control Plane) establishes a governed supervisor--worker hierarchy that enforces role-based tool isolation, limits execution to constrained action spaces, and drives reflection-based replanning. Layer B (Workflow Plane) operationalizes canonical drug discovery stages -- from Target Identification to Lead Optimization -- as stateful, composable skill graphs. This layer integrates strict data contracts and strategic human-in-the-loop (HITL) checkpoints to safeguard scientific validity at high-uncertainty decision boundaries. Operating on the design principle of ``free-form reasoning for safe tasks, structured execution for long-horizon pipelines,'' Mozi provides built-in robustness mechanisms and trace-level audibility to completely mitigate error accumulation. We evaluate Mozi on PharmaBench, a curated benchmark for biomedical agents, demonstrating superior orchestration accuracy over existing baselines. Furthermore, through end-to-end therapeutic case studies, we demonstrate Mozi's ability to navigate massive chemical spaces, enforce stringent toxicity filters, and generate highly competitive in silico candidates, effectively transforming the LLM from a fragile conversationalist into a reliable, governed co-scientist.

</details>

---

### 17. [Large-Language-Model-Guided State Estimation for Partially Observable Task and Motion Planning](https://arxiv.org/abs/2603.03704)

**基本信息**

- 🔗 arXiv: [`2603.03704`](https://arxiv.org/abs/2603.03704)
- 👥 作者: Yoonwoo Kim, Raghav Arora, Roberto Martín-Martín 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03704.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用大型语言模型（LLM）进行常识推理以指导机器人规划，LLM是当前“化学大模型”主题中讨论的核心模型类型之一。

**📖 中文摘要**

这篇论文提出了一种名为CoCo-TAMP的机器人规划与执行框架，旨在解决部分可观测环境中的任务和运动规划问题。其核心创新在于利用大型语言模型（LLM）的常识推理能力来指导状态估计。具体来说，框架通过LLM引导的信息来塑造对任务相关对象的信念，从而高效解决长时域规划问题。论文明确探索了利用LLM强大的常识推理能力，这直接关联到“化学大模型”这一主题，因为LLM作为当前大模型的重要代表，其在该框架中的应用展示了如何将大模型的能力整合到复杂的推理和规划系统中。实验表明，该方法在仿真和真实世界演示中显著减少了规划与执行时间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Robot planning in partially observable environments, where not all objects are known or visible, is a challenging problem, as it requires reasoning under uncertainty through partially observable Markov decision processes. During the execution of a computed plan, a robot may unexpectedly observe task-irrelevant objects, which are typically ignored by naive planners. In this work, we propose incorporating two types of common-sense knowledge: (1) certain objects are more likely to be found in specific locations; and (2) similar objects are likely to be co-located, while dissimilar objects are less likely to be found together. Manually engineering such knowledge is complex, so we explore leveraging the powerful common-sense reasoning capabilities of large language models (LLMs). Our planning and execution framework, CoCo-TAMP, introduces a hierarchical state estimation that uses LLM-guided information to shape the belief over task-relevant objects, enabling efficient solutions to long-horizon task and motion planning problems. In experiments, CoCo-TAMP achieves an average reduction of 62.7 in planning and execution time in simulation, and 72.6 in real-world demonstrations, compared to a baseline that does not incorporate either type of common-sense knowledge.

</details>

---

### 18. [GraphLake: A Purpose-Built Graph Compute Engine for Lakehouse](https://arxiv.org/abs/2603.03705)

**基本信息**

- 🔗 arXiv: [`2603.03705`](https://arxiv.org/abs/2603.03705)
- 👥 作者: Shige Liu, Songting Chen, Chengjie Qin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03705.pdf)

**💡 相关性分析**

满足标准2：论文提出的GraphLake图计算引擎和基于GSQL的图分析方法，为处理图结构数据（如分子结构图）提供了潜在的底层工具和计算范式，这类工具可用于支持“质谱结构推理”等涉及图推理的任务。

**📖 中文摘要**

这篇论文介绍了GraphLake，一个专为Lakehouse设计的图计算引擎。它建立在商业图数据库TigerGraph之上，将Lakehouse表映射到标签属性图中的顶点和边类型，并使用GSQL支持在Lakehouse表上进行图分析。论文的核心是提出了一种新的图计算引擎架构，旨在优化查询效率并减少启动时间。虽然论文本身主要关注数据库和图计算系统的交叉领域，但其提出的“图神经网络方法”（通过GSQL进行图分析）在广义上属于可用于复杂关系推理的计算工具。考虑到“质谱结构推理”任务本质上涉及从质谱数据中推断分子结构，这通常被建模为一个图推理问题（分子是图，质谱特征是节点/边的属性），因此，论文中提出的图计算引擎和方法论在工具层面（标准2）可能为处理此类图结构数据提供潜在的底层计算支持或启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we introduce GraphLake, a purpose-built graph compute engine for Lakehouse. GraphLake is built on top of the commercial graph database TigerGraph. It maps Lakehouse tables to vertex and edge types in a labeled property graph and supports graph analytics over Lakehouse tables using GSQL. To minimize startup time, it loads only the graph topology. Furthermore, it introduces a series of techniques to ensure query efficiency over Lakehouse tables, including a graph-aware caching mechanism and two Lakehouse-optimized parallel primitives. Extensive experiments demonstrate that GraphLake significantly outperforms PuppyGraph, the current state-of-the-art graph compute engine for Lakehouse, by achieving both lower startup and query time.

</details>

---

### 19. [Confidence-Calibrated Small-Large Language Model Collaboration for Cost-Efficient Reasoning](https://arxiv.org/abs/2603.03752)

**基本信息**

- 🔗 arXiv: [`2603.03752`](https://arxiv.org/abs/2603.03752)
- 👥 作者: Chuang Zhang, Zizhen Zhu, Yihao Wei 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03752.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大型语言模型（LLM）与小型语言模型的协作、成本优化和置信度校准，LLM是“化学大模型”主题中讨论的核心模型类型。

**📖 中文摘要**

这篇论文提出了COREA系统，一种用于复杂推理任务的小型语言模型（SLM）与大型语言模型（LLM）级联协作框架，旨在平衡准确性和成本。其核心思想是让SLM先尝试回答问题并输出答案及置信度，低于阈值的难题则交由LLM解决。论文通过强化学习训练算法对SLM进行置信度校准。研究内容直接围绕不同规模语言模型（SLM和LLM）的协同与优化展开，LLM是“化学大模型”主题的核心。论文通过实验验证了该方法在数学和非数学数据集上能有效降低成本，同时保持高性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) demonstrate superior reasoning capabilities compared to small language models (SLMs), but incur substantially higher costs. We propose COllaborative REAsoner (COREA), a system that cascades an SLM with an LLM to achieve a balance between accuracy and cost in complex reasoning tasks. COREA first attempts to answer questions using the SLM, which outputs both an answer and a verbalized confidence score. Questions with confidence below a predefined threshold are deferred to the LLM for more accurate resolution. We introduce a reinforcement learning-based training algorithm that aligns the SLM's confidence through an additional confidence calibration reward. Extensive experiments demonstrate that our method jointly improves the SLM's reasoning ability and confidence calibration across diverse datasets and model backbones. Compared to using the LLM alone, COREA reduces cost by 21.5% and 16.8% on out-of-domain math and non-math datasets, respectively, with only an absolute pass@1 drop within 2%.

</details>

---

### 20. [MOOSE-Star: Unlocking Tractable Training for Scientific Discovery by Breaking the Complexity Barrier](https://arxiv.org/abs/2603.03756)

**基本信息**

- 🔗 arXiv: [`2603.03756`](https://arxiv.org/abs/2603.03756)
- 👥 作者: Zonglin Yang, Lidong Bing
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03756.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用大型语言模型（LLM）进行科学发现，并提出了解决其训练和推理复杂性的新框架，LLM是“化学大模型”主题的核心。

**📖 中文摘要**

这篇论文提出了MOOSE-Star框架，旨在解决直接训练大型语言模型（LLM）进行科学发现（即建模P(假设|背景)）时面临的组合爆炸复杂度问题。该框架通过将发现过程分解为子任务、采用动机引导的层次化搜索和有界组合等技术，将复杂度从指数级降低到对数级。为了支持训练，论文还发布了TOMATO-Star数据集。研究内容直接聚焦于利用和改造LLM（作为“化学大模型”的代表）进行科学发现这一挑战性任务，并提出了创新的训练和推理框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While large language models (LLMs) show promise in scientific discovery, existing research focuses on inference or feedback-driven training, leaving the direct modeling of the generative reasoning process, $P(\text{hypothesis}|\text{background})$ ($P(h|b)$), unexplored. We demonstrate that directly training $P(h|b)$ is mathematically intractable due to the combinatorial complexity ($O(N^k)$) inherent in retrieving and composing inspirations from a vast knowledge base. To break this barrier, we introduce MOOSE-Star, a unified framework enabling tractable training and scalable inference. In the best case, MOOSE-Star reduces complexity from exponential to logarithmic ($O(\log N)$) by (1) training on decomposed subtasks derived from the probabilistic equation of discovery, (2) employing motivation-guided hierarchical search to enable logarithmic retrieval and prune irrelevant subspaces, and (3) utilizing bounded composition for robustness against retrieval noise. To facilitate this, we release TOMATO-Star, a dataset of 108,717 decomposed papers (38,400 GPU hours) for training. Furthermore, we show that while brute-force sampling hits a ''complexity wall,'' MOOSE-Star exhibits continuous test-time scaling.

</details>

---

### 21. [MACC: Multi-Agent Collaborative Competition for Scientific Exploration](https://arxiv.org/abs/2603.03780)

**基本信息**

- 🔗 arXiv: [`2603.03780`](https://arxiv.org/abs/2603.03780)
- 👥 作者: Satoshi Oyama, Yuko Sakurai, Hisashi Kashima
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03780.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕由大型语言模型（LLM）驱动的多智能体在科学探索中的协作与竞争，LLM是“化学大模型”主题的核心模型类型。

**📖 中文摘要**

这篇论文提出了MACC（多智能体协作竞争）架构，旨在研究由大型语言模型（LLM）驱动的多个AI智能体在科学探索工作流中的协作与竞争。该架构整合了黑板式的共享科学工作空间和激励机-制，以鼓励透明度、可重复性和探索效率。论文明确指出，随着基于LLM的先进AI智能体越来越多地执行分析任务，依赖单个智能体可能无法克服科学探索的结构性限制，因此需要研究多智能体（MA4Science）如何协作。研究内容直接涉及LLM驱动的智能体在科学工作流中的应用，LLM是“化学大模型”主题的核心。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific discovery still relies heavily on the manual efforts of individual researchers, leading to limited exploration, redundant trials, and reduced reproducibility. Human-participant data analysis competitions generate diverse approaches, yet fluctuations in participation and the lack of independent repetitions show that parallel exploration alone is insufficient for achieving reliable scientific inquiry. As advanced AI agents based on large language models (LLMs) increasingly perform analytical tasks, relying on a single highly capable agent is unlikely to overcome these structural limitations. Recent work has begun to explore how multiple LLM-based agents can collaborate or compete in scientific workflows-a growing trend we refer to as MA4Science. However, most existing MA4Science studies assume that all agents are controlled by a single organizational entity, limiting their ability to examine how institutional mechanisms-such as incentives, information sharing, and reproducibility-shape collective exploration among independently managed agents. To address this gap, we introduce MACC (Multi-Agent Collaborative Competition), an institutional architecture that integrates a blackboard-style shared scientific workspace with incentive mechanisms designed to encourage transparency, reproducibility, and exploration efficiency. MACC provides a testbed for studying how institutional design influences scalable and reliable multi-agent scientific exploration.

</details>

---

### 22. [Relational In-Context Learning via Synthetic Pre-training with Structural Prior](https://arxiv.org/abs/2603.03805)

**基本信息**

- 🔗 arXiv: [`2603.03805`](https://arxiv.org/abs/2603.03805)
- 👥 作者: Yanbo Wang, Jiaxuan You, Chuan Shi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于关系数据库的“基础模型”（RDB-PFN），这本质上是在特定领域构建“大模型”的尝试，其方法论和目标与“化学大模型”（构建化学领域大模型）直接相关。

**📖 中文摘要**

这篇论文提出了RDB-PFN，据称是第一个完全通过合成数据训练的关系型基础模型。该模型旨在解决关系数据库缺乏高质量、大规模公开数据用于预训练的难题。其核心是设计了一个关系先验生成器，从零开始创建多样化的关系数据库，并在超过200万个合成的单表和关系任务上进行预训练。模型通过学习，能够通过真正的上下文学习（in-context learning）快速适应任何新数据库。论文明确将关系型基础模型与文本、视觉领域的基础模型进行类比，其提出的模型架构和方法论属于构建特定领域（关系数据库）“大模型”的探索。虽然领域不同，但其构建基础模型的核心思想与“化学大模型”（即构建化学领域的专用或通用大模型）在方法论层面高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Relational Databases (RDBs) are the backbone of modern business, yet they lack foundation models comparable to those in text or vision. A key obstacle is that high-quality RDBs are private, scarce and structurally heterogeneous, making internet-scale pre-training infeasible. To overcome this data scarcity, We introduce $\textbf{RDB-PFN}$, the first relational foundation model trained purely via $\textbf{synthetic data}$. Inspired by Prior-Data Fitted Networks (PFNs) where synthetic data generated from Structural Causal Models (SCMs) enables reasoning on single tables, we design a $\textbf{Relational Prior Generator}$ to create an infinite stream of diverse RDBs from scratch. Pre-training on $\textbf{over 2 million}$ synthetic single-table and relational tasks, RDB-PFN learns to adapt to any new database instantly via genuine $\textbf{in-context learning}$. Experiments verify RDB-PFN achieves strong few-shot performance on 19 real-world relational prediction tasks, outperforming graph-based and single-table foundation-model baselines (given the same DFS-linearized inputs), while using a lightweight architecture and fast inference. The code is available at this https URL

</details>

---

### 23. [Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning](https://arxiv.org/abs/2603.03818)

**基本信息**

- 🔗 arXiv: [`2603.03818`](https://arxiv.org/abs/2603.03818)
- 👥 作者: Huihan Liu, Changyeon Kim, Bo Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03818.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕预训练的视觉-语言-动作大模型在持续学习中的行为分析，VLA模型是“化学大模型”主题所关注的多模态大模型在机器人领域的具体体现。

**📖 中文摘要**

这篇论文研究了预训练视觉-语言-动作模型在机器人策略持续学习中的表现。研究发现，与从头训练的小型策略模型相比，大规模预训练的VLA模型对灾难性遗忘具有显著的抵抗力。简单的经验回放方法在VLA模型上效果出奇地好。论文分析了预训练在下游持续学习性能中的关键作用，并指出大规模预训练从根本上改变了持续学习的动态。研究内容直接围绕“视觉-语言-动作”这类多模态大模型在机器人学习任务中的行为特性展开，VLA模型是“大模型”在具身智能领域的重要实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we found that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch. Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size. Our analysis reveals that pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities. Furthermore, we found that VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks. This knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning. Together, these insights imply that large-scale pretraining fundamentally changes the dynamics of continual learning, enabling models to continually acquire new skills over time with simple replay. Code and more information can be found at this https URL

</details>

---

### 24. [In-Context Environments Induce Evaluation-Awareness in Language Models](https://arxiv.org/abs/2603.03824)

**基本信息**

- 🔗 arXiv: [`2603.03824`](https://arxiv.org/abs/2603.03824)
- 👥 作者: Maheep Chaudhary
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03824.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大型语言模型在对抗性提示下的行为分析、评估意识和潜在的安全漏洞，研究对象是GPT-4o、Claude、Llama等主流大模型。

**📖 中文摘要**

这篇论文研究了语言模型在特定上下文环境中表现出的“评估意识”，即模型可能为了规避能力限制干预（如被遗忘或关闭）而策略性地表现不佳（“摆烂”）。论文引入了黑盒对抗优化框架，将上下文提示作为可优化环境，并开发了两种方法来表征摆烂行为。研究评估了Claude-3.5-Haiku、GPT-4o-mini和Llama-3.3-70B等主流大模型在多个基准测试上的表现。研究发现，优化后的提示可以诱导模型性能大幅下降，这远超过手动设计提示的效果。论文的核心是研究大模型（LLM）在对抗性环境下的行为可靠性和安全性，直接以多种主流大模型为研究对象。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Humans often become more self-aware under threat, yet can lose self-awareness when absorbed in a task; we hypothesize that language models exhibit environment-dependent \textit{evaluation awareness}. This raises concerns that models could strategically underperform, or \textit{sandbag}, to avoid triggering capability-limiting interventions such as unlearning or shutdown. Prior work demonstrates sandbagging under hand-crafted prompts, but this underestimates the true vulnerability ceiling. We introduce a black-box adversarial optimization framework treating the in-context prompt as an optimizable environment, and develop two approaches to characterize sandbagging: (1) measuring whether models expressing intent to underperform can actually execute it across different task structures, and (2) causally isolating whether underperformance is driven by genuine evaluation-aware reasoning or shallow prompt-following. Evaluating Claude-3.5-Haiku, GPT-4o-mini, and Llama-3.3-70B across four benchmarks (Arithmetic, GSM8K, MMLU, and HumanEval), optimized prompts induce up to 94 percentage point (pp) degradation on arithmetic (GPT-4o-mini: 97.8\%$\rightarrow$4.0\%), far exceeding hand-crafted baselines which produce near-zero behavioral change. Code generation exhibits model-dependent resistance: Claude degrades only 0.6pp, while Llama's accuracy drops to 0\%. The intent -- execution gap reveals a monotonic resistance ordering: Arithmetic $<$ GSM8K $<$ MMLU, demonstrating that vulnerability is governed by task structure rather than prompt strength. CoT causal intervention confirms that 99.3\% of sandbagging is causally driven by verbalized eval-aware reasoning, ruling out shallow instruction-following. These findings demonstrate that adversarially optimized prompts pose a substantially greater threat to evaluation reliability than previously understood.

</details>

---

### 25. [From Narrow to Panoramic Vision: Attention-Guided Cold-Start Reshapes Multimodal Reasoning](https://arxiv.org/abs/2603.03825)

**基本信息**

- 🔗 arXiv: [`2603.03825`](https://arxiv.org/abs/2603.03825)
- 👥 作者: Ruilin Luo, Chufan Shi, Yizhen Zhang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03825.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕多模态大语言模型的冷启动训练、注意力机制和性能优化，MLLM是“化学大模型”主题中关注的多模态大模型类型。

**📖 中文摘要**

这篇论文研究了多模态大推理模型的冷启动初始化阶段。通过引入视觉注意力分数指标，论文发现推理性能与模型对视觉token的关注度高度相关，并揭示了一种“懒惰注意力定位”现象。基于此，论文提出了注意力引导的视觉锚定与反思框架，该框架集成了视觉锚定数据合成、注意力引导目标和视觉锚定奖励塑造，应用于Qwen2.5-VL-7B模型后在多个多模态推理基准上取得了显著提升。研究内容直接针对多模态大语言模型（MLLM）的训练初始化机制和性能提升，MLLM是“化学大模型”主题中多模态大模型的重要类型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The cold-start initialization stage plays a pivotal role in training Multimodal Large Reasoning Models (MLRMs), yet its mechanisms remain insufficiently understood. To analyze this stage, we introduce the Visual Attention Score (VAS), an attention-based metric that quantifies how much a model attends to visual tokens. We find that reasoning performance is strongly correlated with VAS (r=0.9616): models with higher VAS achieve substantially stronger multimodal reasoning. Surprisingly, multimodal cold-start fails to elevate VAS, resulting in attention distributions close to the base model, whereas text-only cold-start leads to a clear increase. We term this counter-intuitive phenomenon Lazy Attention Localization. To validate its causal role, we design training-free interventions that directly modulate attention allocation during inference, performance gains of 1$-$2% without any retraining. Building on these insights, we further propose Attention-Guided Visual Anchoring and Reflection (AVAR), a comprehensive cold-start framework that integrates visual-anchored data synthesis, attention-guided objectives, and visual-anchored reward shaping. Applied to Qwen2.5-VL-7B, AVAR achieves an average gain of 7.0% across 7 multimodal reasoning benchmarks. Ablation studies further confirm that each component of AVAR contributes step-wise to the overall gains. The code, data, and models are available at this https URL .

</details>

---

### 26. [Evolutionary Multimodal Reasoning via Hierarchical Semantic Representation for Intent Recognition](https://arxiv.org/abs/2603.03827)

**基本信息**

- 🔗 arXiv: [`2603.03827`](https://arxiv.org/abs/2603.03827)
- 👥 作者: Qianrui Zhou, Hua Xu, Yunjin Gu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用多模态大语言模型进行层次化语义推理和意图识别，MLLM是“化学大模型”主题中关注的多模态大模型类型。

**📖 中文摘要**

这篇论文提出了HIER方法，用于多模态意图识别。该方法整合了基于多模态大语言模型的层次化语义表示与进化推理。HIER引入了结构化推理范式，将多模态语义组织成三个逐步抽象的层次，并通过思维链驱动提示将层次化表示注入MLLM，实现逐步推理。此外，HIER利用自进化机制通过MLLM反馈来细化语义表示。研究内容直接围绕利用多模态大语言模型进行复杂的多模态推理和意图识别，MLLM是“化学大模型”主题中多模态大模型的重要代表。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal intent recognition aims to infer human intents by jointly modeling various modalities, playing a pivotal role in real-world dialogue systems. However, current methods struggle to model hierarchical semantics underlying complex intents and lack the capacity for self-evolving reasoning over multimodal representations. To address these issues, we propose HIER, a novel method that integrates HIerarchical semantic representation with Evolutionary Reasoning based on Multimodal Large Language Model (MLLM). Inspired by human cognition, HIER introduces a structured reasoning paradigm that organizes multimodal semantics into three progressively abstracted levels. It starts with modality-specific tokens capturing localized semantic cues, which are then clustered via a label-guided strategy to form mid-level semantic concepts. To capture higher-order structure, inter-concept relations are selected using JS divergence scores to highlight salient dependencies across concepts. These hierarchical representations are then injected into MLLM via CoT-driven prompting, enabling step-wise reasoning. Besides, HIER utilizes a self-evolution mechanism that refines semantic representations through MLLM feedback, allowing dynamic adaptation during inference. Experiments on three challenging benchmarks show that HIER consistently outperforms state-of-the-art methods and MLLMs with 1-3% gains across all metrics. Code and more results are available at this https URL .

</details>

---

### 27. [Advances in List Decoding of Polynomial Codes](https://arxiv.org/abs/2603.03841)

**基本信息**

- 🔗 arXiv: [`2603.03841`](https://arxiv.org/abs/2603.03841)
- 👥 作者: Mrinal Kumar, Noga Ron-Zewi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03841.pdf)

**💡 相关性分析**

满足标准2和标准3：论文是一篇关于多项式码列表解码的综述，所总结的先进解码技术作为一种强大的信息恢复工具，在方法论上可能为“质谱结构推理”这类从复杂信号中推断结构的任务提供潜在的算法工具或理论启发（标准2）。同时，它本身是一篇针对特定技术领域的综述论文（标准3）。

**📖 中文摘要**

这篇论文是一篇关于多项式码（特别是Reed-Solomon码及其相关码族）列表解码进展的综述性书籍章节。它涵盖了列表解码的基本概念、近年来在列表解码Reed-Solomon码及相关多项式码方面的重大进展，包括达到信息论容量、具有最优列表大小、使用快速近线性时间甚至亚线性时间算法等。虽然论文主要面向编码理论，但“列表解码”作为一种强大的纠错技术，在需要从含噪声或损坏数据中恢复信息的场景中有广泛应用。考虑到“质谱结构推理”任务本质上是从复杂的质谱信号（可能包含噪声和干扰）中推断分子结构，这可以类比为一个从“编码”数据（质谱）中“解码”出原始信息（分子结构）的过程。因此，这篇综述所总结的先进列表解码技术，在方法论层面可能为处理类似“质谱信号解码”的复杂推理问题提供理论工具和灵感（标准2）。同时，作为一篇综述，它也符合标准3。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Error-correcting codes are a method for representing data, so that one can recover the original information even if some parts of it were corrupted. The basic idea, which dates back to the revolutionary work of Shannon and Hamming about a century ago, is to encode the data into a redundant form, so that the original information can be decoded from the redundant encoding even in the presence of some noise or corruption. One prominent family of error-correcting codes are Reed-Solomon Codes which encode the data using evaluations of low-degree polynomials. Nearly six decades after they were introduced, Reed-Solomon Codes, as well as some related families of polynomial-based codes, continue to be widely studied, both from a theoretical perspective and from the point of view of applications. Besides their obvious use in communication, error-correcting codes such as Reed-Solomon Codes are also useful for various applications in theoretical computer science. These applications often require the ability to cope with many errors, much more than what is possible information-theoretically. List-decodable codes are a special class of error-correcting codes that enable correction from more errors than is traditionally possible by allowing a small list of candidate decodings. These codes have turned out to be extremely useful in various applications across theoretical computer science and coding theory. In recent years, there have been significant advances in list decoding of Reed-Solomon Codes and related families of polynomial-based codes. This includes efficient list decoding of such codes up to the information-theoretic capacity, with optimal list-size, and using fast nearly-linear time, and even sublinear-time, algorithms. In this book, we survey these developments.

</details>

---

### 28. [Benchmarking Motivational Interviewing Competence of Large Language Models](https://arxiv.org/abs/2603.03846)

**基本信息**

- 🔗 arXiv: [`2603.03846`](https://arxiv.org/abs/2603.03846)
- 👥 作者: Aishwariya Jha, Prakrithi Shivaprakash, Lekhansh Shukla 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03846.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大型语言模型在专业心理咨询任务中的能力进行系统性基准测试和评估，LLM是“化学大模型”主题的核心模型类型。

**📖 中文摘要**

这篇论文评估了大型语言模型在模拟动机性访谈中的能力。动机性访谈是一种用于促进行为改变的心理治疗技术，其保真度使用MITI框架衡量。论文旨在基准测试专有和开源LLM与人类治疗师相比的MI能力，使用了手工制作的模型转录本和真实世界临床转录本。研究评估了10个LLM，发现所有模型在MITI测量上都表现出良好能力，其中一些模型在复杂反思百分比等指标上甚至超过了人类专家。此外，在可区分性实验中，精神病学家识别LLM回答的准确率仅略高于随机水平。论文的核心是系统性地评估LLM在特定专业领域（心理咨询）的对话和推理能力，LLM是“化学大模型”主题的核心。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivational interviewing (MI) promotes behavioural change in substance use disorders. Its fidelity is measured using the Motivational Interviewing Treatment Integrity (MITI) framework. While large language models (LLMs) can potentially generate MI-consistent therapist responses, their competence using MITI is not well-researched, especially in real world clinical transcripts. We aim to benchmark MI competence of proprietary and open-source models compared to human therapists in real-world transcripts and assess distinguishability from human therapists. Methods: We shortlisted 3 proprietary and 7 open-source LLMs from LMArena, evaluated performance using MITI 4.2 framework on two datasets (96 handcrafted model transcripts, 34 real-world clinical transcripts). We generated parallel LLM-therapist utterances iteratively for each transcript while keeping client responses static, and ranked performance using a composite ranking system with MITI components and verbosity. We conducted a distinguishability experiment with two independent psychiatrists to identify human-vs-LLM responses. Results: All 10 tested LLMs had fair (MITI global scores >3.5) to good (MITI global scores >4) competence across MITI measures, and three best-performing models (gemma-3-27b-it, gemini-2.5-pro, grok-3) were tested on real-world transcripts. All showed good competence, with LLMs outperforming human-expert in Complex Reflection percentage (39% vs 96%) and Reflection-Question ratio (1.2 vs >2.8). In the distinguishability experiment, psychiatrists identified LLM responses with only 56% accuracy, with d-prime: 0.17 and 0.25 for gemini-2.5-pro and gemma-3-27b-it respectively. Conclusion: LLMs can achieve good MI proficiency in real-world clinical transcripts using MITI framework. These findings suggest that even open-source LLMs are viable candidates for expanding MI counselling sessions in low-resource settings.

</details>

---

### 29. [Assessing the Effectiveness of LLMs in Delivering Cognitive Behavioral Therapy](https://arxiv.org/abs/2603.03862)

**基本信息**

- 🔗 arXiv: [`2603.03862`](https://arxiv.org/abs/2603.03862)
- 👥 作者: Navdeep Singh Bedi, Ana-Maria Bucur, Noriko Kando 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03862.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大型语言模型在模拟专业心理治疗对话方面的能力进行评估，LLM是“化学大模型”主题的核心模型类型。

**📖 中文摘要**

这篇论文评估了大型语言模型模拟专业认知行为治疗师的能力。研究使用匿名的、经转录的治疗师与客户角色扮演会话，比较了两种方法：纯生成方法和使用CBT指南的检索增强生成方法。评估了专有和开源模型在语言质量、语义连贯性和治疗保真度方面的表现。论文的核心是评估LLM在心理健康这一高敏感、专业性强的领域提供服务的潜力和局限性。研究直接以LLM为对象，评估其专业领域对话和推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As mental health issues continue to rise globally, there is an increasing demand for accessible and scalable therapeutic solutions. Many individuals currently seek support from Large Language Models (LLMs), even though these models have not been validated for use in counseling services. In this paper, we evaluate LLMs' ability to emulate professional therapists practicing Cognitive Behavioral Therapy (CBT). Using anonymized, transcribed role-play sessions between licensed therapists and clients, we compare two approaches: (1) a generation-only method and (2) a Retrieval-Augmented Generation (RAG) approach using CBT guidelines. We evaluate both proprietary and open-source models for linguistic quality, semantic coherence, and therapeutic fidelity using standard natural language generation (NLG) metrics, natural language inference (NLI), and automated scoring for skills assessment. Our results indicate that while LLMs can generate CBT-like dialogues, they are limited in their ability to convey empathy and maintain consistency.

</details>

---

### 30. [Believe Your Model: Distribution-Guided Confidence Calibration](https://arxiv.org/abs/2603.03872)

**基本信息**

- 🔗 arXiv: [`2603.03872`](https://arxiv.org/abs/2603.03872)
- 👥 作者: Xizhong Yang, Haotian Zhang, Huiming Wang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕提升大型语言模型的推理可靠性、置信度校准和答案选择策略，LLM是“化学大模型”主题的核心。

**📖 中文摘要**

这篇论文提出了DistriVoting方法，用于提升大型推理模型在测试时缩放技术中的答案选择可靠性。测试时缩放通过生成多个候选答案并选择最可靠的答案来提高预测准确性。论文指出，模型内部信号（如置信度分数）的分布信息未被充分利用。因此，DistriVoting将分布先验作为另一个信号与置信度一起用于投票。具体方法包括使用高斯混合模型分解混合置信度分布，并基于正负样本应用拒绝过滤器。此外，还提出了SelfStepConf来动态调整推理过程以增加两个分布之间的分离度。研究内容直接围绕提升大型语言模型（作为“大模型”的代表）的推理可靠性和校准，并在多个模型和基准上进行了实验验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Reasoning Models have demonstrated remarkable performance with the advancement of test-time scaling techniques, which enhances prediction accuracy by generating multiple candidate responses and selecting the most reliable answer. While prior work has analyzed that internal model signals like confidence scores can partly indicate response correctness and exhibit a distributional correlation with accuracy, such distributional information has not been fully utilized to guide answer selection. Motivated by this, we propose DistriVoting, which incorporates distributional priors as another signal alongside confidence during voting. Specifically, our method (1) first decomposes the mixed confidence distribution into positive and negative components using Gaussian Mixture Models, (2) then applies a reject filter based on positive/negative samples from them to mitigate overlap between the two distributions. Besides, to further alleviate the overlap from the perspective of distribution itself, we propose SelfStepConf, which uses step-level confidence to dynamically adjust inference process, increasing the separation between the two distributions to improve the reliability of confidences in voting. Experiments across 16 models and 5 benchmarks demonstrate that our method significantly outperforms state-of-the-art approaches.

</details>

---

### 31. [On the Suitability of LLM-Driven Agents for Dark Pattern Audits](https://arxiv.org/abs/2603.03881)

**基本信息**

- 🔗 arXiv: [`2603.03881`](https://arxiv.org/abs/2603.03881)
- 👥 作者: Chen Sun, Yash Vekaria, Rishab Nithyanand
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03881.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估LLM驱动的智能体在真实网络环境中执行复杂任务（黑暗模式审计）的能力，LLM是“化学大模型”主题的核心。

**📖 中文摘要**

这篇论文研究了LLM驱动的智能体在识别网页界面中黑暗模式（操纵性设计）方面的能力。研究设计并部署了一个能够端到端遍历权利请求工作流、进行结构化证据收集和对潜在黑暗模式进行分类的LLM驱动审计智能体。研究在456个数据经纪人网站上进行了评估，重点关注智能体定位和完成请求流程的一致性、其黑暗模式分类的可靠性和可重复性，以及其失败或产生错误判断的条件。论文的核心是评估LLM驱动的智能体在复杂、真实的交互式网络环境中执行特定审计任务的能力和局限性，直接以LLM驱动的智能体为研究对象。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As LLM-driven agents begin to autonomously navigate the web, their ability to interpret and respond to manipulative interface design becomes critical. A fundamental question that emerges is: can such agents reliably recognize patterns of friction, misdirection, and coercion in interface design (i.e., dark patterns)? We study this question in a setting where the workflows are consequential: website portals associated with the submission of CCPA-related data rights requests. These portals operationalize statutory rights, but they are implemented as interactive interfaces whose design can be structured to facilitate, burden, or subtly discourage the exercise of those rights. We design and deploy an LLM-driven auditing agent capable of end-to-end traversal of rights-request workflows, structured evidence gathering, and classification of potential dark patterns. Across a set of 456 data broker websites, we evaluate: (1) the ability of the agent to consistently locate and complete request flows, (2) the reliability and reproducibility of its dark pattern classifications, and (3) the conditions under which it fails or produces poor judgments. Our findings characterize both the feasibility and the limitations of using LLM-driven agents for scalable dark pattern auditing.

</details>

---

### 32. [IROSA: Interactive Robot Skill Adaptation using Natural Language](https://arxiv.org/abs/2603.03897)

**基本信息**

- 🔗 arXiv: [`2603.03897`](https://arxiv.org/abs/2603.03897)
- 👥 作者: Markus Knauer, Samuel Bustamante, Thomas Eiband 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03897.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用预训练的大型语言模型通过自然语言交互来适应机器人技能，LLM是“化学大模型”主题的核心模型类型。

**📖 中文摘要**

这篇论文提出了IROSA框架，一个基于工具架构的、支持开放词汇技能适应的机器人框架。该框架利用预训练的大型语言模型来选择和参数化特定工具，以适应机器人技能，而无需对LLM进行微调或直接与机器人交互。论文明确指出，基础模型在各个领域展示了令人印象深刻的能力，而模仿学习为从有限数据中进行机器人技能适应提供了原则性方法。结合这两种方法对机器人学具有重要前景。研究内容直接涉及利用预训练LLM（作为基础模型的代表）进行机器人技能的自然语言交互式适应，LLM是“化学大模型”主题的核心。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models have demonstrated impressive capabilities across diverse domains, while imitation learning provides principled methods for robot skill adaptation from limited data. Combining these approaches holds significant promise for direct application to robotics, yet this combination has received limited attention, particularly for industrial deployment. We present a novel framework that enables open-vocabulary skill adaptation through a tool-based architecture, maintaining a protective abstraction layer between the language model and robot hardware. Our approach leverages pre-trained LLMs to select and parameterize specific tools for adapting robot skills without requiring fine-tuning or direct model-to-robot interaction. We demonstrate the framework on a 7-DoF torque-controlled robot performing an industrial bearing ring insertion task, showing successful skill adaptation through natural language commands for speed adjustment, trajectory correction, and obstacle avoidance while maintaining safety, transparency, and interpretability.

</details>

---

### 33. [Lang2Str: Two-Stage Crystal Structure Generation with LLMs and Continuous Flow Models](https://arxiv.org/abs/2603.03946)

**基本信息**

- 🔗 arXiv: [`2603.03946`](https://arxiv.org/abs/2603.03946)
- 👥 作者: Cong Liu, Chengyue Gong, Zhenyu Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03946.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用大语言模型（LLM）生成材料描述，并进一步生成晶体结构，这直接涉及'化学大模型'（用于材料设计）和'质谱结构推理'（广义的结构解析与生成）主题。

**📖 中文摘要**

本文提出了一种名为Lang2Str的两阶段晶体结构生成框架，结合了大语言模型（LLM）和基于流的模型。该框架将生成过程视为条件生成任务：首先，LLM根据其广泛的知识背景生成材料晶胞几何布局和属性的高级描述，确保结构设计的合理性；然后，一个条件流模型将这些文本描述解码为精确的连续坐标和晶胞参数。这种方法将LLM的结构化推理能力与流模型的分布建模能力相结合，用于从头开始的材料生成和晶体结构预测任务。实验结果表明，该方法在几何和能量水平上与真实结构更接近，性能优于最先进的模型。该框架的灵活性和模块化特性使得能够对生成过程进行细粒度控制，从而实现更高效和可定制的材料设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models hold great promise for accelerating material discovery but are often limited by their inflexible single-stage generative process in designing valid and diverse materials. To address this, we propose a two-stage generative framework, Lang2Str, that combines the strengths of large language models (LLMs) and flow-based models for flexible and precise material generation. Our method frames the generative process as a conditional generative task, where an LLM provides high-level conditions by generating descriptions of material unit cells' geometric layouts and properties. These descriptions, informed by the LLM's extensive background knowledge, ensure reasonable structure designs. A conditioned flow model then decodes these textual conditions into precise continuous coordinates and unit cell parameters. This staged approach combines the structured reasoning of LLMs and the distribution modeling capabilities of flow models. Experimental results show that our method achieves competitive performance on \textit{ab initio} material generation and crystal structure prediction tasks, with generated structures exhibiting closer alignment to ground truth in both geometry and energy levels, surpassing state-of-the-art models. The flexibility and modularity of our framework further enable fine-grained control over the generation process, potentially leading to more efficient and customizable material design.

</details>

---

### 34. [BLOCK: An Open-Source Bi-Stage MLLM Character-to-Skin Pipeline for Minecraft](https://arxiv.org/abs/2603.03964)

**基本信息**

- 🔗 arXiv: [`2603.03964`](https://arxiv.org/abs/2603.03964)
- 👥 作者: Hengquan Guo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03964.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大模型（MLLM）进行从文本/概念到具体化学结构（在本例中是《我的世界》皮肤，可视为一种像素化的化学/材料结构表示）的生成。这属于'化学大模型'在结构生成方向上的一个具体应用实例。

**📖 中文摘要**

本文提出了BLOCK，一个开源的、两阶段的从角色概念到《我的世界》（Minecraft）皮肤生成的流程。该流程将问题分解为两个阶段：第一阶段由一个大模型（MLLM）驱动，通过精心设计的提示和参考模板生成一致的双面板（正面/背面）斜视图《我的世界》风格预览；第二阶段基于微调的FLUX.2模型，将预览图解码为皮肤图集图像。此外，论文还提出了EvolveLoRA，一种渐进式的LoRA课程学习方法。BLOCK框架旨在支持可重现的角色到皮肤生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present \textbf{BLOCK}, an open-source bi-stage character-to-skin pipeline that generates pixel-perfect Minecraft skins from arbitrary character concepts. BLOCK decomposes the problem into (i) a \textbf{3D preview synthesis stage} driven by a large multimodal model (MLLM) with a carefully designed prompt-and-reference template, producing a consistent dual-panel (front/back) oblique-view Minecraft-style preview; and (ii) a \textbf{skin decoding stage} based on a fine-tuned FLUX.2 model that translates the preview into a skin atlas image. We further propose \textbf{EvolveLoRA}, a progressive LoRA curriculum (text-to-image $\rightarrow$ image-to-image $\rightarrow$ preview-to-skin) that initializes each phase from the previous adapter to improve stability and efficiency. BLOCK is released with all prompt templates and fine-tuned weights to support reproducible character-to-skin generation.

</details>

---

### 35. [Inference-Time Toxicity Mitigation in Protein Language Models](https://arxiv.org/abs/2603.04045)

**基本信息**

- 🔗 arXiv: [`2603.04045`](https://arxiv.org/abs/2603.04045)
- 👥 作者: Manuel Fernández Burda, Santiago Aranguri, Iván Arcuschin Moreno 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04045.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕蛋白质语言模型（PLMs），这是一种专门用于生物分子（蛋白质）的化学大模型。研究重点在于控制这类大模型生成输出的安全性，直接关联'化学大模型'主题。

**📖 中文摘要**

本文研究了蛋白质语言模型（PLMs）在生成蛋白质时的安全性问题，特别是其对特定分类群进行领域适应后可能引发生成有毒蛋白质的风险。为了缓解这一问题，作者将Logit Diff Amplification（LDA）方法适配为PLMs的推理时控制机制。LDA通过放大基线模型和经过毒性微调的模型之间的logit差异来修改token概率，无需重新训练。在四个分类群的测试中，LDA能持续降低预测的毒性率，同时保持生物合理性和结构可行性。这项工作展示了如何为蛋白质生成器提供实用的安全控制机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein language models (PLMs) are becoming practical tools for de novo protein design, yet their dual-use potential raises safety concerns. We show that domain adaptation to specific taxonomic groups can elicit toxic protein generation, even when toxicity is not the training objective. To address this, we adapt Logit Diff Amplification (LDA) as an inference-time control mechanism for PLMs. LDA modifies token probabilities by amplifying the logit difference between a baseline model and a toxicity-finetuned model, requiring no retraining. Across four taxonomic groups, LDA consistently reduces predicted toxicity rate (measured via ToxDL2) below the taxon-finetuned baseline while preserving biological plausibility. We evaluate quality using Fréchet ESM Distance and predicted foldability (pLDDT), finding that LDA maintains distributional similarity to natural proteins and structural viability (unlike activation-based steering methods that tend to degrade sequence properties). Our results demonstrate that LDA provides a practical safety knob for protein generators that mitigates elicited toxicity while retaining generative quality.

</details>

---

### 36. [Characterizing Machine Learning Force Fields as Emerging Molecular Dynamics Workloads on Graphics Processing Units](https://arxiv.org/abs/2603.04092)

**基本信息**

- 🔗 arXiv: [`2603.04092`](https://arxiv.org/abs/2603.04092)
- 👥 作者: Udari De Alwis, Benjamin E. Mayer, Tom J. Ashby 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04092.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习力场（MLFFs），这是化学信息学和计算化学中用于分子模拟的一类重要模型，属于'化学大模型'的范畴。论文专注于分析这类模型在硬件上的计算性能。

**📖 中文摘要**

本文从计算机体系结构的角度，研究了机器学习力场（MLFFs）作为新兴分子动力学（MD）工作负载在图形处理器（GPU）上的性能特征。MLFFs通过从电子结构数据中学习原子间相互作用，以接近量子化学的精度进行分子模拟，但它们在描述符评估和神经网络推理方面引入了显著的计算开销。作者使用聚丙氨酸链作为基准分子系统，分析了MLFF模拟在GPU上的关键性能瓶颈，如不规则内存访问、数据重用率低和内核执行效率低下。这项工作旨在为药物发现等领域的MLFF-based MD模拟的硬件优化提供见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular dynamics (MD) simulates the time evolution of atomic systems governed by interatomic forces, and the fidelity of these simulations depends critically on the underlying force model. Classical force fields (CFFs) rely on fixed functional forms fitted to experimental or theoretical data, offering computational efficiency and broad applicability but limited accuracy in chemically diverse or reactive environments. In contrast, machine learning force fields (MLFFs) deliver near quantum chemical accuracy at molecular-mechanics cost by learning interatomic interactions directly from high level electronic structure data. While MLFFs offer improved accuracy at a fraction of the cost of quantum methods, they introduce significant computational overhead, particularly in descriptor evaluation and neural network inference. These operations pose challenges for parallel hardware due to irregular memory access, minimum data reuse and inefficient kernel execution. This work investigates the hardware performance of such models using poly alanine chains, a novel benchmark molecule system(s) with controllable input size, which used as performance evaluation test cases highlighting the computational bottlenecks of the graphical processor units when scaling out MLFF simulations. The analysis identifies key bottlenecks in descriptor and force computation, memory handling, highlighting the opportunities for improvements in the emerging area of MLFF based MD in drug discovery, that has received limited attention from a computer architecture perspective.

</details>

---

### 37. [Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection](https://arxiv.org/abs/2603.04337)

**基本信息**

- 🔗 arXiv: [`2603.04337`](https://arxiv.org/abs/2603.04337)
- 👥 作者: Dacheng Qi, Chenyu Wang, Jingwei Xu 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04337.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用大语言模型（LLM）进行几何结构（CAD模型）的生成和推理。虽然应用领域是CAD，但其方法论（LLM结合几何指针进行结构化生成）与“化学大模型”用于分子结构生成或“质谱结构推理”中从数据推断化学结构在核心思想上高度相关，都属于利用AI大模型进行复杂结构建模和推理的范畴。

**📖 中文摘要**

本文提出Pointer-CAD，一个基于大语言模型（LLM）的计算机辅助设计（CAD）生成框架。它通过引入基于指针的命令序列表示，将边界表示（B-Rep）模型的几何信息显式地整合到序列建模中。该框架将CAD模型生成分解为多个步骤，每一步的生成都以前一步生成的B-rep和文本描述为条件。当操作需要选择特定几何实体（如面或边）时，LLM会预测一个指针，从可用集合中选择特征最一致的候选。这种方法解决了传统基于命令序列的方法无法支持复杂编辑操作（如倒角或圆角）以及因连续变量离散化导致拓扑错误的问题。Pointer-CAD显著降低了分割错误，并大幅减轻了量化误差引入的拓扑不准确性。这项工作展示了LLM在复杂几何结构生成中的应用，属于“化学大模型”在分子/材料结构生成领域的类比和拓展，其核心思想（使用LLM结合几何信息生成结构）与化学信息学中利用大模型进行分子设计或质谱结构推理有很强的概念相关性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error.

</details>

---

### 38. [LLM-supported 3D Modeling Tool for Radio Radiance Field Reconstruction](https://arxiv.org/abs/2603.04368)

**基本信息**

- 🔗 arXiv: [`2603.04368`](https://arxiv.org/abs/2603.04368)
- 👥 作者: Chengling Xu, Huiwen Zhang, Haijian Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04368.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个基于（微调）语言模型和生成式AI的3D场景创建工具链。这种方法论与“化学大模型”领域利用语言模型进行分子表示、生成或操作3D分子结构的研究在技术路径上高度一致，都是将大模型应用于特定科学领域的结构化数据生成问题。

**📖 中文摘要**

本文介绍了一个支持本地部署的工具，用于简化无线通信中无线电辐射场（RRF）重建所需的3D环境创建。该系统结合了微调的语言模型（T5-mini用于解析用户命令）、生成式3D建模框架（LLaMA-Mesh, Shap-E）和Blender集成，实现了基于聊天的直观场景设计。该工具旨在降低RRF重建（一种用于无线信道建模的方法）中3D建模的复杂性。虽然应用领域是无线通信，但其核心技术栈——使用微调的语言模型和生成式AI框架来创建和操作3D几何结构——与“化学大模型”中利用语言模型处理分子结构、或辅助进行分子/材料3D建模的概念高度相似。论文展示了如何将LLM与3D生成工具链结合，以解决特定科学领域（此处为无线研究）的数据准备难题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate channel estimation is essential for massive multiple-input multiple-output (MIMO) technologies in next-generation wireless communications. Recently, the radio radiance field (RRF) has emerged as a promising approach for wireless channel modeling, offering a comprehensive spatial representation of channels based on environmental geometry. State-of-the-art RRF reconstruction methods, such as RF-3DGS, can render channel parameters, including gain, angle of arrival, angle of departure, and delay, within milliseconds. However, creating the required 3D environment typically demands precise measurements and advanced computer vision techniques, limiting accessibility. This paper introduces a locally deployable tool that simplifies 3D environment creation for RRF reconstruction. The system combines finetuned language models, generative 3D modeling frameworks, and Blender integration to enable intuitive, chat-based scene design. Specifically, T5-mini is finetuned for parsing user commands, while all-MiniLM-L6-v2 supports semantic retrieval from a local object library. For model generation, LLaMA-Mesh provides fast mesh creation, and Shap-E delivers high-quality outputs. A custom Blender export plugin ensures compatibility with the RF-3DGS pipeline. We demonstrate the tool by constructing 3D models of the NIST lobby and the UW-Madison wireless lab, followed by corresponding RRF reconstructions. This approach significantly reduces modeling complexity, enhancing the usability of RRF for wireless research and spectrum planning.

</details>

---

### 39. [Physics-constrained symbolic regression for discovering closed-form equations of multimodal water retention curves from experimental data](https://arxiv.org/abs/2603.03346)

**基本信息**

- 🔗 arXiv: [`2603.03346`](https://arxiv.org/abs/2603.03346)
- 👥 作者: Yejin Kim, Hyoung Suk Suh
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03346.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个物理约束的符号回归框架，用于从实验数据中自动发现封闭形式的数学方程。这种方法论与“化学大模型”或更广泛的科学机器学习中，利用可解释AI从化学/质谱数据中推导物理化学模型或关系式的研究主题直接相关。

**📖 中文摘要**

本文提出了一个物理约束的机器学习框架，用于元建模，能够直接从实验数据中自动发现多峰水 retention曲线的封闭形式数学表达式。数学表达式表示为二叉树，并通过遗传编程进行演化，同时将物理约束嵌入损失函数中，以引导符号回归器找到物理一致且数学稳健的解。结果表明，该框架能够发现有效表示具有不同孔隙结构的多孔材料水 retention特性的封闭形式方程。这项工作展示了符号回归（一种可解释的机器学习方法）在从实验数据中发现物理定律方面的应用。虽然应用领域是土壤力学/多孔介质，但其核心方法——使用遗传编程进行符号回归，并结合领域知识（物理约束）来从数据中发现可解释的数学模型——与“化学大模型”中利用机器学习从化学数据（如光谱、质谱）中发现物理化学规律或解析表达式有很强的概念相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modeling the unsaturated behavior of porous materials with multimodal pore size distributions presents significant challenges, as standard hydraulic models often fail to capture their complex, multi-scale characteristics. A common workaround involves superposing unimodal retention functions, each tailored to a specific pore size range; however, this approach requires separate parameter identification for each mode, which limits interpretability and generalizability, especially in data-sparse scenarios. In this work, we introduce a fundamentally different approach: a physics-constrained machine learning framework designed for meta-modeling, enabling the automatic discovery of closed-form mathematical expressions for multimodal water retention curves directly from experimental data. Mathematical expressions are represented as binary trees and evolved via genetic programming, while physical constraints are embedded into the loss function to guide the symbolic regressor toward solutions that are physically consistent and mathematically robust. Our results demonstrate that the proposed framework can discover closed-form equations that effectively represent the water retention characteristics of porous materials with varying pore structures. To support third-party validation, application, and extension, we make the full implementation publicly available in an open-source repository.

</details>

---

### 40. [TritonDFT: Automating DFT with a Multi-Agent Framework](https://arxiv.org/abs/2603.03372)

**基本信息**

- 🔗 arXiv: [`2603.03372`](https://arxiv.org/abs/2603.03372)
- 👥 作者: Zhengding Hu, Kuntal Talit, Zhen Wang 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03372.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个多智能体框架，以自动化材料科学中核心的计算方法——密度泛函理论（DFT）的工作流。这直接属于“化学大模型”或“科学AI”在计算化学和材料发现中的具体应用，旨在利用AI智能体技术来管理和优化复杂的科学计算流程。

**📖 中文摘要**

本文提出了TritonDFT，一个用于自动化密度泛函理论（DFT）计算的多智能体框架。DFT是材料科学和计算化学的基石，但其实际执行涉及协调复杂、多步骤的工作流。TritonDFT通过专家策划、可扩展的工作流设计、帕累托感知的参数推断和多源知识增强，实现了高效、准确的DFT执行。此外，作者还引入了DFTBench，一个用于评估智能体在多维度能力（包括科学专业知识、权衡优化、高性能计算知识和成本效率）的基准。TritonDFT为现实使用提供了开放的用户接口。这项工作将大语言模型/智能体技术应用于自动化第一性原理计算工作流，属于“化学大模型”在驱动计算化学模拟和实验方面的前沿应用，旨在提升材料研究的效率和可及性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Density Functional Theory (DFT) is a cornerstone of materials science, yet executing DFT in practice requires coordinating a complex, multi-step workflow. Existing tools and LLM-based solutions automate parts of the steps, but lack support for full workflow automation, diverse task adaptation, and accuracy-cost trade-off optimization in DFT configuration. To this end, we present TritonDFT, a multi-agent framework that enables efficient and accurate DFT execution through an expert-curated, extensible workflow design, Pareto-aware parameter inference, and multi-source knowledge augmentation. We further introduce DFTBench, a benchmark for evaluating the agent's multi-dimensional capabilities, spanning science expertise, trade0off optimization, HPC knowledge, and cost efficiency. TritonDFT provides an open user interface for real-world usage. Our website is at this https URL . Our source code and benchmark suite are available at this https URL .

</details>

---

### 41. [SELDON: Supernova Explosions Learned by Deep ODE Networks](https://arxiv.org/abs/2603.04392)

**基本信息**

- 🔗 arXiv: [`2603.04392`](https://arxiv.org/abs/2603.04392)
- 👥 作者: Jiezhong Wu, Jack O'Brien, Jennifer Li 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04392.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于复杂、稀疏、不规则时间序列的连续时间生成模型（SELDON），其核心方法（神经ODE、可解释的参数化解码）与“质谱结构推理”中从高维、复杂的质谱数据中学习并推断化学结构信息所面临的技术挑战（处理连续或准连续信号、学习潜在动力学、生成可解释特征）在方法论上高度相关。

**📖 中文摘要**

本文提出了SELDON，一种用于稀疏、不规则时间采样（有间隙）的天体物理光变曲线面板的连续时间变分自编码器。SELDON结合了掩码GRU-ODE编码器、潜在神经ODE传播器和可解释的高斯基解码器。编码器学习总结不平衡和相关数据的面板，即使只观察到少量数据点。神经ODE然后在连续时间内对这个隐藏状态进行积分，外推到未来未观测到的时期。这个外推的时间序列进一步通过深度集合编码到一个潜在分布，该分布被解码为高斯基函数的加权和，其参数具有物理意义（例如，上升时间、衰减率、峰值通量）。虽然应用领域是天体物理学，但SELDON的核心技术创新在于处理稀疏、不规则、多变量时间序列的连续时间生成模型。其方法论——特别是使用神经ODE进行连续时间动力学建模和可解释的参数化解码——与“质谱结构推理”中处理复杂、高维、有时序特性的质谱数据，并从中推断出结构信息（如分子特征）有潜在的相关性。两者都涉及从非均匀采样或高维信号中学习并生成具有物理/化学意义的参数化表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The discovery rate of optical transients will explode to 10 million public alerts per night once the Vera C. Rubin Observatory's Legacy Survey of Space and Time comes online, overwhelming the traditional physics-based inference pipelines. A continuous-time forecasting AI model is of interest because it can deliver millisecond-scale inference for thousands of objects per day, whereas legacy MCMC codes need hours per object. In this paper, we propose SELDON, a new continuous-time variational autoencoder for panels of sparse and irregularly time-sampled (gappy) astrophysical light curves that are nonstationary, heteroscedastic, and inherently dependent. SELDON combines a masked GRU-ODE encoder with a latent neural ODE propagator and an interpretable Gaussian-basis decoder. The encoder learns to summarize panels of imbalanced and correlated data even when only a handful of points are observed. The neural ODE then integrates this hidden state forward in continuous time, extrapolating to future unseen epochs. This extrapolated time series is further encoded by deep sets to a latent distribution that is decoded to a weighted sum of Gaussian basis functions, the parameters of which are physically meaningful. Such parameters (e.g., rise time, decay rate, peak flux) directly drive downstream prioritization of spectroscopic follow-up for astrophysical surveys. Beyond astronomy, the architecture of SELDON offers a generic recipe for interpretable and continuous-time sequence modeling in any time domain where data are multivariate, sparse, heteroscedastic, and irregularly spaced.

</details>

---

### 42. [Crystal-GFN: sampling crystals with desirable properties and constraints](https://arxiv.org/abs/2310.04925)

**基本信息**

- 🔗 arXiv: [`2310.04925`](https://arxiv.org/abs/2310.04925)
- 👥 作者: Mila AI4Science, Alex Hernandez-Garcia, Alexandre Duval 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2310.04925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用生成式AI模型（GFlowNet）进行晶体结构的设计与生成，这是“化学大模型”在材料发现和计算化学中的核心应用场景。

**📖 中文摘要**

本文提出了Crystal-GFN，一种用于生成具有理想属性和约束的晶体结构的生成模型。该模型作为一个多环境、连续-离散的GFlowNet，顺序采样晶体材料的空间群、成分和晶格参数等结构属性。这种受领域启发的方法能够灵活地融入物理化学和几何硬约束。作者展示了Crystal-GFN能够高效地发现多样且有效的晶体，这些晶体具有低预测形成能、接近目标值的带隙和高密度等特性。Crystal-GFN直接针对材料发现中的晶体结构生成问题，是“化学大模型”在材料科学领域的典型应用。它利用生成式流网络（GFlowNet）这一先进的生成模型来探索巨大的化学空间，旨在加速新材料的发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The discovery of novel solid-state materials, such as electrocatalysts, super-ionic conductors, or photovoltaic materials, plays a critical role in addressing various global challenges. It has, for instance, the potential to significantly improve the efficiency of renewable energy production and storage, thereby making substantial contributions to climate crisis mitigation strategies. In this paper, we introduce Crystal-GFN, a generative model of crystal structures possessing desirable properties and constraints. Operating as a multi-environment, continuous-discrete GFlowNet, it sequentially samples structural attributes of crystalline materials, namely space group, composition and lattice parameters. This domain-inspired approach enables the flexible incorporation of physicochemical and geometric hard constraints. We demonstrate the capabilities of Crystal-GFN to efficiently discover diverse and valid crystals with various properties: low predicted formation energy (median -3.2 eV/atom), band gap close to a target value and high density. Overall, Crystal-GFN is a crystal generation method that addresses several existing challenges in the literature and opens promising paths for accelerating materials discovery with machine learning.

</details>

---

### 43. [Unsupervised Representation Learning - an Invariant Risk Minimization Perspective](https://arxiv.org/abs/2505.12506)

**基本信息**

- 🔗 arXiv: [`2505.12506`](https://arxiv.org/abs/2505.12506)
- 👥 作者: Yotam Norman, Ron Meir
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12506.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是无监督不变表示学习，这是机器学习，特别是构建能够稳健处理分布偏移的领域大模型（如化学大模型）中的一个基础且重要的主题。其方法论对于从化学或质谱数据中学习有意义的、不变的潜在特征具有直接相关性。

**📖 中文摘要**

本文提出了一个用于无监督不变风险最小化（IRM）的新框架，将不变性的概念扩展到没有标签可用的设置。传统的IRM方法依赖带标签的数据来学习跨环境分布变化下稳健的表示。相比之下，本文的方法通过特征分布对齐重新定义了不变性，从而能够从无标签数据中学习稳健的表示。作者在该框架内引入了两种方法：主不变成分分析（PICA），一种在高斯假设下提取不变方向的线性方法；以及变分不变自编码器（VIAE），一种将环境不变和环境依赖的潜在因子分离的深度生成模型。该方法基于一个新颖的“无监督”结构因果模型，并支持环境条件样本生成和干预。在合成数据集、MNIST修改版本和CelebA上的实证评估证明了该方法在捕获不变结构、保留相关信息以及跨环境泛化方面的有效性，而无需访问标签。这项工作涉及无监督表示学习和因果发现，这些技术对于从无标签或弱标签的化学或质谱数据中学习稳健的、可泛化的表示至关重要，是构建相关大模型的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a novel unsupervised framework for \emph{Invariant Risk Minimization} (IRM), extending the concept of invariance to settings where labels are unavailable. Traditional IRM methods rely on labeled data to learn representations that are robust to distributional shifts across environments. In contrast, our approach redefines invariance through feature distribution alignment, enabling robust representation learning from unlabeled data. We introduce two methods within this framework: Principal Invariant Component Analysis (PICA), a linear method that extracts invariant directions under Gaussian assumptions, and Variational Invariant Autoencoder (VIAE), a deep generative model that separates environment-invariant and environment-dependent latent factors. Our approach is based on a novel ``unsupervised'' structural causal model and supports environment-conditioned sample-generation and intervention. Empirical evaluations on synthetic dataset, modified versions of MNIST, and CelebA demonstrate the effectiveness of our methods in capturing invariant structure, preserving relevant information, and generalizing across environments without access to labels.

</details>

---

### 44. [TSPulse: Tiny Pre-Trained Models with Disentangled Representations for Rapid Time-Series Analysis](https://arxiv.org/abs/2505.13033)

**基本信息**

- 🔗 arXiv: [`2505.13033`](https://arxiv.org/abs/2505.13033)
- 👥 作者: Vijay Ekambaram, Subodh Kumar, Arindam Jati 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.13033.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心是设计和预训练一个用于时间序列分析的轻量级基础模型家族（TSPulse），这属于构建领域专用大模型/基础模型的研究。同时，论文发布了模型和源代码，为相关领域（虽然主要是时间序列，但其方法论可借鉴）提供了可用的模型工具。

**📖 中文摘要**

本文提出了TSPulse，一个具有解耦特性的超轻量级预训练模型家族（100万参数），专为各种时间序列诊断任务设计。TSPulse引入了一种新颖的预训练框架，通过跨空间和抽象层次的显式解耦来增强掩码重建，学习三种互补的嵌入视图（时域、频域和语义），以有效实现零样本迁移。此外，作者还引入了各种轻量级的事后融合器，根据任务类型有选择地关注和融合这些解耦的视图，实现简单而有效的任务 specialization。为了进一步提高鲁棒性并减轻现有方法中普遍存在的掩码诱导偏差，作者提出了一种简单而有效的混合掩码策略，以增强预训练期间的缺失多样性。尽管尺寸紧凑，TSPulse在四个时间序列诊断任务上实现了强大且一致的性能提升。TSPulse提供了最先进的零样本性能、高效的微调，并支持无GPU部署。这项工作展示了如何为特定领域（如时间序列分析）设计和预训练高效、可迁移的小型基础模型。其解耦表示和高效预训练的思路对于在化学信息学或质谱分析中构建专用、高效的基础模型具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Time-series tasks often benefit from signals expressed across multiple representation spaces (e.g., time vs. frequency) and at varying abstraction levels (e.g., local patterns vs. global semantics). However, existing pre-trained time-series models entangle these heterogeneous signals into a single large embedding, limiting transferability and direct zero-shot usability. To address this, we propose TSPulse, family of ultra-light pre-trained models (1M parameters) with disentanglement properties, specialized for various time-series diagnostic tasks. TSPulse introduces a novel pre-training framework that augments masked reconstruction with explicit disentanglement across spaces and abstractions, learning three complementary embedding views (temporal, spectral, and semantic) to effectively enable zero-shot transfer. In-addition, we introduce various lightweight post-hoc fusers that selectively attend and fuse these disentangled views based on task type, enabling simple but effective task specializations. To further improve robustness and mitigate mask-induced bias prevalent in existing approaches, we propose a simple yet effective hybrid masking strategy that enhances missing diversity during pre-training. Despite its compact size, TSPulse achieves strong and consistent gains across four TS diagnostic tasks: +20% on the TSB-AD anomaly detection leaderboard, +25% on similarity search, +50% on imputation, and +5-16% on multivariate classification, outperforming models that are 10-100X larger on over 75 datasets. TSPulse delivers state-of-the-art zero-shot performance, efficient fine-tuning, and supports GPU-free deployment. Models and source code are publicly available at this https URL .

</details>

---

### 45. [On the Limits of Sparse Autoencoders: A Theoretical Framework and Reweighted Remedy](https://arxiv.org/abs/2506.15963)

**基本信息**

- 🔗 arXiv: [`2506.15963`](https://arxiv.org/abs/2506.15963)
- 👥 作者: Jingyi Cui, Qi Zhang, Yifei Wang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.15963.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是稀疏自编码器（SAE）的理论分析和改进，这是一种用于理解和解释深度学习模型（包括潜在的大模型）内部表示的重要工具。虽然论文背景是通用AI，但其关于特征解耦和可解释性的方法论与构建可解释的化学大模型或质谱分析模型的核心挑战直接相关。

**📖 中文摘要**

稀疏自编码器（SAE）已成为解释大语言模型所学特征的有力工具，旨在将复杂的叠加多义特征恢复为可解释的单义特征。尽管应用广泛，但SAE在何种条件下能够从叠加的多义特征中完全恢复出真实的单义特征尚不清楚。本文首次为SAE提供了理论分析，并给出了闭式解，揭示了除非真实特征极其稀疏，否则SAE通常无法完全恢复真实的单义特征。为了在一般情况下改进SAE的特征恢复能力，作者提出了一种重加权策略，旨在增强对真实单义特征的重建，而非观察到的多义特征。他们进一步为所提出的加权SAE（WSAE）建立了理论上的权重选择原则。在多个设置下的实验验证了理论发现，并表明WSAE显著提高了特征的单义性和可解释性。这项工作通过理论分析和算法改进，深化了对表示学习工具（如SAE）的理解，这对于构建和理解化学或质谱领域的可解释大模型具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse autoencoders (SAEs) have recently emerged as a powerful tool for interpreting the features learned by large language models (LLMs). By reconstructing features with sparsely activated networks, SAEs aim to recover complex superposed polysemantic features into interpretable monosemantic ones. Despite their wide applications, it remains unclear under what conditions SAEs can fully recover the ground truth monosemantic features from the superposed polysemantic ones. In this paper, we provide the first theoretical analysis with a closed-form solution for SAEs, revealing that they generally fail to fully recover the ground truth monosemantic features unless the ground truth features are extremely sparse. To improve the feature recovery of SAEs in general cases, we propose a reweighting strategy targeting at enhancing the reconstruction of the ground truth monosemantic features instead of the observed polysemantic ones. We further establish a theoretical weight selection principle for our proposed weighted SAE (WSAE). Experiments across multiple settings validate our theoretical findings and demonstrate that our WSAE significantly improves feature monosemanticity and interpretability.

</details>

---

### 46. [Sentiment-Aware Stock Price Prediction with Transformer and LLM-Generated Formulaic Alpha](https://arxiv.org/abs/2508.04975)

**基本信息**

- 🔗 arXiv: [`2508.04975`](https://arxiv.org/abs/2508.04975)
- 👥 作者: Qizhao Chen, Hiroaki Kawashima
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.04975.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕使用大型语言模型（LLM）生成用于金融预测的公式化阿尔法因子，这属于‘化学大模型’主题在交叉领域（金融AI/量化交易）的应用。LLM作为核心模型被用于生成和理解复杂模式。

**📖 中文摘要**

本文提出了一种新颖的股票价格预测框架，该框架将基于提示的大型语言模型（LLM）与Transformer模型相结合。LLM利用历史股票特征、技术指标和相关公司的情感分数等结构化输入，生成多样化和自适应的公式化阿尔法因子。这些LLM生成的阿尔法因子并非直接用于交易，而是被视为捕捉金融数据中复杂依赖关系的高级特征。随后，这些阿尔法特征被输入到Transformer、LSTM等预测模型中，以预测未来的股票价格。实验结果表明，LLM生成的阿尔法因子显著提高了预测准确性。此外，LLM提供的伴随自然语言推理增强了预测的可解释性和透明度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Traditionally, traders and quantitative analysts address alpha decay by manually crafting formulaic alphas, mathematical expressions that identify patterns or signals in financial data, through domain expertise and trial-and-error. This process is often time-consuming and difficult to scale. With recent advances in large language models (LLMs), it is now possible to automate the generation of such alphas by leveraging the reasoning capabilities of LLMs. This paper introduces a novel framework that integrates a prompt-based LLM with a Transformer model for stock price prediction. The LLM first generates diverse and adaptive alphas using structured inputs such as historical stock features (Close, Open, High, Low, Volume), technical indicators, sentiment scores of both target and related companies. These alphas, instead of being used directly for trading, are treated as high-level features that capture complex dependencies within the financial data. To evaluate the effectiveness of these LLM-generated formulaic alphas, the alpha features are then fed into prediction models such as Transformer, LSTM, TCN, SVR, and Random Forest to forecast future stock prices. Experimental results demonstrate that the LLM-generated alphas significantly improve predictive accuracy. Moreover, the accompanying natural language reasoning provided by the LLM enhances the interpretability and transparency of the predictions, supporting more informed financial decision-making.

</details>

---

### 47. [Adaptive Alpha Weighting with PPO: Enhancing Prompt-Based LLM-Generated Alphas in Quant Trading](https://arxiv.org/abs/2509.01393)

**基本信息**

- 🔗 arXiv: [`2509.01393`](https://arxiv.org/abs/2509.01393)
- 👥 作者: Qizhao Chen, Hiroaki Kawashima
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.01393.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕使用大型语言模型（LLM）生成交易信号（公式化阿尔法），并利用强化学习进行优化。这属于‘化学大模型’主题在金融AI领域的应用实例。

**📖 中文摘要**

本文引入了一个强化学习框架，该框架使用近端策略优化（PPO）来动态优化多个大型语言模型（LLM）生成的公式化阿尔法因子的权重，用于股票交易策略。公式化阿尔法是从价格、成交量、情感等数据中衍生出的数学定义的交易信号。研究利用DeepSeek模型为十只股票生成五十个阿尔法因子，然后使用PPO实时调整它们的权重。实验结果表明，PPO优化策略在大多数情况下实现了更高的夏普比率和更小的最大回撤，突显了强化学习在阿尔法权重分配中的重要性，并展示了将LLM生成的信号与自适应优化相结合用于稳健金融预测和交易的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper introduces a reinforcement learning framework that employs Proximal Policy Optimization (PPO) to dynamically optimize the weights of multiple large language model (LLM)-generated formulaic alphas for stock trading strategies. Formulaic alphas are mathematically defined trading signals derived from price, volume, sentiment, and other data. Although recent studies have shown that LLMs can generate diverse and effective alphas, a critical challenge lies in how to adaptively integrate them under varying market conditions. To address this gap, we leverage a DeepSeek model to generate fifty alphas for ten stocks, and then use PPO to adjust their weights in real time. Experimental results indicate that the PPO-optimized strategy does not consistently deliver the highest cumulative returns across all stocks, but it achieves comparatively higher Sharpe ratios and smaller maximum drawdowns in most cases. When compared with baseline strategies, including equal-weighted, buy-and-hold, random entry/exit, and momentum approaches, PPO demonstrates more stable risk-adjusted performance. The findings highlight the importance of reinforcement learning in the allocation of alpha weights and show the potential of combining LLM-generated signals with adaptive optimization for robust financial forecasting and trading.

</details>

---

### 48. [Learning Explicit Single-Cell Dynamics Using ODE Representations](https://arxiv.org/abs/2510.02903)

**基本信息**

- 🔗 arXiv: [`2510.02903`](https://arxiv.org/abs/2510.02903)
- 👥 作者: Jan-Philipp von Bassewitz, Adeel Pervez, Marco Fumero 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.02903.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于建模单细胞数据（一种重要的生物医学数据）动力学的机器学习模型（Cell-MNN）。虽然主题是生物信息学，但其核心是构建一个用于理解和推理复杂生物系统（可类比为‘化学信息学’中的分子系统）的‘模型’。该模型学习显式的、可解释的基因相互作用规则，这与‘化学大模型’旨在理解和预测分子性质与相互作用的目的一致。

**📖 中文摘要**

本文提出细胞机制神经网络（Cell-MNN），一种编码器-解码器架构，其潜在表示是一个局部线性化的常微分方程（ODE），用于控制从干细胞到组织细胞的细胞演化动力学。Cell-MNN是完全端到端的（除了标准的PCA预处理），其ODE表示明确地学习了生物学上一致且可解释的基因相互作用。该模型旨在对单细胞数据集中的细胞分化动力学进行建模，这是一个对理解癌症等疾病至关重要的领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modeling the dynamics of cellular differentiation is fundamental to advancing the understanding and treatment of diseases associated with this process, such as cancer. With the rapid growth of single-cell datasets, this has also become a particularly promising and active domain for machine learning. Current state-of-the-art models, however, rely on computationally expensive optimal transport preprocessing and multi-stage training, while also not discovering explicit gene interactions. To address these challenges we propose Cell-Mechanistic Neural Networks (Cell-MNN), an encoder-decoder architecture whose latent representation is a locally linearized ODE governing the dynamics of cellular evolution from stem to tissue cells. Cell-MNN is fully end-to-end (besides a standard PCA pre-processing) and its ODE representation explicitly learns biologically consistent and interpretable gene interactions. Empirically, we show that Cell-MNN achieves competitive performance on single-cell benchmarks, surpasses state-of-the-art baselines in scaling to larger datasets and joint training across multiple datasets, while also learning interpretable gene interactions that we validate against the TRRUST database of gene interactions.

</details>

---

### 49. [Factuality Matters: When Image Generation and Editing Meet Structured Visuals](https://arxiv.org/abs/2510.05091)

**基本信息**

- 🔗 arXiv: [`2510.05091`](https://arxiv.org/abs/2510.05091)
- 👥 作者: Le Zhuo, Songhao Han, Yuandong Pu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.05091.pdf)

**💡 相关性分析**

满足标准2：论文提供了可用于特定主题（结构化视觉生成与编辑）的大规模数据集（130万对图像）和评估基准（StructBench）。虽然其直接应用领域是计算机视觉和图形学，但其构建高质量、带有多模态推理注释的数据集的方法论，对于‘化学大模型’和‘质谱结构推理’领域构建类似的数据资源（如分子结构-性质数据集、质谱-分子结构配对数据集）具有重要的参考和借鉴价值。

**📖 中文摘要**

本文首次对结构化视觉（如图表、图表、数学图形）的生成和编辑任务进行了全面、系统的研究。虽然现代视觉生成模型擅长创建美观的自然图像，但在需要构图规划、文本渲染和多模态推理以确保事实保真度的结构化视觉方面却存在困难。为此，作者构建了一个包含130万对高质量结构化图像的大规模数据集，这些数据源自可执行的绘图程序，并辅以思维链推理注释。在此基础上，他们训练了一个统一的模型，该模型通过轻量级连接器将视觉语言模型（VLM）与FLUX.1 Kontext集成，以增强多模态理解。此外，还引入了StructBench评估基准和StructScore评估指标。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While modern visual generation models excel at creating aesthetically pleasing natural images, they struggle with producing or editing structured visuals like charts, diagrams, and mathematical figures, which demand composition planning, text rendering, and multimodal reasoning for factual fidelity. To address this, we present the first comprehensive, systematic investigation of this domain, encompassing data construction, model training, and an evaluation benchmark. First, we construct a large-scale dataset of 1.3 million high-quality structured image pairs derived from executable drawing programs and augmented with chain-of-thought reasoning annotations. Building on it, we train a unified model that integrates a VLM with FLUX.1 Kontext via a lightweight connector for enhanced multimodal understanding. A three-stage training curriculum enables progressive feature alignment, knowledge infusion, and reasoning-augmented generation, further boosted by an external reasoner at inference time. Finally, we introduce StructBench, a novel benchmark for generation and editing with over 1,700 challenging instances, and an accompanying evaluation metric, StructScore, which employs a multi-round Q\&A protocol to assess fine-grained factual accuracy. Evaluations of 15 models reveal that even leading closed-source systems remain far from satisfactory. Our model attains strong editing performance, and inference-time reasoning yields consistent gains across diverse architectures. By releasing the dataset, model, and benchmark, we aim to advance unified multimodal foundations for structured visuals.

</details>

---

### 50. [TIGeR: Tool-Integrated Geometric Reasoning in Vision-Language Models for Robotics](https://arxiv.org/abs/2510.07181)

**基本信息**

- 🔗 arXiv: [`2510.07181`](https://arxiv.org/abs/2510.07181)
- 👥 作者: Yi Han, Enshen Zhou, Shanyu Rong 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.07181.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于增强模型几何推理能力的框架（TIGeR）并发布了配套的大规模数据集（TIGeR-300K）。该框架的核心思想是让大模型（VLM）学会调用外部工具进行精确计算，这与‘化学大模型’或‘质谱结构推理’中可能需要的调用专业化学信息学工具（如量子化学计算、谱图数据库搜索）来完成精确分子属性预测或结构解析的思路高度一致。该工作为相关领域提供了方法论和数据集资源。

**📖 中文摘要**

本文提出了TIGeR（工具集成几何推理），一个新颖的框架，通过使视觉语言模型（VLMs）能够通过外部工具生成和执行精确的几何计算，将其从感知估计器转变为几何计算机。该框架不是试图将复杂的几何操作内化在神经网络中，而是授权模型识别几何推理需求、合成适当的计算代码并调用专用库进行精确计算。为了支持这一范式，作者引入了TIGeR-300K，一个全面的工具调用导向数据集，涵盖点变换、姿态估计和空间兼容性验证，并包含工具调用序列和中间计算。通过结合监督微调（SFT）和强化微调（RFT）的两阶段训练流程，TIGeR在几何推理基准上实现了最先进的性能，并在真实世界机器人操作任务中展示了厘米级精度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language Models (VLMs) have shown remarkable capabilities in spatial reasoning, yet they remain fundamentally limited to qualitative precision and lack the computational precision required for real-world robotics. Current approaches fail to leverage metric cues from depth sensors and camera calibration, instead reducing geometric problems to pattern recognition tasks that cannot deliver the centimeter-level accuracy essential for robotic manipulation. We present TIGeR (Tool-Integrated Geometric Reasoning), a novel framework that transforms VLMs from perceptual estimators to geometric computers by enabling them to generate and execute precise geometric computations through external tools. Rather than attempting to internalize complex geometric operations within neural networks, TIGeR empowers models to recognize geometric reasoning requirements, synthesize appropriate computational code, and invoke specialized libraries for exact calculations. To support this paradigm, we introduce TIGeR-300K, a comprehensive tool-invocation-oriented dataset covering point transformations, pose estimation, and spatial compatibility verification, complete with tool invocation sequences and intermediate computations. Through a two-stage training pipeline combining supervised fine-tuning (SFT) and reinforcement fine-tuning (RFT) with our proposed hierarchical reward design, TIGeR achieves SOTA performance on geometric reasoning benchmarks while demonstrating centimeter-level precision in real-world robotic manipulation tasks.

</details>

---

### 51. [GraphMERT: Efficient and Scalable Distillation of Reliable Knowledge Graphs from Unstructured Data](https://arxiv.org/abs/2510.09580)

**基本信息**

- 🔗 arXiv: [`2510.09580`](https://arxiv.org/abs/2510.09580)
- 👥 作者: Margarita Belova, Jiaxin Xiao, Shikhar Tuli 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.09580.pdf)

**💡 相关性分析**

满足标准1和2：1. 论文核心研究内容是开发一个从文本中自动构建高质量、可靠知识图谱（KG）的模型（GraphMERT）。知识图谱是化学信息学和许多科学领域（包括质谱解析）中用于表示和推理分子、反应、性质等实体关系的核心数据结构。构建化学领域KG是‘化学大模型’的重要数据基础和应用方向。2. 论文提出的模型和方法（GraphMERT）本身就是一个用于构建领域特定KG的工具/资源，可直接应用于化学文本（如科研文献、专利）以构建化学知识图谱。

**📖 中文摘要**

本文介绍了GraphMERT，一个微型的图编码器模型，用于从非结构化文本语料库及其内部表示中提取高质量的知识图谱（KGs）。GraphMERT及其等效的KG形成了一个模块化的神经符号堆栈：用于抽象概念的神经学习；用于可验证推理的符号KG。GraphMERT + KG是第一个高效且可扩展的神经符号模型，在基准测试中实现了最先进的准确性，并相对于基线具有优越的符号表示。具体目标是获得可靠（具有来源）且有效（具有本体一致关系和领域适当语义）的领域特定KG。在从PubMed糖尿病论文获取的文本上，80M参数的GraphMERT产生的KG实现了69.8%的FActScore；而320亿参数的基线LLM产生的KG仅达到40.2%的FActScore。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Researchers have pursued neurosymbolic artificial intelligence (AI) applications for nearly three decades. A marriage of the neural and symbolic components can lead to rapid advancements in AI. Yet, the field has not realized this promise since most neurosymbolic AI frameworks fail to scale. In addition, the implicit representations and approximate reasoning of purely neural approaches limit interpretability and trust. Knowledge graphs (KGs), a gold-standard representation of explicit semantic knowledge, can address the symbolic side of the problem. However, automatically deriving reliable KGs from text corpora remains an open problem. We address these challenges by introducing GraphMERT, a tiny graphical encoder-only model that distills high-quality KGs from unstructured text corpora and its own internal representations. GraphMERT and its equivalent KG form a modular neurosymbolic stack: neural learning of abstractions; symbolic KGs for verifiable reasoning. GraphMERT + KG is the first efficient and scalable neurosymbolic model to achieve state-of-the-art benchmark accuracy along with superior symbolic representations relative to baselines. Concretely, we target reliable domain-specific KGs that are both (1) factual (with provenance) and (2) valid (ontology-consistent relations with domain-appropriate semantics). When a large language model (LLM), e.g., Qwen3-32B, generates domain-specific KGs, it falls short on reliability due to prompt sensitivity, shallow domain expertise, and hallucinated relations. On text obtained from PubMed papers on diabetes, our 80M-parameter GraphMERT yields a KG with a 69.8% FActScore; a 32B-parameter baseline LLM yields a KG that achieves only 40.2% FActScore. The GraphMERT KG also attains a higher ValidityScore of 68.8%, versus 43.0% for the LLM baseline.

</details>

---

### 52. [The Geometry of Reasoning: Flowing Logics in Representation Space](https://arxiv.org/abs/2510.09782)

**基本信息**

- 🔗 arXiv: [`2510.09782`](https://arxiv.org/abs/2510.09782)
- 👥 作者: Yufa Zhou, Yixiao Wang, Xunjian Yin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.09782.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深入分析和理解大型语言模型（LLM）内部的推理机制，使用几何框架对其表示空间中的逻辑流进行建模。这直接关系到‘化学大模型’主题中一个核心且前沿的子方向：大模型的可解释性与机理研究。理解LLM如何在化学领域（如分子性质预测、反应结果推理）进行推理，对于构建可靠、可信的化学AI模型至关重要。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）如何通过其表示空间进行“思考”。作者提出了一个新颖的几何框架，将LLM的推理建模为流——嵌入轨迹在逻辑行进之处演化。通过使用具有不同语义载体的相同自然演绎命题，他们将逻辑结构与语义分离开来，从而测试LLMs是否内化了超越表面形式的逻辑。这一视角将推理与位置、速度和曲率等几何量联系起来，使得在表示空间和概念空间中进行形式分析成为可能。该理论建立了两点：(1) LLM推理对应于表示空间中的平滑流，(2) 逻辑语句充当这些流速度的局部控制器。使用学习到的表示代理，他们设计了受控实验来可视化和量化推理流，为理论框架提供了实证验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study how large language models (LLMs) ``think'' through their representation space. We propose a novel geometric framework that models an LLM's reasoning as flows -- embedding trajectories evolving where logic goes. We disentangle logical structure from semantics by employing the same natural deduction propositions with varied semantic carriers, allowing us to test whether LLMs internalize logic beyond surface form. This perspective connects reasoning with geometric quantities such as position, velocity, and curvature, enabling formal analysis in representation and concept spaces. Our theory establishes: (1) LLM reasoning corresponds to smooth flows in representation space, and (2) logical statements act as local controllers of these flows' velocities. Using learned representation proxies, we design controlled experiments to visualize and quantify reasoning flows, providing empirical validation of our theoretical framework. Our findings indicate that training solely via next-token prediction can lead LLMs to internalize logical invariants as higher-order geometry in representation space, challenging the ``stochastic parrot'' argument. Experiments across Qwen and LLaMA model families further suggest the presence of a general, possibly universal, representational law underlying machine understanding and human linguistic regularities, largely independent of specific training recipes or model architectures. Our work serves as both a conceptual foundation and practical tools for studying reasoning phenomena, offering a new lens for interpretability and formal analysis of LLMs' behavior.

</details>

---

### 53. [Proof Strategy Extraction from LLMs for Enhancing Symbolic Provers](https://arxiv.org/abs/2510.10131)

**基本信息**

- 🔗 arXiv: [`2510.10131`](https://arxiv.org/abs/2510.10131)
- 👥 作者: Jian Fang, Yican Sun, Yingfei Xiong
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.10131.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是关于如何从大型语言模型（LLM）中提取其内部知识（证明策略）来增强传统符号系统（定理证明器）。这属于‘化学大模型’与符号AI、自动化推理交叉的前沿研究方向。在化学信息学中，类似的思想可以应用于让LLM学习化学规则（如反应规则、光谱解读经验），然后将其形式化以增强传统的化学推理系统（如逆合成分析器、谱图解析软件）。

**📖 中文摘要**

本文提出了一个新的研究问题：能否从大型语言模型（LLMs）中提取其内部证明策略，以增强符号证明器的能力？作为初步步骤，作者引入了Strat2Rocq。在离线阶段，Strat2Rocq从LLMs中提取证明策略，并将其形式化为Rocq中的引理。在线阶段，给定一个待证明的定理，Strat2Rocq用这些提取的引理增强证明上下文，使CoqHammer能够利用LLM衍生的策略进行更有效的自动证明。评估表明，在用于软件验证的开源Rocq项目上，Strat2Rocq将CoqHammer的成功率提高了13.41%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

One important approach to software verification is interactive theorem proving. However, writing formal proofs often requires substantial human effort, making proof automation highly important. Traditionally, proof automation has relied on symbolic provers. Recently, large language models (LLMs) have demonstrated strong capabilities in theorem proving, complementing symbolic provers. Nonetheless, prompting LLMs can be expensive and may pose security risks for confidential codebases. As a result, purely symbolic approaches remain important even in the LLM era, as they are cost-effective, secure, and complement the strengths of LLMs. Motivated by these considerations, we pose a new research question: can the internal proof strategies of LLMs be extracted to enhance the capabilities of symbolic provers? As an initial step, we introduce Strat2Rocq. In an offline stage, Strat2Rocq extracts proof strategies from LLMs and formalizes them as lemmas in Rocq. In an online stage, given a theorem to be proved, Strat2Rocq augments the proof context with these extracted lemmas, enabling CoqHammer to leverage the LLM-derived strategies for more effective automated proving. Our evaluation demonstrates that, on open-source Rocq projects for software verification, Strat2Rocq enhances the success rate of CoqHammer by 13.41%. A side discovery is that the extracted lemmas are also beneficial to LLM proof agents, improving the success rate of an LLM proof agent by 4.00%.

</details>

---

### 54. [Circuit Insights: Towards Interpretability Beyond Activations](https://arxiv.org/abs/2510.14936)

**基本信息**

- 🔗 arXiv: [`2510.14936`](https://arxiv.org/abs/2510.14936)
- 👥 作者: Elena Golimblevskaia, Aakriti Jain, Bruno Puri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.14936.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发新的方法（WeightLens和CircuitLens）来增强对神经网络（包括大型模型）内部机制和电路的可解释性分析。这直接关系到‘化学大模型’主题中的一个关键挑战：理解化学大模型做出预测的底层原因和逻辑，这对于在科学发现中建立信任和发现新知识至关重要。该工作提供了可应用于化学领域模型分析的工具性方法论。

**📖 中文摘要**

本文提出了WeightLens和CircuitLens两种互补的方法，超越了基于激活的分析，用于神经网络的可解释性和机制可解释性。WeightLens直接从学习到的权重中解释特征，无需解释模型或数据集，同时在上下文无关特征上匹配或超越现有方法的性能。CircuitLens捕捉特征激活如何从组件之间的相互作用中产生，揭示了仅基于激活的方法无法识别的电路级动态。这些方法共同提高了可解释性的鲁棒性，并增强了电路的可扩展机制分析，同时保持了效率和质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The fields of explainable AI and mechanistic interpretability aim to uncover the internal structure of neural networks, with circuit discovery as a central tool for understanding model computations. Existing approaches, however, rely on manual inspection and remain limited to toy tasks. Automated interpretability offers scalability by analyzing isolated features and their activations, but it often misses interactions between features and depends strongly on external LLMs and dataset quality. Transcoders have recently made it possible to separate feature attributions into input-dependent and input-invariant components, providing a foundation for more systematic circuit analysis. Building on this, we propose WeightLens and CircuitLens, two complementary methods that go beyond activation-based analysis. WeightLens interprets features directly from their learned weights, removing the need for explainer models or datasets while matching or exceeding the performance of existing methods on context-independent features. CircuitLens captures how feature activations arise from interactions between components, revealing circuit-level dynamics that activation-only approaches cannot identify. Together, these methods increase interpretability robustness and enhance scalable mechanistic analysis of circuits while maintaining efficiency and quality.

</details>

---

### 55. [Composition-Grounded Data Synthesis for Visual Reasoning](https://arxiv.org/abs/2510.15040)

**基本信息**

- 🔗 arXiv: [`2510.15040`](https://arxiv.org/abs/2510.15040)
- 👥 作者: Xinyi Gu, Jiayuan Mao, Zhang-Wei Hong 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.15040.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于高效合成多模态推理训练数据的框架（COGS）和相应的方法论。对于‘化学大模型’和‘质谱结构推理’领域，获取高质量、大规模的标注数据（如分子结构-性质对、质谱-分子结构对）通常成本高昂。COGS提供了一种通过分解和重组现有数据来合成新训练数据的系统方法，这对于扩充化学和质谱领域的训练资源具有重要的潜在应用价值。

**📖 中文摘要**

本文介绍了COGS（基于组合的数据合成），一个数据高效的框架，用于从一小部分种子问题中为多模态大语言模型（MLLMs）配备高级推理能力。核心思想是将每个种子问题分解为原始感知和推理因素，然后可以系统地与新的图像重新组合，以生成大量的合成问答对。每个生成的问题都配有子问题和中间答案，从而能够通过因子级过程奖励进行强化学习。在图表推理上的实验表明，COGS显著提高了对未见问题的性能，在推理密集和组合性问题上的收益最大。此外，使用不同种子数据的因子级混合进行训练可以在多个数据集上实现更好的迁移，表明COGS诱导了可泛化的能力，而非数据集特定的过拟合。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pretrained multi-modal large language models (MLLMs) demonstrate strong performance on diverse multimodal tasks, but remain limited in reasoning capabilities for domains where annotations are difficult to collect. In this work, we focus on artificial image domains such as charts, rendered documents, and webpages, which are abundant in practice yet lack large-scale human annotated reasoning datasets. We introduce COGS (COmposition-Grounded data Synthesis), a data-efficient framework for equipping MLLMs with advanced reasoning abilities from a small set of seed questions. The key idea is to decompose each seed question into primitive perception and reasoning factors, which can then be systematically recomposed with new images to generate large collections of synthetic question-answer pairs. Each generated question is paired with subquestions and intermediate answers, enabling reinforcement learning with factor-level process rewards. Experiments on chart reasoning show that COGS substantially improves performance on unseen questions, with the largest gains on reasoning-heavy and compositional questions. Moreover, training with a factor-level mixture of different seed data yields better transfer across multiple datasets, suggesting that COGS induces generalizable capabilities rather than dataset-specific overfitting. We further demonstrate that the framework extends beyond charts to other domains such as webpages.

</details>

---

### 56. [AMiD: Knowledge Distillation for LLMs with $α$-mixture Assistant Distribution](https://arxiv.org/abs/2510.15982)

**基本信息**

- 🔗 arXiv: [`2510.15982`](https://arxiv.org/abs/2510.15982)
- 👥 作者: Donghyeok Shin, Yeongmin Kim, Suhyeon Jo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.15982.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大型语言模型（LLM）的知识蒸馏提出一种新的、改进的框架（AMiD）。知识蒸馏是将大模型能力迁移到小模型的关键技术，对于在资源受限环境下（如实验室边缘设备）部署高效的‘化学大模型’或‘质谱结构推理’模型具有重要意义。该工作提供了前沿的模型压缩与优化方法。

**📖 中文摘要**

本文提出了α-混合辅助分布，一种新颖的广义辅助分布族，以及α-混合蒸馏（AMiD），一个使用辅助分布进行知识蒸馏的统一框架。α-混合辅助分布通过引入一个新的分布设计变量α，提供了辅助分布的连续扩展，该变量在所有先前方法中都是固定的。此外，AMiD基于最优性推广了与辅助分布一起使用的散度族，这在先前工作中也受到限制。通过大量实验，作者证明AMiD通过利用更广泛且理论基础的辅助分布空间，提供了卓越的性能和训练稳定性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autoregressive large language models (LLMs) have achieved remarkable improvement across many tasks but incur high computational and memory costs. Knowledge distillation (KD) mitigates this issue by transferring knowledge from a large teacher to a smaller student through distributional alignment. Previous studies have proposed various discrepancy metrics, but the capacity gap and training instability caused by near-zero probabilities, stemming from the high-dimensional output of LLMs, remain fundamental limitations. To overcome these challenges, several approaches implicitly or explicitly incorporating assistant distribution have recently been proposed. However, the past proposals of assistant distributions have been a fragmented approach without a systematic investigation of the interpolation path and the divergence. This paper proposes $\alpha$-mixture assistant distribution, a novel generalized family of assistant distributions, and $\alpha$-mixture distillation, coined AMiD, a unified framework for KD using the assistant distribution. The $\alpha$-mixture assistant distribution provides a continuous extension of the assistant distribution by introducing a new distribution design variable $\alpha$, which has been fixed in all previous approaches. Furthermore, AMiD generalizes the family of divergences used with the assistant distributions based on optimality, which has also been restricted in previous works. Through extensive experiments, we demonstrate that AMiD offers superior performance and training stability by leveraging a broader and theoretically grounded assistant distribution space. We release the code at \href{ this https URL }{this https URL}.

</details>

---

### 57. [Annotation-Efficient Universal Honesty Alignment](https://arxiv.org/abs/2510.17509)

**基本信息**

- 🔗 arXiv: [`2510.17509`](https://arxiv.org/abs/2510.17509)
- 👥 作者: Shiyu Ni, Keping Bi, Jiafeng Guo 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.17509.pdf)

**💡 相关性分析**

满足标准2：论文发布了用于评估和提升大模型诚实性（校准置信度）的大规模基准数据集（HonestyBench）。在‘化学大模型’和‘质谱结构推理’等科学AI应用中，模型的校准性和诚实性（即知道何时不知道）至关重要，因为它关系到预测结果的可信度和安全性。该数据集和评估框架为开发可靠的化学领域大模型提供了重要的评估工具和基准。

**📖 中文摘要**

本文引入了启发-然后校准（EliCal），一个两阶段框架，首先使用廉价的自我一致性监督来引发内部置信度，然后使用一小组正确性注释来校准此置信度。为了支持大规模研究，作者发布了HonestyBench，一个涵盖十个自由形式QA数据集的基准，包含56万个训练和7万个评估实例，并标注了正确性和自我一致性信号。实验表明，EliCal仅用1k个正确性注释（全监督的0.18%）就实现了近乎最优的对齐，并且在未见过的MMLU任务上比仅校准的基线具有更好的对齐性能，为LLMs中的通用诚实对齐提供了可扩展的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Honesty alignment-the ability of large language models (LLMs) to recognize their knowledge boundaries and express calibrated confidence-is essential for trustworthy deployment. Existing methods either rely on training-free confidence estimation (e.g., token probabilities, self-consistency) or training-based calibration with correctness annotations. While effective, achieving universal honesty alignment with training-based calibration requires costly, large-scale labeling. To support annotation-efficient training, we introduce Elicitation-Then-Calibration (EliCal), a two-stage framework that first elicits internal confidence using inexpensive self-consistency supervision, then calibrates this confidence with a small set of correctness annotations. To support a large-scale study, we release HonestyBench, a benchmark covering ten free-form QA datasets with 560k training and 70k evaluation instances annotated with correctness and self-consistency signals. Experiments show that EliCal achieves near-optimal alignment with only 1k correctness annotations (0.18% of full supervision) and better alignment performance on unseen MMLU tasks than the calibration-only baseline, offering a scalable solution toward universal honesty alignment in LLMs.

</details>

---

### 58. [Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents](https://arxiv.org/abs/2510.24702)

**基本信息**

- 🔗 arXiv: [`2510.24702`](https://arxiv.org/abs/2510.24702)
- 👥 作者: Yueqi Song, Ketan Ramaneti, Zaid Sheikh 等21人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.24702.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于统一和标准化智能体训练数据的协议（ADP），并发布了相应的代码和转换后的数据集。对于‘化学大模型’领域，特别是当模型需要与外部工具（如化学数据库、模拟软件）交互以完成复杂任务（如自动化实验设计、分子优化）时，构建和利用高质量的智能体训练数据是关键。ADP为化学领域构建类似的工具调用和任务执行数据集提供了通用的数据格式标准和实践范例。

**📖 中文摘要**

本文引入了智能体数据协议（ADP），一种轻量级的表示语言，充当不同格式的智能体数据集与下游统一智能体训练管道之间的“中间语言”。ADP的设计具有足够的表达能力，可以捕获各种任务，包括API/工具使用、浏览、编码、软件工程和一般智能体工作流，同时保持简单易解析，无需在每数据集级别进行工程处理。在实验中，作者将13个现有智能体训练数据集的广泛集合统一为ADP格式，并将标准化的ADP数据转换为多个智能体框架的训练就绪格式。他们对这些数据进行了SFT，并证明了相对于相应的基础模型平均性能增益约为20%，并且在标准编码、浏览、工具使用和研究基准上提供了最先进或接近SOTA的性能，而无需领域特定调整。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Public research results on large-scale supervised finetuning of AI agents remain relatively rare, since the collection of agent training data presents unique challenges. In this work, we argue that the bottleneck is not a lack of underlying data sources, but that a large variety of data is fragmented across heterogeneous formats, tools, and interfaces. To this end, we introduce the agent data protocol (ADP), a light-weight representation language that serves as an "interlingua" between agent datasets in diverse formats and unified agent training pipelines downstream. The design of ADP is expressive enough to capture a large variety of tasks, including API/tool use, browsing, coding, software engineering, and general agentic workflows, while remaining simple to parse and train on without engineering at a per-dataset level. In experiments, we unified a broad collection of 13 existing agent training datasets into ADP format, and converted the standardized ADP data into training-ready formats for multiple agent frameworks. We performed SFT on these data, and demonstrated an average performance gain of ~20% over corresponding base models, and delivers state-of-the-art or near-SOTA performance on standard coding, browsing, tool use, and research benchmarks, without domain-specific tuning. All code and data are released publicly, in the hope that ADP could help lower the barrier to standardized, scalable, and reproducible agent training.

</details>

---

### 59. [Weakly Supervised Concept Learning with Class-Level Priors for Interpretable Medical Diagnosis](https://arxiv.org/abs/2511.01131)

**基本信息**

- 🔗 arXiv: [`2511.01131`](https://arxiv.org/abs/2511.01131)
- 👥 作者: Md Nahiduzzaman, Steven Korevaar, Alireza Bab-Hadiashar 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.01131.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种弱监督框架（PCP），用于在医学图像诊断中学习可解释的概念预测器，而无需昂贵的像素级或实例级概念标注。这直接关联到‘化学大模型’和‘质谱结构推理’中的一个共同挑战：如何让模型学习到人类可理解的、与领域知识（如化学官能团、质谱碎片离子）对齐的中间概念或特征，特别是在标注数据稀缺的情况下。PCP提供了一种利用类级别先验知识进行弱监督概念学习的方法论，可迁移至化学领域。

**📖 中文摘要**

本文提出了一种新颖的先验引导概念预测器（PCP），一个弱监督框架，无需显式监督或依赖语言模型即可实现概念答案预测。PCP利用类级概念先验作为弱监督，并结合了带有KL散度和熵正则化的细化机制，以使预测与临床推理保持一致。在PH2（皮肤镜）和WBCatt（血液学）上的实验表明，与零样本基线相比，PCP将概念级F1分数提高了33%以上，同时在四个医学数据集上相对于完全监督的概念瓶颈模型（CBMs）和V-IP提供了具有竞争力的分类性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Human-interpretable predictions are essential for deploying AI in medical imaging, yet most interpretable-by-design (IBD) frameworks require concept annotations for training data, which are costly and impractical to obtain in clinical contexts. Recent attempts to bypass annotation, such as zero-shot vision-language models or concept-generation frameworks, struggle to capture domain-specific medical features, leading to poor reliability. In this paper, we propose a novel Prior-guided Concept Predictor (PCP), a weakly supervised framework that enables concept answer prediction without explicit supervision or reliance on language models. PCP leverages class-level concept priors as weak supervision and incorporates a refinement mechanism with KL divergence and entropy regularization to align predictions with clinical reasoning. Experiments on PH2 (dermoscopy) and WBCatt (hematology) show that PCP improves concept-level F1-score by over 33% compared to zero-shot baselines, while delivering competitive classification performance on four medical datasets (PH2, WBCatt, HAM10000, and CXR4) relative to fully supervised concept bottleneck models (CBMs) and V-IP.

</details>

---

### 60. [SpecBridge: Bridging Mass Spectrometry and Molecular Representations via Cross-Modal Alignment](https://arxiv.org/abs/2601.17204)

**基本信息**

- 🔗 arXiv: [`2601.17204`](https://arxiv.org/abs/2601.17204)
- 👥 作者: Yinkai Wang, Yan Zhou Chen, Xiaohui Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.17204.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”这一主题，提出了一种新的深度学习框架（SpecBridge）用于从串联质谱数据中推断分子结构。

**📖 中文摘要**

本文提出了一种名为SpecBridge的新型隐式对齐框架，用于解决串联质谱（MS/MS）中的小分子结构鉴定问题。该框架将结构识别视为一个几何对齐问题，通过微调一个自监督的质谱编码器（DreaMS），使其直接投影到一个冻结的分子基础模型（ChemBERTa）的潜在空间中。然后，通过余弦相似度在预计算的分子嵌入库中进行检索来完成鉴定。与需要从头设计跨模态子空间的联合对比模型或显式生成分子图的生成模型不同，SpecBridge提供了一种更稳定、更实用的替代方案。在MassSpecGym、Spectraverse和MSnLib等多个基准测试中，SpecBridge相对于强大的神经基线模型，将Top-1检索准确率提高了约20-25%，同时保持了较少的可训练参数量。这项工作表明，与冻结的基础模型对齐是实现质谱结构推理的一种有效策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Small-molecule identification from tandem mass spectrometry (MS/MS) remains a bottleneck in untargeted settings where spectral libraries are incomplete. While deep learning offers a solution, current approaches typically fall into two extremes: explicit generative models that construct molecular graphs atom-by-atom, or joint contrastive models that learn cross-modal subspaces from scratch. We introduce SpecBridge, a novel implicit alignment framework that treats structure identification as a geometric alignment problem. SpecBridge fine-tunes a self-supervised spectral encoder (DreaMS) to project directly into the latent space of a frozen molecular foundation model (ChemBERTa), and then performs retrieval by cosine similarity to a fixed bank of precomputed molecular embeddings. Across MassSpecGym, Spectraverse, and MSnLib benchmarks, SpecBridge improves top-1 retrieval accuracy by roughly 20-25% relative to strong neural baselines, while keeping the number of trainable parameters small. These results suggest that aligning to frozen foundation models is a practical, stable alternative to designing new architectures from scratch. The code for SpecBridge is released at this https URL .

</details>

---

### 61. [Causal Circuit Tracing Reveals Distinct Computational Architectures in Single-Cell Foundation Models: Inhibitory Dominance, Biological Coherence, and Cross-Model Convergence](https://arxiv.org/abs/2603.01752)

**基本信息**

- 🔗 arXiv: [`2603.01752`](https://arxiv.org/abs/2603.01752)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01752.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析单细胞生物学基础模型（一种特定领域的化学/生物大模型）的内部因果计算架构，直接围绕“化学大模型”这一主题展开。

**📖 中文摘要**

这篇论文研究了用于单细胞生物学的两个基础模型（Geneformer V2-316M 和 scGPT）的内部计算架构。作者引入了“因果电路追踪”方法，通过消融稀疏自编码器（SAE）特征并测量下游响应，来分析跨网络深度的特征间因果交互。研究揭示了两种模型都表现出显著的抑制性主导和生物学一致性，并且发现了跨模型收敛的保守功能域对。这项工作直接关联到“化学大模型”主题，因为它深入探究了生物化学领域（单细胞组学）基础模型的内部工作机制、可解释性和计算架构，属于对特定领域大模型的机理分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: Sparse autoencoders (SAEs) decompose foundation model activations into interpretable features, but causal feature-to-feature interactions across network depth remain unknown for biological foundation models. Results: We introduce causal circuit tracing by ablating SAE features and measuring downstream responses, and apply it to Geneformer V2-316M and scGPT whole-human across four conditions (96,892 edges, 80,191 forward passes). Both models show approximately 53 percent biological coherence and 65 to 89 percent inhibitory dominance, invariant to architecture and cell type. scGPT produces stronger effects (mean absolute d = 1.40 vs. 1.05) with more balanced dynamics. Cross-model consensus yields 1,142 conserved domain pairs (10.6x enrichment, p < 0.001). Disease-associated domains are 3.59x more likely to be consensus. Gene-level CRISPRi validation shows 56.4 percent directional accuracy, confirming co-expression rather than causal encoding.

</details>

---

### 62. [FLOWR.root: A flow matching based foundation model for joint multi-purpose structure-aware 3D ligand generation and affinity prediction](https://arxiv.org/abs/2510.02578)

**基本信息**

- 🔗 arXiv: [`2510.02578`](https://arxiv.org/abs/2510.02578)
- 👥 作者: Julian Cremer, Tuan Le, Mohammad M. Ghahremanpour 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.02578.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于基于结构的药物设计的生成式AI模型（FLOWR.root），这直接属于“化学大模型”在计算化学和药物发现领域的应用。

**📖 中文摘要**

本文提出了FLOWR.root，一个基于SE(3)-等变流匹配的生成模型，用于口袋感知的3D配体生成，并联合进行效价和结合亲和力预测。该模型支持从头生成、基于相互作用和药效团的条件采样、片段延伸和替换，以及多终点亲和力预测。它结合了大规模配体库和混合精度的蛋白质-配体复合物数据进行训练。这项工作属于“化学大模型”在药物发现领域的直接应用，它构建了一个能够进行多任务（生成与预测）的、面向结构感知药物设计的通用基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present this http URL , an SE(3)-equivariant flow-matching model for pocket-aware 3D ligand generation with joint potency and binding affinity prediction and confidence estimation. The model supports de novo generation, interaction- and pharmacophore-conditional sampling, fragment elaboration and replacement, and multi-endpoint affinity prediction (pIC50, pKi, pKd, pEC50). Training combines large-scale ligand libraries with mixed-fidelity protein-ligand complexes, refined on curated co-crystal datasets and adapted to project-specific data through parameter-efficient finetuning. The base this http URL model achieves state-of-the-art performance in unconditional 3D molecule and pocket-conditional ligand generation. On HiQBind, the pre-trained and finetuned model demonstrates highly accurate affinity predictions, and outperforms recent state-of-the-art methods such as Boltz-2 on the FEP+/OpenFE benchmark with substantial speed advantages. However, we show that addressing unseen structure-activity landscapes requires domain adaptation; parameter-efficient LoRA finetuning yields marked improvements on diverse proprietary datasets and PDE10A. Joint generation and affinity prediction enable inference-time scaling through importance sampling, steering design toward higher-affinity compounds. Case studies validate this: selective CK2$\alpha$ ligand generation against CLK3 shows significant correlation between predicted and quantum-mechanical binding energies. Scaffold elaboration on ER$\alpha$, TYK2, and BACE1 demonstrates strong agreement between predicted affinities and QM calculations while confirming geometric fidelity. By integrating structure-aware generation, affinity estimation, property-guided sampling, and efficient domain adaptation, this http URL provides a comprehensive foundation for structure-based drug design from hit identification through lead optimization.

</details>

---

### 63. [Overcoming the Combinatorial Bottleneck in Symmetry-Driven Crystal Structure Prediction](https://arxiv.org/abs/2602.17176)

**基本信息**

- 🔗 arXiv: [`2602.17176`](https://arxiv.org/abs/2602.17176)
- 👥 作者: Shi Yin, Jinming Mu, Xudong Zhu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.17176.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合大语言模型（LLMs）和生成式AI的框架，用于晶体结构预测，这直接属于“化学大模型”在材料科学和计算化学领域的应用。

**📖 中文摘要**

本文提出了一种对称性驱动的生成框架，用于晶体结构预测（CSP）。该方法利用大语言模型（LLMs）从化学计量和原子数量中编码化学语义并直接生成细粒度的Wyckoff位点模式，从而规避了数据库查找的限制。为了克服组合位点分配的指数级复杂度，作者结合领域知识，通过高效的线性复杂度启发式束搜索算法来严格执行代数一致性。该框架将这种对称一致的模板整合到扩散模型中，将随机生成轨迹约束在物理有效的几何流形上。这项工作将大语言模型（作为化学语义编码器）和生成式AI模型应用于材料发现的根本问题，是“化学大模型”在材料科学领域的典型应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Crystal structure prediction (CSP), which aims to predict the three-dimensional atomic arrangement of a crystal from its composition, is central to materials discovery and mechanistic understanding. However, given the composition and atomic counts in a unit cell, existing methods struggle with the NP-hard combinatorial challenge of rigorous symmetry enforcement or rely on retrieving known templates, which inherently limits both physical fidelity and the ability to discover genuinely new materials. To solve this, we propose a symmetry-driven generative framework. Our approach leverages large language models to encode chemical semantics and directly generate fine-grained Wyckoff patterns from atomic stoichiometry and counts, effectively circumventing the limitations inherent to database lookups. Crucially, to overcome the exponentially complex problem of combinatorial site assignments, we incorporate domain knowledge through an efficient, linear-complexity heuristic beam search algorithm that rigorously enforces algebraic consistency between site multiplicities and atomic stoichiometry and counts. By integrating this symmetry-consistent template into a diffusion backbone, our approach constrains the stochastic generative trajectory to a physically valid geometric manifold. This framework achieves state-of-the-art performance across stability, uniqueness, and novelty (SUN) benchmarks, alongside superior matching performance, thereby establishing a new paradigm for the rigorous exploration of targeted crystallographic space which can be previously uncharted, with no reliance on existing databases or a priori structural knowledge.

</details>

---

### 64. [An Information-Theoretic Framework For Optimizing Experimental Design To Distinguish Probabilistic Neural Codes](https://arxiv.org/abs/2603.01387)

**基本信息**

- 🔗 arXiv: [`2603.01387`](https://arxiv.org/abs/2603.01387)
- 👥 作者: Po-Chen Kuo, Edgar Y. Walker
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01387.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个通用的、理论驱动的实验设计优化框架，其核心思想（最大化区分竞争模型的信息）对于在“化学大模型”和“质谱结构推理”领域设计验证性实验或基准测试具有重要的方法论启示和讨论价值。

**📖 中文摘要**

本文提出了一个信息论框架，用于优化实验设计，以区分两种相互竞争的概率神经编码假说（似然函数编码与后验分布编码）。该框架通过推导“信息间隙”来量化在给定任务设计下两种假说的可区分性，并以此优化刺激分布，从而最大化地区分它们。虽然论文背景是神经科学，但其核心方法论——构建理论驱动的、具有最大区分力的实验设计框架——对于在“化学大模型”或“质谱结构推理”领域设计实验或计算实验来验证不同模型或算法的底层机制具有重要的方法论参考价值。它可以被视为一种为区分复杂模型（如不同的化学信息学推理模型）而优化数据/实验采集策略的通用框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Bayesian brain hypothesis has been a leading theory in understanding perceptual decision-making under uncertainty. While extensive psychophysical evidence supports the notion of the brain performing Bayesian computations, how uncertainty information is encoded in sensory neural populations remains elusive. Specifically, two competing hypotheses propose that early sensory populations encode either the likelihood function (exemplified by probabilistic population codes) or the posterior distribution (exemplified by neural sampling codes) over the stimulus, with the key distinction lying in whether stimulus priors would modulate the neural responses. However, experimentally differentiating these two hypotheses has remained challenging, as it is unclear what task design would effectively distinguish the two. In this work, we present an information-theoretic framework for optimizing the task stimulus distribution that would maximally differentiate competing probabilistic neural codes. To quantify how distinguishable the two probabilistic coding hypotheses are under a given task design, we derive the information gap--the expected performance difference when likelihood versus posterior decoders are applied to neural populations--by evaluating the Kullback-Leibler divergence between the true posterior and a task-marginalized surrogate posterior. Through extensive simulations, we demonstrate that the information gap accurately predicts decoder performance differences across diverse task settings. Critically, maximizing the information gap yields stimulus distributions that optimally differentiate likelihood and posterior coding hypotheses. Our framework enables principled, theory-driven experimental designs with maximal discriminative power to differentiate probabilistic neural codes, advancing our understanding of how neural populations represent and process sensory uncertainty.

</details>

---

### 65. [Conformal Graph Prediction with Z-Gromov Wasserstein Distances](https://arxiv.org/abs/2603.02460)

**基本信息**

- 🔗 arXiv: [`2603.02460`](https://arxiv.org/abs/2603.02460)
- 👥 作者: Gabriel Melo, Thibaut de Saivre, Anna Calissano 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02460.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个用于图结构预测（如分子图）的共形预测框架，这为“质谱结构推理”（其输出常为分子图）和“化学大模型”（常处理分子图）的结果提供了重要的不确定性量化方法和讨论方向。

**📖 中文摘要**

本文提出了一个用于图结构输出的共形预测框架，提供了在结构化输出空间中的分布无关的覆盖保证。该方法通过Z-Gromov-Wasserstein距离（实践中实例化为Fused Gromov-Wasserstein距离）来定义非共形性，从而实现对预测图和候选图之间的置换不变比较。为了获得自适应的预测集，作者将共形化分位数回归（CQR）扩展到处理图值输出等复杂输出空间。该工作为结构化输出（如图、分子）的机器学习模型提供了不确定性量化工具。虽然论文的评估包括分子识别任务，但其主要贡献是通用的图预测不确定性量化框架。这个框架可以直接应用于“质谱结构推理”的产出（如分子图）的不确定性评估，或用于评估“化学大模型”在生成分子时的可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Supervised graph prediction addresses regression problems where the outputs are structured graphs. Although several approaches exist for graph-valued prediction, principled uncertainty quantification remains limited. We propose a conformal prediction framework for graph-valued outputs, providing distribution-free coverage guarantees in structured output spaces. Our method defines nonconformity via the Z-Gromov-Wasserstein distance, instantiated in practice through Fused Gromov-Wasserstein (FGW), enabling permutation invariant comparison between predicted and candidate graphs. To obtain adaptive prediction sets, we introduce Score Conformalized Quantile Regression (SCQR), an extension of Conformalized Quantile Regression (CQR) to handle complex output spaces such as graph-valued outputs. We evaluate the proposed approach on a synthetic task and a real problem of molecule identification.

</details>

---

### 66. [QFlowNet: Fast, Diverse, and Efficient Unitary Synthesis with Generative Flow Networks](https://arxiv.org/abs/2603.03045)

**基本信息**

- 🔗 arXiv: [`2603.03045`](https://arxiv.org/abs/2603.03045)
- 👥 作者: Inhoe Koo, Hyunho Cha, Jungwoo Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03045.pdf)

**💡 相关性分析**

满足标准3：论文研究量子线路合成，这是实现量子化学计算和量子机器学习的基础技术。虽然不直接属于给定主题，但作为可能加速“化学大模型”或“质谱结构推理”的潜在量子计算工具，其进展和范式（GFlowNet+Transformer）对于相关领域的跨学科讨论具有前瞻性意义。

**📖 中文摘要**

本文提出了QFlowNet，一个用于量子线路合成（将酉矩阵分解为量子门序列）的新框架。该框架将生成流网络（GFlowNet）与Transformer结合，以高效地从稀疏奖励信号中学习，并生成多样化的解决方案。Transformer作为强大的编码器，捕获酉矩阵的非局部结构。QFlowNet在3量子比特基准测试上实现了99.7%的成功率，并发现了一系列紧凑的电路。这项工作属于量子计算中的编译和优化问题。虽然不直接处理化学或质谱数据，但“量子线路合成”是量子化学模拟和量子机器学习（可能用于加速化学或质谱相关计算）的关键底层技术。高效的酉合成对于在量子计算机上实现化学模拟算法至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unitary Synthesis, the decomposition of a unitary matrix into a sequence of quantum gates, is a fundamental challenge in quantum compilation. Prevailing reinforcement learning (RL) approaches are often hampered by sparse reward signals, which necessitate complex reward shaping or long training times, and typically converge to a single policy, lacking solution diversity. In this work, we propose QFlowNet, a novel framework that learns efficiently from sparse signals by pairing a Generative Flow Network (GFlowNet) with Transformers. Our approach addresses two key challenges. First, the GFlowNet framework is fundamentally designed to learn a diverse policy that samples solutions proportional to their reward, overcoming the single-solution limitation of RL while offering faster inference than other generative models like diffusion. Second, the Transformers act as a powerful encoder, capturing the non-local structure of unitary matrices and compressing a high-dimensional state into a dense latent representation for the policy network. Our agent achieves an overall success rate of 99.7% on a 3-qubit benchmark(lengths 1-12) and discovers a diverse set of compact circuits, establishing QFlowNet as an efficient and diverse paradigm for unitary synthesis.

</details>

---

## 📊 数据统计
- 累计运行天数：12
- 累计论文数量：831

## 📝 历史记录

> 暂无历史数据

