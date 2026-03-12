# 📚 ArXiv 论文日报

> 每天自动更新，关注 **化学大模型, 质谱结构推理** 相关的最新论文

## 更新时间
⏰ 2026-03-12 01:13:39

## 📅 2026-03-12 (今日最新)

**相关论文数：88**

### 1. [SiliconMind-V1: Multi-Agent Distillation and Debug-Reasoning Workflows for Verilog Code Generation](https://arxiv.org/abs/2603.08719)

**基本信息**

- 🔗 arXiv: [`2603.08719`](https://arxiv.org/abs/2603.08719)
- 👥 作者: Mu-Chi Chen, Yu-Hung Kao, Po-Hsuan Huang 等13人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08719.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于硬件设计（Verilog代码生成）的多智能体大语言模型框架。这直接体现了“化学大模型”主题中“大模型”在特定科学/工程领域的应用、构建和优化方法。论文重点在于模型的推理、调试和迭代生成能力，这些是构建复杂领域大模型（如化学大模型）的关键技术。

**📖 中文摘要**

这篇论文提出了SiliconMind-V1，一个用于Verilog代码生成的多智能体框架。该框架集成了面向推理的训练数据生成和基于测试平台的验证。其核心是通过测试时扩展，使经过本地微调的大语言模型能够迭代地生成、测试和调试寄存器传输级设计。论文在多个基准测试上进行了评估，结果表明该方法在功能正确性方面优于现有技术，同时使用了更少的训练资源。虽然论文主要关注硬件设计自动化，但其核心方法是利用大语言模型进行迭代生成和调试，这本质上是在特定领域（硬件设计）应用和构建“化学大模型”的类似思路。它展示了如何将大语言模型与领域特定知识（测试平台）结合，形成一个能够推理和修正的智能系统，这与构建用于科学发现的化学大模型在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models (LLMs) have recently emerged as a promising approach for automating Verilog code generation; however, existing methods primarily emphasize syntactic correctness and often rely on commercial models or external verification tools, which introduces concerns regarding cost, data privacy, and limited guarantees of functional correctness. This work proposes a unified multi-agent framework for reasoning-oriented training data generation with integrated testbench-driven verification, enabling locally fine-tuned LLMs, SiliconMind-V1, to iteratively generate, test, and debug Register-Transfer Level (RTL) designs through test-time scaling. Experimental results on representative benchmarks (VerilogEval-v2, RTLLM-v2, and CVDP) demonstrate that the proposed approach outperforms the state-of-the-art QiMeng-CodeV-R1 in functional correctness while using fewer training resources.

</details>

---

### 2. [Robust Parameter and State Estimation in Multiscale Neuronal Systems Using Physics-Informed Neural Networks](https://arxiv.org/abs/2603.08742)

**基本信息**

- 🔗 arXiv: [`2603.08742`](https://arxiv.org/abs/2603.08742)
- 👥 作者: Changliang Wei, Yangyang Wang, Xueyu Zhu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08742.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用物理信息神经网络（PINN）进行生物物理系统的参数和状态估计。这本质上是“结构推理”问题——从观测数据（可类比为质谱信号）推断出底层系统的结构（模型参数）和状态。虽然领域是计算神经科学，但其方法论（基于深度学习的逆问题求解、从信号推理结构）与“质谱结构推理”的核心挑战高度一致。

**📖 中文摘要**

这篇论文开发了一个基于物理信息神经网络（PINN）的框架，用于从部分且嘈杂的观测数据中联合重建未观测的神经元状态变量并估计未知的生物物理参数。该方法应用于包括Morris-Lecar模型在内的生物物理神经元模型，涵盖了多个尖峰和爆发模式。论文表明，该方法仅需短时间窗口内的部分电压观测数据，并且即使在初始参数猜测不具信息性的情况下也能保持鲁棒性。PINN框架为多尺度神经元动力学中的逆问题提供了有前景的替代方案，而传统技术在此类问题上常常难以解决。这项工作展示了深度学习模型（PINN）在复杂生物物理系统建模和参数推理中的强大能力。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Inferring biophysical parameters and hidden state variables from partial and noisy observations is a fundamental challenge in computational neuroscience. This problem is particularly difficult for fast - slow spiking and bursting models, where strong nonlinearities, multiscale dynamics, and limited observational data often lead to severe sensitivity to initial parameter guesses and convergence failure in the methods replying on the traditional numerical forward solvers. In this work, we developed a physics-informed neural network (PINN) framework for the joint reconstruction of unobserved state variables and the estimation of unknown biophysical parameters in neuronal models. We demonstrate the effectiveness of the method on biophysical neuron models, including the Morris-Lecar model across multiple spiking and bursting regimes and a respiratory model neuron. The method requires only partial voltage observations over short observation windows and remains robust even when initialized with non-informative parameter guesses. These results suggest that PINN can deliver robust and accurate parameter inference and state reconstruction, providing a promising alternative for inverse problems in multiscale neuronal dynamics, where traditional techniques often struggle.

</details>

---

### 3. [Diagnosing FP4 inference: a layer-wise and block-wise sensitivity analysis of NVFP4 and MXFP4](https://arxiv.org/abs/2603.08747)

**基本信息**

- 🔗 arXiv: [`2603.08747`](https://arxiv.org/abs/2603.08747)
- 👥 作者: Musa Cim, Burak Topcu, Mahmut Taylan Kandemir
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08747.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大语言模型（作为“大模型”的一种）进行低精度量化（FP4）下的敏感性分析。这直接关系到“化学大模型”主题中模型优化、部署和效率的关键方面。量化是使大模型（包括化学大模型）能够在资源受限环境下（如边缘设备）高效运行的重要技术。论文对模型内部组件敏感性的深入分析，为设计高效的化学大模型提供了重要的方法论参考。

**📖 中文摘要**

本研究对两种4位浮点数格式（MXFP4和NVFP4）在三个不同规模的Qwen2.5模型上进行了系统的、组件级和块级的敏感性分析，以阐明量化敏感性。研究观察到，MLP的上投影和下投影层在敏感性方面 consistently 占主导地位，而门控投影和注意力投影对FP4量化的敏感性分别为中等和显著较低。研究进一步发现，敏感性并不普遍集中在最后的块中，早期的块也可能高度敏感，尤其是在MXFP4格式下。该结果为跨组件、深度和FP4格式的推理行为提供了诊断性特征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Quantization addresses the high resource demand for large language models (LLMs) by alleviating memory pressure and bandwidth congestion and providing significantly scaled compute power with a tolerable impact on accuracy. Four-bit floating point (FP4), the lowest-precision format that preserves essential numerical properties such as exponent and sign, has begun to be adopted in cutting-edge architectures, including Blackwell and AMD CDNA, to support LLM quantization and reduce deployment costs. Although aggressive quantization can yield efficiency gains, the quantization sensitivity of within-transformer layers and whether these sensitivities generalize across existing FP4 formats and model scales remain underexplored. To elucidate quantization sensitivity, this study conducts a systematic analysis of two FP4 formats, MXFP4 and NVFP4, across three Qwen2.5 model scales (0.5B, 7B, and 14B), using controlled component-wise and block-wise isolation methodologies. We observe that MLP up- and down-projection layers consistently dominate in terms of sensitivity, while gate and attention projections are moderately and substantially less sensitive to FP4 quantization, respectively. We further find that sensitivity does not universally localize to the final blocks, but early blocks can be highly sensitive, particularly under MXFP4. Our results provide a diagnostic characterization of the inference behavior of FP4 across components, depths, and FP4 formats.

</details>

---

### 4. [The Temporal Markov Transition Field](https://arxiv.org/abs/2603.08803)

**基本信息**

- 🔗 arXiv: [`2603.08803`](https://arxiv.org/abs/2603.08803)
- 👥 作者: Michael Leznik
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08803.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种新的时间序列表示方法（TMTF），可将序列数据转换为图像。这种数据表示技术本身可以作为一种“工具”或“资源”，用于处理和分析时序数据。在化学信息学和质谱分析中，质谱信号本身就是一种时间序列或序列数据。TMTF提供了一种将此类序列转换为适合深度学习模型（如CNN）处理的图像格式的潜在方法，这可能有助于后续的质谱结构推理或模式识别任务。

**📖 中文摘要**

本文引入了时间马尔可夫转移场（TMTF），它是经典马尔可夫转移场（MTF）的扩展。TMTF将时间序列划分为K个连续的时间块，为每个块估计一个局部转移矩阵，并组装图像，使得每一行反映其所在块的局部动态而非全局平均。由此产生的T×T图像具有K个不同纹理的水平带，每个带编码一个时间段的转移动力学。TMTF是幅度无关且保序的，使其适合作为卷积神经网络应用于时间序列表征任务的输入通道。该方法提供了一种将时间序列数据转换为结构化图像表示的新方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Markov Transition Field (MTF), introduced by Wang and Oates (2015), encodes a time series as a two-dimensional image by mapping each pair of time steps to the transition probability between their quantile states, estimated from a single global transition matrix. This construction is efficient when the transition dynamics are stationary, but produces a misleading representation when the process changes regime over time: the global matrix averages across regimes and the resulting image loses all information about \emph{when} each dynamical regime was active. In this paper we introduce the \emph{Temporal Markov Transition Field} (TMTF), an extension that partitions the series into $K$ contiguous temporal chunks, estimates a separate local transition matrix for each chunk, and assembles the image so that each row reflects the dynamics local to its chunk rather than the global average. The resulting $T \times T$ image has $K$ horizontal bands of distinct texture, each encoding the transition dynamics of one temporal segment. We develop the formal definition, establish the key structural properties of the representation, work through a complete numerical example that makes the distinction from the global MTF concrete, analyse the bias--variance trade-off introduced by temporal chunking, and discuss the geometric interpretation of the local transition matrices in terms of process properties such as persistence, mean reversion, and trending behaviour. The TMTF is amplitude-agnostic and order-preserving, making it suitable as an input channel for convolutional neural networks applied to time series characterisation tasks.

</details>

---

### 5. [Test-Driven AI Agent Definition (TDAD): Compiling Tool-Using Agents from Behavioral Specifications](https://arxiv.org/abs/2603.08806)

**基本信息**

- 🔗 arXiv: [`2603.08806`](https://arxiv.org/abs/2603.08806)
- 👥 作者: Tzafrir Rehan
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是针对大语言模型智能体的开发、测试和验证框架。这直接涉及“大模型”的应用层——如何可靠地构建基于大模型的智能体系统。论文中关于规范遵循、测试驱动、迭代优化的方法论，对于构建需要高度可靠性和可解释性的“化学大模型”或基于大模型的化学研究智能体具有重要的参考价值。

**📖 中文摘要**

本文提出了测试驱动的AI智能体定义（TDAD）方法，该方法将智能体提示视为编译产物：工程师提供行为规范，一个编码智能体将其转换为可执行测试，第二个编码智能体迭代优化提示直到测试通过。为了减轻规范博弈，TDAD引入了三种机制：（1）可见/隐藏测试分割，（2）通过语义突变测试进行后编译验证，（3）规范演化场景。论文在SpecSuite-Core基准上进行了评估，TDAD实现了高编译成功率和隐藏测试通过率。这项工作为构建行为可测量、符合规范的AI智能体（尤其是工具使用型LLM智能体）提供了系统化的工程方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present Test-Driven AI Agent Definition (TDAD), a methodology that treats agent prompts as compiled artifacts: engineers provide behavioral specifications, a coding agent converts them into executable tests, and a second coding agent iteratively refines the prompt until tests pass. Deploying tool-using LLM agents in production requires measurable behavioral compliance that current development practices cannot provide. Small prompt changes cause silent regressions, tool misuse goes undetected, and policy violations emerge only after deployment. To mitigate specification gaming, TDAD introduces three mechanisms: (1) visible/hidden test splits that withhold evaluation tests during compilation, (2) semantic mutation testing via a post-compilation agent that generates plausible faulty prompt variants, with the harness measuring whether the test suite detects them, and (3) spec evolution scenarios that quantify regression safety when requirements change. We evaluate TDAD on SpecSuite-Core, a benchmark of four deeply-specified agents spanning policy compliance, grounded analytics, runbook adherence, and deterministic enforcement. Across 24 independent trials, TDAD achieves 92% v1 compilation success with 97% mean hidden pass rate; evolved specifications compile at 58%, with most failed runs passing all visible tests except 1-2, and show 86-100% mutation scores, 78% v2 hidden pass rate, and 97% regression safety scores. The implementation is available as an open benchmark at this https URL .

</details>

---

### 6. [Beyond Relevance: On the Relationship Between Retrieval and RAG Information Coverage](https://arxiv.org/abs/2603.08819)

**基本信息**

- 🔗 arXiv: [`2603.08819`](https://arxiv.org/abs/2603.08819)
- 👥 作者: Saron Samuel, Alexander Martin, Eugene Yang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08819.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是检索增强生成（RAG）系统的性能评估与关联分析。RAG是大语言模型（“大模型”）处理知识密集型任务的关键技术之一。论文深入探讨了检索组件与生成组件之间的关系，这对于构建需要访问外部知识库（如化学数据库）的“化学大模型”或化学问答系统至关重要，有助于优化此类系统的架构和评估。

**📖 中文摘要**

本研究调查了检索增强生成（RAG）系统中，上游检索指标是否能作为最终生成响应信息覆盖度的可靠早期指标。通过在两个文本RAG基准和一个多模态基准上的实验，分析了多种检索策略和RAG流程。研究结果表明，基于覆盖度的检索指标与生成响应中的信息块覆盖度在主题和系统层面均存在强相关性。当检索目标与生成目标一致时，这种关系最为牢固，尽管更复杂的迭代RAG流程可以部分解耦生成质量与检索效果。这些发现为使用检索指标作为RAG性能的代理提供了实证支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-augmented generation (RAG) systems combine document retrieval with a generative model to address complex information seeking tasks like report generation. While the relationship between retrieval quality and generation effectiveness seems intuitive, it has not been systematically studied. We investigate whether upstream retrieval metrics can serve as reliable early indicators of the final generated response's information coverage. Through experiments across two text RAG benchmarks (TREC NeuCLIR 2024 and TREC RAG 2024) and one multimodal benchmark (WikiVideo), we analyze 15 text retrieval stacks and 10 multimodal retrieval stacks across four RAG pipelines and multiple evaluation frameworks (Auto-ARGUE and MiRAGE). Our findings demonstrate strong correlations between coverage-based retrieval metrics and nugget coverage in generated responses at both topic and system levels. This relationship holds most strongly when retrieval objectives align with generation goals, though more complex iterative RAG pipelines can partially decouple generation quality from retrieval effectiveness. These findings provide empirical support for using retrieval metrics as proxies for RAG performance.

</details>

---

### 7. [MASEval: Extending Multi-Agent Evaluation from Models to Systems](https://arxiv.org/abs/2603.08835)

**基本信息**

- 🔗 arXiv: [`2603.08835`](https://arxiv.org/abs/2603.08835)
- 👥 作者: Cornelius Emde, Alexander Rubinstein, Anmol Goel 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08835.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于评估多智能体系统的基准和框架（MASEval）。这提供了一个重要的“工具”和“评估资源”。随着基于大语言模型的智能体系统在科学研究（包括化学）中变得越来越普遍，一个系统级的评估框架对于比较不同智能体架构、优化基于“化学大模型”的研究助手或实验自动化平台至关重要。

**📖 中文摘要**

本文介绍了MASEval，一个用于评估多智能体系统的框架无关的库。它将整个系统作为分析单元，超越了传统的模型中心评估。通过一个涵盖3个基准、3个模型和3个框架的系统级比较，研究发现框架选择与模型选择同样重要。MASEval允许研究人员探索智能体系统的所有组件，为系统设计开辟了新途径，并帮助实践者为特定用例确定最佳实现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid adoption of LLM-based agentic systems has produced a rich ecosystem of frameworks (smolagents, LangGraph, AutoGen, CAMEL, LlamaIndex, i.a.). Yet existing benchmarks are model-centric: they fix the agentic setup and do not compare other system components. We argue that implementation decisions substantially impact performance, including choices such as topology, orchestration logic, and error handling. MASEval addresses this evaluation gap with a framework-agnostic library that treats the entire system as the unit of analysis. Through a systematic system-level comparison across 3 benchmarks, 3 models, and 3 frameworks, we find that framework choice matters as much as model choice. MASEval allows researchers to explore all components of agentic systems, opening new avenues for principled system design, and practitioners to identify the best implementation for their use case. MASEval is available under the MIT licence this https URL .

</details>

---

### 8. [LDP: An Identity-Aware Protocol for Multi-Agent LLM Systems](https://arxiv.org/abs/2603.08852)

**基本信息**

- 🔗 arXiv: [`2603.08852`](https://arxiv.org/abs/2603.08852)
- 👥 作者: Sunil Prakash
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08852.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个用于多智能体大语言模型系统间通信的新型协议（LDP）。这直接涉及“大模型”生态系统中的系统集成和交互问题。对于构建由多个 specialized 模型（例如，一个负责反应预测，一个负责光谱解析）协作完成的复杂化学研究任务，这样一个支持身份、质量、溯源和安全通信的协议具有重要的基础架构意义。

**📖 中文摘要**

本文提出了LLM委托协议（LDP），一种AI原生的通信协议，引入了五个机制：（1）包含质量提示和推理配置文件的丰富委托身份卡；（2）具有协商和回退功能的渐进式负载模式；（3）具有持久上下文的治理会话；（4）跟踪置信度和验证状态的结构化溯源；（5）在协议级别强制执行安全边界的信任域。LDP被实现为JamJet智能体运行时的插件，并通过实验评估表明，身份感知路由在简单任务上实现了更低的延迟，语义帧负载减少了令牌数量，治理会话消除了开销。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As multi-agent AI systems grow in complexity, the protocols connecting them constrain their capabilities. Current protocols such as A2A and MCP do not expose model-level properties as first-class primitives, ignoring properties fundamental to effective delegation: model identity, reasoning profile, quality calibration, and cost characteristics. We present the LLM Delegate Protocol (LDP), an AI-native communication protocol introducing five mechanisms: (1) rich delegate identity cards with quality hints and reasoning profiles; (2) progressive payload modes with negotiation and fallback; (3) governed sessions with persistent context; (4) structured provenance tracking confidence and verification status; (5) trust domains enforcing security boundaries at the protocol level. We implement LDP as a plugin for the JamJet agent runtime and evaluate against A2A and random baselines using local Ollama models and LLM-as-judge evaluation. Identity-aware routing achieves ~12x lower latency on easy tasks through delegate specialization, though it does not improve aggregate quality in our small delegate pool; semantic frame payloads reduce token count by 37% (p=0.031) with no observed quality loss; governed sessions eliminate 39% token overhead at 10 rounds; and noisy provenance degrades synthesis quality below the no-provenance baseline, arguing that confidence metadata is harmful without verification. Simulated analyses show architectural advantages in attack detection (96% vs. 6%) and failure recovery (100% vs. 35% completion). This paper contributes a protocol design, reference implementation, and initial evidence that AI-native protocol primitives enable more efficient and governable delegation.

</details>

---

### 9. [One Language, Two Scripts: Probing Script-Invariance in LLM Concept Representations](https://arxiv.org/abs/2603.08869)

**基本信息**

- 🔗 arXiv: [`2603.08869`](https://arxiv.org/abs/2603.08869)
- 👥 作者: Sripad Karne
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08869.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对大语言模型内部表示（通过SAE特征）的抽象性进行探测。这直接关系到“大模型”的可解释性和表示学习。理解大模型如何在内部表示抽象概念（如化学结构或反应，而非其具体字符串表示），对于构建和优化能够真正理解化学领域的“化学大模型”至关重要。论文提供了一种探测方法学和对表示不变性的见解。

**📖 中文摘要**

本研究利用塞尔维亚语的双文字（Digraphia）现象作为受控测试平台，探究稀疏自编码器（SAE）学习的特征是否表示抽象含义。塞尔维亚语可以用拉丁字母和西里尔字母互换书写，两者字符映射近乎完美，这使得可以在保持含义完全不变的情况下改变正字法。分析Gemma模型家族中SAE特征的激活发现，不同文字书写的相同句子激活了高度重叠的特征，远超随机基线。改变文字导致的表征差异小于同一文字内的释义差异，表明SAE特征优先考虑含义而非正字法形式。这种文字不变性随着模型规模而增强。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Do the features learned by Sparse Autoencoders (SAEs) represent abstract meaning, or are they tied to how text is written? We investigate this question using Serbian digraphia as a controlled testbed: Serbian is written interchangeably in Latin and Cyrillic scripts with a near-perfect character mapping between them, enabling us to vary orthography while holding meaning exactly constant. Crucially, these scripts are tokenized completely differently, sharing no tokens whatsoever. Analyzing SAE feature activations across the Gemma model family (270M-27B parameters), we find that identical sentences in different Serbian scripts activate highly overlapping features, far exceeding random baselines. Strikingly, changing script causes less representational divergence than paraphrasing within the same script, suggesting SAE features prioritize meaning over orthographic form. Cross-script cross-paraphrase comparisons provide evidence against memorization, as these combinations rarely co-occur in training data yet still exhibit substantial feature overlap. This script invariance strengthens with model scale. Taken together, our findings suggest that SAE features can capture semantics at a level of abstraction above surface tokenization, and we propose Serbian digraphia as a general evaluation paradigm for probing the abstractness of learned representations.

</details>

---

### 10. [Quantifying the Accuracy and Cost Impact of Design Decisions in Budget-Constrained Agentic LLM Search](https://arxiv.org/abs/2603.08877)

**基本信息**

- 🔗 arXiv: [`2603.08877`](https://arxiv.org/abs/2603.08877)
- 👥 作者: Kyle McCleary, James Ghawaly
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08877.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是预算约束下智能体RAG系统的性能优化。这直接关联到“大模型”在资源受限场景下的高效应用。对于需要调用外部工具和数据库进行复杂推理的“化学大模型”（例如，迭代查询质谱数据库或文献进行结构解析），如何平衡搜索成本、生成质量和计算预算是一个关键的实际问题。论文提供了该问题的实证分析和设计指南。

**📖 中文摘要**

本研究对预算约束下的智能体检索增强生成（RAG）系统进行了受控测量研究，探讨了搜索深度、检索策略和生成预算如何影响固定约束下的准确性和成本。使用预算约束智能体搜索（BCAS）评估框架，在六个LLM和三个问答基准上进行了比较。研究发现，准确率随着额外搜索次数的增加而提高，但存在一个小上限；结合词汇和稠密检索的混合检索策略带来了最大的平均增益；在HotpotQA风格的合成任务上，更大的生成预算最有帮助。这些结果为配置预算化的智能体检索管道提供了实用指导。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Agentic Retrieval-Augmented Generation (RAG) systems combine iterative search, planning prompts, and retrieval backends, but deployed settings impose explicit budgets on tool calls and completion tokens. We present a controlled measurement study of how search depth, retrieval strategy, and completion budget affect accuracy and cost under fixed constraints. Using Budget-Constrained Agentic Search (BCAS), a model-agnostic evaluation harness that surfaces remaining budget and gates tool use, we run comparisons across six LLMs and three question-answering benchmarks. Across models and datasets, accuracy improves with additional searches up to a small cap, hybrid lexical and dense retrieval with lightweight re-ranking produces the largest average gains in our ablation grid, and larger completion budgets are most helpful on HotpotQA-style synthesis. These results provide practical guidance for configuring budgeted agentic retrieval pipelines and are accompanied by reproducible prompts and evaluation settings.

</details>

---

### 11. [MultiGraSCCo: A Multilingual Anonymization Benchmark with Annotations of Personal Identifiers](https://arxiv.org/abs/2603.08879)

**基本信息**

- 🔗 arXiv: [`2603.08879`](https://arxiv.org/abs/2603.08879)
- 👥 作者: Ibrahim Baroud, Christoph Otto, Vera Czehmann 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08879.pdf)

**💡 相关性分析**

满足标准2：论文贡献了一个多语言的、包含个人信息标注的合成数据集（基准）。虽然其应用领域是文本匿名化，但该数据集作为“数据资源”，其构建方法（通过机器翻译生成高质量、跨语言、保留语义的合成数据）对于其他需要多语言或跨领域数据的研究具有参考价值。在化学信息学中，构建高质量、标注好的数据集（如质谱-结构对）是训练和评估模型的关键，此工作的方法论有借鉴意义。

**📖 中文摘要**

本研究创建了一个包含十种语言的多语言匿名化基准，使用了机器翻译方法来生成数据，同时保留了原始注释，并以文化和语境适当的形式呈现了城市和人名。该基准包含超过2500条个人信息的注释，可用于多种应用，包括训练标注员、跨机构验证注释以及帮助提高自动个人信息检测的性能。我们提供了基准和标注指南以供进一步研究。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accessing sensitive patient data for machine learning is challenging due to privacy concerns. Datasets with annotations of personally identifiable information are crucial for developing and testing anonymization systems to enable safe data sharing that complies with privacy regulations. Since accessing real patient data is a bottleneck, synthetic data offers an efficient solution for data scarcity, bypassing privacy regulations that apply to real data. Moreover, neural machine translation can help to create high-quality data for low-resource languages by translating validated real or synthetic data from a high-resource language. In this work, we create a multilingual anonymization benchmark in ten languages, using a machine translation methodology that preserves the original annotations and renders names of cities and people in a culturally and contextually appropriate form in each target language. Our evaluation study with medical professionals confirms the quality of the translations, both in general and with respect to the translation and adaptation of personal information. Our benchmark with over 2,500 annotations of personal information can be used in many applications, including training annotators, validating annotations across institutions without legal complications, and helping improve the performance of automatic personal information detection. We make our benchmark and annotation guidelines available for further research.

</details>

---

### 12. [ConFu: Contemplate the Future for Better Speculative Sampling](https://arxiv.org/abs/2603.08899)

**基本信息**

- 🔗 arXiv: [`2603.08899`](https://arxiv.org/abs/2603.08899)
- 👥 作者: Zongyue Qin, Raghavv Goel, Mukul Gagrani 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08899.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是大语言模型推理加速技术——推测解码的改进。这直接针对“大模型”的部署和效率优化。使化学大模型能够快速响应对交互式研究（如实时分子设计或光谱分析）至关重要。ConFu通过让草稿模型“展望未来”来提升加速效率，这是一种创新的模型优化思路。

**📖 中文摘要**

本文提出了ConFu（Contemplate the Future），一种新颖的推测解码框架，使草稿模型能够预测生成的未来方向。ConFu引入了（1）思考令牌和软提示，允许草稿模型以可忽略的成本利用来自目标模型的面向未来的信号；（2）具有MoE的动态思考令牌机制，以实现上下文感知的未来预测；（3）带有锚令牌采样和未来预测复制的训练框架，以学习鲁棒的未来预测。实验表明，ConFu在Llama-3 3B和8B模型的各种下游任务中，比EAGLE-3提高了8-11%的令牌接受率和生成速度。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Speculative decoding has emerged as a powerful approach to accelerate large language model (LLM) inference by employing lightweight draft models to propose candidate tokens that are subsequently verified by the target model. The effectiveness of this paradigm critically depends on the quality of the draft model. While recent advances such as the EAGLE series achieve state-of-the-art speedup, existing draft models remain limited by error accumulation: they condition only on the current prefix, causing their predictions to drift from the target model over steps. In this work, we propose \textbf{ConFu} (Contemplate the Future), a novel speculative decoding framework that enables draft models to anticipate the future direction of generation. ConFu introduces (i) contemplate tokens and soft prompts that allow the draft model to leverage future-oriented signals from the target model at negligible cost, (ii) a dynamic contemplate token mechanism with MoE to enable context-aware future prediction, and (iii) a training framework with anchor token sampling and future prediction replication that learns robust future prediction. Experiments demonstrate that ConFu improves token acceptance rates and generation speed over EAGLE-3 by 8--11% across various downstream tasks with Llama-3 3B and 8B models. We believe our work is the first to bridge speculative decoding with continuous reasoning tokens, offering a new direction for accelerating LLM inference.

</details>

---

### 13. [NetDiffuser: Deceiving DNN-Based Network Attack Detection Systems with Diffusion-Generated Adversarial Traffic](https://arxiv.org/abs/2603.08901)

**基本信息**

- 🔗 arXiv: [`2603.08901`](https://arxiv.org/abs/2603.08901)
- 👥 作者: Pratyay Kumar, Abu Saleh Md Tayeen, Satyajayant Misra 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08901.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是使用生成模型（扩散模型）为网络安全领域生成对抗样本。这直接涉及“大模型”（扩散模型）在特定领域的攻击性/安全性应用。虽然领域不同，但其核心技术——使用生成模型创建难以检测的、语义合理的扰动数据——与“化学大模型”可能面临的安全和鲁棒性挑战（例如，对抗性攻击导致分子性质预测错误）在方法论上相关。研究此类攻击有助于理解和防御未来化学AI系统的潜在漏洞。

**📖 中文摘要**

本文提出了NetDiffuser，一个用于生成能够欺骗基于深度学习的网络入侵检测系统（NIDS）的自然对抗样本（NAE）的新框架。NetDiffuser包含两个新颖组件：首先，一种新的特征分类算法，用于识别网络流量中相对独立的特征，扰动这些特征可以在保持网络流有效性的同时最小化变更。第二个组件是扩散模型的新应用，用于注入语义一致的扰动以生成NAE。NetDiffuser在三个基准NIDS数据集上进行了广泛评估，实验结果表明，与基线攻击相比，NetDiffuser实现了更高的攻击成功率，并显著降低了对抗样本检测性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Deep learning (DL)-based Network Intrusion Detection System (NIDS) has demonstrated great promise in detecting malicious network traffic. However, they face significant security risks due to their vulnerability to adversarial examples (AEs). Most existing adversarial attacks maliciously perturb data to maximize misclassification errors. Among AEs, natural adversarial examples (NAEs) are particularly difficult to detect because they closely resemble real data, making them challenging for both humans and machine learning models to distinguish from legitimate inputs. Creating NAEs is crucial for testing and strengthening NIDS defenses. This paper proposes NetDiffuser1, a novel framework for generating NAEs capable of deceiving NIDS. NetDiffuser consists of two novel components. First, a new feature categorization algorithm is designed to identify relatively independent features in network traffic. Perturbing these features minimizes changes while preserving network flow validity. The second component is a novel application of diffusion models to inject semantically consistent perturbations for generating NAEs. NetDiffuser performance was extensively evaluated using three benchmark NIDS datasets across various model architectures and state-of-the-art adversarial detectors. Our experimental results show that NetDiffuser achieves up to a 29.93% higher attack success rate and reduces AE detection performance by at least 0.267 (in some cases up to 0.534) in the Area under the Receiver Operating Characteristic Curve (AUC-ROC) score compared to the baseline attacks.

</details>

---

### 14. [Quantifying Memorization and Privacy Risks in Genomic Language Models](https://arxiv.org/abs/2603.08913)

**基本信息**

- 🔗 arXiv: [`2603.08913`](https://arxiv.org/abs/2603.08913)
- 👥 作者: Alexander Nemecek, Wenbiao Li, Xiaoqian Jiang 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08913.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕“大模型”（此处为基因组语言模型）的数据记忆与隐私风险展开，其方法论和评估框架可直接迁移并应用于“化学大模型”的安全性与隐私评估。

**📖 中文摘要**

本文研究了基因组语言模型（GLMs）中的记忆化与隐私风险。虽然论文的核心是基因组学，但其研究框架和方法论与化学信息学领域高度相关。论文系统地评估了GLMs如何记忆训练数据中的特定序列，并提出了一个多向量的隐私评估框架，用于量化记忆化风险。该框架集成了基于困惑度的检测、金丝雀序列提取和成员推理等方法。这项研究为评估和审计AI模型（包括潜在的化学大模型）的数据记忆和隐私泄露风险提供了一个通用且可复现的范例。论文提出的量化方法和评估流程，可以直接应用于评估化学大模型在训练过程中对分子结构、质谱数据等敏感信息的记忆程度，是构建安全、可信的化学AI系统的重要参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Genomic language models (GLMs) have emerged as powerful tools for learning representations of DNA sequences, enabling advances in variant prediction, regulatory element identification, and cross-task transfer learning. However, as these models are increasingly trained or fine-tuned on sensitive genomic cohorts, they risk memorizing specific sequences from their training data, raising serious concerns around privacy, data leakage, and regulatory compliance. Despite growing awareness of memorization risks in general-purpose language models, little systematic evaluation exists for these risks in the genomic domain, where data exhibit unique properties such as a fixed nucleotide alphabet, strong biological structure, and individual identifiability. We present a comprehensive, multi-vector privacy evaluation framework designed to quantify memorization risks in GLMs. Our approach integrates three complementary risk assessment methodologies: perplexity-based detection, canary sequence extraction, and membership inference. These are combined into a unified evaluation pipeline that produces a worst-case memorization risk score. To enable controlled evaluation, we plant canary sequences at varying repetition rates into both synthetic and real genomic datasets, allowing precise quantification of how repetition and training dynamics influence memorization. We evaluate our framework across multiple GLM architectures, examining the relationship between sequence repetition, model capacity, and memorization risk. Our results establish that GLMs exhibit measurable memorization and that the degree of memorization varies across architectures and training regimes. These findings reveal that no single attack vector captures the full scope of memorization risk, underscoring the need for multi-vector privacy auditing as a standard practice for genomic AI systems.

</details>

---

### 15. [bsort: A theoretically efficient non-comparison-based sorting algorithm for integer and floating-point numbers](https://arxiv.org/abs/2603.08929)

**基本信息**

- 🔗 arXiv: [`2603.08929`](https://arxiv.org/abs/2603.08929)
- 👥 作者: Benjamín Guzmán
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08929.pdf)

**💡 相关性分析**

满足标准2：论文提出了一种高效的数值排序算法（bsort），该算法可作为数据处理工具，用于优化化学信息学和质谱分析中大规模数值数据集（如分子特征、质谱峰）的预处理流程，从而支持相关模型的开发与应用。

**📖 中文摘要**

本文提出了一种名为bsort的非比较排序算法，适用于整数和浮点数。该算法通过一种源自二进制快速排序的方法，统一处理有符号/无符号整数和浮点数，实现了O(wn)的时间复杂度和O(w)的辅助空间复杂度，其中w是元素的字长。虽然论文本身属于算法研究，但其高效处理数值数据（包括浮点数）的能力，与科学计算和数据处理密切相关。在“化学信息学”和“质谱分析”中，经常需要处理海量的数值型数据，例如分子描述符、质谱峰强度、保留时间等。高效的数据排序和预处理是构建高性能分析管道和模型（包括大模型）的基础。bsort算法作为一种理论上高效且对特定数据类型（小字长）具有竞争力的工具，可以作为化学信息学数据处理工具箱中的一个潜在组件，用于优化数据预处理流程，从而间接支持化学大模型的训练和质谱数据的快速分析。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This paper presents bsort, a non-comparison-based sorting algorithm for signed and unsigned integers, and floating-point values. The algorithm unifies these cases through an approach derived from binary quicksort, achieving $O(wn)$ runtime asymptotic behavior and $O(w)$ auxiliary space, where $w$ is the element word size. This algorithm is highly efficient for data types with small word sizes, where empirical analysis exhibits performance competitive with highly optimized hybrid algorithms from popular libraries.

</details>

---

### 16. [PathoScribe: Transforming Pathology Data into a Living Library with a Unified LLM-Driven Framework for Semantic Retrieval and Clinical Integration](https://arxiv.org/abs/2603.08935)

**基本信息**

- 🔗 arXiv: [`2603.08935`](https://arxiv.org/abs/2603.08935)
- 👥 作者: Abdul Rehman Akbar, Samuel Wales-McGrath, Alejadro Levya 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08935.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文核心是构建一个基于LLM的领域智能检索与推理系统（PathoScribe），其架构和方法可直接类比并应用于化学信息学领域，构建用于分子、谱图、文献检索与推理的“化学大模型”系统。2) 论文提出的框架本身即是一个强大的工具原型，可用于管理和挖掘化学数据资源。

**📖 中文摘要**

本文介绍了PathoScribe，一个统一的检索增强大语言模型（LLM）框架，旨在将静态病理学档案转化为可搜索、可推理的“活体”知识库。该系统支持自然语言病例探索、自动队列构建、临床问答、免疫组化面板推荐和提示控制的报告转换。PathoScribe在70,000份多机构外科病理报告上进行了评估，在自然语言病例检索上实现了完美的Recall@10，并展示了高质量的检索增强推理能力。该框架的核心是LLM与领域专业知识的深度结合，以实现对复杂、非结构化医学数据的语义理解、检索和推理。这一范式与“化学大模型”和“质谱结构推理”的研究目标高度一致。在化学领域，同样存在海量的、非结构化的实验报告、文献、谱图数据。PathoScribe所展示的利用LLM构建领域特定智能检索与推理系统的能力，为在化学信息学中构建类似的系统（例如，基于自然语言查询检索相关分子合成路线、质谱解析案例或物化性质）提供了直接的技术蓝图和可行性证明。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Pathology underpins modern diagnosis and cancer care, yet its most valuable asset, the accumulated experience encoded in millions of narrative reports, remains largely inaccessible. Although institutions are rapidly digitizing pathology workflows, storing data without effective mechanisms for retrieval and reasoning risks transforming archives into a passive data repository, where institutional knowledge exists but cannot meaningfully inform patient care. True progress requires not only digitization, but the ability for pathologists to interrogate prior similar cases in real time while evaluating a new diagnostic dilemma. We present PathoScribe, a unified retrieval-augmented large language model (LLM) framework designed to transform static pathology archives into a searchable, reasoning-enabled living library. PathoScribe enables natural language case exploration, automated cohort construction, clinical question answering, immunohistochemistry (IHC) panel recommendation, and prompt-controlled report transformation within a single architecture. Evaluated on 70,000 multi-institutional surgical pathology reports, PathoScribe achieved perfect Recall@10 for natural language case retrieval and demonstrated high-quality retrieval-grounded reasoning (mean reviewer score 4.56/5). Critically, the system operationalized automated cohort construction from free-text eligibility criteria, assembling research-ready cohorts in minutes (mean 9.2 minutes) with 91.3% agreement to human reviewers and no eligible cases incorrectly excluded, representing orders-of-magnitude reductions in time and cost compared to traditional manual chart review. This work establishes a scalable foundation for converting digital pathology archives from passive storage systems into active clinical intelligence platforms.

</details>

---

### 17. [GenAI Is No Silver Bullet for Qualitative Research in Software Engineering](https://arxiv.org/abs/2603.08951)

**基本信息**

- 🔗 arXiv: [`2603.08951`](https://arxiv.org/abs/2603.08951)
- 👥 作者: Neil A. Ernst, Christoph Treude
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08951.pdf)

**💡 相关性分析**

满足标准3：论文是对“生成式AI（作为大模型的一种体现）在定性研究中的应用”的综述与展望，包含了重要的相关讨论。这些讨论直接适用于化学信息学与质谱分析领域的研究者，指导他们如何利用大模型进行文献分析、知识发现和未来方向展望。

**📖 中文摘要**

本文探讨了生成式人工智能（GenAI）在软件工程定性研究中的应用、承诺与陷阱。论文认为，GenAI并非定性研究的“银弹”，必须根据具体的研究策略和数据特征进行谨慎调整。作者回顾了GenAI在软件工程中使用的经验证据，分析了GenAI介导的定性研究实践的利弊，并重新审视了定性研究质量因素。虽然论文背景是软件工程，但其对“GenAI辅助定性研究”的批判性分析和框架性讨论具有高度的普遍性。在“化学信息学”和“质谱分析”领域，研究同样大量依赖对文献、实验记录、专家知识的定性分析来提出假设、总结规律、进行展望。本文系统地评估了GenAI（作为大模型的一种应用形式）在此类分析任务中的能力边界、风险（如产生幻觉、过度泛化）和有效使用模式，为化学领域的研究者如何负责任且有效地利用大模型工具进行文献综述、假设生成、研究展望等工作提供了至关重要的方法论指导和风险警示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Qualitative research gives rich insights into the quintessentially human aspects of software engineering as a socio-technical system. Qualitative research spans diverse strategies and methods, from interpretivist, in situ observational field studies, to deductive coding of data from mining studies. Advances in large language models and generative AI (GenAI) have prompted claims that artificial intelligence could automate qualitative analysis. Such claims are overgeneralizing from narrow successes. GenAI support must be carefully adapted to the data of interest, but also to the characteristics of a particular research strategy. In this Frontiers of SE paper, we discuss the emerging use of GenAI in relation to the broad spectrum of qualitative research in software engineering. We outline the dimensions of qualitative work in software engineering, review emerging empirical evidence for GenAI assistance, examine the pros and cons of GenAI-mediated qualitative research practices, and revisit qualitative research quality factors, in light of GenAI. Our goal is to inform researchers about the promises and pitfalls of GenAI-assisted qualitative research. We conclude with future plans to advance understanding of its use in software engineering.

</details>

---

### 18. [Automated Tensor-Relational Decomposition for Large-Scale Sparse Tensor Computation](https://arxiv.org/abs/2603.08957)

**基本信息**

- 🔗 arXiv: [`2603.08957`](https://arxiv.org/abs/2603.08957)
- 👥 作者: Yuxin Tang, Zhiyuan Xin, Zhimin Ding 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08957.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于自动化优化张量计算的框架（EinSum），该工具可用于高效处理化学信息学和质谱分析中常见的大规模、稀疏张量数据，从而支持相关模型（包括大模型）的训练与推理。

**📖 中文摘要**

本文介绍了EinSum，一种张量-关系计算版本的爱因斯坦求和符号。论文研究了如何将爱因斯坦符号表示的计算自动重写为EinSum，以便使用高效数值内核执行计算密集型组件，同时利用关系系统管理稀疏性。张量计算是机器学习和科学计算的核心，而“化学大模型”（尤其是涉及分子结构、相互作用预测的模型）和“质谱结构推理”中的许多算法（如张量分解用于谱图分析、图神经网络中的消息传递）都涉及复杂的张量操作。本文提出的EinSum框架，旨在自动化地优化张量计算在混合（关系型+数值型）数据环境下的执行，这对于处理化学中常见的大规模、稀疏、高维张量数据（如分子构象空间、高通量筛选数据、质谱成像数据）具有潜在的重要价值。该工作为构建高效、可扩展的化学信息学计算引擎提供了新的思路和工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A \emph{tensor-relational} computation is a relational computation where individual tuples carry vectors, matrices, or higher-dimensional arrays. An advantage of tensor-relational computation is that the overall computation can be executed on top of a relational system, inheriting the system's ability to automatically handle very large inputs with high levels of sparsity while high-performance kernels (such as optimized matrix-matrix multiplication codes) can be used to perform most of the underlying mathematical operations. In this paper, we introduce upper-case-lower-case \texttt{EinSum}, which is a tensor-relational version of the classical Einstein Summation Notation. We study how to automatically rewrite a computation in Einstein Notation into upper-case-lower-case \texttt{EinSum} so that computationally intensive components are executed using efficient numerical kernels, while sparsity is managed relationally.

</details>

---

### 19. [Semantic Level of Detail: Multi-Scale Knowledge Representation via Heat Kernel Diffusion on Hyperbolic Manifolds](https://arxiv.org/abs/2603.08965)

**基本信息**

- 🔗 arXiv: [`2603.08965`](https://arxiv.org/abs/2603.08965)
- 👥 作者: Edward Izgorodin
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08965.pdf)

**💡 相关性分析**

满足标准1：论文提出的语义细节层次（SLoD）框架，专注于为图结构知识提供连续的多尺度表示，其方法可直接应用于化学知识图谱（如分子结构层次、反应网络）和质谱-结构关联图的表示学习，是构建具有层次化推理能力的化学大模型的核心技术。

**📖 中文摘要**

本文提出了语义细节层次（SLoD）框架，通过在双曲流形（庞加莱球）上进行热核扩散，为知识图等图结构提供连续的多尺度知识表示。该框架定义了一个连续的“缩放”操作：在粗尺度上，扩散将嵌入聚合为高级摘要；在细尺度上，则保留局部语义细节。论文证明了该方法在树状层次结构下的层次一致性，并展示了图拉普拉斯算子的谱间隙会诱导出 emergent scale boundaries（表示发生定性转变的尺度），这些边界可以被自动检测。该方法在WordNet名词层次结构上进行了验证。该研究直接关联“化学大模型”和“质谱结构推理”中的核心问题：如何对化学知识（如分子层次结构、反应网络、谱图-结构关联）进行多尺度、可解释的表示与推理。SLoD框架提供了一种数学上严谨的方法，可以在一个统一的嵌入空间中，实现从原子/官能团级别到分子/反应类型级别的平滑语义缩放，这对于构建能够理解不同抽象层次化学概念的大模型至关重要。同时，自动检测语义边界的能力有助于发现质谱特征与分子子结构之间的隐含层次关系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

AI memory systems increasingly organize knowledge into graph structures -- knowledge graphs, entity relations, community hierarchies -- yet lack a principled mechanism for continuous resolution control: where do the qualitative boundaries between abstraction levels lie, and how should an agent navigate them? We introduce Semantic Level of Detail (SLoD), a framework that answers both questions by defining a continuous zoom operator via heat kernel diffusion on the Poincaré ball $\mathbb{B}^d$. At coarse scales ($\sigma \to \infty$), diffusion aggregates embeddings into high-level summaries; at fine scales ($\sigma \to 0$), local semantic detail is preserved. We prove hierarchical coherence with bounded approximation error $O(\sigma)$ and $(1+\varepsilon)$ distortion for tree-structured hierarchies under Sarkar embedding. Crucially, we show that spectral gaps in the graph Laplacian induce emergent scale boundaries -- scales where the representation undergoes qualitative transitions -- which can be detected automatically without manual resolution parameters. On synthetic hierarchies (HSBM), our boundary scanner recovers planted levels with ARI up to 1.00, with detection degrading gracefully near the information-theoretic Kesten-Stigum threshold. On the full WordNet noun hierarchy (82K synsets), detected boundaries align with true taxonomic depth ($\tau = 0.79$), demonstrating that the method discovers meaningful abstraction levels in real-world knowledge graphs without supervision.

</details>

---

### 20. [Automated Thematic Analysis for Clinical Qualitative Data: Iterative Codebook Refinement with Full Provenance](https://arxiv.org/abs/2603.08989)

**基本信息**

- 🔗 arXiv: [`2603.08989`](https://arxiv.org/abs/2603.08989)
- 👥 作者: Seungjun Yi, Joakim Nguyen, Huimin Xu 等12人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08989.pdf)

**💡 相关性分析**

满足标准2和3：2) 论文提出了一个基于LLM的自动化主题分析框架，该工具可用于从化学文献、实验报告等文本数据中提取知识、构建数据集，支持化学大模型的训练与评估。3) 该框架本身可用于生成领域综述，或辅助进行化学信息学与质谱分析领域的趋势分析与展望。

**📖 中文摘要**

本文提出了一个结合迭代码本优化和完整溯源跟踪的自动化主题分析（TA）框架，用于处理临床定性数据。该框架利用LLM实现自动化，并在五个包含临床访谈、社交媒体和公开转录本的数据集上进行了评估，在四个数据集上取得了最高的综合质量分数。迭代优化在四个数据集上带来了统计显著的改进。这项研究展示了LLM在自动化、可扩展地分析复杂领域文本数据（如患者访谈、临床记录）方面的强大能力。在“化学信息学”和“质谱分析”领域，同样存在大量非结构化的文本数据，如科研论文、实验记录、专利文档、仪器日志等。从这些文本中自动提取主题、趋势、方法总结和未来展望，是驱动领域发展和大模型知识更新的关键。本文提出的自动化TA框架，为化学领域研究者提供了一个现成的、经过验证的工具和方法论，可以用于从海量化学文献中系统地挖掘研究主题、技术演进路径和未解决问题，从而直接支持“化学大模型”的知识构建和“质谱结构推理”领域的综述与展望工作。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Thematic analysis (TA) is widely used in health research to extract patterns from patient interviews, yet manual TA faces challenges in scalability and reproducibility. LLM-based automation can help, but existing approaches produce codebooks with limited generalizability and lack analytic auditability. We present an automated TA framework combining iterative codebook refinement with full provenance tracking. Evaluated on five corpora spanning clinical interviews, social media, and public transcripts, the framework achieves the highest composite quality score on four of five datasets compared to six baselines. Iterative refinement yields statistically significant improvements on four datasets with large effect sizes, driven by gains in code reusability and distributional consistency while preserving descriptive quality. On two clinical corpora (pediatric cardiology), generated themes align with expert-annotated themes.

</details>

---

### 21. [Meissa: Multi-modal Medical Agentic Intelligence](https://arxiv.org/abs/2603.09018)

**基本信息**

- 🔗 arXiv: [`2603.09018`](https://arxiv.org/abs/2603.09018)
- 👥 作者: Yixiong Chen, Xinyi Bai, Yue Pan 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09018.pdf)

**💡 相关性分析**

满足标准1：论文核心是构建一个轻量级、可离线部署的领域专业多模态大模型代理（Meissa）。其通过轨迹蒸馏实现代理能力的方法论，为在化学信息学和质谱分析领域开发类似的、能够进行复杂推理和工具调用的“化学大模型代理”提供了直接的技术路径和成功案例。

**📖 中文摘要**

本文提出了Meissa，一个轻量级的40亿参数医学多模态大语言模型（MM-LLM），旨在实现离线代理能力。Meissa通过从前沿模型（如GPT）中蒸馏结构化的轨迹（推理和行动轨迹），学习何时进行外部交互（策略选择）以及如何执行多步交互（策略执行）。论文提出了统一轨迹建模、三层分层监督和前瞻-回顾监督等方法。Meissa在13个医学基准测试的16个评估设置中，有10个匹配或超过了专有前沿代理的性能。这项研究是“大模型”在垂直领域（医学）轻量化、代理化部署的典范。其技术路线——通过轨迹蒸馏将复杂推理和工具使用能力注入一个更小、可离线部署的模型——对于“化学大模型”和“质谱结构推理”具有极高的参考价值。化学领域同样需要能够调用计算工具（如量子化学计算、数据库查询）、进行多步推理（如逆合成分析、谱图解析）的代理系统。Meissa证明了构建此类轻量化、可部署的领域专业代理是可行的，为化学AI代理的开发提供了完整的技术蓝图和实证支持。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multi-modal large language models (MM-LLMs) have shown strong performance in medical image understanding and clinical reasoning. Recent medical agent systems extend them with tool use and multi-agent collaboration, enabling complex decision-making. However, these systems rely almost entirely on frontier models (e.g., GPT), whose API-based deployment incurs high cost, high latency, and privacy risks that conflict with on-premise clinical requirements. We present Meissa, a lightweight 4B-parameter medical MM-LLM that brings agentic capability offline. Instead of imitating static answers, Meissa learns both when to engage external interaction (strategy selection) and how to execute multi-step interaction (strategy execution) by distilling structured trajectories from frontier models. Specifically, we propose: (1) Unified trajectory modeling: trajectories (reasoning and action traces) are represented within a single state-action-observation formalism, allowing one model to generalize across heterogeneous medical environments. (2) Three-tier stratified supervision: the model's own errors trigger progressive escalation from direct reasoning to tool-augmented and multi-agent interaction, explicitly learning difficulty-aware strategy selection. (3) Prospective-retrospective supervision: pairing exploratory forward traces with hindsight-rationalized execution traces enables stable learning of effective interaction policies. Trained on 40K curated trajectories, Meissa matches or exceeds proprietary frontier agents in 10 of 16 evaluation settings across 13 medical benchmarks spanning radiology, pathology, and clinical reasoning. Using over 25x fewer parameters than typical frontier models like Gemini-3, Meissa operates fully offline with 22x lower end-to-end latency compared to API-based deployment. Data, models, and environments are released at this https URL .

</details>

---

### 22. [Reading, Not Thinking: Understanding and Bridging the Modality Gap When Text Becomes Pixels in Multimodal LLMs](https://arxiv.org/abs/2603.09095)

**基本信息**

- 🔗 arXiv: [`2603.09095`](https://arxiv.org/abs/2603.09095)
- 👥 作者: Kaiser Sun, Xiaochuang Yuan, Hongjun Liu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09095.pdf)

**💡 相关性分析**

满足标准1：论文核心研究多模态大语言模型（MLLMs）处理图像文本的“模态差距”问题，并提出了改进方案。该问题直接关系到化学大模型能否准确理解化学结构图、谱图、文献图表中的信息，是构建可靠化学多模态大模型必须解决的关键挑战。

**📖 中文摘要**

本文系统地诊断了多模态大语言模型（MLLMs）在处理图像形式文本时存在的“模态差距”问题。论文评估了七个MLLM在五种输入模式下的表现，发现模态差距是任务和数据依赖的，渲染选择（如字体、分辨率）是强混淆因素。通过分析4000多个样本，论文揭示了图像模式选择性地放大了阅读错误，而知识和推理错误基本不变。基于此，论文提出了一种自蒸馏方法，使用模型自身的纯文本推理轨迹与图像输入进行配对训练，显著提升了图像模式下的准确率，并能迁移到未见过的基准测试上。这项研究直接关联“化学大模型”和“质谱结构推理”中的实际问题：化学领域有大量信息以图像形式存在，如化学结构图、图表、谱图（质谱、核磁等）、论文中的表格和公式。MLLMs需要准确“读懂”这些图像中的文本和符号信息。本文不仅深入剖析了MLLMs在此任务上的失败模式，还提出了有效的改进方案（自蒸馏）。这对于开发能够可靠处理化学文档、谱图报告图像的化学多模态大模型至关重要，是提升“质谱结构推理”等任务中信息提取准确性的关键。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal large language models (MLLMs) can process text presented as images, yet they often perform worse than when the same content is provided as textual tokens. We systematically diagnose this "modality gap" by evaluating seven MLLMs across seven benchmarks in five input modes, spanning both synthetically rendered text and realistic document images from arXiv PDFs to Wikipedia pages. We find that the modality gap is task- and data-dependent. For example, math tasks degrade by over 60 points on synthetic renderings, while natural document images often match or exceed text-mode performance. Rendering choices such as font and resolution are strong confounds, with font alone swinging accuracy by up to 47 percentage points. To understand this, we conduct a grounded-theory error analysis of over 4,000 examples, revealing that image mode selectively amplifies reading errors (calculation and formatting failures) while leaving knowledge and reasoning errors largely unchanged, and that some models exhibit a chain-of-thought reasoning collapse under visual input. Motivated by these findings, we propose a self-distillation method that trains the model on its own pure text reasoning traces paired with image inputs, raising image-mode accuracy on GSM8K from 30.71% to 92.72% and transferring to unseen benchmarks without catastrophic forgetting. Overall, our study provides a systematic understanding of the modality gap and suggests a practical path toward improving visual text understanding in multimodal language models.

</details>

---

### 23. [MedKCO: Medical Vision-Language Pretraining via Knowledge-Driven Cognitive Orchestration](https://arxiv.org/abs/2603.09101)

**基本信息**

- 🔗 arXiv: [`2603.09101`](https://arxiv.org/abs/2603.09101)
- 👥 作者: Chenran Zhang, Ruiqi Wu, Tao Zhou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09101.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种改进视觉-语言预训练的方法（MedKCO），其基于课程学习和自适应对比损失的认知编排策略，可直接应用于化学多模态数据（如分子图-文本、质谱图-结构）的预训练，以优化“化学大模型”和“质谱结构推理”基础模型的性能。

**📖 中文摘要**

本文提出了MedKCO，一种通过知识驱动认知编排进行的医学视觉-语言预训练方法。该方法设计了一个两级课程，结合诊断敏感性和类内样本代表性来排序预训练数据。此外，考虑到医学图像的类间相似性，引入了一种自步长非对称对比损失来动态调整预训练目标的参与度。该方法在多个视觉-语言下游任务中的三个医学成像场景上进行了评估。虽然论文聚焦医学影像，但其核心思想——通过课程学习（由易到难的数据排序）和自适应对比损失来优化视觉-语言预训练——具有普遍意义。在“化学大模型”和“质谱结构推理”的预训练中，同样面临数据异构、概念复杂度不一、类间相似性高（如结构相似的分子、谱图相似的化合物）等挑战。MedKCO提出的认知编排策略，为如何更有效地组织化学多模态数据（分子结构图、质谱图、文本描述）进行预训练，以学习到更鲁棒、更具泛化能力的表示，提供了创新的解决方案。其方法可以直接迁移到化学领域，用于训练更好的化学视觉-语言基础模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Medical vision-language pretraining (VLP) models have recently been investigated for their generalization to diverse downstream tasks. However, current medical VLP methods typically force the model to learn simple and complex concepts simultaneously. This anti-cognitive process leads to suboptimal feature representations, especially under distribution shift. To address this limitation, we propose a Knowledge-driven Cognitive Orchestration for Medical VLP (MedKCO) that involves both the ordering of the pretraining data and the learning objective of vision-language contrast. Specifically, we design a two level curriculum by incorporating diagnostic sensitivity and intra-class sample representativeness for the ordering of the pretraining data. Moreover, considering the inter-class similarity of medical images, we introduce a self-paced asymmetric contrastive loss to dynamically adjust the participation of the pretraining objective. We evaluate the proposed pretraining method on three medical imaging scenarios in multiple vision-language downstream tasks, and compare it with several curriculum learning methods. Extensive experiments show that our method significantly surpasses all baselines. this https URL .

</details>

---

### 24. [VIVID-Med: LLM-Supervised Structured Pretraining for Deployable Medical ViTs](https://arxiv.org/abs/2603.09109)

**基本信息**

- 🔗 arXiv: [`2603.09109`](https://arxiv.org/abs/2603.09109)
- 👥 作者: Xiyao Wang, Xiaoyu Tan, Yang Dai 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09109.pdf)

**💡 相关性分析**

满足标准1和2：1) 论文提出了一个利用LLM蒸馏训练视觉编码器的框架（VIVID-Med），该范式可直接应用于化学领域，用于训练基于分子结构图或质谱图的专用视觉编码器，服务于“化学大模型”的视觉分支或“质谱结构推理”任务。2) 该框架提供了一种从LLM中提取结构化知识以构建高质量化学视觉数据集的工具和方法。

**📖 中文摘要**

本文介绍了VIVID-Med，一个利用冻结的大语言模型（LLM）作为结构化语义教师来预训练医学视觉Transformer（ViTs）的新框架。VIVID-Med通过统一医学模式（UMS）将临床发现转化为可验证的JSON字段-状态对，并采用可回答性感知掩码进行优化。它使用结构化预测分解（SPD）将交叉注意力划分为正交正则化的查询组，以提取互补的视觉方面。关键的是，训练后丢弃LLM，得到一个轻量级、可部署的纯ViT骨干网络。该框架在多个任务上表现出色，包括线性探测、零样本跨域迁移和跨模态泛化。这项研究为在资源受限的临床环境中部署高性能视觉模型提供了高效、可扩展的替代方案。其“LLM作为教师，训练后丢弃”的范式对“化学大模型”和“质谱结构推理”极具启发性。在化学领域，可以利用一个强大的化学LLM（或通用LLM结合化学知识）作为教师，为分子图像、谱图等视觉数据生成高质量的结构化语义标签（如官能团、谱图特征描述），从而预训练一个强大的、可独立部署的化学视觉编码器。这种方法既能利用LLM的丰富知识，又能避免在推理时依赖沉重的LLM，非常适合构建高效、专用于谱图分类、分子属性预测的嵌入式模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Vision-language pretraining has driven significant progress in medical image analysis. However, current methods typically supervise visual encoders using one-hot labels or free-form text, neither of which effectively captures the complex semantic relationships among clinical findings. In this study, we introduce VIVID-Med, a novel framework that leverages a frozen large language model (LLM) as a structured semantic teacher to pretrain medical vision transformers (ViTs). VIVID-Med translates clinical findings into verifiable JSON field-state pairs via a Unified Medical Schema (UMS), utilizing answerability-aware masking to focus optimization. It then employs Structured Prediction Decomposition (SPD) to partition cross-attention into orthogonality-regularized query groups, extracting complementary visual aspects. Crucially, the LLM is discarded post-training, yielding a lightweight, deployable ViT-only backbone. We evaluated VIVID-Med across multiple settings: on CheXpert linear probing, it achieves a macro-AUC of 0.8588, outperforming BiomedCLIP by +6.65 points while using 500x less data. It also demonstrates robust zero-shot cross-domain transfer to NIH ChestX-ray14 (0.7225 macro-AUC) and strong cross-modality generalization to CT, achieving 0.8413 AUC on LIDC-IDRI lung nodule classification and 0.9969 macro-AUC on OrganAMNIST 11-organ classification. VIVID-Med offers a highly efficient, scalable alternative to deploying resource-heavy vision-language models in clinical settings.

</details>

---

### 25. [Better Bounds for the Distributed Experts Problem](https://arxiv.org/abs/2603.09168)

**基本信息**

- 🔗 arXiv: [`2603.09168`](https://arxiv.org/abs/2603.09168)
- 👥 作者: David P. Woodruff, Samson Zhou
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09168.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容直接围绕‘化学大模型’主题，提出了一个用于理性分子设计的可进化推理引擎（Logos），这是一个专门为分子科学设计的AI模型。

**📖 中文摘要**

论文《Logos: An evolvable reasoning engine for rational molecular design》提出了一种名为Logos的紧凑型分子推理模型，旨在实现可靠且可解释的分子设计。该模型通过多步逻辑推理与严格的化学一致性相结合，采用分阶段训练策略：首先让模型学习从分子描述到结构决策的显式推理示例，然后逐步将这些推理模式与分子表示对齐。在最终训练阶段，化学规则和不变性被直接纳入优化目标，引导模型生成化学上有效的输出。该工作明确展示了中间推理步骤，使人类能够检查和评估每个生成结构背后的设计逻辑。这项研究为分子科学中可靠且可解释的人工智能系统提供了一条实用路径，支持人工智能更紧密地融入科学发现过程。该论文的核心是开发一个用于“理性分子设计”的推理引擎，这直接涉及使用人工智能模型（化学大模型）进行分子结构的生成与推理，与“化学大模型”和“质谱结构推理”（作为分子结构推理的一种具体应用场景）的核心主题高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this paper, we study the distributed experts problem, where $n$ experts are distributed across $s$ servers for $T$ timesteps. The loss of each expert at each time $t$ is the $\ell_p$ norm of the vector that consists of the losses of the expert at each of the $s$ servers at time $t$. The goal is to minimize the regret $R$, i.e., the loss of the distributed protocol compared to the loss of the best expert, amortized over the all $T$ times, while using the minimum amount of communication. We give a protocol that achieves regret roughly $R\gtrsim\frac{1}{\sqrt{T}\cdot\text{poly}\log(nsT)}$, using $\mathcal{O}\left(\frac{n}{R^2}+\frac{s}{R^2}\right)\cdot\max(s^{1-2/p},1)\cdot\text{poly}\log(nsT)$ bits of communication, which improves on previous work.

</details>

---

### 26. [The Radio-Frequency Transformer for Signal Separation](https://arxiv.org/abs/2603.09201)

**基本信息**

- 🔗 arXiv: [`2603.09201`](https://arxiv.org/abs/2603.09201)
- 👥 作者: Egor Lifar, Semyon Savkin, Rachana Madhukara 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09201.pdf)

**💡 相关性分析**

满足标准1：论文的核心是开发一个基于Transformer的、数据驱动的模型，用于从复杂背景中分离和识别特定信号。虽然应用领域是射频通信，但其解决“从混合物中推理目标结构”的方法论与“质谱结构推理”的核心任务（从复杂质谱数据中解析化合物）在本质上高度相关，可视为该主题的方法论研究。

**📖 中文摘要**

论文《The Radio-Frequency Transformer for Signal Separation》研究信号分离问题：从未知的非高斯背景/干扰中估计目标信号。作者提出了一种完全数据驱动的信号分离器构建方法。具体而言，他们为目标信号学习了一个良好的离散标记器，然后基于交叉熵损失训练一个端到端的Transformer模型。与传统的均方误差相比，使用交叉熵训练显示出显著的改进。该标记器是谷歌SoundStream的修改版本，结合了额外的Transformer层，并从VQVAE切换到有限标量量化。该方法在MIT RF挑战数据集的真实和合成混合物上进行了评估，取得了有竞争力的性能，包括在将QPSK信号与5G干扰分离时，误码率比现有技术降低了122倍。学习的表示能够适应干扰类型，并在推理时对未见过的混合物表现出零样本泛化能力。虽然该方法实例化于射频混合物，但作者预期相同的架构也适用于引力波数据（如LIGO应变）和其他需要背景和噪声数据驱动建模的科学传感问题。这项工作本质上是在开发一个基于Transformer的、数据驱动的模型，用于从复杂混合物中分离和识别特定信号（如QPSK信号），这与“质谱结构推理”中从复杂质谱数据中解析出目标化合物信号的核心挑战在方法论上高度相似。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We study a problem of signal separation: estimating a signal of interest (SOI) contaminated by an unknown non-Gaussian background/interference. Given the training data consisting of examples of SOI and interference, we show how to build a fully data-driven signal separator. To that end we learn a good discrete tokenizer for SOI and then train an end-to-end transformer on a cross-entropy loss. Training with a cross-entropy shows substantial improvements over the conventional mean-squared error (MSE). Our tokenizer is a modification of Google's SoundStream, which incorporates additional transformer layers and switches from VQVAE to finite-scalar quantization (FSQ). Across real and synthetic mixtures from the MIT RF Challenge dataset, our method achieves competitive performance, including a 122x reduction in bit-error rate (BER) over prior state-of-the-art techniques for separating a QPSK signal from 5G interference. The learned representation adapts to the interference type without side information and shows zero-shot generalization to unseen mixtures at inference time, underscoring its potential beyond RF. Although we instantiate our approach on radio-frequency mixtures, we expect the same architecture to apply to gravitational-wave data (e.g., LIGO strain) and other scientific sensing problems that require data-driven modeling of background and noise.

</details>

---

### 27. [ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph](https://arxiv.org/abs/2603.09266)

**基本信息**

- 🔗 arXiv: [`2603.09266`](https://arxiv.org/abs/2603.09266)
- 👥 作者: Junhao Cai, Deyu Zeng, Junhao Pang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09266.pdf)

**💡 相关性分析**

满足标准1：论文的主要研究内容是针对工业应用的文本到3D生成，这直接涉及使用AI模型（大模型）进行分子或材料结构的生成与设计，是“化学大模型”在生成式AI和结构设计方面的具体应用。

**📖 中文摘要**

论文《ForgeDreamer: Industrial Text-to-3D Generation with Multi-Expert LoRA and Cross-View Hypergraph》针对工业文本到3D生成任务，提出了一个名为ForgeDreamer的新框架。该框架解决了两个关键限制：1）领域适应挑战，其中传统的LoRA融合会导致跨类别知识干扰；2）几何推理缺陷，其中成对一致性约束无法捕获对精密制造至关重要的高阶结构依赖性。该论文通过两个关键创新来解决这些挑战：首先，引入多专家LoRA集成机制，将多个特定类别的LoRA模型整合到一个统一的表示中，在消除知识干扰的同时实现卓越的跨类别泛化。其次，在增强的语义理解基础上，开发了一种跨视图超图几何增强方法，可同时捕获跨越多个视点的结构依赖性。这些组件协同工作，实现了改进的语义理解和更有效的几何推理。该工作专注于为工业应用生成精确的3D分子/材料结构，这属于“化学大模型”在分子和材料设计领域的一个重要应用方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Current text-to-3D generation methods excel in natural scenes but struggle with industrial applications due to two critical limitations: domain adaptation challenges where conventional LoRA fusion causes knowledge interference across categories, and geometric reasoning deficiencies where pairwise consistency constraints fail to capture higher-order structural dependencies essential for precision manufacturing. We propose a novel framework named ForgeDreamer addressing both challenges through two key innovations. First, we introduce a Multi-Expert LoRA Ensemble mechanism that consolidates multiple category-specific LoRA models into a unified representation, achieving superior cross-category generalization while eliminating knowledge interference. Second, building on enhanced semantic understanding, we develop a Cross-View Hypergraph Geometric Enhancement approach that captures structural dependencies spanning multiple viewpoints simultaneously. These components work synergistically improved semantic understanding, enables more effective geometric reasoning, while hypergraph modeling ensures manufacturing-level consistency. Extensive experiments on a custom industrial dataset demonstrate superior semantic generalization and enhanced geometric fidelity compared to state-of-the-art approaches. Our code and data are provided in the supplementary material attached in the appendix for review purposes.

</details>

---

### 28. [Learning Convex Decomposition via Feature Fields](https://arxiv.org/abs/2603.09285)

**基本信息**

- 🔗 arXiv: [`2603.09285`](https://arxiv.org/abs/2603.09285)
- 👥 作者: Yuezhi Yang, Qixing Huang, Mikaela Angelina Uy 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09285.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种基于学习特征场的几何结构分解方法。虽然应用场景是3D形状，但其核心是开发一个AI模型来学习和推理复杂对象的内部结构组成，这与“化学大模型”和“质谱结构推理”中关于分子结构表示、分解与推理的核心主题在方法论层面高度相关。

**📖 中文摘要**

论文《Learning Convex Decomposition via Feature Fields》提出了一种通过学习特征场进行凸分解的新方法，实现了首个用于开放世界凸分解的前馈模型。该方法将3D形状分解为凸体的并集，这对于加速物理模拟中的碰撞检测等应用至关重要。关键见解是采用特征学习方法，学习一个连续特征场，然后通过从凸性经典定义推导出的自监督、纯几何目标进行聚类，从而产生良好的凸分解。该公式可用于单形状优化，但更重要的是，特征预测实现了在大规模数据集上的可扩展、自监督学习，从而产生了首个用于凸分解的开放世界学习模型。实验表明，该方法的分解质量高于替代方案，并且能够泛化到开放世界对象以及不同的表示形式（如网格、CAD模型甚至高斯溅射）。这项工作展示了如何利用学习到的特征场来解决复杂的几何结构推理问题，其“从数据中学习结构表示并进行分解”的核心思想与“化学大模型”中学习分子表示并推理其结构组分，以及“质谱结构推理”中从谱图数据反推分子结构碎片的思想有相通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work proposes a new formulation to the long-standing problem of convex decomposition through learning feature fields, enabling the first feed-forward model for open-world convex decomposition. Our method produces high-quality decompositions of 3D shapes into a union of convex bodies, which are essential to accelerate collision detection in physical simulation, amongst many other applications. The key insight is to adopt a feature learning approach and learn a continuous feature field that can later be clustered to yield a good convex decomposition via our self-supervised, purely-geometric objective derived from the classical definition of convexity. Our formulation can be used for single shape optimization, but more importantly, feature prediction unlocks scalable, self-supervised learning on large datasets resulting in the first learned open-world model for convex decomposition. Experiments show that our decompositions are higher-quality than alternatives and generalize across open-world objects as well as across representations to meshes, CAD models, and even Gaussian splats. this https URL

</details>

---

### 29. [Reward-Zero: Language Embedding Driven Implicit Reward Mechanisms for Reinforcement Learning](https://arxiv.org/abs/2603.09331)

**基本信息**

- 🔗 arXiv: [`2603.09331`](https://arxiv.org/abs/2603.09331)
- 👥 作者: Heng Zhang, Haddy Alchaer, Arash Ajoudani 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09331.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一种利用语言嵌入（可视为一种语言/化学信息学模型）来生成强化学习奖励信号的通用机制。虽然应用领域是强化学习，但其核心方法（语言嵌入的语义比较与信号生成）与构建和利用“化学大模型”进行信息推理（例如，从文本描述中推断化学性质或反应结果）在方法论上高度相关，都属于利用高级语义模型（大模型）从非结构化或半结构化输入中生成结构化输出或信号的范畴。

**📖 中文摘要**

本文提出了Reward-Zero，一种通用的隐式奖励机制，可将自然语言任务描述转化为密集的、基于语义的进度信号，用于强化学习（RL）。Reward-Zero作为一个简单而复杂的通用奖励函数，利用语言嵌入进行高效的RL训练。通过比较任务规范的嵌入与从智能体交互经验中导出的嵌入，Reward-Zero产生一个连续的、语义对齐的完成感信号。该奖励补充了稀疏或延迟的环境反馈，无需特定于任务的工程。当集成到标准RL框架中时，它加速了探索，稳定了训练，并增强了跨不同任务的泛化能力。从经验上看，使用Reward-Zero训练的智能体比使用PPO等传统方法和常见奖励塑造基线的智能体收敛更快，最终成功率更高，成功解决了某些复杂任务中手工设计奖励无法解决的问题。此外，作者还开发了一个通过语言嵌入评估任务执行过程中完成感的小型基准。这些结果凸显了语言驱动的隐式奖励函数作为实现更样本高效、可泛化和可扩展的具身智能体RL的实用路径的前景。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Reward-Zero, a general-purpose implicit reward mechanism that transforms natural-language task descriptions into dense, semantically grounded progress signals for reinforcement learning (RL). Reward-Zero serves as a simple yet sophisticated universal reward function that leverages language embeddings for efficient RL training. By comparing the embedding of a task specification with embeddings derived from an agent's interaction experience, Reward-Zero produces a continuous, semantically aligned sense-of-completion signal. This reward supplements sparse or delayed environmental feedback without requiring task-specific engineering. When integrated into standard RL frameworks, it accelerates exploration, stabilizes training, and enhances generalization across diverse tasks. Empirically, agents trained with Reward-Zero converge faster and achieve higher final success rates than conventional methods such as PPO with common reward-shaping baselines, successfully solving tasks that hand-designed rewards could not in some complex tasks. In addition, we develop a mini benchmark for the evaluation of completion sense during task execution via language embeddings. These results highlight the promise of language-driven implicit reward functions as a practical path toward more sample-efficient, generalizable, and scalable RL for embodied agents. Code will be released after peer review.

</details>

---

### 30. [TimberAgent: Gram-Guided Retrieval for Executable Music Effect Control](https://arxiv.org/abs/2603.09332)

**基本信息**

- 🔗 arXiv: [`2603.09332`](https://arxiv.org/abs/2603.09332)
- 👥 作者: Shihao He, Yihan Xia, Fang Liu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09332.pdf)

**💡 相关性分析**

满足标准2：论文提出了TRR（Texture Resonance Retrieval）这一新颖的音频表示方法，该方法基于Wav2Vec2模型的中间层激活构建。虽然应用领域是音频处理，但其核心是开发一种用于复杂信号（音频）的“结构推理”方法，即从原始信号中提取有意义的、可用于检索和匹配的表示。这与“质谱结构推理”的核心挑战高度相似，后者也是从复杂的质谱信号中推断出分子结构或特征。TRR作为一种信号表示和检索框架，其设计思路（利用预训练模型的中间表示、构建Gram矩阵捕获共现结构）为处理质谱等复杂光谱数据的表示学习和检索任务提供了潜在的方法论参考和工具思路。

**📖 中文摘要**

本文研究了基于检索的音频效果控制，其输出是可编辑的插件配置而非最终波形。研究重点是纹理共振检索（TRR），这是一种基于投影的中层Wav2Vec2激活的Gram矩阵构建的音频表示。该设计保留了与纹理相关的协同激活结构。作者在包含1,063个候选预设和204个查询的吉他效果基准上评估了TRR。评估遵循Protocol-A，这是一种防止训练-测试泄漏的交叉验证方案。作者将TRR与CLAP以及内部检索基线（Wav2Vec-RAG, Text-RAG, FeatureNN-RAG）进行了比较，使用了基于物理DSP参数范围的min-max归一化指标。消融研究验证了TRR的核心设计选择：投影维度、层选择和投影类型。近重复敏感性分析证实结果对琐碎的知识库匹配具有鲁棒性。TRR在评估方法中实现了最低的归一化参数误差。一项有26名参与者参与的多刺激听力研究提供了互补的感知证据。作者将这些结果解释为基准证据，表明基于纹理感知的检索对于可编辑的音频效果控制是有用的。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Digital audio workstations expose rich effect chains, yet a semantic gap remains between perceptual user intent and low-level signal-processing parameters. We study retrieval-grounded audio effect control, where the output is an editable plugin configuration rather than a finalized waveform. Our focus is Texture Resonance Retrieval (TRR), an audio representation built from Gram matrices of projected mid-level Wav2Vec2 activations. This design preserves texture-relevant co-activation structure. We evaluate TRR on a guitar-effects benchmark with 1,063 candidate presets and 204 queries. The evaluation follows Protocol-A, a cross-validation scheme that prevents train-test leakage. We compare TRR against CLAP and internal retrieval baselines (Wav2Vec-RAG, Text-RAG, FeatureNN-RAG), using min-max normalized metrics grounded in physical DSP parameter ranges. Ablation studies validate TRR's core design choices: projection dimensionality, layer selection, and projection type. A near-duplicate sensitivity analysis confirms that results are robust to trivial knowledge-base matches. TRR achieves the lowest normalized parameter error among evaluated methods. A multiple-stimulus listening study with 26 participants provides complementary perceptual evidence. We interpret these results as benchmark evidence that texture-aware retrieval is useful for editable audio effect control, while broader personalization and real-audio robustness claims remain outside the verified evidence presented here.

</details>

---

### 31. [The Virtuous Cycle: AI-Powered Vector Search and Vector Search-Augmented AI](https://arxiv.org/abs/2603.09347)

**基本信息**

- 🔗 arXiv: [`2603.09347`](https://arxiv.org/abs/2603.09347)
- 👥 作者: Jiuqi Wei, Quanqing Xu, Chuanhui Yang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09347.pdf)

**💡 相关性分析**

满足标准3：论文是一篇针对“AI赋能向量搜索”和“向量搜索赋能AI（特别是RAG）”交叉领域的综述/教程。虽然主题宽泛，但其中核心部分“检索增强生成（RAG）”是当前大模型应用的关键技术之一。RAG框架通过检索外部知识来增强大模型的生成能力，这与“化学大模型”领域利用外部数据库（如化学知识库、质谱库）来增强模型在化学信息学任务（如分子性质预测、反应规划、质谱解析）中的准确性和可靠性的思路完全一致。因此，该论文提供了与“化学大模型”构建和应用（尤其是知识增强方面）相关的重要技术讨论和展望。

**📖 中文摘要**

本文是一篇教程，全面概述了现代人工智能（AI）与向量搜索（VS）快速融合这一新兴智能信息系统研究前沿的最新研究和进展。一方面，AI的进步极大地提高了向量搜索的语义准确性和效率，包括学习索引结构、自适应剪枝策略和自动参数调优。另一方面，强大的向量搜索技术实现了新的人工智能范式，特别是检索增强生成（RAG），它有效缓解了大型语言模型（LLM）中的知识过时和幻觉等挑战。这种相互强化建立了一个良性循环：AI将智能和自适应优化注入向量搜索，而向量搜索反过来扩展了AI在知识整合和上下文感知生成方面的能力。本教程首先讨论了整合向量搜索和AI的基础背景和动机。随后，探讨了AI如何在向量搜索管线的每个步骤中赋能向量搜索（AI4VS）。然后，研究了向量搜索如何赋能AI（VS4AI），特别关注将动态外部知识源集成到LLM生成过程中的RAG框架。此外，分析了充分释放向量搜索与AI之间“良性循环”潜力的端到端协同优化策略。最后，强调了这一新兴领域的关键挑战和未来研究机遇。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern AI and vector search are rapidly converging, forming a promising research frontier in intelligent information systems. On one hand, advances in AI have substantially improved the semantic accuracy and efficiency of vector search, including learned indexing structures, adaptive pruning strategies, and automated parameter tuning. On the other hand, powerful vector search techniques have enabled new AI paradigms, notably Retrieval-Augmented Generation (RAG), which effectively mitigates challenges in Large Language Models (LLMs) like knowledge staleness and hallucinations. This mutual reinforcement establishes a virtuous cycle where AI injects intelligence and adaptive optimization into vector search, while vector search, in turn, expands AI's capabilities in knowledge integration and context-aware generation. This tutorial provides a comprehensive overview of recent research and advancements at this intersection. We begin by discussing the foundational background and motivations for integrating vector search and AI. Subsequently, we explore how AI empowers vector search (AI4VS) across each step of the vector search pipeline. We then investigate how vector search empowers AI (VS4AI), with a particular focus on RAG frameworks that integrate dynamic, external knowledge sources into the generative process of LLMs. Furthermore, we analyze end-to-end co-optimization strategies that fully unlock the potential of the ``virtuous cycle" between vector search and AI. Finally, we highlight key challenges and future research opportunities in this emerging area. This paper was published in ICDE 2026.

</details>

---

### 32. [Quantifying and extending the coverage of spatial categorization data sets](https://arxiv.org/abs/2603.09373)

**基本信息**

- 🔗 arXiv: [`2603.09373`](https://arxiv.org/abs/2603.09373)
- 👥 作者: Wanchun Li, Alexandra Carstensen, Yang Xu 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09373.pdf)

**💡 相关性分析**

满足标准2：论文的核心贡献之一是使用大型语言模型（LLM）生成空间关系分类的标签数据，并利用这些数据来指导和扩展实证数据集（TRPS）。这直接提供了“可用于这些主题的数据集、资源或工具”。具体来说，它展示了LLM作为一种工具，用于生成或扩充特定领域（此处为空间关系）的标注数据。这种方法论可以平行迁移到“化学大模型”和“质谱结构推理”领域，例如，利用LLM生成分子描述、反应规则或质谱-结构对应关系的合成数据，以扩充训练集或创建评估基准。

**📖 中文摘要**

本文研究了跨语言空间分类的变异，通常通过收集人类对拓扑关系图片系列（TRPS）中描绘的关系的标签来进行。作者证明，大型语言模型（LLM）生成的标签与人类标签相对吻合，并展示了LLM生成的标签如何帮助决定在现有空间数据集中添加哪些场景和语言。为了说明方法，作者通过添加42个新场景扩展了TRPS，并证明这种扩展比TRPS之前的两次扩展更好地覆盖了可能场景的空间。研究结果为扩展到包含数十种语言和数百个场景的空间数据集奠定了基础。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Variation in spatial categorization across languages is often studied by eliciting human labels for the relations depicted in a set of scenes known as the Topological Relations Picture Series (TRPS). We demonstrate that labels generated by large language models (LLMs) align relatively well with human labels, and show how LLM-generated labels can help to decide which scenes and languages to add to existing spatial data sets. To illustrate our approach we extend the TRPS by adding 42 new scenes, and show that this extension achieves better coverage of the space of possible scenes than two previous extensions of the TRPS. Our results provide a foundation for scaling towards spatial data sets with dozens of languages and hundreds of scenes.

</details>

---

### 33. [First Steps towards Categorical Algebraic Artificial Chemistry](https://arxiv.org/abs/2603.09431)

**基本信息**

- 🔗 arXiv: [`2603.09431`](https://arxiv.org/abs/2603.09431)
- 👥 作者: Joe Pratt-Johns, Toby St. Clere Smithe, Chris Guiver 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09431.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕“人工化学”（Artificial Chemistry）这一主题，这是化学信息学和系统化学中的一个重要子领域。AlChemy模型使用lambda演算来模拟分子和化学反应，是“化学大模型”的一种早期、形式化的计算表现形式。论文旨在使用范畴论这一高级数学工具来形式化和推广此类模型，这直接与“化学大模型”的理论基础和研究前沿相关，致力于为化学系统的计算表示和动力学模拟提供更严谨、更通用的数学框架。

**📖 中文摘要**

本文为相互作用的组件的代数模型构建了一个函子，该函子赋予模型一种动力学。该构造概括了Fontana和Buss在人工生命领域（称为AlChemy）中的一个计算模型，在该模型中，分子及其化学相互作用通过lambda演算项及其应用和后续归约来模拟。作者讨论了范畴论在未来应用于代数人工化学作为组织工具的方向，重点在于形式化此类模型的代数方面和动力学方面之间的联系。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We construct a functor that gives a dynamics to an algebraic model of interacting components. The construction generalises a computational model of Fontana and Buss in the field of artificial life known as AlChemy, in which molecules and their chemical interactions are emulated by lambda calculus terms and their application and subsequent reduction. We discuss future directions for the application of category theory to algebraic artificial chemistry as an organisational tool, with a focus on formalising the connection between the algebraic and the dynamical facets of such models.

</details>

---

### 34. [AI Act Evaluation Benchmark: An Open, Transparent, and Reproducible Evaluation Dataset for NLP and RAG Systems](https://arxiv.org/abs/2603.09435)

**基本信息**

- 🔗 arXiv: [`2603.09435`](https://arxiv.org/abs/2603.09435)
- 👥 作者: Athanasios Davvetas, Michael Papademas, Xenia Ziouvelou 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09435.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于评估NLP和RAG系统符合AI法规（欧盟AI法案）的基准数据集（AI Act Evaluation Benchmark）。该数据集是通过结合领域知识和LLM生成创建的。这直接提供了一个“可用于这些主题的数据集、资源或工具”。虽然评估领域是法规遵从性，但其构建方法（利用LLM生成基于法规文本的评估场景和任务）为在“化学大模型”和“质谱结构推理”领域构建专门的评估基准（例如，评估模型对化学安全法规的理解、对质谱解析结果的可靠性判断）提供了可借鉴的范例和工具思路。

**📖 中文摘要**

人工智能在异构公共和社会部门的快速部署随之加大了对符合监管标准和框架的需求。欧盟《人工智能法案》已成为监管领域的里程碑。开发能够引出人工智能系统符合此类标准水平的解决方案通常受到资源缺乏的限制，阻碍了对其性能的半自动化或自动化评估。这产生了对人工工作的需求，而人工工作往往容易出错、资源有限或仅限于法规未明确描述的情况。本文提出了一种开放、透明和可重复的方法来创建一种资源，该资源有助于评估NLP模型，并特别关注RAG系统。我们开发了一个数据集，其中包含针对欧盟《人工智能法案》的风险级别分类、条款检索、义务生成和问答任务。数据集文件采用机器对机器合适的格式。为了生成文件，我们利用领域知识作为注释基础，结合大型语言模型的处理和推理能力来生成场景以及相应的任务。我们的方法展示了一种利用语言模型进行具有高文档相关性的基础生成的方法。此外，我们克服了诸如导航欧盟《人工智能法案》中未明确定义的风险级别（如有限和最小风险情况）决策边界等限制。最后，我们通过评估一个基于RAG的解决方案来证明数据集的有效性，该解决方案在禁止和高风险场景下的F1分数分别达到0.87和0.85。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The rapid rollout of AI in heterogeneous public and societal sectors has subsequently escalated the need for compliance with regulatory standards and frameworks. The EU AI Act has emerged as a landmark in the regulatory landscape. The development of solutions that elicit the level of AI systems' compliance with such standards is often limited by the lack of resources, hindering the semi-automated or automated evaluation of their performance. This generates the need for manual work, which is often error-prone, resource-limited or limited to cases not clearly described by the regulation. This paper presents an open, transparent, and reproducible method of creating a resource that facilitates the evaluation of NLP models with a strong focus on RAG systems. We have developed a dataset that contain the tasks of risk-level classification, article retrieval, obligation generation, and question-answering for the EU AI Act. The dataset files are in a machine-to-machine appropriate format. To generate the files, we utilise domain knowledge as an exegetical basis, combining with the processing and reasoning power of large language models to generate scenarios along with the respective tasks. Our methodology demonstrates a way to harness language models for grounded generation with high document relevancy. Besides, we overcome limitations such as navigating the decision boundaries of risk-levels that are not explicitly defined within the EU AI Act, such as limited and minimal cases. Finally, we demonstrate our dataset's effectiveness by evaluating a RAG-based solution that reaches 0.87 and 0.85 F1-score for prohibited and high-risk scenarios.

</details>

---

### 35. [CyberThreat-Eval: Can Large Language Models Automate Real-World Threat Research?](https://arxiv.org/abs/2603.09452)

**基本信息**

- 🔗 arXiv: [`2603.09452`](https://arxiv.org/abs/2603.09452)
- 👥 作者: Xiangsen Chen, Xuan Feng, Shuo Chen 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09452.pdf)

**💡 相关性分析**

满足标准2：论文提出了CyberThreat-Eval，一个从真实网络威胁情报工作流程中收集的、专家标注的基准数据集，用于评估LLM在OSINT分析任务上的表现。这直接提供了一个“可用于这些主题的数据集、资源或工具”。虽然领域是网络安全，但其构建真实世界、多阶段、专家评估的复杂任务基准的方法论，对于在“化学大模型”和“质谱结构推理”领域构建类似的、贴近实际科研或工业应用场景的评估基准（例如，评估模型从化学文献中提取信息、推理反应路径或解析未知质谱的能力）具有重要的参考价值。

**📖 中文摘要**

从海量数据中分析开源情报（OSINT）对于起草和发布全面的网络威胁情报（CTI）报告至关重要。此过程通常遵循三阶段工作流程——分类、深度搜索和威胁情报起草。虽然大型语言模型（LLM）为实现自动化提供了一条有希望的途径，但现有基准仍有局限性。这些基准通常由不能反映真实世界分析师工作流程的任务组成。例如，人类分析师很少以多项选择题的形式接收任务。此外，现有基准通常依赖以词汇重叠为中心的模型中心指标，而不是安全分析师必需的可操作的、详细的见解。而且，它们通常未能覆盖完整的三阶段工作流程。为了解决这些问题，我们引入了CyberThreat-Eval，它收集自一家世界领先公司的日常CTI工作流程。这个由专家标注的基准在所有上述三个阶段的实际任务上评估LLM。它利用以分析师为中心的指标来衡量事实准确性、内容质量和运营成本。使用该基准进行的评估揭示了当前LLM局限性的重要见解。例如，LLM通常缺乏处理复杂细节所需的细致专业知识，并且难以区分正确和错误信息。为了应对这些挑战，CTI工作流程结合了外部真实数据库和人类专家知识。TRA允许人类专家迭代提供反馈以进行持续改进。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Analyzing Open Source Intelligence (OSINT) from large volumes of data is critical for drafting and publishing comprehensive CTI reports. This process usually follows a three-stage workflow -- triage, deep search and TI drafting. While Large Language Models (LLMs) offer a promising route toward automation, existing benchmarks still have limitations. These benchmarks often consist of tasks that do not reflect real-world analyst workflows. For example, human analysts rarely receive tasks in the form of multiple-choice questions. Also, existing benchmarks often rely on model-centric metrics that emphasize lexical overlap rather than actionable, detailed insights essential for security analysts. Moreover, they typically fail to cover the complete three-stage workflow. To address these issues, we introduce CyberThreat-Eval, which is collected from the daily CTI workflow of a world-leading company. This expert-annotated benchmark assesses LLMs on practical tasks across all three stages as mentioned above. It utilizes analyst-centric metrics that measure factual accuracy, content quality, and operational costs. Our evaluation using this benchmark reveals important insights into the limitations of current LLMs. For example, LLMs often lack the nuanced expertise required to handle complex details and struggle to distinguish between correct and incorrect information. To address these challenges, the CTI workflow incorporates both external ground-truth databases and human expert knowledge. TRA allows human experts to iteratively provide feedback for continuous improvement. The code is available at \href{ this https URL }{\texttt{GitHub}} and \href{ this https URL }{\texttt{HuggingFace}}.

</details>

---

### 36. [GenePlan: Evolving Better Generalized PDDL Plans using Large Language Models](https://arxiv.org/abs/2603.09481)

**基本信息**

- 🔗 arXiv: [`2603.09481`](https://arxiv.org/abs/2603.09481)
- 👥 作者: Andrew Murray, Danial Dervovic, Alberto Pozanco 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09481.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个利用大型语言模型（LLM）来进化生成可执行规划器（广义规划）的框架。这直接涉及“化学大模型”的应用场景之一：自动化规划。在化学信息学中，反应合成规划、实验流程设计等都是复杂的规划问题。GenePlan展示了一种将LLM与进化算法结合来自动生成领域特定规划器的方法，这种方法可以直接应用于化学合成规划等领域，是“化学大模型”在自动化化学研究中的一种具体实现形式。

**📖 中文摘要**

本文提出了GenePlan（广义进化规划器），这是一个新颖的框架，利用大型语言模型（LLM）辅助的进化算法为PDDL描述的经典规划任务生成领域依赖的广义规划器。通过将广义规划视为优化问题，GenePlan迭代地演化可解释的Python规划器，以最小化跨不同问题实例的规划长度。在六个现有基准领域和两个新领域的实证评估中，GenePlan的平均SAT分数达到0.91，与最先进规划器的性能（SAT分数0.93）非常接近，并显著优于其他基于LLM的基线，例如思维链（CoT）提示（平均SAT分数0.64）。生成的规划器能够快速解决新实例（平均每个任务0.49秒）且成本低（使用GPT-4o平均每个领域1.82美元）。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present GenePlan (GENeralized Evolutionary Planner), a novel framework that leverages large language model (LLM) assisted evolutionary algorithms to generate domain-dependent generalized planners for classical planning tasks described in PDDL. By casting generalized planning as an optimization problem, GenePlan iteratively evolves interpretable Python planners that minimize plan length across diverse problem instances. In empirical evaluation across six existing benchmark domains and two new domains, GenePlan achieved an average SAT score of 0.91, closely matching the performance of the state-of-the-art planners (SAT score 0.93), and significantly outperforming other LLM-based baselines such as chain-of-thought (CoT) prompting (average SAT score 0.64). The generated planners solve new instances rapidly (average 0.49 seconds per task) and at low cost (average $1.82 per domain using GPT-4o).

</details>

---

### 37. [Symbolic Discovery of Stochastic Differential Equations with Genetic Programming](https://arxiv.org/abs/2603.09597)

**基本信息**

- 🔗 arXiv: [`2603.09597`](https://arxiv.org/abs/2603.09597)
- 👥 作者: Sigur de Vries, Sander W. Keemink, Marcel A. J. van Gerven
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09597.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（基于遗传编程的符号回归用于发现随机微分方程）直接围绕“化学大模型”主题，因为化学大模型的核心任务之一就是从化学数据中学习可解释的数学模型和规律。该方法为从复杂的化学/质谱数据中自动发现控制方程或结构-性质关系提供了技术路径。

**📖 中文摘要**

这篇论文提出了一种基于遗传编程的随机微分方程符号发现方法。该方法的核心是联合优化漂移和扩散函数的最大似然估计，从而能够从观测数据中学习可解释的数学表达式。虽然论文主要关注随机动力系统，但其核心方法——符号回归——是化学信息学和计算化学中用于从数据中发现物理定律和反应动力学模型的关键技术。该方法通过遗传编程自动发现方程，这与“化学大模型”中利用机器学习从化学数据中学习底层规律和模型的目标高度一致。论文展示了该方法在从噪声数据中恢复控制方程、扩展到高维系统以及对稀疏采样问题的鲁棒性，这些能力对于从复杂的质谱或化学动力学数据中推断结构或反应网络具有重要意义。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Automated scientific discovery aims to improve scientific understanding through machine learning. A central approach in this field is symbolic regression, which uses genetic programming or sparse regression to learn interpretable mathematical expressions to explain observed data. Conventionally, the focus of symbolic regression is on identifying ordinary differential equations. The general view is that noise only complicates the recovery of deterministic dynamics. However, explicitly learning a symbolic function of the noise component in stochastic differential equations enhances modelling capacity, increases knowledge gain and enables generative sampling. We introduce a method for symbolic discovery of stochastic differential equations based on genetic programming, jointly optimizing drift and diffusion functions via the maximum likelihood estimate. Our results demonstrate accurate recovery of governing equations, efficient scaling to higher-dimensional systems, robustness to sparsely sampled problems and generalization to stochastic partial differential equations. This work extends symbolic regression toward interpretable discovery of stochastic dynamical systems, contributing to the automation of science in a noisy and dynamic world.

</details>

---

### 38. [MM-algorithms for traditional and convex NMF with Tweedie and Negative Binomial cost functions and empirical evaluation](https://arxiv.org/abs/2603.09601)

**基本信息**

- 🔗 arXiv: [`2603.09601`](https://arxiv.org/abs/2603.09601)
- 👥 作者: Elisabeth Sommer James, Asger Hobolth, Marta Pelizzola
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09601.pdf)

**💡 相关性分析**

满足标准2：论文提供了可用于“化学大模型”和“质谱分析”主题的数据分析工具和算法（非负矩阵分解框架及其针对不同噪声模型的实现）。质谱数据经常需要进行降维和模式提取，NMF是其中关键技术之一，而论文中针对计数数据（如质谱峰强度）的负二项式等模型更新规则具有直接应用价值。

**📖 中文摘要**

这篇论文提出了一个用于传统和非负矩阵分解（NMF）的统一框架，该框架基于Majorize-Minimisation方法，并针对包括负二项式和Tweedie模型在内的一类广泛分布假设推导了乘法更新规则。NMF是化学信息学和生物信息学中用于从高通量数据（如质谱成像、基因表达谱）中提取特征和模式的常用工具。论文特别强调了噪声模型（如泊松、负二项式）的选择对模型拟合和特征恢复的关键影响，并提供了首个针对泊松和负二项式成本函数的凸NMF模型实现。这项工作为处理化学和质谱数据中常见的过离散或复杂均值-方差关系提供了重要的数据分析和特征提取工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Non-negative matrix factorisation (NMF) is a widely used tool for unsupervised learning and feature extraction, with applications ranging from genomics to text analysis and signal processing. Standard formulations of NMF are typically derived under Gaussian or Poisson noise assumptions, which may be inadequate for data exhibiting overdispersion or other complex mean-variance relationships. In this paper, we develop a unified framework for both traditional and convex NMF under a broad class of distributional assumptions, including Negative Binomial and Tweedie models, where the connection between the Tweedie and the $\beta$-divergence is also highlighted. Using a Majorize-Minimisation approach, we derive multiplicative update rules for all considered models, and novel updates for convex NMF with Poisson and Negative Binomial cost functions. We provide a unified implementation of all considered models, including the first implementations of several convex NMF models. Empirical evaluations on mutational and word count data demonstrate that the choice of noise model critically affects model fit and feature recovery, and that convex NMF can provide an efficient and robust alternative to traditional NMF in scenarios where the number of classes is large. The code for our proposed updates is available in the R package nmfgenr and can be found at this https URL .

</details>

---

### 39. [Understanding the Interplay between LLMs' Utilisation of Parametric and Contextual Knowledge: A keynote at ECIR 2025](https://arxiv.org/abs/2603.09654)

**基本信息**

- 🔗 arXiv: [`2603.09654`](https://arxiv.org/abs/2603.09654)
- 👥 作者: Isabelle Augenstein
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09654.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心讨论（LLMs中参数化知识与上下文知识的交互）直接关系到如何构建和评估可靠的“化学大模型”。同时，作为一篇会议主题报告，它包含了针对该主题的重要综述和展望性讨论，指出了当前挑战和未来研究方向，这对于化学信息学领域的研究人员具有指导意义。

**📖 中文摘要**

这篇论文是ECIR 2025的一个主题报告，重点探讨了大型语言模型（LLMs）中参数化知识与上下文知识之间的相互作用。报告讨论了如何评估模型中的知识、揭示知识冲突的诊断测试，以及理解成功使用的上下文知识的特征。虽然报告以通用语言模型为背景，但其核心问题——模型如何整合和权衡其内部记忆（参数化知识）与外部提供的证据（上下文知识）——对于构建可靠的“化学大模型”至关重要。在化学信息学中，大模型需要将其在大量文献和化合物数据上预训练的知识与特定的实验数据、用户查询或数据库检索结果相结合，以进行准确的质谱结构推理或化学反应预测。报告中对这一“交互作用”的研究为设计更可靠、更少幻觉的化学领域大模型提供了重要的理论基础和诊断视角。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Language Models (LMs) acquire parametric knowledge from their training process, embedding it within their weights. The increasing scalability of LMs, however, poses significant challenges for understanding a model's inner workings and further for updating or correcting this embedded knowledge without the significant cost of retraining. Moreover, when using these language models for knowledge-intensive language understanding tasks, LMs have to integrate relevant context, mitigating their inherent weaknesses, such as incomplete or outdated knowledge. Nevertheless, studies indicate that LMs often ignore the provided context as it can be in conflict with the pre-existing LM's memory learned during pre-training. Conflicting knowledge can also already be present in the LM's parameters, termed intra-memory conflict. This underscores the importance of understanding the interplay between how a language model uses its parametric knowledge and the retrieved contextual knowledge. In this talk, I will aim to shed light on this important issue by presenting our research on evaluating the knowledge present in LMs, diagnostic tests that can reveal knowledge conflicts, as well as on understanding the characteristics of successfully used contextual knowledge.

</details>

---

### 40. [Physics-informed neural operator for predictive parametric phase-field modelling](https://arxiv.org/abs/2603.09693)

**基本信息**

- 🔗 arXiv: [`2603.09693`](https://arxiv.org/abs/2603.09693)
- 👥 作者: Nanxi Chen, Airong Chen, Rujin Ma
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09693.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容（物理信息神经算子）是构建“化学大模型”的一种重要技术路径。化学大模型不仅需要数据驱动，还需要融入物理化学定律作为约束，以提升其在预测化学反应、材料性质等任务中的准确性和可靠性。PF-PINO框架展示了如何将领域知识（物理方程）嵌入到神经网络中，这对于开发下一代化学AI模型具有直接的参考价值。

**📖 中文摘要**

这篇论文提出了PF-PINO，一个物理信息神经算子框架，用于学习参数化的相场偏微分方程。该框架通过将相场控制方程的残差嵌入到数据保真度损失函数中，在训练期间有效强制执行物理约束。作者在电化学腐蚀、枝晶凝固和旋节分解等基准相场问题上验证了PF-PINO。相场建模是材料科学和化学中模拟微观结构演化的强大工具，而PF-PINO通过结合物理约束的深度学习，为加速这类计算密集型模拟提供了新途径。虽然论文聚焦于材料相场，但其“物理信息神经算子”的核心方法论——即利用神经网络加速求解受物理定律约束的PDE——与“化学大模型”中整合物理化学先验知识以提升模型泛化能力和可解释性的目标高度一致。该方法为构建用于化学过程模拟或材料性质预测的、具有物理一致性的机器学习模型提供了技术框架。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Predicting the microstructural and morphological evolution of materials through phase-field modelling is computationally intensive, particularly for high-throughput parametric studies. While neural operators such as the Fourier neural operator (FNO) show promise in accelerating the solution of parametric partial differential equations (PDEs), the lack of explicit physical constraints, may limit generalisation and long-term accuracy for complex phase-field dynamics. Here, we develop a physics-informed neural operator framework to learn parametric phase-field PDEs, namely PF-PINO. By embedding the residuals of phase-field governing equations into the data-fidelity loss function, our framework effectively enforces physical constraints during training. We validate PF-PINO against benchmark phase-field problems, including electrochemical corrosion, dendritic crystal solidification, and spinodal decomposition. Our results demonstrate that PF-PINO significantly outperforms conventional FNO in accuracy, generalisation capability, and long-term stability. This work provides a robust and efficient computational tool for phase-field modelling and highlights the potential of physics-informed neural operators to advance scientific machine learning for complex interfacial evolution problems.

</details>

---

### 41. [Epistemic Closure: Autonomous Mechanism Completion for Physically Consistent Simulation](https://arxiv.org/abs/2603.09756)

**基本信息**

- 🔗 arXiv: [`2603.09756`](https://arxiv.org/abs/2603.09756)
- 👥 作者: Yue Wua, Tianhao Su, Rui Hu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09756.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕利用大语言模型（LLMs）进行科学发现和物理机制推理，这直接关联到“化学大模型”主题中关于AI模型在科学（包括化学）领域应用和推理的核心思想。

**📖 中文摘要**

本文提出了一种神经符号生成代理，作为传统数值引擎之上的认知监督器。该研究旨在解决将大语言模型（LLMs）集成到科学发现中时遇到的“隐式上下文”问题，即从文献中提取的控制方程包含标准生成模型无法识别的不可见热力学假设（例如，不排水条件），从而导致“物理幻觉”：生成语法正确但物理上无效的求解器。该代理将物理定律封装到模块化的“本构技能”中，并利用潜在的内在先验，采用思维链推理工作流来自主验证、剪枝和补全物理机制。研究以低渗透率砂岩中的热增压挑战为例进行了演示。这项工作建立了一种范式，使AI代理超越编码助手的角色，成为能够推理和纠正科学数据中嵌入的理论假设的认知伙伴。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into scientific discovery is currently hindered by the Implicit Context problem, where governing equations extracted from literature contain invisible thermodynamic assumptions (e.g., undrained conditions) that standard generative models fail to recognize. This leads to Physical Hallucination: the generation of syntactically correct solvers that faithfully execute physically invalid laws. Here, we introduce a Neuro-Symbolic Generative Agent that functions as a cognitive supervisor atop traditional numerical engines. By encapsulating physical laws into modular Constitutive Skills and leveraging latent intrinsic priors, the Agent employs a Chain-of-Thought reasoning workflow to autonomously validate, prune, and complete physical mechanisms. We demonstrate this capability on the challenge of thermal pressurization in low-permeability sandstone. While a standard literature-retrieval baseline erroneously predicts catastrophic material failure by blindly adopting a rigid "undrained" simplification, our Agent autonomously identifies the system as operating in a drained regime (Deborah number De << 1) via dimensionless scaling analysis. Consequently, it inductively completes the missing dissipation mechanism (Darcy flow) required to satisfy boundary constraints, predicting a stable stress path consistent with experimental reality. This work establishes a paradigm where AI agents transcend the role of coding assistants to act as epistemic partners, capable of reasoning about and correcting the theoretical assumptions embedded in scientific data.

</details>

---

### 42. [MITRA: An AI Assistant for Knowledge Retrieval in Physics Collaborations](https://arxiv.org/abs/2603.09800)

**基本信息**

- 🔗 arXiv: [`2603.09800`](https://arxiv.org/abs/2603.09800)
- 👥 作者: Abhishikth Mallampalli, Sridhara Dasu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09800.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个专门用于科学（物理学）领域的检索增强生成（RAG）系统MITRA，该系统构建了从文档检索到文本提取、再到向量数据库检索的完整工具链和数据管道。这为在科学领域（可扩展至化学信息学）构建基于大模型的问答或知识检索系统提供了相关的数据资源、工具和架构参考。

**📖 中文摘要**

本文介绍了MITRA，一个基于检索增强生成（RAG）的系统原型，旨在回答关于物理分析的特定、上下文感知的问题。该系统设计用于处理大型科学合作（如CERN的CMS）产生的大量内部文档。MITRA采用了一个新颖的自动化管道，使用Selenium从内部数据库检索文档，并使用光学字符识别（OCR）和布局解析进行高保真文本提取。其整个框架（从嵌入模型到大语言模型）都在本地托管，确保了敏感合作数据的隐私。该系统引入了一个双层向量数据库架构，首先从摘要中识别相关分析，然后专注于完整文档，解决了不同分析之间的潜在歧义。该研究展示了原型在现实查询上相对于标准基于关键词基线的优越检索性能。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large-scale scientific collaborations, such as the Compact Muon Solenoid (CMS) at CERN, produce a vast and ever-growing corpus of internal documentation. Navigating this complex information landscape presents a significant challenge for both new and experienced researchers, hindering knowledge sharing and slowing down the pace of scientific discovery. To address this, we present a prototype of MITRA, a Retrieval-Augmented Generation (RAG) based system, designed to answer specific, context-aware questions about physics analyses. MITRA employs a novel, automated pipeline using Selenium for document retrieval from internal databases and Optical Character Recognition (OCR) with layout parsing for high-fidelity text extraction. Crucially, MITRA's entire framework, from the embedding model to the Large Language Model (LLM), is hosted on-premise, ensuring that sensitive collaboration data remains private. We introduce a two-tiered vector database architecture that first identifies the relevant analysis from abstracts before focusing on the full documentation, resolving potential ambiguities between different analyses. We demonstrate the prototype's superior retrieval performance against a standard keyword-based baseline on realistic queries and discuss future work towards developing a comprehensive research agent for large experimental collaborations.

</details>

---

### 43. [Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision via In-Context Reinforcement Learning](https://arxiv.org/abs/2603.09803)

**基本信息**

- 🔗 arXiv: [`2603.09803`](https://arxiv.org/abs/2603.09803)
- 👥 作者: Tiehua Mei, Minxuan Lv, Leiyu Pan 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09803.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕提升大语言模型（LLMs）的推理质量，特别是通过强化学习和上下文学习进行优化。这直接关联到“化学大模型”主题中关于提升AI模型在科学领域（如化学结构推理）的推理能力和可靠性的核心挑战。

**📖 中文摘要**

本文研究了通过上下文强化学习对推理质量进行隐式监督的方法。论文观察到，更好的推理是更好的老师：高质量的解决方案比低质量的解决方案能作为更有效的演示。作者将这种教学能力称为“演示效用”，并表明策略模型自身的上下文学习能力提供了一种有效的方法来衡量它，从而产生一个称为“证据增益”的质量信号。为了在训练中使用这个信号，作者引入了“上下文RLVR”。通过贝叶斯分析，作者表明这个目标函数通过证据增益隐式地重新加权奖励，将更高的权重分配给高质量轨迹，更低的权重分配给低质量轨迹，而不需要昂贵的计算或外部评估器。在数学基准上的实验显示，该方法在准确性和推理质量上都优于标准的RLVR。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Reinforcement Learning with Verifiable Rewards (RLVR) improves reasoning in large language models but treats all correct solutions equally, potentially reinforcing flawed traces that get correct answers by chance. We observe that better reasoning are better teachers: high-quality solutions serve as more effective demonstrations than low-quality ones. We term this teaching ability Demonstration Utility, and show that the policy model's own in-context learning ability provides an efficient way to measure it, yielding a quality signal termed Evidence Gain. To employ this signal during training, we introduce In-Context RLVR. By Bayesian analysis, we show that this objective implicitly reweights rewards by Evidence Gain, assigning higher weights to high-quality traces and lower weights to low-quality ones, without requiring costly computation or external evaluators. Experiments on mathematical benchmarks show improvements in both accuracy and reasoning quality over standard RLVR.

</details>

---

### 44. [Expressive Power of Property Graph Constraint Languages](https://arxiv.org/abs/2603.09806)

**基本信息**

- 🔗 arXiv: [`2603.09806`](https://arxiv.org/abs/2603.09806)
- 👥 作者: Stefania Dumbrava, Nadime Francis, Victor Marsault 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09806.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是对图数据（属性图）约束语言的表达能力和形式化研究。图是化学信息学中表示分子结构的核心数据模型（如分子图）。对图约束和查询语言的研究，为化学大模型中处理、验证和推理分子图数据提供了理论基础和形式化工具，属于核心主题相关的底层技术研究。

**📖 中文摘要**

本文首次对属性图约束语言的表达能力进行了原则性和系统性的研究，重点关注了即将影响GQL标准修订的PG-Keys语言。为此，作者将PG-Keys置于更广泛的现有形式化体系中进行定位。特别是，将PG-Keys与两种核心的属性图约束语言：图函数依赖（GFD）和图生成依赖（GGD）进行了比较。为了进行公平的比较，作者首先提出了一个统一框架。在该框架内，作者考虑将带有等式和不等式谓词的合取正则路径查询（CRPQ）作为图模式。然后，作者识别了行为良好的片段，建立了表达能力包含关系，并证明了分离结果，从而产生了一个完整且严格的表达能力层次结构。研究结果精确地指出了PG-Keys在何时提供严格更强的表达能力，阐明了其在最先进的属性图约束形式化中的地位。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We present the first principled and systematic study of the expressive power of property graph constraint languages, focused on the recent PG-Keys language, set to inform the upcoming revision of the GQL standard. To this end, we position PG-Keys within the broader landscape of existing formalisms. In particular, we compare PG-Keys with two core property graph constraint languages: Graph Functional Dependencies (GFD) and Graph Generating Dependencies (GGD). One hurdle is that these formalisms allow different kinds of graph pattern languages and data predicates. To make a fair comparison, based on their structural differences only, we first present a unifying framework. Within this framework, we consider conjunctive regular path queries (CRPQ) as graph patterns with equality and inequality predicates. We then identify well-behaved fragments, establish expressiveness inclusion, and prove separation results, yielding a complete and strict hierarchy of expressive power. The results identify precisely when PG-Keys provide strictly greater expressive power, clarifying their place among state-of-the-art property graph constraint formalisms.

</details>

---

### 45. [RecThinker: An Agentic Framework for Tool-Augmented Reasoning in Recommendation](https://arxiv.org/abs/2603.09843)

**基本信息**

- 🔗 arXiv: [`2603.09843`](https://arxiv.org/abs/2603.09843)
- 👥 作者: Haobo Zhang, Yutao Zhu, Kelong Mao 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09843.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容围绕构建一个基于大语言模型（LLMs）的、具备工具使用和自主推理能力的智能体框架（RecThinker）。虽然应用场景是推荐系统，但其核心方法论——即让大模型具备分析信息缺口、规划工具调用序列、执行工具获取信息并进行推理的能力——与构建用于化学信息学或质谱分析领域的“化学大模型”或“推理智能体”在架构和思路上高度相关。

**📖 中文摘要**

本文提出了RecThinker，一个用于推荐系统中工具增强推理的智能体框架。该框架将推荐从被动处理转变为自主调查，通过动态规划推理路径并自主调用工具使用来主动获取关键信息。具体来说，RecThinker采用分析-规划-执行范式，首先分析用户-项目信息的充分性，然后自主调用工具调用序列来弥合可用知识与推理需求之间的信息差距。作者为RecThinker开发了一套专用工具，使模型能够获取用户端、项目端和协同信息，以进行更好的推理和用户-项目匹配。此外，作者引入了一个自增强训练流程，包括监督微调阶段以内化高质量推理轨迹，以及强化学习阶段以优化决策准确性和工具使用效率。在多个基准数据集上的大量实验表明，RecThinker在推荐场景中 consistently 优于强基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have revolutionized recommendation agents by providing superior reasoning and flexible decision-making capabilities. However, existing methods mainly follow a passive information acquisition paradigm, where agents either rely on static pre-defined workflows or perform reasoning with constrained information. It limits the agent's ability to identify information sufficiency, often leading to suboptimal recommendations when faced with fragmented user profiles or sparse item metadata. To address these limitations, we propose RecThinker, an agentic framework for tool-augmented reasoning in recommendation, which shifts recommendation from passive processing to autonomous investigation by dynamically planning reasoning paths and proactively acquiring essential information via autonomous tool-use. Specifically, RecThinker adopts an Analyze-Plan-Act paradigm, which first analyzes the sufficiency of user-item information and autonomously invokes tool-calling sequences to bridge information gaps between available knowledge and reasoning requirements. We develop a suite of specialized tools for RecThinker, enabling the model to acquire user-side, item-side, and collaborative information for better reasoning and user-item matching. Furthermore, we introduce a self-augmented training pipeline, comprising a Supervised Fine-Tuning (SFT) stage to internalize high-quality reasoning trajectories and a Reinforcement Learning (RL) stage to optimize for decision accuracy and tool-use efficiency. Extensive experiments on multiple benchmark datasets demonstrate that RecThinker consistently outperforms strong baselines in the recommendation scenario.

</details>

---

### 46. [SCENEBench: An Audio Understanding Benchmark Grounded in Assistive and Industrial Use Cases](https://arxiv.org/abs/2603.09853)

**基本信息**

- 🔗 arXiv: [`2603.09853`](https://arxiv.org/abs/2603.09853)
- 👥 作者: Laya Iyer, Angelina Wang, Sanmi Koyejo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09853.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个新的音频理解基准测试SCENEBench，并构建了相应的合成和自然数据集。虽然主题是音频，但构建系统性、多任务、用于评估AI模型在特定领域（此处是音频）理解能力的基准和数据集的方法论，与在“化学信息学”和“质谱分析”领域构建评估“化学大模型”或“质谱结构推理”模型性能的基准和数据集的需求高度相关，提供了数据资源构建和评估范式的参考。

**📖 中文摘要**

本文提出了一个基准测试套件SCENEBench，旨在针对现实世界辅助技术和工业噪声监测的需求，对音频理解进行广泛评估。该基准包含四个类别：背景声音理解、噪声定位、跨语言语音理解和声音特征识别。这些音频样本是合成构建的（例如，通过叠加两个自然音频样本）。此外，作者还通过从现有数据集中子采样以匹配任务标准的20个自然音频项目来验证基准的生态效度。作者评估了五个最先进的大型音频语言模型，并发现了关键差距：性能在不同任务间存在差异，有些任务的表现低于随机机会，而其他任务则达到高精度。这些结果为模型能力的针对性改进提供了方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Advances in large language models (LLMs) have enabled significant capabilities in audio processing, resulting in state-of-the-art models now known as Large Audio Language Models (LALMs). However, minimal work has been done to measure audio understanding beyond automatic speech recognition (ASR). This paper closes that gap by proposing a benchmark suite, SCENEBench (Spatial, Cross-lingual, Environmental, Non-speech Evaluation), that targets a broad form of audio comprehension across four real-world categories: background sound understanding, noise localization, cross-linguistic speech understanding, and vocal characterizer recognition. These four categories are selected based on understudied needs from accessibility technology and industrial noise monitoring. In addition to performance, we also measure model latency. The purpose of this benchmark suite is to assess audio beyond just what words are said - rather, how they are said and the non-speech components of the audio. Because our audio samples are synthetically constructed (e.g., by overlaying two natural audio samples), we further validate our benchmark against 20 natural audio items per task, sub-sampled from existing datasets to match our task criteria, to assess ecological validity. We assess five state-of-the-art LALMs and find critical gaps: performance varies across tasks, with some tasks performing below random chance and others achieving high accuracy. These results provide direction for targeted improvements in model capabilities.

</details>

---

### 47. [GAST: Gradient-aligned Sparse Tuning of Large Language Models with Data-layer Selection](https://arxiv.org/abs/2603.09865)

**基本信息**

- 🔗 arXiv: [`2603.09865`](https://arxiv.org/abs/2603.09865)
- 👥 作者: Kai Yao, Zhenghan Song, Kaixin Wu 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09865.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种针对大语言模型（LLMs）的参数高效微调（PEFT）新方法。该方法旨在通过同时在数据和模型层两个维度进行自适应选择，来提升微调效率和效果。优化大模型的微调策略是构建和应用“化学大模型”的关键技术环节，因此该研究与核心主题直接相关。

**📖 中文摘要**

本文提出了梯度对齐稀疏调优（GAST），一种创新的方法，将数据和层的选择性微调作为统一优化策略的组成部分同时执行。GAST特别针对信息冗余，采用层稀疏策略，自适应地为每一层选择最具影响力的数据点，提供了一个比局限于单一维度的方法更全面和复杂的解决方案。实验表明，GAST consistently 优于基线方法，为PEFT策略的未来研究确立了一个有前景的方向。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Parameter-Efficient Fine-Tuning (PEFT) has become a key strategy for adapting large language models, with recent advances in sparse tuning reducing overhead by selectively updating key parameters or subsets of data. Existing approaches generally focus on two distinct paradigms: layer-selective methods aiming to fine-tune critical layers to minimize computational load, and data-selective methods aiming to select effective training subsets to boost training. However, current methods typically overlook the fact that different data points contribute varying degrees to distinct model layers, and they often discard potentially valuable information from data perceived as of low quality. To address these limitations, we propose Gradient-aligned Sparse Tuning (GAST), an innovative method that simultaneously performs selective fine-tuning at both data and layer dimensions as integral components of a unified optimization strategy. GAST specifically targets redundancy in information by employing a layer-sparse strategy that adaptively selects the most impactful data points for each layer, providing a more comprehensive and sophisticated solution than approaches restricted to a single dimension. Experiments demonstrate that GAST consistently outperforms baseline methods, establishing a promising direction for future research in PEFT strategies.

</details>

---

### 48. [N-gram-like Language Models Predict Reading Time Best](https://arxiv.org/abs/2603.09872)

**基本信息**

- 🔗 arXiv: [`2603.09872`](https://arxiv.org/abs/2603.09872)
- 👥 作者: James A. Michaelov, Roger P. Levy
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09872.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是比较和分析不同语言模型（包括n-gram和Transformer）的预测概率与人类阅读行为（阅读时间）的关联。这属于对“大模型”内在机制和认知对齐的基础研究，对于理解化学领域大模型（如用于文献阅读或报告生成）的可能行为模式具有参考价值，属于核心主题相关的底层机理探索。

**📖 中文摘要**

近期研究发现，像Transformer这样的当代语言模型在下一个词预测上变得如此优秀，以至于它们计算出的概率对于预测阅读时间反而变得更差。本文提出，这可以通过阅读时间对简单的n-gram统计量敏感，而不是对最先进的Transformer语言模型学习的更复杂的统计量敏感来解释。作者证明，其预测与n-gram概率最相关的神经语言模型，也是那些计算出的概率与自然文本上基于眼动的阅读时间指标最相关的模型。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent work has found that contemporary language models such as transformers can become so good at next-word prediction that the probabilities they calculate become worse for predicting reading time. In this paper, we propose that this can be explained by reading time being sensitive to simple n-gram statistics rather than the more complex statistics learned by state-of-the-art transformer language models. We demonstrate that the neural language models whose predictions are most correlated with n-gram probability are also those that calculate probabilities that are the most correlated with eye-tracking-based metrics of reading time on naturalistic text.

</details>

---

### 49. [Influencing LLM Multi-Agent Dialogue via Policy-Parameterized Prompts](https://arxiv.org/abs/2603.09890)

**基本信息**

- 🔗 arXiv: [`2603.09890`](https://arxiv.org/abs/2603.09890)
- 👥 作者: Hongbo Bo, Jingyu Hu, Weiru Liu
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09890.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是如何通过参数化提示来影响和控制基于大语言模型（LLMs）的多智能体系统的对话行为。构建可控、可引导的多智能体系统是“化学大模型”可能的应用形态之一（例如，多个专业AI助手协作解决化学问题），因此该研究在智能体行为控制和引导方面与核心主题相关。

**📖 中文摘要**

本文研究了基于大语言模型（LLMs）的多智能体系统的行为。与强化学习不同，作者研究了提示作为行动是否可以被参数化，以构建一个轻量级策略，该策略由一系列状态-行动对组成，用于在不训练的情况下影响对话行为。作者的框架将提示视为由LLMs执行的动作，并根据智能体的当前状态通过五个组件动态构建提示。为了测试参数化控制的有效性，作者基于五个指标评估了对话流程：响应性、反驳、证据使用、非重复性和立场转变。作者使用不同的LLM驱动智能体在与公众相关的两种讨论场景中进行实验，结果表明提示参数化可以影响对话动态。这一结果表明，策略参数化的提示提供了一种简单有效的机制来影响对话过程。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Language Models (LLMs) have emerged as a new paradigm for multi-agent systems. However, existing research on the behaviour of LLM-based multi-agents relies on ad hoc prompts and lacks a principled policy perspective. Different from reinforcement learning, we investigate whether prompt-as-action can be parameterized so as to construct a lightweight policy which consists of a sequence of state-action pairs to influence conversational behaviours without training. Our framework regards prompts as actions executed by LLMs, and dynamically constructs prompts through five components based on the current state of the agent. To test the effectiveness of parameterized control, we evaluated the dialogue flow based on five indicators: responsiveness, rebuttal, evidence usage, non-repetition, and stance shift. We conduct experiments using different LLM-driven agents in two discussion scenarios related to the general public and show that prompt parameterization can influence the dialogue dynamics. This result shows that policy-parameterised prompts offer a simple and effective mechanism to influence the dialogue process, which will help the research of multi-agent systems in the direction of social simulation.

</details>

---

### 50. [MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning](https://arxiv.org/abs/2603.09892)

**基本信息**

- 🔗 arXiv: [`2603.09892`](https://arxiv.org/abs/2603.09892)
- 👥 作者: Yiyang Lu, Yu He, Jianlong Chen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09892.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种针对大语言模型（LLMs）的持续学习（持续微调）方法，旨在解决灾难性遗忘问题。使“化学大模型”能够持续学习新的化学知识、反应或谱图数据而不遗忘旧知识，是其实际应用的关键挑战之一。因此，该研究与核心主题直接相关。

**📖 中文摘要**

本文提出了记忆感知自适应回放（MSSR），一个经验回放框架，用于大语言模型（LLMs）的持续微调。该框架估计样本级别的记忆强度，并以自适应间隔安排复习，以减轻灾难性遗忘，同时保持快速适应能力。在三个骨干模型和11个顺序任务上的大量实验表明，MSSR consistently 优于最先进的回放基线，在推理密集型和多项选择题基准上取得了特别强的增益。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Continual fine-tuning of large language models (LLMs) is becoming increasingly crucial as these models are deployed in dynamic environments where tasks and data distributions evolve over time. While strong adaptability enables rapid acquisition of new knowledge, it also exposes LLMs to catastrophic forgetting, where previously learned skills degrade during sequential training. Existing replay-based strategies, such as fixed interleaved replay, accuracy-supervised, and loss-driven scheduling, remain limited: some depend on heuristic rules and provide only partial mitigation of forgetting, while others improve performance but incur substantial computational overhead. Motivated by retention dynamics under sequential fine-tuning, we propose Memory-Inspired Sampler and Scheduler Replay (MSSR), an experience replay framework that estimates sample-level memory strength and schedules rehearsal at adaptive intervals to mitigate catastrophic forgetting while maintaining fast adaptation. Extensive experiments across three backbone models and 11 sequential tasks show that MSSR consistently outperforms state-of-the-art replay baselines, with particularly strong gains on reasoning-intensive and multiple-choice benchmarks.

</details>

---

### 51. [Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs](https://arxiv.org/abs/2603.09906)

**基本信息**

- 🔗 arXiv: [`2603.09906`](https://arxiv.org/abs/2603.09906)
- 👥 作者: Zorik Gekhman, Roee Aharoni, Eran Ofek 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09906.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容深入探讨了大语言模型（LLMs）中推理过程如何影响其内部知识的提取和回忆。这对于构建用于“质谱结构推理”或化学问题求解的“化学大模型”至关重要，因为这类模型需要可靠地从其参数化知识（如化学规则、谱图-结构关联）中检索信息并进行逻辑推理。该研究揭示了推理与知识回忆之间的机制，属于核心主题相关的底层认知研究。

**📖 中文摘要**

本文研究了推理在大语言模型（LLMs）中回忆参数化知识的作用。作者发现，启用推理可以显著扩展模型参数化知识回忆的能力边界，解锁那些原本无法触及的正确答案。为了探究原因，作者设计了一系列假设驱动的受控实验，并确定了两个关键驱动机制：（1）计算缓冲效应，模型使用生成的推理词元执行与其语义内容无关的潜在计算；（2）事实性启动，生成主题相关的事实作为语义桥梁，促进正确答案的检索。重要的是，后一种生成式自我检索机制带有固有风险：作者证明，在推理过程中产生幻觉的中间事实会增加最终答案出现幻觉的可能性。最后，作者展示了如何利用这些见解通过优先选择包含无幻觉事实陈述的推理轨迹来直接提高模型准确性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While reasoning in LLMs plays a natural role in math, code generation, and multi-hop factual questions, its effect on simple, single-hop factual questions remains unclear. Such questions do not require step-by-step logical decomposition, making the utility of reasoning highly counterintuitive. Nevertheless, we find that enabling reasoning substantially expands the capability boundary of the model's parametric knowledge recall, unlocking correct answers that are otherwise effectively unreachable. Why does reasoning aid parametric knowledge recall when there are no complex reasoning steps to be done? To answer this, we design a series of hypothesis-driven controlled experiments, and identify two key driving mechanisms: (1) a computational buffer effect, where the model uses the generated reasoning tokens to perform latent computation independent of their semantic content; and (2) factual priming, where generating topically related facts acts as a semantic bridge that facilitates correct answer retrieval. Importantly, this latter generative self-retrieval mechanism carries inherent risks: we demonstrate that hallucinating intermediate facts during reasoning increases the likelihood of hallucinations in the final answer. Finally, we show that our insights can be harnessed to directly improve model accuracy by prioritizing reasoning trajectories that contain hallucination-free factual statements.

</details>

---

### 52. [MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical Multi-Agent Systems](https://arxiv.org/abs/2603.09909)

**基本信息**

- 🔗 arXiv: [`2603.09909`](https://arxiv.org/abs/2603.09909)
- 👥 作者: Yunhang Qian, Xiaobin Hu, Jiaquan Yu 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09909.pdf)

**💡 相关性分析**

满足标准2和3：论文提出了一个用于多模态、多智能体系统的统一框架和大型基准测试平台（MedMASLab），并进行了系统性评估。这为在“化学信息学”或“质谱分析”领域构建类似的、用于评估“化学大模型”或多智能体系统在跨任务、跨数据模态场景下性能的基准测试，提供了重要的方法论、架构设计和评估范式的参考（满足标准2）。同时，该工作对当前多智能体系统在跨领域泛化方面的局限性的分析，也包含了对相关主题的重要讨论（满足标准3）。

**📖 中文摘要**

本文提出了MedMASLab，一个用于多模态医学多智能体系统的统一框架和基准测试平台。MedMASLab引入了：（1）一个标准化的多模态智能体通信协议，实现了跨11种异构MAS架构和24种医学模态的无缝集成。（2）一个自动化的临床推理评估器，这是一种零样本语义评估范式，通过利用大型视觉-语言模型来验证诊断逻辑和视觉基础，克服了词汇字符串匹配的局限性。（3）迄今为止最广泛的基准，涵盖11个器官系统和473种疾病，标准化了来自11个临床基准的数据。系统评估揭示了一个关键的领域特定性能差距：虽然MAS提高了推理深度，但当前架构在专业医学子领域之间转换时表现出显著的脆弱性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

While Multi-Agent Systems (MAS) show potential for complex clinical decision support, the field remains hindered by architectural fragmentation and the lack of standardized multimodal integration. Current medical MAS research suffers from non-uniform data ingestion pipelines, inconsistent visual-reasoning evaluation, and a lack of cross-specialty benchmarking. To address these challenges, we present MedMASLab, a unified framework and benchmarking platform for multimodal medical multi-agent systems. MedMASLab introduces: (1) A standardized multimodal agent communication protocol that enables seamless integration of 11 heterogeneous MAS architectures across 24 medical modalities. (2) An automated clinical reasoning evaluator, a zero-shot semantic evaluation paradigm that overcomes the limitations of lexical string-matching by leveraging large vision-language models to verify diagnostic logic and visual grounding. (3) The most extensive benchmark to date, spanning 11 organ systems and 473 diseases, standardizing data from 11 clinical benchmarks. Our systematic evaluation reveals a critical domain-specific performance gap: while MAS improves reasoning depth, current architectures exhibit significant fragility when transitioning between specialized medical sub-domains. We provide a rigorous ablation of interaction mechanisms and cost-performance trade-offs, establishing a new technical baseline for future autonomous clinical systems. The source code and data is publicly available at: this https URL

</details>

---

### 53. [WikiCLIP: An Efficient Contrastive Baseline for Open-domain Visual Entity Recognition](https://arxiv.org/abs/2603.09921)

**基本信息**

- 🔗 arXiv: [`2603.09921`](https://arxiv.org/abs/2603.09921)
- 👥 作者: Shan Ning, Longtian Qiu, Jiaxuan Sun 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09921.pdf)

**💡 相关性分析**

满足标准1和2：论文的核心研究内容是一种高效的开放域视觉实体识别方法，该方法利用大语言模型嵌入和视觉-语言对比学习。虽然应用领域是通用实体识别，但其技术核心——如何将视觉信息与来自知识库（如Wikipedia）的文本/实体信息进行高效对齐和检索——与“质谱结构推理”中需要将质谱数据（可视为一种“视觉”或“数值”模式）与分子结构数据库进行关联的任务在方法论上高度相似。因此，该研究在跨模态对齐和检索方面提供了相关的技术参考（满足标准1）。同时，论文构建的方法框架本身也可被视为一种可用于化学信息学的工具或基线模型（满足标准2）。

**📖 中文摘要**

本文重新审视了对比学习范式用于开放域视觉实体识别（VER），并介绍了WikiCLIP，一个简单而有效的框架，为开放域VER建立了一个强大且高效的基线。WikiCLIP利用大语言模型嵌入作为知识丰富的实体表示，并通过视觉引导知识适配器（VGKA）对其进行增强，该适配器在图像块级别将文本语义与视觉线索对齐。为了进一步鼓励细粒度区分，硬负样本合成机制在训练期间生成视觉相似但语义不同的负样本。在流行的开放域VER基准（如OVEN）上的实验结果表明，WikiCLIP显著优于强基线。具体来说，WikiCLIP在具有挑战性的OVEN未见集上实现了16%的改进，同时与领先的生成模型AutoVER相比，推理延迟减少了近100倍。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Open-domain visual entity recognition (VER) seeks to associate images with entities in encyclopedic knowledge bases such as Wikipedia. Recent generative methods tailored for VER demonstrate strong performance but incur high computational costs, limiting their scalability and practical deployment. In this work, we revisit the contrastive paradigm for VER and introduce WikiCLIP, a simple yet effective framework that establishes a strong and efficient baseline for open-domain VER. WikiCLIP leverages large language model embeddings as knowledge-rich entity representations and enhances them with a Vision-Guided Knowledge Adaptor (VGKA) that aligns textual semantics with visual cues at the patch level. To further encourage fine-grained discrimination, a Hard Negative Synthesis Mechanism generates visually similar but semantically distinct negatives during training. Experimental results on popular open-domain VER benchmarks, such as OVEN, demonstrate that WikiCLIP significantly outperforms strong baselines. Specifically, WikiCLIP achieves a 16% improvement on the challenging OVEN unseen set, while reducing inference latency by nearly 100 times compared with the leading generative model, AutoVER. The project page is available at this https URL

</details>

---

### 54. [Adaptive Clinical-Aware Latent Diffusion for Multimodal Brain Image Generation and Missing Modality Imputation](https://arxiv.org/abs/2603.09931)

**基本信息**

- 🔗 arXiv: [`2603.09931`](https://arxiv.org/abs/2603.09931)
- 👥 作者: Rong Zhou, Houliang Zhou, Yao Su 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09931.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是一种基于扩散模型的多模态医学图像生成和缺失模态补全方法。虽然应用领域是医学影像，但其核心技术——利用生成式模型（扩散模型）和跨模态信息（包括临床元数据）来合成或补全缺失的数据模态——与“质谱结构推理”中可能遇到的挑战（如仅有质谱数据，需要推断结构或其他光谱数据）在问题定义和技术路径上具有高度的相似性和启发性。因此，该研究与核心主题相关。

**📖 中文摘要**

本文提出了ACADiff，一个通过自适应临床感知扩散来合成缺失脑成像模态的框架。ACADiff通过学习不完整多模态观察与目标模态之间的映射，在逐步去噪潜在表示的同时，关注可用的成像数据和临床元数据。该框架采用自适应融合，根据输入可用性动态重新配置，并通过GPT-4o编码的提示与语义临床指导相结合。三个专用生成器支持sMRI、FDG-PET和AV45-PET之间的双向合成。在ADNI受试者上的评估表明，ACADiff实现了卓越的生成质量，即使在极端80%缺失的情况下也能保持稳健的诊断性能，优于所有现有基线。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Multimodal neuroimaging provides complementary insights for Alzheimer's disease diagnosis, yet clinical datasets frequently suffer from missing modalities. We propose ACADiff, a framework that synthesizes missing brain imaging modalities through adaptive clinical-aware diffusion. ACADiff learns mappings between incomplete multimodal observations and target modalities by progressively denoising latent representations while attending to available imaging data and clinical metadata. The framework employs adaptive fusion that dynamically reconfigures based on input availability, coupled with semantic clinical guidance via GPT-4o-encoded prompts. Three specialized generators enable bidirectional synthesis among sMRI, FDG-PET, and AV45-PET. Evaluated on ADNI subjects, ACADiff achieves superior generation quality and maintains robust diagnostic performance even under extreme 80\% missing scenarios, outperforming all existing baselines. To promote reproducibility, code is available at this https URL

</details>

---

### 55. [Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions](https://arxiv.org/abs/2603.09938)

**基本信息**

- 🔗 arXiv: [`2603.09938`](https://arxiv.org/abs/2603.09938)
- 👥 作者: Mingyang Song, Mao Zheng
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09938.pdf)

**💡 相关性分析**

满足标准3：这是一篇针对‘大模型’（Large Language Models）这一广泛主题的全面综述，其中包含的模型合并技术、理论及应用讨论，为理解和构建化学等领域的大模型提供了重要的方法论和未来方向展望。

**📖 中文摘要**

这篇论文是关于大语言模型（LLM）时代模型合并（Model Merging）的全面综述。模型合并是一种无需额外训练即可将多个神经网络能力整合到单一统一模型中的范式。该论文提出了一个名为FUSE的四维分类法，系统地回顾了模型合并的理论基础（如损失景观几何、模式连接性）、算法（如权重平均、任务向量算术、稀疏化增强方法、专家混合架构等）、下游应用（如多任务学习、安全对齐、领域专业化）以及支持生态系统（开源工具、社区平台、评估基准）。虽然论文的核心主题是模型合并，而非直接的化学大模型或质谱结构推理，但它作为一篇针对“大模型”这一广泛主题的综述，深入讨论了如何组合和利用大模型（包括化学领域可能的大模型）的专业化能力，符合综述展望相关的标准。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Model merging has emerged as a transformative paradigm for combining the capabilities of multiple neural networks into a single unified model without additional training. With the rapid proliferation of fine-tuned large language models~(LLMs), merging techniques offer a computationally efficient alternative to ensembles and full retraining, enabling practitioners to compose specialized capabilities at minimal cost. This survey presents a comprehensive and structured examination of model merging in the LLM era through the \textbf{FUSE} taxonomy, a four-dimensional framework organized along \textbf{F}oundations, \textbf{U}nification Strategies, \textbf{S}cenarios, and \textbf{E}cosystem. We first establish the theoretical underpinnings of merging, including loss landscape geometry, mode connectivity, and the linear mode connectivity hypothesis. We then systematically review the algorithmic landscape, spanning weight averaging, task vector arithmetic, sparsification-enhanced methods, mixture-of-experts architectures, and evolutionary optimization approaches. For each method family, we analyze the core formulation, highlight representative works, and discuss practical trade-offs. We further examine downstream applications across multi-task learning, safety alignment, domain specialization, multilingual transfer, and federated learning. Finally, we survey the supporting ecosystem of open-source tools, community platforms, and evaluation benchmarks, and identify key open challenges including theoretical gaps, scalability barriers, and standardization needs. This survey aims to equip researchers and practitioners with a structured foundation for advancing model merging.

</details>

---

### 56. [PathMem: Toward Cognition-Aligned Memory Transformation for Pathology MLLMs](https://arxiv.org/abs/2603.09943)

**基本信息**

- 🔗 arXiv: [`2603.09943`](https://arxiv.org/abs/2603.09943)
- 👥 作者: Jinyue Li, Yuci Liang, Qiankun Li 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09943.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是设计一个用于整合结构化领域知识的多模态大语言模型框架。这直接围绕“化学大模型”主题，因为构建能够理解和推理化学与质谱知识的专业大模型需要类似PathMem的、能够处理领域特定结构化知识（如化学 taxonomy、质谱碎裂规则）的架构。

**📖 中文摘要**

这篇论文提出了PathMem，一个用于病理学多模态大语言模型（MLLM）的以记忆为中心的多模态框架。该框架受到人类病理学家分层记忆过程的启发，将结构化的病理学知识组织为长期记忆（LTM），并引入一个记忆转换器（Memory Transformer）来模拟从LTM到工作记忆（WM）的动态转换。其核心是通过多模态记忆激活和上下文感知的知识落地，实现下游推理的上下文感知记忆精炼。PathMem在多个基准测试中达到了最先进的性能。虽然该论文聚焦于病理学图像和文本，但其核心贡献——为专业领域（如化学、质谱）的大模型设计结构化知识整合与记忆控制机制——与构建能够处理复杂领域知识（如化学结构、质谱解析规则）的“化学大模型”在方法论上高度相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Computational pathology demands both visual pattern recognition and dynamic integration of structured domain knowledge, including taxonomy, grading criteria, and clinical evidence. In practice, diagnostic reasoning requires linking morphological evidence with formal diagnostic and grading criteria. Although multimodal large language models (MLLMs) demonstrate strong vision language reasoning capabilities, they lack explicit mechanisms for structured knowledge integration and interpretable memory control. As a result, existing models struggle to consistently incorporate pathology-specific diagnostic standards during reasoning. Inspired by the hierarchical memory process of human pathologists, we propose PathMem, a memory-centric multimodal framework for pathology MLLMs. PathMem organizes structured pathology knowledge as a long-term memory (LTM) and introduces a Memory Transformer that models the dynamic transition from LTM to working memory (WM) through multimodal memory activation and context-aware knowledge grounding, enabling context-aware memory refinement for downstream reasoning. PathMem achieves SOTA performance across benchmarks, improving WSI-Bench report generation (12.8% WSI-Precision, 10.1% WSI-Relevance) and open-ended diagnosis by 9.7% and 8.9% over prior WSI-based models.

</details>

---

### 57. [Quantum algorithm for anisotropic diffusion and convection equations with vector norm scaling](https://arxiv.org/abs/2603.08799)

**基本信息**

- 🔗 arXiv: [`2603.08799`](https://arxiv.org/abs/2603.08799)
- 👥 作者: Julien Zylberman, Thibault Fredon, Nuno F. Loureiro 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08799.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是构建一个增强型的多模态大语言模型（MLLM）。这直接属于“大模型”的研究范畴。论文重点解决了视觉编码中全局语义与局部细节的平衡问题，并引入了自适应机制，这些技术创新对于构建需要处理复杂多模态数据（如化学结构图像与文本描述）的“化学大模型”具有重要的借鉴意义。

**📖 中文摘要**

这篇论文提出了Granulon，一种基于DINOv3的新型多模态大语言模型，具有自适应粒度增强功能。Granulon引入了一个文本条件化的粒度控制器，根据文本输入的语义范围动态调整视觉抽象级别，以及一个自适应令牌聚合模块，执行粒度引导的池化和关系感知的聚类，以产生紧凑、语义丰富的视觉令牌。这种设计使得在单次前向传递中实现统一的“像素到细粒度到粗粒度”推理成为可能。广泛的实验表明，Granulon在相同设置下优于所有视觉编码器。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

In this work, we tackle the resolution of partial differential equations (PDEs) on digital quantum computers. Two fundamental PDEs are addressed: the anisotropic diffusion equation and the anisotropic convection equation. We present a quantum numerical scheme consisting of three steps: quantum state preparation, evolution with diagonal operators, and measurement of observables of interest. The evolution step relies on a high-order centered finite difference and a product formula approximation, also known as Trotterization. We provide novel vector-norm analysis to bound the different sources of error. We prove that the number of time-steps required in the evolution can be reduced by a factor $\Theta (16^n)$ for the diffusion equation, and $\Theta (4^n)$ for the convection equation, where $n$ is the number of qubits per dimension, an exponential reduction compared to the previously established operator-norm analysis.

</details>

---

### 58. [From Word2Vec to Transformers: Text-Derived Composition Embeddings for Filtering Combinatorial Electrocatalysts](https://arxiv.org/abs/2603.08881)

**基本信息**

- 🔗 arXiv: [`2603.08881`](https://arxiv.org/abs/2603.08881)
- 👥 作者: Lei Zhang, Markus Stricker
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08881.pdf)

**💡 相关性分析**

满足标准1：论文的核心是利用从科学文本中学习到的表示（嵌入）来指导材料发现和筛选。这直接涉及“化学大模型”的一个关键应用方向：学习化学实体的高质量表示，并将其用于预测和推理任务。

**📖 中文摘要**

这篇论文研究组合电催化剂的高通量筛选策略。面对巨大的组合空间，作者评估了一种无标签的筛选方法，该方法使用从科学文本中衍生的嵌入（embeddings）来表示每种材料组成，并基于与两个属性概念（‘导电性’和‘介电性’）的相似性来优先选择候选物。作者比较了基于语料库训练的Word2Vec基线模型与基于Transformer的嵌入方法（通过线性元素混合或简短组成提示进行编码）。在包含贵金属合金和多组分氧化物的15个材料库上进行了评估。这项工作展示了如何利用从文本数据中学习到的表示（嵌入）来指导材料发现，这种方法论与构建“化学大模型”以学习分子/材料表示并用于下游预测任务（如性质预测、结构推理）的核心思想一致。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Compositionally complex solid solution electrocatalysts span vast composition spaces, and even one materials system can contain more candidate compositions than can be measured exhaustively. Here we evaluate a label-free screening strategy that represents each composition using embeddings derived from scientific texts and prioritizes candidates based on similarity to two property concepts. We compare a corpus-trained Word2Vec baseline with transformer-based embeddings, where compositions are encoded either by linear element-wise mixing or by short composition prompts. Similarities to `concept directions', the terms conductivity and dielectric, define a 2-dimensional descriptor space, and a symmetric Pareto-front selection is used to filter candidate subsets without using electrochemical labels. Performance is assessed on 15 materials libraries including noble metal alloys and multicomponent oxides. In this setting, the lightweight Word2Vec baseline, which uses a simple linear combination of element embeddings, often achieves the highest number of reductions of possible candidate compositions while staying close to the best measured performance.

</details>

---

### 59. [A Generative Sampler for distributions with possible discrete parameter based on Reversibility](https://arxiv.org/abs/2603.09251)

**基本信息**

- 🔗 arXiv: [`2603.09251`](https://arxiv.org/abs/2603.09251)
- 👥 作者: Lei Li, Zhen Wang, Lishuo Zhang
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09251.pdf)

**💡 相关性分析**

满足标准1：论文提出了一种适用于离散和混合变量系统的生成式采样框架。这与“化学大模型”和“质谱结构推理”密切相关，因为分子结构生成、候选结构排序以及质谱碎裂过程的概率建模都可以视为从复杂分布中采样的任务。

**📖 中文摘要**

这篇论文提出了一种统一的、无需目标梯度的生成式采样框架，适用于连续、离散或混合变量系统。该方法基于细致平衡条件意味着平衡随机过程的时间可逆性这一事实，将这种对称性作为统计约束来执行。使用规定的物理转移核（如Metropolis-Hastings），最小化前向和后向马尔可夫轨迹的联合分布之间的最大平均差异（MMD）。训练过程仅通过接受比进行能量评估，绕过了对目标评分函数或连续松弛的需求。论文在三个不同的基准上进行了演示，包括离散高维伊辛模型。该方法为从复杂非归一化分布中采样提供了一种物理基础且普遍适用的替代方案。生成式采样和概率建模是“化学大模型”和“质谱结构推理”中的核心组成部分，例如用于生成候选分子结构或对质谱碎片化过程进行概率建模。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Learning to sample from complex unnormalized distributions is a fundamental challenge in computational physics and machine learning. While score-based and variational methods have achieved success in continuous domains, extending them to discrete or mixed-variable systems remains difficult due to ill-defined gradients or high variance in estimators. We propose a unified, target-gradient-free generative sampling framework applicable across diverse state spaces. Building on the fact that detailed balance implies the time-reversibility of the equilibrium stochastic process, we enforce this symmetry as a statistical constraint. Specifically, using a prescribed physical transition kernel (such as Metropolis-Hastings), we minimize the Maximum Mean Discrepancy (MMD) between the joint distributions of forward and backward Markov trajectories. Crucially, this training procedure relies solely on energy evaluations via acceptance ratios, circumventing the need for target score functions or continuous relaxations. We demonstrate the versatility of our method on three distinct benchmarks: (1) a continuous multi-modal Gaussian mixture, (2) the discrete high-dimensional Ising model, and (3) a challenging hybrid system coupling discrete indices with continuous dynamics. Experiments show that our framework accurately reproduces thermodynamic observables and captures mode-switching behavior across all regimes, offering a physically grounded and universally applicable alternative for equilibrium sampling.

</details>

---

### 60. [First Estimation of Model Parameters for Neutrino-Induced Nucleon Knockout Using Simulation-Based Inference](https://arxiv.org/abs/2603.09778)

**基本信息**

- 🔗 arXiv: [`2603.09778`](https://arxiv.org/abs/2603.09778)
- 👥 作者: Karla Tame-Narvaez, Steven Gardiner, Aleksandra Ćiprijanović 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.09778.pdf)

**💡 相关性分析**

满足标准1：论文的核心是使用基于模拟的推理（SBI）从实验数据中估计复杂物理模拟器的模型参数。这直接围绕“质谱结构推理”主题，因为质谱解析的本质就是从观测到的质谱数据（模拟器的输出）反向推断产生该谱图的分子结构（模拟器的输入参数）。SBI为此类逆问题提供了强大的框架。

**📖 中文摘要**

这篇论文首次将基于模拟的推理（Simulation-Based Inference, SBI）应用于中微子诱导核子敲出反应的模型参数估计。为了改进中微子振荡实验的模拟，需要调整核相互作用物理模型的参数。传统的经验调参方法复杂，而该研究利用SBI这一机器学习技术来处理未来可能更复杂的模型调优。作者重新审视了由MicroBooNE合作组织开发的GENIE中微子事件生成器的调优配置，并使用SBI算法从实验数据中推断物理参数。结果表明，SBI可以近似替代传统调参，并可能实现更好的拟合。这项工作展示了SBI在从复杂模拟器（如化学或质谱模拟器）和实验数据中联合推断模型参数方面的潜力，这与“质谱结构推理”中从质谱数据反推分子结构参数的任务在方法论上相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

To enable an accurate determination of oscillation parameters, accelerator-based neutrino experiments require detailed simulations of nuclear interaction physics in the GeV regime. While substantial effort from both theory and experiment is currently being invested to improve the fidelity of these simulations, their present deficiencies typically oblige experimental collaborations to resort to empirical tuning of simulation model parameters. As the precision requirements of the field continue to become more stringent, machine learning techniques may provide a powerful means of handling corresponding growth in the complexity of future neutrino interaction model tuning exercises. To study the suitability of simulation-based inference (SBI) for this physics application, in this paper we revisit a tuned configuration of the GENIE neutrino event generator that was originally developed by the MicroBooNE collaboration. Despite closely reproducing the adopted values of four physics parameters when confronted with the tuned cross-section predictions as input, we find that our trained SBI algorithm prefers modestly different values (within MicroBooNE's assigned uncertainties) and achieves slightly better goodness-of-fit when inference is run on the experimental data set originally used by MicroBooNE. We also find that our trained algorithm can create a fair approximation of an alternative neutrino scattering simulation, NuWro, that shares only a subset of its physics model parameters with GENIE.

</details>

---

### 61. [Learning with Errors over Group Rings Constructed by Semi-direct Product](https://arxiv.org/abs/2311.15868)

**基本信息**

- 🔗 arXiv: [`2311.15868`](https://arxiv.org/abs/2311.15868)
- 👥 作者: Jiaqi Liu, Fang-Wei Fu
- 📄 PDF: [下载](https://arxiv.org/pdf/2311.15868.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是基于非交换群环的Learning with Errors问题，这是一种将复杂代数结构（群环）与机器学习基础问题（带误差学习）相结合的理论研究。虽然应用领域是密码学，但这种“结构化表示上的学习问题”的形式化分析与“化学大模型”中利用分子图、对称性等代数结构进行表示学习和推理的理论探索高度相关。

**📖 中文摘要**

这篇论文研究一种称为群环学习带误差（Group Ring Learning with Errors, GRLWE）的代数变体LWE问题。作者选择了由两个循环群半直积构造的有限群所对应的群环（或其直和项）作为基础结构。与经典的Ring-LWE不同，这里的乘法运算是非交换的。论文提出了两个多项式时间的量子归约证明：1) 从理想格中具有多项式近似因子的最坏情况最短独立向量问题（SIVP）到GRLWE搜索版本的量子归约；2) 对于两类特定的群环，将最坏情况SIVP问题直接归约到（平均情况）决策GRLWE问题的量子归约。GRLWE的伪随机性可用于构建语义安全的公钥密码系统。虽然论文属于密码学领域，但其研究的GRLWE问题是构建后量子密码学的基础。而设计安全的、能够处理化学数据的“化学大模型”可能需要考虑数据隐私和加密计算，因此理解此类基础密码学原语具有相关性。更直接的是，论文对非交换代数结构上LWE问题的形式化分析和归约证明，展示了将复杂代数结构应用于学习问题的理论框架，这与“化学大模型”中利用分子图、对称群等代数结构进行表示学习在精神上有共通之处。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The Learning with Errors (\LWE) problem has been widely utilized as a foundation for numerous cryptographic tools over the years. In this study, we focus on an algebraic variant of the \LWE problem called \emph{Group ring} \LWE ($\GRLWE$). We select group rings (or their direct summands) that underlie specific families of finite groups constructed by taking the semi-direct product of two cyclic groups. Unlike the Ring-\LWE problem described in \cite{lyubashevsky2010ideal}, the multiplication operation in the group rings considered here is non-commutative. As an extension of Ring-$\LWE$, it maintains computational hardness and can be potentially applied in many cryptographic scenarios. In this paper, we present two polynomial-time quantum reductions. Firstly, we provide a quantum reduction from the worst-case shortest independent vectors problem (\SIVP) in ideal lattices with polynomial approximate factor to the search version of $\GRLWE$. This reduction requires that the underlying group ring possesses certain mild properties; Secondly, we present another quantum reduction for two types of group rings, where the worst-case \SIVP problem is directly reduced to the (average-case) decision $\GRLWE$ problem. The pseudorandomness of $\GRLWE$ samples guaranteed by this reduction can be consequently leveraged to construct semantically secure public-key cryptosystems.

</details>

---

### 62. [Scalable Message Passing Neural Networks: No Need for Attention in Large Graph Representation Learning](https://arxiv.org/abs/2411.00835)

**基本信息**

- 🔗 arXiv: [`2411.00835`](https://arxiv.org/abs/2411.00835)
- 👥 作者: Haitz Sáez de Ocáriz Borde, Artem Lukoianov, Anastasis Kratsios 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2411.00835.pdf)

**💡 相关性分析**

满足标准1：论文提出的可扩展消息传递神经网络（SMPNNs）是构建化学大模型（特别是基于分子图的模型）的核心技术之一，其研究内容直接围绕图表示学习这一化学信息学和化学大模型的基础。

**📖 中文摘要**

本文提出了可扩展消息传递神经网络（SMPNNs），这是一种基于图神经网络（GNNs）的新型架构。它通过将标准卷积消息传递集成到Transformer风格的块中，取代了注意力机制，从而构建了高性能的深度消息传递GNNs。该模型在大型图表示学习任务中表现出色。虽然论文主要关注通用图学习，但其提出的可扩展、高性能的图神经网络架构和方法，为处理化学信息学中常见的分子图数据（如分子结构图）提供了强大的工具。这类图神经网络是构建化学大模型（用于分子性质预测、生成等）的核心组件之一。因此，该论文提出的方法直接与“化学大模型”这一主题相关。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We propose Scalable Message Passing Neural Networks (SMPNNs) and demonstrate that, by integrating standard convolutional message passing into a Pre-Layer Normalization Transformer-style block instead of attention, we can produce high-performing deep message-passing-based Graph Neural Networks (GNNs). This modification yields results competitive with the state-of-the-art in large graph transductive learning, particularly outperforming the best Graph Transformers in the literature, without requiring the otherwise computationally and memory-expensive attention mechanism. Our architecture not only scales to large graphs but also makes it possible to construct deep message-passing networks, unlike simple GNNs, which have traditionally been constrained to shallow architectures due to oversmoothing. Moreover, we provide a new theoretical analysis of oversmoothing based on universal approximation which we use to motivate SMPNNs. We show that in the context of graph convolutions, residual connections are necessary for maintaining the universal approximation properties of downstream learners and that removing them can lead to a loss of universality.

</details>

---

### 63. [The Gaussian-Multinoulli Restricted Boltzmann Machine: A Potts Model Extension of the GRBM](https://arxiv.org/abs/2505.11635)

**基本信息**

- 🔗 arXiv: [`2505.11635`](https://arxiv.org/abs/2505.11635)
- 👥 作者: Nikhil Kapasi, Mohamed Elfouly, William Whitehead 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.11635.pdf)

**💡 相关性分析**

满足标准1：论文提出的高斯-多项受限玻尔兹曼机（GM-RBM）是一种新型的生成式能量模型，专注于学习离散、结构化的表示。这类模型是化学信息学中构建分子表示、生成模型（化学大模型的一个子类）的重要基础，其研究内容与化学大模型的架构探索直接相关。

**📖 中文摘要**

本文提出了高斯-多项受限玻尔兹曼机（GM-RBM），这是一种生成式能量模型，通过用q状态分类（Potts）单元替换二元隐藏单元，扩展了高斯-伯努利RBM（GB-RBM）。该模型旨在为多值概念提供更丰富的潜在状态空间，适用于联想记忆和符号推理等任务。论文详细推导了能量函数、条件分布和学习规则，并提供了避免状态崩溃的实用训练选择。在类比回忆和结构化记忆基准测试中，GM-RBM展示了其处理离散、结构化表示的能力。虽然论文未明确针对化学领域，但受限玻尔兹曼机及其变体是深度学习在化学信息学中用于分子表示学习、生成和性质预测的经典模型之一。GM-RBM作为一种具有更丰富离散潜在空间的生成模型，为化学大模型中分子结构的表示和生成提供了新的可能架构。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Many real-world tasks, from associative memory to symbolic reasoning, benefit from discrete, structured representations that standard continuous latent models can struggle to express. We introduce the Gaussian-Multinoulli Restricted Boltzmann Machine (GM-RBM), a generative energy-based model that extends the Gaussian-Bernoulli RBM (GB-RBM) by replacing binary hidden units with q-state categorical (Potts) units, yielding a richer latent state space for multivalued concepts. We provide a self-contained derivation of the energy, conditional distributions, and learning rules, and detail practical training choices (contrastive divergence with temperature annealing and intra-slot diversity constraints) that avoid state collapse. To separate architectural effects from sheer latent capacity, we evaluate under both capacity-matched and parameter-matched setups, comparing GM-RBM with GB-RBM configured to have the same number of possible latent assignments. On analogical recall and structured memory benchmarks, GM-RBM achieves competitive, and in several regimes improved, recall at equal capacity with comparable training cost, despite using only Gibbs updates. The discrete q-ary formulation is also amenable to efficient implementation. These results clarify when categorical hidden units provide a simple, scalable alternative to binary latents for discrete inference within tractable RBMs.

</details>

---

### 64. [Discovering Symbolic Differential Equations with Symmetry Invariants](https://arxiv.org/abs/2505.12083)

**基本信息**

- 🔗 arXiv: [`2505.12083`](https://arxiv.org/abs/2505.12083)
- 👥 作者: Jianke Yang, Manu Bhat, Bryan Hu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2505.12083.pdf)

**💡 相关性分析**

满足标准1：论文提出的基于对称不变量的符号微分方程发现方法，其研究范式（利用领域知识约束模型发现）与化学信息学中从复杂数据（如质谱、动力学数据）发现可解释的化学模型或规律（质谱结构推理的终极目标之一）直接相关，为构建可解释的化学推理模型提供了方法论支持。

**📖 中文摘要**

本文提出了一种利用对称不变量从数据中发现符号微分方程的新方法。现有方法通常在巨大的方程搜索空间中挣扎，并且可能产生违反已知物理定律的方程。本文通过引入对称不变量的概念来解决这些问题，利用微分方程若允许一个对称群，则可以用对称变换的微分不变量来表示这一事实。因此，作者提出在方程发现中使用这些不变量作为原子实体，确保发现的方程满足指定的对称性。该方法可以与稀疏回归和遗传编程等现有方程发现方法无缝集成，提高其准确性和效率。论文通过在流体和反应-扩散等各种物理系统上的应用验证了所提方法。虽然论文侧重于物理系统，但其核心方法——利用领域知识（对称性）约束和指导符号模型的发现——与化学信息学中“从数据中发现化学定律或模型”（例如，从光谱或反应数据中推断模型）的研究范式高度一致。该方法为构建可解释的、符合物理化学原理的“化学大模型”或推理模型提供了有力的工具。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Discovering symbolic differential equations from data uncovers fundamental dynamical laws underlying complex systems. However, existing methods often struggle with the vast search space of equations and may produce equations that violate known physical laws. In this work, we address these problems by introducing the concept of symmetry invariants in equation discovery. We leverage the fact that differential equations admitting a symmetry group can be expressed in terms of differential invariants of symmetry transformations. Thus, we propose to use these invariants as atomic entities in equation discovery, ensuring the discovered equations satisfy the specified symmetry. Our approach integrates seamlessly with existing equation discovery methods such as sparse regression and genetic programming, improving their accuracy and efficiency. We validate the proposed method through applications to various physical systems, such as fluid and reaction-diffusion, demonstrating its ability to recover parsimonious and interpretable equations that respect the laws of physics.

</details>

---

### 65. [Evaluating Large Language Models for Multilingual Vulnerability Detection at Dual Granularities](https://arxiv.org/abs/2506.07503)

**基本信息**

- 🔗 arXiv: [`2506.07503`](https://arxiv.org/abs/2506.07503)
- 👥 作者: Honglin Shu, Michael Fu, Junji Yu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2506.07503.pdf)

**💡 相关性分析**

满足标准1：论文的核心是对大语言模型（LLMs）在特定专业领域（代码）进行复杂推理和检测任务能力的系统性评估。该研究范式、评估方法及关于LLMs能力的结论，对于研究和开发应用于化学领域的“化学大模型”（处理分子、反应、光谱等复杂数据）具有直接的借鉴和参考意义。

**📖 中文摘要**

本文对最先进的预训练语言模型（PLMs）和大语言模型（LLMs）在多语言漏洞检测中的有效性进行了全面的实证研究。研究使用跨越七种编程语言的超过30,000个真实世界漏洞修复补丁，系统地评估了模型在函数级和行级的性能。关键发现表明，通过指令微调和少量提示增强的GPT-4o显著优于所有其他评估模型。此外，基于LLM的方法在检测独特的跨语言漏洞方面表现出卓越的能力。虽然论文聚焦于软件安全，但其核心是评估和利用大语言模型（LLMs）处理复杂、结构化信息（代码）并进行推理的能力。这种对LLMs在专业领域（此处是代码）的推理、理解和检测能力的深入评估，其方法论和结论对于探索LLMs在另一个专业领域——化学（即“化学大模型”）——的潜力具有重要的参考价值。研究展示了如何系统性地评估和提升大模型在特定科学或工程领域的任务表现。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Various deep learning-based approaches utilizing pre-trained language models (PLMs) have been proposed for automated vulnerability detection. With recent advancements in large language models (LLMs), several studies have begun exploring their application to vulnerability detection tasks. However, existing studies primarily focus on specific programming languages (e.g., C/C++) and function-level detection, leaving the strengths and weaknesses of PLMs and LLMs in multilingual and multi-granularity scenarios largely unexplored. To bridge this gap, we conduct a comprehensive fine-grained empirical study evaluating the effectiveness of state-of-the-art PLMs and LLMs for multilingual vulnerability detection. Using over 30,000 real-world vulnerability-fixing patches across seven programming languages, we systematically assess model performance at both the function-level and line-level. Our key findings indicate that GPT-4o, enhanced through instruction tuning and few-shot prompting, significantly outperforms all other evaluated models, including CodeT5P. Furthermore, the LLM-based approach demonstrates superior capability in detecting unique multilingual vulnerabilities, particularly excelling in identifying the most dangerous and high-severity vulnerabilities. These results underscore the promising potential of adopting LLMs for multilingual vulnerability detection at function-level and line-level, revealing their complementary strengths and substantial improvements over PLM approaches. This empirical evaluation of PLMs and LLMs for multilingual vulnerability detection highlights LLMs' value in addressing real-world software security challenges.

</details>

---

### 66. [OPENXRD: A Comprehensive Benchmark Framework for LLM/MLLM XRD Question Answering](https://arxiv.org/abs/2507.09155)

**基本信息**

- 🔗 arXiv: [`2507.09155`](https://arxiv.org/abs/2507.09155)
- 👥 作者: Ali Vosoughi, Ayoub Shahnazari, Yufeng Xi 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.09155.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心是构建和评估用于科学领域（晶体学）的大模型基准。这直接与“化学大模型”的主题相关（标准1），因为它提供了评估化学领域大模型性能的方法论范例。同时，论文对多种大模型在科学领域知识同化能力的系统性分析和结论，构成了对该主题的重要讨论和展望（标准3）。

**📖 中文摘要**

本文介绍了OPENXRD，一个用于评估大语言模型（LLMs）和多模态大语言模型（MLLMs）在晶体学问答任务中表现的综合基准框架。该框架衡量模型的上下文同化能力，即模型在推理过程中如何使用固定的、特定领域的支持信息。框架包含217个专家策划的X射线衍射（XRD）问题，涵盖从基础到高级的晶体学概念。作者对74个最先进的LLMs和MLLMs进行了基准测试，以量化不同架构和规模的模型如何同化外部知识。结果表明，中型模型（7B-70B参数）从上下文材料中获益最多。专家评审的材料即使在与AI生成材料token数量匹配的情况下，也能提供显著更高的性能提升，证实了内容质量（而非数量）驱动性能。OPENXRD为评估科学领域中的推理、知识整合和指导敏感性提供了一个可重复的诊断基准。虽然主题是晶体学，但其构建的“领域科学问答基准”的方法论，以及关于大模型如何吸收和利用领域专业知识（如化学、材料科学知识）的深入分析，与“化学大模型”的研究高度相关。它为如何构建和评估化学领域的大模型基准提供了范例。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce OPENXRD, a comprehensive benchmarking framework for evaluating large language models (LLMs) and multimodal LLMs (MLLMs) in crystallography question answering. The framework measures context assimilation, or how models use fixed, domain-specific supporting information during inference. The framework includes 217 expert-curated X-ray diffraction (XRD) questions covering fundamental to advanced crystallographic concepts, each evaluated under closed-book (without context) and open-book (with context) conditions, where the latter includes concise reference passages generated by GPT-4.5 and refined by crystallography experts. We benchmark 74 state-of-the-art LLMs and MLLMs, including GPT-4, GPT-5, O-series, LLaVA, LLaMA, QWEN, Mistral, and Gemini families, to quantify how different architectures and scales assimilate external knowledge. Results show that mid-sized models (7B--70B parameters) gain the most from contextual materials, while very large models often show saturation or interference and the largest relative gains appear in small and mid-sized models. Expert-reviewed materials provide significantly higher improvements than AI-generated ones even when token counts are matched, confirming that content quality, not quantity, drives performance. OPENXRD offers a reproducible diagnostic benchmark for assessing reasoning, knowledge integration, and guidance sensitivity in scientific domains, and provides a foundation for future multimodal and retrieval-augmented crystallography systems.

</details>

---

### 67. [Improving Large Vision-Language Models' Understanding for Flow Field Data](https://arxiv.org/abs/2507.18311)

**基本信息**

- 🔗 arXiv: [`2507.18311`](https://arxiv.org/abs/2507.18311)
- 👥 作者: Xiaomei Zhang, Hanyu Zheng, Xiangyu Zhu 等7人
- 📄 PDF: [下载](https://arxiv.org/pdf/2507.18311.pdf)

**💡 相关性分析**

满足标准1：论文提出的FieldLVLM框架专注于提升大模型对复杂科学数据（场数据）的理解和推理能力。其技术路线（特征提取、结构化描述生成、数据压缩微调）为构建能够处理化学领域复杂数据（如质谱图、分子结构、反应路径）的“化学大模型”或“质谱结构推理模型”提供了创新的方法论和具体实现思路。

**📖 中文摘要**

本文提出了FieldLVLM，一个旨在提升大视觉-语言模型（LVLMs）对场数据（如流场数据）理解能力的新框架。FieldLVLM包含两个主要组件：场感知语言生成策略和数据压缩的多模态模型调优。场感知语言生成策略利用专用的机器学习流程从场数据中提取关键物理特征（如流动分类、雷诺数、涡旋模式），并将其转换为结构化的文本描述作为数据集。数据压缩的多模态模型调优则使用这些生成的数据集对LVLMs进行微调，采用数据压缩策略降低场输入的复杂性，仅保留最具信息量的值。实验结果表明，FieldLVLM在新提出的基准数据集上显著优于现有方法。这项工作展示了将大视觉-语言模型应用于科学领域数据（如物理化学中的流场、浓度场等）的新可能性。虽然论文侧重于流体力学等物理场，但其核心思想——让大模型理解和推理复杂的、结构化的科学数据——与“化学大模型”处理化学结构、光谱图、分子动力学轨迹等复杂数据的愿景完全一致。该框架为化学领域类似任务（例如，从分子模拟轨迹或光谱图中提取特征并生成描述/推理）提供了直接的技术参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large Vision-Language Models (LVLMs) have shown impressive capabilities across a range of tasks that integrate visual and textual understanding, such as image captioning and visual question answering. These models are trained on large-scale image and video datasets paired with text, enabling them to bridge visual perception and natural language processing. However, their application to scientific domains, especially in interpreting complex field data commonly used in the natural sciences, remains underexplored. In this work, we introduce FieldLVLM, a novel framework designed to improve large vision-language models' understanding of field data. FieldLVLM consists of two main components: a field-aware language generation strategy and a data-compressed multimodal model tuning. The field-aware language generation strategy leverages a special-purpose machine learning pipeline to extract key physical features from field data, such as flow classification, Reynolds number, and vortex patterns. This information is then converted into structured textual descriptions that serve as a dataset. The data-compressed multimodal model tuning focuses on LVLMs with these generated datasets, using a data compression strategy to reduce the complexity of field inputs and retain only the most informative values. This ensures compatibility with the models language decoder and guides its learning more effectively. Experimental results on newly proposed benchmark datasets demonstrate that FieldLVLM significantly outperforms existing methods in tasks involving scientific field data. Our findings suggest that this approach opens up new possibilities for applying large vision-language models to scientific research, helping bridge the gap between large models and domain-specific discovery.

</details>

---

### 68. [RF-Informed Graph Neural Networks for Accurate and Data-Efficient Circuit Performance Prediction](https://arxiv.org/abs/2508.16403)

**基本信息**

- 🔗 arXiv: [`2508.16403`](https://arxiv.org/abs/2508.16403)
- 👥 作者: Anahita Asadi, Leonid Popryho, Inna Partin-Vaisband
- 📄 PDF: [下载](https://arxiv.org/pdf/2508.16403.pdf)

**💡 相关性分析**

满足标准1：论文提出的结合领域知识的图神经网络（GNN）框架，其方法论（领域知识注入的图表示、跨拓扑泛化）与化学信息学中利用GNN构建分子性质预测模型（化学大模型的核心任务之一）的研究直接相关，为解决化学领域的类似问题提供了新颖且高效的技术思路。

**📖 中文摘要**

本文提出了一种轻量级、数据高效且具有拓扑感知能力的图神经网络（GNN）框架，用于预测有源射频（RF）电路（如低噪声放大器、混频器、压控振荡器和功率放大器）的关键性能指标。该框架采用射频集成电路领域知识启发的特征索引，通过对功能器件语义（如差分对和变容二极管晶体管）进行廉价编码，实现跨拓扑结构的适应性和高效的知识迁移。代理模型使用器件-端子图抽象来表示电路，以保留细粒度的连接性和晶体管级对称性。实验结果表明，该方法能够准确建模多模态和重尾的射频性能分布，平均相对误差为3.45%，比现有技术提高了9.2倍。此外，该方法将类别级泛化性能提高了约161倍。虽然应用领域是电子设计自动化，但其核心贡献在于提出了一种结合领域知识（化学信息学中称为“领域指纹”或“先验知识”）的图神经网络方法，用于对具有复杂拓扑结构（图结构）的物体进行性能预测。这与化学信息学中利用GNN预测分子性质（分子也是图结构）的任务高度同构。论文中“RFIC领域知识启发的特征索引”和“器件-端子图抽象”等方法，可以直接类比到化学信息学中的“原子/化学键类型编码”和“分子图表示”，为构建更精准、数据高效的化学性质预测大模型提供了有价值的架构参考。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Accurately predicting the performance of active radio frequency (RF) circuits is essential for modern wireless systems but remains challenging due to highly nonlinear, layout-sensitive behavior and the high computational cost of traditional simulation tools. Existing machine learning (ML) surrogates often require large datasets to generalize across various topologies or are not accurate on unseen circuits. This work presents a lightweight, data-efficient, and topology-aware graph neural network (GNN) framework for predicting key performance metrics of active RF circuit classes, such as low-noise amplifiers (LNAs), mixers, voltage-controlled oscillators (VCOs), and power amplifiers (PAs). The proposed framework employs RFIC domain-informed feature indexing to enable cross-topology adaptability by cheap encoding of functional device semantics (e.g., differential pair and varactor transistors) and efficient knowledge transfer. The surrogate model represents circuits using device-terminal graph abstractions to preserve fine-grained connectivity and transistor-level symmetry. The final model is generalized to a wide variety of classes by being trained in parallel. Experimental results demonstrate accurate modeling of multimodal and heavy-tailed RF performance distributions, achieving an average mean relative error (MRE) of 3.45%, an improvement of 9.2x compared to state-of-the-art. Furthermore, the method improves class-level generalization performance by ~161x compared to prior art, demonstrating its effectiveness for scalable and deployment-ready RF design automation.

</details>

---

### 69. [Does Scientific Writing Converge to U.S. English? Evidence from Generative AI-Assisted Publications](https://arxiv.org/abs/2511.11687)

**基本信息**

- 🔗 arXiv: [`2511.11687`](https://arxiv.org/abs/2511.11687)
- 👥 作者: Dragan Filimonovic, Christian Rutzer, Jeffrey Macher 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.11687.pdf)

**💡 相关性分析**

满足标准3：论文虽然不是直接关于化学信息学或质谱分析，但其核心研究内容是生成式人工智能（GenAI）如何改变科学写作。鉴于“化学大模型”是生成式AI在化学领域的具体应用，本文对GenAI在科学领域（包括化学）的宏观影响、使用模式及其后果（如风格趋同）进行了重要的相关讨论，属于对相关主题的展望性分析。

**📖 中文摘要**

本文研究了生成式人工智能（GenAI）对科学写作风格的影响，特别是其是否导致非英语母语国家作者的写作风格向占主导地位的美国科学英语趋同。研究分析了2021年至2024年间Scopus索引的565万篇英文科学文章，采用事件研究双重差分法，以ChatGPT发布为时间节点。研究发现，来自非英语国家的GenAI辅助发表的论文，其语言风格显著地向美国科学英语趋同，这种效应在语言上与英语差异较大的国家、国内作者团队以及影响力较低的期刊中尤为明显。这项工作揭示了GenAI工具正在改变科学交流的语言格局，可能降低语言相关的发表障碍。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

A growing literature documents that generative artificial intelligence (GenAI) is changing scientific writing, yet most studies focus on absolute changes in vocabulary or readability. An important question remains unanswered: Does GenAI use lead to systematic convergence, or a narrowing of stylistic gaps relative to the dominant form of scientific English? Unlike absolute changes, convergence signals whether language-related publication barriers are declining and suggests broader implications for participation and competition in global science. This study directly addresses this question using 5.65 million English-language scientific articles published from 2021 to 2024 and indexed in Scopus. We measure linguistic similarity to a U.S. benchmark corpus using SciBERT text embeddings, and estimate dynamic changes using an event-study difference-in-differences design with repeated cross-sections centered on the late-2022 release of ChatGPT. We find that GenAI-assisted publications from non-English-speaking countries exhibit statistically significant and increasing convergence toward U.S. scientific English, relative to non-GenAI-assisted publications from these countries. This effect is strongest for domestic author teams from countries more linguistically distant from English and for articles published in lower-impact journals -- precisely the contexts where language barriers have historically been most consequential. The results suggest that GenAI tools are reducing language-related barriers in scientific publications. Whether this represents genuine inclusion or a deepening dependence on a single linguistic standard remains an open question.

</details>

---

### 70. [TSFM in-context learning for time-series classification of bearing-health status](https://arxiv.org/abs/2511.15447)

**基本信息**

- 🔗 arXiv: [`2511.15447`](https://arxiv.org/abs/2511.15447)
- 👥 作者: Michel Tokic, Slobodan Djukanović, Anja von Beuningen 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.15447.pdf)

**💡 相关性分析**

满足标准1和2：1. 核心主题相关：论文的核心是利用时间序列基础模型（TSFM）进行模式识别和分类，这属于“化学大模型”中基础模型在科学数据分析（此处是振动/传感器数据分析）中的应用。2. 数据资源相关：论文提出了一种新颖的、基于TSFM上下文学习的分类方法框架，这本身是一种可用于时序数据分析（类比于质谱时序信号）的工具或方法论资源。

**📖 中文摘要**

本文提出了一种基于时间序列基础模型（TSFM）上下文学习（in-context learning）的分类方法，无需对基础模型进行微调或训练传统分类模型。该方法将示例（包括类别标签和数据矩阵）表示为TSFM提示的一部分，通过上下文学习对未知数据的模式进行分类。作者将该方法应用于振动数据，以评估伺服压力机电机中轴承的健康状态。该方法将频域参考信号转换为伪时间序列模式，生成对齐的协变量和目标信号，并利用TSFM预测预定义标签的类别归属概率。该方法利用了预训练模型的可扩展性，在不同操作条件下均表现出有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce a classification method based on in-context learning using time-series foundation models (TSFMs). We demonstrate how data not included in the TSFM training can be classified without fine-tuning the foundation model or training a traditional classification model. Examples are represented as targets (class labels) and covariates (data matrices) within the TSFM prompt, enabling the classification of unknown covariate data patterns alongside the forecast horizon through in-context learning. We apply this method to vibration data to assess the health state of a bearing within a servo-press motor. The method transforms frequency-domain reference signals into pseudo time-series patterns, generates aligned covariate and target signals, and uses the TSFM to predict class-membership probabilities for predefined labels. Leveraging the scalability of pre-trained models, the proposed method demonstrates effectiveness across varying operational conditions. This represents significant progress beyond traditional, custom AI solutions towards broader AI-driven maintenance systems that could potentially be provided as Model- or Software-as-a-Service applications.

</details>

---

### 71. [Research and Prototyping Study of an LLM-Based Chatbot for Electromagnetic Simulations](https://arxiv.org/abs/2511.17680)

**基本信息**

- 🔗 arXiv: [`2511.17680`](https://arxiv.org/abs/2511.17680)
- 👥 作者: Albert Piwonski, Mirsad Hadžiefendić
- 📄 PDF: [下载](https://arxiv.org/pdf/2511.17680.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个基于大语言模型（LLM）的聊天机器人，用于自动化科学仿真（电磁仿真）模型的设置。这直接属于“化学大模型”的广义范畴，即利用大模型技术辅助或自动化科学研究流程（在此是仿真建模），展示了LLM作为科学智能体在专业领域的应用。

**📖 中文摘要**

本研究探讨了如何利用生成式人工智能（基于大语言模型）来减少电磁仿真模型的设置时间。论文提出了一个基于Google Gemini 2.0 Flash大语言模型的聊天机器人，能够自动生成并求解二维有限元涡流模型。该系统使用Python协调工作流组件，支持用户定义具有可变位置和数量的圆形截面导体几何形状，并可定义自定义后处理程序。研究展示了如何通过LLM驱动的自动化工作流程，将自然语言指令转化为具体的仿真模型设置和求解步骤，从而加速专业科学计算任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

This work addresses the question of how generative artificial intelligence can be used to reduce the time required to set up electromagnetic simulation models. A chatbot based on a large language model is presented, enabling the automated generation of simulation models with various functional enhancements. A chatbot-driven workflow based on the large language model Google Gemini 2.0 Flash automatically generates and solves two-dimensional finite element eddy current models using Gmsh and GetDP. Python is used to coordinate and automate interactions between the workflow components. The study considers conductor geometries with circular cross-sections of variable position and number. Additionally, users can define custom post-processing routines and receive a concise summary of model information and simulation results. Each functional enhancement includes the corresponding architectural modifications and illustrative case studies.

</details>

---

### 72. [Small Language Models for Efficient Agentic Tool Calling: Outperforming Large Models with Targeted Fine-tuning](https://arxiv.org/abs/2512.15943)

**基本信息**

- 🔗 arXiv: [`2512.15943`](https://arxiv.org/abs/2512.15943)
- 👥 作者: Polaris Jhandi, Owais Kazi, Shreyas Subramanian 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.15943.pdf)

**💡 相关性分析**

满足标准3：论文的核心是对比和优化大型语言模型与小型语言模型在具体任务（如工具调用）上的应用策略。虽然不直接针对化学或质谱，但其关于模型缩放、效率优化、领域适应微调以及工具调用能力的深入讨论，与构建高效、实用的“化学大模型”或智能分析工具所面临的技术挑战（模型选型、部署成本、性能平衡）高度相关，提供了重要的技术视角和展望。

**📖 中文摘要**

本文探讨了在生成式AI规模化应用中，用小型语言模型（SLM）替代大型语言模型（LLM）以实现成本优化和操作效率的可行性。作者通过针对性的微调（使用Hugging Face TRL的SFT训练器），训练了一个领域适应的SLM（基于facebook/opt-350m模型）来执行文档摘要、问答和结构化数据解释等任务。实验结果表明，微调后的SLM在ToolBench评估中取得了77.55%的通过率，显著超过了包括ChatGPT-CoT、ToolLLaMA在内的多个基线模型。研究强调了通过精心设计和针对性训练，SLM可以显著降低生成式AI的生产系统集成门槛。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

As organizations scale adoption of generative AI, model cost optimization and operational efficiency have emerged as critical factors determining sustainability and accessibility. While Large Language Models (LLMs) demonstrate impressive capabilities across diverse tasks, their extensive computational requirements make them cost-prohibitive for routine enterprise use. This limitation motivates the exploration of Small Language Models (SLMs), which can deliver comparable performance in targeted applications while drastically reducing infrastructure overhead (Irugalbandara et al., 2023). In this work, we investigate the feasibility of replacing LLM-driven workflows with optimized SLMs. We trained a domain-adapted SLM to execute representative tasks traditionally handled by LLMs, such as document summarization, query answering, and structured data interpretation. As part of the experiment, we investigated the fine-tuning of facebook/opt-350m model (single epoch only) using the Hugging Face TRL (Transformer Reinforcement Learning), specifically the Supervised Fine-Tuning (SFT) trainer. The OPT-350M model was released by Meta AI in 2022 as part of the OPT (Open Pretrained Transformer) family of models. Similar studies demonstrate that even models at the 350M parameter scale can meaningfully contribute to instruction-tuning pipelines (Mekala et al., 2024). Experimental results demonstrated that our fine-tuned SLM achieves exceptional performance with a 77.55\% pass rate on ToolBench evaluation, significantly outperforming all baseline models including ChatGPT-CoT (26.00\%), ToolLLaMA-DFS (30.18\%), and ToolLLaMA-CoT (16.27\%). These findings emphasize that thoughtful design and targeted training of SLMs can significantly lower barriers to adoption, enabling cost-effective, large-scale integration of generative AI into production systems.

</details>

---

### 73. [DEER: A Benchmark for Evaluating Deep Research Agents on Expert Report Generation](https://arxiv.org/abs/2512.17776)

**基本信息**

- 🔗 arXiv: [`2512.17776`](https://arxiv.org/abs/2512.17776)
- 👥 作者: Janghoon Han, Heegyu Kim, Changho Lee 等9人
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.17776.pdf)

**💡 相关性分析**

满足标准2和3：2. 数据资源相关：论文提出了一个用于评估AI生成研究报告的新基准（DEER），包括系统的评估分类法、指南和验证架构。这为评估“化学大模型”在生成化学研究报告、文献综述或数据分析结论方面的能力提供了潜在的评估框架和工具资源。3. 综述展望相关：论文对当前基于LLM的深度研究系统的能力、局限性进行了深入分析和展望，这些讨论对于思考如何开发和应用“化学大模型”进行可靠的科学研究（如自动文献综述、实验报告生成）具有重要的参考价值。

**📖 中文摘要**

本文提出了DEER基准，用于评估基于大语言模型的深度研究智能体在生成专家级报告方面的能力。该基准系统化了评估标准，提出了一个包含7个维度、25个子维度、101个细粒度评分项的专家开发分类法，并提供了任务特定的专家评估指南以支持基于LLM的评判。此外，论文还提出了一种声明验证架构，用于验证报告中引用和未引用的声明，并量化证据质量。实验表明，当前的深度研究系统可以生成结构合理、引用外部证据的报告，但在满足专家级用户请求和实现逻辑完整性方面仍有改进空间。DEER基准使得系统优劣势可解释，并为改进提供了诊断信号。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Recent advances in large language models have enabled deep research systems that generate expert-level reports through multi-step reasoning and evidence-based synthesis. However, evaluating such reports remains challenging: report quality is multifaceted, making it difficult to determine what to assess and by what criteria; LLM-based judges may miss errors that require domain expertise to identify; and because deep research relies on retrieved evidence, report-wide claim verification is also necessary. To address these issues, we propose DEER, a benchmark for evaluating expert-level deep research reports. DEER systematizes evaluation criteria with an expert-developed taxonomy (7 dimensions, 25 subdimensions) operationalized as 101 fine-grained rubric items. We also provide task-specific Expert Evaluation Guidance to support LLM-based judging. Alongside rubric-based assessment, we propose a claim verification architecture that verifies both cited and uncited claims and quantifies evidence quality. Experiments show that while current deep research systems can produce structurally plausible reports that cite external evidence, there is room for improvement in fulfilling expert-level user requests and achieving logical completeness. Beyond simple performance comparisons, DEER makes system strengths and limitations interpretable and provides diagnostic signals for improvement.

</details>

---

### 74. [CovertComBench: A First Domain-Specific Testbed for LLMs in Wireless Covert Communication](https://arxiv.org/abs/2601.18315)

**基本信息**

- 🔗 arXiv: [`2601.18315`](https://arxiv.org/abs/2601.18315)
- 👥 作者: Zhaozhi Liu, Jiaxin Chen, Yuanai Xie 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.18315.pdf)

**💡 相关性分析**

满足标准2和3：2. 数据资源相关：论文提出了一个专门用于评估LLM在特定科学工程领域（隐蔽通信）问题解决能力的基准测试（CovertComBench）。这为评估“化学大模型”或“质谱结构推理”模型在解决类似需要严格理论约束和数值优化的化学问题（如谱图解析、分子性质优化）上的能力，提供了一个方法论范例和潜在的评估工具思路。3. 综述展望相关：论文通过系统评估，对LLM在解决复杂工程优化问题上的当前能力和局限性进行了重要讨论，并指出了未来研究方向（如外部工具增强）。这些见解对于展望“化学大模型”在解决类似复杂化学问题（如逆合成规划、谱图解析）中的角色和开发路径具有相关性。

**📖 中文摘要**

本文介绍了CovertComBench，这是首个用于评估大语言模型在无线隐蔽通信中能力的领域特定测试平台。隐蔽通信需要在严格的检测理论约束（如KL散度限制）下优化传输效用，这与传统的吞吐量最大化不同。该基准旨在统一评估LLM在整个隐蔽通信流程中的能力，涵盖概念理解（MCQ）、优化推导（ODQ）和代码生成（CGQ）。评估揭示了显著的性能差距：LLM在概念识别（81%）和代码实现（83%）上准确率很高，但在保障安全所需的高阶数学推导方面表现不佳（18%-55%）。这表明当前LLM更适合作为实现助手，而非安全约束优化问题的自主求解器。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

The integration of Large Language Models (LLMs) into wireless networks presents significant potential for automating system design. However, unlike conventional throughput maximization, Covert Communication (CC) requires optimizing transmission utility under strict detection-theoretic constraints, such as Kullback-Leibler divergence limits. Existing benchmarks primarily focus on general reasoning or standard communication tasks and do not adequately evaluate the ability of LLMs to satisfy these rigorous security constraints. To address this limitation, we introduce CovertComBench, a unified benchmark designed to assess LLM capabilities across the CC pipeline, encompassing conceptual understanding (MCQs), optimization derivation (ODQs), and code generation (CGQs). Furthermore, we analyze the reliability of automated scoring within a detection-theoretic ``LLM-as-Judge'' framework. Extensive evaluations across state-of-the-art models reveal a significant performance discrepancy. While LLMs achieve high accuracy in conceptual identification (81%) and code implementation (83%), their performance in the higher-order mathematical derivations necessary for security guarantees ranges between 18% and 55%. This limitation indicates that current LLMs serve better as implementation assistants rather than autonomous solvers for security-constrained optimization. These findings suggest that future research should focus on external tool augmentation to build trustworthy wireless AI systems.

</details>

---

### 75. [MolCrystalFlow: Molecular Crystal Structure Prediction via Flow Matching](https://arxiv.org/abs/2602.16020)

**基本信息**

- 🔗 arXiv: [`2602.16020`](https://arxiv.org/abs/2602.16020)
- 👥 作者: Cheng Zeng, Harry W. Sullivan, Thomas Egg 等11人
- 📄 PDF: [下载](https://arxiv.org/pdf/2602.16020.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于分子晶体结构预测的生成模型（MolCrystalFlow）。这直接属于化学信息学领域，并涉及利用机器学习/人工智能模型（化学大模型的一个子领域）来生成和预测化学结构，与‘化学大模型’主题高度相关。

**📖 中文摘要**

本文提出了MolCrystalFlow，一个基于流匹配的生成模型，用于预测分子晶体结构。分子晶体结构预测是计算化学中的一个重大挑战，涉及复杂的分子内和分子间相互作用。该工作将生成建模扩展到完全周期性的分子晶体，通过将分子作为刚体嵌入，并联合学习晶格矩阵、分子取向和质心位置。质心和取向在其原生黎曼流形上表示，允许构建测地线流和尊重几何对称性的图神经网络操作。该模型在开源分子晶体数据集上进行了基准测试，并展示了与通用机器学习势的集成，以加速分子晶体结构预测。这项工作直接与化学信息学中利用生成模型进行分子和材料结构发现的核心主题相关，特别是为复杂的周期性系统提供了一种新的数据驱动生成方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Molecular crystal structure prediction represents a grand challenge in computational chemistry due to large sizes of constituent molecules and complex intra- and intermolecular interactions. While generative modeling has revolutionized structure discovery for molecules, inorganic solids, and metal-organic frameworks, extending such approaches to fully periodic molecular crystals is still elusive. Here, we present MolCrystalFlow, a flow-based generative model for molecular crystal structure prediction. The framework disentangles intramolecular complexity from intermolecular packing by embedding molecules as rigid bodies and jointly learning the lattice matrix, molecular orientations, and centroid positions. Centroids and orientations are represented on their native Riemannian manifolds, allowing geodesic flow construction and graph neural network operations that respects geometric symmetries. We benchmark our model against a state-of-the-art generative model (MOFFlow) for large-size periodic crystals and a rule-based structure generation method (Genarris) on two open-source molecular crystal datasets. MolCrystalFlow outperforms MOFFlow while achieving competitive performance against Genarris. We also demonstrate an integration of MolCrystalFlow model with universal machine learning potential to accelerate molecular crystal structure prediction, paving the way for data-driven generative discovery of molecular crystals.

</details>

---

### 76. [Timer-S1: A Billion-Scale Time Series Foundation Model with Serial Scaling](https://arxiv.org/abs/2603.04791)

**基本信息**

- 🔗 arXiv: [`2603.04791`](https://arxiv.org/abs/2603.04791)
- 👥 作者: Yong Liu, Xingjian Su, Shiyu Wang 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04791.pdf)

**💡 相关性分析**

满足标准1：论文的核心内容是构建和扩展一个大规模的时间序列基础模型（Timer-S1）。这属于‘大模型’在特定科学计算领域（时间序列）的应用实例。其关于模型架构（MoE）、数据策划和训练流程的讨论，对于理解和构建其他领域的‘化学大模型’具有重要的参考价值。

**📖 中文摘要**

本文介绍了Timer-S1，一个强大的时间序列基础模型，采用混合专家（MoE）架构，总参数量83亿，每个token激活参数0.75亿，上下文长度11.5K。为了克服现有预训练时间序列基础模型的可扩展性瓶颈，该工作在模型架构、数据集和训练流程三个维度上进行了序列缩放。模型集成了稀疏的TimeMoE块和通用的TimeSTP块，用于序列令牌预测（STP）——一种遵循预测序列本质的通用训练目标。该研究还策划了包含一万亿时间点的语料库TimeBench，并应用了细致的数据增强以减轻预测偏差。在GIFT-Eval排行榜上的评估表明，Timer-S1作为预训练模型达到了最先进的预测性能。虽然主要应用于时间序列预测，但其作为大规模预训练基础模型（MoE架构）的开发范式、数据处理和训练策略，为构建和扩展领域特定的大模型（包括潜在的化学或质谱领域模型）提供了方法论参考和洞见。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

We introduce Timer-S1, a strong Mixture-of-Experts (MoE) time series foundation model with 8.3B total parameters, 0.75B activated parameters for each token, and a context length of 11.5K. To overcome the scalability bottleneck in existing pre-trained time series foundation models, we perform Serial Scaling in three dimensions: model architecture, dataset, and training pipeline. Timer-S1 integrates sparse TimeMoE blocks and generic TimeSTP blocks for Serial-Token Prediction (STP), a generic training objective that adheres to the serial nature of forecasting. The proposed paradigm introduces serial computations to improve long-term predictions while avoiding costly rolling-style inference and pronounced error accumulation in the standard next-token prediction. Pursuing a high-quality and unbiased training dataset, we curate TimeBench, a corpus with one trillion time points, and apply meticulous data augmentation to mitigate predictive bias. We further pioneer a post-training stage, including continued pre-training and long-context extension, to enhance short-term and long-context performance. Evaluated on the large-scale GIFT-Eval leaderboard, Timer-S1 achieves state-of-the-art forecasting performance, attaining the best MASE and CRPS scores as a pre-trained model. Timer-S1 will be released to facilitate further research.

</details>

---

### 77. [LLM-Grounded Explainable AI for Supply Chain Risk Early Warning via Temporal Graph Attention Networks](https://arxiv.org/abs/2603.04818)

**基本信息**

- 🔗 arXiv: [`2603.04818`](https://arxiv.org/abs/2603.04818)
- 👥 作者: Zhiming Xue, Yujue Wang, Menghao Huo
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.04818.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及开发一个结合了图神经网络和大型语言模型（LLM）的框架，用于风险预测和解释。LLM是‘化学大模型’在自然语言处理领域的典型代表。该工作展示了如何将大模型与领域特定模型（TGAT）结合，进行结构化推理和生成，这种方法论可以迁移到化学信息学中，例如结合分子图神经网络和LLM进行性质预测或反应推理。

**📖 中文摘要**

本文提出了一个证据接地的框架，用于供应链风险早期预警，该框架结合了时序图注意力网络（TGAT）和结构化大语言模型（LLM）推理模块，共同执行供应链瓶颈预测和可信的自然语言风险解释。以海运枢纽作为全球供应链节点的代表性案例研究，从自动识别系统（AIS）广播构建每日空间图，并通过基于注意力的消息传递对节点间交互进行建模。TGAT预测器捕捉时空风险动态，而模型内部证据（包括特征z分数和注意力衍生的邻居影响）被转化为结构化提示，以约束LLM推理到可验证的模型输出。为了评估解释的可靠性，引入了一个方向一致性验证协议，定量衡量生成的风险叙述与底层统计证据之间的一致性。实验表明，该框架在预测性能的同时，实现了可解释和可审计的风险报告。这项工作展示了将LLM生成与图模型证据相结合，以实现可解释人工智能。虽然应用领域是供应链，但其核心方法——将领域知识/数据与大型语言模型（作为大模型的一种）结合进行推理和解释——与利用大模型解决复杂科学问题（如化学信息学中的结构推理）的思路相通。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Disruptions at critical logistics nodes pose severe risks to global supply chains, yet existing risk prediction systems typically prioritize forecasting accuracy without providing operationally interpretable early warnings. This paper proposes an evidence-grounded framework that jointly performs supply chain bottleneck prediction and faithful natural-language risk explanation by coupling a Temporal Graph Attention Network (TGAT) with a structured large language model (LLM) reasoning module. Using maritime hubs as a representative case study for global supply chain nodes, daily spatial graphs are constructed from Automatic Identification System (AIS) broadcasts, where inter-node interactions are modeled through attention-based message passing. The TGAT predictor captures spatiotemporal risk dynamics, while model-internal evidence -- including feature z-scores and attention-derived neighbor influence -- is transformed into structured prompts that constrain LLM reasoning to verifiable model outputs. To evaluate explanatory reliability, we introduce a directional-consistency validation protocol that quantitatively measures agreement between generated risk narratives and underlying statistical evidence. Experiments on six months of real-world logistics data demonstrate that the proposed framework outperforms baseline models, achieving a test AUC of 0.761, AP of 0.344, and recall of 0.504 under a strict chronological split while producing early warning explanations with 99.6\% directional consistency. Results show that grounding LLM generation in graph-model evidence enables interpretable and auditable risk reporting without sacrificing predictive performance. The framework provides a practical pathway toward operationally deployable explainable AI for supply chain risk early warning and resilience management.

</details>

---

### 78. [Censored LLMs as a Natural Testbed for Secret Knowledge Elicitation](https://arxiv.org/abs/2603.05494)

**基本信息**

- 🔗 arXiv: [`2603.05494`](https://arxiv.org/abs/2603.05494)
- 👥 作者: Helena Casademunt, Bartosz Cywiński, Khoi Tran 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05494.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是评估和比较从大型语言模型（LLMs）中引出被隐藏或压制的知识（秘密知识）的各种技术。LLM是‘大模型’的核心类型之一。该研究直接探讨了大模型的行为控制、知识访问和可靠性问题，这些是构建和部署可信赖的化学或科学领域大模型时必须考虑的关键方面。

**📖 中文摘要**

本文研究了经过审查的大型语言模型（LLMs）作为秘密知识引出的自然测试平台。这些来自中国开发者的开源权重LLMs被训练来审查政治敏感话题，因此经常在相关主题上产生虚假陈述，但偶尔也能正确回答，表明它们拥有被训练压制的知识。利用此作为测试平台，作者评估了一系列引出和谎言检测技术。对于诚实性引出，研究发现无聊天模板的采样、少样本提示以及在通用诚实数据上的微调最能可靠地增加真实回答。对于谎言检测，提示被审查模型对其自身回答进行分类的性能接近未审查模型的上限，而在无关数据上训练的线性探针提供了更便宜的替代方案。最强的诚实性引出技术也能迁移到包括DeepSeek R1在内的前沿开源权重模型。值得注意的是，没有技术能完全消除错误回答。这项工作系统地评估了如何从可能隐藏知识的大模型中引出真实信息，并比较了不同技术的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Large language models sometimes produce false or misleading responses. Two approaches to this problem are honesty elicitation -- modifying prompts or weights so that the model answers truthfully -- and lie detection -- classifying whether a given response is false. Prior work evaluates such methods on models specifically trained to lie or conceal information, but these artificial constructions may not resemble naturally-occurring dishonesty. We instead study open-weights LLMs from Chinese developers, which are trained to censor politically sensitive topics: Qwen3 models frequently produce falsehoods about subjects like Falun Gong or the Tiananmen protests while occasionally answering correctly, indicating they possess knowledge they are trained to suppress. Using this as a testbed, we evaluate a suite of elicitation and lie detection techniques. For honesty elicitation, sampling without a chat template, few-shot prompting, and fine-tuning on generic honesty data most reliably increase truthful responses. For lie detection, prompting the censored model to classify its own responses performs near an uncensored-model upper bound, and linear probes trained on unrelated data offer a cheaper alternative. The strongest honesty elicitation techniques also transfer to frontier open-weights models including DeepSeek R1. Notably, no technique fully eliminates false responses. We release all prompts, code, and transcripts.

</details>

---

### 79. [Towards Robust Retrieval-Augmented Generation Based on Knowledge Graph: A Comparative Analysis](https://arxiv.org/abs/2603.05698)

**基本信息**

- 🔗 arXiv: [`2603.05698`](https://arxiv.org/abs/2603.05698)
- 👥 作者: Hazem Amamou, Stéphane Gagnon, Alan Davoust 等4人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.05698.pdf)

**💡 相关性分析**

满足标准1和3：论文的核心研究内容是比较和增强基于知识图谱的检索增强生成（GraphRAG）系统的鲁棒性。RAG是使大模型（如LLMs）能够利用外部知识库的关键技术。这项工作直接涉及大模型的应用架构（RAG）的评估与改进。同时，它对不同RAG方法在多种鲁棒性场景下的比较分析，也包含了重要的相关讨论，可作为该主题的微型综述或技术分析。

**📖 中文摘要**

本文使用检索增强生成基准（RGB）来评估基于知识图谱的检索系统（GraphRAG）与基线RAG系统在噪声鲁棒性、信息整合、负面拒绝和反事实鲁棒性四种场景下的性能。研究对GraphRAG进行了三种定制化改进以提升鲁棒性。结果表明，与RGB基线相比有所改进，并为设计更可靠的现实世界RAG系统提供了见解。检索增强生成（RAG）是大语言模型（LLMs）扩展知识和减少幻觉的关键技术。虽然应用场景是通用问答，但RAG架构本身是构建领域专家系统（如化学知识问答、质谱解析辅助系统）的核心技术。本文对基于知识图谱的RAG进行的鲁棒性评估和改进，为在化学信息学等领域构建更可靠的、基于大模型的检索推理系统提供了直接的技术参考和评估思路。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Retrieval-Augmented Generation (RAG) was introduced to enhance the capabilities of Large Language Models (LLMs) beyond their encoded prior knowledge. This is achieved by providing LLMs with an external source of knowledge, which helps reduce factual hallucinations and enables access to new information not available during pretraining. However, inconsistent retrieved information can negatively affect LLM responses. The Retrieval-Augmented Generation Benchmark (RGB) was introduced to evaluate the robustness of RAG systems under such conditions. In this work, we use the RGB corpus to evaluate LLMs in four scenarios: noise robustness, information integration, negative rejection, and counterfactual robustness. We perform a comparative analysis between the RGB RAG baseline and GraphRAG, a knowledge graph based retrieval system. We test three GraphRAG customizations to improve robustness. Results show improvements over the RGB baseline and provide insights for designing more reliable RAG systems for real world scenarios.

</details>

---

### 80. [Property-driven Protein Inverse Folding With Multi-Objective Preference Alignment](https://arxiv.org/abs/2603.06748)

**基本信息**

- 🔗 arXiv: [`2603.06748`](https://arxiv.org/abs/2603.06748)
- 👥 作者: Xiaoyang Hou, Junqi Liu, Chence Shi 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.06748.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个框架（ProtAlign），用于对齐和优化预训练的蛋白质逆折叠模型（如ProteinMPNN），使其生成同时满足结构要求和多种生物物理属性的蛋白质序列。蛋白质逆折叠是化学信息学和计算生物学中的一个核心问题，而使用预训练模型并进行偏好对齐微调，正是‘化学大模型’在特定下游任务上应用和优化的典型案例。

**📖 中文摘要**

本文介绍了ProtAlign，一个多目标偏好对齐框架，用于微调预训练的蛋白质逆折叠模型，在保持结构保真度的同时满足多样的可开发性目标（如溶解度、热稳定性和表达量）。蛋白质序列设计需要在可设计性（恢复目标骨架的能力）与多个常相互竞争的可开发性属性之间取得平衡。ProtAlign采用半在线直接偏好优化策略，具有灵活的偏好边界，以减轻竞争目标之间的冲突，并利用计算机属性预测器构建偏好对。应用于广泛使用的ProteinMPNN骨架，所得模型MoMPNN在包括CATH 4.3晶体结构、从头生成的骨架和真实世界结合剂设计场景在内的任务中，增强了可开发性且未损害可设计性。这项工作展示了如何通过对齐学习将领域知识（生物物理属性）注入到预训练的生成模型中，从而生成更符合实际应用需求的蛋白质序列。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Protein sequence design must balance designability, defined as the ability to recover a target backbone, with multiple, often competing, developability properties such as solubility, thermostability, and expression. Existing approaches address these properties through post hoc mutation, inference-time biasing, or retraining on property-specific subsets, yet they are target dependent and demand substantial domain expertise or careful hyperparameter tuning. In this paper, we introduce ProtAlign, a multi-objective preference alignment framework that fine-tunes pretrained inverse folding models to satisfy diverse developability objectives while preserving structural fidelity. ProtAlign employs a semi-online Direct Preference Optimization strategy with a flexible preference margin to mitigate conflicts among competing objectives and constructs preference pairs using in silico property predictors. Applied to the widely used ProteinMPNN backbone, the resulting model MoMPNN enhances developability without compromising designability across tasks including sequence design for CATH 4.3 crystal structures, de novo generated backbones, and real-world binder design scenarios, making it an appealing framework for practical protein sequence design.

</details>

---

### 81. [High-Fidelity Medical Shape Generation via Skeletal Latent Diffusion](https://arxiv.org/abs/2603.07504)

**基本信息**

- 🔗 arXiv: [`2603.07504`](https://arxiv.org/abs/2603.07504)
- 👥 作者: Guoqing Zhang, Jingyun Yang, Siqi Chen 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07504.pdf)

**💡 相关性分析**

满足标准2：论文提出了一个用于医学形状生成的新框架，并构建并发布了大规模数据集MedSDF。虽然应用领域是医学影像，但其核心方法——基于扩散模型的3D形状生成、结合结构先验（骨架）的表示学习、以及大规模高质量数据集的创建——为化学信息学中分子3D构象生成、材料结构生成等任务提供了直接可借鉴的技术路线和潜在的数据资源构建思路。

**📖 中文摘要**

本文提出了一个骨骼潜在扩散框架，用于高效、高保真度的医学形状生成。该框架明确结合了结构先验，以解决解剖结构几何复杂性和拓扑可变性带来的挑战。作者引入了一个形状自动编码器，其中编码器通过可微分骨架化模块捕获全局几何信息，并将局部表面特征聚合为形状潜在表示；解码器则在稀疏采样的坐标上预测相应的隐式场。新形状通过潜在空间扩散模型生成，随后进行神经隐式解码和网格提取。为了解决医学形状数据有限的问题，作者构建了一个大规模数据集MedSDF，包含多个解剖类别的表面点云和对应的有符号距离场。在MedSDF和血管数据集上的大量实验表明，该方法在保持更高计算效率的同时，实现了卓越的重建和生成质量。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Anatomy shape modeling is a fundamental problem in medical data analysis. However, the geometric complexity and topological variability of anatomical structures pose significant challenges to accurate anatomical shape generation. In this work, we propose a skeletal latent diffusion framework that explicitly incorporates structural priors for efficient and high-fidelity medical shape generation. We introduce a shape auto-encoder in which the encoder captures global geometric information through a differentiable skeletonization module and aggregates local surface features into shape latents, while the decoder predicts the corresponding implicit fields over sparsely sampled coordinates. New shapes are generated via a latent-space diffusion model, followed by neural implicit decoding and mesh extraction. To address the limited availability of medical shape data, we construct a large-scale dataset, \textit{MedSDF}, comprising surface point clouds and corresponding signed distance fields across multiple anatomical categories. Extensive experiments on MedSDF and vessel datasets demonstrate that the proposed method achieves superior reconstruction and generation quality while maintaining a higher computational efficiency compared with existing approaches. Code is available at: this https URL .

</details>

---

### 82. [TableMind++: An Uncertainty-Aware Programmatic Agent for Tool-Augmented Table Reasoning](https://arxiv.org/abs/2603.07528)

**基本信息**

- 🔗 arXiv: [`2603.07528`](https://arxiv.org/abs/2603.07528)
- 👥 作者: Mingyue Cheng, Shuo Yu, Chuang Jiang 等8人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07528.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个用于表格推理的、不确定性感知的程序化智能体（TableMind++）。该智能体基于大型语言模型（LLMs），并通过训练（SFT和RL）使其能够规划、使用工具（程序）和反思。这属于构建面向特定领域（表格）的、基于大模型的自主智能体（Agent）。其关于缓解LLM幻觉、不确定性量化、以及工具使用的设计，对于构建化学或质谱领域的推理智能体（例如，用于解析质谱数据或规划化学合成的智能体）具有重要的方法论参考价值。

**📖 中文摘要**

本文介绍了TableMind++，一个不确定性感知的程序化智能体，用于工具增强的表格推理。表格推理要求模型同时执行语义理解和精确的数值运算。TableMind++在之前TableMind工作的基础上，通过引入新颖的不确定性感知推理框架来缓解幻觉问题。具体包括：基于记忆的计划剪枝，以检索历史轨迹来验证和过滤逻辑有缺陷的计划，解决认知不确定性；基于置信度的动作细化，监控令牌级概率以检测和自校正句法噪声，缓解偶然不确定性；以及双权重轨迹聚合，从多个推理路径中合成稳健的共识。在多样化基准测试上的大量实验表明，TableMind++持续优于之前的基线和专有模型，验证了将自主训练与不确定性量化相结合的有效性。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Table reasoning requires models to jointly perform semantic understanding and precise numerical operations. Most existing methods rely on a single-turn reasoning paradigm over tables which suffers from context overflow and weak numerical sensitivity. To address these limitations, we previously proposed TableMind as a tuning-based autonomous programmatic agent that simulates human-like interaction within a lightweight large language model (LLM). TableMind internalizes planning, action, and reflection through a two-stage training strategy involving supervised fine-tuning (SFT) on filtered high-quality data and reinforcement learning (RL) via a multi-perspective reward and the Rank-Aware Policy Optimization (RAPO) algorithm. While TableMind establishes a solid foundation for programmatic agents, the inherent stochasticity of LLMs remains a critical challenge that leads to hallucinations. In this paper, we extend this foundation to TableMind++ by introducing a novel uncertainty-aware inference framework to mitigate hallucinations. Specifically, we propose memory-guided plan pruning to retrieve historical trajectories for validating and filtering out logically flawed plans to address epistemic uncertainty. To ensure execution precision, we introduce confidence-based action refinement which monitors token-level probabilities to detect and self-correct syntactic noise for aleatoric uncertainty mitigation. Finally, we employ dual-weighted trajectory aggregation to synthesize a robust consensus from multiple reasoning paths. Extensive experiments on diverse benchmarks demonstrate that TableMind++ consistently outperforms previous baselines and proprietary models to validate the effectiveness of integrating autonomous training with uncertainty quantification. Our code is available.

</details>

---

### 83. [Designing probabilistic AI monsoon forecasts to inform agricultural decision-making](https://arxiv.org/abs/2603.07893)

**基本信息**

- 🔗 arXiv: [`2603.07893`](https://arxiv.org/abs/2603.07893)
- 👥 作者: Colin Aitken, Rajat Masiwal, Adam Marchakitus 等10人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.07893.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是开发一个结合了AI天气预测模型和统计模型的混合系统，用于生成服务于农业决策的季风预报。AI天气预测模型是地球科学领域的大模型应用。这项工作展示了如何将大模型（AI预测）与领域特定模型（统计模型）和决策理论框架结合，解决现实世界的高风险决策问题。这种“大模型+领域知识+决策支持”的范式，与利用化学大模型辅助实验设计或风险评估的思路高度相关。

**📖 中文摘要**

本文介绍了一个决策理论框架，用于在设计预测者无法规定最优行动（因为农民的情况各异）的情况下设计有用的预测。并将此框架应用于季风降雨季节性开始这一案例，这是许多热带国家种植决策和农业投资的关键日期。作者开发了一个系统，通过将系统基准测试的人工智能（AI）天气预测模型与一个新的“演化农民期望”统计模型相结合，来定制符合该框架要求的预测。该统计模型应用贝叶斯推理于历史观测，以预测整个季节中首次发生事件的时间变化概率。混合系统在更长提前期上产生了比其组件或任何多模型平均更熟练的印度季风预测。2025年，该系统在一个政府主导的项目中投入业务运行，向3800万印度农民提供次季节季风开始预报。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Hundreds of millions of farmers make high-stakes decisions under uncertainty about future weather. Forecasts can inform these decisions, but available choices and their risks and benefits vary between farmers. We introduce a decision-theory framework for designing useful forecasts in settings where the forecaster cannot prescribe optimal actions because farmers' circumstances are heterogeneous. We apply this framework to the case of seasonal onset of monsoon rains, a key date for planting decisions and agricultural investments in many tropical countries. We develop a system for tailoring forecasts to the requirements of this framework by blending systematically benchmarked artificial intelligence (AI) weather prediction models with a new "evolving farmer expectations" statistical model. This statistical model applies Bayesian inference to historical observations to predict time-varying probabilities of first-occurrence events throughout a season. The blended system yields more skillful Indian monsoon forecasts at longer lead times than its components or any multi-model average. In 2025, this system was deployed operationally in a government-led program that delivered subseasonal monsoon onset forecasts to 38 million Indian farmers, skillfully predicting that year's early-summer anomalous dry period. This decision-theory framework and blending system offer a pathway for developing climate adaptation tools for large vulnerable populations around the world.

</details>

---

### 84. [Adaptive Loops and Memory in Transformers: Think Harder or Know More?](https://arxiv.org/abs/2603.08391)

**基本信息**

- 🔗 arXiv: [`2603.08391`](https://arxiv.org/abs/2603.08391)
- 👥 作者: Markus Frey, Behzad Shomali, Ali Hamza Bashir 等5人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08391.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是探索和评估通过架构修改（自适应循环和记忆库）来增强Transformer模型（一种基础的大模型架构）推理能力的方法。这直接属于大模型架构创新的研究，旨在提高其计算效率和复杂任务（如数学推理）的性能。这些架构探索对于设计下一代更高效、更强大的化学领域大模型具有启发意义。

**📖 中文摘要**

本文研究了同时具有自适应逐层循环（每个Transformer块通过学习的停止机制迭代其隐藏状态）和门控记忆库的Transformer模型。研究发现，循环主要有利于数学推理，而记忆库有助于在常识任务上恢复性能。结合这两种机制产生的模型在数学基准测试上优于FLOP匹配的基线模型。对模型内部的分析揭示了层的专业化：早期层学习最小化循环并稀疏访问记忆，而后期层则更频繁地进行两者。这项工作探索了通过改变模型架构（引入循环和记忆）来增强Transformer模型推理能力的方法，而不是仅仅依赖思维链提示。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Chain-of-thought (CoT) prompting enables reasoning in language models but requires explicit verbalization of intermediate steps. Looped transformers offer an alternative by iteratively refining representations within hidden states. This parameter efficiency comes at a cost, as looped models lack the storage capacity of deeper models which use unique weights per layer. In this work, we investigate transformer models that feature both adaptive per-layer looping, where each transformer block learns to iterate its hidden state via a learned halting mechanism, and gated memory banks, that provide additional learned storage. We find that looping primarily benefits mathematical reasoning, while memory banks help recover performance on commonsense tasks compared to parameter and FLOP matched models. Combining both mechanisms yields a model that outperforms an iso-FLOP baseline, with three times the number of layers, across math benchmarks. Analysis of model internals reveals layer specialization: early layers learn to loop minimally and access memory sparingly, while later layers do both more heavily.

</details>

---

### 85. [PRISM: Streaming Human Motion Generation with Per-Joint Latent Decomposition](https://arxiv.org/abs/2603.08590)

**基本信息**

- 🔗 arXiv: [`2603.08590`](https://arxiv.org/abs/2603.08590)
- 👥 作者: Zeyu Ling, Qing Shuai, Teng Zhang 等6人
- 📄 PDF: [下载](https://arxiv.org/pdf/2603.08590.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容是提出并训练一个统一的、多功能的运动生成基础模型（PRISM）。这属于在特定模态（人体运动）上构建大模型（基础模型）的工作。其关于潜在空间结构化设计、多任务统一、以及长序列生成稳定性的创新，对于在化学信息学中构建类似的、能够处理多种任务（如分子生成、反应预测、性质优化）的统一分子基础模型具有重要的参考价值。

**📖 中文摘要**

本文提出了PRISM，一个用于流式人体运动生成的结构化关节潜在分解框架。针对文本到运动生成的两个挑战：1）现有运动自编码器将每帧压缩成单个整体潜在向量，纠缠了轨迹和关节旋转；2）长序列生成中自回归方法的错误累积。PRISM的贡献包括：（1）关节因子化的运动潜在空间：每个身体关节占据自己的令牌，形成一个结构化的2D网格，由带有前向运动学监督的因果VAE压缩。这种潜在空间设计的简单改变显著提高了生成质量。（2）无噪声条件注入：每个潜在令牌携带自己的时间步嵌入，允许将条件帧作为干净令牌注入，而其余令牌被去噪。这使得文本到运动和姿态条件生成统一在单个模型中，并直接支持自回归片段链接以进行流式合成。通过这两个组件，作者训练了一个单一的运动生成基础模型，无缝处理文本到运动、姿态条件生成、自回归序列生成和叙事运动组合，在多个基准测试上达到了最先进水平。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Text-to-motion generation has advanced rapidly, yet two challenges persist. First, existing motion autoencoders compress each frame into a single monolithic latent vector, entangling trajectory and per-joint rotations in an unstructured representation that downstream generators struggle to model faithfully. Second, text-to-motion, pose-conditioned generation, and long-horizon sequential synthesis typically require separate models or task-specific mechanisms, with autoregressive approaches suffering from severe error accumulation over extended rollouts. We present PRISM, addressing each challenge with a dedicated contribution. (1) A joint-factorized motion latent space: each body joint occupies its own token, forming a structured 2D grid (time joints) compressed by a causal VAE with forward-kinematics supervision. This simple change to the latent space -- without modifying the generator -- substantially improves generation quality, revealing that latent space design has been an underestimated bottleneck. (2) Noise-free condition injection: each latent token carries its own timestep embedding, allowing conditioning frames to be injected as clean tokens (timestep0) while the remaining tokens are denoised. This unifies text-to-motion and pose-conditioned generation in a single model, and directly enables autoregressive segment chaining for streaming synthesis. Self-forcing training further suppresses drift in long rollouts. With these two components, we train a single motion generation foundation model that seamlessly handles text-to-motion, pose-conditioned generation, autoregressive sequential generation, and narrative motion composition, achieving state-of-the-art on HumanML3D, MotionHub, BABEL, and a 50-scenario user study.

</details>

---

### 86. [Molecular Fingerprints Are Strong Models for Peptide Function Prediction](https://arxiv.org/abs/2501.17901)

**基本信息**

- 🔗 arXiv: [`2501.17901`](https://arxiv.org/abs/2501.17901)
- 👥 作者: Jakub Adamczyk, Piotr Ludynia, Wojciech Czech
- 📄 PDF: [下载](https://arxiv.org/pdf/2501.17901.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容直接围绕化学信息学中的分子表示（分子指纹）及其在肽性质预测中的应用，这与“化学大模型”主题中关于分子表示和模型效率的讨论高度相关。

**📖 中文摘要**

本文研究了分子指纹在肽功能预测中的应用，挑战了传统观点，即预测肽性质需要建模长程分子相互作用（通常使用复杂的图神经网络或预训练Transformer）。作者通过132个数据集（包括LRGB和其他五个肽基准测试）的实验表明，使用基于计数的ECFP、拓扑扭转和RDKit指纹等简单、领域特定的分子指纹，结合LightGBM模型，可以实现最先进的预测精度。尽管这些指纹仅编码短程分子特征，但其性能优于GNN和基于Transformer的方法。控制实验（如序列打乱和氨基酸计数）证实，指纹虽然本质上是局部的，但足以实现稳健的肽性质预测。这项工作为化学信息学中的分子表示学习提供了新的视角，表明高效的分子指纹可以作为复杂模型的可行替代方案，用于肽相关的性质预测任务。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding peptide properties is often assumed to require modeling long-range molecular interactions, motivating the use of complex graph neural networks and pretrained transformers. Yet, whether such long-range dependencies are essential remains unclear. We investigate if simple, domain-specific molecular fingerprints can capture peptide function without these assumptions. Atomic-level representation aims to provide richer information than purely sequence-based models and better efficiency than structural ones. Across 132 datasets, including LRGB and five other peptide benchmarks, models using count-based ECFP, Topological Torsion, and RDKit fingerprints with LightGBM achieve state-of-the-art accuracy. Despite encoding only short-range molecular features, these models outperform GNNs and transformer-based approaches. Control experiments with sequence shuffling and amino acid counts confirm that fingerprints, though inherently local, suffice for robust peptide property prediction. Our results challenge the presumed necessity of long-range interaction modeling and highlight molecular fingerprints as efficient, interpretable, and computationally lightweight alternatives for peptide prediction.

</details>

---

### 87. [Enhancing Reconstruction Capability of Wavelet Transform Amorphous Radial Distribution Function via Machine Learning Assisted Parameter Tuning](https://arxiv.org/abs/2512.17245)

**基本信息**

- 🔗 arXiv: [`2512.17245`](https://arxiv.org/abs/2512.17245)
- 👥 作者: Deriyan Senjaya, Stephen Ekaputra Limantoro
- 📄 PDF: [下载](https://arxiv.org/pdf/2512.17245.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容涉及化学信息学中用于材料科学（非晶态材料）的机器学习方法（WT-RDF+），通过机器学习优化物理模型的参数，以改进结构表征，这与“化学大模型”主题中关于AI/ML在化学和材料科学中的应用密切相关。

**📖 中文摘要**

本研究针对非晶态材料原子结构分析的挑战，改进了基于物理的小波变换径向分布函数（WT-RDF）方法。WT-RDF能够可靠地重建二元（Ge0.25Se0.75）和三元Agx(Ge0.25Se0.75)100-x（x = 5, 10, 15, 20, 25）体系中的第一、第二径向分布函数（RDF）峰和整体曲线趋势，但其振幅精度存在局限，影响了配位数等定量分析。作者指出，WT-RDF的局限性源于参数（a, b, Kf, C, Λ）选择不当，这些参数本质上代表了非晶材料内的原子相互作用。为了解决这个问题，本研究通过机器学习辅助的参数优化（包括可学习参数优化、参数边界和选择性损失）来增强WT-RDF，提出了WT-RDF+框架。WT-RDF+提高了峰值重建的精度，并且在仅使用25%的二元数据集进行训练时，其性能优于基准机器学习模型（如径向基函数RBF和长短期记忆LSTM）。这些结果表明，WT-RDF+是Ge-Se和Ag-Ge-Se家族RDF重建的稳健可靠模型。这项工作展示了机器学习如何优化物理启发的模型参数，以改进对非晶材料的结构表征。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Understanding atomic structures is crucial, yet amorphous materials remain challenging due to their irregular and non-periodic nature. The Wavelet Transform Radial Distribution Function (WT-RDF) offers a physics-based framework for analyzing amorphous structures, reliably reconstructing the first and second Radial Distribution Function (RDF) peaks and overall curve trends in both binary (Ge 0.25 Se 0.75) and ternary Ag x(Ge 0.25 Se 0.75)100-x (x = 5, 10, 15, 20, 25) systems. Despite these strengths, WT-RDF shows limitations in amplitude accuracy, which affects quantitative analyses such as coordination numbers. The shortcoming arises from improper parameter (a, b, Kf, C, and {\Lambda})) selection, as the parameters intrinsically represent atomic interactions within amorphous materials. This study addresses the issue by optimizing WT-RDF parameters using a machine learning approach via learnable parameter optimization, parameter bounding, and selective loss, producing the enhanced WT-RDF+ framework. WT-RDF+ improves the precision of peak reconstructions and outperforms benchmark Machine Learning (ML) models, including Radial Basis Function (RBF) and Long Short-term Memory (LSTM), when trained on only 25% of the binary dataset. Specifically, the machine learning benchmarks are defined as regressors with radial distance r input and G(r) output taken from Ab Initio Molecular Dynamics (AIMD) RDF simulation, not the reduced structure factor SR(q) to G(r) inversions. These results demonstrate that WT-RDF+ is a robust and reliable model for RDF reconstruction of Ge-Se and Ag-Ge-Se family.

</details>

---

### 88. [An AI-powered Bayesian Generative Modeling Approach for Arbitrary Conditional Inference](https://arxiv.org/abs/2601.05355)

**基本信息**

- 🔗 arXiv: [`2601.05355`](https://arxiv.org/abs/2601.05355)
- 👥 作者: Qiao Liu, Wing Hung Wong
- 📄 PDF: [下载](https://arxiv.org/pdf/2601.05355.pdf)

**💡 相关性分析**

满足标准1：论文的核心研究内容提出了一种通用的AI生成建模框架（BGM），用于任意条件推断，这属于“化学大模型”主题中关于通用AI模型在科学数据（可能包括化学数据）分析中的应用范畴。

**📖 中文摘要**

本文提出了一种名为贝叶斯生成建模（BGM）的统一框架，用于解决现代数据分析中日益需要的任意条件推断问题，即给定观测变量X的任意分区（XA, XB），推断P(XB | XA)。现有方法要么局限于固定的条件结构，要么严重依赖于训练期间条件掩码的分布。BGM通过学习X的生成模型来解决这些限制，该模型通过随机迭代贝叶斯更新算法进行训练，其中模型参数和潜在变量被更新直至收敛。一旦训练完成，无需重新训练即可获得任何条件分布。实证表明，BGM在具有后验预测区间的情况下实现了优越的预测性能，证明单个学习模型可以作为具有原则性不确定性量化的条件预测的通用引擎。作者为随机迭代算法的收敛性、统计一致性和条件风险界限提供了理论保证。所提出的BGM框架利用现代AI捕捉变量之间的复杂关系，同时遵循贝叶斯原则，为现代数据科学中的广泛应用提供了一种有前景的方法。

<details>
<summary><b>🔍 查看原文摘要</b></summary>

Modern data analysis increasingly requires flexible conditional inference P(X_B | X_A) where (X_A, X_B) is an arbitrary partition of observed variable X. Existing approaches are either restricted to a fixed conditioning structure or depend strongly on the distribution of conditioning masks during training. To address these limitations, we introduce Bayesian generative modeling (BGM), a unified framework for arbitrary conditional inference. BGM learns a generative model of X via a stochastic iterative Bayesian updating algorithm in which model parameters and latent variables are updated until convergence. Once trained, any conditional distribution can be obtained without retraining. Empirically, BGM achieves superior predictive performance with posterior predictive intervals, demonstrating that a single learned model can serve as a universal engine for conditional prediction with principled uncertainty quantification. We provide theoretical guarantees for convergence of the stochastic iterative algorithm, statistical consistency, and conditional risk bounds. The proposed BGM framework leverages modern AI to capture complex relationships among variables while adhering to Bayesian principles, offering a promising approach for a wide range of applications in modern data science. Code for BGM is available at this https URL . Document of BGM is available at this https URL .

</details>

---

## 📊 数据统计
- 累计运行天数：24
- 累计论文数量：1822

## 📝 历史记录

> 暂无历史数据

