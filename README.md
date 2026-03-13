# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-13 01:21:24

## 📅 2026-03-13 (今日最新)

**相关论文数：53**

### 1. [A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)

**基本信息**

- 🔗 arXiv: [`2603.10090`](https://arxiv.org/abs/2603.10090)
- 👥 作者: Xiaolong Han, Zehong Wang, Bo Zhao 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10090.pdf)

**💡 相关性分析**

满足标准3：这是一篇关于权重空间学习的综述论文，它系统性地回顾和分类了如何理解、表示和生成神经网络权重空间。虽然标题未直接提及化学信息学或质谱，但其核心主题是‘模型权重空间的分析与建模’，这属于‘化学大模型’研究中的一个重要子方向（即模型的分析、表示和生成）。因此，它作为一篇重要的综述，与关注主题中的‘化学大模型’相关。

**📖 中文摘要**

这篇综述论文系统性地回顾和分类了权重空间学习这一新兴研究方向。它将权重空间学习分为三个核心维度：权重空间理解、权重空间表示和权重空间生成。该研究领域将神经网络的权重本身视为一个具有丰富结构、可以进行建模和分析的领域。论文讨论了如何通过分析预训练模型的权重分布、对称性，以及学习权重的嵌入表示，来促进模型分析、知识迁移和权重生成等应用。这项工作为理解和利用神经网络权重空间中的结构提供了一个统一的框架，对于构建更高效、可解释和可迁移的模型具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural network weights are typically viewed as the end product of training, while most deep learning research focuses on data, features, and architectures. However, recent advances show that the set of all possible weight values (weight space) itself contains rich structure: pretrained models form organized distributions, exhibit symmetries, and can be embedded, compared, or even generated. Understanding such structures has tremendous impact on how neural networks are analyzed and compared, and on how knowledge is transferred across models, beyond individual training instances. This emerging research direction, which we refer to as Weight Space Learning (WSL), treats neural weights as a meaningful domain for analysis and modeling. This survey provides the first unified taxonomy of WSL. We categorize existing methods into three core dimensions: Weight Space Understanding (WSU), which studies the geometry and symmetries of weights; Weight Space Representation (WSR), which learns embeddings over model weights; and Weight Space Generation (WSG), which synthesizes new weights through hypernetworks or generative models. We further show how these developments enable practical applications, including model retrieval, continual and federated learning, neural architecture search, and data-free reconstruction. By consolidating fragmented progress under a coherent framework, this survey highlights weight space as a learnable, structured domain with growing impact across model analysis, transferring, and weight generation. We release an accompanying resource at this https URL .

</details>

---

### 2. [Equivariant Asynchronous Diffusion: An Adaptive Denoising Schedule for Accelerated Molecular Conformation Generation](https://arxiv.org/abs/2603.10093)

**基本信息**

- 🔗 arXiv: [`2603.10093`](https://arxiv.org/abs/2603.10093)
- 👥 作者: Junyi An, Chao Qu, Yun-Fei Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10093.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于3D分子生成的新型扩散模型（EAD），这直接属于“化学大模型”的研究范畴。

**📖 中文摘要**

本文提出了一种名为等变异步扩散（EAD）的新型扩散模型，用于3D分子生成。该模型结合了异步自回归模型和同步扩散模型的优点，通过异步去噪计划更好地捕捉分子的层次结构，同时保持分子级的生成视野。研究引入了动态调度机制来自适应地确定去噪时间步。实验结果表明，EAD在3D分子生成任务上达到了最先进的性能。该工作直接围绕“化学大模型”主题，特别是用于分子生成的生成模型，属于核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent 3D molecular generation methods primarily use asynchronous auto-regressive or synchronous diffusion models. While auto-regressive models build molecules sequentially, they're limited by a short horizon and a discrepancy between training and inference. Conversely, synchronous diffusion models denoise all atoms at once, offering a molecule-level horizon but failing to capture the causal relationships inherent in hierarchical molecular structures. We introduce Equivariant Asynchronous Diffusion (EAD) to overcome these limitations. EAD is a novel diffusion model that combines the strengths of both approaches: it uses an asynchronous denoising schedule to better capture molecular hierarchy while maintaining a molecule-level horizon. Since these relationships are often complex, we propose a dynamic scheduling mechanism to adaptively determine the denoising timestep. Experimental results show that EAD achieves state-of-the-art performance in 3D molecular generation.

</details>

---

### 3. [Unbalanced Optimal Transport Dictionary Learning for Unsupervised Hyperspectral Image Clustering](https://arxiv.org/abs/2603.10132)

**基本信息**

- 🔗 arXiv: [`2603.10132`](https://arxiv.org/abs/2603.10132)
- 👥 作者: Joshua Lentz, Nicholas Karris, Alex Cloninger 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10132.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于非平衡Wasserstein重心的字典学习方法，用于高维光谱数据的降维和聚类。这种方法作为一种数据分析工具，可以潜在地应用于质谱等高维化学数据的处理和分析，为“质谱结构推理”等任务提供数据降维和特征学习资源。

**📖 中文摘要**

本文提出了一种利用非平衡Wasserstein重心进行字典学习的方法，用于高光谱图像的无监督聚类。该方法旨在学习高维光谱数据的低维表示，并通过在Wasserstein空间中学习字典来对数据进行分区。通过使用非平衡Wasserstein重心，该方法避免了平衡光谱分布的需要，从而提高了对异常值和噪声的鲁棒性。在学到的表示上应用谱聚类，实现了有效的无监督标签学习。该工作属于化学信息学中数据分析与降维的范畴，其提出的方法可用于处理类似质谱的高维光谱数据。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hyperspectral images capture vast amounts of high-dimensional spectral information about a scene, making labeling an intensive task that is resistant to out-of-the-box statistical methods. Unsupervised learning of clusters allows for automated segmentation of the scene, enabling a more rapid understanding of the image. Partitioning the spectral information contained within the data via dictionary learning in Wasserstein space has proven an effective method for unsupervised clustering. However, this approach requires balancing the spectral profiles of the data, blurring the classes, and sacrificing robustness to outliers and noise. In this paper, we suggest improving this approach by utilizing unbalanced Wasserstein barycenters to learn a lower-dimensional representation of the underlying data. The deployment of spectral clustering on the learned representation results in an effective approach for the unsupervised learning of labels.

</details>

---

### 4. [Performance Evaluation of Delay Tolerant Network Protocols to Improve Nepal Earthquake Rescue Communications](https://arxiv.org/abs/2603.10153)

**基本信息**

- 🔗 arXiv: [`2603.10153`](https://arxiv.org/abs/2603.10153)
- 👥 作者: Xiaofei Liu, Milena Radenkovic
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10153.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个统一的跨视图对比学习框架，用于整合全局和局部特征表示。这种多模态数据融合与对齐的方法论，可以作为工具或思路，应用于化学信息学领域，例如整合质谱数据与分子结构图数据进行联合表示学习，从而服务于“质谱结构推理”等任务。

**📖 中文摘要**

本文提出了一种名为联合成像-ROI表示学习的统一跨视图对比框架，用于脑部疾病分类。该方法同时学习受试者级别的全局（成像）和局部（ROI图）嵌入，并使用双向对比目标将它们对齐到一个共享的潜在空间中。这种对齐产生了可比较的嵌入，适用于下游融合，并允许在统一的训练协议下系统评估仅成像、仅ROI和联合配置。在ADHD-200和ABIDE数据集上的实验表明，联合学习始终优于任一单独分支。该工作属于生物医学数据分析，其提出的多模态数据融合与表示学习方法在方法论上与化学信息学中整合多种数据源（如质谱与结构信息）进行推理的思路相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In the fields of disaster rescue and communication in extreme environments, Delay Tolerant Network (DTN) has become an important technology due to its "store-carry-forward" mechanism. Selecting the appropriate routing strategy is of crucial significance for improving the success rate of distress message transmission and reducing delays in material dispatch. We design a pseudo realistic use case of Nepal Kathmandu earthquake rescue based on dynamically changing population distribution model and characteristics of rescue activities in the initial rescue efforts in Nepal Kathmandu earthquakes to conducted the multi criteria two benchmark routing protocols performance analysis in the face of different buffer sizes of the rescue team nodes. We identify multiple real world node groups, including affected residents, rescue teams, drones and ground vehicles and communication models are established according to the movement behaviors of these groups. We analyze the communication of distress messages between edge nodes to obtain performance metrics such as delivered probability, average delay, hop count, and buffer time. By analyzing the multi layer complex data and protocols differences, the research results show the effectiveness of distributed DTN communication methods in the Nepal earthquake rescue use case, reveal existence of trade-offs between transmission reliability and resource utilization of different routing protocols in disaster communication environment and provide a basis for the design of next-generation emergency communication services based on edge nodes.

</details>

---

### 5. [Discovery of a Hematopoietic Manifold in scGPT Yields a Method for Extracting Performant Algorithms from Biological Foundation Model Internals](https://arxiv.org/abs/2603.10261)

**基本信息**

- 🔗 arXiv: [`2603.10261`](https://arxiv.org/abs/2603.10261)
- 👥 作者: Ihor Kendiukhov
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10261.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究了从生物领域基础模型（scGPT）中提取可解释算法，这直接关联到“化学大模型”的可解释性与内部知识挖掘主题。2) 论文提出了一种从基础模型提取算法的通用方法，这作为一种工具或方法论，可以应用于化学领域的大模型（如用于分子表示或生成的模型），以提取用于下游任务（如性质预测或结构推理）的模型内部知识或子模块。

**📖 中文摘要**

本文报告了从单细胞基础模型scGPT中通过机制可解释性方法发现并提取出一个紧凑的造血算法。研究表明，scGPT内部编码了一个具有显著发育分支结构的紧凑造血流形。作者引入了一种通用的三阶段提取方法，包括从冻结的注意力权重中直接导出操作符、轻量级学习适配器和任务特定读出，从而在不进行目标数据集重新训练的情况下产生独立的算法。在多个基准测试中，提取出的算法在伪时间排序和关键亚型端点分类上表现优异。该工作展示了从基础模型中提取可解释、高性能生物算法的方法，属于生物信息学与基础模型可解释性交叉领域。其方法论对于理解化学领域的基础模型（如分子语言模型）内部工作机制，并从中提取有用知识或算法具有重要启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We report the discovery and extraction of a compact hematopoietic algorithm from the single-cell foundation model scGPT, to our knowledge the first biologically useful, competitive algorithm extracted from a foundation model via mechanistic interpretability. We show that scGPT internally encodes a compact hematopoietic manifold with significant developmental branch structure, validated on a strict non-overlap Tabula Sapiens external panel and confirmed via frozen-head zero-shot transfer to an independent multi-donor immune panel. To isolate this geometry, we introduce a general three-stage extraction method consisting of direct operator export from frozen attention weights, a lightweight learned adaptor, and a task-specific readout, producing a standalone algorithm without target-dataset retraining. In 88-split donor-holdout benchmarks against scVI, Palantir, DPT, CellTypist, PCA, and raw-expression baselines, the extracted algorithm achieves the strongest pseudotime-depth ordering and leads on key subtype endpoints (CD4/CD8 AUROC 0.867, mono/macro AUROC 0.951). Compared to standard probing of frozen scGPT embeddings with a 3-layer MLP, the extracted head is BH-significantly better on 6/8 classification endpoints while completing a full 12-split evaluation campaign 34.5x faster with approximately 1000x fewer trainable parameters. The exported operator compresses from three pooled attention heads to a single head without statistically significant loss, and further to a rank-64 surrogate. Mechanistic interpretability of the compact operator reveals a concentrated four-factor core explaining 66.2% of ablation impact, with factors resolving into explicit T/lymphoid, B/plasma, granulocytic, and monocyte/macrophage gene programs. A supplementary second-manifold validation (intercellular communication geometry) confirms that the extraction method generalizes beyond hematopoiesis.

</details>

---

### 6. [How to make the most of your masked language model for protein engineering](https://arxiv.org/abs/2603.10302)

**基本信息**

- 🔗 arXiv: [`2603.10302`](https://arxiv.org/abs/2603.10302)
- 👥 作者: Calvin McCarter, Nick Bhattacharya, Sebastian W. Ober 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10302.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何优化从蛋白质掩码语言模型（MLM）中采样的策略，以更好地优化所需的生物特性（如抗体结合力）。这直接围绕“化学大模型”（此处特指蛋白质语言模型）的应用主题展开。

**📖 中文摘要**

本文针对蛋白质工程中的采样问题，提出了一种灵活有效的从掩码语言模型（MLM）中采样的方法。作者提出了使用随机波束搜索进行采样，利用了MLM在评估序列的整个1-编辑邻域的伪困惑度方面非常高效的特点。将生成重新定义为对整个序列的评估，使得能够灵活地指导多个优化目标。此外，论文报告了在抗体工程设置中进行的广泛体外头对头评估结果，表明采样方法的选择至少与所使用的模型一样重要。该工作直接面向蛋白质语言模型的应用，属于“化学大模型”在生物分子（蛋白质）工程领域的核心应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A plethora of protein language models have been released in recent years. Yet comparatively little work has addressed how to best sample from them to optimize desired biological properties. We fill this gap by proposing a flexible, effective sampling method for masked language models (MLMs), and by systematically evaluating models and methods both in silico and in vitro on actual antibody therapeutics campaigns. Firstly, we propose sampling with stochastic beam search, exploiting the fact that MLMs are remarkably efficient at evaluating the pseudo-perplexity of the entire 1-edit neighborhood of a sequence. Reframing generation in terms of entire-sequence evaluation enables flexible guidance with multiple optimization objectives. Secondly, we report results from our extensive in vitro head-to-head evaluation for the antibody engineering setting. This reveals that choice of sampling method is at least as impactful as the model used, motivating future research into this under-explored area.

</details>

---

### 7. [Spatial self-supervised Peak Learning and correlation-based Evaluation of peak picking in Mass Spectrometry Imaging](https://arxiv.org/abs/2603.10487)

**基本信息**

- 🔗 arXiv: [`2603.10487`](https://arxiv.org/abs/2603.10487)
- 👥 作者: Philipp Weigand, Nikolas Ebert, Shad A. Mohammed 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10487.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕质谱成像（MSI）数据的分析，特别是峰值挑选这一关键步骤，这是质谱结构推理的核心任务之一。论文提出的自监督学习网络旨在从复杂的质谱数据中识别有意义的峰值，直接服务于从质谱数据中推断分子结构或分布这一目标。

**📖 中文摘要**

本文提出了一种用于质谱成像（MSI）数据峰值挑选的新方法。MSI生成复杂的高维数据，有效的峰值挑选对于减少数据量同时保留有意义的生物信息至关重要。现有方法在不同数据集上表现不一致，且评估通常局限于合成数据或手动选择的离子图像，不能完全代表MSI中的真实挑战。为解决这些限制，作者提出了一种基于自动编码器的空间自监督峰值学习神经网络，该网络通过利用空间和光谱信息学习注意力掩码来选择具有空间结构的峰值。此外，引入了一种基于专家标注分割掩码的评估程序，允许对峰值挑选性能进行更具代表性和空间基础的评估。在四个不同的公共MSI数据集上，该方法通过选择空间结构化的峰值，性能优于最先进的峰值挑选方法。这项工作突出了在质谱数据分析中利用空间自监督学习进行结构推理的价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mass spectrometry imaging (MSI) enables label-free visualization of molecular distributions across tissue samples but generates large and complex datasets that require effective peak picking to reduce data size while preserving meaningful biological information. Existing peak picking approaches perform inconsistently across heterogeneous datasets, and their evaluation is often limited to synthetic data or manually selected ion images that do not fully represent real-world challenges in MSI. To address these limitations, we propose an autoencoder-based spatial self-supervised peak learning neural network that selects spatially structured peaks by learning an attention mask leveraging both spatial and spectral information. We further introduce an evaluation procedure based on expert-annotated segmentation masks, allowing a more representative and spatially grounded assessment of peak picking performance. We evaluate our approach on four diverse public MSI datasets using our proposed evaluation procedure. Our approach consistently outperforms state-of-the-art peak picking methods by selecting spatially structured peaks, thus demonstrating its efficacy. These results highlight the value of our spatial self-supervised network in comparison to contemporary state-of-the-art methods. The evaluation procedure can be readily applied to new MSI datasets, thereby providing a consistent and robust framework for the comparison of spatially structured peak picking methods across different datasets.

</details>

---

### 8. [SCORE: Replacing Layer Stacking with Contractive Recurrent Depth](https://arxiv.org/abs/2603.10544)

**基本信息**

- 🔗 arXiv: [`2603.10544`](https://arxiv.org/abs/2603.10544)
- 👥 作者: Guillaume Godin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10544.pdf)

**💡 相关性分析**

满足标准2：论文提出的SCORE架构在图神经网络（GNN）上的应用案例是ESOL分子溶解度预测，这是一个经典的化学信息学任务。虽然论文主要贡献是通用神经网络架构，但其在化学信息学基准任务上的成功验证，使其成为可用于构建或改进化学大模型（特别是基于GNN的模型）的一种方法资源。

**📖 中文摘要**

本文提出了一种名为SCORE（Skip-Connection ODE Recurrent Embedding）的离散循环架构，作为传统层堆叠的替代方案。SCORE通过ODE启发的收缩更新迭代应用单个共享神经块，可以解释为一种深度迭代细化过程。该研究在图神经网络（用于ESOL分子溶解度预测）、多层感知机和基于Transformer的语言模型（nanoGPT）上进行了评估。论文的核心贡献在于提出了一种轻量级且有效的深度神经网络架构替代方案。虽然论文本身并非直接研究化学大模型或质谱结构推理，但其在ESOL分子溶解度预测任务上的应用，展示了所提方法在化学信息学（一个与化学大模型紧密相关的领域）中的潜在适用性。因此，它提供了可用于这些主题的模型架构或方法资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Residual connections are central to modern deep neural networks, enabling stable optimization and efficient information flow across depth. In this work, we propose SCORE (Skip-Connection ODE Recurrent Embedding), a discrete recurrent alternative to classical layer stacking. Instead of composing multiple independent layers, SCORE iteratively applies a single shared neural block using an ODE (Ordinary Differential Equation)-inspired contractive update: ht+1 = (1 - dt) * ht + dt * F(ht) This formulation can be interpreted as a depth-by-iteration refinement process, where the step size dt explicitly controls stability and update magnitude. Unlike continuous Neural ODE approaches, SCORE uses a fixed number of discrete iterations and standard backpropagation without requiring ODE solvers or adjoint methods. We evaluate SCORE across graph neural networks (ESOL molecular solubility), multilayer perceptrons, and Transformer-based language models (nanoGPT). Across architectures, SCORE generally improves convergence speed and often accelerates training. SCORE is reducing parameter count through shared weights. In practice, simple Euler integration provides the best trade-off between computational cost and performance, while higher-order integrators yield marginal gains at increased compute. These results suggest that controlled recurrent depth with contractive residual updates offers a lightweight and effective alternative to classical stacking in deep neural networks.

</details>

---

### 9. [Gradient Flow Drifting: Generative Modeling via Wasserstein Gradient Flows of KDE-Approximated Divergences](https://arxiv.org/abs/2603.10592)

**基本信息**

- 🔗 arXiv: [`2603.10592`](https://arxiv.org/abs/2603.10592)
- 👥 作者: Jiarui Cao, Zixuan Wei, Yuxin Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10592.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是生成模型的新理论框架，该框架通过将漂移模型与Wasserstein梯度流和KDE近似联系起来，为生成建模提供了新的数学视角。生成模型是构建化学大模型（如用于分子生成或性质预测的模型）的核心技术之一。因此，这篇论文直接围绕构建大模型所需的基础生成建模理论展开，与“化学大模型”主题高度相关。

**📖 中文摘要**

本文提出了一个名为梯度流漂移（Gradient Flow Drifting）的生成模型新家族的理论框架。作者证明，最近提出的漂移模型（Drifting Model）在核密度估计（KDE）近似下，等价于前向KL散度的Wasserstein梯度流。具体而言，漂移模型的漂移场等于KDE对数密度梯度之差（∇ log p_kde - ∇ log q_kde）乘以一个带宽平方的缩放因子。该框架还将MMD-based生成器作为KDE近似下不同散度的Wasserstein梯度流的特例包含在内。论文提供了简明的可识别性证明和理论基础的混合散度策略，并结合反向KL和χ²散度梯度流来同时避免模式崩溃和模式模糊。该方法还被扩展到黎曼流形上。初步实验在合成基准上验证了该框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We reveal a precise mathematical framework about a new family of generative models which we call Gradient Flow Drifting. With this framework, we prove an equivalence between the recently proposed Drifting Model and the Wasserstein gradient flow of the forward KL divergence under kernel density estimation (KDE) approximation. Specifically, we prove that the drifting field of drifting model ( arXiv:2602.04770 ) equals, up to a bandwidth-squared scaling factor, the difference of KDE log-density gradients $\nabla \log p_{\mathrm{kde}} - \nabla \log q_{\mathrm{kde}}$, which is exactly the particle velocity field of the Wasserstein-2 gradient flow of $KL(q\|p)$ with KDE-approximated densities. Besides that, this broad family of generative models can also include MMD-based generators, which arises as special cases of Wasserstein gradient flows of different divergences under KDE approximation. We provide a concise identifiability proof, and a theoretically grounded mixed-divergence strategy. We combine reverse KL and $\chi^2$ divergence gradient flows to simultaneously avoid mode collapse and mode blurring, and extend this method onto Riemannian manifold which loosens the constraints on the kernel function, and makes this method more suitable for the semantic space. Preliminary experiments on synthetic benchmarks validate the framework.

</details>

---

### 10. [Disentangling Similarity and Relatedness in Topic Models](https://arxiv.org/abs/2603.10619)

**基本信息**

- 🔗 arXiv: [`2603.10619`](https://arxiv.org/abs/2603.10619)
- 👥 作者: Hanlin Xiao, Mauricio A. Álvarez, Rainer Breitling
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10619.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索集成预训练语言模型（PLM）嵌入的主题模型。PLM是构建大语言模型（LLM）的基础，而将LLM/PLM的语义先验与特定领域（如化学）的主题建模相结合，是构建领域大模型（如化学大模型）的一种重要途径。论文对PLM增强主题模型的深入分析，直接围绕如何利用大模型技术改进语义表示这一核心主题。

**📖 中文摘要**

本文研究了如何将预训练语言模型（PLM）嵌入集成到主题模型中，这从根本上改变了主题捕获语义结构的方式。经典模型（如LDA）从词共现统计中推导主题，而PLM增强模型将这些统计锚定到预训练的嵌入空间中，施加了一个同样有利于语义相似词聚类的先验。这种结构差异可以通过主题词的主题相关性和分类相似性这两个心理语言学维度来捕捉。为了在主题模型中解耦这些维度，作者使用基于LLM的标注构建了一个大型合成词对基准，并训练了一个神经评分函数。该评分器被应用于跨多个语料库和主题模型家族的全面评估，揭示了不同模型家族在其主题中捕获了不同的语义结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The recent advancement of large language models has spurred a growing trend of integrating pre-trained language model (PLM) embeddings into topic models, fundamentally reshaping how topics capture semantic structure. Classical models such as Latent Dirichlet Allocation (LDA) derive topics from word co-occurrence statistics, whereas PLM-augmented models anchor these statistics to pre-trained embedding spaces, imposing a prior that also favours clustering of semantically similar words. This structural difference can be captured by the psycholinguistic dimensions of thematic relatedness and taxonomic similarity of the topic words. To disentangle these dimensions in topic models, we construct a large synthetic benchmark of word pairs using LLM-based annotation to train a neural scoring function. We apply this scorer to a comprehensive evaluation across multiple corpora and topic model families, revealing that different model families capture distinct semantic structure in their topics. We further demonstrate that similarity and relatedness scores successfully predict downstream task performance depending on task requirements. This paper establishes similarity and relatedness as essential axes for topic model evaluation and provides a reliable pipeline for characterising these across model families and corpora.

</details>

---

### 11. [Surrogate models for nuclear fusion with parametric Shallow Recurrent Decoder Networks: applications to magnetohydrodynamics](https://arxiv.org/abs/2603.10678)

**基本信息**

- 🔗 arXiv: [`2603.10678`](https://arxiv.org/abs/2603.10678)
- 👥 作者: M. Lo Verso, C. Introini, E. Cervi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10678.pdf)

**💡 相关性分析**

满足标准2：论文提出并验证了SHRED作为一种用于复杂物理系统（磁流体动力学）的、计算高效的代理建模（即替代模型）策略。代理模型或替代模型是科学机器学习（SciML）的核心，而构建复杂化学或物理过程（如质谱解析背后的分子碎裂动力学）的准确、高效的代理模型，是“化学大模型”和“质谱结构推理”领域的关键需求。因此，该论文提供的方法资源与这些主题高度相关。

**📖 中文摘要**

本文针对核聚变应用中的磁流体动力学（MHD）问题，研究了一种完全数据驱动的状态重构框架。该框架结合了通过奇异值分解（SVD）进行的降维和浅层循环解码器（SHRED）神经网络架构。SHRED旨在从有限数量观测值的稀疏时间序列测量中恢复完整的时空状态。该方法应用于一个参数化MHD测试案例，涉及在阶梯通道中受热梯度和宽范围强度磁场作用的可压缩铅锂流。仅使用三个传感器的温度测量作为输入，网络即可重建速度、压力和温度的完整场。结果表明，即使对于训练集中未包含的磁场强度，SHRED也能准确重建完整的MHD状态。这些发现证明了SHRED作为聚变相关多物理问题计算高效代理建模策略的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Magnetohydrodynamic (MHD) effects play a key role in the design and operation of nuclear fusion systems, where electrically conducting fluids (such as liquid metals or molten salts in reactor blankets) interact with magnetic fields of varying intensity and orientation, which affect the resulting flow. The numerical resolution of MHD models involves highly nonlinear multiphysics systems of equations and can become computationally expensive, particularly in multi-query, parametric, or real-time contexts. This work investigates a fully data-driven framework for MHD state reconstruction that combines dimensionality reduction via Singular Value Decomposition (SVD) with the SHallow REcurrent Decoder (SHRED), a neural network architecture designed to recover the full spatio-temporal state from sparse time-series measurements of a limited number of observables. The methodology is applied to a parametric MHD test case involving compressible lead-lithium flow in a stepped channel subjected to thermal gradients and magnetic fields spanning a broad range of intensities. To improve efficiency, the full-order dataset is first compressed using SVD, yielding a reduced representation used as reference truth for training. Only temperature measurements from three sensors are provided as input, while the network reconstructs the full fields of velocity, pressure, and temperature. To assess robustness with respect to sensor placement, thirty randomly generated sensor configurations are tested in ensemble mode. Results show that SHRED accurately reconstructs the full MHD state even for magnetic field intensities not included in the training set. These findings demonstrate the potential of SHRED as a computationally efficient surrogate modeling strategy for fusion-relevant multiphysics problems, enabling low-cost state estimation with possible applications in real-time monitoring and control.

</details>

---

### 12. [eLasmobranc Dataset: An Image Dataset for Elasmobranch Species Recognition and Biodiversity Monitoring](https://arxiv.org/abs/2603.10724)

**基本信息**

- 🔗 arXiv: [`2603.10724`](https://arxiv.org/abs/2603.10724)
- 👥 作者: Ismael Beviá-Ballesteros, Mario Jerez-Tallón, Nieves Aranda-Garrido 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10724.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是创建并发布了一个新的、公开可用的、用于细粒度物种识别的图像数据集。虽然领域不同（海洋生物学），但其在构建高质量、专家标注、具有明确任务目标（细粒度分类）的数据集方面的实践，为“化学大模型”和“质谱结构推理”领域提供了宝贵的范例。这些领域同样急需高质量、标准化的数据集（如质谱-结构配对数据集、分子属性数据集）来训练和评估模型。因此，该论文在数据资源构建的方法论上具有相关性。

**📖 中文摘要**

本文介绍了eLasmobranc数据集，一个用于七种生态相关板鳃亚纲物种识别和生物多样性监测的、经过整理且公开可用的图像集合。该数据集主要包含在标准化协议下于水环境外获取的图像，以确保诊断性形态特征的清晰可视化。它集成了专家验证的物种标注、结构化的时空元数据以及补充的物种级信息。eLasmobranc数据集专门设计用于支持有监督的物种级分类、种群研究以及用于生物多样性监测的人工智能系统开发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Elasmobranch populations are experiencing significant global declines, and several species are currently classified as threatened. Reliable monitoring and species-level identification are essential to support conservation and spatial planning initiatives such as Important Shark and Ray Areas (ISRAs). However, existing visual datasets are predominantly detection-oriented, underwater-acquired, or limited to coarse-grained categories, restricting their applicability to fine-grained morphological classification. We present the eLasmobranc Dataset, a curated and publicly available image collection from seven ecologically relevant elasmobranch species inhabiting the eastern Spanish Mediterranean coast, a region where two ISRAs have been identified. Images were obtained through dedicated data collection, including field campaigns and collaborations with local fish markets and projects, as well as from open-access public sources. The dataset was constructed predominantly from images acquired outside the aquatic environment under standardized protocols to ensure clear visualization of diagnostic morphological traits. It integrates expert-validated species annotations, structured spatial and temporal metadata, and complementary species-level information. The eLasmobranc Dataset is specifically designed to support supervised species-level classification, population studies, and the development of artificial intelligence systems for biodiversity monitoring. By combining morphological clarity, taxonomic reliability, and public accessibility, the dataset addresses a critical gap in fine-grained elasmobranch identification and promotes reproducible research in conservation-oriented computer vision. The dataset is publicly available at this https URL .

</details>

---

### 13. [A Grammar of Machine Learning Workflows](https://arxiv.org/abs/2603.10742)

**基本信息**

- 🔗 arXiv: [`2603.10742`](https://arxiv.org/abs/2603.10742)
- 👥 作者: Simon Roth
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10742.pdf)

**💡 相关性分析**

满足标准3：论文提出了一个通用的机器学习工作流语法和约束框架，这对于构建和验证可靠的化学大模型（如用于质谱分析的模型）具有重要的方法论指导意义，属于相关的重要讨论。

**📖 中文摘要**

本文提出了一种用于监督学习工作流的结构化语法，旨在通过运行时强制执行的约束来防止数据泄漏等常见错误。该语法将学习生命周期分解为7个核心原语，并通过一个有向无环图连接。其核心贡献是“终端评估约束”，它在运行时强制执行一个评估/评估边界，防止对测试集的重复评估。虽然论文主要关注机器学习工作流的通用问题，但其提出的结构化框架和防止数据泄漏的机制，对于构建和验证用于化学信息学（如质谱数据分析）的机器学习模型具有重要的方法论意义。它为解决模型开发中的可靠性问题提供了系统性的工具，这与构建稳健的化学大模型和质谱结构推理工具的需求直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Data leakage affected 294 published papers across 17 scientific fields (Kapoor & Narayanan, 2023). The dominant response has been documentation: checklists, linters, best-practice guides. Documentation does not prevent these failures. This paper proposes a structural remedy: a grammar that decomposes the supervised learning lifecycle into 7 kernel primitives connected by a typed directed acyclic graph (DAG), with four hard constraints that reject the two most damaging leakage classes at call time. The grammar's core contribution is the terminal assess constraint: a runtime-enforced evaluate/assess boundary where repeated test-set assessment is rejected by a guard on a nominally distinct Evidence type. A companion study across 2,047 experimental instances quantifies why this matters: selection leakage inflates performance by d_z = 0.93 and memorization leakage by d_z = 0.53-1.11. Three separate implementations (Python, R, and Julia) confirm the claims. The appendix specification lets anyone build a conforming version.

</details>

---

### 14. [CUPID: A Plug-in Framework for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single Model](https://arxiv.org/abs/2603.10745)

**基本信息**

- 🔗 arXiv: [`2603.10745`](https://arxiv.org/abs/2603.10745)
- 👥 作者: Xinran Xu, Xiuyi Fan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10745.pdf)

**💡 相关性分析**

满足标准2：CUPID框架作为一个通用的不确定性估计工具，可以应用于化学信息学和质谱分析中的模型（例如，用于预测分子性质或解析质谱图的模型），以提供可靠的置信度估计，这对于高风险的科研和决策场景至关重要。

**📖 中文摘要**

本文提出了CUPID，一个用于联合估计偶然不确定性和认知不确定性的即插即用框架。CUPID可以灵活地插入任何预训练网络的层中，无需修改或重新训练基础模型。它通过学习贝叶斯恒等映射来建模偶然不确定性，并通过分析模型对结构化扰动的内部响应来捕获认知不确定性。论文在分类、回归和分布外检测等任务上进行了评估。该框架旨在使不确定性估计变得模块化、可解释且与模型无关，从而支持更透明和可信的AI系统。相关代码和数据已公开。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate estimation of uncertainty in deep learning is critical for deploying models in high-stakes domains such as medical diagnosis and autonomous decision-making, where overconfident predictions can lead to harmful outcomes. In practice, understanding the reason behind a model's uncertainty and the type of uncertainty it represents can support risk-aware decisions, enhance user trust, and guide additional data collection. However, many existing methods only address a single type of uncertainty or require modifications and retraining of the base model, making them difficult to adopt in real-world systems. We introduce CUPID (Comprehensive Uncertainty Plug-in estImation moDel), a general-purpose module that jointly estimates aleatoric and epistemic uncertainty without modifying or retraining the base model. CUPID can be flexibly inserted into any layer of a pretrained network. It models aleatoric uncertainty through a learned Bayesian identity mapping and captures epistemic uncertainty by analyzing the model's internal responses to structured perturbations. We evaluate CUPID across a range of tasks, including classification, regression, and out-of-distribution detection. The results show that it consistently delivers competitive performance while offering layer-wise insights into the origins of uncertainty. By making uncertainty estimation modular, interpretable, and model-agnostic, CUPID supports more transparent and trustworthy AI. Related code and data are available at this https URL .

</details>

---

### 15. [A PUF-Based Approach for Copy Protection of Intellectual Property in Neural Network Models](https://arxiv.org/abs/2603.10753)

**基本信息**

- 🔗 arXiv: [`2603.10753`](https://arxiv.org/abs/2603.10753)
- 👥 作者: Daniel Dorfmeister, Flavio Ferrarotti, Bernhard Fischer 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10753.pdf)

**💡 相关性分析**

满足标准3：论文讨论了保护包含知识产权的神经网络模型（如化学大模型）的技术。虽然不直接研究化学大模型本身，但其关于模型安全性和知识产权保护的讨论，对于部署和商业化化学信息学领域的专有模型具有重要的相关性和前瞻性。

**📖 中文摘要**

本文提出了一种基于物理不可克隆函数（PUF）的方法，用于保护神经网络模型中的知识产权。该方法将神经网络模型的关键权重与底层硬件的独特、不可克隆的属性绑定。通过这种方式，只有在目标硬件上才能恢复原始权重并达到足够的精度，从而使得在克隆硬件上正确执行神经网络模型变得不可能。作者在多种神经网络模型上证明了该方法可以实现期望的精度退化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

More and more companies' Intellectual Property (IP) is being integrated into Neural Network (NN) models. This IP has considerable value for companies and, therefore, requires adequate protection. For example, an attacker might replicate a production machines' hardware and subsequently simply copy associated software and NN models onto the cloned hardware. To make copying NN models onto cloned hardware infeasible, we present an approach to bind NN models - and thus also the IP contained within them - to their underlying hardware. For this purpose, we link an NN model's weights, which are crucial for its operation, to unique and unclonable hardware properties by leveraging Physically Unclonable Functions (PUFs). By doing so, sufficient accuracy can only be achieved using the target hardware to restore the original weights, rendering proper execution of the NN model on cloned hardware impossible. We demonstrate that our approach accomplishes the desired degradation of accuracy on various NN models and outline possible future improvements.

</details>

---

### 16. [CodePercept: Code-Grounded Visual STEM Perception for MLLMs](https://arxiv.org/abs/2603.10757)

**基本信息**

- 🔗 arXiv: [`2603.10757`](https://arxiv.org/abs/2603.10757)
- 👥 作者: Tongkun Guan, Zhibo Yang, Jianqiang Wan 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10757.pdf)

**💡 相关性分析**

满足标准2：论文构建了大规模图像-代码数据集ICC-1M和评估基准STEM2Code-Eval。这些资源对于开发能够理解和推理科学图表（可能包括化学结构式、质谱图等）的“化学大模型”具有潜在价值，为模型提供了结构化的训练和评估数据。

**📖 中文摘要**

本文研究了多模态大语言模型（MLLMs）在STEM视觉推理中的瓶颈。通过系统性的缩放分析，作者发现感知能力（而非推理能力）是当前限制STEM视觉推理的真正杠杆。基于此洞察，作者提出将代码确立为强大的感知媒介，因为可执行代码的精确语义与STEM视觉的结构化性质自然对齐。为此，他们构建了ICC-1M大规模数据集，包含100万个图像-描述-代码三元组，通过两种互补的方法实现“代码作为感知”的范式。此外，还引入了STEM2Code-Eval基准，通过图像重建的可执行代码生成来直接评估视觉感知。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

When MLLMs fail at Science, Technology, Engineering, and Mathematics (STEM) visual reasoning, a fundamental question arises: is it due to perceptual deficiencies or reasoning limitations? Through systematic scaling analysis that independently scales perception and reasoning components, we uncover a critical insight: scaling perception consistently outperforms scaling reasoning. This reveals perception as the true lever limiting current STEM visual reasoning. Motivated by this insight, our work focuses on systematically enhancing the perception capabilities of MLLMs by establishing code as a powerful perceptual medium--executable code provides precise semantics that naturally align with the structured nature of STEM visuals. Specifically, we construct ICC-1M, a large-scale dataset comprising 1M Image-Caption-Code triplets that materializes this code-as-perception paradigm through two complementary approaches: (1) Code-Grounded Caption Generation treats executable code as ground truth for image captions, eliminating the hallucinations inherent in existing knowledge distillation methods; (2) STEM Image-to-Code Translation prompts models to generate reconstruction code, mitigating the ambiguity of natural language for perception enhancement. To validate this paradigm, we further introduce STEM2Code-Eval, a novel benchmark that directly evaluates visual perception in STEM domains. Unlike existing work relying on problem-solving accuracy as a proxy that only measures problem-relevant understanding, our benchmark requires comprehensive visual comprehension through executable code generation for image reconstruction, providing deterministic and verifiable assessment. Code is available at this https URL .

</details>

---

### 17. [mAceReason-Math: A Dataset of High-Quality Multilingual Math Problems Ready For RLVR](https://arxiv.org/abs/2603.10767)

**基本信息**

- 🔗 arXiv: [`2603.10767`](https://arxiv.org/abs/2603.10767)
- 👥 作者: Konstantin Dobler, Simon Lehnerer, Federico Scozzafava 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10767.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门为强化学习与可验证奖励（RLVR）设计的高质量多语言数学问题数据集。RLVR是提升大模型（包括潜在的化学推理大模型）在数学和逻辑问题领域能力的关键技术之一。该数据集可作为训练或评估具有复杂推理能力的化学信息学模型的宝贵资源。

**📖 中文摘要**

本文发布了mAceReason-Math数据集，这是一个高质量的多语言数学问题数据集，专为强化学习与可验证奖励（RLVR）研究设计。该数据集源自专门为RLVR策划的英文语料库（AceReason-Math），并进行了高质量的翻译和清理，覆盖14种语言，每种语言包含超过10,000个样本。这些数学问题具有挑战性，能为当前模型提供适当的训练信号。该数据集的发布旨在促进多语言RLVR的研究和基准测试。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has been successfully applied to significantly boost the capabilities of pretrained large language models, especially in the math and logic problem domains. However, current research and available training datasets remain English-centric. While mul- tilingual training data and benchmarks have been created in the past, they were not created with RLVR and current model capability in mind, and their level of difficulty is often too low to provide appropriate training signals for current models. To address this gap, we provide mAceReason-Math, a dataset of high-quality translations of challenging math problems sourced from a corpus specifically curated for RLVR (AceReason-Math). We further take specific care to clean and improve our translations, resulting in a coverage of 14 languages with more than 10,000 samples per language. We release the dataset to facilitate multilingual RLVR research and benchmarking in the research community.

</details>

---

### 18. [Word Recovery in Large Language Models Enables Character-Level Tokenization Robustness](https://arxiv.org/abs/2603.10771)

**基本信息**

- 🔗 arXiv: [`2603.10771`](https://arxiv.org/abs/2603.10771)
- 👥 作者: Zhipeng Yang, Shu Yang, Lijie Hu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10771.pdf)

**💡 相关性分析**

满足标准3：论文深入研究了大型语言模型内部处理非标准输入的工作机制。这对于理解“化学大模型”如何处理化学命名法（可能包含非常规字符组合）或质谱数据编码等任务具有重要的基础性启示，属于对模型底层能力的重要相关讨论。

**📖 中文摘要**

本文通过机械可解释性研究了大型语言模型对非规范输入（如字符级分词）表现出鲁棒性的机制。作者识别了一个核心过程，称为“词恢复”，即隐藏状态从字符级输入中重建规范词级token的身份。他们提供了因果证据，并进行了细粒度的注意力分析，表明属于同一规范token的字符之间的组内注意力对于词恢复至关重要。这些发现为分词鲁棒性提供了一种机制性解释，并确定了词恢复是使LLM能够处理字符级输入的关键机制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) trained with canonical tokenization exhibit surprising robustness to non-canonical inputs such as character-level tokenization, yet the mechanisms underlying this robustness remain unclear. We study this phenomenon through mechanistic interpretability and identify a core process we term word recovery. We first introduce a decoding-based method to detect word recovery, showing that hidden states reconstruct canonical word-level token identities from character-level inputs. We then provide causal evidence by removing the corresponding subspace from hidden states, which consistently degrades downstream task performance. Finally, we conduct a fine-grained attention analysis and show that in-group attention among characters belonging to the same canonical token is critical for word recovery: masking such attention in early layers substantially reduces both recovery scores and task performance. Together, our findings provide a mechanistic explanation for tokenization robustness and identify word recovery as a key mechanism enabling LLMs to process character-level inputs.

</details>

---

### 19. [Multilingual Reasoning Gym: Multilingual Scaling of Procedural Reasoning Environments](https://arxiv.org/abs/2603.10793)

**基本信息**

- 🔗 arXiv: [`2603.10793`](https://arxiv.org/abs/2603.10793)
- 👥 作者: Konstantin Dobler, Simon Lehnerer, Federico Scozzafava 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10793.pdf)

**💡 相关性分析**

满足标准2：论文发布了一个多语言、程序化生成的推理问题数据集和框架。这为开发和评估具有复杂推理能力的多语言大模型（包括可能应用于化学信息学的模型）提供了重要的数据资源和测试平台。

**📖 中文摘要**

本文介绍了多语言推理健身房（Multilingual Reasoning Gym），它是推理健身房（Reasoning Gym）的扩展，能够程序化地生成覆盖14种语言的可验证推理问题。它翻译了94个任务的模板，并进行了母语者验证和代码/模板适配，以确保语言自然性。该资源保留了程序化生成方法的核心优势，并可直接用于强化学习与可验证奖励（RLVR）和评估设置。由于问题的程序化生成性质，该健身房支持大规模、跨语言并行的数据生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present the Multilingual Reasoning Gym, an extension of Reasoning Gym (Stojanovski et al., 2025), that procedurally generates verifiable reasoning problems across 14 languages. We translate templates for 94 tasks with native-speaker validation in 10 languages and targeted code or template adaptations to ensure linguistic naturalness. The Multilingual Reasoning Gym preserves the core benefits of the procedural generation approach used in the original Reasoning Gym, such as virtually unlimited problem instance generation and adjustable difficulty, and remains directly usable for Reinforcement Learning from Verifiable Rewards and evaluation settings. Problems in the Multilingual Reasoning Gym are parallel across languages, enabling crosslingually parallel data generation at massive scale due to the procedural nature of the environments. We release our implementation to support research into multilingual reasoning models.

</details>

---

### 20. [Protein Counterfactuals via Diffusion-Guided Latent Optimization](https://arxiv.org/abs/2603.10811)

**基本信息**

- 🔗 arXiv: [`2603.10811`](https://arxiv.org/abs/2603.10811)
- 👥 作者: Weronika Kłos, Sidney Bender, Lukas Kades
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10811.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散模型等生成式AI技术进行蛋白质序列的反事实生成和设计。这直接属于“化学大模型”在生物分子设计领域的应用，是化学信息学与AI交叉的前沿方向。

**📖 中文摘要**

本文提出了MCCOP框架，用于为蛋白质生成最小的、生物学上合理的序列编辑（反事实），以将模型的预测翻转到期望的目标状态。MCCOP在连续的序列-结构联合潜在空间中操作，并使用预训练的扩散模型作为流形先验，平衡三个目标：有效性（达到目标属性）、邻近性（最小化突变）和合理性（产生可折叠的蛋白质）。作者在三个蛋白质工程任务上评估了MCCOP，并表明其生成的对抗事实比离散和连续基线更稀疏、更合理。恢复的突变与已知的生物物理机制一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning models can predict protein properties with unprecedented accuracy but rarely offer mechanistic insight or actionable guidance for engineering improved variants. When a model flags an antibody as unstable, the protein engineer is left without recourse: which mutations would rescue stability while preserving function? We introduce Manifold-Constrained Counterfactual Optimization for Proteins (MCCOP), a framework that computes minimal, biologically plausible sequence edits that flip a model's prediction to a desired target state. MCCOP operates in a continuous joint sequence-structure latent space and employs a pretrained diffusion model as a manifold prior, balancing three objectives: validity (achieving the target property), proximity (minimizing mutations), and plausibility (producing foldable proteins). We evaluate MCCOP on three protein engineering tasks - GFP fluorescence rescue, thermodynamic stability enhancement, and E3 ligase activity recovery - and show that it generates sparser, more plausible counterfactuals than both discrete and continuous baselines. The recovered mutations align with known biophysical mechanisms, including chromophore packing and hydrophobic core consolidation, establishing MCCOP as a tool for both model interpretation and hypothesis-driven protein design. Our code is publicly available at this http URL .

</details>

---

### 21. [$V_{0.5}$: Generalist Value Model as a Prior for Sparse RL Rollouts](https://arxiv.org/abs/2603.10848)

**基本信息**

- 🔗 arXiv: [`2603.10848`](https://arxiv.org/abs/2603.10848)
- 👥 作者: Yi-Kai Zhang, Yueqing Sun, Hongyan Hao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10848.pdf)

**💡 相关性分析**

满足标准3：论文专注于提升强化学习与可验证奖励（RLVR）的技术，而RLVR是训练和提升大模型（包括化学推理大模型）在数学和科学问题解决能力上的关键方法。论文对RLVR基线的改进进行了深入讨论，具有重要的相关性。

**📖 中文摘要**

本文提出了$V_{0.5}$，一种在强化学习与可验证奖励（RLVR）中构建稳健优势基线的方法。$V_{0.5}$自适应地融合了通用价值模型（如$V_0$）预测的基线（作为先验）与稀疏rollouts得出的经验均值，从而在计算效率和极低方差之间取得平衡。该方法通过实时统计测试和动态预算分配来实现。在六个数学推理基准上的广泛评估表明，$V_{0.5}$显著优于GRPO和DAPO，实现了更快的收敛和超过10%的性能提升。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In Reinforcement Learning with Verifiable Rewards (RLVR), constructing a robust advantage baseline is critical for policy gradients, effectively guiding the policy model to reinforce desired behaviors. Recent research has introduced Generalist Value Models (such as $V_0$), which achieve pre-trained value estimation by explicitly encoding model capabilities in-context, eliminating the need to synchronously update the value model alongside the policy model. In this paper, we propose $V_{0.5}$, which adaptively fuses the baseline predicted by such value model (acting as a prior) with the empirical mean derived from sparse rollouts. This constructs a robust baseline that balances computational efficiency with extremely low variance. Specifically, we introduce a real-time statistical testing and dynamic budget allocation. This balances the high variance caused by sparse sampling against the systematic bias (or hallucinations) inherent in the value model's prior. By constructing a hypothesis test to evaluate the prior's reliability in real-time, the system dynamically allocates additional rollout budget on demand. This mechanism minimizes the baseline estimator's Mean Squared Error (MSE), guaranteeing stable policy gradients, even under extreme sparsity with a group size of 4. Extensive evaluations across six mathematical reasoning benchmarks demonstrate that $V_{0.5}$ significantly outperforms GRPO and DAPO, achieving faster convergence and over some 10% performance improvement.

</details>

---

### 22. [6ABOS: An Open-Source Atmospheric Correction Framework for the EnMAP Hyperspectral Mission Based on 6S](https://arxiv.org/abs/2603.10856)

**基本信息**

- 🔗 arXiv: [`2603.10856`](https://arxiv.org/abs/2603.10856)
- 👥 作者: Gabriel Caballero Cañas, Bárbara Alvado Arranz, Xavier Sòria-Perpinyà 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10856.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于高光谱影像大气校正的开源工具6ABOS。虽然应用领域是遥感，但其核心是处理复杂的光谱数据以提取准确的信息。这种从复杂仪器信号中推理出目标物化性质（反射率）的流程，与从质谱信号中推理出化学结构的“质谱结构推理”任务在方法论上具有类比性。该工具展示了处理光谱数据的标准化流程，具有参考价值。

**📖 中文摘要**

本文介绍了6ABOS，一个基于6S辐射传输模型的开源Python框架，用于自动化EnMAP高光谱影像的大气校正。该框架集成了自动化的EnMAP元数据解析与通过Google Earth Engine API的动态大气参数检索。在西班牙两个内陆水库上的验证结果表明，6ABOS反演的水体反射率与现场测量值具有高度的光谱相似性。6ABOS通过conda-forge分发，为科学界提供了一个可扩展、透明、可重复的开源工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Environmental Mapping and Analysis Program (EnMAP) mission has opened new frontiers in the monitoring of optically complex environments. However, the accurate retrieval of surface reflectance over water bodies remains a significant challenge, as the water-leaving signal typically accounts for only a small fraction of the total radiance, being easily obscured by atmospheric scattering and surface reflection effects. This paper introduces 6ABOS (6S-based Atmospheric Background Offset Subtraction), a novel open-source Python framework designed to automate the atmospheric correction (AC) of EnMAP hyperspectral imagery. By leveraging the Second Simulation of the Satellite Signal in the Solar Spectrum (6S) radiative transfer model, 6ABOS implements a physically-based inversion scheme that accounts for Rayleigh scattering, aerosol interactions, and gaseous absorption. The framework integrates automated EnMAP metadata parsing with dynamic atmospheric parameter retrieval via the Google Earth Engine (GEE) Application Programming Interface (API). Validation was conducted over two Mediterranean inland water reservoirs with contrasting trophic states: the oligotrophic Benag{'e}ber and the hypertrophic Bell{'u}s. Results demonstrate a high degree of spectral similarity between in situ measurements and EnMAP-derived water-leaving reflectances. The Spectral Angle Mapper (SAM) values remained consistently low (SAM $<$ 10$^\circ$) across both study sites. 6ABOS is distributed via conda-forge, providing the scientific community with a scalable, transparent, and reproducible open-science tool for advancing hyperspectral aquatic research in the cloud-computing era.

</details>

---

### 23. [SNPgen: Phenotype-Supervised Genotype Representation and Synthetic Data Generation via Latent Diffusion](https://arxiv.org/abs/2603.10873)

**基本信息**

- 🔗 arXiv: [`2603.10873`](https://arxiv.org/abs/2603.10873)
- 👥 作者: Andrea Lampis, Michela Carlotta Massi, Nicola Pirastu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10873.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是使用生成式AI（变分自编码器和扩散模型）生成合成基因型数据。这属于“化学大模型”在生物信息学和基因组学领域的直接应用，是化学信息学的一个重要分支。

**📖 中文摘要**

本文提出了SNPgen，一个用于生成表型监督的合成基因型的两阶段条件潜在扩散框架。SNPgen结合了GWAS指导的变异选择、用于基因型压缩的变分自编码器，以及通过无分类器指导以二元疾病标签为条件的潜在扩散模型。在英国生物银行458,724个个体的四种复杂疾病上的评估表明，在“用合成数据训练，用真实数据测试”的协议下，使用合成数据训练的模型匹配了真实数据的预测性能。隐私分析确认了数据的隐私保护性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Polygenic risk scores and other genomic analyses require large individual-level genotype datasets, yet strict data access restrictions impede sharing. Synthetic genotype generation offers a privacy-preserving alternative, but most existing methods operate unconditionally, producing samples without phenotype alignment, or rely on unsupervised compression, creating a gap between statistical fidelity and downstream task utility. We present SNPgen, a two-stage conditional latent diffusion framework for generating phenotype-supervised synthetic genotypes. SNPgen combines GWAS-guided variant selection (1,024-2,048 trait-associated SNPs) with a variational autoencoder for genotype compression and a latent diffusion model conditioned on binary disease labels via classifier-free guidance. Evaluated on 458,724 UK Biobank individuals across four complex diseases (coronary artery disease, breast cancer, type 1 and type 2 diabetes), models trained on synthetic data matched real-data predictive performance in a train-on-synthetic, test-on-real protocol, approaching genome-wide PRS methods that use $2$-$6\times$ more variants. Privacy analysis confirmed zero identical matches, near-random membership inference (AUC $\approx 0.50$), preserved linkage disequilibrium structure, and high allele frequency correlation ($r \geq 0.95$) with source data. A controlled simulation with known causal effects verified faithful recovery of the imposed genetic association structure.

</details>

---

### 24. [A Physics-Informed, Global-in-Time Neural Particle Method for the Spatially Homogeneous Landau Equation](https://arxiv.org/abs/2603.10874)

**基本信息**

- 🔗 arXiv: [`2603.10874`](https://arxiv.org/abs/2603.10874)
- 👥 作者: Minseok Kim, Sung-Jun Son, Yeoneung Kim 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10874.pdf)

**💡 相关性分析**

满足标准3：论文提出了一种结合物理方程（Landau方程）与神经网络的新方法。虽然应用领域是等离子体物理，但其“物理信息神经网络”与“粒子方法”结合的思想，对于开发用于模拟化学动力学或分子动力学的“化学大模型”具有方法论上的启发和相关性。

**📖 中文摘要**

本文为空间齐次Landau方程提出了一种物理信息神经粒子方法（PINN-PM）。该方法采用拉格朗日相互作用粒子公式，并用神经网络联合参数化时间相关的分数和特征流图。通过沿着粒子轨迹定义的连续时间残差来强制执行Landau动力学。作者在$L^2_v$框架中建立了严格的稳定性分析，并将学习到的与精确的特征之间的偏差控制为三个可解释的来源。数值实验证明了稳定的传输、宏观不变量的保持以及与时间步进分数粒子方法相比具有竞争力或更高的精度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a physics-informed neural particle method (PINN--PM) for the spatially homogeneous Landau equation. The method adopts a Lagrangian interacting-particle formulation and jointly parameterizes the time-dependent score and the characteristic flow map with neural networks. Instead of advancing particles through explicit time stepping, the Landau dynamics is enforced via a continuous-time residual defined along particle trajectories. This design removes time-discretization error and yields a mesh-free solver that can be queried at arbitrary times without sequential integration. We establish a rigorous stability analysis in an $L^2_v$ framework. The deviation between learned and exact characteristics is controlled by three interpretable sources: (i) score approximation error, (ii) empirical particle approximation error, and (iii) the physics residual of the neural flow. This trajectory estimate propagates to density reconstruction, where we derive an $L^2_v$ error bound for kernel density estimators combining classical bias--variance terms with a trajectory-induced contribution. Using Hyvarinen's identity, we further relate the oracle score-matching gap to the $L^2_v$ score error and show that the empirical loss concentrates at the Monte Carlo rate, yielding computable a posteriori accuracy certificates. Numerical experiments on analytical benchmarks, including the two- and three-dimensional BKW solutions, as well as reference-free configurations, demonstrate stable transport, preservation of macroscopic invariants, and competitive or improved accuracy compared with time-stepping score-based particle and blob methods while using significantly fewer particles.

</details>

---

### 25. [Continuous Diffusion Transformers for Designing Synthetic Regulatory Elements](https://arxiv.org/abs/2603.10885)

**基本信息**

- 🔗 arXiv: [`2603.10885`](https://arxiv.org/abs/2603.10885)
- 👥 作者: Jonathan Liu, Kia Ghods
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10885.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散Transformer模型生成合成DNA调控序列。这直接属于“化学大模型”在合成生物学和DNA序列设计领域的应用，是化学信息学与AI交叉的前沿。

**📖 中文摘要**

本文提出了一个参数高效的扩散Transformer（DiT），用于生成200bp细胞类型特异性的调控DNA序列。通过用配备2D CNN输入编码器的Transformer去噪器替换DNA-Diffusion的U-Net主干，该模型在13个周期内匹配了U-Net的最佳验证损失，并收敛到低39%的损失。作者进一步应用DDPO微调，使用Enformer作为奖励模型，实现了预测调控活性的38倍改进。与DRAKES在独立预测任务上的交叉验证证实了改进反映了真实的调控信号。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a parameter-efficient Diffusion Transformer (DiT) for generating 200bp cell-type-specific regulatory DNA sequences. By replacing the U-Net backbone of DNA-Diffusion with a transformer denoiser equipped with a 2D CNN input encoder, our model matches the U-Net's best validation loss in 13 epochs (60$\times$ fewer) and converges 39% lower, while reducing memorization from 5.3% to 1.7% of generated sequences aligning to training data via BLAT. Ablations show the CNN encoder is essential: without it, validation loss increases 70% regardless of positional embedding choice. We further apply DDPO finetuning using Enformer as a reward model, achieving a 38$\times$ improvement in predicted regulatory activity. Cross-validation against DRAKES on an independent prediction task confirms that improvements reflect genuine regulatory signal rather than reward model overfitting.

</details>

---

### 26. [Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models](https://arxiv.org/abs/2603.10887)

**基本信息**

- 🔗 arXiv: [`2603.10887`](https://arxiv.org/abs/2603.10887)
- 👥 作者: Yixiu Mao, Yun Qu, Qi Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10887.pdf)

**💡 相关性分析**

满足标准3：论文专注于提升大型语言模型RL微调效率的数据选择策略。该技术对于高效训练专注于化学推理的“化学大模型”具有直接的方法论价值，属于对相关训练技术的重要讨论。

**📖 中文摘要**

本文提出了动态预测采样（DPS），用于大型推理模型的主动RL微调中的数据选择。DPS通过推断其学习动态来在线预测和选择信息丰富的提示，而无需昂贵的rollouts。具体来说，作者将每个提示在RL微调期间的解决进度建模为一个动力系统，其中解决程度表示为状态，转移由隐马尔可夫模型刻画。使用历史rollout奖励信号，进行在线贝叶斯推断以估计演化状态分布，推断结果为高效的提示选择提供了预测先验。在包括数学、规划和视觉几何在内的多样化推理任务上的实证结果表明，DPS显著减少了冗余rollouts，加速了训练过程，并实现了卓越的推理性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement learning (RL) finetuning has become a key technique for enhancing the reasoning abilities of large language models (LLMs). However, its effectiveness critically depends on the selection of training data. Recent advances underscore the importance of online prompt selection methods, which typically concentrate training on partially solved or moderately challenging examples under the current policy, thereby yielding more effective model updates. While significantly accelerating RL finetuning in terms of training steps, they also incur substantial computational overhead by requiring extensive LLM rollouts over large candidate batches to identify informative samples, an expense that can outweigh the finetuning process itself. To address this challenge, this work proposes Dynamics-Predictive Sampling (DPS), which online predicts and selects informative prompts by inferring their learning dynamics prior to costly rollouts. Specifically, we introduce a new perspective by modeling each prompt's solving progress during RL finetuning as a dynamical system, where the extent of solving is represented as the state and the transition is characterized by a hidden Markov model. Using historical rollout reward signals, we perform online Bayesian inference to estimate evolving state distributions, and the inference outcome provides a predictive prior for efficient prompt selection without rollout-intensive filtering. Empirical results across diverse reasoning tasks, including mathematics, planning, and visual geometry, demonstrate that DPS substantially reduces redundant rollouts, accelerates the training process, and achieves superior reasoning performance.

</details>

---

### 27. [A Hybrid Knowledge-Grounded Framework for Safety and Traceability in Prescription Verification](https://arxiv.org/abs/2603.10891)

**基本信息**

- 🔗 arXiv: [`2603.10891`](https://arxiv.org/abs/2603.10891)
- 👥 作者: Yichi Zhu, Kan Ling, Xu Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10891.pdf)

**💡 相关性分析**

满足标准1：论文的核心是构建一个结合了结构化知识库和大型语言模型的系统，用于药学领域的处方审核和推理。这直接属于“化学大模型”在药物安全和医疗化学信息学领域的应用实例。

**📖 中文摘要**

本文介绍了PharmGraph-Auditor，一个用于处方审核的安全、有证据支撑的新系统。其核心是一个在虚拟知识图谱（VKG）范式下实现的、可信的混合药学知识库（HPKB）。该架构战略性地统一了用于集合约束满足的关系组件和用于拓扑推理的图组件。为了构建HPKB，提出了迭代模式细化（ISR）算法。对于审核，引入了基于知识库的验证链（CoV），这是一种新的推理范式，将LLM从一个不可靠的生成器转变为一个透明的推理引擎。实验结果表明了强大的知识提取能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medication errors pose a significant threat to patient safety, making pharmacist verification (PV) a critical, yet heavily burdened, final safeguard. The direct application of Large Language Models (LLMs) to this zero-tolerance domain is untenable due to their inherent factual unreliability, lack of traceability, and weakness in complex reasoning. To address these challenges, we introduce PharmGraph-Auditor, a novel system designed for safe and evidence-grounded prescription auditing. The core of our system is a trustworthy Hybrid Pharmaceutical Knowledge Base (HPKB), implemented under the Virtual Knowledge Graph (VKG) paradigm. This architecture strategically unifies a relational component for set constraint satisfaction and a graph component for topological reasoning via a rigorous mapping layer. To construct this HPKB, we propose the Iterative Schema Refinement (ISR) algorithm, a framework that enables the co-evolution of both graph and relational schemas from medical texts. For auditing, we introduce the KB-grounded Chain of Verification (CoV), a new reasoning paradigm that transforms the LLM from an unreliable generator into a transparent reasoning engine. CoV decomposes the audit task into a sequence of verifiable queries against the HPKB, generating hybrid query plans to retrieve evidence from the most appropriate data store. Experimental results demonstrate robust knowledge extraction capabilities and show promises of using PharmGraph-Auditor to enable pharmacists to achieve safer and faster prescription verification.

</details>

---

### 28. [LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future without Generation](https://arxiv.org/abs/2603.10899)

**基本信息**

- 🔗 arXiv: [`2603.10899`](https://arxiv.org/abs/2603.10899)
- 👥 作者: Jinwoo Ahn, Ingyu Seong, Akhil Kedia 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10899.pdf)

**💡 相关性分析**

满足标准3：论文研究了提升大型语言模型长上下文处理效率的技术（KV缓存管理）。这对于处理长序列化学数据（如长分子序列或连续的质谱谱图）的“化学大模型”具有重要的工程优化意义，属于相关的重要技术讨论。

**📖 中文摘要**

本文提出了LookaheadKV，一个轻量级的KV缓存驱逐框架，它利用了代理未来响应的优势，但无需显式的草稿生成。LookaheadKV通过训练参数高效的模块来准确预测真实的重要性分数。其设计确保了与现有廉价启发式方法相当的可忽略运行时开销，同时实现了比更昂贵的近似方法更高的准确性。在长上下文理解基准上的大量实验表明，该方法不仅在各种长上下文理解任务中优于最近的竞争基线，还将驱逐成本降低了高达14.5倍，从而显著加快了首次令牌生成时间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transformer-based large language models (LLMs) rely on key-value (KV) caching to avoid redundant computation during autoregressive inference. While this mechanism greatly improves efficiency, the cache size grows linearly with the input sequence length, quickly becoming a bottleneck for long-context tasks. Existing solutions mitigate this problem by evicting prompt KV that are deemed unimportant, guided by estimated importance scores. Notably, a recent line of work proposes to improve eviction quality by "glimpsing into the future", in which a draft generator produces a surrogate future response approximating the target model's true response, and this surrogate is subsequently used to estimate the importance of cached KV more accurately. However, these approaches rely on computationally expensive draft generation, which introduces substantial prefilling overhead and limits their practicality in real-world deployment. To address this challenge, we propose LookaheadKV, a lightweight eviction framework that leverages the strength of surrogate future response without requiring explicit draft generation. LookaheadKV augments transformer layers with parameter-efficient modules trained to predict true importance scores with high accuracy. Our design ensures negligible runtime overhead comparable to existing inexpensive heuristics, while achieving accuracy superior to more costly approximation methods. Extensive experiments on long-context understanding benchmarks, across a wide range of models, demonstrate that our method not only outperforms recent competitive baselines in various long-context understanding tasks, but also reduces the eviction cost by up to 14.5x, leading to significantly faster time-to-first-token. Our code is available at this https URL .

</details>

---

### 29. [LLM2Vec-Gen: Generative Embeddings from Large Language Models](https://arxiv.org/abs/2603.10913)

**基本信息**

- 🔗 arXiv: [`2603.10913`](https://arxiv.org/abs/2603.10913)
- 👥 作者: Parishad BehnamGhader, Vaibhav Adlakha, Fabian David Schmidt 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10913.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种从大型语言模型生成高质量文本嵌入的新方法。文本嵌入是化学信息学中表示分子、反应和文献的关键技术。该方法为构建更好的化学实体嵌入模型提供了新的工具和思路，具有资源相关性。

**📖 中文摘要**

本文提出了LLM2Vec-Gen，一种新颖的自监督方法，用于从大型语言模型生成文本嵌入。与编码输入不同，该方法学习表示模型的潜在响应。具体来说，我们将可训练的特殊token添加到LLM的词汇表中，将其附加到输入，并优化它们以在固定长度的序列中表示LLM的响应。训练由LLM自身对查询的完成以及提供蒸馏目标的非监督嵌入教师模型指导。这种表述有助于弥合输入-输出差距，并将LLM的安全对齐和推理等能力转移到嵌入任务中。LLM2Vec-Gen在Massive Text Embedding Benchmark（MTEB）上实现了最先进的自监督性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLM-based text embedders typically encode the semantic content of their input. However, embedding tasks require mapping diverse inputs to similar outputs. Typically, this input-output is addressed by training embedding models with paired data using contrastive learning. In this work, we propose a novel self-supervised approach, LLM2Vec-Gen, which adopts a different paradigm: rather than encoding the input, we learn to represent the model's potential response. Specifically, we add trainable special tokens to the LLM's vocabulary, append them to input, and optimize them to represent the LLM's response in a fixed-length sequence. Training is guided by the LLM's own completion for the query, along with an unsupervised embedding teacher that provides distillation targets. This formulation helps to bridge the input-output gap and transfers LLM capabilities such as safety alignment and reasoning to embedding tasks. Crucially, the LLM backbone remains frozen and training requires only unlabeled queries. LLM2Vec-Gen achieves state-of-the-art self-supervised performance on the Massive Text Embedding Benchmark (MTEB), improving by 9.3% over the best unsupervised embedding teacher. We also observe up to 43.2% reduction in harmful content retrieval and 29.3% improvement in reasoning capabilities for embedding tasks. Finally, the learned embeddings are interpretable and can be decoded into text to reveal their semantic content.

</details>

---

### 30. [Bridging the Skill Gap in Clinical CBCT Interpretation with CBCTRepD](https://arxiv.org/abs/2603.10933)

**基本信息**

- 🔗 arXiv: [`2603.10933`](https://arxiv.org/abs/2603.10933)
- 👥 作者: Qinxin Wu, Fucheng Niu, Hengchuan Zhu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10933.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了一个大规模、高质量的口腔医学影像-报告配对数据集，并开发了相应的报告生成系统。虽然领域特定，但其构建专业领域“数据-文本”配对数据集的方法、以及开发领域大模型系统的流程，对于构建化学领域（如质谱-结构配对）的类似数据集和模型具有重要的参考价值和示范作用。

**📖 中文摘要**

本文介绍了CBCTRepD，一个双语口腔颌面锥形束CT报告生成系统。作者策划了一个大规模、高质量的口腔颌面CBCT报告配对数据集，包含约7,408项研究，涵盖55种口腔疾病实体。基于此，开发了报告生成系统，并建立了一个临床基础的多层次评估框架。评估表明，CBCTRepD在报告生成性能上表现优异，其草稿的书写质量和标准化程度可与中级放射科医生相媲美。更重要的是，在人机协作中，CBCTRepD为不同经验水平的放射科医生提供了一致且具有临床意义的帮助。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative AI has advanced rapidly in medical report generation; however, its application to oral and maxillofacial CBCT reporting remains limited, largely because of the scarcity of high-quality paired CBCT-report data and the intrinsic complexity of volumetric CBCT interpretation. To address this, we introduce CBCTRepD, a bilingual oral and maxillofacial CBCT report-generation system designed for integration into routine radiologist-AI co-authoring workflows. We curated a large-scale, high-quality paired CBCT-report dataset comprising approximately 7,408 studies, covering 55 oral disease entities across diverse acquisition settings, and used it to develop the system. We further established a clinically grounded, multi-level evaluation framework that assesses both direct AI-generated drafts and radiologist-edited collaboration reports using automatic metrics together with radiologist- and clinician-centered evaluation. Using this framework, we show that CBCTRepD achieves superior report-generation performance and produces drafts with writing quality and standardization comparable to those of intermediate radiologists. More importantly, in radiologist-AI collaboration, CBCTRepD provides consistent and clinically meaningful benefits across experience levels: it helps novice radiologists improve toward intermediate-level reporting, enables intermediate radiologists to approach senior-level performance, and even assists senior radiologists by reducing omission-related errors, including clinically important missed lesions. By improving report structure, reducing omissions, and promoting attention to co-existing lesions across anatomical regions, CBCTRepD shows strong and reliable potential as a practical assistant for real-world CBCT reporting across multi-level care settings.

</details>

---

### 31. [Historical Consensus: Preventing Posterior Collapse via Iterative Selection of Gaussian Mixture Priors](https://arxiv.org/abs/2603.10935)

**基本信息**

- 🔗 arXiv: [`2603.10935`](https://arxiv.org/abs/2603.10935)
- 👥 作者: Zegu Zhang, Jian Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10935.pdf)

**💡 相关性分析**

满足标准3：论文深入研究了变分自编码器中后验坍塌问题的根本原因和解决方案。VAE及其变体是化学信息学中用于分子生成和表示学习的常用模型。该研究对于构建更稳定、更有效的化学分子生成大模型具有重要的理论和方法论意义。

**📖 中文摘要**

本文提出了历史共识训练（Historical Consensus Training），一种迭代选择程序，通过交替优化和选择逐步细化一组候选高斯混合模型（GMM）先验。关键见解是，被训练以满足多个不同聚类约束的模型会形成一个历史障碍——参数空间中的一个区域，即使在后续使用单一目标训练时也能保持稳定。作者证明了这个障碍排除了坍塌解，并通过在合成和真实世界数据集上的大量实验证明，该方法无论解码器方差或正则化强度如何，都能实现非坍塌表示。该方法不需要显式的稳定性条件，并且适用于任意的神经架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Variational autoencoders (VAEs) frequently suffer from posterior collapse, where latent variables become uninformative and the approximate posterior degenerates to the prior. Recent work has characterized this phenomenon as a phase transition governed by the spectral properties of the data covariance matrix. In this paper, we propose a fundamentally different approach: instead of avoiding collapse through architectural constraints or hyperparameter tuning, we eliminate the possibility of collapse altogether by leveraging the multiplicity of Gaussian mixture model (GMM) clusterings. We introduce Historical Consensus Training, an iterative selection procedure that progressively refines a set of candidate GMM priors through alternating optimization and selection. The key insight is that models trained to satisfy multiple distinct clustering constraints develop a historical barrier -- a region in parameter space that remains stable even when subsequently trained with a single objective. We prove that this barrier excludes the collapsed solution, and demonstrate through extensive experiments on synthetic and real-world datasets that our method achieves non-collapsed representations regardless of decoder variance or regularization strength. Our approach requires no explicit stability conditions (e.g., $\sigma^{\prime 2} < \lambda_{\max}$) and works with arbitrary neural architectures. The code is available at this https URL .

</details>

---

### 32. [When should we trust the annotation? Selective prediction for molecular structure retrieval from mass spectra](https://arxiv.org/abs/2603.10950)

**基本信息**

- 🔗 arXiv: [`2603.10950`](https://arxiv.org/abs/2603.10950)
- 👥 作者: Mira Jürgens, Gaetan De Waele, Morteza Rakhshaninejad 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10950.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕【质谱结构推理】这一主题，专注于从串联质谱中识别分子结构并评估预测不确定性。

**📖 中文摘要**

本文针对从串联质谱（MS/MS）中识别分子结构这一核心任务，提出了一种选择性预测框架。该框架允许模型在预测不确定性过高时主动放弃预测，从而在高风险的临床代谢组学等应用中提高预测的可靠性。研究在MassSpecGym基准上全面评估了不同粒度（指纹级和检索级）的不确定性量化策略，包括一阶置信度、二阶分布估计的偶然和认知不确定性，以及潜在空间中的距离度量。结果表明，检索级的偶然不确定性估计能实现良好的风险-覆盖率权衡。这项工作直接针对【质谱结构推理】的核心挑战——提高预测的可靠性，并提供了实用的不确定性量化工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning methods for identifying molecular structures from tandem mass spectra (MS/MS) have advanced rapidly, yet current approaches still exhibit significant error rates. In high-stakes applications such as clinical metabolomics and environmental screening, incorrect annotations can have serious consequences, making it essential to determine when a prediction can be trusted. We introduce a selective prediction framework for molecular structure retrieval from MS/MS spectra, enabling models to abstain from predictions when uncertainty is too high. We formulate the problem within the risk-coverage tradeoff framework and comprehensively evaluate uncertainty quantification strategies at two levels of granularity: fingerprint-level uncertainty over predicted molecular fingerprint bits, and retrieval-level uncertainty over candidate rankings. We compare scoring functions including first-order confidence measures, aleatoric and epistemic uncertainty estimates from second-order distributions, as well as distance-based measures in the latent space. All experiments are conducted on the MassSpecGym benchmark. Our analysis reveals that while fingerprint-level uncertainty scores are poor proxies for retrieval success, computationally inexpensive first-order confidence measures and retrieval-level aleatoric uncertainty achieve strong risk-coverage tradeoffs across evaluation settings. We demonstrate that by applying distribution-free risk control via generalization bounds, practitioners can specify a tolerable error rate and obtain a subset of annotations satisfying that constraint with high probability.

</details>

---

### 33. [Reference Architecture of a Quantum-Centric Supercomputer](https://arxiv.org/abs/2603.10970)

**基本信息**

- 🔗 arXiv: [`2603.10970`](https://arxiv.org/abs/2603.10970)
- 👥 作者: Seetharami Seelam, Jerry M. Chow, Antonio Córcoles 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10970.pdf)

**💡 相关性分析**

满足标准3：论文是关于未来计算系统（量子-经典混合）的综述和展望，其中明确将化学和材料科学作为关键应用领域，讨论了支撑未来【化学大模型】运行的基础设施蓝图。

**📖 中文摘要**

本文提出了量子中心超级计算机（QCSC）的参考架构和路线图，旨在整合量子处理单元（QPU）、图形处理单元（GPU）和中央处理单元（CPU），以加速跨应用的算法发现。文章特别指出，在化学和材料科学等领域，算法和工作流需要同时利用量子计算机和经典高性能计算系统来扩展模拟规模。该架构设想通过三个阶段演进，最终实现用于混合计算工作流的完全协同设计的异构量子-HPC系统。这项工作为未来利用量子-经典混合计算系统解决化学等领域的复杂问题（即运行【化学大模型】）提供了关键的硬件和系统架构展望。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum computers have demonstrated utility in simulating quantum systems beyond brute-force classical approaches. As the community builds on these demonstrations to explore using quantum computing for applied research, algorithms and workflows have emerged that require leveraging both quantum computers and classical high-performance computing (HPC) systems to scale applications, especially in chemistry and materials, beyond what either system can simulate alone. Today, these disparate systems operate in isolation, forcing users to manually orchestrate workloads, coordinate job scheduling, and transfer data between systems -- a cumbersome process that hinders productivity and severely limits rapid algorithmic exploration. These challenges motivate the need for flexible and high-performance Quantum-Centric Supercomputing (QCSC) systems that integrate Quantum Processing Units (QPUs), Graphics Processing Units (GPUs), and Central Processing Units (CPUs) to accelerate discovery of such algorithms across applications. These systems will be co-designed across quantum and classical HPC infrastructure, middleware, and application layers to accelerate the adoption of quantum computing for solving critical computational problems. We envision QCSC evolution through three distinct phases: (1) quantum systems as specialized compute offload engines within existing HPC complexes; (2) heterogeneous quantum and classical HPC systems coupled through advanced middleware, enabling seamless execution of hybrid quantum-classical algorithms; and (3) fully co-designed heterogeneous quantum-HPC systems for hybrid computational workflows. This article presents a reference architecture and roadmap for these QCSC systems.

</details>

---

### 34. [Flexible Cutoff Learning: Optimizing Machine Learning Potentials After Training](https://arxiv.org/abs/2603.10205)

**基本信息**

- 🔗 arXiv: [`2603.10205`](https://arxiv.org/abs/2603.10205)
- 👥 作者: Rick Oerder, Jan Hamaekers
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10205.pdf)

**💡 相关性分析**

满足标准2：论文提出的FCL方法是一种用于机器学习原子间势（MLIPs）的新工具和训练范式，可用于构建和优化化学领域的【化学大模型】。

**📖 中文摘要**

本文提出了灵活截止学习（FCL），一种用于训练机器学习原子间势（MLIPs）的方法。该方法允许在训练后调整模型的截止半径，从而在保持精度的同时优化计算成本。作者使用修改后的MACE架构在MAD数据集上进行演示，并展示了通过后训练优化，可以在分子晶体子集上减少超过60%的计算成本，而力误差增加不到1%。这项工作通过提供一种可适应不同应用的通用MLIP训练方法，为【化学大模型】（特别是用于分子模拟的机器学习势函数）的开发提供了重要的工具和资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Flexible Cutoff Learning (FCL), a method for training machine learning interatomic potentials (MLIPs) whose cutoff radii can be adjusted after training. Unlike conventional MLIPs that fix the cutoff radius during training, FCL models are trained by randomly sampling cutoff radii independently for each atom. The resulting model can then be deployed with different per-atom cutoff radii depending on the application, enabling application-specific optimization of the accuracy-cost tradeoff. Using a differentiable cost model, these per-atom cutoffs can be optimized for specific target systems after training. We demonstrate FCL with a modified MACE architecture trained on the MAD dataset. For a subset featuring molecular crystals, optimized per-atom cutoffs reduce computational cost by more than 60% while increasing force errors by less than 1%. These results show that FCL enables training of a single general-purpose MLIP that can be adapted to diverse applications through post-training cutoff optimization, eliminating the need for retraining.

</details>

---

### 35. [Geo-ADAPT-VQE: Quantum Information Metric-Aware Circuit Optimization for Quantum Chemistry](https://arxiv.org/abs/2603.10325)

**基本信息**

- 🔗 arXiv: [`2603.10325`](https://arxiv.org/abs/2603.10325)
- 👥 作者: Mohammad Aamir Sohail, Toshiaki Koike-Akino
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10325.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用量子计算和自适应算法优化量子化学模拟，这直接属于利用先进计算模型（【化学大模型】）解决化学问题的范畴。

**📖 中文摘要**

本文介绍了Geo-ADAPT-VQE，一种用于量子化学变分量子本征求解器（VQE）的几何感知自适应算法。该算法利用自然梯度规则从算子池中选择算子，使ansatz沿着量子态空间的底层几何方向增长，从而改善收敛性、减少对局部极小值和鞍点区域的敏感性，并生成更短的ansatz。数值模拟涉及五个分子，结果表明Geo-ADAPT-VQE相比现有方法实现了更快、更稳定的收敛，同时显著缩短了ansatz长度。这项工作直接推动了量子计算在【化学大模型】（特别是量子化学模拟）中的应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adaptive ansatz construction has emerged as a powerful technique for reducing circuit depth and improving optimization efficiency in variational quantum eigensolvers. However, existing adaptive methods, including ADAPT-VQE, rely solely on first-order gradients and therefore ignore the underlying geometry of the quantum state space, limiting both convergence behavior and operator-selection efficiency. We introduce Geo-ADAPT-VQE, a geometry-aware adaptive VQE algorithm that selects operators from a pool using the natural gradient rule. The geometric operator-selection rule enables the ansatz to grow along directions aligned with the underlying quantum-state geometry, thereby improving convergence and reducing the algorithm's susceptibility to shallow local minima and saddle-point regions. We further provide an asymptotic convergence result. We present numerical simulations involving five molecules, which demonstrate that Geo-ADAPT-VQE achieves faster and more stable convergence compared to existing methods, while producing significantly shorter ansatz. In particular, Geo-ADAPT achieves up to 100-fold reduction in energy error compared to existing methods.

</details>

---

### 36. [Hybridlane: A Software Development Kit for Hybrid Continuous-Discrete Variable Quantum Computing](https://arxiv.org/abs/2603.10919)

**基本信息**

- 🔗 arXiv: [`2603.10919`](https://arxiv.org/abs/2603.10919)
- 👥 作者: Jim Furches, Timothy J. Stavenger, Carlos Ortiz Marrero
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10919.pdf)

**💡 相关性分析**

满足标准2：论文提出了Hybridlane这一软件开发工具包，为在量子计算平台上实现和运行可能用于化学模拟的混合连续-离散变量模型（属于【化学大模型】范畴）提供了重要的工具和资源。

**📖 中文摘要**

本文介绍了Hybridlane，一个用于混合连续-离散变量量子计算的开源软件开发工具包。它提供了统一的混合电路前端，支持自动线类型推断以区分量子比特和量子模，实现了广泛的混合门和分解库，并与PennyLane的量子比特算法库兼容。该框架支持包括Bosonic Qiskit经典模拟和Sandia国家实验室QSCOUT离子阱硬件编译在内的多个后端。作者通过玻色子量子相位估计和离子阱校准工作流展示了其能力。这项工作为构建和运行涉及连续变量（如用于化学模拟的振动模式）的【化学大模型】提供了关键的软件基础设施和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hybrid quantum computing systems that combine discrete-variable qubits with continuous-variable qumodes offer promising advantages for quantum simulation, error correction, and sensing applications. However, existing quantum software frameworks lack native support for expressing and manipulating hybrid circuits, forcing developers to work with fragmented toolchains or rely on simulation-coupled representations that limit scalability. We present Hybridlane, an open-source software development kit providing a unified frontend for hybrid continuous-discrete variable quantum computing. Hybridlane introduces automatic wire type inference to distinguish qubits from qumodes without manual annotations, enabling compile-time validation of circuit correctness. By decoupling gate semantics from matrix representations, Hybridlane can describe wide and deep circuits with minimal memory consumption and without requiring simulation. The framework implements a comprehensive library of hybrid gates and decompositions following established instruction set architectures, while remaining compatible with PennyLane's extensive qubit algorithm library. Furthermore, it supports multiple backends including classical simulation with Bosonic Qiskit and hardware compilation to Sandia National Laboratories' QSCOUT ion trap. We demonstrate Hybridlane's capabilities through bosonic quantum phase estimation and ion trap calibration workflows.

</details>

---

### 37. [Bayesian Optimization with Gaussian Processes to Accelerate Stationary Point Searches](https://arxiv.org/abs/2603.10992)

**基本信息**

- 🔗 arXiv: [`2603.10992`](https://arxiv.org/abs/2603.10992)
- 👥 作者: Rohit Goswami
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10992.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于贝叶斯优化和高斯过程的计算框架与算法，可用于加速化学中势能面搜索等核心计算任务，为【化学大模型】的开发和优化提供了重要的方法和工具资源。

**📖 中文摘要**

本文提出了一个统一的贝叶斯优化框架，用于加速势能面上驻点（如极小值和鞍点）的搜索。该框架使用带有导数观测的高斯过程回归作为代理模型，并集成了最优传输GP扩展、最远点采样、自适应信任半径等技术来提高准确性和效率。作者提供了配套的教学用Rust代码来演示该方法。这项工作为化学中至关重要的势能面探索和反应路径寻找提供了先进的优化算法，是构建和优化【化学大模型】（特别是那些涉及能量和几何结构计算的模型）的关键计算工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accelerating the explorations of stationary points on potential energy surfaces building local surrogates spans decades of effort. Done correctly, surrogates reduce required evaluations by an order of magnitude while preserving the accuracy of the underlying theory. We present a unified Bayesian Optimization view of minimization, single point saddle searches, and double ended saddle searches through a unified six-step surrogate loop, differing only in the inner optimization target and acquisition criterion. The framework uses Gaussian process regression with derivative observations, inverse-distance kernels, and active learning. The Optimal Transport GP extensions of farthest point sampling with Earth mover's distance, MAP regularization via variance barrier and oscillation detection, and adaptive trust radius form concrete extensions of the same basic methodology, improving accuracy and efficiency. We also demonstrate random Fourier features decouple hyperparameter training from predictions enabling favorable scaling for high-dimensional systems. Accompanying pedagogical Rust code demonstrates that all applications use the exact same Bayesian optimization loop, bridging the gap between theoretical formulation and practical execution.

</details>

---

### 38. [Mindstorms in Natural Language-Based Societies of Mind](https://arxiv.org/abs/2305.17066)

**基本信息**

- 🔗 arXiv: [`2305.17066`](https://arxiv.org/abs/2305.17066)
- 👥 作者: Mingchen Zhuge, Haozhe Liu, Francesco Faccio 等26人
- 📄 PDF: [下载](https://arxiv.org/pdf/2305.17066.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕由大型语言模型（LLMs）构成的智能体社会（NLSOMs），这直接关联到“化学大模型”这一主题，探讨了如何通过多智能体协作来增强模型能力，为构建领域专用大模型（如化学大模型）提供了架构思路。

**📖 中文摘要**

这篇论文探讨了基于自然语言的多模态神经网络社会（NLSOMs）的概念，其中大型语言模型（LLMs）和其他神经网络专家通过自然语言接口进行通信和协作，以解决复杂问题。论文的核心思想是通过“思维风暴”（mindstorm）让不同的AI代理（包括LLMs）进行交互和访谈，从而克服单一LLM的局限性，提升多模态零样本推理能力。这项工作直接关联到“化学大模型”的主题，因为它研究的是由大型语言模型构成的、可模块化扩展的智能体社会，这种架构和协作范式对于构建用于复杂科学问题（如化学信息学中的分子设计或质谱解析）的“化学大模型”或“专家社会”具有重要的启发和借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Both Minsky's "society of mind" and Schmidhuber's "learning to think" inspire diverse societies of large multimodal neural networks (NNs) that solve problems by interviewing each other in a "mindstorm." Recent implementations of NN-based societies of minds consist of large language models (LLMs) and other NN-based experts communicating through a natural language interface. In doing so, they overcome the limitations of single LLMs, improving multimodal zero-shot reasoning. In these natural language-based societies of mind (NLSOMs), new agents -- all communicating through the same universal symbolic language -- are easily added in a modular fashion. To demonstrate the power of NLSOMs, we assemble and experiment with several of them (having up to 129 members), leveraging mindstorms in them to solve some practical AI tasks: visual question answering, image captioning, text-to-image synthesis, 3D generation, egocentric retrieval, embodied AI, and general language-based task solving. We view this as a starting point towards much larger NLSOMs with billions of agents-some of which may be humans. And with this emergence of great societies of heterogeneous minds, many new research questions have suddenly become paramount to the future of artificial intelligence. What should be the social structure of an NLSOM? What would be the (dis)advantages of having a monarchical rather than a democratic structure? How can principles of NN economies be used to maximize the total reward of a reinforcement learning NLSOM? In this work, we identify, discuss, and try to answer some of these questions.

</details>

---

### 39. [Optimal Transport Aggregation for Distributed Mixture-of-Experts](https://arxiv.org/abs/2312.09877)

**基本信息**

- 🔗 arXiv: [`2312.09877`](https://arxiv.org/abs/2312.09877)
- 👥 作者: Faïcel Chamroukhi, Nhat Thien Pham
- 📄 PDF: [下载](https://arxiv.org/pdf/2312.09877.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是混合专家模型的分布式聚合，混合专家模型是构建大规模、专业化模型（如“化学大模型”）的关键架构之一。论文提出的最优传输聚合框架为解决此类大模型的分布式训练与集成提供了重要的方法论。

**📖 中文摘要**

本文提出了一种基于最优传输（Optimal Transport）的分布式混合专家模型（MoE）聚合框架。该框架旨在解决数据分散存储在不同机器上时，如何将本地训练的MoE模型高效地聚合成一个全局MoE估计器的问题。论文的核心贡献是设计了一个基于最优传输距离最小化的原则性聚合方法，并推导了高效的优化算法。虽然论文的应用背景是通用的分布式学习，但“混合专家模型”本身就是一种重要的大模型架构范式。论文所解决的模型聚合、参数对齐和通信效率问题，对于在化学信息学等领域构建和部署需要整合多方数据或模型知识的“化学大模型”具有直接的技术参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixture-of-experts (MoE) models provide a flexible statistical framework for modeling heterogeneity and nonlinear relationships. In many modern applications, however, datasets are naturally distributed across multiple machines due to storage, computational, or governance constraints. We consider a distributed model aggregation setting in which local MoE models are trained independently on decentralized datasets and subsequently combined into a global estimator. Aggregating MoE models is challenging because standard averaging produces models that do not preserve the MoE structure, and therefore do not yield estimates of the global model parameters. To address this issue, we propose a principled aggregation framework based on optimal transport that constructs a reduced global MoE estimator by minimizing a transportation divergence between the collection of local estimators and the aggregated model. An efficient majorization--minimization (MM) algorithm is derived to solve the resulting optimization problem. The method requires only a single communication step from local machines to a central server, making it a frugal distributed learning approach particularly attractive for large-scale settings where communication costs are a major bottleneck. We further establish statistical guarantees for the aggregated estimator, including consistency under standard assumptions on the local estimators. Experiments on synthetic and real datasets demonstrate that the approach achieves performance comparable to centralized training while significantly reducing computation time. The source codes are publicly available on Github.

</details>

---

### 40. [Communication-Efficient Multimodal Federated Learning: Joint Modality and Client Selection](https://arxiv.org/abs/2401.16685)

**基本信息**

- 🔗 arXiv: [`2401.16685`](https://arxiv.org/abs/2401.16685)
- 👥 作者: Liangqi Yuan, Dong-Jun Han, Su Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2401.16685.pdf)

**💡 相关性分析**

满足标准1：论文研究多模态联邦学习的高效框架，其解耦架构和选择机制对于在数据分散、模态异构的场景下构建和优化“化学大模型”具有重要的方法论参考价值，直接关联到大模型的训练与集成技术。

**📖 中文摘要**

本文提出了MFedMC，一个通信高效的多模态联邦学习框架，其核心是解耦的架构和联合模态与客户端选择算法。该框架将模态编码器（用于跨客户端泛化）与融合模块（用于客户端个性化）分离，并设计算法来选择重要的模态和客户端进行更新。虽然论文的应用场景是多模态联邦学习，但其核心思想——通过解耦设计和选择性通信来高效训练和整合来自异构数据源的模型——与构建需要整合多源、多模态数据（如化学结构、质谱、文本描述）的“化学大模型”所面临的挑战高度相关。论文为解决大模型训练中的数据异构性和通信瓶颈问题提供了可行的技术方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal federated learning (MFL) aims to enrich model training in FL settings where clients are collecting measurements across multiple modalities. However, key challenges to MFL remain unaddressed, particularly in heterogeneous network settings where: (i) the set of modalities collected by each client is diverse, and (ii) communication limitations prevent clients from uploading all their locally trained modality encoders to the server. In this paper, we propose Multimodal Federated learning with joint Modality and Client selection (MFedMC), a communication-efficient MFL framework that tackles these challenges through a decoupled architecture and selective uploading. Unlike traditional holistic fusion approaches, MFedMC separates modality encoders and fusion modules: modality encoders are aggregated at the server for generalization across diverse client distributions, while fusion modules remain local to each client for personalized adaptation to individual modality configurations and data characteristics. Building on this decoupled design, our joint selection algorithm incorporates two main components: (a) A modality selection methodology for each client, which weighs (i) the impact of the modality, gauged by Shapley value analysis, (ii) the modality encoder size as a gauge of communication overhead, and (iii) the frequency of modality encoder updates, denoted recency, to enhance generalizability. (b) A client selection strategy for the server based on the local loss of modality encoders at each client. Experiments on five real-world datasets demonstrate that MFedMC achieves comparable accuracy to several baselines while reducing communication overhead by over 20$\times$. A demo video and our code are available at this https URL .

</details>

---

### 41. [Modelling Language using Large Language Models](https://arxiv.org/abs/2404.09579)

**基本信息**

- 🔗 arXiv: [`2404.09579`](https://arxiv.org/abs/2404.09579)
- 👥 作者: Jumbly Grindrod
- 📄 PDF: [下载](https://arxiv.org/pdf/2404.09579.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是论证大型语言模型作为科学模型（特别是语言模型）的价值和角色。这直接关联到“化学大模型”主题的根本性问题：大模型如何作为化学领域的知识表示和推理工具。

**📖 中文摘要**

本文论证了大型语言模型可以作为公共语言的科学模型，在语言学研究中扮演有价值的角色。论文主张，语言学不仅应关注语言能力背后的认知过程，也应将语言视为一种外部的、社会的实体。一旦认识到这一点，大型语言模型作为科学模型的价值就变得清晰。作者通过构建“模型解释”来阐述如何利用计算语言学的最新进展来理解LLMs的内部工作机制，从而将其发展为语言的模型。这篇论文是从哲学和语言学角度对“大模型”本质和价值的探讨，虽然不直接针对化学，但其关于大模型如何作为领域（此处是语言）知识载体的核心论点，对于思考“化学大模型”如何表征和推理化学知识具有根本性的启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper argues that large language models have a valuable scientific role to play in serving as scientific models of public languages. Linguistic study should not only be concerned with the cognitive processes behind linguistic competence, but also with language understood as an external, social entity. Once this is recognized, the value of large language models as scientific models becomes clear. This paper defends the position against a number of arguments to the effect that language models provide no linguistic insight. Building upon Weisberg's (2007) notion of a model construal, it is then argued that recent work in computational linguistics to better understand the inner workings of large language models can be used to develop a model construal for large language models as models of a language.

</details>

---

### 42. [EoRA: Fine-tuning-free Compensation for Compressed LLM with Eigenspace Low-Rank Approximation](https://arxiv.org/abs/2410.21271)

**基本信息**

- 🔗 arXiv: [`2410.21271`](https://arxiv.org/abs/2410.21271)
- 👥 作者: Shih-Yang Liu, Maksim Khadkevich, Nai Chit Fung 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2410.21271.pdf)

**💡 相关性分析**

满足标准1：论文研究大型语言模型的压缩与性能恢复，提出的EoRA方法旨在高效恢复压缩模型的能力。这对于“化学大模型”的实际部署和应用至关重要，提供了在保持性能的同时降低计算成本的技术方案。

**📖 中文摘要**

本文提出了EoRA，一种无需微调的方法，用于补偿压缩后的大型语言模型的精度损失。EoRA通过特征空间低秩近似，为压缩后的LLM添加低秩矩阵，使用户能够快速提升模型在特定任务上的性能，并在精度和计算开销之间自由权衡，不受压缩格式的限制。论文还引入了优化的CUDA内核来加速推理。这项工作虽然主要针对通用LLM的后训练压缩与恢复，但其核心思想——通过低秩适配来快速、灵活地恢复或增强压缩模型在特定领域的性能——对于在资源受限环境下部署和优化“化学大模型”具有直接的应用价值。它为化学领域大模型的轻量化部署和快速任务适配提供了可行的技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While post-training compression techniques effectively reduce the memory footprint, latency, and power consumption of Large Language Models (LLMs), they often result in noticeable accuracy degradation and remain limited by hardware and kernel constraints that restrict supported compression formats ultimately reducing flexibility across a wide range of deployment scenarios. In this work, we propose EoRA, a novel fine-tuning-free method that augments compressed LLMs with low-rank matrices, allowing users to rapidly enhance task-specific performance and freely balance the trade-off between accuracy and computational overhead beyond the constraints of compression formats. EoRA consistently outperforms prior training-free low rank methods in recovering the accuracy of compressed LLMs, achieving notable accuracy improvements (e.g., $\mathbf{10.84\%}$ on ARC-Challenge, $\mathbf{6.74\%}$ on MathQA, and $\mathbf{11.45\%}$ on GSM8K) for LLaMA3-8B compressed to 3-bit. We also introduce an optimized CUDA kernel, accelerating inference by up to 1.4x and reducing memory overhead through quantizing EoRA. Overall, EoRA offers a prompt solution for improving the accuracy of compressed models under varying user requirements, enabling more efficient and flexible deployment of LLMs. Code is available at this https URL .

</details>

---

### 43. [Training with Pseudo-Code for Instruction Following](https://arxiv.org/abs/2505.18011)

**基本信息**

- 🔗 arXiv: [`2505.18011`](https://arxiv.org/abs/2505.18011)
- 👥 作者: Prince Kumar, Rudra Murthy, Riyaz Bhat 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.18011.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通过伪代码增强来提升大型语言模型的指令遵循能力。这对于构建能够准确理解并执行复杂化学领域指令（如结构生成、反应推理）的“化学大模型”具有直接的技术指导意义。

**📖 中文摘要**

本文提出了一种训练时的方法，通过使用增强了伪代码表示的自然语言指令数据来微调大型语言模型，以改善其遵循指令的能力。论文发现，用伪代码表达指令时，模型能更有效地遵循指令，特别是当指令包含组合结构时。作者提出的方法在指令遵循、数学推理和常识推理等多个基准测试上取得了显著提升。这项研究直接关联到“化学大模型”的构建和优化，因为化学领域充满复杂的、结构化的符号表示（如SMILES、反应方程式）和操作流程。将化学领域的指令或问题转化为伪代码或形式化语言，可能显著提升化学大模型在分子设计、合成路线规划、性质预测等任务上的准确性和可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite rapid advances in the capabilities of Large Language Models (LLMs), they continue to struggle with following relatively simple and unambiguous instructions, particularly when compositional structure is involved. Recent work suggests that models may follow instructions more effectively when they are expressed in pseudo-code rather than natural language. However, writing pseudo-code programs can be tedious, and relying on few-shot demonstrations or inference-time code prompting is often unnatural for non-expert users of LLMs. To overcome these limitations, we propose a training time approach that fine-tunes LLMs using instruction-tuning data augmented with pseudo-code representations of natural language instructions paired with final responses. We evaluate our method on 12 publicly available benchmarks spanning instruction-following, mathematical reasoning, and commonsense reasoning, across six base models. Our results show that models trained with pseudo-code follow instructions more reliably, achieving relative gains of 8-21\% on instruction following benchmarks, while largely preserving and in some cases improving performance on mathematical and commonsense reasoning tasks, with an average gain of up to 30\% across all evaluated benchmarks.

</details>

---

### 44. [LLLMs: A Data-Driven Survey of Evolving Research on Limitations of Large Language Models](https://arxiv.org/abs/2505.19240)

**基本信息**

- 🔗 arXiv: [`2505.19240`](https://arxiv.org/abs/2505.19240)
- 👥 作者: Aida Kostikova, Zhipin Wang, Deidamea Bajri 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19240.pdf)

**💡 相关性分析**

满足标准3：论文是关于大型语言模型局限性的系统性综述，涵盖了推理、泛化、幻觉等多个关键主题。这对于“化学大模型”的研究具有重要的展望和指导意义，帮助领域研究者认清挑战并定位研究方向。

**📖 中文摘要**

本文对关于大型语言模型局限性的研究进行了数据驱动的系统性综述。通过分析大量ACL和arXiv论文，作者识别并聚类了LLM研究的各类局限性主题，如推理、泛化、幻觉、偏见和安全性等，并追踪了其随时间的变化趋势。这篇论文是一篇关于大模型研究的元分析，虽然不直接解决化学问题，但它全面梳理了当前大模型（包括潜在的专业领域大模型如“化学大模型”）所面临的核心挑战和前沿研究方向。对于任何计划构建或应用化学大模型的研究者来说，了解这些普遍存在的局限性（如幻觉、推理错误）以及相应的研究进展，是至关重要的背景知识。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language model (LLM) research has grown rapidly, along with increasing concern about their limitations. In this survey, we conduct a data-driven, semi-automated review of research on limitations of LLMs (LLLMs) from 2022 to early 2025 using a bottom-up approach. From a corpus of 250,000 ACL and arXiv papers, we identify 14,648 relevant papers using keyword filtering, LLM-based classification, validated against expert labels, and topic clustering (via two approaches, HDBSCAN+BERTopic and LlooM). We find that the share of LLM-related papers increases over fivefold in ACL and nearly eightfold in arXiv between 2022 and 2025. Since 2022, LLLMs research grows even faster, reaching over 30% of LLM papers by 2025. Reasoning remains the most studied limitation, followed by generalization, hallucination, bias, and security. The distribution of topics in the ACL dataset stays relatively stable over time, while arXiv shifts toward security risks, alignment, hallucinations, knowledge editing, and multimodality. We offer a quantitative view of trends in LLLMs research and release a dataset of annotated abstracts and a validated methodology, available at: this https URL .

</details>

---

### 45. [Silhouette-Driven Instance-Weighted $k$-means](https://arxiv.org/abs/2506.12878)

**基本信息**

- 🔗 arXiv: [`2506.12878`](https://arxiv.org/abs/2506.12878)
- 👥 作者: Aggelos Semoglou, Aristidis Likas, John Pavlopoulos
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.12878.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种改进的聚类算法。聚类是化学信息学和质谱数据分析中的基础工具，用于从高维数据中发现模式和结构。该算法通过提升聚类质量，可为“质谱结构推理”中的数据处理和特征提取环节提供更强大的技术支持。

**📖 中文摘要**

本文提出了K-Sil，一种基于轮廓系数的k-means变体算法。该算法在每次迭代中，使用轮廓分数的质心-边界代理来加权数据点，强调被明确分配的实例，同时降低边界点或噪声区域的权重。质心更新采用softmax加权平均的形式，并采用自适应温度进行校准。虽然这是一篇关于聚类算法的论文，但聚类和降维是化学信息学（尤其是质谱分析）中用于处理高维数据、发现模式、进行化合物分类或质谱峰对齐的基础技术。论文提出的改进聚类方法，对于从复杂的质谱数据中提取有意义的化学结构信息或进行样本分类具有潜在的应用价值，间接服务于“质谱结构推理”的数据分析环节。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Clustering is a fundamental unsupervised learning task with applications across a wide range of domains. Popular algorithms such as $k$-means are efficient and widely used, but can be sensitive to outliers, ambiguous boundary points, and heterogeneous cluster geometry, which may distort centroid estimates and yield suboptimal partitions. We introduce K-Sil, a silhouette-driven $k$-means variant that, at each iteration, weights points using a centroid-margin proxy for the silhouette score, emphasizing confidently assigned instances while down-weighting borderline or noisy regions. Centroid updates take the form of a softmax-weighted mean, and an adaptive temperature automatically calibrates the sharpness of the weight distribution using a cluster-balanced, macro-averaged, silhouette criterion. Under standard separation conditions, we establish a local convergence result for the induced weighted centroid updates. Experiments on 15 real-world datasets spanning tabular, biomedical, text, and image representations show consistent gains in internal validation metrics and typical improvements in external validation metrics over $k$-means and competitive instance-weighted baselines.

</details>

---

### 46. [AutoPCR: Automated Phenotype Concept Recognition by Prompting](https://arxiv.org/abs/2507.19315)

**基本信息**

- 🔗 arXiv: [`2507.19315`](https://arxiv.org/abs/2507.19315)
- 👥 作者: Yicheng Tao, Yuanhao Huang, Yiqun Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.19315.pdf)

**💡 相关性分析**

满足标准1：论文研究利用大型语言模型进行生物医学概念识别，其提示工程和无需本体特定训练的方法论，对于构建用于化学文本挖掘、分子信息抽取的“化学大模型”具有直接的技术参考价值。

**📖 中文摘要**

本文提出了AutoPCR，一种基于提示的、无需针对特定本体进行训练的表型概念识别方法。AutoPCR通过结合规则和神经标注策略进行实体抽取，利用SapBERT进行候选检索，并通过提示大型语言模型进行实体链接。在多个基准数据集上的实验表明，AutoPCR取得了最佳的平均性能和最稳健的表现。这项研究属于生物医学文本挖掘领域，其核心是使用大型语言模型进行生物医学实体识别和链接。虽然直接应用是表型，但其方法论——利用LLM和提示工程解决生物医学领域的结构化信息抽取问题——与“化学大模型”在化学文献挖掘、分子实体识别、反应条件提取等任务上的应用高度相似。它为如何构建和利用领域大模型（化学大模型）解决具体的文本信息抽取问题提供了可借鉴的技术框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Phenotype concept recognition (CR) is a fundamental task in biomedical text mining, enabling applications such as clinical diagnostics and knowledge graph construction. However, existing methods often require ontology-specific training and struggle to generalize across diverse text types and evolving biomedical terminology. We present AutoPCR, a prompt-based phenotype CR method that does not require ontology-specific training. AutoPCR performs CR in three stages: entity extraction using a hybrid of rule-based and neural tagging strategies, candidate retrieval via SapBERT, and entity linking through prompting a large language model. Experiments on four benchmark datasets show that AutoPCR achieves the best average and most robust performance across both mention-level and document-level evaluations, surpassing prior state-of-the-art methods. Further ablation and transfer studies demonstrate its inductive capability and generalizability to new ontologies.

</details>

---

### 47. [QCSE: A Pretrained Quantum Context-Sensitive Word Embedding for Natural Language Processing](https://arxiv.org/abs/2509.05729)

**基本信息**

- 🔗 arXiv: [`2509.05729`](https://arxiv.org/abs/2509.05729)
- 👥 作者: Charles M. Varmantchaonala, Niclas Götting, Nils-Erik Schütte 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.05729.pdf)

**💡 相关性分析**

满足标准1：论文研究量子计算与自然语言处理的交叉，提出量子上下文词嵌入模型。这为“化学大模型”的未来发展提供了一个极具前瞻性的方向：利用量子计算的优势来处理和表示化学信息，可能催生新一代的量子化学信息学模型。

**📖 中文摘要**

本文提出了一种预训练的量子上下文敏感词嵌入模型QCSE，用于自然语言处理。该模型利用量子系统的独特特性来学习语言中的上下文关系，实现了量子原生的上下文学习。论文引入了创新的上下文矩阵计算方法，旨在基于词语周围的上下文创建独特的表示。作者在低资源的非洲富拉尼语和英语语料库上进行了评估，结果表明QCSE不仅能够捕捉上下文敏感性，还能利用量子系统的表达能力来表示丰富的、上下文感知的语言信息。这项研究属于量子自然语言处理的前沿探索。虽然处于早期阶段，但它展示了将量子计算与NLP结合的新范式。对于“化学大模型”而言，量子计算本身就是模拟分子系统和化学反应的重要工具。探索量子启发的或量子原生的模型架构，可能为未来处理量子化学计算、分子模拟等任务的“化学大模型”开辟全新的可能性，属于前瞻性的交叉研究方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantum Natural Language Processing (QNLP) offers a novel approach to encoding and understanding the complexity of natural languages through the power of quantum computation. This paper presents a pretrained quantum context-sensitive embedding model, called QCSE, that captures context-sensitive word embeddings, leveraging the unique properties of quantum systems to learn contextual relationships in languages. The model introduces quantum-native context learning, enabling the utilization of quantum computers for linguistic tasks. Central to the proposed approach are innovative context matrix computation methods, designed to create unique, representations of words based on their surrounding linguistic context. Five distinct methods are proposed and tested for computing the context matrices, incorporating techniques such as exponential decay, sinusoidal modulation, phase shifts, and hash-based transformations. These methods ensure that the quantum embeddings retain context sensitivity, thereby making them suitable for downstream language tasks where the expressibility and properties of quantum systems are valuable resources. To evaluate the effectiveness of the model and the associated context matrix methods, evaluations are conducted on both a Fulani corpus, a low-resource African language, dataset of small size and an English corpus of slightly larger size. The results demonstrate that QCSE not only captures context sensitivity but also leverages the expressibility of quantum systems for representing rich, context-aware language information. The use of Fulani further highlights the potential of QNLP to mitigate the problem of lack of data for this category of languages. This work underscores the power of quantum computation in natural language processing (NLP) and opens new avenues for applying QNLP to real-world linguistic challenges across various tasks and domains.

</details>

---

### 48. [Global Minimizers of Sigmoid Contrastive Loss](https://arxiv.org/abs/2509.18552)

**基本信息**

- 🔗 arXiv: [`2509.18552`](https://arxiv.org/abs/2509.18552)
- 👥 作者: Kiril Bangachev, Guy Bresler, Iliyas Noman 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.18552.pdf)

**💡 相关性分析**

满足标准1：论文对视觉-语言对比学习模型（如SigLIP）进行理论分析，对比学习是构建关联化学结构、光谱、性质等多模态数据的“化学大模型”的关键技术。论文的理论发现有助于优化此类化学大模型的训练和目标函数设计。

**📖 中文摘要**

本文从理论上分析了在对比预训练中使用可训练逆温度和偏置参数的优势，特别是在Sigmoid损失函数下。作者研究了Google DeepMind近期模型SigLIP和SigLIP2中实现的同步机制，并理论证明了温度和偏置如何驱动损失函数趋于零。论文引入了一种称为“星座”的新组合对象来表征最优配置，并利用该表征从理论上解释了SigLIP在检索任务上的成功、SigLIP和CLIP中存在的模态差距，以及产生高质量表示所需的维度。这项工作是对当前流行的视觉-语言对比学习模型（如CLIP, SigLIP）的理论深化。虽然不直接针对化学，但对比学习是构建多模态“化学大模型”（如关联分子结构、质谱图、文本描述）的核心技术之一。论文对对比学习损失函数和模型参数作用的深刻理论洞察，对于设计和优化化学领域的多模态表示学习模型具有重要的指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The meta-task of obtaining and aligning representations through contrastive pretraining is steadily gaining importance since its introduction in CLIP and ALIGN. In this paper we theoretically explain the advantages of synchronizing with trainable inverse temperature and bias under the sigmoid loss, as implemented in the recent SigLIP and SigLIP2 models of Google DeepMind. Temperature and bias can drive the loss function to zero for a rich class of configurations that we call $(\mathsf{m}, \mathsf{b}_{\mathsf{rel}})$-Constellations. $(\mathsf{m}, \mathsf{b}_{\mathsf{rel}})$-Constellations are a novel combinatorial object related to spherical codes and are parametrized by a margin $\mathsf{m}$ and relative bias $\mathsf{b}_{\mathsf{rel}}$. We use our characterization of constellations to theoretically justify the success of SigLIP on retrieval, to explain the modality gap present in SigLIP and CLIP, and to identify the necessary dimension for producing high-quality representations. Finally, we propose a reparameterization of the sigmoid loss with explicit relative bias, which improves training dynamics in experiments with synthetic data.

</details>

---

### 49. [Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search](https://arxiv.org/abs/2512.09566)

**基本信息**

- 🔗 arXiv: [`2512.09566`](https://arxiv.org/abs/2512.09566)
- 👥 作者: Junkai Ji, Zhangfan Yang, Dong Xu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.09566.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分子设计的生成框架，这直接属于“化学大模型”的研究范畴，因为它利用分子语言模型和强化学习等AI技术进行分子生成和优化。

**📖 中文摘要**

本文提出Trio，一个用于闭环靶向分子设计的分子生成框架。该框架整合了基于片段的分子语言建模、强化学习和蒙特卡洛树搜索。其核心是通过三个关键组件实现上下文感知的片段组装，强制执行物理化学和合成可行性，并在蛋白质结合口袋内引导新颖化学型探索与有前景中间体利用之间的平衡搜索。实验结果表明，Trio能够可靠地生成化学有效且药理学增强的配体，在结合亲和力、类药性和合成可及性方面优于现有方法，同时将分子多样性扩展了四倍以上。该工作通过结合泛化性、合理性和可解释性，建立了一个闭环生成范式，为AI驱动的药物发现新时代提供了变革性基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drug discovery is a time-consuming and expensive process, with traditional high-throughput and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in generative modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate generalization, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular generation framework integrating fragment-based molecular language modeling, reinforcement learning, and Monte Carlo tree search, for effective and interpretable closed-loop targeted molecular design. Through the three key components, Trio enables context-aware fragment assembly, enforces physicochemical and synthetic feasibility, and guides a balanced search between the exploration of novel chemotypes and the exploitation of promising intermediates within protein binding pockets. Experimental results show that Trio reliably achieves chemically valid and pharmacologically enhanced ligands, outperforming state-of-the-art approaches with improved binding affinity (+7.85%), drug-likeness (+11.10%) and synthetic accessibility (+12.05%), while expanding molecular diversity more than fourfold. By combining generalization, plausibility, and interpretability, Trio establishes a closed-loop generative paradigm that redefines how chemical space can be navigated, offering a transformative foundation for the next era of AI-driven drug discovery.

</details>

---

### 50. [Pretrained battery transformer (PBT): A foundation model for universal battery life prediction](https://arxiv.org/abs/2512.16334)

**基本信息**

- 🔗 arXiv: [`2512.16334`](https://arxiv.org/abs/2512.16334)
- 👥 作者: Ruifeng Tan, Weixiang Hong, Jia Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.16334.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于电池寿命预测的预训练Transformer基础模型。这属于“化学大模型”在材料科学和化学信息学领域的应用，旨在利用大规模数据学习化学/材料系统的通用表征。

**📖 中文摘要**

本文介绍了预训练电池变压器（PBT），一个用于电池寿命预测的基础模型。PBT通过编码电池知识的专家混合层，从异构数据中学习可迁移的表征。该模型在13个锂离子电池数据集上进行预训练，随后通过迁移学习适应下游电池寿命预测任务。在涵盖锂离子、钠离子和锌离子电池的15个数据集上，PBT实现了最先进的性能，平均超越最强竞争方法21.8%。这项研究建立了第一个用于电池寿命预测的基础模型，并为构建通用的电池寿命预测系统提供了一条可扩展的途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early prediction of battery cycle life is essential for improving battery design, manufacturing, and deployment. However, despite encouraging results with machine learning, progress remains constrained by scarce data and data heterogeneity across battery chemistries, specifications, formation protocols, and operating conditions. Although transfer learning has been widely explored to alleviate these challenges, its effectiveness is constrained by the lack of a foundation model that can capture broadly transferable knowledge from diverse battery life data. This gap persists because integration of heterogeneous battery datasets under data scarcity is inherently challenging. Here we introduce the pretrained battery transformer (PBT), a foundation model for battery life prediction that incorporates battery-knowledge-encoded mixture-of-experts layers to learn transferable representations from heterogeneous data. PBT is pretrained on 13 lithium-ion battery datasets and subsequently adapted to downstream battery life prediction tasks through transfer learning. Across 15 datasets covering 977 batteries and 533 sets of aging conditions from lithium-ion, sodium-ion and zinc-ion batteries, PBT achieves state-of-the-art performance, surpassing the strongest competing method by 21.8% on average, with gains of up to 86.9%. Our study establishes the first foundation model for battery life prediction and provides a scalable route towards universal battery lifetime prediction systems, with broader implications for other scientific and technological domains characterized by scarce and heterogeneous data.

</details>

---

### 51. [Sampling via Stochastic Interpolants by Langevin-based Velocity and Initialization Estimation in Flow ODEs](https://arxiv.org/abs/2601.08527)

**基本信息**

- 🔗 arXiv: [`2601.08527`](https://arxiv.org/abs/2601.08527)
- 👥 作者: Chenguang Duan, Yuling Jiao, Gabriele Steidl 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.08527.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于从化学和物理系统中常见的非归一化玻尔兹曼密度进行采样的新算法。这属于“化学大模型”和计算化学中分子模拟和采样方法的研究范畴，是化学信息学和计算化学的基础问题。

**📖 中文摘要**

本文提出了一种基于概率流常微分方程（ODE）的新方法，用于从非归一化的玻尔兹曼密度中采样。该方法的关键创新是使用一系列朗之万采样器来实现流的有效模拟。具体来说，这些朗之万采样器被用于（i）在中间时间从插值分布生成样本，以及（ii）从这些中间时间开始，构建控制概率流ODE的速度场的鲁棒估计器。理论上，我们为两个朗之万组件提供了收敛保证，并为概率流ODE建立了非渐近收敛速率。广泛的数值实验证明了该方法在跨维度范围具有挑战性的多峰分布上的效率，以及其在贝叶斯推理任务中的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a novel method for sampling from unnormalized Boltzmann densities based on a probability flow ordinary differential equation (ODE) derived from linear stochastic interpolants. The key innovation of our approach is the use of a sequence of Langevin samplers to enable efficient simulation of the flow. Specifically, these Langevin samplers are employed (i) to generate samples from the interpolant distribution at intermediate times and (ii) to construct, starting from these intermediate times, a robust estimator of the velocity field governing the probability flow ODE. Theoretically, we provide convergence guarantees for both Langevin components, and establish a non-asymptotic convergence rate for the probability flow ODE. Extensive numerical experiments demonstrate the efficiency of the proposed method on challenging multimodal distributions across a range of dimensions, as well as its effectiveness in Bayesian inference tasks.

</details>

---

### 52. [NMIRacle: Multi-modal Generative Molecular Elucidation from IR and NMR Spectra](https://arxiv.org/abs/2512.19733)

**基本信息**

- 🔗 arXiv: [`2512.19733`](https://arxiv.org/abs/2512.19733)
- 👥 作者: Federico Ottomano, Yingzhen Li, Alex M. Ganose
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.19733.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”主题，提出了一种从IR和NMR光谱生成分子结构的AI框架。

**📖 中文摘要**

本文提出了一种名为NMIRacle的两阶段生成式框架，用于从红外（IR）和核磁共振（NMR）光谱数据中直接推断分子结构。该框架首先学习从片段表示重建分子结构，然后通过一个光谱编码器将输入光谱映射到潜在嵌入中，用以条件化预训练的生成器，从而实现从光谱到分子的直接生成。这项工作直接针对“质谱结构推理”这一核心主题，旨在解决化学信息学中长期存在的分子结构解析挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular structure elucidation from spectroscopic data is a long-standing challenge in Chemistry, traditionally requiring expert interpretation. We introduce NMIRacle, a two-stage generative framework that builds upon recent paradigms in AI-driven spectroscopy with minimal assumptions. In the first stage, NMIRacle learns to reconstruct molecular structures from count-aware fragment representations, capturing both fragment identities and their occurrences. In the second stage, a spectral encoder maps input spectra (IR, 1H-NMR, 13C-NMR) into a latent embedding used to condition the pre-trained generator, which is fine-tuned for direct spectra-to-molecule generation. This formulation bridges fragment-level chemical modeling with spectral evidence, yielding accurate molecular predictions. Empirical results demonstrate that NMIRacle outperforms existing baselines on molecular elucidation, while maintaining robust performance across increasing levels of molecular complexity.

</details>

---

### 53. [Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)](https://arxiv.org/abs/2602.22248)

**基本信息**

- 🔗 arXiv: [`2602.22248`](https://arxiv.org/abs/2602.22248)
- 👥 作者: Julia Gonski, Jenni Ott, Shiva Abbaszadeh 等100人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22248.pdf)

**💡 相关性分析**

满足标准3：论文作为一篇前瞻性/综述性白皮书，包含了关于AI/ML模型（可涵盖化学大模型）与先进硬件（如量子计算）结合以解决科学大数据问题的重要讨论和展望。

**📖 中文摘要**

这篇白皮书探讨了下一代粒子物理实验在数据获取和处理方面面临的挑战，并强调了利用新兴技术（如人工智能/机器学习、异构加速器系统和量子处理）的重要性。文中特别指出，在极端环境和操作约束下，实现实时推理、智能数据缩减和高效处理架构至关重要。虽然论文主题是粒子物理，但其核心论点——将AI/ML（包括潜在的化学信息学模型）与专用硬件（如边缘计算设备、量子处理器）相结合以应对科学数据挑战——与构建和部署“化学大模型”所需的技术栈和跨学科思路高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The next generation of particle physics experiments will face a new era of challenges in data acquisition, due to unprecedented data rates and volumes along with extreme environments and operational constraints. Harnessing this data for scientific discovery demands real-time inference and decision-making, intelligent data reduction, and efficient processing architectures beyond current capabilities. Crucial to the success of this experimental paradigm are several emerging technologies, such as artificial intelligence and machine learning (AI/ML), silicon microelectronics, and the advent of quantum algorithms and processing. Their intersection includes areas of research such as low-power and low-latency devices for edge computing, heterogeneous accelerator systems, reconfigurable hardware, novel codesign and synthesis strategies, readout for cryogenic or high-radiation environments, and analog computing. This white paper presents a community-driven vision to identify and prioritize research and development opportunities in hardware-based ML systems and corresponding physics applications, contributing towards a successful transition to the new data frontier of fundamental science.

</details>

---

## 📊 数据统计
- 累计运行天数：26
- 累计论文数量：1921

## 📝 历史记录

> 暂无历史数据

