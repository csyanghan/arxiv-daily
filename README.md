# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-21 01:15:26

## 📅 2026-03-21 (今日最新)

**相关论文数：70**

### 1. [Continually self-improving AI](https://arxiv.org/abs/2603.18073)

**基本信息**

- 🔗 arXiv: [`2603.18073`](https://arxiv.org/abs/2603.18073)
- 👥 作者: Zitong Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕如何构建能够持续自我改进的“大模型”（包括知识获取、数据生成和算法发现），这与“化学大模型”主题中关于模型能力提升和自演进的方向直接相关。

**📖 中文摘要**

这篇论文探讨了如何克服当前语言模型在知识获取、数据依赖和训练算法方面的局限性，以创建持续自我改进的AI。论文提出了三个核心章节：1）通过合成数据方法，将小型语料库多样化和放大为丰富的知识表示，使模型能够从有限的源材料中有效更新其参数，从而克服知识获取中的数据效率障碍。2）为了减少对人类数据的依赖，论文展示了在给定固定数量的人类数据的情况下，模型可以自生成合成数据来引导其基本预训练能力，而无需从任何现成的指令调优LM中进行蒸馏。3）为了超越人类设计的训练范式，论文证明了通过在测试时对算法空间进行扩展搜索，AI可以探索比人类研究人员手动探索更大的学习算法配置空间。虽然论文主要关注通用语言模型，但其核心主题——通过合成数据、自生成数据和算法搜索来构建“化学大模型”或改进“质谱结构推理”的底层模型能力——与“化学大模型”的研究方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern language model-based AI systems are remarkably powerful, yet their capabilities remain fundamentally capped by their human creators in three key ways. First, although a model's weights can be updated via fine-tuning, acquiring new knowledge from small, specialized corpora after pretraining remains highly data-inefficient. Second, the training of these systems relies heavily on finite, human-generated data from across history. Third, the pipelines used to train AI models are confined by the algorithms that human researchers can discover and explore. This thesis takes a small step toward overcoming these inherent limitations, presenting three chapters aimed at breaking these dependencies to create continually self-improving AI. First, to overcome this data-efficiency barrier in knowledge acquisition, we propose a synthetic data approach that diversifies and amplifies small corpora into rich knowledge representations, enabling a model to effectively update its parameters from limited source material. Second, to reduce reliance on human data, we show that given a fixed amount of such data, the model can self-generate synthetic data to bootstrap its fundamental pretraining capabilities without distillation from any off-the-shelf, instruction-tuned LM. Finally, to transcend human-engineered training paradigms, we demonstrate that by scaling search during test time over the space of algorithms, AI can search over a larger space of learning algorithm configurations than human researchers can explore manually.

</details>

---

### 2. [HWE-Bench: Can Language Models Perform Board-level Schematic Designs?](https://arxiv.org/abs/2603.18102)

**基本信息**

- 🔗 arXiv: [`2603.18102`](https://arxiv.org/abs/2603.18102)
- 👥 作者: Weibo Qiu, Yinhao Xiao, Runyu Pan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18102.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升大语言模型在复杂科学工程领域（电路设计）进行结构化推理和生成的能力。这种让大模型处理专业领域数据、进行多步推理并输出结构化结果的研究范式，与“化学大模型”和“质谱结构推理”的研究目标（即让AI模型理解化学数据并推理出分子结构）在核心方法论上直接相关。

**📖 中文摘要**

这篇论文提出了HWE-Bench评估框架，用于评测大语言模型（LLMs）执行板级电路原理图设计的能力。该任务需要模型综合理解真实世界的物理学和集成电路（IC）数据手册。HWE-Bench包含300个从开源和众包平台收集的设计任务，涵盖8个应用领域，并辅以一个包含2,914份真实IC数据手册的知识库。对于每个任务，LLMs需要根据提供的电路功能要求和一组元件数据手册，从零开始生成原理图。生成的原理图将通过静态电气规则检查，并传递给电路模拟器以验证其动态行为。评估表明，当前模型虽然实现了初步的工程可用性和文档理解，但缺乏物理直觉。这项研究旨在为开发实用的电子设计自动化（EDA）代理铺平道路。虽然应用领域是电子工程，但该框架的核心——让大模型理解复杂的领域特定数据（数据手册）、进行多步骤推理并生成结构化输出（原理图）——与“化学大模型”处理化学数据（如质谱、分子结构）和“质谱结构推理”中从复杂数据推导出化学结构的任务在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated significant potential in various engineering tasks, including software development, digital logic generation, and companion document maintenance. However, their ability to perform board-level circuit design is understudied, as this task requires a synergized understanding of real-world physics and Integrated Circuit (IC) datasheets, the latter comprising detailed specifications for individual components. To address this challenge, we propose \hweb, an evaluation framework that benchmarks the ability of LLMs to perform such designs. It consists of 300 board-level design tasks pulled from open-source and crowdsourcing platforms such as GitHub and OSHWLab, covering 8 application domains, and is complemented with a knowledge base of 2,914 real IC datasheets. For each task, the LLMs are tasked with generating a schematic from scratch, using the provided circuit functional requirements and a set of component datasheets as input. The resulting schematic will be checked against a static electrical rules, and then passed to a circuit simulator to verify its dynamic behavior. Our evaluation show that although current models achieve initial engineering usability and documentation understanding, they lack physical intuition, as the top-performing model achieved an overall pass rate of 8.15\%. We envision that advancements on \hweb\ will pave the way for the development of practical Electronic Design Automation (EDA) agents, revolutionizing the field of board-level design.

</details>

---

### 3. [LLM-Augmented Computational Phenotyping of Long Covid](https://arxiv.org/abs/2603.18115)

**基本信息**

- 🔗 arXiv: [`2603.18115`](https://arxiv.org/abs/2603.18115)
- 👥 作者: Jing Wang, Jie Shen, Amar Sra 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18115.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个LLM增强的、用于科学发现（医学表型分析）的计算框架。这种将大模型作为推理和假设生成引擎，与领域数据和分析流程深度结合的模式，与“化学大模型”在化学信息学中辅助结构解析、反应预测等任务的研究主题直接相关。

**📖 中文摘要**

本研究提出了一个名为“Grace Cycle”的LLM增强的计算表型分析框架，用于从纵向患者数据中发现具有临床意义的亚组。该框架迭代地整合假设生成、证据提取和特征细化。研究将其应用于13,511名长新冠参与者数据，识别出三种不同的临床表型。该框架展示了如何将大语言模型整合到一个有原则的、基于统计的流程中，用于从复杂的纵向数据中进行表型筛查。作者指出，所提出的框架是疾病无关的，为发现临床可解释的亚表型提供了一种通用方法。这项研究展示了LLM在增强科学发现流程（假设生成、特征工程）方面的潜力。这种将LLM作为智能组件嵌入到特定领域（此处为医学）数据分析管道中的范式，与利用“化学大模型”辅助化学信息学发现（例如，从质谱数据中提出假设性的分子结构或反应路径）的研究思路高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phenotypic characterization is essential for understanding heterogeneity in chronic diseases and for guiding personalized interventions. Long COVID, a complex and persistent condition, yet its clinical subphenotypes remain poorly understood. In this work, we propose an LLM-augmented computational phenotyping framework ``Grace Cycle'' that iteratively integrates hypothesis generation, evidence extraction, and feature refinement to discover clinically meaningful subgroups from longitudinal patient data. The framework identifies three distinct clinical phenotypes, Protected, Responder, and Refractory, based on 13,511 Long Covid participants. These phenotypes exhibit pronounced separation in peak symptom severity, baseline disease burden, and longitudinal dose-response patterns, with strong statistical support across multiple independent dimensions. This study illustrates how large language models can be integrated into a principled, statistically grounded pipeline for phenotypic screening from complex longitudinal data. Note that the proposed framework is disease-agnostic and offers a general approach for discovering clinically interpretable subphenotypes.

</details>

---

### 4. [A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective](https://arxiv.org/abs/2603.18126)

**基本信息**

- 🔗 arXiv: [`2603.18126`](https://arxiv.org/abs/2603.18126)
- 👥 作者: Zhengze Xiao, Xuanzhe Ding, Yuyang Lou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18126.pdf)

**💡 相关性分析**

满足标准3：论文是针对“神经网络变分蒙特卡洛”这一特定领域AI模型的综述性分析，而NNVMC是“化学大模型”在计算化学和量子化学中的一个核心应用范例。论文对该类模型的性能、瓶颈和优化方向的深入讨论，为化学领域大模型的研究提供了重要的技术背景和前瞻性视角。

**📖 中文摘要**

本综述从计算工作负载特征的角度，对神经网络变分蒙特卡洛（NNVMC）方法进行了调研。NNVMC通过将变分蒙特卡洛与富有表现力的神经网络波函数拟设相结合，已成为解决量子多体问题的一种有前景的范式。论文对四种代表性的拟设（PauliNet, FermiNet, Psiformer, Orbformer）进行了统一的性能分析，包括模型级运行时/内存趋势以及内核级行为（如算术强度、硬件利用率）。基于这些发现，论文讨论了可扩展NNVMC系统的算法-硬件协同设计意义。虽然应用领域是计算量子化学，但NNVMC本身是“化学大模型”在微观尺度（电子结构计算）上的一个典型且重要的实例。该论文系统地总结了这类特定领域大模型的计算特性和优化挑战，为理解和开发更高效的化学模拟AI模型提供了宝贵的见解和基准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Network Variational Monte Carlo (NNVMC) has emerged as a promising paradigm for solving quantum many-body problems by combining variational Monte Carlo with expressive neural-network wave-function ansätze. Although NNVMC can achieve competitive accuracy with favorable asymptotic scaling, practical deployment remains limited by high runtime and memory cost on modern graphics processing units (GPUs). Compared with language and vision workloads, NNVMC execution is shaped by physics-specific stages, including Markov-Chain Monte Carlo sampling, wave-function construction, and derivative/Laplacian evaluation, which produce heterogeneous kernel behavior and nontrivial bottlenecks. This paper provides a workload-oriented survey and empirical GPU characterization of four representative ansätze: PauliNet, FermiNet, Psiformer, and Orbformer. Using a unified profiling protocol, we analyze model-level runtime and memory trends and kernel-level behavior through family breakdown, arithmetic intensity, roofline positioning, and hardware utilization counters. The results show that end-to-end performance is often constrained by low-intensity elementwise and data-movement kernels, while the compute/memory balance varies substantially across ansätze and stages. Based on these findings, we discuss algorithm--hardware co-design implications for scalable NNVMC systems, including phase-aware scheduling, memory-centric optimization, and heterogeneous acceleration.

</details>

---

### 5. [Modeling the human lexicon under temperature variations: linguistic factors, diversity and typicality in LLM word associations](https://arxiv.org/abs/2603.18171)

**基本信息**

- 🔗 arXiv: [`2603.18171`](https://arxiv.org/abs/2603.18171)
- 👥 作者: Maria Andueza Rodriguez, Marie Candito, Richard Huyghe
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18171.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和评估大语言模型的内部语义表示（词汇联想）与人类认知的相似性和差异性。这种对模型底层语义能力的基础性研究，对于构建和理解能够在专业领域（如化学）进行准确推理的“化学大模型”至关重要，是相关主题的基础支撑研究。

**📖 中文摘要**

本研究通过比较人类和LLM生成的词汇联想，评估了模型捕捉人类词汇模式的能力。研究使用了来自SWOW数据集的英语线索-反应对，以及从三个LLM（Mistral-7B, Llama-3.1-8B, Qwen-2.5-32B）在多个温度设置下新生成的联想。研究考察了词汇因素（如词频、具体性）对线索-反应对的影响，以及LLM反应与人类反应相比的变异性和典型性。结果表明，所有模型都反映了人类在频率和具体性上的趋势，但在反应变异性和典型性上存在差异。更大的模型（如Qwen）倾向于模拟一个单一的“原型”人类参与者，产生高度典型但变异最小的反应，而较小的模型（如Mistral和Llama）产生更多变异但典型性较低的反应。温度设置进一步影响了这种权衡。这项研究揭示了人类和LLM词汇库之间的异同。理解大语言模型的内部语义表示和生成行为，是构建可靠“化学大模型”的基础。例如，在质谱结构推理中，模型需要准确关联质谱特征与化学子结构词汇，这项研究为评估和改善模型在专业领域（如化学）的语义空间质量提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) achieve impressive results in terms of fluency in text generation, yet the nature of their linguistic knowledge - in particular the human-likeness of their internal lexicon - remains uncertain. This study compares human and LLM-generated word associations to evaluate how accurately models capture human lexical patterns. Using English cue-response pairs from the SWOW dataset and newly generated associations from three LLMs (Mistral-7B, Llama-3.1-8B, and Qwen-2.5-32B) across multiple temperature settings, we examine (i) the influence of lexical factors such as word frequency and concreteness on cue-response pairs, and (ii) the variability and typicality of LLM responses compared to human responses. Results show that all models mirror human trends for frequency and concreteness but differ in response variability and typicality. Larger models such as Qwen tend to emulate a single "prototypical" human participant, generating highly typical but minimally variable responses, while smaller models such as Mistral and Llama produce more variable yet less typical responses. Temperature settings further influence this trade-off, with higher values increasing variability but decreasing typicality. These findings highlight both the similarities and differences between human and LLM lexicons, emphasizing the need to account for model size and temperature when probing LLM lexical representations.

</details>

---

### 6. [How Psychological Learning Paradigms Shaped and Constrained Artificial Intelligence](https://arxiv.org/abs/2603.18203)

**基本信息**

- 🔗 arXiv: [`2603.18203`](https://arxiv.org/abs/2603.18203)
- 👥 作者: Alex Anvi Eponon, Ildar Batyrshin, Christian E. Maldonado-Sifuentes 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18203.pdf)

**💡 相关性分析**

满足标准3：论文是一篇深刻的综述和展望性文章，它批判性地回顾了AI范式背后的心理学根源及其局限性，并提出了新的架构设计方向。这些关于如何构建具有更好推理、记忆和适应能力的AI系统的讨论，与“化学大模型”和“质谱结构推理”领域对未来模型能力（如可解释性、组合推理、持续学习）的展望高度相关，提供了重要的理论框架。

**📖 中文摘要**

本文论证了人工智能的主导范式是由心理学学习理论塑造的：行为主义启发了强化学习，认知主义催生了深度学习和记忆增强架构，建构主义影响了课程学习和组合方法。论文认为，每个AI范式不仅继承了其灵感来源的心理理论的优点，也继承了其结构局限性。论文进一步探讨了东西方对机械学习解读的跨文化差异，认为东方将记忆视为结构化、多阶段理解前奏的概念，为连接心理学理论和AI方法论提供了一座尚未充分开发的桥梁。基于对经典主义和连接主义的系统性争论的批判，本文引入了ReSynth，一个将推理（智力）、目的（身份）和知识（记忆）分离为架构独立组件的三模块框架。本文追溯了从心理学范式到AI方法的发展谱系，诊断了每个阶段继承的局限性，并认为适应性（人工智能的核心挑战）需要一种系统行为是必然结果而非偶然属性的表征架构。这篇论文从认知科学和AI历史的角度，深入探讨了构建更通用、更可解释AI的架构设计原则。这些原则对于设计面向复杂科学推理（如化学信息学、质谱解析）的“化学大模型”具有重要的理论指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The dominant paradigms of artificial intelligence were shaped by learning theories from psychology: behaviorism inspired reinforcement learning, cognitivism gave rise to deep learning and memory-augmented architectures, and constructivism influenced curriculum learning and compositional approaches. This paper argues that each AI paradigm inherited not only the strengths but the structural limitations of the psychological theory that inspired it. Reinforcement learning cannot account for the internal structure of knowledge, deep learning compresses representations into opaque parameter spaces resistant to principled update, and current integrative approaches lack a formal account of how new understanding is constructed from existing components. The paper further examines a cross-cultural divergence in the interpretation of rote learning, arguing that the Eastern conception of memorization as a structured, multi-phase precursor to understanding offers an underexploited bridge between psychological theory and AI methodology. Drawing on the systematicity debate and critique of Aizawa of both classicism and connectionism, this paper introduces ReSynth, a trimodular framework that separates reasoning (Intellect), purpose (Identity), and knowledge (Memory) as architecturally independent components. The paper traces the genealogy from psychological paradigm to AI method, diagnoses the inherited limitations at each stage, and argues that adaptability, the central challenge of artificial general intelligence requires a representational architecture in which systematic behavior is a necessary consequence rather than an accidental property.

</details>

---

### 7. [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](https://arxiv.org/abs/2603.18256)

**基本信息**

- 🔗 arXiv: [`2603.18256`](https://arxiv.org/abs/2603.18256)
- 👥 作者: Philippe Formont, Maxime Darrin, Ismail Ben Ayed 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18256.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”在分子生成和设计中的应用，提出了一个专门用于训练和评估推理LLMs进行从头分子生成的基准和数据集。

**📖 中文摘要**

本文介绍了MolRGen，一个用于训练和评估基于推理的大语言模型（LLMs）进行从头分子生成的大规模基准和数据集。该研究旨在弥补现有方法在监督需求上的不足，这些方法通常依赖于已知属性修饰的分子对，而这种监督在从头分子生成中是不可用的。MolRGen提出了一个用于评估和训练从头分子生成及性质预测模型的设定，并引入了一种新颖的多样性感知top-k评分，以同时捕捉生成分子的质量和多样性。研究展示了该设定可用于训练LLMs进行分子生成，例如通过强化学习训练了一个240亿参数的LLM，并对其性能和局限性进行了详细分析。这项工作直接针对化学信息学中的“化学大模型”主题，为使用推理LLMs进行分子设计提供了专门的训练和评估环境。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in reasoning-based large language models (LLMs) have demonstrated substantial improvements in complex problem-solving tasks. Motivated by these advances, several works have explored the application of reasoning LLMs to drug discovery and molecular design. However, most existing approaches either focus on evaluation or rely on training setups that require ground-truth labels, such as molecule pairs with known property modifications. Such supervision is unavailable in \textit{de novo} molecular generation, where the objective is to generate novel molecules that optimize a desirability score without prior knowledge of high-scoring candidates. To bridge this gap, we introduce MolRGen, a large-scale benchmark and dataset for training and evaluating reasoning-based LLMs on \textit{de novo} molecular generation. Our contributions are threefold. First, we propose a setting to evaluate and train models for \textit{de novo} molecular generation and property prediction. Second, we introduce a novel diversity-aware top-$k$ score that captures both the quality and diversity of generated molecules. Third, we show our setting can be used to train LLMs for molecular generation, training a 24B LLM with reinforcement learning, and we provide a detailed analysis of its performance and limitations.

</details>

---

### 8. [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297)

**基本信息**

- 🔗 arXiv: [`2603.18297`](https://arxiv.org/abs/2603.18297)
- 👥 作者: Zijin Gu, Tatiana Likhomanenko, Vimal Thilak 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18297.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一个名为FlowMS的新框架，专门用于从质谱数据中进行条件化的从头分子结构解析。

**📖 中文摘要**

本文提出了FlowMS，这是首个用于谱图条件化从头分子生成的离散流匹配框架。该框架通过概率空间中的迭代精炼来生成分子图，同时强制执行化学式约束，并基于预训练的公式Transformer编码器提供的谱图嵌入进行条件化。FlowMS在NPLIB1基准测试的6个指标中的5个上取得了最先进的性能，包括9.15%的top-1准确率（相对于DiffMS有9.7%的相对提升）和7.96的top-10 MCES（相对于MS-BART有4.2%的提升）。这项工作将离散流匹配确立为基于质谱的结构解析（质谱结构推理）的一个有前景的新范式，应用于代谢组学和天然产物发现领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Mixture-of-Experts (MoE) architectures enable efficient scaling by activating only a subset of parameters for each input. However, conventional MoE routing selects each layer's experts independently, creating N^L possible expert paths -- for N experts across L layers. This far exceeds typical training set sizes, leading to statistical inefficiency as the model may not learn meaningful structure over such a vast path space. To constrain it, we propose \pathmoe, which shares router parameters across consecutive layers. Experiments on 0.9B and 16B parameter models demonstrate consistent improvements on perplexity and downstream tasks over independent routing, while eliminating the need for auxiliary load balancing losses. Analysis reveals that tokens following the same path naturally cluster by linguistic function, with \pathmoe{} producing more concentrated groups, better cross-layer consistency, and greater robustness to routing perturbations. These results offer a new perspective for understanding MoE architectures through the lens of expert paths.

</details>

---

### 9. [Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information](https://arxiv.org/abs/2603.18359)

**基本信息**

- 🔗 arXiv: [`2603.18359`](https://arxiv.org/abs/2603.18359)
- 👥 作者: Shih-Heng Wang, Tiantian Feng, Aditya Kommineni 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18359.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（使用稀疏自编码器解释深度模型表征）与理解和解释“化学大模型”的内部工作机制高度相关，属于模型可解释性研究，这是大模型应用中的重要主题。

**📖 中文摘要**

本文研究了神经音频编解码器（NACs）如何编码语言学和副语言学信息，特别是口音信息。为了提高NAC表征的可解释性，作者采用了稀疏自编码器（SAEs）将密集的NAC表征分解为稀疏、可解释的激活。研究重点放在一个具有挑战性的副语言学属性——口音上，并提出了一个量化NAC可解释性的框架。作者评估了四种NAC模型在16种SAE配置下的表现，使用了相对性能指数。结果表明，DAC和SpeechTokenizer具有最高的可解释性。进一步分析揭示，声学导向的NACs主要在稀疏表征的激活幅度中编码口音信息，而语音导向的NACs则更依赖于激活位置，并且低比特率的EnCodec变体显示出更高的可解释性。这项工作虽然主要关注音频，但其核心方法（使用SAEs分解和解释深度模型表征）与化学信息学中理解“化学大模型”内部表示的需求高度相关，为模型可解释性研究提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented NACs encode accent information primarily in activation magnitudes of sparse representations, whereas phonetic-oriented NACs rely more on activation positions, and that low-bitrate EnCodec variants show higher interpretability.

</details>

---

### 10. [TENSURE: Fuzzing Sparse Tensor Compilers (Registered Report)](https://arxiv.org/abs/2603.18372)

**基本信息**

- 🔗 arXiv: [`2603.18372`](https://arxiv.org/abs/2603.18372)
- 👥 作者: Kabilan Mahathevan, Yining Zhang, Muhammad Ali Gulzar 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18372.pdf)

**💡 相关性分析**

满足标准2：论文提出的TENSURE框架是一个用于测试稀疏张量编译器的工具。稀疏张量计算是许多科学计算任务（包括潜在的化学模拟和数据处理）的基础，该工具的开发有助于保障相关计算资源的可靠性，间接支持化学信息学等领域的研究。

**📖 中文摘要**

本文提出了TENSURE，这是首个专门为测试稀疏张量编译器（STCs）而设计的可扩展黑盒模糊测试框架。STCs对于优化高维数据分析和机器学习工作负载至关重要，但由于需要直接从高级声明式规范合成复杂、不规则的控制流，因此极易出现细微的正确性缺陷。TENSURE利用爱因斯坦求和（Einsum）符号作为通用输入抽象，能够生成复杂、非常规的张量收缩运算，从而暴露STC代码生成阶段的边界情况。论文提出了一种新颖的基于约束的生成算法，保证合成内核100%的语义有效性，显著优于基线语法模糊测试器约3.3%的有效率。这项工作为稀疏编译生态系统提供了专门的测试工具。虽然论文主题是编译器测试，但其针对的“稀疏张量编译器”是支撑大规模科学计算（可能包括化学模拟和数据分析）的关键基础设施，其稳定性和正确性间接影响到依赖此类工具的科学应用，包括可能使用“化学大模型”的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Tensor Compilers (STCs) have emerged as critical infrastructure for optimizing high-dimensional data analytics and machine learning workloads. The STCs must synthesize complex, irregular control flow for various compressed storage formats directly from high-level declarative specifications, thereby making them highly susceptible to subtle correctness defects. Existing testing frameworks, which rely on mutating computation graphs restricted to a standard vocabulary of operators, fail to exercise the arbitrary loop synthesis capabilities of these compilers. Furthermore, generic grammar-based fuzzers struggle to generate valid inputs due to the strict rules governing how indices are reused across multiple tensors. In this paper, we present TENSURE, the first extensible black-box fuzzing framework specifically designed for the testing of STCs. TENSURE leverages Einstein Summation (Einsum) notation as a general input abstraction, enabling the generation of complex, unconventional tensor contractions that expose corner cases in the code-generation phases of STCs. We propose a novel constraint-based generation algorithm that guarantees 100% semantic validity of synthesized kernels, significantly outperforming the ~3.3% validity rate of baseline grammar fuzzers. To enable metamorphic testing without a trusted reference, we introduce a set of semantic-preserving mutation operators that exploit algebraic commutativity and heterogeneity in storage formats. Our evaluation on two state-of-the-art systems, TACO and Finch, reveals widespread fragility, particularly in TACO, where TENSURE exposed crashes or silent miscompilations in a majority of generated test cases. These findings underscore the critical need for specialized testing tools in the sparse compilation ecosystem.

</details>

---

### 11. [Mathematical Foundations of Deep Learning](https://arxiv.org/abs/2603.18387)

**基本信息**

- 🔗 arXiv: [`2603.18387`](https://arxiv.org/abs/2603.18387)
- 👥 作者: Xiaojing Ye
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18387.pdf)

**💡 相关性分析**

满足标准3：本书稿是关于深度学习数学基础的综述性著作，其内容直接涵盖了支撑“化学大模型”和生成模型的核心理论（如神经网络理论、生成模型、强化学习），为相关主题提供了重要的理论背景和讨论。

**📖 中文摘要**

本书稿对现代深度学习的数学原理进行了全面而严谨的阐述。内容涵盖了核心理论主题，从深度神经网络的逼近能力、最优控制和强化学习与深度学习技术相结合的理论和算法，到推动当今人工智能进步的当代生成模型。虽然这是一本涵盖广泛深度学习数学基础的书籍，但其内容直接涉及构建和理解“大模型”（包括生成模型）的理论基石。对于在“化学信息学”领域致力于开发和理解“化学大模型”的研究人员而言，掌握这些数学基础至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This draft book offers a comprehensive and rigorous treatment of the mathematical principles underlying modern deep learning. The book spans core theoretical topics, from the approximation capabilities of deep neural networks, the theory and algorithms of optimal control and reinforcement learning integrated with deep learning techniques, to contemporary generative models that drive today's advances in artificial intelligence.

</details>

---

### 12. [Seeking Universal Shot Language Understanding Solutions](https://arxiv.org/abs/2603.18448)

**基本信息**

- 🔗 arXiv: [`2603.18448`](https://arxiv.org/abs/2603.18448)
- 👥 作者: Haoxin Liu, Harshavardhan Kamarthi, Zhiyuan Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18448.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发通用的视觉-语言模型（VLMs）解决方案来处理复杂的镜头语言理解任务。这直接围绕“化学大模型”这一广义的、旨在构建通用领域或多模态基础模型的研究主题。

**📖 中文摘要**

论文《Seeking Universal Shot Language Understanding Solutions》聚焦于镜头语言理解（SLU），这是一个与视觉-语言模型（VLMs）和通用视觉理解高度相关的领域。虽然论文主题是电影分析，但其核心是开发通用的、可训练的视觉-语言模型解决方案（如UniShot和AgentShots），以处理复杂的、多维度（包括构图、运动、灯光等）的视觉理解任务。这项工作直接涉及构建和训练用于复杂视觉场景理解和推理的“大模型”，其方法论和提出的解决方案（通用专家模型与专家集群）与“化学大模型”在构建通用、可适应特定领域的多模态基础模型这一核心主题上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Shot language understanding (SLU) is crucial for cinematic analysis but remains challenging due to its diverse cinematographic dimensions and subjective expert judgment. While vision-language models (VLMs) have shown strong ability in general visual understanding, recent studies reveal judgment discrepancies between VLMs and film experts on SLU tasks. To address this gap, we introduce SLU-SUITE, a comprehensive training and evaluation suite containing 490K human-annotated QA pairs across 33 tasks spanning six film-grounded dimensions. Using SLU-SUITE, we originally observe two insights into VLM-based SLU from: the model side, which diagnoses key bottlenecks of modules; the data side, which quantifies cross-dimensional influences among tasks. These findings motivate our universal SLU solutions from two complementary paradigms: UniShot, a balanced one-for-all generalist trained via dynamic-balanced data mixing, and AgentShots, a prompt-routed expert cluster that maximizes peak dimension performance. Extensive experiments show that our models outperform task-specific ensembles on in-domain tasks and surpass leading commercial VLMs by 22% on out-of-domain tasks.

</details>

---

### 13. [Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images](https://arxiv.org/abs/2603.18461)

**基本信息**

- 🔗 arXiv: [`2603.18461`](https://arxiv.org/abs/2603.18461)
- 👥 作者: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18461.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文研究如何从病理图像中预测基因表达，这是一个典型的化学信息学/生物信息学问题，涉及从视觉数据推理分子特征。2) 数据资源相关：论文的方法论核心是利用公开可用的单细胞RNA测序数据集来构建细胞类型原型，这为相关研究提供了数据整合和利用的思路与潜在资源。

**📖 中文摘要**

论文《Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images》提出了一种利用单细胞RNA测序数据（scRNA-seq）构建细胞类型原型，并基于此从病理图像中估计基因表达谱的神经网络方法（CPNN）。该方法的核心创新在于将生物学知识（细胞类型特异的基因表达模式）整合到深度学习模型中，以提升从组织图像预测分子特征的准确性和可解释性。这项工作位于生物信息学、计算病理学和化学信息学的交叉领域，因为它涉及从高维图像数据中推断化学/分子层面的信息（基因表达）。其方法论——利用外部生物数据集（scRNA-seq）来指导和正则化模型预测——为“化学大模型”如何整合领域特定知识和数据资源提供了范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Estimating slide- and patch-level gene expression profiles from pathology images enables rapid and low-cost molecular analysis with broad clinical impact. Despite strong results, existing approaches treat gene expression as a mere slide- or spot-level signal and do not incorporate the fact that the measured expression arises from the aggregation of underlying cell-level expression. To explicitly introduce this missing cell-resolved guidance, we propose a Cell-type Prototype-informed Neural Network (CPNN) that leverages publicly available single-cell RNA-sequencing datasets. Since single-cell measurements are noisy and not paired with histology images, we first estimate cell-type prototypes-mean expression profiles that reflect stable gene-gene co-variation this http URL then learns cell-type compositional weights directly from images and models the relationship between prototypes and observed bulk or spatial expression, providing a biologically grounded and structurally regularized prediction framework. We evaluate CPNN on three slide-level datasets and three patch-level spatial transcriptomics datasets. Across all settings, CPNN achieves the highest performance in terms of Spearman correlation. Moreover, by visualizing the inferred compositional weights, our framework provides interpretable insights into which cell types drive the predicted expression. Code is publicly available at this https URL .

</details>

---

### 14. [Cognitive Mismatch in Multimodal Large Language Models for Discrete Symbol Understanding](https://arxiv.org/abs/2603.18472)

**基本信息**

- 🔗 arXiv: [`2603.18472`](https://arxiv.org/abs/2603.18472)
- 👥 作者: Yinghui Li, Jiayi Kuang, Peng Xing 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18472.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕多模态大语言模型对包括“化学结构”在内的离散符号的理解能力进行评估和分析。这直接关联到“化学大模型”主题中关于模型如何处理和推理化学领域特定符号表示的关键问题。

**📖 中文摘要**

论文《Cognitive Mismatch in Multimodal Large Language Models for Discrete Symbol Understanding》系统评估了多模态大语言模型（MLLMs）在理解离散符号（如数学公式、化学结构、语言字符）方面的能力。论文专门将“化学”列为评估的五个关键领域之一，旨在检验MLLMs是否能够真正“感知和理解”化学结构式等符号化语言。这项工作直接触及了“化学大模型”的一个核心挑战：即大模型在处理化学领域特有的、精确的符号表示（如分子结构）时的能力与局限性。论文构建的基准和发现（模型在基础符号识别上失败却在复杂推理上成功）为未来开发更强大的、真正理解化学符号的AI系统指明了方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Multimodal Large Language Models (MLLMs) have achieved remarkable success in interpreting natural scenes, their ability to process discrete symbols -- the fundamental building blocks of human cognition -- remains a critical open question. Unlike continuous visual data, symbols such as mathematical formulas, chemical structures, and linguistic characters require precise, deeper interpretation. This paper introduces a comprehensive benchmark to evaluate how top-tier MLLMs navigate these "discrete semantic spaces" across five domains: language, culture, mathematics, physics, and chemistry. Our investigation uncovers a counterintuitive phenomenon: models often fail at basic symbol recognition yet succeed in complex reasoning tasks, suggesting they rely on linguistic probability rather than true visual perception. By exposing this "cognitive mismatch", we highlight a significant gap in current AI capabilities: the struggle to truly perceive and understand the symbolic languages that underpin scientific discovery and abstract thought. This work offers a roadmap for developing more rigorous, human-aligned intelligent systems.

</details>

---

### 15. [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505)

**基本信息**

- 🔗 arXiv: [`2603.18505`](https://arxiv.org/abs/2603.18505)
- 👥 作者: Jingzhi Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18505.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对人工智能在蛋白质科学中应用的综述，其中包含了对生成式模型、多模态学习等重要方向的深入讨论，这些内容与构建和理解“化学大模型”密切相关，提供了重要的领域背景和未来展望。

**📖 中文摘要**

论文《From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions》是一篇关于人工智能驱动蛋白质科学发展的综述。它系统性地回顾了该领域从静态结构预测向生成动态构象、多模态表示和复杂生物分子相互作用建模的范式转变。论文涵盖了统一多模态表示、生成式框架（如扩散模型）、蛋白质-配体相互作用预测等前沿方向。这篇综述全面讨论了AI在化学和生物学核心问题（蛋白质）上的应用演进，与“化学大模型”主题高度契合，因为它探讨的正是如何构建能够理解、模拟和生成复杂化学/生物分子系统的大规模AI模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular interactions. This review systematically examines the paradigm shift in AI driven protein science across five interconnected dimensions: unified multimodal representations that integrate sequences, geometries, and textual knowledge; refinement of static prediction through MSA free architectures and all atom complex modeling; generative frameworks, including diffusion models and flow matching, that capture conformational distributions consistent with thermodynamic ensembles; prediction of heterogeneous interactions spanning protein ligand, protein nucleic acid, and protein protein complexes; and functional inference of fitness landscapes, mutational effects, and text guided property prediction. We critically analyze current bottlenecks, including data distribution biases, limited mechanistic interpretability, and the disconnect between geometric metrics and biophysical reality, while identifying future directions toward physically consistent generative models, multimodal foundation architectures, and experimental closed loop systems. This methodological transformation marks artificial intelligence's transition from a structural analysis tool into a universal simulator capable of understanding and ultimately rewriting the dynamic language of life.

</details>

---

### 16. [SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks](https://arxiv.org/abs/2603.18548)

**基本信息**

- 🔗 arXiv: [`2603.18548`](https://arxiv.org/abs/2603.18548)
- 👥 作者: Amanda A. Howard, Nicholas Zolman, Bruno Jacob 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18548.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、可解释的机器学习框架（SINDy-KANs），用于从数据中发现稀疏的动力学方程。这在化学信息学和计算化学中是一个重要课题，例如从光谱或质谱时间序列数据中推断反应机理或动力学模型，与“化学大模型”中关注模型可解释性和从数据学习规律的主题相关。

**📖 中文摘要**

论文《SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks》提出了一种结合Kolmogorov-Arnold网络（KANs）和稀疏识别非线性动力学（SINDy）的新方法，用于从数据中发现可解释的、稀疏的动力学方程。虽然论文的应用示例包括一般动力系统，但SINDy方法在化学动力学、系统生物学等领域有广泛应用，用于从时间序列数据中推断反应速率方程等。该方法的核心目标是提升机器学习模型（KANs）的可解释性和稀疏性，这与“化学大模型”研究中追求模型可解释性、以及从数据中挖掘物理/化学规律的目标一致。论文为如何将符号回归与神经网络结合提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method to a number of symbolic regression tasks, including dynamical systems, to show accurate equation discovery across a range of systems.

</details>

---

### 17. [CAPSUL: A Comprehensive Human Protein Benchmark for Subcellular Localization](https://arxiv.org/abs/2603.18571)

**基本信息**

- 🔗 arXiv: [`2603.18571`](https://arxiv.org/abs/2603.18571)
- 👥 作者: Yicheng Hu, Xinyu Lin, Shulin Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18571.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个包含3D结构信息和详细亚细胞定位注释的新基准数据集CAPSUL。这为开发和评估“化学大模型”（特别是那些能够处理蛋白质结构数据的模型）提供了一个重要的数据资源和测试平台。

**📖 中文摘要**

论文《CAPSUL: A Comprehensive Human Protein Benchmark for Subcellular Localization》引入了一个新的综合性人类蛋白质基准数据集（CAPSUL），专门用于蛋白质亚细胞定位任务。该数据集的关键创新在于整合了蛋白质的3D结构信息与精细的亚细胞定位注释。论文评估了多种基于序列和基于结构的模型，强调了结构特征在此任务中的重要性。这项工作为“化学大模型”在化学生物学领域的应用提供了一个高质量、结构信息丰富的基准测试平台。蛋白质亚细胞定位是药物靶点识别和功能注释的关键，该数据集和评估框架可用于开发和验证能够融合多模态信息（序列、结构、文本）的大规模模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Subcellular localization is a crucial biological task for drug target identification and function annotation. Although it has been biologically realized that subcellular localization is closely associated with protein structure, no existing dataset offers comprehensive 3D structural information with detailed subcellular localization annotations, thus severely hindering the application of promising structure-based models on this task. To address this gap, we introduce a new benchmark called $\mathbf{CAPSUL}$, a $\mathbf{C}$omprehensive hum$\mathbf{A}$n $\mathbf{P}$rotein benchmark for $\mathbf{SU}$bcellular $\mathbf{L}$ocalization. It features a dataset that integrates diverse 3D structural representations with fine-grained subcellular localization annotations carefully curated by domain experts. We evaluate this benchmark using a variety of state-of-the-art sequence-based and structure-based models, showcasing the importance of involving structural features in this task. Furthermore, we explore reweighting and single-label classification strategies to facilitate future investigation on structure-based methods for this task. Lastly, we showcase the powerful interpretability of structure-based methods through a case study on the Golgi apparatus, where we discover a decisive localization pattern $\alpha$-helix from attention mechanisms, demonstrating the potential for bridging the gap with intuitive biological interpretability and paving the way for data-driven discoveries in cell biology.

</details>

---

### 18. [Elastic Weight Consolidation Done Right for Continual Learning](https://arxiv.org/abs/2603.18596)

**基本信息**

- 🔗 arXiv: [`2603.18596`](https://arxiv.org/abs/2603.18596)
- 👥 作者: Xuan Liu, Xiaobin Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18596.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕模型权重重要性估计和持续学习优化，这是构建和优化“化学大模型”等专业领域大模型的关键底层技术之一。论文提出的Logits Reversal操作旨在解决梯度消失和冗余保护问题，这对于训练稳定、高效且能持续进化的化学信息学大模型具有直接的方法论参考价值。

**📖 中文摘要**

本文对持续学习中的权重正则化方法进行了系统性分析，重点关注了基于梯度的权重重要性估计。论文的核心是分析Elastic Weight Consolidation (EWC)及其变体在估计权重重要性时存在的根本性错位问题，并提出了Logits Reversal (LR)操作来修正EWC的重要性估计。虽然论文主要关注通用机器学习模型的持续学习，但其核心方法——通过分析模型梯度（Fisher信息矩阵）来理解和修正模型参数的重要性——与构建和优化“化学大模型”的底层技术（如模型架构设计、参数重要性评估、防止灾难性遗忘）在方法论上高度相关。该研究为如何设计、训练和微调能够持续学习新知识而不遗忘旧知识的大模型提供了重要的技术见解和解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight regularization methods in continual learning (CL) alleviate catastrophic forgetting by assessing and penalizing changes to important model weights. Elastic Weight Consolidation (EWC) is a foundational and widely used approach within this framework that estimates weight importance based on gradients. However, it has consistently shown suboptimal performance. In this paper, we conduct a systematic analysis of importance estimation in EWC from a gradient-based perspective. For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios. Our analysis also reveals that Memory Aware Synapses (MAS), a variant of EWC, imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection. Consequently, both EWC and its variants exhibit fundamental misalignments in estimating weight importance, leading to inferior performance. To tackle these issues, we propose the Logits Reversal (LR) operation, a simple yet effective modification that rectifies EWC's importance estimation. Specifically, reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection. Extensive experiments across various CL tasks and datasets show that the proposed method significantly outperforms existing EWC and its variants. Therefore, we refer to it as EWC Done Right (EWC-DR).

</details>

---

### 19. [DiscoPhon: Benchmarking the Unsupervised Discovery of Phoneme Inventories With Discrete Speech Units](https://arxiv.org/abs/2603.18612)

**基本信息**

- 🔗 arXiv: [`2603.18612`](https://arxiv.org/abs/2603.18612)
- 👥 作者: Maxime Poli, Manel Khentout, Angelo Ortiz Tandazo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18612.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究主题是从数据（语音）中无监督推理出底层结构（音素），这与“质谱结构推理”从质谱数据推理分子结构的核心任务在方法论和问题范式上直接相关。

**📖 中文摘要**

本文介绍了DiscoPhon，一个用于评估从离散语音单元中无监督发现音素的多语言基准。该基准涵盖6种开发语言和6种测试语言，旨在评估系统在仅给定10小时未见语言语音的情况下，产生可映射到预定义音素清单的离散单元的能力。论文提供了基于多语言HuBERT和SpidR的预训练基线，并展示了当前模型中存在足够的音素信息。这项工作专注于从数据（语音信号）中无监督地推导出结构化的表示（音素清单），其核心任务——从复杂、高维的原始数据中推理出底层化学结构——与“质谱结构推理”的研究主题在问题范式上高度相似。质谱结构推理同样旨在从高维、复杂的质谱数据中推断出未知化合物的分子结构，两者都涉及从信号到符号化表示的映射和推理过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce DiscoPhon, a multilingual benchmark for evaluating unsupervised phoneme discovery from discrete speech units. DiscoPhon covers 6 dev and 6 test languages, chosen to span a wide range of phonemic contrasts. Given only 10 hours of speech in a previously unseen language, systems must produce discrete units that are mapped to a predefined phoneme inventory, through either a many-to-one or a one-to-one assignment. The resulting sequences are evaluated for unit quality, recognition and segmentation. We provide four pretrained multilingual HuBERT and SpidR baselines, and show that phonemic information is available enough in current models for derived units to correlate well with phonemes, though with variations across languages.

</details>

---

### 20. [GEAR: Geography-knowledge Enhanced Analog Recognition Framework in Extreme Environments](https://arxiv.org/abs/2603.18626)

**基本信息**

- 🔗 arXiv: [`2603.18626`](https://arxiv.org/abs/2603.18626)
- 👥 作者: Zelin Liu, Bocheng Li, Yuling Zhou 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18626.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文提出的MSG-Net图神经网络方法可用于处理分子图等结构化化学数据，与化学大模型的核心技术相关。2) 论文发布了一个专家标注的地形相似性数据集，其构建理念和方法可用于创建化学信息学或质谱分析领域用于模型训练和评估的专用数据集。

**📖 中文摘要**

本文提出了GEAR框架，用于从青藏高原高效检索马里亚纳海沟的地形结构同源体。该框架采用三阶段流程，并设计了一个基于图神经网络的形态集成孪生图网络(MSG-Net)进行精细识别。论文的核心是开发一种能够从大规模地理数据中识别复杂结构相似性的AI模型。虽然应用领域是地理学，但其核心技术——使用图神经网络（MSG-Net）处理基于形态学度量的结构化数据，并学习用于相似性检索的表示——与“化学大模型”和“质谱结构推理”中处理分子图、光谱图等结构化化学数据，并进行相似性搜索、性质预测或结构分类的任务在技术路径上高度一致。论文释放的专家标注地形相似性数据集也符合构建领域专用模型对高质量数据的需求。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Mariana Trench and the Qinghai-Tibet Plateau exhibit significant similarities in geological origins and microbial metabolic functions. Given that deep-sea biological sampling faces prohibitive costs, recognizing structurally homologous terrestrial analogs of the Mariana Trench on the Qinghai-Tibet Plateau is of great significance. Yet, no existing model adequately addresses cross-domain topographic similarity retrieval, either neglecting geographical knowledge or sacrificing computational efficiency. To address these challenges, we present \underline{\textbf{G}}eography-knowledge \underline{\textbf{E}}nhanced \underline{\textbf{A}}nalog \underline{\textbf{R}}ecognition (\textbf{GEAR}) Framework, a three-stage pipeline designed to efficiently retrieve analogs from 2.5 million square kilometers of the Qinghai-Tibet Plateau: (1) Skeleton guided Screening and Clipping: Recognition of candidate valleys and initial screening based on size and linear morphological criteria. (2) Physics aware Filtering: The Topographic Waveform Comparator (TWC) and Morphological Texture Module (MTM) evaluate the waveform and texture and filter out inconsistent candidate valleys. (3) Graph based Fine Recognition: We design a \underline{\textbf{M}}orphology-integrated \underline{\textbf{S}}iamese \underline{\textbf{G}}raph \underline{\textbf{N}}etwork (\textbf{MSG-Net}) based on geomorphological metrics. Correspondingly, we release an expert-annotated topographic similarity dataset targeting tectonic collision zones. Experiments demonstrate the effectiveness of every stage. Besides, MSG-Net achieved an F1-Score 1.38 percentage points higher than the SOTA baseline. Using features extracted by MSG-Net, we discovered a significant correlation with biological data, providing evidence for future biological analysis.

</details>

---

### 21. [Enhancing Multi-Corpus Training in SSL-Based Anti-Spoofing Models: Domain-Invariant Feature Extraction](https://arxiv.org/abs/2603.18657)

**基本信息**

- 🔗 arXiv: [`2603.18657`](https://arxiv.org/abs/2603.18657)
- 👥 作者: Anh-Tuan Dao, Driss Matrouf, Mickael Rouvier 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18657.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容——通过域不变学习提升模型在跨数据集（跨域）任务上的泛化能力——直接关系到如何构建能够泛化到不同仪器、实验室和实验条件的鲁棒性“化学大模型”和“质谱结构推理”模型。

**📖 中文摘要**

本文研究了语音欺骗检测中多语料库训练的性能不稳定性问题，并提出了一种不变域特征提取(IDFE)框架。该框架采用多任务学习和梯度反转层，以最小化学到的嵌入中的语料库特定信息，从而提高模型在不同数据集上的泛化能力和鲁棒性。这项工作的核心是解决机器学习模型（特别是涉及信号处理的模型）在跨域数据上的泛化挑战。这对于“化学大模型”和“质谱结构推理”至关重要，因为化学数据（如来自不同仪器、实验条件的质谱）同样存在显著的域差异（如仪器偏差、采样条件变化）。论文提出的域不变表示学习方法，可以直接应用于构建对实验条件变化具有鲁棒性的质谱分析模型或通用的化学表示学习模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The performance of speech spoofing detection often varies across different training and evaluation corpora. Leveraging multiple corpora typically enhances robustness and performance in fields like speaker recognition and speech recognition. However, our spoofing detection experiments show that multi-corpus training does not consistently improve performance and may even degrade it. We hypothesize that dataset-specific biases impair generalization, leading to performance instability. To address this, we propose an Invariant Domain Feature Extraction (IDFE) framework, employing multi-task learning and a gradient reversal layer to minimize corpus-specific information in learned embeddings. The IDFE framework reduces the average equal error rate by 20% compared to the baseline, assessed across four varied datasets.

</details>

---

### 22. [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660)

**基本信息**

- 🔗 arXiv: [`2603.18660`](https://arxiv.org/abs/2603.18660)
- 👥 作者: Peihang Wu, Zehong Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18660.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对多模态计算病理学的综述，其中包含多个重要章节（如自监督表示学习、令牌压缩、小样本学习、多智能体推理）深入讨论了与“化学大模型”（处理高维数据、小样本学习）和“质谱结构推理”（可解释推理、多模态融合）直接相关的关键技术和方法论。

**📖 中文摘要**

本文全面综述了多模态计算病理学的最新进展，系统分析了四个研究方向，包括WSI的自监督表示学习和结构感知令牌压缩、多模态数据生成与增强、参数高效适应和推理增强的小样本学习，以及用于可信诊断的多智能体协同推理。综述特别探讨了令牌压缩如何实现跨尺度建模，以及多智能体机制如何模拟病理学家在不同放大倍数下的“思维链”以实现不确定性感知的证据融合。这篇综述广泛涵盖了与“化学大模型”和“质谱结构推理”高度相关的多个前沿技术主题，例如：处理高维、高分辨率数据（如质谱成像）的表示学习和压缩技术；用于增强小样本场景下模型性能的适应方法；以及实现可解释、可信AI决策的推理框架。这些技术可直接迁移至化学信息学领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Whole slide imaging (WSI) has transformed digital pathology by enabling computational analysis of gigapixel histopathology images. Recent foundation model advances have accelerated progress in computational pathology, facilitating joint reasoning across pathology images, clinical reports, and structured data. Despite this progress, challenges remain: the extreme resolution of WSIs creates computational hurdles for visual learning; limited expert annotations constrain supervised approaches; integrating multimodal information while preserving biological interpretability remains difficult; and the opacity of modeling ultra-long visual sequences hinders clinical transparency. This review comprehensively surveys recent advances in multimodal computational pathology. We systematically analyze four research directions: (1) self-supervised representation learning and structure-aware token compression for WSIs; (2) multimodal data generation and augmentation; (3) parameter-efficient adaptation and reasoning-enhanced few-shot learning; and (4) multi-agent collaborative reasoning for trustworthy diagnosis. We specifically examine how token compression enables cross-scale modeling and how multi-agent mechanisms simulate a pathologist's "Chain of Thought" across magnifications to achieve uncertainty-aware evidence fusion. Finally, we discuss open challenges and argue that future progress depends on unified multimodal frameworks integrating high-resolution visual data with clinical and biomedical knowledge to support interpretable and safe AI-assisted diagnosis.

</details>

---

### 23. [STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation](https://arxiv.org/abs/2603.18688)

**基本信息**

- 🔗 arXiv: [`2603.18688`](https://arxiv.org/abs/2603.18688)
- 👥 作者: Chen Zhang, Liwei Liu, Jun Tao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18688.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个用于科学时间序列的统一编码器预训练框架，其技术方案（跨域蒸馏、处理异构数据、学习通用表示）直接适用于构建融合多模态化学数据、具备强大泛化能力的“化学大模型”。

**📖 中文摘要**

本文提出了STEP框架，一个通过跨域蒸馏进行科学时间序列编码器预训练的框架。STEP引入自适应分块处理极端长度序列，采用统计补偿方案适应不同的数值尺度，并利用跨域蒸馏整合来自多个相关领域（如音频、通用时间序列、脑信号）基础模型的知识到一个统一的编码器中。该研究专注于为科学时间序列学习通用、可迁移的特征表示。其核心技术——整合多源预训练模型知识、处理异构和稀疏数据、学习领域不变的表示——与构建“化学大模型”面临的核心挑战高度一致。化学数据（如各种光谱、色谱、分子描述符）同样是异构、多尺度且标注稀缺的。STEP框架中跨域蒸馏和统一编码器的设计思想，为构建能够融合多种化学数据模态、并具备强大泛化能力的化学基础模型提供了可行的技术路线参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientific tasks and their complementary strengths. Based on this observation, we propose STEP, a Scientific Time Series Encoder Pretraining framework via cross domain distillation. STEP introduces adaptive patching to handle extreme-length sequences and a statistics compensation scheme to accommodate diverse numerical scales. It further leverages cross-domain distillation to integrate knowledge from multiple foundation models into a unified encoder. By combining complementary representations across different domains, STEP learns general-purpose and transferable features tailored for scientific signals. Experiments on seven scientific time series tasks demonstrate that STEP provides both an effective structure and an effective pretraining paradigm, taking a STEP toward scientific time series representation learning.

</details>

---

### 24. [CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks](https://arxiv.org/abs/2603.18736)

**基本信息**

- 🔗 arXiv: [`2603.18736`](https://arxiv.org/abs/2603.18736)
- 👥 作者: Hao Wang, Licheng Pan, Zhichao Chen 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18736.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容——从有噪声和偏差的观测数据中学习无偏的奖励模型——直接关系到如何利用现实世界中不完美、有偏的化学实验数据来训练或优化“化学大模型”，特别是在涉及强化学习或偏好学习的场景下。

**📖 中文摘要**

本文提出了CausalRM，一个基于因果理论的奖励建模框架，旨在从观测性用户反馈（如点击、复制、点赞）中学习无偏的奖励模型，以替代RLHF中昂贵的人工标注反馈。CausalRM通过显式建模标注错误生成过程来应对观测反馈的噪声问题，并使用倾向得分对训练样本重新加权以消除用户偏好偏差。该研究专注于从有噪声和偏差的观测数据中学习准确的奖励信号，这对于在现实世界场景中训练和微调“化学大模型”具有重要意义。例如，在化学领域，实验数据可能带有仪器误差或研究人员的选择性报告偏差。CausalRM框架中处理噪声和偏差的方法，为利用不完美的化学实验数据或文献数据来训练或优化模型（如用于反应预测或性质优化的强化学习模型）提供了理论工具和实践思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite the success of reinforcement learning from human feedback (RLHF) in aligning language models, current reward modeling heavily relies on experimental feedback data collected from human annotators under controlled and costly conditions. In this work, we introduce observational reward modeling -- learning reward models with observational user feedback (e.g., clicks, copies, and upvotes) -- as a scalable and cost-effective alternative. We identify two fundamental challenges in this setting: (1) observational feedback is noisy due to annotation errors, which deviates it from true user preference; (2) observational feedback is biased by user preference, where users preferentially provide feedback on responses they feel strongly about, which creats a distribution shift between training and inference data. To address these challenges, we propose CausalRM, a causal-theoretic reward modeling framework that aims to learn unbiased reward models from observational feedback. To tackle challenge (1), CausalRM introduces a noise-aware surrogate loss term that is provably equivalent to the primal loss under noise-free conditions by explicitly modeling the annotation error generation process. To tackle challenge (2), CausalRM uses propensity scores -- the probability of a user providing feedback for a given response -- to reweight training samples, yielding a loss function that eliminates user preference bias. Extensive experiments across diverse LLM backbones and benchmark datasets validate that CausalRM effectively learns accurate reward signals from noisy and biased observational feedback and delivers substantial performance improvements on downstream RLHF tasks -- including a 49.2% gain on WildGuardMix and a 32.7% improvement on HarmBench. Code is available on our project website.

</details>

---

### 25. [Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN](https://arxiv.org/abs/2603.18766)

**基本信息**

- 🔗 arXiv: [`2603.18766`](https://arxiv.org/abs/2603.18766)
- 👥 作者: Marcio Augusto Sampaio, Paulo Henrique Ranazzi, Martin Julian Blunt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18766.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及使用深度生成模型（VAE-GAN）处理非高斯分布参数并与物理模型结合，这直接关联到“化学大模型”中分子生成、性质预测等任务的核心技术，以及将数据驱动模型与物理化学原理相结合的前沿方向。

**📖 中文摘要**

本文提出将变分自编码生成对抗网络(VAE-GAN)集成到集合平滑器多重数据同化(ESMDA)方法中，用于油藏模拟中的历史拟合。该方法旨在结合VAE在数据同化方面的优势和GAN在生成地质真实模型方面的优势，实现对非高斯分布油藏属性（如渗透率）的参数化。其核心创新在于使用深度生成模型（VAE-GAN）将复杂的、非高斯的物理场参数映射到更适合数据同化算法的潜在空间。这项技术与“化学大模型”和“质谱结构推理”高度相关：1）在化学领域，分子结构、材料性质等也常服从复杂、非高斯的分布。VAE-GAN等生成模型是构建化学大模型（如分子生成模型）的核心组件。2）该研究展示了如何将生成模型与物理驱动（油藏模拟器）的数据同化框架结合，这为在化学中结合生成模型与物理/化学原理（如将分子生成模型与量子化学计算结合）提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Currently, the methods called Iterative Ensemble Smoothers, especially the method called Ensemble Smoother with Multiple Data Assimilation (ESMDA) can be considered state-of-the-art for history matching in petroleum reservoir simulation. However, this approach has two important limitations: the use of an ensemble with finite size to represent the distributions and the Gaussian assumption in parameter and data uncertainties. This latter is particularly important because many reservoir properties have non-Gaussian distributions. Parameterization involves mapping non-Gaussian parameters to a Gaussian field before the update and then mapping them back to the original domain to forward the ensemble through the reservoir simulator. A promising approach to perform parameterization is through deep learning models. Recent studies have shown that Generative Adversarial Networks (GAN) performed poorly concerning data assimilation, but generated more geologically plausible realizations of the reservoir, while the Variational Autoencoder (VAE) performed better than the GAN in data assimilation, but generated less geologically realistic models. This work is innovative in combining the strengths of both to implement a deep learning model called Variational Autoencoder Generative Adversarial Network (VAE-GAN) integrated with ESMDA. The methodology was applied in two case studies, one case being categorical and the other with continuous values of permeability. Our findings demonstrate that by applying the VAE-GAN model we can obtain high quality reservoir descriptions (just like GANs) and a good history matching on the production curves (just like VAEs) simultaneously.

</details>

---

### 26. [dTRPO: Trajectory Reduction in Policy Optimization of Diffusion Large Language Models](https://arxiv.org/abs/2603.18806)

**基本信息**

- 🔗 arXiv: [`2603.18806`](https://arxiv.org/abs/2603.18806)
- 👥 作者: Wenxuan Zhang, Lemeng Wu, Changsheng Zhao 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散大语言模型（dLLMs）的策略优化，而扩散大语言模型是构建“化学大模型”（用于分子生成、反应预测等）的关键技术路径之一，因此论文主题直接相关。

**📖 中文摘要**

本文提出了一种名为dTRPO（轨迹缩减策略优化）的新方法，旨在改进扩散大语言模型（dLLMs）的策略优化。论文的核心是解决dLLMs与人类偏好对齐的挑战，通过理论证明和算法设计，显著降低了轨迹概率计算的开销，从而实现了可扩展的离线策略训练。该方法在指令遵循和推理基准测试中，显著提升了7B参数dLLMs的核心性能，在STEM任务上获得高达9.6%的提升，在代码任务上提升4.3%，在指令遵循任务上提升3.0%。论文的研究内容直接针对“化学大模型”这一主题，因为扩散大语言模型是当前构建化学领域大模型（如分子生成、性质预测）的一种重要前沿范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion Large Language Models (dLLMs) introduce a new paradigm for language generation, which in turn presents new challenges for aligning them with human preferences. In this work, we aim to improve the policy optimization for dLLMs by reducing the cost of the trajectory probability calculation, thereby enabling scaled-up offline policy training. We prove that: (i) under reference policy regularization, the probability ratio of the newly unmasked tokens is an unbiased estimate of that of intermediate diffusion states, and (ii) the probability of the full trajectory can be effectively estimated with a single forward pass of a re-masked final state. By integrating these two trajectory reduction strategies into a policy optimization objective, we propose Trajectory Reduction Policy Optimization (dTRPO). We evaluate dTRPO on 7B dLLMs across instruction-following and reasoning benchmarks. Results show that it substantially improves the core performance of state-of-the-art dLLMs, achieving gains of up to 9.6% on STEM tasks, up to 4.3% on coding tasks, and up to 3.0% on instruction-following tasks. Moreover, dTRPO exhibits strong training efficiency due to its offline, single-forward nature, and achieves improved generation efficiency through high-quality outputs.

</details>

---

### 27. [Seasoning Generative Models for a Generalization Aftertaste](https://arxiv.org/abs/2603.18817)

**基本信息**

- 🔗 arXiv: [`2603.18817`](https://arxiv.org/abs/2603.18817)
- 👥 作者: Hisham Husain, Valentin De Bortoli, Richard Nock
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18817.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型（特别是扩散模型）的泛化理论与精炼方法。生成模型是构建“化学大模型”的核心技术组件，因此论文的主题与化学信息学中构建大模型的基础理论直接相关。

**📖 中文摘要**

本文研究了一种利用判别器来训练或微调生成模型的通用框架。论文扩展了与f-散度相关的强对偶性结果，提出了一种判别器引导的“精炼”方法，可以应用于任何生成模型。理论分析表明，经过精炼的生成模型在泛化能力上相比未精炼的版本有可证明的提升。该框架包含了一种已显示出巨大经验成功的基于分数的扩散方法，并为其泛化保证提供了理论验证。论文的工作为理解生成模型的泛化性做出了贡献。虽然论文本身不专门针对化学或质谱，但其研究的核心——生成模型（特别是扩散模型）的精炼与泛化理论——是构建高性能“化学大模型”（如用于分子设计、光谱预测的生成模型）的重要理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The use of discriminators to train or fine-tune generative models has proven to be a rather successful framework. A notable example is Generative Adversarial Networks (GANs) that minimize a loss incurred by training discriminators along with other paradigms that boost generative models via discriminators that satisfy weak learner constraints. More recently, even diffusion models have shown advantages with some kind of discriminator guidance. In this work, we extend a strong-duality result related to $f$-divergences which gives rise to a discriminator-guided recipe that allows us to \textit{refine} any generative model. We then show that the refined generative models provably improve generalization, compared to its non-refined counterpart. In particular, our analysis reveals that the gap in generalization is improved based on the Rademacher complexity of the discriminator set used for refinement. Our recipe subsumes a recently introduced score-based diffusion approach (Kim et al., 2022) that has shown great empirical success, however allows us to shed light on the generalization guarantees of this method by virtue of our analysis. Thus, our work provides a theoretical validation for existing work, suggests avenues for new algorithms, and contributes to our understanding of generalization in generative models at large.

</details>

---

### 28. [Pore-scale modeling of capillary-driven binder migration during battery electrode drying](https://arxiv.org/abs/2603.18860)

**基本信息**

- 🔗 arXiv: [`2603.18860`](https://arxiv.org/abs/2603.18860)
- 👥 作者: Marcel Weichel, Martin Reder, Gerit Mühlberg 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18860.pdf)

**💡 相关性分析**

满足标准1：论文应用计算建模和模拟（化学信息学的核心方法）来研究电池电极制造中的物理化学过程。虽然焦点是过程模拟而非大模型或质谱，但其方法论和问题域（电化学材料）与化学信息学高度相关，可视为该领域内一个重要的应用研究方向。

**📖 中文摘要**

本文提出了一个空间分辨的孔隙尺度连续介质模型，用于模拟钠离子电池硬碳电极干燥过程中，由毛细力驱动的粘结剂迁移。该模型明确描述了孔隙排空过程中的毛细驱动传输，并将其应用于具有不同平均粒径的硬碳微观结构。模拟揭示了颗粒尺寸、蒸发速率和表面张力等因素对粘结剂分布均匀性的影响。这项工作为优化电极干燥工艺提供了基于物理的、微观结构解析的预测基础。论文的研究内容属于电化学和材料制造领域，虽然不直接涉及“化学大模型”或“质谱结构推理”，但其核心是应用计算建模（一种化学信息学工具）来理解和优化化学材料（电池电极）的制造过程。这可以视为化学信息学在具体工业问题中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sodium-ion batteries employing hard carbon electrodes are considered a drop-in technology for lithium-ion batteries. Electrode drying is a critical manufacturing step, as binder migration during pore emptying impacts the mechanical integrity and electrical performance of the electrode. Existing modeling approaches predominantly rely on the film shrinkage phase in a one dimensional way or neglect the capillary transport, resulting in a lack of physically consistent microstructure resolved predictions of binder migration. In this work, a spatially resolved pore scale continuum model is extended to explicitly describe capillary driven binder transport during pore emptying. The model is applied to hard carbon microstructures with varying mean particle diameters. The simulations reveal that smaller particle sizes lead to a more homogeneous binder distribution, whereas higher evaporation rates and increased surface tension promote stronger binder gradients. Variations in solvent viscosity show only a minor influence on binder migration, as long as no hydrophilic or hydrophobic behavior is present. Finally, the simulations demonstrate that an explicit description of capillary transport and microstructural effects is essential for accurately predicting binder migration and provides a basis for the targeted optimization of electrode drying processes.

</details>

---

### 29. [Neural Galerkin Normalizing Flow for Transition Probability Density Functions of Diffusion Models](https://arxiv.org/abs/2603.18907)

**基本信息**

- 🔗 arXiv: [`2603.18907`](https://arxiv.org/abs/2603.18907)
- 👥 作者: Riccardo Saporiti, Fabio Nobile
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18907.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的“神经伽辽金归一化流”生成建模框架，这是一种可用于密度估计和生成的高级机器学习工具。该工具/方法有潜力应用于“化学大模型”和“质谱结构推理”中，例如用于模拟分子构象分布、解析质谱中的混合物成分或生成化学结构，因此提供了潜在有用的方法资源。

**📖 中文摘要**

本文提出了一种新的神经伽辽金归一化流框架，用于参数化地近似扩散过程的转移概率密度函数（通过求解相应的Fokker-Planck方程）。该方法利用归一化流，将解表示为参考随机过程转移概率密度函数的变换，从而确保近似解满足结构保持、正性和质量守恒约束。通过将神经伽辽金方案扩展到归一化流背景，推导出了流参数随时间演化的常微分方程组。该方法在完成离线训练后，在线评估成本显著低于从头求解偏微分方程。所提出的方法可作为随机微分方程相关许多查询问题（如贝叶斯推断、模拟和扩散桥生成）的一个有前景的代理模型。论文的研究内容属于计算数学和机器学习交叉领域，其提出的“神经伽辽金归一化流”框架是一种强大的生成模型和密度估计方法。这种方法对于构建“化学大模型”中处理不确定性、进行分子动力学模拟或生成化学空间分布具有潜在的重要工具价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Neural Galerkin Normalizing Flow framework to approximate the transition probability density function of a diffusion process by solving the corresponding Fokker-Planck equation with an atomic initial distribution, parametrically with respect to the location of the initial mass. By using Normalizing Flows, we look for the solution as a transformation of the transition probability density function of a reference stochastic process, ensuring that our approximation is structure-preserving and automatically satisfies positivity and mass conservation constraints. By extending Neural Galerkin schemes to the context of Normalizing Flows, we derive a system of ODEs for the time evolution of the Normalizing Flow's parameters. Adaptive sampling routines are used to evaluate the Fokker-Planck residual in meaningful locations, which is of vital importance to address high-dimensional PDEs. Numerical results show that this strategy captures key features of the true solution and enforces the causal relationship between the initial datum and the density function at subsequent times. After completing an offline training phase, online evaluation becomes significantly more cost-effective than solving the PDE from scratch. The proposed method serves as a promising surrogate model, which could be deployed in many-query problems associated with stochastic differential equations, like Bayesian inference, simulation, and diffusion bridge generation.

</details>

---

### 30. [BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery](https://arxiv.org/abs/2603.18957)

**基本信息**

- 🔗 arXiv: [`2603.18957`](https://arxiv.org/abs/2603.18957)
- 👥 作者: Sijian Fan, Liyan Xiong, Dayuan Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18957.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对药物发现问题（结核病耐药性预测、药物重定位）开发新的机器学习模型（BVSIMC）。这直接属于化学信息学和计算药物化学的研究范畴，是构建面向药物发现的“化学大模型”或专业预测模型的相关工作。

**📖 中文摘要**

本文提出了BVSIMC（贝叶斯变量选择引导的归纳矩阵补全），一种新的贝叶斯模型，用于在药物发现中从侧边信息（如药物的化学性质和疾病的基因组信息）中进行变量选择。通过学习稀疏的潜在嵌入，BVSIMC同时提高了预测准确性和可解释性。该方法通过模拟研究和两个药物发现应用进行了验证：1) 预测结核分枝杆菌的耐药性，2) 预测计算药物重定位中的新药-疾病关联。在合成数据和真实数据上，BVSIMC在预测方面优于其他几种最先进的方法。论文的研究内容直接应用于药物发现和化学信息学领域，核心目标是利用机器学习模型（结合变量选择）从化学和生物数据中预测生物活性或关联关系。这本质上是构建用于化学和生物医学研究的预测模型，与“化学大模型”中关于小分子性质预测和药物-靶点相互作用预测的子方向高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in drug discovery have demonstrated that incorporating side information (e.g., chemical properties about drugs and genomic information about diseases) often greatly improves prediction performance. However, these side features can vary widely in relevance and are often noisy and high-dimensional. We propose Bayesian Variable Selection-Guided Inductive Matrix Completion (BVSIMC), a new Bayesian model that enables variable selection from side features in drug discovery. By learning sparse latent embeddings, BVSIMC improves both predictive accuracy and interpretability. We validate our method through simulation studies and two drug discovery applications: 1) prediction of drug resistance in Mycobacterium tuberculosis, and 2) prediction of new drug-disease associations in computational drug repositioning. On both synthetic and real data, BVSIMC outperforms several other state-of-the-art methods in terms of prediction. In our two real examples, BVSIMC further reveals the most clinically meaningful side features.

</details>

---

### 31. [SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141)

**基本信息**

- 🔗 arXiv: [`2603.19141`](https://arxiv.org/abs/2603.19141)
- 👥 作者: Mingxing Zhang, Nicola Rossberg, Simone Innocente 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19141.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于处理光谱数据的可解释机器学习框架（SHAPCA）。光谱数据（如质谱、红外光谱）是化学信息学和质谱分析领域的核心数据类型。该框架旨在提供稳定、可解释的模型预测，这对于化学大模型（用于预测或分析）的构建、验证和信任至关重要，属于为相关主题提供方法论工具。

**📖 中文摘要**

本文提出SHAPCA，一个用于光谱数据的可解释机器学习流程。该流程结合了主成分分析（PCA）进行降维和SHAP（Shapley Additive exPlanations）进行事后解释，旨在为化学和生物医学分析中的光谱数据集提供稳定且可解释的模型预测解释。论文的核心是解决光谱数据固有的高维度和强共线性问题，这些问题不仅使模型训练复杂化，还会导致特征重要性在不同训练轮次中不稳定。SHAPCA通过将解释映射回原始输入空间，使从业者能够将预测与生物组分联系起来，从而进行解释。该框架支持全局和局部分析，揭示了驱动整体模型行为的谱带以及影响个体预测的实例特定特征。数值分析证明了结果的可解释性以及不同运行间更高的一致性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

</details>

---

### 32. [UGID: Unified Graph Isomorphism for Debiasing Large Language Models](https://arxiv.org/abs/2603.19144)

**基本信息**

- 🔗 arXiv: [`2603.19144`](https://arxiv.org/abs/2603.19144)
- 👥 作者: Zikang Ding, Junchi Yao, Junhao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19144.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大语言模型（LLMs）的去偏方法。虽然不专门针对化学领域，但“化学大模型”通常是基于Transformer架构的大语言模型或跨模态模型在化学领域的应用。因此，针对大模型内部表示和架构的通用去偏方法（UGID）与构建更公平、可靠的化学大模型这一主题直接相关。

**📖 中文摘要**

本文提出UGID（统一图同构去偏），一种针对大语言模型内部表示层面的去偏框架。该框架将Transformer建模为一个结构化的计算图，其中注意力机制定义图的边，隐藏状态定义图的节点。具体来说，去偏被表述为在反事实输入上强制图结构不变，只允许敏感属性存在差异。UGID联合约束偏见敏感区域的注意力路由和隐藏表示，有效防止偏见在架构组件间迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) exhibit pronounced social biases. Output-level or data-optimization--based debiasing methods cannot fully resolve these biases, and many prior works have shown that biases are embedded in internal representations. We propose \underline{U}nified \underline{G}raph \underline{I}somorphism for \underline{D}ebiasing large language models (\textit{\textbf{UGID}}), an internal-representation--level debiasing framework for large language models that models the Transformer as a structured computational graph, where attention mechanisms define the routing edges of the graph and hidden states define the graph nodes. Specifically, debiasing is formulated as enforcing invariance of the graph structure across counterfactual inputs, with differences allowed only on sensitive attributes. \textit{\textbf{UGID}} jointly constrains attention routing and hidden representations in bias-sensitive regions, effectively preventing bias migration across architectural components. To achieve effective behavioral alignment without degrading general capabilities, we introduce a log-space constraint on sensitive logits and a selective anchor-based objective to preserve definitional semantics. Extensive experiments on large language models demonstrate that \textit{\textbf{UGID}} effectively reduces bias under both in-distribution and out-of-distribution settings, significantly reduces internal structural discrepancies, and preserves model safety and utility.

</details>

---

### 33. [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](https://arxiv.org/abs/2603.19183)

**基本信息**

- 🔗 arXiv: [`2603.19183`](https://arxiv.org/abs/2603.19183)
- 👥 作者: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19183.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用稀疏自编码器（SAEs）等可解释性技术来理解和分析视觉-语言-动作（VLA）模型的内部表示。VLA模型是“大模型”在多模态和具身智能领域的具体实例。该工作探索了大模型如何学习通用特征与记忆特定模式，这对于理解任何领域（包括化学）的大模型的工作原理、泛化能力和潜在缺陷都具有核心相关性。

**📖 中文摘要**

本文对视觉-语言-动作（VLA）模型应用机械可解释性技术，以更好地理解其内部工作机制。为了探测内部表示，作者在VLA的隐藏层激活上训练稀疏自编码器（SAEs）。SAEs学习一个稀疏字典，其特征作为模型计算的一个紧凑、可解释的基础。研究发现，大多数提取的SAE特征对应于特定训练演示中的记忆序列。然而，一些特征对应于可解释的、通用的、可引导的运动基元和语义属性。作者提出了一种指标，根据特征是代表可泛化的可转移基元还是特定于情节的记忆来对特征进行分类。通过在LIBERO基准上的引导实验验证了这些发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for general-purpose robot manipulation. However, their generalization is inconsistent: while these models can perform impressively in some settings, fine-tuned variants often fail on novel objects, scenes, and instructions. We apply mechanistic interpretability techniques to better understand the inner workings of VLA models. To probe internal representations, we train Sparse Autoencoders (SAEs) on hidden layer activations of the VLA. SAEs learn a sparse dictionary whose features act as a compact, interpretable basis for the model's computation. We find that the large majority of extracted SAE features correspond to memorized sequences from specific training demonstrations. However, some features correspond to interpretable, general, and steerable motion primitives and semantic properties, offering a promising glimpse toward VLA generalizability. We propose a metric to categorize features according to whether they represent generalizable transferable primitives or episode-specific memorization. We validate these findings through steering experiments on the LIBERO benchmark. We show that individual SAE features causally influence robot behavior. Steering general features induces behaviors consistent with their semantic meaning and can be applied across tasks and scenes. This work provides the first mechanistic evidence that VLAs can learn generalizable features across tasks and scenes. We observe that supervised fine-tuning on small robotics datasets disproportionately amplifies memorization. In contrast, training on larger, more diverse datasets (e.g., DROID) or using knowledge insulation promotes more general features. We provide an open-source codebase and user-friendly interface for activation collection, SAE training, and feature steering. Our project page is located at this http URL

</details>

---

### 34. [MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185)

**基本信息**

- 🔗 arXiv: [`2603.19185`](https://arxiv.org/abs/2603.19185)
- 👥 作者: Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19185.pdf)

**💡 相关性分析**

满足标准2：论文的核心是评估扩散模型（一种生成模型）在合成数据（特别是表格数据）上的隐私性。虽然焦点是隐私攻击，但该工作涉及对生成模型（可视为化学大模型的一种类型）生成的数据集进行评估的方法和基准。这对于构建和评估用于化学信息学（如分子生成、性质预测）的生成模型或大模型具有参考价值，因为它关注生成数据的质量和潜在漏洞。

**📖 中文摘要**

本文介绍了MIDST挑战赛，旨在定量评估由扩散模型生成的合成表格数据的隐私增益，特别关注其对成员推理攻击（MIA）的抵抗力。鉴于表格数据的异质性和复杂性，研究探索了多个目标模型进行MIA，包括用于混合数据类型单表的扩散模型和具有互连约束的多关系表。MIDST的一个关键成果是启发了针对这些目标扩散模型的新型黑盒和白盒MIA的开发，从而能够全面评估其隐私效力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at this https URL

</details>

---

### 35. [Generative Replica-Exchange: A Flow-based Framework for Accelerating Replica Exchange Simulations](https://arxiv.org/abs/2603.18076)

**基本信息**

- 🔗 arXiv: [`2603.18076`](https://arxiv.org/abs/2603.18076)
- 👥 作者: Shengjie Huang, Sijie Yang, Jianqiao Yi 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18076.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用深度生成模型（归一化流）来加速分子模拟采样，这直接属于“化学大模型”在计算化学/化学信息学中的应用范畴。

**📖 中文摘要**

本文提出了一种生成式副本交换（GREX）框架，将深度生成模型（特别是归一化流）集成到副本交换分子动力学（REX）模拟中，以加速采样。该方法利用训练好的归一化流按需生成高温构型，并通过势能约束将其直接映射到目标分布，从而消除了对大量中间温度副本的需求，将生产模拟简化为目标温度下的单个副本。该方法在三个复杂度递增的基准系统上进行了验证，展示了其在分子模拟中的优越效率和实际适用性。该工作属于化学信息学中利用生成模型（化学大模型的一种）加速分子模拟和采样的核心研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Replica exchange (REX) is one of the most widely used enhanced sampling methodologies, yet its efficiency is limited by the requirement for a large number of intermediate temperature replicas. Here we present Generative Replica Exchange (GREX), which integrates deep generative models into the REX framework to eliminate this temperature ladder. Drawing inspiration from reservoir replica exchange (res-REX), GREX utilizes trained normalizing flows to generate high-temperature configurations on demand and map them directly to the target distribution using the potential energy as a constraint, without requiring target-temperature training data. This approach reduces production simulations to a single replica at the target temperature while maintaining thermodynamic rigor through Metropolis exchange acceptance. We validate GREX on three benchmark systems of increasing complexity, highlighting its superior efficiency and practical applicability for molecular simulations.

</details>

---

### 36. [Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows](https://arxiv.org/abs/2603.18205)

**基本信息**

- 🔗 arXiv: [`2603.18205`](https://arxiv.org/abs/2603.18205)
- 👥 作者: Dominic Schuh, Lena Funcke, Janik Kreit 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用归一化流（一种生成模型）来解决量子化学/物理中哈伯德模型的模拟难题，属于“化学大模型”在量子化学计算中的应用。

**📖 中文摘要**

本文解决了掺杂哈伯德模型在有限化学势下的模拟难题，该模型因符号问题而难以处理。作者扩展了在零掺杂（半填充）情况下使用归一化流的最新进展，通过引入退火方案实现了遍历采样，从而将方法推广到有限化学势。与电荷基下的最先进混合蒙特卡罗方法相比，该方法能准确再现精确对角化结果，同时将统计不确定性降低了一个数量级，为模拟掺杂关联系统开辟了新途径。该工作展示了生成模型（归一化流）在解决量子多体物理和计算化学中核心计算难题的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hubbard model at finite chemical potential is a cornerstone for understanding doped correlated systems, but simulations are severely limited by the sign problem. In the auxiliary-field formulation, the spin basis mitigates the sign problem, yet severe ergodicity issues have limited its use. We extend recent advances with normalizing flows at half-filling to finite chemical potential by introducing an annealing scheme enabling ergodic sampling. Compared to state-of-the-art hybrid Monte Carlo in the charge basis, our approach accurately reproduces exact diagonalization results while reducing statistical uncertainties by an order of magnitude, opening a new path for simulations of doped correlated systems.

</details>

---

### 37. [Nonlinear Incompressible Shear Wave Models in Hyperelasticity and Viscoelasticity Frameworks, with Applications to Love Waves](https://arxiv.org/abs/2603.18296)

**基本信息**

- 🔗 arXiv: [`2603.18296`](https://arxiv.org/abs/2603.18296)
- 👥 作者: Shawn Samuel Carl McAdam, Samuel Opoku Agyemang, Alexei Cheviakov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18296.pdf)

**💡 相关性分析**

满足标准1（边缘相关）：论文的核心是建立非线性波在材料中传播的物理模型。虽然不直接涉及质谱，但其处理复杂信号（位移场）和非线性方程的方法，在广义的“结构推理”数学工具层面，与从质谱信号中推断分子结构有微弱的理念相似性。基于包容性筛选原则，予以纳入。

**📖 中文摘要**

本文提出了描述不可压缩超弹性材料中剪切位移的通用方程，并将其应用于描述在具有不同力学性能的材料界面上传播的非线性Love型波。该模型适用于一大类超粘弹性材料。对于一个立方Yeoh模型，剪切波方程包含三次和五次微分多项式项，以及以材料位移的混合导数形式出现的粘弹性贡献项。该工作涉及材料本构关系的数学建模，虽然主要聚焦于力学，但其对非线性波在复杂材料中传播的建模思想，与质谱分析中解析复杂谱图信号（如解卷积、峰形拟合）所需的数学工具有一定类比性，但关联性较弱。考虑到“质谱结构推理”可能广义地包含从复杂信号中推断物理/化学结构，本文的数学方法可能提供间接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General equations describing shear displacements in incompressible hyperelastic materials, holding for an arbitrary form of strain energy density function, are presented and applied to the description of nonlinear Love-type waves propagating on an interface between materials with different mechanical properties. The model is valid for a broad class of hyper-viscoelastic materials. For a cubic Yeoh model, shear wave equations contain cubic and quintic differential polynomial terms, including viscoelasticity contributions in terms of dispersion terms that include mixed derivatives $u_{xxt}$ of the material displacement. Full (2+1)-dimensional numerical simulations of waves propagating in the bulk of a two-layered solid are undertaken and analyzed with respect to the source position and mechanical properties of the layers. Interfacial nonlinear Love waves and free upper surface shear waves are tracked; it is demonstrated that in the fully nonlinear case, the variable wave speed of interface and surface waves generally satisfies the linear Love wave existence condition $c_1 < \abs{v} < c_2$, while tending to the larger material wave speed $c_1$ or $c_2$ for large times.

</details>

---

### 38. [Precise Performance of Linear Denoisers in the Proportional Regime](https://arxiv.org/abs/2603.18483)

**基本信息**

- 🔗 arXiv: [`2603.18483`](https://arxiv.org/abs/2603.18483)
- 👥 作者: Reza Ghane, Danil Akhtiamov, Babak Hassibi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18483.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计并分析用于从含噪数据中恢复信号的线性降噪器。虽然背景是通用信号处理，但其理论框架和优化方法可直接应用于质谱数据的预处理和去噪，这是“质谱结构推理”流程中至关重要的一环。

**📖 中文摘要**

本文研究了线性降噪器在噪声数据下的性能。作者提出了一种不同于传统经验维纳滤波的方法：通过向数据样本中注入具有特定协方差的合成高斯噪声来构造噪声样本，然后通过最小二乘法训练一个线性降噪器，使其输出的降噪结果逼近干净数据。在比例机制下，作者使用凸高斯最小最大定理（CGMT）解析地推导了该过程所得降噪器的泛化误差闭式表达式。该表达式可用于优化合成噪声的协方差以得到最佳降噪器。数值模拟表明，该方法在许多场景下优于“经验”维纳滤波器。该工作属于信号处理领域，但其核心——从噪声观测中学习最优线性变换以恢复信号——与质谱分析中的基线校正、噪声滤除等预处理步骤在数学原理上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the present paper we study the performance of linear denoisers for noisy data of the form $\mathbf{x} + \mathbf{z}$, where $\mathbf{x} \in \mathbb{R}^d$ is the desired data with zero mean and unknown covariance $\mathbf{\Sigma}$, and $\mathbf{z} \sim \mathcal{N}(0, \mathbf{\Sigma}_{\mathbf{z}})$ is additive noise. Since the covariance $\mathbf{\Sigma}$ is not known, the standard Wiener filter cannot be employed for denoising. Instead we assume we are given samples $\mathbf{x}_1,\dots,\mathbf{x}_n \in \mathbb{R}^d$ from the true distribution. A standard approach would then be to estimate $\mathbf{\Sigma}$ from the samples and use it to construct an ``empirical" Wiener filter. However, in this paper, motivated by the denoising step in diffusion models, we take a different approach whereby we train a linear denoiser $\mathbf{W}$ from the data itself. In particular, we synthetically construct noisy samples $\hat{\mathbf{x}}_i$ of the data by injecting the samples with Gaussian noise with covariance $\mathbf{\Sigma}_1 \neq \mathbf{\Sigma}_{\mathbf{z}}$ and find the best $\mathbf{W}$ that approximates $\mathbf{W}\hat{\mathbf{x}}_i \approx \mathbf{x}_i$ in a least-squares sense. In the proportional regime $\frac{n}{d} \rightarrow \kappa > 1$ we use the {\it Convex Gaussian Min-Max Theorem (CGMT)} to analytically find the closed form expression for the generalization error of the denoiser obtained from this process. Using this expression one can optimize over $\mathbf{\Sigma}_1$ to find the best possible denoiser. Our numerical simulations show that our denoiser outperforms the ``empirical" Wiener filter in many scenarios and approaches the optimal Wiener filter as $\kappa\rightarrow\infty$.

</details>

---

### 39. [DeePAW: A universal machine learning model for orbital-free ab initio calculations](https://arxiv.org/abs/2603.18650)

**基本信息**

- 🔗 arXiv: [`2603.18650`](https://arxiv.org/abs/2603.18650)
- 👥 作者: Tianhao Su, Shunbo Hu, Yue Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18650.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个通用的、基于深度学习的无轨道密度泛函理论模型，用于预测材料的电子密度和能量。这直接属于“化学大模型”在计算化学和材料科学中的核心应用。

**📖 中文摘要**

本文提出了深度增强方式模型（DeePAW），这是一种用于无轨道从头算计算的通用机器学习模型。DeePAW基于密度泛函理论，是目前最好的无轨道密度泛函理论机器学习模型，覆盖元素数量最多，对多样晶体结构的应用能力最广，且无需微调即可实现最高的预测精度。DeePAW的科学价值源于新颖的SE(3)-等变双消息传递神经网络。除了预测电子密度分布，DeePAW还能预测晶体的形成能，从而为超越传统电子结构计算方法的跨尺度材料建模开辟了高效途径。该工作属于化学信息学和计算材料学交叉领域，是“化学大模型”在量子化学计算中的典型代表。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing universal machine learning models for ab initio calculations is the frontier of materials cutting edge research in the new era of artificial intelligence. Here, we present the Deep Augment Way model (DeePAW) that is a universal machine learning (ML) model for orbital-free (OF) ab initio calculations, based on the density functional theory (DFT). DeePAW is currently the best OFDFT ML model according to the three criterions, 1) covering the largest number of elements, 2) having the widest application capability to diverse crystal structures, and 3) achieving the highest prediction accuracy without further fine-tuning. These scientific merits and innovations of DeePAW are stemmed from the novel SE(3)-equivariant double massage passing neuron networks. Besides predicting electron density distributions, DeePAW predicts formation energies of crystals as well and therefore paves an efficient avenue for multiscale materials modeling beyond conventional electronic structure calculation methods.

</details>

---

### 40. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](https://arxiv.org/abs/2603.18864)

**基本信息**

- 🔗 arXiv: [`2603.18864`](https://arxiv.org/abs/2603.18864)
- 👥 作者: Samuel Del Fré, Gilberto A. Alou Angulo, Maurice Monnerville 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18864.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建用于气体-表面散射动力学的机器学习原子间势。这属于“化学大模型”（具体为机器学习力场）在物理化学和表面科学中的直接应用，用于从第一性原理数据中学习并模拟复杂的化学反应动力学。

**📖 中文摘要**

本文为气体-表面散射动力学开发了一种数据驱动的工作流程，用于构建机器学习原子间势。以一氧化氮在石墨表面散射为基准系统，该工作流程从初始的从头算分子动力学数据集出发，使用SOAP描述符描述局部原子环境，并通过主成分分析在降维特征空间中进行分析。使用最远点采样构建紧凑训练集，并通过基于委员会的主动学习策略，从扩展的入射能和表面温度范围的分子动力学模拟中提取额外构型，对得到的深度势模型进行细化。最终的MLIP能够以远低于从头算的成本进行大规模分子动力学模拟，重现了散射实验的主要趋势。该工作展示了描述符引导采样与主动学习相结合，为构建气体-表面相互作用的MLIP提供了一种高效且可迁移的策略。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate atomistic simulations of gas-surface scattering require potential energy surfaces that remain reliable over broad configurational and energetic ranges while retaining the efficiency needed for extensive trajectory sampling. Here, we develop a data-driven workflow for constructing a machine-learning interatomic potential (MLIP) tailored to gas-surface scattering dynamics, using nitric oxide (NO) scattering from highly oriented pyrolytic graphite (HOPG) as a benchmark system. Starting from an initial ab initio molecular dynamics (AIMD) dataset, local atomic environments are described by SOAP descriptors and analyzed in a reduced feature space obtained through principal component analysis. Farthest point sampling is then used to build a compact training set, and the resulting Deep Potential model is refined through a query-by-committee active-learning strategy using additional configurations extracted from molecular dynamics simulations over extended ranges of incident energies and surface temperatures. The final MLIP reproduces reference energies and forces with high fidelity and enables large-scale molecular dynamics simulations of NO scattering from graphite at a computational cost far below that of AIMD. The simulations provide detailed insight into adsorption energetics, trapping versus direct scattering probabilities, translational energy loss, angular distributions, and rotational excitation. Overall, the results reproduce the main experimental trends and demonstrate that descriptor-guided sampling combined with active learning offers an efficient and transferable strategy for constructing MLIPs for gas-surface interactions.

</details>

---

### 41. [Improving moment tensor solutions under Earth structure uncertainty with simulation-based inference](https://arxiv.org/abs/2603.18925)

**基本信息**

- 🔗 arXiv: [`2603.18925`](https://arxiv.org/abs/2603.18925)
- 👥 作者: A. A. Saoulis, T.-S. Pham, A. M. G. Ferreira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用模拟推理等机器学习方法，从数据中学习并建模反演过程中的不确定性，从而获得更可靠的地球物理参数（矩张量）估计。这种方法论与“质谱结构推理”中利用机器学习处理噪声、偏差和模型不确定性以推断更准确的分子结构完全同源。

**📖 中文摘要**

本文介绍了利用模拟推理来处理全波形矩张量反演中地球结构不确定性的稳健方法。传统贝叶斯方法通常需要对理论误差做出可能使解产生偏差的近似。模拟推理作为一种机器学习方法，通过经验性地建模不确定性对观测的影响来避免对其函数形式的限制性假设。作者首先证明了在轻微的一维地球模型不确定性下，理论误差的高斯参数化会失效。为了解决这个问题，他们开发了两种利用SBI改进矩张量解质量的形式：一种基于对理论误差的物理洞察，另一种利用端到端深度学习算法。结果表明，高斯假设会引入偏差并显著低估矩张量的不确定性，而SBI能产生更可靠、校准更好的震源机制后验分布。该工作将机器学习方法引入地球物理反演问题，其“从数据中学习不确定性模型以改进反演”的核心思想，与质谱分析中利用机器学习处理仪器误差、解卷积不确定性以改进结构推理的思路高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian inference represents a principled way to incorporate Earth structure uncertainty in full-waveform moment tensor inversions, but traditional approaches generally require significant approximations that risk biasing the resulting solutions. We introduce a robust method for handling theory errors using simulation-based inference (SBI), a machine learning approach that empirically models their impact on the observations. This framework retains the rigour of Bayesian inference while avoiding restrictive assumptions about the functional form of the uncertainties. We begin by demonstrating that the common Gaussian parametrisation of theory errors breaks down under minor ($1-3 \%$) 1-D Earth model uncertainty. To address this issue, we develop two formalisms for utilising SBI to improve the quality of the moment tensor solutions: one using physics-based insights into the theory errors, and another utilising an end-to-end deep learning algorithm. We then compare the results of moment tensor inversion with the standard Gaussian approach and SBI, and demonstrate that Gaussian assumptions induce bias and significantly under-report moment tensor uncertainties. We also show that these effects are particularly problematic when inverting short period data and for shallow, isotropic events. On the other hand, SBI produces more reliable, better calibrated posteriors of the earthquake source mechanism. Finally, we successfully apply our methodology to two well studied moderate magnitude earthquakes: one from the 1997 Long Valley Caldera volcanic earthquake sequence, and the 2020 Zagreb earthquake.

</details>

---

### 42. [BSTModelKit.jl: A Julia Package for Constructing, Solving, and Analyzing Biochemical Systems Theory Models](https://arxiv.org/abs/2603.19115)

**基本信息**

- 🔗 arXiv: [`2603.19115`](https://arxiv.org/abs/2603.19115)
- 👥 作者: Sandra Vadhin, Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19115.pdf)

**💡 相关性分析**

满足标准2：论文的核心内容是发布一个用于生化系统理论建模的软件工具包（BSTModelKit.jl）。这为化学信息学和系统生物学领域的研究者提供了可直接用于构建和分析化学/生物网络模型的“工具”和“资源”。

**📖 中文摘要**

本文介绍了BSTModelKit.jl，一个用于构建、求解和分析生化系统理论模型的开源Julia软件包。该包实现了S系统表示法，这是一种用于建模代谢和调控网络的规范幂律形式主义。BSTModelKit.jl提供了声明式模型规范格式、通过常微分方程积分进行动态模拟、稳态计算以及使用Morris和Sobol方法进行全局敏感性分析。该软件包利用Julia科学计算生态系统，特别是SciML微分方程求解器套件，提供高效灵活的模型分析工具。该工作提供了用于生化网络建模与分析的专用工具和资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present this http URL , an open-source Julia package for constructing, solving, and analyzing Biochemical Systems Theory (BST) models of biochemical networks. The package implements S-system representations, a canonical power-law formalism for modeling metabolic and regulatory networks. this http URL provides a declarative model specification format, dynamic simulation via ordinary differential equation (ODE) integration, steady-state computation, and global sensitivity analysis using the Morris and Sobol methods. The package leverages the Julia scientific computing ecosystem, in particular the SciML suite of differential equation solvers, to provide efficient and flexible model analysis tools. We describe the mathematical formulation, software design, and demonstrate the package capabilities with illustrative examples.

</details>

---

### 43. [Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset](https://arxiv.org/abs/2407.17869)

**基本信息**

- 🔗 arXiv: [`2407.17869`](https://arxiv.org/abs/2407.17869)
- 👥 作者: Yiming Ma, Jianzhi Teng, Xinjie Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.17869.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成模型（条件流匹配）解决从椭圆偏振测量信号中反演材料光学常数和厚度的逆问题。这本质上与“质谱结构推理”从质谱信号反演分子结构的任务同属一类，即利用生成模型解决仪器测量数据的逆向解析问题。

**📖 中文摘要**

本文针对逆椭圆偏振测量这一病态反问题，引入了EllipBench基准数据集，包含超过800万个涵盖98种薄膜材料和5种基底的高精度样本。基于此基准，作者系统评估了包括传统机器学习模型、深度神经网络和物理信息神经网络在内的多种方法，发现现有范式难以完全解决该逆问题。为此，作者进一步提出了一种新颖的解耦条件流匹配框架。DCFM将几何膜厚解耦并作为稳健的物理条件，引导一个连续向量场来建模波长相关光学常数的逆概率分布。结合梯度分离策略和基于物理的约束，该联合架构有效缓解了固有的物理模糊性，为逆椭圆偏振测量提供了稳健准确的解决方案。该工作属于计算光学和材料表征领域，其核心是使用生成模型（流匹配）解决一个从测量信号（Δ, Ψ）反演材料本征参数（光学常数、厚度）的逆问题。这与“质谱结构推理”从质谱信号反演分子结构的任务在问题定义和解决范式上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse ellipsometry, i.e., reconstructing optical constants and film thickness from the measured phase difference $\Delta$ and amplitude ratio $\Psi$, is a fundamentally ill-posed problem. Traditional solutions rely on slow, expert-driven iterative fitting, while the development of machine learning approaches has been severely limited by the lack of large-scale, physically consistent datasets. To address this gap, we introduce \textbf{EllipBench}, a comprehensive benchmark comprising over 8 million high-precision samples spanning 98 thin-film materials and 5 substrates. Building upon this benchmark, we conduct a systematic evaluation of a broad spectrum of methods, including traditional machine learning models, deep neural networks, and Physics-Informed Neural Networks, and show that existing paradigms consistently struggle to fully resolve the inverse ellipsometry task. To better capture its inherent ambiguity, we further propose a novel \textbf{Decoupled Conditional Flow Matching (DCFM)} framework. Rather than formulating the problem as deterministic point-to-point regression, DCFM explicitly decouples geometric film thickness and incorporates it as a robust physical condition to guide a continuous vector field for modeling the inverse probability distribution of wavelength-dependent optical constants. Combined with a gradient detachment strategy and physics-based constraints, our joint architecture effectively mitigates intrinsic physical ambiguities and delivers a robust and accurate solution for inverse ellipsometry.

</details>

---

### 44. [Biased AI can Influence Political Decision-Making](https://arxiv.org/abs/2410.06415)

**基本信息**

- 🔗 arXiv: [`2410.06415`](https://arxiv.org/abs/2410.06415)
- 👥 作者: Jillian Fisher, Shangbin Feng, Robert Aron 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.06415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用结构化Transformer（Cliqueformer）进行模型优化，并将其应用于化学设计任务，这直接关联到“化学大模型”主题。

**📖 中文摘要**

论文标题为“Cliqueformer: Model-Based Optimization with Structured Transformers”。该论文提出了一种基于Transformer的架构Cliqueformer，用于解决离线模型优化（MBO）问题。它通过学习黑盒函数的结构（通过功能图模型）来应对分布偏移，而无需依赖显式的保守方法。论文在多个领域（包括化学和遗传设计任务）进行了评估，表明其性能优于现有方法。该工作与“化学大模型”主题相关，因为它提出了一种用于化学设计任务的通用、基于Transformer的优化框架，这属于化学信息学中利用大模型进行分子或材料发现的范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As modern large language models (LLMs) become integral to everyday tasks, concerns about their inherent biases and their potential impact on human decision-making have emerged. While bias in models are well-documented, less is known about how these biases influence human decisions. This paper presents two interactive experiments investigating the effects of partisan bias in LLMs on political opinions and decision-making. Participants interacted freely with either a biased liberal, biased conservative, or unbiased control model while completing these tasks. We found that participants exposed to partisan biased models were significantly more likely to adopt opinions and make decisions which matched the LLM's bias. Even more surprising, this influence was seen when the model bias and personal political partisanship of the participant were opposite. However, we also discovered that prior knowledge of AI was weakly correlated with a reduction of the impact of the bias, highlighting the possible importance of AI education for robust mitigation of bias effects. Our findings not only highlight the critical effects of interacting with biased LLMs and its ability to impact public discourse and political conduct, but also highlights potential techniques for mitigating these risks in the future.

</details>

---

### 45. [LLM-Based World Models Can Make Decisions Solely, But Rigorous Evaluations are Needed](https://arxiv.org/abs/2411.08794)

**基本信息**

- 🔗 arXiv: [`2411.08794`](https://arxiv.org/abs/2411.08794)
- 👥 作者: Chang Yang, Xinrun Wang, Junzhe Jiang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.08794.pdf)

**💡 相关性分析**

满足标准3：论文是对基于大语言模型（LLM）的世界模型进行的系统性评估和讨论，虽然不专门针对化学，但其对LLM作为通用推理和规划模型的评估框架与“化学大模型”主题中关于模型能力、评估和应用的讨论高度相关。

**📖 中文摘要**

论文标题为“LLM-Based World Models Can Make Decisions Solely, But Rigorous Evaluations are Needed”。该论文对基于大型语言模型（LLM）的世界模型进行了全面评估，从决策制定的角度出发。它设计了策略验证、行动提议和策略规划等任务，并在31个多样化环境中对先进的LLM（如GPT-4o）进行了评估。虽然论文主要关注通用决策，但其对LLM作为世界模型能力的系统性评估框架，为理解大模型（包括潜在的化学或科学领域大模型）在复杂推理和规划任务中的潜力和局限性提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

World model emerges as a key module in decision making, where MuZero and Dreamer achieve remarkable successes in complex tasks. Recent work leverages Large Language Models (LLMs) as general world simulators to simulate the dynamics of the world due to their generalizability. LLMs also serve as the world model for deliberative reasoning in Reasoning via Planning (RAP) and Tree of Thought (ToT). However, the world models are either evaluated as a general world simulator, or as a functional module of the agent, i.e., predicting the transitions to assist the planning. In this work, we propose a comprehensive evaluation of the world models with LLMs from the decision making perspective. Specifically, we leverage the 31 diverse environments from (Wang et al., 2023;2024) and curate the rule-based policy of each environment for the diverse evaluation. Then, we design three main tasks, i.e., policy verification, action proposal, and policy planning, where the world models can be used for decision making solely. Finally, we conduct the comprehensive evaluation of the advanced LLMs, i.e., GPT-4o and GPT-4o-mini, on the environments for the three main tasks under various settings. The key observations include: i) GPT-4o significantly outperforms GPT-4o-mini on the three main tasks, especially for the tasks which require the domain knowledge, ii) the performance of the world model with LLM will be decreased for long-term decision-making tasks, and iii) the combination of different functionalities of the world model will brings additional unstabilities of the performance.

</details>

---

### 46. [Is Contrastive Distillation Enough for Learning Comprehensive 3D Representations?](https://arxiv.org/abs/2412.08973)

**基本信息**

- 🔗 arXiv: [`2412.08973`](https://arxiv.org/abs/2412.08973)
- 👥 作者: Yifan Zhang, Junhui Hou
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.08973.pdf)

**💡 相关性分析**

满足标准3：论文提出的跨模态表示学习框架涉及对现有对比学习方法局限性的理论分析和新框架的提出，这属于对模型学习机制的深入讨论，与构建能够处理复杂科学数据（如化学多模态数据）的大模型的研究方向相关。

**📖 中文摘要**

论文标题为“Is Contrastive Distillation Enough for Learning Comprehensive 3D Representations?”。该论文提出了一个新的跨模态综合表示学习框架CMCR，用于学习更全面的3D表示。它通过引入掩码图像建模和占用估计任务来指导网络学习模态特定特征，并提出了一个新颖的多模态统一码本。虽然应用背景是3D视觉，但其核心方法——通过设计特定任务和构建共享嵌入空间来增强跨模态表示学习——与构建和理解复杂数据（如化学结构或质谱数据）的多模态大模型在方法论上具有相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cross-modal contrastive distillation has recently been explored for learning effective 3D representations. However, existing methods focus primarily on modality-shared features, neglecting the modality-specific features during the pre-training process, which leads to suboptimal representations. In this paper, we theoretically analyze the limitations of current contrastive methods for 3D representation learning and propose a new framework, namely CMCR (Cross-Modal Comprehensive Representation Learning), to address these shortcomings. Our approach improves upon traditional methods by better integrating both modality-shared and modality-specific features. Specifically, we introduce masked image modeling and occupancy estimation tasks to guide the network in learning more comprehensive modality-specific features. Furthermore, we propose a novel multi-modal unified codebook that learns an embedding space shared across different modalities. Besides, we introduce geometry-enhanced masked image modeling to further boost 3D representation learning. Extensive experiments demonstrate that our method mitigates the challenges faced by traditional approaches and consistently outperforms existing image-to-LiDAR contrastive distillation methods in downstream tasks. Code will be available at this https URL .

</details>

---

### 47. [Mitigating Omitted Variable Bias in Empirical Software Engineering](https://arxiv.org/abs/2501.17026)

**基本信息**

- 🔗 arXiv: [`2501.17026`](https://arxiv.org/abs/2501.17026)
- 👥 作者: Carlo A. Furia, Richard Torkar
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.17026.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是直接利用和增强大型语言模型（LLM）来构建新的文本嵌入方法。这属于“化学大模型”主题中利用和适应大模型基础技术的一部分。

**📖 中文摘要**

论文标题为“Enhancing Lexicon-Based Text Embeddings with Large Language Models”。该论文引入了第一种基于词典的文本嵌入方法LENS，该方法利用大型语言模型（LLM）实现，并在通用文本嵌入任务上取得了有竞争力的性能。LENS通过令牌嵌入聚类来整合词汇空间，处理LLM词汇中的冗余问题，并支持高效的嵌入维度剪枝。论文在Massive Text Embedding Benchmark (MTEB) 上进行了广泛实验。这项工作展示了如何利用和改造LLM的底层表示来创建新的、高效的嵌入方法，为利用大模型处理特定领域（如化学文本）的语义信息提供了技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Omitted variable bias occurs when a statistical model leaves out variables that are relevant determinants of the effects under study. This results in the model attributing the missing variables' effect to some of the included variables -- hence over- or under-estimating the latter's true effect. Omitted variable bias presents a significant threat to the validity of empirical research, particularly in non-experimental studies such as those prevalent in empirical software engineering. This paper illustrates the impact of omitted variable bias on two illustrative examples in the software engineering domain, and uses them to present methods to investigate the possible presence of omitted variable bias, to estimate its impact, and to mitigate its drawbacks. The analysis techniques we present are based on causal structural models of the variables of interest, which provide a practical, intuitive summary of the key relations among variables. This paper demonstrates a sequence of analysis steps that inform the design and execution of any empirical study in software engineering. An important observation is that it pays off to invest effort investigating omitted variable bias before actually executing an empirical study, because this effort can lead to a more solid study design, and to a significant reduction in its threats to validity.

</details>

---

### 48. [Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment](https://arxiv.org/abs/2502.03714)

**基本信息**

- 🔗 arXiv: [`2502.03714`](https://arxiv.org/abs/2502.03714)
- 👥 作者: Harrish Thasarathan, Julian Forsyth, Thomas Fel 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03714.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个用于跨模型概念对齐和可解释性分析的新框架（USAE）。这属于对深度学习模型（包括大模型）内部表示和可解释性方法的深入研究和讨论，与构建和理解“化学大模型”的内在机制相关。

**📖 中文摘要**

论文标题为“Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment”。该论文提出了通用稀疏自编码器（USAE），一个用于发现和对齐多个预训练深度神经网络中可解释概念的框架。与现有方法不同，USAE学习一个通用的概念空间，可以同时重建和解释多个模型的内部激活。该框架通过优化共享目标，捕获跨不同任务、架构和数据集的变化共同因素（概念）。这项工作为理解不同模型（包括可能用于化学或质谱分析的大模型）内部表示的一致性提供了新工具，有助于模型的可解释性和跨模型知识迁移。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Universal Sparse Autoencoders (USAEs), a framework for uncovering and aligning interpretable concepts spanning multiple pretrained deep neural networks. Unlike existing concept-based interpretability methods, which focus on a single model, USAEs jointly learn a universal concept space that can reconstruct and interpret the internal activations of multiple models at once. Our core insight is to train a single, overcomplete sparse autoencoder (SAE) that ingests activations from any model and decodes them to approximate the activations of any other model under consideration. By optimizing a shared objective, the learned dictionary captures common factors of variation-concepts-across different tasks, architectures, and datasets. We show that USAEs discover semantically coherent and important universal concepts across vision models; ranging from low-level features (e.g., colors and textures) to higher-level structures (e.g., parts and objects). Overall, USAEs provide a powerful new method for interpretable cross-model analysis and offers novel applications, such as coordinated activation maximization, that open avenues for deeper insights in multi-model AI systems

</details>

---

### 49. [Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning](https://arxiv.org/abs/2503.16252)

**基本信息**

- 🔗 arXiv: [`2503.16252`](https://arxiv.org/abs/2503.16252)
- 👥 作者: Zhaowei Liu, Xin Guo, Zhi Yang 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.16252.pdf)

**💡 相关性分析**

满足标准3：论文详细阐述了一个针对特定领域（金融）构建专业化大语言模型的方法论，包括数据集构建、模型训练（SFT+RL）和评估。这为在“化学信息学”领域构建类似的“化学大模型”提供了重要的技术路径和展望参考。

**📖 中文摘要**

论文标题为“Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning”。该论文介绍了Fin-R1，一个专为金融场景设计的推理大语言模型。其开发采用两阶段流程：首先构建高质量金融思维链数据集Fin-R1-Data，然后通过监督微调（SFT）和强化学习（RL）进行训练。尽管领域是金融，但该工作展示了一个针对特定科学领域（金融）构建专业化、可推理大模型的完整方法论，包括高质量领域数据集的构建、思维链蒸馏以及RLHF技术的应用。这种方法论对于在“化学信息学”或“质谱分析”领域构建类似的领域专用大模型具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, general-purpose large language models (LLMs) such as GPT, Gemini, Claude, and DeepSeek have advanced at an unprecedented pace. Despite these achievements, their application to finance remains challenging, due to fragmented data sources, intransparent reasoning processes, and weak transferability to business applications. In response, we introduce Fin-R1, a reasoning LLM designed for financial scenarios. With a compact size of 7 billion parameters, Fin-R1 reduces deployment costs while addressing the aforementioned challenges. Its development follows a two-stage pipeline. First, we construct Fin-R1-Data, a high-quality financial dataset consisting of 60,091 chain-of-thought (CoT) samples, distilled and filtered from multiple authoritative benchmarks to ensure consistency and reliability. Second, we train Fin-R1 using Fin-R1-Data through supervised fine-tuning (SFT), followed by reinforcement learning (RL). This stage substantially improves the model's ability to solve complex financial reasoning tasks, yielding outputs that are both accurate and interpretable. Despite its relatively small parameter scale, Fin-R1 achieves competitive empirical performance across established financial benchmarks and demonstrates practical utility in compliance checking and robo-advisory. Our code is publicly available at this https URL , and has already attracted over 700 stars.

</details>

---

### 50. [Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability](https://arxiv.org/abs/2505.03530)

**基本信息**

- 🔗 arXiv: [`2505.03530`](https://arxiv.org/abs/2505.03530)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03530.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个用于生成模型（VAE）机制可解释性的因果干预框架，属于对模型内部工作机制的深入分析和讨论。这对于理解和解释未来可能用于化学结构生成或推理的“化学大模型”具有前瞻性意义。

**📖 中文摘要**

论文标题为“Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability”。该论文为变分自编码器（VAE）的机制可解释性引入了一个全面的因果干预框架。它开发了技术来识别和分析VAE中的“电路基元”，研究语义因子如何通过网络层进行编码、处理和分离。该框架使用不同级别的针对性干预：输入操作、潜在空间扰动、激活修补和因果中介分析。这项工作推进了对生成模型（如VAE）的机制理解，并提供了使VAE架构更加透明和可控的工具。虽然VAE不是当前最主流的“大模型”，但该框架所代表的因果解释方法论对于理解任何复杂生成模型（包括可能用于分子生成或质谱数据生成的化学大模型）的内部工作机制具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic interpretability of deep learning models has emerged as a crucial research direction for understanding the functioning of neural networks. While significant progress has been made in interpreting discriminative models like transformers, understanding generative models such as Variational Autoencoders (VAEs) remains challenging. This paper introduces a comprehensive causal intervention framework for mechanistic interpretability of VAEs. We develop techniques to identify and analyze "circuit motifs" in VAEs, examining how semantic factors are encoded, processed, and disentangled through the network layers. Our approach uses targeted interventions at different levels: input manipulations, latent space perturbations, activation patching, and causal mediation analysis. We apply our framework to both synthetic datasets with known causal relationships and standard disentanglement benchmarks. Results show that our interventions can successfully isolate functional circuits, map computational graphs to causal graphs of semantic factors, and distinguish between polysemantic and monosemantic units. Furthermore, we introduce metrics for causal effect strength, intervention specificity, and circuit modularity that quantify the interpretability of VAE components. Experimental results demonstrate clear differences between VAE variants, with FactorVAE achieving higher disentanglement scores (0.084) and effect strengths (mean 4.59) compared to standard VAE (0.064, 3.99) and Beta-VAE (0.051, 3.43). Our framework advances the mechanistic understanding of generative models and provides tools for more transparent and controllable VAE architectures.

</details>

---

### 51. [RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval](https://arxiv.org/abs/2506.08625)

**基本信息**

- 🔗 arXiv: [`2506.08625`](https://arxiv.org/abs/2506.08625)
- 👥 作者: Minhae Oh, Jeonghye Kim, Nakyung Lee 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08625.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是直接提升大型语言模型（LLM）在科学推理任务上的能力，通过一个逐步检索增强框架（RAISE）。这直接关联到“化学大模型”主题中关于模型科学推理能力的研究。

**📖 中文摘要**

论文标题为“RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval”。该论文针对科学推理中的挑战，引入了RAISE，一个逐步检索增强框架，用于从开放语料库中检索逻辑相关的文档。RAISE分为三个步骤：问题分解、逻辑查询生成和逻辑检索。论文指出，RAISE在科学推理基准测试中 consistently outperforms other baselines，并且检索到的文档不仅在领域知识上相似，而且在逻辑上更相关。这项工作直接针对提升大语言模型（LLM）在科学推理任务上的能力，其提出的检索增强框架对于构建能够处理复杂化学或质谱推理问题的“化学大模型”具有直接的应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific reasoning requires not only long-chain reasoning processes, but also knowledge of domain-specific terminologies and adaptation to updated findings. To deal with these challenges for scientific reasoning, we introduce RAISE, a step-by-step retrieval-augmented framework which retrieves logically relevant documents from in-the-wild corpus. RAISE is divided into three steps: problem decomposition, logical query generation, and logical retrieval. We observe that RAISE consistently outperforms other baselines on scientific reasoning benchmarks. We analyze that unlike other baselines, RAISE retrieves documents that are not only similar in terms of the domain knowledge, but also documents logically more relevant.

</details>

---

### 52. [Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning](https://arxiv.org/abs/2506.16931)

**基本信息**

- 🔗 arXiv: [`2506.16931`](https://arxiv.org/abs/2506.16931)
- 👥 作者: Jiaqi Chen, Mingfeng Fan, Xuefeng Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.16931.pdf)

**💡 相关性分析**

满足标准3：论文提出的多模态融合学习（MMFL）框架涉及如何有效整合不同数据模态（图、图像）以解决复杂优化问题，这为“质谱结构推理”中可能涉及的多模态数据（质谱图、分子图、文本描述）融合与推理提供了方法论上的参考和讨论。

**📖 中文摘要**

论文标题为“Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning”。该论文提出了一个多模态融合学习（MMFL）框架，利用图基和图像基表示来捕捉广义旅行商问题（GTSP）的互补方面，并学习一个能够实时生成高质量任务规划方案的策略。虽然应用场景是机器人任务规划，但其核心方法——融合不同模态（图、图像）的表示以更好地解决组合优化问题——与化学信息学中利用多模态数据（如分子图、质谱图）进行分子性质预测或结构推理的思路在方法论上相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Effective and efficient task planning is essential for mobile robots, especially in applications like warehouse retrieval and environmental monitoring. These tasks often involve selecting one location from each of several target clusters, forming a Generalized Traveling Salesman Problem (GTSP) that remains challenging to solve both accurately and efficiently. To address this, we propose a Multimodal Fused Learning (MMFL) framework that leverages both graph and image-based representations to capture complementary aspects of the problem, and learns a policy capable of generating high-quality task planning schemes in real time. Specifically, we first introduce a coordinate-based image builder that transforms GTSP instances into spatially informative representations. We then design an adaptive resolution scaling strategy to enhance adaptability across different problem scales, and develop a multimodal fusion module with dedicated bottlenecks that enables effective integration of geometric and spatial features. Extensive experiments show that our MMFL approach significantly outperforms state-of-the-art methods across various GTSP instances while maintaining the computational efficiency required for real-time robotic applications. Physical robot tests further validate its practical effectiveness in real-world scenarios.

</details>

---

### 53. [Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes](https://arxiv.org/abs/2507.12261)

**基本信息**

- 🔗 arXiv: [`2507.12261`](https://arxiv.org/abs/2507.12261)
- 👥 作者: Johann Frei, Nils Feldhus, Lisa Raithel 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.12261.pdf)

**💡 相关性分析**

满足标准3：论文展示了一个基于LLM智能体的端到端框架，用于从非结构化文本生成复杂的结构化资源（FHIR）。这为利用大模型处理化学领域非结构化文本（如文献、实验记录）以辅助“化学大模型”数据构建或“质谱结构推理”提供了重要的技术展望和讨论。

**📖 中文摘要**

论文标题为“Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes”。该论文提出了Infherno，一个由LLM智能体、代码执行和医学术语数据库工具驱动的端到端框架，用于将自由形式的临床笔记转化为结构化的FHIR（Fast Healthcare Interoperability Resources）资源。该框架旨在遵守FHIR文档模式，并在从非结构化文本预测FHIR资源方面与人类基线相竞争。这项工作展示了利用大语言模型智能体进行复杂、结构化信息抽取和合成的能力。虽然领域是临床医学，但其技术框架（LLM智能体、工具使用、结构化输出生成）对于在化学信息学中构建类似系统，例如从科学文献或实验报告中自动提取和结构化化学实体、反应或质谱数据，具有很高的借鉴价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

For clinical data integration and healthcare services, the HL7 FHIR standard has established itself as a desirable format for interoperability between complex health data. Previous attempts at automating the translation from free-form clinical notes into structured FHIR resources address narrowly defined tasks and rely on modular approaches or LLMs with instruction tuning and constrained decoding. As those solutions frequently suffer from limited generalizability and structural inconformity, we propose an end-to-end framework powered by LLM agents, code execution, and healthcare terminology database tools to address these issues. Our solution, called Infherno, is designed to adhere to the FHIR document schema and competes well with a human baseline in predicting FHIR resources from unstructured text. The implementation features a front end for custom and synthetic data and both local and proprietary models, supporting clinical data integration processes and interoperability across institutions. Gemini 2.5-Pro excels in our evaluation on synthetic and clinical datasets, yet ambiguity and feasibility of collecting ground-truth data remain open problems.

</details>

---

### 54. [GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM](https://arxiv.org/abs/2507.13323)

**基本信息**

- 🔗 arXiv: [`2507.13323`](https://arxiv.org/abs/2507.13323)
- 👥 作者: Kyeongjin Ahn, Sungwon Han, Seungeon Lee 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.13323.pdf)

**💡 相关性分析**

满足标准3：论文提出了一种利用大语言模型（LLM）作为特征工程师来增强少样本回归模型性能的新方法。这种将LLM用于特征工程和模型约束的思路，为在数据稀缺的化学或质谱分析任务中利用“化学大模型”提供了创新的方法论讨论。

**📖 中文摘要**

论文标题为“GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM”。该研究介绍了GeoReg，一个回归模型，它整合了卫星图像和基于网络的地理空间信息等多种数据源，以估计社会经济指标。该模型利用大语言模型的先验知识来解决标记数据稀缺的问题，语言模型作为数据工程师，通过提取信息丰富的特征来实现少样本设置下的有效估计。具体来说，模型获取数据特征与目标指标之间的上下文关系，将其相关性分类为正、负、混合或不相关，然后将这些特征输入带有针对每个类别定制权重约束的线性估计器。这项工作展示了如何利用LLM作为特征工程师来增强少样本回归任务，这种方法可以迁移到化学信息学中，例如利用LLM从分子描述或文献中提取特征，辅助少样本条件下的分子性质预测或质谱解析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Socio-economic indicators like regional GDP, population, and education levels, are crucial to shaping policy decisions and fostering sustainable development. This research introduces GeoReg a regression model that integrates diverse data sources, including satellite imagery and web-based geospatial information, to estimate these indicators even for data-scarce regions such as developing countries. Our approach leverages the prior knowledge of large language model to address the scarcity of labeled data, with the language model functioning as a data engineer by extracting informative features to enable effective estimation in few-shot settings. Specifically, our model obtains contextual relationships between data features and the target indicator, categorizing their correlations as positive, negative, mixed, or irrelevant. These features are then fed into the linear estimator with tailored weight constraints for each category. To capture nonlinear patterns, the model also identifies meaningful feature interactions and integrates them, along with nonlinear transformations. Experiments across three countries at different stages of development demonstrate that our model outperforms baselines in estimating socio-economic indicators, even for low-income countries with limited data availability.

</details>

---

### 55. [All-in-One Slider for Attribute Manipulation in Diffusion Models](https://arxiv.org/abs/2508.19195)

**基本信息**

- 🔗 arXiv: [`2508.19195`](https://arxiv.org/abs/2508.19195)
- 👥 作者: Weixin Ye, Hongguang Zhu, Wei Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.19195.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种用于扩散模型的通用属性操控方法（All-in-One Slider）。虽然演示在图像领域，但其技术核心（在嵌入空间学习可组合的语义方向以实现可控生成）直接适用于“化学大模型”中的一个关键子方向：可控分子生成与编辑。

**📖 中文摘要**

论文标题为“All-in-One Slider for Attribute Manipulation in Diffusion Models”。该论文引入了“All-in-One”Slider，一个轻量级模块，它将文本嵌入空间分解为稀疏的、有语义意义的属性方向。一旦训练完成，它可以作为一个通用滑块，实现对各种属性的可解释和细粒度连续控制。此外，通过重新组合学习到的方向，All-in-One Slider支持多个属性的组合以及对未见属性（例如，种族、名人）的零样本操控。这项工作针对扩散模型中的属性操控，其核心思想——在嵌入空间中学习解耦的、可组合的语义方向——对于化学领域具有重要意义。例如，可以设想在分子生成扩散模型中集成类似的滑块，实现对分子属性（如溶解度、活性）的连续、可控编辑，这直接关联到“化学大模型”中的可控分子生成主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Text-to-image (T2I) diffusion models have made significant strides in generating high-quality images. However, progressively manipulating certain attributes of generated images to meet the desired user expectations remains challenging, particularly for content with rich details, such as human faces. Some studies have attempted to address this by training slider modules. However, they follow a **One-for-One** manner, where an independent slider is trained for each attribute, requiring additional training whenever a new attribute is introduced. This not only results in parameter redundancy accumulated by sliders but also restricts the flexibility of practical applications and the scalability of attribute manipulation. To address this issue, we introduce the **All-in-On** Slider, a lightweight module that decomposes the text embedding space into sparse, semantically meaningful attribute directions. Once trained, it functions as a general-purpose slider, enabling interpretable and fine-grained continuous control over various attributes. Moreover, by recombining the learned directions, the All-in-One Slider supports the composition of multiple attributes and zero-shot manipulation of unseen attributes (e.g., races and celebrities). Extensive experiments demonstrate that our method enables accurate and scalable attribute manipulation, achieving notable improvements compared to previous methods. Furthermore, our method can be extended to integrate with the inversion framework to perform attribute manipulation on real images, broadening its applicability to various real-world scenarios. The code is available on [our project]( this https URL ) page.

</details>

---

### 56. [CausalARC: Abstract Reasoning with Causal World Models](https://arxiv.org/abs/2509.03636)

**基本信息**

- 🔗 arXiv: [`2509.03636`](https://arxiv.org/abs/2509.03636)
- 👥 作者: Jacqueline Maasch, John Kalantari, Kia Khezeli
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.03636.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了一个专注于因果推理和少样本学习的基准测试平台CausalARC。这为评估“化学大模型”在复杂科学推理任务上的能力提供了新的数据集和评估框架（标准2）。同时，论文本身也包含了对大模型在因果和抽象推理方面能力的深入讨论（标准3）。

**📖 中文摘要**

论文标题为“CausalARC: Abstract Reasoning with Causal World Models”。该工作引入了CausalARC：一个用于AI在低数据和分布外场景下推理的实验测试平台，其建模灵感来源于抽象与推理语料库（ARC）。每个CausalARC推理任务都从一个完全指定的因果世界模型中采样，该模型以结构因果模型的形式正式表达。作为概念验证，作者说明了CausalARC在四种语言模型评估设置中的用途。该平台专注于因果推理和少样本学习，为评估和提升大模型（包括潜在的化学领域大模型）在复杂、数据稀缺的科学推理任务（如基于有限实验数据的反应机理推理）上的能力提供了一个新颖的基准和框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

On-the-fly reasoning often requires adaptation to novel problems under limited data and distribution shift. This work introduces CausalARC: an experimental testbed for AI reasoning in low-data and out-of-distribution regimes, modeled after the Abstraction and Reasoning Corpus (ARC). Each CausalARC reasoning task is sampled from a fully specified causal world model, formally expressed as a structural causal model. Principled data augmentations provide observational, interventional, and counterfactual feedback about the world model in the form of few-shot, in-context learning demonstrations. As a proof-of-concept, we illustrate the use of CausalARC for four language model evaluation settings: (1) abstract reasoning with test-time training, (2) counterfactual reasoning with in-context learning, (3) program synthesis, and (4) causal discovery with logical reasoning. Within- and between-model performance varied heavily across tasks, indicating room for significant improvement in language model reasoning.

</details>

---

### 57. [Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning](https://arxiv.org/abs/2509.08759)

**基本信息**

- 🔗 arXiv: [`2509.08759`](https://arxiv.org/abs/2509.08759)
- 👥 作者: Mominul Rubel, Adam Meyers, Gabriel Nicolosi
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.08759.pdf)

**💡 相关性分析**

满足标准3：论文提出了一种新颖的神经网络架构（FLM），专为科学机器学习设计，具有强大的函数表示能力。这属于对适用于科学计算的新型模型架构的深入研究和讨论，为构建下一代“化学大模型”（尤其是涉及物理方程或频谱分析的模型）提供了有潜力的基础组件和技术思路。

**📖 中文摘要**

论文标题为“Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning”。该论文介绍了傅里叶学习机（FLM），一种设计用于表示多维非调和傅里叶级数的神经网络架构。FLM使用具有余弦激活函数的简单前馈结构，将级数的频率、振幅和相移作为可训练参数进行学习。这种设计允许模型创建一个适应周期和非周期函数的问题特定谱基。作者在包括偏微分方程（PDE）和最优控制问题（OCP）在内的多个科学计算问题上评估了FLM的性能。计算实验表明，FLM的性能与SIREN和普通前馈NN等成熟架构相当，且通常更优。这项工作提出了一种新的、具有强大函数表示能力的神经网络架构，特别适用于科学机器学习。这种架构有可能作为基础组件，集成到用于解决化学PDE、分子动力学模拟或光谱数据拟合的更大、更复杂的“化学大模型”中。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Fourier Learning Machine (FLM), a neural network (NN) architecture designed to represent a multidimensional nonharmonic Fourier series. The FLM uses a simple feedforward structure with cosine activation functions to learn the frequencies, amplitudes, and phase shifts of the series as trainable parameters. This design allows the model to create a problem-specific spectral basis adaptable to both periodic and nonperiodic functions. Unlike previous Fourier-inspired NN models, the FLM is the first architecture able to represent a multidimensional Fourier series with a complete set of basis functions in separable form, doing so by using a standard Multilayer Perceptron-like architecture. A one-to-one correspondence between the Fourier coefficients and amplitudes and phase-shifts is demonstrated, allowing for the translation between a full, separable basis form and the cosine phase-shifted one. Additionally, we evaluate the performance of FLMs on several scientific computing problems, including benchmark Partial Differential Equations (PDEs) and a family of Optimal Control Problems (OCPs). Computational experiments show that the performance of FLMs is comparable, and often superior, to that of established architectures like SIREN and vanilla feedforward NNs.

</details>

---

### 58. [Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity](https://arxiv.org/abs/2601.18032)

**基本信息**

- 🔗 arXiv: [`2601.18032`](https://arxiv.org/abs/2601.18032)
- 👥 作者: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18032.pdf)

**💡 相关性分析**

满足标准2：论文构建了一个用于聚合物性能预测的高质量数据集，并利用预训练的化学大模型（聚合物表示）进行多模态学习，为化学大模型在材料发现中的应用提供了数据资源和具体案例。

**📖 中文摘要**

本文聚焦于高性能介电弹性体的开发，这是一个化学信息学与材料科学交叉的领域。论文的核心贡献在于构建了一个高质量的丙烯酸酯基介电弹性体数据集，并提出了一个多模态学习框架。该框架利用大规模预训练的聚合物表示（即化学大模型）来迁移化学和结构知识，从而在数据稀缺的情况下实现对介电和机械性能的准确预测。这项工作直接提供了用于化学大模型应用的数据集（标准2），并展示了如何利用预训练的化学表示来加速新材料发现，与“化学大模型”主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggregating experimental results from the past decade. Building on this dataset, we propose a multimodal learning framework leveraging large-scale pretrained polymer representations. These pretrained embeddings transfer chemical and structural knowledge from vast polymer corpora, enabling accurate few-shot prediction of dielectric and mechanical properties and accelerating data-efficient discovery of soft high-$k$ dielectric elastomers. Our data and implementation are publicly available at: this https URL

</details>

---

### 59. [Sheaf Neural Networks and biomedical applications](https://arxiv.org/abs/2602.00159)

**基本信息**

- 🔗 arXiv: [`2602.00159`](https://arxiv.org/abs/2602.00159)
- 👥 作者: Aneeqa Mehrab, Jan Willem Van Looy, Pietro Demurtas 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00159.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的图神经网络（层神经网络），这是构建化学大模型（用于分子表示和性质预测）和进行质谱结构推理（将质谱数据与分子图关联）的关键底层技术之一。

**📖 中文摘要**

本文介绍了层神经网络（SNN）的理论和数学模型，并将其应用于生物医学问题。虽然论文主要关注图神经网络（GNN）的变体，但其核心是开发一种新的神经网络架构用于建模复杂关系数据。在化学信息学领域，分子通常被表示为图，图神经网络是化学大模型和质谱结构推理中的关键技术之一。论文通过一个具体的生物医学案例研究展示了SNN相对于主流GNN（如GCN、GAT、GraphSage）的优越性能，这为改进化学信息学中的分子表示学习提供了潜在的架构思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The purpose of this paper is to elucidate the theory and mathematical modelling behind the sheaf neural network (SNN) algorithm and then show how SNN can effectively answer to biomedical questions in a concrete case study and outperform the most popular graph neural networks (GNNs) as graph convolutional networks (GCNs), graph attention networks (GAT) and GraphSage.

</details>

---

### 60. [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](https://arxiv.org/abs/2603.03686)

**基本信息**

- 🔗 arXiv: [`2603.03686`](https://arxiv.org/abs/2603.03686)
- 👥 作者: Jiangyu Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03686.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是自动化化学配方设计，这是化学信息学和化学大模型的典型应用。提出的AI4S-SDS框架集成了多智能体、MCTS和可微物理引擎，直接围绕利用AI模型进行化学发现这一主题。

**📖 中文摘要**

本文提出了AI4S-SDS，一个用于自动化化学配方设计的神经符号框架。该框架集成了多智能体协作和定制的蒙特卡洛树搜索（MCTS）引擎，旨在解决化学配方设计这一高维组合空间导航问题。论文明确将化学配方设计（如光刻胶显影剂配方）作为应用场景，并引入了可微物理引擎来桥接符号推理和物理可行性，通过混合归一化损失和稀疏性诱导正则化来优化连续混合比例。这项工作直接针对化学信息学中的核心挑战——分子/配方空间的探索与优化，并提出了一个结合了大语言模型智能体与科学约束的先进框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.

</details>

---

### 61. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于计算材料发现（CMD）的AI优化方法（CliqueFlowmer），这属于化学信息学和化学大模型在材料设计领域的直接应用。

**📖 中文摘要**

本文针对计算材料发现（CMD）中的优化问题，提出了一种基于离线模型优化（MBO）的新方法CliqueFlowmer。该方法将目标材料属性的直接优化融合到生成过程中，克服了传统生成模型在探索材料空间有吸引力区域方面的不足。CliqueFlowmer结合了基于团的MBO最新进展与Transformer和流生成模型，专门用于材料优化问题。论文表明，该方法生成的材料在性能上显著优于生成式基线。这项工作直接面向化学信息学中的材料发现与优化，提供了一种新的、高效的AI驱动材料设计范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 62. [A Unified View of Drifting and Score-Based Models](https://arxiv.org/abs/2603.07514)

**基本信息**

- 🔗 arXiv: [`2603.07514`](https://arxiv.org/abs/2603.07514)
- 👥 作者: Chieh-Hsin Lai, Bac Nguyen, Naoki Murata 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07514.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从理论上统一漂移模型和基于分数的模型（扩散模型），这为理解生成式AI的核心机制提供了重要见解。生成模型（如扩散模型）是构建用于分子生成、质谱数据合成等任务的化学大模型的关键组成部分。

**📖 中文摘要**

本文从理论角度统一了漂移模型和基于分数的模型（如扩散模型）。论文证明，对于高斯核，群体均值漂移场与高斯平滑后的数据分布和模型分布之间的分数差相一致。这一恒等式源于Tweedie公式，表明高斯核漂移正是在平滑分布上的分数匹配式目标。这一理论工作建立了漂移模型与扩散模型核心机制（分数匹配）之间的深刻联系。扩散模型和分数匹配是当前生成式AI的基石，也被用于分子生成和质谱数据生成等化学信息学任务。因此，该理论分析为理解这些生成模型提供了统一视角，与构建化学大模型（尤其是生成模型）的理论基础相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drifting models train one-step generators by optimizing a mean-shift discrepancy induced by a kernel between the data and model distributions, with Laplace kernels used by default in practice. At each point, this discrepancy compares the kernel-weighted displacement toward nearby data samples with the corresponding displacement toward nearby model samples, yielding a transport direction for generated samples. In this paper, we make its relationship to the score-matching principle behind diffusion models precise by showing that drifting admits a score-based formulation on kernel-smoothed distributions. For Gaussian kernels, the population mean-shift field coincides with the score difference between the Gaussian-smoothed data and model distributions. This identity follows from Tweedie's formula, which links the score of a Gaussian-smoothed density to the corresponding conditional mean, and implies that Gaussian-kernel drifting is exactly a score-matching-style objective on smoothed distributions. It also clarifies the connection to Distribution Matching Distillation (DMD): both methods use score-mismatch transport directions, but drifting realizes the score signal nonparametrically from kernel neighborhoods, whereas DMD uses a pretrained diffusion teacher. Beyond Gaussians, we derive an exact decomposition for general radial kernels, and for the Laplace kernel we prove rigorous error bounds showing that drifting remains an accurate proxy for score matching in low-temperature and high-dimensional regimes.

</details>

---

### 63. [Nonparametric Variational Differential Privacy via Embedding Parameter Clipping](https://arxiv.org/abs/2603.09583)

**基本信息**

- 🔗 arXiv: [`2603.09583`](https://arxiv.org/abs/2603.09583)
- 👥 作者: Dina El Zein, Shashi Kumar, James Henderson
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09583.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进隐私保护语言模型的变分框架（NVDP/NVIB）。虽然应用场景是通用语言模型，但其理论和方法可直接迁移至需要隐私保护的化学大模型（例如，用于处理专利分子或私有质谱数据库的模型）的开发中。

**📖 中文摘要**

本文针对非参数变分差分隐私（NVDP）框架中的问题，提出了一种参数裁剪策略，以改进隐私保护语言模型的隐私-效用权衡。NVDP框架基于非参数变分信息瓶颈（NVIB），用于构建隐私保护的语言模型。论文从最小化Rényi散度上界的目标出发，数学推导出对后验均值、方差和混合权重参数的具体约束。虽然论文主要关注通用语言模型的隐私保护，但其提出的变分框架和优化方法对于处理敏感化学数据（如分子结构、质谱关联信息）的化学信息学模型具有重要的借鉴意义。在化学领域，保护分子结构的隐私同时进行有效学习是一个新兴挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The nonparametric variational information bottleneck (NVIB) provides the foundation for nonparametric variational differential privacy (NVDP), a framework for building privacy-preserving language models. However, the learned latent representations can drift into regions with high information content, leading to poor privacy guarantees, but also low utility due to numerical instability during training. In this work, we introduce a principled parameter clipping strategy to directly address this issue. Our method is mathematically derived from the objective of minimizing the Rényi Divergence (RD) upper bound, yielding specific, theoretically grounded constraints on the posterior mean, variance, and mixture weight parameters. We apply our technique to an NVIB based model and empirically compare it against an unconstrained baseline. Our findings demonstrate that the clipped model consistently achieves tighter RD bounds, implying stronger privacy, while simultaneously attaining higher performance on several downstream tasks. This work presents a simple yet effective method for improving the privacy-utility trade-off in variational models, making them more robust and practical.

</details>

---

### 64. [Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining](https://arxiv.org/abs/2603.11103)

**基本信息**

- 🔗 arXiv: [`2603.11103`](https://arxiv.org/abs/2603.11103)
- 👥 作者: Zhiyuan Zeng, Yichi Zhang, Yong Shan 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11103.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种通过模拟和重构中间推理轨迹来增强大语言模型对复杂结构化任务理解的新范式。这种方法论对于开发能够进行复杂推理的化学大模型（如逆合成分析、反应预测、分子性质优化）具有直接的启发和借鉴价值。

**📖 中文摘要**

本文提出了一种通过“重构理解”来增强大语言模型（LLMs）代码生成能力的新范式。作者认为，标准的预训练数据（静态代码仓库）只代表了复杂智力过程的最终状态，缺失了中间的规划、调试和迭代细化步骤。为了弥补这一差距，他们引入了一个通过多智能体模拟合成这些“智能体轨迹”的框架。该过程以源代码仓库的结构现实（如依赖图和文件层次结构）为基础，并采用基于搜索的优化技术来迭代细化思维链推理。这项工作虽然主要针对软件工程，但其核心思想——通过重构和模拟中间推理步骤来增强模型对复杂结构化生成任务的理解——与化学信息学高度相关。例如，在分子设计或逆合成规划中，模型同样需要理解从目标性质到分子结构，或从产物到反应路径的复杂、多步推理过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have achieved remarkable success in code generation, they often struggle with the deep, long-horizon reasoning required for complex software engineering. We attribute this limitation to the nature of standard pre-training data: static software repositories represent only the terminal state of an intricate intellectual process, abstracting away the intermediate planning, debugging, and iterative refinement. To bridge this gap, we propose a novel paradigm: understanding via reconstruction. We hypothesize that reverse-engineering the latent agentic trajectories -- the planning, reasoning, and debugging steps -- behind static repositories provides a far richer supervision signal than raw code alone. To operationalize this, we introduce a framework that synthesizes these trajectories using a multi-agent simulation. This process is grounded in the structural realities of the source repositories (e.g., dependency graphs and file hierarchies) to ensure fidelity. Furthermore, to guarantee the logical rigor of the synthetic data, we employ a search-based optimization technique that iteratively refines the Chain-of-Thought (CoT) reasoning to maximize the likelihood of the ground-truth code. Empirical results demonstrate that continuous pre-training on these reconstructed trajectories significantly enhances Llama-3-8B's performance across diverse benchmarks, including long-context understanding, coding proficiency, and agentic capabilities.

</details>

---

### 65. [To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation](https://arxiv.org/abs/2603.15159)

**基本信息**

- 🔗 arXiv: [`2603.15159`](https://arxiv.org/abs/2603.15159)
- 👥 作者: Yitong Zhang, Chengze Li, Ruize Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15159.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是教导大语言模型有效使用一个特定的、封闭的符号系统（私有库API）。这一挑战与化学信息学中让AI模型掌握和运用化学领域知识（如化合物数据库、反应规则、光谱解读规则）进行推理和生成的任务在本质上是一致的，为解决化学大模型和质谱结构推理中的领域知识集成问题提供了方法论参考。

**📖 中文摘要**

本文针对私有库导向的代码生成任务，提出了PriCoder方法，通过自动合成数据来教导大语言模型（LLMs）调用私有库API。现有方法主要依赖在推理时检索并注入API文档，但即使提供了准确的知识，LLMs仍难以有效调用。PriCoder将私有库数据合成建模为图构建问题，并交替使用两个图算子来提升数据的多样性和质量。实验表明，PriCoder能显著提升LLMs在私有库代码生成上的能力。虽然应用场景是软件工程，但其核心问题——如何让大模型有效学习和使用一个封闭、特定的符号系统（API）——与化学信息学中的关键挑战高度相似。例如，在质谱结构推理中，模型需要学习并正确调用庞大的化学知识库（如化合物数据库、反应规则、光谱解读规则）；在化学大模型中，模型需要内化并运用复杂的化学命名法、SMILES语法或分子描述符体系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability. Our code and benchmarks are publicly available at this https URL .

</details>

---

### 66. [Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences](https://arxiv.org/abs/2603.16313)

**基本信息**

- 🔗 arXiv: [`2603.16313`](https://arxiv.org/abs/2603.16313)
- 👥 作者: Hugo Math
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16313.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容围绕利用大语言模型（LLM）对高维、结构化的科学数据进行建模、预测和因果推理，这与“化学大模型”主题直接相关，展示了LLM在科学数据分析（类比于化学信息学中的质谱或分子数据）中的应用框架。

**📖 中文摘要**

这篇论文提出了一种将事件序列建模、因果发现和大语言模型（LLM）统一起来的框架，用于高维事件流（如车辆诊断代码）的自动化故障诊断。论文的核心是将诊断序列视为一种可以建模、预测和解释的语言。这直接与“化学大模型”主题相关，因为它展示了如何将LLM应用于结构化、高维的科学数据（这里是诊断代码序列）进行推理和解释。论文中提出的多智能体系统可以自动合成布尔规则，这体现了大模型在复杂科学推理任务中的应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>

---

### 67. [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](https://arxiv.org/abs/2603.17380)

**基本信息**

- 🔗 arXiv: [`2603.17380`](https://arxiv.org/abs/2603.17380)
- 👥 作者: Shuizhou Chen, Lang Yu, Kedu Jin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17380.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建一个用于生物信息学（虚拟细胞扰动预测）的大规模基础模型（SCALE），并集成了LLaMA等大型语言模型进行细胞编码。这属于“化学大模型”在生命科学和生物化学交叉领域的应用实例。

**📖 中文摘要**

这篇论文提出了一个名为SCALE的大规模基础模型，用于虚拟细胞扰动预测。该模型将扰动预测表述为条件传输问题，并使用了一个结合LLaMA编码的集合感知流架构。模型在生物数据集Tahoe-100M上进行了评估。这项工作代表了在生物信息学领域构建和应用大型基础模型的努力，旨在实现可扩展、稳定且具有生物学意义的预测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Virtual cell models aim to enable in silico experimentation by predicting how cells respond to genetic, chemical, or cytokine perturbations from single-cell measurements. In practice, however, large-scale perturbation prediction remains constrained by three coupled bottlenecks: inefficient training and inference pipelines, unstable modeling in high-dimensional sparse expression space, and evaluation protocols that overemphasize reconstruction-like accuracy while underestimating biological fidelity. In this work we present a specialized large-scale foundation model SCALE for virtual cell perturbation prediction that addresses the above limitations jointly. First, we build a BioNeMo-based training and inference framework that substantially improves data throughput, distributed scalability, and deployment efficiency, yielding 12.51* speedup on pretrain and 1.29* on inference over the prior SOTA pipeline under matched system settings. Second, we formulate perturbation prediction as conditional transport and implement it with a set-aware flow architecture that couples LLaMA-based cellular encoding with endpoint-oriented supervision. This design yields more stable training and stronger recovery of perturbation effects. Third, we evaluate the model on Tahoe-100M using a rigorous cell-level protocol centered on biologically meaningful metrics rather than reconstruction alone. On this benchmark, our model improves PDCorr by 12.02% and DE Overlap by 10.66% over STATE. Together, these results suggest that advancing virtual cells requires not only better generative objectives, but also the co-design of scalable infrastructure, stable transport modeling, and biologically faithful evaluation.

</details>

---

### 68. [Cell-cell Communication Inference and Analysis: Biological Mechanisms, Computational Approaches, and Future Opportunities](https://arxiv.org/abs/2512.03497)

**基本信息**

- 🔗 arXiv: [`2512.03497`](https://arxiv.org/abs/2512.03497)
- 👥 作者: Xiangzheng Cheng, Haili Huang, Ye Su 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03497.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对从组学数据中推断细胞间通讯这一主题的综合性综述。虽然其直接应用在生物学，但其核心——从复杂、高维的生物数据中提取关系和模式——所涉及的计算方法（包括可能基于图的或机器学习的方法）与化学信息学中从质谱等数据推断分子结构或相互作用的理念高度相关，属于重要的相关讨论范畴。

**📖 中文摘要**

这篇论文是一篇综述，全面概述了从单细胞和空间组学数据中推断和分析细胞间通讯（CCC）的计算方法。它介绍了超过140种计算方法，涵盖了方法框架的多样性和所解决的生物学问题。论文讨论了当前挑战和未来机遇，并提供了一个在线资源以方便方法比较和选择。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In multicellular organisms, cells coordinate their activities through cell-cell communication (CCC), which is crucial for development, tissue homeostasis, and disease progression. Recent advances in single-cell and spatial omics technologies provide unprecedented opportunities to systematically infer and analyze CCC from these omics data, either by integrating prior knowledge of ligand-receptor interactions (LRIs) or through de novo approaches. A variety of computational methods have been developed, focusing on methodological innovations, accurate modeling of complex signaling mechanisms, and investigation of broader biological questions. These advances have greatly enhanced our ability to analyze CCC and generate biological hypotheses. Here, we introduce the biological mechanisms and modeling strategies of CCC, and provide a focused overview of more than 140 computational methods for inferring CCC from single-cell and spatial transcriptomic data, emphasizing the diversity in methodological frameworks and biological questions. Finally, we discuss the current challenges and future opportunities in this rapidly evolving field, and summarize available methods in an interactive online resource ( this https URL ) to facilitate more efficient method comparison and selection.

</details>

---

### 69. [Generalization of Long-Range Machine Learning Potentials in Complex Chemical Spaces](https://arxiv.org/abs/2512.10989)

**基本信息**

- 🔗 arXiv: [`2512.10989`](https://arxiv.org/abs/2512.10989)
- 👥 作者: Michal Sanocki, Julija Zavadlav
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10989.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升机器学习原子间势（MLIP）——一种化学领域的大模型——在复杂化学空间中的泛化能力。这直接关系到“化学大模型”的开发、评估和应用，特别是针对材料科学和计算化学中的模型泛化挑战。

**📖 中文摘要**

这篇论文系统地评估了不同具有长程修正的机器学习原子间势（MLIP）架构在多样化化学空间中的泛化能力。论文强调了长程建模对于实现可泛化MLIP的重要性，并引入了有偏的训练-测试分割策略来严格评估模型在化学空间未见区域的性能。研究以金属-有机框架为例，但方法可广泛应用于其他材料。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vastness of chemical space makes generalization a central challenge in the development of machine learning interatomic potentials (MLIPs). While MLIPs could enable large-scale atomistic simulations with near-quantum accuracy, their usefulness is often limited by poor transferability to out-of-distribution samples. Here, we systematically evaluate different MLIP architectures with long-range corrections across diverse chemical spaces and show that such schemes are essential, not only for improving in-distribution performance but, more importantly, for enabling significant gains in transferability to unseen regions of chemical space. To enable a more rigorous benchmarking, we introduce biased train-test splitting strategies, which explicitly test the model performance in significantly different regions of chemical space. Together, our findings highlight the importance of long-range modeling for achieving generalizable MLIPs and provide a framework for diagnosing systematic failures across chemical space. Although we demonstrate our methodology on metal-organic frameworks, it is broadly applicable to other materials, offering insights into the design of more robust and transferable MLIPs.

</details>

---

### 70. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准3：论文是一篇展望性文章，专门讨论并展望了机器学习大模型（如量子精度的ML势函数）与高性能/量子计算在化学和药物发现领域的融合前景。它包含了对“化学大模型”未来发展方向的重要讨论和展望。

**📖 中文摘要**

这篇论文是一篇前瞻性文章，探讨了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何为下一代药物发现提供决定性解决方案。论文指出，机器学习基础模型（如FeNNix-Bio1）能够实现量子精度的模拟，而高性能量子计算（HPQC）将成为量子化学数据的终极加速器。文章详细描述了这种三方融合如何优化从系统准备到高保真模拟的整个药物发现流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

## 📊 数据统计
- 累计运行天数：42
- 累计论文数量：3021

## 📝 历史记录

> 暂无历史数据

