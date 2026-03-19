# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-19 12:49:53

## 📅 2026-03-19 (今日最新)

**相关论文数：72**

### 1. [A foundation model for electrodermal activity data](https://arxiv.org/abs/2603.16878)

**基本信息**

- 🔗 arXiv: [`2603.16878`](https://arxiv.org/abs/2603.16878)
- 👥 作者: Leonardo Alchieri, Matteo Garzon, Lidia Alecci 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16878.pdf)

**💡 相关性分析**

满足标准2：论文提供了大规模、开放的数据集（EDAMAME）和专门的基础模型（UME），这些资源可用于化学信息学领域，特别是与生理信号（如对化学刺激的反应）相关的建模和分析。

**📖 中文摘要**

本文提出了一个用于皮肤电活动（EDA）数据的基础模型UME。该研究首先构建了EDAMAME数据集，这是一个从24个公开数据集中整理的大规模、开放的EDA信号数据集，包含超过25,000小时的数据。在此基础上，他们训练了UME，这是第一个专门针对EDA的基础模型。该模型在多项任务中超越了基线模型，并与通用的时间序列基础模型性能相当，同时计算资源消耗减少了20倍。这项工作为生理信号领域提供了重要的数据资源（EDAMAME数据集）和模型工具（UME），可用于构建更复杂的化学信息学或生物医学分析模型，例如通过生理信号推断化学物质暴露或反应。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Foundation models have recently extended beyond natural language and vision to timeseries domains, including physiological signals. However, progress in electrodermal activity (EDA) modeling is hindered by the absence of large-scale, curated, and openly accessible datasets. EDA reflects sympathetic nervous system activity and is widely used to infer cognitive load, stress, and engagement. Yet very few wearable devices provide continuous, unobtrusive sensing, and the only large-scale archive to date is proprietary. To address this gap, we compile EDAMAME, a collection of EDA traces from 24 public datasets, comprising more than 25,000 hours from 634 users. Using this resource, we train UME, the first dedicated foundation model for EDA. In eight out of ten scenarios, UME outperforms baselines and matches generalist timeseries foundation models while using 20x fewer computational resources. Our findings, however, also highlight the intrinsic challenges of EDA modeling, motivating further research to unlock its full potential. All datasets, model weights, and code are released to support further research.

</details>

---

### 2. [From Language to Action in Arabic: Reliable Structured Tool Calling via Data-Centric Fine-Tuning](https://arxiv.org/abs/2603.16901)

**基本信息**

- 🔗 arXiv: [`2603.16901`](https://arxiv.org/abs/2603.16901)
- 👥 作者: Omer Nacar, Deema Alquffari, Saleh Alsharideh 等25人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16901.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发可靠的结构化工具调用（函数调用）语言模型，这是构建能够执行“质谱结构推理”或“化学大模型”交互任务的智能代理系统的关键技术基础。

**📖 中文摘要**

本文提出了AISA-AR-FunctionCall框架，旨在解决大型语言模型在阿拉伯语环境下进行结构化工具调用（函数调用）时的稳定性问题。该框架基于一个270M参数的FunctionGemma骨干模型，通过系统性的数据集审计、模式修复、工具感知的提示重构和全参数监督微调进行训练。实验表明，微调将解析失败率从87%降低到1%以下，并显著提高了函数名和参数的准确性。这项工作专注于将自然语言可靠地转换为可执行的结构化动作，这是构建化学信息学或质谱分析领域智能代理（如用于结构推理或数据库查询的代理）的核心技术之一。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Function-calling language models are essential for agentic AI systems that translate natural language into executable structured actions, yet existing models exhibit severe structural instability when applied to Arabic. We present AISA-AR-FunctionCall, a production-oriented Arabic function-calling framework built on a 270M-parameter FunctionGemma backbone and trained through systematic dataset auditing, schema repair, tool-aware prompt restructuring, and full-parameter supervised fine-tuning. On a held-out test set, fine-tuning reduces parse failures from 87\% to below 1\%, improves function name accuracy by more than eightfold, and substantially enhances argument alignment across dialects and domains. Error analysis reveals a transition from structural collapse to semantic misalignment, suggesting that serialization stability and decision-level reasoning are separable challenges. We further explore a reasoning-augmented LoRA variant that introduces explicit intermediate reasoning prior to tool invocation. All datasets and models are publicly released under the AISA framework.

</details>

---

### 3. [HoloByte: Continuous Hyperspherical Distillation for Tokenizer-Free Modeling](https://arxiv.org/abs/2603.16917)

**基本信息**

- 🔗 arXiv: [`2603.16917`](https://arxiv.org/abs/2603.16917)
- 👥 作者: Vladimer Khasia
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16917.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的、无需分词的序列建模基础架构（HoloByte）。这种处理原始字节序列的通用方法可以直接应用于化学信息学中的序列表示（如SMILES、质谱峰值序列），是构建“化学大模型”底层技术的一种有前景的探索。

**📖 中文摘要**

本文提出了HoloByte，一个完全无需分词器的序列建模框架。它采用连续超球面蒸馏技术，将离散的字节序列分块并投影到一个连续、有界的超球面流形上。这种方法避免了传统子词分词强加的人工形态边界和词汇表依赖，保持了优化景观的连续性。理论上，该方法将精确注意力时间复杂度从O(N^2D)降低到O(N^2/W^2 * D + ND^2)。在参数严格匹配的条件下，HoloByte系统地超越了基于字节对编码的基线模型。这项工作为词汇表无关的序列建模提供了数学上严谨且计算上可行的新范式，对于处理化学SMILES字符串、质谱序列等非自然语言序列的“化学大模型”具有潜在的重要价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Sequence modeling universally relies on discrete subword tokenization to circumvent the $\mathcal{O}(N^2)$ computational intractability of native byte-level attention. However, this heuristic quantization imposes artificial morphological boundaries, enforces vocabulary dependence, and fractures the continuity of the optimization landscape. To resolve this dichotomy, we introduce \textbf{HoloByte}: a strictly tokenizer-free framework utilizing Continuous Hyperspherical Distillation. HoloByte partitions discrete byte sequences into fixed-capacity chunks and projects them into a continuous, strictly bounded hyperspherical manifold via an invertible, dimension-preserving orthogonal rotation operator. This spatial superposition allows a macroscopic transformer to operate exclusively on compressed continuous representations, formally reducing the exact attention time complexity from $\mathcal{O}(N^2D)$ to $\mathcal{O}\left( \frac{N^2}{W^2}D + ND^2 \right)$. A localized causal micro-decoder subsequently unbinds these representations to compute exact byte-level distributions. To govern this continuous trajectory, we propose a dual-objective formulation incorporating a mathematically precise Holographic Latent Mean Squared Error, which strictly bounds the gradient and guarantees asymptotic stability. Theoretically, we derive the minimal embedding dimension $D = \Omega(W \ln |\mathcal{V}|)$ required to ensure error-free discrete recovery from the continuous manifold. Empirically, under strictly matched parameter constraints, HoloByte is systematically outperforming a comparable discrete Byte-Pair Encoding (BPE) baseline. These results establish Continuous Hyperspherical Distillation as a mathematically rigorous and computationally tractable foundation for vocabulary-invariant sequence modeling. The code is available at this https URL

</details>

---

### 4. [Minimum-Action Learning: Energy-Constrained Symbolic Model Selection for Physical Law Identification from Noisy Data](https://arxiv.org/abs/2603.16951)

**基本信息**

- 🔗 arXiv: [`2603.16951`](https://arxiv.org/abs/2603.16951)
- 👥 作者: Martin G. Frasch
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16951.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从数据中识别符号形式的物理定律，这是一种结合了机器学习与符号推理的方法。这与“化学大模型”和“质谱结构推理”中追求可解释、物理约束的模型的目标直接相关，为从化学或质谱数据中发现规律提供了方法论参考。

**📖 中文摘要**

本文提出了最小动作学习（MAL）框架，用于从噪声观测数据中识别物理定律（符号力定律）。MAL通过最小化一个结合了轨迹重建、架构稀疏性和能量守恒执行的三重动作泛函，从一个预定义的基函数库中选择符号力定律。该方法采用了一种宽间隔加速度匹配技术，将噪声方差降低了10,000倍，从而将一个难以处理的问题转化为可学习的问题。在开普勒引力和胡克定律两个基准测试中，MAL成功恢复了正确的力定律。该工作展示了如何将符号回归、神经网络与物理先验（如能量守恒）相结合，从数据中推导出可解释的模型。这种方法论与“化学大模型”中追求可解释性和物理一致性的目标高度相关，也可用于从质谱数据中推导碎片化规律。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Identifying physical laws from noisy observational data is a central challenge in scientific machine learning. We present Minimum-Action Learning (MAL), a framework that selects symbolic force laws from a pre-specified basis library by minimizing a Triple-Action functional combining trajectory reconstruction, architectural sparsity, and energy-conservation enforcement. A wide-stencil acceleration-matching technique reduces noise variance by 10,000x, transforming an intractable problem (SNR ~0.02) into a learnable one (SNR ~1.6); this preprocessing is the critical enabler shared by all methods tested, including SINDy variants. On two benchmarks -- Kepler gravity and Hooke's law -- MAL recovers the correct force law with Kepler exponent p = 3.01 +/- 0.01 at ~0.07 kWh (40% reduction vs. prediction-error-only baselines). The raw correct-basis rate is 40% for Kepler and 90% for Hooke; an energy-conservation-based criterion discriminates the true force law in all cases, yielding 100% pipeline-level identification. Basis library sensitivity experiments show that near-confounders degrade selection (20% with added r^{-2.5} and r^{-1.5}), while distant additions are harmless, and the conservation diagnostic remains informative even when the correct basis is absent. Direct comparison with noise-robust SINDy variants, Hamiltonian Neural Networks, and Lagrangian Neural Networks confirms MAL's distinct niche: interpretable, energy-constrained model selection that combines symbolic basis identification with dynamical rollout validation.

</details>

---

### 5. [Implementation of tangent linear and adjoint models for neural networks based on a compiler library tool](https://arxiv.org/abs/2603.16976)

**基本信息**

- 🔗 arXiv: [`2603.16976`](https://arxiv.org/abs/2603.16976)
- 👥 作者: Sa Xiao, Hao Jing, Honglu Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16976.pdf)

**💡 相关性分析**

满足标准2：论文提供了一个实用的工具（TorchNWP），用于将深度学习模型（如潜在的化学大模型）集成到传统的科学计算框架中，并支持构建其切线性/伴随模型。这为化学信息学和质谱分析领域的研究者部署和优化复杂模型提供了重要的技术资源和工具。

**📖 中文摘要**

本文提出了TorchNWP，一个用于高效耦合人工智能组件（基于PyTorch的深度学习模型）与传统数值模型（通常用Fortran编写）的编译库工具。它解决了操作级数值模型与Python深度学习框架之间跨语言兼容性差、耦合灵活性不足和数据传输效率低的问题。该工具将PyTorch框架下的深度学习模型转换为静态二进制格式，并提供C/C++接口，使得模型可以部署在数值模型中。在此基础上，论文还在C/C++层面实现了基于神经网络的切线性模型和伴随模型，这可以简化四维变分同化系统的构建过程。该工具已应用于耦合基于深度学习的物理参数化方案（如辐射、非地形重力波拖曳）及其切线性/伴随模型的开发。这项工作为将复杂的“化学大模型”或质谱预测模型集成到大型科学计算软件栈中提供了重要的工程解决方案和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents TorchNWP, a compilation library tool for the efficient coupling of artificial intelligence components and traditional numerical models. It aims to address the issues of poor cross-language compatibility, insufficient coupling flexibility, and low data transfer efficiency between operational numerical models developed in Fortran and Python-based deep learning frameworks. Based on LibTorch, it optimizes and designs a unified application-layer calling interface, converts deep learning models under the PyTorch framework into a static binary format, and provides C/C++ interfaces. Then, using hybrid Fortran/C/C++ programming, it enables the deployment of deep learning models within numerical models. Integrating TorchNWP into a numerical model only requires compiling it into a callable link library and linking it during the compilation and linking phase to generate the executable. On this basis, tangent linear and adjoint model based on neural networks are implemented at the C/C++ level, which can shield the internal structure of neural network models and simplify the construction process of four-dimensional variational data assimilation systems. Meanwhile, it supports deployment on heterogeneous platforms, is compatible with mainstream neural network models, and enables mapping of different parallel granularities and efficient parallel execution. Using this tool requires minimal code modifications to the original numerical model, thus reducing coupling costs. It can be efficiently integrated into numerical weather prediction models such as CMA-GFS and MCV, and has been applied to the coupling of deep learning-based physical parameterization schemes (e.g., radiation, non-orographic gravity wave drag) and the development of their tangent linear and adjoint models, significantly improving the accuracy and efficiency of numerical weather prediction.

</details>

---

### 6. [Formal verification of tree-based machine learning models for lateral spreading](https://arxiv.org/abs/2603.16983)

**基本信息**

- 🔗 arXiv: [`2603.16983`](https://arxiv.org/abs/2603.16983)
- 👥 作者: Krishna Kumar
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16983.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是机器学习模型的形式化验证，以确保其输出符合预定义的物理/逻辑规范。这直接关系到如何构建可靠、可信的“化学大模型”和“质谱结构推理”系统，确保它们的预测符合化学规则和安全性约束，属于核心方法论的相关扩展。

**📖 中文摘要**

本文提出了一种用于岩土灾害预测的树集成机器学习模型的形式化验证方法。该方法将训练好的树集成模型（XGBoost和可解释提升机EBM）编码为可满足性模理论（SMT）求解器中的逻辑公式，并在整个输入域（而不仅仅是采样点）上检查物理规范。论文形式化了四个岩土工程规范（地下水位深度、PGA单调性、距离安全性和平坦地面安全性）为可判定的逻辑公式，并通过SMT对模型进行验证。SMT求解器要么产生规范失败的具体反例，要么证明不存在违规。这项工作建立了一个“验证-修复-验证”的工程循环，为在安全关键的岩土工程应用中部署物理一致的ML模型提供了形式化认证。这种方法论对于确保“化学大模型”或“质谱结构推理”模型在安全关键场景（如毒性预测、药物发现）中的可靠性和符合化学物理规则具有重要的借鉴意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Machine learning models for geotechnical hazard prediction can achieve high accuracy while learning physically inconsistent relationships from sparse or biased training data. Current remedies (post-hoc explainability, such as SHAP and LIME, and training-time constraints) either diagnose individual predictions approximately or restrict model capacity without providing exhaustive guarantees. This paper encodes trained tree ensembles as logical formulas in a Satisfiability Modulo Theories (SMT) solver and checks physical specifications across the entire input domain, not just sampled points. Four geotechnical specifications (water table depth, PGA monotonicity, distance safety, and flat-ground safety) are formalized as decidable logical formulas and verified via SMT against both XGBoost ensembles and Explainable Boosting Machines (EBMs) trained on the 2011 Christchurch earthquake lateral spreading dataset (7,291 sites, four features). The SMT solver either produces a concrete counterexample where a specification fails or proves that no violation exists. The unconstrained EBM (80.1% accuracy) violates all four specifications. A fully constrained EBM (67.2%) satisfies three of four specifications, demonstrating that iterative constraint application guided by verification can progressively improve physical consistency. A Pareto analysis of 33 model variants reveals a persistent trade-off, as none of the variants studied achieve both greater than 80% accuracy and full compliance with the specified set. SHAP analysis of specification counterexamples shows that the offending feature can rank last, demonstrating that post-hoc explanations do not substitute for formal verification. These results establish a verify-fix-verify engineering loop and a formal certification for deploying physically consistent ML models in safety-critical geotechnical applications.

</details>

---

### 7. [OpenQlaw: An Agentic AI Assistant for Analysis of 2D Quantum Materials](https://arxiv.org/abs/2603.17043)

**基本信息**

- 🔗 arXiv: [`2603.17043`](https://arxiv.org/abs/2603.17043)
- 👥 作者: Sankalp Pandey, Xuan-Bac Nguyen, Hoang-Quan Nguyen 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17043.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个用于材料科学分析的智能代理系统（OpenQlaw）。该系统整合了LLM代理和领域专家模型，其架构和方法可直接类比并应用于“化学大模型”和“质谱结构推理”领域，用于创建能够理解、推理和操作化学数据的智能助手。

**📖 中文摘要**

本文介绍了OpenQlaw，一个用于分析二维量子材料的智能代理编排系统。该系统基于轻量级代理框架NanoBot和物理感知的多模态平台QuPAINT构建。OpenQlaw允许核心大型语言模型（LLM）代理将领域专家多模态大模型（QuPAINT）作为一个专门节点进行编排，成功地将视觉识别与推理和确定性图像渲染解耦。通过解析来自专家的空间数据，代理可以动态处理用户查询（例如执行尺度感知的物理计算或生成孤立的视觉注释），并以自然的方式回答。该系统具有持久记忆功能，可以保存物理尺度比例和样品制备方法。这种将代理架构与领域特定专家相结合的应用，将孤立的推理转变为上下文感知的助手，能够加速高通量器件制造。这项工作展示了智能代理在材料科学领域的应用，其架构思想可迁移至化学信息学，用于构建分析化学数据（如质谱图像、分子结构）的智能助手。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The transition from optical identification of 2D quantum materials to practical device fabrication requires dynamic reasoning beyond the detection accuracy. While recent domain-specific Multimodal Large Language Models (MLLMs) successfully ground visual features using physics-informed reasoning, their outputs are optimized for step-by-step cognitive transparency. This yields verbose candidate enumerations followed by dense reasoning that, while accurate, may induce cognitive overload and lack immediate utility for real-world interaction with researchers. To address this challenge, we introduce OpenQlaw, an agentic orchestration system for analyzing 2D materials. The architecture is built upon NanoBot, a lightweight agentic framework inspired by OpenClaw, and QuPAINT, one of the first Physics-Aware Instruction Multi-modal platforms for Quantum Material Discovery. This allows accessibility to the lab floor via a variety of messaging channels. OpenQlaw allows the core Large Language Model (LLM) agent to orchestrate a domain-expert MLLM,with QuPAINT, as a specialized node, successfully decoupling visual identification from reasoning and deterministic image rendering. By parsing spatial data from the expert, the agent can dynamically process user queries, such as performing scale-aware physical computation or generating isolated visual annotations, and answer in a naturalistic manner. Crucially, the system features a persistent memory that enables the agent to save physical scale ratios (e.g., 1 pixel = 0.25 {\mu}m) for area computations and store sample preparation methods for efficacy comparison. The application of an agentic architecture, together with the extension that uses the core agent as an orchestrator for domain-specific experts, transforms isolated inferences into a context-aware assistant capable of accelerating high-throughput device fabrication.

</details>

---

### 8. [Transformers are Bayesian Networks](https://arxiv.org/abs/2603.17063)

**基本信息**

- 🔗 arXiv: [`2603.17063`](https://arxiv.org/abs/2603.17063)
- 👥 作者: Gregory Coppola
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17063.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是从贝叶斯网络和概率图模型的角度，对Transformer这一构建“化学大模型”的核心架构提供了深刻的理论解释。这有助于理解模型如何进行不确定性推理和知识整合，直接关系到如何设计更好的化学信息学模型。

**📖 中文摘要**

本文从贝叶斯网络的角度对Transformer架构提供了全新的理论解释。论文通过五种方式证明：带有Sigmoid的Transformer（无论权重如何）在其隐式因子图上实现了加权循环信念传播（BP），一层Transformer对应一轮BP。论文进一步证明，Transformer可以实现任何声明知识库上的精确信念传播，从而在无循环依赖的知识库上产生可证明正确的概率估计。此外，论文还证明了唯一性：产生精确后验的Sigmoid Transformer必然具有BP权重。这项工作将Transformer的注意力机制和前馈网络分别对应于布尔逻辑的AND/OR结构及其交替执行。该理论框架为理解Transformer的推理机制提供了坚实的基础，对于构建和解释用于“化学大模型”和“质谱结构推理”的Transformer模型具有深远的理论指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Transformers are the dominant architecture in AI, yet why they work remains poorly understood. This paper offers a precise answer: a transformer is a Bayesian network. We establish this in five ways. First, we prove that every sigmoid transformer with any weights implements weighted loopy belief propagation on its implicit factor graph. One layer is one round of BP. This holds for any weights -- trained, random, or constructed. Formally verified against standard mathematical axioms. Second, we give a constructive proof that a transformer can implement exact belief propagation on any declared knowledge base. On knowledge bases without circular dependencies this yields provably correct probability estimates at every node. Formally verified against standard mathematical axioms. Third, we prove uniqueness: a sigmoid transformer that produces exact posteriors necessarily has BP weights. There is no other path through the sigmoid architecture to exact posteriors. Formally verified against standard mathematical axioms. Fourth, we delineate the AND/OR boolean structure of the transformer layer: attention is AND, the FFN is OR, and their strict alternation is Pearl's gather/update algorithm exactly. Fifth, we confirm all formal results experimentally, corroborating the Bayesian network characterization in practice. We also establish the practical viability of loopy belief propagation despite the current lack of a theoretical convergence guarantee. We further prove that verifiable inference requires a finite concept space. Any finite verification procedure can distinguish at most finitely many concepts. Without grounding, correctness is not defined. Hallucination is not a bug that scaling can fix. It is the structural consequence of operating without concepts. Formally verified against standard mathematical axioms.

</details>

---

### 9. [Synchronized DNA sources for unconditionally secure cryptography](https://arxiv.org/abs/2603.17149)

**基本信息**

- 🔗 arXiv: [`2603.17149`](https://arxiv.org/abs/2603.17149)
- 👥 作者: Sandra Jaudou, Hélène Gasnier, Elias Boudjella 等14人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17149.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种基于合成DNA分子池的密码学系统，这些DNA分子库作为同步熵源，本质上是一种新型的、可用于加密的化学数据集/资源。虽然主要应用在密码学，但其底层技术（分子编码、测序）与化学信息学和质谱分析所处理的分子数据在概念上相关，符合“数据资源相关”标准的广义解释。

**📖 中文摘要**

本文介绍了一种基于DNA的密码学原语，利用合成DNA的随机池在远距离双方之间建立同步的熵源。该方法使用包含随机索引-有效载荷对的重复DNA分子作为共享秘密。这些分子在本地进行测序和数字化，生成用于一次性密码本（OTP）加密的通用二进制掩码，从而在不依赖计算假设的情况下实现无条件安全。作者在东京和巴黎之间实验演示了该协议，生成了约400 Mb的共享秘密掩码。该系统的二进制掩码的最小熵满足最新的NIST要求，并且可以抵抗两种类型的对抗性干扰。这项工作将分子生物学和密码学结合起来，为全球通信网络中的无条件安全提供了一条有前景的新途径。虽然论文主题是密码学，但其核心创新在于利用合成DNA分子作为产生随机密钥的“数据/物质资源”，这种分子级别的信息编码和读取技术与质谱分析（作为另一种分子分析技术）在理念上有相通之处，且其构建的DNA分子库本身可被视为一种特殊的化学数据集。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Secure communication is the cornerstone of modern infrastructures, yet achieving unconditional security -resistant to any computational attack- remains a fundamental challenge. The One-Time Pad (OTP), proven by Shannon to offer perfect secrecy, requires a shared random key as long as the message, used only once. However, distributing large keys over long distances has been impractical due to the lack of secure and scalable sharing options. Here, we introduce a DNA-based cryptographic primitive that leverages random pools of synthetic DNA to install a synchronized entropy source between distant parties. Our approach uses duplicated DNA molecules -comprising random index-payload pairs- as a shared secret. These molecules are locally sequenced and digitized to generate a common binary mask for OTP encryption, achieving unconditional security without relying on computational assumptions. We experimentally demonstrate this protocol between Tokyo and Paris, using in-house sequencing, generating a shared secret mask of $\sim$ 400 Mb with a residual error rate to achieve the usual overall decryption failure rate of $2^{-128}$. The min-entropy of the binary mask meets the most recent National Institute of Standards and Technology requirements (SP 800-90B), and is comparable to that of approved cryptographic random number generators. Critically, our system can resist two types of adversarial interference through molecular copy-number statistics, providing an additional layer of security reminiscent of Quantum Key Distribution, but without distance limitations. This work establishes DNA as a scalable entropy source for long-distance OTP, enabling high-throughput and secure communications in sensitive contexts. By bridging molecular biology and cryptography, DNA-based key distribution opens a promising new route toward unconditional security in global communication networks.

</details>

---

### 10. [Self-Conditioned Denoising for Atomistic Representation Learning](https://arxiv.org/abs/2603.17196)

**基本信息**

- 🔗 arXiv: [`2603.17196`](https://arxiv.org/abs/2603.17196)
- 👥 作者: Tynan Perez, Rafael Gomez-Bombarelli
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17196.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发用于原子表示学习（涵盖分子、材料等）的自监督预训练方法（SCD），这直接属于“化学大模型”的研究范畴，旨在构建化学领域的基础模型。

**📖 中文摘要**

本文提出了一种名为自条件去噪（SCD）的预训练策略，旨在为原子表示学习构建基础模型。该方法是一种与主干网络无关的重建目标，利用自嵌入在原子数据的任何领域（包括小分子、蛋白质、周期性材料和“非平衡”几何结构）进行条件去噪。研究指出，大规模监督预训练（基于DFT力-能标签）为下游性质预测提供了最强的性能增益，而现有的自监督学习方法（SSL）仅限于基态几何结构和/或单一原子数据领域。SCD方法解决了这些不足。在控制主干架构和预训练数据集的情况下，SCD在多个下游基准测试中显著优于先前的SSL方法，并与监督的力-能预训练性能相当或更优。这项工作表明，一个经过SCD预训练的小型快速图神经网络（GNN）可以在多个领域的任务中，达到与在更大标记或未标记数据集上预训练的更大模型相竞争甚至更优的性能。该研究与化学信息学中构建用于分子和材料表示的“化学大模型”这一核心主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The success of large-scale pretraining in NLP and computer vision has catalyzed growing efforts to develop analogous foundation models for the physical sciences. However, pretraining strategies using atomistic data remain underexplored. To date, large-scale supervised pretraining on DFT force-energy labels has provided the strongest performance gains to downstream property prediction, out-performing existing methods of self-supervised learning (SSL) which remain limited to ground-state geometries, and/or single domains of atomistic data. We address these shortcomings with Self-Conditioned Denoising (SCD), a backbone-agnostic reconstruction objective that utilizes self-embeddings for conditional denoising across any domain of atomistic data, including small molecules, proteins, periodic materials, and 'non-equilibrium' geometries. When controlled for backbone architecture and pretraining dataset, SCD significantly outperforms previous SSL methods on downstream benchmarks and matches or exceeds the performance of supervised force-energy pretraining. We show that a small, fast GNN pretrained by SCD can achieve competitive or superior performance to larger models pretrained on significantly larger labeled or unlabeled datasets, across tasks in multiple domains. Our code is available at: this https URL

</details>

---

### 11. [Binary Latent Protein Fitness Landscapes for Quantum Annealing Optimization](https://arxiv.org/abs/2603.17247)

**基本信息**

- 🔗 arXiv: [`2603.17247`](https://arxiv.org/abs/2603.17247)
- 👥 作者: Truong-Son Hy
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17247.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于预训练蛋白质语言模型和优化框架的AI系统（Q-BIOLAT），用于蛋白质适应度图谱建模和变体设计，这直接属于“化学大模型”在生物化学和蛋白质工程中的应用。

**📖 中文摘要**

本文提出了Q-BIOLAT框架，用于在二进制潜在空间中建模和优化蛋白质适应度图谱。该方法利用预训练的蛋白质语言模型将蛋白质序列转换为连续嵌入，再进一步转化为紧凑的二进制潜在表示。在此空间中，蛋白质适应度使用二次无约束二进制优化（QUBO）模型进行近似，从而能够通过模拟退火和遗传算法等经典启发式方法进行高效的组合搜索。在ProteinGym基准测试中，Q-BIOLAT能够捕捉蛋白质适应度图谱中有意义的结构，并识别出高适应度的变体。该方法将蛋白质适应度表述为QUBO问题，为蛋白质表示学习和组合优化之间建立了桥梁。该框架与新兴的量子退火硬件天然兼容，为量子辅助的蛋白质工程开辟了新方向。这项工作直接涉及使用AI模型（蛋白质语言模型）进行蛋白质性质预测和优化，是“化学大模型”在生物分子领域的典型应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose Q-BIOLAT, a framework for modeling and optimizing protein fitness landscapes in binary latent spaces. Starting from protein sequences, we leverage pretrained protein language models to obtain continuous embeddings, which are then transformed into compact binary latent representations. In this space, protein fitness is approximated using a quadratic unconstrained binary optimization (QUBO) model, enabling efficient combinatorial search via classical heuristics such as simulated annealing and genetic algorithms. On the ProteinGym benchmark, we demonstrate that Q-BIOLAT captures meaningful structure in protein fitness landscapes and enables the identification of high-fitness variants. Despite using a simple binarization scheme, our method consistently retrieves sequences whose nearest neighbors lie within the top fraction of the training fitness distribution, particularly under the strongest configurations. We further show that different optimization strategies exhibit distinct behaviors, with evolutionary search performing better in higher-dimensional latent spaces and local search remaining competitive in preserving realistic sequences. Beyond its empirical performance, Q-BIOLAT provides a natural bridge between protein representation learning and combinatorial optimization. By formulating protein fitness as a QUBO problem, our framework is directly compatible with emerging quantum annealing hardware, opening new directions for quantum-assisted protein engineering. Our implementation is publicly available at: this https URL

</details>

---

### 12. [SCALE:Scalable Conditional Atlas-Level Endpoint transport for virtual cell perturbation prediction](https://arxiv.org/abs/2603.17380)

**基本信息**

- 🔗 arXiv: [`2603.17380`](https://arxiv.org/abs/2603.17380)
- 👥 作者: Shuizhou Chen, Lang Yu, Kedu Jin 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17380.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于虚拟细胞扰动预测的专门化大规模基础模型（SCALE），这直接围绕“化学大模型”这一主题。

**📖 中文摘要**

本文提出了SCALE，一个用于虚拟细胞扰动预测的大规模基础模型。该模型将扰动预测表述为条件传输问题，并使用基于流的架构实现，该架构将基于LLaMA的细胞编码与端点导向的监督相结合。这项工作属于“化学大模型”的范畴，因为它开发了一个专门用于生物化学领域（单细胞测量和扰动预测）的大型基础模型。模型的设计旨在处理高维稀疏的表达数据，并专注于学习细胞对遗传、化学或细胞因子扰动的响应，这与化学信息学中利用计算模型理解和预测化学/生物系统行为的目标高度一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Virtual cell models aim to enable in silico experimentation by predicting how cells respond to genetic, chemical, or cytokine perturbations from single-cell measurements. In practice, however, large-scale perturbation prediction remains constrained by three coupled bottlenecks: inefficient training and inference pipelines, unstable modeling in high-dimensional sparse expression space, and evaluation protocols that overemphasize reconstruction-like accuracy while underestimating biological fidelity. In this work we present a specialized large-scale foundation model SCALE for virtual cell perturbation prediction that addresses the above limitations jointly. First, we build a BioNeMo-based training and inference framework that substantially improves data throughput, distributed scalability, and deployment efficiency, yielding 12.51* speedup on pretrain and 1.29* on inference over the prior SOTA pipeline under matched system settings. Second, we formulate perturbation prediction as conditional transport and implement it with a set-aware flow architecture that couples LLaMA-based cellular encoding with endpoint-oriented supervision. This design yields more stable training and stronger recovery of perturbation effects. Third, we evaluate the model on Tahoe-100M using a rigorous cell-level protocol centered on biologically meaningful metrics rather than reconstruction alone. On this benchmark, our model improves PDCorr by 12.02% and DE Overlap by 10.66% over STATE. Together, these results suggest that advancing virtual cells requires not only better generative objectives, but also the co-design of scalable infrastructure, stable transport modeling, and biologically faithful evaluation.

</details>

---

### 13. [Cohomological Obstructions to Global Counterfactuals: A Sheaf-Theoretic Foundation for Generative Causal Models](https://arxiv.org/abs/2603.17384)

**基本信息**

- 🔗 arXiv: [`2603.17384`](https://arxiv.org/abs/2603.17384)
- 👥 作者: Rui Wu, Hong Xie, Yongjun Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17384.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是为生成式因果模型建立层论基础，这属于构建和理解复杂生成模型（“化学大模型”的一个方面）的理论前沿工作。

**📖 中文摘要**

本文为生成式因果模型提供了一个层论基础，形式化了结构因果模型作为Wasserstein空间上的胞腔层。它引入了“熵Wasserstein因果层拉普拉斯算子”，这是一个耦合的非线性Fokker-Planck方程系统。该框架旨在解决当因果图表现出非平凡同调性（如结构冲突或隐藏混杂因素）时，局部一致的因果机制无法自然产生全局连贯反事实的问题。这项工作在概念和方法论上与“化学大模型”相关，因为它为复杂的、可能具有高维和结构化数据（如scRNA-seq数据）的生成模型提供了严格的数学基础。论文中提到的scRNA-seq反事实实验也表明了其在化学生物学领域的潜在应用。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current continuous generative models (e.g., Diffusion Models, Flow Matching) implicitly assume that locally consistent causal mechanisms naturally yield globally coherent counterfactuals. In this paper, we prove that this assumption fails fundamentally when the causal graph exhibits non-trivial homology (e.g., structural conflicts or hidden confounders). We formalize structural causal models as cellular sheaves over Wasserstein spaces, providing a strict algebraic topological definition of cohomological obstructions in measure spaces. To ensure computational tractability and avoid deterministic singularities (which we define as manifold tearing), we introduce entropic regularization and derive the Entropic Wasserstein Causal Sheaf Laplacian, a novel system of coupled non-linear Fokker-Planck equations. Crucially, we prove an entropic pullback lemma for the first variation of pushforward measures. By integrating this with the Implicit Function Theorem (IFT) on Sinkhorn optimality conditions, we establish a direct algorithmic bridge to automatic differentiation (VJP), achieving O(1)-memory reverse-mode gradients strictly independent of the iteration horizon. Empirically, our framework successfully leverages thermodynamic noise to navigate topological barriers ("entropic tunneling") in high-dimensional scRNA-seq counterfactuals. Finally, we invert this theoretical framework to introduce the Topological Causal Score, demonstrating that our Sheaf Laplacian acts as a highly sensitive algebraic detector for topology-aware causal discovery.

</details>

---

### 14. [The Causal Uncertainty Principle: Manifold Tearing and the Topological Limits of Counterfactual Interventions](https://arxiv.org/abs/2603.17385)

**基本信息**

- 🔗 arXiv: [`2603.17385`](https://arxiv.org/abs/2603.17385)
- 👥 作者: Rui Wu, Hong Xie, Yongjun Li
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17385.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索连续生成模型（如扩散模型、流匹配）中因果干预的几何挑战和根本限制，这直接关联到“化学大模型”的可靠性和可解释性构建。

**📖 中文摘要**

本文研究了连续生成模型中因果干预的基本限制。它定义了“反事实事件视界”并证明了“流形撕裂定理”，指出确定性流在极端干预下不可避免地会产生有限时间奇点。论文还建立了关于干预极端性与身份保持之间权衡的“因果不确定性原理”。最后，它引入了“几何感知因果流”（GACF），一种利用拓扑雷达绕过流形撕裂的可扩展算法，并在高维scRNA-seq数据上进行了验证。这项工作与“化学大模型”主题相关，因为它深入探讨了生成模型（如扩散模型、流匹配）在因果推理场景下的能力和局限性，这对于在化学和生物学中构建可靠的可解释模型至关重要。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Judea Pearl's do-calculus provides a foundation for causal inference, but its translation to continuous generative models remains fraught with geometric challenges. We establish the fundamental limits of such interventions. We define the Counterfactual Event Horizon and prove the Manifold Tearing Theorem: deterministic flows inevitably develop finite-time singularities under extreme interventions. We establish the Causal Uncertainty Principle for the trade-off between intervention extremity and identity preservation. Finally, we introduce Geometry-Aware Causal Flow (GACF), a scalable algorithm that utilizes a topological radar to bypass manifold tearing, validated on high-dimensional scRNA-seq data.

</details>

---

### 15. [Causal Representation Learning on High-Dimensional Data: Benchmarks, Reproducibility, and Evaluation Metrics](https://arxiv.org/abs/2603.17405)

**基本信息**

- 🔗 arXiv: [`2603.17405`](https://arxiv.org/abs/2603.17405)
- 👥 作者: Alireza Sadeghi, Wael AbdAlmageed
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17405.pdf)

**💡 相关性分析**

满足标准2和3：论文提供了用于评估因果表示学习模型的数据集和评估指标的全面分析（满足标准2：数据资源相关）。同时，作为一篇综述性论文，它系统性地回顾和评估了CRL领域的现状、挑战和最佳实践，这对于指导化学和质谱领域的大模型开发具有重要的讨论价值（满足标准3：综述展望相关）。

**📖 中文摘要**

本文对高维数据的因果表示学习（CRL）进行了基准测试、可重复性和评估指标的综述。CRL模型旨在将高维数据转换到潜在空间，从而能够基于潜在变量之间的因果关系进行干预以生成反事实样本或修改现有数据。论文批判性地分析了文献中使用的合成和真实世界数据集，强调了它们的局限性，并提出了适用于CRL模型开发的数据集应具备的基本特征。此外，论文还引入了一个单一的聚合指标，以整合模型在所有评估方向（包括重建、解耦、因果发现和反事实推理）上的性能。这项工作与“化学大模型”和“质谱结构推理”都相关，因为CRL是构建可解释、可干预的化学和质谱分析模型的关键技术。论文中讨论的评估框架和数据集特征对于开发用于质谱数据解析的稳健模型具有指导意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Causal representation learning (CRL) models aim to transform high-dimensional data into a latent space, enabling interventions to generate counterfactual samples or modify existing data based on the causal relationships among latent variables. To facilitate the development and evaluation of these models, a variety of synthetic and real-world datasets have been proposed, each with distinct advantages and limitations. For practical applications, CRL models must perform robustly across multiple evaluation directions, including reconstruction, disentanglement, causal discovery, and counterfactual reasoning, using appropriate metrics for each direction. However, this multi-directional evaluation can complicate model comparison, as a model may excel in some direction while under-performing in others. Another significant challenge in this field is reproducibility: the source code corresponding to published results must be publicly available, and repeated runs should yield performance consistent with the original reports. In this study, we critically analyzed the synthetic and real-world datasets currently employed in the literature, highlighting their limitations and proposing a set of essential characteristics for suitable datasets in CRL model development. We also introduce a single aggregate metric that consolidates performance across all evaluation directions, providing a comprehensive score for each model. Finally, we reviewed existing implementations from the literature and assessed them in terms of reproducibility, identifying gaps and best practices in the field.

</details>

---

### 16. [Proactive Knowledge Inquiry in Doctor-Patient Dialogue: Stateful Extraction, Belief Updating, and Path-Aware Action Planning](https://arxiv.org/abs/2603.17425)

**基本信息**

- 🔗 arXiv: [`2603.17425`](https://arxiv.org/abs/2603.17425)
- 👥 作者: Zhenhai Pan, Yan Liu, Jia You
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17425.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出一个基于LLM的主动知识查询和推理框架，该框架的方法论（状态建模、混合检索、规划）对于构建能够进行复杂推理和交互的“化学大模型”具有直接的借鉴意义。

**📖 中文摘要**

本文将医患对话构建为一个部分可观测性下的主动知识查询问题。提出的框架结合了状态提取、顺序信念更新、间隙感知状态建模、基于客观化医学知识的混合检索以及一个POMDP-lite动作规划器。该框架将文档记录视为持续查询循环的结构化投影。虽然应用场景是临床对话，但其核心方法论——即使用大型语言模型（LLM）作为语义接口，通过结构化查询、信念更新和规划来主动获取和整合知识——与“化学大模型”的主题高度相关。这种主动推理和知识整合的框架可以类比地应用于化学信息学中，例如，通过对话或交互式查询来推理化学结构、性质或反应路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Most automated electronic medical record (EMR) pipelines remain output-oriented: they transcribe, extract, and summarize after the consultation, but they do not explicitly model what is already known, what is still missing, which uncertainty matters most, or what question or recommendation should come next. We formulate doctor-patient dialogue as a proactive knowledge-inquiry problem under partial observability. The proposed framework combines stateful extraction, sequential belief updating, gap-aware state modeling, hybrid retrieval over objectified medical knowledge, and a POMDP-lite action planner. Instead of treating the EMR as the only target artifact, the framework treats documentation as the structured projection of an ongoing inquiry loop. To make the formulation concrete, we report a controlled pilot evaluation on ten standardized multi-turn dialogues together with a 300-query retrieval benchmark aggregated across dialogues. On this pilot protocol, the full framework reaches 83.3% coverage, 80.0% risk recall, 81.4% structural completeness, and lower redundancy than the chunk-only and template-heavy interactive baselines. These pilot results do not establish clinical generalization; rather, they suggest that proactive inquiry may be methodologically interesting under tightly controlled conditions and can be viewed as a conceptually appealing formulation worth further investigation for dialogue-based EMR generation. This work should be read as a pilot concept demonstration under a controlled simulated setting rather than as evidence of clinical deployment readiness. No implication of clinical deployment readiness, clinical safety, or real-world clinical utility should be inferred from this pilot protocol.

</details>

---

### 17. [Humans and transformer LMs: Abstraction drives language learning](https://arxiv.org/abs/2603.17475)

**基本信息**

- 🔗 arXiv: [`2603.17475`](https://arxiv.org/abs/2603.17475)
- 👥 作者: Jasper Jian, Christopher D. Manning
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17475.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索Transformer语言模型（一种大模型）的学习机制和抽象能力的涌现，这直接与“化学大模型”这一主题相关，因为化学信息学中的大模型研究也关注模型如何学习和表示化学知识。

**📖 中文摘要**

这篇论文研究了基于Transformer的语言模型（LM）如何学习语言类别，并将其学习过程与人类语言习得的抽象特征和具体实例理论进行了比较。它通过新颖的基于分歧的度量来追踪学习轨迹，发现当学习一个结构时，抽象的类级行为比词汇项特定行为更早出现，并且不同的语言行为在训练的不同阶段依次突然出现。这表明抽象在语言模型学习中起着关键作用。论文的核心是探索语言模型（一种化学信息学中“化学大模型”的典型代表）的学习机制，特别是其抽象能力的涌现，这与“化学大模型”主题中模型如何学习化学概念和规则高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Categorization is a core component of human linguistic competence. We investigate how a transformer-based language model (LM) learns linguistic categories by comparing its behaviour over the course of training to behaviours which characterize abstract feature-based and concrete exemplar-based accounts of human language acquisition. We investigate how lexical semantic and syntactic categories emerge using novel divergence-based metrics that track learning trajectories using next-token distributions. In experiments with GPT-2 small, we find that (i) when a construction is learned, abstract class-level behaviour is evident at earlier steps than lexical item-specific behaviour, and (ii) that different linguistic behaviours emerge abruptly in sequence at different points in training, revealing that abstraction plays a key role in how LMs learn. This result informs the models of human language acquisition that LMs may serve as an existence proof for.

</details>

---

### 18. [Learning When to Attend: Conditional Memory Access for Long-Context LLMs](https://arxiv.org/abs/2603.17484)

**基本信息**

- 🔗 arXiv: [`2603.17484`](https://arxiv.org/abs/2603.17484)
- 👥 作者: Sakshi Choudhary, Aditya Chattopadhyay, Luca Zancato 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17484.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是改进大语言模型（LLM）的长上下文处理能力和效率，这直接属于“化学大模型”主题的范畴，因为化学领域的大模型（如用于分子性质预测或反应生成的模型）同样面临处理长序列（如长分子SMILES或复杂反应路径）的挑战。

**📖 中文摘要**

这篇论文提出了L2A（Learning To Attend），一种用于大语言模型（LLM）的条件记忆访问层，旨在解决模型难以泛化到预训练上下文长度之外的问题。L2A通过学习决定何时调用全局注意力，使模型能够条件性地（基于每个token）进行长程记忆访问。该方法在Qwen模型上进行了评估，成功将有效上下文长度从32K扩展到128K tokens，同时跳过了约80% token的全局注意力计算，实现了训练吞吐量和推理速度的提升。这项工作聚焦于改进大语言模型的长上下文处理能力，属于大模型架构和效率优化研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Language models struggle to generalize beyond pretraining context lengths, limiting long-horizon reasoning and retrieval. Continued pretraining on long-context data can help but is expensive due to the quadratic scaling of Attention. We observe that most tokens do not require (Global) Attention over the entire sequence and can rely on local context. Based on this, we propose L2A (Learning To Attend), a layer that enables conditional (token-wise) long-range memory access by deciding when to invoke global attention. We evaluate L2A on Qwen 2.5 and Qwen 3 models, extending their effective context length from 32K to 128K tokens. L2A matches the performance of standard long-context training to within 3% while skipping Global Attention for $\sim$80% of tokens, outperforming prior baselines. We also design custom Triton kernels to efficiently implement this token-wise conditional Attention on GPUs, achieving up to $\sim$2x improvements in training throughput and time-to-first-token over FlashAttention. Moreover, L2A enables post-training pruning of highly sparse Global Attention layers, reducing KV cache memory by up to 50% with negligible performance loss.

</details>

---

### 19. [Inducing Epistemological Humility in Large Language Models: A Targeted SFT Approach to Reducing Hallucination](https://arxiv.org/abs/2603.17504)

**基本信息**

- 🔗 arXiv: [`2603.17504`](https://arxiv.org/abs/2603.17504)
- 👥 作者: Cem Uluoglakci, Tugba Taskaya Temizel
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17504.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何通过数据和方法改进大语言模型（LLM）的可靠性，减少幻觉。这直接与“化学大模型”主题相关，因为化学领域的大模型（如用于文献总结或假设生成的模型）的准确性和可靠性至关重要。

**📖 中文摘要**

这篇论文针对大语言模型（LLM）的幻觉问题，提出了一种通过有监督微调（SFT）诱导模型产生“认识论谦逊”的方法。作者构建了HypoTermInstruct数据集，该数据集包含关于不存在的“假设”术语的问题，旨在教会模型承认自身知识的局限性。通过大量的控制实验，论文证明了使用这种针对性的SFT数据可以显著降低模型的幻觉倾向，同时保持其在通用知识基准上的性能。这项研究为大模型的可信性和可靠性提供了实用的改进路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) often hallucinate, producing fluent but false information, partly because supervised fine-tuning (SFT) implicitly rewards always responding. We introduce $\textit{HypoTermInstruct}$, an SFT dataset (31,487 responses for 11,151 questions) designed to teach models epistemological humility-the ability to recognize the limits of their own knowledge and admit uncertainty. This is achieved through questions about non-existent "hypothetical" terms. We also release $\textit{HypoTermQA-Enhanced}$, a benchmark for hallucination tendency strengthened through multiple validations. We conducted 800 controlled LoRA SFT runs across $\textit{Llama3.1-8B}$ and $\textit{Gemma3-4B}$ (base and instruct), testing 100 fine-tuning configurations with paired controls. Our results demonstrate that replacing generic instruction data with $\textit{HypoTermInstruct}$ significantly improves the HypoTerm Score (median increases of 0.19% to 25.91%) and FactScore (+0.39% to +0.86%), while maintaining stable performance on MMLU (minimal decreases of 0.26% to 0.35%). Our work demonstrates that targeted, high-quality SFT data teaching meta-cognitive skills can effectively reduce hallucination without preference/RL pipelines, providing mechanistic insights and a practical path toward more reliable AI systems.

</details>

---

### 20. [Language on Demand, Knowledge at Core: Composing LLMs with Encoder-Decoder Translation Models for Extensible Multilinguality](https://arxiv.org/abs/2603.17512)

**基本信息**

- 🔗 arXiv: [`2603.17512`](https://arxiv.org/abs/2603.17512)
- 👥 作者: Mengyu Bu, Yang Feng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17512.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是如何通过组合式架构增强大语言模型（LLM）的多语言能力，这属于大模型能力扩展和架构创新的范畴，与“化学大模型”主题中关于模型通用性和多任务处理的研究方向相关。

**📖 中文摘要**

这篇论文提出了XBridge架构，旨在解决大语言模型（LLM）在多语言任务上性能不平衡的问题。XBridge将多语言理解和生成任务卸载给外部预训练的编码器-解码器翻译模型，同时保留LLM作为以英语为核心的通识知识处理器。通过引入轻量级的跨模型映射层和基于最优传输的对齐目标，该框架实现了细粒度的语义一致性，从而在多语言理解、推理、总结和生成任务上取得了优异表现，特别是在低资源和未见语言上。这项工作属于大模型的多语言能力扩展和架构设计研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) exhibit strong general intelligence, yet their multilingual performance remains highly imbalanced. Although LLMs encode substantial cross-lingual knowledge in a unified semantic space, they often struggle to reliably interface this knowledge with low-resource or unseen languages. Fortunately, pretrained encoder-decoder translation models already possess balanced multilingual capability, suggesting a natural complement to LLMs. In this work, we propose XBridge, a compositional encoder-LLM-decoder architecture that offloads multilingual understanding and generation to external pretrained translation models, while preserving the LLM as an English-centric core for general knowledge processing. To address the resulting representation misalignment across models, we introduce lightweight cross-model mapping layers and an optimal transport-based alignment objective, enabling fine-grained semantic consistency for multilingual generation. Experiments on four LLMs across multilingual understanding, reasoning, summarization, and generation indicate that XBridge outperforms strong baselines, especially on low-resource and previously unseen languages, without retraining the LLM.

</details>

---

### 21. [Anisotropic Permeability Tensor Prediction from Porous Media Microstructure via Physics-Informed Progressive Transfer Learning with Hybrid CNN-Transformer](https://arxiv.org/abs/2603.17532)

**基本信息**

- 🔗 arXiv: [`2603.17532`](https://arxiv.org/abs/2603.17532)
- 👥 作者: Mohammad Nooraiepour
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17532.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个结合物理知识的深度学习模型（MaxViT混合架构）来解决科学计算中的逆问题（从结构预测性质）。虽然应用领域是地质/材料，但其方法论——物理信息深度学习、Transformer与CNN的混合架构、以及从复杂数据中学习物理规律——与“化学大模型”主题中利用AI模型从化学结构数据（如质谱、分子图）中推理物理化学性质的研究高度相似。

**📖 中文摘要**

这篇论文提出了一个物理信息驱动的深度学习框架，用于从多孔介质的微观结构图像中快速预测各向异性渗透率张量。该框架结合了混合CNN-Transformer架构（MaxViT）、渐进式迁移学习和可微分的物理约束（如Onsager互易性和正定性）。通过在大规模合成数据集上的训练，该模型能够以接近直接数值模拟的精度预测渗透率，同时计算成本大幅降低。论文强调了将物理约束作为可微架构组件集成的重要性。这项工作展示了深度学习（特别是结合物理知识的模型）在解决复杂科学计算问题（如多孔介质流动）中的潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurate prediction of permeability tensors from pore-scale microstructure images is essential for subsurface flow modeling, yet direct numerical simulation requires hours per sample, fundamentally limiting large-scale uncertainty quantification and reservoir optimization workflows. A physics-informed deep learning framework is presented that resolves this bottleneck by combining a MaxViT hybrid CNN-Transformer architecture with progressive transfer learning and differentiable physical constraints. MaxViT's multi-axis attention mechanism simultaneously resolves grain-scale pore-throat geometry via block-local operations and REV-scale connectivity statistics through grid-global operations, providing the spatial hierarchy that permeability tensor prediction physically requires. Training on 20000 synthetic porous media samples spanning three orders of magnitude in permeability, a three-phase progressive curriculum advances from an ImageNet-pretrained baseline with D4-equivariant augmentation and tensor transformation, through component-weighted loss prioritizing off-diagonal coupling, to frozen-backbone transfer learning with porosity conditioning via Feature-wise Linear Modulation (FiLM). Onsager reciprocity and positive definiteness are enforced via differentiable penalty terms. On a held-out test set of 4000 samples, the framework achieves variance-weighted R2 = 0.9960 (R2_Kxx = 0.9967, R2_Kxy = 0.9758), a 33% reduction in unexplained variance over the supervised baseline. The results offer three transferable principles for physics-informed scientific machine learning: large-scale visual pretraining transfers effectively across domain boundaries; physical constraints are most robustly integrated as differentiable architectural components; and progressive training guided by diagnostic failure-mode analysis enables unambiguous attribution of performance gains across methodological stages.

</details>

---

### 22. [A Unified Language Model for Large Scale Search, Recommendation, and Reasoning](https://arxiv.org/abs/2603.17533)

**基本信息**

- 🔗 arXiv: [`2603.17533`](https://arxiv.org/abs/2603.17533)
- 👥 作者: Marco De Nadai, Edoardo D'Amico, Max Lefarov 等21人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17533.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何改造和利用大语言模型（LLM）来处理大规模、结构化的实体发现任务（搜索、推荐、推理）。这属于大模型在特定领域（信息检索、推荐系统）的应用和适配研究，其“语言可操控性”和统一生成框架的思路与构建领域专用大模型（如化学大模型）有相通之处。

**📖 中文摘要**

这篇论文提出了NEO框架，旨在将预训练的解码器LLM适配为一个无需工具、基于目录的生成器，以统一支持大规模、异构目录上的搜索、推荐和推理任务。NEO将物品表示为语义ID（SID），并训练单个模型在共享序列中交错生成自然语言和类型化的物品标识符。通过指令控制任务、目标实体类型和输出格式，并利用约束解码保证生成物品的有效性。该框架在包含超过1000万物品的真实世界目录上进行了评估，在推荐、搜索和用户理解等发现任务上表现优异，并展示了跨任务迁移能力。这项工作探索了如何让大语言模型在严格延迟和可靠性约束下，对多领域实体、用户和语言进行联合推理。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

LLMs are increasingly applied to recommendation, retrieval, and reasoning, yet deploying a single end-to-end model that can jointly support these behaviors over large, heterogeneous catalogs remains challenging. Such systems must generate unambiguous references to real items, handle multiple entity types, and operate under strict latency and reliability constraints requirements that are difficult to satisfy with text-only generation. While tool-augmented recommender systems address parts of this problem, they introduce orchestration complexity and limit end-to-end optimization. We view this setting as an instance of a broader research problem: how to adapt LLMs to reason jointly over multiple-domain entities, users, and language in a fully self-contained manner. To this end, we introduce NEO, a framework that adapts a pre-trained decoder-only LLM into a tool-free, catalog-grounded generator. NEO represents items as SIDs and trains a single model to interleave natural language and typed item identifiers within a shared sequence. Text prompts control the task, target entity type, and output format (IDs, text, or mixed), while constrained decoding guarantees catalog-valid item generation without restricting free-form text. We refer to this instruction-conditioned controllability as language-steerability. We treat SIDs as a distinct modality and study design choices for integrating discrete entity representations into LLMs via staged alignment and instruction tuning. We evaluate NEO at scale on a real-world catalog of over 10M items across multiple media types and discovery tasks, including recommendation, search, and user understanding. In offline experiments, NEO consistently outperforms strong task-specific baselines and exhibits cross-task transfer, demonstrating a practical path toward consolidating large-scale discovery capabilities into a single language-steerable generative model.

</details>

---

### 23. [Learning Coordinate-based Convolutional Kernels for Continuous SE(3) Equivariant and Efficient Point Cloud Analysis](https://arxiv.org/abs/2603.17538)

**基本信息**

- 🔗 arXiv: [`2603.17538`](https://arxiv.org/abs/2603.17538)
- 👥 作者: Jaein Kim, Hee Bin Yoo, Dong-Sig Han 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17538.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发用于3D点云分析的等变神经网络。虽然应用场景是通用点云，但其核心方法——设计具有严格对称性（SE(3)）的深度学习模型——与“化学大模型”和“质谱结构推理”高度相关。在化学信息学中，分子可以表示为3D点云（原子坐标），其性质应在旋转和平移下不变（等变或不变）。同样，从质谱数据推理分子结构也需要对分子几何有深刻理解的模型。因此，该论文提出的等变卷积框架为处理化学3D结构数据提供了有力的工具。

**📖 中文摘要**

这篇论文提出了ECKConv（等变坐标核卷积），一种用于3D点云分析的SE(3)等变且高效的卷积方法。该方法利用交织器框架，在双陪集空间中定义核域以获得SE(3)等变性，并通过基于坐标的网络进行显式核设计，从而增强了学习能力和内存效率。在点云分类、姿态配准、部件分割和大规模语义分割等多种任务上的实验验证了该方法的刚性等变性、内存可扩展性和卓越性能。这项工作属于几何深度学习范畴，专注于设计具有严格对称性的高效模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A symmetry on rigid motion is one of the salient factors in efficient learning of 3D point cloud problems. Group convolution has been a representative method to extract equivariant features, but its realizations have struggled to retain both rigorous symmetry and scalability simultaneously. We advocate utilizing the intertwiner framework to resolve this trade-off, but previous works on it, which did not achieve complete SE(3) symmetry or scalability to large-scale problems, necessitate a more advanced kernel architecture. We present Equivariant Coordinate-based Kernel Convolution, or ECKConv. It acquires SE(3) equivariance from the kernel domain defined in a double coset space, and its explicit kernel design using coordinate-based networks enhances its learning capability and memory efficiency. The experiments on diverse point cloud tasks, e.g., classification, pose registration, part segmentation, and large-scale semantic segmentation, validate the rigid equivariance, memory scalability, and outstanding performance of ECKConv compared to state-of-the-art equivariant methods.

</details>

---

### 24. [KA2L: A Knowledge-Aware Active Learning Framework for LLMs](https://arxiv.org/abs/2603.17566)

**基本信息**

- 🔗 arXiv: [`2603.17566`](https://arxiv.org/abs/2603.17566)
- 👥 作者: Haoxuan Yin, Bojian Liu, Chen Tang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17566.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何为大语言模型（LLM）设计高效的主动学习框架，以针对性地提升其领域知识。这直接与“化学大模型”主题相关，因为训练化学领域的大模型通常需要大量标注数据，而主动学习策略可以优化数据使用效率，帮助模型更快地掌握复杂的化学知识。

**📖 中文摘要**

这篇论文提出了KA2L（知识感知主动学习）框架，旨在通过评估大语言模型（LLM）对特定知识点的掌握程度，来构建模型尚未掌握的问题，从而实现高效的主动学习。该框架采用知识分布探测技术来检查Transformer特定层的隐藏状态，识别LLM中已知和未知知识的分布，并提出一种隐藏状态解码方法，从潜在知识空间生成大量未知问题的自然语言表述。实验表明，KA2L能在显著降低标注和计算成本的同时，提升模型性能。这项工作为大模型的主动学习策略提供了新见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Fine-tuning large language models (LLMs) with high-quality knowledge has been shown to enhance their performance effectively. However, there is a paucity of research on the depth of domain-specific knowledge comprehension by LLMs and the application of targeted active learning to improve their expertise. To address this gap, we introduce the Knowledge-Aware Active Learning (KA2L) framework. This framework assesses LLMs' mastery of specific knowledge points to aid in constructing unanswerable or unknowable questions through latent space analysis. This active learning strategy enhances training efficiency by focusing on knowledge the model has yet to master, thereby minimizing redundancy in learning already acquired information. This study innovatively employs a knowledge distribution probing technique to examine the hidden states of specific Transformer layers and identify the distribution of known and unknown knowledge within the LLM. Additionally, a hidden-state decoding method is proposed to generate numerous unknown questions in natural language from the latent knowledge space. In our experiments, we selected nine open-source LLMs to validate the effectiveness of the proposed framework. Results indicate that KA2L not only significantly reduces 50% annotation and computation costs across two open-domain and one vertical-domain dataset but also achieves better performance, offering valuable insights into active learning strategies for LLMs. The code is available at this https URL .

</details>

---

### 25. [Unsupervised Symbolic Anomaly Detection](https://arxiv.org/abs/2603.17575)

**基本信息**

- 🔗 arXiv: [`2603.17575`](https://arxiv.org/abs/2603.17575)
- 👥 作者: Md Maruf Hossain, Tim Katzke, Simon Klüttermann 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17575.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种基于符号回归的、可解释的异常检测方法。虽然应用领域不限，但其方法论——从数据中学习人类可读的符号规则（方程）——与“化学大模型”和“质谱结构推理”主题高度相关。在化学信息学中，从质谱数据中推导出解释峰出现的符号化规则（如同位素模式、碎裂规律），正是“质谱结构推理”的核心任务之一。SYRAN提供了一种实现这种可解释推理的潜在框架。

**📖 中文摘要**

这篇论文提出了SYRAN，一种基于符号回归的无监督异常检测方法。与将正常模式编码在高维不透明模型中的方法不同，SYRAN学习一组人类可读的方程来描述符号不变量（即在正常数据上近似恒定的函数）。对这些不变量的偏离即产生异常分数，从而使检测逻辑本身是可解释的。实验结果表明，SYRAN具有高度可解释性，并能提供与已知科学或医学关系对应的方程，同时保持了与最先进方法相当的强大异常检测性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose SYRAN, an unsupervised anomaly detection method based on symbolic regression. Instead of encoding normal patterns in an opaque, high-dimensional model, our method learns an ensemble of human-readable equations that describe symbolic invariants: functions that are approximately constant on normal data. Deviations from these invariants yield anomaly scores, so that the detection logic is interpretable by construction, rather than via post-hoc explanation. Experimental results demonstrate that SYRAN is highly interpretable, providing equations that correspond to known scientific or medical relationships, and maintains strong anomaly detection performance comparable to that of state-of-the-art methods.

</details>

---

### 26. [From Isolated Scoring to Collaborative Ranking: A Comparison-Native Framework for LLM-Based Paper Evaluation](https://arxiv.org/abs/2603.17588)

**基本信息**

- 🔗 arXiv: [`2603.17588`](https://arxiv.org/abs/2603.17588)
- 👥 作者: Pujun Zheng, Jiacheng Yao, Jinquan Zheng 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17588.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是开发一个基于大语言模型（LLM）的、用于科学论文评估和排名的框架。这属于大模型在特定垂直领域（学术评估）的应用，与构建用于化学文献分析、论文筛选或知识发现的“化学大模型”有直接关联。

**📖 中文摘要**

这篇论文提出了CNPE框架，将论文评估任务从独立的绝对评分转向协作式排名。该框架通过基于图的相似性排序算法从论文集合中采样更具信息量和区分度的论文对，然后通过有监督微调和基于比较的奖励强化学习来增强相对质量判断能力。在推理时，模型对采样的论文对进行两两比较，并将这些偏好信号聚合成全局的相对质量排名。实验表明，该框架在多个未见数据集上表现出强大的泛化能力。这项工作聚焦于利用大语言模型（LLM）进行科学论文评估，属于大模型在学术领域的应用研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) are currently applied to scientific paper evaluation by assigning an absolute score to each paper independently. However, since score scales vary across conferences, time periods, and evaluation criteria, models trained on absolute scores are prone to fitting narrow, context-specific rules rather than developing robust scholarly judgment. To overcome this limitation, we propose shifting paper evaluation from isolated scoring to collaborative ranking. In particular, we design \textbf{C}omparison-\textbf{N}ative framework for \textbf{P}aper \textbf{E}valuation (\textbf{CNPE}), integrating comparison into both data construction and model learning. We first propose a graph-based similarity ranking algorithm to facilitate the sampling of more informative and discriminative paper pairs from a collection. We then enhance relative quality judgment through supervised fine-tuning and reinforcement learning with comparison-based rewards. At inference, the model performs pairwise comparisons over sampled paper pairs and aggregates these preference signals into a global relative quality ranking. Experimental results demonstrate that our framework achieves an average relative improvement of \textbf{21.8\%} over the strong baseline DeepReview-14B, while exhibiting robust generalization to five previously unseen datasets. \href{ this https URL }{Code}.

</details>

---

### 27. [Do Language Models Encode Semantic Relations? Probing and Sparse Feature Analysis](https://arxiv.org/abs/2603.17624)

**基本信息**

- 🔗 arXiv: [`2603.17624`](https://arxiv.org/abs/2603.17624)
- 👥 作者: Andor Diera, Ansgar Scherp
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17624.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索语言模型内部如何表示和编码语义关系。理解大模型如何学习概念之间的关系，对于构建能够理解化学实体间关系（如官能团、反应类型、性质趋势）的“化学大模型”至关重要。这项基础性研究为化学领域大模型的知识表示和推理能力提供了理论参考。

**📖 中文摘要**

这篇论文研究了不同规模的语言模型（Pythia-70M, GPT-2, Llama 3.1 8B）是否以及如何编码四种语义关系（同义、反义、上位、下位）。研究结合了线性探测和机制可解释性技术（如稀疏自编码器和激活修补），以识别这些关系在模型中的编码位置和方式。结果表明，关系信号是分散的，但在中层达到峰值，并且在残差后/MLP通路中比在注意力中更强。在Llama 3.1上，稀疏自编码器引导的修补可以可靠地改变这些信号。这项工作为了解LLM内部如何表示结构化语义关系提供了清晰的证据和可复现框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding whether large language models (LLMs) capture structured meaning requires examining how they represent concept relationships. In this work, we study three models of increasing scale: Pythia-70M, GPT-2, and Llama 3.1 8B, focusing on four semantic relations: synonymy, antonymy, hypernymy, and hyponymy. We combine linear probing with mechanistic interpretability techniques, including sparse autoencoders (SAE) and activation patching, to identify where these relations are encoded and how specific features contribute to their representation. Our results reveal a directional asymmetry in hierarchical relations: hypernymy is encoded redundantly and resists suppression, while hyponymy relies on compact features that are more easily disrupted by ablation. More broadly, relation signals are diffuse but exhibit stable profiles: they peak in the mid-layers and are stronger in post-residual/MLP pathways than in attention. Difficulty is consistent across models (antonymy easiest, synonymy hardest). Probe-level causality is capacity-dependent: on Llama 3.1, SAE-guided patching reliably shifts these signals, whereas on smaller models the shifts are weak or unstable. Our results clarify where and how reliably semantic relations are represented inside LLMs, and provide a reproducible framework for relating sparse features to probe-level causal evidence.

</details>

---

### 28. [The Program Hypergraph: Multi-Way Relational Structure for Geometric Algebra, Spatial Compute, and Physics-Aware Compilation](https://arxiv.org/abs/2603.17627)

**基本信息**

- 🔗 arXiv: [`2603.17627`](https://arxiv.org/abs/2603.17627)
- 👥 作者: Houston Haynes
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17627.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是将几何代数（克利福德代数）集成到编译框架中，并利用超图结构进行表示和优化。几何代数是描述物理和几何（包括分子几何和对称性）的强大数学工具。这项工作为在“化学大模型”中更自然、更高效地集成和处理几何与物理约束（例如，在分子动力学模拟或三维分子结构生成中）提供了底层计算和表示基础。

**📖 中文摘要**

这篇论文引入了程序超图（PHG），作为程序语义图（PSG）的泛化，将二元边推广到任意元数的超边。论文展示了克利福德代数中的“阶”是现有维度类型系统框架内的一个自然维度轴，阶推断可以推导出几何乘积的稀疏性，从而无需手动特化即可消除克利福德代数神经网络的主要性能障碍。PHG在Fidelity编译框架内解决了当前几何代数库生态系统一致存在的类型理论差距。其结果是一个编译框架，其中几何正确性、内存布局、数值精度选择和硬件分区都可以从单个图结构联合推导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Program Semantic Graph (PSG) introduced in prior work on Dimensional Type Systems and Deterministic Memory Management encodes compilation-relevant properties as binary edge relations between computation nodes. This representation is adequate for scalar and tensor computations, but becomes structurally insufficient for two classes of problems central to heterogeneous compute: tile co-location and routing constraints in spatial dataflow architectures, which are inherently multi-way; and geometric algebra computation, where graded multi-way products cannot be faithfully represented as sequences of binary operations without loss of algebraic identity. This paper introduces the Program Hypergraph (PHG) as a principled generalization of the PSG that promotes binary edges to hyperedges of arbitrary arity. We demonstrate that grade in Clifford algebra is a natural dimension axis within the existing DTS abelian group framework, that grade inference derives geometric product sparsity eliminating the primary performance objection to Clifford algebra neural networks without manual specialization, and that the k-simplex structure of mesh topology is a direct instance of the hyperedge formalism. We assess the existing geometric algebra library ecosystem, identify the consistent type-theoretic gap that no current system addresses, and show that the PHG closes it within the Fidelity compilation framework. The result is a compilation framework where geometric correctness, memory placement, numerical precision selection, and hardware partitioning are jointly derivable from a single graph structure exposed as interactive design-time feedback.

</details>

---

### 29. [Interpretable Cross-Domain Few-Shot Learning with Rectified Target-Domain Local Alignment](https://arxiv.org/abs/2603.17655)

**基本信息**

- 🔗 arXiv: [`2603.17655`](https://arxiv.org/abs/2603.17655)
- 👥 作者: Yaze Zhao, Yixiong Zou, Yuhua Li 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17655.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是改进视觉-语言模型（如CLIP）在跨域少样本学习中的细粒度对齐能力。虽然应用场景是通用图像分类，但其核心问题——如何让模型更好地对齐局部视觉特征和语义概念——与“质谱结构推理”高度相关。在质谱分析中，需要将质谱图中的局部峰（视觉特征）与特定的分子子结构或碎裂途径（语义概念）精确对齐。该论文的方法论为解决此类跨模态细粒度对齐问题提供了思路。

**📖 中文摘要**

这篇论文针对基于CLIP的跨域少样本学习（CDFSL）中存在的局部错位问题，提出了CC-CDFSL方法。该方法利用循环一致性，将局部视觉特征翻译成文本特征再翻译回视觉特征（反之亦然），并约束原始特征接近翻译回来的特征。为了减少视觉模态中更丰富信息引入的噪声，进一步提出了语义锚机制。实验表明，该方法能有效改善局部视觉-语言对齐，通过可视化图像块增强所学模式和模型决策的可解释性，并在多个基准上达到最先进的性能。这项工作聚焦于提升视觉-语言模型在细粒度跨域任务中的对齐和可解释性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Cross-Domain Few-Shot Learning (CDFSL) adapts models trained with large-scale general data (source domain) to downstream target domains with only scarce training data, where the research on vision-language models (e.g., CLIP) is still in the early stages. Typical downstream domains, such as medical diagnosis, require fine-grained visual cues for interpretable recognition, but we find that current fine-tuned CLIP models can hardly focus on these cues, albeit they can roughly focus on important regions in source domains. Although current works have demonstrated CLIP's shortcomings in capturing local subtle patterns, in this paper, we find that the domain gap and scarce training data further exacerbate such shortcomings, much more than that of holistic patterns, which we call the local misalignment problem in CLIP-based CDFSL. To address this problem, due to the lack of supervision in aligning local visual features and text semantics, we turn to self-supervision information. Inspired by the translation task, we propose the CC-CDFSL method with cycle consistency, which translates local visual features into text features and then translates them back into visual features (and vice versa), and constrains the original features close to the translated back features. To reduce the noise imported by richer information in the visual modality, we further propose a Semantic Anchor mechanism, which first augments visual features to provide a larger corpus for the text-to-image mapping, and then shrinks the image features to filter out irrelevant image-to-text mapping. Extensive experiments on various benchmarks, backbones, and fine-tuning methods show we can (1) effectively improve the local vision-language alignment, (2) enhance the interpretability of learned patterns and model decisions by visualizing patches, and (3) achieve state-of-the-art performance.

</details>

---

### 30. [From Symbol to Meaning: Ontological and Philosophical Reflections on Large Language Models in Information Systems Engineering](https://arxiv.org/abs/2603.17659)

**基本信息**

- 🔗 arXiv: [`2603.17659`](https://arxiv.org/abs/2603.17659)
- 👥 作者: José Palazzo Moreira de Oliveira
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17659.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对大型语言模型（LLM）的哲学和理论性综述与展望。它深入讨论了LLM对信息、知识和表示的根本性影响。虽然不直接涉及化学，但它对“大模型”的本质、局限性和社会影响的批判性思考，为任何领域（包括化学信息学）应用大模型提供了重要的元认知框架和伦理考量，属于对“化学大模型”主题的宏观和前瞻性讨论。

**📖 中文摘要**

这篇论文从本体论、认识论和符号学角度，对大型语言模型（LLM）在信息系统工程中的理论基础进行了反思。论文认为，LLM的出现重新配置了语言、意义和系统设计之间的关系，要求重新审视当代信息系统的概念基础。借鉴从皮尔斯到海德格尔和弗洛里迪的哲学传统，论文探讨了生成模型的逻辑如何扩展并破坏经典的本体论和意指概念。讨论强调，有必要将基于LLM的系统建立在透明、伦理连贯的框架中，以尊重以人为中心的知识过程的完整性。最终，论文主张LLM不应仅仅被理解为自动化工具，而应被理解为重塑信息系统工程哲学和符号学基础的认识论主体。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The advent of Large Language Models (LLMs) represents a turning point in the theoretical foundations of Information Systems Engineering. Beyond their technical significance, LLMs challenge the ontological, epistemological, and semiotic assumptions that have long structured our understanding of in-formation, representation, and knowledge. This article proposes an integrative reflection on how LLMs reconfigure the relationships among language, meaning, and system design, suggesting that their emergence demands a re-examination of the conceptual foundations of contemporary information systems. Sketching on philosophical traditions from Peirce to Heidegger and Floridi, we investigate how the logic of generative models both extends and destabilises classical notions of ontology and signification. The discussion emphasises the necessity of grounding LLM-based systems in transparent, ethically coherent frameworks that respect the integrity of human-centred knowledge processes. Ultimately, the paper argues that LLMs should be understood not merely as tools for automation but as epistemic agents that reshape the philosophical and semiotic foundations of information systems engineering.

</details>

---

### 31. [FINER: MLLMs Hallucinate under Fine-grained Negative Queries](https://arxiv.org/abs/2603.17662)

**基本信息**

- 🔗 arXiv: [`2603.17662`](https://arxiv.org/abs/2603.17662)
- 👥 作者: Rui Xiao, Sanghwan Kim, Yongqin Xian 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17662.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心研究多模态大语言模型（MLLM）的幻觉问题及解决方案，这直接关联“化学大模型”的可靠性（例如，化学图像描述或谱图解释模型必须高度准确）。2) 论文提出了新的基准数据集（FINER-CompreCap和FINER-DOCCI），可用于评估MLLM的细粒度感知和幻觉倾向，这为相关研究提供了重要的数据资源。

**📖 中文摘要**

这篇论文指出了当前多模态大语言模型（MLLM）在细粒度负面查询下容易产生幻觉的问题，并为此引入了FIne-grained NEgative queRies（FINER）基准，包括FINER-CompreCap和FINER-DOCCI。该基准揭示了当细粒度不匹配与图像中真实存在的元素同时出现时，MLLM会产生幻觉。为了应对这一问题，论文提出了FINER-Tuning方法，利用直接偏好优化（DPO）在FINER启发的数据上进行微调。对四个前沿MLLM的微调实验表明，该方法在幻觉基准上取得了显著提升，同时增强了通用多模态能力。这项工作专注于评估和提升MLLM在细粒度场景下的可靠性和准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal large language models (MLLMs) struggle with hallucinations, particularly with fine-grained queries, a challenge underrepresented by existing benchmarks that focus on coarse image-related questions. We introduce FIne-grained NEgative queRies (FINER), alongside two benchmarks: FINER-CompreCap and FINER-DOCCI. Using FINER, we analyze hallucinations across four settings: multi-object, multi-attribute, multi-relation, and ``what'' questions. Our benchmarks reveal that MLLMs hallucinate when fine-grained mismatches co-occur with genuinely present elements in the image. To address this, we propose FINER-Tuning, leveraging Direct Preference Optimization (DPO) on FINER-inspired data. Finetuning four frontier MLLMs with FINER-Tuning yields up to 24.2\% gains (InternVL3.5-14B) on hallucinations from our benchmarks, while simultaneously improving performance on eight existing hallucination suites, and enhancing general multimodal capabilities across six benchmarks. Code, benchmark, and models are available at \href{ this https URL }{ this https URL }.

</details>

---

### 32. [Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671)

**基本信息**

- 🔗 arXiv: [`2603.17671`](https://arxiv.org/abs/2603.17671)
- 👥 作者: Liangyu Yuan, Ruoyu Wang, Tong Zhao 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17671.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进扩散模型的采样框架，这是一种在化学信息学中用于分子生成和性质预测的“化学大模型”的关键底层技术。

**📖 中文摘要**

本文提出了一种实例感知的离散化框架，用于改进扩散和流匹配模型的采样过程。虽然论文主要关注于通用生成模型（如图像、视频）的采样加速，但其核心方法——通过自适应时间步分配来优化基于ODE/SDE的生成路径——与“化学大模型”中用于分子生成或性质预测的扩散模型在方法论上高度相关。该论文提出的框架可以潜在地应用于化学领域，例如用于生成分子结构或预测质谱图的扩散模型，以提升其采样效率和生成质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion and flow matching models generate high-fidelity data by simulating paths defined by Ordinary or Stochastic Differential Equations (ODEs/SDEs), starting from a tractable prior distribution. The probability flow ODE formulation enables the use of advanced numerical solvers to accelerate sampling. Orthogonal yet vital to solver design is the discretization strategy. While early approaches employed handcrafted heuristics and recent methods adopt optimization-based techniques, most existing strategies enforce a globally shared timestep schedule across all samples. This uniform treatment fails to account for instance-specific complexity in the generative process, potentially limiting performance. Motivated by controlled experiments on synthetic data, which reveals the suboptimality of global schedules under instance-specific dynamics, we propose an instance-aware discretization framework. Our method learns to adapt timestep allocations based on input-dependent priors, extending gradient-based discretization search to the conditional generative setting. Empirical results across diverse settings, including synthetic data, pixel-space diffusion, latent-space images and video flow matching models, demonstrate that our method consistently improves generation quality with marginal tuning cost compared to training and negligible inference overhead.

</details>

---

### 33. [Adaptive Guidance for Retrieval-Augmented Masked Diffusion Models](https://arxiv.org/abs/2603.17677)

**基本信息**

- 🔗 arXiv: [`2603.17677`](https://arxiv.org/abs/2603.17677)
- 👥 作者: Jaemin Kim, Jong Chul Ye
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17677.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕改进扩散模型（一种重要的生成式大模型）与外部知识的整合机制，这与构建更强大、更可靠的“化学大模型”直接相关。

**📖 中文摘要**

本文提出了自适应检索增强掩码扩散模型（ARAM），一个用于在检索增强生成（RAG）设置中校准掩码扩散模型（MDM）引导的训练免费框架。虽然论文的评估集中在知识密集型问答任务上，但其核心技术创新——动态调整基于检索上下文的引导尺度——直接针对扩散模型在整合外部知识时面临的挑战。鉴于扩散模型是构建“化学大模型”（如用于分子设计或反应预测）的重要范式，本文提出的自适应引导机制为解决化学领域扩散模型如何有效、可靠地利用外部化学知识库（如反应规则、光谱数据库）提供了方法论上的参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-Augmented Generation (RAG) improves factual grounding by incorporating external knowledge into language model generation. However, when retrieved context is noisy, unreliable, or inconsistent with the model's parametric knowledge, it introduces retrieval-prior conflicts that can degrade generation quality. While this problem has been studied in autoregressive language models, it remains largely unexplored in diffusion-based language models, where the iterative denoising process introduces unique challenges for integrating retrieved context. In this work, we propose Adaptive Retrieval-Augmented Masked Diffusion (ARAM), a training-free adaptive guidance framework for Masked Diffusion Models (MDMs) in RAG settings. ARAM dynamically calibrates the guidance scale during denoising according to the Signal-to-Noise Ratio (SNR) of the distributional shift induced by retrieved context. Intuitively, the model strengthens guidance when the retrieved context provides reliable corrective evidence and suppresses it when the contextual signal is noisy or non-supportive. Extensive experiments on multiple knowledge-intensive QA benchmarks show that ARAM improves overall QA performance over competitive RAG baselines.

</details>

---

### 34. [Flow Matching Policy with Entropy Regularization](https://arxiv.org/abs/2603.17685)

**基本信息**

- 🔗 arXiv: [`2603.17685`](https://arxiv.org/abs/2603.17685)
- 👥 作者: Ting Gao, Stavros Orfanoudakis, Nan Lin 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17685.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容“流匹配”是构建生成式“化学大模型”的关键技术之一，其与强化学习的结合为化学领域的决策优化问题提供了方法论参考。

**📖 中文摘要**

本文提出了带有熵正则化的流匹配策略（FMER），一个基于常微分方程（ODE）的在线强化学习框架。FMER通过流匹配来参数化策略，并沿着由最优传输启发的直线概率路径采样动作。论文在机器人操控任务上进行了验证。虽然应用领域不同，但“流匹配”是当前生成式AI，特别是连续数据（如分子构象、光谱）生成模型中的一项重要技术。将流匹配与熵正则化结合用于策略学习的方法，为在化学领域构建能够进行探索和优化的“智能体”（例如，用于逆合成规划或实验条件优化的AI）提供了新的技术思路，属于“化学大模型”中决策与优化方向的相关工作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion-based policies have gained significant popularity in Reinforcement Learning (RL) due to their ability to represent complex, non-Gaussian distributions. Stochastic Differential Equation (SDE)-based diffusion policies often rely on indirect entropy control due to the intractability of the exact entropy, while also suffering from computationally prohibitive policy gradients through the iterative denoising chain. To overcome these issues, we propose Flow Matching Policy with Entropy Regularization (FMER), an Ordinary Differential Equation (ODE)-based online RL framework. FMER parameterizes the policy via flow matching and samples actions along a straight probability path, motivated by optimal transport. FMER leverages the model's generative nature to construct an advantage-weighted target velocity field from a candidate set, steering policy updates toward high-value regions. By deriving a tractable entropy objective, FMER enables principled maximum-entropy optimization for enhanced exploration. Experiments on sparse multi-goal FrankaKitchen benchmarks demonstrate that FMER outperforms state-of-the-art methods, while remaining competitive on standard MuJoco benchmarks. Moreover, FMER reduces training time by 7x compared to heavy diffusion baselines (QVPO) and 10-15% relative to efficient variants.

</details>

---

### 35. [Cache-enabled Generative Joint Source-Channel Coding for Evolving Semantic Communications](https://arxiv.org/abs/2603.17702)

**基本信息**

- 🔗 arXiv: [`2603.17702`](https://arxiv.org/abs/2603.17702)
- 👥 作者: Shunpu Tang, Qianqian Yang, Jihong Park 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17702.pdf)

**💡 相关性分析**

满足标准1：论文的核心方法利用了预训练的大规模生成模型（GAN）进行语义推理和重建，这与利用“化学大模型”从复杂数据（如质谱）中推理化学结构在范式上相通。

**📖 中文摘要**

本文提出了一种基于通道感知生成对抗网络（GAN）反转的联合信源信道编码框架（CAGI-JSCC），用于实现免训练的语义通信。该框架利用预训练的SemanticStyleGAN模型，并通过引入缓存机制来重用已传输的语义组件。虽然论文的应用场景是图像传输，但其核心思想——利用预训练的大规模生成模型（GAN）作为语义先验，并通过缓存和重用语义组件来提升效率——与“化学大模型”和“质谱结构推理”有潜在关联。例如，在质谱分析中，可以设想使用预训练的化学结构生成模型作为先验，通过类似的反转和缓存机制，从质谱数据中更高效地推断出分子结构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning-based semantic communication (SemCom) has recently emerged as a promising paradigm for improving the transmission efficiency of wireless networks. However, existing methods typically rely on extensive end-to-end training, which is both inflexible and computationally expensive in dynamic wireless environments. Moreover, they fail to exploit redundancy across multiple transmissions of semantically similar content, limiting overall efficiency. To overcome these limitations, we propose a channel-aware generative adversarial network (GAN) inversion-based joint source-channel coding (CAGI-JSCC) framework that enables training-free SemCom by leveraging a pre-trained SemanticStyleGAN model. By explicitly incorporating wireless channel characteristics into the GAN inversion process, CAGI-JSCC adapts to varying channel conditions without additional training. Furthermore, we introduce a cache-enabled dynamic codebook (CDC) that caches disentangled semantic components at both the transmitter and receiver, allowing the system to reuse previously transmitted content. This semantic-level caching can continuously reduce redundant transmissions as experience accumulates. Extensive experiments on image transmission demonstrate the effectiveness of the proposed framework. In particular, our system achieves comparable perceptual quality with an average bandwidth compression ratio (BCR) of 1/224, and as low as 1/1024 for a single image, significantly outperforming baselines with a BCR of 1/128.

</details>

---

### 36. [From Virtual Environments to Real-World Trials: Emerging Trends in Autonomous Driving](https://arxiv.org/abs/2603.17714)

**基本信息**

- 🔗 arXiv: [`2603.17714`](https://arxiv.org/abs/2603.17714)
- 👥 作者: A. Humnabadkar, A. Sikdar, B. Cave 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17714.pdf)

**💡 相关性分析**

满足标准3：论文是一篇综述，其中包含了对合成数据、仿真、领域自适应等跨领域方法的系统性讨论，这些方法对于推动“化学大模型”和“质谱结构推理”的研究具有重要的参考和展望价值。

**📖 中文摘要**

本文是一篇关于自动驾驶技术的综述，全面回顾了合成数据、虚拟环境、数字孪生、领域自适应以及视觉语言模型在该领域的应用和发展趋势。虽然主题是自动驾驶，但综述中系统讨论的“使用合成数据进行感知和规划”、“数字孪生仿真进行系统验证”以及“连接合成与现实数据的领域适应策略”是跨领域的通用方法论。这些方法对于“化学大模型”和“质谱结构推理”的研究具有重要的借鉴意义。例如，在化学领域，可以利用合成数据（如计算生成的质谱-结构对）来训练模型，通过数字孪生模拟实验过程，并研究如何将模型从模拟数据迁移到真实实验数据。因此，这篇综述包含了与关注主题相关的重要讨论和展望。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Autonomous driving technologies have achieved significant advances in recent years, yet their real-world deployment remains constrained by data scarcity, safety requirements, and the need for generalization across diverse environments. In response, synthetic data and virtual environments have emerged as powerful enablers, offering scalable, controllable, and richly annotated scenarios for training and evaluation. This survey presents a comprehensive review of recent developments at the intersection of autonomous driving, simulation technologies, and synthetic datasets. We organize the landscape across three core dimensions: (i) the use of synthetic data for perception and planning, (ii) digital twin-based simulation for system validation, and (iii) domain adaptation strategies bridging synthetic and real-world data. We also highlight the role of vision-language models and simulation realism in enhancing scene understanding and generalization. A detailed taxonomy of datasets, tools, and simulation platforms is provided, alongside an analysis of trends in benchmark design. Finally, we discuss critical challenges and open research directions, including Sim2Real transfer, scalable safety validation, cooperative autonomy, and simulation-driven policy learning, that must be addressed to accelerate the path toward safe, generalizable, and globally deployable autonomous driving systems.

</details>

---

### 37. [Towards Infinitely Long Neural Simulations: Self-Refining Neural Surrogate Models for Dynamical Systems](https://arxiv.org/abs/2603.17750)

**基本信息**

- 🔗 arXiv: [`2603.17750`](https://arxiv.org/abs/2603.17750)
- 👥 作者: Qi Liu, Laure Zanna, Joan Bruna
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17750.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕提升生成模型/代理模型在模拟动力系统时的长期一致性，这是构建用于化学过程模拟或光谱序列生成的“化学大模型”必须解决的关键问题之一。

**📖 中文摘要**

本文针对自回归神经代理模型在模拟动力系统时存在的分布漂移（长期一致性差）问题，提出了一个统一的数学框架，并引入了自 refining 神经代理模型（SNS）。SNS可以作为一个独立的模型来优化其自回归输出，或作为现有神经代理的补充模型以确保长期一致性。论文在复杂动力系统的高保真长时间模拟中验证了其可行性。该方法论对于构建用于模拟化学动力学、分子动力学或光谱时间序列的“化学大模型”具有直接相关性。确保生成或模拟过程的长期一致性是此类模型可靠性的关键，本文提出的框架为解决化学模拟中的类似挑战提供了新的思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in autoregressive neural surrogate models have enabled orders-of-magnitude speedups in simulating dynamical systems. However, autoregressive models are generally prone to distribution drift: compounding errors in autoregressive rollouts that severely degrade generation quality over long time horizons. Existing work attempts to address this issue by implicitly leveraging the inherent trade-off between short-time accuracy and long-time consistency through hyperparameter tuning. In this work, we introduce a unifying mathematical framework that makes this tradeoff explicit, formalizing and generalizing hyperparameter-based strategies in existing approaches. Within this framework, we propose a robust, hyperparameter-free model implemented as a conditional diffusion model that balances short-time fidelity with long-time consistency by construction. Our model, Self-refining Neural Surrogate model (SNS), can be implemented as a standalone model that refines its own autoregressive outputs or as a complementary model to existing neural surrogates to ensure long-time consistency. We also demonstrate the numerical feasibility of SNS through high-fidelity simulations of complex dynamical systems over arbitrarily long time horizons.

</details>

---

### 38. [Procedural Generation of Algorithm Discovery Tasks in Machine Learning](https://arxiv.org/abs/2603.17863)

**基本信息**

- 🔗 arXiv: [`2603.17863`](https://arxiv.org/abs/2603.17863)
- 👥 作者: Alexander D. Goldie, Zilin Wang, Adrian Hayler 等20人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17863.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个程序化生成算法发现任务和基准的系统（DiscoGen和DiscoBench），这为开发和评估用于化学发现（可视为“化学大模型”的应用）的AI智能体提供了潜在的数据集、资源和工具范式。

**📖 中文摘要**

本文介绍了DiscoGen，一个用于机器学习中算法发现任务（例如为强化学习开发优化器或为图像分类开发损失函数）的程序化生成器。它通过少量配置参数生成数百万个不同难度和复杂度的任务，用于优化算法发现智能体。论文还提出了一个用于算法发现智能体评估的基准DiscoBench。这项工作与“化学大模型”相关，因为它提供了一个自动化和可扩展的框架来评估和优化“发现算法”的AI智能体。在化学信息学中，类似的框架可以用于生成和评估用于分子设计、反应预测或光谱解析等任务的算法/模型，从而推动“化学大模型”在自动化发现方面的进展。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automating the development of machine learning algorithms has the potential to unlock new breakthroughs. However, our ability to improve and evaluate algorithm discovery systems has thus far been limited by existing task suites. They suffer from many issues, such as: poor evaluation methodologies; data contamination; and containing saturated or very similar problems. Here, we introduce DiscoGen, a procedural generator of algorithm discovery tasks for machine learning, such as developing optimisers for reinforcement learning or loss functions for image classification. Motivated by the success of procedural generation in reinforcement learning, DiscoGen spans millions of tasks of varying difficulty and complexity from a range of machine learning fields. These tasks are specified by a small number of configuration parameters and can be used to optimise algorithm discovery agents (ADAs). We present DiscoBench, a benchmark consisting of a fixed, small subset of DiscoGen tasks for principled evaluation of ADAs. Finally, we propose a number of ambitious, impactful research directions enabled by DiscoGen, in addition to experiments demonstrating its use for prompt optimisation of an ADA. DiscoGen is released open-source at this https URL .

</details>

---

### 39. [scicode-lint: Detecting Methodology Bugs in Scientific Python Code with LLM-Generated Patterns](https://arxiv.org/abs/2603.17893)

**基本信息**

- 🔗 arXiv: [`2603.17893`](https://arxiv.org/abs/2603.17893)
- 👥 作者: Sergey V. Samsonau
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17893.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于检测科学代码中方法论错误的工具（scicode-lint），这为从事“化学大模型”和“质谱结构推理”研究的人员提供了确保其实验代码正确性和可重复性的重要资源或工具。

**📖 中文摘要**

本文介绍了scicode-lint，一个用于检测科学Python代码中方法论错误（如数据泄漏、错误的交叉验证、缺失随机种子）的框架。其架构将模式设计（使用前沿大模型）与执行（使用小型本地模型）分离，通过生成而非手动编码的模式来适应新的库版本。论文在Kaggle笔记本和已发表的科学论文上进行了评估。该工具与“化学大模型”和“质谱结构推理”高度相关，因为在这些领域的研究中，广泛使用Python进行机器学习和数据分析。确保代码没有方法论错误对于研究结果的可重复性和可靠性至关重要。scicode-lint提供了一种自动化检测此类错误的方案，可以被化学信息学和质谱分析领域的研究人员用作提高代码质量、避免错误结论的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Methodology bugs in scientific Python code produce plausible but incorrect results that traditional linters and static analysis tools cannot detect. Several research groups have built ML-specific linters, demonstrating that detection is feasible. Yet these tools share a sustainability problem: dependency on specific pylint or Python versions, limited packaging, and reliance on manual engineering for every new pattern. As AI-generated code increases the volume of scientific software, the need for automated methodology checking (such as detecting data leakage, incorrect cross-validation, and missing random seeds) grows. We present scicode-lint, whose two-tier architecture separates pattern design (frontier models at build time) from execution (small local model at runtime). Patterns are generated, not hand-coded; adapting to new library versions costs tokens, not engineering hours. On Kaggle notebooks with human-labeled ground truth, preprocessing leakage detection reaches 65% precision at 100% recall; on 38 published scientific papers applying AI/ML, precision is 62% (LLM-judged) with substantial variation across pattern categories; on a held-out paper set, precision is 54%. On controlled tests, scicode-lint achieves 97.7% accuracy across 66 patterns.

</details>

---

### 40. [Only relative ranks matter in weight-clustered large language models](https://arxiv.org/abs/2603.17917)

**基本信息**

- 🔗 arXiv: [`2603.17917`](https://arxiv.org/abs/2603.17917)
- 👥 作者: Borja Aizpurua, Sukhbinder Singh, Román Orús
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17917.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕大型语言模型（作为“化学大模型”的一种重要类型和实现技术）的权重表示、压缩和鲁棒性，其关于“相对排名重要性”的发现对理解和构建高效、鲁棒的化学领域大模型具有直接参考价值。

**📖 中文摘要**

本文研究了大型语言模型（LLMs）的权重聚类压缩。作者发现，对于LLMs的性能而言，权重的相对排名（即一个连接比另一个更强或更弱）比精确的数值大小更为关键。通过应用权重聚类（如K-means）将预训练模型的每个权重矩阵替换为少量（如16-64个）共享值，可以在不重新训练的情况下保持较强的模型精度，这为LLMs提供了一种简单的、免训练的压缩方法。该研究从“相对排名”这一新视角审视模型压缩和鲁棒性，其核心发现——模型性能对权重相对排名的敏感性——与“化学大模型”中模型架构、参数表示和压缩技术的研究主题直接相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) contain billions of parameters, yet many exact values are not essential. We show that what matters most is the relative rank of weights-whether one connection is stronger or weaker than another-rather than precise magnitudes. To reduce the number of unique weight values, we apply weight clustering to pretrained models, replacing every weight matrix with K shared values from K-means. For Llama 3.1-8B-Instruct and SmolLM2-135M, reducing each matrix to only 16-64 distinct values preserves strong accuracy without retraining, providing a simple, training-free method to compress LLMs on disk. Optionally fine-tuning only the cluster means (centroids) recovers 30-40 percent of the remaining accuracy gap at minimal cost. We then systematically randomize cluster means while keeping assignments fixed. Scrambling the relative ranks of the clusters degrades quality sharply-perplexity can increase by orders of magnitude-even when global statistics such as mean and variance are preserved. In contrast, rank-preserving randomizations cause almost no loss at mid and late layers. On the other hand, when many layers are perturbed simultaneously, progressive layer-by-layer replacement reveals that scale drift-not rank distortion-is the dominant collapse mechanism; however, an affine correction w' = aw + b with a > 0 (which preserves both rank order and overall weight distribution) can substantially delay this drift. This rank-based perspective offers a new lens on model compression and robustness.

</details>

---

### 41. [Training Diffusion Language Models for Black-Box Optimization](https://arxiv.org/abs/2603.17919)

**基本信息**

- 🔗 arXiv: [`2603.17919`](https://arxiv.org/abs/2603.17919)
- 👥 作者: Zipeng Sun, Can Chen, Ye Yuan 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17919.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是利用和调整大语言模型（特别是扩散模型）来解决科学发现中的优化问题，这直接关联到“化学大模型”在分子生成、逆向设计等任务中的应用场景和技术路径。

**📖 中文摘要**

本文研究离线黑盒优化问题，旨在从有限的设计-标签数据集中发现改进的设计。作者指出，现有的自回归大语言模型在处理设计问题时，其从左到右的生成方式难以捕捉设计问题中固有的强双向依赖关系。为此，他们提出使用扩散大语言模型来适应离线黑盒优化任务，以利用其双向建模能力。为了弥合扩散大语言模型在自然文本预训练与黑盒优化中异构信号（提示、设计、标签）之间的领域差距，论文构建了统一的提示-响应语料库，并引入了分隔符标记来显式标记字段边界以进行领域适应。此外，还提出了一个两阶段的后训练框架，使扩散大语言模型的生成与高标签设计对齐。这项工作展示了如何针对特定领域（如材料科学、DNA设计）调整和利用大语言模型（包括扩散模型）进行优化和生成，与“化学大模型”在分子设计、性质预测等任务中的应用高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study offline black-box optimization (BBO), aiming to discover improved designs from an offline dataset of designs and labels, a problem common in robotics, DNA, and materials science with limited labeled samples. While recent work applies autoregressive LLMs to BBO by formatting tasks as natural-language prompts, their left-to-right design generation struggles to capture the strong bidirectional dependencies inherent in design problems. To address this, we propose adapting diffusion LLMs to offline BBO to leverage their bidirectional modeling capabilities. However, a domain gap exists between the natural text pre-training of diffusion LLMs and the heterogeneous signals in BBO (prompts, designs, and labels). To bridge this gap, we construct a unified prompt-response corpus and introduce delimiter tokens to explicitly mark field boundaries for domain adaptation. We further propose a two-stage post-training framework to align the diffusion LLM generation with high-label designs. The first stage performs supervised fine-tuning on the unified dataset via masked-response prediction, and the second stage adopts reinforcement learning with rewards defined by label improvements. Our method achieves state-of-the-art results on Design-Bench small-data settings.

</details>

---

### 42. [Gaussian Process Regression-based Knowledge Distillation Framework for Simultaneous Prediction of Physical and Mechanical Properties of Epoxy Polymers](https://arxiv.org/abs/2603.16925)

**基本信息**

- 🔗 arXiv: [`2603.16925`](https://arxiv.org/abs/2603.16925)
- 👥 作者: Sindu B.S., Jan Hamaekers
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16925.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个机器学习框架（结合GPR和深度学习）来预测化学材料（环氧聚合物）的多种性质，这直接属于“化学大模型”在化学信息学、材料性质预测与设计中的应用领域。

**📖 中文摘要**

本文针对环氧聚合物，开发了一种基于高斯过程回归的知识蒸馏框架，用于同时预测其多种物理和机械性能。由于环氧聚合物复杂的3D分子结构、多组分特性以及缺乏高质量数据集，现有的机器学习应用受到限制。该框架使用从SMILES表示中提取的分子描述符来构建物理信息模型。个体GPR模型作为教师模型，捕捉特征与性能之间的非线性关系，而统一的神经网络学生模型则同时学习所有性能的蒸馏知识。通过将目标性能编码为输入特征，学生模型利用了跨性能相关性。该框架结合了GPR的可解释性和鲁棒性以及深度学习的可扩展性和泛化能力。比较分析表明，其预测精度优于传统机器学习模型。同时的多性能预测通过跨相关性能的信息共享进一步提高了准确性。所提出的框架能够加速设计具有定制性能的新型环氧聚合物。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Epoxy polymers are widely used due to their multifunctional properties, but machine learning (ML) applications remain limited owing to their complex 3D molecular structure, multi-component nature, and lack of curated datasets. Existing ML studies are largely restricted to simulation data, specific properties, or narrow constituent ranges. To address these limitations, we developed an informed Gaussian Process Regression-based Knowledge Distillation (GPR-KD) framework for predicting multiple physical (glass transition temperature, density) and mechanical properties (elastic modulus, tensile strength, compressive strength, flexural strength, fracture energy, adhesive strength) of thermoset epoxy polymers. The model was trained on experimental literature data covering diverse monomer classes (9 resins, 40 hardeners). Individual GPR models serve as teacher models capturing nonlinear feature-property relationships, while a unified neural network student model learns distilled knowledge across all properties simultaneously. By encoding the target property as an input feature, the student model leverages cross-property correlations. Molecular-level descriptors extracted from SMILES representations using RDKit create a physics-informed model. The framework combines GPR interpretability and robustness with deep learning scalability and generalization. Comparative analysis demonstrates superior prediction accuracy over conventional ML models. Simultaneous multi-property prediction further improves accuracy through information sharing across correlated properties. The proposed framework enables accelerated design of novel epoxy polymers with tailored properties.

</details>

---

### 43. [Machine intelligence supports the full chain of 2D dendrite synthesis](https://arxiv.org/abs/2603.16959)

**基本信息**

- 🔗 arXiv: [`2603.16959`](https://arxiv.org/abs/2603.16959)
- 👥 作者: Wenqiang Huang, Susu Fang, Xuhang Gu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.16959.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心是开发一个基于机器学习的智能框架来指导和控制材料（二维晶体）的合成，这属于“化学大模型”在实验自动化、工艺优化和逆向设计中的应用范畴。2) 论文提出的框架、策略和模型本身可作为用于材料合成优化的“工具”或“方法学”资源。

**📖 中文摘要**

本文以二维树枝状晶体的化学气相沉积生长为例，提出了一个由机器学习智能驱动的材料合成全链条支持框架。该框架涵盖了快速工艺优化、精准定制合成和综合机理分析。首先，将主动学习集成到实验工作流中，通过少量实验迭代找到生长高分支、电催化活性ReSe2树枝晶的最佳配方。其次，开发了一种基于预测精度的数据增强策略，结合树基机器学习算法，仅用少量额外实验就揭示了5个工艺变量与ReSe2树枝晶分形维数之间的非线性关系，从而指导合成各种用户定义分形维数的晶体。最后，通过整合跨尺度表征、可解释机器学习模型以及热力学和动力学领域知识，构建了一个数据-知识双驱动的机理模型，揭示了多个工艺参数对产物形态的协同贡献。这项工作展示了机器学习在改变材料合成研究范式方面的潜力，其方法论可适用于更广泛的材料合成领域，包括化学合成与表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Exemplified by the chemical vapor deposition growth of two-dimensional dendrites, which has potential applications in catalysis and presents a parameter-intensive, data-scarce and reaction process-complex model problem, we devise a machine intelligence-empowered framework for the full chain support of material synthesis, encompassing rapid process optimization, accurate customized synthesis, and comprehensive mechanism this http URL , active learning is integrated into the experimental workflow, identifying an optimal recipe for the growth of highly-branched, electrocatalytically-active ReSe2 dendrites through 60 experiments (4 iterations), which account for less than 1.3% of the numerous possible parameter this http URL , a prediction accuracy-guided data augmentation strategy is developed combined with a tree-based machine learning (ML) algorithm, unveiling a non-linear correlation between 5 process variables and fractal dimension (DF) of ReSe2 dendrites with only 9 experiment additions, which guides the synthesis of various user-defined DF. Finally, we construct a data-knowledge dual-driven mechanism model by integration of cross-scale characterizations, interpretable ML models, and domain knowledge in thermodynamics and kinetics, unraveling synergistic contributions of multiple process parameters to the product morphology. This work demonstrates the ML potential to transform the research paradigm and is adaptable to broader material synthesis.

</details>

---

### 44. [Rapid Neural Network Prediction of Linear Block Copolymer Free Energies](https://arxiv.org/abs/2603.17391)

**基本信息**

- 🔗 arXiv: [`2603.17391`](https://arxiv.org/abs/2603.17391)
- 👥 作者: Ian Chen, Alfredo Alexander-Katz
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17391.pdf)

**💡 相关性分析**

满足标准1：论文的核心是应用机器学习（神经网络）来快速、准确地预测聚合物系统的热力学性质（自由能），这属于“化学大模型”在高分子化学、计算化学和材料模拟中的典型应用，旨在替代或加速传统的计算密集型方法。

**📖 中文摘要**

本文开发了一个机器学习框架，用于根据模拟得出的能量描述符快速预测线性二嵌段共聚物系统的过量自由能。使用耗散粒子动力学模拟，构建了每个链的能量统计数据数据集，包括异质相互作用能、同质相互作用能和键合弹簧能，并训练前馈神经网络来学习这些描述符与使用分层Bennett接受比程序计算的自由能之间的关系。所得模型能够准确再现一系列链长、组成和密度下的参考自由能，包括训练中未包含的聚合物架构。在直接、粗暴的BAR估计因相空间重叠差而变得不可靠的情况下，神经网络预测仍然与参考值一致。这些结果表明，基于物理信息的机器学习模型可以作为昂贵自由能计算的有效替代品，并为加速聚合物系统的热力学分析提供了一种有前景的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Free energies are fundamental quantities governing phase behavior and thermodynamic stability in polymer systems, yet their accurate computation often requires extensive simulations and post-processing techniques such as the Bennett Acceptance Ratio (BAR). While BAR provides reliable estimates when applied between closely related thermodynamic states, evaluating free energies across large changes in interaction strength typically requires a sequence of intermediate simulations to maintain sufficient phase-space overlap, substantially increasing computational cost. In this work we develop a machine learning framework for rapidly predicting excess free energies of linear diblock copolymer systems from simulation-derived energetic descriptors. Using dissipative particle dynamics simulations of freely-jointed chain polymers, we construct a dataset of per-chain energetic statistics, including heterogeneous interaction energies, homogeneous interaction energies, and bonded spring energies, and train feed-forward neural networks to learn the relationship between these descriptors and free energies computed using a stratified BAR procedure. The resulting models accurately reproduce the reference free energies across a range of chain lengths, compositions, and densities, including polymer architectures held out from training. In regimes where direct, brute-force BAR estimates become unreliable due to poor phase-space overlap, the neural network predictions remain consistent with the reference values. These results demonstrate that physically informed machine learning models can serve as efficient surrogates for expensive free-energy calculations and provide a promising approach for accelerating thermodynamic analysis of polymer systems.

</details>

---

### 45. [On the number of inequivalent linearized Reed-Solomon codes](https://arxiv.org/abs/2603.17636)

**基本信息**

- 🔗 arXiv: [`2603.17636`](https://arxiv.org/abs/2603.17636)
- 👥 作者: Jonathan Mannaert, Marta Messia, Ferdinando Zullo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17636.pdf)

**💡 相关性分析**

不相关。论文的核心是编码理论中的等价性问题和组合计数，属于纯数学/信息论领域。其内容（线性化Reed-Solomon码、和秩度量、子空间系统）与指定的重点关注主题（化学大模型、质谱结构推理）没有直接或间接的关联。不满足任何一条相关性判断标准。

**📖 中文摘要**

本文研究线性化Reed-Solomon (LRS) 码的等价性问题，并确定了该码族中不等价码的数量。虽然论文本身不直接涉及化学信息学或质谱分析，但其核心是关于最大和秩距离 (MSRD) 码的数学理论研究。LRS码是Reed-Solomon码和Gabidulin码的推广。论文利用和秩度量码与子空间系统之间的对应关系，分析了Gabidulin系统的稳定子，并给出了LRS码等价的充要条件。研究结果推导出了不等价线性化Reed-Solomon码数量的计算公式，并通过具体示例进行了说明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Linearized Reed-Solomon (LRS) codes form an important family of maximum sum-rank distance (MSRD) codes that generalize both Reed--Solomon codes and Gabidulin codes. In this paper we study the equivalence problem for LRS codes and determine the number of inequivalent codes within this family. Using the correspondence between sum-rank metric codes and systems of $\mathbb{F}_q$-subspaces, we analyze the stabilizer of the Gabidulin system and derive a characterization of equivalence between LRS codes. In particular, we prove that two LRS codes are equivalent if and only if the sets of norms that define the codes coincide up to multiplication by an element of $\mathbb{F}_q^\ast$. This description allows us to reduce the classification problem to the action of $\mathbb{F}_q^\ast$ on subsets of $\mathbb{F}_q^\ast$. As a consequence, we derive formulas for the number of inequivalent linearized Reed-Solomon codes and illustrate the results with explicit examples.

</details>

---

### 46. [The Convergence Frontier: Integrating Machine Learning and High Performance Quantum Computing for Next-Generation Drug Discovery](https://arxiv.org/abs/2603.17790)

**基本信息**

- 🔗 arXiv: [`2603.17790`](https://arxiv.org/abs/2603.17790)
- 👥 作者: Narjes Ansari, César Feniou, Nicolaï Gouraud 等16人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.17790.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的主要研究内容直接围绕“化学大模型”在药物发现中的应用。它深入讨论了机器学习（特别是基础模型）与量子计算相结合，以实现量子精度的化学模拟和加速药物发现流程，这完全符合“化学大模型”这一主题。

**📖 中文摘要**

本文探讨了高性能计算 (HPC)、机器学习 (ML) 和量子计算 (QC) 的融合如何解决药物发现中的计算瓶颈。论文指出，虽然像 FeNNix-Bio1 这样的机器学习基础模型能够实现量子精度的模拟，但它们仍然受限于经典数据生成的固有局限。作者详细阐述了利用混合 QPU-GPU 架构的高性能量子计算 (HPQC) 将如何成为量子化学数据的终极加速器。通过利用希尔伯特空间映射，这些系统可以在绕过经典近似启发式方法的同时实现真正的化学精度。论文展示了这种三方融合如何优化从初始系统准备到 ML 驱动的高保真模拟的药物发现流程，并将量子增强采样定位为超越 GPU 的、用于建模反应性细胞系统和开创下一代材料的前沿。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Integrating quantum mechanics into drug discovery marks a decisive shift from empirical trial-and-error toward quantitative precision. However, the prohibitive cost of ab initio molecular dynamics has historically forced a compromise between chemical accuracy and computational scalability. This paper identifies the convergence of High-Performance Computing (HPC), Machine Learning (ML), and Quantum Computing (QC) as the definitive solution to this bottleneck. While ML foundation models, such as FeNNix-Bio1, enable quantum-accurate simulations, they remain tethered to the inherent limits of classical data generation. We detail how High-Performance Quantum Computing (HPQC), utilizing hybrid QPU-GPU architectures, will serve as the ultimate accelerator for quantum chemistry data. By leveraging Hilbert space mapping, these systems can achieve true chemical accuracy while bypassing the heuristics of classical approximations. We show how this tripartite convergence optimizes the drug discovery pipeline, spanning from initial system preparation to ML-driven, high-fidelity simulations. Finally, we position quantum-enhanced sampling as the beyond GPU frontier for modeling reactive cellular systems and pioneering next-generation materials.

</details>

---

### 47. [Byte-token Enhanced Language Models for Temporal Point Processes Analysis](https://arxiv.org/abs/2502.07139)

**基本信息**

- 🔗 arXiv: [`2502.07139`](https://arxiv.org/abs/2502.07139)
- 👥 作者: Quyu Kong, Yixuan Zhang, Yang Liu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2502.07139.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文提出了一个名为 Language-TPP 的“大语言模型”框架，专门用于时间点过程建模。虽然应用场景是网络事件序列，但其核心是开发一个集成 LLMs 的新型建模框架，这直接与“化学大模型”主题中“大模型”的构建与应用技术相关。论文展示了如何将连续时间信息编码并融入 LLM，这种模型架构和方法论上的创新对于构建处理复杂序列数据（如质谱或分子序列）的化学大模型具有参考价值。

**📖 中文摘要**

本文介绍了 Language-TPP，一个将时间点过程 (TPPs) 与大语言模型 (LLMs) 相集成的统一框架，用于增强网络事件序列建模。其核心创新是一种新颖的时间编码机制，将连续时间间隔转换为专门的字节令牌，使其能够直接与标准语言模型架构集成以进行 TPP 建模，而无需针对 TPP 进行特定修改。该方法使 Language-TPP 在多个 TPP 基准测试（包括事件时间预测和类型预测）上实现了最先进的性能，数据集涵盖电子商务评论、社交媒体和在线问答平台等真实网络数据。更重要的是，该框架解锁了 TPP 研究的新能力：结合时间信息提高了生成事件描述的质量，并产生了更一致的情感分布。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Temporal Point Processes (TPPs) have been widely used for modeling event sequences on the Web, such as user reviews, social media posts, and online transactions. However, traditional TPP models often struggle to effectively incorporate the rich textual descriptions that accompany these events, while Large Language Models (LLMs), despite their remarkable text processing capabilities, lack mechanisms for handling the temporal dynamics inherent in Web-based event sequences. To bridge this gap, we introduce Language-TPP, a unified framework that seamlessly integrates TPPs with LLMs for enhanced Web event sequence modeling. Our key innovation is a novel temporal encoding mechanism that converts continuous time intervals into specialized byte-tokens, enabling direct integration with standard language model architectures for TPP modeling without requiring TPP-specific modifications. This approach allows Language-TPP to achieve state-of-the-art performance across multiple TPP benchmarks, including event time prediction and type prediction, on real-world Web datasets spanning e-commerce reviews, social media and online Q&A platforms. More importantly, we demonstrate that our unified framework unlocks new capabilities for TPP research: incorporating temporal information improves the quality of generated event descriptions, as evidenced by enhanced ROUGE-L scores, and better aligned sentiment distributions. Through comprehensive experiments, including qualitative analysis of learned distributions and scalability evaluations on long sequences, we show that Language-TPP effectively captures both temporal dynamics and textual patterns in Web user behavior, with important implications for content generation, user behavior understanding, and Web platform applications. Code is available at this https URL .

</details>

---

### 48. [CMADiff: Cross-Modal Aligned Diffusion for Controllable Protein Generation](https://arxiv.org/abs/2503.21450)

**基本信息**

- 🔗 arXiv: [`2503.21450`](https://arxiv.org/abs/2503.21450)
- 👥 作者: Changjian Zhou, Yuexi Qiu, Jia Song 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2503.21450.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的核心研究内容是开发一个名为 CMADiff 的生成模型，用于“可控蛋白质生成”。该模型结合了扩散模型和条件生成技术，属于“化学大模型”在生物分子生成领域的直接应用。它利用文本描述（一种高级语义）来指导蛋白质序列的生成，这正是化学/生物信息学中大模型研究的前沿方向。

**📖 中文摘要**

本文提出了 CMADiff，一个通过潜在扩散过程将蛋白质序列的理化性质与基于文本的描述对齐，从而实现可控蛋白质生成的新框架。具体来说，CMADiff 采用条件变分自编码器 (CVAE) 将理化特征作为条件输入，形成一个捕捉生物学特征的鲁棒潜在空间。在此潜在空间中，应用条件扩散过程，该过程由 BioAligner（一个基于对比学习的模块）引导，该模块将文本描述与蛋白质特征对齐，从而实现对蛋白质序列生成的文本驱动控制。在包括 AlphaFold3 在内的一系列评估验证下，实验结果表明 CMADiff 在蛋白质序列生成基准测试中表现优异，并显示出强大的未来应用潜力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI-assisted protein design has emerged as a critical tool for advancing biotechnology, as deep generative models have demonstrated their reliability in this domain. However, most existing models primarily utilize protein sequence or structural data for training, neglecting the physicochemical properties of this http URL , they are deficient to control the generation of proteins in intuitive conditions. To address these limitations,we propose CMADiff here, a novel framework that enables controllable protein generation by aligning the physicochemical properties of protein sequences with text-based descriptions through a latent diffusion process. Specifically, CMADiff employs a Conditional Variational Autoencoder (CVAE) to integrate physicochemical features as conditional input, forming a robust latent space that captures biological traits. In this latent space, we apply a conditional diffusion process, which is guided by BioAligner, a contrastive learning-based module that aligns text descriptions with protein features, enabling text-driven control over protein sequence generation. Validated by a series of evaluations including AlphaFold3, the experimental results indicate that CMADiff outperforms protein sequence generation benchmarks and holds strong potential for future applications. The implementation and code are available at this https URL .

</details>

---

### 49. [TwinTrack: Bridging Vision and Contact Physics for Real-Time Tracking of Unknown Objects in Contact-Rich Scenes](https://arxiv.org/abs/2505.22882)

**基本信息**

- 🔗 arXiv: [`2505.22882`](https://arxiv.org/abs/2505.22882)
- 👥 作者: Wen Yang, Zhixian Xie, Yiting Wang 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.22882.pdf)

**💡 相关性分析**

不相关。论文的核心是医学图像分割的自监督学习框架，并集成了 SAM 模型进行后处理和 3D 传播。虽然涉及“大模型”(SAM)，但其应用领域是医学影像分析，与指定的“化学信息学”和“质谱分析”领域没有直接关联。研究目标和数据模态（CT图像）均不匹配关注主题。

**📖 中文摘要**

本文提出 PolyCL，一种用于医学图像分割的新型自监督对比学习框架。该框架无需任何像素级标注或不合理的数据增强，通过一个创新的代理任务，以任务相关的方式学习并迁移对分割有用的上下文感知判别特征。此外，论文以两种新颖的方式将 Segment Anything Model (SAM) 集成到框架中：1) 作为后处理细化模块，利用从粗略输出导出的边界框提示来改进预测掩码的准确性；2) 作为通过 SAM 2 的传播机制，从单个注释的 2D 切片生成体积分割。在三个公共 CT 数据集上的实验评估表明，PolyCL 在低数据和跨域场景中均优于全监督和自监督基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Real-time tracking of previously unseen, highly dynamic objects in contact-rich scenes, such as during dexterous in-hand manipulation, remains a major challenge. Pure vision-based approaches often fail under heavy occlusions due to frequent contact interactions and motion blur caused by abrupt impacts. We propose Twintrack, a physics-aware perception system that enables robust, real-time 6-DoF pose tracking of unknown dynamic objects in contact-rich scenes by leveraging contact physics cues. At its core, Twintrack integrates Real2Sim and Sim2Real. Real2Sim combines vision and contact physics to jointly estimate object geometry and physical properties: an initial reconstruction is obtained from vision, then refined by learning a geometry residual and simultaneously estimating physical parameters (e.g., mass, inertia, and friction) based on contact dynamics consistency. Sim2Real achieves robust pose estimation by adaptively fusing a visual tracker with predictions from the updated contact dynamics. Twintrack is implemented on a GPU-accelerated, customized MJX engine to guarantee real-time performance. We evaluate our method on two contact-rich scenarios: object falling with environmental contacts and multi-fingered in-hand manipulation. Results show that, compared to baselines, Twintrack delivers significantly more robust, accurate, and real-time tracking in these challenging settings, with tracking speeds above 20 Hz. Project page: this https URL

</details>

---

### 50. [HyperMotionX: The Dataset and Benchmark with DiT-Based Pose-Guided Human Image Animation of Complex Motions](https://arxiv.org/abs/2505.22977)

**基本信息**

- 🔗 arXiv: [`2505.22977`](https://arxiv.org/abs/2505.22977)
- 👥 作者: Shuolin Xu, Siming Zheng, Ziyi Wang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.22977.pdf)

**💡 相关性分析**

不相关。论文的核心是计算机视觉和图形学领域的人体图像动画生成，专注于扩散变换器 (DiT) 模型在视频生成任务中的应用。虽然涉及生成模型，但其主题（人体动画、姿势引导）和应用领域与化学信息学、质谱分析或化学大模型无关。

**📖 中文摘要**

本文针对基于姿势引导的人体图像动画任务，提出了一个简洁而强大的基于 DiT 的生成基线模型，并设计了空间低频增强 RoPE 模块。此外，引入了 Open-HyperMotionX 数据集和 HyperMotionX 基准，用于评估和改进复杂人体运动条件下的姿势引导人体图像动画模型。该方法显著提高了高动态人体运动序列中的结构稳定性和外观一致性。大量实验证明了所提出数据集和方法在提升复杂人体运动图像动画生成质量方面的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in diffusion models have significantly improved conditional video generation, particularly in the pose-guided human image animation task. Although existing methods are capable of generating high-fidelity and time-consistent animation sequences in regular motions and static scenes. However there are still obvious limitations when facing complex human body motions that contain highly dynamic, non-standard motions, and the lack of a high-quality benchmark for evaluation of complex human motion animations. To address this challenge, we propose a concise yet powerful DiT-based human animation generation baseline and design spatial low-frequency enhanced RoPE, a novel module that selectively enhances low-frequency spatial feature modeling by introducing learnable frequency scaling. Furthermore, we introduce the Open-HyperMotionX Dataset and HyperMotionX Bench, which provide high-quality human pose annotations and curated video clips for evaluating and improving pose-guided human image animation models under complex human motion conditions. Our method significantly improves structural stability and appearance consistency in highly dynamic human motion sequences. Extensive experiments demonstrate the effectiveness of our dataset and proposed approach in advancing the generation quality of complex human motion image animations. The codes, model weights, and dataset have been made publicly available at this https URL

</details>

---

### 51. [Enhancing Critical Thinking in Generative AI Search with Metacognitive Prompts](https://arxiv.org/abs/2505.24014)

**基本信息**

- 🔗 arXiv: [`2505.24014`](https://arxiv.org/abs/2505.24014)
- 👥 作者: Anjali Singh, Zhitong Guan, Soo Young Rieh
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.24014.pdf)

**💡 相关性分析**

不相关。论文研究的是人机交互和认知科学领域的问题，即如何通过设计提示来改善用户在使用生成式AI搜索工具时的批判性思维和元认知参与。其核心是用户体验和交互设计，而非AI模型本身在化学或质谱领域的构建、应用或数据资源提供。与指定主题无关。

**📖 中文摘要**

本研究探讨了在基于生成式 AI (GenAI) 的搜索过程中，元认知提示（旨在鼓励用户暂停、反思、评估自己的理解并考虑多种视角）是否能够支持批判性思维。通过一项用户研究 (N=40)，发现这些提示能导致更积极的参与，促使学生探索更广泛的主题并通过后续查询进行更深入的探究。学生报告称，这些提示特别有助于考虑被忽视的视角、促进对 AI 响应的评估以及识别关键要点。此外，提示的有效性受到学生元认知灵活性的影响。研究结果凸显了元认知提示在培养批判性思维方面的潜力，并为在人类-AI 交互中设计和实施元认知支持提供了见解。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The growing use of Generative AI (GenAI) conversational search tools has raised concerns about their effects on people's metacognitive engagement, critical thinking, and learning. As people increasingly rely on GenAI to perform tasks such as analyzing and applying information, they may become less actively engaged in thinking and learning. This study examines whether metacognitive prompts - designed to encourage people to pause, reflect, assess their understanding, and consider multiple perspectives - can support critical thinking during GenAI-based search. We conducted a user study (N=40) with university students to investigate the impact of metacognitive prompts on their thought processes and search behaviors while searching with a GenAI tool. We found that these prompts led to more active engagement, prompting students to explore a broader range of topics and engage in deeper inquiry through follow-up queries. Students reported that the prompts were especially helpful for considering overlooked perspectives, promoting evaluation of AI responses, and identifying key takeaways. Additionally, the effectiveness of these prompts was influenced by students' metacognitive flexibility. Our findings highlight the potential of metacognitive prompts to foster critical thinking and provide insights for designing and implementing metacognitive support in human-AI interactions.

</details>

---

### 52. [An Introduction to Flow Matching and Diffusion Models](https://arxiv.org/abs/2506.02070)

**基本信息**

- 🔗 arXiv: [`2506.02070`](https://arxiv.org/abs/2506.02070)
- 👥 作者: Peter Holderrieth, Ezra Erives
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.02070.pdf)

**💡 相关性分析**

满足标准3：综述展望相关。论文是一篇关于扩散和流匹配生成模型的教程/综述。虽然不专门针对化学领域，但它全面介绍了这些已成为生成式AI最先进技术的模型的理论和实践。鉴于“化学大模型”很可能采用扩散模型等生成架构（例如用于分子生成或质谱解析），这篇教程提供了重要的基础知识和相关讨论，对于理解和构建化学领域的生成大模型具有重要参考价值。

**📖 中文摘要**

本教程对扩散和基于流的生成模型进行了自成体系的介绍。它从基本原理出发，系统性地介绍了常微分方程和随机微分方程的必要数学背景，并推导了流匹配和去噪扩散模型的核心算法。随后，提供了构建图像和视频生成器的分步指南，包括训练方法、引导和架构设计。本课程非常适合希望从原理上理解生成式AI理论和实践的机器学习研究人员。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Diffusion and flow-based models have become the state of the art for generative AI across a wide range of data modalities, including images, videos, shapes, molecules, music, and more. This tutorial provides a self-contained introduction to diffusion and flow-based generative models from first principles. We systematically develop the necessary mathematical background in ordinary and stochastic differential equations and derive the core algorithms of flow matching and denoising diffusion models. We then provide a step-by-step guide to building image and video generators, including training methods, guidance, and architectural design. This course is ideal for machine learning researchers who want to develop a principled understanding of the theory and practice of generative AI.

</details>

---

### 53. [Mechanistic Interpretability of Diffusion Models: Circuit-Level Analysis and Causal Validation](https://arxiv.org/abs/2506.17237)

**基本信息**

- 🔗 arXiv: [`2506.17237`](https://arxiv.org/abs/2506.17237)
- 👥 作者: Dip Roy
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.17237.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文的核心研究内容是对“扩散模型”进行机制可解释性分析。扩散模型是当前最强大的生成模型之一，是构建“化学大模型”（尤其是生成式模型，如用于分子设计或质谱生成）的关键技术基石。论文深入探究了扩散模型内部的工作机制和计算电路，这种对生成模型底层原理的理解对于设计和优化应用于化学领域的扩散模型具有直接的相关性和重要性。

**📖 中文摘要**

本文对扩散模型进行了定量的电路级分析，建立了支撑图像生成过程的计算路径和机制原理。通过对2000张合成图像和2000张CelebA人脸图像进行系统干预实验，发现了扩散架构在处理合成数据与自然数据分布时的基本算法差异。研究表明，真实世界的人脸处理需要具有可测量更高计算复杂度的电路，并在去噪时间步上表现出不同的注意力专业化模式。我们识别出八种功能不同的注意力机制，显示出专门的计算角色：边缘检测、纹理分析和语义理解。干预分析证明了关键的计算瓶颈，有针对性的消融会导致25.6%到128.3%的性能下降，为已识别的电路功能提供了因果证据。这些发现通过机制干预策略为算法理解和控制生成模型行为奠定了定量基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present a quantitative circuit-level analysis of diffusion models, establishing computational pathways and mechanistic principles underlying image generation processes. Through systematic intervention experiments across 2,000 synthetic and 2,000 CelebA facial images, we discover fundamental algorithmic differences in how diffusion architectures process synthetic versus naturalistic data distributions. Our investigation reveals that real-world face processing requires circuits with measurably higher computational complexity (complexity ratio = 1.084 plus/minus 0.008, p < 0.001), exhibiting distinct attention specialization patterns with entropy divergence ranging from 0.015 to 0.166 across denoising timesteps. We identify eight functionally distinct attention mechanisms showing specialized computational roles: edge detection (entropy = 3.18 plus/minus 0.12), texture analysis (entropy = 4.16 plus/minus 0.08), and semantic understanding (entropy = 2.67 plus/minus 0.15). Intervention analysis demonstrates critical computational bottlenecks where targeted ablations produce 25.6% to 128.3% performance degradation, providing causal evidence for identified circuit functions. These findings establish quantitative foundations for algorithmic understanding and control of generative model behavior through mechanistic intervention strategies.

</details>

---

### 54. [MLlm-DR: Towards Explainable Depression Recognition with MultiModal Large Language Models](https://arxiv.org/abs/2507.05591)

**基本信息**

- 🔗 arXiv: [`2507.05591`](https://arxiv.org/abs/2507.05591)
- 👥 作者: Wei Zhang, Juan Chen, En Zhu 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.05591.pdf)

**💡 相关性分析**

满足标准1：核心主题相关。论文提出了一个名为 MLlm-DR 的“多模态大语言模型”，用于可解释的抑郁症识别。虽然应用领域是心理健康，但其核心是构建和微调一个专门用于处理多模态（音频、视觉）数据并生成解释性输出的大语言模型。这项工作直接涉及“大模型”的架构设计、微调和应用，属于大模型技术在特定科学领域（此处是医学）的应用实例。其方法论（多模态融合、模型微调、可解释性生成）对于构建应用于化学或质谱领域的类似大模型具有参考价值。

**📖 中文摘要**

本文提出了一种新颖的多模态大语言模型 (MLlm-DR)，该模型能够理解多模态信息输入并支持可解释的抑郁症诊断。MLlm-DR 集成了一个较小的 LLM 和一个轻量级查询模块 (LQ-former)。具体来说，较小的 LLM 被设计用于生成抑郁分数和相应的评估依据。为了在保持实用性的同时增强其针对领域特定任务的逻辑推理能力，我们构建了一个强大的训练数据集对其进行微调。同时，LQ-former 从语音和视觉数据中捕获与抑郁相关的特征，帮助模型处理多模态信息，以实现全面的抑郁症诊断。我们的方法在两个基于访谈的基准数据集 CMDC 和 E-DAIC-WOZ 上取得了最先进的结果，证明了其有效性和优越性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated depression diagnosis aims to analyze multimodal information from interview videos to predict participants' depression scores. Previous studies often lack clear explanations of how these scores were determined, limiting their adoption in clinical practice. While the advent of LLMs provides a possible pathway for explainable depression diagnosis, current LLMs capable of processing multimodal data lack training on interview data, resulting in poor diagnostic performance when used directly. In this paper, we propose a novel multimodal large language model (MLlm-DR) that can understand multimodal information inputs and supports explainable depression diagnosis. MLlm-DR integrates a smaller LLMs and a lightweight query module (LQ-former). Specifically, the smaller LLMs is designed to generate depression scores and corresponding evaluation rationales. To enhance its logical reasoning for domain-specific tasks while maintaining practicality, we constructed a robust training dataset to fine-tune it. Meanwhile, the LQ-former captures depression-related features from speech and visual data, aiding the model's ability to process multimodal information, to achieve comprehensive depression diagnosis. Our approach achieves state-of-the-art results on two interview-based benchmark datasets, CMDC and E-DAIC-WOZ, demonstrating its effectiveness and superiority.

</details>

---

### 55. [Fast weight programming and linear transformers: from machine learning to neurobiology](https://arxiv.org/abs/2508.08435)

**基本信息**

- 🔗 arXiv: [`2508.08435`](https://arxiv.org/abs/2508.08435)
- 👥 作者: Kazuki Irie, Samuel J. Gershman
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.08435.pdf)

**💡 相关性分析**

满足标准3：论文是一篇关于快速权重编程器和Transformer等架构的综述，其中对Transformer的讨论与构建和理解“化学大模型”的核心架构直接相关。

**📖 中文摘要**

这篇论文是一篇关于快速权重编程器（Fast Weight Programmers, FWPs）的入门综述。FWPs是一类使用二维矩阵形式隐藏状态的循环神经网络，其“快速权重”会随时间根据输入动态变化，充当短期记忆存储。论文回顾了FWPs的技术基础、计算特性，并探讨了它们与Transformer和状态空间模型的联系。虽然论文主要聚焦于机器学习架构，但其对Transformer等现代序列建模架构的深入讨论，为理解“化学大模型”（尤其是基于Transformer架构的模型）的设计原理和计算范式提供了重要的理论基础和背景知识。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in artificial neural networks for machine learning, and language modeling in particular, have established a family of recurrent neural network (RNN) architectures that, unlike conventional RNNs with vector-form hidden states, use two-dimensional (2D) matrix-form hidden states. Such 2D-state RNNs, known as Fast Weight Programmers (FWPs), can be interpreted as a neural network whose synaptic weights (called fast weights) dynamically change over time as a function of input observations, and serve as short-term memory storage; corresponding synaptic weight modifications are controlled or programmed by another network (the programmer) whose parameters are trained (e.g., by gradient descent). In this Primer, we review the technical foundations of FWPs, their computational characteristics, and their connections to transformers and state space models. We also discuss connections between FWPs and models of synaptic plasticity in the brain, suggesting a convergence of natural and artificial intelligence.

</details>

---

### 56. [Functional Information Decomposition: A First-Principles Approach to Analyzing Functional Relationships](https://arxiv.org/abs/2509.18522)

**基本信息**

- 🔗 arXiv: [`2509.18522`](https://arxiv.org/abs/2509.18522)
- 👥 作者: Clifford Bohm, Vincent R. Ragusa, Arend Hintze 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.18522.pdf)

**💡 相关性分析**

满足标准1：论文提出的功能信息分解（FID）框架，其核心研究内容围绕从系统输入-输出映射中分解和解释多变量交互，这一方法论与构建能够进行复杂推理（如质谱结构推理）的化学大模型高度相关。

**📖 中文摘要**

本文提出了功能信息分解（Functional Information Decomposition, FID），这是一个用于分析复杂系统中多变量交互的计算和理论框架。FID的核心创新在于，它基于系统完整的输入-输出映射来定义信息组件，从而将系统的内在功能逻辑与有限的观测数据带来的统计伪影分离开来。当映射完全指定时，FID可以将系统行为唯一地分解为独立和协同的贡献。在部分观测的情况下，FID通过采样兼容函数来刻画所有一致分解的空间，使推理的局限性变得明确。论文展示了FID在典型逻辑函数、康威生命游戏以及基于基因表达的癌症药物反应预测等跨学科问题上的应用。该框架为分析多变量依赖关系提供了原则性基础，其思想和方法论（如从数据中推断功能关系、分解复杂交互）对于构建能够理解化学结构-性质关系或从质谱数据中推理分子结构的“化学大模型”具有重要的启发意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A central challenge in analyzing multivariate interactions within complex systems is to decompose how multiple inputs jointly determine an output. Existing approaches generally operate on observed probability distributions and can conflate a system's intrinsic functional logic with statistical artifacts of limited data. As a result, distinct systems can yield identical observations, rendering information decomposition fundamentally underdetermined and obscuring true higher-order interactions. We introduce Functional Information Decomposition (FID), both a computational and theoretical framework, which defines informational components with respect to a system's complete input-output mapping, thereby addressing a core cross-scale inference problem: determining how information carried by individual components combines to shape system-level behavior. When the mapping is fully specified, FID provides a unique decomposition into independent and synergistic contributions. Crucially, given only partial observations, FID characterizes the entire space of consistent decompositions by sampling compatible functions, making inferential limits explicit. A complementary geometric perspective clarifies the structural origin of informational components. We demonstrate FID's interdisciplinary utility on canonical logical functions, Conway's Game of Life, and gene-expression-based prediction of cancer drug response, and provide an open-source implementation. By separating functional architecture from observational distribution, FID offers a principled foundation for analyzing multivariate dependence in both fully and partially observed complex systems.

</details>

---

### 57. [Tree Search for LLM Agent Reinforcement Learning](https://arxiv.org/abs/2509.21240)

**基本信息**

- 🔗 arXiv: [`2509.21240`](https://arxiv.org/abs/2509.21240)
- 👥 作者: Yuxiang Ji, Ziyu Ma, Yong Wang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2509.21240.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于树搜索的强化学习方法，旨在解决复杂、多步任务中的监督稀疏问题，其“过程监督”和“偏好学习”的思想可直接应用于训练进行多步、可解释性质谱结构推理的化学大模型或智能体。

**📖 中文摘要**

本文研究了用于大语言模型智能体强化学习的树搜索方法。作者提出了基于树搜索的分组智能体相对策略优化方法，以解决长周期、多轮次智能体任务中因结果奖励稀疏而导致的监督信号不足问题。树结构轨迹允许构建逐步的过程监督信号。理论分析表明，组内相对策略优化的目标等价于逐步直接偏好学习。论文在11个数据集和3类问答任务上进行了实验。虽然论文背景是通用LLM智能体，但其核心方法——利用树搜索结构生成更丰富的训练信号（包括过程监督），以及将强化学习与偏好学习联系起来——为训练用于复杂推理任务（如质谱解析）的化学领域大模型或智能体提供了有潜力的技术思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in reinforcement learning (RL) have significantly enhanced the agentic capabilities of large language models (LLMs). In long-term and multi-turn agent tasks, existing approaches driven solely by outcome rewards often suffer from the problem of sparse supervision. To address the challenge, we propose Tree-based Group Relative Policy Optimization (Tree-GRPO), a grouped agent RL method based on tree search, where each tree node represents the complete agent interaction step. By sharing common prefixes, the tree search sampling increases the number of rollouts achievable within a fixed budget of tokens or tool calls. Moreover, we find that the tree-structured trajectory naturally allows the construction of step-wise process supervised signals even using only the outcome reward. Based on this, Tree-GRPO estimates the grouped relative advantages both on intra-tree and inter-tree levels. Through theoretical analysis, we demonstrate that the objective of intra-tree level group relative policy optimization is equivalent to that of step-level direct preference learning. Experiments across 11 datasets and 3 types of QA tasks demonstrate the superiority of the proposed tree-based RL over the chain-based RL method.

</details>

---

### 58. [Semantics-Aligned, Curriculum-Driven, and Reasoning-Enhanced Vulnerability Repair Framework](https://arxiv.org/abs/2510.01002)

**基本信息**

- 🔗 arXiv: [`2510.01002`](https://arxiv.org/abs/2510.01002)
- 👥 作者: Chengran Yang, Ting Zhang, Jinfeng Jiang 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01002.pdf)

**💡 相关性分析**

满足标准1：论文提出的“先推理后编辑”范式、语义对齐的强化学习以及课程学习框架，其核心是提升模型对复杂结构化问题（代码）的深度理解和推理能力。这些方法可以直接迁移并应用于训练能够进行分子结构解析、反应预测等复杂推理的“化学大模型”。

**📖 中文摘要**

本文提出了SeCuRepair框架，一个用于自动化漏洞修复的语义对齐、课程驱动和推理增强框架。其核心采用“先推理后编辑”的范式，要求模型在生成补丁前，明确阐述为何以及如何修复漏洞。这种显式的推理机制强制模型真正理解修复逻辑，而非仅仅记忆表面的词汇模式。此外，框架采用了语义感知的强化学习，根据补丁与标准补丁在句法和语义上的对齐程度给予奖励，而非简单的词汇重叠。配合难度感知的课程学习，模型从简单修复逐步过渡到复杂的多块协同编辑。该框架在漏洞修复任务上取得了显著性能提升。论文的核心贡献——通过显式推理和语义对齐来增强模型对复杂、结构化问题（代码）的理解和生成能力——与“化学大模型”需要处理分子结构、反应机理等复杂结构化信息的挑战高度相似，其方法论对构建具有深度推理能力的化学模型具有重要参考价值。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current learning-based Automated Vulnerability Repair (AVR) approaches, while promising, often fail to generalize effectively in real-world scenarios. Our diagnostic analysis reveals three fundamental weaknesses in state-of-the-art AVR approaches: (1) limited cross-repository generalization, with performance drops on unseen codebases; (2) inability to capture long-range dependencies, causing a performance degradation on complex, multi-hunk repairs; and (3) over-reliance on superficial lexical patterns, leading to significant performance drops on vulnerabilities with minor syntactic variations like variable renaming. To address these limitations, we propose SeCuRepair, a semantics-aligned, curriculum-driven, and reasoning-enhanced framework for vulnerability repair. At its core, SeCuRepair adopts a reason-then-edit paradigm, requiring the model to articulate why and how a vulnerability should be fixed before generating the patch. This explicit reasoning enforces a genuine understanding of repair logic rather than superficial memorization of lexical patterns. SeCuRepair also moves beyond traditional supervised fine-tuning and employs semantics-aware reinforcement learning, rewarding patches for their syntactic and semantic alignment with the oracle patch rather than mere token overlap. Complementing this, a difficulty-aware curriculum progressively trains the model, starting with simple fixes and advancing to complex, multi-hunk coordinated edits. We evaluate SeCuRepair on strict, repository-level splits of BigVul and newly crafted PrimeVul_AVR datasets. SeCuRepair significantly outperforms all baselines, surpassing the best-performing baselines by 34.52% on BigVul and 31.52% on PrimeVul\textsubscript{AVR} in terms of CodeBLEU, respectively. Comprehensive ablation studies further confirm that each component of our framework contributes to its final performance.

</details>

---

### 59. [IoDResearch: Deep Research on Private Heterogeneous Data via the Internet of Data](https://arxiv.org/abs/2510.01553)

**基本信息**

- 🔗 arXiv: [`2510.01553`](https://arxiv.org/abs/2510.01553)
- 👥 作者: Zhuofan Shi, Zijie Guo, Xinjian Ma 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.01553.pdf)

**💡 相关性分析**

满足标准2：论文提出的IoDResearch框架核心是构建一个用于高效组织、检索和利用异构私有数据（如科学数据）的系统。这为“化学信息学”和“质谱分析”领域管理、整合和挖掘化学数据集、质谱库等资源提供了创新的工具和架构参考。

**📖 中文摘要**

本文提出了IoDResearch，一个以私有数据为中心的深度研究框架，实现了数据互联网范式。该框架将异构资源封装为符合FAIR原则的数字对象，并将其进一步细化为原子知识单元和知识图谱，形成一个用于多粒度检索的异构图索引。在此基础上，一个多智能体系统支持可靠的问答和结构化的科研报告生成。作者还建立了IoD深度研究基准，以系统评估数据表示和深度研究能力。实验表明，IoDResearch在检索、问答和报告撰写任务上 consistently 优于代表性的RAG和深度研究基线。该工作展示了在数据互联网范式下以私有数据为中心的深度研究的可行性。对于“化学信息学”和“质谱分析”领域，该框架为解决如何有效组织、检索和利用海量、异构的化学数据（如质谱数据库、分子结构库、文献）提供了创新的系统架构思路，其多智能体系统也可用于构建化学领域的专业问答和报告生成工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid growth of multi-source, heterogeneous, and multimodal scientific data has increasingly exposed the limitations of traditional data management. Most existing DeepResearch (DR) efforts focus primarily on web search while overlooking local private data. Consequently, these frameworks exhibit low retrieval efficiency for private data and fail to comply with the FAIR principles, ultimately resulting in inefficiency and limited reusability. To this end, we propose IoDResearch (Internet of Data Research), a private data-centric Deep Research framework that operationalizes the Internet of Data paradigm. IoDResearch encapsulates heterogeneous resources as FAIR-compliant digital objects, and further refines them into atomic knowledge units and knowledge graphs, forming a heterogeneous graph index for multi-granularity retrieval. On top of this representation, a multi-agent system supports both reliable question answering and structured scientific report generation. Furthermore, we establish the IoD DeepResearch Benchmark to systematically evaluate both data representation and Deep Research capabilities in IoD scenarios. Experimental results on retrieval, QA, and report-writing tasks show that IoDResearch consistently surpasses representative RAG and Deep Research baselines. Overall, IoDResearch demonstrates the feasibility of private-data-centric Deep Research under the IoD paradigm, paving the way toward more trustworthy, reusable, and automated scientific discovery.

</details>

---

### 60. [Improving IR-based Bug Localization with Semantics-Driven Query Reduction](https://arxiv.org/abs/2510.04468)

**基本信息**

- 🔗 arXiv: [`2510.04468`](https://arxiv.org/abs/2510.04468)
- 👥 作者: Asif Mohammed Samir, Mohammad Masudur Rahman
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.04468.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用LLM的语义理解能力来增强信息检索系统，以解决软件缺陷定位这一特定领域的复杂检索和匹配问题。这种方法论与“质谱结构推理”中需要从质谱特征语义出发检索和匹配分子结构的核心挑战直接相关。

**📖 中文摘要**

本文提出了IQLoc，一种结合信息检索和大型语言模型进行软件缺陷定位的新方法。该方法利用基于Transformer的模型对代码语义的理解，来推理代码的可疑性并重新制定搜索查询，从而增强基于信息检索的缺陷定位。具体而言，IQLoc通过理解代码语义来重新制定与缺陷报告相关的搜索查询，以提高检索精度。该方法在包含约7.5K个缺陷报告的扩展基准上进行了评估，结果显示其性能显著优于八种基线技术。该工作的核心思想是利用LLM的语义理解能力来增强传统检索系统的性能，这一“语义增强检索”范式与“质谱结构推理”中需要从海量质谱库中检索和匹配候选结构的问题高度相关。IQLoc的方法论可以启发构建能够理解质谱特征语义、从而更精准检索候选分子结构的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Despite decades of research, software bug localization remains challenging due to heterogeneous content and inherent ambiguities in bug reports. Existing methods, such as Information Retrieval (IR)-based approaches, often attempt to match source documents to bug reports, overlooking the context and semantics of the source code. On the other hand, Large Language Models (LLMs) (e.g., Transformer models) show promising results in understanding both texts and code. However, they have not yet been adapted well to localize software bugs using bug reports. They could also be data or resource-intensive. To bridge this gap, we propose, IQLoc, a novel approach that capitalizes on the strengths of both IR and LLMs for bug localization. In particular, we leverage the transformer-based model's understanding of code semantics to reason about its suspiciousness and to reformulate search queries and thus enhance bug localization using Information Retrieval. To evaluate IQLoc, we refine the Bench4BL benchmark dataset and extend it by incorporating ~30% more recent bug reports, resulting in a benchmark containing ~7.5K bug reports. We evaluated IQLoc using three performance metrics and compare it against eight baseline techniques. Experimental results demonstrate its superiority, achieving up to 100.40% and 78.08% in MAP, 61.49% and 64.58% in MRR, and 76.98% and 100.90% in HIT@K for the test bug reports with random and time-wise splits, respectively. Moreover, IQLoc improves MAP by 118.70% for bug reports with stack traces, 111.87% for those that include code elements, and 127.45% for those containing only descriptions in natural language. By integrating program semantic understanding into Information Retrieval, IQLoc mitigates several longstanding challenges of traditional IR-based approaches in bug localization.

</details>

---

### 61. [CoT-PL: Chain-of-Thought Pseudo-Labeling for Open-Vocabulary Object Detection](https://arxiv.org/abs/2510.14792)

**基本信息**

- 🔗 arXiv: [`2510.14792`](https://arxiv.org/abs/2510.14792)
- 👥 作者: Hojun Choi, Youngsun Lim, Jaeyo Shin 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.14792.pdf)

**💡 相关性分析**

满足标准1：论文提出的CoT-PL框架，其核心是将复杂视觉任务分解为多步可解释推理链并用于生成监督信号。这一方法论与构建能够进行逐步、可解释推理的“质谱结构推理”模型高度契合，为解决该领域的核心挑战提供了创新思路。

**📖 中文摘要**

本文提出了CoT-PL框架，将视觉思维链推理融入开放词汇目标检测的伪标签生成过程。它将复杂的场景理解分解为三个可解释的步骤：目标定位、类别识别和背景 grounding。这些中间推理状态作为丰富的监督源。在标准OVD评估协议上的大量实验表明，CoT-PL实现了最先进的性能。该工作的核心创新在于将复杂的感知任务分解为多步、可解释的推理链，并利用中间步骤的输出作为监督信号。这种“思维链”赋能的方法对于“质谱结构推理”这一复杂任务具有极强的借鉴意义。质谱解析同样可以建模为一个多步推理过程（如峰解析、子结构推断、结构组装），CoT-PL的框架为设计能够进行可解释、分步推理的质谱分析大模型提供了直接的技术蓝图。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Open-vocabulary object detection (OVD) aims to recognize and localize object categories beyond the training set. Recent approaches leverage vision-language models to generate pseudo-labels using image-text alignment, allowing detectors to generalize to unseen classes without explicit supervision. However, these methods depend heavily on single-step image-text matching, neglecting the intermediate reasoning steps crucial for interpreting semantically complex visual contexts, such as crowding or occlusion. In this paper, we introduce CoT-PL, a framework that incorporates visual chain-of-thought reasoning into the pseudo-labeling process for OVD. It decomposes complex scene understanding into three interpretable steps-object localization, category recognition, and background grounding-where these intermediate reasoning states serve as rich supervision sources. Extensive experiments on standard OVD evaluation protocols demonstrate that CoT-PL achieves state-of-the-art performance with superior pseudo-labeling efficiency, outperforming the strong baseline by 9.4 AP50 for novel classes on OV-COCO and improving box and mask APr by 3.2 and 2.2, respectively, on OV-LVIS. Code and models are available at this https URL .

</details>

---

### 62. [SHAP Meets Tensor Networks: Provably Tractable Explanations with Parallelism](https://arxiv.org/abs/2510.21599)

**基本信息**

- 🔗 arXiv: [`2510.21599`](https://arxiv.org/abs/2510.21599)
- 👥 作者: Reda Marzouk, Shahaf Bassan, Guy Katz
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.21599.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对张量网络等模型的可解释性（SHAP）计算，并给出了高效计算的理论结果。模型可解释性是“化学大模型”和“质谱结构推理”模型可信赖部署的关键要求，该工作为此提供了重要的理论和方法参考。

**📖 中文摘要**

本文分析了为张量网络计算SHAP解释的问题。作者提出了一个通用框架，用于计算具有任意结构的通用张量网络的精确SHAP解释。有趣的是，当张量网络被限制为张量链结构时，SHAP计算可以在多项式对数时间内使用并行计算完成。由于张量链的表达能力，这一复杂性结果可以推广到许多其他流行的ML模型，如决策树、树集成、线性模型和线性RNN。最后，通过将二值化神经网络约简为张量网络表示，作者证明了当网络的“宽度”固定时，SHAP计算可以变得“高效可处理”。该工作从计算复杂性和模型表达性的理论角度，深入分析了SHAP这一重要可解释性方法在各类模型（包括可作为大模型组件的子模型）上的可行性。这对于理解和构建可解释的“化学大模型”（例如，理解模型为何预测某个分子结构）提供了重要的理论基础和工具洞察。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Although Shapley additive explanations (SHAP) can be computed in polynomial time for simple models like decision trees, they unfortunately become NP-hard to compute for more expressive black-box models like neural networks - where generating explanations is often most critical. In this work, we analyze the problem of computing SHAP explanations for *Tensor Networks (TNs)*, a broader and more expressive class of models than those for which current exact SHAP algorithms are known to hold, and which is widely used for neural network abstraction and compression. First, we introduce a general framework for computing provably exact SHAP explanations for general TNs with arbitrary structures. Interestingly, we show that, when TNs are restricted to a *Tensor Train (TT)* structure, SHAP computation can be performed in *poly-logarithmic* time using *parallel* computation. Thanks to the expressiveness power of TTs, this complexity result can be generalized to many other popular ML models such as decision trees, tree ensembles, linear models, and linear RNNs, therefore tightening previously reported complexity results for these families of models. Finally, by leveraging reductions of binarized neural networks to Tensor Network representations, we demonstrate that SHAP computation can become *efficiently tractable* when the network's *width* is fixed, while it remains computationally hard even with constant *depth*. This highlights an important insight: for this class of models, width - rather than depth - emerges as the primary computational bottleneck in SHAP computation.

</details>

---

### 63. [From Slides to Chatbots: Enhancing Large Language Models with University Course Materials](https://arxiv.org/abs/2510.22272)

**基本信息**

- 🔗 arXiv: [`2510.22272`](https://arxiv.org/abs/2510.22272)
- 👥 作者: Tu Anh Dinh, Philipp Nicolas Schumacher, Jan Niehues
- 📄 PDF: [下载](https://arxiv.org/pdf/2510.22272.pdf)

**💡 相关性分析**

满足标准2：论文系统地研究了如何利用特定领域（计算机科学课程）的多模态材料（幻灯片、文字稿）作为数据资源，通过RAG等技术增强LLM的领域能力。这为构建“化学大模型”时，如何利用化学领域的类似多模态资料（教科书、论文、演示文稿）提供了直接的方法论参考和数据利用策略。

**📖 中文摘要**

本文研究了如何通过融入大学课程材料来增强大型语言模型在大学计算机科学课程问答中的性能。作者比较了检索增强生成和持续预训练两种策略，将课程特定知识扩展到LLMs中。对于讲座幻灯片，作者进一步探索了多模态RAG方法，将检索到的内容以图像形式呈现给生成器。实验表明，鉴于大学课程材料的规模相对较小，RAG比CPT更有效和高效。此外，在多模态设置中将幻灯片作为图像纳入，比纯文本检索显著提高了性能。该工作系统地探索了如何利用领域特定、多模态材料（幻灯片、文字稿）来增强LLM的领域专业知识。这对于构建“化学大模型”具有直接的参考价值：化学领域同样拥有大量幻灯片、教科书、研究论文等多模态资料，该论文的方法论为如何有效利用这些资源来训练或增强化学领域专业模型提供了实证依据和技术路径。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have advanced rapidly in recent years. One application of LLMs is to support student learning in educational settings. However, prior work has shown that LLMs still struggle to answer questions accurately within university-level computer science courses. In this work, we investigate how incorporating university course materials can enhance LLM performance in this setting. A key challenge lies in leveraging diverse course materials such as lecture slides and transcripts, which differ substantially from typical textual corpora: slides also contain visual elements like images and formulas, while transcripts contain spoken, less structured language. We compare two strategies, Retrieval-Augmented Generation (RAG) and Continual Pre-Training (CPT), to extend LLMs with course-specific knowledge. For lecture slides, we further explore a multi-modal RAG approach, where we present the retrieved content to the generator in image form. Our experiments reveal that, given the relatively small size of university course materials, RAG is more effective and efficient than CPT. Moreover, incorporating slides as images in the multi-modal setting significantly improves performance over text-only retrieval. These findings highlight practical strategies for developing AI assistants that better support learning and teaching, and we hope they inspire similar efforts in other educational contexts.

</details>

---

### 64. [Genomic Next-Token Predictors are In-Context Learners](https://arxiv.org/abs/2511.12797)

**基本信息**

- 🔗 arXiv: [`2511.12797`](https://arxiv.org/abs/2511.12797)
- 👥 作者: Nathan Breslow, Aayush Mishra, Mahler Revsine 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.12797.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是探索在非语言的基因组序列领域，通过大规模预测训练能否涌现出上下文学习能力。这为“化学大模型”的研究提供了重要的类比和理论基础，即通过对化学序列数据的类似训练，也可能使模型获得强大的化学领域ICL和推理能力。同时，这也是一篇关于ICL涌现机制的展望性讨论。

**📖 中文摘要**

本文研究了在主要通过大规模下一代核苷酸预测训练的基因组序列模型中，上下文学习能力是否能够有机地涌现。作者研究了Evo2基因组模型，其训练规模与中型LLM相当。他们开发了一个包含符号推理任务的受控实验框架，这些任务以语言和基因组形式实例化，从而能够直接比较基因组模型和语言模型的ICL能力。结果表明，基因组模型与其语言对应物一样，随着上下文演示数量的增加，在模式归纳方面表现出对数线性增益。据作者所知，这是基因组序列中有机涌现ICL的第一个证据，支持了ICL作为对丰富数据进行大规模预测建模的结果而出现的假设。这项研究将涌现的元学习能力扩展到了语言之外，指向了对上下文学习的统一、模态不可知的观点。这对于“化学大模型”的构建具有深刻启示：它表明，通过对化学序列数据（如SMILES字符串、质谱峰序列）进行大规模的自监督预测训练，模型也有可能涌现出对化学结构和规律的上下文学习能力，从而更好地进行分子生成、性质预测或质谱解析等任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In-context learning (ICL) -- the capacity of a model to infer and apply abstract patterns from examples provided within its input -- has been extensively studied in large language models trained for next-token prediction on human text. In fact, prior work often attributes this emergent behavior to distinctive statistical properties in human language. This raises a fundamental question: can ICL arise organically in other sequence domains purely through large-scale predictive training? To explore this, we turn to genomic sequences, an alternative symbolic domain rich in statistical structure. Specifically, we study the Evo2 genomic model, trained predominantly on next-nucleotide (A/T/C/G) prediction, at a scale comparable to mid-sized LLMs. We develop a controlled experimental framework comprising symbolic reasoning tasks instantiated in both linguistic and genomic forms, enabling direct comparison of ICL across genomic and linguistic models. Our results show that genomic models, like their linguistic counterparts, exhibit log-linear gains in pattern induction as the number of in-context demonstrations increases. To the best of our knowledge, this is the first evidence of organically emergent ICL in genomic sequences, supporting the hypothesis that ICL arises as a consequence of large-scale predictive modeling over rich data. These findings extend emergent meta-learning beyond language, pointing toward a unified, modality-agnostic view of in-context learning.

</details>

---

### 65. [DSeq-JEPA: Discriminative Sequential Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2511.17354)

**基本信息**

- 🔗 arXiv: [`2511.17354`](https://arxiv.org/abs/2511.17354)
- 👥 作者: Xiangteng He, Shunsuke Sakai, Shivam Chandhok 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.17354.pdf)

**💡 相关性分析**

满足标准1：论文提出的DSeq-JEPA自监督学习框架，其核心创新是让模型按判别性顺序学习预测视觉信息。这种“顺序重要性感知”的预训练范式，对于设计能够进行层次化、分步推理的“化学大模型”（如质谱结构推理）具有重要的方法论启示。

**📖 中文摘要**

本文提出了DSeq-JEPA，一种判别性顺序联合嵌入预测架构，它将潜在预测与自回归自监督学习联系起来。具体来说，DSeq-JEPA将判别性有序顺序过程与JEPA风格的学习目标相结合。这是通过（i）使用注意力衍生的显著性图来识别主要判别性区域，作为视觉重要性的代理，以及（ii）按判别性顺序预测后续区域，从而在预训练中诱导从主要线索到次要线索的课程式语义进展。在图像分类、细粒度视觉分类、检测/分割和低级推理等任务上的大量实验表明，与I-JEPA变体相比，DSeq-JEPA consistently 学习到更具判别性和可泛化的表示。该工作提出了一种新颖的自监督学习框架，通过引入“顺序”和“判别性”的概念来改进表示学习。其核心思想——模型应该按照重要性顺序关注和预测信息的不同部分——对于设计“化学大模型”的预训练任务具有启发意义。例如，在质谱解析中，模型可以学习先关注基峰或特征峰（主要判别区域），再逐步推理其他碎片信息（次要区域），从而获得更好的表示和推理能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in self-supervised visual representation learning have demonstrated the effectiveness of predictive latent-space objectives for learning transferable features. In particular, Image-based Joint-Embedding Predictive Architecture (I-JEPA) learns representations by predicting latent embeddings of masked target regions from visible context. However, it predicts target regions in parallel and all at once, lacking ability to order predictions meaningfully. Inspired by human visual perception, which attends selectively and progressively from primary to secondary cues, we propose DSeq-JEPA, a Discriminative Sequential Joint-Embedding Predictive Architecture that bridges latent predictive and autoregressive self-supervised learning. Specifically, DSeq-JEPA integrates a discriminatively ordered sequential process with JEPA-style learning objective. This is achieved by (i) identifying primary discriminative regions using an attention-derived saliency map that serves as a proxy for visual importance, and (ii) predicting subsequent regions in discriminative order, inducing a curriculum-like semantic progression from primary to secondary cues in pre-training. Extensive experiments across tasks -- image classification (ImageNet), fine-grained visual categorization (iNaturalist21, CUB, Stanford Cars), detection/segmentation (MS-COCO, ADE20K), and low-level reasoning (CLEVR) -- show that DSeq-JEPA consistently learns more discriminative and generalizable representations compared to I-JEPA variants. Project page: this https URL .

</details>

---

### 66. [Open Biomedical Knowledge Graphs at Scale: Construction, Federation, and AI Agent Access with Samyama Graph Database](https://arxiv.org/abs/2603.15080)

**基本信息**

- 🔗 arXiv: [`2603.15080`](https://arxiv.org/abs/2603.15080)
- 👥 作者: Madhulatha Mandarapu, Sandeep Kunkunuru
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15080.pdf)

**💡 相关性分析**

满足标准2：论文构建并发布了三个开放的大规模生物医学知识图谱，为化学信息学和相关领域的研究提供了可直接使用的结构化数据集和资源。

**📖 中文摘要**

这篇论文介绍了三个开源生物医学知识图谱（Pathways KG、Clinical Trials KG、Drug Interactions KG）的构建，这些图谱整合了来自Reactome、STRING、ClinicalTrials.gov、DrugBank等多个异构公共数据源的信息。论文的核心贡献在于描述了一种可复现的ETL模式，用于从异构数据源构建大规模知识图谱，并实现了跨图谱的联邦查询。此外，论文还引入了基于模式驱动的MCP服务器生成方法，以支持LLM智能体对图谱的访问。这项工作为化学信息学和生物信息学领域提供了可直接用于模型训练和推理的结构化、大规模、高质量数据集资源。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Biomedical knowledge is fragmented across siloed databases -- Reactome for pathways, STRING for protein interactions, this http URL for study registries, DrugBank for drug vocabularies, DGIdb for drug-gene interactions, SIDER for side effects. We present three open-source biomedical knowledge graphs -- Pathways KG (118,686 nodes, 834,785 edges from 5 sources), Clinical Trials KG (7,774,446 nodes, 26,973,997 edges from 5 sources), and Drug Interactions KG (32,726 nodes, 191,970 edges from 3 sources) -- built on Samyama, a high-performance graph database written in Rust. Our contributions are threefold. First, we describe a reproducible ETL pattern for constructing large-scale KGs from heterogeneous public data sources, with cross-source deduplication, batch loading (Python Cypher and Rust native loaders), and portable snapshot export. Second, we demonstrate cross-KG federation: loading all three snapshots into a single graph tenant enables property-based joins across datasets. Third, we introduce schema-driven MCP server generation for LLM agent access, evaluated on a new BiomedQA benchmark (40 pharmacology questions): domain-specific MCP tools achieve 98% accuracy vs. 85% for schema-aware text-to-Cypher and 75% for standalone GPT-4o, with zero schema errors. All data sources are open-license. The combined federated graph (7.9M nodes, 28M edges) loads in approximately 3 minutes on commodity cloud hardware, with single-KG queries completing in 80-100ms and cross-KG federation joins in 1-4s

</details>

---

### 67. [CTG-DB: An Ontology-Based Transformation of ClinicalTrials.gov to Enable Cross-Trial Drug Safety Analyses](https://arxiv.org/abs/2603.15936)

**基本信息**

- 🔗 arXiv: [`2603.15936`](https://arxiv.org/abs/2603.15936)
- 👥 作者: Jeffery L. Painter, François Haguinet, Andrew Bate
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15936.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个数据处理流程，将ClinicalTrials.gov的原始数据转化为标准化的、可用于系统药理学和药物安全分析的关系数据库，为化学信息学研究提供了重要的数据资源。

**📖 中文摘要**

这篇论文提出了CTG-DB，一个将ClinicalTrials.gov（CT.gov）临床试验注册数据转换为关系数据库的开放源代码流程。该流程的关键创新在于使用医学词典MedDRA对临床试验中非标准化的不良事件（AE）术语进行标准化映射，从而支持概念级别的检索和跨试验的聚合分析。这项工作为药物安全性和药效学研究（属于化学信息学的应用范畴）提供了一个经过清洗、标准化、可大规模分析的数据集，能够用于下游的信号检测和整合分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

ClinicalTrials .gov (CT .gov) is the largest publicly accessible registry of clinical studies, yet its registry-oriented architecture and heterogeneous adverse event (AE) terminology limit systematic pharmacovigilance (PV) analytics. AEs are typically recorded as investigator-reported text rather than standardized identifiers, requiring manual reconciliation to identify coherent safety concepts. We present the ClinicalTrials .gov Transformation Database (CTG-DB), an open-source pipeline that ingests the complete CT .gov XML archive and produces a relational database aligned to standardized AE terminology using the Medical Dictionary for Regulatory Activities (MedDRA). CTG-DB preserves arm-level denominators, represents placebo and comparator arms, and normalizes AE terminology using deterministic exact and fuzzy matching to ensure transparent and reproducible mappings. This framework enables concept-level retrieval and cross-trial aggregation for scalable placebo-referenced safety analyses and integration of clinical trial evidence into downstream PV signal detection.

</details>

---

### 68. [A Comprehensive Benchmark of Histopathology Foundation Models for Kidney Digital Pathology Images](https://arxiv.org/abs/2603.15967)

**基本信息**

- 🔗 arXiv: [`2603.15967`](https://arxiv.org/abs/2603.15967)
- 👥 作者: Harishwar Reddy Kasireddy, Patricio S. La Rosa, Akshita Gupta 等15人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.15967.pdf)

**💡 相关性分析**

满足标准2：论文对一系列预训练模型在特定生物医学领域（肾脏病理）进行了系统性评估，并发布了用于复现评估流程的开源工具包，为相关领域的研究提供了重要的模型评估资源和工具。

**📖 中文摘要**

这篇论文对11个公开的组织病理学基础模型（HFMs）在肾脏数字病理图像上的表现进行了全面的基准测试。研究涵盖了多个染色、空间尺度和临床任务。虽然焦点是组织病理学，但论文系统地评估了预训练基础模型在非癌症慢性肾病（一个重要的生物医学领域）上的迁移能力和局限性。这项工作为化学信息学和生物医学中基于图像的分子表型或疾病诊断研究提供了模型评估的方法学参考和性能基准。同时，论文发布了一个开源Python包（kidney-hfm-eval），促进了相关研究的可复现性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Histopathology foundation models (HFMs), pretrained on large-scale cancer datasets, have advanced computational pathology. However, their applicability to non-cancerous chronic kidney disease remains underexplored, despite coexistence of renal pathology with malignancies such as renal cell and urothelial carcinoma. We systematically evaluate 11 publicly available HFMs across 11 kidney-specific downstream tasks spanning multiple stains (PAS, H&E, PASM, and IHC), spatial scales (tile and slide-level), task types (classification, regression, and copy detection), and clinical objectives, including detection, diagnosis, and prognosis. Tile-level performance is assessed using repeated stratified group cross-validation, while slide-level tasks are evaluated using repeated nested stratified cross-validation. Statistical significance is examined using Friedman test followed by pairwise Wilcoxon signed-rank testing with Holm-Bonferroni correction and compact letter display visualization. To promote reproducibility, we release an open-source Python package, kidney-hfm-eval, available at this https URL , that reproduces the evaluation pipelines. Results show moderate to strong performance on tasks driven by coarse meso-scale renal morphology, including diagnostic classification and detection of prominent structural alterations. In contrast, performance consistently declines for tasks requiring fine-grained microstructural discrimination, complex biological phenotypes, or slide-level prognostic inference, largely independent of stain type. Overall, current HFMs appear to encode predominantly static meso-scale representations and may have limited capacity to capture subtle renal pathology or prognosis-related signals. Our results highlight the need for kidney-specific, multi-stain, and multimodal foundation models to support clinically reliable decision-making in nephrology.

</details>

---

### 69. [Reduced Density Matrices Through Machine Learning](https://arxiv.org/abs/2511.07367)

**基本信息**

- 🔗 arXiv: [`2511.07367`](https://arxiv.org/abs/2511.07367)
- 👥 作者: Awwab A. Azam, Lexu Zhao, Jiabin Yu
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.07367.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用神经网络预测强关联量子系统的约化密度矩阵，这是量子化学和计算化学中的核心问题。该方法为构建更高效的化学模拟大模型提供了新的技术路径。

**📖 中文摘要**

这篇论文利用神经网络架构来加速甚至预测大系统强关联态的n粒子约化密度矩阵（n-RDMs）。研究直觉在于，对于有能隙的态，n-RDMs通常是布里渊区上的平滑函数，因此是可插值的，允许在小型系统上训练的神经网络预测大型系统的n-RDMs。论文构建了两种神经网络：一种将随机RDM映射到物理RDM的自注意力网络；另一种直接将动量空间坐标映射到RDM值的正弦表示网络。该方法在三个二维模型上进行了测试。这项工作为量子化学和材料科学中计算成本高昂的强关联系统模拟提供了一种高效的机器学习加速方案，与“化学大模型”中涉及电子结构计算的部分密切相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

$n$-particle reduced density matrices ($n$-RDMs) play a central role in understanding correlated phases of matter, but their calculation is often computationally inefficient for strongly-correlated states at large system sizes. In this work, we use neural network (NN) architectures to accelerate and even predict $n$-RDMs for large systems. Our underlying intuition is that, for gapped states, $n$-RDMs are often smooth functions over the Brillouin zone (BZ) and are therefore interpolable, allowing NNs trained on small-size systems to predict large-size ones. Building on this, we devise two NNs: (i) a self-attention NN that maps random RDMs to physical ones, and (ii) a Sinusoidal Representation Network (SIREN) that directly maps momentum-space coordinates to RDM values. We test the NNs on RDMs in three 2D models: the pair-pair correlation functions of the Richardson model of superconductivity, the translationally-invariant Hartree-Fock (HF) 1-RDM in a four-band repulsive model, and the translation-breaking HF 1-RDM in the half-filled Hubbard model. We find that a SIREN trained on a $6\times 6$ momentum mesh and a SIREN trained on $4$ tilted meshes (each of which has $12$ momentum points) can predict the $18\times 18$ pair-pair correlation function with a relative accuracy of $94.29\%$ and $93.77\%$, respectively. NNs trained on $6\times 6$ and $8\times 8$ meshes provide high-quality initial guesses for $50\times 50$ translation-invariant HF and $30\times 30$ fully translation-breaking-allowed HF, reducing the required number of iterations by up to $91.63\%$ and $92.78\%$, respectively, compared to random initializations. Our results illustrate the potential of NN-based methods for interpolable $n$-RDMs, which might open a new avenue for future research on strongly correlated phases.

</details>

---

### 70. [Solving physics-constrained inverse problems with conditional flow matching](https://arxiv.org/abs/2603.14135)

**基本信息**

- 🔗 arXiv: [`2603.14135`](https://arxiv.org/abs/2603.14135)
- 👥 作者: Agnimitra Dasgupta, Ali Fardisi, Mehrnegar Aminy 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14135.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是解决物理约束的逆问题，提出了一种基于条件流匹配的通用贝叶斯推理框架。该框架可直接应用于化学和质谱分析中的逆问题，如从光谱数据推断分子结构或性质，与“质谱结构推理”主题高度相关。

**📖 中文摘要**

这篇论文提出了一个条件流匹配框架，用于解决物理约束的贝叶斯逆问题。该框架能够从推断变量和测量的联合分布中采样，而不需要显式评估先验和似然密度。它通过训练神经网络来学习概率流ODE的速度场，从而直接将样本从源分布传输到以观测测量为条件的后验分布。该方法是黑盒式的，适用于非线性、高维且可能不可微的正向模型。论文在多个基于物理的逆问题上进行了评估。这项工作为“化学大模型”和“质谱结构推理”中常见的逆问题（例如，从光谱数据反推分子结构或性质）提供了一种强大的、无需显式似然函数的概率推理工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This study presents a conditional flow matching framework for solving physics-constrained Bayesian inverse problems. In this setting, samples from the joint distribution of inferred variables and measurements are assumed available, while explicit evaluation of the prior and likelihood densities is not required. We derive a simple and self-contained formulation of both the unconditional and conditional flow matching algorithms, tailored specifically to inverse problems. In the conditional setting, a neural network is trained to learn the velocity field of a probability flow ordinary differential equation that transports samples from a chosen source distribution directly to the posterior distribution conditioned on observed measurements. This black-box formulation accommodates nonlinear, high-dimensional, and potentially non-differentiable forward models without restrictive assumptions on the noise model. We further analyze the behavior of the learned velocity field in the regime of finite training data. Under mild architectural assumptions, we show that overtraining can induce degenerate behavior in the generated conditional distributions, including variance collapse and a phenomenon termed selective memorization, wherein generated samples concentrate around training data points associated with similar observations. A simplified theoretical analysis explains this behavior, and numerical experiments confirm it in practice. We demonstrate that standard early-stopping criteria based on monitoring test loss effectively mitigate such degeneracy. The proposed method is evaluated on several physics-based inverse problems. We investigate the impact of different choices of source distributions, including Gaussian and data-informed priors. Across these examples, conditional flow matching accurately captures complex, multimodal posterior distributions while maintaining computational efficiency.

</details>

---

### 71. [AR-Flow VAE: A Structured Autoregressive Flow Prior Variational Autoencoder for Unsupervised Blind Source Separation](https://arxiv.org/abs/2603.14441)

**基本信息**

- 🔗 arXiv: [`2603.14441`](https://arxiv.org/abs/2603.14441)
- 👥 作者: Yuan-Hao Wei, Fu-Hao Deng, Lin-Yong Cui 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14441.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种新的生成模型（AR-Flow VAE）用于盲源分离，这直接对应于“质谱结构推理”中从混合观测数据中推断潜在源（化合物）的基本问题。

**📖 中文摘要**

这篇论文提出了AR-Flow VAE，一种用于无监督盲源分离的新型变分自编码器框架。该框架的核心创新是为每个潜在源信号配备一个参数自适应的自回归流先验。这种先验极大地增强了潜在源建模的灵活性，能够捕捉复杂的非高斯行为和时间相关性等结构化依赖。论文将盲源分离问题自然地解释为VAE的编码（解混）和解码（重混）过程。这项工作为从混合信号（例如复杂的质谱或色谱数据）中分离出潜在的化学成分或信号源提供了一种新的、灵活的生成式建模方法，与“质谱结构推理”中从混合谱图推断单一化合物结构的问题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Blind source separation (BSS) seeks to recover latent source signals from observed mixtures. Variational autoencoders (VAEs) offer a natural perspective for this problem: the latent variables can be interpreted as source components, the encoder can be viewed as a demixing mapping from observations to sources, and the decoder can be regarded as a remixing process from inferred sources back to observations. In this work, we propose AR-Flow VAE, a novel VAE-based framework for BSS in which each latent source is endowed with a parameter-adaptive autoregressive flow prior. This prior significantly enhances the flexibility of latent source modeling, enabling the framework to capture complex non-Gaussian behaviors and structured dependencies, such as temporal correlations, that are difficult to represent with conventional priors. In addition, the structured prior design assigns distinct priors to different latent dimensions, thereby encouraging the latent components to separate into different source signals under heterogeneous prior constraints. Experimental results validate the effectiveness of the proposed architecture for blind source separation. More importantly, this work provides a foundation for future investigations into the identifiability and interpretability of AR-Flow VAE.

</details>

---

### 72. [Distance Backbones Optimize Spreading Dynamics and Centrality Ranks in the Sparsification of Complex Networks](https://arxiv.org/abs/2603.14564)

**基本信息**

- 🔗 arXiv: [`2603.14564`](https://arxiv.org/abs/2603.14564)
- 👥 作者: Bernardo Pereira, Felipe Xavier Costa, Luís M. Rocha
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.14564.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是图稀疏化和网络动力学保留，其提出的距离骨干和DBS方法为处理化学信息学中的分子图、相互作用网络等复杂图结构提供了新的算法工具，与基于图的化学大模型研究相关。

**📖 中文摘要**

这篇论文研究了加权图的距离骨干（Distance Backbones）在复杂网络稀疏化中的应用。距离骨干通过移除违反广义三角不等式的边来保留加权图的所有最短路径。论文表明，与最先进的替代方法相比，距离骨干通常能更有效地稀疏化图，并更好地保留节点中心性排名以及传播动力学中的局部和全局动态。论文引入了距离骨干合成（DBS）方法，用于根据嵌套距离骨干族逐步稀疏化加权图。这项工作为化学信息学中常见的分子图或相互作用网络的简化、特征提取和动力学模拟提供了新的理论工具和方法，有助于构建更高效、可解释的化学图模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Detailed network models of social, biological and other complex systems are often dense, which increases their computational complexity in simulations and analysis. To address this challenge, graph sparsification is used to remove edges while preserving desired network properties. Distance backbones of weighted graphs, which remove edges that break a generalized triangle inequality for any given path-length measure, preserve all shortest paths of weighted graphs. They have been shown to typically sparsify graphs more, as well as preserve community structure and spreading dynamics better than alternative state-of-the-art methods. Here, We show that they significantly best preserve node centrality ranks, as well as local and global dynamics in spreading phenomena. This is done by introducing the distance backbone synthesis (DBS) to progressively sparsify weighted graphs according to a general family of nested distance backbones, whereby each edge is associated with the smallest distance backbone in which it appears. DBS provides a principled and natural method to sweep all degrees of sparsification possible while preserving connectivity, allowing us to precisely study (directed and undirected) weighted graph sparsification under multi-objective criteria. It provides an algebraically-principled explanation of edge importance by revealing the precise topological space associated with each edge. The theory is demonstrated with a battery of social contact networks obtained from real-world social activity in different scenarios. Our study also shows that the optimal preservation of node centrality and spreading dynamics happens for the distance backbone obeying the generalized triangle inequality for the path-length measure $g(x, y) = (\sqrt[3]{x}+\sqrt[3]{y})^3$, which removes more than half of the edges from the empirical networks studied.

</details>

---

## 📊 数据统计
- 累计运行天数：39
- 累计论文数量：2804

## 📝 历史记录

> 暂无历史数据

