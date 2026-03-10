# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-10 01:28:37

## 📅 2026-03-10 (今日最新)

**相关论文数：82**

### 1. [FuseDiff: Symmetry-Preserving Joint Diffusion for Dual-Target Structure-Based Drug Design](https://arxiv.org/abs/2603.05567)

**基本信息**

- 🔗 arXiv: [`2603.05567`](https://arxiv.org/abs/2603.05567)
- 👥 作者: Jianliang Wu, Anjie Qiao, Zhen Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于双靶点药物设计的生成模型（FuseDiff），这直接属于“化学大模型”（用于分子生成的AI模型）范畴，并且其任务（基于蛋白质口袋结构推理配体分子）与“质谱结构推理”（基于谱图数据推理分子结构）在“结构推理”这一核心目标上高度相关。

**📖 中文摘要**

这篇论文提出了一种名为FuseDiff的端到端扩散模型，用于双靶点结构药物设计。该模型联合生成一个配体分子图和两个口袋特异性结合构象，条件是给定的两个蛋白质口袋。其核心创新在于通过双靶点局部上下文融合（DLCF）的消息传递主干网络，融合来自两个口袋的局部上下文信息，从而实现表达性的联合建模，同时保持所需的对称性。该工作明确解决了化学信息学中一个关键问题：基于结构的药物设计（SBDD），特别是针对多靶点（polypharmacology）的复杂场景。论文生成了一个用于双靶点训练的数据集，并在基准测试和真实世界双靶点系统上进行了评估，展示了最先进的对接性能。这项工作直接围绕“化学大模型”（用于分子生成）和“质谱结构推理”（虽然本文聚焦于基于结构的推理，但其核心任务——从结构信息推理分子结构——与质谱结构推理在方法论上高度相关，都属于从（部分）结构信息预测完整分子结构）的主题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Dual-target structure-based drug design aims to generate a single ligand together with two pocket-specific binding poses, each compatible with a corresponding target pocket, enabling polypharmacological therapies with improved efficacy and reduced resistance. Existing approaches typically rely on staged pipelines, which either decouple the two poses via conditional-independence assumptions or enforce overly rigid correlations, and therefore fail to jointly generate two target-specific binding modes. To address this, we propose FuseDiff, an end-to-end diffusion model that jointly generates a ligand molecular graph and two pocket-specific binding poses conditioned on both pockets. FuseDiff features a message-passing backbone with Dual-target Local Context Fusion (DLCF), which fuses each ligand atom's local context from both pockets to enable expressive joint modeling while preserving the desired symmetries. Together with explicit bond generation, FuseDiff enforces topological consistency across the two poses under a shared graph while allowing target-specific geometric adaptation in each pocket. To support principled training and evaluation, we derive a dual-target training set and use an independent held-out test set for evaluation. Experiments on the benchmark and a real-world dual-target system show that FuseDiff achieves state-of-the-art docking performance and enables the first systematic assessment of dual-target pose quality prior to docking-based pose search.

</details>

---

### 2. [Relational Semantic Reasoning on 3D Scene Graphs for Open World Interactive Object Search](https://arxiv.org/abs/2603.05642)

**基本信息**

- 🔗 arXiv: [`2603.05642`](https://arxiv.org/abs/2603.05642)
- 👥 作者: Imen Mahdi, Matteo Cassinelli, Fabien Despinoy 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05642.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了用于评估语义推理的基准（SymSearch）和包含多模态交互数据的数据集（RFM-HRI），这些资源可用于相关研究。同时，论文的方法论部分（利用场景图进行关系推理、从LLMs蒸馏知识）为“化学大模型”（如何让模型理解分子图等结构化知识）和“质谱结构推理”（如何结合化学知识进行推理）提供了重要的技术思路和讨论，属于相关的方法论讨论。

**📖 中文摘要**

这篇论文提出了SCOUT方法，用于开放世界家庭环境中的交互式物体搜索。该方法的核心创新在于利用3D场景图进行语义推理，并通过从大型语言模型（LLMs）中提取结构化关系知识到轻量级模型中，实现高效、开放词汇的搜索。论文还提出了SymSearch，一个用于评估交互式物体搜索任务中语义推理的可扩展符号基准。虽然该工作的应用场景是机器人导航和物体搜索，但其方法论涉及两个关键方面：1) 利用场景图（一种结构化的知识表示）进行关系推理；2) 从LLMs中蒸馏知识到轻量级模型。这些技术（结构化知识表示、知识蒸馏用于高效推理）与“化学大模型”和“质谱结构推理”中面临的挑战（如如何让模型理解复杂的化学结构关系、如何构建高效可部署的推理模型）在方法论上是相通的。论文提供的数据集（RFM-HRI）和基准（SymSearch）也属于数据资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Open-world interactive object search in household environments requires understanding semantic relationships between objects and their surrounding context to guide exploration efficiently. Prior methods either rely on vision-language embeddings similarity, which does not reliably capture task-relevant relational semantics, or large language models (LLMs), which are too slow and costly for real-time deployment. We introduce SCOUT: Scene Graph-Based Exploration with Learned Utility for Open-World Interactive Object Search, a novel method that searches directly over 3D scene graphs by assigning utility scores to rooms, frontiers, and objects using relational exploration heuristics such as room-object containment and object-object co-occurrence. To make this practical without sacrificing open-vocabulary generalization, we propose an offline procedural distillation framework that extracts structured relational knowledge from LLMs into lightweight models for on-robot inference. Furthermore, we present SymSearch, a scalable symbolic benchmark for evaluating semantic reasoning in interactive object search tasks. Extensive evaluations across symbolic and simulation environments show that SCOUT outperforms embedding similarity-based methods and matches LLM-level performance while remaining computationally efficient. Finally, real-world experiments demonstrate effective transfer to physical environments, enabling open-world interactive object search under realistic sensing and navigation constraints.

</details>

---

### 3. [Autonomous Algorithm Discovery for Ptychography via Evolutionary LLM Reasoning](https://arxiv.org/abs/2603.05696)

**基本信息**

- 🔗 arXiv: [`2603.05696`](https://arxiv.org/abs/2603.05696)
- 👥 作者: Xiangyu Yin, Ming Du, Junjing Deng 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05696.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是使用LLMs和进化算法自动发现科学计算算法，这本身就是“AI for Science”或“科学大模型”应用的一个实例，与“化学大模型”的广义范畴相关。同时，该工作展示的方法论（LLM驱动的代码生成与演化）为如何利用AI自动优化和设计领域特定模型/算法提供了重要的前瞻性讨论和案例，对“化学大模型”和“质谱结构推理”领域的方法论发展具有启发和参考价值。

**📖 中文摘要**

这篇论文介绍了Ptychi-Evolve，一个用于叠层成像（Ptychography）的自主正则化算法发现框架。该框架利用大型语言模型（LLMs）来生成和演化新的正则化算法代码，并结合了进化机制（如语义引导的交叉和变异）。在三个具有挑战性的数据集（X射线集成电路、低剂量电子显微镜载铁蛋白、具有串扰伪影的多层成像）上的实验表明，发现的规则化器优于传统重建方法。该工作展示了LLMs与进化算法结合，在科学计算领域（特别是计算成像）进行算法自动发现的潜力。虽然应用领域是成像，但其核心范式——使用LLMs作为代码生成和演化的引擎，以自动发现优化特定目标函数（如图像质量指标）的算法——具有高度的通用性。这种“AI for Science”的自动化算法设计思路，完全可以应用于“化学大模型”的架构搜索、训练策略优化，或“质谱结构推理”中谱图解析、去卷积等算法的自动设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Ptychography is a computational imaging technique widely used for high-resolution materials characterization, but high-quality reconstructions often require the use of regularization functions that largely remain manually designed. We introduce Ptychi-Evolve, an autonomous framework that uses large language models (LLMs) to discover and evolve novel regularization algorithms. The framework combines LLM-driven code generation with evolutionary mechanisms, including semantically-guided crossover and mutation. Experiments on three challenging datasets (X-ray integrated circuits, low-dose electron microscopy of apoferritin, and multislice imaging with crosstalk artifacts) demonstrate that discovered regularizers outperform conventional reconstructions, achieving up to +0.26 SSIM and +8.3~dB PSNR improvements. Besides, Ptychi-Evolve records algorithm lineage and evolution metadata, enabling interpretable and reproducible analysis of discovered regularizers.

</details>

---

### 4. [Unsupervised domain adaptation for radioisotope identification in gamma spectroscopy](https://arxiv.org/abs/2603.05719)

**基本信息**

- 🔗 arXiv: [`2603.05719`](https://arxiv.org/abs/2603.05719)
- 👥 作者: Peter Lalor, Ayush Panigrahy, Alex Hagen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05719.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对“放射性核素识别”这一具体的分析化学任务，开发并评估基于深度学习的模型及其域适应方法。这直接属于“化学信息学”的应用范畴（将机器学习应用于化学数据分析）。虽然未直接提及“质谱”，但伽马能谱与质谱同属于分析化学中的谱学技术，其数据形式（谱图）和任务目标（从谱图识别物质）与“质谱结构推理”高度相似。因此，该工作解决的核心问题（如何利用模拟数据和域适应技术提升谱图识别模型的泛化能力）与“质谱结构推理”面临的关键挑战直接相关。

**📖 中文摘要**

这篇论文研究了使用伽马能谱进行放射性核素识别的无监督域适应（UDA）问题。训练用于放射性核素识别的机器学习模型面临的主要挑战是难以获取和标注大规模、多样化的实验数据集。模拟数据可以缓解这一问题，但在模拟数据上训练的模型部署到分布外的操作环境时，性能会严重下降。本研究证明，如果可以获得目标领域的未标记数据，无监督域适应可以提高基于合成数据训练的模型对新测试域的泛化能力。作者比较了一系列不同的UDA技术，发现最小化源域和目标域特征向量之间的最大均值差异（MMD）能最一致地提高测试分数。这项工作聚焦于一个具体的科学仪器数据分析任务（伽马能谱），并成功应用了深度学习中的域适应技术来提升模型在真实场景下的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training machine learning models for radioisotope identification using gamma spectroscopy remains an elusive challenge for many practical applications, largely stemming from the difficulty of acquiring and labeling large, diverse experimental datasets. Simulations can mitigate this challenge, but the accuracy of models trained on simulated data can deteriorate substantially when deployed to an out-of-distribution operational environment. In this study, we demonstrate that unsupervised domain adaptation (UDA) can improve the ability of a model trained on synthetic data to generalize to a new testing domain, provided unlabeled data from the target domain are available. Conventional supervised techniques are unable to utilize this data because the absence of isotope labels precludes defining a supervised classification loss. Instead, we first pretrain a spectral classifier using labeled synthetic data and subsequently leverage unlabeled target data to align the learned feature representations between the source and target domains. We compare a range of different UDA techniques, finding that minimizing the maximum mean discrepancy (MMD) between source and target feature vectors yields the most consistent improvement to testing scores. For instance, using a custom transformer-based neural network, we achieved a testing accuracy of $0.904 \pm 0.022$ on an experimental LaBr$_3$ test set after performing unsupervised feature alignment via MMD minimization, compared to $0.754 \pm 0.014$ before alignment. Overall, our results highlight the potential of using UDA to adapt a radioisotope classifier trained on synthetic data for real-world deployment.

</details>

---

### 5. [A Quantization-Aware Training Based Lightweight Method for Neural Distinguishers](https://arxiv.org/abs/2603.05791)

**基本信息**

- 🔗 arXiv: [`2603.05791`](https://arxiv.org/abs/2603.05791)
- 👥 作者: Guangwei Xiong, Linyuan Wang, Zhizhong Zheng 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05791.pdf)

**💡 相关性分析**

满足标准2：论文提出的量化感知训练和轻量化神经网络架构方法，虽然应用于密码分析，但其核心思想（模型压缩、运算简化、特征提取）与构建用于化学信息学或质谱结构推理的高效、可解释计算模型高度相关，可被视为一种潜在的工具或方法资源。

**📖 中文摘要**

本文提出了一种基于量化感知训练的轻量化神经区分器，用于分析SPECK轻量级分组密码。该方法利用可学习步长量化将模型权重量化为1.58比特，从而将所有卷积乘法运算替换为布尔逻辑运算。ReLU激活函数也被重新实现为基于比较的指示函数。这使得原本依赖32位乘法的架构转变为仅由布尔运算、加法和指示函数组成的轻量级结构。实验结果表明，该方法显著降低了计算复杂度，总运算量仅为Gohr原始模型的13.9%，同时分类精度仅下降2.87%。这项工作展示了如何将深度学习模型（特别是用于密码分析的神经区分器）进行轻量化改造，其方法（量化、布尔化）与构建高效、可解释的化学信息学或质谱分析模型有潜在关联。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In 2019, Gohr pioneered the application of deep neural networks to differential cryptanalysis, developing DNN-based neural distinguisher classifiers to analyze the SPECK lightweight block cipher. Unlike traditional differential analysis, which relies on Boolean operations on 0-1 sequences, neural distinguishers extract continuous features, introducing 32-bit multiplications operations that increase complexity and potential redundancy. This study proposes a lightweight neural distinguisher based on quantization-aware training. Leveraging learnable step-size quantization, the model's weights are quantized to 1.58 bits, enabling the replacement of all convolutional multiplication operations with Boolean logic. Additionally, the ReLU activation function is reimplemented as a comparison-based indicator function. This transforms the original 32-bit multiplication-dependent architecture into a lightweight structure composed solely of Boolean operations, additions, and indicator functions. Experimental results confirm significant computational complexity reduction. Owing to a high proportion of zero-valued weights, the total operations amount to just 13.9% of Gohr's model. Critically, the most costly 32-bit multiplications are eliminated, with classification accuracy dropping by only 2.87%. When applied exclusively to the initial convolutional layer, the 128 1-by-1 convolutions are replaced with 4 Boolean operations on 16-bit sequences, incurring a negligible 0.3% accuracy loss.

</details>

---

### 6. [Sparse Crosscoders for diffing MoEs and Dense models](https://arxiv.org/abs/2603.05805)

**基本信息**

- 🔗 arXiv: [`2603.05805`](https://arxiv.org/abs/2603.05805)
- 👥 作者: Marmik Chaudhari, Nishkal Hundia, Idhant Gulati
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05805.pdf)

**💡 相关性分析**

满足标准2：论文提出的交叉编码器和特征分析方法，为理解和比较复杂模型（如MoE）的内部表示提供了系统工具。这种对模型内部表示和特征的专业化/通用化模式的分析，对于理解和设计用于化学信息学（如分子表示学习）或质谱数据分析的“化学大模型”具有重要的方法论参考价值。

**📖 中文摘要**

本文使用交叉编码器（一种稀疏自编码器变体）来系统比较混合专家模型（MoE）和稠密模型的内部表示。研究在代码、科学文本和英文故事上训练了具有相等活跃参数的5层稠密模型和MoE模型。通过使用具有明确指定共享特征的BatchTopK交叉编码器，实现了约87%的分数方差解释，并揭示了特征组织上的具体差异。研究发现，与稠密模型相比，MoE学习到的独特特征数量显著更少。MoE特定特征也比共享特征表现出更高的激活密度，而稠密特定特征则显示出较低的密度。分析表明，MoE形成了更专业化、更聚焦的表示，而稠密模型则在更广泛、更通用的特征间分布信息。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture of Experts (MoE) achieve parameter-efficient scaling through sparse expert routing, yet their internal representations remain poorly understood compared to dense models. We present a systematic comparison of MoE and dense model internals using crosscoders, a variant of sparse autoencoders, that jointly models multiple activation spaces. We train 5-layer dense and MoEs (equal active parameters) on 1B tokens across code, scientific text, and english stories. Using BatchTopK crosscoders with explicitly designated shared features, we achieve $\sim 87\%$ fractional variance explained and uncover concrete differences in feature organization. The MoE learns significantly fewer unique features compared to the dense model. MoE-specific features also exhibit higher activation density than shared features, whereas dense-specific features show lower density. Our analysis reveals that MoEs develop more specialized, focused representations while dense models distribute information across broader, more general-purpose features.

</details>

---

### 7. [MoE Lens -- An Expert Is All You Need](https://arxiv.org/abs/2603.05806)

**基本信息**

- 🔗 arXiv: [`2603.05806`](https://arxiv.org/abs/2603.05806)
- 👥 作者: Marmik Chaudhari, Idhant Gulati, Nishkal Hundia 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05806.pdf)

**💡 相关性分析**

满足标准2：论文对MoE模型内部工作机制和专家专业化的深入分析，为理解和优化大模型（包括潜在的“化学大模型”）的结构和效率提供了重要见解。其分析工具和结论（如专家集中性、路由模式）可用于指导面向化学或质谱数据的大规模专业模型的架构设计与知识组织。

**📖 中文摘要**

本文对混合专家模型（MoE）中的专家专业化行为进行了系统分析，通过两种互补方法：特定领域的路由模式，以及跟踪专家对输出表示贡献的早期解码框架。对DeepSeekMoE模型的分析表明，尽管模型有64个路由专家，每层计算激活6个，但模型主要依赖少数几个专业化专家，其中权重最高的专家的输出与完整集成预测非常接近。通过对令牌路由分布的系统分析定量验证了这些发现，表明极少数专家处理了超过50%的不同专业领域的路由决策。单专家与集成专家在各层的隐藏状态相似度极高，某些层的余弦相似度高达0.95，当在所有三个领域使用单个专家时，困惑度仅增加5%。结果表明，MoE模型表现出集中的专业知识，这突出了通过有针对性的专家修剪进行推理优化的潜在机会，同时为研究这些模型中学习知识的定位开辟了途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture of Experts (MoE) models enable parameter-efficient scaling through sparse expert activations, yet optimizing their inference and memory costs remains challenging due to limited understanding of their specialization behavior. We present a systematic analysis of expert specialization in MoEs through two complementary approaches: domain-specific routing patterns and an early decoding framework that tracks expert contributions to output representations. Our analysis of the DeepSeekMoE model reveals that despite having 64 routed experts with 6 active for each layer's computation, the model predominantly relies on a few specialized experts, with the top-weighted expert's output closely approximating the full ensemble prediction. We quantitatively validate these findings through a systematic analysis of the token routing distribution, demonstrating that very few experts handle over 50\% of routing decisions across different specialized domains. Hidden state similarity between single and ensemble experts for every layer is extremely high, with some layers having cosine similarity as high as 0.95 and perplexity increasing by only 5\% when using a single expert across all three domains. Our results indicate that Mixture of Experts models exhibit concentrated expertise highlighting potential opportunities for inference optimization through targeted expert pruning while maintaining model performance and opening avenues towards studying localization of learned knowledge in these models.

</details>

---

### 8. [Self-Auditing Parameter-Efficient Fine-Tuning for Few-Shot 3D Medical Image Segmentation](https://arxiv.org/abs/2603.05822)

**基本信息**

- 🔗 arXiv: [`2603.05822`](https://arxiv.org/abs/2603.05822)
- 👥 作者: Son Thai Ly, Hien V. Nguyen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05822.pdf)

**💡 相关性分析**

满足标准2：论文提出的SEA-PEFT框架是一种新颖、自动化的参数高效微调方法，特别适用于数据稀缺场景。这种自适应、可审计的模型微调机制，对于在化学信息学或质谱分析领域，利用有限标注数据对预训练大模型进行领域适配和任务定制具有重要的工具参考价值。

**📖 中文摘要**

本文针对少样本3D医学图像分割中基础模型适应新临床站点的挑战，提出了SEA-PEFT（自审计参数高效微调）方法。该方法将适配器配置视为在线分配问题，在微调过程中解决，而非通过手动、固定拓扑选择。SEA-PEFT采用搜索-审计-分配循环：训练活跃适配器，通过暂时关闭每个适配器来估计其Dice效用，然后使用贪心背包分配器在参数预算下重新选择活跃集。结合指数移动平均和四分位距平滑以及有限状态排名控制器，稳定了循环并提高了高噪声少样本场景下的可靠性。在TotalSegmentator和FLARE'22数据集上的实验表明，SEA-PEFT在1/5/10样本设置下，相比最强的固定拓扑PEFT基线，平均Dice提高了2.4-2.8个点，同时训练参数少于1%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adapting foundation models to new clinical sites remains challenging in practice. Domain shift and scarce annotations must be handled by experts, yet many clinical groups do not have ready access to skilled AI engineers to tune adapter designs and training recipes. As a result, adaptation cycles can stretch from weeks to months, particularly in few-shot settings. Existing PEFT methods either require manual adapter configuration or automated searches that are computationally infeasible in few-shot 3D settings. We propose SEA-PEFT (SElf-Auditing Parameter-Efficient Fine-Tuning) to automate this process. SEA-PEFT treats adapter configuration as an online allocation problem solved during fine-tuning rather than through manual, fixed-topology choices. SEA-PEFT uses a search-audit-allocate loop that trains active adapters, estimates each adapter's Dice utility by momentarily toggling it off, and then reselects the active set under a parameter budget using a greedy knapsack allocator. Exponential Moving Average and Interquartile Range smoothing, together with a Finite-State Ranking controller, stabilize the loop and improve reliability in high-noise few-shot regimes. On TotalSegmentator and FLARE'22, SEA-PEFT improves mean Dice by 2.4--2.8 points over the strongest fixed-topology PEFT baselines across 1/5/10-shot settings while training <1% of parameters. For reproducibility purposes, we made our code publicly available at this https URL

</details>

---

### 9. [HART: Data-Driven Hallucination Attribution and Evidence-Based Tracing for Large Language Models](https://arxiv.org/abs/2603.05828)

**基本信息**

- 🔗 arXiv: [`2603.05828`](https://arxiv.org/abs/2603.05828)
- 👥 作者: Shize Liang, Hongzhi Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05828.pdf)

**💡 相关性分析**

满足标准2：论文提出的HART框架和配套的结构化数据集，为分析和归因大模型（包括潜在的“化学大模型”）的生成错误（如预测错误的分子结构或质谱解析结果）提供了系统化的工具和方法论。这对于提高化学领域大模型的可信度和可解释性至关重要。

**📖 中文摘要**

本文针对大语言模型（LLM）生成幻觉内容的问题，提出了HART（细粒度幻觉归因与证据检索）框架。HART将幻觉追踪形式化为一个结构化建模任务，包含四个阶段：片段定位、机制归因、证据检索和因果追踪。基于此，作者构建了首个为幻觉追踪量身定制的结构化数据集，其中幻觉类型、错误机制和反事实证据集被联合标注，以实现因果级可解释性评估。实验结果表明，HART在提出的数据集上显著优于BM25和DPR等强检索基线，验证了所提出的追踪范式在幻觉分析和证据对齐方面的有效性和泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated remarkable performance in text generation and knowledge-intensive question answering. Nevertheless, they are prone to producing hallucinated content, which severely undermines their reliability in high-stakes application domains. Existing hallucination attribution approaches, based on either external knowledge retrieval or internal model mechanisms, primarily focus on semantic similarity matching or representation-level discrimination. As a result, they have difficulty establishing structured correspondences at the span level between hallucination types, underlying error generation mechanisms, and external factual evidence, thereby limiting the interpretability of hallucinated fragments and the traceability of supporting or opposing evidence. To address these limitations, we propose HART, a fine-grained hallucination attribution and evidence retrieval framework for large language models. HART formalizes hallucination tracing as a structured modeling task comprising four stages: span localization, mechanism attribution, evidence retrieval, and causal tracing. Based upon this formulation, we develop the first structured dataset tailored for hallucination tracing, in which hallucination types, error mechanisms, and sets of counterfactual evidence are jointly annotated to enable causal-level interpretability evaluation. Experimental results on the proposed dataset demonstrate that HART substantially outperforms strong retrieval baselines, including BM25 and DPR, validating the effectiveness and generalization capability of the proposed tracing paradigm for hallucination analysis and evidence alignment.

</details>

---

### 10. [Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery](https://arxiv.org/abs/2603.05860)

**基本信息**

- 🔗 arXiv: [`2603.05860`](https://arxiv.org/abs/2603.05860)
- 👥 作者: Lin Fan, Pengyu Dai, Zhipeng Deng 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05860.pdf)

**💡 相关性分析**

满足标准2：论文提出的MACRO框架展示了一种智能体通过经验自动发现和合成高级工具（复合工具）的自我进化机制。这种机制对于构建能够自主探索化学信息学或质谱分析工作流（例如，组合不同的计算工具或解析步骤）的“化学大模型”或分析智能体具有重要的启发性和工具参考价值。

**📖 中文摘要**

本文针对临床图像解读的多步骤、工具中心化特点，以及现有LLM智能体工具集和调用策略静态化导致的脆弱性问题，提出了MACRO，一种自进化、经验增强的医学智能体。该智能体从经验驱动的工具发现转向：从已验证的执行轨迹中，自主识别反复有效的多步骤工具序列，将其合成为可复用的复合工具，并注册为新的高级原语，持续扩展其行为库。轻量级的图像特征记忆将工具选择锚定在视觉-临床上下文中，而类似GRPO的训练循环则强化了对已发现复合工具的可靠调用，实现了以最小监督进行闭环自我改进。跨多个医学成像数据集和任务的广泛实验表明，自主复合工具发现 consistently 提高了多步骤编排的准确性和跨领域泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Clinical image interpretation is inherently multi-step and tool-centric: clinicians iteratively combine visual evidence with patient context, quantify findings, and refine their decisions through a sequence of specialized procedures. While LLM-based agents promise to orchestrate such heterogeneous medical tools, existing systems treat tool sets and invocation strategies as static after deployment. This design is brittle under real-world domain shifts, across tasks, and evolving diagnostic requirements, where predefined tool chains frequently degrade and demand costly manual re-design. We propose MACRO, a self-evolving, experience-augmented medical agent that shifts from static tool composition to experience-driven tool discovery. From verified execution trajectories, the agent autonomously identifies recurring effective multi-step tool sequences, synthesizes them into reusable composite tools, and registers these as new high-level primitives that continuously expand its behavioral repertoire. A lightweight image-feature memory grounds tool selection in a visual-clinical context, while a GRPO-like training loop reinforces reliable invocation of discovered composites, enabling closed-loop self-improvement with minimal supervision. Extensive experiments across diverse medical imaging datasets and tasks demonstrate that autonomous composite tool discovery consistently improves multi-step orchestration accuracy and cross-domain generalization over strong baselines and recent state-of-the-art agentic methods, bridging the gap between brittle static tool use and adaptive, context-aware clinical AI assistance. Code will be available upon acceptance.

</details>

---

### 11. [ReflexiCoder: Teaching Large Language Models to Self-Reflect on Generated Code and Self-Correct It via Reinforcement Learning](https://arxiv.org/abs/2603.05863)

**基本信息**

- 🔗 arXiv: [`2603.05863`](https://arxiv.org/abs/2603.05863)
- 👥 作者: Juyong Jiang, Jiasi Shen, Sunghun Kim 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05863.pdf)

**💡 相关性分析**

满足标准2：论文提出的ReflexiCoder框架，通过强化学习将自我反思和纠错能力内化到代码生成模型中。这种使模型具备内在调试和优化能力的范式，对于开发能够自主验证、修正其化学结构推理或质谱解析结果的“化学大模型”或分析智能体，提供了极具潜力的方法学工具和架构思路。

**📖 中文摘要**

本文提出了ReflexiCoder，一种新颖的强化学习（RL）框架，旨在将结构化的推理轨迹（包括初始生成、bug和优化感知的反思以及自我纠正）内化到模型权重中。与依赖外部反馈的方法不同，ReflexiCoder将范式从外部依赖的细化转变为在推理时具备内在的、完全自主的自我反思和自我纠正能力。该框架采用RL-zero训练范式和细粒度奖励函数来优化整个反思-纠正轨迹，教导模型如何在推理时不依赖真实反馈或执行引擎进行调试。在七个基准测试上的广泛实验表明，ReflexiCoder-8B在1.5B-14B参数范围的开源模型中达到了新的最先进水平，并且在单次尝试设置下，推理计算开销通过有纪律的、高速的推理和反思模式减少了约40%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Large Language Models (LLMs) have revolutionized code generation, standard "System 1" approaches, generating solutions in a single forward pass, often hit a performance ceiling when faced with complex algorithmic tasks. Existing iterative refinement strategies attempt to bridge this gap at inference time, yet they predominantly rely on external oracles, execution feedback, or computationally expensive prompt-response cycles. In this work, we propose ReflexiCoder, a novel reinforcement learning (RL) framework that internalizes the structured reasoning trajectory, encompassing initial generation, bug and optimization aware reflection, and self-correction, directly into the model's weights. Unlike prior methods, ReflexiCoder shifts the paradigm from external-dependent refinement to an intrinsic, fully autonomous self-reflection and self-correction capabilities at inference time. We utilize an RL-zero training paradigm with granular reward functions to optimize the entire reflection-correction trajectory, teaching the model how to debug without reliance on ground-truth feedback or execution engines at inference time. Extensive experiments across seven benchmarks demonstrate that our ReflexiCoder-8B establishes a new state-of-the-art (SOTA) among leading open-source models in the 1.5B-14B range, achieving 94.51% (87.20%) on HumanEval (Plus), 81.80% (78.57%) on MBPP (Plus), 35.00% on BigCodeBench, 52.21% on LiveCodeBench, and 37.34% on CodeForces in a single-attempt setting, rivaling or surpassing proprietary models like GPT-5.1. Notably, our framework is significantly more token-efficient than base models, reducing inference-time compute overhead by approximately 40% through disciplined, high-speed reasoning and reflection patterns. Source code is available at this https URL .

</details>

---

### 12. [TumorChain: Interleaved Multimodal Chain-of-Thought Reasoning for Traceable Clinical Tumor Analysis](https://arxiv.org/abs/2603.05867)

**基本信息**

- 🔗 arXiv: [`2603.05867`](https://arxiv.org/abs/2603.05867)
- 👥 作者: Sijing Li, Zhongwei Qiu, Jiang Liu 等25人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05867.pdf)

**💡 相关性分析**

满足标准2：论文提出的TumorChain框架和TumorCoT数据集，为构建具有可解释、多步骤推理能力的医学多模态大模型提供了完整的范例。其核心思想（链式思维、跨模态对齐、自我优化）可直接借鉴用于构建面向“质谱结构推理”的类似系统，即从原始谱图数据出发，通过多步推理得出化合物结构结论。

**📖 中文摘要**

本文针对临床肿瘤分析任务，构建了一个大规模基准测试，将多模态推理流程操作化，涵盖影像发现、临床印象和病理预测。作者策划了TumorCoT，一个包含150万条带有CoT标注的VQA指令与3D CT扫描配对的大规模数据集，具有从发现到印象再到病理的步骤对齐原理和跨模态对齐，能够评估答案准确性和推理一致性。进一步提出了TumorChain，一个多模态交错推理框架，紧密耦合3D影像编码器、临床文本理解和器官级视觉-语言对齐。通过跨模态对齐和迭代交错因果推理，TumorChain在多次自我优化循环后，基于视觉证据得出结论并发布病理预测，提高了可追溯性并降低了幻觉风险。实验表明，该方法在病灶检测、印象生成和病理分类方面 consistently 优于强基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate tumor analysis is central to clinical radiology and precision oncology, where early detection, reliable lesion characterization, and pathology-level risk assessment guide diagnosis and treatment planning. Chain-of-Thought (CoT) reasoning is particularly important in this setting because it enables step-by-step interpretation from imaging findings to clinical impressions and pathology conclusions, improving traceability and reducing diagnostic errors. Here, we target the clinical tumor analysis task and build a large-scale benchmark that operationalizes a multimodal reasoning pipeline, spanning findings, impressions, and pathology predictions. We curate TumorCoT, a large-scale dataset of 1.5M CoT-labeled VQA instructions paired with 3D CT scans, with step-aligned rationales and cross-modal alignments along the trajectory from findings to impression to pathology, enabling evaluation of both answer accuracy and reasoning consistency. We further propose TumorChain, a multimodal interleaved reasoning framework that tightly couples 3D imaging encoders, clinical text understanding, and organ-level vision-language alignment. Through cross-modal alignment and iterative interleaved causal reasoning, TumorChain grounds visual evidence, aggregates conclusions, and issues pathology predictions after multiple rounds of self-refinement, improving traceability and reducing hallucination risk. Experiments show consistent improvements over strong baselines in lesion detection, impression generation, and pathology classification, and demonstrate strong generalization on the DeepTumorVQA benchmark. These results highlight the potential of multimodal reasoning for reliable and interpretable tumor analysis in clinical practice. Detailed information about our project can be found on our project homepage at this https URL .

</details>

---

### 13. [PatchCue: Enhancing Vision-Language Model Reasoning with Patch-Based Visual Cues](https://arxiv.org/abs/2603.05869)

**基本信息**

- 🔗 arXiv: [`2603.05869`](https://arxiv.org/abs/2603.05869)
- 👥 作者: Yukun Qi, Pei Fu, Hang Li 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05869.pdf)

**💡 相关性分析**

满足标准2：论文提出的PatchCue范式，为增强多模态大模型（VLMs）的视觉推理能力提供了一种新的、与模型架构（patch tokenization）天然契合的方法。这种在图像块级别注入视觉提示以引导推理的思路，对于开发能够结合质谱图像、分子结构图或其他化学可视化数据进行推理的“化学大模型”具有重要的方法论启示和工具潜力。

**📖 中文摘要**

本文提出了PatchCue，一种新颖的基于图像块（patch）的视觉提示范式，旨在显著增强视觉-语言模型（VLM）的视觉推理能力。通过将图像分割成块并在块级别表示提示，PatchCue更好地与人类感知习惯对齐，并利用了现代VLM的块-令牌化输入。作者采用两阶段方法训练VLM：首先进行冷启动监督微调以输出块级提示，然后使用过程监督的提示奖励进行强化学习，以指导中间视觉推理步骤。在多个VLM和多样化基准测试（包括通用视觉问答、复杂推理和文档理解）上的广泛实验表明，PatchCue consistently 提高了模型的整体性能。结果表明，块级提示在提供更有效、认知对齐的视觉推理范式方面，优于像素级边界框和基于点的提示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language Models (VLMs) have achieved remarkable progress on a wide range of challenging multimodal understanding and reasoning tasks. However, existing reasoning paradigms, such as the classical Chain-of-Thought (CoT), rely solely on textual information and often underutilize important visual cues. While prior work has incorporated pixel-level visual cues, these representations require precise spatial localization, introducing additional learning complexity. To address this, we propose PatchCue, a novel patch-based visual cue paradigm designed to significantly enhance the visual reasoning capabilities of VLMs. By partitioning images into patches and representing cues at the patch level, PatchCue aligns better with human perceptual habits and leverages the patch-tokenized input of modern VLMs. We train VLMs using a two-stage approach: cold-start supervised fine-tuning to output patch-level cues, followed by reinforcement learning with a process-supervised cue reward that guides intermediate visual reasoning steps. Extensive experiments on multiple VLMs and diverse benchmarks, including general visual question answering, complex reasoning, and document understanding, demonstrate that PatchCue consistently improves overall model performance. Our results show that patch-level cues outperform both pixel-level bounding boxes and point-based cues, providing a more effective and cognitively aligned visual reasoning paradigm.

</details>

---

### 14. [Computational Pathology in the Era of Emerging Foundation and Agentic AI -- International Expert Perspectives on Clinical Integration and Translational Readiness](https://arxiv.org/abs/2603.05884)

**基本信息**

- 🔗 arXiv: [`2603.05884`](https://arxiv.org/abs/2603.05884)
- 👥 作者: Qian Da, Yijiang Chen, Min Ju 等28人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05884.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对计算病理学领域新兴基础模型和智能体AI的综述与展望，深入讨论了其技术进展、临床整合挑战和未来方向。虽然领域是医学影像，但其对“基础模型”、“智能体”在科学领域应用的分析框架、面临的挑战（如数据、评估、部署）以及未来方向的思考，对“化学大模型”和“质谱分析”领域的研究者具有重要的借鉴和参考价值，属于重要的相关讨论。

**📖 中文摘要**

本文回顾了基础模型和智能体人工智能在计算病理学领域的突破，并探讨了其在临床整合和转化准备方面的挑战与前景。尽管在预测任务（如诊断、预后和治疗反应）的基准数据集中报告了性能提升，激发了临床应用的巨大热情，但现实世界的采用仍然滞后，因为实施面临经济、技术和行政挑战。本文超越了现有关于技术架构和比较性能的讨论，通过将可部署的临床相关性与下游分析能力及其技术成熟度、操作准备度以及经济和监管背景联系起来，考虑了这些新兴AI系统如何负责任地整合到医疗实践中。基于国际专家组的观点，本文对当前能力和患者护理环境中的采用障碍进行了实用评估。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent breakthroughs in artificial intelligence through foundation models and agents have accelerated the evolution of computational pathology. Demonstrated performance gains reported across academia in benchmarking datasets in predictive tasks such as diagnosis, prognosis, and treatment response have ignited substantial enthusiasm for clinical application. Despite this development momentum, real world adoption has lagged, as implementation faces economic, technical, and administrative challenges. Beyond existing discussions of technical architectures and comparative performance, this review considers how these emerging AI systems can be responsibly integrated into medical practice by connecting deployable clinical relevance with downstream analytical capabilities and their technical maturity, operational readiness, and economic and regulatory context. Drawing on perspectives from an international group, we provide a practical assessment of current capabilities and barriers to adoption in patient care settings.

</details>

---

### 15. [Reference-guided Policy Optimization for Molecular Optimization via LLM Reasoning](https://arxiv.org/abs/2603.05900)

**基本信息**

- 🔗 arXiv: [`2603.05900`](https://arxiv.org/abs/2603.05900)
- 👥 作者: Xuan Li, Zhanke Zhou, Zongze Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”的应用场景——分子优化。它提出了一种新的训练范式（RePO），专门用于解决基于LLM的分子优化中数据（仅有最终优化结果，无过程轨迹）和训练（探索与利用平衡）的挑战。这是与指定主题高度相关的核心研究。

**📖 中文摘要**

本文针对基于指令的分子优化任务（每个数据点通常只提供一个优化的参考分子，没有逐步优化轨迹），揭示了仅对参考分子进行答案式监督微调会导致推理崩溃，而带有可验证奖励的强化学习由于模型缺乏有效探索，在相似性约束下提供稀疏反馈，从而减慢学习并限制优化。为了在平衡利用参考分子的同时鼓励探索新分子，作者引入了参考引导的策略优化（RePO），一种无需轨迹数据即可从参考分子中学习的优化方法。在每次更新时，RePO从模型中采样带有中间推理轨迹的候选分子，并使用在RL方式下测量相似性约束下属性满足度的可验证奖励来训练模型。同时，它通过将策略的中间推理轨迹保持为上下文并仅以监督方式训练答案来应用参考引导。RL项促进探索，而引导项通过将输出锚定到参考分子来减轻奖励稀疏性并稳定训练。在分子优化基准测试中，RePO consistently 优于SFT和RLVR基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) benefit substantially from supervised fine-tuning (SFT) and reinforcement learning with verifiable rewards (RLVR) in reasoning tasks. However, these recipes perform poorly in instruction-based molecular optimization, where each data point typically provides only a single optimized reference molecule and no step-by-step optimization trajectory. We reveal that answer-only SFT on the reference molecules collapses reasoning, and RLVR provides sparse feedback under similarity constraints due to the model's lack of effective exploration, which slows learning and limits optimization. To encourage the exploration of new molecules while balancing the exploitation of the reference molecules, we introduce Reference-guided Policy Optimization (RePO), an optimization approach that learns from reference molecules without requiring trajectory data. At each update, RePO samples candidate molecules with their intermediate reasoning trajectories from the model and trains the model using verifiable rewards that measure property satisfaction under similarity constraints in an RL manner. Meanwhile, it applies reference guidance by keeping the policy's intermediate reasoning trajectory as context and training only the answer in a supervised manner. Together, the RL term promotes exploration, while the guidance term mitigates reward sparsity and stabilizes training by grounding outputs to references when many valid molecular edits exist. Across molecular optimization benchmarks, RePO consistently outperforms SFT and RLVR baselines (e.g., GRPO), achieving improvements on the optimization metric (Success Rate $\times$ Similarity), improving balance across competing objectives, and generalizing better to unseen instruction styles. Our code is publicly available at this https URL .

</details>

---

### 16. [CORE-Seg: Reasoning-Driven Segmentation for Complex Lesions via Reinforcement Learning](https://arxiv.org/abs/2603.05911)

**基本信息**

- 🔗 arXiv: [`2603.05911`](https://arxiv.org/abs/2603.05911)
- 👥 作者: Yuxin Xie, Yuming Chen, Yishan Yang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05911.pdf)

**💡 相关性分析**

满足标准2：论文提出的CORE-Seg框架将大语言模型的推理能力与分割任务相结合，并设计了专门的训练策略和奖励机制。这种“推理驱动分割”的范式，对于构建需要结合化学知识进行推理的“质谱结构推理”系统（即从谱图推理出结构，可视为一种特殊的“分割”或“解析”任务）具有重要的方法论参考价值。其框架和训练技术可作为相关工具。

**📖 中文摘要**

本文针对医学图像分割正从传统的视觉模式匹配向认知推理分析范式转变的背景，指出现有通用多模态大语言模型（MLLM）缺乏复杂病变所需的专业视觉推理能力，而传统分割模型擅长像素级分割但缺乏逻辑可解释性。为此，作者引入了ComLesion-14K，首个用于推理驱动的复杂病变分割的多样化思维链基准。为了完成此任务，提出了CORE-Seg，一个通过语义引导提示适配器将推理与分割集成的端到端框架。设计了从SFT到GRPO的渐进训练策略，并配备了自适应双粒度奖励机制以减轻奖励稀疏性。该方法取得了最先进的结果，平均Dice为37.06%（比第二好的基线高14.89%），同时将失败率降低到18.42%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medical image segmentation is undergoing a paradigm shift from conventional visual pattern matching to cognitive reasoning analysis. Although Multimodal Large Language Models (MLLMs) have shown promise in integrating linguistic and visual knowledge, significant gaps remain: existing general MLLMs possess broad common sense but lack the specialized visual reasoning required for complex lesions, whereas traditional segmentation models excel at pixel-level segmentation but lack logical interpretability. In this paper, we introduce ComLesion-14K, the first diverse Chain-of-Thought (CoT) benchmark for reasoning-driven complex lesion segmentation. To accomplish this task, we propose CORE-Seg, an end-to-end framework integrating reasoning with segmentation through a Semantic-Guided Prompt Adapter. We design a progressive training strategy from SFT to GRPO, equipped with an adaptive dual-granularity reward mechanism to mitigate reward sparsity. Our Method achieves state-of-the-art results with a mean Dice of 37.06\% (14.89\% higher than the second-best baseline), while reducing the failure rate to 18.42\%. Project Page: this https URL

</details>

---

### 17. [RAC: Rectified Flow Auto Coder](https://arxiv.org/abs/2603.05925)

**基本信息**

- 🔗 arXiv: [`2603.05925`](https://arxiv.org/abs/2603.05925)
- 👥 作者: Sen Fang, Yalin Feng, Yanxin Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种新型的生成模型架构（Rectified Flow Auto Coder），这属于化学信息学中用于分子生成和表示的“化学大模型”范畴。

**📖 中文摘要**

本文提出了一种名为Rectified Flow Auto Coder (RAC)的生成模型，旨在替代传统的变分自编码器(VAE)。RAC的核心思想是受Rectified Flow启发，通过将解码器应用于流时间步来实现多步解码。其解码路径是笔直且可修正的，支持逐步细化。该模型本质上支持双向推理，其中解码器通过时间反转充当编码器（因此称为Coder而非编码器或解码器），将参数数量减少了近41%。这种生成式解码方法通过允许模型沿路径修正潜在变量，部分解决了重建与生成之间的差距，从而提高了生成质量。实验表明，RAC在重建和生成方面均超越了最先进的VAE，且计算成本降低了约70%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we propose a Rectified Flow Auto Coder (RAC) inspired by Rectified Flow to replace the traditional VAE: 1. It achieves multi-step decoding by applying the decoder to flow timesteps. Its decoding path is straight and correctable, enabling step-by-step refinement. 2. The model inherently supports bidirectional inference, where the decoder serves as the encoder through time reversal (hence Coder rather than encoder or decoder), reducing parameter count by nearly 41%. 3. This generative decoding method improves generation quality since the model can correct latent variables along the path, partially addressing the reconstruction--generation gap. Experiments show that RAC surpasses SOTA VAEs in both reconstruction and generation with approximately 70% lower computational cost.

</details>

---

### 18. [PriorIDENT: Prior-Informed PDE Identification from Noisy Data](https://arxiv.org/abs/2603.05946)

**基本信息**

- 🔗 arXiv: [`2603.05946`](https://arxiv.org/abs/2603.05946)
- 👥 作者: Cheng Tang, Hao Liu, Dong Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05946.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种从数据中识别物理定律（PDE）的算法框架。这直接属于“化学大模型”中利用AI/机器学习进行科学发现（如发现物理方程、化学反应动力学）的子领域，是化学信息学和计算化学中模型构建的重要方向。

**📖 中文摘要**

本文提出了一种先验信息驱动的弱形式稀疏回归框架，用于从噪声时空数据中识别控制偏微分方程(PDE)。该方法通过将导数转移到平滑的测试函数上，解决了噪声放大和过完备库的模糊性问题。其设计编码了三种紧凑的物理先验：哈密顿量（斜梯度和能量守恒）、守恒定律（具有共享交叉方向系数的通量形式）和能量最小化（变分、耗散），从而确保所有候选特征在构造上都是物理上可接受的。这些与先验一致的库与一个通过修剪和残差缩减模型选择增强的子空间追踪流程相结合，以产生简约、可解释的模型。在包括哈密顿振荡器、三体问题、粘性Burgers方程、二维浅水方程以及扩散和Allen-Cahn动力学在内的典型系统上的实验表明，该方法在存在大量噪声的情况下，实现了更高的真阳性率、稳定的系数恢复和结构保持的动力学，在强形式和弱形式设置下均持续优于无先验基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Identifying governing partial differential equations (PDEs) from noisy spatiotemporal data remains challenging due to differentiation-induced noise amplification and ambiguity from overcomplete libraries. We propose a prior-informed weak-form sparse-regression framework that resolves both issues by refining the dictionary before regression and shifting derivatives onto smooth test functions. Our design encodes three compact physics priors-Hamiltonian (skew-gradient and energy-conserving), conservation-law (flux-form with shared cross-directional coefficients), and energy-minimization (variational, dissipative)-so that all candidate features are physically admissible by construction. These prior-consistent libraries are coupled with a subspace-pursuit pipeline enhanced by trimming and residual-reduction model selection to yield parsimonious, interpretable models. Across canonical systems-including Hamiltonian oscillators and the three-body problem, viscous Burgers and two-dimensional shallow-water equations, and diffusion and Allen--Cahn dynamics-our method achieves higher true-positive rates, stable coefficient recovery, and structure-preserving dynamics under substantial noise, consistently outperforming no-prior baselines in both strong- and weak-form settings. The results demonstrate that compact structural priors, when combined with weak formulations, provide a robust and unified route to physically faithful PDE identification from noisy data.

</details>

---

### 19. [THETA: A Textual Hybrid Embedding-based Topic Analysis Framework and AI Scientist Agent for Scalable Computational Social Science](https://arxiv.org/abs/2603.05972)

**基本信息**

- 🔗 arXiv: [`2603.05972`](https://arxiv.org/abs/2603.05972)
- 👥 作者: Zhenke Duan, Xin Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05972.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于主题分析的AI框架（THETA），它结合了领域自适应微调和大语言模型。这属于“化学大模型”在文本分析（如科学文献挖掘、专利分析）和知识发现方面的应用，是化学信息学的核心任务之一。

**📖 中文摘要**

本文介绍了文本混合嵌入主题分析（THETA），这是一种新颖的计算范式和开源工具，旨在弥合大规模数据与丰富理论深度之间的鸿沟。THETA通过在大规模嵌入模型上实现领域自适应微调（DAFT）来超越基于频率的统计，有效优化特定社会语境中的语义向量结构以捕捉潜在含义。为确保认识论上的严谨性，我们将此过程封装到一个AI科学家代理框架中，该框架由数据管理员、建模分析师和领域专家代理组成，以模拟扎根理论中核心的人类参与专家判断和持续比较过程。该框架使代理能够迭代评估算法聚类、执行跨主题语义对齐，并将原始输出提炼为逻辑一致的理论类别。为了验证THETA的有效性，我们在金融监管和公共卫生等六个领域进行了实验。结果表明，THETA在捕捉领域特定解释结构的同时保持卓越的连贯性方面，显著优于LDA、ETM和CTM等传统模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The explosion of big social data has created a scalability trap for traditional qualitative research, as manual coding remains labor-intensive and conventional topic models often suffer from semantic thinning and a lack of domain awareness. This paper introduces Textual Hybrid Embedding based Topic Analysis (THETA), a novel computational paradigm and open-source tool designed to bridge the gap between massive data scale and rich theoretical depth. THETA moves beyond frequency-based statistics by implementing Domain-Adaptive Fine-tuning (DAFT) via LoRA on foundation embedding models, which effectively optimizes semantic vector structures within specific social contexts to capture latent meanings. To ensure epistemological rigor, we encapsulate this process into an AI Scientist Agent framework, comprising Data Steward, Modeling Analyst, and Domain Expert agents, to simulate the human-in-the-loop expert judgment and constant comparison processes central to grounded theory. Departing from purely computational models, this framework enables agents to iteratively evaluate algorithmic clusters, perform cross-topic semantic alignment, and refine raw outputs into logically consistent theoretical categories. To validate the effectiveness of THETA, we conducted experiments across six domains, including financial regulation and public health. Our results demonstrate that THETA significantly outperforms traditional models, such as LDA, ETM, and CTM, in capturing domain-specific interpretive constructs while maintaining superior coherence. By providing an interactive analysis platform, THETA democratizes advanced natural language processing for social scientists and ensures the trustworthiness and reproducibility of research findings. Code is available at this https URL .

</details>

---

### 20. [An Interactive Multi-Agent System for Evaluation of New Product Concepts](https://arxiv.org/abs/2603.05980)

**基本信息**

- 🔗 arXiv: [`2603.05980`](https://arxiv.org/abs/2603.05980)
- 👥 作者: Bin Xuan, Ruo Ai, Hakyeon Lee
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05980.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个基于大语言模型的多智能体系统，用于自动化评估和决策支持。这属于“化学大模型”在辅助研发、决策制定和知识管理方面的应用，与化学信息学中利用AI进行分子设计、反应优化和实验室自动化的目标高度相关。

**📖 中文摘要**

本文提出了一种利用基于大语言模型（LLM）的多智能体系统（MAS）来自动化产品概念评估的方法。通过系统分析先前关于产品开发和团队协作的研究，本研究建立了两个主要的评估维度：技术可行性和市场可行性。所提出的系统由代表研发和营销等专业领域的八个虚拟代理组成。这些代理使用检索增强生成（RAG）和实时搜索工具来收集客观证据，并基于既定标准通过结构化审议来验证概念。此外，还使用专业产品评论数据对这些代理进行了微调，以提高其判断准确性。一项涉及专业显示监视器概念的案例研究表明，该系统的评估排名与资深行业专家的排名一致。这些结果证实了所提出的基于多智能体的评估方法在支持产品开发决策方面的可用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Product concept evaluation is a critical stage that determines strategic resource allocation and project success in enterprises. However, traditional expert-led approaches face limitations such as subjective bias and high time and cost requirements. To support this process, this study proposes an automated approach utilizing a large language model (LLM)-based multi-agent system (MAS). Through a systematic analysis of previous research on product development and team collaboration, this study established two primary evaluation dimensions, namely technical feasibility and market feasibility. The proposed system consists of a team of eight virtual agents representing specialized domains such as R&D and marketing. These agents use retrieval-augmented generation (RAG) and real-time search tools to gather objective evidence and validate concepts through structured deliberations based on the established criteria. The agents were further fine-tuned using professional product review data to enhance their judgment accuracy. A case study involving professional display monitor concepts demonstrated that the system's evaluation rankings were consistent with those of senior industry experts. These results confirm the usability of the proposed multi-agent-based evaluation approach for supporting product development decisions.

</details>

---

### 21. [HarvestFlex: Strawberry Harvesting via Vision-Language-Action Policy Adaptation in the Wild](https://arxiv.org/abs/2603.05982)

**基本信息**

- 🔗 arXiv: [`2603.05982`](https://arxiv.org/abs/2603.05982)
- 👥 作者: Ziyang Zhao, Shuheng Wang, Zhonghua Miao 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05982.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发并微调视觉-语言-动作（VLA）模型，用于机器人任务执行。这属于“化学大模型”在机器人学和自动化实验（如自动化合成、材料处理）中的应用，是化学信息学与自动化交叉的前沿领域。

**📖 中文摘要**

本研究提出了首个关于在真实温室桌面草莓采摘场景中迁移视觉-语言-动作（VLA）策略的研究，这是一个受遮挡和镜面反射挑战的长时程、非结构化任务。我们在HarvestFlex平台上构建了一个端到端的闭环系统，使用三视图RGB传感（两个固定场景视图加一个腕戴式视图），并有意避免使用深度点云和显式几何标定。我们收集了3.71小时的VR遥操作演示（227个片段），并使用全微调和LoRA对pi_0、pi_0.5和WALL-OSS模型进行了微调。在统一的50次真实温室试验协议和涵盖完成度、成功率、采摘时间和损坏率的指标下，经过全微调的pi_0.5模型实现了74.0%的成功率、32.6秒/次的采摘时间和4.1%的损坏率。异步推理-控制解耦进一步提高了相对于同步部署的性能。结果表明，仅用不到四小时的真实数据即可实现非平凡的闭环采摘，同时仍受限于近距离可观测性损失和接触动力学不匹配。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work presents the first study on transferring vision-language-action (VLA) policies to real greenhouse tabletop strawberry harvesting, a long-horizon, unstructured task challenged by occlusion and specular reflections. We built an end-to-end closed-loop system on the HarvestFlex platform using three-view RGB sensing (two fixed scene views plus a wrist-mounted view) and intentionally avoided depth clouds and explicit geometric calibration. We collected 3.71 h of VR teleoperated demonstrations (227 episodes) and fine-tuned pi_0, pi_0.5, and WALL-OSS with full fine-tuning and LoRA. Under a unified 50 trials real-greenhouse protocol and metrics spanning completion, pi_0.5 with full fine-tuning achieved success rate of 74.0% with 32.6 s/pick and damage rate of 4.1%. Asynchronous inference-control decoupling further improved performance over synchronous deployment. Results showed non-trivial closed-loop picking with fewer than four hours of real data, while remaining limited by close-range observability loss and contact-dynamics mismatch. A demonstration video is available at: this https URL .

</details>

---

### 22. [Fostering Knowledge Infrastructures in Science Communication and Aerospace Engineering](https://arxiv.org/abs/2603.05984)

**基本信息**

- 🔗 arXiv: [`2603.05984`](https://arxiv.org/abs/2603.05984)
- 👥 作者: Tim Wittenborg
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05984.pdf)

**💡 相关性分析**

满足标准2：论文讨论了构建知识基础设施（包括工具、工作流程和数据集）以支持特定领域（如科学传播）的研究。这提供了可用于“化学大模型”和“质谱结构推理”研究的数据管理、信息提取和知识表示的资源与方法论，符合“数据资源相关”标准。

**📖 中文摘要**

本文概述了如何利用科学传播和航空航天工程这两个用例来培育欠发达的知识基础设施。通过分析这些问题并确定可用解决方案，可以实现并评估支持协作基础设施的工具辅助工作流程。这些工作流程包括用于信息提取和处理的人机交互人工智能（AI）支持工作流程、基于维基和知识图谱的数字图书馆，以及利益相关者需求驱动的界面。虽然这些为工作流程自动化和知识表示开发的工具显示出前景，但仍存在重大挑战。未来的工作必须超越技术问题解决，解决阻碍特定领域知识联网的社会和法律障碍。除此之外，任何新兴知识基础设施的倡导者都欢迎应用本工作的发现来促进可用知识的联网。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Knowledge infrastructures are defined as robust networks of people, artifacts, and institutions that generate, share and maintain specific knowledge. Yet, many domains are fragmented and far from robustly networked, such as science communication or aerospace engineering. While FAIR (Findable, Accessible, Interoperable, Reusable) data management tools exist, their adoption in these domains is limited. Several challenges inhibit this adoption, from complex heterogeneous data formats to lack of structured support to outright incentives against collaboration or legal barriers. This doctoral work outlines how to foster underdeveloped knowledge infrastructures with the use-cases of science communication and aerospace engineering. By analyzing these problems and identifying available solutions, tool-supported workflows towards collaborative infrastructure can be implemented and evaluated. These include human-in-the-loop artificial intelligence (AI)-supported workflows for information extraction and processing, wiki- and knowledge-graph-based digital libraries, and stakeholder-requirement-driven interfaces. While these developed tools for workflow automation and knowledge representation show promise, significant challenges remain. Future work will have to go beyond technical problem-solving and address the societal and legal barriers to unlock the particular domains. Beyond that, advocates of emerging knowledge infrastructures in any domain are welcome to apply the findings of this work to foster the networking of available knowledge.

</details>

---

### 23. [Track-SQL: Enhancing Generative Language Models with Dual-Extractive Modules for Schema and Context Tracking in Multi-turn Text-to-SQL](https://arxiv.org/abs/2603.05996)

**基本信息**

- 🔗 arXiv: [`2603.05996`](https://arxiv.org/abs/2603.05996)
- 👥 作者: Bingfeng Chen, Shaobin Shi, Yongqi Luo 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05996.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是增强大语言模型（LLM）在多轮交互中的复杂信息处理能力。这属于“化学大模型”中提升模型在专业领域（如化学数据库查询、实验步骤理解）进行复杂、多步推理和交互能力的研究方向。

**📖 中文摘要**

生成式语言模型在单轮文本到SQL（Text-to-SQL）中显示出巨大潜力，但其性能并未同等地扩展到多轮Text-to-SQL。这主要是由于生成式语言模型在处理多轮交互中上下文信息和动态模式链接的复杂性方面存在不足。本文提出了一个名为Track-SQL的框架，该框架通过设计用于跟踪多轮Text-to-SQL中模式和上下文变化的双提取模块来增强生成式语言模型。具体来说，Track-SQL包含一个语义增强的模式提取器和一个模式感知的上下文提取器。实验结果表明，Track-SQL在SparC和CoSQL数据集上实现了最先进的性能。此外，详细的消融研究表明，Track-SQL将这些数据集上多轮交互的执行准确率分别显著提高了7.1%和9.55%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative language models have shown significant potential in single-turn Text-to-SQL. However, their performance does not extend equivalently to multi-turn Text-to-SQL. This is primarily due to generative language models' inadequacy in handling the complexities of context information and dynamic schema linking in multi-turn interactions. In this paper, we propose a framework named Track-SQL, which enhances generative language models with dual-extractive modules designed to track schema and contextual changes in multi-turn Text-to-SQL. Specifically, Track-SQL incorporates a \emph{Semantic-enhanced Schema Extractor} and a \emph{Schema-aware Context Extractor}. Experimental results demonstrate that Track-SQL achieves state-of-the-art performance on the SparC and CoSQL datasets. Furthermore, detailed ablation studies reveal that Track-SQL significantly improves execution accuracy in multi-turn interactions by 7.1\% and 9.55\% on these datasets, respectively. Our implementation will be open-sourced at this https URL .

</details>

---

### 24. [MASFactory: A Graph-centric Framework for Orchestrating LLM-Based Multi-Agent Systems with Vibe Graphing](https://arxiv.org/abs/2603.06007)

**基本信息**

- 🔗 arXiv: [`2603.06007`](https://arxiv.org/abs/2603.06007)
- 👥 作者: Yang Liu, Jinxuan Cai, Yishen Li 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06007.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于构建、编排和可视化基于大语言模型的多智能体工作流的框架（MASFactory）。这为“化学大模型”的研究提供了可用于构建复杂化学研究智能体（如用于逆合成规划、实验设计的智能体系统）的工具和平台资源。

**📖 中文摘要**

本文介绍了MASFactory，一个用于编排基于LLM的多智能体系统（MAS）的以图为中心的框架。它引入了Vibe Graphing，这是一种人机交互方法，可将自然语言意图编译成可编辑的工作流规范，然后编译成可执行图。此外，该框架提供了可重用组件和可插拔的上下文集成，以及一个用于拓扑预览、运行时跟踪和人机交互交互的可视化工具。我们在七个公共基准上评估了MASFactory，验证了其对于代表性MAS方法的再现一致性以及Vibe Graphing的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model-based (LLM-based) multi-agent systems (MAS) are increasingly used to extend agentic problem solving via role specialization and collaboration. MAS workflows can be naturally modeled as directed computation graphs, where nodes execute agents/sub-workflows and edges encode dependencies and message passing. However, implementing complex graph workflows in current frameworks still requires substantial manual effort, offers limited reuse, and makes it difficult to integrate heterogeneous external context sources. To overcome these limitations, we present MASFactory, a graph-centric framework for orchestrating LLM-based MAS. It introduces Vibe Graphing, a human-in-the-loop approach that compiles natural-language intent into an editable workflow specification and then into an executable graph. In addition, the framework provides reusable components and pluggable context integration, as well as a visualizer for topology preview, runtime tracing, and human-in-the-loop interaction. We evaluate MASFactory on seven public benchmarks, validating both reproduction consistency for representative MAS methods and the effectiveness of Vibe Graphing. Our code ( this https URL ) and video ( this https URL ) are publicly available.

</details>

---

### 25. [StruVis: Enhancing Reasoning-based Text-to-Image Generation via Thinking with Structured Vision](https://arxiv.org/abs/2603.06032)

**基本信息**

- 🔗 arXiv: [`2603.06032`](https://arxiv.org/abs/2603.06032)
- 👥 作者: Yuanhuiyi Lyu, Kaiyu Lei, Ziqiao Weng 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06032.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升多模态大模型在复杂推理任务（文本到图像生成）中的表现，通过引入结构化中间表示。这属于“化学大模型”中提升模型对复杂科学概念（如分子结构、反应过程）进行多模态理解和推理能力的研究范畴。

**📖 中文摘要**

本文提出了StruVis，一个通过“结构化视觉思维”来增强基于推理的文本到图像（T2I）生成的新框架。与依赖中间图像生成的文本-图像交错推理不同，StruVis采用基于文本的结构化视觉表示作为中间推理状态，从而使多模态大语言模型（MLLM）能够在纯文本推理过程中有效地“感知”视觉结构。在此基础上，通过结构化视觉引导的推理，释放了MLLM在T2I生成中的推理潜力。此外，作为一个生成器无关的推理框架，所提出的StruVis可以无缝集成到不同的T2I生成器中，并有效提升它们在基于推理的T2I生成中的性能。大量实验表明，StruVis在基于推理的T2I基准测试中取得了显著的性能提升，例如在T2I-ReasonBench上提升了4.61%，在WISE上提升了4%。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reasoning-based text-to-image (T2I) generation requires models to interpret complex prompts accurately. Existing reasoning frameworks can be broadly categorized into two types: (1) Text-Only Reasoning, which is computationally efficient but lacks access to visual context, often resulting in the omission of critical spatial and visual elements; and (2) Text-Image Interleaved Reasoning, which leverages a T2I generator to provide visual references during the reasoning process. While this approach enhances visual grounding, it incurs substantial computational costs and constrains the reasoning capacity of MLLMs to the representational limitations of the generator. To this end, we propose StruVis, a novel framework that enhances T2I generation through Thinking with Structured Vision. Instead of relying on intermediate image generation, StruVis employs text-based structured visual representations as intermediate reasoning states, thereby enabling the MLLM to effectively "perceive" visual structure within a purely text-based reasoning process. Powered by this, the reasoning potential for T2I generation of the MLLM is unlocked through structured-vision-guided reasoning. Additionally, as a generator-agnostic reasoning framework, our proposed StruVis can be seamlessly integrated with diverse T2I generators and efficiently enhance their performance in reasoning-based T2I generation. Extensive experiments demonstrate that StruVis achieves significant performance improvements on reasoning-based T2I benchmarks, e.g., a 4.61% gain on T2I-ReasonBench and a 4% gain on WISE.

</details>

---

### 26. [Detecting Semantic Alignments between Textual Specifications and Domain Models](https://arxiv.org/abs/2603.06037)

**基本信息**

- 🔗 arXiv: [`2603.06037`](https://arxiv.org/abs/2603.06037)
- 👥 作者: Shwetali Shimangaud, Lola Burgueño, Rijul Saini 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06037.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型（LLM）来评估和验证领域模型与文本规范的一致性。这属于“化学大模型”在自动化知识提取、模型验证和软件工程（如化学信息学软件规范验证）中的应用。

**📖 中文摘要**

本文提出了一种用于确定部分领域模型与文本规范之间对齐关系的方法。为此，我们使用自然语言处理技术对文本进行预处理，为每个模型元素生成人工的自然语言描述，然后使用大语言模型（LLM）将生成的描述与原始规范中的匹配句子进行比较。最终，我们的算法将每个模型元素分类为对齐（即正确）、未对齐（即错误）或未分类（即证据不足）。此外，它还会输出为确定类别提供证据的文本规范中的相关句子。我们在一组来自文献的示例上评估了我们的方法，这些示例包含不同的领域，每个都包含一个文本规范和一个参考领域模型，以及在通过突变从正确模型系统派生的包含建模错误的模型上进行了评估。我们的结果表明，我们能够以接近1的精确度和约78%的召回率来识别对齐和未对齐，每个模型元素的执行时间从18秒到1分钟不等。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Context: Having domain models derived from textual specifications has proven to be very useful in the early phases of software engineering. However, creating correct domain models and establishing clear links with the textual specification is a challenging task, especially for novice modelers. Objectives: We propose an approach for determining the alignment between a partial domain model and a textual specification. Methods: To this aim, we use Natural Language Processing techniques to pre-process the text, generate an artificial natural language specification for each model element, and then use an LLM to compare the generated description with matched sentences from the original specification. Ultimately, our algorithm classifies each model element as either aligned (i.e., correct), misaligned (i.e., incorrect), or unclassified (i.e., insufficient evidence). Furthermore, it outputs the related sentences from the textual specification that provide the evidence for the determined class. Results: We have evaluated our approach on a set of examples from the literature containing diverse domains, each consisting of a textual specification and a reference domain model, as well as on models containing modeling errors that were systematically derived from the correct models through mutation. Our results show that we are able to identify alignments and misalignments with a precision close to 1 and a recall of approximately 78%, with execution times ranging from 18 seconds to 1 minute per model element. Conclusion: Since our algorithm almost never classifies model elements incorrectly, and is able to classify over 3/4 of the model elements, it could be integrated into a modeling tool to provide positive feedback or generate warnings, or employed for offline validation and quality assessment.

</details>

---

### 27. [Learning to Generate via Understanding: Understanding-Driven Intrinsic Rewarding for Unified Multimodal Models](https://arxiv.org/abs/2603.06043)

**基本信息**

- 🔗 arXiv: [`2603.06043`](https://arxiv.org/abs/2603.06043)
- 👥 作者: Jiadong Pan, Liang Li, Yuxin Peng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06043.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决统一多模态模型中理解与生成能力不匹配的问题，通过自监督强化学习利用模型自身的理解能力来提升生成质量。这直接属于“化学大模型”中关于模型架构优化和能力对齐的研究，对于构建既能理解化学文献又能生成分子结构或实验方案的模型至关重要。

**📖 中文摘要**

最近，统一多模态模型（UMMs）在整合视觉理解和生成方面取得了显著进展，显示出处理复杂文本到图像（T2I）任务的强大潜力。尽管理论上很有前景，但存在一个持续的能力差距：UMMs通常表现出卓越的视觉理解能力，但生成能力相对较弱。这种差异很大程度上源于理解过程和生成过程之间的内在解耦。虽然UMM可以准确解释细粒度的视觉细节，但它通常难以根据复杂的文本提示生成语义连贯的图像。为了应对这一挑战，我们探索利用UMMs的内部理解能力来提升生成质量。我们提出了一种基于标记级的内在文本-图像对齐奖励机制GvU，使UMM能够同时充当教师和学生：它使用理解分支评估自己的输出，从而相应地指导生成。在此基础上，我们设计了一个自监督强化学习框架，允许UMMs通过基于理解的内在奖励信号迭代改进其生成质量——而无需依赖外部监督。实验结果表明，我们的方法显著提升了UMMs的生成能力，这反过来又加强了它们的细粒度视觉理解，缩小了UMMs视觉理解与生成能力之间的差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recently, unified multimodal models (UMMs) have made remarkable progress in integrating visual understanding and generation, demonstrating strong potential for complex text-to-image (T2I) tasks. Despite their theoretical promise, a persistent capability gap exists: UMMs typically exhibit superior visual understanding but comparatively weaker generative capabilities. This discrepancy arises largely from the intrinsic decoupling between the understanding and generation processes. While a UMM can accurately interpret fine-grained visual details, it often struggles to produce semantically coherent images from complex textual prompts. To address this challenge, we explore UMMs' internal understanding capability to enhance generation quality. We propose a token-level intrinsic text-image alignment reward mechanism, GvU, enabling the UMM to act simultaneously as teacher and student: it evaluates its own outputs using the understanding branch to guide the generations accordingly. Building upon this, we design a self-supervised reinforcement learning framework, allowing UMMs to iteratively improve their generation quality through understanding-based intrinsic reward signals--without reliance on external supervision. Experimental results show that our method substantially boosts UMMs' generation, which in turn strengthens their fine-grained visual understanding, narrowing the capability gap between UMMs' visual understanding and generation.

</details>

---

### 28. [A LINDDUN-based Privacy Threat Modeling Framework for GenAI](https://arxiv.org/abs/2603.06051)

**基本信息**

- 🔗 arXiv: [`2603.06051`](https://arxiv.org/abs/2603.06051)
- 👥 作者: Qianying Liao, Jonah Bellemans, Laurens Sion 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06051.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对生成式人工智能（GenAI）系统隐私威胁的综述和框架构建工作。它系统回顾了相关文献并提出了一个分析框架。鉴于“化学大模型”也属于GenAI在特定领域的应用，本文关于GenAI隐私、安全和可信度的讨论与展望，对化学信息学领域应用大模型时考虑数据安全和伦理问题具有重要的参考价值，属于“综述展望相关”。

**📖 中文摘要**

随着生成式人工智能（GenAI）系统在各种技术栈中变得越来越普遍，此类系统如何处理敏感和个人数据流的问题变得越来越重要。具体来说，它们处理和利用大量信息的能力以及其随机性都引发了与安全和隐私相关的关键问题。不幸的是，虽然一些传统的安全威胁建模可以有效地识别某些违规行为，但隐私相关问题常常被忽视。为了应对这些挑战，我们引入了一个新颖的领域特定隐私威胁建模框架，以支持对基于GenAI的应用程序进行隐私威胁分析。该框架通过双管齐下的方法构建：（1）对关于GenAI隐私威胁的新兴文献进行系统回顾，以及（2）在具有代表性的聊天机器人系统中进行案例驱动的应用。这些努力产生了一个基于LINDDUN的基础性GenAI隐私威胁建模框架。新框架影响了LINDDUN七种隐私威胁类型中的三种，并向知识库引入了100个新的GenAI示例。其有效性在一个AI智能体系统上得到了验证，这表明新框架可以支持全面的隐私分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As generative AI (GenAI) systems become increasingly prevalent across various technological stacks, the question of how such systems handle sensitive and personal data flows becomes increasingly important. Specifically, both the ability to harness and process large swaths of information as well as their stochastic nature raise key concerns related to both security and privacy. Unfortunately, while some of the traditional security threat modeling can effectively identify certain violations, privacy-related issues are often overlooked. To respond to these challenges, we introduce a novel domain-specific privacy threat modeling framework to support the privacy threat analysis of GenAI-based applications. This framework is constructed through a two-pronged approach: (1) a systematic review of the emerging literature on GenAI privacy threats, and (2) a case-driven application to a representative Chatbot system. These efforts yield a foundational GenAI privacy threat modeling framework built on LINDDUN. The new framework affects three out of the seven privacy threat types of LINDDUN and introduces 100 new GenAI examples to the knowledge base. Its effectiveness is validated on an AI Agent system, which demonstrates that a comprehensive privacy analysis can be supported by the new framework.

</details>

---

### 29. [Offline Materials Optimization with CliqueFlowmer](https://arxiv.org/abs/2603.06082)

**基本信息**

- 🔗 arXiv: [`2603.06082`](https://arxiv.org/abs/2603.06082)
- 👥 作者: Jakub Grudzien Kuba, Benjamin Kurt Miller, Sergey Levine 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06082.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是开发一种用于材料发现和优化的新型生成模型（CliqueFlowmer），这直接属于“化学大模型”在材料设计中的应用。同时，论文承诺开源代码，这为相关研究提供了可用的工具资源，因此同时满足标准1和标准2。

**📖 中文摘要**

本文提出了一种基于离线模型优化（MBO）的计算材料发现（CMD）技术，该技术将目标材料属性的直接优化融合到生成过程中。为此，我们引入了一个领域特定模型，称为CliqueFlowmer，它将基于团的MBO的最新进展融入Transformer和流生成中。我们验证了CliqueFlowmer的优化能力，并表明它产生的材料在性能上显著优于生成基线提供的材料。为了使CliqueFlowmer能够应用于专门的材料优化问题并支持跨学科研究，我们在指定网址开源了我们的代码。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in deep learning inspired neural network-based approaches to computational materials discovery (CMD). A plethora of problems in this field involve finding materials that optimize a target property. Nevertheless, the increasingly popular generative modeling methods are ineffective at boldly exploring attractive regions of the materials space due to their maximum likelihood training. In this work, we offer an alternative CMD technique based on offline model-based optimization (MBO) that fuses direct optimization of a target material property into generation. To that end, we introduce a domain-specific model, dubbed CliqueFlowmer, that incorporates recent advances of clique-based MBO into transformer and flow generation. We validate CliqueFlowmer's optimization abilities and show that materials it produces strongly outperform those provided by generative baselines. To enable employment of CliqueFlowmer in specialized materials optimization problems and support interdisciplinary research, we open-source our code at this https URL .

</details>

---

### 30. [Multimodal Behavior Tree Generation: A Small Vision-Language Model for Robot Task Planning](https://arxiv.org/abs/2603.06084)

**基本信息**

- 🔗 arXiv: [`2603.06084`](https://arxiv.org/abs/2603.06084)
- 👥 作者: Cristiano Battistini, Riccardo Andrea Izzo, Gianluca Bardaro 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06084.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是训练一个紧凑的多模态模型（VLM）来生成机器人任务规划（行为树）。这属于“化学大模型”在机器人学和自动化实验规划中的应用。同时，论文提出了构建特定数据集的方法并进行了模型训练，为相关领域提供了方法和潜在的模型资源，因此同时满足标准1和标准2。

**📖 中文摘要**

本文通过部署一个紧凑的开源多模态模型来生成机器人任务规划的行为树，从而结合了语言模型和视觉-语言模型这两种方法。实现这一目标的主要障碍是缺乏将视觉观察和指令与可执行行为树联系起来的现有数据集。我们提出了一种从现有机器人片段（例如Open X-Embodiment）开始构建此类数据集的方法，其中一个大模型作为多阶段生成流程中的教师。我们使用该数据集通过参数高效微调（PEFT）对参数量从5亿到40亿不等的视觉-语言模型（VLM）进行微调。生成的行为树与this http URL库兼容，并通过结构化和词汇指标进行离线评估，以及通过在先进的具身模拟器中执行家庭任务进行在线评估。我们的结果表明，我们微调后的40亿参数VLM接近最先进的闭源模型的性能，实现了87%的成功率，同时仅需要一小部分计算资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large and small language models have been widely used for robotic task planning. At the same time, vision-language models (VLMs) have successfully tackled problems such as image captioning, scene understanding, and visual question answering. In this work, we combine these two approaches by deploying a compact, open-source multimodal model to generate behavior trees for robotic task planning. The main obstacle to achieving this goal is the lack of an existing dataset that links visual observations and instructions to executable behavior trees. We propose a method to construct such a dataset starting from existing robotic episodes (i.e., Open X-Embodiment), in which a large model serves as a teacher in a multi-stage generation pipeline. We use this dataset to fine-tune VLMs ranging from 500M to 4B parameters via parameter-efficient fine-tuning (PEFT). The generated behavior trees, compatible with the this http URL library, are evaluated both offline, using structural and lexical metrics, and online through the execution of household tasks in a state-of-the-art embodied simulator. Our results demonstrate that our fine-tuned 4B-parameter VLM approaches the performance of state-of-the-art closed-source models, achieving an 87\% success rate while requiring only a fraction of the computational resources.

</details>

---

### 31. [Experiences Build Characters: The Linguistic Origins and Functional Impact of LLM Personality](https://arxiv.org/abs/2603.06088)

**基本信息**

- 🔗 arXiv: [`2603.06088`](https://arxiv.org/abs/2603.06088)
- 👥 作者: Xi Wang, Mengdie Zhuang, Jiqun Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06088.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索大语言模型（LLM）“个性”（即行为倾向）的形成机制及其对问题解决能力的影响。这属于“化学大模型”中关于模型行为分析、可解释性以及如何为特定化学任务（如创造性分子设计、假设生成）定制模型特性的前沿研究。

**📖 中文摘要**

本研究通过持续预训练以无监督方式将模型暴露于领域特定文本，模拟经验的积累，从而调查不同经验如何塑造机器个性并影响问题解决。通过机器个性量表（MPI）调整大五人格框架，我们量化了这些模型变体的人格特质，并分析了它们与语言风格和推理行为的关系。研究结果表明，模型能力是双峰的，在“表达型通才”和“抑制型专家”处达到峰值，同时识别出“抑制优势”，即降低的社会特质增强了复杂推理性能。本研究进一步建立了训练数据语言学特征（如祈使句频率和词汇多样性）与模型个性之间的因果关系，为“个性工程”提供了路线图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Human problem-solving is enriched by a diversity of styles and personality traits, yet the development of Large Language Models (LLMs) has largely prioritized uniform performance benchmarks that favour specific behavioural tendencies such as assertiveness. To investigate how diverse experiences shape machine personality and influence problem-solving, this study employs continued pre-training to expose models to domain-specific texts in an unsupervised manner, simulating the accumulation of experience. By adapting the Big Five framework via the Machine Personality Inventory (MPI), we quantify the personality traits of these model variants and analyse their relationship to linguistic style and reasoning behaviour. The findings reveal that model competence is bimodal, peaking at "Expressive Generalists" and "Suppressed Specialists," while identifying a "Suppression Advantage" where reduced social traits enhance complex reasoning performance. This study further establishes a causal link between training data linguistics, such as imperative frequency, and lexical diversity, providing a roadmap for "Personality Engineering".

</details>

---

### 32. [Latent Diffusion-Based 3D Molecular Recovery from Vibrational Spectra](https://arxiv.org/abs/2603.06113)

**基本信息**

- 🔗 arXiv: [`2603.06113`](https://arxiv.org/abs/2603.06113)
- 👥 作者: Wenjin Wu, Aleš Leonardis, Linjiang Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06113.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一种从红外振动光谱（与质谱同属分子光谱分析范畴）推理三维分子结构的扩散模型方法。

**📖 中文摘要**

本文提出了一种名为IR-GeoDiff的潜在扩散模型，用于从红外（IR）光谱中恢复分子的三维几何结构。红外光谱是一种振动光谱，广泛用于分子结构测定。传统方法依赖于一维SMILES字符串或二维分子图，无法捕捉光谱特征与三维分子几何之间的复杂关系。IR-GeoDiff通过将光谱信息整合到分子结构的节点和边表示中，能够从单一IR光谱中恢复对应的分子分布。该模型在光谱和结构两个角度进行了评估，并基于注意力的分析表明，模型能够聚焦于IR光谱中特征官能团区域，这与常见的化学解释实践在定性上是一致的。这项工作直接针对“质谱结构推理”主题，利用扩散模型从光谱数据中推断分子三维结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Infrared (IR) spectroscopy, a type of vibrational spectroscopy, is widely used for molecular structure determination and provides critical structural information for chemists. However, existing approaches for recovering molecular structures from IR spectra typically rely on one-dimensional SMILES strings or two-dimensional molecular graphs, which fail to capture the intricate relationship between spectral features and three-dimensional molecular geometry. Recent advances in diffusion models have greatly enhanced the ability to generate molecular structures in 3D space. Yet, no existing model has explored the distribution of 3D molecular geometries corresponding to a single IR spectrum. In this work, we introduce IR-GeoDiff, a latent diffusion model that recovers 3D molecular geometries from IR spectra by integrating spectral information into both node and edge representations of molecular structures. We evaluate IR-GeoDiff from both spectral and structural perspectives, demonstrating its ability to recover the molecular distribution corresponding to a given IR spectrum. Furthermore, an attention-based analysis reveals that the model is able to focus on characteristic functional group regions in IR spectra, qualitatively consistent with common chemical interpretation practices.

</details>

---

### 33. [Enhanced Protein Intrinsic Disorder Prediction Through Dual-View Multiscale Features and Multi-objective Evolutionary Algorithm](https://arxiv.org/abs/2603.06292)

**基本信息**

- 🔗 arXiv: [`2603.06292`](https://arxiv.org/abs/2603.06292)
- 👥 作者: Shaokuan Wang, Pengshan Cui, Yining Qian 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06292.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是蛋白质内在无序区域的预测，这是计算化学和生物信息学中的一个重要问题。所提出的D2MOE框架结合了深度学习和进化算法，属于“化学大模型”在蛋白质结构/性质预测领域的应用。

**📖 中文摘要**

本文提出了一种名为D2MOE的双视图多尺度特征和多目标进化算法，用于增强蛋白质内在无序区域的预测。蛋白质的内在无序区域在细胞信号传导和药物发现中起着关键作用，但由于其高结构灵活性，在残基水平上进行准确预测具有挑战性。D2MOE首先引入了一种双视图多尺度特征提取方法，将进化视图与深度语义视图相结合，并采用多尺度提取器来捕获不同感受野的结构信息。其次，设计了一种多目标进化算法，通过共同进化离散特征选择和连续融合权重，自适应地探索最优的跨特征架构，以提高预测准确性同时保持模型紧凑性。在三个基准数据集上的实验结果表明，D2MOE consistently outperforms state-of-the-art methods。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Intrinsically disordered regions of proteins play a crucial role in cell signaling and drug discovery. However, their high structural flexibility makes accurate residue-level prediction challenging. Existing methods often rely on single-view representations or rigid manual fusion strategies, which fail to effectively balance the complex interplay between local amino acid preferences and long-range sequence patterns. To address these limitations, we propose D2MOE, a Dual-View Multiscale Features and Multi-objective Evolutionary Algorithm, which consists of two stages. First, a dual-view multiscale feature extraction method is introduced. This method integrates evolutionary views with deep semantic views and employs multiscale extractors to capture structural information across diverse receptive fields. Second, a multi-objective evolutionary algorithm is designed to adaptively discover optimal fusion architectures. By co-evolving discrete feature selection and continuous fusion weights, the algorithm adaptively explores optimal cross-feature architectures to enhance predictive accuracy while maintaining model compactness. Experimental results across three benchmark datasets demonstrate that D2MOE consistently outperforms state-of-the-art methods. D2MOE combines the feature extraction capabilities of deep learning with the global search advantages of evolutionary algorithms, enabling efficient feature integration without manual design, and providing a robust computational tool for protein disorder prediction.

</details>

---

### 34. [Structured Exploration vs. Generative Flexibility: A Field Study Comparing Bandit and LLM Architectures for Personalised Health Behaviour Interventions](https://arxiv.org/abs/2603.06330)

**基本信息**

- 🔗 arXiv: [`2603.06330`](https://arxiv.org/abs/2603.06330)
- 👥 作者: Dominik P. Hofer, Haochen Song, Rania Islambouli 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06330.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大语言模型（LLMs）的应用、评估和与其他优化方法（如bandit）的比较。LLMs是“化学大模型”主题中的关键技术范式，因此论文的核心主题是相关的。

**📖 中文摘要**

这篇论文比较了用于个性化健康行为干预的两种AI架构：上下文老虎机（Contextual Bandits）和大语言模型（LLMs）。虽然论文的核心应用领域是行为改变技术（BCTs）和健康干预，但其核心方法涉及使用大语言模型（LLMs）进行灵活、上下文敏感的文本生成。这直接与“化学大模型”这一关注主题相关，因为化学信息学领域同样在探索如何利用LLMs进行分子生成、性质预测和反应规划。论文中对LLM生成能力、与模板方法的比较以及混合架构（bandit+LLM）的讨论，为化学领域构建和应用大模型提供了方法论上的参考和启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Behaviour Change Techniques (BCTs) are central to digital health interventions, yet selecting and delivering effective techniques remains challenging. Contextual bandits enable statistically grounded optimisation of BCT selection, while Large Language Models (LLMs) offer flexible, context-sensitive message generation. We conducted a 4-week study on physical activity motivation (N=54; 9 post-study interviews) that compared five daily messaging approaches: random templates, contextual bandit with templates, LLM generation, hybrid bandit+LLM, and LLM with interaction history. LLM-based approaches were rated substantially more helpful than templates, but no significant differences emerged among LLM conditions. Unexpectedly, bandit optimisation for BCTs selection yielded no additional perceived helpfulness compared with LLM-only approaches. Unconstrained LLMs focused heavily on a single BCT, whereas bandit systems enforced systematic exploration-exploitation across techniques. Quantitative and qualitative findings suggest contextual acknowledgement of user input drove perceived helpfulness. We contribute design suggestions for reflective AI health behaviour change systems that address a trade-off between structured exploration and generative autonomy.

</details>

---

### 35. [Transparent AI for Mathematics: Transformer-Based Large Language Models for Mathematical Entity Relationship Extraction with XAI](https://arxiv.org/abs/2603.06348)

**基本信息**

- 🔗 arXiv: [`2603.06348`](https://arxiv.org/abs/2603.06348)
- 👥 作者: Tanjim Taharat Aurpa
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06348.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是应用Transformer-based模型（BERT）进行结构化信息提取。Transformer架构是构建化学领域大模型的核心技术，其方法可直接类比或应用于化学文本/数据的理解与推理。

**📖 中文摘要**

本研究将数学问题理解构建为数学实体关系提取（MERE）任务，并应用基于Transformer的模型（特别是BERT）来自动从数学文本中提取实体（操作数）和关系（运算符）。论文的核心是使用Transformer架构（BERT）进行关系提取，并集成了可解释人工智能（XAI）技术（SHAP）来增强模型预测的透明度。Transformer模型是构建“化学大模型”的基础架构之一，广泛应用于分子表示学习、反应预测和性质分析。论文中展示的基于Transformer的关系提取框架，其方法论可以迁移到化学信息学领域，例如从科学文献中提取化学实体（分子、官能团）及其关系（反应、相互作用），或用于质谱解析中的结构-谱图关系建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mathematical text understanding is a challenging task due to the presence of specialized entities and complex relationships between them. This study formulates mathematical problem interpretation as a Mathematical Entity Relation Extraction (MERE) task, where operands are treated as entities and operators as their relationships. Transformer-based models are applied to automatically extract these relations from mathematical text, with Bidirectional Encoder Representations from Transformers (BERT) achieving the best performance, reaching an accuracy of 99.39%. To enhance transparency and trust in the model's predictions, Explainable Artificial Intelligence (XAI) is incorporated using Shapley Additive Explanations (SHAP). The explainability analysis reveals how specific textual and mathematical features influence relation prediction, providing insights into feature importance and model behavior. By combining transformer-based learning, a task-specific dataset, and explainable modeling, this work offers an effective and interpretable framework for MERE, supporting future applications in automated problem solving, knowledge graph construction, and intelligent educational systems.

</details>

---

### 36. [MoEless: Efficient MoE LLM Serving via Serverless Computing](https://arxiv.org/abs/2603.06350)

**基本信息**

- 🔗 arXiv: [`2603.06350`](https://arxiv.org/abs/2603.06350)
- 👥 作者: Hanfei Yu, Bei Ouyang, Shwai He 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06350.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化混合专家（MoE）架构的大语言模型（LLMs）的推理服务。MoE是构建和扩展“化学大模型”的关键技术之一，因此论文的主题直接相关。

**📖 中文摘要**

论文提出了MoEless，一个基于无服务器计算的、用于高效服务混合专家（Mixture-of-Experts, MoE）大语言模型（LLMs）的框架。MoE是一种用于扩展LLM规模的关键架构，通过稀疏激活机制来降低计算成本。论文重点解决了MoE LLM服务中的专家负载不均衡和推理延迟问题。虽然应用场景是通用的LLM服务，但MoE架构本身是构建大规模、高效能“化学大模型”的一种重要技术路径。论文中关于优化MoE模型推理效率的方法（如负载预测、专家放置策略）对于未来部署计算密集型的化学领域大模型（如用于分子生成或高通量虚拟筛选的模型）具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have become a cornerstone of AI, driving progress across diverse domains such as content creation, search and recommendation systems, and AI-assisted workflows. To alleviate extreme training costs and advancing model scales, Mixture-of-Experts (MoE) has become a popular backbone for modern LLMs, which are commonly served in distributed deployment using expert parallelism (EP). However, MoE's sparse activation mechanism leads to severe expert load imbalance, where a few experts become overloaded while others remain idle, resulting in expert stragglers that inflate inference latency and serving cost. Existing expert load balancing solutions assume static resource configurations on serverful infrastructures, limiting expert scalability and elasticity, and resulting in either costly real-time expert swapping or degraded generation quality. We present MoEless, the first serverless MoE serving framework that mitigates expert load imbalance and accelerates inference via serverless experts. MoEless employs lightweight, layer-aware predictors to accurately estimate incoming expert load distributions and proactively identify stragglers. We design optimized expert scaling and placement strategies to maximize function locality, improve GPU utilization, and balance loads across experts and GPUs. MoEless is prototyped on top of Megatron-LM and deployed on an eight-GPU testbed. Experiments with open-source MoE models and real-world workloads show that MoEless reduces inference latency by 43% and inference cost by 84% compared to state-of-the-art solutions.

</details>

---

### 37. [Tiny, Hardware-Independent, Compression-based Classification](https://arxiv.org/abs/2603.06359)

**基本信息**

- 🔗 arXiv: [`2603.06359`](https://arxiv.org/abs/2603.06359)
- 👥 作者: Charles Meyers, Aaron MacSween, Erik Elmroth 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06359.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种基于压缩距离的通用分类框架。这种方法论可以迁移到化学信息学领域，用于分子或质谱数据的相似性度量和分类，与“质谱结构推理”主题相关。

**📖 中文摘要**

这篇论文提出了一种基于压缩距离（归一化压缩距离，NCD）的轻量级分类方法，旨在解决用户隐私和客户端设备计算资源有限的问题。该方法的核心思想是使用数据压缩算法来衡量对象之间的相似性，并应用于经典的基于距离的机器学习方法中。虽然论文的应用领域是通用的分类任务，但其提出的“压缩距离”作为一种通用的、与硬件无关的特征表示和相似性度量方法，在原理上可以应用于化学信息学领域。例如，分子结构或质谱数据可以转换为字符串或序列表示，然后利用压缩距离来度量分子相似性或进行谱图匹配，这为“质谱结构推理”提供了一种新颖的、计算高效的方法论思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The recent developments in machine learning have highlighted a conflict between online platforms and their users in terms of privacy. The importance of user privacy and the struggle for power over user data has been intensified as regulators and operators attempt to police online platforms. As users have become increasingly aware of privacy issues, client-side data storage, management, and analysis have become a favoured approach to large-scale centralised machine learning. However, state-of-the-art machine learning methods require vast amounts of labelled user data, making them unsuitable for models that reside client-side and only have access to a single user's data. State-of-the-art methods are also computationally expensive, which degrades the user experience on compute-limited hardware and also reduces battery life. A recent alternative approach has proven remarkably successful in classification tasks across a wide variety of data -- using a compression-based distance measure (called normalised compression distance) to measure the distance between generic objects in classical distance-based machine learning methods. In this work, we demonstrate that the normalised compression distance is actually not a metric; develop it for the wider context of kernel methods to allow modelling of complex data; and present techniques to improve the training time of models that use this distance measure. We demonstrate that the normalised compression distance works as well as and sometimes better than other metrics and kernels -- while requiring only marginally more computational costs and in spite of the lack of formal metric properties. The end results is a simple model with remarkable accuracy even when trained on a very small number of samples allowing for models that are small and effective enough to run entirely on a client device using only user-supplied data.

</details>

---

### 38. [CLAIRE: Compressed Latent Autoencoder for Industrial Representation and Evaluation -- A Deep Learning Framework for Smart Manufacturing](https://arxiv.org/abs/2603.06361)

**基本信息**

- 🔗 arXiv: [`2603.06361`](https://arxiv.org/abs/2603.06361)
- 👥 作者: Mohammadhossein Ghahramani, Mengchu Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06361.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用深度自编码器进行表示学习，并结合可解释性分析。这种方法论是化学信息学和质谱分析中用于数据降维、特征提取和结构推理的常用技术，因此直接相关。

**📖 中文摘要**

论文提出了CLAIRE框架，一个用于智能制造的端到端深度学习框架，集成了无监督深度表示学习（通过优化的深度自编码器）和有监督分类。该框架旨在从高维、嘈杂的工业传感器数据中学习紧凑的潜在表示，以进行准确的故障检测，并利用可解释AI技术分析潜在空间。虽然应用场景是制造业，但其核心方法论——使用深度自编码器进行特征学习和降维，并结合下游任务——与化学信息学和质谱分析中的常见挑战高度相关。例如，在质谱分析中，自编码器常用于学习质谱数据的低维表示，用于化合物鉴定、聚类或异常检测。论文中关于学习鲁棒表示和模型可解释性的讨论，对构建用于质谱数据分析和推理的模型具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate fault detection in high-dimensional industrial environments remains a major challenge due to the inherent complexity, noise, and redundancy in sensor data. This paper introduces CLAIRE, i.e., a hybrid end-to-end learning framework that integrates unsupervised deep representation learning with supervised classification for intelligent quality control in smart manufacturing systems. It employs an optimized deep autoencoder to transform raw input into a compact latent space, effectively capturing the intrinsic data structure while suppressing irrelevant or noisy features. The learned representations are then fed into a downstream classifier to perform binary fault prediction. Experimental results on a high-dimensional dataset demonstrate that CLAIRE significantly outperforms conventional classifiers trained directly on raw features. Moreover, the framework incorporates a post hoc phase, using a game-theory-based interpretability technique, to analyze the latent space and identify the most informative input features contributing to fault predictions. The proposed framework highlights the potential of integrating explainable AI with feature-aware regularization for robust fault detection. The modular and interpretable nature of the proposed framework makes it highly adaptable, offering promising applications in other domains characterized by complex, high-dimensional data, such as healthcare, finance, and environmental monitoring.

</details>

---

### 39. [Computer vision-based estimation of invertebrate biomass](https://arxiv.org/abs/2603.06362)

**基本信息**

- 🔗 arXiv: [`2603.06362`](https://arxiv.org/abs/2603.06362)
- 👥 作者: Mikko Impiö, Philipp M. Rehsen, Jarrett Blair 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06362.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从图像数据中预测物理属性（生物量）。这与“质谱结构推理”从谱图数据中预测分子结构属性的任务在方法论上同构，因此主题相关。

**📖 中文摘要**

本研究提出了两种基于计算机视觉的方法，用于仅通过图像估计无脊椎动物的生物量（干重），从而避免手动称重的破坏性过程。第一种方法使用由成像设备自动计算的新预测因子（面积和下沉速度）拟合线性模型；第二种方法训练端到端的深度神经网络。研究收集了一个包含干重测量和图像序列对的大型数据集。虽然研究对象是生物样本，但其核心科学问题——如何从图像中准确推断物理或化学属性——与“质谱结构推理”在方法论上高度相似。质谱结构推理的核心也是从复杂的谱图数据（可视为一种特殊“图像”或高维向量）中推断出分子的结构属性。论文中关于评估指标选择、数据增强和模型架构比较的讨论，对于设计和评估质谱解析模型具有直接的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The ability to estimate invertebrate biomass using only images could help scaling up quantitative biodiversity monitoring efforts. Computer vision-based methods have the potential to omit the manual, time-consuming, and destructive process of dry weighing specimens. We present two approaches for dry mass estimation that do not require additional manual effort apart from imaging the specimens: fitting a linear model with novel predictors, automatically calculated by an imaging device, and training a family of end-to-end deep neural networks for the task, using single-view, multi-view, and metadata-aware architectures. We propose using area and sinking speed as predictors. These can be calculated with BIODISCOVER, which is a dual-camera system that captures image sequences of specimens sinking in an ethanol column. For this study, we collected a large dataset of dry mass measurement and image sequence pairs to train and evaluate models. We show that our methods can estimate specimen dry mass even with complex and visually diverse specimen morphologies. Combined with automatic taxonomic classification, our approach is an accurate method for group-level dry mass estimation, with a median percentage error of 10-20% for individuals. We highlight the importance of choosing appropriate evaluation metrics, and encourage using both percentage errors and absolute errors as metrics, because they measure different properties. We also explore different optimization losses, data augmentation methods, and model architectures for training deep-learning models.

</details>

---

### 40. [Adaptive Lipschitz-Free Conditional Gradient Methods for Stochastic Composite Nonconvex Optimization](https://arxiv.org/abs/2603.06369)

**基本信息**

- 🔗 arXiv: [`2603.06369`](https://arxiv.org/abs/2603.06369)
- 👥 作者: Ganzhao Yuan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06369.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大规模、非凸优化问题提出新的自适应优化算法。训练“化学大模型”本质上是大规模非凸优化问题，因此该优化方法的研究与主题相关。

**📖 中文摘要**

论文提出了ALFCG，一种用于随机复合非凸优化的自适应、无投影（即条件梯度/Conditional Gradient）框架。它不需要全局平滑常数或线搜索，通过维护历史迭代差分的自归一化累加器来估计局部平滑度。论文研究了三种变体，并给出了达到平稳点的迭代复杂度。虽然论文是优化理论和方法研究，但其提出的自适应优化算法对于训练复杂的“化学大模型”具有潜在价值。化学大模型（如用于分子生成的扩散模型或大型图神经网络）的训练通常涉及大规模、非凸的损失函数，高效的优化器是关键。论文中针对随机、非凸问题的条件梯度方法的改进，可以为训练化学领域的大规模参数模型提供新的优化工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose ALFCG (Adaptive Lipschitz-Free Conditional Gradient), the first \textit{adaptive} projection-free framework for stochastic composite nonconvex minimization that \textit{requires neither global smoothness constants nor line search}. Unlike prior conditional gradient methods that use openloop diminishing stepsizes, conservative Lipschitz constants, or costly backtracking, ALFCG maintains a self-normalized accumulator of historical iterate differences to estimate local smoothness and minimize a quadratic surrogate model at each step. This retains the simplicity of Frank-Wolfe while adapting to unknown geometry. We study three variants. ALFCG-FS addresses finite-sum problems with a SPIDER estimator. ALFCG-MVR1 and ALFCG-MVR2 handle stochastic expectation problems by using momentum-based variance reduction with single-batch and two-batch updates, and operate under average and individual smoothness, respectively. To reach an $\epsilon$-stationary point, ALFCG-FS attains $\mathcal{O}(N+\sqrt{N}\epsilon^{-2})$ iteration complexity, while ALFCG-MVR1 and ALFCG-MVR2 achieve $\tilde{\mathcal{O}}(\sigma^2\epsilon^{-4}+\epsilon^{-2})$ and $\tilde{\mathcal{O}}(\sigma\epsilon^{-3}+\epsilon^{-2})$, where $N$ is the number of components and $\sigma$ is the noise level. In contrast to typical $\mathcal{O}(\epsilon^{-4})$ or $\mathcal{O}(\epsilon^{-3})$ rates, our bounds reduce to the optimal rate up to logarithmic factors $\tilde{\mathcal{O}}(\epsilon^{-2})$ as the noise level $\sigma \to 0$. Extensive experiments on multiclass classification over nuclear norm balls and $\ell_p$ balls show that ALFCG generally outperforms state-of-the-art conditional gradient baselines.

</details>

---

### 41. [Toward Generative Quantum Utility via Correlation-Complexity Map](https://arxiv.org/abs/2603.06440)

**基本信息**

- 🔗 arXiv: [`2603.06440`](https://arxiv.org/abs/2603.06440)
- 👥 作者: Chen-Yu Liu, Leonardo Placidi, Eric Brunner 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06440.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和实现量子生成模型（IQP）对复杂数据分布的建模能力。生成模型是“化学大模型”和“质谱结构推理”中的重要技术，因此主题相关。

**📖 中文摘要**

论文提出了“相关性-复杂性图谱”作为一种诊断工具，用于判断现实世界的数据分布是否在结构上与IQP型量子生成模型对齐。论文引入了两个指标：量子相关性指标（QCLI）和经典相关性-复杂性指标（CCI）。通过该图谱，作者识别出经典湍流数据与IQP模型兼容且具有经典复杂性，并在此基础上使用可逆的浮点数到比特串表示和潜在参数自适应方案，训练了一个紧凑的IQP电路用于生成建模。这项工作探索了量子生成模型在经典复杂数据上的应用潜力。虽然主要涉及量子机器学习，但其核心是研究生成模型（特别是基于电路的量子生成模型）如何捕获复杂数据分布。这与“化学大模型”中利用生成模型（如扩散模型、自回归模型）进行分子设计和“质谱结构推理”中利用生成模型进行谱图生成或解释的研究方向在概念上并行。论文中关于模型与数据分布对齐的分析方法具有启发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a Correlation-Complexity Map as a practical diagnostic tool for determining when real-world data distributions are structurally aligned with IQP-type quantum generative models. Characterized by two complementary indicators: (i) a Quantum Correlation-Likeness Indicator (QCLI), computed from the dataset's correlation-order (Walsh-Hadamard/Fourier) power spectrum aggregated by interaction order and quantified via Jensen-Shannon divergence from an i.i.d. binomial reference; and (ii) a Classical Correlation-Complexity Indicator (CCI), defined as the fraction of total correlation not captured by the optimal Chow-Liu tree approximation, normalized by total correlation. We provide theoretical support by relating QCLI to a support-mismatch mechanism, for fixed-architecture IQP families trained with an MMD objective, higher QCLI implies a smaller irreducible approximation floor. Using the map, we identify the classical turbulence data as both IQP-compatible and classically complex (high QCLI/high CCI). Guided by this placement, we use an invertible float-to-bitstring representation and a latent-parameter adaptation scheme that reuses a compact IQP circuit over a temporal sequence by learning and interpolating a low-dimensional latent trajectory. In comparative evaluations against classical models such as Restricted Boltzmann Machine (RBM) and Deep Convolutional Generative Adversarial Networks (DCGAN), the IQP approach achieves competitive distributional alignment while using substantially fewer training snapshots and a small latent block, supporting the use of QCLI/CCI as practical indicators for locating IQP-aligned domains and advancing generative quantum utility.

</details>

---

### 42. [CaTok: Taming Mean Flows for One-Dimensional Causal Image Tokenization](https://arxiv.org/abs/2603.06449)

**基本信息**

- 🔗 arXiv: [`2603.06449`](https://arxiv.org/abs/2603.06449)
- 👥 作者: Yitong Chen, Zuxuan Wu, Xipeng Qiu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06449.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于图像的自回归（AR）因果分词器和生成模型。自回归生成是构建化学大模型（如用于分子序列生成）的核心范式之一，因此论文的主题直接相关。

**📖 中文摘要**

论文提出了CaTok，一种用于图像的1D因果分词器，采用MeanFlow解码器。它通过学习将图像表示为支持自回归生成的因果1D序列，实现了快速的一步生成和高保真的多步采样。CaTok的核心是构建一个支持自回归生成的视觉表示，这与构建能够进行序列生成（如分子SMILES序列、反应序列）的“化学大模型”在技术目标上一致。论文中关于学习因果表示、结合扩散模型目标（MeanFlow）的方法，为化学领域开发新型的、高效的分子表示和生成模型提供了思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autoregressive (AR) language models rely on causal tokenization, but extending this paradigm to vision remains non-trivial. Current visual tokenizers either flatten 2D patches into non-causal sequences or enforce heuristic orderings that misalign with the "next-token prediction" pattern. Recent diffusion autoencoders similarly fall short: conditioning the decoder on all tokens lacks causality, while applying nested dropout mechanism introduces imbalance. To address these challenges, we present CaTok, a 1D causal image tokenizer with a MeanFlow decoder. By selecting tokens over time intervals and binding them to the MeanFlow objective, as illustrated in Fig. 1, CaTok learns causal 1D representations that support both fast one-step generation and high-fidelity multi-step sampling, while naturally capturing diverse visual concepts across token intervals. To further stabilize and accelerate training, we propose a straightforward regularization REPA-A, which aligns encoder features with Vision Foundation Models (VFMs). Experiments demonstrate that CaTok achieves state-of-the-art results on ImageNet reconstruction, reaching 0.75 FID, 22.53 PSNR and 0.674 SSIM with fewer training epochs, and the AR model attains performance comparable to leading approaches.

</details>

---

### 43. [Training Flow Matching: The Role of Weighting and Parameterization](https://arxiv.org/abs/2603.06454)

**基本信息**

- 🔗 arXiv: [`2603.06454`](https://arxiv.org/abs/2603.06454)
- 👥 作者: Anne Gagneux, Ségolène Martin, Rémi Gribonval 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06454.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和比较扩散模型/流匹配模型的不同训练目标。扩散模型是构建“化学大模型”用于分子生成和“质谱结构推理”中谱图生成的关键技术，因此主题高度相关。

**📖 中文摘要**

论文系统地研究了基于去噪的生成模型（如扩散模型/流匹配）的训练目标，重点关注损失加权和输出参数化（包括基于噪声、干净图像和速度的公式化）。通过系统的数值研究，分析了这些训练选择如何与数据流形的内在维度、模型架构和数据集大小相互作用。生成模型，特别是扩散模型和流匹配，是当前“化学大模型”领域用于分子生成和构象采样的前沿技术。论文对训练目标中关键超参数和设计选择的深入分析，对于化学信息学研究者理解和优化用于分子生成或质谱数据生成的扩散模型具有直接的指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study the training objectives of denoising-based generative models, with a particular focus on loss weighting and output parameterization, including noise-, clean image-, and velocity-based formulations. Through a systematic numerical study, we analyze how these training choices interact with the intrinsic dimensionality of the data manifold, model architecture, and dataset size. Our experiments span synthetic datasets with controlled geometry as well as image data, and compare training objectives using quantitative metrics for denoising accuracy (PSNR across noise levels) and generative quality (FID). Rather than proposing a new method, our goal is to disentangle the various factors that matter when training a flow matching model, in order to provide practical insights on design choices.

</details>

---

### 44. [The DNA Coverage Depth Problem: Duality, Weight Distributions, and Applications](https://arxiv.org/abs/2603.06489)

**基本信息**

- 🔗 arXiv: [`2603.06489`](https://arxiv.org/abs/2603.06489)
- 👥 作者: Matteo Bertuzzo, Alberto Ravagnani, Eitan Yaakobi
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06489.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用编码理论解决DNA数据存储中的覆盖问题。其数学方法和模型可以类比到化学信息学中的分子库设计或数据库搜索问题，与主题有一定相关性。

**📖 中文摘要**

论文研究了DNA数据存储中的覆盖深度问题，即计算恢复所有编码链所需的预期读取次数。给定一个线性码的生成矩阵，该数量等于获得满秩所需的随机抽取列的预期数量。论文基于对偶性论证和扩展权重枚举器的概念，开发了组合工具来解决各种线性码的DNA覆盖深度问题，并为单纯形码、汉明码、三元戈莱码等推导了闭合公式。虽然论文聚焦于DNA存储的编码理论，但其核心数学工具——线性码的权重分布和覆盖性质——与化学信息学中分子描述符的设计、分子库的多样性分析以及质谱数据库搜索中的覆盖问题在抽象层面上有共通之处。论文提供了一种严谨的数学框架来分析“覆盖”问题，这可能启发化学信息学中类似问题的建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The coverage depth problem in DNA data storage is about computing the expected number of reads needed to recover all encoded strands. Given a generator matrix of a linear code, this quantity equals the expected number of randomly drawn columns required to obtain full rank. While MDS codes are optimal when they exist, i.e., over large fields, practical scenarios may rely on structured code families defined over small fields. In this work, we develop combinatorial tools to solve the DNA coverage depth problem for various linear codes, based on duality arguments and the notion of extended weight enumerator. Using these methods, we derive closed formulas for the simplex, Hamming, ternary Golay, extended ternary Golay, and first-order Reed-Muller codes. The centerpiece of this paper is a general expression for the coverage depth of a linear code in terms of the weight distributions of its higher-field extensions.

</details>

---

### 45. [Self-Supervised Flow Matching for Scalable Multi-Modal Synthesis](https://arxiv.org/abs/2603.06507)

**基本信息**

- 🔗 arXiv: [`2603.06507`](https://arxiv.org/abs/2603.06507)
- 👥 作者: Hila Chefer, Patrick Esser, Dominik Lorenz 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06507.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种统一表示学习和生成训练的自监督流匹配框架。学习通用、强大的表示是化学大模型和质谱分析的核心目标，因此主题高度相关。

**📖 中文摘要**

论文提出了Self-Flow，一种自监督的流匹配范式，将表示学习集成到生成框架中。其关键机制是“双时间步调度”，在不同token上应用异构的噪声水平，创建信息不对称，迫使模型从损坏的输入中推断缺失信息，从而驱动模型在学习生成能力的同时学习强表示，而无需外部监督。该方法跨模态通用，支持多模态训练。这项工作旨在改进生成模型的表示学习能力。强大的表示学习是“化学大模型”和“质谱结构推理”的基础，例如学习分子的通用表示或质谱的特征表示。论文中提出的将表示学习与生成训练统一起来的自监督框架，为化学领域开发既能生成又能理解分子/谱图数据的统一模型提供了新颖的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Strong semantic representations improve the convergence and generation quality of diffusion and flow models. Existing approaches largely rely on external models, which require separate training, operate on misaligned objectives, and exhibit unexpected scaling behavior. We argue that this dependence arises from the model's training objective, which poses a denoising task with little incentive to learn semantic representations. We introduce Self-Flow: a self-supervised flow matching paradigm that integrates representation learning within the generative framework. Our key mechanism, Dual-Timestep Scheduling, applies heterogeneous noise levels across tokens, creating an information asymmetry that forces the model to infer missing information from corrupted inputs. This drives learning strong representations alongside generative capabilities without external supervision. Our method generalizes across modalities and enables multi-modal training while following expected scaling laws, achieving superior image, video, and audio generation.

</details>

---

### 46. [Causal Interpretation of Neural Network Computations with Contribution Decomposition](https://arxiv.org/abs/2603.06557)

**基本信息**

- 🔗 arXiv: [`2603.06557`](https://arxiv.org/abs/2603.06557)
- 👥 作者: Joshua Brendan Melander, Zaki Alaoui, Shenghua Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06557.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的神经网络可解释性方法，用于分解和解释内部神经元的贡献。模型可解释性是化学和质谱分析中AI模型可靠应用的关键，因此主题相关。

**📖 中文摘要**

论文提出了CODEC（贡献分解），一种通过稀疏自编码器将神经网络行为分解为隐藏神经元贡献的稀疏模式的方法，以揭示仅分析激活无法确定的因果过程。该方法应用于图像分类网络，发现贡献跨层变得稀疏和高维，并且正负贡献逐渐去相关。该方法支持对网络输出的因果操纵和人类可解释的可视化。在化学信息学领域，理解神经网络（尤其是用于分子性质预测或谱图解析的模型）的内部决策过程至关重要。CODEC提供了一种新的、可解释的框架来分析神经网络中非线性计算的演化，这对于构建透明、可信的“化学大模型”和“质谱结构推理”模型具有重要价值，有助于进行机理洞察和模型调试。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding how neural networks transform inputs into outputs is crucial for interpreting and manipulating their behavior. Most existing approaches analyze internal representations by identifying hidden-layer activation patterns correlated with human-interpretable concepts. Here we take a direct approach to examine how hidden neurons act to drive network outputs. We introduce CODEC (Contribution Decomposition), a method that uses sparse autoencoders to decompose network behavior into sparse motifs of hidden-neuron contributions, revealing causal processes that cannot be determined by analyzing activations alone. Applying CODEC to benchmark image-classification networks, we find that contributions grow in sparsity and dimensionality across layers and, unexpectedly, that they progressively decorrelate positive and negative effects on network outputs. We further show that decomposing contributions into sparse modes enables greater control and interpretation of intermediate layers, supporting both causal manipulations of network output and human-interpretable visualizations of distinct image components that combine to drive that output. Finally, by analyzing state-of-the-art models of neural activity in the vertebrate retina, we demonstrate that CODEC uncovers combinatorial actions of model interneurons and identifies the sources of dynamic receptive fields. Overall, CODEC provides a rich and interpretable framework for understanding how nonlinear computations evolve across hierarchical layers, establishing contribution modes as an informative unit of analysis for mechanistic insights into artificial neural networks.

</details>

---

### 47. [A recipe for scalable attention-based MLIPs: unlocking long-range accuracy with all-to-all node attention](https://arxiv.org/abs/2603.06567)

**基本信息**

- 🔗 arXiv: [`2603.06567`](https://arxiv.org/abs/2603.06567)
- 👥 作者: Eric Qu, Brandon M. Wood, Aditi S. Krishnapriyan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06567.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种可扩展的、基于注意力机制的机器学习原子间势（MLIP）模型。MLIP是化学领域“大模型”的重要子类，用于分子和材料模拟，因此主题直接相关。

**📖 中文摘要**

论文提出了AllScAIP，一种基于注意力、能量守恒的机器学习原子间势（MLIP）模型，可扩展至数亿训练样本。它通过数据驱动的全对全节点注意力组件来解决长程相互作用挑战。广泛的消融实验表明，在数据/模型规模扩大时，全对全注意力对于捕获长程相互作用至关重要。该模型在分子系统上实现了最先进的能量/力精度，并支持稳定、长时间的分子动力学模拟。机器学习原子间势（MLIP）是“化学大模型”在计算化学和材料科学中的核心应用之一，用于准确、高效地模拟原子系统的势能面和动力学。论文中针对大规模、长程相互作用的模型设计，直接推动了化学领域大模型的发展，特别是对于生物大分子和电解质溶液等复杂体系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine-learning interatomic potentials (MLIPs) have advanced rapidly, with many top models relying on strong physics-based inductive biases. However, as models scale to larger systems like biomolecules and electrolytes, they struggle to accurately capture long-range (LR) interactions, leading current approaches to rely on explicit physics-based terms or components. In this work, we propose AllScAIP, a straightforward, attention-based, and energy-conserving MLIP model that scales to O(100 million) training samples. It addresses the long-range challenge using an all-to-all node attention component that is data-driven. Extensive ablations reveal that in low-data/small-model regimes, inductive biases improve sample efficiency. However, as data and model size scale, these benefits diminish or even reverse, while all-to-all attention remains critical for capturing LR interactions. Our model achieves state-of-the-art energy/force accuracy on molecular systems, as well as a number of physics-based evaluations (OMol25), while being competitive on materials (OMat24) and catalysts (OC20). Furthermore, it enables stable, long-timescale MD simulations that accurately recover experimental observables, including density and heat of vaporization predictions.

</details>

---

### 48. [Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders](https://arxiv.org/abs/2603.06569)

**基本信息**

- 🔗 arXiv: [`2603.06569`](https://arxiv.org/abs/2603.06569)
- 👥 作者: Boqiang Zhang, Lei Ke, Ruihan Yang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06569.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是视觉语言模型（VLM）的架构创新，特别是视觉编码器的设计和初始化。其方法论对于构建化学领域的多模态大模型（结合文本、结构、谱图）具有直接的借鉴意义。

**📖 中文摘要**

论文提出了Penguin-VL，一种探索紧凑型视觉语言模型（VLM）性能极限的工作。其关键创新是使用从纯文本LLM初始化的视觉编码器（Penguin-Encoder），而非传统的基于对比预训练（如CLIP）的编码器。作者认为对比学习的目标与VLM所需的细粒度视觉线索存在不匹配。实验表明，Penguin-Encoder作为视觉编码器，在多种图像和视频基准测试中，能以轻量级架构实现与领先VLM相当或更优的性能，特别是在需要密集感知和复杂推理的任务上。这项工作对VLM的架构设计提出了新思路。构建高效的“化学大模型”同样面临如何设计或初始化模态特定编码器（如分子图编码器、谱图编码器）并与LLM融合的挑战。论文中关于编码器初始化、多模态融合效率的探索，对化学多模态大模型（如结合文本、分子结构、谱图）的设计具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision Language Model (VLM) development has largely relied on scaling model size, which hinders deployment on compute-constrained mobile and edge devices such as smartphones and robots. In this work, we explore the performance limits of compact (e.g., 2B and 8B) VLMs. We challenge the prevailing practice that state-of-the-art VLMs must rely on vision encoders initialized via massive contrastive pretraining (e.g., CLIP/SigLIP). We identify an objective mismatch: contrastive learning, optimized for discrimination, enforces coarse and category-level invariances that suppress fine-grained visual cues needed for dense captioning and complex VLM reasoning. To address this issue, we present Penguin-VL, whose vision encoder is initialized from a text-only LLM. Our experiments reveal that Penguin-Encoder serves as a superior alternative to traditional contrastive pretraining, unlocking a higher degree of visual fidelity and data efficiency for multimodal understanding. Across various image and video benchmarks, Penguin-VL achieves performance comparable to leading VLMs (e.g., Qwen3-VL) in mathematical reasoning and surpasses them in tasks such as document understanding, visual knowledge, and multi-perspective video understanding. Notably, these gains are achieved with a lightweight architecture, demonstrating that improved visual representation rather than model scaling is the primary driver of performance. Our ablations show that Penguin-Encoder consistently outperforms contrastive-pretrained encoders, preserving fine-grained spatial and temporal cues that are critical for dense perception and complex reasoning. This makes it a strong drop-in alternative for compute-efficient VLMs and enables high performance in resource-constrained settings. Code: this https URL

</details>

---

### 49. [Omni-Diffusion: Unified Multimodal Understanding and Generation with Masked Discrete Diffusion](https://arxiv.org/abs/2603.06577)

**基本信息**

- 🔗 arXiv: [`2603.06577`](https://arxiv.org/abs/2603.06577)
- 👥 作者: Lijiang Li, Zuwei Long, Yunhang Shen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06577.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个基于掩码离散扩散模型的统一多模态理解和生成系统。扩散模型是化学大模型的关键技术，其统一多模态的框架设计对化学领域有重要的启示作用。

**📖 中文摘要**

论文提出了Omni-Diffusion，第一个完全基于掩码离散扩散模型构建的任意模态到任意模态的多模态语言模型，统一了文本、语音和图像的理解与生成。该模型采用统一的掩码离散扩散模型来直接捕获离散多模态token的联合分布。这项工作展示了扩散模型作为多模态系统骨干的巨大潜力。扩散模型是当前“化学大模型”在分子生成、构象生成等领域的前沿技术。论文将扩散模型扩展到统一的多模态理解和生成，这一范式为化学信息学提供了新的思路：可以构想一个基于扩散的、统一的化学多模态模型，能够同时处理分子结构（图/SMILES）、质谱、红外光谱、文本描述等，并执行跨模态的生成和推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While recent multimodal large language models (MLLMs) have made impressive strides, they predominantly employ a conventional autoregressive architecture as their backbone, leaving significant room to explore effective and efficient alternatives in architectural design. Concurrently, recent studies have successfully applied discrete diffusion models to various domains, such as visual understanding and image generation, revealing their considerable potential as a promising backbone for multimodal systems. Drawing inspiration from these pioneering research, we introduce Omni-Diffusion, the first any-to-any multimodal language model built entirely on mask-based discrete diffusion models, which unifies understanding and generation across text, speech, and images. Omni-Diffusion employs a unified mask-based discrete diffusion model to directly capture the joint distribution over discrete multimodal tokens. This approach supports not only bimodal tasks but also more complex scenarios involving multiple modalities. On a diverse set of benchmarks, our method outperforms or performs on par with existing multimodal systems that process two or more modalities, highlighting the significant promise of diffusion models in powering the next generation of multimodal foundation models. Project webpage: this https URL .

</details>

---

### 50. [Molecular Representations for AI in Chemistry and Materials Science: An NLP Perspective](https://arxiv.org/abs/2603.05525)

**基本信息**

- 🔗 arXiv: [`2603.05525`](https://arxiv.org/abs/2603.05525)
- 👥 作者: Sanjanasri JP, Pratiti Bhadra, N. Sukumar 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05525.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学中的分子表示方法，这是构建和应用化学大模型的基础。

**📖 中文摘要**

这篇论文从自然语言处理（NLP）的视角，系统性地回顾了化学和材料科学中用于人工智能的分子表示方法。论文讨论了多种流行的数字分子表示形式，这些表示形式对于化学信息学至关重要，旨在为不同领域的研究人员提供一个指南。它直接涉及化学信息学领域的核心主题，即如何为AI模型（包括化学大模型）准备和处理分子数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning, a subfield of machine learning, has gained importance in various application areas in recent years. Its growing popularity has led it to enter the natural sciences as well. This has created the need for molecular representations that are both machine-readable and understandable to scientists from different fields. Over the years, many chemical molecular representations have been constructed, and new ones continue to be developed as computer technology advances and knowledge of molecular complexity increases. This paper presents some of the most popular digital molecular representations inspired by natural language processing (NLP) and used in chemical informatics. In addition, the paper discusses some notable AI-based applications that use these representations. This paper aims to provide a guide to structural representations that are important for the application of AI in chemistry and materials science from the perspective of an NLP researcher. This review is a reference tool for researchers with little experience working with chemical representations who wish to work on projects at the interface of these fields.

</details>

---

### 51. [Drifting to Boltzmann: Million-Fold Acceleration in Boltzmann Sampling with Force-Guided Drifting](https://arxiv.org/abs/2603.05527)

**基本信息**

- 🔗 arXiv: [`2603.05527`](https://arxiv.org/abs/2603.05527)
- 👥 作者: Pipi Hu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05527.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分子构象的生成与采样，这是计算化学和化学信息学的核心问题。其提出的利用物理力标签加速采样的方法，为从数据（如计算或实验数据）中学习并生成分子结构提供了新思路，与“质谱结构推理”中从谱数据推断分子结构这一主题在技术路径上高度相关。

**📖 中文摘要**

论文提出了一种名为“漂移模型”的新方法，用于从玻尔兹曼分布中采样分子构象，实现了百万倍的加速。该方法通过引入“漂移力恒等式”，将分子力标签（直接编码玻尔兹曼分数）整合到生成过程中，从而在坐标空间或距离特征空间中实现一步生成。这项工作展示了将物理力（一种特定类型的先验知识）整合到生成模型中的新范式，对于从计算数据中学习并生成物理上合理的分子结构具有重要价值，这与质谱结构推理中需要从谱图推断三维结构的核心挑战在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sampling molecular conformations from the Boltzmann distribution is essential for computational chemistry, but iterative diffusion methods are prohibitively slow. Drifting Models offer one-step generation, yet their equilibrium matches the \emph{training} distribution, which may deviate from the true Boltzmann distribution due to sampling bias. We introduce Drifting Models to molecular conformation generation for the first time, establishing a theoretical bridge via the \emph{Drifting Score Identity}: for Gaussian kernels, the drifting field's attraction equals a kernel-weighted average of \emph{any} distribution's score function. Substituting molecular force labels -- which directly encode the Boltzmann score -- yields the \emph{Drifting Force Identity} and decomposes the field into standard drift plus a Boltzmann correction. We further discover a striking phenomenon unique to molecular systems: force incorporation's effectiveness \emph{reverses across representations}. In coordinate space, Force-Interpolated Drifting (FI) dominates by blending physical force directions with data displacements. In distance feature space, Force-Aligned Kernel (FK) achieves superior accuracy by modifying only kernel weights, thereby preserving the manifold of geometrically valid molecules. On MD17 Ethanol, both approaches achieve one-step generation with over 1000x speedup relative to recent score-matching methods with Boltzmann guiding, providing more than million-fold acceleration over traditional molecular dynamics, while ensuring perfect structural validity and distributional accuracy rivaling multi-step methods.

</details>

---

### 52. [On the Reliability of AI Methods in Drug Discovery: Evaluation of Boltz-2 for Structure and Binding Affinity Prediction](https://arxiv.org/abs/2603.05532)

**基本信息**

- 🔗 arXiv: [`2603.05532`](https://arxiv.org/abs/2603.05532)
- 👥 作者: Shunzhou Wan, Xibei Zhang, Xiao Xue 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05532.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是评估一个用于生物分子结构预测的AI基础模型（Boltz-2），这直接属于“化学大模型”在特定应用场景（结构预测）下的研究和评估范畴。

**📖 中文摘要**

论文评估了名为Boltz-2的生物分子基础模型在预测蛋白质-配体结构和结合亲和力方面的可靠性。研究将Boltz-2的预测结果与传统分子对接以及基于物理的ESMACS协议进行比较。尽管评估焦点是药物发现，但论文深入探讨了AI模型（特别是大模型）在预测生物分子结构和相互作用方面的能力、局限性和验证需求。这为评估化学/生物大模型在结构预测任务上的性能提供了具体案例和方法学参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite continuing hype about the role of AI in drug discovery, no "AI-discovered drugs" have so far received regulatory approval. Here we assess one of the latest AI based tools in this domain. The ability to rapidly predict protein-ligand structures and binding affinities is pivotal for accelerating drug discovery. Boltz-2, a recently developed biomolecular foundation model, aims to bridge the gap between AI efficiency and physics-based precision through a joint "co-folding" approach. In this study, we provide an extensive evaluation of Boltz-2 using two large-scale datasets: 16,780 compounds for 3CLPro and 21,702 compounds for TNKS2. We compare Boltz-2 predicted structures with traditional docking and binding affinities with binding free energies derived from the physics-based ESMACS protocol. Structural analysis reveals significant global RMSD variations, indicating that Boltz-2 predicts multiple protein conformations and ligand binding positions rather than a single converged pose. Energetic evaluations exhibit only weak to moderate correlations across the global datasets. Furthermore, a focused analysis of the top 100 compounds yields no significant correlation between the Boltz-2 predictions and the binding free energies from fine-grained ESMACS, alongside observed saturation difference in ligand structures. Our results show that while Boltz-2 offers substantial speed for initial screening, it lacks the energetic resolution required for lead identification. These findings highlight the necessity of employing physics-based methods for the reliability and refinement of AI-derived models.

</details>

---

### 53. [Classical Explanations in (and of) General Probabilistic Theories](https://arxiv.org/abs/2603.05627)

**基本信息**

- 🔗 arXiv: [`2603.05627`](https://arxiv.org/abs/2603.05627)
- 👥 作者: John Harding, Alex Wilce
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05627.pdf)

**💡 相关性分析**

满足标准1：论文在广义概率论框架下研究模型的“解释”问题，其关于为复杂模型寻找经典、可解释表示的理论探讨，与化学信息学中构建可解释AI模型（包括大模型）的核心挑战直接相关。

**📖 中文摘要**

论文在广义概率理论的范畴中引入了“解释”的概念，并证明每个局部有限的概率模型都有一个经典的、尖锐的解释。虽然论文本身是高度理论性的，但其核心思想——为复杂系统（如概率模型）寻找经典的、可解释的表示——与化学信息学和质谱分析中常面临的问题相通：例如，如何为复杂的质谱数据或分子性质预测模型提供可解释的、基于物理或化学原理的“解释”或表示。这项工作为构建可解释的化学AI模型提供了理论工具和视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a notion of the ``explanation" of one (generalized) probabilistic model by another as particular kind of span in the category $\Prob$ of probabilistic models and morphisms. We show that explanations compose under a standard pullback construction (notwithstanding that $\Prob$ does not support arbitrary pullbacks). We then show that every locally-finite probabilistic model has a canonical, sharp classical explanation. The construction is functorial, so every locally-finite probabilistic theory has a canonical, sharp classical (though of course, usually non-local) representation.

</details>

---

### 54. [Predicting Atomistic Transitions with Transformers](https://arxiv.org/abs/2603.06526)

**基本信息**

- 🔗 arXiv: [`2603.06526`](https://arxiv.org/abs/2603.06526)
- 👥 作者: Henry Tischler, Wenting Li, Qi Tang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06526.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用Transformer模型预测原子尺度转变，这是将“化学大模型”（具体为Transformer架构）应用于材料科学和计算化学中结构动力学问题的直接范例。

**📖 中文摘要**

论文展示了如何使用Transformer模型来预测纳米团簇中的原子尺度转变路径。作者训练模型以学习支配原子转变的复杂涌现行为，作为一个快速的替代模型，从而大幅降低寻找这些转变的计算成本。这项工作是将Transformer这一主流大模型架构直接应用于原子尺度模拟和材料科学预测的实例，展示了AI大模型在理解和预测物质微观结构动态变化方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate knowledge of the atomistic transition pathways in materials and material surfaces is crucial for many material science problems. However, conventional simulation techniques used to find these transitions are extremely computationally intensive. Even with large-scale, accelerated material simulations, the computational cost constrains the applicable domain in practice. Machine learning models, with the potential to learn the complex emergent behaviors governing atomistic transitions as a fast surrogate model, have great promise to predict transitions with a vastly reduced computational cost. Here, we demonstrate how transformers can be trained to predict atomistic transitions in nano-clusters. We show how we evaluate physical validity of the predictions and how a multitude of additional, different microstates can be generated by slightly varying the data provided to the model.

</details>

---

### 55. [FragFM: Hierarchical Framework for Efficient Molecule Generation via Fragment-Level Discrete Flow Matching](https://arxiv.org/abs/2502.15805)

**基本信息**

- 🔗 arXiv: [`2502.15805`](https://arxiv.org/abs/2502.15805)
- 👥 作者: Joongwon Lee, Seonghwan Kim, Seokhyun Moon 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.15805.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的基于片段和流匹配的生成模型（FragFM）用于分子生成，这是“化学大模型”在分子设计领域的一个具体而重要的研究方向。

**📖 中文摘要**

论文提出了FragFM，一个通过片段级离散流匹配进行高效分子图生成的层次化框架。该方法在片段级别生成分子，并利用从粗到细的自编码器在原子级别重建细节。FragFM代表了使用生成式AI模型（特别是基于流匹配的模型）进行分子设计的最新进展。它通过操作化学片段而非原子，实现了更高效、可扩展的分子生成，并展示了在性质控制方面的优势。这直接推动了化学大模型在分子生成领域的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce FragFM, a novel hierarchical framework via fragment-level discrete flow matching for efficient molecular graph generation. FragFM generates molecules at the fragment level, leveraging a coarse-to-fine autoencoder to reconstruct details at the atom level. Together with a stochastic fragment bag strategy to effectively handle a large fragment space, our framework enables more efficient, scalable molecular generation. We demonstrate that our fragment-based approach achieves better property control than the atom-based method and additional flexibility through conditioning the fragment bag. We also propose a Natural Product Generation benchmark (NPGen) to evaluate the ability of modern molecular graph generative models to generate natural product-like molecules. Since natural products are biologically prevalidated and differ from typical drug-like molecules, our benchmark provides a more challenging yet meaningful evaluation relevant to drug discovery. We conduct a comparative study of FragFM against various models on diverse molecular generation benchmarks, including NPGen, demonstrating superior performance. The results highlight the potential of fragment-based generative modeling for large-scale, property-aware molecular design, paving the way for more efficient exploration of chemical space.

</details>

---

### 56. [From Tokenizer Bias to Backbone Capability: A Controlled Study of LLMs for Time Series Forecasting](https://arxiv.org/abs/2504.08818)

**基本信息**

- 🔗 arXiv: [`2504.08818`](https://arxiv.org/abs/2504.08818)
- 👥 作者: Xinyu Zhang, Shanshan Feng, Xutao Li 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2504.08818.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是系统性地评估LLM作为非文本数据（时间序列）预测主干的能力，其研究范式（Tokenizer-LLM主干-Detokenizer）和评估方法（控制变量、探究模型本质能力）与如何有效利用和评估“化学大模型”处理化学数据（如分子序列、谱图）直接相关。

**📖 中文摘要**

论文探讨了使用预训练大语言模型作为时间序列预测主干模型的有效性。虽然主题是时间序列，但其方法论的核心——使用Tokenizer将输入数据映射到LLM的token空间，通过冻结或微调的LLM主干进行处理，再用Detokenizer重建预测——与许多将非文本数据（如分子、光谱）适配到大语言模型的研究范式高度相似。论文通过控制实验剥离Tokenizer偏差的影响，探究LLM主干的内在预测能力，这种分析思路对于评估化学大模型（如将分子或质谱表示为序列后输入LLM）的实质贡献具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Using pre-trained large language models (LLMs) as a backbone for time series prediction has recently attracted growing research interest. Existing approaches typically split time series into patches, map them to the token space of LLMs via a Tokenizer, process the tokens through a frozen or fine-tuned LLM backbone, and then reconstruct numerical forecasts using a Detokenizer. However, the actual effectiveness of LLMs for time series forecasting remains under debate. We observe that when trained and evaluated on small datasets, these Tokenizer-Detokenizer pairs often overfit to the specific data distribution, thereby masking the intrinsic predictive capability of the LLM backbone. To investigate the inherent potential of LLMs in this context, we design three models with identical architectures but distinct pre-training strategies. By leveraging large-scale pre-training, we obtain more unbiased Tokenizer-Detokenizer pairs that are seamlessly integrated with the LLM backbone. Through controlled experiments, we evaluate the zero-shot and few-shot forecasting performance of the LLM, offering insights into its true capabilities. Our extensive experiments reveal that, although the LLM backbone shows some promise, its performance remains limited and does not consistently surpass that of models specifically trained on large-scale time series data. Our source code is publicly available in the repository: this https URL .

</details>

---

### 57. [Quantifying Cross-Attention Interaction in Transformers for Interpreting TCR-pMHC Binding](https://arxiv.org/abs/2507.03197)

**基本信息**

- 🔗 arXiv: [`2507.03197`](https://arxiv.org/abs/2507.03197)
- 👥 作者: Jiarui Li, Zixiang Yin, Haley Smith 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.03197.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于解释Transformer模型（一种重要的深度学习架构，可视为广义的“大模型”范畴）在生物化学领域（具体是TCR-pMHC结合预测）中行为的方法。这直接关联到使用复杂模型（化学大模型）进行化学/生物分子结构推理（质谱结构推理的类比和扩展，属于分子相互作用和结构预测）。

**📖 中文摘要**

本文提出了一种名为“量化交叉注意力交互”（QCAI）的新事后解释方法，旨在解释用于TCR-pMHC结合建模的编码器-解码器Transformer模型中的交叉注意力机制。T细胞受体（TCR）与主要组织相容性复合体（pMHC）的结合建模对于理解人类免疫反应的基本机制和开发疗法至关重要。虽然像TULIP这样的Transformer模型在该领域取得了令人印象深刻的性能，但其黑盒性质阻碍了可解释性，从而限制了对T细胞反应的更深层次机制理解。QCAI方法专门设计用于解释Transformer解码器中的交叉注意力机制。为了对XAI方法进行定量评估，作者汇编了TCR-XAI基准，该基准包含274个实验确定的TCR-pMHC结构作为结合的真实依据。使用这些结构，他们计算了TCR-pMHC相互作用区域中相关氨基酸残基之间的物理距离，并评估了他们的方法和其他方法在整个数据集中估计该区域残基重要性的效果。结果表明，QCAI在TCR-XAI基准测试中，在可解释性和预测准确性方面都达到了最先进的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

CD8+ "killer" T cells and CD4+ "helper" T cells play a central role in the adaptive immune system by recognizing antigens presented by Major Histocompatibility Complex (pMHC) molecules via T Cell Receptors (TCRs). Modeling binding between T cells and the pMHC complex is fundamental to understanding basic mechanisms of human immune response as well as in developing therapies. While transformer-based models such as TULIP have achieved impressive performance in this domain, their black-box nature precludes interpretability and thus limits a deeper mechanistic understanding of T cell response. Most existing post-hoc explainable AI (XAI) methods are confined to encoder-only, co-attention, or model-specific architectures and cannot handle encoder-decoder transformers used in TCR-pMHC modeling. To address this gap, we propose Quantifying Cross-Attention Interaction (QCAI), a new post-hoc method designed to interpret the cross-attention mechanisms in transformer decoders. Quantitative evaluation is a challenge for XAI methods; we have compiled TCR-XAI, a benchmark consisting of 274 experimentally determined TCR-pMHC structures to serve as ground truth for binding. Using these structures we compute physical distances between relevant amino acid residues in the TCR-pMHC interaction region and evaluate how well our method and others estimate the importance of residues in this region across the dataset. We show that QCAI achieves state-of-the-art performance on both interpretability and prediction accuracy under the TCR-XAI benchmark.

</details>

---

### 58. [TrinityDNA: A Bio-Inspired Foundational Model for Efficient Long-Sequence DNA Modeling](https://arxiv.org/abs/2507.19229)

**基本信息**

- 🔗 arXiv: [`2507.19229`](https://arxiv.org/abs/2507.19229)
- 👥 作者: Qirong Yang, Yucheng Guo, Zicheng Liu 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.19229.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于DNA序列建模的“基础模型”（TrinityDNA）。这属于在生物化学/生物信息学子领域构建和利用“大模型”（基础模型）来处理和理解分子（此处是DNA大分子）序列信息，可视为化学信息学和生物分子结构推理的紧密相关领域。

**📖 中文摘要**

本文提出了TrinityDNA，一种新颖的DNA基础模型，旨在解决基因组序列建模中的独特挑战，例如长程依赖性和DNA固有的结构复杂性。该模型整合了生物学启发的组件，包括用于捕获DNA结构特征的Groove Fusion和处理DNA序列固有对称性的门控反向互补（GRC）。此外，作者引入了一种多尺度注意力机制，允许模型关注不同级别的序列依赖性，以及一种进化训练策略，使模型逐步适应原核和真核基因组。TrinityDNA为基因组序列建模提供了更准确和高效的方法，在基因功能预测、调控机制发现和其他基因组学应用中提供了显著改进。该模型弥合了机器学习技术与生物学见解之间的差距，为更有效地分析基因组数据铺平了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The modeling of genomic sequences presents unique challenges due to their length and structural complexity. Traditional sequence models struggle to capture long-range dependencies and biological features inherent in DNA. In this work, we propose TrinityDNA, a novel DNA foundational model designed to address these challenges. The model integrates biologically informed components, including Groove Fusion for capturing DNA's structural features and Gated Reverse Complement (GRC) to handle the inherent symmetry of DNA sequences. Additionally, we introduce a multi-scale attention mechanism that allows the model to attend to varying levels of sequence dependencies, and an evolutionary training strategy that progressively adapts the model to both prokaryotic and eukaryotic genomes. TrinityDNA provides a more accurate and efficient approach to genomic sequence modeling, offering significant improvements in gene function prediction, regulatory mechanism discovery, and other genomics applications. Our model bridges the gap between machine learning techniques and biological insights, paving the way for more effective analysis of genomic data. Additionally, we introduced a new DNA long-sequence CDS annotation benchmark to make evaluations more comprehensive and oriented toward practical applications.

</details>

---

### 59. [A Multi-Agent System Enables Versatile Information Extraction from the Chemical Literature](https://arxiv.org/abs/2507.20230)

**基本信息**

- 🔗 arXiv: [`2507.20230`](https://arxiv.org/abs/2507.20230)
- 👥 作者: Yufan Chen, Ching Ting Leung, Bowen Yu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.20230.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于从化学文献中自动提取化学信息的AI系统，这直接服务于化学信息学领域，旨在构建高质量的化学数据库，是AI驱动化学研究的基础。

**📖 中文摘要**

本文提出了一种基于多模态大语言模型（MLLM）的多智能体系统，用于从化学文献中自动、稳健地提取化学信息。该系统利用MLLM强大的推理能力来理解多样的化学图形结构，并将提取任务分解为子任务。它协调一组专门的智能体，每个智能体将MLLM的能力与专用工具和网络服务的精确、领域特定优势相结合，以准确解决子任务并将结果整合为统一输出。该系统在文献中复杂的多模态化学反应图形基准数据集上取得了76.27%的F1分数，显著超越了之前的最佳模型（39.13%）。此外，它还在分子图像识别、反应图像解析、命名实体识别和基于文本的反应提取等一系列其他信息提取任务中展示了广泛适用性。这项工作朝着将化学信息自动提取为结构化数据集迈出了关键一步，这将极大地促进AI驱动的化学研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To fully expedite AI-powered chemical research, high-quality chemical databases are the foundation. Automatic extraction of chemical information from the literature is essential for constructing reaction databases, but it is currently limited by the multimodality and style variability of chemical information. In this work, we developed a multimodal large language model (MLLM)-based multi-agent system for robust and automated chemical information extraction. It utilizes the MLLM's strong reasoning capability to understand the structure of diverse chemical graphics and decompose the extraction task into sub-tasks. It then coordinates a set of specialized agents, each combining the capabilities of the MLLM with the precise, domain-specific strengths of dedicated tools and web services, to solve the subtasks accurately and integrate the results into a unified output. Our system achieved an F1 score of 76.27% on a benchmark dataset of sophisticated multimodal chemical reaction graphics from the literature, surpassing the previous state-of-the-art model (F1 score of 39.13%) by a significant margin. Additionally, it demonstrated versatile applicability in a range of other information extraction tasks, including molecular image recognition, reaction image parsing, named entity recognition and text-based reaction extraction. This work is a critical step toward automated chemical information extraction into structured datasets, which will be a strong promoter of AI-driven chemical research.

</details>

---

### 60. [Agri-Query: A Case Study on RAG vs. Long-Context LLMs for Cross-Lingual Technical Question Answering](https://arxiv.org/abs/2508.18093)

**基本信息**

- 🔗 arXiv: [`2508.18093`](https://arxiv.org/abs/2508.18093)
- 👥 作者: Julius Gun, Timo Oksanen
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.18093.pdf)

**💡 相关性分析**

满足标准3：论文是一项关于长上下文LLM与RAG在技术文档问答中性能比较的案例研究。虽然其应用领域是农业机械，但论文的核心是对LLM（作为大模型的一种）在复杂信息检索和推理任务中能力的系统性评估和讨论。这提供了关于大模型在实际、专业领域应用效能的重要见解和展望，与“化学大模型”在专业领域（如化学文献处理）的应用评估具有方法论上的相关性。

**📖 中文摘要**

本文提出了一项案例研究，评估了具有128K令牌上下文窗口的大型语言模型（LLM）在技术问答（QA）任务上的表现。基准测试基于一份农业机械的用户手册构建，该手册有英文、法文和德文版本。它模拟了一个跨语言信息检索场景，其中问题以英文提出，但需要针对所有三种语言版本的手册进行回答。评估侧重于现实的“大海捞针”挑战，并包含无法回答的问题以测试幻觉。作者比较了九种使用直接提示的长上下文LLM与三种检索增强生成（RAG）策略（关键词、语义、混合）的性能，并使用LLM作为评判员进行评估。研究结果表明，对于这份特定的手册，混合RAG consistently优于直接长上下文提示。像Gemini 2.5 Flash和较小的Qwen 2.5 7B这样的模型在使用RAG时，在所有语言上都实现了高准确率（超过85%）。本文对LLM在特定工业领域（此处为农业机械，但方法论可推广）的性能进行了详细分析，并提供了一个用于类似评估的开放框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a case study evaluating large language models (LLMs) with 128K-token context windows on a technical question answering (QA) task. Our benchmark is built on a user manual for an agricultural machine, available in English, French, and German. It simulates a cross-lingual information retrieval scenario where questions are posed in English against all three language versions of the manual. The evaluation focuses on realistic "needle-in-a-haystack" challenges and includes unanswerable questions to test for hallucinations. We compare nine long-context LLMs using direct prompting against three Retrieval-Augmented Generation (RAG) strategies (keyword, semantic, hybrid), with an LLM-as-a-judge for evaluation. Our findings for this specific manual show that Hybrid RAG consistently outperforms direct long-context prompting. Models like Gemini 2.5 Flash and the smaller Qwen 2.5 7B achieve high accuracy (over 85%) across all languages with RAG. This paper contributes a detailed analysis of LLM performance in a specialized industrial domain and an open framework for similar evaluations, highlighting practical trade-offs and challenges.

</details>

---

### 61. [Online Minimization of Polarization and Disagreement via Low-Rank Matrix Bandits](https://arxiv.org/abs/2510.00803)

**基本信息**

- 🔗 arXiv: [`2510.00803`](https://arxiv.org/abs/2510.00803)
- 👥 作者: Federico Cinus, Yuko Kuroki, Atsushi Miyauchi 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.00803.pdf)

**💡 相关性分析**

满足标准3：论文的核心是将大型语言模型/意见动力学模型（作为复杂系统模型）的在线干预和控制问题形式化为一个新颖的赌博机问题，并提出了解决方案。这属于对“大模型”（此处是社会动力学模型）行为进行建模、优化和评估的前沿方法论讨论，与如何理解和控制复杂模型系统相关，为相关领域（包括化学信息学中模型的应用和优化）提供了理论和方法参考。

**📖 中文摘要**

本文研究了在不完全信息下，基于Friedkin-Johnsen意见动力学模型最小化极化和分歧的问题。与先前假设静态设置且完全了解智能体内在意见的工作不同，作者解决了更现实的在线设置，其中内在意见未知，必须通过顺序观察来学习。这个新颖的设置自然地反映了社交媒体平台上的周期性干预，被表述为一个遗憾最小化问题，从而在社交媒体平台的算法干预理论与多臂赌博机理论之间建立了关键联系。在他们的表述中，学习者在干预后只能观察到总体极化和分歧的标量反馈。针对这个新颖的赌博机问题，作者提出了一种基于低秩矩阵赌博机的两阶段算法。该算法首先执行子空间估计以识别潜在的低维结构，然后在从估计子空间导出的紧凑维度表示中采用线性赌博机算法。作者表明，他们的算法在时间范围T内实现了$\widetilde{\mathcal{O}}\big(\max(\tfrac{1}{\kappa},\sqrt{|V|})\sqrt{|V|T}\big)$的累积遗憾，其中V是智能体集合，$\kappa$是一个依赖于干预多样性的参数。实证结果验证了他们的算法在累积遗憾和运行时间方面都显著优于线性赌博机基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study the problem of minimizing polarization and disagreement in the Friedkin-Johnsen opinion dynamics model under incomplete information. Unlike prior work that assumes a static setting with full knowledge of agents' innate opinions, we address the more realistic online setting where innate opinions are unknown and must be learned through sequential observations. This novel setting, which naturally mirrors periodic interventions on social media platforms, is formulated as a regret minimization problem, establishing a key connection between algorithmic interventions on social media platforms and the theory of multi-armed bandits. In our formulation, a learner observes only a scalar feedback of the overall polarization and disagreement after an intervention. For this novel bandit problem, we propose a two-stage algorithm based on low-rank matrix bandits. The algorithm first performs subspace estimation to identify an underlying low-dimensional structure, and then employs a linear bandit algorithm within the compact dimensional representation derived from the estimated subspace. We show that our algorithm achieves the cumulative regret of $\widetilde{\mathcal{O}}\big(\max(\tfrac{1}{\kappa},\sqrt{|V|})\sqrt{|V|T}\big)$ over time horizon $T$, where $V$ is the set of agents and $\kappa$ is a parameter dependent on the diversity of interventions. Empirical results validate that our algorithm significantly outperforms a linear bandit baseline in terms of both cumulative regret and running time.

</details>

---

### 62. [KLASS: KL-Guided Fast Inference in Masked Diffusion Models](https://arxiv.org/abs/2511.05664)

**基本信息**

- 🔗 arXiv: [`2511.05664`](https://arxiv.org/abs/2511.05664)
- 👥 作者: Seo Hyun Kim, Sunwoo Hong, Hojung Jung 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05664.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种可用于加速扩散模型推理的采样方法，并在评估中包含了分子生成任务。这直接关联到‘化学大模型’主题下的生成模型和高效推理方法。

**📖 中文摘要**

本文提出了KLASS（KL自适应稳定性采样），一种用于掩码扩散模型的快速采样方法。该方法利用标记级别的KL散度来识别稳定、高置信度的预测，从而在每次迭代中无需额外模型训练即可解掩多个标记，显著加速生成过程。作者在包括分子生成在内的多个领域验证了KLASS的有效性，表明其作为一种通用采样器的潜力。虽然论文主要关注语言和图像生成，但其方法在分子生成任务上的应用与化学信息学中的生成模型主题相关，特别是涉及使用扩散模型进行分子结构生成和推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Masked diffusion models have demonstrated competitive results on various tasks including language generation. However, due to its iterative refinement process, the inference is often bottlenecked by slow and static sampling speed. To overcome this problem, we introduce `KL-Adaptive Stability Sampling' (KLASS), a fast yet effective sampling method that exploits token-level KL divergence to identify stable, high-confidence predictions. By unmasking multiple tokens in each iteration without any additional model training, our approach speeds up generation significantly while maintaining sample quality. On reasoning benchmarks, KLASS achieves up to $2.78\times$ wall-clock speedups while improving performance over standard greedy decoding, attaining state-of-the-art results among diffusion-based samplers. We further validate KLASS across diverse domains, including text, image, and molecular generation, showing its effectiveness as a broadly applicable sampler across different models.

</details>

---

### 63. [CADM: Cluster-customized Adaptive Distance Metric for Categorical Data Clustering](https://arxiv.org/abs/2511.05826)

**基本信息**

- 🔗 arXiv: [`2511.05826`](https://arxiv.org/abs/2511.05826)
- 👥 作者: Taixi Chen, Yiu-ming Cheung, Yiqun Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.05826.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的距离度量方法（CADM）并提供了源代码。这种用于聚类和分析（可能是化学）数据的工具，可以作为化学信息学中构建或分析化学大模型的数据预处理或特征工程资源。

**📖 中文摘要**

本文提出了CADM，一种用于分类数据聚类的、针对集群定制的自适应距离度量方法。该方法根据不同集群中属性的不同分布来竞争性地更新距离，从而提供更合理的距离测量。论文还将其扩展到包含数值和分类属性的混合数据。实验证明了该方法的有效性。虽然论文主要关注通用数据聚类，但其提出的自适应距离度量框架，特别是处理混合类型数据（可能包含分子描述符等化学数据）的能力，为化学信息学中的数据分析和模型构建提供了潜在的工具和方法论支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

An appropriate distance metric is crucial for categorical data clustering, as the distance between categorical data cannot be directly calculated. However, the distances between attribute values usually vary in different clusters induced by their different distributions, which has not been taken into account, thus leading to unreasonable distance measurement. Therefore, we propose a cluster-customized distance metric for categorical data clustering, which can competitively update distances based on different distributions of attributes in each cluster. In addition, we extend the proposed distance metric to the mixed data that contains both numerical and categorical attributes. Experiments demonstrate the efficacy of the proposed method, i.e., achieving an average ranking of around first in fourteen datasets. The source code is available at this https URL

</details>

---

### 64. [Diffusion Fine-Tuning via Reparameterized Policy Gradient of the Soft Q-Function](https://arxiv.org/abs/2512.04559)

**基本信息**

- 🔗 arXiv: [`2512.04559`](https://arxiv.org/abs/2512.04559)
- 👥 作者: Hyeongyu Kang, Jaewoo Lee, Woocheol Shin 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.04559.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对扩散模型的强化学习微调框架。优化扩散模型生成质量与多样性的方法，直接适用于化学信息学中用于分子设计或性质预测的生成式大模型的开发和调优。

**📖 中文摘要**

本文提出了SQDF（基于软Q函数的扩散微调），一种用于扩散模型对齐的新型KL正则化强化学习方法。该方法应用了基于训练免费、可微分的软Q函数估计的重参数化策略梯度，并引入了折扣因子、一致性模型集成和离策略经验回放缓冲区等创新来改进Q函数估计并管理奖励-多样性权衡。实验表明，SQDF在文本到图像对齐任务中实现了优异的目标奖励，同时保持了多样性。论文的研究聚焦于优化和调整生成模型（如扩散模型）的行为，这属于构建和优化‘化学大模型’（特别是用于分子生成的扩散模型）的核心技术范畴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion models excel at generating high-likelihood samples but often require alignment with downstream objectives. Existing fine-tuning methods for diffusion models significantly suffer from reward over-optimization, resulting in high-reward but unnatural samples and degraded diversity. To mitigate over-optimization, we propose Soft Q-based Diffusion Finetuning (SQDF), a novel KL-regularized RL method for diffusion alignment that applies a reparameterized policy gradient of a training-free, differentiable estimation of the soft Q-function. SQDF is further enhanced with three innovations: a discount factor for proper credit assignment in the denoising process, the integration of consistency models to refine Q-function estimates, and the use of an off-policy replay buffer to improve mode coverage and manage the reward-diversity trade-off. Our experiments demonstrate that SQDF achieves superior target rewards while preserving diversity in text-to-image alignment. Furthermore, in online black-box optimization, SQDF attains high sample efficiency while maintaining naturalness and diversity. Our code is available at this https URL .

</details>

---

### 65. [A Novel Patch-Based TDA Approach for Computed Tomography Imaging](https://arxiv.org/abs/2512.12108)

**基本信息**

- 🔗 arXiv: [`2512.12108`](https://arxiv.org/abs/2512.12108)
- 👥 作者: Dashti A. Ali, Aras T. Asaad, Jacob J. Peoples 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.12108.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的拓扑数据分析方法（Patch-TDA）并提供了相应的Python工具包。这种从复杂科学图像中提取特征的数据处理工具，可以作为化学信息学或质谱分析中，处理结构图像或光谱图像以构建模型的数据资源。

**📖 中文摘要**

本文提出了一种新颖的、基于图像块（patch）的拓扑数据分析（TDA）方法，专门用于处理体积CT成像数据。该方法通过构建持久同调（PH）来提取拓扑特征（如连通分量、环、空洞），旨在改进基于CT图像的机器学习模型的性能。作者进行了系统实验，证明该方法在分类性能和计算时间上均优于传统的3D立方体复形算法和放射组学特征。论文提供了方便的Python包（Patch-TDA）以方便使用。该方法为从复杂科学图像（如医学影像，潜在也可用于材料或化学结构的显微图像）中提取高层次、稳健的特征提供了新的数据分析和特征工程工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The development of machine learning (ML) models based on computed tomography (CT) imaging has been a major focus due to the promise that imaging holds for diagnosis, staging, and prognostication. These models often rely on the extraction of hand-crafted features, incorporating robust feature engineering improves the performance of these models. Topological data analysis (TDA), based on the mathematical field of algebraic topology, focuses on data from a topological perspective, extracting deeper insight and higher dimensional structures. Persistent homology (PH), a fundamental tool in TDA, extracts topological features such as connected components, cycles, and voids. A popular approach to construct PH from 3D CT images is to utilize the 3D cubical complex filtration, a method adapted for grid-structured data. However, this approach is subject to poor performance and high computational cost with higher resolution CT images. This study introduces a novel patch-based PH construction approach tailored for volumetric CT imaging data that improves performance and reduces computational time. This study conducts a series of systematic experiments to comprehensively analyze the performance of the proposed method with various parameters and benchmarks against the 3D cubical complex algorithm and radiomic features. Our results highlight the dominance of the patch-based TDA approach in terms of both classification performance and computational time. The proposed approach outperformed the cubical complex method and radiomic features, achieving average improvement of 7.2%, 3.6%, 2.7%, 8.0%, and 7.2% in accuracy, AUC, sensitivity, specificity, and F1 score, respectively, across all datasets. Finally, we provide a convenient python package, Patch-TDA, to facilitate the utilization of the proposed approach.

</details>

---

### 66. [Creating a Hybrid Rule and Neural Network Based Semantic Tagger using Silver Standard Data: the PyMUSAS framework for Multilingual Semantic Annotation](https://arxiv.org/abs/2601.09648)

**基本信息**

- 🔗 arXiv: [`2601.09648`](https://arxiv.org/abs/2601.09648)
- 👥 作者: Andrew Moore, Paul Rayson, Dawn Archer 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.09648.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个多语言语义标注框架（PyMUSAS），并发布了相关的模型、数据集和代码。这种用于文本信息提取和标注的工具包，可以作为化学信息学中从科学文献构建数据集的潜在资源或工具。

**📖 中文摘要**

本文介绍了PyMUSAS框架，用于多语言语义标注。该工作创建了一个新的银标英语数据集，以克服缺乏手动标注训练数据的问题，并在此基础上训练和评估了各种单语和多语言神经模型。研究展示了如何通过神经网络模型增强基于规则的系统。最终发布的资源包括神经网络模型、训练数据、中文评估数据集和所有代码。这项工作在自然语言处理领域提供了新的语义标注工具和数据集。虽然其直接应用是语言学，但其核心——结合规则与神经网络、处理多语言数据、以及发布完整的工具链（框架、模型、数据）——为化学信息学中构建类似的多语言或跨领域文本信息提取工具（例如，从科学文献中提取化学实体和关系）提供了可借鉴的技术范式和潜在的数据处理资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Word Sense Disambiguation (WSD) has been widely evaluated using the semantic frameworks of WordNet, BabelNet, and the Oxford Dictionary of English. However, for the UCREL Semantic Analysis System (USAS) framework, no open extensive evaluation has been performed beyond lexical coverage or single language evaluation. In this work, we perform the largest semantic tagging evaluation of the rule based system that uses the lexical resources in the USAS framework covering five different languages using four existing datasets and one novel Chinese dataset. We create a new silver labelled English dataset, to overcome the lack of manually tagged training data, that we train and evaluate various mono and multilingual neural models in both mono and cross-lingual evaluation setups with comparisons to their rule based counterparts, and show how a rule based system can be enhanced with a neural network model. The resulting neural network models, including the data they were trained on, the Chinese evaluation dataset, and all of the code have been released as open resources.

</details>

---

### 67. [PepEDiff: Zero-Shot Peptide Binder Design via Protein Embedding Diffusion](https://arxiv.org/abs/2601.13327)

**基本信息**

- 🔗 arXiv: [`2601.13327`](https://arxiv.org/abs/2601.13327)
- 👥 作者: Po-Yu Liang, Tibo Duran, Jun Bai
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.13327.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕使用扩散模型和蛋白质嵌入进行肽段（小分子/生物大分子）设计。这完全属于‘化学大模型’和‘质谱结构推理’的交叉领域，即利用AI模型进行分子生成和结构功能预测。

**📖 中文摘要**

本文提出了PepEDiff，一种新颖的肽段结合剂生成器，能够在给定目标受体蛋白序列及其口袋残基的情况下，设计结合序列。该方法摒弃了依赖中间结构预测的传统范式，直接在源自预训练蛋白质嵌入模型的连续潜在空间中生成结合剂序列。通过潜在空间探索和基于扩散的采样，该方法能够生成超出已知结合剂分布范围的新肽序列。这种零样本生成策略利用全局蛋白质嵌入流形作为语义先验，使模型能够在先前未见的蛋白质空间区域中提出新的肽序列。论文在包括TIGIT在内的案例研究中评估了PepEDiff，表明其性能优于现有最先进的方法。这项工作为肽段结合剂设计提供了一个通用的、无需结构的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present PepEDiff, a novel peptide binder generator that designs binding sequences given a target receptor protein sequence and its pocket residues. Peptide binder generation is critical in therapeutic and biochemical applications, yet many existing methods rely heavily on intermediate structure prediction, adding complexity and limiting sequence diversity. Our approach departs from this paradigm by generating binder sequences directly in a continuous latent space derived from a pretrained protein embedding model, without relying on predicted structures, thereby improving structural and sequence diversity. To encourage the model to capture binding-relevant features rather than memorizing known sequences, we perform latent-space exploration and diffusion-based sampling, enabling the generation of peptides beyond the limited distribution of known binders. This zero-shot generative strategy leverages the global protein embedding manifold as a semantic prior, allowing the model to propose novel peptide sequences in previously unseen regions of the protein space. We evaluate PepEDiff on TIGIT, a challenging target with a large, flat protein-protein interaction interface that lacks a druggable pocket. Despite its simplicity, our method outperforms state-of-the-art approaches across benchmark tests and in the TIGIT case study, demonstrating its potential as a general, structure-free framework for zero-shot peptide binder design. The code for this research is available at GitHub: this https URL

</details>

---

### 68. [Beyond Mapping : Domain-Invariant Representations via Spectral Embedding of Optimal Transport Plans](https://arxiv.org/abs/2601.13350)

**基本信息**

- 🔗 arXiv: [`2601.13350`](https://arxiv.org/abs/2601.13350)
- 👥 作者: Abdel Djalil Sad Saoud, Fred Maurice Ngolè Mboula, Hanane Slimani
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.13350.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种用于领域适应和获得领域不变表示的通用机器学习框架。这种处理分布偏移、提升模型泛化能力的方法，可以作为构建鲁棒的化学大模型或质谱分析模型的重要技术工具。

**📖 中文摘要**

本文提出了一种新的领域适应方法，通过将平滑的最优传输计划解释为连接源域和目标域的二部图的邻接矩阵，并基于此进行谱嵌入，从而推导出领域不变的样本表示。该方法避免了传统基于Monge映射近似的方法对正则化策略和超参数的敏感性。作者在音乐流派识别、音乐-语音 discrimination 以及电缆缺陷检测等声学和时域反射任务上评估了该方法，取得了强劲的整体性能。虽然应用领域不同，但该方法的核心——利用最优传输和谱嵌入进行领域不变表示学习——为解决化学信息学中常见的数据分布偏移问题（例如，不同仪器、不同实验条件获得的质谱数据）提供了通用的机器学习框架和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Distributional shifts between training and inference time data remain a central challenge in machine learning, often leading to poor performance. It motivated the study of principled approaches for domain alignment, such as optimal transport based unsupervised domain adaptation, that relies on approximating Monge map using transport plans, which is sensitive to the transport problem regularization strategy and hyperparameters, and might yield biased domains alignment. In this work, we propose to interpret smoothed transport plans as adjacency matrices of bipartite graphs connecting source to target domain and derive domain-invariant samples' representations through spectral embedding. We evaluate our approach on acoustic adaptation benchmarks for music genre recognition, music-speech discrimination, as well as electrical cable defect detection and classification tasks using time domain reflection in different diagnosis settings, achieving overall strong performances.

</details>

---

### 69. [SpatialMem: Metric-Aligned Long-Horizon Video Memory for Language Grounding and QA](https://arxiv.org/abs/2601.14895)

**基本信息**

- 🔗 arXiv: [`2601.14895`](https://arxiv.org/abs/2601.14895)
- 👥 作者: Xinyi Zheng, Yunze Liu, Chi-Hao Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.14895.pdf)

**💡 相关性分析**

满足标准3：论文提出了一种新颖的多模态记忆和检索架构。虽然应用场景不同，但其关于结构化表示、关系推理和可查询记忆系统的讨论，为思考如何构建和管理用于化学大模型或质谱结构推理的知识库和数据系统提供了重要的前瞻性视角和方法论参考。

**📖 中文摘要**

本文提出了SpatialMem，一个以记忆为中心的系统，用于从以自我为中心的视频中进行长时程、基于语言的检索和问答。该系统为室内场景构建了一个度量对齐的空间支架，并以3D坐标存储开放词汇对象节点，链接证据图像块、视觉嵌入和文本描述。这种设计支持对关系（如距离、方向、可见性）进行可解释的、空间 grounded 的查询。虽然论文主要关注视觉和机器人领域，但其核心思想——构建一个结构化的、可查询的多模态记忆来表示和推理复杂环境——与化学信息学中构建可解释的、基于知识的分子或反应数据库系统有概念上的相似性。其方法论可能为管理化学结构、属性和光谱数据的多模态数据库提供启发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present SpatialMem, a memory-centric system for long-horizon, language-grounded retrieval and QA from egocentric video, where metric 3D serves as an interpretable indexing scaffold rather than an explicit mapping objective. Starting from casually captured egocentric RGB video, SpatialMem builds a metric-aligned spatial scaffold for indoor scenes, detects structural 3D anchors (walls, doors, windows) as first-layer support, and populates a hierarchical memory with open-vocabulary object nodes that link evidence patches, visual embeddings, and two-layer textual descriptions to 3D coordinates for compact storage and fast retrieval. This design enables interpretable, spatially grounded queries over relations (e.g., distance, direction, visibility) and supports downstream tasks such as language-guided retrieval/QA and offline navigation-style guidance over a prebuilt memory, without specialized sensors. Experiments on one public Replica scene and two real-world egocentric indoor scenes show that SpatialMem maintains stable layout reasoning, offline guidance, and hierarchical retrieval across these evaluated scenes despite increasing clutter and occlusion. A compact ablation further shows that the two-layer description memory improves path-level grounding, while moderate scale perturbation causes only limited degradation. These results position SpatialMem as an efficient and extensible memory interface for spatially grounded long-horizon video understanding.

</details>

---

### 70. [Knowledge Graphs are Implicit Reward Models: Path-Derived Signals Enable Compositional Reasoning](https://arxiv.org/abs/2601.15160)

**基本信息**

- 🔗 arXiv: [`2601.15160`](https://arxiv.org/abs/2601.15160)
- 👥 作者: Yuval Kansal, Niraj K. Jha
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.15160.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是利用知识图谱提升大模型在科学领域的推理能力（标准1）。同时，这项工作为如何将领域知识（如化学知识）整合到大模型中提供了重要的方法论讨论和前瞻性方向，属于相关的重要讨论（标准3）。

**📖 中文摘要**

本文提出了一种基于知识图谱（KG）作为隐式奖励模型的自底向上学习范式，用于增强大语言模型在专业科学领域（如医学）的组合式多跳推理能力。通过从知识图谱路径中推导新的奖励信号，该框架提供了可验证的、可扩展的、有根据的监督，鼓励模型组合中间公理。在医学领域的实验中，该方法使模型在复杂的多跳查询上显著优于更大的模型和前沿系统。这项工作表明，将推理过程建立在结构化知识中是实现智能推理的可扩展且有效的途径。这项研究直接关联到如何利用领域知识（如化学知识图谱）来指导和提升大模型在科学推理任务（如分子性质推理、反应预测）中的性能，是化学大模型研究的前沿方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models have achieved near-expert performance in structured reasoning domains like mathematics and programming, yet their ability to perform compositional multi-hop reasoning in specialized scientific fields remains limited. We propose a bottom-up learning paradigm in which models are grounded in axiomatic domain facts and compose them to solve complex, unseen tasks. To this end, we present a post-training pipeline, based on a combination of supervised fine-tuning and reinforcement learning (RL), in which knowledge graphs act as implicit reward models. By deriving novel reward signals from knowledge graph paths, we provide verifiable, scalable, and grounded supervision that encourages models to compose intermediate axioms rather than optimize only final answers during RL. We validate this approach in the medical domain, training a 14B model on short-hop reasoning paths (1-3 hops) and evaluating its zero-shot generalization to complex multi-hop queries (4-5 hops). Our experiments show that path-derived rewards act as a "compositional bridge", enabling our model to significantly outperform much larger models and frontier systems like GPT-5.2 and Gemini 3 Pro, on the most difficult reasoning tasks. Furthermore, we demonstrate the robustness of our approach to adversarial perturbations against option-shuffling stress tests. This work suggests that grounding the reasoning process in structured knowledge is a scalable and efficient path toward intelligent reasoning. Our code is publicly available at: this https URL .

</details>

---

### 71. [SRA 2: Variational Autoencoder Self-Representation Alignment for Efficient Diffusion Training](https://arxiv.org/abs/2601.17830)

**基本信息**

- 🔗 arXiv: [`2601.17830`](https://arxiv.org/abs/2601.17830)
- 👥 作者: Mengmeng Wang, Dengyang Jiang, Liuzhuozheng Li 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.17830.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提高扩散Transformer训练效率的框架。加速和稳定扩散模型的训练技术，直接适用于需要训练大规模化学分子生成或性质预测模型的研究。

**📖 中文摘要**

本文提出了SRA 2，一个用于高效扩散模型训练的轻量级内在引导框架。SRA 2利用现成的预训练变分自编码器（VAE）特征，通过一个轻量级的投影层将扩散Transformer的中间潜在特征与VAE特征对齐，并由特征对齐损失进行监督。这种设计在不增加外部表示编码器或双模型维护的情况下加速了训练。实验表明，SRA 2在生成质量和训练收敛速度上均优于原始扩散Transformer，并与最先进的加速方法相媲美。该方法专注于优化扩散模型的训练效率，这是构建大规模化学生成模型（如用于分子设计的扩散模型）时必须面对的关键工程挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Denoising-based diffusion transformers, despite their strong generation performance, suffer from inefficient training convergence. Existing methods addressing this issue, such as REPA (relying on external representation encoders) or SRA (requiring dual-model setups), inevitably incur heavy computational overhead during training due to external dependencies. To tackle these challenges, this paper proposes SRA 2, a lightweight intrinsic guidance framework for efficient diffusion training. SRA 2 leverages off-the-shelf pre-trained Variational Autoencoder (VAE) features: their reconstruction property ensures inherent encoding of visual priors like rich texture details, structural patterns, and basic semantic information. Specifically, SRA 2 aligns the intermediate latent features of diffusion transformers with VAE features via a lightweight projection layer, supervised by a feature alignment loss. This design accelerates training without extra representation encoders or dual-model maintenance, resulting in a simple yet effective pipeline. Extensive experiments demonstrate that SRA 2 improves both generation quality and training convergence speed compared to vanilla diffusion transformers, matches or outperforms state-of-the-art acceleration methods, and incurs merely 4% extra GFLOPs with zero additional cost for external guidance models.

</details>

---

### 72. [Neural Signals Generate Clinical Notes in the Wild](https://arxiv.org/abs/2601.22197)

**基本信息**

- 🔗 arXiv: [`2601.22197`](https://arxiv.org/abs/2601.22197)
- 👥 作者: Jathurshan Pradeepkumar, Zheng Chen, Jimeng Sun
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22197.pdf)

**💡 相关性分析**

满足标准2和3：论文构建了一个大规模的多模态（EEG-文本）数据集并发布了模型（标准2）。同时，其提出的从复杂科学仪器数据（时间序列）生成文本报告的端到端多模态大模型框架，为‘质谱结构推理’（即从质谱数据生成分子结构描述或报告）提供了重要的技术范例和前瞻性讨论（标准3）。

**📖 中文摘要**

本文开发了CELM，首个临床脑电图到语言的基座模型，能够总结长时程、可变长度的脑电图记录，并执行端到端的临床报告生成，包括记录描述、背景活动、癫痫样异常、事件/癫痫发作和印象等多个尺度。该模型整合了预训练的脑电图基座模型和语言模型，以实现可扩展的多模态学习。虽然应用领域是神经医学，但该工作的核心贡献在于：1）构建了大规模的多模态（时间序列信号+文本）数据集；2）开发了能够处理长序列、复杂时间序列数据并生成结构化文本报告的端到端多模态大模型框架。这种方法论对于处理其他科学时间序列数据（如质谱、色谱）并生成解释性报告具有直接的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generating clinical reports that summarize abnormal patterns, diagnostic findings, and clinical interpretations from long-term EEG recordings remains labor-intensive. We curate a large-scale clinical EEG dataset with $9{,}922$ reports paired with approximately $11{,}000$ hours of EEG recordings from $9{,}048$ patients. We therefore develop CELM, the first clinical EEG-to-Language foundation model capable of summarizing long-duration, variable-length EEG recordings and performing end-to-end clinical report generation at multiple scales, including recording description, background activity, epileptiform abnormalities, events/seizures, and impressions. Experimental results show that, with patient history supervision, our method achieves $70\%$-$95\%$ average relative improvements in standard generation metrics (e.g., ROUGE-1 and METEOR) from $0.2$-$0.3$ to $0.4$-$0.6$. In the zero-shot setting without patient history, CELM attains generation scores in the range of $0.43$-$0.52$, compared to baselines of $0.17$-$0.26$. CELM integrates pretrained EEG foundation models with language models to enable scalable multimodal learning. We release our model and benchmark construction pipeline at this https URL .

</details>

---

### 73. [A Structured Approach to Safety Case Construction for AI Systems](https://arxiv.org/abs/2601.22773)

**基本信息**

- 🔗 arXiv: [`2601.22773`](https://arxiv.org/abs/2601.22773)
- 👥 作者: Sung Une Lee, Liming Zhu, Md Shamsujjoha 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.22773.pdf)

**💡 相关性分析**

满足标准3：论文是关于AI系统（包括大模型）安全保证的综述性和方法论研究。它为如何评估和确保化学大模型在真实世界应用中的安全性与可靠性提供了重要的框架性讨论和前瞻性指导，属于相关的重要讨论。

**📖 中文摘要**

本文研究了如何为AI系统构建安全案例（Safety Case），并针对现代生成式和智能体AI系统的动态性、不可预测性等挑战，引入了全面的分类法（针对AI特定的声明类型、论证类型和证据族）和可重用的安全案例模板。每个模板都遵循针对AI系统定制的声明、论证和证据的预定义结构。这项工作为系统化、可组合、可维护地构建安全案例提供了方法，使其可信、可审计并能适应生成式和前沿AI系统的演化行为。虽然不直接研究化学模型，但确保AI系统（包括化学大模型）的安全性、可靠性和可解释性是其在高风险领域（如药物发现、材料设计）部署的前提。该论文提供了构建此类安全保证的通用框架和重要讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Safety cases, structured arguments that a system is acceptably safe, are becoming central to the governance of AI systems. Yet, traditional safety-case practices from aviation or nuclear engineering rely on well-specified system boundaries, stable architectures, and known failure modes. Modern AI systems, such as generative and agentic AI, are the opposite. Their capabilities emerge unpredictably from low-level training objectives, their behaviour varies with prompts, and their risk profiles shift through fine-tuning, scaffolding, or deployment context. This study examines how safety cases are currently constructed for AI systems and why classical approaches fail to capture these dynamics. This study introduces comprehensive taxonomies for AI-specific claim types (assertion-based, constraint-based, capability-based), argument types (demonstrative, comparative, causal/explanatory, risk-based, and normative), and evidence families (empirical, mechanistic, comparative, expert-driven, formal methods, operational/field data, and model-based). It then proposes a reusable safety-case template, each of which follows a predefined structure of claims, arguments, and evidence tailored for AI systems. Each template is illustrated by end-to-end patterns that address distinctive challenges, such as evaluation without ground truth, dynamic model updates, and threshold-based risk decisions. The result is a systematic, composable, and reusable approach to constructing and maintaining safety cases that are credible, auditable, and adaptive to the evolving behaviour of generative and frontier AI systems.

</details>

---

### 74. [MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](https://arxiv.org/abs/2602.16020)

**基本信息**

- 🔗 arXiv: [`2602.16020`](https://arxiv.org/abs/2602.16020)
- 👥 作者: Cheng Zeng, Harry W. Sullivan, Thomas Egg 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.16020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于分子晶体结构预测的生成模型（MolCrystalFlow），这直接属于“化学大模型”范畴，即利用深度学习模型（特别是生成模型）解决化学结构预测问题。

**📖 中文摘要**

本文提出了MolCrystalFlow，一种基于流匹配的生成模型，用于预测分子晶体结构。该模型将分子视为刚体，联合学习晶格矩阵、分子取向和质心位置，从而将分子内复杂性从分子间堆积中解耦。研究在开源分子晶体数据集上进行了基准测试，并展示了与通用机器学习势能集成以加速分子晶体结构预测的潜力。虽然论文核心是晶体结构预测，但其使用的生成建模框架（流匹配、图神经网络）是构建化学大模型（用于结构生成）的典型技术路径，与“化学大模型”主题在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular crystal structure prediction represents a grand challenge in computational chemistry due to large sizes of constituent molecules and complex intra- and intermolecular interactions. While generative modeling has revolutionized structure discovery for molecules, inorganic solids, and metal-organic frameworks, extending such approaches to fully periodic molecular crystals is still elusive. Here, we present MolCrystalFlow, a flow-based generative model for molecular crystal structure prediction. The framework disentangles intramolecular complexity from intermolecular packing by embedding molecules as rigid bodies and jointly learning the lattice matrix, molecular orientations, and centroid positions. Centroids and orientations are represented on their native Riemannian manifolds, allowing geodesic flow construction and graph neural network operations that respects geometric symmetries. We benchmark our model against state-of-the-art generative models for large-size periodic crystals and rule-based structure generation methods on two open-source molecular crystal datasets. We demonstrate an integration of MolCrystalFlow model with universal machine learning potential to accelerate molecular crystal structure prediction, paving the way for data-driven generative discovery of molecular crystals.

</details>

---

### 75. [Conditionally Site-Independent Neural Evolution of Antibody Sequences](https://arxiv.org/abs/2602.18982)

**基本信息**

- 🔗 arXiv: [`2602.18982`](https://arxiv.org/abs/2602.18982)
- 👥 作者: Stephen Zhewen Lu, Aakarsh Vermani, Kohei Sanno 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.18982.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发CoSiNE模型，这是一个用于抗体序列设计和优化的深度生成模型。它直接涉及利用神经网络模型（一种特定领域的“化学大模型”）来理解和生成生物分子序列，并优化其功能属性。

**📖 中文摘要**

本文提出了CoSiNE模型，用于抗体序列的条件性位点独立神经进化。该模型是一个由深度神经网络参数化的连续时间马尔可夫链，旨在捕获抗体亲和力成熟过程中的复杂上位相互作用。CoSiNE在零射击变体效应预测上超越了最先进的语言模型，并通过显式地将选择与上下文依赖的体细胞超突变解耦来改进预测。此外，还引入了引导Gillespie采样方案，以在推理时引导模型优化抗体对特定抗原的结合亲和力。这项工作将经典的系统发育模型与深度学习的表达能力相结合，用于抗体工程，是构建用于生物分子（抗体）序列设计与优化的化学/生物大模型的典型案例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Common deep learning approaches for antibody engineering focus on modeling the marginal distribution of sequences. By treating sequences as independent samples, however, these methods overlook affinity maturation as a rich and largely untapped source of information about the evolutionary process by which antibodies explore the underlying fitness landscape. In contrast, classical phylogenetic models explicitly represent evolutionary dynamics but lack the expressivity to capture complex epistatic interactions. We bridge this gap with CoSiNE, a continuous-time Markov chain parameterized by a deep neural network. Mathematically, we prove that CoSiNE provides a first-order approximation to the intractable sequential point mutation process, capturing epistatic effects with an error bound that is quadratic in branch length. Empirically, CoSiNE outperforms state-of-the-art language models in zero-shot variant effect prediction by explicitly disentangling selection from context-dependent somatic hypermutation. Finally, we introduce Guided Gillespie, a classifier-guided sampling scheme that steers CoSiNE at inference time, enabling efficient optimization of antibody binding affinity toward specific antigens.

</details>

---

### 76. [Multimodal Mixture-of-Experts with Retrieval Augmentation for Protein Active Site Identification](https://arxiv.org/abs/2603.01511)

**基本信息**

- 🔗 arXiv: [`2603.01511`](https://arxiv.org/abs/2603.01511)
- 👥 作者: Jiayang Wu, Jiale Zhou, Rubo Wang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.01511.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发MERA框架，这是一个结合了检索增强、混合专家和多模态融合的深度学习模型，专门用于蛋白质活性位点识别。这属于构建应用于结构生物信息学领域的专用“化学大模型”。

**📖 中文摘要**

本文提出了MERA，首个用于蛋白质活性位点识别的检索增强多模态混合专家框架。该框架采用分层多专家检索，通过残基级混合专家门控动态聚合链、序列和活性位点角度的上下文信息。为了解决模态退化问题，提出了基于Dempster-Shafer证据理论的可靠性感知融合策略。在ProTAD-Gen和TS125数据集上的实验表明，MERA在活性位点预测上达到了最先进的性能。这项工作展示了如何将大型模型（混合专家、检索增强）与特定领域的生物信息（蛋白质结构、序列）相结合，是构建用于蛋白质功能预测的化学/生物信息学大模型的一个实例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate identification of protein active sites at the residue level is crucial for understanding protein function and advancing drug discovery. However, current methods face two critical challenges: vulnerability in single-instance prediction due to sparse training data, and inadequate modality reliability estimation that leads to performance degradation when unreliable modalities dominate fusion processes. To address these challenges, we introduce Multimodal Mixture-of-Experts with Retrieval Augmentation (MERA), the first retrieval-augmented framework for protein active site identification. MERA employs hierarchical multi-expert retrieval that dynamically aggregates contextual information from chain, sequence, and active-site perspectives through residue-level mixture-of-experts gating. To prevent modality degradation, we propose a reliability-aware fusion strategy based on Dempster-Shafer evidence theory that quantifies modality trustworthiness through belief mass functions and learnable discounting coefficients, enabling principled multimodal integration. Extensive experiments on ProTAD-Gen and TS125 datasets demonstrate that MERA achieves state-of-the-art performance, with 90% AUPRC on active site prediction and significant gains on peptide-binding site identification, validating the effectiveness of retrieval-augmented multi-expert modeling and reliability-guided fusion.

</details>

---

### 77. [MatRIS: Toward Reliable and Efficient Pretrained Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.02002)

**基本信息**

- 🔗 arXiv: [`2603.02002`](https://arxiv.org/abs/2603.02002)
- 👥 作者: Yuanchang Zhou, Siyu Hu, Xiangyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02002.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发MatRIS，一种新的机器学习原子间势。MLIPs是“化学大模型”在计算材料科学和化学中的一个关键应用，旨在用数据驱动的模型替代传统的力场，以高精度模拟材料的性质和相互作用。

**📖 中文摘要**

本文提出了MatRIS，一种用于材料表示和相互作用模拟的不变机器学习原子间势。MatRIS引入了基于注意力的三体相互作用建模，并利用具有线性复杂度的可分离注意力机制，实现了可扩展性和表达性。在包括Matbench-Discovery、MatPES在内的多个流行基准测试中，MatRIS提供了与领先的等变模型相媲美的准确性，但训练成本更低。这项工作表明，精心设计的不变模型可以以更低的成本匹配或超过等变模型的准确性，为开发准确高效的机器学习原子间势（MLIPs）提供了启示。MLIPs是计算材料科学和化学中“化学大模型”的核心组成部分之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation MLIPs demonstrate broad applicability across diverse material systems and have emerged as a powerful and transformative paradigm in chemical and computational materials science. Equivariant MLIPs achieve state-of-the-art accuracy in a wide range of benchmarks by incorporating equivariant inductive bias. However, the reliance on tensor products and high-degree representations makes them computationally costly. This raises a fundamental question: as quantum mechanical-based datasets continue to expand, can we develop a more compact model to thoroughly exploit high-dimensional atomic interactions? In this work, we present MatRIS (\textbf{Mat}erials \textbf{R}epresentation and \textbf{I}nteraction \textbf{S}imulation), an invariant MLIP that introduces attention-based modeling of three-body interactions. MatRIS leverages a novel separable attention mechanism with linear complexity $O(N)$, enabling both scalability and expressiveness. MatRIS delivers accuracy comparable to that of leading equivariant models on a wide range of popular benchmarks (Matbench-Discovery, MatPES, MDR phonon, Molecular dataset, etc). Taking Matbench-Discovery as an example, MatRIS achieves an F1 score of up to 0.847 and attains comparable accuracy at a lower training cost. The work indicates that our carefully designed invariant models can match or exceed the accuracy of equivariant models at a fraction of the cost, shedding light on the development of accurate and efficient MLIPs.

</details>

---

### 78. [Rigidity-Aware Geometric Pretraining for Protein Design and Conformational Ensembles](https://arxiv.org/abs/2603.02406)

**基本信息**

- 🔗 arXiv: [`2603.02406`](https://arxiv.org/abs/2603.02406)
- 👥 作者: Zhanghan Ni, Yanjing Li, Zeju Qiu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.02406.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发RigidSSL，一个用于蛋白质结构生成与设计的几何预训练框架。这直接属于“化学大模型”的研究范畴，特别是针对生物大分子（蛋白质）的三维结构生成与建模。

**📖 中文摘要**

本文提出了RigidSSL，一个用于蛋白质设计和构象系综的刚性感知自监督学习预训练框架。该框架通过模拟扰动和分子动力学轨迹，学习蛋白质结构的几何先验和物理真实的构象转变。其核心是一个双向的、刚性感知的流匹配目标，共同优化平移和旋转动力学以最大化构象间的互信息。实验表明，RigidSSL变体在无条件生成中提高了可设计性、新颖性和多样性，在零射击基序支架中提高了成功率，并能在G蛋白偶联受体建模中捕获更生物物理真实的构象系综。这项工作专注于为蛋白质生成任务开发几何预训练方法，是构建用于蛋白质结构生成与设计的“化学大模型”的前沿探索。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative models have recently advanced $\textit{de novo}$ protein design by learning the statistical regularities of natural structures. However, current approaches face three key limitations: (1) Existing methods cannot jointly learn protein geometry and design tasks, where pretraining can be a solution; (2) Current pretraining methods mostly rely on local, non-rigid atomic representations for property prediction downstream tasks, limiting global geometric understanding for protein generation tasks; and (3) Existing approaches have yet to effectively model the rich dynamic and conformational information of protein structures. To overcome these issues, we introduce $\textbf{RigidSSL}$ ($\textit{Rigidity-Aware Self-Supervised Learning}$), a geometric pretraining framework that front-loads geometry learning prior to generative finetuning. Phase I (RigidSSL-Perturb) learns geometric priors from 432K structures from the AlphaFold Protein Structure Database with simulated perturbations. Phase II (RigidSSL-MD) refines these representations on 1.3K molecular dynamics trajectories to capture physically realistic transitions. Underpinning both phases is a bi-directional, rigidity-aware flow matching objective that jointly optimizes translational and rotational dynamics to maximize mutual information between conformations. Empirically, RigidSSL variants improve designability by up to 43% while enhancing novelty and diversity in unconditional generation. Furthermore, RigidSSL-Perturb improves the success rate by 5.8% in zero-shot motif scaffolding and RigidSSL-MD captures more biophysically realistic conformational ensembles in G protein-coupled receptor modeling.

</details>

---

### 79. [BInD: Bond and Interaction-generating Diffusion Model for Multi-objective Structure-based Drug Design](https://arxiv.org/abs/2405.16861)

**基本信息**

- 🔗 arXiv: [`2405.16861`](https://arxiv.org/abs/2405.16861)
- 👥 作者: Joongwon Lee, Wonho Zhung, Jisu Seo 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.16861.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发BInD模型，这是一个用于基于结构的药物设计的扩散模型。它属于利用生成式人工智能（化学大模型）进行分子设计与优化的典型研究。

**📖 中文摘要**

本文提出了BInD，一种基于知识引导的扩散模型，用于多目标基于结构的药物设计。BInD通过共同生成分子及其与靶标蛋白的相互作用，来平衡考虑关键目标，包括靶标特异性相互作用、分子性质和局部几何结构。综合评估表明，BInD在所有目标上均实现了稳健的性能，达到或超越了最先进的方法。此外，还提出了一种NCI驱动的分子设计和优化方法，通过阐述适当的相互作用模式来增强靶标结合和特异性。这项工作将扩散模型这一强大的生成框架应用于药物分子设计，是“化学大模型”在药物发现领域的直接应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent remarkable advancements in geometric deep generative models, coupled with accumulated structural data, enable structure-based drug design (SBDD) using only target protein information. However, existing models often struggle to balance multiple objectives, excelling only in specific tasks. BInD, a diffusion model with knowledge-based guidance, is introduced to address this limitation by co-generating molecules and their interactions with a target protein. This approach ensures balanced consideration of key objectives, including target-specific interactions, molecular properties, and local geometry. Comprehensive evaluations demonstrate that BInD achieves robust performance across all objectives, matching or surpassing state-of-the-art methods. Additionally, an NCI-driven molecule design and optimization method is proposed, enabling the enhancement of target binding and specificity by elaborating the adequate interaction patterns.

</details>

---

### 80. [Spectral/Spatial Tensor Atomic Cluster Expansion with Universal Embeddings in Cartesian Space](https://arxiv.org/abs/2509.14961)

**基本信息**

- 🔗 arXiv: [`2509.14961`](https://arxiv.org/abs/2509.14961)
- 👥 作者: Zemin Xu, Wenbo Xie, P. Hu
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.14961.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出TACE框架，这是一种用于开发机器学习原子间势的新方法。MLIPs作为“化学大模型”的一种，旨在以数据驱动的方式高精度模拟原子间相互作用，是计算化学和材料科学的基础工具。

**📖 中文摘要**

本文介绍了张量原子簇展开，它将标量和张量建模在笛卡尔空间和频域中统一起来，通过将局部环境分解为不可约笛卡尔张量，并利用原子簇扩展构建受控的多体层次结构。TACE提供了通用的不变和等变嵌入，并且可以平等地处理预测的张量可观测量，并在推理时实现显式控制。研究展示了其在有限分子和扩展材料上的准确性、稳定性和效率，包括域内和域外基准测试、光谱、Hessian、外场响应、带电系统以及多保真度/多头训练。TACE是构建下一代基础性机器学习原子间势的框架，这类模型是“化学大模型”在原子尺度模拟中的核心。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Equivariant atomistic machine learning models have largely been built on spherical-tensor representations, where explicit angular-momentum coupling introduces substantial complexity and systematic extensions beyond energies and forces remain challenging, often requires problem-specific architectural choices. Here we introduce the Tensor Atomic Cluster Expansion (TACE), which unifies scalar and tensorial modeling in Cartesian and space by decomposing local environments into irreducible Cartesian tensors (ICT) constructing a controlled many-body hierarchy with atomic cluster expansion (ACE). In addition to performing ACE in the frequency domain, we propose an efficient Clebsch-Gordan-free alternative in the spatial domain. TACE provides universal invariant (e.g., fidelity tags and charges) and equivariant (e.g., external electric fields and non-collinear magnetic moments) embeddings and predicted tensorial observables are handled on equal footing and enabling explicit control at inference. We demonstrate the accuracy, stability, and efficiency across finite molecules and extended materials, including in-domain and out-of-domain benchmarks, spectra, Hessian, external-field responses, charged systems, and multi-fidelity/head training. We further show its robustness on nonequilibrium/reactive datasets and controlled scaling when extending to large foundation model datasets.

</details>

---

### 81. [TCR-EML: Explainable Model Layers for TCR-pMHC Prediction](https://arxiv.org/abs/2510.04377)

**基本信息**

- 🔗 arXiv: [`2510.04377`](https://arxiv.org/abs/2510.04377)
- 👥 作者: Jiarui Li, Zixiang Yin, Zhengming Ding 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04377.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于TCR-pMHC结合预测的可解释深度学习模型（TCR-EML）。这属于利用人工智能模型（可视为特定领域的化学/生物大模型）预测生物分子间相互作用，是化学信息学和计算生物学的交叉研究。

**📖 中文摘要**

本文提出了TCR-EML，一种可解释的模型层，可用于TCR-pMHC结合预测。该方法使用原型层来表示已知TCR-pMHC结合机制中的氨基酸残基接触，从而为预测的TCR-pMHC结合提供高质量的解释。在大规模数据集上的实验表明，该方法具有竞争力的预测准确性和泛化能力，在TCR-XAI基准测试上的评估显示其可解释性优于现有方法。这项工作将“解释性设计”理念引入蛋白质相互作用预测模型，虽然主题更偏向生物信息学，但其构建可解释深度学习模型用于分子间相互作用预测的思路，与“化学大模型”中追求模型可解释性的方向相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

T cell receptor (TCR) recognition of peptide-MHC (pMHC) complexes is a central component of adaptive immunity, with implications for vaccine design, cancer immunotherapy, and autoimmune disease. While recent advances in machine learning have improved prediction of TCR-pMHC binding, the most effective approaches are black-box transformer models that cannot provide a rationale for predictions. Post-hoc explanation methods can provide insight with respect to the input but do not explicitly model biochemical mechanisms (e.g. known binding regions), as in TCR-pMHC binding. ``Explain-by-design'' models (i.e., with architectural components that can be examined directly after training) have been explored in other domains, but have not been used for TCR-pMHC binding. We propose explainable model layers (TCR-EML) that can be incorporated into protein-language model backbones for TCR-pMHC modeling. Our approach uses prototype layers for amino acid residue contacts drawn from known TCR-pMHC binding mechanisms, enabling high-quality explanations for predicted TCR-pMHC binding. Experiments of our proposed method on large-scale datasets demonstrate competitive predictive accuracy and generalization, and evaluation on the TCR-XAI benchmark demonstrates improved explainability compared with existing approaches.

</details>

---

### 82. [Validating Interpretability in siRNA Efficacy Prediction: A Perturbation-Based, Dataset-Aware Protocol](https://arxiv.org/abs/2602.10152)

**基本信息**

- 🔗 arXiv: [`2602.10152`](https://arxiv.org/abs/2602.10152)
- 👥 作者: Zahra Khodagholi, Niloofar Yousefi
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.10152.pdf)

**💡 相关性分析**

满足标准1：论文的研究场景是siRNA功效预测，这是利用机器学习模型（化学信息学模型）预测生物分子功能的一个具体应用。论文的核心贡献是为此类模型的可解释性提供验证协议，以确保其可靠地用于指导序列设计，这与“化学大模型”的负责任应用密切相关。

**📖 中文摘要**

本文针对siRNA功效预测中的可解释性验证提出了一个基于扰动的、数据集感知的协议。该协议作为一个预合成门控，通过反事实敏感性忠实度测试，来验证突变高显著性位置是否比组成匹配的对照组更能改变模型输出。跨数据集转移揭示了两种失败模式。研究还引入了一种生物学信息先验正则化器来增强显著性忠实度。这项工作虽然主要关注模型可解释性的验证方法，但其应用场景是siRNA（小干扰RNA）序列的功效预测，这本质上是利用机器学习模型（可视为一种化学/生物序列大模型）进行生物活性预测。论文提出的验证协议对于可靠地部署此类预测模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Saliency maps are increasingly used as design guidance in siRNA efficacy prediction, yet attribution methods are rarely validated before motivating sequence edits. We introduce a pre-synthesis gate: a protocol for counterfactual sensitivity faithfulness that tests whether mutating high-saliency positions changes model output more than composition-matched controls. Cross-dataset transfer reveals two failure modes that would otherwise go undetected: faithful-but-wrong (saliency valid, predictions fail) and inverted saliency (top-saliency edits less impactful than random). Strikingly, models trained on mRNA-level assays collapse on a luciferase reporter dataset, demonstrating that protocol shifts can silently invalidate deployment. Across four benchmarks, 19/20 fold instances pass; the single failure shows inverted saliency. A biology-informed regularizer (BioPrior) strengthens saliency faithfulness with modest, dataset-dependent predictive trade-offs. Our results establish saliency validation as essential pre-deployment practice for explanation-guided therapeutic design. Code is available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：20
- 累计论文数量：1419

## 📝 历史记录

> 暂无历史数据

