# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-23 12:48:06

## 📅 2026-03-23 (今日最新)

**相关论文数：42**

### 1. [Engineering-Oriented Symbolic Regression: LLMs as Physics Agents for Discovery of Simulation-Ready Constitutive Laws](https://arxiv.org/abs/2603.19241)

**基本信息**

- 🔗 arXiv: [`2603.19241`](https://arxiv.org/abs/2603.19241)
- 👥 作者: Yue Wu, Tianhao Su, Mingchuan Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19241.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（LLMs）作为物理信息代理来发现材料的本构定律，这直接围绕‘化学大模型’这一主题，展示了LLMs在化学/材料科学建模中的应用。

**📖 中文摘要**

本文提出了一种面向工程的符号回归（EO-SR）框架，利用大型语言模型（LLMs）作为“物理信息代理”来发现复杂材料的本构定律。该框架的核心是让LLM代理零样本合成可执行的物理约束（如热力学一致性和框架无差异性），从而将搜索过程从数学曲线拟合转变为受物理规律支配的发现引擎。研究以橡胶类材料的超弹性建模为例进行验证，框架自主发现了一种新颖的混合本构定律。这项工作展示了LLMs在物理定律发现和科学建模中的应用，属于利用大模型（化学大模型）解决复杂科学问题（如材料建模）的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The discovery of constitutive laws for complex materials has historically faced a dichotomy between high-fidelity data-driven approaches, which demand prohibitive full-field experimental data, and traditional engineering fitting, which often yields numerically unstable models outside calibration regimes. In this work, we propose an Engineering-Oriented Symbolic Regression (EO-SR) framework that bridges this gap by leveraging Large Language Models (LLMs) as "Physics-Informed Agents." Unlike unconstrained symbolic regression, our framework utilizes an LLM Agent to zero-shot synthesize executable physical constraints -- specifically thermodynamic consistency and frame indifference -- transforming the search process from mathematical curve-fitting into a physics-governed discovery engine. We validate this approach on the hyperelastic modeling of rubber-like materials using standard Treloar datasets. The framework autonomously identifies a novel hybrid constitutive law that combines a Mooney-Rivlin linear base with a rational locking term. This discovered model not only achieves high predictive accuracy across multi-axial deformation modes (including zero-shot prediction of pure shear) but also guarantees unconditional convexity. Finite element validation demonstrates that while industry-standard models (e.g., Ogden N=3) fail due to numerical singularities under severe transverse compression, the EO-SR-discovered model maintains robust convergence. This study establishes a generalized, low-barrier pathway for discovering simulation-ready constitutive closures that satisfy both data accuracy and rigorous physical laws.

</details>

---

### 2. [Full-Stack Domain Enhancement for Combustion LLMs: Construction and Optimization](https://arxiv.org/abs/2603.19268)

**基本信息**

- 🔗 arXiv: [`2603.19268`](https://arxiv.org/abs/2603.19268)
- 👥 作者: Quanjia Xiao, Weimin Ouyang, Zonglin Yang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19268.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是针对燃烧科学领域构建和优化领域特定的大语言模型（LLM），这直接属于‘化学大模型’在专业科学领域（化学/燃烧学）的应用主题。

**📖 中文摘要**

本文针对燃烧科学这一复杂物理系统，提出了首个全栈式领域增强大语言模型（LLM）工作流程。该流程集成了自动化领域语料库构建、增量预训练、指令微调和基于可验证奖励的强化学习，旨在确保模型真正内化物理定律，而非仅仅学习文本统计模式。同时，本文发布了专为燃烧科学复杂推理任务设计的标准化评估基准FlameBench。实验结果表明，该工作开发的模型在燃烧科学推理任务上显著优于最先进的通用闭源模型和传统的检索增强生成方法。这项工作为开发具有可靠科学推理能力的领域特定科研智能体奠定了技术和资源基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) in the direction of task adaptation and capability enhancement for professional fields demonstrate significant application potential. Nevertheless, for complex physical systems such as combustion science, general-purpose LLMs often generate severe hallucinations due to insufficient domain knowledge and the inability to adhere to physical conservation laws. To address this issue, we propose the first full-stack domain-enhanced LLM workflow tailored for the field of combustion science, which integrates automated domain corpus construction, incremental pre-training, instruction fine-tuning, and verifiable reward-based reinforcement learning. This workflow ensures that the model truly internalizes physical laws rather than merely learning textual statistical patterns. We also release FlameBench, a standardized evaluation benchmark specifically designed for complex reasoning tasks in combustion science. Experimental results demonstrate that the model developed in this work significantly outperforms state-of-the-art general-purpose closed-source models and traditional retrieval-augmented generation methods on combustion science reasoning tasks. This work lays a solid technical and resource foundation for the subsequent development of domain-specific scientific research agents with reliable scientific reasoning capabilities.

</details>

---

### 3. [From Tokens To Agents: A Researcher's Guide To Understanding Large Language Models](https://arxiv.org/abs/2603.19269)

**基本信息**

- 🔗 arXiv: [`2603.19269`](https://arxiv.org/abs/2603.19269)
- 👥 作者: Daniele Barolo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19269.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于如何理解和使用大型语言模型（LLMs）的综述/指南性文章，其中包含了对LLM核心组件（包括智能体能力）的重要讨论，与‘化学大模型’（作为大模型的一个应用领域）的主题相关，提供了理解大模型的基础框架。

**📖 中文摘要**

本文是一篇指导性章节，旨在帮助研究人员理解大型语言模型（LLMs）的机制，以便决定如何在研究中使用它们。文章将LLMs分解为六个基本组成部分进行分析：预训练数据、分词与嵌入、Transformer架构、概率生成、对齐和智能体能力。每个部分都从技术基础和科研影响两方面进行分析，识别了具体的可供性和局限性。文章并未提供规定性指导，而是建立了一个框架，用于批判性地推理LLMs是否以及如何满足特定的研究需求，并通过一个使用基于LLM的智能体模拟社交媒体动态的扩展案例研究进行说明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Researchers face a critical choice: how to use -- or not use -- large language models in their work. Using them well requires understanding the mechanisms that shape what LLMs can and cannot do. This chapter makes LLMs comprehensible without requiring technical expertise, breaking down six essential components: pre-training data, tokenization and embeddings, transformer architecture, probabilistic generation, alignment, and agentic capabilities. Each component is analyzed through both technical foundations and research implications, identifying specific affordances and limitations. Rather than prescriptive guidance, the chapter develops a framework for reasoning critically about whether and how LLMs fit specific research needs, finally illustrated through an extended case study on simulating social media dynamics with LLM-based agents.

</details>

---

### 4. [A Human-Centered Workflow for Using Large Language Models in Content Analysis](https://arxiv.org/abs/2603.19271)

**基本信息**

- 🔗 arXiv: [`2603.19271`](https://arxiv.org/abs/2603.19271)
- 👥 作者: Ivan Zupic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19271.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于在内容分析中系统化使用大型语言模型（LLMs）的方法论综述和实用指南。虽然不专门针对化学，但其提供的框架、验证方法和最佳实践对于在化学信息学等领域应用LLMs（即构建或使用化学大模型）具有重要的参考和指导价值。

**📖 中文摘要**

本文提出了一个以人为中心的工作流程，用于在内容分析任务中使用大型语言模型（LLMs）。该工作流程将LLMs概念化为通用文本处理机器，并详细阐述了在三种定性和定量内容分析任务（标注、摘要和信息提取）中应用LLMs的步骤。该流程强调研究人员在设计、监督和验证LLM过程的每个阶段中的作用，以确保严谨性和透明度。文章综合了来自政治学、社会学、计算机科学、心理学和管理学等多个学科的广泛方法论文献的见解，概述了验证程序和最佳实践，以解决LLMs的黑箱性质、提示敏感性和幻觉倾向等关键限制。为便于实际实施，还提供了补充材料，包括提示库和Jupyter Notebook格式的Python代码及详细使用说明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While many researchers use Large Language Models (LLMs) through chat-based access, their real potential lies in leveraging LLMs via application programming interfaces (APIs). This paper conceptualizes LLMs as universal text processing machines and presents a comprehensive workflow for employing LLMs in three qualitative and quantitative content analysis tasks: (1) annotation (an umbrella term for qualitative coding, labeling and text classification), (2) summarization, and (3) information extraction. The workflow is explicitly human-centered. Researchers design, supervise, and validate each stage of the LLM process to ensure rigor and transparency. Our approach synthesizes insights from extensive methodological literature across multiple disciplines: political science, sociology, computer science, psychology, and management. We outline validation procedures and best practices to address key limitations of LLMs, such as their black-box nature, prompt sensitivity, and tendency to hallucinate. To facilitate practical implementation, we provide supplementary materials, including a prompt library and Python code in Jupyter Notebook format, accompanied by detailed usage instructions.

</details>

---

### 5. [Improving Automatic Summarization of Radiology Reports through Mid-Training of Large Language Models](https://arxiv.org/abs/2603.19275)

**基本信息**

- 🔗 arXiv: [`2603.19275`](https://arxiv.org/abs/2603.19275)
- 👥 作者: Mengxian Lyu, Cheng Peng, Ziyi Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19275.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对特定科学领域（放射学/医学）优化大语言模型（LLMs）的性能，通过引入中期训练进行子领域适应。这属于领域特定大模型（可类比化学大模型）的构建和优化方法研究。

**📖 中文摘要**

本文研究了通过大语言模型（LLMs）的中期训练（mid-training）方法来改进放射学报告的自动摘要生成。传统的“预训练-微调”策略被广泛用于使LLMs适应摘要任务。本研究提出了通过子领域适应（即放射学领域）的中期训练方法。文章探索了三种适应策略，并利用佛罗里达大学（UF）健康中心的大规模临床文本开发模型，在OpenI和MIMIC-CXR等广泛使用的基准数据集上进行了中期训练和微调实验。实验结果表明，经过中期训练的模型GatorTronT5-Radio取得了最佳性能，在文本度量（ROUGE-L）和事实性度量（RadGraph-F1）上均优于未经中期训练的模型。研究支持使用“预训练-中期训练-微调”策略来替代广泛使用的直接微调策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automatic summarization of radiology reports is an essential application to reduce the burden on physicians. Previous studies have widely used the "pre-training, fine-tuning" strategy to adapt large language models (LLMs) for summarization. This study proposed a subdomain adaptation through a mid-training method to improve summarization. We explored three adaptation strategies: (1) general-domain pre-training, (2) clinical-domain pre-training, and (3) clinical-domain pre-training followed by subdomain mid-training. We developed models using large-scale clinical text from the University of Florida (UF) Health and conducted mid-training and fine-tuning experiments using widely used benchmark datasets including OpenI and MIMIC-CXR. The experimental results show that the mid-trained model, GatorTronT5-Radio, achieved the best performance, outperforming models without mid-training in both text-based measures (ROUGE-L) and factuality measures (RadGraph-F1). Our mid-training methods also demonstrate better few-shot learning and could alleviate the "cold start" problem reported in previous studies as a learning barrier. Our findings support the use of "pre-training, mid-training, fine-tuning," instead of the widely used direct fine-tuning strategy.

</details>

---

### 6. [HypeLoRA: Hyper-Network-Generated LoRA Adapters for Calibrated Language Model Fine-Tuning](https://arxiv.org/abs/2603.19278)

**基本信息**

- 🔗 arXiv: [`2603.19278`](https://arxiv.org/abs/2603.19278)
- 👥 作者: Bartosz Trojan, Filip Gębala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19278.pdf)

**💡 相关性分析**

满足标准2：论文提出并系统评估了HypeLoRA这一参数高效微调方法，该方法通过超网络生成LoRA适配器。虽然论文本身不直接提供化学数据集或工具，但其提出的模型微调方法和框架（LoRA变体）是构建和优化领域大模型（如化学大模型）的关键技术资源，可用于提升模型在特定任务上的校准和性能。

**📖 中文摘要**

本文研究了Transformer模型（特别是RoBERTa）在参数高效微调方法下的校准动态。研究评估了低秩适应（LoRA）和一种新颖的基于超网络的适应框架，并将其与全参数微调在GLUE基准上进行比较。结果表明，基于LoRA的适应在保持显著更高参数效率的同时， consistently achieves calibration parity with (and in specific tasks exceeds) full fine-tuning。研究进一步探索了一种动态方法，其中共享的超网络生成LoRA因子（A和B矩阵）以在层间引入结构耦合。该研究揭示了参数效率与概率可靠性之间的关系，将结构化的低秩更新定位为不确定性感知Transformer架构的可行基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern Transformer-based models frequently suffer from miscalibration, producing overconfident predictions that do not reflect true empirical frequencies. This work investigates the calibration dynamics of LoRA: Low-Rank Adaptation and a novel hyper-network-based adaptation framework as parameter-efficient alternatives to full fine-tuning for RoBERTa. Evaluating across the GLUE benchmark, we demonstrate that LoRA-based adaptation consistently achieves calibration parity with (and in specific tasks exceeds) full fine-tuning, while maintaining significantly higher parameter efficiency. We further explore a dynamic approach where a shared hyper-network generates LoRA factors (A and B matrices) to induce structural coupling across layers. This approach produced results similar to standard LoRA fine-tuning, even achieving better MCC on CoLA dataset. Our study also reveal a critical trade-off: constraining the adaptation space (e.g., freezing matrices A) acts as a powerful regularizer that enhances Expected Calibration Error (ECE), but necessitates a carefully balanced sacrifice in downstream task accuracy. To support future research, we provide a unified and reproducible implementation of contemporary calibration metrics, including ECE, MCE, and ACE. Our findings clarify the relationship between parameter efficiency and probabilistic reliability, positioning structured low-rank updates as a viable foundation for uncertainty-aware Transformer architectures. Code available at: this https URL

</details>

---

### 7. [From Feature-Based Models to Generative AI: Validity Evidence for Constructed Response Scoring](https://arxiv.org/abs/2603.19280)

**基本信息**

- 🔗 arXiv: [`2603.19280`](https://arxiv.org/abs/2603.19280)
- 👥 作者: Jodi M. Casabianca, Daniel F. McCaffrey, Matthew S. Johnson 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19280.pdf)

**💡 相关性分析**

满足标准3：论文是一篇讨论生成式人工智能（包括大语言模型）在评估领域应用的方法论和有效性验证的综述性文章。虽然主题是教育评估，但其关于生成式AI模型评估、验证和解释的深入讨论，对于在化学信息学等领域评估和验证“化学大模型”的输出质量和可靠性具有重要的参考价值。

**📖 中文摘要**

本文讨论了在大规模高风险测试环境中应用生成式人工智能（AI）对建构反应进行评分的趋势。文章重点比较了基于特征的AI评分引擎与生成式AI在评分系统中的差异，并提出了一套最佳实践，用于收集有效性证据以支持使用和解释由生成式AI评分系统得出的建构反应分数。文章使用来自6-12年级学生的大量独立议论文语料库的建构反应分数数据，演示了为不同类型的评分系统收集有效性证据的过程，并强调了在为这些分数进行有效性论证时的众多复杂性和考虑因素。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid advancements in large language models and generative artificial intelligence (AI) capabilities are making their broad application in the high-stakes testing context more likely. Use of generative AI in the scoring of constructed responses is particularly appealing because it reduces the effort required for handcrafting features in traditional AI scoring and might even outperform those methods. The purpose of this paper is to highlight the differences in the feature-based and generative AI applications in constructed response scoring systems and propose a set of best practices for the collection of validity evidence to support the use and interpretation of constructed response scores from scoring systems using generative AI. We compare the validity evidence needed in scoring systems using human ratings, feature-based natural language processing AI scoring engines, and generative AI. The evidence needed in the generative AI context is more extensive than in the feature-based scoring context because of the lack of transparency and other concerns unique to generative AI such as consistency. Constructed response score data from a large corpus of independent argumentative essays written by 6-12th grade students demonstrate the collection of validity evidence for different types of scoring systems and highlight the numerous complexities and considerations when making a validity argument for these scores.

</details>

---

### 8. [Maximizing mutual information between user-contexts and responses improve LLM personalization with no additional data](https://arxiv.org/abs/2603.19294)

**基本信息**

- 🔗 arXiv: [`2603.19294`](https://arxiv.org/abs/2603.19294)
- 👥 作者: Hyunji Nam, Haoran Li, Natasha Jaques
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19294.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种名为MIPO的新颖的、无需额外标注数据的LLM自我改进框架。该方法通过对比数据增强和偏好优化来提升模型性能。虽然论文的评估涉及多个领域，但其提出的方法本身是一种通用的模型优化工具/技术，可直接应用于优化“化学大模型”在特定任务（如质谱结构推理）上的表现。

**📖 中文摘要**

本文提出了互信息偏好优化（MIPO），一种对比数据增强方法，用于在没有外部监督的情况下实现大语言模型（LLMs）的自我改进。MIPO通过生成基于正确提示的正向响应和基于随机无关提示的负向响应来构建偏好对。研究表明，使用直接偏好优化（DPO）从这种配对数据中学习，可以最大化提示与模型响应之间的点态条件互信息。在各种规模的Llama和Qwen指令模型上的实证结果表明，当用于最大化用户上下文和响应之间的互信息时，MIPO提供了一种有效的个性化技术。令人惊讶的是，MIPO也可以应用于改进数学和多项选择题的性能，且无需任何额外数据或人工监督。这些结果表明了一个有前景的自我改进方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While post-training has successfully improved large language models (LLMs) across a variety of domains, these gains heavily rely on human-labeled data or external verifiers. Existing data has already been exploited, and new high-quality data is expensive to collect. More fundamentally, true intelligence goes far beyond tasks that are easily verifiable. Therefore, we need self-improvement frameworks that allow models to improve without external oversight. We propose *Mutual Information Preference Optimization (MIPO)*, a contrastive data augmentation method that constructs preference pairs by generating a positive response conditioning on the correct prompt, and a negative response by conditioning on a random, unrelated prompt. We show that using Direct Preference Optimization (DPO) to learn from this paired data maximizes pointwise conditional mutual information (MI) (under the base LLM) between prompts and model responses. Empirical results with various-sized Llama- and Qwen-Instruct models show that when used to maximize MI between user context and response, MIPO provides an effective personalization technique, achieving 3-40% improvements on personalization tasks using real-user datasets compared to strong baselines. Surprisingly, MIPO can also be applied to improve performance on math and multiple-choice problems, yielding 1-18% **without any additional data or human supervision**. These results suggest a promising direction for self-improvement.

</details>

---

### 9. [TTQ: Activation-Aware Test-Time Quantization to Accelerate LLM Inference On The Fly](https://arxiv.org/abs/2603.19296)

**基本信息**

- 🔗 arXiv: [`2603.19296`](https://arxiv.org/abs/2603.19296)
- 👥 作者: Toshiaki Koike-Akino, Jing Liu, Ye Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19296.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种名为TTQ的测试时量化框架，这是一种用于加速大语言模型（LLMs）推理的模型压缩工具/技术。该技术对于部署和优化计算密集型的大模型（如化学大模型）具有实用价值，可以降低其推理成本和提高效率。

**📖 中文摘要**

本文提出了测试时量化（TTQ）框架，旨在解决大模型激活感知压缩技术因依赖校准数据而可能产生的领域偏移问题。TTQ在推理时动态压缩大型模型，通过高效的在线校准，实现即时激活感知量化，从而适应不同的下游任务，同时获得推理加速。实验表明，TTQ可以超越最先进的基线方法，提升量化性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To tackle the huge computational demand of large foundation models, activation-aware compression techniques without retraining have been introduced. However, since these methods highly rely on calibration data, domain shift issues may arise for unseen downstream tasks. We propose a test-time quantization (TTQ) framework which compresses large models on the fly at inference time to resolve this issue. With an efficient online calibration, instant activation-aware quantization can adapt every prompt regardless of the downstream tasks, yet achieving inference speedup. Several experiments demonstrate that TTQ can improve the quantization performance over state-of-the-art baselines.

</details>

---

### 10. [Parameter-Efficient Token Embedding Editing for Clinical Class-Level Unlearning](https://arxiv.org/abs/2603.19302)

**基本信息**

- 🔗 arXiv: [`2603.19302`](https://arxiv.org/abs/2603.19302)
- 👥 作者: Iyad Ait Hou, Shrenik Borad, Harsh Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19302.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种针对大语言模型的参数高效遗忘方法STEU。该方法对于在化学信息学等领域管理大模型（如化学大模型）的知识更新、隐私保护或合规性调整（例如，需要从模型中移除某些敏感或错误数据关联）具有工具价值。

**📖 中文摘要**

本文针对临床语言模型中的机器遗忘问题，提出了稀疏词嵌入遗忘（STEU）方法，用于行为级别的类别遗忘。该方法仅更新由PMI选择的词嵌入以及一个小的分类器头部，同时保持所有编码器层冻结，从而实现参数高效的遗忘。在MIMIC-IV、MIMIC-III和eICU数据集上使用BioClinicalBERT、BERT-base和DistilBERT进行的实验表明，STEU能够持续抑制目标类别，同时在很大程度上保留剩余任务的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine unlearning is increasingly important for clinical language models, where privacy regulations and institutional policies may require removing sensitive information from deployed systems without retraining from scratch. In practice, deletion requests must balance effective forgetting of targeted information with preservation of model utility and minimal parameter modification. We introduce Sparse Token Embedding Unlearning (STEU), a parameter-efficient method for behavioral class-level unlearning that updates only PMI-selected token embeddings together with a small classifier head while keeping all encoder layers frozen. Across experiments on MIMIC-IV, MIMIC-III, and eICU using BioClinicalBERT, BERT-base, and DistilBERT, STEU consistently suppresses the target class while largely preserving retained task performance. In the primary MIMIC-IV setting, STEU achieves near-complete forgetting (forget F1 = 0.0004) while maintaining competitive retained utility (retain avg F1 = 0.4766) after modifying only 0.19\% of model parameters. These results suggest that targeted behavioral unlearning can be achieved through sparse embedding edits without modifying deeper encoder representations.

</details>

---

### 11. [Benchmarking Cross-Scale Perception Ability of Large Multimodal Models in Material Science](https://arxiv.org/abs/2603.19327)

**基本信息**

- 🔗 arXiv: [`2603.19327`](https://arxiv.org/abs/2603.19327)
- 👥 作者: Yuting Zheng, Zijian Chen, Qi Jia
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19327.pdf)

**💡 相关性分析**

满足标准2：论文提出了CSMBench，这是一个专门针对材料科学领域构建的、用于评估多模态大模型跨尺度感知能力的基准数据集。该数据集是评估和开发面向材料科学（属于化学相关领域）的大模型（化学大模型）的重要资源和工具。

**📖 中文摘要**

本文引入了CSMBench，一个用于评估大型多模态模型（LMMs）在材料科学中跨尺度感知能力的基准数据集。该数据集包含从顶级期刊中精心挑选的1,041张高质量图表，并严格按材料研究的定义分为四个科学上不同的尺度：原子、微观、介观和宏观尺度。通过开放式图表描述和多项选择标题匹配任务，评估了最先进的开源和闭源模型。分析发现，由于不同尺度的视觉特征差异，模型性能在不同物理尺度上存在显著差异，这凸显了当前通用模型的局限性，并为在材料研究中实现层次化和准确理解指明了关键方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Unraveling the hierarchical structure-property relationships is the central challenge of materials science, necessitating the interpretation of data across vast physical scales from micro to macro. Despite the rapid integration of Large Multimodal Models (LMMs) into scientific workflows, existing scientific benchmarks primarily focus on general chart interpretation or isolated common-sense reasoning, failing to capture reasoning ability across intricate physical dimensions. To address this, we introduce CSMBench, a dataset comprising 1,041 high-quality figures curated from premier journals up to September 2025. CSMBench categorizes data into four scientifically distinct regimes: atomic, micro, meso, and macro scales, strictly aligning with the focus and definitions in materials study. Through open-ended figure description and multiple-choice caption matching tasks, we evaluate state-of-the-art open-source and closed-source models. Our analysis identifies that performance varies significantly across physical scales due to the distinct visual characteristics, highlighting the limitations of current generalist models and identifying critical directions for achieving hierarchical and accurate understanding in materials research. The CSMBench is publicly released at: this https URL .

</details>

---

### 12. [Do Post-Training Algorithms Actually Differ? A Controlled Study Across Model Scales Uncovers Scale-Dependent Ranking Inversions](https://arxiv.org/abs/2603.19335)

**基本信息**

- 🔗 arXiv: [`2603.19335`](https://arxiv.org/abs/2603.19335)
- 👥 作者: Xiaoyi Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19335.pdf)

**💡 相关性分析**

满足标准2和3：论文通过大规模的对照实验，系统评估和比较了多种大语言模型（LLMs）后训练对齐算法（如DPO, SimPO等），并发布了统一的代码框架和基准。这既提供了用于优化大模型（包括化学大模型）的重要工具和基准数据，也包含了对不同算法性能的深入分析和讨论，具有综述和展望价值。

**📖 中文摘要**

本文通过统一的OXRL框架，对51种后训练对齐算法进行了首次大规模、控制变量的比较评估。研究涵盖了8种算法、4种模型规模（0.5B-7B）、3个评估领域以及一个包含20个变体的DPO分类法，总计约240次训练运行。主要发现包括：1）算法排名随模型规模变化而不稳定，存在完全的排名反转；2）损失函数修改带来的收益微乎其微；3）算法的影响力是任务特定的。这些发现为从业者提供了一个杠杆层次：模型规模 >> 训练范式 >> 在线与离线 >> 损失函数。作者发布了所有代码、配置和评估数据作为一个持续的社区基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Post-training alignment has produced dozens of competing algorithms -- DPO, SimPO, KTO, GRPO, and others -- yet practitioners lack controlled comparisons to guide algorithm selection. We present OXRL, a unified framework implementing 51 post-training algorithms with identical infrastructure, enabling the first large-scale apples-to-apples evaluation. Our study spans 8 algorithms across 4 model scales (0.5B--7B), 3 evaluation domains, and a 20-variant DPO taxonomy (100 runs at 1.5B, 5 seeds each), totaling $\sim$240 training runs on H100 GPUs. Three headline findings emerge. (1)~Algorithm rankings are unstable across scale: at 1.5B, online RL (SGRPO) tops all methods at 58.0\%~$\pm$0.57 on GSM8K; by 7B, the worst small-scale method (SimPO) becomes the best (85.8\%), a complete ranking inversion driven by model scale rather than LoRA regularization (confirmed via 2$\times$2 factorial). (2)~Loss function modifications yield negligible gains: none of 20 DPO variants significantly outperform vanilla DPO after Bonferroni correction; the sole significant outlier, SimPO, is worse ($-$11.5~pp, $p < 10^{-4}$). (3)~Algorithm leverage is task-specific: the 19.3~pp GSM8K spread collapses to 0.54~pp on MATH ($36\times$) and 0.47~pp on general-domain benchmarks ($41\times$), confirming that algorithm choice matters primarily within the training distribution. These findings yield a hierarchy of leverage for practitioners: model scale (${\sim}$50~pp) $\gg$ training paradigm (${\sim}$10~pp) $\gg$ online vs.\ offline (${\sim}$9~pp) $\gg$ loss function (${\sim}$1~pp). We release all code, configs, and evaluation data as a living community benchmark.

</details>

---

### 13. [DAPA: Distribution Aware Piecewise Activation Functions for On-Device Transformer Inference and Training](https://arxiv.org/abs/2603.19338)

**基本信息**

- 🔗 arXiv: [`2603.19338`](https://arxiv.org/abs/2603.19338)
- 👥 作者: Maoyang Xiang, Bo Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19338.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种名为DAPA的新型、硬件友好的激活函数，旨在优化Transformer模型在设备上的推理和训练效率。这是一种底层模型架构优化工具，对于部署和优化包括“化学大模型”在内的大规模Transformer模型具有实用价值。

**📖 中文摘要**

本文提出了分布感知分段激活函数（DAPA），一种针对Transformer架构的可微分且硬件友好的激活函数。DAPA利用预激活数据的分布，采用非均匀分段近似，将更精细的段分配给分布的高概率区域，从而改进了先前分段线性方法的泛化能力。所得的近似进一步使用分布加权均方误差进行量化，以减少硬件部署的延迟和资源利用率。硬件实现表明，DAPA将GELU计算速度提高了16倍，并将DSP利用率降低了16倍，同时在视觉Transformer和GPT-2模型上保持相当或更好的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Non-linear activation functions play a pivotal role in on-device inference and training, as they not only consume substantial hardware resources but also impose a significant impact on system performance and energy efficiency. In this work, we propose Distribution-Aware Piecewise Activation (DAPA), a differentiable and hardware-friendly activation function for Transformer architectures by exploiting the distribution of pre-activation data. DAPA employs a non-uniform piecewise approximation that allocates finer segments to high-probability regions of the distribution, improving generalizability over prior piecewise linear methods. The resulting approximation is further quantized using Distribution-Weighted Mean Square Error to reduce latency and resource utilization for hardware deployment. Our HLS implementation demonstrates that DAPA speeds up GELU computation by 16$\times$ and decreases DSP utilization by 16$\times$ while maintaining comparable or better performance across vision Transformers and GPT-2 models.

</details>

---

### 14. [Spectral Tempering for Embedding Compression in Dense Passage Retrieval](https://arxiv.org/abs/2603.19339)

**基本信息**

- 🔗 arXiv: [`2603.19339`](https://arxiv.org/abs/2603.19339)
- 👥 作者: Yongkang Li, Panagiotis Eustratiadis, Evangelos Kanoulas
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19339.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种名为SpecTemp的嵌入压缩方法，用于提升密集检索系统的效率和性能。虽然应用于通用检索，但其提出的谱分析和技术对于处理化学信息学中的大规模分子或光谱数据检索、构建高效的化学信息检索系统具有工具价值，可间接支持质谱结构推理等任务。

**📖 中文摘要**

本文针对密集检索系统中的嵌入压缩问题，提出了谱调温（SpecTemp）方法。该方法是一种无需学习的方法，通过局部信噪比分析和拐点归一化，直接从语料库特征谱中推导出自适应的缩放强度γ(k)，无需标注数据或基于验证的搜索。大量实验表明，SpecTemp相对于网格搜索的γ*(k) consistently achieves near-oracle performance，同时保持完全无需学习和模型无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dimensionality reduction is critical for deploying dense retrieval systems at scale, yet mainstream post-hoc methods face a fundamental trade-off: principal component analysis (PCA) preserves dominant variance but underutilizes representational capacity, while whitening enforces isotropy at the cost of amplifying noise in the heavy-tailed eigenspectrum of retrieval embeddings. Intermediate spectral scaling methods unify these extremes by reweighting dimensions with a power coefficient $\gamma$, but treat $\gamma$ as a fixed hyperparameter that requires task-specific tuning. We show that the optimal scaling strength $\gamma$ is not a global constant: it varies systematically with target dimensionality $k$ and is governed by the signal-to-noise ratio (SNR) of the retained subspace. Based on this insight, we propose Spectral Tempering (\textbf{SpecTemp}), a learning-free method that derives an adaptive $\gamma(k)$ directly from the corpus eigenspectrum using local SNR analysis and knee-point normalization, requiring no labeled data or validation-based search. Extensive experiments demonstrate that Spectral Tempering consistently achieves near-oracle performance relative to grid-searched $\gamma^*(k)$ while remaining fully learning-free and model-agnostic. Our code is publicly available at this https URL .

</details>

---

### 15. [Exploring the Agentic Frontier of Verilog Code Generation](https://arxiv.org/abs/2603.19347)

**基本信息**

- 🔗 arXiv: [`2603.19347`](https://arxiv.org/abs/2603.19347)
- 👥 作者: Patrick Yubeaton, Chinmay Hegde, Siddharth Garg
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19347.pdf)

**💡 相关性分析**

满足标准3：论文系统评估了智能体（Agent）框架在硬件描述语言代码生成任务中的应用，分析了不同架构和模型的性能。虽然领域是硬件设计，但其关于智能体框架设计、评估以及与LLMs结合的研究发现和讨论，对于探索如何构建用于“质谱结构推理”或“化学合成规划”等化学信息学任务的智能体系统具有重要的参考和展望价值。

**📖 中文摘要**

本文首次系统评估了智能体框架（Agentic Frameworks）在Verilog代码生成任务中的应用。研究使用CVDP基准，并引入了几个开源硬件设计智能体工具，为未来工作提供了模型无关的基线。通过跨前沿模型的对照实验，研究了结构化提示和工具设计如何影响性能，分析了智能体故障模式和工具使用模式，比较了开源和闭源模型，并提供了成功和失败智能体运行的定性示例。结果表明，朴素的智能体包装可能会降低性能，但结构化的工具能够有意义地匹配并在某些情况下超过非智能体基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have made rapid advancements in code generation for popular languages such as Python and C++. Many of these recent gains can be attributed to the use of ``agents'' that wrap domain-relevant tools alongside LLMs. Hardware design languages such as Verilog have also seen improved code generation in recent years, but the impact of agentic frameworks on Verilog code generation tasks remains unclear. In this work, we present the first systematic evaluation of agentic LLMs for Verilog generation, using the recently introduced CVDP benchmark. We also introduce several open-source hardware design agent harnesses, providing a model-agnostic baseline for future work. Through controlled experiments across frontier models, we study how structured prompting and tool design affect performance, analyze agent failure modes and tool usage patterns, compare open-source and closed-source models, and provide qualitative examples of successful and failed agent runs. Our results show that naive agentic wrapping around frontier models can degrade performance (relative to standard forward passes with optimized prompts), but that structured harnesses meaningfully match and in some cases exceed non-agentic baselines. We find that the performance gap between open and closed source models is driven by both higher crash rates and weaker tool output interpretation. Our exploration illuminates the path towards designing special-purpose agents for verilog generation in the future.

</details>

---

### 16. [A Mathematical Theory of Understanding](https://arxiv.org/abs/2603.19349)

**基本信息**

- 🔗 arXiv: [`2603.19349`](https://arxiv.org/abs/2603.19349)
- 👥 作者: Bahar Taşkesen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19349.pdf)

**💡 相关性分析**

满足标准3：论文提出了一种关于学习和理解的抽象数学模型，从信息论和认知结构的角度形式化了教学与学习的过程。虽然不直接针对化学或质谱，但其理论框架对于理解和设计用于复杂科学推理（如质谱结构推理）的大模型或智能体系统具有深层的理论指导意义，属于相关的方法论讨论。

**📖 中文摘要**

本文提出了一个关于“理解”的数学模型，将学习者抽象为一个具有概念先决结构的心智（Mind）。教学被建模为与潜在目标的顺序通信。由于教学信号只有在学习者掌握了解析它们所需的先决条件时才可用，因此有效通信信道取决于学习者当前的知识状态，并随着学习的进展而变得更加信息丰富。该模型产生了学习速度的两个限制：由先决条件可达性决定的结构性限制和由目标不确定性决定的认识性限制。该框架暗示了训练和能力获取中的阈值效应。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative AI has transformed the economics of information production, making explanations, proofs, examples, and analyses available at very low cost. Yet the value of information still depends on whether downstream users can absorb and act on it. A signal conveys meaning only to a learner with the structural capacity to decode it: an explanation that clarifies a concept for one user may be indistinguishable from noise to another who lacks the relevant prerequisites. This paper develops a mathematical model of that learner-side bottleneck. We model the learner as a mind, an abstract learning system characterized by a prerequisite structure over concepts. A mind may represent a human learner, an artificial learner such as a neural network, or any agent whose ability to interpret signals depends on previously acquired concepts. Teaching is modeled as sequential communication with a latent target. Because instructional signals are usable only when the learner has acquired the prerequisites needed to parse them, the effective communication channel depends on the learner's current state of knowledge and becomes more informative as learning progresses. The model yields two limits on the speed of learning and adoption: a structural limit determined by prerequisite reachability and an epistemic limit determined by uncertainty about the target. The framework implies threshold effects in training and capability acquisition. When the teaching horizon lies below the prerequisite depth of the target, additional instruction cannot produce successful completion of teaching; once that depth is reached, completion becomes feasible. Across heterogeneous learners, a common broadcast curriculum can be slower than personalized instruction by a factor linear in the number of learner types.

</details>

---

### 17. [Warm-Start Flow Matching for Guaranteed Fast Text/Image Generation](https://arxiv.org/abs/2603.19360)

**基本信息**

- 🔗 arXiv: [`2603.19360`](https://arxiv.org/abs/2603.19360)
- 👥 作者: Minyoung Kim
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19360.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种名为WS-FM（热启动流匹配）的生成模型加速框架。该技术通过结合轻量级生成模型来显著加速高质量样本的生成过程。虽然论文演示了文本和图像生成，但其核心加速方法是一种通用的生成模型优化工具，可应用于加速与“化学大模型”或“质谱结构推理”相关的生成任务，例如分子生成或质谱解析。

**📖 中文摘要**

本文提出了一种新颖的解决方案，通过有保证的加速因子来减少流匹配（Flow Matching, FM）算法的样本生成时间，而不牺牲生成样本的质量。核心思想是利用计算量轻的生成模型（其生成时间与目标FM模型相比可忽略不计）来生成草稿样本，并将这些质量尚可但生成快速的草稿样本作为FM算法的初始分布。与从纯噪声初始分布开始的传统FM不同，草稿样本已经具有不错的品质，因此我们可以将起始时间设置为更接近结束时间，从而显著减少达到目标数据分布所需的时间步数，且加速因子是有保证的。该方法被称为“热启动FM”（WS-FM），本质上可被视为一种从低质量草稿样本到高质量样本的“学习-精炼”生成模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current auto-regressive (AR) LLMs, diffusion-based text/image generative models, and recent flow matching (FM) algorithms are capable of generating premium quality text/image samples. However, the inference or sample generation in these models is often very time-consuming and computationally demanding, mainly due to large numbers of function evaluations corresponding to the lengths of tokens or the numbers of diffusion steps. This also necessitates heavy GPU resources, time, and electricity. In this work we propose a novel solution to reduce the sample generation time of flow matching algorithms by a guaranteed speed-up factor, without sacrificing the quality of the generated samples. Our key idea is to utilize computationally lightweight generative models whose generation time is negligible compared to that of the target AR/FM models. The draft samples from a lightweight model, whose quality is not satisfactory but fast to generate, are regarded as an initial distribution for a FM algorithm. Unlike conventional usage of FM that takes a pure noise (e.g., Gaussian or uniform) initial distribution, the draft samples are already of decent quality, so we can set the starting time to be closer to the end time rather than 0 in the pure noise FM case. This will significantly reduce the number of time steps to reach the target data distribution, and the speed-up factor is guaranteed. Our idea, dubbed {\em Warm-Start FM} or WS-FM, can essentially be seen as a {\em learning-to-refine} generative model from low-quality draft samples to high-quality samples. As a proof of concept, we demonstrate the idea on some synthetic toy data as well as real-world text and image generation tasks, illustrating that our idea offers guaranteed speed-up in sample generation without sacrificing the quality of the generated samples.

</details>

---

### 18. [CO-EVOLVE: Bidirectional Co-Evolution of Graph Structure and Semantics for Heterophilous Learning](https://arxiv.org/abs/2603.19596)

**基本信息**

- 🔗 arXiv: [`2603.19596`](https://arxiv.org/abs/2603.19596)
- 👥 作者: Jinming Xing, Muhammad Shahzad
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19596.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大语言模型（LLMs）与图神经网络（GNNs）的集成与协同演化，这是构建能够处理复杂结构化数据（如分子）的“化学大模型”的关键技术路径。

**📖 中文摘要**

这篇论文提出了CO-EVOLVE框架，旨在解决大语言模型（LLMs）和图神经网络（GNNs）集成中的核心挑战。它通过双向协同演化机制，将图拓扑和语义嵌入视为动态的、相互增强的潜在变量。该框架采用Gauss-Seidel交替优化策略，建立了一个循环反馈回路：GNN将结构上下文作为软提示注入以指导LLM，而LLM则构建有利的动态语义图来重新连接GNN。论文引入了三项关键创新来稳定这种演化过程。这项工作直接关联到“化学大模型”主题，因为它探索了LLMs与结构化数据模型（如GNNs）的深度集成与协同优化，这是构建能够理解复杂化学结构（如分子图）和语义（如化学文本描述）的化学大模型的核心研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) and Graph Neural Networks (GNNs) promises to unify semantic understanding with structural reasoning, yet existing methods typically rely on static, unidirectional pipelines. These approaches suffer from fundamental limitations: (1) Bidirectional Error Propagation, where semantic hallucinations in LLMs or structural noise in GNNs permanently poison the downstream modality without opportunity for recourse; (2) Semantic-Structural Dissonance, particularly in heterophilous settings where textual similarity contradicts topological reality; (3) a Blind Leading the Blind phenomenon, where indiscriminate alignment forces models to mirror each other's mistakes regardless of uncertainty. To address these challenges, we propose CO-EVOLVE, a dual-view co-evolution framework that treats graph topology and semantic embeddings as dynamic, mutually reinforcing latent variables. By employing a Gauss-Seidel alternating optimization strategy, our framework establishes a cyclic feedback loop: the GNN injects structural context as Soft Prompts to guide the LLM, while the LLM constructs favorable Dynamic Semantic Graphs to rewire the GNN. We introduce three key innovations to stabilize this evolution: (1) a Hard-Structure Conflict-Aware Contrastive Loss that warps the semantic manifold to respect high-order topological boundaries; (2) an Adaptive Node Gating Mechanism that dynamically fuses static and learnable structures to recover missing links; (3) an Uncertainty-Gated Consistency strategy that enables meta-cognitive alignment, ensuring models only learn from the confident view. Finally, an Entropy-Aware Adaptive Fusion integrates predictions during inference. Extensive experiments on public benchmarks demonstrate that CO-EVOLVE significantly outperforms state-of-the-art baselines, achieving average improvements of 9.07% in Accuracy and 7.19% in F1-score.

</details>

---

### 19. [RiboSphere: Learning Unified and Efficient Representations of RNA Structures](https://arxiv.org/abs/2603.19636)

**基本信息**

- 🔗 arXiv: [`2603.19636`](https://arxiv.org/abs/2603.19636)
- 👥 作者: Zhou Zhang, Hanqun Cao, Cheng Tan 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19636.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于RNA三维结构建模和生成的深度学习框架。这直接关系到“质谱结构推理”主题，因为从质谱数据推断未知化合物的三维结构是化学信息学和质谱分析领域的核心挑战之一，该论文提供了一种先进的、基于学习的结构生成与表示方法。

**📖 中文摘要**

这篇论文提出了RiboSphere框架，用于学习RNA结构的统一且高效的离散几何表示。该框架结合了向量量化和流匹配技术，其设计灵感来源于RNA架构的模块化组织特性。RiboSphere使用一个几何Transformer编码器来生成SE(3)不变的特征，然后通过有限标量化（FSQ）将这些特征离散化为有限的潜在代码词汇表。以这些离散代码为条件，一个流匹配解码器可以重建原子坐标，从而实现高保真度的结构生成。研究发现，学习到的代码索引富含特定的RNA基序信息，表明模型捕获了基序级别的组合结构。该框架在结构重建、逆折叠和RNA-配体结合预测等任务上表现出色。这项工作与“质谱结构推理”高度相关，因为它提供了一种从离散表示生成和推理生物大分子（如RNA）三维结构的新方法。在质谱分析中，从谱图数据推断未知化合物的结构是一个核心挑战，RiboSphere所展示的从潜在表示生成精确3D结构的能力，为开发基于学习的质谱结构推理模型提供了重要的方法论参考和潜在的技术组件。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate RNA structure modeling remains difficult because RNA backbones are highly flexible, non-canonical interactions are prevalent, and experimentally determined 3D structures are comparatively scarce. We introduce \emph{RiboSphere}, a framework that learns \emph{discrete} geometric representations of RNA by combining vector quantization with flow matching. Our design is motivated by the modular organization of RNA architecture: complex folds are composed from recurring structural motifs. RiboSphere uses a geometric transformer encoder to produce SE(3)-invariant (rotation/translation-invariant) features, which are discretized with finite scalar quantization (FSQ) into a finite vocabulary of latent codes. Conditioned on these discrete codes, a flow-matching decoder reconstructs atomic coordinates, enabling high-fidelity structure generation. We find that the learned code indices are enriched for specific RNA motifs, suggesting that the model captures motif-level compositional structure rather than acting as a purely compressive bottleneck. Across benchmarks, RiboSphere achieves strong performance in structure reconstruction (RMSD 1.25\,Å, TM-score 0.84), and its pretrained discrete representations transfer effectively to inverse folding and RNA--ligand binding prediction, with robust generalization in data-scarce regimes.

</details>

---

### 20. [From Token to Item: Enhancing Large Language Models for Recommendation via Item-aware Attention Mechanism](https://arxiv.org/abs/2603.19693)

**基本信息**

- 🔗 arXiv: [`2603.19693`](https://arxiv.org/abs/2603.19693)
- 👥 作者: Xiaokun Zhang, Bowei He, Jiamin Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19693.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大语言模型（LLMs）以更好地处理结构化项目（物品）及其关系，通过引入物品感知注意力机制。这项技术可以迁移到化学领域，用于构建能够理解分子内和分子间关系的“化学大模型”，例如用于分子表示学习、性质预测和反应推理。

**📖 中文摘要**

这篇论文研究了基于大语言模型（LLMs）的推荐系统。现有方法通常将物品表示为令牌序列，并应用注意力层来生成推荐。然而，这种标准的注意力机制侧重于建模令牌级关系，忽略了物品作为推荐基本单元的特性，从而无法有效捕获物品级别的协同关系。为此，作者提出了一个带有物品感知注意力机制（IAM）的新框架来增强LLMs的推荐能力。IAM设计了两个互补的注意力层：1）物品内注意力层，将注意力限制在同一物品内的令牌上，以建模物品内容语义；2）物品间注意力层，专门关注跨物品的令牌关系，以捕获物品协同关系。通过这种堆叠设计，IAM明确强调了物品作为推荐基本单元的重要性，使LLMs能够有效利用物品级别的协同关系。这项研究与“化学大模型”主题相关，因为它探索了如何让大语言模型更好地理解和处理结构化项目（在化学背景下可以是分子、化合物）及其之间的关系。将类似的物品感知机制应用于化学领域，可以帮助构建能够理解分子内原子间相互作用（物品内）和分子间相似性或反应性（物品间）的化学大模型，从而用于分子性质预测、反应结果推理等任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have recently gained increasing attention in the field of recommendation. Existing LLM-based methods typically represent items as token sequences, and apply attention layers on these tokens to generate recommendations. However, by inheriting the standard attention mechanism, these methods focus on modeling token-level relations. This token-centric focus overlooks the item as the fundamental unit of recommendation, preventing existing methods from effectively capturing collaborative relations at the item level. In this work, we revisit the role of tokens in LLM-driven recommendation and categorize their relations into two types: (1) intra-item token relations, which present the content semantics of an item, e.g., name, color, and size; and (2) inter-item token relations, which encode collaborative relations across items. Building on these insights, we propose a novel framework with an item-aware attention mechanism (IAM) to enhance LLMs for recommendation. Specifically, IAM devises two complementary attention layers: (1) an intra-item attention layer, which restricts attention to tokens within the same item, modeling item content semantics; and (2) an inter-item attention layer, which attends exclusively to token relations across items, capturing item collaborative relations. Through this stacked design, IAM explicitly emphasizes items as the fundamental units in recommendation, enabling LLMs to effectively exploit item-level collaborative relations. Extensive experiments on several public datasets demonstrate the effectiveness of IAM in enhancing LLMs for personalized recommendation.

</details>

---

### 21. [Adapting a Pre-trained Single-Cell Foundation Model to Spatial Gene Expression Generation from Histology Images](https://arxiv.org/abs/2603.19766)

**基本信息**

- 🔗 arXiv: [`2603.19766`](https://arxiv.org/abs/2603.19766)
- 👥 作者: Donghai Fang, Yongheng Li, Zhen Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19766.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何适配和利用预训练的单细胞基础模型（一种特定领域的化学/生物大模型）进行条件生成任务，直接涉及“化学大模型”主题。

**📖 中文摘要**

这篇论文提出了一种名为HINGE的方法，用于从组织学图像生成空间基因表达。其核心创新在于将预训练的单细胞基础模型（sc-FM）改造为条件表达生成器。单细胞基础模型（sc-FM）是本文关注主题“化学大模型”在生物医学领域（单细胞组学）的一个具体实例。该模型通过预训练捕获了关键的基因-基因关系，这些关系是仅从组织学图像中无法揭示的。HINGE方法通过引入轻量级的SoftAdaLN调制机制，将视觉上下文注入到模型骨干中，同时保留了预训练模型学到的基因关系。这项工作展示了如何将预训练的基础模型（大模型）适配到新的条件生成任务中，与“化学大模型”的主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Spatial transcriptomics (ST) enables spot-level in situ expression profiling, but its high cost and limited throughput motivate predicting expression directly from HE-stained histology. Recent advances explore using score- or flow-based generative models to estimate the conditional distribution of gene expression from histology, offering a flexible alternative to deterministic regression approaches. However, most existing generative approaches omit explicit modeling of gene-gene dependencies, undermining biological coherence. Single-cell foundation models (sc-FMs), pre-trained across diverse cell populations, capture these critical gene relationships that histology alone cannot reveal. Yet, applying expression-only sc-FMs to histology-conditioned expression modeling is nontrivial due to the absence of a visual pathway, a mismatch between their pre-training and conditional ST objectives, and the scarcity of mixed-cell ST supervision. To address these challenges, we propose HINGE (HIstology-coNditioned GEneration), which retrofits a pre-trained sc-FM into a conditional expression generator while mostly preserving its learned gene relationships. We achieve this by introducing SoftAdaLN, a lightweight, identity-initialized modulation that injects layer-wise visual context into the backbone, coupled with an expression-space masked diffusion objective and a warm-start curriculum to ensure objective alignment and training stability. Evaluated on three ST datasets, ours outperforms state-of-the-art baselines on mean Pearson correlation and yields more accurate spatial marker expression patterns and higher pairwise co-expression consistency, establishing a practical route to adapt pre-trained sc-FMs for histology-conditioned spatial expression generation.

</details>

---

### 22. [Embodied Science: Closing the Discovery Loop with Agentic Embodied AI](https://arxiv.org/abs/2603.19782)

**基本信息**

- 🔗 arXiv: [`2603.19782`](https://arxiv.org/abs/2603.19782)
- 👥 作者: Xiang Zhuang, Chenyi Zhou, Kehua Feng 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19782.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容（具身科学范式）直接围绕如何将AI（包括大模型）与物理实验闭环结合进行科学发现，这与利用“化学大模型”进行探索和“推理”的主题高度相关。同时，论文提出了一个前瞻性的框架和路线图，属于重要的相关讨论和展望。

**📖 中文摘要**

这篇论文提出了“具身科学”的新范式，主张将科学发现重新定义为智能体推理与物理执行紧密耦合的闭环过程。论文提出了统一的感知-语言-行动-发现框架，其中具身智能体感知实验环境、推理科学知识、执行物理干预并内化结果以驱动后续探索。虽然论文以生命科学和化学科学为例，但其核心思想——通过将计算推理建立在物理反馈之上来弥合数字预测与经验验证之间的鸿沟——为在化学信息学等领域构建自主发现系统提供了路线图。这涉及到利用大模型（作为推理引擎）与物理实验设备（如质谱仪）的交互，从而与“化学大模型”和通过实验（可能包括质谱分析）进行“结构推理”的主题产生关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Artificial intelligence has demonstrated remarkable capability in predicting scientific properties, yet scientific discovery remains an inherently physical, long-horizon pursuit governed by experimental cycles. Most current computational approaches are misaligned with this reality, framing discovery as isolated, task-specific predictions rather than continuous interaction with the physical world. Here, we argue for embodied science, a paradigm that reframes scientific discovery as a closed loop tightly coupling agentic reasoning with physical execution. We propose a unified Perception-Language-Action-Discovery (PLAD) framework, wherein embodied agents perceive experimental environments, reason over scientific knowledge, execute physical interventions, and internalize outcomes to drive subsequent exploration. By grounding computational reasoning in robust physical feedback, this approach bridges the gap between digital prediction and empirical validation, offering a roadmap for autonomous discovery systems in the life and chemical sciences.

</details>

---

### 23. [GDEGAN: Gaussian Dynamic Equivariant Graph Attention Network for Ligand Binding Site Prediction](https://arxiv.org/abs/2603.19817)

**基本信息**

- 🔗 arXiv: [`2603.19817`](https://arxiv.org/abs/2603.19817)
- 👥 作者: Animesh, Plaban Kumar Bhowmick, Pralay Mitra
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19817.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一种新的深度学习模型用于蛋白质-配体结合位点预测，这是化学信息学和计算药物发现的核心问题，与“质谱结构推理”同属分子相互作用与结构预测范畴，且其方法（等变GNN）是构建“化学大模型”的重要技术之一。

**📖 中文摘要**

这篇论文提出了GDEGAN，一种用于蛋白质配体结合位点预测的新型等变图注意力网络。该方法专注于从蛋白质的3D结构中预测配体（小分子）可能结合的位置，这是计算药物发现中的关键步骤。论文的核心是提出了一种新的注意力机制，用自适应核取代点积注意力，以捕捉相邻残基在化学和几何特性上的变化。虽然论文主要应用在结构生物信息学领域，但其解决的问题（结合位点预测）是“质谱结构推理”的互补性技术：质谱用于推断小分子结构，而结合位点预测则是给定蛋白质结构，推断小分子可能的作用位置。两者都是化学信息学和计算药物发现的核心任务。论文提出的等变图神经网络方法本身也是一种用于处理3D分子/蛋白质结构的AI模型，与“化学大模型”中处理几何结构的方向相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of binding sites of a given protein, to which ligands can bind, is a critical step in structure-based computational drug discovery. Recently, Equivariant Graph Neural Networks (GNNs) have emerged as a powerful paradigm for binding site identification methods due to the large-scale availability of 3D structures of proteins via protein databases and AlphaFold predictions. The state-of-the-art equivariant GNN methods implement dot product attention, disregarding the variation in the chemical and geometric properties of the neighboring residues. To capture this variation, we propose GDEGAN (Gaussian Dynamic Equivariant Graph Attention Network), which replaces dot-product attention with adaptive kernels that recognize binding sites. The proposed attention mechanism captures variation in neighboring residues using statistics of their characteristic local feature distributions. Our mechanism dynamically computes neighborhood statistics at each layer, using local variance as an adaptive bandwidth parameter with learnable per-head temperatures, enabling each protein region to determine its own context-specific importance. GDEGAN outperforms existing methods with relative improvements of 37-66% in DCC and 7-19% DCA success rates across COACH420, HOLO4k, and PDBBind2020 datasets. These advances have direct application in accelerating protein-ligand docking by identifying potential binding sites for therapeutic target identification.

</details>

---

### 24. [Integrating Meta-Features with Knowledge Graph Embeddings for Meta-Learning](https://arxiv.org/abs/2603.19888)

**基本信息**

- 🔗 arXiv: [`2603.19888`](https://arxiv.org/abs/2603.19888)
- 👥 作者: Antonis Klironomos, Ioannis Dasoulas, Francesco Periti 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19888.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于知识图谱嵌入的元学习框架（KGmetaSP）和构建的统一KG，为整合科学实验数据（包括化学实验数据）提供了方法论和潜在工具，这些资源可用于构建或增强“化学大模型”或相关推理系统。

**📖 中文摘要**

这篇论文提出了KGmetaSP，一种利用知识图谱嵌入进行元学习的方法，旨在改进机器学习中的管道性能估计和数据集相似性估计任务。虽然论文的应用背景是通用机器学习，但其核心方法——构建一个统一的知识图谱来整合数据集、管道和实验结果的元数据，并从中学习嵌入以支持元学习任务——为化学信息学领域提供了宝贵的思路。在化学信息学中，存在海量的化合物、实验条件、谱图数据和模型预测结果，可以类似地构建领域特定的知识图谱。这样的图谱和嵌入可以作为训练更强大的“化学大模型”的优质数据资源，或者用于增强模型在特定任务（如质谱解析）上的元学习能力。因此，该论文提供的方法论和框架具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vast collection of machine learning records available on the web presents a significant opportunity for meta-learning, where past experiments are leveraged to improve performance. Two crucial meta-learning tasks are pipeline performance estimation (PPE), which predicts pipeline performance on target datasets, and dataset performance-based similarity estimation (DPSE), which identifies datasets with similar performance patterns. Existing approaches primarily rely on dataset meta-features (e.g., number of instances, class entropy, etc.) to represent datasets numerically and approximate these meta-learning tasks. However, these approaches often overlook the wealth of past experimental results and pipeline metadata available. This limits their ability to capture dataset - pipeline interactions that reveal performance similarity patterns. In this work, we propose KGmetaSP, a knowledge-graph-embeddings approach that leverages existing experiment data to capture these interactions and improve both PPE and DPSE. We represent datasets and pipelines within a unified knowledge graph (KG) and derive embeddings that support pipeline-agnostic meta-models for PPE and distance-based retrieval for DPSE. To validate our approach, we construct a large-scale benchmark comprising 144,177 OpenML experiments, enabling a rich cross-dataset evaluation. KGmetaSP enables accurate PPE using a single pipeline-agnostic meta-model and improves DPSE over baselines. The proposed KGmetaSP, KG, and benchmark are released, establishing a new reference point for meta-learning and demonstrating how consolidating open experiment data into a unified KG advances the field.

</details>

---

### 25. [SAGE: Sustainable Agent-Guided Expert-tuning for Culturally Attuned Translation in Low-Resource Southeast Asia](https://arxiv.org/abs/2603.19931)

**基本信息**

- 🔗 arXiv: [`2603.19931`](https://arxiv.org/abs/2603.19931)
- 👥 作者: Zhixiang Lu, Chong Zhang, Yulong Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19931.pdf)

**💡 相关性分析**

满足标准2和3：论文提出的可持续、数据高效的训练框架（SAGE）为在数据稀缺领域（如特定化学分支）构建大模型提供了重要的方法论工具和资源优化思路。同时，其关于平衡性能与能耗的讨论对化学AI的发展具有前瞻性意义。

**📖 中文摘要**

这篇论文提出了SAGE框架，旨在为低资源东南亚语言提供高质量、文化适配的机器翻译。其核心是采用强化学习智能体来从海量网络语料中自主筛选出紧凑、高质量的训练集，然后使用LoRA高效微调开源大语言模型。虽然论文聚焦于自然语言翻译，但其解决的核心矛盾——“数据稀缺与质量” vs “训练成本与可持续性”——以及提出的“质量优于数量”的能源感知范式，对“化学大模型”的构建具有直接的借鉴意义。化学大模型同样面临高质量、标注良好的领域数据（如精确的质谱-结构对）稀缺，以及训练超大模型能耗高的问题。SAGE框架中基于强化学习的智能数据筛选和高效微调策略，可以迁移到化学领域，用于从嘈杂的化学文献或数据库中构建高质量训练集，从而以更可持续的方式开发专业化学大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vision of an inclusive World Wide Web is impeded by a severe linguistic divide, particularly for communities in low-resource regions of Southeast Asia. While large language models (LLMs) offer a potential solution for translation, their deployment in data-poor contexts faces a dual challenge: the scarcity of high-quality, culturally relevant data and the prohibitive energy costs of training on massive, noisy web corpora. To resolve the tension between digital inclusion and environmental sustainability, we introduce Sustainable Agent-Guided Expert-tuning (SAGE). This framework pioneers an energy-aware paradigm that prioritizes the "right data" over "big data". Instead of carbon-intensive training on unfiltered datasets, SAGE employs a reinforcement learning (RL) agent, optimized via Group Relative Policy Optimization (GRPO), to autonomously curate a compact training set. The agent utilizes a semantic reward signal derived from a small, expert-constructed set of community dialogues to filter out noise and cultural misalignment. We then efficiently fine-tune open-source LLMs on this curated data using Low-Rank Adaptation (LoRA). We applied SAGE to translation tasks between English and seven low-resource languages (LRLs) in Southeast Asia. Our approach establishes new state-of-the-art performance on BLEU-4 and COMET-22 metrics, effectively capturing local linguistic nuances. Crucially, SAGE surpasses baselines trained on full datasets while reducing data usage by 97.1% and training energy consumption by 95.2%. By delivering high-performance models with a minimal environmental footprint, SAGE offers a scalable and responsible pathway to bridge the digital divide in the Global South.

</details>

---

### 26. [Hybrid topic modelling for computational close reading: Mapping narrative themes in Pushkin's Evgenij Onegin](https://arxiv.org/abs/2603.19940)

**基本信息**

- 🔗 arXiv: [`2603.19940`](https://arxiv.org/abs/2603.19940)
- 👥 作者: Angelo Maria Sabatini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19940.pdf)

**💡 相关性分析**

满足标准2：论文提出的混合主题建模方法为从文本数据（如化学文献）中提取结构化知识和特征提供了一种有效的工具，这些提取的知识可以作为构建或增强“化学大模型”和“质谱结构推理”系统的数据资源。

**📖 中文摘要**

这篇论文提出了一种用于计算文学分析的混合主题建模框架，结合了LDA和sPLS-DA。虽然其应用领域是文学文本分析，但该方法论本身具有通用性。在化学信息学中，文本挖掘是至关重要的技术，用于从海量科学文献中提取化合物、反应、性质等信息以构建知识库或训练模型。论文提出的“混合主题建模”框架，特别是结合无监督与有监督方法以在小规模语料上获得稳定、可解释主题的策略，可以迁移到化学文献分析中。例如，用于从质谱相关研究论文中自动发现和归类不同的谱图解析方法、应用领域或化合物类别主题，从而为“质谱结构推理”领域提供结构化的知识资源或特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study presents a hybrid topic modelling framework for computational literary analysis that integrates Latent Dirichlet Allocation (LDA) with sparse Partial Least Squares Discriminant Analysis (sPLS-DA) to model thematic structure and longitudinal dynamics in narrative poetry. As a case study, we analyse Evgenij Onegin-Aleksandr S. Pushkin's novel in verse-using an Italian translation, testing whether unsupervised and supervised lexical structures converge in a small-corpus setting. The poetic text is segmented into thirty-five documents of lemmatised content words, from which five stable and interpretable topics emerge. To address small-corpus instability, a multi-seed consensus protocol is adopted. Using sPLS-DA as a supervised probe enhances interpretability by identifying lexical markers that refine each theme. Narrative hubs-groups of contiguous stanzas marking key episodes-extend the bag-of-words approach to the narrative level, revealing how thematic mixtures align with the poem's emotional and structural arc. Rather than replacing traditional literary interpretation, the proposed framework offers a computational form of close reading, illustrating how lightweight probabilistic models can yield reproducible thematic maps of complex poetic narratives, even when stylistic features such as metre, phonology, or native morphology are abstracted away. Despite relying on a single lemmatised translation, the approach provides a transparent methodological template applicable to other high-density literary texts in comparative studies.

</details>

---

### 27. [Graph2TS: Structure-Controlled Time Series Generation via Quantile-Graph VAEs](https://arxiv.org/abs/2603.19970)

**基本信息**

- 🔗 arXiv: [`2603.19970`](https://arxiv.org/abs/2603.19970)
- 👥 作者: Shaoshuai Du, Joze M. Rozanec, Andy Pimentel 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19970.pdf)

**💡 相关性分析**

满足标准2：论文提出的Graph2TS框架（基于图的条件生成模型）为“化学大模型”和“质谱结构推理”主题提供了潜在的方法论和工具资源。其核心思想——使用图结构控制跨模态生成——可直接类比于从分子图生成性质或从质谱数据推理分子结构。

**📖 中文摘要**

本文提出Graph2TS，一种基于分位数图的条件变分自编码器，用于从结构图到时序数据的跨模态生成。该方法的核心是将时序数据分解为结构骨架和随机残差动态，并使用基于分位数的转移图来紧凑地捕获全局分布和时间依赖性。通过将生成过程以结构图为条件，模型能够在保持全局时间组织的同时实现可控的随机变化。虽然论文主要关注通用时序信号生成（如太阳黑子、心电图），但其提出的“从结构图到时序数据”的生成范式，以及利用图结构控制生成过程的思想，与“化学大模型”中分子图生成、结构-性质预测，以及“质谱结构推理”中从质谱数据推断分子结构（可视为一种跨模态推理）的核心挑战高度相关。论文提供了一种可用于结构控制生成的方法论和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although recent generative models can produce time series with close marginal distributions, they often face a fundamental tension between preserving global temporal structure and modeling stochastic local variations, particularly for highly volatile signals with weak or irregular periodicity. Direct distribution matching in such settings can amplify noise or suppress meaningful temporal patterns. In this work, we propose a structure-residual perspective on time-series generation, viewing temporal data as the combination of a structural backbone and stochastic residual dynamics, thereby motivating the separation of global organization from sample-level variability. Based on this insight, we represent time-series structure using a quantile-based transition graph that compactly captures global distributional and temporal dependencies. Building on this representation, we propose Graph2TS, a quantile-graph conditioned variational autoencoder that performs cross-modal generation from structural graphs to time series. By conditioning generation on structure rather than labels or metadata, the model preserves global temporal organization while enabling controlled stochastic variation. Experiments on diverse datasets, including sunspot, electricity load, ECG, and EEG signals, demonstrate improved distributional fidelity, temporal alignment, and representativeness compared to diffusion- and GAN-based baselines, highlighting structure-controlled and cross-modal generation as a promising direction for time-series modeling.

</details>

---

### 28. [DIAL-KG: Schema-Free Incremental Knowledge Graph Construction via Dynamic Schema Induction and Evolution-Intent Assessment](https://arxiv.org/abs/2603.20059)

**基本信息**

- 🔗 arXiv: [`2603.20059`](https://arxiv.org/abs/2603.20059)
- 👥 作者: Weidong Bao, Yilin Wang, Ruyu Gao 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.20059.pdf)

**💡 相关性分析**

满足标准2：论文提出的DIAL-KG框架为动态、增量式知识图谱构建提供了系统的方法和工具，这直接可用于构建和维护化学领域的动态知识库，为“化学大模型”提供持续更新的结构化知识资源。

**📖 中文摘要**

本文介绍DIAL-KG，一个用于增量知识图谱构建的闭环框架，由元知识库（MKB）协调。该框架在一个三阶段循环中运行：双轨提取（确保知识完整性）、治理裁决（确保事实保真度和时效性）和模式演化（从已验证的知识中归纳新模式以指导后续构建周期）。该框架旨在解决传统静态知识图谱构建方法在动态数据流和预定义模式限制下的不足。DIAL-KG的核心——从动态数据流中增量构建和演化知识图谱——与“化学大模型”中整合不断增长的化学知识（如反应、性质、文献）的需求高度契合。化学领域正是一个数据动态增长、需要持续更新知识表示的典型场景。该框架为构建和维护化学领域的动态知识图谱提供了系统性的方法论和工具思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge Graphs (KGs) are foundational to applications such as search, question answering, and recommendation. Conventional knowledge graph construction methods are predominantly static, rely ing on a single-step construction from a fixed corpus with a prede f ined schema. However, such methods are suboptimal for real-world sce narios where data arrives dynamically, as incorporating new informa tion requires complete and computationally expensive graph reconstruc tions. Furthermore, predefined schemas hinder the flexibility of knowl edge graph construction. To address these limitations, we introduce DIAL KG, a closed-loop framework for incremental KG construction orches trated by a Meta-Knowledge Base (MKB). The framework oper ates in a three-stage cycle: (i) Dual-Track Extraction, which ensures knowledge completeness by defaulting to triple generation and switching to event extraction for complex knowledge; (ii) Governance Adjudica tion, which ensures the fidelity and currency of extracted facts to prevent hallucinations and knowledge staleness; and (iii) Schema Evolution, in which new schemas are induced from validated knowledge to guide subsequent construction cycles, and knowledge from the current round is incrementally applied to the existing KG. Extensive experiments demon strate that our framework achieves state-of-the-art (SOTA) performance in the quality of both the constructed graph and the induced schemas.

</details>

---

### 29. [LLM-Enhanced Semantic Data Integration of Electronic Component Qualifications in the Aerospace Domain](https://arxiv.org/abs/2603.20094)

**基本信息**

- 🔗 arXiv: [`2603.20094`](https://arxiv.org/abs/2603.20094)
- 👥 作者: Antonio De Santis, Marco Balduini, Matteo Belcao 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.20094.pdf)

**💡 相关性分析**

满足标准2：论文提出的结合LLM与虚拟知识图谱的数据集成与检索管道，为“化学大模型”领域整合分散、异构的化学数据资源（如化合物数据库、反应库、文献）提供了可借鉴的方法论和工具框架。

**📖 中文摘要**

本文提出一个使用虚拟知识图谱和大型语言模型来集成和检索航空航天领域电子元件资格数据的管道。该方案旨在解决大型制造企业中因数据孤岛导致的信息检索不一致问题。管道利用虚拟知识图谱提供对异构数据源的统一视图，并利用LLM增强检索和减少数据清洗的手动工作。资格检索通过基于本体的数据访问方法进行结构化查询，并通过向量搜索机制基于相似的文本属性进行检索。论文进行了成本效益分析，表明该管道在长期效率上也优于单纯依赖LLM的方法（如RAG）。这项工作展示了如何将LLM与知识图谱、本体论等符号AI技术结合，以解决特定领域（这里是航空航天）复杂、异构数据的集成与智能检索问题。这种方法论完全可以迁移到化学信息学领域，用于整合分散的化学数据库、文献和实验数据，为“化学大模型”提供高质量、结构化的知识支撑。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large manufacturing companies face challenges in information retrieval due to data silos maintained by different departments, leading to inconsistencies and misalignment across databases. This paper presents an experience in integrating and retrieving qualification data for electronic components used in satellite board design. Due to data silos, designers cannot immediately determine the qualification status of individual components. However, this process is critical during the planning phase, when assembly drawings are issued before production, to optimize new qualifications and avoid redundant efforts. To address this, we propose a pipeline that uses Virtual Knowledge Graphs for a unified view over heterogeneous data sources and LLMs to enhance retrieval and reduce manual effort in data cleansing. The retrieval of qualifications is then performed through an Ontology-based Data Access approach for structured queries and a vector search mechanism for retrieving qualifications based on similar textual properties. We perform a comparative cost-benefit analysis, demonstrating that the proposed pipeline also outperforms approaches relying solely on LLMs, such as Retrieval-Augmented Generation (RAG), in terms of long-term efficiency.

</details>

---

### 30. [Conditioning Protein Generation via Hopfield Pattern Multiplicity](https://arxiv.org/abs/2603.20115)

**基本信息**

- 🔗 arXiv: [`2603.20115`](https://arxiv.org/abs/2603.20115)
- 👥 作者: Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.20115.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕蛋白质（作为一类重要的化学分子）的生成模型，并通过引入Hopfield模式多样性实现可控生成，这属于“化学大模型”在生物大分子设计方向上的前沿研究。

**📖 中文摘要**

本文提出一种通过Hopfield模式多样性调节蛋白质序列生成的方法。该方法基于随机注意力机制，允许用户通过一个简单的标量参数（作为采样器注意力logits的偏置）连续地将生成从整个蛋白质家族转向用户指定的功能子集（例如，来自结合筛选的命中序列），而无需重新训练或改变模型架构。该方法对子集所代表的属性（结合、稳定性、特异性等）不可知。核心思想是利用采样器内部表示进行精确调节，并通过几何度量预测解码序列表型可能存在的差距。实验在五个Pfam家族和靶向疼痛信号钙通道的ω-芋螺毒素肽上验证了该方法的有效性。这项工作直接涉及“化学大模型”的一个核心子领域——蛋白质生成与设计。它提供了一种无需重新训练即可引导生成模型聚焦于特定功能属性的实用技术，这对于基于AI的分子设计与优化具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequence generation via stochastic attention produces plausible family members from small alignments without training, but treats all stored sequences equally and cannot direct generation toward a functional subset of interest. We show that a single scalar parameter, added as a bias to the sampler's attention logits, continuously shifts generation from the full family toward a user-specified subset, with no retraining and no change to the model architecture. A practitioner supplies a small set of sequences (for example, hits from a binding screen) and a multiplicity ratio that controls how strongly generation favors them. The method is agnostic to what the subset represents: binding, stability, specificity, or any other property. We find that the conditioning is exact at the level of the sampler's internal representation, but that the decoded sequence phenotype can fall short because the dimensionality reduction used to encode sequences does not always preserve the residue-level variation that defines the functional split. We term this discrepancy the calibration gap and show that it is predicted by a simple geometric measure of how well the encoding separates the functional subset from the rest of the family. Experiments on five Pfam families (Kunitz, SH3, WW, Homeobox, and Forkhead domains) confirm the monotonic relationship between separation and gap across a fourfold range of geometries. Applied to omega-conotoxin peptides targeting a calcium channel involved in pain signaling, curated seeding from 23 characterized binders produces over a thousand candidates that preserve the primary pharmacophore and all experimentally identified binding determinants. These results show that stochastic attention enables practitioners to expand a handful of experimentally characterized sequences into diverse candidate libraries without retraining a generative model.

</details>

---

### 31. [Kolmogorov-Arnold causal generative models](https://arxiv.org/abs/2603.20184)

**基本信息**

- 🔗 arXiv: [`2603.20184`](https://arxiv.org/abs/2603.20184)
- 👥 作者: Alejandro Almodóvar, Mar Elizo, Patricia A. Apellániz 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.20184.pdf)

**💡 相关性分析**

满足标准2：论文提出的KaCGM框架将可解释的KAN网络与因果生成模型结合，为构建可解释、可审计的化学表格数据（如QSAR数据集）因果模型提供了新的工具和方法。

**📖 中文摘要**

本文提出KaCGM，一种用于混合类型表格数据的因果生成模型，其中每个结构方程都由一个Kolmogorov-Arnold网络（KAN）参数化。这种分解允许直接检查学习到的因果机制，包括符号近似和父子关系可视化，同时保持查询无关的生成语义。论文引入了一个基于分布匹配和推断外生变量独立性诊断的验证流程。在合成和半合成基准测试上的实验显示了与最先进方法相比具有竞争力的性能。一个真实世界的心血管案例研究进一步证明了提取简化结构方程和可解释因果效应的能力。这项工作将可解释的KAN架构与因果生成建模相结合，为表格数据（化学数据常以表格形式存在，如分子描述符、物化性质）的因果发现与生成提供了新工具。其强调的可解释性和机制透明性，对于构建可信的、可审计的“化学大模型”（如用于预测化合物毒性或活性的因果模型）具有重要价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Causal generative models provide a principled framework for answering observational, interventional, and counterfactual queries from observational data. However, many deep causal models rely on highly expressive architectures with opaque mechanisms, limiting auditability in high-stakes domains. We propose KaCGM, a causal generative model for mixed-type tabular data where each structural equation is parameterized by a Kolmogorov--Arnold Network (KAN). This decomposition enables direct inspection of learned causal mechanisms, including symbolic approximations and visualization of parent--child relationships, while preserving query-agnostic generative semantics. We introduce a validation pipeline based on distributional matching and independence diagnostics of inferred exogenous variables, allowing assessment using observational data alone. Experiments on synthetic and semi-synthetic benchmarks show competitive performance against state-of-the-art methods. A real-world cardiovascular case study further demonstrates the extraction of simplified structural equations and interpretable causal effects. These results suggest that expressive causal generative modeling and functional transparency can be achieved jointly, supporting trustworthy deployment in tabular decision-making settings. Code: this https URL

</details>

---

### 32. [Reinforcement-guided generative protein language models enable de novo design of highly diverse AAV capsids](https://arxiv.org/abs/2603.19473)

**基本信息**

- 🔗 arXiv: [`2603.19473`](https://arxiv.org/abs/2603.19473)
- 👥 作者: Lucas Ferraz, Ana F. Rodrigues, Pedro Giesteira Cotovio 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19473.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用和微调预训练的蛋白质语言模型（一种化学大模型）来生成新的蛋白质序列，属于化学大模型在蛋白质设计领域的应用。

**📖 中文摘要**

本文提出了一种基于蛋白质语言模型和强化学习的生成式设计框架，用于生成高度新颖且功能合理的腺相关病毒（AAV）衣壳蛋白序列。该框架首先在实验验证的衣壳序列上对预训练模型进行微调，以学习与蛋白活性相关的模式。随后，利用强化学习引导序列生成，其奖励函数同时促进预测的蛋白活性和序列新颖性，从而能够探索训练数据分布之外的序列空间。该方法为蛋白质序列空间的生成式探索提供了一个框架，并推进了生成式蛋白质语言模型在AAV生物工程中的应用。这项工作与“化学大模型”主题直接相关，因为它利用并微调了预训练的蛋白质语言模型（一种特定领域的化学大模型）来生成新的蛋白质序列。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adeno-associated viral (AAV) vectors are widely used delivery platforms in gene therapy, and the design of improved capsids is key to expanding their therapeutic potential. A central challenge in AAV bioengineering, as in protein design more broadly, is the vast sequence design space relative to the scale of feasible experimental screening. Machine-guided generative approaches provide a powerful means of navigating this landscape and proposing novel protein sequences that satisfy functional constraints. Here, we develop a generative design framework based on protein language models and reinforcement learning to generate highly novel yet functionally plausible AAV capsids. A pretrained model was fine-tuned on experimentally validated capsid sequences to learn patterns associated with viability. Reinforcement learning was then used to guide sequence generation, with a reward function that jointly promoted predicted viability and sequence novelty, thereby enabling exploration beyond regions represented in the training data. Comparative analyses showed that fine-tuning alone produces sequences with high predicted viability but remains biased toward the training distribution, whereas reinforcement learining-guided generation reaches more distant regions of sequence space while maintaining high predicted viability. Finally, we propose a candidate selection strategy that integrates predicted viability, sequence novelty, and biophysical properties to prioritize variants for downstream evaluation. This work establishes a framework for the generative exploration of protein sequence space and advances the application of generative protein language models to AAV bioengineering.

</details>

---

### 33. [Physics-Informed Long-Range Coulomb Correction for Machine-learning Hamiltonians](https://arxiv.org/abs/2603.20007)

**基本信息**

- 🔗 arXiv: [`2603.20007`](https://arxiv.org/abs/2603.20007)
- 👥 作者: Yang Zhong, Xiwen Li, Xingao Gong 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.20007.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个物理信息驱动的机器学习框架（HamGNN-LR），用于改进化学系统（特别是极性材料和异质结构）的电子哈密顿量预测，这直接涉及化学大模型（用于分子/材料性质的机器学习模型）的构建与优化。

**📖 中文摘要**

本文针对机器学习电子哈密顿量模型普遍忽略长程库仑相互作用的问题，提出了一个物理信息驱动的长程修正框架。该框架通过静电能的变分分解，在非正交原子轨道基组中推导出长程哈密顿矩阵元的闭式解，从而得到从电子密度矩阵到有效原子电荷的变分一致映射。作者将此框架实现为HamGNN-LR，这是一个双通道架构，结合了E(3)-等变消息传递和倒易空间Ewald求和。基准测试表明，这种基于物理的长程修正对于捕捉宏观静电势至关重要，而纯数据驱动的注意力机制则无法做到。在极性ZnO板、CdSe/ZnS异质结构和GaN/AlN超晶格上的测试显示，该方法将误差降低了2到3倍，并能鲁棒地迁移到远超训练规模的系统，消除了短程模型在存在内建电场时特有的阶梯状伪影。这项工作直接利用物理原理增强机器学习模型（图神经网络）对化学系统（极性晶体和异质结构）的建模能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learning electronic Hamiltonians achieve orders-of-magnitude speedups over density-functional theory, yet current models omit long-range Coulomb interactions that govern physics in polar crystals and heterostructures. We derive closed-form long-range Hamiltonian matrix elements in a nonorthogonal atomic-orbital basis through variational decomposition of the electrostatic energy, deriving a variationally consistent mapping from the electron density matrix to effective atomic charges. We implement this framework in HamGNN-LR, a dual-channel architecture combining E(3)-equivariant message passing with reciprocal-space Ewald summation. Benchmarks demonstrate that physics-based long-range corrections are essential: purely data-driven attention mechanisms fail to capture macroscopic electrostatic potentials. Benchmarks on polar ZnO slabs, CdSe/ZnS heterostructures, and GaN/AlN superlattices show two- to threefold error reductions and robust transferability to systems far beyond training sizes, eliminating the characteristic staircase artifacts that plague short-range models in the presence of built-in electric fields.

</details>

---

### 34. [Causal Learning in Biomedical Applications: Krebs Cycle as a Benchmark](https://arxiv.org/abs/2406.15189)

**基本信息**

- 🔗 arXiv: [`2406.15189`](https://arxiv.org/abs/2406.15189)
- 👥 作者: Xiaoyu He, Petr Ryšavý, Jakub Mareček
- 📄 PDF: [下载](https://arxiv.org/pdf/2406.15189.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个基于生化途径模拟的基准数据集，该数据集可用于开发和评估从复杂化学/生物时间序列数据中学习因果关系的模型。这类模型（如因果发现方法）可以应用于质谱衍生的代谢组学时间序列数据，以进行结构推理或通路分析，因此提供了相关的数据资源。

**📖 中文摘要**

本文提出了一个基于克雷布斯循环（一种关键生化途径）模拟的新基准数据集，用于评估时间序列数据的因果发现方法。数据使用基于粒子的模拟器生成，该模拟器在受控环境中模拟分子相互作用。该基准提供了四种不同的场景，并包含用于评估的真实因果图。它支持使用结构汉明距离、结构干预距离和F1分数等指标进行定量比较。作者对来自不同建模范式的14种因果发现方法进行了全面评估。该数据集为测试时间序列数据上的因果学习方法提供了一个可重复、可解释且非平凡的基准。这项工作与“化学大模型”和“质谱结构推理”相关，因为它提供了一个基于生物化学途径的基准，可用于开发和评估能够从复杂化学/生物时间序列数据（如代谢组学时间序列，可能源自质谱）中推断因果关系的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning causal relationships from time series data is an important but challenging problem. Existing synthetic datasets often contain hidden artifacts that can be exploited by causal discovery methods, reducing their usefulness for benchmarking. We present a new benchmark dataset based on simulations of the Krebs cycle, a key biochemical pathway. The data are generated using a particle-based simulator that models molecular interactions in a controlled environment. Four distinct scenarios are provided, varying in time series length, number of samples, and intervention settings. The benchmark includes ground-truth causal graphs for evaluation. It supports quantitative comparisons using metrics such as Structural Hamming Distance, Structural Intervention Distance, and F1-score. A comprehensive evaluation of 14 causal discovery methods from different modelling paradigms is presented. Performance is compared across datasets using multiple accuracy and efficiency measures. The dataset provides a reproducible, interpretable, and non-trivial benchmark for testing causal learning methods on time series data. It avoids common pitfalls such as residual structural patterns and supports interventions and evaluation with known causal ground truth. This makes it a useful tool for the development and comparison of causal discovery algorithms.

</details>

---

### 35. [Simulation-based Inference with the Python Package sbijax](https://arxiv.org/abs/2409.19435)

**基本信息**

- 🔗 arXiv: [`2409.19435`](https://arxiv.org/abs/2409.19435)
- 👥 作者: Simon Dirmeier, Antonietta Mira, Carlo Albert
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.19435.pdf)

**💡 相关性分析**

满足标准2：论文介绍了一个Python软件包（sbijax），它实现了多种模拟推理方法。这些方法可以应用于化学和质谱分析中的逆问题，例如从质谱数据中推断分子结构或反应参数，因此提供了可用于这些主题的工具资源。

**📖 中文摘要**

本文介绍了sbijax，一个基于JAX的Python库，实现了多种最先进的神经模拟推理方法，用于具有难处理似然函数的贝叶斯推断。该库采用模块化和解耦的架构，将环境、神经网络模块和训练目标视为可互换组件，为用户提供了简单而强大的API以促进快速原型设计和研究。SBI方法在化学和质谱分析中具有潜在应用，例如，用于从光谱数据中推断分子结构参数（逆问题），或校准复杂计算化学模型的参数。该库提供了高效实现相关算法的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural simulation-based inference (SBI) describes an emerging family of methods for Bayesian inference with intractable likelihood functions that use neural networks as surrogate models. Here we introduce sbijax, a Python package that implements a wide variety of state-of-the-art methods in neural simulation-based inference using a user-friendly programming interface. sbijax offers high-level functionality to quickly construct SBI estimators, and compute and visualize posterior distributions with only a few lines of code. In addition, the package provides functionality for conventional approximate Bayesian computation, to compute model diagnostics, and to automatically estimate summary statistics. By virtue of being entirely written in JAX, sbijax is extremely computationally efficient, allowing rapid training of neural networks and executing code automatically in parallel on both CPU and GPU.

</details>

---

### 36. [CatBOX: A Categorical-Continuous Bayesian Optimization with Spectral Mixture Kernels for Accelerated Catalysis Experiments](https://arxiv.org/abs/2505.17393)

**基本信息**

- 🔗 arXiv: [`2505.17393`](https://arxiv.org/abs/2505.17393)
- 👥 作者: Changquan Zhao, Yi Zhang, Zhuo Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.17393.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种机器学习优化框架（CatBOX），用于高效探索催化剂组成和反应条件的化学空间，这是化学信息学和化学大模型（用于逆向设计和优化）的典型应用场景。

**📖 中文摘要**

本文提出了CatBOX，一种用于加速催化实验设计的贝叶斯优化方法，能够联合优化分类（如催化剂组成、载体类型）和连续（如温度、压力）实验参数。该方法引入了一种新颖的谱混合核函数，结合高斯和柯西混合的逆傅里叶变换，以灵活表示连续参数空间，捕捉平滑和非平滑的变化。分类选择通过基于汉明距离的信任区域进行导航。CatBOX在合成函数和三个真实催化实验（甲烷氧化偶联、尿素选择性催化还原、咪唑直接芳基化）上进行了基准测试，在缺乏先验知识的情况下可靠地识别出最高效的催化剂配方和反应条件。这项工作展示了贝叶斯优化（一种用于化学空间探索的机器学习方法）在催化剂发现这一核心化学信息学任务中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Identifying optimal catalyst compositions and reaction conditions is central in catalysis research, yet remains challenging due to the vast multidimensional design spaces encompassing both continuous and categorical parameters. In this work, we present CatBOX, a Bayesian Optimization method for accelerated catalytic experimental design that jointly optimizes categorical and continuous experimental parameters. Our approach introduces a novel spectral mixture kernel that combines the inverse Fourier transform of Gaussian and Cauchy mixtures to provide a flexible representation of the continuous parameter space, capturing both smooth and non-smooth variations. Categorical choices, such as catalyst compositions and support types, are navigated via trust regions based on Hamming distance. For performance evaluation, CatBOX was theoretically verified based on information theory and benchmarked on a series of synthetic functions, achieving more than a 3-fold improvement relative to the best-performing baseline and a 19-fold improvement relative to random search on average across tasks. Additionally, three real-life catalytic experiments, including oxidative coupling of methane, urea-selective catalytic reduction, and direct arylation of imidazoles, were further used for in silico benchmarking, where CatBOX reliably identified top catalyst recipes and reaction conditions with the highest efficiencies in the absence of any a priori knowledge. Finally, we develop an open-source, code-free online platform to facilitate trial deployment in real experimental settings, particularly for self-driving laboratory environments.

</details>

---

### 37. [Jump-diffusion models of parametric volume-price distributions](https://arxiv.org/abs/2511.16838)

**基本信息**

- 🔗 arXiv: [`2511.16838`](https://arxiv.org/abs/2511.16838)
- 👥 作者: Anup Budhathoki, Leonardo Rydin Gorjão, Pedro G. Lind 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.16838.pdf)

**💡 相关性分析**

满足标准1：论文提出的对高维实证数据进行参数化分布建模和时间序列动力学分析的数据驱动框架，其核心方法论与质谱结构推理中处理复杂光谱数据、进行模式识别和特征提取的研究思路高度相关，可被视为一种广义的“结构推理”方法在金融数据上的应用。

**📖 中文摘要**

本文提出了一个数据驱动的框架，用于模拟纽约证券交易所（NYSE）股票交易中成交量-价格分布的随机演化。该研究对976个交易日内每10分钟采样的经验分布进行拟合，使用了Gamma、逆Gamma、Weibull和对数正态等参数化模型。通过分析去趋势后的形状参数和尺度参数的时间序列，并利用Kramers-Moyal系数提取其内在动力学，论文展示了如何对金融时间序列进行建模和分类（如纯扩散或跳跃扩散）。虽然论文本身聚焦于金融计量经济学，但其核心方法——对复杂、高维的实证数据进行参数化分布建模、时间序列分析以及动力学机制识别——与化学信息学和质谱分析中处理大量、高维化学或光谱数据、进行模式识别和结构推理的思路在方法论上高度相关。例如，质谱数据可以视为一种多维信号分布，其分析同样涉及拟合、去噪、特征提取和动力学建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a data-driven framework to model the stochastic evolution of volume-price distribution from the New York Stock Exchange (NYSE) equities. The empirical distributions are sampled every 10 minutes over 976 trading days, and fitted to different models, namely Gamma, Inverse Gamma, Weibull, and Log-Normal distributions. Each of these models is parameterized by a shape parameter, $phi$, and a scale parameter, $\theta$, which are detrended from their daily average behavior. The time series of the detrended parameters is analyzed using adaptive binning and regression-based extraction of the Kramers-Moyal (KM) coefficients, up to their sixth order, enabling to classification of its intrinsic dynamics. We show that (i) $\phi$ is well described as a pure diffusion with a linear mean regression for the Gamma, Inverse Gamma, and Weibull models, while $\theta$ shows dominant jump-diffusion dynamics, with an elevated fourth- and sixth-order moment contributions; (ii) the log-normal model shows however the opposite: $\theta$ is predominantly diffusive, with $\phi$ showing weak jump signatures; (iii) global moment inversion yields jump rates and amplitudes that account for a large share of total variance for $\theta$, confirming that rare discontinuities dominate volatility.

</details>

---

### 38. [CryoHype: Reconstructing a thousand cryo-EM structures with transformer-based hypernetworks](https://arxiv.org/abs/2512.06332)

**基本信息**

- 🔗 arXiv: [`2512.06332`](https://arxiv.org/abs/2512.06332)
- 👥 作者: Jeffrey Gu, Minkyu Jeon, Ambri Ma 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.06332.pdf)

**💡 相关性分析**

满足标准1：论文提出的使用Transformer超网络从混合信号中同时重构大量三维结构的方法，其核心研究内容（混合信号解析、多目标结构推理、基于Transformer的生成模型）与“化学大模型”和“质谱结构推理”主题高度相关，为解决质谱数据分析中的类似挑战提供了创新的模型架构视角。

**📖 中文摘要**

本文提出了CryoHype，一种基于Transformer超网络的冷冻电镜（cryo-EM）重构方法，用于从可能包含许多不同分子物种混合物的未标记冷冻电镜图像中同时解析大量（高达1000个）不同的生物分子结构。该方法通过超网络动态调整隐式神经表示的权重，从而能够处理由混合物引起的组成异质性。这一工作将冷冻电镜从通常针对单一或少数结构建模，推向高通量、多目标结构解析。虽然应用领域是结构生物学，但CryoHype的核心技术创新——使用Transformer超网络和隐式神经表示来处理和重构来自复杂混合信号的高维结构数据——与“化学大模型”和“质谱结构推理”主题在核心挑战上高度相似。质谱同样用于分析复杂混合物（如代谢组学），并从混合信号中推断出众多化合物的结构。因此，该论文在解决“从混合信号中推理多个结构”这一根本性难题上提供了前沿的模型架构思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cryo-electron microscopy (cryo-EM) is an indispensable technique for determining the 3D structures of dynamic biomolecular complexes. While typically applied to image a single molecular species, cryo-EM has the potential for structure determination of many targets simultaneously in a high-throughput fashion. However, existing methods typically focus on modeling conformational heterogeneity within a single or a few structures and are not designed to resolve compositional heterogeneity arising from mixtures of many distinct molecular species. To address this challenge, we propose CryoHype, a transformer-based hypernetwork for cryo-EM reconstruction that dynamically adjusts the weights of an implicit neural representation. Using CryoHype, we achieve state-of-the-art results on a challenging benchmark dataset containing 100 structures. We further demonstrate that CryoHype scales to the reconstruction of 1,000 distinct structures from unlabeled cryo-EM images in the fixed-pose setting.

</details>

---

### 39. [Accelerating Large-Scale Cheminformatics Using a Byte-Offset Indexing Architecture for Terabyte-Scale Data Integration](https://arxiv.org/abs/2601.18921)

**基本信息**

- 🔗 arXiv: [`2601.18921`](https://arxiv.org/abs/2601.18921)
- 👥 作者: Malikussaid, Septian Caesar Floresko, Sutiyo
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18921.pdf)

**💡 相关性分析**

满足标准2：论文的核心内容是构建用于机器学习（包括潜在的大模型）的大规模、精选化学数据集，并提供了高效的数据集成架构和工具，这直接为化学信息学领域，特别是化学大模型的训练和评估，提供了关键的数据资源和方法。

**📖 中文摘要**

本文针对大规模化学信息学数据集成中的关键瓶颈问题进行了案例研究，旨在整合PubChem、ChEMBL和eMolecules等主要公共化学数据库，以构建用于分子性质预测的精选数据集。研究探讨了字节偏移索引架构能否在保持数据完整性的前提下，克服百亿级数据规模的暴力搜索可扩展性限制。通过将算法复杂度从O(N×M)降低到O(N+M)，实现了740倍的性能提升。研究过程中发现了InChIKey分子标识符的哈希碰撞问题，并重建了使用无碰撞完整InChI字符串的数据处理流程。这项工作为大规模科学数据集成提供了通用原则，特别是在唯一性约束超出基于哈希的标识符能力的情况下。该研究直接为化学信息学领域提供了大规模、高质量、多源验证的数据集构建方法和工具，这对于训练和评估化学大模型（如用于性质预测或结构生成的模型）至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of large-scale chemical databases represents a critical bottleneck in modern cheminformatics research, particularly for machine learning applications requiring high-quality, multi-source validated datasets. This paper presents a case study of integrating three major public chemical repositories: PubChem (176 million compounds), ChEMBL, and eMolecules, to construct a curated dataset for molecular property prediction. We investigate whether byte-offset indexing can practically overcome brute-force scalability limits while preserving data integrity at hundred-million scale. Our results document the progression from an intractable brute-force search algorithm with projected 100-day runtime to a byte-offset indexing architecture achieving 3.2-hour completion - a 740-fold performance improvement through algorithmic complexity reduction from $O(N \times M)$ to $O(N + M)$. Systematic validation of 176 million database entries revealed hash collisions in InChIKey molecular identifiers, necessitating pipeline reconstruction using collision-free full InChI strings. We present performance benchmarks, quantify trade-offs between storage overhead and scientific rigor, and compare our approach with alternative large-scale integration strategies. The resulting system successfully extracted 435,413 validated compounds and demonstrates generalizable principles for large-scale scientific data integration where uniqueness constraints exceed hash-based identifier capabilities.

</details>

---

### 40. [Learning Representations for Independence Testing](https://arxiv.org/abs/2409.06890)

**基本信息**

- 🔗 arXiv: [`2409.06890`](https://arxiv.org/abs/2409.06890)
- 👥 作者: Nathaniel Xu, Feng Liu, Danica J. Sutherland
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.06890.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是学习用于依赖性检验的表示，这直接关系到评估模型表示的质量和发现数据中的复杂关系。在化学信息学和质谱分析中，评估分子表示与性质之间的依赖关系，以及从质谱数据中推断结构，本质上都是依赖性分析问题。因此，该论文提出的框架和方法与这两个主题高度相关。

**📖 中文摘要**

本文研究了两种学习强大独立性检验的方法。首先，展示了如何利用互信息的变分估计量（如InfoNCE或NWJ估计量）来构建具有有限样本有效性的强大统计检验。其次，建立了这些基于变分互信息的检验与基于希尔伯特-施密特独立性准则（HSIC）的检验之间的紧密联系；特别是，学习互信息的变分界（通常由深度网络参数化）与学习HSIC的核密切相关。最后，展示了如何选择一种表示来最大化检验的效力，而不是最大化统计量本身。这项工作与“化学大模型”和“质谱结构推理”都相关。在化学信息学中，评估分子表示（如SMILES字符串或分子图）与目标性质之间的依赖性至关重要。本文提出的学习依赖性统计量的方法，可以用于评估和比较不同化学大模型生成的表示的质量，或者用于构建能够从质谱数据中推断分子结构的模型，其中需要检测质谱特征与分子子结构之间的复杂依赖关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many tools exist to detect dependence between random variables, a core question across a wide range of machine learning, statistical, and scientific endeavors. Although several statistical tests guarantee eventual detection of any dependence with enough samples, standard tests may require an exorbitant amount of samples for detecting subtle dependencies between high-dimensional random variables with complex distributions. In this work, we study two related ways to learn powerful independence tests. First, we show how to construct powerful statistical tests with finite-sample validity by using variational estimators of mutual information, such as the InfoNCE or NWJ estimators. Second, we establish a close connection between these variational mutual information-based tests and tests based on the Hilbert-Schmidt Independence Criterion (HSIC); in particular, learning a variational bound (typically parameterized by a deep network) for mutual information is closely related to learning a kernel for HSIC. Finally, we show how to, rather than selecting a representation to maximize the statistic itself, select a representation which can maximize the power of a test, in either setting; we term the former case a Neural Dependency Statistic (NDS). While HSIC power optimization has been recently considered in the literature, we correct some important misconceptions and expand to considering deep kernels. In our experiments, while all approaches can yield powerful tests with exact level control, optimized HSIC tests generally outperform the other approaches on difficult problems of detecting structured dependence.

</details>

---

### 41. [Virtual Sensing for Solder Layer Degradation and Temperature Monitoring in IGBT Modules](https://arxiv.org/abs/2508.10515)

**基本信息**

- 🔗 arXiv: [`2508.10515`](https://arxiv.org/abs/2508.10515)
- 👥 作者: Andrea Urgolo, Monika Stipsitz, Hèlios Sanchis-Alepuz
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.10515.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用机器学习进行状态估计（虚拟传感），从有限的、可观测的信号推断内部不可观测的退化状态和温度分布。这种方法论与“质谱结构推理”高度相似，后者旨在从观测到的质谱信号推断未观测到的分子结构。因此，该论文为解决质谱结构推理问题提供了相关的技术思路和概念框架。

**📖 中文摘要**

本文探讨了基于机器学习虚拟传感技术，通过有限数量的物理传感器来估计绝缘栅双极晶体管（IGBT）模块中焊料层的退化状态和相应完整温度图的可行性。基于特定退化模式的合成数据，作者在退化焊料区域面积估计上获得了高精度（1.17%的平均绝对误差），并且能够以最大相对误差4.56%（对应平均相对误差0.37%）重现IGBT的表面温度。这项工作与“质谱结构推理”主题在方法论上相关。质谱结构推理的核心是从复杂的、高维的质谱信号中推断出低维的分子结构信息，这同样是一个从有限观测（质谱峰）估计底层不可见状态（分子结构）的逆问题。本文展示的虚拟传感方法——使用机器学习模型从可访问的传感器数据推断内部不可访问的状态——为解决质谱结构推理问题提供了概念上的类比和技术上的启发，例如，可以训练模型从质谱特征“虚拟感知”分子的子结构或官能团。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Monitoring the degradation state of Insulated Gate Bipolar Transistor (IGBT) modules is essential for ensuring the reliability and longevity of power electronic systems, especially in safety-critical and high-performance applications. However, direct measurement of key degradation indicators - such as junction temperature, solder fatigue or delamination - remains challenging due to the physical inaccessibility of internal components and the harsh environment. In this context, machine learning-based virtual sensing offers a promising alternative by bridging the gap from feasible sensor placement to the relevant but inaccessible locations. This paper explores the feasibility of estimating the degradation state of solder layers, and the corresponding full temperature maps based on a limited number of physical sensors. Based on synthetic data of a specific degradation mode, we obtain a high accuracy in the estimation of the degraded solder area (1.17% mean absolute error), and are able to reproduce the surface temperature of the IGBT with a maximum relative error of 4.56% (corresponding to an average relative error of 0.37%).

</details>

---

### 42. [An SO(3)-equivariant reciprocal-space neural potential for long-range interactions](https://arxiv.org/abs/2603.18389)

**基本信息**

- 🔗 arXiv: [`2603.18389`](https://arxiv.org/abs/2603.18389)
- 👥 作者: Lingfeng Zhang, Taoyong Cui, Dongzhan Zhou 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种SO(3)-等变的神经原子间势能，这是一种先进的机器学习方法，用于精确模拟分子系统的能量和力，直接属于构建“化学大模型”以理解和预测化学结构与性质的核心技术范畴。

**📖 中文摘要**

本文提出了一种名为EquiEwald的新型神经原子间势能模型，旨在解决机器学习势能中长期存在的长程相互作用（如静电和极化作用）建模难题。该模型的核心创新在于将Ewald求和的倒空间思想嵌入到一个不可约的SO(3)-等变神经网络框架中。通过在倒空间进行等变消息传递，并利用学习到的等变k空间滤波器和等变逆变换，该模型能够捕捉各向异性的、缓慢衰减的多极关联，同时保持能量-力的一致性。这项工作代表了在构建物理原理清晰、能够准确描述长程相互作用的机器学习势能方面的重要进展。虽然论文主要聚焦于分子和凝聚态系统的通用势能模型，但其核心方法——即利用等变神经网络框架处理复杂的、与方向相关的物理相互作用——与“化学大模型”中处理分子结构和性质预测的核心挑战高度相关。该模型可被视为构建更准确、更通用的化学领域基础模型（化学大模型）的关键技术组件。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Long-range electrostatic and polarization interactions play a central role in molecular and condensed-phase systems, yet remain fundamentally incompatible with locality-based machine-learning interatomic potentials. Although modern SO(3)-equivariant neural potentials achieve high accuracy for short-range chemistry, they cannot represent the anisotropic, slowly decaying multipolar correlations governing realistic materials, while existing long-range extensions either break SO(3) equivariance or fail to maintain energy-force consistency. Here we introduce EquiEwald, a unified neural interatomic potential that embeds an Ewald-inspired reciprocal-space formulation within an irreducible SO(3)-equivariant framework. By performing equivariant message passing in reciprocal space through learned equivariant k-space filters and an equivariant inverse transform, EquiEwald captures anisotropic, tensorial long-range correlations without sacrificing physical consistency. Across periodic and aperiodic benchmarks, EquiEwald captures long-range electrostatic behavior consistent with ab initio reference data and consistently improves energy and force accuracy, data efficiency, and long-range extrapolation. These results establish EquiEwald as a physically principled paradigm for long-range-capable machine-learning interatomic potentials.

</details>

---

## 📊 数据统计
- 累计运行天数：47
- 累计论文数量：3363

## 📝 历史记录

> 暂无历史数据

