# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-20 12:45:12

## 📅 2026-03-20 (今日最新)

**相关论文数：70**

### 1. [Continually self-improving AI](https://arxiv.org/abs/2603.18073)

**基本信息**

- 🔗 arXiv: [`2603.18073`](https://arxiv.org/abs/2603.18073)
- 👥 作者: Zitong Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕如何构建能够持续自我改进、减少对人类数据和算法依赖的AI大模型，这与“化学大模型”主题高度相关，为构建该领域的专用大模型提供了方法论思路。

**📖 中文摘要**

这篇论文探讨了如何创建持续自我改进的AI系统，以克服当前语言模型在知识获取、数据依赖和训练算法方面的根本限制。论文提出了三个核心章节：首先，通过合成数据方法，将小型专业语料库多样化和放大，使模型能够从有限的源材料中高效更新其参数，从而克服知识获取中的数据效率障碍。其次，为了减少对人类数据的依赖，论文展示了在给定固定数量的人类数据的情况下，模型可以自我生成合成数据来引导其基本预训练能力，而无需从任何现成的、经过指令调优的语言模型中进行蒸馏。最后，为了超越人类设计的训练范式，论文证明了通过在算法空间上进行扩展搜索，AI可以探索比人类研究人员手动探索更大的学习算法配置空间。这项工作直接与“化学大模型”主题相关，因为它专注于开发能够持续学习和自我改进的、不依赖于固定人类数据或算法的大型模型框架，这是构建领域专用化学大模型（如用于质谱分析）的关键愿景。

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

满足标准1：论文的核心研究内容是关于如何高效地将大型语言模型适应到复杂的技术服务领域，这直接关系到如何构建和优化用于“化学信息学”和“质谱分析”等专业领域的“化学大模型”。

**📖 中文摘要**

本文提出了一个轻量级适应框架，用于在复杂的专业技术服务领域（如云服务）中适配大型语言模型（LLM）。该框架旨在解决人类演示中缺乏显式认知链以及有效响应多样性带来的固有模糊性等问题，这些问题严重阻碍了智能体内化潜在决策动态并进行有效泛化。框架包含三个关键贡献：1）潜在逻辑增强：通过引入规划感知轨迹建模和决策推理增强，弥合表面监督与潜在决策逻辑之间的差距，从而增强监督微调对齐的稳定性。2）鲁棒噪声降低：通过双重过滤方法构建多真实答案数据集，通过验证多样化响应来降低噪声，从而捕捉语义多样性。3）轻量级适应：设计了一个混合奖励机制，融合了基于LLM的评判器和轻量级基于相关性的重排序器，以提取高保真度的奖励信号，同时降低与标准LLM-as-a-Judge强化学习相比的计算成本。该框架在真实世界的云服务任务上进行了评估，展示了其通过潜在逻辑增强和鲁棒噪声降低实现的稳定性和性能提升。这项工作与“化学大模型”主题相关，因为它提供了一种高效、轻量化的方法来使通用大模型适应特定、复杂的专业领域（如化学信息学或质谱分析），这对于开发领域专用的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting Large Language Models in complex technical service domains is constrained by the absence of explicit cognitive chains in human demonstrations and the inherent ambiguity arising from the diversity of valid responses. These limitations severely hinder agents from internalizing latent decision dynamics and generalizing effectively. Moreover, practical adaptation is often impeded by the prohibitive resource and time costs associated with standard training paradigms. To overcome these challenges and guarantee computational efficiency, we propose a lightweight adaptation framework comprising three key contributions. (1) Latent Logic Augmentation: We introduce Planning-Aware Trajectory Modeling and Decision Reasoning Augmentation to bridge the gap between surface-level supervision and latent decision logic. These approaches strengthen the stability of Supervised Fine-Tuning alignment. (2) Robust Noise Reduction: We construct a Multiple Ground Truths dataset through a dual-filtering method to reduce the noise by validating diverse responses, thereby capturing the semantic diversity. (3) Lightweight Adaptation: We design a Hybrid Reward mechanism that fuses an LLM-based judge with a lightweight relevance-based Reranker to distill high-fidelity reward signals while reducing the computational cost compared to standard LLM-as-a-Judge reinforcement learning. Empirical evaluations on real-world Cloud service tasks, conducted across semantically diverse settings, demonstrate that our framework achieves stability and performance gains through Latent Logic Augmentation and Robust Noise Reduction. Concurrently, our Hybrid Reward mechanism achieves alignment comparable to standard LLM-as-a-judge methods with reduced training time, underscoring the practical value for deploying technical service agents.

</details>

---

### 3. [HWE-Bench: Can Language Models Perform Board-level Schematic Designs?](https://arxiv.org/abs/2603.18102)

**基本信息**

- 🔗 arXiv: [`2603.18102`](https://arxiv.org/abs/2603.18102)
- 👥 作者: Weibo Qiu, Yinhao Xiao, Runyu Pan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18102.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估LLM在需要深厚领域知识和物理理解的复杂工程任务（电路设计）上的能力。这为如何评估和构建在“化学信息学”和“质谱分析”领域具有类似深度理解和推理能力的“化学大模型”提供了直接的参考范例和方法论启示。

**📖 中文摘要**

本文提出了HWE-Bench评估框架，用于基准测试大型语言模型（LLM）执行板级电路设计的能力。该任务需要协同理解真实世界的物理原理和集成电路（IC）数据手册。HWE-Bench包含300个从开源和众包平台收集的板级设计任务，涵盖8个应用领域，并辅以一个包含2,914份真实IC数据手册的知识库。对于每个任务，LLM需要根据提供的电路功能要求和一组组件数据手册作为输入，从头开始生成原理图。生成的原理图将根据静态电气规则进行检查，然后传递给电路模拟器以验证其动态行为。评估表明，尽管当前模型实现了初步的工程可用性和文档理解，但它们缺乏物理直觉。这项工作与“化学大模型”主题高度相关，因为它系统地评估了LLM在需要深厚领域知识（数据手册）和物理理解（电路行为）的复杂工程任务上的能力。这为评估LLM在化学领域（如理解质谱仪原理、解析化学文献或设计分子合成路径）的类似能力提供了一个极佳的类比和参考框架。构建化学大模型同样需要模型理解复杂的领域特定数据（如质谱图、化学数据库）和物理化学原理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated significant potential in various engineering tasks, including software development, digital logic generation, and companion document maintenance. However, their ability to perform board-level circuit design is understudied, as this task requires a synergized understanding of real-world physics and Integrated Circuit (IC) datasheets, the latter comprising detailed specifications for individual components. To address this challenge, we propose \hweb, an evaluation framework that benchmarks the ability of LLMs to perform such designs. It consists of 300 board-level design tasks pulled from open-source and crowdsourcing platforms such as GitHub and OSHWLab, covering 8 application domains, and is complemented with a knowledge base of 2,914 real IC datasheets. For each task, the LLMs are tasked with generating a schematic from scratch, using the provided circuit functional requirements and a set of component datasheets as input. The resulting schematic will be checked against a static electrical rules, and then passed to a circuit simulator to verify its dynamic behavior. Our evaluation show that although current models achieve initial engineering usability and documentation understanding, they lack physical intuition, as the top-performing model achieved an overall pass rate of 8.15\%. We envision that advancements on \hweb\ will pave the way for the development of practical Electronic Design Automation (EDA) agents, revolutionizing the field of board-level design.

</details>

---

### 4. [LLM-Augmented Computational Phenotyping of Long Covid](https://arxiv.org/abs/2603.18115)

**基本信息**

- 🔗 arXiv: [`2603.18115`](https://arxiv.org/abs/2603.18115)
- 👥 作者: Jing Wang, Jie Shen, Amar Sra 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18115.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是利用LLM增强的框架从复杂数据中进行表型发现，这直接展示了LLM（作为“大模型”的一种）在复杂科学数据分析中的应用。同时，该方法论具有通用性，为“质谱结构推理”中从海量质谱数据中提取模式和进行亚结构分类提供了可借鉴的技术框架。

**📖 中文摘要**

本文提出了一个名为“Grace Cycle”的LLM增强计算表型框架，用于从纵向患者数据中发现具有临床意义的亚组。该框架迭代地整合假设生成、证据提取和特征细化。作者将其应用于13,511名长新冠参与者数据，识别出三种不同的临床表型。该框架是疾病无关的，为从复杂的纵向数据中发现临床可解释的亚表型提供了一种通用方法。这项工作与“化学大模型”和“质谱结构推理”主题相关，因为它展示了一种将大型语言模型整合到原则性、统计基础的数据分析流程中的方法，用于从复杂数据（如质谱数据集）中提取模式和见解。在化学信息学中，类似的方法可以用于从大量的质谱数据中识别分子亚结构模式、推断化合物类别或发现新的生物标志物，从而辅助“质谱结构推理”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phenotypic characterization is essential for understanding heterogeneity in chronic diseases and for guiding personalized interventions. Long COVID, a complex and persistent condition, yet its clinical subphenotypes remain poorly understood. In this work, we propose an LLM-augmented computational phenotyping framework ``Grace Cycle'' that iteratively integrates hypothesis generation, evidence extraction, and feature refinement to discover clinically meaningful subgroups from longitudinal patient data. The framework identifies three distinct clinical phenotypes, Protected, Responder, and Refractory, based on 13,511 Long Covid participants. These phenotypes exhibit pronounced separation in peak symptom severity, baseline disease burden, and longitudinal dose-response patterns, with strong statistical support across multiple independent dimensions. This study illustrates how large language models can be integrated into a principled, statistically grounded pipeline for phenotypic screening from complex longitudinal data. Note that the proposed framework is disease-agnostic and offers a general approach for discovering clinically interpretable subphenotypes.

</details>

---

### 5. [A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective](https://arxiv.org/abs/2603.18126)

**基本信息**

- 🔗 arXiv: [`2603.18126`](https://arxiv.org/abs/2603.18126)
- 👥 作者: Zhengze Xiao, Xuanzhe Ding, Yuyang Lou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18126.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和优化用于量子化学计算的神经网络模型（NNVMC），这些模型是“化学大模型”在计算化学领域的一个重要子类和具体应用。论文对其计算特性的深入分析直接关系到此类模型的可扩展性和实用性。

**📖 中文摘要**

本文从计算工作负载特征的角度，对神经网络变分蒙特卡洛（NNVMC）方法进行了综述和实证GPU性能分析。NNVMC通过将变分蒙特卡洛与富有表现力的神经网络波函数拟设相结合，已成为解决量子多体问题的一种有前景的范式。论文分析了四种代表性拟设（PauliNet, FermiNet, Psiformer, Orbformer）的模型级运行时和内存趋势，以及内核级行为。研究结果表明，端到端性能通常受到低强度元素级和数据移动内核的限制，而计算/内存平衡在不同拟设和阶段之间存在显著差异。基于这些发现，论文讨论了可扩展NNVMC系统的算法-硬件协同设计意义。这项工作与“化学大模型”主题间接相关，因为它深入分析了用于解决量子化学核心问题（电子结构计算）的专用神经网络模型的计算特性。这些模型本身就是“化学大模型”在量子化学领域的具体体现。理解它们的计算瓶颈和优化策略，对于未来构建更大规模、更高效的用于化学模拟和性质预测的专用大模型具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Network Variational Monte Carlo (NNVMC) has emerged as a promising paradigm for solving quantum many-body problems by combining variational Monte Carlo with expressive neural-network wave-function ansätze. Although NNVMC can achieve competitive accuracy with favorable asymptotic scaling, practical deployment remains limited by high runtime and memory cost on modern graphics processing units (GPUs). Compared with language and vision workloads, NNVMC execution is shaped by physics-specific stages, including Markov-Chain Monte Carlo sampling, wave-function construction, and derivative/Laplacian evaluation, which produce heterogeneous kernel behavior and nontrivial bottlenecks. This paper provides a workload-oriented survey and empirical GPU characterization of four representative ansätze: PauliNet, FermiNet, Psiformer, and Orbformer. Using a unified profiling protocol, we analyze model-level runtime and memory trends and kernel-level behavior through family breakdown, arithmetic intensity, roofline positioning, and hardware utilization counters. The results show that end-to-end performance is often constrained by low-intensity elementwise and data-movement kernels, while the compute/memory balance varies substantially across ansätze and stages. Based on these findings, we discuss algorithm--hardware co-design implications for scalable NNVMC systems, including phase-aware scheduling, memory-centric optimization, and heterogeneous acceleration.

</details>

---

### 6. [CWoMP: Morpheme Representation Learning for Interlinear Glossing](https://arxiv.org/abs/2603.18184)

**基本信息**

- 🔗 arXiv: [`2603.18184`](https://arxiv.org/abs/2603.18184)
- 👥 作者: Morris Alper, Enora Rice, Bhargav Shandilya 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18184.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种用于处理组合结构序列数据的新表示学习方法。该方法论（原子化单元表示、对比学习、词典检索）为“质谱结构推理”任务提供了一种新颖且可能更可解释的技术路径，即如何从质谱信号中识别和组合化学子结构来推断完整分子。

**📖 中文摘要**

本文提出了CWoMP（对比词-语素预训练）方法，用于语言文档中的语际标注（IGT）任务。与将词缀视为字符序列的现有方法不同，CWoMP将语素视为具有学习表示的原子形式-意义单元。通过对比训练的编码器，将上下文中的单词与其组成语素在共享嵌入空间中对齐；然后，自回归解码器通过从这些嵌入的可变词典中检索条目来生成语素序列。预测结果是可解释的——基于词典条目——用户可以通过扩展词典在推理时改进结果，而无需重新训练。该方法在多种低资源语言上进行了评估。这项工作与“化学大模型”和“质谱结构推理”主题相关，因为它提出了一种新的、可解释的表示学习方法，用于处理具有组合结构的序列数据（语素序列）。在化学领域，分子可以视为原子和官能团（类似于语素）的组合。CWoMP中学习原子化单元表示、构建可变词典以及进行组合推理的思想，可以迁移到“质谱结构推理”任务中，用于学习化学子结构的表示，并从质谱数据中组合推理出完整的分子结构，从而提高模型的可解释性和在低数据资源下的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Interlinear glossed text (IGT) is a standard notation for language documentation which is linguistically rich but laborious to produce manually. Recent automated IGT methods treat glosses as character sequences, neglecting their compositional structure. We propose CWoMP (Contrastive Word-Morpheme Pretraining), which instead treats morphemes as atomic form-meaning units with learned representations. A contrastively trained encoder aligns words-in-context with their constituent morphemes in a shared embedding space; an autoregressive decoder then generates the morpheme sequence by retrieving entries from a mutable lexicon of these embeddings. Predictions are interpretable--grounded in lexicon entries--and users can improve results at inference time by expanding the lexicon without retraining. We evaluate on diverse low-resource languages, showing that CWoMP outperforms existing methods while being significantly more efficient, with particularly strong gains in extremely low-resource settings.

</details>

---

### 7. [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](https://arxiv.org/abs/2603.18256)

**基本信息**

- 🔗 arXiv: [`2603.18256`](https://arxiv.org/abs/2603.18256)
- 👥 作者: Philippe Formont, Maxime Darrin, Ismail Ben Ayed 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18256.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用推理大型语言模型进行从头分子生成，这是“化学大模型”在药物发现和分子设计领域的具体应用。

**📖 中文摘要**

本文介绍了MolRGen，这是一个用于训练和评估基于推理的大型语言模型（LLMs）进行从头分子生成的大规模基准和数据集。该研究旨在弥补现有方法在从头分子生成（即生成优化期望得分的新分子，而无需已知的高分候选分子）方面的监督空白。MolRGen提出了一个评估和训练模型用于从头分子生成和性质预测的设置，并引入了一种新颖的多样性感知top-k评分，以捕捉生成分子的质量和多样性。作者展示了该设置可用于训练LLMs进行分子生成，他们使用强化学习训练了一个240亿参数的LLM，并对其性能和局限性进行了详细分析。这项工作直接针对化学信息学中的“化学大模型”主题，特别是利用推理LLMs进行分子设计。

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

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一种新的深度学习框架（离散流匹配）用于从质谱进行从头分子结构解析。

**📖 中文摘要**

本文提出了FlowMS，这是首个用于谱图条件从头分子生成的离散流匹配框架。该工作针对质谱（MS）从头结构解析的挑战，即从质谱碎片模式推断分子结构。FlowMS通过在概率空间中进行迭代精化来生成分子图，同时强制执行化学式约束，并以来自预训练公式Transformer编码器的谱图嵌入为条件。该方法在NPLIB1基准测试的6个指标中的5个上实现了最先进的性能，包括9.15%的top-1准确率（相对于DiffMS有9.7%的相对改进）和7.96的top-10 MCES（相对于MS-BART有4.2%的改进）。这些结果表明，离散流匹配是质谱学中基于质谱的结构解析（如代谢组学和天然产物发现）的一个有前景的范式。

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

满足标准1：论文的核心研究内容涉及使用可解释AI技术（稀疏自编码器）来理解和解释神经模型的内部表示。这种方法论与化学信息学中试图理解和解释“化学大模型”（如分子表示模型）内部工作机制的研究主题直接相关。

**📖 中文摘要**

本文研究了神经音频编解码器（NACs）如何编码语言和副语言信息，并专注于一个具有挑战性的副语言属性——口音。作者采用稀疏自编码器（SAEs）将密集的NAC表示分解为稀疏、可解释的激活，以提高NAC表示的可解释性。他们提出了一个量化NAC可解释性的框架，并在16种SAE配置下评估了四种NAC模型。研究结果表明，声学导向和语音导向的NACs在编码口音信息的方式上存在差异。这项工作通过可解释AI技术（稀疏自编码器）深入探究了神经音频模型内部表示与特定属性（如口音）之间的关系，虽然应用领域是音频，但其方法论（使用SAEs分解和理解神经表示）与化学信息学中理解“化学大模型”内部表示的研究思路高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented NACs encode accent information primarily in activation magnitudes of sparse representations, whereas phonetic-oriented NACs rely more on activation positions, and that low-bitrate EnCodec variants show higher interpretability.

</details>

---

### 10. [Synthetic Data Generation for Training Diversified Commonsense Reasoning Models](https://arxiv.org/abs/2603.18361)

**基本信息**

- 🔗 arXiv: [`2603.18361`](https://arxiv.org/abs/2603.18361)
- 👥 作者: Tianhui Zhang, Bei Peng, Danushka Bollegala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18361.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种生成合成数据集的方法，用于训练多样化的常识推理模型。这种为特定任务（多样化生成）创建数据资源的方法，可以类比并应用于“化学大模型”领域，为解决化学数据稀缺或构建特定属性的分子数据集提供思路和工具。

**📖 中文摘要**

本文针对多样化常识推理生成器训练数据缺乏的问题，提出了一种两阶段方法来创建首个用于多样化生成式常识推理（GCR）的合成数据集CommonSyn。由于高质量多样化常识训练数据集的标注成本高昂，现有数据集规模小且覆盖场景狭窄。作者的方法旨在解决这一训练资源缺口。实验表明，使用该合成数据微调的模型，在生成多样性和质量上均优于原始模型以及在人工标注数据集上微调的模型。这项工作为训练能够产生多样化、高质量响应的对话代理提供了数据资源，其数据生成方法对于构建和增强“化学大模型”的训练数据集（例如用于分子性质预测或生成的多样化数据）具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Conversational agents are required to respond to their users not only with high quality (i.e. commonsense bearing) responses, but also considering multiple plausible alternative scenarios, reflecting the diversity in their responses. Despite the growing need to train diverse commonsense generators, the progress of this line of work has been significantly hindered by the lack of large-scale high-quality diverse commonsense training datasets. Due to the high annotation costs, existing Generative Commonsense Reasoning (GCR) datasets are created using a small number of human annotators, covering only a narrow set of commonsense scenarios. To address this training resource gap, we propose a two-stage method to create the first-ever synthetic dataset CommonSyn for diversified (GCR). The model fine-tuned on our synthetic data jointly increase both generation diversity and quality compared with vanilla models and the model fine-tuned on human-crafted dataset across different size Large Language Models (LLMs)

</details>

---

### 11. [Seeking Universal Shot Language Understanding Solutions](https://arxiv.org/abs/2603.18448)

**基本信息**

- 🔗 arXiv: [`2603.18448`](https://arxiv.org/abs/2603.18448)
- 👥 作者: Haoxin Liu, Harshavardhan Kamarthi, Zhiyuan Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18448.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个大规模、多维度、带注释的数据集（SLU-SUITE），用于训练和评估视觉语言模型。这种构建高质量、结构化数据集以支持模型训练和评估的方法，与化学信息学和质谱分析领域构建用于化学大模型或质谱结构推理的数据集和基准任务在本质上是一致的。

**📖 中文摘要**

这篇论文提出了SLU-SUITE，一个用于镜头语言理解（SLU）的综合训练和评估套件，包含49万个带注释的问答对，涵盖33个任务和六个电影维度。SLU是电影分析的关键任务，但因其多样性和主观性而具有挑战性。论文观察到视觉语言模型（VLMs）在SLU任务上与电影专家存在判断差异。为了弥合这一差距，论文从模型和数据两个角度提出了两种通用SLU解决方案：UniShot（一个通过动态平衡数据混合训练的通用模型）和AgentShots（一个最大化各维度性能的专家集群）。这些模型在领域内任务上超越了特定任务的集成模型，并在领域外任务上领先商业VLMs 22%。虽然论文主要关注电影分析，但其核心是构建和利用大规模、多维度、带注释的数据集来训练和评估视觉语言模型，这与化学信息学中构建用于质谱结构推理或化学大模型训练的数据集和基准在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Shot language understanding (SLU) is crucial for cinematic analysis but remains challenging due to its diverse cinematographic dimensions and subjective expert judgment. While vision-language models (VLMs) have shown strong ability in general visual understanding, recent studies reveal judgment discrepancies between VLMs and film experts on SLU tasks. To address this gap, we introduce SLU-SUITE, a comprehensive training and evaluation suite containing 490K human-annotated QA pairs across 33 tasks spanning six film-grounded dimensions. Using SLU-SUITE, we originally observe two insights into VLM-based SLU from: the model side, which diagnoses key bottlenecks of modules; the data side, which quantifies cross-dimensional influences among tasks. These findings motivate our universal SLU solutions from two complementary paradigms: UniShot, a balanced one-for-all generalist trained via dynamic-balanced data mixing, and AgentShots, a prompt-routed expert cluster that maximizes peak dimension performance. Extensive experiments show that our models outperform task-specific ensembles on in-domain tasks and surpass leading commercial VLMs by 22% on out-of-domain tasks.

</details>

---

### 12. [Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images](https://arxiv.org/abs/2603.18461)

**基本信息**

- 🔗 arXiv: [`2603.18461`](https://arxiv.org/abs/2603.18461)
- 👥 作者: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18461.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种整合外部生物数据（单细胞RNA测序数据集）来构建细胞类型原型，并用于增强模型预测的方法。这种利用公开数据集构建生物原型或先验知识，并将其整合到机器学习模型中的范式，与化学信息学中利用已知化学结构数据库或质谱库来辅助质谱结构推理或训练化学大模型的思路高度相关。

**📖 中文摘要**

这篇论文提出了一种细胞类型原型信息神经网络（CPNN），用于从病理图像中估计基因表达谱。该方法的关键创新在于利用公开可用的单细胞RNA测序数据集来获取细胞类型原型（即反映稳定基因共变性的平均表达谱）。CPNN直接从图像中学习细胞类型组成权重，并建模原型与观察到的批量或空间表达之间的关系，从而提供了一个有生物学基础且结构正则化的预测框架。论文在三个切片级数据集和三个斑块级空间转录组学数据集上进行了评估，CPNN在斯皮尔曼相关性方面均取得了最佳性能。该方法通过可视化推断的组成权重，为哪些细胞类型驱动预测的表达提供了可解释的见解。这项工作展示了如何整合外部生物数据（单细胞RNA测序）来增强基于图像的预测模型的生物学合理性和可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Estimating slide- and patch-level gene expression profiles from pathology images enables rapid and low-cost molecular analysis with broad clinical impact. Despite strong results, existing approaches treat gene expression as a mere slide- or spot-level signal and do not incorporate the fact that the measured expression arises from the aggregation of underlying cell-level expression. To explicitly introduce this missing cell-resolved guidance, we propose a Cell-type Prototype-informed Neural Network (CPNN) that leverages publicly available single-cell RNA-sequencing datasets. Since single-cell measurements are noisy and not paired with histology images, we first estimate cell-type prototypes-mean expression profiles that reflect stable gene-gene co-variation this http URL then learns cell-type compositional weights directly from images and models the relationship between prototypes and observed bulk or spatial expression, providing a biologically grounded and structurally regularized prediction framework. We evaluate CPNN on three slide-level datasets and three patch-level spatial transcriptomics datasets. Across all settings, CPNN achieves the highest performance in terms of Spearman correlation. Moreover, by visualizing the inferred compositional weights, our framework provides interpretable insights into which cell types drive the predicted expression. Code is publicly available at this https URL .

</details>

---

### 13. [A Faster Deterministic Algorithm for Kidney Exchange via Representative Set](https://arxiv.org/abs/2603.18471)

**基本信息**

- 🔗 arXiv: [`2603.18471`](https://arxiv.org/abs/2603.18471)
- 👥 作者: Kangyi Tian, Mingyu Xiao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18471.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为CAPSUL的新基准数据集，该数据集整合了蛋白质的3D结构信息和详细的亚细胞定位注释。构建这种结合结构信息与功能注释的高质量、综合性数据集，对于训练和评估化学信息学或生物信息学领域的大模型（例如用于蛋白质功能预测或结构-性质关系建模的模型）至关重要，与关注主题中构建数据资源的方向高度一致。

**📖 中文摘要**

这篇论文介绍了CAPSUL，一个用于蛋白质亚细胞定位的综合人类蛋白质基准。该基准的关键贡献在于提供了一个数据集，该数据集整合了多样化的3D结构表示与由领域专家精心策划的细粒度亚细胞定位注释。论文指出，尽管从生物学上认识到亚细胞定位与蛋白质结构密切相关，但现有数据集缺乏全面的3D结构信息和详细的亚细胞定位注释，这严重阻碍了有前景的基于结构的模型在此任务上的应用。CAPSUL填补了这一空白。论文使用各种最先进的基于序列和基于结构的模型评估了该基准，展示了在此任务中引入结构特征的重要性。此外，论文还探索了重加权和单标签分类策略，以促进未来对此任务基于结构方法的研究。最后，通过一个关于高尔基体的案例研究，展示了基于结构方法的强大可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Kidney Exchange Problem is a prominent challenge in healthcare and economics, arising in the context of organ transplantation. It has been extensively studied in artificial intelligence and optimization. In a kidney exchange, a set of donor-recipient pairs and altruistic donors are considered, with the goal of identifying a sequence of exchange -- comprising cycles or chains starting from altruistic donors -- such that each donor provides a kidney to the compatible recipient in the next donor-recipient pair. Due to constraints in medical resources, some limits are often imposed on the lengths of these cycles and chains. These exchanges create a network of transplants aimed at maximizing the total number, $t$, of successful transplants. Recently, this problem was deterministically solved in $O^*(14.34^t)$ time (IJCAI 2024). In this paper, we introduce the representative set technique for the Kidney Exchange Problem, showing that the problem can be deterministically solved in $O^*(6.855^t)$ time.

</details>

---

### 14. [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505)

**基本信息**

- 🔗 arXiv: [`2603.18505`](https://arxiv.org/abs/2603.18505)
- 👥 作者: Jingzhi Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18505.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于人工智能在蛋白质科学中应用的综述，特别涵盖了生成框架（如扩散模型）用于捕获构象分布、多模态表示整合以及功能推断等前沿主题。这些主题（生成模型、多模态整合）与“化学大模型”和“质谱结构推理”（后者可视为从光谱数据推断分子构象）的研究方向高度相关。论文对当前瓶颈和未来方向的讨论，为化学信息学和质谱分析领域的相关研究提供了重要的前瞻性视角。

**📖 中文摘要**

这篇论文是一篇综述，系统地审视了人工智能驱动的蛋白质科学在五个相互关联维度上的范式转变：统一的多模态表示（整合序列、几何和文本知识）；通过无MSA架构和全原子复合物建模改进静态预测；生成框架（包括扩散模型和流匹配）以捕获与热力学系综一致的构象分布；预测跨越蛋白质-配体、蛋白质-核酸和蛋白质-蛋白质复合物的异质相互作用；以及对适应度景观、突变效应和文本引导属性预测的功能推断。论文批判性地分析了当前的瓶颈，包括数据分布偏差、有限的机制可解释性以及几何指标与生物物理现实之间的脱节，同时确定了未来朝着物理一致的生成模型、多模态基础架构和实验闭环系统发展的方向。这篇综述标志着人工智能从结构分析工具向能够理解并最终重写生命动态语言的通用模拟器的转变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular interactions. This review systematically examines the paradigm shift in AI driven protein science across five interconnected dimensions: unified multimodal representations that integrate sequences, geometries, and textual knowledge; refinement of static prediction through MSA free architectures and all atom complex modeling; generative frameworks, including diffusion models and flow matching, that capture conformational distributions consistent with thermodynamic ensembles; prediction of heterogeneous interactions spanning protein ligand, protein nucleic acid, and protein protein complexes; and functional inference of fitness landscapes, mutational effects, and text guided property prediction. We critically analyze current bottlenecks, including data distribution biases, limited mechanistic interpretability, and the disconnect between geometric metrics and biophysical reality, while identifying future directions toward physically consistent generative models, multimodal foundation architectures, and experimental closed loop systems. This methodological transformation marks artificial intelligence's transition from a structural analysis tool into a universal simulator capable of understanding and ultimately rewriting the dynamic language of life.

</details>

---

### 15. [SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks](https://arxiv.org/abs/2603.18548)

**基本信息**

- 🔗 arXiv: [`2603.18548`](https://arxiv.org/abs/2603.18548)
- 👥 作者: Amanda A. Howard, Nicholas Zolman, Bruno Jacob 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18548.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合KAN和SINDy的新方法（SINDy-KANs），用于从数据中发现可解释的方程，特别是在动力系统等科学领域。这直接涉及构建可解释的、基于数据的模型来推断系统内在结构或动力学，这与“质谱结构推理”（从质谱数据推断分子结构）以及“化学大模型”（追求模型的可解释性和物理合理性）的核心目标在方法论和精神上高度一致。

**📖 中文摘要**

这篇论文提出了SINDy-KANs，该方法将Kolmogorov-Arnold网络（KANs）与非线性动力学稀疏识别（SINDy）相结合，以提高机器学习模型的解释性。SINDy-KANs同时训练一个KAN和一个类似SINDy的表征，在KAN的每个激活函数级别应用SINDy来增加KAN表征的可解释性，同时保持深度KAN可能实现的功能组合。该方法应用于一系列符号回归任务，包括动力系统，以展示在不同系统中准确的方程发现能力。KANs作为一种新兴的、可能更具解释性的神经网络架构，与SINDy这种旨在从数据中发现稀疏、可解释方程的经典方法相结合，为构建可解释的科学机器学习模型提供了新思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method to a number of symbolic regression tasks, including dynamical systems, to show accurate equation discovery across a range of systems.

</details>

---

### 16. [MedForge: Interpretable Medical Deepfake Detection via Forgery-aware Reasoning](https://arxiv.org/abs/2603.18577)

**基本信息**

- 🔗 arXiv: [`2603.18577`](https://arxiv.org/abs/2603.18577)
- 👥 作者: Zhihui Chen, Kai He, Qingyuan Lei 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18577.pdf)

**💡 相关性分析**

满足标准2：论文构建了一个大规模、带专家注释的医学图像篡改基准数据集MedForge-90K。这种构建高质量、领域特定、带详细注释（如病变编辑位置和推理依据）数据集的工作，与化学信息学和质谱分析领域为训练和评估化学大模型或质谱结构推理模型而构建标注数据集（例如，带有标准质谱和对应分子结构的数据集）的努力直接相关。

**📖 中文摘要**

这篇论文提出了MedForge，一个用于医学图像深度伪造检测的数据和方法解决方案。论文引入了MedForge-90K，一个大规模基准数据集，包含跨越19种病理的真实病变编辑，并通过医生检查指南和黄金编辑位置提供专家指导的推理监督。基于此，MedForge-Reasoner执行“定位-分析”推理，在产生判断前预测可疑区域，并进一步与Forgery-aware GSPO对齐，以加强证据基础并减少幻觉。实验证明了最先进的检测准确性和可信的、与专家一致的解释。这项工作专注于医学图像篡改的检测和解释，其核心是构建高质量、带专家注释的数据集（MedForge-90K）并开发可解释的、基于推理的检测模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Text-guided image editors can now manipulate authentic medical scans with high fidelity, enabling lesion implantation/removal that threatens clinical trust and safety. Existing defenses are inadequate for healthcare. Medical detectors are largely black-box, while MLLM-based explainers are typically post-hoc, lack medical expertise, and may hallucinate evidence on ambiguous cases. We present MedForge, a data-and-method solution for pre-hoc, evidence-grounded medical forgery detection. We introduce MedForge-90K, a large-scale benchmark of realistic lesion edits across 19 pathologies with expert-guided reasoning supervision via doctor inspection guidelines and gold edit locations. Building on it, MedForge-Reasoner performs localize-then-analyze reasoning, predicting suspicious regions before producing a verdict, and is further aligned with Forgery-aware GSPO to strengthen grounding and reduce hallucinations. Experiments demonstrate state-of-the-art detection accuracy and trustworthy, expert-aligned explanations.

</details>

---

### 17. [Elastic Weight Consolidation Done Right for Continual Learning](https://arxiv.org/abs/2603.18596)

**基本信息**

- 🔗 arXiv: [`2603.18596`](https://arxiv.org/abs/2603.18596)
- 👥 作者: Xuan Liu, Xiaobin Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18596.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进基于梯度的模型参数重要性估计方法（如EWC），这对于训练和优化能够持续学习、适应新任务的“化学大模型”具有直接的方法论参考价值。模型参数的重要性评估和正则化是构建稳健大模型的关键技术之一。

**📖 中文摘要**

本文对持续学习中的权重正则化方法进行了系统性分析，重点关注了基于梯度的权重重要性估计。论文的核心是分析Elastic Weight Consolidation (EWC)及其变体在估计权重重要性时存在的根本性错位问题，并提出了Logits Reversal (LR)操作来修正EWC的重要性估计。虽然论文主要关注通用机器学习模型的持续学习，但其核心方法——通过分析模型梯度（Fisher信息矩阵）来理解和修正模型参数的重要性——与构建和优化“化学大模型”时面临的挑战（如灾难性遗忘、多任务学习下的参数重要性评估）在方法论上高度相关。论文提出的修正方法为训练能够持续学习新知识而不遗忘旧知识的大模型提供了技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight regularization methods in continual learning (CL) alleviate catastrophic forgetting by assessing and penalizing changes to important model weights. Elastic Weight Consolidation (EWC) is a foundational and widely used approach within this framework that estimates weight importance based on gradients. However, it has consistently shown suboptimal performance. In this paper, we conduct a systematic analysis of importance estimation in EWC from a gradient-based perspective. For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios. Our analysis also reveals that Memory Aware Synapses (MAS), a variant of EWC, imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection. Consequently, both EWC and its variants exhibit fundamental misalignments in estimating weight importance, leading to inferior performance. To tackle these issues, we propose the Logits Reversal (LR) operation, a simple yet effective modification that rectifies EWC's importance estimation. Specifically, reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection. Extensive experiments across various CL tasks and datasets show that the proposed method significantly outperforms existing EWC and its variants. Therefore, we refer to it as EWC Done Right (EWC-DR).

</details>

---

### 18. [A Complexity Hierarchy of Shuffles in Card-Based Protocols](https://arxiv.org/abs/2603.18608)

**基本信息**

- 🔗 arXiv: [`2603.18608`](https://arxiv.org/abs/2603.18608)
- 👥 作者: Tomoki Ono, Suthee Ruangwises
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18608.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究“无监督音素发现”与“质谱结构推理”在问题范式上高度相关，都是致力于从复杂数据中无监督地推断出底层的基本结构单元。其方法论（基于离散单元的映射和评估）对质谱数据的结构解析有直接的启发意义。

**📖 中文摘要**

本文提出了一个用于评估无监督音素发现的跨语言基准DiscoPhon。该基准涵盖6种开发语言和6种测试语言，旨在评估系统仅从离散语音单元中无监督发现音素的能力。论文提供了基于多语言HuBERT和SpidR的预训练基线，并展示了当前模型中存在足够的音素信息。虽然研究领域是语音处理，但其核心是“从数据中无监督发现结构化的、有意义的单元（音素）”。这与“质谱结构推理”的核心任务——从质谱数据中推断出潜在的化学结构单元——在问题范式上高度相似。两者都是从复杂的、高维的观测数据（语音信号/质谱图）中，无监督或弱监督地发现底层的基本构成单元（音素/化学子结构）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Card-based cryptography uses physical playing cards to construct protocols for secure multi-party computation. Existing card-based protocols employ various types of shuffles, some of which are easy to implement in practice while others are considerably more complex. In this paper, we classify shuffle operations into several levels according to their implementation complexity. We motivate this hierarchy from both practical and theoretical perspectives, and prove separation results between several levels by showing that certain shuffles cannot be realized using only operations from lower levels. Finally, we propose a new complexity measure for evaluating card-based protocols based on this hierarchy.

</details>

---

### 19. [GEAR: Geography-knowledge Enhanced Analog Recognition Framework in Extreme Environments](https://arxiv.org/abs/2603.18626)

**基本信息**

- 🔗 arXiv: [`2603.18626`](https://arxiv.org/abs/2603.18626)
- 👥 作者: Zelin Liu, Bocheng Li, Yuling Zhou 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18626.pdf)

**💡 相关性分析**

满足标准1：论文提出的MSG-Net（图神经网络）是处理结构化数据（如分子图）的核心模型架构之一，直接适用于化学信息学中的分子表示学习和性质预测。其整个框架展示了如何利用图网络从复杂数据中学习特征并进行推理，这与化学大模型和质谱结构推理的技术栈高度相关。

**📖 中文摘要**

本文提出了GEAR框架，用于从青藏高原大规模地形数据中高效检索与马里亚纳海沟结构同源的陆地类似物。该框架的核心创新之一是设计了一个基于地貌学指标的Morphology-integrated Siamese Graph Network (MSG-Net)。论文利用MSG-Net提取的特征，发现了与生物数据的显著相关性，为未来的生物分析提供了证据。这项研究涉及从复杂的高维空间数据（地形）中学习有意义的表示并进行相似性匹配。虽然应用领域是地理学和生物学，但其核心技术——图神经网络（MSG-Net）用于学习复杂结构的嵌入表示并进行相似性推理——与“化学大模型”和“质谱结构推理”中利用图神经网络处理分子图、进行性质预测或结构匹配的核心技术路线完全一致。论文为处理类似的结构化数据（如图数据）提供了具体的模型架构和评估案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Mariana Trench and the Qinghai-Tibet Plateau exhibit significant similarities in geological origins and microbial metabolic functions. Given that deep-sea biological sampling faces prohibitive costs, recognizing structurally homologous terrestrial analogs of the Mariana Trench on the Qinghai-Tibet Plateau is of great significance. Yet, no existing model adequately addresses cross-domain topographic similarity retrieval, either neglecting geographical knowledge or sacrificing computational efficiency. To address these challenges, we present \underline{\textbf{G}}eography-knowledge \underline{\textbf{E}}nhanced \underline{\textbf{A}}nalog \underline{\textbf{R}}ecognition (\textbf{GEAR}) Framework, a three-stage pipeline designed to efficiently retrieve analogs from 2.5 million square kilometers of the Qinghai-Tibet Plateau: (1) Skeleton guided Screening and Clipping: Recognition of candidate valleys and initial screening based on size and linear morphological criteria. (2) Physics aware Filtering: The Topographic Waveform Comparator (TWC) and Morphological Texture Module (MTM) evaluate the waveform and texture and filter out inconsistent candidate valleys. (3) Graph based Fine Recognition: We design a \underline{\textbf{M}}orphology-integrated \underline{\textbf{S}}iamese \underline{\textbf{G}}raph \underline{\textbf{N}}etwork (\textbf{MSG-Net}) based on geomorphological metrics. Correspondingly, we release an expert-annotated topographic similarity dataset targeting tectonic collision zones. Experiments demonstrate the effectiveness of every stage. Besides, MSG-Net achieved an F1-Score 1.38 percentage points higher than the SOTA baseline. Using features extracted by MSG-Net, we discovered a significant correlation with biological data, providing evidence for future biological analysis.

</details>

---

### 20. [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660)

**基本信息**

- 🔗 arXiv: [`2603.18660`](https://arxiv.org/abs/2603.18660)
- 👥 作者: Peihang Wu, Zehong Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18660.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对多模态计算病理学的综述，其中包含了对自监督表示学习、令牌压缩、多智能体推理等重要技术的深入讨论。这些技术直接适用于处理化学和质谱领域的高维复杂数据，属于对相关主题的重要技术讨论和展望。

**📖 中文摘要**

本文是一篇关于多模态计算病理学的综述，系统性地分析了该领域的四个研究方向。其中，第一个方向明确提到了“全切片图像的自监督表示学习和结构感知的令牌压缩”。论文讨论了如何对极高分辨率的医学图像进行令牌压缩以实现跨尺度建模，以及多智能体协作推理机制如何模拟病理学家的思维链。这些技术——针对高维、复杂数据的自监督表示学习、令牌压缩（降维/特征提取）以及多智能体推理——正是构建“化学大模型”和处理“质谱结构推理”等复杂科学数据所需的核心技术。综述中总结的进展和挑战为相关领域的研究提供了重要的技术参考和前瞻性讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Whole slide imaging (WSI) has transformed digital pathology by enabling computational analysis of gigapixel histopathology images. Recent foundation model advances have accelerated progress in computational pathology, facilitating joint reasoning across pathology images, clinical reports, and structured data. Despite this progress, challenges remain: the extreme resolution of WSIs creates computational hurdles for visual learning; limited expert annotations constrain supervised approaches; integrating multimodal information while preserving biological interpretability remains difficult; and the opacity of modeling ultra-long visual sequences hinders clinical transparency. This review comprehensively surveys recent advances in multimodal computational pathology. We systematically analyze four research directions: (1) self-supervised representation learning and structure-aware token compression for WSIs; (2) multimodal data generation and augmentation; (3) parameter-efficient adaptation and reasoning-enhanced few-shot learning; and (4) multi-agent collaborative reasoning for trustworthy diagnosis. We specifically examine how token compression enables cross-scale modeling and how multi-agent mechanisms simulate a pathologist's "Chain of Thought" across magnifications to achieve uncertainty-aware evidence fusion. Finally, we discuss open challenges and argue that future progress depends on unified multimodal frameworks integrating high-resolution visual data with clinical and biomedical knowledge to support interpretable and safe AI-assisted diagnosis.

</details>

---

### 21. [STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation](https://arxiv.org/abs/2603.18688)

**基本信息**

- 🔗 arXiv: [`2603.18688`](https://arxiv.org/abs/2603.18688)
- 👥 作者: Chen Zhang, Liwei Liu, Jun Tao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18688.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是构建一个适用于科学时间序列的统一编码器预训练框架（STEP）。这直接与为化学/质谱数据构建专用基础模型（化学大模型）相关。同时，其方法论（跨领域蒸馏）和框架本身可作为处理科学数据（包括质谱数据）的工具和资源。

**📖 中文摘要**

本文提出了STEP框架，一个通过跨领域蒸馏进行科学时间序列编码器预训练的框架。科学时间序列（如质谱信号、光谱信号）与论文关注的数据类型高度相似：稀疏、异构、规模有限。STEP框架系统地评估了来自相关领域（音频、通用时间序列、脑信号）的基础模型的可迁移性和互补性，并提出通过跨领域蒸馏将多个基础模型的知识整合到一个统一的编码器中。该方法旨在学习适用于科学信号的通用、可迁移的特征。这直接为“化学大模型”的构建和“质谱结构推理”提供了宝贵的技术路线：即如何利用现有相关领域的预训练模型（或知识），通过蒸馏等技术，快速构建适用于特定科学领域（化学、质谱）的专用编码器或基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientific tasks and their complementary strengths. Based on this observation, we propose STEP, a Scientific Time Series Encoder Pretraining framework via cross domain distillation. STEP introduces adaptive patching to handle extreme-length sequences and a statistics compensation scheme to accommodate diverse numerical scales. It further leverages cross-domain distillation to integrate knowledge from multiple foundation models into a unified encoder. By combining complementary representations across different domains, STEP learns general-purpose and transferable features tailored for scientific signals. Experiments on seven scientific time series tasks demonstrate that STEP provides both an effective structure and an effective pretraining paradigm, taking a STEP toward scientific time series representation learning.

</details>

---

### 22. [Green Architectural Tactics in ML-enabled Systems: An LLM-based Repository Mining Study](https://arxiv.org/abs/2603.18734)

**基本信息**

- 🔗 arXiv: [`2603.18734`](https://arxiv.org/abs/2603.18734)
- 👥 作者: Vincenzo De Martino, Silverio Martínez-Fernández, Fabio Palomba
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18734.pdf)

**💡 相关性分析**

满足标准1：论文的核心是应用大语言模型（LLM）进行软件工程知识的自动化挖掘和分析。这种方法论本身代表了“大模型”在科学和工程数据分析中的一个重要应用方向，与利用AI大模型推动化学信息学研究的技术路线相关。

**📖 中文摘要**

本文进行了一项基于LLM的软件仓库挖掘研究，旨在调查机器学习赋能系统中绿色架构战术的采用情况，并识别新的可持续实践。论文设计了一种基于大语言模型的新机制，能够从代码仓库中识别已知和新的可持续实践。研究涉及对205个开源ML项目的分析。虽然论文聚焦于AI系统的环境可持续性，但其核心方法——使用大语言模型（LLM）自动化地分析和挖掘软件项目中的模式、实践和知识——与利用AI（特别是大模型）加速科学研究（包括化学信息学）的范式高度相关。论文展示了LLM作为智能分析工具在处理大规模代码/文本数据方面的潜力，这种方法可以迁移到分析化学文献、代码或数据集，以发现新的模式或最佳实践。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Context: The increasing adoption of machine learning (ML) and artificial intelligence (AI) technologies raises growing concerns about their environmental sustainability. Developing and deploying ML-enabled systems is computationally intensive, particularly during training and inference. Green AI has emerged to address these issues by promoting efficiency without sacrificing accuracy. While prior research has proposed catalogs of sustainable practices (i.e., green tactics), there remains limited understanding of their adoption in practice and whether additional, undocumented tactics exist. Objective: This study aims to investigate the extent to which existing sustainable practices are implemented in real-world ML-enabled systems and to identify previously undocumented practices that support environmental sustainability. Method: We conduct a mining software repository study on 205 open-source ML projects on GitHub. To support our analysis, we design a novel mechanism based on large language models (LLMs) capable of identifying both known and new sustainable practices from code repositories. Results: Our findings confirm that green tactics reported in the literature are used in practice, although adoption rates vary. Furthermore, our LLM-based approach reveals nine previously undocumented sustainable practices. Each tactic is supported with code examples to aid adoption and integration. Conclusions: We finally provide insights for practitioners seeking to reduce the environmental impact of ML-enabled systems and offer a foundation for future research in automating the detection and adoption of sustainable practices.

</details>

---

### 23. [WeNLEX: Weakly Supervised Natural Language Explanations for Multilabel Chest X-ray Classification](https://arxiv.org/abs/2603.18752)

**基本信息**

- 🔗 arXiv: [`2603.18752`](https://arxiv.org/abs/2603.18752)
- 👥 作者: Isabel Rio-Torto, Jaime S. Cardoso, Luís F. Teixeira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18752.pdf)

**💡 相关性分析**

满足标准1：论文研究如何为黑盒模型生成忠实且合理的自然语言解释，其方法（基于特征空间对齐和分布约束的生成）对于构建可解释的“化学大模型”或为“质谱结构推理”结果提供解释具有直接的方法论参考价值。

**📖 中文摘要**

本文提出了WeNLEX，一个用于多标签胸部X光分类的弱监督自然语言解释生成模型。该模型的核心创新在于通过匹配从自然语言解释生成的图像与原始图像（在黑盒模型的特征空间中）来确保解释的忠实性，并通过与少量临床医生标注的解释数据库进行分布对齐来保持解释的合理性。虽然应用领域是医学影像，但其核心技术——使用生成模型（如图像生成）和特征空间对齐来约束和评估文本解释的生成——与“化学大模型”中可解释性研究和“质谱结构推理”中生成结构解释的任务在方法论上相通。论文为解决“如何让AI模型产生既合理又忠实的解释”这一通用挑战提供了具体方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Natural language explanations provide an inherently human-understandable way to explain black-box models, closely reflecting how radiologists convey their diagnoses in textual reports. Most works explicitly supervise the explanation generation process using datasets annotated with explanations. Thus, though plausible, the generated explanations are not faithful to the model's reasoning. In this work, we propose WeNLEX, a weakly supervised model for the generation of natural language explanations for multilabel chest X-ray classification. Faithfulness is ensured by matching images generated from their corresponding natural language explanations with original images, in the black-box model's feature space. Plausibility is maintained via distribution alignment with a small database of clinician-annotated explanations. We empirically demonstrate, through extensive validation on multiple metrics to assess faithfulness, simulatability, diversity, and plausibility, that WeNLEX is able to produce faithful and plausible explanations, using as little as 5 ground-truth explanations per diagnosis. Furthermore, WeNLEX can operate in both post-hoc and in-model settings. In the latter, i.e., when the multilabel classifier is trained together with the rest of the network, WeNLEX improves the classification AUC of the standalone classifier by 2.21%, thus showing that adding interpretability to the training process can actually increase the downstream task performance. Additionally, simply by changing the database, WeNLEX explanations are adaptable to any target audience, and we showcase this flexibility by training a layman version of WeNLEX, where explanations are simplified for non-medical users.

</details>

---

### 24. [DA-Mamba: Learning Domain-Aware State Space Model for Global-Local Alignment in Domain Adaptive Object Detection](https://arxiv.org/abs/2603.18757)

**基本信息**

- 🔗 arXiv: [`2603.18757`](https://arxiv.org/abs/2603.18757)
- 👥 作者: Haochen Li, Rui Zhang, Hantao Yao 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18757.pdf)

**💡 相关性分析**

满足标准1：论文的核心是探索并应用一种新型的基础模型架构——状态空间模型于视觉任务。这直接与“化学大模型”的基础架构创新研究相关，为处理化学序列数据（如SMILES、质谱峰序列）提供了新的模型选择和技术思路。

**📖 中文摘要**

本文提出了DA-Mamba，一种用于领域自适应目标检测的混合CNN-状态空间模型架构。该模型结合了CNN的效率和状态空间模型的线性时间长程建模能力，以捕获全局和局部的域不变特征。论文引入了图像感知SSM和对象感知SSM两个新颖模块。状态空间模型是近年来在序列建模中备受关注的一种高效架构，与Transformer形成竞争。将SSM引入视觉任务并进行改进，代表了基础模型架构前沿探索的一个方向。虽然应用是目标检测，但其核心——探索并整合新型高效的基础模型架构（SSM）以更好地处理视觉数据——与探索和构建下一代“化学大模型”的基础架构这一主题直接相关。论文为在科学数据（如分子序列、质谱序列）上应用SSM类模型提供了参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Domain Adaptive Object Detection (DAOD) aims to transfer detectors from a labeled source domain to an unlabeled target domain. Existing DAOD methods employ multi-granularity feature alignment to learn domain-invariant representations. However, the local connectivity of their CNN-based backbone and detection head restricts alignment to local regions, failing to extract global domain-invariant features. Although transformer-based DAOD methods capture global dependencies via attention mechanisms, their quadratic computational cost hinders practical deployment. To solve this, we propose DA-Mamba, a hybrid CNN-State Space Models (SSMs) architecture that combines the efficiency of CNNs with the linear-time long-range modeling capability of State Space Models (SSMs) to capture both global and local domain-invariant features. Specifically, we introduce two novel modules: Image-Aware SSM (IA-SSM) and Object-Aware SSM (OA-SSM). IA-SSM is integrated into the backbone to enhance global domain awareness, enabling image-level global and local alignment. OA-SSM is inserted into the detection head to model spatial and semantic dependencies among objects, enhancing instance-level alignment. Comprehensive experiments demonstrate that the proposed method can efficiently improve the cross-domain performance of the object detector.

</details>

---

### 25. [Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN](https://arxiv.org/abs/2603.18766)

**基本信息**

- 🔗 arXiv: [`2603.18766`](https://arxiv.org/abs/2603.18766)
- 👥 作者: Marcio Augusto Sampaio, Paulo Henrique Ranazzi, Martin Julian Blunt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18766.pdf)

**💡 相关性分析**

满足标准1：论文的核心是应用深度生成模型进行复杂科学数据的参数化和生成。VAE-GAN是化学信息学中用于分子生成和表示学习的核心模型之一。该研究为这类模型在解决实际科学问题（如数据同化、参数反演）中的应用提供了方法论参考。

**📖 中文摘要**

本文提出将变分自编码器生成对抗网络集成到集合平滑器多重数据同化方法中，用于石油储层模拟中的历史匹配和参数化。该工作的创新点在于结合了VAE和GAN的优势，以实现高质量的地质描述和良好的生产曲线历史匹配。虽然应用领域是地质建模，但其核心技术——使用深度生成模型进行高维、非高斯参数的表示学习和域转换——与“化学大模型”中学习分子结构的潜在表示，以及“质谱结构推理”中生成与质谱匹配的候选分子结构等任务高度相关。VAE-GAN是生成化学领域分子结构的一种重要模型架构，论文为其在复杂科学数据上的应用和与传统优化方法的结合提供了具体案例。

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

满足标准1：论文的核心研究内容围绕扩散大语言模型（dLLMs）的策略优化，这是“化学大模型”主题下生成模型（如用于分子生成的扩散模型）训练和优化的一个重要子领域。

**📖 中文摘要**

本文提出了dTRPO（轨迹缩减策略优化）方法，旨在改进扩散大语言模型（dLLMs）的策略优化。论文的核心是解决dLLMs与人类偏好对齐的挑战，通过减少轨迹概率计算成本，实现可扩展的离线策略训练。作者证明了在参考策略正则化下，新解掩码词元的概率比是中间扩散状态概率比的无偏估计，并且完整轨迹的概率可以通过对重新掩码的最终状态进行单次前向传递来有效估计。该方法在指令跟随和推理基准测试中显著提升了dLLMs的核心性能。虽然论文主要关注语言模型，但其核心方法——针对扩散生成模型的策略优化——与“化学大模型”主题中关于生成模型（如用于分子生成的扩散模型）的训练和优化高度相关。

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

满足标准1：论文的核心研究内容是关于生成模型（包括扩散模型）的改进和理论分析，这与“化学大模型”主题下关于分子生成等生成模型的研究直接相关。

**📖 中文摘要**

本文研究了一种利用判别器来训练或微调生成模型的通用框架。作者扩展了与f-散度相关的强对偶性结果，提出了一种判别器引导的“精炼”方法，可以改进任何生成模型。理论分析表明，精炼后的生成模型相比未精炼的版本，能够提供可证明的泛化性改进。论文特别指出，他们的方法包含了一种已显示出巨大经验成功的基于分数的扩散方法（Kim等人，2022），并通过分析揭示了该方法的泛化保证。这项工作为理解生成模型的泛化性做出了贡献。虽然论文是通用性的，但其核心是关于生成模型（包括扩散模型）的改进和理论分析，这与“化学大模型”主题中关于分子生成等生成模型的研究直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The use of discriminators to train or fine-tune generative models has proven to be a rather successful framework. A notable example is Generative Adversarial Networks (GANs) that minimize a loss incurred by training discriminators along with other paradigms that boost generative models via discriminators that satisfy weak learner constraints. More recently, even diffusion models have shown advantages with some kind of discriminator guidance. In this work, we extend a strong-duality result related to $f$-divergences which gives rise to a discriminator-guided recipe that allows us to \textit{refine} any generative model. We then show that the refined generative models provably improve generalization, compared to its non-refined counterpart. In particular, our analysis reveals that the gap in generalization is improved based on the Rademacher complexity of the discriminator set used for refinement. Our recipe subsumes a recently introduced score-based diffusion approach (Kim et al., 2022) that has shown great empirical success, however allows us to shed light on the generalization guarantees of this method by virtue of our analysis. Thus, our work provides a theoretical validation for existing work, suggests avenues for new algorithms, and contributes to our understanding of generalization in generative models at large.

</details>

---

### 28. [Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827)

**基本信息**

- 🔗 arXiv: [`2603.18827`](https://arxiv.org/abs/2603.18827)
- 👥 作者: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18827.pdf)

**💡 相关性分析**

满足标准3：论文是一项关于AI伦理和社会影响的调查性研究，包含了对AI在多个领域（如医学）应用前景和影响的讨论，这为思考“化学大模型”等AI技术在科学领域的应用和社会接受度提供了相关的背景和展望视角。

**📖 中文摘要**

本文从性别视角调查了学生对人工智能伦理和社会影响的看法。研究通过对230名计算机科学专业二年级学生进行问卷调查，探讨了人工智能在医学、教育、媒体等领域的影响，以及学生感知到的潜在威胁和伦理考量。虽然论文主题是AI伦理教育，但其调查对象是计算机科学学生，调查内容涵盖了AI对社会各领域（包括医学）的影响。这间接涉及到AI（可能包括化学信息学或分析领域的AI模型）的应用和社会接受度，但与“化学大模型”或“质谱结构推理”的核心技术关联较弱。考虑到“综述展望相关”标准的包容性（包含重要的相关讨论），本文对AI社会影响的广泛讨论可被视为与AI在科学领域（包括化学）应用前景相关的背景性讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An investigation, from a gender perspective, of how students view the ethical implications and societal effects of artificial intelligence is conducted, examining concepts that could have a big influence on how artificial intelligence may be taught in the future. For this, we conducted a survey on a cohort of 230 second year computer science students to reveal their opinions. The results revealed that AI, from the students' perspective, will significantly impact daily life, particularly in areas such as medicine, education, or media. Men are more aware of potential changes in Computer Science, autonomous driving, image and video processing, and chatbot usage, while women mention more the impact on social media. Both men and women perceive potential threats in the same manner, with men more aware of war, AI controlled drones, terrain recognition, and information war. Women seem to have a stronger tendency towards ethical considerations and helping others.

</details>

---

### 29. [Statistical Characteristic-Guided Denoising for Rapid High-Resolution Transmission Electron Microscopy Imaging](https://arxiv.org/abs/2603.18834)

**基本信息**

- 🔗 arXiv: [`2603.18834`](https://arxiv.org/abs/2603.18834)
- 👥 作者: Hesong Li, Ziqi Wu, Ruiwen Shao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18834.pdf)

**💡 相关性分析**

满足标准2：论文提出了针对HRTEM图像的去噪网络和特定数据集。虽然领域不同，但其开发的深度学习图像分析方法论和生成的数据资源，与“质谱结构推理”中处理复杂仪器信号、进行特征提取和结构推理的技术挑战具有可比性和参考价值。

**📖 中文摘要**

本文提出了一种统计特征引导的去噪网络，用于快速高分辨率透射电子显微镜（HRTEM）成像。HRTEM能够原子级观察成核动力学，但快速成像导致严重噪声。该方法利用统计特征在空间域和频域引导去噪过程，并开发了HRTEM特定的噪声校准方法，生成了包含无序结构和真实HRTEM图像噪声的数据集。实验表明该方法在HRTEM图像去噪和下游定位任务中优于现有方法。虽然应用领域是材料科学的显微成像，但其核心是开发一种先进的、针对科学仪器（HRTEM）图像的去噪模型。这种基于深度学习的图像处理和分析方法与“质谱结构推理”主题有方法论上的相似性，后者也涉及从复杂的仪器信号（质谱图）中提取和推理结构信息。论文提供的数据集和去噪工具也可视为相关资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

High-Resolution Transmission Electron Microscopy (HRTEM) enables atomic-scale observation of nucleation dynamics, which boosts the studies of advanced solid materials. Nonetheless, due to the millisecond-scale rapid change of nucleation, it requires short-exposure rapid imaging, leading to severe noise that obscures atomic positions. In this work, we propose a statistical characteristic-guided denoising network, which utilizes statistical characteristics to guide the denoising process in both spatial and frequency domains. In the spatial domain, we present spatial deviation-guided weighting to select appropriate convolution operations for each spatial position based on deviation characteristic. In the frequency domain, we present frequency band-guided weighting to enhance signals and suppress noise based on band characteristics. We also develop an HRTEM-specific noise calibration method and generate a dataset with disordered structures and realistic HRTEM image noises. It can ensure the denoising performance of models on real images for nucleation observation. Experiments on synthetic and real data show our method outperforms the state-of-the-art methods in HRTEM image denoising, with effectiveness in the localization downstream task. Code will be available at this https URL .

</details>

---

### 30. [Pore-scale modeling of capillary-driven binder migration during battery electrode drying](https://arxiv.org/abs/2603.18860)

**基本信息**

- 🔗 arXiv: [`2603.18860`](https://arxiv.org/abs/2603.18860)
- 👥 作者: Marcel Weichel, Martin Reder, Gerit Mühlberg 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18860.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用孔隙尺度连续介质模型来模拟电池电极干燥这一化学材料制备过程。这种计算建模方法与“化学大模型”主题中利用先进模型解决化学和材料科学问题的研究方向直接相关。

**📖 中文摘要**

本文提出了一个孔隙尺度连续介质模型，用于模拟钠离子电池硬碳电极干燥过程中的毛细管驱动粘结剂迁移。电极干燥是制造中的关键步骤，因为孔隙排空期间的粘结剂迁移会影响电极的机械完整性和电性能。现有模型主要依赖一维薄膜收缩阶段或忽略毛细管传输，缺乏对粘结剂迁移的物理一致的微观结构解析预测。本研究扩展了空间解析的孔隙尺度模型，明确描述了孔隙排空过程中毛细管驱动的粘结剂传输。该模型应用于具有不同平均粒径的硬碳微观结构，模拟揭示了颗粒尺寸、蒸发速率和表面张力等因素对粘结剂分布的影响。这项工作为优化电极干燥过程提供了基础。论文属于电化学和材料制造领域，但其核心是应用计算建模（孔隙尺度连续介质模型）来模拟和优化化学材料（电池电极）的制备过程。这种基于物理的建模和仿真方法与“化学大模型”中利用计算模型解决化学材料问题的范式一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sodium-ion batteries employing hard carbon electrodes are considered a drop-in technology for lithium-ion batteries. Electrode drying is a critical manufacturing step, as binder migration during pore emptying impacts the mechanical integrity and electrical performance of the electrode. Existing modeling approaches predominantly rely on the film shrinkage phase in a one dimensional way or neglect the capillary transport, resulting in a lack of physically consistent microstructure resolved predictions of binder migration. In this work, a spatially resolved pore scale continuum model is extended to explicitly describe capillary driven binder transport during pore emptying. The model is applied to hard carbon microstructures with varying mean particle diameters. The simulations reveal that smaller particle sizes lead to a more homogeneous binder distribution, whereas higher evaporation rates and increased surface tension promote stronger binder gradients. Variations in solvent viscosity show only a minor influence on binder migration, as long as no hydrophilic or hydrophobic behavior is present. Finally, the simulations demonstrate that an explicit description of capillary transport and microstructural effects is essential for accurately predicting binder migration and provides a basis for the targeted optimization of electrode drying processes.

</details>

---

### 31. [RadioDiff-FS: Physics-Informed Manifold Alignment in Few-Shot Diffusion Models for High-Fidelity Radio Map Construction](https://arxiv.org/abs/2603.18865)

**基本信息**

- 🔗 arXiv: [`2603.18865`](https://arxiv.org/abs/2603.18865)
- 👥 作者: Xiucheng Wang, Zixuan Guo, Nan Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18865.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于科学数据（无线电地图）生成的少样本扩散模型框架。这种方法论与“化学大模型”主题中利用扩散模型等生成模型解决化学数据生成和预测问题直接相关。

**📖 中文摘要**

本文提出了RadioDiff-FS，一个用于高保真无线电地图构建的少样本扩散框架。无线电地图对于6G网络规划至关重要，但高保真构建具有挑战性。严格的电磁求解器计算延迟高，而数据驱动模型需要大量标注数据且从简化仿真到复杂多径环境的泛化能力差。RadioDiff-FS使预训练的主路径生成器能够仅用少量高保真样本适应多径丰富的目标域。该适应基于对多径无线电地图的理论分解，并引入了方向一致性损失来约束扩散分数更新沿物理上合理的传播方向。实验表明，该方法在有限监督下显著优于原始扩散基线。论文属于无线通信领域，但其核心是提出了一种针对特定科学数据（无线电地图）的、基于扩散模型的少样本生成和适应框架。这种方法论——使用生成模型（特别是扩散模型）来生成或补全科学数据——与“化学大模型”主题中利用生成模型（如用于分子生成或光谱预测的扩散模型）的思路高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Radio maps (RMs) provide spatially continuous propagation characterizations essential for 6G network planning, but high-fidelity RM construction remains challenging. Rigorous electromagnetic solvers incur prohibitive computational latency, while data-driven models demand massive labeled datasets and generalize poorly from simplified simulations to complex multipath environments. This paper proposes RadioDiff-FS, a few-shot diffusion framework that adapts a pre-trained main-path generator to multipath-rich target domains with only a small number of high-fidelity samples. The adaptation is grounded in a theoretical decomposition of the multipath RM into a dominant main-path component and a directionally sparse residual. This decomposition shows that the cross-domain shift corresponds to a bounded and geometrically structured feature translation rather than an arbitrary distribution change. A Direction-Consistency Loss (DCL) is then introduced to constrain diffusion score updates along physically plausible propagation directions, suppressing phase-inconsistent artifacts that arise in the low-data regime. Experiments show that RadioDiff-FS reduces NMSE by 59.5% on static RMs and by 74.0% on dynamic RMs relative to the vanilla diffusion baseline, achieving an SSIM of 0.9752 and a PSNR of 36.37 dB under severely limited supervision.

</details>

---

### 32. [Translating MRI to PET through Conditional Diffusion Models with Enhanced Pathology Awareness](https://arxiv.org/abs/2603.18896)

**基本信息**

- 🔗 arXiv: [`2603.18896`](https://arxiv.org/abs/2603.18896)
- 👥 作者: Yitong Li, Igor Yakushev, Dennis M. Hedderich 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18896.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于条件扩散模型的医学图像生成方法。这种利用先进生成模型（扩散模型）解决科学数据生成问题的范式，与“化学大模型”主题中利用生成模型处理化学数据的研究直接相关。

**📖 中文摘要**

本文提出了PASTA，一个基于条件扩散模型、具有增强病理感知能力的图像翻译框架，用于从磁共振图像生成合成的正电子发射断层扫描图像。PET对于诊断神经退行性疾病至关重要，但成本高且有辐射。MRI则没有这些限制，但诊断敏感性较低。现有方法大多强调结构保留而忽视了病理感知的关键需求。PASTA通过其高度交互的双臂架构和多模态条件集成，在保留结构和病理细节方面超越了现有方法。此外，还引入了新颖的循环交换一致性和体积生成策略，显著增强了生成高质量3D PET图像的能力。定性和定量结果表明，合成的PET扫描具有高质量和病理感知能力。论文属于医学影像分析领域，但其核心是开发一种先进的、基于条件扩散模型的跨模态医学图像生成方法。这种利用扩散模型生成科学/医学数据的方法，与“化学大模型”主题中利用生成模型（如用于分子结构生成或光谱预测）的技术路线高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Positron emission tomography (PET) is a widely recognized technique for diagnosing neurodegenerative diseases, offering critical functional insights. However, its high costs and radiation exposure hinder its widespread use. In contrast, magnetic resonance imaging (MRI) does not involve such limitations. While MRI also detects neurodegenerative changes, it is less sensitive for diagnosis compared to PET. To overcome such limitations, one approach is to generate synthetic PET from MRI. Recent advances in generative models have paved the way for cross-modality medical image translation; however, existing methods largely emphasize structural preservation while neglecting the critical need for pathology awareness. To address this gap, we propose PASTA, a novel image translation framework built on conditional diffusion models with enhanced pathology awareness. PASTA surpasses state-of-the-art methods by preserving both structural and pathological details through its highly interactive dual-arm architecture and multi-modal condition integration. Additionally, we introduce a novel cycle exchange consistency and volumetric generation strategy that significantly enhances PASTA's ability to produce high-quality 3D PET images. Our qualitative and quantitative results demonstrate the high quality and pathology awareness of the synthesized PET scans. For Alzheimer's diagnosis, the performance of these synthesized scans improves over MRI by 4%, almost reaching the performance of actual PET. Our code is available at this https URL .

</details>

---

### 33. [Neural Galerkin Normalizing Flow for Transition Probability Density Functions of Diffusion Models](https://arxiv.org/abs/2603.18907)

**基本信息**

- 🔗 arXiv: [`2603.18907`](https://arxiv.org/abs/2603.18907)
- 👥 作者: Riccardo Saporiti, Fabio Nobile
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18907.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种结合归一化流和神经伽辽金方法的科学机器学习框架，用于构建随机微分方程的代理模型。这种开发先进机器学习模型以解决科学计算问题的方法，与“化学大模型”主题中利用大模型和生成模型加速化学发现和模拟的研究直接相关。

**📖 中文摘要**

本文提出了一个新的神经伽辽金归一化流框架，用于通过求解相应的福克-普朗克方程来近似扩散过程的转移概率密度函数。该方法将解表示为参考随机过程转移概率密度函数的变换，确保近似是结构保持的，并自动满足正性和质量守恒约束。通过将神经伽辽金方案扩展到归一化流的背景中，推导出了归一流参数时间演化的常微分方程组。自适应采样例程用于在有意义的位置评估福克-普朗克残差。数值结果表明该策略捕捉了真实解的关键特征。所提出的方法作为一个有前景的代理模型，可用于与随机微分方程相关的许多查询问题，如贝叶斯推断、模拟和扩散桥生成。论文的核心是提出了一种结合归一化流和神经伽辽金方法的新框架，用于求解与随机过程相关的偏微分方程。这种方法论属于科学机器学习的前沿，旨在为复杂的科学计算问题提供高效的代理模型。这与“化学大模型”主题中利用先进机器学习模型（如生成模型、代理模型）加速化学计算和模拟的研究方向高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Neural Galerkin Normalizing Flow framework to approximate the transition probability density function of a diffusion process by solving the corresponding Fokker-Planck equation with an atomic initial distribution, parametrically with respect to the location of the initial mass. By using Normalizing Flows, we look for the solution as a transformation of the transition probability density function of a reference stochastic process, ensuring that our approximation is structure-preserving and automatically satisfies positivity and mass conservation constraints. By extending Neural Galerkin schemes to the context of Normalizing Flows, we derive a system of ODEs for the time evolution of the Normalizing Flow's parameters. Adaptive sampling routines are used to evaluate the Fokker-Planck residual in meaningful locations, which is of vital importance to address high-dimensional PDEs. Numerical results show that this strategy captures key features of the true solution and enforces the causal relationship between the initial datum and the density function at subsequent times. After completing an offline training phase, online evaluation becomes significantly more cost-effective than solving the PDE from scratch. The proposed method serves as a promising surrogate model, which could be deployed in many-query problems associated with stochastic differential equations, like Bayesian inference, simulation, and diffusion bridge generation.

</details>

---

### 34. [Theoretical Analyses of Detectors for Additive Noise Channels with Mean-Variance Uncertainty under Nonlinear Expectation Theory](https://arxiv.org/abs/2603.18937)

**基本信息**

- 🔗 arXiv: [`2603.18937`](https://arxiv.org/abs/2603.18937)
- 👥 作者: Wen-Xuan Lang, Guiying Yan, Zhi-Ming Ma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18937.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是在概率模型不确定条件下，利用非线性期望理论进行最优检测和推理。这种处理数据不确定性和进行鲁棒推理的理论框架，与“质谱结构推理”主题中从复杂、噪声数据中推断化学结构所涉及的核心方法论挑战相关。

**📖 中文摘要**

本文在非线性期望理论下，分析了加性噪声信道在均值-方差不确定性下的检测器。经典信息论中，加性噪声信道的最优检测器形式和性能可以精确推导，但基于噪声服从特定概率分布的假设。本文利用非线性期望理论，将检测器分析扩展到信道噪声概率模型不确定的情况。考虑了两种分布不确定性：一种无均值不确定性但有方差不确定性，另一种同时具有均值和方差不确定性。推导了两种场景下二元输入加性噪声信道在非线性期望最优准则下的最优检测器，并给出了其显式形式。研究发现均值不确定性显著影响最优检测器的形式，而方差不确定性则不影响。此外，还提出了一种信道噪声不确定参数的估计方法。最后，给出了新推导的最优检测器的理论分析和仿真性能结果。论文属于信息论和信号处理领域，但其核心是在模型不确定性下（使用非线性期望理论）进行最优推理和决策的理论框架。这种处理不确定性和进行鲁棒推理的数学框架，与“质谱结构推理”中从噪声、不确定的质谱数据中推断分子结构所面临的挑战在方法论层面有相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In classical information theory, both the form and performance of the optimal detector for additive noise channels can be precisely derived, based on the assumption that the channel noise follows a specific probability distribution or a mixture of known distributions, or that the exact distribution exists but is unknown. In this paper, we extend the analyses of detectors for additive noise channel to the situation where the probability model for analyzing channels is uncertain, utilizing nonlinear expectation theory. We consider two types of distribution uncertainties: one with no mean uncertainty but with variance uncertainty, and another with both mean and variance uncertainties. We derive the optimal detectors for binary input additive noise channel under the nonlinear expectation optimal criterion for both scenarios and provide their explicit forms. Our findings reveal that mean uncertainty significantly influences the form of the optimal detector, whereas variance uncertainty does not. Additionally, we propose an estimation method for the uncertain parameters of the channel noise. Finally, we present theoretical analyses and simulated performance results of the newly derived optimal detectors, and compare these results with the performance of optimal detector under classical information theory, which assumes a deterministic probability model. The results of experiments show that our new detection methods outperform conventional methods in most scenarios with uncertain probability models, showing the practical relevance of our theoretical contributions.

</details>

---

### 35. [BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery](https://arxiv.org/abs/2603.18957)

**基本信息**

- 🔗 arXiv: [`2603.18957`](https://arxiv.org/abs/2603.18957)
- 👥 作者: Sijian Fan, Liyan Xiong, Dayuan Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18957.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的贝叶斯机器学习模型（BVSIMC），用于药物发现中的预测任务（如耐药性预测、药物-疾病关联预测），这直接属于“化学信息学”和“化学大模型”的研究领域。

**📖 中文摘要**

本文提出了BVSIMC（贝叶斯变量选择引导的归纳矩阵补全），一种新的贝叶斯模型，用于在药物发现中实现从侧信息（如药物的化学性质和疾病的基因组信息）中进行变量选择。通过学习稀疏的潜在嵌入，BVSIMC提高了预测准确性和可解释性。该方法通过模拟研究和两个药物发现应用进行了验证：1) 预测结核分枝杆菌的耐药性，2) 预测计算药物重定位中的新药-疾病关联。在合成和真实数据上，BVSIMC在预测方面优于其他几种最先进的方法。在两个真实例子中，BVSIMC进一步揭示了最具临床意义的侧特征。论文属于计算药物发现和化学信息学领域，其核心是开发一种新的机器学习模型（BVSIMC），该模型整合了侧信息并进行变量选择，以改进药物-靶点相互作用或药物性质的预测。这直接属于“化学大模型”和“化学信息学”的研究范畴，即利用机器学习模型解决化学和药物发现中的预测问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in drug discovery have demonstrated that incorporating side information (e.g., chemical properties about drugs and genomic information about diseases) often greatly improves prediction performance. However, these side features can vary widely in relevance and are often noisy and high-dimensional. We propose Bayesian Variable Selection-Guided Inductive Matrix Completion (BVSIMC), a new Bayesian model that enables variable selection from side features in drug discovery. By learning sparse latent embeddings, BVSIMC improves both predictive accuracy and interpretability. We validate our method through simulation studies and two drug discovery applications: 1) prediction of drug resistance in Mycobacterium tuberculosis, and 2) prediction of new drug-disease associations in computational drug repositioning. On both synthetic and real data, BVSIMC outperforms several other state-of-the-art methods in terms of prediction. In our two real examples, BVSIMC further reveals the most clinically meaningful side features.

</details>

---

### 36. [Foundations of Schrödinger Bridges for Generative Modeling](https://arxiv.org/abs/2603.18992)

**基本信息**

- 🔗 arXiv: [`2603.18992`](https://arxiv.org/abs/2603.18992)
- 👥 作者: Sophia Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18992.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于薛定谔桥数学基础的教程性/综述性文章，薛定谔桥是扩散模型等生成模型的理论核心。这为“化学大模型”主题中利用扩散模型进行分子生成等研究提供了重要的理论背景和展望。

**📖 中文摘要**

本文系统阐述了生成建模中薛定谔桥问题的数学基础。薛定谔桥在现代生成建模框架（包括扩散模型、基于分数的模型和流匹配）中处于核心地位，它将问题框架化为在边际分布约束下确定一个最优的随机桥，该桥与预定义的参考过程具有最小熵偏差。本指南利用最优传输、随机控制和路径空间优化等工具，发展了薛定谔桥问题的数学基础，并重点介绍了其与现代生成建模直接相关的动态表述。文章为从第一性原理构建薛定谔桥提供了一个全面的工具包，并展示了这些构建如何产生通用和特定于任务的计算方法。论文是一篇关于薛定谔桥及其在生成模型中应用的教程或基础性论述。薛定谔桥是理解扩散模型等生成模型的理论基础，而扩散模型在“化学大模型”主题中常被用于分子生成等任务。因此，这篇论文提供了与“化学大模型”紧密相关的生成模型的理论背景和基础。

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

满足标准2：论文提出的SHAPCA框架专门用于处理和分析光谱数据（如质谱/红外光谱等），这是一种在化学信息学和质谱分析中至关重要的数据类型。该框架旨在为这类高维、共线性的数据提供稳定和可解释的机器学习模型分析工具，因此与主题‘质谱结构推理’高度相关，因为它提供了可用于该主题数据分析的方法和工具。

**📖 中文摘要**

本文提出了一种名为SHAPCA的可解释机器学习流程，用于解决光谱数据（一种化学分析中常见的质谱/光谱数据）的高维性和共线性问题。该流程结合了主成分分析（PCA）进行降维和SHAP（Shapley Additive exPlanations）进行事后解释，能够在原始输入空间（即光谱波段）提供模型预测的解释。这使得化学或生物医学领域的研究人员和从业者能够将模型的决策与原始光谱信号中的生物或化学组分联系起来，从而理解和信任模型的推理过程。该研究强调了在化学信息学领域，为基于光谱数据的机器学习模型提供稳定、一致且可解释的结果的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

</details>

---

### 38. [MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185)

**基本信息**

- 🔗 arXiv: [`2603.19185`](https://arxiv.org/abs/2603.19185)
- 👥 作者: Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19185.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容围绕评估扩散模型（一种生成模型）生成的合成数据的隐私性。这与‘化学大模型’主题直接相关，因为化学领域的大模型（如分子生成模型）也属于生成模型范畴，面临类似的隐私和安全性评估需求。同时，论文提出的挑战赛和评估方法为相关领域提供了评估数据生成工具隐私风险的基准和资源。

**📖 中文摘要**

本文介绍了MIDST挑战赛，其核心目标是评估基于扩散模型生成的合成表格数据在隐私保护方面的有效性，特别是抵抗成员推理攻击（MIA）的能力。虽然论文主要关注表格数据，但其方法论和评估框架直接针对生成模型（扩散模型）的隐私风险。在化学信息学和质谱分析领域，生成模型（如化学大模型）正被用于生成分子结构或质谱数据，因此评估这些生成模型的隐私泄露风险至关重要。该挑战赛催生了针对扩散模型的新型黑盒和白盒成员推理攻击，为全面评估生成模型的隐私效能提供了基准和方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at this https URL

</details>

---

### 39. [Generative Replica-Exchange: A Flow-based Framework for Accelerating Replica Exchange Simulations](https://arxiv.org/abs/2603.18076)

**基本信息**

- 🔗 arXiv: [`2603.18076`](https://arxiv.org/abs/2603.18076)
- 👥 作者: Shengjie Huang, Sijie Yang, Jianqiao Yi 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18076.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用深度生成模型（归一化流）来加速分子模拟中的副本交换采样，这直接属于化学信息学中利用‘化学大模型’（此处指用于分子系统的生成模型）解决计算化学问题的范畴。

**📖 中文摘要**

本文提出了一种生成式副本交换（GREX）方法，将深度生成模型（特别是归一化流）集成到副本交换（REX）模拟框架中。该方法旨在消除传统REX中对大量中间温度副本的需求，从而加速分子模拟。GREX利用训练好的归一化流按需生成高温构型，并通过势能约束将其直接映射到目标分布。这项工作展示了生成模型在增强分子模拟采样效率方面的应用，属于化学信息学中利用机器学习模型解决复杂化学系统模拟问题的核心主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Replica exchange (REX) is one of the most widely used enhanced sampling methodologies, yet its efficiency is limited by the requirement for a large number of intermediate temperature replicas. Here we present Generative Replica Exchange (GREX), which integrates deep generative models into the REX framework to eliminate this temperature ladder. Drawing inspiration from reservoir replica exchange (res-REX), GREX utilizes trained normalizing flows to generate high-temperature configurations on demand and map them directly to the target distribution using the potential energy as a constraint, without requiring target-temperature training data. This approach reduces production simulations to a single replica at the target temperature while maintaining thermodynamic rigor through Metropolis exchange acceptance. We validate GREX on three benchmark systems of increasing complexity, highlighting its superior efficiency and practical applicability for molecular simulations.

</details>

---

### 40. [Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows](https://arxiv.org/abs/2603.18205)

**基本信息**

- 🔗 arXiv: [`2603.18205`](https://arxiv.org/abs/2603.18205)
- 👥 作者: Dominic Schuh, Lena Funcke, Janik Kreit 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用归一化流（一种生成模型）来解决掺杂哈伯德模型的模拟难题，这直接属于化学信息学和计算化学中利用‘化学大模型’进行复杂系统建模和模拟的主题。

**📖 中文摘要**

本文研究了掺杂哈伯德模型在有限化学势下的模拟问题，该模型因符号问题而难以处理。作者扩展了在零掺杂情况下使用归一化流的最新进展，通过引入退火方案来实现遍历采样，从而将方法推广到有限化学势情况。与在电荷基下的最先进混合蒙特卡罗方法相比，该方法能准确重现精确对角化结果，并将统计不确定性降低了一个数量级。这项工作展示了归一化流这一生成模型在解决强关联电子系统模拟这一核心化学物理问题中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hubbard model at finite chemical potential is a cornerstone for understanding doped correlated systems, but simulations are severely limited by the sign problem. In the auxiliary-field formulation, the spin basis mitigates the sign problem, yet severe ergodicity issues have limited its use. We extend recent advances with normalizing flows at half-filling to finite chemical potential by introducing an annealing scheme enabling ergodic sampling. Compared to state-of-the-art hybrid Monte Carlo in the charge basis, our approach accurately reproduces exact diagonalization results while reducing statistical uncertainties by an order of magnitude, opening a new path for simulations of doped correlated systems.

</details>

---

### 41. [A Hybrid Conditional Diffusion-DeepONet Framework for High-Fidelity Stress Prediction in Hyperelastic Materials](https://arxiv.org/abs/2603.18225)

**基本信息**

- 🔗 arXiv: [`2603.18225`](https://arxiv.org/abs/2603.18225)
- 👥 作者: Purna Vindhya Kota, Meer Mehran Rashid, Somdatta Goswami 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18225.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用条件扩散模型（cDDPM）和神经算子（DeepONet）等先进的机器学习模型来解决材料科学中的物理场预测问题，这属于‘化学大模型’在跨学科计算（化学/材料）中的应用范畴。

**📖 中文摘要**

本文提出了一种混合条件扩散-DeepONet框架（cDDPM-DeepONet），用于超弹性材料中复杂微结构的高保真应力预测。该框架将应力形态与幅值解耦：一个基于UNet的条件去噪扩散概率模型（cDDPM）生成归一化的冯·米塞斯应力场，同时一个改进的DeepONet预测全局缩放参数。这种方法允许扩散模型专注于空间结构，而算子网络校正全局幅值，从而缓解了光谱和缩放偏差。该工作展示了扩散模型和神经算子等先进机器学习架构在材料科学和计算化学中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting stress fields in hyperelastic materials with complex microstructures remains challenging for traditional deep learning surrogates, which struggle to capture both sharp stress concentrations and the wide dynamic range of stress magnitudes. Convolutional architectures such as UNet tend to oversmooth high-frequency gradients, while neural operators like DeepONet exhibit spectral bias and underpredict localized extremes. Diffusion models can recover fine-scale structure but often introduce low-frequency amplitude drift, degrading physical scaling. To address these limitations, we propose a hybrid surrogate framework, cDDPM-DeepONet, that decouples stress morphology from magnitude. A conditional denoising diffusion probabilistic model (cDDPM), built on a UNet backbone, generates normalized von Mises stress fields conditioned on geometry and loading. In parallel, a modified DeepONet predicts global scaling parameters (minimum and maximum stress), enabling reconstruction of full-resolution physical stress maps. This separation allows the diffusion model to focus on spatial structure while the operator network corrects global amplitude, mitigating spectral and scaling biases. We evaluate the framework on nonlinear hyperelastic datasets with single and multiple polygonal voids. The proposed model consistently outperforms UNet, DeepONet, and standalone cDDPM baselines by one to two orders of magnitude. Spectral analysis shows strong agreement with finite element solutions across all wavenumbers, preserving both global behavior and localized stress concentrations.

</details>

---

### 42. [Impact of automatic speech recognition quality on Alzheimer's disease detection from spontaneous speech: a reproducible benchmark study with lexical modeling and statistical validation](https://arxiv.org/abs/2603.18239)

**基本信息**

- 🔗 arXiv: [`2603.18239`](https://arxiv.org/abs/2603.18239)
- 👥 作者: Himadri Samanta
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18239.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用ASR和机器学习模型从语音信号中提取特征并进行疾病分类。虽然领域不同，但其‘从复杂仪器信号（语音/质谱）中提取特征并利用模型进行推理’的方法论与‘质谱结构推理’的核心任务高度相似，可视为相关技术在不同领域的平行应用。

**📖 中文摘要**

本研究调查了自动语音识别（ASR）质量对基于自发语音的阿尔茨海默病检测下游临床语言建模的影响。研究使用Whisper ASR转录本在ADReSSo 2021诊断数据集上提取词汇特征，并评估可解释的机器学习模型（如逻辑回归和线性支持向量机）。结果表明，转录质量对分类性能有统计学上的显著影响。该研究提供了一个可复现的基准流程，并强调了ASR选择作为临床语音人工智能系统中关键建模决策的作用。虽然论文主题是医学诊断，但其核心方法涉及从语音信号（可视为一种时间序列/光谱数据）中提取特征并进行分类，其数据处理和模型评估流程与从质谱等复杂仪器数据中提取信息进行推理有方法论上的相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early detection of Alzheimer's disease from spontaneous speech has emerged as a promising non-invasive screening approach. However, the influence of automatic speech recognition (ASR) quality on downstream clinical language modeling remains insufficiently understood. In this study, we investigate Alzheimer's disease detection using lexical features derived from Whisper ASR transcripts on the ADReSSo 2021 diagnosis dataset. We evaluate interpretable machine-learning models, including Logistic Regression and Linear Support Vector Machines, using TF-IDF text representations under repeated 5x5 stratified cross-validation. Our results demonstrate that transcript quality has a statistically significant impact on classification performance. Models trained on Whisper-small transcripts consistently outperform those using Whisper-base transcripts, achieving balanced accuracy above 0.7850 with Linear SVM. Paired statistical testing confirms that the observed improvements are significant. Importantly, classifier complexity contributes less to performance variation than ASR transcription quality. Feature analysis reveals that cognitively normal speakers produce more semantically precise object- and scene-descriptive language, whereas Alzheimer's speech is characterized by vagueness, discourse markers, and increased hesitation patterns. These findings suggest that high-quality ASR can enable simple, interpretable lexical models to achieve competitive Alzheimer's detection performance without explicit acoustic modeling. The study provides a reproducible benchmark pipeline and highlights ASR selection as a critical modeling decision in clinical speech-based artificial intelligence systems.

</details>

---

### 43. [Precise Performance of Linear Denoisers in the Proportional Regime](https://arxiv.org/abs/2603.18483)

**基本信息**

- 🔗 arXiv: [`2603.18483`](https://arxiv.org/abs/2603.18483)
- 👥 作者: Reza Ghane, Danil Akhtiamov, Babak Hassibi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18483.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对线性降噪器进行理论分析，并明确其动机来源于扩散模型中的降噪步骤。这直接关联到生成模型（扩散模型）的理论基础，属于‘化学大模型’（特别是生成模型）相关的基础理论研究。

**📖 中文摘要**

本文研究了在高维比例体系下，用于含噪声数据的线性降噪器的性能。给定形式为 $\mathbf{x} + \mathbf{z}$ 的噪声数据，其中 $\mathbf{x}$ 是协方差未知的期望数据，$\mathbf{z}$ 是加性高斯噪声。作者没有采用估计协方差再构建经验维纳滤波器的标准方法，而是受扩散模型中降噪步骤的启发，采用了一种不同的方法：通过向数据样本中注入具有不同协方差的高斯噪声来合成噪声样本，然后以最小二乘意义训练一个线性降噪器 $\mathbf{W}$。在比例体系 $\frac{n}{d} \rightarrow \kappa > 1$ 下，作者使用凸高斯最小最大定理（CGMT）解析地找到了该过程获得的降噪器的泛化误差的闭合形式表达式。这项工作为理解扩散模型等生成模型中降噪步骤的理论基础提供了见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the present paper we study the performance of linear denoisers for noisy data of the form $\mathbf{x} + \mathbf{z}$, where $\mathbf{x} \in \mathbb{R}^d$ is the desired data with zero mean and unknown covariance $\mathbf{\Sigma}$, and $\mathbf{z} \sim \mathcal{N}(0, \mathbf{\Sigma}_{\mathbf{z}})$ is additive noise. Since the covariance $\mathbf{\Sigma}$ is not known, the standard Wiener filter cannot be employed for denoising. Instead we assume we are given samples $\mathbf{x}_1,\dots,\mathbf{x}_n \in \mathbb{R}^d$ from the true distribution. A standard approach would then be to estimate $\mathbf{\Sigma}$ from the samples and use it to construct an ``empirical" Wiener filter. However, in this paper, motivated by the denoising step in diffusion models, we take a different approach whereby we train a linear denoiser $\mathbf{W}$ from the data itself. In particular, we synthetically construct noisy samples $\hat{\mathbf{x}}_i$ of the data by injecting the samples with Gaussian noise with covariance $\mathbf{\Sigma}_1 \neq \mathbf{\Sigma}_{\mathbf{z}}$ and find the best $\mathbf{W}$ that approximates $\mathbf{W}\hat{\mathbf{x}}_i \approx \mathbf{x}_i$ in a least-squares sense. In the proportional regime $\frac{n}{d} \rightarrow \kappa > 1$ we use the {\it Convex Gaussian Min-Max Theorem (CGMT)} to analytically find the closed form expression for the generalization error of the denoiser obtained from this process. Using this expression one can optimize over $\mathbf{\Sigma}_1$ to find the best possible denoiser. Our numerical simulations show that our denoiser outperforms the ``empirical" Wiener filter in many scenarios and approaches the optimal Wiener filter as $\kappa\rightarrow\infty$.

</details>

---

### 44. [Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement](https://arxiv.org/abs/2603.18497)

**基本信息**

- 🔗 arXiv: [`2603.18497`](https://arxiv.org/abs/2603.18497)
- 👥 作者: Quilee Simeon
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18497.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从不完全的观测数据中推断神经网络的连接结构。其‘从观测数据反推生成模型的结构’这一核心问题，与‘质谱结构推理’（从质谱信号反推分子结构）在抽象层面上属于同一类逆问题，方法论上具有相关性。

**📖 中文摘要**

本文提出了一种基于协方差的方法，用于从稀疏、部分观测中推断递归神经网络（模拟神经回路）的连接性。该方法通过在多个记录会话中累积成对协方差估计，无需同时记录所有神经元即可重建完整的连接矩阵。一个基于投影梯度下降的格兰杰因果细化步骤通过生物约束来增强结果。该工作涉及从高维、不完全的观测数据中推断底层图结构（连接矩阵），这与从质谱数据中推断分子结构（质谱结构推理）在问题形式上具有类比性：都是从观测信号反推生成该信号的底层结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inferring the connectivity of neural circuits from incomplete observations is a fundamental challenge in neuroscience. We present a covariance-based method for estimating the weight matrix of a recurrent neural network from sparse, partial measurements across multiple recording sessions. By accumulating pairwise covariance estimates across sessions where different subsets of neurons are observed, we reconstruct the full connectivity matrix without requiring simultaneous recording of all neurons. A Granger-causality refinement step enforces biological constraints via projected gradient descent. Through systematic experiments on synthetic networks modeling small brain circuits, we characterize a fundamental control-estimation tradeoff: stimulation aids identifiability but disrupts intrinsic dynamics, with the optimal level depending on measurement density. We discover that the ``incorrect'' linear approximation acts as implicit regularization -- outperforming the oracle estimator with known nonlinearity at all operating regimes -- and provide an exact characterization via the Stein--Price identity.

</details>

---

### 45. [DeePAW: A universal machine learning model for orbital-free ab initio calculations](https://arxiv.org/abs/2603.18650)

**基本信息**

- 🔗 arXiv: [`2603.18650`](https://arxiv.org/abs/2603.18650)
- 👥 作者: Tianhao Su, Shunbo Hu, Yue Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18650.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个通用的机器学习模型（DeePAW）用于无轨道从头算计算，这直接属于‘化学大模型’在计算化学和材料科学中的核心应用，旨在用AI模型替代或加速传统的量子化学计算。

**📖 中文摘要**

本文提出了深度增强方式模型（DeePAW），这是一种用于无轨道（OF）从头算计算的通用机器学习模型。DeePAW基于密度泛函理论（DFT），是目前覆盖元素最多、晶体结构应用能力最广、且无需微调即可实现最高预测精度的OFDFT ML模型。其科学价值源于新颖的SE(3)-等变双消息传递神经网络。除了预测电子密度分布，DeePAW还能预测晶体的形成能，从而为超越传统电子结构计算方法的跨尺度材料建模开辟了高效途径。这项工作代表了在化学和材料科学中构建通用、准确的‘化学大模型’以替代或加速传统计算的重要进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing universal machine learning models for ab initio calculations is the frontier of materials cutting edge research in the new era of artificial intelligence. Here, we present the Deep Augment Way model (DeePAW) that is a universal machine learning (ML) model for orbital-free (OF) ab initio calculations, based on the density functional theory (DFT). DeePAW is currently the best OFDFT ML model according to the three criterions, 1) covering the largest number of elements, 2) having the widest application capability to diverse crystal structures, and 3) achieving the highest prediction accuracy without further fine-tuning. These scientific merits and innovations of DeePAW are stemmed from the novel SE(3)-equivariant double massage passing neuron networks. Besides predicting electron density distributions, DeePAW predicts formation energies of crystals as well and therefore paves an efficient avenue for multiscale materials modeling beyond conventional electronic structure calculation methods.

</details>

---

### 46. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](https://arxiv.org/abs/2603.18864)

**基本信息**

- 🔗 arXiv: [`2603.18864`](https://arxiv.org/abs/2603.18864)
- 👥 作者: Samuel Del Fré, Gilberto A. Alou Angulo, Maurice Monnerville 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18864.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对特定的化学系统（NO-石墨散射），构建一个数据驱动的机器学习原子间势（MLIP）。这属于化学信息学和计算化学中利用机器学习模型（‘化学大模型’的一种形式）来准确、高效地模拟化学过程和相互作用的典型研究。

**📖 中文摘要**

本文为气体-表面散射动力学开发了一种数据驱动的工作流程，用于构建机器学习原子间势（MLIP），以一氧化氮（NO）在石墨上的散射作为基准系统。工作流程从初始的从头算分子动力学数据集开始，使用SOAP描述符描述局部原子环境，并通过主成分分析在降维特征空间中进行分析。使用最远点采样构建紧凑训练集，并通过基于委员会的主动学习策略，从扩展的入射能量和表面温度范围的分子动力学模拟中提取额外构型来细化最终的深度势能模型。最终的MLIP以远低于AIMD的计算成本实现了大规模NO散射分子动力学模拟。这项工作展示了在化学动力学领域构建专用机器学习势能面的完整流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate atomistic simulations of gas-surface scattering require potential energy surfaces that remain reliable over broad configurational and energetic ranges while retaining the efficiency needed for extensive trajectory sampling. Here, we develop a data-driven workflow for constructing a machine-learning interatomic potential (MLIP) tailored to gas-surface scattering dynamics, using nitric oxide (NO) scattering from highly oriented pyrolytic graphite (HOPG) as a benchmark system. Starting from an initial ab initio molecular dynamics (AIMD) dataset, local atomic environments are described by SOAP descriptors and analyzed in a reduced feature space obtained through principal component analysis. Farthest point sampling is then used to build a compact training set, and the resulting Deep Potential model is refined through a query-by-committee active-learning strategy using additional configurations extracted from molecular dynamics simulations over extended ranges of incident energies and surface temperatures. The final MLIP reproduces reference energies and forces with high fidelity and enables large-scale molecular dynamics simulations of NO scattering from graphite at a computational cost far below that of AIMD. The simulations provide detailed insight into adsorption energetics, trapping versus direct scattering probabilities, translational energy loss, angular distributions, and rotational excitation. Overall, the results reproduce the main experimental trends and demonstrate that descriptor-guided sampling combined with active learning offers an efficient and transferable strategy for constructing MLIPs for gas-surface interactions.

</details>

---

### 47. [Improving moment tensor solutions under Earth structure uncertainty with simulation-based inference](https://arxiv.org/abs/2603.18925)

**基本信息**

- 🔗 arXiv: [`2603.18925`](https://arxiv.org/abs/2603.18925)
- 👥 作者: A. A. Saoulis, T.-S. Pham, A. M. G. Ferreira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用基于模拟的推理（SBI）和深度学习算法来解决地球物理中的逆问题（矩张量反演）。SBI与生成模型密切相关，这项工作属于利用先进的机器学习模型（‘化学大模型’在广义科学计算中的应用）处理科学计算中的不确定性和逆问题。

**📖 中文摘要**

本文介绍了使用基于模拟的推理（SBI）来处理全波形矩张量反演中地球结构不确定性的稳健方法。SBI是一种机器学习方法，可以经验性地建模理论误差对观测的影响。该框架保持了贝叶斯推理的严谨性，同时避免了对不确定性函数形式的限制性假设。作者开发了两种利用SBI改进矩张量解质量的形式：一种基于对理论误差的物理洞察，另一种利用端到端深度学习算法。研究表明，高斯假设会导致偏差并显著低估矩张量的不确定性，而SBI能产生更可靠、校准更好的地震源机制后验分布。这项工作展示了生成模型（扩散模型）和机器学习方法在解决地球物理逆问题中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian inference represents a principled way to incorporate Earth structure uncertainty in full-waveform moment tensor inversions, but traditional approaches generally require significant approximations that risk biasing the resulting solutions. We introduce a robust method for handling theory errors using simulation-based inference (SBI), a machine learning approach that empirically models their impact on the observations. This framework retains the rigour of Bayesian inference while avoiding restrictive assumptions about the functional form of the uncertainties. We begin by demonstrating that the common Gaussian parametrisation of theory errors breaks down under minor ($1-3 \%$) 1-D Earth model uncertainty. To address this issue, we develop two formalisms for utilising SBI to improve the quality of the moment tensor solutions: one using physics-based insights into the theory errors, and another utilising an end-to-end deep learning algorithm. We then compare the results of moment tensor inversion with the standard Gaussian approach and SBI, and demonstrate that Gaussian assumptions induce bias and significantly under-report moment tensor uncertainties. We also show that these effects are particularly problematic when inverting short period data and for shallow, isotropic events. On the other hand, SBI produces more reliable, better calibrated posteriors of the earthquake source mechanism. Finally, we successfully apply our methodology to two well studied moderate magnitude earthquakes: one from the 1997 Long Valley Caldera volcanic earthquake sequence, and the 2020 Zagreb earthquake.

</details>

---

### 48. [BSTModelKit.jl: A Julia Package for Constructing, Solving, and Analyzing Biochemical Systems Theory Models](https://arxiv.org/abs/2603.19115)

**基本信息**

- 🔗 arXiv: [`2603.19115`](https://arxiv.org/abs/2603.19115)
- 👥 作者: Sandra Vadhin, Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19115.pdf)

**💡 相关性分析**

满足标准2：论文的核心内容是发布一个用于生化系统理论建模的新软件工具（BSTModelKit.jl）。该工具提供了构建、模拟和分析生化网络模型的功能，属于为化学和系统生物学研究提供的数据集、资源或工具，可用于支持更复杂的化学大模型构建或验证。

**📖 中文摘要**

本文介绍了BSTModelKit.jl，一个用于构建、求解和分析生化系统理论（BST）模型的开源Julia软件包。该包实现了S-system表示法，这是一种用于建模代谢和调控网络的规范幂律形式主义。BSTModelKit.jl提供了声明式模型规范格式、通过常微分方程（ODE）积分的动态模拟、稳态计算以及使用Morris和Sobol方法的全局敏感性分析。该软件包利用了Julia科学计算生态系统，特别是SciML微分方程求解器套件，以提供高效灵活的模型分析工具。这项工作为生化网络建模提供了新的软件资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present this http URL , an open-source Julia package for constructing, solving, and analyzing Biochemical Systems Theory (BST) models of biochemical networks. The package implements S-system representations, a canonical power-law formalism for modeling metabolic and regulatory networks. this http URL provides a declarative model specification format, dynamic simulation via ordinary differential equation (ODE) integration, steady-state computation, and global sensitivity analysis using the Morris and Sobol methods. The package leverages the Julia scientific computing ecosystem, in particular the SciML suite of differential equation solvers, to provide efficient and flexible model analysis tools. We describe the mathematical formulation, software design, and demonstrate the package capabilities with illustrative examples.

</details>

---

### 49. [CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions](https://arxiv.org/abs/2403.17210)

**基本信息**

- 🔗 arXiv: [`2403.17210`](https://arxiv.org/abs/2403.17210)
- 👥 作者: Azmine Toushik Wasi, Taki Hasan Rafi, Raima Islam 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2403.17210.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于变分图自编码器（VGAE）的深度图学习框架（CADGL）来预测药物-药物相互作用。这直接属于化学信息学中利用图神经网络等‘化学大模型’进行分子性质预测和关系推理的核心主题。

**📖 中文摘要**

本文提出了CADGL，一个用于预测药物-药物相互作用（DDI）的新型上下文感知深度图学习框架。基于定制的变分图自编码器（VGAE），该框架使用两个上下文预处理器从两个不同角度（局部邻域和分子上下文）在异质图结构中提取关键的结构和物理化学信息。定制的VGAE由图编码器、潜在信息编码器和MLP解码器组成。CADGL超越了其他最先进的DDI预测模型，在预测具有临床价值的新型DDI方面表现出色。这项工作展示了图神经网络在化学信息学和药物发现中的重要应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Examining Drug-Drug Interactions (DDIs) is a pivotal element in the process of drug development. DDIs occur when one drug's properties are affected by the inclusion of other drugs. Detecting favorable DDIs has the potential to pave the way for creating and advancing innovative medications applicable in practical settings. However, existing DDI prediction models continue to face challenges related to generalization in extreme cases, robust feature extraction, and real-life application possibilities. We aim to address these challenges by leveraging the effectiveness of context-aware deep graph learning by introducing a novel framework named CADGL. Based on a customized variational graph autoencoder (VGAE), we capture critical structural and physio-chemical information using two context preprocessors for feature extraction from two different perspectives: local neighborhood and molecular context, in a heterogeneous graphical structure. Our customized VGAE consists of a graph encoder, a latent information encoder, and an MLP decoder. CADGL surpasses other state-of-the-art DDI prediction models, excelling in predicting clinically valuable novel DDIs, supported by rigorous case studies. CADGL is vailable at: this https URL

</details>

---

### 50. [Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset](https://arxiv.org/abs/2407.17869)

**基本信息**

- 🔗 arXiv: [`2407.17869`](https://arxiv.org/abs/2407.17869)
- 👥 作者: Yiming Ma, Jianzhi Teng, Xinjie Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.17869.pdf)

**💡 相关性分析**

满足标准1和标准2：1）论文的核心研究内容是提出一种新的生成模型框架（解耦条件流匹配，DCFM）来解决逆椭圆偏振这一物理逆问题，这属于利用‘化学大模型’（生成模型）解决材料表征问题。2）论文构建并发布了EllipBench，一个包含超过800万个样本的大规模、高精度数据集，这为相关领域的研究提供了宝贵的数据资源。

**📖 中文摘要**

本文针对逆椭圆偏振问题（即从测量的相位差Δ和振幅比Ψ重建光学常数和薄膜厚度），引入了EllipBench基准数据集，包含超过800万个高精度样本，涵盖98种薄膜材料和5种基底。基于此基准，作者系统评估了多种方法，并提出了解耦条件流匹配（DCFM）框架。DCFM将几何膜厚解耦并将其作为稳健的物理条件，来指导一个连续向量场，用于对波长相关光学常数的逆概率分布进行建模。该工作结合了大规模数据集构建和新型生成模型（流匹配）的应用，以解决物理逆问题中的固有模糊性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse ellipsometry, i.e., reconstructing optical constants and film thickness from the measured phase difference $\Delta$ and amplitude ratio $\Psi$, is a fundamentally ill-posed problem. Traditional solutions rely on slow, expert-driven iterative fitting, while the development of machine learning approaches has been severely limited by the lack of large-scale, physically consistent datasets. To address this gap, we introduce \textbf{EllipBench}, a comprehensive benchmark comprising over 8 million high-precision samples spanning 98 thin-film materials and 5 substrates. Building upon this benchmark, we conduct a systematic evaluation of a broad spectrum of methods, including traditional machine learning models, deep neural networks, and Physics-Informed Neural Networks, and show that existing paradigms consistently struggle to fully resolve the inverse ellipsometry task. To better capture its inherent ambiguity, we further propose a novel \textbf{Decoupled Conditional Flow Matching (DCFM)} framework. Rather than formulating the problem as deterministic point-to-point regression, DCFM explicitly decouples geometric film thickness and incorporates it as a robust physical condition to guide a continuous vector field for modeling the inverse probability distribution of wavelength-dependent optical constants. Combined with a gradient detachment strategy and physics-based constraints, our joint architecture effectively mitigates intrinsic physical ambiguities and delivers a robust and accurate solution for inverse ellipsometry.

</details>

---

### 51. [Biased AI can Influence Political Decision-Making](https://arxiv.org/abs/2410.06415)

**基本信息**

- 🔗 arXiv: [`2410.06415`](https://arxiv.org/abs/2410.06415)
- 👥 作者: Jillian Fisher, Shangbin Feng, Robert Aron 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.06415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种可用于化学设计（如材料发现）的模型优化方法，与“化学大模型”主题直接相关。

**📖 中文摘要**

论文《Cliqueformer: Model-Based Optimization with Structured Transformers》提出了一种基于Transformer的架构Cliqueformer，用于解决离线模型优化（MBO）问题。该模型通过学习黑盒函数的结构（通过功能图模型FGM）来应对分布偏移，而无需依赖显式的保守方法。论文在多个领域（包括化学和遗传设计任务）中展示了其性能优于现有方法。这项工作与“化学大模型”主题相关，因为它提出了一种可用于化学设计（如材料发现）的通用优化框架，属于模型驱动的化学发现方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As modern large language models (LLMs) become integral to everyday tasks, concerns about their inherent biases and their potential impact on human decision-making have emerged. While bias in models are well-documented, less is known about how these biases influence human decisions. This paper presents two interactive experiments investigating the effects of partisan bias in LLMs on political opinions and decision-making. Participants interacted freely with either a biased liberal, biased conservative, or unbiased control model while completing these tasks. We found that participants exposed to partisan biased models were significantly more likely to adopt opinions and make decisions which matched the LLM's bias. Even more surprising, this influence was seen when the model bias and personal political partisanship of the participant were opposite. However, we also discovered that prior knowledge of AI was weakly correlated with a reduction of the impact of the bias, highlighting the possible importance of AI education for robust mitigation of bias effects. Our findings not only highlight the critical effects of interacting with biased LLMs and its ability to impact public discourse and political conduct, but also highlights potential techniques for mitigating these risks in the future.

</details>

---

### 52. [DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models](https://arxiv.org/abs/2503.16426)

**基本信息**

- 🔗 arXiv: [`2503.16426`](https://arxiv.org/abs/2503.16426)
- 👥 作者: Keyan Chen, Chenyang Liu, Bowen Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.16426.pdf)

**💡 相关性分析**

满足标准1：论文提出的动态稀疏处理、自适应建模和区域级特征学习框架，其核心思想和技术路径（处理稀疏、高维数据并提取关键特征）与“质谱结构推理”中处理复杂质谱数据、识别关键碎片离子的挑战高度相关，可视为一种相关的方法论探讨。

**📖 中文摘要**

论文《DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models》提出了一种专为遥感图像稀疏特性设计的视觉基础模型DynamicVis。它引入了一种动态区域感知状态空间模型（Dynamic Region-Aware SSM），能够自适应地处理和建模仅与任务相关的高显著性标记，同时采用参数无关的背景上下文集成，从而大幅降低了处理超长二维标记序列的复杂度。该模型在包括小目标检测和变化检测在内的多个下游任务中表现出色。虽然论文主要关注遥感图像，但其提出的动态稀疏处理、自适应建模以及区域级元嵌入多实例学习（MIL）预训练范式，为解决“质谱结构推理”中常见的稀疏、高维数据（如质谱峰）的建模和特征提取问题提供了潜在的技术思路和架构参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The advancement of RS technology has enabled high-resolution Earth observation; however, interpreting these images using modern VFMs remains a significant challenge. Unlike object-centric natural images, RS imagery is fundamentally characterized by extreme target sparsity and massive spatial redundancy. Key objects of interest (e.g., ships, vehicles) often occupy less than 1% of the spatial extent, surrounded by vast, target-free backgrounds. Existing VFMs predominantly rely on uniform dense processing (e.g., ViTs) and pixel-reconstruction pre-training paradigms (e.g., MAE). These approaches inherently waste substantial computational capacity on modeling redundant backgrounds and inadvertently dilute the feature representations of small, sparse targets. To bridge this structural misalignment, we propose DynamicVis, a visual foundation model explicitly tailored to the sparse nature of RS imagery. Architecturally, DynamicVis introduces a Dynamic Region-Aware SSM that bypasses uniform computation. It adaptively routes and incrementally models only task-relevant, high-salience tokens while employing a parameter-free integration for background context, drastically reducing the complexity of processing ultra-long 2D token sequences ($\sim$100,000). Crucially, to equip the network with robust spatial-selection capabilities, we propose a novel Region-Level Meta-Embedding Multi-Instance Learning (MIL) pre-training paradigm. Trained on a million-scale dataset, this paradigm explicitly disentangles sparse foreground instances from dense backgrounds in the latent semantic space, overcoming the semantic ambiguity of conventional pixel-reconstruction methods. Extensive evaluations across nine diverse downstream tasks reveal that DynamicVis exhibits exceptional efficacy, particularly dominating in sparse-target and instance-level perception tasks (e.g., small object detection, and change detection).

</details>

---

### 53. [Faster multivariate integration in D-modules](https://arxiv.org/abs/2504.12724)

**基本信息**

- 🔗 arXiv: [`2504.12724`](https://arxiv.org/abs/2504.12724)
- 👥 作者: Hadrien Brochet, Frédéric Chyzak, Pierre Lairez
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.12724.pdf)

**💡 相关性分析**

满足标准1：论文的核心是发展一种高效的数学计算算法（多元积分），该算法在计算化学、谱学模拟等化学信息学核心计算任务中有直接应用潜力，与“化学信息学”主题相关。

**📖 中文摘要**

论文《Faster multivariate integration in D-modules》提出了一种解决全纯积分约化问题的新算法，该算法将Griffiths-Dwork约化技术扩展到全纯系统，并提供了在Julia中的实现。作为应用，论文推导出了8-正则图生成系列的一个先前无法获得的微分方程。这项工作属于“化学信息学”中计算化学和数学化学的交叉领域。微分方程和积分技术在化学中常用于描述反应动力学、量子化学计算以及谱图（如NMR、质谱）的模拟与分析。论文提出的高效多元积分算法，为处理化学中的复杂数学模型和计算问题（例如，从理论模型推导光谱或性质）提供了潜在的加速工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a new algorithm for solving the reduction problem in the context of holonomic integrals, which in turn provides an approach to integration with parameters. Our method extends the Griffiths--Dwork reduction technique to holonomic systems and is implemented in Julia. While not yet outperforming creative telescoping in D-finite cases, it enhances computational capabilities within the holonomic framework. As an application, we derive a previously unattainable differential equation for the generating series of 8-regular graphs.

</details>

---

### 54. [Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability](https://arxiv.org/abs/2505.03530)

**基本信息**

- 🔗 arXiv: [`2505.03530`](https://arxiv.org/abs/2505.03530)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03530.pdf)

**💡 相关性分析**

满足标准1：论文提出的因果干预框架旨在深度理解生成模型（VAE）的内部工作机制，这与构建可解释、可控的“化学大模型”（用于分子生成、性质预测等）的核心挑战直接相关，提供了重要的可解释性方法论。

**📖 中文摘要**

论文《Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability》为变分自编码器（VAE）的机制可解释性引入了一个全面的因果干预框架。该框架开发了识别和分析VAE中“电路模式”的技术，研究语义因子如何通过网络层进行编码、处理和分离。方法包括在输入操作、潜在空间扰动、激活修补和因果中介分析等不同层次进行针对性干预。论文在具有已知因果关系的合成数据集和标准解纠缠基准上应用了该框架。这项工作虽然主要针对VAE，但其核心——通过因果干预理解深度生成模型的内部工作机制——是构建可解释、可控的“化学大模型”（尤其是生成化学结构的模型）的关键基础。该框架为分析化学大模型如何学习并组合化学子结构（即“电路模式”）提供了方法论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic interpretability of deep learning models has emerged as a crucial research direction for understanding the functioning of neural networks. While significant progress has been made in interpreting discriminative models like transformers, understanding generative models such as Variational Autoencoders (VAEs) remains challenging. This paper introduces a comprehensive causal intervention framework for mechanistic interpretability of VAEs. We develop techniques to identify and analyze "circuit motifs" in VAEs, examining how semantic factors are encoded, processed, and disentangled through the network layers. Our approach uses targeted interventions at different levels: input manipulations, latent space perturbations, activation patching, and causal mediation analysis. We apply our framework to both synthetic datasets with known causal relationships and standard disentanglement benchmarks. Results show that our interventions can successfully isolate functional circuits, map computational graphs to causal graphs of semantic factors, and distinguish between polysemantic and monosemantic units. Furthermore, we introduce metrics for causal effect strength, intervention specificity, and circuit modularity that quantify the interpretability of VAE components. Experimental results demonstrate clear differences between VAE variants, with FactorVAE achieving higher disentanglement scores (0.084) and effect strengths (mean 4.59) compared to standard VAE (0.064, 3.99) and Beta-VAE (0.051, 3.43). Our framework advances the mechanistic understanding of generative models and provides tools for more transparent and controllable VAE architectures.

</details>

---

### 55. [RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval](https://arxiv.org/abs/2506.08625)

**基本信息**

- 🔗 arXiv: [`2506.08625`](https://arxiv.org/abs/2506.08625)
- 👥 作者: Minhae Oh, Jeonghye Kim, Nakyung Lee 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08625.pdf)

**💡 相关性分析**

满足标准1：论文的核心是提升LLM在科学领域（包括化学）的推理能力，其提出的逐步检索增强框架直接针对化学大模型所需的知识更新和术语理解挑战，与“化学大模型”主题直接相关。

**📖 中文摘要**

论文《RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval》提出了RAISE框架，通过逐步检索增强大型语言模型（LLM）的科学推理能力。RAISE分为三个步骤：问题分解、逻辑查询生成和逻辑检索。该框架从开放语料库中检索逻辑相关的文档，以应对科学推理中领域术语知识和最新发现更新的挑战。实验表明，RAISE在科学推理基准测试中 consistently 优于其他基线方法。这项工作与“化学大模型”主题高度相关，因为化学领域的推理（如反应预测、逆合成分析、文献挖掘）严重依赖专业术语和不断更新的科学知识。RAISE框架为构建能够进行可靠、可追溯化学推理的大模型提供了关键的技术路径（即检索增强生成，RAG）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific reasoning requires not only long-chain reasoning processes, but also knowledge of domain-specific terminologies and adaptation to updated findings. To deal with these challenges for scientific reasoning, we introduce RAISE, a step-by-step retrieval-augmented framework which retrieves logically relevant documents from in-the-wild corpus. RAISE is divided into three steps: problem decomposition, logical query generation, and logical retrieval. We observe that RAISE consistently outperforms other baselines on scientific reasoning benchmarks. We analyze that unlike other baselines, RAISE retrieves documents that are not only similar in terms of the domain knowledge, but also documents logically more relevant.

</details>

---

### 56. [Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning](https://arxiv.org/abs/2506.16931)

**基本信息**

- 🔗 arXiv: [`2506.16931`](https://arxiv.org/abs/2506.16931)
- 👥 作者: Jiaqi Chen, Mingfeng Fan, Xuefeng Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.16931.pdf)

**💡 相关性分析**

满足标准1：论文提出的多模态融合学习框架，其核心思想（融合异构数据表示进行联合学习与推理）与“质谱结构推理”中整合质谱数据、分子图和其他化学信息以推断分子结构的关键技术路径直接相关。

**📖 中文摘要**

论文《Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning》提出了一个多模态融合学习（MMFL）框架，用于解决机器人任务规划中的广义旅行商问题（GTSP）。该框架利用图和图像两种表示来捕捉问题的互补方面，并学习一个能够实时生成高质量任务规划方案的策略。具体包括一个基于坐标的图像构建器、自适应分辨率缩放策略以及一个带有专用瓶颈的多模态融合模块。虽然应用场景是机器人路径规划，但其核心方法——融合几何（图）和空间（图像）特征的多模态学习框架——与“质谱结构推理”中融合多种数据源（如质谱图、分子图、文本描述）进行结构解析的思路在方法论上高度相似。该论文为解决多模态化学数据（如质谱-结构对）的联合建模与推理提供了有价值的架构参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Effective and efficient task planning is essential for mobile robots, especially in applications like warehouse retrieval and environmental monitoring. These tasks often involve selecting one location from each of several target clusters, forming a Generalized Traveling Salesman Problem (GTSP) that remains challenging to solve both accurately and efficiently. To address this, we propose a Multimodal Fused Learning (MMFL) framework that leverages both graph and image-based representations to capture complementary aspects of the problem, and learns a policy capable of generating high-quality task planning schemes in real time. Specifically, we first introduce a coordinate-based image builder that transforms GTSP instances into spatially informative representations. We then design an adaptive resolution scaling strategy to enhance adaptability across different problem scales, and develop a multimodal fusion module with dedicated bottlenecks that enables effective integration of geometric and spatial features. Extensive experiments show that our MMFL approach significantly outperforms state-of-the-art methods across various GTSP instances while maintaining the computational efficiency required for real-time robotic applications. Physical robot tests further validate its practical effectiveness in real-world scenarios.

</details>

---

### 57. [Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes](https://arxiv.org/abs/2507.12261)

**基本信息**

- 🔗 arXiv: [`2507.12261`](https://arxiv.org/abs/2507.12261)
- 👥 作者: Johann Frei, Nils Feldhus, Lisa Raithel 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.12261.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于LLM智能体的端到端信息结构化框架，其解决的核心问题（从非结构化文本到结构化模式的转换）与化学信息学中的文本挖掘、信息提取和知识库构建任务高度相关，可视为一种相关的方法论创新。

**📖 中文摘要**

论文《Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes》提出了一个由LLM智能体驱动的端到端框架，用于将自由格式的临床笔记转换为结构化的HL7 FHIR资源。该框架利用LLM智能体、代码执行和医学术语数据库工具，旨在提高转换的泛化能力和结构符合性。虽然应用领域是临床信息学，但其核心任务——从非结构化文本中提取结构化信息并填充到复杂的、预定义的模式（FHIR schema）中——与“化学信息学”中从科学文献、实验报告等非结构化文本中提取化学实体、反应、性质等信息，并构建结构化数据库（如化学知识图谱）的任务在本质上相同。该论文展示的基于智能体的、结合领域知识工具（如术语库）的端到端信息提取框架，为化学文本挖掘和知识提取提供了先进的技术范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

For clinical data integration and healthcare services, the HL7 FHIR standard has established itself as a desirable format for interoperability between complex health data. Previous attempts at automating the translation from free-form clinical notes into structured FHIR resources address narrowly defined tasks and rely on modular approaches or LLMs with instruction tuning and constrained decoding. As those solutions frequently suffer from limited generalizability and structural inconformity, we propose an end-to-end framework powered by LLM agents, code execution, and healthcare terminology database tools to address these issues. Our solution, called Infherno, is designed to adhere to the FHIR document schema and competes well with a human baseline in predicting FHIR resources from unstructured text. The implementation features a front end for custom and synthetic data and both local and proprietary models, supporting clinical data integration processes and interoperability across institutions. Gemini 2.5-Pro excels in our evaluation on synthetic and clinical datasets, yet ambiguity and feasibility of collecting ground-truth data remain open problems.

</details>

---

### 58. [Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions](https://arxiv.org/abs/2508.17303)

**基本信息**

- 🔗 arXiv: [`2508.17303`](https://arxiv.org/abs/2508.17303)
- 👥 作者: Dhiraj S Kori, Abhinav Chandraker, Syed Abdur Rahman 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.17303.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发用于材料性能预测的物理信息神经网络（PINN），这属于材料信息学和化学信息学的交叉领域，与构建用于材料发现和性质预测的“化学大模型”主题直接相关。

**📖 中文摘要**

论文《Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions》提出了一种物理信息神经网络（PINN）框架，用于预测核反应堆用钢在辐照等复杂条件下的低周疲劳寿命。该模型将疲劳寿命控制的物理约束嵌入损失函数，实现了物理一致的学习。论文在495个应变控制疲劳数据点上进行了训练，并展示了优于传统机器学习方法的性能。这项工作属于“化学信息学”中材料信息学（Materials Informatics）的子领域。它展示了如何将领域知识（物理约束）与数据驱动模型结合，以预测复杂化学系统（此处为合金材料）在极端环境下的性能。这种方法论对于构建用于材料发现、性质预测的“化学大模型”（尤其是基于物理的机器学习模型）具有直接的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study proposes a Physics-Informed Neural Network (PINN) framework to predict the low-cycle fatigue (LCF) life of irradiated austenitic and ferritic/martensitic (F/M) steels used in nuclear reactors. These materials undergo cyclic loading, neutron irradiation, and elevated temperatures, leading to complex degradation mechanisms that are difficult to capture with conventional empirical or purely data-driven models. The proposed PINN embeds fatigue-life governing physical constraints into the loss function, enabling physically consistent learning while improving predictive accuracy, reliability, and generalizability. The model was trained on 495 strain-controlled fatigue data points spanning irradiated and unirradiated conditions. Compared with traditional machine learning approaches, including Random Forest, Gradient Boosting, eXtreme Gradient Boosting, and conventional neural networks, the PINN demonstrated superior performance. SHapley Additive exPlanations (SHAP) analysis identified strain amplitude, irradiation dose, and test temperature as the dominant features, each exhibiting physically meaningful inverse correlations with fatigue life. Univariate and multivariate analyses revealed clear alloy-specific degradation characteristics. Austenitic steels exhibited strong nonlinear coupling among strain amplitude, irradiation dose, and temperature, resulting in pronounced fatigue degradation under combined loading. In contrast, F/M steels demonstrated comparatively stable irradiation responses, including dose-saturation behavior, but showed sensitivity to elevated temperatures beyond tempering thresholds. Overall, the proposed PINN framework serves as a reliable and interpretable tool for reactor-relevant fatigue assessment, enabling performance evaluation for advanced nuclear applications.

</details>

---

### 59. [Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning](https://arxiv.org/abs/2509.08759)

**基本信息**

- 🔗 arXiv: [`2509.08759`](https://arxiv.org/abs/2509.08759)
- 👥 作者: Mominul Rubel, Adam Meyers, Gabriel Nicolosi
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.08759.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种新的用于科学机器学习的神经网络架构（FLM），其频谱表示和自适应基学习能力，为化学中的科学计算（如求解PDE）和质谱信号的分析与建模提供了核心方法，与两个关注主题均相关。

**📖 中文摘要**

论文《Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning》提出了傅里叶学习机（FLM），一种设计用于表示多维非调和傅里叶级数的神经网络架构。FLM使用具有余弦激活函数的前馈结构，将级数的频率、振幅和相移作为可训练参数进行学习。该设计使模型能够创建适应周期和非周期函数的问题特定谱基。论文在包括偏微分方程（PDE）和最优控制问题（OCP）在内的多个科学计算问题上评估了FLM的性能。计算实验表明，FLM的性能与SIREN等成熟架构相当甚至更优。这项工作与“化学大模型”和“质谱结构推理”均相关：1）FLM为科学机器学习（SciML）提供了一种新的基础模型架构，可用于求解化学中的PDE（如量子化学、反应扩散方程）或进行分子动力学模拟；2）其频谱表示和学习能力，为分析和建模质谱信号（本质上是频率/质荷比域的强度分布）提供了潜在的、更灵活且可学习的表示方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Fourier Learning Machine (FLM), a neural network (NN) architecture designed to represent a multidimensional nonharmonic Fourier series. The FLM uses a simple feedforward structure with cosine activation functions to learn the frequencies, amplitudes, and phase shifts of the series as trainable parameters. This design allows the model to create a problem-specific spectral basis adaptable to both periodic and nonperiodic functions. Unlike previous Fourier-inspired NN models, the FLM is the first architecture able to represent a multidimensional Fourier series with a complete set of basis functions in separable form, doing so by using a standard Multilayer Perceptron-like architecture. A one-to-one correspondence between the Fourier coefficients and amplitudes and phase-shifts is demonstrated, allowing for the translation between a full, separable basis form and the cosine phase-shifted one. Additionally, we evaluate the performance of FLMs on several scientific computing problems, including benchmark Partial Differential Equations (PDEs) and a family of Optimal Control Problems (OCPs). Computational experiments show that the performance of FLMs is comparable, and often superior, to that of established architectures like SIREN and vanilla feedforward NNs.

</details>

---

### 60. [Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity](https://arxiv.org/abs/2601.18032)

**基本信息**

- 🔗 arXiv: [`2601.18032`](https://arxiv.org/abs/2601.18032)
- 👥 作者: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18032.pdf)

**💡 相关性分析**

满足标准2：论文构建并提供了一个高质量的介电弹性体数据集，该数据集整合了分子序列和性能数据，可直接用于化学大模型的训练和评估。

**📖 中文摘要**

本文聚焦于高性能介电弹性体的开发，这是一个化学材料设计问题。作者通过整理过去十年的实验数据，构建了一个高质量的丙烯酸酯基介电弹性体数据集，该数据集系统地整合了分子序列、介电和机械性能。在此基础上，论文提出了一个多模态学习框架，利用大规模预训练的聚合物表示（即化学大模型）来迁移化学和结构知识。该框架能够在数据稀缺的情况下，准确预测介电和机械性能，从而加速软高介电常数弹性体的数据高效发现。这项工作直接提供了用于化学大模型训练和应用的数据集资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggregating experimental results from the past decade. Building on this dataset, we propose a multimodal learning framework leveraging large-scale pretrained polymer representations. These pretrained embeddings transfer chemical and structural knowledge from vast polymer corpora, enabling accurate few-shot prediction of dielectric and mechanical properties and accelerating data-efficient discovery of soft high-$k$ dielectric elastomers. Our data and implementation are publicly available at: this https URL

</details>

---

### 61. [Sheaf Neural Networks and biomedical applications](https://arxiv.org/abs/2602.00159)

**基本信息**

- 🔗 arXiv: [`2602.00159`](https://arxiv.org/abs/2602.00159)
- 👥 作者: Aneeqa Mehrab, Jan Willem Van Looy, Pietro Demurtas 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.00159.pdf)

**💡 相关性分析**

满足标准2：论文提出的层神经网络（SNN）作为一种图神经网络变体，是化学信息学（用于分子图分析）和质谱结构推理（用于谱图关系建模）中常用的工具类方法，提供了潜在的技术资源。

**📖 中文摘要**

本文介绍了层神经网络（SNN）的理论和数学模型，并将其应用于生物医学领域的具体案例研究。虽然论文核心是图神经网络的一种变体，但其应用场景是生物医学问题。在化学信息学和质谱分析领域，图神经网络是用于分子表示学习和质谱结构推理的常用方法。因此，该论文提出的SNN算法作为一种新的图神经网络架构，有潜力被应用于分子图分析或质谱谱图的结构化表示与推理任务中，属于可用于这些主题的工具或方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The purpose of this paper is to elucidate the theory and mathematical modelling behind the sheaf neural network (SNN) algorithm and then show how SNN can effectively answer to biomedical questions in a concrete case study and outperform the most popular graph neural networks (GNNs) as graph convolutional networks (GCNs), graph attention networks (GAT) and GraphSage.

</details>

---

### 62. [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](https://arxiv.org/abs/2603.03686)

**基本信息**

- 🔗 arXiv: [`2603.03686`](https://arxiv.org/abs/2603.03686)
- 👥 作者: Jiangyu Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03686.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个神经符号AI框架（AI4S-SDS）用于自动化化学配方设计和发现，这直接围绕“化学大模型”在材料科学中的应用这一主题。

**📖 中文摘要**

本文提出了AI4S-SDS，一个用于自动化化学配方设计的神经符号框架。该框架集成了多智能体协作和定制的蒙特卡洛树搜索（MCTS）引擎，旨在解决高维组合空间（涉及离散组成选择和连续几何约束）的导航问题。为了确保物理可行性，框架通过一个可微物理引擎桥接符号推理和物理现实，并采用混合归一化损失和稀疏诱导正则化来优化连续混合比例。论文在初步的光刻实验中，识别出一种新型光刻胶显影剂配方，其性能与商业基准相当或更优。这项工作展示了神经符号搜索在科学发现（特别是化学配方设计）中的潜力，直接应用了AI大模型（多智能体、MCTS）解决化学领域复杂优化问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.

</details>

---

### 63. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的AI模型（CliqueFlowmer），用于优化和发现材料，这直接属于“化学大模型”在材料科学和化学信息学中的应用范畴。

**📖 中文摘要**

本文针对计算材料发现（CMD）中的优化问题，提出了一种基于离线模型优化（MBO）的新技术。该方法将目标材料属性的直接优化融合到生成过程中，以克服流行生成模型在探索材料空间有吸引力区域方面的不足。作者引入了领域特定模型CliqueFlowmer，该模型将最新的基于团的MBO进展融入Transformer和流生成中。论文验证了CliqueFlowmer的优化能力，并表明其产生的材料性能显著优于生成基线。这项工作为专门的材料优化问题提供了新的AI驱动方法，属于化学大模型在材料发现与设计方向上的具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 64. [Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining](https://arxiv.org/abs/2603.11103)

**基本信息**

- 🔗 arXiv: [`2603.11103`](https://arxiv.org/abs/2603.11103)
- 👥 作者: Zhiyuan Zeng, Yichi Zhang, Yong Shan 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11103.pdf)

**💡 相关性分析**

满足标准3：论文提出了一种通过重建智能体轨迹来增强LLM预训练的新范式，虽然应用在代码领域，但其关于如何为复杂推理任务构建更丰富训练数据的讨论和框架，对“化学大模型”（尤其是需要规划能力的模型）的构建具有重要的前瞻性和方法论参考价值。

**📖 中文摘要**

本文针对大型语言模型在复杂软件工程中深度、长程推理的不足，提出了一种新的预训练范式：“通过重建来理解”。作者认为，标准的预训练数据（静态软件仓库）只代表了复杂智力过程的最终状态，抽象掉了中间的规划、调试和迭代细化步骤。为了弥补这一差距，论文引入了一个框架，通过多智能体模拟来合成这些潜在的智能体轨迹（规划、推理和调试步骤）。这些轨迹以源代码仓库的结构现实（如依赖图和文件层次结构）为基础，以确保保真度。此外，为了保证合成数据的逻辑严谨性，采用了一种基于搜索的优化技术，迭代地细化思维链推理，以最大化真实代码的可能性。实验表明，在这些重建的轨迹上进行持续预训练，显著增强了Llama-3-8B在多种基准测试上的性能。这项工作虽然主要面向代码生成，但其核心思想——重建智能体轨迹以丰富训练数据——对于构建需要复杂推理的“化学大模型”（例如用于逆合成规划或反应预测）具有重要的方法论启示。

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

满足标准2和3：1) 论文提出的PriCoder框架提供了教导大模型使用私有（专业）API的方法论和潜在工具，可直接应用于教导化学大模型使用化学信息学或质谱分析工具包（标准2）。2) 论文深入探讨了大模型与领域专用工具/库集成的挑战与解决方案，这对化学和质谱领域大模型的开发具有重要的综述和展望意义（标准3）。

**📖 中文摘要**

本文针对大型语言模型在私有库导向的代码生成任务中的局限性，提出了PriCoder方法。该方法通过自动合成数据来教导LLMs调用私有库API。具体而言，PriCoder将私有库数据合成建模为图的构建，并交替使用两个图算子：（1）渐进式图演化，从基本样本逐步合成更多样化的训练样本；（2）多维图剪枝，通过严格的过滤流程提高数据质量。论文基于新发布的、模型不熟悉的库构建了两个新基准进行严格评估。在三个主流LLM上的实验表明，PriCoder显著改善了私有库导向的代码生成能力。虽然该工作聚焦于代码生成，但其核心问题——如何让大模型有效学习和调用未知的、结构化的API（或函数）——与“化学大模型”和“质谱结构推理”高度相关。例如，在化学信息学中，模型需要调用特定的化学信息学工具包（如RDKit）的API来处理分子或分析质谱数据；在质谱分析中，模型可能需要调用谱库搜索或碎片化规则计算的函数。因此，PriCoder提出的数据合成和模型教导方法，为解决化学领域大模型与专业工具集成的问题提供了直接的技术思路和工具。

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

满足标准1：论文的核心研究内容围绕使用大语言模型（LLM）对高维、结构化的序列数据进行建模和推理，这与‘化学大模型’主题中利用大模型处理复杂化学/质谱数据的核心思想直接相关。

**📖 中文摘要**

本文提出了一种用于高维事件序列（如车辆诊断故障码）的统一框架，将事件序列建模、因果发现和大语言模型（LLM）整合在一起。论文的核心是将诊断序列视为一种可以建模、预测和解释的语言。这直接与【化学大模型】的主题相关，因为它展示了如何将LLM应用于结构化、高维的序列数据（类似于化学或质谱数据）进行推理和解释。论文中引入的Transformer架构和用于自动化合成布尔规则的多智能体系统，为复杂数据的结构推理提供了方法论上的借鉴。

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

满足标准1：论文的核心是构建一个用于生物系统预测的大规模基础模型（SCALE），其架构基于LLaMA等大模型，并专注于生成式建模和精确推理。这与‘化学大模型’主题中开发用于化学领域预测和推理的大型生成模型高度相关。

**📖 中文摘要**

本文提出了SCALE，一个用于虚拟细胞扰动预测的大规模基础模型。该模型将扰动预测表述为条件传输问题，并使用基于LLaMA的细胞编码与端点导向监督相结合的集合感知流架构。这项工作属于生物信息学领域，但其核心是开发一个用于预测细胞对扰动反应的、可扩展的、基于大模型的基础设施。模型架构利用了类似LLaMA的大模型进行编码，并专注于生成式建模和生物数据的准确推理。这为在化学信息学中构建类似的大模型（用于预测分子性质或反应）提供了参考范例。

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

满足标准3：论文是一篇针对从复杂生物数据中推断相互作用和关系的计算方法的综合性综述。虽然领域不同，但其涵盖的图神经网络、深度学习等推理方法，与‘质谱结构推理’和‘化学大模型’主题中所需的数据分析和模型构建方法在本质上高度相关，提供了重要的方法论讨论和参考。

**📖 中文摘要**

本文是一篇关于从单细胞和空间组学数据推断和分析细胞间通讯（CCC）的计算方法的综述。文章系统性地介绍了超过140种计算方法，涵盖了方法学框架和生物学问题的多样性。虽然主题是生物信息学，但其核心——从高维、复杂的生物数据中推断相互作用和关系——与【质谱结构推理】和【化学大模型】在方法论上高度相通。质谱数据分析同样涉及从复杂信号中推断分子结构或相互作用，而许多先进的CCC推断方法（如基于图神经网络或深度学习的方法）也可为质谱数据的结构推理提供思路。本文提供了该领域方法论的全面概览。

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

满足标准1：论文的核心研究内容直接围绕机器学习原子间势（MLIP）的泛化能力，这是构建用于分子模拟和性质预测的‘化学大模型’的核心技术之一。论文重点评估了不同模型架构在复杂化学空间中的表现，并提出了改进泛化性的策略。

**📖 中文摘要**

本文系统地评估了具有长程修正的不同机器学习原子间势（MLIP）架构在复杂化学空间中的泛化能力。研究强调了长程建模对于实现可泛化MLIP的重要性，并引入了有偏的训练-测试分割策略来严格评估模型在化学空间不同区域的性能。这项工作直接针对【化学大模型】的一个关键子领域——开发能够准确、可泛化地模拟分子和材料性质的机器学习势函数。论文的核心挑战（泛化性）和解决方案（长程修正、严格的基准测试）对于构建稳健的化学大模型至关重要。

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

满足标准3：论文包含对下一代药物发现范式的展望性讨论，其中核心部分阐述了机器学习大模型与高性能/量子计算结合以实现化学精度模拟的融合趋势。这为‘化学大模型’主题提供了重要的未来发展方向和跨领域整合的讨论。

**📖 中文摘要**

本文展望了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何彻底改变药物发现。文章明确指出，机器学习基础模型（如FeNNix-Bio1）能够实现量子精度的模拟，但其数据生成受限于经典计算。而高性能量子计算（HPQC）将成为量子化学数据的终极加速器，实现真正的化学精度。论文的核心论点是这种“三位一体”的融合将优化从系统准备到高保真模拟的整个药物发现流程。这直接与【化学大模型】的未来发展愿景相关，即利用更强大的计算基础（包括量子计算）来训练和部署能够进行高精度化学预测的大型模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

## 📊 数据统计
- 累计运行天数：41
- 累计论文数量：2951

## 📝 历史记录

> 暂无历史数据

