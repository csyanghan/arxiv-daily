# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-20 01:23:48

## 📅 2026-03-20 (今日最新)

**相关论文数：77**

### 1. [A foundation model for electrodermal activity data](https://arxiv.org/abs/2603.16878)

**基本信息**

- 🔗 arXiv: [`2603.16878`](https://arxiv.org/abs/2603.16878)
- 👥 作者: Leonardo Alchieri, Matteo Garzon, Lidia Alecci 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16878.pdf)

**💡 相关性分析**

满足标准2：论文构建并开源了一个大规模、高质量的生理信号（EDA）数据集，并基于此训练了一个专门的基础模型。这为化学信息学和质谱分析领域（尤其是处理复杂时序/光谱信号）提供了重要的数据资源和模型构建思路，展示了如何利用大规模数据集训练特定领域的专用基础模型。

**📖 中文摘要**

本文提出并发布了EDAMAME，一个包含超过25,000小时、来自634名用户的皮肤电活动（EDA）信号的大型公开数据集。基于此数据集，作者训练了UME，这是首个专门针对EDA信号的基础模型。该模型在多个场景下超越了基线模型，并与通用的时序基础模型性能相当，同时计算资源消耗减少了20倍。作者公开了所有数据集、模型权重和代码以支持进一步研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models have recently extended beyond natural language and vision to timeseries domains, including physiological signals. However, progress in electrodermal activity (EDA) modeling is hindered by the absence of large-scale, curated, and openly accessible datasets. EDA reflects sympathetic nervous system activity and is widely used to infer cognitive load, stress, and engagement. Yet very few wearable devices provide continuous, unobtrusive sensing, and the only large-scale archive to date is proprietary. To address this gap, we compile EDAMAME, a collection of EDA traces from 24 public datasets, comprising more than 25,000 hours from 634 users. Using this resource, we train UME, the first dedicated foundation model for EDA. In eight out of ten scenarios, UME outperforms baselines and matches generalist timeseries foundation models while using 20x fewer computational resources. Our findings, however, also highlight the intrinsic challenges of EDA modeling, motivating further research to unlock its full potential. All datasets, model weights, and code are released to support further research.

</details>

---

### 2. [HoloByte: Continuous Hyperspherical Distillation for Tokenizer-Free Modeling](https://arxiv.org/abs/2603.16917)

**基本信息**

- 🔗 arXiv: [`2603.16917`](https://arxiv.org/abs/2603.16917)
- 👥 作者: Vladimer Khasia
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16917.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新型的、无需分词的序列建模框架。这直接与“化学大模型”的主题相关，因为化学大模型（如用于分子表示学习或光谱预测的模型）同样面临如何有效处理离散符号序列（如SMILES字符串、质谱峰序列）的挑战。HoloByte提出的连续表示和降维方法为化学信息学中处理分子序列或光谱数据提供了新颖的建模思路。

**📖 中文摘要**

本文提出了HoloByte，一个完全无需分词器的序列建模框架。它通过连续超球面蒸馏技术，将离散的字节序列块投影到一个连续、有界的超球面流形上，从而允许宏观Transformer在压缩后的连续表示上操作，显著降低了精确注意力的时间复杂度。该方法旨在解决传统子词分词带来的形态边界、词汇依赖和优化景观不连续等问题，为词汇无关的序列建模提供了数学上严谨且计算上可行的基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sequence modeling universally relies on discrete subword tokenization to circumvent the $\mathcal{O}(N^2)$ computational intractability of native byte-level attention. However, this heuristic quantization imposes artificial morphological boundaries, enforces vocabulary dependence, and fractures the continuity of the optimization landscape. To resolve this dichotomy, we introduce \textbf{HoloByte}: a strictly tokenizer-free framework utilizing Continuous Hyperspherical Distillation. HoloByte partitions discrete byte sequences into fixed-capacity chunks and projects them into a continuous, strictly bounded hyperspherical manifold via an invertible, dimension-preserving orthogonal rotation operator. This spatial superposition allows a macroscopic transformer to operate exclusively on compressed continuous representations, formally reducing the exact attention time complexity from $\mathcal{O}(N^2D)$ to $\mathcal{O}\left( \frac{N^2}{W^2}D + ND^2 \right)$. A localized causal micro-decoder subsequently unbinds these representations to compute exact byte-level distributions. To govern this continuous trajectory, we propose a dual-objective formulation incorporating a mathematically precise Holographic Latent Mean Squared Error, which strictly bounds the gradient and guarantees asymptotic stability. Theoretically, we derive the minimal embedding dimension $D = \Omega(W \ln |\mathcal{V}|)$ required to ensure error-free discrete recovery from the continuous manifold. Empirically, under strictly matched parameter constraints, HoloByte is systematically outperforming a comparable discrete Byte-Pair Encoding (BPE) baseline. These results establish Continuous Hyperspherical Distillation as a mathematically rigorous and computationally tractable foundation for vocabulary-invariant sequence modeling. The code is available at this https URL

</details>

---

### 3. [Minimum-Action Learning: Energy-Constrained Symbolic Model Selection for Physical Law Identification from Noisy Data](https://arxiv.org/abs/2603.16951)

**基本信息**

- 🔗 arXiv: [`2603.16951`](https://arxiv.org/abs/2603.16951)
- 👥 作者: Martin G. Frasch
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16951.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从数据中学习符号化的物理定律（力定律）。这直接与“质谱结构推理”的主题高度相关，因为质谱结构推理的本质就是从质谱数据（观测数据）中推断出产生该谱图的分子结构（底层“物理定律”或“生成规则”）。MAL框架中使用的符号基函数库选择、稀疏性约束和能量守恒等思想，可以类比为从质谱数据中寻找最可能的分子碎片化规则和结构约束。

**📖 中文摘要**

本文提出了最小行动学习（MAL），一个从噪声观测数据中识别物理定律的框架。MAL通过最小化一个结合了轨迹重建、架构稀疏性和能量守恒强制执行的三重行动泛函，从一个预定义的符号基函数库中选择符号力定律。该方法利用宽间隔加速度匹配技术将噪声方差降低10,000倍，从而将不可学习的问题转化为可学习的问题。在开普勒引力和胡克定律基准测试中，MAL能够以高精度恢复正确的力定律。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Identifying physical laws from noisy observational data is a central challenge in scientific machine learning. We present Minimum-Action Learning (MAL), a framework that selects symbolic force laws from a pre-specified basis library by minimizing a Triple-Action functional combining trajectory reconstruction, architectural sparsity, and energy-conservation enforcement. A wide-stencil acceleration-matching technique reduces noise variance by 10,000x, transforming an intractable problem (SNR ~0.02) into a learnable one (SNR ~1.6); this preprocessing is the critical enabler shared by all methods tested, including SINDy variants. On two benchmarks -- Kepler gravity and Hooke's law -- MAL recovers the correct force law with Kepler exponent p = 3.01 +/- 0.01 at ~0.07 kWh (40% reduction vs. prediction-error-only baselines). The raw correct-basis rate is 40% for Kepler and 90% for Hooke; an energy-conservation-based criterion discriminates the true force law in all cases, yielding 100% pipeline-level identification. Basis library sensitivity experiments show that near-confounders degrade selection (20% with added r^{-2.5} and r^{-1.5}), while distant additions are harmless, and the conservation diagnostic remains informative even when the correct basis is absent. Direct comparison with noise-robust SINDy variants, Hamiltonian Neural Networks, and Lagrangian Neural Networks confirms MAL's distinct niche: interpretable, energy-constrained model selection that combines symbolic basis identification with dynamical rollout validation.

</details>

---

### 4. [Implementation of tangent linear and adjoint models for neural networks based on a compiler library tool](https://arxiv.org/abs/2603.16976)

**基本信息**

- 🔗 arXiv: [`2603.16976`](https://arxiv.org/abs/2603.16976)
- 👥 作者: Sa Xiao, Hao Jing, Honglu Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16976.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门的工具（TorchNWP），用于将深度学习模型（尤其是PyTorch模型）集成到传统的科学计算框架（如数值天气预报模型）中，并支持生成其切线性/伴随模型。这为化学信息学和质谱分析领域提供了一个重要的工具资源范例。例如，在构建“化学大模型”或质谱预测模型时，可能需要将训练好的神经网络集成到更大的模拟或优化流程中，TorchNWP所解决的跨语言兼容性、耦合效率和模型导出问题具有直接的参考价值。

**📖 中文摘要**

本文提出了TorchNWP，一个用于高效耦合人工智能组件和传统数值模型的编译库工具。它基于LibTorch，将PyTorch框架下的深度学习模型转换为静态二进制格式，并提供C/C++接口，从而允许在Fortran编写的数值模型中部署深度学习模型。在此基础上，该工具还在C/C++层面实现了基于神经网络的切线性模型和伴随模型，简化了四维变分同化系统的构建过程。该工具已应用于耦合基于深度学习的物理参数化方案（如辐射、非地形重力波拖曳）及其切线性/伴随模型的开发。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents TorchNWP, a compilation library tool for the efficient coupling of artificial intelligence components and traditional numerical models. It aims to address the issues of poor cross-language compatibility, insufficient coupling flexibility, and low data transfer efficiency between operational numerical models developed in Fortran and Python-based deep learning frameworks. Based on LibTorch, it optimizes and designs a unified application-layer calling interface, converts deep learning models under the PyTorch framework into a static binary format, and provides C/C++ interfaces. Then, using hybrid Fortran/C/C++ programming, it enables the deployment of deep learning models within numerical models. Integrating TorchNWP into a numerical model only requires compiling it into a callable link library and linking it during the compilation and linking phase to generate the executable. On this basis, tangent linear and adjoint model based on neural networks are implemented at the C/C++ level, which can shield the internal structure of neural network models and simplify the construction process of four-dimensional variational data assimilation systems. Meanwhile, it supports deployment on heterogeneous platforms, is compatible with mainstream neural network models, and enables mapping of different parallel granularities and efficient parallel execution. Using this tool requires minimal code modifications to the original numerical model, thus reducing coupling costs. It can be efficiently integrated into numerical weather prediction models such as CMA-GFS and MCV, and has been applied to the coupling of deep learning-based physical parameterization schemes (e.g., radiation, non-orographic gravity wave drag) and the development of their tangent linear and adjoint models, significantly improving the accuracy and efficiency of numerical weather prediction.

</details>

---

### 5. [Formal verification of tree-based machine learning models for lateral spreading](https://arxiv.org/abs/2603.16983)

**基本信息**

- 🔗 arXiv: [`2603.16983`](https://arxiv.org/abs/2603.16983)
- 👥 作者: Krishna Kumar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16983.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文研究如何确保机器学习模型（特别是树模型）的预测符合领域物理约束，这与构建可靠、可解释的“化学大模型”或“质谱结构推理”模型的目标高度一致。在化学领域，模型预测也需要符合化学规则（如价键规则、能量约束）。2) 工具资源相关：论文展示了一套将领域知识形式化并用于验证和修正机器学习模型的完整方法论和流程，这为化学信息学领域开发可信的AI模型提供了重要的方法学工具和思路。

**📖 中文摘要**

本文提出使用可满足性模理论（SMT）求解器对训练好的树集成模型（如XGBoost、可解释提升机EBM）进行形式化验证，以检查其在整个输入域上是否满足指定的物理约束（如单调性、安全性）。作者以2011年基督城地震侧向扩展数据集为例，将四个岩土工程规范编码为可判定的逻辑公式，并通过SMT求解器进行验证。该方法能够产生违反规范的具体反例，或证明不存在违规。通过迭代应用约束，可以逐步提高模型的物理一致性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning models for geotechnical hazard prediction can achieve high accuracy while learning physically inconsistent relationships from sparse or biased training data. Current remedies (post-hoc explainability, such as SHAP and LIME, and training-time constraints) either diagnose individual predictions approximately or restrict model capacity without providing exhaustive guarantees. This paper encodes trained tree ensembles as logical formulas in a Satisfiability Modulo Theories (SMT) solver and checks physical specifications across the entire input domain, not just sampled points. Four geotechnical specifications (water table depth, PGA monotonicity, distance safety, and flat-ground safety) are formalized as decidable logical formulas and verified via SMT against both XGBoost ensembles and Explainable Boosting Machines (EBMs) trained on the 2011 Christchurch earthquake lateral spreading dataset (7,291 sites, four features). The SMT solver either produces a concrete counterexample where a specification fails or proves that no violation exists. The unconstrained EBM (80.1% accuracy) violates all four specifications. A fully constrained EBM (67.2%) satisfies three of four specifications, demonstrating that iterative constraint application guided by verification can progressively improve physical consistency. A Pareto analysis of 33 model variants reveals a persistent trade-off, as none of the variants studied achieve both greater than 80% accuracy and full compliance with the specified set. SHAP analysis of specification counterexamples shows that the offending feature can rank last, demonstrating that post-hoc explanations do not substitute for formal verification. These results establish a verify-fix-verify engineering loop and a formal certification for deploying physically consistent ML models in safety-critical geotechnical applications.

</details>

---

### 6. [OpenQlaw: An Agentic AI Assistant for Analysis of 2D Quantum Materials](https://arxiv.org/abs/2603.17043)

**基本信息**

- 🔗 arXiv: [`2603.17043`](https://arxiv.org/abs/2603.17043)
- 👥 作者: Sankalp Pandey, Xuan-Bac Nguyen, Hoang-Quan Nguyen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17043.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于材料科学（具体是二维量子材料分析）的智能体AI助手。这直接属于“化学大模型”在具体科学领域（材料化学）的应用范畴。OpenQlaw架构中利用领域专家MLLM进行视觉特征提取和物理感知推理，并由核心LLM智能体进行任务编排和自然语言交互，展示了如何将大模型能力与领域知识结合来解决复杂的化学/材料科学问题，为化学信息学中的智能分析系统设计提供了参考案例。

**📖 中文摘要**

本文介绍了OpenQlaw，一个用于分析二维量子材料的智能体编排系统。该系统基于轻量级智能体框架NanoBot和物理感知多模态平台QuPAINT构建。OpenQlaw允许核心大型语言模型（LLM）智能体将QuPAINT（一个用于量子材料发现的领域专家多模态大模型）作为专用节点进行编排，成功地将视觉识别与推理和解耦。智能体可以解析来自专家的空间数据，动态处理用户查询（如执行尺度感知的物理计算或生成孤立的视觉注释），并以自然的方式回答。系统具有持久记忆，可以保存物理尺度比例和样品制备方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The transition from optical identification of 2D quantum materials to practical device fabrication requires dynamic reasoning beyond the detection accuracy. While recent domain-specific Multimodal Large Language Models (MLLMs) successfully ground visual features using physics-informed reasoning, their outputs are optimized for step-by-step cognitive transparency. This yields verbose candidate enumerations followed by dense reasoning that, while accurate, may induce cognitive overload and lack immediate utility for real-world interaction with researchers. To address this challenge, we introduce OpenQlaw, an agentic orchestration system for analyzing 2D materials. The architecture is built upon NanoBot, a lightweight agentic framework inspired by OpenClaw, and QuPAINT, one of the first Physics-Aware Instruction Multi-modal platforms for Quantum Material Discovery. This allows accessibility to the lab floor via a variety of messaging channels. OpenQlaw allows the core Large Language Model (LLM) agent to orchestrate a domain-expert MLLM,with QuPAINT, as a specialized node, successfully decoupling visual identification from reasoning and deterministic image rendering. By parsing spatial data from the expert, the agent can dynamically process user queries, such as performing scale-aware physical computation or generating isolated visual annotations, and answer in a naturalistic manner. Crucially, the system features a persistent memory that enables the agent to save physical scale ratios (e.g., 1 pixel = 0.25 {\mu}m) for area computations and store sample preparation methods for efficacy comparison. The application of an agentic architecture, together with the extension that uses the core agent as an orchestrator for domain-specific experts, transforms isolated inferences into a context-aware assistant capable of accelerating high-throughput device fabrication.

</details>

---

### 7. [Early Quantization Shrinks Codebook: A Simple Fix for Diversity-Preserving Tokenization](https://arxiv.org/abs/2603.17052)

**基本信息**

- 🔗 arXiv: [`2603.17052`](https://arxiv.org/abs/2603.17052)
- 👥 作者: Wenhao Zhao, Qiran Zou, Rushi Shah 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17052.pdf)

**💡 相关性分析**

满足标准1和3：1) 核心主题相关：向量量化是许多生成模型（包括一些化学大模型和光谱生成模型）中用于离散化连续表示的关键技术。论文深入研究了该技术的内在问题（表征崩溃），这对于构建稳定、高效的化学表示学习模型至关重要。2) 综述展望相关：论文对向量量化中的崩溃问题进行了系统性的首次全面研究，分析了其原因并提出了解决方案方向，这属于对底层技术的重要探讨和展望，对相关领域的研究者有指导意义。

**📖 中文摘要**

本文系统研究了生成模型中向量量化的表征崩溃问题。通过合成和真实数据集，作者识别了两种崩溃类型（令牌崩溃和嵌入崩溃）及其触发条件。分析表明，随机初始化和有限的编码器容量会导致令牌和嵌入的崩溃。基于这些发现，作者提出了缓解每种崩溃的潜在解决方案。据作者所知，这是首个全面研究向量量化中表征崩溃问题的工作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vector quantization is a technique in machine learning that discretizes continuous representations into a set of discrete vectors. It is widely employed in tokenizing data representations for large language models, diffusion models, and other generative models. Despite its prevalence, the characteristics and behaviors of vector quantization in generative models remain largely underexplored. In this study, we systematically investigate the issue of collapses in vector quantization, where collapsed representations are observed across discrete codebook tokens and continuous latent embeddings. By leveraging both synthetic and real datasets, we identify the severity of each type of collapses and triggering conditions. Our analysis reveals that random initialization and limited encoder capacity result in tokens collapse and embeddings collapse. Building on these findings, we propose potential solutions aimed at mitigating each collapse. To the best of our knowledge, this is the first comprehensive study examining representation collapsing problems in vector quantization.

</details>

---

### 8. [Transformers are Bayesian Networks](https://arxiv.org/abs/2603.17063)

**基本信息**

- 🔗 arXiv: [`2603.17063`](https://arxiv.org/abs/2603.17063)
- 👥 作者: Gregory Coppola
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17063.pdf)

**💡 相关性分析**

满足标准3：论文是对Transformer模型底层工作机制的重要理论探讨和解释，将其与贝叶斯网络和信念传播联系起来。这属于对“大模型”核心架构的基础性、展望性讨论。虽然不直接针对化学或质谱，但对任何领域（包括化学信息学）想要深入理解、改进或理论化其使用的大模型（如化学LLM、光谱Transformer）的研究者来说，这篇论文提供了深刻的理论视角和解释框架。

**📖 中文摘要**

本文从贝叶斯网络的角度为Transformer的工作原理提供了一个精确的解释。作者通过五种方式证明：Transformer（具体是Sigmoid Transformer）在其隐式因子图上实现了加权循环信念传播；Transformer可以实现任何声明知识库上的精确信念传播；产生精确后验的Sigmoid Transformer必然具有信念传播的权重；Transformer层的AND/OR布尔结构精确对应了Pearl的收集/更新算法；并通过实验证实了所有形式结果。论文进一步指出，可验证的推理需要一个有限的概念空间，没有 grounding，正确性就无法定义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transformers are the dominant architecture in AI, yet why they work remains poorly understood. This paper offers a precise answer: a transformer is a Bayesian network. We establish this in five ways. First, we prove that every sigmoid transformer with any weights implements weighted loopy belief propagation on its implicit factor graph. One layer is one round of BP. This holds for any weights -- trained, random, or constructed. Formally verified against standard mathematical axioms. Second, we give a constructive proof that a transformer can implement exact belief propagation on any declared knowledge base. On knowledge bases without circular dependencies this yields provably correct probability estimates at every node. Formally verified against standard mathematical axioms. Third, we prove uniqueness: a sigmoid transformer that produces exact posteriors necessarily has BP weights. There is no other path through the sigmoid architecture to exact posteriors. Formally verified against standard mathematical axioms. Fourth, we delineate the AND/OR boolean structure of the transformer layer: attention is AND, the FFN is OR, and their strict alternation is Pearl's gather/update algorithm exactly. Fifth, we confirm all formal results experimentally, corroborating the Bayesian network characterization in practice. We also establish the practical viability of loopy belief propagation despite the current lack of a theoretical convergence guarantee. We further prove that verifiable inference requires a finite concept space. Any finite verification procedure can distinguish at most finitely many concepts. Without grounding, correctness is not defined. Hallucination is not a bug that scaling can fix. It is the structural consequence of operating without concepts. Formally verified against standard mathematical axioms.

</details>

---

### 9. [PRISM: Demystifying Retention and Interaction in Mid-Training](https://arxiv.org/abs/2603.17074)

**基本信息**

- 🔗 arXiv: [`2603.17074`](https://arxiv.org/abs/2603.17074)
- 👥 作者: Bharat Runwal, Ashish Agrawal, Anurag Roy 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17074.pdf)

**💡 相关性分析**

满足标准3：论文是对大语言模型训练策略（特别是中训练）的系统性实证研究和分析。这属于对“大模型”如何有效训练和提升能力（尤其是科学推理能力）的重要方法论探讨和展望。对于旨在构建具有强大推理能力的“化学大模型”或“质谱结构推理”模型的研究者而言，PRISM中关于数据组合、中训练与RL分工的发现具有重要的借鉴和指导意义。

**📖 中文摘要**

本文提出了PRISM，一项关于大语言模型中训练（mid-training）设计选择的综合性实证研究。通过控制实验，作者表明，在约270亿高质量token上进行中训练，能在数学、代码和科学基准上带来一致的性能提升，同时保持通用性能。研究的关键发现是：数据组合在中训练中最为重要，而不是后续的强化学习（RL）；中训练密集地重构了超过90%的模型权重，而RL只对约5%的参数进行稀疏、前载的 refinement；中训练将模型置于一个RL可以有效改进性能的配置中。这些结果为设计可靠的中训练流程提供了实用指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present PRISM, a comprehensive empirical study of mid-training design choices for large language models. Through controlled experiments across seven base models spanning four families (Granite, LLaMA, Mistral, Nemotron-H), two architecture types (dense Transformer and attention-Mamba hybrid), and scales from 3B to 24B parameters, we show that mid-training on approximately 27B high-quality tokens yields consistent gains of +15 to +40 points on math, +5 to +12 points on code, and +6 to +13 points on science benchmarks while preserving general performance. The full PRISM to RL pipeline improves macro-average across six reasoning benchmarks from under 12 to 29-42 (a 3-4x improvement), whereas RL applied directly to most of the base models remains substantially less effective, with AIME scores near zero. Data composition matters most at mid-training, not RL: including science data during mid-training unlocks +17 to +28 point GPQA-Diamond gains during RL, while changing the RL mix produces less than 2 point differences. Mechanistically, mid-training densely restructures over 90% of model weights, while RL makes sparse, front-loaded refinements to approximately 5% of parameters. Representation analysis (CKA) confirms that RL consistently preserves mid-training's representational geometry (over 0.998 CKA) across architectures. Crucially, RL applies identical weight changes regardless of starting point, yet only succeeds on mid-trained models, consistent with mid-training placing the model in a configuration from which RL can effectively improve performance. Our results demonstrate that retention-aware mid-training is highly effective for reliable reasoning enhancement and provide practical guidance for designing robust mid-training pipelines.

</details>

---

### 10. [ACE-LoRA: Graph-Attentive Context Enhancement for Parameter-Efficient Adaptation of Medical Vision-Language Models](https://arxiv.org/abs/2603.17079)

**基本信息**

- 🔗 arXiv: [`2603.17079`](https://arxiv.org/abs/2603.17079)
- 👥 作者: M. Arda Aydın, Melih B. Yilmaz, Aykut Koç 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17079.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文研究如何对预训练的多模态大模型（VLM）进行参数高效的领域适应（医学影像）。这直接与“化学大模型”的主题相关，因为化学领域同样面临如何将通用大模型（或预训练的化学模型）高效适配到特定子任务（如某种特定类型的质谱解析或分子性质预测）的问题。2) 方法资源相关：论文提出的ACE-LoRA框架（结合LoRA、超图网络和特定损失函数）为多模态大模型的领域微调提供了一个新颖且有效的工具方法，可供化学信息学领域参考。

**📖 中文摘要**

本文提出了ACE-LoRA，一个用于通用医学视觉-语言模型（VLM）的参数高效适应框架。ACE-LoRA将低秩适应（LoRA）模块集成到冻结的图像-文本编码器中，并引入了一个基于注意力的上下文增强超图神经网络（ACE-HGNN）模块，该模块捕获超越成对相似性的高阶上下文交互，以用局部诊断线索丰富全局表示。此外，还制定了一个标签引导的InfoNCE损失来增强跨模态对齐。尽管只增加了0.95M可训练参数，ACE-LoRA在跨多个领域的零样本分类、分割和检测基准上 consistently 优于最先进的医学VLM和PEFT基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of CLIP-like vision-language models (VLMs) on natural images has inspired medical counterparts, yet existing approaches largely fall into two extremes: specialist models trained on single-domain data, which capture domain-specific details but generalize poorly, and generalist medical VLMs trained on multi-domain data, which retain broad semantics but dilute fine-grained diagnostic cues. Bridging this specialization-generalization trade-off remains challenging. To address this problem, we propose ACE-LoRA, a parameter-efficient adaptation framework for generalist medical VLMs that maintains robust zero-shot generalization. ACE-LoRA integrates Low-Rank Adaptation (LoRA) modules into frozen image-text encoders and introduces an Attention-based Context Enhancement Hypergraph Neural Network (ACE-HGNN) module that captures higher-order contextual interactions beyond pairwise similarity to enrich global representations with localized diagnostic cues, addressing a key limitation of prior Parameter-Efficient Fine-Tuning (PEFT) methods that overlook fine-grained details. To further enhance cross-modal alignment, we formulate a label-guided InfoNCE loss to effectively suppress false negatives between semantically related image-text pairs. Despite adding only 0.95M trainable parameters, ACE-LoRA consistently outperforms state-of-the-art medical VLMs and PEFT baselines across zero-shot classification, segmentation, and detection benchmarks spanning multiple domains. Our code is available at this https URL .

</details>

---

### 11. [Synchronized DNA sources for unconditionally secure cryptography](https://arxiv.org/abs/2603.17149)

**基本信息**

- 🔗 arXiv: [`2603.17149`](https://arxiv.org/abs/2603.17149)
- 👥 作者: Sandra Jaudou, Hélène Gasnier, Elias Boudjella 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17149.pdf)

**💡 相关性分析**

满足标准2：论文提出并实验验证了一种基于DNA分子的、用于生成加密密钥的同步熵源系统和协议。这提供了一种新颖的、物理的“分子数据”生成和处理资源。虽然应用场景是密码学而非质谱分析，但其利用分子实体编码和处理信息的核心方法与“质谱结构推理”中从分子数据（质谱）中提取信息（结构）在概念上相关，可视为一种广义的分子信息学工具或资源。

**📖 中文摘要**

本文介绍了一种基于DNA的密码学原语，利用合成DNA的随机池在远距离双方之间建立同步的熵源。该协议使用包含随机索引-有效载荷对的重复DNA分子作为共享秘密。这些分子在本地进行测序和数字化，生成用于一次性密码本（OTP）加密的通用二进制掩码，从而在不依赖计算假设的情况下实现无条件安全。作者在东京和巴黎之间进行了实验演示，生成了约400 Mb的共享秘密掩码。该系统可以抵抗两种类型的对抗性干扰。这项工作将分子生物学与密码学相结合，为全球通信网络中的无条件安全开辟了一条新途径。虽然论文主要关注密码学，但其核心技术创新是使用DNA作为可扩展的、物理的随机熵源来生成加密密钥。这种利用分子（DNA）特性生成和处理信息（密钥）的思路，与利用分子（质谱）数据推理结构（质谱结构推理）在方法论层面有相似之处，都属于“分子信息学”的交叉领域。论文提出的DNA分子作为信息载体的系统，也可以被视为一种特殊的、用于安全通信的“分子数据资源”。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Secure communication is the cornerstone of modern infrastructures, yet achieving unconditional security -resistant to any computational attack- remains a fundamental challenge. The One-Time Pad (OTP), proven by Shannon to offer perfect secrecy, requires a shared random key as long as the message, used only once. However, distributing large keys over long distances has been impractical due to the lack of secure and scalable sharing options. Here, we introduce a DNA-based cryptographic primitive that leverages random pools of synthetic DNA to install a synchronized entropy source between distant parties. Our approach uses duplicated DNA molecules -comprising random index-payload pairs- as a shared secret. These molecules are locally sequenced and digitized to generate a common binary mask for OTP encryption, achieving unconditional security without relying on computational assumptions. We experimentally demonstrate this protocol between Tokyo and Paris, using in-house sequencing, generating a shared secret mask of $\sim$ 400 Mb with a residual error rate to achieve the usual overall decryption failure rate of $2^{-128}$. The min-entropy of the binary mask meets the most recent National Institute of Standards and Technology requirements (SP 800-90B), and is comparable to that of approved cryptographic random number generators. Critically, our system can resist two types of adversarial interference through molecular copy-number statistics, providing an additional layer of security reminiscent of Quantum Key Distribution, but without distance limitations. This work establishes DNA as a scalable entropy source for long-distance OTP, enabling high-throughput and secure communications in sensitive contexts. By bridging molecular biology and cryptography, DNA-based key distribution opens a promising new route toward unconditional security in global communication networks.

</details>

---

### 12. [Self-Conditioned Denoising for Atomistic Representation Learning](https://arxiv.org/abs/2603.17196)

**基本信息**

- 🔗 arXiv: [`2603.17196`](https://arxiv.org/abs/2603.17196)
- 👥 作者: Tynan Perez, Rafael Gomez-Bombarelli
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17196.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于原子表示学习的自监督预训练方法（SCD），旨在为物理科学构建基础模型，这直接与“化学大模型”这一关注主题相关。

**📖 中文摘要**

本文提出了一种名为自条件去噪（SCD）的原子表示学习预训练策略。该方法是骨干网络无关的，旨在为化学和材料科学领域构建基础模型。SCD利用原子数据的自嵌入进行跨域条件去噪，其训练数据域包括小分子、蛋白质、周期性材料和非平衡几何结构。论文表明，在控制骨干架构和预训练数据集的情况下，SCD在下游基准测试中显著优于先前的自监督学习方法，并与基于DFT力-能量标签的大规模监督预训练性能相当或更优。这项工作直接针对化学信息学中构建化学大模型的核心挑战，即开发有效的、可扩展的预训练策略，以学习通用的原子级表示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of large-scale pretraining in NLP and computer vision has catalyzed growing efforts to develop analogous foundation models for the physical sciences. However, pretraining strategies using atomistic data remain underexplored. To date, large-scale supervised pretraining on DFT force-energy labels has provided the strongest performance gains to downstream property prediction, out-performing existing methods of self-supervised learning (SSL) which remain limited to ground-state geometries, and/or single domains of atomistic data. We address these shortcomings with Self-Conditioned Denoising (SCD), a backbone-agnostic reconstruction objective that utilizes self-embeddings for conditional denoising across any domain of atomistic data, including small molecules, proteins, periodic materials, and 'non-equilibrium' geometries. When controlled for backbone architecture and pretraining dataset, SCD significantly outperforms previous SSL methods on downstream benchmarks and matches or exceeds the performance of supervised force-energy pretraining. We show that a small, fast GNN pretrained by SCD can achieve competitive or superior performance to larger models pretrained on significantly larger labeled or unlabeled datasets, across tasks in multiple domains. Our code is available at: this https URL

</details>

---

### 13. [Binary Latent Protein Fitness Landscapes for Quantum Annealing Optimization](https://arxiv.org/abs/2603.17247)

**基本信息**

- 🔗 arXiv: [`2603.17247`](https://arxiv.org/abs/2603.17247)
- 👥 作者: Truong-Son Hy
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17247.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于预训练蛋白质语言模型和组合优化的框架（Q-BIOLAT）来建模和优化蛋白质适应度图谱，这直接属于“化学大模型”在蛋白质工程领域的应用。

**📖 中文摘要**

本文提出了Q-BIOLAT框架，用于在二进制潜在空间中建模和优化蛋白质适应度图谱。该方法利用预训练的蛋白质语言模型获得连续嵌入，然后将其转换为紧凑的二进制潜在表示。在该空间中，蛋白质适应度使用二次无约束二进制优化（QUBO）模型进行近似，从而能够通过模拟退火和遗传算法等经典启发式方法进行高效的组合搜索。在ProteinGym基准测试上的结果表明，Q-BIOLAT能够捕捉蛋白质适应度图谱中有意义的结构，并能够识别高适应度变体。该框架在蛋白质表示学习和组合优化之间建立了桥梁，通过将蛋白质适应度表述为QUBO问题，为量子辅助蛋白质工程开辟了新方向。这项工作属于利用机器学习模型（特别是大语言模型）进行蛋白质工程和性质预测的范畴，是化学信息学和生物信息学中“化学大模型”应用的一个重要方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose Q-BIOLAT, a framework for modeling and optimizing protein fitness landscapes in binary latent spaces. Starting from protein sequences, we leverage pretrained protein language models to obtain continuous embeddings, which are then transformed into compact binary latent representations. In this space, protein fitness is approximated using a quadratic unconstrained binary optimization (QUBO) model, enabling efficient combinatorial search via classical heuristics such as simulated annealing and genetic algorithms. On the ProteinGym benchmark, we demonstrate that Q-BIOLAT captures meaningful structure in protein fitness landscapes and enables the identification of high-fitness variants. Despite using a simple binarization scheme, our method consistently retrieves sequences whose nearest neighbors lie within the top fraction of the training fitness distribution, particularly under the strongest configurations. We further show that different optimization strategies exhibit distinct behaviors, with evolutionary search performing better in higher-dimensional latent spaces and local search remaining competitive in preserving realistic sequences. Beyond its empirical performance, Q-BIOLAT provides a natural bridge between protein representation learning and combinatorial optimization. By formulating protein fitness as a QUBO problem, our framework is directly compatible with emerging quantum annealing hardware, opening new directions for quantum-assisted protein engineering. Our implementation is publicly available at: this https URL

</details>

---

### 14. [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](https://arxiv.org/abs/2603.17380)

**基本信息**

- 🔗 arXiv: [`2603.17380`](https://arxiv.org/abs/2603.17380)
- 👥 作者: Shuizhou Chen, Lang Yu, Kedu Jin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17380.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于预测细胞对化学或遗传扰动反应的大规模基础模型，这直接与化学信息学中利用大模型进行预测和推理的主题相关。

**📖 中文摘要**

本文提出了SCALE，一个用于虚拟细胞扰动预测的大规模基础模型。该模型将扰动预测表述为条件传输问题，并使用基于集合的流架构实现，该架构将基于LLaMA的细胞编码与面向端点的监督相结合。这项工作与化学信息学中构建用于预测化学或遗传扰动的计算模型高度相关，特别是与“化学大模型”主题相关，因为它描述了一个用于大规模生物化学数据（单细胞测量）的专用基础模型。该模型旨在预测细胞对扰动的反应，这类似于化学信息学中预测分子性质或反应的任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Virtual cell models aim to enable in silico experimentation by predicting how cells respond to genetic, chemical, or cytokine perturbations from single-cell measurements. In practice, however, large-scale perturbation prediction remains constrained by three coupled bottlenecks: inefficient training and inference pipelines, unstable modeling in high-dimensional sparse expression space, and evaluation protocols that overemphasize reconstruction-like accuracy while underestimating biological fidelity. In this work we present a specialized large-scale foundation model SCALE for virtual cell perturbation prediction that addresses the above limitations jointly. First, we build a BioNeMo-based training and inference framework that substantially improves data throughput, distributed scalability, and deployment efficiency, yielding 12.51* speedup on pretrain and 1.29* on inference over the prior SOTA pipeline under matched system settings. Second, we formulate perturbation prediction as conditional transport and implement it with a set-aware flow architecture that couples LLaMA-based cellular encoding with endpoint-oriented supervision. This design yields more stable training and stronger recovery of perturbation effects. Third, we evaluate the model on Tahoe-100M using a rigorous cell-level protocol centered on biologically meaningful metrics rather than reconstruction alone. On this benchmark, our model improves PDCorr by 12.02% and DE Overlap by 10.66% over STATE. Together, these results suggest that advancing virtual cells requires not only better generative objectives, but also the co-design of scalable infrastructure, stable transport modeling, and biologically faithful evaluation.

</details>

---

### 15. [Cohomological Obstructions to Global Counterfactuals: A Sheaf-Theoretic Foundation for Generative Causal Models](https://arxiv.org/abs/2603.17384)

**基本信息**

- 🔗 arXiv: [`2603.17384`](https://arxiv.org/abs/2603.17384)
- 👥 作者: Rui Wu, Hong Xie, Yongjun Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17384.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为生成因果模型提供理论基础，这直接关系到构建能够进行复杂推理（如反事实预测）的“化学大模型”的能力和局限性。

**📖 中文摘要**

本文为生成因果模型提供了一个层论基础。它将结构因果模型形式化为Wasserstein空间上的胞腔层，并提供了测度空间中同调障碍的严格代数拓扑定义。为了确保计算可处理性并避免确定性奇点，作者引入了熵正则化并推导了熵Wasserstein因果层拉普拉斯算子。该框架旨在解决当因果图表现出非平凡同调时，局部一致的因果机制无法自然产生全局连贯反事实的问题。这项工作与“化学大模型”主题相关，因为它为理解生成模型（如扩散模型）在因果推理中的局限性提供了理论基础，这对于构建能够进行可靠反事实推理的化学大模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current continuous generative models (e.g., Diffusion Models, Flow Matching) implicitly assume that locally consistent causal mechanisms naturally yield globally coherent counterfactuals. In this paper, we prove that this assumption fails fundamentally when the causal graph exhibits non-trivial homology (e.g., structural conflicts or hidden confounders). We formalize structural causal models as cellular sheaves over Wasserstein spaces, providing a strict algebraic topological definition of cohomological obstructions in measure spaces. To ensure computational tractability and avoid deterministic singularities (which we define as manifold tearing), we introduce entropic regularization and derive the Entropic Wasserstein Causal Sheaf Laplacian, a novel system of coupled non-linear Fokker-Planck equations. Crucially, we prove an entropic pullback lemma for the first variation of pushforward measures. By integrating this with the Implicit Function Theorem (IFT) on Sinkhorn optimality conditions, we establish a direct algorithmic bridge to automatic differentiation (VJP), achieving O(1)-memory reverse-mode gradients strictly independent of the iteration horizon. Empirically, our framework successfully leverages thermodynamic noise to navigate topological barriers ("entropic tunneling") in high-dimensional scRNA-seq counterfactuals. Finally, we invert this theoretical framework to introduce the Topological Causal Score, demonstrating that our Sheaf Laplacian acts as a highly sensitive algebraic detector for topology-aware causal discovery.

</details>

---

### 16. [The Causal Uncertainty Principle: Manifold Tearing and the Topological Limits of Counterfactual Interventions](https://arxiv.org/abs/2603.17385)

**基本信息**

- 🔗 arXiv: [`2603.17385`](https://arxiv.org/abs/2603.17385)
- 👥 作者: Rui Wu, Hong Xie, Yongjun Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17385.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索连续生成模型中因果干预的几何限制，这直接关系到“化学大模型”在进行分子设计、性质预测等反事实推理时的可靠性和能力边界。

**📖 中文摘要**

本文研究了连续生成模型中因果干预的基本限制。作者定义了反事实事件视界并证明了流形撕裂定理：确定性流在极端干预下不可避免地会产生有限时间奇点。他们还建立了因果不确定性原理，用于权衡干预极端性与身份保持。这项工作与“化学大模型”主题相关，因为它探讨了生成模型（如用于分子设计的模型）在进行因果干预（例如，改变分子结构以预测性质）时可能遇到的根本性几何挑战。这对于开发可靠且可解释的化学大模型具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Judea Pearl's do-calculus provides a foundation for causal inference, but its translation to continuous generative models remains fraught with geometric challenges. We establish the fundamental limits of such interventions. We define the Counterfactual Event Horizon and prove the Manifold Tearing Theorem: deterministic flows inevitably develop finite-time singularities under extreme interventions. We establish the Causal Uncertainty Principle for the trade-off between intervention extremity and identity preservation. Finally, we introduce Geometry-Aware Causal Flow (GACF), a scalable algorithm that utilizes a topological radar to bypass manifold tearing, validated on high-dimensional scRNA-seq data.

</details>

---

### 17. [Causal Representation Learning on High-Dimensional Data: Benchmarks, Reproducibility, and Evaluation Metrics](https://arxiv.org/abs/2603.17405)

**基本信息**

- 🔗 arXiv: [`2603.17405`](https://arxiv.org/abs/2603.17405)
- 👥 作者: Alireza Sadeghi, Wael AbdAlmageed
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17405.pdf)

**💡 相关性分析**

满足标准1和标准3：论文的核心研究内容（因果表示学习）是构建能够进行推理和反事实预测的化学大模型的基础。同时，该论文是一篇综述/展望类论文，系统性地评估了该领域的现状、挑战和评估方法，包含重要的相关讨论。

**📖 中文摘要**

本文对高维数据的因果表示学习进行了基准测试、可重复性和评估指标的综述。因果表示学习模型旨在将高维数据转换到潜在空间，从而能够基于潜在变量之间的因果关系进行干预，以生成反事实样本或修改现有数据。作者批判性地分析了文献中使用的合成和真实世界数据集，强调了它们的局限性，并提出了适用于CRL模型开发的数据集应具备的基本特征。这项工作与“化学大模型”和“质谱结构推理”都相关，因为因果表示学习是构建能够理解分子结构-性质关系并进行反事实推理的化学大模型的关键技术。同时，从复杂质谱数据中推断分子结构也可以被视为一个因果表示学习问题。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Causal representation learning (CRL) models aim to transform high-dimensional data into a latent space, enabling interventions to generate counterfactual samples or modify existing data based on the causal relationships among latent variables. To facilitate the development and evaluation of these models, a variety of synthetic and real-world datasets have been proposed, each with distinct advantages and limitations. For practical applications, CRL models must perform robustly across multiple evaluation directions, including reconstruction, disentanglement, causal discovery, and counterfactual reasoning, using appropriate metrics for each direction. However, this multi-directional evaluation can complicate model comparison, as a model may excel in some direction while under-performing in others. Another significant challenge in this field is reproducibility: the source code corresponding to published results must be publicly available, and repeated runs should yield performance consistent with the original reports. In this study, we critically analyzed the synthetic and real-world datasets currently employed in the literature, highlighting their limitations and proposing a set of essential characteristics for suitable datasets in CRL model development. We also introduce a single aggregate metric that consolidates performance across all evaluation directions, providing a comprehensive score for each model. Finally, we reviewed existing implementations from the literature and assessed them in terms of reproducibility, identifying gaps and best practices in the field.

</details>

---

### 18. [Joint Degradation-Aware Arbitrary-Scale Super-Resolution for Variable-Rate Extreme Image Compression](https://arxiv.org/abs/2603.17408)

**基本信息**

- 🔗 arXiv: [`2603.17408`](https://arxiv.org/abs/2603.17408)
- 👥 作者: Xinning Chai, Zhengxue Cheng, Xin Li 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17408.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于扩散模型的生成框架和条件生成思想，与“化学大模型”中利用生成模型（如扩散模型）进行分子设计、构象生成等任务在方法论上核心相关。

**📖 中文摘要**

本文提出了ASSR-EIC，一个利用任意尺度超分辨率支持可变速率极端图像压缩的新框架。虽然主要应用在图像压缩，但其核心方法——利用扩散模型先验进行率自适应重建——与化学信息学中利用生成模型（如扩散模型）进行分子生成或性质预测有概念上的相似性。论文中提到的“压缩-重缩放感知扩散先验”用于指导重建，这种利用条件生成模型处理多尺度、多任务问题的思路，可以类比于化学中处理不同精度或条件下的分子表示与生成。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent diffusion-based extreme image compression methods have demonstrated remarkable performance at ultra-low bitrates. However, most approaches require training separate diffusion models for each target bitrate, resulting in substantial computational overhead and hindering practical deployment. Meanwhile, recent studies have shown that joint super-resolution can serve as an effective approach for enhancing low-bitrate reconstruction. However, when moving toward ultra-low bitrate regimes, these methods struggle due to severe information loss, and their reliance on fixed super-resolution scales prevents flexible adaptation across diverse bitrates. To address these limitations, we propose ASSR-EIC, a novel image compression framework that leverages arbitrary-scale super-resolution (ASSR) to support variable-rate extreme image compression (EIC). An arbitrary-scale downsampling module is introduced at the encoder side to provide controllable rate reduction, while a diffusion-based, joint degradation-aware ASSR decoder enables rate-adaptive reconstruction within a single model. We exploit the compression- and rescaling-aware diffusion prior to guide the reconstruction, yielding high fidelity and high realism restoration across diverse compression and rescaling settings. Specifically, we design a global compression-rescaling adaptor that offers holistic guidance for rate adaptation, and a local compression-rescaling modulator that dynamically balances generative and fidelity-oriented behaviors to achieve fine-grained, bitrate-adaptive detail restoration. To further enhance reconstruction quality, we introduce a dual semantic-enhanced design. Extensive experiments demonstrate that ASSR-EIC delivers state-of-the-art performance in extreme image compression while simultaneously supporting flexible bitrate control and adaptive rate-dependent reconstruction.

</details>

---

### 19. [Mutually Causal Semantic Distillation Network for Zero-Shot Learning](https://arxiv.org/abs/2603.17412)

**基本信息**

- 🔗 arXiv: [`2603.17412`](https://arxiv.org/abs/2603.17412)
- 👥 作者: Shiming Chen, Shuhuang Chen, Guo-Sen Xie 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17412.pdf)

**💡 相关性分析**

满足标准1：论文提出的相互因果语义蒸馏框架，其核心是学习跨模态（视觉-属性）的可靠因果关联，这种方法论可以直接迁移并应用于“质谱结构推理”任务，即建立质谱信号（视觉/信号模态）与分子结构（属性/语义模态）之间的因果推理模型。

**📖 中文摘要**

本文提出了MSDN++，一个用于零样本学习的相互因果语义蒸馏网络。该网络包含两个相互的因果注意力子网，分别学习基于属性的视觉特征和基于视觉的属性特征，并通过语义蒸馏损失进行协作学习。虽然应用在计算机视觉的零样本学习，但其核心思想——通过因果注意力机制学习视觉和属性特征之间可靠的、具有因果关系的关联——与“质谱结构推理”高度相关。在质谱结构推理中，目标是从质谱数据（视觉/信号特征）中推断出分子结构（属性/语义特征），这同样需要建立信号与结构之间的可靠、可解释的映射关系。MSDN++的相互因果蒸馏框架为解决质谱信号与分子结构之间的复杂、模糊关联提供了新颖的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Zero-shot learning (ZSL) aims to recognize the unseen classes in the open-world guided by the side-information (e.g., attributes). Its key task is how to infer the latent semantic knowledge between visual and attribute features on seen classes, and thus conducting a desirable semantic knowledge transfer from seen classes to unseen ones. Prior works simply utilize unidirectional attention within a weakly-supervised manner to learn the spurious and limited latent semantic representations, which fail to effectively discover the intrinsic semantic knowledge (e.g., attribute semantic) between visual and attribute features. To solve the above challenges, we propose a mutually causal semantic distillation network (termed MSDN++) to distill the intrinsic and sufficient semantic representations for ZSL. MSDN++ consists of an attribute$\rightarrow$visual causal attention sub-net that learns attribute-based visual features, and a visual$\rightarrow$attribute causal attention sub-net that learns visual-based attribute features. The causal attentions encourages the two sub-nets to learn causal vision-attribute associations for representing reliable features with causal visual/attribute learning. With the guidance of semantic distillation loss, the two mutual attention sub-nets learn collaboratively and teach each other throughout the training process. Extensive experiments on three widely-used benchmark datasets (e.g., CUB, SUN, AWA2, and FLO) show that our MSDN++ yields significant improvements over the strong baselines, leading to new state-of-the-art performances.

</details>

---

### 20. [Physics-informed Deep Mixture-of-Koopmans Vehicle Dynamics Model with Dual-branch Encoder for Distributed Electric-drive Trucks](https://arxiv.org/abs/2603.17416)

**基本信息**

- 🔗 arXiv: [`2603.17416`](https://arxiv.org/abs/2603.17416)
- 👥 作者: Jinyu Miao, Pu Zhang, Rujun Yan 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17416.pdf)

**💡 相关性分析**

满足标准1：论文核心研究的Koopman算子理论和混合Koopman框架，是一种用于非线性系统建模和表示学习的先进方法，该方法可以应用于化学领域，例如从分子动力学数据中学习有效的表示，从而与“化学大模型”中处理复杂化学系统的主题相关。

**📖 中文摘要**

本文提出了一种用于复杂分布式电驱动卡车的完全数据驱动的动力学建模方法，该方法基于Koopman算子理论，将高度非线性的动力学表示在提升的线性嵌入空间中。为了适应卡车的多种驾驶模式，作者将普通的Koopman算子扩展为混合Koopman算子框架。这项工作与“化学大模型”相关，因为Koopman算子理论是一种强大的系统辨识和降维技术，可用于从高维时间序列数据（如分子动力学模拟轨迹）中学习可解释的线性表示。这种技术对于构建能够理解和预测复杂分子系统动态行为的化学大模型具有潜在价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advanced autonomous driving systems require accurate vehicle dynamics modeling. However, identifying a precise dynamics model remains challenging due to strong nonlinearities and the coupled longitudinal and lateral dynamic characteristics. Previous research has employed physics-based analytical models or neural networks to construct vehicle dynamics representations. Nevertheless, these approaches often struggle to simultaneously achieve satisfactory performance in terms of system identification efficiency, modeling accuracy, and compatibility with linear control strategies. In this paper, we propose a fully data-driven dynamics modeling method tailored for complex distributed electric-drive trucks (DETs), leveraging Koopman operator theory to represent highly nonlinear dynamics in a lifted linear embedding space. To achieve high-precision modeling, we first propose a novel dual-branch encoder which encodes dynamic states and provides a powerful basis for the proposed Koopman-based methods entitled KODE. A physics-informed supervision mechanism, grounded in the geometric consistency of temporal vehicle motion, is incorporated into the training process to facilitate effective learning of both the encoder and the Koopman operator. Furthermore, to accommodate the diverse driving patterns of DETs, we extend the vanilla Koopman operator to a mixture-of-Koopman operator framework, enhancing modeling capability. Simulations conducted in a high-fidelity TruckSim environment and real-world experiments demonstrate that the proposed approach achieves state-of-the-art performance in long-term dynamics state estimation.

</details>

---

### 21. [Argument Reconstruction as Supervision for Critical Thinking in LLMs](https://arxiv.org/abs/2603.17432)

**基本信息**

- 🔗 arXiv: [`2603.17432`](https://arxiv.org/abs/2603.17432)
- 👥 作者: Hyun Ryu, Gyouk Chu, Gregor Betz 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17432.pdf)

**💡 相关性分析**

满足标准1和标准2：论文的核心研究内容（论证重构作为监督）旨在提升LLM的逻辑推理能力，这直接关系到构建具有强大推理能力的“化学大模型”。同时，论文提出了一个新的数据集（Arguinas），这满足了标准2中“提供了可用于这些主题的数据集”的条件。

**📖 中文摘要**

本文提出了一个用于增强LLM批判性思维能力的整体框架，其核心是通过学习论证重构来监督模型。作者（1）提出了一个自动重构任意论证的引擎（GAAR），（2）使用该引擎合成了一个新的高质量论证重构数据集（Arguinas），（3）研究了学习论证重构是否有利于下游的批判性思维任务。这项工作与“化学大模型”相关，因为批判性思维和逻辑推理能力是构建能够进行科学发现、假设生成和结果解释的化学大模型所必需的。论文中提出的论证重构作为一种监督信号，可以作为一种提升模型逻辑推理能力的方法，这对于化学领域的复杂问题求解至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To think critically about arguments, human learners are trained to identify, reconstruct, and evaluate arguments. Argument reconstruction is especially important because it makes an argument's underlying inferences explicit. However, it remains unclear whether LLMs can similarly enhance their critical thinking ability by learning to reconstruct arguments. To address this question, we introduce a holistic framework with three contributions. We (1) propose an engine that automatically reconstructs arbitrary arguments (GAAR), (2) synthesize a new high-quality argument reconstruction dataset (Arguinas) using the GAAR engine, and (3) investigate whether learning argument reconstruction benefits downstream critical thinking tasks. Our experimental results show that, across seven critical thinking tasks, models trained to learn argument reconstruction outperform models that do not, with the largest performance gains observed when training on the proposed Arguinas dataset. The source code and dataset will be publicly available.

</details>

---

### 22. [TimeAPN: Adaptive Amplitude-Phase Non-Stationarity Normalization for Time Series Forecasting](https://arxiv.org/abs/2603.17436)

**基本信息**

- 🔗 arXiv: [`2603.17436`](https://arxiv.org/abs/2603.17436)
- 👥 作者: Yue Hu, Jialiang Tang, Siwei Yu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17436.pdf)

**💡 相关性分析**

满足标准1：论文提出的幅度-相位非平稳归一化框架，其核心思想是联合建模信号的振幅和相位（时频特性），这种方法论非常适用于分析像质谱这样的复杂信号数据，可直接应用于“质谱结构推理”任务，以提升从质谱中推断分子结构的模型的性能。

**📖 中文摘要**

本文提出了TimeAPN，一个自适应幅度-相位非平稳归一化框架，用于多元长期时间序列预测。该框架从时域和频域明确建模和预测非平稳因素，并结合振幅信息到自适应归一化机制中。虽然应用于时间序列预测，但其处理非平稳性、多尺度信号以及结合时频域分析的方法，与“质谱结构推理”有很强的相关性。质谱数据本质上是信号数据，包含丰富的频域信息（如同位素模式、碎片离子模式），并且其强度（振幅）和质荷比位置（相位）都携带关键的结构信息。TimeAPN中提出的幅度-相位联合建模思想，为从质谱信号中更鲁棒地提取分子结构特征提供了新的技术视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Non-stationarity is a fundamental challenge in multivariate long-term time series forecasting, often manifested as rapid changes in amplitude and phase. These variations lead to severe distribution shifts and consequently degrade predictive performance. Existing normalization-based methods primarily rely on first- and second-order statistics, implicitly assuming that distributions evolve smoothly and overlooking fine-grained temporal dynamics. To address these limitations, we propose TimeAPN, an Adaptive Amplitude-Phase Non-Stationarity Normalization framework that explicitly models and predicts non-stationary factors from both the time and frequency domains. Specifically, TimeAPN first models the mean sequence jointly in the time and frequency domains, and then forecasts its evolution over future horizons. Meanwhile, phase information is extracted in the frequency domain, and the phase discrepancy between the predicted and ground-truth future sequences is explicitly modeled to capture temporal misalignment. Furthermore, TimeAPN incorporates amplitude information into an adaptive normalization mechanism, enabling the model to effectively account for abrupt fluctuations in signal energy. The predicted non-stationary factors are subsequently integrated with the backbone forecasting outputs through a collaborative de-normalization process to reconstruct the final non-stationary time series. The proposed framework is model-agnostic and can be seamlessly integrated with various forecasting backbones. Extensive experiments on seven real-world multivariate datasets demonstrate that TimeAPN consistently improves long-term forecasting accuracy across multiple prediction horizons and outperforms state-of-the-art reversible normalization methods.

</details>

---

### 23. [Baguan-TS: A Sequence-Native In-Context Learning Model for Time Series Forecasting with Covariates](https://arxiv.org/abs/2603.17439)

**基本信息**

- 🔗 arXiv: [`2603.17439`](https://arxiv.org/abs/2603.17439)
- 👥 作者: Linxiao Yang, Xue Jiang, Gezheng Xu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17439.pdf)

**💡 相关性分析**

满足标准1：论文提出的序列原生上下文学习模型，其统一处理原始序列和进行上下文推理的能力，与“化学大模型”中处理复杂化学序列数据（如光谱序列、反应序列）并进行预测推理的任务核心相关。

**📖 中文摘要**

本文提出了Baguan-TS，一个将原始序列表示学习与上下文学习相统一的时序预测框架，通过一个在时间、变量和上下文轴上联合关注的3D Transformer实现。该模型旨在处理带有协变量的时间序列预测，并通过目标空间检索的局部校准等技术解决训练稳定性问题。这项工作与“化学大模型”和“质谱结构推理”均相关。在化学领域，许多数据是时间序列或序列数据（如反应过程监测、分子动力学轨迹、色谱/质谱联用数据）。Baguan-TS提供的端到端序列建模与上下文学习相结合的统一框架，为处理化学中的序列预测和推理问题（例如，预测反应产率、根据时间分辨质谱数据推断反应路径）提供了新的模型范式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transformers enable in-context learning (ICL) for rapid, gradient-free adaptation in time series forecasting, yet most ICL-style approaches rely on tabularized, hand-crafted features, while end-to-end sequence models lack inference-time adaptation. We bridge this gap with a unified framework, Baguan-TS, which integrates the raw-sequence representation learning with ICL, instantiated by a 3D Transformer that attends jointly over temporal, variable, and context axes. To make this high-capacity model practical, we tackle two key hurdles: (i) calibration and training stability, improved with a feature-agnostic, target-space retrieval-based local calibration; and (ii) output oversmoothing, mitigated via context-overfitting strategy. On public benchmark with covariates, Baguan-TS consistently outperforms established baselines, achieving the highest win rate and significant reductions in both point and probabilistic forecasting metrics. Further evaluations across diverse real-world energy datasets demonstrate its robustness, yielding substantial improvements.

</details>

---

### 24. [TRiMS: Real-Time Tracking of Minimal Sufficient Length for Efficient Reasoning via RL](https://arxiv.org/abs/2603.17449)

**基本信息**

- 🔗 arXiv: [`2603.17449`](https://arxiv.org/abs/2603.17449)
- 👥 作者: Tingcheng Bian, Jinchang Luo, Mingquan Cheng 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17449.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是优化大语言模型的推理效率，提出最小充分长度度量和相应的强化学习训练框架，这直接适用于提升“化学大模型”在解决复杂化学问题时的推理效率和成本。

**📖 中文摘要**

本文引入了MSL的理论度量，并提出了TRiMS框架，通过GRPO算法和基于MSL的估计来训练模型，以实现高效的推理并减少推理链长度。该工作旨在最大化“每令牌智能”，即用更短的推理步骤达到相同的正确性。这与“化学大模型”高度相关，因为化学领域的推理（如逆合成分析、性质预测）往往需要复杂的多步思维链。提升推理效率、减少冗余计算对于构建实用且高效的化学大模型至关重要。TRiMS提出的方法为优化化学大模型的推理过程提供了直接的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models achieve breakthroughs in complex reasoning via long chain-of-thought sequences. However, this often leads to severe reasoning inflation, causing substantial computational redundancy. To maximize Intelligence per Token, we introduce a theoretical metric, MSL-Minimal Sufficient Length. MSL rigorously characterizes the shortest reasoning length that preserves answer correctness. We provide a recursive definition based on independently sampled sequences and prove the existence of its limit, establishing the first measurable lower bound for reasoning-chain compression. Building on an analysis of mainstream CoT compression strategies, we identify key structural factors enabling a model to approach MSL. Based on these insights, we propose TRiMS which employs the GRPO algorithm in conjunction with MSL-based estimation during training, while mitigating instabilities during the training process through dynamic batch aggregation and advantage computation using batch-level standard deviation. TRiMS achieves over 80% CoT token reduction with a minor accuracy boost across all benchmarks.

</details>

---

### 25. [FACE-net: Factual Calibration and Emotion Augmentation for Retrieval-enhanced Emotional Video Captioning](https://arxiv.org/abs/2603.17455)

**基本信息**

- 🔗 arXiv: [`2603.17455`](https://arxiv.org/abs/2603.17455)
- 👥 作者: Weidong Chen, Cheng Ye, Zhendong Mao 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17455.pdf)

**💡 相关性分析**

满足标准1：论文提出的检索增强框架及其事实校准、多模态交互机制，为解决“质谱结构推理”中利用数据库检索辅助解析并处理检索结果不确定性的问题提供了新颖且相关的模型设计思路。

**📖 中文摘要**

本文提出了FACE-net，一个用于检索增强型情感视频描述生成的框架，包含事实校准和情感增强模块。其技术核心包括通过不确定性估计进行事实校准，以及渐进式视觉情感增强。虽然应用于视频描述，但其方法论——通过检索外部知识库增强语义信息，然后对检索信息进行校准和细化，并与原始内容交互以生成最终描述——与“质谱结构推理”有很强的类比性。在质谱结构推理中，可以检索已知的质谱-结构对数据库来辅助未知谱图的解析，然后需要校准检索结果（处理噪声、仪器差异），并将校准后的信息与原始谱图特征融合以推断最终结构。FACE-net的框架为这种检索-校准-推理流程提供了可借鉴的模型架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Emotional Video Captioning (EVC) is an emerging task, which aims to describe factual content with the intrinsic emotions expressed in videos. Existing works perceive global emotional cues and then combine with video content to generate descriptions. However, insufficient factual and emotional cues mining and coordination during generation make their methods difficult to deal with the factual-emotional bias, which refers to the factual and emotional requirements being different in different samples on generation. To this end, we propose a retrieval-enhanced framework with FActual Calibration and Emotion augmentation (FACE-net), which through a unified architecture collaboratively mines factual-emotional semantics and provides adaptive and accurate guidance for generation, breaking through the compromising tendency of factual-emotional descriptions in all sample learning. Technically, we firstly introduces an external repository and retrieves the most relevant sentences with the video content to augment the semantic information. Subsequently, our factual calibration via uncertainty estimation module splits the retrieved information into subject-predicate-object triplets, and self-refines and cross-refines different components through video content to effectively mine the factual semantics; while our progressive visual emotion augmentation module leverages the calibrated factual semantics as experts, interacts with the video content and emotion dictionary to generate visual queries and candidate emotions, and then aggregates them to adaptively augment emotions to each factual semantics. Moreover, to alleviate the factual-emotional bias, we design a dynamic bias adjustment routing module to predict and adjust the degree of bias of a sample.

</details>

---

### 26. [Adaptive Encoding Strategy for Quantum Annealing in Mixed-Variable Engineering Optimization](https://arxiv.org/abs/2603.17506)

**基本信息**

- 🔗 arXiv: [`2603.17506`](https://arxiv.org/abs/2603.17506)
- 👥 作者: Fabian Key, Lukas Freinberger, Mayu Muramatsu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17506.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学/计算化学中常见的混合变量优化问题，提出了一种用于量子计算（一种前沿计算范式）的自适应编码策略。虽然未直接提及质谱，但其处理复杂、高维搜索空间（类似于分子构象或结构搜索空间）的方法论与化学信息学中的核心挑战高度相关。

**📖 中文摘要**

本文探讨了量子退火（QA）在混合离散-连续变量工程优化问题中的应用。研究指出，QA本身仅支持离散变量，因此如何对连续变量进行准确高效的编码是一个核心挑战。现有方法要么将耦合问题拆分，要么使用固定位深度编码，前者会损害QA的全局搜索优势，后者则可能无法充分表示动态范围或增加二进制变量数量。为此，作者提出了一种用于QA中连续变量的自适应编码策略，该策略能够更新连续变量的可表示范围。通过将其集成到结构设计优化的最小互补能公式中，作者展示了该方法在固定二进制变量预算下提高了解决方案质量，实现了精度与资源之间的更优权衡。该框架可推广到结构设计之外，为在QA中编码连续变量提供了实用指导，并表明自适应表示可以增强当前硬件的精度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Mixed discrete-continuous optimization is central to engineering design, where discrete choices interact with continuous fields. These problems are difficult due to high-dimensional, complex search spaces. To tackle them, Quantum Annealing (QA) is promising, yet its native binary nature supports only discrete variables, making accurate and efficient encodings of continuous quantities a central challenge. Existing approaches either split the coupled problem, mapping discrete decisions to QA while solving continuous fields classically, or use fixed-bit-depth encodings. The former compromises QA's global search advantages; the latter can underrepresent dynamic range or inflate the number of binary variables. We show that simply increasing bit depth can even degrade performance on current QA hardware, underscoring the need for alternative encodings. In response, we introduce an adaptive encoding strategy for continuous variables in QA that enables efficient treatment of coupled mixed-variable problems. We propose an update strategy for the representable ranges of the continuous variables and demonstrate its utility by integrating it into the minimum complementary energy formulation for structural design optimization, which provides a single, coupled constrained problem. We apply a quadratic penalty method where we update the representation of the continuous variables while targeting the full original objective, preserving QA's global search capability. On a published benchmark, the size optimization of a composite rod, our adaptive encoding improves solution quality under a fixed binary variable budget, demonstrating a superior precision-resource trade-off. Since the framework generalizes beyond structural design, it offers practical guidance for encoding continuous variables for QA and indicates that adaptive representations can enhance precision on current hardware.

</details>

---

### 27. [Anisotropic Permeability Tensor Prediction from Porous Media Microstructure via Physics-Informed Progressive Transfer Learning with Hybrid CNN-Transformer](https://arxiv.org/abs/2603.17532)

**基本信息**

- 🔗 arXiv: [`2603.17532`](https://arxiv.org/abs/2603.17532)
- 👥 作者: Mohammad Nooraiepour
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17532.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于从微观结构图像预测物理性质（渗透率张量）的深度学习模型。这直接属于化学信息学和材料信息学的范畴，其中从结构图像推断复杂物理化学性质是一个核心任务。该方法论（混合架构、物理约束、渐进学习）对于处理类似质谱数据（从光谱推断结构）或分子性质预测具有重要的借鉴意义。

**📖 中文摘要**

本文提出了一种物理信息深度学习框架，用于从多孔介质微观结构图像中快速预测各向异性渗透率张量。该框架结合了MaxViT混合CNN-Transformer架构、渐进式迁移学习和可微分物理约束。MaxViT的多轴注意力机制能够同时解析晶粒尺度的孔喉几何（通过块局部操作）和代表性体积单元（REV）尺度的连通性统计（通过网格全局操作），为渗透率张量预测提供了所需的物理空间层次结构。该模型在涵盖三个数量级渗透率的20000个合成多孔介质样本上进行训练，采用三阶段渐进式课程学习，并利用可微分惩罚项来强制执行Onsager互易性和正定性。在包含4000个样本的测试集上，该框架实现了方差加权R2 = 0.9960，相比监督基线减少了33%的未解释方差。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of permeability tensors from pore-scale microstructure images is essential for subsurface flow modeling, yet direct numerical simulation requires hours per sample, fundamentally limiting large-scale uncertainty quantification and reservoir optimization workflows. A physics-informed deep learning framework is presented that resolves this bottleneck by combining a MaxViT hybrid CNN-Transformer architecture with progressive transfer learning and differentiable physical constraints. MaxViT's multi-axis attention mechanism simultaneously resolves grain-scale pore-throat geometry via block-local operations and REV-scale connectivity statistics through grid-global operations, providing the spatial hierarchy that permeability tensor prediction physically requires. Training on 20000 synthetic porous media samples spanning three orders of magnitude in permeability, a three-phase progressive curriculum advances from an ImageNet-pretrained baseline with D4-equivariant augmentation and tensor transformation, through component-weighted loss prioritizing off-diagonal coupling, to frozen-backbone transfer learning with porosity conditioning via Feature-wise Linear Modulation (FiLM). Onsager reciprocity and positive definiteness are enforced via differentiable penalty terms. On a held-out test set of 4000 samples, the framework achieves variance-weighted R2 = 0.9960 (R2_Kxx = 0.9967, R2_Kxy = 0.9758), a 33% reduction in unexplained variance over the supervised baseline. The results offer three transferable principles for physics-informed scientific machine learning: large-scale visual pretraining transfers effectively across domain boundaries; physical constraints are most robustly integrated as differentiable architectural components; and progressive training guided by diagnostic failure-mode analysis enables unambiguous attribution of performance gains across methodological stages.

</details>

---

### 28. [CA-Based Interpretable Knowledge Representation and Analysis of Geometric Design Parameters](https://arxiv.org/abs/2603.17535)

**基本信息**

- 🔗 arXiv: [`2603.17535`](https://arxiv.org/abs/2603.17535)
- 👥 作者: Alexander Köhler, Michael Breuß
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17535.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及高维设计参数空间的降维和可解释参数估计，这是化学信息学中的一个核心问题，例如在分子描述符分析、构象空间探索或从光谱数据中逆向推导分子特征时。论文对PCA及其局限性的分析，以及寻求可解释参数估计的目标，与化学信息学中从复杂数据中提取有意义、可解释特征的研究高度相关。

**📖 中文摘要**

本文讨论了在CAD应用中，复杂几何体通常由大量设计参数定义，导致高维设计空间，给下游工程过程（如仿真、优化和设计探索）带来挑战。因此，常使用主成分分析（PCA）等降维方法来识别几何变化的主导模式，并获得几何的紧凑表示。然而，经典PCA虽然擅长紧凑表示，但不能直接恢复生成几何体的底层设计参数。本文致力于解决从基于PCA的表示中估计设计参数的问题。作者分析了一种针对该应用领域的最新PCA修改方法，并证明其结果实际上与标准PCA相同。他们研究了该方法的局限性，并提出了在何种合理条件下可以获得准确、可解释的参数估计。通过专门的实验，作者深入探讨了PCA的每个阶段以及在这些过程中几何体可能发生的变化。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In many CAD-based applications, complex geometries are defined by a high number of design parameters. This leads to high-dimensional design spaces that are challenging for downstream engineering processes like simulations, optimization, and design exploration tasks. Therefore, dimension reduction methods such as principal component analysis (PCA) are used. The PCA identifies dominant modes of geometric variation and yields a compact representation of the geometry. While classical PCA excels in the compact representation part, it does not directly recover underlying design parameters of a generated geometry. In this work, we deal with the problem of estimating design parameters from PCA-based representations. Analyzing a recent modification of the PCA dedicated to our field of application, we show that the results are actually identical to the standard PCA. We investigate limitations of this approach and present reasonable conditions under which accurate, interpretable parameter estimation can be obtained. With the help of dedicated experiments, we take a more in-depth look at every stage of the PCA and the possible changes of the geometry during these processes.

</details>

---

### 29. [Conditional Inverse Learning of Time-Varying Reproduction Numbers Inference](https://arxiv.org/abs/2603.17549)

**基本信息**

- 🔗 arXiv: [`2603.17549`](https://arxiv.org/abs/2603.17549)
- 👥 作者: Lanlan Yu, Quan-Hui Liu, Haoyue Zheng 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17549.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决一个逆问题（从观测数据推断底层时变参数）。虽然应用领域是流行病学，但其方法论——将物理/动力学约束（更新方程）与数据驱动的条件映射学习相结合——与化学信息学中的质谱结构推理高度相似。在质谱推理中，目标也是从观测光谱（质谱）逆向推断底层分子结构（一个逆问题），并常常需要结合化学规则（类似物理约束）。因此，该框架为解决质谱逆问题提供了新颖的方法论视角。

**📖 中文摘要**

从流行病发病率数据中估计时变再生数是一个核心任务，但这本质上是一个不适定的逆问题。现有方法通常依赖于从流行病学模型中推导出的强结构假设，这限制了它们适应由干预措施或行为变化引起的非平稳传播动态的能力，导致对机制转变的检测延迟和估计精度下降。本文提出了一个条件逆再生数学习框架（CIRL），通过学习从历史发病模式和显式时间信息到潜在再生数的条件映射来解决该逆问题。CIRL不是强加参数约束，而是将流行病学结构与灵活的基于似然的统计建模软性结合，使用更新方程作为前向算子来强制动态一致性。由此产生的框架结合了基于流行病学的约束和数据驱动的时间表示，产生的再生数估计对观测噪声具有鲁棒性，同时对突发的传播变化和零膨胀的发病率观测保持响应。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Estimating time-varying reproduction numbers from epidemic incidence data is a central task in infectious disease surveillance, yet it poses an inherently ill-posed inverse problem. Existing approaches often rely on strong structural assumptions derived from epidemiological models, which can limit their ability to adapt to non-stationary transmission dynamics induced by interventions or behavioral changes, leading to delayed detection of regime shifts and degraded estimation accuracy. In this work, we propose a Conditional Inverse Reproduction Learning framework (CIRL) that addresses the inverse problem by learning a {conditional mapping} from historical incidence patterns and explicit time information to latent reproduction numbers. Rather than imposing strongly enforced parametric constraints, CIRL softly integrates epidemiological structure with flexible likelihood-based statistical modeling, using the renewal equation as a forward operator to enforce dynamical consistency. The resulting framework combines epidemiologically grounded constraints with data-driven temporal representations, producing reproduction number estimates that are robust to observation noise while remaining responsive to abrupt transmission changes and zero-inflated incidence observations. Experiments on synthetic epidemics with controlled regime changes and real-world SARS and COVID-19 data demonstrate the effectiveness of the proposed approach.

</details>

---

### 30. [Unsupervised Symbolic Anomaly Detection](https://arxiv.org/abs/2603.17575)

**基本信息**

- 🔗 arXiv: [`2603.17575`](https://arxiv.org/abs/2603.17575)
- 👥 作者: Md Maruf Hossain, Tim Katzke, Simon Klüttermann 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17575.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于符号回归（一种可解释的机器学习方法）的异常检测方法。化学信息学和质谱分析中的一个关键需求是从复杂数据（如质谱、色谱）中检测异常或识别未知化合物，同时要求模型具有可解释性以支持化学家的决策。SYRAN的方法论（学习人类可读的符号不变量）直接适用于化学数据分析，为从光谱数据中发现规律和异常提供了新的、可解释的工具。

**📖 中文摘要**

本文提出了SYRAN，一种基于符号回归的无监督异常检测方法。与在 opaque 的高维模型中编码正常模式不同，我们的方法学习一组人类可读的方程，这些方程描述了符号不变量：即在正常数据上近似恒定的函数。对这些不变量的偏离产生异常分数，因此检测逻辑从构造上就是可解释的，而不是通过事后解释。实验结果表明，SYRAN具有高度可解释性，提供的方程对应于已知的科学或医学关系，并且保持了与最先进方法相当的强大异常检测性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose SYRAN, an unsupervised anomaly detection method based on symbolic regression. Instead of encoding normal patterns in an opaque, high-dimensional model, our method learns an ensemble of human-readable equations that describe symbolic invariants: functions that are approximately constant on normal data. Deviations from these invariants yield anomaly scores, so that the detection logic is interpretable by construction, rather than via post-hoc explanation. Experimental results demonstrate that SYRAN is highly interpretable, providing equations that correspond to known scientific or medical relationships, and maintains strong anomaly detection performance comparable to that of state-of-the-art methods.

</details>

---

### 31. [One-Step Sampler for Boltzmann Distributions via Drifting](https://arxiv.org/abs/2603.17579)

**基本信息**

- 🔗 arXiv: [`2603.17579`](https://arxiv.org/abs/2603.17579)
- 👥 作者: Wenhan Cao, Keyu Yan, Lin Zhao
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17579.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种用于从玻尔兹曼分布（在统计物理和化学中至关重要，用于描述分子系统在平衡态下的概率分布）进行高效采样的新方法。化学信息学和计算化学中经常需要从复杂的能量景观中采样分子构象或反应路径。本文提出的“漂移”框架和一步采样器为在化学空间中进行高效、摊销的采样提供了有前景的新技术，与分子模拟和设计相关。

**📖 中文摘要**

本文提出了一种基于漂移的框架，用于对由能量函数定义的玻尔兹曼分布进行摊销采样。该方法通过将样本沿着当前模型分布向目标玻尔兹曼分布的高斯平滑得分场进行投影，来训练一个一步神经生成器。对于仅指定到未知归一化常数的目标，我们从平滑能量推导出一个实用的目标侧漂移，并使用两个估计器：局部重要性采样均值漂移估计器和二阶曲率校正近似。结合采样器侧平滑得分的迷你批次高斯均值漂移估计，这产生了一个简单的停止梯度目标，用于稳定的一步训练。在一个四模式高斯混合玻尔兹曼目标上，我们的采样器实现了均值误差0.0754，协方差误差0.0425和RBF MMD 0.0020。额外的双阱和香蕉形目标表明，相同的公式也能处理非凸和弯曲的低能量几何形状。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a drifting-based framework for amortized sampling of Boltzmann distributions defined by energy functions. The method trains a one-step neural generator by projecting samples along a Gaussian-smoothed score field from the current model distribution toward the target Boltzmann distribution. For targets specified only up to an unknown normalization constant, we derive a practical target-side drift from a smoothed energy and use two estimators: a local importance-sampling mean-shift estimator and a second-order curvature-corrected approximation. Combined with a mini-batch Gaussian mean-shift estimate of the sampler-side smoothed score, this yields a simple stop-gradient objective for stable one-step training. On a four-mode Gaussian-mixture Boltzmann target, our sampler achieves mean error $0.0754$, covariance error $0.0425$, and RBF MMD $0.0020$. Additional double-well and banana targets show that the same formulation also handles nonconvex and curved low-energy geometries. Overall, the results support drifting as an effective way to amortize iterative sampling from Boltzmann distributions into a single forward pass at test time.

</details>

---

### 32. [On the validity limits of the parametrisation method for invariant manifolds: an assessment of practical criteria for vibrating systems](https://arxiv.org/abs/2603.17611)

**基本信息**

- 🔗 arXiv: [`2603.17611`](https://arxiv.org/abs/2603.17611)
- 👥 作者: André de Figueiredo Stabile, Aurélien Grolet, Alessandra Vizzaccaro 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17611.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和确保用于非线性系统建模的数学方法（参数化方法）的可靠性和有效性范围。虽然应用在力学振动，但其核心是关于从高维复杂系统（如分子动力学系统）提取低维可解释模型（如反应坐标）的数学基础。化学信息学中，从分子模拟数据或光谱数据中提取主导模式和动力学信息面临类似挑战。论文对方法有效性、误差估计和收敛性的严格分析，对化学中复杂动力系统的模型降阶和解释具有重要参考价值。

**📖 中文摘要**

本文研究了用于不变流形的参数化方法在非线性振动系统背景下的有效性极限，该方法是一种推导降阶模型、精确计算非线性正规模态的强大技术。得益于任意阶渐近展开，收敛结果触手可及并可直接应用于有限元结构。然而，由于它依赖于局部理论和渐近展开，结果仅在达到给定振幅之前有效，该振幅定义了近似的收敛半径。本文旨在研究该方法的有效性极限，回顾现有的误差估计，并提出一种在计算过程中估计有效性范围的实用方法，从而产生安全边界，在此范围内可以使用降阶模型。评估了三种不同的准则。第一种使用随着到不动点距离增加时不变性方程中的误差。第二种改编自为正规形式变换推导的上界准则，基于同调算子的潜在奇点。第三种使用级数的柯西和达朗贝尔收敛规则。这些准则在一系列代表处理非线性振动时遇到的情况的不同示例上进行了测试。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The parametrisation method for invariant manifolds is a powerful technique for deriving reduced-order models in the context of nonlinear vibrating systems, allowing accurate computations of nonlinear normal modes. Thanks to arbitrary order asymptotic expansions, converged results are within reach and directly applicable to finite element structures. However, since it relies on a local theory and asymptotic expansions, the results are only valid up to a given amplitude, which defines the convergence radius of the approximation. The aim of this contribution is to investigate the validity limits of the approach and review the existing error estimates, with the concrete objective of proposing a practical approach to estimate the validity range during the computation, thus producing safe bounds within which the reduced-order model can be used. Three different criteria are assessed. The first one uses the error in the invariance equation as the distance to the fixed point increases. The second one is adapted from an upper bound criterion derived for normal form transforms and based on the potential singularities of the homological operator. The third one uses Cauchy and d'Alembert convergence rules for series. The criteria are tested on a number of different examples that are representative of the situations encountered when dealing with nonlinear vibrations. The Duffing equation serves as a first benchmark that allows considering conservative oscillations, forced systems at primary resonance, and superharmonic resonance. The investigations are then extended to a vibrating system with two degrees of freedom. Finally, the different criteria are assessed on a finite element beam structure, and guidelines are formulated to generalise their practical use and produce accurate and easy-to-use error bounds in the context of model order reduction for nonlinear vibrating structures.

</details>

---

### 33. [The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation](https://arxiv.org/abs/2603.17627)

**基本信息**

- 🔗 arXiv: [`2603.17627`](https://arxiv.org/abs/2603.17627)
- 👥 作者: Houston Haynes
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17627.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是引入一种新的数学表示框架（程序超图）来处理几何代数计算和空间计算。几何代数（又称克利福德代数）是数学物理和计算机图形学中的强大工具，近年来也开始应用于化学信息学，用于表示分子几何、对称性和相互作用。本文提出的PHG框架旨在更自然、高效地编译此类计算，这对于开发用于分子建模和模拟的新型计算工具具有潜在重要性。

**📖 中文摘要**

本文介绍了程序超图（PHG），作为程序语义图（PSG）的原则性推广，将二元边提升为任意元数的超边。我们证明了克利福德代数中的阶是现有DTS阿贝尔群框架内的自然维度轴，阶推断可以推导出几何乘积的稀疏性，从而消除了对克利福德代数神经网络进行手动专业化的主要性能异议，并且网格拓扑的k-单纯形结构是超边形式的直接实例。我们评估了现有的几何代数库生态系统，指出了当前系统未解决的一致的类型论差距，并展示了PHG如何在Fidelity编译框架内填补这一空白。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Program Semantic Graph (PSG) introduced in prior work on Dimensional Type Systems and Deterministic Memory Management encodes compilation-relevant properties as binary edge relations between computation nodes. This representation is adequate for scalar and tensor computations, but becomes structurally insufficient for two classes of problems central to heterogeneous compute: tile co-location and routing constraints in spatial dataflow architectures, which are inherently multi-way; and geometric algebra computation, where graded multi-way products cannot be faithfully represented as sequences of binary operations without loss of algebraic identity. This paper introduces the Program Hypergraph (PHG) as a principled generalization of the PSG that promotes binary edges to hyperedges of arbitrary arity. We demonstrate that grade in Clifford algebra is a natural dimension axis within the existing DTS abelian group framework, that grade inference derives geometric product sparsity eliminating the primary performance objection to Clifford algebra neural networks without manual specialization, and that the k-simplex structure of mesh topology is a direct instance of the hyperedge formalism. We assess the existing geometric algebra library ecosystem, identify the consistent type-theoretic gap that no current system addresses, and show that the PHG closes it within the Fidelity compilation framework. The result is a compilation framework where geometric correctness, memory placement, numerical precision selection, and hardware partitioning are jointly derivable from a single graph structure exposed as interactive design-time feedback.

</details>

---

### 34. [Automated Grammar-based Algebraic Multigrid Design With Evolutionary Algorithms](https://arxiv.org/abs/2603.17641)

**基本信息**

- 🔗 arXiv: [`2603.17641`](https://arxiv.org/abs/2603.17641)
- 👥 作者: Dinesh Parthasarathy, Wayne Mitchell, Arjun Gambhir 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17641.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用进化算法（一种优化和搜索技术）自动设计高效的数值算法（代数多重网格法）。化学信息学和计算化学中充斥着需要求解大规模线性系统或特征值问题（例如，在量子化学计算、分子动力学中）的任务。自动化算法设计和优化的方法论（如本文使用的遗传编程）可以直接应用于优化化学计算中的数值求解器，提高模拟效率，属于化学信息学中的高性能计算方向。

**📖 中文摘要**

尽管多重网格法对于求解许多重要的偏微分方程是渐近最优的，但其效率严重依赖于各个算法组件的精心选择。与最近可以使用深度学习技术优化某些多重网格组件的方法相比，我们采用了一种互补的策略，利用进化算法从经过验证的算法构建块中构建高效的多重网格循环。在这里，我们将展示其应用于生成具有所谓灵活循环的高效代数多重网格方法，即特定于层次的平滑序列和非递归循环模式。具有此类非标准循环的搜索空间是手动导航难以处理的，并使用由上下文无关文法指导的遗传编程（GP）生成。使用线性代数库hypre进行的数值实验证明了这些非标准GP循环作为求解器和预处理器提高多重网格性能的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although multigrid is asymptotically optimal for solving many important partial differential equations, its efficiency relies heavily on the careful selection of the individual algorithmic components. In contrast to recent approaches that can optimize certain multigrid components using deep learning techniques, we adopt a complementary strategy, employing evolutionary algorithms to construct efficient multigrid cycles from proven algorithmic building blocks. Here, we will present its application to generate efficient algebraic multigrid methods with so-called \emph{flexible cycling}, that is, level-specific smoothing sequences and non-recursive cycling patterns. The search space with such non-standard cycles is intractable to navigate manually, and is generated using genetic programming (GP) guided by context-free grammars. Numerical experiments with the linear algebra library, \emph{hypre}, demonstrate the potential of these non-standard GP cycles to improve multigrid performance both as a solver and a preconditioner.

</details>

---

### 35. [Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment](https://arxiv.org/abs/2603.17655)

**基本信息**

- 🔗 arXiv: [`2603.17655`](https://arxiv.org/abs/2603.17655)
- 👥 作者: Yaze Zhao, Yixiong Zou, Yuhua Li 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17655.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是改进视觉语言模型（VLMs）在跨域少样本学习中对细粒度视觉模式的理解和对齐能力。在化学信息学和质谱分析中，一个关键挑战是让模型能够理解复杂的、细粒度的科学图像（如化学结构图、光谱图）并与文本描述（如分子式、反应条件）进行精确关联，尤其是在数据稀缺的新领域（如新的化合物类别）。本文提出的解决局部错位问题的方法（循环一致性、语义锚）为提高模型对化学视觉数据的细粒度理解提供了技术思路。

**📖 中文摘要**

跨域少样本学习（CDFSL）使使用大规模通用数据（源域）训练的模型能够适应仅有稀缺训练数据的下游目标域，其中视觉语言模型（例如CLIP）的研究仍处于早期阶段。典型的下游领域，如医学诊断，需要细粒度的视觉线索以进行可解释的识别，但我们发现当前微调的CLIP模型很难聚焦于这些线索，尽管它们可以粗略地聚焦于源域中的重要区域。尽管当前工作已经证明了CLIP在捕捉局部细微模式方面的不足，但在本文中，我们发现领域差距和稀缺的训练数据进一步加剧了这种不足，远超过整体模式的不足，我们称之为基于CLIP的CDFSL中的局部错位问题。为了解决这个问题，由于在对齐局部视觉特征和文本语义方面缺乏监督，我们转向自监督信息。受翻译任务的启发，我们提出了具有循环一致性的CC-CDFSL方法，该方法将局部视觉特征翻译成文本特征，然后再翻译回视觉特征（反之亦然），并约束原始特征接近翻译回来的特征。为了减少视觉模态中更丰富信息引入的噪声，我们进一步提出了语义锚机制，该机制首先增强视觉特征以提供更大的语料库用于文本到图像的映射，然后缩小图像特征以过滤掉不相关的图像到文本映射。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cross-Domain Few-Shot Learning (CDFSL) adapts models trained with large-scale general data (source domain) to downstream target domains with only scarce training data, where the research on vision-language models (e.g., CLIP) is still in the early stages. Typical downstream domains, such as medical diagnosis, require fine-grained visual cues for interpretable recognition, but we find that current fine-tuned CLIP models can hardly focus on these cues, albeit they can roughly focus on important regions in source domains. Although current works have demonstrated CLIP's shortcomings in capturing local subtle patterns, in this paper, we find that the domain gap and scarce training data further exacerbate such shortcomings, much more than that of holistic patterns, which we call the local misalignment problem in CLIP-based CDFSL. To address this problem, due to the lack of supervision in aligning local visual features and text semantics, we turn to self-supervision information. Inspired by the translation task, we propose the CC-CDFSL method with cycle consistency, which translates local visual features into text features and then translates them back into visual features (and vice versa), and constrains the original features close to the translated back features. To reduce the noise imported by richer information in the visual modality, we further propose a Semantic Anchor mechanism, which first augments visual features to provide a larger corpus for the text-to-image mapping, and then shrinks the image features to filter out irrelevant image-to-text mapping. Extensive experiments on various benchmarks, backbones, and fine-tuning methods show we can (1) effectively improve the local vision-language alignment, (2) enhance the interpretability of learned patterns and model decisions by visualizing patches, and (3) achieve state-of-the-art performance.

</details>

---

### 36. [From Symbol to Meaning: Ontological and Philosophical Reflections on Large Language Models in Information Systems Engineering](https://arxiv.org/abs/2603.17659)

**基本信息**

- 🔗 arXiv: [`2603.17659`](https://arxiv.org/abs/2603.17659)
- 👥 作者: José Palazzo Moreira de Oliveira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17659.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对大型语言模型（作为“化学大模型”的一个子集或相关领域）的哲学和概念性综述/展望文章。它深入讨论了LLMs对信息、知识和表示的根本性影响。虽然不直接涉及化学，但其对“模型”、“意义”、“知识”的深刻反思，对于思考如何构建、理解和评估化学领域的大模型（如用于分子设计、反应预测的LLMs）具有重要的启发意义，属于对基础模型在科学中应用的远景讨论。

**📖 中文摘要**

本文对大型语言模型（LLMs）在信息系统工程中的本体论和哲学影响进行了反思。文章认为，LLMs的出现不仅具有技术意义，更挑战了长期以来构建我们对信息、表示和知识理解的本体论、认识论和符号学假设。本文提出了一种整合性反思，探讨LLMs如何重新配置语言、意义和系统设计之间的关系，表明它们的出现要求重新审视当代信息系统的概念基础。借鉴从皮尔士到海德格尔和弗洛里迪的哲学传统，我们研究了生成模型的逻辑如何既扩展又动摇了本体论和意指的经典概念。讨论强调了将基于LLM的系统建立在透明、伦理一致的框架中的必要性，这些框架尊重以人为中心的知识过程的完整性。最终，本文认为LLMs不应仅仅被理解为自动化工具，而应被理解为重塑信息系统工程的哲学和符号学基础的认识论主体。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The advent of Large Language Models (LLMs) represents a turning point in the theoretical foundations of Information Systems Engineering. Beyond their technical significance, LLMs challenge the ontological, epistemological, and semiotic assumptions that have long structured our understanding of in-formation, representation, and knowledge. This article proposes an integrative reflection on how LLMs reconfigure the relationships among language, meaning, and system design, suggesting that their emergence demands a re-examination of the conceptual foundations of contemporary information systems. Sketching on philosophical traditions from Peirce to Heidegger and Floridi, we investigate how the logic of generative models both extends and destabilises classical notions of ontology and signification. The discussion emphasises the necessity of grounding LLM-based systems in transparent, ethically coherent frameworks that respect the integrity of human-centred knowledge processes. Ultimately, the paper argues that LLMs should be understood not merely as tools for automation but as epistemic agents that reshape the philosophical and semiotic foundations of information systems engineering.

</details>

---

### 37. [Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671)

**基本信息**

- 🔗 arXiv: [`2603.17671`](https://arxiv.org/abs/2603.17671)
- 👥 作者: Liangyu Yuan, Ruoyu Wang, Tong Zhao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17671.pdf)

**💡 相关性分析**

满足标准1：论文提出的实例感知离散化框架是扩散模型（一种重要的生成式大模型）采样方法的核心改进。该方法可直接迁移应用于化学信息学领域的分子生成等“化学大模型”任务，以提高生成质量和效率。

**📖 中文摘要**

本文提出了一种实例感知的离散化框架，用于改进扩散和流匹配模型的采样过程。虽然论文主要关注于通用生成模型的采样加速，但其核心方法——通过自适应调整时间步分配来优化生成过程——与“化学大模型”中生成式模型（如用于分子生成的扩散模型）的采样效率提升高度相关。该技术可直接应用于化学信息学中基于扩散模型的分子结构生成与优化任务，提高采样质量和效率。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion and flow matching models generate high-fidelity data by simulating paths defined by Ordinary or Stochastic Differential Equations (ODEs/SDEs), starting from a tractable prior distribution. The probability flow ODE formulation enables the use of advanced numerical solvers to accelerate sampling. Orthogonal yet vital to solver design is the discretization strategy. While early approaches employed handcrafted heuristics and recent methods adopt optimization-based techniques, most existing strategies enforce a globally shared timestep schedule across all samples. This uniform treatment fails to account for instance-specific complexity in the generative process, potentially limiting performance. Motivated by controlled experiments on synthetic data, which reveals the suboptimality of global schedules under instance-specific dynamics, we propose an instance-aware discretization framework. Our method learns to adapt timestep allocations based on input-dependent priors, extending gradient-based discretization search to the conditional generative setting. Empirical results across diverse settings, including synthetic data, pixel-space diffusion, latent-space images and video flow matching models, demonstrate that our method consistently improves generation quality with marginal tuning cost compared to training and negligible inference overhead.

</details>

---

### 38. [Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models](https://arxiv.org/abs/2603.17677)

**基本信息**

- 🔗 arXiv: [`2603.17677`](https://arxiv.org/abs/2603.17677)
- 👥 作者: Jaemin Kim, Jong Chul Ye
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17677.pdf)

**💡 相关性分析**

满足标准1：论文研究的自适应检索增强扩散模型框架，直接关联“化学大模型”如何有效、可靠地整合外部领域知识（如质谱库、分子数据库）这一核心挑战，为构建知识增强的化学AI模型提供了方法论参考。

**📖 中文摘要**

本文提出了自适应检索增强掩码扩散模型（ARAM），一个用于在检索增强生成（RAG）设置中动态校准引导尺度的免训练框架。该工作专注于扩散语言模型，但其核心思想——处理外部知识（检索到的上下文）与模型内部参数知识之间的冲突——对于构建能够整合外部化学知识库（如质谱数据库、分子结构库）的“化学大模型”具有重要启示。该方法为解决大模型在专业领域（如质谱解析）中如何可靠地利用外部结构化数据提供了技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-Augmented Generation (RAG) improves factual grounding by incorporating external knowledge into language model generation. However, when retrieved context is noisy, unreliable, or inconsistent with the model's parametric knowledge, it introduces retrieval-prior conflicts that can degrade generation quality. While this problem has been studied in autoregressive language models, it remains largely unexplored in diffusion-based language models, where the iterative denoising process introduces unique challenges for integrating retrieved context. In this work, we propose Adaptive Retrieval-Augmented Masked Diffusion (ARAM), a training-free adaptive guidance framework for Masked Diffusion Models (MDMs) in RAG settings. ARAM dynamically calibrates the guidance scale during denoising according to the Signal-to-Noise Ratio (SNR) of the distributional shift induced by retrieved context. Intuitively, the model strengthens guidance when the retrieved context provides reliable corrective evidence and suppresses it when the contextual signal is noisy or non-supportive. Extensive experiments on multiple knowledge-intensive QA benchmarks show that ARAM improves overall QA performance over competitive RAG baselines.

</details>

---

### 39. [Flow Matching Policy with Entropy Regularization](https://arxiv.org/abs/2603.17685)

**基本信息**

- 🔗 arXiv: [`2603.17685`](https://arxiv.org/abs/2603.17685)
- 👥 作者: Ting Gao, Stavros Orfanoudakis, Nan Lin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17685.pdf)

**💡 相关性分析**

满足标准1：论文提出的流匹配策略（FMER）是基于流匹配（Flow Matching）的生成模型方法，与“化学大模型”中用于分子、构象或连续属性生成的生成式AI技术直接相关，提供了新的模型框架和优化视角。

**📖 中文摘要**

本文提出了带有熵正则化的流匹配策略（FMER），一个基于常微分方程（ODE）的在线强化学习框架。该方法参数化策略并通过流匹配进行动作采样。虽然应用于机器人控制，但其核心技术创新——使用流匹配（Flow Matching）来参数化策略并实现最大熵优化——是生成模型领域的前沿方法。流匹配与扩散模型紧密相关，是构建连续数据（如分子构象、光谱）生成模型的重要技术。因此，该工作为开发用于分子动力学模拟或光谱生成的“化学大模型”提供了有价值的模型架构和优化思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion-based policies have gained significant popularity in Reinforcement Learning (RL) due to their ability to represent complex, non-Gaussian distributions. Stochastic Differential Equation (SDE)-based diffusion policies often rely on indirect entropy control due to the intractability of the exact entropy, while also suffering from computationally prohibitive policy gradients through the iterative denoising chain. To overcome these issues, we propose Flow Matching Policy with Entropy Regularization (FMER), an Ordinary Differential Equation (ODE)-based online RL framework. FMER parameterizes the policy via flow matching and samples actions along a straight probability path, motivated by optimal transport. FMER leverages the model's generative nature to construct an advantage-weighted target velocity field from a candidate set, steering policy updates toward high-value regions. By deriving a tractable entropy objective, FMER enables principled maximum-entropy optimization for enhanced exploration. Experiments on sparse multi-goal FrankaKitchen benchmarks demonstrate that FMER outperforms state-of-the-art methods, while remaining competitive on standard MuJoco benchmarks. Moreover, FMER reduces training time by 7x compared to heavy diffusion baselines (QVPO) and 10-15% relative to efficient variants.

</details>

---

### 40. [Cache-enabled Generative Joint Source-Channel Coding for Evolving Semantic Communications](https://arxiv.org/abs/2603.17702)

**基本信息**

- 🔗 arXiv: [`2603.17702`](https://arxiv.org/abs/2603.17702)
- 👥 作者: Shunpu Tang, Qianqian Yang, Jihong Park 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17702.pdf)

**💡 相关性分析**

满足标准1：论文利用预训练生成模型和语义缓存的核心框架，为“化学大模型”如何高效表示、存储和重用化学实体（如分子片段）的语义信息，以及如何将其应用于质谱等数据的推理任务提供了创新的技术类比和思路。

**📖 中文摘要**

本文提出了一个基于GAN反转的联合信源信道编码框架，用于语义通信。虽然应用领域是无线图像传输，但其核心方法——利用预训练生成模型（SemanticStyleGAN）并通过缓存解耦的语义组件来重用已传输内容——展示了一种高效的、基于大模型的语义表示与重用范式。这种“语义级缓存”和利用预训练生成模型进行自适应编码的思想，可以启发“化学大模型”和“质谱结构推理”领域的研究，例如：如何缓存和重用分子片段的语义表示，或利用预训练的化学生成模型对质谱信号进行高效、可解释的编码与解码。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning-based semantic communication (SemCom) has recently emerged as a promising paradigm for improving the transmission efficiency of wireless networks. However, existing methods typically rely on extensive end-to-end training, which is both inflexible and computationally expensive in dynamic wireless environments. Moreover, they fail to exploit redundancy across multiple transmissions of semantically similar content, limiting overall efficiency. To overcome these limitations, we propose a channel-aware generative adversarial network (GAN) inversion-based joint source-channel coding (CAGI-JSCC) framework that enables training-free SemCom by leveraging a pre-trained SemanticStyleGAN model. By explicitly incorporating wireless channel characteristics into the GAN inversion process, CAGI-JSCC adapts to varying channel conditions without additional training. Furthermore, we introduce a cache-enabled dynamic codebook (CDC) that caches disentangled semantic components at both the transmitter and receiver, allowing the system to reuse previously transmitted content. This semantic-level caching can continuously reduce redundant transmissions as experience accumulates. Extensive experiments on image transmission demonstrate the effectiveness of the proposed framework. In particular, our system achieves comparable perceptual quality with an average bandwidth compression ratio (BCR) of 1/224, and as low as 1/1024 for a single image, significantly outperforming baselines with a BCR of 1/128.

</details>

---

### 41. [Towards Infinitely Long Neural Simulations: Self-Refining Neural Surrogate Models for Dynamical Systems](https://arxiv.org/abs/2603.17750)

**基本信息**

- 🔗 arXiv: [`2603.17750`](https://arxiv.org/abs/2603.17750)
- 👥 作者: Qi Liu, Laure Zanna, Joan Bruna
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17750.pdf)

**💡 相关性分析**

满足标准1：论文针对生成模型长序列生成中的一致性难题提出了理论框架和解决方案，这与“化学大模型”生成复杂分子或模拟动力学过程时确保结构合理性和物理一致性的核心需求直接相关。

**📖 中文摘要**

本文针对自回归神经代理模型在模拟动力系统时存在的分布漂移问题，提出了一个统一的数学框架和自 refining 神经代理模型（SNS）。该模型通过条件扩散模型来平衡短期保真度和长期一致性。这项工作虽然聚焦于动力系统模拟，但其解决的核心问题——如何确保生成模型在长序列生成中的一致性——正是“化学大模型”在生成长序列分子（如聚合物）或模拟长时间分子动力学轨迹时所面临的关键挑战。论文提出的框架为开发能够进行可靠长程预测的化学生成模型提供了理论基础和方法论。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in autoregressive neural surrogate models have enabled orders-of-magnitude speedups in simulating dynamical systems. However, autoregressive models are generally prone to distribution drift: compounding errors in autoregressive rollouts that severely degrade generation quality over long time horizons. Existing work attempts to address this issue by implicitly leveraging the inherent trade-off between short-time accuracy and long-time consistency through hyperparameter tuning. In this work, we introduce a unifying mathematical framework that makes this tradeoff explicit, formalizing and generalizing hyperparameter-based strategies in existing approaches. Within this framework, we propose a robust, hyperparameter-free model implemented as a conditional diffusion model that balances short-time fidelity with long-time consistency by construction. Our model, Self-refining Neural Surrogate model (SNS), can be implemented as a standalone model that refines its own autoregressive outputs or as a complementary model to existing neural surrogates to ensure long-time consistency. We also demonstrate the numerical feasibility of SNS through high-fidelity simulations of complex dynamical systems over arbitrarily long time horizons.

</details>

---

### 42. [Fine-Grained Post-Training Quantization for Large Vision Language Models with Quantization-Aware Integrated Gradients](https://arxiv.org/abs/2603.17809)

**基本信息**

- 🔗 arXiv: [`2603.17809`](https://arxiv.org/abs/2603.17809)
- 👥 作者: Ziwei Xiang, Fanhu Zeng, Hongjian Fang 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17809.pdf)

**💡 相关性分析**

满足标准1：论文提出的细粒度后训练量化方法，直接关系到“化学大模型”在实际部署中的效率与精度权衡问题，为如何对复杂的化学AI模型进行高效压缩提供了先进的技术方案。

**📖 中文摘要**

本文针对大型视觉语言模型（LVLM）的后训练量化，提出了一种细粒度的、基于量化感知积分梯度的策略。该方法将敏感度评估从模态级别推进到令牌级别，以更精细地校准量化误差。虽然研究对象是通用LVLM，但其提出的“细粒度量化”和“基于积分梯度的敏感度评估”框架，对于量化“化学大模型”（尤其是多模态化学模型，如同时处理分子图和文本描述的模型）以降低部署成本，同时保持关键化学特征（如官能团、质谱峰）的推理精度，具有直接的技术参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Vision Language Models (LVLMs) have achieved remarkable success in a range of downstream tasks that require multimodal interaction, but their capabilities come with substantial computational and memory overhead, which hinders practical deployment. Among numerous acceleration techniques, post-training quantization is a popular and effective strategy for reducing memory cost and accelerating inference. However, existing LVLM quantization methods typically measure token sensitivity at the modality level, which fails to capture the complex cross-token interactions and falls short in quantitatively measuring the quantization error at the token level. As tokens interact within the model, the distinction between modalities gradually diminishes, suggesting the need for fine-grained calibration. Inspired by axiomatic attribution in mechanistic interpretability, we introduce a fine-grained quantization strategy on Quantization-aware Integrated Gradients (QIG), which leverages integrated gradients to quantitatively evaluate token sensitivity and push the granularity from modality level to token level, reflecting both inter-modality and intra-modality dynamics. Extensive experiments on multiple LVLMs under both W4A8 and W3A16 settings show that our method improves accuracy across models and benchmarks with negligible latency overhead. For example, under 3-bit weight-only quantization, our method improves the average accuracy of LLaVA-onevision-7B by 1.60%, reducing the gap to its full-precision counterpart to only 1.33%. The code is available at this https URL .

</details>

---

### 43. [Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Information Gain](https://arxiv.org/abs/2603.17815)

**基本信息**

- 🔗 arXiv: [`2603.17815`](https://arxiv.org/abs/2603.17815)
- 👥 作者: Corentin Royer, Debarun Bhattacharjya, Gaetano Rossiello 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17815.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于信息论的链式推理步骤监督方法，与“质谱结构推理”这一典型的多步、可解释推理任务高度相关，为构建可靠、透明的质谱解析AI模型提供了关键的技术思路。

**📖 中文摘要**

本文提出了一种基于信息论的新方法，用于自动生成步骤级标签，以监督大型语言模型的链式推理过程。该方法通过估计每个推理步骤对正确答案可能性的影响来提供步骤质量信号。这项研究虽然针对通用LLM的推理，但其核心思想——对多步推理过程进行细粒度、自动化的质量评估与优化——对于“质谱结构推理”任务至关重要。质谱解析本身就是一个典型的、需要多步推理（从峰匹配到碎片推导再到结构组装）的过程。该工作为开发能够进行可解释、可验证、步骤优化的质谱解析AI模型提供了重要的方法论工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-step reasoning improves the capabilities of large language models (LLMs) but increases the risk of errors propagating through intermediate steps. Process reward models (PRMs) mitigate this by scoring each step individually, enabling fine-grained supervision and improved reliability. Existing methods for training PRMs rely on costly human annotations or computationally intensive automatic labeling. We propose a novel approach to automatically generate step-level labels using Information Theory. Our method estimates how each reasoning step affects the likelihood of the correct answer, providing a signal of step quality. Importantly, it reduces computational complexity to $\mathcal{O}(N)$, improving over the previous $\mathcal{O}(N \log N)$ methods. We demonstrate that these labels enable effective chain-of-thought selection in best-of-$K$ evaluation settings across diverse reasoning benchmarks, including mathematics, Python programming, SQL, and scientific question answering. This work enables scalable and efficient supervision of LLM reasoning, particularly for tasks where error propagation is critical.

</details>

---

### 44. [TINA: Text-Free Inversion Attack for Unlearned Text-to-Image Diffusion Models](https://arxiv.org/abs/2603.17828)

**基本信息**

- 🔗 arXiv: [`2603.17828`](https://arxiv.org/abs/2603.17828)
- 👥 作者: Qianlong Xiang, Miao Zhang, Haoyu Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17828.pdf)

**💡 相关性分析**

满足标准1：论文关于扩散模型概念擦除与攻击的研究，触及了生成模型安全性与可控性的核心，这对于负责任地开发和应用“化学大模型”（尤其是分子生成模型）至关重要，提供了重要的安全性评估视角。

**📖 中文摘要**

本文提出了TINA，一种针对已进行概念擦除的文本到图像扩散模型的、无需文本的反转攻击方法。该方法通过DDIM反转在视觉层面探测被擦除概念是否仍存在可生成的路径。这项工作揭示了当前基于文本映射切断的擦除防御的局限性，并强调了直接操作内部视觉知识的重要性。这对于“化学大模型”的安全性和可控性研究具有警示和启发意义。例如，在训练模型避免生成危险分子时，不能仅依赖文本提示的阻断，而需确保模型内部的化学结构知识空间也得到了妥善约束。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although text-to-image diffusion models exhibit remarkable generative power, concept erasure techniques are essential for their safe deployment to prevent the creation of harmful content. This has fostered a dynamic interplay between the development of erasure defenses and the adversarial probes designed to bypass them, and this co-evolution has progressively enhanced the efficacy of erasure methods. However, this adversarial co-evolution has converged on a narrow, text-centric paradigm that equates erasure with severing the text-to-image mapping, ignoring that the underlying visual knowledge related to undesired concepts still persist. To substantiate this claim, we investigate from a visual perspective, leveraging DDIM inversion to probe whether a generative pathway for the erased concept can still be found. However, identifying such a visual generative pathway is challenging because standard text-guided DDIM inversion is actively resisted by text-centric defenses within the erased model. To address this, we introduce TINA, a novel Text-free INversion Attack, which enforces this visual-only probe by operating under a null-text condition, thereby avoiding existing text-centric defenses. Moreover, TINA integrates an optimization procedure to overcome the accumulating approximation errors that arise when standard inversion operates without its usual textual guidance. Our experiments demonstrate that TINA regenerates erased concepts from models treated with state-of-the-art unlearning. The success of TINA proves that current methods merely obscure concepts, highlighting an urgent need for paradigms that operate directly on internal visual knowledge.

</details>

---

### 45. [How do LLMs Compute Verbal Confidence](https://arxiv.org/abs/2603.17839)

**基本信息**

- 🔗 arXiv: [`2603.17839`](https://arxiv.org/abs/2603.17839)
- 👥 作者: Dharshan Kumaran, Arthur Conmy, Federico Barbero 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17839.pdf)

**💡 相关性分析**

满足标准1：论文对LLM置信度生成机制的基础性研究，直接关系到如何使“化学大模型”和“质谱结构推理”系统输出可靠的不确定性估计，是构建可信赖化学AI的关键支撑技术。

**📖 中文摘要**

本文通过实验探究了大型语言模型如何计算口头置信度。研究发现，置信度表示在答案相邻位置提前出现并被缓存，随后在需要时检索输出，且这些缓存表示包含了比词元对数概率更丰富的答案质量评估信息。这项基础性研究对于构建可靠的“化学大模型”和“质谱结构推理”系统具有重要意义。它揭示了模型内部自我评估（元认知）的机制，这有助于我们设计出能够输出不确定性量化、并在置信度低时寻求外部知识（如数据库）辅助的化学AI系统，从而提高其在开放领域应用中的可靠性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Verbal confidence -- prompting LLMs to state their confidence as a number or category -- is widely used to extract uncertainty estimates from black-box models. However, how LLMs internally generate such scores remains unknown. We address two questions: first, when confidence is computed - just-in-time when requested, or automatically during answer generation and cached for later retrieval; and second, what verbal confidence represents - token log-probabilities, or a richer evaluation of answer quality? Focusing on Gemma 3 27B and Qwen 2.5 7B, we provide convergent evidence for cached retrieval. Activation steering, patching, noising, and swap experiments reveal that confidence representations emerge at answer-adjacent positions before appearing at the verbalization site. Attention blocking pinpoints the information flow: confidence is gathered from answer tokens, cached at the first post-answer position, then retrieved for output. Critically, linear probing and variance partitioning reveal that these cached representations explain substantial variance in verbal confidence beyond token log-probabilities, suggesting a richer answer-quality evaluation rather than a simple fluency readout. These findings demonstrate that verbal confidence reflects automatic, sophisticated self-evaluation -- not post-hoc reconstruction -- with implications for understanding metacognition in LLMs and improving calibration.

</details>

---

### 46. [Video Understanding: From Geometry and Semantics to Unified Models](https://arxiv.org/abs/2603.17840)

**基本信息**

- 🔗 arXiv: [`2603.17840`](https://arxiv.org/abs/2603.17840)
- 👥 作者: Zhaochong An, Zirui Li, Mingqiao Ye 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17840.pdf)

**💡 相关性分析**

满足标准3：论文作为视频理解领域的综述，其总结的从任务特定模型到统一基础模型的发展范式、核心挑战和设计原则，为“化学大模型”这一平行领域的研究提供了重要的宏观视角和框架性借鉴。

**📖 中文摘要**

本文是一篇关于视频理解的综述，系统性地将文献组织为低层几何理解、高层语义理解和统一视频理解模型三个互补视角，并强调了从孤立任务特定管道向统一建模范式的更广泛转变。虽然主题是视频，但其总结的“从特定任务到统一模型”的发展趋势、时空推理的挑战以及统一基础模型的设计原则，与“化学大模型”领域的发展脉络高度相似。化学AI同样经历了从单一任务模型（如性质预测、反应预测）向能够处理多任务、多模态的通用化学基础模型发展的过程。该综述为化学领域构建统一的多任务、多模态基础模型提供了跨领域的框架性参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Video understanding aims to enable models to perceive, reason about, and interact with the dynamic visual world. In contrast to image understanding, video understanding inherently requires modeling temporal dynamics and evolving visual context, placing stronger demands on spatiotemporal reasoning and making it a foundational problem in computer vision. In this survey, we present a structured overview of video understanding by organizing the literature into three complementary perspectives: low-level video geometry understanding, high-level semantic understanding, and unified video understanding models. We further highlight a broader shift from isolated, task-specific pipelines toward unified modeling paradigms that can be adapted to diverse downstream objectives, enabling a more systematic view of recent progress. By consolidating these perspectives, this survey provides a coherent map of the evolving video understanding landscape, summarizes key modeling trends and design principles, and outlines open challenges toward building robust, scalable, and unified video foundation models.

</details>

---

### 47. [Revisiting foundation models for cell instance segmentation](https://arxiv.org/abs/2603.17845)

**基本信息**

- 🔗 arXiv: [`2603.17845`](https://arxiv.org/abs/2603.17845)
- 👥 作者: Anwai Archit, Constantin Pape
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17845.pdf)

**💡 相关性分析**

满足标准2：论文对一系列视觉基础模型在生物医学图像分割任务上的性能进行了系统性评估和比较，并提出了改进策略。其评估框架、模型比较结果以及适配方法，可作为重要的“数据资源”和“工具”参考，用于指导化学相关成像分析（如质谱成像）中基础模型的选择与微调。

**📖 中文摘要**

本文全面评估了用于细胞实例分割的基础模型（包括CellPoseSAM, CellSAM, μSAM）和通用分割基础模型（SAM, SAM2, SAM3），并引入了一种新的称为自动提示生成的实例分割策略。该工作虽然聚焦于生物医学图像分析，但其系统性的评估框架、对基础模型适应策略的探索以及提出的改进方法，对于“化学大模型”和“质谱分析”领域具有方法论上的参考价值。例如，在质谱成像数据分析中，同样需要对细胞或组织区域进行分割以关联化学组成信息。如何将通用视觉基础模型（如SAM系列）有效地适配到化学相关的显微图像分析任务，本文提供了可借鉴的实验范式和改进思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cell segmentation is a fundamental task in microscopy image analysis. Several foundation models for cell segmentation have been introduced, virtually all of them are extensions of Segment Anything Model (SAM), improving it for microscopy data. Recently, SAM2 and SAM3 have been published, further improving and extending the capabilities of general-purpose segmentation foundation models. Here, we comprehensively evaluate foundation models for cell segmentation (CellPoseSAM, CellSAM, $\mu$SAM) and for general-purpose segmentation (SAM, SAM2, SAM3) on a diverse set of (light) microscopy datasets, for tasks including cell, nucleus and organoid segmentation. Furthermore, we introduce a new instance segmentation strategy called automatic prompt generation (APG) that can be used to further improve SAM-based microscopy foundation models. APG consistently improves segmentation results for $\mu$SAM, which is used as the base model, and is competitive with the state-of-the-art model CellPoseSAM. Moreover, our work provides important lessons for adaptation strategies of SAM-style models to microscopy and provides a strategy for creating even more powerful microscopy foundation models. Our code is publicly available at this https URL .

</details>

---

### 48. [ProbeFlow: Training-Free Adaptive Flow Matching for Vision-Language-Action Models](https://arxiv.org/abs/2603.17850)

**基本信息**

- 🔗 arXiv: [`2603.17850`](https://arxiv.org/abs/2603.17850)
- 👥 作者: Zhou Fang, Jiaqi Wang, Yi Zhou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17850.pdf)

**💡 相关性分析**

满足标准1：论文提出的自适应流匹配推理框架，旨在高效加速生成式策略的推理。该技术可直接应用于“化学大模型”中基于流匹配或扩散模型的分子生成、构象搜索等计算密集型任务，提升其推理效率。

**📖 中文摘要**

本文提出了ProbeFlow，一个用于视觉-语言-动作模型中流匹配动作头的免训练自适应推理框架。通过评估轨迹几何复杂度，动态调度积分步骤以加速动作解码。这项工作针对机器人控制，但其核心创新——对基于流匹配的生成式策略进行自适应计算加速——与“化学大模型”中基于流匹配或扩散模型的分子构象生成、分子动力学模拟等任务高度相关。在这些任务中，同样需要对连续空间中的生成过程进行大量采样，计算成本高昂。ProbeFlow的自适应调度思想可直接迁移，用于加速化学生成模型的推理过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent Vision-Language-Action (VLA) models equipped with Flow Matching (FM) action heads achieve state-of-the-art performance in complex robot manipulation. However, the multi-step iterative ODE solving required by FM introduces inference latency that precludes responsive physical control. While current acceleration efforts optimize the Vision-Language Model (VLM) backbone, the action head bottleneck remains overlooked. To address this, we propose ProbeFlow, a training-free adaptive inference framework tai- lored for continuous robotic control. By evaluating geometric trajectory complexity via the cosine similarity between initial and lookahead velocity vectors, ProbeFlow dynamically sched- ules integration steps to prune redundant network evaluations. On the MetaWorld benchmark, it accelerates action decoding by 14.8x (reducing average steps from N = 50 to 2.6) and cuts end-to-end system latency by 2.8x without compromising the manipulation success rate. On the long-horizon LIBERO benchmark, the probe automatically allocates a denser schedule to navigate semantic bottlenecks, effectively resolving the flow solver delay. Real-world physical deployments confirm that ProbeFlow successfully mitigates action decoding latency while ensuring execution stability, offering a highly practical solution for low-latency continuous generative policies.

</details>

---

### 49. [DebugLM: Learning Traceable Training Data Provenance for LLMs](https://arxiv.org/abs/2603.17884)

**基本信息**

- 🔗 arXiv: [`2603.17884`](https://arxiv.org/abs/2603.17884)
- 👥 作者: Wenjie Jacky Mo, Qin Liu, Xiaofei Wen 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17884.pdf)

**💡 相关性分析**

满足标准1：论文提出的使LLM行为可追溯至训练数据源的技术，直接关系到“化学大模型”的可信度、安全性和可审计性，是构建负责任化学AI的核心技术之一。

**📖 中文摘要**

本文提出了DebugLM框架，旨在为大型语言模型内置数据溯源能力，使其能够将行为追溯到特定的训练数据源。模型学习将响应与唯一的溯源标签相关联。这项研究对于开发透明、可审计的“化学大模型”至关重要。在化学领域，模型的预测（如分子毒性、反应产物）需要极高的可靠性，并能追溯其判断依据（来源于哪个训练数据集或知识库）。DebugLM提供了一种使模型行为可追溯的机制，这对于化学AI在药物发现、安全评估等高风险场景中的应用具有重要价值，有助于建立信任和进行责任界定。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are trained through multi-stage pipelines over heterogeneous data sources, yet developers lack a principled way to pinpoint the specific data responsible for an observed behavior. This lack of observability reduces debugging to reactive patching and makes failures prone to recur under distribution shift or subsequent model updates. To address this limitation, we propose DebugLM, a framework that equips LLMs with built-in data provenance, enabling them to explicitly trace the origins of their behaviors to specific training data sources. Specifically, the model learns to associate its responses with unique provenance tags that indicate the responsible dataset, empowering developers to precisely identify where undesirable behaviors are learned. Building on this capability, DebugLM further supports targeted test-time remediation, enabling developers to selectively trigger targeted refusal for specified data sources without retraining or modifying model parameters. Experiments demonstrate that DebugLM provides accurate behavior tracing in multi-stage training pipelines and effective test-time remediation while preserving the general utility of the model.

</details>

---

### 50. [RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Device LLM Inference](https://arxiv.org/abs/2603.17891)

**基本信息**

- 🔗 arXiv: [`2603.17891`](https://arxiv.org/abs/2603.17891)
- 👥 作者: Arpit Singh Gautam, Saurabh Jha
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17891.pdf)

**💡 相关性分析**

满足标准1：论文提出的先进模型量化框架和技术，直接针对大模型的高效部署问题，对于将计算密集型的“化学大模型”部署到实际科研和生产环境（如嵌入式质谱分析仪）至关重要，提供了关键的模型压缩与加速解决方案。

**📖 中文摘要**

本文提出了RAMP，一个基于强化学习的自适应混合精度量化框架，用于在设备上进行高效的LLM推理。它学习每层的比特宽度分配，以在全局比特预算下最小化困惑度。论文还引入了Scale Folding技术来稳定4比特以下的量化。这项工作虽然针对通用LLM，但其先进的量化技术（混合精度、强化学习搜索、低比特稳定化）对于在资源受限环境下（如实验室边缘设备）部署大型“化学大模型”（如用于实时光谱分析或分子设计的模型）具有直接且重要的应用价值。其方法可以显著降低化学大模型的存储和计算开销，促进其实际落地。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Post training quantization is essential for deploying large language models (LLMs) on resource constrained hardware, yet state of the art methods enforce uniform bit widths across layers, yielding suboptimal accuracy efficiency trade offs. We present RAMP (Reinforcement Adaptive Mixed Precision), an off policy Soft Actor Critic framework that learns per layer bit width assignments to minimize perplexity under a global bit budget. The policy conditions on an 11 dimensional embedding of activation statistics, weight properties, and structural descriptors, enabling zero shot transfer across model families and scales. To enable stable sub 4 bit quantization, we introduce Scale Folding, a preconditioning technique that migrates activation outliers into weights via per channel scaling and normalization layer compensation. A quality prioritized reward with asymmetric penalties and budget cliffs drives rapid convergence. On Llama 2 7B, RAMP achieves 5.54 perplexity at 3.68GB (3.65 effective bits), outperforming uniform 4 bit AWQ (5.60 at 3.90 GB) and GPTQ by 6% in size and 1% to3% in quality. Critically, a policy trained only on Llama 2 7B generalizes zero shot to Llama 2 13B and Mistral 7B, often surpassing target specific training, supporting the hypothesis that quantization sensitivity is primarily architectural. The HALO pipeline exports allocations to GGUF format for kernel free inference on CPUs, GPUs, and edge devices, retaining 99.5% of FP16 commonsense reasoning performance.

</details>

---

### 51. [scicode-lint: Detecting Methodology Bugs in Scientific Python Code with LLM-Generated Patterns](https://arxiv.org/abs/2603.17893)

**基本信息**

- 🔗 arXiv: [`2603.17893`](https://arxiv.org/abs/2603.17893)
- 👥 作者: Sergey V. Samsonau
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17893.pdf)

**💡 相关性分析**

满足标准2：论文提出的scicode-lint是一个用于自动检测科学代码（包括化学信息学和质谱分析中常用的ML代码）方法论错误的工具。它提供了可直接用于提升化学AI研究代码质量的资源和工具。

**📖 中文摘要**

本文介绍了scicode-lint，一个用于检测科学Python代码中方法论错误的工具。它采用两层架构，利用前沿大模型在构建时生成检测模式，在运行时使用小型本地模型执行。该工具旨在自动检测数据泄露、错误的交叉验证、缺失随机种子等机器学习工作流中的常见错误。这项研究与“化学信息学”和“质谱分析”中基于机器学习的工作流高度相关。在这些领域，数据分析流程复杂，容易引入类似的方法论错误，导致结果不可靠。scicode-lint提供的自动化检测框架，可以作为保障化学与质谱数据分析代码质量、提升研究可重复性的重要工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Methodology bugs in scientific Python code produce plausible but incorrect results that traditional linters and static analysis tools cannot detect. Several research groups have built ML-specific linters, demonstrating that detection is feasible. Yet these tools share a sustainability problem: dependency on specific pylint or Python versions, limited packaging, and reliance on manual engineering for every new pattern. As AI-generated code increases the volume of scientific software, the need for automated methodology checking (such as detecting data leakage, incorrect cross-validation, and missing random seeds) grows. We present scicode-lint, whose two-tier architecture separates pattern design (frontier models at build time) from execution (small local model at runtime). Patterns are generated, not hand-coded; adapting to new library versions costs tokens, not engineering hours. On Kaggle notebooks with human-labeled ground truth, preprocessing leakage detection reaches 65% precision at 100% recall; on 38 published scientific papers applying AI/ML, precision is 62% (LLM-judged) with substantial variation across pattern categories; on a held-out paper set, precision is 54%. On controlled tests, scicode-lint achieves 97.7% accuracy across 66 patterns.

</details>

---

### 52. [Only relative ranks matter in weight-clustered large language models](https://arxiv.org/abs/2603.17917)

**基本信息**

- 🔗 arXiv: [`2603.17917`](https://arxiv.org/abs/2603.17917)
- 👥 作者: Borja Aizpurua, Sukhbinder Singh, Román Orús
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17917.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕化学信息学/人工智能领域中的“化学大模型”（具体指大型语言模型的权重压缩与鲁棒性分析）展开，其方法（权重聚类、相对排名分析）和结论对理解和构建高效、鲁棒的化学领域大模型具有直接参考价值。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）的权重压缩问题，重点关注权重聚类方法。研究发现，对于LLMs的性能而言，权重的相对排名（即一个连接比另一个更强或更弱）比精确的数值大小更为关键。通过将预训练模型的权重矩阵替换为K-means聚类得到的K个共享值，可以在不重新训练的情况下，仅用16-64个不同的值就保持较强的模型准确性。文章进一步通过随机化聚类中心（同时保持分配不变）进行实验，发现打乱聚类的相对排名会严重损害模型质量（困惑度可能增加数个数量级），而保持排名顺序的随机化则几乎不会造成损失。这一基于权重的视角为模型压缩和鲁棒性提供了新的见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) contain billions of parameters, yet many exact values are not essential. We show that what matters most is the relative rank of weights-whether one connection is stronger or weaker than another-rather than precise magnitudes. To reduce the number of unique weight values, we apply weight clustering to pretrained models, replacing every weight matrix with K shared values from K-means. For Llama 3.1-8B-Instruct and SmolLM2-135M, reducing each matrix to only 16-64 distinct values preserves strong accuracy without retraining, providing a simple, training-free method to compress LLMs on disk. Optionally fine-tuning only the cluster means (centroids) recovers 30-40 percent of the remaining accuracy gap at minimal cost. We then systematically randomize cluster means while keeping assignments fixed. Scrambling the relative ranks of the clusters degrades quality sharply-perplexity can increase by orders of magnitude-even when global statistics such as mean and variance are preserved. In contrast, rank-preserving randomizations cause almost no loss at mid and late layers. On the other hand, when many layers are perturbed simultaneously, progressive layer-by-layer replacement reveals that scale drift-not rank distortion-is the dominant collapse mechanism; however, an affine correction w' = aw + b with a > 0 (which preserves both rank order and overall weight distribution) can substantially delay this drift. This rank-based perspective offers a new lens on model compression and robustness.

</details>

---

### 53. [Training Diffusion Language Models for Black-Box Optimization](https://arxiv.org/abs/2603.17919)

**基本信息**

- 🔗 arXiv: [`2603.17919`](https://arxiv.org/abs/2603.17919)
- 👥 作者: Zipeng Sun, Can Chen, Ye Yuan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17919.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“化学大模型”在科学发现（如材料、DNA设计）中的应用范式。它探讨了如何将扩散语言模型（一种生成式大模型）专门适配用于解决化学、材料等领域常见的黑盒优化问题，这与利用AI大模型进行分子或材料设计的主题高度相关。

**📖 中文摘要**

本文研究离线黑盒优化（BBO）问题，旨在从设计和标签的离线数据集中发现改进的设计。针对自回归LLMs在BBO中因左到右生成而难以捕捉设计问题中强双向依赖关系的局限性，论文提出使用扩散语言模型（Diffusion LLMs）来适应离线BBO，以利用其双向建模能力。为了弥合扩散LLMs的自然文本预训练与BBO中异构信号（提示、设计、标签）之间的领域差距，作者构建了一个统一的提示-响应语料库，并引入分隔符标记来显式标记字段边界以进行领域适应。此外，还提出了一个两阶段的后训练框架，使扩散LLM的生成与高标签设计对齐。该方法在Design-Bench的小数据设置上取得了最先进的结果。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study offline black-box optimization (BBO), aiming to discover improved designs from an offline dataset of designs and labels, a problem common in robotics, DNA, and materials science with limited labeled samples. While recent work applies autoregressive LLMs to BBO by formatting tasks as natural-language prompts, their left-to-right design generation struggles to capture the strong bidirectional dependencies inherent in design problems. To address this, we propose adapting diffusion LLMs to offline BBO to leverage their bidirectional modeling capabilities. However, a domain gap exists between the natural text pre-training of diffusion LLMs and the heterogeneous signals in BBO (prompts, designs, and labels). To bridge this gap, we construct a unified prompt-response corpus and introduce delimiter tokens to explicitly mark field boundaries for domain adaptation. We further propose a two-stage post-training framework to align the diffusion LLM generation with high-label designs. The first stage performs supervised fine-tuning on the unified dataset via masked-response prediction, and the second stage adopts reinforcement learning with rewards defined by label improvements. Our method achieves state-of-the-art results on Design-Bench small-data settings.

</details>

---

### 54. [Gaussian Process Regression-based Knowledge Distillation Framework for Simultaneous Prediction of Physical and Mechanical Properties of Epoxy Polymers](https://arxiv.org/abs/2603.16925)

**基本信息**

- 🔗 arXiv: [`2603.16925`](https://arxiv.org/abs/2603.16925)
- 👥 作者: Sindu B.S., Jan Hamaekers
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个机器学习框架（GPR-KD）用于预测环氧聚合物的多种性质。这属于化学信息学的核心领域，即利用AI/ML模型进行化学物质的性质预测与设计。论文提出的方法（知识蒸馏、多任务学习）对构建用于化学性质预测的专用模型具有参考价值。

**📖 中文摘要**

本文针对环氧聚合物，开发了一个基于高斯过程回归的知识蒸馏（GPR-KD）框架，用于同时预测其多种物理（玻璃化转变温度、密度）和机械性能（弹性模量、拉伸强度等）。该模型在涵盖多种单体类别（9种树脂，40种硬化剂）的实验文献数据上进行训练。框架使用单独的GPR模型作为教师模型来捕获非线性特征-属性关系，同时使用统一的神经网络学生模型来同时学习所有属性的蒸馏知识。通过将目标属性编码为输入特征，学生模型利用了跨属性的相关性。使用RDKit从SMILES表示中提取分子级描述符，从而创建了一个物理信息模型。该框架结合了GPR的可解释性和鲁棒性以及深度学习的可扩展性和泛化能力。比较分析表明，其预测精度优于传统ML模型。同时的多属性预测通过跨相关属性的信息共享进一步提高了准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Epoxy polymers are widely used due to their multifunctional properties, but machine learning (ML) applications remain limited owing to their complex 3D molecular structure, multi-component nature, and lack of curated datasets. Existing ML studies are largely restricted to simulation data, specific properties, or narrow constituent ranges. To address these limitations, we developed an informed Gaussian Process Regression-based Knowledge Distillation (GPR-KD) framework for predicting multiple physical (glass transition temperature, density) and mechanical properties (elastic modulus, tensile strength, compressive strength, flexural strength, fracture energy, adhesive strength) of thermoset epoxy polymers. The model was trained on experimental literature data covering diverse monomer classes (9 resins, 40 hardeners). Individual GPR models serve as teacher models capturing nonlinear feature-property relationships, while a unified neural network student model learns distilled knowledge across all properties simultaneously. By encoding the target property as an input feature, the student model leverages cross-property correlations. Molecular-level descriptors extracted from SMILES representations using RDKit create a physics-informed model. The framework combines GPR interpretability and robustness with deep learning scalability and generalization. Comparative analysis demonstrates superior prediction accuracy over conventional ML models. Simultaneous multi-property prediction further improves accuracy through information sharing across correlated properties. The proposed framework enables accelerated design of novel epoxy polymers with tailored properties.

</details>

---

### 55. [Machine intelligence supports the full chain of 2D dendrite synthesis](https://arxiv.org/abs/2603.16959)

**基本信息**

- 🔗 arXiv: [`2603.16959`](https://arxiv.org/abs/2603.16959)
- 👥 作者: Wenqiang Huang, Susu Fang, Xuhang Gu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16959.pdf)

**💡 相关性分析**

满足标准1和2：1) 核心主题相关：论文的核心是使用机器学习（主动学习、数据增强、可解释ML）来优化和指导二维材料的合成过程，这直接关联化学信息学中“AI for Materials Discovery/Synthesis”的主题。2) 数据资源相关：论文提出的框架（包括主动学习工作流、数据增强策略和机理建模方法）本身构成了一个可用于类似材料合成优化问题的工具和方法资源。

**📖 中文摘要**

本文以二维枝晶（如ReSe2）的化学气相沉积生长为例，提出了一个由机器智能驱动的材料合成全链条支持框架。该框架涵盖了快速工艺优化、精准定制合成和全面机理理解。首先，将主动学习集成到实验工作流程中，通过仅60次实验（4次迭代）就找到了生长高分支、电催化活性ReSe2枝晶的最佳配方。其次，开发了一种结合基于树的机器学习算法的预测精度引导数据增强策略，仅通过9次额外实验就揭示了5个工艺变量与ReSe2枝晶分形维数之间的非线性关系，从而指导合成各种用户定义分形维数的枝晶。最后，通过整合跨尺度表征、可解释ML模型以及热力学和动力学领域的知识，构建了一个数据-知识双驱动的机理模型，揭示了多个工艺参数对产物形态的协同贡献。这项工作展示了机器学习改变材料合成研究范式的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Exemplified by the chemical vapor deposition growth of two-dimensional dendrites, which has potential applications in catalysis and presents a parameter-intensive, data-scarce and reaction process-complex model problem, we devise a machine intelligence-empowered framework for the full chain support of material synthesis, encompassing rapid process optimization, accurate customized synthesis, and comprehensive mechanism this http URL , active learning is integrated into the experimental workflow, identifying an optimal recipe for the growth of highly-branched, electrocatalytically-active ReSe2 dendrites through 60 experiments (4 iterations), which account for less than 1.3% of the numerous possible parameter this http URL , a prediction accuracy-guided data augmentation strategy is developed combined with a tree-based machine learning (ML) algorithm, unveiling a non-linear correlation between 5 process variables and fractal dimension (DF) of ReSe2 dendrites with only 9 experiment additions, which guides the synthesis of various user-defined DF. Finally, we construct a data-knowledge dual-driven mechanism model by integration of cross-scale characterizations, interpretable ML models, and domain knowledge in thermodynamics and kinetics, unraveling synergistic contributions of multiple process parameters to the product morphology. This work demonstrates the ML potential to transform the research paradigm and is adaptable to broader material synthesis.

</details>

---

### 56. [Rapid Neural Network Prediction of Linear Block Copolymer Free Energies](https://arxiv.org/abs/2603.17391)

**基本信息**

- 🔗 arXiv: [`2603.17391`](https://arxiv.org/abs/2603.17391)
- 👥 作者: Ian Chen, Alfredo Alexander-Katz
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17391.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发神经网络模型来快速、准确地预测聚合物（线性二嵌段共聚物）系统的自由能。自由能是决定相行为和热力学稳定性的关键物理量，其快速预测对于高分子材料的设计至关重要。这属于化学信息学和计算化学中利用AI加速分子模拟和性质预测的典型研究方向。

**📖 中文摘要**

本文开发了一个机器学习框架，用于根据模拟得出的能量描述符快速预测线性二嵌段共聚物系统的过量自由能。使用耗散粒子动力学模拟，构建了一个包含异质相互作用能、均质相互作用能和键合弹簧能等每链能量统计量的数据集，并训练前馈神经网络来学习这些描述符与使用分层Bennett接受比（BAR）程序计算的自由能之间的关系。所得模型能够准确再现一系列链长、组成和密度下的参考自由能，包括训练中未见的聚合物架构。在直接、暴力BAR估计因相空间重叠差而变得不可靠的情况下，神经网络预测仍与参考值保持一致。这些结果表明，基于物理信息的机器学习模型可以作为昂贵自由能计算的有效替代品，并为加速聚合物系统的热力学分析提供了一种有前景的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Free energies are fundamental quantities governing phase behavior and thermodynamic stability in polymer systems, yet their accurate computation often requires extensive simulations and post-processing techniques such as the Bennett Acceptance Ratio (BAR). While BAR provides reliable estimates when applied between closely related thermodynamic states, evaluating free energies across large changes in interaction strength typically requires a sequence of intermediate simulations to maintain sufficient phase-space overlap, substantially increasing computational cost. In this work we develop a machine learning framework for rapidly predicting excess free energies of linear diblock copolymer systems from simulation-derived energetic descriptors. Using dissipative particle dynamics simulations of freely-jointed chain polymers, we construct a dataset of per-chain energetic statistics, including heterogeneous interaction energies, homogeneous interaction energies, and bonded spring energies, and train feed-forward neural networks to learn the relationship between these descriptors and free energies computed using a stratified BAR procedure. The resulting models accurately reproduce the reference free energies across a range of chain lengths, compositions, and densities, including polymer architectures held out from training. In regimes where direct, brute-force BAR estimates become unreliable due to poor phase-space overlap, the neural network predictions remain consistent with the reference values. These results demonstrate that physically informed machine learning models can serve as efficient surrogates for expensive free-energy calculations and provide a promising approach for accelerating thermodynamic analysis of polymer systems.

</details>

---

### 57. [On the number of inequivalent linearized Reed-Solomon codes](https://arxiv.org/abs/2603.17636)

**基本信息**

- 🔗 arXiv: [`2603.17636`](https://arxiv.org/abs/2603.17636)
- 👥 作者: Jonathan Mannaert, Marta Messia, Ferdinando Zullo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17636.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于子空间系统和代数结构的等价性分析框架，其核心方法论可直接应用于化学信息学中分子结构的表示、比较和推理问题，为化学大模型和质谱结构推理中的关键挑战（如分子表示和等价性判断）提供了理论工具。

**📖 中文摘要**

本文研究了线性化Reed-Solomon（LRS）码的等价性问题，并确定了该码族中不等价码的数量。虽然论文本身属于编码理论范畴，但其核心方法——利用有限域子空间系统与度量码之间的对应关系来分析结构等价性——与化学信息学中分子结构的表示、比较和推理问题在方法论上高度相关。化学大模型和质谱结构推理任务的核心挑战之一是如何对分子（可视为具有特定拓扑和属性的图或子空间系统）进行有效的数学表示和等价性判断，以进行准确的谱图预测或结构解析。本文提供的基于代数结构的等价性刻画框架，为开发新型的、具有严格数学保证的分子表示和比较算法提供了理论工具和灵感。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Linearized Reed-Solomon (LRS) codes form an important family of maximum sum-rank distance (MSRD) codes that generalize both Reed--Solomon codes and Gabidulin codes. In this paper we study the equivalence problem for LRS codes and determine the number of inequivalent codes within this family. Using the correspondence between sum-rank metric codes and systems of $\mathbb{F}_q$-subspaces, we analyze the stabilizer of the Gabidulin system and derive a characterization of equivalence between LRS codes. In particular, we prove that two LRS codes are equivalent if and only if the sets of norms that define the codes coincide up to multiplication by an element of $\mathbb{F}_q^\ast$. This description allows us to reduce the classification problem to the action of $\mathbb{F}_q^\ast$ on subsets of $\mathbb{F}_q^\ast$. As a consequence, we derive formulas for the number of inequivalent linearized Reed-Solomon codes and illustrate the results with explicit examples.

</details>

---

### 58. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕利用机器学习（特别是基础模型）和先进计算技术（包括量子计算）来加速和提升药物发现过程的精度，这属于“化学大模型”在具体领域（药物发现）的前沿应用和展望。

**📖 中文摘要**

本文探讨了高性能计算（HPC）、机器学习（ML）和量子计算（QC）的融合如何解决下一代药物发现中的瓶颈。论文明确指出，ML基础模型（如FeNNix-Bio1）能够实现量子精度的模拟，但其数据生成仍受限于经典计算。而利用混合QPU-GPU架构的高性能量子计算（HPQC）将成为量子化学数据的终极加速器。通过希尔伯特空间映射，这些系统可以在绕过经典近似启发式方法的同时实现真正的化学精度。本文详细阐述了这种三方融合如何优化从初始系统准备到ML驱动的高保真模拟的整个药物发现流程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

### 59. [Hi-GMAE: Hierarchical Graph Masked Autoencoders](https://arxiv.org/abs/2405.10642)

**基本信息**

- 🔗 arXiv: [`2405.10642`](https://arxiv.org/abs/2405.10642)
- 👥 作者: Chuang Liu, Zelin Yao, Xueqi Ma 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2405.10642.pdf)

**💡 相关性分析**

满足标准1：论文提出的Hi-GMAE框架专门用于学习具有分层结构的图数据（如分子图）的表示。分子图是化学信息学的核心数据结构，学习其高质量表示是构建化学大模型和进行质谱结构推理的基础。因此，该工作直接为核心主题提供了先进的图表示学习方法。

**📖 中文摘要**

本文提出了分层图掩码自编码器（Hi-GMAE），这是一种新颖的多尺度图掩码自编码器框架，旨在处理图中的分层结构。作者指出，现有的单尺度GMAE模型主要关注重建节点级信息，但往往忽略了现实世界图中固有的复杂分层结构（例如分子图中的原子-官能团-分子结构）。Hi-GMAE通过图池化构建多尺度图层次结构，并采用从粗到细的掩码策略和渐进恢复策略来学习全面的图信息。实验在17个图数据集上进行，覆盖两个图学习任务，结果表明Hi-GMAE在捕获全面图信息方面优于29个最先进的自监督竞争对手。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Graph Masked Autoencoders (GMAEs) have emerged as a notable self-supervised learning approach for graph-structured data. Existing GMAE models primarily focus on reconstructing node-level information, categorizing them as single-scale GMAEs. This methodology, while effective in certain contexts, tends to overlook the complex hierarchical structures inherent in many real-world graphs. For instance, molecular graphs exhibit a clear hierarchical organization in the form of the atoms-functional groups-molecules structure. Therefore, the inability of single-scale GMAE models to incorporate these hierarchical relationships often results in an inadequate capture of crucial high-level graph information, leading to a noticeable decline in performance. To address this limitation, we propose Hierarchical Graph Masked AutoEncoders (Hi-GMAE), a novel multi-scale GMAE framework designed to handle the hierarchical structures within graphs. First, Hi-GMAE constructs a multi-scale graph hierarchy through graph pooling, enabling the exploration of graph structures across different granularity levels. To ensure masking uniformity of subgraphs across these scales, we propose a novel coarse-to-fine strategy that initiates masking at the coarsest scale and progressively back-projects the mask to finer scales. Furthermore, we integrate a gradual recovery strategy with the masking process to mitigate the learning challenges posed by completely masked subgraphs. Our experiments on 17 graph datasets, covering two graph learning tasks, consistently demonstrate that Hi-GMAE outperforms 29 state-of-the-art self-supervised competitors in capturing comprehensive graph information.

</details>

---

### 60. [Beyond Static Pattern Matching? Rethinking Automatic Cryptographic API Misuse Detection in the Era of LLMs](https://arxiv.org/abs/2407.16576)

**基本信息**

- 🔗 arXiv: [`2407.16576`](https://arxiv.org/abs/2407.16576)
- 👥 作者: Yifan Xia, Zichen Xie, Peiyu Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2407.16576.pdf)

**💡 相关性分析**

满足标准1：虽然论文主要关注密码学API的安全分析，但其核心是研究如何利用和增强大型语言模型（LLMs）在复杂代码理解和推理任务中的能力。LLMs作为当前“化学大模型”的一种重要实现形式（如用于分子性质预测、反应生成、谱图解释的LLMs），其能力边界、可靠性提升方法（如通过领域对齐和验证技术）的研究对化学信息学领域具有直接的借鉴意义。该工作展示了如何使LLMs在需要精确推理的专业领域（类比于化学）变得更可靠。

**📖 中文摘要**

本文首次系统性地探索了大型语言模型（LLMs）在密码学API误用检测中的应用。研究发现，直接应用LLMs会导致超过一半的初始报告为误报，但通过将检测范围与现实场景对齐并采用新颖的代码和分析验证技术，可以显著提高LLM检测的可靠性，实现接近90%的检测召回率。这一改进大大超过了传统方法，并导致在已建立的基准中发现了先前未知的漏洞。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While the automated detection of cryptographic API misuses has progressed significantly, its precision diminishes for intricate targets due to the reliance on manually defined patterns. Large Language Models (LLMs) offer a promising context-aware understanding to address this shortcoming, yet the stochastic nature and the hallucination issue pose challenges to their applications in precise security analysis. This paper presents the first systematic study to explore LLMs' application in cryptographic API misuse detection. Our findings are noteworthy: The instability of directly applying LLMs results in over half of the initial reports being false positives. Despite this, the reliability of LLM-based detection could be significantly enhanced by aligning detection scopes with realistic scenarios and employing a novel code and analysis validation technique, achieving a nearly 90% detection recall. This improvement substantially surpasses traditional methods and leads to the discovery of previously unknown vulnerabilities in established benchmarks. Nevertheless, we identify recurring failure patterns that illustrate current LLMs' blind spots. Leveraging these findings, we deploy an LLM-based detection system and uncover 63 new vulnerabilities (47 confirmed, 7 already fixed) in open-source Java and Python repositories, including prominent projects like Apache.

</details>

---

### 61. [Den-TP: A Density-Balanced Data Curation and Evaluation Framework for Trajectory Prediction](https://arxiv.org/abs/2409.17385)

**基本信息**

- 🔗 arXiv: [`2409.17385`](https://arxiv.org/abs/2409.17385)
- 👥 作者: Ruining Yang, Yi Xu, Yun Fu 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2409.17385.pdf)

**💡 相关性分析**

满足标准2：论文提出的Den-TP框架提供了一种系统性的、密度感知的数据集管理和评估方法。在质谱结构推理任务中，数据集同样可能存在长尾分布（例如，某些复杂或稀有分子结构的谱图数据稀缺），导致模型在安全关键或罕见案例上表现不佳。Den-TP中关于数据重平衡、代表性样本选择以及针对长尾场景的评估协议，为构建更公平、更鲁棒的化学大模型和质谱数据集提供了宝贵的工具和方法论参考。

**📖 中文摘要**

本文提出了Den-TP，一个用于轨迹预测的密度感知数据集管理和评估框架。该框架从数据中心的视角重新审视轨迹预测，首先使用智能体数量作为交互复杂度的代理，将数据划分为密度条件区域。然后应用基于梯度的次模选择目标，在每个区域内选择代表性样本，同时明确地重新平衡不同密度区域的数据。生成的子集将数据集大小减少了50%，但保持了整体性能，并显著提高了高密度场景下的鲁棒性。此外，作者引入了密度条件评估协议，揭示了传统指标所忽视的长尾故障模式。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Trajectory prediction in autonomous driving has traditionally been studied from a model-centric perspective. However, existing datasets exhibit a strong long-tail distribution in scenario density, where common low-density cases dominate and safety-critical high-density cases are severely underrepresented. This imbalance limits model robustness and hides failure modes when standard evaluations average errors across all scenarios. We revisit trajectory prediction from a data-centric perspective and present Den-TP, a framework for density-aware dataset curation and evaluation. Den-TP first partitions data into density-conditioned regions using agent count as a dataset-agnostic proxy for interaction complexity. It then applies a gradient-based submodular selection objective to choose representative samples within each region while explicitly rebalancing across densities. The resulting subset reduces the dataset size by 50\% yet preserves overall performance and significantly improves robustness in high-density scenarios. We further introduce density-conditioned evaluation protocols that reveal long-tail failure modes overlooked by conventional metrics. Experiments on Argoverse 1 and 2 with state-of-the-art models show that robust trajectory prediction depends not only on data scale, but also on balancing scenario density.

</details>

---

### 62. [CMADiff: Cross-Modal Aligned Diffusion for Controllable Protein Generation](https://arxiv.org/abs/2503.21450)

**基本信息**

- 🔗 arXiv: [`2503.21450`](https://arxiv.org/abs/2503.21450)
- 👥 作者: Changjian Zhou, Yuexi Qiu, Jia Song 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.21450.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于可控蛋白质生成的AI模型框架（CMADiff）。这直接属于“化学大模型”在生物分子设计领域的应用。该模型整合了文本描述、理化性质和扩散模型，旨在生成符合特定功能或性质要求的蛋白质序列，是化学信息学和AI交叉前沿的典型工作。

**📖 中文摘要**

本文提出了CMADiff，一个通过潜在扩散过程将蛋白质序列的理化性质与基于文本的描述对齐，从而实现可控蛋白质生成的新框架。具体来说，CMADiff采用条件变分自编码器（CVAE）将理化特征作为条件输入，形成一个捕获生物学特征的鲁棒潜在空间。在该潜在空间中，应用条件扩散过程，该过程由基于对比学习的模块BioAligner引导，该模块将文本描述与蛋白质特征对齐，从而实现文本驱动的蛋白质序列生成控制。实验结果表明，CMADiff在蛋白质序列生成基准测试中表现出色，并显示出未来应用的强大潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI-assisted protein design has emerged as a critical tool for advancing biotechnology, as deep generative models have demonstrated their reliability in this domain. However, most existing models primarily utilize protein sequence or structural data for training, neglecting the physicochemical properties of this http URL , they are deficient to control the generation of proteins in intuitive conditions. To address these limitations,we propose CMADiff here, a novel framework that enables controllable protein generation by aligning the physicochemical properties of protein sequences with text-based descriptions through a latent diffusion process. Specifically, CMADiff employs a Conditional Variational Autoencoder (CVAE) to integrate physicochemical features as conditional input, forming a robust latent space that captures biological traits. In this latent space, we apply a conditional diffusion process, which is guided by BioAligner, a contrastive learning-based module that aligns text descriptions with protein features, enabling text-driven control over protein sequence generation. Validated by a series of evaluations including AlphaFold3, the experimental results indicate that CMADiff outperforms protein sequence generation benchmarks and holds strong potential for future applications. The implementation and code are available at this https URL .

</details>

---

### 63. [Domain and Task-Focused Example Selection for Data-Efficient Contrastive Medical Image Segmentation](https://arxiv.org/abs/2505.19208)

**基本信息**

- 🔗 arXiv: [`2505.19208`](https://arxiv.org/abs/2505.19208)
- 👥 作者: Tyler Ward, Aaron Moseley, Abdullah-Al-Zubaer Imran
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.19208.pdf)

**💡 相关性分析**

满足标准2：论文提出的PolyCL框架是一种先进的自监督学习算法，旨在从有限标注数据中学习鲁棒的视觉表示。虽然应用于医学图像，但其核心方法——利用图像间关系进行对比学习、结合基础模型（SAM）进行增强——对于化学信息学中面临类似数据标注瓶颈的任务（例如，从有限的标记质谱或分子图像数据中学习通用表示）具有重要的参考价值。该工作为相关领域提供了可借鉴的数据高效学习工具。

**📖 中文摘要**

本文提出了一种用于医学图像分割的新型自监督对比学习框架PolyCL，该框架利用不同图像之间的固有关系，在不需像素级标注或不合理数据增强的情况下，以任务相关的方式从创新的替代任务中学习并迁移对分割有用的上下文感知判别特征。此外，作者将Segment Anything Model（SAM）以两种新颖方式集成到框架中：作为后处理细化模块，以及通过SAM 2从单个标注的2D切片生成体积分割的传播机制。在三个公共CT数据集上的实验评估表明，PolyCL在低数据和跨域场景下均优于全监督和自监督基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Segmentation is one of the most important tasks in the medical imaging pipeline as it influences a number of image-based decisions. To be effective, fully supervised segmentation approaches require large amounts of manually annotated training data. However, the pixel-level annotation process is expensive, time-consuming, and error-prone, hindering progress and making it challenging to perform effective segmentations. Therefore, models must learn efficiently from limited labeled data. Self-supervised learning (SSL), particularly contrastive learning via pre-training on unlabeled data and fine-tuning on limited annotations, can facilitate such limited labeled image segmentation. To this end, we propose a novel self-supervised contrastive learning framework for medical image segmentation, leveraging inherent relationships of different images, dubbed PolyCL. Without requiring any pixel-level annotations or unreasonable data augmentations, our PolyCL learns and transfers context-aware discriminant features useful for segmentation from an innovative surrogate, in a task-related manner. Additionally, we integrate the Segment Anything Model (SAM) into our framework in two novel ways: as a post-processing refinement module that improves the accuracy of predicted masks using bounding box prompts derived from coarse outputs, and as a propagation mechanism via SAM 2 that generates volumetric segmentations from a single annotated 2D slice. Experimental evaluations on three public computed tomography (CT) datasets demonstrate that PolyCL outperforms fully-supervised and self-supervised baselines in both low-data and cross-domain scenarios. Our code is available at this https URL .

</details>

---

### 64. [BiomedSQL: Text-to-SQL for Scientific Reasoning on Biomedical Knowledge Bases](https://arxiv.org/abs/2505.20321)

**基本信息**

- 🔗 arXiv: [`2505.20321`](https://arxiv.org/abs/2505.20321)
- 👥 作者: Mathew J. Koretsky, Maya Willey, Owen Bianchi 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.20321.pdf)

**💡 相关性分析**

满足标准2：BiomedSQL基准提供了一个大规模、高质量的文本到SQL数据集，专门针对生物医学领域的复杂科学推理。该数据集和评估框架可直接用于训练和评估能够理解和查询结构化化学/生物医学数据库的LLMs（即化学领域大模型）。这对于构建能够进行知识检索、假设检验和科学发现的化学信息学AI助手至关重要，因此提供了宝贵的“数据资源”。

**📖 中文摘要**

本文介绍了BiomedSQL，这是第一个专门设计用于在真实世界生物医学知识库上评估文本到SQL生成中科学推理能力的基准。BiomedSQL包含68,000个问题/SQL查询/答案三元组，基于一个集成了基因-疾病关联、组学数据因果推断和药物批准记录的统一BigQuery知识库生成。每个问题都需要模型推断领域特定标准（例如全基因组显著性阈值、效应方向性或试验阶段过滤），而不是仅仅依赖句法翻译。作者评估了一系列开源和闭源LLM在不同提示策略和交互范式下的表现。结果表明，当前模型在支持通过结构化生物医学知识库进行稳健推理以促进科学发现方面存在显著性能差距。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biomedical researchers increasingly rely on large-scale structured databases for complex analytical tasks. However, current text-to-SQL systems often struggle to map qualitative scientific questions into executable SQL, particularly when implicit domain reasoning is required. We introduce BiomedSQL, the first benchmark explicitly designed to evaluate scientific reasoning in text-to-SQL generation over a real-world biomedical knowledge base. BiomedSQL comprises 68,000 question/SQL query/answer triples generated from templates and grounded in a harmonized BigQuery knowledge base that integrates gene-disease associations, causal inference from omics data, and drug approval records. Each question requires models to infer domain-specific criteria, such as genome-wide significance thresholds, effect directionality, or trial phase filtering, rather than rely on syntactic translation alone. We evaluate a range of open- and closed-source LLMs across prompting strategies and interaction paradigms. Our results reveal a substantial performance gap: Gemini-3-Pro achieves 58.1% execution accuracy, while our custom multi-step agent, BMSQL, reaches 62.6%, both well below the expert baseline of 90.0%. BiomedSQL provides a new foundation for advancing text-to-SQL systems capable of supporting scientific discovery through robust reasoning over structured biomedical knowledge bases. Our dataset is publicly available at this https URL , and our code is open-source at this https URL .

</details>

---

### 65. [An Introduction to Flow Matching and Diffusion Models](https://arxiv.org/abs/2506.02070)

**基本信息**

- 🔗 arXiv: [`2506.02070`](https://arxiv.org/abs/2506.02070)
- 👥 作者: Peter Holderrieth, Ezra Erives
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.02070.pdf)

**💡 相关性分析**

满足标准3：这是一篇关于扩散和流匹配模型的教程/综述论文。扩散模型是当前生成式AI的核心技术之一，在化学信息学中正被广泛应用于分子生成、逆合成规划、谱图生成等任务，是构建“化学大模型”的关键组成部分。该教程系统性地介绍了相关理论和实践，为化学领域的研究者理解和应用这些前沿生成技术提供了重要的学习资源，属于针对相关主题的重要综述和讨论。

**📖 中文摘要**

本教程对扩散和基于流的生成模型进行了自成体系的介绍。它从基本原理出发，系统性地介绍了常微分方程和随机微分方程的必要数学背景，并推导了流匹配和去噪扩散模型的核心算法。然后，提供了构建图像和视频生成器的分步指南，包括训练方法、引导和架构设计。本课程非常适合希望从原理上理解生成AI理论和实践的机器学习研究人员。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion and flow-based models have become the state of the art for generative AI across a wide range of data modalities, including images, videos, shapes, molecules, music, and more. This tutorial provides a self-contained introduction to diffusion and flow-based generative models from first principles. We systematically develop the necessary mathematical background in ordinary and stochastic differential equations and derive the core algorithms of flow matching and denoising diffusion models. We then provide a step-by-step guide to building image and video generators, including training methods, guidance, and architectural design. This course is ideal for machine learning researchers who want to develop a principled understanding of the theory and practice of generative AI.

</details>

---

### 66. [Mechanistic Interpretability of Diffusion Models: Circuit-Level Analysis and Causal Validation](https://arxiv.org/abs/2506.17237)

**基本信息**

- 🔗 arXiv: [`2506.17237`](https://arxiv.org/abs/2506.17237)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.17237.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对扩散模型进行可解释的、机制性的分析。扩散模型是当前最强大的生成模型之一，在化学领域正被用于分子、材料、谱图的生成。理解其内部工作机制（“化学大模型”如何工作）对于提高其可靠性、可控性以及在新化学空间中的泛化能力至关重要。因此，该工作直接关联到“化学大模型”的可解释性和可靠性这一核心主题。

**📖 中文摘要**

本文对扩散模型进行了定量的电路级分析，建立了支撑图像生成过程的计算路径和机制原理。通过对2000张合成图像和2000张CelebA人脸图像进行系统干预实验，发现了扩散架构在处理合成数据与自然数据分布时的基本算法差异。研究揭示了真实世界人脸处理需要具有可测量更高计算复杂度的电路，并在去噪时间步上表现出不同的注意力专业化模式。作者识别了八种功能不同的注意力机制，并展示了专门的干预分析，其中针对性消融会产生25.6%到128.3%的性能下降，为已识别的电路功能提供了因果证据。这些发现为通过机制干预策略算法化理解和控制生成模型行为奠定了定量基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a quantitative circuit-level analysis of diffusion models, establishing computational pathways and mechanistic principles underlying image generation processes. Through systematic intervention experiments across 2,000 synthetic and 2,000 CelebA facial images, we discover fundamental algorithmic differences in how diffusion architectures process synthetic versus naturalistic data distributions. Our investigation reveals that real-world face processing requires circuits with measurably higher computational complexity (complexity ratio = 1.084 plus/minus 0.008, p < 0.001), exhibiting distinct attention specialization patterns with entropy divergence ranging from 0.015 to 0.166 across denoising timesteps. We identify eight functionally distinct attention mechanisms showing specialized computational roles: edge detection (entropy = 3.18 plus/minus 0.12), texture analysis (entropy = 4.16 plus/minus 0.08), and semantic understanding (entropy = 2.67 plus/minus 0.15). Intervention analysis demonstrates critical computational bottlenecks where targeted ablations produce 25.6% to 128.3% performance degradation, providing causal evidence for identified circuit functions. These findings establish quantitative foundations for algorithmic understanding and control of generative model behavior through mechanistic intervention strategies.

</details>

---

### 67. [Fast weight programming and linear transformers: from machine learning to neurobiology](https://arxiv.org/abs/2508.08435)

**基本信息**

- 🔗 arXiv: [`2508.08435`](https://arxiv.org/abs/2508.08435)
- 👥 作者: Kazuki Irie, Samuel J. Gershman
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.08435.pdf)

**💡 相关性分析**

满足标准3：论文是一篇技术综述，深入讨论了包括Transformer在内的神经网络架构，这些架构是构建“化学大模型”的核心技术基础，为相关主题提供了重要的背景和展望讨论。

**📖 中文摘要**

这篇论文是一篇关于快速权重编程器（Fast Weight Programmers, FWPs）的入门综述。FWPs是一种使用二维矩阵形式隐藏状态的循环神经网络架构，其权重（称为快速权重）会随时间根据输入动态变化，充当短期记忆存储。论文回顾了FWPs的技术基础、计算特性，并讨论了它们与Transformer和状态空间模型的联系。虽然论文的核心是机器学习架构，但其对Transformer（作为现代大语言模型的核心组件）的深入讨论和连接分析，为理解“化学大模型”可能采用的基础架构（如Transformer变体）提供了重要的背景知识和理论视角。因此，这篇综述与构建和理解用于化学领域的“大模型”具有相关性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in artificial neural networks for machine learning, and language modeling in particular, have established a family of recurrent neural network (RNN) architectures that, unlike conventional RNNs with vector-form hidden states, use two-dimensional (2D) matrix-form hidden states. Such 2D-state RNNs, known as Fast Weight Programmers (FWPs), can be interpreted as a neural network whose synaptic weights (called fast weights) dynamically change over time as a function of input observations, and serve as short-term memory storage; corresponding synaptic weight modifications are controlled or programmed by another network (the programmer) whose parameters are trained (e.g., by gradient descent). In this Primer, we review the technical foundations of FWPs, their computational characteristics, and their connections to transformers and state space models. We also discuss connections between FWPs and models of synaptic plasticity in the brain, suggesting a convergence of natural and artificial intelligence.

</details>

---

### 68. [Functional Information Decomposition: A First-Principles Approach to Analyzing Functional Relationships](https://arxiv.org/abs/2509.18522)

**基本信息**

- 🔗 arXiv: [`2509.18522`](https://arxiv.org/abs/2509.18522)
- 👥 作者: Clifford Bohm, Vincent R. Ragusa, Arend Hintze 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.18522.pdf)

**💡 相关性分析**

满足标准2：论文提出的FID框架和开源实现是一种新的分析多变量依赖关系的工具和方法论。这种功能分解和推理工具可以应用于分析复杂的化学或质谱数据，以理解不同特征（如质谱峰）如何协同决定分子结构，从而间接支持“质谱结构推理”任务的方法论发展。

**📖 中文摘要**

本文提出了功能信息分解（Functional Information Decomposition, FID），这是一个用于分析复杂系统中多变量交互的计算和理论框架。FID的核心创新在于基于系统完整的输入-输出映射来定义信息组件，从而将系统的内在功能逻辑与有限的观测数据带来的统计伪影分离开来。当映射完全指定时，FID可以将信息唯一地分解为独立和协同的贡献。在部分观测的情况下，FID通过采样兼容的函数来刻画所有一致分解的空间，使推理的局限性变得明确。论文在包括康威生命游戏和基于基因表达的癌症药物反应预测等多个案例上展示了FID的跨学科实用性。该框架和开源实现为分析多变量依赖关系（例如在化学或生物分子数据中识别协同效应）提供了新的方法论工具，可用于开发更强大的推理模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A central challenge in analyzing multivariate interactions within complex systems is to decompose how multiple inputs jointly determine an output. Existing approaches generally operate on observed probability distributions and can conflate a system's intrinsic functional logic with statistical artifacts of limited data. As a result, distinct systems can yield identical observations, rendering information decomposition fundamentally underdetermined and obscuring true higher-order interactions. We introduce Functional Information Decomposition (FID), both a computational and theoretical framework, which defines informational components with respect to a system's complete input-output mapping, thereby addressing a core cross-scale inference problem: determining how information carried by individual components combines to shape system-level behavior. When the mapping is fully specified, FID provides a unique decomposition into independent and synergistic contributions. Crucially, given only partial observations, FID characterizes the entire space of consistent decompositions by sampling compatible functions, making inferential limits explicit. A complementary geometric perspective clarifies the structural origin of informational components. We demonstrate FID's interdisciplinary utility on canonical logical functions, Conway's Game of Life, and gene-expression-based prediction of cancer drug response, and provide an open-source implementation. By separating functional architecture from observational distribution, FID offers a principled foundation for analyzing multivariate dependence in both fully and partially observed complex systems.

</details>

---

### 69. [SHAP Meets Tensor Networks: Provably Tractable Explanations with Parallelism](https://arxiv.org/abs/2510.21599)

**基本信息**

- 🔗 arXiv: [`2510.21599`](https://arxiv.org/abs/2510.21599)
- 👥 作者: Reda Marzouk, Shahaf Bassan, Guy Katz
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.21599.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种为张量网络等复杂模型计算SHAP解释的新框架和算法。模型可解释性是开发和信任“化学大模型”及“质谱结构推理”模型的关键方面。该工作提供了一种潜在的工具，可用于分析和理解这些领域中所用模型的决策过程。

**📖 中文摘要**

本文研究了为张量网络（Tensor Networks, TNs）计算沙普利加性解释（SHAP）的问题。SHAP是解释黑盒模型预测的流行方法，但对于神经网络等复杂模型，其计算是NP难的。作者提出了一个通用框架，用于为具有任意结构的通用TN计算可证明精确的SHAP解释。特别地，当TN被限制为张量链（Tensor Train, TT）结构时，SHAP计算可以在多项式对数时间内使用并行计算完成。由于TT的表达能力，这一复杂度结果可以推广到许多其他流行的ML模型，如决策树、树集成、线性模型和线性RNN。此外，通过将二值化神经网络约简为张量网络表示，作者证明了当网络的“宽度”固定时，SHAP计算可以变得“高效可处理”。这项工作为复杂模型（可能包括用于化学或质谱分析的大模型）提供了一种新的、更高效的可解释性计算方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although Shapley additive explanations (SHAP) can be computed in polynomial time for simple models like decision trees, they unfortunately become NP-hard to compute for more expressive black-box models like neural networks - where generating explanations is often most critical. In this work, we analyze the problem of computing SHAP explanations for *Tensor Networks (TNs)*, a broader and more expressive class of models than those for which current exact SHAP algorithms are known to hold, and which is widely used for neural network abstraction and compression. First, we introduce a general framework for computing provably exact SHAP explanations for general TNs with arbitrary structures. Interestingly, we show that, when TNs are restricted to a *Tensor Train (TT)* structure, SHAP computation can be performed in *poly-logarithmic* time using *parallel* computation. Thanks to the expressiveness power of TTs, this complexity result can be generalized to many other popular ML models such as decision trees, tree ensembles, linear models, and linear RNNs, therefore tightening previously reported complexity results for these families of models. Finally, by leveraging reductions of binarized neural networks to Tensor Network representations, we demonstrate that SHAP computation can become *efficiently tractable* when the network's *width* is fixed, while it remains computationally hard even with constant *depth*. This highlights an important insight: for this class of models, width - rather than depth - emerges as the primary computational bottleneck in SHAP computation.

</details>

---

### 70. [Genomic Next-Token Predictors are In-Context Learners](https://arxiv.org/abs/2511.12797)

**基本信息**

- 🔗 arXiv: [`2511.12797`](https://arxiv.org/abs/2511.12797)
- 👥 作者: Nathan Breslow, Aayush Mishra, Mahler Revsine 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.12797.pdf)

**💡 相关性分析**

满足标准3：论文通过研究基因组序列模型，对“大模型”中上下文学习（ICL）这一核心能力的起源和普适性进行了重要的基础性讨论和展望。这对于理解如何构建和训练能够处理化学序列（如SMILES）或质谱数据模式的“化学大模型”具有重要的启发意义。

**📖 中文摘要**

本文研究了在基因组序列这一符号域中，通过大规模预测训练（下一个核苷酸预测）是否能够有机地产生上下文学习（ICL）能力。作者使用主要在下一个核苷酸预测上训练的Evo2基因组模型，开发了一个包含符号推理任务的实验框架，这些任务以语言和基因组形式实例化，从而能够直接比较基因组模型和语言模型的ICL能力。结果表明，基因组模型像它们的语言对应物一样，随着上下文演示数量的增加，在模式归纳上表现出对数线性增益。这是基因组序列中有机涌现ICL的第一个证据，支持了ICL作为对丰富数据进行大规模预测建模的结果而出现的假设。这一发现将涌现的元学习能力扩展到了语言之外，为理解大模型（包括可能用于化学序列或光谱数据的大模型）的上下文学习机制提供了新的视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In-context learning (ICL) -- the capacity of a model to infer and apply abstract patterns from examples provided within its input -- has been extensively studied in large language models trained for next-token prediction on human text. In fact, prior work often attributes this emergent behavior to distinctive statistical properties in human language. This raises a fundamental question: can ICL arise organically in other sequence domains purely through large-scale predictive training? To explore this, we turn to genomic sequences, an alternative symbolic domain rich in statistical structure. Specifically, we study the Evo2 genomic model, trained predominantly on next-nucleotide (A/T/C/G) prediction, at a scale comparable to mid-sized LLMs. We develop a controlled experimental framework comprising symbolic reasoning tasks instantiated in both linguistic and genomic forms, enabling direct comparison of ICL across genomic and linguistic models. Our results show that genomic models, like their linguistic counterparts, exhibit log-linear gains in pattern induction as the number of in-context demonstrations increases. To the best of our knowledge, this is the first evidence of organically emergent ICL in genomic sequences, supporting the hypothesis that ICL arises as a consequence of large-scale predictive modeling over rich data. These findings extend emergent meta-learning beyond language, pointing toward a unified, modality-agnostic view of in-context learning.

</details>

---

### 71. [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](https://arxiv.org/abs/2603.15080)

**基本信息**

- 🔗 arXiv: [`2603.15080`](https://arxiv.org/abs/2603.15080)
- 👥 作者: Madhulatha Mandarapu, Sandeep Kunkunuru
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15080.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了三个大规模、开放许可的生物医学知识图谱，并提供了可复现的ETL模式和联邦查询能力。这些数据集和资源可直接用于化学大模型（如用于药物发现、分子关系预测）的训练或增强，以及为质谱结构推理（如代谢物鉴定、通路分析）提供背景知识。

**📖 中文摘要**

这篇论文介绍了三个开源生物医学知识图谱（Pathways KG、Clinical Trials KG、Drug Interactions KG）的构建，这些图谱整合了来自Reactome、STRING、ClinicalTrials.gov、DrugBank等多个异构公共数据源的信息。论文的核心贡献在于描述了一个可重复的ETL模式，用于从异构数据源构建大规模知识图谱，并实现了跨知识图谱的联邦查询。此外，论文还引入了基于模式驱动的MCP服务器生成方法，以支持LLM智能体对知识图谱的访问。这项工作为化学信息学和质谱分析领域提供了重要的、可扩展的结构化数据资源，这些资源可用于训练化学大模型（例如用于药物发现或代谢通路分析）或作为质谱结构推理任务中分子实体关系查询的背景知识库。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, this http URL for study registries, DrugBank for drug vocabularies, DGIdb for drug-gene interactions, SIDER for side effects. We present three open-source biomedical knowledge graphs -- Pathways KG (118,686 nodes, 834,785 edges from 5 sources), Clinical Trials KG (7,774,446 nodes, 26,973,997 edges from 5 sources), and Drug Interactions KG (32,726 nodes, 191,970 edges from 3 sources) -- built on Samyama, a high-performance graph database written in Rust. Our contributions are threefold. First, we describe a reproducible ETL pattern for constructing large-scale KGs from heterogeneous public data sources, with cross-source deduplication, batch loading (Python Cypher and Rust native loaders), and portable snapshot export. Second, we demonstrate cross-KG federation: loading all three snapshots into a single graph tenant enables property-based joins across datasets. Third, we introduce schema-driven MCP server generation for LLM agent access, evaluated on a new BiomedQA benchmark (40 pharmacology questions): domain-specific MCP tools achieve 98% accuracy vs. 85% for schema-aware text-to-Cypher and 75% for standalone GPT-4o, with zero schema errors. All data sources are open-license. The combined federated graph (7.9M nodes, 28M edges) loads in approximately 3 minutes on commodity cloud hardware, with single-KG queries completing in 80-100ms and cross-KG federation joins in 1-4s

</details>

---

### 72. [CTG-DB: An Ontology-Based Transformation of ClinicalTrials.gov to Enable Cross-Trial Drug Safety Analyses](https://arxiv.org/abs/2603.15936)

**基本信息**

- 🔗 arXiv: [`2603.15936`](https://arxiv.org/abs/2603.15936)
- 👥 作者: Jeffery L. Painter, François Haguinet, Andrew Bate
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15936.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个将大型公共临床试验注册数据转化为标准化关系数据库的管道（CTG-DB）。这个经过处理和标准化的数据集是一个重要的数据资源，可用于训练或评估化学大模型（特别是在药物发现、药物安全性和药理学领域），也可为质谱分析中的代谢物鉴定提供临床背景信息。

**📖 中文摘要**

这篇论文提出了CTG-DB，一个将ClinicalTrials.gov (CT.gov) XML档案转化为关系数据库的开源管道。该管道的关键创新在于使用医学词典MedDRA对不良事件(AE)术语进行标准化，通过确定性的精确和模糊匹配实现透明且可复现的映射。这使得能够进行概念级别的检索和跨试验的聚合，从而支持可扩展的、以安慰剂为参照的安全性分析。虽然论文主要关注药物安全性的药理学监督，但其核心贡献——一个将非结构化或半结构化临床文本数据转化为标准化、可查询的关系型知识库的框架——与化学信息学高度相关。该资源和方法可用于构建或增强用于药物发现、副作用预测或药物-靶点相互作用的化学大模型所需的训练数据。同时，标准化的药物和不良事件数据也可作为质谱结构推理中鉴定药物代谢物或相关生物标志物的辅助信息源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

ClinicalTrials .gov (CT .gov) is the largest publicly accessible registry of clinical studies, yet its registry-oriented architecture and heterogeneous adverse event (AE) terminology limit systematic pharmacovigilance (PV) analytics. AEs are typically recorded as investigator-reported text rather than standardized identifiers, requiring manual reconciliation to identify coherent safety concepts. We present the ClinicalTrials .gov Transformation Database (CTG-DB), an open-source pipeline that ingests the complete CT .gov XML archive and produces a relational database aligned to standardized AE terminology using the Medical Dictionary for Regulatory Activities (MedDRA). CTG-DB preserves arm-level denominators, represents placebo and comparator arms, and normalizes AE terminology using deterministic exact and fuzzy matching to ensure transparent and reproducible mappings. This framework enables concept-level retrieval and cross-trial aggregation for scalable placebo-referenced safety analyses and integration of clinical trial evidence into downstream PV signal detection.

</details>

---

### 73. [Reduced Density Matrices Through Machine Learning](https://arxiv.org/abs/2511.07367)

**基本信息**

- 🔗 arXiv: [`2511.07367`](https://arxiv.org/abs/2511.07367)
- 👥 作者: Awwab A. Azam, Lexu Zhao, Jiabin Yu
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.07367.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用神经网络近似量子多体系统中的约化密度矩阵。这直接与“化学大模型”主题相关，因为开发用于量子化学计算的高效、准确的机器学习模型是该领域的核心目标之一。论文的方法为构建能够处理强关联电子系统的化学AI模型提供了新的思路和技术。

**📖 中文摘要**

这篇论文利用神经网络架构来加速甚至预测大系统强关联态的n粒子约化密度矩阵。其核心直觉是，对于有能隙的态，n-RDM在布里渊区通常是平滑且可插值的函数，这使得在小尺寸系统上训练的神经网络能够预测大尺寸系统的RDM。论文测试了两种神经网络：一种是将随机RDM映射到物理RDM的自注意力网络；另一种是直接将动量空间坐标映射到RDM值的正弦表示网络。在化学和计算材料科学中，精确计算分子或材料的电子结构（通过波函数或密度矩阵）是核心挑战。这项工作展示了使用神经网络高效近似关键量子化学对象（RDM）的潜力，这直接有助于开发更高效的电子结构计算方法，这是构建下一代“化学大模型”（用于量子化学计算）的基础。同时，对电子结构的精确推理也与从光谱数据（如质谱、光谱）推断分子结构的“质谱结构推理”有间接但深层的联系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

$n$-particle reduced density matrices ($n$-RDMs) play a central role in understanding correlated phases of matter, but their calculation is often computationally inefficient for strongly-correlated states at large system sizes. In this work, we use neural network (NN) architectures to accelerate and even predict $n$-RDMs for large systems. Our underlying intuition is that, for gapped states, $n$-RDMs are often smooth functions over the Brillouin zone (BZ) and are therefore interpolable, allowing NNs trained on small-size systems to predict large-size ones. Building on this, we devise two NNs: (i) a self-attention NN that maps random RDMs to physical ones, and (ii) a Sinusoidal Representation Network (SIREN) that directly maps momentum-space coordinates to RDM values. We test the NNs on RDMs in three 2D models: the pair-pair correlation functions of the Richardson model of superconductivity, the translationally-invariant Hartree-Fock (HF) 1-RDM in a four-band repulsive model, and the translation-breaking HF 1-RDM in the half-filled Hubbard model. We find that a SIREN trained on a $6\times 6$ momentum mesh and a SIREN trained on $4$ tilted meshes (each of which has $12$ momentum points) can predict the $18\times 18$ pair-pair correlation function with a relative accuracy of $94.29\%$ and $93.77\%$, respectively. NNs trained on $6\times 6$ and $8\times 8$ meshes provide high-quality initial guesses for $50\times 50$ translation-invariant HF and $30\times 30$ fully translation-breaking-allowed HF, reducing the required number of iterations by up to $91.63\%$ and $92.78\%$, respectively, compared to random initializations. Our results illustrate the potential of NN-based methods for interpolable $n$-RDMs, which might open a new avenue for future research on strongly correlated phases.

</details>

---

### 74. [Generative Adversarial Networks for Resource State Generation](https://arxiv.org/abs/2601.13708)

**基本信息**

- 🔗 arXiv: [`2601.13708`](https://arxiv.org/abs/2601.13708)
- 👥 作者: Shahbaz Shaik, Sourav Chatterjee, Sayantan Pramanik 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.13708.pdf)

**💡 相关性分析**

满足标准1：论文提出了一个基于物理信息生成对抗网络的逆向设计框架，用于生成满足特定任务需求的量子态。这种方法论与化学信息学中“化学大模型”的核心应用之一——分子逆向设计（即生成具有目标性质的分子）——在概念和技术路径上高度相关，为后者提供了可借鉴的模型框架和训练范式。

**📖 中文摘要**

这篇论文引入了一个物理信息生成对抗网络框架，将量子资源态生成重新表述为一个逆向设计任务。通过将任务特定的效用函数嵌入训练中，模型学习生成针对量子隐形传态和纠缠广播优化的有效两量子比特态。该框架再现了类Werner态和贝尔对角态的理论资源边界，保真度超过~98%，确立了对抗学习作为一种轻量级但有效的约束驱动量子态发现方法。在化学信息学背景下，“逆向设计”是一个核心概念，例如设计具有特定性质的分子或材料。本文虽然聚焦于量子信息中的资源态，但其方法论——使用嵌入物理约束的生成模型进行目标驱动的结构生成——与化学中“生成化学”或“分子逆向设计”的理念高度相似。因此，该框架为“化学大模型”领域，特别是用于分子生成的生成模型，提供了方法论上的参考和跨领域启示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a physics-informed Generative Adversarial Network framework that recasts quantum resource-state generation as an inverse-design task. By embedding task-specific utility functions into training, the model learns to generate valid two-qubit states optimized for teleportation and entanglement broadcasting. Comparing decomposition-based and direct-generation architectures reveals that structural enforcement of Hermiticity, trace-one, and positivity yields higher fidelity and training stability than loss-only approaches. The framework reproduces theoretical resource boundaries for Werner-like and Bell-diagonal states with fidelities exceeding ~98%, establishing adversarial learning as a lightweight yet effective method for constraint-driven quantum-state discovery. This approach provides a scalable foundation for automated design of tailored quantum resources for information-processing applications, exemplified with teleportation and broadcasting of entanglement, and it opens up the possibility of using such states in efficient quantum network design.

</details>

---

### 75. [Solving physics-constrained inverse problems with conditional flow matching](https://arxiv.org/abs/2603.14135)

**基本信息**

- 🔗 arXiv: [`2603.14135`](https://arxiv.org/abs/2603.14135)
- 👥 作者: Agnimitra Dasgupta, Ali Fardisi, Mehrnegar Aminy 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14135.pdf)

**💡 相关性分析**

满足标准1：论文提出的条件流匹配框架是解决物理约束逆问题的通用方法。这直接适用于“质谱结构推理”（从质谱数据逆推分子结构）和“化学大模型”（学习分子表示以解决性质预测等逆问题）这两个核心主题，为这些领域中的概率建模和不确定性量化提供了新的工具。

**📖 中文摘要**

本研究提出了一个条件流匹配框架，用于解决物理约束的贝叶斯逆问题。该框架能够从推断变量和测量的联合分布中采样，而不需要显式评估先验和似然密度。在条件设置下，神经网络被训练来学习概率流常微分方程的向量场，该向量场将样本从选定的源分布直接传输到以观测测量为条件的后验分布。这种黑盒公式适应非线性、高维且可能不可微的前向模型。在化学信息学和质谱分析中，许多核心问题都属于逆问题范畴，例如：从光谱数据推断分子结构（质谱结构推理）、根据物理化学性质预测分子特性（化学大模型的应用）、或从部分观测中重建反应网络。本论文提出的通用框架为这些逆问题的求解提供了一种先进的、基于生成模型的概率推理方法，特别是当正向模型复杂或显式似然难以获得时。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study presents a conditional flow matching framework for solving physics-constrained Bayesian inverse problems. In this setting, samples from the joint distribution of inferred variables and measurements are assumed available, while explicit evaluation of the prior and likelihood densities is not required. We derive a simple and self-contained formulation of both the unconditional and conditional flow matching algorithms, tailored specifically to inverse problems. In the conditional setting, a neural network is trained to learn the velocity field of a probability flow ordinary differential equation that transports samples from a chosen source distribution directly to the posterior distribution conditioned on observed measurements. This black-box formulation accommodates nonlinear, high-dimensional, and potentially non-differentiable forward models without restrictive assumptions on the noise model. We further analyze the behavior of the learned velocity field in the regime of finite training data. Under mild architectural assumptions, we show that overtraining can induce degenerate behavior in the generated conditional distributions, including variance collapse and a phenomenon termed selective memorization, wherein generated samples concentrate around training data points associated with similar observations. A simplified theoretical analysis explains this behavior, and numerical experiments confirm it in practice. We demonstrate that standard early-stopping criteria based on monitoring test loss effectively mitigate such degeneracy. The proposed method is evaluated on several physics-based inverse problems. We investigate the impact of different choices of source distributions, including Gaussian and data-informed priors. Across these examples, conditional flow matching accurately captures complex, multimodal posterior distributions while maintaining computational efficiency.

</details>

---

### 76. [AR-Flow VAE: A Structured Autoregressive Flow Prior Variational Autoencoder for Unsupervised Blind Source Separation](https://arxiv.org/abs/2603.14441)

**基本信息**

- 🔗 arXiv: [`2603.14441`](https://arxiv.org/abs/2603.14441)
- 👥 作者: Yuan-Hao Wei, Fu-Hao Deng, Lin-Yong Cui 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14441.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（盲源分离）与“质谱结构推理”主题直接相关。论文提出的AR-Flow VAE框架，利用自回归流先验对复杂源信号进行建模，为从混合观测信号（如质谱数据）中推理出潜在源结构（如纯化合物谱图）提供了一种先进的机器学习方法。

**📖 中文摘要**

这篇论文提出了AR-Flow VAE，一种用于无监督盲源分离（BSS）的新型变分自编码器框架。该框架的核心创新是为每个潜在源信号配备了一个参数自适应的自回归流先验。这种先验显著增强了潜在源建模的灵活性，能够捕捉复杂的非高斯行为和结构化依赖（如时间相关性）。在化学信息学和质谱分析的背景下，盲源分离是处理复杂混合物质谱数据（如LC-MS或GC-MS）的关键技术，旨在从观测到的混合谱中解析出单个纯组分（化合物）的谱图。AR-Flow VAE所展示的、利用灵活先验对复杂潜在源进行建模的能力，直接适用于“质谱结构推理”这一核心主题。该框架为从混合质谱数据中推断单个化合物的质谱特征提供了一种先进的、基于深度生成模型的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Blind source separation (BSS) seeks to recover latent source signals from observed mixtures. Variational autoencoders (VAEs) offer a natural perspective for this problem: the latent variables can be interpreted as source components, the encoder can be viewed as a demixing mapping from observations to sources, and the decoder can be regarded as a remixing process from inferred sources back to observations. In this work, we propose AR-Flow VAE, a novel VAE-based framework for BSS in which each latent source is endowed with a parameter-adaptive autoregressive flow prior. This prior significantly enhances the flexibility of latent source modeling, enabling the framework to capture complex non-Gaussian behaviors and structured dependencies, such as temporal correlations, that are difficult to represent with conventional priors. In addition, the structured prior design assigns distinct priors to different latent dimensions, thereby encouraging the latent components to separate into different source signals under heterogeneous prior constraints. Experimental results validate the effectiveness of the proposed architecture for blind source separation. More importantly, this work provides a foundation for future investigations into the identifiability and interpretability of AR-Flow VAE.

</details>

---

### 77. [Distance Backbones Optimize Spreading Dynamics and Centrality Ranks in the Sparsification of Complex Networks](https://arxiv.org/abs/2603.14564)

**基本信息**

- 🔗 arXiv: [`2603.14564`](https://arxiv.org/abs/2603.14564)
- 👥 作者: Bernardo Pereira, Felipe Xavier Costa, Luís M. Rocha
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14564.pdf)

**💡 相关性分析**

满足标准1和2：论文提出的距离骨干和图稀疏化方法（DBS）与化学信息学中分子图表示的学习和处理直接相关。该方法可以作为一种数据预处理或特征工程工具，用于优化分子图数据的表示，从而可能提升化学大模型的训练效率和性能。因此，它既提供了潜在的工具（标准2），其研究内容也与基于图的化学模型核心主题相关（标准1）。

**📖 中文摘要**

这篇论文研究了加权图的距离骨干（Distance Backbones）在图稀疏化中的应用。距离骨干通过移除违反广义三角不等式的边来保留加权图的所有最短路径。论文表明，与最先进的替代方法相比，距离骨干通常能更有效地稀疏化图，并更好地保留社区结构、节点中心性排名以及传播动力学。论文引入了距离骨干合成（DBS）方法，根据一个通用的嵌套距离骨干族逐步稀疏化加权图。在化学信息学中，分子通常被表示为图（原子为节点，化学键为边），而分子性质预测、反应预测等任务常常依赖于图神经网络等模型。对大型分子图数据库进行有效的稀疏化，可以在保持关键化学结构信息（如分子骨架、官能团连接）的同时，降低计算和存储成本，这对于构建和部署高效的化学大模型具有重要意义。此外，传播动力学的保持也与分子内能量或信息传递的模拟有关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Detailed network models of social, biological and other complex systems are often dense, which increases their computational complexity in simulations and analysis. To address this challenge, graph sparsification is used to remove edges while preserving desired network properties. Distance backbones of weighted graphs, which remove edges that break a generalized triangle inequality for any given path-length measure, preserve all shortest paths of weighted graphs. They have been shown to typically sparsify graphs more, as well as preserve community structure and spreading dynamics better than alternative state-of-the-art methods. Here, We show that they significantly best preserve node centrality ranks, as well as local and global dynamics in spreading phenomena. This is done by introducing the distance backbone synthesis (DBS) to progressively sparsify weighted graphs according to a general family of nested distance backbones, whereby each edge is associated with the smallest distance backbone in which it appears. DBS provides a principled and natural method to sweep all degrees of sparsification possible while preserving connectivity, allowing us to precisely study (directed and undirected) weighted graph sparsification under multi-objective criteria. It provides an algebraically-principled explanation of edge importance by revealing the precise topological space associated with each edge. The theory is demonstrated with a battery of social contact networks obtained from real-world social activity in different scenarios. Our study also shows that the optimal preservation of node centrality and spreading dynamics happens for the distance backbone obeying the generalized triangle inequality for the path-length measure $g(x, y) = (\sqrt[3]{x}+\sqrt[3]{y})^3$, which removes more than half of the edges from the empirical networks studied.

</details>

---

## 📊 数据统计
- 累计运行天数：40
- 累计论文数量：2881

## 📝 历史记录

> 暂无历史数据

