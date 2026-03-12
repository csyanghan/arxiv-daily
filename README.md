# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-12 13:01:37

## 📅 2026-03-12 (今日最新)

**相关论文数：46**

### 1. [Evaluating Progress in Graph Foundation Models: A Comprehensive Benchmark and New Insights](https://arxiv.org/abs/2603.10033)

**基本信息**

- 🔗 arXiv: [`2603.10033`](https://arxiv.org/abs/2603.10033)
- 👥 作者: Xingtong Yu, Shenghua Ye, Ruijuan Liang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10033.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图基础模型（Graph Foundation Models），这是一种特定类型的‘大模型’。虽然论文未直接提及‘化学大模型’，但其研究的图基础模型在概念、方法论和评估框架上与化学信息学中用于分子表示和性质预测的图神经网络大模型高度相关。论文提出的二维评估范式（主题域和格式域）对于理解和评估化学领域大模型的泛化能力具有直接的借鉴意义。

**📖 中文摘要**

这篇论文提出了一个用于评估图基础模型（Graph Foundation Models, GFM）的新基准。图基础模型通过在不同图数据上进行预训练来获取可迁移的知识，以适配各种下游任务。该研究指出，图数据的领域偏移本质上是二维的：图不仅在描述的内容（主题领域）上不同，而且在表示形式（格式领域）上也不同。现有的GFM基准大多只改变主题领域，从而模糊了知识在这两个维度上的迁移情况。本文提出的新基准联合评估了GFM全流程（包括多领域自监督预训练和少样本下游适配）中的主题和格式差异，并对快速发展的GFM领域中的最新模型进行了及时评估。该协议支持在四种设置下进行受控评估，从而将语义泛化与对表示偏移的鲁棒性区分开来。这项工作为图基础模型的系统评估和比较提供了框架和见解，其方法和基准对于理解和推进化学信息学等领域中基于图的分子表示和性质预测模型（可视为化学大模型的一种形式）的发展具有参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph foundation models (GFM) aim to acquire transferable knowledge by pre-training on diverse graphs, which can be adapted to various downstream tasks. However, domain shift in graphs is inherently two-dimensional: graphs differ not only in what they describe (topic domains) but also in how they are represented (format domains). Most existing GFM benchmarks vary only topic domains, thereby obscuring how knowledge transfers across both dimensions. We present a new benchmark that jointly evaluates topic and format gaps across the full GFM pipeline, including multi-domain self-supervised pre-training and few-shot downstream adaptation, and provides a timely evaluation of recent GFMs in the rapidly evolving landscape. Our protocol enables controlled assessment in four settings: (i) pre-training on diverse topics and formats, while adapting to unseen downstream datasets; (ii) same pre-training as in (i), while adapting to seen datasets; (iii) pre-training on a single topic domain, while adapting to other topics; (iv) pre-training on a base format, while adapting to other formats. This two-axis evaluation disentangles semantic generalization from robustness to representational shifts. We conduct extensive evaluations of eight state-of-the-art GFMs on 33 datasets spanning seven topic domains and six format domains, surfacing new empirical observations and practical insights for future research. Codes/data are available at this https URL .

</details>

---

### 2. [A Survey of Weight Space Learning: Understanding, Representation, and Generation](https://arxiv.org/abs/2603.10090)

**基本信息**

- 🔗 arXiv: [`2603.10090`](https://arxiv.org/abs/2603.10090)
- 👥 作者: Xiaolong Han, Zehong Wang, Bo Zhao 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10090.pdf)

**💡 相关性分析**

满足标准1：论文的核心主题是‘权重空间学习’，这是理解和分析大型神经网络（包括化学信息学等领域的大模型）内部结构和行为的一个基础且前沿的方向。论文系统地总结了如何表示、理解和生成模型权重，这些研究直接关系到‘化学大模型’的可解释性、模型压缩、知识迁移和高效训练等核心问题。

**📖 中文摘要**

这篇综述论文首次对“权重空间学习”（Weight Space Learning, WSL）这一新兴研究方向进行了统一的分类和总结。WSL将神经网络的权重本身视为一个有意义、可分析和建模的领域，而不仅仅是训练的最终产物。论文将现有方法分为三个核心维度：权重空间理解（研究权重的几何和对称性）、权重空间表示（学习模型权重的嵌入）和权重空间生成（通过超网络或生成模型合成新权重）。文章进一步展示了这些进展如何推动实际应用，包括模型检索、持续和联邦学习、神经架构搜索以及无数据重建。通过将分散的进展整合到一个连贯的框架下，本综述强调了权重空间作为一个可学习的、结构化的领域，在模型分析、迁移和权重生成方面日益增长的影响力。这项工作为理解和构建包括化学领域在内的各类‘大模型’提供了底层权重层面的理论基础和方法论视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural network weights are typically viewed as the end product of training, while most deep learning research focuses on data, features, and architectures. However, recent advances show that the set of all possible weight values (weight space) itself contains rich structure: pretrained models form organized distributions, exhibit symmetries, and can be embedded, compared, or even generated. Understanding such structures has tremendous impact on how neural networks are analyzed and compared, and on how knowledge is transferred across models, beyond individual training instances. This emerging research direction, which we refer to as Weight Space Learning (WSL), treats neural weights as a meaningful domain for analysis and modeling. This survey provides the first unified taxonomy of WSL. We categorize existing methods into three core dimensions: Weight Space Understanding (WSU), which studies the geometry and symmetries of weights; Weight Space Representation (WSR), which learns embeddings over model weights; and Weight Space Generation (WSG), which synthesizes new weights through hypernetworks or generative models. We further show how these developments enable practical applications, including model retrieval, continual and federated learning, neural architecture search, and data-free reconstruction. By consolidating fragmented progress under a coherent framework, this survey highlights weight space as a learnable, structured domain with growing impact across model analysis, transferring, and weight generation. We release an accompanying resource at this https URL .

</details>

---

### 3. [Equivariant Asynchronous Diffusion: An Adaptive Denoising Schedule for Accelerated Molecular Conformation Generation](https://arxiv.org/abs/2603.10093)

**基本信息**

- 🔗 arXiv: [`2603.10093`](https://arxiv.org/abs/2603.10093)
- 👥 作者: Junyi An, Chao Qu, Yun-Fei Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10093.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于3D分子生成的新型扩散模型（EAD），这直接属于“化学大模型”的研究范畴，是化学信息学中利用生成模型进行分子设计的前沿方向。

**📖 中文摘要**

本文提出了一种名为等变异步扩散（EAD）的新型扩散模型，用于3D分子生成。该模型结合了异步自回归模型和同步扩散模型的优点，通过异步去噪调度来更好地捕捉分子的层次结构，同时保持分子级别的视野。为了解决分子层次关系的复杂性，论文还提出了一种动态调度机制来自适应地确定去噪时间步。实验结果表明，EAD在3D分子生成方面达到了最先进的性能。该研究直接围绕“化学大模型”这一主题，特别是针对分子生成这一化学信息学核心任务，属于核心主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent 3D molecular generation methods primarily use asynchronous auto-regressive or synchronous diffusion models. While auto-regressive models build molecules sequentially, they're limited by a short horizon and a discrepancy between training and inference. Conversely, synchronous diffusion models denoise all atoms at once, offering a molecule-level horizon but failing to capture the causal relationships inherent in hierarchical molecular structures. We introduce Equivariant Asynchronous Diffusion (EAD) to overcome these limitations. EAD is a novel diffusion model that combines the strengths of both approaches: it uses an asynchronous denoising schedule to better capture molecular hierarchy while maintaining a molecule-level horizon. Since these relationships are often complex, we propose a dynamic scheduling mechanism to adaptively determine the denoising timestep. Experimental results show that EAD achieves state-of-the-art performance in 3D molecular generation.

</details>

---

### 4. [Unbalanced Optimal Transport Dictionary Learning for Unsupervised Hyperspectral Image Clustering](https://arxiv.org/abs/2603.10132)

**基本信息**

- 🔗 arXiv: [`2603.10132`](https://arxiv.org/abs/2603.10132)
- 👥 作者: Joshua Lentz, Nicholas Karris, Alex Cloninger 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10132.pdf)

**💡 相关性分析**

满足标准1：论文提出的“不平衡Wasserstein重心字典学习”方法是一种用于高维数据（如光谱）的无监督表示学习技术。虽然应用场景是高光谱图像，但其方法论与化学信息学中处理质谱等高维化学数据的核心挑战（降维、特征提取、聚类）高度相关，可视为一种通用的数据分析和结构推理工具。

**📖 中文摘要**

本文提出了一种利用不平衡Wasserstein重心进行字典学习的方法，用于高光谱图像的无监督聚类。该方法旨在学习高维光谱数据的低维表示，以改进场景分割。虽然论文的应用领域是图像处理，但其核心方法——在Wasserstein空间中利用字典学习进行数据降维和表示学习——与化学信息学中处理高维光谱数据（如质谱）的范式有很强的相似性。质谱数据同样具有高维、复杂的特点，需要有效的降维和特征提取方法来进行结构推理或分类。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hyperspectral images capture vast amounts of high-dimensional spectral information about a scene, making labeling an intensive task that is resistant to out-of-the-box statistical methods. Unsupervised learning of clusters allows for automated segmentation of the scene, enabling a more rapid understanding of the image. Partitioning the spectral information contained within the data via dictionary learning in Wasserstein space has proven an effective method for unsupervised clustering. However, this approach requires balancing the spectral profiles of the data, blurring the classes, and sacrificing robustness to outliers and noise. In this paper, we suggest improving this approach by utilizing unbalanced Wasserstein barycenters to learn a lower-dimensional representation of the underlying data. The deployment of spectral clustering on the learned representation results in an effective approach for the unsupervised learning of labels.

</details>

---

### 5. [Improving TabPFN's Synthetic Data Generation by Integrating Causal Structure](https://arxiv.org/abs/2603.10254)

**基本信息**

- 🔗 arXiv: [`2603.10254`](https://arxiv.org/abs/2603.10254)
- 👥 作者: Davide Tugnoli, Andrea De Lorenzo, Marco Virgolin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10254.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究对象是TabPFN，这是一个专门为表格数据设计的化学信息学基础模型。研究重点是如何改进该模型生成合成数据的能力，这直接属于“化学大模型”的研究范畴，特别是针对模型的可解释性和可靠性进行优化。

**📖 中文摘要**

本文研究了如何通过整合因果结构来改进TabPFN（一种用于表格数据的先验数据拟合网络）的合成数据生成能力。TabPFN是一种能够生成高质量合成表格数据的化学信息学基础模型。论文指出，当特征顺序与因果结构冲突时，模型会产生虚假相关性，损害其生成数据和保留因果效应的能力。为此，作者提出了两种将因果结构整合到TabPFN生成过程中的方法：基于有向无环图（DAG）的条件采样和基于部分有向无环图（CPDAG）的策略。实验表明，整合因果结构可以提高合成数据的质量和稳定性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic tabular data generation addresses data scarcity and privacy constraints in a variety of domains. Tabular Prior-Data Fitted Network (TabPFN), a recent foundation model for tabular data, has been shown capable of generating high-quality synthetic tabular data. However, TabPFN is autoregressive: features are generated sequentially by conditioning on the previous ones, depending on the order in which they appear in the input data. We demonstrate that when the feature order conflicts with causal structure, the model produces spurious correlations that impair its ability to generate synthetic data and preserve causal effects. We address this limitation by integrating causal structure into TabPFN's generation process through two complementary approaches: Directed Acyclic Graph (DAG)-aware conditioning, which samples each variable given its causal parents, and a Completed Partially Directed Acyclic Graph (CPDAG)-based strategy for scenarios with partial causal knowledge. We evaluate these approaches on controlled benchmarks and six CSuite datasets, assessing structural fidelity, distributional alignment, privacy preservation, and Average Treatment Effect (ATE) preservation. Across most settings, DAG-aware conditioning improves the quality and stability of synthetic data relative to vanilla TabPFN. The CPDAG-based strategy shows moderate improvements, with effectiveness depending on the number of oriented edges. These results indicate that injecting causal structure into autoregressive generation enhances the reliability of synthetic tabular data.

</details>

---

### 6. [How to make the most of your masked language model for protein engineering](https://arxiv.org/abs/2603.10302)

**基本信息**

- 🔗 arXiv: [`2603.10302`](https://arxiv.org/abs/2603.10302)
- 👥 作者: Calvin McCarter, Nick Bhattacharya, Sebastian W. Ober 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10302.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化蛋白质语言模型（一种特定领域的化学大模型）的采样策略，以用于蛋白质/抗体工程。这直接涉及如何利用和引导大模型进行分子设计和优化，是化学大模型在生物分子领域的核心应用。

**📖 中文摘要**

本文针对蛋白质工程中的关键问题——如何从蛋白质语言模型中最佳采样以优化目标生物学特性——提出了系统性的解决方案。作者提出了一种用于掩码语言模型（MLMs）的灵活有效的采样方法，即随机束搜索，该方法利用MLM高效评估序列整个1-编辑邻域的伪困惑度。通过将生成重新定义为对整个序列的评估，该方法能够灵活地指导多目标优化。论文还报告了在抗体工程场景下进行的广泛体外头对头评估结果，表明采样方法的选择与模型本身的选择至少同等重要。

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

满足标准2：论文提出了一种用于质谱成像（MSI）数据峰值挑选的新方法，这是一种专门用于质谱分析数据处理和特征选择的工具/方法，与‘质谱结构推理’主题直接相关。

**📖 中文摘要**

本文提出了一种用于质谱成像（MSI）数据峰值挑选的新方法。MSI生成复杂的高维数据，有效的峰值挑选对于减少数据量同时保留有意义的生物信息至关重要。现有方法在不同数据集上表现不一致，且评估通常局限于合成数据或手动选择的离子图像，不能完全代表MSI中的真实挑战。为了解决这些限制，作者提出了一种基于自动编码器的空间自监督峰值学习神经网络，该网络通过利用空间和光谱信息学习注意力掩码来选择具有空间结构的峰值。此外，作者引入了一种基于专家标注分割掩码的评估程序，允许对峰值挑选性能进行更具代表性和空间基础的评估。该方法在四个不同的公共MSI数据集上进行了评估，结果表明其通过选择空间结构化的峰值，性能优于最先进的峰值挑选方法。这项工作突出了在质谱分析中利用空间自监督学习进行结构化特征选择的价值。

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

满足标准1：论文在化学信息学子领域（分子溶解度预测）评估了其提出的SCORE架构，该架构作为通用的深度建模方法，与构建用于分子表示与性质预测的化学大模型核心主题直接相关。

**📖 中文摘要**

本文提出SCORE（Skip-Connection ODE Recurrent Embedding），一种用离散循环更新替代经典层堆叠的深度神经网络架构。其核心思想是迭代应用一个共享的神经块，采用受常微分方程启发的收缩更新公式。该方法被评估于图神经网络（用于ESOL分子溶解度预测）、多层感知机和Transformer语言模型。论文明确指出在ESOL分子溶解度数据集上进行了评估，该数据集属于化学信息学领域，涉及分子性质预测。SCORE框架作为一种通用的深度建模方法，其评估案例直接关联化学信息学中的分子表示学习与性质预测任务，为构建或改进化学大模型（如用于分子性质预测的图神经网络）提供了新的架构思路。

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

满足标准1：论文提出并理论分析了一类新的生成模型框架（梯度流漂移），该框架专注于密度估计和基于梯度的数据生成。这与构建用于分子结构生成、质谱数据生成或增强的化学大模型的核心主题在方法论上直接相关。

**📖 中文摘要**

本文提出了一个名为梯度流漂移（Gradient Flow Drifting）的生成模型新家族的统一数学框架。该框架证明了最近提出的漂移模型（Drifting Model）与在核密度估计近似下的前向KL散度的Wasserstein梯度流之间的等价性。具体而言，漂移模型的漂移场等于KDE对数密度梯度之差。此外，该广义生成模型家族还包括基于MMD的生成器，它们是不同散度在KDE近似下的Wasserstein梯度流的特例。论文提供了简明的可识别性证明和理论基础的混合散度策略，结合了反向KL和χ²散度梯度流，以避免模式崩溃和模式模糊，并将该方法扩展到黎曼流形上。在合成基准上的初步实验验证了该框架。论文的核心是提出并理论分析了一类新的生成模型，这类模型通过密度估计和梯度流进行数据生成，与化学信息学中用于分子生成或质谱数据生成的化学大模型在方法论上高度相关。

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

满足标准1：论文核心研究如何利用预训练语言模型（PLMs）和大型语言模型（LLMs）来增强和改进主题模型，这直接关联到利用大模型进行语义表示和结构分析，与化学信息学中利用大模型处理化学文本或分子表示的主题相关。

**📖 中文摘要**

本文研究如何将预训练语言模型嵌入集成到主题模型中，以重塑主题捕获语义结构的方式。经典模型如LDA从词共现统计中推导主题，而PLM增强模型将这些统计锚定到预训练嵌入空间，施加了一个也倾向于语义相似词聚类的先验。这种结构差异可以通过主题词的主题相关性和分类相似性这两个心理语言学维度来捕捉。为了在主题模型中解开这些维度，作者使用基于LLM的注释构建了一个大型合成词对基准，并训练了一个神经评分函数。该评分器被应用于跨多个语料库和主题模型家族的全面评估，揭示了不同模型家族在其主题中捕获了不同的语义结构。本文建立相似性和相关性作为主题模型评估的基本轴，并提供了一个可靠的流程来表征不同模型家族和语料库的这些特性。这项工作涉及使用大型语言模型进行语义表示和评估，与构建和理解化学大模型（例如用于化学文献主题挖掘或分子描述符生成的模型）中嵌入表示的学习与评估相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The recent advancement of large language models has spurred a growing trend of integrating pre-trained language model (PLM) embeddings into topic models, fundamentally reshaping how topics capture semantic structure. Classical models such as Latent Dirichlet Allocation (LDA) derive topics from word co-occurrence statistics, whereas PLM-augmented models anchor these statistics to pre-trained embedding spaces, imposing a prior that also favours clustering of semantically similar words. This structural difference can be captured by the psycholinguistic dimensions of thematic relatedness and taxonomic similarity of the topic words. To disentangle these dimensions in topic models, we construct a large synthetic benchmark of word pairs using LLM-based annotation to train a neural scoring function. We apply this scorer to a comprehensive evaluation across multiple corpora and topic model families, revealing that different model families capture distinct semantic structure in their topics. We further demonstrate that similarity and relatedness scores successfully predict downstream task performance depending on task requirements. This paper establishes similarity and relatedness as essential axes for topic model evaluation and provides a reliable pipeline for characterising these across model families and corpora.

</details>

---

### 11. [Reinforcement Learning with Conditional Expectation Reward](https://arxiv.org/abs/2603.10624)

**基本信息**

- 🔗 arXiv: [`2603.10624`](https://arxiv.org/abs/2603.10624)
- 👥 作者: Changyi Xiao, Caijun Xu, Yixin Cao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10624.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种基于大语言模型自我验证的强化学习奖励机制（CER），用于改进模型的推理能力。这种方法论与训练和优化用于复杂科学推理任务（如质谱结构推理）的化学大模型直接相关。

**📖 中文摘要**

本文提出了条件期望奖励（Conditional Expectation Reward, CER），用于增强大型语言模型的推理能力。CER利用大语言模型自身作为隐式验证器，计算在生成答案条件下生成参考答案的期望似然。与产生二元反馈的基于规则的验证器不同，CER提供了一个软的、分级的奖励信号，反映了不同程度的正确性，使其更适合答案正确性程度不一的任务。实验结果表明，CER在广泛的推理任务（包括数学和一般领域）上都有效，表明CER作为一种灵活且通用的验证机制。该方法通过大模型自我评估来提供训练信号，是构建和优化用于复杂推理任务（如质谱解析或化学反应预测）的化学大模型的一种潜在技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has proven effective in enhancing the reasoning capabilities of large language models, particularly in domains such as mathematics where reliable rule-based verifiers can be constructed. However, the reliance on handcrafted, domain-specific verification rules substantially limits the applicability of RLVR to general reasoning domains with free-form answers, where valid answers often exhibit significant variability, making it difficult to establish complete and accurate rules. To address this limitation, we propose Conditional Expectation Reward (CER), which leverages the large language model itself as an implicit verifier, and is therefore applicable to general domains and eliminates the need for external verifiers or auxiliary models. CER is defined as the expected likelihood of generating the reference answer conditioned on the generated answer. In contrast to rule-based verifiers that yield binary feedback, CER provides a soft, graded reward signal that reflects varying degrees of correctness, making it better suited to tasks where answers vary in correctness. Experimental results demonstrate that CER is effective across a wide range of reasoning tasks, spanning both mathematical and general domains, indicating that CER serves as a flexible and general verification mechanism. The code is available at this https URL .

</details>

---

### 12. [How To Embed Matters: Evaluation of EO Embedding Design Choices](https://arxiv.org/abs/2603.10658)

**基本信息**

- 🔗 arXiv: [`2603.10658`](https://arxiv.org/abs/2603.10658)
- 👥 作者: Luis Gilch, Isabelle Wittmann, Maximilian Nitsche 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10658.pdf)

**💡 相关性分析**

满足标准1：论文系统研究了如何从大规模预训练模型（基础模型）中提取、聚合和利用嵌入表示，以服务于下游任务。这种方法论与化学信息学中利用化学大模型（如分子Transformer）生成分子表示，并用于性质预测、虚拟筛选等任务的核心主题直接相关。

**📖 中文摘要**

本文对地理空间基础模型（GeoFM）嵌入设计在EO工作流程中的影响进行了系统分析。利用NeuCo-Bench，作者研究了骨干架构、预训练策略、表示深度、空间聚合和表示组合如何影响EO任务性能。研究表明，可以将GeoFM嵌入聚合为比原始输入数据小500倍以上的固定大小表示。跨模型发现了一致的趋势：具有均值池化的Transformer骨干提供了强大的默认嵌入，中间ResNet层可以优于最终层，自监督目标表现出任务特定的优势，结合来自不同目标的嵌入通常能提高鲁棒性。这项工作系统地评估了如何从基础模型中提取和构建有效的嵌入表示，这与化学信息学中如何从化学大模型（如分子Transformer）中获取和利用分子表示进行下游任务（如性质预测）的方法论高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Earth observation (EO) missions produce petabytes of multispectral imagery, increasingly analyzed using large Geospatial Foundation Models (GeoFMs). Alongside end-to-end adaptation, workflows make growing use of intermediate representations as task-agnostic embeddings, enabling models to compute representations once and reuse them across downstream tasks. Consequently, when GeoFMs act as feature extractors, decisions about how representations are obtained, aggregated, and combined affect downstream performance and pipeline scalability. Understanding these trade-offs is essential for scalable embedding-based EO workflows, where compact embeddings can replace raw data while remaining broadly useful. We present a systematic analysis of embedding design in GeoFM-based EO workflows. Leveraging NeuCo-Bench, we study how backbone architecture, pretraining strategy, representation depth, spatial aggregation, and representation combination influence EO task performance. We demonstrate the usability of GeoFM embeddings by aggregating them into fixed-size representations more than 500x smaller than the raw input data. Across models, we find consistent trends: transformer backbones with mean pooling provide strong default embeddings, intermediate ResNet layers can outperform final layers, self-supervised objectives exhibit task-specific strengths, and combining embeddings from different objectives often improves robustness.

</details>

---

### 13. [EvoSchema: Towards Text-to-SQL Robustness Against Schema Evolution](https://arxiv.org/abs/2603.10697)

**基本信息**

- 🔗 arXiv: [`2603.10697`](https://arxiv.org/abs/2603.10697)
- 👥 作者: Tianshu Zhang, Kun Qian, Siddhartha Sahai 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10697.pdf)

**💡 相关性分析**

满足标准1：论文专注于评估和提升大型语言模型在处理动态、演化的结构化数据（数据库模式）时的鲁棒性和适应性。这与化学信息学中利用大模型处理化学数据库查询、分子/反应检索以及结构推理时，需要应对数据库更新和模式变化的挑战直接相关。

**📖 中文摘要**

本文提出了EvoSchema，一个用于评估和增强文本到SQL系统在真实世界模式演化下鲁棒性的综合基准。EvoSchema引入了一种新的模式演化分类法，涵盖了列级和表级修改的十种扰动类型，系统地模拟了数据库模式的动态性质。通过EvoSchema，作者对不同的开源和闭源LLM进行了深入评估，发现表级扰动对模型性能的影响显著大于列级更改。此外，EvoSchema启发了在模型训练和数据库设计方面更具弹性的文本到SQL系统的开发。在EvoSchema多样化模式设计上训练的模型可以迫使模型区分相同问题的模式差异，避免学习虚假模式，与在未扰动数据上训练的模型相比，平均表现出显著的鲁棒性。该基准为模型行为提供了有价值的见解，并为在动态、真实世界环境中设计系统指明了前进道路。这项工作专注于评估和提升大语言模型在结构化数据（数据库模式）变化下的鲁棒性，这与化学信息学中处理不断演化的化学数据库（如化合物库、反应库）和构建相应的稳健查询或推理模型面临类似挑战。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural text-to-SQL models, which translate natural language questions (NLQs) into SQL queries given a database schema, have achieved remarkable performance. However, database schemas frequently evolve to meet new requirements. Such schema evolution often leads to performance degradation for models trained on static schemas. Existing work either mainly focuses on simply paraphrasing some syntactic or semantic mappings among NLQ, DB and SQL, or lacks a comprehensive and controllable way to investigate the model robustness issue under the schema evolution, which is insufficient when facing the increasingly complex and rich database schema changes in reality, especially in the LLM era. To address the challenges posed by schema evolution, we present EvoSchema, a comprehensive benchmark designed to assess and enhance the robustness of text-to-SQL systems under real-world schema changes. EvoSchema introduces a novel schema evolution taxonomy, encompassing ten perturbation types across columnlevel and table-level modifications, systematically simulating the dynamic nature of database schemas. Through EvoSchema, we conduct an in-depth evaluation spanning different open source and closed-source LLMs, revealing that table-level perturbations have a significantly greater impact on model performance compared to column-level changes. Furthermore, EvoSchema inspires the development of more resilient text-to-SQL systems, in terms of both model training and database design. The models trained on EvoSchema's diverse schema designs can force the model to distinguish the schema difference for the same questions to avoid learning spurious patterns, which demonstrate remarkable robustness compared to those trained on unperturbed data on average. This benchmark offers valuable insights into model behavior and a path forward for designing systems capable of thriving in dynamic, real-world environments.

</details>

---

### 14. [eLasmobranc Dataset: An Image Dataset for Elasmobranch Species Recognition and Biodiversity Monitoring](https://arxiv.org/abs/2603.10724)

**基本信息**

- 🔗 arXiv: [`2603.10724`](https://arxiv.org/abs/2603.10724)
- 👥 作者: Ismael Beviá-Ballesteros, Mario Jerez-Tallón, Nieves Aranda-Garrido 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10724.pdf)

**💡 相关性分析**

满足标准2：论文贡献了一个高质量、专家标注、细粒度的物种图像数据集（eLasmobranc Dataset），专门用于训练和评估AI分类模型。这直接对应于化学信息学和质谱分析领域对高质量、标准化数据集（如质谱数据库、分子性质数据集）的迫切需求，这些数据集是训练和验证化学大模型及质谱结构推理工具的基础资源。

**📖 中文摘要**

本文介绍了eLasmobranc数据集，一个用于七种生态相关板鳃亚纲物种识别和生物多样性监测的 curated 公共图像数据集。图像主要通过专门的数据收集获得，包括实地活动、与当地鱼市场和项目的合作，以及来自公开来源。该数据集主要包含在标准化协议下于水环境外获取的图像，以确保诊断性形态特征的清晰可视化。它集成了专家验证的物种注释、结构化的空间和时间元数据以及补充的物种级信息。eLasmobranc数据集专门设计用于支持监督下的物种级分类、种群研究以及用于生物多样性监测的人工智能系统开发。该数据集通过结合形态清晰度、分类可靠性和公共可访问性，解决了细粒度板鳃亚纲识别中的关键空白，并促进了保护导向计算机视觉中的可重复研究。虽然主题是海洋生物，但该工作核心是创建了一个高质量、细粒度、带有专家注释的图像数据集，用于训练和评估AI模型。这种构建专用、高质量数据集以推动特定领域AI模型（如分类模型）发展的范式，与化学信息学和质谱分析中构建用于训练化学大模型或质谱结构推理模型的标准化数据集（如质谱库、分子数据集）的努力在目标和价值上完全一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Elasmobranch populations are experiencing significant global declines, and several species are currently classified as threatened. Reliable monitoring and species-level identification are essential to support conservation and spatial planning initiatives such as Important Shark and Ray Areas (ISRAs). However, existing visual datasets are predominantly detection-oriented, underwater-acquired, or limited to coarse-grained categories, restricting their applicability to fine-grained morphological classification. We present the eLasmobranc Dataset, a curated and publicly available image collection from seven ecologically relevant elasmobranch species inhabiting the eastern Spanish Mediterranean coast, a region where two ISRAs have been identified. Images were obtained through dedicated data collection, including field campaigns and collaborations with local fish markets and projects, as well as from open-access public sources. The dataset was constructed predominantly from images acquired outside the aquatic environment under standardized protocols to ensure clear visualization of diagnostic morphological traits. It integrates expert-validated species annotations, structured spatial and temporal metadata, and complementary species-level information. The eLasmobranc Dataset is specifically designed to support supervised species-level classification, population studies, and the development of artificial intelligence systems for biodiversity monitoring. By combining morphological clarity, taxonomic reliability, and public accessibility, the dataset addresses a critical gap in fine-grained elasmobranch identification and promotes reproducible research in conservation-oriented computer vision. The dataset is publicly available at this https URL .

</details>

---

### 15. [A Grammar of Machine Learning Workflows](https://arxiv.org/abs/2603.10742)

**基本信息**

- 🔗 arXiv: [`2603.10742`](https://arxiv.org/abs/2603.10742)
- 👥 作者: Simon Roth
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10742.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕构建可靠、可验证的机器学习工作流，这对于开发和评估化学大模型（作为一类特定的机器学习模型）至关重要，直接涉及模型构建的方法论和可靠性保障。

**📖 中文摘要**

本文提出了一种用于监督学习工作流的结构化语法，旨在通过运行时强制执行的硬约束来防止数据泄露。该语法将工作流分解为7个核心原语，并通过有向无环图连接。其核心贡献是“终端评估约束”，它在评估/评估边界上强制执行，防止对测试集的重复评估。这项工作与“化学大模型”主题相关，因为它提供了一个通用的、可形式化的机器学习工作流框架，该框架对于构建和验证可靠的化学信息学模型（包括大模型）至关重要。它强调了模型开发中可重复性和防止数据泄露的结构化方法，这是训练和评估化学大模型时的核心关切。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Data leakage affected 294 published papers across 17 scientific fields (Kapoor & Narayanan, 2023). The dominant response has been documentation: checklists, linters, best-practice guides. Documentation does not prevent these failures. This paper proposes a structural remedy: a grammar that decomposes the supervised learning lifecycle into 7 kernel primitives connected by a typed directed acyclic graph (DAG), with four hard constraints that reject the two most damaging leakage classes at call time. The grammar's core contribution is the terminal assess constraint: a runtime-enforced evaluate/assess boundary where repeated test-set assessment is rejected by a guard on a nominally distinct Evidence type. A companion study across 2,047 experimental instances quantifies why this matters: selection leakage inflates performance by d_z = 0.93 and memorization leakage by d_z = 0.53-1.11. Three separate implementations (Python, R, and Julia) confirm the claims. The appendix specification lets anyone build a conforming version.

</details>

---

### 16. [CUPID: A Plug-in Framework for Joint Aleatoric and Epistemic Uncertainty Estimation with a Single Model](https://arxiv.org/abs/2603.10745)

**基本信息**

- 🔗 arXiv: [`2603.10745`](https://arxiv.org/abs/2603.10745)
- 👥 作者: Xinran Xu, Xiuyi Fan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10745.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是深度学习模型的不确定性估计，这是一个在化学信息学（用于大模型预测）和质谱分析（用于结构推理置信度评估）中都具有高度相关性的基础方法论问题。

**📖 中文摘要**

本文提出了CUPID，一个用于联合估计偶然不确定性和认知不确定性的即插即用框架。CUPID可以灵活地插入任何预训练网络的层中，无需修改或重新训练基础模型。它通过学习的贝叶斯恒等映射来建模偶然不确定性，并通过分析模型对结构化扰动的内部响应来捕获认知不确定性。论文在分类、回归和分布外检测等任务上进行了评估。这项工作与“化学大模型”和“质谱结构推理”都相关。在化学信息学中，模型预测的不确定性量化对于高风险的决策（如药物发现或化合物性质预测）至关重要。对于质谱结构推理，可靠的不确定性估计可以帮助判断所推断的分子结构的置信度，提高推理结果的可信度和实用性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate estimation of uncertainty in deep learning is critical for deploying models in high-stakes domains such as medical diagnosis and autonomous decision-making, where overconfident predictions can lead to harmful outcomes. In practice, understanding the reason behind a model's uncertainty and the type of uncertainty it represents can support risk-aware decisions, enhance user trust, and guide additional data collection. However, many existing methods only address a single type of uncertainty or require modifications and retraining of the base model, making them difficult to adopt in real-world systems. We introduce CUPID (Comprehensive Uncertainty Plug-in estImation moDel), a general-purpose module that jointly estimates aleatoric and epistemic uncertainty without modifying or retraining the base model. CUPID can be flexibly inserted into any layer of a pretrained network. It models aleatoric uncertainty through a learned Bayesian identity mapping and captures epistemic uncertainty by analyzing the model's internal responses to structured perturbations. We evaluate CUPID across a range of tasks, including classification, regression, and out-of-distribution detection. The results show that it consistently delivers competitive performance while offering layer-wise insights into the origins of uncertainty. By making uncertainty estimation modular, interpretable, and model-agnostic, CUPID supports more transparent and trustworthy AI. Related code and data are available at this https URL .

</details>

---

### 17. [CodePercept: Code-Grounded Visual STEM Perception for MLLMs](https://arxiv.org/abs/2603.10757)

**基本信息**

- 🔗 arXiv: [`2603.10757`](https://arxiv.org/abs/2603.10757)
- 👥 作者: Tongkun Guan, Zhibo Yang, Jianqiang Wan 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10757.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究如何利用代码作为感知媒介来增强MLLMs在结构化视觉领域（如STEM）的理解能力，这与化学信息学中处理结构化化学数据（可视为一种STEM数据）的需求直接相关。同时，论文贡献了大规模数据集ICC-1M和评估基准STEM2Code-Eval，这属于可用于相关主题研究的数据资源和工具。

**📖 中文摘要**

本文提出了CodePercept，一个通过将代码确立为强大的感知媒介来系统增强多模态大语言模型（MLLMs）在科学、技术、工程和数学领域视觉推理能力的工作。作者构建了ICC-1M，一个包含100万个图像-标题-代码三元组的大规模数据集，通过两种互补的方法实现“代码即感知”范式：1) 以可执行代码作为图像标题的ground truth进行代码锚定标题生成；2) 通过生成重建代码进行STEM图像到代码的翻译。此外，还引入了STEM2Code-Eval基准，通过生成用于图像重建的可执行代码来直接评估视觉感知。这项工作与“化学大模型”高度相关，因为化学领域（如分子结构、反应方程、光谱图）充满了结构化的视觉信息。将化学视觉信息（如质谱图、分子式）转化为可执行代码或结构化表示，可以作为一种强大的感知和表示方法，用于构建更精确、可解释的化学领域大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

When MLLMs fail at Science, Technology, Engineering, and Mathematics (STEM) visual reasoning, a fundamental question arises: is it due to perceptual deficiencies or reasoning limitations? Through systematic scaling analysis that independently scales perception and reasoning components, we uncover a critical insight: scaling perception consistently outperforms scaling reasoning. This reveals perception as the true lever limiting current STEM visual reasoning. Motivated by this insight, our work focuses on systematically enhancing the perception capabilities of MLLMs by establishing code as a powerful perceptual medium--executable code provides precise semantics that naturally align with the structured nature of STEM visuals. Specifically, we construct ICC-1M, a large-scale dataset comprising 1M Image-Caption-Code triplets that materializes this code-as-perception paradigm through two complementary approaches: (1) Code-Grounded Caption Generation treats executable code as ground truth for image captions, eliminating the hallucinations inherent in existing knowledge distillation methods; (2) STEM Image-to-Code Translation prompts models to generate reconstruction code, mitigating the ambiguity of natural language for perception enhancement. To validate this paradigm, we further introduce STEM2Code-Eval, a novel benchmark that directly evaluates visual perception in STEM domains. Unlike existing work relying on problem-solving accuracy as a proxy that only measures problem-relevant understanding, our benchmark requires comprehensive visual comprehension through executable code generation for image reconstruction, providing deterministic and verifiable assessment. Code is available at this https URL .

</details>

---

### 18. [AI-Generated Rubric Interfaces: K-12 Teachers' Perceptions and Practices](https://arxiv.org/abs/2603.10773)

**基本信息**

- 🔗 arXiv: [`2603.10773`](https://arxiv.org/abs/2603.10773)
- 👥 作者: Bahare Riahi, Sayali Patukale, Joy Niranjan 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10773.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及人类与AI（特别是通过提示工程）在专业任务中的交互和协作，这种范式对于在化学信息学等领域有效利用和引导化学大模型具有直接的相关性和参考价值。

**📖 中文摘要**

本文研究了K-12教师对AI支持的评分规则生成工具的感知和实践。教师使用AI工具生成评分规则，并通过提示工程来定制标准和表现水平。他们发现AI生成的评分规则是强大的初稿，但需要教师监督和大量编辑。这项工作与“化学大模型”主题间接相关。虽然焦点是教育领域的AI应用，但其核心探索了人类与AI在复杂任务（评分规则制定）中的协作模式，以及如何通过提示工程引导AI生成符合特定领域（在此是教学）需求的内容。这种“人类-AI协作”和“提示工程”范式对于在化学领域应用大模型（例如，让大模型生成实验方案、数据分析报告或化合物评估标准）具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study investigates K--12 teachers' perceptions and experiences with AI-supported rubric generation during a summer professional development workshop ($n = 25$). Teachers used this http URL to generate rubrics and practiced prompting to tailor criteria and performance levels. They then applied these rubrics to provide feedback on a sample block-based programming activity, followed by using a chatbot to deliver rubric-based feedback for the same work. Data were collected through pre- and post-workshop surveys, open discussions, and exit tickets. We used thematic analysis to analyze the qualitative data. Teachers reported that they rarely create rubrics from scratch because the process is time-consuming and defining clear distinctions between performance levels is challenging. After hands-on use, teachers described AI-generated rubrics as strong starting drafts that improved structure and clarified vague criteria. However, they emphasized the need for teacher oversight due to generic or grade-misaligned language, occasional misalignment with instructional priorities, and the need for substantial editing. Survey results indicated high perceived clarity and ethical acceptability, moderate alignment with assignments, and usability as the primary weakness -- particularly the ability to add, remove, or revise criteria. Open-ended responses highlighted a ``strictness-versus-detail'' trade-off: AI feedback was often perceived as harsher but more detailed and scalable. As a result, teachers expressed conditional willingness to adopt AI rubric tools when workflows support easy customization and preserve teacher control.

</details>

---

### 19. [Phase-Interface Instance Segmentation as a Visual Sensor for Laboratory Process Monitoring](https://arxiv.org/abs/2603.10782)

**基本信息**

- 🔗 arXiv: [`2603.10782`](https://arxiv.org/abs/2603.10782)
- 👥 作者: Mingyue Li, Xin Yang, Shilin Yan 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10782.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容是化学实验室场景下的视觉感知与过程监控，这是化学信息学的一个具体且重要的应用方向。同时，论文贡献了CTG 2.0数据集，这是一个专门针对化学实验玻璃器皿和多相界面的标注数据集，可作为相关研究的宝贵资源。

**📖 中文摘要**

本文提出了LGA-RCM-YOLO模型，用于化学实验玻璃器皿中的多相界面实例分割，旨在作为实验室过程监控的视觉传感器。作者构建了Chemical Transparent Glasses dataset 2.0 (CTG 2.0)，一个包含3,668张图像、23种玻璃器皿类别和五种多相界面类型的基准数据集。该模型在CTG 2.0上取得了优异的性能，并展示了在分液漏斗相分离和结晶等连续过程监控中的应用。这项工作与“化学信息学”领域紧密相关，它直接针对化学实验室场景，提供了一种将计算机视觉和机器学习应用于实时监测化学实验过程的方法。虽然不直接涉及“大模型”或“质谱结构推理”，但它代表了AI在化学实验自动化、数据采集和过程分析中的前沿应用，是化学信息学的一个重要分支。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reliable visual monitoring of chemical experiments remains challenging in transparent glassware, where weak phase boundaries and optical artifacts degrade conventional segmentation. We formulate laboratory phenomena as the time evolution of phase interfaces and introduce the Chemical Transparent Glasses dataset 2.0 (CTG 2.0), a vessel-aware benchmark with 3,668 images, 23 glassware categories, and five multiphase interface types for phase-interface instance segmentation. Building on YOLO11m-seg, we propose LGA-RCM-YOLO, which combines Local-Global Attention (LGA) for robust semantic representation and a Rectangular Self-Calibration Module (RCM) for boundary refinement of thin, elongated interfaces. On CTG 2.0, the proposed model achieves 84.4% AP@0.5 and 58.43% AP@0.5-0.95, improving over the YOLO11m baseline by 6.42 and 8.75 AP points, respectively, while maintaining near real-time inference (13.67 FPS, RTX 3060). An auxiliary color-attribute head further labels liquid instances as colored or colorless with 98.71% precision and 98.32% recall. Finally, we demonstrate continuous process monitoring in separatory-funnel phase separation and crystallization, showing that phase-interface instance segmentation can serve as a practical visual sensor for laboratory automation.

</details>

---

### 20. [Protein Counterfactuals via Diffusion-Guided Latent Optimization](https://arxiv.org/abs/2603.10811)

**基本信息**

- 🔗 arXiv: [`2603.10811`](https://arxiv.org/abs/2603.10811)
- 👥 作者: Weronika Kłos, Sidney Bender, Lukas Kades
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10811.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对蛋白质的、基于扩散模型和反事实优化的可解释性设计与工程方法。这直接关联到化学信息学中利用生成模型（如扩散模型）进行分子设计，以及为模型预测提供可操作见解的研究主题，是化学大模型在生物分子领域的一个高级应用。

**📖 中文摘要**

本文提出了MCCOP框架，用于为蛋白质生成最小、生物学上合理的序列编辑（反事实），以将模型的预测翻转到期望的目标状态。MCCOP在连续的序列-结构联合潜在空间中操作，并使用预训练的扩散模型作为流形先验。论文在三个蛋白质工程任务上进行了评估：GFP荧光拯救、热力学稳定性增强和E3连接酶活性恢复。这项工作与“化学大模型”和“质谱结构推理”都高度相关。在化学信息学中，蛋白质工程和设计是大模型的重要应用场景。MCCOP提供了一种基于模型解释进行蛋白质逆向设计的方法。对于“质谱结构推理”，虽然本文焦点是蛋白质序列，但其“反事实优化”的核心思想可以迁移：给定一个质谱图和一个预测的分子结构，MCCOP式的框架可以用于搜索对该质谱图更合理的替代分子结构（反事实），从而帮助验证或改进推理结果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning models can predict protein properties with unprecedented accuracy but rarely offer mechanistic insight or actionable guidance for engineering improved variants. When a model flags an antibody as unstable, the protein engineer is left without recourse: which mutations would rescue stability while preserving function? We introduce Manifold-Constrained Counterfactual Optimization for Proteins (MCCOP), a framework that computes minimal, biologically plausible sequence edits that flip a model's prediction to a desired target state. MCCOP operates in a continuous joint sequence-structure latent space and employs a pretrained diffusion model as a manifold prior, balancing three objectives: validity (achieving the target property), proximity (minimizing mutations), and plausibility (producing foldable proteins). We evaluate MCCOP on three protein engineering tasks - GFP fluorescence rescue, thermodynamic stability enhancement, and E3 ligase activity recovery - and show that it generates sparser, more plausible counterfactuals than both discrete and continuous baselines. The recovered mutations align with known biophysical mechanisms, including chromophore packing and hydrophobic core consolidation, establishing MCCOP as a tool for both model interpretation and hypothesis-driven protein design. Our code is publicly available at this http URL .

</details>

---

### 21. [Evaluating Few-Shot Pill Recognition Under Visual Domain Shift](https://arxiv.org/abs/2603.10833)

**基本信息**

- 🔗 arXiv: [`2603.10833`](https://arxiv.org/abs/2603.10833)
- 👥 作者: W. I. Chu, G. Tarroni, L. Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10833.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是在真实世界复杂条件下，对化学实体（药片）进行鲁棒的少样本视觉识别。这属于化学信息学中物质识别与分类的一个具体而重要的子问题，其方法论对处理其他化学数据（如光谱）的类似挑战具有参考意义。

**📖 中文摘要**

本研究从部署角度评估了在视觉域偏移下的少样本药片识别。研究采用两阶段目标检测框架（基础训练后进行少样本微调），使模型能够使用每个新类别仅1、5或10个标记示例进行适应，并在一个包含多物体、杂乱场景的独立部署数据集上进行评估。评估重点是基于分类和基于错误的指标。研究发现，在重叠和遮挡条件下，模型的定位和召回率显著下降。这项工作与“化学信息学”和“质谱分析”有间接关联。虽然主题是药片识别，但其核心是解决在复杂、嘈杂的真实世界条件下，基于视觉的化学物质（药片）识别和分类的鲁棒性问题。这种在有限样本下适应新类别、并抵抗域偏移的方法论，对于质谱分析中处理新型或罕见化合物的谱图识别问题具有类比和参考价值。它强调了数据质量、模型泛化和部署就绪性在化学相关AI应用中的重要性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adverse drug events are a significant source of preventable harm, which has led to the development of automated pill recognition systems to enhance medication safety. Real-world deployment of these systems is hindered by visually complex conditions, including cluttered scenes, overlapping pills, reflections, and diverse acquisition environments. This study investigates few-shot pill recognition from a deployment-oriented perspective, prioritizing generalization under realistic cross-dataset domain shifts over architectural innovation. A two-stage object detection framework is employed, involving base training followed by few-shot fine-tuning. Models are adapted to novel pill classes using one, five, or ten labeled examples per class and are evaluated on a separate deployment dataset featuring multi-object, cluttered scenes. The evaluation focuses on classification-centric and error-based metrics to address heterogeneous annotation strategies. Findings indicate that semantic pill recognition adapts rapidly with few-shot supervision, with classification performance reaching saturation even with a single labeled example. However, stress testing under overlapping and occluded conditions demonstrates a marked decline in localization and recall, despite robust semantic classification. Models trained on visually realistic, multi-pill data consistently exhibit greater robustness in low-shot scenarios, underscoring the importance of training data realism and the diagnostic utility of few-shot fine-tuning for deployment readiness.

</details>

---

### 22. [6ABOS: An Open-Source Atmospheric Correction Framework for the EnMAP Hyperspectral Mission Based on 6S](https://arxiv.org/abs/2603.10856)

**基本信息**

- 🔗 arXiv: [`2603.10856`](https://arxiv.org/abs/2603.10856)
- 👥 作者: Gabriel Caballero Cañas, Bárbara Alvado Arranz, Xavier Sòria-Perpinyà 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10856.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于高光谱影像大气校正的开源框架6ABOS，并展示了其应用。高光谱数据在化学信息学中用于物质识别和定量，因此该工具为处理此类化学相关数据提供了重要的资源和工具。

**📖 中文摘要**

本文介绍了6ABOS，一个基于6S辐射传输模型的开源Python框架，用于对EnMAP高光谱影像进行自动化大气校正。该框架集成了自动化的EnMAP元数据解析与通过Google Earth Engine API的动态大气参数检索，实现了一种物理反演方案。论文在两个地中海内陆水库上进行了验证。这项工作与“化学信息学”和“质谱分析”有间接但重要的关联。高光谱成像在环境化学、地质化学和农业化学中用于检测和量化化学成分。准确的大气校正是从高光谱数据中可靠反演地表反射率（进而进行化学物质识别和定量）的关键预处理步骤。虽然不直接涉及“大模型”或“质谱结构推理”，但6ABOS作为一个专门用于处理高光谱化学传感数据的工具，为相关领域的研究提供了重要的数据预处理资源和开源工具。

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

满足标准1：论文的核心研究内容是使用扩散模型生成条件化的、高质量的合成生物数据（基因型）。这种方法论与化学信息学中利用生成模型创建合成化学数据（如分子、光谱）以解决数据稀缺或隐私问题的研究主题直接平行且高度相关。

**📖 中文摘要**

本文提出了SNPgen，一个用于生成表型监督的合成基因型的两阶段条件潜在扩散框架。SNPgen结合了GWAS指导的变异选择、用于基因型压缩的变分自编码器以及通过无分类器指导以二元疾病标签为条件的潜在扩散模型。论文在UK Biobank的458,724个个体的四种复杂疾病数据上进行了评估。这项工作与“化学信息学”中的生物信息学子领域高度相关。虽然主要面向遗传学，但“生成合成数据以保护隐私同时保持下游任务效用”是化学信息学中的一个普遍挑战，例如在生成合成分子数据或光谱数据时。SNPgen所采用的扩散模型框架和条件生成方法，可以直接启发或应用于生成合成的化学数据（如质谱图或分子结构），用于数据增强或隐私保护，从而支持化学大模型的训练和质谱结构推理研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Polygenic risk scores and other genomic analyses require large individual-level genotype datasets, yet strict data access restrictions impede sharing. Synthetic genotype generation offers a privacy-preserving alternative, but most existing methods operate unconditionally, producing samples without phenotype alignment, or rely on unsupervised compression, creating a gap between statistical fidelity and downstream task utility. We present SNPgen, a two-stage conditional latent diffusion framework for generating phenotype-supervised synthetic genotypes. SNPgen combines GWAS-guided variant selection (1,024-2,048 trait-associated SNPs) with a variational autoencoder for genotype compression and a latent diffusion model conditioned on binary disease labels via classifier-free guidance. Evaluated on 458,724 UK Biobank individuals across four complex diseases (coronary artery disease, breast cancer, type 1 and type 2 diabetes), models trained on synthetic data matched real-data predictive performance in a train-on-synthetic, test-on-real protocol, approaching genome-wide PRS methods that use $2$-$6\times$ more variants. Privacy analysis confirmed zero identical matches, near-random membership inference (AUC $\approx 0.50$), preserved linkage disequilibrium structure, and high allele frequency correlation ($r \geq 0.95$) with source data. A controlled simulation with known causal effects verified faithful recovery of the imposed genetic association structure.

</details>

---

### 24. [Continuous Diffusion Transformers for Designing Synthetic Regulatory Elements](https://arxiv.org/abs/2603.10885)

**基本信息**

- 🔗 arXiv: [`2603.10885`](https://arxiv.org/abs/2603.10885)
- 👥 作者: Jonathan Liu, Kia Ghods
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10885.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散Transformer模型生成具有特定功能的生物分子序列（DNA）。这属于化学信息学和计算生物学中“分子生成与设计”范畴，是化学大模型的一个前沿应用方向，其技术方法具有跨分子类型的借鉴意义。

**📖 中文摘要**

本文提出了一个参数高效的扩散Transformer，用于生成200bp细胞类型特异性的调控DNA序列。该模型用配备2D CNN输入编码器的Transformer去噪器替换了DNA-Diffusion的U-Net主干。论文进一步应用DDPO微调，使用Enformer作为奖励模型，在预测的调控活性上实现了38倍的改进。这项工作与“化学信息学”中的生物信息学和计算生物学子领域直接相关。它涉及使用先进的生成AI模型（扩散Transformer）进行生物分子（DNA序列）的设计。这体现了“化学大模型”在生物序列生成和设计方面的应用。虽然对象是DNA而非小分子，但其技术框架（DiT, 强化学习微调）对于探索分子生成和优化的化学信息学研究具有重要的参考价值和启发性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a parameter-efficient Diffusion Transformer (DiT) for generating 200bp cell-type-specific regulatory DNA sequences. By replacing the U-Net backbone of DNA-Diffusion with a transformer denoiser equipped with a 2D CNN input encoder, our model matches the U-Net's best validation loss in 13 epochs (60$\times$ fewer) and converges 39% lower, while reducing memorization from 5.3% to 1.7% of generated sequences aligning to training data via BLAT. Ablations show the CNN encoder is essential: without it, validation loss increases 70% regardless of positional embedding choice. We further apply DDPO finetuning using Enformer as a reward model, achieving a 38$\times$ improvement in predicted regulatory activity. Cross-validation against DRAKES on an independent prediction task confirms that improvements reflect genuine regulatory signal rather than reward model overfitting.

</details>

---

### 25. [A Hybrid Knowledge-Grounded Framework for Safety and Traceability in Prescription Verification](https://arxiv.org/abs/2603.10891)

**基本信息**

- 🔗 arXiv: [`2603.10891`](https://arxiv.org/abs/2603.10891)
- 👥 作者: Yichi Zhu, Kan Ling, Xu Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10891.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是在特定化学领域（药学）构建一个结合了符号知识库和大型语言模型的可靠、可解释的AI推理系统。这直接关联到“化学大模型”的研究，特别是如何将领域专业知识与大模型能力结合以实现安全、可信的化学信息处理与决策支持。

**📖 中文摘要**

本文介绍了PharmGraph-Auditor，一个用于处方审核的安全、有证据基础的创新系统。其核心是一个基于虚拟知识图范式的混合药物知识库，统一了用于集合约束满足的关系组件和用于拓扑推理的图组件。为了进行审核，论文引入了知识库锚定的验证链，这是一种新的推理范式，将LLM转变为透明的推理引擎。这项工作与“化学信息学”和“化学大模型”高度相关。它直接针对药物和医疗领域，构建了一个结构化的药物知识库，并设计了LLM与知识库协作的推理框架。这代表了在专业化学领域（此处是药学）构建可靠、可解释、基于知识的AI系统的典范。该系统的方法论——结合符号知识库与神经语言模型进行复杂推理和验证——对于开发其他化学领域的专家大模型（如用于反应预测、毒性评估的模型）具有重要的参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medication errors pose a significant threat to patient safety, making pharmacist verification (PV) a critical, yet heavily burdened, final safeguard. The direct application of Large Language Models (LLMs) to this zero-tolerance domain is untenable due to their inherent factual unreliability, lack of traceability, and weakness in complex reasoning. To address these challenges, we introduce PharmGraph-Auditor, a novel system designed for safe and evidence-grounded prescription auditing. The core of our system is a trustworthy Hybrid Pharmaceutical Knowledge Base (HPKB), implemented under the Virtual Knowledge Graph (VKG) paradigm. This architecture strategically unifies a relational component for set constraint satisfaction and a graph component for topological reasoning via a rigorous mapping layer. To construct this HPKB, we propose the Iterative Schema Refinement (ISR) algorithm, a framework that enables the co-evolution of both graph and relational schemas from medical texts. For auditing, we introduce the KB-grounded Chain of Verification (CoV), a new reasoning paradigm that transforms the LLM from an unreliable generator into a transparent reasoning engine. CoV decomposes the audit task into a sequence of verifiable queries against the HPKB, generating hybrid query plans to retrieve evidence from the most appropriate data store. Experimental results demonstrate robust knowledge extraction capabilities and show promises of using PharmGraph-Auditor to enable pharmacists to achieve safer and faster prescription verification.

</details>

---

### 26. [Bridging the Skill Gap in Clinical CBCT Interpretation with CBCTRepD](https://arxiv.org/abs/2603.10933)

**基本信息**

- 🔗 arXiv: [`2603.10933`](https://arxiv.org/abs/2603.10933)
- 👥 作者: Qinxin Wu, Fucheng Niu, Hengchuan Zhu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10933.pdf)

**💡 相关性分析**

满足标准1和2：论文核心研究内容是在一个专业科学领域（口腔放射学）开发与大模型结合的AI辅助报告生成系统，并深入研究了人机协作模式。这直接关联到化学信息学中构建领域专家AI系统的主题。同时，论文贡献了一个大规模、高质量的口腔CBCT-报告配对数据集，这是一个有价值的领域特定数据资源。

**📖 中文摘要**

本文介绍了CBCTRepD，一个用于口腔颌面锥形束CT报告生成的双语系统，旨在集成到常规的放射科医生-AI协同工作流中。作者策划了一个包含约7,408项研究的大规模、高质量配对CBCT-报告数据集，涵盖55种口腔疾病实体，并在此基础上开发了该系统。论文建立了一个临床基础的多层次评估框架。这项工作与“化学信息学”中的医疗信息学子领域以及“AI for Science”相关。虽然焦点是医学影像报告生成，但其核心是开发一个用于专业领域（此处是口腔放射学）的、能够与人类专家协作的大模型应用。这展示了在高度专业化的科学/医学领域构建和评估领域大模型的完整流程，包括数据构建、系统开发、人机协作评估等。其方法论对于在化学的其他子领域（如谱图解读、实验报告生成）开发类似的专业AI助手具有示范意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative AI has advanced rapidly in medical report generation; however, its application to oral and maxillofacial CBCT reporting remains limited, largely because of the scarcity of high-quality paired CBCT-report data and the intrinsic complexity of volumetric CBCT interpretation. To address this, we introduce CBCTRepD, a bilingual oral and maxillofacial CBCT report-generation system designed for integration into routine radiologist-AI co-authoring workflows. We curated a large-scale, high-quality paired CBCT-report dataset comprising approximately 7,408 studies, covering 55 oral disease entities across diverse acquisition settings, and used it to develop the system. We further established a clinically grounded, multi-level evaluation framework that assesses both direct AI-generated drafts and radiologist-edited collaboration reports using automatic metrics together with radiologist- and clinician-centered evaluation. Using this framework, we show that CBCTRepD achieves superior report-generation performance and produces drafts with writing quality and standardization comparable to those of intermediate radiologists. More importantly, in radiologist-AI collaboration, CBCTRepD provides consistent and clinically meaningful benefits across experience levels: it helps novice radiologists improve toward intermediate-level reporting, enables intermediate radiologists to approach senior-level performance, and even assists senior radiologists by reducing omission-related errors, including clinically important missed lesions. By improving report structure, reducing omissions, and promoting attention to co-existing lesions across anatomical regions, CBCTRepD shows strong and reliable potential as a practical assistant for real-world CBCT reporting across multi-level care settings.

</details>

---

### 27. [When should we trust the annotation? Selective prediction for molecular structure retrieval from mass spectra](https://arxiv.org/abs/2603.10950)

**基本信息**

- 🔗 arXiv: [`2603.10950`](https://arxiv.org/abs/2603.10950)
- 👥 作者: Mira Jürgens, Gaetan De Waele, Morteza Rakhshaninejad 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10950.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”这一主题，专注于从MS/MS谱图进行分子结构检索的机器学习方法，并提出了一个提高预测可靠性的选择性预测框架。

**📖 中文摘要**

这篇论文针对从串联质谱（MS/MS）中识别分子结构这一核心任务，提出了一个选择性预测框架。该框架允许模型在不确定性过高时放弃预测，这对于临床代谢组学等高风险应用至关重要。论文在MassSpecGym基准上全面评估了不同粒度（指纹级和检索级）的不确定性量化策略，包括一阶置信度度量、二阶分布估计的偶然和认知不确定性，以及潜在空间中的距离度量。研究发现，虽然指纹级不确定性评分是检索成功的较差代理，但计算成本低廉的一阶置信度度量和检索级偶然不确定性在各种评估设置下都能实现强大的风险-覆盖率权衡。这项工作直接解决了质谱结构推理中的一个关键挑战——预测可靠性，并提供了实用的工具和评估方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning methods for identifying molecular structures from tandem mass spectra (MS/MS) have advanced rapidly, yet current approaches still exhibit significant error rates. In high-stakes applications such as clinical metabolomics and environmental screening, incorrect annotations can have serious consequences, making it essential to determine when a prediction can be trusted. We introduce a selective prediction framework for molecular structure retrieval from MS/MS spectra, enabling models to abstain from predictions when uncertainty is too high. We formulate the problem within the risk-coverage tradeoff framework and comprehensively evaluate uncertainty quantification strategies at two levels of granularity: fingerprint-level uncertainty over predicted molecular fingerprint bits, and retrieval-level uncertainty over candidate rankings. We compare scoring functions including first-order confidence measures, aleatoric and epistemic uncertainty estimates from second-order distributions, as well as distance-based measures in the latent space. All experiments are conducted on the MassSpecGym benchmark. Our analysis reveals that while fingerprint-level uncertainty scores are poor proxies for retrieval success, computationally inexpensive first-order confidence measures and retrieval-level aleatoric uncertainty achieve strong risk-coverage tradeoffs across evaluation settings. We demonstrate that by applying distribution-free risk control via generalization bounds, practitioners can specify a tolerable error rate and obtain a subset of annotations satisfying that constraint with high probability.

</details>

---

### 28. [Flexible Cutoff Learning: Optimizing Machine Learning Potentials After Training](https://arxiv.org/abs/2603.10205)

**基本信息**

- 🔗 arXiv: [`2603.10205`](https://arxiv.org/abs/2603.10205)
- 👥 作者: Rick Oerder, Jan Hamaekers
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10205.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于化学和材料科学的机器学习原子间势（MLIPs），这是“化学大模型”在分子模拟和材料发现领域的一个关键应用。提出的FCL方法旨在优化这类模型的部署效率。

**📖 中文摘要**

本文提出了灵活截止学习（FCL），一种用于训练机器学习原子间势（MLIPs）的方法，其截止半径可以在训练后进行调整。与在训练期间固定截止半径的传统MLIP不同，FCL模型通过为每个原子独立随机采样截止半径进行训练。由此产生的模型可以根据应用需求，以不同的每原子截止半径部署，从而实现特定应用的精度-成本权衡优化。作者使用修改后的MACE架构在MAD数据集上进行了演示。对于包含分子晶体的子集，优化的每原子截止半径将计算成本降低了60%以上，同时力误差增加不到1%。这项工作展示了如何通过训练后优化，使单个通用MLIP适应不同应用，而无需重新训练。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Flexible Cutoff Learning (FCL), a method for training machine learning interatomic potentials (MLIPs) whose cutoff radii can be adjusted after training. Unlike conventional MLIPs that fix the cutoff radius during training, FCL models are trained by randomly sampling cutoff radii independently for each atom. The resulting model can then be deployed with different per-atom cutoff radii depending on the application, enabling application-specific optimization of the accuracy-cost tradeoff. Using a differentiable cost model, these per-atom cutoffs can be optimized for specific target systems after training. We demonstrate FCL with a modified MACE architecture trained on the MAD dataset. For a subset featuring molecular crystals, optimized per-atom cutoffs reduce computational cost by more than 60% while increasing force errors by less than 1%. These results show that FCL enables training of a single general-purpose MLIP that can be adapted to diverse applications through post-training cutoff optimization, eliminating the need for retraining.

</details>

---

### 29. [Geo-ADAPT-VQE: Quantum Information Metric-Aware Circuit Optimization for Quantum Chemistry](https://arxiv.org/abs/2603.10325)

**基本信息**

- 🔗 arXiv: [`2603.10325`](https://arxiv.org/abs/2603.10325)
- 👥 作者: Mohammad Aamir Sohail, Toshiaki Koike-Akino
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10325.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是用于量子化学计算的变分量子算法（VQE）的改进，这是“化学大模型”在量子计算领域的前沿应用。提出的Geo-ADAPT-VQE算法旨在更高效、更稳定地求解分子电子结构问题。

**📖 中文摘要**

本文介绍了Geo-ADAPT-VQE，一种用于量子化学的几何感知自适应变分量子本征求解器（VQE）算法。自适应ansatz构建是减少电路深度和提高VQE优化效率的强大技术。然而，现有的自适应方法（如ADAPT-VQE）仅依赖于一阶梯度，忽略了量子态空间的底层几何结构。Geo-ADAPT-VQE使用自然梯度规则从算子池中选择算子，使ansatz能够沿着与底层量子态几何一致的方向增长，从而改善收敛性并减少算法陷入浅层局部极小值和鞍点区域的敏感性。数值模拟涉及五个分子，结果表明Geo-ADAPT-VQE相比现有方法实现了更快、更稳定的收敛，同时产生了更短的ansatz。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Adaptive ansatz construction has emerged as a powerful technique for reducing circuit depth and improving optimization efficiency in variational quantum eigensolvers. However, existing adaptive methods, including ADAPT-VQE, rely solely on first-order gradients and therefore ignore the underlying geometry of the quantum state space, limiting both convergence behavior and operator-selection efficiency. We introduce Geo-ADAPT-VQE, a geometry-aware adaptive VQE algorithm that selects operators from a pool using the natural gradient rule. The geometric operator-selection rule enables the ansatz to grow along directions aligned with the underlying quantum-state geometry, thereby improving convergence and reducing the algorithm's susceptibility to shallow local minima and saddle-point regions. We further provide an asymptotic convergence result. We present numerical simulations involving five molecules, which demonstrate that Geo-ADAPT-VQE achieves faster and more stable convergence compared to existing methods, while producing significantly shorter ansatz. In particular, Geo-ADAPT achieves up to 100-fold reduction in energy error compared to existing methods.

</details>

---

### 30. [Beam-Plasma Collective Oscillations in Intense Charged-Particle Beams: Dielectric Response Theory, Langmuir Wave Dispersion, and Unsupervised Detection via Prometheus](https://arxiv.org/abs/2603.10457)

**基本信息**

- 🔗 arXiv: [`2603.10457`](https://arxiv.org/abs/2603.10457)
- 👥 作者: Brandon Yee, Wilson Collins, Michael Iofin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10457.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是强流带电粒子束中的集体动力学，这属于计算化学和物理化学中模拟带电粒子系统的基础理论范畴，与“化学大模型”所依赖的底层物理原理和模拟技术相关。

**📖 中文摘要**

本文为强流带电粒子束中的束-等离子体集体振荡开发了一个理论和计算框架。在第一部分，作者制定了由Vlasov-Poisson系统支配的动力学场论，推导了三种束分布函数的Lindhard介电函数和随机相位近似（RPA）极化张量。通过介电函数，作者证明了在临界束密度n_c以上存在无阻尼的朗缪尔波模式，获得了显式的束-等离子体色散关系，并证明了朗道阻尼在粒子-空穴连续谱之上消失。等离子体频率由f求和定则固定，与分布形状无关；更高的色散系数取决于速度矩。空间电荷效应驱动了具有sqrt(n-n_c)起始的异常束展宽和在q=2k_F处的Friedel振荡。束-等离子体转变通过重整化群分析属于3D Ising普适类。这项工作为理解强流束中的集体动力学提供了理论基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We develop a theoretical and computational framework for beam-plasma collective oscillations in intense charged-particle beams at intermediate energies (10-100 MeV). In Part I, we formulate a kinetic field theory governed by the Vlasov-Poisson system, deriving the Lindhard dielectric function and random phase approximation (RPA) polarization tensor for three beam distribution functions. We prove via the dielectric function epsilon(omega,q)=0 the existence of undamped Langmuir wave modes above a critical beam density n_c, obtain explicit beam-plasma dispersion relations, and show that Landau damping vanishes above the particle-hole continuum. The plasma frequency Omega_p^2 = ne^2/(m*epsilon_0) is fixed by the f-sum rule independently of distribution shape; higher dispersion coefficients depend on velocity moments. Space charge effects drive anomalous beam broadening with sqrt(n-n_c) onset and Friedel oscillations at q=2k_F. The beam-plasma transition belongs to the 3D Ising universality class via renormalization group analysis. In Part II, we validate these predictions using Prometheus, a beta-VAE trained on static structure factor data S(q) from particle-in-cell (PIC) beam simulations. Prometheus detects collective plasma oscillation onset in Gaussian and uniform distributions, confirms their absence in the degenerate Fermi gas (n_c -> 0), and resolves the Kohn anomaly at q=2k_F. Dispersion analysis of S(q,omega) from PIC simulations verifies the distribution-independent Omega_p predicted by the f-sum rule. All six validation checks pass. Predicted signatures -- density-tunable plasma resonances at omega_p proportional to sqrt(n), anomalous beam broadening with sqrt(n-n_c) onset, and Friedel oscillations -- are accessible at existing intermediate-energy beam facilities.

</details>

---

### 31. [Hybridlane: A Software Development Kit for Hybrid Continuous-Discrete Variable Quantum Computing](https://arxiv.org/abs/2603.10919)

**基本信息**

- 🔗 arXiv: [`2603.10919`](https://arxiv.org/abs/2603.10919)
- 👥 作者: Jim Furches, Timothy J. Stavenger, Carlos Ortiz Marrero
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10919.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个用于混合量子计算的软件开发工具包（Hybridlane），这是一个可用于量子化学模拟等“化学大模型”应用的工具和资源。它降低了在化学等领域开发混合量子算法的门槛。

**📖 中文摘要**

本文提出了Hybridlane，一个用于混合连续-离散变量量子计算的开源软件开发工具包。结合了离散变量量子比特和连续变量量子模式的混合量子计算系统，在量子模拟、纠错和传感应用中具有优势。然而，现有的量子软件框架缺乏对表达和操作混合电路的原生支持。Hybridlane引入了自动线类型推断，以区分量子比特和量子模式，而无需手动注释，从而实现了电路正确性的编译时验证。通过将门语义与矩阵表示解耦，Hybridlane可以用最小的内存消耗描述宽而深的电路，且不需要模拟。该框架实现了遵循既定指令集架构的混合门和分解的全面库，同时与PennyLane的广泛量子比特算法库保持兼容。此外，它支持包括使用Bosonic Qiskit的经典模拟和编译到桑迪亚国家实验室QSCOUT离子阱硬件在内的多个后端。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hybrid quantum computing systems that combine discrete-variable qubits with continuous-variable qumodes offer promising advantages for quantum simulation, error correction, and sensing applications. However, existing quantum software frameworks lack native support for expressing and manipulating hybrid circuits, forcing developers to work with fragmented toolchains or rely on simulation-coupled representations that limit scalability. We present Hybridlane, an open-source software development kit providing a unified frontend for hybrid continuous-discrete variable quantum computing. Hybridlane introduces automatic wire type inference to distinguish qubits from qumodes without manual annotations, enabling compile-time validation of circuit correctness. By decoupling gate semantics from matrix representations, Hybridlane can describe wide and deep circuits with minimal memory consumption and without requiring simulation. The framework implements a comprehensive library of hybrid gates and decompositions following established instruction set architectures, while remaining compatible with PennyLane's extensive qubit algorithm library. Furthermore, it supports multiple backends including classical simulation with Bosonic Qiskit and hardware compilation to Sandia National Laboratories' QSCOUT ion trap. We demonstrate Hybridlane's capabilities through bosonic quantum phase estimation and ion trap calibration workflows.

</details>

---

### 32. [Bayesian Optimization with Gaussian Processes to Accelerate Stationary Point Searches](https://arxiv.org/abs/2603.10992)

**基本信息**

- 🔗 arXiv: [`2603.10992`](https://arxiv.org/abs/2603.10992)
- 👥 作者: Rohit Goswami
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.10992.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是加速化学中势能面探索的优化算法，这是“化学大模型”进行反应路径寻找和过渡态搜索的关键组成部分。同时，它提供了一种具体的算法框架（贝叶斯优化与高斯过程），可作为相关研究的工具。

**📖 中文摘要**

本文提出了一种使用高斯过程的贝叶斯优化方法来加速势能面上驻点（包括极小点和鞍点）的搜索。作者提出了一个统一的六步代理循环，通过贝叶斯优化视角统一了极小化、单点鞍点搜索和双端鞍点搜索，仅在内部优化目标和获取准则上有所不同。该框架使用具有导数观测的高斯过程回归、反距离核和主动学习。通过最远点采样与地球移动距离、通过方差屏障和振荡检测的MAP正则化以及自适应信任半径形成的Optimal Transport GP扩展，是相同基本方法的具体扩展，提高了准确性和效率。作者还演示了随机傅里叶特征将超参数训练与预测解耦，从而为高维系统实现有利的缩放。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accelerating the explorations of stationary points on potential energy surfaces building local surrogates spans decades of effort. Done correctly, surrogates reduce required evaluations by an order of magnitude while preserving the accuracy of the underlying theory. We present a unified Bayesian Optimization view of minimization, single point saddle searches, and double ended saddle searches through a unified six-step surrogate loop, differing only in the inner optimization target and acquisition criterion. The framework uses Gaussian process regression with derivative observations, inverse-distance kernels, and active learning. The Optimal Transport GP extensions of farthest point sampling with Earth mover's distance, MAP regularization via variance barrier and oscillation detection, and adaptive trust radius form concrete extensions of the same basic methodology, improving accuracy and efficiency. We also demonstrate random Fourier features decouple hyperparameter training from predictions enabling favorable scaling for high-dimensional systems. Accompanying pedagogical Rust code demonstrates that all applications use the exact same Bayesian optimization loop, bridging the gap between theoretical formulation and practical execution.

</details>

---

### 33. [Toward Closed-loop Molecular Discovery via Language Model, Property Alignment and Strategic Search](https://arxiv.org/abs/2512.09566)

**基本信息**

- 🔗 arXiv: [`2512.09566`](https://arxiv.org/abs/2512.09566)
- 👥 作者: Junkai Ji, Zhangfan Yang, Dong Xu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.09566.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学大模型（分子语言模型）和分子生成/设计，这是化学信息学的核心主题。

**📖 中文摘要**

本文提出了一种名为Trio的分子生成框架，用于靶向分子设计。该框架整合了基于片段的分子语言建模、强化学习和蒙特卡洛树搜索，实现了有效且可解释的闭环分子设计。Trio通过三个核心组件实现：基于上下文的片段组装、强化学习以增强物理化学和合成可行性，以及蒙特卡洛树搜索在蛋白质结合口袋内平衡新颖化学型的探索和有前景中间体的利用。实验结果表明，Trio能够可靠地生成化学有效且药理学性质增强的配体，在结合亲和力、类药性和合成可及性方面优于现有方法，同时将分子多样性扩展了四倍以上。该工作通过结合泛化性、合理性和可解释性，建立了一个闭环生成范式，为AI驱动的药物发现提供了变革性基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drug discovery is a time-consuming and expensive process, with traditional high-throughput and docking-based virtual screening hampered by low success rates and limited scalability. Recent advances in generative modelling, including autoregressive, diffusion, and flow-based approaches, have enabled de novo ligand design beyond the limits of enumerative screening. Yet these models often suffer from inadequate generalization, limited interpretability, and an overemphasis on binding affinity at the expense of key pharmacological properties, thereby restricting their translational utility. Here we present Trio, a molecular generation framework integrating fragment-based molecular language modeling, reinforcement learning, and Monte Carlo tree search, for effective and interpretable closed-loop targeted molecular design. Through the three key components, Trio enables context-aware fragment assembly, enforces physicochemical and synthetic feasibility, and guides a balanced search between the exploration of novel chemotypes and the exploitation of promising intermediates within protein binding pockets. Experimental results show that Trio reliably achieves chemically valid and pharmacologically enhanced ligands, outperforming state-of-the-art approaches with improved binding affinity (+7.85%), drug-likeness (+11.10%) and synthetic accessibility (+12.05%), while expanding molecular diversity more than fourfold. By combining generalization, plausibility, and interpretability, Trio establishes a closed-loop generative paradigm that redefines how chemical space can be navigated, offering a transformative foundation for the next era of AI-driven drug discovery.

</details>

---

### 34. [Pretrained battery transformer (PBT): A foundation model for universal battery life prediction](https://arxiv.org/abs/2512.16334)

**基本信息**

- 🔗 arXiv: [`2512.16334`](https://arxiv.org/abs/2512.16334)
- 👥 作者: Ruifeng Tan, Weixiang Hong, Jia Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.16334.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于电池化学领域的预训练基础模型（PBT），这直接属于化学大模型在特定化学领域（电化学）的应用范畴。

**📖 中文摘要**

本文提出了预训练电池变压器（PBT），一个用于电池寿命预测的基础模型。PBT通过整合电池知识编码的专家混合层，从异构数据中学习可迁移的表征。该模型在13个锂离子电池数据集上进行预训练，随后通过迁移学习适应下游电池寿命预测任务。在涵盖锂离子、钠离子和锌离子电池的15个数据集上，PBT实现了最先进的性能，平均比最强竞争方法高出21.8%。这项研究建立了首个用于电池寿命预测的基础模型，并为构建通用的电池寿命预测系统提供了一条可扩展的途径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early prediction of battery cycle life is essential for improving battery design, manufacturing, and deployment. However, despite encouraging results with machine learning, progress remains constrained by scarce data and data heterogeneity across battery chemistries, specifications, formation protocols, and operating conditions. Although transfer learning has been widely explored to alleviate these challenges, its effectiveness is constrained by the lack of a foundation model that can capture broadly transferable knowledge from diverse battery life data. This gap persists because integration of heterogeneous battery datasets under data scarcity is inherently challenging. Here we introduce the pretrained battery transformer (PBT), a foundation model for battery life prediction that incorporates battery-knowledge-encoded mixture-of-experts layers to learn transferable representations from heterogeneous data. PBT is pretrained on 13 lithium-ion battery datasets and subsequently adapted to downstream battery life prediction tasks through transfer learning. Across 15 datasets covering 977 batteries and 533 sets of aging conditions from lithium-ion, sodium-ion and zinc-ion batteries, PBT achieves state-of-the-art performance, surpassing the strongest competing method by 21.8% on average, with gains of up to 86.9%. Our study establishes the first foundation model for battery life prediction and provides a scalable route towards universal battery lifetime prediction systems, with broader implications for other scientific and technological domains characterized by scarce and heterogeneous data.

</details>

---

### 35. [Sampling via Stochastic Interpolants by Langevin-based Velocity and Initialization Estimation in Flow ODEs](https://arxiv.org/abs/2601.08527)

**基本信息**

- 🔗 arXiv: [`2601.08527`](https://arxiv.org/abs/2601.08527)
- 👥 作者: Chenguang Duan, Yuling Jiao, Gabriele Steidl 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.08527.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于从（化学系统中常见的）复杂概率分布（如玻尔兹曼密度）中采样的新型算法框架。这属于化学信息学中分子模拟和采样方法的核心问题，与构建和利用化学系统的概率模型密切相关。

**📖 中文摘要**

本文提出了一种基于概率流常微分方程（ODE）从非归一化玻尔兹曼密度中采样的新方法。该ODE源自线性随机插值。该方法的关键创新在于使用一系列朗之万采样器来实现流的有效模拟。具体来说，这些朗之万采样器被用于（i）在中间时间从插值分布生成样本，以及（ii）从这些中间时间开始，构建控制概率流ODE的速度场的鲁棒估计器。理论上，我们为两个朗之万组件提供了收敛保证，并为概率流ODE建立了非渐近收敛速率。广泛的数值实验证明了该方法在跨维度范围具有挑战性的多峰分布上的效率，以及其在贝叶斯推理任务中的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a novel method for sampling from unnormalized Boltzmann densities based on a probability flow ordinary differential equation (ODE) derived from linear stochastic interpolants. The key innovation of our approach is the use of a sequence of Langevin samplers to enable efficient simulation of the flow. Specifically, these Langevin samplers are employed (i) to generate samples from the interpolant distribution at intermediate times and (ii) to construct, starting from these intermediate times, a robust estimator of the velocity field governing the probability flow ODE. Theoretically, we provide convergence guarantees for both Langevin components, and establish a non-asymptotic convergence rate for the probability flow ODE. Extensive numerical experiments demonstrate the efficiency of the proposed method on challenging multimodal distributions across a range of dimensions, as well as its effectiveness in Bayesian inference tasks.

</details>

---

### 36. [A Finite-Blocklength Analysis for ORBGRAND](https://arxiv.org/abs/2603.07526)

**基本信息**

- 🔗 arXiv: [`2603.07526`](https://arxiv.org/abs/2603.07526)
- 👥 作者: Zhuang Li, Wenyi Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07526.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是通信信道中的解码算法（GRAND），特别是其利用软信息（可靠性）进行推理的变体（ORBGRAND）。虽然领域不同，但“利用可靠性信息进行推理”这一核心方法论，与“质谱结构推理”中利用谱图信号强度（一种可靠性/概率信息）推断分子结构在数学和算法思想层面存在深刻的相似性，属于核心主题相关的方法论迁移研究。

**📖 中文摘要**

本文对有序可靠性比特GRAND解码器进行了有限码长分析。GRAND解码器家族通过猜测信道噪声进行解码，ORBGRAND是其利用软信息的硬件友好变体。论文推导了ORBGRAND特定的随机编码联合界，并分析了两个关键的译码度量：将发送码字的度量视为U-统计量并通过Hoeffding分解进行分析，将竞争码字的度量简化为独立同分布伯努利随机变量的加权和并通过强大偏差分析进行处理。结合Berry-Esseen论证，得到了二阶可达速率展开及其相关的正态近似。数值结果验证了ORB-RCU界相对于基于最大似然的RCU基准的紧密度，以及正态近似在实际操作区域的准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Within the Guessing Random Additive Noise Decoding (GRAND) family, ordered reliability bits GRAND (ORBGRAND) has received considerable attention for its hardware-friendly exploitation of soft information. Existing information-theoretic results for ORBGRAND are asymptotic in blocklength and do not quantify its performance at short-to-moderate blocklengths. This paper develops a finite-blocklength analysis for ORBGRAND over general bit channel, addressing the key challenge that the rank-induced decoding metric is non-additive and coupled across symbols. We first derive an ORBGRAND-specific random-coding union (RCU)-type achievability (ORB-RCU) bound on the ensemble-average error probability. We then characterize two governing decoding metrics: the transmitted-codeword metric is treated as a U-statistic and analyzed via Hoeffding decomposition, while the competing-codeword metric is reduced to a weighted sum of independent and identically distributed Bernoulli random variables and analyzed through strong large-deviation analysis. Combining these ingredients with a Berry-Esseen argument yields a second-order achievable-rate expansion and the associated normal approximation, whose first-order term is shown to equal the ORBGRAND generalized mutual information and whose second-order term defines an ORBGRAND dispersion with a single-letter variance representation. Numerical results for BPSK-modulated additive white Gaussian noise channel validate the tightness of ORB-RCU relative to the maximum-likelihood based RCU benchmark and the accuracy of the normal approximation in the operating regime of practical interest.

</details>

---

### 37. [GRAND for Gaussian Intersymbol Interference Channels](https://arxiv.org/abs/2603.08325)

**基本信息**

- 🔗 arXiv: [`2603.08325`](https://arxiv.org/abs/2603.08325)
- 👥 作者: Zhuang Li, Wenyi Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08325.pdf)

**💡 相关性分析**

满足标准1：与上一篇论文类似，本文核心研究内容是在有记忆信道（ISI）中利用序列可靠性进行解码推理。这种在噪声和干扰（类似于质谱中的背景噪声和碎片离子干扰）环境下进行信号推理和结构恢复的方法，与质谱结构推理的核心挑战（从复杂的谱图中推断分子结构）在问题建模和解决思路上高度相关。

**📖 中文摘要**

本文将有记忆信道中的解码任务建模为一个具有挑战性的问题，并将最近提出的猜测随机加性噪声解码范式应用于具有记忆的线性高斯符号间干扰信道。为了描述错误模式，引入了错误突发概念以考虑记忆效应，并定义了序列可靠性来表征错误模式的可能性。基于序列可靠性，得到了线性高斯ISI信道的最优GRAND算法（SGRAND-ISI），它等价于最大似然解码算法。随后开发了基于SGRAND-ISI的序可靠性比特GRAND算法以方便实现。数值实验表明，所提算法相比忽略信道记忆的GRAND算法实现了多dB的改进，并且通常能达到与ML下界相差0.1-0.2dB的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Channel decoding is a challenging task in communication channels exhibiting memory effects. In this work, we apply the recently proposed decoding paradigm of guessing random additive noise decoding (GRAND) to channels with memory, focusing on linear Gaussian intersymbol interference (ISI) channels. For describing error patterns (EPs), we introduce the concept of error burst to account for the memory effect, and define sequence reliability to characterize the likelihood of EP. Based on sequence reliability, we obtain the optimal GRAND algorithm as a generalization of soft GRAND (SGRAND) for linear Gaussian ISI channels, termed SGRAND-ISI, which is equivalent to the maximum-likelihood (ML) decoding algorithm. We then develop order-reliability-bit (ORB) GRAND algorithms based on SGRAND-ISI, to facilitate implementation. In numerical experiments, our proposed algorithms achieve multiple-dB improvements compared to GRAND algorithms which ignore channel memory, and can often attain performance within 0.1--0.2dB of the ML lower bound. We also compare our proposed algorithms with the recently proposed ORBGRAND-Approximate Independence algorithm for handling channel memory, and observe a performance gain of at least 0.5dB at block error rate of $10^{-3}$, meanwhile incurring a substantially lower computational complexity.

</details>

---

### 38. [A New Modeling to Feature Selection Based on the Fuzzy Rough Set Theory in Normal and Optimistic States on Hybrid Information Systems](https://arxiv.org/abs/2603.08900)

**基本信息**

- 🔗 arXiv: [`2603.08900`](https://arxiv.org/abs/2603.08900)
- 👥 作者: Mohammad Hossein Safarpour, Seyed Majid Alavi, Mohammad Izadikhah 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08900.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是特征选择，这是机器学习和化学信息学（如QSAR建模、光谱分析）中的基础任务。论文提出的基于模糊粗糙集和优化问题重构的新模型，为高维数据（如化学描述符、质谱特征）的特征选择提供了新的方法，直接与化学信息学中的数据分析主题相关。

**📖 中文摘要**

本文针对混合信息系统中的特征选择问题，提出了一种基于模糊粗糙集理论的新模型。该模型通过计算对象之间的组合距离来推导模糊等价关系，从而避免了在高维空间中通过交集操作获取模糊等价关系所带来的耗时和内存密集问题。该方法将特征选择问题重新表述为一个优化问题，并可以使用适当的元启发式算法求解。提出的FSbuHD模型在正常和乐观两种模式下运行，并在UCI存储库的标准数据集上进行了测试。结果表明，与先前的方法和算法相比，FSbuHD是特征选择中最有效的方法之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Considering the high volume, wide variety, and rapid speed of data generation, investigating feature selection methods for big data presents various applications and advantages. By removing irrelevant and redundant features, feature selection reduces data dimensions, thereby facilitating optimal decision-making within decision systems. One of the key tools for feature selection in hybrid information systems is fuzzy rough set theory. However, this theory faces two significant challenges: First, obtaining fuzzy equivalence relations through intersection operations in high-dimensional spaces can be both time-consuming and memory-intensive. Additionally, this method may produce noisy data, complicating the feature selection process. The purpose and innovation of this paper are to address these issues. We proposed a new feature selection model that calculates the combined distance between objects and subsequently used this information to derive the fuzzy equivalence relation. Rather than directly solving the feature selection problem, this approach reformulates it into an optimization problem that can be tackled using appropriate meta-heuristic algorithms. We have named this new approach FSbuHD. The FSbuHD model operates in two modes - normal and optimistic - based on the selection of one of the two introduced fuzzy equivalence relations. The model is then tested on standard datasets from the UCI repository and compared with other algorithms. The results of this research demonstrate that FSbuHD is one of the most efficient and effective methods for feature selection when compared to previous methods and algorithms.

</details>

---

### 39. [PathoScribe: Transforming Pathology Data into a Living Library with a Unified LLM-Driven Framework for Semantic Retrieval and Clinical Integration](https://arxiv.org/abs/2603.08935)

**基本信息**

- 🔗 arXiv: [`2603.08935`](https://arxiv.org/abs/2603.08935)
- 👥 作者: Abdul Rehman Akbar, Samuel Wales-McGrath, Alejadro Levya 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08935.pdf)

**💡 相关性分析**

满足标准2：论文提出的PathoScribe框架是一个强大的检索增强生成系统，专门用于处理复杂的科学/医学文本数据（病理报告），并将其转化为可查询的知识库。这种构建结构化、可检索的科学数据资源的方法，与化学信息学和质谱分析领域构建可查询的化合物、质谱谱图数据库的需求在方法论上高度一致。

**📖 中文摘要**

本文提出了PathoScribe，一个统一的检索增强大语言模型框架，旨在将静态的病理学档案转化为可搜索、支持推理的“活体图书馆”。该系统支持自然语言病例探索、自动队列构建、临床问答、免疫组化面板推荐和提示控制的报告转换。在70,000份多机构外科病理报告上的评估表明，PathoScribe在自然语言病例检索上实现了完美的Recall@10，并展示了高质量的检索增强推理能力。该系统能够根据自由文本的资格标准在几分钟内自动构建研究就绪的队列，与人工审核的一致性达到91.3%。这项工作为将数字病理档案从被动存储系统转变为主动的临床智能平台奠定了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pathology underpins modern diagnosis and cancer care, yet its most valuable asset, the accumulated experience encoded in millions of narrative reports, remains largely inaccessible. Although institutions are rapidly digitizing pathology workflows, storing data without effective mechanisms for retrieval and reasoning risks transforming archives into a passive data repository, where institutional knowledge exists but cannot meaningfully inform patient care. True progress requires not only digitization, but the ability for pathologists to interrogate prior similar cases in real time while evaluating a new diagnostic dilemma. We present PathoScribe, a unified retrieval-augmented large language model (LLM) framework designed to transform static pathology archives into a searchable, reasoning-enabled living library. PathoScribe enables natural language case exploration, automated cohort construction, clinical question answering, immunohistochemistry (IHC) panel recommendation, and prompt-controlled report transformation within a single architecture. Evaluated on 70,000 multi-institutional surgical pathology reports, PathoScribe achieved perfect Recall@10 for natural language case retrieval and demonstrated high-quality retrieval-grounded reasoning (mean reviewer score 4.56/5). Critically, the system operationalized automated cohort construction from free-text eligibility criteria, assembling research-ready cohorts in minutes (mean 9.2 minutes) with 91.3% agreement to human reviewers and no eligible cases incorrectly excluded, representing orders-of-magnitude reductions in time and cost compared to traditional manual chart review. This work establishes a scalable foundation for converting digital pathology archives from passive storage systems into active clinical intelligence platforms.

</details>

---

### 40. [Tracking Cancer Through Text: Longitudinal Extraction From Radiology Reports Using Open-Source Large Language Models](https://arxiv.org/abs/2603.09638)

**基本信息**

- 🔗 arXiv: [`2603.09638`](https://arxiv.org/abs/2603.09638)
- 👥 作者: Luc Builtjes, Alessa Hering
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09638.pdf)

**💡 相关性分析**

满足标准2：论文提出的开源LLM流程是一种可用于从非结构化文本（如科学报告）中提取结构化信息的工具，这种数据提取和资源构建能力与化学信息学中处理质谱报告、构建结构化知识库的需求高度相关。

**📖 中文摘要**

本文提出了一种完全开源的、可本地部署的流程，用于从放射学报告中提取纵向信息。该系统利用qwen2.5-72b模型，根据RECIST标准提取和关联不同时间点的靶病灶、非靶病灶和新发病灶数据。在50对荷兰语胸部/腹部CT报告上的评估显示，该流程在属性级别取得了高准确率：靶病灶93.7%，非靶病灶94.9%，新发病灶94.0%。这项工作展示了开源大语言模型在临床多时间点肿瘤学任务中实现有意义的性能，同时确保了数据隐私和可复现性。其核心在于利用大语言模型从非结构化的临床文本中提取结构化数据，这直接关联到化学信息学和质谱分析领域中对非结构化科学报告（如质谱实验报告）进行信息提取和知识构建的需求。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Radiology reports capture crucial longitudinal information on tumor burden, treatment response, and disease progression, yet their unstructured narrative format complicates automated analysis. While large language models (LLMs) have advanced clinical text processing, most state-of-the-art systems remain proprietary, limiting their applicability in privacy-sensitive healthcare environments. We present a fully open-source, locally deployable pipeline for longitudinal information extraction from radiology reports, implemented using the llm_extractinator framework. The system applies the qwen2.5-72b model to extract and link target, non-target, and new lesion data across time points in accordance with RECIST criteria. Evaluation on 50 Dutch CT Thorax/Abdomen report pairs yielded high extraction performance, with attribute-level accuracies of 93.7% for target lesions, 94.9% for non-target lesions, and 94.0% for new lesions. The approach demonstrates that open-source LLMs can achieve clinically meaningful performance in multi-timepoint oncology tasks while ensuring data privacy and reproducibility. These results highlight the potential of locally deployable LLMs for scalable extraction of structured longitudinal data from routine clinical text.

</details>

---

### 41. [Fusing Semantic, Lexical, and Domain Perspectives for Recipe Similarity Estimation](https://arxiv.org/abs/2603.09688)

**基本信息**

- 🔗 arXiv: [`2603.09688`](https://arxiv.org/abs/2603.09688)
- 👥 作者: Denica Kjorvezir, Danilo Najkov, Eva Valencič 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09688.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估复杂对象（食谱）的相似性，这涉及到多模态信息（文本、成分、营养）的融合与推理。评估化学结构或质谱谱图的相似性是化学信息学和质谱分析中的核心任务。论文中提出的结合语义、词汇和领域视角的相似性评估框架，其方法论可直接类比或应用于化学结构相似性计算或质谱谱图匹配。

**📖 中文摘要**

本研究专注于通过结合不同信息源和分析方法来评估食谱之间的相似性。我们探索了食物食谱的语义、词汇和领域相似性，通过分析成分、制备方法和营养属性进行评估。开发了一个基于Web的界面，允许领域专家验证组合的相似性结果。在评估了318个食谱对之后，专家对255个（80%）达成一致。对专家评估的分析使得能够估计词汇、语义或营养相似性方面中哪些对专家决策最有影响。这些方法的应用在食品行业具有广泛意义，并支持个性化饮食、营养推荐和自动食谱生成系统的开发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This research focuses on developing advanced methods for assessing similarity between recipes by combining different sources of information and analytical approaches. We explore the semantic, lexical, and domain similarity of food recipes, evaluated through the analysis of ingredients, preparation methods, and nutritional attributes. A web-based interface was developed to allow domain experts to validate the combined similarity results. After evaluating 318 recipe pairs, experts agreed on 255 (80%). The evaluation of expert assessments enables the estimation of which similarity aspects--lexical, semantic, or nutritional--are most influential in expert decision-making. The application of these methods has broad implications in the food industry and supports the development of personalized diets, nutrition recommendations, and automated recipe generation systems.

</details>

---

### 42. [Evaluation of LLMs in retrieving food and nutritional context for RAG systems](https://arxiv.org/abs/2603.09704)

**基本信息**

- 🔗 arXiv: [`2603.09704`](https://arxiv.org/abs/2603.09704)
- 👥 作者: Maks Požarnik Vavken, Matevž Ogrinc, Tome Eftimov 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09704.pdf)

**💡 相关性分析**

满足标准2：论文的核心是评估LLM在RAG系统中作为“自然语言到结构化查询”转换器的性能，用于检索专业的科学数据库（食物成分数据库）。这种构建智能接口以查询专业科学数据库（如化学化合物数据库、质谱库）的技术，正是化学信息学和质谱分析领域所需的关键工具和资源。

**📖 中文摘要**

本文评估了四种大语言模型及其在专门的检索增强生成系统中检索数据的有效性，该系统使用了一个全面的食物成分数据库。我们的方法侧重于LLM将自然语言查询转换为结构化元数据过滤器的能力，从而实现通过Chroma向量数据库进行高效检索。通过在这一关键检索步骤中实现高精度，我们证明LLM可以作为一种易于使用的高性能工具，极大地减少了领域专家（如食物汇编者和营养学家）利用复杂食物和营养数据所需的手动工作和技术专长。然而，尽管在简单和中等复杂度的查询上表现出高性能，我们对困难问题的分析表明，当查询涉及无法表达的约束时，可靠的检索仍然具有挑战性。这些发现表明，当约束可以明确表达时，LLM驱动的元数据过滤表现出色，但当查询超出元数据格式的表征范围时则会遇到困难。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this article, we evaluate four Large Language Models (LLMs) and their effectiveness at retrieving data within a specialized Retrieval-Augmented Generation (RAG) system, using a comprehensive food composition database. Our method is focused on the LLMs ability to translate natural language queries into structured metadata filters, enabling efficient retrieval via a Chroma vector database. By achieving high accuracy in this critical retrieval step, we demonstrate that LLMs can serve as an accessible, high-performance tool, drastically reducing the manual effort and technical expertise previously required for domain experts, such as food compilers and nutritionists, to leverage complex food and nutrition data. However, despite the high performance on easy and moderately complex queries, our analysis of difficult questions reveals that reliable retrieval remains challenging when queries involve non-expressible constraints. These findings demonstrate that LLM-driven metadata filtering excels when constraints can be explicitly expressed, but struggles when queries exceed the representational scope of the metadata format.

</details>

---

### 43. [NMIRacle: Multi-modal Generative Molecular Elucidation from IR and NMR Spectra](https://arxiv.org/abs/2512.19733)

**基本信息**

- 🔗 arXiv: [`2512.19733`](https://arxiv.org/abs/2512.19733)
- 👥 作者: Federico Ottomano, Yingzhen Li, Alex M. Ganose
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.19733.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“质谱结构推理”这一主题，提出了一个从IR和NMR光谱生成分子结构的AI生成框架。

**📖 中文摘要**

本文提出了NMIRacle，一个用于从红外（IR）和核磁共振（NMR）光谱数据中生成分子结构的两阶段生成式框架。该工作直接针对化学信息学中的核心挑战——从光谱数据推断分子结构（即质谱/光谱结构推理）。在第一阶段，模型学习从片段表示重建分子结构。在第二阶段，一个光谱编码器将输入的IR、1H-NMR和13C-NMR光谱映射为潜在嵌入，用于条件化预训练的生成器，从而实现直接从光谱到分子的生成。该方法弥合了片段级化学建模与光谱证据之间的差距，在分子解析任务上优于现有基线，并能在分子复杂性增加时保持鲁棒性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular structure elucidation from spectroscopic data is a long-standing challenge in Chemistry, traditionally requiring expert interpretation. We introduce NMIRacle, a two-stage generative framework that builds upon recent paradigms in AI-driven spectroscopy with minimal assumptions. In the first stage, NMIRacle learns to reconstruct molecular structures from count-aware fragment representations, capturing both fragment identities and their occurrences. In the second stage, a spectral encoder maps input spectra (IR, 1H-NMR, 13C-NMR) into a latent embedding used to condition the pre-trained generator, which is fine-tuned for direct spectra-to-molecule generation. This formulation bridges fragment-level chemical modeling with spectral evidence, yielding accurate molecular predictions. Empirical results demonstrate that NMIRacle outperforms existing baselines on molecular elucidation, while maintaining robust performance across increasing levels of molecular complexity.

</details>

---

### 44. [Benchmarking Graph Neural Networks in Solving Hard Constraint Satisfaction Problems](https://arxiv.org/abs/2602.18419)

**基本信息**

- 🔗 arXiv: [`2602.18419`](https://arxiv.org/abs/2602.18419)
- 👥 作者: Geri Skenderi, Lorenzo Buffoni, Francesco D'Amico 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.18419.pdf)

**💡 相关性分析**

满足标准2：论文提出的基准测试框架和关于GNN能力的分析，为开发和评估用于化学信息学任务（可建模为图上的约束满足或优化问题）的“化学大模型”提供了重要的工具和见解。

**📖 中文摘要**

本文从统计物理学的角度，为图神经网络（GNNs）解决硬约束满足问题（CSPs）提出了新的、基于随机问题的基准测试。作者提供了这些基准以及经典启发式算法和GNNs的性能比较结果。虽然论文主要关注CSPs，但图神经网络是构建“化学大模型”（特别是用于分子表示和性质预测的模型）的核心架构之一。本文对GNN在解决复杂优化问题上的能力进行了严格的基准测试和讨论，指出了当前神经网络的局限性。这项工作为评估和开发用于化学信息学任务（如分子生成、逆合成规划，这些可被视为特殊的约束满足问题）的GNN模型提供了重要的方法论参考和评估标准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph neural networks (GNNs) are increasingly applied to hard optimization problems, often claiming superiority over classical heuristics. However, such claims risk being unsolid due to a lack of standard benchmarks on truly hard instances. From a statistical physics perspective, we propose new hard benchmarks based on random problems. We provide these benchmarks, along with performance results from both classical heuristics and GNNs. Our fair comparison shows that classical algorithms still outperform GNNs. We discuss the challenges for neural networks in this domain. Future claims of superiority can be made more robust using our benchmarks, available at this https URL .

</details>

---

### 45. [Machine Learning on Heterogeneous, Edge, and Quantum Hardware for Particle Physics (ML-HEQUPP)](https://arxiv.org/abs/2602.22248)

**基本信息**

- 🔗 arXiv: [`2602.22248`](https://arxiv.org/abs/2602.22248)
- 👥 作者: Julia Gonski, Jenni Ott, Shiva Abbaszadeh 等100人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.22248.pdf)

**💡 相关性分析**

满足标准2：论文讨论了可用于“化学大模型”和“质谱结构推理”等主题的硬件、系统架构和工具研发方向，特别是边缘AI、异构计算和专用加速器，这些是处理大规模化学数据和运行复杂模型的关键使能技术。

**📖 中文摘要**

这篇白皮书探讨了下一代粒子物理实验在数据获取、实时推理和高效处理架构方面面临的挑战。它强调了利用新兴技术（如人工智能/机器学习、硅微电子学和量子算法）来解决这些挑战的必要性。虽然论文的总体背景是粒子物理学，但它明确将AI/ML（包括可能的化学信息学模型）在边缘计算、异构加速器系统、可重构硬件和模拟计算等领域的应用确定为核心研发方向。这些技术对于处理高维科学数据（如质谱数据）和开发实时推理系统具有广泛的适用性，为相关领域（包括化学信息学和质谱分析）提供了潜在的工具和方法论资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The next generation of particle physics experiments will face a new era of challenges in data acquisition, due to unprecedented data rates and volumes along with extreme environments and operational constraints. Harnessing this data for scientific discovery demands real-time inference and decision-making, intelligent data reduction, and efficient processing architectures beyond current capabilities. Crucial to the success of this experimental paradigm are several emerging technologies, such as artificial intelligence and machine learning (AI/ML), silicon microelectronics, and the advent of quantum algorithms and processing. Their intersection includes areas of research such as low-power and low-latency devices for edge computing, heterogeneous accelerator systems, reconfigurable hardware, novel codesign and synthesis strategies, readout for cryogenic or high-radiation environments, and analog computing. This white paper presents a community-driven vision to identify and prioritize research and development opportunities in hardware-based ML systems and corresponding physics applications, contributing towards a successful transition to the new data frontier of fundamental science.

</details>

---

### 46. [Reinforced Generation of Combinatorial Structures: Ramsey Numbers](https://arxiv.org/abs/2603.09172)

**基本信息**

- 🔗 arXiv: [`2603.09172`](https://arxiv.org/abs/2603.09172)
- 👥 作者: Ansh Nagda, Prabhakar Raghavan, Abhradeep Thakurta
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09172.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论是使用大语言模型（LLM）作为元算法来生成解决科学问题的代码，这直接体现了“化学大模型”主题中“大模型”在自动化科学发现和算法设计方面的应用潜力。

**📖 中文摘要**

本文介绍了AlphaEvolve，一个基于大语言模型（LLM）的代码突变智能体，用于生成解决组合结构（如拉姆齐数）问题的搜索算法。该工作利用LLM作为元算法，自动演化出能够找到组合问题新下界的专用搜索程序。虽然应用领域是组合数学，但其核心方法论——使用大语言模型（作为“大模型”的一种）来自动化算法设计和优化过程——与“化学大模型”的主题高度相关。在化学信息学中，类似的方法可用于自动设计分子生成算法、优化化学反应条件或发现新的材料结构。本文展示了大型生成模型在自动解决复杂科学计算问题方面的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present improved lower bounds for five classical Ramsey numbers: $\mathbf{R}(3, 13)$ is increased from $60$ to $61$, $\mathbf{R}(3, 18)$ from $99$ to $100$, $\mathbf{R}(4, 13)$ from $138$ to $139$, $\mathbf{R}(4, 14)$ from $147$ to $148$, and $\mathbf{R}(4, 15)$ from $158$ to $159$. These results were achieved using AlphaEvolve, an LLM-based code mutation agent. Beyond these new results, we successfully recovered lower bounds for all Ramsey numbers known to be exact, and matched the best known lower bounds across many other cases. These include bounds for which previous work does not detail the algorithms used. Virtually all known Ramsey lower bounds are derived computationally, with bespoke search algorithms each delivering a handful of results. AlphaEvolve is a single meta-algorithm yielding search algorithms for all of our results.

</details>

---

## 📊 数据统计
- 累计运行天数：25
- 累计论文数量：1868

## 📝 历史记录

> 暂无历史数据

