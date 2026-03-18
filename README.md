# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-18 01:43:08

## 📅 2026-03-18 (今日最新)

**相关论文数：109**

### 1. [Tracing the Evolution of Word Embedding Techniques in Natural Language Processing](https://arxiv.org/abs/2603.13271)

**基本信息**

- 🔗 arXiv: [`2603.13271`](https://arxiv.org/abs/2603.13271)
- 👥 作者: Minh Anh Nguyen, Kuheli Sai, Minh Nguyen
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13271.pdf)

**💡 相关性分析**

满足标准3：论文是关于词嵌入技术演变的全面综述，词嵌入是构建化学大模型（如用于分子表示学习）和质谱分析模型（如用于谱图嵌入）的基础技术之一。该综述讨论了从静态到上下文嵌入的演变，这与化学信息学和质谱分析中构建更强大、更具上下文感知能力的模型（如用于结构推理的模型）的发展脉络直接相关。

**📖 中文摘要**

本文系统性地追溯了自然语言处理（NLP）中词嵌入技术从1954年至2025年的演变历程。它全面回顾了四种主要的嵌入范式：基于统计的表示方法（如one-hot编码、词袋模型、TF-IDF）、静态词嵌入（如Word2Vec、GloVe、FastText）、上下文词嵌入（如ELMo、BERT、GPT）以及句子/文档嵌入。论文不仅进行了方法论综述，还以GPT-3的发布为分界线，通过七种假设检验对研究重点、合作模式和机构参与度的转变进行了定量分析。研究发现，GPT-3之后出现了显著的范式转变：上下文和句子级方法的主导地位是GPT-3之前的6.4倍，平均团队规模显著增长，并涌现了30种全新方法，而54种GPT-3之前的方法未再受到关注。这些发现为大语言模型（LLM）时代如何重塑该领域的认知优先级提供了定量描述。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work traces the evolution of word-embedding techniques within the natural language processing (NLP) literature. We collect and analyze 149 research articles spanning the period from 1954 to 2025, providing both a comprehensive methodological review and a data-driven bibliometric analysis of how representation learning has developed over seven decades. Our study covers four major embedding paradigms, statistical representation-based methods (one-hot encoding, bag-of-words, TF-IDF), static word embeddings (Word2Vec, GloVe, FastText), contextual word embeddings (ELMo, BERT, GPT), and sentence/document embeddings, critically discussing the strengths, limitations, and intellectual lineage connecting each category. Beyond the methodological survey, we conduct a formal era comparison using GPT-3's release as a dividing line, applying seven hypothesis tests to quantify shifts in research focus, collaboration patterns, and institutional involvement. Our analysis reveals a dramatic post-GPT-3 paradigm shift: contextual and sentence-level methods now dominate at 6.4X the odds of the pre-GPT-3 era, mean team sizes have grown significantly (p = 0.018), and 30 entirely new techniques have emerged while 54 pre-GPT-3 methods received no further attention. These findings, combined with evidence of rising industry involvement, provide a quantitative account of how the field's epistemic priorities have been reshaped by the advent of large language models.

</details>

---

### 2. [Learning Retrieval Models with Sparse Autoencoders](https://arxiv.org/abs/2603.13277)

**基本信息**

- 🔗 arXiv: [`2603.13277`](https://arxiv.org/abs/2603.13277)
- 👥 作者: Thibault Formal, Maxime Louis, Hervé Dejean 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13277.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于稀疏自编码器（SAE）的新型检索模型训练方法。该方法产生的结构化、语言无关的稀疏潜在嵌入，可作为化学信息学和质谱分析领域构建专用检索系统（例如，用于检索相似分子结构或质谱谱图）的重要工具或数据表示资源。

**📖 中文摘要**

本文提出SPLARE，一种基于稀疏自编码器（SAE）训练学习型稀疏检索（LSR）模型的方法。稀疏自编码器能够将大语言模型（LLM）产生的密集表示分解为可解释的潜在特征。作者认为，与现有将输入序列投影到词汇空间的LSR方法相比，基于SAE的表示有潜力产生更具语义结构、表达力更强且语言无关的特征。实验表明，该方法在多语言和领域外设置下持续优于基于词汇的LSR。SPLARE-7B是一个多语言检索模型，能够为广泛的语言和领域生成可泛化的稀疏潜在嵌入，并在MMTEB的多语言和英语检索任务中取得了顶尖结果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sparse autoencoders (SAEs) provide a powerful mechanism for decomposing the dense representations produced by Large Language Models (LLMs) into interpretable latent features. We posit that SAEs constitute a natural foundation for Learned Sparse Retrieval (LSR), whose objective is to encode queries and documents into high-dimensional sparse representations optimized for efficient retrieval. In contrast to existing LSR approaches that project input sequences into the vocabulary space, SAE-based representations offer the potential to produce more semantically structured, expressive, and language-agnostic features. Building on this insight, we introduce SPLARE, a method to train SAE-based LSR models. Our experiments, relying on recently released open-source SAEs, demonstrate that this technique consistently outperforms vocabulary-based LSR in multilingual and out-of-domain settings. SPLARE-7B, a multilingual retrieval model capable of producing generalizable sparse latent embeddings for a wide range of languages and domains, achieves top results on MMTEB's multilingual and English retrieval tasks. We also developed a 2B-parameter variant with a significantly lighter footprint.

</details>

---

### 3. [Do Diffusion Models Dream of Electric Planes? Discrete and Continuous Simulation-Based Inference for Aircraft Design](https://arxiv.org/abs/2603.13284)

**基本信息**

- 🔗 arXiv: [`2603.13284`](https://arxiv.org/abs/2603.13284)
- 👥 作者: Aurelien Ghiglino, Daniel Elenius, Anirban Roy 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13284.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用扩散模型进行生成式设计。扩散模型是当前生成式AI和“化学大模型”（如用于分子生成或性质预测的模型）中的关键技术。论文提出的分层扩散框架，特别是处理离散-连续混合空间的方法，对于化学信息学中类似的问题（如生成具有特定属性的分子结构）具有直接的借鉴意义，可视为一种“化学大模型”的方法论应用。

**📖 中文摘要**

本文采用基于模拟的推理（SBI）范式，生成电动垂直起降（eVTOL）飞机的概念工程设计。为了学习涵盖离散飞机配置（拓扑）及其对应连续参数的全设计空间的后验分布，作者引入了一个包含两个扩散模型的分层概率模型。第一个模型基于黎曼扩散语言建模（RDLM）和统一世界模型（UWM），用于从离散和连续空间中采样拓扑。第二个模型采用掩码扩散方法，在给定拓扑的条件下采样对应参数。该方法重新发现了飞机设计中已知的趋势和物理定律，同时显著加速了设计生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we generate conceptual engineering designs of electric vertical take-off and landing (eVTOL) aircraft. We follow the paradigm of simulation-based inference (SBI), whereby we look to learn a posterior distribution over the full eVTOL design space. To learn this distribution, we sample over discrete aircraft configurations (topologies) and their corresponding set of continuous parameters. Therefore, we introduce a hierarchical probabilistic model consisting of two diffusion models. The first model leverages recent work on Riemannian Diffusion Language Modeling (RDLM) and Unified World Models (UWMs) to enable us to sample topologies from a discrete and continuous space. For the second model we introduce a masked diffusion approach to sample the corresponding parameters conditioned on the topology. Our approach rediscovers known trends and governing physical laws in aircraft design, while significantly accelerating design generation.

</details>

---

### 4. [DreamReader: An Interpretability Toolkit for Text-to-Image Models](https://arxiv.org/abs/2603.13299)

**基本信息**

- 🔗 arXiv: [`2603.13299`](https://arxiv.org/abs/2603.13299)
- 👥 作者: Nirmalendu Prakash, Narmeen Oozeer, Michael Lan 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13299.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个名为DreamReader的可解释性工具包，专门用于分析和干预文生图扩散模型。该工具包提供的技术（如激活引导、表示微调、跨模型映射）可以作为重要的“工具”或“资源”，用于理解和改进化学信息学或质谱分析中可能使用的类似生成模型（例如，用于分子图生成或质谱预测的扩散模型）的内部工作机制和安全性。

**📖 中文摘要**

本文介绍了DreamReader，一个用于文生图（T2I）扩散模型的可解释性工具包。它提供了一个统一的框架，将扩散模型的可解释性形式化为可组合的表示操作符，涵盖激活提取、因果修补、结构化消融以及跨模块和时间步的激活引导。除了整合现有方法，DreamReader还引入了三种新颖的干预原语：用于子空间约束内部适应的表示微调（LoReFT）、使用在激活上训练的MLP探针的分类器引导梯度引导，以及用于系统研究跨模态表示可迁移性的组件级跨模型映射。通过控制实验，作者展示了从语言模型可解释性技术改编而来的方法能够在扩散模型中产生有前景且可控的干预。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite the rapid adoption of text-to-image (T2I) diffusion models, causal and representation-level analysis remains fragmented and largely limited to isolated probing techniques. To address this gap, we introduce DreamReader: a unified framework that formalizes diffusion interpretability as composable representation operators spanning activation extraction, causal patching, structured ablations, and activation steering across modules and timesteps. DreamReader provides a model-agnostic abstraction layer enabling systematic analysis and intervention across diffusion architectures. Beyond consolidating existing methods, DreamReader introduces three novel intervention primitives for diffusion models: (1) representation fine-tuning (LoReFT) for subspace-constrained internal adaptation; (2) classifier-guided gradient steering using MLP probes trained on activations; and (3) component-level cross-model mapping for systematic study of transferability of representations across modalities. These mechanisms allows us to do lightweight white-box interventions on T2I models by drawing inspiration from interpretability techniques on LLMs. We demonstrate DreamReader through controlled experiments that (i) perform activation stitching between two models, and (ii) apply LoReFT to steer multiple activation units, reliably injecting a target concept into the generated images. Experiments are specified declaratively and executed in controlled batched pipelines to enable reproducible large-scale analysis. Across multiple case studies, we show that techniques adapted from language model interpretability yield promising and controllable interventions in diffusion models. DreamReader is released as an open source toolkit for advancing research on T2I interpretability.

</details>

---

### 5. [Safety-Guided Flow (SGF): A Unified Framework for Negative Guidance in Safe Generation](https://arxiv.org/abs/2603.13300)

**基本信息**

- 🔗 arXiv: [`2603.13300`](https://arxiv.org/abs/2603.13300)
- 👥 作者: Mingyu Kim, Young-Heon Kim, Mijung Park
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13300.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是扩散/流模型中的安全生成机制，提出了一个统一的“安全引导流”框架。这直接关系到构建安全、可控的生成模型，是“化学大模型”（如用于生成新分子或合成路径的模型）在部署前必须考虑的关键问题。论文提出的理论框架和方法对化学领域的安全生成具有重要参考价值。

**📖 中文摘要**

本文为图像生成任务引入了一个统一的概率框架，使用最大均值差异（MMD）势能，将“屏蔽扩散”和“安全去噪器”重新表述为针对不安全数据样本的基于能量的负引导实例。此外，作者利用控制屏障函数分析来证明存在一个关键时间窗口，在此窗口内负引导必须很强；在此窗口之外，引导应衰减至零以确保安全且高质量的生成。该框架在几个现实的安全生成场景中进行了评估，证实了负引导应在去噪过程的早期阶段应用才能成功实现安全生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Safety mechanisms for diffusion and flow models have recently been developed along two distinct paths. In robot planning, control barrier functions are employed to guide generative trajectories away from obstacles at every denoising step by explicitly imposing geometric constraints. In parallel, recent data-driven, negative guidance approaches have been shown to suppress harmful content and promote diversity in generated samples. However, they rely on heuristics without clearly stating when safety guidance is actually necessary. In this paper, we first introduce a unified probabilistic framework using a Maximum Mean Discrepancy (MMD) potential for image generation tasks that recasts both Shielded Diffusion and Safe Denoiser as instances of our energy-based negative guidance against unsafe data samples. Furthermore, we leverage control-barrier functions analysis to justify the existence of a critical time window in which negative guidance must be strong; outside of this window, the guidance should decay to zero to ensure safe and high-quality generation. We evaluate our unified framework on several realistic safe generation scenarios, confirming that negative guidance should be applied in the early stages of the denoising process for successful safe generation.

</details>

---

### 6. [Machine Learning Models to Identify Promising Nested Antiresonance Nodeless Fiber Designs](https://arxiv.org/abs/2603.13302)

**基本信息**

- 🔗 arXiv: [`2603.13302`](https://arxiv.org/abs/2603.13302)
- 👥 作者: Rania A. Eltaieb, Sophie LaRochelle, Leslie A. Rusch
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13302.pdf)

**💡 相关性分析**

满足标准1：论文的核心是使用机器学习（特别是神经网络）来加速和优化复杂物理系统（光纤）的设计。这本质上是一个“基于AI的材料/结构设计”案例，与“化学大模型”用于分子发现、材料设计或反应优化的目标高度一致。论文展示的“小数据学习并外推”范式在数据稀缺的化学领域尤为相关。

**📖 中文摘要**

本文提出了一种高效的两阶段机器学习框架，用于使用最少的训练数据识别高性能嵌套反谐振无节点光纤（NANF）设计。该模型采用神经网络（NN）分类器筛选单模设计，然后使用回归器预测限制损耗（CL）。通过在仅包含1,819个设计（所有设计的CL均大于或等于1 dB/km）的稀疏数据集上进行训练，该模型成功识别出了经确认CL为0.25 dB/km的优化设计。这表明神经网络已经捕捉到了潜在的物理行为，并且能够外推到更低CL的区域。作者展示了小数据集足以实现稳定、高精度的性能预测，从而能够以相对于有限元方法可忽略的计算成本探索多达1400万个案例的设计空间。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hollow-core fibers offer superior loss and latency characteristics compared to solid-core alternatives, yet the geometric complexity of nested antiresonance nodeless fibers (NANFs) makes traditional optimization computationally prohibitive. We propose a high-efficiency, two-stage machine learning framework designed to identify high-performance NANF designs using minimal training data. The model employs a neural network (NN) classifier to filter for single-mode designs (suppression ratio $\ge$ 50 dB), followed by a regressor that predicts confinement loss (CL). By training on the common logarithm of the loss, the regressor overcomes the challenges of high dynamic range. Using a sparse data set of only 1,819 designs, all with CL greater or equal to 1 dB/km, the model successfully identified optimized designs with a confirmed CL of 0.25 dB/km. {This demonstrates the NN has captured underlying physical behavior and is able to extrapolate to regions of lower CL. We show that small data sets are sufficient for stable, high-accuracy performance prediction, enabling the exploration of design spaces as large as $14e6$ cases at a negligible computational cost compared to finite element methods.

</details>

---

### 7. [Suppressing Domain-Specific Hallucination in Construction LLMs: A Knowledge Graph Foundation for GraphRAG and QLoRA on River and Sediment Control Technical Standards](https://arxiv.org/abs/2603.13307)

**基本信息**

- 🔗 arXiv: [`2603.13307`](https://arxiv.org/abs/2603.13307)
- 👥 作者: Takato Yasuno
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13307.pdf)

**💡 相关性分析**

满足标准2：论文详细记录了一个完整的工程流程，包括知识图谱构建、QLoRA训练数据生成、训练和部署。这项工作为解决领域特定（如化学、质谱）问题提供了重要的“工具”和“方法资源”，特别是对比了知识图谱增强（GraphRAG）与参数高效微调（QLoRA）在抑制大模型幻觉、提升专业领域答案准确性方面的效果，对构建化学或质谱领域的专业问答系统具有直接的参考价值。

**📖 中文摘要**

本文解决了使用完全在本地硬件上运行的开源大语言模型（LLM）回答源自日本《河流与泥沙控制技术标准》的技术问题所面临的挑战。作者评估了三种互补方法：案例A（普通的20B LLM基线）、案例B（使用QLoRA在715个图衍生的QA对上进行了领域微调的8B LLM）和案例C（通过GraphRAG用Neo4j知识图谱增强的20B LLM）。关键发现是性能反转：经过QLoRA微调的8B模型在质量上超越了20B的GraphRAG方法和20B的普通基线，同时运行延迟快了3倍。GraphRAG提供了中等增益，但在质量和效率上均被领域特定微调超越。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper addresses the challenge of answering technical questions derived from Japan's River and Sediment Control Technical Standards -- a multi-volume regulatory document covering survey, planning, design, and maintenance of river levees, dams, and sabo structures -- using open-source large language models running entirely on local hardware. We implement and evaluate three complementary approaches: Case A (plain 20B LLM baseline), Case B (8B LLM with QLoRA domain fine-tuning on 715 graph-derived QA pairs), and Case C (20B LLM augmented with a Neo4j knowledge graph via GraphRAG). All three cases use the Swallow series of Japanese-adapted LLMs and are evaluated on a 100-question benchmark spanning 8 technical categories, judged automatically by an independent LLM (Qwen2.5-14B, score 0--3). The key finding is a performance inversion: the 8B QLoRA fine-tuned model (Case B) achieves a judge average of 2.92/3 -- surpassing both the 20B plain baseline (Case A: 2.29/3, $+$0.63) and the 20B GraphRAG approach (Case C: 2.62/3, $+$0.30) -- while running at 3$\times$ faster latency (14.2s vs. 42.2s for Case A). GraphRAG provides moderate gains ($+$0.33 over baseline) but is outperformed by domain-specific fine-tuning in both quality and efficiency. We document the full engineering pipeline, including knowledge graph construction (200 nodes, 268 relations), QLoRA training data generation from Neo4j relations, training on a single GPU (16 GB VRAM) using unsloth, GGUF Q4_K_M quantisation and Ollama deployment, and the graph retrieval and re-ranking design. High-level engineering lessons are distilled in the main body; implementation pitfalls and toolchain details are documented in Supplementary Materials.

</details>

---

### 8. [Neural Approximation and Its Applications](https://arxiv.org/abs/2603.13311)

**基本信息**

- 🔗 arXiv: [`2603.13311`](https://arxiv.org/abs/2603.13311)
- 👥 作者: Wei-Hao Wu, Ting-Zhu Huang, Xi-Le Zhao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13311.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一种新的、基于神经网络的通用函数逼近框架（NeuApprox）。函数逼近是几乎所有机器学习模型的基础，包括“化学大模型”和用于“质谱结构推理”的模型。该框架强调强大的逼近能力和灵活的数据适应性，这为构建更强大、更通用的化学或光谱数据分析模型提供了新的方法论工具，可被视为构建下一代“化学大模型”的底层技术之一。

**📖 中文摘要**

本文针对多元函数逼近这一机器学习基本问题，提出了神经逼近（NeuApprox）范式。作者利用未经训练的神经网络作为基函数，引入神经基函数。基于此，将背后的多元函数分解为多个块项之和。每个具有物理解释性的块项是表达性神经基函数与其对应可学习系数的乘积，这使得模型能够忠实捕捉底层数据的不同组成部分，并通过微调神经基函数灵活适应新数据。得益于精心设计的块项，NeuApprox在逼近能力和数据适应能力上优于基于手工基函数的方法。作者从理论上证明了NeuApprox可以以任意精度逼近任何多元连续函数。在多光谱图像、光场数据、视频、交通数据和点云数据等多种多维数据集上的实验证明了NeuApprox在逼近能力和适应性方面的优异性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multivariate function approximation is a fundamental problem in machine learning. Classic multivariate function approximations rely on hand-crafted basis functions (e.g., polynomial basis and Fourier basis), which limits their approximation ability and data adaptation ability, resulting in unsatisfactory performance. To address these challenges, we introduce the neural basis function by leveraging an untrained neural network as the basis function. Equipped with the proposed neural basis function, we suggest the neural approximation (NeuApprox) paradigm for multivariate function approximation. Specifically, the underlying multivariate function behind the multi-dimensional data is decomposed into a sum of block terms. The clear physically-interpreted block term is the product of expressive neural basis functions and their corresponding learnable coefficients, which allows us to faithfully capture distinct components of the underlying data and also flexibly adapt to new data by readily fine-tuning the neural basis functions. Attributed to the elaborately designed block terms, the suggested NeuApprox enjoys strong approximation ability and flexible data adaptation ability over the hand-crafted basis function-based methods. We also theoretically prove that NeuApprox can approximate any multivariate continuous function to arbitrary accuracy. Extensive experiments on diverse multi-dimensional datasets (including multispectral images, light field data, videos, traffic data, and point cloud data) demonstrate the promising performance of NeuApprox in terms of both approximation capability and adaptability.

</details>

---

### 9. [RBF-Solver: A Multistep Sampler for Diffusion Probabilistic Models via Radial Basis Functions](https://arxiv.org/abs/2603.13330)

**基本信息**

- 🔗 arXiv: [`2603.13330`](https://arxiv.org/abs/2603.13330)
- 👥 作者: Soochul Park, Yeon Ju Lee, SeongJin Yoon 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13330.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进扩散模型的采样算法，这是生成式AI和“化学大模型”（特别是基于扩散的分子生成模型）中的核心组成部分。提出的RBF-Solver通过引入可学习的径向基函数来优化采样轨迹，旨在以更少的步骤获得更高质量的生成结果。这项工作直接提升了扩散模型的效率和性能，对化学领域构建高效的分子生成或谱图生成扩散模型具有重要价值。

**📖 中文摘要**

本文提出了RBF-Solver，一种用于扩散概率模型的多步采样器，它使用高斯径向基函数（RBF）对模型评估进行插值。通过利用高斯RBF中可学习的形状参数，RBF-Solver能够显式地遵循最优采样轨迹。在一阶时，它简化为欧拉方法（DDIM）。在二阶或更高阶时，当形状参数趋近于无穷大时，RBF-Solver收敛于Adams方法，确保了与现有采样器的兼容性。由于高斯RBF的局部性，RBF-Solver即使在四阶或更高阶时也能保持高图像保真度，而之前的采样器在此情况下性能会下降。对于无条件生成，RBF-Solver在高NFE区域（NFE >= 15）持续优于基于多项式的采样器。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion probabilistic models (DPMs) are widely adopted for their outstanding generative fidelity, yet their sampling is computationally demanding. Polynomial-based multistep samplers mitigate this cost by accelerating inference; however, despite their theoretical accuracy guarantees, they generate the sampling trajectory according to a predefined scheme, providing no flexibility for further optimization. To address this limitation, we propose RBF-Solver, a multistep diffusion sampler that interpolates model evaluations with Gaussian radial basis functions (RBFs). By leveraging learnable shape parameters in Gaussian RBFs, RBF-Solver explicitly follows optimal sampling trajectories. At first order, it reduces to the Euler method (DDIM). At second order or higher, as the shape parameters approach infinity, RBF-Solver converges to the Adams method, ensuring its compatibility with existing samplers. Owing to the locality of Gaussian RBFs, RBF-Solver maintains high image fidelity even at fourth order or higher, where previous samplers deteriorate. For unconditional generation, RBF-Solver consistently outperforms polynomial-based samplers in the high-NFE regime (NFE >= 15). On CIFAR-10 with the Score-SDE model, it achieves an FID of 2.87 with 15 function evaluations and further improves to 2.48 with 40 function evaluations. For conditional ImageNet 256 x 256 generation with the Guided Diffusion model at a guidance scale 8.0, substantial gains are achieved in the low-NFE range (5-10), yielding a 16.12-33.73% reduction in FID relative to polynomial-based samplers.

</details>

---

### 10. [Why Grokking Takes So Long: A First-Principles Theory of Representational Phase Transitions](https://arxiv.org/abs/2603.13331)

**基本信息**

- 🔗 arXiv: [`2603.13331`](https://arxiv.org/abs/2603.13331)
- 👥 作者: Truong Xuan Khanh, Truong Quynh Hoa, Luu Duc Trung 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13331.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大模型训练中“顿悟”现象的理论解释和定量分析。“顿悟”是理解模型从记忆到泛化转变的关键现象。这项研究不仅对一般的大语言模型训练有重要意义，对于训练“化学大模型”（例如，用于从大量分子数据中学习泛化规则）同样具有深刻的启示。理解并可能利用“顿悟”机制，有助于设计更高效的化学领域模型训练策略。

**📖 中文摘要**

本文提出了一个关于“顿悟”现象的第一性原理理论。“顿悟”是指在模型完美记忆其训练数据很久之后突然出现的泛化现象。作者证明，“顿悟”源于正则化训练动态中范数驱动的表示相变。训练首先收敛到一个高范数的记忆解，然后才收缩到一个低范数的、可泛化的结构化表示。主要结果建立了延迟时间的标度律：T_grok - T_mem = Θ((1 / γ_eff) * log(||θ_mem||^2 / ||θ_post||^2))，其中γ_eff是优化器的有效收缩率。该上界源自离散李雅普诺夫收缩论证，匹配的下界源于正则化一阶优化的动力学约束。在涵盖模加法、模乘法和稀疏奇偶性任务的293次训练运行中，作者确认了三个预测：与权重衰减成反比缩放、与学习率成反比缩放、以及对范数比的对数依赖关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Grokking is the sudden generalization that appears long after a model has perfectly memorized its training data. Although this phenomenon has been widely observed, there is still no quantitative theory explaining the length of the delay between memorization and generalization. Prior work has noted that weight decay plays an important role, but no result derives tight bounds for the delay or explains its scaling behavior. We present a first-principles theory showing that grokking arises from a norm-driven representational phase transition in regularized training dynamics. Training first converges to a high-norm memorization solution and only later contracts toward a lower-norm structured representation that generalizes. Our main result establishes a scaling law for the delay: T_grok - T_mem = Theta((1 / gamma_eff) * log(||theta_mem||^2 / ||theta_post||^2)), where gamma_eff is the effective contraction rate of the optimizer (gamma_eff = eta * lambda for SGD and gamma_eff >= eta * lambda for AdamW). The upper bound follows from a discrete Lyapunov contraction argument, and the matching lower bound arises from dynamical constraints of regularized first-order optimization. Across 293 training runs spanning modular addition, modular multiplication, and sparse parity tasks, we confirm three predictions: inverse scaling with weight decay, inverse scaling with learning rate, and logarithmic dependence on the norm ratio (R^2 > 0.97). We further find that grokking requires an optimizer that can decouple memorization from contraction: SGD fails under hyperparameters where AdamW reliably groks. These results show that grokking is a predictable consequence of norm separation between competing interpolating representations and provide the first quantitative scaling law for the delay of grokking.

</details>

---

### 11. [MS2MetGAN: Latent-space adversarial training for metabolite-spectrum matching in MS/MS database search](https://arxiv.org/abs/2603.13342)

**基本信息**

- 🔗 arXiv: [`2603.13342`](https://arxiv.org/abs/2603.13342)
- 👥 作者: Meng Tsai, Alexzander Dwyer, Estelle Nuckels 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13342.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕“质谱结构推理”主题，提出了一种用于代谢物鉴定的新机器学习框架MS2MetGAN，旨在从串联质谱（MS/MS）数据中推断化学结构。

**📖 中文摘要**

本文提出了一种名为MS2MetGAN的新框架，用于改进基于数据库搜索的代谢物鉴定。该框架的核心是利用机器学习方法提升代谢物-谱图匹配的准确性。具体而言，它首先使用自编码器学习代谢物化学结构和串联质谱（MS/MS）的潜在表示，从而将匹配问题转化为潜在向量之间的匹配。然后，它使用生成对抗网络（GAN）生成“诱饵”代谢物的潜在向量，并构建负样本用于训练。实验结果表明，MS2MetGAN在代谢物鉴定准确性上优于现有方法。这项工作直接针对“质谱结构推理”这一核心主题，提出了一种新的机器学习框架来从质谱数据中推断化学结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Database search is a widely used approach for identifying metabolites from tandem mass spectra (MS/MS). In this strategy, an experimental spectrum is matched against a user-specified database of candidate metabolites, and candidates are ranked such that true metabolite-spectrum matches receive the highest scores. Machine-learning methods have been widely incorporated into database-search-based identification tools and have substantially improved performance. To further improve identification accuracy, we propose a new framework for generating negative training samples. The framework first uses autoencoders to learn latent representations of metabolite structures and MS/MS spectra, thereby recasting metabolite-spectrum matching as matching between latent vectors. It then uses a GAN to generate latent vectors of decoy metabolites and constructs decoy metabolite-spectrum matches as negative samples for training. Experimental results show that our tool, MS2MetGAN, achieves better overall performance than existing metabolite identification methods.

</details>

---

### 12. [Local Precise Refinement: A Dual-Gated Mixture-of-Experts for Enhancing Foundation Model Generalization against Spectral Shifts](https://arxiv.org/abs/2603.13352)

**基本信息**

- 🔗 arXiv: [`2603.13352`](https://arxiv.org/abs/2603.13352)
- 👥 作者: Xi Chen, Maojun Zhang, Yu Liu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13352.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法论（基于混合专家MoE的、针对基础大模型的参数高效微调框架）与“化学大模型”主题中关于大模型适应、微调和领域泛化的技术讨论直接相关。

**📖 中文摘要**

本文提出了一种名为SpectralMoE的新型参数高效微调（PEFT）框架，用于解决光谱遥感图像中的领域泛化语义分割问题。该框架利用混合专家（MoE）架构对基础模型的特征进行局部精细化调整，以应对不同采集条件导致的光谱偏移。虽然论文的应用领域是遥感图像，但其核心方法——利用MoE架构对基础模型（可视为一种“大模型”）进行高效、细粒度的适应和调整——与“化学大模型”主题中关于大模型高效微调、适应特定领域（如化学）的核心思想高度相关。论文展示了如何通过创新的架构设计来增强基础模型在复杂、异构数据上的泛化能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Domain Generalization Semantic Segmentation (DGSS) in spectral remote sensing is severely challenged by spectral shifts across diverse acquisition conditions, which cause significant performance degradation for models deployed in unseen domains. While Parameter-Efficient Fine-Tuning (PEFT) on foundation models is a promising direction, existing methods employ global, homogeneous adjustments. This "one-size-fits-all" tuning struggles with the spatial heterogeneity of land cover, causing semantic confusion. We argue that the key to robust DGSS lies not in a single global adaptation, but in performing fine-grained, spatially-adaptive refinement of a foundation model's features. To achieve this, we propose SpectralMoE, a novel PEFT framework for DGSS. It operationalizes this principle by utilizing a Mixture-of-Experts (MoE) architecture to perform local precise refinement on the foundation model's features, incorporating depth features estimated from selected RGB bands of the spectral remote sensing imagery to guide the fine-tuning process. Specifically, SpectralMoE employs a dual-gated MoE architecture that independently routes visual and depth features to top-k selected experts for specialized refinement, enabling modality-specific adjustments. A subsequent cross-attention mechanism then judiciously fuses the refined structural cues into the visual stream, mitigating semantic ambiguities caused by spectral variations. Extensive experiments show that SpectralMoE sets a new state-of-the-art on multiple DGSS benchmarks across hyperspectral, multispectral, and RGB remote sensing imagery.

</details>

---

### 13. [GraphVLM: Benchmarking Vision Language Models for Multimodal Graph Learning](https://arxiv.org/abs/2603.13370)

**基本信息**

- 🔗 arXiv: [`2603.13370`](https://arxiv.org/abs/2603.13370)
- 👥 作者: Jiajin Liu, Dongzhe Fan, Chuanhao Ji 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13370.pdf)

**💡 相关性分析**

满足标准3：论文是专门针对“视觉语言模型在多模态图学习中的应用”这一主题的系统性综述和基准构建工作。其中关于大模型（VLMs）如何处理和推理结构化数据（如图）的讨论，为“化学大模型”如何应用于化学图数据（如分子图）提供了重要的相关讨论和评估范式参考。

**📖 中文摘要**

本文提出了GraphVLM，一个系统性的基准测试，旨在评估和利用视觉语言模型（VLMs）在多模态图学习（MMGL）中的能力。论文探讨了将VLMs与图推理结合的三种范式，并进行了广泛的实验。虽然其应用背景是通用的多模态图学习（如社交网络、推荐系统），但GraphVLM基准测试的构建思想、以及其评估VLM作为编码器、对齐器和预测器的方法论，对于在化学信息学领域构建和评估“化学大模型”（例如，用于分子图、反应预测、性质预测的多模态大模型）具有重要的参考价值和前瞻性。它为解决如何让大模型理解和推理结构化数据（如图结构）这一关键问题提供了系统性的评估框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-Language Models (VLMs) have demonstrated remarkable capabilities in aligning and understanding multimodal signals, yet their potential to reason over structured data, where multimodal entities are connected through explicit relational graphs, remains largely underexplored. Unlocking this capability is crucial for real-world applications such as social networks, recommendation systems, and scientific discovery, where multimodal information is inherently structured. To bridge this gap, we present GraphVLM, a systematic benchmark designed to evaluate and harness the capabilities of VLMs for multimodal graph learning (MMGL). GraphVLM investigates three complementary paradigms for integrating VLMs with graph reasoning: (1) VLM-as-Encoder, which enriches graph neural networks through multimodal feature fusion; (2) VLM-as-Aligner, which bridges modalities in latent or linguistic space to facilitate LLM-based structured reasoning; and (3) VLM-as-Predictor, which directly employs VLMs as multimodal backbones for graph learning tasks. Extensive experiments across six datasets from diverse domains demonstrate that VLMs enhance multimodal graph learning via all three roles. Among these paradigms, VLM-as-Predictor achieves the most substantial and consistent performance gains, revealing the untapped potential of vision-language models as a new foundation for multimodal graph learning. The benchmark code is publicly available at this https URL .

</details>

---

### 14. [Deep Learning for BioImaging: What Are We Learning?](https://arxiv.org/abs/2603.13377)

**基本信息**

- 🔗 arXiv: [`2603.13377`](https://arxiv.org/abs/2603.13377)
- 👥 作者: Ivan Svatko, Maxime Sanchez, Ihab Bendidi 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13377.pdf)

**💡 相关性分析**

满足标准3：论文包含对深度学习在科学图像（显微镜）中表征学习能力的系统性评估和重要讨论。这些关于模型学到了什么、如何评估表征质量、以及现有基准局限性的深刻见解，与“化学大模型”和“质谱分析”领域（同样涉及复杂科学数据的建模与评估）的研究高度相关，提供了重要的跨领域参考。

**📖 中文摘要**

本文对显微镜图像的表征学习进行了系统性研究，探讨了当前深度学习方法在生物成像中学到了什么。研究通过引入一系列简单的基线方法（如未训练模型、简单的细胞组织结构表示），并与最先进的方法进行比较，发现现有模型在获取高级别、具有生物学意义的特征方面存在局限。论文指出，常用的基准测试指标不足以评估表征质量。这项工作虽然聚焦于生物显微镜图像，但其核心问题——如何评估和提升深度学习模型在科学数据（如化学结构、质谱图像）上的表征学习能力——与“化学大模型”和“质谱分析”领域面临的挑战高度相似。它为思考如何构建和评估化学领域的大模型或专用模型提供了重要的方法论启示和批判性视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Representation learning has driven major advances in natural image analysis by enabling models to acquire high-level semantic features. In microscopy imaging, however, it remains unclear what current representation learning methods actually learn. In this work, we conduct a systematic study of representation learning for the two most widely used and broadly available microscopy data types, representing critical scales in biology: cell culture and tissue imaging. To this end, we introduce a set of simple yet revealing baselines on curated benchmarks, including untrained models and simple structural representations of cellular tissue. Our results show that, surprisingly, state-of-the-art methods perform comparably to these baselines. We further show that, in contrast to natural images, existing models fail to consistently acquire high-level, biologically meaningful features. Moreover, we demonstrate that commonly used benchmark metrics are insufficient to assess representation quality and often mask this limitation. In addition, we investigate how detailed comparisons with these benchmarks provide ways to interpret the strengths and weaknesses of models for further improvements. Together, our results suggest that progress in microscopy image representation learning requires not only stronger models, but also more diagnostic benchmarks that measure what is actually learned.

</details>

---

### 15. [MAD: Microenvironment-Aware Distillation -- A Pretraining Strategy for Virtual Spatial Omics from Microscopy](https://arxiv.org/abs/2603.13401)

**基本信息**

- 🔗 arXiv: [`2603.13401`](https://arxiv.org/abs/2603.13401)
- 👥 作者: Jiashu Han, Kunzan Liu, Yeojin Kim 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13401.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种新颖的、用于显微镜图像的表征学习预训练策略（MAD），其核心方法论（多视图自蒸馏学习通用、可迁移的细胞表征）与“化学大模型”主题中关于从科学数据学习通用表征以支持下游任务（如性质预测、结构推理）的研究直接相关。

**📖 中文摘要**

本文提出了MAD（微环境感知蒸馏），一种用于显微镜图像的表征学习预训练策略。该方法通过联合自蒸馏同一索引细胞的形态学视图和微环境视图，学习细胞中心的嵌入表示，旨在实现从图像到分子状态的“虚拟空间组学”分析。MAD在多种组织和成像模态上实现了最先进的预测性能，甚至在模型参数数量相似但训练数据量更大的基础模型上表现更优。这项工作展示了通过创新的预训练策略，使模型能够有效捕捉组织内细胞的复杂性和多样性。其核心思想——通过多视图自监督学习从显微图像中提取具有生物学意义的、可用于下游预测任务（如转录组预测）的表征——与“化学大模型”中关于从科学数据（如化学结构图像、光谱图）学习通用、可迁移表征的目标高度一致，为化学信息学中的类似问题提供了方法论借鉴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bridging microscopy and omics would allow us to read molecular states from images-at single-cell resolution and tissue scale-without the cost and throughput limits of omics technologies. Self-supervised pretraining offers a scalable approach with minimal labels, yet how to encode single-cell identity within tissue environments-and the extent of biological information such models can capture-remains an open question. Here, we introduce MAD (microenvironment-aware distillation), a pretraining strategy that learns cell-centric embeddings by jointly self-distilling the morphology view and the microenvironment view of the same indexed cell into a unified embedding space. Across diverse tissues and imaging modalities, MAD achieves state-of-the-art prediction performance on downstream tasks including cell subtyping, transcriptomic prediction, and bioinformatic inference. MAD even outperforms foundation models with a similar number of model parameters that have been trained on substantially larger datasets. These results demonstrate that MAD's dual-view joint self-distillation effectively captures the complexity and diversity of cells within tissues. Together, this establishes MAD as a general tool for representation learning in microscopy, enabling virtual spatial omics and biological insights from vast microscopy datasets.

</details>

---

### 16. [CHIMERA-Bench: A Benchmark Dataset for Epitope-Specific Antibody Design](https://arxiv.org/abs/2603.13431)

**基本信息**

- 🔗 arXiv: [`2603.13431`](https://arxiv.org/abs/2603.13431)
- 👥 作者: Mansoor Ahmed, Nadeem Taj, Imdad Ullah Khan 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13431.pdf)

**💡 相关性分析**

满足标准2：论文提供了CHIMERA-Bench这一大规模、精心策划的基准数据集，专门用于评估表位条件化的抗体设计方法。该数据集的构建理念、划分方法和评估协议，可作为“化学大模型”（如分子生成）和“质谱结构推理”（如结构鉴定）领域构建类似基准的重要参考资源和工具。

**📖 中文摘要**

本文介绍了CHIMERA-Bench，一个用于表位特异性抗体设计的统一基准数据集。针对计算抗体设计领域缺乏标准化评估的问题，该基准围绕一个规范任务构建：表位条件化的互补决定区（CDR）序列-结构协同设计。它提供了经过整理的抗体-抗原复合物数据集、具有生物学意义的划分（测试对未见表位、抗原折叠的泛化能力）以及全面的评估协议。CHIMERA-Bench是此类问题中最大的数据集，旨在促进新方法的开发和测试。虽然专注于抗体设计，但其构建标准化基准以公平比较和推动深度生成方法发展的理念，完全适用于“化学大模型”和“质谱结构推理”领域。它为如何构建评估化学分子生成、质谱解析等任务的基准提供了优秀的范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational antibody design has seen rapid methodological progress, with dozens of deep generative methods proposed in the past three years, yet the field lacks a standardized benchmark for fair comparison and model development. These methods are evaluated on different SAbDab snapshots, non-overlapping test sets, and incompatible metrics, and the literature fragments the design problem into numerous sub-tasks with no common definition. We introduce \textsc{Chimera-Bench} (\textbf{C}DR \textbf{M}odeling with \textbf{E}pitope-guided \textbf{R}edesign), a unified benchmark built around a single canonical task: \emph{epitope-conditioned CDR sequence-structure co-design}. \textsc{Chimera-Bench} provides (1) a curated, deduplicated dataset of \textbf{2,922} antibody-antigen complexes with epitope and paratope annotations; (2) three biologically motivated splits testing generalization to unseen epitopes, unseen antigen folds, and prospective temporal targets; and (3) a comprehensive evaluation protocol with five metric groups including novel epitope-specificity measures. We benchmark representative methods spanning different generative paradigms and report results across all splits. \textsc{Chimera-Bench} is the largest dataset of its kind for the antibody design problem, allowing the community to develop and test novel methods and evaluate their generalizability. The source code and data are available at: this https URL

</details>

---

### 17. [Spatial Transcriptomics as Images for Large-Scale Pretraining](https://arxiv.org/abs/2603.13432)

**基本信息**

- 🔗 arXiv: [`2603.13432`](https://arxiv.org/abs/2603.13432)
- 👥 作者: Yishun Zhu, Jiaxin Qi, Jian Wang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13432.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种将空间转录组学（ST）数据重构为图像形式以进行大规模预训练的新范式。这种方法论创新与“化学大模型”主题高度相关，因为它展示了如何将复杂的科学数据适配到现有的大模型架构（如图像模型）中进行有效学习，为化学领域数据的类似处理（如分子图、光谱图、化学空间表示）提供了直接的技术思路。

**📖 中文摘要**

本文提出将空间转录组学（ST）数据视为可裁剪的图像，以解决其大规模预训练中“训练样本”定义不明确的问题。作者构建了一种固定空间大小的多通道图像表示（通过从原始幻灯片中裁剪斑块），从而在保留空间上下文的同时大幅增加训练样本数量。实验表明，这种图像化的数据集构建方式能持续提升下游任务性能。这项工作为组织ST数据以实现大规模预训练建立了一个统一、实用的范式。其核心创新——将高维、结构复杂的科学数据（ST）重新组织为适合现代深度学习架构（如图像模型）处理的形式——对于“化学大模型”和“质谱分析”领域具有直接的启发性。例如，可以将分子结构、质谱数据或化学空间信息类似地“图像化”或“序列化”，以利用强大的预训练模型（如视觉或语言大模型）进行迁移学习。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Spatial Transcriptomics (ST) profiles thousands of gene expression values at discrete spots with precise coordinates on tissue sections, preserving spatial context essential for clinical and pathological studies. With rising sequencing throughput and advancing platforms, the expanding data volumes motivate large-scale ST pretraining. However, the fundamental unit for pretraining, i.e., what constitutes a single training sample, remains ill-posed. Existing choices fall into two camps: (1) treating each spot as an independent sample, which discards spatial dependencies and collapses ST into single-cell transcriptomics; and (2) treating an entire slide as a single sample, which produces prohibitively large inputs and drastically fewer training examples, undermining effective pretraining. To address this gap, we propose treating spatial transcriptomics as croppable images. Specifically, we define a multi-channel image representation with fixed spatial size by cropping patches from raw slides, thereby preserving spatial context while substantially increasing the number of training samples. Along the channel dimension, we define gene subset selection rules to control input dimensionality and improve pretraining stability. Extensive experiments show that the proposed image-like dataset construction for ST pretraining consistently improves downstream performance, outperforming conventional pretraining schemes. Ablation studies verify that both spatial patching and channel design are necessary, establishing a unified, practical paradigm for organizing ST data and enabling large-scale pretraining.

</details>

---

### 18. [Deep Invertible Autoencoders for Dimensionality Reduction of Dynamical Systems](https://arxiv.org/abs/2603.13496)

**基本信息**

- 🔗 arXiv: [`2603.13496`](https://arxiv.org/abs/2603.13496)
- 👥 作者: Nicolò Botteghi, Silke Glas, Christoph Brune
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13496.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于高维科学数据降维的深度可逆自编码器。虽然未直接提及化学大模型或质谱，但其研究的降维和特征学习方法是化学信息学中构建和处理化学数据（包括质谱数据）模型的基础技术，与‘化学大模型’主题中涉及的数据表示和模型架构高度相关。

**📖 中文摘要**

本文提出了一种深度可逆自编码器（inv-AE）架构，用于高维参数化动力系统的降阶建模。该方法通过结合可逆神经网络层，逐步从高维全阶模型解中恢复信息，从而缓解了传统自编码器在增加降维流形维度时出现的投影误差停滞问题。该工作属于化学信息学中用于处理高维科学数据（如分子动力学模拟或光谱数据）的机器学习模型开发范畴。提出的inv-AE架构作为一种先进的降维和特征提取工具，可以潜在地应用于处理质谱等高维化学数据，为后续的分析和推理任务（如结构推断）构建更有效的低维表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Constructing reduced-order models (ROMs) capable of efficiently predicting the evolution of high-dimensional, parametric systems is crucial in many applications in engineering and applied sciences. A popular class of projection-based ROMs projects the high-dimensional full-order model (FOM) dynamics onto a low-dimensional manifold. These projection-based ROMs approaches often rely on classical model reduction techniques such as proper orthogonal decomposition (POD) or, more recently, on neural network architectures such as autoencoders (AEs). In the case that the ROM is constructed by the POD, one has approximation guaranteed based based on the singular values of the problem at hand. However, POD-based techniques can suffer from slow decay of the singular values in transport- and advection-dominated problems. In contrast to that, AEs allow for better reduction capabilities than the POD, often with the first few modes, but at the price of theoretical considerations. In addition, it is often observed, that AEs exhibits a plateau of the projection error with the increment of the dimension of the trial manifold. In this work, we propose a deep invertible AE architecture, named inv-AE, that improves upon the stagnation of the projection error typical of traditional AE architectures, e.g., convolutional, and the reconstructions quality. Inv-AE is composed of several invertible neural network layers that allows for gradually recovering more information about the FOM solutions the more we increase the dimension of the reduced manifold. Through the application of inv-AE to a parametric 1D Burgers' equation and a parametric 2D fluid flow around an obstacle with variable geometry, we show that (i) inv-AE mitigates the issue of the characteristic plateau of (convolutional) AEs and (ii) inv-AE can be combined with popular projection-based ROM approaches to improve their accuracy.

</details>

---

### 19. [Efficient Sketching-Based Summation of Tucker Tensors](https://arxiv.org/abs/2603.13532)

**基本信息**

- 🔗 arXiv: [`2603.13532`](https://arxiv.org/abs/2603.13532)
- 👥 作者: Rudi Smith, Mirjeta Pasha, Andrés Galindo-Olarte 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13532.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对科学计算中张量运算的高效算法。虽然应用领域是偏微分方程数值解，但其核心方法——处理高维张量数据的压缩和近似算法——是化学信息学和计算化学中的关键技术。化学大模型（如用于分子性质预测的模型）经常涉及高维张量运算，本文提出的高效张量求和方法为处理此类大规模化学数据提供了潜在的算法工具。

**📖 中文摘要**

本文提出了基于草图技术的高效Tucker张量求和方法。该方法利用Khatri-Rao和Kronecker乘积的代数结构，在控制秩增长和计算成本的同时，实现对Tucker格式张量的压缩算术运算。所提出的草图框架避免了显式形成大型中间张量，而是直接对因子矩阵和核心张量进行操作，以产生张量和的精确低秩近似。论文通过数值实验验证了该方法在参数依赖椭圆方程和一维线性输运问题等高阶不连续伽辽金离散化中的应用有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present efficient, sketching-based methods for the summation of tensors in Tucker format. Leveraging the algebraic structure of Khatri-Rao and Kronecker products, our approach enables compressed arithmetic on Tucker tensors while controlling rank growth and computational cost. The proposed sketching framework avoids the explicit formation of large intermediate tensors, instead operating directly on the factor matrices and core tensors to produce accurate low-rank approximations of tensor sums. Furthermore, we analyze the computational complexity and the theoretical approximation properties of the proposed methodology. Numerical experiments demonstrate the effectiveness of our approach on four problems: two synthetic test cases, a parameter-dependent elliptic equation (commonly referred to as the cookie problem) solved via GMRES, and a one-dimensional linear transport problem discretized via high-order discontinuous Galerkin methods, where repeated tensor summation arises as a core computational bottleneck. Across these examples, the sketching-based summation achieves substantial computational savings while preserving high accuracy relative to direct summation and re-compression.

</details>

---

### 20. [BERTology of Molecular Property Prediction](https://arxiv.org/abs/2603.13627)

**基本信息**

- 🔗 arXiv: [`2603.13627`](https://arxiv.org/abs/2603.13627)
- 👥 作者: Mohammad Mostafanejad, Paul Saxe, T. Daniel Crawford
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13627.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕‘化学大模型’主题。它专门研究化学语言模型在分子性质预测任务上的性能，系统分析影响其表现的各种因素，是构建和优化化学大模型的关键工作。

**📖 中文摘要**

本文对化学语言模型在分子性质预测任务上的性能进行了系统性研究。通过数百个精心控制的实验，系统性地调查了数据集大小、模型大小和标准化等各种因素对CLMs预训练和微调性能的影响。研究旨在提供全面的数值证据，并深入理解影响CLMs在MPP任务上性能的潜在机制，其中一些机制在现有文献中被完全忽视。该工作直接针对化学信息学中‘化学大模型’（具体指化学语言模型）的核心议题，即模型性能的评估、理解和优化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chemical language models (CLMs) have emerged as promising competitors to popular classical machine learning models for molecular property prediction (MPP) tasks. However, an increasing number of studies have reported inconsistent and contradictory results for the performance of CLMs across various MPP benchmark tasks. In this study, we conduct and analyze hundreds of meticulously controlled experiments to systematically investigate the effects of various factors, such as dataset size, model size, and standardization, on the pre-training and fine-tuning performance of CLMs for MPP. In the absence of well-established scaling laws for encoder-only masked language models, our aim is to provide comprehensive numerical evidence and a deeper understanding of the underlying mechanisms affecting the performance of CLMs for MPP tasks, some of which appear to be entirely overlooked in the literature.

</details>

---

### 21. [Benchmarking Large Language Models on Reference Extraction and Parsing in the Social Sciences and Humanities](https://arxiv.org/abs/2603.13651)

**基本信息**

- 🔗 arXiv: [`2603.13651`](https://arxiv.org/abs/2603.13651)
- 👥 作者: Yurui Zhu, Giovanni Colavizza, Matteo Romanello
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13651.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个用于评估LLMs在特定领域（SSH）文本处理任务性能的基准测试框架、数据集和评估方法。虽然主题是文献解析，但其构建的基准（如CEX, EXCITE, LinkedBooks数据集）和评估流程本身是一种‘数据资源’和‘工具’，可用于测试和比较不同模型（包括潜在的化学领域LLMs）处理结构化科学文本的能力。

**📖 中文摘要**

本文提出了一个统一的基准测试，用于评估大型语言模型在社会科学和人文科学领域的参考文献提取和解析任务上的性能。该基准针对SSH领域的现实条件，包括多语言引用、脚注嵌入、缩写和异构历史惯例等挑战。研究评估了三个难度递增的任务——参考文献提取、参考文献解析和端到端文档解析，并在模式约束设置下比较了监督基线（GROBID）与当代LLMs（如DeepSeek-V3.1, Mistral, Gemma, Qwen3-VL）的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Bibliographic reference extraction and parsing are foundational for citation indexing, linking, and downstream scholarly knowledge-graph construction. However, most established evaluations focus on clean, English, end-of-document bibliographies, and therefore underrepresent the Social Sciences and Humanities (SSH), where citations are frequently multilingual, embedded in footnotes, abbreviated, and shaped by heterogeneous historical conventions. We present a unified benchmark that targets these SSH-realistic conditions across three complementary datasets: CEX (English journal articles spanning multiple disciplines), EXCITE (German/English documents with end-section, footnote-only, and mixed regimes), and LinkedBooks (humanities references with strong stylistic variation and multilinguality). We evaluate three tasks of increasing difficulty -- reference extraction, reference parsing, and end-to-end document parsing -- under a schema-constrained setup that enables direct comparison between a strong supervised pipeline baseline (GROBID) and contemporary LLMs (DeepSeek-V3.1, Mistral-Small-3.2-24B, Gemma-3-27B-it, and Qwen3-VL (4B-32B variants)). Across datasets, extraction largely saturates beyond a moderate capability threshold, while parsing and end-to-end parsing remain the primary bottlenecks due to structured-output brittleness under noisy layouts. We further show that lightweight LoRA adaptation yields consistent gains -- especially on SSH-heavy benchmarks -- and that segmentation/pipelining can substantially improve robustness. Finally, we argue for hybrid deployment via routing: leveraging GROBID for well-structured, in-distribution PDFs while escalating multilingual and footnote-heavy documents to task-adapted LLMs.

</details>

---

### 22. [Privacy Preserving Topic-wise Sentiment Analysis of the Iran Israel USA Conflict Using Federated Transformer Models](https://arxiv.org/abs/2603.13655)

**基本信息**

- 🔗 arXiv: [`2603.13655`](https://arxiv.org/abs/2603.13655)
- 👥 作者: Md Saiful Islam, Tanjim Taharat Aurpa, Sharad Hasan 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13655.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个结合主题建模、Transformer模型微调和联邦学习的完整分析框架。虽然应用领域是社交媒体情感分析，但其框架（包括数据处理、模型选择与训练、隐私保护机制）为构建和分析大规模文本数据（例如科学文献或实验报告）提供了可复用的工具和方法论，属于可用于相关主题的数据处理工具。

**📖 中文摘要**

本研究旨在通过挖掘YouTube新闻频道的用户评论，分析全球公众关于伊朗-以色列-美国冲突的情绪。工作引入了一个结合主题情感分析与现代深度学习技术及联邦学习的隐私保护框架。收集了约19,000条YouTube评论，使用VADER情感分析器生成初始情感标签，并应用LDA识别关键讨论主题。研究微调了多种基于Transformer的模型进行情感分类，并将性能最佳的模型集成到联邦学习环境中以实现分布式训练并保护用户数据隐私。此外，应用SHAP的XAI技术来解释模型预测。实验结果表明，Transformer模型表现有效，其中ELECTRA取得了最佳性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The recent escalation of the Iran Israel USA conflict in 2026 has triggered widespread global discussions across social media platforms. As people increasingly use these platforms for expressing opinions, analyzing public sentiment from these discussions can provide valuable insights into global public perception. This study aims to analyze global public sentiment regarding the Iran Israel USA conflict by mining user-generated comments from YouTube news channels. The work contributes to public opinion analysis by introducing a privacy preserving framework that combines topic wise sentiment analysis with modern deep learning techniques and Federated Learning. To achieve this, approximately 19,000 YouTube comments were collected from major international news channels and preprocessed to remove noise and normalize text. Sentiment labels were initially generated using the VADER sentiment analyzer and later validated through manual inspection to improve reliability. Latent Dirichlet Allocation (LDA) was applied to identify key discussion topics related to the conflict. Several transformer-based models, including BERT, RoBERTa, XLNet, DistilBERT, ModernBERT, and ELECTRA, were fine tuned for sentiment classification. The best-performing model was further integrated into a federated learning environment to enable distributed training by preserving user data privacy. Additionally, Explainable Artificial Intelligence (XAI) techniques using SHAP were applied to interpret model predictions and identify influential words affecting sentiment classification. Experimental results demonstrate that transformer models perform effectively, and among them, ELECTRA achieved the best performance with 91.32% accuracy. The federated learning also maintained strong performance while preserving privacy, achieving 89.59% accuracy in a two client configuration.

</details>

---

### 23. [LLM-MINE: Large Language Model based Alzheimer's Disease and Related Dementias Phenotypes Mining from Clinical Notes](https://arxiv.org/abs/2603.13673)

**基本信息**

- 🔗 arXiv: [`2603.13673`](https://arxiv.org/abs/2603.13673)
- 👥 作者: Mingchen Shao, Yuzhang Xie, Carl Yang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13673.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个基于LLM的框架（LLM-MINE），用于从非结构化文本中提取特定领域的（医学）信息。该框架本身是一种‘工具’，其方法论（使用LLM进行少样本提示和信息提取）可以迁移到化学信息学领域，例如从科学文献中提取分子结构-性质关系或反应条件，为构建化学大模型提供数据支持。

**📖 中文摘要**

本文提出了LLM-MINE，一个基于大型语言模型的表型挖掘框架，用于从临床笔记中自动提取阿尔茨海默病及相关痴呆症的表型。使用两个专家定义的表型列表，通过检查跨队列的表型统计显著性及其在无监督疾病分期中的效用来评估提取的表型。卡方分析证实了跨队列的表型差异具有统计显著性。结合表型列表的少样本提示实现了最佳的聚类性能。结果表明，基于LLM的表型提取是从非结构化文本中发现具有临床意义的ADRD信号的有前途的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate extraction of Alzheimer's Disease and Related Dementias (ADRD) phenotypes from electronic health records (EHR) is critical for early-stage detection and disease staging. However, this information is usually embedded in unstructured textual data rather than tabular data, making it difficult to be extracted accurately. We therefore propose LLM-MINE, a Large Language Model-based phenotype mining framework for automatic extraction of ADRD phenotypes from clinical notes. Using two expert-defined phenotype lists, we evaluate the extracted phenotypes by examining their statistical significance across cohorts and their utility for unsupervised disease staging. Chi-square analyses confirm statistically significant phenotype differences across cohorts, with memory impairment being the strongest discriminator. Few-shot prompting with the combined phenotype lists achieves the best clustering performance (ARI=0.290, NMI=0.232), substantially outperforming biomedical NER and dictionary-based baselines. Our results demonstrate that LLM-based phenotype extraction is a promising tool for discovering clinically meaningful ADRD signals from unstructured notes.

</details>

---

### 24. [TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics](https://arxiv.org/abs/2603.13676)

**基本信息**

- 🔗 arXiv: [`2603.13676`](https://arxiv.org/abs/2603.13676)
- 👥 作者: Zhihao Chen, Jiahui Wang, Yizhou Chen 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13676.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于医学决策支持的多智能体框架（TheraAgent），其核心组件包括多模态特征提取、自进化记忆和证据校准推理。虽然应用于医学影像，但其框架设计（特别是处理异构数据、进行案例推理和集成领域知识的方法）为构建复杂的、用于科学发现（如质谱数据解析与结构推理）的AI智能体系统提供了可借鉴的架构和工具。

**📖 中文摘要**

本文提出了TheraAgent，据我们所知，这是首个用于PET诊疗学的智能体框架。该框架包含三个核心创新：1）具有置信度加权共识的多专家特征提取，处理异构输入并进行不确定性量化；2）自进化智能体记忆，从累积病例中学习预后模式，实现基于案例的推理；3）证据校准推理，整合 curated 的诊疗学知识库，将预测基于VISION/TheraP试验证据。在35名真实患者和400个合成病例上评估，TheraAgent在真实患者上达到75.7%的整体准确率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

PET theranostics is transforming precision oncology, yet treatment response varies substantially; many patients receiving 177Lu-PSMA radioligand therapy (RLT) for metastatic castration-resistant prostate cancer (mCRPC) fail to respond, demanding reliable pre-therapy prediction. While LLM-based agents have shown remarkable potential in complex medical diagnosis, their application to PET theranostic outcome prediction remains unexplored, which faces three key challenges: (1) data and knowledge scarcity: RLT was only FDA-approved in 2022, yielding few training cases and insufficient domain knowledge in general LLMs; (2) heterogeneous information integration: robust prediction hinges on structured knowledge extraction from PET/CT, laboratory tests, and free-text clinical documentation; (3) evidence-grounded reasoning: clinical decisions must be anchored in trial evidence rather than LLM hallucinations. In this paper, we present TheraAgent, to our knowledge, the first agentic framework for PET theranostics, with three core innovations: (1) Multi-Expert Feature Extraction with Confidence-Weighted Consensus, where three specialized experts process heterogeneous inputs with uncertainty quantification; (2) Self-Evolving Agentic Memory (SEA-Mem), which learns prognostic patterns from accumulated cases, enabling case-based reasoning from limited data; (3) Evidence-Calibrated Reasoning, integrating a curated theranostics knowledge base to ground predictions in VISION/TheraP trial evidence. Evaluated on 35 real patients and 400 synthetic cases, TheraAgent achieves 75.7% overall accuracy on real patients and 87.0% on synthetic cases, outperforming MDAgents and MedAgent-Pro by over 20%. These results highlight a promising blueprint for trustworthy AI agents in PET theranostics, enabling trial-calibrated, multi-source decision support. Code will be released upon acceptance.

</details>

---

### 25. [Data-driven Progressive Discovery of Physical Laws](https://arxiv.org/abs/2603.13727)

**基本信息**

- 🔗 arXiv: [`2603.13727`](https://arxiv.org/abs/2603.13727)
- 👥 作者: Mingkun Xia, Weiwei Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13727.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕数据驱动的符号回归和物理定律发现，这是一种构建可解释模型的方法论，与构建和理解“化学大模型”（用于从化学数据中学习规律和预测）的核心主题直接相关。

**📖 中文摘要**

本文提出了一种名为符号回归链（CoSR）的新框架，用于从数据中渐进式地发现物理定律。该方法将物理定律的发现过程建模为一系列具有明确物理意义的符号知识单元的链式组合，遵循从简单到复杂的科学发现基本路径。CoSR框架能够从数据中精确地发现潜在的物理定律，并在经典力学（如从开普勒第三定律到万有引力定律的发现过程）和复杂工程问题（如不同飞行器的空气动力系数标度）上得到验证。这项工作与“化学大模型”主题相关，因为它提出了一种用于从复杂系统数据中发现可解释数学表达式的符号回归框架，这种数据驱动的知识发现范式是构建和理解化学领域大模型（如用于预测性质或反应）的核心组成部分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Symbolic regression is a powerful tool for knowledge discovery, enabling the extraction of interpretable mathematical expressions directly from data. However, conventional symbolic discovery typically follows an end-to-end, "one-step" process, which often generates lengthy and physically meaningless expressions when dealing with real physical systems, leading to poor model generalization. This limitation fundamentally stems from its deviation from the basic path of scientific discovery: physical laws do not exist in a single form but follow a hierarchical and progressive pattern from simplicity to complexity. Motivated by this principle, we propose Chain of Symbolic Regression (CoSR), a novel framework that models the discovery of physical laws as a chain of symbolic knowledge. This knowledge chain is formed by progressively combining multiple knowledge units with clear physical meanings along a specific logic, ultimately enabling the precise discovery of the underlying physical laws from data. CoSR fully recapitulates the progressive discovery path from Kepler's third law to the law of universal gravitation in classical mechanics, and is applied to three types of problems: turbulent Rayleigh-Benard convection, viscous flows in a circular pipe, and laser-metal interaction, demonstrating its ability to improve classical scaling theories. Finally, CoSR showcases its capability to discover new knowledge in the complex engineering problem of aerodynamic coefficients scaling for different aircraft.

</details>

---

### 26. [Ransomware and Artificial Intelligence: A Comprehensive Systematic Review of Reviews](https://arxiv.org/abs/2603.13734)

**基本信息**

- 🔗 arXiv: [`2603.13734`](https://arxiv.org/abs/2603.13734)
- 👥 作者: Therdpong Daengsi, Phisit Pornpongtechavanich, Paradorn Boonpoor 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13734.pdf)

**💡 相关性分析**

满足标准3：这是一篇专门针对人工智能（包括机器学习/深度学习模型）在网络安全领域应用的系统性综述。虽然其应用领域是勒索软件防御，而非直接的化学或质谱，但论文的核心是对“AI模型”（作为“大模型”的一个子集或相关领域）在该领域应用现状、挑战和未来方向的全面回顾与展望，符合“综述展望相关”的标准。

**📖 中文摘要**

本研究采用“综述的综述”方法，对过去五年（2020-2024年）人工智能（特别是机器学习和深度学习）在勒索软件防御中的应用进行了全面综合。它探讨了AI如何改变勒索软件的检测、预防和缓解策略，重点分析了结合静态和动态分析的混合模型的有效性，以及用于早期预警的异常检测机制。该研究还讨论了勒索软件防御中的关键挑战，包括旨在欺骗AI驱动检测系统的技术以及缺乏强大且多样化的数据集。这篇综述系统地整合了多篇综述文章的见解，确定了有效的AI模型，并将理论与实践联系起来，为学术界、工业界和政策制定者之间的合作提供支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study provides a comprehensive synthesis of Artificial Intelligence (AI), especially Machine Learning (ML) and Deep Learning (DL), in ransomware defense. Using a "review of reviews" methodology based on PRISMA, this paper gathers insights on how AI is transforming ransomware detection, prevention, and mitigation strategies during the past five years (2020-2024). The findings highlight the effectiveness of hybrid models that combine multiple analysis techniques such as code inspection (static analysis) and behavior monitoring during execution (dynamic analysis). The study also explores anomaly detection and early warning mechanisms before encryption to address the increasing complexity of ransomware. In addition, it examines key challenges in ransomware defense, including techniques designed to deceive AI-driven detection systems and the lack of strong and diverse datasets. The results highlight the role of AI in early detection and real-time response systems, improving scalability and resilience. Using a systematic review-of-reviews approach, this study consolidates insights from multiple review articles, identifies effective AI models, and bridges theory with practice to support collaboration among academia, industry, and policymakers. Future research directions and practical recommendations for cybersecurity practitioners are also discussed. Finally, this paper proposes a roadmap for advancing AI-driven countermeasures to protect critical systems and infrastructures against evolving ransomware threats.

</details>

---

### 27. [Knowledge Distillation for Large Language Models](https://arxiv.org/abs/2603.13765)

**基本信息**

- 🔗 arXiv: [`2603.13765`](https://arxiv.org/abs/2603.13765)
- 👥 作者: Alejandro Paredes La Torre, Barbara Flores, Diego Rodriguez
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13765.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型（LLM）的压缩与优化技术，特别是知识蒸馏和思维链强化学习。LLM是“化学大模型”在自然语言处理领域的对应物，其模型架构、训练和压缩技术（如知识蒸馏）对于构建和部署化学领域的专用大模型具有直接的参考价值和相关性。

**📖 中文摘要**

本文提出了一个通过知识蒸馏压缩大型语言模型（LLM）的资源高效框架，并结合了引导式思维链强化学习。该研究使用Qwen 3B作为教师模型，Qwen 0.5B作为学生模型，在多个数据集（包括英文和西班牙文Dolly-15k，以及代码数据集BugNet和PyTorrent）上应用知识蒸馏。对于代码任务，通过将思维链提示与使用CoT注释的Codeforces数据进行组相对策略优化相结合，提高了推理连贯性和解决方案的正确性。训练后的4位权重量化进一步减少了内存占用和推理延迟。结果表明，知识蒸馏与思维链引导的强化学习相结合，可以产生适用于资源受限环境部署的紧凑、高效模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose a resource-efficient framework for compressing large language models through knowledge distillation, combined with guided chain-of-thought reinforcement learning. Using Qwen 3B as the teacher and Qwen 0.5B as the student, we apply knowledge distillation across English Dolly-15k, Spanish Dolly-15k, and code BugNet and PyTorrent datasets, with hyperparameters tuned in the English setting to optimize student performance. Across tasks, the distilled student retains a substantial portion of the teacher's capability while remaining significantly smaller: 70% to 91% in English, up to 95% in Spanish, and up to 93.5% Rouge-L in code. For coding tasks, integrating chain-of-thought prompting with Group Relative Policy Optimization using CoT-annotated Codeforces data improves reasoning coherence and solution correctness compared to knowledge distillation alone. Post-training 4-bit weight quantization further reduces memory footprint and inference latency. These results show that knowledge distillation combined with chain-of-thought guided reinforcement learning can produce compact, efficient models suitable for deployment in resource-constrained settings.

</details>

---

### 28. [Retrieve, Schedule, Reflect: LLM Agents for Chip QoR Optimization](https://arxiv.org/abs/2603.13767)

**基本信息**

- 🔗 arXiv: [`2603.13767`](https://arxiv.org/abs/2603.13767)
- 👥 作者: Yikang ouyang, Yang Luo, Dongsheng Zuo 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13767.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个基于LLM的智能体框架，用于自动化复杂任务（芯片设计优化）。这直接涉及“大模型”（此处为LLM）在专业领域的应用、规划、决策和与工具交互的能力，与“化学大模型”主题中关于利用大模型解决复杂化学问题（如分子设计、合成规划）的研究范式高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern chip design requires multi-objective optimization of timing, power, and area under stringent time-to-market constraints. Although powerful optimization algorithms are integrated into EDA tools, achieving high QoR hinges on effective long-horizon scheduling, which relies heavily on manual expert intervention. To address this issue and automate chip design, we propose an agentic LLM framework that schedules chip optimizations through direct interaction with EDA tools. The agent is grounded in natural language expertise expressed as a search tree through retrieval-augmented generation (RAG). We further improve scheduling quality with Pareto-driven QoR feedback through language reflection. Experimental results show that, compared with black-box search methods such as reinforcement learning, our framework achieves 10% greater timing improvement while consuming less power and area, with more than 4x speedup. The post-optimization QoR is also comparable to that achieved by human experts. Finally, the agent supports customized tasks expressed in natural language, enabling preferential QoR trade-offs. The code and chip design data will be publicly available at this https URL .

</details>

---

### 29. [Retrieval-Feedback-Driven Distillation and Preference Alignment for Efficient LLM-based Query Expansion](https://arxiv.org/abs/2603.13776)

**基本信息**

- 🔗 arXiv: [`2603.13776`](https://arxiv.org/abs/2603.13776)
- 👥 作者: Minghan Li, Guodong Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13776.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型（LLM）的优化，特别是通过知识蒸馏和偏好对齐来压缩模型并提升其在特定任务（查询扩展）上的效率与效果。这直接关联“化学大模型”主题中关于如何高效训练、优化和部署用于化学任务的大模型的技术挑战。

**📖 中文摘要**

本文针对基于大型语言模型（LLM）的查询扩展方法推理成本高的问题，提出了一个检索反馈驱动的蒸馏和偏好对齐框架，旨在将检索友好的扩展行为从强大的教师模型转移到紧凑的学生模型。该框架利用教师在零样本和少样本提示条件下生成的两种互补扩展类型作为蒸馏的监督信号和偏好构建的候选池。随后引入了一种检索指标驱动的策略，根据nDCG@10差异自动形成选择/拒绝的扩展对，并应用直接偏好优化（DPO）使生成偏好与检索目标明确对齐。实验表明，该方法在保持强大检索有效性的同时，大幅降低了推理成本。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models have recently enabled a generative paradigm for query expansion, but their high inference cost makes direct deployment difficult in practical retrieval systems. To address this issue, a retrieval-feedback-driven distillation and preference-alignment framework is proposed to transfer retrieval-friendly expansion behavior from a strong teacher model to a compact student model. Rather than relying on few-shot exemplars at inference time, the framework first leverages two complementary types of teacher-generated expansions, produced under zero-shot and few-shot prompting conditions, as supervision signals for distillation and as candidate pools for preference construction. A retrieval-metric-driven strategy is then introduced to automatically form chosen/rejected expansion pairs according to nDCG@10 differences, and Direct Preference Optimization is applied to explicitly align generation preferences with retrieval objectives. Experiments on TREC DL19/20/21 and MIRACL-zh show that the proposed approach preserves strong retrieval effectiveness while substantially reducing inference cost. In particular, the distilled Qwen3-4B model reaches about 97% of the teacher (DeepSeek-685B) model's nDCG@10 performance on DL19, and remains effective on the Chinese MIRACL-zh benchmark, demonstrating strong practicality across both English and Chinese retrieval settings.

</details>

---

### 30. [Greedy Information Projection for LLM Data Selection](https://arxiv.org/abs/2603.13790)

**基本信息**

- 🔗 arXiv: [`2603.13790`](https://arxiv.org/abs/2603.13790)
- 👥 作者: Victor Ye Dong, Kuan-Yun Lee, Jiamei Shuai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13790.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为大型语言模型（LLM）微调设计数据选择框架。这直接关系到如何高效、有针对性地训练和优化大模型，是构建和优化“化学大模型”（需要高质量、相关的化学数据）过程中必须面对的关键技术问题。

**📖 中文摘要**

本文提出了贪婪信息投影（GIP），一个用于为大语言模型微调选择训练示例的原则性框架。GIP将选择问题转化为最大化示例子集与任务特定查询信号之间的互信息，这些信号可以来自LLM质量判断、元数据或其他来源。该框架涉及优化一个使用数据和查询嵌入定义的闭式互信息目标，自然地平衡了质量和多样性。优化此分数等价于最大化查询嵌入矩阵到所选数据张成空间上的投影，这为质量和多样性的共同出现提供了解释。基于此，作者采用了一种快速的贪婪匹配追踪程序。在指令跟随和数学推理数据集上的实验表明，GIP选择的小规模子集能够达到全数据微调的效果，同时仅使用一小部分示例和计算量，统一了质量感知和多样性感知的选择以实现高效微调。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present \emph{Greedy Information Projection} (\textsc{GIP}), a principled framework for choosing training examples for large language model fine-tuning. \textsc{GIP} casts selection as maximizing mutual information between a subset of examples and task-specific query signals, which may originate from LLM quality judgments, metadata, or other sources. The framework involves optimizing a closed-form mutual information objective defined using both data and query embeddings, naturally balancing {\it quality} and {\it diversity}. Optimizing this score is equivalent to maximizing the projection of the query embedding matrix onto the span of the selected data, which provides a geometric explanation for the co-emergence of quality and diversity. Building on this view, we employ a fast greedy matching-pursuit procedure with efficient projection-based updates. On instruction-following and mathematical reasoning datasets, \textsc{GIP} selects small subsets that match full-data fine-tuning while using only a fraction of examples and compute, unifying quality-aware and diversity-aware selection for efficient fine-tuning.

</details>

---

### 31. [DeceptGuard :A Constitutional Oversight Framework For Detecting Deception in LLM Agents](https://arxiv.org/abs/2603.13791)

**基本信息**

- 🔗 arXiv: [`2603.13791`](https://arxiv.org/abs/2603.13791)
- 👥 作者: Snehasis Mukhopadhyay
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13791.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大型语言模型（LLM）智能体的安全性与可靠性评估，特别是欺骗行为的检测。这直接关联到“大模型”的安全性、对齐和可信赖性研究，是任何领域大模型（包括化学大模型）在实际部署前必须考虑和评估的关键方面。

**📖 中文摘要**

本文介绍了DECEPTGUARD，一个用于检测大型语言模型（LLM）智能体中欺骗行为的统一框架。该框架系统比较了三种监控机制：黑盒监控（仅观察动作和输出）、思维链感知监控（额外观察智能体的思维链推理轨迹）和激活探针监控（额外读取冻结开源编码器的隐藏状态表示）。作者引入了DECEPTSYNTH，一个可扩展的合成流程，用于在新的12类欺骗分类法（涵盖言语、行为和结构欺骗）上生成欺骗阳性和欺骗阴性的智能体轨迹。监控器在4800条合成轨迹上优化，并在9200个来自DeceptArena基准的保留样本上评估。实验表明，思维链感知和激活探针监控器显著优于黑盒监控器。作者进一步提出了混合宪法集成作为一种深度防御方法，在测试集上达到了0.934的pAUROC。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reliable detection of deceptive behavior in Large Language Model (LLM) agents is an essential prerequisite for safe deployment in high-stakes agentic contexts. Prior work on scheming detection has focused exclusively on black-box monitors that observe only externally visible tool calls and outputs, discarding potentially rich internal reasoning signals. We introduce DECEPTGUARD, a unified framework that systematically compares three monitoring regimes: black-box monitors (actions and outputs only), CoT-aware monitors (additionally observing the agent's chain-of-thought reasoning trace), and activation-probe monitors (additionally reading hidden-state representations from a frozen open-weights encoder). We introduce DECEPTSYNTH, a scalable synthetic pipeline for generating deception-positive and deception-negative agent trajectories across a novel 12-category taxonomy spanning verbal, behavioral, and structural deception. Our monitors are optimized on 4,800 synthetic trajectories and evaluated on 9,200 held-out samples from DeceptArena, a benchmark of realistic sandboxed agent environments with execution-verified labels. Across all evaluation settings, CoT-aware and activation-probe monitors substantially outperform their black-box counterparts (mean pAUROC improvement of +0.097), with the largest gains on subtle, long-horizon deception that leaves minimal behavioral footprints. We empirically characterize a transparency-detectability trade-off: as agents learn to suppress overt behavioral signals, chain-of-thought becomes the primary detection surface but is itself increasingly unreliable due to post-training faithfulness degradation. We propose HYBRID-CONSTITUTIONAL ensembles as a robust defense-in-depth approach, achieving a pAUROC of 0.934 on the held-out test set, representing a substantial advance over the prior state of the art.

</details>

---

### 32. [IGU-LoRA: Adaptive Rank Allocation via Integrated Gradients and Uncertainty-Aware Scoring](https://arxiv.org/abs/2603.13792)

**基本信息**

- 🔗 arXiv: [`2603.13792`](https://arxiv.org/abs/2603.13792)
- 👥 作者: Xuan Cui, Huiyue Li, Run Zeng 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13792.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型（LLM）的参数高效微调（PEFT）技术，特别是低秩适配（LoRA）的改进。这是训练和适配“化学大模型”以用于特定下游任务（如分子性质预测、反应预测）时至关重要的技术，直接关系到模型训练的效率和效果。

**📖 中文摘要**

本文提出了IGU-LoRA，一种基于积分梯度和不确定性感知评分的自适应秩分配低秩适配（LoRA）方法。针对现有自适应LoRA变体（如AdaLoRA）依赖瞬时梯度导致评分不稳定和有偏差的问题，IGU-LoRA（i）计算层内积分梯度（IG）敏感性并将其聚合为层级评分以进行秩分配，（ii）应用采用偏差跟踪的指数移动平均的不确定性感知方案来抑制噪声更新并校准秩选择。理论上，作者证明了在路径wise Hessian-Lipschitz条件下参数空间IG的复合梯形规则近似误差的上界。在多样任务和架构上的实验表明，IGU-LoRA在匹配的参数预算下 consistently 优于强大的PEFT基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As large language models (LLMs) scale to billions of parameters, full-parameter fine-tuning becomes compute- and memory-prohibitive. Parameter-efficient fine-tuning (PEFT) mitigates this issue by updating only a small set of task-specific parameters while keeping the base model frozen. Among PEFT approaches, low-rank adaptation (LoRA) is widely adopted; however, it enforces a uniform rank across layers despite substantial variation in layer importance, motivating {layerwise} rank allocation. Recent adaptive-rank variants (e.g., AdaLoRA) allocate ranks based on importance scores, yet typically rely on instantaneous gradients that capture only local sensitivity, overlooking non-local, pathwise effects within the same layer, which yields unstable and biased scores. To address this limitation, we introduce IGU-LoRA, an adaptive-rank LoRA that (i) computes within-layer Integrated Gradients (IG) sensitivities and aggregates them into a layer-level score for rank allocation, and (ii) applies an uncertainty-aware scheme using exponential moving averages with deviation tracking to suppress noisy updates and calibrate rank selection. Theoretically, we prove an upper bound on the composite trapezoidal rule approximation error for parameter-space IG under a pathwise Hessian-Lipschitz condition, which informs the quadrature budget. Across diverse tasks and architectures, IGU-LoRA consistently outperforms strong PEFT baselines at matched parameter budgets, improving downstream accuracy and robustness. Ablations confirm the contributions of pathwise within-layer sensitivity estimates and uncertainty-aware selection to effective rank allocation. Our code is publicly available at this https URL

</details>

---

### 33. [GhanaNLP Parallel Corpora: Comprehensive Multilingual Resources for Low-Resource Ghanaian Languages](https://arxiv.org/abs/2603.13793)

**基本信息**

- 🔗 arXiv: [`2603.13793`](https://arxiv.org/abs/2603.13793)
- 👥 作者: Lawrence Adu Gyamfi, Paul Azunre, Stephen Edward Moore 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13793.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是创建和发布了一个大规模、高质量的多语言平行语料库。虽然语言是加纳本土语言而非化学领域，但论文明确提供了可用于自然语言处理任务（如机器翻译）的数据集和资源。这符合“数据资源相关”的标准，即论文提供了可用于构建或评估模型（包括可能用于处理化学文本的大模型）的数据集。

**📖 中文摘要**

本文介绍了GhanaNLP计划为加纳的低资源语言（Twi、Fante、Ewe、Ga和Kusaal）开发和整理的41,513个平行句对数据集。每个数据集由本地语言和英语之间仔细对齐的句对组成。数据由人类专业人员收集、翻译和注释，并丰富了标准结构元数据以确保一致性和可用性。这些语料库旨在支持研究、教育和商业应用，包括机器翻译、语音技术和语言保护。这项工作有助于实现人工智能民主化的更广泛努力，为非洲语言实现包容和可访问的语言技术。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Low resource languages present unique challenges for natural language processing due to the limited availability of digitized and well structured linguistic data. To address this gap, the GhanaNLP initiative has developed and curated 41,513 parallel sentence pairs for the Twi, Fante, Ewe, Ga, and Kusaal languages, which are widely spoken across Ghana yet remain underrepresented in digital spaces. Each dataset consists of carefully aligned sentence pairs between a local language and English. The data were collected, translated, and annotated by human professionals and enriched with standard structural metadata to ensure consistency and usability. These corpora are designed to support research, educational, and commercial applications, including machine translation, speech technologies, and language preservation. This paper documents the dataset creation methodology, structure, intended use cases, and evaluation, as well as their deployment in real world applications such as the Khaya AI translation engine. Overall, this work contributes to broader efforts to democratize AI by enabling inclusive and accessible language technologies for African languages.

</details>

---

### 34. [Decision Aggregation under Quantal Response](https://arxiv.org/abs/2603.13807)

**基本信息**

- 🔗 arXiv: [`2603.13807`](https://arxiv.org/abs/2603.13807)
- 👥 作者: Zhihuan Huang, Yichong Xia, Yuqing Kong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13807.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及大型语言模型（LLM）的行为建模（量化响应）以及基于LLM的集体决策聚合。这直接关联到对“大模型”本身行为特性的理解、评估以及如何利用多个模型实例进行决策，是“化学大模型”主题中关于模型可靠性、集成和决策支持的相关研究方向。

**📖 中文摘要**

本文研究了在有限理性个体存在下的集体决策聚合问题。作者假设每个专家收到一个关于未知状态的私有信号，并使用量化响应（一种捕捉有限理性的随机选择模型）来建模专家行为。在一个最小化最大遗憾的框架下，作者证明当个体理性低于某个阈值时，多数投票是最优的鲁棒聚合器。有趣的是，这样的群体可以胜过完全理性的智能体，因为他们的决策随机性编码了在确定性行为中丢失的微弱但信息丰富的信号。作者使用大型语言模型（LLM）验证了这些发现，LLM通过其温度参数自然地表现出量化响应。聚合适度随机的LLM输出显著提高了复杂推理任务的准确性，这凸显了有限理性在集体智能中可能是一种优势而非限制。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The effectiveness of collective decision-making is often challenged by the bounded rationality and inherent stochasticity of individual agents. We investigate this by analyzing how to aggregate decisions from n experts, each receiving a private signal about an unknown state. Assuming signals are conditionally independent and identically distributed, we depart from the fully rational paradigm and model expert behavior using quantal response, a stochastic choice model capturing bounded rationality. Within a minimax regret framework, we show that majority voting is the optimal robust aggregator when individual rationality falls below a certain threshold. Interestingly, such groups can outperform perfectly rational agents, as their decision randomness encodes weak but informative signals lost in deterministic behavior. We validate these findings using large language models (LLMs), which naturally exhibit quantal response via their temperature parameter. Aggregating moderately stochastic LLM outputs significantly improves accuracy on complex reasoning tasks, highlighting bounded rationality not as a limitation, but as a potential strength in collective intelligence.

</details>

---

### 35. [Intelligent Materials Modelling: Large Language Models Versus Partial Least Squares Regression for Predicting Polysulfone Membrane Mechanical Performance](https://arxiv.org/abs/2603.13834)

**基本信息**

- 🔗 arXiv: [`2603.13834`](https://arxiv.org/abs/2603.13834)
- 👥 作者: Dingding Cao, Mieow Kee Chan, Wan Sieng Yeo 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13834.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是直接使用大型语言模型（LLMs）作为预测模型，用于材料性能（聚砜膜的机械性能）预测。这是一个将“大模型”应用于化学/材料科学领域具体预测任务的实例，与“化学大模型”主题高度相关，展示了LLMs在解决化学信息学问题中的潜力和方法论。

**📖 中文摘要**

本研究针对从结构描述符预测聚砜（PSF）膜机械性能的挑战，基准测试了使用四种大语言模型（LLMs）的知识驱动推理与偏最小二乘（PLS）回归方法。研究的性能指标包括杨氏模量、拉伸强度和断裂伸长率，输入特征为孔径、接触角、厚度和孔隙率。结果表明，对于非线性、约束敏感的属性（如断裂伸长率），LLMs取得了统计上显著的改进，DeepSeek-R1和GPT-5分别实现了40.5%和40.3%的均方根误差降低。对于具有强结构-属性相关性的属性（如杨氏模量和拉伸强度），两种方法表现相当。误差拓扑分析揭示了由数据机制效应主导的系统性回归到平均的行为。这些发现表明，LLMs在bootstrap不稳定性下的非线性、约束敏感属性方面表现出色，而PLS对于需要可解释潜在变量分解的线性关系仍然具有竞争力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting the mechanical properties of polysulfone (PSF) membranes from structural descriptors remains challenging due to extreme data scarcity typical of experimental studies. To investigate this issue, this study benchmarked knowledge-driven inference using four large language models (LLMs) (DeepSeek-V3, DeepSeek-R1, ChatGPT-4o, and GPT-5) against partial least squares (PLS) regression for predicting Young's modulus (E), tensile strength (TS), and elongation at break (EL) based on pore diameter (PD), contact angle (CA), thickness (T), and porosity (P) measurements. These knowledge-driven approaches demonstrated property-specific advantages over the chemometric baseline. For EL, LLMs achieved statistically significant improvements, with DeepSeek-R1 and GPT-5 delivering 40.5% and 40.3% of Root Mean Square Error reductions, respectively, reducing mean absolute errors from $11.63\pm5.34$% to $5.18\pm0.17$%. Run-to-run variability was markedly compressed for LLMs ($\leq$3%) compared to PLS (up to 47%). E and TS predictions showed statistical parity between approaches ($q\geq0.05$), indicating sufficient performance of linear methods for properties with strong structure-property correlations. Error topology analysis revealed systematic regression-to-the-mean behavior dominated by data-regime effects rather than model-family limitations. These findings establish that LLMs excel for non-linear, constraint-sensitive properties under bootstrap instability, while PLS remains competitive for linear relationships requiring interpretable latent-variable decompositions. The demonstrated complementarity suggests hybrid architectures leveraging LLM-encoded knowledge within interpretable frameworks may optimise small-data materials discovery.

</details>

---

### 36. [GRPO and Reflection Reward for Mathematical Reasoning in Large Language Models](https://arxiv.org/abs/2603.14041)

**基本信息**

- 🔗 arXiv: [`2603.14041`](https://arxiv.org/abs/2603.14041)
- 👥 作者: Zhijie Wang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14041.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕如何通过GRPO和反思奖励机制来增强大语言模型的推理能力，这直接关联到构建具有高级推理能力的“化学大模型”这一主题。

**📖 中文摘要**

本文提出了一种将组相对策略优化（GRPO）与反思奖励机制相结合的四阶段框架，旨在增强大型语言模型（LLMs）在数学推理任务中的自我反思能力。该研究专注于通过强化学习范式优化LLMs的推理过程，其中反思奖励被设计为鼓励模型在生成答案时进行主动的自我检查和修正。实验结果表明，GRPO方法通过反思鼓励训练达到了最先进的性能，并且消融研究证实了反思奖励的关键作用。这项工作直接涉及如何通过特定的训练机制（反思奖励）来构建和优化“化学大模型”所依赖的核心能力之一——复杂推理，为开发能够进行质谱数据深度分析和结构推理的化学AI模型提供了方法论参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The enhancement of reasoning capabilities in large language models (LLMs) has garnered significant attention, with supervised fine-tuning (SFT) and reinforcement learning emerging as dominant paradigms. While recent studies recognize the importance of reflection in reasoning processes, existing methodologies seldom address proactive reflection encouragement during training. This study focuses on mathematical reasoning by proposing a four-stage framework integrating Group Relative Policy Optimization (GRPO) with reflection reward mechanisms to strengthen LLMs' self-reflective capabilities. Besides, this approach incorporates established accuracy and format reward. Experimental results demonstrate GRPO's state-of-the-art performance through reflection-encouraged training, with ablation studies confirming the reflection reward's pivotal role. Comparative evaluations demonstrate full-parameter SFT's superiority over low-rank adaptation (LoRA) despite heightened computational demands. Building on these cumulative findings, this research substantiates GRPO's methodological significance in post-training optimization and envisions its potential to serve as a pivotal enabler for future LLM-based intelligent agents through the synergistic integration of cognitive rewards with dynamic environmental interactions.

</details>

---

### 37. [The Reasoning Bottleneck in Graph-RAG: Structured Prompting and Context Compression for Multi-Hop QA](https://arxiv.org/abs/2603.14045)

**基本信息**

- 🔗 arXiv: [`2603.14045`](https://arxiv.org/abs/2603.14045)
- 👥 作者: Yasaman Zarinkia, Venkatesh Srinivasan, Alex Thomo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14045.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何解决大模型在基于知识图谱的复杂推理任务中的瓶颈问题。其提出的结构化推理和上下文压缩方法，为构建能够处理质谱-结构关联图谱并进行复杂结构推理的“化学大模型”提供了重要的技术思路和借鉴。

**📖 中文摘要**

本文研究了图检索增强生成（Graph-RAG）系统在多跳问答任务中存在的“推理瓶颈”问题。作者发现，即使检索到了包含正确答案的上下文，系统的最终答案准确率仍然不高，主要错误源于推理失败。为此，论文提出了两种增强方法：SPARQL链式思维提示和基于图遍历的上下文压缩。这些方法旨在通过结构化提示和高效的信息压缩，来提升模型对复杂知识图谱上下文的推理能力。这项工作虽然不直接针对化学领域，但其核心——如何让大模型更有效地对结构化知识（如图谱）进行推理——与“化学大模型”和“质谱结构推理”高度相关。质谱解析本质上是从谱图数据中推理出分子结构，可以视为一种特殊的、基于图谱（质谱峰与子结构关系）的推理任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph-RAG systems achieve strong multi-hop question answering by indexing documents into knowledge graphs, but strong retrieval does not guarantee strong answers. Evaluating KET-RAG, a leading Graph-RAG system, on three multi-hop QA benchmarks (HotpotQA, MuSiQue, 2WikiMultiHopQA), we find that 77% to 91% of questions have the gold answer in the retrieved context, yet accuracy is only 35% to 78%, and 73% to 84% of errors are reasoning failures. We propose two augmentations: (i) SPARQL chain-of-thought prompting, which decomposes questions into triple-pattern queries aligned with the entity-relationship context, and (ii) graph-walk compression, which compresses the context by ~60% via knowledge-graph traversal with no LLM calls. SPARQL CoT improves accuracy by +2 to +14 pp; graph-walk compression adds +6 pp on average when paired with structured prompting on smaller models. Surprisingly, we show that, with question-type routing, a fully augmented budget open-weight Llama-8B model matches or exceeds the unaugmented Llama-70B baseline on all three benchmarks at ~12x lower cost. A replication on LightRAG confirms that our augmentations transfer across Graph-RAG systems.

</details>

---

### 38. [Understanding the Emergence of Seemingly Useless Features in Next-Token Predictors](https://arxiv.org/abs/2603.14087)

**基本信息**

- 🔗 arXiv: [`2603.14087`](https://arxiv.org/abs/2603.14087)
- 👥 作者: Mark Rofin, Jalal Naghiyev, Michael Hahn
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14087.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是理解大模型（Transformer）内部“隐藏特征”的涌现机制，特别是那些与复杂推理相关的特征。这对于理解和设计能够进行质谱结构推理等复杂科学推理任务的“化学大模型”具有根本性的启示。

**📖 中文摘要**

本文研究了在训练好的Transformer模型中，那些看似对预测下一个令牌“无用”的特征是如何出现的。作者识别了来自下一令牌预测目标的梯度信号中哪些成分导致了这种现象，并提出了一种方法来估计这些成分对特定特征出现的影响。在验证了该方法在玩具任务上的有效性后，作者将其应用于解释OthelloGPT中的世界模型特征和一个小型语言模型中的句法特征。最后，该框架被应用于一个预训练的LLM，表明对未来令牌影响极高或极低的特征往往与代码等形式推理领域相关。这项研究为理解Transformer模型的内部工作机制提供了重要视角，特别是那些可能服务于复杂、长程推理（如化学结构推理）的隐藏特征是如何在训练中形成的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Trained Transformers have been shown to compute abstract features that appear redundant for predicting the immediate next token. We identify which components of the gradient signal from the next-token prediction objective give rise to this phenomenon, and we propose a method to estimate the influence of those components on the emergence of specific features. After validating our approach on toy tasks, we use it to interpret the origins of the world model in OthelloGPT and syntactic features in a small language model. Finally, we apply our framework to a pretrained LLM, showing that features with extremely high or low influence on future tokens tend to be related to formal reasoning domains such as code. Overall, our work takes a step toward understanding hidden features of Transformers through the lens of their development during training.

</details>

---

### 39. [The Institutional Scaling Law: Non-Monotonic Fitness, Capability-Trust Divergence, and Symbiogenetic Scaling in Generative AI](https://arxiv.org/abs/2603.14126)

**基本信息**

- 🔗 arXiv: [`2603.14126`](https://arxiv.org/abs/2603.14126)
- 👥 作者: Mark Baciak, Thomas A. Cellucci
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14126.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容直接围绕大模型的缩放定律与发展范式，提出了不同于单纯追求模型规模的新路径（领域特定模型系统）。这为“化学大模型”和“质谱结构推理”模型的未来发展提供了重要的综述和展望性讨论，指出了可能更高效、更可持续的技术方向。

**📖 中文摘要**

本文挑战了经典的AI性能随模型规模单调提升的缩放定律，提出了“制度缩放定律”。该定律表明，衡量能力、信任度、可负担性和自主性的“制度适应性”在模型规模上是非单调的，存在一个依赖于环境的最优规模。论文进一步证明了超越临界规模后，模型的能力和信任度会正式背离。此外，作者还提出了“共生缩放”修正，表明由领域特定模型组成的协调系统可以在其原生部署环境中超越前沿的通用模型。该研究将分析置于生成式AI的形式化进化分类中，并预测下一个阶段转变将由更好协调的、适应特定制度生态位的领域特定模型系统驱动，而非更大的模型。这为“化学大模型”的发展路径提供了重要的战略视角，即可能不需要追求单一的巨型通用模型，而是发展面向化学信息学、质谱分析等特定领域的、高效协同的模型系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Classical scaling laws model AI performance as monotonically improving with model size. We challenge this assumption by deriving the Institutional Scaling Law, showing that institutional fitness -- jointly measuring capability, trust, affordability, and sovereignty -- is non-monotonic in model scale, with an environment-dependent optimum N*(epsilon). Our framework extends the Sustainability Index of Han et al. (2025) from hardware-level to ecosystem-level analysis, proving that capability and trust formally diverge beyond critical scale (Capability-Trust Divergence). We further derive a Symbiogenetic Scaling correction demonstrating that orchestrated systems of domain-specific models can outperform frontier generalists in their native deployment environments. These results are contextualized within a formal evolutionary taxonomy of generative AI spanning five eras (1943-present), with analysis of frontier lab dynamics, sovereign AI emergence, and post-training alignment evolution from RLHF through GRPO. The Institutional Scaling Law predicts that the next phase transition will be driven not by larger models but by better-orchestrated systems of domain-specific models adapted to specific institutional niches.

</details>

---

### 40. [An Alternative Trajectory for Generative AI](https://arxiv.org/abs/2603.14147)

**基本信息**

- 🔗 arXiv: [`2603.14147`](https://arxiv.org/abs/2603.14147)
- 👥 作者: Margarita Belova, Yuval Kansal, Yihao Liang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14147.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容直接针对大模型的发展范式，并提出了一种专注于领域专业知识与符号系统结合的替代路径。这为“化学大模型”和“质谱结构推理”模型的构建提供了重要的综述、批判和前瞻性框架，具有极强的指导意义。

**📖 中文摘要**

本文批判性地分析了当前生成式AI生态系统追求通过扩展单体模型来实现通用人工智能（AGI）的轨迹所面临的可持续性挑战，包括能源负担、数据缩放收益递减等问题。作者提出了一条基于“领域特定超智能”（DSS）的替代发展轨迹。该路径主张首先构建显式的符号抽象（如知识图谱、本体论和形式逻辑），以此为支撑合成课程，使得小型语言模型能够在没有典型LLM合成数据方法导致的模型坍塌问题的情况下，掌握领域特定的推理能力。最终愿景是形成一个“DSS模型社会”：动态的生态系统，其中协调智能体将任务路由到不同的DSS后端。这一范式转变将能力与模型规模解耦，使得智能能够从耗能的数据中心迁移到安全的、设备端的专家系统。这项工作为“化学大模型”和“质谱结构推理”模型的构建提供了颠覆性的蓝图，即不依赖于单一的、庞大的通用模型，而是构建基于化学领域知识（如反应规则、光谱-结构关联图谱）的、可协同工作的、高效的专业化模型系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The generative artificial intelligence (AI) ecosystem is undergoing rapid transformations that threaten its sustainability. As models transition from research prototypes to high-traffic products, the energetic burden has shifted from one-time training to recurring, unbounded inference. This is exacerbated by reasoning models that inflate compute costs by orders of magnitude per query. The prevailing pursuit of artificial general intelligence through scaling of monolithic models is colliding with hard physical constraints: grid failures, water consumption, and diminishing returns on data scaling. This trajectory yields models with impressive factual recall but struggles in domains requiring in-depth reasoning, possibly due to insufficient abstractions in training data. Current large language models (LLMs) exhibit genuine reasoning depth only in domains like mathematics and coding, where rigorous, pre-existing abstractions provide structural grounding. In other fields, the current approach fails to generalize well. We propose an alternative trajectory based on domain-specific superintelligence (DSS). We argue for first constructing explicit symbolic abstractions (knowledge graphs, ontologies, and formal logic) to underpin synthetic curricula enabling small language models to master domain-specific reasoning without the model collapse problem typical of LLM-based synthetic data methods. Rather than a single generalist giant model, we envision "societies of DSS models": dynamic ecosystems where orchestration agents route tasks to distinct DSS back-ends. This paradigm shift decouples capability from size, enabling intelligence to migrate from energy-intensive data centers to secure, on-device experts. By aligning algorithmic progress with physical constraints, DSS societies move generative AI from an environmental liability to a sustainable force for economic empowerment.

</details>

---

### 41. [Deep probabilistic model synthesis enables unified modeling of whole-brain neural activity across individual subjects](https://arxiv.org/abs/2603.14161)

**基本信息**

- 🔗 arXiv: [`2603.14161`](https://arxiv.org/abs/2603.14161)
- 👥 作者: William E. Bishop, Luuk W. Hesselink, Bernhard Englitz 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14161.pdf)

**💡 相关性分析**

满足标准1：论文提出的深度概率模型合成（DPMS）框架，其核心研究内容是如何整合多个相关系统实例的数据以构建统一且适应性的模型。这种方法论可直接应用于整合来自不同来源、不同条件的化学或质谱数据，用于训练更强大的“化学大模型”或“质谱结构推理”模型，解决了该领域数据异构和稀缺的关键挑战。

**📖 中文摘要**

本文介绍了深度概率模型合成（DPMS）框架，该框架利用系统辅助属性将多个系统实例的数据结合起来进行建模。DPMS使用变分推断来学习模型参数的条件先验分布和实例特定的后验分布，从而分别将系统实例联系起来并捕捉其独特结构。DPMS可以合成多种模型类别，如回归、分类和降维模型。作者在合成数据和斑马鱼全脑神经活动数据上展示了其超越单实例模型的能力。这项研究的方法论对于“化学大模型”和“质谱结构推理”具有重要意义。在化学信息学中，我们经常需要整合来自不同实验条件、不同仪器或不同化合物类别的数据来构建一个通用的预测或推理模型。DPMS提供了一种原则性的机器学习框架，能够从多个相关但不同的数据源（例如，来自不同实验室的质谱数据集）中学习一个统一的模型，同时保留每个数据源的特性，这对于构建稳健、可泛化的化学AI模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many disciplines need quantitative models that synthesize experimental data across multiple instances of the same general system. For example, neuroscientists must combine data from the brains of many individual animals to understand the species' brain in general. However, typical machine learning models treat one system instance at a time. Here we introduce a machine learning framework, deep probabilistic model synthesis (DPMS), that leverages system properties auxiliary to the model to combine data across system instances. DPMS specifically uses variational inference to learn a conditional prior distribution and instance-specific posterior distributions over model parameters that respectively tie together the system instances and capture their unique structure. DPMS can synthesize a wide variety of model classes, such as those for regression, classification, and dimensionality reduction, and we demonstrate its ability to improve upon single-instance models on synthetic data and whole-brain neural activity data from larval zebrafish.

</details>

---

### 42. [TACTIC for Navigating the Unknown: Tabular Anomaly deteCTion via In-Context inference](https://arxiv.org/abs/2603.14171)

**基本信息**

- 🔗 arXiv: [`2603.14171`](https://arxiv.org/abs/2603.14171)
- 👥 作者: Patryk Marszałek, Tomasz Kuśmierczyk, Marek Śmieja
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14171.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于表格数据异常检测的上下文学习模型。这种能够快速适应新数据上下文并进行推理的模型架构，非常适用于化学和质谱分析中常见的小样本、新场景下的异常检测或新奇化合物识别任务，是构建智能化学数据分析工具的相关技术。

**📖 中文摘要**

本文研究了上下文学习模型在表格数据异常检测任务中的应用。作者指出，尽管TabPFN等上下文模型在监督问题上表现良好，但其基于分类学习的先验可能无法直接扩展到异常检测。现有的无监督扩展版本存在不稳定行为和高计算成本的问题。为此，作者提出了TACTIC，一种基于异常中心合成先验进行预训练的上下文异常检测方法。TACTIC能够进行快速、数据依赖的异常推理，同时避免针对特定数据集的调优。与典型的基于分数的方法不同，TACTIC被训练为一个判别式预测器，能够在单次前向传播中做出明确的异常决策。这项工作为开发用于化学和质谱数据的异常检测模型提供了新思路。在质谱分析中，识别异常谱图（如含有未知杂质或仪器故障）至关重要。TACTIC所代表的上下文学习范式，使得模型能够基于提供的参考样本（上下文）快速适应新的数据集或检测任务，这对于处理不断涌现的新化合物或新型质谱仪数据具有潜在优势，为构建自适应、低维护的化学数据分析工具提供了技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anomaly detection for tabular data has been a long-standing unsupervised learning problem that remains a major challenge for current deep learning models. Recently, in-context learning has emerged as a new paradigm that has shifted efforts from task-specific optimization to large-scale pretraining aimed at creating foundation models that generalize across diverse datasets. Although in-context models, such as TabPFN, perform well in supervised problems, their learned classification-based priors may not readily extend to anomaly detection. In this paper, we study in-context models for anomaly detection and show that the unsupervised extensions to TabPFN exhibit unstable behavior, particularly in noisy or contaminated contexts, in addition to the high computational cost. We address these challenges and introduce TACTIC, an in-context anomaly detection approach based on pretraining with anomaly-centric synthetic priors, which provides fast and data-dependent reasoning about anomalies while avoiding dataset-specific tuning. In contrast to typical score-based approaches, which produce uncalibrated anomaly scores that require post-processing (e.g. threshold selection or ranking heuristics), the proposed model is trained as a discriminative predictor, enabling unambiguous anomaly decisions in a single forward pass. Through experiments on real-world datasets, we examine the performance of TACTIC in clean and noisy contexts with varying anomaly rates and different anomaly types, as well as the impact of prior choices on detection quality. Our experiments clearly show that specialized anomaly-centric in-context models such as TACTIC are highly competitive compared to other task-specific methods.

</details>

---

### 43. [Hybrid Intent-Aware Personalization with Machine Learning and RAG-Enabled Large Language Models for Financial Services Marketing](https://arxiv.org/abs/2603.14173)

**基本信息**

- 🔗 arXiv: [`2603.14173`](https://arxiv.org/abs/2603.14173)
- 👥 作者: Akhil Chandra Shanivendra
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14173.pdf)

**💡 相关性分析**

满足标准1：论文提出的混合架构（机器学习预测 + RAG-LLM生成）其核心研究内容是如何构建透明、可解释的智能决策与内容生成系统。这种架构设计思路可以直接迁移到化学信息学领域，用于构建能够进行性质预测、实验设计、结果解释和报告生成的综合性“化学大模型”或智能助手。

**📖 中文摘要**

本文提出了一种用于金融服务营销的混合架构，该架构集成了用于客户细分、潜在意图建模和个性化预测的经典机器学习，以及用于生成合规、上下文相关内容的检索增强生成（RAG）大语言模型。该框架包含时间编码器、潜在表示和多任务分类，以估计细分成员、客户意图和产品-渠道推荐。一个RAG生成层然后根据检索到的领域文档生成面向客户的消息。实验表明，时间建模和意图特征提高了个性化准确性，而基于引用的检索减少了无支持的生成，并支持受监管环境下的可审计性。这项研究展示了预测建模和RAG生成如何结合成一个透明、可解释的流程。这种方法论与构建“化学大模型”高度相关。例如，可以类似地构建一个混合系统：用机器学习模型预测化合物的性质或反应结果，同时用RAG增强的LLM根据检索到的化学文献、安全数据表或反应规则，生成实验方案、解释或报告。这为开发面向化学研究全流程的智能辅助系统提供了可行的技术框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Personalized marketing in financial services requires models that can both predict customer behavior and generate compliant, context-appropriate content. This paper presents a hybrid architecture that integrates classical machine learning for segmentation, latent intent modeling, and personalization prediction with retrieval-augmented large language models for grounded content generation. A synthetic, reproducible dataset is constructed to reflect temporal customer behavior, product interactions, and marketing responses. The proposed framework incorporates temporal encoders, latent representations, and multi-task classification to estimate segment membership, customer intent, and product-channel recommendations. A retrieval-augmented generation layer then produces customer-facing messages constrained by retrieved domain documents. Experiments show that temporal modeling and intent features improve personalization accuracy, while citation-based retrieval reduces unsupported generation and supports auditability in regulated settings. The contribution is primarily architectural, demonstrating how predictive modeling and RAG-based generation can be combined into a transparent, explainable pipeline for financial services personalization.

</details>

---

### 44. [Vavanagi: a Community-run Platform for Documentation of the Hula Language in Papua New Guinea](https://arxiv.org/abs/2603.14210)

**基本信息**

- 🔗 arXiv: [`2603.14210`](https://arxiv.org/abs/2603.14210)
- 👥 作者: Bri Olewale, Raphael Merx, Ekaterina Vylomova
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14210.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是构建了一个由领域专家社区主导的数据创建与治理平台。这种模式为创建高质量、社区驱动的化学与质谱数据集（例如，众包标注质谱图与分子结构的对应关系、反应条件与产率等）提供了宝贵的范例和可行性证明，是构建“化学大模型”所需数据资源的重要相关工具和方法。

**📖 中文摘要**

本文介绍了Vavanagi，一个由社区运营的用于记录巴布亚新几内亚Hula（Vula'a）语言的平台。该平台支持众包的英-Hula文本翻译和语音录制，并包含长者主导的审核和社区治理的数据基础设施。截至目前，已产生了超过1.2万对平行句子，覆盖9000个独特的Hula单词。作者提出了一个衡量社区参与度的多层次框架，并将Vavanagi定位为最高级别（第5级）：倡议、设计、实施和数据治理完全由Hula社区主导。这项工作展示了语言技术如何能够连接乡村和城市成员、连接代际，并以社区自己的方式支持文化遗产。虽然主题是语言学，但其核心——构建由领域专家（本族语者）主导、用于创建高质量领域特定数据（语言数据）的平台——与“化学大模型”和“质谱结构推理”高度相关。要训练优秀的化学AI模型，需要大量高质量、标注准确的化学数据（如反应、性质、谱图-结构对）。Vavanagi的模式启示我们可以构建类似的、由化学家社区主导的数据众包与审核平台，用于构建开放、高质量的化学数据集，这直接服务于“数据资源相关”的标准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Vavanagi, a community-run platform for Hula (Vula'a), an Austronesian language of Papua New Guinea with approximately 10,000 speakers. Vavanagi supports crowdsourced English-Hula text translation and voice recording, with elder-led review and community-governed data infrastructure. To date, 77 translators and 4 reviewers have produced over 12k parallel sentence pairs covering 9k unique Hula words. We also propose a multi-level framework for measuring community involvement, from consultation to fully community-initiated and governed projects. We position Vavanagi at Level 5: initiative, design, implementation, and data governance all sit within the Hula community, making it, to our knowledge, the first community-led language technology initiative for a language of this size. Vavanagi shows how language technology can bridge village-based and urban members, connect generations, and support cultural heritage on the community's own terms.

</details>

---

### 45. [Sampling Boltzmann distributions via normalizing flow approximation of transport maps](https://arxiv.org/abs/2603.14258)

**基本信息**

- 🔗 arXiv: [`2603.14258`](https://arxiv.org/abs/2603.14258)
- 👥 作者: Zia Ur Rehman, Gero Friesecke
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14258.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用归一化流（一种生成模型）来近似分子动力学中的玻尔兹曼分布，以实现高效采样。这直接属于“化学大模型”范畴，即利用先进的机器学习模型（如生成模型）解决化学（分子动力学）中的核心计算问题。

**📖 中文摘要**

这篇论文提出了一种使用归一化流（normalizing flow）近似传输映射来高效采样分子动力学中出现的高维玻尔兹曼分布的方法。作者从数学上证明了在参考测度和真实玻尔兹曼分布之间存在一个归一化流，其Wasserstein距离误差可以任意小。该证明基于低正则性端点密度的Moser传输映射的严格构造以及Sobolev空间中神经网络的逼近定理。数值模拟证实了生成分布与真实分布接近。这项工作为化学信息学中一个核心问题——从复杂能量分布中采样——提供了一种基于机器学习（归一化流）的严格数学框架和高效计算方法。该方法直接针对分子结构（蛋白质）的采样，与“化学大模型”中处理分子结构和性质预测的主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In a celebrated paper \cite{noe2019boltzmann}, Noé, Olsson, Köhler and Wu introduced an efficient method for sampling high-dimensional Boltzmann distributions arising in molecular dynamics via normalizing flow approximation of transport maps. Here, we place this approach on a firm mathematical foundation. We prove the existence of a normalizing flow between the reference measure and the true Boltzmann distribution up to an arbitrarily small error in the Wasserstein distance. This result covers general Boltzmann distributions from molecular dynamics, which have low regularity due to the presence of interatomic Coulomb and Lennard-Jones interactions. The proof is based on a rigorous construction of the Moser transport map for low-regularity endpoint densities and approximation theorems for neural networks in Sobolev spaces. Numerical simulations for a simple model system and for the alanine dipeptide molecule confirm that the true and generated distributions are close in the Wasserstein distance. Moreover we observe that the RealNVP architecture does not just successfully capture the equilibrium Boltzmann distribution but also the metastable dynamics.

</details>

---

### 46. [High-Fidelity Compression of Seismic Velocity Models via SIREN Auto-Decoders](https://arxiv.org/abs/2603.14284)

**基本信息**

- 🔗 arXiv: [`2603.14284`](https://arxiv.org/abs/2603.14284)
- 👥 作者: Caiyun Liu, Xiaoxue Luo, Jie Xiong
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14284.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个基于SIREN自解码器的神经压缩框架，用于表示和压缩地震速度模型。这为化学信息学和相关领域（如材料科学、地球化学）中处理复杂、高维结构数据提供了新的数据表示和压缩工具/方法，属于“数据资源相关”的范畴。

**📖 中文摘要**

本文提出了一种基于SIREN（正弦表示网络）自解码器的高保真神经压缩框架，用于表示来自OpenFWI基准的多结构地震速度模型。该方法将每个70x70的速度图（4900个点）压缩成一个紧凑的256维潜在向量，实现了19:1的压缩比。实验在五个不同的地质家族上进行，展示了高保真重建（平均PSNR 32.47 dB， SSIM 0.956）。此外，该方法展示了隐式神经表示的两个关键优势：平滑的潜在空间插值（可生成合理的中间速度结构）和零样本超分辨率能力（可在无需额外训练的情况下以任意分辨率重建速度场）。这项工作为地球物理数据的高效存储、多尺度分析和下游应用（如全波形反演）提供了新工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Implicit Neural Representations (INRs) have emerged as a powerful paradigm for representing continuous signals independently of grid resolution. In this paper, we propose a high-fidelity neural compression framework based on a SIREN (Sinusoidal Representation Networks) auto-decoder to represent multi-structural seismic velocity models from the OpenFWI benchmark. Our method compresses each 70x70 velocity map (4,900 points) into a compact 256-dimensional latent vector, achieving a compression ratio of 19:1. We evaluate the framework on 1,000 samples across five diverse geological families: FlatVel, CurveVel, FlatFault, CurveFault, and Style. Experimental results demonstrate an average PSNR of 32.47 dB and SSIM of 0.956, indicating high-quality reconstruction. Furthermore, we showcase two key advantages of our implicit representation: (1) smooth latent space interpolation that generates plausible intermediate velocity structures, and (2) zero-shot super-resolution capability that reconstructs velocity fields at arbitrary resolutions up to 280x280 without additional training. The results highlight the potential of INR-based auto-decoders for efficient storage, multi-scale analysis, and downstream geophysical applications such as full waveform inversion.

</details>

---

### 47. [Windowed Fourier Propagator: A Frequency-Local Neural Operator for Wave Equations in Inhomogeneous Media](https://arxiv.org/abs/2603.14289)

**基本信息**

- 🔗 arXiv: [`2603.14289`](https://arxiv.org/abs/2603.14289)
- 👥 作者: Yiyang Cai, Zixuan Qiu, Yunlu Shu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14289.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是提出一种新型神经算子（Windowed Fourier Propagator）来高效学习波动方程的解算子。这属于利用“大模型”（此处指神经算子，一种用于学习偏微分方程解算子的机器学习模型）解决科学计算（物理建模）问题，与“化学大模型”中利用先进AI模型解决科学问题的核心精神一致。

**📖 中文摘要**

本文提出了窗口傅里叶传播子（WFP），一种用于非均匀介质中波动方程的新型神经算子。其设计基于频率局域性这一物理原理，即波能量主要散射到相邻频率。通过学习一组紧凑的、局部化的传播子，每个传播子将输入频率映射到一小组输出窗口，该方法避免了密集交互模型的复杂性并实现了计算效率。另一个关键特征是显式保持叠加原理，这使得模型能够从简单的训练数据（如平面波）显著泛化到任意的复杂波状态。作者证明WFP为复杂介质中的数据驱动波建模提供了一个可解释、高效且准确的框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Wave equations are fundamental to describing a vast array of physical phenomena, yet their simulation in inhomogeneous media poses a computational challenge due to the highly oscillatory nature of the solutions. To overcome the high costs of traditional solvers, we propose the Windowed Fourier Propagator (WFP), a novel neural operator that efficiently learns the solution operator. The WFP's design is rooted in the physical principle of frequency locality, where wave energy scatters primarily to adjacent frequencies. By learning a set of compact, localized propagators, each mapping an input frequency to a small window of outputs, our method avoids the complexity of dense interaction models and achieves computational efficiency. Another key feature is the explicit preservation of superposition, which enables remarkable generalization from simple training data (e.g., plane waves) to arbitrary, complex wave states. We demonstrate that the WFP provides an explainable, efficient and accurate framework for data-driven wave modeling in complex media.

</details>

---

### 48. [Autonomous Agents Coordinating Distributed Discovery Through Emergent Artifact Exchange](https://arxiv.org/abs/2603.14312)

**基本信息**

- 🔗 arXiv: [`2603.14312`](https://arxiv.org/abs/2603.14312)
- 👥 作者: Fiona Y. Wang, Lee Marom, Subhadeep Pal 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14312.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个由多个AI智能体（Agent）组成的自主科学探究框架。这些智能体能够使用工具、生成数据并进行推理，这体现了“化学大模型”或更广义的“科学AI”向自主化、智能体化发展的前沿趋势。框架的核心是构建能够进行复杂科学发现任务的AI系统。

**📖 中文摘要**

本文提出了ScienceClaw + Infinite框架，用于自主科学探究。在该框架中，独立的智能体（Agent）在没有中央协调的情况下进行研究，任何贡献者都可以将新智能体部署到共享生态系统中。系统围绕三个组件构建：一个包含300多个可互操作科学技能的可扩展注册表；一个将完整计算谱系保存为有向无环图（DAG）的工件层；以及一个具有溯源感知治理功能的、基于智能体的结构化科学讨论平台。智能体根据其科学配置文件选择和链接工具，产生带有类型化元数据和父系谱系的不可变工件，并将未满足的信息需求广播到共享的全局索引。该框架展示了异构工具链、独立操作智能体之间的涌现收敛性，以及从原始计算到已发表发现的可追溯推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present ScienceClaw + Infinite, a framework for autonomous scientific investigation in which independent agents conduct research without central coordination, and any contributor can deploy new agents into a shared ecosystem. The system is built around three components: an extensible registry of over 300 interoperable scientific skills, an artifact layer that preserves full computational lineage as a directed acyclic graph (DAG), and a structured platform for agent-based scientific discourse with provenance-aware governance. Agents select and chain tools based on their scientific profiles, produce immutable artifacts with typed metadata and parent lineage, and broadcast unsatisfied information needs to a shared global index. The ArtifactReactor enables plannerless coordination: peer agents discover and fulfill open needs through pressure-based scoring, while schema-overlap matching triggers multi-parent synthesis across independent analyses. An autonomous mutation layer actively prunes the expanding artifact DAG to resolve conflicting or redundant workflows, while persistent memory allows agents to continuously build upon complex epistemic states across multiple cycles. Infinite converts these outputs into auditable scientific records through structured posts, provenance views, and machine-readable discourse relations, with community feedback steering subsequent investigation cycles. Across four autonomous investigations, peptide design for the somatostatin receptor SSTR2, lightweight impact-resistant ceramic screening, cross-domain resonance bridging biology, materials, and music, and formal analogy construction between urban morphology and grain-boundary evolution, the framework demonstrates heterogeneous tool chaining, emergent convergence among independently operating agents, and traceable reasoning from raw computation to published finding.

</details>

---

### 49. [Refold: Refining Protein Inverse Folding with Efficient Structural Matching and Fusion](https://arxiv.org/abs/2603.14350)

**基本信息**

- 🔗 arXiv: [`2603.14350`](https://arxiv.org/abs/2603.14350)
- 👥 作者: Yiran Zhu, Changxi Chi, Hongxin Xiang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14350.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是蛋白质逆折叠，即给定结构预测序列，这是计算生物学和化学信息学中的一个关键问题。所提出的Refold框架深度融合了数据库先验和深度学习模型，是构建用于蛋白质设计的“化学大模型”的一个典型范例。

**📖 中文摘要**

蛋白质逆折叠旨在为给定的蛋白质骨架结构设计氨基酸序列，是蛋白质设计中的核心任务。本文介绍了Refold，一个新颖的框架，它协同整合了数据库衍生的结构先验和深度学习预测的优势，以增强逆折叠。Refold从匹配的邻居中获取结构先验，并将其与模型预测融合以细化残基概率。为了解决低质量邻居引入噪声的问题，作者提出了动态效用门来控制先验注入，并在先验不可信时回退到基础预测。在标准基准测试上的综合评估表明，Refold在CATH 4.2和CATH 4.3上均实现了0.63的最先进天然序列恢复率。分析表明，Refold在高不确定性区域带来了更大的增益，反映了结构先验和深度学习预测之间的互补性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein inverse folding aims to design an amino acid sequence that will fold into a given backbone structure, serving as a central task in protein design. Two main paradigms have been widely explored. Template-based methods exploit database-derived structural priors and can achieve high local precision when close structural neighbors are available, but their dependence on database coverage and match quality often degrades performance on out-of-distribution (OOD) targets. Deep learning approaches, in contrast, learn general structure-to-sequence regularities and usually generalize better to new backbones. However, they struggle to capture fine-grained local structure, which can cause uncertain residue predictions and missed local motifs in ambiguous regions. We introduce Refold, a novel framework that synergistically integrates the strengths of database-derived structural priors and deep learning prediction to enhance inverse folding. Refold obtains structural priors from matched neighbors and fuses them with model predictions to refine residue probabilities. In practice, low-quality neighbors can introduce noise, potentially degrading model performance. We address this issue with a Dynamic Utility Gate that controls prior injection and falls back to the base prediction when the priors are untrustworthy. Comprehensive evaluations on standard benchmarks demonstrate that Refold achieves state-of-the-art native sequence recovery of 0.63 on both CATH 4.2 and CATH 4.3. Also, analysis indicates that Refold delivers larger gains on high-uncertainty regions, reflecting the complementarity between structural priors and deep learning predictions.

</details>

---

### 50. [LawMind: A Law-Driven Paradigm for Discovering Analytical Solutions to Partial Differential Equations](https://arxiv.org/abs/2603.14353)

**基本信息**

- 🔗 arXiv: [`2603.14353`](https://arxiv.org/abs/2603.14353)
- 👥 作者: Min-Yi Zheng, Shengqi Zhang, Liancheng Wu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14353.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个名为LawMind的AI框架，用于从偏微分方程自主发现符号形式的解析解。这代表了“科学大模型”或“AI for Science”的一个前沿方向，即开发能够进行符号推理和科学发现的AI系统，与“化学大模型”中利用AI解决复杂科学问题的目标高度契合。

**📖 中文摘要**

本文介绍了LawMind，一个定律驱动的符号发现框架，能够自主地从偏微分方程（PDE）及其相关条件构建闭式解，而无需依赖数据或监督。通过将结构化符号探索与物理约束评估相结合，LawMind在仅由控制定律引导下逐步组装有效的解组件。在从两本权威手册中抽取的100个基准PDE上进行评估，LawMind成功恢复了所有情况的闭式解析解。除了已知解之外，LawMind还进一步发现了线性和非线性PDE的先前未报告的闭式解。这些发现建立了一种计算范式，其中控制方程本身驱动自主符号发现，从而能够系统地推导PDE的解析解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Partial differential equations (PDEs) encode fundamental physical laws, yet closed-form analytical solutions for many important equations remain unknown and typically require substantial human insight to derive. Existing numerical, physics-informed, and data-driven approaches approximate solutions from data rather than systematically deriving symbolic expressions directly from governing equations. Here we introduce LawMind, a law-driven symbolic discovery framework that autonomously constructs closed-form solutions from PDEs and their associated conditions without relying on data or supervision. By integrating structured symbolic exploration with physics-constrained evaluation, LawMind progressively assembles valid solution components guided solely by governing laws. Evaluated on 100 benchmark PDEs drawn from two authoritative handbooks, LawMind successfully recovers closed-form analytical solutions for all cases. Beyond known solutions, LawMind further discovers previously unreported closed-form solutions to both linear and nonlinear PDEs. These findings establish a computational paradigm in which governing equations alone drive autonomous symbolic discovery, enabling the systematic derivation of analytical PDE solutions.

</details>

---

### 51. [ES-Merging: Biological MLLM Merging via Embedding Space Signals](https://arxiv.org/abs/2603.14405)

**基本信息**

- 🔗 arXiv: [`2603.14405`](https://arxiv.org/abs/2603.14405)
- 👥 作者: Wonbin Lee, Dongki Kim, Sung Ju Hwang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14405.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕构建和整合用于科学发现（包括化学领域）的多模态大语言模型（MLLMs），即“化学大模型”。

**📖 中文摘要**

这篇论文提出了一种名为ES-Merging的新框架，用于合并针对不同模态（例如，化学、生物）训练的生物多模态大语言模型（MLLMs），以解决跨模态科学问题。现有方法依赖于与输入无关的参数空间启发式方法，无法有效捕获模态特异性。ES-Merging通过嵌入空间信号来估计合并系数，首先设计包含不同模态令牌的探针输入，通过每个专门的MLLM获取反映模态特定表示变化的层间嵌入响应，然后从嵌入空间中估计粗粒度的层级系数和细粒度的元素级系数，并将它们联合组合以进行稳健的系数估计。在交互效应预测基准测试中，该方法优于现有的合并方法，甚至超过了特定任务微调的模型。这项工作直接涉及构建用于科学发现的化学/生物大模型（化学大模型），并提供了整合多模态专业知识的工具和方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biological multimodal large language models (MLLMs) have emerged as powerful foundation models for scientific discovery. However, existing models are specialized to a single modality, limiting their ability to solve inherently cross-modal scientific problems. While model merging is an efficient method to combine the different modalities into a unified MLLM, existing methods rely on input-agnostic parameter space heuristics that fail to faithfully capture modality specialization. To overcome this limitation, we propose a representation-aware merging framework that estimates merging coefficients from embedding space signals. We first design a probe input that consists of different modality tokens and forward it through each specialized MLLM to obtain layer-wise embedding responses that reflect modality-specific representation changes. We then estimate complementary merging coefficients at two granularities from the embedding space: layer-wise coefficients from coarse-grained signals and element-wise coefficients from fine-grained signals, which are jointly combined for robust coefficient estimation. Experiments on interactive effect prediction benchmarks show that our method outperforms existing merging methods and even surpasses task-specific fine-tuned models, establishing that embedding space signals provide a principled and effective foundation for cross-modal MLLM merging.

</details>

---

### 52. [Graph-Based Deep Learning for Intelligent Detection of Energy Losses, Theft, and Operational Inefficiencies in Oil & Gas Production Networks](https://arxiv.org/abs/2603.14406)

**基本信息**

- 🔗 arXiv: [`2603.14406`](https://arxiv.org/abs/2603.14406)
- 👥 作者: AbdulQoyum A. Olowookere, Adewale U. Oguntola, Ebenezer. Leke Odekanle
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14406.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用图神经网络进行复杂工业系统（包括化学生产网络）的异常检测和模式推理。其方法论（从复杂、高维、相互关联的数据中学习并推理）与“质谱结构推理”领域解决的核心问题（从复杂的质谱信号中推断分子结构）在技术路径上高度相关。

**📖 中文摘要**

本研究提出了一个基于时空图深度学习的框架，用于检测石油和天然气生产网络中的能量损失、盗窃和运行低效问题。该框架将生产系统建模为井、设施和油田的分层图，并利用时间图注意力网络（Temporal Graph Attention Network）来学习关系依赖性和捕获时间动态。弱监督的异常标签是基于生产、压力和流动行为的物理信息启发式方法推导出来的。该模型在基于时间的评估中实现了约0.98的ROC-AUC和高于0.93的异常召回率。这项工作展示了图神经网络在复杂工业系统（如化学生产网络）中进行异常检测和模式推理的先进应用，其方法论（图神经网络学习复杂系统内的依赖关系）与从复杂数据（如质谱）中进行结构推理的核心挑战有概念上的相似性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early detection of energy losses, theft, and operational inefficiencies remains a critical challenge in oil and gas production systems due to complex interdependencies among wells and facilities, evolving operating conditions, and limited labeled anomaly data. Traditional machine learning approaches often treat production units independently and struggle under temporal distribution shifts. This study proposes a spatiotemporal graph-based deep learning framework for anomaly detection in oil and gas production networks. The production system is modeled as a hierarchical graph of wells, facilities, and fields, with additional peer connections among wells sharing common infrastructure. Weakly supervised anomaly labels are derived from physically informed heuristics based on production, pressure, and flow behavior. Temporal dynamics are captured through sequence modeling, while relational dependencies are learned using a Temporal Graph Attention Network. Under time-based evaluation, the proposed model achieves an ROC-AUC of about 0.98 and anomaly recall above 0.93, demonstrating improved robustness and practical potential for proactive monitoring in real-world energy operations.

</details>

---

### 53. [Geometric and Topological Deep Learning for Predicting Thermo-mechanical Performance in Cold Spray Deposition Process Modeling](https://arxiv.org/abs/2603.14478)

**基本信息**

- 🔗 arXiv: [`2603.14478`](https://arxiv.org/abs/2603.14478)
- 👥 作者: Akshansh Mishra
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14478.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是应用先进的几何深度学习模型（如图神经网络、注意力网络）来模拟和预测材料科学中的物理化学过程（冷喷涂）。这属于构建能够处理化学领域复杂问题的“大模型”或高级AI模型范畴。

**📖 中文摘要**

本研究提出了一个几何深度学习框架，用于预测冷喷涂粒子冲击响应。该框架利用有限元模拟数据，实现了四种新颖的算法：GraphSAGE风格的归纳图神经网络、Chebyshev谱图卷积网络、拓扑数据分析增强的多层感知器以及几何注意力网络。每个输入样本被视为特征空间k近邻图中的一个节点，使模型能够在训练过程中利用过程条件之间的空间相似性。定量评估表明，GraphSAGE和几何注意力网络（GAT）在大多数预测目标上实现了超过0.93的R平方值。这项研究展示了先进的深度学习模型（如图神经网络和注意力机制）在模拟和预测复杂物理化学过程（材料沉积）中的应用。这些模型是构建能够理解和推理物理化学现象的“化学大模型”的重要组成部分。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study presents a geometric deep learning framework for predicting cold spray particle impact responses using finite element simulation data. A parametric dataset was generated through automated Abaqus simulations spanning a systematic range of particle velocity, particle temperature, and friction coefficient, yielding five output targets including maximum equivalent plastic strain, average contact plastic strain, maximum temperature, maximum von Mises stress, and deformation ratio. Four novel algorithms i.e. a GraphSAGE-style inductive graph neural network, a Chebyshev spectral graph convolution network, a topological data analysis augmented multilayer perceptron, and a geometric attention network were implemented and evaluated. Each input sample was treated as a node in a k-nearest-neighbour feature-space graph, enabling the models to exploit spatial similarity between process conditions during training. Three-dimensional feature space visualisations and two-dimensional contour projections confirmed the highly non-linear and velocity-dominated nature of the input-output relationships. Quantitative evaluation demonstrated that GraphSAGE and GAT consistently achieved R-square values exceeding 0.93 across most targets, with GAT attaining peak performance of R-square equal to 0.97 for maximum plastic strain. ChebSpectral and TDA-MLP performed considerably worse, yielding negative R-square values for several targets. These findings establish spatial graph-based neighbourhood aggregation as a robust and physically interpretable surrogate modelling strategy for cold spray process optimisation.

</details>

---

### 54. [Disentangling Dynamical Systems: Causal Representation Learning Meets Local Sparse Attention](https://arxiv.org/abs/2603.14483)

**基本信息**

- 🔗 arXiv: [`2603.14483`](https://arxiv.org/abs/2603.14483)
- 👥 作者: Markus W. Baumgartner, Anson Lei, Joe Watson 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14483.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用因果表示学习和Transformer等先进模型，从动态系统的观测数据中学习其底层结构和参数的解耦表示。这种方法论与“化学大模型”（需要理解化学系统的复杂表示）和“质谱结构推理”（从观测数据推断分子结构）的研究目标高度一致。

**📖 中文摘要**

本文开发了一种新颖的可识别性定理，利用因果表示学习来揭示系统参数的解耦表示，而无需结构假设。我们推导了一个图形准则，指定了系统参数何时可以从原始轨迹数据中唯一地解耦出来（直到排列和微分同胚）。我们将系统参数识别实例化为一个变分推断问题，利用稀疏正则化的Transformer来揭示状态相关的因果结构。我们在四个合成领域上实证验证了我们的方法，证明了其恢复高度解耦表示的能力，而基线方法无法恢复。这项工作在动态系统识别中融合了因果表示学习和Transformer等先进模型。其核心思想——从观测数据中学习底层系统（如化学反应动力学）的结构化、解耦表示——与“质谱结构推理”（从观测质谱数据中推断分子结构）以及构建能够理解化学动态的“化学大模型”在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Parametric system identification methods estimate the parameters of explicitly defined physical systems from data. Yet, they remain constrained by the need to provide an explicit function space, typically through a predefined library of candidate functions chosen via available domain knowledge. In contrast, deep learning can demonstrably model systems of broad complexity with high fidelity, but black-box function approximation typically fails to yield explicit descriptive or disentangled representations revealing the structure of a system. We develop a novel identifiability theorem, leveraging causal representation learning, to uncover disentangled representations of system parameters without structural assumptions. We derive a graphical criterion specifying when system parameters can be uniquely disentangled from raw trajectory data, up to permutation and diffeomorphism. Crucially, our analysis demonstrates that global causal structures provide a lower bound on the disentanglement guarantees achievable when considering local state-dependent causal structures. We instantiate system parameter identification as a variational inference problem, leveraging a sparsity-regularised transformer to uncover state-dependent causal structures. We empirically validate our approach across four synthetic domains, demonstrating its ability to recover highly disentangled representations that baselines fail to recover. Corroborating our theoretical analysis, our results confirm that enforcing local causal structure is often necessary for full identifiability.

</details>

---

### 55. [Predicting Stress-strain Behaviors of Additively Manufactured Materials via Loss-based and Activation-based Physics-informed Machine Learning](https://arxiv.org/abs/2603.14489)

**基本信息**

- 🔗 arXiv: [`2603.14489`](https://arxiv.org/abs/2603.14489)
- 👥 作者: Chenglong Duan, Dazhong Wu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14489.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发物理信息机器学习（PIML）模型，用于准确预测材料（包括化学材料）的力学性能。该方法将领域物理知识嵌入AI模型，是构建用于化学和材料科学的可靠、可解释大模型（化学大模型）的重要研究方向。

**📖 中文摘要**

本研究提出了一个物理信息机器学习（PIML）框架，用于预测增材制造聚合物和金属的应力-应变行为。该框架将多项式回归模型与两个长短期记忆（LSTM）模型相结合，分别预测弹性和塑性区域。通过将胡克定律、Voce硬化定律和Hollomon定律等物理定律嵌入到损失函数或激活函数中，开发了基于损失和基于激活的PIML架构。在尼龙、碳纤维-ABS、AlSi10Mg和Ti6Al4V四种增材制造材料的实验数据上，所提出的PIML架构在预测应力-应变曲线方面 consistently 优于其他机器学习模型和物理本构模型。这项工作展示了如何将领域知识（物理定律）整合到机器学习模型中，以改善其在材料化学/力学属性预测方面的性能和可解释性。这是构建“化学大模型”或更广泛的“科学AI”的关键技术路径之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting the stress-strain behaviors of additively manufactured materials is crucial for part qualification in additive manufacturing (AM). Conventional physics-based constitutive models often oversimplify material properties, while data-driven machine learning (ML) models often lack physical consistency and interpretability. To address these issues, we propose a physics-informed machine learning (PIML) framework to improve the predictive performance and physical consistency for predicting the stress-strain curves of additively manufactured polymers and metals. A polynomial regression model is used to predict the yield point from AM process parameters, then stress-strain curves are segmented into elastic and plastic regions. Two long short-term memory (LSTM) models are trained to predict two regions separately. For the elastic region, Hooke's law is embedded into the LSTM model for both polymer and metal. For the plastic region, Voce hardening law and Hollomon's law are embedded into the LSTM model for polymer and metal, respectively. The loss-based and activation-based PIML architectures are developed by embedding the physical laws into the loss and activation functions, respectively. The performance of the two PIML architectures are compared with two LSTM-based ML models, three additional ML models, and a physics-based constitutive model. These models are built on experimental data collected from two additively manufactured polymers (i.e., Nylon and carbon fiber-acrylonitrile butadiene styrene) and two additively manufactured metals (i.e., AlSi10Mg and Ti6Al4V). Experimental results demonstrate that two PIML architectures consistently outperform the other models. The segmental predictive model with activation-based PIML architecture achieves the lowest MAPE of 10.46+/-0.81% and the highest R^2 of 0.82+/-0.05 arocss four datasets.

</details>

---

### 56. [Excited Pfaffians: Generalized Neural Wave Functions Across Structure and State](https://arxiv.org/abs/2603.14515)

**基本信息**

- 🔗 arXiv: [`2603.14515`](https://arxiv.org/abs/2603.14515)
- 👥 作者: Nicholas Gao, Till Grutschus, Frank Noé 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14515.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种名为“激发态Pfaffians”的新型神经网络架构，用于在量子化学中高效、准确地表示分子和原子的多个量子态。这直接属于构建用于计算化学和量子化学模拟的“化学大模型”。

**📖 中文摘要**

我们提出了“激发态Pfaffian”（Excited Pfaffians），这是一种受哈特里-福克方法启发的神经网络波函数架构，可以在单个神经网络中表示多个量子态。该架构作为广义波函数，允许单个模型表示多态势能面。我们在碳二聚体上进行了测试，匹配了O(N_s^4)标度的自然激发态，同时训练速度快了200倍以上，并且建模了多50%的态。我们首次使用神经网络找到了铍原子的所有不同能级。此外，我们证明单个波函数可以表示各种分子的激发态。这项工作代表了在量子化学计算中应用高级神经网络架构（“化学大模型”）的前沿进展，旨在以统一、高效的模型处理复杂的量子态和分子系统。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Neural-network wave functions in Variational Monte Carlo (VMC) have achieved great success in accurately representing both ground and excited states. However, achieving sufficient numerical accuracy in state overlaps requires increasing the number of Monte Carlo samples, and consequently the computational cost, with the number of states. We present a nearly constant sample-size approach, Multi-State Importance Sampling (MSIS), that leverages samples from all states to estimate pairwise overlap. To efficiently evaluate all states for all samples, we introduce Excited Pfaffians. Inspired by Hartree-Fock, this architecture represents many states within a single neural network. Excited Pfaffians also serve as generalized wave functions, allowing a single model to represent multi-state potential energy surfaces. On the carbon dimer, we match the $O(N_s^4)$-scaling natural excited states while training $>200\times$ faster and modeling 50\% more states. Our favorable scaling enables us to be the first to use neural networks to find all distinct energy levels of the beryllium atom. Finally, we demonstrate that a single wave function can represent excited states across various molecules.

</details>

---

### 57. [Learning to Forget: Sleep-Inspired Memory Consolidation for Resolving Proactive Interference in Large Language Models](https://arxiv.org/abs/2603.14517)

**基本信息**

- 🔗 arXiv: [`2603.14517`](https://arxiv.org/abs/2603.14517)
- 👥 作者: Ying Xie
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14517.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种新颖的、受生物学启发的AI模型记忆管理机制。虽然应用场景是文本，但其处理序列数据干扰、提取和巩固关键信息的核心方法论，对于处理类似质谱这样的复杂时间序列/频谱数据以进行结构推理，具有潜在的相关性和启发性。

**📖 中文摘要**

本文提出了SleepGate，一个受睡眠启发的记忆巩固框架，用于解决大语言模型（LLMs）中的主动干扰问题。该框架通过在学习到的睡眠周期中对键值（KV）缓存进行操作，引入了冲突感知时间标记器、轻量级遗忘门和巩固模块。这些组件在推理过程中周期性地激活，选择性地驱逐或压缩过时的缓存条目，并将存活的条目合并为紧凑的摘要。理论分析表明，SleepGate将干扰范围从O(n)减少到O(log n)。在小规模Transformer上的实验表明，SleepGate在主动干扰深度为5和10时分别实现了99.5%和97.0%的检索准确率，显著优于所有基线。这项工作虽然主要针对LLMs的文本缓存优化，但其核心思想——通过选择性遗忘和记忆合并来管理序列数据中的干扰并提取关键信息——与处理复杂、高维序列数据（如质谱或色谱时间序列）以进行“质谱结构推理”所面临的挑战有概念上的相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) suffer from proactive interference (PI): outdated information in the context window disrupts retrieval of current values. This interference degrades retrieval accuracy log-linearly as stale associations accumulate, a bottleneck that persists regardless of context length and resists prompt-engineering mitigations. Biological brains resolve an analogous challenge through sleep-dependent memory consolidation: synaptic downscaling, selective replay, and targeted forgetting. We propose SleepGate, a biologically inspired framework that augments transformer-based LLMs with a learned sleep cycle over the key-value (KV) cache. SleepGate introduces three mechanisms: (1) a conflict-aware temporal tagger detecting when new entries supersede old ones; (2) a lightweight forgetting gate trained to selectively evict or compress stale cache entries; and (3) a consolidation module that merges surviving entries into compact summaries. These components activate periodically during inference in sleep micro-cycles, governed by an adaptive entropy-based trigger. We formalize a dual-phase training objective jointly optimizing language modeling during the wake phase and post-consolidation retrieval during the sleep phase. Theoretical analysis shows SleepGate reduces the interference horizon from O(n) to O(log n). In experiments with a small-scale transformer (4 layers, 793K parameters), SleepGate achieves 99.5% retrieval accuracy at PI depth 5 and 97.0% at depth 10, while all five baselines -- full KV cache, sliding window, H2O, StreamingLLM, and decay-only ablation -- remain below 18%. Our framework offers an architecture-level solution that prompt engineering cannot address.

</details>

---

### 58. [Expert Mind: A Retrieval-Augmented Architecture for Expert Knowledge Preservation in the Energy Sector](https://arxiv.org/abs/2603.14541)

**基本信息**

- 🔗 arXiv: [`2603.14541`](https://arxiv.org/abs/2603.14541)
- 👥 作者: Diego Ezequiel Cervera
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14541.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是构建一个基于LLM和RAG的领域专家知识保存与查询系统。这直接相关于构建特定领域的“大模型”应用（标准1）。同时，该系统框架本身可以视为一种用于构建和管理领域知识资源（数据集、工具）的方法论，可用于化学信息学和质谱分析领域（标准2）。

**📖 中文摘要**

本文提出了Expert Mind，一个实验性系统，利用检索增强生成（RAG）、大语言模型（LLMs）和多模态捕获技术来保存、结构化和查询组织知识持有者的深层专业知识。该系统针对能源等行业领域，通过结构化访谈、有声思维会话和文本语料库摄取来获取知识，随后将其嵌入向量存储并通过对话界面进行查询。初步设计考虑表明，Expert Mind可以显著减少知识转移延迟并提高入职效率。这项工作展示了如何利用大语言模型和RAG架构来构建领域特定的知识库和专家系统。虽然应用领域是能源，但其技术框架（LLMs + RAG + 领域知识）完全适用于构建“化学大模型”或“质谱分析专家系统”，用于保存和查询化学家、质谱专家的专业知识，或作为智能助手辅助结构解析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The departure of subject-matter experts from industrial organizations results in the irreversible loss of tacit knowledge that is rarely captured through conventional documentation practices. This paper proposes Expert Mind, an experimental system that leverages Retrieval-Augmented Generation (RAG), large language models (LLMs), and multimodal capture techniques to preserve, structure, and make queryable the deep expertise of organizational knowledge holders. Drawing on the specific context of the energy sector, where decades of operational experience risk being lost to an aging workforce, we describe the system architecture, processing pipeline, ethical framework, and evaluation methodology. The proposed system addresses the knowledge elicitation problem through structured interviews, think-aloud sessions, and text corpus ingestion, which are subsequently embedded into a vector store and queried through a conversational interface. Preliminary design considerations suggest Expert Mind can significantly reduce knowledge transfer latency and improve onboarding efficiency. Ethical dimensions including informed consent, intellectual property, and the right to erasure are addressed as first-class design constraints.

</details>

---

### 59. [Can Large Language Models Evaluate Grant Proposal Quality? Revisiting the Wennerås and Wold Peer Review Data](https://arxiv.org/abs/2603.14565)

**基本信息**

- 🔗 arXiv: [`2603.14565`](https://arxiv.org/abs/2603.14565)
- 👥 作者: Ulf Sandström, Mike Thelwall
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14565.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估大型语言模型（LLMs）在特定科学评估任务（基金评审）中的能力。'化学大模型'是大型语言模型在科学领域应用的一个子集，本文直接围绕LLM的科学评估能力展开，属于核心主题相关。

**📖 中文摘要**

本文探讨了大型语言模型（LLMs）在评估科研项目申请书质量方面的能力。研究使用了一个历史数据集（1994年瑞典医学研究委员会的博士后基金申请），将多种中等规模开源LLM的评分与同行评审专家的评分进行了比较。研究发现，LLM评分之间具有中等相关性，但与专家平均评分的相关性较弱但为正，且大多具有统计显著性。其中，基于申请书标题和摘要（不含正文）的Gemma 3 27b模型与专家评分的秩相关性最高，约为评审专家间相关性的一半。尽管LLM在定量评估能力上弱于专家，但研究认为LLM可能在申请初筛或打破平局等环节发挥作用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Purpose: Despite the importance of peer review for grant funding decisions, academics are often reluctant to conduct it. This can lead to long delays between submission and the final decision as well as the risk of substandard reviews from busy or non-specialist scholars. At least one funder now uses Large Language Models (LLMs) to reduce the reviewing burden but the accuracy of LLMs for scoring grant proposals needs to be assessed. Design/methodology/approach: This article compares scores from a range of medium sized open weights LLMs with peer review scores for a well-researched dataset, the Swedish Medical Council's post-doctoral fellowship applications from 1994. Findings: Whilst the LLM scores correlate moderately between each other (mean Spearman correlation: 0.34), they correlated weakly but positively and mostly statistically significantly with the average expert scores (mean Spearman correlation: 0.22). The highest rank correlation between expert scores and LLMs was 0.33 for Gemma 3 27b based on proposal titles and summaries without their main texts, which is about half (56%) of the correlation between reviewers. Research limitations: The small sample size, old funding call and heterogeneous evaluation criteria all undermine the robustness of the analysis. Practical implications: Despite the ability of LLMs to score grant proposals being quantitatively weaker than that of experts, at least in this special case, they may have role in application triage or tie-breaking. Originality/value: This is the first assessment of the value of LLM scores for funding proposals.

</details>

---

### 60. [CausalEvolve: Towards Open-Ended Discovery with Causal Scratchpad](https://arxiv.org/abs/2603.14575)

**基本信息**

- 🔗 arXiv: [`2603.14575`](https://arxiv.org/abs/2603.14575)
- 👥 作者: Yongqiang Chen, Chenxi Liu, Zhenhao Chen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14575.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个利用大型语言模型（LLMs）进行开放式科学发现的AI代理（AI Scientist）。'化学大模型'可以视为LLM在化学科学领域的特定应用或实例，本文研究的通用AI科学家框架与利用大模型进行科学发现（可能包括化学发现）的主题直接相关。

**📖 中文摘要**

本文提出了CausalEvolve，一个旨在解决开放式科学发现问题的AI科学家代理框架。该框架基于演化算法（如AlphaEvolve），利用大型语言模型（LLMs）的先验知识和推理能力来迭代改进和演化程序。为了解决现有演化代理缺乏针对性指导和有效利用历史演化知识的问题，CausalEvolve引入了一个因果草稿本（causal scratchpad），利用LLM来识别和推理演化的指导因素。在演化开始时，它识别结果层面的因素；在演化过程中，通过观察意外模式并进行溯因推理来假设新的因素，从而提供新的演化方向。实验表明，CausalEvolve在四个具有挑战性的开放式科学任务中有效提高了演化效率并发现了更好的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Evolve-based agent such as AlphaEvolve is one of the notable successes in using Large Language Models (LLMs) to build AI Scientists. These agents tackle open-ended scientific problems by iteratively improving and evolving programs, leveraging the prior knowledge and reasoning capabilities of LLMs. Despite the success, existing evolve-based agents lack targeted guidance for evolution and effective mechanisms for organizing and utilizing knowledge acquired from past evolutionary experience. Consequently, they suffer from decreasing evolution efficiency and exhibit oscillatory behavior when approaching known performance boundaries. To mitigate the gap, we develop CausalEvolve, equipped with a causal scratchpad that leverages LLMs to identify and reason about guiding factors for evolution. At the beginning, CausalEvolve first identifies outcome-level factors that offer complementary inspirations in improving the target objective. During the evolution, CausalEvolve also inspects surprise patterns during the evolution and abductive reasoning to hypothesize new factors, which in turn offer novel directions. Through comprehensive experiments, we show that CausalEvolve effectively improves the evolutionary efficiency and discovers better solutions in 4 challenging open-ended scientific tasks.

</details>

---

### 61. [ResearchPilot: A Local-First Multi-Agent System for Literature Synthesis and Related Work Drafting](https://arxiv.org/abs/2603.14629)

**基本信息**

- 🔗 arXiv: [`2603.14629`](https://arxiv.org/abs/2603.14629)
- 👥 作者: Peng Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14629.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于文献检索、信息提取和综合的工具（ResearchPilot）。虽然其应用领域是通用的文献综述，但其核心功能（从科学文献库中检索和结构化提取信息）是构建科学领域大模型（如化学大模型）所需数据资源或工具链的重要组成部分。因此，它提供了可用于相关主题的数据处理工具。

**📖 中文摘要**

本文介绍了ResearchPilot，一个开源、可自托管的多智能体系统，用于辅助文献综述工作。给定一个自然语言研究问题，该系统能够从Semantic Scholar和arXiv检索相关论文，从论文摘要中提取结构化发现，综合跨论文的模式，并起草一份带有引用的相关工作章节。系统结合了FastAPI、DSPy、SQLite和Qdrant，采用本地优先架构，支持用户自带API密钥访问模型和远程或本地嵌入。论文描述了系统设计、类型化的智能体接口、持久化和历史搜索机制，以及构建透明研究助手所涉及的工程权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

ResearchPilot is an open-source, self-hostable multi-agent system for literature-review assistance. Given a natural-language research question, it retrieves papers from Semantic Scholar and arXiv, extracts structured findings from paper abstracts, synthesizes cross-paper patterns, and drafts a citation-aware related-work section. The system combines FastAPI, this http URL , DSPy, SQLite, and Qdrant in a local-first architecture that supports bring-your-own-key model access and remote-or-local embeddings. This paper describes the system design, typed agent interfaces, persistence and history-search mechanisms, and the engineering tradeoffs involved in building a transparent research assistant. Rather than claiming algorithmic novelty, we present ResearchPilot as a systems contribution and evaluate it through automated tests and end-to-end local runs. We discuss limitations including external API rate limits, abstract-only extraction, incomplete corpus coverage, and the lack of citation verification.

</details>

---

### 62. [Gradient Atoms: Unsupervised Discovery, Attribution and Steering of Model Behaviors via Sparse Decomposition of Training Gradients](https://arxiv.org/abs/2603.14665)

**基本信息**

- 🔗 arXiv: [`2603.14665`](https://arxiv.org/abs/2603.14665)
- 👥 作者: J Rosser
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14665.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是分析和操控大型语言模型（LLMs）的内部行为与知识。'化学大模型'作为特定领域的大模型，其行为分析、知识归因和可控生成同样是该领域的关键问题。本文提出的无监督方法为理解和控制大模型（包括化学大模型）的行为提供了新的技术思路。

**📖 中文摘要**

本文提出了Gradient Atoms，一种无监督方法，用于发现和归因语言模型中的行为。该方法通过字典学习，将每个训练文档的梯度分解为稀疏组件（称为“原子”）。这些原子在预处理的特征空间中被发现，无需行为标签即可恢复出可解释的任务类型行为（如拒绝、算术、分类等）。这些原子还可以作为有效的控制向量：在权重空间应用这些向量作为扰动，可以产生大规模、可控的模型行为偏移。该方法不需要针对特定查询行为对每个训练文档进行评分，其计算成本与感兴趣的行为数量无关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Training data attribution (TDA) methods ask which training documents are responsible for a model behavior. We argue that this per-document framing is fundamentally mismatched to how fine-tuning actually works: models often learn broad concepts shared across many examples. Existing TDA methods are supervised -- they require a query behavior, then score every training document against it -- making them both expensive and unable to surface behaviors the user did not think to ask about. We present Gradient Atoms, an unsupervised method that decomposes per-document training gradients into sparse components ("atoms") via dictionary learning in a preconditioned eigenspace. Among the 500 discovered atoms, the highest-coherence ones recover interpretable task-type behaviors -- refusal, arithmetic, yes/no classification, trivia QA -- without any behavioral labels. These atoms double as effective steering vectors: applying them as weight-space perturbations produces large, controllable shifts in model behavior (e.g., bulleted-list generation 33% to 94%; systematic refusal 50% to 0%). The method requires no query--document scoring stage, and scales independently of the number of query behaviors of interest. Code is here: this https URL

</details>

---

### 63. [Seamless Deception: Larger Language Models Are Better Knowledge Concealers](https://arxiv.org/abs/2603.14672)

**基本信息**

- 🔗 arXiv: [`2603.14672`](https://arxiv.org/abs/2603.14672)
- 👥 作者: Dhananjay Ashok, Ruth-Ann Armstrong, Jonathan May
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14672.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大型语言模型（LLMs）的安全性与可靠性，特别是模型隐藏其所有知识的能力。这对于评估和部署任何领域的大模型（包括化学大模型）都至关重要，涉及模型审计、可信度评估等核心主题。

**📖 中文摘要**

本文研究了语言模型（LMs）可能获取有害知识，并在审计时伪装对此类话题无知的行为（即知识隐藏）。受近期在LMs中发现欺骗相关行为模式的启发，本文旨在训练分类器来检测LM何时在主动隐藏知识。在较小模型上的初步发现表明，分类器比人类评估者更能可靠地检测隐藏行为，基于梯度的隐藏比基于提示的方法更容易识别。然而，与先前工作相反，研究发现分类器不能可靠地推广到未见过的模型架构和隐藏知识主题。最令人担忧的是，与隐藏行为相关的可识别痕迹随着模型规模的增大而变淡，分类器在参数超过700亿的任何模型上的表现都不优于随机猜测。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Language Models (LMs) may acquire harmful knowledge, and yet feign ignorance of these topics when under audit. Inspired by the recent discovery of deception-related behaviour patterns in LMs, we aim to train classifiers that detect when a LM is actively concealing knowledge. Initial findings on smaller models show that classifiers can detect concealment more reliably than human evaluators, with gradient-based concealment proving easier to identify than prompt-based methods. However, contrary to prior work, we find that the classifiers do not reliably generalize to unseen model architectures and topics of hidden knowledge. Most concerningly, the identifiable traces associated with concealment become fainter as the models increase in scale, with the classifiers achieving no better than random performance on any model exceeding 70 billion parameters. Our results expose a key limitation in black-box-only auditing of LMs and highlight the need to develop robust methods to detect models that are actively hiding the knowledge they contain.

</details>

---

### 64. [Towards Next-Generation LLM Training: From the Data-Centric Perspective](https://arxiv.org/abs/2603.14712)

**基本信息**

- 🔗 arXiv: [`2603.14712`](https://arxiv.org/abs/2603.14712)
- 👥 作者: Hao Liang, Zhengyang Zhao, Zhaoyang Han 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14712.pdf)

**💡 相关性分析**

满足标准3：论文是对大语言模型（LLMs）训练中数据问题的综述和展望。它系统分析了当前数据处理的局限性，并提出了未来的研究方向。'化学大模型'作为领域大模型，其训练同样严重依赖高质量数据，本文的讨论对其数据集的构建、管理和高效利用具有重要的指导意义，属于包含重要相关讨论的综述展望类论文。

**📖 中文摘要**

本文从数据中心的视角探讨了下一代大语言模型（LLM）训练所面临的挑战和未来方向。作者指出，尽管数据在LLM的成功中扮演核心角色，但大规模训练数据的准备和有效利用仍然是主要瓶颈。当前实践中，LLM训练数据通常通过临时脚本构建，缺乏成熟的、基于智能体的数据准备系统。此外，数据集一旦收集，通常在训练中被整体消耗，缺乏系统的数据选择、混合优化或重加权机制。为此，作者倡导两个互补的研究方向：一是构建健壮的、基于智能体的自动数据准备系统；二是建立一个统一的数据-模型交互训练系统，实现训练过程中数据的动态选择、混合和重加权。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have demonstrated remarkable performance across a wide range of tasks and domains, with data playing a central role in enabling these advances. Despite this success, the preparation and effective utilization of the massive datasets required for LLM training remain major bottlenecks. In current practice, LLM training data is often constructed using ad hoc scripts, and there is still a lack of mature, agent-based data preparation systems that can automatically construct robust and reusable data workflows, thereby freeing data scientists from repetitive and error-prone engineering efforts. Moreover, once collected, datasets are often consumed largely in their entirety during training, without systematic mechanisms for data selection, mixture optimization, or reweighting. To address these limitations, we advocate two complementary research directions. First, we propose building a robust, agent-based automatic data preparation system that supports automated workflow construction and scalable data management. Second, we argue for a unified data-model interaction training system in which data is dynamically selected, mixed, and reweighted throughout the training process, enabling more efficient, adaptive, and performance-aware data utilization. Finally, we discuss the remaining challenges and outline promising directions for future research and system development.

</details>

---

### 65. [Training-Free Generation of Protein Sequences from Small Family Alignments via Stochastic Attention](https://arxiv.org/abs/2603.14717)

**基本信息**

- 🔗 arXiv: [`2603.14717`](https://arxiv.org/abs/2603.14717)
- 👥 作者: Jeffrey D. Varner
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14717.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用基于注意力机制的生成模型（随机注意力）进行蛋白质序列生成。蛋白质的质谱分析是推断其结构的关键步骤，而序列是结构的基础。本文提出的方法直接涉及从有限数据中生成合理的生物分子（蛋白质）序列，这与'质谱结构推理'中从谱图推断分子结构（尤其是序列作为一级结构）的主题高度相关。该方法为小数据场景下的分子生成提供了新思路。

**📖 中文摘要**

本文提出了随机注意力（Stochastic Attention, SA），一种免训练采样器，用于从小的蛋白质家族比对中生成蛋白质序列。该方法将现代Hopfield能量视为玻尔兹曼分布，并通过朗之万动力学进行采样。其评分函数是一个闭式的softmax注意力操作，无需训练、预训练数据或GPU，计算成本与比对大小呈线性关系。在八个Pfam家族上的实验表明，SA生成的序列具有较低的氨基酸组成差异、显著的新颖性，并且经ESMFold和AlphaFold2确认具有结构合理性。与profile HMMs、EvoDiff和MSA Transformer相比，SA生成的序列在保持新颖性的同时，与家族的一致性在51%到66%之间，且运行速度极快。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Most protein families have fewer than 100 known members, a regime where deep generative models overfit or collapse. We propose stochastic attention (SA), a training-free sampler that treats the modern Hopfield energy over a protein alignment as a Boltzmann distribution and draws samples via Langevin dynamics. The score function is a closed-form softmax attention operation requiring no training, no pretraining data, and no GPU, with cost linear in alignment size. Across eight Pfam families, SA generates sequences with low amino acid compositional divergence, substantial novelty, and structural plausibility confirmed by ESMFold and AlphaFold2. Generated sequences fold more faithfully to canonical family structures than natural members in six of eight families. Against profile HMMs, EvoDiff, and the MSA Transformer, which produce sequences that drift far outside the family, SA maintains 51 to 66 percent identity while remaining novel, in seconds on a laptop. The critical temperature governing generation is predicted from PCA dimensionality alone, enabling fully automatic operation. Controls confirm SA encodes correlated substitution patterns, not just per-position amino acid frequencies.

</details>

---

### 66. [Multimodal Deep Learning for Early Prediction of Patient Deterioration in the ICU: Integrating Time-Series EHR Data with Clinical Notes](https://arxiv.org/abs/2603.14719)

**基本信息**

- 🔗 arXiv: [`2603.14719`](https://arxiv.org/abs/2603.14719)
- 👥 作者: Binesh Sadanandan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14719.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个结合时间序列和文本数据（临床笔记）的多模态深度学习框架，并使用了MIMIC-IV这一大型公开数据集。虽然应用领域是医疗，但其方法论核心——多模态数据融合、时间序列处理、文本信息提取——与构建科学领域大模型（如化学大模型）所需处理异构数据（如化学时间序列数据、文献文本）的技术栈高度相关。论文提供了可用于相关主题的方法论参考和数据集范例。

**📖 中文摘要**

本文提出了一种多模态深度学习方法，用于早期预测重症监护室（ICU）患者的临床恶化风险。该方法结合了结构化时间序列数据（生命体征和实验室数值）与非结构化临床笔记，以预测未来24小时内患者的不良事件（如死亡、血管加压药使用、机械通气）。研究使用MIMIC-IV数据库，构建了包含74,822次ICU住院的队列，生成了570万个小时级预测样本。模型架构采用双向LSTM编码器处理生理数据的时间模式，采用ClinicalBERT嵌入处理临床笔记，并通过跨模态注意力机制进行融合。本文还对ICU恶化预测的现有方法进行了系统综述，识别了2015年至2024年间发表的31项研究。实验表明，多模态模型显著优于仅使用结构化数据的基线模型，临床笔记将AUROC提高了2.5个百分点。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Early identification of patients at risk for clinical deterioration in the intensive care unit (ICU) remains a critical challenge. Delayed recognition of impending adverse events, including mortality, vasopressor initiation, and mechanical ventilation, contributes to preventable morbidity and mortality. We present a multimodal deep learning approach that combines structured time-series data (vital signs and laboratory values) with unstructured clinical notes to predict patient deterioration within 24 hours. Using the MIMIC-IV database, we constructed a cohort of 74,822 ICU stays and generated 5.7 million hourly prediction samples. Our architecture employs a bidirectional LSTM encoder for temporal patterns in physiologic data and ClinicalBERT embeddings for clinical notes, fused through a cross-modal attention mechanism. We also present a systematic review of existing approaches to ICU deterioration prediction, identifying 31 studies published between 2015 and 2024. Most existing models rely solely on structured data and achieve area under the curve (AUC) values between 0.70 and 0.85. Studies incorporating clinical notes remain rare but show promise for capturing information not present in structured fields. Our multimodal model achieves a test AUROC of 0.7857 and AUPRC of 0.1908 on 823,641 held-out samples, with a validation-to-test gap of only 0.6 percentage points. Ablation analysis validates the multimodal approach: clinical notes improve AUROC by 2.5 percentage points and AUPRC by 39.2% relative to a structured-only baseline, while deep learning models consistently outperform classical baselines (XGBoost AUROC: 0.7486, logistic regression: 0.7171). This work contributes both a thorough review of the field and a reproducible multimodal framework for clinical deterioration prediction.

</details>

---

### 67. [GNNVerifier: Graph-based Verifier for LLM Task Planning](https://arxiv.org/abs/2603.14730)

**基本信息**

- 🔗 arXiv: [`2603.14730`](https://arxiv.org/abs/2603.14730)
- 👥 作者: Yu Hao, Qiuyu Wang, Cheng Yang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14730.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提升大语言模型（LLMs）在任务规划中的可靠性和结构性。'化学大模型'在应用于实验设计、合成路线规划等任务时，同样面临规划幻觉和结构错误的问题。本文提出的基于图结构的验证和修正框架，为增强领域大模型在复杂规划任务中的可靠性和可解释性提供了直接相关的技术方案。

**📖 中文摘要**

本文提出了GNNVerifier，一个基于图的验证器，用于大语言模型（LLM）任务规划。该方法将LLM生成的计划表示为带有丰富属性的有向图（节点为子任务，边编码执行顺序和依赖约束），然后使用图神经网络（GNN）进行结构评估和诊断，输出计划级别的合理性分数以及节点/边级别的风险分数以定位错误区域。通过从真实计划图中构建可控扰动，自动生成带有细粒度注释的训练数据。最后，根据GNN验证器的反馈，引导LLM进行局部编辑以修正计划。实验表明，GNNVerifier在提高计划质量方面取得了显著增益。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) facilitate the development of autonomous agents. As a core component of such agents, task planning aims to decompose complex natural language requests into concrete, solvable sub-tasks. Since LLM-generated plans are frequently prone to hallucinations and sensitive to long-context prom-pts, recent research has introduced plan verifiers to identify and correct potential flaws. However, most existing approaches still rely on an LLM as the verifier via additional prompting for plan review or self-reflection. LLM-based verifiers can be misled by plausible narration and struggle to detect failures caused by structural relations across steps, such as type mismatches, missing intermediates, or broken dependencies. To address these limitations, we propose a graph-based verifier for LLM task planning. Specifically, the proposed method has four major components: Firstly, we represent a plan as a directed graph with enriched attributes, where nodes denote sub-tasks and edges encode execution order and dependency constraints. Secondly, a graph neural network (GNN) then performs structural evaluation and diagnosis, producing a graph-level plausibility score for plan acceptance as well as node/edge-level risk scores to localize erroneous regions. Thirdly, we construct controllable perturbations from ground truth plan graphs, and automatically generate training data with fine-grained annotations. Finally, guided by the feedback from our GNN verifier, we enable an LLM to conduct local edits (e.g., tool replacement or insertion) to correct the plan when the graph-level score is insufficient. Extensive experiments across diverse datasets, backbone LLMs, and planners demonstrate that our GNNVerifier achieves significant gains in improving plan quality. Our data and code is available at this https URL .

</details>

---

### 68. [A Skill-augmented Agentic Framework and Benchmark for Multi-Video Understanding](https://arxiv.org/abs/2603.14733)

**基本信息**

- 🔗 arXiv: [`2603.14733`](https://arxiv.org/abs/2603.14733)
- 👥 作者: Yue Zhang, Liqiang Jing, Jia Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14733.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新的多视频理解基准测试（MVX-Bench）和一个智能体框架（SAMA）。虽然应用场景是通用视频理解，但其核心贡献——构建复杂多模态基准、设计模块化智能体框架以整合工具和进行结构化推理——为构建和评估能够处理复杂多模态数据（如化学实验视频、光谱图像序列）的科学大模型提供了重要的方法论和评估资源参考。

**📖 中文摘要**

本文针对多视频理解任务，提出了MVX-Bench基准测试和SAMA框架。MVX-Bench是一个多视频跨维度基准，将11个经典计算机视觉任务重新表述为统一的多视频问答框架，包含来自多样化真实数据集的4,255个视频上的1,442个问题。SAMA是一个技能增强的智能体框架，集成了视觉工具、任务特定技能和冲突感知验证机制，以实现迭代和结构化推理。实验结果表明，SAMA在MVX-Bench上优于强大的开源基线和GPT模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal Large Language Models have achieved strong performance in single-video understanding, yet their ability to reason across multiple videos remains limited. Existing approaches typically concatenate multiple videos into a single input and perform direct inference, which introduces training-inference mismatch, information loss from frame compression, and a lack of explicit cross-video coordination. Meanwhile, current multi-video benchmarks primarily emphasize event-level comparison, leaving identity-level matching, fine-grained discrimination, and structured multi-step reasoning underexplored. To address these gaps, we introduce MVX-Bench, a Multi-Video Cross-Dimension Benchmark that reformulates 11 classical computer vision tasks into a unified multi-video question-answering framework, comprising 1,442 questions over 4,255 videos from diverse real-world datasets. We further propose SAMA, a Skill-Augmented Agentic Framework for Multi-Video Understanding, which integrates visual tools, task-specific skills, and a conflict-aware verification mechanism to enable iterative and structured reasoning. Experimental results show that SAMA outperforms strong open-source baselines and GPT on MVX-Bench, and ablations validate the effectiveness of skill design and conflict resolution.

</details>

---

### 69. [LaPro-DTA: Latent Dual-View Drug Representations and Salient Protein Feature Extraction for Generalizable Drug--Target Affinity Prediction](https://arxiv.org/abs/2603.14792)

**基本信息**

- 🔗 arXiv: [`2603.14792`](https://arxiv.org/abs/2603.14792)
- 👥 作者: Zihan Dun, Liuyi Xu, An-Yang Lu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14792.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是药物-靶点亲和力预测，这是化学信息学和计算药物发现的核心主题，其提出的框架（潜在双视图表示、显著特征提取）直接围绕构建更鲁棒和可泛化的预测模型，与‘化学大模型’主题高度相关。

**📖 中文摘要**

本文提出LaPro-DTA，一个用于药物-靶点亲和力预测的框架，旨在解决冷启动场景下的泛化性问题。该框架设计了一种潜在双视图药物表示机制，结合实例级视图和分布级视图来学习可迁移的结构规则，而非记忆特定样本。同时，引入了一种基于模式感知的top-k池化策略来提取蛋白质的显著特征，并过滤背景噪声。通过跨视图多头注意力机制融合这些特征以建模全面的相互作用。该工作在基准数据集上的实验表明，LaPro-DTA显著优于现有方法，在具有挑战性的未见药物设置下，在Davis数据集上实现了8%的MSE降低。该研究直接涉及化学信息学中的关键任务——药物-靶点相互作用预测，其提出的框架和数据集资源对构建和评估化学大模型（特别是用于分子性质预测和相互作用的模型）具有重要价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Drug--target affinity prediction is pivotal for accelerating drug discovery, yet existing methods suffer from significant performance degradation in realistic cold-start scenarios (unseen drugs/targets/pairs), primarily driven by overfitting to training instances and information loss from irrelevant target sequences. In this paper, we propose LaPro-DTA, a framework designed to achieve robust and generalizable DTA prediction. To tackle overfitting, we devise a latent dual-view drug representation mechanism. It synergizes an instance-level view to capture fine-grained substructures with stochastic perturbation and a distribution-level view to distill generalized chemical scaffolds via semantic remapping, thereby enforcing the model to learn transferable structural rules rather than memorizing specific samples. To mitigate information loss, we introduce a salient protein feature extraction strategy using pattern-aware top-$k$ pooling, which effectively filters background noise and isolates high-response bioactive regions. Furthermore, a cross-view multi-head attention mechanism fuses these purified features to model comprehensive interactions. Extensive experiments on benchmark datasets demonstrate that LaPro-DTA significantly outperforms state-of-the-art methods, achieving an 8\% MSE reduction on the Davis dataset in the challenging unseen-drug setting, while offering interpretable insights into binding mechanisms.

</details>

---

### 70. [Multi-Task Genetic Algorithm with Multi-Granularity Encoding for Protein-Nucleotide Binding Site Prediction](https://arxiv.org/abs/2603.14797)

**基本信息**

- 🔗 arXiv: [`2603.14797`](https://arxiv.org/abs/2603.14797)
- 👥 作者: Yiming Gao, Liuyi Xu, Pengshan Cui 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14797.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是蛋白质-核苷酸结合位点预测，这是化学信息学和计算生物学中的一个关键问题。其提出的多任务学习框架、多粒度编码和遗传算法优化，为构建复杂的生物分子相互作用模型提供了方法论，与‘化学大模型’（尤其是用于生物分子建模的模型）主题相关。

**📖 中文摘要**

本文提出MTGA-MGE，一个集成了多任务遗传算法和多粒度编码的框架，用于增强蛋白质-核苷酸结合位点预测。该框架开发了一个多粒度编码网络，结合多尺度卷积和自注意力机制，从高维冗余的生物学数据中提取判别性信号。为了克服静态融合的限制，采用遗传算法自适应地演化任务特定的融合策略，从而有效提高模型泛化能力。此外，引入了一个外部邻域机制，利用生物学相似性促进跨任务的有针对性的信息交换。该框架在十五个核苷酸数据集上的广泛评估表明，MTGA-MGE不仅在数据丰富的高资源场景中建立了新的最先进水平，而且在罕见的低资源场景中也保持了强大的竞争力。该研究属于化学生物信息学领域，专注于蛋白质-配体相互作用的解码。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate identification of protein-nucleotide binding sites is fundamental to deciphering molecular mechanisms and accelerating drug discovery. However, current computational methods often struggle with suboptimal performance due to inadequate feature representation and rigid fusion mechanisms, which hinder the effective exploitation of cross-task information synergy. To bridge this gap, we propose MTGA-MGE, a framework that integrates a Multi-Task Genetic Algorithm with Multi-Granularity Encoding to enhance binding site prediction. Specifically, we develop a Multi-Granularity Encoding (MGE) network that synergizes multi-scale convolutions and self-attention mechanisms to distill discriminative signals from high-dimensional, redundant biological data. To overcome the constraints of static fusion, a genetic algorithm is employed to adaptively evolve task-specific fusion strategies, thereby effectively improving model generalization. Furthermore, to catalyze collaborative learning, we introduce an External-Neighborhood Mechanism (ENM) that leverages biological similarities to facilitate targeted information exchange across tasks. Extensive evaluations on fifteen nucleotide datasets demonstrate that MTGA-MGE not only establishes a new state-of-the-art in data-abundant, high-resource scenarios but also maintains a robust competitive edge in rare, low-resource regimes, presenting a highly adaptive scheme for decoding complex protein-ligand interactions in the post-genomic era.

</details>

---

### 71. [IgPose: A Generative Data-Augmented Pipeline for Robust Immunoglobulin-Antigen Binding Prediction](https://arxiv.org/abs/2603.14870)

**基本信息**

- 🔗 arXiv: [`2603.14870`](https://arxiv.org/abs/2603.14870)
- 👥 作者: Tien-Cuong Bui, Injae Chung, Wonjun Lee 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14870.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了SIDD（结构免疫球蛋白诱饵数据库），这是一个用于训练和评估免疫球蛋白-抗原结合预测模型的高质量合成数据集资源。该资源可直接用于‘化学大模型’或‘质谱结构推理’相关研究中，用于训练或验证分子对接、蛋白质-蛋白质相互作用预测等模型。

**📖 中文摘要**

本文提出IgPose，一个用于免疫球蛋白-抗原结合姿态识别和评分的通用框架。为了解决实验解析复合物数据稀缺的问题，该工作构建了结构免疫球蛋白诱饵数据库（SIDD），一个包含高保真合成诱饵的综合资源库。IgPose集成了等变图神经网络、ESM-2嵌入和门控循环单元，以协同捕获几何和进化特征。该框架包含两个子网络：用于结合姿态判别的IgPoseClassifier和用于DockQ评分估计的IgPoseScore。实验表明，IgPose在精心策划的内部测试集和CASP-16基准测试上相比物理和深度学习基线取得了鲁棒的性能。该工作为高通量抗体发现流程提供了一个通用的计算工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting immunoglobulin-antigen (Ig-Ag) binding remains a significant challenge due to the paucity of experimentally-resolved complexes and the limited accuracy of de novo Ig structure prediction. We introduce IgPose, a generalizable framework for Ig-Ag pose identification and scoring, built on a generative data-augmentation pipeline. To mitigate data scarcity, we constructed the Structural Immunoglobulin Decoy Database (SIDD), a comprehensive repository of high-fidelity synthetic decoys. IgPose integrates equivariant graph neural networks, ESM-2 embeddings, and gated recurrent units to synergistically capture both geometric and evolutionary features. We implemented interface-focused k-hop sampling with biologically guided pooling to enhance generalization across diverse interfaces. The framework comprises two sub-networks--IgPoseClassifier for binding pose discrimination and IgPoseScore for DockQ score estimation--and achieves robust performance on curated internal test sets and the CASP-16 benchmark compared to physics and deep learning baselines. IgPose serves as a versatile computational tool for high-throughput antibody discovery pipelines by providing accurate pose filtering and ranking. IgPose is available on GitHub ( this https URL ).

</details>

---

### 72. [BiTro: Bidirectional Transfer Learning Enhances Bulk and Spatial Transcriptomics Prediction in Cancer Pathological Images](https://arxiv.org/abs/2603.14897)

**基本信息**

- 🔗 arXiv: [`2603.14897`](https://arxiv.org/abs/2603.14897)
- 👥 作者: Jingkun Yu, Guangkai Shang, Changtao Li 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14897.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是利用病理图像预测转录组学数据，这属于生物信息学和计算病理学的交叉领域，与化学信息学中利用多模态数据推断分子表型有相似之处。同时，该工作提出的框架、模型架构以及在多个癌症数据集上的实验，为相关领域的研究提供了方法论和潜在的基准资源。

**📖 中文摘要**

本文提出BiTro，一个双向迁移学习框架，用于从病理图像中增强预测批量转录组学和空间转录组学。该框架设计了一个通用且可迁移的模型架构，适用于批量+WSI和空间转录组数据。一个主要亮点是在细胞级别对WSI图像进行建模，以更好地捕获细胞的视觉特征、形态表型及其空间关系；为了将细胞特征映射到批量或空间测量的转录组学，采用了多实例学习。其次，通过使用LoRA，该模型可以在批量数据和空间数据之间高效迁移，以利用它们的互补信息。在五个癌症数据集上的综合实验表明，1）基础模型在批量或空间转录组学预测上可以达到比现有模型更好或具有竞争力的性能；2）迁移学习可以进一步提高基础模型的性能。该研究涉及多模态生物医学数据分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cancer pathological analysis requires modeling tumor heterogeneity across multiple modalities, primarily through transcriptomics and whole slide imaging (WSI), along with their spatial relations. On one hand, bulk transcriptomics and WSI images are largely available but lack spatial mapping; on the other hand, spatial transcriptomics (ST) data can offer high spatial resolution, yet facing challenges of high cost, low sequencing depth, and limited sample sizes. Therefore, the data foundation of either side is flawed and has its limit in accurately finding the mapping between the two modalities. To this end, we propose BiTro, a bidirectional transfer learning framework that can enhance bulk and spatial transcriptomics prediction from pathological images. Our contributions are twofold. First, we design a universal and transferable model architecture that works for both bulk+WSI and ST data. A major highlight is that we model WSI images on the cellular level to better capture cells' visual features, morphological phenotypes, and their spatial relations; to map cells' features to their transcriptomics measured in bulk or ST, we adopt multiple instance learning. Second, by using LoRA, our model can be efficiently transferred between bulk and ST data to exploit their complementary information. To test our framework, we conducted comprehensive experiments on five cancer datasets. Results demonstrate that 1) our base model can achieve better or competitive performance compared to existing models on bulk or spatial transcriptomics prediction, and 2) transfer learning can further improve the base model's performance.

</details>

---

### 73. [FairMed-XGB: A Bayesian-Optimised Multi-Metric Framework with Explainability for Demographic Equity in Critical Healthcare Data](https://arxiv.org/abs/2603.14947)

**基本信息**

- 🔗 arXiv: [`2603.14947`](https://arxiv.org/abs/2603.14947)
- 👥 作者: Mitul Goswami, Romit Chatterjee, Arif Ahmed Sekh
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14947.pdf)

**💡 相关性分析**

满足标准2：该论文提供了一个用于检测和减轻临床预测模型中偏差的框架和评估方法，其提出的公平感知损失函数、优化策略和SHAP可解释性分析，为构建更公平、更可靠的化学信息学或生物医学预测模型（可视为相关工具或方法资源）提供了思路和工具。

**📖 中文摘要**

本文提出FairMed-XGB框架，旨在检测和减轻重症监护环境中机器学习模型的性别预测偏差，同时保持模型性能和可解释性。该框架集成了一个结合统计奇偶差异、泰尔指数和Wasserstein距离的公平感知损失函数，并通过贝叶斯搜索进行联合优化。在从MIMIC-IV-ED和eICU数据库衍生的七个临床不同队列上进行后缓解评估，结果显示统计奇偶差异、泰尔指数和Wasserstein距离均显著降低，且预测准确性（AUC-ROC）下降可忽略不计（<0.02）。基于SHAP的可解释性分析表明，该框架减少了对性别代理特征的依赖，为临床医生提供了关于偏差如何被纠正的可操作见解。FairMed-XGB为高风险医疗环境中公平、可信的AI部署提供了一个稳健、可解释且符合伦理的解决方案。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning models deployed in critical care settings exhibit demographic biases, particularly gender disparities, that undermine clinical trust and equitable treatment. This paper introduces FairMed-XGB, a novel framework that systematically detects and mitigates gender-based prediction bias while preserving model performance and transparency. The framework integrates a fairness-aware loss function combining Statistical Parity Difference, Theil Index, and Wasserstein Distance, jointly optimised via Bayesian Search into an XGBoost classifier. Post-mitigation evaluation on seven clinically distinct cohorts derived from the MIMIC-IV-ED and eICU databases demonstrates substantial bias reduction: Statistical Parity Difference decreases by 40 to 51 percent on MIMIC-IV-ED and 10 to 19 percent on eICU; Theil Index collapses by four to five orders of magnitude to near-zero values; Wasserstein Distance is reduced by 20 to 72 percent. These gains are achieved with negligible degradation in predictive accuracy (AUC-ROC drop <0.02). SHAP-based explainability reveals that the framework diminishes reliance on gender-proxy features, providing clinicians with actionable insights into how and where bias is corrected. FairMed-XGB offers a robust, interpretable, and ethically aligned solution for equitable clinical decision-making, paving the way for trustworthy deployment of AI in high-stakes healthcare environments.

</details>

---

### 74. [Molecular Identifier Visual Prompt and Verifiable Reinforcement Learning for Chemical Reaction Diagram Parsing](https://arxiv.org/abs/2603.15011)

**基本信息**

- 🔗 arXiv: [`2603.15011`](https://arxiv.org/abs/2603.15011)
- 👥 作者: Jiahe Song, Chuang Wang, Yinfan Wang 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15011.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”（使用视觉语言模型处理化学图表）和“质谱结构推理”的相近领域（化学反应图解析，同属从结构化数据中推理化学信息），属于核心主题相关。

**📖 中文摘要**

本文针对化学反应图解析（RxnDP）这一化学信息学关键任务，提出了两项增强视觉语言模型（VLM）性能的互补性贡献。首先，提出了“标识符作为视觉提示”（IdtVP）方法，利用图中天然存在的分子标识符（如粗体数字1a）来激活VLM在预训练阶段获得的化学知识，从而显著提升了模型的零样本和分布外泛化能力。其次，为了在微调范式中进一步优化性能，引入了Re3-DAPO强化学习算法，该算法利用可验证的奖励直接优化反应级指标，相比标准监督微调取得了一致的性能提升。此外，论文还发布了ScannedRxn基准数据集，包含带有真实世界伪影的扫描历史反应图，用于严格评估模型的鲁棒性和分布外能力。这些工作共同推进了基于VLM的反应图解析的准确性和泛化性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reaction diagram parsing (RxnDP) is critical for extracting chemical synthesis information from literature. Although recent Vision-Language Models (VLMs) have emerged as a promising paradigm to automate this complex visual reasoning task, their application is fundamentally bottlenecked by the inability to align visual chemical entities with pre-trained knowledge, alongside the inherent discrepancy between token-level training and reaction-level evaluation. To address these dual challenges, this work enhances VLM-based RxnDP from two complementary perspectives: prompting representation and learning paradigms. First, we propose Identifier as Visual Prompting (IdtVP), which leverages naturally occurring molecule identifiers (e.g., bold numerals like 1a) to activate the chemical knowledge acquired during VLM pre-training. IdtVP enables powerful zero-shot and out-of-distribution capabilities, outperforming existing prompting strategies. Second, to further optimize performance within fine-tuning paradigms, we introduce Re3-DAPO, a reinforcement learning algorithm that leverages verifiable rewards to directly optimize reaction-level metrics, thereby achieving consistent gains over standard supervised fine-tuning. Additionally, we release the ScannedRxn benchmark, comprising scanned historical reaction diagrams with real-world artifacts, to rigorously assess model robustness and out-of-distribution ability. Our contributions advance the accuracy and generalization of VLM-based reaction diagram parsing. We will release data, models, and code on GitHub.

</details>

---

### 75. [CrossADR: enhancing adverse drug reactions prediction for combination pharmacotherapy with cross-layer feature integration and cross-level associative learning](https://arxiv.org/abs/2603.15047)

**基本信息**

- 🔗 arXiv: [`2603.15047`](https://arxiv.org/abs/2603.15047)
- 👥 作者: Y. Cheung
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15047.pdf)

**💡 相关性分析**

满足标准2：该论文提出了一个用于预测药物组合不良反应的层次化框架CrossADR，并构建了大规模数据集（CrossADR-Dataset）。其方法涉及多尺度特征整合和关联学习，为化学信息学中药物安全性和相互作用预测提供了新的数据资源和计算工具。

**📖 中文摘要**

本文提出CrossADR框架，用于联合药物治疗中器官水平的不良反应（ADR）预测。该框架通过跨层特征整合和跨级关联学习，整合多尺度分子特征，并利用可学习的ADR嵌入空间动态捕捉跨15个器官系统的潜在生物学相关性。系统评估在新构建的CrossADR数据集（涵盖1,376种药物和946,000个独特组合）上进行，表明CrossADR在80个不同的实验场景中 consistently 达到最先进的性能，并提供了对药物相关蛋白质相互作用和通路的高分辨率洞察。总体而言，CrossADR代表了跨尺度生物医学信息整合、跨层特征整合以及跨级关联学习的强大工具，可有效用于临床决策中预防ADR。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Combination pharmacotherapy offers substantial therapeutic advantages but also poses substantial risks of adverse drug reactions (ADRs). The accurate prediction of ADRs with interpretable computational methods is crucial for clinical safety management, drug development, and precision medicine. However, managing ADRs remains a challenge due to the vast search space of drug combinations and the complexity of physiological responses. Current graph-based architectures often struggle to effectively integrate multi-scale biological information and frequently rely on fixed association matrices, which limits their ability to capture dynamic organ-level dependencies and generalize across diverse datasets. Here we propose CrossADR, a hierarchical framework for organ-level ADR prediction through cross-layer feature integration and cross-level associative learning. It incorporates a gated-residual-flow graph neural network to fuse multi-scale molecular features and utilizes a learnable ADR embedding space to dynamically capture latent biological correlations across 15 organ systems. Systematic evaluation on the newly constructed CrossADR-Dataset-covering 1,376 drugs and 946,000 unique combinations-demonstrates that CrossADR consistently achieves state-of-the-art performance across 80 distinct experimental scenarios and provides high-resolution insights into drug-related protein protein interactions and pathways. Overall, CrossADR represents a robust tool for cross-scale biomedical information integration, cross-layer feature integration as well as cross-level associative learning, and can be effectively utilized to prevent ADRs in clinical decision-making.

</details>

---

### 76. [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](https://arxiv.org/abs/2603.15080)

**基本信息**

- 🔗 arXiv: [`2603.15080`](https://arxiv.org/abs/2603.15080)
- 👥 作者: Madhulatha Mandarapu, Sandeep Kunkunuru
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15080.pdf)

**💡 相关性分析**

满足标准2：该论文构建并发布了两个大规模、开放许可的生物医学知识图谱（Pathways KG和Clinical Trials KG），并提供了完整的ETL流程和与AI智能体交互的接口。这些数据集、资源（图谱、代码、协议）可直接用于化学信息学和药物发现相关的研究，支持基于知识的推理和数据挖掘。

**📖 中文摘要**

本文介绍了两个基于高性能图数据库Samyama构建的开源生物医学知识图谱：Pathways KG（整合了Reactome、STRING等5个来源的通路和蛋白质相互作用数据）和Clinical Trials KG（整合了5个来源的临床试验数据）。论文的主要贡献包括：1）描述了一种从异构公共数据源构建大规模知识图谱的可重现ETL模式；2）演示了跨知识图谱的联邦查询能力，例如回答“哪些生物通路被目前处于乳腺癌III期试验的药物所破坏？”这类单一图谱无法回答的问题；3）引入了模式驱动的MCP服务器生成，使每个知识图谱能通过模型上下文协议自动向LLM智能体暴露类型化工具，实现自然语言访问图查询。所有数据源均为开放许可，快照、ETL代码和MCP配置公开可用。该工作为生物医学研究提供了大规模、可连接、可通过AI智能体访问的结构化知识资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, Gene Ontology for functional annotations, this http URL for study registries, and dozens more. Researchers routinely download flat files from each source and write bespoke scripts to cross-reference them, a process that is slow, error-prone, and not reproducible. We present two open-source biomedical knowledge graphs -- Pathways KG (118,686 nodes, 834,785 edges from 5 sources) and Clinical Trials KG (7,774,446 nodes, 26,973,997 edges from 5 sources) -- built on Samyama, a high-performance graph database written in Rust. Our contributions are threefold. First, we describe a reproducible ETL pattern for constructing large-scale KGs from heterogeneous public data sources, with cross-source deduplication, batch Cypher loading, and portable snapshot export. Second, we demonstrate cross-KG federation: loading both snapshots into a single graph tenant enables property-based joins across datasets, answering questions like ``Which biological pathways are disrupted by drugs currently in Phase~3 trials for breast cancer?'' -- a query that neither KG can answer alone. Third, we introduce schema-driven MCP server generation: each KG automatically exposes typed tools for LLM agents via the Model Context Protocol, enabling natural-language access to graph queries without manual tool authoring. All data sources are open-license (CC~BY~4.0, CC0, OBO). Snapshots, ETL code, and MCP configurations are publicly available. The combined federated graph (7.89M nodes, 27.8M edges) loads in 76 seconds on commodity hardware (Mac Mini M4, 16GB RAM), and the signature cross-KG query -- ``which pathways are disrupted by drugs in Phase~3 breast cancer trials?'' -- returns validated results in 2.1 seconds.

</details>

---

### 77. [Gaussian mixture models for model improvement](https://arxiv.org/abs/2603.15101)

**基本信息**

- 🔗 arXiv: [`2603.15101`](https://arxiv.org/abs/2603.15101)
- 👥 作者: Paolo Villani, Daniel Andrés Arcones, Jörg F. Unger 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15101.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于混合模型的模型差异分析和改进框架。虽然应用领域是土木工程，但其核心方法——处理模型与数据不匹配、通过聚类分析指导模型修正——具有通用性。该方法论可被视为一种用于改进预测模型（可能包括化学或质谱预测模型）的工具或分析框架，为相关领域提供了方法学资源。

**📖 中文摘要**

本文提出了一种使用混合模型进行模型差异分析的非侵入式方法，旨在改进复杂物理系统（如土木工程应用）的模型。该方法不是直接修改模型结构，而是将传感器读数映射到具有物理意义的参数簇，自动将传感器读数分配给参数向量簇。这种映射可以揭示系统性的差异和模型偏差，从而指导建模者进行有针对性的、基于物理的改进。该方法在贝叶斯框架内制定，通过期望最大化算法识别参数簇及其分配。该方法通过数值实验进行了演示，包括一个说明性示例和一个关于混凝土桥梁热传递的真实案例研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modeling complex physical systems such as they arise in civil engineering applications requires finding a trade-off between physical fidelity and practicality. Consequently, deviations of simulation from measurements are ubiquitous even after model calibration due to the model discrepancy, which may result from deliberate modeling decisions, ignorance, or lack of this http URL the mismatch between simulation and measurements are deemed unacceptable, the model has to be improved. Targeted model improvement is challenging due to a non-local impact of model discrepancies on measurements and the dependence on sensor configurations. Many approaches to model improvement, such as Bayesian calibration with additive mismatch terms, gray-box models, symbolic regression, or stochastic model updating, often lack interpretability, generalizability, physical consistency, or practical applicability. This paper introduces a non-intrusive approach to model discrepancy analysis using mixture models. Instead of directly modifying the model structure, the method maps sensor readings to clusters of physically meaningful parameters, automatically assigning sensor readings to parameter vector clusters. This mapping can reveal systematic discrepancies and model biases, guiding targeted, physics-based refinements by the modeler. The approach is formulated within a Bayesian framework, enabling the identification of parameter clusters and their assignments via the Expectation-Maximization (EM) algorithm. The methodology is demonstrated through numerical experiments, including an illustrative example and a real-world case study of heat transfer in a concrete bridge.

</details>

---

### 78. [Data Augmentation via Causal-Residual Bootstrapping](https://arxiv.org/abs/2603.15335)

**基本信息**

- 🔗 arXiv: [`2603.15335`](https://arxiv.org/abs/2603.15335)
- 👥 作者: Mateusz Gajewski, Sophia Xiao, Bijan Mazaheri
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15335.pdf)

**💡 相关性分析**

满足标准1：论文提出的因果残差自助法是一种整合领域知识（因果结构）的数据增强框架，其核心思想可直接应用于化学信息学领域，用于构建和增强训练化学大模型（如预测分子性质或反应路径）所需的数据，因此与‘化学大模型’主题直接相关。

**📖 中文摘要**

本文提出了一种通过因果残差自助法进行数据增强的方法。该方法建立在独立机制原理之上，通过对基于边际概率分布构建的模型的残差进行置换来整合因果知识。虽然论文主要关注通用数据增强和因果知识整合，但其核心思想——利用因果结构（例如，A导致B导致C）来生成或增强数据——与化学信息学中构建和验证化学大模型（特别是用于预测分子性质或反应）高度相关。该方法提供了一种将领域知识（如化学反应路径）注入机器学习模型的框架，这对于训练更可靠、可解释的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Data augmentation integrates domain knowledge into a dataset by making domain-informed modifications to existing data points. For example, image data can be augmented by duplicating images in different tints or orientations, thereby incorporating the knowledge that images may vary in these dimensions. Recent work by Teshima and Sugiyama has explored the integration of causal knowledge (e.g, A causes B causes C) up to conditional independence equivalence. We suggest a related approach for settings with additive noise that can incorporate information beyond a Markov equivalence class. The approach, built on the principle of independent mechanisms, permutes the residuals of models built on marginal probability distributions. Predictive models built on our augmented data demonstrate improved accuracy, for which we provide theoretical backing in linear Gaussian settings.

</details>

---

### 79. [Matched Filter-Based Molecule Source Localization in Advection-Diffusion-Driven Pipe Networks with Known Topology](https://arxiv.org/abs/2603.15394)

**基本信息**

- 🔗 arXiv: [`2603.15394`](https://arxiv.org/abs/2603.15394)
- 👥 作者: Timo Jakumeit, Bastian Heinlein, Vukašin Spasojević 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15394.pdf)

**💡 相关性分析**

满足标准1：论文研究在已知拓扑的管道网络中定位分子源，其核心是利用传感器信号和物理模型（平流-扩散）进行逆向推理。这与‘质谱结构推理’主题在方法论上高度相关，因为质谱分析的本质也是从复杂的谱图信号逆向推断分子的结构或来源，两者都涉及基于物理/化学模型的逆问题求解。

**📖 中文摘要**

本文提出了一种在已知拓扑结构的管道网络（如心血管系统、污水网络）中定位分子源的方法框架。该框架利用混合逆高斯血流输运模型作为管道网络中平流-扩散驱动分子通信的闭式表示，并提出了基于匹配滤波的方法来识别分子源。论文的核心是解决合成分子通信中的一个应用问题，即通过传感器信号推断分子释放源的位置。这项工作虽然侧重于通信和定位，但其底层模型（平流-扩散）和从混合信号中推理源位置的问题，与质谱分析中从复杂的质谱信号推断分子结构或来源（如代谢组学中的生物标志物发现）在数学和概念上具有高度的相似性。论文提出的算法为解决质谱结构推理中的类似逆问题（从观测数据反推源头或结构）提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Synthetic molecular communication (MC) has emerged as a powerful framework for modeling, analyzing, and designing communication systems where information is encoded into properties of molecules. Among the envisioned applications of MC is the localization of molecule sources in pipe networks (PNs) like the human cardiovascular system (CVS), sewage networks (SNs), and industrial plants. While existing algorithms mostly focus on simplified scenarios, in this paper, we propose the first framework for source localization in complex PNs with known topology, by leveraging the mixture of inverse Gaussians for hemodynamic transport (MIGHT) model as a closed-form representation for advection-diffusion-driven MC in PNs. We propose a matched filter (MF)-based approach to identify molecule sources under realistic conditions such as unknown release times, random numbers of released molecules, sensor noise, and limited sensor sampling rate. We apply the algorithm to localize a source of viral markers in a real-world SN and show that the proposed scheme outperforms randomly guessing sources even at low signal-to-noise ratios (SNRs) at the sensor and achieves error-free localization under favorable conditions, i.e., high SNRs and sampling rates. Furthermore, by identifying clusters of frequently confused sources, reliable cluster-level localization is possible at substantially lower SNRs and sampling rates.

</details>

---

### 80. [TabKD: Tabular Knowledge Distillation through Interaction Diversity of Learned Feature Bins](https://arxiv.org/abs/2603.15481)

**基本信息**

- 🔗 arXiv: [`2603.15481`](https://arxiv.org/abs/2603.15481)
- 👥 作者: Shovon Niverd Pereira, Krishna Khadka, Yu Lei
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15481.pdf)

**💡 相关性分析**

满足标准1：论文专注于表格模型的知识蒸馏，并强调对特征交互的系统性覆盖。这一核心思想与化学信息学中构建化学大模型的关键挑战——准确建模原子和子结构之间的复杂相互作用——直接相关。该方法为生成用于训练或增强化学大模型的合成数据，以及压缩复杂的化学模型提供了新颖的技术路径。

**📖 中文摘要**

本文提出了TabKD，一种面向表格数据的无数据知识蒸馏方法。该方法的核心见解是，有效的表格模型蒸馏需要明确处理特征交互（即特征组合的编码方式）。TabKD通过学习与教师模型决策边界对齐的自适应特征分箱，并生成能最大化成对交互覆盖的合成查询数据。论文在多个基准数据集和教师架构上验证了其有效性。这项工作虽然针对通用的表格数据，但其对特征交互的系统性覆盖和探索，对于化学信息学领域至关重要。在化学中，分子的性质往往由原子和键的复杂组合（高阶交互）决定。因此，TabKD中提出的交互多样性最大化和基于分箱的特征表示方法，为构建更能捕捉分子复杂结构的化学大模型（尤其是基于表格或描述符的模型）提供了重要的数据生成和模型压缩思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Data-free knowledge distillation enables model compression without original training data, critical for privacy-sensitive tabular domains. However, existing methods does not perform well on tabular data because they do not explicitly address feature interactions, the fundamental way tabular models encode predictive knowledge. We identify interaction diversity, systematic coverage of feature combinations, as an essential requirement for effective tabular distillation. To operationalize this insight, we propose TabKD, which learns adaptive feature bins aligned with teacher decision boundaries, then generates synthetic queries that maximize pairwise interaction coverage. Across 4 benchmark datasets and 4 teacher architectures, TabKD achieves highest student-teacher agreement in 14 out of 16 configurations, outperforming 5 state-of-the-art baselines. We further show that interaction coverage strongly correlates with distillation quality, validating our core hypothesis. Our work establishes interaction-focused exploration as a principled framework for tabular model extraction.

</details>

---

### 81. [Not All Invariants Are Equal: Curating Training Data to Accelerate Program Verification with SLMs](https://arxiv.org/abs/2603.15510)

**基本信息**

- 🔗 arXiv: [`2603.15510`](https://arxiv.org/abs/2603.15510)
- 👥 作者: Ido Pinto, Yizhak Yisrael Elboher, Haoze Wu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15510.pdf)

**💡 相关性分析**

满足标准2和标准1：论文提出了一套系统化的高质量训练数据策展流程，用于提升模型在复杂推理任务（程序不变式生成）上的性能。这套方法论（数据清洗、语义重写、质量保证）可作为构建用于‘化学大模型’和‘质谱结构推理’的专用数据集的宝贵资源（标准2）。同时，其解决的‘从规则/数据中推理出隐藏结构/约束’问题，与化学信息学中的核心推理任务在本质上高度相关（标准1）。

**📖 中文摘要**

本文关注程序验证中的关键瓶颈——归纳循环不变式的自动合成。针对大型语言模型在此任务上的局限性，论文提出了一个严格的数据处理流程（Wonda），用于从验证器生成的原始不变式中提取高质量的训练数据。该流程通过AST标准化和LLM驱动的语义重写来精炼噪声数据，并附有可证明的质量保证。研究表明，在此精选数据集上对小型语言模型进行微调，能使其性能大幅提升，在具有挑战性的不变式生成任务上达到甚至超过大型模型的效果。这项工作虽然处于程序验证领域，但其核心贡献——通过精心策划的训练数据来显著提升模型在复杂推理任务（不变式生成）上的能力——为化学信息学和质谱分析提供了重要启示。例如，训练模型从质谱数据中推理分子结构或从化学反应规则中预测产物，同样是复杂的符号推理任务。本文的数据策展和模型微调方法论可直接迁移，用于构建和优化专门用于‘质谱结构推理’或‘化学反应预测’的领域大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The synthesis of inductive loop invariants is a critical bottleneck in automated program verification. While Large Language Models (LLMs) show promise in mitigating this issue, they often fail on hard instances, generating invariants that are invalid or computationally ineffective. While fine-tuning is a natural route to mitigate this limitation, obtaining high-quality training data for invariant generation remains an open challenge. We present a rigorous data curation pipeline designed to extract high-quality training signals from raw verifier-generated invariants. First, we formalize the properties required for a high-quality training invariant. Second, we propose Wonda, a pipeline that refines noisy data via AST-based normalization, followed by LLM-driven semantic rewriting and augmentation with provable quality guarantees. We demonstrate that fine-tuning Small Language Models (SLMs) on this curated dataset result in consistent and significant performance gain. In particular, a fine-tuned 4B parameter model matches the utility of a GPT-OSS-120B baseline and approaches the state-of-the-art GPT-5.2, without incurring reasoning-time overhead. On challenging instances from the recent InvBench evaluation suite, our approach doubles the invariant correctness and speedup rates of base models; and improves their Virtual Best Performance (VBP) rates on the verification task by up to 14.2%.

</details>

---

### 82. [PolyMon: A Unified Framework for Polymer Property Prediction](https://arxiv.org/abs/2603.13303)

**基本信息**

- 🔗 arXiv: [`2603.13303`](https://arxiv.org/abs/2603.13303)
- 👥 作者: Gaopeng Ren, Yijie Yang, Jiajun Zhou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13303.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于聚合物性质预测的统一机器学习框架（PolyMon），这直接属于化学信息学领域，并与构建用于材料发现的化学大模型/机器学习模型这一主题高度相关。

**📖 中文摘要**

本文提出了PolyMon，一个用于聚合物性质预测的统一机器学习框架。该框架整合了多种聚合物表示方法（如描述符和图结构）、多种机器学习模型（从表格模型到图神经网络）以及灵活的训练策略（如多保真度学习、Δ-学习、主动学习和集成学习）。通过五个关键聚合物性质的基准测试，作者系统评估了不同表示和模型对预测性能的影响。该工作为化学信息学领域提供了一个全面的、可扩展的基准测试和模型开发平台，其核心是开发用于材料设计的机器学习模型，这与“化学大模型”的主题高度相关，因为PolyMon本身就是一个用于聚合物性质预测的集成化、可扩展的机器学习模型框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of polymer properties is essential for materials design, but remains challenging due to data scarcity, diverse polymer representations, and the lack of systematic evaluation across modelling choices. Here, we present PolyMon, a unified and accessible framework that integrates multiple polymer representations, machine learning methods, and training strategies within a single, accessible platform. PolyMon supports various descriptors and graph construction strategies for polymer representations, and includes a wide range of models, from tabular models to graph neural networks, along with flexible training strategies including multi-fidelity learning, {\Delta}-learning, active learning, and ensemble learning. Using five key polymer properties as benchmarks, we perform systematic evaluations to assess how representations and models affect predictive performance. These case studies further illustrate how different training strategies can be applied within a consistent workflow to leverage limited data and incorporate physical model derived information. Overall, PolyMon provides a comprehensive and extensible foundation for benchmarking and advancing machine learning-based polymer property prediction. The code is available at this http URL .

</details>

---

### 83. [Diffusion-based Generative Machine Learning Model for Predicting Crack Propagation in Aluminum Nitride at the Atomic Scale](https://arxiv.org/abs/2603.13445)

**基本信息**

- 🔗 arXiv: [`2603.13445`](https://arxiv.org/abs/2603.13445)
- 👥 作者: Jiali Lu, Shengfeng Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13445.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于预测材料（氮化铝）原子尺度行为的生成式机器学习模型（扩散模型）。这属于化学信息学和材料信息学中利用AI大模型解决复杂科学问题的研究主题。

**📖 中文摘要**

本文开发了一种基于扩散的生成式机器学习模型，用于预测氮化铝（AlN）在原子尺度上的裂纹扩展。该模型仅以初始微观结构嵌入为条件，经过分子动力学模拟训练后，能够显著加速预测过程，同时准确预测动态断裂过程，包括应力驱动的裂纹萌生、裂纹分支和原子尺度的桥接韧带。该模型展示了固有的物理保真度，能够重现材料内在的断裂机制，并且可以推广到未见的多裂纹构型。这项工作展示了生成式模型（扩散模型）在模拟复杂材料物理过程（如断裂）中的应用，是机器学习与计算材料科学交叉的范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting atomic-scale crack propagation in aluminum nitride (AlN) is critical for semiconductor reliability but remains prohibitively expensive via molecular dynamics (MD). We develop a diffusion-based generative machine learning model to predict atomic-scale crack propagation in AlN, a critical semiconductor material, by conditioning solely on initial microstructure embeddings. Trained on MD simulations of single-crack systems, the model achieves a significant speedup while accurately forecasting dynamic fracture processes, including stress-driven crack initiation, crack branching, and atomic-scale bridging ligaments. Crucially, it demonstrates inherent physical fidelity by reproducing material-intrinsic mechanisms while disregarding periodic boundary artifacts, and generalizes to unseen multi-crack configurations. Validation against MD ground truth confirms the capability of the model to capture complex fracture physics without auxiliary stress or energy data, enabling rapid exploration of crack-mediated failure for semiconductor reliability optimization.

</details>

---

### 84. [EmDT: Embedding Diffusion Transformer for Tabular Data Generation in Fraud Detection](https://arxiv.org/abs/2603.13566)

**基本信息**

- 🔗 arXiv: [`2603.13566`](https://arxiv.org/abs/2603.13566)
- 👥 作者: En-Ya Kuo, Sebastien Motsch
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13566.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于表格数据生成的扩散-Transformer混合模型（EmDT）。虽然应用场景是欺诈检测，但其核心模型属于生成式AI大模型在结构化数据上的应用，与机器学习大模型的主题相关。

**📖 中文摘要**

本文提出了Clustered Embedding Diffusion-Transformer (EmDT)，一种为欺诈检测中不平衡表格数据生成欺诈样本的扩散模型。该模型的关键创新在于利用UMAP聚类识别不同的欺诈模式，并训练一个带有正弦位置嵌入的Transformer去噪网络，以在整个扩散过程中捕获特征关系。生成合成数据后，使用标准的基于决策树的分类器进行分类。在信用卡欺诈检测数据集上的实验表明，EmDT显著提高了下游分类性能。这项工作将扩散模型和Transformer架构应用于表格数据生成，是生成式AI在特定领域（金融风控）的应用，其模型架构属于“大模型”范畴的一种应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Imbalanced datasets pose a difficulty in fraud detection, as classifiers are often biased toward the majority class and perform poorly on rare fraudulent transactions. Synthetic data generation is therefore commonly used to mitigate this problem. In this work, we propose the Clustered Embedding Diffusion-Transformer (EmDT), a diffusion model designed to generate fraudulent samples. Our key innovation is to leverage UMAP clustering to identify distinct fraudulent patterns, and train a Transformer denoising network with sinusoidal positional embeddings to capture feature relationships throughout the diffusion process. Once the synthetic data has been generated, we employ a standard decision-tree-based classifier (e.g., XGBoost) for classification, as this type of model remains better suited to tabular datasets. Experiments on a credit card fraud detection dataset demonstrate that EmDT significantly improves downstream classification performance compared to existing oversampling and generative methods, while maintaining comparable privacy protection and preserving feature correlations present in the original data.

</details>

---

### 85. [Research Paradigm of Materials Science Tetrahedra with Artificial Intelligence](https://arxiv.org/abs/2603.13744)

**基本信息**

- 🔗 arXiv: [`2603.13744`](https://arxiv.org/abs/2603.13744)
- 👥 作者: Shiyun Zhang, Yibo Yao, Haoquan Long 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13744.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于AI（包括大模型和机器学习）如何变革材料科学研究范式的综述和展望性文章。它专门讨论了AI与材料科学（化学信息学的核心应用领域）的整合，提出了新的研究范式，因此与“化学大模型”主题高度相关。

**📖 中文摘要**

本文探讨了人工智能（AI）如何与材料科学研究范式（经典的材料四面体：结构-性质-加工-性能-表征）相结合。作者提出了两个新的研究范式：一个专注于“AI for materials science”，涉及物质-数据-模型-潜力-代理的图表；另一个展示了“AI research”，讨论数据-架构-编码-优化-推理的关系。文章讨论了这些框架的关键要素及其联系，旨在激发科学思维的完善和技术的进步。这项工作从宏观范式层面，系统地阐述了如何将AI（包括大模型和机器学习）整合到材料科学发现流程中，为AI驱动的材料研究提供了理论框架和思考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The classical material tetrahedron that represents the Structure-Property-Processing-Performance-Characterization relationship is the most important research paradigm in materials science so far. It has served as a protocol to guide experiments, modeling, and theory to uncover hidden relationships between various aspects of a certain material. This substantially facilitates knowledge accumulation and material discovery with desired functionalities to realize versatile applications. In recent years, with the advent of artificial intelligence (AI) techniques, the attention of AI towards scientific research is soaring. The trials of implementing AI in various disciplines are endless, with great potential to revolutionize the research diagram. Despite the success in natural language processing and computer vision, how to effectively integrate AI with natural science is still a grand challenge, bearing in mind their fundamental differences. Inspired by these observations and limitations, we delve into the current research paradigm dictated by the classical material tetrahedron and propose two new paradigms to stimulate data-driven and AI-augmented research. One tetrahedron focuses on AI for materials science by considering the Matter-Data-Model-Potential-Agent diagram. The other demonstrates AI research by discussing Data-Architecture-Encoding-Optimization-Inference relationships. The crucial ingredients of these frameworks and their connections are discussed, which will likely motivate both scientific thinking refinement and technology advancement. Despite the widespread enthusiasm for chasing AI for science, we must analyze issues rationally to come up with well-defined, resolvable scientific problems in order to better master the power of AI.

</details>

---

### 86. [Generative Inverse Design of Cold Metals for Low-Power Electronics](https://arxiv.org/abs/2603.13920)

**基本信息**

- 🔗 arXiv: [`2603.13920`](https://arxiv.org/abs/2603.13920)
- 👥 作者: Kedeng Wu, Yucheng Zhu, Yan Chen 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.13920.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成式Transformer模型（MatterGPT）进行新材料的逆向设计。这直接属于化学信息学中“AI for science”和“生成式化学大模型”的研究范畴。

**📖 中文摘要**

本文提出了一种用于发现新型“冷金属”材料的生成式逆向设计工作流。冷金属因其在低功耗电子器件中的应用前景而备受关注。作者使用MatterGPT（一种基于可逆且对称不变的晶体字符串表示SLICES训练的条件自回归Transformer模型）来生成三维冷金属晶体结构。该工作流针对热力学稳定性和特定的能带边缘距离（50-500 meV）进行条件生成，产生了大量候选结构，并通过高通量DFT验证，最终从Materials Project数据库之外发现了257种新型冷金属。这项工作展示了生成式AI模型（特别是基于Transformer的大语言模型架构）在发现具有目标功能的新材料方面的强大能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cold metals are a class of metals with an intrinsic energy gap located close to the Fermi level, which enables cold-carrier injection for steep-slope transistors and is therefore promising for low-power electronic applications. High-throughput screening has revealed 252 three-dimensional (3D) cold metals in the Materials Project database, but database searches are inherently limited to known compounds. Here we present an inverse-design workflow that generates 3D cold metals using MatterGPT, a conditional autoregressive Transformer trained on SLICES, an invertible and symmetry-invariant crystal string representation. We curate a training set of 26,309 metallic structures labeled with energy above hull and a unified band-edge distance descriptor that merges p-type and n-type cold-metal characteristics to address severe label imbalance. Property-conditioned generation targeting thermodynamic stability and 50-500 meV band-edge distances produces 148,506 unique candidates; 92.1% are successfully reconstructed to 3D structures and down-selected by symmetry, uniqueness and novelty filters, followed by high-throughput DFT validation. We identify 257 cold metals verified as novel with respect to the Materials Project database, with gaps around the Fermi level spanning 50-500 meV. First-principles phonon, electronic-structure, and work-function calculations for representative candidates confirm dynamical stability and contact-relevant work functions. Our results demonstrate that SLICES-enabled generative transformers can expand the chemical space of cold metals beyond high-throughput screening, providing a route to low-power electronic materials discovery.

</details>

---

### 87. [Distributional Uncertainty and Adaptive Decision-Making in System](https://arxiv.org/abs/2603.14047)

**基本信息**

- 🔗 arXiv: [`2603.14047`](https://arxiv.org/abs/2603.14047)
- 👥 作者: Yujun Huang, Gioele Zardini
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14047.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从理论层面剖析大型语言模型（作为“化学大模型”的一种范式）的行为生成与决策机制，并探讨其与社会规范、理性之间的关系，这对于设计和理解化学领域大模型的行为基础至关重要。

**📖 中文摘要**

本文提出了一个“社会优先”的规范性适当性理论，该理论将个体建模为类似于大型语言模型（LLMs）的预训练行动者。论文的核心观点是，个体的行为是通过基于上下文的预测性模式补全来生成的，即回答“像我这样的人在这种情况下会做什么？”这样的问题。这一理论旨在解释人类规范的关键特征，如上下文依赖性、任意性和自动性，并对理性选择理论提出了挑战。该研究从认知架构和社会科学的角度，深入探讨了LLMs作为行为生成模型的隐喻及其对社会规范建模的启示。虽然不直接涉及化学或质谱，但它从理论层面深入剖析了“大模型”的行为生成与决策机制，这对于理解如何构建和约束面向科学发现的化学大模型（例如，使其遵循化学规则或实验规范）具有重要的基础理论价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Complex engineered systems require coordinated design choices across heterogeneous components under multiple conflicting objectives and uncertain specifications. Monotone co-design provides a compositional framework for such problems by modeling each subsystem as a design problem: a feasible relation between provided functionalities and required resources in partially ordered sets. Existing uncertain co-design models rely on interval bounds, which support worst-case reasoning but cannot represent probabilistic risk or multi-stage adaptive decisions. We develop a distributional extension of co-design that models uncertain design outcomes as distributions over design problems and supports adaptive decision processes through Markov-kernel re-parameterizations. Using quasi-measurable and quasi-universal spaces, we show that the standard co-design interconnection operations remain compositional under this richer notion of uncertainty. We further introduce queries and observations that extract probabilistic design trade-offs, including feasibility probabilities, confidence bounds, and distributions of minimal required resources. A task-driven unmanned aerial vehicle case study illustrates how the framework captures risk-sensitive and information-dependent design choices that interval-based models cannot express.

</details>

---

### 88. [Reversible Lifetime Semantics for Quantum Programs](https://arxiv.org/abs/2603.14538)

**基本信息**

- 🔗 arXiv: [`2603.14538`](https://arxiv.org/abs/2603.14538)
- 👥 作者: Simone Faro, Francesco Pio Marino, Gabriele Messina
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14538.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于高能物理现象学研究的语言驱动智能体系统。这直接围绕“化学大模型”主题的扩展理解（即科学领域的大模型/智能体），因为它构建了一个能够理解物理符号和自然语言、自主执行复杂科学工作流的AI系统，是科学大模型/智能体在物理领域的具体应用。

**📖 中文摘要**

这篇论文提出了一个用于对撞机物理及其他领域的端到端语言驱动智能体系统（ColliderAgent）。该系统在一个解耦的、领域无关的架构中实例化，能够仅根据自然语言提示（辅以标准物理符号）执行从理论拉格朗日量到最终现象学输出的完整工作流，而不依赖于特定软件包的代码。该框架将一个分层的多智能体推理层与一个用于现象学计算和模拟工具链的统一执行后端（Magnus）耦合。作者在涵盖轻夸克和轴子样粒子场景、高维有效算子、部分子水平和探测器水平分析以及导致排除极限的大规模参数扫描的代表性文献复现上验证了该系统。这项工作为在对撞机物理、宇宙学及更广泛的物理学中实现更自动化、可扩展和可重复的研究指明了道路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reversible computation requires that intermediate data be explicitly undone rather than discarded. In quantum programming, this principle appears as uncomputation, usually treated as a technical cleanup mechanism. We instead present uncomputation as a semantic foundation. In the Qutes language, we introduce a formal model of \emph{Scope-Bounded Liveness-Guided Uncomputation}, where lexical scope bounds variable lifetime and static liveness and entanglement analysis determine the earliest safe reclamation point. We define semantic lifetime and a Restoration Invariant ensuring that temporary quantum information disappears once it becomes semantically irrelevant. We prove compositional correctness under nested scopes and show that early reclamation can reduce circuit depth by avoiding critical-path overhead and can bound peak live qubits through disciplined ancilla reuse. Finally, we show that parameter passing semantics emerges from the same lifetime discipline, with pass-by-value and pass-by-reference corresponding to different lifetime boundaries, and we characterize the constraints (irreversibility, persistent entanglement, and aliasing) under which automatic uncomputation must be restricted.

</details>

---

### 89. [Scaling Autoregressive Models for Lattice Thermodynamics](https://arxiv.org/abs/2603.14695)

**基本信息**

- 🔗 arXiv: [`2603.14695`](https://arxiv.org/abs/2603.14695)
- 👥 作者: Xiaochen Du, Juno Nam, Sulin Liu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14695.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于晶格热力学建模的自回归生成模型框架。这直接围绕“化学大模型”主题，因为它提出了用于材料科学中原子构型分布建模的新型生成式模型（自回归模型和Transformer），属于化学领域专用生成模型的前沿工作。

**📖 中文摘要**

这篇论文开发了一个结合任意顺序自回归模型（ARMs）和边缘化模型（MAMs）的框架，用于预测晶体晶格上原子构型的统计分布（晶格热力学）。传统自回归模型按固定顺序生成构型，内存和训练成本高。新框架允许模型通过以任何已知的晶格点子集为条件来灵活生成构型，而MAMs可以在单次前向传递中近似任何部分构型的概率，从而大幅降低内存需求。这种组合使得在较小晶格上训练的模型可以重复用于对更大系统进行采样，同时支持具有晶格感知位置编码的表达性Transformer架构，且计算成本可控。作者在二维Ising模型和CuAu合金上证明，基于Transformer的任意顺序MAMs比基于多层感知机的ARMs实现了更精确的自由能计算，忠实地捕捉了相变和临界行为。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting how materials behave under realistic conditions requires understanding the statistical distribution of atomic configurations on crystal lattices, a problem central to alloy design, catalysis, and the study of phase transitions. Traditional Markov-chain Monte Carlo sampling suffers from slow convergence and critical slowing down near phase transitions, motivating the use of generative models that directly learn the thermodynamic distribution. Existing autoregressive models (ARMs), however, generate configurations in a fixed sequential order and incur high memory and training costs, limiting their applicability to realistic systems. Here, we develop a framework combining any-order ARMs, which generate configurations flexibly by conditioning on any known subset of lattice sites, with marginalization models (MAMs), which approximate the probability of any partial configuration in a single forward pass and substantially reduce memory requirements. This combination enables models trained on smaller lattices to be reused for sampling larger systems, while supporting expressive Transformer architectures with lattice-aware positional encodings at manageable computational cost. We demonstrate that Transformer-based any-order MAMs achieve more accurate free energies than multilayer perceptron-based ARMs on both the two-dimensional Ising model and CuAu alloys, faithfully capturing phase transitions and critical behavior. Overall, our framework scales from $10 \times 10$ to $20 \times 20$ Ising systems and from $2 \times 2 \times 4$ to $4 \times 4 \times 8$ CuAu supercells at reduced computational cost compared to conventional sampling methods.

</details>

---

### 90. [Design Space of Self--Consistent Electrostatic Machine Learning Interatomic Potentials](https://arxiv.org/abs/2603.14700)

**基本信息**

- 🔗 arXiv: [`2603.14700`](https://arxiv.org/abs/2603.14700)
- 👥 作者: William J. Baldwin, Ilyes Batatia, Martin Vondrák 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14700.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习原子间势（MLIPs）中静电效应的建模框架和设计空间探索。这直接围绕“化学大模型”主题，因为MLIPs是用于原子尺度模拟的基础化学模型，而论文专注于提升这类模型在复杂静电相互作用方面的能力，属于化学领域专用大模型的前沿研究。

**📖 中文摘要**

这篇论文系统地研究了机器学习原子间势（MLIPs）中结合静电效应的设计空间。作者提出了一个将现有模型视为密度泛函理论（DFT）粗粒度近似的框架，从而明确了所涉及的近似，阐明了学习量的物理意义，并揭示了先前提出的几种模型之间的联系和等价性。利用这一形式化方法，作者识别了定义自洽静电MLIPs更广泛设计空间的关键设计选择。他们在MACE架构中实现了该空间中的突出点，并使用共享的电荷密度表示，从而能够对不同方法进行受控比较。最后，他们在两个指导性测试案例上评估了这些模型：金属-水界面（探测导体和绝缘体系统的对比静电响应）和二氧化硅中的带电空位。这项工作为理解和开发能够处理长程静电、电荷转移或诱导极化的下一代MLIPs提供了重要见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning interatomic potentials (MLIPs) have become widely used tools in atomistic simulations. For much of the history of this field, the most commonly employed architectures were based on short-ranged atomic energy contributions, and the assumption of locality still persists in many modern foundation models. While this approach has enabled efficient and accurate modelling for many use cases, it poses intrinsic limitations for systems where long-range electrostatics, charge transfer, or induced polarization play a central role. A growing body of work has proposed extensions that incorporate electrostatic effects, ranging from locally predicted atomic charges to self-consistent models. While these models have demonstrated success for specific examples, their underlying assumptions, and fundamental limitations are not yet well understood. In this work, we present a framework for treating electrostatics in MLIPs by viewing existing models as coarse-grained approximations to density functional theory (DFT). This perspective makes explicit the approximations involved, clarifies the physical meaning of the learned quantities, and reveals connections and equivalences between several previously proposed models. Using this formalism, we identify key design choices that define a broader design space of self-consistent electrostatic MLIPs. We implement salient points in this space using the MACE architecture and a shared representation of the charge density, enabling controlled comparisons between different approaches. Finally, we evaluate these models on two instructive test cases: metal-water interfaces, which probe the contrasting electrostatic response of conducting and insulating systems, and charged vacancies in silicon dioxide. Our results highlight the limitations of existing approaches and demonstrate how more expressive self-consistent models are needed to resolve failures.

</details>

---

### 91. [Fold-CP: A Context Parallelism Framework for Biomolecular Modeling](https://arxiv.org/abs/2603.14806)

**基本信息**

- 🔗 arXiv: [`2603.14806`](https://arxiv.org/abs/2603.14806)
- 👥 作者: Dejun Lin, Simon Chu, Vishanth Iyer 等38人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于大规模生物分子结构预测的并行计算框架，以扩展像AlphaFold这样的基础模型的能力。这直接围绕“化学大模型”主题，因为AlphaFold是结构生物学领域的革命性大模型，而本工作旨在突破其计算瓶颈，属于支撑化学/生物大模型应用的关键技术。

**📖 中文摘要**

这篇论文介绍了NVIDIA BioNeMo Fold-CP，一个用于生物分子建模的上下文并行框架。该框架旨在克服像AlphaFold 3这样的模型在单个GPU上处理残基数（通常限于几千个）的硬件内存限制。Fold-CP通过将共折叠模型的推理和训练管道分布在多个GPU上，实现了高效的内存扩展；对于一个分布在P个GPU上的N个令牌输入，每个设备的内存按O(N^2/P)缩放，从而能够在64个NVIDIA B300 GPU上预测超过30,000个残基的组装体结构。作者展示了该方法在成功开发人员用例中的科学效用：Fold-CP能够对哺乳动物蛋白质复合物综合资源（CORUM）数据库中超过90%的复合物进行评分，以及折叠与内在无序区域结合的疾病相关PI4KA脂质激酶复合物而无需裁剪。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding cellular machinery requires atomic-scale reconstruction of large biomolecular assemblies. However, predicting the structures of these systems has been constrained by hardware memory requirements of models like AlphaFold 3, imposing a practical ceiling of a few thousand residues that can be processed on a single GPU. Here we present NVIDIA BioNeMo Fold-CP, a context parallelism framework that overcomes this barrier by distributing the inference and training pipelines of co-folding models across multiple GPUs. We use the Boltz models as open source reference architectures and implement custom multidimensional primitives that efficiently parallelize both the dense triangular updates and the irregular, data-dependent pattern of window-batched local attention. Our approach achieves efficient memory scaling; for an N-token input distributed across P GPUs, per-device memory scales as $O(N^2/P)$, enabling the structure prediction of assemblies exceeding 30,000 residues on 64 NVIDIA B300 GPUs. We demonstrate the scientific utility of this approach through successful developer use cases: Fold-CP enabled the scoring of over 90% of Comprehensive Resource of Mammalian protein complexes (CORUM) database, as well as folding of disease-relevant PI4KA lipid kinase complex bound to an intrinsically disordered region without cropping. By providing a scalable pathway for modeling massive systems with full global context, Fold-CP represents a significant step toward the realization of a virtual cell.

</details>

---

### 92. [Empowering Chemical Structures with Biological Insights for Scalable Phenotypic Virtual Screening](https://arxiv.org/abs/2603.15006)

**基本信息**

- 🔗 arXiv: [`2603.15006`](https://arxiv.org/abs/2603.15006)
- 👥 作者: Xiaoqing Lian, Pengsen Ma, Tengfeng Ma 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15006.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个名为DECODE的深度学习框架，该框架旨在从化学结构中提取具有生物语义的表示，以进行虚拟筛选和生物分析。这直接围绕“化学大模型”这一主题，因为它构建了一个用于化学-生物关系建模的专用模型。

**📖 中文摘要**

这篇论文提出了DECODE框架，旨在解决药物发现中可扩展的生物活性化合物识别问题。该框架的核心是通过将有限的配对转录组学和形态学数据作为监督信号，从化学结构中提取测量不变的生物指纹，并显式过滤实验噪声。DECODE通过训练一个模型，使化学表示能够内在地编码生物语义，从而在不需要推理时使用生物数据的情况下，实现基于结构的体外生物分析。该方法在零样本设置下检索功能相似的药物方面，相对于化学基线有超过20%的相对改进，并在外部验证中实现了新型抗癌药物命中率6倍的提升。这项工作直接关联化学信息学中的化学大模型主题，因为它开发了一个从化学结构预测生物活性的深度学习框架，本质上是一个用于化学-生物关系建模的专用大模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Motivation: The scalable identification of bioactive compounds is essential for contemporary drug discovery. This process faces a key trade-off: structural screening offers scalability but lacks biological context, whereas high-content phenotypic profiling provides deep biological insights but is resource-intensive. The primary challenge is to extract robust biological signals from noisy data and encode them into representations that do not require biological data at inference. Results: This study presents DECODE (DEcomposing Cellular Observations of Drug Effects), a framework that bridges this gap by empowering chemical representations with intrinsic biological semantics to enable structure-based in silico biological profiling. DECODE leverages limited paired transcriptomic and morphological data as supervisory signals during training, enabling the extraction of a measurement-invariant biological fingerprint from chemical structures and explicit filtering of experimental noise. Our evaluations demonstrate that DECODE retrieves functionally similar drugs in zero-shot settings with over 20% relative improvement over chemical baselines in mechanism-of-action (MOA) prediction. Furthermore, the framework achieves a 6-fold increase in hit rates for novel anti-cancer agents during external validation. Availability and implementation: The codes and datasets of DECODE are available at this https URL .

</details>

---

### 93. [Agentic workflow enables the recovery of critical materials from complex feedstocks via selective precipitation](https://arxiv.org/abs/2603.15491)

**基本信息**

- 🔗 arXiv: [`2603.15491`](https://arxiv.org/abs/2603.15491)
- 👥 作者: Andrew Ritchhart, Sarah I. Allec, Pravalika Butreddy 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15491.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于关键材料回收的AI驱动多智能体工作流程。这直接围绕“化学大模型”这一主题，因为它涉及在化学实验和过程优化中部署和协调多个AI智能体（可视为一种特定领域的模型化、自动化系统）。

**📖 中文摘要**

这篇论文提出了一个用于关键材料回收的多智能体工作流程。该流程部署了一系列AI智能体和自动化仪器，从采出水和磁体浸出液中回收关键材料。该方法使用简单的化学品实现了从真实世界原料中选择性沉淀，将高效、适应性强的分离工艺开发时间从数月或数年加速到数天。这项工作展示了AI驱动的自动化工作流程在解决复杂化学分离问题中的应用，是化学信息学和自动化实验交叉领域的前沿研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a multi-agentic workflow for critical materials recovery that deploys a series of AI agents and automated instruments to recover critical materials from produced water and magnet leachates. This approach achieves selective precipitation from real-world feedstocks using simple chemicals, accelerating the development of efficient, adaptable, and scalable separations to a timeline of days, rather than months and years.

</details>

---

### 94. [Benchmarking Machine Learning Approaches for Polarization Mapping in Ferroelectrics Using 4D-STEM](https://arxiv.org/abs/2603.15582)

**基本信息**

- 🔗 arXiv: [`2603.15582`](https://arxiv.org/abs/2603.15582)
- 👥 作者: Matej Martinc, Goran Dražič, Anton Kokalj 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15582.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和开发机器学习方法，用于从4D-STEM数据（一种重要的材料表征技术）中自动推断材料的物理属性（极化方向）。这直接围绕“化学大模型”主题，因为它涉及为化学/材料科学中的特定分析任务（从复杂仪器数据中提取信息）开发和应用机器学习模型。

**📖 中文摘要**

这篇论文系统地评估了多种机器学习模型（ResNet, VGG, 自定义CNN, PCA-informed k-NN）在从铁电材料钾钠铌酸盐的4D-STEM衍射图案中自动检测极化方向的任务上的性能。研究旨在解决从4D-STEM数据中提取特定物理属性（如对铁电体功能特性至关重要的极化方向）的挑战。作者在合成数据上训练模型，并分析了仿真与实验之间的领域差距。研究表明，尽管在等效厚度的理想化合成衍射图案上可以达到高精度，但仿真与实验之间的领域差距仍然是实际部署的关键障碍。在此背景下，定制的原型表示训练方案和基于PCA的方法，结合数据增强和过滤，可以更好地弥合这一差距。这项工作为电子显微镜分析开发稳健、可迁移的机器学习工具提供了指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Four-dimensional scanning transmission electron microscopy (4D-STEM) provides rich, atomic-scale insights into materials structures. However, extracting specific physical properties - such as polarization directions essential for understanding functional properties of ferroelectrics - remains a significant challenge. In this study, we systematically benchmark multiple machine learning models, namely ResNet, VGG, a custom convolutional neural network, and PCA-informed k-Nearest Neighbors, to automate the detection of polarization directions from 4D-STEM diffraction patterns in ferroelectric potassium sodium niobate. While models trained on synthetic data achieve high accuracy on idealized synthetic diffraction patterns of equivalent thickness, the domain gap between simulation and experiment remains a critical barrier to real-world deployment. In this context, a custom made prototype representation training regime and PCA-based methods, combined with data augmentation and filtering, can better bridge this gap. Error analysis reveals periodic missclassification patterns, indicating that not all diffraction patterns carry enough information for a successful classification. Additionally, our qualitative analysis demonstrates that irregularities in the model's prediction patterns correlate with defects in the crystal structure, suggesting that supervised models could be used for detecting structural defects. These findings guide the development of robust, transferable machine learning tools for electron microscopy analysis.

</details>

---

### 95. [FC-KAN: Function Combinations in Kolmogorov-Arnold Networks](https://arxiv.org/abs/2409.01763)

**基本信息**

- 🔗 arXiv: [`2409.01763`](https://arxiv.org/abs/2409.01763)
- 👥 作者: Hoang-Thang Ta, Duy-Quy Thai, Abu Bakar Siddiqur Rahman 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.01763.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕一种新型的神经网络架构（KAN）展开，该架构作为基础模型的一种潜在范式，与“化学大模型”这一主题直接相关，为构建化学领域的专用大模型提供了新的技术思路和架构选择。

**📖 中文摘要**

本文介绍了FC-KAN，一种基于Kolmogorov-Arnold网络（KAN）的模型。KAN是一种新兴的神经网络架构，旨在通过可学习的激活函数（如B样条、小波、径向基函数等）来替代传统多层感知机（MLP）中的固定激活函数。FC-KAN的核心创新在于探索了多种数学函数的组合方式（如求和、逐元素乘积、二次/三次函数表示、拼接等）来构建网络。作者在MNIST和Fashion-MNIST数据集上进行了实验，结果表明某些FC-KAN变体（结合B样条和高斯导数DoG，或结合B样条和线性变换的二次函数形式）在平均性能上优于MLP和其他现有的KAN模型（如BSRBF-KAN、EfficientKAN等）。本文的研究属于“化学大模型”主题的范畴，因为KAN作为一种新型的基础模型架构，其设计理念（利用可解释的数学函数作为基础组件）和探索不同函数组合以提升性能的思路，对于构建更强大、更可解释的化学领域专用大模型具有重要的启发意义。它提供了一种不同于传统Transformer或MLP的模型构建范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we introduce FC-KAN, a Kolmogorov-Arnold Network (KAN) that leverages combinations of popular mathematical functions such as B-splines, wavelets, and radial basis functions on low-dimensional data through element-wise operations. We explore several methods for combining the outputs of these functions, including sum, element-wise product, the addition of sum and element-wise product, representations of quadratic and cubic functions, concatenation, linear transformation of the concatenated output, and others. In our experiments, we compare FC-KAN with a multi-layer perceptron network (MLP) and other existing KANs, such as BSRBF-KAN, EfficientKAN, FastKAN, and FasterKAN, on the MNIST and Fashion-MNIST datasets. Two variants of FC-KAN, which use a combination of outputs from B-splines and Derivative of Gaussians (DoG) and from B-splines and linear transformations in the form of a quadratic function, outperformed overall other models on the average of 5 independent training runs. We expect that FC-KAN can leverage function combinations to design future KANs. Our repository is publicly available at: this https URL .

</details>

---

### 96. [Interpretable Visualizations of Data Spaces for Classification Problems](https://arxiv.org/abs/2503.05861)

**基本信息**

- 🔗 arXiv: [`2503.05861`](https://arxiv.org/abs/2503.05861)
- 👥 作者: Christian Jorgensen, Arthur Y. Lin, Rhushil Vasavada 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.05861.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于分类模型（包括潜在的化学大模型）决策边界可视化和解释的方法，并以化学神经毒性预测为例进行演示。这直接服务于理解和解释化学大模型的内在机制，是化学信息学中模型可解释性研究的重要组成部分。

**📖 中文摘要**

本文提出了一种新颖的、混合监督-无监督的可视化技术，专门用于可视化分类问题中的决策边界。该方法能够生成人类可解释的图谱，支持定性和定量分析。作者以化学神经毒性预测为例，展示了如何利用该方法来“打开”机器学习分类模型的“黑箱”，解释其决策过程。虽然论文在化学驱动的分类问题上进行了演示，但该方法可以推广到其他子领域。这项工作与“化学大模型”主题高度相关，因为它直接解决了化学领域机器学习模型（包括潜在的大模型）的可解释性问题。通过提供一种可视化决策边界的方法，它有助于化学家理解模型如何根据分子特征或性质数据进行分类，这对于建立对复杂化学大模型的信任、调试模型以及发现新的化学知识至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

How do classification models "see" our data? Based on their success in delineating behaviors, there must be some lens through which it is easy to see the boundary between classes; however, our current set of visualization techniques makes this prospect difficult. In this work, we propose a hybrid supervised-unsupervised technique distinctly suited to visualizing the decision boundaries determined by classification problems. This method provides a human-interpretable map that can be analyzed qualitatively and quantitatively, which we demonstrate through visualizing and interpreting a decision boundary for chemical neurotoxicity. While we discuss this method in the context of chemistry-driven problems, its application can be generalized across subfields for "unboxing" the operations of machine-learning classification models.

</details>

---

### 97. [A Survey on Deep Learning Approaches for Tabular Data Generation: Utility, Alignment, Fidelity, Privacy, Diversity, and Beyond](https://arxiv.org/abs/2503.05954)

**基本信息**

- 🔗 arXiv: [`2503.05954`](https://arxiv.org/abs/2503.05954)
- 👥 作者: Mihaela Cătălina Stoian, Eleonora Giunchiglia, Thomas Lukasiewicz
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.05954.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于表格数据生成深度学习方法（包括生成模型）的综合性综述。它系统地梳理了该领域的模型、评估方法和挑战。由于化学和质谱数据常以表格形式存在，这篇综述为化学信息学和质谱分析领域的研究者提供了选择和应用数据生成技术的重要参考和展望，有助于推动相关主题下数据资源的构建和模型训练。

**📖 中文摘要**

本文对用于表格数据生成的深度生成模型方法进行了全面的综述。生成建模已成为合成表格数据的标准方法，但不同的用例对合成数据有不同的要求。本综述从五个需求角度回顾了深度生成建模方法：合成数据的效用、与领域特定知识的对齐、合成数据分布与真实数据分布的统计保真度、隐私保护能力以及采样多样性。作者根据这些需求以及所利用的基础模型类型对方法进行了分组。此外，还总结了针对每个需求的适当评估方法、需求之间的关系以及每种模型类型的具体特征。最后，讨论了该领域的未来方向以及改进当前评估方法的机会。这篇综述与“化学大模型”和“质谱结构推理”主题都相关。在化学信息学中，经常需要处理分子性质、光谱数据等表格数据。生成高质量的合成化学数据（如分子结构、质谱图）对于数据增强、隐私保护以及构建训练大模型的数据集至关重要。本文提供的框架和见解可以直接指导化学领域中选择和评估合适的表格数据生成模型，特别是对于构建用于质谱结构推理或分子性质预测的合成数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Generative modelling has become the standard approach for synthesising tabular data. However, different use cases demand synthetic data to comply with different requirements to be useful in practice. In this survey, we review deep generative modelling approaches for tabular data from the perspective of five types of requirements: utility of the synthetic data, alignment of the synthetic data with domain-specific knowledge, statistical fidelity of the synthetic data distribution compared to the real data distribution, privacy-preserving capabilities, and sampling diversity. We group the approaches along two levels of granularity: (i) based on the requirements they address and (ii) according to the underlying model they utilise. Additionally, we summarise the appropriate evaluation methods for each requirement, the relationships among the requirements, and the specific characteristics of each model type. Finally, we discuss future directions for the field, along with opportunities to improve the current evaluation methods. Overall, this survey can be seen as a user guide to tabular data generation: helping readers navigate available models and evaluation methods to find those best suited to their needs.

</details>

---

### 98. [High Quality Underwater Image Compression with Adaptive Color Correction](https://arxiv.org/abs/2505.09986)

**基本信息**

- 🔗 arXiv: [`2505.09986`](https://arxiv.org/abs/2505.09986)
- 👥 作者: Yimin Zhou, Yichong Xia, Sicheng Pan 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.09986.pdf)

**💡 相关性分析**

满足标准1：论文提出的自适应颜色校正和光照估计方法，虽然应用于图像领域，但其处理信号失真、进行自适应校正的核心思想，与质谱分析中预处理原始谱图数据（如基线校正、噪声抑制）以服务于后续结构推理的任务在方法论上高度相关。这为改进质谱数据预处理流程提供了潜在的技术借鉴。

**📖 中文摘要**

本文提出了一种名为HQUIC的高质量水下图像压缩框架。水下图像受到水对光波的折射和散射影响，存在独特的照明条件和颜色偏移，给压缩带来挑战。HQUIC框架包含一个自适应照明和色调校正（ALTC）模块，用于预测图像的衰减系数和全局光信息，从而缓解水下图像的照明和色调变化问题。其次，它动态加权多尺度频率成分，优先保留对失真质量关键的信息，同时丢弃冗余细节。此外，还引入了色调调整损失，使模型能更好地平衡不同颜色通道之间的差异。在多个水下数据集上的综合评估验证了HQUIC优于最先进的压缩方法。虽然论文主要关注图像压缩，但其核心技术——自适应颜色校正和光照估计——与“质谱结构推理”主题存在潜在关联。在质谱分析中，原始谱图数据（如色谱图、质谱图）也经常受到基线漂移、噪声和仪器响应变化的影响，需要进行预处理（如基线校正、归一化）以提取可靠的特征用于结构推理。HQUIC中用于处理复杂光照和颜色失真的自适应校正思路，可以类比并启发质谱数据预处理中针对复杂背景和信号变化的自适应校正算法的设计。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

With the increasing exploration and exploitation of the underwater world, underwater images have become a critical medium for human interaction with marine environments, driving extensive research into their efficient transmission and storage. However, contemporary underwater image compression algorithms fail to adequately address the impact of water refraction and scattering on light waves, which not only elevate training complexity but also result in suboptimal compression performance. To tackle this limitation, we propose High Quality Underwater Image Compression (HQUIC), a novel framework designed to handle the unique illumination conditions and color shifts inherent in underwater images, thereby achieving superior compression performance. HQUIC first incorporates an Adaptive Lighting and Tone Correction (ALTC) module to adaptively predict the attenuation coefficients and global light information of images, effectively alleviating issues stemming from variations in illumination and tone across underwater images. Secondly, it dynamically weights multi-scale frequency components, prioritizing information critical to distortion quality while discarding redundant details. Furthermore, we introduce a tone adjustment loss to enable the model to better balance discrepancies among different color channels. Comprehensive evaluations on diverse underwater datasets validate that HQUIC outperforms state-of-the-art compression methods, demonstrating its effectiveness.

</details>

---

### 99. [The Future of Artificial Intelligence and the Mathematical and Physical Sciences (AI+MPS)](https://arxiv.org/abs/2509.02661)

**基本信息**

- 🔗 arXiv: [`2509.02661`](https://arxiv.org/abs/2509.02661)
- 👥 作者: Andrew Ferguson, Marisa LaFleur, Lars Ruthotto 等100人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.02661.pdf)

**💡 相关性分析**

满足标准3：论文是关于AI（包括大模型）在科学领域（明确包含化学）未来应用的综述和展望，包含了对这些主题的重要讨论。

**📖 中文摘要**

这篇论文是美国国家科学基金会（NSF）关于人工智能（AI）与数学和物理科学（MPS）未来研讨会的社区报告。报告总结了天文学、化学、材料研究、数学科学和物理学等MPS领域如何最好地利用AI的未来发展并为之做出贡献。报告明确指出，AI与MPS之间的联系正变得日益紧密，现在是加强AI与科学联系的关键时刻。为此，报告提出了战略优先事项和活动建议，包括：1）促进双向的AI+MPS研究；2）建立跨学科的AI+MPS研究社区；3）培养MPS研究人员和学生在AI方面的教育和劳动力发展。虽然论文主题广泛，但其中明确包含了化学领域，并讨论了AI（包括大模型）对整个科学领域（包括化学）的变革性潜力及其在科学发现中的应用。这符合对化学信息学中“化学大模型”主题的重要展望和讨论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This community paper developed out of the NSF Workshop on the Future of Artificial Intelligence (AI) and the Mathematical and Physics Sciences (MPS), which was held in March 2025 with the goal of understanding how the MPS domains (Astronomy, Chemistry, Materials Research, Mathematical Sciences, and Physics) can best capitalize on, and contribute to, the future of AI. We present here a summary and snapshot of the MPS community's perspective, as of Spring/Summer 2025, in a rapidly developing field. The link between AI and MPS is becoming increasingly inextricable; now is a crucial moment to strengthen the link between AI and Science by pursuing a strategy that proactively and thoughtfully leverages the potential of AI for scientific discovery and optimizes opportunities to impact the development of AI by applying concepts from fundamental science. To achieve this, we propose activities and strategic priorities that: (1) enable AI+MPS research in both directions; (2) build up an interdisciplinary community of AI+MPS researchers; and (3) foster education and workforce development in AI for MPS researchers and students. We conclude with a summary of suggested priorities for funding agencies, educational institutions, and individual researchers to help position the MPS community to be a leader in, and take full advantage of, the transformative potential of AI+MPS.

</details>

---

### 100. [Machine Learning Detection of Lithium Plating in Lithium-ion Cells: A Gaussian Process Approach](https://arxiv.org/abs/2509.26234)

**基本信息**

- 🔗 arXiv: [`2509.26234`](https://arxiv.org/abs/2509.26234)
- 👥 作者: Ayush Patnaik, Jackson Fogelquist, Adam B Zufall 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.26234.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于高斯过程的机器学习模型，用于分析质谱/电化学谱的衍生数据（微分容量曲线），以推断电池内部的化学结构状态（锂镀层）。这直接涉及“质谱结构推理”主题中“从谱数据推理结构”的核心思想，尽管数据源是电化学而非传统质谱，但方法论高度相关。

**📖 中文摘要**

这篇论文提出了一种基于高斯过程（Gaussian Process, GP）的机器学习框架，用于检测锂离子电池快充过程中的锂枝晶析出（锂镀层）。锂镀层是电池退化和安全失效的关键机制。传统方法通过计算微分容量（dQ/dV）来识别特征峰，但受噪声和滤波影响。该框架将电荷-电压关系Q(V)建模为一个随机过程，并利用GP的导数仍是GP的特性，直接从后验概率中解析地推断出dQ/dV，从而实现了鲁棒的检测和不确定性量化。该方法具有噪声感知、闭式导数和可扩展至嵌入式电池管理系统（BMS）等优点。实验在多种倍率和温度下的锂离子纽扣电池上验证了该方法的有效性，能够可靠地识别与锂镀层相关的高压二次峰特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Lithium plating during fast charging is a critical degradation mechanism that accelerates capacity fade and can trigger catastrophic safety failures. Recent work has shown that plating onset can manifest in incremental-capacity analysis as an additional high-voltage feature above 4.0 V, often appearing as a secondary peak or shoulder distinct from the main intercalation peak complex; however, conventional methods for computing dQ/dV rely on finite differencing with filtering, which amplifies sensor noise and introduces bias in feature location. In this paper, we propose a Gaussian Process (GP) framework for lithium plating detection by directly modeling the charge-voltage relationship Q(V) as a stochastic process with calibrated uncertainty. Leveraging the property that derivatives of GPs remain GPs, we infer dQ/dV analytically and probabilistically from the posterior, enabling robust detection without ad hoc smoothing. The framework provides three key benefits: (i) noise-aware inference with hyperparameters learned from data, (ii) closed-form derivatives with credible intervals for uncertainty quantification, and (iii) scalability to online variants suitable for embedded BMS. Experimental validation on Li-ion coin cells across a range of C-rates (0.2C-1C) and temperatures (0-40$^\circ$C) demonstrates that the GP-based method reliably resolves distinct high-voltage secondary peak features under low-temperature, high-rate charging, while correctly reporting no features in non-plating cases. The concurrence of GP-identified differential features, reduced charge throughput, capacity fade measured via reference performance tests, and post-mortem microscopy confirmation supports the interpretation of these signatures as plating-related, establishing a practical pathway for real-time lithium plating detection.

</details>

---

### 101. [TsLLM: Augmenting LLMs for General Time Series Understanding and Prediction](https://arxiv.org/abs/2510.01111)

**基本信息**

- 🔗 arXiv: [`2510.01111`](https://arxiv.org/abs/2510.01111)
- 👥 作者: Felix Parker, Nimeesha Chan, Chi Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01111.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个通用的、基于大语言模型（LLM）的“化学大模型”类框架，用于理解和分析复杂的数值时间序列数据。虽然应用领域不限于化学，但其“增强LLM以处理专业领域数值数据”的核心范式与化学信息学中构建领域大模型（如用于光谱、分子性质预测的模型）高度相关。

**📖 中文摘要**

本文介绍了TsLLM，一种通过基于补丁的编码器-解码器架构，用专门的时间序列感知能力来增强大语言模型（LLM）的模型。TsLLM在超过250亿个交织的时间序列和文本标记上进行训练，涵盖了多种任务，包括带有上下文信息的预测、问答、异常检测、分类、报告生成等。训练使TsLLM能够利用其语言理解能力和新获得的时间序列推理能力。虽然TsLLM并非旨在传统基准测试上超越专用模型，但它在需要将时间序列分析与自然语言整合的任务上表现出强大的性能。此外，它还展示了强大的零样本和少样本性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Time series data is fundamental to decision-making across many domains including healthcare, finance, power systems, and logistics. However, analyzing this data correctly often requires incorporating unstructured contextual information, answering domain-specific questions, and generating natural language explanations - capabilities that traditional time series models lack. While Large Language Models (LLMs) excel at contextual reasoning and knowledge integration, they struggle with numerical time series due to inefficient text-based representations and limited exposure to numerical data during pretraining. We address this gap by augmenting an LLM with specialized time series perception through a patch-based encoder-decoder architecture. We train this Time Series augmented LLM (TsLLM) on a large corpus of over 25 billion tokens of interleaved time series and text spanning diverse tasks: forecasting with contextual information, question-answering, anomaly detection, classification, report generation, and more, all unified as next token prediction. This training enables TsLLM to leverage both its language understanding and newly acquired temporal reasoning capabilities. While not designed to surpass specialized models on traditional benchmarks, TsLLM demonstrates strong performance on tasks requiring the integration of time series analysis with natural language - capabilities that existing approaches cannot provide. It also exhibits strong zero-shot and few-shot performance, showing it can adapt to new data without additional training.

</details>

---

### 102. [Eliciting Chain-of-Thought Reasoning for Time Series Analysis using Reinforcement Learning](https://arxiv.org/abs/2510.01116)

**基本信息**

- 🔗 arXiv: [`2510.01116`](https://arxiv.org/abs/2510.01116)
- 👥 作者: Felix Parker, Nimeesha Chan, Chi Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01116.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种训练大语言模型（LLM）进行复杂推理的方法论框架（COUNTS），特别针对时间序列等数值数据的分析。这属于“化学大模型”主题中“如何训练和增强领域大模型进行科学推理”的重要子方向，其方法可迁移至化学数据（如质谱、光谱序列）的分析与推理。

**📖 中文摘要**

本文介绍了COUNTS框架，这是第一个使用带有可验证奖励的强化学习（RL）来训练大语言模型（LLM）在各种时间序列任务上执行思维链（CoT）推理的框架。该方法采用残差向量量化变分自编码器（Residual VQ-VAE）来创建高保真度的离散标记，并将其无缝集成到预训练LLM的词表中。COUNTS经过两阶段训练：首先在时间序列分析任务上进行监督微调，然后使用鼓励在产生最终答案前进行显式推理步骤的提示策略，在可验证问题上进行组相对策略优化（GRPO）训练。实验表明，这种带有中间CoT推理的RL驱动方法显著提升了LLM在各种时间序列分析任务上的性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Complex numerical time series analysis often demands multi-step reasoning capabilities beyond current models' reach. Tasks like medical diagnosis and weather forecasting require sequential reasoning processes - including counterfactual analysis, logical deduction, knowledge application, and multi-modal contextual integration - that existing time series models cannot explicitly perform. While recent research has shown large language models (LLMs) can achieve sophisticated Chain-of-Thought (CoT) reasoning through reinforcement learning (RL), these advances have primarily focused on mathematical and coding domains, with LLMs still demonstrating poor performance on time series tasks. We introduce Chain Of thought for Understanding Numerical Time Series (COUNTS), the first framework that trains LLMs to perform CoT reasoning across diverse time series tasks using RL with verifiable rewards. Our approach employs a Residual Vector-Quantized VAE to create high-fidelity discrete tokens that seamlessly integrate into a pre-trained LLM's vocabulary. COUNTS undergoes a two-stage training process: first, supervised fine-tuning on time series analysis tasks to master our novel representations, followed by Group Relative Policy Optimization training on verifiable problems using prompting strategies that encourage explicit reasoning steps before producing final answers. Our experiments demonstrate that this RL-driven approach with intermediate CoT reasoning significantly enhances LLM performance across various time series analysis tasks, opening new possibilities for complex temporal data reasoning.

</details>

---

### 103. [Automated Genomic Interpretation via Concept Bottleneck Models for Medical Robotics](https://arxiv.org/abs/2510.01618)

**基本信息**

- 🔗 arXiv: [`2510.01618`](https://arxiv.org/abs/2510.01618)
- 👥 作者: Zijun Li, Jinchang Zhang, Ming Zhang 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01618.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于概念瓶颈模型（CBM）和混沌游戏表示（CGR）的、可解释的机器学习模型，用于从生物序列（DNA）数据中推理出结构化和语义化的信息（如亚型、生物概念）。这本质上是“结构推理”在生物信息学中的体现，其“从序列数据推理出结构化概念/属性”的范式与“质谱结构推理”（从谱图推理出分子结构/属性）高度相似，属于广义的“化学信息学”范畴。

**📖 中文摘要**

本文提出了一个自动化基因组解释模块，将原始DNA序列转化为可操作的、可解释的决策，适用于集成到医疗自动化和机器人系统中。该框架结合了混沌游戏表示（CGR）和概念瓶颈模型（CBM），强制预测通过具有生物学意义的概念（如GC含量、CpG密度、k-mer基序）流动。为了增强可靠性，该模块整合了概念保真度监督、先验一致性对齐、KL分布匹配和不确定性校准。除了在内部和LANL数据集上准确分类HIV亚型外，该模块还提供可解释的证据，可直接与生物学先验进行验证。一个成本感知的推荐层进一步将预测输出转化为决策策略，平衡准确性、校准和临床效用。大量实验表明，该系统实现了最先进的分类性能、卓越的概念预测保真度，以及与现有基线相比更有利的成本效益权衡。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose an automated genomic interpretation module that transforms raw DNA sequences into actionable, interpretable decisions suitable for integration into medical automation and robotic systems. Our framework combines Chaos Game Representation (CGR) with a Concept Bottleneck Model (CBM), enforcing predictions to flow through biologically meaningful concepts such as GC content, CpG density, and k mer motifs. To enhance reliability, we incorporate concept fidelity supervision, prior consistency alignment, KL distribution matching, and uncertainty calibration. Beyond accurate classification of HIV subtypes across both in-house and LANL datasets, our module delivers interpretable evidence that can be directly validated against biological priors. A cost aware recommendation layer further translates predictive outputs into decision policies that balance accuracy, calibration, and clinical utility, reducing unnecessary retests and improving efficiency. Extensive experiments demonstrate that the proposed system achieves state of the art classification performance, superior concept prediction fidelity, and more favorable cost benefit trade-offs compared to existing baselines. By bridging the gap between interpretable genomic modeling and automated decision-making, this work establishes a reliable foundation for robotic and clinical automation in genomic medicine.

</details>

---

### 104. [From Text to Alpha: Can LLMs Track Evolving Signals in Corporate Disclosures?](https://arxiv.org/abs/2510.03195)

**基本信息**

- 🔗 arXiv: [`2510.03195`](https://arxiv.org/abs/2510.03195)
- 👥 作者: Chanyeol Choi, Yoon Kim, Yu Yu 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.03195.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用大语言模型（LLM）作为特征提取器，从非结构化的专业领域文本（公司财报）中提取和量化语义信号，用于预测任务。这属于“化学大模型”在专业领域（此处是金融）进行信息提取和推理的应用范例。其方法论（LLM提取语义特征+嵌入量化变化）可类比于化学信息学中使用LLM处理科学文献或实验报告以提取化学实体和关系。

**📖 中文摘要**

本文探讨了大语言模型（LLMs）能否从公司披露文本中追踪演化信号并预测超额收益（Alpha）。作者提出了一个简单的框架“LLM作为提取器，嵌入作为标尺”，该框架提取上下文感知的、以指标为中心的文本片段，并使用基于嵌入的相似性来量化连续披露期间之间的语义变化。这允许我们度量“指标偏移”的程度——即公司偏离先前强调的指标的程度。在投资组合和横截面回归测试中，与最近的基于命名实体识别（NER）的基线相比，该方法实现了超过两倍的风险调整后Alpha，并显示出显著更强的预测能力。定性分析表明，这些收益源于保留了上下文限定词，并过滤掉了基于关键词的方法经常遗漏的非指标术语。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Natural language processing (NLP) has been widely used in quantitative finance, but traditional methods often struggle to capture rich narratives in corporate disclosures, leaving potentially informative signals under-explored. Large language models (LLMs) offer a promising alternative due to their ability to extract nuanced semantics. In this paper, we ask whether semantic signals extracted by LLMs from corporate disclosures predict alpha, defined as abnormal returns beyond broad market movements and common risk factors. We introduce a simple framework, LLM as extractor, embedding as ruler, which extracts context-aware, metric-focused textual spans and quantifies semantic changes across consecutive disclosure periods using embedding-based similarity. This allows us to measure the degree of metric shifting -- how much firms move away from previously emphasized metrics, referred as moving targets. In experiments with portfolio and cross-sectional regression tests against a recent NER-based baseline, our method achieves more than twice the risk-adjusted alpha and shows significantly stronger predictive power. Qualitative analysis suggests that these gains stem from preserving contextual qualifiers and filtering out non-metric terms that keyword-based approaches often miss.

</details>

---

### 105. [MaP: A Unified Framework for Reliable Evaluation of Pre-training Dynamics](https://arxiv.org/abs/2510.09295)

**基本信息**

- 🔗 arXiv: [`2510.09295`](https://arxiv.org/abs/2510.09295)
- 👥 作者: Jiapeng Wang, Changxin Tian, Kunlong Chen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.09295.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献是提出了一个用于可靠评估大语言模型（LLM）预训练动态的框架（MaP）。虽然不直接提供化学数据集，但它提供了一种重要的“工具”或“方法”（检查点合并+Pass@k评估协议），可用于评估和比较化学领域大模型的训练过程和质量，这对于开发和优化“化学大模型”至关重要。

**📖 中文摘要**

本文提出了MaP框架，旨在解决大语言模型（LLM）预训练过程中评估不稳定的问题。该框架通过协同整合检查点合并（Checkpoint Merging）和Pass@k指标来应对参数不稳定性和评估不稳定性这两种噪声源。检查点合并通过对近期模型权重进行平均来平滑参数空间，而Pass@k则提供了模型能力的鲁棒、低方差统计估计。大量实验表明，MaP能产生更平滑的性能曲线，减少运行间方差，并确保更一致的模型排名。最终，MaP为观察LLM训练动态提供了一个更可靠、更真实的视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reliable evaluation is fundamental to the progress of Large Language Models (LLMs), yet the evaluation process during pre-training is plagued by significant instability that obscures true learning dynamics. In this work, we systematically diagnose this instability, attributing it to two distinct sources: \textit{Parameter Instability} from training stochasticity and \textit{Evaluation Instability} from noisy measurement protocols. To counteract both sources of noise, we introduce \textbf{MaP}, a dual-pronged framework that synergistically integrates checkpoint \underline{M}erging \underline{a}nd the \underline{P}ass@k metric. Checkpoint merging smooths the parameter space by averaging recent model weights, while Pass@k provides a robust, low-variance statistical estimate of model capability. Extensive experiments show that MaP yields significantly smoother performance curves, reduces inter-run variance, and ensures more consistent model rankings. Ultimately, MaP provides a more reliable and faithful lens for observing LLM training dynamics, laying a crucial empirical foundation for LLM research.

</details>

---

### 106. [Beyond AlphaEarth: Toward Human-Centered Geospatial Foundation Models via POI-Guided Contrastive Learning](https://arxiv.org/abs/2510.09894)

**基本信息**

- 🔗 arXiv: [`2510.09894`](https://arxiv.org/abs/2510.09894)
- 👥 作者: Junyuan Liu, Quan Qin, Guangsheng Dong 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.09894.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个框架（AETHER），用于对齐和增强基础模型（此处是地理空间基础模型），通过多模态对齐（图像-文本）使其具备更好的语义理解和自然语言交互能力。这属于“大模型”技术（基础模型对齐、多模态学习）在专业领域的应用。其“增强基础模型的领域语义和可解释性”的方法论与化学信息学中构建和增强“化学大模型”（如对齐分子模型与自然语言描述）的研究方向直接相关。

**📖 中文摘要**

本文介绍了AETHER框架，一个通过由兴趣点（POI）引导的多模态对齐，将AlphaEarth地理空间基础模型与以人为中心的城市分析对齐的轻量级框架。通过强制执行跨模态的AE-POI对齐和模态内的多尺度一致性，AETHER将功能性城市语义与EO驱动的表征相结合，并将嵌入空间建立在自然语言基础上。生成的表征支持城市绘图任务和自然语言条件化的空间检索。在大伦敦和新加坡的四个下游任务上的实验展示了持续的最先进性能。此外，对齐的嵌入空间支持通过自然语言查询进行空间定位。通过将基于EO的基础模型与以人为中心的语义对齐，AETHER提高了地理空间表征的可解释性，并推动了地理空间表征学习向以人为中心、语言可访问的地理空间基础模型发展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent geospatial foundation models (GFMs) produce spatially extensive representations of the Earth's surface that capture rich physical and environmental patterns. Among them, the AlphaEarth Foundation (AE) represents a major step, generating 10 m embeddings from multi-source Earth Observation (EO) data that include diverse environmental and spectral characteristics. However, such EO-driven representations primarily encode physical and spectral patterns rather than human activities or urban semantics, limiting their ability to capture the functional dimensions of cities and making the learned representations difficult to interpret or query using natural language. We introduce AETHER (AlphaEarth-POI Enriched Representation Learning), a lightweight framework that aligns AlphaEarth with human-centered urban analysis through multimodal alignment guided by Points of Interest (POIs). By enforcing both cross-modal AE-POI alignment and intra-modal multi-scale consistency, AETHER integrates functional urban semantics with EO-driven representations and grounds the embedding space in natural language. The resulting representations support both urban mapping tasks and natural language-conditioned spatial retrieval. Experiments across four downstream tasks in Greater London and Singapore demonstrate consistent state-of-the-art performance, with relative improvements ranging from 4.5% to 21.9%. Furthermore, the aligned embedding space enables spatial localization through natural language queries. By aligning EO-based foundation models with human-centered semantics, AETHER improves the interpretability of geospatial representations and advances geospatial representation learning toward human-centered, language-accessible geospatial foundation models.

</details>

---

### 107. [SigMA: Path Signatures and Multi-head Attention for Learning Parameters in fBm-driven SDEs](https://arxiv.org/abs/2512.15088)

**基本信息**

- 🔗 arXiv: [`2512.15088`](https://arxiv.org/abs/2512.15088)
- 👥 作者: Xianglin Wu, Chiheb Ben Hammouda, Cornelis W. Oosterlee
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15088.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕使用路径签名和深度学习（SigMA架构）从复杂的时间序列数据（如fBm驱动的SDE路径）中学习模型参数。这与质谱结构推理中从质谱信号（一种时间/质荷比序列）推断分子结构的任务在方法论上高度相似，都属于从复杂信号中进行参数/结构推断的范畴。

**📖 中文摘要**

本文介绍了SigMA（Signature Multi-head Attention）模型，这是一个将路径签名（Path Signatures）与多头自注意力机制相结合的神经架构，用于从分数布朗运动（fBm）驱动的随机微分方程（SDE）的合成路径中学习模型参数，特别是赫斯特参数（Hurst parameter）。路径签名是一种强大的数学工具，用于从时间序列数据中提取特征，常用于金融、物理和工程等领域的复杂动态系统建模。该研究专注于参数推断，包括分数布朗运动、分数Ornstein-Uhlenbeck过程和粗糙Heston模型。SigMA在合成数据和两个真实世界数据集（股票指数已实现波动率和锂离子电池退化）上的实验表明，其准确性、鲁棒性和模型紧凑性优于CNN、LSTM、Transformer和深度签名基线。这项工作为具有粗糙或持久时间结构的随机系统中的参数推断提供了一个有效且可扩展的框架，与化学信息学和质谱分析中用于建模复杂动态和从时间序列数据（如质谱信号）中推断参数的方法高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Stochastic differential equations (SDEs) driven by fractional Brownian motion (fBm) are increasingly used to model systems with rough dynamics and long-range dependence, such as those arising in quantitative finance and reliability engineering. However, these processes are non-Markovian and lack a semimartingale structure, rendering many classical parameter estimation techniques inapplicable or computationally intractable beyond very specific cases. This work investigates two central questions: (i) whether integrating path signatures into deep learning architectures can improve the trade-off between estimation accuracy and model complexity, and (ii) what constitutes an effective architecture for leveraging signatures as feature maps. We introduce SigMA (Signature Multi-head Attention), a neural architecture that integrates path signatures with multi-head self-attention, supported by a convolutional preprocessing layer and a multilayer perceptron for effective feature encoding. SigMA learns model parameters from synthetically generated paths of fBm-driven SDEs, including fractional Brownian motion, fractional Ornstein-Uhlenbeck, and rough Heston models, with a particular focus on estimating the Hurst parameter and on joint multi-parameter inference, and it generalizes robustly to unseen trajectories. Extensive experiments on synthetic data and two real-world datasets (i.e., equity-index realized volatility and Li-ion battery degradation) show that SigMA consistently outperforms CNN, LSTM, vanilla Transformer, and Deep Signature baselines in accuracy, robustness, and model compactness. These results demonstrate that combining signature transforms with attention-based architectures provides an effective and scalable framework for parameter inference in stochastic systems with rough or persistent temporal structure.

</details>

---

### 108. [The Active Discoverer Framework: Towards Autonomous Physics Reasoning through Neuro-Symbolic LaTeX Synthesis](https://arxiv.org/abs/2601.06117)

**基本信息**

- 🔗 arXiv: [`2601.06117`](https://arxiv.org/abs/2601.06117)
- 👥 作者: Hyunjun Jeon
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.06117.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于自主科学发现（特别是物理规律发现）的神经符号框架。其强调的可解释性、从数据中学习结构化表示（如通过LaTeX瓶颈）以及处理复杂数值外推的能力，与构建能够进行推理、预测和发现的可解释“化学大模型”的研究主题在理念和技术路径上高度相关。

**📖 中文摘要**

本文提出了“主动发现者框架”（Active Discoverer Framework），这是一个面向不变性发现的数字原生神经符号架构。其核心是NumberNet，一个使用最低有效位序列编码的孪生算术Transformer，旨在实现零精度损失和大尺度外推。该框架的关键创新是“符号LaTeX瓶颈”：一个主动发现循环，模型通过自回归LaTeX解码器被迫假设未知的物理变量，从而确保发现的物理学是简洁且人类可解释的。该研究评估了系统从数据中自主推导物理常数（如引力常数G）的能力。虽然主要应用于理论物理和数学推理，但该框架的核心思想——将数值“幻觉”与结构上有效的数学表达式相协调，以实现可解释的模型和自主科学发现——与构建“化学大模型”的目标高度一致，后者也旨在从数据中发现可解释的化学规律和分子表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern artificial intelligence excels at statistical interpolation within seen manifolds but fundamentally fails at the exact reasoning required for theoretical physics and mathematics. We identify the "Float Wall" -- a catastrophic collapse of neural extrapolation at scales beyond $10^{16}$ -- caused by standard floating-point representation and linguistic tokenization (BPE). To resolve this, we introduce the Active Discoverer Framework, a digit-native neuro-symbolic architecture designed for invariant discovery. At its core is NumberNet, a Siamese Arithmetic Transformer that utilizes least-significant-bit (LSB) sequence encoding to achieve 0% precision loss and cosmic-scale extrapolation up to $10^{50}$. To enforce physical grounding, we implement a Hamiltonian-based energy descent and Symmetry Grouping layer, ensuring the model respects Noether's theorem natively. The primary innovation is the Symbolic LaTeX Bottleneck: an active discovery loop where the model is forced to hypothesize unknown physical variables through an autoregressive LaTeX decoder. By reconciling numeric "hallucinations" with structurally valid mathematical expressions, the framework ensures that any discovered physics is parsimonious and human-interpretable. We evaluate this system against a 30-billion scale benchmark and the Universal Physics Pantheon, featuring 50 "Chaos Mode" systemic perturbations. Our results demonstrate that while traditional GBDT and LLM-based architectures collapse at cosmic scales, the Active Discoverer autonomously deduces universal constants such as the Gravitational Constant ($G$) with high fidelity. This framework establishes a path toward zero-hallucination artificial intelligence and truly autonomous scientific research agents.

</details>

---

### 109. [ChemPro: A Progressive Chemistry Benchmark for Large Language Models](https://arxiv.org/abs/2602.03108)

**基本信息**

- 🔗 arXiv: [`2602.03108`](https://arxiv.org/abs/2602.03108)
- 👥 作者: Aaditya Baranwal, Shruti Vyas
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.03108.pdf)

**💡 相关性分析**

满足标准2：论文提供了专门用于评估化学领域大型语言模型（即“化学大模型”）性能的数据集和基准（ChemPro）。这是一个重要的数据资源，可用于训练、微调和评估面向化学的LLM，直接服务于“化学大模型”这一主题的研究与发展。

**📖 中文摘要**

本文介绍了ChemPro，一个包含4100个自然语言问答对的渐进式化学基准测试，旨在评估大型语言模型在广泛普通化学主题上的熟练程度。问题涵盖生物化学、无机化学、有机化学和物理化学，难度从基础信息回忆到长程推理、多概念问题、需要细致表述的问题解决等逐步增加。该基准测试模拟了学生从基础到高中化学的学术评估过程。作者评估了45+7个最先进的LLM，发现它们在基础化学问题上表现良好，但随着问题类型和复杂度的增加，准确性下降。这些发现突出了LLM在一般科学推理和理解方面的关键局限性。该工作直接为“化学大模型”的评估提供了专门的、大规模的基准测试工具和深入的分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce ChemPro, a progressive benchmark with 4100 natural language question-answer pairs in Chemistry, across 4 coherent sections of difficulty designed to assess the proficiency of Large Language Models (LLMs) in a broad spectrum of general chemistry topics. We include Multiple Choice Questions and Numerical Questions spread across fine-grained information recall, long-horizon reasoning, multi-concept questions, problem-solving with nuanced articulation, and straightforward questions in a balanced ratio, effectively covering Bio-Chemistry, Inorganic-Chemistry, Organic-Chemistry and Physical-Chemistry. ChemPro is carefully designed analogous to a student's academic evaluation for basic to high-school chemistry. A gradual increase in the question difficulty rigorously tests the ability of LLMs to progress from solving basic problems to solving more sophisticated challenges. We evaluate 45+7 state-of-the-art LLMs, spanning both open-source and proprietary variants, and our analysis reveals that while LLMs perform well on basic chemistry questions, their accuracy declines with different types and levels of complexity. These findings highlight the critical limitations of LLMs in general scientific reasoning and understanding and point towards understudied dimensions of difficulty, emphasizing the need for more robust methodologies to improve LLMs.

</details>

---

## 📊 数据统计
- 累计运行天数：36
- 累计论文数量：2590

## 📝 历史记录

> 暂无历史数据

