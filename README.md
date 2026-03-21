# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-21 12:38:19

## 📅 2026-03-21 (今日最新)

**相关论文数：77**

### 1. [Continually self-improving AI](https://arxiv.org/abs/2603.18073)

**基本信息**

- 🔗 arXiv: [`2603.18073`](https://arxiv.org/abs/2603.18073)
- 👥 作者: Zitong Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18073.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建能够持续自我改进的AI系统，这直接围绕“化学大模型”这一主题的核心挑战（如数据效率、算法发现）展开，为化学领域大模型的发展提供了通用的方法论框架。

**📖 中文摘要**

这篇论文探讨了如何创建持续自我改进的人工智能系统，旨在克服当前语言模型在知识获取、数据依赖和训练算法方面的局限性。论文提出了三个核心章节：1）通过合成数据方法，将小型专业语料库多样化和放大，使模型能够从有限的源材料中有效更新其参数；2）通过模型自生成合成数据来引导其基础预训练能力，减少对人类数据的依赖；3）通过在算法空间进行扩展搜索，使AI能够探索比人类研究人员手动探索更大的学习算法配置空间。虽然论文主要关注通用语言模型的自我改进，但其核心主题——利用合成数据和算法搜索来增强和扩展模型能力——与“化学大模型”的研究方向高度相关。化学大模型同样面临数据稀缺、领域知识整合和算法适应性等挑战，该论文提出的“持续自我改进AI”框架为化学领域构建能够从有限实验数据中学习、自我演化并发现新知识的专用大模型提供了重要的方法论启示和前瞻性视角。

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

满足标准1：论文的核心研究内容是系统性地评估大型语言模型在复杂工程设计任务中的能力，这直接关联到“化学大模型”主题，即如何让大模型处理化学领域的专业、多模态和需要精确推理的任务。论文的基准构建方法和评估维度为化学信息学领域类似评估提供了范本。

**📖 中文摘要**

论文提出了HWE-Bench评估框架，用于测试大型语言模型（LLMs）执行板级电路原理图设计的能力。该基准包含300个从开源平台收集的设计任务，覆盖8个应用领域，并配有一个包含2914份真实集成电路数据手册的知识库。模型的任务是根据电路功能要求和一组元件数据手册，从零开始生成原理图。生成的原理图会通过静态电气规则检查，并传递到电路模拟器以验证其动态行为。评估显示，当前顶级模型的总体通过率仅为8.15%。这项工作虽然聚焦于电子工程领域，但其核心是评估和推进LLMs在复杂、多模态（文本+结构化数据）、需要物理直觉和精确推理的专业领域任务中的能力。这种对“大模型”在高度专业化、数据密集且需要精确输出的科学工程任务中能力的系统性评估，其方法论和发现与评估“化学大模型”在类似复杂任务（如逆合成分析、反应条件预测）中的表现具有高度的相似性和参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have demonstrated significant potential in various engineering tasks, including software development, digital logic generation, and companion document maintenance. However, their ability to perform board-level circuit design is understudied, as this task requires a synergized understanding of real-world physics and Integrated Circuit (IC) datasheets, the latter comprising detailed specifications for individual components. To address this challenge, we propose \hweb, an evaluation framework that benchmarks the ability of LLMs to perform such designs. It consists of 300 board-level design tasks pulled from open-source and crowdsourcing platforms such as GitHub and OSHWLab, covering 8 application domains, and is complemented with a knowledge base of 2,914 real IC datasheets. For each task, the LLMs are tasked with generating a schematic from scratch, using the provided circuit functional requirements and a set of component datasheets as input. The resulting schematic will be checked against a static electrical rules, and then passed to a circuit simulator to verify its dynamic behavior. Our evaluation show that although current models achieve initial engineering usability and documentation understanding, they lack physical intuition, as the top-performing model achieved an overall pass rate of 8.15\%. We envision that advancements on \hweb\ will pave the way for the development of practical Electronic Design Automation (EDA) agents, revolutionizing the field of board-level design.

</details>

---

### 3. [A Survey of Neural Network Variational Monte Carlo from a Computing Workload Characterization Perspective](https://arxiv.org/abs/2603.18126)

**基本信息**

- 🔗 arXiv: [`2603.18126`](https://arxiv.org/abs/2603.18126)
- 👥 作者: Zhengze Xiao, Xuanzhe Ding, Yuyang Lou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18126.pdf)

**💡 相关性分析**

满足标准1：论文的核心是对用于科学计算（量子化学）的“大模型”（神经网络波函数拟设）进行全面的计算特征分析和优化讨论。这直接围绕“化学大模型”主题中关于模型效率、可扩展性及硬件协同设计的关键挑战。

**📖 中文摘要**

本论文从计算工作负载特征的角度，对神经网络变分蒙特卡洛（NNVMC）方法进行了综述和实证分析。NNVMC通过将变分蒙特卡洛与富有表现力的神经网络波函数拟设相结合，已成为解决量子多体问题的一种有前景的范式。论文对四种代表性的拟设（PauliNet, FermiNet, Psiformer, Orbformer）进行了统一的性能剖析，分析了模型级别的运行时和内存趋势，以及内核级别的行为（如算术强度、硬件利用率）。研究结果表明，端到端性能通常受低强度的逐元素计算和数据移动内核的限制，而计算/内存平衡在不同拟设和阶段之间存在显著差异。基于这些发现，论文讨论了可扩展NNVMC系统的算法-硬件协同设计意义。这项工作虽然聚焦于计算物理领域，但其核心是对用于科学计算的专用“大模型”（这里指大型神经网络波函数）进行深入的性能和可扩展性分析。这种对科学计算中大型神经网络模型的计算特征、瓶颈和优化策略的系统性研究，为在“化学大模型”领域（如用于分子性质预测、势能面拟合的大型模型）进行类似的性能剖析、硬件适配和效率优化提供了直接的方法论参考和宝贵的经验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Network Variational Monte Carlo (NNVMC) has emerged as a promising paradigm for solving quantum many-body problems by combining variational Monte Carlo with expressive neural-network wave-function ansätze. Although NNVMC can achieve competitive accuracy with favorable asymptotic scaling, practical deployment remains limited by high runtime and memory cost on modern graphics processing units (GPUs). Compared with language and vision workloads, NNVMC execution is shaped by physics-specific stages, including Markov-Chain Monte Carlo sampling, wave-function construction, and derivative/Laplacian evaluation, which produce heterogeneous kernel behavior and nontrivial bottlenecks. This paper provides a workload-oriented survey and empirical GPU characterization of four representative ansätze: PauliNet, FermiNet, Psiformer, and Orbformer. Using a unified profiling protocol, we analyze model-level runtime and memory trends and kernel-level behavior through family breakdown, arithmetic intensity, roofline positioning, and hardware utilization counters. The results show that end-to-end performance is often constrained by low-intensity elementwise and data-movement kernels, while the compute/memory balance varies substantially across ansätze and stages. Based on these findings, we discuss algorithm--hardware co-design implications for scalable NNVMC systems, including phase-aware scheduling, memory-centric optimization, and heterogeneous acceleration.

</details>

---

### 4. [CWoMP: Morpheme Representation Learning for Interlinear Glossing](https://arxiv.org/abs/2603.18184)

**基本信息**

- 🔗 arXiv: [`2603.18184`](https://arxiv.org/abs/2603.18184)
- 👥 作者: Morris Alper, Enora Rice, Bhargav Shandilya 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18184.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于从词形到语素序列的“结构推理”的新方法。其问题抽象（从复杂信号推断离散结构）、技术路线（对比学习、可检索词典、自回归生成）与“质谱结构推理”任务高度相关，为解决质谱到分子结构的推理问题提供了创新的方法论启示。

**📖 中文摘要**

论文提出了CWoMP（对比词-语素预训练）方法，用于语言文档中的交互线性注释（IGT）任务。与将注释视为字符序列的现有方法不同，CWoMP将语素视为具有学习表示的原子形式-意义单元。该方法通过对比训练的编码器，在共享嵌入空间中对齐上下文中的单词及其组成语素；然后，自回归解码器通过从这些嵌入的可变词典中检索条目来生成语素序列。预测结果是可解释的——基于词典条目——用户可以通过在推理时扩展词典来改进结果，而无需重新训练。论文在多种低资源语言上进行了评估，表明CWoMP在显著提高效率的同时，性能优于现有方法，在极低资源设置下表现尤其出色。这项工作虽然属于计算语言学领域，但其核心创新在于为序列到序列的“结构推理”任务（从词形推导语素序列）设计了一种新的、基于对比学习和可检索词典的表示学习方法。这种专注于从复杂输入（词形）中推断出离散的、结构化的中间表示（语素序列）的框架，与“质谱结构推理”任务（从质谱数据推断出离散的分子结构）在问题抽象层面上高度相似。因此，该论文提出的方法为质谱结构推理中如何学习鲁棒的、可解释的“子结构”表示并用于自回归生成，提供了新颖的思路和技术借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Interlinear glossed text (IGT) is a standard notation for language documentation which is linguistically rich but laborious to produce manually. Recent automated IGT methods treat glosses as character sequences, neglecting their compositional structure. We propose CWoMP (Contrastive Word-Morpheme Pretraining), which instead treats morphemes as atomic form-meaning units with learned representations. A contrastively trained encoder aligns words-in-context with their constituent morphemes in a shared embedding space; an autoregressive decoder then generates the morpheme sequence by retrieving entries from a mutable lexicon of these embeddings. Predictions are interpretable--grounded in lexicon entries--and users can improve results at inference time by expanding the lexicon without retraining. We evaluate on diverse low-resource languages, showing that CWoMP outperforms existing methods while being significantly more efficient, with particularly strong gains in extremely low-resource settings.

</details>

---

### 5. [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](https://arxiv.org/abs/2603.18256)

**基本信息**

- 🔗 arXiv: [`2603.18256`](https://arxiv.org/abs/2603.18256)
- 👥 作者: Philippe Formont, Maxime Darrin, Ismail Ben Ayed 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18256.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用推理大型语言模型进行从头分子生成，这是化学大模型在药物发现和分子设计中的一个具体应用。

**📖 中文摘要**

本文介绍了MolRGen，这是一个用于训练和评估基于推理的大型语言模型（LLMs）进行从头分子生成的大规模基准和数据集。该研究旨在弥补现有方法在从头分子生成方面的监督空白，现有方法通常依赖于已知属性修改的分子对等真实标签。MolRGen提出了一个评估和训练模型进行从头分子生成和属性预测的设置，并引入了一种新颖的多样性感知top-k分数，以捕捉生成分子的质量和多样性。研究表明，该设置可用于训练LLMs进行分子生成，例如通过强化学习训练了一个240亿参数的LLM，并对其性能和局限性进行了详细分析。这项工作直接针对化学信息学中的“化学大模型”主题，特别是利用推理LLMs进行分子设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in reasoning-based large language models (LLMs) have demonstrated substantial improvements in complex problem-solving tasks. Motivated by these advances, several works have explored the application of reasoning LLMs to drug discovery and molecular design. However, most existing approaches either focus on evaluation or rely on training setups that require ground-truth labels, such as molecule pairs with known property modifications. Such supervision is unavailable in \textit{de novo} molecular generation, where the objective is to generate novel molecules that optimize a desirability score without prior knowledge of high-scoring candidates. To bridge this gap, we introduce MolRGen, a large-scale benchmark and dataset for training and evaluating reasoning-based LLMs on \textit{de novo} molecular generation. Our contributions are threefold. First, we propose a setting to evaluate and train models for \textit{de novo} molecular generation and property prediction. Second, we introduce a novel diversity-aware top-$k$ score that captures both the quality and diversity of generated molecules. Third, we show our setting can be used to train LLMs for molecular generation, training a 24B LLM with reinforcement learning, and we provide a detailed analysis of its performance and limitations.

</details>

---

### 6. [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297)

**基本信息**

- 🔗 arXiv: [`2603.18297`](https://arxiv.org/abs/2603.18297)
- 👥 作者: Zijin Gu, Tatiana Likhomanenko, Vimal Thilak 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18297.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕从质谱数据中进行从头分子结构解析，这是“质谱结构推理”主题的核心。

**📖 中文摘要**

本文提出了FlowMS，这是首个用于谱图条件从头分子生成的离散流匹配框架。该框架通过概率空间中的迭代细化生成分子图，同时强制执行化学式约束，并以来自预训练公式Transformer编码器的谱图嵌入为条件。FlowMS在NPLIB1基准测试的6个指标中的5个上实现了最先进的性能，包括9.15%的top-1准确率（相对于DiffMS有9.7%的相对改进）和7.96的top-10 MCES（相对于MS-BART有4.2%的改进）。这项工作将离散流匹配确立为代谢组学和天然产物发现中基于质谱的结构解析的一个有前景的范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Mixture-of-Experts (MoE) architectures enable efficient scaling by activating only a subset of parameters for each input. However, conventional MoE routing selects each layer's experts independently, creating N^L possible expert paths -- for N experts across L layers. This far exceeds typical training set sizes, leading to statistical inefficiency as the model may not learn meaningful structure over such a vast path space. To constrain it, we propose \pathmoe, which shares router parameters across consecutive layers. Experiments on 0.9B and 16B parameter models demonstrate consistent improvements on perplexity and downstream tasks over independent routing, while eliminating the need for auxiliary load balancing losses. Analysis reveals that tokens following the same path naturally cluster by linguistic function, with \pathmoe{} producing more concentrated groups, better cross-layer consistency, and greater robustness to routing perturbations. These results offer a new perspective for understanding MoE architectures through the lens of expert paths.

</details>

---

### 7. [Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information](https://arxiv.org/abs/2603.18359)

**基本信息**

- 🔗 arXiv: [`2603.18359`](https://arxiv.org/abs/2603.18359)
- 👥 作者: Shih-Heng Wang, Tiantian Feng, Aditya Kommineni 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18359.pdf)

**💡 相关性分析**

满足标准3：论文包含对神经表示进行可解释性分析的重要讨论，其方法论（稀疏自编码器）与理解和分析化学大模型的内部表示这一更广泛主题相关。

**📖 中文摘要**

本文研究了神经音频编解码器（NACs）如何编码语言和副语言信息，并采用稀疏自编码器（SAEs）将密集的NAC表示分解为稀疏、可解释的激活。研究重点是一个具有挑战性的副语言属性——口音，并提出了一个量化NAC可解释性的框架。该研究评估了四种NAC模型在16种SAE配置下的表现，使用相对性能指数。结果表明，声学导向的NACs主要在稀疏表示的激活幅度中编码口音信息，而语音导向的NACs则更依赖于激活位置。这项工作通过可解释性方法（SAEs）分析音频编码模型，虽然应用领域是语音，但其方法论（使用SAEs分解和理解神经表示）与化学信息学中理解分子或光谱表示的核心挑战相关，为分析“化学大模型”的内部表示提供了潜在的工具思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented NACs encode accent information primarily in activation magnitudes of sparse representations, whereas phonetic-oriented NACs rely more on activation positions, and that low-bitrate EnCodec variants show higher interpretability.

</details>

---

### 8. [Seeking Universal Shot Language Understanding Solutions](https://arxiv.org/abs/2603.18448)

**基本信息**

- 🔗 arXiv: [`2603.18448`](https://arxiv.org/abs/2603.18448)
- 👥 作者: Haoxin Liu, Harshavardhan Kamarthi, Zhiyuan Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18448.pdf)

**💡 相关性分析**

满足标准2：论文构建了SLU-SUITE，这是一个大规模、多维度、人工标注的数据集和评估套件，专门用于镜头语言理解任务。该数据集可作为训练和评估视觉语言模型在特定领域（电影分析）性能的重要资源，与'化学大模型'主题中关注特定领域数据资源构建的方向相关。

**📖 中文摘要**

这篇论文提出了SLU-SUITE，一个用于镜头语言理解（SLU）的综合训练和评估套件。SLU是电影分析中的关键任务，但由于其多样的电影摄影维度和主观的专家判断而具有挑战性。该工作构建了一个包含49万个人工标注的问答对的数据集，涵盖33个任务和六个电影维度。论文旨在弥合通用视觉语言模型与电影专家在SLU任务上的判断差异。研究从模型和数据两个角度分析了VLM在SLU任务上的瓶颈，并提出了两种通用的SLU解决方案范式：UniShot（一个通过动态平衡数据混合训练的通用模型）和AgentShots（一个最大化各维度性能的专家集群）。这项工作为电影领域的视觉语言理解提供了重要的数据集和基准，并提出了改进模型性能的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Shot language understanding (SLU) is crucial for cinematic analysis but remains challenging due to its diverse cinematographic dimensions and subjective expert judgment. While vision-language models (VLMs) have shown strong ability in general visual understanding, recent studies reveal judgment discrepancies between VLMs and film experts on SLU tasks. To address this gap, we introduce SLU-SUITE, a comprehensive training and evaluation suite containing 490K human-annotated QA pairs across 33 tasks spanning six film-grounded dimensions. Using SLU-SUITE, we originally observe two insights into VLM-based SLU from: the model side, which diagnoses key bottlenecks of modules; the data side, which quantifies cross-dimensional influences among tasks. These findings motivate our universal SLU solutions from two complementary paradigms: UniShot, a balanced one-for-all generalist trained via dynamic-balanced data mixing, and AgentShots, a prompt-routed expert cluster that maximizes peak dimension performance. Extensive experiments show that our models outperform task-specific ensembles on in-domain tasks and surpass leading commercial VLMs by 22% on out-of-domain tasks.

</details>

---

### 9. [Cell-Type Prototype-Informed Neural Network for Gene Expression Estimation from Pathology Images](https://arxiv.org/abs/2603.18461)

**基本信息**

- 🔗 arXiv: [`2603.18461`](https://arxiv.org/abs/2603.18461)
- 👥 作者: Kazuya Nishimura, Ryoma Bise, Shinnosuke Matsuo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18461.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从病理图像预测基因表达谱的AI模型（CPNN）。这属于生物信息学/化学信息学中利用深度学习进行分子表型预测的范畴，是'化学大模型'在生物医学交叉领域的一个具体应用实例。模型整合了单细胞测序数据，旨在建立图像特征与分子表达之间的关联。

**📖 中文摘要**

这篇论文提出了一种名为细胞类型原型信息神经网络（CPNN）的新方法，用于从病理学图像中估计基因表达谱。该方法的核心创新在于利用公开可用的单细胞RNA测序数据集来引入细胞水平的表达指导。具体而言，CPNN首先从单细胞数据中估计细胞类型原型（即反映稳定基因共变关系的平均表达谱），然后直接从图像中学习细胞类型组成权重，并建模原型与观察到的批量或空间表达之间的关系。这种方法提供了一个基于生物学的、结构正则化的预测框架。论文在三个切片级数据集和三个斑块级空间转录组数据集上进行了评估，结果表明CPNN在斯皮尔曼相关性方面达到了最高性能。此外，通过可视化推断的组成权重，该框架为哪些细胞类型驱动预测的表达提供了可解释的见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Estimating slide- and patch-level gene expression profiles from pathology images enables rapid and low-cost molecular analysis with broad clinical impact. Despite strong results, existing approaches treat gene expression as a mere slide- or spot-level signal and do not incorporate the fact that the measured expression arises from the aggregation of underlying cell-level expression. To explicitly introduce this missing cell-resolved guidance, we propose a Cell-type Prototype-informed Neural Network (CPNN) that leverages publicly available single-cell RNA-sequencing datasets. Since single-cell measurements are noisy and not paired with histology images, we first estimate cell-type prototypes-mean expression profiles that reflect stable gene-gene co-variation this http URL then learns cell-type compositional weights directly from images and models the relationship between prototypes and observed bulk or spatial expression, providing a biologically grounded and structurally regularized prediction framework. We evaluate CPNN on three slide-level datasets and three patch-level spatial transcriptomics datasets. Across all settings, CPNN achieves the highest performance in terms of Spearman correlation. Moreover, by visualizing the inferred compositional weights, our framework provides interpretable insights into which cell types drive the predicted expression. Code is publicly available at this https URL .

</details>

---

### 10. [A Faster Deterministic Algorithm for Kidney Exchange via Representative Set](https://arxiv.org/abs/2603.18471)

**基本信息**

- 🔗 arXiv: [`2603.18471`](https://arxiv.org/abs/2603.18471)
- 👥 作者: Kangyi Tian, Mingyu Xiao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18471.pdf)

**💡 相关性分析**

满足标准2：论文提出了CAPSUL基准，这是一个整合了蛋白质3D结构信息和详细亚细胞定位注释的综合数据集。该数据集专门设计用于推动基于结构的AI模型在蛋白质功能预测（亚细胞定位）任务上的发展，为'化学大模型'（特别是面向生物大分子的模型）的训练和评估提供了重要的数据资源。

**📖 中文摘要**

这篇论文介绍了CAPSUL，一个用于蛋白质亚细胞定位的综合人类蛋白质基准数据集。亚细胞定位是药物靶点识别和功能注释的关键生物学任务。作者指出，现有的数据集缺乏全面的3D结构信息以及详细的亚细胞定位注释，这严重阻碍了有前景的基于结构的模型在此任务上的应用。为了填补这一空白，CAPSUL整合了多样化的3D结构表示与由领域专家精心策划的细粒度亚细胞定位注释。论文使用多种最先进的基于序列和基于结构的模型对该基准进行了评估，展示了在此任务中引入结构特征的重要性。此外，论文还探索了重加权和单标签分类策略，以促进未来基于结构的方法在此任务上的研究。最后，通过一个关于高尔基体的案例研究，展示了基于结构的方法强大的可解释性潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Kidney Exchange Problem is a prominent challenge in healthcare and economics, arising in the context of organ transplantation. It has been extensively studied in artificial intelligence and optimization. In a kidney exchange, a set of donor-recipient pairs and altruistic donors are considered, with the goal of identifying a sequence of exchange -- comprising cycles or chains starting from altruistic donors -- such that each donor provides a kidney to the compatible recipient in the next donor-recipient pair. Due to constraints in medical resources, some limits are often imposed on the lengths of these cycles and chains. These exchanges create a network of transplants aimed at maximizing the total number, $t$, of successful transplants. Recently, this problem was deterministically solved in $O^*(14.34^t)$ time (IJCAI 2024). In this paper, we introduce the representative set technique for the Kidney Exchange Problem, showing that the problem can be deterministically solved in $O^*(6.855^t)$ time.

</details>

---

### 11. [Leveraging Large Language Models for Generalizing Peephole Optimizations](https://arxiv.org/abs/2603.18477)

**基本信息**

- 🔗 arXiv: [`2603.18477`](https://arxiv.org/abs/2603.18477)
- 👥 作者: Chunhao Liao, Hongxu Xu, Xintong Zhou 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18477.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大型语言模型（LLM）来自动化编译器优化规则的泛化过程。这直接涉及'化学大模型'主题的一个延伸应用，即利用大语言模型的推理和代码生成能力来解决程序优化这一特定领域的复杂问题，展示了AI大模型在非自然语言处理领域的应用潜力。

**📖 中文摘要**

这篇论文提出了LPG（大型语言模型辅助的窥孔优化泛化）框架，该框架利用大型语言模型来泛化编译器中的窥孔优化。窥孔优化通过将特定指令重写为语义等效但更高效的形式来提升性能。将具体的优化实例提升为更通用的、能匹配更广泛指令模式的重写规则是关键但困难的一步。LPG的设计基于观察到LLMs在语义抽象和探索性推理方面有效，而形式分析对于确保生成的规则正确且有利是必要的。LPG采用了一个闭环工作流程，集成了LLM驱动的符号常量泛化、结构泛化、约束松弛和位宽/精度泛化，并辅以语法验证、语义验证和盈利性检查的反馈。论文在从LLVM生态系统中提取的真实世界窥孔优化问题上评估了LPG，结果显示LPG成功泛化了102个优化中的90个。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Peephole optimizations are a core component of modern optimizing compilers. It rewrites specific instruction into semantically equivalent but more efficient forms. In practice, creating a new peephole optimization often starts from a concrete optimization instance and requires lifting it into a more general rewrite rule that matches a wider range of instruction patterns. This generalization step is critical to optimization effectiveness, but it is also difficult: producing rules that are both correct and sufficiently general typically demands substantial manual effort and domain expertise. Existing approaches such as Hydra attempt to automate this task with program synthesis, but their generalization capability is often limited by search-space explosion, under-generalization, and restricted support for diverse instruction domains. We present LPG, large language model aided peephole optimization generalization, a framework that uses large language models (LLMs) to generalize peephole optimizations. The design of LPG is motivated by the observation that LLMs are effective at semantic abstraction and exploratory reasoning, while formal analyses are necessary to ensure that generated rules are sound and profitable. Based on this observation, LPG adopts a closed-loop workflow that integrates LLM-driven symbolic constant generalization, structural generalization, constraint relaxation, and bitwidth/precision generalization with feedback from syntactic validation, semantic verification, and profitability checking. We evaluate LPG on real-world peephole optimization issues drawn from the LLVM ecosystem. Overall, LPG successfully generalizes 90 out of 102 optimizations. On the integer-focused subset that is directly comparable to Hydra, LPG generalizes 74 out of 81 optimizations, whereas Hydra generalizes 35.

</details>

---

### 12. [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505)

**基本信息**

- 🔗 arXiv: [`2603.18505`](https://arxiv.org/abs/2603.18505)
- 👥 作者: Jingzhi Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18505.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于AI在蛋白质科学中演变的综合性综述，涵盖了从静态结构预测到生成动态构象和复杂相互作用的多个前沿方向。它详细讨论了生成模型（如扩散模型）在蛋白质结构生成中的应用，以及多模态表示学习，这些内容与'化学大模型'和'质谱结构推理'（作为分子结构解析的一种方式）高度相关，提供了该领域重要的现状总结和未来展望。

**📖 中文摘要**

这篇论文是一篇综述，系统性地审视了人工智能驱动的蛋白质科学在五个相互关联维度上的范式转变：1）整合序列、几何和文本知识的统一多模态表示；2）通过无MSA架构和全原子复合物建模改进静态预测；3）包括扩散模型和流匹配在内的生成框架，以捕获与热力学系综一致的构象分布；4）跨越蛋白质-配体、蛋白质-核酸和蛋白质-蛋白质复合物的异质相互作用预测；5）适应度景观、突变效应和文本引导属性预测的功能推断。论文批判性地分析了当前的瓶颈，并指出了未来方向，包括物理一致的生成模型、多模态基础架构和实验闭环系统。这篇综述标志着人工智能从结构分析工具向能够理解和最终重写生命动态语言的通用模拟器的转变。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular interactions. This review systematically examines the paradigm shift in AI driven protein science across five interconnected dimensions: unified multimodal representations that integrate sequences, geometries, and textual knowledge; refinement of static prediction through MSA free architectures and all atom complex modeling; generative frameworks, including diffusion models and flow matching, that capture conformational distributions consistent with thermodynamic ensembles; prediction of heterogeneous interactions spanning protein ligand, protein nucleic acid, and protein protein complexes; and functional inference of fitness landscapes, mutational effects, and text guided property prediction. We critically analyze current bottlenecks, including data distribution biases, limited mechanistic interpretability, and the disconnect between geometric metrics and biophysical reality, while identifying future directions toward physically consistent generative models, multimodal foundation architectures, and experimental closed loop systems. This methodological transformation marks artificial intelligence's transition from a structural analysis tool into a universal simulator capable of understanding and ultimately rewriting the dynamic language of life.

</details>

---

### 13. [SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks](https://arxiv.org/abs/2603.18548)

**基本信息**

- 🔗 arXiv: [`2603.18548`](https://arxiv.org/abs/2603.18548)
- 👥 作者: Amanda A. Howard, Nicholas Zolman, Bruno Jacob 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18548.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发SINDy-KANs，一种结合了可解释KAN网络和稀疏方程发现（SINDy）的新方法，用于从数据中识别非线性动力学方程。这属于科学发现AI的范畴，与'化学大模型'主题中利用AI模型从复杂数据（如化学反应动力学数据）中提取可解释的物理规律或模型的目标高度相关。

**📖 中文摘要**

这篇论文提出了SINDy-KANs方法，将稀疏识别非线性动力学（SINDy）与Kolmogorov-Arnold网络（KANs）相结合。KANs作为一种增强机器学习可解释性的潜在方式出现，但KANs学习到的解不一定具有可解释性（即稀疏或简约）。SINDy是一种互补的方法，允许从数据中学习动力学系统的稀疏方程；然而，学习的方程受限于预设的基函数库。SINDy-KANs同时训练一个KAN和一个类似SINDy的表征，通过在每个激活函数级别应用SINDy来增加KAN表征的可解释性，同时保持通过深度KANs可能实现的函数组合能力。作者将该方法应用于一系列符号回归任务，包括动力学系统，以展示其在各种系统中准确的方程发现能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method to a number of symbolic regression tasks, including dynamical systems, to show accurate equation discovery across a range of systems.

</details>

---

### 14. [Elastic Weight Consolidation Done Right for Continual Learning](https://arxiv.org/abs/2603.18596)

**基本信息**

- 🔗 arXiv: [`2603.18596`](https://arxiv.org/abs/2603.18596)
- 👥 作者: Xuan Liu, Xiaobin Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18596.pdf)

**💡 相关性分析**

满足标准1：论文提出的Logits Reversal（LR）操作是一种改进模型训练和微调的通用方法。虽然论文背景是持续学习，但该方法论的核心——通过修正梯度计算来更准确地评估参数重要性并防止性能退化——可以迁移并应用于训练和优化化学领域的大型基础模型（化学大模型），以整合多源数据或适应新任务，因此与“化学大模型”这一核心主题在方法论层面相关。

**📖 中文摘要**

本文系统分析了持续学习中权重正则化方法，特别是弹性权重巩固（EWC）及其变体。虽然论文本身不直接研究化学大模型或质谱结构推理，但其核心贡献——Logits Reversal（LR）操作——是一种用于改进模型权重重要性估计的通用方法。该方法通过修正Fisher信息矩阵（FIM）的计算来防止梯度消失和冗余保护，从而提升模型在持续学习任务中的性能。这种改进模型训练稳定性和权重重要性评估的通用技术，原则上可以应用于训练和微调化学领域的大模型（例如，用于分子性质预测或质谱数据解释的模型），以缓解灾难性遗忘并更好地整合来自不同数据集或任务的知识。因此，该论文提供了一种可能有助于构建和优化“化学大模型”的工具或方法论见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight regularization methods in continual learning (CL) alleviate catastrophic forgetting by assessing and penalizing changes to important model weights. Elastic Weight Consolidation (EWC) is a foundational and widely used approach within this framework that estimates weight importance based on gradients. However, it has consistently shown suboptimal performance. In this paper, we conduct a systematic analysis of importance estimation in EWC from a gradient-based perspective. For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios. Our analysis also reveals that Memory Aware Synapses (MAS), a variant of EWC, imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection. Consequently, both EWC and its variants exhibit fundamental misalignments in estimating weight importance, leading to inferior performance. To tackle these issues, we propose the Logits Reversal (LR) operation, a simple yet effective modification that rectifies EWC's importance estimation. Specifically, reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection. Extensive experiments across various CL tasks and datasets show that the proposed method significantly outperforms existing EWC and its variants. Therefore, we refer to it as EWC Done Right (EWC-DR).

</details>

---

### 15. [STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation](https://arxiv.org/abs/2603.18688)

**基本信息**

- 🔗 arXiv: [`2603.18688`](https://arxiv.org/abs/2603.18688)
- 👥 作者: Chen Zhang, Liwei Liu, Jun Tao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18688.pdf)

**💡 相关性分析**

满足标准1：论文提出的STEP框架旨在为稀疏、异构的科学时间序列构建统一的表示学习模型。这一范式与构建针对特定科学领域（如化学信息学）的大模型高度相关。质谱数据作为一种典型的科学时间序列，其分析可以借鉴该框架中处理数据挑战和整合多源预训练知识的思想，因此与“化学大模型”和“质谱结构推理”的核心主题在方法论上相关。

**📖 中文摘要**

本文针对科学时间序列数据（通常具有稀疏、异构和小规模的特点）提出了一种统一的表示学习框架STEP。该框架通过跨领域蒸馏，整合了来自音频、通用时间序列和脑信号等相关领域的预训练基础模型的知识，以学习适用于科学信号的通用且可迁移的特征。论文的核心创新包括自适应分块处理、统计补偿方案以及利用多个基础模型进行知识融合的跨领域蒸馏。虽然论文主要关注科学时间序列（如金融、供应链、能源规划等），但其提出的“通过整合多个相关领域预训练模型的知识来构建一个针对特定领域（此处为科学时间序列）的统一编码器”这一范式，与构建“化学大模型”的思路有相通之处。化学信息学中的质谱数据本质上也是一种复杂的、具有特定领域知识的科学时间序列/信号数据。STEP框架中处理数据稀疏性、异构性和利用外部知识的方法，可以为构建用于质谱数据分析的专用大模型或表示学习模型提供方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientific tasks and their complementary strengths. Based on this observation, we propose STEP, a Scientific Time Series Encoder Pretraining framework via cross domain distillation. STEP introduces adaptive patching to handle extreme-length sequences and a statistics compensation scheme to accommodate diverse numerical scales. It further leverages cross-domain distillation to integrate knowledge from multiple foundation models into a unified encoder. By combining complementary representations across different domains, STEP learns general-purpose and transferable features tailored for scientific signals. Experiments on seven scientific time series tasks demonstrate that STEP provides both an effective structure and an effective pretraining paradigm, taking a STEP toward scientific time series representation learning.

</details>

---

### 16. [CausalRM: Causal-Theoretic Reward Modeling for RLHF from Observational User Feedbacks](https://arxiv.org/abs/2603.18736)

**基本信息**

- 🔗 arXiv: [`2603.18736`](https://arxiv.org/abs/2603.18736)
- 👥 作者: Hao Wang, Licheng Pan, Zhichao Chen 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18736.pdf)

**💡 相关性分析**

满足标准1：论文提出的CausalRM框架解决了从有噪声和偏差的观察数据中学习鲁棒奖励模型的核心问题。该方法论可以迁移到化学信息学和质谱分析领域，用于从非完美的、观察性的化学或质谱数据中学习训练信号，从而辅助构建或优化用于分子性质预测、质谱解析等任务的“化学大模型”或推理模型，因此与核心主题相关。

**📖 中文摘要**

本文提出了CausalRM，一个基于因果理论的奖励建模框架，用于从观察性用户反馈（如点击、复制、点赞）中学习无偏的奖励模型，以替代强化学习从人类反馈中学习（RLHF）中昂贵且受控的实验性反馈数据。CausalRM通过显式建模标注错误生成过程来处理观察性反馈的噪声，并利用倾向得分来重新加权训练样本以消除用户偏好偏差。该框架旨在学习准确的奖励信号，以用于下游的RLHF任务。虽然论文的应用背景是通用语言模型的对齐，但其核心方法——从有噪声、有偏差的观察数据中学习鲁棒且无偏的奖励模型——具有高度的通用性。在化学信息学和质谱分析领域，专家标注（如将质谱图与分子结构关联）成本高昂且可能带有主观偏差。CausalRM提供了一种方法论，有可能用于从历史实验数据、文献中的关联或众包注释等观察性来源中学习用于训练“化学大模型”或“质谱结构推理模型”的奖励或监督信号，从而降低对完美标注数据的依赖。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite the success of reinforcement learning from human feedback (RLHF) in aligning language models, current reward modeling heavily relies on experimental feedback data collected from human annotators under controlled and costly conditions. In this work, we introduce observational reward modeling -- learning reward models with observational user feedback (e.g., clicks, copies, and upvotes) -- as a scalable and cost-effective alternative. We identify two fundamental challenges in this setting: (1) observational feedback is noisy due to annotation errors, which deviates it from true user preference; (2) observational feedback is biased by user preference, where users preferentially provide feedback on responses they feel strongly about, which creats a distribution shift between training and inference data. To address these challenges, we propose CausalRM, a causal-theoretic reward modeling framework that aims to learn unbiased reward models from observational feedback. To tackle challenge (1), CausalRM introduces a noise-aware surrogate loss term that is provably equivalent to the primal loss under noise-free conditions by explicitly modeling the annotation error generation process. To tackle challenge (2), CausalRM uses propensity scores -- the probability of a user providing feedback for a given response -- to reweight training samples, yielding a loss function that eliminates user preference bias. Extensive experiments across diverse LLM backbones and benchmark datasets validate that CausalRM effectively learns accurate reward signals from noisy and biased observational feedback and delivers substantial performance improvements on downstream RLHF tasks -- including a 49.2% gain on WildGuardMix and a 32.7% improvement on HarmBench. Code is available on our project website.

</details>

---

### 17. [dTRPO: Trajectory Reduction in Policy Optimization of Diffusion Large Language Models](https://arxiv.org/abs/2603.18806)

**基本信息**

- 🔗 arXiv: [`2603.18806`](https://arxiv.org/abs/2603.18806)
- 👥 作者: Wenxuan Zhang, Lemeng Wu, Changsheng Zhao 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”主题，专注于改进扩散大语言模型（dLLMs）的策略优化，这是一种特定类型的大模型。

**📖 中文摘要**

本文提出了一种名为dTRPO（轨迹缩减策略优化）的新方法，旨在改进扩散大语言模型（dLLMs）的策略优化。dLLMs是一种用于语言生成的新范式，其对齐人类偏好面临挑战。dTRPO的核心是通过减少轨迹概率计算成本来扩展离线策略训练。作者证明，在参考策略正则化下，新解掩码标记的概率比是中间扩散状态概率比的无偏估计，并且完整轨迹的概率可以通过对重新掩码的最终状态进行单次前向传递来有效估计。通过将这两种轨迹缩减策略整合到策略优化目标中，dTRPO在指令跟随和推理基准测试中显著提升了7B dLLMs的核心性能，在STEM任务上提升高达9.6%，在代码任务上提升高达4.3%，在指令跟随任务上提升高达3.0%。此外，由于其离线和单次前向的特性，dTRPO展现出强大的训练效率，并通过高质量输出提高了生成效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion Large Language Models (dLLMs) introduce a new paradigm for language generation, which in turn presents new challenges for aligning them with human preferences. In this work, we aim to improve the policy optimization for dLLMs by reducing the cost of the trajectory probability calculation, thereby enabling scaled-up offline policy training. We prove that: (i) under reference policy regularization, the probability ratio of the newly unmasked tokens is an unbiased estimate of that of intermediate diffusion states, and (ii) the probability of the full trajectory can be effectively estimated with a single forward pass of a re-masked final state. By integrating these two trajectory reduction strategies into a policy optimization objective, we propose Trajectory Reduction Policy Optimization (dTRPO). We evaluate dTRPO on 7B dLLMs across instruction-following and reasoning benchmarks. Results show that it substantially improves the core performance of state-of-the-art dLLMs, achieving gains of up to 9.6% on STEM tasks, up to 4.3% on coding tasks, and up to 3.0% on instruction-following tasks. Moreover, dTRPO exhibits strong training efficiency due to its offline, single-forward nature, and achieves improved generation efficiency through high-quality outputs.

</details>

---

### 18. [Seasoning Generative Models for a Generalization Aftertaste](https://arxiv.org/abs/2603.18817)

**基本信息**

- 🔗 arXiv: [`2603.18817`](https://arxiv.org/abs/2603.18817)
- 👥 作者: Hisham Husain, Valentin De Bortoli, Richard Nock
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18817.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”主题，深入探讨了生成模型（包括扩散模型）的泛化理论，这是构建和理解化学领域大模型的基础。

**📖 中文摘要**

本文探讨了使用判别器来训练或微调生成模型（如GANs和扩散模型）的框架。作者扩展了一个与f-散度相关的强对偶性结果，从而产生了一个判别器引导的“精炼”方法，该方法可以应用于任何生成模型。理论分析表明，经过精炼的生成模型相比其未精炼的对应物，能够可证明地改善泛化能力，其泛化差距的改进基于用于精炼的判别器集合的Rademacher复杂度。该工作为现有的基于分数的扩散方法（Kim等人，2022）提供了理论验证，并有助于更广泛地理解生成模型的泛化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The use of discriminators to train or fine-tune generative models has proven to be a rather successful framework. A notable example is Generative Adversarial Networks (GANs) that minimize a loss incurred by training discriminators along with other paradigms that boost generative models via discriminators that satisfy weak learner constraints. More recently, even diffusion models have shown advantages with some kind of discriminator guidance. In this work, we extend a strong-duality result related to $f$-divergences which gives rise to a discriminator-guided recipe that allows us to \textit{refine} any generative model. We then show that the refined generative models provably improve generalization, compared to its non-refined counterpart. In particular, our analysis reveals that the gap in generalization is improved based on the Rademacher complexity of the discriminator set used for refinement. Our recipe subsumes a recently introduced score-based diffusion approach (Kim et al., 2022) that has shown great empirical success, however allows us to shed light on the generalization guarantees of this method by virtue of our analysis. Thus, our work provides a theoretical validation for existing work, suggests avenues for new algorithms, and contributes to our understanding of generalization in generative models at large.

</details>

---

### 19. [Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827)

**基本信息**

- 🔗 arXiv: [`2603.18827`](https://arxiv.org/abs/2603.18827)
- 👥 作者: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18827.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”的广义主题（即人工智能大模型）的社会影响和伦理维度展开讨论。

**📖 中文摘要**

本文从性别视角调查了学生对人工智能伦理和社会影响的看法，探讨了可能对未来人工智能教学方式产生重大影响的概念。通过对230名计算机科学专业大二学生进行问卷调查，结果显示学生普遍认为AI将对日常生活产生显著影响，特别是在医学、教育或媒体等领域。研究揭示了男性和女性在认知AI潜在变化和威胁方面的差异。虽然论文主题是AI伦理教育，但其核心研究对象是学生对“人工智能”这一大模型/大技术范式的看法和预期影响。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An investigation, from a gender perspective, of how students view the ethical implications and societal effects of artificial intelligence is conducted, examining concepts that could have a big influence on how artificial intelligence may be taught in the future. For this, we conducted a survey on a cohort of 230 second year computer science students to reveal their opinions. The results revealed that AI, from the students' perspective, will significantly impact daily life, particularly in areas such as medicine, education, or media. Men are more aware of potential changes in Computer Science, autonomous driving, image and video processing, and chatbot usage, while women mention more the impact on social media. Both men and women perceive potential threats in the same manner, with men more aware of war, AI controlled drones, terrain recognition, and information war. Women seem to have a stronger tendency towards ethical considerations and helping others.

</details>

---

### 20. [Statistical Characteristic-Guided Denoising for Rapid High-Resolution Transmission Electron Microscopy Imaging](https://arxiv.org/abs/2603.18834)

**基本信息**

- 🔗 arXiv: [`2603.18834`](https://arxiv.org/abs/2603.18834)
- 👥 作者: Hesong Li, Ziqi Wu, Ruiwen Shao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18834.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门针对高分辨率透射电子显微镜（HRTEM）成像的去噪方法和生成的数据集。HRTEM是材料科学和化学中用于原子尺度观测的关键工具，其高质量图像数据对于后续的化学结构分析和推理至关重要。因此，该工作提供的去噪方法和数据集是“质谱结构推理”相关领域（同为分析科学）的重要数据预处理工具和资源。

**📖 中文摘要**

本文提出了一种统计特征引导的去噪网络，用于快速高分辨率透射电子显微镜（HRTEM）成像。HRTEM能够实现原子尺度的成核动力学观测，但由于成核过程的快速变化需要短曝光快速成像，导致严重噪声。该方法利用统计特征在空间域和频域引导去噪过程：在空间域，基于偏差特征选择适当的卷积操作；在频域，基于频带特征增强信号并抑制噪声。此外，作者还开发了一种HRTEM特定的噪声校准方法，并生成了一个包含无序结构和真实HRTEM图像噪声的数据集，以确保模型在真实图像上的去噪性能。实验表明，该方法在HRTEM图像去噪方面优于现有技术，并在定位下游任务中有效。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

High-Resolution Transmission Electron Microscopy (HRTEM) enables atomic-scale observation of nucleation dynamics, which boosts the studies of advanced solid materials. Nonetheless, due to the millisecond-scale rapid change of nucleation, it requires short-exposure rapid imaging, leading to severe noise that obscures atomic positions. In this work, we propose a statistical characteristic-guided denoising network, which utilizes statistical characteristics to guide the denoising process in both spatial and frequency domains. In the spatial domain, we present spatial deviation-guided weighting to select appropriate convolution operations for each spatial position based on deviation characteristic. In the frequency domain, we present frequency band-guided weighting to enhance signals and suppress noise based on band characteristics. We also develop an HRTEM-specific noise calibration method and generate a dataset with disordered structures and realistic HRTEM image noises. It can ensure the denoising performance of models on real images for nucleation observation. Experiments on synthetic and real data show our method outperforms the state-of-the-art methods in HRTEM image denoising, with effectiveness in the localization downstream task. Code will be available at this https URL .

</details>

---

### 21. [Pore-scale modeling of capillary-driven binder migration during battery electrode drying](https://arxiv.org/abs/2603.18860)

**基本信息**

- 🔗 arXiv: [`2603.18860`](https://arxiv.org/abs/2603.18860)
- 👥 作者: Marcel Weichel, Martin Reder, Gerit Mühlberg 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18860.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是电池电极材料制造过程的物理化学建模，这属于化学信息学和计算化学的范畴。虽然不直接涉及大模型或质谱，但其对多物理场过程的精细模拟与化学信息学中利用计算模型理解和优化化学过程的目标高度一致。

**📖 中文摘要**

本文提出了一个空间分辨的孔隙尺度连续介质模型，用于模拟钠离子电池硬碳电极干燥过程中的毛细管驱动粘结剂迁移。电极干燥是制造过程中的关键步骤，因为孔隙排空期间的粘结剂迁移会影响电极的机械完整性和电性能。现有建模方法主要依赖薄膜收缩阶段的一维方式或忽略毛细管传输，导致缺乏物理一致的、基于微观结构的粘结剂迁移预测。该模型扩展了现有框架，明确描述了孔隙排空过程中毛细管驱动的粘结剂传输，并将其应用于具有不同平均粒径的硬碳微观结构。模拟揭示了颗粒尺寸、蒸发速率和表面张力等因素对粘结剂分布均匀性的影响。研究表明，明确描述毛细管传输和微观结构效应对于准确预测粘结剂迁移至关重要，为优化电极干燥工艺提供了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sodium-ion batteries employing hard carbon electrodes are considered a drop-in technology for lithium-ion batteries. Electrode drying is a critical manufacturing step, as binder migration during pore emptying impacts the mechanical integrity and electrical performance of the electrode. Existing modeling approaches predominantly rely on the film shrinkage phase in a one dimensional way or neglect the capillary transport, resulting in a lack of physically consistent microstructure resolved predictions of binder migration. In this work, a spatially resolved pore scale continuum model is extended to explicitly describe capillary driven binder transport during pore emptying. The model is applied to hard carbon microstructures with varying mean particle diameters. The simulations reveal that smaller particle sizes lead to a more homogeneous binder distribution, whereas higher evaporation rates and increased surface tension promote stronger binder gradients. Variations in solvent viscosity show only a minor influence on binder migration, as long as no hydrophilic or hydrophobic behavior is present. Finally, the simulations demonstrate that an explicit description of capillary transport and microstructural effects is essential for accurately predicting binder migration and provides a basis for the targeted optimization of electrode drying processes.

</details>

---

### 22. [RadioDiff-FS: Physics-Informed Manifold Alignment in Few-Shot Diffusion Models for High-Fidelity Radio Map Construction](https://arxiv.org/abs/2603.18865)

**基本信息**

- 🔗 arXiv: [`2603.18865`](https://arxiv.org/abs/2603.18865)
- 👥 作者: Xiucheng Wang, Zixuan Guo, Nan Cheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18865.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕扩散模型（一种重要的生成式大模型）的领域自适应方法。虽然应用场景是无线通信，但其提出的少样本扩散框架、理论分解和方向一致性损失等方法论，对于其他科学领域（如化学）中利用扩散模型进行数据生成或推理具有重要的参考价值。

**📖 中文摘要**

本文提出了RadioDiff-FS，一个少样本扩散框架，用于将预训练的主路径生成器适配到多径丰富的目标域，仅需少量高保真样本。该适配基于一个理论分解：将多径无线电地图分解为主导的主路径分量和方向稀疏的残差。该分解表明跨域偏移对应于一个有界的、几何结构化的特征平移，而非任意的分布变化。作者引入了方向一致性损失（DCL）来约束扩散分数更新沿着物理上合理的传播方向，抑制低数据状态下出现的相位不一致伪影。实验表明，RadioDiff-FS在静态和动态无线电地图上的归一化均方误差相比原始扩散基线分别降低了59.5%和74.0%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Radio maps (RMs) provide spatially continuous propagation characterizations essential for 6G network planning, but high-fidelity RM construction remains challenging. Rigorous electromagnetic solvers incur prohibitive computational latency, while data-driven models demand massive labeled datasets and generalize poorly from simplified simulations to complex multipath environments. This paper proposes RadioDiff-FS, a few-shot diffusion framework that adapts a pre-trained main-path generator to multipath-rich target domains with only a small number of high-fidelity samples. The adaptation is grounded in a theoretical decomposition of the multipath RM into a dominant main-path component and a directionally sparse residual. This decomposition shows that the cross-domain shift corresponds to a bounded and geometrically structured feature translation rather than an arbitrary distribution change. A Direction-Consistency Loss (DCL) is then introduced to constrain diffusion score updates along physically plausible propagation directions, suppressing phase-inconsistent artifacts that arise in the low-data regime. Experiments show that RadioDiff-FS reduces NMSE by 59.5% on static RMs and by 74.0% on dynamic RMs relative to the vanilla diffusion baseline, achieving an SSIM of 0.9752 and a PSNR of 36.37 dB under severely limited supervision.

</details>

---

### 23. [Neural Galerkin Normalizing Flow for Transition Probability Density Functions of Diffusion Models](https://arxiv.org/abs/2603.18907)

**基本信息**

- 🔗 arXiv: [`2603.18907`](https://arxiv.org/abs/2603.18907)
- 👥 作者: Riccardo Saporiti, Fabio Nobile
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18907.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用归一化流（一种生成模型）和神经伽辽金方法来解决与扩散过程相关的概率密度函数近似问题。这直接涉及生成模型在科学计算中的应用，与“化学大模型”中利用生成模型模拟化学动力学或分子扩散过程的研究主题相关。

**📖 中文摘要**

本文提出了一个新的神经伽辽金归一化流框架，用于通过求解相应的福克-普朗克方程来近似扩散过程的转移概率密度函数，并以初始质量位置为参数。通过使用归一化流，我们将解寻找为参考随机过程转移概率密度函数的变换，确保我们的近似是结构保持的，并自动满足正性和质量守恒约束。通过将神经伽辽金方案扩展到归一化流的背景中，我们推导了归一化流参数时间演化的常微分方程组。自适应采样例程用于在有意义的位置评估福克-普朗克残差，这对于处理高维偏微分方程至关重要。数值结果表明，该策略捕捉了真实解的关键特征，并强制执行了初始数据与后续时间密度函数之间的因果关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a new Neural Galerkin Normalizing Flow framework to approximate the transition probability density function of a diffusion process by solving the corresponding Fokker-Planck equation with an atomic initial distribution, parametrically with respect to the location of the initial mass. By using Normalizing Flows, we look for the solution as a transformation of the transition probability density function of a reference stochastic process, ensuring that our approximation is structure-preserving and automatically satisfies positivity and mass conservation constraints. By extending Neural Galerkin schemes to the context of Normalizing Flows, we derive a system of ODEs for the time evolution of the Normalizing Flow's parameters. Adaptive sampling routines are used to evaluate the Fokker-Planck residual in meaningful locations, which is of vital importance to address high-dimensional PDEs. Numerical results show that this strategy captures key features of the true solution and enforces the causal relationship between the initial datum and the density function at subsequent times. After completing an offline training phase, online evaluation becomes significantly more cost-effective than solving the PDE from scratch. The proposed method serves as a promising surrogate model, which could be deployed in many-query problems associated with stochastic differential equations, like Bayesian inference, simulation, and diffusion bridge generation.

</details>

---

### 24. [BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery](https://arxiv.org/abs/2603.18957)

**基本信息**

- 🔗 arXiv: [`2603.18957`](https://arxiv.org/abs/2603.18957)
- 👥 作者: Sijian Fan, Liyan Xiong, Dayuan Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18957.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发一种新的贝叶斯模型（BVSIMC）用于药物发现中的关联预测，这属于化学信息学和计算药物设计的核心领域。同时，该方法被应用于两个具体的药物发现任务（耐药性预测和药物重定位），并揭示了有意义的特征，这提供了可用于相关主题（如化学大模型的数据分析或质谱数据的多组学整合）的方法论和潜在数据洞察资源。

**📖 中文摘要**

本文提出了BVSIMC（贝叶斯变量选择引导的归纳矩阵补全），一种新的贝叶斯模型，用于在药物发现中从侧边特征进行变量选择。通过学习稀疏的潜在嵌入，BVSIMC提高了预测准确性和可解释性。作者通过模拟研究和两个药物发现应用验证了该方法：1) 预测结核分枝杆菌的耐药性，2) 预测计算药物重定位中的新药物-疾病关联。在合成数据和真实数据上，BVSIMC在预测方面优于其他几种最先进的方法。在两个真实例子中，BVSIMC进一步揭示了最具临床意义的侧边特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in drug discovery have demonstrated that incorporating side information (e.g., chemical properties about drugs and genomic information about diseases) often greatly improves prediction performance. However, these side features can vary widely in relevance and are often noisy and high-dimensional. We propose Bayesian Variable Selection-Guided Inductive Matrix Completion (BVSIMC), a new Bayesian model that enables variable selection from side features in drug discovery. By learning sparse latent embeddings, BVSIMC improves both predictive accuracy and interpretability. We validate our method through simulation studies and two drug discovery applications: 1) prediction of drug resistance in Mycobacterium tuberculosis, and 2) prediction of new drug-disease associations in computational drug repositioning. On both synthetic and real data, BVSIMC outperforms several other state-of-the-art methods in terms of prediction. In our two real examples, BVSIMC further reveals the most clinically meaningful side features.

</details>

---

### 25. [Foundations of Schrödinger Bridges for Generative Modeling](https://arxiv.org/abs/2603.18992)

**基本信息**

- 🔗 arXiv: [`2603.18992`](https://arxiv.org/abs/2603.18992)
- 👥 作者: Sophia Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18992.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于薛定谔桥的专题指南/综述，薛定谔桥是扩散模型等生成式大模型背后的统一数学框架。该工作系统性地阐述了该主题的数学基础，并将其与现代生成建模联系起来，属于对“化学大模型”底层核心技术的深入综述和展望。

**📖 中文摘要**

本文系统性地阐述了薛定谔桥问题的数学基础，该问题构成了现代生成建模框架（包括扩散模型、基于分数的模型和流匹配）的核心统一原理。薛定谔桥将生成任务框架化为在边际分布约束下确定一个最优的随机桥，该桥与预定义的参考过程具有最小熵偏差。本指南从最优传输、随机控制和路径空间优化中汲取知识，发展了薛定谔桥问题的数学基础，并侧重于其与现代生成建模直接相关的动态公式。作者为从第一性原理构建薛定谔桥建立了一个全面的工具包，并展示了这些构造如何产生广义的和特定于任务的计算方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

At the core of modern generative modeling frameworks, including diffusion models, score-based models, and flow matching, is the task of transforming a simple prior distribution into a complex target distribution through stochastic paths in probability space. Schrödinger bridges provide a unifying principle underlying these approaches, framing the problem as determining an optimal stochastic bridge between marginal distribution constraints with minimal-entropy deviations from a pre-defined reference process. This guide develops the mathematical foundations of the Schrödinger bridge problem, drawing on optimal transport, stochastic control, and path-space optimization, and focuses on its dynamic formulation with direct connections to modern generative modeling. We build a comprehensive toolkit for constructing Schrödinger bridges from first principles, and show how these constructions give rise to generalized and task-specific computational methods.

</details>

---

### 26. [SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141)

**基本信息**

- 🔗 arXiv: [`2603.19141`](https://arxiv.org/abs/2603.19141)
- 👥 作者: Mingxing Zhang, Nicola Rossberg, Simone Innocente 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19141.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于光谱数据分析的可解释机器学习框架（SHAPCA），这为化学信息学领域（特别是光谱分析）提供了可用于模型解释和特征分析的工具和方法。

**📖 中文摘要**

本文提出SHAPCA，一个用于光谱数据的可解释机器学习流程。该流程结合了主成分分析（PCA）进行降维和SHAP（Shapley Additive exPlanations）进行事后解释，旨在为化学和生物医学分析中的光谱数据集提供稳定、一致且可解释的模型预测解释。光谱数据具有高维度和强共线性的特点，这使得模型训练复杂化，并导致特征重要性在不同训练轮次间波动，从而破坏了模型的可信度。SHAPCA通过将解释映射回原始输入空间，使从业者能够将预测与生物组分联系起来，从全局和局部两个角度进行分析。数值分析证明了该方法的结果具有可解释性，并且在多次运行中具有更高的一致性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

</details>

---

### 27. [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](https://arxiv.org/abs/2603.19183)

**基本信息**

- 🔗 arXiv: [`2603.19183`](https://arxiv.org/abs/2603.19183)
- 👥 作者: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19183.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用稀疏自编码器等机制可解释性技术来分析视觉-语言-动作（VLA）模型的内部表征，这属于对复杂模型（可视为一种“大模型”）的内部工作机制进行分析和理解的范畴，与“化学大模型”的研究范式有共通之处。

**📖 中文摘要**

本文应用机制可解释性技术来理解视觉-语言-动作（VLA）模型的内部工作机制。为了探究内部表征，作者在VLA的隐藏层激活上训练了稀疏自编码器（SAE）。SAE学习到一个稀疏字典，其特征作为模型计算的一个紧凑、可解释的基础。研究发现，大多数提取的SAE特征对应于特定训练演示中的记忆序列，但也有一些特征对应于可解释、通用且可引导的运动基元和语义属性。作者提出了一个指标，根据特征是代表可泛化的可迁移基元还是特定情节的记忆来对特征进行分类。通过在LIBERO基准测试上的引导实验验证了这些发现，表明单个SAE特征可以因果性地影响机器人行为。这项工作提供了第一个机制证据，表明VLA可以跨任务和场景学习可泛化的特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for general-purpose robot manipulation. However, their generalization is inconsistent: while these models can perform impressively in some settings, fine-tuned variants often fail on novel objects, scenes, and instructions. We apply mechanistic interpretability techniques to better understand the inner workings of VLA models. To probe internal representations, we train Sparse Autoencoders (SAEs) on hidden layer activations of the VLA. SAEs learn a sparse dictionary whose features act as a compact, interpretable basis for the model's computation. We find that the large majority of extracted SAE features correspond to memorized sequences from specific training demonstrations. However, some features correspond to interpretable, general, and steerable motion primitives and semantic properties, offering a promising glimpse toward VLA generalizability. We propose a metric to categorize features according to whether they represent generalizable transferable primitives or episode-specific memorization. We validate these findings through steering experiments on the LIBERO benchmark. We show that individual SAE features causally influence robot behavior. Steering general features induces behaviors consistent with their semantic meaning and can be applied across tasks and scenes. This work provides the first mechanistic evidence that VLAs can learn generalizable features across tasks and scenes. We observe that supervised fine-tuning on small robotics datasets disproportionately amplifies memorization. In contrast, training on larger, more diverse datasets (e.g., DROID) or using knowledge insulation promotes more general features. We provide an open-source codebase and user-friendly interface for activation collection, SAE training, and feature steering. Our project page is located at this http URL

</details>

---

### 28. [MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185)

**基本信息**

- 🔗 arXiv: [`2603.19185`](https://arxiv.org/abs/2603.19185)
- 👥 作者: Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19185.pdf)

**💡 相关性分析**

满足标准2：论文围绕基于扩散模型的合成表格数据生成及其隐私评估展开，这为化学信息学领域（例如，用于保护隐私的分子数据生成和评估）提供了相关的数据生成模型和评估框架（工具）。

**📖 中文摘要**

本文介绍了MIDST挑战赛，该挑战赛旨在对基于扩散模型生成的合成表格数据的隐私增益进行定量评估，特别关注其对成员推理攻击（MIA）的抵抗力。鉴于表格数据的异质性和复杂性，研究探索了多个目标模型进行MIA，包括用于混合数据类型单表的扩散模型和具有互连约束的多关系表。MIDST的一个关键成果是启发了针对这些目标扩散模型的新型黑盒和白盒MIA的开发，从而能够全面评估其隐私效力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at this https URL

</details>

---

### 29. [RPiAE: A Representation-Pivoted Autoencoder Enhancing Both Image Generation and Editing](https://arxiv.org/abs/2603.19206)

**基本信息**

- 🔗 arXiv: [`2603.19206`](https://arxiv.org/abs/2603.19206)
- 👥 作者: Yue Gong, Hongyu Li, Shanyuan Liu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19206.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的视觉表征标记器（RPiAE），这是一种用于生成模型（如扩散模型）的工具/方法，旨在改进图像生成和编辑。虽然应用领域是计算机视觉，但其核心方法（改进表征学习以服务于生成任务）与构建更高效的“化学大模型”（例如用于分子生成或性质预测的模型）所需的技术有潜在的相关性。

**📖 中文摘要**

本文提出了Representation-Pivoted AutoEncoder（RPiAE），一种基于表征的标记器，旨在同时改进图像生成和编辑。该方法引入了一种训练策略，使经过表征初始化的编码器能够为重建进行微调，同时保留预训练表征空间的语义结构。随后通过一个变分桥将潜在空间压缩成一个更紧凑的空间，以便更好地进行扩散建模。实验表明，RPiAE在文本到图像生成和图像编辑方面优于其他视觉标记器，同时在基于表征的标记器中提供了最佳的重建保真度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have become the dominant paradigm for image generation and editing, with latent diffusion models shifting denoising to a compact latent space for efficiency and scalability. Recent attempts to leverage pretrained visual representation models as tokenizer priors either align diffusion features to representation features or directly reuse representation encoders as frozen tokenizers. Although such approaches can improve generation metrics, they often suffer from limited reconstruction fidelity due to frozen encoders, which in turn degrades editing quality, as well as overly high-dimensional latents that make diffusion modeling difficult. To address these limitations, We propose Representation-Pivoted AutoEncoder, a representation-based tokenizer that improves both generation and editing. We introduce Representation-Pivot Regularization, a training strategy that enables a representation-initialized encoder to be fine-tuned for reconstruction while preserving the semantic structure of the pretrained representation space, followed by a variational bridge which compress latent space into a compact one for better diffusion modeling. We adopt an objective-decoupled stage-wise training strategy that sequentially optimizes generative tractability and reconstruction-fidelity objectives. Together, these components yield a tokenizer that preserves strong semantics, reconstructs faithfully, and produces latents with reduced diffusion modeling complexity. Experiments demonstrate that RPiAE outperforms other visual tokenizers on text-to-image generation and image editing, while delivering the best reconstruction fidelity among representation-based tokenizers.

</details>

---

### 30. [Generative Replica-Exchange: A Flow-based Framework for Accelerating Replica Exchange Simulations](https://arxiv.org/abs/2603.18076)

**基本信息**

- 🔗 arXiv: [`2603.18076`](https://arxiv.org/abs/2603.18076)
- 👥 作者: Shengjie Huang, Sijie Yang, Jianqiao Yi 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18076.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用深度生成模型（归一化流）来加速分子模拟，这直接属于“化学大模型”在计算化学中的应用范畴。

**📖 中文摘要**

本文提出了生成式副本交换（GREX），这是一种将深度生成模型（特别是归一化流）集成到副本交换（REX）模拟框架中的新方法。GREX旨在通过消除对大量中间温度副本的需求来加速分子模拟。该方法利用训练好的归一化流按需生成高温构型，并使用势能作为约束将其直接映射到目标分布。这项工作与化学信息学中开发用于加速分子模拟和采样的新型生成模型（化学大模型）高度相关。它提供了一个具体的框架，展示了生成模型如何解决计算化学中的经典采样问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Replica exchange (REX) is one of the most widely used enhanced sampling methodologies, yet its efficiency is limited by the requirement for a large number of intermediate temperature replicas. Here we present Generative Replica Exchange (GREX), which integrates deep generative models into the REX framework to eliminate this temperature ladder. Drawing inspiration from reservoir replica exchange (res-REX), GREX utilizes trained normalizing flows to generate high-temperature configurations on demand and map them directly to the target distribution using the potential energy as a constraint, without requiring target-temperature training data. This approach reduces production simulations to a single replica at the target temperature while maintaining thermodynamic rigor through Metropolis exchange acceptance. We validate GREX on three benchmark systems of increasing complexity, highlighting its superior efficiency and practical applicability for molecular simulations.

</details>

---

### 31. [Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows](https://arxiv.org/abs/2603.18205)

**基本信息**

- 🔗 arXiv: [`2603.18205`](https://arxiv.org/abs/2603.18205)
- 👥 作者: Dominic Schuh, Lena Funcke, Janik Kreit 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用归一化流（一种生成模型/化学大模型）来解决量子化学和凝聚态物理中一个基础且具有挑战性的计算问题（哈伯德模型的符号问题）。

**📖 中文摘要**

本文解决了掺杂哈伯德模型在有限化学势下的符号问题，这是一个理解掺杂相关系统的基石模型。作者扩展了在半填充情况下使用归一化流的最新进展，通过引入退火方案实现对有限化学势情况的遍历采样。与在电荷基中使用的最先进的混合蒙特卡罗方法相比，该方法在减少统计不确定性的同时准确再现了精确对角化结果。这项工作展示了归一化流（一种生成模型）在解决量子多体系统关键计算挑战（符号问题）中的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hubbard model at finite chemical potential is a cornerstone for understanding doped correlated systems, but simulations are severely limited by the sign problem. In the auxiliary-field formulation, the spin basis mitigates the sign problem, yet severe ergodicity issues have limited its use. We extend recent advances with normalizing flows at half-filling to finite chemical potential by introducing an annealing scheme enabling ergodic sampling. Compared to state-of-the-art hybrid Monte Carlo in the charge basis, our approach accurately reproduces exact diagonalization results while reducing statistical uncertainties by an order of magnitude, opening a new path for simulations of doped correlated systems.

</details>

---

### 32. [A Hybrid Conditional Diffusion-DeepONet Framework for High-Fidelity Stress Prediction in Hyperelastic Materials](https://arxiv.org/abs/2603.18225)

**基本信息**

- 🔗 arXiv: [`2603.18225`](https://arxiv.org/abs/2603.18225)
- 👥 作者: Purna Vindhya Kota, Meer Mehran Rashid, Somdatta Goswami 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18225.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法依赖于条件扩散模型（cDDPM），这是一种先进的生成模型，用于解决材料科学中的物理场预测问题，属于生成式科学模型（化学/材料大模型）的应用。

**📖 中文摘要**

本文提出了一种混合条件扩散-DeepONet框架（cDDPM-DeepONet），用于超弹性材料中高保真度的应力预测。该框架将应力形态与幅值解耦：一个基于UNet的条件去噪扩散概率模型（cDDPM）生成归一化的冯·米塞斯应力场，同时一个改进的DeepONet预测全局缩放参数。该方法旨在克服传统深度学习代理在捕捉尖锐应力集中和宽动态范围方面的局限性。虽然应用背景是固体力学，但其核心方法——结合扩散模型（一种强大的生成模型）和神经算子进行物理场预测——展示了生成式人工智能在科学计算和材料建模中的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting stress fields in hyperelastic materials with complex microstructures remains challenging for traditional deep learning surrogates, which struggle to capture both sharp stress concentrations and the wide dynamic range of stress magnitudes. Convolutional architectures such as UNet tend to oversmooth high-frequency gradients, while neural operators like DeepONet exhibit spectral bias and underpredict localized extremes. Diffusion models can recover fine-scale structure but often introduce low-frequency amplitude drift, degrading physical scaling. To address these limitations, we propose a hybrid surrogate framework, cDDPM-DeepONet, that decouples stress morphology from magnitude. A conditional denoising diffusion probabilistic model (cDDPM), built on a UNet backbone, generates normalized von Mises stress fields conditioned on geometry and loading. In parallel, a modified DeepONet predicts global scaling parameters (minimum and maximum stress), enabling reconstruction of full-resolution physical stress maps. This separation allows the diffusion model to focus on spatial structure while the operator network corrects global amplitude, mitigating spectral and scaling biases. We evaluate the framework on nonlinear hyperelastic datasets with single and multiple polygonal voids. The proposed model consistently outperforms UNet, DeepONet, and standalone cDDPM baselines by one to two orders of magnitude. Spectral analysis shows strong agreement with finite element solutions across all wavenumbers, preserving both global behavior and localized stress concentrations.

</details>

---

### 33. [Nonlinear Incompressible Shear Wave Models in Hyperelasticity and Viscoelasticity Frameworks, with Applications to Love Waves](https://arxiv.org/abs/2603.18296)

**基本信息**

- 🔗 arXiv: [`2603.18296`](https://arxiv.org/abs/2603.18296)
- 👥 作者: Shawn Samuel Carl McAdam, Samuel Opoku Agyemang, Alexei Cheviakov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18296.pdf)

**💡 相关性分析**

不相关。论文专注于连续介质力学和波动方程的解析与数值研究，未涉及化学信息学、质谱分析、化学大模型或质谱结构推理。

**📖 中文摘要**

本文提出了不可压缩超弹性材料中剪切位移的通用方程，并将其应用于描述在具有不同力学性能的材料界面上传播的非线性Love型波。该模型适用于一大类超粘弹性材料。对于三次Yeoh模型，剪切波方程包含三次和五次微分多项式项，以及以混合导数形式表示的粘弹性贡献。这项工作专注于连续介质力学中材料行为的物理建模和数值模拟。虽然不直接涉及机器学习或大模型，但其研究的非线性波传播和材料本构关系是计算材料科学和物理信息机器学习的基础物理知识。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

General equations describing shear displacements in incompressible hyperelastic materials, holding for an arbitrary form of strain energy density function, are presented and applied to the description of nonlinear Love-type waves propagating on an interface between materials with different mechanical properties. The model is valid for a broad class of hyper-viscoelastic materials. For a cubic Yeoh model, shear wave equations contain cubic and quintic differential polynomial terms, including viscoelasticity contributions in terms of dispersion terms that include mixed derivatives $u_{xxt}$ of the material displacement. Full (2+1)-dimensional numerical simulations of waves propagating in the bulk of a two-layered solid are undertaken and analyzed with respect to the source position and mechanical properties of the layers. Interfacial nonlinear Love waves and free upper surface shear waves are tracked; it is demonstrated that in the fully nonlinear case, the variable wave speed of interface and surface waves generally satisfies the linear Love wave existence condition $c_1 < \abs{v} < c_2$, while tending to the larger material wave speed $c_1$ or $c_2$ for large times.

</details>

---

### 34. [An SO(3)-equivariant reciprocal-space neural potential for long-range interactions](https://arxiv.org/abs/2603.18389)

**基本信息**

- 🔗 arXiv: [`2603.18389`](https://arxiv.org/abs/2603.18389)
- 👥 作者: Linfeng Zhang, Taoyong Cui, Dongzhan Zhou 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的SO(3)-等变神经原子间势（EquiEwald），这是一种用于分子和材料模拟的机器学习力场（化学大模型），专门设计用于捕获长程相互作用。

**📖 中文摘要**

本文介绍了EquiEwald，一种统一的神经原子间势，它将Ewald启发的倒空间公式嵌入到不可约SO(3)-等变框架中。通过在学习等变k空间滤波器和等变逆变换的倒空间中进行等变消息传递，EquiEwald能够捕获各向异性、张量化的长程关联，而不牺牲物理一致性。该工作旨在解决基于机器学习的原子间势在表示长程静电和极化相互作用方面的根本限制。EquiEwald是专门为分子和凝聚相系统设计的“机器学习原子间势”，这是化学大模型在原子尺度模拟中的核心应用之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Long-range electrostatic and polarization interactions play a central role in molecular and condensed-phase systems, yet remain fundamentally incompatible with locality-based machine-learning interatomic potentials. Although modern SO(3)-equivariant neural potentials achieve high accuracy for short-range chemistry, they cannot represent the anisotropic, slowly decaying multipolar correlations governing realistic materials, while existing long-range extensions either break SO(3) equivariance or fail to maintain energy-force consistency. Here we introduce EquiEwald, a unified neural interatomic potential that embeds an Ewald-inspired reciprocal-space formulation within an irreducible SO(3)-equivariant framework. By performing equivariant message passing in reciprocal space through learned equivariant k-space filters and an equivariant inverse transform, EquiEwald captures anisotropic, tensorial long-range correlations without sacrificing physical consistency. Across periodic and aperiodic benchmarks, EquiEwald captures long-range electrostatic behavior consistent with ab initio reference data and consistently improves energy and force accuracy, data efficiency, and long-range extrapolation. These results establish EquiEwald as a physically principled paradigm for long-range-capable machine-learning interatomic potentials.

</details>

---

### 35. [Precise Performance of Linear Denoisers in the Proportional Regime](https://arxiv.org/abs/2603.18483)

**基本信息**

- 🔗 arXiv: [`2603.18483`](https://arxiv.org/abs/2603.18483)
- 👥 作者: Reza Ghane, Danil Akhtiamov, Babak Hassibi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18483.pdf)

**💡 相关性分析**

不相关。论文核心是统计估计和信号处理理论，虽然涉及从数据中学习模型，但其背景、方法和目标（通用线性降噪）与化学信息学、质谱分析或特定的化学大模型/质谱结构推理主题没有直接联系。

**📖 中文摘要**

本文研究了噪声数据线性降噪器的性能，其中数据具有未知协方差。作者提出了一种替代经验维纳滤波的方法：通过向数据样本注入具有不同协方差的合成高斯噪声来训练线性降噪器W。在比例机制下，他们使用凸高斯Min-Max定理（CGMT）找到了该过程获得的降噪器泛化误差的闭合形式表达式。这项工作为理解数据驱动线性估计器的统计特性提供了理论框架。虽然主题是信号处理中的降噪，但其关于从数据中学习最优线性变换（可视为一种简单模型）的理论分析与机器学习模型的理论分析有相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the present paper we study the performance of linear denoisers for noisy data of the form $\mathbf{x} + \mathbf{z}$, where $\mathbf{x} \in \mathbb{R}^d$ is the desired data with zero mean and unknown covariance $\mathbf{\Sigma}$, and $\mathbf{z} \sim \mathcal{N}(0, \mathbf{\Sigma}_{\mathbf{z}})$ is additive noise. Since the covariance $\mathbf{\Sigma}$ is not known, the standard Wiener filter cannot be employed for denoising. Instead we assume we are given samples $\mathbf{x}_1,\dots,\mathbf{x}_n \in \mathbb{R}^d$ from the true distribution. A standard approach would then be to estimate $\mathbf{\Sigma}$ from the samples and use it to construct an ``empirical" Wiener filter. However, in this paper, motivated by the denoising step in diffusion models, we take a different approach whereby we train a linear denoiser $\mathbf{W}$ from the data itself. In particular, we synthetically construct noisy samples $\hat{\mathbf{x}}_i$ of the data by injecting the samples with Gaussian noise with covariance $\mathbf{\Sigma}_1 \neq \mathbf{\Sigma}_{\mathbf{z}}$ and find the best $\mathbf{W}$ that approximates $\mathbf{W}\hat{\mathbf{x}}_i \approx \mathbf{x}_i$ in a least-squares sense. In the proportional regime $\frac{n}{d} \rightarrow \kappa > 1$ we use the {\it Convex Gaussian Min-Max Theorem (CGMT)} to analytically find the closed form expression for the generalization error of the denoiser obtained from this process. Using this expression one can optimize over $\mathbf{\Sigma}_1$ to find the best possible denoiser. Our numerical simulations show that our denoiser outperforms the ``empirical" Wiener filter in many scenarios and approaches the optimal Wiener filter as $\kappa\rightarrow\infty$.

</details>

---

### 36. [End-to-End QGAN-Based Image Synthesis via Neural Noise Encoding and Intensity Calibration](https://arxiv.org/abs/2603.18554)

**基本信息**

- 🔗 arXiv: [`2603.18554`](https://arxiv.org/abs/2603.18554)
- 👥 作者: Xue Yang, Rigui Zhou, Shizheng Jia 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18554.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子生成对抗网络（QGAN），这是一种在量子计算设备上实现的生成模型。虽然应用是图像生成，但QGAN本身是生成模型（大模型）在量子计算领域的一个变种，与探索新型生成模型架构的研究主题相关。

**📖 中文摘要**

本文提出了ReQGAN，一种用于图像合成的端到端量子生成对抗网络框架。ReQGAN使用单个D量子电路合成整个N=2^D像素的图像，克服了直接像素生成的两个瓶颈：刚性的经典到量子噪声接口和输出失配。作者引入了可学习的神经噪声编码器用于自适应状态准备，以及可微分的强度校准模块将测量映射到稳定的像素域。在MNIST和Fashion-MNIST上的实验表明，ReQGAN在严格的量子比特预算下实现了稳定的训练和有效的图像合成。这项工作属于量子机器学习范畴，探索了用于生成任务的量子生成模型（QGAN）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Generative Adversarial Networks (QGANs) offer a promising path for learning data distributions on near-term quantum devices. However, existing QGANs for image synthesis avoid direct full-image generation, relying on classical post-processing or patch-based methods. These approaches dilute the quantum generator's role and struggle to capture global image semantics. To address this, we propose ReQGAN, an end-to-end framework that synthesizes an entire N=2^D-pixel image using a single D-qubit quantum circuit. ReQGAN overcomes two fundamental bottlenecks hindering direct pixel generation: (1) the rigid classical-to-quantum noise interface and (2) the output mismatch between normalized quantum statistics and the desired pixel-intensity space. We introduce a learnable Neural Noise Encoder for adaptive state preparation and a differentiable Intensity Calibration module to map measurements to a stable, visually meaningful pixel domain. Experiments on MNIST and Fashion-MNIST demonstrate that ReQGAN achieves stable training and effective image synthesis under stringent qubit budgets, with ablation studies verifying the contribution of each component.

</details>

---

### 37. [DeePAW: A universal machine learning model for orbital-free ab initio calculations](https://arxiv.org/abs/2603.18650)

**基本信息**

- 🔗 arXiv: [`2603.18650`](https://arxiv.org/abs/2603.18650)
- 👥 作者: Tianhao Su, Shunbo Hu, Yue Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18650.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是DeePAW，一个用于无轨道ab initio计算的通用机器学习模型。这直接属于“化学大模型”范畴，旨在用AI革命化电子结构计算和材料建模。

**📖 中文摘要**

本文提出了深度增强方式模型（DeePAW），这是一种用于无轨道ab initio计算的通用机器学习模型。DeePAW基于密度泛函理论，是目前覆盖元素最多、晶体结构应用能力最广、预测精度最高且无需微调的最佳无轨道DFT ML模型。其科学优点和创新源于新颖的SE(3)-等变双消息传递神经网络。除了预测电子密度分布，DeePAW还能预测晶体的形成能。这项工作代表了开发用于ab initio计算的通用机器学习模型的前沿，是化学和材料科学中“大模型”的典型实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing universal machine learning models for ab initio calculations is the frontier of materials cutting edge research in the new era of artificial intelligence. Here, we present the Deep Augment Way model (DeePAW) that is a universal machine learning (ML) model for orbital-free (OF) ab initio calculations, based on the density functional theory (DFT). DeePAW is currently the best OFDFT ML model according to the three criterions, 1) covering the largest number of elements, 2) having the widest application capability to diverse crystal structures, and 3) achieving the highest prediction accuracy without further fine-tuning. These scientific merits and innovations of DeePAW are stemmed from the novel SE(3)-equivariant double massage passing neuron networks. Besides predicting electron density distributions, DeePAW predicts formation energies of crystals as well and therefore paves an efficient avenue for multiscale materials modeling beyond conventional electronic structure calculation methods.

</details>

---

### 38. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](https://arxiv.org/abs/2603.18864)

**基本信息**

- 🔗 arXiv: [`2603.18864`](https://arxiv.org/abs/2603.18864)
- 👥 作者: Samuel Del Fré, Gilberto A. Alou Angulo, Maurice Monnerville 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18864.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对特定化学过程（NO在石墨上的散射）构建数据驱动的机器学习原子间势（MLIP）。MLIP是化学大模型在分子模拟中的关键应用，本文详细阐述了其构建工作流程，包括主动学习，与主题高度相关。

**📖 中文摘要**

本文为气体-表面散射动力学开发了一种数据驱动的工作流程，用于构建机器学习原子间势（MLIP），以一氧化氮（NO）在石墨上散射为基准系统。工作流程从初始的ab initio分子动力学数据集开始，使用SOAP描述符描述局部原子环境，并通过主成分分析在降维特征空间中进行分析。使用最远点采样构建紧凑训练集，并通过基于查询的委员会主动学习策略，利用从扩展入射能和表面温度范围的分子动力学模拟中提取的额外构型来细化最终的深度势模型。最终的MLIP能够以远低于AIMD的计算成本实现NO在石墨上散射的大规模分子动力学模拟。这项工作展示了为特定化学系统（气体-表面散射）构建专用MLIP的完整流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate atomistic simulations of gas-surface scattering require potential energy surfaces that remain reliable over broad configurational and energetic ranges while retaining the efficiency needed for extensive trajectory sampling. Here, we develop a data-driven workflow for constructing a machine-learning interatomic potential (MLIP) tailored to gas-surface scattering dynamics, using nitric oxide (NO) scattering from highly oriented pyrolytic graphite (HOPG) as a benchmark system. Starting from an initial ab initio molecular dynamics (AIMD) dataset, local atomic environments are described by SOAP descriptors and analyzed in a reduced feature space obtained through principal component analysis. Farthest point sampling is then used to build a compact training set, and the resulting Deep Potential model is refined through a query-by-committee active-learning strategy using additional configurations extracted from molecular dynamics simulations over extended ranges of incident energies and surface temperatures. The final MLIP reproduces reference energies and forces with high fidelity and enables large-scale molecular dynamics simulations of NO scattering from graphite at a computational cost far below that of AIMD. The simulations provide detailed insight into adsorption energetics, trapping versus direct scattering probabilities, translational energy loss, angular distributions, and rotational excitation. Overall, the results reproduce the main experimental trends and demonstrate that descriptor-guided sampling combined with active learning offers an efficient and transferable strategy for constructing MLIPs for gas-surface interactions.

</details>

---

### 39. [Improving moment tensor solutions under Earth structure uncertainty with simulation-based inference](https://arxiv.org/abs/2603.18925)

**基本信息**

- 🔗 arXiv: [`2603.18925`](https://arxiv.org/abs/2603.18925)
- 👥 作者: A. A. Saoulis, T.-S. Pham, A. M. G. Ferreira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18925.pdf)

**💡 相关性分析**

不相关。论文应用模拟推理和深度学习解决地球物理学中的地震源反演问题。虽然使用了先进的机器学习方法，但其研究领域（地震学）和具体问题（矩张量反演）与化学信息学、质谱分析、化学大模型或质谱结构推理没有直接关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian inference represents a principled way to incorporate Earth structure uncertainty in full-waveform moment tensor inversions, but traditional approaches generally require significant approximations that risk biasing the resulting solutions. We introduce a robust method for handling theory errors using simulation-based inference (SBI), a machine learning approach that empirically models their impact on the observations. This framework retains the rigour of Bayesian inference while avoiding restrictive assumptions about the functional form of the uncertainties. We begin by demonstrating that the common Gaussian parametrisation of theory errors breaks down under minor ($1-3 \%$) 1-D Earth model uncertainty. To address this issue, we develop two formalisms for utilising SBI to improve the quality of the moment tensor solutions: one using physics-based insights into the theory errors, and another utilising an end-to-end deep learning algorithm. We then compare the results of moment tensor inversion with the standard Gaussian approach and SBI, and demonstrate that Gaussian assumptions induce bias and significantly under-report moment tensor uncertainties. We also show that these effects are particularly problematic when inverting short period data and for shallow, isotropic events. On the other hand, SBI produces more reliable, better calibrated posteriors of the earthquake source mechanism. Finally, we successfully apply our methodology to two well studied moderate magnitude earthquakes: one from the 1997 Long Valley Caldera volcanic earthquake sequence, and the 2020 Zagreb earthquake.

</details>

---

### 40. [Revisiting OmniAnomaly for Anomaly Detection: performance metrics and comparison with PCA-based models](https://arxiv.org/abs/2603.18985)

**基本信息**

- 🔗 arXiv: [`2603.18985`](https://arxiv.org/abs/2603.18985)
- 👥 作者: Bruna Alves, Ana Martins, Armando J. Pinho 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18985.pdf)

**💡 相关性分析**

不相关。论文核心是比较时间序列异常检测中的深度学习模型与经典线性方法，属于机器学习中的模型评估研究，与化学信息学、质谱分析或指定的化学大模型/质谱结构推理主题无关。

**📖 中文摘要**

本文重新审视了OmniAnomaly（一种用于多元时间序列异常检测的广泛使用的随机循环模型），并在服务器机器数据集（SMD）上将其与基于主成分分析（PCA）的简单线性基线进行了系统比较。两种方法在相同的阈值评估程序下进行评估。结果表明，PCA可以达到与OmniAnomaly相当的性能，甚至在不应用点调整时表现更优。这些发现对当前基准测试实践下更复杂架构的附加价值提出了质疑。本文侧重于时间序列异常检测的模型评估和比较，属于机器学习应用领域。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning models have become the dominant approach for multivariate time series anomaly detection (MTSAD), often reporting substantial performance improvements over classical statistical methods. However, these gains are frequently evaluated under heterogeneous thresholding strategies and evaluation protocols, making fair comparisons difficult. This work revisits OmniAnomaly, a widely used stochastic recurrent model for MTSAD, and systematically compares it with a simple linear baseline based on Principal Component Analysis (PCA) on the Server Machine Dataset (SMD). Both methods are evaluated under identical thresholding and evaluation procedures, with experiments repeated across 100 runs for each of the 28 machines in the dataset. Performance is evaluated using Precision, Recall and F1-score at point-level, with and without point-adjustment, and under different aggregation strategies across machines and runs, with the corresponding standard deviations also reported. The results show large variability across machines and show that PCA can achieve performance comparable to OmniAnomaly, and even outperform it when point-adjustment is not applied. These findings question the added value of more complex architectures under current benchmarking practices and highlight the critical role of evaluation methodology in MTSAD research.

</details>

---

### 41. [Fast and Interpretable Autoregressive Estimation with Neural Network Backpropagation](https://arxiv.org/abs/2603.19041)

**基本信息**

- 🔗 arXiv: [`2603.19041`](https://arxiv.org/abs/2603.19041)
- 👥 作者: Anaísa Lucena, Ana Martins, Armando J. Pinho 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19041.pdf)

**💡 相关性分析**

不相关。论文提出了一种使用神经网络估计经典时间序列模型（AR）参数的新方法。虽然涉及神经网络，但其应用场景是通用时间序列分析，并非化学或质谱领域，也未涉及化学大模型或质谱结构推理。

**📖 中文摘要**

本文提出了一种自回归（AR）模型的神经网络（NN）公式，通过将自回归结构直接嵌入前馈神经网络中，使得能够通过反向传播进行系数估计，同时保持可解释性。在125,000个具有短期依赖性的合成AR(p)时间序列上的模拟实验表明，所提出的基于NN的方法能一致地恢复所有序列的模型系数，而条件最大似然（CML）在大约55%的情况下无法收敛。当两种方法都收敛时，估计精度相当。这项工作展示了使用梯度下降NN优化作为可解释AR参数估计的快速高效替代方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autoregressive (AR) models remain widely used in time series analysis due to their interpretability, but convencional parameter estimation methods can be computationally expensive and prone to convergence issues. This paper proposes a Neural Network (NN) formulation of AR estimation by embedding the autoregressive structure directly into a feedforward NN, enabling coefficient estimation through backpropagation while preserving interpretability. Simulation experiments on 125,000 synthetic AR(p) time series with short-term dependence (1 <= p <= 5) show that the proposed NN-based method consistently recovers model coefficients for all series, while Conditional Maximum Likelihood (CML) fails to converge in approximately 55% of cases. When both methods converge, estimation accuracy is comparable with negligible differences in relative error, R2 and, perplexity/likelihood. However, when CML fails, the NN-based approach still provides reliable estimates. In all cases, the NN estimator achieves substantial computational gains, reaching a median speedup of 12.6x and up to 34.2x for higher model orders. Overall, results demonstrate that gradient-descent NN optimization can provide a fast and efficient alternative for interpretable AR parameter estimation.

</details>

---

### 42. [BSTModelKit.jl: A Julia Package for Constructing, Solving, and Analyzing Biochemical Systems Theory Models](https://arxiv.org/abs/2603.19115)

**基本信息**

- 🔗 arXiv: [`2603.19115`](https://arxiv.org/abs/2603.19115)
- 👥 作者: Sandra Vadhin, Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19115.pdf)

**💡 相关性分析**

满足标准2：论文介绍了一个软件包（BSTModelKit.jl），用于构建和分析生化系统理论模型。这为化学信息学和系统生物学领域的研究人员提供了用于建模生化网络（一种特定类型的化学模型）的工具和资源。

**📖 中文摘要**

本文介绍了BSTModelKit.jl，一个用于构建、求解和分析生化系统理论（BST）模型的开源Julia软件包。该包实现了S-system表示法，这是一种用于建模代谢和调控网络的规范幂律形式主义。BSTModelKit.jl提供了声明式模型规范格式、通过常微分方程（ODE）积分的动态模拟、稳态计算以及使用Morris和Sobol方法的全局敏感性分析。该软件包利用了Julia科学计算生态系统，特别是SciML微分方程求解器套件，以提供高效灵活的模型分析工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present this http URL , an open-source Julia package for constructing, solving, and analyzing Biochemical Systems Theory (BST) models of biochemical networks. The package implements S-system representations, a canonical power-law formalism for modeling metabolic and regulatory networks. this http URL provides a declarative model specification format, dynamic simulation via ordinary differential equation (ODE) integration, steady-state computation, and global sensitivity analysis using the Morris and Sobol methods. The package leverages the Julia scientific computing ecosystem, in particular the SciML suite of differential equation solvers, to provide efficient and flexible model analysis tools. We describe the mathematical formulation, software design, and demonstrate the package capabilities with illustrative examples.

</details>

---

### 43. [Variational and Annealing-Based Approaches to Quantum Combinatorial Optimization](https://arxiv.org/abs/2603.19117)

**基本信息**

- 🔗 arXiv: [`2603.19117`](https://arxiv.org/abs/2603.19117)
- 👥 作者: Hala Hawashin, Deep Nath, Marco Alberto Javarone
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19117.pdf)

**💡 相关性分析**

不相关。论文是一篇关于量子计算在组合优化中应用的综述，其核心是优化算法和量子硬件，并非针对化学信息学或质谱分析领域，也未讨论化学大模型或质谱结构推理。

**📖 中文摘要**

本文回顾了组合优化的量子方法，旨在连接理论发展和工业相关性。作者首先调查了主要的量子算法家族，包括量子退火、量子近似优化算法（QAOA）、量子强化学习（QRL）和量子生成建模（QGM）。然后，他们研究了量子技术目前显示出量子优势证据的问题类别，并借鉴了已建立的基准测试计划。这些工作将量子计算中的优化算法（包括量子退火和QAOA）与工业应用联系起来。虽然涉及量子算法，但综述重点在优化，而非化学信息学或质谱。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we review quantum approaches to combinatorial optimization, with the aim of bridging theoretical developments and industrial relevance. We first survey the main families of quantum algorithms, including Quantum Annealing, the Quantum Approximate Optimization Algorithm (QAOA), Quantum Reinforcement Learning (QRL), and Quantum Generative Modeling (QGM). We then examine the problem classes where quantum technologies currently show evidence of quantum advantage, drawing on established benchmarking initiatives such as QOBLIB, QUARK, QASMBench, and QED-C. These problem classes are subsequently mapped to representative industrial domains, including logistics, finance, and telecommunications. Our analysis indicates that quantum annealing currently exhibits the highest level of operational maturity, while QAOA shows promising potential on NISQ-era hardware. In contrast, QRL and QGM emerge as longer-term research directions with significant potential for future industrial impact.

</details>

---

### 44. [Quantum block encoding for semiseparable matrices](https://arxiv.org/abs/2603.19130)

**基本信息**

- 🔗 arXiv: [`2603.19130`](https://arxiv.org/abs/2603.19130)
- 👥 作者: Giacomo Antonioli, Paola Boito, Gianna M. Del Corso 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19130.pdf)

**💡 相关性分析**

不相关。论文研究量子计算中特定类型矩阵（单对可分矩阵）的块编码技术，属于量子算法和线性代数子领域，与化学信息学、质谱分析或化学大模型无直接关联。

**📖 中文摘要**

本文研究了用于单对可分矩阵的量子块编码（QBE）。作者提出了一种新的块编码方法，该方法依赖于将给定矩阵分解为三角因子和 diagonal 因子的乘积。为了编码矩阵，算法需要2log(N)+7个辅助量子比特。这个过程需要多对数时间，并且误差为O(N^2)。这项工作属于量子算法设计范畴，专注于为特定类型的结构化矩阵开发高效的量子子程序。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum block encoding (QBE) is a crucial step in the development of most quantum algorithms, as it provides an embedding of a given matrix into a suitable larger unitary matrix. Historically, the development of efficient techniques for QBE has mostly focused on sparse matrices; less effort has been devoted to data-sparse (e.g., rank-structured) matrices. In this work we examine a particular case of rank structure, namely, one-pair semiseparable matrices. We present a new block encoding approach that relies on a suitable factorization of the given matrix as the product of triangular and diagonal factors. To encode the matrix, the algorithm needs $2\log(N)+7$ ancillary qubits. This process takes polylogarithmic time and has an error of $\mathcal{O}(N^2)$, where $N$ is the matrix size.

</details>

---

### 45. [How Auditory Knowledge in LLM Backbones Shapes Audio Language Models: A Holistic Evaluation](https://arxiv.org/abs/2603.19195)

**基本信息**

- 🔗 arXiv: [`2603.19195`](https://arxiv.org/abs/2603.19195)
- 👥 作者: Ke-Han Lu, Szu-Wei Fu, Chao-Han Huck Yang 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19195.pdf)

**💡 相关性分析**

不相关。论文研究大型语言模型在音频任务中的知识迁移和能力评估，属于多模态机器学习（音频-语言）领域，与化学信息学、质谱分析或化学大模型/质谱结构推理无关。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）作为大型音频语言模型（LALMs）知识骨干时，通过纯文本预训练编码了多少听觉知识，以及这如何影响下游性能。作者通过比较不同LLMs在三种设置下的表现来研究这一问题：1）在AKB-2000基准上直接探测；2）级联评估；3）音频接地评估。研究结果表明，听觉知识在不同模型家族间差异很大，并且纯文本结果与音频性能强相关。这项工作旨在理解LLMs在音频研究中的基础作用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been widely used as knowledge backbones of Large Audio Language Models (LALMs), yet how much auditory knowledge they encode through text-only pre-training and how this affects downstream performance remains unclear. We study this gap by comparing different LLMs under two text-only and one audio-grounded setting: (1) direct probing on AKB-2000, a curated benchmark testing the breadth and depth of auditory knowledge; (2) cascade evaluation, where LLMs reason over text descriptions from an audio captioner; and (3) audio-grounded evaluation, where each LLM is fine-tuned into a Large Audio Language Model (LALM) with an audio encoder. Our findings reveal that auditory knowledge varies substantially across families, and text-only results are strongly correlated with audio performance. Our work provides empirical grounding for a comprehensive understanding of LLMs in audio research.

</details>

---

### 46. [CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions](https://arxiv.org/abs/2403.17210)

**基本信息**

- 🔗 arXiv: [`2403.17210`](https://arxiv.org/abs/2403.17210)
- 👥 作者: Azmine Toushik Wasi, Taki Hasan Rafi, Raima Islam 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2403.17210.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于图神经网络（变分图自编码器）的深度学习模型（CADGL）来预测药物-药物相互作用。这直接属于化学信息学中利用AI大模型（特别是图神经网络）解决药物发现问题的范畴。

**📖 中文摘要**

本文提出了CADGL，一个用于预测药物-药物相互作用（DDIs）的情境感知深度图学习框架。基于定制的变分图自编码器（VGAE），该框架使用两个情境预处理器从两个不同角度（局部邻域和分子情境）提取特征。定制的VGAE由图像编码器、潜在信息编码器和MLP解码器组成。CADGL超越了其他最先进的DDI预测模型，在预测具有临床价值的新型DDI方面表现出色。这项工作属于化学信息学和药物发现领域，利用图神经网络（一种深度学习模型）来建模分子间相互作用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Examining Drug-Drug Interactions (DDIs) is a pivotal element in the process of drug development. DDIs occur when one drug's properties are affected by the inclusion of other drugs. Detecting favorable DDIs has the potential to pave the way for creating and advancing innovative medications applicable in practical settings. However, existing DDI prediction models continue to face challenges related to generalization in extreme cases, robust feature extraction, and real-life application possibilities. We aim to address these challenges by leveraging the effectiveness of context-aware deep graph learning by introducing a novel framework named CADGL. Based on a customized variational graph autoencoder (VGAE), we capture critical structural and physio-chemical information using two context preprocessors for feature extraction from two different perspectives: local neighborhood and molecular context, in a heterogeneous graphical structure. Our customized VGAE consists of a graph encoder, a latent information encoder, and an MLP decoder. CADGL surpasses other state-of-the-art DDI prediction models, excelling in predicting clinically valuable novel DDIs, supported by rigorous case studies. CADGL is vailable at: this https URL

</details>

---

### 47. [Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset](https://arxiv.org/abs/2407.17869)

**基本信息**

- 🔗 arXiv: [`2407.17869`](https://arxiv.org/abs/2407.17869)
- 👥 作者: Yiming Ma, Jianzhi Teng, Xinjie Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.17869.pdf)

**💡 相关性分析**

满足标准1和标准2：1）论文的核心方法是提出一种新的解耦条件流匹配（DCFM）框架，这是一种用于解决逆问题的生成模型（流匹配），属于“化学大模型”在材料表征（椭圆偏振）中的应用。2）论文构建并发布了EllipBench，一个用于逆椭圆偏振问题的大规模、高精度数据集，为相关研究提供了宝贵的资源。

**📖 中文摘要**

本文介绍了EllipBench，一个包含超过800万个高精度样本的综合基准数据集，涵盖98种薄膜材料和5种基底。基于此基准，作者系统评估了包括传统机器学习模型、深度神经网络和物理信息神经网络在内的多种方法，并表明现有范式难以完全解决逆椭圆偏振问题。为此，作者进一步提出了一种新颖的解耦条件流匹配（DCFM）框架。DCFM将几何膜厚解耦，并将其作为稳健的物理条件来指导一个连续向量场，用于对波长相关光学常数的逆概率分布进行建模。该工作结合了大规模数据集构建和新型生成模型（流匹配）的开发，以解决材料科学中的逆问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse ellipsometry, i.e., reconstructing optical constants and film thickness from the measured phase difference $\Delta$ and amplitude ratio $\Psi$, is a fundamentally ill-posed problem. Traditional solutions rely on slow, expert-driven iterative fitting, while the development of machine learning approaches has been severely limited by the lack of large-scale, physically consistent datasets. To address this gap, we introduce \textbf{EllipBench}, a comprehensive benchmark comprising over 8 million high-precision samples spanning 98 thin-film materials and 5 substrates. Building upon this benchmark, we conduct a systematic evaluation of a broad spectrum of methods, including traditional machine learning models, deep neural networks, and Physics-Informed Neural Networks, and show that existing paradigms consistently struggle to fully resolve the inverse ellipsometry task. To better capture its inherent ambiguity, we further propose a novel \textbf{Decoupled Conditional Flow Matching (DCFM)} framework. Rather than formulating the problem as deterministic point-to-point regression, DCFM explicitly decouples geometric film thickness and incorporates it as a robust physical condition to guide a continuous vector field for modeling the inverse probability distribution of wavelength-dependent optical constants. Combined with a gradient detachment strategy and physics-based constraints, our joint architecture effectively mitigates intrinsic physical ambiguities and delivers a robust and accurate solution for inverse ellipsometry.

</details>

---

### 48. [Biased AI can Influence Political Decision-Making](https://arxiv.org/abs/2410.06415)

**基本信息**

- 🔗 arXiv: [`2410.06415`](https://arxiv.org/abs/2410.06415)
- 👥 作者: Jillian Fisher, Shangbin Feng, Robert Aron 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.06415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（结构化Transformer用于模型优化）在化学设计任务上进行了应用和验证，直接围绕“化学大模型”这一主题。

**📖 中文摘要**

论文《Cliqueformer: Model-Based Optimization with Structured Transformers》提出了一种基于Transformer的架构Cliqueformer，用于解决离线模型优化问题。该架构通过学习黑盒函数的结构（通过功能图模型）来应对分布偏移，而无需依赖显式的保守方法。论文在多个领域（包括化学和遗传设计任务）中展示了其性能优于现有方法。虽然论文主要关注通用的模型优化框架，但其明确将化学设计任务作为应用领域之一。这使其与“化学大模型”主题相关，因为该工作展示了结构化Transformer在化学设计这一化学信息学核心问题上的应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As modern large language models (LLMs) become integral to everyday tasks, concerns about their inherent biases and their potential impact on human decision-making have emerged. While bias in models are well-documented, less is known about how these biases influence human decisions. This paper presents two interactive experiments investigating the effects of partisan bias in LLMs on political opinions and decision-making. Participants interacted freely with either a biased liberal, biased conservative, or unbiased control model while completing these tasks. We found that participants exposed to partisan biased models were significantly more likely to adopt opinions and make decisions which matched the LLM's bias. Even more surprising, this influence was seen when the model bias and personal political partisanship of the participant were opposite. However, we also discovered that prior knowledge of AI was weakly correlated with a reduction of the impact of the bias, highlighting the possible importance of AI education for robust mitigation of bias effects. Our findings not only highlight the critical effects of interacting with biased LLMs and its ability to impact public discourse and political conduct, but also highlights potential techniques for mitigating these risks in the future.

</details>

---

### 49. [LLM-Based World Models Can Make Decisions Solely, But Rigorous Evaluations are Needed](https://arxiv.org/abs/2411.08794)

**基本信息**

- 🔗 arXiv: [`2411.08794`](https://arxiv.org/abs/2411.08794)
- 👥 作者: Chang Yang, Xinrun Wang, Junzhe Jiang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.08794.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大语言模型作为世界模型的能力，这直接关联到“化学大模型”所依赖的基础模型架构和能力评估方法论。

**📖 中文摘要**

论文《LLM-Based World Models Can Make Decisions Solely, But Rigorous Evaluations are Needed》对基于大语言模型的世界模型进行了全面评估。虽然论文主要讨论LLM作为通用世界模拟器在决策制定中的应用，但其核心研究对象是“大语言模型”作为世界模型。考虑到“化学大模型”是广义“大模型”在化学领域的具体化，且论文探讨了大模型（LLM）的核心能力（模拟、推理、规划）评估，这与构建和理解领域大模型（如化学大模型）的基础方法论和挑战相关。论文的讨论为评估任何领域特定大模型（包括化学大模型）的推理和决策能力提供了重要的视角和评估框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

World model emerges as a key module in decision making, where MuZero and Dreamer achieve remarkable successes in complex tasks. Recent work leverages Large Language Models (LLMs) as general world simulators to simulate the dynamics of the world due to their generalizability. LLMs also serve as the world model for deliberative reasoning in Reasoning via Planning (RAP) and Tree of Thought (ToT). However, the world models are either evaluated as a general world simulator, or as a functional module of the agent, i.e., predicting the transitions to assist the planning. In this work, we propose a comprehensive evaluation of the world models with LLMs from the decision making perspective. Specifically, we leverage the 31 diverse environments from (Wang et al., 2023;2024) and curate the rule-based policy of each environment for the diverse evaluation. Then, we design three main tasks, i.e., policy verification, action proposal, and policy planning, where the world models can be used for decision making solely. Finally, we conduct the comprehensive evaluation of the advanced LLMs, i.e., GPT-4o and GPT-4o-mini, on the environments for the three main tasks under various settings. The key observations include: i) GPT-4o significantly outperforms GPT-4o-mini on the three main tasks, especially for the tasks which require the domain knowledge, ii) the performance of the world model with LLM will be decreased for long-term decision-making tasks, and iii) the combination of different functionalities of the world model will brings additional unstabilities of the performance.

</details>

---

### 50. [LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics](https://arxiv.org/abs/2412.01113)

**基本信息**

- 🔗 arXiv: [`2412.01113`](https://arxiv.org/abs/2412.01113)
- 👥 作者: Keito Kudo, Yoichi Aoki, Tatsuki Kuribayashi 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2412.01113.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型的内部推理机制与忠实性，这对于开发和评估用于复杂科学推理（如质谱结构推理）的“化学大模型”至关重要。

**📖 中文摘要**

论文《LLMs Faithfully and Iteratively Compute Answers During CoT: A Systematic Analysis With Multi-step Arithmetics》研究了大语言模型在执行思维链推理时的内部信息流。通过受控的算术任务实验，揭示了LLMs一种系统的内部推理机制：模型并非在输入时即已确定答案，而是在生成推理链的过程中动态计算（子）答案。因此，生成的推理链可以被视为模型内部计算过程的忠实反映。这项研究深入探讨了大模型推理过程的可信性与机制，这对于构建需要复杂结构推理的“化学大模型”（例如，用于质谱解析或逆合成分析）具有重要的启示意义。理解并确保大模型在科学推理中的忠实性，是化学领域大模型研发的关键基础之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study investigates the internal information flow of large language models (LLMs) while performing chain-of-thought (CoT) style reasoning. Specifically, with a particular interest in the faithfulness of the CoT explanation to LLMs' final answer, we explore (i) when the LLMs' answer is (pre)determined, especially before the CoT begins or after, and (ii) how strongly the information from CoT specifically has a causal effect on the final answer. Our experiments with controlled arithmetic tasks reveal a systematic internal reasoning mechanism of LLMs. They have not derived an answer at the moment when input was fed into the model. Instead, they compute (sub-)answers while generating the reasoning chain on the fly. Therefore, the generated reasoning chains can be regarded as faithful reflections of the model's internal computation.

</details>

---

### 51. [Enhancing Lexicon-Based Text Embeddings with Large Language Models](https://arxiv.org/abs/2501.09749)

**基本信息**

- 🔗 arXiv: [`2501.09749`](https://arxiv.org/abs/2501.09749)
- 👥 作者: Yibin Lei, Tao Shen, Yu Cao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.09749.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于LLM的词典嵌入方法LENS，作为一种改进文本表示的工具，可被应用于化学信息学中处理分子文本描述、文献数据等，为“化学大模型”提供数据表示资源或工具思路。

**📖 中文摘要**

论文《Enhancing Lexicon-Based Text Embeddings with Large Language Models》提出了一种基于词典的文本嵌入方法LENS，该方法利用大语言模型，并在通用文本嵌入任务上达到了有竞争力的性能。虽然论文主要关注通用NLP任务，但其核心贡献在于利用LLM改进嵌入表示。在化学信息学中，分子、反应和性质的文本描述（如SMILES、文献描述）的嵌入是构建化学大模型的基础。论文提出的方法（通过聚类处理词汇冗余、探索双向注意力和池化策略）为如何利用大模型获得更有效的化学领域文本或序列表示提供了潜在的技术思路和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent large language models (LLMs) have demonstrated exceptional performance on general-purpose text embedding tasks. While dense embeddings have dominated related research, we introduce the first lexicon-based embeddings (LENS) leveraging LLMs that achieve competitive performance on these tasks. LENS consolidates the vocabulary space through token embedding clustering to handle the issue of token redundancy in LLM vocabularies. To further improve performance, we investigate bidirectional attention and various pooling strategies. Specifically, LENS simplifies lexical matching with redundant vocabularies by assigning each dimension to a specific token cluster, where semantically similar tokens are grouped together. Extensive experiments demonstrate that LENS outperforms dense embeddings on the Massive Text Embedding Benchmark (MTEB), delivering compact representations with dimensionality comparable to dense counterparts. Furthermore, LENS inherently supports efficient embedding dimension pruning without any specialized objectives like Matryoshka Representation Learning. Notably, combining LENS with dense embeddings achieves state-of-the-art performance on the retrieval subset of MTEB (i.e., BEIR).

</details>

---

### 52. [Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment](https://arxiv.org/abs/2502.03714)

**基本信息**

- 🔗 arXiv: [`2502.03714`](https://arxiv.org/abs/2502.03714)
- 👥 作者: Harrish Thasarathan, Julian Forsyth, Thomas Fel 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03714.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是跨模型的可解释概念发现与对齐，这直接适用于理解和解释“化学大模型”内部学到的化学概念，提升其可解释性和可靠性。

**📖 中文摘要**

论文《Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment》提出了通用稀疏自编码器框架，用于发现和对齐多个预训练深度神经网络中的可解释概念。该框架训练一个单一的过完备稀疏自编码器，可以接收任何模型的激活并解码以近似任何其他模型的激活。USAEs发现了跨视觉模型的语义连贯的通用概念。这项研究在模型可解释性和概念对齐方面提供了创新方法。对于“化学大模型”，理解模型内部学到的化学概念（如官能团、反应类型）以及在不同化学模型之间对齐这些概念，对于提高模型的可信度、可解释性以及进行知识迁移至关重要。因此，该论文的方法论与化学大模型的开发和理解高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Universal Sparse Autoencoders (USAEs), a framework for uncovering and aligning interpretable concepts spanning multiple pretrained deep neural networks. Unlike existing concept-based interpretability methods, which focus on a single model, USAEs jointly learn a universal concept space that can reconstruct and interpret the internal activations of multiple models at once. Our core insight is to train a single, overcomplete sparse autoencoder (SAE) that ingests activations from any model and decodes them to approximate the activations of any other model under consideration. By optimizing a shared objective, the learned dictionary captures common factors of variation-concepts-across different tasks, architectures, and datasets. We show that USAEs discover semantically coherent and important universal concepts across vision models; ranging from low-level features (e.g., colors and textures) to higher-level structures (e.g., parts and objects). Overall, USAEs provide a powerful new method for interpretable cross-model analysis and offers novel applications, such as coordinated activation maximization, that open avenues for deeper insights in multi-model AI systems

</details>

---

### 53. [Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning](https://arxiv.org/abs/2503.16252)

**基本信息**

- 🔗 arXiv: [`2503.16252`](https://arxiv.org/abs/2503.16252)
- 👥 作者: Zhaowei Liu, Xin Guo, Zhi Yang 等17人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.16252.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心是构建领域特定大模型（金融）的方法论，这为“化学大模型”的构建提供了直接相关的技术范例（满足标准1）。同时，论文也涉及对领域大模型挑战的讨论，具有综述和展望性质（满足标准3）。

**📖 中文摘要**

论文《Fin-R1: A Large Language Model for Financial Reasoning through Reinforcement Learning》介绍了Fin-R1，一个专为金融场景设计的推理大语言模型。其开发采用了两阶段流程：首先构建高质量金融思维链数据集，然后通过监督微调和强化学习进行训练，显著提升了模型解决复杂金融推理任务的能力。尽管该模型针对金融领域，但其方法论——构建领域特定高质量数据、结合SFT和RL来增强领域大模型的复杂推理能力——为构建“化学大模型”（例如，用于化学反应预测、谱图解析或合成规划）提供了一个清晰的范例和技术路线图。论文中关于处理碎片化数据源、提升推理过程透明度和可迁移性的挑战，也与化学大模型面临的挑战相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, general-purpose large language models (LLMs) such as GPT, Gemini, Claude, and DeepSeek have advanced at an unprecedented pace. Despite these achievements, their application to finance remains challenging, due to fragmented data sources, intransparent reasoning processes, and weak transferability to business applications. In response, we introduce Fin-R1, a reasoning LLM designed for financial scenarios. With a compact size of 7 billion parameters, Fin-R1 reduces deployment costs while addressing the aforementioned challenges. Its development follows a two-stage pipeline. First, we construct Fin-R1-Data, a high-quality financial dataset consisting of 60,091 chain-of-thought (CoT) samples, distilled and filtered from multiple authoritative benchmarks to ensure consistency and reliability. Second, we train Fin-R1 using Fin-R1-Data through supervised fine-tuning (SFT), followed by reinforcement learning (RL). This stage substantially improves the model's ability to solve complex financial reasoning tasks, yielding outputs that are both accurate and interpretable. Despite its relatively small parameter scale, Fin-R1 achieves competitive empirical performance across established financial benchmarks and demonstrates practical utility in compliance checking and robo-advisory. Our code is publicly available at this https URL , and has already attracted over 700 stars.

</details>

---

### 54. [Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability](https://arxiv.org/abs/2505.03530)

**基本信息**

- 🔗 arXiv: [`2505.03530`](https://arxiv.org/abs/2505.03530)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03530.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型（VAE）的机制可解释性框架，这直接适用于理解和解释用于分子生成或谱图生成的化学领域生成模型，与“化学大模型”和“质谱结构推理”中涉及的生成建模高度相关。

**📖 中文摘要**

论文《Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability》为变分自编码器的机制可解释性引入了一个全面的因果干预框架。该研究开发了技术来识别和分析VAE中的“电路模式”，研究语义因素如何通过网络层进行编码、处理和分离。该方法在具有已知因果关系的合成数据集和标准解纠缠基准上进行了应用。对于“化学大模型”和“质谱结构推理”，生成模型（如VAE、扩散模型）常被用于分子生成、谱图生成或分子-谱图联合建模。理解这些生成模型的内部工作机制，对于确保其生成的分子结构或谱图预测的可靠性、可控性以及实现定向优化至关重要。该论文提供的框架和工具可直接应用于化学领域生成模型的机制解释。

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

满足标准2：论文提出的逐步检索增强推理框架RAISE，作为一种提升大模型科学推理能力的工具，可被应用于“化学大模型”和“质谱结构推理”任务中，用于集成外部化学知识库（如PubChem、质谱数据库），进行更准确和可靠的多步推理。

**📖 中文摘要**

论文《RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval》提出了RAISE，一个逐步检索增强的框架，用于提升大语言模型在科学推理任务上的表现。RAISE通过问题分解、逻辑查询生成和逻辑检索三个步骤，从开放语料库中检索逻辑相关的文档。论文指出，RAISE检索到的文档不仅在领域知识上相似，而且在逻辑上更相关，从而在科学推理基准上持续优于其他基线。科学推理是“化学大模型”和“质谱结构推理”的核心能力之一。该论文提出的检索增强推理框架，为解决化学推理中需要结合领域知识（如反应规则、光谱数据库）和进行多步逻辑推导的挑战，提供了有力的方法论和工具思路。

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

满足标准1：论文的核心研究内容是多模态（图与图像）融合学习框架，这直接适用于“化学大模型”中处理分子的多模态表示（如图、序列、谱图图像），与化学信息学的多模态学习需求高度相关。

**📖 中文摘要**

论文《Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning》提出了一个多模态融合学习框架，用于解决机器人任务规划中的广义旅行商问题。该框架利用图和图像两种表示来捕捉问题的互补方面，并学习一个能够实时生成高质量任务规划方案的策略。虽然应用场景是机器人学，但其核心技术创新在于多模态（图+图像）融合学习。在化学信息学中，分子可以同时用图（分子图）和图像（分子结构式、谱图）表示。因此，该论文提出的多模态融合学习方法，对于开发能够同时处理分子多种表示的“化学大模型”（例如，联合理解分子图、3D结构和质谱/红外谱图像）具有重要的借鉴意义。

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

满足标准1和2：论文的核心是基于LLM智能体的信息结构化框架，这可直接应用于化学信息学中的信息提取任务（如从文献提取反应数据），为“化学大模型”提供数据处理工具（满足标准2）。同时，其方法也涉及大模型在特定领域的复杂任务应用（满足标准1）。

**📖 中文摘要**

论文《Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes》提出了一个由大语言模型智能体驱动的端到端框架，用于将自由形式的临床笔记转化为结构化的FHIR医疗资源。该框架利用LLM智能体、代码执行和医学术语数据库工具，旨在遵守FHIR文档模式并实现从非结构化文本到结构化资源的转换。虽然领域是医疗，但其核心是LLM智能体在复杂信息结构化任务中的应用。在化学信息学中，类似的任务广泛存在，例如从科学文献中自动提取化学反应信息、实验步骤、化合物性质并转化为结构化数据库（如JSON-LD、RDF），或从质谱解析报告中提取化合物标识和碎片信息。该论文的智能体框架为自动化这些化学信息提取和结构化任务提供了可参考的架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

For clinical data integration and healthcare services, the HL7 FHIR standard has established itself as a desirable format for interoperability between complex health data. Previous attempts at automating the translation from free-form clinical notes into structured FHIR resources address narrowly defined tasks and rely on modular approaches or LLMs with instruction tuning and constrained decoding. As those solutions frequently suffer from limited generalizability and structural inconformity, we propose an end-to-end framework powered by LLM agents, code execution, and healthcare terminology database tools to address these issues. Our solution, called Infherno, is designed to adhere to the FHIR document schema and competes well with a human baseline in predicting FHIR resources from unstructured text. The implementation features a front end for custom and synthetic data and both local and proprietary models, supporting clinical data integration processes and interoperability across institutions. Gemini 2.5-Pro excels in our evaluation on synthetic and clinical datasets, yet ambiguity and feasibility of collecting ground-truth data remain open problems.

</details>

---

### 58. [GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM](https://arxiv.org/abs/2507.13323)

**基本信息**

- 🔗 arXiv: [`2507.13323`](https://arxiv.org/abs/2507.13323)
- 👥 作者: Kyeongjin Ahn, Sungwon Han, Seungeon Lee 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.13323.pdf)

**💡 相关性分析**

满足标准2：论文提出的利用LLM进行特征工程和权重约束的少样本回归框架，作为一种数据分析和建模工具，可被应用于化学信息学中的少样本学习问题，例如小数据下的分子性质预测或谱图解析，为相关研究提供方法资源。

**📖 中文摘要**

论文《GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM》提出了GeoReg模型，该模型整合了卫星图像和网络地理空间信息等多种数据源，用于估计社会经济指标。其方法利用大语言模型的先验知识来解决标记数据稀缺的问题，语言模型充当数据工程师，提取信息特征以在少样本设置下实现有效估计。具体来说，模型获取数据特征与目标指标之间的上下文关系，并对它们的相关性进行分类。在化学信息学中，同样面临数据稀缺问题（如某些类别化合物的性质数据少）。该论文提出的利用LLM作为特征工程师、结合领域知识进行约束回归的方法，为在数据有限的化学领域（如预测新型材料的性质、小样本下的谱图-结构关联）开发预测模型提供了新颖的思路和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Socio-economic indicators like regional GDP, population, and education levels, are crucial to shaping policy decisions and fostering sustainable development. This research introduces GeoReg a regression model that integrates diverse data sources, including satellite imagery and web-based geospatial information, to estimate these indicators even for data-scarce regions such as developing countries. Our approach leverages the prior knowledge of large language model to address the scarcity of labeled data, with the language model functioning as a data engineer by extracting informative features to enable effective estimation in few-shot settings. Specifically, our model obtains contextual relationships between data features and the target indicator, categorizing their correlations as positive, negative, mixed, or irrelevant. These features are then fed into the linear estimator with tailored weight constraints for each category. To capture nonlinear patterns, the model also identifies meaningful feature interactions and integrates them, along with nonlinear transformations. Experiments across three countries at different stages of development demonstrate that our model outperforms baselines in estimating socio-economic indicators, even for low-income countries with limited data availability.

</details>

---

### 59. [All-in-One Slider for Attribute Manipulation in Diffusion Models](https://arxiv.org/abs/2508.19195)

**基本信息**

- 🔗 arXiv: [`2508.19195`](https://arxiv.org/abs/2508.19195)
- 👥 作者: Weixin Ye, Hongguang Zhu, Wei Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.19195.pdf)

**💡 相关性分析**

满足标准2：论文提出的All-in-One滑块模块，作为一种对扩散模型生成内容进行属性操控的通用工具，可被集成到化学领域的扩散模型中，用于可控分子生成或谱图条件化生成，为“化学大模型”和“质谱结构推理”提供重要的模型控制和优化工具。

**📖 中文摘要**

论文《All-in-One Slider for Attribute Manipulation in Diffusion Models》提出了一种轻量级的“All-in-One”滑块模块，用于在扩散模型中对生成图像的属性进行精细、连续的操控。该模块将文本嵌入空间分解为稀疏的、有语义意义的属性方向，训练后可作为通用滑块，支持对各种属性的可解释控制，并支持属性组合和零样本属性操作。在化学领域，扩散模型已用于分子生成和优化。该论文的方法为化学扩散模型（如用于分子生成或反应预测的模型）提供了强大的后处理和控制工具，使得研究人员能够通过直观的“滑块”交互，连续地调整生成分子的特定属性（如极性、溶解度、活性），或引导模型生成具有特定光谱特征（如质谱碎片峰）的分子结构，这对于“化学大模型”的可控生成和“质谱结构推理”的逆向设计具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Text-to-image (T2I) diffusion models have made significant strides in generating high-quality images. However, progressively manipulating certain attributes of generated images to meet the desired user expectations remains challenging, particularly for content with rich details, such as human faces. Some studies have attempted to address this by training slider modules. However, they follow a **One-for-One** manner, where an independent slider is trained for each attribute, requiring additional training whenever a new attribute is introduced. This not only results in parameter redundancy accumulated by sliders but also restricts the flexibility of practical applications and the scalability of attribute manipulation. To address this issue, we introduce the **All-in-On** Slider, a lightweight module that decomposes the text embedding space into sparse, semantically meaningful attribute directions. Once trained, it functions as a general-purpose slider, enabling interpretable and fine-grained continuous control over various attributes. Moreover, by recombining the learned directions, the All-in-One Slider supports the composition of multiple attributes and zero-shot manipulation of unseen attributes (e.g., races and celebrities). Extensive experiments demonstrate that our method enables accurate and scalable attribute manipulation, achieving notable improvements compared to previous methods. Furthermore, our method can be extended to integrate with the inversion framework to perform attribute manipulation on real images, broadening its applicability to various real-world scenarios. The code is available on [our project]( this https URL ) page.

</details>

---

### 60. [CausalARC: Abstract Reasoning with Causal World Models](https://arxiv.org/abs/2509.03636)

**基本信息**

- 🔗 arXiv: [`2509.03636`](https://arxiv.org/abs/2509.03636)
- 👥 作者: Jacqueline Maasch, John Kalantari, Kia Khezeli
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.03636.pdf)

**💡 相关性分析**

满足标准2和3：论文提出的CausalARC平台是一个用于评估因果推理的数据集和基准（满足标准2）。同时，它专注于因果推理这一高级推理形式，为评估和开发具有因果推理能力的“化学大模型”提供了重要的讨论框架和展望方向（满足标准3）。

**📖 中文摘要**

论文《CausalARC: Abstract Reasoning with Causal World Models》介绍了CausalARC，一个用于评估AI在低数据和分布外情况下推理能力的实验平台。该平台模仿抽象与推理语料库，每个推理任务都从一个完全指定的因果世界模型中采样，并以结构因果模型的形式正式表达。平台提供观察性、干预性和反事实性的反馈作为少样本上下文学习演示。论文将其用于大语言模型的四种评估设置，包括反事实推理、程序合成和因果发现。对于“化学大模型”和“质谱结构推理”，因果推理能力至关重要，例如理解反应条件（干预）如何影响产物分布，或根据碎片模式（观察）反推断裂机理（反事实）。CausalARC提供的因果推理评估框架和任务，可以直接用于评估和提升化学大模型在复杂、数据稀缺的化学推理任务中的因果理解能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

On-the-fly reasoning often requires adaptation to novel problems under limited data and distribution shift. This work introduces CausalARC: an experimental testbed for AI reasoning in low-data and out-of-distribution regimes, modeled after the Abstraction and Reasoning Corpus (ARC). Each CausalARC reasoning task is sampled from a fully specified causal world model, formally expressed as a structural causal model. Principled data augmentations provide observational, interventional, and counterfactual feedback about the world model in the form of few-shot, in-context learning demonstrations. As a proof-of-concept, we illustrate the use of CausalARC for four language model evaluation settings: (1) abstract reasoning with test-time training, (2) counterfactual reasoning with in-context learning, (3) program synthesis, and (4) causal discovery with logical reasoning. Within- and between-model performance varied heavily across tasks, indicating room for significant improvement in language model reasoning.

</details>

---

### 61. [Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning](https://arxiv.org/abs/2509.08759)

**基本信息**

- 🔗 arXiv: [`2509.08759`](https://arxiv.org/abs/2509.08759)
- 👥 作者: Mominul Rubel, Adam Meyers, Gabriel Nicolosi
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.08759.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种新型的、基于傅里叶级数的神经网络架构FLM，这为科学机器学习（包括化学领域）提供了新的模型构建思路，可直接应用于需要频域表示的化学问题（如光谱预测与解析），与“化学大模型”和“质谱结构推理”中的模型架构创新相关。

**📖 中文摘要**

论文《Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning》介绍了傅里叶学习机，一种设计用于表示多维非调和傅里叶级数的神经网络架构。FLM使用具有余弦激活函数的前馈结构，将级数的频率、振幅和相移作为可训练参数进行学习。该设计使模型能够创建适应周期和非周期函数的问题特定谱基。论文在包括偏微分方程和最优控制问题在内的多个科学计算问题上评估了FLM的性能。在化学信息学和计算化学中，许多问题涉及周期或振荡行为（如分子振动光谱、量子化学波函数、周期性材料结构）。FLM作为一种基于傅里叶基的神经网络，为建模这些具有内在频域特征的化学现象提供了新的、可能更高效和可解释的架构选择，与开发用于谱图分析或量子性质预测的“化学大模型”相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Fourier Learning Machine (FLM), a neural network (NN) architecture designed to represent a multidimensional nonharmonic Fourier series. The FLM uses a simple feedforward structure with cosine activation functions to learn the frequencies, amplitudes, and phase shifts of the series as trainable parameters. This design allows the model to create a problem-specific spectral basis adaptable to both periodic and nonperiodic functions. Unlike previous Fourier-inspired NN models, the FLM is the first architecture able to represent a multidimensional Fourier series with a complete set of basis functions in separable form, doing so by using a standard Multilayer Perceptron-like architecture. A one-to-one correspondence between the Fourier coefficients and amplitudes and phase-shifts is demonstrated, allowing for the translation between a full, separable basis form and the cosine phase-shifted one. Additionally, we evaluate the performance of FLMs on several scientific computing problems, including benchmark Partial Differential Equations (PDEs) and a family of Optimal Control Problems (OCPs). Computational experiments show that the performance of FLMs is comparable, and often superior, to that of established architectures like SIREN and vanilla feedforward NNs.

</details>

---

### 62. [Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?](https://arxiv.org/abs/2512.19980)

**基本信息**

- 🔗 arXiv: [`2512.19980`](https://arxiv.org/abs/2512.19980)
- 👥 作者: Zhe Yin, Xiaodong Gu, Beijun Shen
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.19980.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大语言模型（LLMs）的内部工作机制和可解释性进行分析，这属于“化学大模型”主题中模型构建与理解的方法论范畴。

**📖 中文摘要**

本文研究了代码大语言模型（Code LLMs）在神经元层面的可解释性。作者针对编程语言的形式化、层次化和可执行性特点，对Llama-3.1-8B和Qwen2.5-Coder-32B等模型进行了实证分析。研究发现，模型中存在针对特定编程语言（如C++、Java、Python）的专用神经元，以及一个支持通用代码生成的通用神经元子集。此外，模型的底层主要编码语言特定的语法，而中间层则捕获跨语言的语义抽象，成为“概念层”。这项工作通过神经元引导的微调、基于概念层嵌入的克隆检测以及概念层引导的代码摘要迁移等任务，展示了神经元级分析在理解和提升代码大模型能力方面的实用性。该研究直接关联“化学大模型”主题，因为它探索了大语言模型（作为大模型的一种）的内部工作机制和可解释性，这对于理解和构建化学领域的专用大模型具有方法论上的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Code language models excel on code intelligence tasks, yet their internal interpretability is underexplored. Existing neuron interpretability techniques from NLP are suboptimal for source code due to programming languages formal, hierarchical, and executable nature. We empirically investigate code LLMs at the neuron level, localizing language-specific neurons (selectively responsive to one language) and concept layers (feed-forward layers encoding language-agnostic code representations). We analyze Llama-3.1-8B and Qwen2.5-Coder-32B on multilingual inputs in C++, Java, Python, Go, and JavaScript, measuring neuron selectivity and layerwise contributions during generation. We find (1) neurons specialized for individual languages alongside a universal subset supporting general-purpose generation; and (2) lower layers mainly encode language-specific syntax, while middle layers capture semantic abstractions shared across languages, emerging as concept layers. We demonstrate utility on three tasks: neuron-guided fine-tuning for code generation, clone detection via concept-layer embeddings, and concept-layer-guided transfer for code summarization, each yielding consistent gains in multilingual settings.

</details>

---

### 63. [Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer](https://arxiv.org/abs/2601.05770)

**基本信息**

- 🔗 arXiv: [`2601.05770`](https://arxiv.org/abs/2601.05770)
- 👥 作者: Yifan Zhang, Wei Bi, Kechi Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.05770.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一种新型Transformer架构（离散Transformer），旨在从模型中提取可解释的算法。这直接关联“化学大模型”主题中关于模型可解释性、符号推理以及领域专用模型构建的研究方向。

**📖 中文摘要**

本文提出了“离散Transformer”（Discrete Transformer）架构，旨在弥合连续表示与离散符号逻辑之间的鸿沟。该框架通过温度退火采样注入离散性，并有效利用假设检验和符号回归来提取人类可读的程序。其目标是直接从在算法任务上训练的模型中合成可执行程序，实现无需依赖人工编写代码的算法发现。作者表明，该架构的归纳偏置可以对合成程序进行细粒度控制，从而将离散Transformer确立为一个用于免演示算法发现和Transformer可解释性的鲁棒框架。这项工作与“化学大模型”主题高度相关，因为它专注于从复杂模型中提取可解释的、符号化的算法，这对于构建能够进行可解释推理（如化学结构推理）的领域大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithm extraction aims to synthesize executable programs directly from models trained on algorithmic tasks, enabling de novo algorithm discovery without relying on human-written code. However, applying this paradigm to Transformer is hindered by representation entanglement (e.g., superposition), where entangled features encoded in overlapping directions obstruct the recovery of symbolic expressions. We propose the Discrete Transformer, an architecture explicitly designed to bridge the gap between continuous representations and discrete symbolic logic. By injecting discreteness through temperature-annealed sampling, our framework effectively leverages hypothesis testing and symbolic regression to extract human-readable programs. Empirically, the Discrete Transformer achieves performance comparable to RNN-based methods while extending interpretability to continuous variable domains, and the annealing dynamics exhibit a clear exploration-to-exploitation transition. Finally, we show that architectural inductive biases provide fine-grained control over synthesized programs, establishing the Discrete Transformer as a robust framework for demonstration-free algorithm discovery and Transformer interpretability.

</details>

---

### 64. [DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI](https://arxiv.org/abs/2601.06134)

**基本信息**

- 🔗 arXiv: [`2601.06134`](https://arxiv.org/abs/2601.06134)
- 👥 作者: Jiquan Wang, Sha Zhao, Yangxuan Zhou 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.06134.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为神经科学领域构建一个融合领域先验知识的基础模型（DeeperBrain）。这直接对应于“化学大模型”主题，即探讨如何为化学等特定科学领域构建专用的大模型或基础模型。

**📖 中文摘要**

本文提出了DeeperBrain，一个基于神经科学先验知识的脑电图（EEG）基础模型。该模型将领域特定的归纳偏置整合到其模型设计和学习目标中，旨在实现通用的脑机接口（BCI）。架构上，它包含了模拟空间混合的容积传导感知通道编码和捕获振荡的动态感知时间编码。预训练采用双目标策略，结合掩码EEG重建和神经动力学统计预测。论文的核心是构建一个能够学习通用神经表征的基础模型。这项工作与“化学大模型”主题在方法论上平行，都属于为特定科学领域（神经科学 vs. 化学）构建具有领域知识嵌入的专用基础模型/大模型。其模型设计思路（融入领域先验、多目标预训练）对化学信息学中构建类似模型具有借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalography (EEG) foundation models hold significant promise for universal Brain-Computer Interfaces (BCIs). However, existing approaches often rely on end-to-end fine-tuning and exhibit limited efficacy under frozen-probing protocols, lacking the intrinsic universality required for broad generalization. This limitation stems from adapting general-purpose sequence architectures that overlook the biophysical and dynamical principles of neural activity. To bridge this gap, we propose DeeperBrain, a neuro-grounded foundation model integrating domain-specific inductive biases into its model design and learning objectives. Architecturally, DeeperBrain incorporates a volume conduction-aware channel encoding to model spatial mixing via 3D geometry, and a neurodynamics-aware temporal encoding capturing slow adaptations using oscillatory and exponential bases. For pretraining, we introduce a dual-objective strategy combining Masked EEG Reconstruction (MER) for local fidelity and Neurodynamics Statistics Prediction (NSP). NSP enforces alignment with macroscopic brain states by predicting interpretable order parameters, including spectral power, functional connectivity, cross-frequency coupling, and dynamic complexity. Extensive experiments demonstrate that DeeperBrain achieves state-of-the-art or highly competitive performance under end-to-end fine-tuning. Crucially, it maintains superior efficacy under a rigorous frozen-probing protocol, verifying that embedding neuroscientific first principles endows learned representations with the intrinsic universality essential for universal BCI. The code will be publicly available.

</details>

---

### 65. [GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models](https://arxiv.org/abs/2601.07632)

**基本信息**

- 🔗 arXiv: [`2601.07632`](https://arxiv.org/abs/2601.07632)
- 👥 作者: Zhankai Ye, Bofan Li, Yukai Jin 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.07632.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过几何对齐（正交性约束）来改善多模态（运动与语言）表征的联合学习与推理。这种方法论可以迁移到“质谱结构推理”问题中，用于对齐质谱特征空间与分子结构空间，从而提升推理性能。

**📖 中文摘要**

本文提出了GeoMotionGPT，一个用于运动理解和大语言模型运动-语言推理的新框架。针对现有方法将运动量化与语义嵌入学习解耦、导致运动空间几何与嵌入空间对齐不佳的问题，该框架通过在运动码本和LLM嵌入空间上显式强制执行正交性，确保它们的关系结构自然相互映射。具体方法包括使用可微分训练的解码器量化器、保持正交性的稀疏投影，以及两阶段正交正则化计划。这项工作虽然针对运动理解，但其核心创新点——通过几何对齐（正交性）来改善模态（这里是运动与语言）之间的表征对齐和推理能力——与“化学大模型”和“质谱结构推理”主题高度相关。在质谱结构推理中，如何将质谱数据（一种几何/拓扑结构）与分子结构（另一种几何/拓扑结构）进行有效对齐和联合推理是一个核心挑战，本论文的方法论提供了有价值的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete motion tokenization has recently enabled Large Language Models (LLMs) to serve as versatile backbones for motion understanding and motion-language reasoning. However, existing pipelines typically decouple motion quantization from semantic embedding learning, linking them solely via token IDs. This approach fails to effectively align the intrinsic geometry of the motion space with the embedding space, thereby hindering the LLM's capacity for nuanced motion reasoning. We argue that alignment is most effective when both modalities share a unified geometric basis. Therefore, instead of forcing the LLM to reconstruct the complex geometry among motion tokens from scratch, we present a novel framework that explicitly enforces orthogonality on both the motion codebook and the LLM embedding space, ensuring that their relational structures naturally mirror each other. Specifically, we employ a decoder-only quantizer with Gumbel-Softmax for differentiable training and balanced codebook usage. To bridge the modalities, we use a sparse projection that maps motion codes into the LLM embedding space while preserving orthogonality. Finally, a two-stage orthonormal regularization schedule enforces soft constraints during tokenizer training and LLM fine-tuning to maintain geometric alignment without hindering semantic adaptation. Extensive experiments show that our framework improves the aggregated Average by 22.4% over the strongest baseline on HumanML3D and by 14.4% on KIT-ML, while ablations confirm the effectiveness of the tokenizer, projection, and regularization designs.

</details>

---

### 66. [Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity](https://arxiv.org/abs/2601.18032)

**基本信息**

- 🔗 arXiv: [`2601.18032`](https://arxiv.org/abs/2601.18032)
- 👥 作者: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18032.pdf)

**💡 相关性分析**

满足标准1和标准2：论文主要研究内容是利用预训练的聚合物表示（化学大模型）进行材料性能预测，属于化学大模型的核心应用。同时，论文构建并公开了高质量的数据集，为相关研究提供了数据资源。

**📖 中文摘要**

本文聚焦于软高介电常数弹性体的开发，这是一个化学信息学中的材料发现与设计问题。论文的核心贡献在于构建了一个高质量的丙烯酸酯基介电弹性体数据集，并提出了一个多模态学习框架。该框架利用大规模预训练的聚合物表示（即化学大模型）来迁移化学和结构知识，从而在数据稀缺的情况下实现对介电和机械性能的准确预测。这项工作直接提供了用于材料发现的化学大模型应用案例和数据集资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggregating experimental results from the past decade. Building on this dataset, we propose a multimodal learning framework leveraging large-scale pretrained polymer representations. These pretrained embeddings transfer chemical and structural knowledge from vast polymer corpora, enabling accurate few-shot prediction of dielectric and mechanical properties and accelerating data-efficient discovery of soft high-$k$ dielectric elastomers. Our data and implementation are publicly available at: this https URL

</details>

---

### 67. [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](https://arxiv.org/abs/2603.03686)

**基本信息**

- 🔗 arXiv: [`2603.03686`](https://arxiv.org/abs/2603.03686)
- 👥 作者: Jiangyu Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03686.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个用于自动化化学配方设计的神经符号框架，其中涉及多智能体规划和推理，属于化学大模型在材料科学和化学信息学中的核心应用。

**📖 中文摘要**

本文提出了AI4S-SDS，一个用于自动化化学配方设计的神经符号框架。该框架集成了多智能体协作和定制的蒙特卡洛树搜索引擎，旨在解决化学信息学中高维组合空间的导航问题。论文的核心是开发一个闭环系统，通过结合符号推理和物理可行性（通过可微物理引擎），在热力学约束下优化连续混合比例。这项工作代表了化学大模型（通过多智能体规划和推理）在科学发现（如光刻胶配方设计）中的具体应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.

</details>

---

### 68. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是开发一种用于材料发现与优化的新型深度学习模型（CliqueFlowmer），属于化学大模型/生成模型在材料科学中的应用。同时，论文开源了代码，为社区提供了工具资源。

**📖 中文摘要**

本文提出了CliqueFlowmer，一种基于离线模型优化的计算材料发现技术。该方法将目标材料属性的直接优化融合到生成过程中，旨在克服传统生成模型在探索材料空间有吸引力区域方面的不足。CliqueFlowmer结合了基于团的模型优化、Transformer和流生成等最新进展，专门用于材料优化问题。这项工作直接针对化学信息学中的核心挑战——材料发现与优化，并提供了开源代码以支持相关研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 69. [A Unified View of Drifting and Score-Based Models](https://arxiv.org/abs/2603.07514)

**基本信息**

- 🔗 arXiv: [`2603.07514`](https://arxiv.org/abs/2603.07514)
- 👥 作者: Chieh-Hsin Lai, Bac Nguyen, Naoki Murata 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07514.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从分数匹配的角度统一漂移模型和扩散模型，这属于生成模型的基础理论，而生成模型是构建化学大模型（用于分子生成、性质预测等）的关键组成部分。

**📖 中文摘要**

本文从理论角度统一了漂移模型和基于分数的模型（如扩散模型）。论文的核心贡献在于证明，对于高斯核，漂移模型的总体均值漂移场恰好等于高斯平滑后的数据分布与模型分布之间的分数差异。这一恒等式源于Tweedie公式，它建立了高斯平滑密度的分数与相应条件均值之间的联系。这意味着基于高斯核的漂移本质上是在平滑分布上的一种分数匹配式目标。这项工作为理解生成模型（包括可能用于分子生成的扩散模型）提供了统一的理论视角，与构建化学大模型的基础理论相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drifting models train one-step generators by optimizing a mean-shift discrepancy induced by a kernel between the data and model distributions, with Laplace kernels used by default in practice. At each point, this discrepancy compares the kernel-weighted displacement toward nearby data samples with the corresponding displacement toward nearby model samples, yielding a transport direction for generated samples. In this paper, we make its relationship to the score-matching principle behind diffusion models precise by showing that drifting admits a score-based formulation on kernel-smoothed distributions. For Gaussian kernels, the population mean-shift field coincides with the score difference between the Gaussian-smoothed data and model distributions. This identity follows from Tweedie's formula, which links the score of a Gaussian-smoothed density to the corresponding conditional mean, and implies that Gaussian-kernel drifting is exactly a score-matching-style objective on smoothed distributions. It also clarifies the connection to Distribution Matching Distillation (DMD): both methods use score-mismatch transport directions, but drifting realizes the score signal nonparametrically from kernel neighborhoods, whereas DMD uses a pretrained diffusion teacher. Beyond Gaussians, we derive an exact decomposition for general radial kernels, and for the Laplace kernel we prove rigorous error bounds showing that drifting remains an accurate proxy for score matching in low-temperature and high-dimensional regimes.

</details>

---

### 70. [Nonparametric Variational Differential Privacy via Embedding Parameter Clipping](https://arxiv.org/abs/2603.09583)

**基本信息**

- 🔗 arXiv: [`2603.09583`](https://arxiv.org/abs/2603.09583)
- 👥 作者: Dina El Zein, Shashi Kumar, James Henderson
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09583.pdf)

**💡 相关性分析**

满足标准1：论文主要研究内容是为语言模型（包括可能用于化学文本或分子表示的大模型）提供隐私保护框架，属于大模型安全性和可靠性研究的一部分，与化学信息学中部署可信模型相关。

**📖 中文摘要**

本文研究了非参数变分差分隐私框架，该框架建立在非参数变分信息瓶颈的基础上，用于构建隐私保护的语言模型。论文针对学习到的潜在表示可能漂移到高信息内容区域从而导致隐私保障差和训练数值不稳定的问题，提出了一种基于原理的参数裁剪策略。该方法从最小化Rényi散度上界的目标中推导出来，产生了对后验均值、方差和混合权重参数的具体约束。这项工作涉及保护语言模型（可作为化学大模型的基础）隐私的技术，与构建安全、可靠的化学信息学模型相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The nonparametric variational information bottleneck (NVIB) provides the foundation for nonparametric variational differential privacy (NVDP), a framework for building privacy-preserving language models. However, the learned latent representations can drift into regions with high information content, leading to poor privacy guarantees, but also low utility due to numerical instability during training. In this work, we introduce a principled parameter clipping strategy to directly address this issue. Our method is mathematically derived from the objective of minimizing the Rényi Divergence (RD) upper bound, yielding specific, theoretically grounded constraints on the posterior mean, variance, and mixture weight parameters. We apply our technique to an NVIB based model and empirically compare it against an unconstrained baseline. Our findings demonstrate that the clipped model consistently achieves tighter RD bounds, implying stronger privacy, while simultaneously attaining higher performance on several downstream tasks. This work presents a simple yet effective method for improving the privacy-utility trade-off in variational models, making them more robust and practical.

</details>

---

### 71. [Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining](https://arxiv.org/abs/2603.11103)

**基本信息**

- 🔗 arXiv: [`2603.11103`](https://arxiv.org/abs/2603.11103)
- 👥 作者: Zhiyuan Zeng, Yichi Zhang, Yong Shan 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11103.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的预训练范式，旨在通过重建智能体轨迹来增强LLM的深度推理和规划能力。这种能力对于化学信息学中复杂的任务（如逆合成分析、反应预测）至关重要，因此与开发更强大的化学领域大模型直接相关。

**📖 中文摘要**

本文提出了一种通过重建进行理解的新范式，用于大型语言模型的预训练。作者认为，标准的预训练数据（静态软件仓库）只代表了复杂智力过程的终端状态，抽象掉了中间的规划、调试和迭代细化步骤。为了弥补这一差距，他们引入了一个框架，通过多智能体模拟合成这些潜在的智能体轨迹（规划、推理和调试步骤）。该过程以源仓库的结构现实（例如依赖图和文件层次结构）为基础，以确保保真度。这项工作旨在增强LLM的深度、长视野推理能力，这对于复杂任务（如化学合成规划或分子设计）至关重要，因此与构建更强大的化学领域大模型相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have achieved remarkable success in code generation, they often struggle with the deep, long-horizon reasoning required for complex software engineering. We attribute this limitation to the nature of standard pre-training data: static software repositories represent only the terminal state of an intricate intellectual process, abstracting away the intermediate planning, debugging, and iterative refinement. To bridge this gap, we propose a novel paradigm: understanding via reconstruction. We hypothesize that reverse-engineering the latent agentic trajectories -- the planning, reasoning, and debugging steps -- behind static repositories provides a far richer supervision signal than raw code alone. To operationalize this, we introduce a framework that synthesizes these trajectories using a multi-agent simulation. This process is grounded in the structural realities of the source repositories (e.g., dependency graphs and file hierarchies) to ensure fidelity. Furthermore, to guarantee the logical rigor of the synthetic data, we employ a search-based optimization technique that iteratively refines the Chain-of-Thought (CoT) reasoning to maximize the likelihood of the ground-truth code. Empirical results demonstrate that continuous pre-training on these reconstructed trajectories significantly enhances Llama-3-8B's performance across diverse benchmarks, including long-context understanding, coding proficiency, and agentic capabilities.

</details>

---

### 72. [To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation](https://arxiv.org/abs/2603.15159)

**基本信息**

- 🔗 arXiv: [`2603.15159`](https://arxiv.org/abs/2603.15159)
- 👥 作者: Yitong Zhang, Chengze Li, Ruize Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15159.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是教导LLM使用特定API，这是一种提升模型在专业领域（如化学信息学）工具使用能力的方法。同时，论文提出的基准测试和方法论为相关研究提供了工具和思路。

**📖 中文摘要**

本文提出了PriCoder，一种通过自动合成数据来教导大型语言模型调用私有库API的方法。该方法将私有库数据合成建模为图的构建，并交替使用两个图算子：渐进图演化（提高数据多样性）和多维图剪枝（提高数据质量）。论文构建了两个基于新发布库的基准测试来支持严格评估。实验表明，PriCoder显著提高了面向私有库的代码生成能力。虽然主要针对代码生成，但该方法论（通过合成数据教导模型使用特定领域API）可以推广到化学信息学领域，例如教导模型使用化学信息学工具包（如RDKit）的API进行分子操作和分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability. Our code and benchmarks are publicly available at this https URL .

</details>

---

### 73. [Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences](https://arxiv.org/abs/2603.16313)

**基本信息**

- 🔗 arXiv: [`2603.16313`](https://arxiv.org/abs/2603.16313)
- 👥 作者: Hugo Math
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16313.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容围绕利用大语言模型（LLMs）对高维、结构化的序列数据进行建模、预测和因果推理，这与“化学大模型”主题中利用大模型处理化学数据（如分子序列、光谱）的核心思想高度一致。

**📖 中文摘要**

这篇论文提出了一种用于高维事件序列（如汽车诊断故障码）的统一框架，该框架将事件序列建模、因果发现和大语言模型（LLMs）整合在一起。论文的核心是将诊断序列视为一种可以建模、预测和解释的语言。这直接与【化学大模型】的主题相关，因为它展示了如何将LLMs应用于结构化、高维的科学或工程数据（类似于化学信息学中的分子序列或质谱数据）进行推理和模式发现。论文中引入的基于Transformer的架构和多智能体系统用于自动合成布尔规则，也体现了大模型在复杂推理任务中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>

---

### 74. [Network and Device Level Cyber Deception for Contested Environments Using RL and LLMs](https://arxiv.org/abs/2603.17272)

**基本信息**

- 🔗 arXiv: [`2603.17272`](https://arxiv.org/abs/2603.17272)
- 👥 作者: Abhijeet Sahu, Shuva Paul, Richard Macwan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17272.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大语言模型（LLMs）与强化学习的融合，以解决复杂的动态决策问题。这种方法论与开发用于化学信息学或质谱分析任务的智能模型（化学大模型）在技术层面上是相关的。

**📖 中文摘要**

这篇论文综述了在网络和设备级别构建网络欺骗策略的各种基于人工智能的解决方案，特别关注利用大语言模型（LLMs）和强化学习（RL）的融合来最优地学习这些策略。论文的核心是探讨如何利用LLMs来增强网络欺骗的动态性和成本效益。虽然应用领域是网络安全，但其方法论——即融合LLMs与RL来解决复杂的、动态的决策问题——与构建和优化“化学大模型”或用于“质谱结构推理”的智能系统在技术路径上具有相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cyber deception assists in increasing the attacker's budget in reconnaissance or any early phases of threat intrusions. In the past, numerous methods of cyber deception have been adopted, such as IP address randomization, the creation of honeypots and honeynets mimicking an actual set of services, and networks deployed within an enterprise or operational technology(OT) network. These types of strategies follow naive approaches of recreating services that are expensive and that need a lot of human intervention. The advent of cloud services and other automations of containerized applications, such as Kubernetes, makes cyber defense easier. Yet, there remains a lot of potential to improve the accuracy of these deception strategies and to make them cost-effective using artificial intelligence (AI)-based solutions by making the deception more dynamic. Hence, in this work, we review various AI-based solutions in building network- and device-level cyber deception methods in contested environments. Specifically, we focus on leveraging the fusion of large language models (LLMs) and reinforcement learning(RL) in optimally learning these cyber deception strategies and validating the efficacy of such strategies in some stealthy attacks against OT systems in the literature.

</details>

---

### 75. [Cell-cell Communication Inference and Analysis: Biological Mechanisms, Computational Approaches, and Future Opportunities](https://arxiv.org/abs/2512.03497)

**基本信息**

- 🔗 arXiv: [`2512.03497`](https://arxiv.org/abs/2512.03497)
- 👥 作者: Xiangzheng Cheng, Haili Huang, Ye Su 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03497.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对从复杂生物数据中推断相互作用的计算方法的综述，其涵盖的模型框架、推理策略和挑战与“质谱结构推理”领域面临的问题（从高维数据中推断结构）高度相似，提供了重要的相关讨论和跨领域见解。

**📖 中文摘要**

这篇论文是一篇关于从单细胞和空间组学数据中推断和分析细胞间通信（CCC）的计算方法的综述。它系统性地介绍了超过140种计算方法，涵盖了方法学框架和生物学问题的多样性。虽然主题是生物信息学，但其核心——开发计算模型来从复杂的、高维的生物学数据中推断相互作用和机制——与化学信息学中从质谱等数据中推断分子结构的任务在方法论和精神上高度平行。论文对计算方法的全面概述为相关领域（如质谱结构推理）提供了可借鉴的模型框架和算法思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In multicellular organisms, cells coordinate their activities through cell-cell communication (CCC), which is crucial for development, tissue homeostasis, and disease progression. Recent advances in single-cell and spatial omics technologies provide unprecedented opportunities to systematically infer and analyze CCC from these omics data, either by integrating prior knowledge of ligand-receptor interactions (LRIs) or through de novo approaches. A variety of computational methods have been developed, focusing on methodological innovations, accurate modeling of complex signaling mechanisms, and investigation of broader biological questions. These advances have greatly enhanced our ability to analyze CCC and generate biological hypotheses. Here, we introduce the biological mechanisms and modeling strategies of CCC, and provide a focused overview of more than 140 computational methods for inferring CCC from single-cell and spatial transcriptomic data, emphasizing the diversity in methodological frameworks and biological questions. Finally, we discuss the current challenges and future opportunities in this rapidly evolving field, and summarize available methods in an interactive online resource ( this https URL ) to facilitate more efficient method comparison and selection.

</details>

---

### 76. [Generalization of Long-Range Machine Learning Potentials in Complex Chemical Spaces](https://arxiv.org/abs/2512.10989)

**基本信息**

- 🔗 arXiv: [`2512.10989`](https://arxiv.org/abs/2512.10989)
- 👥 作者: Michal Sanocki, Julija Zavadlav
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10989.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕机器学习原子间势（MLIPs）在复杂化学空间中的泛化问题，这是构建高性能“化学大模型”用于分子模拟和性质预测的关键挑战。论文提出的评估框架和方法对相关研究具有直接参考价值。

**📖 中文摘要**

这篇论文系统地评估了不同具有长程修正的机器学习原子间势（MLIPs）架构在多样化化学空间中的泛化能力。研究强调了长程建模对于实现可泛化MLIPs的重要性，并引入了有偏的训练-测试分割策略来严格评估模型在化学空间不同区域的性能。这项工作直接针对“化学大模型”中的一个核心挑战：如何开发能够在广阔且复杂的化学空间中保持准确性和可转移性的机器学习模型。论文的发现和框架为构建更稳健、可泛化的化学性质预测和分子模拟大模型提供了重要指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vastness of chemical space makes generalization a central challenge in the development of machine learning interatomic potentials (MLIPs). While MLIPs could enable large-scale atomistic simulations with near-quantum accuracy, their usefulness is often limited by poor transferability to out-of-distribution samples. Here, we systematically evaluate different MLIP architectures with long-range corrections across diverse chemical spaces and show that such schemes are essential, not only for improving in-distribution performance but, more importantly, for enabling significant gains in transferability to unseen regions of chemical space. To enable a more rigorous benchmarking, we introduce biased train-test splitting strategies, which explicitly test the model performance in significantly different regions of chemical space. Together, our findings highlight the importance of long-range modeling for achieving generalizable MLIPs and provide a framework for diagnosing systematic failures across chemical space. Although we demonstrate our methodology on metal-organic frameworks, it is broadly applicable to other materials, offering insights into the design of more robust and transferable MLIPs.

</details>

---

### 77. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准3：论文包含对“化学大模型”未来发展的重要讨论和展望，特别是深入探讨了机器学习、高性能计算和量子计算的融合如何解决化学模拟中的精度与可扩展性瓶颈，属于相关主题的前瞻性分析。

**📖 中文摘要**

这篇论文展望了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何彻底改变药物发现。它明确指出，机器学习基础模型（如FeNNix-Bio1）能够实现量子精度的模拟，但其数据生成受限于经典计算。论文提出，高性能量子计算（HPQC）将成为量子化学数据的终极加速器，从而实现真正的化学精度。这一论述直接位于“化学大模型”发展的前沿，探讨了如何利用最先进的计算范式（包括量子计算）来赋能和加速下一代化学与药物发现模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

## 📊 数据统计
- 累计运行天数：43
- 累计论文数量：3098

## 📝 历史记录

> 暂无历史数据

