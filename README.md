# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-22 12:36:59

## 📅 2026-03-22 (今日最新)

**相关论文数：69**

### 1. [MolRGen: A Training and Evaluation Setting for De Novo Molecular Generation with Reasonning Models](https://arxiv.org/abs/2603.18256)

**基本信息**

- 🔗 arXiv: [`2603.18256`](https://arxiv.org/abs/2603.18256)
- 👥 作者: Philippe Formont, Maxime Darrin, Ismail Ben Ayed 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18256.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用基于推理的大语言模型进行化学分子生成（化学大模型的应用）。

**📖 中文摘要**

本文介绍了MolRGen，一个用于训练和评估基于推理的大语言模型（LLMs）进行从头分子生成的大规模基准和数据集。该工作旨在弥合当前方法在监督需求上的差距，这些方法通常依赖于已知属性修饰的分子对，而这在需要优化期望分数而无需事先了解高分候选分子的从头生成场景中是不可用的。MolRGen提出了一个用于评估和训练从头分子生成和属性预测模型的设置，并引入了一种新颖的多样性感知top-k分数，以同时捕获生成分子的质量和多样性。作者展示了该设置可用于训练LLMs进行分子生成，他们使用强化学习训练了一个240亿参数的LLM，并详细分析了其性能和局限性。这项工作直接针对化学信息学中的“化学大模型”主题，特别是利用推理LLMs进行分子设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in reasoning-based large language models (LLMs) have demonstrated substantial improvements in complex problem-solving tasks. Motivated by these advances, several works have explored the application of reasoning LLMs to drug discovery and molecular design. However, most existing approaches either focus on evaluation or rely on training setups that require ground-truth labels, such as molecule pairs with known property modifications. Such supervision is unavailable in \textit{de novo} molecular generation, where the objective is to generate novel molecules that optimize a desirability score without prior knowledge of high-scoring candidates. To bridge this gap, we introduce MolRGen, a large-scale benchmark and dataset for training and evaluating reasoning-based LLMs on \textit{de novo} molecular generation. Our contributions are threefold. First, we propose a setting to evaluate and train models for \textit{de novo} molecular generation and property prediction. Second, we introduce a novel diversity-aware top-$k$ score that captures both the quality and diversity of generated molecules. Third, we show our setting can be used to train LLMs for molecular generation, training a 24B LLM with reinforcement learning, and we provide a detailed analysis of its performance and limitations.

</details>

---

### 2. [Path-Constrained Mixture-of-Experts](https://arxiv.org/abs/2603.18297)

**基本信息**

- 🔗 arXiv: [`2603.18297`](https://arxiv.org/abs/2603.18297)
- 👥 作者: Zijin Gu, Tatiana Likhomanenko, Vimal Thilak 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18297.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕从质谱数据中进行分子结构推理（质谱结构推理）。

**📖 中文摘要**

本文提出了FlowMS，这是首个用于谱图条件从头分子生成的离散流匹配框架。该框架通过概率空间中的迭代精炼生成分子图，同时强制执行化学式约束，并基于预训练的公式Transformer编码器提供的谱图嵌入进行条件生成。FlowMS在NPLIB1基准测试的6个指标中的5个上实现了最先进的性能，包括9.15%的top-1准确率（相对于DiffMS有9.7%的相对改进）和7.96的top-10 MCES（相对于MS-BART有4.2%的改进）。这项工作直接解决了质谱分析中的一个核心挑战——从质谱图中进行从头结构解析，属于“质谱结构推理”主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse Mixture-of-Experts (MoE) architectures enable efficient scaling by activating only a subset of parameters for each input. However, conventional MoE routing selects each layer's experts independently, creating N^L possible expert paths -- for N experts across L layers. This far exceeds typical training set sizes, leading to statistical inefficiency as the model may not learn meaningful structure over such a vast path space. To constrain it, we propose \pathmoe, which shares router parameters across consecutive layers. Experiments on 0.9B and 16B parameter models demonstrate consistent improvements on perplexity and downstream tasks over independent routing, while eliminating the need for auxiliary load balancing losses. Analysis reveals that tokens following the same path naturally cluster by linguistic function, with \pathmoe{} producing more concentrated groups, better cross-layer consistency, and greater robustness to routing perturbations. These results offer a new perspective for understanding MoE architectures through the lens of expert paths.

</details>

---

### 3. [Towards Interpretable Framework for Neural Audio Codecs via Sparse Autoencoders: A Case Study on Accent Information](https://arxiv.org/abs/2603.18359)

**基本信息**

- 🔗 arXiv: [`2603.18359`](https://arxiv.org/abs/2603.18359)
- 👥 作者: Shih-Heng Wang, Tiantian Feng, Aditya Kommineni 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18359.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（使用稀疏自编码器进行模型表示的可解释性分析）与理解和解释“化学大模型”的内部机制这一主题高度相关。

**📖 中文摘要**

本文研究了神经音频编解码器（NACs）如何编码语言和副语言信息（如口音）的问题，并采用稀疏自编码器（SAEs）将密集的NAC表示分解为稀疏、可解释的激活。研究重点是一个具有挑战性的副语言属性——口音，并提出了一个量化NAC可解释性的框架。作者评估了四种NAC模型在16种SAE配置下的表现，使用相对性能指数进行比较。结果表明，声学导向的NAC主要通过稀疏表示的激活幅度编码口音信息，而语音导向的NAC则更依赖激活位置。这项工作虽然主要关注音频，但其核心方法论——使用稀疏自编码器等可解释AI技术来理解和分解复杂模型（如NACs）的内部表示——与化学信息学中理解“化学大模型”内部工作机制的研究目标高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural Audio Codecs (NACs) are widely adopted in modern speech systems, yet how they encode linguistic and paralinguistic information remains unclear. Improving the interpretability of NAC representations is critical for understanding and deploying them in sensitive applications. Hence, we employ Sparse Autoencoders (SAEs) to decompose dense NAC representations into sparse, interpretable activations. In this work, we focus on a challenging paralinguistic attribute-accent-and propose a framework to quantify NAC interpretability. We evaluate four NAC models under 16 SAE configurations using a relative performance index. Our results show that DAC and SpeechTokenizer achieve the highest interpretability. We further reveal that acoustic-oriented NACs encode accent information primarily in activation magnitudes of sparse representations, whereas phonetic-oriented NACs rely more on activation positions, and that low-bitrate EnCodec variants show higher interpretability.

</details>

---

### 4. [Synthetic Data Generation for Training Diversified Commonsense Reasoning Models](https://arxiv.org/abs/2603.18361)

**基本信息**

- 🔗 arXiv: [`2603.18361`](https://arxiv.org/abs/2603.18361)
- 👥 作者: Tianhui Zhang, Bei Peng, Danushka Bollegala
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18361.pdf)

**💡 相关性分析**

满足标准2：论文提供了用于训练多样化常识推理模型（可视为一种特定的大模型应用）的合成数据集生成方法。

**📖 中文摘要**

本文提出了一种两阶段方法，创建了首个用于多样化生成式常识推理（GCR）的合成数据集CommonSyn。由于标注成本高昂，现有的GCR数据集仅涵盖有限的常识场景。为了解决训练资源缺口，作者的方法能够生成大规模、高质量的多样化常识训练数据。在大型语言模型（LLMs）上微调后，模型在生成多样性和质量上均优于基线模型以及在人工标注数据集上微调的模型。这项工作直接涉及利用合成数据来增强和训练大语言模型，以提升其在多样化常识推理任务上的能力，属于“化学大模型”领域外围但相关的基础技术（数据生成与模型训练）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Conversational agents are required to respond to their users not only with high quality (i.e. commonsense bearing) responses, but also considering multiple plausible alternative scenarios, reflecting the diversity in their responses. Despite the growing need to train diverse commonsense generators, the progress of this line of work has been significantly hindered by the lack of large-scale high-quality diverse commonsense training datasets. Due to the high annotation costs, existing Generative Commonsense Reasoning (GCR) datasets are created using a small number of human annotators, covering only a narrow set of commonsense scenarios. To address this training resource gap, we propose a two-stage method to create the first-ever synthetic dataset CommonSyn for diversified (GCR). The model fine-tuned on our synthetic data jointly increase both generation diversity and quality compared with vanilla models and the model fine-tuned on human-crafted dataset across different size Large Language Models (LLMs)

</details>

---

### 5. [Mathematical Foundations of Deep Learning](https://arxiv.org/abs/2603.18387)

**基本信息**

- 🔗 arXiv: [`2603.18387`](https://arxiv.org/abs/2603.18387)
- 👥 作者: Xiaojing Ye
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18387.pdf)

**💡 相关性分析**

满足标准3：论文（书籍草稿）是对深度学习数学基础的综述，其中包含生成模型等重要章节，这些内容是理解和构建“化学大模型”的理论基石。

**📖 中文摘要**

这份书籍草稿提供了对现代深度学习数学原理的全面而严谨的论述。书籍涵盖了核心理论主题，从深度神经网络的近似能力、最优控制和强化学习的理论与算法（与深度学习技术相结合），到推动当今人工智能进步的当代生成模型。虽然不专门针对化学，但该书系统地阐述了深度学习（包括生成模型）的数学基础，这些是构建和理解“化学大模型”（如用于分子生成的扩散模型或流匹配模型）所必需的理论工具。对于从事化学信息学和质谱分析中复杂模型开发的研究人员来说，这是一份重要的理论基础资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This draft book offers a comprehensive and rigorous treatment of the mathematical principles underlying modern deep learning. The book spans core theoretical topics, from the approximation capabilities of deep neural networks, the theory and algorithms of optimal control and reinforcement learning integrated with deep learning techniques, to contemporary generative models that drive today's advances in artificial intelligence.

</details>

---

### 6. [From Snapshots to Symphonies: The Evolution of Protein Prediction from Static Structures to Generative Dynamics and Multimodal Interactions](https://arxiv.org/abs/2603.18505)

**基本信息**

- 🔗 arXiv: [`2603.18505`](https://arxiv.org/abs/2603.18505)
- 👥 作者: Jingzhi Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18505.pdf)

**💡 相关性分析**

满足标准3：论文是针对蛋白质科学中AI模型（包括生成模型和结构推理模型）演进的一篇综合性综述，包含了对化学大模型和结构推理相关主题的重要讨论和展望。

**📖 中文摘要**

这篇综述论文系统地审视了人工智能驱动的蛋白质科学范式的转变，涵盖了从静态结构预测到动态构象集合和复杂生物分子相互作用建模的演进。论文重点讨论了五个相互关联的维度，其中特别强调了生成式框架（包括扩散模型和流匹配）在捕获与热力学集合一致的构象分布方面的应用。这直接与“化学大模型”的主题相关，因为它深入探讨了用于模拟复杂化学/生物分子系统（如蛋白质）动态行为的生成式AI模型。此外，论文还讨论了用于蛋白质-配体、蛋白质-核酸和蛋白质-蛋白质复合物等异质相互作用预测的模型，这涉及到从结构数据（可视为一种特殊形式的“质谱结构推理”的扩展，即从相互作用数据推断分子结构和功能）中进行推理。因此，该论文是对化学和生物分子AI模型（包括生成模型和结构推理模型）当前进展和未来方向的全面展望。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The protein folding problem has been fundamentally transformed by artificial intelligence, evolving from static structure prediction toward the modeling of dynamic conformational ensembles and complex biomolecular interactions. This review systematically examines the paradigm shift in AI driven protein science across five interconnected dimensions: unified multimodal representations that integrate sequences, geometries, and textual knowledge; refinement of static prediction through MSA free architectures and all atom complex modeling; generative frameworks, including diffusion models and flow matching, that capture conformational distributions consistent with thermodynamic ensembles; prediction of heterogeneous interactions spanning protein ligand, protein nucleic acid, and protein protein complexes; and functional inference of fitness landscapes, mutational effects, and text guided property prediction. We critically analyze current bottlenecks, including data distribution biases, limited mechanistic interpretability, and the disconnect between geometric metrics and biophysical reality, while identifying future directions toward physically consistent generative models, multimodal foundation architectures, and experimental closed loop systems. This methodological transformation marks artificial intelligence's transition from a structural analysis tool into a universal simulator capable of understanding and ultimately rewriting the dynamic language of life.

</details>

---

### 7. [SINDy-KANs: Sparse identification of non-linear dynamics through Kolmogorov-Arnold networks](https://arxiv.org/abs/2603.18548)

**基本信息**

- 🔗 arXiv: [`2603.18548`](https://arxiv.org/abs/2603.18548)
- 👥 作者: Amanda A. Howard, Nicholas Zolman, Bruno Jacob 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18548.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发一种结合SINDy和KANs的新方法，用于从数据中发现可解释的符号方程（核心主题相关：化学系统的动力学建模与推理）。同时，该方法本身是一个可用于化学/质谱数据分析和模型构建的工具（数据资源/工具相关）。

**📖 中文摘要**

本文提出了SINDy-KANs方法，将稀疏识别非线性动力学（SINDy）与Kolmogorov-Arnold网络（KANs）相结合，用于从数据中发现符号方程。SINDy本身是一种从时间序列数据中学习稀疏、可解释微分方程模型的方法，广泛应用于物理、化学和生物系统的动力学建模。KANs是一种新型的、理论上更具可解释性的神经网络架构。SINDy-KANs在KAN的每个激活函数层面应用SINDy式的表示，旨在提高KAN表示的可解释性（稀疏性），同时保持深度KAN可能实现的函数组合能力。该方法应用于包括动力学系统在内的多个符号回归任务，展示了在不同系统中进行准确方程发现的能力。这项工作与“化学大模型”和“质谱结构推理”相关，因为它提供了一种从观测数据（例如，来自动力学实验或光谱时间序列）中学习可解释的化学系统模型的新框架。质谱数据解析和分子结构推理本质上可以视为从高维光谱数据中推断底层化学动力学或结构模型的问题，SINDy-KANs为此类推理任务提供了一种潜在的、可解释的机器学习工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Kolmogorov-Arnold networks (KANs) have arisen as a potential way to enhance the interpretability of machine learning. However, solutions learned by KANs are not necessarily interpretable, in the sense of being sparse or parsimonious. Sparse identification of nonlinear dynamics (SINDy) is a complementary approach that allows for learning sparse equations for dynamical systems from data; however, learned equations are limited by the library. In this work, we present SINDy-KANs, which simultaneously train a KAN and a SINDy-like representation to increase interpretability of KAN representations with SINDy applied at the level of each activation function, while maintaining the function compositions possible through deep KANs. We apply our method to a number of symbolic regression tasks, including dynamical systems, to show accurate equation discovery across a range of systems.

</details>

---

### 8. [CAPSUL: A Comprehensive Human Protein Benchmark for Subcellular Localization](https://arxiv.org/abs/2603.18571)

**基本信息**

- 🔗 arXiv: [`2603.18571`](https://arxiv.org/abs/2603.18571)
- 👥 作者: Yicheng Hu, Xinyu Lin, Shulin Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18571.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个包含蛋白质3D结构信息和亚细胞定位注释的综合基准数据集（CAPSUL），该资源可直接用于训练和评估化学/生物大模型在结构相关的推理任务（如亚细胞定位，可类比质谱数据解析）上的性能。

**📖 中文摘要**

本文介绍了CAPSUL，一个用于蛋白质亚细胞定位任务的新基准数据集。亚细胞定位是药物靶点识别和功能注释的关键生物学任务。该基准的独特之处在于，它首次整合了多样化的3D结构表示与由领域专家精心策划的细粒度亚细胞定位注释。作者评估了多种最先进的基于序列和基于结构的模型在该基准上的表现，展示了结构特征在此任务中的重要性。这项工作与“化学大模型”和“质谱结构推理”高度相关。首先，蛋白质的3D结构是其化学性质和功能的核心，基于结构的模型（如图神经网络、Transformer等）是当前化学和生物信息学中大模型的重要分支。其次，质谱技术（如空间转录组学、蛋白质组学）常被用于研究蛋白质的表达和定位，从质谱数据中推断蛋白质的亚细胞定位本身就是一个“结构推理”问题（从光谱信号推理生物空间分布）。CAPSUL基准为开发和应用能够处理3D结构信息的大模型（化学大模型）解决此类生物医学推理任务提供了高质量的数据资源和评估平台。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Subcellular localization is a crucial biological task for drug target identification and function annotation. Although it has been biologically realized that subcellular localization is closely associated with protein structure, no existing dataset offers comprehensive 3D structural information with detailed subcellular localization annotations, thus severely hindering the application of promising structure-based models on this task. To address this gap, we introduce a new benchmark called $\mathbf{CAPSUL}$, a $\mathbf{C}$omprehensive hum$\mathbf{A}$n $\mathbf{P}$rotein benchmark for $\mathbf{SU}$bcellular $\mathbf{L}$ocalization. It features a dataset that integrates diverse 3D structural representations with fine-grained subcellular localization annotations carefully curated by domain experts. We evaluate this benchmark using a variety of state-of-the-art sequence-based and structure-based models, showcasing the importance of involving structural features in this task. Furthermore, we explore reweighting and single-label classification strategies to facilitate future investigation on structure-based methods for this task. Lastly, we showcase the powerful interpretability of structure-based methods through a case study on the Golgi apparatus, where we discover a decisive localization pattern $\alpha$-helix from attention mechanisms, demonstrating the potential for bridging the gap with intuitive biological interpretability and paving the way for data-driven discoveries in cell biology.

</details>

---

### 9. [Elastic Weight Consolidation Done Right for Continual Learning](https://arxiv.org/abs/2603.18596)

**基本信息**

- 🔗 arXiv: [`2603.18596`](https://arxiv.org/abs/2603.18596)
- 👥 作者: Xuan Liu, Xiaobin Chang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18596.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕模型训练、优化和重要性估计方法展开。虽然未直接提及化学或质谱，但其对梯度、FIM和模型权重正则化的系统性分析，为构建和优化复杂的“化学大模型”提供了重要的方法论参考和理论基础。

**📖 中文摘要**

本文对持续学习中的权重正则化方法进行了系统性分析，重点关注了基于梯度的权重重要性估计。论文的核心是分析弹性权重巩固（EWC）及其变体在估计权重重要性时存在的根本性错位问题，并提出了Logits Reversal（LR）操作来修正EWC的重要性估计。虽然论文主要关注通用机器学习模型的持续学习，但其对梯度、Fisher信息矩阵（FIM）和权重重要性的系统性分析，为理解和改进任何基于梯度的模型（包括潜在的化学大模型）的训练和优化过程提供了理论基础和方法论。提出的LR操作作为一种简单有效的修改，可以防止梯度消失和冗余保护，这种优化思想可能迁移到化学大模型的训练中，以提高其学习效率和稳定性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Weight regularization methods in continual learning (CL) alleviate catastrophic forgetting by assessing and penalizing changes to important model weights. Elastic Weight Consolidation (EWC) is a foundational and widely used approach within this framework that estimates weight importance based on gradients. However, it has consistently shown suboptimal performance. In this paper, we conduct a systematic analysis of importance estimation in EWC from a gradient-based perspective. For the first time, we find that EWC's reliance on the Fisher Information Matrix (FIM) results in gradient vanishing and inaccurate importance estimation in certain scenarios. Our analysis also reveals that Memory Aware Synapses (MAS), a variant of EWC, imposes unnecessary constraints on parameters irrelevant to prior tasks, termed the redundant protection. Consequently, both EWC and its variants exhibit fundamental misalignments in estimating weight importance, leading to inferior performance. To tackle these issues, we propose the Logits Reversal (LR) operation, a simple yet effective modification that rectifies EWC's importance estimation. Specifically, reversing the logit values during the calculation of FIM can effectively prevent both gradient vanishing and redundant protection. Extensive experiments across various CL tasks and datasets show that the proposed method significantly outperforms existing EWC and its variants. Therefore, we refer to it as EWC Done Right (EWC-DR).

</details>

---

### 10. [myMNIST: Benchmark of PETNN, KAN, and Classical Deep Learning Models for Burmese Handwritten Digit Recognition](https://arxiv.org/abs/2603.18597)

**基本信息**

- 🔗 arXiv: [`2603.18597`](https://arxiv.org/abs/2603.18597)
- 👥 作者: Ye Kyaw Thu, Thazin Myint Oo, Thepchai Supnithi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18597.pdf)

**💡 相关性分析**

满足标准1：论文评估了物理启发的PETNN模型，这是一种受科学原理（物理学）启发的新型神经网络架构。这种“科学启发式”或“物理信息”的模型设计思路与“化学大模型”的构建理念高度相关，后者同样旨在将化学领域的先验知识（如分子力场、量子化学原理）嵌入到机器学习模型中。论文为这类模型的性能评估提供了方法论参考。

**📖 中文摘要**

本文对缅甸手写数字数据集myMNIST进行了系统性的基准测试，评估了包括经典深度学习模型、近期替代模型（如KAN）以及物理启发的PETNN变体在内的十一种架构。论文特别评估了PETNN（一种物理启发神经网络）在数字识别任务上的性能，发现其表现优异，紧随CNN之后，并超越了LSTM、GRU、Transformer和KAN变体。同时，论文还将PETNN与真正的基于能量的模型（JEM）进行了性能比较。这项工作为评估新兴架构（包括受物理或化学原理启发的模型）在特定任务上的表现建立了一个可复现的基准框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present the first systematic benchmark on myMNIST (formerly BHDD), a publicly available Burmese handwritten digit dataset important for Myanmar NLP/AI research. We evaluate eleven architectures spanning classical deep learning models (Multi-Layer Perceptron, Convolutional Neural Network, Long Short-Term Memory, Gated Recurrent Unit, Transformer), recent alternatives (FastKAN, EfficientKAN), an energy-based model (JEM), and physics-inspired PETNN variants (Sigmoid, GELU, SiLU). Using Precision, Recall, F1-Score, and Accuracy as evaluation metrics, our results show that the CNN remains a strong baseline, achieving the best overall scores (F1 = 0.9959, Accuracy = 0.9970). The PETNN (GELU) model closely follows (F1 = 0.9955, Accuracy = 0.9966), outperforming LSTM, GRU, Transformer, and KAN variants. JEM, representing energy-based modeling, performs competitively (F1 = 0.9944, Accuracy = 0.9958). KAN-based models (FastKAN, EfficientKAN) trail the top performers but provide a meaningful alternative baseline (Accuracy ~0.992). These findings (i) establish reproducible baselines for myMNIST across diverse modeling paradigms, (ii) highlight PETNN's strong performance relative to classical and Transformer-based models, and (iii) quantify the gap between energy-inspired PETNNs and a true energy-based model (JEM). We release this benchmark to facilitate future research on Myanmar digit recognition and to encourage broader evaluation of emerging architectures on regional scripts.

</details>

---

### 11. [GEAR: Geography-knowledge Enhanced Analog Recognition Framework in Extreme Environments](https://arxiv.org/abs/2603.18626)

**基本信息**

- 🔗 arXiv: [`2603.18626`](https://arxiv.org/abs/2603.18626)
- 👥 作者: Zelin Liu, Bocheng Li, Yuling Zhou 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18626.pdf)

**💡 相关性分析**

满足标准1：论文提出的MSG-Net是一种专门用于处理复杂结构关系（地形形态）并进行跨域关联的图神经网络方法。这种方法论与“质谱结构推理”任务高度相关，后者同样需要利用神经网络（尤其是图神经网络）从复杂的质谱信号中推理出分子的图结构。论文为结构推理任务提供了一种可借鉴的神经网络架构设计思路。

**📖 中文摘要**

本文提出了GEAR框架，用于从青藏高原高效检索与马里亚纳海沟结构同源的陆地类似物。该框架的核心创新之一是设计了一个基于地貌学指标的形态集成孪生图网络（MSG-Net）。论文使用MSG-Net提取的特征，发现了与生物数据的显著相关性，这为未来的生物分析提供了证据。虽然研究背景是地理学和生物学，但其核心方法——设计专门的图神经网络（MSG-Net）来处理具有复杂结构关系（如地形形态）的数据，并建立跨域（地形到生物）的关联——与“质谱结构推理”中利用图神经网络从质谱数据推断分子结构（另一种复杂的结构关系）的研究范式高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Mariana Trench and the Qinghai-Tibet Plateau exhibit significant similarities in geological origins and microbial metabolic functions. Given that deep-sea biological sampling faces prohibitive costs, recognizing structurally homologous terrestrial analogs of the Mariana Trench on the Qinghai-Tibet Plateau is of great significance. Yet, no existing model adequately addresses cross-domain topographic similarity retrieval, either neglecting geographical knowledge or sacrificing computational efficiency. To address these challenges, we present \underline{\textbf{G}}eography-knowledge \underline{\textbf{E}}nhanced \underline{\textbf{A}}nalog \underline{\textbf{R}}ecognition (\textbf{GEAR}) Framework, a three-stage pipeline designed to efficiently retrieve analogs from 2.5 million square kilometers of the Qinghai-Tibet Plateau: (1) Skeleton guided Screening and Clipping: Recognition of candidate valleys and initial screening based on size and linear morphological criteria. (2) Physics aware Filtering: The Topographic Waveform Comparator (TWC) and Morphological Texture Module (MTM) evaluate the waveform and texture and filter out inconsistent candidate valleys. (3) Graph based Fine Recognition: We design a \underline{\textbf{M}}orphology-integrated \underline{\textbf{S}}iamese \underline{\textbf{G}}raph \underline{\textbf{N}}etwork (\textbf{MSG-Net}) based on geomorphological metrics. Correspondingly, we release an expert-annotated topographic similarity dataset targeting tectonic collision zones. Experiments demonstrate the effectiveness of every stage. Besides, MSG-Net achieved an F1-Score 1.38 percentage points higher than the SOTA baseline. Using features extracted by MSG-Net, we discovered a significant correlation with biological data, providing evidence for future biological analysis.

</details>

---

### 12. [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660)

**基本信息**

- 🔗 arXiv: [`2603.18660`](https://arxiv.org/abs/2603.18660)
- 👥 作者: Peihang Wu, Zehong Chen, Lijian Xu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18660.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对多模态计算病理学的综述，其中包含了对自监督表示学习、令牌压缩（用于处理高维数据）以及多智能体推理机制等重要技术的深入讨论。这些技术对于构建能够处理高维、复杂科学数据（如质谱）的“化学大模型”或“结构推理模型”具有重要的参考价值和前瞻性指导意义。

**📖 中文摘要**

本文全面综述了多模态计算病理学的最新进展。论文系统分析了四个研究方向，其中第一个方向就是“全切片图像的自监督表示学习和结构感知的令牌压缩”。文章特别探讨了如何通过令牌压缩实现跨尺度建模，以及多智能体机制如何模拟病理学家在不同放大倍数下的“思维链”，以实现不确定性感知的证据融合。这篇综述深入讨论了在超高分辨率医学图像上，如何利用自监督学习、令牌压缩和高级推理机制来学习有效的表示并进行诊断，这些技术挑战和解决方案与处理复杂科学数据（如质谱或化学结构数据）有共通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Whole slide imaging (WSI) has transformed digital pathology by enabling computational analysis of gigapixel histopathology images. Recent foundation model advances have accelerated progress in computational pathology, facilitating joint reasoning across pathology images, clinical reports, and structured data. Despite this progress, challenges remain: the extreme resolution of WSIs creates computational hurdles for visual learning; limited expert annotations constrain supervised approaches; integrating multimodal information while preserving biological interpretability remains difficult; and the opacity of modeling ultra-long visual sequences hinders clinical transparency. This review comprehensively surveys recent advances in multimodal computational pathology. We systematically analyze four research directions: (1) self-supervised representation learning and structure-aware token compression for WSIs; (2) multimodal data generation and augmentation; (3) parameter-efficient adaptation and reasoning-enhanced few-shot learning; and (4) multi-agent collaborative reasoning for trustworthy diagnosis. We specifically examine how token compression enables cross-scale modeling and how multi-agent mechanisms simulate a pathologist's "Chain of Thought" across magnifications to achieve uncertainty-aware evidence fusion. Finally, we discuss open challenges and argue that future progress depends on unified multimodal frameworks integrating high-resolution visual data with clinical and biomedical knowledge to support interpretable and safe AI-assisted diagnosis.

</details>

---

### 13. [STEP: Scientific Time-Series Encoder Pretraining via Cross-Domain Distillation](https://arxiv.org/abs/2603.18688)

**基本信息**

- 🔗 arXiv: [`2603.18688`](https://arxiv.org/abs/2603.18688)
- 👥 作者: Chen Zhang, Liwei Liu, Jun Tao 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18688.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究内容是针对“科学时间序列”设计统一的表示学习框架，这与为化学数据（如质谱、分子序列）构建通用表示学习模型的“化学大模型”目标高度一致。2) 论文提出的STEP框架本身是一种用于科学数据表示学习的“工具”或“方法”，其跨域蒸馏、自适应分块等设计思想，可直接为化学信息学领域构建预训练模型提供技术参考和解决方案。

**📖 中文摘要**

本文提出了STEP框架，一个通过跨域蒸馏进行科学时间序列编码器预训练的框架。STEP旨在解决科学时间序列数据稀疏、异构且规模有限的问题，通过整合来自相关领域（如音频、通用时间序列、脑信号）的多个基础模型的知识，学习适用于科学信号的通用且可迁移的特征。该框架引入了自适应分块来处理极长序列，以及统计补偿方案来适应不同的数值尺度。论文在七个科学时间序列任务上进行了实验验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific time series are central to scientific AI but are typically sparse, highly heterogeneous, and limited in scale, making unified representation learning particularly challenging. Meanwhile, foundation models pretrained on relevant time series domains such as audio, general time series, and brain signals contain rich knowledge, but their applicability to scientific signals remains underexplored. In this paper, we investigate the transferability and complementarity of foundation models from relevant time series domains, and study how to effectively leverage them to build a unified encoder for scientific time series. We first systematically evaluate relevant foundation models, showing the effectiveness of knowledge transfer to scientific tasks and their complementary strengths. Based on this observation, we propose STEP, a Scientific Time Series Encoder Pretraining framework via cross domain distillation. STEP introduces adaptive patching to handle extreme-length sequences and a statistics compensation scheme to accommodate diverse numerical scales. It further leverages cross-domain distillation to integrate knowledge from multiple foundation models into a unified encoder. By combining complementary representations across different domains, STEP learns general-purpose and transferable features tailored for scientific signals. Experiments on seven scientific time series tasks demonstrate that STEP provides both an effective structure and an effective pretraining paradigm, taking a STEP toward scientific time series representation learning.

</details>

---

### 14. [WeNLEX: Weakly Supervised Natural Language Explanations for Multilabel Chest X-ray Classification](https://arxiv.org/abs/2603.18752)

**基本信息**

- 🔗 arXiv: [`2603.18752`](https://arxiv.org/abs/2603.18752)
- 👥 作者: Isabel Rio-Torto, Jaime S. Cardoso, Luís F. Teixeira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18752.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发能够为黑盒模型（深度学习分类器）生成忠实且合理的自然语言解释的方法。这种“可解释人工智能（XAI）”技术对于构建可信的“化学大模型”或“质谱结构推理”系统至关重要。例如，在质谱结构推理中，模型不仅需要预测分子结构，还需要提供其预测的推理依据或关键谱图特征，这与WeNLEX的目标高度相似。论文的方法论为化学AI模型的可解释性研究提供了参考。

**📖 中文摘要**

本文提出了WeNLEX，一个用于多标签胸部X光分类的弱监督自然语言解释生成模型。该模型通过确保从自然语言解释生成的图像与原始图像在黑盒模型特征空间中匹配来保证解释的忠实性，并通过与少量临床医生标注的解释数据库进行分布对齐来保持解释的合理性。论文在多个评估忠实性、可模拟性、多样性和合理性的指标上进行了验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Natural language explanations provide an inherently human-understandable way to explain black-box models, closely reflecting how radiologists convey their diagnoses in textual reports. Most works explicitly supervise the explanation generation process using datasets annotated with explanations. Thus, though plausible, the generated explanations are not faithful to the model's reasoning. In this work, we propose WeNLEX, a weakly supervised model for the generation of natural language explanations for multilabel chest X-ray classification. Faithfulness is ensured by matching images generated from their corresponding natural language explanations with original images, in the black-box model's feature space. Plausibility is maintained via distribution alignment with a small database of clinician-annotated explanations. We empirically demonstrate, through extensive validation on multiple metrics to assess faithfulness, simulatability, diversity, and plausibility, that WeNLEX is able to produce faithful and plausible explanations, using as little as 5 ground-truth explanations per diagnosis. Furthermore, WeNLEX can operate in both post-hoc and in-model settings. In the latter, i.e., when the multilabel classifier is trained together with the rest of the network, WeNLEX improves the classification AUC of the standalone classifier by 2.21%, thus showing that adding interpretability to the training process can actually increase the downstream task performance. Additionally, simply by changing the database, WeNLEX explanations are adaptable to any target audience, and we showcase this flexibility by training a layman version of WeNLEX, where explanations are simplified for non-medical users.

</details>

---

### 15. [Enhancing the Parameterization of Reservoir Properties for Data Assimilation Using Deep VAE-GAN](https://arxiv.org/abs/2603.18766)

**基本信息**

- 🔗 arXiv: [`2603.18766`](https://arxiv.org/abs/2603.18766)
- 👥 作者: Marcio Augusto Sampaio, Paulo Henrique Ranazzi, Martin Julian Blunt
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18766.pdf)

**💡 相关性分析**

满足标准1：论文核心研究内容是使用深度生成模型（VAE-GAN）对复杂的、非高斯分布的科学数据进行参数化和表示学习，以优化基于物理的模拟过程。这种利用生成模型学习科学数据底层分布并用于后续推理和优化的范式，与“化学大模型”中利用生成模型学习分子或材料空间分布，并用于性质预测或结构生成的思路完全一致。论文为在科学领域应用复杂的生成模型提供了具体案例和方法细节。

**📖 中文摘要**

本文提出将变分自编码器生成对抗网络（VAE-GAN）这一深度学习模型与集合平滑器多重数据同化（ESMDA）方法相结合，用于石油储层模拟中的历史拟合。该方法旨在对非高斯分布的储层属性（如渗透率）进行参数化，即将非高斯参数映射到高斯场进行更新，然后再映射回原始域。论文通过两个案例研究（一个分类案例，一个连续渗透率案例）验证了该方法能够同时获得高质量的储层描述（像GAN一样）和良好的生产曲线历史匹配（像VAE一样）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Currently, the methods called Iterative Ensemble Smoothers, especially the method called Ensemble Smoother with Multiple Data Assimilation (ESMDA) can be considered state-of-the-art for history matching in petroleum reservoir simulation. However, this approach has two important limitations: the use of an ensemble with finite size to represent the distributions and the Gaussian assumption in parameter and data uncertainties. This latter is particularly important because many reservoir properties have non-Gaussian distributions. Parameterization involves mapping non-Gaussian parameters to a Gaussian field before the update and then mapping them back to the original domain to forward the ensemble through the reservoir simulator. A promising approach to perform parameterization is through deep learning models. Recent studies have shown that Generative Adversarial Networks (GAN) performed poorly concerning data assimilation, but generated more geologically plausible realizations of the reservoir, while the Variational Autoencoder (VAE) performed better than the GAN in data assimilation, but generated less geologically realistic models. This work is innovative in combining the strengths of both to implement a deep learning model called Variational Autoencoder Generative Adversarial Network (VAE-GAN) integrated with ESMDA. The methodology was applied in two case studies, one case being categorical and the other with continuous values of permeability. Our findings demonstrate that by applying the VAE-GAN model we can obtain high quality reservoir descriptions (just like GANs) and a good history matching on the production curves (just like VAEs) simultaneously.

</details>

---

### 16. [Pore-scale modeling of capillary-driven binder migration during battery electrode drying](https://arxiv.org/abs/2603.18860)

**基本信息**

- 🔗 arXiv: [`2603.18860`](https://arxiv.org/abs/2603.18860)
- 👥 作者: Marcel Weichel, Martin Reder, Gerit Mühlberg 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18860.pdf)

**💡 相关性分析**

满足标准2：论文提出的孔隙尺度毛细管驱动粘合剂迁移模型，为化学大模型（特别是涉及多相传输和材料结构的模型）的开发和验证提供了物理机理明确的模拟框架和潜在的数据生成工具。

**📖 中文摘要**

本文提出了一种孔隙尺度连续介质模型，用于模拟钠离子电池硬碳电极干燥过程中的毛细管驱动粘合剂迁移。该研究通过空间分辨的微观结构模拟，揭示了颗粒尺寸、蒸发速率和表面张力对粘合剂分布均匀性的影响。这项工作为电极制造过程的优化提供了物理上一致的预测工具。虽然论文核心是电化学制造过程模拟，但其提出的毛细管驱动传输模型和微观结构效应分析，为化学信息学中复杂多相系统的建模提供了方法论和数据生成工具，可用于训练或验证化学大模型（特别是涉及流体传输和材料结构的模型）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sodium-ion batteries employing hard carbon electrodes are considered a drop-in technology for lithium-ion batteries. Electrode drying is a critical manufacturing step, as binder migration during pore emptying impacts the mechanical integrity and electrical performance of the electrode. Existing modeling approaches predominantly rely on the film shrinkage phase in a one dimensional way or neglect the capillary transport, resulting in a lack of physically consistent microstructure resolved predictions of binder migration. In this work, a spatially resolved pore scale continuum model is extended to explicitly describe capillary driven binder transport during pore emptying. The model is applied to hard carbon microstructures with varying mean particle diameters. The simulations reveal that smaller particle sizes lead to a more homogeneous binder distribution, whereas higher evaporation rates and increased surface tension promote stronger binder gradients. Variations in solvent viscosity show only a minor influence on binder migration, as long as no hydrophilic or hydrophobic behavior is present. Finally, the simulations demonstrate that an explicit description of capillary transport and microstructural effects is essential for accurately predicting binder migration and provides a basis for the targeted optimization of electrode drying processes.

</details>

---

### 17. [BVSIMC: Bayesian Variable Selection-Guided Inductive Matrix Completion for Improved and Interpretable Drug Discovery](https://arxiv.org/abs/2603.18957)

**基本信息**

- 🔗 arXiv: [`2603.18957`](https://arxiv.org/abs/2603.18957)
- 👥 作者: Sijian Fan, Liyan Xiong, Dayuan Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18957.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容直接围绕化学信息学中的关键问题——药物发现，提出了一种结合变量选择的新模型。同时，该方法通过利用化学和基因组侧信息进行预测，为化学大模型（特别是用于药物属性预测和关联推断的模型）提供了新的算法框架和可解释性工具。

**📖 中文摘要**

本文提出了一种贝叶斯变量选择引导的归纳矩阵补全（BVSIMC）方法，用于改进药物发现中的预测性能和可解释性。该方法通过从药物和疾病的侧信息（如化学性质和基因组信息）中进行变量选择，学习稀疏的潜在嵌入。研究在两个药物发现应用中得到验证：1) 结核分枝杆菌的药物耐药性预测；2) 计算药物重定位中的新药-疾病关联预测。BVSIMC在预测准确性上优于其他最先进的方法，并揭示了最具临床意义的侧信息特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in drug discovery have demonstrated that incorporating side information (e.g., chemical properties about drugs and genomic information about diseases) often greatly improves prediction performance. However, these side features can vary widely in relevance and are often noisy and high-dimensional. We propose Bayesian Variable Selection-Guided Inductive Matrix Completion (BVSIMC), a new Bayesian model that enables variable selection from side features in drug discovery. By learning sparse latent embeddings, BVSIMC improves both predictive accuracy and interpretability. We validate our method through simulation studies and two drug discovery applications: 1) prediction of drug resistance in Mycobacterium tuberculosis, and 2) prediction of new drug-disease associations in computational drug repositioning. On both synthetic and real data, BVSIMC outperforms several other state-of-the-art methods in terms of prediction. In our two real examples, BVSIMC further reveals the most clinically meaningful side features.

</details>

---

### 18. [Foundations of Schrödinger Bridges for Generative Modeling](https://arxiv.org/abs/2603.18992)

**基本信息**

- 🔗 arXiv: [`2603.18992`](https://arxiv.org/abs/2603.18992)
- 👥 作者: Sophia Tang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18992.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心内容是生成模型（包括扩散模型）的统一数学原理，这与构建“化学大模型”（尤其是基于扩散或流的分子生成模型）的理论基础直接相关。同时，论文具有综述和展望性质，系统性地梳理了生成模型的理论框架，为相关领域的研究提供了重要的理论讨论和方向指引。

**📖 中文摘要**

本文系统阐述了生成建模框架（如扩散模型、基于分数的模型和流匹配）背后的数学基础——薛定谔桥问题。它将生成过程视为在概率空间中连接先验分布和目标分布的最优随机桥问题。论文从最优传输、随机控制和路径空间优化等角度构建了薛定谔桥问题的数学工具包，并展示了其与现代生成建模的直接联系。这些构造产生了广义的、针对特定任务的计算方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

At the core of modern generative modeling frameworks, including diffusion models, score-based models, and flow matching, is the task of transforming a simple prior distribution into a complex target distribution through stochastic paths in probability space. Schrödinger bridges provide a unifying principle underlying these approaches, framing the problem as determining an optimal stochastic bridge between marginal distribution constraints with minimal-entropy deviations from a pre-defined reference process. This guide develops the mathematical foundations of the Schrödinger bridge problem, drawing on optimal transport, stochastic control, and path-space optimization, and focuses on its dynamic formulation with direct connections to modern generative modeling. We build a comprehensive toolkit for constructing Schrödinger bridges from first principles, and show how these constructions give rise to generalized and task-specific computational methods.

</details>

---

### 19. [Unleashing the Power of Simplicity: A Minimalist Strategy for State-of-the-Art Fingerprint Enhancement](https://arxiv.org/abs/2603.19004)

**基本信息**

- 🔗 arXiv: [`2603.19004`](https://arxiv.org/abs/2603.19004)
- 👥 作者: Raffaele Cappelli
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19004.pdf)

**💡 相关性分析**

满足标准2：论文提出的指纹图像增强方法，特别是其基于学习的方法和开源实现，为化学信息学和质谱分析领域提供了一个潜在的、可用于信号预处理或图像式谱图增强的工具或算法参考。虽然应用领域不同，但信号/图像增强的核心技术具有跨领域迁移的潜力。

**📖 中文摘要**

本文提出了一种极简主义的指纹增强方法，旨在提高指纹识别系统中关键点提取的准确性。论文引入了两种新方法：上下文过滤方法和基于学习的方法。这些方法在具有挑战性的潜指纹数据库上得到验证， consistently outperforms 复杂的现有方法，产生更清晰、更准确、噪声更少的图像。研究强调了简单性在实现高质量指纹增强中的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fingerprint recognition systems, which rely on the unique characteristics of human fingerprints, are essential in modern security and verification applications. Accurate minutiae extraction, a critical step in these systems, depends on the quality of fingerprint images. Despite recent improvements in fingerprint enhancement techniques, state-of-the-art methods often struggle with low-quality fingerprints and can be computationally demanding. This paper presents a minimalist approach to fingerprint enhancement, prioritizing simplicity and effectiveness. Two novel methods are introduced: a contextual filtering method and a learning-based method. These techniques consistently outperform complex state-of-the-art methods, producing clearer, more accurate, and less noisy images. The effectiveness of these methods is validated using a challenging latent fingerprint database. The open-source implementation of these techniques not only fosters reproducibility but also encourages further advancements in the field. The findings underscore the importance of simplicity in achieving high-quality fingerprint enhancement and suggest that future research should balance complexity and practical benefits.

</details>

---

### 20. [SHAPCA: Consistent and Interpretable Explanations for Machine Learning Models on Spectroscopy Data](https://arxiv.org/abs/2603.19141)

**基本信息**

- 🔗 arXiv: [`2603.19141`](https://arxiv.org/abs/2603.19141)
- 👥 作者: Mingxing Zhang, Nicola Rossberg, Simone Innocente 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19141.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种专门用于光谱数据分析的可解释机器学习流程（SHAPCA），这为化学信息学领域（质谱分析是光谱分析的一种）提供了可用于模型解释和分析的工具资源。

**📖 中文摘要**

本文提出了一种名为SHAPCA的可解释机器学习流程，用于分析光谱数据。该流程结合了主成分分析（PCA）进行降维和SHAP（Shapley Additive exPlanations）进行事后解释，旨在为化学和生物医学分析中的光谱数据集提供稳定、一致且可解释的模型预测解释。文章指出，光谱数据固有的高维度和强共线性对模型的可解释性构成了根本挑战，容易导致特征重要性在不同训练轮次中波动。SHAPCA框架通过将解释映射回原始输入空间，使从业者能够将预测与生物成分联系起来，从而从全局和局部两个角度进行分析。这项工作直接面向化学信息学领域（特别是光谱分析）的机器学习应用，解决了该领域模型可解释性的关键需求。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In recent years, machine learning models have been increasingly applied to spectroscopic datasets for chemical and biomedical analysis. For their successful adoption, particularly in clinical and safety-critical settings, professionals and researchers must be able to understand and trust the reasoning behind model predictions. However, the inherently high dimensionality and strong collinearity of spectroscopy data pose a fundamental challenge to model explainability. These properties not only complicate model training but also undermine the stability and consistency of explanations, leading to fluctuations in feature importance across repeated training runs. Feature extraction techniques have been used to reduce the input dimensionality; these new features hinder the connection between the prediction and the original signal. This study proposes SHAPCA, an explainable machine learning pipeline that combines Principal Component Analysis (for dimensionality reduction) and Shapely Additive exPlanations (for post hoc explanation) to provide explanations in the original input space, which a practitioner can interpret and link back to the biological components. The proposed framework enables analysis from both global and local perspectives, revealing the spectral bands that drive overall model behaviour as well as the instance-specific features that influence individual predictions. Numerical analysis demonstrated the interpretability of the results and greater consistency across different runs.

</details>

---

### 21. [Sparse Autoencoders Reveal Interpretable and Steerable Features in VLA Models](https://arxiv.org/abs/2603.19183)

**基本信息**

- 🔗 arXiv: [`2603.19183`](https://arxiv.org/abs/2603.19183)
- 👥 作者: Aiden Swann, Lachlain McGranahan, Hugo Buurmeijer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19183.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用机制可解释性技术（稀疏自编码器）来分析和理解视觉-语言-动作（VLA）模型的内部表征与泛化能力。VLA模型是化学大模型（特别是多模态大模型）在机器人领域的具体应用和延伸，其内部表征学习的研究对于理解大模型的工作原理具有普遍意义。

**📖 中文摘要**

本文研究了视觉-语言-动作（VLA）模型在机器人操作中的内部工作机制。作者应用机制可解释性技术，特别是稀疏自编码器（SAEs），来分析和理解VLA模型的内部表征。研究发现，大多数提取的SAE特征对应于特定训练演示的记忆序列，但也有一些特征对应于可解释、通用且可引导的运动基元和语义属性。作者提出了一个指标来根据特征是代表可泛化的可迁移基元还是特定情节的记忆来对特征进行分类。通过在LIBERO基准测试上的引导实验，验证了单个SAE特征可以因果性地影响机器人行为。这项工作为VLA模型能够跨任务和场景学习可泛化特征提供了首个机制性证据，并讨论了不同训练数据策略（如监督微调与在更大、更多样化数据集上训练）对特征泛化性的影响。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language-Action (VLA) models have emerged as a promising approach for general-purpose robot manipulation. However, their generalization is inconsistent: while these models can perform impressively in some settings, fine-tuned variants often fail on novel objects, scenes, and instructions. We apply mechanistic interpretability techniques to better understand the inner workings of VLA models. To probe internal representations, we train Sparse Autoencoders (SAEs) on hidden layer activations of the VLA. SAEs learn a sparse dictionary whose features act as a compact, interpretable basis for the model's computation. We find that the large majority of extracted SAE features correspond to memorized sequences from specific training demonstrations. However, some features correspond to interpretable, general, and steerable motion primitives and semantic properties, offering a promising glimpse toward VLA generalizability. We propose a metric to categorize features according to whether they represent generalizable transferable primitives or episode-specific memorization. We validate these findings through steering experiments on the LIBERO benchmark. We show that individual SAE features causally influence robot behavior. Steering general features induces behaviors consistent with their semantic meaning and can be applied across tasks and scenes. This work provides the first mechanistic evidence that VLAs can learn generalizable features across tasks and scenes. We observe that supervised fine-tuning on small robotics datasets disproportionately amplifies memorization. In contrast, training on larger, more diverse datasets (e.g., DROID) or using knowledge insulation promotes more general features. We provide an open-source codebase and user-friendly interface for activation collection, SAE training, and feature steering. Our project page is located at this http URL

</details>

---

### 22. [MIDST Challenge at SaTML 2025: Membership Inference over Diffusion-models-based Synthetic Tabular data](https://arxiv.org/abs/2603.19185)

**基本信息**

- 🔗 arXiv: [`2603.19185`](https://arxiv.org/abs/2603.19185)
- 👥 作者: Masoumeh Shafieinejad, Xi He, Mahshid Alinoori 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19185.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容围绕评估扩散模型（一种生成式大模型）生成的合成数据的隐私性，这直接关联到“化学大模型”在生成化学数据时可能面临的隐私和安全评估问题。同时，该挑战赛催生了新的攻击方法并建立了评估基准，为相关领域提供了工具和资源。

**📖 中文摘要**

本文介绍了MIDST挑战赛，该挑战赛旨在定量评估由扩散模型生成的合成表格数据的隐私增益，特别关注其对成员推理攻击（MIAs）的抵抗力。鉴于表格数据的异质性和复杂性，挑战赛探索了多种目标模型进行MIA，包括用于混合数据类型单表的扩散模型和具有互连约束的多关系表。MIDST挑战赛的一个关键成果是启发了针对这些目标扩散模型的新型黑盒和白盒MIA的开发，从而能够全面评估其隐私效力。该工作聚焦于扩散模型在生成合成数据时的隐私问题，虽然主要背景是表格数据，但其核心——评估生成模型（扩散模型）的隐私弹性——与构建和评估化学信息学中用于数据生成或增强的“化学大模型”所面临的挑战（如数据隐私、生成质量评估）在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic data is often perceived as a silver-bullet solution to data anonymization and privacy-preserving data publishing. Drawn from generative models like diffusion models, synthetic data is expected to preserve the statistical properties of the original dataset while remaining resilient to privacy attacks. Recent developments of diffusion models have been effective on a wide range of data types, but their privacy resilience, particularly for tabular formats, remains largely unexplored. MIDST challenge sought a quantitative evaluation of the privacy gain of synthetic tabular data generated by diffusion models, with a specific focus on its resistance to membership inference attacks (MIAs). Given the heterogeneity and complexity of tabular data, multiple target models were explored for MIAs, including diffusion models for single tables of mixed data types and multi-relational tables with interconnected constraints. MIDST inspired the development of novel black-box and white-box MIAs tailored to these target diffusion models as a key outcome, enabling a comprehensive evaluation of their privacy efficacy. The MIDST GitHub repository is available at this https URL

</details>

---

### 23. [RPiAE: A Representation-Pivoted Autoencoder Enhancing Both Image Generation and Editing](https://arxiv.org/abs/2603.19206)

**基本信息**

- 🔗 arXiv: [`2603.19206`](https://arxiv.org/abs/2603.19206)
- 👥 作者: Yue Gong, Hongyu Li, Shanyuan Liu 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19206.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进扩散模型的视觉表示学习与标记化方法（RPiAE）。这是构建和理解多模态大模型（可视为“化学大模型”在视觉模态上的技术基础）底层架构和表征能力的重要研究方向。

**📖 中文摘要**

本文提出了Representation-Pivoted AutoEncoder（RPiAE），一种基于表示的标记器，旨在同时改进图像生成和编辑。该方法针对潜在扩散模型中标记器的局限性，引入了一种训练策略（Representation-Pivot Regularization），使经过表示初始化的编码器能够在微调以进行重建的同时，保留预训练表示空间的语义结构。随后通过一个变分桥将潜在空间压缩为一个更紧凑的空间，以利于扩散建模。采用分阶段训练策略，依次优化生成可处理性和重建保真度目标。实验表明，RPiAE在文本到图像生成和图像编辑方面优于其他视觉标记器，同时在基于表示的标记器中提供了最佳的重建保真度。这项工作专注于改进扩散模型的视觉编码/标记化部分，这是构建高性能多模态大模型（包括可能的化学大模型）的关键组件之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models have become the dominant paradigm for image generation and editing, with latent diffusion models shifting denoising to a compact latent space for efficiency and scalability. Recent attempts to leverage pretrained visual representation models as tokenizer priors either align diffusion features to representation features or directly reuse representation encoders as frozen tokenizers. Although such approaches can improve generation metrics, they often suffer from limited reconstruction fidelity due to frozen encoders, which in turn degrades editing quality, as well as overly high-dimensional latents that make diffusion modeling difficult. To address these limitations, We propose Representation-Pivoted AutoEncoder, a representation-based tokenizer that improves both generation and editing. We introduce Representation-Pivot Regularization, a training strategy that enables a representation-initialized encoder to be fine-tuned for reconstruction while preserving the semantic structure of the pretrained representation space, followed by a variational bridge which compress latent space into a compact one for better diffusion modeling. We adopt an objective-decoupled stage-wise training strategy that sequentially optimizes generative tractability and reconstruction-fidelity objectives. Together, these components yield a tokenizer that preserves strong semantics, reconstructs faithfully, and produces latents with reduced diffusion modeling complexity. Experiments demonstrate that RPiAE outperforms other visual tokenizers on text-to-image generation and image editing, while delivering the best reconstruction fidelity among representation-based tokenizers.

</details>

---

### 24. [Generative Replica-Exchange: A Flow-based Framework for Accelerating Replica Exchange Simulations](https://arxiv.org/abs/2603.18076)

**基本信息**

- 🔗 arXiv: [`2603.18076`](https://arxiv.org/abs/2603.18076)
- 👥 作者: Shengjie Huang, Sijie Yang, Jianqiao Yi 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18076.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用深度生成模型（归一化流）来加速分子模拟采样。这直接属于化学信息学中利用机器学习/生成模型解决化学和分子科学问题的范畴，可视为一种面向化学领域的“大模型”应用。

**📖 中文摘要**

本文提出了一种生成式副本交换（GREX）方法，将深度生成模型（特别是归一化流）集成到副本交换分子动力学（REX）框架中，以加速分子模拟采样。该方法利用训练好的归一化流按需生成高温构型，并通过势能约束将其直接映射到目标分布，从而消除了对大量中间温度副本的需求，将生产模拟简化为目标温度下的单个副本。该方法在三个复杂度递增的基准系统上进行了验证，证明了其在分子模拟中的优越效率和实际适用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Replica exchange (REX) is one of the most widely used enhanced sampling methodologies, yet its efficiency is limited by the requirement for a large number of intermediate temperature replicas. Here we present Generative Replica Exchange (GREX), which integrates deep generative models into the REX framework to eliminate this temperature ladder. Drawing inspiration from reservoir replica exchange (res-REX), GREX utilizes trained normalizing flows to generate high-temperature configurations on demand and map them directly to the target distribution using the potential energy as a constraint, without requiring target-temperature training data. This approach reduces production simulations to a single replica at the target temperature while maintaining thermodynamic rigor through Metropolis exchange acceptance. We validate GREX on three benchmark systems of increasing complexity, highlighting its superior efficiency and practical applicability for molecular simulations.

</details>

---

### 25. [Tackling the Sign Problem in the Doped Hubbard Model with Normalizing Flows](https://arxiv.org/abs/2603.18205)

**基本信息**

- 🔗 arXiv: [`2603.18205`](https://arxiv.org/abs/2603.18205)
- 👥 作者: Dominic Schuh, Lena Funcke, Janik Kreit 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用归一化流（一种生成模型）来解决量子化学/凝聚态物理中具有挑战性的计算问题（哈伯德模型模拟）。这属于化学信息学和计算化学中利用先进机器学习模型（大模型）进行模拟和推理的范畴。

**📖 中文摘要**

本文研究了掺杂哈伯德模型在有限化学势下的模拟问题，该模型是理解掺杂关联系统的基石，但模拟受到符号问题的严重限制。作者扩展了在零掺杂（半填充）情况下使用归一化流的最新进展，通过引入退火方案实现遍历采样，将其应用于有限化学势情况。与在电荷基中采用的最先进的混合蒙特卡罗方法相比，该方法能准确再现精确对角化结果，同时将统计不确定性降低一个数量级，为模拟掺杂关联系统开辟了新途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Hubbard model at finite chemical potential is a cornerstone for understanding doped correlated systems, but simulations are severely limited by the sign problem. In the auxiliary-field formulation, the spin basis mitigates the sign problem, yet severe ergodicity issues have limited its use. We extend recent advances with normalizing flows at half-filling to finite chemical potential by introducing an annealing scheme enabling ergodic sampling. Compared to state-of-the-art hybrid Monte Carlo in the charge basis, our approach accurately reproduces exact diagonalization results while reducing statistical uncertainties by an order of magnitude, opening a new path for simulations of doped correlated systems.

</details>

---

### 26. [A Hybrid Conditional Diffusion-DeepONet Framework for High-Fidelity Stress Prediction in Hyperelastic Materials](https://arxiv.org/abs/2603.18225)

**基本信息**

- 🔗 arXiv: [`2603.18225`](https://arxiv.org/abs/2603.18225)
- 👥 作者: Purna Vindhya Kota, Meer Mehran Rashid, Somdatta Goswami 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18225.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种结合了条件扩散模型（cDDPM）和神经算子（DeepONet）的混合生成模型框架，用于解决材料科学中的物理场预测问题。这属于利用生成式人工智能（化学/材料领域的大模型）进行科学计算和推理的范畴。

**📖 中文摘要**

本文提出了一种混合条件扩散-DeepONet框架（cDDPM-DeepONet），用于超弹性材料中复杂微结构的高保真应力预测。该框架将应力形态与幅值解耦：一个基于UNet主干的条件去噪扩散概率模型（cDDPM）生成以几何和载荷为条件的归一化冯·米塞斯应力场；同时，一个改进的DeepONet预测全局缩放参数（最小和最大应力），从而重建全分辨率物理应力图。这种分离使扩散模型专注于空间结构，而算子网络校正全局幅值，减轻了光谱和缩放偏差。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting stress fields in hyperelastic materials with complex microstructures remains challenging for traditional deep learning surrogates, which struggle to capture both sharp stress concentrations and the wide dynamic range of stress magnitudes. Convolutional architectures such as UNet tend to oversmooth high-frequency gradients, while neural operators like DeepONet exhibit spectral bias and underpredict localized extremes. Diffusion models can recover fine-scale structure but often introduce low-frequency amplitude drift, degrading physical scaling. To address these limitations, we propose a hybrid surrogate framework, cDDPM-DeepONet, that decouples stress morphology from magnitude. A conditional denoising diffusion probabilistic model (cDDPM), built on a UNet backbone, generates normalized von Mises stress fields conditioned on geometry and loading. In parallel, a modified DeepONet predicts global scaling parameters (minimum and maximum stress), enabling reconstruction of full-resolution physical stress maps. This separation allows the diffusion model to focus on spatial structure while the operator network corrects global amplitude, mitigating spectral and scaling biases. We evaluate the framework on nonlinear hyperelastic datasets with single and multiple polygonal voids. The proposed model consistently outperforms UNet, DeepONet, and standalone cDDPM baselines by one to two orders of magnitude. Spectral analysis shows strong agreement with finite element solutions across all wavenumbers, preserving both global behavior and localized stress concentrations.

</details>

---

### 27. [Impact of automatic speech recognition quality on Alzheimer's disease detection from spontaneous speech: a reproducible benchmark study with lexical modeling and statistical validation](https://arxiv.org/abs/2603.18239)

**基本信息**

- 🔗 arXiv: [`2603.18239`](https://arxiv.org/abs/2603.18239)
- 👥 作者: Himadri Samanta
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18239.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和利用大规模预训练模型（Whisper ASR）的输出（转录本）作为特征，来构建和优化下游的疾病检测模型。这涉及使用大模型（Whisper）作为特征提取器或数据处理工具，属于化学信息学/生物信息学中利用AI模型进行生物标志物发现和推理的广义范畴。

**📖 中文摘要**

本研究调查了自动语音识别（ASR）质量对基于自发语音的阿尔茨海默病检测中下游临床语言建模的影响。研究使用Whisper ASR转录本在ADReSSo 2021诊断数据集上提取词汇特征，并评估可解释的机器学习模型（如逻辑回归和线性支持向量机）。结果表明，转录质量对分类性能有统计学上的显著影响。使用Whisper-small转录本训练的模型 consistently outperforms those using Whisper-base transcripts。特征分析揭示了认知正常说话者和阿尔茨海默病患者在语言模式上的差异。这些发现表明，高质量的ASR可以使简单、可解释的词汇模型在不进行显式声学建模的情况下实现有竞争力的阿尔茨海默病检测性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early detection of Alzheimer's disease from spontaneous speech has emerged as a promising non-invasive screening approach. However, the influence of automatic speech recognition (ASR) quality on downstream clinical language modeling remains insufficiently understood. In this study, we investigate Alzheimer's disease detection using lexical features derived from Whisper ASR transcripts on the ADReSSo 2021 diagnosis dataset. We evaluate interpretable machine-learning models, including Logistic Regression and Linear Support Vector Machines, using TF-IDF text representations under repeated 5x5 stratified cross-validation. Our results demonstrate that transcript quality has a statistically significant impact on classification performance. Models trained on Whisper-small transcripts consistently outperform those using Whisper-base transcripts, achieving balanced accuracy above 0.7850 with Linear SVM. Paired statistical testing confirms that the observed improvements are significant. Importantly, classifier complexity contributes less to performance variation than ASR transcription quality. Feature analysis reveals that cognitively normal speakers produce more semantically precise object- and scene-descriptive language, whereas Alzheimer's speech is characterized by vagueness, discourse markers, and increased hesitation patterns. These findings suggest that high-quality ASR can enable simple, interpretable lexical models to achieve competitive Alzheimer's detection performance without explicit acoustic modeling. The study provides a reproducible benchmark pipeline and highlights ASR selection as a critical modeling decision in clinical speech-based artificial intelligence systems.

</details>

---

### 28. [An SO(3)-equivariant reciprocal-space neural potential for long-range interactions](https://arxiv.org/abs/2603.18389)

**基本信息**

- 🔗 arXiv: [`2603.18389`](https://arxiv.org/abs/2603.18389)
- 👥 作者: Linfeng Zhang, Taoyong Cui, Dongzhan Zhou 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18389.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、具有物理原则的机器学习原子间势（MLIP），专门设计用于捕获分子和凝聚相系统中的长程相互作用。这直接属于化学信息学和计算化学中利用等变神经网络（可视为一种特定领域的“大模型”）进行高精度分子模拟和性质预测的范畴。

**📖 中文摘要**

本文介绍了EquiEwald，一种统一的神经原子间势，将受Ewald启发的倒空间公式嵌入到不可约SO(3)-等变框架中。通过在倒空间中进行等变消息传递（使用学习到的等变k空间滤波器和等变逆变换），EquiEwald能够捕获各向异性、张量化的长程关联，而不牺牲物理一致性。在周期和非周期基准测试中，EquiEwald捕获了与从头算参考数据一致的长程静电行为，并 consistently improves energy and force accuracy, data efficiency, and long-range extrapolation。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Long-range electrostatic and polarization interactions play a central role in molecular and condensed-phase systems, yet remain fundamentally incompatible with locality-based machine-learning interatomic potentials. Although modern SO(3)-equivariant neural potentials achieve high accuracy for short-range chemistry, they cannot represent the anisotropic, slowly decaying multipolar correlations governing realistic materials, while existing long-range extensions either break SO(3) equivariance or fail to maintain energy-force consistency. Here we introduce EquiEwald, a unified neural interatomic potential that embeds an Ewald-inspired reciprocal-space formulation within an irreducible SO(3)-equivariant framework. By performing equivariant message passing in reciprocal space through learned equivariant k-space filters and an equivariant inverse transform, EquiEwald captures anisotropic, tensorial long-range correlations without sacrificing physical consistency. Across periodic and aperiodic benchmarks, EquiEwald captures long-range electrostatic behavior consistent with ab initio reference data and consistently improves energy and force accuracy, data efficiency, and long-range extrapolation. These results establish EquiEwald as a physically principled paradigm for long-range-capable machine-learning interatomic potentials.

</details>

---

### 29. [Multi-Domain Causal Empirical Bayes Under Linear Mixing](https://arxiv.org/abs/2603.18404)

**基本信息**

- 🔗 arXiv: [`2603.18404`](https://arxiv.org/abs/2603.18404)
- 👥 作者: Bohan Wu, Julius von Kügelgen, David M. Blei
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18404.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是因果表示学习（CRL），旨在从高维观察中学习低维因果潜变量。这属于机器学习的基础研究，但其方法论（特别是涉及多领域数据和经验贝叶斯）对于构建能够进行因果推理的“化学大模型”或任何科学领域的分析模型具有核心意义。

**📖 中文摘要**

本文探讨了使用经验贝叶斯（EB）来估计因果表示。具体而言，考虑了从多个领域的数据中学习的问题，其中领域间的差异通过共享底层因果模型中的干预来建模。多领域因果表示学习自然地提出了一个同时推理问题，而经验贝叶斯正是为解决此类问题而设计的。作者提出了一种EB f-建模算法，通过利用领域内和领域间的不变结构来提高学习到的因果变量的质量。具体考虑了一个线性测量模型和由共享无环结构因果模型产生的干预先验。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Causal representation learning (CRL) aims to learn low-dimensional causal latent variables from high-dimensional observations. While identifiability has been extensively studied for CRL, estimation has been less explored. In this paper, we explore the use of empirical Bayes (EB) to estimate causal representations. In particular, we consider the problem of learning from data from multiple domains, where differences between domains are modeled by interventions in a shared underlying causal model. Multi-domain CRL naturally poses a simultaneous inference problem that EB is designed to tackle. Here, we propose an EB $f$-modeling algorithm that improves the quality of learned causal variables by exploiting invariant structure within and across domains. Specifically, we consider a linear measurement model and interventional priors arising from a shared acyclic SCM. When the graph and intervention targets are known, we develop an EM-style algorithm based on causally structured score matching. We further discuss EB $\rmg$-modeling in the context of existing CRL approaches. In experiments on synthetic data, our proposed method achieves more accurate estimation than other methods for CRL.

</details>

---

### 30. [Recovering Sparse Neural Connectivity from Partial Measurements: A Covariance-Based Approach with Granger-Causality Refinement](https://arxiv.org/abs/2603.18497)

**基本信息**

- 🔗 arXiv: [`2603.18497`](https://arxiv.org/abs/2603.18497)
- 👥 作者: Quilee Simeon
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18497.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从部分观测数据中推断神经网络连接性（即结构）的算法。虽然应用背景是神经科学，但其核心问题——从观测数据中推理底层结构——与质谱结构推理（从质谱数据推断分子结构）在方法论上高度相似，都属于从复杂数据中逆向工程生成模型的参数或结构。

**📖 中文摘要**

本文提出了一种基于协方差的方法，用于从跨多个记录会话的稀疏、部分观测中估计递归神经网络的权重矩阵。通过累积不同神经元子集被观测到的会话中的成对协方差估计，无需同时记录所有神经元即可重建完整的连接矩阵。一个基于投影梯度下降的格兰杰因果细化步骤通过生物物理约束来增强估计。通过在模拟小脑回路合成网络上的系统实验，作者描述了一个基本的控制-估计权衡：刺激有助于可识别性但会破坏内在动力学，其最佳水平取决于测量密度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inferring the connectivity of neural circuits from incomplete observations is a fundamental challenge in neuroscience. We present a covariance-based method for estimating the weight matrix of a recurrent neural network from sparse, partial measurements across multiple recording sessions. By accumulating pairwise covariance estimates across sessions where different subsets of neurons are observed, we reconstruct the full connectivity matrix without requiring simultaneous recording of all neurons. A Granger-causality refinement step enforces biological constraints via projected gradient descent. Through systematic experiments on synthetic networks modeling small brain circuits, we characterize a fundamental control-estimation tradeoff: stimulation aids identifiability but disrupts intrinsic dynamics, with the optimal level depending on measurement density. We discover that the ``incorrect'' linear approximation acts as implicit regularization -- outperforming the oracle estimator with known nonlinearity at all operating regimes -- and provide an exact characterization via the Stein--Price identity.

</details>

---

### 31. [End-to-End QGAN-Based Image Synthesis via Neural Noise Encoding and Intensity Calibration](https://arxiv.org/abs/2603.18554)

**基本信息**

- 🔗 arXiv: [`2603.18554`](https://arxiv.org/abs/2603.18554)
- 👥 作者: Xue Yang, Rigui Zhou, Shizheng Jia 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18554.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是量子生成对抗网络（QGAN），这是一种用于在量子设备上学习数据分布的生成模型。这属于利用新兴计算范式（量子计算）构建生成模型（“大模型”的一种形式）的前沿研究，与化学信息学中探索量子机器学习用于分子生成的兴趣点相关。

**📖 中文摘要**

本文提出了ReQGAN，一个用于图像合成的端到端量子生成对抗网络框架。该框架使用单个D量子电路合成整个N=2^D像素的图像，克服了阻碍直接像素生成的两个基本瓶颈：（1）僵化的经典到量子噪声接口，以及（2）归一化量子统计量与所需像素强度空间之间的输出失配。作者引入了可学习的神经噪声编码器用于自适应状态准备，以及可微分的强度校准模块，将测量结果映射到稳定、视觉有意义的像素域。在MNIST和Fashion-MNIST上的实验表明，ReQGAN在严格的量子比特预算下实现了稳定的训练和有效的图像合成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Generative Adversarial Networks (QGANs) offer a promising path for learning data distributions on near-term quantum devices. However, existing QGANs for image synthesis avoid direct full-image generation, relying on classical post-processing or patch-based methods. These approaches dilute the quantum generator's role and struggle to capture global image semantics. To address this, we propose ReQGAN, an end-to-end framework that synthesizes an entire N=2^D-pixel image using a single D-qubit quantum circuit. ReQGAN overcomes two fundamental bottlenecks hindering direct pixel generation: (1) the rigid classical-to-quantum noise interface and (2) the output mismatch between normalized quantum statistics and the desired pixel-intensity space. We introduce a learnable Neural Noise Encoder for adaptive state preparation and a differentiable Intensity Calibration module to map measurements to a stable, visually meaningful pixel domain. Experiments on MNIST and Fashion-MNIST demonstrate that ReQGAN achieves stable training and effective image synthesis under stringent qubit budgets, with ablation studies verifying the contribution of each component.

</details>

---

### 32. [DeePAW: A universal machine learning model for orbital-free ab initio calculations](https://arxiv.org/abs/2603.18650)

**基本信息**

- 🔗 arXiv: [`2603.18650`](https://arxiv.org/abs/2603.18650)
- 👥 作者: Tianhao Su, Shunbo Hu, Yue Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18650.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种通用的、覆盖多元素的机器学习原子间势（MLIP），用于高精度、高效率的无轨道密度泛函理论计算。这直接是化学信息学和计算材料学中“大模型”的典范：一个单一模型能够处理多种元素和结构，进行电子密度和能量预测，是替代传统量子化学计算的有力工具。

**📖 中文摘要**

本文提出了深度增强波模型（DeePAW），这是一种用于无轨道（OF）从头算计算的通用机器学习模型，基于密度泛函理论（DFT）。DeePAW是目前最好的OFDFT ML模型，覆盖了最大数量的元素，具有最广泛的不同晶体结构应用能力，并且在不进行进一步微调的情况下实现了最高的预测精度。DeePAW的科学优点和创新源于新颖的SE(3)-等变双消息传递神经网络。除了预测电子密度分布外，DeePAW还能预测晶体的形成能，从而为超越传统电子结构计算方法的跨尺度材料建模开辟了一条高效途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Developing universal machine learning models for ab initio calculations is the frontier of materials cutting edge research in the new era of artificial intelligence. Here, we present the Deep Augment Way model (DeePAW) that is a universal machine learning (ML) model for orbital-free (OF) ab initio calculations, based on the density functional theory (DFT). DeePAW is currently the best OFDFT ML model according to the three criterions, 1) covering the largest number of elements, 2) having the widest application capability to diverse crystal structures, and 3) achieving the highest prediction accuracy without further fine-tuning. These scientific merits and innovations of DeePAW are stemmed from the novel SE(3)-equivariant double massage passing neuron networks. Besides predicting electron density distributions, DeePAW predicts formation energies of crystals as well and therefore paves an efficient avenue for multiscale materials modeling beyond conventional electronic structure calculation methods.

</details>

---

### 33. [Data-driven construction of machine-learning-based interatomic potentials for gas-surface scattering dynamics: the case of NO on graphite](https://arxiv.org/abs/2603.18864)

**基本信息**

- 🔗 arXiv: [`2603.18864`](https://arxiv.org/abs/2603.18864)
- 👥 作者: Samuel Del Fré, Gilberto A. Alou Angulo, Maurice Monnerville 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18864.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对一个具体的化学物理问题（气体-表面散射），构建一个专用的机器学习原子间势（MLIP）。这体现了化学信息学中“针对特定问题定制大模型”的研究范式，涉及描述符工程、主动学习等关键化学信息学技术，用于实现高精度、高效率的分子动力学模拟。

**📖 中文摘要**

本文开发了一种数据驱动的工作流程，用于构建专门针对气体-表面散射动力学的机器学习原子间势（MLIP），以一氧化氮（NO）在高度取向热解石墨（HOPG）上的散射作为基准系统。工作流程从初始的从头算分子动力学数据集开始，使用SOAP描述符描述局部原子环境，并通过主成分分析在降维特征空间中进行分析。然后使用最远点采样构建紧凑的训练集，并通过基于委员会的主动学习策略，利用从扩展入射能量和表面温度范围的分子动力学模拟中提取的额外构型来细化得到的深度势模型。最终的MLIP以远低于AIMD的计算成本，实现了对NO在石墨上散射的大规模分子动力学模拟。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate atomistic simulations of gas-surface scattering require potential energy surfaces that remain reliable over broad configurational and energetic ranges while retaining the efficiency needed for extensive trajectory sampling. Here, we develop a data-driven workflow for constructing a machine-learning interatomic potential (MLIP) tailored to gas-surface scattering dynamics, using nitric oxide (NO) scattering from highly oriented pyrolytic graphite (HOPG) as a benchmark system. Starting from an initial ab initio molecular dynamics (AIMD) dataset, local atomic environments are described by SOAP descriptors and analyzed in a reduced feature space obtained through principal component analysis. Farthest point sampling is then used to build a compact training set, and the resulting Deep Potential model is refined through a query-by-committee active-learning strategy using additional configurations extracted from molecular dynamics simulations over extended ranges of incident energies and surface temperatures. The final MLIP reproduces reference energies and forces with high fidelity and enables large-scale molecular dynamics simulations of NO scattering from graphite at a computational cost far below that of AIMD. The simulations provide detailed insight into adsorption energetics, trapping versus direct scattering probabilities, translational energy loss, angular distributions, and rotational excitation. Overall, the results reproduce the main experimental trends and demonstrate that descriptor-guided sampling combined with active learning offers an efficient and transferable strategy for constructing MLIPs for gas-surface interactions.

</details>

---

### 34. [Improving moment tensor solutions under Earth structure uncertainty with simulation-based inference](https://arxiv.org/abs/2603.18925)

**基本信息**

- 🔗 arXiv: [`2603.18925`](https://arxiv.org/abs/2603.18925)
- 👥 作者: A. A. Saoulis, T.-S. Pham, A. M. G. Ferreira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.18925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用模拟推理（SBI，一种基于生成模型/似然自由推理的机器学习方法）来改进地球物理中的矩张量反演。这属于利用先进的生成式AI方法（大模型推理技术）解决科学中的逆问题，其方法论与从复杂数据（如质谱）中推断底层参数（如分子结构）的“推理”问题在本质上相通。

**📖 中文摘要**

本文介绍了一种利用模拟推理（SBI）处理理论误差的稳健方法，用于全波形矩张量反演。SBI是一种机器学习方法，可以凭经验建模理论误差对观测的影响。该框架保留了贝叶斯推理的严谨性，同时避免了对不确定性函数形式的限制性假设。作者首先证明了在轻微（1-3%）的一维地球模型不确定性下，理论误差的常见高斯参数化会失效。为了解决这个问题，他们开发了两种利用SBI来提高矩张量解质量的形式：一种基于对理论误差的物理洞察，另一种利用端到端的深度学习算法。结果表明，高斯假设会导致偏差并显著低估矩张量的不确定性，而SBI则能产生更可靠、校准更好的地震源机制后验分布。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bayesian inference represents a principled way to incorporate Earth structure uncertainty in full-waveform moment tensor inversions, but traditional approaches generally require significant approximations that risk biasing the resulting solutions. We introduce a robust method for handling theory errors using simulation-based inference (SBI), a machine learning approach that empirically models their impact on the observations. This framework retains the rigour of Bayesian inference while avoiding restrictive assumptions about the functional form of the uncertainties. We begin by demonstrating that the common Gaussian parametrisation of theory errors breaks down under minor ($1-3 \%$) 1-D Earth model uncertainty. To address this issue, we develop two formalisms for utilising SBI to improve the quality of the moment tensor solutions: one using physics-based insights into the theory errors, and another utilising an end-to-end deep learning algorithm. We then compare the results of moment tensor inversion with the standard Gaussian approach and SBI, and demonstrate that Gaussian assumptions induce bias and significantly under-report moment tensor uncertainties. We also show that these effects are particularly problematic when inverting short period data and for shallow, isotropic events. On the other hand, SBI produces more reliable, better calibrated posteriors of the earthquake source mechanism. Finally, we successfully apply our methodology to two well studied moderate magnitude earthquakes: one from the 1997 Long Valley Caldera volcanic earthquake sequence, and the 2020 Zagreb earthquake.

</details>

---

### 35. [BSTModelKit.jl: A Julia Package for Constructing, Solving, and Analyzing Biochemical Systems Theory Models](https://arxiv.org/abs/2603.19115)

**基本信息**

- 🔗 arXiv: [`2603.19115`](https://arxiv.org/abs/2603.19115)
- 👥 作者: Sandra Vadhin, Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19115.pdf)

**💡 相关性分析**

满足标准2：论文的核心内容是发布了一个用于生化系统建模和模拟的软件工具包（BSTModelKit.jl）。该工具提供了构建和分析BST模型（一种用于代谢网络的数学模型）的资源，可用于生成模拟数据或作为更大建模管道的一部分。这为化学信息学和系统生物学领域的研究人员提供了可直接使用的数据和工具资源。

**📖 中文摘要**

本文介绍了BSTModelKit.jl，一个用于构建、求解和分析生化系统理论（BST）模型的开源Julia软件包。该包实现了S-system表示法，这是一种用于建模代谢和调控网络的规范幂律形式主义。BSTModelKit.jl提供了声明式模型规范格式、通过常微分方程（ODE）积分进行动态模拟、稳态计算以及使用Morris和Sobol方法进行全局敏感性分析。该包利用Julia科学计算生态系统，特别是SciML微分方程求解器套件，提供高效灵活的模型分析工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present this http URL , an open-source Julia package for constructing, solving, and analyzing Biochemical Systems Theory (BST) models of biochemical networks. The package implements S-system representations, a canonical power-law formalism for modeling metabolic and regulatory networks. this http URL provides a declarative model specification format, dynamic simulation via ordinary differential equation (ODE) integration, steady-state computation, and global sensitivity analysis using the Morris and Sobol methods. The package leverages the Julia scientific computing ecosystem, in particular the SciML suite of differential equation solvers, to provide efficient and flexible model analysis tools. We describe the mathematical formulation, software design, and demonstrate the package capabilities with illustrative examples.

</details>

---

### 36. [Variational and Annealing-Based Approaches to Quantum Combinatorial Optimization](https://arxiv.org/abs/2603.19117)

**基本信息**

- 🔗 arXiv: [`2603.19117`](https://arxiv.org/abs/2603.19117)
- 👥 作者: Hala Hawashin, Deep Nath, Marco Alberto Javarone
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19117.pdf)

**💡 相关性分析**

满足标准3：论文是一篇综述/展望性文章，系统地回顾和比较了用于组合优化的各类量子算法（包括量子生成模型QGM），并讨论了它们的工业应用前景。这直接涉及对“量子生成模型”这一特定类型大模型的现状和未来的讨论，属于对前沿AI/量子计算模型在优化问题中应用的综述。

**📖 中文摘要**

本文回顾了用于组合优化的量子方法，旨在连接理论发展和工业相关性。首先综述了主要的量子算法家族，包括量子退火、量子近似优化算法（QAOA）、量子强化学习（QRL）和量子生成建模（QGM）。然后考察了量子技术目前显示出量子优势证据的问题类别，借鉴了QOBLIB、QUARK、QASMBench和QED-C等已建立的基准测试计划。这些 problem classes 随后被映射到代表性的工业领域，包括物流、金融和电信。分析表明，量子退火目前展现出最高的操作成熟度，而QAOA在NISQ时代的硬件上显示出有希望的潜力。相比之下，QRL和QGM则成为具有未来重大工业潜力的长期研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we review quantum approaches to combinatorial optimization, with the aim of bridging theoretical developments and industrial relevance. We first survey the main families of quantum algorithms, including Quantum Annealing, the Quantum Approximate Optimization Algorithm (QAOA), Quantum Reinforcement Learning (QRL), and Quantum Generative Modeling (QGM). We then examine the problem classes where quantum technologies currently show evidence of quantum advantage, drawing on established benchmarking initiatives such as QOBLIB, QUARK, QASMBench, and QED-C. These problem classes are subsequently mapped to representative industrial domains, including logistics, finance, and telecommunications. Our analysis indicates that quantum annealing currently exhibits the highest level of operational maturity, while QAOA shows promising potential on NISQ-era hardware. In contrast, QRL and QGM emerge as longer-term research directions with significant potential for future industrial impact.

</details>

---

### 37. [Quantum block encoding for semiseparable matrices](https://arxiv.org/abs/2603.19130)

**基本信息**

- 🔗 arXiv: [`2603.19130`](https://arxiv.org/abs/2603.19130)
- 👥 作者: Giacomo Antonioli, Paola Boito, Gianna M. Del Corso 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19130.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对一类特定结构矩阵（半可分离矩阵）设计高效的量子块编码算法。量子块编码是许多量子机器学习算法（包括可能用于化学模拟的量子线性系统求解器、量子主成分分析等）的基础模块。这项工作属于为量子机器学习（可视为下一代“大模型”的计算基础）开发核心组件的范畴。

**📖 中文摘要**

量子块编码（QBE）是大多数量子算法开发中的关键步骤，因为它将给定矩阵嵌入到合适的更大酉矩阵中。历史上，高效QBE技术的发展主要集中在稀疏矩阵上；对数据稀疏（例如，秩结构）矩阵投入的努力较少。在这项工作中，我们研究了一种特殊的秩结构情况，即一对半可分离矩阵。我们提出了一种新的块编码方法，该方法依赖于将给定矩阵适当地分解为三角因子和对角因子的乘积。为了编码矩阵，该算法需要2log(N)+7个辅助量子比特。这个过程需要多对数时间，并且具有O(N^2)的误差，其中N是矩阵大小。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum block encoding (QBE) is a crucial step in the development of most quantum algorithms, as it provides an embedding of a given matrix into a suitable larger unitary matrix. Historically, the development of efficient techniques for QBE has mostly focused on sparse matrices; less effort has been devoted to data-sparse (e.g., rank-structured) matrices. In this work we examine a particular case of rank structure, namely, one-pair semiseparable matrices. We present a new block encoding approach that relies on a suitable factorization of the given matrix as the product of triangular and diagonal factors. To encode the matrix, the algorithm needs $2\log(N)+7$ ancillary qubits. This process takes polylogarithmic time and has an error of $\mathcal{O}(N^2)$, where $N$ is the matrix size.

</details>

---

### 38. [How Auditory Knowledge in LLM Backbones Shapes Audio Language Models: A Holistic Evaluation](https://arxiv.org/abs/2603.19195)

**基本信息**

- 🔗 arXiv: [`2603.19195`](https://arxiv.org/abs/2603.19195)
- 👥 作者: Ke-Han Lu, Szu-Wei Fu, Chao-Han Huck Yang 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.19195.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和比较不同大语言模型（LLMs）中编码的听觉知识，并研究这些知识如何转移到音频任务中。这直接涉及对“大模型”（LLMs）内部表示和知识迁移能力的研究，属于大模型能力评估和理解的范畴。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）作为大型音频语言模型（LALMs）知识骨干时，它们通过纯文本预训练编码了多少听觉知识，以及这如何影响下游性能。作者通过比较不同LLM在两种纯文本和一种音频接地设置下的表现来研究这一差距：（1）在AKB-2000（一个用于测试听觉知识广度和深度的精选基准）上进行直接探测；（2）级联评估，其中LLMs对来自音频描述器的文本描述进行推理；（3）音频接地评估，其中每个LLM通过音频编码器微调成大型音频语言模型（LALM）。研究结果表明，不同模型家族间的听觉知识差异很大，纯文本结果与音频性能 strongly correlated。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have been widely used as knowledge backbones of Large Audio Language Models (LALMs), yet how much auditory knowledge they encode through text-only pre-training and how this affects downstream performance remains unclear. We study this gap by comparing different LLMs under two text-only and one audio-grounded setting: (1) direct probing on AKB-2000, a curated benchmark testing the breadth and depth of auditory knowledge; (2) cascade evaluation, where LLMs reason over text descriptions from an audio captioner; and (3) audio-grounded evaluation, where each LLM is fine-tuned into a Large Audio Language Model (LALM) with an audio encoder. Our findings reveal that auditory knowledge varies substantially across families, and text-only results are strongly correlated with audio performance. Our work provides empirical grounding for a comprehensive understanding of LLMs in audio research.

</details>

---

### 39. [CADGL: Context-Aware Deep Graph Learning for Predicting Drug-Drug Interactions](https://arxiv.org/abs/2403.17210)

**基本信息**

- 🔗 arXiv: [`2403.17210`](https://arxiv.org/abs/2403.17210)
- 👥 作者: Azmine Toushik Wasi, Taki Hasan Rafi, Raima Islam 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2403.17210.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的深度学习框架（CADGL），用于预测药物-药物相互作用。这直接属于化学信息学和药物发现的核心领域，利用图神经网络等先进模型（可视为针对化学图的“大模型”）进行分子性质预测和关系推理。

**📖 中文摘要**

本文提出了一个名为CADGL的新型框架，用于药物-药物相互作用（DDI）预测。CADGL基于定制的变分图自编码器（VGAE），使用两个上下文预处理器从两个不同角度（局部邻域和分子上下文）在异质图结构中提取关键的结构和物理化学信息。定制的VGAE由图形编码器、潜在信息编码器和MLP解码器组成。CADGL超越了其他最先进的DDI预测模型，在预测具有临床价值的新型DDI方面表现出色，并得到了严谨的案例研究支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Examining Drug-Drug Interactions (DDIs) is a pivotal element in the process of drug development. DDIs occur when one drug's properties are affected by the inclusion of other drugs. Detecting favorable DDIs has the potential to pave the way for creating and advancing innovative medications applicable in practical settings. However, existing DDI prediction models continue to face challenges related to generalization in extreme cases, robust feature extraction, and real-life application possibilities. We aim to address these challenges by leveraging the effectiveness of context-aware deep graph learning by introducing a novel framework named CADGL. Based on a customized variational graph autoencoder (VGAE), we capture critical structural and physio-chemical information using two context preprocessors for feature extraction from two different perspectives: local neighborhood and molecular context, in a heterogeneous graphical structure. Our customized VGAE consists of a graph encoder, a latent information encoder, and an MLP decoder. CADGL surpasses other state-of-the-art DDI prediction models, excelling in predicting clinically valuable novel DDIs, supported by rigorous case studies. CADGL is vailable at: this https URL

</details>

---

### 40. [Modeling Inverse Ellipsometry Problem via Flow Matching with a Large-Scale Dataset](https://arxiv.org/abs/2407.17869)

**基本信息**

- 🔗 arXiv: [`2407.17869`](https://arxiv.org/abs/2407.17869)
- 👥 作者: Yiming Ma, Jianzhi Teng, Xinjie Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.17869.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献之一是构建并发布了EllipBench，一个用于逆椭圆偏振问题的大规模、高精度数据集。该数据集专为训练和评估机器学习模型（包括提出的DCFM生成模型）而设计，为光学常数和薄膜厚度的数据驱动推理提供了宝贵的资源。同时，论文提出的DCFM框架本身也是一种用于解决逆问题的生成模型。

**📖 中文摘要**

本文针对逆椭圆偏振问题（即从测量的相位差Δ和振幅比Ψ重建光学常数和薄膜厚度）提出了解决方案。为了弥补大规模数据集的缺乏，作者引入了EllipBench，一个包含超过800万个高精度样本的综合基准，涵盖98种薄膜材料和5种基底。在此基础上，作者系统评估了包括传统机器学习模型、深度神经网络和物理信息神经网络在内的多种方法。为了更好捕捉其固有的模糊性，作者进一步提出了一种新颖的解耦条件流匹配（DCFM）框架。DCFM将几何薄膜厚度解耦，并将其作为稳健的物理条件来指导一个连续向量场，用于建模波长相关光学常数的逆概率分布。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inverse ellipsometry, i.e., reconstructing optical constants and film thickness from the measured phase difference $\Delta$ and amplitude ratio $\Psi$, is a fundamentally ill-posed problem. Traditional solutions rely on slow, expert-driven iterative fitting, while the development of machine learning approaches has been severely limited by the lack of large-scale, physically consistent datasets. To address this gap, we introduce \textbf{EllipBench}, a comprehensive benchmark comprising over 8 million high-precision samples spanning 98 thin-film materials and 5 substrates. Building upon this benchmark, we conduct a systematic evaluation of a broad spectrum of methods, including traditional machine learning models, deep neural networks, and Physics-Informed Neural Networks, and show that existing paradigms consistently struggle to fully resolve the inverse ellipsometry task. To better capture its inherent ambiguity, we further propose a novel \textbf{Decoupled Conditional Flow Matching (DCFM)} framework. Rather than formulating the problem as deterministic point-to-point regression, DCFM explicitly decouples geometric film thickness and incorporates it as a robust physical condition to guide a continuous vector field for modeling the inverse probability distribution of wavelength-dependent optical constants. Combined with a gradient detachment strategy and physics-based constraints, our joint architecture effectively mitigates intrinsic physical ambiguities and delivers a robust and accurate solution for inverse ellipsometry.

</details>

---

### 41. [Biased AI can Influence Political Decision-Making](https://arxiv.org/abs/2410.06415)

**基本信息**

- 🔗 arXiv: [`2410.06415`](https://arxiv.org/abs/2410.06415)
- 👥 作者: Jillian Fisher, Shangbin Feng, Robert Aron 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.06415.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（用于设计问题的模型优化）直接应用于化学设计任务，这是化学信息学和化学大模型（用于分子发现与优化）的核心应用场景。

**📖 中文摘要**

论文《Cliqueformer: Model-Based Optimization with Structured Transformers》提出了一种基于Transformer的架构Cliqueformer，用于解决基于模型的离线优化（MBO）问题。该模型通过学习黑盒函数的结构（通过功能图模型）来处理分布偏移，而无需依赖显式的保守方法。论文在多个领域（包括化学和遗传设计任务）中展示了其性能优于现有方法。虽然论文主要关注通用的MBO框架，但其明确将化学设计任务作为应用领域之一。化学设计（如分子发现）是化学信息学的核心问题，通常涉及构建和优化化学大模型（如用于性质预测或生成的模型）来指导搜索。因此，该工作与“化学大模型”主题在核心应用层面相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As modern large language models (LLMs) become integral to everyday tasks, concerns about their inherent biases and their potential impact on human decision-making have emerged. While bias in models are well-documented, less is known about how these biases influence human decisions. This paper presents two interactive experiments investigating the effects of partisan bias in LLMs on political opinions and decision-making. Participants interacted freely with either a biased liberal, biased conservative, or unbiased control model while completing these tasks. We found that participants exposed to partisan biased models were significantly more likely to adopt opinions and make decisions which matched the LLM's bias. Even more surprising, this influence was seen when the model bias and personal political partisanship of the participant were opposite. However, we also discovered that prior knowledge of AI was weakly correlated with a reduction of the impact of the bias, highlighting the possible importance of AI education for robust mitigation of bias effects. Our findings not only highlight the critical effects of interacting with biased LLMs and its ability to impact public discourse and political conduct, but also highlights potential techniques for mitigating these risks in the future.

</details>

---

### 42. [Enhancing a Hierarchical Graph Rewriting Language based on MELL Cut Elimination](https://arxiv.org/abs/2411.14802)

**基本信息**

- 🔗 arXiv: [`2411.14802`](https://arxiv.org/abs/2411.14802)
- 👥 作者: Kento Takyu, Kazunori Ueda
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.14802.pdf)

**💡 相关性分析**

满足标准2：论文提出的基于分层图重写的增强型语言和工具链，为化学结构的表示、操作和推理（这是质谱结构推理和化学大模型构建的关键环节）提供了潜在的数据处理框架和工具资源。

**📖 中文摘要**

论文《Enhancing a Hierarchical Graph Rewriting Language based on MELL Cut Elimination》基于分层图重写和线性逻辑，扩展了声明式语言LMNtal。虽然论文本身属于形式化方法和编程语言领域，但其核心技术——分层图重写——是表示和操作化学结构的强大工具。在化学信息学中，分子通常被表示为图（原子为节点，化学键为边），而图重写规则是模拟化学反应、进行分子结构枚举和推理的基础。因此，该论文提出的增强型图重写语言框架，为化学结构（包括可能从质谱数据中推理出的结构）的表示、转换和计算提供了潜在的理论和工具基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hierarchical graph rewriting is a highly expressive computational formalism that manipulates graphs enhanced with box structures for representing hierarchies. It has provided the foundations of various graph-based modeling tools, but the design of high-level declarative languages based on hierarchical graph rewriting is still a challenge. For a solid design choice, well-established formalisms with backgrounds other than graph rewriting would provide useful guidelines. Proof nets of Multiplicative Exponential Linear Logic (MELL) is such a framework because its original formulation of cut elimination is essentially graph rewriting involving box structures, where so-called Promotion Boxes with an indefinite number of non-local edges may be cloned, migrated and deleted. This work builds on LMNtal as a declarative language based on hierarchical (port) graph rewriting, and discusses how it can be extended to support the above operations on Promotion Boxes of MELL proof nets. LMNtal thus extended turns out to be a practical graph rewriting language that has strong affinity with MELL proof nets. The language features provided are general enough to encode other well-established models of concurrency. Using the toolchain of LMNtal that provides state-space search and model checking, we implemented cut elimination rules of MELL proof nets in extended LMNtal and demonstrated that the platform could serve as a useful workbench for proof nets.

</details>

---

### 43. [Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment](https://arxiv.org/abs/2502.03714)

**基本信息**

- 🔗 arXiv: [`2502.03714`](https://arxiv.org/abs/2502.03714)
- 👥 作者: Harrish Thasarathan, Julian Forsyth, Thomas Fel 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.03714.pdf)

**💡 相关性分析**

满足标准1：论文提出的跨模型可解释概念对齐框架，其核心方法论直接适用于分析和理解化学大模型（如分子表征模型）学到的内部表示和化学概念，提升模型的可解释性和可比性。

**📖 中文摘要**

论文《Universal Sparse Autoencoders: Interpretable Cross-Model Concept Alignment》提出了通用稀疏自编码器（USAE）框架，用于发现和对齐多个预训练深度神经网络中的可解释概念。该框架学习一个通用的概念空间，可以重建和解释多个模型的内部激活。虽然论文以视觉模型为例，但其核心方法——学习跨模型的稀疏、可解释表示——与构建和理解“化学大模型”高度相关。在化学领域，可解释的表示学习对于理解分子表征模型（如图神经网络、Transformer）学到的化学概念（官能团、子结构等）至关重要。USAE提供了一种将不同化学模型（如不同架构或在不同数据集上训练的模型）的内部表示对齐到统一概念空间的方法，这有助于模型比较、知识迁移和提升化学大模型的可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Universal Sparse Autoencoders (USAEs), a framework for uncovering and aligning interpretable concepts spanning multiple pretrained deep neural networks. Unlike existing concept-based interpretability methods, which focus on a single model, USAEs jointly learn a universal concept space that can reconstruct and interpret the internal activations of multiple models at once. Our core insight is to train a single, overcomplete sparse autoencoder (SAE) that ingests activations from any model and decodes them to approximate the activations of any other model under consideration. By optimizing a shared objective, the learned dictionary captures common factors of variation-concepts-across different tasks, architectures, and datasets. We show that USAEs discover semantically coherent and important universal concepts across vision models; ranging from low-level features (e.g., colors and textures) to higher-level structures (e.g., parts and objects). Overall, USAEs provide a powerful new method for interpretable cross-model analysis and offers novel applications, such as coordinated activation maximization, that open avenues for deeper insights in multi-model AI systems

</details>

---

### 44. [This looks like what? Challenges and Future Research Directions for Part-Prototype Models](https://arxiv.org/abs/2502.09340)

**基本信息**

- 🔗 arXiv: [`2502.09340`](https://arxiv.org/abs/2502.09340)
- 👥 作者: Khawla Elhadri, Tomasz Michalski, Adam Wróbel 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.09340.pdf)

**💡 相关性分析**

满足标准3：论文是针对内置可解释性模型（部件-原型模型）的综述，其讨论的挑战和未来方向对设计和评估具有可解释性的化学大模型具有重要的参考和展望价值。

**📖 中文摘要**

论文《This looks like what? Challenges and Future Research Directions for Part-Prototype Models》是一篇关于“部件-原型模型”（PPMs）的综述。PPMs通过将输入与学习的原型进行比较来进行分类，并提供“这个看起来像那个”形式的人类可理解解释。虽然综述主要关注计算机视觉中的PPMs，但其讨论的核心主题——内置可解释性模型的设计、挑战和未来方向——与“化学大模型”的研究高度相关。在化学信息学中，开发可解释的分子性质预测、反应结果预测或分子生成模型是一个重要趋势。理解PPMs的局限性（如原型质量、泛化能力）和前沿研究方向，可以为设计下一代可解释的化学人工智能模型提供宝贵的见解和跨领域启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The growing interest in eXplainable Artificial Intelligence (XAI) has stimulated research on models with built-in interpretability, among which part-prototype models are particularly prominent. Part-Prototype Models (PPMs) classify inputs by comparing them to learned prototypes and provide human-understandable explanations of the form "this looks like that". Despite this intrinsic interpretability, PPMs have not yet emerged as a competitive alternative to post-hoc explanation methods. This survey reviews work published between 2019 and 2025 and derives a taxonomy of the challenges faced by current PPMs. The analysis reveals a diverse set of open problems. The main issue concerns the quality and number of learned prototypes. Further challenges include limited generalization across tasks and contexts, as well as methodological shortcomings such as non-standardized evaluation. Five broad research directions are identified: improving predictive performance, developing theoretically grounded architectures, establishing frameworks for human-AI collaboration, aligning models with human concepts, and defining robust metrics and benchmarks for evaluation. The survey aims to stimulate further research and promote intrinsically interpretable models for practical applications. A curated list of the surveyed papers is available at this https URL .

</details>

---

### 45. [DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models](https://arxiv.org/abs/2503.16426)

**基本信息**

- 🔗 arXiv: [`2503.16426`](https://arxiv.org/abs/2503.16426)
- 👥 作者: Keyan Chen, Chenyang Liu, Bowen Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.16426.pdf)

**💡 相关性分析**

满足标准1：论文核心研究的高效稀疏目标感知与建模方法论，与“质谱结构推理”中从复杂、高维数据中提取关键稀疏特征（谱峰）以推断分子结构的核心挑战在问题本质上高度相关，提供了可借鉴的技术思路。

**📖 中文摘要**

论文《DynamicVis: Dynamic Visual Perception for Efficient Remote Sensing Foundation Models》提出了一种为遥感图像定制的视觉基础模型DynamicVis，采用动态区域感知的状态空间模型（SSM）来高效处理超长序列的视觉令牌。虽然应用领域是遥感，但其核心技术创新——针对稀疏目标（在图像中占比极小）进行自适应计算和表示学习——与“质谱结构推理”面临的核心挑战有方法论上的相似性。在质谱分析中，需要从复杂的质谱信号（背景化学噪声）中识别出代表特定化合物结构的特征峰（稀疏但关键的目标）。论文中处理极端空间冗余和稀疏目标的技术思路（如自适应路由、增量建模、区域级元嵌入多实例学习预训练范式）为解决质谱数据中从高维、噪声信号中推理稀疏但决定性的结构信息这一问题提供了新颖的计算视角和潜在的技术借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The advancement of RS technology has enabled high-resolution Earth observation; however, interpreting these images using modern VFMs remains a significant challenge. Unlike object-centric natural images, RS imagery is fundamentally characterized by extreme target sparsity and massive spatial redundancy. Key objects of interest (e.g., ships, vehicles) often occupy less than 1% of the spatial extent, surrounded by vast, target-free backgrounds. Existing VFMs predominantly rely on uniform dense processing (e.g., ViTs) and pixel-reconstruction pre-training paradigms (e.g., MAE). These approaches inherently waste substantial computational capacity on modeling redundant backgrounds and inadvertently dilute the feature representations of small, sparse targets. To bridge this structural misalignment, we propose DynamicVis, a visual foundation model explicitly tailored to the sparse nature of RS imagery. Architecturally, DynamicVis introduces a Dynamic Region-Aware SSM that bypasses uniform computation. It adaptively routes and incrementally models only task-relevant, high-salience tokens while employing a parameter-free integration for background context, drastically reducing the complexity of processing ultra-long 2D token sequences ($\sim$100,000). Crucially, to equip the network with robust spatial-selection capabilities, we propose a novel Region-Level Meta-Embedding Multi-Instance Learning (MIL) pre-training paradigm. Trained on a million-scale dataset, this paradigm explicitly disentangles sparse foreground instances from dense backgrounds in the latent semantic space, overcoming the semantic ambiguity of conventional pixel-reconstruction methods. Extensive evaluations across nine diverse downstream tasks reveal that DynamicVis exhibits exceptional efficacy, particularly dominating in sparse-target and instance-level perception tasks (e.g., small object detection, and change detection).

</details>

---

### 46. [Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability](https://arxiv.org/abs/2505.03530)

**基本信息**

- 🔗 arXiv: [`2505.03530`](https://arxiv.org/abs/2505.03530)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.03530.pdf)

**💡 相关性分析**

满足标准1：论文提出的针对生成模型（VAE）的机制可解释性因果干预框架，其核心方法论直接适用于分析和理解化学领域广泛使用的分子VAE等生成模型，有助于提升化学大模型的可解释性和可控性。

**📖 中文摘要**

论文《Causal Intervention Framework for Variational Auto Encoder Mechanistic Interpretability》提出了一个用于变分自编码器（VAE）机制可解释性的因果干预框架。该框架通过在不同层级（输入、潜在空间、激活修补）进行针对性干预，来识别和分析VAE中的“电路模块”，研究语义因子如何通过网络层进行编码、处理和分离。虽然论文主要使用合成数据和标准解纠缠基准进行评估，但其提出的框架和方法论与“化学大模型”的可解释性研究直接相关。在化学领域，VAE及其变体（如用于分子生成和表示的VAE）被广泛使用。理解这些生成模型的内部工作机制、它们如何编码化学语义（如官能团、溶解度），以及如何进行因果干预以控制特定属性的生成，对于构建可靠、可控的化学大模型至关重要。该论文为系统性地分析和解释化学VAE模型提供了工具和评估指标。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mechanistic interpretability of deep learning models has emerged as a crucial research direction for understanding the functioning of neural networks. While significant progress has been made in interpreting discriminative models like transformers, understanding generative models such as Variational Autoencoders (VAEs) remains challenging. This paper introduces a comprehensive causal intervention framework for mechanistic interpretability of VAEs. We develop techniques to identify and analyze "circuit motifs" in VAEs, examining how semantic factors are encoded, processed, and disentangled through the network layers. Our approach uses targeted interventions at different levels: input manipulations, latent space perturbations, activation patching, and causal mediation analysis. We apply our framework to both synthetic datasets with known causal relationships and standard disentanglement benchmarks. Results show that our interventions can successfully isolate functional circuits, map computational graphs to causal graphs of semantic factors, and distinguish between polysemantic and monosemantic units. Furthermore, we introduce metrics for causal effect strength, intervention specificity, and circuit modularity that quantify the interpretability of VAE components. Experimental results demonstrate clear differences between VAE variants, with FactorVAE achieving higher disentanglement scores (0.084) and effect strengths (mean 4.59) compared to standard VAE (0.064, 3.99) and Beta-VAE (0.051, 3.43). Our framework advances the mechanistic understanding of generative models and provides tools for more transparent and controllable VAE architectures.

</details>

---

### 47. [RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval](https://arxiv.org/abs/2506.08625)

**基本信息**

- 🔗 arXiv: [`2506.08625`](https://arxiv.org/abs/2506.08625)
- 👥 作者: Minhae Oh, Jeonghye Kim, Nakyung Lee 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.08625.pdf)

**💡 相关性分析**

满足标准1：论文提出的用于增强LLMs科学推理的逐步检索增强框架，其核心方法（结合外部知识库进行结构化检索推理）可直接应用于构建更强大的化学领域大模型，特别是辅助完成像质谱解析这类需要复杂领域知识推理的任务。

**📖 中文摘要**

论文《RAISE: Enhancing Scientific Reasoning in LLMs via Step-by-Step Retrieval》提出了RAISE框架，通过逐步检索增强大型语言模型（LLMs）的科学推理能力。该框架将推理过程分解为问题分解、逻辑查询生成和逻辑检索三个步骤，从开放语料库中检索逻辑相关的文档。虽然论文主要评估在通用科学推理基准上的表现，但其核心思想——通过结构化检索获取外部知识来辅助复杂推理——与“化学大模型”和“质谱结构推理”的需求高度契合。在化学信息学中，LLMs需要结合专业的化学知识（如反应规则、光谱数据库、物化性质）进行推理。RAISE的逐步检索机制为解决化学问题（例如，根据质谱特征推理可能的结构，需要检索子结构碎片库、已知化合物谱库等）提供了一个可操作的增强框架，能够提升LLMs在化学领域的准确性和可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Scientific reasoning requires not only long-chain reasoning processes, but also knowledge of domain-specific terminologies and adaptation to updated findings. To deal with these challenges for scientific reasoning, we introduce RAISE, a step-by-step retrieval-augmented framework which retrieves logically relevant documents from in-the-wild corpus. RAISE is divided into three steps: problem decomposition, logical query generation, and logical retrieval. We observe that RAISE consistently outperforms other baselines on scientific reasoning benchmarks. We analyze that unlike other baselines, RAISE retrieves documents that are not only similar in terms of the domain knowledge, but also documents logically more relevant.

</details>

---

### 48. [Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning](https://arxiv.org/abs/2506.16931)

**基本信息**

- 🔗 arXiv: [`2506.16931`](https://arxiv.org/abs/2506.16931)
- 👥 作者: Jiaqi Chen, Mingfeng Fan, Xuefeng Zhang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.16931.pdf)

**💡 相关性分析**

满足标准1：论文核心研究的多模态（图与图像）融合学习方法，与化学信息学中融合分子图表示和分子形状/图像表示以构建更全面分子表征模型的挑战直接相关，提供了可借鉴的架构设计思路。

**📖 中文摘要**

论文《Multimodal Fused Learning for Solving the Generalized Traveling Salesman Problem in Robotic Task Planning》提出了多模态融合学习（MMFL）框架，利用图和图像两种表示来解决广义旅行商问题（GTSP），用于机器人任务规划。虽然应用场景是机器人学，但其核心方法——融合不同模态（图结构信息和空间图像信息）以更好地解决组合优化问题——与“化学大模型”中的分子表示学习有很强的类比性。在化学信息学中，分子通常同时用图（原子和键）和基于网格的图像（如分子表面、电子密度）来表示。有效地融合这些多模态信息对于构建强大的分子性质预测或生成模型至关重要。该论文在GTSP上验证的多模态融合策略（如自适应分辨率缩放、带有专用瓶颈的多模态融合模块）为化学领域中如何设计神经网络架构以融合分子图与分子图像/形状信息提供了技术参考和灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Effective and efficient task planning is essential for mobile robots, especially in applications like warehouse retrieval and environmental monitoring. These tasks often involve selecting one location from each of several target clusters, forming a Generalized Traveling Salesman Problem (GTSP) that remains challenging to solve both accurately and efficiently. To address this, we propose a Multimodal Fused Learning (MMFL) framework that leverages both graph and image-based representations to capture complementary aspects of the problem, and learns a policy capable of generating high-quality task planning schemes in real time. Specifically, we first introduce a coordinate-based image builder that transforms GTSP instances into spatially informative representations. We then design an adaptive resolution scaling strategy to enhance adaptability across different problem scales, and develop a multimodal fusion module with dedicated bottlenecks that enables effective integration of geometric and spatial features. Extensive experiments show that our MMFL approach significantly outperforms state-of-the-art methods across various GTSP instances while maintaining the computational efficiency required for real-time robotic applications. Physical robot tests further validate its practical effectiveness in real-world scenarios.

</details>

---

### 49. [Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes](https://arxiv.org/abs/2507.12261)

**基本信息**

- 🔗 arXiv: [`2507.12261`](https://arxiv.org/abs/2507.12261)
- 👥 作者: Johann Frei, Nils Feldhus, Lisa Raithel 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.12261.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于智能体和工具使用的端到端文本到结构化数据生成框架，其方法论可迁移至化学信息学领域，用于从科学文本或实验报告中自动提取和构建结构化的化学信息（如化合物、反应、光谱数据），这与构建化学知识库和增强大模型数据源密切相关。

**📖 中文摘要**

论文《Infherno: End-to-end Agent-based FHIR Resource Synthesis from Free-form Clinical Notes》提出了一个基于LLM智能体的端到端框架，用于将自由文本临床笔记转化为结构化的FHIR（Fast Healthcare Interoperability Resources）资源。该框架利用LLM智能体、代码执行和医学术语数据库工具，以遵循FHIR模式并生成符合规范的结构化输出。虽然应用领域是临床信息学，但其核心技术创新——使用智能体框架结合领域知识工具，将非结构化文本精确转换为复杂的、模式化的结构化数据——与“化学大模型”和“质谱结构推理”中的信息提取和结构化任务高度相关。例如，从科学文献中自动提取化学反应条件、从质谱解析报告中提取化合物标识信息，或直接将质谱数据与文本描述结合生成结构化的化合物数据库条目，都可以借鉴该论文的智能体驱动、工具增强的端到端结构化生成范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

For clinical data integration and healthcare services, the HL7 FHIR standard has established itself as a desirable format for interoperability between complex health data. Previous attempts at automating the translation from free-form clinical notes into structured FHIR resources address narrowly defined tasks and rely on modular approaches or LLMs with instruction tuning and constrained decoding. As those solutions frequently suffer from limited generalizability and structural inconformity, we propose an end-to-end framework powered by LLM agents, code execution, and healthcare terminology database tools to address these issues. Our solution, called Infherno, is designed to adhere to the FHIR document schema and competes well with a human baseline in predicting FHIR resources from unstructured text. The implementation features a front end for custom and synthetic data and both local and proprietary models, supporting clinical data integration processes and interoperability across institutions. Gemini 2.5-Pro excels in our evaluation on synthetic and clinical datasets, yet ambiguity and feasibility of collecting ground-truth data remain open problems.

</details>

---

### 50. [GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM](https://arxiv.org/abs/2507.13323)

**基本信息**

- 🔗 arXiv: [`2507.13323`](https://arxiv.org/abs/2507.13323)
- 👥 作者: Kyeongjin Ahn, Sungwon Han, Seungeon Lee 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.13323.pdf)

**💡 相关性分析**

满足标准1：论文提出的利用LLM进行特征工程和约束建模以解决少样本回归问题的方法，其核心思路可直接应用于化学信息学中的小数据挑战，例如利用LLM理解分子描述符与目标性质的关系，或质谱特征与分子子结构的关系，从而构建更数据高效的化学模型。

**📖 中文摘要**

论文《GeoReg: Weight-Constrained Few-Shot Regression for Socio-Economic Estimation using LLM》提出了GeoReg模型，利用大语言模型（LLM）作为数据工程师，从卫星图像和网络地理空间信息等多源数据中提取特征，并在少样本设置下估计社会经济指标。其核心是利用LLM的先验知识理解数据特征与目标指标之间的上下文关系（正相关、负相关等），并对线性估计器施加相应的权重约束。虽然应用领域是社会经济估计，但其核心方法——利用LLM进行特征工程和关系建模以解决数据稀缺领域的回归问题——与“化学大模型”和“质谱结构推理”中的小数据问题高度相关。在化学中，许多任务（如新材料性质预测、稀有化合物谱图解析）也面临标记数据稀缺的挑战。GeoReg展示的利用LLM先验知识引导特征构建和模型约束的思路，为在化学小数据场景下构建稳健的预测或推理模型提供了有前景的方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Socio-economic indicators like regional GDP, population, and education levels, are crucial to shaping policy decisions and fostering sustainable development. This research introduces GeoReg a regression model that integrates diverse data sources, including satellite imagery and web-based geospatial information, to estimate these indicators even for data-scarce regions such as developing countries. Our approach leverages the prior knowledge of large language model to address the scarcity of labeled data, with the language model functioning as a data engineer by extracting informative features to enable effective estimation in few-shot settings. Specifically, our model obtains contextual relationships between data features and the target indicator, categorizing their correlations as positive, negative, mixed, or irrelevant. These features are then fed into the linear estimator with tailored weight constraints for each category. To capture nonlinear patterns, the model also identifies meaningful feature interactions and integrates them, along with nonlinear transformations. Experiments across three countries at different stages of development demonstrate that our model outperforms baselines in estimating socio-economic indicators, even for low-income countries with limited data availability.

</details>

---

### 51. [Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions](https://arxiv.org/abs/2508.17303)

**基本信息**

- 🔗 arXiv: [`2508.17303`](https://arxiv.org/abs/2508.17303)
- 👥 作者: Dhiraj S Kori, Abhinav Chandraker, Syed Abdur Rahman 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.17303.pdf)

**💡 相关性分析**

满足标准1：论文核心研究的物理信息神经网络（PINN）方法，是构建具有物理可解释性和约束性的“化学大模型”（如用于性质预测、过程模拟）的关键技术之一。该工作提供了PINN在复杂材料科学问题上的成功应用实例，验证了该范式在相关领域的潜力。

**📖 中文摘要**

论文《Physics-informed neural network for predicting fatigue life of unirradiated and irradiated austenitic and ferritic/martensitic steels under reactor-relevant conditions》提出了一种物理信息神经网络（PINN）框架，用于预测核反应堆用钢在辐照等复杂条件下的低周疲劳寿命。该模型将控制疲劳寿命的物理约束嵌入损失函数，在提高预测准确性的同时保证物理一致性。虽然应用领域是材料科学，但其核心方法——PINN——是“科学机器学习”的典范，也是构建“化学大模型”的重要范式之一。在化学信息学中，PINN被广泛应用于求解化学动力学方程、预测分子性质（结合量子力学约束）、以及优化化学过程。该论文展示了PINN在处理复杂、多因素（应变、辐照剂量、温度）耦合的工业级科学问题上的有效性，为在化学领域构建类似的高保真、物理约束模型（如预测反应速率、催化剂性能）提供了成功的应用案例和方法验证。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study proposes a Physics-Informed Neural Network (PINN) framework to predict the low-cycle fatigue (LCF) life of irradiated austenitic and ferritic/martensitic (F/M) steels used in nuclear reactors. These materials undergo cyclic loading, neutron irradiation, and elevated temperatures, leading to complex degradation mechanisms that are difficult to capture with conventional empirical or purely data-driven models. The proposed PINN embeds fatigue-life governing physical constraints into the loss function, enabling physically consistent learning while improving predictive accuracy, reliability, and generalizability. The model was trained on 495 strain-controlled fatigue data points spanning irradiated and unirradiated conditions. Compared with traditional machine learning approaches, including Random Forest, Gradient Boosting, eXtreme Gradient Boosting, and conventional neural networks, the PINN demonstrated superior performance. SHapley Additive exPlanations (SHAP) analysis identified strain amplitude, irradiation dose, and test temperature as the dominant features, each exhibiting physically meaningful inverse correlations with fatigue life. Univariate and multivariate analyses revealed clear alloy-specific degradation characteristics. Austenitic steels exhibited strong nonlinear coupling among strain amplitude, irradiation dose, and temperature, resulting in pronounced fatigue degradation under combined loading. In contrast, F/M steels demonstrated comparatively stable irradiation responses, including dose-saturation behavior, but showed sensitivity to elevated temperatures beyond tempering thresholds. Overall, the proposed PINN framework serves as a reliable and interpretable tool for reactor-relevant fatigue assessment, enabling performance evaluation for advanced nuclear applications.

</details>

---

### 52. [CausalARC: Abstract Reasoning with Causal World Models](https://arxiv.org/abs/2509.03636)

**基本信息**

- 🔗 arXiv: [`2509.03636`](https://arxiv.org/abs/2509.03636)
- 👥 作者: Jacqueline Maasch, John Kalantari, Kia Khezeli
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.03636.pdf)

**💡 相关性分析**

满足标准2：论文提出的CausalARC平台及其背后的因果世界模型框架，为开发和评估具有因果推理能力的化学大模型（这是该领域的前沿方向）提供了重要的概念框架、评估范式和潜在的工具资源。

**📖 中文摘要**

论文《CausalARC: Abstract Reasoning with Causal World Models》引入了CausalARC，一个用于评估AI在低数据和分布外泛化环境下推理能力的实验平台。该平台受抽象与推理语料库（ARC）启发，但每个推理任务都从一个完全指定的因果世界模型（结构因果模型）中采样。它提供观察性、干预性和反事实性的反馈作为少样本上下文学习示例。虽然平台本身是通用推理测试台，但其核心围绕“因果世界模型”和“结构化因果模型”展开，这与“化学大模型”的前沿研究方向高度一致。在化学领域，构建能够进行反事实推理（例如，“如果改变这个官能团，分子毒性会如何变化？”）和干预推理的因果模型是一个重要目标。CausalARC为开发和评估具有因果推理能力的化学大模型（无论是用于分子设计、反应预测还是谱图解析）提供了一个形式化、可控制的评估框架和灵感来源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

On-the-fly reasoning often requires adaptation to novel problems under limited data and distribution shift. This work introduces CausalARC: an experimental testbed for AI reasoning in low-data and out-of-distribution regimes, modeled after the Abstraction and Reasoning Corpus (ARC). Each CausalARC reasoning task is sampled from a fully specified causal world model, formally expressed as a structural causal model. Principled data augmentations provide observational, interventional, and counterfactual feedback about the world model in the form of few-shot, in-context learning demonstrations. As a proof-of-concept, we illustrate the use of CausalARC for four language model evaluation settings: (1) abstract reasoning with test-time training, (2) counterfactual reasoning with in-context learning, (3) program synthesis, and (4) causal discovery with logical reasoning. Within- and between-model performance varied heavily across tasks, indicating room for significant improvement in language model reasoning.

</details>

---

### 53. [Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning](https://arxiv.org/abs/2509.08759)

**基本信息**

- 🔗 arXiv: [`2509.08759`](https://arxiv.org/abs/2509.08759)
- 👥 作者: Mominul Rubel, Adam Meyers, Gabriel Nicolosi
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.08759.pdf)

**💡 相关性分析**

满足标准1：论文提出的傅里叶学习机（FLM）架构，其核心是基于可学习傅里叶基的表示方法，这与质谱分析中信号处理、谱图表示和特征学习的本质高度相关，为“质谱结构推理”提供了一种新的、有潜力的神经网络建模范式。

**📖 中文摘要**

论文《Fourier Learning Machines: Nonharmonic Fourier-Based Neural Networks for Scientific Machine Learning》提出了傅里叶学习机（FLM），一种设计用于表示多维非谐波傅里叶级数的神经网络架构。FLM使用简单的前馈结构和余弦激活函数，将级数的频率、振幅和相移作为可训练参数进行学习。该设计使模型能够创建适用于周期和非周期函数的问题特定谱基。论文评估了FLM在包括偏微分方程（PDE）和最优控制问题（OCP）在内的多个科学计算问题上的性能。FLM的核心——基于傅里叶级数的可学习谱表示——与“质谱结构推理”有深刻联系。质谱的本质是信号（强度）随质荷比（可视为频率域）的分布。将质谱数据表示为可学习的傅里叶级数，可能为谱图去噪、特征提取、以及建立谱图与分子结构之间的映射关系提供一种新颖且具有坚实数学基础的建模方法。这与质谱结构推理的核心任务直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce the Fourier Learning Machine (FLM), a neural network (NN) architecture designed to represent a multidimensional nonharmonic Fourier series. The FLM uses a simple feedforward structure with cosine activation functions to learn the frequencies, amplitudes, and phase shifts of the series as trainable parameters. This design allows the model to create a problem-specific spectral basis adaptable to both periodic and nonperiodic functions. Unlike previous Fourier-inspired NN models, the FLM is the first architecture able to represent a multidimensional Fourier series with a complete set of basis functions in separable form, doing so by using a standard Multilayer Perceptron-like architecture. A one-to-one correspondence between the Fourier coefficients and amplitudes and phase-shifts is demonstrated, allowing for the translation between a full, separable basis form and the cosine phase-shifted one. Additionally, we evaluate the performance of FLMs on several scientific computing problems, including benchmark Partial Differential Equations (PDEs) and a family of Optimal Control Problems (OCPs). Computational experiments show that the performance of FLMs is comparable, and often superior, to that of established architectures like SIREN and vanilla feedforward NNs.

</details>

---

### 54. [Neuron-Guided Interpretation of Code LLMs: Where, Why, and How?](https://arxiv.org/abs/2512.19980)

**基本信息**

- 🔗 arXiv: [`2512.19980`](https://arxiv.org/abs/2512.19980)
- 👥 作者: Zhe Yin, Xiaodong Gu, Beijun Shen
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.19980.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析代码大语言模型（Code LLMs）的内部工作机制，这直接属于“化学大模型”主题的范畴（大模型在特定科学领域的应用与可解释性研究）。

**📖 中文摘要**

本文研究了代码大语言模型（Code LLMs）在神经元层面的可解释性。作者分析了Llama-3.1-8B和Qwen2.5-Coder-32B等模型在处理多语言代码（C++、Java、Python等）时的内部激活模式。研究发现，模型中存在专门处理特定编程语言的神经元，也存在支持通用生成的通用神经元子集。此外，模型的较低层主要编码语言特定的语法，而中间层则捕获跨语言的语义抽象，这些“概念层”编码了语言无关的代码表示。这项工作通过神经元引导的微调、基于概念层嵌入的克隆检测以及概念层引导的代码摘要迁移等任务，展示了这些发现的实际应用价值。该研究为理解代码大模型的内部工作机制提供了新的视角，并探索了如何利用这些发现来提升模型在代码生成和理解任务上的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Code language models excel on code intelligence tasks, yet their internal interpretability is underexplored. Existing neuron interpretability techniques from NLP are suboptimal for source code due to programming languages formal, hierarchical, and executable nature. We empirically investigate code LLMs at the neuron level, localizing language-specific neurons (selectively responsive to one language) and concept layers (feed-forward layers encoding language-agnostic code representations). We analyze Llama-3.1-8B and Qwen2.5-Coder-32B on multilingual inputs in C++, Java, Python, Go, and JavaScript, measuring neuron selectivity and layerwise contributions during generation. We find (1) neurons specialized for individual languages alongside a universal subset supporting general-purpose generation; and (2) lower layers mainly encode language-specific syntax, while middle layers capture semantic abstractions shared across languages, emerging as concept layers. We demonstrate utility on three tasks: neuron-guided fine-tuning for code generation, clone detection via concept-layer embeddings, and concept-layer-guided transfer for code summarization, each yielding consistent gains in multilingual settings.

</details>

---

### 55. [Weights to Code: Extracting Interpretable Algorithms from the Discrete Transformer](https://arxiv.org/abs/2601.05770)

**基本信息**

- 🔗 arXiv: [`2601.05770`](https://arxiv.org/abs/2601.05770)
- 👥 作者: Yifan Zhang, Wei Bi, Kechi Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.05770.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一种新型Transformer架构（离散Transformer）用于从模型中提取可解释的算法，这直接涉及“化学大模型”主题中模型架构设计与可解释性研究。

**📖 中文摘要**

本文提出了“离散Transformer”（Discrete Transformer）架构，旨在弥合连续表示与离散符号逻辑之间的鸿沟。该架构通过温度退火采样注入离散性，并利用假设检验和符号回归来提取人类可读的程序。其目标是直接从在算法任务上训练的模型中合成可执行程序，实现无需人工编写代码的算法发现。论文表明，该架构在连续变量域上实现了与基于RNN的方法相当的性能，同时扩展了可解释性。退火动态显示出清晰的探索到利用的转变。此外，架构的归纳偏置为合成程序提供了细粒度控制，确立了离散Transformer作为无演示算法发现和Transformer可解释性的鲁棒框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Algorithm extraction aims to synthesize executable programs directly from models trained on algorithmic tasks, enabling de novo algorithm discovery without relying on human-written code. However, applying this paradigm to Transformer is hindered by representation entanglement (e.g., superposition), where entangled features encoded in overlapping directions obstruct the recovery of symbolic expressions. We propose the Discrete Transformer, an architecture explicitly designed to bridge the gap between continuous representations and discrete symbolic logic. By injecting discreteness through temperature-annealed sampling, our framework effectively leverages hypothesis testing and symbolic regression to extract human-readable programs. Empirically, the Discrete Transformer achieves performance comparable to RNN-based methods while extending interpretability to continuous variable domains, and the annealing dynamics exhibit a clear exploration-to-exploitation transition. Finally, we show that architectural inductive biases provide fine-grained control over synthesized programs, establishing the Discrete Transformer as a robust framework for demonstration-free algorithm discovery and Transformer interpretability.

</details>

---

### 56. [DeeperBrain: A Neuro-Grounded EEG Foundation Model Towards Universal BCI](https://arxiv.org/abs/2601.06134)

**基本信息**

- 🔗 arXiv: [`2601.06134`](https://arxiv.org/abs/2601.06134)
- 👥 作者: Jiquan Wang, Sha Zhao, Yangxuan Zhou 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.06134.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于脑电图分析的基础模型（DeeperBrain），这属于“化学大模型”主题的范畴（基础模型在科学数据分析中的应用）。

**📖 中文摘要**

本文提出了DeeperBrain，一个基于神经科学原理的脑电图（EEG）基础模型，旨在实现通用的脑机接口（BCI）。该模型在架构设计中融入了领域特定的归纳偏置，包括模拟容积传导的空间通道编码和捕获神经动力学的时间编码。在预训练阶段，采用了结合掩码EEG重建（MER）和神经动力学统计预测（NSP）的双目标策略。NSP通过预测可解释的序参量（如频谱功率、功能连接性等）来强制模型与宏观大脑状态对齐。实验表明，DeeperBrain在端到端微调和严格的冻结探测协议下均能达到先进性能，验证了将神经科学第一性原理嵌入学习表示中，可以赋予模型通用BCI所需的内在普适性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electroencephalography (EEG) foundation models hold significant promise for universal Brain-Computer Interfaces (BCIs). However, existing approaches often rely on end-to-end fine-tuning and exhibit limited efficacy under frozen-probing protocols, lacking the intrinsic universality required for broad generalization. This limitation stems from adapting general-purpose sequence architectures that overlook the biophysical and dynamical principles of neural activity. To bridge this gap, we propose DeeperBrain, a neuro-grounded foundation model integrating domain-specific inductive biases into its model design and learning objectives. Architecturally, DeeperBrain incorporates a volume conduction-aware channel encoding to model spatial mixing via 3D geometry, and a neurodynamics-aware temporal encoding capturing slow adaptations using oscillatory and exponential bases. For pretraining, we introduce a dual-objective strategy combining Masked EEG Reconstruction (MER) for local fidelity and Neurodynamics Statistics Prediction (NSP). NSP enforces alignment with macroscopic brain states by predicting interpretable order parameters, including spectral power, functional connectivity, cross-frequency coupling, and dynamic complexity. Extensive experiments demonstrate that DeeperBrain achieves state-of-the-art or highly competitive performance under end-to-end fine-tuning. Crucially, it maintains superior efficacy under a rigorous frozen-probing protocol, verifying that embedding neuroscientific first principles endows learned representations with the intrinsic universality essential for universal BCI. The code will be publicly available.

</details>

---

### 57. [GeoMotionGPT: Geometry-Aligned Motion Understanding with Large Language Models](https://arxiv.org/abs/2601.07632)

**基本信息**

- 🔗 arXiv: [`2601.07632`](https://arxiv.org/abs/2601.07632)
- 👥 作者: Zhankai Ye, Bofan Li, Yukai Jin 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.07632.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进大型语言模型（LLMs）对运动数据的理解和推理能力，涉及大模型在多模态数据（运动序列）上的应用与对齐，属于“化学大模型”主题的广义范畴（大模型处理科学数据）。

**📖 中文摘要**

本文提出了GeoMotionGPT，一个用于运动理解与运动-语言推理的新框架。针对现有基于离散运动标记化的方法在运动空间几何与语言模型嵌入空间对齐不足的问题，该框架显式地对运动码本和LLM嵌入空间施加正交性约束，确保它们的关系结构自然相互映射。具体方法包括使用带Gumbel-Softmax的仅解码器量化器、保持正交性的稀疏投影，以及两阶段正交正则化调度。实验表明，该框架在HumanML3D和KIT-ML数据集上显著提升了运动文本生成等任务的性能，消融实验验证了量化器、投影和正则化设计的有效性。这项工作通过几何对齐增强了LLM对运动数据的语义推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discrete motion tokenization has recently enabled Large Language Models (LLMs) to serve as versatile backbones for motion understanding and motion-language reasoning. However, existing pipelines typically decouple motion quantization from semantic embedding learning, linking them solely via token IDs. This approach fails to effectively align the intrinsic geometry of the motion space with the embedding space, thereby hindering the LLM's capacity for nuanced motion reasoning. We argue that alignment is most effective when both modalities share a unified geometric basis. Therefore, instead of forcing the LLM to reconstruct the complex geometry among motion tokens from scratch, we present a novel framework that explicitly enforces orthogonality on both the motion codebook and the LLM embedding space, ensuring that their relational structures naturally mirror each other. Specifically, we employ a decoder-only quantizer with Gumbel-Softmax for differentiable training and balanced codebook usage. To bridge the modalities, we use a sparse projection that maps motion codes into the LLM embedding space while preserving orthogonality. Finally, a two-stage orthonormal regularization schedule enforces soft constraints during tokenizer training and LLM fine-tuning to maintain geometric alignment without hindering semantic adaptation. Extensive experiments show that our framework improves the aggregated Average by 22.4% over the strongest baseline on HumanML3D and by 14.4% on KIT-ML, while ablations confirm the effectiveness of the tokenizer, projection, and regularization designs.

</details>

---

### 58. [Multimodal Machine Learning for Soft High-k Elastomers under Data Scarcity](https://arxiv.org/abs/2601.18032)

**基本信息**

- 🔗 arXiv: [`2601.18032`](https://arxiv.org/abs/2601.18032)
- 👥 作者: Brijesh FNU, Viet Thanh Duy Nguyen, Ashima Sharma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18032.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容是利用预训练的聚合物表示（化学大模型）进行材料性能预测，直接围绕‘化学大模型’主题。同时，论文整理并公开了高质量的介电弹性体数据集，为相关研究提供了数据资源。

**📖 中文摘要**

本文聚焦于软高介电常数弹性体的开发，这是一个化学材料设计问题。论文的核心贡献在于构建了一个高质量的丙烯酸酯基介电弹性体数据集，并提出了一个多模态学习框架。该框架利用大规模预训练的聚合物表示（即化学大模型）来迁移化学和结构知识，从而在数据稀缺的情况下实现对介电和机械性能的准确预测。这项工作直接为化学大模型在材料发现领域的应用提供了数据资源和具体方法，展示了如何利用预训练模型的知识来加速特定化学材料的性能预测和设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dielectric materials are critical building blocks for modern electronics such as sensors, actuators, and transistors. With rapid advances in soft and stretchable electronics for emerging human- and robot-interfacing applications, there is a growing need for high-performance dielectric elastomers. However, developing soft elastomers that simultaneously exhibit high dielectric constants (k) and low Young's moduli (E) remains a major challenge. Although individual elastomer designs have been reported, structured datasets that systematically integrate molecular sequence, dielectric, and mechanical properties are largely unavailable. To address this gap, we curate a compact, high-quality dataset of acrylate-based dielectric elastomers by aggregating experimental results from the past decade. Building on this dataset, we propose a multimodal learning framework leveraging large-scale pretrained polymer representations. These pretrained embeddings transfer chemical and structural knowledge from vast polymer corpora, enabling accurate few-shot prediction of dielectric and mechanical properties and accelerating data-efficient discovery of soft high-$k$ dielectric elastomers. Our data and implementation are publicly available at: this https URL

</details>

---

### 59. [AI4S-SDS: A Neuro-Symbolic Solvent Design System via Sparse MCTS and Differentiable Physics Alignment](https://arxiv.org/abs/2603.03686)

**基本信息**

- 🔗 arXiv: [`2603.03686`](https://arxiv.org/abs/2603.03686)
- 👥 作者: Jiangyu Chen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.03686.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个用于自动化化学配方设计的神经符号框架，其中涉及多智能体协作和基于模型的优化，这直接应用了化学大模型（作为智能体的基础）来解决化学信息学中的核心问题——分子/配方设计。

**📖 中文摘要**

本文提出了AI4S-SDS，一个用于自动化化学配方设计的神经符号框架。该框架集成了多智能体协作和定制的蒙特卡洛树搜索（MCTS）引擎，旨在解决化学配方设计这一高维组合空间中的探索问题。论文的核心是开发一个闭环系统，通过模拟用户反应和结合可微分物理引擎来优化配方，以符合热力学约束。这项工作将化学大模型（作为智能体推理的基础）和结构化搜索方法应用于化学配方设计这一核心化学信息学问题，旨在实现科学发现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated design of chemical formulations is a cornerstone of materials science, yet it requires navigating a high-dimensional combinatorial space involving discrete compositional choices and continuous geometric constraints. Existing Large Language Model (LLM) agents face significant challenges in this setting, including context window limitations during long-horizon reasoning and path-dependent exploration that may lead to mode collapse. To address these issues, we introduce AI4S-SDS, a closed-loop neuro-symbolic framework that integrates multi-agent collaboration with a tailored Monte Carlo Tree Search (MCTS) engine. We propose a Sparse State Storage mechanism with Dynamic Path Reconstruction, which decouples reasoning history from context length and enables arbitrarily deep exploration under fixed token budgets. To reduce local convergence and improve coverage, we implement a Global--Local Search Strategy: a memory-driven planning module adaptively reconfigures the search root based on historical feedback, while a Sibling-Aware Expansion mechanism promotes orthogonal exploration at the node level. Furthermore, we bridge symbolic reasoning and physical feasibility through a Differentiable Physics Engine, employing a hybrid normalized loss with sparsity-inducing regularization to optimize continuous mixing ratios under thermodynamic constraints. Empirical results show that AI4S-SDS achieves full validity under the adopted HSP-based physical constraints and substantially improves exploration diversity compared to baseline agents. In preliminary lithography experiments, the framework identifies a novel photoresist developer formulation that demonstrates competitive or superior performance relative to a commercial benchmark, highlighting the potential of diversity-driven neuro-symbolic search for scientific discovery.

</details>

---

### 60. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发CliqueFlowmer模型，这是一种专门用于材料发现（化学信息学核心领域）的模型优化方法。它深度结合了Transformer等大模型架构与优化算法，直接围绕‘化学大模型’在材料设计中的应用主题。

**📖 中文摘要**

本文针对计算材料发现（CMD）中的优化问题，提出了一种基于离线模型优化（MBO）的新方法CliqueFlowmer。该方法将目标材料属性的直接优化融入到生成过程中，超越了传统的基于最大似然训练的生成模型。CliqueFlowmer结合了基于团的MBO最新进展与Transformer和流生成模型，专门用于材料发现。论文验证了该模型在优化材料性能方面的能力，并表明其生成的材料显著优于生成式基线模型。这项工作为材料科学中的化学大模型应用提供了一种新的、更有效的优化范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 61. [A Unified View of Drifting and Score-Based Models](https://arxiv.org/abs/2603.07514)

**基本信息**

- 🔗 arXiv: [`2603.07514`](https://arxiv.org/abs/2603.07514)
- 👥 作者: Chieh-Hsin Lai, Bac Nguyen, Naoki Murata 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07514.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从分数匹配的角度统一漂移模型和扩散模型的理论。扩散模型是当前化学大模型（特别是用于分子生成和结构推理）中常用的生成范式，因此该理论研究直接关联到化学大模型底层生成机制的理解。

**📖 中文摘要**

本文从理论角度统一了漂移模型和基于分数的模型（如扩散模型）。论文的核心发现是，对于高斯核，基于核的漂移模型的平均漂移场恰好等于高斯平滑后的数据分布与模型分布之间的分数差异。这一恒等式源于Tweedie公式，表明高斯核漂移本质上是在平滑分布上的一种分数匹配式目标。这项工作建立了漂移模型与扩散模型之间的理论联系，而扩散模型是当前生成式AI和化学大模型（用于分子生成）中的重要组成部分。因此，该研究为理解相关生成模型的数学基础提供了重要见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drifting models train one-step generators by optimizing a mean-shift discrepancy induced by a kernel between the data and model distributions, with Laplace kernels used by default in practice. At each point, this discrepancy compares the kernel-weighted displacement toward nearby data samples with the corresponding displacement toward nearby model samples, yielding a transport direction for generated samples. In this paper, we make its relationship to the score-matching principle behind diffusion models precise by showing that drifting admits a score-based formulation on kernel-smoothed distributions. For Gaussian kernels, the population mean-shift field coincides with the score difference between the Gaussian-smoothed data and model distributions. This identity follows from Tweedie's formula, which links the score of a Gaussian-smoothed density to the corresponding conditional mean, and implies that Gaussian-kernel drifting is exactly a score-matching-style objective on smoothed distributions. It also clarifies the connection to Distribution Matching Distillation (DMD): both methods use score-mismatch transport directions, but drifting realizes the score signal nonparametrically from kernel neighborhoods, whereas DMD uses a pretrained diffusion teacher. Beyond Gaussians, we derive an exact decomposition for general radial kernels, and for the Laplace kernel we prove rigorous error bounds showing that drifting remains an accurate proxy for score matching in low-temperature and high-dimensional regimes.

</details>

---

### 62. [Nonparametric Variational Differential Privacy via Embedding Parameter Clipping](https://arxiv.org/abs/2603.09583)

**基本信息**

- 🔗 arXiv: [`2603.09583`](https://arxiv.org/abs/2603.09583)
- 👥 作者: Dina El Zein, Shashi Kumar, James Henderson
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09583.pdf)

**💡 相关性分析**

满足标准1：论文的研究重点是改进用于构建隐私保护语言模型的变分框架。语言模型是化学大模型的核心组件，因此该工作直接关联到化学大模型在隐私敏感场景下的安全部署和性能优化。

**📖 中文摘要**

本文针对非参数变分差分隐私（NVDP）框架中存在的潜在表示漂移问题，提出了一种基于参数裁剪的策略。NVDP框架是构建隐私保护语言模型的基础，而语言模型是化学大模型的重要组成部分。论文从最小化Rényi散度上界的目标出发，数学推导出对后验参数的具体约束，从而提高了模型的隐私保障和下游任务性能。这项工作通过改进变分模型，增强了在隐私约束下大模型的实用性和鲁棒性，对化学大模型在处理敏感化学数据（如私有分子库）时的隐私保护具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The nonparametric variational information bottleneck (NVIB) provides the foundation for nonparametric variational differential privacy (NVDP), a framework for building privacy-preserving language models. However, the learned latent representations can drift into regions with high information content, leading to poor privacy guarantees, but also low utility due to numerical instability during training. In this work, we introduce a principled parameter clipping strategy to directly address this issue. Our method is mathematically derived from the objective of minimizing the Rényi Divergence (RD) upper bound, yielding specific, theoretically grounded constraints on the posterior mean, variance, and mixture weight parameters. We apply our technique to an NVIB based model and empirically compare it against an unconstrained baseline. Our findings demonstrate that the clipped model consistently achieves tighter RD bounds, implying stronger privacy, while simultaneously attaining higher performance on several downstream tasks. This work presents a simple yet effective method for improving the privacy-utility trade-off in variational models, making them more robust and practical.

</details>

---

### 63. [Understanding by Reconstruction: Reversing the Software Development Process for LLM Pretraining](https://arxiv.org/abs/2603.11103)

**基本信息**

- 🔗 arXiv: [`2603.11103`](https://arxiv.org/abs/2603.11103)
- 👥 作者: Zhiyuan Zeng, Yichi Zhang, Yong Shan 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.11103.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种为LLM注入规划与推理过程的新预训练范式，以增强其复杂推理能力。这种增强LLM推理能力的方法，对于提升化学大模型在质谱结构推理、逆合成分析等需要多步逻辑推理的化学信息学任务上至关重要，因此高度相关。

**📖 中文摘要**

本文提出了一种名为“通过重建来理解”的新范式，旨在解决大语言模型（LLM）在复杂软件工程中深度推理能力不足的问题。作者认为，标准的预训练数据（静态代码库）缺失了背后的规划、调试和迭代过程。为此，他们引入了一个框架，通过多智能体模拟来合成这些“智能体轨迹”，并利用基于搜索的优化技术来提炼推理链。实验表明，在这些重建的轨迹上进行持续预训练，能显著提升LLM在长上下文理解、编码和智能体能力方面的表现。虽然论文以代码生成为例，但其核心思想——为模型注入规划与推理过程——对于提升化学大模型在分子逆向合成、反应预测等需要多步推理的任务能力具有直接的启发和借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have achieved remarkable success in code generation, they often struggle with the deep, long-horizon reasoning required for complex software engineering. We attribute this limitation to the nature of standard pre-training data: static software repositories represent only the terminal state of an intricate intellectual process, abstracting away the intermediate planning, debugging, and iterative refinement. To bridge this gap, we propose a novel paradigm: understanding via reconstruction. We hypothesize that reverse-engineering the latent agentic trajectories -- the planning, reasoning, and debugging steps -- behind static repositories provides a far richer supervision signal than raw code alone. To operationalize this, we introduce a framework that synthesizes these trajectories using a multi-agent simulation. This process is grounded in the structural realities of the source repositories (e.g., dependency graphs and file hierarchies) to ensure fidelity. Furthermore, to guarantee the logical rigor of the synthetic data, we employ a search-based optimization technique that iteratively refines the Chain-of-Thought (CoT) reasoning to maximize the likelihood of the ground-truth code. Empirical results demonstrate that continuous pre-training on these reconstructed trajectories significantly enhances Llama-3-8B's performance across diverse benchmarks, including long-context understanding, coding proficiency, and agentic capabilities.

</details>

---

### 64. [To See is Not to Master: Teaching LLMs to Use Private Libraries for Code Generation](https://arxiv.org/abs/2603.15159)

**基本信息**

- 🔗 arXiv: [`2603.15159`](https://arxiv.org/abs/2603.15159)
- 👥 作者: Yitong Zhang, Chengze Li, Ruize Chen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15159.pdf)

**💡 相关性分析**

满足标准1：论文研究如何让大语言模型学习和使用私有API（一种特定领域语言）。这与化学信息学中让化学大模型集成和调用专业化学工具（如用于质谱结构推理的谱库匹配算法、量子化学计算软件）的核心挑战直接对应，为解决化学大模型的工具使用和领域适应问题提供了思路。

**📖 中文摘要**

本文关注大语言模型在私有库导向的代码生成任务中的局限性，即模型难以有效调用私有库的API。论文提出了PriCoder方法，通过自动合成数据来教导LLMs调用私有库API。该方法将数据合成建模为图构建问题，并交替进行图演化与剪枝。实验表明，PriCoder能显著提升模型在私有库代码生成上的能力。虽然论文聚焦于编程，但其核心问题——如何让大模型学习和使用一个封闭、特定的“领域语言”（私有API）——与化学信息学中让化学大模型理解和调用特定的化学知识库、工具或数据库（例如，用于质谱解析的谱库或化学规则）在本质上高度相似。该研究为解决化学大模型与领域工具集成问题提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have shown strong potential for code generation, yet they remain limited in private-library-oriented code generation, where the goal is to generate code using APIs from private libraries. Existing approaches mainly rely on retrieving private-library API documentation and injecting relevant knowledge into the context at inference time. However, our study shows that this is insufficient: even given accurate required knowledge, LLMs still struggle to invoke private-library APIs effectively. To address this limitation, we propose PriCoder, an approach that teaches LLMs to invoke private-library APIs through automatically synthesized data. Specifically, PriCoder models private-library data synthesis as the construction of a graph, and alternates between two graph operators: (1) Progressive Graph Evolution, which improves data diversity by progressively synthesizing more diverse training samples from basic ones, and (2) Multidimensional Graph Pruning, which improves data quality through a rigorous filtering pipeline. To support rigorous evaluation, we construct two new benchmarks based on recently released libraries that are unfamiliar to the tested models. Experiments on three mainstream LLMs show that PriCoder substantially improves private-library-oriented code generation, yielding gains of over 20% in pass@1 in many settings, while causing negligible impact on general code generation capability. Our code and benchmarks are publicly available at this https URL .

</details>

---

### 65. [Learning to Predict, Discover, and Reason in High-Dimensional Event Sequences](https://arxiv.org/abs/2603.16313)

**基本信息**

- 🔗 arXiv: [`2603.16313`](https://arxiv.org/abs/2603.16313)
- 👥 作者: Hugo Math
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16313.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及将大语言模型（LLMs）应用于高维事件序列的建模、预测和推理，这与“化学大模型”主题直接相关，并为“质谱结构推理”这类复杂序列数据的分析提供了潜在的方法论框架。

**📖 中文摘要**

本文提出了一种统一事件序列建模、因果发现和大语言模型（LLMs）的框架，用于处理高维事件流（如车辆诊断故障码序列）的自动故障诊断。论文的核心是将诊断序列视为一种可以建模、预测和解释的语言。该框架包含三个部分：用于预测性维护的Transformer架构、可扩展的因果发现框架以及一个用于自动合成布尔规则的多智能体系统。这项工作与“化学大模型”主题相关，因为它展示了如何将大语言模型（LLMs）应用于复杂、高维的序列数据（类似于质谱或化学结构序列）进行推理和规则生成，为“质谱结构推理”提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Electronic control units (ECUs) embedded within modern vehicles generate a large number of asynchronous events known as diagnostic trouble codes (DTCs). These discrete events form complex temporal sequences that reflect the evolving health of the vehicle's subsystems. In the automotive industry, domain experts manually group these codes into higher-level error patterns (EPs) using Boolean rules to characterize system faults and ensure safety. However, as vehicle complexity grows, this manual process becomes increasingly costly, error-prone, and difficult to scale. Notably, the number of unique DTCs in a modern vehicle is on the same order of magnitude as the vocabulary of a natural language, often numbering in the tens of thousands. This observation motivates a paradigm shift: treating diagnostic sequences as a language that can be modeled, predicted, and ultimately explained. Traditional statistical approaches fail to capture the rich dependencies and do not scale to high-dimensional datasets characterized by thousands of nodes, large sample sizes, and long sequence lengths. Specifically, the high cardinality of categorical event spaces in industrial logs poses a significant challenge, necessitating new machine learning architectures tailored to such event-driven systems. This thesis addresses automated fault diagnostics by unifying event sequence modeling, causal discovery, and large language models (LLMs) into a coherent framework for high-dimensional event streams. It is structured in three parts, reflecting a progressive transition from prediction to causal understanding and finally to reasoning for vehicle diagnostics. Consequently, we introduce several Transformer-based architectures for predictive maintenance, scalable sample- and population-level causal discovery frameworks and a multi-agent system that automates the synthesis of Boolean EP rules.

</details>

---

### 66. [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](https://arxiv.org/abs/2603.17380)

**基本信息**

- 🔗 arXiv: [`2603.17380`](https://arxiv.org/abs/2603.17380)
- 👥 作者: Shuizhou Chen, Lang Yu, Kedu Jin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17380.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于虚拟细胞扰动预测的大规模基础模型（SCALE），该模型集成了LLaMA（一种大语言模型）进行细胞编码，直接体现了“化学大模型”在生物化学系统建模中的应用。

**📖 中文摘要**

本文提出了一个名为SCALE的大规模基础模型，用于虚拟细胞扰动预测。该模型将扰动预测表述为条件传输问题，并采用了一种结合LLaMA（一种大语言模型）进行细胞编码的架构。SCALE旨在解决大规模扰动预测中的训练/推理效率、高维稀疏表达空间的建模稳定性以及生物学保真度评估等瓶颈。这项工作与“化学大模型”主题相关，因为它展示了如何将大语言模型（如LLaMA）的编码能力整合到生物化学领域的特定预测任务中，构建了一个面向生物化学系统（细胞）的、具有可扩展性的基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Virtual cell models aim to enable in silico experimentation by predicting how cells respond to genetic, chemical, or cytokine perturbations from single-cell measurements. In practice, however, large-scale perturbation prediction remains constrained by three coupled bottlenecks: inefficient training and inference pipelines, unstable modeling in high-dimensional sparse expression space, and evaluation protocols that overemphasize reconstruction-like accuracy while underestimating biological fidelity. In this work we present a specialized large-scale foundation model SCALE for virtual cell perturbation prediction that addresses the above limitations jointly. First, we build a BioNeMo-based training and inference framework that substantially improves data throughput, distributed scalability, and deployment efficiency, yielding 12.51* speedup on pretrain and 1.29* on inference over the prior SOTA pipeline under matched system settings. Second, we formulate perturbation prediction as conditional transport and implement it with a set-aware flow architecture that couples LLaMA-based cellular encoding with endpoint-oriented supervision. This design yields more stable training and stronger recovery of perturbation effects. Third, we evaluate the model on Tahoe-100M using a rigorous cell-level protocol centered on biologically meaningful metrics rather than reconstruction alone. On this benchmark, our model improves PDCorr by 12.02% and DE Overlap by 10.66% over STATE. Together, these results suggest that advancing virtual cells requires not only better generative objectives, but also the co-design of scalable infrastructure, stable transport modeling, and biologically faithful evaluation.

</details>

---

### 67. [Cell-cell Communication Inference and Analysis: Biological Mechanisms, Computational Approaches, and Future Opportunities](https://arxiv.org/abs/2512.03497)

**基本信息**

- 🔗 arXiv: [`2512.03497`](https://arxiv.org/abs/2512.03497)
- 👥 作者: Xiangzheng Cheng, Haili Huang, Ye Su 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.03497.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对从单细胞和空间组学数据（常涉及质谱数据）中推断细胞间通讯的计算方法的综述，涵盖了大量相关模型和推理策略，与“化学大模型”（用于生物分子数据建模）和“质谱结构推理”（从质谱数据推断相互作用）主题高度相关。

**📖 中文摘要**

本文是关于从单细胞和空间组学数据中推断和分析细胞间通讯（CCC）的计算方法的综述。文章系统性地介绍了超过140种计算方法，涵盖了从整合已知配体-受体相互作用的策略到全新的推断方法。文章讨论了该领域的生物学机制、建模策略、当前挑战和未来机遇，并提供了一个在线资源以方便方法比较和选择。这项工作与“化学大模型”和“质谱结构推理”主题相关，因为它综述了用于分析复杂生物分子数据（通常来自质谱等组学技术）的计算模型和推理方法，这些方法的核心目标是从数据中推断出有意义的生物化学相互作用和结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In multicellular organisms, cells coordinate their activities through cell-cell communication (CCC), which is crucial for development, tissue homeostasis, and disease progression. Recent advances in single-cell and spatial omics technologies provide unprecedented opportunities to systematically infer and analyze CCC from these omics data, either by integrating prior knowledge of ligand-receptor interactions (LRIs) or through de novo approaches. A variety of computational methods have been developed, focusing on methodological innovations, accurate modeling of complex signaling mechanisms, and investigation of broader biological questions. These advances have greatly enhanced our ability to analyze CCC and generate biological hypotheses. Here, we introduce the biological mechanisms and modeling strategies of CCC, and provide a focused overview of more than 140 computational methods for inferring CCC from single-cell and spatial transcriptomic data, emphasizing the diversity in methodological frameworks and biological questions. Finally, we discuss the current challenges and future opportunities in this rapidly evolving field, and summarize available methods in an interactive online resource ( this https URL ) to facilitate more efficient method comparison and selection.

</details>

---

### 68. [Generalization of Long-Range Machine Learning Potentials in Complex Chemical Spaces](https://arxiv.org/abs/2512.10989)

**基本信息**

- 🔗 arXiv: [`2512.10989`](https://arxiv.org/abs/2512.10989)
- 👥 作者: Michal Sanocki, Julija Zavadlav
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.10989.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和提升机器学习原子间势（MLIPs）——一种用于化学系统建模的机器学习模型——在复杂化学空间中的泛化能力，这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

本文系统地评估了不同具有长程修正的机器学习原子间势（MLIPs）在复杂化学空间中的泛化能力。研究强调了长程建模方案对于实现可泛化MLIPs的重要性，并引入了一种有偏的训练-测试分割策略来严格评估模型在化学空间未见区域的性能。虽然研究以金属有机框架为例，但该方法广泛适用于其他材料。这项工作与“化学大模型”主题直接相关，因为它专注于开发能够准确、可泛化地模拟化学系统（分子、材料）的机器学习模型，这是化学信息学和计算化学中“化学大模型”的核心目标之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The vastness of chemical space makes generalization a central challenge in the development of machine learning interatomic potentials (MLIPs). While MLIPs could enable large-scale atomistic simulations with near-quantum accuracy, their usefulness is often limited by poor transferability to out-of-distribution samples. Here, we systematically evaluate different MLIP architectures with long-range corrections across diverse chemical spaces and show that such schemes are essential, not only for improving in-distribution performance but, more importantly, for enabling significant gains in transferability to unseen regions of chemical space. To enable a more rigorous benchmarking, we introduce biased train-test splitting strategies, which explicitly test the model performance in significantly different regions of chemical space. Together, our findings highlight the importance of long-range modeling for achieving generalizable MLIPs and provide a framework for diagnosing systematic failures across chemical space. Although we demonstrate our methodology on metal-organic frameworks, it is broadly applicable to other materials, offering insights into the design of more robust and transferable MLIPs.

</details>

---

### 69. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心内容是关于整合量子计算、高性能计算和机器学习来推动下一代药物发现，这直接涉及构建更强大、更精确的“化学大模型”。同时，论文包含了对未来技术融合前景的重要讨论和展望，符合“综述展望相关”的标准。

**📖 中文摘要**

本文探讨了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何解决药物发现中化学精度与计算可扩展性之间的瓶颈。论文指出，机器学习基础模型（如FeNNix-Bio1）能够实现量子精度的模拟，但其数据生成仍受限于经典计算。而高性能量子计算（HPQC）利用混合QPU-GPU架构，将成为量子化学数据的终极加速器，实现真正的化学精度。文章详细阐述了这种三方融合如何优化从系统准备到高保真模拟的药物发现流程。这项工作与“化学大模型”主题高度相关，因为它前瞻性地讨论了如何利用量子计算加速数据生成，以支撑下一代用于药物发现的、具有量子精度的大型化学机器学习模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

## 📊 数据统计
- 累计运行天数：45
- 累计论文数量：3233

## 📝 历史记录

> 暂无历史数据

